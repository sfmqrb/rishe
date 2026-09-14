# Verification process log — verify-page-477


## [2026-09-14T02:28:18.149Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 477 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-477.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-477.json. Write /home/sfmqrb/git/rishe/data/verification/page-477.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 477` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:28:19.338Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:28:20.115Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:28:20.129Z] TOOL RESULT

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


## [2026-09-14T02:28:20.622Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-477.txt"
}
```


### [2026-09-14T02:28:20.651Z] TOOL RESULT

```
1	=== PDF page 477 (book page 447) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Steg, Teg : to cover  (refs POK:1013)
4	#1 (parent #0) [Old Persian] refs=KNT:186 | tačara : cover, house, castle
5	  #2 (parent #1) [Persian] refs=HRN:84; BQT:472 | tajar «تَجَر ( تَزَر ، طَزَر )» : winter house, castle
6	#3 (parent #0) [Persian] refs=AHD:1543; KLN:1510 | tâj «تاج» : crown
7	  #4 (parent #3) [Persian] refs=HRN:81; BQT:458 | Tâjîk «تاجیک ( تاجیکستان )» ; tâzî «تازی» : Arab | NOTE: Originally, "tazî, tajî: royal" referred to Iranians in Yemen. Later it referred to Arabs. MON:996 derives "tâjîk" from Turkish :tât: farmer".
8	  #5 (parent #3) [Persian] refs=MON:996 | tâj-var «تاجور» : crown wearer, king ☞Bher 1
9	  #6 (parent #3) [Greek] refs=PRT:719; SHP:358 | tiara : a head dress (crown)
10	    #7 (parent #6) [English] refs=PRT:358 | tiara, tire, attire
11	      #8 (parent #7) [Persian] refs=MON:1014 | tâyer «تایر» : tire,", "wheel crown"
12	  #9 (parent #3) [Hindustani] refs=None | 
13	    #10 (parent #9) [English] refs=PRT | Taj Mahal : royal place (palace), a mausoleum in India
14	#11 (parent #0) [Germanic] refs=POK:1013; AHD | thakjan : to cover ; thakam : roof
15	  #12 (parent #11) [English] refs=AHD | thatch : foliage used for building roofs ; deck
16	#13 (parent #0) [Latin] refs=AHD | tegere : to cover ; tegula : tile
17	  #14 (parent #13) [English] refs=AHD | tile, toga, detect, protect
18	#15 (parent #0) [Old Irish] refs=AHD | tech : house
19	  #16 (parent #15) [Irish] refs=AHD:1191 | sean tig : old house
20	    #17 (parent #16) [English] refs=AHD:1191 | shanty : cabin
21	--- entry 1 ---
22	ROOT [Indo-European] Stei, Stâi 2 : stone  (refs POK:1010)
23	#1 (parent #0) [Avestan] refs=POK:1010; KLN:1518 | stâ 2, stây : heap
24	  #2 (parent #1) [] refs=None | 
25	#3 (parent #0) [Germanic] refs=AHD | stainaz : stone ; stîfaz : stiff
26	  #4 (parent #3) [Swedish] refs=AHD:1381 | tung-sten : heavy stone
27	    #5 (parent #4) [French] refs=None | 
28	      #6 (parent #5) [Persian] refs=AMD:628 | tangstan «تنگستن» : "heavy stone"
29	  #7 (parent #3) [English] refs=AHD | stone, tungsten, stiff
30	
```


## [2026-09-14T02:28:23.503Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-477.json",
 "description": "Read source JSON for page 477"
}
```


### [2026-09-14T02:28:23.548Z] TOOL RESULT

```
{
  "pdf_page": 477,
  "book_page": 447,
  "entries": [
    {
      "root": {
        "name": "Steg, Teg",
        "lang": "Indo-European",
        "refs": "POK:1013",
        "gloss": "to cover"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:186",
          "words": [
            {"translit": "tačara", "gloss": "cover, house, castle", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:84; BQT:472",
          "words": [
            {"translit": "tajar", "gloss": "winter house, castle", "script": "تَجَر ( تَزَر ، طَزَر )"}
          ],
          "note": null,
          "quote": {
            "text": "میان این تجر و گنبد فلک فرق است - که هست این بثبات، آن نباشد آرامش",
            "poet": "Nazârî Qahestânî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "AHD:1543; KLN:1510",
          "words": [
            {"translit": "tâj", "gloss": "crown", "script": "تاج"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "HRN:81; BQT:458",
          "words": [
            {"translit": "Tâjîk", "gloss": null, "script": "تاجیک ( تاجیکستان )"},
            {"translit": "tâzî", "gloss": "Arab", "script": "تازی"}
          ],
          "note": "Originally, \"tazî, tajî: royal\" referred to Iranians in Yemen. Later it referred to Arabs. MON:996 derives \"tâjîk\" from Turkish :tât: farmer\".",
          "quote": {
            "text": "عرب دیده و تُرک و تاجیک و روم - زهر جنس در نفس پاکش علوم",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:996",
          "words": [
            {"translit": "tâj-var", "gloss": "crown wearer, king", "script": "تاجور", "see": ["Bher 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Greek",
          "refs": "PRT:719; SHP:358",
          "words": [
            {"translit": "tiara", "gloss": "a head dress (crown)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "PRT:358",
          "words": [
            {"translit": "tiara, tire, attire", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:1014",
          "words": [
            {"translit": "tâyer", "gloss": "tire,\", \"wheel crown\"", "script": "تایر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 3,
          "lang": "Hindustani",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "PRT",
          "words": [
            {"translit": "Taj Mahal", "gloss": "royal place (palace), a mausoleum in India", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Germanic",
          "refs": "POK:1013; AHD",
          "words": [
            {"translit": "thakjan", "gloss": "to cover", "script": null},
            {"translit": "thakam", "gloss": "roof", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "thatch", "gloss": "foliage used for building roofs", "script": null},
            {"translit": "deck", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "tegere", "gloss": "to cover", "script": null},
            {"translit": "tegula", "gloss": "tile", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "tile, toga, detect, protect", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Old Irish",
          "refs": "AHD",
          "words": [
            {"translit": "tech", "gloss": "house", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Irish",
          "refs": "AHD:1191",
          "words": [
            {"translit": "sean tig", "gloss": "old house", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": "AHD:1191",
          "words": [
            {"translit": "shanty", "gloss": "cabin", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Stei, Stâi 2",
        "lang": "Indo-European",
        "refs": "POK:1010",
        "gloss": "stone"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1010; KLN:1518",
          "words": [
            {"translit": "stâ 2, stây", "gloss": "heap", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "stainaz", "gloss": "stone", "script": null},
            {"translit": "stîfaz", "gloss": "stiff", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Swedish",
          "refs": "AHD:1381",
          "words": [
            {"translit": "tung-sten", "gloss": "heavy stone", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "AMD:628",
          "words": [
            {"translit": "tangstan", "gloss": "\"heavy stone\"", "script": "تنگستن"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "stone, tungsten, stiff", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T02:28:24.528Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---\" && ls data/verification/sources/refs/ | head -80",
 "description": "List verification dir and refs"
}
```


### [2026-09-14T02:28:24.594Z] TOOL RESULT

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
page-128.json
page-129.json
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
---
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
```


## [2026-09-14T02:28:48.580Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','HRN','BQT','AHD','KLN','MON','PRT','SHP','AMD','WLD','IEC','SYN','PHD','NYB','BRT','HUB','CHEUNG','ARY','SKT','FSD','WEB','LKT','TTS','HJB','AID','FVQ']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-14T02:28:49.302Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T02:28:49.518Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q

SHP {"title": "J. T. Shipley, Dictionary of Word Origins, New York 1945", "edition_found": "1945 (lending-only)", "kind": "hathitrust_fullview+archive_restricted", "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.32106001576476 (1945 ed., rightsCode pd = FULL VIEW, catalog record 001441050) ; archive.org dictionaryofword00ship and 15 others = lending only", "identifier": "dictionaryofword0000jose_n4p8 (also dictionaryofword0000jose_n6p4, dictionaryofword0000ship_d0v5)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.", "notes": "RE-SEARCH

AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Entry-level verification only."}

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

CHEUNG null

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
```


### [2026-09-14T02:28:49.611Z] TOOL RESULT

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
```


## [2026-09-14T02:28:53.809Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK (s)teg- ===\"\ngrep -n \"steg-\" POK_full.txt | head -30\necho \"=== POK stāi ===\"\ngrep -n \"stāi-\" POK_full.txt | head -20"
}
```


### [2026-09-14T02:28:53.916Z] TOOL RESULT

```
=== POK (s)teg- ===
81683:e-Reihe war preferred through die Germanic Ablegerfrom *steg- ' shaft, pole' (e.g. Old 
81686:meaning from *steg-: Old Icelandic stika. Old High German 5/^/7/70 'Stecken' (latter but 
81719:References: WP. II 614; different Vasmer 3, 8 (to steg-2). 
=== POK stāi ===
```


## [2026-09-14T02:28:55.628Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT tacara ===\"\ngrep -n -i \"tacara\\|tačara\" KNT_full.txt KNT.txt | head -20\necho \"=== AHD steg ===\"\ngrep -n -i \"^steg\\|steg-\\|(s)teg\" AHD_watkins1985.txt | head -20\necho \"=== AHD stei ===\"\ngrep -n -i \"tungsten\\|shanty\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T02:28:55.770Z] TOOL RESULT

```
=== KNT tacara ===
KNT.txt:717:taxsacd. in borrowed tacaram DPa 6, ХР], and dacaram DSd 3. (b) c/& in late inscriptions: haga A'Sde 4, for the usual hacá. Xsayarcahyd A'Sa 2 bis, for XSayarsa ete. {ustalcandm A’Sc 5f, for ustasanàm A?Pa 22. Ardaxcasca AVsa for Ат{ах$ага. (с) с and variants: in late Ardaxcasca AVsa, for ArtaxSaca. in late Мита), M'tra, M*$ra (see Lexi- eon), and the Persian personal name Vau-misa DB 2.49 ete. Other variants are explained in the phonology
KNT.txt:1084:V. There are also numerous instances of OP { @ d which are not traceable with certainty to IE origins, or are demonstrably borrowings from non-IE sources. Among these are taka- ‘shield, round hat’ in faka-bara-, tacara- ‘palace’, dipi- ‘inscription’ (see Lex. s.v.), spáda- ‘army’ (only in Iranian), imv. rax@atuv of uncertain meaning; and personal and place names such as Atamaita- (Elamite), Nadztabaira (Semitic), Ufratu- 'Eu- phrates', Katpatuka ‘Cappadocia’, Tigra- ‘Tigris’, Putaya- ‘Libyan’, Datwahya-, Daha-, Dwubála-, Mudràya-, Aburā, etc.
KNT.txt:2812:§26b. THe DEMONSTRATIVE NSM.-NSF. туйт ‘this’, with its suppletions (§199), is likewise either pronoun or adjective, mainly of the following types: tyam Pàrsa ‘this is the Persian’ (DN I), hya imam tacaram akunaus ‘who built this palace’ (DPa 5f) zšāyaðiya ahyayd bimiyd vazrakayd ‘king in this great earth’ (DNa 110). It is а pro- noun with rather distant reference in tya imaty kàram adurujwasa ‘so that these deceived the people’ (DB 4.34f), where zmazy refers to the rebel pretenders listed in DB 4.7-30.
KNT.txt:3373:XPk = Xerxes, PERSEPOLIS к: OP and Elam., each in one line, on the garment of the king’s figure in the eastern part of the middle door of the tacara. Hz. ApI 42 No. 18 (1938); Sen, OPI 255 (1941).
KNT.txt:4037:DPa = Darius, PERSEPOLIS A. 1 Darayavaus : xsayafiya : 2 vazraka : xsdya(lya : x&à 8 yafiyánàm : xšāyaðiya : 4 dahyünàm : Vistaspahy 5 à : puça : Haximanidiya : h 6 ya : imam : tacaram : akunaus
KNT.txt:4624:XPj = XERXES, PERSEPOLIS J. adam : Xšayāršā : XS : vazraka : XŠ : XSyanam : XŠ : DHyünäm : XS : ahyaya : bümiyà : Dárayavahaus : XSyahya : риса : Haxamani&iya : бабу : Xšayäršā : XS : imam : tacaram : adam : akunavam XSc = Xerxes, SUSA C.
KNT.txt:5428:tacara- sb. ‘palace’: NPers. tdzér, Elam. da-is- ѕа-та-ит, Akk. bit (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
KNT.txt:5509:dacara-, see tacara-.
KNT_full.txt:3548:in borrowed tacaram DPa 6, ХР], and 
KNT_full.txt:5012:round hat’ in faka-bara-, tacara- ‘palace’, dipi- 
KNT_full.txt:12646:imam tacaram akunaus ‘who built this palace’ 
KNT_full.txt:16054:in the eastern part of the middle door of the tacara. 
KNT_full.txt:19014:6 ya : imam : tacaram : akunaus 
KNT_full.txt:21337:: бабу : Xšayäršā : XS : imam : tacaram : adam 
KNT_full.txt:25946:tacara- sb. ‘palace’: NPers. tdzér, Elam. da-is- 
KNT_full.txt:26396:dacara-, see tacara-. 
=== AHD steg ===
1006:steg-. Pole, stick. O-grade form *stog- in Germanic *stak- in: a. Old English staca, stake: sTAKE!; b. Old Norse stakkr, haystack: stack; c. Old Norse staka, to push, cause to stumble (as with a stick): STAGGER; d. Old Italian attacare, to attack: ATTACK; e. Old French atta- chier, to attack: ATTACH; f. Spanish estaca, stake: STOCKADE. [Pok. 2. (s)teg- 1014.]
1007:(s)teg-. To cover. I. O-grade form *tog-. 1. Germanic *thakjan in: a. Old English theccan, to cover: THATCH; b. Middle Dutch dekken, to cover: DECK?; c. Old High German decchen, to cover: DECKLE. 2. Germanic *tha- kam in Middle Dutch dec, decke, roof, covering: DECK}. 3. Suffixed form *tog-d-, covering, in Latin toga, toga: TOGA. 4. Possibly Sanskrit sthagayati, he covers: THUG. II. Basic form *steg- in Greek stegein, to cover: STEGODON. III. Basic form *teg-. 1. Latin tegere, to cover, and tegula, tile: TECTRIX, TECTUM, TEGMEN, TEG- MENTUM, TEGULAR, TEGUMENT, TILE, TUILLE; DETECT, INTEGUMENT, OBTECT, PROTECT. 2. Persian fdj, crown: Tad. [Pok. 1. (s)teg- 1013.]
1008:stegh-. To stick, prick; pointed. 1. Nasalized form *stengh- perhaps in Germanic *stingan in Old English stingan, to sting: STING. 2. O-grade form *stogh- in: a. Germanic *stag- in Old English stagga, stag: STAG; b. Greek stokhos, pointed stake or pillar (used as a target for archers), goal: STOCHASTIC. [Pok. stegh- 1014.]
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1681:INQUIRE quaerere INSCRIBE skribh- INSECT sek- INSERT ser-3, s6-1 INSESSORIAL sed-1 INSIGNIA sekw-1 INSIST sta- INSOLATE sawel- INSOMNIA swep-! INSPECT spek- INSPIRE spirare INSTALL | stel- INSTALLMENT! | stel- INSTANT sta- INSTAURATION sta- INSTIGATE | steig- INSTINCT | steig- INSTITUTE sta- INSTRUCT  ster-2 INSULT sel-4 INSURE cura INTACT tag- INTEGER tag- INTEGUMENT (s)teg- INTELLIGENT leg-1 INTEND ten-
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2138:PROSTYLE sta- PROTAGONIST ag- PROTASIS ten- PROTECT (s)teg- PROTEIN per! PROTEROZOIC per! PROTEST trei- PROTHALLUS dhal- PROTHESIS dhé-1 PROTHONOTARY gnd- PROTIST per! PROTO- pert PROTOCOL koli- PROTON per! PROTONEMA (s)né- PROTOPATHIC kWent(h)- PROTRACT tragh- PROTRUDE treud- PROTUBERATE teue- PROUD es-
2281:SPRINGE spergh- SPRINKLE (8)preg- SPRIT sper-4 SPROUT sper-4 SPRY (s)preg- SPUME (S)poi-mo- SPUR spere- SPURGE peue- SPURN spere- SPURRY (s)preg- SPURT sper-4 SPUTNIK ksun, pent- SPUTTER spyeu- SPUTUM spyeu- SPY spek- SQUAD kWetwer- SQUALENE (8)kWal-o- SQUARE kWetwer- SQUASH2 kwét- SQUAT ag- SQUIRE skei- SQUIRREL ors-, skeoi- STABLE! sta- STABLE? sta- STACK steg- STACTE stag- STADDLE sta- STADHOLDER sta- STAFF! stebh- STAG stegh- STAGE sta- STAGGER steg- STAGNANT stag- STAIN teng-
2283:STAIR steigh- STAKE! steg- STALAG legh-, stebh- STALK! | stel- STALK?  ster-4 STALL  stel- STALLION stel- STALWART wer-3 STAMEN sta- STAMMEL sta- STAMMER stam- STAMP stebh- STAMPEDE stebh- STANCE sta- STANCH sta- STANCHION sta- STAND sta- STANDARD kar-1, sta- STANZA sta- STAPHYLO- stebh- STAPHYLORRHAPHY wer-3 STAPLE! stebh- STAPLE? stebh- STAR ster-3 STARBOARD bherdh-, sta- STARCH  ster-1 STARE ster-1 STARETS sta- STARK ster-1 STARLING!  storo- STARLING? sta- START sster-1 STARTLE  ster-1 STARVE ster-1 STASIS sta-
2291:STEER? sta- STEEVE! steip- STEGODON (s)teg- STEIN stei-
2307:STOA sta- STOCHASTIC stegh- STOCK (s)teu- STOCKADE steg- STOIC sta- STOICHIOMETRY steigh- STOKER (s)teu- STOLE! stel-
2336:TaaL del-2 TABES ta- TACET tak-1 TACHE dek-? TACHISM deik- TACHYLYTE leu-! TACHYPNEA pneu- TACIT tak-1 Tack! dek-2 TACT tag- TACTICS tag- TACTORECEPTOR tag- TAEL tele- TAENIA ten- TAFFETA temp- TAG! dek-2 TAHSILDAR dher-2 TAIL! dek-2 TAINT teng- Tad (s)teg- TAKE tak-2 TALE del-2 TALENT tela- TALES to- TALION tele- TALISMAN kWel-1 TALK del-2 TALLOW del-4 TAME deme-2 TAMPON tap- TANDEM to- TANG! denk- TANGENT tag- TANGIBLE tag- TANGLE? tenk-2 TANGORECEPTOR tag- TANSY dhwene- TANTALIZE tele- TANTALUS tele- TANTAMOUNT to- TANTRA ten- Tap! tap-
2349:TEAR? dakru- TECHNICAL teks- TECHNOLOGY teks- TECTONIC teks- TECTRIX (s)teg- TECTUM (s)teg- TEEM! deuk- TEEN? deu-3 TEETER der-1 TEETOTUM teuta- TEGMEN (s)teg- TEGMENTUM (s)teg- TEGULAR (s)teg- TEGUMENT (s)teg- TEIGLACH dheigh- 'TELAMON tele- TELANGIECTASIA ten- TELE- kwel-2 TELEKINESIS kei-3 TELEOLOGY kWel-1 TELEOST kWel-1, ost- TELESCOPE spek- TELEUTOSPORE kwel-1 TELIC kwel-1 TELIUM kwel-1 TELL del-2 TELLURIAN tel- TELLURIC tel- TELLURION tel- TELLURIUM tel- TELLURO- tel- TELO- kwel-1 TELPHER bher-1 TEMERARIOUS teme- TEMERITY teme- TEMPLE! tem- TEMPLE? temp- TEMPLES tem-
2366:THATCH (s)teg- THAUMATURGE werg- THAW ta-
2388:THRUST treud- THUG (s)teg- THUJA dheu-! THUMB teue- THUNDER (s)tene- THURIBLE dheu-! THURIFER dheu-! THURSDAY (s)tene- THUS to- THWART terkw- THY tu-
2389:THYME dheu-! -THYMIA dheu-1 THYROID dhwer- TICK? deigh- TICK3 dhé-1 TICKET steig- TIDE! da- TIDE2 da- TIDINGS da- TIE deuk- TIERCE trei- TIFFANY bha-1 TIGER steig- TIGHT tenk-2 TILE (s)teg- TILLER? teks- TILLERS del-3 TILT? del-3 TIMBER deme-1 TIME da- TIMOCRACY kWeig-1 TINCT teng- TINGE teng- TINSEL skeei- TINT teng-
2395:TOFT deme-1 TOGA (s)teg- TOGETHER ghedh- TOIL! (s)teu- TOIL? teks- TOKEN deik- TOLA tele- TOLERATE tele- TOLL! tele- TOMB teue- TOME tem- -TOMY tem- TONE ten- TONGS denk- TONGUE dnghi TONOPLAST ten- TONSURE tem- Too de-
2416:TUILLE (s)teg- TUITION teu-
=== AHD stei ===
1009:stei-. Stone. Suffixed o-grade form *stoi-no- in Germanic *stainaz in: a. Old English stan, stone: STONE; b. Middle Dutch steen, stone: STEENBOK; C. Old Norse steinn, stone: TUNGSTEN; d. Old High German stein, stone, in German Steingut, stoneware: STEIN. [Pok. stdi- 1010.]
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
2420:TUMID teue- TUMOR teue- TUMULUS teu@- TUNGSTEN | stei- TURBARY derbh- TURBID twer-1 TURBINE twer-1 TURD der-2 TUREEN ters- TURF derbh- TURN tere-1 TURNSOLE sawel-
```


## [2026-09-14T02:29:11.831Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['tegos','stégō','stego','tegula','Dach, Decke','decken','sthagayati']:\n    idxs=[m.start() for m in re.finditer(re.escape(pat),t)]\n    print(pat, len(idxs), idxs[:10])\nEOF"
}
```


### [2026-09-14T02:29:12.960Z] TOOL RESULT

```
tegos 2 [1718103, 1718288]
stégō 0 []
stego 0 []
tegula 3 [3422562, 3422725, 3422769]
Dach, Decke 0 []
decken 6 [3209859, 3210584, 3422218, 3422280, 3422421, 3423899]
sthagayati 1 [3422067]
```


## [2026-09-14T02:29:13.145Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1013\" POK_full.txt | head -20\necho \"--- page markers? ---\"\ngrep -n -m5 \"Page\\|\\[pdf page\" POK_full.txt | head"
}
```


### [2026-09-14T02:29:13.209Z] TOOL RESULT

```
81477:Page(s): 1011-1013 
81552:Page(s): 1013-1014 
84934:See also: see above S. 1013 f. under (s)teg- and S. 1055. 
--- page markers? ---
1549:Page(s): 2 
1574:Page(s): 2 
1607:Page(s): 2-3 
1637:Page(s): 1 
1679:Page(s): 3
```


## [2026-09-14T02:29:16.065Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nprint(t[3421700:3424300])\nEOF"
}
```


## [2026-09-14T02:29:16.620Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '81440,81560p' POK_full.txt"
}
```


### [2026-09-14T02:29:17.127Z] TOOL RESULT

```
teh, poln. scieg, sc/g" prick, sting'; 

here as "sich versteifen', with the intonation of a heavy basis: Lithuanian steng-iu, -ti 
"sich anstrengen', Refl. "sich widersetzen', stangus "widerspenstig'? 

References: WP. II 622 f., Vasmer 3, 9, Trautmann 285. 
Page(s): 1014-1015 

Root / lemma: (s)teg-1 

Meaning: to cover 

Material: Old Indie 5//7a^a//(umbelegt), sthagayati^verhuWi, verbirgt'; gr. GTsyu) "cover, 

schijtze etc.', Qit^OQ,, rsyoc; n. (= Old Irish tech), OTEyn, Tsyn f. "roof, house', aiz-^avoc, 

"deckend, sheltering; bedeckt, hidden, concealed', aT£yv6(; "bedeckend, schutzend; 

bedeckt, verschlossen; compact, tight, firm, dense' (see because of this meaning also 

*tegu- "thick'), aT£KTiK6(; "bedeckend, schutzend'; 

Latin tego, -ere^ cover ', tectum 'rooV (= aT£KT6(;), tegu/um' cover, roof, wrapping ', 
teges, -et/'s "cover, mat ', tegula " a roof tile ', toga " the white woolen upper garment worn 
by Roman citizens '; Umbrian tehtenm " a covering, plaster used for covering'; 

Maybe alb. {* tegula) tjegulla^X\\e, brick', truncated {* tegula) tulla'tWe, brick', tehu{*tegu) 
"blade, sharp edge' Latin loanwords [common alb., italic -g- > -/?-] 

Old Irish /ec/7 (neutraler -es-stem = gr. t£YO(;), acymr. tig, ncymr. ty, acorn, //"house', 
abret. bou-tig^ cowshed ' (with unclear brit. /); PI. acymr. te, ncymr. tal, also in Old Irish 
teg-lach^ Hausgenossenschaft ', cymr. teulu, acorn, tellu' family ' {*tego-slougo-). Old 
Irish -tulglur^\ cover' = Old High German decchlu, /^/ge "stramen' {*togla), Imthuge 
"Bedeckung, Bekleidung', cymr. 5/77-o'c»"amiculum, involucrum'. Old Irish e/5c/7 "dress', 
cymr. corn. /c»"roof', cymr. /o/"tegere'; 

Old Icelandic t^ekja "cover'. Old English t^eccan "cover'. Old High German decchen 
"cover' (iterative *togeJd= Old Irish tulglur, under Verdrangung from Indo Germanic *tegd); 
Old Icelandic t^ak. Old English dsec. Old High German dahu. "roof; Old Icelandic t^ekja 
"roof. Old High German decchr cover, roof; Old English t^ecen. Old Saxon theclna6s., in 
addition Old Icelandic staka, stakkai. "fell, fur'; (without s Norwegian dial, taka 
"Schweinshaut'); 



lengthened grade Lithuanian stfegiu stfegtr e\'c\ Dach eindecken', Old Prussian steege 
"barn', Lithuanian s//e^/oyas "Dachdecker', ablaut. st6gas= Old Prussian stog/s'rooV; 
perhaps russ. -Church Slavic stogbm. 'barn, haystack, heap'. 

References: WP. II 621 f., WH. II 654 f., Trautmann 288. 
Page(s): 1013-1014 

Root / lemma: (s)teg-2 

Meaning: pole, stick, beam 

Note: s. also under ste/^r- 'prick' 

Material: Armenian t'akn. Gen. /'a/ra/? 'cudgel, c
```


### [2026-09-14T02:29:17.178Z] TOOL RESULT

```
Maybe alb. stap^ stick, pad, rod ' a Germanic loanword. 

Old Icelandic stefu. {*stabja-), stefnai. {*stabanjdn-) " certain, feste time etc.', Old 
English stefn, sfemmm. "time, Mai, Periode'; Old Icelandic stafnn. 'Steven, Hausgiebel', 
Old Saxon stamnm. 'Steven', Old English stefn, stemnm. 'stem, root, Steven', Old High 
German sfam {-mm-) ' tree truck, Geschlechtsstamm ', Modern High German stem 
(Verquikkung eines *stad-na- \N\t\r\ a *stam-na-: Old Irish tamun ^tree truck'); 

nasalized Old High German stumba/' cut-off piece, stump ', stumb/7dn' mutilate ', Old 
Frisian stemb//nge' mutilation '. 

Lithuanian stembtr stalk ansetzen', stembras, stembrys^ stalk' (= Middle Irish 
semmor), stimbras^ tail stub, tail stump ', zem. stambris^ stalk', Lithuanian stambus 



'coarse, coarsely granulated ', 5/a/77i6'55'Kohlstrunk', Latvian stuobrs^ stem, reed'; 
Lithuanian stebulei. 'hub of a wheel', Latvian stebe^ mast ', russ. stebatb, kir. stebnuty' 
lash, flog; steppen, sew '; stabyti, stabdyti^ halt, stop, cause to stop, block ', stabas' jamb, 
Schlagfluft', Old Lithuanian sfabas' idol ' (gottlich verehrter Pflock), Latvian stabs' pillar, 
column ', Old Prussian stab/sm. ' stone ', stabn/t '( stony) oven', Lithuanian stabaras'6ry 
bough'. Old Church Slavic stoborb ' column '; with the meaning ' be amazed, marvel ': 
Lithuanian stebetis; 

root form in -/?-: 

Old Indie in Kaus. sthapayami' place, found, ground '; 

Old Church Slavic stopa' footprint ', stepent 'grade'. Old Lithuanian s/S/OyZ/s 'stand 
bleiben', Lithuanian s/epas 'Schlagfluft', stapinti' penem erig6re '; 

Old Church Slavic stgpiti, stgpat/'trea6'. 

References: WP. II 623 ff., Trautmann 280, 284, Kniper Nasalpras. 195 ff., Vasmer 3, 16, 

19,35. 

Page(s): 1011-1013 

Root / lemma: stegh-, nasal, stengh- 
Meaning: to stick; pole, stalk, etc.. 

Material: Gr. aT6xo(; 'das assigned purpose, Vermutung' (aroxa^oijai 'ziele, investigate 
from, errate'); Swedish s/a^^ (Germanic *stagga-) 'stiff and stechendes Gras', dial. 'Achel, 
Stichling (fish)', wherefore *staggian- 'with *sting, prick = penis versehen' in Old Icelandic 
stegg/m. 'Stecher', nisi, also 'tomcat, male-cat' (late Old English staggam., engl. stag 'the 
adult male deer', engl. dial, also 'male', from dem Nord.); Prussian-Lithuanian stege, stegis 
'Stichling', Latvian staga{/)s'a prickly fish', stage' A\ant' (also stag/"e\n herb, das as 
cabbage gegessen wird'?); 

nasalized: gr. gtovu^, -uxoc; (geformt after ovux- ' sharp cusp, peak'), gtovu^i Kspaai 
Hes.; omx(J<^, -^oq (also aoraxuc;) m. ' ear ' (a = rf); 

Old Icelandic st/'nga, stakk. Old English st/ngan 'st\ck'; Gothic usstagg "z^zkz, stich 
from!'; Old High German stanga. Old Icelandic stgng'sWck, picket, pole, shaft, pole'. Old 
English steng {* stangi-) ds., nl. steng {*stangid[n]-) ds.. Old High German stengil 'stalk; 
ablaut. Old High German stungen 'pnck'; 



Church Slavic ostegi), serb. -Church Slavic ostezb "dress, mantle'; russ. stegatb, 
stegnutb 'steppen, sew, lash, flog ', stezka^ suture' (ein geschlossener syllable from b 
and aufs/e^a& figurative); Czech steh, poln. scieg, sc/g" prick, sting'; 

here as "sich versteifen', with the intonation of a heavy basis: Lithuanian steng-iu, -ti 
"sich anstrengen', Refl. "sich widersetzen', stangus "widerspenstig'? 

References: WP. II 622 f., Vasmer 3, 9, Trautmann 285. 
Page(s): 1014-1015 

Root / lemma: (s)teg-1 

Meaning: to cover 

Material: Old Indie 5//7a^a//(umbelegt), sthagayati^verhuWi, verbirgt'; gr. GTsyu) "cover, 

schijtze etc.', Qit^OQ,, rsyoc; n. (= Old Irish tech), OTEyn, Tsyn f. "roof, house', aiz-^avoc, 

"deckend, sheltering; bedeckt, hidden, concealed', aT£yv6(; "bedeckend, schutzend; 

bedeckt, verschlossen; compact, tight, firm, dense' (see because of this meaning also 

*tegu- "thick'), aT£KTiK6(; "bedeckend, schutzend'; 

Latin tego, -ere^ cover ', tectum 'rooV (= aT£KT6(;), tegu/um' cover, roof, wrapping ', 
teges, -et/'s "cover, mat ', tegula " a roof tile ', toga " the white woolen upper garment worn 
by Roman citizens '; Umbrian tehtenm " a covering, plaster used for covering'; 

Maybe alb. {* tegula) tjegulla^X\\e, brick', truncated {* tegula) tulla'tWe, brick', tehu{*tegu) 
"blade, sharp edge' Latin loanwords [common alb., italic -g- > -/?-] 

Old Irish /ec/7 (neutraler -es-stem = gr. t£YO(;), acymr. tig, ncymr. ty, acorn, //"house', 
abret. bou-tig^ cowshed ' (with unclear brit. /); PI. acymr. te, ncymr. tal, also in Old Irish 
teg-lach^ Hausgenossenschaft ', cymr. teulu, acorn, tellu' family ' {*tego-slougo-). Old 
Irish -tulglur^\ cover' = Old High German decchlu, /^/ge "stramen' {*togla), Imthuge 
"Bedeckung, Bekleidung', cymr. 5/77-o'c»"amiculum, involucrum'. Old Irish e/5c/7 "dress', 
cymr. corn. /c»"roof', cymr. /o/"tegere'; 

Old Icelandic t^ekja "cover'. Old English t^eccan "cover'. Old High German decchen 
"cover' (iterative *togeJd= Old Irish tulglur, under Verdrangung from Indo Germanic *tegd); 
Old Icelandic t^ak. Old English dsec. Old High German dahu. "roof; Old Icelandic t^ekja 
"roof. Old High German decchr cover, roof; Old English t^ecen. Old Saxon theclna6s., in 
addition Old Icelandic staka, stakkai. "fell, fur'; (without s Norwegian dial, taka 
"Schweinshaut'); 



lengthened grade Lithuanian stfegiu stfegtr e\'c\ Dach eindecken', Old Prussian steege 
"barn', Lithuanian s//e^/oyas "Dachdecker', ablaut. st6gas= Old Prussian stog/s'rooV; 
perhaps russ. -Church Slavic stogbm. 'barn, haystack, heap'. 

References: WP. II 621 f., WH. II 654 f., Trautmann 288. 
Page(s): 1013-1014 

Root / lemma: (s)teg-2 

Meaning: pole, stick, beam 

Note: s. also under ste/^r- 'prick' 

Material: Armenian t'akn. Gen. /'a/ra/? 'cudgel, club, beetle, hammer, club, mace, joint',
```


## [2026-09-14T02:29:23.202Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 1010\\|Page(s): 1009-1010\\|Page(s): 1010-1011\" POK_full.txt | head"
}
```


### [2026-09-14T02:29:23.259Z] TOOL RESULT

```
80984:Page(s): 1010 
80996:Page(s): 1010 
81042:Page(s): 1010-1011
```


## [2026-09-14T02:29:24.786Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '80920,81045p' POK_full.txt"
}
```


### [2026-09-14T02:29:24.847Z] TOOL RESULT

```
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

References: WP. II 706; Machek Slavia 16, 191, IF. 53, 94; Vasmer3, 272 f. 

Page(s): 1 004 

Root / lemma: stag- 
Meaning: to drop, drizzle 

Material: Gr. ara^u), aTa^w GTaynvai "drip, trickle, eintraufein tr., drip, trickle let; drip, trickle 
intr., rinnen', araKToq "tropfeind, tropfend', araycbv, -6vo(;f. "drip', omyzq PI. ds.; 

Latin stagnum^]e6es ausgetretene Gewasser, sea, pond, pool, pond, pool or langsam 
running Gewasser'; 



Latin (Celtic loanword?) stagnum'Z\nn' ("das Getropfte, light Schmelzbare'), Old Irish 
Stan 'Z\nn'; cymr. ystaen, ncorn. stean, bret. stean {irovc\ Latin?); 

abret. staer, nbret. s/e^'river, stream, brook' {*stagra), cymr. /ae/7"conspersio, 
adspersio' {*stagna). 

References: WP. II 612, WH. II 585, Flasdieck Zinn under Zink 14 ff. 
Page(s): 1010 

Root / lemma: (s)tai- 
Meaning: to conceal; to steal 

Material: Old Indie stayat^ clanoestine, hide, conceal', stay'u-, tay'u- "thief (= Old Church 
Slavic /ay Adv. 'secret ', if from *tajLr, gr. Tr|u-aiO(;); steya-m^ theft ', stena- 'thief; Avestan 
tayu- 'thief, taya- ' theft '; gr. rriuairi 656c; 'ein way, the einen um die MiJhe the intention 
betrugt' (*tc(u-tio(;, from *tc(ju-tc(), Tniri arropia, £v5£ia, GTspnaK; Hes., rriTau) 'bringe um 
etwas, rob', Med. 'darbe'; Old Irish /a/io''thief (= Old Bulgarian tatb, das -o'analogical); Old 
Church Slavic /ay" secret ', tajQ, tajiti^ hide ', tatb 'thief; Hittite tajezzi, /ayazz/'stiehit'. 
References: WP. II 610, Trautmann 313, Vasmer 3, 69. 
Page(s): 1010 

Root / lemma: stai-, sff- sti-a- 

Meaning: to condense, press together 

Note: in addition steib(h)-, steip-^ shaft, pole etc' 

Material: Old Indie s/yaya/e'gerinnt, wird hart', participle styana-; (Gramm.) prastJma- 

'gedrangt, gehauft', s//777a-'idle' (actually ' jammed, packed, stuck '), vistTmfn- Bez. of 

pudenda, stfyai. 'trages, stehendes water', stimita- ' clumsy, idle, unbeweglich, damp'; 

Avestan sta{}/)- 'heap, mass'; 

gr. GTsap, oitaioQ, 'stehendes fat, tallow, suet' {*stajj)\ hom. ayxi-aiTvoq ' near 
aneinandergedrangt' (compare Old Indie stya-na-); afia f., gtTov n. ' small stone '; oY\kr\ 
'drip' (compare Latin stfr/'a, stTlla); 

Latin s//?/a 'frozen drip, icicle', Demin. s//7/a'drip' {*stTr[e]la); 

nisi. 5//?^/" 'stiffness in the eyes', Norwegian stTra, Old Icelandic stira, Danish Swedish 
stirra^Qaze, stare'. East Frisian s//?' stiff, rigid'. Modern High German stier, stieren, 
Lithuanian styrstu, styrti' solidify, congeal ', styrau, -oti^ stiff and lijmmelhaft dastehen'; 



Old Icelandic stfmn. " restlessness, din, fuss, noise', Norwegian 5//777Tischschwarnn', 
Middle High German st/m, ste/m ^bunte bulk, mass, Getummel'; 

Gothic stains. Old Icelandic steinn. Old English stan. Old High German stein ' stone '; 

Old Church Slavic stena'\Na\\', stentnh " stony '; 

perhaps also Old Icelandic s//"n. "stall', stTa' make a hedge, fence ', Old English stig, stT 
" pigpen; hall'. Middle Low German s/ege "corral, pen, fold'. Old High German stTga, Middle 
High German stTge, 5/ye "stall or Lattenverschlag for small cattle'; 

Lithuanian stlngtr curdle, coagulate, harden ', Latvian stingt^ compact become', stingrs 
"stramm, rigid, zusammenhaltend, gespannt, stiff; 

about Latin ///77ed "dread myself, etc. s. WH. II 682. 

References: WP. II 610 f., WH. II 595; 
See also: s. also steya-S. 1035. 
Page(s): 1010-1011 

Root / lemma: stak-, stek-
```


## [2026-09-14T02:29:37.007Z] TOOL CALL #15: Bash

```json
{
 "command": "ls site/pages/477.jpg 2>/dev/null; pdftoppm -f 477 -l 477 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg477 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg477.png"
}
```


### [2026-09-14T02:29:39.098Z] TOOL RESULT

```
site/pages/477.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 84381 Sep 13 22:29 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg477.png
```


## [2026-09-14T02:29:40.930Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg477.png"
}
```


### [2026-09-14T02:29:41.490Z] TOOL RESULT

```

```


## [2026-09-14T02:29:41.482Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:29:56.862Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN taj/tazar ===\"\ngrep -n -i \"tāǰ\\|tâǰ\\|taǰ \\|tāj\\|tazar\\|tāzar\\|tažar\\|Krone\" HRN.txt | head -40"
}
```


### [2026-09-14T02:29:56.925Z] TOOL RESULT

```
=== HRN taj/tazar ===
1280:99. efser 'Krone'.
1281:aw. ^aiwisara-; phlv. afsar 'Krone' (6ö§t-T Fr.)^).
3437:17. täj 'Krone*, täjver,
3440:ebenso wenig mit assyr. agü 'Krone' (nach Jensen,
3543:arab. LW. tazar,
3710:*Krone* elamitischen Ursprungs wäre, ebenso wie taka- in takabarä, so
```


## [2026-09-14T02:29:58.225Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 taj ===\"\ngrep -n -i \"^Taj\\|Taj Mahal\\|tiara\" KLN_1966.txt | head -20\necho \"=== KLN 1971 ===\"\ngrep -n -i \"Taj Mahal\\|tiara,\" KLN_1971.txt | head -20"
}
```


### [2026-09-14T02:29:58.315Z] TOOL RESULT

```
=== KLN 1966 taj ===
38028:taj,  ‘crown’,  fr.  Pers.  taj,  of  s.m.  See  stemma. take,  tr.  and  intr.  v.  —  ME.  taken,  fr.  OE.  tacan, fr.  ON.  taka,  rel.  to  MLG.  tacken,  MDu.  taken, Goth,  tekan,  ‘to  touch’ ;  of  uncertain  etymology. Cp.  the  second  element  in  wapentake.  Late  OE. tacan  has  replaced  OE.  niman,  which  has  sur¬ vived  only  in  the  adjective  nimble.
39216:tiara,  n.,  head  dress.  —  L.  tiara,  fr.  Gk.  vtapa, which  is  of  Oriental  origin.
=== KLN 1971 ===
247785:tiara, n., head dress. — L. tiara, fr. Gk. Ttapa,
```


## [2026-09-14T02:30:04.530Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3430,3460p' HRN.txt\necho \"=== ~3540 ===\"\nsed -n '3530,3560p' HRN.txt\necho \"=== ~3700 ===\"\nsed -n '3695,3725p' HRN.txt"
}
```


### [2026-09-14T02:30:04.614Z] TOOL RESULT

```
(vergl. Hörn, KZ. 32, 584 No. 17).
T.
)6. tä *bis; damit*.
phlv. ^öi6(?), Hs. tai oder tag, vd. 3 (136) (Thon-
nelier; Spiegel 11), päz. afi]dak, an\dd (phlv. 11).
kurd. da 'damit' ; bei. da\l7i, da[m, da[n/{ö 'bis jetzt,
noch* (73).
17. täj 'Krone*, täjver,
arm. LW. fag, fagavor.
Hat mit ap. Yauna takabara nichts zu tun; und
ebenso wenig mit assyr. agü 'Krone' (nach Jensen,
mündliche Mitteilung).
de Lagarde, Nachr. GGG. 1891, 160 folg. stellt
np. Täßk, Täzik, TäzT f Ureinwohner Persiens, die
weder Araber noch Türken sind' (vergl. phlv. Tajik
(Bund.), arm. Tacik 'Araber), taziyüne 'Peitsche'
*) Aw. pivasca steht neben *pivo (ohne nachfolgende Enklitika)
e starewcä neben stärem (Burtholoniae, Handbuch § 69 Anm. 2).
Hörn, Grundrisg d. noup. F^tyniolugio.- 82 —
ursprünglich ^arabisch' (*die Semiten sind ja gegen
unterworfene Völker nie sehr gütig gewesen) zu taj.
Die Erklärung Quatremere's (Tazi als Nisbe von
Tai) ist indess auch nach Nöldeke*s Meinung die
richtige.
368. täyten *laufen; laufen machen (z.B. ab)\ Praes. täz-em,
täz^ täziSj taziyän.
aw. l^taC' 'laufen'; ai. l/^tak- *dahinschiessen,
stürzen; phlv. ta/tan, tacet^) (Bund., Bahmyät),
tacänitan (Bund.), täc(i)sn (Bahmy§t), viel häufiger mit
mittlerem Stamm faöltan, taöat (vd. 5 (43)), tacend
(vd. 5 (57)), tacet (vd. 8 (287) flf.), tazad (vd. 8 (280),
=== ~3540 ===
Das auslautende t in tat beruht auf Übertragung
wie in np. sm {sö%) — phlv. sük (sök), jüd.-pers. "]1D
(Jer. 17, 1), arab. LW. süq — np. deräl 'Schelle' —
jüd.-pers. <3X"n (Is. 3, 16, 18) — u. a. m.
374. teber, tewer 'Beil', arab. LW. tabar,
phlv. tabrak, y. 9 (89); arm. tapar (LW.?); kurd.
tefer, tewir; bei. tapar, toivär, n. fafar (380); wa;^.
tipdr; russ. topor.
np. teberzed (arab. tabarzad) ist Zucker, 'der so hart
sein soll , dass man , um ihn zu zerhauen , ein Beil
anwenden muss' (el Sejestänl bei Ibn Baitär).
Volksetymologie ?
375. tejer 'Winterhaus mit Heizvorrichtung; Magazin*,
arab. LW. tazar,
ap. tacara- (Bedeutung nicht sicher); arm. LW.
tacar *Hau8, Tempel', tacarapet aoxi^T(}Uhvog,
376. te^s Tfeil' (Sahn. I, 466, V. 521).
gr. roV; Hübschmann, ZDMG. 38, 430.
377. teyßä 'eifrig, geschäftig.
ap. vergl. hamata^saly^ hamata/satä (Bartholomae,
Studien II, 22 Note 1) ; aw. [/'^wa/s-, i^wa/sa- 'eifrig ,
&wa/sah-^ S^wa/sista-; phlv. tu/säk {päz. tu/sä), tu/säkth^
tuxs(l)sn, tu^sUan; ai. tväksas^ 'Thatkraft'.
378. tuyirn 'Same, Geschlecht', tu/me; arab. LW. tu/m.
ap. taumä' 'Geschlecht'; aw. ttto/man-; phlv. tö/m,
töxnmk bezw. tu/m/ak, päz. tti/m, arm. LW. tohm;
ai. tokman- 'Schössling'.
kurd. töm; wa/. tay^Hy sar. töym, yidg. tüyum.
*) Pehlv. pancötak hat ein mir unverständliches ö; darum scheinen
mir auch de Goeje's (ZDMG. 35, 340) auf ihm beruhende, sonst sehr
ansprechende arab. dahötah^ Instötah zweifelhaft.— 85 —
=== ~3700 ===
(9) 61. — ZDM6. 43, 43 — ist tuhtk zu lesen).
394. tenjlden zusammenziehen ; trinken' (jüd.-pers., z. B.
Is. 63, 6), }T:Nj:n.
aw. i^danj' ziehen' u. s. w. (6 eidner, Drei Yasht,
95). ^ .
oss..t. tlinfin, d. iünjun 'ausdehnen' (249); bei. tajenag
'spannen, dehnen (375).
Der Übergang von der Bedeutung 'ziehen* zu 'trinken
findet sich auch bei np. ähenjiden und kestden.
Da magidüta kein Abstractum auf üiu («', d) sein kann, muss es für
magidäta stehen. Im Neubabyl. wiederholt -ü^w für -äti Endung des
Plurals fem. gen. Agidtu *ßinde* bezeugt (von "I^IX)« Davon könnte
magidtu eine Form MafUlatu sein. Ev. aber auch magidtu : agidlu
= JISi^niD • Ärahsamna, Taka- also höchst wahrscheinlich irgend eine
*Binde' als Kopfbedeckung. Nähme man mit Recht an, dass täj =
*Krone* elamitischen Ursprungs wäre, ebenso wie taka- in takabarä, so
stände der Verknüpfung beider Wörter, soweit wir dies beurteilen können,
nichts im Wege. Die beiden Wörter könnten zu verschiedenen Zeiten
und aus verschiedenen Dialccten entlehnt sein".
Ehe ich Jensen 's Erklärung kannte, hatte ich an siyn. tdki
'Pelzmütze' gedacht, ß e z o 1 d , Achaemenideninschriften 72, hält übrigens
magidüta für den xgwßvXog (Thycyd. I, 6).
*) Aus tan + näz^ de Lagarde, Ges. Abh., 51 Note 4.— 89 —
395. tund schnell, heftig, stark'.
aw. Hvant" (= Hnvant-), [/'tav-, vergl. tuvan (No. 401).
396. tunder, tundur ^Donner .
Vergl. ai. i/^tan-, tdnyati erschallen, laut tönen,
rauschen', tanayitnü- 'donnernd', tanyatii' 'Donner';
lat. tonare, tonitnis; ags. pnnjan, punor, nhd. Donner^
engl, thufider,
397. tenuk *düun, zart, fein'.
```


## [2026-09-14T02:30:23.049Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD tag/crown ===\"\ngrep -n -i \"crown\" PHD.txt | head -20\necho \"--- tʾg ---\"\ngrep -n \"tāg\\|tʾg\\b\" PHD.txt | head -20\necho \"=== PHD tazig ===\"\ngrep -n -i \"tāzīg\\|tazig\\|Arab\" PHD.txt | head -20"
}
```


### [2026-09-14T02:30:23.125Z] TOOL RESULT

```
=== PHD tag/crown ===
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
1448:crown abesar.
--- tʾg ---
772:alone ēwtāg, tag, tanīhā,
905:Avesta abestāg.
1066:branch azg, tāg.
2421:individual ēwtāg, ēwāzīg.
3539:scriptures nibēg; abestāg, hādamāns'r, dad.
3669:single ēwtāg, tāg.
=== PHD tazig ===
92:Later forms of the word are quoted from Judaeo-Persian (J—from whatever source) and the earliest New Persian (N— rarely in their Arabic guise, when this has displaced the Persian, Ar.).
93:When the forms presented are not directly comparable, being from a different dialect or in some way modified (e.g. by popular etymology), they are enclosed in parentheses.
107:Ar. Arabic
120:... N, etc., form not directly comparable = M the same spelling in M, etc.
595:~ih: bitterness. taxt [2А | N ~] throne. ~ag [-#! | N ~a] tablet, plank, (chess) board. taxtan, taz- [Phtn', tc- | M rem, tz-] run, flow. išnīh : flow. tāxtan, taz- [?Аїп!, Pc- | M Рс-, N ~] cause to run, flow; chase; pour. taxt-gàh [?hig’h | N <] couch. taz-, —išnih, v. taxtan. táz-, v. tāxtan, tazāģ [tc’k'] flowing, running. tāzānaģ [P enh | N tāz(y)āna] whip. tazënidan, tazën- [tcyn-ytn'] = tāxtan. tazidan, taz- [tc-ytn'] = taxtan. Itázig [Pcyk! | N tázi] swift, fast. "Táüzig [Pcyk! | N tāzi] Arab. tēmār [tym] | M tym’r, N ~] sorrow, grief, care. ltërag [tylk' | N tēra] dark, turbid. *térag [tylk'] (mountain) peak, summit. téx [tyh | N téy] sharp edge, ridge; ray. Mēz [tye | M tyz, N ~] quick. ~ih: speed. *téz [tye | (P tyj), N ~] sharp. ~ih: sharpness. *tidag [tytk' | (N dida)] pupil (of eye). tigr [HTY A < А Шу; tgl | M tygr, N tir] arrow. *tihóg [tyh:wk! | N tihi] small grey partridge. tir, v. tigr. Tir [tyl | M tyr, N ~] a god (confused with Tištar); astr. Mercury; cal. 4th month; 13th day. tis [MNDOM < А mnd‘m; ts | M, J tys] thing, affair. «iz [-c | M -yc] (with a negative) по... at all. tišn [tyšn!] thirst. tišnag [tyfnk! | M tyšng, N ~a] thirsty. ~th: thirst. Tištar [гуй | № ~] astr. Sirius. të [LK < A l-k | M tw, N tu] thou, thee. *tóf [twp | N to] layer. tóhmag [twhmk' | M twhmg, N tuxma] seed; stock, family. tom [t(w)m | M tm, N tam] darkness. -tom [-twm | (M. -dwm)] suffix forming superlative adjectives. tóm [twm | (M twhm, N tuxm)] seed, family. tórag [twlk' | N tora] jackal. tūšag [twšk! | N tófa] provisions. tóxtan, töz- [twhtn', twc- | M twz-, N ~] atone, expiate. ~išn: atonement, expiation. tóz [twe | N ~] bark, skin.
826:Arab 'Tazig.
1885:fast (a.) tazig; v. quick, swift.
```


## [2026-09-14T02:30:24.642Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB taj ===\"\ngrep -n -i \"täj\\|tāǰ\\|tacar\\|tazar\" HUB.txt | head -20\necho \"=== BRT stay/heap ===\"\ngrep -n -i \"Haufe\" BRT.txt | head -20"
}
```


### [2026-09-14T02:30:24.711Z] TOOL RESULT

```
=== HUB taj ===
8084:tajar *heizbares Winterhaus', arab. tazar 'Sommerhaus* =
8085:ap. tacara-, arm. tadar 'Tempel, Palast, Haus'; varj 'Grosse,
=== BRT stay/heap ===
9605:(sd.)  V. /4-II- Zum  V.  'ioB-,  S  ^SS.  —  Vgl.  >i.  Jihaniira-  n. 'Schaufel';  S  ^41  No.  2.—  Pü.:  ias,  erl.;  ä« ke  .  .  /fl/fli  kanind,  bei.
26723:•  j.  stä(y)-  m.  'Haufen,  Masse';  aßiiia- nqmat  .  .  vazyäis  (sd.)  stilisca  •>  staoysbxi ratsui  nmänim  frSnasayata  A.  J.  5.
```


## [2026-09-14T02:30:37.522Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB tag ===\"\ngrep -n \"tāg\\|tʾk'\\|Krone\\|crown\" NYB_vol2_glossary.txt | head -20\necho \"=== NYB tazig ===\"\ngrep -n -i \"tāzīk\\|tazik\\|Araber\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T02:30:37.587Z] TOOL RESULT

```
=== NYB tag ===
590:api-sar [pysl] crown 6%. — MPrs ’bysr (S); NP afsar. Probably < Olr *upa-sarah- ‘that which is on the head’ (v. sar) > *apa-sara- and then remodelled to "api- sara- with variable accent: *api-sara- > apisar, *ápi-sara- > *apsar > afsar.
900:bälen [b'lyn'] the crown of the head 728. — Paz. bälin, Skr. v. erroneously utsirsaka ‘pillow’ after NP bälin. < OP
1544:Frašāvart [pls’wlt’] the son of Vištaspa, the crown prince and the co-regent of his father 2216, 2314, 2419, - Av. (1010) Fraš.ham.varota-.
3691:tag [t’k'] crown 5619; han i zrös ~ a cockscomb 56°. — Syr. lw. čaja; Arab. lw. taj and hence again NP ta; cf Arm t‘aga-vor ‘king’.
4011:vaspuhr [w’spwhl] belonging to the class of vispuhr (g.v.), i.e. the lawful heirs within the clan or family: [1. adj.: pus ~~ + šāhān farrax"tom (the son entitled to share the patrimony, foremost among the princes =) the crown prince, the heir to the throne SS 10.] — 2. subst. (royal) heir: ~ % Vistäspän the (foremost) heir of the Vistasp family 26”. 2719, of Frašāvart, the crown prince and co-regent (2217). — < *väispudri-, vrddhi derivative from *eispuÜra- (v. vispuhr), v. Bthl, WZKM 25, 1911, 251-254; in Babylonian cunei- form script 4-ma-su- (var. -as-) pe-it-ru-u = *wäspidri- < *wäspudri-, v. Eilers in Taqizadeh Vol., 1962, 55-63. The mean- ing and juridical purport of this term and its derivatives, as also of the basic w. vispuhr and its derivatives, have been
=== NYB tazig ===
```


## [2026-09-14T02:30:38.643Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA taj ===\"\ngrep -n \"تاج\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== AFM taj ===\"\ngrep -n \"تاج\" AFM.txt | head -20"
}
```


### [2026-09-14T02:30:38.711Z] TOOL RESULT

```
=== PLA taj ===
=== AFM taj ===
215:وتاج المصادر والدشديشة 20 اللغات واقدى الارب ܓ اللغات ومشكلات الشهنامة 
1156:. (البندّار) التاجر الذي يازم العادن ܘܰܐܚܠܳܐ ܠܙܐ( واصل معناه صاحب 
1162:جد ( 0( ي اقم عن لاع كد اتاج ه بالامر والسين اغة ٠والسّد‏ اللحيالي : 
1313:١‏ اتاج ). 00 ¿ أب اي ܘܪ ماء 
2007:( الجَوْذَ اهنج ) دواء هندي فارسي معرب (التاج) 
2288:19 شيء الردي وانا - معر , 0 فارسة واه اليابس «التاج) . 
2631:* (الدستآرّان) قال في التاج في مادة دشن :< الداشْن "ܐ 3 | 
3647:93 حاجب مسر بد اي لا شعر عليه عن اع (التاج) 3 من 
3897:وقال في التاج في ترجمة السنبوق وهي لغة في السلبوك :«زورق سفر يعمل في سواحل 
4797:+ لا :” تقول للقطعة من © الفدرة » ٠وفي‏ التاجج :« ¥ ما كان 
5133:قال الاب لامنس في كتاب الفروق:« القسطار هو الصيرف وقيل التاجر. ومن اغرب 
5408:ذلك مألهرن 2 كنا ومعناه التسول والفقيد المحتاج ٠‏ ومنة 016 اي 
5424:د الكردن) 7 30 تاج ماوك فارس 4536 عظيما 0 ان 
5426:مرصعاً بمائة جوهرة ينة كل واحدة منها بكبر بيضة العصفور. 3 هذا اتاج 
5977:الشمس ٠‏ وسن على خلفائه من الملوك ان يعقدوا في ذلك اليوم نفسه التاج على روس 
6158:تاج المرضع ܬܐܨ النفيسة وجاس على العرش امنصوب له ܶܪ | طلعث الشمس 
6167:سؤل جميع الحتاجين و يطلقرن الحموسين ܣ مع ذلك يتعكفهون على !ܠ ܐܙ اث
```


## [2026-09-14T02:31:32.748Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT_v1_pages structure ===\"\ngrep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3\ngrep -c \"\\[pdf page\" BQT_v1_pages.txt\necho \"=== search تاجیک ===\"\ngrep -n \"تاجیک\" BQT_v1_pages.txt | head -10\necho \"=== search تجر ===\"\ngrep -n \"تجر\\b\\|تَجَر\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-14T02:31:32.859Z] TOOL RESULT

```
=== BQT_v1_pages structure ===
0
=== search تاجیک ===
704:از کوه «مورغ» تاجیکتان درسال ۲ هم بدست آمده ودرجپان دانش
911:پارسی نو زبان شپر های شرقی و تاجیکان ناحیه ایران خاوری »
30511:۷ - ر: تك. ۵ در تاجیکی
=== search تجر ===
1799:بپارسی‌قدیم ترجمه کرد درتوحید وتجرید وحکمت‌وطاعت است.و آن‌چپارده
3523:یب - قزوینی ( زبان قزوینی ) : تجر۱۱ توتك » سرك.
7449:آدوین - بر وزن پا کدین » تجربه
7686:م رکب از پیشوند 21 ( < 2ل1 که در پارسی دز» شده) و 118 بمعنی انداز هک فتن ؛ تجربه
9484:عروسانه بر کرسی زر شست شهنتاه رااکشت آیین برست  .‏ نظامی «لخت باحه».و امد تجرید نوفتر
9919:است وزمخشری در زمان‌او بود و ماسلطان‌ستجر
11150:گویند - و بممنی تجربه وآزمایش حم هست .
11162:ادو یی » بروزن‌پروین , تجربه‌وامتحان
14031:اتجره - بروزن پنجره ؛ نباتی است که
16866:و بمعتی مجرد هم‌بنظر ؛مده که از ترك وتجرید
```


## [2026-09-14T02:31:34.405Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON taj ===\"\ngrep -n \"تاجور\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON tayer ===\"\ngrep -n \"تایر\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON tajik ===\"\ngrep -n \"تاجیک\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-14T02:31:34.567Z] TOOL RESULT

```
=== MON taj ===
MON_part1.txt:36433:تاجور: ۱-57 (ص‌مر.) دارای تاج با افسر. 
MON_part1.txt:37098:تایج: آعبج) [غ. تاج ] (افا.) تاجدار» تاجور. 
MON_part1.txt:83278:تاجور. شاه انجم: (کذ.) آفتاب» خورشید. 
=== MON tayer ===
MON_part2.txt:47427:مسثابرت: (عط)احدطاقعهه زع. متایر 5 ] 
MON_part2.txt:58224:قرار کر فته و بتایرای ین دومین طبقه کر چشم 
MON_part1.txt:29902:آنتایرا کنان خی انعر کردن آن ترا کتلان 
MON_part1.txt:61388:شتایر ده. 
MON_part1.txt:86946:محتوای دانه‌ها را می‌خورد و بتایراین از 
=== MON tajik ===
MON_part1.txt:36436:تاجیک: :211 [- تاجک > تازیک (به 
MON_part1.txt:36440:(خصوصا). سکن کنونی «تاجیکستان» 
MON_part1.txt:36843:تازیی: ۱22-1 [- تاجیکک - تاژیک] (ص.
```


## [2026-09-14T02:31:41.040Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36425,36450p' MON_part1.txt\necho \"=== tazi ===\"\nsed -n '36838,36852p' MON_part1.txt\necho \"=== taj headword ===\"\ngrep -n \"^تاج\\|تاج:\" MON_part1.txt | head -10"
}
```


### [2026-09-14T02:31:41.136Z] TOOL RESULT

```
است از تبرة بادنجانیان که علفی است و 
بعض گونه‌هایش بصورت درختچه‌اند. 
برگ‌های آن پهن و گل‌هایش منظم و گل 
آذینش گرزن است. میوه‌اش سته می‌باشد؛ 
انگور روباه» عنب‌العلب. 
تاج‌گذاری: آ2022۲-1-.۱ [معر. ف.] 
9 آیین | نهادن دیهیم بر سر بادشاهی 
نوء جشن تاج گذاردن پادشاهان؛ تتویج» 
تاجور: ۱-57 (ص‌مر.) دارای تاج با افسر. 
بادشاه» سلطان. 

تاجیک: :211 [- تاجک > تازیک (به 
یک معنی) - تاژیک» تر. تات. (رعیت) + 
چیک (پس. تصغیر و تحقیر)] غیر ترک 
(عموماٌ)» آنکه ترک و مغولی نباشد. ایرانی 
(خصوصا). سکن کنونی «تاجیکستان» 
شوروی. صح.- رتاجک» با رتازی» (- 
تاز یک به معنی عرب) فرق دارد. 


۴۳۱۰ فرهنگ فارسی معین تاچه 


تاچه: (ه)هةا [- تایجه: تا (عدل لنگه) + 
چه» سد. تصف.] (ا.مصف.) لنکه خرد» یک 
لنگه از خورجین» یک عدل» یک جوال. 
=== tazi ===
کردن. سوراخ کردن. 

تاریی: -22) [- تازی] (ص. .) تازی» 
طر سب 

تازیی: ۱22-1 [- تاجیکک - تاژیک] (ص. 
.) غیر ترکک. ایرانی؛ ج. تازیکان. 
تازی‌هش: ۰.05 تازی هوش ] (ص‌مر.) 
دارندةٌ هوش و انديشة عربی. 

تارک: *222ا (.) (جاد.) (فره.) رشتة دراز و 
باریکك که در دنبالةٌ پروتوپلاسم برخی 
جانوران تک سلولی وجود دارد. این دنبالة 
پروتوپلاسمی در نتیجه حرکاتی که می‌کند 
موجب سهولت حرکت جانوران تازک‌دار 
=== taj headword ===
12514:استنتاج: لماجه‌ای [ع.] (مسصم.) طلب 
25528:تاجی که درویشان و قلندران بر سر گذارند. 
34074:تاجریزی سرح. (بز.) بیچجش. . (کیا.) نام 
36381:تاج لةا (ا.) کلاه جواهرنشان که شاهان در 
36403:تاج لعل: (کد.) آفتاب. تاج مقوا (مقوی): 
36404:تاجی که از مقوا سازند. تاج هد‌هد: (جان.) 
36414:تاج» تاج‌خانه. (گیا.) گیاه صاحب تاج و 
36418:تاج‌دار: ۱-۲ [معر. ف.] (ص‌مر.) به 
36421:تاجر: لها [ع. ] (افا.) بازرگان» سوداگر؛ 
36424:تاجریزی: 21-12 (امر.) (گیاء) گیاهی
```


## [2026-09-14T02:31:42.812Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- BQT_v1_pages head ---\"; head -c 600 BQT_v1_pages.txt; echo; echo \"--- formfeeds ---\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read(); print(t.count('\\f'))\nt2=open('BQT_v1.txt',encoding='utf-8',errors='replace').read(); print('v1',t2.count('\\f'))\n\""
}
```


### [2026-09-14T02:31:43.983Z] TOOL RESULT

```
--- BQT_v1_pages head ---
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م�
--- formfeeds ---
776
v1 0
```


## [2026-09-14T02:32:04.132Z] TOOL CALL #28: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:472 --image 2>&1 | head -60"
}
```


### [2026-09-14T02:32:05.310Z] TOOL RESULT

```
no scan of BQT covers printed page 472 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:32:14.253Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\nfor i,p in enumerate(pages):\n    if 'تاجیک' in p or 'تازیک' in p or 'تاژیک' in p:\n        print('HIT tajik page idx',i, p[:200].replace('\\n',' | '))\nprint('---tjr---')\nfor i,p in enumerate(pages):\n    if re.search(r'تجر\\s*[-–—]', p):\n        print('HIT tjr idx',i, p[:150].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-14T02:32:15.377Z] TOOL RESULT

```
npages 777
HIT tajik page idx 27 نوزده زبانهای ایرانی | بلکه آنرا فقط بر مردمی اطلاق میکردند که مر کز آنان شپر سمر قند | بوده است ا . | در اینجا لازم است بانار استاد فریمان ۴ عضو وابتهٌ فرهنکستان | شوروی وفرهنگستان ايران راجم بانتشار وضیر ون
HIT tajik page idx 33 یست وینج زبانهای ایرانی | ز بان ازحیطة ز بانهای ایرانی‌خارج‌است. ولی گاه در کتب اسلامی نامز بان | تخاری (طخاریه) بز با نیایرا نی اطلاق شده‌است از [ نجمله ابوریحان بیرونی | در ]نار الباقیه ۱ <]ذرجشن>را از < 
HIT tajik page idx 530 بن کوهی | ممروف است که زیر ره کوش باشد  -‏ و کتابه | ازاطاعت وانقیاد و صدق وادب تمام بود- و سخن | ع ۰ ۳ یز گویند . | لین کوهی» بنتم اول و کسر ثانی » | کیاهی است بیار چرب, واز آن آش پزند. | شاه - بنم اول وسکون ثان
HIT tajik page idx 734 تکیز | اوواحت | کفده اند - وبکسراول لقمه و بارمای از هرچز | باشد ۱ چنانکه کویند *«فلانی چیز را نکه تکه | کرد » » یمنی پاره پاره ساخت ۴ . | لگیز - بر وزن تمیز » تخم واستخوان | انگور راگویند؟ . | تکین بر وزن زمین .نا
---tjr---
```


## [2026-09-14T02:32:21.731Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfa='۰۱۲۳۴۵۶۷۸۹'\nfor i in [500,520,540,560,580,600]:\n    p=pages[i]\n    lines=[l.strip() for l in p.split('\\n') if l.strip()]\n    print('=== idx',i,'first:',lines[0][:80] if lines else '','|| last:',lines[-1][:80] if lines else '')\nEOF"
}
```


### [2026-09-14T02:32:22.804Z] TOOL RESULT

```
=== idx 500 first: و با بای عارسی نیز درست است - || last: ( بر هان قابلع ۴«
=== idx 520 first: مکتك ون || last: و جم فارسی , قومی باشند صحرابی و کم عفل
=== idx 540 first: بو عادران || last: ( بر های فاطی۳ )
=== idx 560 first: بنم ثانث مر وزث میگفت اه || last: معرب آن یمارستان و مارستان «شی». "
=== idx 580 first: پالای || last: *اسشق ۸ ۲۷.
=== idx 600 first: فر ) گنف ه باکاف قارسی بروزندهاوند, || last: (برهان فاطع ۲ )
```


## [2026-09-14T02:32:33.593Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef fanum(s):\n    return all(c in fa for c in s) and len(s)>=2\nfound=[]\nfor i,p in enumerate(pages):\n    for l in p.split('\\n'):\n        l=l.strip()\n        if fanum(l):\n            found.append((i,l))\n            break\nprint(len(found))\nfor x in found[:60]: print(x)\nEOF"
}
```


### [2026-09-14T02:32:34.697Z] TOOL RESULT

```
19
(217, '۲۳۶۱')
(331, '۹۰')
(347, '۱۳')
(378, '۳۳')
(403, '۱۲')
(437, '۲۱۷')
(447, '۳۹')
(457, '۳۹')
(496, '۷۱')
(528, '۲۳۳')
(539, '۳۵')
(550, '۱۳')
(563, '۳۳')
(592, '۳۹')
(656, '۵۵')
(662, '۳۵۰')
(685, '۳۳')
(687, '۲۲')
(702, '۳۹')
```


## [2026-09-14T02:32:42.726Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor fn in ['BQT_v1_pages.txt','BQT_alt_v1.txt','BQT_dli_part1.txt','BQT_v1.txt']:\n    try: t=open(fn,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(fn,e); continue\n    pages=t.split('\\f')\n    hits=[]\n    for i,p in enumerate(pages):\n        if re.search(r'تجر\\s*[-–—]|تزر\\s*[-–—]|طزر', p): hits.append(i)\n    print(fn, 'npages',len(pages),'tjr hits',hits[:20])\n    hits2=[i for i,p in enumerate(pages) if 'خانۀ زمستانی' in p or 'خانه زمستانی' in p]\n    print('  winterhouse', hits2[:20])\nEOF"
}
```


### [2026-09-14T02:32:43.987Z] TOOL RESULT

```
BQT_v1_pages.txt npages 777 tjr hits [698]
  winterhouse []
BQT_alt_v1.txt npages 1 tjr hits [0]
  winterhouse []
BQT_dli_part1.txt npages 1 tjr hits []
  winterhouse []
BQT_v1.txt npages 1 tjr hits [0]
  winterhouse []
```


## [2026-09-14T02:32:46.491Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[698]\nprint(p[:2500])\nEOF"
}
```


### [2026-09-14T02:32:47.770Z] TOOL RESULT

```
تا نا گوس
تحر ۴ » بفتم اول وثئاای بر وزن شرر »
خانةٌ زمستانبر! گوبند که در آن ننور و بخاری
باشد - و بزبان قزوین کنجینه و مخزن را
نامند ۴ . #
سمعتی رولدده باشد ۳۹
تجاد 6 - بروزن شراره » بمعنی تبار
است که کره اسب زمن نکرده باشد و بلخت‌زند
ویازند(۱) رونده راگونند؟ .
در ثای فرشت با خای نقطه دار مشتمل بر سی و شش لت و کنات
أ
قع -جتح اولوسکون تالی , ثل کننبد | که بمربی لیل خوانند .
روغن کشیده را گویند ت تحت از دشیر ب نام توابی ات لد
تخت [ بنوسی « کنابه ازشب است
. ٩یفیسوم‎
(۱) چك: ژند و بازند. (۲) چك: شطه دار .
۱ رک : تجاره. ۴ رکه: تجار. ۴ پارسی‌باستان 420278 «بارتولمه
ارمنی 802۲) ( خانه, عمبد ) «اسشق ۳۷۵». دریهلوی681 - 12085 بممنی هعبد بتان
« یی رک ۲۳۰ > ؛ در پارسی تجر و تزد. اصلا یکاخ زمستانی اطلاق ميشده. درنخت جمشید» کاخ
کوچك داریوش بزر کک که در ضلم شمالی صحن « صد ستون > بباشده به « تچره » موسوم است
رسطح قصرمریم مستطیلی است که بطول قرار کرقنه است. «ابران باستان ج ۲ ص .*٩۰-۱8۸۹‏
همین ترر (طزر) است که درکتب لفت‌عرب مقلوبا «طرز» آمده . مولف ناج العروی ذیلط ر ز
در مستدرك آرد: « الطرز بیت الی الطول» فارسی معرب» و قیل هوالبیت‌السیفی. فال‌الازهری اراء
ممرباً و اصله: ترز. » پیداست که هم درتفدیم راء برزاه تصحیف شده و هم در معنی خانةُ زمستانی
بخانةً تابستانی تبدیبل یاقته و شکی نیست که اصل همان تچر وتزر است و اینکه کوید : « بیت
الی الطول > درست با *تچره» داربوش‌تطبیق مبکند. در دواوین‌شمرا نیز «طرزءرا #طرر» نوشته‌اند
(بدو راء مهمله) (رك: طور»:
۴ رکه: مدمه کتاب حاضر: لهجه‌ها دربرهان قاطع. نزاری فهستانی .
گاه نوروز بزرکه و که نوای بسکنه .
« منوچهری دامثانی ۷۹ ».
۵ فحرمز را : پابان کتاب. لفات مثفرقه. ۵ تخار رك: مقدمه کتاب حاضر :
نخاری.  .‏ ت»ه تعاری - (زبان) ؛ رگ : مقدمه کتاب حاضر:تخلری- نخار ستان - ره :
مقدمة کتاب حاضر: شخاری. ‏ . ۵ قخت - بفتح‌اول» پهلوی/20] «ناوادبا ۱5۵ «مسیناله ۲:۱4
ادکاشمی 48166 (سربر)« کربرسن ۹۷ کیلکی/816),ممربآن نیز تخت (نخت‌خواب» ستر» نخت
رمل) «دژی 4۲:۱۲:۱ «ابن‌درید»» «تفس؟؛ کرسی؛اریکه, سربر, مححل‌جلوی شامدر روژ بار وسلام-
شهر وعفر سلطنت_هرجای مسطح وهموار- نشیمنگاه چوبین باآهنین چهار پایه .
( بر هان فاطع۱۴)
۵ - ء زیر قیصران وگاه تخت اردشیر
```


## [2026-09-14T02:32:59.693Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in [683,684,685]:\n    print('====== idx',i)\n    print(pages[i][:1800])\nEOF"
}
```


### [2026-09-14T02:33:00.800Z] TOOL RESULT

```
====== idx 683
تادون ه بر وزن قارون » بممنی_ تیوه
وتاريك باشد؟ .
تار هیخ- با ین نقطه دار بروزن‌چهار
میخ » بخاری باشد که در ابام ژمستان بر روی
هوا یدید[ ید ومانند دودی شود و اطراف دا تبره
وتاريك سازد » و بعریی ضباپ گویند .
ارو اس بر وزن‌جارو, کنه‌باشد وآن
جانوریست که برشتر و کاو و کوسفند وامثارآن
چسد وخون ایشاارا بنکد .
نار و قود- با ای فرشت مروزت ماو
ومور ۰ بمعتی بیار نیره وتاربك‌باشد ۴- و ریزه
ربزه وذره ره را یز گونند .
تار ومار- با میم بروزن کار وبلر .
این لفت از انماع است بمعنی پراگنده و از هم
پاشیده وزیر و زس شده و سیار پرشانباشد -
وناچیز وابود گردیده را لژ گویند .
اه - .بر وزن پاره ؛ بممنی تار مو
وتار رسمان و تارچنگلموطنبور واتارآن باشد ۳
رتارك سر وفرق سررا یز کوبند ۴" وبمعنی‌تیره
وتارك هم هست؟ - و زيانة کپانرا نیز کفتهاند
و کیان ترازو ماشدی است که بدان بار سنجند »
ات بجای حرف اول نون هم آهده است
وافه‌اعلم ۴ - و تار جولاهگان باشد که نقیض یود
است- وطارم را نیز گوبند وآن خاندای باشد که
مانند خر اه از چوب سازند - و بمعنی تذار سم
کنته‌اند و آن ظرفی‌باشد معروف .
قادی ه بر وزن جاری » آبی با دکه
از درخت ار حاصل شود ومانند شراب‌شاه دهد
و نی تبره وتاربك‌هم کنتداند. *
. سح «نارد» (ه .م): ؟۴ . رك :تار. ۴ ره : ترگ‎ ٩
۴ ممحف «نلرم» (ه .م).
۵ تار یلگ - از: تار - ميك (نسبت). پهلوی 68۳/6 ازتار. دراوستا 4۵۸۵ «بارتولمه
۰ دب رکه 4۲۲۳ «اسشق ۰۳۷۰ سنگسری ٩۵۲1‏ , سرخة ۷۵۲16 , شهمیرزادی ها
« . اس 6۱۹۵ »اشکاشمی 4871620 (پیش ازطلوع فجر) «کربرسن ۹۸ + کیلکیطآتها ؛
یره. نار. ظلمانی . کدر .
» تاریکی - از: تاريك ۳- ی (مصدری) »بهلوی 12246410 عمسینا ۱4٩‏ :۶ کیلکی
لته .فریز دی ونطنزی اعاکقا »یربی تطتها دك . ص۸۵ > کورانی ]ها « گورالی
۰ ظلمت. تیرکی» سیاهی :
ز کار ست. یندش و دل شکته حدار که‌آي چشمه حبوان درون و ازنگی اننعن
«کلتان ۳۷ >.
شمه از صفسهٌ 4۵1
ید ۱۳ ۱ ۳9 قیاق
د منوچهری داهفانی۷۹ *.
۴ بفتح راه , کوره‌است وسیم در جبال بين زوین و کیلان و در آن قریه‌های بیار
وکوههای مخت است و شهری مشپور ندارد. رك : جفرافبای سیا
====== idx 684
#رین
تادلی » بر وزن پارین ؛ بمعنی نیره
وثار يك باشد سوتاری را نیز گونند که‌آب درخت
تار است .
اوه بسکون زای هوز,ممشوق ومحبوب‌را
کویندا - و یمعنی تازنده نیز آمده است ؟ -
وامر بتاختن هم هست بمنی بتاز؟ <- و بععنی
قرومابه هم گفته‌اند که بعربی سفاهخوانتدسویس
امرد ومترش ضخیم را گویند که پیوسته بافاسقان
صحیت دارد۱ ۲ تازبرا هم میگویند.
2 - بسکون‌زای‌فارسی» خانةٌ کرباسی‌را
کوبند کهخیمه باشد؟ - و بمعنی لطیف و نازكه
همآمده‌است ۳
تازر اه ۵ مخنف تازبانه است کهفمجی
باشد .
تاز از" » با بای ابجد ب‌وزن‌کارساز,
تب وی 6 سس
مغلم(۱)وغلام باره را کویند.
از د ۵
دس ه بر وزن بالش, بمعنی قطره
زدن - وناخئن وتك ویوی کردن‌باشد۷ .
از لك ح بکر تاك بروزن سالك .
بمعنی پیل پایه‌است؛ وآن ستونی‌باشد که از کچ
وسنکه سازند وبربالای آن بابهای طاق گذارند,
قاذه ه بفتح اكك . بمعنی نو باشد که
قض کپنه است4 - و بمعنی حادث هم آهده
است که در مقابل قدم است*۷- و ضد بژمرده
هم‌هست . ۱
تادری ع بر وژن بازی » بمعنی عربی ٩۱‏
۴ مخفف ازنده . رک : ناختن .
۴ خسرو غازی آهنکگ بشارا دارد
دلم ز له صابوته وزهره ناز.
دقریم . لفت فرس ۵۶5
3 : ناختن. ۱
زده از غزنین نا جیحون تا وخر کاه.
دبهرامی. بنقل لغت‌فری *۱۹*.
بزد برسر مرد تازانه چند
فکادن همی خواست سم سمند .
اسدی طوسی . رك : تازبانه .
۷ - بهاوی 12615100 «اسشق ۳۹۸ از:
٩‏ - از ريشة تاختن .بلوچی 2[81)
1 تاژيك » مب‌گفتند ۰ و میس این اطلاق را بهمةٌ عرب تعمیم دادند , چنانکه بونانیان و رومیان
2 (پاری) وعرب فری رابهمة ایرانیان اطلاق کردند وابرانیان «بونانگرا- بنام فبیلهٌ «بون»
دراسیای صفیر- بهمةٌ فوم هلاس اطلاق کردند .
====== idx 685
- هی ع <
باشد چه اززبان نازی زبان عربی وازاسب تلزی
اسب عر هی مراد است ۷ ‌- ویسسنی تاضت آری هم
نت۴ - ونوعی‌ازسگه شکاری باشد .
تاخته ودوان دوان - و قصد کنان باشد - وجمع
تازی هم‌هست که عر بان‌باشد .۶
است که غیر عرب وترك باشد۴ - وفرزند عرب
در عجم زاییده شده و بر‌آهده را نب گوند.
تاس » بر وزن دای » بمعنی تلواسه
و انطراب و بی طافتی - ومیل بچیزها باشد »
و زنان آبستن را این‌حال بیشتر دست دهد .
باشد؟ .3
(۱) چش: ۲- در .
۷ .2 اسب تازی ۳ ضصف بود
ای کشته سوار جلد برتازی
تازیت ز بهر علم و دین باشد
کرتلزی و علم‌را بدست آری
ش‌ علم بدست اند از تازی
۴ رک : تازی وتاجيكث.
عمرب آن طسمه «نفس>.
تاسه
تاسمصت؟ - یکرسن و سکون میم ۳
وقتح صاد بی نقطه و فوفانی ساکن . بلفت اهل
بربر ترنج باشد که پوست آنرامربا سازند .
تاسهه ‏ بسکون تاك وفتح میم »
چرم‌خام و دوال چرمی را کوبشد ۷ - وموی‌تانه
کرده دا نیز کفته اند که بر فراژ پیشانی
باشد ۷ -
تاسه - بر وزن کاسه ۰ بمعنی اندوه
و ملالت باشد - ویمشی اضطراب
وبیقراری هم هست۸ - و تیره شدن روی را که
ازغم و الم بهم رسیده باشد - وفشارش و فشردن
کلو بمب سیری با ملال و اندوه دیگر ٩‏ -
ومیل بخوردنی وخواهش بچيزي را گوشد. واین
حالت مثثو(۱) زنان آمستن و مردان ثرباکی‌را
همسنان ازطویله‌ای خر به. « گلستان ۱۵ *.
خر پیش سوار علم چون تازی. ؟
بی علم یکی است تازی ورازی
شاید که بهر دو سر بیفرازی
جز چاکری وفوی وطتازی
« دبوان ناصرخروه 4۷ ».
س ۱۳۹ کرد : تاسممت «لك ]:
۱ - ازثر کی ناسمه»
۸ کردی252) (اتظار
مستصصی
از مانه
6 - توبامن نسازی که ازصحبت من
۵ تاریانه - زباکی 8212408 ؛
و وزن آن از ۱۲ کیلوگرم تجاوز مبکند .
جع00 6096۲و۸ ( فراسه
۳۷) «در بای‌خزر. بریمالی.ص۱۲۸؟.
۳۳
ناس صاهی
```


## [2026-09-14T02:33:11.268Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[684][1700:])\nEOF"
}
```


### [2026-09-14T02:33:12.365Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:33:26.223Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:33:26.228Z] TOOL RESULT

```


```


## [2026-09-14T02:33:29.995Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AC",
 "prompt": "Give the full Persian and Arabic etymology sections for تاج (tāj 'crown'): what is it derived from (Middle Persian tāg? Aramaic/Syriac tāgā? PIE root?), and any cognates listed."
}
```


## [2026-09-14T02:33:32.223Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AC%DB%8C%DA%A9",
 "prompt": "Give the full etymology of Persian تاجیک (Tājik) and, if mentioned, تازی (tāzi). What origin is given (Middle Persian tāzīg, Arabic Ṭayyiʔ, Turkic tāt)?"
}
```


### [2026-09-14T02:33:37.524Z] TOOL RESULT

```
# Etymology of تاج (tāj)

## Arabic Etymology

The Arabic entry states the word was "Borrowed from Parthian *𐫤𐫀𐫃 (tāg), attested in 𐫟𐫀𐫡𐫤𐫀𐫃 (xʾrtʾg /xārtāg/, 'crown of thorns')." It's also described as "Related to Arabic تَخْت (taḵt, 'bed, couch...'), also an Iranian borrowing; and to Aramaic תָּגָא (tāḡā)."

## Persian Etymology

The Persian section indicates the term was "Borrowed from Arabic تَاج (tāj), from Parthian *𐫤𐫀𐫃 (*tʾg /tāg/, 'crown'), attested in 𐫟𐫀𐫡𐫤𐫀𐫃 (xʾrtʾg /xārtāg/, 'crown of thorns')."

It notes the word is "Related to Persian تخت (taxt, 'bed, throne'), and akin to Old Armenian թագ (tʻag), Arabic تاج (tāj), and Aramaic תָּגָא (tāḡā), Iranian borrowings."

## Key Points

Both etymologies trace the word through **Parthian** as the ultimate source, rather than directly to Middle Persian, Aramaic, or Proto-Indo-European roots. The categories list "Persian terms derived from Proto-Indo-European," but no specific PIE root appears in the etymology sections themselves.
```


### [2026-09-14T02:33:38.252Z] TOOL RESULT

```
# Etymology of Persian تاجیک (Tājik)

## Origin Chain

The word traces through multiple languages:

**Arabic → Middle Persian → Persian**

According to the source, it derives from Arabic _طَيِّء_ (ṭayyiʔ), which passed through Middle Persian _tʾcyk'_ before arriving at modern Persian _تاجیک_.

## Alternative Theory

The entry notes: "Possibly related to _تازیک_ (tâzik), a re-borrowing from Old Turkic." Scholar W. Henning proposed the form originated as _*Tāt-čīk_, earlier _*Tād-čīk_.

## Folk Etymology

A popular but unverified explanation connects it to Tajik _тоҷ_ (toj, "crown") and Persian _تاج_ (tâj, "crown").

**Note:** The document does not mention "تازی (tāzi)" specifically. It does reference _تازیک_ (tâzik) as a related term and potential re-borrowing from Turkic sources.
```


## [2026-09-14T02:33:45.368Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-",
 "prompt": "What is the reconstructed root, its meaning, and the descendants listed (Germanic, Latin, Celtic, Greek, Indo-Iranian)? Is any Iranian/Persian word (tāg, tāj) listed?"
}
```


## [2026-09-14T02:33:46.288Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tiara",
 "prompt": "Give the full etymology of tiara, and any statement about its Persian/Oriental origin."
}
```


### [2026-09-14T02:33:50.451Z] TOOL RESULT

```
# Etymology of Tiara

## Full Etymology

The word "tiara" entered English in the 1550s, deriving from Latin *tiara*, which came from Greek *tiara*—a term of Oriental origin. An earlier Englished form, *tiar*, appeared in the 1510s. Originally, it denoted "turban-like head-dress of the Persian kings" and was worn by men of rank. By the 1650s, the meaning shifted to describe "a richly jeweled headband in Western wear."

## Persian/Oriental Origin Statement

According to the source: "from Latin *tiara*, from Greek *tiara*, a word of Oriental origin." The document specifies that the garment was historically associated with Persian royalty and nobility, though the ultimate Oriental source language is not identified with precision in this entry.
```


### [2026-09-14T02:33:51.963Z] TOOL RESULT

```
# Proto-Indo-European *(s)teg- Root Analysis

## Reconstructed Root and Meaning

The root ***(s)teg-*** has two meanings:

1. **"to cover"** (imperfective verb)
2. **"pole, stick, beam"** (possibly a specialization of the first meaning)

## Major Descendants by Language Family

**Germanic:** Proto-Germanic *þaką, *þakjaną (roof-related terms)

**Latin:** *tegō, *tēgula, *tegmen, *tignum, *tugurium

**Celtic:** *tegos, *togos (roof), Old Irish *tí

**Greek:** Ancient Greek *στέγω* (stégō), *στέγος* (stégos)

**Indo-Iranian:** Sanskrit *sthagayati (possibly unrelated per sources)

## Persian/Iranian Terms

Yes, Persian/Iranian words appear in the "Unsorted formations" section:

- **Middle Persian:** *tāg* (from Proto-Iranian *tāgah, meaning "arch, vault")
- **Persian:** *طاق* (tāq) - derived from Middle Persian
- **Arabic:** *طَاق* (ṭāq) - borrowed from Middle Iranian

These represent later developments rather than direct Proto-Indo-European descendants.
```


## [2026-09-14T02:34:00.140Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/attire",
 "prompt": "Full etymology of attire, and of the noun \"tire\" (headdress / band of a wheel). Is any connection with Greek tiara mentioned?"
}
```


## [2026-09-14T02:34:01.153Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/shanty",
 "prompt": "Full etymology of shanty (cabin). Does it mention Irish sean tig 'old house' and Canadian French chantier? Which is preferred?"
}
```


### [2026-09-14T02:34:04.798Z] TOOL RESULT

```
# Etymology of Shanty (Cabin)

Based on the provided content, the etymology traces only **one origin**: Canadian French *chantier*.

The source states: "said to be from Canadian French *chantier* 'lumberjack's headquarters,' in French, 'timber-yard, dock,' from Old French *chantier* 'gantry,' from Latin *cantherius* 'rafter, frame.'"

**The Irish origin (sean tig) is not mentioned** in this document. Therefore, I cannot compare which etymology is preferred based solely on the content provided—only the Canadian French derivation is discussed here.
```


### [2026-09-14T02:34:05.090Z] TOOL RESULT

```
# Etymology of Attire and Tire

Based on the etymonline entry provided, **no connection with Greek tiara is mentioned**.

The etymology traces "attire" to Old French *atirer* ("to equip, ready, prepare"), which combines *a-* (from Latin *ad-*, meaning "to") and *tire* ("order, row, dress"). The entry notes that "tire" (as a noun referring to headdress or wheel rim) derives from "attire" as a shortened form, originally meaning *"equipment, dress, covering, trappings or accoutrements of a knight"* (c. 1300).

The detailed entry states: *"probably from an extended use of tire 'equipment, dress, covering, trappings or accoutrements of a knight' (c. 1300, tir), a shortened form of attire (n.)."*

The source material focuses exclusively on Old French and Latin etymologies, with no reference to Greek origins or the word "tiara."
```


## [2026-09-14T02:34:11.573Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tungsten",
 "prompt": "Full etymology of tungsten: the Swedish source, date, and who named it."
}
```


## [2026-09-14T02:34:13.856Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%8E%A0%F0%90%8E%A2%F0%90%8E%B2%F0%90%8E%A0%F0%90%8E%BC%F0%90%8E%A0",
 "prompt": "Is this the Old Persian word tačara 'palace'? Give its etymology and descendants (New Persian tajar/tazar, Armenian tačar)."
}
```


### [2026-09-14T02:34:15.230Z] TOOL RESULT

```
# Etymology of Tungsten

**Source and Date:**
The term "tungsten" entered English in 1796, originating from Swedish.

**Naming and Discoverer:**
Swedish chemist Karl Wilhelm Scheele (1742-1786) coined the Swedish term *tungsten* in 1780 to describe calcium tungstate, which he discovered.

**Meaning:**
The name combines two Swedish elements: *tung* meaning "heavy" and *sten* meaning "stone." This literally translates to "heavy stone," reflecting the mineral's notable density.

**Atomic Symbol:**
The chemical symbol W derives from the Latin *wolframium*, connected to the German *Wolfram*, referring to iron tungstate—a related mineral compound.
```


### [2026-09-14T02:34:15.380Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:34:17.587Z] TOOL CALL #45: WebSearch

```json
{
 "query": "Old Persian tacara palace etymology Armenian tačar Persian tazar"
}
```


### [2026-09-14T02:34:25.048Z] TOOL RESULT

```
Web search results for query: "Old Persian tacara palace etymology Armenian tačar Persian tazar"

Links: [{"title":"(PDF) On Old Persian tačara- and its Elusive Meaning","url":"https://www.academia.edu/72294857/On_Old_Persian_ta%C4%8Dara_and_its_Elusive_Meaning"},{"title":"տաճար - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D5%BF%D5%A1%D5%B3%D5%A1%D6%80"},{"title":"Persepolis - Wikipedia","url":"https://en.wikipedia.org/wiki/Persepolis"},{"title":"Ruins of the Tachara, the Palace of Darius the Great. Persepolis, Fars Province, Iran Stock Photo - Alamy","url":"https://www.alamy.com/ruins-of-the-tachara-the-palace-of-darius-the-great-persepolis-fars-province-iran-image431048069.html"},{"title":"The Tachara (Winter Palace) of Persepolis – Dr. Kaveh Farrokh","url":"https://www.kavehfarrokh.com/ancient-prehistory-651-a-d/achaemenids/the-tachara-winter-palace-of-persepolis/"},{"title":"տաճար : meaning, etymology, pronunciation, synonyms - iDictio","url":"https://idictio.it/l.php?name=%D5%BF%D5%A1%D5%B3%D5%A1%D6%80"},{"title":"Tachara","url":"https://en.wikipedia.org/wiki/Tachara"},{"title":"Apadana","url":"https://en.wikipedia.org/wiki/Apadana"},{"title":"تجر | Definition of تجر at Definify","url":"https://www.definify.com/word/%D8%AA%D8%AC%D8%B1"},{"title":"Pana-Khan Palace","url":"https://en.wikipedia.org/wiki/Pana-Khan_Palace"}]

Based on the search results, here's what I found about the etymology of these terms:

## Etymology Connection

The Armenian word tačar is an Iranian borrowing that compares to Old Persian tačara- (meaning "palace"), Manichaean Parthian tažar ("palace, dwelling"), and Persian tajar ("winter house; storehouse").

## Old Persian tačara-

Old Persian tačara- connects to various meanings, including 'winter house' in Modern Persian, and scholars have proposed interpretations including 'palace', 'winter house', and 'temple'. In Achaemenid Babylonian, tačara- is represented as a logogram for 'house', while Armenian references point to meanings such as 'temple' or 'banqueting hall'.

## The Tachara at Persepolis

The Tachara was the exclusive palace of Darius the Great at Persepolis, completed after his death in 486 BC by his son Xerxes, who called it a Taçara, meaning "winter palace" in Old Persian.

## Armenian tačar

In Armenian, tačar means palace, court, and also temple, church, banqueting-hall, and hospital.

The terms across Old Persian, Armenian, Middle Iranian, and Modern Persian all derive from the same root and share the basic semantic field of palatial/architectural structures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:34:35.511Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%BF%D5%A1%D5%B3%D5%A1%D6%80",
 "prompt": "Give the full etymology of Armenian տաճար (tačar): which Iranian forms are cited (Old Persian tačara, Parthian tažar, Persian tajar/tazar), and any proposed Iranian/PIE root."
}
```


## [2026-09-14T02:34:38.819Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if \"taj,  ‘crown’\" in p or \"taj, ‘crown’\" in p: print('taj leaf',i)\n    if 'tiara,  n.,  head  dress' in p or 'tiara, n., head dress' in p: print('tiara leaf',i)\n    if 'stone,  n.' in p or 'stone, n.' in p: print('stone leaf',i)\n    if 'stiff,  adj' in p: print('stiff leaf',i)\nEOF"
}
```


### [2026-09-14T02:34:40.309Z] TOOL RESULT

```
# Etymology of Armenian տաճար (tačar)

Based on the Wiktionary entry, here's the etymology:

**Iranian Origin:** The word derives from Iranian languages. The entry cites three comparative forms:

1. **Old Persian:** "𐎫𐎨𐎼 (t-c-r /⁠tačara-⁠/, 'palace')"

2. **Parthian:** "𐫎𐫝𐫡 (ṯcr /⁠*tažar⁠/, 'palace, dwelling')"

3. **Persian:** "تجر (tajar, 'winter house; storehouse')"

**Root:** The entry notes that Persian contains "more" etymological information but doesn't specify a reconstructed Proto-Indo-European root in this article. The semantic field centers on palatial and residential structures across these Iranian languages, suggesting a shared lexical root among Iranian languages rather than detailed PIE reconstruction here.
```


### [2026-09-14T02:34:41.576Z] TOOL RESULT

```
leaves 903
stone leaf 116
stone leaf 194
stone leaf 213
stone leaf 315
stone leaf 375
stone leaf 395
stone leaf 484
stone leaf 485
stone leaf 635
stone leaf 715
taj leaf 801
stiff leaf 803
stone leaf 806
taj leaf 830
tiara leaf 856
```


## [2026-09-14T02:34:46.414Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T02:34:47.731Z] TOOL RESULT

```
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
```


## [2026-09-14T02:34:56.567Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in [766,767,768,830,856]:\n    print('=== leaf',i,'===')\n    print(pages[i][:400].replace('\\n',' '))\n    print()\nEOF"
}
```


### [2026-09-14T02:34:58.070Z] TOOL RESULT

```
=== leaf 766 ===
.  -crximov,  fr.  oxo7reiv,  ‘to  look  at,  ex¬ amine’.  See  -scope. siderosis,  n.,  1)  deposit  of  iron  in  a  tissue  of  the body,  esp.  in  the  lungs;  2)  inhalation  of  iron dust  (med.)  —  Medical  L.,  formed  fr.  Gk. <jl8r)po?,  ‘iron’.  See  1st  sidero-  and  -osis. sideward,  adj.  —  Compounded  of  side  and  adj. suff.  -ward. sideward,  sidewards,  adv.  —  Compounded  

=== leaf 767 ===
g  to,  or  con¬ taining,  silica.  —  See  silica  and  -ous. silicic,  adj.,  derived  from,  or  pertaining  to,  silica. —  See  silica  and  adj.  suff.  -ic. siliciferous,  adj.,  containing  silica.  —  See  silica and  -ferous. silicify,  tr.  v.,  to  convert  into  silica;  intr.  v.,  to  be converted  into  silica.  —  See  silica  and  -fy. silico-,  before  a  vowel  silic-,  combini

=== leaf 768 ===
 Pure  is  dealt  with  as  an  impostor  and  is  believed only  after  he  has  proved  his  identity, simoniac,  n.,  one  who  practises  simony;  adj.,  per¬ taining  to  simony.  —  ML.  simoniacus,  fr.  simo- nia.  See  simony. Derivatives:  simoniae-al,  adj.,  simoniac-al-ly, adv. simony,  n.,  the  buying  or  selling  of  sacred  things. —  F.  simonie,  fr.  ML.  simonia,  fr.  Simon 

=== leaf 830 ===
e  rail  across  the  stern of  a  ship.  —  Du.  tafereel,  dimin.  of  tafel,  ‘table’, which,  together  with  OHG.  zabal  (MHG. zabel),  ‘board,  plank’,  OHG.  tavala,  tabala (MHG.  tavele,  G.  Tafel),  ‘table,  board’,  is  bor¬ rowed  fr.  L.  tabula,  ‘board,  plank’;  see  table. The  form  taffrail  arose  through  the  assimilation of  the  ending  of  tafferel  to  E.  rail. taffy, 

=== leaf 856 ===
and cp.  words  there  referred  to. Thysanoptera,  n.  pi.,  an  order  of  insects,  the  thrips (entomol.)  —  ModL.,  compounded  of  Gk.  &'i- aoevot;,  ‘tassel’,  and  7TTEpov,  ‘wing'.  See  prec. word  and  ptero-. Thysanura,  n.  pi.,  an  order  of  insects,  the  bristle- tail  (entomol.)  —  ModL.,  compounded  of  Gk. fhicravoi;,  ‘tassel’,  and  oupa,  ‘tail’.  See  thysano- and  uro
```


## [2026-09-14T02:35:14.603Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(760,880):\n    p=pages[i]\n    nums=re.findall(r'^\\s*(1[0-9]{3})\\s*$', p, re.M)\n    if nums: print(i, nums, p.strip()[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:35:15.832Z] TOOL RESULT

```
764 ['1439', '1440', '1441'] shout-er,  n.,  shout-ing,  n. shove,  tr.  and  intr.  v.  
765 ['1442'] er,  tr.  v.,  shutt-er- less,  adj.,  shutt-ing,  n. shuttl
766 ['1443', '1445'] .  -crximov,  fr.  oxo7reiv,  ‘to  look  at,  ex¬ amine’.  S
767 ['1444', '1446'] g  to,  or  con¬ taining,  silica.  —  See  silica  and  -ou
768 ['1448'] Pure  is  dealt  with  as  an  impostor  and  is  believed o
769 ['1449', '1450', '1451'] ,  pertaining  to Ceylon;  n.,  a  native  of  Ceylon.  —  F
771 ['1452', '1453'] nding  to  Goth,  sik,  OHG.  sih,  MHG.,  G. sich,  ‘himsel
772 ['1454', '1455', '1456'] of  a  team  or  side.  —  Shortened fr.  skipper,  ‘captain
777 ['1465'] e  *snab-,  ‘beak;  to  snatch  with  the  beak,  to snap’, 
778 ['1466', '1467'] v. snorkel,  n.,  a  device  for  submarines.  —  G. Schnorc
779 ['1469'] sociology,  n.  —  F.  sociologie,  a  hybrid  coined  by th
780 ['1470', '1471'] ),  a derivative  of  sol,  ‘sun’.  See  Sol,  ‘sun’. Solanu
781 ['1473'] 2)  single;  3)  lonely.  — ME.,  fr.  L.  solitarius,  ‘alo
783 ['1477'] nt.  Cp.  absorbefacient. Derivative:  sorbefacient,  n. sor
784 ['1479'] satdm,  Gk.  c-xa- t6v,  L.  centum,  OE.  hand,  etc.,  of 
786 ['1483'] lustrous  mineral.  —  LG. spar,  ‘gypsum’,  fr.  MLG.,  rel
787 ['1485'] ,  n.  pi.,  a  long  gaiter.  —  Compound¬ ed  of  spatter 
790 ['1491'] ument  for  meas¬ uring  blood  pressure  in  the  arteries.
791 ['1492'] (naut.)  — Formed  fr.  spinx,  misreading  of  Sphinx,  the
794 ['1499'] a  with  the  dimin.  suff.  -ala. See  spore  and  -ule. sp
796 ['1501'] quander,  tr.  v.  —  Of  uncertain  origin. Derivatives:  s
797 ['1503'] ��,  and  houder,  ‘holder’;  in¬ fluenced  in  form  by  E.
798 ['1505'] Formed  with adj.  suff.  -ate  fr.  L.  stamen,  gen.  stam
799 ['1507'] ��starboard’,  are  Teut.  loan  words.  See  steer,  ‘to di
802 ['1513'] afette,  etape,  staff,  stamp,  stampede, staple,  ‘bar,  w
803 ['1514', '1515'] there  referred,  to. sternutation,  n.,  sneeze,  sneezing.
811 ['1529', '1531'] n. Derivatives:  studi-ed,  adj.,  studi-ed-ly,  adv. stuff,
813 ['1533'] e  understanding  of  something not  expressed  in  words.  
814 ['1534'] L.  sub,  ‘under’,  and  Gk. 9pf)v,  ‘diaphragm;  mind’.  Se
815 ['1537'] for *sub-texlis,  fr.  sub-  and  tela  (for  *texla),  ‘a  
817 ['1541'] l- Idtus,  suggilldtus,  pp.  of  sugiilare,  suggilldre, wh
818 ['1543'] ,  OE.  seam,  ‘burden,  load  of  a beast  of  burden’.  Cp
819 ['1544', '1545'] ,  surface.  —  L.  superficies,  ‘top,  sur¬ face’,  fr.  s
820 ['1340'] plier,  ‘to  beseech,  en¬ treat’  (fr.  L.  supplicdre;  se
821 ['1548', '1549'] intr.  v.  —  ME.  surmisen,  fr.  MF. surmis,  surmise,  ma
822 ['1510', '1551'] r, sustenance,  n.  —  ME.,  fr.  OF.  sustenance,  souste- 
823 ['1552', '1553'] , orig.  ‘of  the  color  of  dirt',  fr.  I.-E.  base  *  s
824 ['1554', '1555'] waste  away,  lan¬ guish,  disappear’,  whicn  is  rel.  to 
825 ['1556'] s  there  referred to.  Cp.  also  monosyllable,  dissyllabl
829 ['1565'] ntablature, entablement,  taffrail.  Cp.  also  the  first  
830 ['1566'] e  rail  across  the  stern of  a  ship.  —  Du.  tafereel, 
831 ['1568', '1569'] ve,  adj.  —  A  hybrid  coined  fr.  talk  and -ative,  a  
833 ['1572'] cp.  the  first  element  in tandem.  Cp.  also  taunt.  Cp.
835 ['1577'] p,  saucer’.  Cp.  OProveng.  tassa, It.  tazza,  Sp.  taza,
836 ['1578', '1579'] .  —  ME.  taxacioun,  fr.  MF.  (=  F.) taxation,  fr.  L. 
837 ['1580'] .,  an  adherent  of  technocracy.  — Compounded  of  techno
838 ['1583'] tnjXut, of  s.m.,  Gk.  T7]X6flt,  of  s.m.,  xi)X6(1e(v),  
839 ['1584', '1003'] contare,  Sp.  contar,  ‘to  count,  to  recount, narrate’, 
845 ['1596', '1597'] ith  Goth,  hairnet,  ‘skull’,  OE.  hwer,  ‘kettle’  (see c
846 ['1598', '1599'] f  a  province)’, fr.  xsxpa-  (sec  tetra-)  and  -rx?y_r,c
847 ['1600', '1601'] in  its  spectrum. See  Thalia,  ‘the  Muse  of  comedy’. De
848 ['1602', '1603'] er  (masc.), diu  (fem.),  da j  (neut.),  G.  der  (masc.),
849 ['1604', '1606'] ic,  adj.,  considering  God  as  the  center of  all  thing
852 ['1608', '1609'] ,  ‘incense’,  9uo<;,  ‘burned  sac¬ rifice’  (whence  L.  t
862 ['1626'] cut,  a  piece  cut  off, section,  part  of  a  book,  volu
863 ['1629'] to  blow  a  horn.  —  Of  imitative  ori¬ gin;  cp.  Du.  t
864 ['1630'] relief,  chased’,  verbal  adj.  of  xopsii- siv,  ‘to  work
865 ['1632', '1633'] fr.  OProven?.  tartuga,  fr.  It.  tartaruga, which  derive
866 ['1634', '1635'] tornare,  ‘to  turn  in  a  lathe;  to  turn,  fashion’.  Se
867 ['1636', '1637'] Compounded  of  trachelo-  and  Gk. -xopia,  ‘a  cutting  of
869 ['1641'] L.  transfor- matus,  pp.  of  transformdre.  See  prec.  wo
870 ['1642', '1643'] ,  v.,  and  -ation  and cp.  L.  transportatio,  gen.  -dni
871 ['1644', '1043'] t.,  lit. ‘the  woman  led  astray’,  pp.  of  traviare,  ‘t
872 ['1040', '1647'] ,  Tremandra,  Tremella,  tremulous,  tro¬ mometer.  Cp.  al
878 ['1657'] T),  ‘tongue  of  the  balance,  balance  ,  orig. ‘the  hol
```


## [2026-09-14T02:35:26.766Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(799,808):\n    p=pages[i]\n    print('=== leaf',i,'nums',re.findall(r'^\\s*(1[0-9]{3})\\s*$',p,re.M))\n    for kw in ['stego','steg-','tiara','taj','stone','stiff','Avestic','Avestan']:\n        for m in re.finditer(kw,p):\n            print('   ',kw,'->',p[max(0,m.start()-300):m.start()+300].replace('\\n',' '))\n            break\nEOF"
}
```


### [2026-09-14T02:35:27.891Z] TOOL RESULT

```
=== leaf 799 nums ['1507']
    stiff -> ��starboard’,  are  Teut.  loan  words.  See  steer,  ‘to direct’,  and  board. starch,  n.  —  ME.  sterche,  starche,  back  forma¬ tion  fr.  sterchen,  ‘to  starch’,  fr.  OE.  stercan,  ‘to stiffen’,  fr.  stearc,  ‘stiff’.  Cp.  G.  Starke,  ‘strength ; starch’,  and  see  stark. Derivatives:  starch,  adj.  and  tr.  v.,  starch-ed, adj.,  starch-ed-ly,  adv.,  starch-ed-ness,  n.,  starch- y,  adj.,  starch-i-ly,  adv.,  starch-i-ness,  n. stare,  intr.  and  tr.  v.  —  ME.  staren
    Avestic ->   stem  of  stare,  ‘to stand’,  which  is  rel.  to  sistere,  ‘to  place,  stand, stand  still’,  fr.  I.-E.  base  *st(h)a-,  ‘to  stand’, whence  also  OI.  tisfhati,  ‘stands’,  dstham,  ‘I stood’,  stitdh,  ‘standing’,  sthatar-,  ‘ruler,  guide’, sthatf,  ‘that  which  stands’,  OPers.  and  Avestic sta-,  ‘to  stand’,  Avestic  hishtaiti,  ‘stands’,  Toch. shtam,  ‘I  stand’,  Gk.  I'a-rqut  (for  ),  ‘I cause  to  stand,  I  set,  place;  I  stand’,  laxrjxa,  ‘I stand’,  axdaip,  ‘a  standing’,  OSlav.  stanjq,  stati, ‘to  place  oneself’,  stojQ,  stojati,  ‘to  stand’,  Lith. stdj
=== leaf 800 nums []
    stone -> tanchier,  ‘to  check  the flow’.  See  stanch,  v. stauro-,  before  a  vowel  staur-,  combining  form meaning  ‘cross’.  —  Gk.  oxaupo-,  axaup-,  fr. axaupd?,  ‘stock,  pile,  cross’.  See  steer,  ‘to  direct’, and  cp.  words  there  referred  to. stauroiite,  n.  (mineral.)  —  Lit.  ‘cross-stone’,  fr. Gk.  oxaup6?,  ‘cross’,  and  Xtftoc.  ‘stone’.  See stauro-  and  -lite. Derivative:  staurolit-ic. ,  adj. stauroscope,  n.,  an  instrument  for  determining the  position  of  the  planes  of  vibrations  in  crys¬ tals.  —  Compounded  of  stauro-  and  Gk.  -0x6- 7tiov,  fr.  GY.o
    Avestic ->  stehli,  ON.,  MLG.  stal,  Dan.  staal,  Swed. stal ,  MDu.  stael,  Du.  staal,  OHG.  stahal,  MHG. stahel,  stal,  G.  Stahl,  ‘steel’,  and  cogn.  with OPruss.  stakla,  ‘steel’.  These  words  prob.  meant orig.  ‘something  firm  or  hard’,  and  are  cogn. with  OI.  stakati,  ‘resists’,  Avestic  staxta-,  ‘firm, solid’,  staxra-,  ’severe’  (said  of  the  cold  in  win¬ ter).  All  these  words  are  prob.  traceable  ult.  to I.-E.  base  *sta-,  ‘to  stand’.  See  state. Derivatives:  steel,  adj.  and  tr.  v.,  steel-y,  adj., steel-i-ness,  n. steelyard,  n.,  a  kind  of  ba
=== leaf 801 nums []
    stego -> re,  Sp.  estibar.  Port,  estivar,  ‘to compress,  stow’),  fr.  I.-E.  base  *stei-,  *sti-,  ‘to stiffen,  be  compressed’.  See  stone  and  cp.  words there  referred  to.  Cp.  also  the  first  element  in stevedore. Derivative:  steeve,  n.,  spar  used  in  stowing cargo. steg-,  form  of  stego-  before  a  vowel. stegano-,  combining  form  meaning  ‘covered’,  as in  steganography.  —  Gk.  axEyavo-,  fr.  axEya- v6?,  ‘covered’,  fr.  ax^yEiv,  ‘to  cover’.  See  stego-. steganography,  n.,  the  same  as  cryptography.  — Formed  fr.  stegano-  and  Gk.  -ypoctpLa,  fr.  ypa- 9Ei
    steg- -> e also  It.  stivare,  Sp.  estibar.  Port,  estivar,  ‘to compress,  stow’),  fr.  I.-E.  base  *stei-,  *sti-,  ‘to stiffen,  be  compressed’.  See  stone  and  cp.  words there  referred  to.  Cp.  also  the  first  element  in stevedore. Derivative:  steeve,  n.,  spar  used  in  stowing cargo. steg-,  form  of  stego-  before  a  vowel. stegano-,  combining  form  meaning  ‘covered’,  as in  steganography.  —  Gk.  axEyavo-,  fr.  axEya- v6?,  ‘covered’,  fr.  ax^yEiv,  ‘to  cover’.  See  stego-. steganography,  n.,  the  same  as  cryptography.  — Formed  fr.  stegano-  and  Gk.  -ypoctp
    taj -> ormed  fr.  stem,  n., with  the  dimin,  suff.  -let. stemma,  n.,  pedigree.  —  L.,  ‘garland;  pedigree’, fr.  Gk.  aT£(ifia,  ‘garland,  wreath’,  from  the stem  of  cxeqmv,  ‘to  surround,  encircle,  wreathe, crown’,  fr.  I.-E.  base  *stegwh-,  ‘to  encircle, crown’,  whence  also  Pers.  taj,  ‘crown’.  Cp.  ste- phano-  and  the  second  element  in  Agrostemma. Cp.  also  taj.  For  the  ending  see  suff.  -ma. Stemona,  n.,  a  genus  of  plants  (hot.)  —  ModL., fr.  Gk.  crTTKitiiv,  ‘warp’.  See  stamen, stemple,  stempel,  n.,  cross  timber.  —  G.  Stempel, ‘stamp,  die, 
    stone -> the  horizon,  sleev¬ ing,  n. steeve,  tr.  v.,  to  stow.  —  ME.  steven,  fr.  MF.  (  = F.)  estiver,  fr.  L.  stipare,  ‘to  compress’  (whence also  It.  stivare,  Sp.  estibar.  Port,  estivar,  ‘to compress,  stow’),  fr.  I.-E.  base  *stei-,  *sti-,  ‘to stiffen,  be  compressed’.  See  stone  and  cp.  words there  referred  to.  Cp.  also  the  first  element  in stevedore. Derivative:  steeve,  n.,  spar  used  in  stowing cargo. steg-,  form  of  stego-  before  a  vowel. stegano-,  combining  form  meaning  ‘covered’,  as in  steganography.  —  Gk.  axEyavo-,  fr.  axEya- v6?,
    stiff -> lid’,  sthavirah,  ‘broad,  thick’,  stiirdh,  ‘strong’. Arm.  st var,  ‘thick’,  L.  -staurare  in  in-staurdre, ‘to  renew,  repair,  restore’,  re-staurdre,  ‘to  re¬ pair,  restore’.  All  these  words  prob.  derive  fr. I.-E.  *st(h)eu-ro-,  *st(h)au-ro-,  *st(hf  uro-, *st(h)uro-,  ‘strong,  stiff’,  enlargements  of  base *st(h)au-,  *st(h)it-,  ‘stiff,  upright;  post,  pillar’, whence  Gk.  axusiv,  ‘to  make  stiff,  erect,  place, set’,  cttuXo?,  ‘wooden  pole,  style  for  writing; see  Walde-Hofmann,  LEW.,  I,  705-706  s.v. instaurare  and  Kluge-Mitzka  EWDS.,  pp.  747- 748.
=== leaf 802 nums ['1513']
    stone -> nded  of stere-  and  Gk.  otttixov,  neut.  of  oixxixds,  ‘per¬ taining  to  sight’.  See  optic, stereoscope,  n.,  an  instrument  blending  into  one image  two  pictures  of  an  object,  so  as  to  give  the impression  of  solidity.  —  Coined  by  the  English physicist  Sir  Charles  Whetstone  (1802-75)  fr. stereo-  and  Gk.  -axomov,  fr.  axo7TEiv,  ‘to  look at,  examine’.  See  -scope. Derivatives :  stereoscop-ic,  stereoscop-ic-al,  adjs., stereoscop-ic-ally,  adv.,  stereoscop-y,  n. stereotype,  n.  (print.)  —  Compounded  of  stereo- and  -type. Derivatives:  stereotype,
    stiff -> cubic  meter.  —  F.  stere,  fr.  Gkaxe- p£o?,  ‘solid’.  See  stereo-, stere-,  form  of  stereo-  before  a  vowel, stereo,  n.  —  Abbreviation  of  stereotype, stereo-,  before  a  vowel  stere-,  combining  form meaning  ‘solid,  firm’.  —  Gk.  oxepeo-,  fr. oxEpEcu;,  ‘firm,  hard,  solid,  stiff’,  fr.  I.-E.  base *ster-,  ‘stiff,  rigid’.  See  stare  and  cp.  sterile.  Cp. also  the  second  element  in  cholesterol, stereobate,  n.,  a  solid  substructure  without  col¬ umns.  —  Compounded  of  stereo-  and  Gk. [ixxYjC,  ‘that  which  steps  or  treads’,  which  is  rel. to  p
=== leaf 803 nums ['1514', '1515']
    stone ->  way’,  <m|3ap6?,  ‘close,  pres¬ sed,  compact’,  <jxs£(3ei.v,  ‘to  tread’  (prop,  ‘to compress  by  treading’),  fr.  I.-E.  base  *steib-, *steibh-,  *stib-,  *steip-,  ‘compact,  stiff’,  which  is possibly  a  labial  enlargement  of  base  *stei-, *sti-,  ‘to  thicken,  compress,  stiffen;  stone’.  See stone  and  cp.  stifle.  Cp.  also  constipation,  cos¬ tive,  steeve,  ‘to  stow’,  stevedore,  stipate,  stipe, stipes,  stipulate,  stipule. Derivatives:  stiff,  n.,  stiffen,  v.  (q.v.),  stiff-ish, adj.,  stiff-ly,  adv.,  stiff-ness,  n.,  stiff-y,  adj. stiffen,  tr.  and  int
    stiff ->  The  first  element  derives  fr.  OE. sticel,  ‘goad,  sting’,  fr.  stician,  ‘to  stab,  prick, pierce’.  See  stick,  v.,  and  dimin.  suff.  -le  and  cp. the  second  element  in  banstickle.  The  fish  is called  stickleback  in  allusion  to  the  prickles  on its  back.  Cp.  thornback. stiff,  adj.  —  ME.  stif  fr.  ^E.  stif,  rel.  to  ON. stifr,  Du.  stijf,  OHG.,  MHG.  stif,  G.  steif,  ‘stiff’, and  cogn.  with  L.  stipes,  ‘log,  stock,  trunk  of  a tree’,  stipare,  ‘to  compress’,  Lith.  stiprus, ‘strong’,  stimpu,  stipti,  ‘to  grow  stiff’,  Gk.  oxi- <po?,  ‘a 
    Avestic ->  cancel  a  correction.  —  Fr.  L.  stet,  ‘let  it  stand’, 3rd  sing.  pres.  subj.  of  stare,  ‘to  stand’.  See  state, stetho-,  combining  form  meaning  ‘breast,  chest’, as  in  stethoscope.  —  Gk.  ctxtj&o-,  fr.  axvjRo?, ‘breast’,  prob.  cogn.  with  OI.  stanah,  ‘teat,  nip¬ ple’,  Avestic  fshtana-,  Arm.  stin,  of  s.m. stethometer,  n.,  an  instrument  for  measuring  the expansion  of  the  chest  during  breathing.  — Compounded  of  stetho-  and  Gk.  pixpov,  ‘meas¬ ure’.  See  meter,  ‘poetical  rhythm’. Derivatives :  stethometr-ic,  adj.,  stethometr-y,  n. stethos
=== leaf 804 nums []
    stone -> are,  later  distillare,  ‘to  drip, trickle  down,  distill’,  fr.  de-,  resp.  di-,  ‘apart’, and  stillare,  ‘to  drop,  trickle’,  fr.  stilla,  ‘drop’, which  prob.  stands  for  *stir(a)la ,  dimin.  of stiria,  ‘drop’,  from  I.-E.  base  *stei-,  *sti-,  ‘to thicken,  compress,  stiffen ;  stone’.  See  stone  and cp.  distill,  instill. Derivative:  still,  n.,  an  apparatus  for  distilling, stilliform,  adj.,  having  the  form  of  a  drop.  — Compounded  of  L.  stilla,  ‘a  drop’,  and  forma, ‘form,  shape’.  See  still,  ‘to  distil’,  and  form,  n. stilling,  also  stillion
    stiff -> stilbe. stile,  n.,  steps.  —  ME.,  fr.  OE.  stigel,  ‘device  for climbing  ladder’,  rel.  to  OHG.  stigila,  of  s.m., fr.  Teut.  base  *stig-,  ‘to  climb’.  See  sty,  ‘to ascend’,  and  cp.  words  there  referred  to. stile,  n.,  an  upright  piece  in  the  frame  of  a  door. —  Du.  stiff  ‘doorpost’,  fr.  MDu.,  prob.  fr.  L. stilus,  ‘pike,  pale’.  See  2nd  style, stiletto,  n.,  a  small  dagger.  —  It.,  dimin.  of  stilo, fr.  L.  stilus,  ‘a  pointed  instrument’.  See  style,  ‘a pointed  instrument’,  and  cp.  stylet, still,  adj.  —  ME.  stille,  fr.  OE.  still
    Avestic -> ll  of  incentives’,  fr.  L.  stimulus.  See  next word  and  adj.  suff.  -ose. stimulus,  n.,  that  which  stimulates,  incentive.  — - L.,  ‘goad,  sting,  spur,  incentive’,  formed  fr. *sti-mos,  fr.  I.-E.  base  *stei-,  *sti-,  ‘pointed’, whence  also  L.  stilus,  ‘pointed  instrument’, Avestic  staera-,  taera-  ‘summit’,  Afghan,  tera, ‘sharp,  pointed’ ;  see  style,  ‘pointed  instrument’. For  the  derivatives  of  *steig-,  an  enlarged  form of  base  *stei-  see  stick,  v.,  and  cp.  words  there referred  to. stimy,  n.  —  See  stymie. sting,  tr.  and  intr.  v.  —  M
=== leaf 805 nums []
    taj -> omak ,  fr.  OF.  (=  F.)  esto- mac,  fr.  L.  stomachus,  ‘gullet,  esophagus,  stom¬ ach,  liking,  taste’,  fr.  Gk.  ox opayop,  ‘throat, gullet,  esophagus,  stomach’,  fr.  ax6pa,  ‘mouth’, which  is  cogn.  with  Avestic  staman-,  ‘mouth  (of a  dog)',  Hitt,  shtamar ,  ‘mouth’,  MBret.  stajfn, ‘mouth;  jawbone’,  Co.  stefenic,  ‘palate’.  Cp. stoma. Derivatives:  stomach,  tr.  v.,  stomachal  (q.v.), stomach-ed,  adj.,  stomach-er,  n.,  stomach-ful, adj.,  stomachic  (q.v.),  stomach-less,  adj., stomach-y,  adj. stomachal,  adj.,  pertaining  to  the  stomach.  —  See prec.  wo
    stone -> —  L.  stoliditds,  ‘dullness, obtuseness’,  fr.  stolidus.  See  prec.  word  and  -ity. stolon,  n.,  a  shoot,  sucker.  —  L.  stold,  gen.  -dnis, cogn.  with  Arm.  stein ,  ‘trunk  (of  a  tree) ;  branch’, Gk.  axEXeyoc,  ‘trunk,  stem,  log’,  axsXea,  ‘haft, shaft’,  axrjXr],  ‘block  of  stone’,  Lett,  stulms, ‘trunk  (of  a  tree),  arm,  leg’,  fr.  I.-E.  base  *st(h)el-, ‘to  cause  to  stand,  to  place’.  See  stall  and  cp. stolid. stolonate,  adj.,  having  a  stolon.  —  Formed  with adj.  suff.  -ate  fr.  L.  stold,  gen.  -dnis.  See  prec. word. stoloniferous,  adj., 
    Avestic -> o  xaxo?,  ‘bad,  evil’.  See  prec.  word  and caco-. stomach,  n.  —  ME.  stomak ,  fr.  OF.  (=  F.)  esto- mac,  fr.  L.  stomachus,  ‘gullet,  esophagus,  stom¬ ach,  liking,  taste’,  fr.  Gk.  ox opayop,  ‘throat, gullet,  esophagus,  stomach’,  fr.  ax6pa,  ‘mouth’, which  is  cogn.  with  Avestic  staman-,  ‘mouth  (of a  dog)',  Hitt,  shtamar ,  ‘mouth’,  MBret.  stajfn, ‘mouth;  jawbone’,  Co.  stefenic,  ‘palate’.  Cp. stoma. Derivatives:  stomach,  tr.  v.,  stomachal  (q.v.), stomach-ed,  adj.,  stomach-er,  n.,  stomach-ful, adj.,  stomachic  (q.v.),  stomach-less,  adj., stom
=== leaf 806 nums []
    stone -> fo?  and  is  rel.  to  etxea,  which  prob. stands  for  *fctxea;  fr.  I.-E.  base  *wei-,  ‘to  bend, twist’.  See  withy  and  cp.  Itea. -stomous,  combining  form  meaning  ‘having  a mouth’  (zool.  and  bot.)  —  Gk.  -axopo;,  ‘having a mouth,  mouthed’,  fr.  ax6pa,  ‘mouth’.  See  stoma, stone,  n.  —  ME.  Stan ,  ston,  stoon,  fr.  OE.  stan, rel.  to  ON.  steinn,  Dan.  steen,  Swed.  sten, OFris.,  OS.  sten,  Du.  steen,  OHG.,  MHG.,  G. stein,  Goth,  stains,  fr.  I.-E.  base  *stai-,  *stei-, *sti,  ‘to  thicken,  compress,  stiffen;  stone’, whence  also  OI.  styayate, 
    stiff ->  mouthed’,  fr.  ax6pa,  ‘mouth’.  See  stoma, stone,  n.  —  ME.  Stan ,  ston,  stoon,  fr.  OE.  stan, rel.  to  ON.  steinn,  Dan.  steen,  Swed.  sten, OFris.,  OS.  sten,  Du.  steen,  OHG.,  MHG.,  G. stein,  Goth,  stains,  fr.  I.-E.  base  *stai-,  *stei-, *sti,  ‘to  thicken,  compress,  stiffen;  stone’, whence  also  OI.  styayate,  ‘curdles,  becomes hard’,  part,  stydnah,  ‘curdled’,  Avestic  sta-, stay-,  ‘heap’,  Gk.  axeap,  gen.  axeaxo?,  ‘fat,  tal¬ low’,  axTa,  axtov,  ‘pebble’,  axtXr],  ‘drop’,  L. stiria,  stilla,  ‘drop’,  OSlav.  stena,  ‘wall’.  Cp. stean,  steat
    Avestic -> , rel.  to  ON.  steinn,  Dan.  steen,  Swed.  sten, OFris.,  OS.  sten,  Du.  steen,  OHG.,  MHG.,  G. stein,  Goth,  stains,  fr.  I.-E.  base  *stai-,  *stei-, *sti,  ‘to  thicken,  compress,  stiffen;  stone’, whence  also  OI.  styayate,  ‘curdles,  becomes hard’,  part,  stydnah,  ‘curdled’,  Avestic  sta-, stay-,  ‘heap’,  Gk.  axeap,  gen.  axeaxo?,  ‘fat,  tal¬ low’,  axTa,  axtov,  ‘pebble’,  axtXr],  ‘drop’,  L. stiria,  stilla,  ‘drop’,  OSlav.  stena,  ‘wall’.  Cp. stean,  steato-,  the  first  element  in  steenbok, steinbok,  and  the  second  element  in  Athelstan, felstone.  
=== leaf 807 nums []
    stiff -> c¬ cuse’,  G.  stauen,  ‘to  stow’,  Goth,  stojan,  ‘to judge’,  and  cogn.  with  OSlav.  stavljo,  staviti,  ‘to place’,  stavu,  ‘structure’,  Lith.  stdviu,  stoveti,  ‘to 1520  ' stand’,  Lett,  stavu,  stdveju,  stavet,  of  s.m.  All these  words  derive  fr.  I.-E.  *st(h)au-,  *st(h)ii-, ‘stiff,  upright’,  which  is  an  enlargement  of  base *st(h)a-,  ‘to  stand’.  See  state  and  cp.  bestow.  Cp. also  stud,  ‘peg’.  Cp.  also  steer,  ‘to  direct’. Derivatives:  stow-age,  n.,  stow-er,  n.,  stow-ing, n. strabism,  n.,  strabismus.  —  See  strabismus. strabismal,  strabismic
```


## [2026-09-14T02:35:54.069Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=shanty",
 "prompt": "Give the etymology given for shanty (a crudely built cabin) — does it mention Canadian French chantier or Irish sean tig?"
}
```


## [2026-09-14T02:35:56.602Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT thatch/deck/tile/toga ===\"\ngrep -n -A3 \"^THATCH\\|^thatch\\|^DECK\\|^deck,\" SKT.txt | head -30\necho \"=== SYN stone ===\"\ngrep -n -m5 \"stone.*Goth. stains\\|stains\" SYN.txt | head -10"
}
```


### [2026-09-14T02:35:56.728Z] TOOL RESULT

```
=== SKT thatch/deck/tile/toga ===
23138:thatch  ^3).
23139-paladin — palatine.            ^^^^|
23140-jy— oboe.
23141-madam  ~  mftd  oosa.
=== SYN stone ===
1582:‘firewood’. Ernout-M. 549. Walde-H. | NIv. fiodh (Iv. fid, 1.41) still used for 1.799. ‘wood’ in cpds. and derivs. 144 STONE; ROCK Grk. — Aifos; wérpa Goth. stains; hallus Lith. akmuo; uola NG mérpa, ABdpt ON steinn Lett. akmens; klinis Lat. lapis; sacum, petra Dan. _ sten; klippe ChSl. kamy (skala) It. ptelra, sasso; roccia Sw. sten; klippa SCr. kamen; strijena Fr. pierre; roche, rocher (0) 0} slan Boh. kdaen; skdla Sp. piedra; roca ME stone; rokke Pol. kamien; skala, opoka Rum. piatrd; stined, rocd NE stone; rock Russ. kamen’; skala Ir. cloch, lia; carric, all, Du. steen; rots Skt. agman-, acan-, cild- craic OHG - stein; felis, feliso pasana, etc. NIr. loch; carraig, craig MHG stein; vels, velse Av. asan-, zarslva- W. carreg, maen; craig MHG stein; fels, felsen Br. maen; karreg
1611:4. Goth. stains, ON steinn, OE stan, OHG stein, etc., the general Gmc. word for ‘stone’ and in the earlier periods also ‘rock’ : Grk. oria ‘pebble’, creap ‘stiff, fat’, Skt. stya- ‘stiffen’, ChSI. sténa ‘wall’, SCr. stijena ‘rock’, etc. ‘Stone’ fr. ‘stiff, solid’. Walde-P. 2.610 ff. Feist 447, Falk-Torp 1157.
1612:Goth. hallus ‘rock’ (so only once for aérpa, which is otherwise rendered, like AiGos, by stains), ON hallr ‘large stone’, also ‘slope, hill’ (cf. adj. hallr ‘sloping’), OE heall ‘stone, rock’ (rare except in proper names), prob. : Lat. collis ‘hill’, Lith. kalnas ‘mountain’, ete. (1.22), with development through ‘cliff’. Feist 241. Otherwise Walde-P. 1.434, 454, Falk-Torp 395, 1480.
1623:SCr. stijena ‘rock’ : ChSl. sténa ‘wall’, Goth. stains ‘stone’, etc., above, 4.
11911:ChSI. sténa, etc., general Slavic : Goth. stains ‘stone’, etc. Walde-P. 2.611. Traut- mann 281. Otherwise Briickner 529.
```


### [2026-09-14T02:35:57.167Z] TOOL RESULT

```
Based on the dictionary entry provided, the etymology for shanty (a roughly built cabin) **does mention Canadian French** *chantier*. 

The source states: "Probably from Canadian French *chantier*, hut in a lumber camp, from French, timberyard, from Old French, gantry, from Latin *canthērius*, rafter, nag, from Greek *kanthēlios*, pack ass."

The etymology **does not mention Irish** *sean tig*.
```


## [2026-09-14T02:36:08.451Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ncurl -s -m 60 'https://ia-petabox.archive.org/services/search/beta/page_production/scrape.json?q=%22sean%20tig%22&identifier=americanheritag00morr' | head -c 2000; echo; echo \"=== try2 ===\"\ncurl -s -m 60 'https://api.archivelab.org/books/americanheritag00morr/searchinside?q=sean+tig' | head -c 1500"
}
```


### [2026-09-14T02:37:09.755Z] TOOL RESULT

```
=== try2 ===
```


## [2026-09-14T02:37:12.898Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nfor id in americanheritag00morr americanheritage1986morr; do\necho \"### $id\"\ncurl -s -m 60 \"https://ia800000.us.archive.org/fulltext/inside.php?item_id=$id&doc=$id&path=/&q=%22sean+tig%22\" | head -c 1200; echo\ndone"
}
```


### [2026-09-14T02:37:14.157Z] TOOL RESULT

```
### americanheritag00morr

### americanheritage1986morr
```


## [2026-09-14T02:37:21.979Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D8%A7%DB%8C%D8%B1/",
 "prompt": "What do فرهنگ معین and فرهنگ عمید say about تایر — its meaning and its origin tag (e.g. [فر.] French, [انگ.] English)?"
}
```


## [2026-09-14T02:37:23.704Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D9%86%DA%AF%D8%B3%D8%AA%D9%86/",
 "prompt": "What do فرهنگ عمید and فرهنگ معین say about تنگستن — meaning and origin tag (French/Swedish)?"
}
```


### [2026-09-14T02:37:28.312Z] TOOL RESULT

```
# فرهنگ معین and فرهنگ عمید on تایر

**فرهنگ معین** defines تایر as: "(یِ ) [ انگ . ] (اِ. ) = طایر: لاستیک رویی چرخ وسایل نقلیه"

This entry tags the term with [انگ.] (English origin) and provides the basic definition of the rubber covering on vehicle wheels.

**فرهنگ عمید** offers a more comprehensive definition: "لاستیک رویی چرخ اتومبیل، موتور سیکلت، دوچرخه، و مانندِ آن"

This dictionary expands the scope to include various vehicle types (automobiles, motorcycles, bicycles, etc.) but does not include an origin tag in the excerpt provided.

Neither source discusses the etymology in detail; that information appears in the longer historical account in the دانشنامه عمومی section.
```


### [2026-09-14T02:37:30.243Z] TOOL RESULT

```
# فرهنگ عمید and فرهنگ معین on تنگستن

**فرهنگ عمید** defines تنگستن as: "فلزی خاکستری، بسیار سخت و دیرگداز که مفتول های آن در مقابل کشش و حرارت مقاومت بسیار دارد" (a gray metal, extremely hard and durable, whose wires resist tension and heat significantly). It notes the element's industrial importance through its alloys and provides the alternative name "وُلفرام."

**فرهنگ معین** (referenced in the Dānešnāmeh-ye Āzād-e Fārsī section) traces the origin to "عبارتی سوئدی به معنای سنگ سنگین" (a Swedish phrase meaning heavy stone). The entry emphasizes تنگستن's highest melting point among metals and its applications in steel alloys and electrical components.

Neither source explicitly discusses French etymology, though both acknowledge the German-derived name "ولفرام" and Swedish origins of the term's meaning.
```


## [2026-09-14T02:37:40.136Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef find(kw, ctx=420):\n    for i,p in enumerate(pages):\n        m=re.search(kw,p)\n        if m:\n            nums=re.findall(r'^\\s*(1?[0-9]{3})\\s*$',p,re.M)\n            print('---',kw,'leaf',i,'nums',nums)\n            print(p[max(0,m.start()-60):m.start()+ctx].replace('\\n',' '))\n            print()\n            return\nfind(r'thatch,\\s+tr')\nfind(r'\\bdeck,\\s+n')\nfind(r'\\btoga,\\s+n')\nfind(r'\\btile,\\s+n')\nfind(r'\\btaj,')\nEOF"
}
```


### [2026-09-14T02:37:42.638Z] TOOL RESULT

```
--- thatch,\s+tr leaf 847 nums ['1600', '1601']
ly  distinguished  from  the  con¬ junction  dafi,  ‘that’. thatch,  tr.  v.  —  ME.  thecchen,  thacchen,  fr.  OE. peccan,  ‘to  cover’,  rel.  to  OS.  thekkian,  ON. pekja,  Swed.  tacka,  Dan.  deekke,  OFris.  thekka, MDu.  decken,  Du.  dekken,  OHG.  decchen, decken,  MHG.,  G.  decken,  ‘to  cover’,  and  to OE.  pxc,  ‘roof,  thatch’,  ON.  pak,  Swed.  tak, Dan.  tag,  OFris.  thek,  MLG.,  MDu.,  Du.  dak, ‘roof’,  OHG.  dah,  MHG.,  G.  dach,  ‘roof’,  fr. I.-E. 

--- \bdeck,\s+n leaf 226 nums ['410', '411']
 MDu.  decken  (Du.  dek- ken),  ‘to  cover’.  See  thatch, deck,  n.,  covering  (obsol.)  —  MDu.  decke,  dek, (Du.  dek),  ‘roof,  covering’,  fr.  decken,  ‘to  cover'. See  deck,  v.,  and  cp.  next  word, deck,  n.,  covering  of  a  ship.  —  Shortened  fr.  G. verdeck  (whence  also  Du.  overdek,  later  dek), lit.  ‘covering’  (see  for-  and  thatch  and  cp.  deck, v.),  and  prop,  a  loan  translation  of  Olt.  (=  It.) coperta  or  MF.  couverte.  That  E.  

--- \btoga,\s+n leaf 860 nums []
  next  word. Derivatives:  tog,  tr.  v.,  tog-less,  adj. toga,  n.  —  L.  toga,  ‘a  garment’,  lit.  ‘a  covering’, in  gradational  relationship  to  tegere,  ‘to  cover’. See  thatch,  n.,  and  cp.  tegument  and  words  there referred  to. Derivative:  toga-ed,  adj. togated,  adj.,  togaed;  dignified.  —  Formed  with 1st  suff.  -ed  fr.  L.  togatus,  ‘

--- \btile,\s+n leaf 857 nums []
‘inscription,  superscription,  label,  title’. See  title. tile,  n.  —  ME.,  fr.  OE.  tigele,  tigule,  which,  to¬ gether  with  OS.  tiegla,  ON.  tigl,  Dan,  tegl,  Swed. tegel,  MDu.  Hegel  (Du.  tegel),  OHG.  ziagala, ziagal  (MHG.,  G.  ziegel ),  derives  fr.  L.  teguia (whence  also  It.  tegola,  F.  tuile),  which  is  rel.  to tegere,  ‘to  cover’.  See  thatch  and  cp.  tegument. Cp.  also  tuille. Derivatives:  tile,  tr.  v.,  til-ed,  adj.,  til-er,  n

--- \btaj, leaf 801 nums []
se  *stegwh-,  ‘to  encircle, crown’,  whence  also  Pers.  taj,  ‘crown’.  Cp.  ste- phano-  and  the  second  element  in  Agrostemma. Cp.  also  taj.  For  the  ending  see  suff.  -ma. Stemona,  n.,  a  genus  of  plants  (hot.)  —  ModL., fr.  Gk.  crTTKitiiv,  ‘warp’.  See  stamen, stemple,  stempel,  n.,  cross  timber.  —  G.  Stempel, ‘stamp,  die,  prop’,  fr.  LG.  stempel,  lit.  ‘an  in¬ strument  for  stamping’,  formed  from  the  stem of  MLG.  stampen,  ‘to
```


## [2026-09-14T02:37:56.561Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AC' \\\n 'https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AC%DB%8C%DA%A9' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-' \\\n 'https://en.wiktionary.org/wiki/%D5%BF%D5%A1%D5%B3%D5%A1%D6%80' \\\n 'https://www.etymonline.com/word/tiara' \\\n 'https://www.etymonline.com/word/attire' \\\n 'https://www.etymonline.com/word/shanty' \\\n 'https://www.etymonline.com/word/tungsten' \\\n 'https://www.ahdictionary.com/word/search.html?q=shanty' \\\n 'https://abadis.ir/fatofa/%D8%AA%D8%A7%DB%8C%D8%B1/' \\\n 'https://abadis.ir/fatofa/%D8%AA%D9%86%DA%AF%D8%B3%D8%AA%D9%86/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 477 (Steg/Teg, Stei/Stai 2): taj, tajik/tazi, tacara, tiara/attire/tire, shanty, tungsten, tayer, tangstan' 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T02:38:03.300Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d056c3b3f7254dbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b01d803d3575faa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d0ed57c08cddecc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a85fa8d9246bad11.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9a2b2df1ec1f6918.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/37bcd316144b648a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77c8426d3af491a6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a1505f2751a20cba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/75bfb36a89d9fe4a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa87d2d3b0acc0c2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/74c96fed21f27e95.txt
```


## [2026-09-14T02:38:08.096Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Taj_Mahal",
 "prompt": "Give the etymology of Taj Mahal: Persian/Urdu components, meaning, and the route into English."
}
```


### [2026-09-14T02:38:13.915Z] TOOL RESULT

```
# Etymology of Taj Mahal

## Origin and Components

The term comes from Hindustani, derived from Classical Persian and Arabic roots. The name breaks into two parts: **taj** (crown) and **mahal** (palace), literally meaning "crown of palaces."

According to the source, it originates from "Hindustani _ताज महल_ / _تاج محل_ (tāj mahal, 'crown of palaces'), from Classical Persian, ultimately from Arabic."

## Route into English

The word entered English through the Hindustani language, which itself borrowed it from Classical Persian—the lingua franca of the Mughal court. This linguistic pathway reflects the monument's historical context: the Taj Mahal was constructed between 1631 and 1654 under Mughal rule in Agra, India.

The name thus traveled: Arabic → Persian → Hindustani → English, carrying with it the architectural and cultural significance of one of the world's finest examples of Mughal architecture.
```


## [2026-09-14T02:38:16.626Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Taj_Mahal' --note 'page 477, root Steg/Teg, node 10: Taj Mahal from Hindustani taj mahal \"crown of palaces\"' 2>&1 | tail -2"
}
```


### [2026-09-14T02:38:18.103Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b11c5da35382b510.txt
```


## [2026-09-14T02:38:24.200Z] TOOL CALL #62: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:38:24.247Z] TOOL RESULT

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


## [2026-09-14T02:38:32.116Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW tego ===\"; grep -n -m3 \"tego, -ere\\|tegula\" LEW_1910.txt | head -5\necho \"=== LAT tego ===\"; grep -n -m3 \"tegō\\|tego,\" LAT.txt | head -5\necho \"=== IEC steg ===\"; grep -n -m6 \"stegō\\|tegō\\|thakjan\\|tegos\" IEC.txt | head -8\necho \"=== IEC stainaz/stei ===\"; grep -n -m4 \"stainaz\\|staina-\\|stāi\" IEC.txt | head -6\necho \"=== LKT tiara/taj ===\"; grep -n -i -m5 \"Tiara\\|Tadsch\\|tāǧ\" LKT.txt | head -8\necho \"=== HJB taj ===\"; grep -n -m5 \"TAJ\\b\\|Taj Mahal\" HJB.txt | head -5"
}
```


### [2026-09-14T02:38:32.276Z] TOOL RESULT

```
=== LEW tego ===
=== LAT tego ===
4843:3 e d6clinaison (par inflnence de tego, tectus, tSctum?); architecton,
16089:la foraation, cf. lignum et lego, tignum et tego, plenus et pleo. Sens:
63201:tego, -Is, texi, tectum, -ere: couvrir, recouvrir; d'ou, garan-
=== IEC steg ===
18253:tegos, -es- (teget-, tegt-, tegus) “cover, lid, roof, house'. Cf. tego Gk. tégos, gs: -eos, n. ‘covering, roof”; Lat. cf. teges, gs: tegetis, f. (rug, mat: tignum, n. *roof-beam' beside tigillum, n. ‘rafter; tectum "root, home’; (for sub-temen ‘woof, see teKs-); Umb. tettom ‘house’; Osc. cf. tehtefim, n. (/stucco', qua *tectorium); Olr. teg, gs: & npl. tige, m. ‘house’; Mir. teg & tech, m. id. beside (long-gde) tí, s. ‘coat’; Ir. tigh & teach, gs. & npl. tighe, m. ‘house’; OBr. tig-, id. (fr. *tegus); Br. ti, Cor. ty & chy, m. id.; W ty, pl. tai, teiau & tyau, m. id.; OCS cf. tetegü, m. redup. (queried: *home, shelter")
18699:togos, à, io ‘cover, covering, roof, thatch’. WP II, 621. Cf. tego, tegos Lat. toga, f. ‘toga’; Ir. tuighe, f. ‘thatch, roof’; W to, pl. au. -ion, m. id.; Br. tó, m. ‘roof; Cor. tō, pl. tohow, m. as Ir.; OHG dach, n., OE pac, n.; ON bak, n. ‘roof (ON also cover)
=== IEC stainaz/stei ===
=== LKT tiara/taj ===
1898:Armenier  oder  Griechen  aus,  ist  meist allein  und  greift  zur  SchußwatTe  nur, wenn  man  sie  gegen  ihn  erhebt.  Der Hyrsyz  entspricht  dem  gewöhnlichen Briganlen,  wie  er  auch  in  anderen Ländern  der  Halbkultur  vorkommt.  Der Haiduk  ist  der  Bandit  mit  nationaler Färbung,  eine  Spezialität  des  Balkans, heutzutage  häufig  Komitadschi  [<tk. komita  ==  comite  und  Suffix  -gi  zur  An- gabe des  Berufes,  also  ,dem  Komite Angehöriger",  d.h.  dem  Komite  zur  Be- freiung Mazedoniens  von  jeglicher  nicht- mazedonischer oder  -bulgarischer  Herr- schaft] genannt:  frz.  comitadji.
3239:1404.  Ar.  itiarad:
5791:Karett(schildkröte)  1073 harmin  1219 Äaro6<;  832 Aantie  832 Za/w  1087 ÄrtsacÄ;  1143 ka  sacke  mhd.  1143 iTäsf/j  1102 Kaschemme  ].  1129 Kaschmir  1116 Kasimir  1116 Kasperle  1059 kaspern  J.  1059 Kassiber  1168 üfa.wär  1119 kasugele  mhd.  1143 Katesberger  j.  845 Katschäume  j.  1129 Kat(t)un  1272 Katzoff  ].  1107 Kauri(mtixchel)  1133 K'iviar  851 Af/ü«  1176 Keschengannef  j.  659 ifessfZ  j'.  1166 ÄÄaiti  787 ZvV/'er  727 AiVs  j.  1185 Kimono  1177 iC/osfc  732 je*«»)««  1187 KitUchen)  j.  1190 Ai^^eZ  1272 Klabautermann  1022 AZMf<  j.  1154 knassen  j.  1050 Änasi  j.  1050 AocTiafe  St.  1132 kochem  j.  788 kochemer  Loschen  j.  788 A'o/f«-  1225 ATo/t/  j.  1194 A^ofroH  1170 Kolkothar  1236 Komitadschi  781 Konditor  1052 Aopefce  1204 Köpernick  1159 Aojsm  1169 Aoran  1250 Korund  1263
=== HJB taj ===
14237:MBHAUL,  8.  Hind,  from  Arab. maftdUy  being  properly  the  pi.  of  Arab. maMU.  The  worn  is  used  with  a  con- siderable variety  of  application,  the explanation  of  which  would  involve  a f^reater  amount  of  technical  detail  than IS  consistent  with  the  purpose  of  this work.  On  this  WiUon  may  be  con- sulted. But  the  most  usual  An^lo- Indian  application  of  mahdU  (usea  as a  singular  and  generally  written,  in- coiTectly,  mafidi)  is  to  *  an  estate/  in the  Revenue  sense,  t.e,  'a  parcel  or parcels  of  land  separately  assessed  for revenue.'  The  sing,  mciliall  (also written  in  the  vernaculars  mafialy  and mahd^  is  often  used  for  a  palace  or important  edifice,  e,g,  (see  8HI8H- HUHULL,  TAJ-KAHAL).
21331:TAJ,  s.  Pers.  tdj,  *a  crown.'  The most  famous  and  beautiful  mausoleum in  Asia ;  the  Tdi  Malial  at  A^ra, erected  by  Shah  Jahan  over  the  bunal- nlace  of  his  favourite  wife  Mumtaz-i- Mahal  ('Ornament  of  the  Palace') Banu  B^m.
```


## [2026-09-14T02:39:39.463Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HJB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'TAJ,  s.  Pers' in p: print('leaf',i)\nEOF"
}
```


### [2026-09-14T02:39:40.642Z] TOOL RESULT

```
leaf 932
```


## [2026-09-14T02:46:38.582Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HJB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'TAJ,  s.  Pers' in p: print('leaf',i,'-> printed approx', i-35, 'to', i-51)\nEOF"
}
```


### [2026-09-14T02:46:39.726Z] TOOL RESULT

```
leaf 932 -> printed approx 897 to 881
```


## [2026-09-14T02:46:42.452Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:56:46.425Z] TOOL CALL #66: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-477.json <<'JSONEOF'\n{\n  \"pdf_page\": 477,\n  \"book_page\": 447,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Steg, Teg\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *(s)teg- 'to cover' (Pokorny 1. (s)teg- 1013-1014; Watkins/AHD (s)teg-)\",\n      \"note\": \"The root, the language label and the gloss are all correct: Pokorny IEW 1013-1014 'Root / lemma: (s)teg-1, Meaning: to cover', with the s-less variant *teg- in Lat. tego, OIr. tech, Gk. stego (s-mobile). Watkins reprints it as '(s)teg-. To cover. [Pok. 1. (s)teg- 1013.]'. Nourai's double heading 'Steg, Teg' is exactly the s-mobile pair. What is NOT in Pokorny is the whole left-hand Iranian branch: neither OP tacara- nor NP taj appears in IEW under this lemma. Watkins alone adds 'Persian taj, crown' to the root; Klein (p.1510, s.v. stemma) assigns Pers. taj instead to a different IE base *stegwh- 'to encircle, crown' (the root of Gk. stephein, stemma). Nourai follows AHD. The Germanic, Latin and Celtic branches of the chart are textbook-correct.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *(s)teg- «پوشاندن» (پوکورنی، ص ۱۰۱۳–۱۰۱۴؛ واتکینز در پیوست AHD). صورت بی‌s یعنی *teg- در لاتینی tego، ایرلندی باستان tech و صورت s-دار در یونانی stégō دیده می‌شود؛ بنابراین سرنویس دوگانهٔ نورایی «Steg, Teg» درست است. اما شاخهٔ ایرانیِ سمت چپ نمودار (پارسی باستان tačara و فارسی «تاج») در پوکورنی زیر این ریشه نیامده است: تنها واتکینز «فارسی tāj، تاج» را به این ریشه بسته و کلاین (ص ۱۵۱۰، ذیل stemma) آن را به ریشهٔ دیگری، *stegʷh- «گرداگرد گرفتن، تاج نهادن»، نسبت می‌دهد. شاخه‌های ژرمنی، لاتینی و سلتی نمودار کاملاً پذیرفتنی‌اند.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:1013\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root / lemma: (s)teg-1 / Meaning: to cover / ... Page(s): 1013-1014'; material = OI sthagayati, Gk. stego/stegos, Lat. tego, tectum, tegula, toga, OIr. tech, ON thekja/thak, OE theccan/thaec, OHG decchen/dah, Lith. stogas. References WP. II 621 f.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)teg-\", \"stance\": \"supports\", \"note\": \"'(s)teg-. To cover. I. O-grade form *tog-. 1. Germanic *thakjan ... 2. Germanic *thakam ... 3. Suffixed form *tog-d-, ... Latin toga ... II. Basic form *steg- in Greek stegein ... III. Basic form *teg-. 1. Latin tegere ... and tegula ... 2. Persian taj, crown: TAJ. [Pok. 1. (s)teg- 1013.]' (AHD_watkins1985.txt line 1007)\"},\n        {\"src\": \"WLD\", \"where\": \"WP. II 621 f. (cited by Pokorny)\", \"stance\": \"supports\", \"note\": \"Pokorny's own 'References: WP. II 621 f., WH. II 654 f., Trautmann 288' — Walde-Pokorny Bd. II 621 is the predecessor entry of the same root; Bd. II is not in the local library, so this is checked only through Pokorny's cross-reference.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. tegos and togos\", \"stance\": \"supports\", \"note\": \"IEC.txt 18253 'tegos, -es- ... \\\"cover, lid, roof, house\\\". Cf. tego Gk. tégos ... Lat. teges ... tectum \\\"roof, home\\\" ... OIr. teg ... W ty'; 18699 'togos, a, io \\\"cover, covering, roof, thatch\\\". WP II, 621. Lat. toga ... OHG dach, OE thac, ON thak \\\"roof\\\"'. No Iranian form.\"},\n        {\"src\": \"KLN\", \"where\": \"p. 1510 s.v. stemma; p. 1600 s.v. thatch\", \"stance\": \"partial\", \"note\": \"Klein has the root under 'thatch' ('fr. I.-E. base *(s)teg-'), but at p.1510 s.v. stemma he puts Persian taj under a DIFFERENT base: 'fr. I.-E. base *stegwh-, \\\"to encircle, crown\\\", whence also Pers. taj, \\\"crown\\\". ... Cp. also taj.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Old Persian\",\n          \"words\": \"tačara\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"OP tacara- (𐎫𐎨𐎼) is real and well attested: DPa 6 'hya imam tacaram akunaus' = 'who built this palace' (Darius' small palace on the south side of the Persepolis terrace, still called the Tachara), XPj 'imam tacaram adam akunavam'. Kent's lexicon p.186 glosses it 'palace' and gives the descendants 'NPers. tazer, Elam. da-is-sa-ma-um, Akk. bit'. But Kent does NOT trace it to Indo-European: in the phonology (§148.V) he lists tacara- among the OP words 'which are not traceable with certainty to IE origins, or are demonstrably borrowings from non-IE sources' (alongside taka- 'shield, round hat', dipi- 'inscription', spada- 'army'), i.e. probably Elamite. No modern source derives tacara- from *(s)teg-; the Wiktionary/Armenian-etymology literature (s.v. tačar) lists OP tacara-, Parthian *tažar and NP tajar side by side without any PIE root. Nourai's gloss 'cover' is his own bridging gloss, not the attested meaning ('palace, winter palace'; Armenian tačar 'temple, palace, banqueting hall'). The arrow root → tacara- is therefore the author's own conjecture and is not supported by the reference he cites.\",\n          \"derivation_fa\": \"واژهٔ پارسی باستان tačara- «کاخ» واقعی و پربسامد است: در کتیبهٔ DPa داریوش «hya imam tacaram akunauš» یعنی «که این کاخ را ساخت»، و کاخ کوچک داریوش در تخت جمشید هنوز «تچر» خوانده می‌شود. اما کنت (Old Persian، واژه‌نامه ص ۱۸۶) آن را تنها «palace» معنی می‌کند و در بخش آواشناسی (§۱۴۸) صریحاً tačara- را در شمار واژه‌هایی می‌آورد که «با اطمینان به اصل هندواروپایی بازنمی‌گردند یا آشکارا وام‌واژه‌اند» — یعنی احتمالاً وام‌واژه‌ای عیلامی، همانند taka- در taka-bara-. هیچ منبع امروزی این واژه را به ریشهٔ *(s)teg- نبسته است و معنای «پوشش» که نورایی می‌آورد از خودِ اوست. پس این پیکان (ریشه ← tačara) از دید پژوهش امروزی پذیرفتنی نیست، و منبعی که خود نورایی به آن ارجاع داده (کنت) خلافش را می‌گوید.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D5%BF%D5%A1%D5%B3%D5%A1%D6%80\"],\n          \"ref_check\": [\n            {\"ref\": \"KNT:186\", \"status\": \"partial\", \"note\": \"KNT.txt line 5428 (lexicon): 'tacara- sb. \\\"palace\\\": NPers. tazer, Elam. da-is-sa-ma-um, Akk. bit (§76.V, §148.I). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227.' The word, the language and the New Persian descendant are confirmed, but Kent gives no IE etymology — and at KNT.txt line 1084 (§148.V) he says: 'There are also numerous instances of OP t th d which are not traceable with certainty to IE origins, or are demonstrably borrowings from non-IE sources. Among these are taka- \\\"shield, round hat\\\" in taka-bara-, tacara- \\\"palace\\\", dipi- \\\"inscription\\\" ...'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch (grep 'tacara', 'tačara')\", \"stance\": \"silent\", \"note\": \"Bartholomae's dictionary is Avestan + OP; no tacara- entry found in BRT.txt — the word is Old Persian only and is treated in the Achaemenid lexica (Kent, Tolman), not in Bartholomae's main body.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 375, p. 84\", \"stance\": \"supports\", \"note\": \"'375. tejer \\\"Winterhaus mit Heizvorrichtung; Magazin\\\", arab. LW. tazar, ap. tacara- (Bedeutung nicht sicher); arm. LW. tacar \\\"Haus, Tempel\\\", tacarapet ...' — Horn accepts OP tacara- as the source of the Persian word but explicitly flags the OP meaning as uncertain and offers no IE root.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt line 8084\", \"stance\": \"supports\", \"note\": \"'tajar \\\"heizbares Winterhaus\\\", arab. tazar \\\"Sommerhaus\\\" = ap. tacara-, arm. tačar \\\"Tempel, Palast, Haus\\\"' — same chain, again with no Indo-European root.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"tajar «تَجَر ( تَزَر ، طَزَر )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP تجر tajar / تزر tazar 'heated winter house, castle, storehouse' continues OP tacara- through Middle Iranian: OP tacara- > Parthian *tažar 'palace, dwelling' (whence Old Armenian տաճար tačar 'temple, palace, banqueting hall', borrowed in the Arsacid period) > NP tajar ~ tazar, with the regular Middle/New Persian outcome of OIr. -č- between vowels as -z-/-ž- (hence the doublet tajar/tazar) and the OP final -a- lost. Arabic took it as طزر ṭazar and, by metathesis of r and z, as طرز ṭarz, glossed in Taj al-'Arus 'al-ṭarz: bayt ilā l-ṭūl, fārisī mu'arrab' ('a house running lengthways, an arabicized Persian word') — which, as Mo'in notes, matches Darius' long narrow Tachara exactly. The Persepolis palace is called تچره tačare in modern Persian archaeology. Nourai's verse (Nazārī Qahestānī) uses تجر in the 'castle/chamber' sense. All three of the chart's spellings تجر/تزر/طزر are attested.\",\n          \"derivation_fa\": \"«تَجَر / تَزَر» در فارسی نو به معنی «خانهٔ زمستانی گرم‌شونده، مخزن، کاخ» دنبالهٔ پارسی باستان tačara- است و از راه ایرانی میانه رسیده: پارتی *tažar «کاخ، خانه» (که ارمنی տաճար tačar «معبد، کاخ» در روزگار اشکانی از آن وام گرفته شده) و سپس فارسی نو «تجر/تزر». دگرگونی آوایی همان تحول عادی č ایرانی باستان در میان دو واکه به z/ž در فارسی میانه است؛ از همین‌روست که دو صورت «تجر» و «تزر» پهلوی هم وجود دارد. معین در حاشیهٔ برهان قاطع (ص ۴۷۲) می‌افزاید که همین «تزر (طزر)» در کتب لغت عرب به صورت مقلوب «طرز» آمده و تاج‌العروس آن را «الطرز: بیت الی الطول، فارسی معرّب» تعریف کرده است — که درست با تچرهٔ باریک و درازِ داریوش می‌خواند. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D5%BF%D5%A1%D5%B3%D5%A1%D6%80\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:84\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 375 (printed p. 84, the page footer '— 85 —' follows): 'tejer \\\"Winterhaus mit Heizvorrichtung; Magazin\\\", arab. LW. tazar, ap. tacara- ...; arm. LW. tacar \\\"Haus, Tempel\\\"'.\"},\n            {\"ref\": \"BQT:472\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt scan page 698 (= printed 472; the same offset puts BQT:458 on scan page 684, which is indeed the تازی/تاجیک page). Entry 'تجر - بفتح اول و ثانی بر وزن شرر، خانهٔ زمستانی گویند که در آن تنور و بخاری باشد - و بزبان قزوین گنجینه و مخزن را نامند'; Mo'in's footnote 4: 'پارسی باستان *tačara ... ارمنی tačar (خانه، معبد) ... در پهلوی tačar ... در پارسی تجر و تزر. اصلاً به کاخ زمستانی اطلاق می‌شده. در تخت جمشید کاخ کوچک داریوش بزرگ ... به «تچره» موسوم است ... همین تزر (طزر) است که در کتب لغت عرب مقلوباً «طرز» آمده'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien, HUB.txt line 8084\", \"stance\": \"supports\", \"note\": \"'tajar \\\"heizbares Winterhaus\\\", arab. tazar \\\"Sommerhaus\\\" = ap. tacara-, arm. tačar \\\"Tempel, Palast, Haus\\\"'.\"},\n            {\"src\": \"KNT\", \"where\": \"Lexicon p. 186\", \"stance\": \"supports\", \"note\": \"'tacara- sb. \\\"palace\\\": NPers. tazer' — Kent himself gives the New Persian continuant.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, grep tacar/tazar\", \"stance\": \"silent\", \"note\": \"No tacar/tažar entry in the Concise Pahlavi Dictionary; the Middle Iranian form is Parthian (Manichaean tžr), outside MacKenzie's Book Pahlavi corpus.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"tâj «تاج»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian تاج tāj 'crown' is real, but the chart's single arrow from PIE *(s)teg- hides a long and partly disputed route, and the two references Nourai cites disagree with each other. Watkins/AHD does exactly what the chart does: under '(s)teg-. To cover' he lists 'III. Basic form *teg-. ... 2. Persian taj, crown: TAJ' — so AHD:1543 supports the arrow. Klein, however (p. 1510 s.v. stemma), derives Pers. taj from a different Indo-European base, *stegwh- 'to encircle, crown', the root of Gk. stephein 'to wreathe, crown' and stemma 'garland'. The attested chain is: Old/Middle Iranian *tāga- 'covering' > Parthian *tāg 'crown' (attested in Manichaean xʾrtʾg /xārtāg/ 'crown of thorns') and Middle Persian tāg; Syriac/Aramaic borrowed it as tāgā, Armenian as թագ tʻag, and Arabic as تاج tāj; New Persian تاج is a re-borrowing from Arabic (hence -j, not the inherited -g), a Persian→Aramaic/Arabic→Persian round trip explicitly stated by Nyberg ('tag [t'k'] crown ... Arab. lw. taj and hence again NP taj'). The same *tāga- 'covering' gives Persian طاق tāq 'arch, vault'. Horn (p. 81-82) treats tāj as unexplained: he rejects any link with OP taka-bara- and with Akkadian agû, and in his appendix reports Jensen's suggestion that tāj, like taka-, might be Elamite. So: a defensible IE etymology that one major reference (AHD) endorses, another (Klein) assigns to a different root, and the Iranian handbooks leave open.\",\n          \"derivation_fa\": \"«تاج» واژه‌ای است اصیل ولی راهش پیچیده‌تر از تک‌پیکانِ نمودار است و دو مأخذی که نورایی آورده با هم نمی‌خوانند. واتکینز (پیوست ریشه‌های AHD) درست همان کار نمودار را می‌کند و «فارسی tāj، تاج» را زیر *(s)teg- «پوشاندن» می‌آورد؛ اما کلاین (ص ۱۵۱۰، ذیل stemma) آن را به ریشهٔ دیگری، *stegʷh- «گرداگرد گرفتن، تاج نهادن» — ریشهٔ یونانی stéphein و stémma — می‌بندد. آنچه مستند است این زنجیره است: ایرانی *tāga- «پوشش» ← پارتی tāg «تاج» (در ترکیب مانوی xārtāg «تاج خار») و فارسی میانه tāg ← وام‌گیری در آرامی/سریانی tāgā، ارمنی tʿag و عربی «تاج» ← و سپس بازگشت همین واژهٔ معرّب به فارسی نو به صورت «تاج» (با ج، نه گ). نیبرگ در واژه‌نامهٔ پهلوی خود این دور کامل را صریح آورده است: «tag تاج ... وام عربی tāj و از آنجا دوباره فارسی نو tāj». همین *tāga- «پوشش» است که «طاق» فارسی را نیز داده. هرن (ص ۸۱–۸۲) «تاج» را ناشناخته می‌داند، پیوند آن را با taka-bara- پارسی باستان و با agû اکدی رد می‌کند و در پیوست، فرضیهٔ ینسن را می‌آورد که شاید عیلامی باشد. پس ادعای نورایی «با احتیاط پذیرفتنی است».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AC\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1543\", \"status\": \"supports\", \"note\": \"Watkins's IE-roots appendix, s.v. (s)teg-: '... III. Basic form *teg-. 1. Latin tegere ... 2. Persian taj, crown: TAJ. [Pok. 1. (s)teg- 1013.]' (AHD_watkins1985.txt line 1007). The page number 1543 belongs to the 1975 New College appendix (pp. 1505-1550), which is not on disk; the 1985 standalone reprint of the same list carries the identical text, and p.1543 falls exactly in the s-/t- stretch of a 46-page alphabetical appendix, so the citation is internally consistent.\"},\n            {\"ref\": \"KLN:1510\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 801 (printed pp. 1510-1511), s.v. stemma: 'L., \\\"garland; pedigree\\\", fr. Gk. stemma ... from the stem of stephein, \\\"to surround, encircle, wreathe, crown\\\", fr. I.-E. base *stegwh-, \\\"to encircle, crown\\\", whence also Pers. taj, \\\"crown\\\". ... Cp. also taj.' Klein thus supports an IE origin for taj but assigns it to *stegwh-, NOT to *(s)teg- 'to cover'; his own entry 'taj, \\\"crown\\\", fr. Pers. taj, of s.m. See stemma' (leaf 830 = p.1566) repeats the cross-reference.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary), s.v. tag\", \"stance\": \"partial\", \"note\": \"'tag [t\\\\'k\\\\'] crown 56-19; han i zros ~ a cockscomb 56-6. — Syr. lw. taga; Arab. lw. taj and hence again NP taj; cf. Arm. t'aga-vor \\\"king\\\".' Nyberg confirms MP tāg 'crown' as the source of the Semitic and Armenian words and makes NP tāj a re-borrowing from Arabic — a step the chart omits.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 367, pp. 81-82 (+ appendix note, p. 89)\", \"stance\": \"contradicts\", \"note\": \"'17 [=367]. täj \\\"Krone\\\", täjver, arm. LW. t'ag, t'agavor. Hat mit ap. Yauna takabara nichts zu tun; und ebenso wenig mit assyr. agü \\\"Krone\\\" (nach Jensen, mündliche Mitteilung).' Horn offers no IE root at all; the long appendix note (Jensen) says 'Nähme man mit Recht an, dass täj = \\\"Krone\\\" elamitischen Ursprungs wäre, ebenso wie taka- in takabarä ...'\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. tāg / abesar\", \"stance\": \"silent\", \"note\": \"MacKenzie's Book-Pahlavi lexicon has 'tāg' only as 'branch' and gives 'abesar [\\\\'fysl | M \\\\'bysr, N afsar] crown' as the Middle Persian word for crown; tāg 'crown' is Manichaean/Nyberg's Book-Pahlavi reading, not in MacKenzie.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"Tâjîk «تاجیک ( تاجیکستان )»; tâzî «تازی»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both words are real, but neither comes from tāj 'crown'. The standard explanation, already the majority view in Nourai's own source, derives them from the name of the Arab tribe Ṭayyiʾ (طيّئ) — the Arabs whom the Sasanians met first on the Iraqi frontier — via Middle Persian tāzīg (Book Pahlavi tʾcyk', MacKenzie 'Tāzīg [tʾcyk' | N tāzī] Arab'); Persian تازی tāzī 'Arab' and its Sogdian/Eastern form tāžīk > تاجیک tājīk. In Central Asia the same word shifted from 'Arab' to 'Muslim of Iranian speech' and finally to the ethnonym 'Tajik'. Horn, on the very page Nourai cites (p. 81-82), reports de Lagarde's derivation from tāj and rejects it: 'Die Erklärung Quatremère's (Tāzī als Nisbe von Tai) ist indess auch nach Nöldeke's Meinung die richtige' — i.e. tāzī is a nisba of Ṭayy, as Nöldeke also held. Mo'in's footnote in Borhan-e Qāteʿ at exactly BQT:458 says the same ('… تاژیک می‌گفتند، و سپس این اطلاق را به همهٔ عرب تعمیم دادند'). Wiktionary calls the tāj connection a folk etymology and cites Henning's *Tāt-čīk, earlier *Tād-čīk, i.e. Mo'in's own MON:996 analysis (Turkic tāt 'subject, non-Turk' + the diminutive -čīk) which Nourai's note reports. Mo'in moreover insists the two are distinct: 'صح: «تاجیک» با «تازی» (= تازیک به معنی عرب) فرق دارد'. Nourai's added claim that tāzī/tājī originally meant 'royal' and referred to 'Iranians in Yemen' is unsupported by any source consulted; the grain of truth is that Ṭayyiʾ was a Qaḥṭānī (South-Arabian/Yemeni) tribe.\",\n          \"derivation_fa\": \"هر دو واژه واقعی‌اند اما هیچ‌کدام از «تاج» نیامده‌اند. تبیین معیار — که در همان صفحه‌ای که نورایی ارجاع داده آمده — این است که «تازی» نسبتی است از نام قبیلهٔ عرب «طیّ»، نخستین عربانی که ساسانیان در مرز عراق با ایشان روبه‌رو شدند: فارسی میانه tāzīg (پهلوی tʾcyk'، مکنزی: «Tāzīg … N tāzī: عرب») ← فارسی نو «تازی»؛ و صورت خاوری/سغدی tāžīk ← «تاجیک». در فرارود همین واژه از معنی «عرب» به «مسلمانِ فارسی‌زبان» و سرانجام به نام قومی «تاجیک» تحول یافت. هرن در ص ۸۱–۸۲ نظر دلاگارد (اشتقاق از «تاج») را نقل و رد می‌کند و می‌گوید توضیح کاترمر — «تازی» نسبت از «طیّ» — به رأی نولدکه نیز درست است. حاشیهٔ معین در برهان قاطع (همان ص ۴۵۸) نیز می‌گوید ایرانیان ایشان را «تاژیک» می‌خواندند و سپس این نام را به همهٔ عرب تعمیم دادند. ویکی‌واژه پیوند با «تاج» را ریشه‌شناسی عامیانه می‌خواند و صورت *Tāt-čīk هنینگ را می‌آورد که همان تحلیل معین (تات ترکی + پسوند تصغیر ـچیک) است. معین حتی تصریح می‌کند: «تاجیک با تازی (= تازیک به معنی عرب) فرق دارد». افزودهٔ نورایی که «تازی/تاجی» در اصل «شاهانه» بوده و به ایرانیان یمن اطلاق می‌شده در هیچ منبعی نیامده؛ تنها نکتهٔ درست این است که طیّ قبیله‌ای قحطانی (یمنی‌تبار) بوده است. پژوهش امروزی ادعای این گره را رد می‌کند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AC%DB%8C%DA%A9\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:81\", \"status\": \"contradicts\", \"note\": \"Horn no. 367, printed pp. 81-82: 'de Lagarde, Nachr. GGG. 1891, 160 folg. stellt np. Tāžīk, Tāzīk, Tāzī \\\"Ureinwohner Persiens, die weder Araber noch Türken sind\\\" (vergl. phlv. Tajik (Bund.), arm. Tacik \\\"Araber\\\"), taziyāne \\\"Peitsche\\\" ... ursprünglich \\\"arabisch\\\" ... zu taj. Die Erklärung Quatremère's (Tazi als Nisbe von Tai) ist indess auch nach Nöldeke's Meinung die richtige.' Horn cites the tāj derivation only to reject it.\"},\n            {\"ref\": \"BQT:458\", \"status\": \"contradicts\", \"note\": \"BQT_v1_pages.txt scan page 684 (= printed 458, by the offset fixed from BQT:472 = scan 698): Mo'in's footnote '... تاژیک می‌گفتند، و سپس این اطلاق را بهمهٔ عرب تعمیم دادند، چنانکه یونانیان و رومیان ... و عرب فرس را بهمهٔ ایرانیان اطلاق کردند'; the facing entry (scan 685) glosses تاجیک 'است که غیر عرب و ترک باشد' with the cross-reference 'رک: تازی و تاجیک'. The tribal/ethnonymic route, not tāj.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 82-83 s.v. Tāzīg\", \"stance\": \"contradicts\", \"note\": \"'1Tāzig [tʾcyk\\\\' | N tāzi] swift, fast. 2Tāzig [tʾcyk\\\\' | N tāzi] Arab.' — the Middle Persian ethnonym already has -z-, i.e. it cannot come from tāg/tāj.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi, s.v. تاجیک and تازیک (= MON:996)\", \"stance\": \"contradicts\", \"note\": \"'تاجیک: [- تاجک > تازیک (به یک معنی) - تاژیک، تر. تات (رعیت) + چیک (پس. تصغیر و تحقیر)] غیر ترک (عموماً)، آنکه ترک و مغولی نباشد، ایرانی (خصوصاً) ... صح: «تاجیک» با «تازی» (= تازیک به معنی عرب) فرق دارد.' and 'تازیک: [- تاجیک - تاژیک] (ص.) غیر ترک، ایرانی؛ ج. تازیکان.' Confirms Nourai's own NOTE that MON derives tājīk from Turkic tāt — and shows Mo'in keeps tājīk apart from tāj entirely.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"tâj-var «تاجور»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"تاجور tāj-var 'crown-bearer, crowned head, king' is a transparent Persian compound: تاج tāj + the productive possessive/agent suffix -var (also -war), New Persian continuant of Middle Persian -war < Old Iranian *-bara- 'bearing, carrying' (from PIE *bher- 'to carry'), the same suffix as in نامور nām-var 'name-bearing, famous', پیشه‌ور pīše-var, سخنور soxan-var. Nourai's cross-reference '☞ Bher 1' for the second element is therefore correct. The Armenian calque թագաւոր tʻagavor 'king' (= tʻag 'crown' + -vor), already Arsacid-period, shows the compound type is old in Iranian and is cited by Horn in the same entry as tāj. Mo'in's lexicon (the page Nourai cites, MON:996, which also carries تاجیک) glosses it exactly as the chart does. The verdict for the compound is independent of the open question about the ultimate origin of tāj itself (node 3).\",\n          \"derivation_fa\": \"«تاجور» ترکیبی شفاف و کاملاً فارسی است: «تاج» + پسوند ـوَر (ـوار)، بازماندهٔ فارسی میانهٔ -war از ایرانی باستان ‎*-bara-‎ «برنده، دارنده» (از ریشهٔ هندواروپایی *bher- «بردن») — همان پسوندی که در «نامور»، «سخنور» و «پیشه‌ور» دیده می‌شود. بنابراین ارجاع نورایی به «☞ Bher 1» برای جزء دوم درست است. گواه کهنگی این الگو، گَرته‌برداری ارمنی թագաւոր tʿagavor «شاه» (tʿag «تاج» + -vor) است که از روزگار اشکانی به کار رفته و هرن آن را در همان مدخل «تاج» آورده است. معنی‌ای که معین می‌دهد («دارای تاج یا افسر، پادشاه، سلطان») درست همان است که نمودار آورده. ادعای نورایی در این گره درست است — هرچند پرسشِ بازِ خاستگاه خودِ «تاج» (گرهٔ ۳) بر جای می‌ماند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AC\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:996\", \"status\": \"supports\", \"note\": \"MON_part1.txt line 36433: 'تاجور: (ص مر.) دارای تاج یا افسر، پادشاه، سلطان.' The entry sits two lines above تاجیک, the entry Nourai also cites as MON:996 in the node-4 note, so the page number is internally consistent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 367, p. 81\", \"stance\": \"supports\", \"note\": \"'täj \\\"Krone\\\", täjver, arm. LW. t'ag, t'agavor.' Horn lists tājvar as a derivative of tāj and pairs it with Armenian tʻagavor 'king'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, suffix -war\", \"stance\": \"supports\", \"note\": \"MacKenzie's dictionary has the productive MP formant -war 'bearing, having' (e.g. in compounds), the direct antecedent of NP -var < OIr. *-bara-.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"tiara\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Greek τιάρα / τιάρας tiára 'the upright felt head-dress of the Persian king and nobles' is genuinely an Iranian culture-word: it first appears in fifth-century Attic authors describing the Achaemenid court (Aeschylus, Persians; Herodotus 1.132, 7.61; Xenophon, Cyropaedia) and never had a Greek etymology. That much supports the direction of Nourai's arrow (Iran → Greece). What is not supportable is the specific source form: Persian tāj is not attested before the Parthian/Middle Persian period (Parthian *tāg), the Greek word has an -r- that tāj cannot supply, and no Old Persian *tiyāra- is attested. Modern reference works therefore leave the immediate donor open — Klein: 'L. tiara, fr. Gk. tiara, which is of Oriental origin'; Etymonline: 'from Greek tiara, a word of Oriental origin', originally 'turban-like head-dress of the Persian kings'; Beekes likewise treats it as a foreign word, evidently Iranian, without a source form. So the chart's picture is compatible with, but more precise than, the evidence. Nourai's two references (Partridge p.719, Shipley p.358) are lending-only on archive.org and could not be read.\",\n          \"derivation_fa\": \"یونانی τιάρα tiára «کلاه بلند نمدی شاه و بزرگان پارسی» به‌راستی وام‌واژه‌ای فرهنگی از ایران است: نخستین بار در سدهٔ پنجم پیش از میلاد نزد آیسخولوس (پارسیان)، هرودوت و گزنفون در وصف دربار هخامنشی می‌آید و هیچ‌گاه ریشه‌شناسی یونانی نداشته است؛ تا اینجا جهت پیکان نورایی (ایران ← یونان) درست است. آنچه پشتوانه ندارد صورت دقیق مبدأ است: «تاج» پیش از دورهٔ پارتی/فارسی میانه گواهی نشده (پارتی tāg)، و ـr واژهٔ یونانی را «تاج» به دست نمی‌دهد، و صورت پارسی باستان *tiyāra- هم گواهی ندارد. از این‌رو کلاین می‌نویسد «از یونانی tiara که خاستگاه شرقی دارد»، اتیمونلاین «واژه‌ای با خاستگاه شرقی»، و بیکس آن را وام‌واژه‌ای بی‌گمان ایرانی اما بی‌مبدأِ شناخته می‌داند. پس ادعای نورایی با احتیاط پذیرفتنی است. دو مأخذ خودِ او (پارتریج ص ۷۱۹ و شیپلی ص ۳۵۸) فقط امانی‌اند و خوانده نشدند.\",\n          \"sources\": [\"https://www.etymonline.com/word/tiara\"],\n          \"ref_check\": [\n            {\"ref\": \"PRT:719\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958): all archive.org copies (originsshortetym00part etc.) are lending-restricted; no readable copy online, no local file.\"},\n            {\"ref\": \"SHP:358\", \"status\": \"not_checked\", \"note\": \"Shipley, Dictionary of Word Origins (1945): archive.org copies lending-only; the HathiTrust full-view id given in refs_online.json was not reachable in this session.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1618 s.v. tiara (KLN_1966.txt leaf 856)\", \"stance\": \"partial\", \"note\": \"'tiara, n., head dress. — L. tiara, fr. Gk. tiara, which is of Oriental origin.' Klein affirms the Oriental origin but names no Iranian word, and does not link it to his own taj/stemma entry.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch, grep 'Tiara', 'Tadsch'\", \"stance\": \"silent\", \"note\": \"Lokotsch's dictionary of European words of Oriental origin has no Tiara entry (only the unrelated ar. itiarad at no. 1404) — he treats the word as classical rather than as a mediaeval Orientalism.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1 only\", \"stance\": \"silent\", \"note\": \"T is in vol. 2, which is not in the local library.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"tiara, tire, attire\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Only the first of the three belongs here. ENGLISH TIARA is confirmed: Latin tiāra (Vulgate, of the high priest's mitre) > English tiar (1510s), tiara (1550s) 'head-dress of the Persian kings / papal triple crown', then from the 1650s 'jewelled headband'. ATTIRE and TIRE are unrelated to the Greek word: attire is Middle English atiren, from Old French atirier 'to equip, put in order, dress', a compound of a- (< Latin ad- 'to') + tire 'order, row, rank, dress', itself of Germanic (Frankish) origin, cognate with Old English tīr and German Zier; the noun tire 'equipment, dress, covering, trappings of a knight' (c. 1300, tir) is an aphetic shortening of attire, and the wheel-band sense (15th c.) is a figurative use of that noun — 'the clothing of a wheel'. Etymonline's entry for attire makes no mention of tiara at any point. The resemblance tiara ~ tire is accidental and Nourai's arrow #6 → #7 is a folk etymology for two of its three words; hence the worst verdict governs the node.\",\n          \"derivation_fa\": \"از سه واژهٔ این جعبه تنها اولی به اینجا تعلق دارد. «tiara» انگلیسی درست است: از لاتینی tiāra (در ولگات برای تاج کاهن اعظم) به انگلیسی tiar (دههٔ ۱۵۱۰) و tiara (دههٔ ۱۵۵۰) و از میانهٔ سدهٔ هفدهم به معنی «نیم‌تاج جواهرنشان». اما attire و tire هیچ پیوندی با واژهٔ یونانی ندارند: attire از فرانسهٔ کهن atirier «آراستن، ساز و برگ دادن» است، مرکب از a- (از لاتینی ad-) و tire «رده، نظم، جامه» که خود ریشهٔ ژرمنی (فرانکی) دارد؛ و اسم tire «ساز و برگ و جامهٔ شوالیه» (حدود ۱۳۰۰م، tir) کوتاه‌شدهٔ همان attire است و معنی «رویهٔ چرخ» (سدهٔ پانزدهم) کاربردی مجازی از آن است («جامهٔ چرخ»). اتیمونلاین در سراسر مدخل attire هیچ اشاره‌ای به tiara ندارد. شباهت tiara و tire تصادفی است و پیکان ۶ ← ۷ برای دو واژه از سه واژه ریشه‌شناسی عامیانه است؛ پس بدترین حکم بر کل گره حاکم می‌شود.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/attire\",\n            \"https://www.etymonline.com/word/tiara\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PRT:358\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958), p. 358: lending-only on archive.org; not readable. (Note also that Nourai cites PRT:719 for the Greek parent and PRT:358 for the English children — Partridge's own 'tiara' article can only be at one of the two.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1618 s.v. tiara; attire/tire entries\", \"stance\": \"contradicts\", \"note\": \"Klein's tiara comes 'fr. Gk. tiara ... of Oriental origin' with no reference to attire or tire, which he treats under the Old French atirier family; no cross-reference joins them.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. attire/tire\", \"stance\": \"contradicts\", \"note\": \"Skeat likewise takes attire from OF. atirer (a- + tire 'row, rank'), and tire as a shortening of attire — never from Greek tiara.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"tâyer «تایر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian تایر tāyer 'the rubber tyre of a wheel' is a twentieth-century loan taken straight from English tire/tyre with the motor car, transcribed with alef-ye-re; Mo'in's lexicon tags it '[انگ.]' (English) and glosses it 'لاستیک رویی چرخ وسایل نقلیه', noting the variant spelling طایر — i.e. the borrowing as drawn (English #7 → Persian) is correct. What is not correct is Nourai's gloss: the page prints 'tāyer: tire,\\\", \\\"wheel crown\\\"' (the stray quotation marks are in the book), and 'wheel crown' is his own harmonization, meant to make the loan look like a return of tāj 'crown'. Since English tire is not from tiara/tāj (see node 7), this word is not a Persian round trip at all but an ordinary modern Anglicism.\",\n          \"derivation_fa\": \"«تایر» وام‌واژه‌ای است از انگلیسی tire/tyre که در سدهٔ بیستم همراه با خودرو وارد فارسی شد. معین آن را با برچسب «[انگ.]» می‌آورد و «لاستیک رویی چرخ وسایل نقلیه» معنی می‌کند و صورت املایی «طایر» را نیز یاد می‌کند؛ پس خودِ وام‌گیری (انگلیسی ← فارسی) که نمودار کشیده درست است. آنچه درست نیست معنایی است که نورایی افزوده: در کتاب «tire,\", \"wheel crown\"» چاپ شده و «تاجِ چرخ» ساختهٔ خود اوست تا این وام‌واژه شبیه بازگشتِ «تاج» فارسی جلوه کند. چون tire انگلیسی از tiara/تاج نیامده (گرهٔ ۷)، این واژه اصلاً وام‌واژهٔ دورگَرد نیست، بلکه انگلیسی‌گرایی معمولیِ امروزی است.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%AA%D8%A7%DB%8C%D8%B1/\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1014\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi s.v. تایر (read via abadis.ir, section فرهنگ معین): '(یِ) [انگ.] (اِ.) = طایر: لاستیک رویی چرخ وسایل نقلیه' — the origin tag [انگ.] is exactly the English source the chart draws; p. 1014 is 18 pages after MON:996 (تاجور/تاجیک), which is consistent with the alphabetical distance تاجور → تایر.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AMD\", \"where\": \"Farhang-e Amid s.v. تایر (abadis.ir)\", \"stance\": \"supports\", \"note\": \"'لاستیک رویی چرخ اتومبیل، موتورسیکلت، دوچرخه، و مانند آن' — same meaning, a modern technical term with no native Persian pedigree.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā-ye hend-o-orupāyi\", \"stance\": \"silent\", \"note\": \"A modern Anglicism of this kind is outside the scope of Aryanpur's Indo-European-root dictionary; no entry.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Hindustani\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box in the printed chart (the page shows a 'Hindustani' header with no word under it), standing for Hindustani/Urdu تاج ~ ताज tāj 'crown', borrowed from Persian, the court and chancery language of the Delhi Sultanate and the Mughal empire, along with the rest of the royal vocabulary (šāh, mahal, dīvān). The extraction is faithful to the book. From this Hindustani word the compound of node 10 is formed.\",\n          \"derivation_fa\": \"این جعبه در خودِ کتاب خالی چاپ شده است (تنها سرنویس «Hindustani» بی هیچ واژه‌ای) و نمایندهٔ «تاج» هندوستانی/اردو ताज ~ تاج است که همراه با دیگر واژگان درباری (شاه، محل، دیوان) از فارسی — زبان دیوان و دربار سلطنت دهلی و گورکانیان هند — وام گرفته شده. خوانش اسکن با صفحهٔ چاپی مطابق است. ترکیب گرهٔ بعدی از همین واژهٔ هندوستانی ساخته شده است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Taj_Mahal\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (empty box, refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. TAJ (HJB.txt leaf 932, printed ~p. 885)\", \"stance\": \"supports\", \"note\": \"'TAJ, s. Pers. tāj, \\\"a crown.\\\" The most famous and beautiful mausoleum in Asia; the Tāj Mahal at Agra ...' — Yule & Burnell label the Anglo-Indian word as Persian, taken over in India.\"},\n            {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary\", \"stance\": \"silent\", \"note\": \"grep for 'taj' in AID.txt returns no headword; Whitworth omits it.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"Taj Mahal\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Taj Mahal comes through Anglo-Indian usage from Hindustani/Urdu تاج محل tāj mahal 'crown of palaces', a Persian(-Arabic) phrase: tāj 'crown' + Arabic-in-Persian maḥall 'place, residence, palace' (Arabic root ḥ-l-l 'to alight, settle'). The building is the mausoleum Shah Jahan raised at Agra (begun 1631) for his wife Arjumand Bānū Begum, titled Mumtāz Maḥall 'the chosen one of the palace', and the monument's name is generally taken as a contraction of her title as much as a description; Yule & Burnell give exactly this. Nourai's gloss 'royal place (palace)' is loose — the phrase is 'crown of palaces' / 'crown palace' — but the derivation from tāj is right.\",\n          \"derivation_fa\": \"«Taj Mahal» انگلیسی از راه کاربرد انگلیسی‌ـ‌هندی و از هندوستانی/اردو «تاج محل» آمده است؛ عبارتی فارسی‌ـ‌عربی: «تاج» + «محلّ» عربی («جای فرود آمدن، اقامتگاه، کاخ» از ریشهٔ ح‌ل‌ل). این بنا آرامگاهی است که شاه‌جهان از ۱۰۴۰ق/۱۶۳۱م در آگره برای همسرش ارجمندبانو بیگم ملقّب به «ممتاز محل» ساخت، و نام بنا را هم کوتاه‌شدهٔ همان لقب و هم وصفِ «تاجِ کاخ‌ها» دانسته‌اند؛ یول و برنل در Hobson-Jobson دقیقاً همین را می‌گویند. معنایی که نورایی داده («جای شاهانه، کاخ») دقیق نیست — عبارت یعنی «تاج کاخ‌ها» — اما اشتقاق آن از «تاج» درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Taj_Mahal\"],\n          \"ref_check\": [\n            {\"ref\": \"PRT\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins: lending-only on archive.org; the citation carries no page in the book either.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. TAJ (leaf 932, printed ~p. 885) and s.v. MEHAUL\", \"stance\": \"supports\", \"note\": \"'TAJ, s. Pers. tāj, \\\"a crown.\\\" The most famous and beautiful mausoleum in Asia; the Tāj Mahal at Agra, erected by Shah Jahan over the burial-place of his favourite wife Mumtāz-i-Mahal (\\\"Ornament of the Palace\\\") Bānū Begam.' The MEHAUL entry adds 'The sing. mahall ... is often used for a palace or important edifice, e.g. (see SHISH-MUHULL, TAJ-MAHAL).'\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 p. 1566 s.v. taj\", \"stance\": \"supports\", \"note\": \"'taj, \\\"crown\\\", fr. Pers. taj, of s.m. See stemma.' Klein lemmatizes the English word and makes it Persian.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Germanic\",\n          \"words\": \"thakjan : to cover; thakam : roof\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *þakjaną 'to cover' and *þaką 'roof, thatch' are the regular reflexes of the o-grade *tog- of *(s)teg- (Grimm's law: PIE *t > PGmc *þ, PIE *g > PGmc *k). The verb gives OE þeccan, OS thekkian, ON þekja, OHG decchen/decken, Du. dekken; the neuter noun gives OE þæc, ON þak, Swed. tak, Dan. tag, OFris. thek, Du. dak, OHG dah, G. Dach. Nourai's spellings 'thakjan / thakam' are Watkins's transcriptions (th- for þ, -am for the neuter *-an stem) copied verbatim from the AHD appendix.\",\n          \"derivation_fa\": \"ژرمنی آغازین *þakjaną «پوشاندن» و *þaką «بام، پوشش بام» بازتاب قانونمند درجهٔ o ریشه یعنی *tog- هستند: بنا بر قانون گریم، ‎*t‎ هندواروپایی به *þ و *g به *k بدل می‌شود. از فعل: انگلیسی باستان þeccan، ساکسون باستان thekkian، نورس باستان þekja، آلمانی علیای باستان decchen/decken، هلندی dekken؛ و از اسم خنثی: انگلیسی باستان þæc، نورس þak، سوئدی tak، دانمارکی tag، هلندی dak، آلمانی Dach. صورت‌نویسی «thakjan / thakam» در نمودار همان نویسهٔ واتکینز در پیوست AHD است که نورایی عیناً نقل کرده. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1013\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. (s)teg-1: 'Old Icelandic þekja \\\"cover\\\", Old English þeccan \\\"cover\\\", Old High German decchen \\\"cover\\\" ... Old Icelandic þak, Old English dæc [þæc], Old High German dah \\\"roof\\\" ...'\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1007: 'I. O-grade form *tog-. 1. Germanic *thakjan in: a. Old English theccan, to cover: THATCH; b. Middle Dutch dekken, to cover: DECK; c. Old High German decchen, to cover: DECKLE. 2. Germanic *thakam in Middle Dutch dec, decke, roof, covering: DECK.' — Nourai's two forms verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1600 s.v. thatch\", \"stance\": \"supports\", \"note\": \"'thatch, tr. v. — ME. thecchen, thacchen, fr. OE. þeccan, \\\"to cover\\\", rel. to OS. thekkian, ON. þekja, Swed. täcka, Dan. dække, OFris. thekka, MDu. decken, Du. dekken, OHG. decchen ... and to OE. þæc \\\"roof, thatch\\\", ON. þak, Swed. tak, Dan. tag ... OHG. dah, G. Dach \\\"roof\\\", fr. I.-E. [base *(s)teg-]'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. togos\", \"stance\": \"supports\", \"note\": \"IEC.txt 18699: 'togos, ā, io \\\"cover, covering, roof, thatch\\\". WP II, 621. ... OHG dach, n., OE þac, n.; ON þak, n. \\\"roof\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"thatch : foliage used for building roofs; deck\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"THATCH: Middle English thecchen/thacchen < Old English þeccan 'to cover' (< PGmc *þakjaną); the noun thatch 'roof-covering of straw or reeds' is from the related OE þæc. The modern noun sense the chart glosses ('foliage used for building roofs') is the ordinary one. DECK: not inherited but borrowed — Middle Dutch dec, decke 'roof, covering' (from dekken 'to cover', the Dutch reflex of the same *þakjaną), taken into English in the 15th century as a nautical term, partly through German verdeck 'covering (of a ship)', a loan-translation of Italian coperta / Middle French couverte. So thatch is the native member and deck the Low-German/Dutch loan of the same Germanic etymon; both correctly under node 11.\",\n          \"derivation_fa\": \"«thatch»: از انگلیسی میانه thecchen/thacchen و انگلیسی باستان þeccan «پوشاندن» (از ژرمنی *þakjaną)؛ اسم آن («پوشش کاه‌گلی یا نی‌ای بام») از þæc انگلیسی باستان است. اما «deck» واژه‌ای موروثی نیست بلکه وام‌واژه است: از هلندی میانه dec/decke «بام، پوشش» (از فعل dekken، صورت هلندیِ همان *þakjaną) که در سدهٔ پانزدهم به‌عنوان اصطلاح دریانوردی وارد انگلیسی شد، تا اندازه‌ای به میانجی آلمانی Verdeck «پوشش کشتی» که خود گرته‌برداری از ایتالیایی coperta است. پس thatch عضو بومی و deck وام‌واژهٔ آلمانی پست/هلندیِ همان ستاک ژرمنی است؛ هر دو به‌درستی زیر گرهٔ ۱۱ نشسته‌اند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1007 lists both under (s)teg-: 'Old English theccan, to cover: THATCH' and 'Germanic *thakam in Middle Dutch dec, decke, roof, covering: DECK'. The index line 1416 confirms 'DECK1 (s)teg- DECK2 (s)teg-', line 2366 'THATCH (s)teg-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 410 s.v. deck; p. 1600 s.v. thatch\", \"stance\": \"supports\", \"note\": \"'deck, n., covering (obsol.) — MDu. decke, dek, (Du. dek), \\\"roof, covering\\\", fr. decken, \\\"to cover\\\". See deck, v.'; 'deck, n., covering of a ship. — Shortened fr. G. verdeck ... lit. \\\"covering\\\" (see for- and thatch ...), and prop. a loan translation of OIt. (= It.) coperta or MF. couverte.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. thatch, deck\", \"stance\": \"supports\", \"note\": \"Skeat likewise derives thatch from OE þeccan/þæc and deck from Dutch dek 'covering'.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Latin\",\n          \"words\": \"tegere : to cover; tegula : tile\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin tegō, tegere, tēxī, tēctum 'to cover' is the textbook representative of the bare e-grade *teg- (without s-mobile), matching Greek stégō exactly; its derivatives tēctum 'roof', teges 'mat, covering', tegumentum/tegmen 'covering', tignum 'roof-beam' and the diminutive-like tēgula 'roof tile' (> It. tegola, Fr. tuile) are all in Pokorny's material under this lemma. Nourai's two head-forms and their glosses are exactly the ones Watkins prints ('Latin tegere, to cover, and tegula, tile').\",\n          \"derivation_fa\": \"لاتینی tegō/tegere «پوشاندن» نمایندهٔ کلاسیک درجهٔ e ریشه بی‌s است و دقیقاً با yونانی stégō برابر می‌افتد؛ مشتقات آن tēctum «بام»، teges «حصیر، پوشش»، tegmen/tegumentum «پوشش»، tignum «تیر بام» و tēgula «سفال بام» (که ایتالیایی tegola و فرانسهٔ tuile از آن است) همگی در مادهٔ همین مدخل پوکورنی آمده‌اند. دو صورت سرنویسِ نورایی و معنای آن‌ها عیناً همان است که واتکینز چاپ کرده. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1007: 'III. Basic form *teg-. 1. Latin tegere, to cover, and tegula, tile: TECTRIX, TECTUM, TEGMEN, TEGMENTUM, TEGULAR, TEGUMENT, TILE, TUILLE; DETECT, INTEGUMENT, OBTECT, PROTECT.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 1013 s.v. (s)teg-1\", \"stance\": \"supports\", \"note\": \"'Latin tego, -ere \\\"cover\\\", tectum \\\"roof\\\" (= stektos), tegulum \\\"cover, roof, wrapping\\\", teges, -etis \\\"cover, mat\\\", tegula \\\"a roof tile\\\", toga ...; Umbrian tehtenm.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, LAT.txt line 63201\", \"stance\": \"supports\", \"note\": \"'tego, -is, texi, tectum, -ere: couvrir, recouvrir; d'où, garan[tir] ...' — Ernout-Meillet's headword confirms the verb and its family.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. tegos\", \"stance\": \"supports\", \"note\": \"IEC.txt 18253: 'tegos ... Lat. cf. teges, gs: tegetis, f. \\\"rug, mat\\\"; tignum, n. \\\"roof-beam\\\" ...; tectum \\\"roof, home\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"English\",\n          \"words\": \"tile, toga, detect, protect\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four go back to Latin tegere/tegula. TILE: Old English tigele/tigule, an early (Roman-period) borrowing of Latin tēgula, shared with OS tiegla, ON tigl, OHG ziagala > G. Ziegel. TOGA: Latin toga 'the Roman citizen's woollen wrap', literally 'a covering', from the suffixed o-grade *tog-ā, adopted into English in the 16th century. DETECT: Latin dētegere 'to uncover, lay bare' (dē- 'un-, off' + tegere), pp. dētēctus, English from the 15th century. PROTECT: Latin prōtegere 'to cover in front, shield' (prō- 'in front' + tegere), pp. prōtēctus. Watkins lists TILE, TUILLE, TOGA, DETECT, OBTECT, INTEGUMENT and PROTECT under this root.\",\n          \"derivation_fa\": \"هر چهار واژه به tegere/tegula لاتینی بازمی‌گردند. «tile»: انگلیسی باستان tigele/tigule، وامی کهن (دورهٔ رومی) از لاتینی tēgula، همانند ziagala آلمانی علیای باستان (> Ziegel). «toga»: لاتینی toga «ردای پشمی شهروند رومی»، لفظاً «پوشش»، از صورت پسوندیِ درجهٔ o یعنی *tog-ā، که در سدهٔ شانزدهم وارد انگلیسی شد. «detect»: از لاتینی dētegere «روپوش برداشتن» (پیشوند dē- + tegere). «protect»: از لاتینی prōtegere «پیشِ چیزی را پوشاندن، پناه دادن» (پیشوند prō- + tegere). واتکینز همهٔ این‌ها را زیر همین ریشه فهرست کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1007 (root entry) and the reverse index: line 2389 'TILE (s)teg-', line 2395 'TOGA (s)teg-', line 1420 'DETECT (s)teg-', line 2138 'PROTECT (s)teg-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 leaf 857 s.v. tile; leaf 860 s.v. toga\", \"stance\": \"supports\", \"note\": \"'tile, n. — ME., fr. OE. tigele, tigule, which, together with OS. tiegla, ON. tigl, Dan. tegl, Swed. tegel, MDu. tegel, OHG. ziagala ... derives fr. L. tegula (whence also It. tegola, F. tuile), which is rel. to tegere, \\\"to cover\\\".'; 'toga, n. — L. toga, \\\"a garment\\\", lit. \\\"a covering\\\", in gradational relationship to tegere, \\\"to cover\\\".'\"},\n            {\"src\": \"POK\", \"where\": \"IEW 1013\", \"stance\": \"supports\", \"note\": \"Pokorny lists 'tegula \\\"a roof tile\\\", toga \\\"the white woolen upper garment worn by Roman citizens\\\"' under (s)teg-1.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Old Irish\",\n          \"words\": \"tech : house\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Irish tech (also teg), gen. tige, 'house' is an s-stem neuter that corresponds formally to Greek τέγος tégos 'roof, house' — Pokorny notes the equation explicitly ('Old Irish tech, neutraler -es-stem = gr. tégos'). It continues Proto-Celtic *tegos < PIE *teg-os- 'covering, roof'. Its Brittonic cognates are Old Welsh tig, Welsh tŷ, Cornish ty/chy, Old Breton -tig in bou-tig 'cowshed'; the Irish compound teg-lach 'household' and Welsh teulu 'family' (< *tego-slougo- 'house-troop') belong here too. Modern Irish teach/tigh continues it and is the form used in node 16.\",\n          \"derivation_fa\": \"ایرلندی باستان tech (نیز teg)، اضافی tige، «خانه»، اسمی خنثی با ستاک s است و صورتاً با یونانی τέγος tégos «بام، خانه» برابر می‌افتد؛ پوکورنی خود این برابری را می‌آورد. این واژه دنبالهٔ سلتی آغازین *tegos از هندواروپایی *teg-os- «پوشش، بام» است. هم‌ریشه‌های برایتونی‌اش: ولزی باستان tig، ولزی tŷ، کرنوالی ty/chy، و برتون باستان ‎-tig‎ در bou-tig «گاوخانه»؛ ترکیب‌های teg-lach «اهل خانه» در ایرلندی باستان و teulu «خانواده» در ولزی (از *tego-slougo- «گروهِ خانه») نیز از همین‌جایند. صورت ایرلندی امروزی teach/tigh همین واژه است که در گرهٔ ۱۶ به کار رفته. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"The Watkins appendix entry for (s)teg- (AHD_watkins1985.txt line 1007) does NOT list Old Irish tech — Watkins cites only the Germanic, Latin, Greek and Persian branches plus Skt. sthagayati. The Celtic member is in the main-dictionary etymology for SHANTY, which the next nodes cite (AHD:1191); for the root itself Pokorny has to be used.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 1013 s.v. (s)teg-1\", \"stance\": \"supports\", \"note\": \"'Old Irish tech (neutraler -es-stem = gr. tégos), acymr. tig, ncymr. ty, acorn. ti \\\"house\\\", abret. bou-tig \\\"cowshed\\\" ...; Pl. acymr. te, ncymr. tai, also in Old Irish teg-lach \\\"Hausgenossenschaft\\\", cymr. teulu, acorn. tellu \\\"family\\\" (*tego-slougo-).'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. tegos (IEC.txt 18253)\", \"stance\": \"supports\", \"note\": \"'OIr. teg, gs: & npl. tige, m. \\\"house\\\"; Mir. teg & tech, m. id. ...; Ir. tigh & teach, gs. & npl. tighe, m. \\\"house\\\"; OBr. tig-, id. (fr. *tegus); Br. ti, Cor. ty & chy, m. id.; W ty, pl. tai ...'\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Irish\",\n          \"words\": \"sean tig : old house\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Irish phrase itself is unobjectionable in its parts: sean 'old' (< Proto-Celtic *senos, PIE *sen- 'old') + tigh/teach 'house', the modern continuant of Old Irish tech, so the arrow #15 → #16 is formally fine (the dative/oblique tigh is the usual form in such phrases). But the phrase exists in the etymological literature only as the alleged source of English shanty; it is not an ordinary Irish lexical item, and the spelling 'sean tig' is the one that circulates in nineteenth-century English dictionaries rather than standard Irish (seantigh / sean teach). Since the whole node is there only to feed node 17, and that derivation is now rejected (see node 17), the node is credited as plausible: real words, real descent from tech, but a phrase quoted for a purpose modern lexicography no longer accepts.\",\n          \"derivation_fa\": \"خودِ این عبارت ایرلندی از نظر اجزا ایرادی ندارد: sean «کهنه، پیر» (از سلتی آغازین *senos، هندواروپایی *sen-) + tigh/teach «خانه»، دنبالهٔ امروزی tech ایرلندی باستان؛ پس پیکان ۱۵ ← ۱۶ از نظر صوری درست است (صورت tigh همان حالت غیرفاعلی است که در چنین ترکیب‌هایی می‌آید). اما این عبارت در ادبیات ریشه‌شناسی تنها به عنوان مبدأ ادعایی واژهٔ انگلیسی shanty وجود دارد، نه به عنوان مدخلی معمول در واژگان ایرلندی، و املای «sean tig» همان صورتی است که در فرهنگ‌های انگلیسی سدهٔ نوزدهم می‌گردد نه املای معیار ایرلندی (seantigh / sean teach). چون تمام کارکرد این گره تغذیهٔ گرهٔ ۱۷ است و آن اشتقاق امروز رد شده، حکم «با احتیاط پذیرفتنی است» را می‌گذاریم.\",\n          \"sources\": [\"https://www.ahdictionary.com/word/search.html?q=shanty\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1191\", \"status\": \"not_checked\", \"note\": \"The 1975 New College edition (the printing Nourai cites, main-dictionary p. 1191, 'sh-' range) is lending-restricted on archive.org and in-book search was not reachable; only the appendix (Watkins) is on disk. The current AHD online s.v. shanty gives ONLY 'Probably from Canadian French chantier ...' and does not mention Irish sean tig, so whatever the 1975 printing said has been withdrawn in later editions.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 1013\", \"stance\": \"partial\", \"note\": \"Pokorny confirms the descent of the modern Irish word ('Old Irish tech ... Ir. tigh & teach') but says nothing about any phrase sean tig.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. tegos\", \"stance\": \"partial\", \"note\": \"'Ir. tigh & teach, gs. & npl. tighe, m. \\\"house\\\"' — the second element of the phrase is confirmed as the Old Irish word's continuant; the compound is not lexicalized in Mann.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"English\",\n          \"words\": \"shanty : cabin\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"English shanty 'crudely built cabin' is first recorded in North America c. 1820 (Canadian and northern-US lumbering contexts). The Irish etymology the chart draws — shanty < Irish sean tig 'old house' — was popular in nineteenth-century dictionaries and survived into the 1969/1975 American Heritage, which is why Nourai cites AHD:1191; but it is now rejected on both formal and historical grounds (the word appears first in French-Canadian logging country, not in Irish-settled areas, and Irish tigh would not give -ty). The standard modern account derives it from Canadian French chantier 'hut in a lumber camp, lumberjack's headquarters', from French chantier 'timber-yard, dock', Old French chantier 'gantry', from Latin cantherius 'rafter, trellis, nag', itself from Greek kanthēlios 'pack-ass'. That is the only etymology given by the current American Heritage Dictionary and by Etymonline. If so, shanty has nothing to do with *(s)teg-.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی shanty «کلبهٔ سرهم‌بندی‌شده» نخستین بار حدود ۱۸۲۰ در آمریکای شمالی (در فضای چوب‌بری کانادا و شمال ایالات متحده) ثبت شده است. اشتقاقی که نمودار کشیده — shanty از ایرلندی sean tig «خانهٔ کهنه» — در فرهنگ‌های سدهٔ نوزدهم رواج داشت و تا ویراست ۱۹۶۹/۱۹۷۵ فرهنگ American Heritage هم مانده بود (و به همین سبب نورایی به AHD:1191 ارجاع داده)، اما امروز هم از نظر آوایی و هم از نظر تاریخی رد شده است: واژه نخست در منطقهٔ چوب‌بری فرانسوی‌زبان کانادا پیدا می‌شود نه در نواحی ایرلندی‌نشین، و tigh ایرلندی هم ‎-ty‎ نمی‌دهد. تبیین معیار امروزی آن را از فرانسهٔ کانادایی chantier «کلبهٔ اردوگاه چوب‌بری» می‌داند، از فرانسهٔ chantier «چوب‌انبار»، فرانسهٔ کهن chantier «چهارچوب»، از لاتینی cantherius «تیر بام» و آن از یونانی kanthḗlios «خرِ بارکش». ویراست کنونی American Heritage و اتیمونلاین تنها همین را می‌آورند. اگر چنین باشد، shanty هیچ پیوندی با ریشهٔ *(s)teg- ندارد؛ پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/shanty\",\n            \"https://www.ahdictionary.com/word/search.html?q=shanty\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1191\", \"status\": \"not_checked\", \"note\": \"1975 New College edition p. 1191 not accessible (lending-restricted, in-book search unavailable). The claim is credible for that printing — the Irish etymology was standard in mid-century American dictionaries — but the CURRENT AHD entry reads: 'Probably from Canadian French chantier, hut in a lumber camp, from French, timberyard, from Old French, gantry, from Latin canthērius, rafter, nag, from Greek kanthēlios, pack ass', with no Irish alternative.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. shanty (current ed.)\", \"stance\": \"contradicts\", \"note\": \"'Probably from Canadian French chantier, hut in a lumber camp ... from Latin canthērius, rafter, nag, from Greek kanthēlios, pack ass.' No mention of Irish sean tig.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein, grep 'shanty'\", \"stance\": \"contradicts\", \"note\": \"Klein likewise takes shanty from Canadian French chantier; he has no entry connecting it to Irish.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"grep for 'shanty' in SKT.txt returns no headword — Skeat's concise edition omits this Americanism.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Stei, Stâi 2\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *steh₂i- / *stāi-, *stī̆- 'to thicken, condense, stiffen' (Pokorny 1010-1011); the gloss 'stone' is the Germanic specialization\",\n      \"note\": \"The root and the page number are right, but the gloss is not Pokorny's. IEW 1010-1011 heads the lemma 'stāi-, stī̆-, sti-ā-, Meaning: to condense, press together', with the note that *steib(h)-/*steip- are extensions of it; its material is Skt. styāyate 'curdles, hardens', Av. stā(y)- 'heap, mass', Gk. stéar 'tallow', stía/stíon 'pebble', Lat. stīria/stilla 'drop', OCS stěna 'wall' and Gothic stains / OE stān 'stone'. 'Stone' is thus the specialized Germanic (and Slavic 'wall') outcome of 'that which has congealed / hardened', not the root meaning. Nourai is copying Watkins, who does head the entry 'stei-. Stone. [Pok. stāi- 1010.]', so the mistake is inherited from AHD rather than invented. Buck states the semantic path explicitly: \\\"'Stone' fr. 'stiff, solid'\\\". Modern reconstruction writes the root *steyh₂- 'to stiffen'. Verdict: plausible — a real root on the right page, glossed by its most famous daughter rather than by itself.\",\n      \"note_fa\": \"ریشه و شمارهٔ صفحه درست است، اما معنایی که نورایی داده معنای پوکورنی نیست. پوکورنی در ص ۱۰۱۰–۱۰۱۱ مدخل را چنین می‌آورد: «stāi-, stī̆-, sti-ā-، معنی: غلیظ شدن، فشرده شدن»، و یادآور می‌شود که *steib(h)- و *steip- گسترش‌های همین ریشه‌اند؛ و مواد آن: سنسکریت styāyate «می‌بندد، سخت می‌شود»، اوستایی stā(y)- «توده، انبوه»، یونانی stéar «پیه»، stía «سنگ‌ریزه»، لاتینی stīria/stilla «قطره»، اسلاوی کهن stěna «دیوار» و گوتی stains «سنگ». پس «سنگ» تخصیص معناییِ شاخهٔ ژرمنی است («آنچه بسته و سخت شده»)، نه معنای خود ریشه. نورایی این معنی را از واتکینز گرفته که سرمدخل را «stei-. Stone. [Pok. stāi- 1010]» نوشته؛ یعنی خطا از AHD به ارث رسیده است. باک راه معنایی را صریح می‌گوید: «\\\"سنگ\\\" از \\\"سخت، جامد\\\"». بازسازی امروزی ریشه را *steyh₂- «سخت شدن» می‌نویسد. حکم: با احتیاط پذیرفتنی است.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:1010\", \"status\": \"partial\", \"note\": \"POK_full.txt: 'Root / lemma: stāi-, stī̆- sti-ā- / Meaning: to condense, press together / Note: in addition steib(h)-, steip- \\\"shaft, pole etc\\\" / Material: Old Indic styāyate \\\"gerinnt, wird hart\\\" ... Avestan stā(y)- \\\"heap, mass\\\"; gr. stéar ... stía f., stíon n. \\\"small stone\\\" ... Gothic stains, Old Icelandic steinn, Old English stān, Old High German stein \\\"stone\\\"; Old Church Slavic stěna \\\"wall\\\" ... Page(s): 1010-1011.' The page is right; the meaning Pokorny gives is 'to condense', not 'stone'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. stei-\", \"stance\": \"supports\", \"note\": \"'stei-. Stone. Suffixed o-grade form *stoi-no- in Germanic *stainaz in: a. Old English stan, stone: STONE; b. Middle Dutch steen, stone: STEENBOK; c. Old Norse steinn, stone: TUNGSTEN; d. Old High German stein, stone, in German Steingut, stoneware: STEIN. [Pok. stāi- 1010.]' — Nourai's gloss and his whole Germanic branch come from this one entry.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 1.44 'STONE; ROCK', §4\", \"stance\": \"supports\", \"note\": \"'Goth. stains, ON steinn, OE stan, OHG stein, etc., the general Gmc. word for \\\"stone\\\" ... : Grk. stia \\\"pebble\\\", stear \\\"stiff, fat\\\", Skt. stya- \\\"stiffen\\\", ChSl. stěna \\\"wall\\\", SCr. stijena \\\"rock\\\", etc. \\\"Stone\\\" fr. \\\"stiff, solid\\\". Walde-P. 2.610 ff.'\"},\n        {\"src\": \"KLN\", \"where\": \"p. 1518 s.v. stone\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *stai-, *stei-, *sti, \\\"to thicken, compress, stiffen; stone\\\"' — Klein's double gloss shows the same situation: the primary sense is 'thicken', with 'stone' appended as the Germanic outcome.\"},\n        {\"src\": \"WLD\", \"where\": \"WP. II 610 f. (cited by Pokorny and by Buck)\", \"stance\": \"supports\", \"note\": \"Pokorny's 'References: WP. II 610 f., WH. II 595' and Buck's 'Walde-P. 2.610 ff.' both point to the same Walde-Pokorny entry; Bd. II of WLD is not in the local library, so this is checked through the two citing works.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"stâ 2, stây : heap\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan stā(y)- m. 'heap, mass' is genuine and is precisely the Iranian witness cited for this root by both of Nourai's references. Bartholomae's Altiranisches Wörterbuch lists 'stā(y)- m. \\\"Haufen, Masse\\\"' with the Yasna passage in which offerings are piled up (A. J. 5). The form belongs to the root's basic sense 'to congeal, pack together' — a 'heap' being what is pressed together — and stands beside Skt. styāyate 'curdles' and Gk. stéar 'congealed fat'. Nourai's '2' distinguishes it from the far commoner Avestan stā- 'to stand' (PIE *steh₂-), a necessary distinction that he makes correctly.\",\n          \"derivation_fa\": \"اوستایی stā(y)- (مذکر) «توده، انبوه» واژه‌ای واقعی است و درست همان گواه ایرانیِ این ریشه است که هر دو مأخذ نورایی به آن استناد کرده‌اند. بارتولومه در فرهنگ ایرانی باستان می‌آورد: «stā(y)- م. \\\"توده، انبوه\\\"» با شاهدی از یسنا که در آن پیشکش‌ها را روی هم می‌انبارند. این صورت به معنای پایهٔ ریشه («بستن، فشرده شدن») تعلق دارد — «توده» همان چیزی است که به هم فشرده شده — و در کنار سنسکریت styāyate «می‌بندد» و یونانی stéar «پیهِ بسته» می‌نشیند. عدد «۲» که نورایی افزوده برای جدا کردن این ریشه از stā- بسیار پربسامدتر اوستایی به معنی «ایستادن» (از *steh₂-) است و به‌درستی به کار رفته. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1010\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. stāi-, stī̆-: 'Avestan stā(y)- \\\"heap, mass\\\"' stands in the material immediately after Skt. styāyate/stimita- and before Gk. stéar.\"},\n            {\"ref\": \"KLN:1518\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 806 (printed pp. 1518-1519), s.v. stone: 'fr. I.-E. base *stai-, *stei-, *sti, \\\"to thicken, compress, stiffen; stone\\\", whence also OI. styayate, \\\"curdles, becomes hard\\\", part. styanah, \\\"curdled\\\", Avestic stā-, stay-, \\\"heap\\\", Gk. stéar, gen. stéatos, \\\"fat, tallow\\\", stia, stion, \\\"pebble\\\", stilē, \\\"drop\\\", L. stiria, stilla, \\\"drop\\\", OSlav. stěna, \\\"wall\\\".' Klein's page is exactly the one cited and it carries exactly Nourai's two Avestan forms.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, BRT.txt line 26723\", \"stance\": \"supports\", \"note\": \"'stā(y)- m. \\\"Haufen, Masse\\\"; ... nəmatą .. vazyāiš (sd.) stāiiasca staoiiehīš ratūš nmānəm frānāsaiiata A. J. 5.' Bartholomae's headword and gloss match the chart's 'stâ 2, stây: heap'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 1.44 §4\", \"stance\": \"partial\", \"note\": \"Buck cites 'Skt. stya- \\\"stiffen\\\"' and Gk. stia for the semantic bridge but does not quote the Avestan noun; Avestan in his stone article is asan-, zarštva- (a different word for 'stone').\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"\",\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"There is nothing to verify: on the printed page (p. 447) this is an empty rectangle drawn to the right of the Avestan box, with no language header, no word and no reference — an unfilled box left in the layout (most likely a New Persian descendant Nourai intended to add and never did; the Avestan branch of this root has no Persian continuant in the chart). The extraction is faithful to the page: the JSON records lang \\\"\\\", words [] and refs null, exactly what the book shows.\",\n          \"derivation_fa\": \"چیزی برای راستی‌آزمایی نیست: در صفحهٔ چاپی (ص ۴۴۷) این گره مستطیلی است کاملاً خالی در سمت راست جعبهٔ اوستایی، بی سرنویس زبان، بی واژه و بی ارجاع — جعبه‌ای پرنشده در صفحه‌آرایی (به احتمال زیاد جای بازماندهٔ یک صورت فارسی نو که نویسنده می‌خواسته بیفزاید و نیفزوده است؛ شاخهٔ اوستاییِ این ریشه در نمودار هیچ دنبالهٔ فارسی ندارد). خوانش اسکن با صفحهٔ چاپی مطابق است: در JSON نیز زبان تهی، فهرست واژه‌ها خالی و ارجاع null ثبت شده — دقیقاً همان که کتاب نشان می‌دهد. پس خطای خوانش اسکن در کار نیست.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Empty box on the printed page; the node carries no reference (refs=None) and no word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 1010-1011\", \"stance\": \"silent\", \"note\": \"Nothing can be looked up for an empty node; Pokorny's Iranian material under this root is limited to the Avestan noun of node 1.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"stainaz : stone; stîfaz : stiff\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"STAINAZ is confirmed: Proto-Germanic *stainaz 'stone' < suffixed o-grade *stoi-no-, giving Gothic stains, ON steinn, OE stān, OS/Du. steen, OHG/G. Stein, Swed./Dan. sten — the equation with OCS stěna 'wall' and SCr. stijena 'rock' fixes the semantics ('that which has congealed/hardened' > 'stone'). STIFAZ is only indirectly here: PGmc *stīfaz 'stiff' (OE stīf, ON stífr, Du. stijf, OHG/G. steif) goes with Latin stīpes 'log, trunk', stīpāre 'to compress', Lith. stiprus 'strong', from the labial extension *steip-/*steib(h)- 'compact, stiff'. Pokorny explicitly treats *steib(h)-/*steip- as an 'in addition' to stāi- rather than as part of it, Klein calls it 'possibly a labial enlargement of base *stei-', and Watkins gives stiff a separate root entry (steip-), not stei-. So the second word sits one derivational step away from the root box as drawn; the node is credited plausible for that reason.\",\n          \"derivation_fa\": \"«stainaz» تأیید می‌شود: ژرمنی آغازین *stainaz «سنگ» از صورت پسوندیِ درجهٔ o یعنی *stoi-no-، که گوتی stains، نورس باستان steinn، انگلیسی باستان stān، هلندی steen، آلمانی Stein و سوئدی/دانمارکی sten از آن است؛ و برابری آن با اسلاوی کهن stěna «دیوار» و صربی stijena «صخره» راه معنایی را روشن می‌کند («آنچه بسته و سخت شده» ← «سنگ»). اما «stîfaz» تنها با یک واسطه به اینجا می‌رسد: ژرمنی *stīfaz «سِفت» (انگلیسی باستان stīf، نورس stífr، هلندی stijf، آلمانی steif) با لاتینی stīpes «کندهٔ درخت» و stīpāre «فشردن» و لیتوانیایی stiprus «نیرومند» می‌پیوندد و از گسترش لبیِ ریشه، *steip-/*steib(h)- «فشرده، سِفت»، می‌آید. پوکورنی این گسترش را «افزون بر» stāi- می‌آورد نه بخشی از آن، کلاین آن را «شاید گسترش لبیِ ریشهٔ *stei-» می‌خواند، و واتکینز برای stiff مدخل جداگانه‌ای (steip-) گذاشته است. پس واژهٔ دوم یک پله دورتر از جعبهٔ ریشه می‌نشیند و از این‌رو حکم گره «با احتیاط پذیرفتنی است».\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teg-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 1009: 'stei-. Stone. Suffixed o-grade form *stoi-no- in Germanic *stainaz in: a. Old English stan, stone: STONE ... c. Old Norse steinn, stone: TUNGSTEN ...' — *stainaz is Watkins's own form, verbatim. But the index (line 2291 ff.) assigns STIFF to steip-, not to stei-, so Nourai's 'stîfaz' is not from the AHD entry he is following here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1514 s.v. stiff; p. 1518 s.v. stone\", \"stance\": \"partial\", \"note\": \"'stiff, adj. — ME. stif fr. OE. stif, rel. to ON. stifr, Du. stijf, OHG., MHG. stif, G. steif, \\\"stiff\\\", and cogn. with L. stipes, \\\"log, stock, trunk of a tree\\\", stipare, \\\"to compress\\\", Lith. stiprus, \\\"strong\\\" ... fr. I.-E. base *steib-, *steibh-, *stib-, *steip-, \\\"compact, stiff\\\", which is possibly a labial enlargement of base *stei-, *sti-, \\\"to thicken, compress, stiffen; stone\\\".' — related, but through an enlargement.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 1010-1011 (Note) and 1015 ff.\", \"stance\": \"partial\", \"note\": \"Pokorny's Note to stāi- reads 'in addition steib(h)-, steip- \\\"shaft, pole etc\\\"', i.e. he keeps the labial extensions as separate lemmata; the bare stāi- entry's Germanic material is only 'Gothic stains, Old Icelandic steinn, Old English stān, Old High German stein \\\"stone\\\"'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 1.44 §4\", \"stance\": \"supports\", \"note\": \"'Goth. stains, ON steinn, OE stan, OHG stein, etc., the general Gmc. word for \\\"stone\\\" ... \\\"Stone\\\" fr. \\\"stiff, solid\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Swedish\",\n          \"words\": \"tung-sten : heavy stone\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Swedish tungsten 'heavy stone' is a transparent modern compound coined in 1780-81 by the Swedish chemist Carl Wilhelm Scheele (1742-86) for the very dense mineral calcium tungstate (later named scheelite). Its second element sten 'stone' is the direct Swedish continuant of PGmc *stainaz, so the arrow #3 → #4 is correct for that half of the compound; the first element tung 'heavy' is a different word (PGmc *þunguz, cf. ON þungr) and does not belong to this root — the chart's single arrow therefore covers only the -sten. When the metal itself was isolated in 1783 by the brothers Juan José and Fausto Elhuyar (from wolframite), the Swedish mineral name was transferred to the element, which is why the element is 'tungsten' in English and French but 'Wolfram' (symbol W) in German and Swedish.\",\n          \"derivation_fa\": \"سوئدی tungsten «سنگِ سنگین» ترکیبی نو و شفاف است که کارل ویلهلم شیله، شیمی‌دان سوئدی، در ۱۷۸۰–۱۷۸۱ برای کانیِ بسیار چگالِ تنگستات کلسیم (که بعدها «شیلیت» نام گرفت) ساخت. جزء دوم آن sten «سنگ» بازماندهٔ مستقیم *stainaz ژرمنی است، پس پیکان ۳ ← ۴ برای همین نیمه درست است؛ اما جزء نخست tung «سنگین» واژهٔ دیگری است (ژرمنی *þunguz، نورس باستان þungr) و به این ریشه تعلق ندارد — یعنی تک‌پیکان نمودار تنها ‎-sten‎ را پوشش می‌دهد. چون خودِ فلز در ۱۷۸۳ به دست برادران الهویار از کانی ولفرامیت جدا شد، نام کانیِ سوئدی به عنصر منتقل شد؛ از این‌روست که این عنصر در انگلیسی و فرانسه «تنگستن» و در آلمانی و سوئدی «Wolfram» (با نماد W) نامیده می‌شود.\",\n          \"sources\": [\"https://www.etymonline.com/word/tungsten\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1381\", \"status\": \"supports\", \"note\": \"The Watkins appendix (AHD_watkins1985.txt line 1009) explicitly routes the English word through this compound: 'c. Old Norse steinn, stone: TUNGSTEN', and the reverse index (line 2420) has 'TUNGSTEN stei-'. AHD:1381 is the main-dictionary page of the 1975 New College edition (the 'tu-' range of a 1550-page volume), which is lending-restricted and could not be opened; the current AHD and Etymonline both give 'Swedish tung heavy + sten stone'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. stei-\", \"stance\": \"supports\", \"note\": \"'Old Norse steinn, stone: TUNGSTEN' — Watkins derives the -sten element from the Scandinavian reflex of *stainaz, as the chart does.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch, grep 'Wolfram', 'Tungsten'\", \"stance\": \"silent\", \"note\": \"A Swedish scientific coinage of 1780 is outside the scope of Lokotsch's dictionary of Orientalisms; no entry.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box in the printed chart, standing for French tungstène (attested from 1783-85 in the chemical literature, with the learned -ène ending of element names, e.g. oxygène, hydrogène). French was the international language of chemistry in the late eighteenth century and is the normal vehicle by which Scheele's Swedish mineral name reached the rest of Europe — and, in the nineteenth and twentieth centuries, the language through which the modern scientific vocabulary entered Persian (Dar al-Fonun and the Iranian Academy took their chemical nomenclature largely from French). The extraction is faithful: the book prints the header 'French' with no word.\",\n          \"derivation_fa\": \"این جعبه در کتاب خالی چاپ شده و نمایندهٔ فرانسهٔ tungstène است (از ۱۷۸۳–۱۷۸۵ در نوشته‌های شیمی، با پسوند عالمانهٔ ‎-ène‎ که در نام عنصرها به کار می‌رود، مانند oxygène و hydrogène). در پایان سدهٔ هجدهم فرانسه زبان بین‌المللی شیمی بود و همان راهی است که نام کانیِ سوئدیِ شیله از آن به سراسر اروپا رسید — و در سده‌های نوزدهم و بیستم همان زبانی است که واژگان علمی نو از راه آن وارد فارسی شد (دارالفنون و فرهنگستان اصطلاحات شیمی را بیشتر از فرانسه گرفتند). خوانش اسکن با صفحه مطابق است: کتاب تنها سرنویس «French» را بی هیچ واژه‌ای چاپ کرده.\",\n          \"sources\": [\"https://www.etymonline.com/word/tungsten\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Empty box; the node carries no reference in the book (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AMD\", \"where\": \"Amid / Dāneš-nāme, s.v. تنگستن (abadis.ir)\", \"stance\": \"supports\", \"note\": \"The Persian entry traces the name to 'عبارتی سوئدی به معنای سنگ سنگین' (a Swedish phrase meaning 'heavy stone') and gives the German-derived alternative ولفرام, i.e. the word reached Persian as an international scientific term, not from Swedish directly.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étym. des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"tungstène is Scandinavian, not Oriental; no entry, as expected.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"tangstan «تنگستن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian تنگستن (tongesten / tangestan) 'tungsten, wolfram' is a twentieth-century scientific loan of the international chemical term, taken through French tungstène / English tungsten, with the Swedish compound's meaning preserved only as a piece of lexicographical information: Persian dictionaries gloss the metal ('فلزی خاکستری، بسیار سخت و دیرگداز') and note that the name is 'عبارتی سوئدی به معنای سنگ سنگین', a Swedish phrase meaning 'heavy stone', exactly the gloss the chart prints in quotation marks. The alternative Persian name ولفرام wolfrām (from German Wolfram) is also current. The word has no Iranian pedigree whatever — it is in the chart only as the modern end-point of the Germanic branch, and as such the derivation is correct.\",\n          \"derivation_fa\": \"«تنگستن» در فارسی وام‌واژه‌ای علمی از سدهٔ بیستم است که از راه فرانسهٔ tungstène / انگلیسی tungsten گرفته شده و معنای تحت‌اللفظی ترکیب سوئدی تنها به عنوان آگاهیِ فرهنگ‌نویسی در آن مانده است: فرهنگ‌های فارسی خودِ فلز را تعریف می‌کنند («فلزی خاکستری، بسیار سخت و دیرگداز») و می‌افزایند که این نام «عبارتی سوئدی به معنای سنگ سنگین» است — دقیقاً همان معنایی که نمودار درون گیومه آورده. نام دیگر آن در فارسی «ولفرام» (از آلمانی Wolfram) است. این واژه هیچ پیشینهٔ ایرانی ندارد و تنها به عنوان نقطهٔ پایانیِ امروزیِ شاخهٔ ژرمنی در نمودار آمده؛ از این حیث اشتقاقی که کشیده شده درست است.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%AA%D9%86%DA%AF%D8%B3%D8%AA%D9%86/\"],\n          \"ref_check\": [\n            {\"ref\": \"AMD:628\", \"status\": \"supports\", \"note\": \"Farhang-e Amid s.v. تنگستن (read via abadis.ir, section فرهنگ عمید): 'فلزی خاکستری، بسیار سخت و دیرگداز که مفتول‌های آن در مقابل کشش و حرارت مقاومت بسیار دارد', with the alternative name ولفرام. Amid's 2-vol. pagination is not mappable to a public scan (refs_online.json: 'page numbers of the 2-vol 1369 print not mappable'), so only the entry, not the page, could be checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in / Dāneš-nāme-ye āzād, s.v. تنگستن (abadis.ir)\", \"stance\": \"supports\", \"note\": \"Traces the name to 'عبارتی سوئدی به معنای سنگ سنگین' — a Swedish phrase meaning 'heavy stone' — and notes the metal's highest melting point; i.e. the borrowed term, not a Persian formation.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā-ye hend-o-orupāyi\", \"stance\": \"silent\", \"note\": \"A modern chemical Europeanism is outside the scope of Aryanpur's Indo-European-root dictionary; no entry.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"stone, tungsten, stiff\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"STONE is confirmed and inherited: ME stan/ston/stoon < OE stān < PGmc *stainaz < *stoi-no-. STIFF is inherited too but, as at node 3, through the labial extension: OE stīf, cognate with Lat. stīpes/stīpāre, from *steip-/*steib(h)-, which Watkins treats as a root of its own. TUNGSTEN is not inherited at all: it is a borrowing of the Swedish compound of node 4, first recorded in English in 1796 for the mineral and later for the element — the chart is right to derive it from Swedish in the upper line, but placing it in an English box hanging from Germanic *stainaz blurs inheritance and borrowing. Hence plausible rather than confirmed: one of the three words is a modern loan and one comes through an extension of the root.\",\n          \"derivation_fa\": \"«stone» موروثی و تأییدشده است: انگلیسی میانه stan/ston از انگلیسی باستان stān از ژرمنی *stainaz از *stoi-no-. «stiff» نیز موروثی است اما — همچون گرهٔ ۳ — از راه گسترش لبی: انگلیسی باستان stīf، هم‌ریشه با لاتینی stīpes/stīpāre، از *steip-/*steib(h)- که واتکینز آن را ریشه‌ای جداگانه می‌داند. اما «tungsten» اصلاً موروثی نیست: وام‌واژه‌ای است از همان ترکیب سوئدیِ گرهٔ ۴ که نخستین‌بار در ۱۷۹۶ در انگلیسی برای کانی و سپس برای عنصر به کار رفته — نمودار در سطر بالا درست آن را از سوئدی گرفته، اما نشاندنش در جعبه‌ای انگلیسی که از *stainaz ژرمنی آویخته است مرز میان وراثت و وام‌گیری را مبهم می‌کند. از این‌رو حکم «با احتیاط پذیرفتنی است»: یکی از سه واژه وام‌واژهٔ امروزی است و یکی از گسترشِ ریشه می‌آید.\",\n          \"sources\": [\"https://www.etymonline.com/word/tungsten\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 1009 gives STONE and TUNGSTEN under stei- (the latter expressly through Old Norse steinn, i.e. as a Scandinavian loan), but the reverse index puts STIFF under steip-, not stei- — so two of the chart's three words are covered by the cited reference and one is not.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1518 s.v. stone; p. 1514 s.v. stiff\", \"stance\": \"partial\", \"note\": \"'stone, n. — ME. stan, ston, stoon, fr. OE. stan, rel. to ON. steinn, Dan. steen, Swed. sten ... Goth. stains, fr. I.-E. base *stai-, *stei-, *sti, \\\"to thicken, compress, stiffen; stone\\\"'; stiff is placed under the enlargement *steib-/*steip-.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 1.44 §4\", \"stance\": \"supports\", \"note\": \"'ME stone; NE stone' listed among the Germanic reflexes of Goth. stains, 'the general Gmc. word for \\\"stone\\\"'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. stone, stiff\", \"stance\": \"supports\", \"note\": \"Skeat derives stone from OE stān (Goth. stains) and stiff from OE stīf, cognate with Lat. stīpāre — the same split the other sources show.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-477.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-14T02:56:47.786Z] TOOL RESULT

```
Exit code 1
Expecting ':' delimiter: line 157 column 376 (char 31047)
```


## [2026-09-14T02:56:53.801Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n '157p' /home/sfmqrb/git/rishe/data/verification/page-477.json | cut -c330-430"
}
```


### [2026-09-14T02:56:53.861Z] TOOL RESULT

```
د و صورت املایی «طایر» را نیز یاد می‌کند؛ پس خودِ وام‌گ
```


## [2026-09-14T02:57:02.514Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'PYEOF'\nimport io\np='data/verification/page-477.json'\ns=io.open(p,encoding='utf-8').read()\nbefore=s\ns=s.replace('در کتاب «tire,\", \"wheel crown\"» چاپ شده', 'در کتاب «tire, wheel crown» (با گیومه‌های نابجای چاپی) آمده')\ns=s.replace(\"[t\\\\\\\\'k\\\\\\\\']\", \"[tʾk]\")\ns=s.replace(\"'Tāzig [tʾcyk\\\\\\\\' | N tāzi] swift, fast. 2Tāzig [tʾcyk\\\\\\\\' | N tāzi] Arab.'\", \"'1Tazig [tʾcyk | N tazi] swift, fast. 2Tazig [tʾcyk | N tazi] Arab.'\")\ns=s.replace(\"'abesar [\\\\\\\\'fysl | M \\\\\\\\'bysr, N afsar] crown'\", \"'abesar [ʾfysl | M ʾbysr, N afsar] crown'\")\nio.open(p,'w',encoding='utf-8').write(s)\nprint('changed', s!=before)\nPYEOF\npython3 -m json.tool data/verification/page-477.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-14T02:57:03.670Z] TOOL RESULT

```
changed True
JSON OK
```


## [2026-09-14T02:57:09.458Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -o \"tʾcyk[^\\\"]\\{0,30\\}\" data/verification/page-477.json | head\ngrep -c '\\\\\\\\' data/verification/page-477.json\npython3 -c \"\nimport json;d=json.load(open('data/verification/page-477.json'))\nfor e in d['entries']:\n  for n in e['nodes']:\n    if n['id'] in (3,4) and e['entry']==0:\n      for c in n['consulted']: print(c['src'],'|',c['note'][:200])\n\""
}
```


### [2026-09-14T02:57:10.566Z] TOOL RESULT

```
tʾcyk', MacKenzie 'Tāzīg [tʾcyk' | 
tʾcyk'، مکنزی: «Tāzīg … N tāzī: عرب
tʾcyk\\' | N tāzi] swift, fast. 2Tā
tʾcyk\\' | N tāzi] Arab.' — the Mid
1
NYB | 'tag [tʾk] crown 56-19; han i zros ~ a cockscomb 56-6. — Syr. lw. taga; Arab. lw. taj and hence again NP taj; cf. Arm. t'aga-vor "king".' Nyberg confirms MP tāg 'crown' as the source of the Semitic an
HRN | '17 [=367]. täj "Krone", täjver, arm. LW. t'ag, t'agavor. Hat mit ap. Yauna takabara nichts zu tun; und ebenso wenig mit assyr. agü "Krone" (nach Jensen, mündliche Mitteilung).' Horn offers no IE root
PHD | MacKenzie's Book-Pahlavi lexicon has 'tāg' only as 'branch' and gives 'abesar [ʾfysl | M ʾbysr, N afsar] crown' as the Middle Persian word for crown; tāg 'crown' is Manichaean/Nyberg's Book-Pahlavi re
PHD | '1Tāzig [tʾcyk\' | N tāzi] swift, fast. 2Tāzig [tʾcyk\' | N tāzi] Arab.' — the Middle Persian ethnonym already has -z-, i.e. it cannot come from tāg/tāj.
MON | 'تاجیک: [- تاجک > تازیک (به یک معنی) - تاژیک، تر. تات (رعیت) + چیک (پس. تصغیر و تحقیر)] غیر ترک (عموماً)، آنکه ترک و مغولی نباشد، ایرانی (خصوصاً) ... صح: «تاجیک» با «تازی» (= تازیک به معنی عرب) فرق دا
```


## [2026-09-14T02:57:15.244Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'PYEOF'\nimport io,json\np='data/verification/page-477.json'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace(\"[tʾcyk\\\\\\\\' | N tāzi]\", \"[tʾcyk | N tāzi]\")\nio.open(p,'w',encoding='utf-8').write(s)\nd=json.load(open(p))\nprint('ok, entries', len(d['entries']), 'nodes', [len(e['nodes']) for e in d['entries']])\nPYEOF\npython3 tools/verify_check.py 477"
}
```


### [2026-09-14T02:57:16.481Z] TOOL RESULT

```
ok, entries 2 nodes [17, 7]
nodes verified: 24/24
node verdicts: {'disputed': 4, 'confirmed': 14, 'plausible': 5, 'unverified': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'partial': 5, 'supports': 14, 'contradicts': 2, 'not_checked': 9}
books consulted: {'silent': 12, 'supports': 28, 'partial': 8, 'contradicts': 7} | by book: {'KLN': 9, 'POK': 6, 'PHD': 4, 'SKT': 4, 'IEC': 4, 'HRN': 3, 'SYN': 3, 'BRT': 2, 'HUB': 2, 'MON': 2, 'LKT': 2, 'AMD': 2, 'ARY': 2, 'HJB': 2, 'AHD': 2, 'KNT': 1, 'NYB': 1, 'WEB': 1, 'AID': 1, 'LAT': 1, 'DEV': 1}
```


## [2026-09-14T02:57:22.119Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/page-477.json'))\nfor e in d['entries']:\n  for n in e['nodes']:\n    c=len(n.get('consulted') or []); r=len(n.get('ref_check') or [])\n    if c<2 or r<1 or not n.get('derivation_fa'): print('entry',e['entry'],'node',n['id'],'consulted',c,'ref',r,'fa',bool(n.get('derivation_fa')))\nprint('roots fa:',[bool(e.get('note_fa')) for e in d['entries']])\n\""
}
```


### [2026-09-14T02:57:23.168Z] TOOL RESULT

```
entry 1 node 2 consulted 1 ref 1 fa True
roots fa: [True, True]
```


## [2026-09-14T02:57:29.679Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'PYEOF'\nimport json,io\np='data/verification/page-477.json'\nd=json.load(open(p))\nfor n in d['entries'][1]['nodes']:\n    if n['id']==2:\n        n['consulted'].append({\"src\":\"BRT\",\"where\":\"Altiranisches Wörterbuch, s.v. stā(y)-\",\"stance\":\"silent\",\"note\":\"Checked in case the empty box was meant to hold a second Avestan or a Middle Persian form: Bartholomae's stā(y)- 'Haufen, Masse' (BRT.txt line 26723) has no derivative that would fill it, and no Persian continuant of this Avestan noun is recorded in Horn or Hübschmann.\"})\nio.open(p,'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=2)+\"\\n\")\nPYEOF\npython3 tools/verify_check.py 477"
}
```


### [2026-09-14T02:57:30.876Z] TOOL RESULT

```
nodes verified: 24/24
node verdicts: {'disputed': 4, 'confirmed': 14, 'plausible': 5, 'unverified': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'partial': 5, 'supports': 14, 'contradicts': 2, 'not_checked': 9}
books consulted: {'silent': 13, 'supports': 28, 'partial': 8, 'contradicts': 7} | by book: {'KLN': 9, 'POK': 6, 'PHD': 4, 'SKT': 4, 'IEC': 4, 'BRT': 3, 'HRN': 3, 'SYN': 3, 'HUB': 2, 'MON': 2, 'LKT': 2, 'AMD': 2, 'ARY': 2, 'HJB': 2, 'AHD': 2, 'KNT': 1, 'NYB': 1, 'WEB': 1, 'AID': 1, 'LAT': 1, 'DEV': 1}
```


## [2026-09-14T02:57:53.729Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-477.json`; `verify_check.py 477` reports **0 PROBLEM lines** (24/24 nodes).

**Page 477 (book p. 447) — 2 entries, 24 nodes**
- Node verdicts: confirmed 14 · plausible 5 · disputed 4 · unverified 1
- Root verdicts: *Steg, Teg* confirmed · *Stei, Stâi 2* plausible
- Ref checks: supports 14 · partial 5 · contradicts 2 · not_checked 9 (Partridge/Shipley lending-only; AHD 1975 main-dictionary pages restricted)

**Disputed**
- *Steg/Teg* #1 **tačara** (OP) — Kent, the very page cited (KNT:186/§148.V), lists `tacara-` among OP words "not traceable with certainty to IE origins… borrowings from non-IE sources" (probably Elamite). No modern source ties it to *(s)teg-.
- *Steg/Teg* #4 **Tâjîk / tâzî** — from the Arab tribe Ṭayyiʾ via MP *tāzīg*, not from *tāj*. Horn p.81 (Nourai's own ref) quotes the *tāj* derivation only to reject it (Quatremère/Nöldeke); Mo'in's footnote at BQT:458 and Wiktionary ("folk etymology") agree. Nourai's "Iranians in Yemen / royal" claim is unsupported.
- *Steg/Teg* #7 **tire, attire** — from Old French *atirier* (a- + *tire* 'order, row', Frankish), nothing to do with Greek *tiara*; only "tiara" belongs in the box.
- *Steg/Teg* #17 **shanty** — current AHD and Etymonline give only Canadian French *chantier*; the Irish *sean tig* etymology (AHD 1975, p.1191) has been withdrawn.

**Worth flagging to the owner**
- KLN:1510 does not support the chart: Klein (s.v. *stemma*) derives Pers. *tāj* from a **different** IE base `*stegʷʰ-` 'to encircle, crown'. AHD:1543 (Watkins) does support it. Nyberg adds that NP *tāj* is a re-borrowing from Arabic ← Parthian/MP *tāg* — a round trip the chart omits.
- Root 2 gloss "stone" is Watkins's; Pokorny 1010 heads the lemma 'to condense, press together'.
- BQT page offset confirmed: BQT_v1_pages.txt scan page 698 = printed 472 (تجر, with Mo'in's tačara footnote), 684 = printed 458.

**Extraction errors: none.** The three empty boxes (#9 Hindustani, entry-1 #2 and #5 French) and the stray quote marks in `tâyer : tire,", "wheel crown"` are all faithful to the printed page (verified against a 200 dpi render).
