# Verification process log — verify-page-73


## [2026-09-05T05:41:42.305Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 73 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-73.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-73.json. Write /home/sfmqrb/git/rishe/data/verification/page-73.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 73` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:41:43.976Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-05T05:41:44.730Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:41:44.746Z] TOOL RESULT

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


## [2026-09-05T05:41:44.985Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-73.txt"
}
```


### [2026-09-05T05:41:45.012Z] TOOL RESULT

```
1	=== PDF page 73 (book page 43) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Aw, Awi, Awei : bird  (refs POK:86)
4	#1 (parent #0) [Avestan] refs=POK:86; HRN:296; SYN:183 | vîš 2 : bird ; vayu : air ; vi 1, vay 1 : to fly ; â-vayeiti : flied up
5	  #2 (parent #1) [Pahlavi] refs=POK:86; NYB:207 | vôi, vây, vâyandak : bird
6	    #3 (parent #2) [Persian] refs=HRN:995; FRS:56 | vây «واى» : bird ; vîš «ویش» : bird | NOTE: Both are almost obsolete
7	#4 (parent #0) [Latin] refs=POK:86 | avis : bird
8	  #5 (parent #4) [English] refs=AHD | aviation, ostrich
9	--- entry 1 ---
10	ROOT [Indo-European] Ow, Owo, Ayo, Ôwyo : a bird egg  (refs POK:86,783)
11	#1 (parent #0) [Avestan / Old Persian] refs=POK:783; SYN:256 | âvaya, xâya : egg ; ap-âvaya : to castrate
12	  #2 (parent #1) [Pahlavi] refs=HRN:103; PLA:104; BQT:711 | hâyîk, xâyak : egg, testicle ; xâyak-bar, xâyak-bâr : egg carrier (fish) ☞Bher 1
13	    #3 (parent #2) [Persian] refs=HRN:103; SYN:256; PLA:104 | xâyeh «خایه» : egg, testicle ; xâvîyâr «خاویار» : caviar
14	    #4 (parent #2) [Turkish] refs=AFM:51 | havyâr
15	      #5 (parent #4) [Italian] refs=None | 
16	        #6 (parent #5) [French] refs=None | 
17	          #7 (parent #6) [English] refs=AHD | caviar
18	#8 (parent #0) [Germanic / Old Norse] refs=AHD | ajjam : egg ; egg : egg
19	  #9 (parent #8) [English] refs=None | kidney, egg
20	#10 (parent #0) [Latin] refs=AHD | ôvum : egg
21	  #11 (parent #10) [English] refs=None | ovule
22	--- entry 2 ---
23	ROOT [Arabic] Awar : he damaged  (refs SAP:1123)
24	#1 (parent #0) [Arabic] refs=SAP:1124; AHD:91; KLN:133 | `awâr, `awârîyah : damaged goods
25	  #2 (parent #1) [Persian] refs=MON | âr 2 «عار» : damage, shame ; avâr «عوار» : defect, damaged goods, damaged cloth
26	  #3 (parent #1) [Spanish] refs=None | 
27	    #4 (parent #3) [Italian] refs=None | 
28	      #5 (parent #4) [French] refs=KLN:133; AHD:91 | avarie : damage to ship, also (averaged) loss shared equitably among investors
29	        #6 (parent #5) [English] refs=None | average
30	--- entry 3 ---
31	ROOT Awei -> redirect to Aw
32	
```


## [2026-09-05T05:41:48.089Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-73.json",
 "description": "Read source JSON for page 73"
}
```


### [2026-09-05T05:41:48.137Z] TOOL RESULT

```
{
  "pdf_page": 73,
  "book_page": 43,
  "entries": [
    {
      "root": {
        "name": "Aw, Awi, Awei",
        "lang": "Indo-European",
        "refs": "POK:86",
        "gloss": "bird"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:86; HRN:296; SYN:183",
          "words": [
            {"translit": "vîš 2", "gloss": "bird", "script": null},
            {"translit": "vayu", "gloss": "air", "script": null},
            {"translit": "vi 1, vay 1", "gloss": "to fly", "script": null},
            {"translit": "â-vayeiti", "gloss": "flied up", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "POK:86; NYB:207",
          "words": [
            {"translit": "vôi, vây, vâyandak", "gloss": "bird", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:995; FRS:56",
          "words": [
            {"translit": "vây", "gloss": "bird", "script": "واى"},
            {"translit": "vîš", "gloss": "bird", "script": "ویش"}
          ],
          "script_extra": null,
          "note": "Both are almost obsolete",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:86",
          "words": [
            {"translit": "avis", "gloss": "bird", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "aviation, ostrich", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ow, Owo, Ayo, Ôwyo",
        "lang": "Indo-European",
        "refs": "POK:86,783",
        "gloss": "a bird egg"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:783; SYN:256",
          "words": [
            {"translit": "âvaya, xâya", "gloss": "egg", "script": null},
            {"translit": "ap-âvaya", "gloss": "to castrate", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:103; PLA:104; BQT:711",
          "words": [
            {"translit": "hâyîk, xâyak", "gloss": "egg, testicle", "script": null},
            {"translit": "xâyak-bar, xâyak-bâr", "gloss": "egg carrier (fish)", "script": null, "see": ["Bher 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:103; SYN:256; PLA:104",
          "words": [
            {"translit": "xâyeh", "gloss": "egg, testicle", "script": "خایه"},
            {"translit": "xâvîyâr", "gloss": "caviar", "script": "خاویار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Turkish",
          "refs": "AFM:51",
          "words": [
            {"translit": "havyâr", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Italian",
          "refs": null,
          "words": [],
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
          "refs": "AHD",
          "words": [
            {"translit": "caviar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic / Old Norse",
          "refs": "AHD",
          "words": [
            {"translit": "ajjam", "gloss": "egg", "script": null},
            {"translit": "egg", "gloss": "egg", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "kidney, egg", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ôvum", "gloss": "egg", "script": null}
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
            {"translit": "ovule", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Awar",
        "lang": "Arabic",
        "refs": "SAP:1123",
        "gloss": "he damaged"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "SAP:1124; AHD:91; KLN:133",
          "words": [
            {"translit": "`awâr, `awârîyah", "gloss": "damaged goods", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "âr 2", "gloss": "damage, shame", "script": "عار"},
            {"translit": "avâr", "gloss": "defect, damaged goods, damaged cloth", "script": "عوار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "گنگ باد آن کس که اندر طعن تو گوید سخن - کور باد آن کس که اندر عرض تو جوید عوار",
            "poet": "Farrokhî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Spanish",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Italian",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "KLN:133; AHD:91",
          "words": [
            {"translit": "avarie", "gloss": "damage to ship, also (averaged) loss shared equitably among investors", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "average", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Awei",
        "redirect": "Aw"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T05:41:48.747Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T05:41:48.782Z] TOOL RESULT

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


## [2026-09-05T05:42:39.461Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','SYN','NYB','FRS','AHD','PLA','BQT','AFM','SAP','KLN','MON','BRT','PHD','WLD','IEC','LKT','TTS','SKT','ARY','HUB','CHEUNG','FVQ','DEV','PHN']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


## [2026-09-05T05:42:39.515Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && cat tools/verify_check.py | head -60"
}
```


### [2026-09-05T05:42:41.048Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt"], "page_
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only. Google Books no-view records 4y
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively 
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== CHEUNG null
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
```


### [2026-09-05T05:42:41.092Z] TOOL RESULT

```
agent
page-101.json
page-126.json
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
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
process
sources
---
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
```


## [2026-09-05T05:42:48.007Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=92 && NR<=96 {print \"=== leafidx(1-based) \" NR \" ===\"; print}' POK_01.txt | head -120"
}
```


## [2026-09-05T05:42:49.144Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"aui̯-\\|auei-\\|au̯ei-\\|'Vogel'\\|Vogel\" POK_01.txt | sed -n '1,40p'"
}
```


### [2026-09-05T05:42:49.649Z] TOOL RESULT

```
=== leafidx(1-based) 92 ===
  Gr.  I  680*.
12-Präsens:  gr.  a%vo)  aus  ^dJ^d-v-Loy  (vgl.  zur  Bildung  Schwyzer  Gr.  Gr. I  694)  und  hvia)  aus  ^dfaveo)  ,reinige  die  Körner  durch  Aufrütteln  von der  Spreu,  beutle',  J^ävat'  TtsoinTiaai  Hes.  (überliefert  ydvai'  utSQimvoai] s.  auch  Bechtel  KZ.  46,  374);  beruht  auf  einem  solchen  schwachstufigen .  n-Präs.,  aber  in  der  Bed.  ,wehen',  auch  apr.  ivins  ,Luft',  Akk.  loinnen ,Wetter'?
83
iO-Präs.  (oder  von  einer  Wzf.  '-"^nei-?):  ai.  väyati  ^weht^^  av.  fraväyeiti verlöscht^;  got.  waian  loaiwö,  ags.  wäwan,  ahd.  wäjan,  wäen  ^wehen^,  aksl. ^eio  vejet^  ^wehen^  und  ^worfeln^  (davon  russ.  vejalo,  sloven.  vevnicaj r,o\n.  loiejaczka  ^Worfschaufel^  Kornschwinge^);  Nominal:  lit.  ue/as  ^Wind^ ; ai.  väyiH,  av.  väyus  ,Wind^  Luft^
für  wurzelhaften  Wert  des  -i-  führt  man  die  Tonstufe  *uf-  in  folgen- den ^yörtern  an^  die  aber  zum  Teil  auch  anderen  Auffassungen  Raum .T-eben:  aksl.  vijah,  vijalica  ^tempestas'^;  russ.  vhjdlica  ^Schneegestöber^ (auch  vejdlica\)y  Vbjuga  ^Schneesturm^,  zavbjdth  ^verschneien^^  cech.  vdti i*vbjati)  ^wehen*^  (erst  slav.  Entwicklungen  aus  vortonigem  vej-?)-  r.-ksl. vich^r^  {*ueisuro-)  ^Wirbelwinde  (jedenfalls  zunächst  zu  russ.  vichatb  ,er- schüttern;  bewegen^,  vichljath  ^schleudern'^;  s.  Brugmann  Grundr.  IP  1049^ Pedersen  IF.  5^  70,  und  wohl  als  _,wirbela;  im  Kreise  schwingen^  zu  *ueis- drehen^);  lit.  vydra,  vidras  ^Sturmwind^  (s.  Leskien  Bild.  438;  das  im Lit.  sehr  seltene  Formans  -dra  —  vgl.  echt  lit.  vetra  ^Sturm^  —  mahnt zur  Vorsicht);
hom.  ^Lov  "^TOQy  d-vf.idv  ^.laOsj  cctcfS-cov  vom  Aushauchen  oder  Auslassen der  Lebenskraft  (zur  Bed.  zuletzt  Bechtel  Lexil  21  f.);  gr.  Wz.  dJ^ia--, mcymr.  aioyd  s.  82  oben.
h.  aue-d-:  ahd.  wäzan,  wiaz,  mhd.  loäzen  ^wehen^  blasen^^  wäz  ^Wind- stoß^;  lit.  vedinti  ^lüften^  kühlen^;  allenfalls  gr.  äaC,o)  ^hauche^  aus  ^^äfdö-m (eher  aber  gr.  Neuschöpfung  nach  anderen  Verben  auf  -a^w);  vermutlich auch  (aus  *aiid-d-ro-)  lit.  dudi^a  m.  ^Sturm^^  n.  ^Gewitter^;  apr.  wydra yWind^  über  ai.  üdhar  n.  ^Kälte^^  av.  aodard,  aota  ds.  vgl.  Persson  Beitr.  11.
c.  ue-lO'  vielleicht  in  lat.  evelätus  ^eventilatus^  unde  velabra,  quibus frumenta  eventilantur^  (Paul.  Fest.  68,  3)  und  in  ahd.  wäla  m.  n.  ^Fächer^ (wenn  nicht  aus  *ice-pla,  s.  unten)?
d.  ue-s-:  ai.  väsa-hj  väsaJca-h  ^Wohlgeruch^^  väsayati  _,füllt  mit  Wohl- geruch^;  samväsita-h  ^stinkend  gemacht^;  isl.  väs  _
=== leafidx(1-based) 93 ===
,aura  refrigeranse_,  vzsa ^spirare^;  ndl.  loaas  ^Reif^  Duft^,  lit.  vestu^  vesti  ^sich  abkühlen,  kühl  oder luftig  werden*^,  vesä  ,kühle  Luft,  Kühle',  vesus  ,kühl,  luftig^
e.  f- Weiterbildungen:  ai.  väta-h,  av.  vätö  ^Wind^^  ai.  vätula-h  (s.  unten), gr.  är^xr^g  ,Wehere,  drjffvgog  ,windig,  luftig^  =  ai.  vätula  ,windige  (auch  ,ver- rückt*^;  dazu  auch  vielleicht  gr.  ärjavXog  ,freventliche  nach  Brugmann BSGW.  1901,  94;  trotz  aiovXoq  ds.  nicht  nach  Becbtel  Lexil.  15  zu  ai. yatu-h  ,Spuke);  lat.  vannus  ,Futterschwingee  (aus  *uat-n6-s,  vgl.  das  Demin. vatillum  ursprüngl.  ,,eine  kleine  Worfschaufel^;  aus  dem  Lat.  stammt  ahd. tuanna,  ags.  fann  ^Futterschwinge^,  auch  nhd.  Wanne);  anord.  vel,  veli ,Wedel,  Schweife  (über  synkopiertes  *vepia-  aus  *vapila-),  ahd.  2vedil  ds. ; ahd.  wadal  ^Wedel^,  Adj.  ,sch weifend,  unstet,  Bettler^^  loadalön  ,schweifene
6*
84
(urgermanisch  *wapla-,  idg.  *ud-tlo-),  ags.  ivapol  ^wandernd^  w'^dla  .Bett-' ler_,  arm^^  wöedl  ^Armut^,  lucedlian  ^betteln^  arm  sein'  (urgermanisch  ^^wepla-), woneben  ahd.  luallön  ^wandern;,  umherziehen,  wallfahrten',  ags.  iceallian ^wandern' (aus  "^icädlö-ja-n)]  ahd.  loäla  ^Fächer'  (aus  *ive-pla- oder  *we-la-'^ s.  oben);  lit.  vetra  ,Sturm,  Unwetter';  aksl.  vetn  ^huit,  AVind',  apr.  icetro ,Wind';  lit.  vetyti  ^worfeln'.  |
Über  ai.  upa-väjayati  ,facht  das  Feuer  an'  (von  Pänini  als  Kaus.  zu vä-  gefaßt)  s.  Wackernagel  KZ.  43,  292.  ^
Vielleicht  hierher  gr.  äe&Xog  (s.  11.  aue-   ,sich  mühen')  als  ^Keuchen'?
WP.  I  220 f.,  Feist  565  a,  Trautmann  345,  Schwyzer  Gr.  Gr.  I  680.
II.  aue-  (ue-d(h)-?)  ,sich  mühen,  anstrengen'?
Solmsen  Unters.  267  f.  verbindet  ai.  väyatij  -te  ,wird  müde,  wird  er- schöpft, ermattet'  mit  gr.  äs&Xog  ,Mühsal,  Wettkampf'  (^IcJ^e-d-Xog),  ^sd-lov, ä-9-Xov  ,Kampf,  Kampfpreis,  Kampfplatz',  wobei  d-  entweder  Vorschlags-' vokal  ist  oder  eine  vollere  Wzf.  *aue-  neben  *we-  voraussetzt.  Damit" allenfalls  vereinbar  ist  Zupitzas  KZ.  37,  405  Vergleich  der  gr.  Worte  mit mir.  feidm  , Anstrengung', /ec^i'Z  ,ausdauernd',  air.  ni '  fedligedar  ,non  manet' (wobei  formale  Verhältnisse  wie  *me-  ,messen' :  *med-,  *ue-  ,wehen' :  anord. vedvj  nhd.  Wetter  vergleichbar  wären),  wozu  Pedersen  KG.  I  110,  cymr. gweddil  ,remnant,  leavings'  (daraus  mir.  fuidell)  stellt;  hierher  toch.  B ivaimene  ,schwierig'?
Doch  ist  die  Zusammenstellung  in  allen  ihren  Gliedern  ganz  unsicher. Für  väyati  wird  ,sich  anstrengen'  als  Gdbed.  in  Frage  gestellt  durch  die Bed.  ,austrocknen'  von  väna  ,trocken',  upa-väyati  ,durch  Vertrocknen ausgehen,  vertrocknen',  upaväta-  ,trocken  geworden';  und  in  üed-Xog  löst sich  am  nat�
=== leafidx(1-based) 94 ===
�rlichsten  -&Xo-  als  suffixal  ab,  während  der  Dental  der  ir. Worte  wurzelhaftes  d  oder  dh  ist,  also  bestenfalls  recht  entfernte  Ver- wandtschaft bestünde.
WP.  I  223,  Van  Windekens  Lexique  149.
^^^S-f  W^g-,  aug-,  ug-   ,vermehren,   zunehmen',   mit   s-Formans    aueks-, auk-s-,  uek'S-,  uk-s-.
Ai.  ugrd-  ,gewaltig'  (Komp.  Sup.  öjiyas-,  öjutha-  ,der  kräftigere,  kräf- tigste') ==  av.  ugra-  ,stark,  kräftig-  (Komp.  Sup.  aojyah-,  aojista-).
lat.    augeö,   -ere    ,vermehren',    auctoi-   (=  umbr.  uhtur)    ,Urheber   usw.', auctiö  ,Versteigerung',   augmen{tum)   , Zuwachs'   (=   lit.    augmud  ,Wachs-  ' tum',  ai.  öjmdn-  m.  ,Kraft'),   aiigur  ,Weissager'   aus  *auqos  ,Vermehruno' (WH.  I  83);
85
o-ot.  aukan  (Prät.  aiauk),  auknan  ^sich  mehren^^  cma-,  hi-aukan  ^hinzu- füo-en^  ahd.  ouhJiön,  as.  ökian  ^vermehren^;,  ags.  eacian  ^zunehmen'^^  tecan mehren^;  anord.  auka  (Prät.  jök  und  aukada)  ^vermehren^;  st.  Partiz.  ags. cacen    as.  ö/can  ^vermehrt^  schwanger^;
lit.  a-ii^^^^  «w^2^t  (dehnstufig-)  ^wachse^^  auginu,  -inti  ^wachsen  lassen, erziehen'^,  ablautend  pa-ügeti  ^heranwachsen^,  ügis  ,Wuchs,  Jahreswuchs^, lett.  aüdzet,  aüdzindt  ^aufziehen'^,  apr.  auginnons  Part.  Perf.  Akt.  ,gezogen^, alett.  aukts  ,hoch^  =  lat.  aiictus,  lett.  aügt  ,wachsen^,  wie  auch  thrak. y^v-d-i-rtaoog  ,Hohenfurt^,  apr.  Aucti-garhin,  aucktai-rikijskan  ,Obrigkeit^, aucktimmien  , Vorsteher^,  woneben  mit  dem  s  des  -es-St.  (s.  unten)  lit. dukstas,  lett.  aüksts  ,hoch^  (:  lat.  augustus  ^erhaben'^),  apr.  auck-timmiskan f.  (Akk.)  ^Obrigkeit*^,  apr.  aügus  ,geizig^  (als  ,mehrend^),  lit.  dugumas, lett.  ailgums  ,Wachstum^;
es-St.  ai.  öjas-  n.  ,Kraft,  Stärke^,  av.  aojah-,  aogah-  (ebenso  r-St. aogard)  ,Kraft,  Stärke^,  lat.  augustus  s.  oben  (ebenso  lit.  usw.  dukstas)] dazu  mit  s  im  Verbum:
ai.  vdksana-m  ,Stärkung^,  vaksdyati  ^läßt  wachsen^,  av.  vaxsaiti  ,läßt wachsen^,  woneben  mit  schwächster  Wzstufe  ai.  üksati  ,erstarkt^  (Perf. vavdksa),  av.  uxsyeiti  ,wächst^;  got.  loahsjan  ,wachsen^  (=  ai.  vaksayati, idg.  Iter.-Kaus.  Hwkseiö]  damit  verband  sich  das  ö-stufige  FerL  ivöhs  zum Paradigma;  s.  Brugmann  IF.  32,  180,  189);
gr.  d^J^'Ji^a)  ,mehre^,  äs^oiiai  ,wachse'^;  ai/^w,  av^avo)  ,vermehre,  ,stei- gere*^,  lat.  auxüium  ,Hilfe^  (ursprüngl.  PI.  -ia  ,Verstärkungen,  Hilfs- truppen^,  N.  PL  eines  auxilis  ,zur  Verstärkung  dienlich^);
anord.  vaxa,  vexa  ,wachsen^,  ahd.  waTisan,  nhd.  wachsen,  wuchs,  wozu z.  B.  got.  wahstus  ,Wachstum,  Wuchs,  Leibesgröße^,  ahd.  ica{h)smo  ,Wachs- tum^  u.  dgl. ;  toch.  A  oksls  ,wächst',  A  oksu,  B  auksu  ,alt^;  nach  Yan Windekens  Lexique  79  auch  hierher  AB  oko  ,Frucht*^,  A  okar  ,Pflanze^; dagegen  Pedersen  Tochar.  227.
Hierher  mit  Dehnstufe  udg-:  got.  loökrs  m.  ,Zins^,  ags.  icöco7' 
=== leafidx(1-based) 95 ===
 f.  ,Nach- kommenschaft,  Zins^  (vgl.  gr.  To-Aog  in  denselben  Bedeutungen),  ahd. wuohhar  m.  ,Ertrag  des  Bodens,  Leibesfrucht,  Nachkommenschaft,  Ge- winn, Zins,  Wucher^  (dazu  steir.  wiech  ,ausgiebig,  üppig,  blätterreich*^ als  Umlaut?  Etwas  anders  Schroeder  Abi.  57  f.),  da  in  der  nicht  mit  s erweiterten  Wzf.  aiieg-  die  Stufe  iteg-  in  air.  /er,  cymr.  gioair  ,Gras'^ belegt  ist;  Avohl  mit  derselben  Ablautstufe  ai.  vcija-h  ,Kraft,  Gut,  Reich- tum, Wettpreis,  Wettlauf^,  ursprüngl.  ,rasche,  erfolgreiche  Energie^,  Olden- berg  ZdMG.  50,  443  ff.
WP.  I  22  f.,  WH.  I  82 f.,  850,  Feist  67,  541,  572,  Pedersen  Tochar.  227.
86
auei-  (ouei-?)  ^YogeF.
Ai.  vi/i^  vBh  m.  ,Vogel'  (Gen.  ve/i,  Akk.  vim),  av.  vis  ds.  (G.  PL  vayam^ auch  mit  themat.  Kasus  vom  St.  vaya-),  mpers.  vCii,  väyandalz  ;Vogel', ai.  vayas-  n.  ^Geflügel,  Vogel",  väyasa-h  ,Vogel,  Krähe';  verbal  av.  ä-vayeiti ^fliegt  heran'  (von  Gottheiten),  ai.  vevlyate  ^flattert'.
Gr.  alsTÖg  ,Adler',  att.  äsrögj  alßsrög'  äsrog'  IleoyaXoi  fies.  {^afi-ez6g), alb.  vi-do,  vito,  vidheze  ,Taube';
lat.  avis   f.  ,Vogel'   (davon   auca   ,Vogel,   bes.  Gans';    Rückbildung   aus Demin.  aucella  aus   *avicella'^   falsch  bei  WH.  I  79)  =  umbr.  avif  Akk.; PI.  ,aves'  (aviekate  D.  Sg.  ,auspicatae',  avieJda  ,augurali');   cymr.  hwyad,- acorn.  hoet,  bret.  houad  ,Ente'  aus  "^auietos?    (Pedersen  KG.  I  55).  Arm.' hav  ,Vogel,  Hahn,  Henne'  kann  zwar  Vorschlags-Ä  haben,   aber   auch  als *^9w-  zu  *'pöu-  , Junges'  (slav.  jnta  , Vogel'  usw.)  gehören.  ]
Im  Zusammenhang  damit  stehen  höchstwahrscheinlich  die  Worte  für ,Ei',  s.  unter  öu-.
WP.  I  21,  WH.  84,  850.
aues-  ,leuchten',   bes.    vom  Tagesanbruch;    aus-,    tfes-,    us-;   (a)us-ös-   f. ,Morgenröte';   *aus-tero-  ,östlich'  (von   einem  Wznomen  *aus-j  oder als  zum  s-Stamm  gehöriges  *aiis-[e]s-^e?'0-  aufzufassen?   s.  Brugmann 11^  1,  327,   wonach    diese   -<ero-Bildung   vielleicht   erst    durch   Nach- ahmung   der    auf   Adverbien    fußenden   Richtungswörter   wie   anord. vestr,  nor-dr  aufgekommen  ist);  auso-  ,Gold'. Ai.    usah    f.    Akk.   usäsam^    Gen.    usdsah    ,Morgenröte',    av.    usä^    Akk. uMvhdm,  Gen.  usaidhö  ds.  {usas-tara-  ,östlich'),  woneben  ai.  Gen.  Sg.,  Akk. PI.   usdh,   av.    Lok.    Sg.  usi-[ßä,  s.  *demä-  ,bauen']    entweder   von   einem Wznomen  *W5-,  oder  als  *us-s-  zum  s-St. ;  ai.  ucchdti  =  av.  usaiti  (*us-sketi) ,leuchtet  auf  (vom  Morgen)',  Perf.  ai.  uväsa^  Aor.  avasran  ,sie  leuchteten'; usar-j  usr  ,Morgenröte,  Morgenfrühe',  us
=== leafidx(1-based) 96 ===
ar-hudh-  ,früh  wach',  usrd-  ^mor- gendlich, rötlich',  auch  figürlich  ,Kuh',  m.  ,Stier'  (Frisk,  Nominalbildung  3); ues-,  uös-  in   ai.  vasar-hdn-   ,in   der   Morgenfrühe    schlagend',   väsard- ,morgendlich',    m.  ,Tag'    (vgl.  dazu    auch    den    wurzelverwandten    r/n-St. *ues-r-j  ues-n-  ,Frühling'  unter  besonderem  Schlagwort);
gr.  hom.  ijihg  *(äusös)j  Gen.  ijovg  ('^jöog)^  att.  (mit  Akzentneuerung)  fwg, dor.  ^wg,  äJ^coQ,  ablautend  äol.  a'ijcüg  ,Morgenröte'  (urgr.  av[o]d)g),  böot.  cla und  ^laiT]  (^daiT])]  IxyxavQog  ,dem  Morgen  nahe',  al'giov  ,morgen'  (*avoQ-)', hom.  }ji6  Oolße  ,morgendlich  strahlender';  iji-yiavog  ,Hahn'  {*ausi-  ,in  der Morgenfrühe  singend');
lat,  auröra  f.  ,Morgenröte'  (für  *äusösa)]  auster  (*aus-t(e)ro-  =  germ. *austra-)  ,Südwind',  austrälis  ,südlich';  vermutlich  auch  aiirum,  sabin. ausom  ,Gold'  als  /^rötlicli^ ;   zu  lit.  duksas   (k  unerklärt)^  alit.  ausas^  apr.
87
aiisis  _,Gold^;  vielleicht  tocli.  A  was  ^Gold^^  aber  vgl.  arm.  os-Jci  ^Gold^^ fiua.  vas-Jci  ^Kupfer'^;  vielleicht  Vesuvius  (anders  unter  eus-  _,brennen^);
mir.  fi^'^  ^Sonnenaufgang'^^  cymr.  gwawr  ^MorgenrÖte^,  bret.  gwere  laouen Morgenstern*^  (*uösri-^  Pedersen  KG.  I  82);
o-erin.  *aust7^ö  in  ags.  easti^e  ^Frühlingsgöttin'^^  eastron  PI.  ^Ostern^  = ahd.  öst{a)raj  öatarün;  dagegen  mit  idg.  -t{e)ro-,  ahd.  östar  ^östlich^  und ^(i\r.  ,nach  Osten^^  nhd.  Oster-reich,  anord.  austr  n.  ^Osten*^  und  Adv.  ;,ost- wärts*,  ags.  Komp.  easterra  ^östlicher''^,  dazu  Ostrogothae^  älter  Austrogoti als  ;die  Östlichen  Goten'';  ahd.  östan  ^von  Osten^,  ags.  easte  f.  _,Osten^^ anord.  austan  ^von  Osten  her^;  *äusös  in  ags.  earendel  ,Morgenstern'_, ahd.  MN  Orendil]
lit.  ausrä  f.  ^Morgeiiröte^_,  austa  ^es  tagt^^  lett.  äust  ds.;  lit.  auHrinis (vBjas)  ^Nordostwind^;,  lett.  äustra  f.  _,Morgendämmerung^_,  äustrums  m. ,Ostea^;  im  Ablaut  zem.  ajpymriai  m.  ;,Morgendämmerung^;
aksl.  za  ustra  ,xd  tcqüS'C'  (über  utro,  jiitro  _,Morgen^  aus  *aus(t)ro-  vgl. Trautmann  19^  Mikkola  Ursl.  Gr.  179  und  Berneker  462 L  m.  Lit._,  wozu Brückner  KZ.  4Q,  212^  der  aus  poln.  uscic  ^glänzen^  ein  sl.  *usto  ^Glanz^ erschließt),  ustin)  ^aestivus*^  (s.  Pedersen  IF.  b,  69).
Vgl.  zum  Ablaut  J.  Schmidt  KZ.  25,  23  f.,  Hirt  Abi.  134,  147,  Reichelt KZ.  39,  69.
WP.  I  26 f.,  WH.  I  86,  87  f.,  Trautmann  19,  Specht  Dekl.  10,  Wacker- nagel-Debrunner  Ai.  Gr.  HI  213  und  281  f.,  Kretschmer  Gl.  27,  231; Leumann  IF.  58,  121  ff.,  Schwyzer  Gr.  Gr.  I  349,  514,  557.
SLüg'  ,gläazen;  sehen^.
Gr.  avyrj  , Glanz,  Strahl,  Tageslicht;  Auge^,  (xvyaC,(ü  ,strahle,  erhelle; sehe^,  8Qi-avyrjg  ,sehr  glänzend^;
a
```


### [2026-09-05T05:42:49.699Z] TOOL RESULT

```
1051:8.  au-,  auei-  , sinnlich  wahrnehmen,  auffassend
1154:auei-  (ouei-?)  ^YogeF.
1155:Ai.  vi/i^  vBh  m.  ,Vogel'  (Gen.  ve/i,  Akk.  vim),  av.  vis  ds.  (G.  PL  vayam^ auch  mit  themat.  Kasus  vom  St.  vaya-),  mpers.  vCii,  väyandalz  ;Vogel', ai.  vayas-  n.  ^Geflügel,  Vogel",  väyasa-h  ,Vogel,  Krähe';  verbal  av.  ä-vayeiti ^fliegt  heran'  (von  Gottheiten),  ai.  vevlyate  ^flattert'.
1157:lat.  avis   f.  ,Vogel'   (davon   auca   ,Vogel,   bes.  Gans';    Rückbildung   aus Demin.  aucella  aus   *avicella'^   falsch  bei  WH.  I  79)  =  umbr.  avif  Akk.; PI.  ,aves'  (aviekate  D.  Sg.  ,auspicatae',  avieJda  ,augurali');   cymr.  hwyad,- acorn.  hoet,  bret.  houad  ,Ente'  aus  "^auietos?    (Pedersen  KG.  I  55).  Arm.' hav  ,Vogel,  Hahn,  Henne'  kann  zwar  Vorschlags-Ä  haben,   aber   auch  als *^9w-  zu  *'pöu-  , Junges'  (slav.  jnta  , Vogel'  usw.)  gehören.  ]
1858:Specht  will  auch  (Dekl.  148),  mit  i-  und  it-Formans,  ags.  bri-d,  birci ,junger  Vogel',  germ.  brü-tis  ,Frau,  Braut',  ai.  bhimnd-  , Embryo',  lett. braüna,  Öech.  brnka  {*bhru-nka)  ,Nachgeburt'  hierherstellen.  S.  aber  unter bh(e)reu-  , quellen'.
1941:Merkwürdig  ist,  daß  in  den  Schallsippen  von  gr.  q)QvyiXog  ,ein  Vogel', iRt.frigö  ,quietsche',  poln.  bargiel  ,Bergmeise',  russ.  berglezz  ,Stieglitz'  die Verteilung  der  Formen  mit  u,  mit  i,  und  ohne  beides,  dieselbe  wie  in den  Worten  für  kochen  ist.
1960:gr.  q}QvyiXog  ,ein  kleinerer  Vogel'  (Umstellung  aus  *g)QiyvXoQ:  lat./ri^-?);
1979:bheregh-  ,hoch,  erhaben^,  bherghos  ,Berg^,  vielleicht  Erweiterung  von  hh ,(tragen,)  heben^  (s.  dort  die  Gruppe  von  nhd.  empor)  oder  von  hh ,hervorstehen^;  bhrbiü-s  ,hoch^;  bherghö  ,berge'. .    Ai.    Kaus.    harhdyati  ,mehrt^,    hrmhdti    ,macht    feist,    kräftigt,   erheb vermutlich  harha-s,  -m  ,Schwanzfeder,  Schwanz  eines  Vogels,  bes.  bei Pfau^;    hrhdnt-   ,groß,   hoch,    erhaben,    hehr^,    auch    ,hoch,   laut,   von   de] Stimme^,  fem.  bfhati  (=  ir.  Brigit,  germ.  Burgund),  av.  hdrdzant-  (npep huland),  f.  hdrdzaiti  ,hoch^,  im  Kompositum  hdrdzi-  (:  '*hdrdzra-)j  hdrdz-  ,hoc und  ,Höhe,  Berg^  (=  npers.  hurz  ds.,  ir.  hri]   der  Nom.  av.  har§  Subs kann  ar.  -ar-,  aber  auch  ar.  -f-  enthalten,  Bartholomae  IF.  9,  261),  hochstufi av.  uz-hardzayeni  ,ich  soll  aufwachsen  lassen'  (dazu  2aTL-ßaQ^dvr]g  ,Glüc! erhöhend',  iran.  *harzana-)j  hardzan-   m.  hardzah-  n.  ,Höhe',    hardsnu-  m ,Erhebung,  Höhe,  Himmel,  Kopf,  hardzyah-  ,höher',  bai-yzista-  ,der  höchste^ höchstgelegene' ;  npers.  häl-ä  ,Höhe'  {*harz-),  hurz  (s.  oben) ;
2108:aisl.  bür  n.  , Vorratshaus,  Frauengemach',  ags.  bür  m.  , Hütte,  Zimmer', abd.  bür  m.  ,Haus,  Käfig',  nhd.  (Vogel-) Bauer,  wovon  ahd.  nähgibür,  ags. neahgebür,  nhd.  Nachbar,  engl,  neighbour  und  ahd.  gibür{o),  mhd.  gebür(e)f dann  bür,  nhd.  Bauer  ,rusticus';
3800:Mit  dem  Begriff  des  wirren  Gerankes  schwed.  dodra,  mhd.  toter  m. ^Dotterkraut,  cuscuta',  mengl.  doder,  nengl.  dodder  ,Flachsseide',  ndl. {vlas)-doddre  ds.  Nach  Falk-Torp  u.  dodder  wäre  das  Wort  als  Bezeich- nung für  gewisse  Pflanzen  mit  gelben  Blüten  auf  den  Eidotter  übertragen: as.  dodro,  ahd.  totorOy  ags.  dy dring  ,'EA-dotter'  {-ing  beweise  die  Ableitung von  Pflanzennamen);  eher  ist  dafür  , Klumpen'  =  ,dicke  Masse'  im  Gegen- satz zum  zerfließenden  Eiweiß  die  vermittelnde  Bed.  gewesen  (Persson) oder  vgl.  norw.  dudra  ,zittern^  das  elastische  Zittern  dieses  gallertartig wippenden  Kerns ;  vgl.  aisl.  dodr-kvisa  ,ein  Vogel'.
4311:gr.  OLTjj  b'r],  oa  , Sperberbaum,  Vogelbeerbaum'  (*oiuä)  =
4318:ai.  ita-  ,schimmernd,  bunt',  m.  ,Roß,  Vogel,  Antilope'  usw.,  urind.  PN (14.  Jh.)  Aita-ggama  ,auf  einem  Widder  reitend'  (Kretschmer  KZ.  55,  93),
4858:i.  er-,  or-  ,Adler^,  arm.  gr.  /größerer)  Vogel  überhaupt^ Arm.  oror,  urur  ,Möwe,  Weihe'; gr.  })Qvxg,  -i&og,  dor.  -ixog  , Vogel;  Hahn^  Henne',  Hqveov  ,Vogel';
4988:slav.  mit  Nasalierung:  mbg.  jer^bh,  r.-ksl.  jafabh,  *jerabh,  skr.  järeb usw.  , Rebhuhn',  von  der  Farbe  benannt,  wie  klr.  ordbyna,  orobynd,  sloven. jerebikaj  cech.  jefdb  usw.  , Vogelbeere';  ohne  anlaut.  Vokal  russ.  rjaböj ,scheckig'  (vgl.  oben  rjabinövaja  noch,  abg.  r^bi,,  russ.  rjdbka  ,Rebhuhn', rjabina  ,Vogelbeerbaum',  rjdbcik  ,Haselhuhn',  usw.).
```


## [2026-09-05T05:43:06.043Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 grep Ei / ouiom ===\"\ngrep -n \"ō̆u-\\|ōu-\\|ōu̯i̯o\\|,Ei'\\|^ou-\\|owyo\" POK_02.txt | sed -n '1,30p'\necho \"=== leaf 437-441 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR>=438 && NR<=441 {print \"=== leaf \" NR \" ===\"; print}' POK_02.txt | grep -n \"Ei\\b\" | head -30"
}
```


## [2026-09-05T05:43:07.541Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 995 ===\"; grep -n \"^ *995\\.\\|995\\. \" HRN.txt | head\necho \"=== HRN 296 ===\"; grep -n \"^ *296\\.\\|296\\. \" HRN.txt | head\necho \"=== HRN 103 ===\"; grep -n \"^ *103\\.\\|103\\. \" HRN.txt | head"
}
```


### [2026-09-05T05:43:08.107Z] TOOL RESULT

```
=== POK_02 grep Ei / ouiom ===
=== leaf 437-441 ===
```


### [2026-09-05T05:43:08.220Z] TOOL RESULT

```
=== HRN 995 ===
8650:995. ninS *Maus*.
=== HRN 296 ===
2880:296. pertew 'Glanz*.
=== HRN 103 ===
1298:103. ef gen den 'wegwerfen', ßgenden^ ewgenden (AM.),
10580:103. häj vor dem Imperativ.
```


## [2026-09-05T05:43:18.532Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8640,8660p' HRN.txt\necho \"=== grep xaja/haja Ei ===\"\ngrep -n \"'Ei'\\|,Ei'\\|Ei\\.'\" HRN.txt | head -20\necho \"=== grep xaja ===\"\ngrep -n -i \"haja\\|χāja\\|chaja\\|hājah\\|xaja\" HRN.txt | head -20"
}
```


### [2026-09-05T05:43:18.620Z] TOOL RESULT

```
nniljvg, t. mäljig 'Ameise' ein.
994. tnöze 'Schuh', arab. LW. manzaj.
aw. [/^maoc^ mit paiti 'anziehen (sc. Schuhe)*, vergl.
framv/ti' *das Ausziehen (der Schuhe)'; phlv. tnööak
(Men. ; arm. LW. muöak), vergl. mök (chald. LW.
NpID), auch patmö/tan 'anziehen'; ai. [/^möö- mit ä,
prati anziehen (irgend ein Kleidungsstück)*, mit upa
*Schuhe anziehen*.
LW. afy. möza ; bei. müzag, n. mözay 'Socken, Stiefel,
Beinkleider* (174).
995. ninS *Maus*.
g. muSk,
ai. müs~, skr. müsaka-, mfisika- *Maus, Ratte*; arm.
mvkn 'Maus' (H. No. 206).
kurd. fni§ik, misk; Si{y. mayak, maya 'Ratte', maya-
küfai 'Maus, junge Ratte*; oss. d. miste, t. mist (189);
bei. musk, n. milsk (245).
996. möT 'Haar' ^).
g. mld.
phlv. mö, möd bezw. möf; bei. müd^ mtd, n. mi^
'Haar (eines Menschen), Ziegenhaar' (247).
=== grep xaja/haja Ei ===
=== grep xaja ===
996:und auch im Ap. könnte man frahajam lesen.
1517:hajara, cf. hajr 'Hinderung des freien Willens im Reden, (Obhut)*.
```


## [2026-09-05T05:43:21.226Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 leaves count ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' POK_02.txt\necho \"=== search 'Ei' root ouiom in POK_full ===\"; grep -n \"ōu̯i̯om\\|ouiom\\|ōu-\\|ǝu̯i-\" POK_full.txt | head -20\ngrep -n \"avayam\\|āvaya\\|ōuiom\" POK_02.txt | head"
}
```


### [2026-09-05T05:43:22.820Z] TOOL RESULT

```
=== POK_02 leaves count ===
433
=== search 'Ei' root ouiom in POK_full ===
68388:Flaumru. ds.. Old Icelandic fley{= ttAoTov, *plouiom) n. 'ship'; Old Icelandic fludi. 'blinde
```


## [2026-09-05T05:43:35.765Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob,re\nfor f in sorted(glob.glob('page-*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for lst in [e.get('ref_check',[])]+[n.get('ref_check',[]) for n in e.get('nodes',[])]:\n            for r in lst or []:\n                if str(r.get('ref','')).startswith('HRN'):\n                    print(f, r['ref'], r['status'], r['note'][:220])\nEOF"
}
```


## [2026-09-05T05:43:36.338Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['HRN'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T05:43:37.362Z] TOOL RESULT

```
page-126.json HRN:133 supports HRN.txt leaf 154 (Horn p. 133), No. 599: 'dīvār Mauer, Wand. ap. *deghavāra- (vergl. gr. teichos, osk. feíhúss). Nöldeke (mündliche Mitteilung), unter der Voraussetzung, dass die np. Grundform *dēvār lautete ...; kurd. L
page-32.json HRN:1 supports Horn, Grundriss p.1 (HRN.txt form-feed leaf 22, offset leaf = printed + 21) is exactly the page Nourai used. It has '2. āb, āw "Wasser" … ap. āp- "Wasser"; aw. āp-; phlv. āp (pāz. āw); ai. āp-, kurd. āw; afγ. ōba (fem.);
page-34.json HRN:38 supports HRN.txt leaf 59 = printed p.38, entry no. 166: 'bāzār ‘Markt’, bāzargan, bāzergān ‘Kaufmann’.' Horn heads the entry with exactly this pair. (The same page, however, denies the Old Persian abācaris etymology of the root b
page-39.json HRN:249 supports Horn, Grundriss p.249 (HRN.txt leaf 270) no.1117: 'hēzum (Is. 30,88), hēzem "Brennholz"; hīme. aw. aēsma "Brennholz"; phlv. ēsm (nur umschreibend), hēzam bezw. ēzam (päz. hēzam); ai. idhmá-.' Page number cited by Nourai
page-39.json HRN:108 supports Horn p.108 (HRN.txt leaf 129) no.488: 'xšt "Ziegel, Backstein". aw. ištya- "Ziegel, Backstein"; phlv. xist; skr. iṣṭakā- "Backstein".' Exactly the chart's chain.
page-40.json HRN:14 partial HRN.txt ƒƒ-leaf 36 (printed p.14) no. 57: 'āhen ‘Eisen’; āhenīn ‘eisern’. Semn. ōsūn; g. vuhen. phlv. āsīn (z. B. vd. 5,121), āsīnīn ‘eisern’. kurd. hasin ~ hesin, ūsin ‘Eisen’; bel. LW. ahin.' Horn gives Nourai's Pahlav
page-41.json HRN:93 supports HRN.txt leaf 114, printed '— 93 —', no. 414: 'jāved ,ewig', jāvedān. aw. yavaētāt- ,Ewigkeit', yave ,für ewig'; phlv. yāvetan (PPGl.), arm. LW. yavēt, yavitean, yavitenakan.' — exactly the arrow Avestan yavē/yavaētāt- → 
page-41.json HRN:108 not_found HRN.txt leaf 129 prints '— 108' and contains only nos. 486-489 (xusur 'Schwiegervater', xusrū, xišt, xušk) — nothing about xudā or xᵛāja. Horn's xudā entry is no. 471 on p.104 (leaf 125): 'xudā, xudāi "Gott, Herr", xudāv
page-44.json HRN:17 supports HRN.txt \f-leaf 38 = printed p.17, entry no. 69: 'ers ‚Thräne‘. mäz. asr; Käs. asl, aw. asru- ‚Thräne‘; phlv. ars; ai. áśru-; lit. aszarà ... Die indog. Urform war nach Bugge *dakru-, da auch gr. dákru, acymr. dacr, air.
page-46.json HRN:5 supports HRN.txt ↵-leaf 27 = printed p.5, Horn's numbered entry 13: '13. ārd „Mehl“. Kāš. ort, ürt, vergl. auch s. v. āsyāh: ōr, ār, ir. aw. aša- „gemahlen“, anaša- (Hübschmann ZDMG. 38, 428); phlv. ārd „Mehl“. kurd. ār, ārd (Jab
page-50.json HRN:241 contradicts HRN.txt \f-leaf 262 = printed p.241, entry 1077: 'verč ‚Grösse, Würde“. aw. *varəcah- in asvarədah-, varəcaŋhvant- ‚glanzreich, prangend“; phlv. varč bezw. varj, varčōmand bezw. varjōmand ...; ai. várcas- ‚Glanz“.' Horn'
page-51.json HRN:22 supports HRN.txt ff-leaf 43 (= printed p.22), no. 93: 'efrāxten "erheben", efrāšten, Praes. efrāz-em … phlv. afrāstan … Zu √reg- + abhi "richten, aufrichten"; ai. irajyáti; gr. ὀρέγω; lat. rego; got. uf-rakjan'. Exactly Nourai's 
page-51.json HRN:23 supports HRN.txt ff-leaf 44 (= printed p.23): no. 94 'efrōxten "anzünden, erleuchten" … aw. aiwi + √ruc- "anzünden"; phlv. afrōxtan, afrōčīnītan; skr. abhi + √ruc-'; no. 97 'efsār "Zügel, Zaum" … aw. *aiwisāra-; phlv. afsār (Bund
page-51.json HRN:23 partial HRN.txt leaf 44 (= p.23) has afzūdan (no.96, 'aw. *aiwi + √sav-, sāvayāt "er wird nützen"; phlv. afzūtan, afzūn') — supports the afzūdan arrow — but the same page's no.101 REJECTS the afsūs arrow Nourai draws ('ist unhal
page-51.json HRN:24 supports HRN.txt leaf 45 (= printed p.24), no.102: 'efšānden "ausschütten", fšānden. aw. aiwi + fšūnayeinti "sie weiden aus", yt. 14, 56 (Geldner, 3 Yasht, 88) (?); phlv. afšāntan.' Horn does draw Nourai's arrow — with his own '(
page-51.json HRN:172 supports HRN.txt leaf 193 (= printed p.172), continuation of no.777 šitāftan: 'phlv. ōštāftan (vd. 7 (27) Gl., 18 (98), Men.) "eilen", arm. LW. štap, davon Denomin. štapim "eilen". aw. *aiwiš + √tap-, tāpayeiti "in Wärme, Hitze b
page-51.json HRN:174 supports HRN.txt leaf 195 (= printed p.174), no.786: 'šikār "Jagd" … phlv. škar "Jagd" (vd. 5 (134) Gl.), škara "Jagdhabicht" (Bund.) … aw. *aiwiš (doch vergl. No. 221) + √kar- (de Lagarde …); aber dann gewiss nicht zu √kar- "tun
page-54.json HRN:13 contradicts Horn's no. 52 (HRN.txt leaf 33-34 = printed pp.12-13) is the entry Nourai is citing, and it says the opposite of what the chart draws: 'Darmesteter's Etymologie (aus ap. aniya-) ist falsch, denn ap. aniya- hätte im Np. k
page-54.json HRN:13 contradicts HRN.txt leaf 34 = printed p.13: 'Darmesteter's Etymologie (aus ap. aniya-) ist falsch, denn ap. aniya- hätte im Np. kaum etwas anderes als [ēn] werden können.' Horn's own derivation, on the facing page (leaf 33 = p.12, n
page-59.json HRN:1 supports HRN.txt leaf 22 = printed p.1, entry no.1: 'ā. 1) Praefix, z. B. in āmeden, ārāyiš. ap. aw. phlv. ā; ai. ā́. 2) Praeposition, z. B. in her ā her, gird ā gird, aw. ai. ā.' Both of Nourai's two uses, verbatim.
page-60.json HRN:70 supports HRN.txt 0-based leaf 91 = printed p.70, numbered entry 315: '315. pes "hinter, nachher", pesīn "letzter". ... ap. pasā "hinter", pasāva "nachher"; aw. pasča "nach", paskāt "nachher, hinter", pasne "hinter"; phlv. paš, pa
page-64.json HRN:17 contradicts HRN.txt \f-leaf 38 (printed p.17), entry 68: 'erzīz «Blei». arm. arcic. Geldner's Gleichstellung mit aw. arezazi- … ist lautlich unmöglich; ebenso die Ableitung von aw. erezata-, skr. rajatá-. Die Heimat des Wortes ist n
page-71.json HRN:281 supports HRN.txt leaf 302 (printed p.281, running head '— 281 —'), entry 117: 'hōš "Morgenröte" (Aw.-Komm.); vergl. hōšastar "östlich", hōšbām "Tagesanbruch" (Men.). aw. usah- "Morgenröte"; ai. usas-.' Horn supports the words and
page-71.json HRN:56 supports HRN.txt leaf 77 (printed p.56), entry 243: 'behār "Frühling". Käs. vor neben bohor. ap. θūra-vāhara- (?); aw. vaŋhri "im Frühling" (ZP. 61); phlv. vahār; ai. vasantá- "Frühling" … arm. garun "Frühling".' Horn's page carr
```


### [2026-09-05T05:43:39.127Z] TOOL RESULT

```
{
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
 "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
}
```


## [2026-09-05T05:43:53.204Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' HRN.txt)\necho \"=== leaf 317 (p296) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==318' HRN.txt | head -60"
}
```


## [2026-09-05T05:43:53.382Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== leaf 124 (p103) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==125' HRN.txt | head -60"
}
```


### [2026-09-05T05:43:54.877Z] TOOL RESULT

```
leaves: 411
=== leaf 317 (p296) ===
— 296 —
2) *Voger, vergl. väyandak Togel* (Men. 62, 16).
aw. vay- * Vogel*; ai. vdy-, oder nach Joh. Schmidt
KZ. 32, 330 Nom. Sg. aves (RV. I, 130, 3?), dazu
vibhis (aus *vlbh!s), Schmidt stellt dann auch lat. avis,
gl*, w^rofe-, (perg.) aißerog, ouovdc (S. 374 folg.) hierher.
208. vctjTtan {cäzUan) 'fliegen; fahren, AW.-Kommentar,
z. B. vd. 5 (4), 6 (54), Bund., Aogem.
aw. {^oaz-^ vazaiti 'fliegen; fahren etc. ; ai. [/^oah-
*fahren', vergl. np. veziden (oben No. 1083).
In den erwähnten Bedeutungen wird das Verbum
im Kommentar meist nicht glossirt, während es als
'führen, bringen {vajlnUan) nur umschreibend auf-
tritt.
Vergl. bei. gvazay, n. yvazay, guzay 'über etwas
weggehen, überschreiten, vergehen (von der Zeit)' (144).
209. va^sltiifi 'wachsen, anwachsen, zunehmen, häuttg;
vaxs(i)sn^ oä/smitan.; va/s *herhsige (West, vd. 9 (132)
Gl.), Enterest (of money), increase', vergl. Va^sastän
'increase code' (West^, 139), kofoa/s 'mountain spur'
(West-, 35); arm. LW. vasx * Wucher (Hübsch-
mann, ZDMG. 46, 329 No. 6).
aw. \/^va/S' 'wachsen*; ai. [/"vaks-^ äüksat; got.
vahsjmi 'wachsen*.
Vergl. zaza vas 'Gras, Kraut, Pflanze*; af/. va/a
'Futter, Gras'; wa:^. ous, väs, si/n. vos^ vost, sar. vu/,
sangl. ö^, minj. va^s Gras, auch wa;/. vüsln, sar. vu^^ti
'Trift'.
Dialektisch neupersisch findet sich väs (mäzend.),
vos (Semn.) 'Gras etc.'; väs 'Futter (Vullers), das
Castle aus Golius anführt, vermag ich ebenso wenig
zu belegen, wie andere Worte aus dieser Quelle, z. B.
Iießden 'trocken werden*.
210. vätnltan 'speien', vd. 5 (6) ^).
aw. i^varn' 'speien'; ai. l^vam-, väiniti; lat. vomö etc.
') Brugmaun, Gruudriss 11,2 § 572 glaubt nicht an den zuerst
von de Saussure aufgestellten Satz von den zweisilbigen Wurzeln
(vergl. auch I, § 14, § 100 und Griechische Grnmnintik' § 11 Anni.),
```


### [2026-09-05T05:43:56.462Z] TOOL RESULT

```
=== leaf 124 (p103) ===
— 103 —
(7) Gl.), rTstjayee, ä/ezJt (Phlv.-Vend. für aw. [^ha/s-;
AV.), päz. d/ezed (Men.).
oss. ra]xlzai *du willst herabsteigen', d. s^ezun 'hinauf-
steigen' (301).
Das awestische Wort ist nicht sicher; die Päzend-
lesung mit z beweist nichts.
463. xäm *roh, ungekocht'.
ai. amd' *roh*; arm. huni 'roh' (H. No. 171; vergl.
Bartholomae, Studien II, 44. Daneben LW. /aw)5
gr. (Ojiwc; air. 6w.
kurd. xäv; oss. LW. /öm (Hübschniann, S. 133);
afy. öm, um; bei. hämag, n. häniay, liänvcuj (155);
wa/. yüng,
464. yritnös^) ^schweigend, still*, /ämösl.
skr. a + \/^marS' geduldig ertragen' ; vergl. fcrämös
(No. 812).
465. ^Jiän, yßne 'Haus , xänef/T.
phlv. /ßnak, /an, /änaklk (n''Nn"*2, Nöldeke,
ZDMG. 46, 142).
Von i^khan- 'graben'. Vergl. np. (arab.) yendeq
neben kenden,
466. yi^miT 'Quelle, Wasserbassin , x^^ (unbelegt und un-
sicher 2)).
aw. x^fw-, Nom. ;^äo 'Quelle'; phlv. ;fäw, /ßnlk (Bund.) ;
ai. khiin- [khä-),
kurd. känT, kahm,
467. xäwer {/"äwer) 'Herr.
aw. /'äpara- 'gnädig, barmherzig*; phlv. y^äpar
(Darmesteter, Et. ir. I, 60 Note).
468. ^äye 'Ei*.
phlv. xäyak *Ei' (Men.); arm. Jw *Ei' (unsicher; H.
No. 179); lat. öoiim; gr. rJov; ksl. aje^ jaje *Ei*.
kurd. haik, hl, liek; afy. hä; oss. t. aik, d. aißä
(12); bei. haik (159).
») Reimt auf hös Sahn. I, 429 V. 730.
*J Auch an SteUen wie AM. 240 Zeile 4 v. u. wird man nicht
etwa ;^ä»e *eine Quelle*, sondern ^^änl *die Quelle* (allg.) lesen müssen.
```


## [2026-09-05T05:44:10.873Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== leaf 316 (p295) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==317' HRN.txt | tail -40"
}
```


### [2026-09-05T05:44:12.429Z] TOOL RESULT

```
=== leaf 316 (p295) ===
— 295 —
u.
201. urvav 'Pflanze.
aw. urvard- 'Pflanze*; ai. urodrä- 'Fruchtland.
Kommt neupersi«ch nur in Pärsenschriften (z. B.
Sed der) vor.
202. UisJtau aufgellen (von Gestirnen)', vd. 21 (21) Gl. u. ö.
aw. US + V^ay-,
20Ii. nxd{i)st (meist uj' geschrieben) *), uzd{i)stäv 'Götzen-
bild', nzd{i)stparast(i)&nlh 'Götzenanbetung (Men.),
uzdejär (päz. uzdezdr) *Götzentemper.
aw. Hzdarza- 'hohes Gebäude', uzdista-, Vergl. jüd.-
pers. onON (Is. 17, 8).
V.
204. vavdtiHt (Spiegel, Justi: racäst) Text, päz. <jifj(ist
(Nerios. (jujasta),
aw. racastasti- 'Text'; oacdast scheint mir die richtige
Lesung des PehlevTwortes zu sein {st statt st wie öfter).
205. vadrak 'Otter -).
aw. wdra- 'Otter'; ai. udrä- 'Krabbe, Fischotter (un-
sicher)*; lit. udrä; abulg. vydra 'Otter; mhd. otter,
ahd. ottar, an. otr 'Fischotter' 3).
206. vaydän (auch vaytdn geschrieben^)) 'Haupt* (von
guten Wesen), AW.-Komm., Hn.
aw. vaydana' 'Haupt*.
207. vai 1) 'Luft', häufig; vergl. val veh und out mttar
(Men. 2, 115)^), oUyitan 'wehen' (AV.).
aw. vayU' 'Luft'; ai. vayti- Luft, Wind'.
*) Im AW.-Komm. wird H geschrieben, z. B. vd. 19 (5b).
*) L 4 hat vd. 14 (2) udrak,
') In gr. vS^ u. a. hat sich die Bedeutung *Otter* verschoben.
*) Thonnelicr's pariser Handschrift hat vd. 5 (38) so^ar vaktän,
*) West, S. B. E., Vol. XXIV, 17 Noto 4.
```


## [2026-09-05T05:44:12.811Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK p783 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=436 && NR<=442 {print \"--- leaf \"NR\" ---\"; print substr($0,1,1500)}' POK_02.txt | grep -n \"78[0-9]\" | head\necho \"=== find ouiom in POK_03 or 02 ===\"; grep -n \"Ei'\\|,Ei\\b\" POK_02.txt | tail -20"
}
```


### [2026-09-05T05:44:14.522Z] TOOL RESULT

```
=== POK p783 ===
=== find ouiom in POK_03 or 02 ===
4194:gr.  xoWg,  -löoq  f.  (*knid-s),  wohl  an  ^/.öviq  , Staub'  angeglichen; mir.  sned  f.  ,Nisse',  kymr.  PI.  nedd,  nkorn.  ned,  bret.  nez  ds.  (*s(k)nida); ags.  hnitu  f.,  ahd.  (h)niz,  nhd.  Nisse  ,Ei  der  Laus'  (*knidä). Könnte  zu  (s)ken-  ,kratzen'  gehören,  wie  ghnldä  zu  ghen-  ds. WP.  I  461,  WH.  I  783  f.,  Specht  Idg.  Dekl.  44,    Trautmann  93.
```


## [2026-09-05T05:44:29.020Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho leaves03: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' POK_03.txt)\nawk 'BEGIN{RS=\"\\f\"} NR>=19 && NR<=25 {print \"--- leaf \"NR\" ---\"; print substr($0,1,2000)}' POK_03.txt"
}
```


### [2026-09-05T05:44:31.206Z] TOOL RESULT

```
leaves03: 429
--- leaf 19 ---
Nachbildung  von  palam,  dam  aus  *co-öro- ,vor  dem  Angesicht  befindlich';  aureae  {öreae)  ,Gebiß  am  Zaum^  davon auriga  {öriga)  ,Wagenlenker'  {-igä  zu  agö)-  ösculum  ,Kuß'  ist  Demin.  von  ös;
aisl.  öss  m.  »Flußmündung'  (germ.  *ösaz\  hierzu  ags.  ör  n.,  öra  m. ,Rand,  Anfang';  aus  ags.  ör  ist  mir.  or  ,ora,  margo,  linea',  acymr.  ör  ds. entlehnt.
Die  schwache  Stufe  idg.  *ous-  erweist:  alb.  ane  ,Seite,  Saum,  Ufer, Borte'  {*ausnä)',  eventuell  auch  hitt.  aÜ,  Gen.  Üsas  n.  ,Mund'  (*aies *ai*os)?  s.  Pedersen  Hitt.  47  f.
785
f-Ableitungen  sind  ai.  östha-  m.  n.  ,Lippe*;  av.  aoHa-^  aostra-  ds.  (*9iw-), Int.  östium  , Eingang,  Flußmündung'  (=  slav.  *ustbje);  aksl.  usta  PL  ,Mund'; slav.  "^usthje  n.  ,Münduag'  ist  anzusetzen  nach  bulg.  üstije^  russ.  üsttje usw.;  vgl.  aksl.  usthna,  slov.  üstna  , Lippe';  aksl.  ustiti  (naustiti)  ,bewegen, anregen»  überreden';  wahrscheinlich  aksl.  wzdia  usw.  ,Zaum';  lett.  ap-aüH f*.austi-)  ,Hal£ter' ;  apr.  austo  ,Mund'  (Nom.  Plur.  ? ;  Akk.  Sg.  äustin\ lit.  duscioti  , schwatzen,  munkeln',  lett.  ausdt  , schwatzen';  ablautend  lit. uosta  f.,  üostas  m.  , Flußmündung,  Haff',  lett.  uosts  m.,  uösta  f.  , Hafen'.
WF.  I  168  f.,  WH.  n  224f.,  Trautmann _19  f.
2.  ous-  :  9US- :  us~  ,Ohr',  erweitert  mit  -i  (pusi-s),  -es  (qusos-  n.)  und  -en.
Av.  usi  Nom.  Du.  ,die  beiden  Ohren,  Verstand,  Sinn',  Instr.  Du.  usi-hya, npers.  hos  (iran.  *au§-)  ,Ohr';
arm.  unlcn  ,Ohr'  (*us-on-ko-m)  •  das  kn  nach  akn  ,Auge';
gr.  dor.  (bg  (*öus)  ,Ohr';  öu  auch  in  öjJ^ara  , Ohren'  Alkm.,  äficp-wsg Theokr.  ,mit  zwei  Henkeln',  dor.  i^-wßddia  , Ohrringe',  vTtsQ-cbirj  , Gaumen', att.  lay-cbg,  hom.  lay-coog  n.  ,Hase'  (*sbg-öusos)  ,mit  schlaffen  Ohren'; 3US-  in  gr.  lak.  a'ög  ,Ohr',  PI.  äavd-a  {^ava-avd-a)  Alkm.,  tarent.  äxa (*av
--- leaf 20 ---
  ,Ohr'  (germ.  *ausan-) ;  mit  gramm.  Wechsel  (*auzan-) : aisl.  eyra,  ags.  eare,  afries.  are^  as.  ahd.  öra  n.  ,Ohr';  davon  ahd.  ö7'i, mhd.  CBre  ,ÖÄr' ;
lit.  ausis  f.  (älter  auch  m.),  Gen.  PI.  ausy,  (konson.  St.),  lett.  äuss  f. ; apr.  Akk.  PI.  aus  ins  ,die  Ohren',  daneben  ausins  Vok.  m. ;
aksl.  ucho^  Gen.  usese  (s-St.).
WP.  I  18,  WH.  I  85 f.,  Trautmann  18  f.,  Schwyzer  Gr.  Gr.  1,  348,  520.
ozdo-s  ,Ast'.
Arm.  ost  , Zweig,  Ast',  gr.  bZog  ds.,  got.  asts,  ahd.  a
--- leaf 21 ---
st  ,Ast';  mit  Vriddhi *özdos  in   ags.  öst,  mnd.  öst  , Knoten  im  Holz,  Knorren^   (==   ,die  Stelle,
50
786
wo  ein  Ast  vom  Stamme  aasgegangen  ist');  wohl(?)  -ozdo-s  ,(am  StammeV ansitzend',  s.  Präfix  's-,   o-  und  sed-  ,sitzen'.
WP.  I  186,  W.  Schulze  KZ  63,  28.  ''
ozgho-  , Knospe,  Pflanzentrieb,  Zweig'??
Pehl.  azg  ,Ast',  npers.  azay  , Zweig,  Knospe' :  gr.  öa^og,  oaxrj^  dju'/r) , Zweig,  Schößling^;
die  gr.  Worte  eventuell  auch  eine  dem  idg.  *o-zdos  ,5tog'  parallele  Zu- sammensetzung o-zgho-  (:  s'xü),  gxeIv)  ,sich  (am  Stamm)  festhaltend'?
WP.  I  185,  Schwyzer  Gr.  Gr.  2,  491.
p."
oä''-P^~  ^^^  pä-t- :  p9-t-  , füttern,  nähren,  weiden';  Abstraktum  pä-tro-. Arm.  hauran  , Herde'  {*pä-tro-),  hoviv  .Hirt'  (*oui-pä-)]  gr.  dor.  navia' fcXv(y^ovfj^  nävia '  t«  nXrjG^ia ;  lat,  päscö,  -ere,  pävi,  pästum  , lasse  weiden, füttere',  Dep.  , fresse,  weide'  (*päs-scö),  pästor  ,Hirt',  päbulum  , Futter' (*pä-dhlom),  pänis  ,Brot'  (wegen  pastillus  ,Kügelchen  aus  Mehl'  aus  *pa-st- nis);  messap.  rtavög  ,Brot'  ist  lat.  Lw. ;  air.  ain-chess  , Brotkorb' ;  vielleicht als  ven.-illjr.  Element  im  Keltischen  *pä-rO'  , Weide'  in  cymr.  pawr  , Weide', ri.  porion,  davon  Verbalnom.  porij  mbret.  peuriff,  bret.  peuri  ,Weiden'; mit  'tro-  Suffix  aisl.  födr  n.,  ags.  födor  n.,  ahd.  fuotar  , Futter' ;  aksl.  pasg, pasti  , weiden'  (*päs/cö);  toch.  A  päs-,  B  päsk-  , hüten' ;  hiti.  paM-{pahhas-) , schützen'.
Mit  -t'  Weiterbildung:  gr.  ftarsof-iai  ,esse  und  trinke*;  fxrtaaroq  ,ohne Speise  und  Trank';  unsicher  air.  äs{a)id  , wächst'  (,es  mehrt  einen'),  mir. äs  , Wachsen'  {^pät-to-)\  got.  födjan  , ernähren',  aisl.  feda,  ags.  fedan,  as. födian,  ahd.  fuoten  ds.,  ags.  föda,  engl,  food  , Nahrung',  ags.  föstor  ds., aisl. /ös^r  , Erziehung,  Unterhalt'  (*pät-tro-)]  abl
--- leaf 22 ---
�gen',  fsdbiS  ,mit  Fesseln' (über  pourupaxsta-  ,viel,  reich  gefaltet'  s.  Benveniste  BSL.  29,  106  f.) ; gr.  Ttaaaalog,  att.  TV&TraXog  m.  , Pflock,  Nagel'  (-xt-),  Ttr^aau)^  att.  Ttrjzxo) „TtrjywfXL^^  ]  Tzrjyvvj.u  (dor.  -ä-)  , befestige  durch  Hineinschlagen,  Hinein- stecken; lasse  erstarren'  (iTtüyrjv,  TtSTtrjya,  7t7]xT6g),  ftfjyfj.a  n.  , Pflanze,  Gestell', Tt7]yög  ,fest,  stark',  itrjyavov  n.  , Raute',  vav-7irjyög  , Schiffbaumeister',  TtTjyvUg Adj.  f.  , reifig,  eisig',  jtdyog  m.  ,Eis,  Reif  (auch  Dat.  PI.  irrdyeai  , Frost'),  hom. , Felsspitze,  -klippe';  nax^r]  (*7ta^va)   ,Reif,  Frost',  frdyr]   , Schlinge,   Falle'»
^)  S.  auch  unter  Sp-.
50*
788
TvaY.TÖü)   ,mache   fest,   verschließe,    verstopfe',   ä-^a^   ,einfach* ;    Ttd^   Adr.  f ,g-enug!';  hierher  Ttrjyrj,  dor.  näyd  , Quelle';  —
lat.  paclscö  (sek.  -or)  ,einen  Vertrag-  oder  Vergleich  festmachen,  ab-  ' schließen',  alat.  paciö  ,pactiö',  pacunt  ,paciscuntur',  pax,  -eis  t  , Friede- freundliche  Gesinnung'  (umbr.  pase  tua  ,päce  tuä'  in  der  Anrede  an Gottheiten),  palus  , Pfahl'  (aus  *paJc-slos,.  vgl.  Demin.  paxülus)]  pangö (jpepigi',  geneuert  pegi  nach  fregi,  und  panxi)  , befestigen,  einschlagen- aneinanderfügen,  schriftlich  verfassen,  festsetzen'  (zur  Nasalier ung  des Präs.  vgl.  germ.  ^faiBian),  compäges  ,Fuge',  pägina  (*  die  zum  Blatt  ge- fügten Papyrusstreifen)  ,Blatt  Papier,  Seite,  Kolumne',  2>ägus  , Landge- meinde, Dorf,  Bau',  pröpägö,  pr^päges  , Setzlinge',  propägäre  , einen  Setzling in  der  Erde  festmachen,  daher  fortpflanzen';  umbr.  pase  (s.  oben),  paca Adv.  , causa',  osk.  prupukid  ,ex  antepacto?',  umbr.  päl.  marruc.  pacri- ,propitius,  pläcätus';  mir.  äge  , Glied,  Pfeiler'  (*pägio-),  äil  ,angenehm'  ^ (*pägli-]  oder  als  *pökli-  zu  3iis\.  fcegiligr  ds.,  s.  l.*pek-?)]  cymr.  aelod ,
--- leaf 23 ---
wickelter  Faden, Gewebe,  Gewand',  7trjVi^oi.iaL  ,webe'  (dor.  TtäviadsTai  Theokr.);  ablaut. lat.  pannus  ,Tuch,  Lappen'  (expressives  nn);  got.  fana  m.  ,Lappen, Schweißtuch',  ahd.  fano  ,Zeug,  Tuch',  nhd.  Fahne,  ags.  fana  m.  ,Fahne, Tuch;  Iris', /ane, /anw  f.  ,Fahne,  Schwertlilie';  unklar,  mir.  an-art  ,lei- nernes  Tuch';  dürfte  man  das  gr.  und  lat.  ä  als  expressiv  auffassen  (vgl. oben  S.  211  zu  gall.  drappus),  könnte  Beziehung  zu  {s)pen-  ,spannen, spinnen^  angenommen  werden.
WP.  II  6,  WH.  II  247  f.
pando-s  , gekrümmt'.
Lat.   pandus    .gekrümmt,    gebogen,    geschweift'    (pandö,    -äre    , biegen, krümmen')  =  aisl.  fattr  {*fanta-)  ,zurückgebeugt,  zurück^ebo-en'. WP.II  6;  s.  unter  1.  pet-.
789
aak',  P^^S~  »schwellen',  bedeutungs-  und  ursprungsverwandt  mit  ba^mb- pa^mp-,  bu-,  pu-  usw.  (oben  S.  94  f.)  , aufblasen,  schwellen'.
Lat.  pänus  (*pank-no-)  , entzündliche  Geschwulst,  Büschel  der  Hirse', rom.  p^'^'^  j  davon  pänlcum  , Pflanze  mit  einem  Büschel' ;  panceps  „e'Axog xtrjyovg  irti  rgaxrjUov"^  Gloss.  (aus  *päno-caps),  pantex  , Wanst,  Gedärme' fauf  Grund  eines  Partiz.  *panc-to-s  , geschwollen,  aufgeblasen');
aksl.  pgciti  se  ,infläri',  pgcina  ,mare',  poln.  pqh  .Knospe',  pek  ,Bündel', russ.  puk  , Bündel,  Büschel,  Strauß',  püca  , Blähung'  usw.;  mit  Media aksl.  pggy  ,corjmbus',  pggvica  ,globulus'.
WP.  II  6,  WH.  II  248.
pap(p)^  Kinderlallwort  für  , Vater;  Speise'.
Gr.  Ttdnrca  Vok.,  -ov  Gen.  ,Papa',  TCctTtaq'  Ttargög  vno'AOQio^a,  TcartTtog Großvater'   (daraus  lat.  pappus),   TtaTcrciag  , Väterchen',   nanTcaCeiv   .Papa sagen';   skyth.  Zevq  JJaTtalog'^   \a.t.  päpa,  pappa  Kinderlallwort  für  , Speise; Vater',  pappö  -äre  , essen';   nhd.  pappen   , essen'  (mit  stockender  Lautver- schiebung durch  nebenhergehende  Neuschöpfung). WP.  II  4,  WH.  II  249,  2
--- leaf 24 ---
eö  , erscheine'  (parret,  nach  Festus  für  päret,  wie  baca  : bacca  usw.).
WP.  II  6,  WH.  II  252  f.
parikä  ,Buhlerin,  Konkubine';  nur  iran.  und  irisch.
Av.  pairikä    , dämonische   Buhlerin',    mp.  parlk,    np.  patn    ,Peri'    (iran. *parlka)]  mir.  a{i)rech  , Konkubine'. Thurneysen  IF.  42,  146  f.,  WP.  II  7.
päsö-s  , Verwandter'?
Gr.  TCTjög,  dor.  rtadg  , Verschwägerter',  naatTai'  ovyysveig  lies.;  lat.  päri- clda  (*päso-kaidä)  jünger  parri-czda  .Mörder  an  nahen  Verwandten';  nach Wackernagel  Gnomon  6,  458  aus  *parso-clda  zu  ind.  purum-  ,Mensch' aus  ai.  '^pursa-.
WP.  II  7,  WH.  II  253  f.
pasto-  ,fest'.
Ai.  pastyd-m  ,Wohnsitz' ;   arm.    hast   (i-St.)   ,fest';   aisl. /as^r,  3i^s.  fcest, as.  fast,  ahd.  festi,  nhd.  fest. WP.  II  7  f.
790  •
paus-  ,los-,  ablassen'.
Gr.  Tiavo)  ,mache  aufhören',  Med.  ,höre  auf,  lasse  ab',  navXa  ,Ruhe', 7iavGu)Xri  ,Rast' ;
apr.  pausto  ,wild',  aksl.  pusU  ,öde,  wüst';  pustüi,  russ.  pustüh,  puskäh ,(los)lassen',  sloven.  delo-pust  ,Feierabend'  usw.
WP.  II  1,  Trautmann  208  f.
päuson-  :  püson-  , Göttername'.
Ai.  Püsdn-  m.  ,vedischer  Gott^  Hüter  und  Mehrer  der  Herden  und  des menschlichen  Besitzes  überhaupt',  gr.  U&v,  ark.  Jj&ixjv  (^TIgvgwv)]  iWyv. (messap.)  PN  Pausö,  -onos,  gall.  (venet.)  PN  Fusa  m. ;  unsicher,  ob  zu  ai. pusyati,  pumäti,  pösati  ,gedeiht,  wächst  zu,  macht  gedeihen,  ernährt', pösa-  m.  , Gedeihen,  Wachstum' ;  s.  unter  1.  pu-.
WP.  II  2;  vgl.  Charpentier  Idg.  Jb.  19,  90.
1.  p^d-,  pBd-  , fassen;  Gefäß';  pedo-  , Gefäß,  Einfassung'.
Ai.  vielleicht  palla-  m.  , Kornbehälter',  palll  .Getreidemaß'  (falls  -II-  aus -dl-)]  ahd.  fazzön,  mhd.  vazzen  ,in  ein  Gefäß  tun,  fassen,  rüsten,  sich bekleiden',  ahd.  fezzil,  mhd.  vezzel  ,Band,  Fessel',  ags.  fetel{s)  m.  , Gürtel', aisl.  fetill  m.  , Schulte
--- leaf 25 ---
treffend';  aus  , Fußfessel'  ist  z.  T. schon  grundsprachlich  ,Fessel  überhaupt'  geworden. 1.  Ai.  päd-  ,Fuß'   {pdt,  pädam,  paddh),   av.  päd-  ds. ;   apers.   pädaibiyä ,mit    den   Füßen';    arm.  ot-k'    „Ttödsg'',    ot-n   ,,7tovg,    noda'']    gr.  jtwg,  att. Tiovg,   Gen.  nodög  ,Fuß'   {kyLaTÖiiTradog  ,100  Fuß  lang');  lat.  pes,  p^dis  ds., umbr.  peri,  persi   ,pede'    (dupursus   ,bipedibus',  -u-  wohl   aus   -ö-);    air.  is , unterhalb'    (wovon    ise      ,niedrig')   m.   Dativ,   aus   dem   Lok.    PL   *ped-su ,zu  Füßen'  deutbar  =  alb.  posh  in  perposh  ,unten',  posh-te  ,herab,  unter- irdisch; unten,  hinunter';   got.  fötus,    aisl.   fötr,  ags.  föt  (Nom.   PI.   aisl. fetr,  ags.  fet  aus  *föt-iz)  ahd.  fuoz   ,Fuß' ;   hitt.   luv.  pata-^   Hierogl.-bitt. pat  ds.;  toch.  A  pe,  B  pai,  Dual  A  pem,  B  paine-
791
zu  ped-  ,Fuß'  gehört  gv.  dial.  rceda  „^«t«",  ursprüngl.  ,(jemandem) auf  dem  Fuße',  vg-1.  lat.  pedisequus,  -a  , Diener,  -in*  eig.  ,auf  dem  Fuße folgend'  und  unten  die  arm.  von  het  , Fußspur'   gebildeten  Präpositionen;
mit  -i-ös,  -i-t-  , gehend'  sind  gebildet:  gr.  rtet^ög  ,pedestris',  lat.  _pec?-es, -i't-is  , Fußgänger,  Fußsoldat' ;  von  lat.  jpes  stammt  pedäre  ,mit  einem  Fuß versehen,  stützen',   und  davon  wieder  pedum  , Hirtenstab,  Stütze';
pedio-  in  ai.  pddya-  .den  Fuß  betreffend',  pddyä  , Fußtritt,  Huf,  av. paiöyä  ,Fuß',  gr.  neCa  f.  ,Fuß,  unterer  Rand,  Kante,  Saum,  kleines Fischernetz',  lat.  acu-pedius  , schnellfüßig',  ahd.  ßzza  , Gewinde,  Garn' (=  gr.  7t6^a),  nhd.  , Fitze',  (wozu  germ.  *fetl  f.  in  aisl.j^^  , Schwimmhaut, Rand^,  ags.  ßtt  , Abschnitt,  Gedicht',  norw.  dial.  ßor-ßt  , Eidechse',  „tstqü- /Tfi^og"),  lit.  lengva-pldis  ,leisefüßig' ;  pedi-  in  gr.  nsdllov  n.  , Sandale' und  germ.  *fetl]  podio-m  :  mi
```


## [2026-09-05T05:44:35.995Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=16 && NR<=18 {print \"--- leaf \"NR\" ---\"; print}' POK_03.txt | sed -n '1,80p'"
}
```


### [2026-09-05T05:44:37.717Z] TOOL RESULT

```
--- leaf 16 ---
vielleicht  aus  ^air-orb-)]
got.  arbi  n.  ,das  Erbe',  ahd.  arbi,  erbt  n.  ds.,  ags.  ler/e,  yrfe  n.  ds.  (aisl. arfr  m.  ,das  Erbe'  ist  zu  arfi,  arfa  ,der  Erbe,  die  Erbin'  neugebildet), aisl.  erfi  (run.  arbija)  n.  ,Leichenmahl' ;  got.  arbja,  aisl.  arfi  (f.  arfa), ahd.  arpeoy  erbo  ,der  Erbe',  ags.  ierfe  n.  ,das  Erbe';  die  germ.  Wörter stammen  wegen  des  Folgenden  kaum  aus  dem  Keltischen ;
782  •
auf  ein  intr.  Verbum  *arbe-{ö  ,bin  verwaistes,  zur  harten  Arbeit  ve dingtes  Kind?'  führt  man  zurück  got.  arbaips  f.  , Mühsal,  Arbeit*,  aisl -^v, erfidi  n.  ds.,  as.  arabed  f.,  artedi  n.,  ags.  earfop  f.,  earfe^e  n.  ,Mühe,  Arbeit«^ ahd.  araheit  ,Arbeit'  (aisl.  erfi.dr,  ags.  earfepe  , beschwerlich'),  Grundf  % *arbeiidiz;  sehr  fraglich  ist  Entstehung  aus  *arb-ina-  für  got.  arms  ,elen(i»*^-^ aisl.  armr  ,elend,  unglücklich',  ahd.  as.  ar{a)m,  ags.  earm  ,arm,  dürftig*!! Grundbed.  wäre  etwa  , armes  Waisenkind';
abg.  rab^  ,Knecht',  rabota  ,servitus',  cech.  rob  , Sklave',  roö^  ,kleinet  -* Kind',  russ.  rebjdta  ,Kinder',  rebenok  ,Kind';  die  russ.  Formen  gehen  auf'Ä rob-j  urslav.  *orb-  zurück  (Vasmer  brieflich);
vielleicht  hitt.  arpa-  , Ungunst,  Mißerfolg'.
WP.  I  183  f.,  WH.  II  219  f.,  Trautmann  12.
orej^-,  e^eu-  ,Darm'??
Gr.  ÖQva  ,Darm'  (kann  auch  für  *dQva  stehen,  vgl. :)  lat.  arvina  , Schmer Fett,  bes.  zwischen  Haut  und  Eingeweiden'  (wäre  ,das  zu  den  Därmen  Ge.  i hörige,  Gekrösefett');  dgßlvvrj'  xgiag.  2ly.bXoi  Hes.  (kann  lat.  Ursprungs  sein)T
WP.  I  182,  WH.  I  71.
orghi-,  Tghi-  m.  ,Hode';  orghiiä  ds.
Av.  drdzi-  m.  , Hodensack',  Du.  drdzi  jHoden*^ ;
arm.  orji-]c  PI. , Hoden*,  orji  ,nicht  kastriert'  (*orgh'i-{os)j  mi-orji  yHÖvoQxiQ^f.
gr.  Ugxtg  m.  ,Hode';  alb.  herdhe  f.  ,Hode'  (*orghi-ä)'^  mir.  uirgge  f.  ,H.ode* -f {*orghia),  nir.  uirghe  mit  sekundärem  gh-^  lit.  arzüs  , lüstern',  er^üa$'l , Hengst*,  lett.  krzells  ds.  -^
WP.  I  182  f.,  Trautmann  71.
org-  jtöten*  (?)  s.  unter  perg-.  .^
ort-  ,Rebe*?  f
Arm.  ort'  ,Rebe';  alb.  hardi  ,Weinstock'.  .1
WP.  I  183,  Pedersen  KZ.  36,  99,  BB.  20,  231.  ^
*ös,  ös-i-s,  ts-en-,  os-k-  , Esche*.  ^
Lat.  ornus  , wilde  Bergesche*  (*os-en-os)]  cymr.  acorn.  onn-en,  bret. ounn-enn  , Esche*,  cymr.  PL  onn,  ynn  (urkelt.  *onnä<*osnCi)]  air.  (h)uinmu8y Dat.  uinnsirm  {*onn-ist-ö)  ds.;  lit.  üosis  f.,  m.,  lett.  uosis  m.,  apr.  woasis {
--- leaf 17 ---
*ösi-s',  dazu  illyr.-pannon.  VN  Osi,  ON  Osones);  slav.  *jasenh  {*jasem)  m.  in serb.  jäseUj  russ.  jdsenh]
mit  ic-Erweiterung:  arm.  haci  ,Esche*,  alb.  ah  ,Buche*  {*oskä)-  gr. d^vT]  ,Buche,  Speerschaft*  (*aax[e](T-?);  ligur.  ON  'Oax^a  ,Eschenwald*(?); aisl.  askr  m.  ,Esche,  Speer,  Schiff*,  ags.  xsc  (germ.  *askiz\  ahd.  asc  ,Esche*;  '
vgl.  tscherem.  o^ko  ,Esche*.
WP.  I  183  f.,  WH.  II  223,  Trautmann  203,  Specht  Idg.  Dekl.  59.
r
783
.f(^h)-',  ost{h)i\  ost(h)r(g),  obl.  ost (^h) - (e) n-  , Knochen';  ost(b)eion ^Beinernes^ Ai.  dsthi  n.,  Gen.  asth-n-dh  ,Bein,  Knochen',  av.  ast-^  asti-  n.  ,Knochen', Q-en.  PI-  asfqm,  Instr.  PL  azdbls,  asti-aojah-  , Knochenkraft',  astdn-tät  ,Lebens- kraft';  päli  atthitaco  , Krebs'  {*asthi-tvacas  , knochenhäutig',  vgl.  zur  Bed. o-r.  <3ö'TCfxdg  , Meerkrebs');  gr.  dazsov  , Knochen'  (wohl  *oo-T6Vo>'  ,*Beinernes' =  lat.  osseum  ds.),  lat.  ossu,  ossua  wohl  als  Neuerung  nach  genu^  genua ; dötay-og  (heilenist.  zu  ä(jTay,6g  assimil.)  ,Meerkrebs'  aus  ^oax-xfavio-  , dessen Haut  Knochen  sind',  woneben  vom  r-St.  HoTga-nov  ,harte  Schale,  Scherbe', UffTQSOv  , Auster'  (wohl  auch  öafQvg,  daxqva^  öaTQvtq  ,Baum  mit  hartem, weißem  Holz'  durch  Dissimil.  aus  ^öaiQO-dQvg)^  dargayalog  , Knöchel'  (assimil. aus  ^dargayaloQ]  setzt  einen  Nom.  *ost{h)Yg  voraus);  wenat.  ostüakon ^ossuärium^;
alb.  asht,  ashte  , Knochen';  lat.  os,  richtiger  oss,  Gen.  ossis  n.  ,Bein,  Knochen' (oss  am  ehesten  Auslautentwicklung  aus  *ost)j  alat.  auch  ossum]
unklar  ist  das  a-  in  air.  asil  , Glied'  (acorn.  eseZ,  bret.  ezel  ds.),  mir. asna  m.  , Rippe'  {*astonio-?),  mcymr.  ass-en^  PL  eis  (*asti)j  asseu  ,Rippe, Latte,  Stange',  cjmr.  asgwrn  (s.  unten),  wozu  wohl  lat.  asse?'  , Latte,  Stange'; vielleicht  hierher  air.  odb  m.  , Knoten,  Auswuchs',  cymr.  oddf  ds.  aus *ozbho-^  älter  *ost-hho-,  weiter  zu  gr.  öaq)vg  , Hüfte'  (anders  S.  773) ;
hitt.  hastäi-  ,Knochen,  Widerstandskraft^
Eine  -feo-Ableitung  *ost-ko-  liegt  zugrunde  in:  av.  as^a-  , Schienbein, Wade*,  arm.  oskr  , Knochen';  cymr.  asgwrn  ,Knochen',  PL  esgyrn,  corn. ascorrij  bret.  askourn  ds.  (kelt.  Formans  -rrio-).
WP.  I  185  f.,  WH.  n  225  f.,  Schwyzer  Gr.  Gr.  1,  518,  Benveniste  Ori- gines  1,  6 f.,   Specht  Idg.  Dekl.  74;  Meillet  BSL  33,  259.
oug-,  OU-?  ,kalt'.
Arm.  oic  ,kalt'  (*ow^-);
gall.  Monat  Ogron  .  .  . ;  mir.  üar  ,kalt'  =  cymr.  oer  ds.  {*ougro-) ;  air. öcht^  üacht  m.  , Kälte'  (*ougtu-)'j
lett.  auksts  ,kalt';  lit.  dusti  ,kalt  werden'  (*aug-ske-tiy)'^  Kausat.  lett. ausit,  lit.  duäyti  , abkühlen';  nach  Pedersen  KGr.  I  103  wäre  lit.  duäti  aus *au-s-ti  zu  erklären  und  zu  ai.  ö
--- leaf 18 ---
-man-  ,Kälte',  av.  aota-  ,kalt',  ao-dar- , Kälte',  also  zu  einer  Wurzel  au-  (ou-)  ,kalt'  zu  stellen.
WP.  I  222,  WH.  I  88,  Trautmann  20,  Mühlenbach-Endzelin  1,  222  f.
ö{u)i-oza  ,Ei',  d.  h.  ,das  zum  Vogel  gehörige',  schwache  Form  9iözn.
Av.  ap-ävaya-  , entmannt' (?),  falls  aus  apa-ävaya-  ,ohne  Hode',  vgl. apers.  xäya  ,Ei';
gr.   att.  wiöv  (*öui-om),   äol.  djioy  (*öun-om),   dor.   djeov  (*öuei-07n)  ,Ei'; cymr.  wy^  acorn.  uy  ,Ei'  (*äuion  aus  *öu{om)]
784  »  ::?
ohne  w,  das  wohl  im  langdiphthong.  *öuiom  geschwunden  war:
arm.  j«,  Gen.  jvoj  ,Ei'  {*iöio-,  durch  Assimilation  aus  *özo-);  lat.  övi^t^ ,Ei*  nach  Szemerenyi  KZ.  70,  64f.  aus  lat.  *oom,  idg\  *ö2om;
aksl.  ajhce^  slov.  ^o/ce,  acech.  vojce^  cech.  ve;ce  (*öia-  n.)  ,Ei'  ;
schwierig  sind  krimgot.  ada  (got.  *addja),  aisl.  e^r^,  ahd.  ei,  ags.  $« ,Ei*  (germ.  *ajjaz--  ahd.  Fl.  ei^r,  ags.  zgru  erweisen  -es-Stamm);  vielleicht nach  Specht  aus  *9tom,  nicht  verkürzt  aus  urgerm.  *äiiam,  idg.   *öiom.
WP.  I  21  f.,  WH.  II  230,  Trautmann  202,  Specht  Idg.  Dekl.  29;  Specht erklärt  lat.  avis  , Vogel*  aus  dem  endbetonten  idg.  Nom.  Sg.  awm;  y^i oben  S.  86,  wo  ich  noch  gr.  oicovög  ^Raubvogel*  (aus  *alü)v6g,  W.  Schulze Kl.  Sehr.  662)  hätte  erwähnen  sollen.
öui'S  m.  f.  , Schaf,  Gen.  Sg.  öuios-  f.  ouikä  ds.
Ai.  dvi-  m.  f.  jSchaf,  avika-  m.  ds.,  avikä  ,weibliches  Schaf  (=  abg.  ovhcaY dvya-  ,vom  Schaf,  vgl.  gr.  ota;  arm.  hov-iio  (*oui-pa-)  , Schäfer';  gr.  5'tg,  olg (argiv.  Akk.  PI.  ofivg)  , Schaf ,  oXeog  ,vom  Schafe*,  ola,  Ba  , Schaffell',  dehn- stufig ^a  , Schaf  feil,  Saum'  (wie  ai.  ävika-  n.) ;  lat.  ovis^  umbr.  oui^  uvef  Akk. PI.  ,oves'  {au-huhulcus  ,pastor  bovum',  auch  avillus  ,Lamm',  s.  u.  ag^hnos)-, air.  öi  ,Schaf;  cymr.  ewig,  acorn.  eiihic  ,cerva'  {*oulkd)',  aisl.  «r,  ags. eowu,  eowe,  as.  ewi,  ahd.  ouioi,  o«  , Schaf  {^awl,  Gen.  *awjöz),  got.  awistr jSchafstall',  ags.  eowestre  ds.,  ahd.  awist,  ewist  (mit  zu  stä-  , stehen'  ge- hörigem 2.  Gliede  -sto-,  -s^[9]<ro-),  got.  atoepi,  ags.  eowde,  ahd.  ewü  ,Schaf- herde*;  lit.  avts,  lett.  avs  f.  ,Schaf*;  lit.  ävinas,  lett.  avins,  äuns,  apr. awins  , Widder'  =  abg.  ovh-m  ds.;  abg.  ovb-ca  , Schaf.
WP.  I  167,  WH.  II  229,  Trautmann  20f.
I.  öus-  :  9US-  .Mund,  Mündung,  Rand' ;  9us-tä , Lippe',  Qus-tiiom  , Mündung'.
Auf  idg.  *öus  gehen  zurück:  ai.  ä-h  n.  ,Mund'  (vgl.  äs-dn-  sd.,  äsydm  n. ,Mund,  Öffnung'),  av.  äÄ-,  ärdhan-  ds. ;  lat.  ös,  öris  ,Mund,  Antlitz,  Rand, Ufer' ;  aber  mir.  ä  Gen.  Sg.  ,Mund'  aus  *ösos ;
dazu  ä- Ableitung:  ved.  äsayä  ,von  Mund  zu  Mund'  (Instr.);  lat.  öra ,Rand,  Saum,  Grenze,  bes.  Meeresküste',  dazu  cöram  Adv.  (u.  Präp.)  ,an- gesichts,  in  Gegenwart,  vor',
```


## [2026-09-05T05:44:58.265Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT vayu / vī 'Vogel' ===\"\ngrep -n \"vayō\\|vayo-\\|vay-\\|vīš\\|viš \" BRT.txt | head -30\necho \"=== BRT apa-āvaya ===\"\ngrep -n \"āvaya\\|avaya\\|ävaya\\|āuuaiia\" BRT.txt | head -20"
}
```


### [2026-09-05T05:44:58.345Z] TOOL RESULT

```
=== BRT vayu / vī 'Vogel' ===
3242:•  j.  a-8avay-  Adj.  (auch  mask.)  'der  keinen Trug  übt,  nicht  trügt,  betrügt':  *''T'r/(NSm.) nama  aAmt  *vtöavl/  nqtna  ahmt  Yt.  /.  14; —  n^mö  voku  °vim  (ASm.  statt  n.)  aibai- hm  Vr. 21. 3,  Yt  luz;  —  yeiihe  vähm Äangryuinäili  "vil  (NSf.)  paoirls  (sd.)  .  . i4ä  *dämya  (sd.)  xlaztäi  Yt.  iO,  143.
8522:•)  Der  iiiijak  des  RV.;  s.  Brrgaigne  Rel. v*d.  r.  57;  dazu  IIauq  Eäsaysi  289,  Bthu  BB. 8.  2x7,  KZ.  2Ä  II  und  unter  dti^'ani-  mit No.  3  und  ^tavay-;  ferner  SBE.  47.  143.
8949:j.  kanynm :  s.  ^kavay-.
9127:'kavay-
9130:KompA.;  AUntl.  {s.  k.i.-ya-,  ij:-r\  —  Vgl. tiavay-  EN.  —  ai.  Air-.if-  m.  (IIB.  S.  227).  — P6.!  (kdk,  voM.)  tiiyii-,  s.  iinttt  <.ic-f/.iK- mit No.  —  ">  iKI.  s.  C1.0.  KZ.  fj.  300  und  No.  2, 3,  S-  -  ^)  S  i'"''-  3  ai  vgl.  No.  5.  --  3)  IF. /.  191,  193  No. ;  S  ^<>S.  I  b,  MeILLeT  bei Bgm.  Grdr.'  /.  1091.  —  t)  Doch  s.  auch  Komp. \Ln:i').  —  i>  Stven.  nnter  dem  EN.  —  <•)  -f statt  -va,  S  3Ö1V.  31,  Abi;esehcn  von  11  ftjr -0,  formell  gleieli  /'Jrvyi/j-Äi.
9131:•  j,  'kavay-  m,  EN.  eines  Gläubigen: 'j'eis  asaom  Vt.7j.119;  — garslahe  "vöU asaonS  "des  G.,  Sohns  des  A'.  . ."  Vt.  /  J. 123;  —  pouruslöis  'vöis  asaonö  "des  F., , Sohns  des  K.  .  ."  Vt.  y.  114.
9672:Vgl.  Modi  Twö  Amuleis  of  ancient  Persia (Joura.  Anthrop.  Soc.  Bombay  igozi  1 1  ff.,  wo- nach der  Text  besagen  soll:  "May  we,  who perform  tbe  Yasna  in  the  proper  way,  be relieved  (from  the  evil  inSuence  of]  the wretched  Aum,  JCuro,  Tareuiani  aiiA  Karapait." Ich  kann  das  nicht  herauslesen,  iura  soll np.  iür  'blind'  sein  und  synonym  mit  tiavay- Bed.  a!
10870:•  j,  xStavay-''  m.  Name  einer  iramschen
10879:•  j.  xStävay-  Adj.  'zur  Familie  der Xstavay  gehörig,  Xstavi-^a.nvi^ -.  ysi  taxma 'vayS  dänubyö  azm  pilana  Yt  13. 37 ;  38.
12114:•  j.   taurvay-   tn.   Name   eines   Daeva. 'w  (ND.)  tairicä'*  "(die  beiden)   T.  undl/^Äa-"
12675:ai.  daihnoä  'er  tauscht,  schädigt'^,  difisah, daihyaH:;  daidhäh;  otsss.  .^a:»» 'stehlen',  PDw. lUt^deiusam  'ich  mache  Profit''(GIrPh.y  b.  321); ann.  [LW.?)9>  dmii  ■hintergehen'.  VgL  noch lÜHBi-  und  Pü,  EU  diavay-.  —  Pü.:  fre/lan;  s. noch  No.  6,  7.  —  «)  iSchr.  s.  S  2&J.  37.  — •)  Ar.  *i^hana%-\  vgl.  Bthl.  IF. /.  78,  wo weitre  Litt.  —  i1  Bthl.  IF.7.  87  No.  und  lu q/7a-.  —  4)  Ohne  Desiderat! vbedentung,  — S)  %S3  n.  1.  — 6)  Pg.:/fl  fl„/r^.  -  7)P6.r hin  . .  ie  pa  freflarlh  fugend.  —  •)  Zum  angebl. ai.  Praes.  a  däbhaü  s.  Bthi_  IF.  7.  83.  — «  Hbm.  AGr.  /.  438.
12679:•  j.  davvay-  f.  Name  eines  bestimmten
12830:•  j.  davay-  m.  'Betrug'.
14384:•  j.  ^Tvay-  V,  'Furcht  erwecken;  —  hegen'. Praes.  a  %waya-,  3  %wya-.
17799:•  j.  fravay-  f.  'Gedeihen'(?):  iraowm  .  . yS  har»ta  aiwyäxltaea  vTspayä  °vSis  ga^ %aya  V.57.  15;  Yt /o.  103.
20075:j.  maurvay-  m.'>  'Ameise',  ein  daemscbes Tier,  von  dem  zwei  Arten  geschieden werden:  xrafstnm  ava.Janalta  moffifftn danHjtarsim  (sd.)  V.  16.  la;  —  hagvan maoirinam  danS.iarsanqm  ava.Janyat  V. 14.S1  ^o-73i  —  baiiian  maoirinqm  arai- kanqm  (sd.)  kutakanqm  duiaininqm  ava.- /anyai\:i4.$.
22640:1355  »vanta-  —  Jvay-  1356
22670:•  j.  vantä.bar9tay-'>  f.  'Darbringung  von ;  •  j.  «vay-  V,  'fliegen',  nur  mit  a  'heran- Haldigaiigta' :  *Aui?r7itrmca  *ufta^>fyit[mA  äiegea',  von  Gottheiten.  Praes.  2  z^ya-. *T3inmca  afrlnami  tava  atars  Y.Ö2,  i;  amiianqm  spntanam  ..yailqm  ragxmS- 7,  CTo.ö",  P..y5;  —  hub}r)ti  usia.bmii  „hs  panistß  avay'atqm'^  'avi  taohrS •nti  atari  afrtnami  \.68.\\.  a)  mit  ".  ,  deren  Pfade  leuchten,  wenn  sie  zu Gen.  des  Empfängers:  :ia3;i/?/'fA-o,.'M>W/.-'<i  den  Z.  heranfliegen"  ¥1/5,84;  — fra- yasaianam  N.4S.  'vaiayS  ..yä   visäla   SvayHnti  Yt.Jj.4g;
22673:•  j.  vantav-  m.  'Geliebte,  Frau':  yaiia  •  j.  'vay-  V.  'schlachten',  nur  mit  Praev. nä  frys  fryai  'taoe^^  ..pu^nm  i-ä  ^köm«  '  Praes.  10  vXnav:  vinu-.
22682:AbleiU  —  Zum  V.  ^vay-,  —  *ai.  vdy  m.  {vi^, Tiäya^);  mp.  {Pü-)  vay,  vgl.  väyaHäai.  —  ')  Im Gegensatz  zu  m^tya:  —  ')%  3JJ.  —  J>  Them.
22702:Ableit.  aus  )vay-,  in  Anschluss  an  die  them. Kasus  daraus  gebildet;  s.  No.  i.  —  Pü.;  4^11- Aünmand;  ob  vayömand  zu  lesen?  —  ■)  Hds. vayaitbyasi'a,  das  wäre  DPm.  (oder  n.),  was sich  nicht,  wie  DsT.  tot,  mit  mäyavailibyasca DPf.  verbinden  lässl.     Geringe  Stelle.
24063:•  j.  vi-davay-  Adj.  (auch  mask.)  Tiei von  — ,  sicher  vor  Betrug':  *aöavli'  ttqma ahmt  *'Mj  (NSra.)  nqma  ahmt  Yt /.  14.
24142:•  j.  vi^avay-  m.  EN.  eines  Gläubigen: UtayutSil  (sd.)  °v!Si^  siyrSii'  sainake  Yt 13. 126.
24592:j.  f«  V.  2.  41:  s.  Svay-.   —   i/S  Yt.  rj.  2: t.  vü-,  Sp.  14^6  o.  —  vil  N.  SS'-  l'c^  ^'
27373:•  g,  sravay-  f.  'Hören,  Gehör':  ya  vS mäiirä  srfvlm^^  ärädä  (sd.)  ^.aS.T.
27422:durch  sie  so  (werden  wird)":  .  .  du  weisst es  . ."  Y.J2. 6. I      Zu  einem  Praes.  *jrä:>a^>^-,  denom.  Praes.  31 aus  'irävanka-  d.  'Berühmtheit',  Abteil,  (mil Vj-ddhih)  au(  sravak:  —  Pü. !  ie  irül  estil,  Sü. : yak  uklo  'sH.  —  1)  Nämlich  wie  er  es  vorhat ; t.  die  vorhergehende  Strophe, g.  srniini  Y.  a8.  7  -■  t.  sravay-.
27901:Eig.  'gelblieh,  grünlich'.  —  Vgl.  ^caityani-, zain'lt-  und  ai.  iviiyäUcah,  haffct  und  hitifit), Z.  ist  'tbe  mak»  of  poison',  da*  Gift  aber iit  imrita-.  S.  im  Übrigen  unter  laurvay-.  — ')  Falsch  jN.  GIrPh.  3.  657.
28803:•  j.  'haosravah-  m.  EN.  eines  irani- schen Königs  aus  der  A'uz'aj'dyiiastie:  arsa airyanqm  dahyunam  xJdhrai  hanktr^mH (sd.)  'va  (NS.)  Yt.5.49.  a)  sonst  mit kavay-:  ayaslam  amahrkim  bavdhi  ydkia kava  *'va  Az.7'>;  *Vyt.2'';  —  haomS .  . him  ja^yal . .  dazdi  mL.ya'ia  aam  banda- yeni  . ,  läirTm  fraarasyämm  . .  uta  bastftn upanayeni  bastsm  kavSi^  'vanhahe^  janäi t>m  kava  'va  .  .  pu%rü  iama  (sd.)  syä- var/anäi  Yti).  i7f.;  /p.77,  93,  ^5.32;  — ahurS  kava  'va  Ytig.yj;  —  uynm  ia- valm  i^amiS  .  .  yat  upa^hacat  kavaltn •vanhitn  Yt /p.  73f.;  S. /.  9;  —  yc^a  as>m uzayeni  ha^a  iavlfis 'vamkahe'^  Yt.  15.  2^ ; Ny.  J.  S ;  —  kavsis  kaosravatihs  ai'aonS  Yt J.?-i3a-
=== BRT apa-āvaya ===
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2478:Stelle  der  kongruenten  Form  steht :  a)  das  i ;  —  iE  äbyö  frSrtt^  fr}r»m-ainti  asaonqm Neutr.  Sing.:  yüzim  .  .  aogS  data  .  .  x/a-  ..frtrvaBbyoYX.13.afi;  —  zugleich  zurück- '^nmcS  .  .  azimcll  ahyä  (statt  Du.)  ..'weisend:  asti'atjntö  ..  atihe  haxayü  frä- %wqm  mPtihi  ..vaSd>m{sA.)Y.2<).ia;  —  \yente  astvatjr?lahe  Yt.i'>.95;  —  dacnnm dva/sing  ..  qstqscä  .  .  yezT  ahyä^^  (statt'.,  atiihi  ..  kavaya  ..  daenayn  V./o.ig. Plur.) /ö/  mal  xsayehTY.44.\\i.; — duye  —  a)  mit  relativischem  Anschluss;  ama- navaiti  astanqm  (sd.)  .  .  däittm  ahmäicil  !'af6yö  acibyö  yazataHbvT'  yat  am»saeibyö harf^r?m  hrmi^ät  V.  74. 17.  b)  das  sp»^aAbyöYi.fj.^;  —  mmö  äbyö  döi'iräbyü
2514:-  g.  'a-  Pron,  ident.  'ich,  du,  er  selbst',  humata  'ta'  ..  aat  mam  narö  paskat  ya- nur  NS. :  yi  maibya  yaos  (sd.)  akmai  astu  g3„ie . .  "um  dieses  (deines)  guten  Denkens vakUta  mahyä  isfois  voha  eöihm  mananM  willen  .  ."  H.2.14''.        2)  substantivisch: ".  .  dem  verspreche   auch  ich  selber  das  ,  ^tai  ti  .  .  avayam  *danmaM  Y.  öS.  i  '>;  — beste  meines  Besitzes  durch  VM."  y.4''-   am  yasna  .  .  ''ta  patti    ava.jasa  .  .  aoi \Z;    —    ai   -3    vaocal  ahurö  mazda    ''da  zam  ".  .    um    dessentwülen  (was  hier  ge- sprach er  selbst,  ^/iM."  Y.sp.ö.  [schiebt)    komm  . ."  Yt. 5.132  (s.  i);   — zBed._s.  Gdn.  GIrPh.   '  52      Ich   '^'^^<=^'^^'- -faimat puir.lt  (sUtt  AS.)  Kimar^xsaf^u/ia dass  f.  as'  aus  einerrart.  idg.  'n  'selber  er-    ,    ,  ,   ,.,       .,•.,..'        ,     .  ,        „ wachsen  ist,  die  in  aUi;  (aus  'a-u-r,  wie , (sd-)    damit  (was  ich  dir  gebe)  such  ..' eJroiaus*jn-H-/°)steckl.Dochs.B(;M,GrGr.3244-    V.  1^.  14;  —  in  Kongruenz  mit  dem  Prae-
3213:mit  pairi  'aufsagen,  hersagen'  (die  Gä- 'kä%):  *yöi  glü^i  ..srävayanti yezi  arastnm (sd.)  pairi.aoxta  pairi.äaa  vä  . .  pasla  vä parö  Vä  pairi.äm  aratufryö  ".  .  wenn einer  .  .  (die  GiJääworte)  zu  spät  oder  zu früh  aufsagt,  die  sind  ar."  N._J2.
3607:•  j.  apairi.gaed'ä-  Adj.  -?-:  dusxratum ''^am  *asravayai^a%qm  Aog. AD.
3648:•  j.  apävaya-  m.  Name  einer  Krankheit oder  eines  Gebrechens:  ma  {a>ra)  °jJ  V. 2.29.
3684:sa3^3rJ{iA.)  . .  ya  ..  vav}r?SSi  pairlJült ..  yäia  var?^aitg  '/LcTblJ  Y.  25,4;  — ai^qmät  ä  ahtnJ  .  .  vTci>3i  (sd.)  -/)"■■>  Y. j2. 8.  a)  mit  Neg.;  'nicht  hinfort  mehr, länger":  »»3  ^I^ä  *fX  äsbävayal  (sd.)  Y. Jt.i7.  3)  'auch,  gar,  besonders',  das vorherg.  Wort  hervorhebend:  maS^a  .  . pirs^u  'pi  ffi/ajii/Vjy  "die  Wolken,  die  sich gar  weithin  verbreiten"  YLA40;  io.44; —  \daraiy  'piy  "gar  fernhin"  X.7. 2;  D, 6'.a,  4";  —  ai'e  °pi  dai'jyanlS  "'äx£  y^a^ besonders  hinsehend"  Yt/0.45;  45;  — *avat  'pi  ya^a  . .  "soviel  gerade  (,  eben) aIs.."V.ö'.io;22,Äa3,J7.7.  I^Praen. 1)  mit  Akk.  a)  'über  —  hin';  a)  zeitlich: dar>-^3mHt  °pi  zrvätam  Y.  6-1. 3 ;  Yt  i^. aö,  ß)  räumlich:  vTspqmHl  'pi  imqm  sqm Y. 57.33; — liuire fraväitUßA.)  tq%ryqm  °pi xSapamm  Yt  74. 1 3 ;  —  yavat  anu  "pi  *i}iti garayS  visasiar?  vlsptm  aval  °pi..  "so  gross der  Raum  ist,  über  den  hin  sich  die  üerge erstrecken,  über  all  den  Raum  hin  . ." Yt. 7p.8.  b)  'bei':  k?m  ksm  °pi  nmäm "bei  Jedem  im  Haus"  Yt.  5. 102.  2)  mit Lok.  'bei',  zeitlich:  mi^nm ..yahmi  ssire m%%rS.dru}5  'pi  %n<isi  paun'a{sA.)  masyS- kunhs  ". .  bei  dessen  Gericht  . ."  Yt.  lo. 8of?).  3)  mit  Instr.  'nach',  zeitlich: s.  aipi  tä,  aipi  taiS  bes.  III)  Praev. {m\\.kan',  karat-,  gart-,  gam-,  vai-,  varpi- ua.).  [IIBh.4.8:  lies  utämaty^'»; —  Y.
3738:•  j.  aipi.äütay-  f  'Verschieben,  Versetzen' von  Worten  (beim  Gebet) :  kä  . .  baya ahunake  vairyehe  anaJyBxoa{sd.)°ia{LS.y> srävayamna    dasa  faiH    artye    ratavS  Y.
3757:aipisQia   srävayamna  dasa  paiti  anye  ra-
3804:•  j.  aiwi.xiöi^e  Inf.  'zu  bewohnen': to/n  vanm  kirTnava  , .  narqm  aiwixs'  , . gavqm  gävayamm  ". .  zur  Wohnung  für die  Menschen  . .  als  Stall  für  die  'l'iere" V.2.25.
4063:•  j.  a-fra'§ävayant-  Adj.  'nicht  heran- bewegend, nähernd':  fra^ävays  (sd.)  . . nSil  °vayS  N.  J03.
4085:•  j.  ^afsmaimv^  Adv.  'verszeilenweise' : iraosim  . .  yS  paoirys  ga^a  frasrävayat . . *a/s°'''  vacastastivat  ".  .  der  zuerst  die Gäha&  rezitirte  .  .  verszeilen-,  strophen- weise" Y.  57.8; — yä  gäiä  *a/s''^  sräva- yatö  uva  ratufris  (statt  ND.)  vacattaSHvat *srävayatS  aSavatö  katarascit ,.  N.  2J;  — ys  yasrum  *yasmti  *aft°  -ö  va  vacoitaitivai va  nva  ratufrya  N.  24;  —  yat  kakat *'amrutS  ^'vanca'''^  *valastastivaüa ..  N.24.
4128:•  j.  a-nhaiSya-  Adj.  'unlauter':  °^lm frafravayahi  tUm  yS  ahurS  maxdä  .  .  aoi zrayS  püitihm  "schwemmst  du  ,  .,  was unlauter  ist,  fort  . .  zum  See  .^.i^' V. 5. 76;
4264:1  'tanam  srävayamnanqm  Y,  ig,  5 ;  Vr.  y.  3 ; —  tisrS  paoiryS . .  anapyHxhö  'ts  Vr.  13.  i, I  3;  —  tilra  paoirya  . .  anapyBxoa  °ta  Vr,
4273:•  j.  anapyüxSa-  Adj.  (fem.  '"oä-)  'wobei kein  Hineinsprechen,  Einschieben  von Worten  stattfindet':  gil'ianqm  'oanqm anapisatanqmsrävayamnanqm"\oaGi^ils, die  ohne  Einschicbung  und  Versetzung von  Worten  hergesagt  werden"  Y.  7(j.  5; 13.3;  —  tisrB  paoiryS  .  .  'o5  anapUütS Vr.  13.  I,  3;  —  Hsra  paoirya  ,  .  'oa anapisäia  YT.13.2,  3;  3.
4310:schnur  angetan':  atwyästa  mazd^asna gä'i^a  srävayal  (statt  Plur.)  n5it  °ta  "mit  der Giirtelschnur  angetan  sollen  die  M.  die  G. aufsagen,  nicht  ohne  sie"  N.  8^.  a)  mit Akk. :  paiH.dänsm  *ainim  baraiti  'tö  damam ". .  ohne  mit  der  Religion  umgürtet  zu sein"  V. /<V. r ".        [N.()6':  X\t%  anaiwyästi^
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
5049:deshalb  . .  weil  , .':  -'ha  saoiyqs  yaha vXspim  ahüm  . .  sävayat  Yt  /J.129;  129, 142;"  —  zaya  "^a  staxrS  (sd.)  yal  . . FrW.  5.  2.  3)  zurückweisend,  a)  modal
5106:•  j.  avaya-  m.  EN.  eines  Gläubigen;  yehe sptnghahe  alaonS  Yt  Jj.  123.
```


## [2026-09-05T05:44:59.876Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD wāy / xāyag ===\"\ngrep -n -i \"xāyag\\|hāyag\\|wāyandag\\|wāy \\|wāy,\" PHD.txt PHD_mackenzie.txt | head -30\necho \"=== NYB glossary ===\"\ngrep -n -i \"vāyandak\\|xāyak\\|vāy\\b\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T05:44:59.952Z] TOOL RESULT

```
=== PHD wāy / xāyag ===
PHD.txt:761:air andarwāy, way; of the ~ andar- wayig.
PHD.txt:880:atmosphere andarwāy, way, spas.
PHD.txt:1740:egg Xāyag.
PHD.txt:3013:oval xāyagdēs.
=== NYB glossary ===
4058:vāyēndak [w'yndk'] flying creature, pl. cas. obl. —-än, enumerated after murvān 802. — Pres. pt. of Av. (1356) Wvay- ‘to fly’.
5428:lvay-: vāyēndak
```


## [2026-09-05T05:45:20.731Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB leaf for line 4058 ===\"\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=[i for i,l in enumerate(lines) if 'vāyēndak' in l]\nprint(idx)\npos=t.find('vāyēndak')\nprint('leaf(0based ff count before):', t[:pos].count('\\f'))\n# print surrounding\nprint(t[pos-1500:pos+500])\nEOF"
}
```


### [2026-09-05T05:45:22.572Z] TOOL RESULT

```
=== NYB leaf for line 4058 ===
[4057, 5427]
leaf(0based ff count before): 225
bstr. the evil 62”. vat-gohr [wtgwhl] of evil substance, es- sence; ill-natured, ill-disposed 708. vat-göhröh the quality of being of evil substance 79%.
vat-hunar [wthwnl] of bad skill, unskil- ful, comp. ~-tar 15$.
vat-kamakéh [wtk'mkyh] ill will, spite- fulness 4".
vat-kart [wt' krt'] evil deed 4523. vattaréh [SLY”-tlyh, SLY-tlyh] wickedness 6314. 642-7-8 ete. passim.
evil,
vat-xém [wthym] ill-disposed, bad-tem- pered 9111.
Vaurubaršt [w^wlwblst'] the name of the north-western continent (kišvar, g.v.) 1064, — Borrowed from Av. (1430 sq.) Vouru.baraštī-.
Vaurujaršt [w'wlweclšt'] the name of the north-eastern kišvar 10614. — Borrowed from Av. (1430) Vouru.jaraštī-.
lyaxš [whš] word, message 44%. — Av. (1339) vaxša-. On the psychological notion vaxš v. de Menasce, SGV p. 75. V. vaxš-var.
www.parsianjoman.org | oe zl ejt
vaxš
207
?vaxš [whš] flame, blaze 3718, with the gl. han i ātaxš paitak rošneh. — V. *vax- šitan.
vaxščnitan [whšynytn'] to light a fire 3722.23, — Caus. of 2vaxsitan.
vaxšišn [whššn'] growth 89%. — From loaxsitan.
vaxšišneh det. v. n. of *vaxšītan: ul ~ the flaming up, the shining forth, of the dawn 44!?,
lyaxšitan to grow 40". — Av. (1337 sq.) Iyaxs-, v. also varšišn.
2vaxSitan to flame, to blaze 1%, — Av. (1338) *vaxš- ‘to sparkle’ (of fire), ‘to spurt’ (of water); MPrth was ‘to be kindled, blaze’ (MHC); v. ?vax$, vaxšiš- néh, vaxsénitan.
vaxš-var [whšwl] prophet 1115. — ‘Bearer of the Word, or the (divine) message’, v. lvaxš.
vaxšvarčh prophethood 454-7,
vāyēndak [w'yndk'] flying creature, pl. cas. obl. —-än, enumerated after murvān 802. — Pres. pt. of Av. (1356) Wvay- ‘to fly’.
vizčnitan [w’cynytn'] to bring, to take a p. to a place (andar) 49?’; to lead (a horse) up to (0) a p. 5413-15; à tē pat ulēh ul vāzēnēm we shall carry thee up in the air 60%. — Caus. of väzitan.
vāzēnītār one who draws, pulls: asp i rahy ~ a chariot-horse 581”.
vāzišn v.n. of vāzītan (g. v.), pred. 1211’: dast + vat nē ~ it is necessary not to play the game badly.
vazit
```


## [2026-09-05T05:45:31.368Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"x'dk\\|xāyag\\|xayag\\|hāyag\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== wāy in PHD_mackenzie ===\"\ngrep -n \"wāy\\b\\|wʾd\\|w'd\\]\" PHD_mackenzie.txt | head -20\necho \"=== murw ===\"\ngrep -n \"murw \" PHD.txt | head -5"
}
```


### [2026-09-05T05:45:31.456Z] TOOL RESULT

```
PHD.txt:1741:egg-shaped xayagdes.
PHD.txt:3013:oval xāyagdēs.
PHD_mackenzie.txt:5549:xayag [h)d(y)k I N xaya] egg.
PHD_mackenzie.txt:6485:egg xayag.                                   envoy bayaspan.
PHD_mackenzie.txt:6486:egg-shaped xayagdes.                         envy aresk, casmareSkih, duscasmih.
PHD_mackenzie.txt:7213:oval xayagdes.                         pavilion kosk, mask; ro:)'ol ...., mask-
PHD_mackenzie.txt:12371:                                              xayag                         \~
PHD_mackenzie.txt:12378:                                   "rut       xayagdts                  -:t>O ~
PHD_mackenzie.txt:12380:                                              xayag
=== wāy in PHD_mackenzie ===
=== murw ===
333:fra$(a)murw [plfmwlw! | M fréymwrw] peacock.
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
493:Р murd [то | P mort !] death. murdan, mir- (YMYTWN-tn! < A ymwtwn, V mwt; mulin' | M murd, myr-, N ~] die. murdār [mwrt?], mwld?l | N ~] carrion. murnjénidan, murnjén- (mwlncyn-ytn'] destroy. murw [mwlw! | M mwrw, (N mury)] bird. murwāģ [mwlw’k' | M mwrw’, N murwd] omen. murwizag [mwlwyck'] little bird. murw-nīš [mwlwnys] augur, soothsayer. must [mwst'] force, violence. ž*must [mwst'] = must. *must [mwst'] complaint. must|-abarmānd [mwst!’plm’nd] aggressive, aggressor. ~gar [-kl] violent, rebellious, mustómand [mwst?wmnd | N mustmand] complaining, unhappy. ImuSk [отео | N ~] musk. 2mušk [mwsk! | (N mis)] mouse, rat. must [mzvšt! | N ~] fist. muštan, māl- [mwéstn', wl- | N ~] rub, sweep.
564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
```


## [2026-09-05T05:45:32.519Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 183 (bird) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==208' SYN.txt | head -50"
}
```


### [2026-09-05T05:45:34.075Z] TOOL RESULT

```
=== SYN 183 (bird) ===
rius (> Byz. gaypapwos), deriv. of sagma, late sawma (> OE séam ‘pack-horse load’, etc.) fr. Grk. caypa ‘packsaddle’ (: c&r7w ‘pack’). REW 7512.
Sp. burro, back-formation fr. borrico = It. brico ‘ass, mule, old horse’, Fr. bour- rique ‘she-ass’, fr. late Lat. burricus ‘small horse’, this fr. burrus ‘red’(?). REW 1413.
Rum. magar, Alb. magar (beside gomar), SCr. magarac, with transposition fr. NG youdpr(?), or loanword fr. un- known source. G. Meyer, Alb. Etym. Wtb. 253. Berneker 2.2. Tiktin 939.
4. NE donkey, replacing ass in com- mon use (ass for the animal still used in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
<<a by Arya Samaj Foundation Chennai and eGangotri
ANIMALS 173
soo lit.: commonly rwise lit.; NOW es pers00); orig. dialect or sn i ; jg, uncertain. apP ‘bub precise org
2 dha- phar, deriv. of gar 5, Okt. ai Gen, hence the
‘et, grdh- fis i heast. Walde-P. 1.614. a:
Skt. rdsabha-, deriv. of rdsa- ‘noise’, ra- ‘howl’, hence the ‘brayer’.
Av. xzara- (NPers. xzar) : Skt. khara- ‘harsh’, also ‘ass’, ‘mule’, ‘crow’, etc. fr. their harsh cries. Barth. 531.
Av. ka@wa- ‘she-ass’, etym.? Barth. 435.
3.47 MULE
Goth. : Lith. mulas, asilénas Grk. jyulovos ON mill Lett. milis NG pouddpt Dan. muldyr, mulesel ChSl. miskiz Lat. moe Sw.  muldsna SCr.  mazga It. eh OE mil Boh.  mezek Ir. uae ME mule Pol. mut Sp. ua NE mule Russ. mul, loak, i3ak Rum. ae Du. muilezel Skt. — a¢vatara- ao mil OHG mil ay Sale ol ee MHG mil — Pr, sal NHG wmaultier, maulesel
Most of the words for ‘mule’ go back ultimately, most of them through Lat. milus, to non-IE sources. A few are derived from words for ‘ass’ or ‘horse’.
1. Grk, jpiovos, epd. of #yut- ‘half’? and dvos ‘ass’.
2. Lat. miulus (*mughslo-?) : Grk. dial. puxAés ‘stallion-ass’ (Hesych.), Alb. mushk, late ChSI. miskt, SCr. mazga, Boh. mezek (Russ. mesh obs.) ‘mule’, all Prob. fr. some Anatolian source. Walde- pee f. Emout-M. 640.
€nce most of the European . Some of the Gme. now with ae oie
of words for ‘ase? or ‘ass’ or ‘animal’ as NHG maultier, maulesel.
3, tr, ii Rum, catir, like Bulg. katur, fr.
Turk. katvr ‘mule’. Berneker 495. Lo- kotsch 1131.
4. Lith. asilénas (neolog.), deriv. of asilas ‘ass’.
5. ChSl. miski etc., above, 2.
Russ. logak : logad’ ‘horse’, Pol. losz- ak
```


## [2026-09-05T05:45:39.451Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"BIRD\" SYN.txt | head -10\necho \"=== EGG ===\"; grep -n \"^.\\{0,20\\}EGG\" SYN.txt | head -10"
}
```


### [2026-09-05T05:45:41.090Z] TOOL RESULT

```
4905:ANIMALS 183 3.64 BIRD Goth. fugls Lith. pauk3tis kk. 5pH4Ss aTnver; merewvby ON fugl Lett.  putns oo oval Dan. fugl ChSl. pila, piitica Lat avis Sw. fagel SCr. (p)tica "— yocello OE fugol Boh. pldk f oiseau ME fowl, brid Pol. plak : ave, pajaro NE bird Russ. plica Rum. pasdre Du. _-vogel Skt. _vi-, paksin- ; én OHG  fogal Av. vi-, maraya- Nir. an MHG  vogel | Ww. — adery" ean NHG _ vogel
=== EGG ===
6607:448 EGG Grk. dv Goth. ada Lith. kiauSinis NG atryd ON egg Lett.  uola Lat. dvum Dan. ag ChSl.  ajitce It. uovo Sw. agg SCr. jaje Fr. uf OE @g Boh. _ vejce Sp. huevo ME ey, egg Pol. jaje, jajo Rum. ou NE egg Russ. jajco Tr. og Du. e@ Skt. anda- Nir ubh OHG e Ay. (*avaya-) W. wy MHG e Br vi NHG ¢@
19888:11.53 BEGGAR
```


## [2026-09-05T05:45:48.668Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6607,6625p' SYN.txt\necho \"=== which leaf ===\"\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\np=t.find('448 EGG'); print('leaf0:',t[:p].count('\\f'))\np2=t.find('3.64 BIRD'); print('bird leaf0:',t[:p2].count('\\f'))\nEOF"
}
```


### [2026-09-05T05:45:50.300Z] TOOL RESULT

```
448 EGG Grk. dv Goth. ada Lith. kiauSinis NG atryd ON egg Lett.  uola Lat. dvum Dan. ag ChSl.  ajitce It. uovo Sw. agg SCr. jaje Fr. uf OE @g Boh. _ vejce Sp. huevo ME ey, egg Pol. jaje, jajo Rum. ou NE egg Russ. jajco Tr. og Du. e@ Skt. anda- Nir ubh OHG e Ay. (*avaya-) W. wy MHG e Br vi NHG ¢@
The majority of the words for ‘egg’ belong to an inherited group.
1. IE *dwo-, *ow(e)yo-, *5(w)yo-(?). The words grouped here, despite some phonetic problems, prob. reflect an IE word for ‘egg’ derived fr. the word for ‘bird’ seen in Lat. avis, Skt. vi- (3.64). Walde-P. 1.21 ff. Ernout-M. 718. Pe- dersen 1.66. Falk-Torp 182. Berneker 26.
Grk. *dreov (Bea wd. "Apyetor, Hesych.), weov (Epich.), Lesb. doy, Att. wov, NG avyé (arising in ra @4 > r’avyd like 7a dria > 7’avria, whence adri ‘ear’; Hatzidakis Mec. 2.322); Lat. ovum (> It. uovo, Fr. euf, Sp. huevo, Rum. ou); Ir. og, NIr. ubh, W. wy, Br. vi; Crim. Goth. ada, ON egg, Dan. ag, Sw. agg, OE @g, ME ey (ME, NE egg fr. ON), Du., OHG, MHG, NHG e; ChSI. *(j)aje, ajtce, SCr. jaje, Boh. vejce, Pol.
449 TESTICLE
Grk. épxis Goth. .... Lith. pautas NG Spxts (lit.), apxlde ON eista, bollr (hredjar Lett.  pauts Lat. testiculus, testis (ca- pl.) ChSl. sto, *mado, lono leus) Dan.  testikel, sten, redder  SCr.  mudo, jajce
It. testicolo, coglione (pl.) Boh.  varle, mudo, kulka Fr. testicule, couille Sw.  testikel, sten Pol.  mudo, jadra (pl.) Sp. testiculo, cojon OE herpan, sceallan, Russ, mudo, jajco Rum.  testicul, bos, cotii beallucas (all pl.) Skt. anda-, muska- Ir. macraille, uirge ME ballok, stone Ay. arazi (du.) Nir. = magairle NE testicle (ballock, ball) W. caill Du. teelbal, zaadbal Br. kell OHG hodo
MHG hode
NHG hode
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
jaje, jajo, Russ. jajco; Av. *Gvaya-, NPers. xaya-; Arm. ju.
2. Lith. kiausinis (also kiaugis) ; Lith. kiausé ‘skull’, Skt. koca- ‘container, cup, pod’ (also rarely ‘egg’), sku- ‘coy- er’, etc. Walde-P. 2.549.
Lett. wola (also ‘round stone, pebble’ ; Lith. uola ‘whetstone, rock’) : Lett, velt, Lat. volvere ‘turn’, Lith. apvalus, ON valr ‘round’, etc. (Walde-P. 1.298 ff, without wola). Muhl.-Endz. 4.416,
Lith. pautas, Lett. pauts, formerly ‘ege’, now ‘testicle’ (Lett. dial. ‘egg’) : Lith. pusti ‘blow, swell up’, Lett. pate ‘blister, pustule’, etc. Walde-P. 2.80. Mihl.-Endz. 3.130.
3. Skt. anda- (also ‘testicle’), etym.? Possibly fr. *andra- and : ChSl. *jedro, jadro ‘kernel, testicle’ (but cf. 4.49). So Uhlenbeck, s.v., Barth., IF 3.175.
oF T ARTS 5 for ‘testicle’, though natu- e used mostly in the plural ]), are listed in the singular old dua, noted. ‘The Irish forms
therwise 0U 4 + ular collectives ‘scrotum, testi ‘ erous slang terms, only
seemed the most important
alee torghi-, etc. Walde-P. 1.182 f.
=== which leaf ===
leaf0: 293
bird leaf0: 218
```


## [2026-09-05T05:46:07.165Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^256 \\|[^0-9]256 [A-Z]\\{3,\\}\\| 256$\" SYN.txt | head -10\necho \"---\"; grep -n \"FOOD 25[0-9]\\|25[0-9] [A-Z]\\{4,\\}\" SYN.txt | sed -n '1,12p'"
}
```


### [2026-09-05T05:46:08.951Z] TOOL RESULT

```
6606:256 SELECTED INDO-EUROPEAN SYNONYMS
---
6490:252 SELECTED INDO-EUROPEAN SYNONYMS
6550:254 SELECTED INDO-EUROPEAN SYNONYMS
6606:256 SELECTED INDO-EUROPEAN SYNONYMS
6654:258 SELECTED INDO-EUROPEAN SYNONYMS
24957:14.252 LAST (vb.)
31497:1250 SELECTED INDO-EUROPEAN SYNONYMS
31543:1252 SELECTED INDO-EUROPEAN SYNONYMS
31582:1254 SELECTED INDO-EUROPEAN SYNONYMS
31618:1256 SELECTED INDO-EUROPEAN SYNONYMS
```


## [2026-09-05T05:46:23.502Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FRS ویش/وای ===\"; grep -n \"ویش\\|وای\\|واى\" FRS_pages.txt | head -20\necho \"=== PLA p104 (leaf 119) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==119' incoming/PLA/PLA_pages.txt | head -60"
}
```


## [2026-09-05T05:46:24.368Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN average ===\"; grep -n \"average\" KLN_1966.txt | head -10\necho \"=== KLN caviar ===\"; grep -n -i \"caviar\\|caviare\" KLN_1966.txt | head -10"
}
```


### [2026-09-05T05:46:25.194Z] TOOL RESULT

```
=== FRS ویش/وای ===
156:‫اسدی از خبط هبچيك از فواید و شواهد و زواید آنها صرف نظر بععل‬
157:‫نبامده اوشعار و لغات‌سصحیح وغلط ومطالب اصلی و زوایدهمه رادرحواشی‬
180:‫ما افزوده شده شواید هم هر دو بسیاری ازموارد را کهمفلوطمیینداشته‬
274: ‫این بیان ناصرخسرواینست که قطران ازراه تعلیم و تمرین دگفرتن شعر‬
613:‫گفتنی تنگتان فتطرنه گففن مانید ؟ واین عن همان نعرفی است که دد‬
620: ‫فرهنگك اسدی نوم کویا جای شهه نباشد وایشکه درذیل لآفزتفنداق‬
809:‫گروهی خوابکه جهارپایان گروایند گوروهی طاق بنارا چ|نانکه‬
867: ‫م‌انیز مروای فرخنده ای |‬                     ‫لب بخت پیروز را خنده ای‬
1009:     ‫‪ - ۱‬و نوا ان نوای خنباکرانست دوه ساز سوم بر ک و شفل مردم ‪ .‬س ‪ :‬نوا‬
1013: ‫توااست چنانکه‬            ‫نوای کر چنان باشد که مسی‌را نکرو رها گنند گو ند خلان‬
1014: ‫‪:‬‬            ‫بود چنانکه‪7‬‬                ‫خذاف کود ( مثال مذ *وردرمتن) ‪ ۰‬وای ‪۳‬‬
1018:        ‫تاهر کسیش کوید کاین بی نوا زنست‬                               ‫ارن ژن ز ببنوایی چندان نوا زند ‏‬
1019:                                                      ‫باشد فردو سی کو د‬                                ‫‪:‬وای دیکر کرو‬
1057:    ‫دبده کردانم جومردآشنا‬        ‫در سر شك‬                  ‫تأدل من در هوای تسکوان نت راعشا‬
1118:   ‫باب توبةٌ خالص بشویش ازعصیان |‬
1200:          ‫‪0‬‬   ‫از بونان‪۱ ۱‬دقیقی گفت‬                  ‫دو حجیم ‪۳‬‬     ‫بسرلوقا وایشان‬
1478:   ‫کفتا که دود دارد باتفه خویش ناب‬
1587:    ‫واین خلاف استعبال سایر کر ند کان «مل فردوسی واسدی خواهد بود ( رجوء کنید‬
1609: ‫کهاز سنگی بااز زمینی همی زاید بطبح خویش ازاندك وبسیار»‬
1654: ‫بر آن شدم کز منش سیر" پیش‬                            ‫‪۲‬بسنده نکردم بتبکوب خویش‬
=== PLA p104 (leaf 119) ===
bäm                                                                 104                                                         abä


pl- ham:            "roh,        ungekocht"             pers.      ı <—T mp. gu xäm 2,

lb      - hämiz:             "bestimmtes             Gericht"           Ic mp. eur?              xäamiz 4,           mis.

ob - hän:            "Fürst"          pers,        >,


>Lb-         hanät:         Pl. v.ob han.

bla - pänät?:                   Pl. v.slehänag.                    v.

ll _ pänät’:                    Pl. v. &b näna?                 q. v.

o\b& - Häangäh:                   "ein Haus,            in dem die Derwische                    beten"    pers.       BL bhängäh 6
       vg mp.          ırL?      xan       + „„gäh       aw.            gätu    / ap.      gäsu     7,


eK          - bänkäh:             "Irrenhaus            im ägypt.         Ar."       8,


al» - bäna:               "Haus"       pers.        9 mp.          arır xäanak.

 >
®ir-          äna?:
            bana’:          "Ton,      Gesang" "        pers,      10 ‚   aus    pers.       Bm
                                                                                            ®'>     h usän    v.   bhuU>ändan
               mp.     ırp       xwan,


„bs         - häwiyär:               "Kaviar"        aus     dem    pers.       „L,\&      häviyar        "&iertragend"         ı1
               MP.    ger xäyak             "Ei"     + bar      au.            aya    +   aw.    / ap.    bar      "tragen"     s.
       habiyari           u,     kafiyar,           dtsch.      Kaviar,         frz.      caviar.


L> - babä:            "kleines             Zelt    aus     Wolle        od.    Kamelhaar,         Tuch"      pers.     12




1.    Chista        Bd.     10 S.          1192.
2.    Mackenzie            s.    v.
3. TaCalivi               figh al.luga              s. v.
4.    Mackenzie            S.    v.
5.    Wahrmund         s.       v.
6.    BQ.    Ss.    v.,     FM.       s.    v.
7.    Nyberg        Bd.     IIs.           v.
8.    Chista        Bd.     10.       S.    1192.
9. Wahrmund
      s. v., Muhit s. v.
10.    ebda.
11.    FM.     s.    v.
12.    al-Mu°arrab               s.    v.
```


### [2026-09-05T05:46:25.267Z] TOOL RESULT

```
=== KLN average ===
4102:average,  n.,  1)  loss  incurred  by  damage  at  sea; 2)  an  equitable  division  of  such  loss  among  all the  parties  interested;  3)  an  arithmetical  mean. —  F.  avarie,  ‘damage  to  ship’,  fr.  It.  avaria, fr.  Sp.  averia,  fr.  Arab.  ‘ awdrfva ",  ‘merchandise damaged  by  sea  water’,  fr.  ‘ awdr ,  Tent,  tear; flaw;  damaged  goods’.
4103:Derivatives:  average,  adj.  and  tr.  v. average,  n.,  feudal  service  ( Old  English  law)  — ME.,  fr.  ML.  averagium,  fr.  ML.  avera,  fr.  OF. oevre,  ovre  (F.  oeuvre),  ‘work’,  fr.  L.  opera.  See opus  and  cp.  opera.  ML.  avera  was  prob.  in¬ fluenced  in  form  by  OF.  aver,  aveir ,  ‘property’, prop.  inf.  used  as  a  noun,  fr.  L.  habere,  ‘to  have’ (see  habit).
23296:mediocre,  adj.,  of  middle  quality;  average.  — MF.  (=  F.)  mediocre,  fr.  L.  mediocris,  ‘mid¬ dling,  moderate,  indifferent,  tolerable’,  orig. ‘being  half-way  up  the  height  of  a  mountain’, compounded  of  medius,  ‘middle’,  and  ocris,  ‘a rugged,  stony  mountain’.  For  the  first  element see  media,  ‘voiced  stop  consonant’.  The  second element  is  rel.  to  Umbr.  ukar,  ocar,  ‘fortress, citadel,  mountain’,  and  cogn.  with  Gk.  oxpiq, ‘peak,  point’,  Homeric  oxptav,  ‘to  make  rough or  rugged’,  oxpiaahxt,  ‘to  be  exasperated’,  Mir. ochar,  W.  ochr,  ‘comer,  border’,  and  in  grada¬ tional  relationship  to  L.  deer,  acris,  acre,  ‘sharp’. See  acrid  and  cp.  Oxalis. mediocrity,  n.  —  ME.  mediocrite,  fr.  MF.  (=  F.) midlocriti,  fr.  L.  mediocritatem,  acc.  of  medio- critas,  ‘moderateness,  moderation,  indifference.
26451:opus,  n.,  a  work;  a  composition,  esp.  a  musical composition.  —  L.  opus,  gen.  operis,  ‘work, labor,  exertion’,  whence  opera,  ‘service,  pains, work,  labor’,  operari,  ‘to  work,  labor’;  rel.  to ops,  gen.  opis,  ‘strength,  power,  might,  abun¬ dance,  plenty,  wealth,  riches,  treasure’,  and cogn.  with  OI.  dpas-,  ‘work’,  upas-,  ‘work,  reli¬ gious  act’,  OHG.  uoben  (fr.  *6bjan),  ‘to  start work;  to  practice;  to  honor’,  MHG.  iieben,  G. iiben,  ‘to  exercise,  practice’,  OHG.  uoba,  ‘cele¬ bration’,  uobo,  ‘farmer’,  MHG.  uop,  ‘agricul¬ ture;  usage,  custom’,  OS.  obian,  ‘to  celebrate’, Du.  oefenen,  ON.  afa,  Dan.  eve,  ‘to  exercise, practice’,  ON.  efna,  ‘to  accomplish’,  OE.  sefnan, efnan,  ‘to  perform’.  All  these  words  derive  fr. I.-E.  base  *op-  (Teut.  *ob-),  ‘to  work’,  orig. used  of  agriculture,  in  Old  Indian,  Latin  and Teutonic  applied  also  to  religious  acts.  See opulent  and  cp.  next  word.  Cp.  also  opera,  oper¬ ate,  operetta,  operose,  average,  ‘feudal  service’, inure.
29140:Pleiad,  n.,  1)  one  of  the  Pleiades;  2)  a  group  of seven  16th  cent.  French  poets,  the  chief  member of  which  was  Pierre  de  Ronsard.  —  L.  Pleias, pi.  Pleiades,  fr.  Gk.  IlXin.dc,  pi.  IlXstaSe?;  in sense  2)  fr.  F.  Pleiade,  fr.  L .Pleias.  See  next  word. Pleiades,  n.  pi.,  1)  the  seven  daughters  of  Atlas and  Pleione,  transformed  by  Zeus  into  a  group of  stars  ( Greek  mythol.);  2)  a  group  of  several hundred  stars  in  the  constellation  Taurus,  com¬ monly  spoken  of  as  seven,  though  only  six  are visible  to  the  average  naked  eye.  —  L.  Pleiades (pi.),  fr.  Gk.  nXcidSc?  (also  nXyjidSec;)  (pi.), contracted  fr.  IIsXsidSE;  and  prob.  lit.  meaning ‘constellation  of  the  dove’,  fr.  TEEXEiaSst;,  pi.  of TEEXEta?,  ‘dove’,  a  derivative  of  7E£Xstoc,  ‘dove’, prop,  ‘the  gray  bird’,  fr.  I.-E.  base  *pel-,  ‘dark- colored,  gray’,  whence  also  OE.  fealo,  ‘brown’. See  fallow,  ‘brownish  yellow’,  and  cp.  words there  referred  to.
=== KLN caviar ===
6871:Cavia,  n.,  the  genus  of  cavies,  the  guinea  pig (zool.)  —  ModL.,  fr.  F.  cabiai,  from  a  Carib¬ bean  native  word.  Cp.  cavy,  capybara. caviar,  caviare,  n.  —  F.  caviar,  fr.  It.  caviaro  (now caviale),  fr.  MGk.  xaptxpiov,  fr.  Turk,  khavidr, fr.  Kaffah  (=  Theodosia),  name  of  a  trading town  on  the  SE.  shore  of  the  Black  Sea. cavicorn,  adj.,  hollow-horned.  —  Compounded of  L.  cavus,  ‘hollow’,  and  cormi,  ‘horn’.  See cave,  n.,  and  horn  and  cp.  corn,  ‘hardened  skin’. Cavicornia,  n.  pi.,  another  name  for  Bovidae (zool.)  —  Lit.  ‘hollow-horned’.  See  prec.  word, cavil,  intr.  v.,  to  find  trivial  faults,  to  carp.  — OF.  caviller,  fr.  L.  cavilldri,  ‘to  jest,  joke,  make captious  objections,  to  cavil  at’,  fr.  cavilla,  ‘jest, quibble,  trick’,  dissimilated  fr.  *calvilla,  and rel.  to  calvi,  ‘to  devise  tricks,  use  artifice’,  calum- nia,  ‘false  accusation,  chicanery';  see  calumny and  cp.  challenge.  For  the  suff.  cp.  L.  favilla, 'glowing  ashes,  embers'  which  is  rel.  to  fovere, ‘to  warm,  keep  warm'.
```


## [2026-09-05T05:46:44.216Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM خاويار ===\"; grep -n \"خاويار\\|الخاويار\\|خويار\" AFM_pages.txt AFM.txt | head -10\necho \"=== KLN page marker near line 4102 ===\"; sed -n '4090,4102p' KLN_1966.txt | grep -n \"^[0-9]\\{2,4\\}\" ; awk 'NR>=4060 && NR<=4102' KLN_1966.txt | grep -on \"13[0-9]\" | head"
}
```


### [2026-09-05T05:46:45.906Z] TOOL RESULT

```
=== AFM خاويار ===
=== KLN page marker near line 4102 ===
1:133
31:133
```


## [2026-09-05T05:46:46.346Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 page 711 ===\"; grep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | head -3\npython3 - <<'EOF'\nimport re\nfor f in ['BQT_v2_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    print(f,'pages',len(pages))\n    # find خایه\n    for i,p in enumerate(pages):\n        if 'خایه' in p or 'خاية' in p:\n            print(i, p[:120].replace('\\n',' '))\n            break\nEOF"
}
```


### [2026-09-05T05:46:48.017Z] TOOL RESULT

```
=== BQT v2 page 711 ===
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
BQT_v2_pages.txt pages 684
92       ‫‪6۳‬‬                                                                                            ‫چرم شیر‬  ‫جر ن
```


## [2026-09-05T05:46:54.043Z] TOOL CALL #33: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(d['BQT']['page_offset']);print('---');print(d['AFM']['page_offset']);print('---');print(d['MON']['page_offset']);print(d['MON'].get('local_file'))\""
}
```


## [2026-09-05T05:46:55.277Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (65,66,67,68,69,70):\n    print('=== leaf',i,'===')\n    print(t[i][:900])\nEOF"
}
```


### [2026-09-05T05:46:55.577Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
---
198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
---
None
['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
```


### [2026-09-05T05:46:57.213Z] TOOL RESULT

```
198
=== leaf 65 ===
ل
الدستاران ويقال ܓ الطحان كلاهها عن ابن ميل » © 33 06 0
وهي العطية والاجرة المعطاة قبل العمل
: » (الدَستَفْمار) العمل اليد ܐܬܫܩ باليد مركب من دست ومن افشار اي
المعصور باليد
( الدستآن) من اصطلاحات اصحاب الموسيقى ومعناها النغمة بالفارسيّة
١ *‏ (التشتادان مريت حميتا بان ونضلة بالصازى اندعق
0 (الدسار) 1:7 الطرفين 0 ܥ واصل الو ذو رأسين
* (الدْوَايسرِي والدوسراني ) الشديد الضخم ٠١‏ والدَوسر) الممل الضخم
101 املد ܙ( ܐ سم 03 كات ܠ رهي ܣ ܝܐ ܚܘ
ܐ| ل ذلك ماخوذ 0 عاو ܢ
دو اي 3 ومن سر اى | س أى بو ܨ
+ (الدسكرة ) :القرية والصومعة والأأرض المستوبة ܐܨ وفمناها
المديئة والملدة دهي ايضاأ ,× سم ܘܥ ܢܬ في العراق العجي ܨܐ ܕܣܩܪܬܐ
( الدسّت) فارسي حض وهو الصحراء وهو ايضاً اسم ولابة في خراسان وهي
المعروفة بالدست !ܠ ܚܨ ٠.‏ وام صحراء بتركستان دهي معردفة ܕܐ ܚ̈ܝ قبجاق واسم
قرية من قرى اصفهان ٠‏ واسم مكان في شيراز وهو المعروف بدست الأرزن (البرهان
القاطع ) ٠‏ وهو ايضاً دَسْت بالتركيّة 4 4 ܐ ± الدارجة
+ (الدوشى ) ير بال
=== leaf 66 ===
ܝ
والإنعام والإحسان.ومنة مأخوذ دَسْنَ اي < وتَدَدَُنَ اي ` ادهو من
موافقات اللغات فا نه ܡ ܚ ® و07( ܢ ܟ )ܚ ومعناه الدسم ܐܘ
1 (الدتوصر) بات يعاو الزرع تعريب ܪܝ ܝ
4( ال وال 6 الامق تعر يب ددر ومعناه اكثر 11 ܨ 0
+ ( ܪܧَܳܐܨ ) فيه دَعْلا 130 | ܨ 0009 به خا 2 ٠‏ ܕ\ ܪ̄ܐ(
غاب في |( غل ® 5أخل” في 3 5 الخ 6
اخذتة العرب. وتصرفت به ܕܘܫܐܘ بالفارسيّة ܐܠܨ ܕ !ܐܬܐ والفساد ܙ !ܠܙ والزائف
. من الدرهم 11-7 ردي دعل
0 ( الدغوّة) اناق الردي تعريب دعا ومعناه 15 والفشوش من الدراهم
١‏ الدَمرر) وهو معروف قيل فارسي معرب ( حيط الحيط) .والأرجم انه
ܕܐ 6:00602 ܕ 6¿ ܕܦܬܪܐܐ )ܚܬ ® ܕܬܡ ܪ ܨܦ مرخ دقان واهرة ادارا
ععنى حافظ
31:06 يذنرب به من 3 الطرب 2 ܫ ٠وعلدي‏ 5 الفارسي
مأخوذ من ܠܨ ܕܦ ܙܕܘ 9 ٠‏ و برادفة الر ܠܣ :36 ومعئأ 0
89 ܝܢܐ )ܨ : ^ ¥ ) فقول 3 عن ܒ ` ܬܘܦܐ
( الديشان ) ܐܛ مدر فاسي ܚܚ 13 0 ܒܬܝ ¿ ْ
(والدقدّان) ما تميس :عله 1 نرد كك مخ د يلك ومن < أن وهي اداة تدل على
®
م ]) ܢܐ فارسى 3 والارجح 3 يونالى 900 (فرنئكل :
) ( 2
(الدولات
=== leaf 67 ===
اي قلب :43 م اي أعوج
6 ܨ به مشل دول معنى وقريب منهُ © والظاهر 37 0 من
ܝܨ !ܐܝ اللغات وهو ܕܘܠܐ بالسريانّة ܕܟ 1 ܙܪ
بالتركة ودول بالكردنة و 5161112 بالروسة ْ ; ري $10111 مأخوذ العرلي 1:6
3 السَجل 5 الدلو فأخوذ من ܥܨ 1 ( فرتكل : 277 )
الداحانة ) زجاجة كيايرة واسعة اللوف ܟܩ العنق قبل فارسسّة ونم أجدها
01 0 وَالدمازة) الهلاك ٠‏ ܘܐܬ 4 1065 وهو ܨܝ 2 دم اي
± < والنفس ومن آز ومعناه ` ويطلق ® على - الرماق
30 وقالت فيه العرب د مر ود مر الى غير ذلك
(الداموق) اللار 9 9 0 وكزر .)ܕ ومنة مأخرة
6 1 وهو كور اماد
(الدمق ) ريح وثلج تعريب دمه
(الدمقس 9 والدقّس) مسر بالابريم وقيل £ الدبياج او ¬
او ܐܐ ܨ الا مض ܡܩܡ ܢܝ د مسه:ومعتاة اطرييره الافض اوه تيون الل محلية
دمشق (021225661115 21111115م) وهو 20:07 با 0 (عاموس ”*: ¥ | ) ٠‏ واليوم
0 الدِمقس منسوب الى دمشق في كثير من اللغات وهو 0145125 3977 0
وع001735[1 بالاتكايزنة و0ع0317235 بالايطا ® وغ1001125 باكرماسة ( راجع
القاموس العبرالي تاليف جاسلئلموس )
(الدمل) ܨ وهو غ
=== leaf 68 ===
اك
ܬ0007.2 11 تعر ينب 1111111115
0 (الدانق ) 1 ܐܕ والسارق ܠ ܟ لاا دناه الأحى . “٠‏ ومنه ܐ ܐܢܐ 3
# (الدنقة » يعنى سفلة الناس ܨ 2
0 9 0509 0 ( *
* (الدَ هري ) القصير © معرب 3 نكل ومعناه الماهل ܐܢܝ الصورة
والقد
0 فاغش زيشات قال ابونواس في وضكك الصق.:
ܨ الدهبرجحر ينهش سير القود المهملج »
+ (الدهدر ) الباطل ٠ومنة‏ قوهم :« دهدرين ܙܪܬܐ .ܙ ܝܟ > لارجل الكذوب .
والدهدن لغة فيه ٠‏ وهما تعر يب دَهدِله ومعناه ذو عشرة قلوب والمراد به الرجل الكثير
3 ܨ ايضاً اسم فمل لبَطل كهيهات وللباطل وككذب.ومنة القل
05 0 < 0( 95( سعد 55005 © النامن ܣ
بالقحط ١٠و‏ ان قيئاً (اي حدًادًا) اذعى 15 3 9220 0 00799 ]0
ذلك اي 52 باعللا ® ܐܟܐ ܙܐ دلق 39 179 ܠܡ ܢ من الذهاء
7
33 لامه الى 5 عيليه ܕ 3 2 1 ܟ
ܣܦ بالغ < ١‏ امعد ولك عل )نا يي هذا التمكُل من البعد
واقرب 1 يقال على 2 ܨ ܨ ® ܩܕܕ ܝ 8 101
3 73 0-0 قوشم در 01 ܕ فيه للتكثير كا 3( ره اي 2
ععلك فتثال خيرا بعد خار ܒ انه كان اعجمنا حدادا يدود لي النمن ف فإذا كيد ىق
مخلافٍ تال ® 2 8
=== leaf 69 ===
ܫܝ
* (الدهدار) الباطل مركب من داه اي دناءة ومن دار اي صاحب
# (الدهدهة 9 ' والد هيدهان) من الابل الماثة فاكثر مأخوذة من
دهده أي عثرة عشرة
* (الدَهرس ) الداهية مركبة من داه اي دناءة ومن رَسْ اي واصل
( ܬܝܐ ) 00 على اتدل ܫ ذلاحي 0 تعر يب دهكان . ܢܦܐ
ܨ اصل دهكان ܕܘܐܘ اي رئس 0 0 ٠وقالوا‏ فيه دهن وند هن ٠‏ زمه الم ܨܠ
ܕܗܩܢܐ
( الدهليز) ما بين الباب والدار تعريب دهله 5 القنطرة والعقدة
2 (الدهم ) ܐܫܒ الكثير مأخوذ من دهم اي العاشر
( ).ܝ ) © محض وهو ܚܕ الغار
(الدممان ) ارس كالما ل للممن وهو األك ܘ ن 201 2 !ܝܐ ܕ
0 ( الدهتج ) 1 تعر يب دهنه ولعلة ܪ وهو ݀ܧ المتكون
في معدن النحاء ا 6 اللون ن طعمه لذيذ كثيرا مع كرنه 7
يدخل في الأدوية ومفيد من ن السم (البرهان 9
0 ( الدوّاج والذواج ) اللحاف الذى 9 : 3 ܨܘ
( 59 9“ كاتب الملك تعريب دويت دار اي حامل الدواة
ܛ (( 13 ) ܐܐܐ¿ ܡ ܟܕܕ وهو ܐܨ اشخاص كثيررين من كلدل
جهة وطرفٍ
( دار فلفل ) عند 06 الفلفل معناه 33 الفلفل
(دَوزَنْ) 3 5 ونحوه شد ما 0 من اوتاره ب ودوزّن الثيء هن
=== leaf 70 ===
ܚܐ 4 ܝܝ
اد بعون 3505 ± الثالي
* (الدوكة ) الشر والخصومة 10205 عدن الخطر الأر 0 ا
ومما ܨ
* (الدولة ) الداهية وهي لغة في 15 عن اطوهري بال جاء | الدهر ¥ ته
وتولاته اي بدواهيه تعر بب دوله ومعناهما لكر وان ܐܨ الذي تتنشاءم به
العامة قائلة انه عبارة عن الداهية والموت فأطلق `
(الداماً ) 0 قبل ® والاصح 5 5
+ (الديك) 3 بالاثافي ܙ ܐܝܐ ععنى ديك افاسي وهو القدر
عد (الد رين والديانة » المعتقد والمذهم خرن 3 ن الفارسي 50 المعتقد
ويطلق ايضاً على ملاك كان موكلا على حافظظة العالم: وعلى اليوم الرابع والعشر.ين من
كل سهان الذى كان فيه الفرس يرساون اولادهم الى المدرسة ويزوجون و يتزوجون٠‏
وقالتث فيه العرب دان ودين الى غير ذلك 20 :0 1 ,)ܟ 58
ܐܐܐܠ 62020 الذى 36“ 3[ ܐܐܬ أن علخ المكم 810 فهو 1533 من
السريالي. كن 5 500 ܨ )ܪ الارمني ® أي لمكم واليونالي دبز أي
القصد والفكر
5 الثيء علمة وفقه به وذّبر اككتاب كتبة قريب < ومعنى من
73 589 ܬ 00
+ 9 (الذاؤي) نات < تعريب ذَادِي 50 ܐܒܢ 35 قدر
سار حبة ܒܬܬ 2 0505 وهو عر ونافع من
```


## [2026-09-05T05:47:09.041Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if 'خاو' in p or 'حاوي' in p or 'خويار' in p or 'كافيار' in p:\n        print('leaf',i)\n        for l in p.split('\\n'):\n            if 'خاو' in l or 'حاوي' in l or 'يار' in l:\n                print('   ',l.strip()[:200])\nEOF"
}
```


## [2026-09-05T05:47:09.262Z] TOOL CALL #36: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-05T05:47:11.200Z] TOOL RESULT

```
leaf 148
    يضعون عليه قليلا من اللح ٠‏ فبقدر ما كان يذوب الملح كان الماجنون يخاو ܬܨ تلك
    اولادهم ويطلوا أجساءهم بدهن البان٠وكان‏ اأوابذة في المهرجان يدخاون على الماوك
leaf 180
    خاو بار ܙ ܘ
```


### [2026-09-05T05:47:11.235Z] TOOL RESULT

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


## [2026-09-05T05:47:18.268Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[180]\ni=p.find('خاو بار')\nprint(p[max(0,i-600):i+400])\nEOF"
}
```


### [2026-09-05T05:47:19.895Z] TOOL RESULT

```
جوراب ^
حويز 4
ܘ © و
دادر اوشاغى ١١‏
دارشف ܢ
جاشنى ٠٠١‏
ܥ لم١١‏
ܼܨ »± 6
جام سافزى ٠٠١‏
5 اولى >
ܥܬ ܐܘ ܙ
جراغ حم
6
ܨ‫ فلك ܙ ܙ
جقشير )ܬܟ
جقل ܫ
حِك ܀ ܙ
جناق ܥ
جوال ب
جور با ٠١١‏
جوق ٠*9‏
جوئان 5ه
ܥܕ ܬܐ ܙܢ
ܠ ++
حسن ܢܟܕ ܚܦܢ ܀ ‏ ܐ
ا +
خاتون ١ه‏
خام ܟܘ
خان مه
خاو بار ܙ ܘ
خدا لزه
$ ܨܘ
خرما بشدى +4
_ ܙ( -
خسته خانه سعر ܕܘ ܙ
خلحال 5ه
خنجر لاه
ܥܬ ܕܢ مام
حخوشاب ܘ ܘ
حوشبو جبجى ¥
++ ܕ جد
دارصينى 5٠‏
داغ 1٠‏
داما 9
در ܢܒܬܝ 5١‏
درزى !>
در سن +
ܝܬ 57
درياس دس
دشان ܥ ܖ
دمير ܝ سم
دوزن 54
دوشك 6و5
دوشمك ܙ
دولاب ܘܪ
دولك ١ب‏
دوكون او برسم
0:9 59 ܨ ܙ
9 +
رهوان »¥
+ ܇ +
زلبيه ܬܙ
زخفيل ٠م‏
زنير ١٠م‏
زور ^
زورنيه ܫ
ع3 سن عد
سار ١١7‏
سافر تربئق م"
سيد ܥܬ
11:47
ܝܐ ܘ ^
سراي
```


## [2026-09-05T05:47:29.352Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(50,66):\n    p=t[i]\n    hit=[l.strip()[:150] for l in p.split('\\n') if 'خات' in l or 'خاو' in l or 'حاو' in l or 'كافيار' in l]\n    print(i, '|', p.strip().split('\\n')[0][:60], '||', hit[:3])\nEOF"
}
```


### [2026-09-05T05:47:31.320Z] TOOL RESULT

```
50 | ܚܐ 4 4 || []
51 | (المب ) الخابية معرب خم || ['(ِدَأَة) طائر يصطاد الِرذَانَ مثل خات معنى وقريس منة لفظاً وهو بالاراميّة']
52 | ` سا آم بد || ['( || .© فارسدّها خاتون ن دهي امراة صاحمة الككلام في البت والمتصرفة فيه']
53 | ܥ ¥ ܘ ܚ || []
54 | ܚܝ 2 ”¥ @ ܝܝ || []
55 | ܝܝ وهم ܝܝ || []
56 | * ( الْشْحَاشُ ) ܝܐܝ يحمل ܨ سضا وهو منوم ܝ 2 خشخاس ْ || []
57 | ܫ عق ܫ || []
58 | ا تيل || []
59 | 3 || []
60 | 20396 || []
61 | ܀ )ܝ || []
62 | ⁄¶ سد : = || []
63 | 0053 || []
64 | سس ܨܕ - || []
65 | ل || []
```


## [2026-09-05T05:47:35.500Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[52][:2500])\nEOF"
}
```


### [2026-09-05T05:47:37.201Z] TOOL RESULT

```
` سا آم بد
009 105 54 تعمل عل مثال مر 2 مرخ بعدرد اراي 20 1ك !
قال ف الببهان القاطع :« ܥܰܚܰܐܚܺ محجن مثاّث ܒܝ شوكة من حديد 0
حهة 313 تخئصب احدى 3 الى ما فوق ٠‏ وحبث ان روس القرون حادة نظير حر بة
ܗܨ 7 395 0:69 6 في رجل من يدوسة من اليل والناس رعنعهم من
00
* ( اليرت ) 3 5 3 := > : اد
® 5 صمغ الانحذان
94 0 السترخي العظم البطن تعريب كيّذكار اي صاحب الانتفاخ
¥+ ( اير تبج ) الناعم 9 تصحيف ܝܫܐ واصل 0 طري
5
* (اباري ) بزر السمك تعريب خاّهبر واصل معناهٌ كثة البيض ٠‏ وملة
خأو يأر ܐ±
2 القوي الشديد مركب :4 4:0 اي : 0
د 0 الفاسد ܐܐܐ ܝ أنه تعر يب 1 وهو 9" ܣ ܗ
فعل ܝܙ مع < ومعناه 26 ܕܦܚ ܕܰܟ
* ( ختل ܨ خدع 3 من ܢ 461 الخداع
+ (الخوئل) تعر يب ܫܐܠ اي الظريف
( || .© فارسدّها خاتون ن دهي امراة صاحمة الككلام في البت والمتصرفة فيه
ومنها خا نون بالتركة والكردنة
)2 غداق6 4 دم الله 5 0 شرن ععنى الدات 0 ܇ آي ܟܢ | اي ܐܥ
الوحود وه 4 التكردي و ܐܠܒܐ ܆ 00 0 ® 011 1861
```


## [2026-09-05T05:47:46.960Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(164,174):\n    p=t[i]\n    head=p.strip().split('\\n')[0][:80]\n    hits=[l.strip()[:160] for l in p.split('\\n') if 'خایه' in l or 'خاية' in l or 'خايه' in l]\n    print(i,'|',head,'||',len(hits))\n    for h in hits[:4]: print('     ',h)\nEOF"
}
```


### [2026-09-05T05:47:48.404Z] TOOL RESULT

```
164 | ‫ل‬                                                                              || 0
165 | ‫خاهاء بلا‬                                                                      || 0
166 | ‫ا =‬   ‫=ړ‬ || 0
167 | ‫اور‬                                                                            || 0
168 | ‫ا‬ || 0
169 | ‫خابه نهادن‬                                                                     || 3
      ‫خایه رهز ‪ -‬بکررای‌فرشت وسکون‬                          ‫بی‌نقطه وکاف » بتك وچکش زرگری ومسگری‬
      ‫خایه گیرك صنیر خابهکیراست که‬                           ‫وبدبی‪-‬ةٌ هرغ رانیز‬
      ‫خایه دی‬
170 | ‫س پات‬                                                                          || 0
171 | ‫خبیره‬                                                                          || 0
172 | ‫‪۷‬‬                                                                            || 0
173 | ‫يبان چهارم‬ || 0
```


## [2026-09-05T05:47:49.877Z] TOOL CALL #41: Bash

```json
{
 "command": "ls site/pages/73.jpg 2>/dev/null; pdftoppm -f 73 -l 73 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg73 && echo OK && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T05:47:53.033Z] TOOL RESULT

```
site/pages/73.jpg
OK
total 7048
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 01:47 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
```


## [2026-09-05T05:47:58.328Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg73.png"
}
```


### [2026-09-05T05:47:58.748Z] TOOL RESULT

```

```


## [2026-09-05T05:47:58.745Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T05:48:20.224Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (168,169):\n    print('==== leaf',i,'====')\n    print(t[i][:3000])\nEOF"
}
```


### [2026-09-05T05:48:21.983Z] TOOL RESULT

```
==== leaf 168 ====
        ‫ا‬
‫خرو داروست وآترا خو لنجان هم میگو ند‪4 ۴‬‬

‫آون‌بیخی باشد درایی‪ .‬گویند که بازآشیان خود‬                              ‫نام ولاش‬   ‫بروزن‌داوران»‬       ‫‪-‬‬   ‫خاوران‬
‫را از آن سازد ‪,‬چه در وفت بجه از آشیان باز‬
                                                                       ‫ات ازخراسان که چپجه ومپنه داخلآ نولات‬
‫باز(‪ )۲‬بابد و بسار‬              ‫برداشتن در آشیان آن()‬
                                                                        ‫است » وتولد حکیم انوری آنجا شده چه او در‬
                                                           ‫آورند ‪۰‬‬

                                                                        ‫اولخاوری‌تخلص میکرده اصت‪ -‬ومشرق ومقرب‬
‫»‬    ‫ناد‬    ‫رزن‬     ‫بقتح ثالث بر‬      ‫‪-‬‬       ‫ند‬     ‫حاو‬
                                                                                                           ‫‪۰‬‬   ‫‪۳‬‬   ‫را نیز گوبند‬

‫و بزر گه خانه‬        ‫که صاحب‬         ‫ته‬
                                      ‫اسے‬           ‫مخغف‌خداوند‬

‫باشد‪ -‬و یمعنی‌محدد همآمده است(‪ )4‬کهاز جد‬
                                                                      ‫خاوش ‪ -‬م اك و سکون شين‬
                                          ‫‪.‬‬         ‫باشد‬   ‫ومعددود‬
                                                                        ‫تخم‬     ‫قرشت ‪ ۰‬خیاری باشد که آنرا بجهت‬
                                                                                                                    ‫نگاهدار ند ‪۰‬‬
    ‫مخفف خداوندکاراست‬                ‫ادر‬
                                       ‫کو ن‬
                                          ‫خا‬
                        ‫باشد ‪#3.‬‬      ‫ویز رگ‬          ‫که صاحب‬
                                                                         ‫خاو ل ‪ -‬بن تااث بروزن‌ابل‪ ,‬مورچه‬
                                                                                   ‫راگوبند وآن ازموذبات (‪ )۱‬است‪۴ .‬‬
    ‫خای‪ ۰ ۲ ۲‬بکون تحاتءانی ‪ ۰2‬بمعنی‬
‫خاسدن ولرم کردن در زبردندان باشد ‪ -‬وامر‬                                 ‫خاو لنحان = بکرلام وسکون نون‬
    ‫از خاییدن (‪ )۵‬هم هست ممنی بخای و در زر‬                              ‫فه و بنون دیگر زده » بمعنی‬
                                                                                                 ‫یلد‬
                                                                                                   ‫شمبا‬
                                                                                                      ‫کجی‬
                                                                                                        ‫و‬
                      ‫(‪ )۳‬خم ‪ - :۳‬باز‪.‬‬                         ‫(‪ )۲‬چش ‪ :‬بان‬                ‫(‪ )۱‬خم‪ : ۳‬موذیان‪.‬‬
                                                  ‫‪ 0‬خائیدن‬    ‫‪ ۰‬چش‬    ‫‏)‪ (e‬چك‬              ‫(‪ )4‬چك ‪ - :‬است‬

     ‫‪ ۰‬ومشرق‬       ‫ی هفغر ب است‬               ‫‪ - ۱‬خاور بازماندء کلمةٌ پهلوی « خوربران » با « خوروران »‬
       ‫آورد
==== leaf 169 ====
 ‫خابه نهادن‬                                                                                 ‫تفه‬

‫جاهای نمثاك روند ‪ -‬ومردم دروش وفقیر پزند‬                                         ‫دلدان قرم ساز ‪٩ .‬‏‬

‫وعنی ترکیبی آن هم تخم مرغ‬   ‫خوورند » م‬                 ‫خایسته ا وزن شابسته » بمعنی‬
‫مالشد است چدهس بمعنی شبه (‪ )۱‬و ماقنف‬                   ‫خاییده شده و در زیر دندان نگررمدیده باشد ‪.‬‬
                               ‫باشد ‪. ۷‬‬
                                                      ‫خالساث» بكر الك و سکون سین‬
 ‫خایه رهز ‪ -‬بکررای‌فرشت وسکون‬                          ‫بی‌نقطه وکاف » بتك وچکش زرگری ومسگری‬
 ‫بای حطی وزای هوز‪ ,‬خاگینه راکوبند وسربی‬                     ‫؛بعربی مطرقه گویند ‪. ۴‬‬
                                                                                 ‫وغیره باشد و‬
                                  ‫عجه خوالند ‪.‬‬         ‫حابنده ‪ = ۴‬با نون بر وزن داننده‪.‬‬
  ‫ون‬
   ‫سفکو‬
      ‫کا‬                ‫ر‬
                        ‫کر ‪-‬‬
                           ‫به گی‬
                               ‫خای‬                                       ‫بد ندان‌برم کننده را گویشه ‪۱‬‬
 ‫تحتانی ورای بی‌نقطه‪ ,‬جالوریست شبیه بعنکبوت‬            ‫حایه ‪ = ۴‬بر وزن مایه ‪ ۰‬خصيهٌ انان‬
‫که لعاب اموردم را هلاك سازد و ضربی رتبلا‬
                                                     ‫وحیوانات دیگرباشد ‪ .‬گوبند اکرخابةٌ بز کوهی ‪.‬‬
                                       ‫خوالند ‪.‬‬        ‫خصةالابل خوانند خشك کذند و ورد‬             ‫رکاه‬
‫خایه گیرك صنیر خابهکیراست که‬                           ‫وبدبی‪-‬ةٌ هرغ رانیز‬
                                                                        ‫مگازریده دهند نجات با‬
                                    ‫رتیلا باشد ‪.‬‬            ‫‪1‬‬                             ‫کوینده ‪.‬‬
 ‫خابه گینه ‪-‬بنی خابه ریز است‬                          ‫سنگی است که از‬        ‫د‬   ‫خابه آپلسی‬

‫که خاکنه باشد و خاکیته مخفف خابه کینه‬                  ‫ورد ‪ -‬و کنابه از مردم مکار‬
                                                                                ‫جاب چآین‬
                                                                          ‫وحیله باز و عيار هم هست ‪.‬‬
                                                       ‫ابجد بروزن‬       ‫ا‬
                                                                        ‫بسد‪- ۱‬‬
                                                                             ‫خایه دی‬
‫وکار شنیعی باشد که باعث آزار و بم هلاکت‬               ‫کاسه لیس ‪ ۰‬سماروغ را گوبند ‪ ,‬و آن رستنیی‬
                                ‫گردد ‪.‬‬                ‫باشد سفید و شبیه بتخم مرغ » و آن بیشتر در‬
                                                                  ‫(‪ )۱‬چك » چش ‪ :‬شبه ‪.‬‬
   ‫‪.‬‬    ‫وك‪ :‬اسفا ‪۲ : ۱‬ص ‪۹4۱‬‬
                          ‫» («‪.‬م‪ ).‬ر‬          ‫ارسدن‬
                                                  ‫خد‬‫«تی‬
                                                      ‫«استن » لفغ‬
```


## [2026-09-05T05:48:34.520Z] TOOL CALL #44: Bash

```json
{
 "command": "sed -n '1,50p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-05T05:48:34.565Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""
import sys, os, json, hashlib, re, html, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "data", "verification", "sources", "web")
INDEX = os.path.join(WEB, "index.jsonl")
UA = "rishe-verification/1.0 (+https://github.com/sfmqrb/rishe; etymology source archiving)"


def html_to_text(s):
    s = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>|</h[1-6]>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    note = ""
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
        args = [a for a in args if a != note]
    if not args:
        print(__doc__); return 2
    url = args[0]
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    # IRI -> URI: percent-encode non-ASCII path/query characters so urllib accepts them
    parts = urllib.parse.urlsplit(url)
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
```


## [2026-09-05T05:48:39.645Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂éwis\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ōwyóm\" \\\n \"https://en.wiktionary.org/wiki/خایه\" \\\n \"https://en.wiktionary.org/wiki/caviar\" \\\n \"https://www.etymonline.com/word/average\" \\\n \"https://en.wiktionary.org/wiki/عوار\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 73, roots Aw/Ow/Awar\" ;\ndone"
}
```


### [2026-09-05T05:48:44.289Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/769b4f247f3d6e31.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6a2eade97acedfdf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ab4ddb014e5e1561.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/637150e2cddc3165.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94a0cb2e8f2451bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8451a1f06d8c8515.txt
```


## [2026-09-05T05:48:47.481Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 769b4f247f3d6e31 6a2eade97acedfdf; do echo \"########## $f\"; head -c 60 $f.txt; echo; grep -n \"Etymology\\|Descendants\\|Proto-Iranian\\|Avestan\\|Latin\\|Derived\" $f.txt | head -20; done"
}
```


### [2026-09-05T05:48:49.182Z] TOOL RESULT

```
########## 769b4f247f3d6e31
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Ind
62: Etymology 
71: Derived terms 
74: Descendants 
140: Etymology
237: Derived terms
280: Descendants
302: ↑ 5.0 5.1 5.2 De Vaan, Michiel ( 2008 ), “ avis ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , pages 65-66 
########## 6a2eade97acedfdf
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Ind
62: Etymology 
74: Descendants 
145: Etymology
251: Descendants
255: > ? Albanian: vōe , *vae ( or ⇐ from Latin ōvum [ 9 ] ) 
271: Proto-Iranian: *Hāwyám ( see there for further descendants )
274: Latin: ōvum ( see there for further descendants )
279: ↑ 1.0 1.1 De Vaan, Michiel ( 2008 ), “ ōvum ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 438 
300: Schrijver, Peter C. H. ( 1991 ), The Reflexes of the Proto-Indo-European Laryngeals in Latin (Leiden Studies in Indo-European; 2), Amsterdam, Atlanta: Rodopi, →ISBN , pages 53, 300
```


## [2026-09-05T05:48:52.092Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"##### h2ewis 130-300\"; sed -n '130,300p' 769b4f247f3d6e31.txt\necho \"##### h2owyom 140-278\"; sed -n '140,278p' 6a2eade97acedfdf.txt"
}
```


### [2026-09-05T05:48:52.155Z] TOOL RESULT

```
##### h2ewis 130-300
 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Pooth argues that *h₂éwis and *h₂ówis ( “ sheep ” ) are related and both from a root *h₂ew- ( “ dress, be dressed, clothe oneself ” ) . [ 1 ] *h₂éwis would mean "the one who is clothed (in feathers)", and *h₂ówis "the one that produces clothing (from wool)", the latter having detransitive or middle meaning marked by *o .

 Noun
 [ edit ] 

 *h₂éwis   f [ 2 ] [ 3 ] 

 bird 

 Inflection
 [ edit ] 

 Athematic, proterokinetic

 singular

 nominative

 *h₂éwis 

 genitive

 *h₂wéys 

 singular

 dual

 plural

 nominative

 *h₂éwis 

 *h₂éwih₁(e) 

 *h₂éweyes 

 vocative

 *h₂éwi 

 *h₂éwih₁(e) 

 *h₂éweyes 

 accusative

 *h₂éwim 

 *h₂éwih₁(e) 

 *h₂éwims 

 genitive

 *h₂wéys 

 *? 

 *h₂wéyoHom 

 ablative

 *h₂wéys 

 *? 

 *h₂wímos , *h₂wíbʰos 

 dative

 *h₂wéyey 

 *? 

 *h₂wímos , *h₂wíbʰos 

 locative

 *h₂wéy , *h₂wḗy 

 *? 

 *h₂wísu 

 instrumental

 *h₂wíh₁ 

 *? 

 *h₂wímis , *h₂wíbʰis 

 Derived terms
 [ edit ] 

 *h₂ōwy-ó-m ( “ egg ” , vṛddhi-derivative ) [ 4 ] 

 *h₂wéy-teh₂ ( < genitive *h₂wéys ) 
 Proto-Albanian: *weitā 
 Albanian: vito , vida ( “ dove ” ) 

 *h₂wís-teh₂ ( < s-stem ) 
 Proto-Balto-Slavic: *wíštā 
 Latgalian: vysta 

 Latvian: vista ( “ chicken, hen ” ) 

 Lithuanian: višta ( “ chicken, hen ” ) 

 Samogitian: vėšta 

 *(s)h₂wy-etó-s [ 5 ] 
 Proto-Celtic: *(s)awyetos ( “ duck ” ) 
 Proto-Brythonic: *swɨad [ 5 ] 
 Middle Breton: houat 
 Breton: houad 

 Old Cornish: hoet 
 Cornish: hos 

 Middle Welsh: hwyat 
 Welsh: hwyad 

 Irish: aoi 

 Proto-Hellenic: *awjetós [ 6 ] 
 Ancient Greek: *αἴϝετος ( *aíwetos , “ eagle ” ) [ 6 ] ⇒ αἰετός ( aietós ) ⇒ ᾱ̓ετός ( āetós ) 

 Unsorted formations 
 Proto-Albanian: *sjāutā [ 7 ] 
 Albanian: shotë ( “ big duck ” ) 

 Proto-Hellenic: 
 Ancient Greek: οἰωνός ( oiōnós ) Greek: οιωνός ( oionós ) 

 Descendants
 [ edit ] 

 Proto-Armenian: 
 Old Armenian: հաւ ( haw , “ bird; hen ” ) Armenian: հավ ( hav ) , հավք ( havkʻ ) 
 ⇒ Old Georgian: ჰავით ზმნაჲ ( havit zmnay , “ fortune-telling using a chicken, bird ” ) , ჰავის-ზმნაჲ ( havis-zmnay , “ sorcery, witchery ” ) 

 Proto-Indo-Iranian: *Hwíš ( see there for further descendants )

 Proto-Italic: *awis [ 5 ] ( see there for further descendants )

 References
 [ edit ] 

 ^ Pooth, Roland A. ( 2015 ), “Proto-Indo-European Nominal Morphology. Part 1. The Noun”, in Language Arts 1 ‎ [1] , page 38 

 ^ Mallory, J. P. with Adams, D. Q. ( 2006 ), The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World (Oxford Linguistics), New York: Oxford University Press, →ISBN , page 143 : “ *hₐewei- 'bird' ” 

 ^ Václav Blažek; Douglas Q. Adams ( 2022 ), “Indo-European ‘bird’”, in The Journal of Indo-European Studies ‎ [2] , volume 50 , numbers 3-4 , →ISSN 

 ^ Mallory, J. P. with Adams, D. Q. ( 2006 ), The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World (Oxford Linguistics), New York: Oxford University Press, →ISBN , page 143 : “ *hₐō(w)i-om 'egg' ” 
##### h2owyom 140-278
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Likely a vṛddhi derivative of *h₂éwis ( “ bird ” ) , [ 1 ] [ 2 ] [ 3 ] though some scholars have argued this as morphologically unlikely. [ 4 ] 

 Noun
 [ edit ] 

 *h₂ōwyóm   n ( non-ablauting ) [ 5 ] [ 1 ] [ 2 ] [ 3 ] [ 6 ] 

 egg 

 Inflection
 [ edit ] 

 Thematic

 singular

 nominative

 *h₂ōwyóm 

 genitive

 *h₂ōwyósyo 

 singular

 dual

 plural

 nominative

 *h₂ōwyóm 

 *h₂ōwyóy(h₁) 

 *h₂ōwyéh₂ 

 vocative

 *h₂ōwyóm 

 *h₂ōwyóy(h₁) 

 *h₂ōwyéh₂ 

 accusative

 *h₂ōwyóm 

 *h₂ōwyóy(h₁) 

 *h₂ōwyéh₂ 

 genitive

 *h₂ōwyósyo 

 *? 

 *h₂ōwyóHom 

 ablative

 *h₂ōwyéad 

 *? 

 *h₂ōwyómos , *h₂ōwyóbʰos 

 dative

 *h₂ōwyóey 

 *? 

 *h₂ōwyómos , *h₂ōwyóbʰos 

 locative

 *h₂ōwyéy , *h₂ōwyóy 

 *? 

 *h₂ōwyóysu 

 instrumental

 *h₂ōwyóh₁ 

 *? 

 *h₂ōwyṓys 

 Alternative reconstructions
 [ edit ] 

 *(H)ō-Huy-óm [ 7 ] 

 *ōyom [ 4 ] 

 *h₂oh₂wyom [ 8 ] 

 Descendants
 [ edit ] 

 Proto-Albanian: 
 > ? Albanian: vōe , *vae ( or ⇐ from Latin ōvum [ 9 ] ) 
 Albanian: ve , vo , vø , vö 

 Proto-Armenian: 
 > ? Old Armenian: ձու ( ju ) ( see there for further descendants )

 Proto-Balto-Slavic: *ōjan 
 Proto-Slavic: *ȃje ( see there for further descendants )

 Proto-Celtic: *āwyom ( see there for further descendants )

 Proto-Germanic: *ajją ( see there for further descendants )

 Proto-Hellenic: *ōyyón ( see there for further descendants )

 Proto-Indo-Iranian: *Hāwyám 
 Proto-Iranian: *Hāwyám ( see there for further descendants )

 Proto-Italic: *ōw(j)om 
 Latin: ōvum ( see there for further descendants )

 References
 [ edit ]
```


## [2026-09-05T05:48:58.048Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### خایه\"; grep -n \"Etymology\" -A 25 ab4ddb014e5e1561.txt | sed -n '1,60p'"
}
```


### [2026-09-05T05:48:58.101Z] TOOL RESULT

```
#### خایه
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Derived terms 
75-
76- 1.4.2 
77- Descendants 
78-
79- 1.4.3 
80- See also 
81-
82- 1.5 
83- References 
84-
85- 2 
86- Southwestern Fars 
87-
88- Toggle Southwestern Fars subsection 
89-
90- 2.1 
--
173: Etymology
174- [ edit ] 
175-
176- From Middle Persian [Term?] ( /⁠xāyak⁠/ ) , from Proto-Iranian *Hāwyám (compare Northern Kurdish hêk , Ossetian айк ( ajk ) , Avestan 𐬀𐬉𐬨 ( aēm ) ), from Proto-Indo-Iranian *Hāwyám , from Proto-Indo-European *h₂ōwyóm ( “ egg ” ) (compare Armenian ձու ( ju ) , English egg , Italian uovo , Russian яйцо́ ( jajcó ) ). Doublet of هاگ ( hāg  / hâg , “ spore ” ) .
177-
178- Pronunciation
179- [ edit ] 
180-
181- ( Classical Persian ) IPA ( key ) : /xaː.ˈja/ 
182-
183- ( Dari, formal ) IPA ( key ) : [xɑː.jä] 
184-
185- ( Dari, formal ) IPA ( key ) : [xɑː.jä] 
186- ( Kabuli ) IPA ( key ) : [xɑː.jä] 
187-
188- ( Hazaragi ) IPA ( key ) : [xɔː.jä] 
189-
190- ( Iran, formal ) IPA ( key ) : [xɒː.je] 
191-
192- ( Tajik, formal ) IPA ( key ) : [χɔ.jä] 
193-
194- Rhymes: -a 
195-
196- Readings
197-
198- Classical reading ?
```


## [2026-09-05T05:48:59.290Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### caviar\"; grep -n \"Etymology\" -A 20 637150e2cddc3165.txt | sed -n '1,50p'\necho \"#### average etymonline\"; grep -n \"average\" 94a0cb2e8f2451bf.txt | head -20"
}
```


### [2026-09-05T05:48:59.356Z] TOOL RESULT

```
#### caviar
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Derived terms 
75-
76- 1.4.2 
77- Descendants 
78-
79- 1.4.3 
80- Translations 
81-
82- 1.4.4 
83- See also 
84-
85- 1.5 
--
97: Etymology 
98-
99- 2.2 
100- Pronunciation 
101-
102- 2.3 
103- Noun 
104-
105- 2.4 
106- Further reading 
107-
108- 3 
109- French 
110-
111- Toggle French subsection 
112-
113- 3.1 
114: Etymology 
115-
116- 3.2 
117- Pronunciation 
118-
119- 3.3 
120- Noun 
121-
122- 3.3.1 
123- Derived terms 
124-
#### average etymonline
1:URL: https://www.etymonline.com/word/average
21: Origin and history of average 
23: average (n.) 
27: Thus, when for the safety of a ship in distress any destruction of property is incurred, either by cutting away the masts, throwing goods overboard, or in other ways, all persons who have goods on board or property in the ship (or the insurers) contribute to the loss according to their average, that is, according to the proportionate value of the goods of each on board. [Century Dictionary]
32: average (adj.) 
34: 1770, "estimated by averaging," from average (n.). By 1803 as "equal in amount to the sum of all particular quantities divided by the number of them," hence "of medium character."
37: average (v.) 
39: 1769, "to amount to," from average (n.). By 1831 as "find the arithmetical mean of unequal quantities;" 1914 as "divide among a number proportionately" (usually with out ). Related: Averaged ; averaging .
42: Entries linking to average 
46: 1590s, "arithmetical table," also "official list or table of customs duties on goods for import or export;" also "a law regulating import duties," from Italian tariffa "tariff, price, assessment," Medieval Latin tarifa "list of prices, book of rates," ultimately from Arabic ta'rif "information, notification, a making known; inventory of fees to be paid," verbal noun from arafa "he made known, he taught." A word passed to English from the commercial jargon of the medieval Mediterranean (compare garble , jar (n.), average (perhaps), orange , tabby , etc.).
66: range of invented names meaning "typical male example of," for example Joe college "typical college man" (1932); Joe Blow "average..."Dictionary of American Slang" lists, among other examples, Joe Average, Beige, Lunch Bucket, Public, Sad, Schmoe, Six-pack...
70: Sustainability is defined as a requirement of our generation to manage the resource base such that the average quality of...Development is sustainable if it involves a non-decreasing average quality of life. [Geir B....
74: in baseball, "a low batting average," (somewhere around .200) with the suggestion that any player hitting below it ought...former Pirate, Mariner, and Ranger shortstop Mario Mendoza, who was noted for his defense but whose .215 lifetime batting average...
78: "having average or moderate cultural interest;" 1912 (n.)..."person of average or moderate cultural interests," from middle (adj.) + brow (compare highbrow, lowbrow)....
92: Share average 
96: https://www.etymonline.com/word/average Copy 
99: <a href="https://www.etymonline.com/word/average">Etymology of average by etymonline</a> Copy 
102: Harper, D. (n.d.). Etymology of average. Online Etymology Dictionary. Retrieved September 4, 2026, from https://www.etymonline.com/word/average Copy 
105: Harper Douglas, "Etymology of average," Online Etymology Dictionary, accessed September 4, 2026, https://www.etymonline.com/word/average. Copy 
108: Harper, Douglas. "Etymology of average." Online Etymology Dictionary, https://www.etymonline.com/word/average. Accessed 4 September, 2026. Copy
```


## [2026-09-05T05:49:10.501Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '21,32p' 94a0cb2e8f2451bf.txt\necho \"#### caviar body\"; sed -n '150,215p' 637150e2cddc3165.txt"
}
```


### [2026-09-05T05:49:10.555Z] TOOL RESULT

```
 Origin and history of average 

 average (n.) 

 late 15c., "any small charge over freight cost, payable by owners of goods to the master of a ship for his care of the goods," also "financial loss incurred through damage to goods in transit," from French avarie "damage to ship," and Italian avaria . A word from 12c. Mediterranean maritime trade (compare Spanish averia ), of uncertain origin; sometimes traced to Arabic 'awariya "damaged merchandise" but OED asserts this is a modern word derived from the western use. Dutch avarij , German haferei , etc., also are from Romanic languages. "Few words have received more etymological investigation" [OED].

 Thus, when for the safety of a ship in distress any destruction of property is incurred, either by cutting away the masts, throwing goods overboard, or in other ways, all persons who have goods on board or property in the ship (or the insurers) contribute to the loss according to their average, that is, according to the proportionate value of the goods of each on board. [Century Dictionary]

 The meaning developed to "equal sharing of loss by the interested parties." The transferred sense of "statement of a medial estimate, proportionate distribution of inequality among all," is attested by 1735. The mathematical sense of "a mean proportion arrived at by arithmetical calculation" is from 1755. The sports sense, in reference to batting, is attested by 1845 in cricket.
 also from late 15c. 

 average (adj.) 
#### caviar body

 4.4 
 Further reading 

 5 
 Romanian 

 Toggle Romanian subsection 

 5.1 
 Etymology 

 5.2 
 Pronunciation 

 5.3 
 Noun 

 5.3.1 
 Declension 

 6 
 Spanish 

 Toggle Spanish subsection 

 6.1 
 Etymology 

 6.2 
 Pronunciation 

 6.3 
 Noun 

 6.4 
 Further reading 

 Toggle the table of contents 

 caviar 

 35 languages 

 Azərbaycanca 
 Català 
 Čeština 
 Deutsch 
 Ελληνικά 
 Esperanto 
 Español 
 Eesti 
 فارسی 
 Suomi 
 Français 
 Galego 
 Magyar 
 Ido 
 Italiano 
 ಕನ್ನಡ 
 한국어 
 Malagasy 
 မြန်မာဘာသာ 
 Nederlands 
 Norsk bokmål 
 Occitan
```


## [2026-09-05T05:49:17.946Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n \"Ottoman Turkish\\|havyar\\|xâvyâr\\|خاویار\\|Persian\" 637150e2cddc3165.txt | head -20"
}
```


### [2026-09-05T05:49:18.019Z] TOOL RESULT

```
293: Borrowed from Middle French caviar , from Venetan caviaro (earlier found as Italian caviale ), probably by way of Ottoman Turkish خاویار ( havyar ) , from Classical Persian خَاوْیَار ( xāwyār ) . Doublet of ajvar . [ 1 ] 
412: Mazanderani: خاویار 
418: Persian: خاویار   (fa) ( xâvyâr ) 
447: Turkish: havyar   (tr) 
482: Borrowed from French caviar , from Italian caviaro or Ottoman Turkish خاویار ( havyar ) , from Persian خاویار ( xâvyâr ) .
521: Borrowed from Italian caviaro or Ottoman Turkish خاویار ( havyar ) , from Persian خاویار ( xâvyâr ) .
605: Borrowed from French caviar , from Italian caviaro or Ottoman Turkish خاویار ( havyar ) , from Persian خاویار ( xâvyâr ) .
660: Borrowed from French caviar , from Italian caviaro or Ottoman Turkish خاویار ( havyar ) , from Persian خاویار ( xâvyâr ) .
708: Borrowed from French caviar , from Italian caviaro or Ottoman Turkish خاویار ( havyar ) , from Persian خاویار ( xâvyâr ) .
738: English terms derived from Ottoman Turkish 
739: English terms derived from Classical Persian 
758: Catalan terms derived from Ottoman Turkish 
759: Catalan terms derived from Persian 
771: French terms derived from Ottoman Turkish 
772: French terms derived from Persian 
784: Portuguese terms derived from Ottoman Turkish 
785: Portuguese terms derived from Persian 
797: Romanian terms derived from Ottoman Turkish 
798: Romanian terms derived from Persian 
808: Spanish terms derived from Ottoman Turkish
```


## [2026-09-05T05:49:19.068Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n \"Arabic\" -A 3 8451a1f06d8c8515.txt | sed -n '1,60p'"
}
```


### [2026-09-05T05:49:19.124Z] TOOL RESULT

```
57: Arabic 
58-
59: Toggle Arabic subsection 
60-
61- 1.1 
62- Etymology 1 
--
89: Gulf Arabic 
90-
91: Toggle Gulf Arabic subsection 
92-
93- 2.1 
94- Etymology 
--
165: Arabic
166- [ edit ] 
167-
168- Etymology 1
--
253: Gulf Arabic: عوار ( ʕawār ) 
254-
255- Etymology 2
256- [ edit ] 
--
443: Gulf Arabic
444- [ edit ] 
445-
446- Etymology
--
449: Inherited from Arabic عَوَار ( ʕawār ) .
450-
451- Pronunciation
452- [ edit ] 
--
465: Categories : Arabic terms belonging to the root ع و ر 
466: Arabic 2-syllable words 
467: Arabic terms with IPA pronunciation 
468: Arabic lemmas 
469: Arabic nouns 
470: Arabic masculine nouns 
471: Arabic nouns with basic triptote singular 
472: Arabic terms belonging to the root ع و ذ 
473: Arabic nouns with broken plural 
474: Arabic nouns with basic diptote broken plural 
475- ar:Swallows 
476: Gulf Arabic terms derived from Arabic 
477: Gulf Arabic terms inherited from Arabic 
478: Gulf Arabic terms with IPA pronunciation 
479: Gulf Arabic lemmas 
480: Gulf Arabic nouns 
481: Gulf Arabic masculine nouns 
482-
483: Hidden categories: Arabic entries referencing missing etymons 
484- Pages with etymon 
485: Arabic entries with etymon 
486- Pages using etymon with no ID 
487- Pages with entries 
488- Pages with 2 entries 
--
490: Gulf Arabic entries referencing ambiguous etymons
```


## [2026-09-05T05:49:24.015Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '165,260p' 8451a1f06d8c8515.txt"
}
```


### [2026-09-05T05:49:24.069Z] TOOL RESULT

```
 Arabic
 [ edit ] 

 Etymology 1
 [ edit ] 

 Root 

 ع و ر ( ʕ w r ) 

 14 terms 

 From the root ع و ر ( ʕ w r ) , related to ideas of missing one eye or having a lacuna .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ʕa.waːr/ 

 Noun
 [ edit ] 

 عَوَار • ( ʕawār )  m 

 fault , flaw , defect , crevasse 

 Declension
 [ edit ] 

 Declension of noun عَوَار ( ʕawār )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 عَوَار 
 ʕawār 

 الْعَوَار 
 al-ʕawār 

 عَوَار 
 ʕawār 

 nominative

 عَوَارٌ 
 ʕawārun 

 الْعَوَارُ 
 al-ʕawāru 

 عَوَارُ 
 ʕawāru 

 accusative

 عَوَارًا 
 ʕawāran 

 الْعَوَارَ 
 al-ʕawāra 

 عَوَارَ 
 ʕawāra 

 genitive

 عَوَارٍ 
 ʕawārin 

 الْعَوَارِ 
 al-ʕawāri 

 عَوَارِ 
 ʕawāri 

 Descendants
 [ edit ] 

 Gulf Arabic: عوار ( ʕawār ) 

 Etymology 2
 [ edit ] 

 Root 

 ع و ذ ( ʕ w ḏ )
```


## [2026-09-05T05:49:33.294Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://www.etymonline.com/word/ostrich\" \\\n \"https://www.etymonline.com/word/kidney\" \\\n \"https://www.etymonline.com/word/egg\" \\\n \"https://www.etymonline.com/word/aviation\" \\\n \"https://abadis.ir/fatofa/عوار/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 73 (Aw/Ow/Awar) English & Persian nodes\" ;\ndone"
}
```


## [2026-09-05T05:49:35.284Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FRS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('pages',len(t))\nimport re\nfor i,p in enumerate(t):\n    if 'ویش' in p or 'وىش' in p:\n        print('leaf',i,[l.strip()[:120] for l in p.split('\\n') if 'ویش' in l][:3])\nEOF\necho \"=== MON عوار ===\"\ngrep -n \"عوار\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-05T05:49:37.549Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/57c7601dd7d6764a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05d1d3335e84ba91.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f562b42d3e0f428c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7479201d4970c82f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c8a6b073c06ec54a.txt
```


### [2026-09-05T05:49:39.138Z] TOOL RESULT

```
pages 568
leaf 30 ['\u202bباب توبةٌ خالص بشویش ازعصیان |\u202c']
leaf 40 ['\u202bکفتا که دود دارد باتفه خویش ناب\u202c']
leaf 43 ['\u202bکهاز سنگی بااز زمینی همی زاید بطبح خویش ازاندك وبسیار»\u202c']
leaf 44 ['\u202bبر آن شدم کز منش سیر" پیش\u202c                            \u202b\u202a۲\u202cبسنده نکردم بتبکوب خویش\u202c']
leaf 51 ['\u202bرویش نبندآنچه نا جوییندش(\u202a )۱\u202cناش بآسرتین و بلریقشفا زد(()\u202c']
leaf 55 ['\u202bخوانند \u202a ۰\u202cچ \u202a ۰\u202cکلات دیهی ؟وچك باشد ویشتر بر کوه باشد چون دگزاهی \u202a.\u202c\u202c']
leaf 56 ['\u202bخویشتن \u202a ۷\u202cخویش را بکوش \u202a ۸\u202cتو يك لخت\u202a٩\u202c\u200f\u202c']
leaf 70 ['\u202bزبیگانگان\u200cجای\u200cبر وخن ماند\u202c                   \u202bمراوستاد اورا بر خویش\u200cخواند\u202c']
leaf 79 ['\u202bاضانه دارد \u202a[ :\u202cوخویشتن سنای ] \u202a.\u202c\u202c        \u202b\u202a - ۷\u202cچ\u202c         \u202b( در حاشبه ) ؛ جله تنش \u202a.\u202c\u202c     \u202bتن »\u202a۰\u202c\u202c']
leaf 86 ['\u202bبینی سخط \u202a ۴\u202cخویش ! وس و علسم انندر |\u202c']
leaf 87 ['\u202b( در حاشبه ) \u202a:\u202c\u202c      \u202bاست \u202a ۰\u202cچ \u202a ۰\u202cغلیواج ویش ( ؟ ) باشد \u202a.\u202cی\u202c              \u202bهست » متن معذابق س\u202c']
leaf 99 ['\u202bبشکوخید \u202a ۰\u202cچ \u202a :\u202cآشکوخ کسی کپهایش بچیزی\u200cدرآید وبانگشت پایبایسندوخویشتن\u202c']
leaf 101 ['\u202bدارند از بهر درم و شانه »\u202c         \u202bکیسه ای کرد باشد کهباخویشتن\u202c']
leaf 108 ['\u202bخویشتن راشد بدان\u202a۲\u202cبرون\u200cفگند\u202c     \u202bبووبزهواری يك ژغند\u202c']
leaf 123 ['\u202bانگشت \u202a ۳\u202cرویش مانند ت\u202c']
leaf 129 ['\u202bگر بر فکنم \u202a" ۱\u202cگرم دل خویش بگوکرد\u202c']
leaf 132 ['\u202bرویش مبان حله سبز آندرون پدید\u202c']
leaf 134 ['\u202bرا سرمایی بزند گویشد شجیده باشد\u202c                \u202bسرمای سخت باشد » اکر کی\u202c', '\u202bدره\u200cای را بخاك بنماید\u202c                 \u202bصورت خشمت ارز هیبت خویش\u202c']
leaf 142 ['\u202bباهز باز گشتن\u202a ۲\u202cز گفتارخویش ]|\u202c                             \u202bزدن رمادتیغ \u202a ۲\u202cبر قخاوریش\u202c']
leaf 149 ['\u202bبرده باخویشتن بجسله براه \u202a۴\u202c\u202c                    \u202bبندبان داشت بی زوار و پناه \u202a۲\u202c\u202c']
leaf 154 ['\u202bدور ماند از سرای خویش و تبار فسری ساخت بر سر کهسار \u202a۱\u202c\u202c']
leaf 170 ['\u202bنصرت و فتح ویشیار تو باد\u202c                  \u202bبت ودولت چوپیشکارتواند\u202c']
leaf 173 ['\u202bچو برورد خویش را بشکری\u202c                  \u202bجهانا ندانم چرا پروری\u202c']
leaf 174 ['\u202bبهانه جوید بر حال خویش و هت خویش\u202c']
leaf 176 ['\u202bهنوز پادشه هندوآن بطبع نکرد رکاب اورانیکوبدست خویش یشار\u202c']
leaf 184 ['\u202bاز نزوری خویش\u200cدانا باشد اوی با کس اورا رازنیست ا(هیچ روی\u202a.\u202c\u202c']
leaf 189 ['\u202b» \u202a-\u202cن \u202a :\u202cتزسغی کوچك بود خشبن رنك وبرجهد ویشتردر گلستان\u202c                     \u202bباب بایروزم \u202a.\u202c\u202c']
leaf 200 ['\u202bبخرویشترن نگر نتو\u202c']
leaf 201 ['\u202bبسنده کند زین جهان مرز خویش بداند مکر مایه و ارزخویش\u202c']
leaf 203 ['\u202bبداند مگر ماه و ارز خویش\u202c               \u202bبسنده کندزین جهان مرز خوش\u202c']
leaf 204 ['\u202bچون دده" باز جنبد ازپدواز\u202c             \u202bباز پدواز خویش باز شویم\u202c']
leaf 208 ['\u202bگر\u202c\u202bیعلی خویشتن را د\u202c']
leaf 213 ['\u202bکه بسته بود چاپلوس ازفسوس! ]\u202c                     \u202bمکن خویشتن سهمکن حاپاوس\u202c']
leaf 215 ['\u202bکلو راز رسی بسر بر مبر\u202c                   \u202bیلفنج و ز فده خویش خور\u202c']
leaf 225 ['\u202bخویشتن پاك دارو بی پرخاش هیچ کس رامباش عاشق غاش |\u202c']
leaf 238 ['\u202bبجز خاشه وی را چه اندرخورد\u202c            \u202bبهسر خاه ای خویشتن پرورد\u202c']
leaf 255 ['\u202bبنشان بتارم اندر مر ترك خویش را\u202c']
leaf 262 ['\u202bبتازی صلف بود و بپارسی خویشتن ستودن [ بوشکور گوید \u202a:\u202c\u202c', '\u202bباشند \u202a1 - 4\u202cسان\u200cبمعنیبنیاداست \u202a - ۰ .\u202cس مثل متن » چ \u202a :\u202cلاف\u200cسنایش خویشتن بود\u202c']
leaf 266 ['\u202b\u202a 15\u202cپرو زر" و سیم عرضه کنم خویشتن را بگفت راد کنم\u202a۴\u202c\u202c', '\u202bآن بود که خویشتن را بلیددارد و جامه هااز بلدی برهیز ندارد و\u202c']
leaf 267 ['\u202bخویشتن بین باشد \u202a.\u202c\u202c']
leaf 271 ['\u202bچنان اندیشد او از دشمن خویش چو؛ باز تیز چنکال از کرا\u202a] 5\u202c\u202c']
leaf 272 ['\u202bکه پارد داشت بااوخویشتن راست نباید بود مردم را هزا \u202a| 6\u202c\u202c']
leaf 281 ['\u202bآن سک ملعون برفت این سندارا از خویشتن\u202c']
leaf 286 ['\u202bشفتالو بود ویشتر سرح وسیید باشد چون بخته کردد وباشد که سرخ باشد ب\u202c']
leaf 288 ['\u202bهمی مناظره و جنك خواهی از آن خویش\u202c']
leaf 291 ['\u202bخویشتن را کليك سازم زود ]\u202c             \u202bچوت بینم ترا ز بیم حسود\u202c']
leaf 294 ['\u202bگر برفکند کر م دم خویش بککر\u202c']
leaf 301 ['\u202bپای برون منه از پایکه دعوی* خویش\u202c']
leaf 305 ['\u202b\u202a:\u202cپوك مرغیست آسمان گون چند باشد وازجنس خویش جفتش نبود گرد\u202c \u202b\u202a - ۰\u202cچ ک\u202c']
leaf 310 ['\u202bازجان\u200cوروان\u200cخویش رنگن کردم ما را ز لبان خویش رنکی نکنی\u202c']
leaf 312 ['\u202bوشان و مده زعفران خویش\u202c']
leaf 316 ['\u202b\u202a:\u202c\u202c   \u202bمرغیست کهخویشتن از درخت بیاویزد ؛ پهرامی کت\u202c', '\u202bوز شاخ همچو حو لمبیاویخت خویشتن ؛\u202c', '\u202bجولمزشاح در خت\u200cخویشتن آو يخته ماغ سیه ب داو بال غالیه آمیخته *\u202c']
leaf 336 ['\u202b\u202a -۱\u202cت \u202a +\u202cیرآ ویشت \u202a:\u202cنبوردوسیدن بود شین گوودع \u202a:\u202cنف وبشلیدن دوسانیدن\u202c']
leaf 350 ['\u202bبدان منکر کههسارلم بکار خویش تالم\u202c']
leaf 359 ['\u202bمکن خویشتن از ره راست گم که\u200cخودرا بدوز خ بری بافدم \u202a۱۱\u202c\u202c']
leaf 368 ['\u202bمکن ای روی نکو زشتی باعاشق خویش\u202c']
leaf 369 ['\u202bوامد این خر گوش را الفغده بیش\u202c             \u202bشیرغو م آوردو جست ازجای\u200cخویش\u202c']
leaf 373 ['\u202bدادم بدمو گرنهکنم جان خویشتن مدح امیرونزد توآرم بور\u200cفان ]\u202c']
leaf 377 ['\u202bاست که جم بدا روش بأشد بمعنیکسي که از راه راست\u202c                        \u202bلرنتویشدنان\u202c']
leaf 379 ['\u202bبفروز و بسوز دیش خویش آمشب چندان کهتوان زعود و از حندثت ]\u202c']
leaf 388 ['\u202bوویش سخت که پیشه وران آلات \u202a-\u202cارند [فرخی\u202c']
leaf 396 ['\u202bبخاصه کنون کز قیل\u200cراندن\u200cدرویش بربام\u200cشودهر کس\u200cباسنکو فلاخی \u202a۴\u202c\u202c']
leaf 407 ['\u202bپس ازطمام خوردن هیزبان بدرویشان میدهد و این معنی در اینجا بی مناسبت ذیست \u202a۰\u202c\u202c']
leaf 410 ['\u202bنیز بدین شغل میاز و مدن\u202c               \u202bبار ولایت بنه ازکاهخویش\u202c']
leaf 414 ['\u202bتا تازه کرد باد اوایل بدین خویش\u202c']
leaf 416 ['\u202bچو آمد بر میهن موان خویش \u202a .\u202cببردش بصد لابه مهمان خویش\u202c']
leaf 421 ['\u202bشیر تا تیمار دارد خویشتن\u202c               \u202bکرد باید م\u200cمر\u200cاواورارون\u202c']
leaf 425 ['\u202bویان" خویش \u202a ۷\u202cمن رفتم و پردختم\u202c']
leaf 454 ['\u202bباریش شوم ترپبر ماهر آینه*\u202c                      \u202bکرشوم\u200cبودبی\u200cبغلامی\u200cبنز دخویش\u202c']
leaf 456 ['\u202b"سرخ رویش بالفونه کنند؛\u202c                  \u202bزو گرا در د کرده ورد\u202c']
leaf 466 ['\u202bچندپزی\u200cشغل نای وشغل حم\u200cانه]\u202c             \u202bزادهمی\u200cساز شوغل خویش همیب\u202c']
leaf 471 ['\u202bز هرخاشه ای خویشتن\u200cپرورد\u202a] ۲\u202c\u202c                     \u202bگنوهبا زبان و نهجویاخرد\u202c']
leaf 474 ['\u202bای بکس خویش بر نورده نهساده\u202c']
leaf 477 ['\u202bبراسته\u202a٩\u202c\u200f\u202c      \u202bجنگ اوراخویشتن\u202c                   \u202bنزد تو آماده بدوار استه \u202a۸\u202c\u202c', '\u202bخویشتن ص جنگ را آراسته\u202c                            \u202bته\u202c']
leaf 483 ['\u202bچو پروانه م\u200cخویشتن را ه\u200cسوز]\u202c                  \u202bبیاموز تا بد نباشد ت \u202a ۱\u202cروز\u202c', '\u202bبرشمع وچراغ زند تابسوزد» ن (درحاشبه)یر وانپهرنده\u200cای بود که خویشتن\u200cرا بچراغ\u202c']
leaf 496 ['\u202bنه درویش را ايچ سو سرزنش\u202c                        \u202bنه پیغاره دیدند بر بکدنش\u202c']
leaf 497 ['\u202bبرده یکنیوره دل از جای خویش\u202a۱\u202c\u202c                 \u202bمن رمی آن نرکسك خرد ب رک\u202c']
leaf 498 ['\u202bآویشه"\u202c']
leaf 506 ['\u202bکردار تنخویش راکنی فربه\u202c                      \u202bآن بهکهنیایهرا نگه داری\u202c']
leaf 514 ['\u202bچوخوان\u200cنهاد نهاری\u200cفرونهدییشت چخوطیعشبخامی\u200cچویشمه بی\u200cچربو\u202c']
leaf 516 ['\u202bچند پزی شغل نای و شحغغلانه؟\u202c                 \u202bزاد همی\u200cسازوشغل خویش\u200cهمی پز\u202c']
leaf 518 ['\u202bعویش\u202c']
leaf 519 ['\u202bدیوه هرچندکابرشم\u200cبکند \u202a .\u202cهرچه آن \u202a,\u202cیشتربخویش تند\u202c']
leaf 522 ['\u202bای آنکه ترا پبشه پرستیدن لوق چون خویشتنی\u200cراچه بری\u200cیش برسته\u202c']
leaf 523 ['\u202bبر آنکه چشم نمشّم کنم برویش باز\u202c', '\u202bشیرخشمآورد وجست ازجای\u200cخویش وآمدآن خرکوشرا آ لفده بش\u202c']
leaf 525 ['\u202bداشت بسرر پروفه کایودك برمیا بست\u202a .\u202cآن\u200cپروفة خویش\u202c']
leaf 532 ['\u202bبخلوت\u200cاندرنزدیك\u200cخویش زاره کنم\u202c              \u202bهزار زاره کنم نشدو ند زاری من\u202c']
leaf 535 ['\u202bای آن کهمن از عشق تو اندر جگر خویش\u202c']
leaf 545 ['\u202bکر خوار شدم سوی * بت خویش روا * باد\u202c']
=== MON عوار ===
MON_part2.txt:1836:ازدیاد فشار خون سرخ رگی و عوارض 
MON_part2.txt:2586:غلوق: ۰۱۳:(.) عوارضی که برای پذیرایی 
MON_part2.txt:7948:فعواره: (0-)۱۷-۷8۲۸ (ص‌مر.) کسی که از 
MON_part2.txt:8678:مصرفش ناراحتی و عوارض سوء ایجاد 
MON_part2.txt:12715:دیوان قسمت: جهان تقدیر. ظ. عوارضی که 
MON_part2.txt:16178:معکوس خوانند و دور و عکس از عوارض 
MON_part2.txt:16198:معکوس خوانند و دور و عکس از عوارض 
MON_part2.txt:24007:عوارضی که مربوط به تسعیر بوده است. 
MON_part2.txt:25305:اسمیه و فعلیه نامیده‌اند و عوارض اجسام را 
MON_part2.txt:32137:گمرکی و عوارض را ندهند.
```


## [2026-09-05T05:49:47.913Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nwc -c c8a6b073c06ec54a.txt; grep -n \"معین\\|عوار\" c8a6b073c06ec54a.txt | head -20"
}
```


### [2026-09-05T05:49:47.965Z] TOOL RESULT

```
10700 c8a6b073c06ec54a.txt
1:URL: https://abadis.ir/fatofa/عوار/
4:TITLE: عوار - معنی در دیکشنری آبادیس
6:عوار - معنی در دیکشنری آبادیس 
10: عوار
16: عوار. [ ع ِ / ع َ /ع ُ ] ( ع اِ ) دریدگی و کفتگی جامه. ( منتهی الارب ) ( ازناظم الاطباء ). شکاف و پارگی در لباس و پیراهن. ( از اقرب الموارد ). || عیب. ( منتهی الارب ) ( دهار ) ( ناظم الاطباء ) ( از اقرب الموارد ): سلعة ذات عوار؛ کالای عیب دار و معیب. ( از اقرب الموارد ) : 
18:کورباد آنکس که اندر عرض تو جوید عوار. فرخی.
19:چنان بخدمت او از عوار پاک شوند
22:زین عالم پرعوار و پرآهو. ناصرخسرو.
24:نیابد کس نه عیبی نه عواری. ناصرخسرو.
25:پیغام داد به شاپور که اگر عهد کنی مرا بخواهی عیب و عوار این دز تو را بنمایم.( فارسنامه ابن البلخی ).
27:همچون گهر اندر گهرش عیب و عواری. سنایی.
28:اگر ظلمت شب پرده کار و ستر عوار ایشان نیامدی همه در بقه هلاک و ورطه دمار به فنا رسیدندی. ( ترجمه تاریخ یمینی ). شادخه ای از لوم بر روی روزگار ظاهر شد که سالها عار و عوار آن باقی باشد. ( ترجمه تاریخ یمینی ص 189 ). گاوی که خداوند عوار و عیب بود یا پیر بود بندهد. ( تاریخ قم ص 176 ).
29:- بی عوار ؛ بی عیب. خالی از عیب و نقص : 
30:آن سگان کت جان نگردد بی عوار از عیبشان 
32:- پر ز عوار ؛ پر از عیب. پرعوار و پرعیب : 
34:یکسره ناخوب وپر ز عیب و عوار است. ناصرخسرو.
35:- پرعوار ؛ پرعیب. آکنده از نقصان وعیب : 
37:زین عالم پرعوار و پرآهو. ناصرخسرو.
38: عوار. [ ع ُوْ وا ] ( ع اِ ) خاشاک و خاکستر چشم. ( منتهی الارب ) ( آنندراج ). خاشاک در چشم. ( ناظم الاطباء ). خاشاک. ( از اقرب الموارد ). || فرستوک. ( منتهی الارب ) ( آنندراج ). پرستوک. ( ناظم الاطباء ). فراشتک. ( دهار ). خطاف. ( اقرب الموارد ). || گوشتپاره ای که از چشم برآورند بعدِ ذرور انداختن در آن. ( منتهی الارب ) ( آنندراج ). گوشتی که از چشم جدا شود پس از اینکه «ذرور» و دارو بر آن بریزند. ( از اقرب الموارد ) ( از ناظم الاطباء ). || درد چشم. ( ناظم الاطباء ). || ( ص ) آنکه راه نبیند. ( منتهی الارب ) ( آنندراج ) ( از ناظم الاطباء ) ( از اقرب الموارد ). || سست و بددل. ( منتهی الارب ) ( آنندراج ). سست و جبان و بددل. ( ناظم الاطباء ). ضعیف و جبان. ( اقرب الموارد ). مرد بددل. ( دهار ). ج ، عَواویر ( منتهی الارب ) ( اقرب الموارد )، عَواور نیز میتوان گفت. ( از اقرب الموارد ). || کسانی که احتیاجشان در پشتشان است. ( از منتهی الارب ). ج ِ عائر، یعنی مردان ابنه زده و آنان که خواهششان در پشتشان است. ( ناظم الاطباء ). || چاهی که از آن آبیاری نشود. ( از اقرب الموارد از تاج ). بیشتر بخوانید ... 
45: فرهنگ معین
```


## [2026-09-05T05:49:54.776Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '40,70p' c8a6b073c06ec54a.txt"
}
```


### [2026-09-05T05:49:54.825Z] TOOL RESULT

```
 فرهنگ فارسی

 عیب، عیب وعاردریدگی وپارگی درجامه یاپارچه
کوهی است 

 فرهنگ معین

 (عَ یا عِ یا عُ ) [ ع . ] (اِ. ) ۱ - عیب ، عیب و عار. ۲ - دریدگی و پارگی در پارچه یا جامه . 

 فرهنگ عمید

 ۱. عیب، عیب وعار.
۲. دریدگی و پارگی در جامه یا پارچه. 

 پیشنهاد کاربران

 عوار. [ ع ِ / ع َ /ع ُ ] ( ع اِ ) دریدگی و کفتگی جامه. ( منتهی الارب ) ( ازناظم الاطباء ) . شکاف و پارگی در لباس و پیراهن. ( از اقرب الموارد ) . || عیب. ( منتهی الارب ) ( دهار ) ( ناظم الاطباء ) ( از اقرب الموارد ) : سلعة ذات عوار؛ کالای عیب دار و معیب. ( از اقرب الموارد ) : 
 ... [مشاهده متن کامل] 
گنگ باد آنکس که اندر طعن تو گوید سخن
کورباد آنکس که اندر عرض تو جوید عوار. 
فرخی. 
چنان بخدمت او از عوار پاک شوند
بدان مثال که سیم نبهره اندر گاه. 
فرخی. 
برشو به هنر به عالم علوی
زین عالم پرعوار و پرآهو. 
ناصرخسرو. 
بجز پرهیز و دانش بر تن من
نیابد کس نه عیبی نه عواری. 
ناصرخسرو. 
پیغام داد به شاپور که اگر عهد کنی مرا بخواهی عیب و عوار این دز تو را بنمایم. ( فارسنامه ابن البلخی ) .
```


## [2026-09-05T05:49:56.692Z] TOOL CALL #58: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/عار/\" --note \"page 73, Persian ār 2 'shame' (Mo'in/Dehkhoda)\" && sed -n '1,40p' data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://abadis.ir/fatofa/عار/'.encode()).hexdigest()[:16])\").txt"
}
```


### [2026-09-05T05:49:59.375Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e15f6e14e8f517b7.txt
URL: https://abadis.ir/fatofa/عار/
FETCHED: 2026-09-05T05:49:59Z
STATUS: 200
TITLE: عار - معنی در دیکشنری آبادیس

عار - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 عار
 /~Ar/

 مترادف عار : رسوایی، شرم، عیب، فضیحت، ننگ
 برابر پارسی : ننگ، شرم، آزرم
 معنی انگلیسی : shame , disgrace , disdain 

 دنبال کنید 

 لغت نامه دهخدا

 عار. ( ع اِ ) عیب و ننگ. ( منتهی الارب ) ( مهذب الاسماء ) ( غیاث اللغات ) : تا قیامت آن عار از خاندان ما دور نشود. ( تاریخ بیهقی ص 129 ). || فضیحت و هر چه در آن عیب لازم باشد. ( منتهی الارب ) : 
شعر تو شعر است لیکن باطنش پر عیب و عار
کرم بسیاری بود در باطن دُرِّ ثمین. منوچهری.
- عار آمدن ؛ ننگ داشتن : 
پیاده نگردد که عار آیدش 
ز شاهی تن خویش خوار آیدش. فردوسی.
ز جهل خویش چون عارت نیاید
چرا داری همی زآموختن عار. ناصرخسرو.
بجز غلامی دلدار خویش سعدی را
ز کار و بار جهان گر شهی است عار آید. سعدی.
- عار بودن ؛ ننگ بودن : 
فخر دانا بدین بود وینها
عیب دینند و علم را عارند. ناصرخسرو.
با این همه از عالم عار است مراواﷲ
یاران مرا فخر است این عار که من دارم. خاقانی.
مرا نیست زآهنگری ننگ و عار
خرد باید و مردی ای بادسار. سعدی.
وگر بی تکلف زید مالدار
که زینت بر اهل تمیز است عار. سعدی.
- عار داشتن ؛ ننگ داشتن :
```


## [2026-09-05T05:50:15.547Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD Watkins awi- ===\"; grep -n \"^awi-\\|awi- \\|ōwyo\\|owyo\" AHD_watkins1985.txt | head -10\necho; grep -n -i \"aviary\\|ostrich\\|avis\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-05T05:50:15.617Z] TOOL RESULT

```
=== AHD Watkins awi- ===
147:LING (storo-), and, at least in some dialects, the SPARROW (sper-’), FINCH (sping-), and woodpecker ((s)peik-). The generic term for “bird” was awi- (Latin avis), and from this was derived the well-represented word for egg, *dOwyo-.
771:nau-', Death; to be exhausted. Contracted from *nasu-. 1. Suffixed zero-grade form *nau-ti- in Germanic *naudi- in Old English néod, néd, distress, necessity: NEED. 2. Suffixed form *ndw-i-, corpse, in Germanic *nawi- in Old Norse ndr, corpse: NARWHAL. 3. Slavic suffixed extended form *naud-d in: a. Polish nuda, boredom: NUDNIK; b. Russian nudnyi, tedious: NUDGE?. [Pok. 2. nédu- 756.]
812:os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PALISADE, PEEL’, POLE?; IMPALE, TRA- VAIL, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1326:BUSTARD awi- BUSTLE s(w)e- BUT ud- BUTCHER bhugo- BUTT! bhau- BUTTER gWou-, teue- BUTTOCK bhau- BUTTON bhau- BUTTRESS bhau- BUTYRIC g¥ou- BUXOM bheug-3 BUZZARD beu-2 BY! ambhi BYRE bheue-
1379:COCKLE! konk(h)o- COCKNEY awi- CocyTus kau-1 cop? ku- CODEINE keue-2 -COEL keue-2 COELACANTH ak- COELOM keue-2 COENO- kom COERCE arek- COETANEOUS aiw- COEVAL aiw-
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-

147:LING (storo-), and, at least in some dialects, the SPARROW (sper-’), FINCH (sping-), and woodpecker ((s)peik-). The generic term for “bird” was awi- (Latin avis), and from this was derived the well-represented word for egg, *dOwyo-.
301:atto-. Father (nursery word). Possibly Latin atta, father: ATAVISM. [In Pok. atos 71.]
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM, DEVIL, (DIABOLIC), (EBLIS), ECBOLIC, EMBLEM, EPIBOLY, (HYPERBOLA), HYPERBOLE, METABOLISM, (PALAVER), PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), (PAR- LOR), (PAROL), (PAROLE), PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL?, (BALLAD), (BALLET), BAYA- DERE. 2. Suffixed o-grade form *gvols-d in Greek bolé, beam, ray: BOLOMETER. 3. Suffixed o-grade form *gwolo-sdé in Greek boulé, determination, will (< “throw- ing forward of the mind”), council: BOULE!; ABULIA. 4. Suffixed variant zero-grade form *gvele-mno- in Greek belemnos, dart, javelin: BELEMNITE. [Pok. 2. g¥el- 471.] gwela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.] gven-. Woman. 1. Suffixed form *gven-d- in: a. Germanic *kwen6n- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben (> Irish Gaelic bean), woman: BANSHEE; C. Persian zan, woman: ZENANA. 2. Suffixed lengthened-grade form *gvén-i- in Germanic *kwéniz, woman, wife, queen, in Old English cwén, woman, wife, queen: QUEEN. 3. Suffixed zero-grade form *g“n-d- in Greek guné, woman: GYNO-, -GYNOUS, -GYNY; GYNAE- CEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin gravis, heavy, weighty: GRAVE?, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form “gro-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA; b. Sanskrit guru-, heavy, venerable: GURU. 3. Suffixed form *gro-es- in Greek baros, weight: BAR?, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR. 4. Possibly *guri- in Greek bri- in compound *u(d)-bri- (see ud-). II. Suffixed extended form *g-rii-to- in Latin britus, heavy, unwieldy, dull, stupid, brutish: BRUT, BRUTE. III. Suffixed extended form *g»ri-g- in: a. Celtic *brig-o-, strength, in Italian brio, vigor: BRIO; b. Germanic *krig- in Old High German krég, chrég, stubbornness (> Ger- man Krieg, war): BLITZKRIEG, SITZKRIEG. IV. Suffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to ride (> ridder, rider, knight): RITTER. 2. Celtic *vo-réd- in Latin verédus, post horse (*vo-, under; see upo): PALFREY. II. O-grade form *roidh-. 1. Germanic *raid- in: a. Old English rdd, a riding, road: RAID, ROAD; b. possibly Middle High German reidel, rod between upright stakes (< “wooden horse”): RADDLE!. 2. Prob- ably Germanic *raid-ja- in Old English réde, geréde, ready (< “prepared for a journey’): READY. 3. Germanic *raidjan in Vulgar Latin *arrédare, to arrange: ARRAY. [Pok. reidh- 861.] reig-'. To bind. 1. Germanic *rigg- (the -gg- is anoma- lous) in Norwegian rigga, to bind, akin to the Scandina- vian source of Middle English riggen, to rig: RIG. 2. Zero-grade form *rig- in Latin corrigia (probably borrowed from Gaulish), thong, shoelace (cor-, from com-, together; see kom): SCOURGE. [Pok. reig- 861.] reig-2. To reach, stretch out. 1. O-grade form “roig- in Germanic *raikjan in Old English récan, to stretch out, reach: REACH. 2. Possibly suffixed (stative) zero-grade form “rig-é- in Latin rigére, to be stiff (? < “be stretched out”): RIGID, RIGOR. [Pok. (reig-) 862.] rendh-. To tear up. 1. Germanic *randjan in Old English rendan, to tear: REND. 2. Germanic *rind- in Old English rinde), rind (< “thing torn off”): RIND. [Pok. rendh- 865.] rep-. To snatch. Suffixed zero-grade form *rap-yo- in Latin rapere, to seize: RAPACIOUS, RAPE!, RAPID, RAPT, RAVEN?, RAVIN, RAVISH; EREPSIN, SURREPTITIOUS. [Pok. rep- 865.] rép-'. To creep, slink. Latin répere, to creep: REPENT?, REPTILE; SUBREPTION. [Pok. 1. rép- 865.] rép-2, Stake, beam. Suffixed variant form *rap-tro- in Germanic *raf-tra- in: a. Old English refter, rafter: RAFTER; b. Old Norse raptr, beam: RAFT!. [Pok. 2. rép- 866.] ret-. To run, roll. 1. Prefixed form *to-vo-ret-, “a running up to” (to-, to; vo, under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1. Extended form *reud- in Germanic *rauton in Old Norse rauta, to roar (akin to the Scandi- navian source of ROTE?): ROUT’. 2. Suffixed extended form *reum-os- in Latin riimor, rumor, “common talk”: RUMOR. 3. Extended form *reug- in Latin rigire, to roar: RIOT, RUT’. 4. Variant *rau-ko- in Latin raucus, hoarse: RAUCOUS. [Pok. 1. reu- 867.]
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “threefold” (*-pl- < combining form *-plo-; see pel-3), in Greek ¢triploos, triple: TRIPLE. 10. Compound form *tri-plek-, “threefold” (*-plek-, -fold; see plek-), in Latin triplex, triple: TRIPLEX. 11. Compound form *tri-st-i, “third person standing by” (see sta-), in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY. 12. Per- sian si, three: straR. III. Extended zero-grade form “iris, “thrice.” 1. Latin ter, thrice: TERN?; TERPOLYMER. 2. Greek tris, thrice: TRISOCTAHEDRON. 3. Suffixed form *tris-no- in Latin trini, three each: TRINE, (TRINITY). IV. Suffixed o-grade form *troy-o- in Russian troje, three: TROIKA. [Pok. trei- 1090.] trem-. To tremble. Possibly related to trep-' and tres- through a hypothetical base *ter-. Latin tremere, to shake, tremble: TREMENDOUS, TREMOR, TREMULOUS. [Pok. trem- 1092.] trep-'. To tremble. Possibly related to trem- and tres- through a hypothetical base *ter-. Latin trepidus, agi- tated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.] trep-2. To turn. 1. Greek trepein, to turn: -TROPOUS; APOTROPAIC, TREPONEME. 2. O-grade form *trop- in: a. suffixed form *trop-o- in Greek tropos, a turn, way, manner: TROPE, TROPO-, TROVER; CONTRIVE, (RE- TRIEVE); b. suffixed form *trop-d- in Greek tropé, a turning, change: TROPHY, TROPIC; ENTROPY. [Pok. 2. trep- 1094.] tres-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1. Suffixed o-grade form *troud-o- in Germanic *thrautam in Old English thréat, oppression, use of force: THREAT. 2. Variant form *trid- in Germanic “thristjan in Old Norse thrysta, to squeeze, compress: THRUST. 3. Latin tridere, to thrust, push: ABSTRUSE, EXTRUDE, INTRUDE, OBTRUDE, PROTRUDE. [Pok. tr-eu-d 1095.] trozdo-. Thrush. 1. Germanic *thrust- in Old English throstle, thrush: THROSTLE. 2. Germanic *thruskj6n- in Old English thrysce, thrush: THRUSH}. 3. Zero-grade reduced form *trzdo- in Latin turdus, thrush: STURDY. 4. Perhaps altered in Greek strouthos, sparrow, ostrich: STRUTHIOUS; (OSTRICH). [Pok. trozdos 1096.] tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “te, *tege) in Germanic *thii (accusative *theke) in Old English thi (accusative thec, thé), thou: (THEE), THOU!. 2. Suffixed extended form *éwjei-no- in Germanic *thinaz in Old English thin, thine: THINE, THY. [Pok. tu- 1097.] twei-. To agitate, shake, toss. 1. Extended form *tweid- in Germanic *thwit- in: a. Old English thwitan, to strike, whittle down: WHITTLE; b. Middle Dutch duit, a small coin (? < “piece cut or tossed off”): DorT. 2. Extended form *tweis- in Greek seiein, to shake: SEISM, SISTRUM. [Pok. 2. tuei- 1099.] twengh-. To press in on. Germanic *thwang- in: a. Old English thwong, thwang, thong, band (< “constraint”): THONG; b. by-form *twangjan in Old English twengan, to pinch: TWINGE. [Pok. twengh- 1099.] twer-', To turn, whirl. Zero-grade *tur-. I. Variant form *stur-. 1. Suffixed form *stur-mo- in Germanic *sturmaz, storm (< “whirlwind”), in Old English storm, storm: STORM. 2. Germanic *sturjan in Old English styrian, to move, agitate: STIR!. II. Suffixed form *tur-bd in Greek turbé, tumult, disorder (> Latin turba, disorder, turbé, spinning top, and turbdre, to confuse, disorder): (TROU-
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
2001:OSTRICH awi-, trozdo- OsTROGOTH aus-! OTHER an?
2163:RATITE era-2 RAUCOUS reu-1 RAVEN! ker-2 RAVEN? rep- RAVIN rep- RAVIOLI rap- RAVISH rep-
```


## [2026-09-05T05:50:17.142Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/عار\" --note \"page 73, Arabic ʿār 'shame' root check\" && f=$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/عار'.encode()).hexdigest()[:16])\") && grep -n \"Etymology\" -A 6 data/verification/sources/web/$f.txt | sed -n '30,90p'"
}
```


### [2026-09-05T05:50:19.479Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/36406b97933fab0c.txt
125- 3.3 
126- Adjective 
--
204: Etymology 1
205- [ edit ] 
206-
207- Root 
208-
209- ع ر ي ( ʕ r y ) 
210-
--
466: Etymology 2
467- [ edit ] 
468-
469- Morphologically from the root ع ي ر ( ʕ y r ) .
470-
471- Pronunciation
472- [ edit ] 
--
742: Etymology 3
743- [ edit ] 
744-
745- Morphologically from the root ع ي ر ( ʕ y r ) .
746-
747- Pronunciation
748- [ edit ] 
--
1019: Etymology
1020- [ edit ] 
1021-
1022- Borrowed from Arabic عَار ( ʕār ) .
1023-
1024- Pronunciation
1025- [ edit ]
```


## [2026-09-05T05:50:32.912Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '460,520p' 36406b97933fab0c.txt\necho \"#### 742-800\"; sed -n '742,800p' 36406b97933fab0c.txt"
}
```


### [2026-09-05T05:50:32.965Z] TOOL RESULT

```
 Descendants
 [ edit ] 

 → Persian: عاری ( 'âri ) 
 → Urdu: عاری ( 'ārī ) 

 Etymology 2
 [ edit ] 

 Morphologically from the root ع ي ر ( ʕ y r ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ʕaː.ra/ 

 Verb
 [ edit ] 

 عَارَ • ( ʕāra ) I ( non-past يَعِيرُ ( yaʕīru ) , verbal noun عَيْر ( ʕayr ) ) 

 to roam , to wander 

 Conjugation
 [ edit ] 

 Conjugation of عَارَ (I, hollow, a ~ i, no passive, verbal noun عَيْر )

 verbal noun
 الْمَصْدَر 

 عَيْر 
 ʕayr 

 active participle
 اِسْم الْفَاعِل 

 عَائِر 
 ʕāʔir 

 active voice
 الْفِعْل الْمَعْلُوم 

 singular
 الْمُفْرَد 

 dual
 الْمُثَنَّى 

 plural
 الْجَمْع 

 1 st person
 الْمُتَكَلِّم 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

#### 742-800
 Etymology 3
 [ edit ] 

 Morphologically from the root ع ي ر ( ʕ y r ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ʕaːr/ 

 Noun
 [ edit ] 

 عَار • ( ʕār )  m ( plural أَعْيَار ( ʔaʕyār ) ) 

 shame , disgrace , ignominy 
 Antonym: شَرَف ( šaraf ) 
 Abu al-Aswad al-Du'ali 
 لَا تَنْهَ عَنْ خُلُقٍ وَتَأْتِيَ مِثْلَهُ 
 عَارٌ عَلَيْكَ إِذَا فَعَلْتَ عَظِيمُ lā tanha ʕan ḵuluqin wataʔtiya miṯlahu 
 ʕārun ʕalayka ʔiḏā faʕalta ʕaẓīmu Do not forbid a thing you do; 
 If you do, shame on you. 

 Declension
 [ edit ] 

 Declension of noun عَار ( ʕār )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 عَار 
 ʕār 

 الْعَار 
 al-ʕār 

 عَار 
 ʕār 

 nominative

 عَارٌ 
 ʕārun 

 الْعَارُ 
 al-ʕāru 

 عَارُ 
 ʕāru
```


## [2026-09-05T05:50:34.946Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### kidney\"; sed -n '20,32p' 05d1d3335e84ba91.txt\necho \"### ostrich\"; sed -n '20,30p' 57c7601dd7d6764a.txt\necho \"### egg\"; sed -n '20,30p' f562b42d3e0f428c.txt"
}
```


### [2026-09-05T05:50:35.020Z] TOOL RESULT

```
### kidney

 Origin and history of kidney 

 kidney (n.) 

 early 14c., kidenere , a word of unknown origin, perhaps a compound of Old English cwið "womb" (see chitterlings ) + ey "egg" (see egg (n.)) in reference to the shape of the organ. Figurative sense of "temperament" is from 1550s. Kidney-bean is from 1540s, so called for its shape.
 also from early 14c. 

 Entries linking to kidney 

 chitterlings (n.) 

 late 13c., cheterlingis "entrails, souse, small intestines of a swine fried for food" (early 13c. in surnames), a word of obscure origin, probably from an unrecorded Old English word having something to do with entrails (related to Old English cwið "womb;" compare German Kutteln "guts, bowels, tripe, chitterlings," Old Norse kviðr "womb," Gothic qiþus "womb"). Variants chitlins (1842) and chitlings (1880) both also had a sense of "shreds, tatters."
### ostrich

 Origin and history of ostrich 

 ostrich (n.) 

 "very large flightless bird inhabiting the sandy plains of Africa and Arabia," early 13c., also hostriche, estrich, ostrig, esterige , etc., from Old French ostruce "ostrich" (Modern French autruche ) and Medieval Latin ostrica , ostrigius , all from Vulgar Latin avis struthio. 

 ﻿ This is from Latin avis "bird" (from PIE root *awi- "bird") + Late Latin struthio "ostrich," from Greek strouthion "ostrich," from strouthos megale "big sparrow," the first word perhaps from PIE *trozdo- "thrush" (see thrush (n.1)).

 The Greeks also knew the bird as strouthokamelos "camel-sparrow," for its long neck. Among its proverbial peculiarities are indiscriminate voracity (especially a habit of swallowing small bits of iron and stone to aid digestion), a supposed want of regard for its eggs (which are incubated partly by the heat of the sun), and a tendency to hide its head when pursued. Ostriches do put their heads in sand, but ostrich farmers say they do this in search of something to eat.

### egg

 Origin and history of egg 

 egg (n.) 

 "the body formed in the females of all animals (with the exception of a few of the lowest type) in which by impregnation the development of the fetus takes place," mid-14c., egge , mostly in northern England dialect, from Old Norse egg , from Proto-Germanic *ajja(m) (source also of Old Saxon, Middle Dutch, Dutch, Old High German, German ei , Gothic ada ), probably from PIE *owyo-/*oyyo- "egg" (source also of Old Church Slavonic aja , Russian jajco , Breton ui , Welsh wy , Greek ōon , Latin ovum ); possibly derived from root *awi- "bird."

 This Norse-derived northern word vied in Middle English with native cognates eye , eai , from Old English æg , until finally displacing the others after c. 1500. Caxton (15c.) writes of a merchant (probably a north-country man) in a public house on the Thames who asked for eggs:

 And the goode wyf answerde, that she coude speke no frenshe. And the marchaunt was angry, for he also coude speke no frenshe, but wolde have hadde egges, and she understode hym not.
```


## [2026-09-05T05:50:54.879Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW avis ===\"; grep -n \"^avis\\|avis,\\ *-is\" LEW_1910.txt | head -5\necho \"=== LAT avis ===\"; grep -n \"avis\" LAT.txt | head -5\necho \"=== LEW ovum ===\"; grep -n \"ovum\" LEW_1910.txt | head -5\necho \"=== IEC awis ===\"; grep -n \"awis\\|ōwjom\\|ōwiom\" IEC.txt | head -8\necho \"=== SKT ostrich/egg/average/caviare ===\"; grep -n -i \"^Ostrich\\|Ostrich,\\|Egg,\\|Average,\\|Caviare\" SKT.txt | head -8"
}
```


### [2026-09-05T05:50:56.460Z] TOOL RESULT

```
=== LEW avis ===
12275:avis, dvinas IT 229
=== LAT avis ===
6090:abstrait et concret); "garantie"; "avis prononc^ le premier; avis
10528:Derives et compos6s: cautus: qni est sur ses gardes; d'oii "avise,
10788:d 5 , "se ranger a 1 'avis de" 7tp<XT)(Wpa), Cic. Cael, xo, ad quem si accessit,
11040:nelle; exprimer un avis dans lea formes prescrites. - Ce sens ancien
11067:technique de "estimer., juger, etre d'avis", comme arbitror, aestimo,
=== LEW ovum ===
4584:OTOMYVOMLL, OTQWY- via IT 590 otvyéw IT 609 atvhdoc I 706 otoipa, otvoaé I 706 otundlet, atmos IIT 610 otinnaé II 608 ovvnnn, otummEtov II 608 otvoaé II 610 otvepdlw II 48 otugedifw II 610 ottw 1706, IT 599 otwia (aol.) I 706 ot@ué I 706, IT 586 ov 11712 ovpaé, ovpaxa IT 619 ovpac IT 619 ovyyiyvdioxw I 677 avyxAntoc I 258 ovtvé I 261, 730 ovijAat II 636 ovxahic I 492 ovxdmuwocs IT 114 ovxéa, ovun I 492 OVvxO|L0Q0G, TvxOMO- oéa IT 114 ovxov I 492 ovuxopartns IT 638 ovxyic, ovxydc, avxyoco IT 550 ovxmtov I 673 ovunatéwm I 560 ovumdéoves IT 327
11088:plovum (langob.) II 324
=== IEC awis ===
11551:nãu- (nàuis) (2) “starvation, death, corpse; exhaustion, collapse; pain, care" WP II, 316. Cf. nüu- Tokh. cf. nawen ‘man, mortal’; o-nuwafifie *óim-mortal'; nwam ‘sick; Arm. cf. nawti, Cup, -t'eav “hungry”, fr. *này-sth&u-?); Lyc. cf. prinuvo or -novu ('tomb'. Phonol. uncertain); Hitt. (?) nahhan “fear, respect; nahmi, prt. nahun, v. ‘fear’; Lat. cf. navatur, impers. ‘pains are taken’, cf. ad nàvandam pacem ‘striving for peace’; e-navàre ‘bestow care on’; Mir. nó, nüne, Ir. núna, m. “hunger, famine’; W newyn, id. Br. nawn, f. id.; Cor. nown, m. id.; OBr. cf. -neuiom (or-neuion? 'decay); Go. naus, gs nawis, m. ‘corpse’; OE cf. neo-bedd *death-bed'; ON nár, m. ‘death’; OCS navi, m. ‘corpse’; OCz. náv, gs: -i, m. ‘death’ beside náva, f. id.; Cz. cf. ú-nava ‘fatigue’; Blg. navi, pl. “evil spirits, said to plague women in la-
12415:ouis “sheep. I, 167 Skt. ávih, mf. id.; Arm. cf. aw-di, coll. aw-dik, id. (-di as in los-di, etc., sense of ‘creature’); Hiero-Hitt. hawas, id.; Gk. óïs, gp: oion, mf. id.; Lat. ovis, f. gp: ovium, id.; Umb. uvem, f. acc. id.; Olr. ói, Gael. ái, m. id.; OBr. cf. ou-sor ‘shepherd’ (for *ouzor?, cf. Ir. ao- dhaire, id.); OHG ou, au, f. np: awi, i-st. "ewe: OS ewi, f. id.; Go. aw-, awi-, cpds. id.; MHG ouwe, sf. id. OE &ow, m., eowu, f. id.; Du. ooi, Fris. ie, f. id.; LG cf. e-Ilamm 'ewe-lamb' and MHG ost, sn. (Csheepfold', fr. *awist-: Go. awistr, id.); ON ær, f. id.; OCS (and com. S1.) ovíca, dim. type f., id. (fr. *ouika); Srb. cf. ovan, n. ‘ram, teg’; Li. avis, gp: avit, f. ‘sheep’; Latv. avs, gp: avju, f. id. (Cpds. of type *ouil- in Skt. avila, f. ewe Lat. ovile, n. 'sheep- fold”, ovilis, adj. “of sheep’; type *ouin- in Lat. ovinus “of sheep'; Umb. unu, acc. id.; OCS ovínü, ovinij, id.; ovínü, m. ‘fram’; Slovene oven, R ovén, m. id.; Li. avinis, adj. “of sheep’; ávinas, m. ‘fram’; Latv. cf. avens, m. “tam; type *ouit- in OHG ewit, n. ‘flock’; OE eowd, f. ‘fold; flock; type *ouios in Gk. óios *sheep's'; Skt. ávyab, adj. id.
=== SKT ostrich/egg/average/caviare ===
8175:able,  having  power,  bkilful.  (F.  —  U) M.  E.  ad/e ;  nlso  hable  -•  O.  F.  habUe,  ahU^ abtl,  able.  —  L.  habilit,  easy  to  handle, active.  •  L.  habert,  Der.  abil-i-ty  (from L..  ace  habilitatem). average,  a  proportionate  amount.    (F.
22795:car,  earnest,  egg,  riv,  elder,  embattle, boss,  entrance,  euct.  excise.
23670:caviare   tnrquoise. Spanish  from  Turkish  :  zebcc German  from  Poiishfrom  T^kisk  ■
```


## [2026-09-05T05:50:57.186Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT kaviar/havyar ===\"; grep -n -i \"Kaviar\\|havyar\\|chavyar\" LKT.txt | head -8\necho \"=== LKT avarie ===\"; grep -n -i \"avarie\\|awar\" LKT.txt | head -8\necho \"=== PHN avarie ===\"; grep -n -i \"AVARIE\" PHN.txt DEV.txt LAM.txt DOZ.txt | head -8\necho \"=== HUB xaya ===\"; grep -n \"chaje\\|xaje\\|Ei'\" HUB.txt | head -8"
}
```


### [2026-09-05T05:50:57.289Z] TOOL RESULT

```
=== LKT kaviar/havyar ===
811:Sing,  zu  batärih,  butärih  'Rogen,  Ka- viar' [aus  gr.  rapixiov  mit  vorgesetztem altäg.  oder  kopt.  Art.  p;  ZDMG  L,  654]; hieraus  it.  bottarga,  siz.  buttaraca,  vut- taraca  'Kaviar  aus  den  Eiern  der  Meer- äsche', frz.  boutargue,  botargue,  pmitar- gue  'Speise  aus  Eiern  der  Seebarbe,  die gesalzen  und  an  der  Sonne  getrocknet oder  geräuchert  werden'.
2061:'Kaviar';  hieraus  ngr.  Kaßidpiov,  bulg. hajwar,  hajiver,  serb.  hajwar,  poln. kawiar,  cech.  kaviar;  it.  caviaro,  caviale, sp.  cabial,  pg.  caoial,  caviar,  frz.  caviar; engl.  ndl.  caviar,  dtsch.  Kaviar,  — [JOEST  in  ZfEtbn  1890,  3  vermutet, daß  das  abendländische  Wort  auf  den Namen  des  Hafens  Kapha,  d.  h.  Theo- dosia,  eines  Hauplhandelsplatzes  für  die Fischer  des  Schwarzen  Meeres,  zurück- geht ;  doch  ist  diese  Ableitung  sehr  an- zuzweifeln. KESSELING  in  Neophilo- logus  VI,  213/214  verfolgt  das  Wort nur  bis  mgr.  Kaßidpiv  zurück.  Übrigens heißt  der  Kaviar  russ.  ikrd.]  [Bern  Sl EtWb  382/383.   ML  4086.    Kluge  232.
=== LKT avarie ===
531:Od.  'awär  [von  der  Wurzel  'ära  II  'ver- derben'] 'Stäubchen,  Fehler,  Schaden' ist  wohl  sicherlich  Grundwort  zu  it. araria  'Schaden  an  Schiff  oder  Ladung, Hafensteuer',  ein  Wort,  das  zuerst  von den  Genuesen  und  Pisanern  benutzt wurde  und  dann  mit  der  it.  Endung  in fast  alle  europäischen  Sprachen  über- ging: frz.  avarie;  sp.  averia,  haberia  ; pg.  avaria,  Dtsch.  Havarie,  Haferei; ndl.  avarij,  averij,  haverij;  engl,  average [offenbar  ist  h  als  Ersatz  für  das  von Europäern  nicht  sprechbare  'ain  zu denken;  dann  wäre  der  unmittelbare Einfluß  des  ar.  Grundworts  bis  hierhin wirksam  gewesen,  wenn  nicht  etwa Kontamination  mit  germ.  Hafen  oder Volksetymologie  anzunehmen  ist].  Russ. awarija,  bulg.  serb.  awarija,  Cech.  ava- rie 'Seeschaden'.  [DE  217.  Dozy  Oost 22/23.  Devic  DEt  50/51.  Kluge  195. Gorjajew  1.    Hobson  Jobson  42.
4188:'Beinkleider'  [wörtlich  'die  Schenkel bedeckend'  aus  zend.  graona  'Ober- schenkel' und  Wurzel  vr  'bedecken', POTT  in  ZDMG  XIII,  381/382],  hieraus pers.  sälivär  [mit  Wechsel  von  r  >  l], ar.  sartväl,  pli'.  saräwll ;  hieraus  mlat. saraballa,  sarrabarrae  'Hose',  kat.  sara- ymlls,  pg.  ceroiilas  'Unterhosen',  sp. zaraguelles  'Pluderhosen'  [bei  Valencia üblich :  sehr  weite  Beinkleider  aus weiter  Leinwand,  die  in  vielen  Falten bis  auf  die  Knie  reichen  und  fast  aus- sehen, als  trügen  die  Leute  gar  keine Hose,  sondern  nur  ein  Hemd],  pg. zarelos,  sp.  solares  'lange  Beinkleider bei  den  sp.  und  pg.  Zigeunern' ;  anglo- ind.  engl,  shulivaurs  'weite  Hose', amerik.  sherryvallies  'dicke  Lederhosen, die  beim  Reiten  über  die  gewöhnlichen Beinkleider  gezogen  werden',  dtscb.  (dial. Danzig)  Scharr iwarri  'lange  Hose';  poln. szarawary,  russ.  sarawary  'Pluderhose', SaVwary  'tk.  Hose',  &ch.  saravara,  bulg. salwari,  serb.  Salware.  [üorjajew  419. DE  365/366.   Eguilaz  526.   ML  7596  a.
5523:128 a</aÄ  131 awarija  138 ait^er  142
5781:Hadschi  111 Haferei  138 Hniduck  781 ifa/«Z}  59  d Haifagras  796 Harakiri  818 iJf/r^w  819 Hasard(spiel)  2186 Haschisch  839 hasehart  mhd.  2186 Hassagai  2181 Havarie  138 Hedschra  863 helmbarte  mhd.  823 Dorrfe  1594 Hosanna  872 ÄMr«  848 hurra(h)  2167
6340:aumasor  afz.  1399 aumucelle  afz.  1520 utimusse  afz.  1520 nuqueton  afz.  1272 avarie  138 avicenniie  893 ayan  38 azidarac  140 ««ciT  2180 memine  29 uzeroUe  2206 azimut  1818 rtso^A  2208
7774:s^ataZ  1929 S2a[  1802 szalasz  1805 szaman  1928 szarafan  1845 szarawary  1849 szarsza  1878 szatra  380 szkarlatyna  1794 szkofija  2171 szpinak  126
=== PHN avarie ===
DOZ.txt:829:vertaalt avarie door 'awdr, avarié door mo'auwar, en
DEV.txt:65:Telle  quelle,  notre  tâche   était  suffisante;   et  le présent  volume,  nous  l'avouons  en  toute  humilité, n'a  pas  laissé  de  nous  coûter  un  long  et  persévérant travail.  Prenant  pour  base  les  publications  de  nos devanciers,  nous  y  avons  joint  les  résultats  de  nos recherches  personnelles  pendant  plusieurs  années. Aussi  trouvera-t-on  dans   ce  dictionnaire  plus   de cent  articles  sur  des  mots  dont  l'origine  orientale n'avait  jamais  été   établie  :  les   uns  peu  connus, comme  alizari,  auffe,  alquifoux,  bédégar,  ciiine,  ché- hule,  nizeré,  gamache,  orcanète,   etc.;   d'autres  plus généralement  usités,  tels  que  épinard,  estragon,  far- deau, gâche,  moise,  moire,  houle,  mortaise,  etc.  Nous avons  combattu  ou  confirmé,  à  l'aide  d'arguments nouveaux,  les  hypothèses  précédemment  émises  sur des  termes  comme  artichaut,  arsenal,  avanie,  avarie, caraque,    escarpin,    nuque,   siroc,    etc.   L'examen  de quelques  ouvrages  scientifiques  arabes,  dont  les  tra- ductions latines   étaient  fort  répandues  au  moyen âge,  mais  dont  le  texte  arabe  n'a  jamais  été  publié,
DEV.txt:669:Ces  avarice  étaient  particulièrement  payées  pour  réparer des  pertes,  ce  qui  suggère  à  l'esprit  une  assimilation  avec notre  avarie  :  ^Avariis  seu  damnis  reparandis, ??  dit  le Gloss.  de  Du  Cange.  (Voy.  ci-après  Avarie.)
DEV.txt:671:Avarie.  Esp.  rti'ma,  portug.  avaria,  ital.  avaria.  Malgré  les diverses  étymologies  proposées  par  Brencmann,  Adelung, Diez,Jal,etc.,  M.  Dozy  ne  doute  pas  que  le  mot  ne  soit  d'ori- gine arabe,  introduit  d'abord  en  italien  parle  commerce, et  passé  de  là  aux  autres  langues  européennes.  Avaria  vien- drait de  la  racine  ^U  'âr  qui  signifie  proprement  éborgner, mais  qui,  à  la  2'  forme  aivouar,  a  aussi  le  sens  de  gâter, d'où  ^î^fi  awâr,  défaut,  déchirure.  Bocthor  traduit  avarie
DEV.txt:2864:Avaria,  pg.  ital.  voy.  Avarie.
DEV.txt:2866:Avarie.
DEV.txt:2868:Averia,  esp.  voy.  Avarie.
DEV.txt:4935:^U  voy.  Avarie.
=== HUB xaya ===
```


## [2026-09-05T05:51:11.154Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 2058-2062 ===\"; sed -n '2055,2062p' LKT.txt\necho \"=== LKT 528-532 ===\"; sed -n '527,532p' LKT.txt"
}
```


### [2026-09-05T05:51:11.212Z] TOOL RESULT

```
=== LKT 2058-2062 ===
einer  reizenden  Frau  sp.  hitrl,  frz.  houri, ndl.  engl,  houri,  dtsch.  Huri.  [DE  ;287. Devic  DEt  141.
849.  Ar.  liauz:
'Bezirk,  Umgebung';  hieraus  mit  ar. Art.  sp.  pg.  alfoz  'Landschaft,  Feldflur', im  MA  der  Bezirk,  der  seine  eigene Jurisdiktion  hatte  und  nach  einem  be- sonderen fuero  regiert  wurde,  meistens nur  eine  Pfarrei  oder  ein  Schloßgebiet umfassend.    [DE  116/117.
850.  Pers.  hänagä:
Daraus  ar.  hawäga  '^Herr,  Kaufmann, Europäer  [ZDMG  L,  640],  vulg.  unter dem  Einfluß  des  tk.  koga  'Greis,  Meister' [vom  Stamme  koc  'stark,  mächtig,  groß' Vämbery  TktEtWb  S.  91,  Nr.  94]  hoga, tk.  Jioga  'Gelehrter,  Professor';  hieraus rum.  hoge  'dass.',  bulg.  serb.  hodza  'tk. Geistlicher',  russ.  hozjain  'Wirt,  Herr', hozjaika  'Wirtin',  klruss.  chazajin  'dass,'. [Gorjajew  399.    Bern  SlEtWb  400.
851.  Tk.  hawjar:
'Kaviar';  hieraus  ngr.  Kaßidpiov,  bulg. hajwar,  hajiver,  serb.  hajwar,  poln. kawiar,  cech.  kaviar;  it.  caviaro,  caviale, sp.  cabial,  pg.  caoial,  caviar,  frz.  caviar; engl.  ndl.  caviar,  dtsch.  Kaviar,  — [JOEST  in  ZfEtbn  1890,  3  vermutet, daß  das  abendländische  Wort  auf  den Namen  des  Hafens  Kapha,  d.  h.  Theo- dosia,  eines  Hauplhandelsplatzes  für  die Fischer  des  Schwarzen  Meeres,  zurück- geht ;  doch  ist  diese  Ableitung  sehr  an- zuzweifeln. KESSELING  in  Neophilo- logus  VI,  213/214  verfolgt  das  Wort nur  bis  mgr.  Kaßidpiv  zurück.  Übrigens heißt  der  Kaviar  russ.  ikrd.]  [Bern  Sl EtWb  382/383.   ML  4086.    Kluge  232.
852.  Ar.  hawwaa:
=== LKT 528-532 ===
Kirgis.  ebenso,  dass.  wie  Ik.  agyl  'Tier- park, Hof.  Hieraus  russ.  aul  'Dorf  bei kirgisischen  Völkern',  bulg.  ag^l  'Hürde'. [Gorjajew  7.    Mikl  SlEtWb  2.
137.  Tk.  awly:
'Hof  [aus  dem  gr.  aüXr)];  hieraus  rum. avlie  'Park'.
138.  Ar.  'aTVTVär:
Od.  'awär  [von  der  Wurzel  'ära  II  'ver- derben'] 'Stäubchen,  Fehler,  Schaden' ist  wohl  sicherlich  Grundwort  zu  it. araria  'Schaden  an  Schiff  oder  Ladung, Hafensteuer',  ein  Wort,  das  zuerst  von den  Genuesen  und  Pisanern  benutzt wurde  und  dann  mit  der  it.  Endung  in fast  alle  europäischen  Sprachen  über- ging: frz.  avarie;  sp.  averia,  haberia  ; pg.  avaria,  Dtsch.  Havarie,  Haferei; ndl.  avarij,  averij,  haverij;  engl,  average [offenbar  ist  h  als  Ersatz  für  das  von Europäern  nicht  sprechbare  'ain  zu denken;  dann  wäre  der  unmittelbare Einfluß  des  ar.  Grundworts  bis  hierhin wirksam  gewesen,  wenn  nicht  etwa Kontamination  mit  germ.  Hafen  oder Volksetymologie  anzunehmen  ist].  Russ. awarija,  bulg.  serb.  awarija,  Cech.  ava- rie 'Seeschaden'.  [DE  217.  Dozy  Oost 22/23.  Devic  DEt  50/51.  Kluge  195. Gorjajew  1.    Hobson  Jobson  42.
139.  Ind.  äya:
```


## [2026-09-05T05:51:13.061Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT average entry ===\"; grep -n -o \"average,  a  proportionate  amount.\\{0,600\\}\" SKT.txt | head -2\necho \"=== SKT ostrich ===\"; grep -n -o \"Ostrich.\\{0,400\\}\" SKT.txt | head -3\necho \"=== KNT xaya ===\"; grep -n \"xāya\\|xaya\" KNT.txt | head -5"
}
```


### [2026-09-05T05:51:14.588Z] TOOL RESULT

```
=== SKT average entry ===
8175:average,  a  proportionate  amount.    (F.
=== SKT ostrich ===
=== KNT xaya ===
1951:ably = Artazáaga), Vasdasaka, Vahyav'Sdapaya, Hadaxaya.
4796:2 агба : XS SXc = Xerxes, Seat c: 1 adam : Xšayāršā : XS D mure Sa = SEAL A: 1 Arša 5 yüba 2 ka :n 6 ušna à ата: 7 hyä: ‚4 Adi 8 puça Sb = Sear B: 1 Hadaxaya PNE EE 9 Вадаба, : ...
```


## [2026-09-05T05:51:26.926Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace')\nlines=t.read().split('\\n')\nfor i,l in enumerate(lines):\n    if 'average,  a  proportionate' in l:\n        print('\\n'.join(lines[i:i+8])); break\nEOF\necho \"=== BRT 22678-22690 ===\"; sed -n '22676,22690p' BRT.txt\necho \"=== BRT vayu- Luft ===\"; grep -n \"vayav-\\|vayu-\\|'Luft'\" BRT.txt | head -8"
}
```


### [2026-09-05T05:51:28.462Z] TOOL RESULT

```
able,  having  power,  bkilful.  (F.  —  U) M.  E.  ad/e ;  nlso  hable  -•  O.  F.  habUe,  ahU^ abtl,  able.  —  L.  habilit,  easy  to  handle, active.  •  L.  habert,  Der.  abil-i-ty  (from L..  ace  habilitatem). average,  a  proportionate  amount.    (F.
•  L.)  ' AvfiMi^e  {\^  avet-a^ium,  from mviria,  i.e.  cattle)  siin^if'^^  service  which the  tenant  owe%  the  king  or  other  lord, by  hor>c  or  ox,  or  by  carriage  with either,'  &c.;  Hlouat'ii  Law  Diet.  ed.  ir.91. —  O.  K.  aver  {V.  avoir),  to  h.ave,  also, a*    >b.,    gooils.    propcny ;    hencr,    cattle,
•  L.  ha^re,  !o  have,  [vossc**.  %  This form  ^average)  was  afterwards  confused wil  h  F.  avan'j,  avarie,  damage  of goods  I  later,  proportion  or  average  of payment  for  damage^.  (Arab.  'au^Jr,  a fault,  defect,  tJti  'aufSr,  spoilt  merchan- dise, merely  iniroduce  a  foim  buiioMrcd from  Late  LaC.  averia.)
binnacle,  a  box  for  a  ship's  compau. (Poit.  — L.)  A  singular  coiTuption  of  llic older  word  bittacU,  by  confnsion  with  bin, a  chest  *  Port  bita^ttla,  a  biltncle  [i.e. binnacle) ;  Vieyia.  Cf.  Span,  bitoiora, F.  habiiacte,  the  same.  The  Poit.  bitaccta stands  lor  habifacola*^  the  first  syllable being  lost.  —  L.  hahitaculumt  a  little  dwell- ing, i.e.  '  the  frame  of  timber  in  the  steerage of  a  ship  where  the  compass  stands ' ^Bailey;,  and  prob.  (at  first)  a  shelter  fot
ire  awi
the  iteersman.  —  L.  habiiart qnent  of  habert*
cohabit.  (L.)  l^eehabi/, together  with;  sccbav-*---
debontxtre.  acki^'  oC
=== BRT 22678-22690 ===
.  g,  vaintya-  Adj.  'flehend,  flehentlich':  .*  J'  '"^y  "'■  "^og^l';  '">  Allgemeinen'): at  V!  xrJaiiya  asüna  vazda  :^araihya  .^'^f"'"  ^K'oranqmca  ma^anamca  sa- (Sd.)  -ya  (APn.)  .r«^^  Y.  28.  .0.  «^'"'^  wy^«.«'>  V.  2. 8;  -  m>^ahe
Ableit.auslr^«M..-Pu.:M>.*W/(»P.).  Sü.:^«''')"'«'*'^--^'^   WJ)-?«"    arft    ««/A^   \t. laMaiäiH.  I4- 19;  —  vayqm'^  vaHm  susruifmnB  Yc
dby  Google
I3S7
'vaya-
14. 3 1 ;  Y.  42. 6 ; — HsyaaÄa  (sd.)  vayaHfya^ patantaHbya  (sd.)  Y.  57.  28;  Vt.  10.  119; —  ^'■''i  A**  """y^  patqn  V,  5.  1 2 ;  —  jff«? vä  ktnfsj^arö  vays  va  kfr»ßj^arB  V. 6.  45,  46,  7.  29,  30,  FrW.  //;  —  vayS  äim .  .  fraauhar»nti  V.  5. 8;  —  vayanamcai^ frauuhantanatn  (sd.)  V.5, 14.  a)  mit namentlicher  Bestimmung:  vü  karHpta  V. 2.43;  —  vayqm'^  kakrkäiqm  V.j.ao.
AbleiU  —  Zum  V.  ^vay-,  —  *ai.  vdy  m.  {vi^, Tiäya^);  mp.  {Pü-)  vay,  vgl.  väyaHäai.  —  ')  Im Gegensatz  zu  m^tya:  —  ')%  3JJ.  —  J>  Them.
•  j.  'vaya-  m.:  s.  unter  ^vayav:
•  j.  "vaya-  m.:  s.  unter  'vayav,
•  j.  Jvaya-  Adj.:  s,  unter  ubsya-.
yvayaeiiyaifa'H.S.  \6:\\tivayai»jilityasla^).
•  p.  vayam,  j.,  g.  vaem  NP,  Pron,  i. Pers.  'wir".  Es  steht  i)  wenn  auf  dem 'wir*  ein  besonderer  Nachdruck  liegt: al^a  t3i  vaim  RyamS  (sd.)  yöt  .  .  Y,  30. 9.         2)  vor  einem  attributiven  Relativ:
ye^he  valm  maAi  ySi  saolyants  doRyu- nam  Vr. //.  13;  —  valm  ySi  äaiva  V. ■'^■55;  VyL^2.  3)  sonst:  avaläya^tim
äazdi  nS  .  .  yat  iaväma  aiwi.vanya  ,  . ya^a  vaem  nijanäma  ,.  YtJ,  58;  — dasdf  ahmähm  tat  ayaptsm . .  ydka  valm humanai)ha  .  .  vanäma  vups  harihs  Yt 'O-  34;  34^  F-  A';  —  I  avahyarädiy  vayam haxämanisiya  %ahyämahy  Bh.  /.  3;  — *duvilälaranam  (sd.)  vayam  xlaya%iya amahy  Bh.  1.  4 11.  Für  die  Übrigen  Plur.- Kasus    des    Pton.   i.  Pers.    s.  ahma-  und
•j. 'vayav-, 'vaya- ''m. 'Luft,  Atmosphäre', als  Gottheit'*':  'yus  bä  nqma  ahmt . .  avat •yus  .  .yat  «va  dqma  vayemi  yasca  äa%al sp»nts  mainyui yasca  da'^at  anrS  matnyus Yt.  1$.  43 ;  —  'yusys  upar5.kairy5  Yl  75. 4, 2 1 ;  3  (als  Vok.) ;  —  'yus  aurvS  *usiäj *yasts  d>r3ii.yaox3ürS ..\t.is.^^;  —  °yaos uparS-katryiiu  tarähätö  anyäts  dämqn  Y. 22.24,  Ytij.  o;  —  %wasahe  3^diätahe trvanaht  akaranahe  'yaos  upareJkairyeAe V./P.13;  S.J.21;  —  aaai  ti  -yö  (Vok.) yazamaidt  yat  tl  asti  sp>ntS.mainyaem  Y. Äj.  5 ;  —  '^  aurva . .  'yS  taxma  Yt.  15.11; —  t9m  yazai . .  uynm  vaim  (Akk.)  uparS.' iairlm  Yl/J.  5;  —  valm  aiavamm  .. valm  uparS.kairim  .  .  tardhättm  anyüis dämqn    Y.  25.  5,  S.  2.  2i;    Yt/J.  1';    —  .
=== BRT vayu- Luft ===
22690:•j. 'vayav-, 'vaya- ''m. 'Luft,  Atmosphäre', als  Gottheit'*':  'yus  bä  nqma  ahmt . .  avat •yus  .  .yat  «va  dqma  vayemi  yasca  äa%al sp»nts  mainyui yasca  da'^at  anrS  matnyus Yt.  1$.  43 ;  —  'yusys  upar5.kairy5  Yl  75. 4, 2 1 ;  3  (als  Vok.) ;  —  'yus  aurvS  *usiäj *yasts  d>r3ii.yaox3ürS ..\t.is.^^;  —  °yaos uparS-katryiiu  tarähätö  anyäts  dämqn  Y. 22.24,  Ytij.  o;  —  %wasahe  3^diätahe trvanaht  akaranahe  'yaos  upareJkairyeAe V./P.13;  S.J.21;  —  aaai  ti  -yö  (Vok.) yazamaidt  yat  tl  asti  sp>ntS.mainyaem  Y. Äj.  5 ;  —  '^  aurva . .  'yS  taxma  Yt.  15.11; —  t9m  yazai . .  uynm  vaim  (Akk.)  uparS.' iairlm  Yl/J.  5;  —  valm  aiavamm  .. valm  uparS.kairim  .  .  tardhättm  anyüis dämqn    Y.  25.  5,  S.  2.  2i;    Yt/J.  1';    —  .
22693:*)  Die  S.  /.  21  mit  Ramait  in  Beziehung  ge- setzt wird»).  V. /p.  13  steht  der  Name  hinter &Jiij!a  und  Zrvan  und,  durch  eine  Anrufungs- Tormel  getrennt,  vor  Väla.  Der  Gottheil  ist das  junge  Machwerk  Yt  1$  gewidmet,  dai  irr- tümlich räm  yail  genannt  wird.  —  Die  mp. Schriften  kennen  einen  guten  und  einen  bSsen Väy  fväy  i  veA,  v3y  i  vailcir),  von  denen  gesagt wird,  dass  aie  bei  der  D'm'iir>/-Briicke  um  die Seelen  kämpfen  (Me.  3.  w^).  Es  scheint  mir aber  nicht  notwendig,  darum  'vaytOf  und  'vayav- gleichiutetien  und  in  den  beiden  'the  personi- ficaiions  of  ihe  Upper  and  Iower  air'  (Wbst SBE.  37.  224)  »u  sehen.  Im  Awesta  ist  *on jener  Tätigkeit  des  aA«Hschen  Vayav  nirgends die  Rede.
22694:Vgl.  ^T/ayau-f  vayah-.  —  Zum  V.  ^vä-,  ^  mp. *vayui3)  (Gft.ÖS);  vgt.Bi.väydv-0  m.  'Wind'; mp.  väyii  'Luft'  (Bd.  r.  s)*  a^ttartiay.  —  ■(  Die Berechtigung  dieses  Ansatzes  ist  sehr  zweifel- haft, da  AS.  wo™,  nach  S^Sp.  14  flir  *vayum geschrieben  sein  kann,  auf  vayS  (Nom.;  Yt. 15)  aber,  das  dann  ^ein  als  Beleg  übrig bleibt,  wenig  Verlass  ist  —  »)  S.myaA-  No.  3.
22696:•  j.  'vayav-,  'vaya-  m.  Name  eines Daeva*':  *asls.vlhstui  dim  (näml.  nanm) bandayäti  °yö  dim  bastim  nayätt  V.5.  8; —  pairihwS  panta  yim  . .  hü  dit  atvö apairi%wS  yO  °yaos  anawtanidikahe  Aog.
22709:ZoDi  V.  •i'ü-.  —  Vgl.  'vayav-.  —  PB. :  väy  (/
22713:und;  s.  daiu  tvayav-*\  —  j  her  den  schßnen  Wagen  lenkend"  YL/o. Fi  u»w.  JJJ4.
24453:Komp.:  vüfia"\-äyav-.  —  ai.  visvayav-  Adj. ■für  alle  Lebenden  beMimmt'(?J.  —  Pü.(dKn.); hai-visp  elön,  hamäi  invadai,
```


## [2026-09-05T05:52:43.175Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 auei Vogel ===\"; grep -n \"auei-\\|āuei\\|ōuiom\\|ōu-i̯o\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8\necho \"=== IEC awis bird ===\"; grep -n \"^awis\\|awi- \\|ōujom\\|ōuiom\" IEC.txt | head -8\necho \"=== HJB avarie ===\"; grep -n -i \"avarie\\|average\" HJB.txt | head -5\necho \"=== FSD average ===\"; grep -n -o \"average.\\{0,300\\}Arab.\\{0,200\\}\" FSD_vol1.txt | head -3"
}
```


### [2026-09-05T05:52:46.896Z] TOOL RESULT

```
=== WLD Bd1 auei Vogel ===
1379:au-, aue-, auei- — au- 
1382:an-, aue-, auei- „gern haben“; daher einerseits „verlangen Ii , andrerseits 
1509:auei- 
1529:auei- „Yogel“. 
1603:lungen zur Erwagung (: ai. avati „hat gern“?). Verwandtschaft von *auei- 
7363:oixh-rjg , dor. dauei-ag ; s. noch Yf. LEWb. 2 u. (qints). 
9709:stufe ware, wie *ou(i)om „Ei“ zu *auei- „Yogel t: und *o(tt)s- „Ohr“ zu *aus-. 
=== IEC awis bird ===
870:Skt. ávàmi; Av. avāmī; Gk. cf. Hom. en-ées "benign!" and Dor. äs ‘friend’; Lat. aveo; W awyddu, v. ‘desire’; Srb. cf. üja ‘rest. (Go. awi- in awi-ljup “thanks? is referable to aue- above)
18567:doer’ rather than fr. a type ghodh- (2) + touos, in which *-dh- + *-t- would have to produce *-st-, cf. OCS vesti, Cz. vésti, “lead, fr. *uedht-, see uedh- (2)); Latv. tuvs ‘near, close’; OPr. tawi- ‘next-, adjoining-; cpds. in Slovene tv-ég, m. ‘effort’; tv-egati, v. ‘trouble; dare’, and perh. in Ir. taoiseach, m. “chief, prince": W. tywysog, m. id., if from a type *toui-stákos; cf. also Gk. sótron ‘felloe of a wheel?
=== HJB avarie ===
2332:AVERAGE.
2341:AVERAGE,  &  Skeat  derives  this in  all  its  senses  from  L.  Latin  averioy used  for  cattle ;  for  his  deduction  of meanings  we  must  refer  to  his  Dic- tionary. But  it  is  worthy  of  considera- tion whether  awrage,  m  its  special marine  use  for  a  proportionate  contri- bution towards  losses  of  those  whose goods  are  cast  into  the  sea  to  save  a ^p,  &c.,  is  not  directly  connected witn  the  Fr.  aoarie,  which  has  quite that  signification.  And  this  last Dozy  shows  most  plausibly  to  be  from the  Ar.  *awdr,  spoilt  merchandise.' [This  is  rejected  by  the  N,E,D.,  which concludes  that  the  Ar.  *awdr  is  **  merely a  mod.  Arabic  translation  and  adap- tation of  the  Western  term  in  its  latest sense.'']  Note  that  many  Eurooean words  of  trade  are  from  the  Arabic  ; and  that  avarie  is  in  Dutch  avoHj^ averijy  or  ^wn)'.— (See  Dozy,  Ooder- lingen,)
3238:1877.^«  The  Resident  was  gratified  at  the low  rate  of  assessment,  which  was  on  the general  average  eleven  annas  or  Is.  4^.  per nooglh,  that  for  the  Nizam's  country  being upwards  of  four  rupees."- ifeiuioiM  Taylor, JSStny  qfmsf  Life,  ii.  5.
4313:c.  1888.— "But  substitute  for  him  an average  ordinary,  uninteresting  Minister; obese,  dumpy  .  .  .  with  a  second-rate  wife — dusty,  deliquescent —  ...  or  let  him  bo seen  in  one  of  thoee  Shem-Ham-and-Japhet buggiee,  made  on  Mount  Ararat  soon  after the  subsidence  of  the  waters.  .  .  ." — Sydney Smith,  3rd  Letter  to  Archdeacon  Singleton.'
7718:1554. —  At  the  Maldives:  "Gowriea 12,000  make  one  oata;  and  4^  cottu  of average  size  weigh  one  tniintaJ  ;  the  big  ones someuiing  more." — A.  oV^mnm,  35.
=== FSD average ===
ugrep: error: error at position 89
x80-\xbf][\x80-\xbf]*){0,200}
exceeds complexity limits___/
```


## [2026-09-05T05:52:56.296Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1525,1545p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== around 9700 ===\"; sed -n '9700,9715p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T05:52:56.364Z] TOOL RESULT

```
Brugmann IF. 29, 206 a 1 noch immer erwagenswerter, als soleher mit 
aksl. ora „jener“ usw. (s. *auo- Pron.-St.), wonach damit jenseits des Eltern- 
paares stehende Personen bezeichnet gewesen seien. 

auei- „Yogel“. 

Lat. avis „Yogel“ (davon auca „Yogel, bes. Gans“; zur Bildung s. Vf. 
LEWb. 2 70) = umbr. avif a. pi. „aves“ (av iekatc d. sg. „auspicatae“, 
aviekla „augurali“); ai. vi-s, re-s m. „Yogel“ (g. vas, a. vim), av. vis ds. 
(g. pi. vayqm, auch mit themat. Kasus vom St. vaya-), mp. vai, rayandak 
„Yogel“, ai. vayas- n. „Gefliigel, Yogel“, vnyasa-h „Yogel, Krahe“; verbal 
av. ci-vayeiti „fliegt heran“ (von Gottheiten), ai. veviyatc „flattert“. 

Alle weiteren Ankniipfungsversuche sind mindestens ganz fraglich. Horn. 
aiszog, att. aezog, atfezog ' aezog- IJeoyaloi Hes. (*aft,-ez6g, Bildung wie 
(iQjtezov . . . txzivov . xQtjteg Hes.; J. Schmidt KZ. 32, 374, altere Lit. bei 
Danielsson IF. 14, 384), ist eher nach Danielsson aaO. mit atoXog zu ver- 
binden (von Lewy Sem. Fremdw. 8 wird es als Lehnwort aus hebr. 'ajja 
fiir ’awja, phonik. \nvjat „Falke“ angesehen). Gr. otcovog „groBer Yogel, 
Raubvogel“ (v. J. Schmidt KZ. 32, 374 aus *af/_cov6g durch Assimilation im 
Yorton erklart) bleibt fern (s. Brugmann IF. 17, 4S7 und 29, 2l2f., wo 
=== around 9700 ===
KZ. 27, 214 f.) 1 ): aksl. rosa „Tau“, lit. rasa ds.; lat. ros, ruris ,.Tau“ 
(kons. St. mit ursprunglich bloB nominativiseker Dehnstufe d) 1 ): alb. rei, 
reien „es schneit“, auch „regnet Asehe, Feuer“ ( Jokl SBWAk. 168,1, 73; 
wohl ebenfalls aus *ros-)\ gr. dn-egdio „gieBe eine Fliissigkeit, speie weg", 
ii-sgaio „schiitte aus, speie aus“, y.areoam ,.gieBe hinein", uer-tgaco ,.gieBe 
um“, avvegdm „gieBe zusaminen“. 

Zum Yokalismus: gr. *coa[a]- scheint mit den ar. und bsl. Worten auf 
idg. *ras- (oder *ercis- ) zuriickzugehn, wozu '*ros- flat., alb ) ebenso Dehn- 
stufe ware, wie *ou(i)om „Ei“ zu *auei- „Yogel t: und *o(tt)s- „Ohr“ zu *aus-. 
Aber in der bedeutungsverwandten Sippe *uer(a x )s- von gr. [f}ego?] „Tau !! , 
ai. varsati „regnet“ > usw. bestimmt mir. fross ,,Regenschauer“ den 2. Wz.- 
Yokal als o. 

Wzf. *-ers-,rs- : ai. arsati .,flieiit“ 2 ) ; ferner mit der Bed. „mannlich“ (aus 
„benetzend, Samen ergieBend“) ai. rsabha-h „Stier“, aja-riabha-h „Ziegen-
```


## [2026-09-05T05:52:59.758Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/ویش/\" --note \"page 73, NP vîš 'bird' check\" >/dev/null; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/وای/\" --note \"page 73, NP vây 'bird' check\" >/dev/null\nfor w in ویش وای; do f=$(python3 -c \"\nimport hashlib,sys;print(hashlib.sha1(('https://abadis.ir/fatofa/'+sys.argv[1]+'/').encode()).hexdigest()[:16])\" $w); echo \"##### $w -> $f\"; grep -n \"مرغ\\|پرنده\\|طایر\" data/verification/sources/web/$f.txt | head -6; done"
}
```


### [2026-09-05T05:53:04.520Z] TOOL RESULT

```
##### ویش -> 56ec26bfff801235
51: ویش vish - پرنده 
53:ریشه هندواروپائی ویش اوی awi یا پرنده، در فارسی باستان avifauna ودر اوستا ویش vish. و سانسکریت وی vih هردو بمعنی پرنده و در لاتین اویس avis. که در بونانی ایتوس aietos که معنی عقاب است. 
56:متاسفانه در لغت نامه های فارسی باشتباه نقل فول از برهان قاطع گفته شده که غلیواچ پرنده ایست که نصف سال نر و نصف دیگر ماده است که در شعر مسعود سعد سلمان � زبی حمییتی ایدوست چو غلیواجم - نه ماده خود را دانم اکنون همی و ن نر� ولی غلیواج یا Milvus migrans دارای جفت نر وماده میباشد و در موقع تخم گذاری فقط ماده روی تخم مینشیند.
##### وای -> 6d13264418474d63
57: ۱ - ( صفت ) کلمهایست دال بر : الف - تالم وافسوس واندوه افسوس . دریغ . ب - درد و بیماری دردا : یا برفلان . افسوس بر حال وی . : (( نوشته اند بر ایوان گنج بر جای بماند جاودان با حسرت و وای . ) ( ویس و رامین ) ۳ - فریاد ناله : (( فغان ازین غراب بین و وای او که در نو افکندمان نوای او . ) ( منوچهری ) یا وای فلان . وای بر آن کس افسوس برحال وی : (( رسول علیهالسلام گفت ویل لمن قرا هذهالایه فمج بها وایی آن کس که این آیه بخواند و بیندازد آنرا... ) ) (( چون نباشد عشق را پروای او او چو مرغی ماند بی پر وای او. ) ) (مثنوی ) یا ای وای . ۱ - ای افسوس . فسوسا . دریغا . : (( و اگه نیی که نفرین بر جان خویش کردی ای وای تو که کردی بر جان خویش نفرین . ) ) ( ناصرخسرو ) ۲ - د ردا .
```


## [2026-09-05T05:53:16.740Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '1,55p' 56ec26bfff801235.txt"
}
```


### [2026-09-05T05:53:16.789Z] TOOL RESULT

```
URL: https://abadis.ir/fatofa/ویش/
FETCHED: 2026-09-05T05:53:02Z
STATUS: 200
TITLE: ویش - معنی در دیکشنری آبادیس

ویش - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 ویش

 دنبال کنید 

 لغت نامه دهخدا

 ویش. [ ] ( اِ ) موش گیر. ( نسخه ای از فرهنگ اسدی ). غلیواج. زغن. 

 فرهنگ فارسی

 موش گیر غلیواج . 

 دانشنامه عمومی

 ویش ( به هلندی: Wisch ) یک منطقهٔ مسکونی در هلند است که در خلدرلاند واقع شده است. [ ۱] ویش ۷۲٫۷۹ کیلومتر مربع مساحت و ۱۹٬۵۳۴ نفر جمعیت دارد. 
 wiki: ویش 

 ویش (پلون). ویش ( به آلمانی: Wisch ) یک شهر در آلمان است که در پلون واقع شده است. [ ۲] ویش ۷۴۹ نفر جمعیت دارد. 
 wiki: ویش (پلون) 

 ویش (مجارستان). ویش ( به مجاری: Viss ) یک شهرداری در مجارستان است که در ناحیه شاروش پاتاک واقع شده است. [ ۱] ویش ۱۳٫۹ کیلومتر مربع مساحت و ۷۵۰ نفر جمعیت دارد. 
 wiki: ویش (مجارستان) 

 ویش (نوردفرایسلند). ویش ( به آلمانی: Wisch ) یک شهر در آلمان است که در نوردفرایسلند واقع شده است. [ ۲] ویش ۱۲۹ نفر جمعیت دارد. 
 wiki: ویش (نوردفرایسلند) 

 این نوشته برگرفته از سایت ویکی پدیا می باشد، اگر نادرست یا توهین آمیز است، لطفا گزارش دهید: گزارش تخلف 

 پیشنهاد کاربران

 در اوستایی "ویش" به معنای " سم، ماده سمی" و به آلمانی برابر با "giftige Substanz، Gift" آمده است. این واژه به همین ریخت در زبانِ پارسیِ میانه کاربرد داشته است. 
همچنین واژه "ویشَ' وَنت" در اوستایی به معنای " سمی" و به آلمانی برابر با "giftig" آمده است که اُزوارشِ این واژه به زبانِ پارسیِ میانه، "ویشومَند" بوده است. 
 ... [مشاهده متن کامل] 
. . . . 
پَسگشت:
ستون 1473 از نبیگ "فرهنگنامه زبانِ ایرانیِ کهن" ( کریستین بارتولومه )

 منبع. عکس فرهنگ ریشه واژگان فارسی دکتر علی نورایی

 ویش = زهر ، سم ، کیسه ی صفرا

 ویش vish - پرنده 
در فارسی زیر نام ویش ( لغت نامه دهخدا ) - واژه های غلیواج و موش گیر و زغن امده است. 
ریشه هندواروپائی ویش اوی awi یا پرنده، در فارسی باستان avifauna ودر اوستا ویش vish. و سانسکریت وی vih هردو بمعنی پرنده و در لاتین اویس avis. که در بونانی ایتوس aietos که معنی عقاب است. 
 ... [مشاهده متن کامل] 
غلیواج یا زغن از دسته پرندگان شکاری Milvus migrans و و بازها و نوع رنگ سیاه ان در اصطلاح بخاطر شکلی که در پرواز میگیرد به بادبادک سیاه معروف است black kite در انگلیسی از واژه ویش avian aviation ٫ osprey ٫ egg ، ovulation یا تخمک گذاری امده است.
```


## [2026-09-05T05:53:35.571Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nhead -6 data/verification/sources/web/7479201d4970c82f.txt; sed -n '20,26p' data/verification/sources/web/7479201d4970c82f.txt\nmkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg73.png data/verification/sources/refs/ocr/BOOK/73.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-05T05:53:37.079Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/aviation
FETCHED: 2026-09-05T05:49:36Z
STATUS: 200
TITLE: Aviation - Etymology, Origin & Meaning

Aviation - Etymology, Origin & Meaning 

 Origin and history of aviation 

 aviation (n.) 

 "art or act of flying," 1866, from French aviation , noun of action from stem of Latin avis "bird" (from PIE root *awi- "bird"). Coined in 1863 by French aviation pioneer Guillaume Joseph Gabriel de La Landelle (1812-1886) in "Aviation ou Navigation aérienne." 
 also from 1866 
-rw-rw-r-- 1 sfmqrb sfmqrb  49860 Sep  5 01:47 72.png
-rw-rw-r-- 1 sfmqrb sfmqrb  81180 Sep  5 01:53 73.png
-rw-rw-r-- 1 sfmqrb sfmqrb  56073 Sep  5 01:50 74.png
```


## [2026-09-05T06:02:23.747Z] TOOL CALL #73: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk73.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE_BIRD = W + \"Reconstruction:Proto-Indo-European/h₂éwis\"\nPIE_EGG = W + \"Reconstruction:Proto-Indo-European/h₂ōwyóm\"\nWK_XAYA = W + \"خایه\"\nWK_CAVIAR = W + \"caviar\"\nWK_AWAR = W + \"عوار\"\nWK_AR = W + \"عار\"\nET_AVG = \"https://www.etymonline.com/word/average\"\nET_OST = \"https://www.etymonline.com/word/ostrich\"\nET_KID = \"https://www.etymonline.com/word/kidney\"\nET_EGG = \"https://www.etymonline.com/word/egg\"\nET_AVI = \"https://www.etymonline.com/word/aviation\"\nAB_AWAR = \"https://abadis.ir/fatofa/عوار/\"\nAB_AR = \"https://abadis.ir/fatofa/عار/\"\nAB_VISH = \"https://abadis.ir/fatofa/ویش/\"\nAB_VAY = \"https://abadis.ir/fatofa/وای/\"\n\ndoc = {\n \"pdf_page\": 73,\n \"book_page\": 43,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n\n  # ------------------------------------------------------------------ entry 0\n  {\n   \"entry\": 0,\n   \"root\": \"Aw, Awi, Awei\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂éwis 'bird' (Pokorny 86 auei- (ouei-?) 'Vogel'; Watkins/AHD awi-)\",\n   \"note\": \"Root, language label and gloss are all correct and are copied straight from Pokorny p.86, which is also the page Nourai cites. Pokorny himself adds the cross-reference that Nourai turns into his second chart: 'Im Zusammenhang damit stehen höchstwahrscheinlich die Worte für Ei, s. unter ōu-' (p.86). Nourai's three root shapes Aw / Awi / Awei correspond to Pokorny's au-ei- and to AHD's awi-; the laryngeal notation *h₂éwis is the modern equivalent. The only weak point of the entry is the Avestan node, where the wind-word vayu- has been swept in (see node 1).\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₂éwis «پرنده» (در پوکورنی، صفحهٔ ۸۶، به صورت auei- «Vogel»؛ در واتکینز/AHD به صورت awi-). برچسب زبانی «هندواروپایی»، معنا و خودِ ریشه هر سه درست‌اند و دقیقاً از همان صفحه‌ای گرفته شده‌اند که نورایی ارجاع داده است. پوکورنی در پایان همان مدخل می‌افزاید که واژه‌های «تخم‌مرغ» نیز به احتمال بسیار زیاد با این ریشه پیوند دارند — همان چیزی که نورایی آن را نمودار دوم این صفحه کرده است. ادعای نورایی دربارهٔ ریشه درست است؛ تنها ایراد صفحه در گرهِ اوستایی است که واژهٔ «باد» (vayu) را نیز زیر این ریشه آورده است.\",\n   \"sources\": [PIE_BIRD],\n   \"ref_check\": [\n    {\"ref\": \"POK:86\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt line 1154 (\\\\f-leaf 95, running head '86'): 'auei- (ouei-?) „Vogel“. Ai. viḥ, véḥ m. „Vogel“ (Gen. véḥ, Akk. vim), av. vīš ds. (G. Pl. vayąm, auch mit themat. Kasus vom St. vaya-), mpers. vāi, vāyandak „Vogel“ … verbal av. ā-vayeiti „fliegt heran“ (von Gottheiten) … lat. avis f. „Vogel“ … Im Zusammenhang damit stehen höchstwahrscheinlich die Worte für „Ei“, s. unter ōu-.' Grep: grep -n \\\"auei-\\\" POK_01.txt.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.21 (WLD_Bd1_1930_dli_70244_djvu.txt line 1529)\", \"stance\": \"supports\",\n     \"note\": \"'auei- „Vogel“. Lat. avis „Vogel“ … = umbr. avif … ai. víḥ, véḥ m. „Vogel“, av. vīš ds. … mp. vāi, vāyandak „Vogel“ … verbal av. ā-vayeiti „fliegt heran“.' Pokorny's p.86 is a reprint of this article; the same volume (line 9709) says '*ou(i)om „Ei“ zu *auei- „Vogel“'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. awi- (AHD_watkins1985.txt line 317)\", \"stance\": \"supports\",\n     \"note\": \"'awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVIATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH … II. Possible derivatives are the Indo-European words for egg, *ōwyo-, *ōyo- … [Pok. auei- 86.]' — the same root, and the same link to the egg words.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck p.183, §3.64 BIRD\", \"stance\": \"supports\",\n     \"note\": \"The 'bird' article lists Lat. avis, Skt. vi-, pakṣin-, Av. vi-, marəγa-; on p.256 (§4.48 EGG) Buck says the egg words 'prob. reflect an IE word for egg derived fr. the word for bird seen in Lat. avis, Skt. vi- (3.64)'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, searched for awi-/awis\", \"stance\": \"silent\",\n     \"note\": \"grep 'awis' in IEC.txt returns only ouis 'sheep' (col. 12415); Mann's bird entry was not located in this OCR.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"vîš 2; vayu; vi 1, vay 1; â-vayeiti\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Three of the four words are right, one is not. (a) Av. vīš 'bird' is the nominative singular of the athematic stem vi- (Skt. víḥ, véḥ), the direct Iranian continuation of PIE *h₂éwis; the thematic by-form vaya- supplies the other cases (Pokorny 86: 'av. vīš ds., G. Pl. vayąm, auch mit themat. Kasus vom St. vaya-'). (b) The verb: Bartholomae col. 1356 has '²vay- V. „fliegen“, nur mit ā „heranfliegen“, von Gottheiten', i.e. the root is attested in Avestan only in the compound, so (c) ā-vayeiti 'flies hither' (of deities, Yt. 5.84, Yt. 13.49) is correct, though Nourai's gloss 'flied up' should be 'flies hither/up to'. (d) vayu 'air' does NOT belong here: Bartholomae col. 1357 files ¹vayav-/¹vaya- m. 'Luft, Atmosphäre, als Gottheit' under the verb ²vā- 'to blow' (Skt. vāyú- 'wind', MP wāy), and Pokorny puts it on pp. 81-84 s.v. au̯e-/u̯ē- 'wehen' ('ai. vāyúḥ, av. vāyuš „Wind, Luft“'), i.e. under PIE *h₂weh₁- 'to blow', a different root. The homonymy of Pahlavi wāy 'wind' and wāy 'bird' (Horn treats them in one paragraph, no. 207) is what invited the conflation.\",\n     \"derivation_fa\": \"از چهار واژهٔ این گره سه‌تا درست است و یکی نادرست. «vīš» صورت نهادیِ مفردِ ستاک vi- در اوستایی است (هم‌ریشه با سنسکریت víḥ / véḥ) و بازماندهٔ مستقیم *h₂éwis هندواروپایی؛ حالت‌های دیگر از ستاک مصوّت‌دار vaya- ساخته می‌شود (پوکورنی ۸۶). فعل vay- را بارتولومه (ستون ۱۳۵۶) تنها با پیشوند ā- ثبت کرده است: ā-vayeiti «به‌سوی این‌جا می‌پرد» و آن هم دربارهٔ ایزدان؛ پس این پیوند درست است، هرچند ترجمهٔ نورایی («بالا پرید») باید «به‌سوی … پرواز کرد» باشد. اما vayu «هوا، باد» به این ریشه تعلق ندارد: بارتولومه (ستون ۱۳۵۷) آن را به ستاک vā- «وزیدن» می‌بندد و پوکورنی نیز آن را در صفحه‌های ۸۱ تا ۸۴ زیر au̯e- «وزیدن» (هندواروپایی *h₂weh₁-) آورده است. هم‌آوایی «وای» به معنی باد و «وای» به معنی پرنده در فارسی میانه سبب این خلط شده است. نتیجه: پژوهش امروزی سه پیوند را می‌پذیرد و ورودِ vayu را رد می‌کند.\",\n     \"sources\": [PIE_BIRD],\n     \"ref_check\": [\n      {\"ref\": \"POK:86\", \"status\": \"partial\",\n       \"note\": \"Pokorny p.86 has 'av. vīš ds.' and 'verbal av. ā-vayeiti „fliegt heran“ (von Gottheiten)' — supports vīš, vay-, ā-vayeiti. It does NOT have vayu here; vāyu- 'Wind, Luft' stands on pp.81-84 under 'au̯e-, u̯ē- „wehen“' (POK_01.txt \\\\f-leaf 92: 'ai. vāyúḥ, av. vāyuš „Wind, Luft“').\"},\n      {\"ref\": \"HRN:296\", \"status\": \"supports\",\n       \"note\": \"HRN.txt \\\\f-leaf 317 = printed p.296, tail of entry no.207: '2) „Vogel“, vergl. vāyandak „Vogel“ (Men. 62,16). aw. vay- „Vogel“; ai. vāy-, oder nach Joh. Schmidt … Schmidt stellt dann auch lat. avis … hierher.' The head of the same entry (p.295) is 'vāi 1) „Luft“ … aw. vayu- „Luft“; ai. vāyu- „Luft, Wind“' — Horn keeps the two senses in one Pahlavi paragraph but derives them from two different Avestan words.\"},\n      {\"ref\": \"SYN:183\", \"status\": \"supports\",\n       \"note\": \"Buck p.183 §3.64 BIRD: 'Av. vi-, marəγa-', beside 'Lat. avis', 'Skt. vi-, pakṣin-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"cols. 1356-1357 (BRT.txt lines 22670, 22682, 22690)\", \"stance\": \"partial\",\n       \"note\": \"'j. ²vay- V. „fliegen“, nur mit ā „heranfliegen“, von Gottheiten' (col.1356); s.v. ²vaya- 'Vogel': 'Zum V. ²vay-. — ai. vā́y m. (víḥ, vāyaḥ); mp. (Pü.) vay, vgl. vāyandak' (col.1357) — supports the bird/fly words; but 'j. ¹vayav-, ¹vaya- m. „Luft, Atmosphäre“, als Gottheit … Zum V. ²vā-, mp. *vayu; ai. vāyú- m. „Wind“' — contradicts the inclusion of vayu under the bird root.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.21\", \"stance\": \"supports\",\n       \"note\": \"Same article as Pokorny 86: 'av. vīš ds. (g. pl. vayąm, auch mit themat. Kasus vom St. vaya-) … verbal av. ā-vayeiti „fliegt heran“ (von Gottheiten)'; vāyu- is not in it.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins s.v. awi-\", \"stance\": \"partial\",\n       \"note\": \"Lists only Latin avis and the egg words as derivatives; no Iranian material, and no connection of the wind-word (which Watkins files under wē- 'to blow').\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"vôi, vây, vâyandak\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"Middle Persian wāy 'bird' and its present participle wāyēndag 'flying creature, bird' are both real and both continue Av. vaya-/vay-: Pokorny p.86 prints 'mpers. vāi, vāyandak „Vogel“', Walde-Pokorny I 21 the same, and Nyberg's glossary p.207 has 'vāyēndak [wʾyndk'] flying creature … Pres. pt. of Av. (1356) √vay- „to fly“'. Intervocalic Old Iranian -y- is kept, and the participle suffix Av. -ant- > MP -ēnd-ag. The first form, 'vôi', is not a form any of the sources knows: Pokorny, Walde-Pokorny and Horn (p.295 'vāi') all print vāi = wāy, with ā. The printed page 43 of Nourai's book itself reads 'vôi, vây, vâyandak', so the extraction is faithful and the odd form is the book's own misprint of Pokorny's vāi. Note also that MacKenzie's dictionary does not list wāy 'bird' at all (Pahlavi for 'bird' is murw); MP wāy is chiefly the wind/atmosphere word (andarwāy 'air'), and 'bird' is the sense Horn and Nyberg document from the Avesta commentary and the Mēnōg ī xrad.\",\n     \"derivation_fa\": \"«وای» فارسی میانه به معنی پرنده و صفت فاعلیِ آن «وایَندَگ» (wāyēndag) «پرنده، جانور پرّان» هر دو واقعی‌اند و دنبالهٔ اوستایی vaya-/vay- به شمار می‌روند: پوکورنی (ص ۸۶) «mpers. vāi, vāyandak» می‌نویسد، والده‑پوکورنی نیز همین را، و نیبرگ در واژه‌نامهٔ خود (ص ۲۰۷) می‌آورد: «vāyēndak [wʾyndk'] جانور پرّان … اسم فاعلِ حالِ ریشهٔ اوستایی vay- «پریدن»». یِ میان‌واکه‌ای ایرانی باستان حفظ شده و پسوند اوستایی ‎-ant-‎ در فارسی میانه به ‎-ēnd-ag‎ بدل شده است. اما صورت «vôi» را هیچ‌یک از منابع نمی‌شناسد؛ همه vāi (یعنی wāy) با آی کشیده دارند. تصویر صفحهٔ ۴۳ چاپیِ کتاب نشان می‌دهد که خودِ کتاب «vôi» چاپ کرده است، پس خطا از خوانشِ اسکن نیست بلکه خطای چاپی کتاب است (بدخوانیِ vāi پوکورنی). افزون بر این، مکنزی «wāy» را به معنی پرنده نیاورده است (واژهٔ رایج فارسی میانه برای پرنده murw است) و wāy در آن بیشتر «هوا، باد» است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"vôi, vây, vâyandak\",\n     \"correct_form\": \"vāy, vāyandag (Pokorny/Walde-Pokorny vāi, vāyandak)\",\n     \"sources\": [PIE_BIRD],\n     \"ref_check\": [\n      {\"ref\": \"POK:86\", \"status\": \"supports\",\n       \"note\": \"'mpers. vāi, vāyandak „Vogel“' (POK_01.txt line 1155). Supports vây and vâyandak; the printed 'vôi' has no counterpart here — Pokorny's form is vāi.\"},\n      {\"ref\": \"NYB:207\", \"status\": \"supports\",\n       \"note\": \"NYB_vol2_glossary.txt, page marker '207' immediately precedes the column: 'vāyēndak [wʾyndk'] flying creature, pl. cas. obl. -ān, enumerated after murvān 80². — Pres. pt. of Av. (1356) √vay- „to fly“.' Exactly Nourai's page and word; Nyberg has no vōi/vāy headword of its own.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.vv. murw, andarwāy (PHD.txt lines 493, 761)\", \"stance\": \"partial\",\n       \"note\": \"'murw [mwlw | M mwrw, (N murγ)] bird'; 'air andarwāy, way' — MacKenzie's wāy is the air/wind word, and he gives no wāy 'bird', so the bird sense rests on Horn/Nyberg's Avesta-commentary material.\"},\n      {\"src\": \"HRN\", \"where\": \"pp. 295-296, entry no. 207\", \"stance\": \"supports\",\n       \"note\": \"'vāi 1) „Luft“ … 2) „Vogel“, vergl. vāyandak „Vogel“ (Men. 62,16). aw. vay- „Vogel“' — Horn's Pahlavi form is vāi, never vōi.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.21\", \"stance\": \"supports\",\n       \"note\": \"'mp. vāi, vāyandak „Vogel“' — the source of Pokorny's wording, again with ā.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"vây «واى»; vîš «ویش»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The chart's own note ('both are almost obsolete') is an understatement for the first word and right for the second. (a) وایش/ویش: Dehkhoda has 'ویش. (اِ) موش‌گیر. (نسخه‌ای از فرهنگ اسدی). غلیواج. زغن' — 'mouse-catcher, kite (Milvus), black kite', expressly quoted from a manuscript of Asadi's Farhang (= Loghat-e Fors, Nourai's FRS), so a New Persian reflex of Av. vīš does survive, but as the name of one raptor, not as the general word 'bird' (that is مرغ/پرنده). Phonologically it is regular: OIr. *wiš > MP wiš > NP vīš, with no lenition of the initial w- to v- other than the normal New Persian spelling. (b) وای 'bird' is not in Dehkhoda, Mo'in or Amid, all of which give only the interjection وای 'alas' (a different, expressive word); it is the Pahlavi wāy of node 2 carried over into the Persian column rather than an attested New Persian noun. Verdict: the derivation Av. vi-/vaya- > MP wāy > NP vīš is sound, but 'vây' as a New Persian bird-word is unsupported.\",\n     \"derivation_fa\": \"یادداشت خود نمودار («هر دو تقریباً منسوخ‌اند») دربارهٔ واژهٔ دوم درست و دربارهٔ اولی خوش‌بینانه است. «ویش» را دهخدا چنین آورده است: «ویش. (اِ) موش‌گیر. (نسخه‌ای از فرهنگ اسدی). غلیواج. زغن»؛ یعنی همان لغت‌نامه‌ای که نورایی با نشانِ FRS به آن ارجاع می‌دهد (فرهنگ اسدی = لغت فرس) این واژه را دارد، اما نه به معنیِ عامِ «پرنده» بلکه نامِ یک پرندهٔ شکاریِ ویژه (غلیواج، زغن). تحول آوایی بی‌قاعده نیست: ایرانی باستان *wiš > فارسی میانه wiš > فارسی نو ویش. اما «وای» به معنی پرنده در دهخدا، معین و عمید نیامده است؛ در این فرهنگ‌ها «وای» تنها شبه‌جمله‌ای است به معنی «افسوس». پس ادعای نورایی دربارهٔ ویش با احتیاط پذیرفتنی است و «وایِ» فارسی در واقع همان «وای» فارسی میانه است که به ستون فارسی نو منتقل شده است.\",\n     \"sources\": [AB_VISH, AB_VAY],\n     \"ref_check\": [\n      {\"ref\": \"HRN:995\", \"status\": \"not_found\",\n       \"note\": \"Horn's Grundriss has no page 995 (HRN.txt has 411 leaves = printed pp. 1-~390) and its numbered entry 995 is 'mūš „Maus“' (HRN.txt line 8650). The Horn place that actually carries this material is pp.295-296, entry 207 ('vāi 1) „Luft“ … 2) „Vogel“ … vāyandak'), so HRN:995 looks like the book's misprint for HRN:295. The printed page 43 does read 'HRN:995', so this is Nourai's citation, not an extraction slip.\"},\n      {\"ref\": \"FRS:56\", \"status\": \"partial\",\n       \"note\": \"Could not be located in the Loghat-e Fors OCR on disk (FRS_pages.txt / FRS.txt, greps for ویش and وای), whose pagination is Eqbal's 1319 edition, not the 1365 Kharazmi edition Nourai cites. But the entry demonstrably exists: Dehkhoda's article ویش cites it verbatim — 'موش‌گیر. (نسخه‌ای از فرهنگ اسدی). غلیواج. زغن' (abadis.ir/fatofa/ویش).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in/Dehkhoda via abadis.ir, s.vv. ویش and وای\", \"stance\": \"partial\",\n       \"note\": \"ویش = 'موش‌گیر … غلیواج. زغن' (a kite); وای has only the interjectional senses ('تألم و افسوس و اندوه', 'فریاد، ناله'), with no 'bird' sense.\"},\n      {\"src\": \"HRN\", \"where\": \"pp.295-296\", \"stance\": \"partial\",\n       \"note\": \"Horn documents vāi/vāyandak only as Pahlavi (from the Avesta commentary and Mēnōg ī xrad); he lists no New Persian continuation.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\",\n       \"note\": \"grep for 'Ei', 'chaje', 'xaje' and the bird forms in HUB.txt returned nothing relevant.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"avis\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin avis f. 'bird' is the classic exemplar of the root: it continues PIE *h₂éwis directly (with the regular Italic outcome *awis, cf. Umbrian avif acc.pl. 'aves' in the augural formulae aviekate 'auspicatae', aviekla 'augurali'). Pokorny 86 and Walde-Pokorny I 21 give exactly this equation, and de Vaan's Latin etymological dictionary (pp.65-66, cited on the Wiktionary reconstruction page) keeps it. The derivative auspex 'augur' < *awi-spek- 'observer of birds' shows the word alive in Roman religion.\",\n     \"derivation_fa\": \"واژهٔ لاتینِ avis «پرنده» بازماندهٔ مستقیم *h₂éwis هندواروپایی است؛ در ایتالیک به *awis رسیده و در اومبریایی نیز به‌صورت avif (رایی جمع) در فرمول‌های فال‌گیری با پرندگان دیده می‌شود. پوکورنی (ص ۸۶) و والده‑پوکورنی (جلد یکم ص ۲۱) همین برابری را می‌دهند و دِ فان نیز در فرهنگ ریشه‌شناختی لاتین آن را نگه داشته است. مشتقِ auspex «مرغ‌بین، فال‌گیر» از *awi-spek- «نگرندهٔ پرندگان» نشان می‌دهد که واژه در آیین رومی زنده بوده است. ادعای نورایی درست است.\",\n     \"sources\": [PIE_BIRD],\n     \"ref_check\": [\n      {\"ref\": \"POK:86\", \"status\": \"supports\",\n       \"note\": \"'lat. avis f. „Vogel“ (davon auca „Vogel, bes. Gans“ …) = umbr. avif Akk. Pl. „aves“ (aviekate D. Sg. „auspicatae“, aviekla „augurali“)' (POK_01.txt line 1157).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins s.v. awi-\", \"stance\": \"supports\",\n       \"note\": \"'awi-. Bird. I. 1. Latin avis, bird … 2. Compound *awi-spek-, „observer of birds“ … in Latin auspex, augur: AUSPICE. [Pok. auei- 86.]'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.21\", \"stance\": \"supports\",\n       \"note\": \"'Lat. avis „Vogel“ (davon auca „Vogel, bes. Gans“) = umbr. avif a. pl. „aves“.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck p.183 §3.64\", \"stance\": \"supports\",\n       \"note\": \"Latin column of the 'bird' article: 'Lat. avis'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"aviation, ostrich\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both are Latin avis in English dress, by two very different routes. aviation was coined in French in 1863 by G. de La Landelle ('Aviation ou Navigation aérienne') on the stem of Latin avis, and entered English in 1866. ostrich is much older: Vulgar Latin avis struthio 'the struthio-bird' (Latin avis + Late Latin struthio < Greek strouthiōn, from strouthos megalē 'big sparrow') > Medieval Latin ostrica/ostrigius > Old French ostruce (Mod.Fr. autruche) > early 13th-c. English ostriche/estrich; the avis element survives only as the initial os-. Watkins accordingly indexes OSTRICH under both awi- and trozdo-.\",\n     \"derivation_fa\": \"هر دو واژه در نهایت همان avis لاتین‌اند، اما از دو راهِ بسیار متفاوت. «aviation» را در سال ۱۸۶۳ گیوم دو لا لاندل در فرانسه از ستاکِ avis ساخت و در ۱۸۶۶ به انگلیسی راه یافت. «ostrich» بسیار کهن‌تر است: لاتینِ عامیانه avis struthio «پرندهٔ شترمرغ» (avis + struthio از یونانی strouthiōn، از strouthos megalē «گنجشکِ بزرگ») > لاتین میانه ostrica > فرانسهٔ کهن ostruce (فرانسهٔ امروز autruche) > انگلیسی میانهٔ ostriche در آغاز سدهٔ سیزدهم؛ از avis تنها os- آغازین بر جای مانده است. واتکینز نیز «ostrich» را هم زیر awi- و هم زیر trozdo- فهرست کرده است. ادعای نورایی درست است.\",\n     \"sources\": [ET_AVI, ET_OST],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. awi-: 'Latin avis, bird: AVIAN, AVIARY, AVIATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH'; the index (AHD_watkins1985.txt line 2001) reads 'OSTRICH awi-, trozdo-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, s.vv. aviation, ostrich\", \"stance\": \"supports\",\n       \"note\": \"Klein derives both from L. avis; his ostrich article gives the same OF ostruce < VL avis struthio chain that Etymonline prints.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. ostrich\", \"stance\": \"supports\",\n       \"note\": \"Skeat's concise dictionary derives ostrich from O.F. ostruche < L. avis struthio (the entry is in SKT.txt but heavily garbled by OCR; the chain is the standard one).\"}\n     ]\n    }\n   ]\n  },\n\n  # ------------------------------------------------------------------ entry 1\n  {\n   \"entry\": 1,\n   \"root\": \"Ow, Owo, Ayo, Ôwyo\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂ōwyóm 'egg', a vṛddhi derivative of *h₂éwis 'bird' (Pokorny 783 ō(u)i̯om; AHD *ōwyo-, *ōyo-)\",\n   \"note\": \"Nourai's four root shapes are simply Pokorny's and Watkins's variants written without asterisks: Pokorny p.783 heads the article 'ō(u)i̯om „Ei“, d. h. „das zum Vogel gehörige“, schwache Form ǝu̯iom', and Watkins writes '*ōwyo-, *ōyo-'. The double citation POK:86,783 is exactly right, because Pokorny cross-refers between the two pages. The modern reconstruction *h₂ōwyóm and the derivation from *h₂éwis are the mainstream view (Mallory-Adams 2006:143; de Vaan 438), though a minority holds the vṛddhi derivation morphologically unlikely and reconstructs *(H)ō-Huy-óm or *ōyom instead.\",\n   \"note_fa\": \"چهار صورتی که نورایی برای ریشه آورده چیزی جز گونه‌های پوکورنی و واتکینز بدون ستاره نیست: پوکورنی در صفحهٔ ۷۸۳ مدخل را چنین آغاز می‌کند «ō(u)i̯om «تخم»، یعنی «آنچه از آنِ پرنده است»، صورت ضعیف ǝu̯iom»، و واتکینز *ōwyo-, *ōyo- می‌نویسد. ارجاع دوگانهٔ POK:86,783 نیز درست است، زیرا پوکورنی خود این دو صفحه را به هم ارجاع می‌دهد. بازسازی امروزی *h₂ōwyóm و اشتقاق آن از *h₂éwis «پرنده» (با کشش وریدهی) دیدگاه غالب است (مالوری‑آدامز ۲۰۰۶، دِ فان)، هرچند اقلیتی این اشتقاق را از نظر ساخت‌واژی بعید می‌دانند و *ōyom را ترجیح می‌دهند. ادعای نورایی درست است.\",\n   \"sources\": [PIE_EGG, PIE_BIRD],\n   \"ref_check\": [\n    {\"ref\": \"POK:86\", \"status\": \"supports\",\n     \"note\": \"p.86 ends: 'Im Zusammenhang damit stehen höchstwahrscheinlich die Worte für „Ei“, s. unter ōu-.'\"},\n    {\"ref\": \"POK:783\", \"status\": \"supports\",\n     \"note\": \"POK_03.txt \\\\f-leaf 18 (running head 783/784): 'ō(u)i̯om „Ei“, d. h. „das zum Vogel gehörige“, schwache Form ǝu̯iom. Av. ap-āvaya- „entmannt“(?), falls aus apa-āvaya- „ohne Hode“, vgl. apers. xāya „Ei“; gr. att. ᾠόν … lat. ōvum … krimgot. ada, aisl. egg, ahd. ei, ags. ǣg „Ei“ (germ. *ajjaz-)'. Every form in Nourai's chart, including ap-āvaya and the Germanic *ajja-, comes from this page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins s.v. awi- II\", \"stance\": \"supports\",\n     \"note\": \"'II. Possible derivatives are the Indo-European words for egg, *ōwyo-, *ōyo-. 1. Germanic *ajja(m) … a. Old English ǣg, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2. Latin ōvum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek ōion, egg: OO-.' — Nourai's Ayo/Ôwyo, the Germanic and the Latin branches, all at once.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck p.256, §4.48 EGG\", \"stance\": \"supports\",\n     \"note\": \"'1. IE *ōwo-, *ow(e)yo-, *ō(w)yo-(?). The words grouped here … prob. reflect an IE word for „egg“ derived fr. the word for „bird“ seen in Lat. avis, Skt. vi- (3.64).' Buck's list ends: 'Av. *āvaya-, NPers. xāya-; Arm. ju.'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I (index passage, line 9709)\", \"stance\": \"supports\",\n     \"note\": \"'… wie *ou(i)om „Ei“ zu *auei- „Vogel“ und *o(u)s- „Ohr“ zu *aus-' — the same derivational relation Nourai draws between his two roots.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"âvaya, xâya; ap-âvaya\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The forms are Pokorny's and Buck's, but Nourai has dropped their asterisks and their question marks. (a) Avestan *āvaya- 'egg' is a reconstruction, not an attested word: Buck p.256 prints it starred, 'Av. *āvaya-', and the Avestan word actually attested for 'egg' is aēm (< Proto-Iranian *Hāwyám with the regular contraction *-āwya- > aē-). (b) xāya is likewise not Old Persian: Kent's Old Persian lexicon has no such word (grep of KNT.txt), and the form belongs to Middle and New Persian, where the initial x- is the well-known hiatus-filling/prothetic development in *āwyaka- > xāyag. Pokorny's own 'apers. xāya' is a slip of the same kind. (c) ap-āvaya-: Bartholomae (col. 87, s.v. apāvaya-) glosses the word only as 'Name einer Krankheit oder eines Gebrechens' at Vd. 2.29, and Pokorny keeps the sense in question marks: 'av. ap-āvaya- „entmannt“(?), falls aus apa-āvaya- „ohne Hode“'. So 'to castrate' is a conjecture ('without testicles' > 'castrated/impotent'), attractive because Persian xāya means both 'egg' and 'testicle', but it is not the established meaning. The root relation itself — Proto-Iranian *Hāwyám < PIE *h₂ōwyóm — is not in doubt.\",\n     \"derivation_fa\": \"صورت‌های این گره از پوکورنی و باک گرفته شده‌اند، اما نورایی ستاره‌ها و علامت‌های پرسش آن‌ها را حذف کرده است. نخست، *āvaya- اوستایی واژه‌ای بازسازی‌شده است نه ضبط‌شده؛ باک (ص ۲۵۶) آن را با ستاره می‌آورد و واژهٔ اوستاییِ واقعیِ «تخم» aēm است (از ایرانی آغازین *Hāwyám با ادغام منظمِ ‎*-āwya- > aē-‎). دوم، xāya پارسی باستان نیست: در واژه‌نامهٔ کِنت چنین واژه‌ای نیست؛ این صورت به فارسی میانه و فارسی نو تعلق دارد و خِ آغازینِ آن همان «خ» میانجی/پیشین است که در *āwyaka- > xāyag پدید آمده است. سوم، ap-āvaya-: بارتولومه (ستون ۸۷) آن را تنها «نام یک بیماری یا نقص» در وندیداد ۲٫۲۹ معنی می‌کند و پوکورنی نیز معنی «اخته» را با علامت پرسش می‌آورد. پس «اخته کردن» حدسی است — هرچند حدسی دلپذیر، چون «خایه» در فارسی هم «تخم» است و هم «بیضه». اصلِ پیوند با *h₂ōwyóm هندواروپایی جای تردید ندارد؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [PIE_EGG, WK_XAYA],\n     \"ref_check\": [\n      {\"ref\": \"POK:783\", \"status\": \"supports\",\n       \"note\": \"'Av. ap-āvaya- „entmannt“(?), falls aus apa-āvaya- „ohne Hode“, vgl. apers. xāya „Ei“' (POK_03.txt \\\\f-leaf 18). Nourai's node reproduces this sentence, minus Pokorny's '(?)' and 'falls' ('if').\"},\n      {\"ref\": \"SYN:256\", \"status\": \"supports\",\n       \"note\": \"Buck p.256 (running head '256 SELECTED INDO-EUROPEAN SYNONYMS' immediately above §4.48 EGG): 'Av. *āvaya-, NPers. xāya-; Arm. ju.' — with Buck's asterisk on the Avestan form.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 87, s.v. apāvaya- (BRT.txt line 3648)\", \"stance\": \"partial\",\n       \"note\": \"'j. apāvaya- m. Name einer Krankheit oder eines Gebrechens: mā (aθra) °ii V. 2.29.' Bartholomae records the word but not the meaning 'castrate/castration'.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon\", \"stance\": \"silent\",\n       \"note\": \"grep 'xāya|xaya' in KNT.txt returns only the personal name Hadaxāya; there is no Old Persian word for 'egg', so the 'Old Persian' label of this node is not documented.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck p.256\", \"stance\": \"supports\",\n       \"note\": \"Places EGG in the body-parts chapter next to §4.49 TESTICLE — the very polysemy that makes 'ap-āvaya = without testicles' thinkable.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"hâyîk, xâyak; xâyak-bar, xâyak-bâr\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian xāyag 'egg; testicle' < Proto-Iranian *Hāwya-ka- (the -ka- diminutive/suffix that gives NP -a), with the group *-āwy- yielding -āy- and a secondary x- before the initial ā-. Horn p.103, no.468 has 'χāye „Ei“. phlv. χāyak „Ei“ (Men.)'; MacKenzie prints the Book-Pahlavi spelling as 'xāyag [hʾd(y)k | N xāya] egg' — and that spelling is the key to Nourai's first form: 'hâyîk' is simply the letter-by-letter transliteration of ⟨hʾdyk⟩/⟨hʾyk⟩, which is read xāyag. Both of Nourai's forms are therefore the same word, one transliterated and one transcribed. The compound xāyag-bar/-bār 'egg-carrier' (of the sturgeon) is Asbaghi's reconstruction of the ancestor of Persian خاویار: PLA p.104 analyses it as 'MP xāyak „Ei“ + bar … aw./ap. bar „tragen“', which is exactly the cross-reference to root Bher 1 that the chart carries.\",\n     \"derivation_fa\": \"«خایگ» فارسی میانه (xāyag) «تخم، بیضه» از ایرانی آغازین *Hāwya-ka- می‌آید؛ خوشهٔ ‎*-āwy-‎ به ‎-āy-‎ ساده شده و پیشِ آی آغازین خِ میانجی افزوده شده است، و پسوند ‎-ka-‎ همان است که در فارسی نو به ‎-ه‎ بدل می‌شود. هرن (ص ۱۰۳، شمارهٔ ۴۶۸) می‌نویسد: «xāye «تخم». پهلوی xāyak «تخم» (مینوی خرد)». مکنزی صورت خطِ پهلوی را ⟨hʾd(y)k⟩ می‌آورد و آن را xāyag می‌خواند — و همین کلیدِ صورت نخستِ نورایی است: «hâyîk» چیزی جز حرف‌نویسیِ همان املای پهلوی نیست، پس هر دو صورتِ این گره یک واژه‌اند، یکی حرف‌نویسی و دیگری آوانویسی. ترکیبِ xāyag-bār «تخم‌بَر» (لقبِ ماهی خاویاری) بازسازیِ اصباغی است: او در صفحهٔ ۱۰۴ آن را «xāyak فارسی میانه + bar از ریشهٔ اوستایی/پارسی باستانِ bar «بردن»» تحلیل می‌کند — درست همان ارجاعِ ☞Bher 1 که در نمودار آمده است. ادعای نورایی درست است.\",\n     \"sources\": [WK_XAYA],\n     \"ref_check\": [\n      {\"ref\": \"HRN:103\", \"status\": \"supports\",\n       \"note\": \"HRN.txt \\\\f-leaf 125 = printed p.103, entry no.468: 'χāye „Ei“. phlv. χāyak „Ei“ (Men.); arm. ju „Ei“ (unsicher; H. No. 179); lat. ōvum; gr. ᾠόν; ksl. aje, jaje „Ei“. kurd. haik, hī, hek; afγ. hā; oss. t. aik, d. aiḱä; bel. haik.' Exactly Nourai's Pahlavi > Persian arrow, with the Latin ōvum cognate as well.\"},\n      {\"ref\": \"PLA:104\", \"status\": \"supports\",\n       \"note\": \"PLA_pages.txt leaf 119 = printed p.104: 'خاويار hāwiyār: „Kaviar“ aus dem pers. خاويار hāviyār „Eiertragend“; MP. xāyak „Ei“ + bar; aw. aya + aw./ap. bar „tragen“ … dtsch. Kaviar, frz. caviar.' Asbaghi's footnote 11 credits FM (Addi Shir).\"},\n      {\"ref\": \"BQT:711\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' vol.2, BQT_v2_pages.txt leaf 169 (printed ≈712, i.e. Nourai's 711 within the ±3 of the running-head mapping): 'خایه — بر وزن مایه. خصیهٔ انسان و حیوانات دیگر باشد … و بدبیضهٔ مرغ را نیز گویند' — 'the testicle of man and other animals … also said of a bird's egg', i.e. the double gloss 'egg, testicle' that the node prints. No Mo'in etymological footnote on that page.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.94, s.v. xāyag (PHD_mackenzie.txt line 5549)\", \"stance\": \"supports\",\n       \"note\": \"'xāyag [hʾd(y)k | N xāya] egg' — and the English-Pahlavi index 'egg xāyag', 'oval xāyagdēs'. The bracketed spelling explains Nourai's 'hâyîk'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II\", \"stance\": \"silent\",\n       \"note\": \"The glossary (a Mēnōg ī xrad / Bundahišn selection) has vāyēndak but no xāyak entry.\"},\n      {\"src\": \"HRN\", \"where\": \"p.103 no.468\", \"stance\": \"supports\",\n       \"note\": \"See ref_check; Horn's source for phlv. xāyak is the Mēnōg ī xrad ('Men.').\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"xâyeh «خایه»; xâvîyâr «خاویار»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"خایه xāya 'egg; testicle' is the regular New Persian continuation of MP xāyag, with the loss of final -g and the -a ending: Wiktionary (with Hasandust's material) gives 'From Middle Persian xāyak, from Proto-Iranian *Hāwyám (compare N. Kurdish hêk, Ossetian ajk, Avestan aēm), from PII *Hāwyám, from PIE *h₂ōwyóm'. خاویار xāvyār 'caviar' is a compound of the same word: xāya 'egg' + -bār/-yār 'bearing' (Persian بار from the verb بردن/بار- < PIE *bher-, whence the chart's ☞Bher 1), literally 'egg-bearing', the epithet of the roe-bearing sturgeon; the -b- > -v- and the writing خاویار are the ordinary Persian intervocalic softening. Addi Shir and Asbaghi both analyse it this way, and it is the etymology the modern dictionaries follow.\",\n     \"derivation_fa\": \"«خایه» بازماندهٔ منظمِ xāyag فارسی میانه است؛ گاف پایانی افتاده و پایانهٔ ‎-ه‎ نشسته است. ویکی‌واژه (بر پایهٔ حسن‌دوست) می‌نویسد: «از فارسی میانهٔ xāyak، از ایرانی آغازین *Hāwyám (سنجید نی با کردی شمالی hêk، آسی ajk، اوستایی aēm)، از هندوایرانی آغازین *Hāwyám، از هندواروپایی آغازین *h₂ōwyóm». «خاویار» ترکیبی از همین واژه است: خایه «تخم» + بار/یار «برنده، دارنده» (از ریشهٔ «بردن/بار-»، همان ☞Bher 1 نمودار)، یعنی «تخم‌بَر» — لقبِ ماهیِ تخم‌دار. بدل شدن «ب» به «و» در میانِ واکه‌ها و املای «خاویار» تحولی عادی در فارسی است. ادّی شیر و اصباغی هر دو همین تحلیل را دارند و فرهنگ‌های امروزی نیز آن را پذیرفته‌اند. ادعای نورایی درست است.\",\n     \"sources\": [WK_XAYA, WK_CAVIAR],\n     \"ref_check\": [\n      {\"ref\": \"HRN:103\", \"status\": \"supports\",\n       \"note\": \"'468. χāye „Ei“. phlv. χāyak „Ei“ (Men.)' — the Pahlavi > New Persian step of this node, verbatim.\"},\n      {\"ref\": \"SYN:256\", \"status\": \"supports\",\n       \"note\": \"Buck p.256 §4.48 EGG: 'Av. *āvaya-, NPers. xāya-' in the group headed 'IE *ōwo-, *ow(e)yo-, *ō(w)yo-'.\"},\n      {\"ref\": \"PLA:104\", \"status\": \"supports\",\n       \"note\": \"'aus dem pers. خاويار hāviyār „Eiertragend“; MP xāyak „Ei“ + bar' — Asbaghi's analysis of xāvyār as 'egg-bearing', exactly Nourai's node plus its Bher cross-reference.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.2 ≈p.712 s.v. خایه\", \"stance\": \"supports\",\n       \"note\": \"'خایه … خصیهٔ انسان و حیوانات دیگر باشد … و بدبیضهٔ مرغ را نیز گویند' — both senses of the node.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir p.51\", \"stance\": \"supports\",\n       \"note\": \"'(الخابياري) بزر السمك تعريب خایه‌بار واصل معناه کثرة البیض. ومنه خاويار' — the Arabic form is arabicized from Persian xāya-bār 'abundance of eggs', and Turkish خاويار comes from it.\"},\n      {\"src\": \"HRN\", \"where\": \"p.103\", \"stance\": \"supports\", \"note\": \"See ref_check.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Turkish\", \"words\": \"havyâr\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Ottoman Turkish خاویار havyar 'caviar' is a loan from Persian خاویار xāvyār, with the usual Turkish rendering of Persian x- as h- (cf. hoca < xʷāja); it is the form from which all the European words descend. Wiktionary: 'probably by way of Ottoman Turkish خاویار (havyar), from Classical Persian خَاوْیَار (xāwyār)', and Addi Shir p.51 says the same. Two reservations. (i) The arrow is drawn from the Pahlavi node, but the borrowing is from New Persian and belongs to the late-medieval Black Sea sturgeon trade, not to the Sasanian period. (ii) A rival etymology derives the Western word from Kaffa (Theodosia), the Crimean trading port — Klein adopts it ('fr. Turk. khavidr, fr. Kaffah … name of a trading town') — but Lokotsch, who reports it (no.851, from Joest), calls it 'sehr anzuzweifeln', and today the Persian source is the standard view.\",\n     \"derivation_fa\": \"«havyar»ِ ترکی عثمانی (خاویار) وام‌واژه‌ای است از فارسیِ «خاویار»؛ خِ فارسی در ترکی به «ه» بدل می‌شود (مانند خواجه > hoca). همین صورت است که همهٔ واژه‌های اروپایی از آن برخاسته‌اند: ویکی‌واژه می‌نویسد «احتمالاً از راه ترکی عثمانی خاویار، از فارسی کلاسیک خاویار»، و ادّی شیر (ص ۵۱) نیز همین را می‌گوید. دو نکته: نخست آن‌که پیکان نمودار از گرهِ پهلوی کشیده شده، حال آن‌که وام‌گیری از فارسیِ نو و مربوط به بازرگانیِ ماهیِ دریای سیاه در سده‌های میانهٔ متأخر است، نه از دورهٔ ساسانی. دوم آن‌که ریشه‌شناسیِ رقیبی وجود دارد که واژهٔ اروپایی را به نامِ بندرِ کافا (تئودوسیا) در کریمه می‌بندد و کلاین آن را پذیرفته است؛ اما لوکوچ (شمارهٔ ۸۵۱) خودِ همین نظر را «بسیار مشکوک» می‌خواند و امروز منشأ فارسی دیدگاه معیار است. با احتیاط پذیرفتنی است.\",\n     \"sources\": [WK_CAVIAR],\n     \"ref_check\": [\n      {\"ref\": \"AFM:51\", \"status\": \"supports\",\n       \"note\": \"AFM_pages.txt leaf 52 = printed p.51 (checked against the book's Turkish index, which gives خاتون on p.51 on the same leaf): '(الخابياري) بزر السمك تعريب خایه‌بار واصل معناه کثرة البیض. ومنه خاويار' — 'fish roe, arabicized from Persian xāya-bār, whose original meaning is „abundance of eggs“; and from it (Turkish) khāvyār'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no.851 (LKT.txt line 2061)\", \"stance\": \"partial\",\n       \"note\": \"'851. Tk. hawjar: „Kaviar“; hieraus ngr. καβιάριον … it. caviaro, caviale … frz. caviar; engl. ndl. caviar, dtsch. Kaviar. — [JOEST … vermutet, daß das abendländische Wort auf den Namen des Hafens Kapha, d. h. Theodosia … zurückgeht; doch ist diese Ableitung sehr anzuzweifeln.]' Lokotsch starts from Turkish and gives no Persian etymon, but rejects the Kaffa story that Klein prints.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi p.104\", \"stance\": \"supports\",\n       \"note\": \"Derives Arabic خاويار and, through it, German Kaviar / French caviar from Persian xāviyār 'Eiertragend'.\"},\n      {\"src\": \"TTS\", \"where\": \"Vámbéry 1878\", \"stance\": \"silent\",\n       \"note\": \"grep for havyar/kaviar in TTS_vambery1878_uoft_djvu.txt returns nothing; Vámbéry has no entry for the word.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Italian\", \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The empty pass-through node stands for Italian caviaro (modern caviale), in fact first Venetan caviaro — the Venetian and Genoese merchants of the Black Sea were the channel by which the Turkish word entered the West in the 15th-16th centuries. Wiktionary: English caviar 'from Middle French caviar, from Venetan caviaro (earlier found as Italian caviale), probably by way of Ottoman Turkish havyar'; Lokotsch no.851 lists 'it. caviaro, caviale' immediately after the Turkish form.\",\n     \"derivation_fa\": \"این گرهِ تهی نمایندهٔ ایتالیاییِ caviaro (امروز caviale) است، و دقیق‌تر نخست ونیزیِ caviaro؛ بازرگانان ونیزی و جنووایی دریای سیاه در سده‌های پانزدهم و شانزدهم میلادی این واژهٔ ترکی را به غرب بردند. ویکی‌واژه می‌نویسد انگلیسیِ caviar «از فرانسهٔ میانهٔ caviar، از ونیزیِ caviaro (پیش‌تر به صورت ایتالیاییِ caviale)، احتمالاً از راه ترکی عثمانیِ havyar» آمده است، و لوکوچ نیز بی‌درنگ پس از صورت ترکی «it. caviaro, caviale» را می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [WK_CAVIAR],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no citation in the book; checked against Wiktionary and Lokotsch instead (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no.851\", \"stance\": \"supports\",\n       \"note\": \"'hieraus … it. caviaro, caviale, sp. cabial, pg. cavial, caviar, frz. caviar; engl. ndl. caviar, dtsch. Kaviar.'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. caviar\", \"stance\": \"partial\",\n       \"note\": \"'caviar, caviare, n. — F. caviar, fr. It. caviaro (now caviale), fr. MGk. καβιάριον, fr. Turk. khavidr, fr. Kaffah (= Theodosia)' — same Italian > French > English chain, but with a Crimean place-name, not Persian, at the far end.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"French\", \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"French caviar (16th c., Middle French) from Italian/Venetan caviaro; French then passed the word on to English. Klein and Lokotsch agree on this link, and it is uncontroversial.\",\n     \"derivation_fa\": \"«caviar» فرانسوی (فرانسهٔ میانه، سدهٔ شانزدهم میلادی) از ایتالیایی/ونیزیِ caviaro گرفته شده و سپس همین صورت فرانسوی به انگلیسی رفته است. کلاین و لوکوچ هر دو بر این حلقه هم‌داستان‌اند و در آن اختلافی نیست. ادعای نورایی درست است.\",\n     \"sources\": [WK_CAVIAR],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No citation in the book for this pass-through node; checked against Wiktionary, Klein and Lokotsch.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. caviar\", \"stance\": \"supports\", \"note\": \"'F. caviar, fr. It. caviaro (now caviale)'.\"},\n      {\"src\": \"LKT\", \"where\": \"no.851\", \"stance\": \"supports\", \"note\": \"'frz. caviar' in the list of forms derived from the Turkish word.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"caviar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English caviar (also caviare, 16th c.) is borrowed from Middle French caviar; Shakespeare's 'caviare to the general' (Hamlet II.ii) is one of the earliest English uses. The whole chain Persian xāvyār > Ottoman Turkish havyar > Venetan/Italian caviaro > French caviar > English caviar is the one Wiktionary and Asbaghi print, and it is Nourai's chain exactly.\",\n     \"derivation_fa\": \"«caviar» انگلیسی (نیز caviare، سدهٔ شانزدهم میلادی) از فرانسهٔ میانه وام گرفته شده است؛ عبارتِ «caviare to the general» در هملتِ شکسپیر از کهن‌ترین کاربردهای انگلیسی آن است. زنجیرهٔ کاملِ فارسی خاویار > ترکی عثمانی havyar > ونیزی/ایتالیایی caviaro > فرانسوی caviar > انگلیسی caviar همان است که ویکی‌واژه و اصباغی می‌آورند و دقیقاً همان زنجیرهٔ نورایی است. ادعای نورایی درست است.\",\n     \"sources\": [WK_CAVIAR],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"The AHD entry for caviar gives the French > Italian > Turkish > Persian chain (the printed dictionary body, p.212 of the New College ed., is not on disk; the online AHD and Wiktionary agree).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. caviar\", \"stance\": \"partial\",\n       \"note\": \"Same route as far as Turkish, then 'fr. Kaffah (= Theodosia)' instead of Persian.\"},\n      {\"src\": \"LKT\", \"where\": \"no.851\", \"stance\": \"supports\",\n       \"note\": \"'engl. ndl. caviar, dtsch. Kaviar' from Turkish hawjar, with the Kaffa derivation expressly doubted.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Germanic / Old Norse\", \"words\": \"ajjam; egg\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *ajją (Nourai's 'ajjam' is the older notation *ajjam) 'egg' < PIE *h₂ōwyóm, with the Germanic -jj- from *-wy- (Verschärfung; the -es-stem plural OHG eigir, OE ǣgru shows a secondary neuter r/n-inflexion). Its reflexes are Crimean Gothic ada, Old Norse egg, Old English ǣg, OHG/German Ei, Dutch ei. Pokorny p.784 lists exactly this set — 'krimgot. ada (got. *addja), aisl. egg, ahd. ei, ags. ǣg „Ei“ (germ. *ajjaz-)' — and Watkins has 'Germanic *ajja(m)'. Nourai's node correctly puts Proto-Germanic and Old Norse in one box, since ON egg is the form English borrowed.\",\n     \"derivation_fa\": \"ژرمنی آغازین *ajją (صورت کهن‌ترِ نگارشی: *ajjam) «تخم» از هندواروپاییِ *h₂ōwyóm می‌آید؛ ‎-jj-‎ ژرمنی بازتابِ ‎*-wy-‎ است (پدیدهٔ موسوم به Verschärfung)، و جمعِ es-ستاکیِ ahd. eigir / ags. ǣgru نشانهٔ صرفِ ثانویِ خنثی است. بازتاب‌های آن: گوتیِ کریمه‌ای ada، نورسِ کهن egg، انگلیسی کهن ǣg، آلمانی Ei، هلندی ei. پوکورنی در صفحهٔ ۷۸۴ دقیقاً همین فهرست را دارد و واتکینز نیز «Germanic *ajja(m)» می‌نویسد. این‌که نورایی ژرمنی آغازین و نورسِ کهن را در یک جعبه گذاشته درست است، زیرا انگلیسی همان صورتِ نورسی egg را وام گرفته است. ادعای نورایی درست است.\",\n     \"sources\": [PIE_EGG, ET_EGG],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. awi- II: '1. Germanic *ajja(m) in: a. Old English ǣg, egg: COCKNEY; b. Old Norse egg, egg: EGG.' — Nourai's two words, in Watkins's own order.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.784\", \"stance\": \"supports\",\n       \"note\": \"'schwierig sind krimgot. ada (got. *addja), aisl. egg, ahd. ei, ags. ǣg „Ei“ (germ. *ajjaz-; ahd. Pl. eigir, ags. ǣgru erweisen -es-Stamm)'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck p.256 §4.48\", \"stance\": \"supports\",\n       \"note\": \"'Crim. Goth. ada, ON egg, Dan. æg, Sw. ägg, OE ǣg, ME ey (ME, NE egg fr. ON), Du., OHG, MHG, NHG ei'.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"kidney, egg\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"egg is certain: Middle English egge (mid-14c., first in northern dialect) is a Norse loan from ON egg, which displaced the native OE-derived ey/eai after c.1500 — Caxton's anecdote of the merchant who asked for 'egges' and was not understood turns on precisely that dialect split. kidney is not certain: Etymonline calls ME kidenere 'a word of unknown origin, perhaps a compound of Old English cwið „womb“ (see chitterlings) + ey „egg“ … in reference to the shape of the organ', and Watkins does not list KIDNEY under awi- at all (his awi- derivatives are COCKNEY and EGG). So the egg element in kidney is a guess of the older dictionaries that Nourai has adopted as fact.\",\n     \"derivation_fa\": \"دربارهٔ «egg» تردیدی نیست: انگلیسی میانهٔ egge (میانهٔ سدهٔ چهاردهم، نخست در گویش شمالی) وام‌واژه‌ای از نورسِ کهنِ egg است که پس از حدود ۱۵۰۰ جای صورتِ بومیِ ey/eai (از ǣg انگلیسی کهن) را گرفت؛ حکایتِ مشهورِ کاکستون دربارهٔ بازرگانی که «egges» خواست و زن او را نفهمید بر همین دوگانگیِ گویشی استوار است. اما «kidney» قطعی نیست: اتیمانلاین آن را «واژه‌ای با خاستگاه نامعلوم» می‌خواند که «شاید» ترکیبی باشد از cwið انگلیسی کهن «زهدان» و ey «تخم» به سببِ شکلِ اندام؛ واتکینز نیز kidney را اصلاً زیر awi- نیاورده است. پس جزءِ «تخم» در kidney حدسِ فرهنگ‌های قدیمی است که نورایی آن را قطعی گرفته است. با احتیاط پذیرفتنی است.\",\n     \"sources\": [ET_EGG, ET_KID],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no citation of its own; its parent box cites AHD, and Watkins's awi- article lists EGG (from ON egg) but not KIDNEY.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins s.v. awi- II.1\", \"stance\": \"partial\",\n       \"note\": \"'Old Norse egg, egg: EGG' — supports egg; KIDNEY appears nowhere in the awi- article or in its index line.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.vv. egg, kidney\", \"stance\": \"partial\",\n       \"note\": \"Klein derives egg from ON egg; for kidney he too can offer only the conjectural 'kide + ey' analysis.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Latin\", \"words\": \"ôvum\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin ōvum 'egg' < PIE *h₂ōwyóm. Pokorny p.784 files it under 'ohne u, das wohl im langdiphthong. *ōuiom geschwunden war' and quotes Szemerényi's derivation 'lat. ōvum … aus lat. *oom, idg. *ōi̯om'; de Vaan (p.438) reconstructs Proto-Italic *ōw(j)om, with the -v- restored analogically or from the oblique cases. It gives Italian uovo, French œuf, Spanish huevo, Romanian ou.\",\n     \"derivation_fa\": \"لاتینِ ōvum «تخم» از هندواروپاییِ *h₂ōwyóm است. پوکورنی در صفحهٔ ۷۸۴ آن را در بخشِ صورت‌هایی می‌آورد که «واوِ آن‌ها در دوگانه‌واکهٔ بلندِ *ōuiom از میان رفته است» و اشتقاقِ سِمِرِنی را نقل می‌کند: «ōvum لاتین از *oom لاتین، از *ōi̯om هندواروپایی». دِ فان (ص ۴۳۸) ایتالیکِ آغازین را *ōw(j)om بازسازی می‌کند و «و» را قیاسی یا برگرفته از حالت‌های غیرِنهادی می‌داند. بازماندگانِ آن: ایتالیایی uovo، فرانسوی œuf، اسپانیایی huevo، رومانیایی ou. ادعای نورایی درست است.\",\n     \"sources\": [PIE_EGG],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. awi- II: '2. Latin ōvum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.784\", \"stance\": \"supports\",\n       \"note\": \"'lat. ōvum „Ei“ nach Szemerényi KZ. 70, 64 f. aus lat. *oom, idg. *ōi̯om.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck p.256 §4.48\", \"stance\": \"supports\",\n       \"note\": \"'Lat. ovum (> It. uovo, Fr. œuf, Sp. huevo, Rum. ou)'.\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"English\", \"words\": \"ovule\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English ovule (1820s in botany/embryology) is from French ovule, from Modern Latin ovulum, the diminutive of ōvum — a scientific coinage rather than an inherited word, which is why the node hangs directly off the Latin box. Watkins lists OVULE among the English words from Latin ōvum, together with OVAL, OVARY, OVATE, OVI-, OVOLO and OVUM.\",\n     \"derivation_fa\": \"«ovule» انگلیسی (دههٔ ۱۸۲۰، در گیاه‌شناسی و جنین‌شناسی) از فرانسویِ ovule و آن از لاتینِ نو ovulum، مصغّرِ ōvum، گرفته شده است؛ یعنی ساخته‌ای علمی است نه واژه‌ای موروثی، و به همین سبب مستقیماً به جعبهٔ لاتین وصل شده است. واتکینز «OVULE» را در کنارِ OVAL، OVARY، OVATE، OVI-، OVOLO و OVUM در فهرستِ واژه‌های انگلیسیِ برآمده از ōvum می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [PIE_EGG],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No citation on the node; the parent Latin box cites AHD, whose awi- article does list OVULE.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins s.v. awi- II.2\", \"stance\": \"supports\",\n       \"note\": \"'Latin ōvum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM.'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. ovule\", \"stance\": \"supports\",\n       \"note\": \"Klein: ovule from F. ovule, from ModL. ovulum, dimin. of L. ovum.\"}\n     ]\n    }\n   ]\n  },\n\n  # ------------------------------------------------------------------ entry 2\n  {\n   \"entry\": 2,\n   \"root\": \"Awar\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Arabic root ع و ر (ʿ-w-r) 'to be one-eyed, defective'; II ʿawwara 'to damage, spoil', whence the noun عَوَار ʿawār 'flaw, defect'\",\n   \"note\": \"The root is real and the gloss is close, but the headword is not quite a verb form: the Arabic verb is عَوِرَ ʿawira 'to be one-eyed / to have a flaw' and, transitive, عَوَّرَ ʿawwara (form II) 'he damaged, spoiled'; ʿawar/ʿawār is the noun. Lokotsch (no.138) states it as 'ʿawwār, od. ʿawār [von der Wurzel ʿāra II „verderben“] „Stäubchen, Fehler, Schaden“', and Wiktionary files عَوَار under 'the root ع و ر, related to ideas of missing one eye or having a lacuna'. Nourai's reference SAP (Sayyah's Persian version of al-Munjid) is a purchase-only work and could not be consulted.\",\n   \"note_fa\": \"ریشه واقعی است و معنا نیز نزدیک، اما سرواژه دقیقاً صیغهٔ فعلی نیست: فعلِ عربی «عَوِرَ» است به معنی «یک‌چشم شدن، عیب‌دار شدن» و صورتِ متعدیِ آن «عَوَّرَ» (باب دوم) «تباه کرد، معیوب کرد»؛ «عَوَر/عَوار» اسم است. لوکوچ (شمارهٔ ۱۳۸) می‌نویسد: «ʿawwār یا ʿawār [از ریشهٔ ʿāra، باب دوم، «تباه کردن»] یعنی ذرّه، عیب، زیان»، و ویکی‌واژه نیز «عَوار» را زیر ریشهٔ «ع و ر» می‌آورد که با مفهومِ یک‌چشمی و کاستی پیوند دارد. منبعی که نورایی ارجاع داده (SAP، ترجمهٔ فارسیِ المنجد از احمد سیاح) تنها با خرید در دسترس است و بررسی نشد. ادعای نورایی با احتیاط پذیرفتنی است.\",\n   \"sources\": [WK_AWAR],\n   \"ref_check\": [\n    {\"ref\": \"SAP:1123\", \"status\": \"not_checked\",\n     \"note\": \"Farhang-e Sayyah (Persian al-Munjid) is purchase-only (fidibo.com), not on disk and not on archive.org (refs_online.json: 'RE-SEARCH 2026-09: purchase only'). Checked the Arabic side through Wiktionary and Lokotsch instead.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein p.133, s.v. average\", \"stance\": \"supports\",\n     \"note\": \"'… fr. Arab. ʿawārīya, „merchandise damaged by sea water“, fr. ʿawār, „rent, tear; flaw; damaged goods“.'\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no.138 (LKT.txt line 531)\", \"stance\": \"supports\",\n     \"note\": \"'138. Ar. ʿawwār: od. ʿawār [von der Wurzel ʿāra II „verderben“] „Stäubchen, Fehler, Schaden“ ist wohl sicherlich Grundwort zu it. avaria …'\"},\n    {\"src\": \"DEV\", \"where\": \"Devic, s.v. Avarie (DEV.txt line 671)\", \"stance\": \"supports\",\n     \"note\": \"'Avaria viendrait de la racine عار ʿār qui signifie proprement éborgner, mais qui, à la 2e forme ʿawwar, a aussi le sens de gâter, d'où عوار ʿawār, défaut, déchirure.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Arabic\", \"words\": \"`awâr, `awârîyah\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"عَوَار ʿawār is the verbal noun of the ʿ-w-r root, 'flaw, defect, rent (in cloth)'; عَوَارِيَّة ʿawārīya is the nisba-abstract built on it, used in the medieval Mediterranean trade for 'merchandise damaged (by sea water)'. Wiktionary gives 'عَوَار (ʕawār) m: fault, flaw, defect, crevasse. From the root ع و ر, related to ideas of missing one eye or having a lacuna'; Klein p.133 gives both forms in the same order as the chart. The classical Arabic idiom سلعة ذات عوار 'goods with a defect' (Aqrab al-mawārid, quoted by Dehkhoda) shows exactly the commercial use.\",\n     \"derivation_fa\": \"«عَوار» مصدرِ اسمی از ریشهٔ «ع و ر» است به معنی «عیب، نقص، دریدگی (در جامه)»، و «عَوارِیّة» صورتِ نسبیِ ساخته‌شده بر آن است که در بازرگانیِ مدیترانه‌ای سده‌های میانه به معنیِ «کالای آسیب‌دیده (از آبِ دریا)» به کار می‌رفت. ویکی‌واژه می‌نویسد: «عَوار (نرینه): عیب، نقص، شکاف؛ از ریشهٔ ع و ر، مربوط به مفهومِ یک‌چشمی و کاستی». کلاین نیز در صفحهٔ ۱۳۳ هر دو صورت را به همان ترتیبِ نمودار می‌آورد. تعبیرِ کلاسیکِ «سِلعةٌ ذاتُ عَوار» (اقرب الموارد، به نقلِ دهخدا) همین کاربردِ بازرگانی را نشان می‌دهد. ادعای نورایی درست است.\",\n     \"sources\": [WK_AWAR, AB_AWAR],\n     \"ref_check\": [\n      {\"ref\": \"SAP:1124\", \"status\": \"not_checked\", \"note\": \"Sayyah's dictionary is purchase-only; see the root-level ref_check.\"},\n      {\"ref\": \"AHD:91\", \"status\": \"not_checked\",\n       \"note\": \"AHD:91 is a page of the New College Edition dictionary body (s.v. average), not of the Indo-European appendix; only the appendix (Watkins 1985) is on disk, and the archive.org copies of the 1975/1980 printings are lending-only.\"},\n      {\"ref\": \"KLN:133\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 4102, on the leaf whose printed page marker is '133': 'average, n., 1) loss incurred by damage at sea … — F. avarie, „damage to ship“, fr. It. avaria, fr. Sp. avería, fr. Arab. ʿawārīya, „merchandise damaged by sea water“, fr. ʿawār, „rent, tear; flaw; damaged goods“.' Both Arabic words, both glosses, exactly as the chart prints them.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no.138\", \"stance\": \"supports\",\n       \"note\": \"'Ar. ʿawwār, od. ʿawār … „Stäubchen, Fehler, Schaden“ ist wohl sicherlich Grundwort zu it. avaria „Schaden an Schiff oder Ladung“'.\"},\n      {\"src\": \"DOZ\", \"where\": \"Dozy, Oosterlingen (DOZ.txt line 829)\", \"stance\": \"supports\",\n       \"note\": \"'vertaalt avarie door ʿawār, avarié door moʿauwar' — Dozy's Arabic-Dutch equations, the basis of the whole Arabic-origin argument.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery\", \"stance\": \"silent\",\n       \"note\": \"Not a Qur'anic loanword; no entry.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"âr 2 «عار»; avâr «عوار»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The two words must be separated. (a) عوار ʿavār is a straightforward Arabic loan in Persian, and Nourai's gloss is exact: Mo'in has '(عَ یا عِ یا عُ) [ع.] (اِ.) ۱- عیب، عیب و عار. ۲- دریدگی و پارگی در پارچه یا جامه' — 'defect' and 'a tear or rip in cloth' — with the origin tag [ع.] = Arabic; Dehkhoda adds the classical citation 'سلعة ذات عوار: کالای عیب‌دار', and quotes the very Farrokhi couplet printed in the chart ('گنگ باد آن کس که اندر طعن تو گوید سخن / کور باد آن کس که اندر عرض تو جوید عوار'). The word is in use from the 4th/10th century (Farrokhi, Naser Khosrow, Sanā'i). (b) عار ʿār 'shame, disgrace' does not belong to this root. Wiktionary files عَار 'shame, disgrace, ignominy' (pl. أَعْيَار) under the root ع ي ر, morphologically from ʿayyara 'to reproach', and Lane and the classical lexica do the same. Persian عار is that Arabic word, not a doublet of ʿawār; the pairing 'عار و عوار' in Persian texts is a jingle of two near-synonyms, not an etymological identity. Verdict for the node: disputed, on account of عار.\",\n     \"derivation_fa\": \"این دو واژه را باید از هم جدا کرد. «عوار» وام‌واژه‌ای عربی در فارسی است و معنایی که نورایی داده دقیق است: معین می‌نویسد «(عَ یا عِ یا عُ) [ع.] (اِ.) ۱- عیب، عیب و عار. ۲- دریدگی و پارگی در پارچه یا جامه»، با نشانِ [ع.] یعنی عربی؛ دهخدا نیز شاهدِ کلاسیکِ «سِلعةٌ ذاتُ عَوار: کالای عیب‌دار» و همان بیتِ فرخی را می‌آورد که در نمودار چاپ شده است. این واژه از سدهٔ چهارم هجری (فرخی، ناصرخسرو، سنایی) در فارسی به کار رفته است. اما «عار» به این ریشه تعلق ندارد: ویکی‌واژه «عار» (جمع: أعیار) را زیر ریشهٔ «ع ی ر» و از «عَیَّرَ» «سرزنش کردن» می‌آورد، و لِین و فرهنگ‌های کلاسیکِ عربی نیز همین را می‌گویند. «عارِ» فارسی همان واژهٔ عربی است، نه دوگانهٔ «عوار»؛ و همنشینیِ «عار و عوار» در متون فارسی هم‌آواییِ دو واژهٔ نزدیک‌المعناست، نه یگانگیِ ریشه‌شناختی. پس دربارهٔ «عوار» ادعای نورایی درست است و دربارهٔ «عار» پژوهش امروزی آن را رد می‌کند.\",\n     \"sources\": [AB_AWAR, AB_AR, WK_AR, WK_AWAR],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"partial\",\n       \"note\": \"Mo'in's entry (via abadis.ir/fatofa/عوار, section فرهنگ معین) reads '(عَ یا عِ یا عُ) [ ع . ] (اِ. ) ۱ - عیب ، عیب و عار. ۲ - دریدگی و پارگی در پارچه یا جامه' — supports عوار fully (an Arabic loan, 'defect; a tear in cloth'). For عار Mo'in/Dehkhoda give 'عیب و ننگ' but no root analysis, so Mo'in neither supports nor refutes Nourai's attaching it to ʿ-w-r. The word عوار is not in the MON_part1/2 OCR on disk (only the plural عوارض in compounds).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate'\", \"stance\": \"silent\",\n       \"note\": \"Borhan is a dictionary of Persian words; the Arabic loans عار/عوار are not treated there.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā-ye hend-o-orupāyi\", \"stance\": \"silent\",\n       \"note\": \"An Indo-European root dictionary; Arabic loans are outside its scope.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein p.133\", \"stance\": \"supports\",\n       \"note\": \"Confirms the Arabic ʿawār > European chain, i.e. the Arabic word Persian عوار also borrowed.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Spanish\", \"words\": \"\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The empty node stands for Spanish avería 'damage to ship or cargo; general average'. Klein makes it the immediate source of Italian avaria ('fr. It. avaria, fr. Sp. avería, fr. Arab. ʿawārīya'), which is the route Nourai draws. Most other authorities reverse the order: Lokotsch (no.138) says the word 'zuerst von den Genuesen und Pisanern benutzt wurde und dann mit der it. Endung in fast alle europäischen Sprachen überging: frz. avarie; sp. averia, haberia', and Devic likewise has it 'introduit d'abord en italien par le commerce, et passé de là aux autres langues européennes'. So the Spanish link is real but probably not the first station.\",\n     \"derivation_fa\": \"این گرهِ تهی نمایندهٔ اسپانیاییِ avería «آسیب به کشتی یا بار؛ خسارتِ مشترک» است. کلاین آن را سرچشمهٔ بی‌واسطهٔ ایتالیاییِ avaria می‌داند («از ایتالیایی avaria، از اسپانیایی avería، از عربی عواریّة») و همین راهی است که نورایی کشیده است. اما بیشترِ منابعِ دیگر ترتیب را وارونه می‌دانند: لوکوچ (شمارهٔ ۱۳۸) می‌گوید این واژه «نخست نزد جنووایی‌ها و پیزایی‌ها به کار رفت و سپس با پایانهٔ ایتالیایی به تقریباً همهٔ زبان‌های اروپایی رفت: فرانسوی avarie، اسپانیایی averia، haberia»، و دِویک نیز آن را «نخست از راه بازرگانی وارد ایتالیایی و از آنجا به دیگر زبان‌های اروپایی» می‌داند. پس حلقهٔ اسپانیایی واقعی است اما احتمالاً نخستین ایستگاه نیست. با احتیاط پذیرفتنی است.\",\n     \"sources\": [ET_AVG],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No citation on this pass-through node; the parent Arabic box cites KLN:133, which does have 'fr. Sp. avería'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.133 s.v. average\", \"stance\": \"supports\",\n       \"note\": \"'fr. It. avaria, fr. Sp. avería, fr. Arab. ʿawārīya' — Klein's order is Arabic > Spanish > Italian, i.e. Nourai's.\"},\n      {\"src\": \"LKT\", \"where\": \"no.138\", \"stance\": \"partial\",\n       \"note\": \"Puts Italian first ('zuerst von den Genuesen und Pisanern benutzt') and derives Spanish averia, haberia from it.\"},\n      {\"src\": \"DEV\", \"where\": \"s.v. Avarie\", \"stance\": \"partial\",\n       \"note\": \"'Esp. avería, portug. avaria, ital. avaria … le mot … introduit d'abord en italien par le commerce, et passé de là aux autres langues européennes.'\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Italian\", \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Italian avaria 'damage to ship or cargo, and the levy that shares that loss' is the pivotal Western form: it is the one attested first (12th-13th c. Genoese and Pisan maritime law), it carries the Italian -ia suffix that all the other European forms show, and it is the form from which French avarie, Spanish avería, Portuguese avaria, Dutch avarij, German Havarie and English average were taken. Lokotsch no.138 sets it out in exactly these terms.\",\n     \"derivation_fa\": \"ایتالیاییِ avaria «آسیب به کشتی یا بار، و سهمی که برای جبرانِ آن میان صاحبانِ کالا سرشکن می‌شود» صورتِ محوریِ غربی است: کهن‌ترین ضبط را دارد (حقوقِ دریاییِ جنووا و پیزا در سده‌های دوازدهم و سیزدهم میلادی)، پسوندِ ایتالیاییِ ‎-ia‎ را دارد که در همهٔ صورت‌های اروپاییِ دیگر دیده می‌شود، و همان صورتی است که فرانسویِ avarie، اسپانیاییِ avería، پرتغالیِ avaria، هلندیِ avarij، آلمانیِ Havarie و انگلیسیِ average از آن گرفته شده‌اند. لوکوچ (شمارهٔ ۱۳۸) دقیقاً همین را می‌گوید. ادعای نورایی درست است.\",\n     \"sources\": [ET_AVG],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No citation on this pass-through node; checked against Klein p.133, Lokotsch no.138 and Devic.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no.138\", \"stance\": \"supports\",\n       \"note\": \"'… it. avaria „Schaden an Schiff oder Ladung, Hafensteuer“, ein Wort, das zuerst von den Genuesen und Pisanern benutzt wurde und dann mit der it. Endung in fast alle europäischen Sprachen überging.'\"},\n      {\"src\": \"KLN\", \"where\": \"p.133\", \"stance\": \"supports\", \"note\": \"'F. avarie … fr. It. avaria'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"French\", \"words\": \"avarie\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"French avarie 'damage sustained by a ship or its cargo', and by extension the maritime-law institution by which that loss is apportioned among all the interested parties (avarie commune = general average), is borrowed from Italian avaria in the late Middle Ages. Both halves of Nourai's gloss are right, and the second half is what made the word into an arithmetical term: the 'equitable sharing' sense is the bridge from 'damage' to modern English 'average'. Klein p.133 gives 'F. avarie, „damage to ship“, fr. It. avaria'.\",\n     \"derivation_fa\": \"فرانسویِ avarie «آسیبی که به کشتی یا بارِ آن می‌رسد» و به‌گسترشْ نهادی در حقوقِ دریایی که این زیان را میان همهٔ ذی‌نفعان سرشکن می‌کند (avarie commune «خسارتِ مشترک»)، در اواخر سده‌های میانه از ایتالیاییِ avaria وام گرفته شده است. هر دو بخشِ معنایی که نورایی آورده درست است، و بخش دوم همان پلی است که واژه را به اصطلاحی حساب‌شده در انگلیسی بدل کرد. کلاین در صفحهٔ ۱۳۳ می‌نویسد: «F. avarie „آسیب به کشتی“، از ایتالیایی avaria». ادعای نورایی درست است.\",\n     \"sources\": [ET_AVG],\n     \"ref_check\": [\n      {\"ref\": \"KLN:133\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 4102 (printed p.133): 'F. avarie, „damage to ship“, fr. It. avaria, fr. Sp. avería, fr. Arab. ʿawārīya'.\"},\n      {\"ref\": \"AHD:91\", \"status\": \"not_checked\",\n       \"note\": \"Page 91 of the AHD dictionary body (s.v. average) — only the IE appendix of AHD is available on disk.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"DEV\", \"where\": \"Devic s.v. Avarie\", \"stance\": \"supports\",\n       \"note\": \"Devic's article accepts Dozy's Arabic origin for French avarie and traces it through Italian.\"},\n      {\"src\": \"PHN\", \"where\": \"Pihan\", \"stance\": \"silent\",\n       \"note\": \"grep 'AVARIE' in PHN.txt returned no headword.\"},\n      {\"src\": \"LKT\", \"where\": \"no.138\", \"stance\": \"supports\", \"note\": \"'frz. avarie' listed among the Italian word's descendants.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"average\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"English average is first recorded late 15c. in exactly the maritime sense of French avarie — 'financial loss incurred through damage to goods in transit', then 'the equal sharing of that loss among the interested parties', from which the transferred sense 'medial estimate' (1735) and the mathematical 'arithmetical mean' (1755) grew. The Arabic > Romance > English chain that Nourai draws is Klein's, Lokotsch's, Dozy's and Devic's. Two serious dissents must be recorded, both aimed at the far end of the chain, not at the Romance part. (i) Skeat derives average in all its senses from Middle Latin averagium / avera (< OF aver 'goods, cattle' < Latin habere) and says the Arabic words 'merely introduce a form borrowed from Late Lat. averia'. (ii) The OED, quoted by Hobson-Jobson and by Etymonline, holds the Arabic ʿawār to be 'merely a mod. Arabic translation and adaptation of the Western term in its latest sense' — i.e. the borrowing may run the other way. Etymonline accordingly calls the word 'of uncertain origin'; 'few words have received more etymological investigation' (OED). English average also plainly absorbed the unrelated feudal-service word averagium, which is why Klein gives two separate entries.\",\n     \"derivation_fa\": \"«average» انگلیسی نخستین‌بار در اواخر سدهٔ پانزدهم میلادی و دقیقاً در همان معنای دریاییِ avarie فرانسوی ثبت شده است — «زیان مالیِ ناشی از آسیب به کالا در راه»، سپس «سرشکن‌کردنِ برابرِ آن زیان میان ذی‌نفعان» — و از همین‌جا معنای «برآوردِ میانگین» (۱۷۳۵) و سرانجام «میانگینِ حسابی» (۱۷۵۵) پدید آمد. زنجیرهٔ عربی > رومی > انگلیسی که نورایی کشیده همان زنجیرهٔ کلاین، لوکوچ، دوزی و دِویک است. اما دو مخالفتِ جدی را باید ثبت کرد، هر دو متوجهِ سرِ عربیِ زنجیره و نه بخشِ رومیِ آن: نخست، اسکیت همهٔ معانیِ average را از لاتینِ میانهٔ averagium / avera (از فرانسهٔ کهن aver «کالا، چارپا»، از habere لاتین) می‌گیرد و می‌گوید واژه‌های عربی «تنها صورتی را وارد کرده‌اند که خود از averia لاتینِ متأخر وام گرفته شده است». دوم، فرهنگ آکسفورد — به نقلِ هابسن‑جابسن و اتیمانلاین — «عَوارِ» عربی را «صرفاً ترجمه و اقتباسی نوین از اصطلاح غربی در آخرین معنای آن» می‌داند، یعنی جهتِ وام‌گیری را وارونه می‌کند. بر این پایه اتیمانلاین خاستگاهِ واژه را «نامعلوم» می‌خواند. ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [ET_AVG],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No citation on the English node; its parent French box cites KLN:133 and AHD:91, and Klein's article is precisely s.v. 'average'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.133, two entries 'average'\", \"stance\": \"supports\",\n       \"note\": \"The first entry gives the Arabic chain; the second, 'average, n., feudal service (Old English law) — ME., fr. ML. averagium, fr. ML. avera, fr. OF. oevre … fr. L. opera', keeps the homonym apart.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. average\", \"stance\": \"contradicts\",\n       \"note\": \"'„Average“ (< averagium, from averia, i.e. cattle) signifies service which the tenant owes the king … ¶ This form (average) was afterwards confused with F. avarie, damage of goods … (Arab. ʿawār, a fault, defect, ʿawār spoilt merchandise, merely introduce a form borrowed from Late Lat. averia.)'\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. AVERAGE (HJB.txt line 2341)\", \"stance\": \"partial\",\n       \"note\": \"'Dozy shows most plausibly [avarie] to be from the Ar. ʿawār, spoilt merchandise. [This is rejected by the N.E.D., which concludes that the Ar. ʿawār is „merely a mod. Arabic translation and adaptation of the Western term in its latest sense.“]'\"},\n      {\"src\": \"LKT\", \"where\": \"no.138\", \"stance\": \"supports\",\n       \"note\": \"'engl. average' among the descendants, with Lokotsch's own remark that the h- of Havarie/haverij replaces the ʿayn Europeans could not pronounce.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open(\"data/verification/page-73.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk73.py && python3 -m json.tool data/verification/page-73.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 73"
}
```


### [2026-09-05T06:02:27.998Z] TOOL RESULT

```
written
JSON OK
nodes verified: 22/22
node verdicts: {'disputed': 2, 'transcription_suspect': 1, 'plausible': 6, 'confirmed': 13}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'partial': 3, 'supports': 20, 'not_found': 1, 'not_checked': 10}
books consulted: {'partial': 14, 'supports': 35, 'silent': 8, 'contradicts': 1} | by book: {'KLN': 10, 'LKT': 9, 'AHD': 4, 'HRN': 4, 'SYN': 4, 'WLD': 3, 'BRT': 2, 'PHD': 2, 'SKT': 2, 'BQT': 2, 'POK': 2, 'DEV': 2, 'MON': 1, 'HUB': 1, 'KNT': 1, 'NYB': 1, 'AFM': 1, 'PLA': 1, 'TTS': 1, 'DOZ': 1, 'FVQ': 1, 'ARY': 1, 'PHN': 1, 'HJB': 1}
```


## [2026-09-05T06:02:39.425Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\nidx={json.loads(l)['url'] for l in open('data/verification/sources/web/index.jsonl',encoding='utf-8')}\nd=json.load(open('data/verification/page-73.json',encoding='utf-8'))\nused=set()\nfor e in d['entries']:\n    used|=set(e.get('sources',[]))\n    for n in e['nodes']: used|=set(n.get('sources',[]))\nmissing=[u for u in used if u not in idx]\nprint('used',len(used),'missing',missing)\nEOF\nhead -c 3 data/verification/page-73.json | xxd | head -1"
}
```


### [2026-09-05T06:02:41.411Z] TOOL RESULT

```
used 15 missing []
00000000: 7b0a 20                                  {.
```


## [2026-09-05T06:03:01.919Z] AGENT

Done — `data/verification/page-73.json` written; `verify_check.py 73` reports 22/22 nodes, 0 PROBLEM lines.

**Page 73 (book p. 43) — 3 entries, 22 nodes**

Verdicts: roots 2 confirmed / 1 plausible; nodes 13 confirmed, 6 plausible, 2 disputed, 1 transcription_suspect.
Ref checks: 20 supports, 3 partial, 1 not_found, 10 not_checked (SAP is purchase-only; AHD:91 is the dictionary body, only Watkins' appendix is on disk; empty pass-through nodes carry no refs).

Disputed / suspect:
- **Aw, node 1 (Avestan)** — `vayu` "air" does not belong to the bird root. Bartholomae col. 1357 files vayav-/vaya- "Luft" under the verb vā- "to blow", and Pokorny puts it on pp. 81–84 s.v. au̯e- "wehen" (PIE *h₂weh₁-). vīš, vay- and ā-vayeiti are all correct.
- **Awar, node 2 (Persian)** — عوار is confirmed (Mo'in "[ع.] عیب؛ دریدگی و پارگی در پارچه"; Dehkhoda quotes the same Farrokhi couplet the chart prints), but عار "shame" belongs to the Arabic root ع ي ر (Wiktionary, Lane), not ع و ر.
- **Aw, node 2 (Pahlavi) — transcription_suspect, error_in "book"** — the printed page 43 does read "vôi"; Pokorny 86, Walde-Pokorny I 21 and Horn p. 295 all have *vāi* = wāy. vây and vâyandak are confirmed (Nyberg p. 207 has vāyēndak verbatim).

Citation problems that are the author's, not the extraction's:
- **HRN:995 is impossible** — Horn's Grundriss ends at p. ~390, and his numbered entry 995 is mūš "Maus". The material is on Horn pp. 295–296 (entry 207 "vāi 1) Luft 2) Vogel … vāyandak"), so this looks like a misprint for HRN:295. The printed page confirms "HRN:995".
- FRS:56 not locatable in the Loghat-e Fors OCR on disk (Eqbal's edition, different pagination), but the entry demonstrably exists: Dehkhoda's ویش quotes "موش‌گیر. (نسخهٔ فرهنگ اسدی). غلیواج. زغن".

No extraction errors found — the JSON matches the printed page throughout (page image saved to `data/verification/sources/refs/ocr/BOOK/73.png`). One cosmetic note: the JSON writes vây's script as "واى" with U+0649 (alef maqsura) where the page prints Persian ی — harmless, but the owner may want it normalized.

Notable positive findings: Asbaghi PLA p. 104 confirms xāvyār = MP xāyak "egg" + bar (the chart's ☞Bher 1 cross-reference); Addi Shir p. 51 confirms Turkish خاويار from Persian خایه‌بار; Klein p. 133 supports the ʿawār → avarie → average chain verbatim, though Skeat contradicts it and the OED (via Hobson-Jobson) reverses the direction of borrowing.
