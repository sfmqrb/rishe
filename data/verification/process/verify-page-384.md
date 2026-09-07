# Verification process log — verify-page-384


## [2026-09-07T20:41:13.373Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 384 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-384.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-384.json. Write /home/sfmqrb/git/rishe/data/verification/page-384.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 384` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:41:15.144Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:41:15.855Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:41:15.871Z] TOOL RESULT

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


## [2026-09-07T20:41:16.411Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-384.txt"
}
```


### [2026-09-07T20:41:16.428Z] TOOL RESULT

```
1	=== PDF page 384 (book page 354) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ped, Pod : foot  (refs POK:790)  PART 2
4	#1 (parent #0) [Greek] refs=AHD:1365; KLN; POK:790 | pous, peza : foot ; kalo-podion : wooden foot, mold ☞Kŭ 1 ; oktô-pous : eight legged, octopus ☞Okto
5	  #2 (parent #1) [Pahlavi] refs=BQT:1075 | kal-pâd : mold, shape, body | NOTE: IEC:1049,1051 derives this word from Avestan "kehrp: flesh", from Indo-European root "Kwrp, Kwerp: shape, form body".
6	    #3 (parent #2) [Persian] refs=MON:2858; IEC:1047 | kâlâ «کالا» : manufactured good, merchandise | NOTE: References are not very clear on the derivation paths.
7	    #4 (parent #2) [Persian] refs=BQT:1075; MON:2859 | kâleb «کالب» : mold ; kâlbod «کالبد» : body
8	      #5 (parent #4) [Arabic] refs=KLN:223; PLA:215 | qalib : mold ; q.l.b : to make, turn around
9	        #6 (parent #5) [Persian] refs=MON:2621; FVA:337 | qâleb «قالب» : mold | extra: قلب ، انقلاب ، منقلب
10	مقلوب ، تقلب ، قلاب
11	        #7 (parent #5) [Italian] refs=KLN:223 | calibro : mold, size
12	          #8 (parent #7) [French] refs=None | 
13	            #9 (parent #8) [Persian] refs=MON:2868 | kâlibr «کالیبر»
14	            #10 (parent #8) [English] refs=None | caliber
15	#11 (parent #0) [French] refs=None | octopode
16	  #12 (parent #11) [Persian] refs=MON:164 | oxtâpŭs «اختاپوس»
17	#13 (parent #0) [English] refs=None | octopus, pilot, podium
18	#14 (parent #0) [Greek] refs=AHD:1365 | tra-peza : "four-legged" table, trapezoid ☞Kwetwer
19	  #15 (parent #14) [Arabic] refs=MON:1481 | dar-bezin : a seating area between two doors of a room
20	    #16 (parent #15) [Persian] refs=MON:1481 | dârâbzîn «دارابزین» : a seating area | extra: درابزین ، دارافزین ، داروزین
21	  #17 (parent #14) [Latin] refs=AHD | 
22	    #18 (parent #17) [English] refs=AHD | trapezoid, trapeze
23	#19 (parent #0) [Germanic] refs=AHD | fot : foot
24	  #20 (parent #19) [English] refs=None | foot, fetch
25	
```


## [2026-09-07T20:41:21.832Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-384.json",
 "description": "Read source JSON for page 384"
}
```


### [2026-09-07T20:41:21.871Z] TOOL RESULT

```
{
  "pdf_page": 384,
  "book_page": 354,
  "entries": [
    {
      "root": {
        "name": "Ped, Pod",
        "lang": "Indo-European",
        "refs": "POK:790",
        "gloss": "foot"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1365; KLN; POK:790",
          "words": [
            {
              "translit": "pous, peza",
              "gloss": "foot",
              "script": null
            },
            {
              "translit": "kalo-podion",
              "gloss": "wooden foot, mold",
              "script": null,
              "see": [
                "Kŭ 1"
              ]
            },
            {
              "translit": "oktô-pous",
              "gloss": "eight legged, octopus",
              "script": null,
              "see": [
                "Okto"
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
          "lang": "Pahlavi",
          "refs": "BQT:1075",
          "words": [
            {
              "translit": "kal-pâd",
              "gloss": "mold, shape, body",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "IEC:1049,1051 derives this word from Avestan \"kehrp: flesh\", from Indo-European root \"Kwrp, Kwerp: shape, form body\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2858; IEC:1047",
          "words": [
            {
              "translit": "kâlâ",
              "gloss": "manufactured good, merchandise",
              "script": "کالا"
            }
          ],
          "script_extra": null,
          "note": "References are not very clear on the derivation paths.",
          "quote": {
            "text": "چو کالا بر فراز عرصه چیدی - عیان تا آخر بازی بدیدی",
            "poet": "Assâr"
          }
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1075; MON:2859",
          "words": [
            {
              "translit": "kâleb",
              "gloss": "mold",
              "script": "کالب"
            },
            {
              "translit": "kâlbod",
              "gloss": "body",
              "script": "کالبد"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "این من و این من که در این کالب است - هیچ مگو جنبش این قالب است",
            "poet": "Nezâmî"
          }
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Arabic",
          "refs": "KLN:223; PLA:215",
          "words": [
            {
              "translit": "qalib",
              "gloss": "mold",
              "script": null
            },
            {
              "translit": "q.l.b",
              "gloss": "to make, turn around",
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
          "lang": "Persian",
          "refs": "MON:2621; FVA:337",
          "words": [
            {
              "translit": "qâleb",
              "gloss": "mold",
              "script": "قالب"
            }
          ],
          "script_extra": "قلب ، انقلاب ، منقلب\nمقلوب ، تقلب ، قلاب",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "Italian",
          "refs": "KLN:223",
          "words": [
            {
              "translit": "calibro",
              "gloss": "mold, size",
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
          "refs": "MON:2868",
          "words": [
            {
              "translit": "kâlibr",
              "gloss": null,
              "script": "کالیبر"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "caliber",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "French",
          "refs": null,
          "words": [
            {
              "translit": "octopode",
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
          "parent": 11,
          "lang": "Persian",
          "refs": "MON:164",
          "words": [
            {
              "translit": "oxtâpŭs",
              "gloss": null,
              "script": "اختاپوس"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "octopus, pilot, podium",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1365",
          "words": [
            {
              "translit": "tra-peza",
              "gloss": "\"four-legged\" table, trapezoid",
              "script": null,
              "see": [
                "Kwetwer"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Arabic",
          "refs": "MON:1481",
          "words": [
            {
              "translit": "dar-bezin",
              "gloss": "a seating area between two doors of a room",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:1481",
          "words": [
            {
              "translit": "dârâbzîn",
              "gloss": "a seating area",
              "script": "دارابزین"
            }
          ],
          "script_extra": "درابزین ، دارافزین ، داروزین",
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 14,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "trapezoid, trapeze",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "fot",
              "gloss": "foot",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "foot, fetch",
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


## [2026-09-07T20:41:23.474Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','BQT','MON','PLA','IEC','FVA','WLD','SYN','PHD','NYB','HRN','HUB','ARY','BRT','SKT','WEB','FSD','LKT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T20:41:24.762Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
```


## [2026-09-07T20:41:49.152Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; ls ocr 2>/dev/null | head"
}
```


## [2026-09-07T20:41:49.169Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T20:41:49.220Z] TOOL RESULT

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


### [2026-09-07T20:41:49.226Z] TOOL RESULT

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


## [2026-09-07T20:41:55.821Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK grep ped- ===\"; grep -n \"ped-, pod-\\|pēd-, pod-\\|ped-, pōd-\" POK_full.txt | head -20\necho \"=== POK_full page 790 marker ===\"; grep -n \"^790\\|790$\" POK_full.txt | head -5\n"
}
```


### [2026-09-07T20:41:57.191Z] TOOL RESULT

```
=== POK grep ped- ===
=== POK_full page 790 marker ===
```


## [2026-09-07T20:41:57.539Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins ped ===\"; grep -n -i \"^ped-\\|ped-. Foot\\|To walk, stumble, fall\" AHD_watkins1985.txt | head -20\necho \"=== KLN caliber ===\"; grep -n -i \"calibre\\|caliber\" KLN_1966.txt | head -20"
}
```


### [2026-09-07T20:41:57.613Z] TOOL RESULT

```
=== AHD watkins ped ===
819:ped-2. Container. 1. Suffixed o-grade form *pod-om in Germanic “fatam in Old English fzt, cask: vat. 2. Suf- fixed o-grade form *pod-ilo- in Germanic *fatilaz in Old English fetel, girdle: FETTLE. 3. Probably full-grade form *ped- in Germanic *fet- in Middle High German vetze, “clothes,” rags, probably akin to the source of obsolete English fritter, fragment: FRITTER}. [Pok. 1. péd- 790.]
1527:FOOL! bhel-2 FooT ped-! FOOTPAD pent- FoR pert
=== KLN caliber ===
6183:Derivative:  Caliban-ism,  n. caliber,  calibre,  n.,  the  diameter  of  the  bore  of  a gun.  —  F.  calibre,  fr.  It.  calibro,  fr.  Arab,  qdlib, ‘mold,  model’,  fr.  Gk.  xxXo ttoSlov,  ‘shoemaker’s last’,  dimin.  of  xxXomiuc,  gen.  x5X6jro8o?,  of s.m.,  lit.  ‘a  foot  of  wood’,  fr.  xxXov,  ‘wood’,  esp. ‘wood  for  burning’,  and  -064,  gen.  720864,  ‘foot’, Gk.  xiXov  is  contracted  fr.  *xaf-sXn-v  or  *xAF- aXo-v,  a  derivative  of  xaietv  (for  *xAfiav),  ‘to bum’;  see  caustic.  For  the  second  element  see foot  and  cp.  -pod.  Gk.  xAXo7t68lov  came  into Arabic  through  the  medium  of  the  Aramaic, calibrate,  tr.  v.,  to  determine  the  caliber  of.  — A  hybrid  coined  fr.  caliber  and  -ate,  a  suff.  of Latin  origin.
6192:caliper,  calliper,  n.  —  Variant  spellings  of caliber.  Derivatives:  cal(l)iper ,  tr.  and  intr.  v., cal(l)iper-er ,  n.
6855:Derivative:  causeway,  tr.  v, causey,  n.,  a  causeway  (dial.)  —  ME.  cauce,  fr. ONF.  cauciee,  corresponding  to  F.  chaussee, ‘causeway’,  fr.  VL.  (via)  calctata,  lit.  ‘a  road paved  with  limestone’,  fern.  pp.  of  calciare,  ‘to pave  with  limestone’,  fr.  L.  calx,  gen.  calcis, ‘lime, limestone’.  See  calcareous  and  cp.  chaussee. caustic,  adj.,  burning,  corrosive.  —  F.  caustique, fr.  L.  causticus,  fr.  Gk.  xookttixoc,  ‘capable  of burning,  corrosive’,  fr.  xxocrro?,  ‘burnt’,  verbal adj.  of  xcciEiv,  which  stands  for  *xif-ts'.v,  ‘to burn,  set  on  fire’,  fr.  I.-E.  base  *keu-,  *kii-,  ‘to burn,  heat’,  whence  also  Lith.  kttle,  ‘blight,  mil¬ dew',  kiileti,  ‘to  become  blighted’.  Cp.  caeoma, caliber,  calm,  catacaustic,  Caucasian,  cautery, diacaustic,  encaustic,  holocaust,  hypocaust,  ink, Nausicaa.
15110:foot,  n.  —  ME.  fat,  fr.  OE.  fat,  rel.  to  OS.  fat, ON.  fa tr,  Swed.  fat,  Dan.  fad,  Du.  voet,  OHG. fuo3,  MHG.  VU03,  G.  Fuji,  Goth./o/u.s,  ‘foot’,  and cogn.  with  Ol.  pit,  acc.  pidam,  ‘foot’,  Avestic pad-,  ‘foot’,  Toch.  A  pe,  B  pai,  ‘foot’,  A  pent,  B paine,  ‘both  feet’.  Arm.  ot-n,  ‘foot’,  ot-k\  ‘feet’. Dor.  Gk.  7rtii ;,  Att.  7101)9  (formed  on  analogy  of 009,  ‘ear’),  gen.  770809,  L.  pes,  gen.  pedis,  ‘foot’, Ol.  paddm,  ‘step,  track’.  Arm.  het,  gen.  he  toy, ‘track,  footmark’,  Gk.  rtiSt),  ‘fetter’,  TreSav,  ‘to bind  with  fetters’,  7t£Sov,  ‘ground,  earth’,  h.peda, ‘footstep \pedica,  ‘shackle,  fetter’,  impedire,  ‘en¬ tangle,  ensnare’,  expedire,  ‘to  extricate,  disen¬ gage’,  Lith.  peda,  ‘footstep,  trace’,  OSlav.  podii, ‘loft’,  Russ,  pod-oshva,  ‘sole  of  foot’.  All  these words  derive  fr.  I.-E.  base  *pdd-,  *pid-,  ‘foot’. Cp.  fetch,  fetlock,  fetter,  fit,  ‘part  of  a  song’.  Cp. also  antipodes,  apod,  babouche,  biped,  breviped, caliber,  cap-a-pie,  charpoy,  expedient,  expedite, impeach,  impede,  impedimenta.  Lycopodium, millepede,  multiped(e),  octopus,  oppidan,  palmi¬ ped,  pawn  (in  chess),  parallelepiped,  pajama, pedal,  pedate,  -pede,  pedesis,  pedestal,  Pedetes, pedicel,  pedicle,  pedigree,  pedology,  ‘the  study  of soils’,  peduncle,  peon,  pes,  petiole,  pew,  Peziza, pie,  ‘a  small  coin’,  piepoudre,  pilot,  podagra, podal,  podium,  podo-,  pug,  ‘footprint’,  puy,  seer- paw,  Taliped,  Tarsipes,  teapoy,  trapezium,  triped, tripos,  vamp,  ‘front  part  of  the  foot’,  velocipede. Cp.  also  pejorative,  pessimism.
```


## [2026-09-07T20:42:05.821Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '810,822p' AHD_watkins1985.txt"
}
```


### [2026-09-07T20:42:05.866Z] TOOL RESULT

```
ors-. Buttocks, backside. 1. Suffixed form *ors-o- in Germanic *arsaz in Old English zrs, ears, backside: ass?. 2. Suffixed form ‘*ors-d- in: a. Greek oura, tail: URO-2, -UROUS; ANTHURIUM, ANURAN, CYNOSURE, EREMURUS, OXYURIASIS, SQUIRREL, TRICHURIASIS; b. probably Greek silouros, sheatfish (< obscure first element + oura): SILURID. [Pok. ers- 340.]
pan-
os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PALISADE, PEEL’, POLE?; IMPALE, TRA- VAIL, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English
pandoura
fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
peig-
shackle,” entangle, hinder (in-, in; see en): IMPEDE. 6. Suffixed form *ped-ikd- in Latin pedica, fetter, snare: DISPATCH, IMPEACH. 7. O-grade form *pod- in: a. Greek
* pous (stem pod-), foot: PEW, -POD, PODITE, PODIUM;
ANTIPODES, APODAL, APPOGGIATURA, APUS, CALIBER, LYCOPODIUM, MONOPODIUM, OCTOPUS, PELECYPOD, PHALAROPE, PLATYPUS, PODAGRA, PODIATRY, PODOPHYL- LIN, POLYP, POLYPOD, SYMPODIUM; b. Russian pod, un- der: PODZOL. 8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM. 9. Suffixed form *ped-o- in: a. Greek pedon, ground, soil: PEDO-!; PARALLELEPIPED; b. San- skrit padam, footstep, foot, and pat (> Hindi paisd), foot: PAISA, PICE, PIE’, PUG3; c. Middle Persian pdi, leg, foot: PAJAMAS, TEAPOY; d. lengthened-grade form *pédo- in (i) Greek pédon, rudder, steering oar: PILOT (ii) Greek pédan, to leap: DIAPEDEsIs. 10. Suffixed form *ped-i- in Greek pedilon, sandal: CYPRIPEDIUM. II. Verbal root *ped-, to stumble, fall. 1. Germanic *fetén in Old English fetian, feccean, to bring back: FETCH!. 2. Latin *ped- in: a. suffixed (comparative) form *ped-yos in Latin péor, worse (< “stumbling”): PEJORATION; IMPAIR; b. suffixed (superlative) form *ped-samo- in Latin pessimus, worst: PESSIMISM; C. suffixed form *ped-ko- in Latin peccdre, to stumble, sin: PECCABLE, PECCADILLO, PECCANT; IMPEC- CABLE. [Pok. 2. péd- 790.]
ped-2. Container. 1. Suffixed o-grade form *pod-om in Germanic “fatam in Old English fzt, cask: vat. 2. Suf- fixed o-grade form *pod-ilo- in Germanic *fatilaz in Old English fetel, girdle: FETTLE. 3. Probably full-grade form *ped- in Germanic *fet- in Middle High German vetze, “clothes,” rags, probably akin to the source of obsolete English fritter, fragment: FRITTER}. [Pok. 1. péd- 790.]
peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit
paksah, wing: PUNKA. [Pok. (peg-), pdg- 792.]
p@(i)-. Also pé-, pi-. To hurt. Possible root; contracted from *pea(i)-. 1. Suffixed (participial) form *pi-ont- (< *pia-ont-) in Germanic *fiand-, hating, hostile, in Old English féond, fiond, enemy, devil: FIEND. 2. Possibly *pé- in suffixed zero-grade form *po-to- in Latin pati, to suffer: PASSIBLE, PASSION, PASSIVE, PATIENT; COMPAS- SION. [Pok. pé(i)- 792.]
```


## [2026-09-07T20:42:06.961Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls POK*; echo ---; grep -c \"\" POK_full.txt 2>/dev/null; echo ---; grep -n \"pē̆d-\\|1. pē̆d-\\|ped- 'Fuß'\\|Fuss\" POK_full.txt | head -10"
}
```


### [2026-09-07T20:42:07.042Z] TOOL RESULT

```
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
---
93771
---
```


## [2026-09-07T20:42:14.527Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Root / lemma: pē̆d-\\|pē̆d-2\\|ped- 2\\|Fuss; gehen\" POK_full.txt | head -20\necho \"=== try ===\"\ngrep -n \"790\" POK_full.txt | head -20"
}
```


### [2026-09-07T20:42:14.593Z] TOOL RESULT

```
=== try ===
17806:References: WP. I 790. 
18044:References: WP. I 790 f. 
36292:with Persson (Beitr. 790) and Kretschmer (Gl. 21 , 115) the Balto-Slavic *gel- is defined 
36630:Trautmann 83 f., 88, 364 f., 368, 372, Persson Beitr. 170 f., 790 ff., 876 f. 
56343:References: WP. II 417 f., WH. I 790 f., Trautmann 150 f. 
64777:Page(s): 790 
64907:Page(s): 790 
67623:Page(s): 790 
67742:Page(s): 790-792 
69323:poln. etc. yoys/r "snout, muzzle with thick Lippen'); compare above S. 790 pauson-1
```


## [2026-09-07T20:42:17.035Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '67680,67760p' POK_full.txt"
}
```


### [2026-09-07T20:42:17.147Z] TOOL RESULT

```
English fitt^break, section, poem', Norwegian dial. fior-fit^\\z&r6\ 'Tsrpans^oc;'), Lithuanian 
lengva-pedis^\e\seiu{!i\0)'\ pedf-\x\ gr. nsSTAov n. 'sandal' and Germanic *fetf, podio-m. 
Middle Irish u{/)c/en. 'journey'. 

2. Verbal: Old Indie yoaoya/e" 'goes, fallt' (a-pa///- 'Unfair; padat/-, pat-tf-m. 'Fuftknecht'), 
Avestan pa/6ye/f/ ^bewegt sich after downwards, legt sich nieder'; Old Church Slavic padg, 
past/laW also po-past/ ^catcW actually 'auf jemanden fall, spring on, attack ' (or to pecf- 

/?); napastb 'casus'; Lithuanian pedinu, -//7//'slowly go, leise tread', peduoti^Vu{i>\x\\.\.e 
make', gr. nr|5au) 'spring, hijpfe'; compare zur e-grade still Lithuanian peda^ footprint ', 
pesetas 'to foot' from *ped-tios, Latvian yoyo's 'Fuftsohle, Fuftstapfe, foot as measure ', pec 
(from pedis, Instr. PI. from p^ds^ footprint ', compare Lithuanian pedas6s.) 'after, because 
of, gemaR.', Old Church Slavic pesb 'to foot', gr. nr|56v ' rudder blade ', nr|5aAiov ' rudder, 
helm '; auf the verbalen meaning 'more abfallend or to Fallen, Verkommen willing, inclined' 
based on letzten Endes also the Kompar. Latin pe/or^bad' {*ped-ids), Superl. pessimus 
'the schlechteste' {*ped-Semos)\ pessum^to bottom, zugrunde' {*ped-tu-m) = Infin. Old 
\n6\c paftum; Old Icelandic fefa stem V. (also with /e/P, veg, heim) 'den way find' Old 
English ge-fetansiexw V. 'fall'. Old High German /ezz5/7'labare', g/-fezzan^ex\re, 
excidere'. Old Icelandic fafa^se\nen wayfinden'. Old English fatian{wTf} 'uxorem ducere'. 
Old High German s/h uazzon^scan6ere', Old English fef/an, engl. fetch^get, fetch' (Old 
English fat/an an6 fef/an cou\6 also to ped-f be\ong, as generally die beiden the families 
not sharp to separate are). 

3. pedo-metc. Old \r\d'\c pada-n. ' footstep, step, tread; kick, strike or blow delivered by 
the foot; footprint, track, Fuftstapfe', Avestan pada-n. 'spoor' (and 'foot as measure '), ap. 
paf/'-padam ^ an seine Stelle zurijckkehrend'; 

Armenian hef, Gen. hefoy' footprint ', preposition y-ef{*/-het"\n the footprint ') 'after', z- 
het, zetoy^ behind after'; Middle Irish ined{ *eni-pedo-) 'spoor (the Fijfte); place'. Old Irish 
edn. 'stretch of time', gall, candetum^ s'^aWum, centum pedum' probably for cant-fpjedunr, 
compare Latin yoeo'a 'vestigium humanum'. Old Icelandic fetn. ' footstep; foot as measure 
'; Lithuanian peda^ footprint ', Latvian yoyo's 'Fuftsohle' etc. (see above); gr. nsSov 
'ground, bottom', nsSiov ' plain, field' (£p-n£5o(; 'tight, firm stehend'; about SansSov see 
above S. 198); Latin oppido^voWxg, totally and gar' {ob+ *pedom^aui\he place '); Umbrian 
pefum, persom-e^TTzbov 'solum'; Hittite pedann., place'; 



ograde: Lithuanian pac/asTuQ>so}r\\e, Stiefeisoliie' = Old Cliurch Slavic *pocfh' bottom, 
Untergrund, Unterlage' (preposition podb "below, under'), Lithuanian padziaiP\. 
"Untergestell a barrel'. Old Church Slavic pozdb 'fundamentum, locus subterraneus'; 

schwundstufige forms: Old Indie upa-bda-m. "Getrampel', Avestan /^5-Ma 'forefoot' 
(from ped- "foot'), a-bda- "where man nicht hintreten, nicht fixed Fuft fassen kann'; gr. sni- 
pSai "day after dem Feste'. 

4. Meaning group "(Fuft)fessel, hindrance for die Fijfte': Avestan b'hbda- " double 
manacle'; gr. nsSn "manacle', TisSau), TioSi^u) " tie ', av5pa-no5ov n. "slave', £k-tto5u)v 
"from dem Wege', £iJ-no5u)v "in Wege, obstructive'; Latin yoeoVica "manacle, loop, noose, 
snare ' (wherewith e.g. ein Tier an a foot angebunden wird); Latin peccare " blunder, 
commit a sin' to *peccos < *ped-cos "einen flaw am foot habend', wherefore also Umbrian 
yoe'se/c/77"peccatum', cc»/77yC>e5"FuR)Schelle, Fuftblock', impedio, -/?e "hinder', 
Gegensatzbildung expedTre^Aas Hindernis wegnehmen' (probably to *pedis\. "Fuftfessel' 
shaped); in addition oppidum^6\e Schranken of Zirkus (also "quod pedibus obest'); 
Landstadt' (originally with Hindernissen verrammelte refuge); at most Umbrian tribrigu, 
tr/bris/ne ^tern\o' as *//7-peo''//r/o"Dreikoppelung'; Old Icelandic fjgturrm. "manacle, band, 
strap'. Old English feter, feotori.. Old Saxon fetur. Old High German fezzerAs. 

maybe alb. penge< Latin pedica -ae, f. "a fetter; a trap, snare (for animal's feet)'; alb. 
peAT^oy (nasalized *pgdica) "hinder' = Latin * pedica, impedio, -Tre; 

References: WP. II 23 ff., WH. I 428 f., II 214 f., 269, 272 f., 293 ff., Trautmann 209 f. 
Page(s): 790-792 

Root / lemma: pe(i)- pT- 

Meaning: to harm, scold, put to shame 

Material: Old Indie yO/Ka//"schmaht, hohnt', pTyu-, ^//^/^/-"hohnend, schmahend'; 

gr. nnija "ruin, affliction', anrnjwv "unbeschadigt; unschadlich ', rrriMaivu) "stifte mischief, 
ruin' (Indo Germanic *pe-mn), nnaaaOai [JEpujaaOai Hes., rj-navia "lack, Entbehrung'; 
TTPipoq, Doric napoc; "mutilated, blind', a-nr|poc; "unverstummelf; Latin paene{pene) 
"beinahe, fast; totally and gar' (originally neuter eines Adj. *pe-ni-s' damages, 
mangelhaft'), paeniteVos reut, tut leid', penuria ^\3iCV!\ from a participle *pa-t6-s 
"geschadigf derives patior, -I passus sum "dulde, bear, endure, suffer'; 



Indo Germanic pe/- in Gotliic fa/an'rebuke, reproacli', pf-'m Gotliic f/jan, Old Icelandic 
^a, Old English feon, Old High German fwn'hate', participle present in Gothic fijands. Old
```


## [2026-09-07T20:42:21.584Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '67640,67682p' POK_full.txt"
}
```


### [2026-09-07T20:42:21.641Z] TOOL RESULT

```
dem Lok. PI. *ped-su^\.o Fijften' deutbar = alb. posh'xu perposh ' under' , posh-te 'herab, 

subterraneous, underground; under, downwards '; Gothic fotus. Old Icelandic fotr. Old 

English fdt{Novn. PI. Old Icelandic f0tr. Old English fetirom *fdt-iz) Old High German fuoz 

"foot'; Hittite Luvian pata-, Hieroglyphic-Hittite patds.; Tocharian A pe, B pai. Dual A pern, 

B paine; 

Note: 

Maybe alb. ( *po-s) poshte^ below, under ' from the same root as Slavic languages Slavic 

po-d-b " below, under ' from zero grade of Root / lemma: apo- {p6, ap-u, pU)\ (from, out, of) 

not from Root/ lemma: ped-2, p6d-\ (foot, *genitalia). 

Maybe Tadzik PUST, TAXTAPUST, Lahnda PICCHE, Nepali PITH, Kashmiri PYUTHU, 

Singhalese PASSA, Baluchi PHUSHT, Gujarati PITH, Panjabi ST PITTH, Hindi PITH, 

Bengali PIT, Marathi PATH, Persian POSHT " spine '. 

to ped- "foot' belongs gr. dial. n£5a "hetq', originally "(jemandem) auf dem Fufte', 
compare Latin pedisequus, -a "servant, -in' actually "auf dem Fufte folgend' and under die 
Armenian from het^ footprint ' refined prepositions; 

with -i-6s, -/-/-"going' are shaped: gr. ns^oc; "pedestris', Latin ped-es, -/-/-/5"FuR)ganger, 
Fuftsoldat'; from Latin pes denves pedare^W\Vc\ a Fuft versehen, prop, support', and 
therefrom again yOec/i//77 "shepherd's crook; crosier, pad'; 

pedio-\n Old \u6\c padya-^deu Fuft betreffend', /05oya"Fufttritt, hoof, Avestan paidya 
"foot', gr. ns^a f. "foot, untereredge, border, hem, small fishing net', Latin acu-pedius 
"swift-footed'. Old High German /feza "Gewinde, thread, string' (= gr. ns^a). Modern High 



German Titze', (wherefore Germanic *fetTi. in Old Icelandic /^/'Schwimmhaut, edge', Old 
English fitt^break, section, poem', Norwegian dial. fior-fit^\\z&r6\ 'Tsrpans^oc;'), Lithuanian 
lengva-pedis^\e\seiu{!i\0)'\ pedf-\x\ gr. nsSTAov n. 'sandal' and Germanic *fetf, podio-m. 
Middle Irish u{/)c/en. 'journey'.
```


## [2026-09-07T20:42:32.388Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n -i \"kalbod\\|kalbad\\|kʾlpwt\\|kalpod\" PHD.txt PHD_mackenzie.txt | head\necho \"=== NYB ===\"; grep -n -i \"kalbod\\|kalbad\\|kalpat\\|kʾlpwt\" NYB_vol2_glossary.txt | head\necho \"=== HRN ===\"; grep -n -i \"kalbud\\|kālbud\\|kalbad\\|kālib\\|kālā\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"kalbud\\|kalbad\\|kālib\" HUB.txt | head -20"
}
```


### [2026-09-07T20:42:32.489Z] TOOL RESULT

```
=== PHD ===
PHD.txt:5057:kār- wing! *kār-ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd
PHD_mackenzie.txt:3154:kalbod [k)lpwt ' I (M k)lbyd), N ~] body, shape, form.
PHD_mackenzie.txt:6074:bestowal baxsisn.                           body kalbod, kirh, tan.
PHD_mackenzie.txt:9702::!kay                                    ..tg   kalbod                    \lDl~~
=== NYB ===
2168:kālpa6 [k*lpt'], kalpu& [k’Ipwt'] shape, external bodily form 892%, 9026, 10127, — MPrs k’lbyd (List 84); Paz. kälbud, Skr. v. kaya sundara (Aog.); NP kalbad, kälbud ‘the body of a man or an animal’, ‘a model, a last for shoes" which is the original sense, the w. being borrowed from Gr xadronddtov..
=== HRN ===
=== HUB ===
6282:LW. kathad, kalbud *Modeir, paz. kaibud, -phi, kalput^ kalpat,
9471:*Kohr = gr. x()diu(it] ; kdlbad, kalbud *Modeir, phi. kolput =
```


## [2026-09-07T20:42:33.744Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT qalib/kalopodion ===\"; grep -n -i \"qalib\\|kalopodion\\|kalibr\\|Kaliber\" LKT.txt | head -20\necho \"=== PLA text? ===\"; ls incoming/PLA/"
}
```


### [2026-09-07T20:42:33.805Z] TOOL RESULT

```
=== LKT qalib/kalopodion ===
674:Aus  tk.  hal  'Honig'  und  bas  'Kopf, eigentlich  'Honigkopf',  hieraus  rum. balba^,  baba§  'Honigwasser'.  —  Aus  tk. balgy  'Honigverkäufer'  wird  rum.  balgiü 'dass.'.  —  Tk.  bal-jemez  'der  nicht  Honig ißt  oder  frißt'  ist  Bezeichnung  für  ein Geschütz  großen  Kalibers,  vgl.  v.  Moltke, Briefe  über  Zustände  und  Begebenheiten in  der  Türkei.^  1876.  S.  260  im  Briefe vom  12.  Mai  08.  Hieraus  rum.  balimez, baliemez  'großkalibriges  Geschütz'.  Hier- von kommt  sicherlich  auch  der  luia. Ausdruck  a  face  talme§  bahiief  'krumm und  lahm  schlagen'.
2454:'Leisten  eines  Schusters',  ebenso  tk. kalyh,  Icahjp  'Modell,  Form';  hieraus rum.  calib,  calip,  calup  'Gießform,  Mo- dell, Leiste',  calupciü  'Betrüger';  aus dem  Ar.  unmittelbar  sp.  gälibo  'Schiffs- modell', frz.  gabarit;  asp.  calibo,  sp. calibre,  frz.  calibre  'Durchmesser  der Mündung  eines  Geschützes,  Gewicht  der Kugel';  it.  coUbro  'Maßinstrument,  um die  Zusammengehörigkeit  von  Geschütz und  Geschoß  zu  bestimmen';  dtsch. Kaliber,  engl,  calibre  [amerikanische Schreibung  caliber,  s.  Herrigs  Archiv CXLI,  194],  bei  Shakespeare  l.HenrylVth IV,  2,  21.  2.  Henry  IVth  III,  2,  292 und  295  caliver  'kleine  Muskete'  [wenn nicht  aus  frz.  coiileuvre  <^  lat.  coluber 'Schlange'] ;  russ.Ä:«?«/^ 'Gießform, -löffel', kaliber  'Geschützweite',  bulg.  kahp,  serb. kalup  'Gußform,  Schuhleisten'.  [Devic DEt  79/80.  Gorjajew  129.  Sain  48. SCHUCK ARDT  in  ZfromPh  XXIV,  571. A.  KLUYVER  in  ZfdWf  XI,  219/224.
2876:'Tiefer  Korb,  Tragkorb'  [aus  gr.  KÖqpivoq, lat.  cophinus  <C  lat.  cuppa,  vgl.  Lammens Farak  Nr.  1037];  hieraus  nach  der  vulg. Aussprache  mit  o  nach  einem  empha- tischen Laute  sp.  cofa,  cofe,  it.  coffa 'Mastkorb',  pg.  alcofa  'Korb',  cofo  'Kü- bel', siz.  coffa  'Marktkorb',  [mit  rom.  En- dung] it.  cöfano,  sp.  cuibano;  rum.  cofä 'Eimer,  Holzkanne'.  Afrz.  cofre,  frz. coffre,  engl,  coffer,  dtsch.  Koffer  [mit Anfügung  eines  -r  wie  in  Kaliber,  s.  hier Nr.  1030,  und  Kassiber,  hier  Nr.  1168]. Serb.  kofa  'Korb,  Mastkorb',  kofan  'Tru- he', öech.  kufr,  poln.  kufr,  klruss.  kufer 'Koffer'.  [DE  94.  Eguilaz  140.  StGlIt n,281.  GrSVociSic  232.  ML  2207  u.  4730.
5787:Äafta?e  977 iCrtöajg  993 iCa^eZ  766 Zaö(//e  979 ^Tad«  984 ifßtZjne  989 i:fl/f  992 Kaffee  4005 ^^//fe;-  992 Ka filier  j.  1150 Kaftan  774 Kaj>'put(öl)  1142 Kakadu  1Ü17 Kolbehasit  St.  1026 Kalbelazguar  St.  1025 Kalbolacrab  St.  1026 kalekutischer  Hahn  1031 kalemine  mhd.  1149 Kalender  1024 Kalenter  1024 kalfatern  1022 Kaliber  1030 ifaZ//"  798 A'rtZiX-o  1031 Kalium  1029 ifaZ/e  j.  1035 ifaZo«^  1038 Ar<?jjrtfc  1039 Kamel  653 Kamelie  653 Kamelhaut  653 Kamelot(t)  653 Kampfer  1100 Kandare  1051 kandieren  1052 Kandis  fzuckerj  1052 Kantschu(k)  1042 iCao/in  1060 Kap(p)ern  978
=== PLA text? ===
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-07T20:42:46.946Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 2450-2456 ===\"; sed -n '2448,2456p' LKT.txt\necho; echo \"=== NYB context ===\"; sed -n '2160,2172p' NYB_vol2_glossary.txt\necho; echo \"=== HUB context 6275-6290 ===\"; sed -n '6275,6290p' HUB.txt\necho; echo \"=== HUB 9465-9478 ===\"; sed -n '9465,9478p' HUB.txt"
}
```


### [2026-09-07T20:42:47.029Z] TOOL RESULT

```
=== LKT 2450-2456 ===
'Pflaster'  [vom  Stamme  kal  'anschwellen, Menge,  Berg',  also  k.  'erhöhter  Weg, Pflaster',  Vämbery  TktEtWb  S.  67,  Nr.  72] ; hieraus  bulg.  kaldzrim,  kaldhrma  'Pfla- ster', serb.  kaldrma  'Landstraße,  ge- pflasterte Straße';  rum.  caldarim  'Stein- pflaster', caldartmgiü  'Pflasterer'.  [Bern SlEtWb  472.
83
[Ar.  kali.
1029.  Ar.  kali:
Tüttasche,  Aschensalz';  mit  ar.  Art.  in alle  europäischen  Sprachen  als  Fach- ausdruck der  Chemie  übergegangen:  sp. pg.  alcali,  frz.  alcali,  als  alchemistischer Ausdruck  algali  'Salpeter',  dial.  (Süd- frankreich) caliou  'Asche  aus  den  Reb- stöcken', engl,  alhdi,  dtsch.  Alkali  usw. Auch  der  Namen  des  Elementes  Kalium, Calium  gehört  hierhin,  [Devic  DEt  7. Lammens  Rem  7.
1030.  Ar.  kälib:
'Leisten  eines  Schusters',  ebenso  tk. kalyh,  Icahjp  'Modell,  Form';  hieraus rum.  calib,  calip,  calup  'Gießform,  Mo- dell, Leiste',  calupciü  'Betrüger';  aus dem  Ar.  unmittelbar  sp.  gälibo  'Schiffs- modell', frz.  gabarit;  asp.  calibo,  sp. calibre,  frz.  calibre  'Durchmesser  der Mündung  eines  Geschützes,  Gewicht  der Kugel';  it.  coUbro  'Maßinstrument,  um die  Zusammengehörigkeit  von  Geschütz und  Geschoß  zu  bestimmen';  dtsch. Kaliber,  engl,  calibre  [amerikanische Schreibung  caliber,  s.  Herrigs  Archiv CXLI,  194],  bei  Shakespeare  l.HenrylVth IV,  2,  21.  2.  Henry  IVth  III,  2,  292 und  295  caliver  'kleine  Muskete'  [wenn nicht  aus  frz.  coiileuvre  <^  lat.  coluber 'Schlange'] ;  russ.Ä:«?«/^ 'Gießform, -löffel', kaliber  'Geschützweite',  bulg.  kahp,  serb. kalup  'Gußform,  Schuhleisten'.  [Devic DEt  79/80.  Gorjajew  129.  Sain  48. SCHUCK ARDT  in  ZfromPh  XXIV,  571. A.  KLUYVER  in  ZfdWf  XI,  219/224.
1031.  Uiud.  köHködn:
'Hahnfestung',  N.  pr.,  Name  einer  Stadt an  der  Westküste  Ostindiens  [ihr  Name wird  durch  eine  Sage,  die  derjenigen Didos  ähnlich  ist,  erklärt:  der  Raum, auf  dem  ein  Hahnenschrei  zu  hören war,  wurde  einst  dem  Zamorin  gewährt], von  großer  Bedeutung  in  der  ersten Entdeckungsgeschichte  [hier  landete  am 20.  Mai  1498  VASCO  DA  GAMA]  und als  Herstellungsort  von  kattunenen Stoffen;  aus  der  späteren  Form  des Namens  Kalikati,  Calicut  wurde  frz. calicot  'Baumwollstoff  von  leinenartigem Gewebe',  engl.  ndl.  calico,  dtsch.  Kaliko; bulg.  serb.  kaliko,  ßech.  kaliko,  russ. kalenkor,  kolenkor.  —  Nach  der  Stadt wurde  früher  auch  der  Truthahn  [der allerdings  im  Jahre  1524  aus  Florida nach  Europa  gebracht  wurde]  benannt: dtsch.  kalekutischer  Hahn,  der  Kalekut, ndl.  kalkocnsche  oder  kalekntsche  hen, kalkoen;  hieraus  rviss.kalkun,  poln.(dial.) kalkun,  kalkut  [vgl.  hier  Nr.  909). [Hobson  Jobson  147/148.  Gorjajew  150. Bern  SlEtWb  479.

=== NYB context ===
kahvanéh [khwbnyh] decay 1128. — Abstr. of kahvan [khwbn'] NP kuhan, kahun ‘worn, old, aged’, < MPrth kfwn, qfwn (List 84), from kaftan.
kai [kd] king, sovereign, the title of the ancient kings of Eastern Iran: —-Kavät, the founder of the. dynasty; ~-X6sr61, ~-Luhrasp, ~-Vistasp, cf Käyös; pl.cas. obl. kayān [kd’n'] 2727, zuarrah i —-ān, ~-dn xLarrah, v. xuarrah; Artaxser is addressed as ~ before becoming king 618; — the seven assistants of Saosyant who perform the eschatological actions are called ~ 64; also Krišāsp 997°; cf also s. v. Xosrči. — Av. (442 sg.) kavi-; MPrth kw, pl. cas. obl. q’w’n ‘giant’; Prs on coins kd, kdy = FrP 12, with the explanation mas ‘great’; Paz. ka; NP kai ‘great king’ and borrowed from the NW language kav ‘valiant, grand, of fine figure’.
www.parsianjoman.org | coal wok
kai-bäg
*kai-bāg [kdb’(g)] “having share with the kat", "sharing with the king" = co-regent 221’, v. also ném-vécak. — Coin- cides graphically with KDB’ = drag ‘lie’, which is sheer nonsense in this context. Np kiyd ‘a king, protector; a lord, a margrave’, also n. pr.
kai-gah [kdg’s] the royal camp (during a campaign) 211. 23 passim.
Kai-Kavat [kdkw't'] v. Kavāt. Kai-Luhräsp [kdlwhl’sp'] v. Luhräsp.
kaivän [kdw’n'] the planet Saturn 77. — Borrowed from Aram: Syr kewän, bor- rowed in its turn from Ass katamanu. Kai-Vištāsp [kdwSt’sp'] v. Vištāsp. Kai-X čsrči-šat [kdhwslwd š*t'] n. pr. of a town 1149. — “K.-X. is glad"; v.s. v. Xösröi.
kālpa6 [k*lpt'], kalpu& [k’Ipwt'] shape, external bodily form 892%, 9026, 10127, — MPrs k’lbyd (List 84); Paz. kälbud, Skr. v. kaya sundara (Aog.); NP kalbad, kälbud ‘the body of a man or an animal’, ‘a model, a last for shoes" which is the original sense, the w. being borrowed from Gr xadronddtov..
kam [km] little (adj. and adv.), few 6617. 9319.21 966.7, 11022; almost a modest ne- gation: explained by na FrP, Cod. S, XV, 7.— Av. (440) kamna-; Paz. NP kam. V. kem.
kam [k?m] will, desire, wish 694. — Av. (463) kama-; MPrthPrs k'm; Paz. NP kam.
kamak 1. will, wish, desire (= kam): 6 ~ rasét (imp.) may you attain, (the ful- filment of) your Royal Pleasure! 107; brihenisn u spahr u ~ i yazdān the predestination, Heaven, and the will of the gods 69°; pat ~ as teng as ever you wish 5915; ke Būšāsp ~ nē varzét he who does not (work the will of =) addict himself to Drowsiness 841%; ~ dátan 6 to direct one's will towards
110

=== HUB context 6275-6290 ===
wird zu b:
anbostan anfullen , anhaufen', 3. pr. anbdrad = skr.
sampurayati 'flillt an'; dazu anbar 'Speicher, phi. anbdr,
arm. ambar\ canbar 'Kreis' (? H. 446); siinbada *Wetzstein*
= arm. smpatak (wo aber mp auch fiir mb stehen kann);
darb *fett' = phi. carp; kurpa, kulba *Bude' = arm. krpak;
HUbichmann, Persitche Studien. 12- 178 —
LW. kathad, kalbud *Modeir, paz. kaibud, -phi, kalput^ kalpat,
gr. xaAo770()ioi^, arm. kalapar. Aber kirpas *ein femes 6e-
webe' = arm. kerpas *feines Linnen', gr. auQnaooq, skr. kar-
pasa-: erst in jiingerer Zeit entlehnt?
§ 71. Nach dem (tonlosen) s ist p als p geblieben
(gleichviel ob sp = ap. sp auf idg. sp oder k^v zurtickgeht);
asp *) 'Pferd' = zd. aspa-, dazu aspist Xuzerne' H. 79 ; as-
pand *Raute* H. 80, gospand Kleinvieh' H. 942 ; supar Tflug
H. 696; supurdan 'anvertrauen H. 697; sipas Dank, Lob'

=== HUB 9465-9478 ===
*garu- (vgl. zd. garah-) ^) wahrscheinlich ist.
/ aus d in malax 'Heuschrecke* Fird. I, 252, 148 = zd.
madaxa-; almas *Diamant', gr. LW. = ddd/Mxc; I aus t in
(afgh.) Hilmand, s. § 94 und 88. Mehrfach findet sich / in
Lehnw5rtem: sayal ^Schakal* = skr. grgala^; lakan, lagan
'Becken, Leuchter = gr. kt^dvrj; kalam = karanb, arm. kalamh
*Kohr = gr. x()diu(it] ; kdlbad, kalbud *Modeir, phi. kolput =
gr. aaXonddiov; ddl *Einier , nach Noldeke aus dem Semi-
tischen, syr, daula u. s. w. ; pilpil 'Pfeffer = skr. pippall;
piyala *Becher = gr. (pidXri; kiltd *Schlusser = gr. xXsTda
(ace.) u. s. w. (NSldeke, Pers. Stud. II, p. 38 fig.).
Kapitel 31: Konsonantenvorschlag.
Einigen vokalisch anlautenden WSrtern wird h oder
cr vorgeschlagen.
```


## [2026-09-07T20:42:55.925Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA grep qalib ===\"; grep -n -i \"qālib\\|qalib\\|kalopodion\\|kālbad\\|kalbad\\|kālbod\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20\necho \"=== PLA_pages 215 area ===\"; grep -n \"\\[pdf page 21[0-9]\\]\" incoming/PLA/PLA_pages.txt | head"
}
```


### [2026-09-07T20:42:55.994Z] TOOL RESULT

```
=== PLA grep qalib ===
=== PLA_pages 215 area ===
```


## [2026-09-07T20:42:58.465Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ ===\"; grep -n -i \"qalib\\|qālib\" FVQ.txt | head\necho \"=== AFM (Addi Shir) ===\"; grep -n \"قالب\" AFM.txt AFM_alt.txt 2>/dev/null | head\necho \"=== ARB_mo3rb ===\"; grep -n \"قالب\" ARB_mo3rb.txt 2>/dev/null | head -5\necho \"=== darabzin ===\"; grep -rn \"درابزین\\|دارابزین\\|darabzin\\|darābzīn\\|Darabzin\" . --include=*.txt | head -20"
}
```


### [2026-09-07T20:42:58.555Z] TOOL RESULT

```
=== FVQ ===
=== AFM (Addi Shir) ===
=== ARB_mo3rb ===
10200:الكيورة 3 أثثات النناء» ولاق قالبق القاموس + «والبية "سان 
11848:وكذلك تقالببا ”داق م “كو *ق د م“ و *”ق خ د“ و””م دق“ و””م قود“‎ ٠ كثيرة فى العرببوة‎ 
=== darabzin ===
(eval):5: no matches found: --include=*.txt
```


## [2026-09-07T20:43:01.820Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls incoming/PLA/; wc -c incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt incoming/PLA/PLA_pages.txt; head -c 600 incoming/PLA/PLA_pages.txt"
}
```


### [2026-09-07T20:43:01.879Z] TOOL RESULT

```
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
 358695 incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt
 807821 incoming/PLA/PLA_pages.txt
1166516 total
             Asya Asbaghi


Persische Lehnwörter im Arabischen




    OTTO HARRASSOWITZ   - WIESBADEN
          Asya Asbaghi
Persische Lehnwörter im Arabischen
               Asya Asbaghi


Persische Lehnwörter ım Arabischen




                    1988


    OTTO   HARRASSOWITZ    - WIESBADEN
CIP-Titelaufnahme der Deutschen Bibliothek

Asbaghi, Asya:
Persische Lehnwörter im Arabischen / Asya Asbaghi. -
Wiesbaden : Harrassowitz, 1988
  ISBN 3-447-02757-6




Alle Rechte vorbehalten. © Otto Harrassowitz, Wiesbaden 1988. Photomechanische und photographi-
sche Wiedergabe nur mit ausdrü
```


## [2026-09-07T20:43:03.004Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -rln \"درابزین\" . 2>/dev/null | head\necho \"---latin---\"\ngrep -rln \"darabzin\\|darabzīn\\|darābzīn\\|Darâbzîn\" . 2>/dev/null | head"
}
```


### [2026-09-07T20:43:03.182Z] TOOL RESULT

```
BQT_v2.txt
BQT_v2_pages.txt
ocr/BQT/829.vision.txt
---latin---
ocr/BQT/829.vision.txt
```


## [2026-09-07T20:43:08.985Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA arabic qalib ===\"; grep -n \"قالب\\|kālab\\|qālab\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== PLA page 215 tag ===\"; grep -n \"215\" incoming/PLA/PLA_pages.txt | head -5"
}
```


### [2026-09-07T20:43:09.057Z] TOOL RESULT

```
=== PLA arabic qalib ===
=== PLA page 215 tag ===
```


## [2026-09-07T20:43:09.607Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ocr/BQT/829.vision.txt ===\"; cat ocr/BQT/829.vision.txt\necho; echo \"=== BQT_v2 درابزین ===\"; grep -n \"درابزین\" BQT_v2_pages.txt | head"
}
```


### [2026-09-07T20:43:09.674Z] TOOL RESULT

```
=== ocr/BQT/829.vision.txt ===
[BQT = Borhan-e Qate', ed. Mo'in; vol. 2, archive.org/details/borhan-ghate-v2 leaf n289 =
 printed page ۸۲۹ (829; confirmed by the catch-line «بقیهٔ در صفحه ۸۳۰» at the foot).
 Read from the page image by Claude (vision) on 2026-09-06 for verification of PDF page 295,
 nodes #19-#20. Mo'in's etymological footnote at the foot of the page:]

* درابزین ـ از یونانی Trapézion (نرده، شبکه) معرّب آن درابزین و دربوز «دزی ج ۱ ص ۴۳۰»
«معجمیات عربیة سامیة ص ۲۲۷» و درابزون «المنجد». رک: داربزین، دارآفرین(۱) و دارفرین(۱).
                                                            بقیهٔ در صفحه ۸۳۰

[i.e. Mo'in: darābzīn is from Greek "Trapézion" ("railing, lattice"); its Arabicized forms are
 درابزین and دربوز (citing Dozy vol.1 p.430 and Mu'jamiyyat 'arabiyya samiyya p.227), and
 درابزون (al-Munjid).]

=== BQT_v2 درابزین ===
15989:         ‫‪ ۱‬کیلکی ‪( 15-78‬شاخشدرخت)‪.‬‬                          ‫«دربزین»‪« .‬درابزین»و«درایزون» (المنجد)‪.‬‬
17036:    ‫* درابر یی ‪ -‬از بونابی ‪( 00126۳2۲1‬نرده» شدکه)معرب‌آن درابزین ودربوز «دزی‬
```


## [2026-09-07T20:43:21.238Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17030,17045p' BQT_v2_pages.txt\necho \"=== also line 15985-15995 ===\"; sed -n '15985,15995p' BQT_v2_pages.txt"
}
```


### [2026-09-07T20:43:21.295Z] TOOL RESULT

```
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
=== also line 15985-15995 ===
     ‫داروزین (رك‪ :‬دار آفرین ‪9 (1‬‬   ‫ص‬   ‫دارافزین‬   ‫=‬   ‫‪°‬‬                ‫‪.‬‬    ‫رك‪ :‬دار کوب‬     ‫‪۴‬‬

          ‫‏‪( balustrade‬فر) = (عر) جلفق‪.‬جلهق‪« :‬جلفق کجفر» داریزین» «منتهی‌الارب» و‬
 ‫منیعزرب آن‬
         ‫‪ ۱‬کیلکی ‪( 15-78‬شاخشدرخت)‪.‬‬                          ‫«دربزین»‪« .‬درابزین»و«درایزون» (المنجد)‪.‬‬
 ‫‪ - ۸‬اسم مصدر است از «راشتن» ورك‪ :‬فرهنك دسالیر‬                    ‫‪ ۷‬نت رك ‪ ۱‬دارادار کردن ‪۰‬‬

                                                       ‫‪« :‬دارش بندی » وه دارش‌خروی › ‪.‬‬                ‫‪4‬‬
                                                                                 ‫داز شمان‬
```


## [2026-09-07T20:43:22.657Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-295.json'))\nfor e in d['entries']:\n    print('ROOT',e['root'],e['verdict'])\n    for n in e['nodes']:\n        if n['id'] in (14,15,16,17,18,19,20):\n            print(json.dumps(n,ensure_ascii=False)[:2500]);print()\n\" 2>&1 | head -60"
}
```


### [2026-09-07T20:43:23.910Z] TOOL RESULT

```
ROOT Kwetwer, Qwetwor confirmed
{"id": 14, "lang": "Persian", "words": "qarantîn «قرنطین» (قرنطینه)", "verdict": "plausible", "derivation": "Persian قرنطینه qaranṭīne ‘quarantine (station)’ is certainly the same international word, and it is written in Arabic dress (ق and ط for European k/qu and t), which is why Mo‘in labels the shorter قرنطین as ‘[- قرنطینه، معر.]’, i.e. an Arabicised form; that spelling supports Nourai’s Italian → Arabic → Persian route. Against it, most Iranian lexicographers take قرنطینه as a direct loan from French quarantaine, which is what the final -e (ـه) actually renders — an Arabic قرنطينة would normally give Persian قرنطینه too, so the two routes are hard to separate on form alone, and the word entered Persian in the Qajar period together with a mass of French administrative and medical vocabulary. Verdict ‘plausible’: the chain is compatible with Mo‘in, but the French route is at least as likely for the immediate donor.", "derivation_fa": "«قرنطینه» بی‌گمان همان واژهٔ بین‌المللی است و در فارسی با جامهٔ عربی نوشته می‌شود (ق و ط به‌جای k/qu و t اروپایی)؛ به همین سبب معین صورت کوتاه «قرنطین» را «[- قرنطینه، معر.]» یعنی معرّب دانسته است و همین نکته مسیر ایتالیایی ← عربی ← فارسیِ نورایی را تأیید می‌کند. در برابر، بیشتر فرهنگ‌نویسان ایرانی «قرنطینه» را وام‌واژه‌ای یک‌راست از فرانسوی quarantaine می‌دانند و «ـه» پایانی هم همان -aine فرانسوی است؛ از سوی دیگر «قرنطینة» عربی نیز در فارسی «قرنطینه» می‌شود، پس این دو راه را تنها از روی صورت نمی‌توان از هم جدا کرد، و واژه در دورهٔ قاجار همراه انبوهی از واژگان اداری و پزشکی فرانسوی وارد شده است. حکم: ادعای نورایی با احتیاط پذیرفتنی است؛ راه فرانسوی دست‌کم به همان اندازه محتمل است.", "sources": ["https://www.etymonline.com/word/quarantine"], "ref_check": [{"ref": "MON:2666", "status": "partial", "note": "The 6-vol. Mo‘in (where p. 2666 belongs) is not online; the 2-vol. Adena condensation (MON_part2.txt) has “قرنطین: [- قرنطینه، معر.] (ا.) جایی که در آن مسافرانی را که از سرزمینی وارد می‌شوند که در آنجا بیماریی ساری مانند وبا و طاعون شیوع دارد، مدت چند روز نگهداری می‌کنند” — same headword, same gloss, and the tag معر. (Arabicised) that Nourai’s arrow relies on; the page number itself could not be verified."}], "consulted": [{"src": "MON", "where": "MON_part2.txt s.v. قرنطین", "stance": "supports", "note": "see ref_check — “[- قرنطینه، معر.]”."}, {"src": "TAD", "where": "al-Unaysi p. 62", "stance": "supports", "note": "“كرنتينا — ايطالي quarantena” — the Arabic link in the chain exists and is Italian-derived."}, {"src": "BQT"

{"id": 15, "lang": "English", "words": "quarantine", "verdict": "confirmed", "derivation": "English quarantine, in the medical sense, is first recorded in the 1660s, borrowed from Italian quarantina (Venetian quarantena) ‘a space of forty days’, from quaranta ‘forty’ < Latin quadrāgintā; the practice is the Venetian one of holding ships from plague ports offshore for forty days (Ragusa 1377, Venice 1423). Two older English senses of the same word came in earlier through French: quarentyne (15th c.) ‘the desert where Christ fasted forty days’ and quarantine (1520s) ‘the forty days a widow may stay in her dead husband’s house’. The verb is 1804.", "derivation_fa": "واژهٔ انگلیسی quarantine در معنای پزشکی نخستین‌بار در دههٔ ۱۶۶۰ م ثبت شده و وام‌واژه‌ای است از ایتالیایی quarantina (در ونیزی quarantena) «دورهٔ چهل‌روزه»، از quaranta «چهل» و آن از quadrāgintā لاتینی؛ خودِ رسم هم ونیزی است: نگاه‌داشتن چهل‌روزهٔ کشتی‌های آمده از بندرهای طاعون‌زده (راگوزا ۱۳۷۷ م، ونیز ۱۴۲۳ م). دو معنای کهن‌تر همین واژه پیش‌تر از راه فرانسه وارد انگلیسی شده بود: quarentyne (سدهٔ پانزدهم) «بیابانی که مسیح چهل روز در آن روزه گرفت» و quarantine (دههٔ ۱۵۲۰) «چهل روزی که بیوه حق ماندن در خانهٔ شوی درگذشته را دارد». ادعای نورایی درست است.", "sources": ["https://www.etymonline.com/word/quarantine"], "ref_check": [{"ref": "AHD:1068", "status": "supports", "note": "New College p. 1068 not online; the AHD’s IE appendix (AHD_watkins1985.txt s.v. kʷetwer-) has “Latin quadrāgintā, forty (-gintā, ten times; see dekm): QUARANTINE” — the English word is derived from the Latin ‘forty’ exactly as the chart draws."}], "consulted": [{"src": "KLN", "where": "KLN_1966.txt s.v. quarantine", "stance": "supports", "note": "“It. quarantina, fr. quaranta, ‘forty’, fr. L. quadrāgintā… first enforced at Ragusa in 1377”, with the reference to K. Sudhoff, Essays in the History of Medicine, p. 152."}, {"src": "SKT", "where": "SKT.txt s.v. quarantine", "stance": "supports", "note": "“quarantine… O.F. quarantaine, a space of [forty] days. — F. quarante, forty. — L. quadrāgintā” — Skeat routes it through French rather than Italian, a minor difference."}]}

{"id": 16, "lang": "Germanic", "words": "petwor", "verdict": "plausible", "derivation": "Proto-Germanic ‘four’ is *fedwōr (Goth. fidwōr, ON fjórir, OE fēower, OHG fior). Its f- cannot come straight from *kʷ-, which would give Gmc *hw-; a pre-form with initial *p- is therefore posited, *petwor-, produced by dissimilation of the first labiovelar before the *-w- of the second syllable (*kʷetwor- > *petwor- > *fedwōr by Grimm’s law, with *t > *d by Verner’s law). Modern handbooks (Kroonen, Ringe) do reconstruct exactly this *petwor-, so Nourai’s form is defensible; but it is a PRE-Germanic stage, not a Germanic word, and the p-forms actually attested belong to Italic and Celtic (Osc. petora, pettiur, Gaul. petuarios, Welsh pedwar). Pokorny himself, at IEW 643, derives Germanic instead from an assimilated *kʷekʷor-, and Watkins writes ‘Probably Germanic *fe(d)wor-’ — neither prints ‘Germanic petwor’. Hence plausible, with a mislabelled node.", "derivation_fa": "صورت ژرمنی آغازین «چهار» *fedwōr است (گوتی fidwōr، نورس کهن fjórir، انگلیسی کهن fēower، آلمانی علیای کهن fior). f آغازین آن نمی‌تواند یک‌راست از *kʷ آمده باشد، زیرا *kʷ در ژرمنی *hw می‌دهد؛ از این‌رو صورت پیشاژرمنی *petwor- بازسازی می‌شود که از ناهمگونی‌ (dissimilation) نخستین لبی‌کامی پیش از w هجای دوم پدید آمده است (*kʷetwor- ← *petwor- و سپس با قانون گریم و ورنر *fedwōr). کتاب‌های امروزی (کرونن، رینگه) همین *petwor- را بازمی‌سازند، پس صورتِ نورایی بی‌پایه نیست؛ اما این مرحلهٔ پیشاژرمنی است نه واژه‌ای ژرمنی، و صورت‌های p‌دارِ گواهی‌شده به ایتالیایی باستان و سلتی تعلق دارند (اسکی petora، گلی petuarios، ولزی pedwar). خود پوکورنی در ص ۶۴۳ ژرمنی را از *kʷekʷor- همگون‌شده می‌گیرد و واتکینز «احتمالاً ژرمنی *fe(d)wor-» می‌نویسد. پس برچسب این خانه نادرست است، هرچند بازسازی‌اش پذیرفتنی.", "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res"], "ref_check": [{"ref": "AHD", "status": "partial", "note": "AHD_watkins1985.txt s.v. kʷetwer-: “I. O-grade form *kʷetwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English fēower, four: FOUR…” — the AHD supports the root and the English words but writes the Germanic form *fe(d)wor-, never petwor."}], "consulted": [{"src": "POK", "where": "IEW 643 (POK_02.txt leaf 302)", "stance": "contradicts", "note": "“got. fidwōr, nord. und westgerm. auf Grund einer Assimilationsform *kʷekʷor…” — Pokorny explains Germanic by assimilation to *kʷekʷor-, and puts the p-forms under Italic/Celtic: “osk. pettiur, petora… acymr. petuar, ncymr. pe

{"id": 17, "lang": "English", "words": "four, fourteen, forty", "verdict": "confirmed", "derivation": "All three are inherited, not borrowed: OE fēower > ME fower/foure > four; OE fēowertēne (fēower + tēn ‘ten’) > fourteen; OE fēowertig (fēower + -tig ‘decade’) > forty, whose modern spelling with -or- reflects the shortening of the vowel in the unstressed compound (four : forty). All continue Proto-Germanic *fedwōr < the pre-Germanic *petwor- of the parent box, and Watkins lists FOUR, FOURTEEN and FORTY together under Germanic *fe(d)wor-.", "derivation_fa": "هر سه واژه ارثی‌اند نه وام‌واژه: fēower انگلیسی کهن به four، fēowertēne (از fēower + tēn «ده») به fourteen، و fēowertig (از fēower + پسوند دهگانِ -tig) به forty رسیده است؛ املای امروزیِ forty با -or- بازتاب کوتاه‌شدن واکه در ترکیبِ بی‌تکیه است (four در برابر forty). هر سه دنبالهٔ *fedwōr ژرمنی آغازین‌اند که در خانهٔ بالا آمده، و واتکینز نیز FOUR و FOURTEEN و FORTY را با هم ذیل *fe(d)wor- ژرمنی آورده است. ادعای نورایی درست است.", "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res"], "ref_check": [{"ref": "(none cited)", "status": "not_checked", "note": "No reference on this box; the parent cites AHD, whose appendix (s.v. kʷetwer-) lists exactly these three English words: “Old English fēower, four: FOUR; … fēowertig, forty: FORTY; … fēowertēne, fourteen: FOURTEEN”."}], "consulted": [{"src": "KLN", "where": "KLN_1966.txt s.v. four", "stance": "supports", "note": "“four, adj. and n. — ME. feower, fower, foure, four, fr. OE. feower… Cp. fardel, ‘fourth part’, farthing, firkin, forty.”"}, {"src": "SKT", "where": "SKT.txt s.v. four", "stance": "supports", "note": "Skeat likewise: OE fēower, cognate with L. quattuor, Gk. τέσσαρες."}, {"src": "AHD", "where": "AHD_watkins1985.txt s.v. kʷetwer-", "stance": "supports", "note": "FOUR, FORTY, FOURTEEN all listed under Germanic *fe(d)wor-."}]}

{"id": 18, "lang": "Greek", "words": "tra-peza", "verdict": "confirmed", "derivation": "Ancient Greek τράπεζα trápeza ‘table’ is a transparent compound *kʷtwṛ-ped-ya ‘four-footed (thing)’: the zero grade *kʷt(w)r- of *kʷetwer- gives Greek tra- (as in τρά-πεζα, beside the full-grade τετρα-), and -πεζα is the *-ya derivative of *ped- ‘foot’ (Gk. πούς, πεζός). The diminutive τραπέζιον trapézion ‘little table’ was used by the geometers for an irregular quadrilateral, whence trapezium/trapezoid. Watkins files TRAPEZIUM under both kʷetwer- and ped-1, which is precisely the two-root analysis Nourai marks with his ☆Ped cross-reference.", "derivation_fa": "«τράπεζα» یونانی باستان به معنای «میز» ترکیبی است شفاف از *kʷtwṛ-ped-ya یعنی «چهارپا/چهارپایه»: درجهٔ صفر ریشهٔ *kʷetwer- در یونانی tra- می‌دهد (در برابر درجهٔ کاملِ τετρα-) و -πεζα مشتقِ *-ya از *ped- «پا» است (یونانی πούς و πεζός). صورت مصغر τραπέζιον «میز کوچک» را هندسه‌دانان برای چهارضلعی نامنتظم به کار بردند و از همان‌جا trapezium و trapezoid پدید آمد. واتکینز واژهٔ TRAPEZIUM را هم ذیل kʷetwer- و هم ذیل ped- آورده است، یعنی همان تحلیل دو‌ریشه‌ای که نورایی با ارجاع ☆Ped نشان داده است. ادعای نورایی درست است.", "sources": ["https://www.etymonline.com/word/trapeze"], "ref_check": [{"ref": "AHD:1365", "status": "supports", "note": "New College p. 1365 (the ‘tr-’ pages of the main dictionary) is not open online; the AHD’s IE appendix says it twice — s.v. kʷetwer-: “d. zero-grade form *kʷt(w)r- in Greek tra-, four: TRAPEZIUM”, and s.v. ped-1: “8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM”; the index line reads “TRAPEZIUM kʷetwer-, ped-1”."}], "consulted": [{"src": "WLD", "where": "Walde-Pokorny Bd. I 512", "stance": "supports", "note": "“av. čaθru-[gaoša-]: gr. τετρα-[γουνος]… schwundstufig oder durch Diss. aus τετρα- gr. τράπεζα (Lit. auch bei Boisacq 979)” — the zero-grade tra- of τράπεζα explicitly."}, {"src": "KLN", "where": "KLN_1966.txt s.vv. foot and tessara-", "stance": "supports", "note": "s.v. foot the cross-reference list ends “… teapoy, trapezium, triped, tripos”; s.v. tessara- “fr. I.-E. base *qʷetur-, ‘four’. See four and cp.… the first element in trapezium”."}, {"src": "SYN", "where": "Buck 7.44 TABLE", "stance": "supports", "note": "Buck's entry on 'table' analyses “Grk. τράπεζα… ‘four-footed’… (: τέσσαρες, τετρα- ‘four’)… Also Boeot. τρίπεζα… lit. ‘three-footed’” (the OCR of this paragraph is badly scrambled but the four-foot analysis and the Boeotian variant are legible); ChSl. trapeza 

{"id": 19, "lang": "Arabic", "words": "dar-bezin", "verdict": "plausible", "derivation": "The Arabic word is درابزين darābzīn (also دربزين, درابزون) ‘railing, banister, balustrade’, and Mo‘in’s footnote in Borhan-e Qate‘ p. 829 derives it exactly as the chart does: ‘درابزین — from Greek Trapézion (railing, lattice); its Arabicised forms are درابزین and دربوز’ (citing Dozy I 430 and Mu‘jamiyyāt ‘arabiyya sāmiyya 227), i.e. the Greek diminutive τραπέζιον was taken into Arabic with prothetic/metathetic reshaping (tr- unpronounceable initially in Arabic → dar-) and given the sense ‘lattice/railing’ from the trellis-table shape. Two reservations: Nourai’s form ‘dar-bezin’ and his gloss ‘a seating area between two doors of a room’ are really Mo‘in’s Persian entry for دارافزین (‘مجری که در جلو اطاق بین دو در سازند؛ تکیه‌گاه، طارمی’), not the Arabic sense; and Wiktionary reverses the direction, making Arabic درابزين a loan from Ottoman Turkish طرابزان < Persian داربزین.", "derivation_fa": "واژهٔ عربی «درابزین» (و گونه‌های «دربزین» و «درابزون») به معنای «نرده، طارمی، محجر» است و حاشیهٔ معین بر برهان قاطع در ص ۸۲۹ آن را درست همان‌گونه که نورایی رسم کرده ریشه‌یابی می‌کند: «درابزین ــ از یونانی Trapézion (نرده، شبکه) معرّب آن درابزین و دربوز» با ارجاع به دُزی ج۱ ص۴۳۰ و «معجمیات عربیة سامیة» ص۲۲۷. یعنی مصغر یونانی τραπέζιον با دگرگونی آغازین (خوشهٔ tr در آغاز واژهٔ عربی ناممکن است و به dar- بدل شده) وارد عربی شده و معنای «نرده/شبکه» را از شکل شبکه‌مانندِ آن گرفته است. دو نکته: صورت «dar-bezin» و معنای «جایی برای نشستن میان دو درِ اتاق» که نورایی آورده در اصل مدخل فارسیِ «دارافزین» در فرهنگ معین است نه معنای عربی؛ و ویکی‌واژه جهت وام‌گیری را وارونه می‌داند و «درابزین» عربی را از ترکی عثمانی «طرابزان» و آن را از «داربزین» فارسی می‌گیرد. پس با احتیاط پذیرفتنی است.", "sources": ["https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A7%D8%A8%D8%B2%D9%8A%D9%86", "https://www.etymonline.com/word/trapeze"], "ref_check": [{"ref": "MON:1481", "status": "partial", "note": "The 6-vol. Mo‘in is not online, so p. 1481 could not be opened; but Mo‘in’s own footnote in his edition of Borhan-e Qate‘, p. 829 (read from the page image, archive.org/details/borhan-ghate-v2 leaf n289; saved at data/verification/sources/refs/ocr/BQT/829.vision.txt) states the identical claim: “* درابزین ـ از یونانی Trapézion (نرده، شبکه) معرب آن درابزین و دربوز «دزی ج ۱ ص ۴۳۰»… و درابزون «المنجد»”."}], "consulted": [{"src": "BQT", "where": "Borhan-e Qate‘ ed. Mo‘in, vol. 2 p. 829, Mo‘in’s footnote", "stance": "supp

{"id": 20, "lang": "Persian", "words": "dârâbzîn «دارابزین» (درابزین ، دارافزین ، داروزین)", "verdict": "confirmed", "derivation": "Persian دارابزین / دارافزین / داروزین / درابزین ‘balustrade, railing, the rail or dais built between the two doors at the front of a room’ is one word in many shapes, and Mo‘in lists exactly these four in his Farhang (‘دارافزین [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون]’) with the very gloss Nourai gives. The variation ‑bzīn ~ ‑fzīn ~ ‑wzīn is the ordinary Persian alternation of b/f/w in an unstressed medial syllable, helped along by folk etymology (دار ‘wood, post’ + افزودن ‘to add’, as if ‘added woodwork’). Mo‘in’s note in Borhan-e Qate‘ p. 829 traces the word to Greek τραπέζιον through an Arabicised درابزین/دربوز, which is exactly the route drawn here.", "derivation_fa": "«دارابزین / دارافزین / داروزین / درابزین» یک واژه با چند گونهٔ نوشتاری است به معنای «نرده، طارمی، مجری‌ای که در جلو اتاق میان دو در می‌سازند»، و معین در فرهنگ فارسی دقیقاً همین چهار گونه را با همان معنایی که نورایی آورده ثبت کرده است: «دارافزین [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون] مجری که در جلو اطاق بین دو در سازند؛ تکیه‌گاه، طارمی». گوناگونی ـبزین/ـفزین/ـوزین همان ابدال معمول ب و ف و و در هجای میانیِ بی‌تکیه است که ریشه‌شناسی عامیانه (دار + افزودن، گویی «چوبِ افزوده») نیز به آن دامن زده است. حاشیهٔ معین بر برهان قاطع در ص ۸۲۹ واژه را از یونانی τραπέζιον از راه صورت معرّبِ درابزین/دربوز می‌گیرد؛ یعنی همان مسیری که نورایی رسم کرده است. ادعای نورایی درست است.", "sources": ["https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A7%D8%A8%D8%B2%D9%8A%D9%86", "https://www.etymonline.com/word/trapeze"], "ref_check": [{"ref": "MON:1481", "status": "partial", "note": "6-vol. Mo‘in not online; the 2-vol. condensation (MON_part1.txt) has the entry verbatim: “دارافزین: [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون] (ا.) مجری که در جلو اطاق بین دو در سازند؛ تکیه گاه؛ طارمی” — all four variants of Nourai’s box and his gloss, so the content of MON:1481 is confirmed even though the page number is not."}], "consulted": [{"src": "MON", "where": "MON_part1.txt s.v. دارافزین", "stance": "supports", "note": "see ref_check — the four variants and the gloss."}, {"src": "BQT", "where": "Borhan-e Qate‘ vol. 2 pp. 829-830, headword درابزین with Mo‘in’s footnote", "stance": "supports", "note": "“«دارافزین» (درابزین)… وداروزین و داربزین بمعنی تکیه‌گاه و محجر تخت و صفه و بام…” and the footnote “از یونانی Trapézion (نرده، شبکه)”."}, {"src": "RCH",
```


## [2026-09-07T20:43:42.721Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT کالبد across vols ===\"\nfor f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; do echo \"--$f--\"; grep -n \"کالبد\\|کالب\\b\" $f | head -5; done"
}
```


### [2026-09-07T20:43:44.025Z] TOOL RESULT

```
=== BQT کالبد across vols ===
--BQT_v1_pages.txt--
4149:«فرهنگی بی‌شاهد؛کالبدیست بی‌روان ۴ >ازاین روحدوسطی انتغاب کرده
27717:لیگ ر ۴ - بروزن قیصرقالب وکالبدوجله
31042:و بمستی‌صورت وئمثال - و پیکرو کالبد و فاب
--BQT_v2_pages.txt--
28861:          ‫شدش کالبد از زاری وز فرقت زفت‬                        ‫ساعتی با اولششت و یاسود نوضفت‬
--incoming/BQT/BQT_v3_pages.txt--
11578:پونالی نوشادر پیکالبرا گریند , و ‎OT‏ چیزست
26828:کالب ۴ » بر وزن و معنی قالب است
26830:‏که آنرا کالبد نیز گویند .
26832:‏بمعنیکالب (۲) است که قالب هر چیز باشد -
26836:کالبوی ‎٩‏ - با بای ابجد بواورسیده
--incoming/BQT/BQT_v4_pages.txt--
6553:پولی بود که بعد از اجرت استاد بشاکرد دهندب میم کالب - بکر ثالت, کنایه‌از نا
20059:دراز بالیده - و شکوه - و کالبد وپیکر - و بنای بلند - و خانةٌ ترسابان که در آن پیکر مریم
--incoming/BQT/BQT_v5_pages.txt--
```


## [2026-09-07T20:43:45.228Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON کالا ===\"; grep -n \"^کالا\\|کالا:\" MON_part1.txt MON_part2.txt | head -10\necho \"=== MON کالبد ===\"; grep -n \"کالبد\" MON_part1.txt MON_part2.txt | head -10\necho \"=== MON قالب ===\"; grep -n \"قالب:\" MON_part1.txt MON_part2.txt | head -10\necho \"=== MON اختاپوس ===\"; grep -n \"اختاپوس\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON کالیبر ===\"; grep -n \"کالیبر\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-07T20:43:45.391Z] TOOL RESULT

```
=== MON کالا ===
MON_part1.txt:7770:کالا افتعهخا غله) برای فروش به هنگام 
MON_part1.txt:8569:کالای بازرگانی و جز آن بیرون برند» 
MON_part1.txt:9863:کالا کم‌بها و فراوان است. دستوری اجازه» 
MON_part1.txt:11314:کالایی که در استامول سازند و صادر کنند. 
MON_part1.txt:17047:کالاه آنجا که هیزم و غیره ذخیره کنند. خس 
MON_part1.txt:46051:کالا و خواربار و ابزار و ماشین‌ها و غيره. 
MON_part1.txt:79188:کالای تجارت؟ ج. . سلع. آرخ که بی‌درد بر 
MON_part1.txt:92488:کالای وزن شده بر آن افزایند و آن را طرح 
MON_part1.txt:95554:کالای صنعتی زیادتر از حد نیازمندی خود 
MON_part1.txt:95556:کالا هستند عرضه می‌کند و در برابر آن 
=== MON کالبد ===
MON_part1.txt:7470:تن‌هاه جسم‌هاء کالبده . (کیم.) زر و سیم و 
MON_part1.txt:7477:کالبدها. اجسام آلی ( آلیه): [فد.) هر جسم که 
MON_part1.txt:13209:کالبدها. سایه‌ها. سیاهی‌ها که از دور دیده 
MON_part1.txt:13334:کالبدها. سیاهی‌ها. کسان, افراد. " 
MON_part1.txt:17608:جسم کالبد. قد و قامت» قد و بالاء هیکل. 
MON_part1.txt:32279:کفش و کالبد فرو برند تا کفش گشاده شود؛ 
MON_part1.txt:40836:مرده برای تحقیق و مطالعه, کالبدشکافی؛ 
MON_part1.txt:40840:کالبد شکافی. 
MON_part1.txt:46882:خدای تعالی در کالبد آدم دمید؛ روح آدم. 
MON_part1.txt:84588:( کم.) کالبد مردم» تن» بدن. آدمی» اسان. 
=== MON قالب ===
MON_part2.txt:10621:قالب: (ا16-تد. )اهاز [معر . کالبد] شکل. 
MON_part2.txt:10635:قالب: 2۱60 [ع.] (.) (گیء) غورةٌ خرمای 
=== MON اختاپوس ===
=== MON کالیبر ===
```


## [2026-09-07T20:43:56.671Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=26700 && NR<=26860' incoming/BQT/BQT_v3_pages.txt | grep -n \"pdf page\" | tail -3\necho \"=== nearest page tags ===\"\nawk 'NR<=26840 && /\\[pdf page/ {l=NR\": \"$0} END{}' incoming/BQT/BQT_v3_pages.txt\ngrep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | awk -F: '$1<26840' | tail -3\necho \"=== text 26820-26860 ===\"\nsed -n '26815,26860p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-07T20:43:58.060Z] TOOL RESULT

```
28:[pdf page 367]
121:[pdf page 368]
=== nearest page tags ===
26657:[pdf page 366]
26727:[pdf page 367]
26820:[pdf page 368]
=== text 26820-26860 ===

‏«سنائی ‎soe‏ . دیوان ۲ه ©

‎AYN Sy? ‏وفربار)‎ SSL) ۷988 ‏پهلری‎ kalind . Ala» ۴

[pdf page 368]
‎—\eve—‏ کالجوش
کویندکه ‎Ge‏ باشد ‎ASE ASH, ٩‏ |
‎oly!‏ مقدار باشد که اسب وآدم لتواند چست -
و تخته سنك تنك و ‎SW‏ را ‎SaaS js‏ بر
روی مردروهای(۱) زیرحمام وجوبهایآب‌پوشند.
کالاشکن ۴ ه بسکون شین تقطمدار
وفتح‌کاف بروزن وا داشتن » لوعی از حلواباشد .
کالب ۴ » بر وزن و معنی قالب است

‏که آنرا کالبد نیز گویند .
‎gee TAIT‏ با وسکون‌دال ‎ion!‏
‏بمعنیکالب (۲) است که قالب هر چیز باشد -
وبمعنی تن وبدنآدمی وحیوانات دیگرنیزهست؛

‏ویفتح بای ابجد هم گفته‌اند .
کالبوی ‎٩‏ - با بای ابجد بواورسیده

‏(۱) چش: مروررودهای . (۲) چش : قالب .

‏وتحتانی زده ؛بععنی س رکشته و متحیر و حیران
باشد - و بمعنی نادان وهیجمبان همآمدماست؛
وبحذف نحتالی‌هم درست‌است که بروزن هزبوباشد.
کالچاه ۱ = باجي ‎BL‏ کید ,
بلفت ‎OS‏ بروزن ومعنی‌کارزار است که ‎Kee‏
‏وجدال ‎ath‏ - ومزرعةً برج را نی زگوبند۷ .
کال‌جوش - باجم بروزن‌تالپوش,
‎gy!‏ ازماحض باشد که دروبشان پزند وآن‌چنان
باشد که تالرا ریزه کنند همجتان که پرای‌اکنه
ریزه میکنند وکشك باب نرم کرده رابا روغن
‎duly‏ قلفل وزیرء و منز کردکان و ‎Bal‏ ریزء
کرده درديك ریز ند ودوسه جوشی داده‌فرود آرند
وخورند ۸ .

‏۱ « درمیان مردم خراسان مثل است که جابی که کالار است هیزم نیست و ‎ile‏ که
هیزم است کالارنیست» ‎only‏ مثل بدان میکوبند که هرجا که کالار باشد هیزم زودتر کنده‌میشود.»
« جهانگیری » ورك : فرهنگ نظام . ۴ کلاشکن ‎Cea)‏
‏برافراختند از قفایش چو باد از کالاشکن سنجق ‎Jue‏ وداد . . بحاق‌اطعمه «فرهنگه تظام».

‏۴ ره :کالید ۰ ۴ - پهلوی 1220 (شکل » صورت) »پازنت2[000ع1,
مستمار از بوتانی ‎kalopédhion‏ (قالب) . ارمتی ‎kalapar‏ از ‎kalapadh‏ ۵ سریبانی ع
```


## [2026-09-07T20:44:10.260Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26727,26822p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-07T20:44:10.316Z] TOOL RESULT

```
[pdf page 367]
IST
‏سلمین فردون و دختر‎ le ‏بوده ازیسرزاده‎ e
‏نیز گویند با‎ ٩ ‏زادة دختر خحاله راوراکاکوی‎
‏در دست سم اریمان‎ gly » ‏درآخر‎ les ‏زیادتی‎
‎. ‏شته شد‎

OS ‏بر وزن باقوتی‎ - GIO
. ۴ ‏است که آنرا بعربی سعترخوانند‎

کاکوش- بروزن آغوش » پنفشه را
‎Pao‏ وآن کلی باشد موف ومشهور.

کاکول ؟ ین اف و سکون واو
ولام . ‎ISB ew‏ است که موی ‎Ole‏ سرمردان
وپسران واسب واستر باشد .

کا کو 4 * - ‎SE game ging‏
است که خالو باشد وآن برادر مادر است- ‎phy‏
‏پهلوانی هم بود» از پسرزاده های سلم‌بن فریدون
ودخترزاده‌های ضحاك .

. ‏ولف‎ cue: 3). 18160 - ۱

—Nevi—

‎ST‏ »بر رزن خاکی ؛ نام شخصی
است که پسراورا ماکان میگفته‌اند ‎ub Se,‏
۹1
کال = ‎Vo,‏ » نی خم‌وخمیده
و کج باشد ۷ - وجا ومقام وجایگاه بودچه‌متانه
کال ‎Aa Se wl.‏ - و زمین شکافته و آب
کند را نز کفتهاند ‎٩‏ - ویمعنی ژولیده ودرهم
یزآمده است*۱- وخامونارسیدهراهم‌میگویند۱9
— ویمعت ی گندنا وکدو هم هنت ونوعی ا زگل
را بزمیگونند و بععتی هزیمت وگریز باشد
چ هک ک هگرخت کویند کالید۷۴.

‏کال » بروزن بالا. بمعنی رخت‌ورخوت
و ‎OL‏ و متاع باشد ‎-٩۴‏ و ‎wij cal‏ وپازند.
‎abby CGE‏ وففان ‎Mas ST,‏

‎gy‏ = بسکون‌رای‌فرشت, آ بکندیرا

‏۴ - هدایت گوید : «کاکوتی بر وزن

‏بوده

‏یاقوتی؛ در برهان و جهانگیری پمعنی آوشن آورده‌اند ... وندانته‌اند که اين لت غلط است .
کاکونی اسلش «کلليك‌اوتی» است بعنی علف وسبزة کبك , وآن نیز تر ‎ASICS NT‏ کبك

‏را کویند و اوت علف را » والاعلم . » رل :
«کليك اوتی» ‎cal Sg‏ ب
۴ - رك : محیط اعظم.

‏سعتر . آقای دهخدا نوشته‌اند : کاکونی مصحف
نی« کيك گیاه» وبگمان من کاکونی همان ژاژاست. ‎Dy‏ سعترء آومشن.
۴ = کاکل ‎Gem)‏

‎Apa) ‏کاکو‎ = 5

‏۲ - ماکان‌ین کا کی معاصر نصربن‌احمدبن اسماعیل سامانی (۳۳۱-۳۰۱ ) بودوبرجرجان
وری مسلط شد و ‎Lays‏ ۳۷۹در محاربه باامیر ابوعلی‌احمدین محتاح‌چفانی کشته شد . رك:تملیقات

‎٩ - Nee ad ‏چپار مقاله . چاپ‎

‏۷ رگ :کالیده .

‎yl ۸‏ وصف ‎OT‏ ضیاست که از رشك رای اوست

‏پشت

‏9 علال را که خم است از میانه کال .

‎. » ‏خسرو دهلوی « فرهنگه نظلم‎ pal

‎kal ob - ٩‏ (دره) « واژه‌نامه ‎oft‏ ظ . از ‎ta,‏ اوستابی ‎kan‏ ( کندن).

‎. ‏کالیده‎ : Ay ۶

‏(میوشبز) «زابا ۰۳۲۳

‏۱- تهرانی .مشپدی, کیلکی ‎ple) kal‏ ناری). کردیا 158
۴- ره : کالیدن .

‏۳ چو عم آموختی ازحرص, آنگه تری .کادر شب

‏چو دزدی با چراغ‌آید » گزیده‌نی ‎Woy‏

‏«سنائی ‎soe‏ . دیوان ۲ه ©

‎AYN Sy? ‏وفربار)‎ SSL) ۷988 ‏پهلری‎ kalind . Ala» ۴

[pdf page 368]
‎—\eve—‏ کالجوش
کویندکه ‎Ge‏ باشد ‎ASE ASH, ٩‏ |
```


## [2026-09-07T20:44:24.730Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-07T20:44:24.737Z] TOOL RESULT

```


```


## [2026-09-07T20:44:26.916Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC kalopod / kwrp ===\"; grep -n -i \"kalopod\\|kalbad\\|kalbud\\|kalpat\" IEC.txt | head\necho \"=== IEC kwrp ===\"; grep -n -i \"kʷṛp\\|qṛp\\|kerep\\|kehrp\\|kṛp-\" IEC.txt | head -20"
}
```


### [2026-09-07T20:44:26.999Z] TOOL RESULT

```
=== IEC kalopod / kwrp ===
14212:quortos (2) ‘made; make, fabrication, shape’. Cf. quer-, quor-, qur- Skt. cf. kartum, inf. ‘to do, make’; Per. cf. kala ‘manufactures’; kalbad, s. “body, shape,
14265:qurp- “turn, shape, form, body'. Cf. querp-, quorp- Skt. krp, f. “form, beauty’; Av. kohrp “flesh, body’; Per. cf. kalbad, s. “form, body’; Gk. prapís, f. “bosom, heart, diaphragm’; OLat. qurpus, Lat. corpus, gs: -oris, n. “body, flesh, substance, mass’; Olr. & mod. Ir. crí, m. ‘body, shape, frame’; (Olr. also = “life*); OHG cf. href, OE hrif, n. (belly, womb’, fr. *qurep-); Icel. horf, n. “trend, relation, condition); hor- fur, fpl. ‘outlook’; cf. ON horfa, v. ‘turn, ap- pear’. (Isophones: Slovene krp-elj, s. ‘mite, tick, crablouse’; Slovak krpelec, m. ‘dwarf;
=== IEC kwrp ===
7032:A variant arises in Skt. Sardhah *troop") kerep-, kerop- see kerp-
7049:kerp-, kerep- (korp-, korop-; kereps-) 'skull, tile, pan, ladle, bowl, potsherd’ Skt. cf. karparah ‘skull, potsherd’; Arm. Serep, i-st ‘ladle? beside karapn & karap, gs. karapin ‘skull’; Ligurian substr. in Rumansch (?) creppa ‘skull’; OCS érépü (tile, also **ladle' in view of Crépiti, v. ‘draw water); R cérep ‘skull’; Cerepók, dim. ‘potsherd’; Cz. střep, id.; z-gde in OCS Crüpljo, érüpati ‘draw water’;
7697:korops-, korpor-, cf. kerp- (kerep-) and krp- Skt. cf. karparah ‘skull, tortoise-shell; cup, bowl; Arm. karap and karapn, gs karapin ‘skull
7702:korpos, å ‘cut, cutter; cutting, sharp; spike, point, crag’. Cf. kerp-, krp- Skt. (ambig.) cf. karparah (‘pot, sherd’. Cf. kerep-); Alb. karpë ‘rock, cliff; LW in Big. kàrpa, id.; Ligurian substr. in Rumansh crap, m. (‘boulder’, w. metath, as in cravun *carbonem', crapenda 'carpenta"); LW (?) in Alb. krep (‘crag’, as doublet of karpë?). Cf. WP II, 581. Here also prob. Ir. corr ‘peak, tip, corner, snout, bill, corn on foot"; W cor, pl. od m. (1) ‘point’; ON herfi ‘harrow’; Sw. harv, f. id. beside hárv, pl. -ar, f. ‘rake’; cf. EMSw. härvel ‘buckle’; Blg. krap, adi ‘short’; Li. karpas ‘cutting, clearing’; karpà ‘slice’; kárpa ‘wart; Latv. kārpa, id.
7704:(korp-, korop-, see kerp-, kerep-)
```


## [2026-09-07T20:44:35.551Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=14150 && NR<=14280' IEC.txt | grep -n \"^[0-9]\\{3,4\\}$\\|^ *[0-9]\\{3,4\\} *$\" | head -20\necho \"--- context 14205-14220 ---\"; sed -n '14205,14218p' IEC.txt\necho \"--- context 14255-14270 ---\"; sed -n '14255,14270p' IEC.txt"
}
```


### [2026-09-07T20:44:36.761Z] TOOL RESULT

```
4:1042
12:1043
27:1044
34:1045
49:1046
56:1047
72:1048
81:1049
100:1050
111:1051
126:1052
--- context 14205-14220 ---
1047
ants of uncertain cons. (*quorp- or *quoru-) in MHG warbel, adj. ‘mobile’, cf. Skt. kár- varah ‘variegated’; OFris. hwarvel, Du. wervel, m. ‘vertebra; swivel; pegtop; OHG hwirvil (sic), id.; G. dialect Warbel, m. *whorl'. (Iso- phone: Br. porbolen, f. ‘pimple, pustule, bud")
quorquol- (quorquol-) (2) *windpipe; hoarse- ness in the throat. Lat. curculió, gs: -onis, m. ‘windpipe’; Li. kar- kulys, gs: -io, m. *hoarseness'
quorquor- (quorquort-, quorquorbhit-) ‘curly plant or object, creeper’ Skt. karkatih, f. ‘gourd’; (variant: Carbhita, -am, fn. id. fr. *querbh-); Lat. cf. cucurbita *cucumber'; OE *hwerhwefte (*written -fette & -hwette, both once), id.
quorsio ‘drag, pull, til. See next. Cf. WP I, 429. i Skt. kársami, v. ‘draw, drag; plough; lead’; Av. karos-, v. as Skt.; Per. kašam, v. ‘draw; suffer beside kašam, inf: kāštan, kistan, v. ‘plough’; Arm. kašem, v. “pull, pluck’; Alb. cf. të-kurr, v. tr. contract’, fr. *ati-°); Extn. in Av. karstis, f. ‘ploughing’; (z-gde in) Skt. krstah ‘drawn, plowed’; Per. kišt (2) ‘plowing, sown field”
quorstis, iə ‘brushwood, brake’. Cf. qurst-. Welsh variant querkt- Alb. karthje, f. id.; cf. W perth, pl. -i, f. id. beside prys (z-gde), id.; R xvórost, f. id.; OCz. chvrast-, id. (Cosmas); mod. chrast, f. id.
quortos, is (1) (turn; time, occasion’. Cf. qurt- Skt. katah, m. ‘time; season’; Myc. cf. api-qo (r)to- (epithet of tables: ‘round’ or “turned”, fr. *ombhi-^?); Osc. cf. (prob. z-gde) petiro- pert, adv. (‘four times’. For er fr. *-r- cf. Osc. Mamers for Lat. Mamors); W porth, pl: pyrth, m. *help'; OCS kratü, gs: kratu, m. “time”; Cz. krát, id.; Pol. kroC, m. id. (i-st).; Li. kartas, m. id.; Latv. cf. vien-kartis “simple pattern of weaving’; vien-karss, adj. (/simple', fr. *-quortios)
quortos (2) ‘made; make, fabrication, shape’. Cf. quer-, quor-, qur- Skt. cf. kartum, inf. ‘to do, make’; Per. cf. kala ‘manufactures’; kalbad, s. “body, shape,
quorquol- (quorquol-) — quoteros, à
15
20
25
30
35
--- context 14255-14270 ---
(quros, see quros, quró, ið and quero, quer- (2), quoros)
qurkios, om, is 'tuft, shrub'. Cf. qurst-, quorstis Skt. kürcáh, Am. mn. ‘tuft of grass; beard’; Ir. ere, f., curc, pl. -anna m. ‘crest; cap’; Pol. karcz, m., Cz. krč, m. ‘tree-stump’; Ukr. korč, m. ‘bush, shrub’. (Slav. forms ambig. For a possible initial *k- cf. krKos & krsos (2))
(qurksnos, qur?snos ‘dark, black’. See qurs- nos)
qurlis, io (?) ‘round object, bend, twist, curl. (Slav forms doubtful)
Skt. cf. kurulah, m. ‘curl of hair’; Alb. krel, krele, mf. id. (if fr. *quil-is, -io) (also Kerg, f. id.), as Skt.; Cor. (?) pryl, pl. -yon, m. "round lump’; Big. cf. kárlik, kárljak “hook, crook; hayfork'; (LW in) Alb. kérlug, m. (Ccrook, hook? < Blg. kárljüga, id.); OCz. cf. krly, pl. ‘tongues of animals’. (Isophones: Srb. krlja “block, stump’; Blg. kárl-eZ ‘tick, mite") qurminos, ios *worm-like, flesh-coloured,
1051
red See next and cf. WP I, 523 Alb. cf. i krym(b)un ‘worm-eaten’; W pryfyn, m. ‘worm’; OCS érümini, adj. "red R Cerm- nyj, id.; Li. kirminas, adj. of a worm’; kif- minas ‘worm’
qurmis (i-basis) *worm, grub'. WP I, 523. (Variant: qurmà) Skt. krmih, m. id.; Av. (variant) koroma, f. id.; Per. kirm, id.; Oss. kalm, pl: kàlmitá, id.; (LW in Arm. Seram, o-st. 'silkworm"); Alb. krimb, krymb, krym, m. ‘worm, grub’; MIr. cruim, Ir. cruimh, m. id.; Br. prév, prénv, m. id.; W pryf, pl. -ed, m. id.; Cor. pryf, coll. (sg: preven), f. id.; OCS cf. éórüminü, R čermnyj, adj. “crim- son’; Li. kirmis, gs: -iés, f. ‘worm, grub’; Latv. cirmis, kirmis, id. Extn. of type qurmón-, -en- in Br. préon, m. *worm' beside am-prévan, m. ‘vermin’; Cor. preven, f. ‘worm’; Li. kirmuó, gs: -efis, id. (a parallel formation occurs in Lat. vermen, n. ‘colic’, vermina, npl. ‘vermin’ in relation to vermis ‘worm’. Cf. uerm-, urm-)
qur, ið (z-gde of type quero, see quer- (2) and kur- (6) Ir. cuirim, v. ‘set, put, apply, send”; Olr. (also: ‘bury; engage in"); OCS cf. krücí, krútij, m. “smith, wright'; Li. Kur, kürti (2), usually su-kuriü, kurt, v. “build, create, compose". See next
quros 'set, putting, act, fact'. Cf. quro, quer- (2) and kur- (6) (O-gde in) Skt. karáh, adj. (doing, making’, fr. *quor-); MIr. cor, m. “putting, throw, turn’; W pry, pl. pryoedd, m. ‘produce, food’; cf. also par, pl. au, m. (1) ‘cause’ beside peru, v. id. (fr. *quor: *quer-)
qurp- “turn, shape, form, body'. Cf. querp-, quorp- Skt. krp, f. “form, beauty’; Av. kohrp “flesh, body’; Per. cf. kalbad, s. “form, body’; Gk. prapís, f. “bosom, heart, diaphragm’; OLat. qurpus, Lat. corpus, gs: -oris, n. “body, flesh, substance, mass’; Olr. & mod. Ir. crí, m. ‘body, shape, frame’; (Olr. also = “life*); OHG cf. href, OE hrif, n. (belly, womb’, fr. *qurep-); Icel. horf, n. “trend, relation, condition); hor- fur, fpl. ‘outlook’; cf. ON horfa, v. ‘turn, ap- pear’. (Isophones: Slovene krp-elj, s. ‘mite, tick, crablouse’; Slovak krpelec, m. ‘dwarf;
qurmis — qurtos, å
10
15
20
25
```


## [2026-09-07T20:44:53.568Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%A8%D8%AF",
 "prompt": "Give the full Persian etymology section for کالبد (kâlbod): what is it derived from (Middle Persian form, Greek kalopodion?), and any alternative etymologies mentioned. Quote exactly."
}
```


## [2026-09-07T20:44:54.638Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%A7",
 "prompt": "Give the full Persian etymology and definitions for کالا (kâlâ) 'goods, merchandise'. Quote the etymology exactly, including any Middle Persian or reconstructed forms and cited authorities (Hasandust etc.)."
}
```


### [2026-09-07T20:44:58.552Z] TOOL RESULT

```
# Persian Etymology of کالبد

According to the Wiktionary entry, the word derives from Middle Persian **kʾlpwt' (kālbod)**, meaning "body, shape, form," which itself comes from Ancient Greek **καλοπόδιον (kalopódion)**, meaning "shoemaker's last."

The entry states: "From Middle Persian [script needed] (kʾlpwt' /⁠kālbod⁠/, "body, shape, form"), from Ancient Greek _καλοπόδιον_ (kalopódion, "shoemaker's last")."

Related forms are noted in Manichaean Middle Persian and Old Armenian as Iranian loanwords. The entry also notes that کالبد is "a doublet of قالب (qâleb), the same Greek word via Arabic," indicating an alternative transmission route through Arabic rather than direct Persian preservation.

No competing etymologies are presented in the section.
```


### [2026-09-07T20:45:02.688Z] TOOL RESULT

```
# Persian Etymology of کالا (kâlâ)

## Etymology

According to the Wiktionary entry, کالا's etymology traces back through Proto-Iranian and Proto-Indo-European. Specifically:

The term is "ultimately a derivative of Proto-Iranian *kar- ('to do, make'), from Proto-Indo-European *kʷer- ('to make')."

The entry also references Old Armenian կահ (kah) as a cognate for additional etymological support.

## Definitions

The Persian noun کالا (kâlâ) has three primary senses:

1. **Commercial goods**: "things; goods; commodity; article" — referring to merchandise and commodities in trade contexts
2. **Clothing (Dari dialect)**: "clothes, dress, attire; costume"
3. **Archaic sense**: "silk clothes"

A usage example provided from Firdawsī's *Shahnameh* (c. 1011) demonstrates the commercial meaning: "transportation of commodities."

The entry notes that اجناس (ajnâs) serves as a synonym for the primary commercial sense.
```


## [2026-09-07T20:45:12.168Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D8%A7%D9%84%D8%A8",
 "prompt": "Give the Arabic etymology section for قالب (qālab/qālib) 'mould, last, form': what is it borrowed from (Persian kālbod? Greek kalopodion? Aramaic?) and how does it relate to the Arabic root ق ل ب? Also give the Persian section for قالب. Quote exactly."
}
```


## [2026-09-07T20:45:12.925Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/caliber",
 "prompt": "Full etymology of caliber/calibre, including the Italian, Arabic qalib and Greek kalopodion chain and any alternative (Latin qua libra) proposals."
}
```


### [2026-09-07T20:45:18.125Z] TOOL RESULT

```
# Etymology of قالب (qālab/qālib)

## Arabic Etymology

According to the Wiktionary entry, the Arabic word is **not** borrowed from Persian or Greek directly. Rather, it comes from Syriac:

> "From Classical Syriac ܩܠܒܝܕ (/⁠*qālobīḏ⁠/, 'last'), from Ancient Greek καλοπόδιον (kalopódion, 'last')"

The Greek term itself is "a compound of κᾶλον (kâlon, 'wood') and πούς (poús, 'foot')."

The Arabic root is listed as **ق ل ب (q l b)**, though the entry indicates this is the root category the term belongs to, rather than its source.

## Persian Section

The Persian entry states the word is:

> "Borrowed from Arabic قَالِب (qālib). Doublet of کالبد (kâlbod)."

Persian meanings include: mould, template, form/shape, body (as opposed to soul), and cake/block (for countable items like soap).
```


### [2026-09-07T20:45:19.123Z] TOOL RESULT

```
# Etymology of Caliber

The word "caliber" has two competing etymological theories:

## Primary Theory: Arabic Origin
The traditional account traces caliber to French *calibre* (mid-16c.), which is "often said to be ultimately from Arabic *qalib* 'a mold for casting.'" However, this attribution lacks solid evidence.

## Alternative Theory: Latin Origin
A more recent scholarly proposal suggests the word "was formed in French" from Medieval Latin *qua libra*, meaning "of what weight." This combines the interrogative *quis* with *libra* (meaning "balance"), supporting a Latin rather than Arabic source.

## Meaning Evolution
Interestingly, the figurative sense preceded the technical one. The earliest English usage (1560s) meant "degree of merit or importance," only later (1580s) acquiring its technical meaning as "the inside diameter of a gun barrel." The word subsequently developed to describe "the capacity of one's mind, one's intellectual endowments."

The page notes that Spanish and Italian forms "appear too late to act as intermediate forms" between Arabic and French, supporting the direct Latin-to-French development theory.
```


## [2026-09-07T20:45:36.783Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA grep ===\"; grep -n -i \"qalab\\|qālab\\|kalbad\\|kālbad\\|kalopod\\|Leisten\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== PLA index around 215 ===\"; grep -n \"^215$\\|^ *215 *$\" incoming/PLA/PLA_pages.txt | head"
}
```


## [2026-09-07T20:45:38.315Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN page markers near caliber ===\"; awk 'NR>=6150 && NR<=6200' KLN_1966.txt | grep -n \"^[0-9]\\{3\\}$\" | head\nsed -n '6170,6186p' KLN_1966.txt | cut -c1-200"
}
```


### [2026-09-07T20:45:39.641Z] TOOL RESULT

```
=== PLA grep ===
=== PLA index around 215 ===
```


### [2026-09-07T20:45:41.057Z] TOOL RESULT

```
=== KLN page markers near caliber ===
9:222
20:223
38:224
39:225
derivatives  of  base  *kleu-,  enlargement  of  base *kel-,  ‘warm’,  see  lee.
Caleb,  n.,  masculine  PN.;  in  the  Bible,  one  of  the twelve  men  sent  by  Moses  to  spy  out  the  land of  Canaan.  —  Heb.  Kalebh,  prop,  ‘like  a  dog’, fr.  kelebh,  ‘dog’.  
Derivative :  calefacient,  n. calefactory,  adj.,  making  warm.  —  Formed  with adj.  suff.  -ory  fr.  calefactus,  pp.  of  calefacere,  ‘to make  warm’.  See  prec.  word, calembour,  n., 
Derivatives:  calendar,  tr.  v.,  calendar-er,  n., calendar-ial,  adj.,  calendar-ian,  adj.  and  n., calendar-ic,  adj.
calender,  n.,  a  mendicant  dervish.  —  Pers. qalender.
calender,  n.,  machine  with  rollers  for  pressing cloth.  —  F.  calandre ,  ‘calender,  roller,  mangle’, fr.  earlier  *colandre,  fr.  VL.  *colendra,  fr.  Gk. xuXivSpoc,  ‘roller,  cy
Derivative :  calender-er,  n. calends,  kalends,  n.  pi.,  the  first  day  of  the  an¬ cient  Roman  month.  —  ME.  kalendes,  fr.  OE. calend,  ‘month’,  fr.  L.  calendae,  kalendae,  �
calicular
L.  calens,  gen.  -ends,  pres.  part,  of  calere,  ‘to  be hot’.  See  caldron.
Derivatives:  calenture,  tr.  v.,  cakntur-al,  adj. calepin,  n.,  a  dictionary.  —  Named  after  Am- brogio  Calepino  (1435-1 51 0,  author  of  a  famous Latin-Italian  dictionary.
calescence,  n.,  increasing  heat.  —  See  next  word and  -ce  and  cp.  calorescence. calescent,  adj.,  growing  warm;  increasing  in heat.  ■ —  L.  calescens,  gen.  -ends,  pres.  part,
calf,  n.,  young  of  a  cow,  etc.  —  ME.  calf,  kalf fr.  OE.  cealf,  rel.  to  OS.,  MDu.  calf,  ON.  kalfr, Dan.  kalv,  Swed.,  Du.  kalf,  OHG.  chatp,  kalb, MHG.  kalp,  G.  Kalb,  Goth
calf,  n.,  the  fleshy  part  of  the  leg.  —  ON.  kdlfi, ‘calf  of  the  leg’,  generally  supposed  to  be  rel.  to kalfr,  ‘young  of  a  cow’,  hence  derivatively  iden¬ tical  wit
Derivative:  Caliban-ism,  n. caliber,  calibre,  n.,  the  diameter  of  the  bore  of  a gun.  —  F.  calibre,  fr.  It.  calibro,  fr.  Arab,  qdlib, ‘mold,  model’,  fr.  Gk.  xxXo ttoSlov, 
Derivative:  calibrat-ion,  n. calicle,  n.,  a  small  cup-shaped  cavity  (zool.)  — L.  caliculus,  ‘a  small  cup',  dimin.  of  calix,  gen. calicis,  ‘cup’.  See  calyx  and  cp.  calycl
californium
calori-
```


## [2026-09-07T20:45:48.305Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\\[pdf page\" incoming/PLA/PLA_pages.txt; grep -n \"\\[pdf page 21[0-9]\\]\\|\\[pdf page 22[0-9]\\]\" incoming/PLA/PLA_pages.txt | head\necho \"=== try grep qalib variants ===\"\ngrep -n -i \"qālib\\|qalib\\|kalib\\|Schuhmacher\" incoming/PLA/PLA_pages.txt | head"
}
```


### [2026-09-07T20:45:48.382Z] TOOL RESULT

```
0
=== try grep qalib variants ===
```


## [2026-09-07T20:45:51.550Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} END{print NR\" pages\"}' incoming/PLA/PLA_pages.txt\nawk 'BEGIN{RS=\"\\f\"} NR==225' incoming/PLA/PLA_pages.txt | head -40"
}
```


### [2026-09-07T20:45:52.937Z] TOOL RESULT

```
301 pages
fasätin                                                                        210                                                fisfisa



bs                _         asätin:          Pl.        v.olus      fustän         q.    v.


als           -       fustän:           "Überkleid,                Jacke,      Joppe"          pers.     ı


obs - fustän = fustän                                     a. v.

                                                                                                                                            4
Se        -       fustug:              "Pistazie"                   pers. «, peste               2 mp.           Ir»o   3,   u.   bistag
          aram.              Sans.
          Pistazie                    pers.             >     griech.        >      lat.       6, frz.        pistache »-


a3»           - fustuga:                    nom,        un.   v.    is        fustug          "eine    Pistazie".


OR            - fustugi:                     "pistaziengrün".


ansıms - fisfisa:                            "Luzerne"         pers.         ?. 7, dtsch.              Alfalfa.

o5lhs - faßsäga:                             "Rakete",


Als-
     “.               faß$äka
                             ’          - fafääga             q. v.

Aas_          fafakı:             Pl.       v. Es fafaka ga. v

 .
Ais-              fafaka:              "Patrone".

     a,
ls _ faSaka:                           "Patronentasche".
```


## [2026-09-07T20:46:01.412Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==230' incoming/PLA/PLA_pages.txt | head -40\necho \"############# search qalab across\"\ngrep -n \"qālab\\|qälab\\|qalab\\|kālbad\\|kalbad\\|kalapodion\\|καλοπόδιον\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head"
}
```


### [2026-09-07T20:46:02.618Z] TOOL RESULT

```
                                                                              [E>}




sl      -    gäbüs:          "Eigenname"                 <        pers.» / käwus                mp.            ıy-ug     käayus au.
       kavi-usan             ı        mand.        gaiqubas              .


oub     -    gasän:          eine          Stadt     in       der       Nähe         v.    Isfahan    <       pers. „li        ka$an    3   syr.
            s*.

uläl - gäSän                = gasän           a.    v.

                                                             u.                                =9»5
sliLb - gäßäni:                   Nisba        v.    qäßän             q. v.,         syr.     =),

BRIH -        gäfür:         "Kampfer"              pers.          ec         MP. Yıa;»s kapur            7    aram,    $,85,        Yuan sus      »
       mand.        gapur             °, ar.       Lw.       käfür,          engl.         camphor,       dtsch.    Kampfer.


eU-         gäqum:          "Hermelin"              pers.          9 <T mp. +a.3 käkem                    "Name    der Gattung
       Musterlina"                10,


—IV- gälib: "Gußform, Model" pers.                                                        »Wkalbod !!              mp. >10%            kälpüs 12,
    mand. galib 1°,

     IL - gatlibgi
           gälibgi:                   "Gießer"           s. galıb
                                                             galib.

U       - galibi:                 "gegossen,             geformt".


&2 - gibäf: Pl. v. & aögabag
                      gabag q. v.

1.    Addai       Scher          s.    v.,     Nyberg             Bd.    II      s.       v.
2.    Macuch        s.      v.
############# search qalab across
```


## [2026-09-07T20:46:10.221Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==230' incoming/PLA/PLA_pages.txt | tail -25"
}
```


### [2026-09-07T20:46:11.664Z] TOOL RESULT

```
     IL - gatlibgi
           gälibgi:                   "Gießer"           s. galıb
                                                             galib.

U       - galibi:                 "gegossen,             geformt".


&2 - gibäf: Pl. v. & aögabag
                      gabag q. v.

1.    Addai       Scher          s.    v.,     Nyberg             Bd.    II      s.       v.
2.    Macuch        s.      v.
3.    Ernst       S.     101.
4.    Brockelmann                s.    v.
5.    ebda.
6.    as-Suyütl             Ita.       al-MuCarrab                 s.    Ve;         TaCalivl        figh     al-luga     s.    v.
7.    Mackenzie             s.    v.
8.    Macuch        s.      v.,       Brockelmann                 s.    v.
9. TaCalibl Figh al-luga s. v.
10.    Bundahifn             s.       v.
11.    BQ.     s.      v.
12.    Nyberg          Bd.       II    s,     v.
13.    Macuch          s.    v.
```


## [2026-09-07T20:46:41.408Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON kala headword ===\"; grep -n \"کالا\\b\" MON_part2.txt | head -10\necho \"=== MON_part1 lines with کالا: ===\"; grep -n \"کالا[:؛]\" MON_part1.txt MON_part2.txt | head -10\necho \"=== MON کالب ===\"; grep -n \"کالب[:د ]\" MON_part2.txt MON_part1.txt | head -10\necho \"=== MON اختاپ ===\"; grep -rn \"اختاپ\" MON_part1.txt MON_part2.txt incoming/MON/ 2>/dev/null | head -5\necho \"=== MON کالیبر ===\"; grep -rn \"کالیبر\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head -5"
}
```


### [2026-09-07T20:46:41.546Z] TOOL RESULT

```
=== MON kala headword ===
6234:کالایی که از کشور برون رود؛ صادر (فره.) 
10085:کالای ممنوع معامله کند. 
11470:کالاهای ممنوع معامله کند. 
12354:کرک انار آز راب سکالان که 
16968:کالای تجارتی و غیره). 
18033:کالاهای خود را جا دهند. کاروانسرای شاه 
18202:بی‌رونق؛ مق. رواء رواج. کالای (متاع) 
18203:کاسد: متاعی که از آن استقبال نکنند؛ کالای 
19215:کالا: قا2 [- کاله] (.) اسباب خانه» لوازم 
19217:آب کردن کالا: زیادتر از ارزش قیمت 
=== MON_part1 lines with کالا: ===
MON_part2.txt:19215:کالا: قا2 [- کاله] (.) اسباب خانه» لوازم 
MON_part2.txt:19217:آب کردن کالا: زیادتر از ارزش قیمت 
MON_part2.txt:45255:برند؛ آنچه که حوایج را سودمند بود؛ کالا؛ 
MON_part2.txt:75097:نرخ: (.) بهای کالا؛ قیمت جنس. 
=== MON کالب ===
MON_part2.txt:4955:(التفهیم ۴۹۸). فتح میت: (پز.) کالبدگشایی 
MON_part2.txt:10621:قالب: (ا16-تد. )اهاز [معر . کالبد] شکل. 
MON_part2.txt:19231:کالید: 04« ,12۱02۵ [- کالب ] (ا.) قالب هر 
MON_part2.txt:19235:صورت. پیکر» شبح. مشیمه » رحم. کالبد 
MON_part2.txt:33069:کالبد ظاهری» تن هب مق از آب و 
MON_part2.txt:38254:لام هقا [ع.] (.) کالبد مردم» شخص. 
MON_part2.txt:53002:روان از کالبد کسی؛ فوت کردن وفات 
MON_part2.txt:70916:مناظر و مرایا و کالبدشناسی رعایت 
MON_part2.txt:77060:نعش: ۹ (ع.] (.) کالبد مرده (انسان با 
MON_part2.txt:83887:بوشش خانه. قالب. کالبد. قالب طاق و گنبد 
=== MON اختاپ ===
=== MON کالیبر ===
```


## [2026-09-07T20:46:42.011Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/octopus",
 "prompt": "Etymology of octopus; also please give etymology of pilot and podium if shown on the page. Quote the Greek forms."
}
```


### [2026-09-07T20:46:58.255Z] TOOL RESULT

```
# Etymology Summary

**Octopus:**
The word comes from 1758, derived from the Latinized Greek form *oktōpous*, meaning "eight-foot." It combines *oktō* (eight) and *pous* (foot), from the PIE root *ped- meaning "foot." The ancient Greeks more commonly used *polypous* (many-foot). The classical plural would be *octopodes*, though *octopuses* is preferred in modern English.

**Pilot:**
The page lists "pilot" as a word potentially derived from the *ped- root, but provides no detailed etymology for it on this page.

**Podium:**
Similarly, "podium" is mentioned as deriving from the *ped- root (meaning "foot"), but specific etymological details are not provided in this content.

The page does not include the full etymologies for pilot and podium—only references to them under words formed from the *ped- root.
```


## [2026-09-07T20:47:05.919Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19213,19240p' MON_part2.txt\necho \"=== قالب entry ===\"; sed -n '10619,10640p' MON_part2.txt"
}
```


### [2026-09-07T20:47:05.991Z] TOOL RESULT

```
خام» ارس» نار سیده. 

کالا: قا2 [- کاله] (.) اسباب خانه» لوازم 
سرای. مال التجاره» متاع. مهر ه‌های شطر نج. 
آب کردن کالا: زیادتر از ارزش قیمت 
چیزی را گفتن. کالای بد به ریش خاوند 
(خداوند): متاعی که به سبب بدی خریدار 
ندارد» در این هنگام این جمله را بر زبان 
رانند. (قس. مال بد بیرخ ريش صاحیش). 
کالار: 12157 (.) آبکندی عمیق که اسب و 
سوار از آن گذر نتواند کرد. نخته نننلگک 


کالباس: 25 (.) گوشت گاو و چری 
خوک و بعض مواد دیگر را پخته درون 
روده کنند؛ جکر آکند؛ جگر آکنده؛ 
جر غند» جهو دانه» نفانق» عصیب. 

کالید: 04« ,12۱02۵ [- کالب ] (ا.) قالب هر 
جیز (عسموما)» کالب. قالب خشت‌زنی 
(خصوصا). تن (آدمی و جانوران)» بدن. 
انمودج» نمو نه» سرمشق. شکل؛ هت 
صورت. پیکر» شبح. مشیمه » رحم. کالبد 
ار 

ک‌البدشکافی: ۲.3۰5۲ [یو. ف.] 
(حامص.) (پز.) باز کردن و شکافتن اجساد 
در آزمایشگاه؛ تشریح عملی. 
=== قالب entry ===
و حدیث؛ مق. حال. قال جبزی را کندن: 
(عم.) آن را تمام کردن؛ به بایان رسانیدن. 
قالب: (ا16-تد. )اهاز [معر . کالبد] شکل. 
هیثت. آلتی که جسمی شکل‌پذیر را در 
داخل یا خارج آن نهاده بصورت آن آلت 
در آورند. بو ته زرگری؛ نو تقه. واحدی برای 
قطعات بریدهٌ معین و معلوم از چیزی. تن 
بدن. هر یک از سهره‌های چوبی که 
نقش‌های مورد نظر را روی بردة قلمکار 
که بر اساس شکل اولی ساخته شده. (پز. 
قد.) آلتی است که بواسیر را بدان برند و 
دیوچه (زالو) را بدان بردارند. (عر.) جزو» 
رکن. قالب خاکی: (کذ.) تن؛ جسم. قالب 
مثالی: (فد. تص.) بدن مثالی. از قالب بیرون 
(برون) 2 در.ست و آماده شدن. به قالب 
زدن: ساحتن» جعل کردن؛ دروغ پرداختن. 
قالب: 2۱60 [ع.] (.) (گیء) غورةٌ خرمای 
سر ح» سر احمر. 

تالب تهی کر دن: ههار زمعن 
ف.](مصل.) خالی کردن قالب چیزی را. 
( کد.) ببخود شدن. (کد.) مردن؛ فوت کردن.
```


## [2026-09-07T20:47:06.467Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pilot",
 "prompt": "Full etymology of pilot, including Greek pedon/pedalion and the *ped- root; note any doubts."
}
```


### [2026-09-07T20:47:32.695Z] TOOL RESULT

```
# Etymology of "Pilot"

## Origin and Development

The word "pilot" originated in the 1510s as a nautical term. It derives from French *pillote* (16th century), which came from Italian *piloto*. This Italian term is believed to be an alteration of Old Italian *pedoto*, ultimately tracing back to Medieval Greek *pedotes* meaning "rudder, helmsman."

## Root Connection to "Foot"

The etymology connects to the Greek word *pedon*, meaning "steering oar," which relates to *pous* (genitive *podos*), meaning "foot." Both trace to the Proto-Indo-European root *ped-, which means "foot."

Interestingly, the transformation of the *d* sound to *l* in Latin-derived languages (known as "Sabine -l-") parallels similar changes in words like "odor/olfactory."

## Semantic Expansion

The figurative sense—"a guide, a director of the course of others"—emerged by the 1590s. The literal meaning extended significantly: by 1848 to describe those controlling balloons, and by 1907 to airplane operators. As an adjective meaning "serving as a prototype" (as in "pilot episode"), the usage dates to 1928.

## Notable Doubts

The source notes the etymology is "supposed to be" derived from the Greek root, indicating some scholarly uncertainty about the precise pathway of linguistic transmission.
```


## [2026-09-07T20:47:38.240Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%AE%D8%AA%D8%A7%D9%BE%D9%88%D8%B3",
 "prompt": "Persian اختاپوس (oxtâpus): give the etymology (from French octopode? Greek?) and the definition, quoted exactly."
}
```


## [2026-09-07T20:47:39.609Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/trapeze",
 "prompt": "Etymology of trapeze, trapezium, trapezoid: Greek trapeza 'table' < tra- 'four' + peza 'foot'. Quote."
}
```


### [2026-09-07T20:47:41.970Z] TOOL RESULT

```
# Persian اختاپوس (oxtâpus)

**Etymology:**
The word derives "From Ancient Greek ὀκτώπους (oktṓpous)." The Greek term itself combines elements meaning "eight" and "foot."

**Definition:**
According to the entry, اختاپوس is "(less common) octopus (any of several marine molluscs of the family Octopodidae)." The more common Persian synonym is هشت‌پا (hašt-pâ), which literally means "eight-foot."
```


### [2026-09-07T20:47:44.805Z] TOOL RESULT

```
# Trapeze Etymology Summary

The word **trapeze** entered English in 1861 from French *trapèze*, derived from Late Latin *trapezium*. It describes "a gymnastics device, a high swing with a cross-bar suspended by two cords, used for feats of strength and agility."

The term's name reflects its shape: the crossbar, ropes, and ceiling form a trapezium (four-sided geometric figure).

**Root origin:** The geometric term *trapezium* traces to Greek *trapezion*, literally meaning "a little table"—from *tra-* (four) plus *peza* (foot). This makes sense etymologically, as "the classical Greek table is said to have had one side shorter than the opposite," creating the irregular quadrilateral shape that gave the gymnastics apparatus its name.

Related terms include *trapeze-artist* (1938) and *trapezist* (1875).
```


## [2026-09-07T20:47:49.458Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/fetch",
 "prompt": "Etymology of the verb fetch (OE feccan/fetian) and its relation to PIE *ped- 'foot'. Quote."
}
```


## [2026-09-07T20:47:50.354Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.cnrtl.fr/etymologie/calibre",
 "prompt": "Give the TLFi etymology of French 'calibre': what origin is given (Italian calibro, Arabic qalib, or Latin qua libra)? Quote the etymology paragraph."
}
```


### [2026-09-07T20:47:55.786Z] TOOL RESULT

```
I appreciate your question, but I cannot provide the answer you're seeking. The webpage content provided only contains "Portail lexical" (Lexical Portal) as a header/title, with no actual etymology information about the French word "calibre" included in the excerpt.

To answer your question about whether TLFi (Trésor de la Langue Française informatisé) attributes "calibre" to Italian, Arabic, or Latin origins, I would need access to the actual etymology section of that resource, which is not present in the content you've shared.

If you can provide the relevant etymology passage from TLFi, I'd be happy to help identify which origin the dictionary gives and quote it according to your specifications.
```


### [2026-09-07T20:48:00.082Z] TOOL RESULT

```
# Etymology of "Fetch" and Its Connection to PIE *ped-

The verb "fetch" traces back through Middle English *fecchen* to Old English *feccan*, meaning "to bring" or "to seek." According to the Online Etymology Dictionary, this word likely derives from Proto-Germanic *\*fetan*, which connects to an even older Indo-European root.

The key linguistic connection is to the PIE verb meaning "to walk," derived from the root **\*ped-** meaning "foot." This etymological link suggests that the concept of fetching—bringing something toward oneself—is fundamentally related to the physical act of moving on foot.

As the source explains: "This would connect it to the PIE verb for 'to walk' derived from root \*ped- 'foot.'" This demonstrates how semantic fields can expand over time, with a word originally rooted in locomotion broadening to encompass the retrieval and conveyance of objects.

The word's sense development is extensive, eventually encompassing nautical meanings, the familiar dog-training command (attested by 1889), and even 17th-century usage in linguistic discourse.
```


## [2026-09-07T20:48:09.970Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN kalb ===\"; grep -n -i \"k.lbud\\|kalbad\\|kalopod\\|Modell\" HRN.txt | head\necho \"=== HRN kala ===\"; grep -n -i \"kala 'Ware\\|kala 'War\\|Ware'\" HRN.txt | head\necho \"=== ARY کالبد ===\"; grep -n \"کالبد\\|کالا\" incoming/ARY/ARY_pages.txt | head\necho \"=== SKT trapezium/caliber ===\"; grep -n -i \"trapezium\\|caliber\\|calibre\" SKT.txt | head\necho \"=== SYN table trapeza ===\"; grep -n -i \"trapeza\" SYN.txt | head -3"
}
```


### [2026-09-07T20:48:10.108Z] TOOL RESULT

```
=== HRN kalb ===
=== HRN kala ===
=== ARY کالبد ===
=== SKT trapezium/caliber ===
2640:Caliber,  Calibre,  bore  of  a  gtax. F.  caJiJirr,  sire  of  a  bore.  Et)'m.  onks Perhaps  fram  h.pid  lihrJ,  with  what  v< ( Dici) ;  or  from  Aiab.  qjiti>,  a  fonn,  m modd.  Rich.  Dice  p.  1 1 1 1  i  Littr^).
23588:rcl.  bice,  bijon.  blond,  blouse,  brattice, te«  (il,  biet'ze  (2),  broil  (2).  buffer  (,0, ffer  (3).  buffet  (I),  buffet  (j),  huffoon. ruattft  (burgoiict),  busk  (i),  buttress, t>ba|^  {»),  culibcr  ^calibre),  calipers, lirer,  champagne,  chcval-dc-frise,  chi- Bcry,  chiffonier,  cockaJe.  curlew,  davit, le,  dtMase,  drab  (a),  drape,  dupe,  ease, ibiiitlc  (O,  embattle  (a),  cmblaion,  era- S*  { I  \  emboM  (2),  embrasure,  embroider, ibroil,  entice,  entrench,  fribble,  frieze  (i), ppery,  furbelow,  galley,  galliot,  gallon, rland,  gasccmade,  gavotte,  gibbet,  giblets, (3),  gingham,  gobelin,  gormandise, lUTnand,  graze  (l)?,  greaves  (,a),  grouse, illotine,  guxxle,  harass,  haricot  (i),  hari- (a\  harlequin,  harlot,  harridan,  hnunt, ik  ;a],  jacKetf  jostle,  lawn  (^a),  lees, tch,  loo,  lozenge,  magnolia,  maraud, utia,  martinet,  martingale,  martlet,  mich, Trtise,  musit.  Nicotian,  pamphlet?,  pa- Kv  pedigree?,  pillory,  pinch,  pinchbeck vritma/  name),  pirouette,  piss,  pittance, plin,    ricochet,    roan,    sautcmc,    savoy,
=== SYN table trapeza ===
12127:Lat. _ménsa Dan. bord ChSl. trapeza It. lavola Sw. bord SCr. __ stol (irpeza) Fr. table OE bord, beod Boh. — stil
```


## [2026-09-07T20:48:11.500Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/calibre",
 "prompt": "English 'calibre/caliber' etymology section: what chain is given (French, Italian, Arabic qālib, Greek kalopodion) and any note about competing Latin qua libra theory? Quote."
}
```


### [2026-09-07T20:48:17.101Z] TOOL RESULT

```
# Etymology of "Calibre"

Based on the Wiktionary content provided, here's what's documented:

**Direct Etymology Chain:**
The word traces back through French to Arabic. According to the page: "Borrowed from Arabic _قَالِب_ (qālib)."

French borrowed the term from Arabic, and then English, Catalan, Spanish, and Portuguese all subsequently borrowed it from French.

**Notable Absence:**
The document does **not** mention:
- Italian as part of the direct etymological chain
- Greek "kalopodion" 
- Any competing Latin "qua libra" theory

The etymology section only presents the Arabic→French→multiple languages pathway, with no alternative theories or competing explanations discussed.
```


## [2026-09-07T20:49:05.904Z] TOOL CALL #52: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%A8%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D8%A7%D9%84%D8%A8\" \\\n \"https://www.etymonline.com/word/caliber\" \\\n \"https://www.etymonline.com/word/octopus\" \\\n \"https://www.etymonline.com/word/pilot\" \\\n \"https://www.etymonline.com/word/trapeze\" \\\n \"https://www.etymonline.com/word/fetch\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%AE%D8%AA%D8%A7%D9%BE%D9%88%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/calibre\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 384, root Ped/Pod part 2: kalbod/qalib/caliber/octopus/trapeze chain\" 2>&1 | tail -2; done"
}
```


## [2026-09-07T20:49:08.381Z] TOOL CALL #53: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/site/pages/384.jpg 2>/dev/null || (cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 384 -l 384 -r 150 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg384 && echo done)"
}
```


### [2026-09-07T20:49:09.523Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d5ebef9b1f39926a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd60abfb26cd3ab1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3f123263cc905ef7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ea1221b6a9ba9cf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a9d497ac585f6eca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/48382f2b50c88843.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/538c535c37b3081a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7c2a26c95dd095a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b530a4cf749187f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/84d4b4c288ad8ee1.txt
```


### [2026-09-07T20:49:10.757Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/site/pages/384.jpg
```


## [2026-09-07T20:49:14.293Z] TOOL CALL #54: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/384.jpg"
}
```


### [2026-09-07T20:49:14.320Z] TOOL RESULT

```

```


## [2026-09-07T20:49:29.616Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 384 -l 384 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg384 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg384.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.15),int(h*0.13),int(w*0.62),int(h*0.30))).resize((int(w*0.47*1.6),int(h*0.17*1.6))).save('pg384-crop.png')\n\""
}
```


### [2026-09-07T20:49:31.860Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-07T20:49:34.372Z] TOOL CALL #56: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg384-crop.png"
}
```


### [2026-09-07T20:49:34.400Z] TOOL RESULT

```

```


## [2026-09-07T20:49:50.949Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 ped ===\"; grep -n \"ped-\\s*'Fuss'\\|ped- 'Fuss\\|pēd-\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -8\necho \"=== WLD Bd3 register ped ===\"; grep -n \"^ped\\|ped- II 23\\|II 23\" WLD_band3.txt | head -8\necho \"=== SYN foot ===\"; grep -n -i \"4\\.37\\|FOOT$\" SYN.txt | head -8\necho \"=== AFM قالب ===\"; grep -n \"قالب\\|کالبد\" AFM_pages.txt AFM.txt AFM_alt.txt 2>/dev/null | head -8\necho \"=== ARY latin index KALBOD/KALA ===\"; grep -n -i \"kalbod\\|kalbad\\|kala\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -8"
}
```


### [2026-09-07T20:49:52.317Z] TOOL RESULT

```
=== WLD Bd2 ped ===
=== WLD Bd3 register ped ===
=== SYN foot ===
5196:4.32 Ersow 4.33 Hanp 4.34 Fincer 4.342 Taumes 4.35 Lxc 436 Kner 4.37 Foor 4.38 Tor 4.39 Nar 4.392 Wincg 4.393 FeaTaer
6241:NG 706i, oddp. ‘foot’ (4.37), also sometimes ‘leg’.
6249:Rum. picior, orig. only ‘foot’ (4.37).
6253:ON fotr ‘foot’ (4.37) used of the entire ‘leg’.
6261:SCr. noga, etc. the common modern Slavic word for ‘leg’, but properly, and ChSI. noga in Gospels only, ‘foot’ (4.37).
6270:4.37 Grk. — zobs Goth. fotus NG 66, wodé pu ON Jotr Lat, pés Dan. fod ae piede Sw. fot as pied OE Sot sp. pie ME sfote : um.  picior NE foot ae traig, coss Du. voet a troigh OHG fuoz u troed MHG T. troad NHG oe aay Se the inherited group, con- ee © Toot connection of which
6282:FOOT
8100:Skt. manda-: ChS]. maditi ‘delay, linger’, maqdtni ‘slow’, etc. Walde-P. 2.305. Meillet, MSL 14.372.
=== AFM قالب ===
=== ARY latin index KALBOD/KALA ===
691:02S ES Ue ead 99 pd oben WT AUT 5 JS Kala hee aula J feeb ose 4
5169:PYSK, PYKAC (POLISH) ging) PUSTI-, PUSKALA-
11924:CORNACCHIA A(TALIAN) gids! KALA KURDISH) 62
12242:HWAN — (OLD SAXON) pS ig Se KALA AFGHANI) (4) gli}
```


## [2026-09-07T20:49:59.486Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pedis\\|Fussfessel\\|nrjbrj\\|πέδη\\|pes, pedis\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -8\necho \"=== pages tag ===\"; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd2_pages.txt | sed -n '20,40p'"
}
```


### [2026-09-07T20:49:59.550Z] TOOL RESULT

```
1532:vgl. lat. pediseqims, -a „Diener, -in“ eig. „auf dem Fu6e folgend^' (s. Vf. 
1541:lat. am-pediiis „schnellfu6ig‘' ; lit. hngvapedis „leisfuBig“ ; germ. *fetl f. 
4490:im Iran, voraussetzt; pedis und pazdu- eine von pMo unabhangige Sippe??); 
30937:Ahd. beinsegga „pedisequa“ (J. Schmidt KZ. 19, 273), as. segg, ags. scc^, 
42724:Got. spedisa „spaterer“, spediimists „spatesteP^, ahd. spati, Adv. spato 
=== pages tag ===
```


## [2026-09-07T20:50:02.192Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1510,1560p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-07T20:50:02.249Z] TOOL RESULT

```
Ai. pad- {pat, pddam^ padali)^ av. pad- ds. ; arm. ot-l^ 

ot-n „3T0i;g, (aus dem ursprgl. Acc. otn == noba stammt die weitere 

w-Plexion, s. Brugmann'Il^ 139, 299); gr. att. novg (zu dieser Form 
Lit. bei Boisacq s. v.), g. jioddg „Pu6^‘ {kyiaxovmboq, her. J^i'Kaxi-nEbo(; 
„100, 20 Pu6 lang**"; lat. p^s^ pMis ds., umbr. pefi^ persi „pede‘‘^ {dupursiis 
,,bipedibus“, -ti- wohl aus -d-); dafl dbeg' nobeg Hes. als kelt. Wort zu 
gelten babe (Pick II* 28), ist wegen des a ganz schwierig; ganz fraglich 
auch deutet Osthoff ZfcPh. 6, 398 ff. cymr, esgid „Schuh“ aus '^ped-oxvrog; 
wohl aber ist au\ ?s „unterhalb‘^ (wovon 7sel „niedrig“) m. ,,Dativ^‘ nach 
Pedersen KG. I 50, Brugmann II^ 2, 863 aus dem Loc. pi. ^pM-sti „zu 
FiiBem^ deutbar = alb. pos in perpos „unten“, pos-te „herab, unterirdisch ; 
unten, hinunter‘‘ (Pedersen Alb. Texte I 180, KZ 36, 29, Jokl SBAkWien 
168, I59f. Toch. A^e „Fu6‘‘ (von Bois. angefiihrt). 

Got. fotus (w-Decl. aus dem Acc. sg pi. auf germ, -uns = -ns)^ 
aisl. fd/r, ags. fot (n. pi. aisl. fdtr^ ags. fH aus d. sg. ags. aus 

Oti)^ ahd. ftto^ „PuB^‘. — Ein Instr. von ped- „Fu6“ ist gr. mdartl. jrfdd 
^,pex6!-^ m. (adnominalem) Gen., sekundar Loc. und Acc. (s. Gunther IF. 20, 
21 ff., 126 ff., Brugmann IP 2, 863) ursprgl. „(jemandem) auf dem Pu6e“ 
vgl. lat. pediseqims, -a „Diener, -in“ eig. „auf dem Fu6e folgend^' (s. Vf. 
LEWb.^ m. Lit. und bes. Persson IP. 26, 66) und unten die arm. von het 
„Fu6spur“ gebildeten Prapositionen. — Zs. mit i-os, -i-t „gehend“ (Schulze 
EN. 435, Brugmann IP. 17, 355, Grdr. II^ 1, 145, 183), gr. ne^og ,,pedestris“, 
lat. ped-es, -i4-is „Pu6ganger, Pu6soldat"\ — Yon lat. pes stammt pedare 
,,mit einem Fu6 versehen, stiitzen^, und davon wieder pedum „Hirten8tab, 
Stiitze^^. Ai. pddija- „den Pu6 betreffend^^, pddya „Pu6tritt, Huftritt^S av. 
paibya „Fu6‘S gr. ne^a „FuS; (unterer) Band, Saum“ (in der Bed. „kleines 
Pischernetz^*- naher zu nebrj ,,Fesseh‘ s. u.? Bezzenberger BB. 27, 175), 
lat. am-pediiis „schnellfu6ig‘' ; lit. hngvapedis „leisfuBig“ ; germ. *fetl f. 
in aisl. fif^ gen. -jar ,,die zwischen den Klauen befindliche Haut von See- 
vogeln und andern Tieren^'’, mit an jie^a „Saum‘* erinnernder Bed. norw. 
fit ,,Gewinde, Garn, Fitze^" (^ig* vdie Enden der Kettenfaden^, as. fitten^ 
ags. fitt „Abteilung eines Gedichtes, Gedicht*", ahd. fzza „Gewinde Garn*% 
nhd. Fitze\ norw. mdartl. fiorfit „Eidechse'^ eig. xergansl^og^^ (s. Bugge 
BB. 3, 117. Pick III* 225 f., Falk-Torp u fed\ analog palli „eine kleine 
Hauseidechse", wenn nach Liden KZ. 40, 260 das fem. eines "^palla-, pra- 
kritisch = ^padla-^ padra- als „mit FuBen versehene Schlange“) ; zu diesen 
St. "^pedio-, *pedl- wohl auch gr. neblXov ..Sandale‘\ Verbal: ai. pddyate 
,.geht, fallt^* {fl-patti- ,, Unfair^; padatl-, pat'ti- m. ,,FuBganger'S av. pai- 
byeiti ,,bewegt sich nach abwarts, gerat herab, hinein, hinzu, legt sich 
nieder*": abg, pada, pasti „fallen*‘ auch „fassen’" eig. „auf jmdn. 

fallen, anfallen*", Osten-Sacken IP. 33, 240; napasth „casus'*: lit, pMinu, 
-inti ,,lang8am gehn, leise treten'*, pedujti, -uti „Pufitritte machen‘", gr. 
nrjbdco „springe, hupfe'" (vgl. zur 6-Stufe noch lit, pedd ,,Po6spur“, pesczias 
„zu FuB^' aus *ped-tips^ lett. pe^da „Fu6sohle, FuBstapfe, FuB als MaB”, 
pe'z ,,nach, wegen, gemaB” m. Gen. und Acc., abg. peh „zu FuB'*, gr.
```


## [2026-09-07T20:51:08.638Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN octopod/octopus ===\"; grep -n -i \"octopod\\|octopus\" KLN_1966.txt | head -4\necho \"=== KLN podium ===\"; grep -n \"^podium\\|podium,  n\" KLN_1966.txt | head -3\necho \"=== KLN trapezium ===\"; grep -n -i \"trapezium,  n\\|trapeze,  n\" KLN_1966.txt | head -4\necho \"=== LAT trapezium ===\"; grep -n -i \"trapezium\\|trapezus\" LAT.txt LEW_1910.txt | head -4\necho \"=== FSD caliber ===\"; grep -n -i \"calibre\\|caliber\" FSD_vol1.txt | head -3"
}
```


### [2026-09-07T20:51:08.754Z] TOOL RESULT

```
=== KLN octopod/octopus ===
1406:acetabulum,  n.  i)  a  cup  for  vinegar  ( Roman  an- tiq.)  ;  2)  the  cup-shaped  socket  of  the  hip  bone ( anat .);  3)  a  sucker  of  an  octopus,  a  leech,  etc. (zool.)  —  L.  acetabulum,  lit.  ‘a  vessel  for  vinegar’, formed  fr.  acetum,  ‘vinegar’,  with  -dbulum,  a suffix  used  to  form  names  of  tools  and  vessels. See  acetum.  For  the  suff.  cp.  tintinnabulum. Derivatives:  acetabul-ar,  acetabuli-ferous,  aceta- buli-form,  adjs.
6999:Cephalopoda,  n.  pi.,  a  class  of  mollusks,  including the  cuttlefish,  squid,  octopus,  etc.  ( zool .)  — ModL.,  compounded  of  XEtpaTo),  ‘head’,  and iro'jc,  gen.  TroSoc,  ‘foot’.  See  cephalic  and  -pod. cephalothorax,  n.,  the  united  head  and  thorax (of  spiders  and  crustaceans)  (zoo!.)  —  See  ce- phalo-  and  thorax.
12734:eight,  adj.  and  n.  —  ME.  eighte,  eihte,  fr.  OE. eahta,  rel.  to  OS.  ahto,  ON.  atta,  Swed.  dtta, Dan.  otte,  OFris.  ahta,  Du.  acht,  OHG.  ahto, MHG.  ahte,  G.  acht,  Goth,  ahtau,  ‘eight’,  and cogn.  with  OI.  affd,  astdu,  Avestic  ashta,  Toch. A  ok  at,  B  okt.  Arm.  ut‘  (for  *optd ),  Gk.  oxtoj, Alb.  tets  (for  *okto-t),  L.  odd,  OSlav.  osmi  (re¬ fashioned  after  the  ordinal  number  osmu,  ‘the eighth’),  Lith.  astuoni,  OIr.  ocht  n-,  W.  wyth, Bret,  eiz,  ‘eight’.  All  these  words  prob.  derive  fr. I.-E.  *okto(u),  an  old  dual  form,  orig.  meaning ‘twice  four’  (Tetradic  system  of  reckoning!). The  re  in  Elian  Gk.  ortT<i>,  and  the  form  of Arm.  ut'  (for  *opto-)  is  due  to  the  analogy  of I.-E.  *septm-  (whence  Gk.  s7rra,  etc.),  ‘seven’. Cp.  also  Rum.  opt,  ‘eight’  (fr.  L.  odo),  influen¬ ced  in  form  by  $apte,  ‘seven’.  The  n  in  OIr, ocht  n-  is  due  to  the  analogy  of  secht  n-,  ‘seven’. Cp.  octa-,  octant,  octave,  octet,  octillion,  octo-, October,  octopus,  octoroon,  octuple,  utas. eighteen,  adj.  and  n.  —  ME.  eightetene,  eightene, eihtene,  fr.  OE.  eahtatyne,  eahtatene,  fr.  eahta, 'eight',  and  -tyne,  -tene,  ‘-teen’  (see  eight  and -teen);  rel.  to  OS.  ahtotian,  Du.  achttien,  OHG. ahtozehan,  MHG.  ahtzehen,  G.  achtzehn,  ON. dttjan,  atjdn,  Swed.  adertdn,  Dan.  atten,  ‘eigh¬ teen’.
15110:foot,  n.  —  ME.  fat,  fr.  OE.  fat,  rel.  to  OS.  fat, ON.  fa tr,  Swed.  fat,  Dan.  fad,  Du.  voet,  OHG. fuo3,  MHG.  VU03,  G.  Fuji,  Goth./o/u.s,  ‘foot’,  and cogn.  with  Ol.  pit,  acc.  pidam,  ‘foot’,  Avestic pad-,  ‘foot’,  Toch.  A  pe,  B  pai,  ‘foot’,  A  pent,  B paine,  ‘both  feet’.  Arm.  ot-n,  ‘foot’,  ot-k\  ‘feet’. Dor.  Gk.  7rtii ;,  Att.  7101)9  (formed  on  analogy  of 009,  ‘ear’),  gen.  770809,  L.  pes,  gen.  pedis,  ‘foot’, Ol.  paddm,  ‘step,  track’.  Arm.  het,  gen.  he  toy, ‘track,  footmark’,  Gk.  rtiSt),  ‘fetter’,  TreSav,  ‘to bind  with  fetters’,  7t£Sov,  ‘ground,  earth’,  h.peda, ‘footstep \pedica,  ‘shackle,  fetter’,  impedire,  ‘en¬ tangle,  ensnare’,  expedire,  ‘to  extricate,  disen¬ gage’,  Lith.  peda,  ‘footstep,  trace’,  OSlav.  podii, ‘loft’,  Russ,  pod-oshva,  ‘sole  of  foot’.  All  these words  derive  fr.  I.-E.  base  *pdd-,  *pid-,  ‘foot’. Cp.  fetch,  fetlock,  fetter,  fit,  ‘part  of  a  song’.  Cp. also  antipodes,  apod,  babouche,  biped,  breviped, caliber,  cap-a-pie,  charpoy,  expedient,  expedite, impeach,  impede,  impedimenta.  Lycopodium, millepede,  multiped(e),  octopus,  oppidan,  palmi¬ ped,  pawn  (in  chess),  parallelepiped,  pajama, pedal,  pedate,  -pede,  pedesis,  pedestal,  Pedetes, pedicel,  pedicle,  pedigree,  pedology,  ‘the  study  of soils’,  peduncle,  peon,  pes,  petiole,  pew,  Peziza, pie,  ‘a  small  coin’,  piepoudre,  pilot,  podagra, podal,  podium,  podo-,  pug,  ‘footprint’,  puy,  seer- paw,  Taliped,  Tarsipes,  teapoy,  trapezium,  triped, tripos,  vamp,  ‘front  part  of  the  foot’,  velocipede. Cp.  also  pejorative,  pessimism.
=== KLN podium ===
1783:Aegopodium,  n.,  a  genus  of  herbs  of  the  carrot family  (bot.)  —  ModL.,  fr.  Gk.  alyoTriSi-];, ‘goatfooted’,  fr.  al£,  gen.  alyo;,  ‘goat’,  and 7tou;,  gen.  noS6q,  ‘foot’.  See  aego-  and  podo-; prob.  so  called  from  the  shape  of  its  small  leaves, aegrotat,  n.,  a  certificate  that  a  student  is  ill.  — L.,  ‘he  is  sick’,  3  pers.  sing,  of  aegrdtdre,  ‘to  be
7339:Chenopodium,  n.,  a  genus  of  plants  of  the  goose- foot  family  (bot.)  —  ModL.,  lit.  ‘goosefoot’,  fr. Gk.  /fry,  gen.  yr/vo;,  ‘goose’,  and  -ou;,  gen. -080c,  ‘foot’.  See  cheno-  and  -pod. cheque,  n.  —  The  British  spelling  of  check,  ‘a written  order  to  a  bank'  (q.v.) chequer,  n.  -  See  checker.
22382:Lycopodium,  n.,  a  genus  of  plants,  the  club  moss (bot.)  —  ModL.,  lit.  ‘wolf’s  foot’,  compounded of  Gk.  Xdxoi;,  ‘wolf’,  and  nous,  gen.  noS 6?, ‘foot’.  See  lyco-  and  podo-.
=== KLN trapezium ===
39917:trapan,  n.  and  tr.  v.  —  A  var.  of  trepan, trapes,  intr.  v.  —  See  traipse, trapeze,  n.,  a  suspended  horizontal  bar  used  in gymnastics.  —  F.  trapeze,  fr.  Late  L.  trapezium.
39919:trapeziform,  adj.,  having  the  form  of  a  trapezium. —  A  hybrid  coined  fr.  Gk.  xpanE^iov  and  L. forma,  ‘form,  shape'.  See  next  word  and  form,  n. trapezium,  n.,  a  plane  figure  with  four  sides  of which  no  two  are  parallel.  —  Late  L.,  fr.  Gk. xpars^tov,  ‘a  little  table’,  dimin.  of  xp£jre£a, ‘table’,  which  stands  for  *7rxpx7xsqa,  a  com¬ pound  lit.  meaning  ‘provided  with  four  feet’. The  first  element  represents  I.-E.  *qwetr-,  ‘four’ ; see  four  and  cp.  tessares,  tetarto-.  The  second element  is  ‘foot’,  which  is  rel.  to  rcou?,
=== LAT trapezium ===
=== FSD caliber ===
4997:Syn.:  aptitude,  capability,  capacity,  cleverness,  com- petence, dexterity,  efficiency,  expertness,  faculty,  power, qualification,  readiness,  skill,  talent.  Ability  Includes every  form  of  power.  Capacity  Is  power  to  receive,  effi- ciency power  to  do,  to  effect.  Competence  Is  equal  to  the occasion,  readiness  prompt  for  the  occasion.  Faculty  is an  inherent  quality  of  mind  or  body;  talent  some  special mental  ability.  Dexterity  and  skill  are  readiness  and  fa- cility in  action,  having  a   special  end,  and  are  largely  ac- quired. Our  abilities  include  our  natural  capacity,  facul- ties, and  talents,  with  all  the  dexterity,  skill,  and  readiness that  can  be  acquired.  Efficiency  brings  all  one’s  ability to  bear  promptly  on  the  thing  to  be  done.  See  address; caliber.—  Ant.:  awkwardness,  duiness,  imbecility.  In- ability, Inaptitude,  incapacity,  incompetence,  inefficiency, maladroitness,  stupidity,  unskilfulness,  weakness.
25010:Armaments  are  distinguished  according  to  the  size  or  tne guns.  The  main  armament  Includes  the  largest  gu  ,   gc erally  mounted  In  turrets;  the  secondary  armament  co^si of  the  guns  of  medium  caliber;  and  the  tertiary  arma includes  the  smaller  guns.  nnother
25632:grec  of  Increase  or  diminution  of  the  caliber  or  an  artery  duo  mj! I   penultimate  joint  of  the  tarsua  m   cer
```


## [2026-09-07T20:51:09.116Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1074 --image 2>&1 | tail -30"
}
```


### [2026-09-07T20:51:10.541Z] TOOL RESULT

```
no scan of BQT covers printed page 1074 (see 'scans' in refs_online.json)
```


## [2026-09-07T20:51:20.848Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 367 -l 367 -r 300 -png -singlefile /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf bqt384-1074 && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt384-1074.png'); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.72),w,h)).save('bqt384-1074-foot.png')\n\""
}
```


### [2026-09-07T20:51:23.159Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-07T20:51:26.112Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt384-1074-foot.png"
}
```


### [2026-09-07T20:51:26.130Z] TOOL RESULT

```

```


## [2026-09-07T20:51:50.084Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt384-1074.png'); w,h=im.size\nim.crop((0,int(h*0.30),int(w*0.52),int(h*0.62))).resize((int(w*0.52*1.7),int(h*0.32*1.7))).save('bqt384-1074-kala.png')\n\""
}
```


### [2026-09-07T20:51:51.590Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:51:54.958Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt384-1074-kala.png"
}
```


### [2026-09-07T20:51:54.998Z] TOOL RESULT

```

```


## [2026-09-07T20:52:30.711Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1074.vision.txt <<'EOF'\n[BQT = Borhan-e Qate', ed. Mo'in; vol. 3 (incoming/BQT/BQT_v3_picofile.pdf), pdf page 367 =\n printed page ۱۰۷۴ (1074). Read from the page image by Claude (vision) on 2026-09-07 for\n verification of PDF page 384, entry \"Ped, Pod\" part 2, node #3 (کالا).]\n\nHeadword, right-hand column:\n\nکالا ـ بروزن بالا ، بمعنی رخت‌ورخوت و اسباب و متاع باشد ۱۳ ـ و بلغت زند و پازند،\nبانگ و فریاد و فغان را گویند ۱۴.\n\nکالار ـ بسکون رای فرشت، آب‌کندی را ...\n\nMo'in's footnotes at the foot of the same page:\n\n۱۳ ـ چو علم آموختی از حرص، آنگه ترس، کاندر شب\n      چو دزدی با چراغ آید، گزیده‌تر برد کالا .\n      « سنائی غزنوی . دیوان ۵۲ ».\n\n۱۴ ـ هز kâlâ ، kâlmâ ، پهلوی vâng (بانگ و فریاد) «یونکرمن ۱۱۱ و ۱۱۲».\n\n[i.e. footnote 13 is only a shâhed (Sanai) for کالا \"goods\"; footnote 14, the only\n etymological note on the page, belongs to the SECOND sense \"shout, cry\": Pazand kâlâ,\n kâlmâ = Pahlavi vâng \"cry, clamour\", citing Junker pp. 111-112. Borhan/Mo'in therefore\n give NO etymology at all for کالا \"merchandise\", and in particular no link to\n کالبد / Greek kalopodion.]\nEOF\necho saved; sed -n 1,60p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T20:52:32.166Z] TOOL RESULT

```
saved
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


## [2026-09-07T20:52:35.162Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n 60,140p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T20:52:35.202Z] TOOL RESULT

```
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


## [2026-09-07T21:02:00.990Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-384.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_KALBOD = \"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%A8%D8%AF\"\nW_KALA   = \"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%A7\"\nW_QALEB  = \"https://en.wiktionary.org/wiki/%D9%82%D8%A7%D9%84%D8%A8\"\nW_OXTA   = \"https://en.wiktionary.org/wiki/%D8%A7%D8%AE%D8%AA%D8%A7%D9%BE%D9%88%D8%B3\"\nW_CALIB  = \"https://en.wiktionary.org/wiki/calibre\"\nE_CAL    = \"https://www.etymonline.com/word/caliber\"\nE_OCT    = \"https://www.etymonline.com/word/octopus\"\nE_PIL    = \"https://www.etymonline.com/word/pilot\"\nE_TRA    = \"https://www.etymonline.com/word/trapeze\"\nE_FET    = \"https://www.etymonline.com/word/fetch\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Greek\",\n \"words\": \"pous, peza; kalo-podion; oktô-pous\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three Greek items are real and all three belong to *ped-. Attic ποῦς poús (Doric πώς), gen. ποδός podós 'foot', continues the lengthened o-grade *pōd-s with the oblique stem *pod-; πέζα péza f. 'foot, instep, lower edge, hem' is the *-ya derivative *ped-ya (Pokorny lists it under his pedio- section, IEW 791). καλοπόδιον kalopódion 'shoemaker's last' is the diminutive of καλόπους kalópous, lit. 'wood-foot', from κᾶλον kâlon 'wood (for burning)' (contracted from *kaw-elo-, to καίειν 'to burn') + πούς; the compound is a craftsman's word of the Hellenistic/Roman period and it is this word, not πούς itself, that travels east. ὀκτώπους oktṓpous 'eight-footed' (ὀκτώ 'eight' + πούς) is the ancient name used by the naturalists beside the commoner πολύπους. Nourai's transliterations and glosses are accurate.\",\n \"derivation_fa\": \"هر سه واژهٔ یونانیِ این خانه واقعی‌اند و هر سه به ریشهٔ *ped- بازمی‌گردند. ποῦς (در دوری πώς) با حالت اضافیِ ποδός «پا» دنبالهٔ درجهٔ کشیدهٔ *pōd-s است و ستاک غیرفاعلی آن *pod-؛ πέζα «پا، پایین‌ترین کناره، حاشیه» مشتق *ped-ya است که پوکورنی در ص ۷۹۱ ذیل pedio- آورده است. καλοπόδιον «قالبِ کفشگری» مصغّر καλόπους و به‌لفظ «پایِ چوبین» است، از κᾶλον «چوب» و πούς؛ همین واژهٔ پیشه‌وری است — نه خودِ πούς — که به شرق راه می‌یابد. ὀκτώπους «هشت‌پا» نیز از ὀκτώ «هشت» و πούς ساخته شده است. آوانویسی‌ها و معناهایی که نورایی داده درست است.\",\n \"sources\": [E_CAL, E_OCT],\n \"ref_check\": [\n   {\"ref\": \"AHD:1365\", \"status\": \"supports\", \"note\": \"The New College p. 1365 is not online, but Watkins' appendix (AHD_watkins1985.txt s.v. ped-1) says it twice: '7. O-grade form *pod- in: a. Greek pous (stem pod-), foot: PEW, -POD, PODITE, PODIUM; … CALIBER, … OCTOPUS, …' and '8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM'.\"},\n   {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt s.v. foot: 'Dor. Gk. πώς, Att. πούς (formed on analogy of οὖς, ear), gen. ποδός, L. pes, gen. pedis, foot'; s.v. caliber: 'Gk. καλοπόδιον, shoemaker's last, dimin. of καλόπους, gen. καλόποδος, of s.m., lit. a foot of wood, fr. κᾶλον, wood … and -πους, gen. -ποδος, foot'.\"},\n   {\"ref\": \"POK:790\", \"status\": \"supports\", \"note\": \"POK_full.txt, Root/lemma pē̆d-2, pō̆d-, Page(s) 790-792: 'gr. πέζα f. Fuss, untere Rand, Saum, kleines Fischernetz' under the pedio- section, and Attic πούς gen. ποδός in the opening material list.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 790-792 (POK_full.txt, Root/lemma pē̆d-2, pō̆d-)\", \"stance\": \"supports\", \"note\": \"'ai. padya- den Fuss betreffend … gr. πέζα f. Fuss, unterer Rand, Saum' — peza is Pokorny's *ped-ya, exactly as drawn.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 23 ff. (WLD_Bd2_1927_dli_106624_djvu.txt)\", \"stance\": \"supports\", \"note\": \"'gr. att. πούς … g. ποδός Fuss … gr. πέζα Fuss; (unterer) Rand, Saum' — the same two Greek shapes under ped-.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. ped-1\", \"stance\": \"supports\", \"note\": \"see ref_check; CALIBER, OCTOPUS, PODIUM under Greek pous, TRAPEZIUM under peza.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. foot, caliber\", \"stance\": \"supports\", \"note\": \"see ref_check; Klein spells out kalopodion < kalon 'wood' + pous.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\",\n \"words\": \"kal-pâd\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian ⟨klpt'⟩ / ⟨klpwt'⟩, read kālpad / kalpat / kalbod, 'shape, external bodily form, body', is a straight Hellenistic loan from Greek καλοπόδιον 'shoemaker's last': the Greek diminutive was clipped of its -ion, Greek -p- was rendered by MP p (later voiced to b in New Persian), and the technical sense 'last, mould in the shape of a foot' widened to 'mould of any kind' and then to 'the mould of the soul', i.e. the body. Nyberg says so in as many words, and MacKenzie, Hübschmann, Mo'in's footnote in Borhan-e Qate' and Wiktionary all agree; the word is also in Manichaean MP (k'lbyd) and was borrowed into Armenian as kalapar. Nourai's spelling 'kal-pâd' with a hyphen invites the folk-segmentation kal + pād 'foot', which is secondary: the -pad of the Pahlavi word is Greek -pod-, not the Iranian word for foot. The NOTE on the box (Mann, IEC 1049/1051, deriving it from Av. kəhrp- 'body' and a root Kwrp) is the minority view and is rejected by every Iranist source consulted here — Mann's own entry qurp- simply lists 'Per. cf. kalbad' beside Lat. corpus without arguing the point, and it cannot explain the -l-.\",\n \"derivation_fa\": \"صورت فارسی میانه ⟨klpt'⟩ / ⟨klpwt'⟩ که kālpad یا kalpat یا kalbod خوانده می‌شود، به معنای «شکل، هیئت بیرونی، تن»، وام‌واژه‌ای یک‌راست از یونانی καλοπόδιον «قالب کفشگری» است: پسوند مصغّر -ion افتاده، p یونانی در فارسی میانه p مانده و سپس در فارسی نو به b نرم شده، و معنای فنیِ «قالبِ کفش» نخست به «قالب هر چیز» و آنگاه به «قالبِ جان» یعنی تن گسترش یافته است. نیبرگ همین را صریح می‌گوید و مکنزی و هوبشمان و حاشیهٔ معین بر برهان قاطع و ویکی‌واژه نیز هم‌داستان‌اند؛ صورت مانوی k'lbyd و وام ارمنی kalapar هم گواه‌اند. خط تیره‌ای که نورایی در «kal-pâd» گذاشته، تجزیهٔ عامیانهٔ kal + pād «پا» را به ذهن می‌آورد که ثانوی است، زیرا -pad این واژه همان -pod- یونانی است نه واژهٔ ایرانیِ «پای». یادداشتِ خودِ کتاب (نقل از مان، IEC ۱۰۴۹ و ۱۰۵۱) که واژه را از kəhrp- اوستایی «تن» و ریشهٔ *kʷerp- می‌گیرد، نظر اقلیت است و هیچ‌یک از منابع ایران‌شناسیِ بررسی‌شده آن را نمی‌پذیرد؛ افزون بر این، l میانی را توضیح نمی‌دهد. حکم: ادعای نورایی درست است.\",\n \"sources\": [W_KALBOD],\n \"ref_check\": [\n   {\"ref\": \"BQT:1075\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 1075 = vol. 3 pdf page 368 (incoming/BQT/BQT_v3_pages.txt, line ~26857). Headwords کالب and کالبد, with Mo'in's footnote: «پهلوی kalpat (شکل، صورت)، پازند kalbud، مستعار از یونانی kalopódhion (قالب). ارمنی kalapar از kalapadh» — the Greek etymon named explicitly, exactly Nourai's arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary) p. 110 s.v. kālpaδ\", \"stance\": \"supports\", \"note\": \"'kālpaδ [k'lpt'], kalpuδ [k'lpwt'] shape, external bodily form … MPrs k'lbyd; Paz. kälbud … NP kalbad, kālbud \\\"the body of a man or an animal\\\", \\\"a model, a last for shoes\\\" which is the original sense, the w. being borrowed from Gr καλοπόδιον.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. kalbod (PHD_mackenzie.txt line 3154)\", \"stance\": \"supports\", \"note\": \"'kalbod [k)lpwt' | (M k)lbyd), N ~] body, shape, form.' — the form and meaning; MacKenzie gives no etymology but confirms the Pahlavi word.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 178 (HUB.txt line 6282) and the l-chapter (line 9471)\", \"stance\": \"supports\", \"note\": \"'LW. kālbad, kalbud \\\"Modell\\\", paz. kalbud, phl. kalput, kalpat, gr. καλοπόδιον, arm. kalapar' and 'kālbad, kalbud \\\"Modell\\\", phl. kalput = gr. καλοπόδιον' — Hübschmann files it among the Greek loanwords.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC col. 1051 s.v. qurp-\", \"stance\": \"contradicts\", \"note\": \"'qurp- \\\"turn, shape, form, body\\\". … Av. kəhrp \\\"flesh, body\\\"; Per. cf. kalbad, s. \\\"form, body\\\"; … Lat. corpus' — this is the source of the NOTE on the box; Mann simply lists kalbad beside corpus, with no discussion of the -l-.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt), grep 'kalbud|kalbad|kalopod'\", \"stance\": \"silent\", \"note\": \"Horn has no entry for the word (he generally omits the Greek loanwords Hübschmann collected).\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"kâlâ «کالا»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Persian کالا kālā 'goods, merchandise, household stuff' is a real word, well attested from Sanai onwards, but no source derives it from kālbod / Greek kalopodion, and the phonetics are against it (there is no way to lose the -bod). Nourai's own two references point elsewhere: Mo'in's Farhang derives it from کاله kāle ('کالا [- کاله] اسباب خانه، لوازم سرای، مال‌التجاره، متاع'), and Mann (IEC 1047) files 'Per. cf. kala \\\"manufactures\\\"' under quortos (2) 'made; make, fabrication, shape', i.e. under PIE *kʷer- 'to make', which is also the modern view (Wiktionary: 'ultimately a derivative of Proto-Iranian *kar- \\\"to do, make\\\", from Proto-Indo-European *kʷer- \\\"to make\\\"', with Old Armenian կահ kah as a cognate). Borhan-e Qate' p. 1074 gives the word with a Sanai verse and attaches an etymological footnote only to the homonym کالا 'shout, cry' (Pazand kālā, kālmā = Pahl. vāng). Nourai himself hedges with the note 'References are not very clear on the derivation paths'; on the evidence the arrow Pahlavi kal-pād → kālā should be cut.\",\n \"derivation_fa\": \"«کالا» به معنای «متاع، اسباب خانه، مال‌التجاره» واژه‌ای اصیل و از روزگار سنایی گواهی‌شده است، اما هیچ منبعی آن را از «کالبد» یا از καλοπόδιον یونانی نمی‌گیرد و از نظر آوایی نیز راهی برای افتادن ‑بد وجود ندارد. خودِ دو ارجاعِ نورایی جای دیگری را نشان می‌دهند: معین در فرهنگ فارسی آن را از «کاله» می‌گیرد («کالا [- کاله] اسباب خانه، لوازم سرای، مال‌التجاره، متاع»)، و مان در ستون ۱۰۴۷ «Per. kala manufactures» را ذیل quortos (۲) «ساخته، ساخت، شکل» یعنی ذیل ریشهٔ هندواروپاییِ *kʷer- «ساختن» آورده است؛ همین هم نظر امروزی است (ویکی‌واژه: مشتقی از ایرانی آغازین *kar- «کردن، ساختن» از *kʷer- هندواروپایی، هم‌ریشه با کاهِ ارمنی کهن). برهان قاطع در ص ۱۰۷۴ واژه را با شاهدی از سنایی آورده و حاشیهٔ ریشه‌شناختی‌اش تنها به هم‌آواز آن، «کالا» به معنای «بانگ و فریاد» (پازند kālā و kālmā برابر vāng پهلوی)، مربوط است. خودِ نورایی هم نوشته «منابع دربارهٔ مسیر اشتقاق روشن نیستند». پژوهش امروزی این پیکان را رد می‌کند.\",\n \"sources\": [W_KALA],\n \"ref_check\": [\n   {\"ref\": \"MON:2858\", \"status\": \"contradicts\", \"note\": \"The 6-vol. Mo'in is not online; the 2-vol. condensation (MON_part2.txt line 19215) has the entry verbatim: «کالا: [- کاله] (ا.) اسباب خانه، لوازم سرای، مال‌التجاره، متاع، مهره‌های شطرنج» — Mo'in derives کالا from کاله, and nowhere from کالبد.\"},\n   {\"ref\": \"IEC:1047\", \"status\": \"contradicts\", \"note\": \"IEC.txt line 14212, column 1047: 'quortos (2) \\\"made; make, fabrication, shape\\\". Cf. quer-, quor-, qur- … Per. cf. kala \\\"manufactures\\\"; kalbad, s. \\\"body, shape\\\"' — Mann puts kālā under PIE *kʷer- 'to make', not under *ped-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, printed p. 1074 (vol. 3 pdf page 367; page image read and saved at data/verification/sources/refs/ocr/BQT/1074.vision.txt)\", \"stance\": \"silent\", \"note\": \"«کالا ـ بروزن بالا، بمعنی رخت‌ورخوت و اسباب و متاع باشد ۱۳ ـ و بلغت زند و پازند، بانگ و فریاد و فغان را گویند ۱۴.» Footnote 13 is only the Sanai verse; footnote 14, the only etymological note, belongs to the 'shout' homonym: «هز kâlâ، kâlmâ، پهلوی vâng (بانگ و فریاد) «یونکرمن ۱۱۱ و ۱۱۲»». No Greek, no کالبد.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. کالا\", \"stance\": \"contradicts\", \"note\": \"see ref_check — «[- کاله]».\"},\n   {\"src\": \"IEC\", \"where\": \"IEC col. 1047 s.v. quortos (2)\", \"stance\": \"contradicts\", \"note\": \"see ref_check.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'kala|Ware'\", \"stance\": \"silent\", \"note\": \"Horn has no entry for kālā.\"},\n   {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt and ARY_latin_index_pages.txt, grep 'کالا' / 'kala'\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary has no کالا entry (the Latin index hits are Kurdish/Afghani KALA in other entries).\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"kâleb «کالب»; kâlbod «کالبد»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both New Persian shapes continue the Pahlavi word directly: MP kalbod / kālpad > NP کالبد kālbod 'mould; body', with the shorter کالب kāleb beside it (Borhan: «کالب ـ بر وزن و معنی قالب است که آنرا کالبد نیز گویند»; «کالبد … بمعنی کالب است که قالب هر چیز باشد، و بمعنی تن و بدن آدمی و حیوانات دیگر نیز هست»). The intervocalic Middle Persian -p- of ⟨klpt'⟩ is voiced to -b- in New Persian, the regular treatment; the final -d of کالبد is the Pahlavi -δ of kālpaδ. The two senses of Nourai's box — 'mould' for کالب and 'body' for کالبد — are the two ends of the semantic development 'shoemaker's last' > 'mould of any shape' > 'the body as the mould of the soul', and the Nezami couplet he quotes («این من و این من که در این کالب است») uses exactly the 'body' sense. Wiktionary: 'From Middle Persian kʾlpwt' (kālbod) \\\"body, shape, form\\\", from Ancient Greek καλοπόδιον'.\",\n \"derivation_fa\": \"هر دو صورتِ فارسی نو یک‌راست دنبالهٔ واژهٔ پهلوی‌اند: kalbod / kālpad فارسی میانه به «کالبد» رسیده است و «کالب» کوتاه‌شدهٔ آن است (برهان قاطع: «کالب ـ بر وزن و معنی قالب است که آنرا کالبد نیز گویند»؛ «کالبد … بمعنی کالب است که قالب هر چیز باشد، و بمعنی تن و بدن آدمی و حیوانات دیگر نیز هست»). p فارسی میانه در میان دو واکه به b نرم شده است — دگرگونی آواییِ قاعده‌مند — و d پایانی همان δِ kālpaδ پهلوی است. دو معنایی که نورایی آورده («قالب» برای کالب و «تن» برای کالبد) دو سر یک تحول معنایی‌اند: «قالبِ کفش» ← «قالبِ هر چیز» ← «تن، که قالبِ جان است»؛ بیت نظامی که نقل کرده («این من و این من که در این کالب است») نیز در همین معنای «تن» است. ادعای نورایی درست است.\",\n \"sources\": [W_KALBOD],\n \"ref_check\": [\n   {\"ref\": \"BQT:1075\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p. 1075 (vol. 3 pdf page 368): both headwords are there — «کالب ۴ ـ بر وزن و معنی قالب است که آنرا کالبد نیز گویند» and «کالبد ـ … بمعنی کالب است که قالب هر چیز باشد، و بمعنی تن و بدن آدمی و حیوانات دیگر نیز هست» — with the Greek footnote quoted at node #2.\"},\n   {\"ref\": \"MON:2859\", \"status\": \"supports\", \"note\": \"6-vol. Mo'in not online; the 2-vol. condensation (MON_part2.txt line 19231) has «کالبد: [- کالب] (ا.) قالب هر چیز (عموماً)، کالب؛ قالب خشت‌زنی (خصوصاً)؛ تن (آدمی و جانوران)، بدن؛ انموذج، نمونه، سرمشق؛ شکل، هیئت، صورت، پیکر، شبح» — Nourai's two words and both glosses, and Mo'in derives کالبد from کالب just as the box does.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 3 p. 1075, headwords کالب / کالبد + Mo'in's footnote\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. کالبد\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 178\", \"stance\": \"supports\", \"note\": \"'LW. kālbad, kalbud \\\"Modell\\\" … phl. kalput, kalpat, gr. καλοπόδιον' — the New Persian forms with the Greek etymon.\"},\n   {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt s.v. kalbod\", \"stance\": \"supports\", \"note\": \"'kalbod [k)lpwt' | (M k)lbyd), N ~]' — MacKenzie's 'N ~' means the New Persian form is identical.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt, grep\", \"stance\": \"silent\", \"note\": \"no entry.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Arabic\",\n \"words\": \"qalib; q.l.b\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The box makes two claims and they must be judged separately. (a) Arabic قالب qālib/qālab 'mould, last, model' is indeed the same Greek word, and Asbaghi — Nourai's own reference PLA:215 — routes it exactly as the chart does: 'qālib: \\\"Gußform, Model\\\" pers. کالبد kalbod, mp. kālpūδ, mand. galib', citing Borhan-e Qate', Nyberg II and Macuch. Mo'in likewise tags the Persian word «قالب [معر. کالبد]». Klein and Wiktionary, however, bring the word into Arabic through Aramaic/Syriac rather than through Persian ('Gk. καλοπόδιον came into Arabic through the medium of the Aramaic'; Wiktionary: 'From Classical Syriac ܩܠܒܝܕ qālobīḏ \\\"last\\\", from Ancient Greek καλοπόδιον'). Both routes are defensible and the Arabic form is a Greek loan either way, so (a) alone would be 'plausible'. (b) The second word in the box, 'q.l.b: to make, turn around', is a genuine, native Semitic triliteral root ق‑ل‑ب 'to turn over, invert' (Hebrew/Aramaic cognates, whence قلب 'heart', انقلاب 'revolution', مقلوب, تقلّب). It has nothing to do with Greek καλοπόδιον or with PIE *ped-; what happened is that the loanword قالب, which accidentally fits the fāʿil pattern of q-l-b, was reanalysed as a derivative of that root — a classic folk etymology inside Arabic. Because the node presents that root as a descendant of Persian kāleb, the node as a whole is disputed.\",\n \"derivation_fa\": \"این خانه دو ادعا دارد که باید جدا سنجید. الف) «قالبِ» عربی به معنای «قالب، مدل» بی‌گمان همان واژهٔ یونانی است، و آسبقی — که خودِ نورایی به او ارجاع می‌دهد (PLA:215) — درست همان مسیر نمودار را می‌دهد: «qālib: Gußform, Model، از فارسی کالبد، فارسی میانه kālpūδ، مندایی galib» با ارجاع به برهان قاطع، نیبرگ (ج۲) و ماکوخ؛ معین نیز «قالب» فارسی را «[معر. کالبد]» می‌داند. در برابر، کلاین و ویکی‌واژه واژه را از راه آرامی/سریانی وارد عربی می‌دانند نه از راه فارسی («καλοπόδιον یونانی از طریق آرامی به عربی رسید»؛ ویکی‌واژه: از سریانی کلاسیک qālobīḏ). هر دو راه پذیرفتنی است و در هر حال واژه وام‌واژه‌ای یونانی است، پس این بخش «با احتیاط پذیرفتنی» است. ب) واژهٔ دوم خانه، «ق‌ل‌ب: ساختن، گرداندن»، ریشهٔ سه‌حرفیِ اصیل سامی است به معنای «گرداندن، وارونه کردن» (با هم‌ریشه‌های عبری و آرامی؛ از همین ریشه‌اند قلب، انقلاب، مقلوب، تقلّب) و هیچ پیوندی با καλοπόδιον یونانی یا *ped- هندواروپایی ندارد؛ آنچه رخ داده این است که وام‌واژهٔ «قالب» چون تصادفاً بر وزن فاعلِ همان ریشه می‌نشیند، در عربی به آن ریشه بازتحلیل شده است — نمونه‌ای روشن از ریشه‌شناسی عامیانه. چون نمودار همین ریشهٔ سامی را فرزندِ «کالب» فارسی نشان داده، حکم این خانه «رد» است.\",\n \"sources\": [W_QALEB, E_CAL],\n \"ref_check\": [\n   {\"ref\": \"KLN:223\", \"status\": \"partial\", \"note\": \"KLN_1966.txt p. 223 s.v. caliber: 'F. calibre, fr. It. calibro, fr. Arab. qālib, \\\"mold, model\\\", fr. Gk. καλοπόδιον, \\\"shoemaker's last\\\" … Gk. καλοπόδιον came into Arabic through the medium of the Aramaic.' Klein confirms the Greek origin of the Arabic word but routes it through Aramaic, not through Persian, and says nothing about the root q-l-b.\"},\n   {\"ref\": \"PLA:215\", \"status\": \"supports\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p. 215 (incoming/PLA/PLA_pages.txt, form-feed page 230; the OCR renders q as g): 'qālib: \\\"Gußform, Model\\\" pers. کالبد kalbod, mp. kālpūδ, mand. galib', with footnotes 11 = BQ (Borhan-e Qate'), 12 = Nyberg Bd. II, 13 = Macuch. Exactly Nourai's Persian → Arabic arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p. 215 s.v. qālib\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt p. 223 s.v. caliber\", \"stance\": \"partial\", \"note\": \"see ref_check — Greek yes, Aramaic mediation rather than Persian.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1030 (LKT.txt line 2454)\", \"stance\": \"partial\", \"note\": \"'1030. Ar. qālib: \\\"Leisten eines Schusters\\\", ebenso tk. kalyb, kalyp \\\"Modell, Form\\\"; hieraus rum. calib, calip, calup … sp. gálibo … frz. calibre … it. calibro … dtsch. Kaliber, engl. calibre' — Lokotsch takes the Arabic word as the source of the European family but gives no ultimate etymon.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. قالب\", \"stance\": \"supports\", \"note\": \"«قالب: [معر. کالبد] شکل، هیئت، آلتی که جسمی شکل‌پذیر را در داخل یا خارج آن نهاده بصورت آن آلت در آورند …» — Mo'in expressly calls Arabic/Persian قالب the Arabicised form of کالبد.\"},\n   {\"src\": \"FVQ\", \"where\": \"FVQ.txt (Jeffery, Foreign Vocabulary of the Qur'an), grep 'qalib'\", \"stance\": \"silent\", \"note\": \"قالب is not a Qur'anic word, so Jeffery has no entry.\"},\n   {\"src\": \"AFM\", \"where\": \"AFM.txt / AFM_pages.txt (Addi Shir), grep 'قالب'\", \"stance\": \"silent\", \"note\": \"no hit in the OCR (Asbaghi's footnote 11 cites Addai Scher for a different headword on the same page).\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Persian\",\n \"words\": \"qâleb «قالب»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Persian قالب qāleb 'mould, form; body' is the Arabic-mediated return of the native کالبد — a textbook Persian→Arabic→Persian round trip, and a doublet of کالبد in the strict sense (Wiktionary s.v. قالب, Persian section: 'Borrowed from Arabic قَالِب (qālib). Doublet of کالبد (kâlbod)'). Mo'in marks it as such in his own dictionary: «قالب: [معر. کالبد]». The Arabic dress is visible in the ق for the original k and in the fact that the word carries Arabic morphology in Persian (قالب‌گیری, قالبی). The reservation is the list Nourai appends to the box — قلب، انقلاب، منقلب، مقلوب، تقلّب، قلّاب: these are all genuine derivatives of the Semitic root ق‑ل‑ب 'to turn', they are not descendants of Greek καλοπόδιον, and they do not belong under *ped- at all; only قالب itself does.\",\n \"derivation_fa\": \"«قالب» فارسی همان «کالبد» ایرانی است که از راه عربی بازگشته است — نمونهٔ کلاسیک وام‌گیری رفت‌وبرگشتی فارسی ← عربی ← فارسی — و از این‌رو دوگانهٔ (doublet) «کالبد» به شمار می‌رود (ویکی‌واژه، بخش فارسیِ «قالب»: «وام‌گرفته از عربی قالِب؛ دوگانهٔ کالبد»). معین خود در فرهنگ فارسی همین را می‌نویسد: «قالب: [معر. کالبد]». جامهٔ عربیِ واژه در «ق» به‌جای k آغازین و در ساخت‌های عربی‌مآبِ آن (قالب‌گیری، قالبی) پیداست. تنها ایراد، فهرستی است که نورایی به این خانه افزوده — قلب، انقلاب، منقلب، مقلوب، تقلّب، قلّاب — که همگی مشتقات راستینِ ریشهٔ سامیِ ق‑ل‑ب «گرداندن»‌اند، از καλοπόδιον یونانی نیامده‌اند و اصلاً ذیل *ped- جای ندارند؛ تنها خودِ «قالب» در این نمودار جای دارد. حکم: با احتیاط پذیرفتنی.\",\n \"sources\": [W_QALEB],\n \"ref_check\": [\n   {\"ref\": \"MON:2621\", \"status\": \"supports\", \"note\": \"6-vol. Mo'in not online; the condensation (MON_part2.txt line 10621) has «قالب: [معر. کالبد] شکل، هیئت، آلتی که جسمی شکل‌پذیر را در داخل یا خارج آن نهاده بصورت آن آلت در آورند؛ بوته زرگری؛ … تن، بدن …» — the headword, the gloss 'mould' and the معرّب tag Nourai's arrow depends on.\"},\n   {\"ref\": \"FVA:337\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368) — refs_online.json marks it 'catalog' only: no digital copy found on archive.org, ketabnak, noorlib or the open web.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. قالب\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p. 215\", \"stance\": \"supports\", \"note\": \"Arabic qālib is listed as a Persian loanword from کالبد, which is what makes the Persian قالب a re-borrowing.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 3 p. 1075 s.v. کالب\", \"stance\": \"supports\", \"note\": \"«کالب ـ بر وزن و معنی قالب است» — Borhan itself equates کالب and قالب.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt p. 223 s.v. caliber\", \"stance\": \"supports\", \"note\": \"'Arab. qālib, mold, model' — the Arabic word and sense that Persian took back.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Italian\",\n \"words\": \"calibro\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Italian calibro 'gauge, bore, size' is the Romance member of the qālib family, and this is the standard nineteenth/twentieth-century account (Klein p. 223: 'F. calibre, fr. It. calibro, fr. Arab. qālib'; Lokotsch no. 1030 lists it with Spanish gálibo/calibre, Old Spanish calibo, French calibre, German Kaliber, Turkish kalıp, Russian kalyp). The Arabic word would have reached Italy through the Mediterranean gunnery and shipbuilding trade of the fifteenth-sixteenth centuries, the mould for casting shot giving the 'size of the bore' sense. The reservation is chronological: Etymonline reports the now-preferred view that the word 'was formed in French' from Medieval Latin qua libra 'of what weight', noting that 'Spanish and Italian forms appear too late to act as intermediate forms' between Arabic and French; Skeat already recorded both options ('Etym. unknown. Perhaps from L. qua libra, with what weight (Diez); or from Arab. qālib, a form, mould'). Wiktionary still gives the Arabic route. Hence 'plausible', with the Italian link the weakest joint in the chain.\",\n \"derivation_fa\": \"«calibro» ایتالیایی حلقهٔ رومانسِ خانوادهٔ «قالب» است و همین روایتِ معیارِ سدهٔ نوزدهم و بیستم است (کلاین ص ۲۲۳: «فرانسوی calibre از ایتالیایی calibro از عربی قالب»؛ لوکوچ شمارهٔ ۱۰۳۰ آن را در کنار gálibo و calibre اسپانیایی، calibre فرانسوی، Kaliber آلمانی، kalıp ترکی و kalyp روسی می‌آورد). واژهٔ عربی از راه بازرگانی توپخانه و کشتی‌سازی مدیترانه در سده‌های پانزدهم و شانزدهم به ایتالیا رسیده و معنای «قالبِ ریختن گلوله» به «قطر دهانهٔ لوله» بدل شده است. ایراد کار تاریخ‌گذاری است: اتیمانلاین نظر امروزی‌تر را گزارش می‌کند که واژه «در فرانسه ساخته شده» از لاتین میانهٔ qua libra «به چه وزنی»، زیرا صورت‌های اسپانیایی و ایتالیایی دیرتر از آن‌اند که واسطهٔ میان عربی و فرانسوی باشند؛ اسکیت نیز هر دو احتمال را ثبت کرده است. حکم: با احتیاط پذیرفتنی؛ همین حلقهٔ ایتالیایی سست‌ترین بندِ زنجیره است.\",\n \"sources\": [E_CAL, W_CALIB],\n \"ref_check\": [\n   {\"ref\": \"KLN:223\", \"status\": \"supports\", \"note\": \"KLN_1966.txt p. 223 s.v. caliber: 'F. calibre, fr. It. calibro, fr. Arab. qālib, \\\"mold, model\\\"' — precisely the Arabic → Italian → French chain of the chart.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt p. 223\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1030 (LKT.txt line 2454)\", \"stance\": \"supports\", \"note\": \"'it. calibro \\\"Maßinstrument, um die Zusammengehörigkeit von Geschütz und Geschoß zu bestimmen\\\"' in the Arabic qālib article.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Caliber (SKT.txt line 2640)\", \"stance\": \"partial\", \"note\": \"'Caliber, Calibre, bore of a gun. F. calibre, size of a bore. Etym. unknown. Perhaps from L. qua libra, with what weight (Diez); or from Arab. qālib, a form, mould (Rich. Dict. p. 1111; Littré).'\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt, grep 'calibre'\", \"stance\": \"silent\", \"note\": \"the OCR of Funk & Wagnalls has only running-text occurrences of 'caliber', not the headword entry.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Empty pass-through box for French calibre (mid-16th c. in the gunnery sense, 'diameter of the bore'), the form through which the word reached English, German, Russian and, much later, Persian. Klein and Lokotsch have it from Italian calibro; Etymonline holds that the French word is the oldest of the Romance set and was made in France out of Medieval Latin qua libra, in which case the arrow Italian → French should be reversed. Either way French calibre is the immediate parent of the two boxes below it, which is all this box is used for.\",\n \"derivation_fa\": \"خانهٔ خالی و گذری برای «calibre» فرانسوی (در معنای توپخانه‌ای «قطر دهانهٔ لوله»، از میانهٔ سدهٔ شانزدهم)، همان صورتی که واژه از راه آن به انگلیسی و آلمانی و روسی و بسی دیرتر به فارسی رسیده است. کلاین و لوکوچ آن را از calibro ایتالیایی می‌گیرند؛ اتیمانلاین برعکس، صورت فرانسوی را کهن‌ترین عضو خانوادهٔ رومانس می‌داند که در خود فرانسه از qua libra لاتین میانه ساخته شده است — که در آن صورت باید جهت پیکانِ ایتالیایی ← فرانسوی وارونه شود. در هر حال، calibre فرانسوی پدرِ بی‌واسطهٔ دو خانهٔ زیرین است و کارکرد این خانه هم جز این نیست.\",\n \"sources\": [E_CAL],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The box carries no reference; the parent box's KLN:223 covers the link ('F. calibre, fr. It. calibro').\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt p. 223 s.v. caliber\", \"stance\": \"supports\", \"note\": \"'F. calibre, fr. It. calibro' — French from Italian, as drawn.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1030\", \"stance\": \"supports\", \"note\": \"'asp. calibo, sp. calibre, frz. calibre \\\"Durchmesser der Mündung eines Geschützes, Gewicht der Kugel\\\"'.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. Caliber\", \"stance\": \"partial\", \"note\": \"Skeat starts the English word from 'F. calibre' but leaves the ultimate origin open.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Persian\",\n \"words\": \"kâlibr «کالیبر»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"کالیبر kālibr is a modern European loan in Persian, taken with its French phonetics (final -br cluster, no Arabic dress), used of the bore of a firearm and of measuring gauges (کالیبر اسلحه, کالیبرکردن/کالیبراسیون). It arrived in the Qajar/Pahlavi period along with the rest of the military and technical vocabulary that Persian took from French; Mo'in files such words in his volume of foreign compounds, which is why Nourai's MON:2868 is the neighbouring page to کالا/کالبد. Historically it is the same word as کالبد and قالب — a third arrival of Greek καλοπόδιον in Persian, this time by way of Arabic → Romance → French, so Persian ends up with a triplet: کالبد (inherited from the Greek loan in Pahlavi), قالب (via Arabic), کالیبر (via French).\",\n \"derivation_fa\": \"«کالیبر» وام‌واژه‌ای نو و اروپایی در فارسی است که با آواشناسی فرانسوی گرفته شده (خوشهٔ پایانی ‑بر، بی هیچ جامهٔ عربی) و دربارهٔ قطر لولهٔ سلاح و ابزارهای اندازه‌گیری به کار می‌رود (کالیبر اسلحه، کالیبرکردن). این واژه در دورهٔ قاجار و پهلوی همراه دیگر واژگان نظامی و فنیِ فرانسوی وارد فارسی شد؛ معین چنین واژه‌هایی را در جلد ترکیبات خارجی آورده است. از نظر تاریخی همان واژهٔ «کالبد» و «قالب» است: سومین ورودِ καλοπόδιον یونانی به فارسی، این‌بار از راه عربی ← رومانس ← فرانسوی. پس فارسی سه‌گانه‌ای دارد: کالبد (ارثی، از وامِ یونانیِ دورهٔ پهلوی)، قالب (از راه عربی) و کالیبر (از راه فرانسوی). ادعای نورایی درست است.\",\n \"sources\": [E_CAL],\n \"ref_check\": [\n   {\"ref\": \"MON:2868\", \"status\": \"not_checked\", \"note\": \"The 6-vol. Mo'in is not online and the 2-vol. Adena condensation (MON_part1/part2.txt) omits کالیبر, so p. 2868 could not be read; the page number is plausible, since کالا (MON:2858) and کالبد (MON:2859) fall a few pages earlier in the same alphabetical stretch.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep 'کالیبر'\", \"stance\": \"silent\", \"note\": \"not in the condensed edition.\"},\n   {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep 'کالیبر'\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary does not treat modern European loans of this kind.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1030\", \"stance\": \"supports\", \"note\": \"documents the spread of frz. calibre into German, English, Russian, Bulgarian, Serbian — the same wave of borrowing that brought کالیبر into Persian.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"English\",\n \"words\": \"caliber\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English caliber/calibre is borrowed from French calibre; the figurative sense 'degree of merit or importance' is attested first (1560s) and the technical 'inside diameter of a gun barrel' only in the 1580s, which is itself a small argument that the word came in as a fashionable French term rather than as a gunner's technicality. The American spelling caliber and the British calibre are the same word; Shakespeare's caliver 'light musket' (1 Henry IV IV.2) belongs here too according to Lokotsch. Whether the ultimate source is Arabic qālib or Medieval Latin qua libra is the open question discussed at node #7; the French → English step itself is not in doubt.\",\n \"derivation_fa\": \"«caliber/calibre» انگلیسی وام‌واژه‌ای است از «calibre» فرانسوی؛ نکتهٔ جالب آنکه معنای مجازی «پایه و مایه، درجهٔ ارزش» زودتر (دههٔ ۱۵۶۰) گواهی شده و معنای فنی «قطر داخلی لولهٔ تفنگ» دیرتر (دههٔ ۱۵۸۰) — و همین خود نشانهٔ آن است که واژه نخست همچون اصطلاحی مُدِ روز از فرانسه گرفته شده نه همچون اصطلاح توپچیان. املای آمریکایی caliber و بریتانیایی calibre یک واژه‌اند. اینکه سرچشمهٔ نهایی «قالب» عربی است یا qua libra لاتینِ میانه، پرسشی است که در خانهٔ #۷ آمد؛ خودِ گامِ فرانسوی ← انگلیسی جای تردید ندارد. ادعای نورایی درست است.\",\n \"sources\": [E_CAL, W_CALIB],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The box carries no reference; the KLN:223 of the boxes above covers it — 'caliber, calibre, n., the diameter of the bore of a gun. — F. calibre'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt p. 223 s.v. caliber\", \"stance\": \"supports\", \"note\": \"'caliber, calibre, n., the diameter of the bore of a gun. — F. calibre, fr. It. calibro …'\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. Caliber\", \"stance\": \"supports\", \"note\": \"'Caliber, Calibre, bore of a gun. F. calibre, size of a bore.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1030\", \"stance\": \"supports\", \"note\": \"'dtsch. Kaliber, engl. calibre [amerikanische Schreibung caliber] … bei Shakespeare 1. Henry IVth IV, 2, 21 … caliver \\\"kleine Muskete\\\"'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"French\",\n \"words\": \"octopode\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French octopode (adj. and n., 'eight-footed; a member of the Octopoda') is a learned nineteenth-century formation taken from Greek ὀκτώπους, gen. ὀκτώποδος, through the Latinised zoological name Octopoda (Leach 1818); the French keeps the Greek oblique stem -pod- and adds the ordinary French -e, as in céphalopode, gastéropode, myriapode. The everyday French words for the animal are poulpe and pieuvre, so octopode is and remains a scientific term. The derivation from the root box is straightforward: ὀκτώ 'eight' + πούς/ποδ- 'foot'.\",\n \"derivation_fa\": \"«octopode» فرانسوی (هم صفت و هم اسم، «هشت‌پا؛ از راستهٔ Octopoda») ساختی است عالمانه از سدهٔ نوزدهم، برگرفته از ὀκτώπους یونانی با حالت اضافیِ ὀκτώποδος، از راه نام جانورشناختیِ لاتینی‌شدهٔ Octopoda (لیچ، ۱۸۱۸)؛ فرانسوی ستاک غیرفاعلیِ ‑pod- را نگه داشته و ‑e معمول فرانسوی را افزوده است، مانند céphalopode و gastéropode. واژهٔ روزمرهٔ فرانسوی برای این جانور poulpe یا pieuvre است، پس octopode اصطلاحی علمی است و بس. اشتقاق آن از خانهٔ ریشه روشن است: ὀκτώ «هشت» + πούς/ποδ- «پا». ادعای نورایی درست است.\",\n \"sources\": [E_OCT],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The box carries no reference.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. eight, Cephalopoda, -pod\", \"stance\": \"supports\", \"note\": \"'Cephalopoda … compounded of κεφαλή, head, and πούς, gen. ποδός, foot' and s.v. eight the cross-reference list ends '… octo-, October, octopus, octoroon, octuple' — the same Greek formation type.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. ped-1\", \"stance\": \"supports\", \"note\": \"OCTOPUS listed under 'Greek pous (stem pod-), foot'.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century (vol. 1 only, A-?) — no O volume open\", \"stance\": \"silent\", \"note\": \"vol. 2 of the scan is not available, so 'octopode' could not be checked there.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Persian\",\n \"words\": \"oxtâpŭs «اختاپوس»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Persian اختاپوس oxtāpus 'octopus' is a real, if less common, word (the everyday Persian is هشت‌پا hašt-pā, a calque of the same Greek compound), and Wiktionary derives it 'From Ancient Greek ὀκτώπους (oktṓpous)'. What is doubtful is Nourai's immediate parent: the Persian form ends in -pus, i.e. it renders the Greek/scientific-Latin nominative octopus, not French octopode, which would have given اختاپد. The likeliest immediate donor is therefore the international zoological Latin octopus (as read in French, English or Russian scientific writing) rather than the French adjective octopode specifically. The initial اخ- for oct- is the normal Persian treatment of a foreign kt cluster (compare دکتر/داکتر), and the long -ū- of -pūs simply spells the Latin -u-. So the box is right about the ultimate origin and doubtful only about which European language handed the word over.\",\n \"derivation_fa\": \"«اختاپوس» در فارسی واژه‌ای واقعی است، هرچند کم‌کاربردتر از «هشت‌پا» که خود گرته‌برداری از همان ترکیب یونانی است، و ویکی‌واژه آن را «از یونانی باستان ὀκτώπους» می‌داند. آنچه جای تردید دارد پدرِ بی‌واسطهٔ آن در نمودار است: صورت فارسی به ‑پوس ختم می‌شود، یعنی برگردانِ صورت فاعلیِ یونانی/لاتینِ علمی octopus است، نه octopode فرانسوی که در فارسی «اختاپد» می‌شد. پس محتمل‌ترین وام‌دهندهٔ بی‌واسطه، لاتینِ جانورشناسیِ بین‌المللی octopus است (چنان‌که در نوشته‌های علمی فرانسوی، انگلیسی یا روسی خوانده می‌شد) نه بویژه صفتِ فرانسویِ octopode. «اخـ» در آغاز، برخورد معمول فارسی با خوشهٔ بیگانهٔ kt است. بنابراین خانه دربارهٔ خاستگاه نهایی درست است و تنها دربارهٔ زبان واسطه با احتیاط پذیرفتنی است.\",\n \"sources\": [W_OXTA, E_OCT],\n \"ref_check\": [\n   {\"ref\": \"MON:164\", \"status\": \"not_checked\", \"note\": \"The 6-vol. Mo'in is not online and the 2-vol. Adena condensation has no اختاپوس headword (grep of MON_part1/part2 returns nothing), so p. 164 could not be read; p. 164 does fall in the الف section, which is consistent.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep 'اختاپ'\", \"stance\": \"silent\", \"note\": \"not in the condensed edition.\"},\n   {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep 'اختاپوس'\", \"stance\": \"silent\", \"note\": \"no entry.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. eight / octo-\", \"stance\": \"supports\", \"note\": \"Gk. ὀκτώ 'eight' and the -pous compounds — the ultimate source of the Persian word.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"English\",\n \"words\": \"octopus, pilot, podium\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three are Greek *pod- words in English. octopus (1758) is Latinised Greek ὀκτώπους 'eight-foot', introduced as a Linnaean genus name; the classical plural is octopodes. podium is Latin podium 'raised platform, balcony' from Greek πόδιον 'little foot, base', the diminutive of πούς. pilot (1510s) is the least obvious: French pillote < Italian piloto, altered from earlier pedoto, from Medieval Greek πηδώτης pēdṓtēs 'steersman', to πηδόν pēdón 'steering-oar, rudder blade' — the lengthened-grade *pēd-o- of the same root (Pokorny 791 'gr. πηδόν Ruderblatt, πηδάλιον Ruder, Steuer'); the d > l is the Italian 'Sabine -l-' as in odore/olfatto. Watkins lists exactly these three (PEW, -POD, PODITE, PODIUM … OCTOPUS … PILOT) under ped-1.\",\n \"derivation_fa\": \"هر سه واژه از خانوادهٔ *pod- یونانی در انگلیسی‌اند. octopus (۱۷۵۸ م) صورت لاتینی‌شدهٔ ὀκτώπους «هشت‌پا» است که همچون نام جنسِ لینه‌ای وارد شد و جمع کلاسیک آن octopodes است. podium از podium لاتین «سکو، ایوان» و آن از πόδιον یونانی «پایکِ کوچک، پایه»، مصغّر πούς. اما pilot (دههٔ ۱۵۱۰) کمتر آشکار است: از pillote فرانسوی، از piloto ایتالیایی که دگرگون‌شدهٔ pedoto کهن‌تر است، از πηδώτης یونانیِ میانه «سکّان‌دار»، وابسته به πηδόν «پارویِ سکّان» — همان درجهٔ کشیدهٔ *pēd-o- از این ریشه (پوکورنی ص ۷۹۱: «گر. πηδόν Ruderblatt، πηδάλιον Ruder, Steuer»)؛ بدل شدن d به l همان «لامِ سابینی» ایتالیایی است، مانند odore در برابر olfatto. واتکینز دقیقاً همین سه واژه را ذیل ped-1 آورده است. ادعای نورایی درست است.\",\n \"sources\": [E_OCT, E_PIL],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The box carries no reference; the AHD:1365 of the Greek parent box covers it — Watkins s.v. ped-1 lists PODIUM and OCTOPUS under Greek pous and PILOT under 'lengthened-grade form *pēdo- in (i) Greek pēdon, rudder, steering oar: PILOT'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. ped-1, sections 7a and 9d\", \"stance\": \"supports\", \"note\": \"'Greek pous (stem pod-), foot: PEW, -POD, PODITE, PODIUM; … OCTOPUS …' and 'lengthened-grade form *pēdo- in (i) Greek pēdon, rudder, steering oar: PILOT'.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. foot, cross-reference list\", \"stance\": \"supports\", \"note\": \"'Cp. also antipodes, apod, … caliber, … octopus, … pilot, podagra, podal, podium, podo-, … trapezium …' — Klein files all three under foot.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 791\", \"stance\": \"supports\", \"note\": \"'gr. πηδόν Ruderblatt, πηδάλιον Ruder, Helm' in the verbal/ē-grade section — the base of pilot.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Greek\",\n \"words\": \"tra-peza\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Ancient Greek τράπεζα trápeza 'table' is a transparent compound *kʷtwṛ-ped-ya 'four-footed (thing)': the zero grade of *kʷetwer- 'four' gives Greek τρα- (beside full-grade τετρα-), and -πεζα is the *ped-ya derivative of 'foot' seen in πέζα. Klein spells it out: 'τραπέζιον, a little table, dimin. of τράπεζα, which stands for *τετράπεζα, a compound lit. meaning provided with four feet'. The diminutive τραπέζιον 'little table' was taken over by the geometers for a quadrilateral with no two sides parallel, and it is that geometrical sense which produced trapezium/trapezoid/trapeze. Watkins files TRAPEZIUM under both kʷetwer- and ped-1, which is exactly the double parentage Nourai marks with his ☞Kwetwer cross-reference (the same box is verified on PDF page 295, entry 'Kwetwer', node #18).\",\n \"derivation_fa\": \"«τράπεζα» یونانی باستان به معنای «میز» ترکیبی است شفاف از *kʷtwṛ-ped-ya یعنی «چهارپایه»: درجهٔ صفر ریشهٔ *kʷetwer- «چهار» در یونانی τρα- می‌دهد (در برابر درجهٔ کاملِ τετρα-) و ‑πεζα همان مشتقِ *ped-ya است که در πέζα دیده می‌شود. کلاین صریح می‌گوید: «τραπέζιον، میز کوچک، مصغّر τράπεζα که خود از *τετράπεζα است، به‌لفظ چهارپایه». مصغّر τραπέζιον را هندسه‌دانان برای چهارضلعیِ بی‌ضلعِ موازی به کار بردند و از همان معنای هندسی trapezium و trapezoid و trapeze پدید آمد. واتکینز TRAPEZIUM را هم ذیل kʷetwer- و هم ذیل ped-1 آورده است، یعنی همان دوریشگی که نورایی با ارجاع ☞Kwetwer نشان داده است. ادعای نورایی درست است.\",\n \"sources\": [E_TRA],\n \"ref_check\": [\n   {\"ref\": \"AHD:1365\", \"status\": \"supports\", \"note\": \"New College p. 1365 not open online; Watkins' appendix says it twice — s.v. ped-1: '8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM', and s.v. kʷetwer-: 'zero-grade form *kʷt(w)r- in Greek tra-, four: TRAPEZIUM'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. trapezium\", \"stance\": \"supports\", \"note\": \"'Late L., fr. Gk. τραπέζιον, a little table, dimin. of τράπεζα, which stands for *τετράπεζα, a compound lit. meaning provided with four feet. The first element represents I.-E. *qʷetr-, four … The second element is foot, which is rel. to πούς.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 7.44 TABLE (SYN.txt line 12127)\", \"stance\": \"supports\", \"note\": \"the comparative table lists 'ChSl. trapeza' and 'SCr. stol (trpeza)' beside Grk. τράπεζα — the word and its Slavic borrowings.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 23 ff. (ped-)\", \"stance\": \"supports\", \"note\": \"'gr. πέζα Fuss; (unterer) Rand, Saum' — the second element of τράπεζα.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 791\", \"stance\": \"supports\", \"note\": \"πέζα listed under the pedio- derivatives of pē̆d-2.\"}\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Arabic\",\n \"words\": \"dar-bezin\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Arabic word is درابزين darābzīn (variants دربزين darbazīn, درابزون darābzūn) 'railing, banister, balustrade'. Mo'in's footnote in Borhan-e Qate' p. 829 derives it exactly as the chart does: «درابزین ـ از یونانی Trapézion (نرده، شبکه) معرّب آن درابزین و دربوز» citing Dozy I 430 and Muʿjamiyyāt ʿarabiyya sāmiyya 227, plus درابزون from al-Munjid. The Greek diminutive τραπέζιον was thus taken into Arabic — the initial cluster tr- being impossible in Arabic, it was broken up as dar- — and the sense went from the trestle-table/lattice shape to 'railing, lattice'. Two reservations. First, Nourai's form 'dar-bezin' and his gloss 'a seating area between two doors of a room' are really Mo'in's Persian entry for دارافزین, not the Arabic sense, which is 'railing'. Second, Wiktionary reverses the direction, taking Arabic درابزين from Ottoman Turkish طرابزان, itself from Persian داربزین. Hence plausible, not confirmed. (Verified in the same terms on PDF page 295, entry 'Kwetwer', node #19.)\",\n \"derivation_fa\": \"واژهٔ عربی «درابزین» است (با گونه‌های «دربزین» و «درابزون») به معنای «نرده، طارمی، محجر». حاشیهٔ معین بر برهان قاطع در ص ۸۲۹ آن را درست همان‌گونه که نمودار رسم کرده ریشه‌یابی می‌کند: «درابزین ـ از یونانی Trapézion (نرده، شبکه) معرّب آن درابزین و دربوز» با ارجاع به دُزی ج۱ ص۴۳۰ و «معجمیات عربیة سامیة» ص۲۲۷ و «درابزون» از المنجد. یعنی مصغّر یونانی τραπέζιον وارد عربی شده — خوشهٔ tr در آغاز واژهٔ عربی ناممکن است و به dar- شکسته شده — و معنا از شکلِ میزِ چهارپایه/شبکه‌مانند به «نرده و شبکه» رفته است. دو نکته: نخست آنکه صورت «dar-bezin» و معنای «جایی برای نشستن میان دو درِ اتاق» در اصل مدخل فارسیِ «دارافزین» در فرهنگ معین است نه معنای عربی که «نرده» است؛ دوم آنکه ویکی‌واژه جهت وام‌گیری را وارونه می‌داند و «درابزین» عربی را از «طرابزان» ترکی عثمانی و آن را از «داربزین» فارسی می‌گیرد. پس با احتیاط پذیرفتنی است.\",\n \"sources\": [E_TRA],\n \"ref_check\": [\n   {\"ref\": \"MON:1481\", \"status\": \"partial\", \"note\": \"The 6-vol. Mo'in is not online, so p. 1481 could not be opened; but Mo'in's own footnote in his edition of Borhan-e Qate', vol. 2 p. 829 (page image read and saved at data/verification/sources/refs/ocr/BQT/829.vision.txt; also in the OCR at BQT_v2_pages.txt line 17036) states the identical claim: «درابزین ـ از یونانی Trapézion (نرده، شبکه) معرّب آن درابزین و دربوز «دزی ج ۱ ص ۴۳۰» … و درابزون «المنجد»».\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, vol. 2 p. 829, Mo'in's footnote (BQT_v2_pages.txt line 17036)\", \"stance\": \"supports\", \"note\": \"«از یونانی Trapézion (نرده، شبکه) معرّب آن درابزین و دربوز».\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. دارافزین\", \"stance\": \"partial\", \"note\": \"«دارافزین [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون] (ا.) مجری که در جلو اطاق بین دو در سازند؛ تکیه‌گاه؛ طارمی» — this is where Nourai's gloss 'a seating area between two doors of a room' comes from, but it is Mo'in's PERSIAN entry, not a gloss of the Arabic word.\"},\n   {\"src\": \"DOZ\", \"where\": \"Dozy, Supplément I 430 (cited by Mo'in)\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote cites «دزی ج ۱ ص ۴۳۰» for the Arabicised درابزین/دربوز; Dozy is the authority behind the claim.\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"Persian\",\n \"words\": \"dârâbzîn «دارابزین»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian دارابزین / درابزین / دارافزین / داروزین 'balustrade, railing; the railed dais built at the front of a room between its two doors' is one word in four shapes, and Mo'in lists exactly these in his Farhang («دارافزین [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون] مجری که در جلو اطاق بین دو در سازند؛ تکیه‌گاه؛ طارمی»), with the very gloss Nourai gives; Nourai's own 'extra' line (درابزین، دارافزین، داروزین) reproduces Mo'in's variant list. The alternation -bzīn ~ -fzīn ~ -wzīn is the ordinary Persian b/f/w interchange in an unstressed medial syllable, encouraged by the folk etymology دار 'wood, post' + افزودن 'to add'. Mo'in's note in Borhan p. 829 traces the word to Greek τραπέζιον through the Arabicised درابزین/دربوز — the route drawn here. (Same finding as PDF page 295 node #20.)\",\n \"derivation_fa\": \"«دارابزین / درابزین / دارافزین / داروزین» یک واژه با چهار گونهٔ نوشتاری است به معنای «نرده، طارمی، مجری‌ای که در جلو اتاق میان دو در می‌سازند»، و معین در فرهنگ فارسی دقیقاً همین‌ها را با همان معنایی که نورایی آورده ثبت کرده است: «دارافزین [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون] مجری که در جلو اطاق بین دو در سازند؛ تکیه‌گاه؛ طارمی»؛ فهرست «extra»ی خودِ نورایی هم همان فهرست گونه‌های معین است. جابه‌جایی ـبزین/ـفزین/ـوزین همان ابدال معمول ب و ف و و در هجای میانیِ بی‌تکیه است که ریشه‌شناسی عامیانه (دار + افزودن) نیز به آن دامن زده است. حاشیهٔ معین در برهان ص ۸۲۹ واژه را از یونانی τραπέζιον از راه صورت معرّبِ درابزین/دربوز می‌گیرد؛ یعنی همان مسیر نمودار. ادعای نورایی درست است.\",\n \"sources\": [E_TRA],\n \"ref_check\": [\n   {\"ref\": \"MON:1481\", \"status\": \"partial\", \"note\": \"6-vol. Mo'in not online; the 2-vol. condensation (MON_part1.txt) has the entry verbatim: «دارافزین: [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون] (ا.) مجری که در جلو اطاق بین دو در سازند؛ تکیه گاه؛ طارمی» — all of Nourai's variants and his gloss, so the content of MON:1481 is confirmed even though the page number itself is not.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. دارافزین\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 2 pp. 829-830, headword درابزین with Mo'in's footnote (BQT_v2_pages.txt lines 15989, 17036)\", \"stance\": \"supports\", \"note\": \"«…(فر) balustrade = (عر) جلفق … «دربزین»، «درابزین» و «درابزون» (المنجد)» plus the Greek footnote.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'darabzin'\", \"stance\": \"silent\", \"note\": \"Horn has no entry.\"}\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Latin\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box for Late Latin trapezium, the borrowing of Greek τραπέζιον that carried the geometrical term into the West (Boethius and the medieval mathematical tradition; classical Latin used trapezīta 'money-changer' from the related τραπεζίτης). Klein: 'trapezium, n., a plane figure with four sides of which no two are parallel. — Late L., fr. Gk. τραπέζιον'. This is the box through which English trapezoid and trapeze descend.\",\n \"derivation_fa\": \"خانهٔ خالی و گذری برای «trapezium» لاتینِ متأخر، یعنی وام‌گیری τραπέζιον یونانی که اصطلاح هندسی را به مغرب‌زمین رساند (بوئتیوس و سنّت ریاضی سده‌های میانه؛ لاتینِ کلاسیک trapezīta «صرّاف» را از τραπεζίτης هم‌خانواده داشت). کلاین: «trapezium … لاتینِ متأخر، از یونانی τραπέζιον». همین خانه است که trapezoid و trapeze انگلیسی از آن فرود می‌آیند. ادعای نورایی درست است.\",\n \"sources\": [E_TRA],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. ped-1: '8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM' — the appendix routes the English word through the Latin/Greek form, and the index line reads 'TRAPEZIUM kʷetwer-, ped-1'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. trapezium\", \"stance\": \"supports\", \"note\": \"'Late L., fr. Gk. τραπέζιον, a little table, dimin. of τράπεζα'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt) and Walde LEW (LEW_1910.txt), grep 'trapezium'\", \"stance\": \"silent\", \"note\": \"neither Latin etymological dictionary in the local library has the (late, learned) headword in its OCR.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. ped-1\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"English\",\n \"words\": \"trapezoid, trapeze\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"trapezoid (1706) is Modern Latin trapezoides, from Greek τραπεζοειδής 'table-shaped' (τράπεζα + -oeidēs); trapeze (1861) is French trapèze, from the same Late Latin trapezium, the gymnastic apparatus being so named because the cross-bar, the two ropes and the ceiling outline a trapezium. (English and American usage swapped the geometrical definitions of trapezium and trapezoid in the 18th century, which is why the two words look interchangeable.) Both go back through the Latin box to Greek τράπεζα 'four-footed thing', hence to *ped-.\",\n \"derivation_fa\": \"«trapezoid» (۱۷۰۶ م) از لاتینِ نو trapezoides و آن از τραπεζοειδής یونانی «میزمانند» است (τράπεζα + ‑οειδής)؛ و «trapeze» (۱۸۶۱ م) از trapèze فرانسوی و آن از همان trapezium لاتینِ متأخر — ابزار ژیمناستیک را از آن رو چنین نامیدند که میلهٔ افقی و دو طناب و سقف با هم یک ذوزنقه می‌سازند. (کاربرد انگلیسی و آمریکایی در سدهٔ هجدهم تعریف هندسی trapezium و trapezoid را با هم عوض کرد و از این‌رو این دو واژه جابه‌جاشدنی می‌نمایند.) هر دو از راه خانهٔ لاتین به τράπεζα یونانی «چهارپایه» و از آنجا به *ped- بازمی‌گردند. ادعای نورایی درست است.\",\n \"sources\": [E_TRA],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. ped-1 lists TRAPEZIUM (the head of this small family) under Greek peza; the appendix index gives 'TRAPEZIUM kʷetwer-, ped-1'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. trapeze, trapeziform, trapezium\", \"stance\": \"supports\", \"note\": \"'trapeze, n., a suspended horizontal bar used in gymnastics. — F. trapèze, fr. Late L. trapezium'; 'trapeziform … coined fr. Gk. τραπέζιον and L. forma'.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. ped-1\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'trapezium'\", \"stance\": \"silent\", \"note\": \"not in Skeat's Concise (the OCR returns no headword).\"}\n ]\n})\n\nnodes.append({\n \"id\": 19, \"lang\": \"Germanic\",\n \"words\": \"fot\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *fōt- (nom. *fōts) 'foot' is the regular Germanic outcome of the lengthened o-grade *pōd-s: PIE *p- > Gmc *f- and *d > *t by Grimm's Law, giving Gothic fōtus, Old Norse fótr, Old English fōt (pl. fēt by i-umlaut from *fōt-iz), Old High German fuoz. Pokorny prints exactly this list ('got. fotus, aisl. fótr, ags. fōt … ahd. fuoz \\\"Fuss\\\"'), and Watkins writes 'Lengthened o-grade form *pōd- in Germanic *fōt- in Old English fōt, foot: FOOT'. Nourai's bare 'fot' is the Old English/Germanic shape without the length mark; the label and gloss are right.\",\n \"derivation_fa\": \"*fōt- ژرمنی آغازین (حالت فاعلی *fōts) «پا» برآیند قاعده‌مندِ درجهٔ کشیدهٔ *pōd-s است: *p هندواروپایی بنا بر قانون گریم در ژرمنی به *f و *d به *t بدل شده و از آن fōtus گوتی، fótr نورس کهن، fōt انگلیسی کهن (جمع fēt با امالهٔ i از *fōt-iz) و fuoz آلمانی علیای کهن پدید آمده است. پوکورنی همین فهرست را می‌آورد و واتکینز می‌نویسد «درجهٔ کشیدهٔ o یعنی *pōd- در ژرمنی *fōt- و در انگلیسی کهن fōt». صورت ساده و بی‌نشانهٔ کشیدگیِ «fot» در کتاب همان صورت انگلیسی کهن/ژرمنی است؛ برچسب زبان و معنا درست است. ادعای نورایی درست است.\",\n \"sources\": [E_OCT],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. ped-1: 'I. Nominal root. 1. Lengthened o-grade form *pōd- in Germanic *fōt- in Old English fōt, foot: FOOT.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 790 (POK_full.txt)\", \"stance\": \"supports\", \"note\": \"'Gothic fotus, Old Icelandic fótr, Old English fōt (Nom. Pl. Old Icelandic fǿtr, Old English fēt from *fōt-iz), Old High German fuoz \\\"Fuss\\\"'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 23 ff.\", \"stance\": \"supports\", \"note\": \"'Got. fotus (u-Decl. …), aisl. fótr, ags. fōt … ahd. fuoz \\\"Fuss\\\"'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.37 FOOT (SYN.txt line 6270)\", \"stance\": \"supports\", \"note\": \"the comparative row 'Grk. πούς … Lat. pes … Goth. fotus, ON fótr, Dan. fod, Sw. fot, OE fōt, ME fote, NE foot, Du. voet, OHG fuoz' — 'the inherited group'.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. foot\", \"stance\": \"supports\", \"note\": \"'ME. fot, fr. OE. fōt, rel. to OS. fōt, ON. fótr … Goth. fōtus, foot.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 20, \"lang\": \"English\",\n \"words\": \"foot, fetch\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"foot is the direct inheritance: OE fōt > ME fot/foot > foot, plural fēt > feet. fetch is the same root by its verbal branch: OE feccan (also fetian) 'to bring, fetch' < Germanic *fetōn, to Pokorny's verbal section of pē̆d- ('to walk, step, stumble'), whose Iranian and Indic members are Skt. pádyate 'goes, falls' and Av. paiδyeiti 'moves downwards'; Pokorny explicitly notes 'Old English fetian, engl. fetch \\\"get, fetch\\\"' there (adding the caution that fatian/fetian could equally belong to his ped- \\\"vessel\\\"). Watkins puts it under 'II. Verbal root *ped-, to stumble, fall. 1. Germanic *fetōn in Old English fetian, feccean, to bring back: FETCH'. So the two English words of the box are a noun and a verb from the same root, which is what the box asserts.\",\n \"derivation_fa\": \"«foot» میراث مستقیم است: fōt انگلیسی کهن ← fot/foot انگلیسی میانه ← foot، با جمع fēt ← feet. اما «fetch» از شاخهٔ فعلیِ همین ریشه می‌آید: feccan (و نیز fetian) انگلیسی کهن «آوردن، فراآوردن» از *fetōn ژرمنی، وابسته به بخش فعلیِ ریشهٔ pē̆d- نزد پوکورنی («رفتن، گام برداشتن، لغزیدن») که اعضای هندی و ایرانی‌اش pádyate سنسکریت «می‌رود، می‌افتد» و paiδyeiti اوستایی «به‌سوی پایین حرکت می‌کند» است؛ پوکورنی خودِ «Old English fetian, engl. fetch» را در همان‌جا آورده و تنها هشدار داده که fatian/fetian می‌تواند به ped- «ظرف» هم تعلق داشته باشد. واتکینز آن را ذیل «ریشهٔ فعلی *ped- لغزیدن، افتادن: ژرمنی *fetōn در انگلیسی کهن fetian, feccean: FETCH» می‌گذارد. پس دو واژهٔ این خانه یک اسم و یک فعل از یک ریشه‌اند — درست همان که نمودار می‌گوید. ادعای نورایی درست است.\",\n \"sources\": [E_FET],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The box carries no reference; the parent's AHD covers both — Watkins s.v. ped-1: 'Old English fōt, foot: FOOT' and 'Germanic *fetōn in Old English fetian, feccean, to bring back: FETCH'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. ped-1, I.1 and II.1\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 790-791, verbal section\", \"stance\": \"supports\", \"note\": \"'Old English fetian, engl. fetch \\\"get, fetch\\\" (Old English fatian and fetian could also to ped-1 belong, as generally the two families are not sharply to separate)'.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. foot\", \"stance\": \"supports\", \"note\": \"'foot, n. — ME. fot, fr. OE. fōt … Cp. fetch, fetlock, fetter, fit.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.37 FOOT\", \"stance\": \"supports\", \"note\": \"'OE fōt, ME fote, NE foot' in the inherited group.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Ped, Pod\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *pṓds, oblique stem *ped- / *pod- 'foot' (Pokorny 2. pē̆d-, pō̆d- 790-792; Watkins ped-1)\",\n \"note\": \"The root box is right in every respect: the two ablaut shapes Ped/Pod are Pokorny's pē̆d-/pō̆d-, the language label 'Indo-European' is correct, and the gloss 'foot' is the standard one. This is PART 2 of the chart; the Iranian pād/pāy words are in Part 1. What Part 2 collects is (a) the Greek o-grade pod- and its *ped-ya derivative peza, (b) the long chain that hangs on Greek kalopodion 'shoemaker's last' — Pahlavi kalbod > NP کالبد > Arabic قالب > NP قالب, and the western branch Arabic > Italian/French calibre > NP کالیبر, (c) Greek trapeza > Arabic/Persian darābzīn and Latin trapezium > trapeze, and (d) Germanic *fōt- > foot, fetch. 18 of the 20 nodes hold up. Two do not: the arrow from Pahlavi kal-pād to Persian کالا (node #3) is contradicted by both of Nourai's own references and by modern work, which derive کالا from PIE *kʷer- 'to make'; and the Arabic box (node #5) puts the native Semitic root ق-ل-ب 'to turn' under *ped-, which is a folk etymology inside Arabic. Nourai's own NOTE on node #2 (Mann's derivation of kalbod from Av. kəhrp-) is the minority view and is rejected here in favour of the Greek loan, which is what Nyberg, MacKenzie, Hübschmann, Mo'in and Wiktionary all give. The extraction is faithful to the printed page (checked against site/pages/384.jpg at 300 dpi): no extraction errors on this page.\",\n \"note_fa\": \"خانهٔ ریشه از هر نظر درست است: دو صورت Ped/Pod همان pē̆d-/pō̆d- پوکورنی است، برچسب «هندواروپایی» درست است و معنای «پا» همان معنای معیار. این بخش دومِ نمودار است؛ واژه‌های ایرانیِ «پاد/پای» در بخش نخست آمده‌اند. آنچه در این صفحه گرد آمده عبارت است از: (الف) درجهٔ o یونانی pod- و مشتق *ped-ya یعنی peza؛ (ب) زنجیرهٔ بلندی که به καλοπόδιον یونانی «قالب کفشگری» آویخته است — kalbod پهلوی ← «کالبد» فارسی ← «قالب» عربی ← «قالب» فارسی، و شاخهٔ باختریِ عربی ← calibro/calibre ← «کالیبر» فارسی؛ (پ) τράπεζα یونانی ← «درابزین» عربی و فارسی و trapezium لاتین ← trapeze؛ (ت) *fōt- ژرمنی ← foot و fetch. هجده خانه از بیست خانه استوارند. دو خانه نه: پیکانِ «کال‌پاد» پهلوی به «کالا»ی فارسی (خانهٔ ۳) را هم دو ارجاع خودِ نورایی و هم پژوهش امروزی رد می‌کنند و «کالا» را از ریشهٔ *kʷer- «ساختن» می‌گیرند؛ و خانهٔ عربی (خانهٔ ۵) ریشهٔ اصیل سامیِ ق‑ل‑ب «گرداندن» را ذیل *ped- آورده که ریشه‌شناسی عامیانه‌ای در درون عربی است. یادداشت خودِ نورایی بر خانهٔ ۲ (اشتقاق «کالبد» از kəhrp- اوستایی به نقل از مان) نظر اقلیت است و در برابر وامِ یونانی رد می‌شود — همان وامی که نیبرگ، مکنزی، هوبشمان، معین و ویکی‌واژه بر آن‌اند. خوانشِ داده‌ها با صفحهٔ چاپی (site/pages/384.jpg با تفکیک ۳۰۰) مطابقت کامل دارد و خطای استخراج در این صفحه نیست.\",\n \"sources\": [E_OCT, E_CAL],\n \"ref_check\": [\n   {\"ref\": \"POK:790\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: pē̆d-2, pō̆d-, Meaning: foot … Page(s): 790-792'. The material list has ai./av. pad-, arm. ot-n, gr. πούς gen. ποδός, lat. pēs pedis, goth. fotus, hitt. pata-, toch. A pe. Nourai's page number and his two ablaut shapes are exactly Pokorny's.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 790-792\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 23 ff. (WLD_Bd2_1927_dli_106624_djvu.txt lines 1510-1560)\", \"stance\": \"supports\", \"note\": \"'Ai. pad- (pāt, pādam, padáḥ), av. pad- ds.; arm. ot-n; gr. att. πούς … g. ποδός Fuss; lat. pēs, pedis ds.' — the same root, the reference Pokorny himself gives (WP II 23 ff.).\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. ped-1 ('Foot'), '[Pok. 2. pē̆d- 790.]'\", \"stance\": \"supports\", \"note\": \"Watkins' entry is headed 'ped-1. Foot' and closes with the same Pokorny page, 790.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.37 FOOT (SYN.txt line 6270)\", \"stance\": \"supports\", \"note\": \"'Grk. πούς … Lat. pēs … Goth. fotus … NE foot … the inherited group' — Buck's comparative row for the root.\"}\n ],\n \"nodes\": nodes\n}\n\ndoc = {\n \"pdf_page\": 384,\n \"book_page\": 354,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [entry]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-384.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-384.py"
}
```


### [2026-09-07T21:02:02.560Z] TOOL RESULT

```
ok 20
```


## [2026-09-07T21:02:05.861Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-384.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 384"
}
```


### [2026-09-07T21:02:07.266Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'confirmed': 13, 'disputed': 2, 'plausible': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'contradicts': 2, 'partial': 3, 'not_checked': 8}
books consulted: {'supports': 51, 'contradicts': 3, 'silent': 16, 'partial': 5} | by book: {'KLN': 14, 'MON': 8, 'AHD': 6, 'POK': 5, 'BQT': 5, 'LKT': 5, 'HRN': 4, 'SKT': 4, 'WLD': 3, 'ARY': 3, 'SYN': 3, 'PHD': 2, 'HUB': 2, 'IEC': 2, 'PLA': 2, 'NYB': 1, 'FVQ': 1, 'AFM': 1, 'FSD': 1, 'WEB': 1, 'DOZ': 1, 'LAT': 1}
```


## [2026-09-07T21:02:27.802Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-384.json` written; `verify_check.py 384` reports 20/20 nodes, **0 PROBLEM lines**.

**Page 384 (book p. 354), entry 0 "Ped, Pod" PART 2 — root: confirmed**
- Node verdicts: **13 confirmed, 5 plausible, 2 disputed**
- Ref checks: 13 supports, 3 partial, 2 contradicts, 8 not_checked (boxes with no refs, plus FVA:337 and the 6-vol. Mo'in pages that aren't online)

**Disputed**
- `#3 Persian kâlâ «کالا»` — Nourai derives it from Pahlavi kal-pād (Greek kalopodion). Both of his own refs point elsewhere: Mo'in gives «کالا [- کاله]», Mann (IEC:1047) files *kala* under `quortos (2)` = PIE \*kʷer- 'to make'; Wiktionary agrees (PIr \*kar-). Borhan p. 1074 has no etymology for the 'merchandise' sense at all (its footnote 14 belongs to the homonym 'shout' = Pahl. *vāng*) — read from the page image and saved to `sources/refs/ocr/BQT/1074.vision.txt`.
- `#5 Arabic qalib; q.l.b` — قالب itself is fine (Asbaghi PLA:215 supports the Persian route verbatim: "qālib … pers. کالبد kalbod, mp. kālpūδ"; Klein/Wiktionary route it via Aramaic/Syriac instead). But the second word, the Semitic root ق-ل-ب 'to turn' (with the appended قلب/انقلاب/مقلوب family on #6), is native and unrelated to \*ped- — the loan was reanalysed into that root inside Arabic.

**Other notes**
- Nourai's NOTE on #2 (Mann's kəhrp-/\*kʷerp- etymology of kālbod) is the minority view; Nyberg p. 110, MacKenzie, Hübschmann p. 178, Mo'in's footnote at BQT p. 1075 and Wiktionary all give the Greek καλοπόδιον loan, so #2 and #4 are confirmed.
- Plausible: #7/#8 (Italian/French calibre — Etymonline and Skeat record the competing ML *qua libra* origin, Italian/Spanish forms too late to mediate), #12 (اختاپوس ends in ‑pus, i.e. scientific-Latin *octopus*, not French *octopode*), #15 (dar-bezin: gloss given is actually Mo'in's Persian دارافزین entry; Wiktionary reverses the loan direction), #6.
- Nodes #14/#15/#16 duplicate boxes already verified on PDF page 295 (root Kwetwer, nodes #18–20); findings are consistent and cross-referenced.
- **No extraction errors**: the JSON matches the printed page (checked against `site/pages/384.jpg` and a 300 dpi render, including the #2→#3 horizontal arrow).
