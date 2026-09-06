# Verification process log — verify-page-216


## [2026-09-06T15:07:15.146Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 216 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-216.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-216.json. Write /home/sfmqrb/git/rishe/data/verification/page-216.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 216` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:07:16.682Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:07:17.391Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:07:17.406Z] TOOL RESULT

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


## [2026-09-06T15:07:17.709Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-216.txt"
}
```


### [2026-09-06T15:07:17.734Z] TOOL RESULT

```
1	=== PDF page 216 (book page 186) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwher : warm  (refs POK:493)
4	#1 (parent #0) [Avestan] refs=POK:493; KNT:183 | garema : warm
5	  #2 (parent #1) [Persian] refs=HRN:203; BQT:1800 | garm «گرم» : warm | extra: گرما ، گرمابه
6	#3 (parent #0) [Old Persian] refs=POK:493 | garma : warm ; garma-pada : name of a (hot) month
7	  #4 (parent #3) [Sogdian] refs=SOD:169 | grm : warm
8	#5 (parent #0) [Greek] refs=AHD | thermos : warm, heat
9	  #6 (parent #5) [French] refs=None | 
10	    #7 (parent #6) [Persian] refs=MON:1072 |  | extra: ترموس ، ترمومتر ، ترموستات
11	  #8 (parent #5) [English] refs=AHD | thermometer, thermostat, thermos
12	#9 (parent #0) [Latin] refs=AHD | for-nus, fornâx : oven ; for-ceps : fire tongs ☞Kap
13	  #10 (parent #9) [English] refs=None | furnace ; forceps
14	  #11 (parent #9) [French] refs=PHN:187 | four : oven | NOTE: This word has possibly reached French through Arabic.
15	    #12 (parent #11) [Persian] refs=VOP:246; FVF:485,497; MON:2527,2529; PHN:187 | fer «فِر ٢» : oven ; forn «فُرن» : a clay oven for baking bread ; fârîneh «فارینه ( فرنی ، فُرنیه )» : a kind of thick bread | NOTE: There is an indication that Latin word "forn:oven" reached (old) Persian and then found its way back in Europe (France) through Arabic.
16	--- entry 1 ---
17	ROOT [Indo-European] Gwhi, Guhâ, Guhei : thread, string  (refs POK:481,489; AHD)
18	#1 (parent #0) [Avestan] refs=POK:481 | žyâ 2 : bow string
19	  #2 (parent #1) [Persian] refs=HRN:150; BQT:1046 | zeh 1 «زه ١» : bow string
20	#3 (parent #0) [Latin] refs=POK:489; AHD | filum : thread
21	  #4 (parent #3) [French] refs=AHD | fil : thread (used to tie papers) ; filet : a strip of boneless meat
22	    #5 (parent #4) [Persian] refs=MON:2599 | fîleh «فیله» : filet
23	    #6 (parent #4) [English] refs=AHD | file, filament, filet
24	  #7 (parent #3) [Italian] refs=AHD | pro-filare : to draw an outline
25	    #8 (parent #7) [French] refs=None | 
26	      #9 (parent #8) [Persian] refs=VOP:117 | profîl «پروفیل» : shaped hollow metal extrusions
27	    #10 (parent #7) [English] refs=AHD | profile
28	
```


## [2026-09-06T15:07:21.732Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-216.json",
 "description": "Read source JSON page 216"
}
```


### [2026-09-06T15:07:21.769Z] TOOL RESULT

```
{
  "pdf_page": 216,
  "book_page": 186,
  "entries": [
    {
      "root": {
        "name": "Gwher",
        "lang": "Indo-European",
        "refs": "POK:493",
        "gloss": "warm"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:493; KNT:183",
          "words": [
            {"translit": "garema", "gloss": "warm", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:203; BQT:1800",
          "words": [
            {"translit": "garm", "gloss": "warm", "script": "گرم"}
          ],
          "script_extra": "گرما ، گرمابه",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:493",
          "words": [
            {"translit": "garma", "gloss": "warm", "script": null},
            {"translit": "garma-pada", "gloss": "name of a (hot) month", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Sogdian",
          "refs": "SOD:169",
          "words": [
            {"translit": "grm", "gloss": "warm", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "thermos", "gloss": "warm, heat", "script": null}
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
          "lang": "Persian",
          "refs": "MON:1072",
          "words": [],
          "script_extra": "ترموس ، ترمومتر ، ترموستات",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "thermometer, thermostat, thermos", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "for-nus, fornâx", "gloss": "oven", "script": null},
            {"translit": "for-ceps", "gloss": "fire tongs", "script": null, "see": ["Kap"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "furnace", "gloss": null, "script": null},
            {"translit": "forceps", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "French",
          "refs": "PHN:187",
          "words": [
            {"translit": "four", "gloss": "oven", "script": null}
          ],
          "script_extra": null,
          "note": "This word has possibly reached French through Arabic.",
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "VOP:246; FVF:485,497; MON:2527,2529; PHN:187",
          "words": [
            {"translit": "fer", "gloss": "oven", "script": "فِر ٢"},
            {"translit": "forn", "gloss": "a clay oven for baking bread", "script": "فُرن"},
            {"translit": "fârîneh", "gloss": "a kind of thick bread", "script": "فارینه ( فرنی ، فُرنیه )"}
          ],
          "script_extra": null,
          "note": "There is an indication that Latin word \"forn:oven\" reached (old) Persian and then found its way back in Europe (France) through Arabic.",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gwhi, Guhâ, Guhei",
        "lang": "Indo-European",
        "refs": "POK:481,489; AHD",
        "gloss": "thread, string"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:481",
          "words": [
            {"translit": "žyâ 2", "gloss": "bow string", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:150; BQT:1046",
          "words": [
            {"translit": "zeh 1", "gloss": "bow string", "script": "زه ١"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:489; AHD",
          "words": [
            {"translit": "filum", "gloss": "thread", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "fil", "gloss": "thread (used to tie papers)", "script": null},
            {"translit": "filet", "gloss": "a strip of boneless meat", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:2599",
          "words": [
            {"translit": "fîleh", "gloss": "filet", "script": "فیله"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "file, filament, filet", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "Italian",
          "refs": "AHD",
          "words": [
            {"translit": "pro-filare", "gloss": "to draw an outline", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "VOP:117",
          "words": [
            {"translit": "profîl", "gloss": "shaped hollow metal extrusions", "script": "پروفیل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "profile", "gloss": null, "script": null}
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


## [2026-09-06T15:07:24.112Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','HRN','BQT','SOD','AHD','MON','PHN','VOP','FVF','WLD','PHD','NYB','HUB','KLN','SKT','IEC','SYN','BRT','ARY','CHEUNG','FVQ','AFM','PLA','LKT','DEV','LAM','DOZ','WEB','FSD']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:600])\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-06T15:07:25.923Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
CHEUNG MISSING
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start wit
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
```


## [2026-09-06T15:07:30.582Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60"
}
```


## [2026-09-06T15:07:30.595Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,120p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:07:30.645Z] TOOL RESULT

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
```


### [2026-09-06T15:07:30.649Z] TOOL RESULT

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


## [2026-09-06T15:07:35.415Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['POK_full.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for m in re.finditer(r'g[ʷu]?[ʰh]er', t):\n        s=max(0,m.start()-200); print('---',f,m.start()); print(t[s:m.start()+400]); break\nEOF"
}
```


## [2026-09-06T15:07:36.233Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f\"; grep -n \"493\" $f | head -3; wc -c $f; done"
}
```


### [2026-09-06T15:07:37.547Z] TOOL RESULT

```
--- POK_full.txt 38379
suitability ' = Old High German z//" purpose ', preposition Old 
English Old Icelandic ///" to, for '. 

References: WE. I 12, Devoto Mel. Pedersen 224. 
Page(s): 3 

Root / lemma: ad(u)-, ad-ro- {*hegherd) 

English meaning: water current 

Note: 

From Root/ lemma: ang''(h)i-\ "snake, worm' derived Root/ lemma: ak^'a- {more properly 

alci). ek"- 

: "water, river'; Root/ lemma: eghero-: "lake, inner sea'; Root/ lemma: ad(u)-, ad-ro-\ 

"water current': lllyrian Pannonian VN 'Oaspiareg [common alb.- 1 llyrian-Baltic -^^- >-«/-, - 

z\ 

From Root/ lemma: ak^a-^ water, river' nasalized in *a/
```


### [2026-09-06T15:07:40.366Z] TOOL RESULT

```
== POK_01.txt
1628:WP.  II  139  f.,  185  f.,  WH.  I  493  f.
5057:gr.    igs-TTjg    ^Ruderer',    Ersatz    für    *iQSTrjQ   (=  ai.    aritdr-)    wozu   fem 'EgevQicc  ON  erhalten,  egiaaci),  att.  iosTToj  , rudere'  (*€gsT-i(x),  Denominativ)  ,J.- iosTfiög,  PL   igsTf-id    (statt   *6Qfji.iog  =  lat.    remus,    nach    igsTrjg,    Schwyzer  '^ Gr.  Gr.  I  493 2)  , Ruder',   hom.  elgsalrj   (sl-  metr.  Dehnung)  ,das  Rudern'  >''"<' UTTTj^srjyg  , Ruderknecht,  Matrose';   übertragen:  , schwer  arbeitender  Diener' Tievrrjgrjg  ,Fünfdecker';    slyiöa-ogogf   Tgiay-öw-ogogy    ion.   Tgirj-aörT-egog   usw. (die  -o^og-Formen  durch  gr.  Assimihation  von  o  aus  £?);  äh-rjgrjg  ,das  Meer durchrudernd',  dixcp-T^grjg  ,doppelruderig',  Tgirjgrjg  ,Dreidecker';
981836 POK_01.txt
== POK_02.txt
2277:493
2637:vielleicht  mir.  cä(i)d  ,heilig',  wozu  gall.  caddos  ,sanctus'  C.  Gl.L.  V493,  30;
1137861 POK_02.txt
== POK_03.txt
84:lat.  oculus  , Auge'  (ök^^elo-s) ;  atr-öx  ,gräßlich'  (zu  äter,  oben  S.  69),  fer-öx ,wild*  (zu  lat.  ferus,  oben  S.  493),  usw.  (:  gr.  (.iv-toip  ,kurzsichtig',  usw.);
1861:epid.  'fjuirsLtt',  fiidva  ,HälfteO;  lat.  semi-  {semus  späte  Adjektivierung);  ,g^ indekl.'  ,halb,  Hälfte^  wohl  nach  6is;  ahd.   sämi-,   as.   säm--^  vgl.  lat.  ^gnit vivus,  gr.   'fj^d-ßiog,  ahd.  sämi-quecJc,  as.  säm-quick  ,halbtot^ WP.  II  493,  WH.  II  512  f.
1866:WP.  II  493,  Pedersen  Hitt.  185.
1170809 POK_03.txt
== POK_full.txt
11184:References: WP. 11139 f., 185 f., WH. I 493 f. 
27675:£p£Tpa (instead of *£pr||jO(; = Latin remus, after £p£Tr|<;, Schwyzer Gr. Gr. I 493^) " rudder ', 
38221:Page(s): 493 
3971883 POK_full.txt
```


## [2026-09-06T15:07:45.078Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\n# split into entries by \"Root / lemma:\"\nparts=re.split(r'(?=Root / lemma:)', t)\nfor p in parts:\n    m=re.search(r'Page\\(s\\):\\s*(\\d+)', p)\n    if m and m.group(1) in ('493','481','489'):\n        print('=====', p[:60].replace('\\n',' '), '| page', m.group(1), 'len', len(p))\nEOF"
}
```


### [2026-09-06T15:07:48.177Z] TOOL RESULT

```
===== Root / lemma: guet-   Meaning: swelling   Note: (extension f | page 481 len 751
===== Root / lemma: ghuel-   Meaning: to bend, swerve   Material:  | page 489 len 2980
===== Root / lemma: ghuer-   Meaning: wild beast   Material: Gr. G | page 493 len 931
===== Root / lemma: g^heia- : g^hT-     Meaning: vein, sinew   Mat | page 489 len 895
===== Root / lemma: g^hel-   Meaning: to wish   Material: Gr. GsAw | page 489 len 565
===== Root / lemma: g^her-   Meaning: hot, warm   Material: Old In | page 493 len 5106
===== Root / lemma: g''lia, g^ijos   Meaning: sinew   Material: Ol | page 481 len 393
===== Root / lemma: g^is-ti-s: " finger ' derived from zero grade  | page 481 len 324
```


## [2026-09-06T15:07:52.999Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'(?=Root / lemma:)', t)\nfor p in parts:\n    m=re.search(r'Page\\(s\\):\\s*(\\d+)', p)\n    if m and m.group(1) in ('493','481','489'):\n        h=p[:40].replace('\\n',' ')\n        if 'g^her-' in h or 'g^hia' in h or 'g^heia' in h:\n            print('==========',h)\n            print(p)\nEOF"
}
```


### [2026-09-06T15:07:55.024Z] TOOL RESULT

```
========== Root / lemma: g^heia- : g^hT-     Meanin
Root / lemma: g^heia- : g^hT- 



Meaning: vein, sinew 

Material: Cymr. gi-au PI. " nerves, tendons '; 



Lithuanian gija^ Faden im Aufzug eines Gewebes ', Latvian dzija^ filament', PI. threads, 
strings'; 

Old Church Slavic z/-ca "sinew', russ. dial, zfca^ worsted, knit made from spun wool ', 
Serbo-Croatian zTca^ filament, wire, cord, string '; the Balto Slavic-forms could also belong 
to g"ii9-. 

g^hTslo-. 

Armenian y//'sinew, cord'; 

Latin fflum ' filament '; 

Maybe alb. M'thread' a Latin loanword. 

Lithuanian ^ys/a"vein, sinew, midrib, center vein of a leaf, Latvian dzTsIa, dzTksla^yeiVi 
(the nasalization in zemait. g'insla\s secondary). Old Prussian pettegislo^ RiJckenader'; 
but Old Church Slavic zila, russ. zfia, Serbo-Croatian z/'/a etc. "vein, sinew' are neologisms 
to z/-ca, see above. 

References: WP. I 670, 694, WH. I 497 f., Trautmann 87, 90. 
Page(s): 489 


========== Root / lemma: g^her-   Meaning: hot, war
Root / lemma: g^her- 

Meaning: hot, warm 

Material: Old Indie haras-u. 'blaze, glow' (= gr. Qt^oo,, Armenian yie/), ghrna-xx\. "blaze, 

glow, heat' (= Latin fornus. Old Church Slavic gn^n-b), ghrnot/'g\o\NS, shines', gharma-xw. 

"blaze, glow, heat', Avestan garama-^hot', n. "heat, blaze, glow'. Old pers. in garma-pada- 

name of a month, perhaps "* beginning of the heat' (= Latin formus, German M/5/777 "warm'; 

Old Prussian gorme); Note: common Old Indie ^"Z?- >/?-. 



Armenian ye/"" warmth, good weather; \Narxx\\jernum' warm me ',ye/7r7"warm' (= gr. 
Gspfjoc;; perhaps as 'ig"'/7e/'-/77/7-c»s derivative oi men-stem:) Jermn Gen. Jerman lever' (also 
gr. Gsppa f. " warmth ' originally a neuter?); 

thrako-Phrygian germo-^warm' (in many PN: Jokl Eberts Reallex. 10, 142 f., 13, 285, 
292, 294), kappadok. garmia{s) " Stadtname auf der Peutingerschen Tafel ' {a = Indo 
Germanic o); 

Gr. Btpoq n. "summer heat, harvest', Gepofjai "become hot', 0£p|j6(; "warm', Qtp[iaooa 
"oven'; 

also Germ-\n lllyrian PN, as also probably in originally North lllyrian VN German/ 
(Pokorny ZceltPh. 21, 103 ff); alb. Tosc z/arrl\re, heat' (/rfrom rm), gheg. zjarm{: 
9£P|j6(;), ngroh^yNarm' ( *g"hre-as in Old Church Slavic gret/^warm', Latvian gremens 
"pyrosis, heartburn'); alb. ^a/se"burning coal' {*g'^hortia?); 

Maybe alb. grij^ freeze ' : ngroh'warm ' 

Maybe other alb. cognates: 27ey"boil, cook', duplicated zezead]., f. "black, burnt'. 

Also alb. Tosc z/arrl\re, glow, heat, fervour ' : Rumanian ya/'"fire, glow, heat, fervour '. 

Latin formus 'warm' (Festus), fornus, furnus {*g"horno-s), fornax'oven (latter being 
based on a fem. a-stem), forn/x, -ids " dome ' ( *fornicos " having the figure of a stove '); 

Note: 

The shift g(fi)- > d- is of lllyrian alb. origin, hence the common Latin shift d- > /-testifies a 
loanword from lllyrian 



Old Irish fo-geir' warms up, heats up ' etc., bret. gredm. " warmth, heat; courage ' = 
Middle Irish gr/th'sun, heat' {*g"hrtu-s). Middle Irish gorim, guirim^\Narm up, get warm, 
burn', nir. ^o^'heat; brood; ulcer'; cymr. ^c/7"brood', ^OA^brood, pus', bret. gor^ burning 
fire, boil '; Old Irish goml\re' (= Latin fornus); against it is Irish ^0/777 "blue' loanword from 
cymr. ^H7777"dark-(blue)' and this together with abr. uurm\n Uurm-hae/on MH ' aux 
Bourcils bruns ' from Old English wurma ' purple color ' borrowed (Gwynn Hermathena 20, 
63ff.); Old Irish ^c»//f "bitter' ("*the burning taste'), wherefore Old Irish gorte {*g"hortJ§) 
"hunger'; 

Maybe truncated alb. {*g"'horia) ^/ra "hunger', i/za "burning log'. 

Old Norse ggrr{*garwa-), gerr, g0rr{*garwia-) " ready, willing, perfect ', Old High 
German garo^ prepared, ready ', Old English gearu. Modern High German gar. Old Norse 
g0rva. Old High German garawen. Middle High German gerwen^ finish, prepare, make 
ready, tan, convert hide into leather'. Old English ^/e/w5/7 "prepare, concoct, cook'. Old 
Norse gerd {* garwiPo) " fermenting the beer ' (formal indeed = Old High German garawida 
"preparing '), Middle High German gerwe " yeast, filth ', Middle Low German gere^ 
fermentation, stench, dung pool, dirt ', ^e/"©/? "ferment, seethe' are rather after Holthausen 
Wb. of old westn. 102 defined from prefix ga- and *-arwa- > Old Norse p/r"rash, hasty, 
skilful' (above S. 331); 

Old English gyrwe-fenn' morass', gyre' manure', mnl. gore, gore'smoke, smell, odor'. 
Middle Low German gdre'pu66\e, slop', Norwegian dial, gurm'yeast, ordure, food mash'. 
Old Norse gorn. " the half-digested stomach contents ', gjgr {* gerva-) " residuum, sludge ', 
Old English Middle Low German Old High German ^c»/'"crap, muck, manure'; to meaning 
compare above cymr. gor'pus'; 

here probably Old Norse gersta' embitter'. Middle High German garst. Modern High 
German garst/g'spoW; 

about Gothic \/varmjan'\Narm' etc. see though under uer-'cooW; 

Lithuanian garas'vapor; intense desire', Latvian gars\apor, ghost, soul'. Old Prussian 
gorot "stove, hearth', gorme'heat', Latvian garme' warmth ', Old Prussian garewingi 
Mn. "rutting, in heat', Latvian gremens' pyros\s, heartburn'; 

Old Church Slavic gorith, goret/'burn, grejg, gret/'\/\/arm', zeravb " blazing ', pozarb 
"blaze', grbni,' Kessel ' (= Latin fornus), grhn/7o 'os/en', russ. gorn'stove, hearth', poln. 
garn/ec'pot, pan'; further Old Church Slavic gortkb ( *g"'hori-ko-) "bitter' ("*burning of 



taste'; compare above Irish goirt), but sloven, gorgk s\so "warm', Czech horky'\Narr(\\ 
against it Old Czech /7c»/7^y" bitter'; isolated Serbo-Croatian grk, f. ^/Aa 'bitter', compare 
Berneker 232; Old Church Slavic ^OAfo/i. compounds "evil, bad' ('*burning, bitter'), gore 
■blow!' 

g'^hre-ns-o- {due to es-stem g'^hre-nes-): 

Old Indie ghrarhsa-h m. ' solar glow, sunshine, brightness ' = bret. groez, grouez 
{*g"hrenso-) "solar heat', cymr. gwres^heai' (to m^s. Pedersen KG. I 108, ©through the 
influence of /esds.); /"from Old Irish ^/Ts'fire', grJsaid^ fires, stimulates ' probably from 
*ghrenso-, in spite of Thurneysen Gr. 130. 

References: WP. I 687 ff., WH. I 532 ff., Trautmann 79, 102. 
Page(s): 493-495
```


## [2026-09-06T15:08:03.141Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'(?=Root / lemma:)', t)\nfor p in parts:\n    m=re.search(r'Page\\(s\\):\\s*(\\d+)', p)\n    if m and m.group(1) in ('481',):\n        print('==========')\n        print(p)\nEOF"
}
```


### [2026-09-06T15:08:04.758Z] TOOL RESULT

```
==========
Root / lemma: guet- 

Meaning: swelling 

Note: (extension from geu- 'bend'? see there) 

Material: Latin botulus^ intestine, sausage ' (Oscan-Umbrian loanword); 

perhaps Old Irish it'e/'lip' {*guet-lo-s), whether not from *beklo-s\.o gall. beccos^b\\\, 
beak, neb'; 

Gothic qiPus^ stomach, womb', (7/^^/7a//o "pregnant'; Old Icelandic kvidrvn. 'belly, 
womb', /riz/id'^^/'' pregnant'. Old English cwid(a)r(\. 'womb'. Old High German qu/t/'vuWa', 
quoden ' interior of the thigh'; 

in addition further Old English cwidelet 'pustula, varix'. Old High German quedilla6s., 
ndd. quader inflamed swelling of the skin', zero grade Middle High German kutel. Modern 
High German Kuttein ' tripe'. 

References: WP. I 560, 671, WH. 1112 f. 
Page(s): 481 


==========
Root / lemma: g''lia, g^ijos 

Meaning: sinew 

Material: Old Indie yya' sinew, tendon, string esp. of the bow', Avestanyya' bowstring (in 

compounds also sinew of flesh)'; 

gr. pioc; m. ' bowstring '; Note: common lllyrian g"- > b-. 

about Lithuanian gija ' filament ', Old Church Slavic zi-ca 'sinew' etc. see below g"hei-. 

References: WP. I 670, 694, Trautmann 87, 90. 
Page(s): 481 


==========
Root / lemma: g^is-ti-s: " finger ' derived from zero grade of 
Sanskrit: ahgustha- 

First attestation: SB+ 
Part of speech: [m] 
Meaning: thumb' 
Proto-lndo-lranian: HangustHa- 
Page in EWAia: 49 
See also: ahguri- 
Avestan:YAv. angusta-{xx\] "toe' 

Khotanese: hamgusta- "finger' 

References: WP. I 694. 
Page(s): 481
```


## [2026-09-06T15:08:31.782Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf for p.203 (leaf=printed+21 => 224)\" && awk 'BEGIN{RS=\"\\f\"} NR==225' HRN.txt | head -60"
}
```


## [2026-09-06T15:08:32.652Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN p.150 => leaf 171\" && awk 'BEGIN{RS=\"\\f\"} NR==172' HRN.txt | head -60"
}
```


### [2026-09-06T15:08:33.819Z] TOOL RESULT

```
=== HRN leaf for p.203 (leaf=printed+21 => 224)
— 203 —
ap. Varkäna-; aw. cehrka- 'Wolf; phlv. gurg; ai.
vfka- Wolf; arm. gaU (H. No. 62).
kurd. varg *Wolf'; afy. lüg] oss. d. beräyj t. biräy
(60, unsicher) ; bei. gvark, gurk, n. giirß (140) ; yidg.
yter;', yaj'n. aurak,
911. germ Varm*, gerniä 'Wärme', germJ, germis (AM. 54
Zeile 13; 182 Zeile 9).
ap. garma- in Garmalpada-; aw. garema- warm';
phlv. garm^ garmäk, garmth; ai. gharmd- 'Wärmen-
arm. J^rm 'warm', Jermn 'Fieber , jernum *sich erwärmen,
warm werden, erglühen' etc. (H. No. 243).
kurd. bei. (100) garm, bei. garmag (LW. ? 101); afy.
yarma\ oss. d. yarm^ t. yarm (90); siyn. gfarw, sar.
iÄrm, gürm,
912. girevtden glauben* jT^in; (Qiss. Dan., Merx' Archiv,
I, 416, 4).
ap. aw. l/'var- glauben ; phlv. varav(i)stan, mirav{i)sn
(Mün., AV.), päz. garöldan, garöisn, garavisn (AV.).
oss. t. urnjn (262) 'glauben*.
913. gire 'Hals , girebän 'Halsberge' (arab. LW. jirbän,
Jurrubän).
aw. grTva- 'Nacken (des Berges)'; phlv. (aram.) \l^))i
'Hals, Nacken' (Nöldeke, ZDMG. 46, 144), grJvak
'Bergnacken', grtvpän 'Halsberge*; ai. grlvd^ 'Hinter-
hals, Nacken .
afy. griva, greva 'Hals; Halsband'.
914. gureyten 'fliehen , Praes. gurBz-em,
Kauk.-bergjüd. viri/de (!).
skr. vi + i/^reö' (s. No. 638), allerdings nur in der
Bedeutung leer machen , laxiren vorkommend ; doch
vergl. aw. ra^cayeMti (paiti) 'sie verlassen , ai. i^rec-
'räumen, preisgeben', oss. d. lejun , t. iTjin 'laufen,
fliehen' (167); phlv. v(i)rextan.
Eine ältere Bedeutung von np. gure/ten findet sich
wohl bei AM. 237 Zeile 6: 'Also ist das Bedürfniss
nach Wasser grösser als das nach anderen Dingen,
da weder ein Gesunder noch ein Kranker es ent-
```


### [2026-09-06T15:08:35.670Z] TOOL RESULT

```
=== HRN p.150 => leaf 171
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


## [2026-09-06T15:08:54.213Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT printed 183 -> leaf 198 (+15)\" && awk 'BEGIN{RS=\"\\f\"} NR==199' KNT.txt | head -50; echo \"=== grep garmapada\"; grep -n -i \"garmapada\\|garma-pada\\|Garmapada\" KNT.txt | head"
}
```


## [2026-09-06T15:08:55.437Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT garəma\"; grep -n \"garǝma\\|garema\\|garəma\" BRT.txt | head -20; echo \"== BRT jyā\"; grep -n \"jya-\\|jyä\\|jyā\" BRT.txt | head -20"
}
```


### [2026-09-06T15:08:56.838Z] TOOL RESULT

```
== KNT printed 183 -> leaf 198 (+15)
DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43, 45; XPf 19f; XPh BAL.
щй AsH 13; DB 1.34 bis, 34f, 41 ter, 46 bis, 47, 57, 67, 77, 85; 2.3, 4, 18, 74 ter, 77, 81f, 87, 88, 89, 92; 3.30, 47, 48, 50, 58, 74, 77 (written ud, §52. VI), 88, 90, 91; 4.7, 56, 61, 62, 75 bis, 79, 89, 91 bis; 5.11, 12, 19, 20°, 28°, 31, 35 bis; DPd 15; DPe 18, 14; DNa 53; DNb 3f, 26, 27, 28, 30 bis, 37 bis, 40f, 41, 43 bis, 45 ter; DSe 28°, 51f; DSf 13, 28 bis, 29, 33, 35, 36, 37, 40, 44 bis, 48, 50, 52, 55, 57; Обр 2°; DSs 7°; DSt 9; "рле 11; XPa 19 bis; XPb 24, 30; ХРе 13 bis; XPd 19; XPf 19f, 20, 39, 46, 47; XPg 5, 11; XPh 24, 35, 38, 41, 48, 53, 54, 55, 58; Хе 5°; XV 20, 27°; A'Pa 24°: A%Sa 4, 5, 5°; ASe 5; A’Sd 4; A’Ha 5°, 6, 6f; A?He 19; A*Pa 25 bis, 26.
utü-maiy АЗН 12; DB 4.46 (visible to Cameron; ef. note ad loe.); DPh 10; DNa 52f; DH 8; XPb 29; XV 26f°; А?Не 20. utà-taiy DB 4.56, 58, 73f, 75, TH, 79. utā-šaiy DB 2.74f, 89. ша-&т DB 2.13°; 5.18, 26. иій-4ат DB 3.57; 5.15. ulá-di$ DNb 46f.
ula-maiy (§135) DSe 51°; DSf 58; DSj 6°; DSt 9°; XPa 15, 18f; XPd 18f; XPf 41, 45f; XPg 14; XPh 58 (space for w left blank; Lg. 13.303); XSc 5^; A'Pa 23°; Аа 4. uta-Sem (8135) XPh 34, (In restorations there is almost always un- certainty between utà- and uld-.)
Utüna- sb. ‘Otanes’, ally of Darius against Gaumata: Elam, fu-ud-da-na, Akb &»mi-it-la-na-" ,
176
Gk. 'Ürávgs; perhaps u- ‘good’ + tāna- to root tan- ‘stretch, extend’ (§164.II), Av. Skt. tan-, Gk. telve, Lt. tendit, cf. Skt. tdna-m ‘offspring’: ‘Hav- ing good posterity’. [апа] nsm. DB 4.83.
utava- adj. ‘strong, in health’: u- ‘good’ + deriv. of tav- ‘be strong’ (§122). utava nsm. DB 4.71f (emendation of HK, ApKT 1.63, 2.29, for KT’s detse, with first and third characters very faint; $541).
ubanuvaniya- sb. ‘good bowman’: u- ‘good’ + Sanwaniya- ‘bowman’. wudanwaniya nsm. DNb 42.
ud prep. and prefix ‘up’, becoming Iran. us- uz- before dentals ($85): Av. us- uz-, Skt. ud, pIE *ud (and *üd in NEng. out, NHG aus): ud with verbal root раф, us- in ustaxand-, u(z)- in uzma- (S84).
ира (i.e. upd, cf. 5140.1) prep. and prefix ‘to- ward’: Av. ира, Skt. úpa, Gk. iad, Lt. s-ub ‘under’, pIE “иро.
(1) Prep. with acc., ‘under, with, m the time of (hardly ‘belonging to’, as taken by Hz. ApI 353): DB 2.18, 3.30; A’Sa 4; А?Ра 23; Sf.
(2) Prefix, ‘under’, in Upadarma-; ‘toward’, with verb ay-; ‘beside’, in upasia-.
Upadarma- sb. ‘Upadarma’, father of Agina: Elam. uk-ba-[lar|-ra-an-ma. From ира + darma- (root dar-), Skt. dhérma- ‘right conduct’ (§163.V): “Не who is under (= behaves himself according to) right conduct’ (so Bthi. AiW 390, with lit.; hardly Upadara"ma-, after the Elam.; hardly as taken b Hz. ApI 190). Upadarmahyá gsm. DB 1.74.
upariy adv., prep., prefix, ‘above’: Av. upairi, Skt. upd, Gk. тёр, Lt. s-uper, Gt. ufar, pIE *uperi (5191.1). (1) Adv. ‘above’, XPh 31. (2) Prep. with ace., ‘over, over and above, upon, according to’: DB 4.64; DNb 4, 32, 46, 49; DSf 27. (3) Prefix, ‘over’, with verb ay-.
upasté- sb. ‘help, aid’: upa- + verbal root slà- (6140.1, $142), ef. Gm. Bei-stand for meaning. upastém asf. AmH 10; DB 1.25, 55, 87, 94; 2.24f, 34, 40, 45, 54, 60, 68, 86, 97°; 3.6, 17, 37, 45, 62, 67, 87; 4.60f, 62; DPd 13; DNa 50; DSf 19°; DSk 5; XPh 32, 45.
Ufrütu- sb. ‘Euphrates’, river of Babylonia:
OLD PERSIAN
Elam. t-ip-ra-tu-i8, Akk. purattu, Gk. Еўфрат
(§75.V, §76.V, §166, $166.II). Etymology un. |
certain, probably a popular etymologizing in OP of a local non-Iranian name, cf. Bthl. AiW 1830; Fick, ВВ 24.310; Justi, ТЕА 17.116; Tm. Lex. 77, Ufrätwā ism. DB 1.92 (not gen., as taken
=== grep garmapada
1280:name Garma-pada-, c£. Lt. formus ‘hot’. pIE root *g*hen- ‘strike’, OP ja"tiy, Skt. Айли;
1820:1. Primary, in the following: dar-ma- in per- sonal name Upa-darma-, gar-ma- in month name Garma-pada-, fem. tau-mà-, ad]. taz-ma- in per- sonal names (see Lex.), hau-ma- in hauma-varga-. On dubious атат, see Lex.
1914:b. Genitive: Arta-xéaga- ‘Having a kingdom of justice’; Aršāma- (from *aría-ama-) ‘Having the might of a hero’; Haxd-manis- ‘Having the mind of a friend’; Garma-pada- ‘(Month) having the place of heat’; Asa-garta- (Тапа) having caves of stone’. :
1964:Without vriddhi in either part: Garma-pada-, and the restored Varka-zana- (but see Lex. s.v.). For further details, see Lex. s.vv. and 8161.
2897:DB 8.71 Garmapadahya mühyà I тамса 9akalam aha.
2967:$290. COORDINATION AND SUBORDINATION. Not infrequently the OP texts express by coordinate clauses ideas which are logically subordinate; the result is a series of short sentences, syntactically simple, independent of each other grammatically, but logically and semantically connected. Thus, for example, DB 446-8 vafnà Auramazdaha api- mary aniyascry vasiy astiy kartam ava ahydya diptya пазу nipistam avahyarddiy naty nipistam таша ... ‘by the favor of Ahuramazda indeed, much other (work) was done by me; that (work) is not inscribed in this inscription; for the following reason it is not inscribed, lest . . .’; this could have been expressed in one complex sentence somewhat as follows: ‘much other work was done by me, which has not been inscribed in this inscription for the following reason, lest ...’. Another excellent example is found in XPf 20-25 шій Vistáspa иа Arfüma ubā ajivatam асту Auramazdim арабӣ Ката aha Dérayavaum hya manā рий avam asdyabiyam akunaus ahydyd бата 'Hystaspes and Arsames both were living, then—unto Ahu- ramazda thus was the desire—Darius who (was) my father, him he made king in this land’; in the parallel passage DSf 13-5, yadzy ‘when’ is used . instead of асїу ‘then’, and instead of Auramazdém avatà Ката aha (found also XPf 29f, DSf 15f), we find in DNa 37f (and elsewhere) yada mim ата Gha ‘as unto me was the desire’. In dating sen- tences we regularly have expressions of the type seen in DB 1.42 Garmapadahya máhyà I X rauca- bi$ fakaia aha агава zšaçam agarbdyatd ‘of the month Garmapada, 9 days had passed—then he seized the kingship’; only in DB 1.38 the date is followed by a subordinated clause, yadiy udapa- tala ‘when he rose up in rebellion’. The same phenomenon is probably present where conjunc- tions are omitted as introductory to subordinate clauses, such as the absence of tya in РМ 20 and 50 (cf. DNa 39).
3491:42 :agarbàyatà : Garmapadahya : máhyà : IX : raucabis : 0akatà : dha : ауаба : xša 43 cam :agarbàysatá : pasáva : Kabüjiya : uvamarSiyuS : amariyatà : іу
3570:$11. 135-48. Saith Darius the King: After- wards, there was one man, a Magian, Gaumata by name; herose up from Paishiyauvada. À mountain by name Arakadri—from there XIV days of the month Viyakhna were past when he rose up. He lied to the people thus: “I am Smerdis, the son of Cyrus, brother of Cambyses." After that, all the people became rebellious from Cambyses, (and) went over to him, both Persia and Media and the other provinces. He seized the kingdom; of the month Garmapada ІХ days were past, then he seized the kingdom. After that, Cambyses died by his own hand.
3726:46 m : kàram : tyam : Vahyazdatahya : aja : vasiy : Garmapadahya : mah
3779:ingly; of the month Garmapada I day was past— then the battle was fought by them.
```


### [2026-09-06T15:08:56.898Z] TOOL RESULT

```
== BRT garəma
== BRT jyā
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
2869:•  ]*.,  g.  aog-  V.  'praedicare'.  Praes. laog-  [,  22  flö/ffa]').—  PPfP.aox/a-,  PFP. aejya-.
2947:•  j.  aobg-  V,  'niederhalten,  -drücken'. Praes.  27  (Pass.)  ubjya-,
2950:•  j.  aonya-  n,  Bezeichnung  einer  Feuerungs- oder Heizvorrichtung :  'yat  haca  parö.- iarfjyäi {sd.)  V,Ä86;  —  'yat  haSa  taxair- yät(sd.)  V.Ä93.
4057:—  Pü.  (ru  Y.  ji);  fia  .  .  afräi  saHsnTh,  SO.! yal  . .  iijyäm  dStum  iaiyale;  (lU  Y.  63):  an  ie man  ämöxl /räi  saHin,  ?>ä.i yÖ  mi  abhüt  ayog- yatä,  NpQ. :  ängah  marä  iHd  näsatä,  —  >)  Eine unmögliche  Et.  KZ.  30.  511 ;  iBed.  des  Adj. vgl.  »i.  uiiarävotti'  ('snperiorem  reddens^ bhanguravanl-  ('debilem  reddens").
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
4955:barqn  'va  ait>m  nmütam  V,5.4i;  —  Hai^  %iia  (sd.)  aoi  ava  asnavät  P.  2/;  —  "<■«/ ..  avaMmU  -m  «(//.iwffi  (sd.)  karsaya  as5  Vyt  25;  —  yat  he  'vat  pourum V.p.i2.  a)  in  Verbindung  mit  ä  dn.:  ubjyäite  (sd.)  V.7.S2PÜZ.  a)  auf  die ka%S  drußm  nJ/aAmai  3  fiT/.>t3säm3  (&d.}  a.Vevson  bezüglich  'iste':  sarJt  bß~dyrii.. fing  ä  'vä'>ydi..\.44-^2-  2)Praev.(mit  =1,«  ma^rs  >^..  "..gemäss  jenem  (deinem) '£an;gan-,gam-.'bar-,si,l-\ß«.}.  a)  bei ;  Spruch  .  ."  Y.  44.17;  —  cis'ca  '^wam Ellipse  des  Verbums:  t»m  janäi  .  .  k>n-  Jakarta  'va  masanaca  vatahanaca .  .  "Jeder s.lipJ  'va  '>  apaMm  (sd.)  gayeAe  Yt.  /().  44.  hat  dich  gern  gehabt  wegen  jener  (deiner) KompA.  i  Abldt.  ^  a^rS).  -  S._  auch  a-^ö  ~-  ^  q^q^^^  ^^^  .  .'■  H.  2. 11 ;  —  ai/at  tljas.lni ai.    ai'fl   Fraen.,   Praev.j    mp.  n  dm.    —    I  u.  .,  -  ,,  ,     ,
6467:•  j.  "aätay-  m.  'Pfeil':  yat .  .  jyä  navi- >jqn  (sd.)  tiyrar?hs  "tayS  Yt  10.  113.
6752:•  ).  a-ham.baoS^mna-  Adj,  'nicht  wahr-  Oberherm  und  Richter  und  als  den nehmend'  sva,  'der  seine  Sinne  nicht  zu  ersten  Lehrer  der  Menschheit"  Yt. /_J.  1 5  a ; brauchen  weiss'  (vom  Hund):  yat  ..  sfä\ —  ya^a  fr3  loa  (sd.)  ämraot  yat  dim •n<s  Tä  haiat  aoäitySjxratus  "wenn . .  ander- '  ahümca  ratutn^a  ääadat  "'ya^a'  sagt  aus, seits  ein  Hund  seine  Sinne  nicht  zu '  dass  sie  ihn  (näml.  Zar^  als  A.  und  R. brauchen  weiss,  der  (weil  er)  nicht  recht  eingesetzt  haben"  Y.Jfj.u;  Yt  7^.92;  — bei  Verstand  ist"  V.  /_J,  35;  —  yesi  nnl<yailqm  ns  ahurS  maeäh  .  .  vatsks  valaa spS  'nS  mafye  v3  .  .pai'jyäite  aAmai(sA.)\{sA.)  atiqm  zaraiustr5  ankuca  (NS.)'' heüa  irisylt  "sonst  könnte  der  Hund,  der  ratu^ca  Vi.iö.i;  Yt./j.gi;  —  allai  dim seine  Sinne  nicht  recht  zu  brauchen  weiss,  lUsfanam  maziit?m  dazäyli  (sd.)  ahümca in  eine  Grube  ..  geraten"  V.  j_j.  37.  .^ratämca  yim    ahunm    mazdqm    Y.  27.  i;
7132:—  äat . .  ahe  nmänake  frapi'^ws  gäu/  .  . 'lars  ,  .   *vlspqm^ujyäiiii  V.J. 3;  —  "'^rS
7767:•  g.  ar«z9-3i-  Adj.  'der  recht  lebt';  n3it 'jyüi  frajyäiüi  (sd.)  ,  .  drsgvasü  patrT  Y. 2g.  5 ;  —  xsä^rfm  yä  °jyöi  dähl  *dr»gaovi (sd.J  vakys  '^.53.9]  —  'ßs{A-P-)  aSü  .  . fisyasii  (sd.)  "die  rechtlebenden,  o  Asa, . ." Y.jo.,.
9947:■  j.  gaSwa-  m.,  gaSwä-  f.  'Hund,  Hün- din''' i)xa.:di^e  navaiti 'wqm{CiY,) pairi.- yaoidaikUa  stiptibyas£a{^^..'S.i4-  I7;  — bis  hapta  puhrqm  'wqm  (AP.)  uzjämöit (sd.)  V.  r4.  i6;  17;  —'  fra  mi  'wa  (NP. als  AP.)  sasayqn  mzbjnta  (sd.)  V,  8. 37.  2)  f.:  aiia  (näml.  hätrist)  ca%wan.- failißäna ya  'Tva'W .i^.iqGl.; — yaica  aisa toa  uÜrS-itänaisva /rajasät{sA.)  V.  15.23; — yS  °wqm  yqm  apu%Tqm  {sd.) /anaiä  vs ,.pasdaya/i{sd.)  vä  yaica  alsa  "wa  magye .  .  pai'jyäite  V.  Jj.  S ;  —  °wqm  yqm  apu- irqm  "^rayqm  *baesdri  "eine  Hündin,  die kürzlich  geworfen  hat,  . ,"  V.  15.49.
10715:gAw. :  ahya  '"kräXa  maziiiäcä  *hvapa- nhäisca  (sd.)  tsm  at  ,  .  yasamaidl  Y.^J/. a;  —  kudä  (sd.)  asim  vohuca  maus '%r)m^ä  Y.  25.  1 1 ;  —  yüism  aäbyS  .  . aogü  data  .  .  '%nmc3  .  .  yl  kuhitts  rä- mqmcS  (sd-)  däl  Y.  2p.  10;  —  isasä  (sd.) . .  maibyö  '"^nm  aojönahvat  yehy3  vfndä (sd.)  vanalmS  *drujim  Y.J/.  4;  benutzt V.ao.  8;  —  tat  mazdä  tava  '>rfm  yä  .. düAf  drigaov!\sA.)  vaiyj  Y.ß^.g;  — yJ vahyJ  varihSuS  dagdi..ahurö  '"S^rä  mazdä Y.5J.  6;  —  tici  '^rä  mazdä  dqmis  (sd.) ahurS  'V.4$.T,  9;  —  maibyS  masds  tavä rafinS  JräxStuiam  (sd.)  kyat  ^wä  °&rJ a/Jt  hacä  frqifa  Y.  4!?.  1 4 ;  34. 15;  —  y} dfmanahyä  'hnm  M^rahya  vä  daSySu:" va ../radahäi{sA.)  aspinzatä  Y.Ji,  16;  — yastJm  °ärJ/  mazäJ  mSÜai  (sd.)  jyätSul Vä  Y.  46.  4;  —  at  ratqm  zara'iuitrS  .  . dadäiij  paurvatätim  . .  mazdiU . .  ux^aHyäcß (sd.)  ifraespm  '"irimcä  "..  den  Gehorsam und  die  Herrschgewall"  \.33.i4;  benutzt Yt  IJ.  88 ;  —  vauhstts  dazd,l{%ü.)  manau/iS lyaöhananqm  a»fiSus  mazdäi  ''knmca ahuräi  a  X.2-j.iy,  —  hux^a^rSJimäi (sd.)  .  .  '"ir^m  .  .  äad)mahicä  cismahicä *hvqnmakicä  Y.^5. 5;  —  yS  dngvSUi '"^nm  hunüiiJ  {?,d.)  Y.j/,  15;  —  yais *ffrMm3{sd.)  asäivaratä..°'^r3mca  lianqm *dnfim  Y. 32.13;  —  '>rais  yujin  (sd.) karapanU  .  .  akäis  syaohanäis  .  .  Y.  46. II.  a)  mit  Gen.  'über  — '  (s.  2  a);  tarn
10723:yavsi  vjspai  fraßtarihs  aiihamä  Y.4^.8; — ka  tsi  vauAsus  mazda  °%raAya  Isti^{sd.) . .  maibyS  aAura  Y.  48.  8;  —  ku^rä  ^wS '•'irä  (NP.)  mazdä  "wo  sind  deine  Reiche, o  Af.?"  Y.  5/.  4;  —  mazdäi  avaj  °^/v« Ayat  Aöi  voAa  vaxsal  (sd.)  manatjAa  Y. 31. 6j  —  apsnd  (sd.)  dar^S.jyäitlm  *ä °%r>m  vaaASui manatfAs  "..  zu  dem  Reich des  VM."  Y._jj.  5;  57. 18;  —  va»hsus '^rä  (AP.)  manat^AB  . .  ärmailis  vaxst Y.34. 11;  —  asfmcä  .  .  ''hnmiS  Aaurva- tsts  ".  .und  das  Reich  der  Wohlfahrt"  Y.34~ i; — ySzSm  zr.nslyänAö  (sd.)  TsS  "ärjMÄl savatiAqm  "..  Reich  des  (ewigen)  Nutzens" Y.  2Ä  9';  —  Ayai  .  .  cöist  (sd.)  'hröi  Aöi Aaurvütä  anurplätä  .  .  dqn  .  .  Y.  45- 10.  ß)    im  jAw.:   ya^ia    asai    '^rym
11582:Zum  \.  jyä-  (aus  der  volleren  Form;  s.  dazu HlBT  Ablaut  97).  —  Pü-!  *afashtisn')  kämak pa  yin.  —  i)  S.  zu  saed-  No,  2.  So  ist  lU lesen,  gegen  Haug  Essays'  366;  vgl  Pu.  zu
11695:"  j-t  g-  jyätay-  f.  'Leben'.
11697:•  g.  Jyätav- :y>T/»-''  m.  'Leben':  talclt ma  mSnndm  (sd.)  JyStüm  Y.  J2.  11;  — ySi  gSus  mBrmdm  urvSxs.uxl{{&A^  jyötüm Y.J2. 12;  —  dus.sasti!  .  .  mSrindai  (sd.) .  .  jyatSus  .  .  xratOm  Y.  J2,  9 ;  —  yastim xia%raf  .  .  msi^at  (sd.)  jyätSui  vä  Y. 46- a;  —  ys  is  fymiä  hlmi^yai  (sd.) vas7.itSiscä  Y.  5^.  9 ;  —  avais  aibl  ying dairüT  nSitjyätJm  xiayamnfng  vasS  "durch die  (gerade),  die  sie  nicht  nach  Gefallen über  ihr  Leben  schalten  lassen"  Y.^2. I S-  2)  'Lebensunterhalt' :  y!  nsitjyötäm hanarf  (sd.)  vinastJ . .  "der  seinen  Lebcns- miterhalt  nicht  findet  ohne  .  ."  Y._j/.  15.
11698:VgL  jyälay.  —  ai.  vgl.  jh.-ila'i^  m.,  f.  (eine Umgeitaltung  nach  dem  Vra,t%.Ja-ati;  JSchmidt KZ.  j».  378.  Falsch  MlLLs  G.XXiv,478i. — Pfl.:  iBiimöniaHd^ih\ia:aniiakih,  {yi\. 53^46): iana,  iam'Sn  ielid'i.  —  i)  S  39^-  6.  —  '}  Öber- seliung,  nicht  Erläuterung  wie  MlLLS  G.  H5 annimmt;  Sü.i  fmnldra^.  I
11754:—  ta/it  ..ya  neitfä  ar?Aat  (Sp.  271  u.)..' .  .  daidyäi  savS  Y.$l.2o;  —  aitikelhaft: ^•3'-  S;  —  «/  *J  /^»{ADn.y  vaxsya  ..  Ayat  AvS  tSng  frS.ga  paimHig  hunstöis  *carat aksyäisd.)  ..  U'tä  . .  Y.5/.8;  —  s.  noch  Y../Ö.4; — Aad,i(%d.)  vis  ta  (IS.)  T-a  Am Jng Y.43.13,  46.16;  s.Sp.6i4U.  An.-  s^raosäY. 46.17  ;—t}m  äzütöis'mqhrrm.. hang,  ta-  steht  insofern  substantivisch,  als  Y.  29.  7 ;  —  tä  (APn.)  vS  urvatä  (sd.) das  zugehörige  Substantiv  in  den  Relativ-  ff/or^n/iT  . ,  Y.31. 1;  —  tqm  Hstim  d>jä- saXzgtzogeaist;gAvf.:tqm  Aavä  vTstäspi^..  maspj  ..  nntiti  tat  x/ahrvm  ..  Y.jj. nqsat  . .  yqm  Hstlm  (sd.)  manta  ..  mazdä  18;  —  15 i  narspts  rajls  a!.<asä  (sd.)  .  . ahurS  Y .  51.  16;  —  i7/W(APn.)  raxryä  . .  Y.5J.9;  —  at  tH  mazdä  tJm  mainyüm yä  masd3>ä  (sd.)  Ayal^t  2'TdusiY.30.i;  —  ..  mai'iä  (sd.)  ..  bar^tä  Y.33.^;  —  s,  noch tä  (ISn.)  dibinaota  malim  hujyätöis  K.sA.)  V._?o.4,  4?.  10,  47.6;  s,Sp,6i4U.  a)iu- .  .  Ayat  IUI  .  .  syadiatum  .  .  fraHtias  Y.  gleich  auf  ein  Relatimm  ab  dessen  Korrelat 32. t,.  B)  im  jAw.:  tim  aoi  ibai',,!  s(it^Ms,yi€\%Ka.d\tsil zT na  ^adi:aniiS bym- paityantu(sd)  yS  i  dalaY.6^.&;  —  .. /;J  teya^sü  ..Y.34,&.  B)\m\A'9i.:  aAe  raya t»m  slsanät  yS..taurvay3t  ,  .  Yt /_J.  142;   ..  ttm  yiiiäi  ..sraasim  «Äw  Y.57.3;YL7,6,
12102:•  j.  tanp-  V.  'stehlen',  Praes.  27  trpjya-'\
```


## [2026-09-06T15:09:00.906Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Bogensehne\" BRT.txt | head -20"
}
```


### [2026-09-06T15:09:00.956Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:09:01.887Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD garm\"; grep -n \"garm\" PHD.txt | head -20; echo \"== PHD zih\"; grep -n \"^zih\\|zih \\|zih,\" PHD.txt | head -10"
}
```


### [2026-09-06T15:09:01.945Z] TOOL RESULT

```
== PHD garm
378:galēģ [glwk' | N guld] throat. бато [gm | = M, N ~j pace, step, stride; a yard (3 ft.). ~ í dó pay: a pace (s ft.). -рапаб [-k’nk' | M eng, N -gàna] suffix forming numerical adjectives, -fold. бапа [gnd | N ~] stench. gandag [gndk' | (M gng), N —a] foul, stinking. ~th: stench. ģandanāģ [gndn’k' | N gandanā] leek. gandum [Hš < A nth | (M gnwm), N ~] wheat. ganj [gnc | (M gnz), N e treasure, treasury. ~war [-wbl | M -wr, N ~] treasurer. ģan(n)āģ [gr &! | (P gnd?g)] foul, corrupt (v. gandag). ~ ménó$g the Evil Spirit. ~ih: corruption. gar [gl] mountain. -gar [-Al, -gl | M -gr, N ~] suffix forming actor nouns. -gar [-£1| M -g’r, N ~] suffix forming actor nouns. garan [gPn! | M г?л, N girán] heavy, serious, difficult. АҺ; heaviness, weight. garasman [glsm’n' | М ртт?п] = garddman. gard [g/t! | N ~] dust. gardan [gitn! | M grdn, N ~] neck. ģardānāģ [gl h] die (for gaming). gardanidan, gardan- [gl n-ytn! | M grd(y)nydn, N ~] turn (tr.). gardidan, gard- [git-yin' | M grd-, N ~] turn, revolve. ~išn: revolution, turning. garm [gim | M grm, N ~] warm, hot. «„«ih: warmth, heat. garm-ābag [gim'pk! | N ~a] bath-house. garmāģ [glm^ k! | М grmg, N garmá] warmth, heat. g£armóg [gimwk!] warm, ardent, fervent. garmówar(ih) [glmwk wl(yh)] heat ordeal. ģarmsēr [gimsyl | N ~] warm region, lowlands. garódman [glwtmn' = Av. garó dəmana- | M grdm?n] paradise. ~ig [-yk'] (worthy) of paradise. yarranag [g”7k! | M grn’g ?] thunder. yarranidan, yarran- [gl’n-ytn' | (N yurridan)] roar, thunder. ~i$n: roaring. garzag [gick! | N garza] snake, serpent. garzidan, garz- [glc-ytn'] complain; confess. ~i$n: complaint. ~iSnig : complaining. gaw [gw!'] hand (daevic). базу [ТИРА < А twr) | M gw, N ~] ox, bull, cow; astr. Taurus. gawars [PZ < A prg’; g”wls | N ~] sorghum, giant millet.
412:J jad [y’t'] share, portion. Yadag [ytk! | M jdg] omen. tļadaģ [ytk'] form, property. jadag [y’tk' | M del share, portion; case, cause. jadag-g5(w) [y tkgwb'] advocate, intercessor. ~ЛЬ : intercession. jadag-wihīrih [ytkwhylyh] transformation, alteration. Jadarih [y2?lyh] maintenance. *fadisn [ytsn'] (accidental) quality, property. ~ig [-yk'] accidental, non-essential. jadiig [y?te&! | M j?dwg, N jadi] sorcerer, magician. — h: sorcery, magic. *jay [у?л | N ~] sissoo tree. jagar [yal | N jigar] liver. Jah-, v. jastan. jahišn [yhysn' | J jhysn-] chance, fortune, omen. Jahišn-ayār [yhyfn hdyb'l | N n. pr. jhiy?r] fortunate. ~ih: good fortune. jahüd [yhwt' | N juhiid] Jew. jām [y m | N ~] glass. јат [M ANE < A mn-h; ут | M Pm, N <] vessel, goblet. lfamag [y”mk! | N јата) = *jām. атар [y mk! | М ртр, N fama] clothing, garment. jang [yng | M jnng, N ~] struggle, battle, fight. Jar [ywl | M рт] time, occasion. jastan, jah- [ystn!, yh-] happen, occur, chance (to be). ~išn, v. jahišn. Jašn [yfn! | N —] celebration, festival. jaw [ŠZ < A £% | N ~] barley. Jāwēd [y wyt! | (P ywyd), N ~] eternal.
417:kabāh [kp’h | Ar. gabā] garment, cloak.
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
621:wastar [wstl = Av. wastra-] clothing, garment.
831:ardent garmog, taftig.
938:bath ābzan, garmābag.
1695:dress paymēzan; v. garment.
1917:fervent garmēg, taftīg.
2076:garment jàmag, kabàh, paymog, paymózan, warr, wastar(ag).
2241:heat (n.) garmag, garmih, tabišn; о wardagih; on — war-
2326:hot garm; grow — taftan.
2683:lowland garmsér.
2995:ordeal war; heat ~ garmówat(ih).
4264:warm garm(6g); ~ region garmsér,
4265:warmth garmag, garmih.
5358:darak, gilag garm darmān garmāg garmābag
5359:garmīh
5360:dramanag, garmēg
== PHD zih
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
3768:speed tagigih, tézih, züdih.
4211:victory abarwézih, pērēz(gar)īh; final ~ frazām-pērēzīh.
4731:pil payray- fīlāsūfā payrāyag pērāmēn Payrāstan pīrīh péroz pérézih pérozgar
5103:zahrag Kä: zāmyād YU g S zāmēn- - e$ zāmēnīdan Wes PAS zadan US zādag \зтеҳЅ zibāl NS S 1-1, zay- -aS zih AUS zi(w)- _ GAR zēnhār Sao «S
```


## [2026-09-06T15:09:10.068Z] TOOL CALL #18: Bash

```json
{
 "command": "grep -n \"\\[pdf page\" data/verification/sources/refs/BQT_v2_pages.txt | head -3; echo ---; python3 -c \"\nimport re\nt=open('data/verification/sources/refs/BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('زه')\nprint(len(t))\n\"; ls data/verification/sources/refs/ocr/ 2>/dev/null"
}
```


## [2026-09-06T15:09:10.100Z] TOOL CALL #19: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T15:09:12.198Z] TOOL RESULT

```
---
2900526
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
```


### [2026-09-06T15:09:12.236Z] TOOL RESULT

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


## [2026-09-06T15:09:15.453Z] TOOL CALL #20: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/BQT | head -50"
}
```


### [2026-09-06T15:09:15.492Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1275.png
1275.txt
1294.png
1294.txt
1294.vision.txt
1299.png
1299.vision.txt
1300.png
1300.txt
1300.vision.txt
1302.png
1302.txt
1302.vision.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1453.png
1453.txt
1455.png
1455.txt
1462.png
1462.txt
1465.png
1465.txt
1471.png
1471.txt
1472.png
```


## [2026-09-06T15:09:16.626Z] TOOL CALL #21: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1800 2>&1 | head -60"
}
```


### [2026-09-06T15:09:18.422Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 595; check the printed number and re-run with --pdf-page if off)
REF: BQT:1800  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 595  OCR-lang: fas

کر که‌آعتی ۱۹۸
در جایی بخورکنند موشانی که در آن توابع | آخر : نومی‌از پای افزار است که شاطرآن‌وپياده
باشتد همه آنجا جمع شوند واگرزنی بر بالای | روان پوشند ویگرگابی شهرت دارد ۷ "
عاش کر که بشاشد هرکز آبتن‌شودا . گرگ‌پند - بفتح بای ایجد وسکون

گر لك آشتی - سلح‌بتفاقومکروحیله | نون و دال » کنایه از کرفتار و اسیر و زبون
وفریب راکویند ۴ . و خقیف باشد ۸ .

گر 4 آشنایی ۴ «کنایه از آشنایی گرگ بند کردن - کنایه از زبون
و دوستی بغریب و نفاق ومکی وحیله باشد وخفیف و آسیرکردن باشد ۸ .

گر گات - بنم اول وکاف فارسی بالف گر گج - بفتح اول وکاف فارسی‌پروزن
کشیده بروزن سلطان» نام‌شهری‌است دردارالملك | اعرج» سر کوبیرا کویند که بجهت کرفتن قلعه‌از
استراباد و معرب آن جرجان باشد ۴ - وبمعنی | اسنگه وگل وچوب مازند ‎٩‏ .
دشت و بیابان هم بنظرآمده است ۵ . گرگ دق - بنم اول وفتح دال ابجد

گر گانج - ضم اول و سکون نون | وسکون واو »کنایه از دویدن آهسته و بسرعت
و جیم » نام دارالملك ولایت خوارزم باغسوممرب | رفتن و پوبه کردن وقطره زدن باشد وآ نرابمریی
آن جرجانیه است و ترکان ارکنج خوانند۹ . | هروله کوبند .

گر گاو 0 * جم اول وسکون واودر گرگ دیزه *۱- بسمنی ک رکهرنکه

) چش : گرکاو ۰

- این مطالب براساسی لیست! ۴ -قس :ک رکه آشنایی :

باد که با خاک بگ رکه آشتی است ایمن ازین راه ز ناداشغتی امت .

نظامی کنجوی « کنجینه کنجوی ۱۳۲ *.

۴ ر4: رشیدی» وقس: ک رکه‌آشتی . ۴ - پهلوی ۷۱۲۵۳ [20ع6007] -
117۳0892 . ر43 : مار کوارت : شهرستانها ص ۱۲ ح ۱۷ ؛ اونوالا ۹۲ . کرگان باطلاق عام
عامل ابالت استرایاداست که از شمال ببحرخزر وازمشرق بخراسان و ازمغرب بظبرستان میکشید
: مسج‌البلدان » و باطلاق خاص شهری قدیمی است درکنار رود گر کان و بدوقسمت تقسیم‌میشده
یکی شهرستان و دیگری بکرآبا د که بواسطةٌ پلی بهم متصل بوده‌اند و مقبرء قابوس وشمگیر در
سه کیلومتری این شهر ومعروق بکنید قابوی است «کیهان . جغرافیای سیاسی‌ص ۳۰۹ »جمعیت
کرکان ۲۰۰۰۰تن وجزه استان دوم است . 8 - ونیز جمع گر که کر کان آید .

-جرجالیه نام قضصبة انیم خوارزم وشهرست بز رکه برساحل جیخون و مردم خوارزم
آترا پزیان خود «کرکانج » میخوانند: پس‌آلرا تمریب کرده جرجالیه گفتند « معجم‌البلدان > .
لور کنج ۳ کر کانج < جرجانیه کرسی ولایت خوارزم امت « عباس اقبال. تاریخ مغول صس۵».

۷ - بجتجوی توگردون چو عزم راه‌کند ز خام ورکند پای ماه راگرگاو ‏

آذری طوسی « رشیدی > .

۸ - فرهنکه نظام نوشته :کر که‌بند . از ترس از جای خود نجنبیدن :

لزین کربه کون خاکه تا چندچند بغیری توان کردنش کر که بند .

8 « رشیدی» « فرهنگه نظام >.

. ‏-ر3 : جهانگیری - ۴ رك : دیز » دیژه‎ ٩
```


## [2026-09-06T15:09:25.894Z] TOOL CALL #22: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1800 --pdf-page 597 --image 2>&1 | head -70"
}
```


### [2026-09-06T15:09:28.457Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1800.png
REF: BQT:1800  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 595  OCR-lang: fas

کر که‌آعتی ۱۹۸
در جایی بخورکنند موشانی که در آن توابع | آخر : نومی‌از پای افزار است که شاطرآن‌وپياده
باشتد همه آنجا جمع شوند واگرزنی بر بالای | روان پوشند ویگرگابی شهرت دارد ۷ "
عاش کر که بشاشد هرکز آبتن‌شودا . گرگ‌پند - بفتح بای ایجد وسکون

گر لك آشتی - سلح‌بتفاقومکروحیله | نون و دال » کنایه از کرفتار و اسیر و زبون
وفریب راکویند ۴ . و خقیف باشد ۸ .

گر 4 آشنایی ۴ «کنایه از آشنایی گرگ بند کردن - کنایه از زبون
و دوستی بغریب و نفاق ومکی وحیله باشد وخفیف و آسیرکردن باشد ۸ .

گر گات - بنم اول وکاف فارسی بالف گر گج - بفتح اول وکاف فارسی‌پروزن
کشیده بروزن سلطان» نام‌شهری‌است دردارالملك | اعرج» سر کوبیرا کویند که بجهت کرفتن قلعه‌از
استراباد و معرب آن جرجان باشد ۴ - وبمعنی | اسنگه وگل وچوب مازند ‎٩‏ .
دشت و بیابان هم بنظرآمده است ۵ . گرگ دق - بنم اول وفتح دال ابجد

گر گانج - ضم اول و سکون نون | وسکون واو »کنایه از دویدن آهسته و بسرعت
و جیم » نام دارالملك ولایت خوارزم باغسوممرب | رفتن و پوبه کردن وقطره زدن باشد وآ نرابمریی
آن جرجانیه است و ترکان ارکنج خوانند۹ . | هروله کوبند .

گر گاو 0 * جم اول وسکون واودر گرگ دیزه *۱- بسمنی ک رکهرنکه

) چش : گرکاو ۰

- این مطالب براساسی لیست! ۴ -قس :ک رکه آشنایی :

باد که با خاک بگ رکه آشتی است ایمن ازین راه ز ناداشغتی امت .

نظامی کنجوی « کنجینه کنجوی ۱۳۲ *.

۴ ر4: رشیدی» وقس: ک رکه‌آشتی . ۴ - پهلوی ۷۱۲۵۳ [20ع6007] -
117۳0892 . ر43 : مار کوارت : شهرستانها ص ۱۲ ح ۱۷ ؛ اونوالا ۹۲ . کرگان باطلاق عام
عامل ابالت استرایاداست که از شمال ببحرخزر وازمشرق بخراسان و ازمغرب بظبرستان میکشید
: مسج‌البلدان » و باطلاق خاص شهری قدیمی است درکنار رود گر کان و بدوقسمت تقسیم‌میشده
یکی شهرستان و دیگری بکرآبا د که بواسطةٌ پلی بهم متصل بوده‌اند و مقبرء قابوس وشمگیر در
سه کیلومتری این شهر ومعروق بکنید قابوی است «کیهان . جغرافیای سیاسی‌ص ۳۰۹ »جمعیت
کرکان ۲۰۰۰۰تن وجزه استان دوم است . 8 - ونیز جمع گر که کر کان آید .

-جرجالیه نام قضصبة انیم خوارزم وشهرست بز رکه برساحل جیخون و مردم خوارزم
آترا پزیان خود «کرکانج » میخوانند: پس‌آلرا تمریب کرده جرجالیه گفتند « معجم‌البلدان > .
لور کنج ۳ کر کانج < جرجانیه کرسی ولایت خوارزم امت « عباس اقبال. تاریخ مغول صس۵».

۷ - بجتجوی توگردون چو عزم راه‌کند ز خام ورکند پای ماه راگرگاو ‏

آذری طوسی « رشیدی > .

۸ - فرهنکه نظام نوشته :کر که‌بند . از ترس از جای خود نجنبیدن :

لزین کربه کون خاکه تا چندچند بغیری توان کردنش کر که بند .

8 « رشیدی» « فرهنگه نظام >.

. ‏-ر3 : جهانگیری - ۴ رك : دیز » دیژه‎ ٩
```


## [2026-09-06T15:09:33.891Z] TOOL CALL #23: Bash

```json
{
 "command": "rm -f data/verification/sources/refs/ocr/BQT/1800.png data/verification/sources/refs/ocr/BQT/1800.txt && timeout 600 python3 tools/ref_page.py BQT:1800 --pdf-page 597 --image 2>&1 | head -60"
}
```


### [2026-09-06T15:09:41.926Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1800.png
REF: BQT:1800  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 597  OCR-lang: fas

ک رکوی ۱ 1 مرا
نیز گوبند ؛ وبفتح اول هم آمده است. . مطلق پوستین راگوند ه .
گر گوی ۱ - بروزن‌بدکوی(۱). نام گر - بنم اول و سکون ثانی و هیم؛
پهلوانی بوده تورانی که خود بمددافراسیاب آهده بمعنی غم واندوه و زحمت سخت و گرفتگی‌دل
بود و افراسیاب اورا به نزديك پیران وه (۷) | ودلگیری باشد ‎٩‏ - وکرفتن اند را نی زگوبند
بجنگه طوی و رستم فرستاد . ازجملهٌ طلب بسیار - وقوي قزح راهم‌میگوش.
گ رگیج ۲ (۳) » یکر اولوسکون | وبفتح اول وثانی » معروف است که درمقابل‌سرد
ثالی وثالث بتحتانی رسیده وبجیم زده » نام‌شهری باشد ۷ ؛ وبپمة «متیهای‌اول | مده است الا قوس
است از شهر های عالم و عربان شغر را مدبته قزح - و بمعنی شتاب و تمجیل نیز کفته‌اند.
خوانند . گرمابان -ب بای ابجد بر وزن
گر گین (4) « بنم اول‌پروزن‌خرجین, گرماوان ‎)٩(‏ » بمعنی حمام باشد وآ ترا گرمایه
نام پهلوانی است ایرانی ۴ - و بفتح اول‌شخصیر| | نیز کوبند - و مخفف گرمابه‌بان هم‌هست که‌استاد
کوبند که صاحب گر باشد بعنی جرب داشته | حمامی باشد ۸ .
باشد۴ چه کین بممنی صاحب هم‌آمده است. گرمابه * - بر وزن سردایه:» بمعنی
گر گینه (0) < بنم اول‌پروزن‌مرشینه. | حمام باشد .
<< شش مر دس دس نحص

(۱) خم ۱: بد روی - (۲) خم ۱:- وسه . (۳) چش :گ رکیج ۰

(2) چش :کرکی . (ه) چش :گر کینه . ‎)٩(‏ خم ۱:گرمادان ۰

۹ «-و۵ع02. رد: فهرست ولف . ۴ - چنین نامی درکتب جقرافیایی بافته
تقد , ظ . مصحف «کر کنج > (۸.م.) ۳ کر کانج (ه.م.)

۴ - پسرمیلاد . رك : فهرست ولف . میلاد بقول نلد که ( حماسهٌ ملی ایران ص ۷ )
محرف مهرداد * ۸11112۳84181 ( نام پادشاه آشکانی ) است اما گرگین بدرستی معلوم نیست
تحربف چه نامی است ؟ رك : دکتر صفا . حماسه‌سرائی در ابران چاپ اول صس 044 - 46 .

۴ - از :گر ۲+ کین ( پسوند اتصاف ) » مخفف آن « کر کن» (ه.م.)

* - ز باران کجا ترسد آن گر که پیر که کر کینه پوشد بجای حرس .

نظامی کنجوی «فرهنگه‌تظام *.

۹ - «گرم : اندوه باشد . فردوسی ( طوسی ) گوید :

ز چنگال بوزان همه دشت غرم دریده براو دل » پراز داغ وگرم.
لغت فرص عم
آقای دهغدا مصراع دوم را چنین تصحیح کرده‌اند : دریده بر و دل ... (* بر؟ بمعنی سینه ).

۷ - بارسی باستان - 827828 ( در - 2202 ] 827322 ) ؛ اوستا - 8276188 ۰
پبهلوی 827712 . هندی باستان - 813873۸ (گرمی) » ارمنی 67170[ ۰ 67108[ (تب) » کردی
وبلوچی 8270 . اففانی 8027302 » استی 862770 » ۹8773 » شفنی 88۳10 » سربکلی
. 80۲ « اسشق ۰۹۱۱ ۸ - «کرمابان وگرماوان » حمام باشد . بدیع
سیف ی گوید .ع : بحرمت رسن و دلو چاه کرمایان . و بعی گفته‌اند بمعنی حمامی است ودراصل
«کرمابه‌بان» و «گرماوموان » بوده . و در بیت مرقوم نیز باندك تکلفی این معنی میتوا ن گفت.»
رشیدی » . ‎٩‏ - از :گرم + آب ۲ ( پسوند مکان) * گرماوه (.م.)
```


## [2026-09-06T15:09:52.741Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 400 BQT_v2_pages.txt; echo; echo \"--- nform feeds:\"; python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint(t.count('\\f'))\nimport re\nprint(re.findall(r'\\[pdf page \\d+\\]',t)[:5])\n\""
}
```


### [2026-09-06T15:09:54.641Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان�
--- nform feeds:
683
[]
```


## [2026-09-06T15:09:58.784Z] TOOL CALL #25: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\nprint(d['BQT'].get('local_file'))\nprint(d['BQT'].get('lookup_hint'))\n\""
}
```


### [2026-09-06T15:10:00.494Z] TOOL RESULT

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
['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-06T15:10:09.803Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nprint(len(blocks))\ndef clean(s):\n    return re.sub(r'[‎‏‪-‮⁦-⁩ـ]','',s)\n# find blocks containing a plausible page number sequence\nfor i in (500,520,540):\n    print('=== block',i)\n    print(clean(blocks[i])[:600])\nEOF"
}
```


### [2026-09-06T15:10:11.535Z] TOOL RESULT

```
684
=== block 500
  سیز۳ه-۱                                                                                      زلدیچی
زندلاف است که بلبل ®  -ومرغان‌خوش‌الحان -               زد خوان‌است که‌تابعان‌زردغت باشند وآن‌جماعت
                 وزسخوان باشد که مجوس است.              را مجوی خوانند  -وبلبل -وفاختهرالیز گویند.
ردوان  = ۴بر وزن رمزدان» بمعنی
                             ن                          الك     ر
                                                                ک و
                                                                  ر ند ببجی ‌ د بفتح اول
باشد -     خته
             فبا -
           
=== block 520
                                          بیان دوم

                در زای فارسی باخای لقطه دار مشتمل بر دو لفت
                  .   ند
                       ینیز
                          گلهورا
                               زاری و نا               رخ = بفتح اول و سکون انی  .مخفف
  زخار ؟ = یکسر اول بر وزن شکار                         آزخ است؛ وآن‌دانه ای باشد سخت وبی ددرکه
دراعضای آدمی بهم میرسد و آنرا بعربی تولول | بان و لعره را گوبند  -و بممنی سختی لیز
                               -صدای | آمده است .
                                                خوالنند  - ۱وآواز حزین وآهته ؟ و



  
=== block 540
       ه
       جاه
         ا ب
           و                                                                                                  ساو آهن
                   بجهت رشتن را درآ تحاگذار ند .
                                                                   ساو آ هن ه بروزن کاوآهن » سونش
» بر وزن لامور  ,کوهی است               ساهور                       وراد آهنی را گویند که ازدم سوهان‌بریزد.
                                                                                                          ی
 درمغرب که ممدن سنگی است بهمین‌نام  .وآن                            ات     بروزن کاوه
```


## [2026-09-06T15:10:18.385Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\ndef clean(s): return re.sub(r'[‎‏‪-‮⁦-⁩ـ]','',s)\nfor i,b in enumerate(blocks):\n    c=clean(b)\n    if 'زه' in c and 'کمان' in c:\n        print(i, c.count('زه'))\nEOF"
}
```


### [2026-09-06T15:10:21.388Z] TOOL RESULT

```
59 2
66 2
88 1
108 1
109 1
151 1
156 2
179 1
194 3
225 2
302 1
305 3
320 1
383 1
426 1
461 1
496 1
508 9
513 3
623 1
627 1
628 1
633 3
```


## [2026-09-06T15:10:24.199Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\ndef clean(s): return re.sub(r'[‎‏‪-‮⁦-⁩ـ]','',s)\nprint(clean(blocks[508]))\nEOF"
}
```


### [2026-09-06T15:10:27.285Z] TOOL RESULT

```
—        4 6٩
                                                                                                               زو
دیگر وعربان کربه خوانند.وبلفت زندویازنه()۱                                    رزبون وحقیر جثه راکونند .
                               لسر همین معنی دارد
                                                           » بمعنی     دننگ
                                                                          روز
                                                                            رو نګ ١ بخ
-ا نانی »جهووسکون‌های
                    روه‌هنك ب                                 زوتزك است که مردم کوزیشت وحفیر باشد.
 کشت
   هوشمند »> درخت و              بر وزن      هوز )(۱        زنوگل ؟  با کاف فارسی ولاءبروزن
وزراعت بالیده پرزور باشد؛ وبفتح های هوز هم                 که مردم کوزیشت         فلندر  ,بمعنی زویگه است
                                           آهده است.                                                   باشد.   وحقر



روبج  ۴۰بنتم اول بر وزن حویج ,                             پروزن تونی  ۰نی زائو               درو لی ۳
          رودهای پراز گوشت و پبه کآنده باشد .


                                                  بیان هفدهم
                 در زای نقطه دار با هامشتمل بر سی وهفت لفت و کنات

است  -وچلهٌ کمان  - ۷و ابرشم  -ورود‌:تابیده                   ن»ی
                                                                علی
                                                                  م ثا
                                                                     بون
                                                                       رهه بکر اول و سک
را ليز کوبند  - ۷کونارة هرچیزهم‌هست همچو                   باداش ندکی است  -و کلمه‌ای باشد که در محل
آن - ۸           ال
                  تفه
                    مه ص
                       اوز
                         ووض
                           زگرهببان و زه ح
                                                            تصین گوبند حمچو آفرین وباركالة ® -وبمعنی
و بفتح اول وظهور ثانی .مکان جوشیدن و بر                     خوب وخوش هم هت  -وزاییدنآ دمی‌وحیوانات
   اتشد.  ‌ی»بآل
               لال
                 سی‌ت
                    اخفا
                       نولو
                          آمدن آب -ریفتح ت ا                دیگر باشد٩ ؛ و باينمعنی بفتح‌اول همآمده
رهاب = بفتح اول بر وزن شهاب ۰                              -به‌عنی نطفه وبجه و فرزند همگفته‌اند
                                                                                              است و
تراوبدن آب باشد اکنزار رودخانه وچشمه‌ونالاب                 ولپذا فرزند را زمزاد و رحم و بچمدانرا زهدان
 -وضم چشمه را گیوزیند
                    وامثال آن ٩ م                         شگوته ٩ ؛ و باین معنی بفتح اول همآمده

                                ها .      وكس:ک-ون
                                                 ( )۷چ                  ( )۱چك :ژند ویاژند .
                          - ۴رك :زونگه » زوترك .               - ۱رکه  :زودگل  .زور که .
    بممنی زالو » چنالکه در سنگری « 60112ك  ۲ .ص .» ۹۸۱طبری                           - ۴لهجه ات

                           ؟  رك  :زواج م رونج ۰                 « 1۷ساب طبری  › 4۰4و رك  :زالو .
                 زه .   احسن ماك کفت      فلك گت             ده    و قدرگفت   کیر   قضا کفت        _    ®

    .    ۰۵۹٩   «شاهنامه بخ ج  4ص

         ۷اوسا ( 32۷1 ۳وتر کمان  ۰رکے)  ¢هندی‌باستان_[8/9-؛                   .     دن
                                                                                     ی:زهرك
                                                                                          ۱
        بازد از (رسمان»نج)       کردی ( 1012زهکمان) .اففانی  : 202بلوچی 8ز «اسشق ۷۷۹6۰
                                                                                        °نامشیوه : ٩ ٩۷۷
                                                 ساق چون بولاد  .بی‌همجون کمان  .رکه همجو زه


        ( وصف اسب) « منوچهری داعفالی . ۸4۰


         ۹ت‌ رك:زهشزه.           ۱     «منتهی‌الارب»   زىق القمیص  4ره يراهن        (   ٥۱    ۲       سنون    ۸۱۷

    (برهان‌قاطع )۱۳۱
```


## [2026-09-06T15:10:37.838Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"γrm\\|grm\\b\" SOD_pages.txt | head -20; echo \"=== search 'warm' in SOD\"; grep -n \"warm\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T15:10:37.920Z] TOOL RESULT

```
=== search 'warm' in SOD
33095:          Anc. Lett. 5.7                                                warmecya ? ©Av. varpmi; Pahl. warm
```


## [2026-09-06T15:10:41.926Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l SOD_pages.txt SOD.txt; grep -n \"yrm\\|Yrm\\|ɣrm\" SOD_pages.txt | head -20; echo ===; grep -n \"^ *4[0-9][0-9][0-9] \" SOD_pages.txt | head -5"
}
```


### [2026-09-06T15:10:41.991Z] TOOL RESULT

```
Exit code 1
  45615 SOD_pages.txt
 111423 SOD.txt
 157038 total
3250:  /anxaz/     Wz-          rise          Olr. *ham-xaz-               /kirm/           kyrm-      snake             Pers. Jb>m (worm)
9505:                                                                             use-k(i)ran    =^xwrsn qyr'n, kyrm
15800:                                                                                                                     yrmy'nCy)
15841:     yarSak ©Khwar. YrSuk; <gard ©abl. YrS\ pi *!»< 4259 yrm B, M                                                             r/
15843:                                                         yarm ©<OP garma-, Khwarz. Yrm-, Yaghn.
15849:4248 Yr5p>       B => yr5y>, yrP-                                       4260 yrmVy       C                            jS «~jj
15855:                                                                        4261 yrm'ych     S (M)                   (^>)f/^lip
15861:                                                                        4262 yrmy'nCy)     B, M                       <^_<-W
15867:                                                                               S W, IIJ 1976, 69 +wnPkrt, "to exil"; Yrmfny,
15872: yrmyh
15874: 4263 yrmyh       B                                     u/     4275 yryn-1 C                                       j.u>
17482:     karmir, karmir (kyrmyr, qrmyr, krmyr) ©Pahl.                            Vim. 123, BSTBL; GMS 1003
17483:       karmir; Yaghn. kimir; Arm. karmir -^qyrmyr                       4849 qrnw'ncy* M, C                                             j* <ojl*.
17511:     kirmist ©pi. =»kyrm-
18197:         free from hatcrd                                            5111 qyrm C *> kyrm-
18198:                                                                     5112 kyrm- B, M, S                                         >
18200:                                                                           kirm, kirm (qyrm) ©<Skt. krmi         ©nom. ob. -y;
18201:    5100 kynpr B                                       j^j/oj^               inst. -J; ace. -w\ pi. qyrmyst
18210:                                                                              57V32-, kyrm\ SCE 145, 358; kyrmw, TSP 13.18
18211:           vengeance, hatred                                         5113 kyrmpwn S                            j^ r 'j>- «j^ ^^
(eval):1: == not found
```


## [2026-09-06T15:10:47.177Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15835,15860p' SOD_pages.txt; echo \"=== page tag:\"; awk 'NR<=15843 && /\\[pdf page/ {p=$0} END{print p}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<15843' | tail -2"
}
```


### [2026-09-06T15:10:48.861Z] TOOL RESULT

```
     y(a)rSak (y5y\ yr'80 ©<Av. gdrdSa                                       xaryose «*xrywsy

       greed2.1207 n pi 84; Hen. Texts. 735              rabbit
       TSP                                               YrYwsk srdy, Bugut. Insc. B2.6; Livsic. AO
                                               *$ iO*J
4247 Yr5»k(h) B, S, M                                      Hung. 26, 1972,73
     yarSak ©Khwar. YrSuk; <gard ©abl. YrS\ pi *!»< 4259 yrm B, M                                                             r/
       YrSyt                                           £
                                                         yarm ©<OP garma-, Khwarz. Yrm-, Yaghn.
     neck
                                                           Yarm ©loc. -v
     TSP 2.226, 549, 1211 etc.; SCE 98, 125; GMS         hot
       1264, 1685; Hen. Tales. 735; ob. -y, Frag. Len.   GMS 526; TSP 2.302, 421, 3.262; SCE 292;
       40.2, 37.9; STSC 132.16                             BSTBL, Dhy. 346; VJ 533
4248 Yr5p>       B => yr5y>, yrP-                                       4260 yrmVy       C                            jS «~jj
4249 Yr5mn(h)         B, M           oU jf cdTW ^jxS, *
                                                                             yarmawe
                                                                             punishment
       yarSman (>yr5mnwh)           ©Av. garo- Smana         ©in             C2, 31V 28 n p77; GMS 1051n 1, 1082
         compd.
                                                                        4261 yrm'ych     S (M)                   (^>)f/^lip
       highest heaven
4250 yr8mrywndy M            S             tjfjrfj                           yarmec
                                                                             (a kind of)hot food
     yarS-marywnde              jj=r <{* '                                   S W, BAI 1990, 286
     Adam's apple
=== page tag:
```


## [2026-09-06T15:10:55.964Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nprint('blocks',len(blocks))\nn=0\nfor i,b in enumerate(blocks):\n    if '4259 yrm' in b or 'yarm ©<OP garma' in b:\n        print('block',i)\nEOF"
}
```


### [2026-09-06T15:10:58.736Z] TOOL RESULT

```
blocks 645
block 234
```


## [2026-09-06T15:11:03.823Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in ترموس ترمومتر ترموستات فیله فرنی پروفیل; do echo \"=== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done"
}
```


### [2026-09-06T15:11:06.294Z] TOOL RESULT

```
Exit code 1
=== ترموس
MON_part2.txt:0
MON_part1.txt:0
=== ترمومتر
MON_part2.txt:0
MON_part1.txt:0
=== ترموستات
MON_part2.txt:0
MON_part1.txt:0
=== فیله
MON_part1.txt:2
MON_part2.txt:2
=== فرنی
MON_part1.txt:3
MON_part2.txt:7
=== پروفیل
MON_part1.txt:0
MON_part2.txt:0
```


## [2026-09-06T15:11:08.541Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"فیله\" MON_part1.txt MON_part2.txt | head; echo ===; grep -n \"فرنی\" MON_part2.txt | head -10"
}
```


### [2026-09-06T15:11:08.601Z] TOOL RESULT

```
Exit code 1
MON_part1.txt:35603:پیله: ()ه [- بیله - پله - فیله - فیلجه - 
MON_part1.txt:62082:دفیله: »۵0171 (.) عمل گذشتن سربازان؛ 
MON_part2.txt:2103:غفیله: «ارهاهر (ع. غفیلة] (ا.) نمازی است 
MON_part2.txt:9679:فیله: (-):۱1 (.) گوشتی لطیف و لغزان که 
(eval):1: == not found
```


## [2026-09-06T15:11:11.257Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9675,9685p' MON_part2.txt; echo \"=== فرن/فر\"; grep -n \"^فرن:\\|^فر:\\|^فرن \\|فارینه\" MON_part1.txt MON_part2.txt | head -20"
}
```


### [2026-09-06T15:11:11.342Z] TOOL RESULT

```
(حامص.) عمل و شغل فیلم‌برداری. شرکت 
( کمپانی) فیلم‌برداری: شرکتی که سرمايةٌ آن 
صرف تهبة فیلم گردد. 

فیله: (-):۱1 (.) گوشتی لطیف و لغزان که 
در حیوان قرار دارد و از آن مخصو صاً برای 
کباب استفاده کنند. 

فین: (.) (عم.) آب بینی. 

فینال: ا11:7 [نهایی» آخری|(ص..) (ور.) 
=== فرن/فر
MON_part2.txt:5398:فر: 11 ( یش .) ۳ سر کلمات در ينك و 7 3 
MON_part2.txt:5403:فر: (1۸0 |- فره - خره| ).٩(‏ خره. طبق 
MON_part2.txt:5424:فر: ۱:۳ |- پر ] ( پر (مرخ): 
MON_part2.txt:5427:فر: ٩:‏ |اهن | (.) آلت آهنین برای داغ 
MON_part2.txt:5438:فر: (۲۲:] (اصت 
MON_part2.txt:11895:فر: ۲(ص.) (عم.) فرو رفته. 
MON_part2.txt:12441:فرن: (ع.] )۱( 0 از زمان معادل
```


## [2026-09-06T15:11:14.164Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5396,5450p' MON_part2.txt; echo \"==== 12435\"; sed -n '12435,12455p' MON_part2.txt"
}
```


### [2026-09-06T15:11:14.233Z] TOOL RESULT

```
فر: 11 ( یش .) ۳ سر کلمات در ينك و 7 3 
اصل به معنی «پیش» بوده: فرخجسته. (یشف.) 
بر سر افعال در آید و آن در اصل به معنی 
«بیش» بوده: فرسودن. 

فر: (1۸0 |- فره - خره| ).٩(‏ خره. طبق 
مندرجات زامیادیشت (اوستا) فر چنین 
تعریف می‌شود: «فر فروغی است ایزدی: به 
دل هر که بتابد از همگنان برتری یابد. از 
بر تو این فروع است که شخص به پادشاهی 
رسد شاسته تاج و تخت گردد. استافین 
ی ها گر شود و همواره کامیات و 
پیروزمند باشد و یز از پیروی این نور است 
که کسی در کمالات نفسانی و روحانی کامل 
هه از سول ات یی انم 
شود.» فر ابرانی ۰ با فرة ایرانی طنق معتقدات 
ایرانیان باستان فری است که از چهارپایان و 
گله و رمه و ثروت و شکوه برخوردار و 
سخشنده خرد و دانش و دولت و درهم 
شکنندهٌ غیر ایرانی است. فر ایزدی: همان فر 
پا خره است. فر کیان ( کیانی): با فرة کیانی فر 
ایز دی که به بادشاهان و سران و فر وا 
کشور اختصاص دارد و موجب کامیابی و 
بروزی 9 2 ۳۲ مشق کت حسن ‏ 
زیبایی. 

فر: ۱:۳ |- پر ] ( پر (مرخ): 

فر : (۱:۸:6 |ع.] ۲۹ مزار. 
فر: ٩:‏ |اهن | (.) آلت آهنین برای داغ 
0 اتو. (ف.) نوعی احاق خوراک یزی 


که با کاز (نفت) کار کند. (ف.) چین و شک 
مور ی. 
ثر: (۱۲)۲ (.) قر و فر: (عم.) عنج و دلال. 


تا زگی. نوی. 

فر: (۲۲:] (اصت 
فراورده. ()۸۲-۱۷۸۱)۵(۲۸] (امف.) فراهم 
اورده. محصول ( کسافزرخ ت صنعتی ) 


) (عم.) آواز گرفتن اخلاط 


۱۰ ۱ 
ضح. ۳ یافته. 
فرا: 1*۲2 (پشف.) بر سر فعل درآید و آن در 
اصل به معنی به؛ سویء در باشد. (حر. اض.) 
ده زر دبکگا بیش. به با. سوی» جانت. 
==== 12435
فر مه سبزی: آ2تهع-. [تر. ف.] (امر.) نوعی 
خورش است که از گوشت و تره و جعفری 
و شنبلیله درست کنند. بوی قرمه‌سزی دادن 
سر (کلة) کسی: (عم.) بسیار متکبر بودن 
وی» افاده سیار داشتن او 

فرن: (ع.] )۱( 0 از زمان معادل 
سی سال. صد سال (اینکث بدین معنی 
متداول است.) سده. باره‌ای از زمان؛ عهد» 
دوران» دوره؛ ج. دوره. 

فرد: 7210 [ع.] )۱( شاخ» سرون. تندی سر 
مردم که به منزلةٌ جای سرون جانور است؛ 
زبر سر. گیسوء موی بافته. نوک مو. سر کوه. 
کرانه قرص آفتاب و بالای آن. آنجه 
نخست پیدا شود از شعاع آفتاب. رثیس 
قوم» مهتر 

قرن: ۸5« |معر.] (.) (گیا.) زغال اخته. 

فر د: 2 [ع.] (.) شتری که آن را با شتر
```


## [2026-09-06T15:11:29.285Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"فرن\" MON_part2.txt | head -30; echo \"=== فارینه\"; grep -rn \"فارینه\" MON_part1.txt MON_part2.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head"
}
```


### [2026-09-06T15:11:29.370Z] TOOL RESULT

```
1377:موسیقی. . فرنگ و غریو؛ آه و اله و فر باد. 
6008:فرنسحی: ۳۹۹ (حامص.) زرشتی» 
6612:فرناد: ۵ با باب. ضح.- به معنی «یایان» 
6626:فرناس: 5 [ناید ید شدن] (ص.) غافل» 
6629:فرناس: 5 القس. خرناس» خر ناسه» 
6633:فرناس: 5 (.) مهتر روستایبان. . سیر 
6636:فرنج: : [2۲20) [قس. فرانج» فرهنگ] (1.( 
6640:فرنج: آجعع] (۱.) نیم تنة نظامی. 
6642:فرنج: 0۳031) (.) بیرامون دهان» گرداگرد 
6645:فرنحک: 2۵21) [- فر ونجکك» قس. 
6702:فرند: ۳:4] [- افرند» معر. پرند] جوهر 
6707:«فرنگی» بکار رود؟ ج. فرنگان. 
6709:فرنگ: 8۵ (.) باز یجه‌ای است برای 
6718:ی ۲ 1:72 [فنر. ف. - افرنگی] 
6721:(ص‌نسب.) منسوب به فرنگ. فرانسوی. 
6730:فرنی] ((.) خوراکی است رقیق. طرز تهیه: 
6739:فرنی: -0۳) [ع. ف.] (ص‌نسب. ا.) نانی که 
6740:در فرن پخته باشند» نان گرده ستبر با نانی که 
6743:شرنیه: (۵-)0۲۱۲۷۷۵] [ع. . فرنبه ] (.) نان 
6958:فروله: ۱0۷() [ع.] (گیا.) توت فرنگی. 
7010:از آنکه اهورمزدا جهان خاکی را بیافرند 
8509:انگلیسی؛ فلفل افرنجی» فلفل ژامائیکك» 
8543:رومی» فلفل فرنگی» فلفل قرمز هندی» هند 
8880:توت فرنگی. . صح. بقنلای میوه وفنی که ه 
12441:فرن: (ع.] )۱( 0 از زمان معادل 
12501:قفرنفل معمولی» حسن بوسف. قرنفل 
12505:( گیا.) دانه‌های فرنجمشگ را گویند که بنام 
12514:قرنفل بستانی: (گیا.) فرنجمشکث. قرنفل 
12517:فرنیز: 2 [ع. فرناس] (.) (معم.) 
14287:ترکیات اسمی: قلم سرب: قلم فرنگی. قلم 
=== فارینه
```


## [2026-09-06T15:11:32.305Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6726,6750p' MON_part2.txt"
}
```


### [2026-09-06T15:11:32.376Z] TOOL RESULT

```
(ص‌مر.) کسی که به آداب اروپاییان عمل 
کند؟ متححد د. 

شرنی: 6۳6 اظ.. بنام واضع آن» قس. 
فرنی] ((.) خوراکی است رقیق. طرز تهیه: 
آرد برنج را به قدر ضرورت در کمی شیر 
حل کرده و داخل شیر زده ده دقمقه 
می‌جوشانند و نزدیکك پختن هل و گلاب و 
قند زده س از دو سه جوش برمی‌دارند با 
بدون قند کشیده با شیر صاف می‌کنند. در هر 
يکث لیتر شیر دویست گرم آرد برنج کافی 
است؛. 

فرنی: -0۳) [ع. ف.] (ص‌نسب. ا.) نانی که 
در فرن پخته باشند» نان گرده ستبر با نانی که 
کرانه‌هایش را در میان فراهم آورند و بریان 
کرده به روغن و شیر شکر تر سازند. 
شرنیه: (۵-)0۲۱۲۷۷۵] [ع. . فرنبه ] (.) نان 
کلیچة گرد و بزرگ» ج. فرانی 

فرو: ۷ (ع.] ).٩(‏ پوستین» پوستین روباه. 
جامه‌ای که از پوست جانوران سازند؛ ج. 
فراء. 

فرو: ۲055 [- فرود] (پشف.) بر سر افعال
```


## [2026-09-06T15:11:44.244Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHN p.187 -> leaf 218\"; awk 'BEGIN{RS=\"\\f\"} NR==219' PHN.txt | head -40"
}
```


## [2026-09-06T15:11:45.870Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD gwher\"; grep -n -i \"gwher\\|g^wher\\|ghwer\\|gwher-\" AHD_watkins1985.txt | head; grep -n \"thermos\\|therm\" AHD_watkins1985.txt | head -10; echo \"== AHD gwhi\"; grep -n \"filum\\|fīlum\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T15:11:46.555Z] TOOL RESULT

```
== PHN p.187 -> leaf 218
GRE 187
termes identiques semble confirmer naturellement l'origine
arabe du verbe français , que plusieurs étymologistes attribuent
au grecypà[(peiv (^mre), tandis que, dans cette dernière langue,
graver se dit spécialement y\i(puv ou yXu^eiy, d'où vient le
substantif masculin glyphe, trait gravé en creux,
GREDIN, E, subst. (a.)
^tXi [g^Wfr] trompeur, traître, perjlde; dérivé dej«Xfc [ghadar]
tromper, trahir. — L'explication fournie par plusieurs diction-
naires français sur le sens de ce mot paraît manquer de jus-
tesse. Gredin, disent-ils, désigne un homme sans naissance, un
gueux, et, par extension, un homme sans probité, sans honneur;
mais cette dernière acception est la seule qui soit admissible
au fond, puisque gredinerie, s. f., s'emploie vulgairement pour
acte d'improbité, de friponnerie. — Ils considèrent gredin comme
une corruption de gradin, et ajoutent, à l'appui de leur opinion ,
que certains valets au service de grands personnages se tenaient
autrefois sur les gradins ou degrés du château de leur seigneur
en attendant ses ordres, ce qui leur a valu le surnom de gra--
dins ou gredins. Cette raison me parait bien peu solide; car
gredin, aussi bien que son correspondant arabe j^^X^ [ghadir^
désigne un homme perfide, sans probité, qu'il soit riche ou pauvre,
maître ou serviteur. — Les Arabes ont encore d'autres formes
d'adjectifs dérivés de la même racine et donnant le même sens;
mais celui que je viens d'indiquer est, je crois, le type du cor-
respondant français, que l'on obtient par la permutation de la
dernière radical*» ^ r en w. Il ne faut pas oublier non plus que,
```


### [2026-09-06T15:11:46.624Z] TOOL RESULT

```
== AHD gwher
143:Indo-European had a generic term for “wild animal,” ghwer- (FERAL). The wolf was known and evidently feared; its name is subject to taboo deformation (conscious al- teration of the form of a tabooed word, as in English gol-derned, dad-burned). The vari- ant forms wlk’o-, *lupo-, and wlp- (also “fox”), are all found. The name of the bear was likewise subject to a hunter’s taboo: the animal could not be mentioned by its real name on the hunt. The southern Indo- European languages have the original form, rtko- (Latin ursus, Greek arktos), but all the northern languages have a substitute term. In Slavic the bear is the “honey-eater,” in Germanic the “brown one” (BEAR, and note also BRUIN).
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
798:fixed form *ok-to- in Greek optos, seen, visible: OPTIC; CATOPTRIC, DIOPTER, OPTOMETRY, PANOPTIC. 6. Suffixed form *okv-d in Greek opé, opening: METOPE. 7. Suffixed form *okv-mn in Greek omma (< *opma), eye: OMMA- TIDIUM, OMMATOPHORE. 8. Greek ophthalmos, eye (with taboo deformation): OPHTHALMO-; EXOPHTHALMOS. 9. Zero-grade form *ok- (of oldest full-grade form *zok-) in: a. Latin antiquus, “appearing before, having prior aspect,” former (*anti-, before; see ant-); b. Latin atréx, “black-looking,” frightful (*atro- black; see ater-); c. Latin ferdx, “wild-looking,” fierce (*ghwero-, wild; see ghwer-). [Pok. ok+- 775.]
1321:BRAIN mregh-m(n)o- BRAISE bhreu-2 BRAKES bhreg- BRAKE‘ bhreg- BRAMBLE bhrem-2 BRAND gWher- BRANDISH gWher- BRANDY gWher- BRASS ferrum BRASSARD mregh-u- BRASSIERE mregh-u- BRATWURST bhreu-2 BRAWN bhreu-2 BRAY? bhreg- BRAZE? bhreu-2 BRAZEN ferrum BRAZIER! ferrum BRAZIER? bhreu-2 BREACH bhreg- BREAD bhreu-2 BREAK bhreg- BREAKFAST past- BREAM! bherak- BREAST bhreus-1 BREATH gWhré- BREATHE gWhré- BRECCIA bhreg- BREECH brak- BREED bhreu-2
1323:BREEKS brak- BREEZE bhreu-2 BREGMA mregh-m(n)o- BREMSSTRAHLUNG | ster-2 BREW bhreu-2 BREWIS bhreu-2 BRIAR! wer-3 BRIDE? bherek- BRIDEGROOM dhghem- BRIDGE! bhri- BRIDLE bherek- BRIEF mregh-u- BRIGHT bherag- BRIM bhrem-2 BRIMSTONE gWher- BRINDLED gWher- BRING bher-!
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1506:FENCE gWhen-! FENNEL dhé@(i)- FENUGREEK dhé(i)- -FER bher-1 FERAL ghwer- FER-DE-LANCE ferrum FERE per-2
1507:FERIA dhés- FERMATA dher-2 FERMENT bhreu-? FERN per-2 FEROCIOUS ghwer- FERRET! bher-1 FERRET? bhel-3 FERRI- ferrum FERRO- ferrum FERROUS ferrum FERRUGINOUS ferrum FERRULE wei-1 FERRY per-2 FERTILE bher-1 FERVENT bhreu-2 FERVID bhreu-2 FERVOR bhreu-2 FEss bhasko- -FEsT dhés- FESTAL dhés- FESTINATE bhers- FESTIVAL dhés- FESTIVE dhés- FESTOON dhés- FETAL dhé(i)- FETCH! ped-1 FETE dhés- FETICIDE dhé(i)- FETISH dhé-1 FETLOCK ped-! FETTER ped-1 FETTLE ped-2 FETUS dh@(i)- FEUD! peig-2 FEUD? peku- FEUILLETON bhel-3 FEVERFEW bheug-! FEW pau-
1509:FicHu dhig¥- FICKLE pelg-2 FICTILE dheigh- FicTION dheigh- -FID_ bheid- FIDELITY bheidh- FIDUCIAL  bheidh- FIDUCIARY bheidh- FIELD pele-2 FIELDFARE wer-4 FIEND pé@(i)- FIERCE ghwer- Fiesta dhés- FIFE pipp- FIFTEEN penkWe FIFTH penkwe FIGHT pek-2 FIGMENT dheigh- FIGURE dheigh- FILAMENT gWhi- FILAR gWhi- FILARIA gWhi- FILE! gWhi- FILE? peig-1 FILES pu-2 FILIAL dh@(i)- FILIATE dhé(i)- FILIBUSTER pri- FILIFORM gWhi- FILIGREE gre-no-, g¥hi- FILL pele-1 FILLET gWhi- FILLY pau-
1530:FORCEPS gWher- FORCIPATE gWher- FORD per-2
84:A characteristic feature of Indo-European was the system of vocalic alternations termed apophony or ablaut. This was a set of internal vowel changes expressing different morphological functions. A clear reflex of this feature is preserved in the English strong verbs, where, for example, the vocalic alter- nations between write and wrote, give and gave express the present and past tenses. Ablaut in Indo-European affected the vowels e and o. The fundamental form was e; this e could appear as o under certain conditions, and in other conditions both e and o could disappear entirely. On this basis we speak of given forms in Indo-European as exhibiting, respectively, the e-grade (or full grade), the o-grade, or the zero grade. The e and the o might furthermore occur as long é or 6, termed the lengthened grade.
463:eti. Above, beyond. 1. Germanic *ith- in Old Norse idha, whirlpool: EDDY. 2. Latin et, and (< “furthermore”): ET CETERA. [Pok. efi 344.]
547:brand, piece of burning wood, sword: BRAND; b. Old Norse brandr, piece of burning wood, akin (in the sense “blackened by fire,” dark-colored) to the possible Scandi- navian source of Middle English brende, brindled: BRIN- DLED; c. Dutch branden, to burn, distill: BRANDY; d. Old French brand, sword: BRANDISH. 3. Suffixed form *gvher-mo- in Greek thermos, warm, hot (> thermé, heat): THERM, -THERM, THERMO-, -THERMY; HYPOTHER- iA. 4. O-grade form *gvhor- in Latin forceps, pincers, fire tongs (< “that which holds hot things”; -ceps, agential suffix, “-taker”; see kap-): FORCEPS, FORCIPATE. 5. Suffixed o-grade form gvhor-no- in: a. Latin fornus, fornéx, oven: FORNAX, FURNACE, HORNITO; b. probably Latin fornix, arch, vault (< “vaulted brick oven”): FORNICATE. [Pok. g¢her- 493, bhereu- 143.]
== AHD gwhi
548:gvhi-. Thread, tendon. Suffixed form *gwhi-slo- in Latin filum, thread: FILAMENT, FILAR, FILARIA, FILE!, FILLET,
```


## [2026-09-06T15:11:57.114Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '548,552p' AHD_watkins1985.txt"
}
```


### [2026-09-06T15:11:57.156Z] TOOL RESULT

```
gvhi-. Thread, tendon. Suffixed form *gwhi-slo- in Latin filum, thread: FILAMENT, FILAR, FILARIA, FILE!, FILLET,
g“hré-
FILOSE, FILUM; DEFILE*, ENFILADE, FILIFORM, FILIGREE, FILOPLUME, PROFILE, PURFLE. [Pok. gvheia- 489.]
ghré-. To smell, breathe. Contracted from *gvhreo-. Germanic suffixed form *bré-thaz in Old English bréth, odor, exhalation: BREATH, (BREATHE).
g¥hren-. To think. 1. Greek phrén, the mind, also heart, midriff, diaphragm: (FRANTIC), FRENETIC, FRENZY, -PHRENIA, PHRENO-; EUPHROSYNE, (PHRENITIS). 2. Ex- tended zero-grade root form *gvhrn-d- in Greek phra- zein, to point out, show: PHRASE; HOLOPHRASTIC, METAPHRASE, PARAPHRASE, PERIPHRASIS. [Pok. g¥hren- 496.]
```


## [2026-09-06T15:11:58.597Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^FOUR\\|FOUR, subst\\|FOURNEAU\\|furnus\\|fournil\" PHN.txt | head -20; echo \"=== leaf count\"; python3 -c \"\nt=open('PHN.txt',encoding='utf-8',errors='replace').read(); print(t.count('\\f'))\""
}
```


### [2026-09-06T15:12:00.238Z] TOOL RESULT

```
4974:FOUR, s. m. (a.)
5007:FOURBE, adj. des 2 g. (p.)
5020:FOURREUR, s. m. (a.)
=== leaf count
437
```


## [2026-09-06T15:12:06.069Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4960,5010p' PHN.txt; echo \"=== which leaf\"; python3 -c \"\nt=open('PHN.txt',encoding='utf-8',errors='replace').read()\ni=t.find('FOUR, s. m.')\nprint('leaf', t[:i].count('\\f'))\n\""
}
```


### [2026-09-06T15:12:08.030Z] TOOL RESULT

```
lieu ou l'on reçoit tout le mande, ou toute espèce de marcliandises.
— Quelques dictionnaires portent aussi fondique; mais l'ortho-
graphe fondouque me semble préférable , d'autant plus qu'on
appelleyî>un(bti^/y( JJitXÂi), mot évidemment dérivé de foun-FOU 167
tlotuf, une monnaie turque valant environ trente-ciu<| piastres
actuelles du Grand Seigneur.
POSTAT, n. pr. (a.)
LUa^MJ [foust'ât\ Ville d'Egypte sur la rive droite du Nil, à
!i kilomètres au sud-ouest du Caire. — Le mot ^Ua^M» [fous-
t'ai! ] signifie tente en étoffe grossière de coton, et la ville fut ainsi
appelée à cause du camp composé de tentes de ce genre, et
établi sur son emplacement par Amrou ben As, lieutenant du
khalife Omar, lors de la conquête de l'Egypte. Amrou mourut
en 663 de l'ère chrétienne.
FOUR, s. m. (a.)
U^ LA'i^^'O ^^^ arabe qui paraît avoir donné naissance au
latin yûrnu^ onfonius, que les dictionnaires présentent comme
racine du français ybur. Le latin yùrnu^ n'a , je crois, rempli
qu'un rôle secondaire; mais ses dérivés se retrouvent dans le.s
langues néo-latines, comme on le verra ci-après.
Le four est un lieu voûté, avec une seule ouverture par de-
vant, et que l'on fait chauffer pour y cuire le pain, la pâtis-
serie, etc. — Comparez l'espagnol homo (anciennementj/bn*o),
le portugais et l'italien ybnio.
On appelle fournaise, s. f., un four considérable, destiné h
recevoir un très-grand feu, et servant à cuire la chaux, la
brique, le plâtre, etc., ou à fondre les métaux. — Ce mot a
pour correspondants l'espagnol homaza, le portugais yôrna/Zm,
et YiiaMen fornace , qui représente, comme on le sait, l'ablatif
du latin /br/m.r.168 ' FOU
Fouknëau, s. m., se dit ordinairement du meuble de cui-
sine sur lequel on cuit les aliments; le combustible qu'on y
met repose sur une grille à travers laquelle passe la cendre. —
(iomparez l'espagnol hornillo, le portugais forntUio, et l'italien
fornello.
Le mot foorniSe, s. f., désigne la quantité de pain que l'on
peut faire cuire à la fois dans un four. — Les Espagnols
écrivent homada, les Portugais fomada, et les Italiens tii-
FouRNiER, ÈRE, S., indique celui ou celle qui tient un four
public pour y faire cuirt' le pain préparé chez les particuliers.
— Ce mot a pour correspondants homero en espagnol , for-
miro en portugais, eifoîiuijo en italien.
Fournil, s. m., se dit du lieu oii est le four et où l'on pétrit
la pâte.
Enfin le verbe enfourner , mettre au four, a pour correspon-
dants l'espagnol hornear, le portugais ybrwryar ei fomear, ainsi
que l'italien infornare,
FOURBE, adj. des 2 g. (p.)
Uj^ [y&i6a] trompeur, qui trompe avec finesse, avec adresse, —
Voyez Fripon. — L'adjectif italien yurio, qui exprime la même
idée, a bien pu servir d^intermédiaire entre le persan et le
=== which leaf
leaf 198
```


## [2026-09-06T15:12:40.481Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1276,1284p' KNT.txt; echo \"=== leaf/page\"; python3 -c \"\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\\\"name Garma-pada-\\\")\nleaf=t[:i].count('\\f')\nprint('leaf',leaf)\nseg=t.split('\\f')[leaf]\nimport re\nprint(re.findall(r'\\b1[5-9][0-9]\\b', seg)[:10])\n\""
}
```


### [2026-09-06T15:12:42.890Z] TOOL RESULT

```
OP bajim ‘tribute’. pIE *dhrougho-, OP drauga ‘the Lie, and with
palatal suffix -eno-, draujana- ‘follower of the
Lie’; adurujiya ‘he lied’, denommative verb
to the stem seen in Av. (ace.) Druj-tm ‘Devil’. pIE *yhormo- ‘heat’, Skt. gharmá-s, OP month-
name Garma-pada-, c£. Lt. formus ‘hot’. pIE root *g*hen- ‘strike’, OP ja"tiy, Skt. Айли;
OP 3d sg. imf. ија", Skt. dhan; pIE *g#hn-
dh (imv.), OP jadiy, Skt. jaht (Skt. 7 by
Grassmann’s Law, $73.1V),
Other examples of g and у could be added, but these are adequate.
=== leaf/page
leaf 51
[]
```


## [2026-09-06T15:12:47.322Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Garmapada- sb\\|Garmapada-, name\\|Garmapada- s\\|garma- \\|‘heat’\" KNT.txt | head -20"
}
```


### [2026-09-06T15:12:47.374Z] TOOL RESULT

```
585:By the Avestan and Skt. cognates: afar, Skt. атат; garma- in Garmapadahya, Skt. gharmá-; дата-, Av. sarad-; darga-, Av. daraga-, Skt. dirghd-; baršnā, Av. instr. barasna; martiya, Skt. mártya- .
1279:to the stem seen in Av. (ace.) Druj-tm ‘Devil’. pIE *yhormo- ‘heat’, Skt. gharmá-s, OP month-
5369:'"üzu. From garma- ‘heat’, Av. garama-, Skt. gharmá-, Lt. formus ‘hot’, NEng. warm, pIE *gthormo-, cf. Gk. bepuos (with analogical -e-), + pada- ‘step, station’ ($29, §31, $149.1, $161.Ib, $165): ‘Heat-Station Month’. — Garmapadahya gsm, DB 1.42; 3.71, 46.
```


## [2026-09-06T15:12:52.388Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\\\"From garma- 'heat'\\\")\nif i<0: i=t.find('From garma-')\nleaf=t[:i].count('\\f')\nprint('leaf',leaf)\nseg=t.split('\\f')[leaf]\nprint(seg[:200])\nprint('...')\nprint(seg[-200:])\n\""
}
```


### [2026-09-06T15:12:54.195Z] TOOL RESULT

```
leaf 206
n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46).
рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f.
ham- + gam- ‘come
...
4, $113, 5191.11, §201, 6998.11). In the following combinations: aciy (q.v.) ХРЇ 21. aniyaš-ciy nsn. DB 4.46; XPa 13; aniya&-c (452.1) XPh 41f; aniyai-ciy npm. XPf 29. avas-ccy nsn. DNb 55; asn. DNb 5
```


## [2026-09-06T15:13:13.161Z] TOOL CALL #47: Bash

```json
{
 "command": "pdftoppm -f 216 -l 216 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg216 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T15:13:13.189Z] TOOL CALL #48: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:13:15.724Z] TOOL RESULT

```
total 1744
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:13 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    418 Sep  6 11:13 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
```


### [2026-09-06T15:13:15.732Z] TOOL RESULT

```


```


## [2026-09-06T15:13:18.851Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg216.png"
}
```


### [2026-09-06T15:13:19.261Z] TOOL RESULT

```

```


## [2026-09-06T15:13:19.259Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:13:37.297Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0er-",
 "prompt": "Give the reconstructed root, its meaning, and the full list of derived terms/descendants (Avestan, Old Persian, Greek, Latin, Germanic). Quote the etymology section verbatim where possible."
}
```


## [2026-09-06T15:13:38.444Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%86",
 "prompt": "For the Arabic entry فرن (furn) and any Persian entry: quote the etymology verbatim — is it a borrowing from Greek phournos / Latin furnus, or a native word? Also quote any Persian فرن entry."
}
```


### [2026-09-06T15:13:43.459Z] TOOL RESULT

```
# Proto-Indo-European Root *gʷʰer-

**Reconstructed Root:** *gʷʰer-

**Meanings:**
1. "to be warm"
2. "to become warm"

**Derived Terms & Descendants:**

The document lists 78 derived terms across multiple language families:

- **Albanian:** ziej (from Proto-Albanian *džera)
- **Celtic:** gʷereti forms (Proto-Celtic)
- **Greek:** θέρω (thérō), θέρομαι (théromai) from Proto-Hellenic *kʷʰérō
- **Balto-Slavic:** garḗˀtei (Proto-Balto-Slavic), grěti (Proto-Slavic)
- **Sanskrit:** जिघर्ति (jighárti) and घृ (ghṛ, "to shine, burn")

**Note:** The page does not provide specific entries for Avestan or Old Persian descendants, though Indo-Iranian forms are documented through Sanskrit reflexes.
```


### [2026-09-06T15:13:44.419Z] TOOL RESULT

```
# Etymology of فرن (furn)

Based on the Wiktionary content provided:

**Arabic فرن (furn)** is a borrowing. The etymology states: "From Aramaic פורנא / ܦܘܪܢܐ (pūrnā), from Ancient Greek φοῦρνος (phoûrnos), from Latin furnus."

The word traces back through a chain of borrowing: Latin → Greek → Aramaic → Arabic, ultimately deriving from Proto-Indo-European *gʷʰr̥nós (meaning "warm").

**Regarding Persian:** The document does not include a Persian entry for this word, so I cannot provide a quote about any Persian فرن.
```


## [2026-09-06T15:13:50.048Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/four",
 "prompt": "Quote verbatim the French noun 'four' (oven) etymology section. Is it from Latin furnus / Old French forn? Any mention of Arabic?"
}
```


## [2026-09-06T15:13:51.288Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/filum",
 "prompt": "Quote verbatim the Latin noun fīlum etymology and its descendants (French fil, Italian filo, English file/filament), and the PIE reconstruction given."
}
```


### [2026-09-06T15:13:54.711Z] TOOL RESULT

```
# French 'four' Etymology

I cannot locate the French etymology section for "four" (oven) in the provided content. While the page contains extensive translations and a French section header, the actual etymology subsection for the French noun appears to be truncated or not fully included in the material you provided.

The document cuts off mid-translation list and doesn't display the complete French etymology details that would clarify origins from Latin *furnus*, Old French *forn*, or any Arabic connections.
```


### [2026-09-06T15:13:57.014Z] TOOL RESULT

```
# Latin Etymology and Descendants of Fīlum

## Etymology
"From Proto-Italic *fī(s)lom, from Proto-Indo-European *gʷʰiH-(s)lo- ("sinew")."

## Selected Descendants

**French:** The entry lists Old French *fil* with a note directing to that entry for additional descendants, which would include modern French *fil*.

**Italian:** Listed as *filo* and *fila* in the Italo-Dalmatian branch.

**English:** The entry shows English *filum* as a borrowing from Latin, with a related entry noting that *file* is a doublet of *filum*.

The Indo-European root reconstruction provided is "gʷʰiH-(s)lo-," which the source document translates as meaning "sinew."
```


## [2026-09-06T15:14:01.211Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://fr.wiktionary.org/wiki/four",
 "prompt": "Quote verbatim the French noun 'four' etymology section (Étymologie). From Latin furnus? Any mention of Arabic?"
}
```


## [2026-09-06T15:14:02.539Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%87",
 "prompt": "Quote verbatim the Persian entry زه (zeh) 'bowstring': its etymology, Middle Persian and Avestan/Sanskrit forms, and the Proto-Iranian/PIE reconstruction."
}
```


### [2026-09-06T15:14:06.800Z] TOOL RESULT

```
# Etymology of French "four"

According to the Wiktionnaire article, the French noun "four" (meaning oven) comes from Latin:

> "Du latin _[fŭrnus](https://fr.wiktionary.org/wiki/furnus#la "furnus")_."

The entry notes that the 'n' sound persists in related French words like "fourneau," "fournil," "enfourner," and "fournier."

**Regarding Arabic:** The document makes no mention of Arabic in the etymology section for the French noun "four." However, the translations section does list an Arabic equivalent: فرن (furn), but this appears to be a translation rather than an etymological connection.
```


### [2026-09-06T15:14:10.917Z] TOOL RESULT

```
# Persian زه (zeh) - Bowstring Entry

**Etymology:** The entry states it is "[Inherited](/wiki/Appendix:Glossary#inherited "Appendix:Glossary") from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[𐭦𐭩𐭧](/wiki/%F0%90%AD%A6%F0%90%AD%A9%F0%90%AD%A7#Middle_Persian "𐭦𐭩𐭧")_ (zyḥ /⁠zīh⁠/)."

**Cognates listed:** "Cognate with [Avestan](https://en.wikipedia.org/wiki/Avestan "w:Avestan") _[𐬲𐬌𐬌𐬁](/w/index.php?title=%F0%90%AC%B2%F0%90%AC%8C%F0%90%AC%8C%F0%90%AC%81&action=edit&redlink=1 "𐬲𐬌𐬌𐬁 (page does not exist)")_ (žiiā, "bow-string, tendon")" and "[Sanskrit](https://en.wikipedia.org/wiki/Sanskrit "w:Sanskrit") _[ज्या](/wiki/%E0%A4%9C%E0%A5%8D%E0%A4%AF%E0%A4%BE#Sanskrit "ज्या")_ (jyā́)."

**Reconstruction:** The document references "[Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language")" but does not explicitly provide a PIE reconstruction for this particular sense. It cites Proto-Iranian sources for other etymologies but not for this bowstring definition.
```


## [2026-09-06T15:14:22.150Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D8%A7%D8%B1%DB%8C%D9%86%D9%87/",
 "prompt": "Does the Persian word فارینه exist? Quote any dictionary entries (Dehkhoda, Mo'in, Amid) for فارینه, with their glosses and any etymological tag."
}
```


## [2026-09-06T15:14:23.153Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/profile",
 "prompt": "Quote the etymology of 'profile' verbatim: Italian profilo/profilare, Latin filum, and the sense development."
}
```


### [2026-09-06T15:14:28.872Z] TOOL RESULT

```
# Etymology of "Profile"

**Italian Origin:**
"from older Italian _profilo_ 'a drawing in outline,' from _profilare_ 'to draw in outline'"

**Latin Component:**
The Italian _filare_ derives "from Late Latin _filare_ 'to spin, draw out a line,' from _filum_ 'thread'"

**Sense Development:**

The word progressed through distinct meanings over time:

1. **1650s** – Initial sense as "a drawing of the outline of anything," particularly "a representation of the human face in side view"

2. **1660s** – Evolved to mean "a side view"

3. **1734** – Extended to "biographical sketch, character study"

The semantic shift moved from a visual/artistic representation toward descriptive written accounts of individuals, demonstrating how the concept of capturing an outline or essential representation expanded from the visual to the literary domain.
```


### [2026-09-06T15:14:34.815Z] TOOL RESULT

```
# Response

Based on the content provided, **no dictionary entry for فارینه is explicitly shown**. 

The webpage is a dictionary entry *about* the word فارینه from Abadis Dictionary, but it does not include actual glosses or definitions from Dehkhoda, Mo'in, or Amid dictionaries. 

The page references these sources in its general description: "دیکشنری آبادیس شامل... لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید" (Abadis Dictionary includes Dehkhoda lexicon, Mo'in dictionary, Amid Persian dictionary), yet specific dictionary entries for this particular word are absent from the excerpt provided.

The only substantive content shown is an etymology section attributing the word to Turkish language influence on Persian.
```


## [2026-09-06T15:14:40.127Z] TOOL CALL #58: WebSearch

```json
{
 "query": "\"فارینه\" دهخدا نان"
}
```


### [2026-09-06T15:14:47.852Z] TOOL RESULT

```
Web search results for query: ""فارینه" دهخدا نان"

Links: [{"title":"چرا نان باگت نماد فرانسه است؟ تاریخچه و اهمیت","url":"https://www.asriran.com/fa/news/1131821/%DA%86%D8%B1%D8%A7-%D9%86%D8%A7%D9%86-%D8%A8%D8%A7%DA%AF%D8%AA-%D9%86%D9%85%D8%A7%D8%AF-%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87-%D8%A7%D8%B3%D8%AA-%D8%AA%D8%A7%D8%B1%DB%8C%D8%AE%DA%86%D9%87-%D9%88-%D8%A7%D9%87%D9%85%DB%8C%D8%AA"},{"title":"فهرست فرنی‌ها - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%81%D8%B1%D9%86%DB%8C%E2%80%8C%D9%87%D8%A7"},{"title":"نان باگت چطور به نماد آشپزی فرانسوی تبدیل شد؟- کتاب کاله","url":"https://kalleh.com/book/article/%D9%86%D8%A7%D9%86-%D8%A8%D8%A7%DA%AF%D8%AA/"},{"title":"نانوا هم جوش شیرین می‌زند، بیچاره فرهاد Quotes","url":"https://www.goodreads.com/work/quotes/48237541"},{"title":"www.goodreads.com","url":"https://www.goodreads.com/author_blog_posts/25433008"},{"title":"Jump to ratings and reviews","url":"https://www.goodreads.com/book/show/2249501"}]

نتایج جستجو اطلاعاتی درباره "باگت فارینه" و دهخدا را نشان می‌دهند:

باگت فارینه یکی از اصلی‌ترین انواع نان باگت است که در کنار نان باگت معمولی و باگت موله شناخته می‌شود. تفاوت اصلی این باگت‌ها در نحوه پختشان نهفته است.

برای پخت این نان باگت، روی پوسته‌اش را با آرد می‌پوشانند.

با توجه به نتایج جستجو، اطلاعات مستقیمی درباره تعریف دهخدا برای واژه "فارینه" در لغت‌نامه‌ی دهخدا یافت نشد، اگرچه نتایج نشان می‌دهند که "فارینه" واژه‌ای است مرتبط با نشاسته یا آرد در آشپزی.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:15:17.045Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW fornus/furnus\"; grep -n \"furnus\\|fornus\\|fornax\" LEW_1910.txt | head -10; echo \"== LEW filum\"; grep -n \"filum\" LEW_1910.txt | head -10; echo \"== LAT\"; grep -n \"furnus\\|fornus\\|fīlum\\|filum\" LAT.txt | head -10"
}
```


### [2026-09-06T15:15:17.128Z] TOOL RESULT

```
== LEW fornus/furnus
== LEW filum
== LAT
4330:Derives: apicatus: coiffe de 1 'apex; apiculun: filum quo flamines
11478:cf. ceruus: *keru-ik-s. Cf.fornus et fornix.
17819:dans les 1 . romanes: fr .doizil, douzil, M.L.2786; d. lineam filum, telum',
19802:g w h: v. fornus,
22414:filum, -I n. : fil. De la: fil de 1 'dpde (Ennius); fil du discours;
22418:beau brin de fenne" Pl.Mer.755; filum non malum, Lucii. 816; cf. le
22419:sens de "ligne" en franpais. Toutefois, il est possible que filum ,
22524:filum forne (?). V. ce mot.
23464:V. fornus, et forfex.
23611:"chaud", fornus, fornax; ce n'est qu'une 4 tymologie populaire.
```


## [2026-09-06T15:15:18.886Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC ghermos\"; grep -n \"ghermo\\|g'hermo\\|ĝhermo\\|ghormo\" IEC.txt | head -10; echo \"== IEC ghi- thread\"; grep -n \"ghislo\\|g'hislo\\|ĝhislo\" IEC.txt | head; echo \"== SYN warm\"; grep -n \"3\\.5[0-9]\" SYN.txt | head -3; grep -n \"WARM\" SYN.txt | head -5"
}
```


### [2026-09-06T15:15:18.977Z] TOOL RESULT

```
== IEC ghermos
4571:ghalmos “fort, keep, lock-up'. Cf. ghal- (gró- mos, ghormos) Skt. (ambig.) harmyám “castle, palace? (fr. *ghormos, i0s?); LG galm- in galm-lock *lou- vered window of belfry'; Latv. galms “castle, fortress, country seat, Court. (OCS gramü is ambig. *gróm- or *ghorm-)
4827:(ghormos, see grómos and ghalmos, for wh. the evidence is ambiguous)
== IEC ghi- thread
4686:ghislos, om, ios, is “rod, yardstick’. WP I, 633. Cf. gheslio-, &hisl- Lat. (?) hilum (perh. ^beanstick', cf. per- hilum ‘very little’, ni-hil nothing); Lombar- dic gisil “arrow, shaft; OCS Ziízlü, Zízlí «rod; Slovene Zeslo, Žezlo ‘sceptre’. (Latv. zizlis ‘stick’, if not a LW, represents a variant of type *ĝhisl-, cf. Arm. dzoy, o-st. ‘rod’, while G Geissel, OHG geisila ‘switch’ contains a diphth. of type *-oi-)
6072:&hislos, om, is (variant of ghislom, q. v.) ‘rog’. Cf. WP I, 633 Arm. dzoy, o-st., id.; Latv. zizlis, id.
== SYN warm
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
3757:several words for ‘cock’, ‘hen’ (3.51 ff.), etc., there are others derived from cries
3774:The young of an animal may be a ‘calf’ (NE calf, etc., 3.24), ‘chicken’ (Lat. pullus, 3.55), or ‘foal’ (Grk. w&dos, Lat. pullus, NE foal, etc., 3.45). Similarly, a ‘yearling’ may be a ‘calf’ (Lat. vitulus, 3.24), a ‘lamb’, ‘wether’, ‘ram’ (Goth. wiprus, etc., 3.27, 3.29), ‘sow’ (Br. gwiz, 3.34), ‘goat’ (Grk. xivapos, 3.36), or ‘kid’ (SCr. jare, 3.38).
25879:15.85 Hot, WARM 15.86 Cop
27265:15.85 HOT, WARM (Separated by; where distinction holds)
```


## [2026-09-06T15:15:24.983Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- LAT filum 22414\"; sed -n '22414,22432p' LAT.txt; echo \"--- LAT 23600-23625 fornus\"; sed -n '23598,23625p' LAT.txt"
}
```


### [2026-09-06T15:15:25.054Z] TOOL RESULT

```
--- LAT filum 22414
filum, -I n. : fil. De la: fil de 1 'dpde (Ennius); fil du discours;
ligne, trait et particuliferenent "trait dn visage", oris lineamentum
dit Non.313,16. De ce sens ddrive celni de "forne", qui a du a'enployer
d'abord dans la langue des artistes; satis scitum /iZun mulieris "un
beau brin de fenne" Pl.Mer.755; filum non malum, Lucii. 816; cf. le
sens de "ligne" en franpais. Toutefois, il est possible que filum ,
au sens de "forne", appartienne conne figura X la racine de fingo
et qu'il y ait eu k 1'origine deux nots differenta. - Ancien, usuel.
Panronan, M.L.3306.
Derives: filo, -as, substitut populaire et tardif, de n?re, cf .neuerant:
filaverant Gloss., qu'il a renplace dans les 1. ronanes, M.L.3393,
d'oi *fllandaria 339 aa; filamentum, flldtura M.L. 3393 a, fllStim-, cf.
aussi *fllacia M.1.3393; et affllo M.L. 360; exfllG (rare).
Le rapprochement avec lit.g^sZo (ienaite ginsla), v.pruss. -gislo,
v.sl.iriZo "veine, tendon" et ayec arn./iZ "tendon" est sdduisant;
le / arndnien suppose une aspiree conne lat- Peut etre lat. fUnis
a-t-il le nene eldnent radical; v. ce not.
fimbriae, -arum f.pL (le sing. n'apparait qu '4 trfes basse epoque):
franges d'un vetenent. Designe aussi les tresses d'une chevelure,
--- LAT 23600-23625 fornus
fBrmula f.: i° forae d 41 icatej 3° forae, regie, systbme; sp 4 cialeaent
dans la 1. du droit "modele juridique" (priaitivement "loi redigee
et publice in forma"), "foraule", de la fGrnula cadere "etre ais hors
de cause", formularius.
formella (tardif): petit noule; conserve dans 1 1 ital. forme l la, M.
1 . 3444 .
Coapos 4 s en -formis, correspondant souvent A des types grecs en
—jiopcpoS:
informis ( = ajiopcpoc): informe (sur lequel ont et 4 faits conformis,
dSfornis "laid, hideux", contraire de formosus; transformis, d'aprbs
con-, de-, trdns-formo); bi-, tri-, multi-fornis; tauri-fornis (Hor.
= Taupoiiopcpos).
Les anciens (cf. Don. ad Ter.Ph.107-108) rattachent forma k formus
"chaud", fornus, fornax; ce n'est qu'une 4 tymologie populaire.
Aucun rapprocheaent satisfaisant: l'o fait une difficulte parti-
culiere. Sans doute eaprunt 4 . La feraeture de l’o devant r + consonne
rappelle le passage de e k i dans les foraes dialectales st ircus,
Hirqurios, osq. amirikatud. Dn eaprunt k gr.p.opcpq est possible, par
un interaediaire 4 trusque. II s'agit d'un terae technique, concernant
une industrie florissante chez les fitrusques. M.Benveniste envisage
la possibilit 4 d'un *morma avec une dissiailation coaae dan& for¬
mica.
formica (furmlca app.Prob. GLK IV 197,37), -ae f.: fourai. Ancien.
Panroaan. M.1.3445.
D 4 riv 4 s: formicula, M.L.3448 (formiculGsus); formicinus; fornicGsus,
M.L.3447; formicG,-Bs: chatouiller, d 4 aangerj avoir des fourmis,
cf. p,upp,T}>ct.^<»); M.L.3446, d'ou formica(bi) lis; formicoleon, Isid.Or.
13,3,10, d 4 foraation de myrmScoleon; fornicaria (Gloss.) = p,uppiT)“
```


## [2026-09-06T15:15:32.428Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^fornus\\|^formus\\|^fornax\\|fornus, -\" LAT.txt | head; echo ---; sed -n '23630,23700p' LAT.txt | grep -n \"forn\" "
}
```


### [2026-09-06T15:15:32.500Z] TOOL RESULT

```
9013:fornax. Terme technique, fr 4 quent surtout dans la langue de l'£glise,
23662:fornus, -a, -un: chaud. L'adj. n'est plus conserve 4ue cbez les
23674:formus. La racine fournissait un prlsent radical athlaatique dont
23703:fornax, farnus ont et 4 expliqu 4 s ci-dessus sona fornus. Mais on
---
33:fornus, -a, -un: chaud. L'adj. n'est plus conserve 4ue cbez les
34:graaaairiens pour expli4uer forceps et fornax . 11 a Itl reaplace par
53:racine appartiennent sans doute lat. furnus, fornax (v. ces aots), avec
58:fornix (furnax), -icis f. et a.: fourneau, four. Ancien, usuel.
61:Dlrivls: fornScula : petit four; fornacalis', Fornacalia,-ium h.pl. :
62:- sacra erant cum far in fornaculis torrebant, P.F. 73 > l S>; cf.8a,3°«
63:Tardifs: fornacarius, M.L.345<>a; fornacator.
64:furnus, -I a. (fornus; fornum ni dans Varr. citi par Non.531,38,
65:fornum et fornaces dicuntur a formo. ..): four. Panroaan, M.L.3603;
70:le four k pain (furnarius, le boulanger); fornax, le four industriel
```


## [2026-09-06T15:15:34.791Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23662,23710p' LAT.txt"
}
```


### [2026-09-06T15:15:34.870Z] TOOL RESULT

```
fornus, -a, -un: chaud. L'adj. n'est plus conserve 4ue cbez les
graaaairiens pour expli4uer forceps et fornax . 11 a Itl reaplace par
calidus', cf. P.F.74,6, forcipes dicuntur quod his forma, i.e. calida,
capiuntur.
Dlrivl: formidus (adj. crll par Caton, Inc.33, d'aprfes frigidus ; cf.
P.F.73,34, ...Cato ait de quodam aedificio: "aestate frigido, hieme
formido". Cf. aussi *def ornus dans P.F.73,34, ...exta quae dantur
deforma appellantur.
La forae ancienne de 1 'adjectif avait le vocalisae e conservi dans
gr. 6ep|io£, ara./era. Le vocalisae o est celui du substantif: skr.
gharmdh "chaleur", v.pruss.gorae "chaleur", lett.^ofae; il a Itl trans-
portl dans 1 'adjectif, d'o 4 av. garamS "chaud" qui concorde avec lat.
formus. La racine fournissait un prlsent radical athlaatique dont
le .slave conserve le participe noa. plur. gorg$te "brulant"; les foraes
verbales sont dlrivles de aanibres diverses: v.sl. goritu "il brule",
goryti "bruler", lit.goriu, gareti "bruler", iri. guirid et fo-geir
"il chauffe", gr. SepOfiOU "je ae chauffe"; le prlsent en *-nu- est
secondaire dans skr .gh^Qoti "il brille" (cbez les graaaairiens) et
ara. jefnum "je ae chauffe". Le latin n'a pas conservi le thbae en
-es- attestl par skr .hdrali "ardeur" et gr.6epo£ "Itl". - A la aene
racine appartiennent sans doute lat. furnus, fornax (v. ces aots), avec
les correspondants slaves gurnii dans v.sl. gruniSar] i "xepap,euc",
r.gorn "foyer", tch. hrnec "pot" et akr.ghfi}dl} "chaleur". L 1 -ur- de
furnus peut reposer sur *g u> hornos ou *g w hrnos', cf. v.isl .gorn "feu"
et Bkr.ghjndh, v.sl .grunu.
fornix (furnax), -icis f. et a.: fourneau, four. Ancien, usuel.
Panroaan, sauf rouaain. M.L.34SI; v.h.a./urnicAe; iri. uirne ts¥ Souvent
usitl au pluriel.
Dlrivls: fornScula : petit four; fornacalis', Fornacalia,-ium h.pl. :
- sacra erant cum far in fornaculis torrebant, P.F. 73 > l S>; cf.8a,3°«
Tardifs: fornacarius, M.L.345<>a; fornacator.
furnus, -I a. (fornus; fornum ni dans Varr. citi par Non.531,38,
fornum et fornaces dicuntur a formo. ..): four. Panroaan, M.L.3603;
et celt.: irl.sorn, britt. fwrn.
Dlrivls et coaposls: furnaceus; furnarius, M.L.3601; Furnius; prae¬
furnium (Cat. Vitr. = npcm\n.yeXov).
Les deux aots ont Itl difflrencils dans 1 'usage: furnus dlsigne
le four k pain (furnarius, le boulanger); fornax, le four industriel
(f. k poterie, k mltaux, k chaux, f. de bain). Furnus correspond k
L7CVCK, fornax k xoquvoc (que du reste le latin a eapruntl au grec).fornix
443
fornax, farnus ont et 4 expliqu 4 s ci-dessus sona fornus. Mais on
peut ansai rapprocher fornix "voute, are"; cf. le grec xoquvoC A cot 4
de xoqixxpa, le four 4 tant en forne de voute, cf. Kich, a.n. Fornax aerait
A fornix coaae *cornax qne anppoae *cornacula, ital. cornacchia est
A cornix. On ne peut rien affiraer anr 1 'origine d'un aot technique
coaae fornix.
fornix, -icis {fur-) a.: are, arche, voute. Attest 4 depuis Ennius.
A l' 4 poque imperiale, fornix dans le aena d'"arc trionphal" a tendu
```


## [2026-09-06T15:15:42.517Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27265,27300p' SYN.txt | head -50"
}
```


### [2026-09-06T15:15:42.576Z] TOOL RESULT

```
15.85 HOT, WARM (Separated by; where distinction holds)
Goth. *warms (vb. Lith. karitas; Siltas peppos warmjan) Lett. karsts; silts gearbs ON heitr; varmr ChSl. toplii calidus Dan. hed; varm SCr.  vrué; topao caldo Sw. het; varm Boh. _horky; teply chaud “di OE hat; wearm Pol. —_ goracy; cieply caliente, cdlido ME hoot; warm Russ. zarkij, gorjatij; teplyj
_ cald NE hot; warm Skt. ugna-, tapta- 1 Du. heet; warm Av. garama-, tapta- . OHG heiz; warm poelh, twyim, a MHG heiz; warm i ieee NHG _heiss; warm 0
(cf. 15.37), but Boh. horky, Slov. gorak ‘hot’, with vb. Slav. goréti ‘burn’, pres. act. pple. often merely ‘hot’ in modern Slavic, Pol. goracy, Russ. gorjacij (cf. Berneker 333 f.); also Russ. Zarkij (: Zar ‘heat’, Zarit’ ‘roast, scorch’, ChSI. Zeravi. ‘glowing’, po-zaru% ‘burning’).
2. IE *tep-. Walde-P. 1.718f. Er- nout-M. 1030f. Pedersen 1.87, 92f., 2.19. Stokes 124 f.
Ir. t@, pl. téit (pple. *tepent-), NIr. te; W. twym, Br. tomm, OCorn. toim (*tepes- mo-); ChSl. toplit, SCr. topao, Boh. teply, Pol. ciepty, Russ. teplyj; Skt., Av. tapta- (pple. of tap- ‘be hot, warm’); Lat. tepi- dus ‘lukewarm, tepid’, tepére ‘be tepid’, etc. Here also W. cynnes fr. *cyn-tes, epd. of tes, Ir. tess ‘heat’ (*teps-tu). Morris Jones 63.
3. IE *el-, prob. the same ultimately as in words for ‘cold’, Lith. Saltas, etc. Walde-P. 1.429. Ernout-M. 134. Walde- H. 1137.
Lat. calidus (> borrowed Sp. cdlido), caldus (>It. caldo, Fr. chaud, Rum. cald), with vb. calére ‘be warm’ (> OSp. caler, deriv. caliente ‘hot’); Lith. Siltas, Lett. silis, with vb. Lith. Silti, Lett. silt ‘grow warm’; fr. an extended form of the root prob. ON Aly ‘warmth’, hler ‘warm, mild’ (of weather), OE hleowe ‘comfort- able, sheltered’, OHG lao, NHG lau ‘tepid’, etc,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1078 SELECTED INDO-EUROPEAN SYNONYMS
4, NG feorés, in class. Grk. ‘boiled, boiling hot’, fr. ¢éw ‘boil’ (10.31).
5. Ir. té, W. twym, Br. tomm, W. cyn- nes, above, 2.
W. brwd: berwi, Ir. berbaim, etc. ‘boil’. Walde-P. 2.168.
W. poeth = Br. poaz ‘cooked, burn- ing’, Lat. coctus ‘cooked’, pples. of W. pobi, Lat. coquere ‘cook’, etc. Walde-P. 217.
6. ON heitr, OF hat, OHG heiz, etc., general Gmc., fr. *kai-d-, beside *kaz-t- in Lith. katsti, Lett. kaist ‘become hot’,
15.86 Grk. oxpds Goth. kalds NG Kptos ON kaldr Lat.  frigidus, gelidus Dan. _ kold It. freddo Sw. kall Fr. froid OE ceald Sp. Jrio ME cold Rum. rece, friguros NE cold Ir. tar Du. koud Nir. = fuar OHG alt W. oer MHG kalt Br. yen NHG kalt
A distinction similar to that of ‘hot’ and ‘warm’ is partially observed, but here ignored in the list. That is, be- side the generic words for ‘cold’, there are others for ‘moderately cold’, ‘cool’, usually with the feeling of pleasant con- trast to excessive heat. These may be cognate with those for ‘cold’, as NE cool, NHG kihl, etc., or they may be words which mean literally ‘fresh’, as It. fresco, Fr. frais, etc., similarly NG Spocepés in class. Grk. ‘dewy, fresh’ : dpdcos, NG dpoora ‘dew’. Again, NE chilly, also cognate with cold, is ‘moderately but dis- agreeably cold’, and NG Wuxpés (in class. Grk. ‘cold’) is now used in just this sense, or else figuratively.
Apart from inherited groups, there are other words connected with those for ‘ice, frost’, ‘stiffness’ (?), ‘blow’.
1. IE *fel-, prob. the same root as in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
etc., and *kai- in OHG hei, gehei Walde-P. 1.326 f. Falk-Torp 388
7. Lith. kargtas, Lett. karsts, besid Lett. karst ‘become hot’, fr. the root si Lith. kurtt, Lett. kurt ‘heat’, Ch}, kurit; se ‘smoke’, Goth. hauri ‘coals’, ON ; ‘fire’. Walde-P. 1.418.
8. SCr. vrué, and vreo : vreti, Choy viréti ‘boil’, Lith. virti ‘bubble up, boil’ etc, Walde-P. 1.269. Miklosich 381, ”
9. Skt. usna-, fr. ws- ‘burn’ : Grk. ebeo ‘singe’, Lat. drere ‘burn’. Walde-P. ible
‘heat,
.
hyrr
COLD
Lith.  Saltas
Lett. auksts, salts
ChSl.  studenii
SCr. _hladan, studen Boh.  studeny
Pol. zimny
Russ. cholodnyj (studenyj) Skt. ¢ila-, cigira-, hima- Av. aota-, sarata-
words for ‘hot’, Lat. calidus, etc. See 15.85.
```


## [2026-09-06T15:15:50.345Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; echo ---; grep -n \"filum\" WLD_Bd1_pages.txt | head -10; echo \"=== Bogensehne\"; grep -n \"Bogensehne\" WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-06T15:15:50.443Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
---
49898:  lat.       filum,        s.       Yf. LEWb. 2 s. v.
=== Bogensehne
28927:Wiirgen), Bogensehne, Muskel" (Liden Arm. St. 100 f.).
65742:gSiia, g?i„os „Sehne, bes. Bogensehne“.
65745:                                                           av. jga „Bogensehne (in Zs. auch Sehne
65746:des Fleisches)“, gr. (ho; ,,Bogensehne“                     ;
68079:„Sehne“, temptyva „Bogensehne“                aksl. I diva „Sekne“, lit. pampas „An-     =
```


## [2026-09-06T15:15:53.290Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '65735,65775p' WLD_Bd1_pages.txt; echo \"=== page tag\"; awk 'NR<=65742 && /\\[pdf page/{p=$0} END{print p}' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:15:54.913Z] TOOL RESULT

```
                                               :
                                                                ,;


eine solche Wz. nirgends vorliegt (aucli in                          lat.   segnis nicht).


gSiia, g?i„os „Sehne, bes. Bogensehne“.
                                                   £
      Ai. jyd „Sehne, bes. des Bogens                  ,
                                                           av. jga „Bogensehne (in Zs. auch Sehne
des Fleisches)“, gr. (ho; ,,Bogensehne“                     ;
                                                                vielleicht lit. gija „Faden“, lett. dzija
                    Sehne“ (wenn mit anl. p«, vgl. Fick II 4 117, Bezzenberger
,,Garn‘-, aksl. zi-ca      ,



BB. 16, 253, Yf. LEWb. 2 292; oder mit anl. gth-, wie nach Osthoff IF. 4                                       ,
                             T
288 jedenfalls eymr. giaa „lS erven, Sehnen“, vielleicht auch lat. filuni usw.
so Fick BB. 2, 188, Wb. I 4 38. 413). Trautmann Bsl. Wb. 87, Hiihlenbach-
Endzelin I 549 m. Lit.   S. auch oben S. 670!


g"is-ti-s „Finger“??.
                                                                                                              <£
      Cymr.    hys. acorn, bis, bes, bret. biz „Finger“, mir. biss ega „Eiszapfen                                  ,


anord. Jcvistr ,,kleinerer Zweig“ (nur einer jungen dichterischen Metapher
entspringt die Bed. von il-kvisiir „foot-twigs                         = the toes“). B. bei Fick II            4

175,       Brugmann IF.        1   1, 285, Pedersen KG.
                                                79                     I       (vgl.   zur Bed. arm. end
„Zweig, Finger", anord. limr „GIied‘‘ lim f. „Zweig“). Sehr zweifelhaft;
                                                                ;


denn mnd. twist „Zweig“ miiBte dabei ein von hvistr verschiedenes Wort
sein, was ebenso bedenklich ist, wie anord. hvisl f. „gespaltener Zweig oder
=== page tag
```


## [2026-09-06T15:16:04.609Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"Ader, Sehne\\|„Sehne“\\.\" WLD_Bd1_pages.txt | head -20; echo \"=== gheia\"; grep -n \"g^h?ei\\|ghgi\\|g\\\"hei\\|g?hei\" WLD_Bd1_pages.txt | head -10; echo \"=== jil\"; grep -n \"gysla\\|gysla\\|dzisla\" WLD_Bd1_pages.txt | head -5"
}
```


### [2026-09-06T15:16:04.691Z] TOOL RESULT

```
63486:g’.'liei-         .,Ader, Sehne,                    Band            -
=== gheia
=== jil
49897:    Ahd. gaisala nicht nach Pedersne IF. 5, 68 zu aksl. zila, lit. gysla „Ader'‘,
```


## [2026-09-06T15:16:06.715Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '63480,63520p' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:16:06.766Z] TOOL RESULT

```
(Ycreinigung mit                          *gieti- ..kauen".                         *gcns- ..kosten ";-
                                                                                                                1




g’.'liei-         .,Ader, Sehne,                    Band            -
                                                                        .




    Cymr. giau ..Xerven, Sehnen“ (s. Osthoff IF. 4. 2&8;.
   Zweideutig sind lit. gijd ,.Faden im Aufzug eines Gewebes", lett. d.zija
                                                                                                                                                                :
„Faden, pi. Garm", aksl. licit ..Sehne“, russ. dial. I tea ,,Kammgarn‘ bulg.                                                                                        ,


licit, skr. lien .(Faden, Draht. Sehnur, Saite“ (s. u. glial S. 694 und Traut-

mann Bsl. Wb. S7).
   g “ It i »lo-:
   Arm. jil              ..Sehne. Sehnur                        "           (Ilubschmann Arm. Gr. I 486. Pedersen KZ.
39, 413;,           lat. I'd        mu ,.Faden“; lit. gyslo ,,Adcr, Sehne. Blattnerv", lett. dzishi,
d'.ihsla ,.Adci  (die Xasalierung in zemait. ginsia. auf die Mikkola BB. 22,
                            •




245 seine Grundform *ti'ihinslo- stiitzt, ist nach Trautmann Bsl. Wb. 90
sekundar, vgl. auch Leskien Nomina 455), pr. *pctteyisJo ,,Ruckenader“;
aber aksl. ,j!a, russ. Ultt, si. Ida, bulg. Ida, skr. Uln, tech, Ilia, poln. zyfa
,,Ader. Sehne"   iU. *;/</«?  Gegen *gisla Bruckner KZ. 46, 209a..
     Yanicek 97, Fick BB. 2. 188 wo aber mit nicht zugehorigem vereinigt),
   4
 I   413, Muhlenbaeh-Endzelin I 557f.
     Fernzuhalten alb. del „ Sehne, Flechse, Ader s. Pedersen KZ. 36, 326,                                  *
```


## [2026-09-06T15:16:14.044Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"„warm“\\|garəma\\|garema\\|fornus\" WLD_Bd1_pages.txt | head -20"
}
```


### [2026-09-06T15:16:14.094Z] TOOL RESULT

```
30885:szdltas          „warm“ u. dgl. eingetreten sein. — DaB die Wz. mit (s)qai(-t-, -cl-)
40906:1.        kel-   1.   „frieren, kalt“, 2. „warm“.
46409:besser zu kel „warm“); got. Mija ,,Zelt, Hiitte" (fiir Anderung in *Miwa                                                                                ,
65102:    Lat. formas     warm" (Festus), fornus furnus, forndx „Ofen‘ (letzteres
65144:    Ahd. warm anord. varmr „warm“, got. warmjan „wii,rmen" (ahd. ivirma
67776:lat. tepeo, -ere „lauwarm sein“, tepidus „warm“, tepor „Warme“; vermutlich
67803:topiti ) aksl. toph „warm“; Kaus. skr. tbpiti „schmelzen“, russ. topitb „heizen;
```


## [2026-09-06T15:16:15.449Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"fornus\\|Bepuoc\\|thermos\" IEC.txt | head -10; echo \"=== IEC gwhermos\"; grep -n \"hermos\\b\\|hormos\" IEC.txt | head -10"
}
```


### [2026-09-06T15:16:15.515Z] TOOL RESULT

```
5564:guhrnos (1) 'ashpit, firepit, clay oven, earthen pot, crucible’. WP I, 687. Cf. guher-, etc. Skt. cf. ghrnáh ‘heat’; Lat. fornus, furnus ‘oven’ beside hirnea ‘earthen pot’; MIr. gorn ‘fire’. Mod: id. and ‘torch’; guirn ‘firebrand’; W gwrn “urn, cone-shaped vessel’; OCS grünü ‘cauldron’; cf. grünylí ‘foundry’; R gorn “fur- nace, forge, hearth’; Pol. cf. garn-ek, dim. ‘pot’; Cz. hrn-ec, -ek, id.; Srb. grnac. id. Cf. ON orna v. ‘warm’. (For the semantics cf. Skt. kundam ‘firepit’ and ‘pot’, and that Aus- tralian aborigines still build earth-ovens. Cf. the structure of the Sardinian nuraghi, of co- nical shape, primitive blast-furnaces?)
8806:hither”, etc. Lat. citra, prp. “this side of; citimus, adj. "hithermost'; W cf. (?) cyd, cj. though"; ?cyda, mutated to gyda ‘with’; Go. hidre, OE hider, adv. “hither? (Go. *hiduma, OE *hidema not recorded)
=== IEC gwhermos
1527:bhorm- (bhormos, à, is, io) “burden; bearer, holder, container’. Cf. bhero Gk. phormós "basket, corn-measure'; Alb. barrë “load; Go. barms (i-st.); OHG OS barm ‘Jap’; OE bearm ‘lap; possession’; G (uml.) Berme (‘ramp of bulwark’. LW in Fr. berme, OFr. barme); ON cf. barmtog “haul-rope. (Isophonic forms, of uncertain kinship, are the following: Gk. phormís ‘faggot; Alb. barmë “inner bark’; Ger. Barm, Barmen ‘crowd, pack’; Barmen, Bärme ‘barm, yeast’; ON barmr ‘brim’; barmi ‘brother’; Ukr. brama sic ‘gate’). WP II, 164
2808:dher- (2) “hard, fast, firm'. Cf. dhermos, dhern-, dhor- & dháros Skt. cf. dharayami “hold, bear, wear, prevail, agree’; Hind. dharna ‘grasp; pledge’; Av. dar- ‘hold, get’; Ober dar-, id.; Per. (ambig.) dā- ram ‘have’; Arm. (o- or zero-gde) darem ‘stay’; Gk. cf. thérsos, Aeolic: ‘courage’; Lat. cf. fer-tim ‘thickly, closely’; W der ‘stubborn’; deru, derio ‘jib, be stubborn’; Li. derüs ‘thriving’; deriù, éti ‘bargain’; derù, éti ‘serve; suit’; Latv. depu, et ‘befit; pledge; suffice’.
2817:dhermos, à, io (dhermn-, dherom-) “firm, fixed; fixture, pact, order'. See dher- (2) and cf. WP I, 856 Skt. dhármah, dhárman; Tokh. (?) sarm ‘reason’; Arm. cf. darum (fend, term’, fr. *dherom-); Lat. firmus; LLat. firma “fixed payment; farm’; Umb. cf. ferime ‘firmly’; Ir. darmna (‘price-fixing or sim.); MHG térme,
2823:5 dhern- “holding, firm; hold, hardwood'. Cf. dher- (2), dhor-, dhermos Cz. dřeň ‘pith, core; dřín *'cornel-cherry'": OHG tirn-paum, -pauma (“cornel', cognate accdg. to J. Schmidt, LW accdg. to O. Schade);
3196:dhrtos, is. “held; hold, holding; fast. Cf. dheró, dhermos, dhr-. I, 857 Skt. dhrt, adj.; dhrtib, £.; Av. doroto, adj. E s.; Per. (ambig.) dül ‘bucket’; (LW in Arm. dujl, id.); Arm. cf. han-dart (;calm': Skt. sám- dhrtah ‘held together"); W dryd, adj. ‘thrifty’; s. ‘thrift. (Lat. fortis ‘patient, constant, stout, strong' is ambig. cf. turtos)
4571:ghalmos “fort, keep, lock-up'. Cf. ghal- (gró- mos, ghormos) Skt. (ambig.) harmyám “castle, palace? (fr. *ghormos, i0s?); LG galm- in galm-lock *lou- vered window of belfry'; Latv. galms “castle, fortress, country seat, Court. (OCS gramü is ambig. *gróm- or *ghorm-)
4827:(ghormos, see grómos and ghalmos, for wh. the evidence is ambiguous)
5478:guheguh- — guhermos (guhermn, guhermio)
5490:guhermos (guhermn, guhermio) *warm, hot; heat. Variant: guhorm-. Cf. guheros, guhor-. WP I, 687. (Indo-Iranian forms fr. *guhorm-) Skt. gharmáh, m.; Av. garomo, adj.; garomus, m.; OPer. garma-; Per. garm, adj.; Oss. qarm, adj.; Tokh. A $árme, adj.; Arm. germ, o-st. adj.; Éermn gs german ‘fever’; Gk. thermós, adj.; thérme, f. s. beside thérma, n.; Alb. zjarr, zjerm, m. ‘fire’; cf. Dac. (?) Germi-sara (a wa- tering-place); OLat. cf. formus, adj. (Fest.); Formiae (a town nr. Naples); Lig. Bormium, Aquae Bormiae (places in Switzerland); Go. cf. warmjan, v. beside *warms (^warm', and com. Gmc.); Li. (Zemaité?) germe (“virgin
5493:guheros “hot; heat’. WP I, 687. Cf. guhermos. (O-gde in Iran.) Skt. háras, n. (anger; Av. (o-gde) gar-, v. ‘burn’; Arm. ğer, o-st. ‘hot; Gk. théros, n. "summer, harvest’; Olr. cf. fo-gerim, v. ‘heat’; OCS cf. Zeravü *^white-hot'; Srb. Zerava "em. bere": long-gde in OCS Zarü Cheat and com. Sl.)
```


## [2026-09-06T15:16:25.486Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"guhislo\\|guhiia\\|guhi-\\|guhijos\" IEC.txt | head -10; echo \"=== SYN thread\"; grep -n \"9.17 THREAD\\|THREAD\" SYN.txt | head -5"
}
```


### [2026-09-06T15:16:25.598Z] TOOL RESULT

```
=== SYN thread
10304:6.38 THREAD
```


## [2026-09-06T15:16:28.787Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10304,10330p' SYN.txt; echo \"=== IEC search filum\"; grep -n \"'thread'\\|filum\" IEC.txt | grep -i \"filum\" | head -10"
}
```


### [2026-09-06T15:16:28.893Z] TOOL RESULT

```
6.38 THREAD
Grk. vijwa, KAworgp Goth.
NG vijua, yréua, KAwor} ON praor Lat. filum Dan. itraad It. filo Sw. irdd Fr. fil OE prad Sp. hilo ME _ threde Rum. fir NE thread Tr. snathe Du. draad Nir. — snath OHG fadam W. edau MHG vadem Br. neud NHG faden
1. Derivs. of IE *(s)né-, *(s)né- in words for ‘spin’ (6.31). Walde-P. 2.694 f.
Grk. vijua, NG pop. yviua; Ir. snathe, NIr. snath, Br. neud; ChSI. nitt, nista, etc., general Slavic.
2. Grk. wwortp, NG rrworh : row ‘spin’ (6.31).
3. Lat. filum (> Romance words) : Lith. gysla, Lett. dzisla, OPruss. -gislo, ChSl. Zila ‘vein’, etc. Walde-P. 1.670. Ernout-M. 360. Walde-H. 1.497.
4. W. edau, MW adaued (pl.), OW elem (gl. instita), OHG fadam, MHG vadem, NHG faden, orig. ‘a measure of thread from tip to tip of the outstretched arms’ : Ir. aitheamh, OE fepm ‘fathom’, orig. ‘embrace’, ON fadmr ‘embrace’ (IE *pet- in Grk. rerévviue ‘spread out’, Lat. patére ‘stand open’, etc.). The
Lith.  sitilas
Lett. pavediens ChSl.  nitt, nidta SCr. nit
Boh. nit’
Pol. nid.
Russ. nit’, nitka Skt. stilra-
parallel semantic development in Welsh and German is remarkable. Walde-P, 2.18. Pedersen 1.132. Falk-Torp 208 f.
5. ON pradr, Dan. traad, Sw. trad, OE pred, ME threde, NE thread, Du, draad (NHG draht ‘wire’), fr. a Gmo, *prédu- : OE prawan, OHG drajan, ete, ‘turn around, twist’ (10.13). Walde-P. 1.729. NED s.v. thread.
6. Lith. siilas, and with different suffix Skt. sdéra-, fr. Lith, siti, Skt. Stv- ‘sew’ (6.35).
Lett. pavediens, prob. formed with agent-noun suffix -iens (cf. Endz., Gr. 235 f.) fr. pavedu, pavest ‘lead a distance’ (cpd. of vest, Lith. vesiz ‘lead’), with de- velopment of sense ‘thread’ through a Measure (as in NHG faden, etc., above, 4), or through the notion of guidance (in stories like the myth of Ariadne)?
7. OhSl. nzti, etc., above, 1.
6.39 DYE (vb.)
Grk. Béxrw Goth. .... NG Badw ON lita Lat. _tingere, inficere Dan. farve It. lingere Sw. farga Fr. leindre OE
Sp. lefiir ME dye Rum. boi, vépsi NE dye Ir. (dathaigim) Du. __verven Nir. dathuighim OHG farawen W. liwio MHG verwen Br. liva NHG farben
Lith. dazyti, parvuoli Lett. krdsuot (pervet) ChSif se �� SCr. bojadisati (farbatt)
déagian, telgan Boh.  barvili
Pol. farbowad (barwié) Russ. krasit’ Skt. ranjaya-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Sy ee
cLorHl listed mean simply a used alike for ‘dye i a board, house, ete.). m the notion of ‘dip’,
=== IEC search filum
5498:guhislà ‘sinew, gut, vein". WP I, 670 Vedic (*-1-) hirá ‘vein’; Oss. (?) gil, dZil “penis”; Arm. Bil, a-st. beside ğiy “nerve, sinew’; Thrac. zílai (?) ‘vines’; Lat. filum ‘yarn’ beside hila, hilla (dial: eur: OCS Zila (vein? & com. SL); Li. gysla, id.; Latv. dzīsla ‘sinew, ven"
```


## [2026-09-06T15:16:37.475Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN furnace\"; grep -on \"furnace, n\\..\\{0,320\\}\" KLN_1966.txt | head -3; echo \"== KLN forceps\"; grep -on \"forceps, n\\..\\{0,300\\}\" KLN_1966.txt | head -3; echo \"== KLN file thread\"; grep -on \"file, n\\..\\{0,300\\}\" KLN_1966.txt | head -4; echo \"== KLN profile\"; grep -on \"profile, n\\..\\{0,300\\}\" KLN_1966.txt | head -3; echo \"== KLN thermometer\"; grep -on \"thermometer, n\\..\\{0,250\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T15:16:39.168Z] TOOL RESULT

```
== KLN furnace
== KLN forceps
== KLN file thread
== KLN profile
== KLN thermometer
```


## [2026-09-06T15:16:42.024Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c . KLN_1966.txt KLN_1971.txt; echo \"---\"; grep -on \"furnace.\\{0,300\\}\" KLN_1971.txt | head -3; echo \"===\"; grep -on \"profile.\\{0,260\\}\" KLN_1971.txt | head -3"
}
```


### [2026-09-06T15:16:43.990Z] TOOL RESULT

```
KLN_1966.txt:41263
KLN_1971.txt:221180
---
21955:furnace of the al- 
25450:furnace, 
37951:furnace’, and cogn. with 
===
82380:profile. 
92803:profile, purfle. Cp. also 
192209:profile, n., side view. — It. profile , proffilo, 'draw-
```


## [2026-09-06T15:16:46.971Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '192209,192222p' KLN_1971.txt; echo \"=== furnace\"; sed -n '37945,37965p' KLN_1971.txt; echo \"=== forceps\"; grep -n \"forceps, n\" KLN_1971.txt | head -3"
}
```


### [2026-09-06T15:16:47.096Z] TOOL RESULT

```
profile, n., side view. — It. profile , proffilo, 'draw- 
ing in outline’, fr. pr o filar e, projfilare , ‘to draw 
in outline, to outline’, fr. pro - (fr. L. pro, ‘be- 
fore, for'), and filo, ‘thread, line’ (fr. L. filum). 
See 1st pro- and file, ‘collection of papers’, and 
cp. purfle. 

Derivative: profil-ist , n. 

profile, tr. v. — It. profilare , fr. profilo. See pro- 
file, n. 

profit, n. — ME., fr. OF. (= F.) profit, fr. L. pro- 
feet us, ‘advance, progress, effect’, fr. profectus, 
=== furnace
camahutus, ult. fr. Pers. chumahan , ‘agate’, 
through the medium of the Arabic. Cp. camaieu. 
Derivative: cameo, tr. v. 

camera, n., a chamber. — L., ‘vault, arched roof, 
arch', fr. Gk. xa^zapa, which is rel. to xajztvoc 
(whence L. camlnus), ‘furnace’, and cogn. with 
L. camur, camur us, ‘curved’, fr. I.-E. base *qam -, 
*qem-, ‘to bend, vault’. Cp. It., OProven?., 
Catal. camera , Sp. camara, Port, camara , F.cham- 
bre,OHG. chamara , OS. camara, OSlav. komora, 
Llth. kamara, OIr. camra , which all derive fr. 
L. camera. Cp. chamber. Cp. also camara, Cam- 
barus, camber, chimney, comrade, concamerated. 
For derivatives of a -^-enlargement of base *qam- 
see change. Cp. cant, ‘slope’. Cp. also heaven, 
camerlengo, camerlingo, n., the papal chamber- 
lain. — It., a hybrid coined fr. camera (see ca- 
mera) and the Teut. suff. -ling. Cp. chamberlain. 
Camerontan, n., a follower of Richard Cameron 
(died in 1 680). For the ending see suff. -ian. 
=== forceps
95706:forceps, n., a pair of pincers used in surgery. —
```


## [2026-09-06T15:16:50.486Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '95706,95725p' KLN_1971.txt; echo \"=== furnace n\"; grep -n \"furnace, n\" KLN_1971.txt | head -3"
}
```


### [2026-09-06T15:16:50.569Z] TOOL RESULT

```
forceps, n., a pair of pincers used in surgery. — 
L., ‘pair of tongs, pincers’, contracted fr. 
* for mi-caps, fr. formus, ‘hot’, and caper e, ‘to 
catch, seize, take, hold’. See warm and captive 
and cp. forfex. For the change of Latin d (in 
cdpere) to e (in for-cips) see accent and cp. 
words there referred to. 

forcible, adj. — OF., ir. force. See force, ‘strength’, 
and -ible. 

Derivative: forcibl-y , adv. 
forcipate, adj., resembling a forceps. — Formed 
with adj. suff. -ate fr. L. forceps , gen. for tip is, 
‘a pair of tongs’. See forceps, 
forcipated, adj., forcipate. — Formed fr. prec. 
word with suff. -ed. 

Forcipulata, n. pi., an order of starfishes (ich- 
thyol.) — ModL., lit. ‘resembling a small for- 
=== furnace n
98700:furnace, n. — ME. for ne is, for nais, fr. OE . for nais
```


## [2026-09-06T15:16:53.657Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '98700,98715p' KLN_1971.txt; echo \"=== file\"; grep -n \"^file, n., a collection\\|file, n., a line\\|file, n., a steel\" KLN_1971.txt | head; echo \"=== thermo\"; grep -n \"thermometer, n\" KLN_1971.txt | head -2"
}
```


### [2026-09-06T15:16:53.758Z] TOOL RESULT

```
furnace, n. — ME. for ne is, for nais, fr. OE . for nais 
(a collateral form of fornaise , whence F. four- 
naise), fr. L. forndeem, acc. of forndx, ‘furnace, 
oven’, fr. fornus (also furnus ), ‘oven’, which is 
rel. to L. formus and cogn. with Gk. Sep(ju$<;, 
OE. wearm, ‘warm’. See warm and cp. Fornax, 
fornicate, Fumarius, homito. Cp. also therm. 
Derivatives: furnace, tr. v., furnac-er, n. 
furnacite, n., a lead copper chrom-arsenate (mr/i- 
eral.) — Formed with subst. suff. -ite Ir.furnax , 
erroneous form for L. forndx , ‘furnace’ (see 
furnace); so called after the colonial governor 
Lucien Fourneau (fr. fourneau, ‘furnace’). 
Furnariidae, n. pi., a family of South American 
birds, the ovenbirds (ornithol.) — ModL., 
formed with suff. -Idae fr. Furnarius (q.v.) 
=== file
=== thermo
242853:telethermometer, n., a thermometer that records 
246242:thermometer, n. — F. thermometre , coined by the
```


## [2026-09-06T15:16:59.599Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '246242,246252p' KLN_1971.txt; echo \"=== filament\"; grep -n \"filament, n\" KLN_1971.txt | head -2; echo \"=== fillet/file\"; grep -n \"file, n\" KLN_1971.txt | head -5"
}
```


### [2026-09-06T15:16:59.700Z] TOOL RESULT

```
thermometer, n. — F. thermometre , coined by the 
Jesuit Father LeurSchon in 1624 fr. Gk. ff^ppiY], 
‘heat’, and p^rpov, ‘measure’. See therm and 
meter, ‘poetical rhythm’, 
thermometry, n., the measurement of heat. — 
Compounded of tbermo- and Gk. -pLErpia, ‘a 
measuring of’. See -metry. 

Derivatives; thermometr-ic , thermometr-ic-al , 
adjs., thermometr-ic-al-ly , adv. 
thermophile, thermophilic, adj., ‘heat loving’ (said 
=== filament
92762:filament, n., a fine thread, fiber. — F., fr. ModL. 
=== fillet/file
66295:defile, n., a narrow passage. — F. defile, ‘a nar- 
92791:file, n., 1) a collection of papers; 2) a line, row. 
92813:file, n., a tool of steel. — ME. file, fr. OE. feol, 
192209:profile, n., side view. — It. profile , proffilo, 'draw- 
192219:file, n.
```


## [2026-09-06T15:17:01.924Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '92762,92812p' KLN_1971.txt"
}
```


### [2026-09-06T15:17:02.045Z] TOOL RESULT

```
filament, n., a fine thread, fiber. — F., fr. ModL. 
fildmentum , fr. Late E. filare, ‘to spin’. See file, 
‘collection of papers’, and -ment. 

Derivatives : filament-ary, filament-ed, filament- 
ous, adjs. 

Filar ia, n., a genus of nematode worms ( zool .) — 
ModL., lit. ‘threadlike’, ix. filum , ‘thread’. See 
file, ‘collection of papers’, 
filariasis, n., a disease caused by Filaria ( med .) — 
A Medical Latin hybrid coined fr. Filaria (fr. 
L. /Hum) and -iasis, a suff. of Greek origin, 
filature, n., the reeling of silk from cocoons. — 
F., fr. Late L. flatus, pp. of flare, ‘to spin’, fr. 
filum, ‘thread’. See file, ‘collection of papers’, 
and -ure. 

filbert, n., the hazelnut. — Fr. dial. F. noix de 
filbert , lit. ‘nut of Philibert’ ; so called because 
the day of St. Philibert (Aug. 22) fell in the 
nutting season. The name Philibert derives fr. 
OHG. Filuberht and lit. means ‘very bright’. 
See bright and cp. the second element in Albert 
and in names there referred to. 
filch, tr. v., to steal. — Of unknown origin. 
Derivatives: filch-er , n., filch-ery, n., filch-ing, 
adj., filch-ing-ly, adv. 

file, n., 1) a collection of papers; 2) a line, row. 

— In some senses fr, F. file, ‘row’, fr. filer, ‘to 
spin’, fr. Late L. filare, ‘to spin’ (whence also 
It. filare, OProven q. filar, Sp. hilar , ‘to spin’), fr. 
L. filum , ‘thread’, in some fr. F. fil, ‘thread’ (fr. 
L. filum). L. filum stands for I.-E. base *g v his- 
lom and is cogn. with Arm. fil, ‘sinew, string, 
line’, Lith. gysla, ‘vein, sinew’, Lett, dzisla, 
‘vein’, OPruss. pette-gislo, ‘vein of the back*, 
OSlav. zila, ‘vein’. L. funis, ‘rope, line, cord’, 
is not cognate. Cp. Filago, filament, Filaria, 
filigree, ficelle, enfilade, profile, purfle. Cp. also 
hilum, nihil. 

Derivative: file, tr. v., to arrange in a file, 
file, tr. v., to march in file; tr. v., to cause to 
march in file. — F. filer, fr. Late L. filare , ‘to 
march in file’, fr. L. filum, ‘thread’. See file, ‘a 
collection of papers’, and cp. defile, ‘to march 
in file’.
```


## [2026-09-06T15:17:08.348Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HUB garm\"; grep -n \"garm\" HUB.txt | head -8; echo \"== HUB zih\"; grep -n \"zih\\b\" HUB.txt | head -8; echo \"== NYB garm\"; grep -n \"garm\" NYB_vol2_glossary.txt | head -6; echo \"== NYB zih\"; grep -n \"\\bzih\\b\" NYB_vol2_glossary.txt | head -4"
}
```


### [2026-09-06T15:17:08.443Z] TOOL RESULT

```
== HUB garm
750:wie garma etc. (Darmesteter, Etud. iran. I, 267).
2621:731. Np. sarma ^est forme par analogie siir garma'* Dar-
3287:afgh. gir^an the collar or cape of a garment, 2) the
5264:'Nacken', garm Varm', gustardan *ausbreiten', mar *Zahr,
8617:b) garma 'Hitze' ^^ phi. ganmk Gl. and Ind. 262
8618:neben garm 'heiss' = phi. r/arw, ap. garma- in garmapada-;
8808:garm 'warm' — zd. garenia-; gire 'Hals' -- zd. grwd-
9232:'Arzenei' H. 554, garm 'warm' H. 911, kirm
== HUB zih
8169:zan *Weib* = gd. j^ni- 'Weib'; zih *Bogeusehne' =^ zd. skr.
== NYB garm
141:LBWSY?: Z BUŠA (more probable than pl. L'BUSAYY A) garment
563:apa-zón [’pzwn'] increase, addition 11217; tan pat-~ kunéh increase thy physical well being 21%, cf s. v. ?pat (11); increase of spiritual blessings 50%. — MPrs ’bzwn (A-H IT); Paz. awazün; NP afzün ‘more, greater’; < *abi-Zavana-, in which api- was substituted for abi-, v.s. v. apa-; from apa-zūtan, q.v. Wikander, Orbis XXXI, 1972, 183—184, prefers the read- ing Ppzn'] = äp-zan ‘a bath(ing vessel)’, NP abzan referring to the corresponding passage of Sn: bi- garmäbah šau ‘go to the warm bath!’
1019:brahmak [blhmk'] (splendid) garment, of the princely footwear 295. — MPrthPrs brhm ‘garment, elegant form, grace’ eto., v. Henning, TPhS 1944, 108-118 (I cannot accept his combining this w. with OP brazman.) Paz. brahm, Skr. v. vesa, šriigara (SGV).
1636:garm [glm], garmök [glmwk'] hot, warm 1420, 41?9, 10122. — Av. (515) garoma-, (516) garomu- ‘heat; MPrs grm’g ‘heat’ (A-H I); NP garm. l
1637:garméh heat 923,
2710:darraky — to put one’s feet on the rock HajB:6-7.12-13; tigr andar kamān ~ to put the arrow to the bow (-string) 100%; catrang ~ to arrange a game of chess 11914.20.21. gartänäk be ~ to cast the dice 1202122; pat ... ~ to deposit in... 10719, 11312; apar ~ to put (wood) on (the fire) 95°; dast apar ~ to put one's hand (to work) 6215; bé ~ to deposit 4216, to take off (a garment) 5717; — nam m to give a name, to name 1025-36, 11421, 11623; pat nām i ... ~ to name after 1201-2; mēnišn ~ 6 to ponder on 5?2-?3, — Av. (721 sq.) ni-dä-; MPrs nh’dn, nyh?dg, Verbum 194; Ps. nyd?t; Paz. nahādan; NP nihādan; only SW.
== NYB zih
```


## [2026-09-06T15:17:17.014Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8165,8175p' HUB.txt; echo \"--- pages:\"; python3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nfor pat in [\\\"zih *Bogeusehne'\\\",\\\"garm 'warm' — zd. garenia-\\\",\\\"b) garma 'Hitze'\\\"]:\n    i=t.find(pat)\n    print(pat, '-> leaf', t[:i].count('\\f'), 'printed', t[:i].count('\\f')-10)\n\""
}
```


### [2026-09-06T15:17:18.705Z] TOOL RESULT

```
javidan *kauen\ afgh. zOvql, ksl. zwati (Wrzl. iran. jyu^
oben p. 49 — 50 und § il); jtva *Quecksilber = ziva^ siehe
unter c).
b) ^=np. z: zadan 'schlagen' = zd. ap. jan, skr. han\
zan *Weib* = gd. j^ni- 'Weib'; zih *Bogeusehne' =^ zd. skr.
jycL-; zistan 'leben', zd. skr. jiv\ zahr (oben p. 71), arm.
zahr 'Gift' = zd. *fal^ra-; zdv 'Spalt' H. 649, oben p. 68
und 70.
Die Dialekte ^) haben hier j, i, wahrend sie fiir z ==
iran. z {g^^ 9^h): z setzen , siehe das Material bei Horn
p. 143—151. Daher zud H. 673 mit z in den Dialekten
--- pages:
zih *Bogeusehne' -> leaf 239 printed 229
garm 'warm' — zd. garenia- -> leaf 256 printed 246
b) garma 'Hitze' -> leaf 251 printed 241
```


## [2026-09-06T15:17:24.214Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"gher\\|GARM\\|garm\" ARY_latin_index_pages.txt | head -10; echo \"=== persian\"; grep -n \"گرم\" ARY_pages.txt | head -8"
}
```


### [2026-09-06T15:17:24.276Z] TOOL RESULT

```
6882:(ALM (OLD HIGH GERMAN) oS lat i. ‘isansgarm ey fails
12573:JERM, CHERM, CHERMOUTIUN GARMA- (OLD PERSIAN) skal +3,
12574:THERMOS, THERME (GREEK) gy» GARM, GARMOG — (PAHLAVI) 6
12577:(OLD SCANDINAVIAN) 4S 54) GARM, GERM, GERM!
12578:YARMR GARM BALUCHD) gr gh
=== persian
300:گزمسیری می‌بود در حالیکه تفریباً همه‌ی واژه‌های گرمسیری و استوایی از ریشه‌ی هند و اروپایی
8312:۲ واژه‌ی "دما" به چم " گرما" هم پکار می‌رود (مثلاً در "دماسنج").
9990:چم این واژه در زبان‌های رومانس و زبان ولزی: گرم) گرما.
9991:چم این واژه در بان ژرمنی: نیم‌گرم» ولرم» ملایم.
10507:۱ چم این واژه در زبان‌های لائین وگالی: گرم (تغییر معنی این واجريشه در این زبان‌ها بسیار جالب است).
12805:۷۲ | گرم گرماه گرمی ۱
15939:چم این واژه در زبان لاتین؛ گرما» جوشش. 8
```


## [2026-09-06T15:17:27.013Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '12795,12830p' ARY_pages.txt; echo \"=== pdf page tag\"; awk 'NR<=12805 && /\\[pdf page/{p=$0} END{print p}' ARY_pages.txt"
}
```


### [2026-09-06T15:17:28.759Z] TOOL RESULT

```
فپ ,پهلری (الاشالاهه: ندادن اسپانیایی (38۸(184): 100
کردی (۹:)8/807574 :۳ ۰ 0178 ,۷۸۸6 ایتالیایی (۸(۷لل17۸): 110
بلوچی (27ع20و) ۹۰ * ای اد رومانی (74۸(): رز
افغانی (پشتو) (/4۳0۸۸): 13 پر تغالی (۳0771701285): 100
تخاری 8 (8 ((4لق ۰:70 ۷۷۸۲۷۷۵ گونیکه (007[710): 5
سانکریت (54۸/5807): ۷۳3615 ,۷3۸ ایسلندی کهن (/5(010477 052):
ارمنی (/470452/414) شآ لاه بات 11
یونانی (0720): 8 ,1008 ساکسونی کهن (/(5440 0ا0): ان
[pdf page 431]
وا |
۷۲ | گرم گرماه گرمی ۱
فریزی کهن (#نفا9ل2# صام). ۷01 برهمی (/80[7821142): ۷
آلمانی کهن (08704۸2 0ات ضزم: ۷۷012 اسلراکی 5101450): ۲۷
آلمانی (05701۸0۷): ۷۵ لیتوانی ((االمناتالم: ۷۲۳ ,کف
انگلیسی کهن (ز5انا20/0 صان): لتونی (لتی) نالیم + ۷8
,۷۷8۸86 آلبانی (مابممهام: رها
انگلیسی (6۸0//57). اه هتیت (7177]76): 11۸
دانمارکی (0۸۷/3[7): 1ص ۰
سوئدی (850([37). ,۷۸36 پسگشت‌ها ده رادید ۲
نروژی (/07180۵9/): الا . ۲ ۶00220
هلندی (00767): ۰ انا 4 ۲3ج دای اد
اسلاری کهن (6ما؟ نان صازم. 138 م22
۷6 ,نا ۷ 0 ۲۵۲ :لمیر
: لهستانی (8ل0): وان 185 ماه
۱ روسی (4۷ا85): ۷0 نمشد ۸ :45( دم 4 مت تمه
چکه (250(7)): ای 1 (۷0۵3) مد اب ها
صربی (567814۷): ۷ برهان قاطع + ۱۹/۸۰
اوستایی (/6۸۳381۸:)188740 ,۸۵110 ارمنی (4(1ا/۸۸4):
پارسی باستان (۲878140۷ طرا0): ۸86۸۰ 6 ,/580[
پهلری (1(ماتنه): 6۸8/0۵ بلاقزج بونانی (088): 7332385 ,371873105
اوستی (0355716): 7 تفج لانین (710ا): 05
کردی ([8015(): گرتبک (۷7۸8۸17۸01:)00771/0 ,۷۸15+
41 ,ق۲838 بانق0۸ ایسلندی کهن (۸2ا0بی5 صزم.
بلرچی (7۳31ا8۸): 2 ۷
افغانی (پشتو) (//4)۳017۸): فریزی کهن (بلماقل۶# صاه): ایند ده
۸ مباقفت۸ج آلمانی کهن (الفلنها0 04ات صام):,
=== pdf page tag
[pdf page 431]
```


## [2026-09-06T15:17:34.564Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"^.\\{0,20\\}زه\\b\\|زه (کمان\\|زه کمان\" ARY_pages.txt | head -10; echo \"=== latin index JYA\"; grep -n \"JYA\\|ZIH\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-06T15:17:36.640Z] TOOL RESULT

```
78:می‌شد ولی امروزه این نام بشتر برای اشاره به زبانهای بخش شمالی شبه قاره‌ی هند و به صورتث
650:۰ امزوزه زبانهای ایرانی محدود به ایران و افغانستان و تاجیکستان و بخش‌های باختری پا کستان
659:پاسداری مرزهای امپراتوری روم در شمال انگلستان؛ به استخدام رومیان درآمدند
815:امروزه ارمنی‌ها که شمار آنها بیش از پنج میلیون نفر است در جمهوری ارمنستان زندگی می‌کنند
818:این زبانها که امروزه معدوم هستند؛ مشتمل‌اند بر تخاری ۸ (۸ 10017۸/87۸1) و تخاری 8
976:و امروزه نیز در میان برخی از آنها ادامه دارد. ولی هند و اروپائیان نیز (مانند اقوام سامی و
1116:." امروزه شمار لبیدها بسیار کم شده است ولی باز هم در برخی نقاط به آنها برمی‌خوریم. در برخی از
1139:اندازه‌ای است که برخی از واژه‌ها و جمله‌های سانسکریتکاملاً مشاب پرابرهای اوستایی ود هستند.
1165:امروزه حدود نیمی از واژگان زبان فارسی عربی با ترکی است. در چند دهای اغیر نفوذ فرهنگی
1390:-واژه‌ی فارسی «چیزه با واژه‌های فرانسوی 270873 و اسپانیایی ۲08۸ و پر تغالی 0018۸ از
=== latin index JYA
5072:PAND ABALUCHI) gz yo > JYAVESTAN) gle yh
8604:(OLD IRISH) eppS 543 2) PJYATI, RAT-, (SANSKRIT) 2, Si
8689:HOLD HIGH GERMAN) 4S glalT RAJ, RAJYA, SANSKRIT) © Sil.
8905:MALLORY & ADAMS: REG- RAJYATE, RANJAYATI, RANGA
9639:AMINDAROV: (DAMAGE) 208 JAYATI, SYANA, JYA-
15751:MACKENZIE: (WORSHIP) 140 YAJNAH, LJYA., YAJYA,, YAJATI
```


## [2026-09-06T15:17:41.472Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '5060,5080p' ARY_latin_index_pages.txt"
}
```


### [2026-09-06T15:17:41.522Z] TOOL RESULT

```
PESTI PUNO (LEX (SPANISH) glk!
PIASTE (RUSSIAN) g-35 PUGNO (QLSCTALIAN) piste!
PUNHO — (.4s12}(PORTUGUESE) 45 »
‘REFERENCES beth FUsT HOLD SAXON) iS gi pS
POKORNY. = OSO*~S~S~«D FEST OLD FRISIAN) WS 523
BARNHART: (FIST) 385 FUST (OLD HIGH GERMAN) oS lst
MACKENZIE: (PAW) 126 FaUsT (GERMAN) lait
ONroNs: (FIsT) 358 FYST (OLD ENGLISH) 5 gS
frt _ (bb oby FIST ENGLISH) 51831
Jeeta
POKORNY: 808 2-254) 912 Sa otf aT oT GIFINGER por! Sle aly bt ely ye!
(BARNHART: (FINGER) 383-384,
PAND ABALUCHI) gz yo > JYAVESTAN) gle yh
PATHAS SANSKRIT) oy Sons PATHO, PANTA, PATH
HUN, HUNI ARMENIAN) ga} (OLD PERSIAN) gosh gs),
PATOS * GREER) li, PANTI, PATHI
PONS, PONTIS HLATIN) ot PAND PAHLAVI) «5 shy
FINTHAN GOTHIC) S53 FAND (OSSETIC) oa s\
OLD SCANDINAVIAN) 45 6-21-41 PEND (KURDISH) 52,5
[pdf page 177]
erie | WA
```


## [2026-09-06T15:17:58.944Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls | head; python3 - <<'EOF'\nimport json,glob\nf='/home/sfmqrb/git/rishe/data/verification/page-205.json'\nd=json.load(open(f))\ne=d['entries'][0]\nprint(json.dumps(e['nodes'][:2],ensure_ascii=False,indent=1)[:3000])\nEOF"
}
```


### [2026-09-06T15:18:00.554Z] TOOL RESULT

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
[
 {
  "id": 1,
  "lang": "Avestan / Old Persian",
  "words": "jiva, jîta, jva; merezu-jîta; hu-jyâti",
  "verdict": "transcription_suspect",
  "derivation": "The substance of the box is right; two of the citation forms are not. (1) Avestan jva- / jīva- 'living' and Old Persian jīva- are the direct u̯-stem continuants of PIE *gʷih₃-wo-: Pokorny 467-469 lists 'Old Indic jīva- \"living, m. life\", Old pers. jīva-, Avestan jva- (i.e. jīva-) \"living\" = Latin vīvus', and Bartholomae's verb entry jī-/jva- 'leben, am Leben sein' quotes the Old Persian imperative 'utā dargam jīva' (Bh 4.10, DPd) 'and may you live long'. Kent, Old Persian, §217, derives OP jīva 'live!' from pIE *gʷi-we and cites the 3rd dual imperfect ajīvatam '(the two) were living' (XPf 20-25). (2) 'jîta' is not an attested Avestan word: the abstract noun is jīti- f. 'life' (Pokorny p.468 '*gʷī-... Avestan jīti- f. \"life\"'), an i-stem, and it means 'life', not 'living'. (3) Likewise 'merezu-jîta': Pokorny 750-751 under *mreǵʰu- 'short' prints 'Avestan mərəzu-jīti-, -jva- \"βραχύβιος\"' (short-lived), and Bartholomae has both mərəzu.jītay- and mərəzu.jva- 'kurz(?) lebend'. So the compound is real and Nourai's gloss 'short lived' is Pokorny's own, but the second member is -jīti-/-jva-, not -jīta-. (4) hu-jyāiti- is genuine: Bartholomae gives jyātay- f. / jyātav- m. 'Leben' and the compounds vīspō.hujyātay- '(der alles gute Leben hat) der alles besitzt und bietet, was zum behaglichen Leben gehört' and frādat̰-vīspąm.hujyāitim 'die alles fördert, was zum behaglichen Menschenleben gehört', which is exactly Nourai's 'healthy, prosperous'; his spelling 'hu-jyâti' drops the diphthong of -jyāiti-. The printed page (pdf 205, saved as sources/refs/ocr/BOOK/205.png) shows 'jîta' and 'merezu-jîta', so the JSON is a faithful reading and the inaccuracy is the book's.",
  "derivation_fa": "محتوای این جعبه درست است اما دو صورت اوستایی آن دقیق نیست. اوستایی jva-/jīva- و پارسی باستان jīva- «زنده» بازماندهٔ مستقیم صورت *gʷih₃-wo- هندواروپایی‌اند؛ پوکورنی (ص ۴۶۷–۴۶۹) همین را می‌آورد و کنت در دستور پارسی باستان صورت امری jīva «زندگی کن!» (بیستون ۴٫۱۰) و ajīvatam را شاهد می‌گیرد. اما «jîta» صورتی اوستایی نیست؛ آنچه هست jīti- (نامِ مادّهٔ i-ستاک) به معنای «زندگی» است، نه «زنده». همچنین ترکیب «کوته‌زیست» در پوکورنی (ص ۷۵۰) به شکل mərəzu-jīti- و mərəzu-jva- ثبت شده است. hu-jyāiti- «زندگی خوش، کامروایی» نزد بارتولمه درست است (jyātay- «زندگی»). تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «jîta» را چاپ کرده، پس خطا از کتاب است نه از خوانش اسکن.",
  "error_in": "book",
  "book_prints": "jiva, jîta, jva ; merezu-jîta ; hu-jyâti",
  "correct_form": "jva-/jīva- 'living'; jīti- f. 'life' (not jîta); mərəzu-jīti- / mərəzu-jva- 'short-lived'; hu-jyāiti- 'good living'",
  "sources": [
   "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7eyh%E2%82%83-"
  ],
  "ref_check": [
   {
    "ref": "KLN:1288",
    "status": "supports",
    "note": "Klein 1966 p.1288 s.v. 'quick': 'fr. Teut. *qwiqwa-, \"livi
```


## [2026-09-06T15:18:04.865Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 - <<'EOF'\nimport json\nd=json.load(open('page-205.json'))\nfor e in d['entries'][:1]:\n    for n in e['nodes'][1:3]:\n        print(n['id'], n['lang'], n['verdict'])\n        print(n['derivation'][:700])\n        print('--consulted--', json.dumps(n['consulted'],ensure_ascii=False)[:600])\n        print()\nEOF"
}
```


### [2026-09-06T15:18:06.466Z] TOOL RESULT

```
2 Pahlavi plausible
Both words are genuine Middle Persian, and the derivation from the Old Iranian root is uncontested; the two things to correct are a reading and a gloss. (1) 'zivastan' is Horn's 1893 reading of Book Pahlavi ⟨zywstn'⟩: Grundriss no. 683 prints 'phlv. zīvastan, z'w(i)šn, zīvēt (3. Sg.), zīvandak'. MacKenzie's 1971 Concise Pahlavi Dictionary reads the same spelling as 'zī(wi)stan, zī(w)- [zywstn' | M zywystn, zyw-, N zīstan] live', i.e. zīwistan, and Moʿin's footnote in Borhān (p.~1038) also writes zīvistan; so the form in the chart is a superseded reading rather than an error of substance. (2) zīwandag is attested, but it means 'living, alive', not 'mercury': Hübschmann, Persische Studien, rec
--consulted-- [{"src": "PHD", "where": "MacKenzie, Concise Pahlavi Dictionary p.99 (PHD.txt line 680)", "stance": "partial", "note": "'zī(wi)stan, zī(w)- [zywstn' | M zywystn, zyw-, N zīstan] live. zī(w)išn [zywšn'] life; livelihood. zīwēnīdan, zīwēn- vivify, revive. zindag [zy(w)ndk' | M zyndg, N zinda] alive, living.' MacKenzie has zindag but not a separate zīwandag, and no mercury sense."}, {"src": "NYB", "where": "Nyberg, Manual of Pahlavi II (glossary)", "stance": "silent", "note": "grep of NYB_vol2_glossary.txt for zīwistan / zīwandag returned nothing: Shkand-Gumānīg Wizār and the Bundahišn texts Nybe

3 Persian confirmed
All three, and the three extra forms in the box (زیست، زی، آبزی), continue Middle Persian zīw-. (1) زیستن zīstan < MP zī(wi)stan; the intervocalic -w- of the present stem zīw- was lost before the New Persian ending, giving زی‌ zī-/زیَد zīyad, with the old -w- still visible in Awromani ziwāy and Kurdish ziyān; Cheung, Etymological Dictionary of the Iranian Verb, s.v. *jaiH2 (p.223) lists 'NP zīstan/zīy- "to live" ... NP zindah', ultimately '*PIE *gʷeiH₃-, LIV 215 f., Pok. 467 f.'. زیست is the past stem used as a noun ('life, biology'), زی the bare present stem, آبزی 'aquatic (organism)' a modern compound آب + زی of exactly that stem. (2) زندگی is the abstract in -ī of زنده zenda < MP zindag [
--consulted-- [{"src": "CHEUNG", "where": "Etym. Dict. of the Iranian Verb, *jaiH2, p.223 (CHEUNG.txt line 14986)", "stance": "supports", "note": "'*NWIR: NP zīstan/zīy- \"to live\", Kurd. žīyan/žī-, Awrom. žiwāy/-žiw-, ... NP zindah ... *SANSKRIT: jīv- \"to live\" ... «PIE *gʷeiH₃-, *gʷieH₃- ... LIV: 215 f. | Pok.: 467 f.'"}, {"src": "HRN", "where": "Grundriss no. 683 (p.151)", "stance": "supports", "note": "'zīsten \"leben\", Praes. zīy-em; zinde; zīve, jīve \"Quecksilber\"'; footnote: 'Skr. jīvaka- \"lebendig, lebhaft\"; LW. arab. zi'baq, syr. ..., kurd. zīve, arm. zpak \"Quecksilber\"'."}, {"src": "BQT"
```


## [2026-09-06T15:19:19.216Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFM فرن\"; grep -n \"( الفرن )\\|الفرن\\|فرن\" AFM_pages.txt | head -8; echo \"== PLA furn\"; grep -rn \"furn\\b\\|فرن\" incoming/PLA/PLA_pages.txt 2>/dev/null | head -6; echo \"== KLN fillet\"; grep -on \"fillet, n\\..\\{0,200\\}\" KLN_1971.txt | head -2; echo \"== SKT thermometer\"; grep -on \"THERMOMETER.\\{0,200\\}\\|Thermometer.\\{0,200\\}\" SKT.txt | head -3"
}
```


### [2026-09-06T15:19:20.960Z] TOOL RESULT

```
== AFM فرن
109:وفي كرم جرم . ا باء ٠وثي‏ ܨ ܢ فرند او برند ٠وفي‏ كته قرط ق ٠‏ وف ܥܕ به
139:ܝ ® ܨ الافرنسة ܗ الم مم الصرية ٠وان‏ النجمة * اسارة الى
159:ܠ كردي × يق وهر به الرمالى 11 والفرنسي عطعناك
183:ܕ | ܟ بالارامية ܦܐܢܐ ܦܐܐ ° ® بهي وبالفرنسية 18811
190:| 0 13110 و 0 2 000 نالع ٠‏ ومئنهة الفرني ¢¢
212:لقمل الشوك الأرضي فهو عا 17 م 4 الفرني 56 ܐ( ܢܘܟ به
231:بيردت ܝ بالافرنسية ° 11125
261:و 5.5 1ل يك »هيع (فرنكل ض : \ \ ¥)
== PLA furn
== KLN fillet
92941:fillet, n. — F. filet , dimin. of fil, ‘thread, fr. L. 
== SKT thermometer
19570:Thermometer,  an  instrument  for  mea- suring  the  temperature.  (Gk.)  From  Gk. 0tpn6-f,  warm,  allied  to  Skt.  gharma, warm ;  and  t^irpow,  %  measurer ;  see Metre.
```


## [2026-09-06T15:19:28.071Z] TOOL CALL #89: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D8%B1%D9%85%D9%88%D9%85%D8%AA%D8%B1/",
 "prompt": "Quote the Persian dictionary entries (Dehkhoda / Mo'in / Amid) for ترمومتر — especially any origin tag such as [فر.] (French) or the French source word thermomètre. Also any entry for ترموس."
}
```


## [2026-09-06T15:19:29.998Z] TOOL CALL #90: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D8%B1%D9%88%D9%81%DB%8C%D9%84/",
 "prompt": "Quote the Persian dictionary entries (Dehkhoda / Mo'in / Amid) for پروفیل — especially any origin tag such as [فر.] (French) and the French source word (profil / profilé), and the meaning 'shaped metal sections'."
}
```


### [2026-09-06T15:19:35.693Z] TOOL RESULT

```
# Persian Dictionary Entries for ترمومتر

## Dehkhoda Dictionary
**Origin tag:** [فرانسوی، اِ] (French)

The entry notes: "میزان الحراره که سرما و گرما را نشان میدهد، این لفظ فرانسوی است"
(An instrument showing cold and heat; this is a French term)

The entry explains the word derives from Greek: "مأخوذ از ترموس بمعنی گرما و مترون بمعنی اندازه یونانی"
(Derived from Greek thermos meaning heat and metron meaning measure)

## Mo'in Dictionary
**Entry:** (تِ مِ) [فر.] (اِمر.) دماسنج، گرماسنج

The origin is marked as French [فر.] and American [اِمر.], with Persian equivalents provided.

## Amid Dictionary
**Entry:** دماسنج

A concise entry listing the Persian equivalent.

---

**Note:** The document does not contain a separate dictionary entry for ترموس (thermos), though it is mentioned in the Dehkhoda entry's etymology section.
```


### [2026-09-06T15:19:36.341Z] TOOL RESULT

```
# Persian Dictionary Entries for پروفیل

**Farhang-e Mo'in:**
"(پُ رُ ) [ فر. ] (اِ. ) ۱ - نقشه و تصویری که مقطع طولی ساختمان یا سازه را نشان دهد"

This entry marks the term as French-origin [فر.], defining it as an architectural drawing showing longitudinal cross-sections.

**Farhang-e Amid:**
"نقشه و تصویر ساختمان که یک طرف آن را نشان بدهد، مثل اینکه آن را از میان بریده باشند"

This dictionary similarly describes it as a structural illustration, employing the metaphor of a building cut lengthwise to reveal its profile.

**General Encyclopedia Entry:**
The source notes that the term refers to "مقطع ثابت و طول بسیار" (constant cross-section with substantial length), used in construction and mechanical engineering for steel components manufactured in various configurations by iron foundries.

The French origin [فر.] indicates *profil* as the etymological source.
```


## [2026-09-06T15:19:42.933Z] TOOL CALL #91: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0er-\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%86\" \\\n \"https://fr.wiktionary.org/wiki/four\" \\\n \"https://en.wiktionary.org/wiki/filum\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%87\" \\\n \"https://www.etymonline.com/word/profile\" \\\n \"https://abadis.ir/fatofa/%D8%AA%D8%B1%D9%85%D9%88%D9%85%D8%AA%D8%B1/\" \\\n \"https://abadis.ir/fatofa/%D9%BE%D8%B1%D9%88%D9%81%DB%8C%D9%84/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 216 (Gwher / Gwhi) verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:19:50.078Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9d711bdd3e60eaad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c1b0e73d79e8a38a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5290a53c2f11053a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fd0819c749150549.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f021be6c3bf5c8e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6c517c7f333af566.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/affbc31750127810.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b70bb9200671c510.txt
```


## [2026-09-06T15:19:54.807Z] TOOL CALL #92: Bash

```json
{
 "command": "cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg216.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/216.png && sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:19:54.867Z] TOOL RESULT

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


## [2026-09-06T15:19:57.485Z] TOOL CALL #93: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:19:57.541Z] TOOL RESULT

```
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


## [2026-09-06T15:21:00.196Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:34:11.443Z] TOOL CALL #94: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216 && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_head.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\n\nW_POK = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0er-\"\nW_FURN = \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%86\"\nW_FOUR = \"https://fr.wiktionary.org/wiki/four\"\nW_FILUM = \"https://en.wiktionary.org/wiki/filum\"\nW_ZEH = \"https://en.wiktionary.org/wiki/%D8%B2%D9%87\"\nW_PROF = \"https://www.etymonline.com/word/profile\"\nA_TERM = \"https://abadis.ir/fatofa/%D8%AA%D8%B1%D9%85%D9%88%D9%85%D8%AA%D8%B1/\"\nA_PROF = \"https://abadis.ir/fatofa/%D9%BE%D8%B1%D9%88%D9%81%DB%8C%D9%84/\"\n\nentry0 = {\n  \"entry\": 0,\n  \"root\": \"Gwher\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *gʷʰer- 'to be/become warm, hot' (o-grade *gʷʰor-mo-, *gʷʰor-no-)\",\n  \"note\": \"Pokorny 493-495 'gʷher- : hot, warm'; Watkins/AHD 'gʷher-'; Wiktionary *gʷʰer- 'to be warm'. Root name, language label ('Indo-European' = PIE) and gloss 'warm' are all correct; Nourai's 'Gwher' is simply his ASCII spelling of gʷher-. Every branch drawn on this page (Av. garəma-, OP garma-pada-, Gk. thermós, Lat. formus/fornus/fornāx/forceps) stands verbatim in Pokorny's article on p.493 and in Watkins's AHD entry, so the whole chart is really a transcript of POK:493 + AHD. The one substantive problem on the page is the Persian box #12 (fer / forn / fârîneh) and the accompanying note about a Latin > Persian > Arabic > France round trip, which modern scholarship reverses.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *gʷʰer- «گرم بودن/گرم شدن» است؛ پوکورنی در صفحهٔ ۴۹۳ ایو (IEW) همین ریشه را با معنای «heiß, warm» آورده و واتکینز در پیوست ریشه‌های هندواروپاییِ AHD نیز آن را با همین معنا ثبت کرده است. نام ریشه، برچسب زبانی و معنایی که نورایی داده هر سه درست است و همهٔ شاخه‌های این نمودار (اوستایی garəma-، پارسی باستان garma-pada-، یونانی thermós، لاتین formus/fornus/fornāx/forceps) عیناً در همان صفحهٔ پوکورنی و در مدخل AHD آمده‌اند؛ پس ادعای نورایی دربارهٔ خودِ ریشه درست است. تنها گرهِ مسئله‌دار این صفحه جعبهٔ فارسیِ «فِر/فُرن/فارینه» و یادداشتِ زیر آن است که پژوهش امروزی جهتِ وام‌گیری را وارونه می‌داند.\",\n  \"sources\": [W_POK],\n  \"ref_check\": [\n    {\"ref\": \"POK:493\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt, entry 'Root / lemma: g^her-  Meaning: hot, warm ... Page(s): 493-495': 'Avestan garəma- ‘hot’, n. ‘heat’. Old pers. in garma-pada- name of a month, perhaps ‘*beginning of the heat’ (= Latin formus, German warm) ... Gr. θέρος n. ‘summer heat, harvest’, θερμός ‘warm’ ... Latin formus ‘warm’ (Festus), fornus, furnus (*gʷhorno-s), fornax ‘oven’ ... References: WP. I 687 ff.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 687 (WLD_Bd1_pages.txt line 65102)\", \"stance\": \"supports\",\n     \"note\": \"'Lat. formus „warm“ (Festus), fornus furnus, fornāx „Ofen“' — the entry Pokorny 493 was later condensed from.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷher- (AHD_watkins1985.txt line 547)\", \"stance\": \"supports\",\n     \"note\": \"'3. Suffixed form *gʷher-mo- in Greek thermos, warm, hot ... 4. O-grade form *gʷhor- in Latin forceps, pincers, fire tongs (< “that which holds hot things”; -ceps ... see kap-) ... 5. Suffixed o-grade form gʷhor-no- in: a. Latin fornus, fornāx, oven: FORNAX, FURNACE. [Pok. gʷher- 493 ...]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, An Indo-European Comparative Dictionary, s.v. guhermos (IEC.txt line 5490)\", \"stance\": \"supports\",\n     \"note\": \"'guhermos ... “warm, hot; heat”. Variant: guhorm-. WP I, 687. Skt. gharmáh; Av. garomo adj.; OPer. garma-; Per. garm adj.; Oss. qarm; Arm. germ; Gk. thermós; OLat. formus (Fest.)' — one entry covering Avestan, Old Persian and New Persian.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 15.85 'Hot, warm' (SYN.txt line 27265)\", \"stance\": \"supports\",\n     \"note\": \"the comparative list for HOT/WARM prints 'Av. garəma-, tapta-' beside Gk. thermós and the Slavic goreti group.\"}\n  ],\n  \"nodes\": []\n}\njson.dump(entry0, open(os.path.join(OUT, \"e0.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_head.py"
}
```


### [2026-09-06T15:34:13.460Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:35:14.654Z] TOOL CALL #95: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n1.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_POK = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0er-\"\n\nnodes = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"garema\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Avestan garəma- is the regular Indo-Iranian o-grade thematic *gʷʰor-mo- > Proto-Indo-Iranian *gharma- (Sanskrit gharmá- m. 'heat, glow'), with PIE *o > Indo-Iranian *a and the aspirated labiovelar *gʷʰ giving Iranian g-; the anaptyctic ə of gar-ə-ma- is Avestan orthography for the syllabic r-cluster. It is both an adjective 'warm, hot' and a neuter noun 'heat', exactly Nourai's gloss. Pokorny prints it in the same breath as the Old Persian month-name and Latin formus, and Nyberg's glossary gives the Avestan reference numbers (Av. 515 garəma-, 516 garəmu- 'heat').\",\n  \"derivation_fa\": \"صورت اوستایی garəma- «گرم؛ گرما» بازماندهٔ منظمِ ستاکِ *gʷʰor-mo- (درجهٔ o) هندواروپایی است که در ایرانی–هندی باستان به *gharma- بدل شده (سنسکریت gharmá- «گرما»). واکهٔ o هندواروپایی در هندوایرانی به a تبدیل شده و *gʷʰ آغازین در ایرانی g- داده است؛ ə در gar-ə-ma- تنها نشانهٔ نگارشیِ اوستایی برای خوشهٔ ر است. این واژه هم صفت است («گرم») و هم اسم خنثی («گرما»)، درست همان چیزی که نورایی آورده. ادعای نورایی درست است؛ پوکورنی، بارتولمه (به نقل نیبرگ، شمارهٔ ۵۱۵) و مان همگی همین را می‌گویند.\",\n  \"sources\": [W_POK],\n  \"ref_check\": [\n    {\"ref\": \"POK:493\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt s.v. g^her- (Page(s): 493-495): 'gharma-m. “blaze, glow, heat”, Avestan garəma- “hot”, n. “heat”. Old pers. in garma-pada- name of a month'.\"},\n    {\"ref\": \"KNT:183\", \"status\": \"supports\",\n     \"note\": \"Kent, Old Persian, Lexicon s.v. Garmapada- (KNT.txt \\\\f-leaf 206 = printed p.183): 'From garma- “heat”, Av. garəma-, Skt. gharmá-, Lt. formus “hot”, NEng. warm, pIE *gʷhormo-, cf. Gk. thermos' — Kent cites the Avestan form as the cognate of the OP one.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary) s.v. garm (NYB_vol2_glossary.txt line 1636)\", \"stance\": \"supports\",\n     \"note\": \"'garm [glm], garmōk [glmwk'] hot, warm ... — Av. (515) garəma-, (516) garəmu- “heat”; MPrs grm’g “heat”; NP garm.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. guhermos (IEC.txt line 5490)\", \"stance\": \"supports\",\n     \"note\": \"'Av. garomo, adj.' listed among the reflexes of gʷhermos, WP I, 687.\"},\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch (BRT.txt)\", \"stance\": \"silent\",\n     \"note\": \"greps for 'garəma', 'garema', 'garǝma' in the local OCR returned nothing — the Avestan-script/diacritic OCR of BRT.txt is too corrupt to locate col. 513 f.; not a contradiction, just illegible.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 15.85 HOT, WARM (SYN.txt line 27265)\", \"stance\": \"supports\",\n     \"note\": \"'Av. garəma-, tapta-' is Buck's Avestan entry for 'hot, warm'.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"garm «گرم»  [+ گرما ، گرمابه]\", \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian گرم garm continues Old Iranian *garma- through Middle Persian garm ⟨glm⟩ (MacKenzie p.36: 'garm [glm | M grm, N ~] warm, hot'); the stem is unchanged because a short a before rm needs no adjustment and MP -m is kept. The two extra forms in the box are equally regular: گرما garmā < MP garmāg ⟨glm'k'⟩ 'warmth, heat' (MacKenzie 'garmāg [glm'k' | M grmg, N garmā]'), the MP suffix -āg losing its final -g in New Persian as in NP dānā < MP dānāg; and گرمابه garmābe 'bath-house' < MP garm-ābag, i.e. garm 'warm' + āb 'water' + the place suffix -ag > NP -e (Moʿin's own footnote: «از: گرم + آب + ه (پسوند مکان)»). Strictly the line of descent is Old Iranian *garma- > MP > NP, with Avestan garəma- a sister form rather than the ancestor; Nourai's arrow from the Avestan box is the usual chart shorthand and does not affect the substance.\",\n  \"derivation_fa\": \"«گرم» فارسی نو بازماندهٔ *garma- ایرانی باستان است که از راه فارسی میانهٔ garm (نگارش پهلوی ⟨glm⟩) به فارسی دری رسیده؛ مکنزی در فرهنگ کوچک پهلوی می‌آورد: garm [glm | M grm, N ~] «گرم». دو صورت دیگرِ جعبه نیز منظم‌اند: «گرما» از فارسی میانهٔ garmāg («garmāg [glm'k' | N garmā]») با افتادن g پایانیِ پسوند -āg در فارسی نو (مانند دانا < dānāg)، و «گرمابه» از garm-ābag پهلوی، یعنی گرم + آب + پسوند مکانِ -ag که در فارسی نو «ـه» شده است؛ معین در حاشیهٔ برهان قاطع (ص ۱۸۰۰، پانوشت ۹) دقیقاً می‌نویسد «از: گرم + آب + ه (پسوند مکان)». نکتهٔ دقیق آنکه فارسی نو دنبالهٔ اوستایی نیست بلکه هم‌ریشهٔ آن است و راه واقعی ایرانی باستان › فارسی میانه › فارسی نو است؛ پیکانِ نورایی از جعبهٔ اوستایی اختصارِ رایج نمودارهاست و در اصلِ مطلب خللی وارد نمی‌کند. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"HRN:203\", \"status\": \"supports\",\n     \"note\": \"Horn, Grundriss der neupersischen Etymologie, no. 911, p.203 (HRN.txt \\\\f-leaf 225): '911. germ “warm”, germā “Wärme” ... ap. garma- in Garmapada-; aw. garəma- “warm”; phlv. garm, garmāk, garmīh; ai. gharmá- “Wärme”; arm. ǰerm “warm” ... kurd. bel. garm'.\"},\n    {\"ref\": \"BQT:1800\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qateʿ p.1800 (rendered via tools/ref_page.py BQT:1800 --pdf-page 597; the default offset lands on p.1798), Moʿin's footnote 7 to گرم: «پارسی باستان garma- (در garma-pada)؛ اوستا garəma-؛ پهلوی garm؛ هندی باستان gharma- (گرمی)؛ ارمنی ǰerm (تب)؛ کردی و بلوچی garm ...» and footnote 9 to گرمابه: «از: گرم + آب + ه (پسوند مکان)». Note that Nourai's page number is right but it is the printed page of vol. 3, reached as pdf page 597 not 595.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.36 (PHD.txt line 378)\", \"stance\": \"supports\",\n     \"note\": \"'garm [glm | M grm, N ~] warm, hot. ~īh: warmth, heat. garm-ābag [glm'pk' | N ~a] bath-house. garmāg [glm'k' | M grmg, N garmā] warmth, heat. garmsēr [glmsyl | N ~] warm region.'\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien pp.241 and 246 (HUB.txt lines 8617-8618, 8808)\", \"stance\": \"supports\",\n     \"note\": \"'b) garmā “Hitze” = phl. garmāk ... neben garm “heiss” = phl. garm, ap. garma- in garmapada-'; and in the sound-law list 'garm “warm” — zd. garəma-'.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. garm (NYB_vol2_glossary.txt line 1636)\", \"stance\": \"supports\",\n     \"note\": \"'MPrs grm’g “heat”; NP garm' — the Middle Persian link Nourai's chart skips.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi, pdf page 431 (printed 432), entry گرم / گرما / گرمی\", \"stance\": \"supports\",\n     \"note\": \"the entry lists «اوستایی garəma-؛ پارسی باستان garma-؛ پهلوی garmāg؛ یونانی thermós, thérmē؛ لاتین formus» and cites «برهان قاطع».\"}\n  ]\n }\n]\njson.dump(nodes, open(os.path.join(OUT, \"e0_n12.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n1.py"
}
```


### [2026-09-06T15:35:16.478Z] TOOL RESULT

```
ok 2
```


## [2026-09-06T15:36:09.284Z] TOOL CALL #96: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n2.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_POK = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0er-\"\n\nnodes = [\n {\n  \"id\": 3, \"lang\": \"Old Persian\", \"words\": \"garma ; garma-pada\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Old Persian garma- 'heat' is the same *gʷʰor-mo- formation as Avestan garəma-, and it is attested only inside the calendar name Garmapada-, the fourth Achaemenid month (roughly June-July), spelled ⟨g-r-m-p-d⟩ and read in DB 1.42 'Garmapadahya māhyā IX raucabiš θakatā āha' ('nine days of the month Garmapada were past'). Kent's Lexicon analyses it as garma- 'heat' + pada- 'step, station' = 'Heat-Station Month', so Nourai's gloss 'name of a (hot) month' is exactly right; his separate 'garma : warm' entry is a legitimate abstraction of the first member, though the bare adjective is not itself attested in the inscriptions. Old Persian keeps the cluster -rm- and shows none of the Avestan anaptyxis.\",\n  \"derivation_fa\": \"پارسی باستان garma- «گرما» همان ساختِ *gʷʰor-mo- است که در اوستایی garəma- دیده می‌شود، اما در کتیبه‌ها تنها در نامِ ماهِ Garmapada- (چهارمین ماه هخامنشی، تقریباً تیر) به کار رفته است؛ در بند ۴۲ از ستون یکم بیستون می‌خوانیم Garmapadahya māhyā IX raucabiš θakatā āha «نه روز از ماه گَرمَپَدَ گذشته بود». کنت در واژه‌نامهٔ پارسی باستان (ص ۱۸۳) آن را garma- «گرما» + pada- «گام، جایگاه» یعنی «ماهِ جایگاهِ گرما» می‌داند؛ پس تعریفِ نورایی («نام ماهی گرم») درست است. تنها نکته آنکه صفتِ تنهای garma- در کتیبه‌ها گواهی نشده و برساختهٔ تحلیلی است. برخلافِ اوستایی، در پارسی باستان خوشهٔ -rm- بدون واکهٔ میانجی می‌ماند. ادعای نورایی درست است.\",\n  \"sources\": [W_POK],\n  \"ref_check\": [\n    {\"ref\": \"POK:493\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt s.v. g^her-: 'Old pers. in garma-pada- name of a month, perhaps “*beginning of the heat” (= Latin formus, German warm; Old Prussian gorme)'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.183 s.v. Garmapada- (KNT.txt \\\\f-leaf 206)\", \"stance\": \"supports\",\n     \"note\": \"'From garma- “heat”, Av. garəma-, Skt. gharmá-, Lt. formus “hot”, NEng. warm, pIE *gʷhormo-, cf. Gk. thermos (with analogical -e-), + pada- “step, station”: “Heat-Station Month”. — Garmapadahya gsm. DB 1.42; 3.71, 46.' Kent's grammar (p.176 §1820) also lists 'gar-ma- in month name Garma-pada-' among primary -ma- formations.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. guhermos (IEC.txt line 5490)\", \"stance\": \"supports\",\n     \"note\": \"'OPer. garma-' is listed as a direct reflex of gʷhermos.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.241 (HUB.txt line 8618)\", \"stance\": \"supports\",\n     \"note\": \"'ap. garma- in garmapada-'.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"grm\", \"verdict\": \"plausible\",\n  \"derivation\": \"Sogdian ⟨γrm⟩, read γarm 'hot', is genuine: Gharib's dictionary entry 4259 (Buddhist and Manichaean texts, printed p.~168-169) gives 'γrm B, M | γarm ... hot' with references to GMS 526, TSP 2.302, SCE 292 and the Vessantara Jātaka 533, and notes the locative γarmy. Its ancestry, however, is Proto-Iranian *garma-, not Old Persian: Sogdian is an Eastern Iranian language and did not borrow its ordinary vocabulary from the South-Western Achaemenid dialect. Gharib's own note '©<OP garma-' is comparative shorthand (he prints the Khwarezmian γrm- and Yaghnobi γarm alongside), and the Eastern Iranian development *g- > γ- before a is precisely what shows the word to be inherited rather than taken over from Persian, where g- stays g-. So the form and the meaning are confirmed; only the direction of the arrow (Old Persian > Sogdian) is a genealogical shortcut.\",\n  \"derivation_fa\": \"صورت سغدی ⟨γrm⟩ = γarm «گرم» واقعی است؛ قریب در فرهنگ سغدی، مدخل ۴۲۵۹ (صفحهٔ چاپیِ ۱۶۸–۱۶۹) می‌آورد «γrm B, M | γarm ... hot» با ارجاع به GMS 526، TSP 2.302، SCE 292 و ویسنتره‌جاتکه ۵۳۳. اما تبارِ آن ایرانی باستانِ *garma- است، نه پارسی باستان: سغدی از شاخهٔ ایرانیِ خاوری است و واژگان عادی خود را از گویشِ جنوب‌باختریِ هخامنشی وام نگرفته است. یادداشتِ «‎<OP garma-» در فرهنگ قریب اشارهٔ مقایسه‌ای است (او خوارزمی γrm- و یغنابی γarm را هم در کنارش می‌آورد)، و همین تبدیلِ g- آغازین به γ- که ویژهٔ ایرانیِ خاوری است نشان می‌دهد واژه ارثی است نه وام‌گرفته از فارسی که در آن g- می‌ماند. پس صورت و معنا درست است و تنها جهتِ پیکان (پارسی باستان › سغدی) ساده‌سازیِ تباری است؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"SOD:169\", \"status\": \"supports\",\n     \"note\": \"Gharib, Sogdian Dictionary, entry 4259 (SOD_pages.txt \\\\f-leaf 234; printed page ≈ leaf − 66 = 168-169, i.e. Nourai's page): 'γrm B, M | γarm ©<OP garma-, Khwar. γrm-, Yaghn. γarm ©loc. -y | hot | GMS 526; TSP 2.302, 421, 3.262; SCE 292; BSTBL, Dhy. 346; VJ 533'. The neighbouring entries 4260 γrmw'y and 4261 γrm'ych 'a kind of hot food' belong to the same stem.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib no. 4259 (SOD_pages.txt line 15843)\", \"stance\": \"supports\",\n     \"note\": \"as quoted in ref_check; Gharib himself sets the word beside Khwarezmian γrm- and Yaghnobi γarm, i.e. an inherited Eastern Iranian family.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. guhermos (IEC.txt line 5490)\", \"stance\": \"partial\",\n     \"note\": \"Mann lists 'OPer. garma-; Per. garm; Oss. qarm' for this stem but no Sogdian form — the Ossetic q- (< *γ-) is the Eastern Iranian parallel to Sogdian γrm and shows the word is inherited, not a Persian loan.\"}\n  ]\n }\n]\njson.dump(nodes, open(os.path.join(OUT, \"e0_n34.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n2.py"
}
```


### [2026-09-06T15:36:11.501Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:37:22.040Z] TOOL CALL #97: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n3.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_POK = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0er-\"\nA_TERM = \"https://abadis.ir/fatofa/%D8%AA%D8%B1%D9%85%D9%88%D9%85%D8%AA%D8%B1/\"\n\nnodes = [\n {\n  \"id\": 5, \"lang\": \"Greek\", \"words\": \"thermos\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Greek θερμός 'warm, hot' is the e-grade *gʷʰer-mo-, beside the noun θέρμη f. 'heat' and θέρος n. 'summer heat, harvest'; the labiovelar *gʷʰ gives Greek th- before the front vowel e (θ), and *e is kept, so Greek shows the full grade where Indo-Iranian and Latin show the o-grade (Skt. gharmá-, Lat. formus). Kent expressly calls the Greek -e- analogical beside pIE *gʷhormo-. Nourai's double gloss 'warm, heat' covers both θερμός (adj.) and θέρμη (n.), which is the form the modern compounds are actually built on.\",\n  \"derivation_fa\": \"یونانی θερμός «گرم» صورتِ درجهٔ e ریشه، یعنی *gʷʰer-mo- است؛ در کنارِ آن اسمِ θέρμη «گرما» و θέρος «گرمای تابستان» می‌آید. لبی‌کامیِ *gʷʰ در یونانی پیش از واکهٔ پیشینِ e به θ (th) بدل شده و خودِ e نگه داشته شده است؛ از این‌رو یونانی درجهٔ کاملِ ریشه را نشان می‌دهد حال آنکه هندوایرانی و لاتین درجهٔ o را دارند (سنسکریت gharmá-، لاتین formus). کنت نیز -e- یونانی را قیاسی می‌داند. معنایی که نورایی آورده («گرم، گرما») هر دو صورتِ صفتی و اسمی را پوشش می‌دهد و ترکیب‌های امروزی بر پایهٔ θέρμη ساخته شده‌اند. ادعای نورایی درست است.\",\n  \"sources\": [W_POK],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. gʷher- (AHD_watkins1985.txt line 547): '3. Suffixed form *gʷher-mo- in Greek thermos, warm, hot (> thermē, heat): THERM, -THERM, THERMO-, -THERMY; HYPOTHERMIA.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny 493 (POK_full.txt, s.v. g^her-)\", \"stance\": \"supports\",\n     \"note\": \"'Gr. θέρος n. “summer heat, harvest”, θέρομαι “become hot”, θερμός “warm”, θέρμασσα “oven”.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. guhermos (IEC.txt line 5490)\", \"stance\": \"supports\",\n     \"note\": \"'Gk. thermós, adj.; thérme, f. s. beside thérma, n.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Thermometer (SKT.txt line 19570)\", \"stance\": \"supports\",\n     \"note\": \"'From Gk. θερμό-ς, warm, allied to Skt. gharma, warm; and μέτρον, a measurer.'\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"An empty pass-through box standing for the French scientific coinages on Greek θέρμη that carried the root into Persian: thermomètre, coined in 1624 by the Jesuit Jean Leurechon (Klein s.v. thermometer: 'F. thermomètre, coined by the Jesuit Father Leurechon in 1624 fr. Gk. θέρμη, “heat”, and μέτρον, “measure”'), thermostat (English 1830s, French thermostat), and the trade name thermos (1907). French is genuinely the transmitting language for Persian here, since Persian technical vocabulary of the Qajar and early Pahlavi period came through French, not English.\",\n  \"derivation_fa\": \"این جعبهٔ تهی نمایندهٔ واژه‌های علمیِ فرانسوی است که بر پایهٔ θέρμη یونانی ساخته شده‌اند و ریشه را به فارسی رسانده‌اند: thermomètre که کلاین می‌گوید یسوعیِ فرانسوی ژان لورشون در ۱۶۲۴ آن را از θέρμη «گرما» و μέτρον «اندازه» ساخت؛ thermostat؛ و نام تجاریِ thermos (۱۹۰۷). فرانسه در اینجا به‌راستی زبانِ واسطه است، زیرا واژگان فنیِ فارسیِ دورهٔ قاجار و اوایل پهلوی از راه فرانسه وارد شده است نه انگلیسی. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no citation of Nourai's own.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etym. Dict., s.v. thermometer (KLN_1971.txt line 246242)\", \"stance\": \"supports\",\n     \"note\": \"'thermometer, n. — F. thermomètre, coined by the Jesuit Father Leurechon in 1624 fr. Gk. θέρμη, “heat”, and μέτρον, “measure”.'\"},\n    {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Farsi, s.v. ترمومتر (via abadis.ir)\", \"stance\": \"supports\",\n     \"note\": \"«(تِ مِ) [فر.] (اِمر.) دماسنج، گرماسنج» — Moʿin's tag [فر.] = French, i.e. the French box is the actual source of the Persian word.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Persian\", \"words\": \"[ترموس ، ترمومتر ، ترموستات]\", \"verdict\": \"confirmed\",\n  \"derivation\": \"All three are 20th-century French loans, taken over with French phonetics: ترمومتر termometr < Fr. thermomètre, ترموستات termostāt < Fr. thermostat, ترموس termos < Fr. thermos. Persian has no th, so Greek/French th- is rendered ت t-, and the French final -re of thermomètre is reduced to -r. Dehkhoda's entry for ترمومتر states the route explicitly — «[فرانسوی، اِ] ... میزان‌الحراره که سرما و گرما را نشان می‌دهد، این لفظ فرانسوی است ... مأخوذ از ترموس بمعنی گرما و مترون بمعنی اندازه یونانی» — and Moʿin tags it [فر.] (French). Nourai's chain Greek > French > Persian is therefore right; the words did not come to Persian directly from Greek.\",\n  \"derivation_fa\": \"هر سه واژه وام‌واژه‌های فرانسویِ سدهٔ بیستم‌اند و با تلفظ فرانسوی وارد شده‌اند: «ترمومتر» از thermomètre، «ترموستات» از thermostat و «ترموس» از thermos. چون در فارسی واجِ th نیست، thِ یونانی–فرانسوی به «ت» بدل شده و -re پایانیِ فرانسوی به -ر کاهش یافته است. دهخدا خودِ راه را می‌نویسد: «[فرانسوی، اِ] ... این لفظ فرانسوی است ... مأخوذ از ترموس بمعنی گرما و مترون بمعنی اندازه یونانی»، و معین نیز آن را با برچسبِ [فر.] می‌آورد. پس زنجیرهٔ نورایی (یونانی › فرانسوی › فارسی) درست است و این واژه‌ها مستقیم از یونانی به فارسی نیامده‌اند.\",\n  \"sources\": [A_TERM],\n  \"ref_check\": [\n    {\"ref\": \"MON:1072\", \"status\": \"not_found\",\n     \"note\": \"the local Moʿin OCR (MON_part1.txt / MON_part2.txt, the lexicon volumes) has no ترموس / ترمومتر / ترموستات at all — these belong to Moʿin's vol. 4 (foreign compounds), which is not in the local corpus. The entry itself was read online instead (vajehyab/abadis text of Moʿin: «(تِ مِ) [فر.] (اِمر.) دماسنج، گرماسنج»), so the claim is right even though the cited page could not be opened.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Moʿin s.v. ترمومتر (abadis.ir mirror of the Moʿin text)\", \"stance\": \"supports\",\n     \"note\": \"«(تِ مِ) [فر.] (اِمر.) دماسنج، گرماسنج» — origin tag [فر.] = فرانسه.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\",\n     \"note\": \"greps for ترموس / ترمومتر returned nothing; Aryanpur covers inherited Indo-European vocabulary, not modern European loans.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. thermometer (KLN_1971.txt line 246242)\", \"stance\": \"supports\",\n     \"note\": \"confirms that the compound is a French coinage of 1624, i.e. the immediate donor language of the Persian form.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"English\", \"words\": \"thermometer, thermostat, thermos\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English thermometer is borrowed from French thermomètre (1624, Leurechon), first in English 1633; thermostat was coined in English in 1831 by Andrew Ure on Greek θερμός + -στατης 'standing'; thermos is the 1907 trade name of the vacuum flask, taken straight from Greek θερμός 'hot'. All are learned formations on the Greek word rather than inherited Germanic material — the inherited English cognate of this root is warm (Watkins lists BURN¹, BRAND, BRINDLED under gʷher- as the Germanic side).\",\n  \"derivation_fa\": \"«thermometer» انگلیسی از thermomètre فرانسوی (۱۶۲۴) گرفته شده و نخستین کاربردش در انگلیسی به ۱۶۳۳ برمی‌گردد؛ «thermostat» را اندرو یور در ۱۸۳۱ در خودِ انگلیسی از θερμός و -στάτης «ایستنده» ساخت؛ و «thermos» نام تجاریِ فلاسکِ خلأ در ۱۹۰۷ است که مستقیم از θερμός گرفته شده. هر سه ساخت‌های عالمانه بر پایهٔ واژهٔ یونانی‌اند نه میراثِ ژرمنی؛ هم‌ریشهٔ ارثیِ انگلیسیِ این ریشه واژهٔ warm است و واتکینز واژه‌های brand و burn را نیز ذیل همین ریشه می‌آورد. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. gʷher-: 'Greek thermos, warm, hot (> thermē, heat): THERM, -THERM, THERMO-, -THERMY; HYPOTHERMIA' — the THERMO- family covers thermometer/thermostat/thermos.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. thermometer (KLN_1971.txt line 246242)\", \"stance\": \"supports\",\n     \"note\": \"'F. thermomètre, coined by the Jesuit Father Leurechon in 1624 fr. Gk. θέρμη ... and μέτρον' — English via French.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Thermometer (SKT.txt line 19570)\", \"stance\": \"supports\",\n     \"note\": \"'(Gk.) From Gk. θερμό-ς, warm, allied to Skt. gharma, warm; and μέτρον, a measurer; see Metre.'\"}\n  ]\n }\n]\njson.dump(nodes, open(os.path.join(OUT, \"e0_n5678.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n3.py"
}
```


### [2026-09-06T15:37:24.025Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:38:14.679Z] TOOL CALL #98: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n4.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_POK = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0er-\"\nW_FOUR = \"https://fr.wiktionary.org/wiki/four\"\n\nnodes = [\n {\n  \"id\": 9, \"lang\": \"Latin\", \"words\": \"for-nus, fornâx ; for-ceps\", \"verdict\": \"confirmed\",\n  \"derivation\": \"The Latin family rests on the adjective formus 'warm' (< *gʷʰor-mo-, the exact match of Avestan garəma-, preserved only by Festus), from which the -no- derivative fornus / furnus 'oven' (< *gʷʰor-no- or *gʷʰr̥-no-) and its feminine ā-stem enlargement fornāx, -ācis 'furnace, industrial oven' are formed; Ernout-Meillet separate the two in use — 'furnus désigne le four à pain (furnarius, le boulanger); fornax, le four industriel'. forceps 'tongs' is a compound *formi-caps > forceps, i.e. formus 'hot' + capere 'to seize', literally 'that which takes hot things', which is why Nourai adds the cross-reference to his root 'Kap' (PIE *kap-) for the second member; the ancient grammarians already explain it so (Paulus-Festus 74,6 'forcipes dicuntur quod his forma, i.e. calida, capiuntur'). Nourai's hyphens 'for-nus' and 'for-ceps' mark the root morpheme, not attested spellings.\",\n  \"derivation_fa\": \"این خانوادهٔ لاتینی بر صفتِ formus «گرم» استوار است (از *gʷʰor-mo-، دقیقاً برابرِ اوستایی garəma-) که تنها فِستوسِ دستورنویس آن را نگه داشته است؛ از همین صفت مشتقِ -no- یعنی fornus/furnus «تنور» (از *gʷʰor-no- یا *gʷʰr̥-no-) و گسترشِ مؤنثِ آن fornāx «کورهٔ صنعتی» ساخته شده است. ارنو و مه‌یه این دو را در کاربرد جدا می‌کنند: «furnus تنورِ نان است (و furnarius یعنی نانوا) و fornax کورهٔ صنعتی». واژهٔ forceps «انبر» ترکیبی است از *formi-caps یعنی formus «گرم» + capere «گرفتن»، یعنی «آنچه چیزهای داغ را می‌گیرد»؛ به همین سبب نورایی برای جزء دوم به ریشهٔ «Kap» ارجاع داده است. دستورنویسان باستان نیز همین را می‌گفتند (پاولوس–فستوس ۷۴٫۶). خط تیره‌های نورایی («for-nus»، «for-ceps») نشانهٔ تجزیهٔ ریشه است نه املای گواهی‌شده. ادعای نورایی درست است.\",\n  \"sources\": [W_POK],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. gʷher-: '4. O-grade form *gʷhor- in Latin forceps, pincers, fire tongs (< “that which holds hot things”; -ceps, agential suffix, “-taker”; see kap-): FORCEPS, FORCIPATE. 5. Suffixed o-grade form gʷhor-no- in: a. Latin fornus, fornēx, oven: FORNAX, FURNACE, HORNITO.' — Nourai's ☞Kap cross-reference is Watkins's own '(see kap-)'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny 493-494 (POK_full.txt s.v. g^her-)\", \"stance\": \"supports\",\n     \"note\": \"'Latin formus “warm” (Festus), fornus, furnus (*gʷhorno-s), fornax “oven” (latter being based on a fem. ā-stem), fornix, -icis “dome”.'\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dict. étym. de la langue latine, s.vv. fornus / furnus / fornax (LAT.txt lines 23662-23705)\", \"stance\": \"supports\",\n     \"note\": \"'fornus, -a, -um: chaud. L'adj. n'est plus conservé que chez les grammairiens pour expliquer forceps et fornax ... P.F.74,6, forcipes dicuntur quod his forma, i.e. calida, capiuntur ... av. garəma “chaud” qui concorde avec lat. formus ... A la même racine appartiennent sans doute lat. furnus, fornax ... L'-ur- de furnus peut reposer sur *gʷhornos ou *gʷhr̥nos.'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. forceps (KLN_1971.txt line 95706)\", \"stance\": \"supports\",\n     \"note\": \"'L., “pair of tongs, pincers”, contracted fr. *formi-caps, fr. formus, “hot”, and capere, “to catch, seize, take, hold”. See warm and captive.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. guhrnos (IEC.txt line 5564)\", \"stance\": \"supports\",\n     \"note\": \"'guhrnos “ashpit, firepit, clay oven, earthen pot, crucible”. WP I, 687 ... Lat. fornus, furnus “oven” ... OCS grŭnŭ “cauldron”; R gorn “furnace, forge, hearth”.'\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"English\", \"words\": \"furnace ; forceps\", \"verdict\": \"confirmed\",\n  \"derivation\": \"furnace is not a direct Latinism but came through French: Latin fornācem (acc. of fornāx) > Old French fornaise/fornais > Middle English forneis, fornais > furnace (Klein s.v.); the modern spelling with -u- follows Latin furnus. forceps is a straight 16th-century medical borrowing of Latin forceps, gen. forcipis, with its Latin form unaltered; the derivative forcipate is formed on the oblique stem forcip-. Nourai's arrow Latin > English is therefore right for forceps and right in substance, though one step short, for furnace.\",\n  \"derivation_fa\": \"واژهٔ furnace وام‌واژهٔ مستقیم از لاتین نیست بلکه از راه فرانسه آمده است: لاتین fornācem (رایی از fornāx) › فرانسویِ کهن fornaise/fornais › انگلیسیِ میانه forneis › furnace؛ املای امروزی با -u- از furnus لاتین پیروی می‌کند. کلاین همین را می‌گوید. اما forceps وام‌گیریِ مستقیمِ پزشکیِ سدهٔ شانزدهم از لاتین forceps (اضافیِ forcipis) است و صورتش دست‌نخورده مانده؛ صفتِ forcipate بر ستاکِ مایلِ forcip- ساخته شده است. پس پیکانِ نورایی (لاتین › انگلیسی) برای forceps کاملاً درست و برای furnace از نظر محتوا درست ولی یک حلقه (فرانسویِ کهن) کوتاه است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no citation of Nourai's own; the parent Latin box cites AHD, whose FURNACE and FORCEPS entries cover both words.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.vv. furnace and forceps (KLN_1971.txt lines 98700, 95706)\", \"stance\": \"supports\",\n     \"note\": \"'furnace, n. — ME. forneis, fornais, fr. OF. fornais (a collateral form of fornaise, whence F. fournaise), fr. L. fornācem, acc. of fornāx, “furnace, oven”, fr. fornus (also furnus), “oven”, which is rel. to L. formus and cogn. with Gk. θερμός, OE. wearm, “warm”.' / 'forceps ... contracted fr. *formi-caps.'\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. furnus (LAT.txt line ~23694)\", \"stance\": \"supports\",\n     \"note\": \"'furnus, -ī m. (fornus): four. Panroman, M.L.3603' — the pan-Romance survival that fed Old French and hence English.\"}\n  ]\n }\n]\njson.dump(nodes, open(os.path.join(OUT, \"e0_n910.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n4.py"
}
```


### [2026-09-06T15:38:16.461Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:39:31.331Z] TOOL CALL #99: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n5.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_FOUR = \"https://fr.wiktionary.org/wiki/four\"\nW_FURN = \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%86\"\n\nnodes = [\n {\n  \"id\": 11, \"lang\": \"French\", \"words\": \"four\", \"verdict\": \"plausible\",\n  \"derivation\": \"The arrow itself is textbook: Latin furnus 'bread oven' > Gallo-Romance *forn > Old French forn/fourn > modern four, with the regular French loss of preconsonantal -n and its survival in the derivatives fourneau, fournil, fournier and enfourner (Wiktionnaire: 'Du latin furnus'); the same Latin word gives Spanish horno (older forno), Portuguese and Italian forno. What is not confirmed is the box's NOTE, 'This word has possibly reached French through Arabic'. That note is taken over from Nourai's source: Pihan (Dict. étym. des mots ... dérivés de l'arabe, du persan ou du turc, s.v. FOUR) writes that Arabic فرن fourn 'paraît avoir donné naissance au latin furnus ou fornus, que les dictionnaires présentent comme racine du français four'. Modern scholarship reverses that completely: Arabic فُرْن furn is itself the loanword, taken from Aramaic pūrnā, which took it from Ancient Greek φοῦρνος, which took it from Latin furnus. So French four is an inherited Latin word with no Arabic stage at all.\",\n  \"derivation_fa\": \"خودِ پیکان کلاسیک و درست است: لاتین furnus «تنورِ نان» › گالو-رومنسِ *forn › فرانسویِ کهن forn/fourn › four امروزی، با افتادنِ منظمِ n پیش از همخوان که در مشتقات fourneau، fournil، fournier و enfourner هنوز پیداست (ویکی‌واژهٔ فرانسوی: «Du latin furnus»)؛ همین واژهٔ لاتینی در اسپانیایی horno (کهن forno)، پرتغالی و ایتالیایی forno را داده است. آنچه تأیید نمی‌شود یادداشتِ خودِ جعبه است: «شاید این واژه از راه عربی به فرانسه رسیده باشد». این یادداشت از منبعِ نورایی، یعنی پیهان، گرفته شده که در مدخل FOUR می‌نویسد عربیِ «فرن» ظاهراً منشأِ furnus لاتینی است. پژوهش امروزی این را وارونه می‌داند: «فُرن» عربی خود وام‌واژه است، از آرامیِ pūrnā، آن هم از یونانیِ φοῦρνος، و آن نیز از furnus لاتین. پس four فرانسوی واژه‌ای ارثی از لاتین است و هیچ حلقهٔ عربی در میان نیست؛ ادعای پیکان درست ولی یادداشتِ جعبه ردّ می‌شود.\",\n  \"sources\": [W_FOUR, W_FURN],\n  \"ref_check\": [\n    {\"ref\": \"PHN:187\", \"status\": \"partial\",\n     \"note\": \"Pihan's FOUR entry is on printed pp. 167-168, not 187 (PHN.txt \\\\f-leaf 198; the running heads read 'FOU 167' and '168 FOU'; printed p.187 carries GREDIN). Its text is the source of Nourai's note but states the opposite direction: 'فرن [fourn]. Mot arabe qui paraît avoir donné naissance au latin furnus ou fornus, que les dictionnaires présentent comme racine du français four. Le latin furnus n'a, je crois, rempli qu'un rôle secondaire; mais ses dérivés se retrouvent dans les langues néo-latines' — i.e. Pihan makes Arabic the donor of Latin, which modern scholarship rejects.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. furnus (LAT.txt line ~23694)\", \"stance\": \"contradicts\",\n     \"note\": \"'furnus, -ī m. (fornus): four. Panroman, M.L.3603; et celt.: irl. sorn, britt. fwrn.' Ernout-Meillet treat furnus as inherited Latin (root *gʷhor-no-) and its Romance continuants as regular; no Arabic mediation is entertained.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. furnace (KLN_1971.txt line 98700)\", \"stance\": \"contradicts\",\n     \"note\": \"'fr. OF. fornais (a collateral form of fornaise, whence F. fournaise), fr. L. fornācem ... fr. fornus (also furnus), “oven”' — the French forms are derived straight from Latin.\"},\n    {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale (DEV.txt)\", \"stance\": \"silent\",\n     \"note\": \"greps for 'four' as a headword and for 'fourn' produced no entry — Devic, unlike Pihan, does not claim four among the French words of Oriental origin.\"}\n  ]\n },\n {\n  \"id\": 12, \"lang\": \"Persian\", \"words\": \"fer «فِر ٢» ; forn «فُرن» ; fârîneh «فارینه ( فرنی ، فُرنیه )»\", \"verdict\": \"disputed\",\n  \"derivation\": \"The three words are real but they do not all come from French four, and the box's NOTE (Latin forn > old Persian > back to Europe through Arabic) is the reverse of the accepted history. (1) فِر fer 'kitchen oven' IS a modern French loan: Moʿin's entry reads «فر: ... (ف.) نوعی اجاق خوراک‌پزی که با گاز (نفت) کار کند», with the origin tag for French — this part of Nourai's arrow is right. (2) فُرن forn 'clay bread oven' is not from French but from Arabic فُرْن furn, and Arabic furn is itself a borrowing: Aramaic pūrnā < Ancient Greek φοῦρνος < Latin furnus. Persian therefore received the word from Arabic, Arabic from Aramaic/Greek, Greek from Latin — Persian is at the receiving end of the chain, never at its source. (3) فرنی / فُرنیه are the Arabic nisba forms of that same furn: Moʿin, «فرنی: [ع. ف.] (ص‌نسب. ا.) نانی که در فرن پخته باشند» ('bread baked in a furn') and «فرنیه: [ع.] نان کلیچهٔ گرد و بزرگ، ج. فرانی» — so they are Arabic derivatives of the loaned oven-word, which is compatible with the root but not with a French parent. (4) 'fârîneh' فارینه is a different word altogether: it is French farine 'flour' (Latin farīna, from far 'spelt', PIE *bʰars- 'barley, grain'), which has nothing to do with fornus; equating فارینه with فرنی/فرنیه is a folk-etymological conflation and none of the dictionaries consulted (Moʿin, Borhān, Aryanpur) has فارینه in the sense 'thick bread'. Verdict: disputed — one word (fer) is correctly placed, one (forn) has the wrong parent, one pair (فرنی/فرنیه) is Arabic-derived, and one (فارینه) belongs to another root.\",\n  \"derivation_fa\": \"این سه واژه واقعی‌اند اما همه از four فرانسوی نیامده‌اند و یادداشتِ جعبه (لاتین forn › فارسیِ کهن › بازگشت به اروپا از راه عربی) وارونهٔ تاریخِ پذیرفته‌شده است. یک: «فِر» به معنای اجاقِ خوراک‌پزی به‌راستی وام‌واژهٔ فرانسوی است؛ معین می‌نویسد «فر: ... (ف.) نوعی اجاق خوراک‌پزی که با گاز (نفت) کار کند». دو: «فُرن» از فرانسه نیست بلکه معرّبی است که فارسی از عربی گرفته، و خودِ «فُرن» عربی وام‌واژه است: از آرامیِ pūrnā، از یونانیِ φοῦρνος، از furnus لاتین. پس فارسی در پایانِ زنجیرهٔ وام‌گیری ایستاده است نه در آغازِ آن. سه: «فرنی» و «فُرنیه» صورت‌های نسبیِ عربیِ همان «فرن»اند؛ معین: «فرنی: [ع. ف.] (ص‌نسب. ا.) نانی که در فرن پخته باشند» و «فرنیه: نان کلیچهٔ گرد و بزرگ، ج. فرانی». چهار: «فارینه» یکسره واژهٔ دیگری است، همان farine فرانسوی «آرد» از farīna لاتین (از far «گندمِ اسپلت»، ریشهٔ هندواروپاییِ *bʰars-) که هیچ پیوندی با fornus ندارد؛ یکی‌گرفتنِ «فارینه» با «فرنی/فرنیه» ریشه‌شناسیِ عامیانه است و در معین، برهان قاطع و آریان‌پور «فارینه» به معنای «نانِ ستبر» یافت نشد. نتیجه: پژوهش امروزی این جعبه را رد می‌کند؛ تنها «فِر» در جای درست نشسته است.\",\n  \"sources\": [W_FURN],\n  \"ref_check\": [\n    {\"ref\": \"VOP:246\", \"status\": \"not_checked\",\n     \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi — refs_online.json records kind 'none': no scan or ebook found anywhere (re-searched 2026-09), so the page cannot be opened.\"},\n    {\"ref\": \"FVF:485,497\", \"status\": \"not_checked\",\n     \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi — only a login-walled scan on noorlib.ir/ketabnak; no local copy, page not readable.\"},\n    {\"ref\": \"MON:2527,2529\", \"status\": \"partial\",\n     \"note\": \"Moʿin (MON_part2.txt lines 5427 and 6739-6743) has «فر: ... (ف.) نوعی اجاق خوراک‌پزی که با گاز (نفت) کار کند», «فرنی: [ع. ف.] (ص‌نسب. ا.) نانی که در فرن پخته باشند» and «فرنیه: [ع.] نان کلیچهٔ گرد و بزرگ، ج. فرانی» — i.e. Moʿin supports fer as French and فرنی/فرنیه as Arabic formations on فرن, but has no entry فارینه at all and does not make Persian the source of the European word.\"},\n    {\"ref\": \"PHN:187\", \"status\": \"partial\",\n     \"note\": \"same discrepancy as node #11: the FOUR entry is at Pihan pp.167-168, and it argues Arabic > Latin, not Persian > Arabic > Europe.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Moʿin, s.vv. فر / فرنی / فرنیه (MON_part2.txt lines 5427, 6739, 6743)\", \"stance\": \"partial\",\n     \"note\": \"as quoted above; a grep of MON_part1.txt and MON_part2.txt for فارینه returns nothing.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. furnace (KLN_1971.txt line 98700) and the Wiktionary entry for Arabic فرن\", \"stance\": \"contradicts\",\n     \"note\": \"Wiktionary s.v. فرن: 'From Aramaic פורנא / ܦܘܪܢܐ (pūrnā), from Ancient Greek φοῦρνος (phoûrnos), from Latin furnus' — Arabic is the borrower; Klein likewise derives every Western form from Latin fornus/furnus with no Semitic stage.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-Alfaz al-Farisiyya al-Muʿarraba (AFM_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"greps for فرن as a headword found only الفرنسية / الفرني in unrelated lines; Addi Shir does not list فرن among the Persian words arabicised, which is what Nourai's round-trip note would require.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (incoming/PLA/PLA_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep for furn / فرن returned nothing — Asbaghi's inventory of Persian loans in Arabic does not contain it, again against the claimed Persian > Arabic direction.\"}\n  ]\n }\n]\njson.dump(nodes, open(os.path.join(OUT, \"e0_n1112.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e0_n5.py"
}
```


### [2026-09-06T15:39:33.369Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:40:13.126Z] TOOL CALL #100: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_head.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_FILUM = \"https://en.wiktionary.org/wiki/filum\"\nW_ZEH = \"https://en.wiktionary.org/wiki/%D8%B2%D9%87\"\n\nentry1 = {\n  \"entry\": 1,\n  \"root\": \"Gwhi, Guhâ, Guhei\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *gʷʰey- / *gʷʰiH- 'sinew, thread, bowstring' (Pokorny's gʷhii̯ā 481 + gʷhēi̯ə- : gʷhī- 489)\",\n  \"note\": \"Nourai's three-part root name corresponds to two adjacent Pokorny lemmas that Walde-Pokorny itself cross-links: 'gʷhii̯ā, gʷhii̯os “sinew”' (IEW 481 = WP I 694, with Skt. jyā́, Av. jyā 'bowstring', Gk. βιός) and 'gʷhēi̯ə- : gʷhī- “vein, sinew”' (IEW 489 = WP I 670, with the *gʷhī-slo- derivative Arm. ǰil, Lat. fīlum, Lith. gýsla). Watkins collapses them into one entry 'gʷhi-. Thread, tendon', and Wiktionary reconstructs Latin fīlum from *gʷʰiH-(s)lo- 'sinew', so the modern consensus is exactly Nourai's: the Avestan bowstring word and Latin fīlum belong together. 'Guhâ' and 'Guhei' are his ASCII renderings of gʷhii̯ā and gʷhēi̯ə-; the gloss 'thread, string' is a fair summary of 'sinew, bowstring, thread'. The one thing to keep in mind is that the semantic starting point is 'sinew/gut' (the material of a bowstring) rather than 'thread' in the textile sense.\",\n  \"note_fa\": \"نامِ سه‌بخشیِ ریشه نزد نورایی برابرِ دو مدخلِ همجوارِ پوکورنی است که خودِ والده–پوکورنی آنها را به هم ارجاع می‌دهد: «gʷhii̯ā, gʷhii̯os «زه، پی»» (ایو ۴۸۱ = WP I 694، با سنسکریت jyā́، اوستایی jyā «زهِ کمان» و یونانی βιός) و «gʷhēi̯ə- : gʷhī- «رگ، پی»» (ایو ۴۸۹ = WP I 670، با مشتقِ *gʷhī-slo- یعنی ارمنی ǰil، لاتین fīlum و لیتوانیایی gýsla). واتکینز این دو را در یک مدخل «gʷhi- «نخ، پی»» یکی کرده و ویکی‌واژه fīlum لاتین را از *gʷʰiH-(s)lo- «پی» می‌گیرد؛ پس اجماعِ امروزی همان است که نورایی می‌گوید: واژهٔ اوستاییِ زهِ کمان و fīlum لاتین به یک ریشه بازمی‌گردند. «Guhâ» و «Guhei» صورت‌های لاتین‌نویسِ او برای gʷhii̯ā و gʷhēi̯ə- است و معنای «نخ، ریسمان» تقریبِ درستی از «پی، زه، نخ» است؛ تنها باید توجه داشت که نقطهٔ آغازِ معنایی «پی/روده» (مادّهٔ زهِ کمان) است نه «نخِ» بافندگی. ادعای نورایی درست است.\",\n  \"sources\": [W_FILUM],\n  \"ref_check\": [\n    {\"ref\": \"POK:481\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt, 'Root / lemma: gʷhiā, gʷhii̯os  Meaning: sinew ... Page(s): 481': 'Old Indic jyā “sinew, tendon, string esp. of the bow”, Avestan jyā “bowstring (in compounds also sinew of flesh)”; gr. βιός m. “bowstring” ... about Lithuanian gija “filament”, Old Church Slavic ži-ca “sinew” etc. see below gʷhei-. References: WP. I 670, 694.'\"},\n    {\"ref\": \"POK:489\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt, 'Root / lemma: gʷhēi̯ə- : gʷhī-  Meaning: vein, sinew ... Page(s): 489': 'gʷhīslo-. Armenian ǰil “sinew, cord”; Latin fīlum “filament”; Lithuanian gýsla “vein, sinew, midrib”, Latvian dzīsla ... References: WP. I 670, 694.'\"},\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 548): 'gʷhi-. Thread, tendon. Suffixed form *gʷhi-slo- in Latin filum, thread: FILAMENT, FILAR, FILARIA, FILE¹, FILLET, FILOSE, FILUM; DEFILE, ENFILADE, FILIFORM, FILIGREE, FILOPLUME, PROFILE, PURFLE. [Pok. gʷhei̯ə- 489.]'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 670 and 694 (WLD_Bd1_pages.txt lines 63486 and 65742)\", \"stance\": \"supports\",\n     \"note\": \"I 670: 'gʷhēi- „Ader, Sehne, Band“ ... gʷhi-slo-: Arm. ǰil „Sehne, Schnur“, lat. fīlum „Faden“; lit. gýsla „Ader, Sehne“'; I 694: 'gʷhii̯ā, gʷhii̯os „Sehne, bes. Bogensehne“. Ai. jyā ..., av. jyā „Bogensehne“, gr. βιός ... vielleicht auch lat. fīlum usw. ... S. auch oben S. 670!' — Walde-Pokorny expressly ties the two lemmas together, which is what Nourai's compound root name does.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. guhislā (IEC.txt line 5498)\", \"stance\": \"supports\",\n     \"note\": \"'guhislā “sinew, gut, vein”. WP I, 670. Vedic hirā “vein”; Arm. ǰil, a-st. beside ǰiy “nerve, sinew”; Lat. filum “yarn”; OCS žila “vein”; Li. gysla; Latv. dzīsla “sinew, vein”.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 6.38 THREAD (SYN.txt line 10304)\", \"stance\": \"supports\",\n     \"note\": \"'3. Lat. filum (> Romance words) : Lith. gysla, Lett. dzīsla, OPruss. -gislo, ChSl. žila “vein”, etc. Walde-P. 1.670.'\"}\n  ],\n  \"nodes\": []\n}\njson.dump(entry1, open(os.path.join(OUT, \"e1.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_head.py"
}
```


### [2026-09-06T15:40:14.895Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:41:14.713Z] TOOL CALL #101: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_n1.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_ZEH = \"https://en.wiktionary.org/wiki/%D8%B2%D9%87\"\n\nnodes = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"žyâ 2\", \"verdict\": \"confirmed\",\n  \"derivation\": \"The Avestan word for 'bowstring' is a feminine ā-stem from *gʷʰih₂-, the same formation as Sanskrit jyā́ 'bowstring, sinew' and Greek βιός 'bowstring'; the PIE labiovelar *gʷʰ before *i gives Indo-Iranian palatal *ǰ. It occurs e.g. in Yašt 10.130 'yat̰ ... jyā nāuuaii̯an tigrā̊ŋhō' (of the bowstring twanging and the arrows). The chart's spelling 'žyâ' is not an error: the Avestan manuscripts write the palatal before -ii̯- with the letter 𐬲, and Wiktionary accordingly cites the form as žiiā 'bow-string, tendon', while Bartholomae, Horn and Pokorny normalise it as jyā-. Nourai's '2' is the homonym number that separates it from jyā- 'to oppress, deprive'. The gloss 'bow string' is Pokorny's own, who adds that in compounds it also means the sinew of the flesh.\",\n  \"derivation_fa\": \"واژهٔ اوستاییِ «زهِ کمان» اسمِ مؤنثِ ā-ستاک از *gʷʰih₂- است، هم‌ساختِ سنسکریت jyā́ «زه، پی» و یونانی βιός «زهِ کمان»؛ لبی‌کامیِ دمیدهٔ *gʷʰ پیش از i در هندوایرانی به کام‌سایِ *ǰ بدل شده است. این واژه برای نمونه در مهریشت (یشت ۱۰٫۱۳۰) در وصفِ زه و تیرها آمده است. املای «žyâ» در نمودار خطا نیست: دست‌نویس‌های اوستایی این همخوانِ کامی را پیش از -ii̯- با حرفِ 𐬲 می‌نویسند و ویکی‌واژه نیز صورت را žiiā «زهِ کمان، پی» ضبط کرده است، حال آنکه بارتولمه، هرن و پوکورنی آن را به jyā- هنجارین می‌کنند. عددِ «۲» نزد نورایی شمارهٔ هم‌آواست که این واژه را از jyā- «ستم کردن» جدا می‌کند. معنایی که آورده همان معنای پوکورنی است. ادعای نورایی درست است.\",\n  \"sources\": [W_ZEH],\n  \"ref_check\": [\n    {\"ref\": \"POK:481\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt s.v. gʷhiā, gʷhii̯os (Page(s): 481): 'Old Indic jyā “sinew, tendon, string esp. of the bow”, Avestan jyā “bowstring (in compounds also sinew of flesh)”; gr. βιός m. “bowstring”.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 694 (WLD_Bd1_pages.txt line 65745)\", \"stance\": \"supports\",\n     \"note\": \"'Ai. jyā „Sehne, bes. des Bogens“, av. jyā „Bogensehne (in Zs. auch Sehne des Fleisches)“, gr. βιός „Bogensehne“.'\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 677, p.150 (HRN.txt \\\\f-leaf 172)\", \"stance\": \"supports\",\n     \"note\": \"'aw. jyā “Bogensehne; Sehne” (yt. 10, 70, Geldner, KZ. 30, 514); ai. jyā-.'\"},\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch (BRT.txt line 11582)\", \"stance\": \"partial\",\n     \"note\": \"the OCR is largely unusable, but the surviving cross-reference 'Zum 1. jyā- (aus der volleren Form; s. dazu ...)' shows Bartholomae's headword is spelt jyā-, i.e. with j not ž — a normalisation difference, not a different word.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.229 (HUB.txt line 8169)\", \"stance\": \"supports\",\n     \"note\": \"'zih “Bogensehne” = zd. skr. jyā-' — Hübschmann's Avestan citation form again with j-.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"zeh 1 «زه ١»\", \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian زه zeh/zih 'bowstring' continues Middle Persian zih ⟨zyh⟩ (MacKenzie p.100: 'zih [zyh | N zih] bow-string'), from Old Iranian *ǰiyā-/*ǰiyaka-. The sound law is the ordinary South-West Iranian one: Old Iranian palatal *ǰ (the Avestan j of jyā-) yields Middle and New Persian z — Hübschmann sets it out with the parallel series 'zadan “schlagen” = zd. ap. jan-, zan “Weib” = jani-, zih “Bogensehne” = jyā-, zīstan “leben” = jīv-'. Horn adds that the Persian word presupposes a suffixed *jiyaka- ('Urform von zih ist *jiyaka-'), whose -ka- gives the MP -h; the Kāšān dialect forms zeh, ze that he records are the same word. Moʿin's footnote in Borhān-e Qāṭeʿ gives the same comparison (Avestan jyā, Sanskrit jyā-, Kurdish zih-kamān).\",\n  \"derivation_fa\": \"«زه» فارسی نو دنبالهٔ zih فارسی میانه است (مکنزی، ص ۱۰۰: «zih [zyh | N zih] bow-string») و آن از ایرانی باستانِ *ǰiyā-/*ǰiyaka- می‌آید. قانونِ آواییِ آن همان قاعدهٔ همیشگیِ ایرانیِ جنوب‌باختری است: *ǰ کامیِ ایرانی باستان (همان j اوستاییِ jyā-) در فارسی میانه و نو «ز» می‌شود؛ هوبشمان این را با زنجیرهٔ نمونه‌ها نشان می‌دهد: «زدن = اوستایی/پارسی باستان jan-؛ زن = jani-؛ زه = jyā-؛ زیستن = jīv-». هرن می‌افزاید که صورتِ فارسی بر *jiyaka- استوار است که -ka- آن در فارسی میانه به h بدل شده، و گونه‌های کاشانیِ zeh و ze را نیز همان واژه می‌داند. حاشیهٔ معین بر برهان قاطع نیز همین مقایسه را می‌آورد (اوستا jyā، هندی باستان jyā-، کردی zih-kamān). ادعای نورایی درست است.\",\n  \"sources\": [W_ZEH],\n  \"ref_check\": [\n    {\"ref\": \"HRN:150\", \"status\": \"supports\",\n     \"note\": \"Horn, Grundriss no. 677, p.150: '677. zih “Bogensehne”. Kāš. zeh, ze. aw. jyā “Bogensehne; Sehne” ...; ai. jyā-. kurd. zih “Bogensehne”; afγ. zaγ, bel. jiy (177). Urform von zih ist *jiyaka-.'\"},\n    {\"ref\": \"BQT:1046\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qateʿ, the زه entry with Moʿin's footnote 7, found in BQT_v2_pages.txt \\\\f-block 508 (the بیان هفدهم section «در زای نقطه‌دار با ها»; the block sequence puts it at printed p. ≈1046, Nourai's page). The entry glosses زه as «چلهٔ کمان ... وتر» and footnote 7 reads «اوستا [jyā] وتر کمان ...؛ هندی باستان [jyā]-؛ کردی zih-kamān (زه کمان)؛ افغانی ...؛ بلوچی ...» — exactly the comparison Nourai's arrow asserts.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.100 (PHD.txt line 680)\", \"stance\": \"supports\",\n     \"note\": \"'zih [zyh | N zih] bow-string.' — the Middle Persian stage the chart skips.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.229 (HUB.txt line 8169)\", \"stance\": \"supports\",\n     \"note\": \"'b) [aw. j] = np. z: zadan “schlagen” = zd. ap. jan, skr. han; zan “Weib” = gd. jāni-; zih “Bogensehne” = zd. skr. jyā-; zīstan “leben”, zd. skr. jīv-.'\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II glossary (NYB_vol2_glossary.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep for zih returned nothing — the word does not occur in the texts Nyberg glosses.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt, ARY_latin_index_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"greps for زه as a headword and for JYA in the Latin index found only the unrelated پند/PANTHĀ entry; Aryanpur has no article on زه.\"}\n  ]\n }\n]\njson.dump(nodes, open(os.path.join(OUT, \"e1_n12.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_n1.py"
}
```


### [2026-09-06T15:41:17.222Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:42:11.417Z] TOOL CALL #102: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_n2.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_FILUM = \"https://en.wiktionary.org/wiki/filum\"\n\nnodes = [\n {\n  \"id\": 3, \"lang\": \"Latin\", \"words\": \"filum\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Latin fīlum 'thread' goes back to *gʷʰiH-(s)lo- (Proto-Italic *fī(s)lom), an instrument noun in *-slo- from the same 'sinew' root as the Avestan bowstring word; the initial *gʷʰ regularly gives Latin f-, and the -sl- cluster is simplified with compensatory lengthening, giving fī-lum. The cognates that guarantee the reconstruction are Armenian ǰil 'sinew, cord' (whose ǰ presupposes an aspirate, as Ernout-Meillet note), Lithuanian gýsla 'vein, sinew' and Old Church Slavonic žila 'vein'. Semantically Latin moved from 'sinew, gut' to 'thread, string' and then to 'outline, contour' (Nonius 313,16 oris lineamentum), which is what makes the Italian profilare of node #7 possible.\",\n  \"derivation_fa\": \"لاتین fīlum «نخ» به *gʷʰiH-(s)lo- بازمی‌گردد (ایتالیکِ آغازین *fī(s)lom)، اسمِ ابزار با پسوندِ *-slo- از همان ریشهٔ «پی» که واژهٔ اوستاییِ زهِ کمان از آن است؛ *gʷʰ آغازین در لاتین به‌قاعده f- می‌دهد و خوشهٔ -sl- با کشیدگیِ جبرانیِ واکه ساده می‌شود و fī-lum به دست می‌آید. هم‌ریشه‌هایی که این بازسازی را تضمین می‌کنند عبارت‌اند از ارمنی ǰil «پی، ریسمان» (که ǰ آن، به گفتهٔ ارنو و مه‌یه، وجودِ همخوانِ دمیده را ایجاب می‌کند)، لیتوانیایی gýsla «رگ، پی» و اسلاویِ کهنِ کلیسایی žila «رگ». از نظر معنایی لاتین از «پی/روده» به «نخ، ریسمان» و سپس به «خط، طرح» رسیده است (نونیوس ۳۱۳٫۱۶ oris lineamentum) و همین تحولِ معنایی است که ساختِ profilare ایتالیایی در گرهِ ۷ را ممکن می‌کند. ادعای نورایی درست است.\",\n  \"sources\": [W_FILUM],\n  \"ref_check\": [\n    {\"ref\": \"POK:489\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt s.v. gʷhēi̯ə- : gʷhī- (Page(s): 489): 'gʷhīslo-. Armenian ǰil “sinew, cord”; Latin fīlum “filament”; Lithuanian gýsla “vein, sinew”, Latvian dzīsla “vein”; Old Prussian pettegislo “Rückenader”.'\"},\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 (line 548): 'gʷhi-. Thread, tendon. Suffixed form *gʷhi-slo- in Latin filum, thread. [Pok. gʷhei̯ə- 489.]'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. filum (LAT.txt lines 22414-22431)\", \"stance\": \"supports\",\n     \"note\": \"'filum, -ī n.: fil ... Le rapprochement avec lit. gýsla (žemaite ginsla), v.pruss. -gislo, v.sl. žila “veine, tendon” et avec arm. ǰil “tendon” est séduisant; le ǰ arménien suppose une aspirée comme lat.' They add that the sense 'forme' may belong with fingō, i.e. two homonyms — a caveat that does not touch the 'thread' sense used here.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. file 'a collection of papers' (KLN_1971.txt line 92791)\", \"stance\": \"supports\",\n     \"note\": \"'L. filum stands for I.-E. base *gʷhis-lom and is cogn. with Arm. ǰil, “sinew, string, line”, Lith. gysla, “vein, sinew”, Lett. dzīsla, OPruss. pette-gislo, OSlav. žila, “vein”. L. funis “rope” is not cognate.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. guhislā (IEC.txt line 5498)\", \"stance\": \"supports\",\n     \"note\": \"'Lat. filum “yarn” beside hila, hilla' under gʷhislā 'sinew, gut, vein', WP I, 670.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 6.38 THREAD (SYN.txt line 10304)\", \"stance\": \"supports\",\n     \"note\": \"'Lat. filum (> Romance words) : Lith. gysla, Lett. dzīsla, OPruss. -gislo, ChSl. žila “vein”. Walde-P. 1.670. Ernout-M. 360.'\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"French\", \"words\": \"fil ; filet\", \"verdict\": \"confirmed\",\n  \"derivation\": \"French fil 'thread' is the direct phonetic continuation of Latin fīlum (Old French fil, with loss of the neuter ending and of final -um), and filet is its diminutive in -et. The butcher's filet is a specialisation of 'little thread, little band': the long narrow strip of tenderloin taken from along the backbone, named from its ribbon shape; the sense is attested in French cookery from the 17th century and reached English as fillet/filet. Klein: 'fillet, n. — F. filet, dimin. of fil, “thread”, fr. L. filum'. Nourai's gloss for fil, 'thread (used to tie papers)', is a slightly odd paraphrase — it is the ordinary French word for thread — but it points at the same word that gives English file.\",\n  \"derivation_fa\": \"«fil» فرانسوی دنبالهٔ آواییِ مستقیمِ fīlum لاتین است (فرانسویِ کهن fil، با افتادنِ پایانهٔ خنثای -um) و «filet» صورتِ تصغیرِ آن با پسوندِ -et است. «فیلهٔ» قصابی تخصیصِ معناییِ «نخِ کوچک، نوارِ باریک» است: نوارِ دراز و باریکِ گوشتِ کنارِ ستونِ فقرات که از شکلِ نواری‌اش چنین نامیده شده؛ این معنا از سدهٔ هفدهم در آشپزیِ فرانسه گواهی شده و از همان‌جا به انگلیسی (fillet/filet) رفته است. کلاین می‌نویسد: «fillet — از filet فرانسوی، مصغّرِ fil «نخ»، از filum لاتین». معنایی که نورایی برای fil آورده («نخی که با آن کاغذها را می‌بندند») کمی نامتعارف است — fil واژهٔ عادیِ «نخ» در فرانسه است — ولی به همان واژه‌ای اشاره دارد که file انگلیسی از آن آمده. ادعای نورایی درست است.\",\n  \"sources\": [W_FILUM],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. gʷhi- lists FILE¹ and FILLET among the English words from Latin filum, i.e. exactly the French fil / filet chain.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.vv. fillet and file (KLN_1971.txt lines 92941, 92791)\", \"stance\": \"supports\",\n     \"note\": \"'fillet, n. — F. filet, dimin. of fil, “thread”, fr. L. filum'; 'file ... fr. F. file, “row”, fr. filer, “to spin”, fr. Late L. filare ... fr. L. filum, “thread”, in some fr. F. fil, “thread” (fr. L. filum).'\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. filum (LAT.txt line 22422)\", \"stance\": \"supports\",\n     \"note\": \"'Panroman, M.L.3306' with the derivative 'filo, -ās, substitut populaire et tardif de nēre ... qu'il a remplacé dans les langues romanes, M.L.3393' — the Romance continuation that yields French fil/filer.\"}\n  ]\n }\n]\njson.dump(nodes, open(os.path.join(OUT, \"e1_n34.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_n2.py"
}
```


### [2026-09-06T15:42:13.449Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:43:09.607Z] TOOL CALL #103: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_n3.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_PROF = \"https://www.etymonline.com/word/profile\"\nA_PROF = \"https://abadis.ir/fatofa/%D9%BE%D8%B1%D9%88%D9%81%DB%8C%D9%84/\"\n\nnodes = [\n {\n  \"id\": 5, \"lang\": \"Persian\", \"words\": \"fîleh «فیله»\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian فیله fīle 'fillet (of meat)' is a modern loan from French filet, taken over through the cuisine vocabulary of the late Qajar / Pahlavi period; the French final -t is not pronounced, so Persian took the spoken form [filɛ] and wrote it فیله with a final ـه for the [e]. Moʿin's entry defines it purely by its butchery sense — «فیله: گوشتی لطیف و لغزان که در حیوان قرار دارد و از آن مخصوصاً برای کباب استفاده کنند» — and prints the Latin-script source form in the customary bracket. The word is not related to Persian پیله or فیل; it is the French diminutive of fil, hence ultimately Latin fīlum.\",\n  \"derivation_fa\": \"«فیله» در فارسی وام‌واژه‌ای نو از filet فرانسوی است که از راه واژگانِ آشپزیِ اواخر قاجار و دورهٔ پهلوی وارد شده است؛ چون t پایانیِ فرانسوی تلفظ نمی‌شود، فارسی صورتِ گفتاریِ [filɛ] را گرفته و آن را با «ـه» پایانی نوشته است. معین آن را تنها با معنای قصابی تعریف می‌کند: «فیله: گوشتی لطیف و لغزان که در حیوان قرار دارد و از آن مخصوصاً برای کباب استفاده کنند» و صورتِ لاتینِ مأخذ را در قلابِ معمولِ خود می‌آورد. این واژه ربطی به «پیله» یا «فیل» فارسی ندارد و مصغّرِ فرانسویِ fil، یعنی در نهایت از fīlum لاتین است. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"MON:2599\", \"status\": \"supports\",\n     \"note\": \"Moʿin, s.v. فیله (MON_part2.txt line 9679): «فیله: (-)... (اِ.) گوشتی لطیف و لغزان که در حیوان قرار دارد و از آن مخصوصاً برای کباب استفاده کنند» — the entry carries the Latin-script European source form in its bracket (OCR-garbled) and no Persian/Arabic etymon, i.e. Moʿin treats it as the European loan Nourai says it is.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Moʿin s.v. فیله (MON_part2.txt line 9679)\", \"stance\": \"supports\", \"note\": \"as quoted; the neighbouring entries فیلم، فینال are likewise French loans, confirming the section's loan character.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. fillet (KLN_1971.txt line 92941)\", \"stance\": \"supports\",\n     \"note\": \"'F. filet, dimin. of fil, “thread”, fr. L. filum' — establishes the French word that Persian borrowed.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep for فیله returned nothing; Aryanpur treats only inherited Indo-European vocabulary of Persian, not modern French loans.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"English\", \"words\": \"file, filament, filet\", \"verdict\": \"confirmed\",\n  \"derivation\": \"All three reach English through French from Latin fīlum. file (the collection of papers, and the row) is from French file 'row' / filer 'to spin' < Late Latin fīlāre < fīlum — the office sense comes from the practice of stringing documents on a thread or wire. filament is French filament, from Modern Latin fīlāmentum, on Late Latin fīlāre. filet is the unassimilated 19th-century re-borrowing of French filet beside the older, anglicised fillet. Note that English file 'steel tool' (Old English fēol) is a different, Germanic word and does not belong here — Nourai's box contains only the fīlum-words.\",\n  \"derivation_fa\": \"هر سه واژه از راه فرانسه و از fīlum لاتین به انگلیسی رسیده‌اند. «file» (هم به معنای پروندهٔ کاغذها و هم به معنای صف) از file فرانسوی «ردیف» و filer «رشتن» از fīlāre لاتینِ متأخر است؛ معنای اداری از رسمِ به‌نخ‌کشیدنِ اسناد پدید آمده. «filament» از filament فرانسوی و آن از fīlāmentum لاتینِ نو بر پایهٔ fīlāre است. «filet» وام‌گیریِ دوبارهٔ سدهٔ نوزدهم از filet فرانسوی است در کنارِ صورتِ کهن‌ترِ انگلیسی‌شدهٔ fillet. باید توجه داشت که file انگلیسی به معنای «سوهان» (انگلیسیِ کهن fēol) واژه‌ای ژرمنی و جداست و به این خانواده تعلق ندارد؛ جعبهٔ نورایی تنها واژه‌های خانوادهٔ fīlum را دارد. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. gʷhi-: 'FILAMENT, FILAR, FILARIA, FILE¹, FILLET, FILOSE, FILUM; DEFILE², ENFILADE, FILIFORM, FILIGREE, FILOPLUME, PROFILE, PURFLE' — file, filament and fillet/filet are all listed.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.vv. file, filament, fillet (KLN_1971.txt lines 92791, 92762, 92941)\", \"stance\": \"supports\",\n     \"note\": \"'filament, n., a fine thread, fiber. — F., fr. ModL. filamentum, fr. Late L. filare, “to spin”. See file, “collection of papers”'; 'file ... fr. F. file, “row”, fr. filer ... fr. L. filum'; 'fillet — F. filet, dimin. of fil'. Klein also flags the homonym 'file, n., a tool of steel. — ME. file, fr. OE. feol' as unrelated.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt)\", \"stance\": \"supports\",\n     \"note\": \"Skeat likewise derives 'file (1)' (a string, row) from F. fil, L. filum, and keeps 'file (2)' the tool separate as Old English fēol.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Italian\", \"words\": \"pro-filare\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Italian profilare 'to draw in outline' is pro- 'forward, along' + filare 'to spin, draw out a line' (Late Latin fīlāre, from fīlum 'thread'), the verbal noun being profilo 'a drawing in outline'; the metaphor is that of drawing a line along the edge of a shape. The word belongs to the vocabulary of Renaissance painting and was carried out of Italian into French, English and, in its technical 'constant cross-section' sense, into the language of engineering. Nourai's hyphenation 'pro-filare' marks the prefix and is not an Italian spelling.\",\n  \"derivation_fa\": \"«profilare» ایتالیایی «طرحِ بیرونیِ چیزی را کشیدن» از pro- «به‌سوی، در امتداد» و filare «رشتن، خط کشیدن» (لاتینِ متأخر fīlāre از fīlum «نخ») ساخته شده و اسمِ آن profilo «طرحِ نمای بیرونی» است؛ استعارهٔ آن کشیدنِ خطی در امتدادِ لبهٔ یک شکل است. این واژه به واژگانِ نقاشیِ رنسانس تعلق دارد و از ایتالیایی به فرانسه و انگلیسی رفته و در معنای فنیِ «مقطعِ ثابت» واردِ زبانِ مهندسی شده است. خط تیرهٔ نورایی در «pro-filare» نشانهٔ پیشوند است نه املای ایتالیایی. ادعای نورایی درست است.\",\n  \"sources\": [W_PROF],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. gʷhi- lists PROFILE among the English descendants of Latin filum.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. profile (KLN_1971.txt line 192209)\", \"stance\": \"supports\",\n     \"note\": \"'It. profilo, proffilo, “drawing in outline”, fr. profilare, proffilare, “to draw in outline”, fr. pro- (fr. L. pro, “before, for”), and filo, “thread, line” (fr. L. filum).'\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. filum (LAT.txt line 22424)\", \"stance\": \"supports\",\n     \"note\": \"'filo, -ās, substitut populaire et tardif de nēre ... qu'il a remplacé dans les langues romanes, M.L.3393' — Late Latin fīlāre, the base of Italian filare/profilare.\"}\n  ]\n }\n]\njson.dump(nodes, open(os.path.join(OUT, \"e1_n567.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_n3.py"
}
```


### [2026-09-06T15:43:12.035Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:44:01.309Z] TOOL CALL #104: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_n4.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nOUT = \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216\"\nW_PROF = \"https://www.etymonline.com/word/profile\"\nA_PROF = \"https://abadis.ir/fatofa/%D9%BE%D8%B1%D9%88%D9%81%DB%8C%D9%84/\"\n\nnodes = [\n {\n  \"id\": 8, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"An empty pass-through box for French profil, borrowed from Italian profilo in the 16th century as a term of drawing and architecture ('a side view, an outline'), later extended in engineering to profilé 'a rolled metal section of constant cross-section'. French is the right intermediary for the Persian word in node #9: Persian technical vocabulary of this kind was taken from French, and Moʿin tags پروفیل [فر.].\",\n  \"derivation_fa\": \"این جعبهٔ تهی نمایندهٔ «profil» فرانسوی است که در سدهٔ شانزدهم از profilo ایتالیایی به‌عنوان اصطلاحِ نقاشی و معماری («نمای نیم‌رخ، طرحِ بیرونی») وام گرفته شد و سپس در مهندسی به profilé «مقطعِ فلزیِ نوردشدهٔ با مقطعِ ثابت» گسترش یافت. برای واژهٔ فارسیِ گرهِ ۹ همین فرانسه واسطهٔ درست است، زیرا واژگانِ فنیِ از این دست در فارسی از فرانسه گرفته شده و معین نیز «پروفیل» را با برچسبِ [فر.] می‌آورد. ادعای نورایی درست است.\",\n  \"sources\": [A_PROF],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no citation of Nourai's own.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. profile (KLN_1971.txt line 192209)\", \"stance\": \"partial\",\n     \"note\": \"Klein derives English profile directly from Italian profilo and does not mention French; the French form profil is nonetheless the attested 16th-c. Italianism and the demonstrable source of the Persian word.\"},\n    {\"src\": \"MON\", \"where\": \"Moʿin s.v. پروفیل (abadis.ir mirror)\", \"stance\": \"supports\",\n     \"note\": \"«(پُ رُ) [فر.] (اِ.) ۱- نقشه و تصویری که مقطع طولی ساختمان یا سازه را نشان دهد» — the tag [فر.] names French as the donor.\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"Persian\", \"words\": \"profîl «پروفیل»\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian پروفیل profīl is a 20th-century French loan, with two senses that both come from French: the drawing sense ('a section, a side view'), which Moʿin defines as «نقشه و تصویری که مقطع طولی ساختمان یا سازه را نشان دهد», and the industrial sense Nourai glosses, 'shaped hollow metal extrusions' — French profilé, the rolled or extruded steel sections of constant cross-section used in building. Persian took the French form with p- (there is no Persian phoneme problem here) and the stress-final -īl. The chain is therefore Latin fīlum > Late Latin fīlāre > Italian profilare/profilo > French profil > Persian پروفیل, exactly as drawn.\",\n  \"derivation_fa\": \"«پروفیل» در فارسی وام‌واژهٔ فرانسویِ سدهٔ بیستم است و هر دو معنای آن از فرانسه آمده است: معنای ترسیمی («مقطع، نمای نیم‌رخ») که معین چنین تعریفش می‌کند: «نقشه و تصویری که مقطع طولی ساختمان یا سازه را نشان دهد»، و معنای صنعتی که نورایی آورده، یعنی مقاطعِ فولادیِ نوردشده یا اکسترودشده با مقطعِ ثابت که در ساختمان به کار می‌رود (فرانسوی profilé). فارسی صورتِ فرانسوی را با p- و تکیهٔ پایانیِ -īl گرفته است. پس زنجیره چنین است: fīlum لاتین › fīlāre لاتینِ متأخر › profilare/profilo ایتالیایی › profil فرانسوی › «پروفیل» فارسی، درست همان‌گونه که در نمودار کشیده شده است.\",\n  \"sources\": [A_PROF],\n  \"ref_check\": [\n    {\"ref\": \"VOP:117\", \"status\": \"not_checked\",\n     \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi — refs_online.json records kind 'none' (no scan, no ebook found), so the cited page cannot be opened. The claim was checked against Moʿin instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Moʿin s.v. پروفیل (abadis.ir mirror; not present in the local MON_part1/2 OCR)\", \"stance\": \"supports\",\n     \"note\": \"«(پُ رُ) [فر.] (اِ.) ۱- نقشه و تصویری که مقطع طولی ساختمان یا سازه را نشان دهد»; the general article adds the engineering sense «مقطع ثابت و طول بسیار» used of steel sections — Nourai's gloss.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep for پروفیل returned nothing — outside the scope of a dictionary of inherited Indo-European roots in Persian.\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"English\", \"words\": \"profile\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English profile is borrowed from older Italian profilo 'a drawing in outline' (Klein), first attested in the 1650s as 'a drawing of the outline of anything', especially the human face seen from the side; 'a side view' follows in the 1660s and the figurative 'biographical sketch, character study' in 1734, whence the modern 'user profile'. The word is thus a Renaissance art term that entered English from Italian rather than through French, which is why Nourai draws it straight from the Italian box.\",\n  \"derivation_fa\": \"«profile» انگلیسی از profilo ایتالیاییِ کهن «طرحِ نمای بیرونی» وام گرفته شده (کلاین) و نخستین گواهیِ آن در دههٔ ۱۶۵۰ به معنای «کشیدنِ خطِ بیرونیِ هر چیز» به‌ویژه چهرهٔ آدمی از نیم‌رخ است؛ معنای «نمای جانبی» در دههٔ ۱۶۶۰ و معنای مجازیِ «شرح‌حالِ کوتاه، تصویرِ شخصیت» در ۱۷۳۴ پدید آمده که «پروفایلِ کاربر» امروزی از همان است. پس این واژه اصطلاحی هنری از دورهٔ رنسانس است که از ایتالیایی به انگلیسی رفته، نه از راه فرانسه، و به همین سبب نورایی پیکان را مستقیم از جعبهٔ ایتالیایی کشیده است. ادعای نورایی درست است.\",\n  \"sources\": [W_PROF],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. gʷhi- lists PROFILE among the descendants of Latin filum.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. profile (KLN_1971.txt line 192209)\", \"stance\": \"supports\",\n     \"note\": \"'profile, n., side view. — It. profilo, proffilo, “drawing in outline”, fr. profilare ... fr. pro- and filo, “thread, line” (fr. L. filum). See 1st pro- and file, “collection of papers”, and cp. purfle.'\"},\n    {\"src\": \"WEB\", \"where\": \"Etymonline, s.v. profile (archived)\", \"stance\": \"supports\",\n     \"note\": \"'from older Italian profilo “a drawing in outline,” from profilare “to draw in outline” ... from Late Latin filare “to spin, draw out a line,” from filum “thread”'; senses 1650s 'drawing of the outline', 1660s 'a side view', 1734 'biographical sketch'.\"}\n  ]\n }\n]\njson.dump(nodes, open(os.path.join(OUT, \"e1_n8910.json\"), \"w\", encoding=\"utf-8\"), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216/e1_n4.py"
}
```


### [2026-09-06T15:44:03.350Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:44:05.278Z] AGENT

Now assembling the final file.


## [2026-09-06T15:44:10.267Z] TOOL CALL #105: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p216 && python3 - <<'PYEOF'\nimport json\nL = lambda f: json.load(open(f, encoding=\"utf-8\"))\ne0 = L(\"e0.json\")\ne0[\"nodes\"] = L(\"e0_n12.json\") + L(\"e0_n34.json\") + L(\"e0_n5678.json\") + L(\"e0_n910.json\") + L(\"e0_n1112.json\")\ne1 = L(\"e1.json\")\ne1[\"nodes\"] = L(\"e1_n12.json\") + L(\"e1_n34.json\") + L(\"e1_n567.json\") + L(\"e1_n8910.json\")\nout = {\n  \"pdf_page\": 216,\n  \"book_page\": 186,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [e0, e1],\n}\nassert [n[\"id\"] for n in e0[\"nodes\"]] == list(range(1,13)), [n[\"id\"] for n in e0[\"nodes\"]]\nassert [n[\"id\"] for n in e1[\"nodes\"]] == list(range(1,11)), [n[\"id\"] for n in e1[\"nodes\"]]\njson.dump(out, open(\"/home/sfmqrb/git/rishe/data/verification/page-216.json\",\"w\",encoding=\"utf-8\"),\n          ensure_ascii=False, indent=2)\nprint(\"written\")\nPYEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-216.json > /dev/null && echo \"valid JSON\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 216"
}
```


### [2026-09-06T15:44:12.450Z] TOOL RESULT

```
written
valid JSON
nodes verified: 22/22
node verdicts: {'confirmed': 19, 'plausible': 2, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 19, 'not_checked': 6, 'not_found': 1, 'partial': 3}
books consulted: {'supports': 47, 'silent': 9, 'partial': 4, 'contradicts': 3} | by book: {'KLN': 14, 'IEC': 6, 'MON': 6, 'LAT': 6, 'ARY': 5, 'HUB': 4, 'NYB': 3, 'SKT': 3, 'BRT': 2, 'SYN': 2, 'PHD': 2, 'POK': 2, 'KNT': 1, 'SOD': 1, 'DEV': 1, 'AFM': 1, 'PLA': 1, 'WLD': 1, 'HRN': 1, 'WEB': 1}
```


## [2026-09-06T15:44:19.169Z] TOOL CALL #106: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"File (1).\\{0,260\\}\\|File (2).\\{0,200\\}\\|Filament.\\{0,200\\}\" SKT.txt | head -5"
}
```


### [2026-09-06T15:44:21.648Z] TOOL RESULT

```
6576:Filament;  see  File  (i). Filbert,  fruit  of  hattl.   (F.-O.  H.  G.) Formerly  phiiibtrd  (Goweri ;    »hort    for Pkitibird  or  Pkiiibert  nut,  from  the  proper name  Pkiiibert ;  (S.  Philibcrt's  d
```


## [2026-09-06T15:44:24.622Z] TOOL CALL #107: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"File (i).\\{0,300\\}\" SKT.txt | head -3; echo ---; grep -on \"a  string.\\{0,200\\}\" SKT.txt | head -3"
}
```


### [2026-09-06T15:44:26.804Z] TOOL RESULT

```
---
8340:a  string, G.  Atnkil,  a  handle,  ear  of  a  vessel.  The orig.  sense  seems  to  have  been  'a  loop*  to hang  up  by.     From  the  verb  above.
10467:a  string  made  of  Aax, being  fern,  of  adj.  liruuj,  made  of  tlax.* L.  limtm,  flax.  Cf.  Gk.  Kivw,  Aax.  Der. out  dine.
15031:a  stringed  instniment.  (F.<* L.-Gk.i  O.V.psalterie  (iJth  ccnt)*L. psalterium,  —  Gk.  (pa\T^>M(M'.  a  kind  of  harp. —  Gk.  ^aAr^p.  a  harper.  —  Gk.  i^\.-\tiv,  to twang  a  harp;  with  suffix -
```


## [2026-09-06T15:44:29.771Z] TOOL CALL #108: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6570,6580p' SKT.txt"
}
```


### [2026-09-06T15:44:29.816Z] TOOL RESULT

```
pp.  Of/Wjp/flf.
figment.    (L.)     \a.  figmemtum^  an  in- vention —  L-/^-,  base  m  fimnn. trnjisflgure.  ( F  -  L.)   F.  tramfigmrt*
150
FILAMENT.
«  L.  tramfi^ran,  to  change  the  fignre  or
ipcorance.  —  L.  ttanst  kcrow  (implying
langc) ;  fi^tra,  figure. Filament;  see  File  (i). Filbert,  fruit  of  hattl.   (F.-O.  H.  G.) Formerly  phiiibtrd  (Goweri ;    »hort    for Pkitibird  or  Pkiiibert  nut,  from  the  proper name  Pkiiibert ;  (S.  Philibcrt's  day  i«  Aug. aa).  — O. H.  G.jtf/i'-A^/t,  very  bright;  from Jtii  (G.  vul),  greatly,  bert,  berht,  bright. %  Called    in    Germany  Lamhertsnufs  (S. Laml)ert,  Sept.  17);  prob.  fron\  the  lime of  year  of  nottmg. Flloh.    (Scand.)     Extended  from  M.  E. fiUn,  to  conceal.  •Icel.yr/o,  to  hide,  bury. +Goth.y(/Aa«,  to  hide. File  (1),  string,   line,  order.    (F.  *  L.) O.  F.  JiU;  allied  to  F./A  a  thread.  -  L. JUum.,  a  thread.
defile  (3),  to  march  ia  a  file.  —  F.  di- fiUr,  10  defile.  -  F.  ii/.  -  O.  F.  des-  -» L,  dis-, apart ;  ftUr,  to  spin  threads,  from  h^Jilum. Der  defilt,  sb.
enfilade,  a  line  or  itnight  passage. (F.  —  L.)  F.  enfilade,  a  long  slrmg  lof things).  —  F.  enJiUr,  to  thread.  —  F.  «••  — L. in,  m  ;  fil,  a  thread,  from  h.JHum.
filament.  (F.  -  L.)  O.F. //amen,  • L  jUamentiim,  thin  thread.  —  Low  h./ilartt to  wind  thread.  — L.yf/iiM.
ftligrree.  Span.  -  U)  Formerly //«'- grvnt;  XVII  cent.  —  Span./Zi^rana,  fili- gree-work, fine  wrought  work.  — Span. ^/d, a  thread  or  tow,  JiJar,  to  spin ;  gutno,  grain or  texture ;  so  called  because  the  chief texture  of  it  was  wrought  in  silver  wiie. From  X^filnm,  thread;  ^ranum^  grain.
```


## [2026-09-06T15:44:40.413Z] TOOL CALL #109: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\np=\"data/verification/page-216.json\"\nd=json.load(open(p,encoding=\"utf-8\"))\ne1=d[\"entries\"][1]\nn6=[n for n in e1[\"nodes\"] if n[\"id\"]==6][0]\nfor c in n6[\"consulted\"]:\n    if c[\"src\"]==\"SKT\":\n        c[\"where\"]=\"Skeat, Concise Etym. Dict. s.vv. File (1) and filament (SKT.txt line ~6578)\"\n        c[\"note\"]=(\"'File (1), string, line, order. (F. - L.) O.F. file; allied to F. fil, a thread. - L. filum, a thread.' \"\n                   \"with the sub-entries 'filament. (F. - L.) O.F. filament, - L. filamentum, thin thread. - Low L. filare, to wind thread. - L. filum.', \"\n                   \"'enfilade ... F. enfiler, to thread ... from L. filum' and 'filigree'. Skeat keeps 'File (2)', the steel tool, apart as a Germanic word.\")\nn10=[n for n in e1[\"nodes\"] if n[\"id\"]==10][0]\nfor c in n10[\"consulted\"]:\n    if c[\"src\"]==\"WEB\":\n        c[\"src\"]=\"ETYMONLINE\"\njson.dump(d,open(p,\"w\",encoding=\"utf-8\"),ensure_ascii=False,indent=2)\nprint(\"ok\")\nPYEOF\npython3 tools/verify_check.py 216"
}
```


### [2026-09-06T15:44:42.434Z] TOOL RESULT

```
ok
nodes verified: 22/22
node verdicts: {'confirmed': 19, 'plausible': 2, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 19, 'not_checked': 6, 'not_found': 1, 'partial': 3}
books consulted: {'supports': 47, 'silent': 9, 'partial': 4, 'contradicts': 3} | by book: {'KLN': 14, 'IEC': 6, 'MON': 6, 'LAT': 6, 'ARY': 5, 'HUB': 4, 'NYB': 3, 'SKT': 3, 'BRT': 2, 'SYN': 2, 'PHD': 2, 'POK': 2, 'KNT': 1, 'SOD': 1, 'DEV': 1, 'AFM': 1, 'PLA': 1, 'WLD': 1, 'HRN': 1, 'ETYMONLINE': 1}
```


## [2026-09-06T15:44:59.922Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-216.json` written, valid JSON, `verify_check.py 216` shows **0 PROBLEM lines** (22/22 nodes).

**Page 216 (book p. 186) — Gwher "warm" / Gwhi "thread, string"**
- Roots: 2 confirmed. Nodes: 19 confirmed, 2 plausible, 1 disputed.
- Ref checks: 19 supports, 3 partial, 1 not_found, 6 not_checked (VOP and FVF have no accessible copy).

Flagged items:
- **disputed — Gwher #12, Persian fer/forn/fârîneh**: only فِر (French *four*) belongs under this arrow. فُرن is from Arabic فُرْن, itself Aramaic *pūrnā* ← Greek φοῦρνος ← Latin *furnus*; فرنی/فُرنیه are Arabic nisbas of that loan (Moʿin: «نانی که در فرن پخته باشند»); فارینه is French *farine* (Latin *farīna* < *far*, a different root) and is in no dictionary in the sense "thick bread". The box's note about a Latin → old Persian → Arabic → France round trip is the reverse of the accepted direction (Addi Shir and Asbaghi both silent on فرن as a Persian export).
- **plausible — Gwher #11, French *four***: the Latin *furnus* → *four* arrow is textbook, but the box's note "possibly reached French through Arabic" comes from Pihan, who claimed Arabic gave rise to Latin; modern scholarship reverses this.
- **plausible — Gwher #4, Sogdian γrm**: word and gloss confirmed (Gharib 4259), but it is inherited Eastern Iranian *garma- (cf. γ- < *g-, Khwar. γrm-, Yaghn. γarm), not a borrowing from Old Persian.

No extraction errors: the printed page (saved as `data/verification/sources/refs/ocr/BOOK/216.png`) matches the JSON exactly, including "žyâ 2" and "fârîneh". Note "žyâ" is *not* an error — Wiktionary cites the Avestan as 𐬲𐬌𐬌𐬁 žiiā, though Bartholomae/Horn/Pokorny normalise it as jyā-.

Two citation-page discrepancies for the owner: **PHN:187** — Pihan's FOUR entry is at pp. 167–168 (p. 187 is GREDIN); **BQT:1800** — right printed page, but `ref_page.py`'s default offset lands on p. 1798, use `--pdf-page 597`.
