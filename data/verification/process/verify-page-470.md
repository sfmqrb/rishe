# Verification process log — verify-page-470


## [2026-09-14T02:27:58.873Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 470 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-470.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-470.json. Write /home/sfmqrb/git/rishe/data/verification/page-470.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 470` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:59.775Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:28:00.690Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:28:00.704Z] TOOL RESULT

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


## [2026-09-14T02:28:01.360Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-470.txt"
}
```


### [2026-09-14T02:28:01.387Z] TOOL RESULT

```
1	=== PDF page 470 (book page 440) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Spher : ankle, also to move fast, spread  (refs POK:992)
4	#1 (parent #0) [Avestan] refs=POK:992; BQT:1086; HRN:154 | spar : to walk ; apa-spar : walk up to, trust (BQT:1086) ☞Apo ; us-spar : walk away, trust (HRN:154) ☞Ud 1
5	  #2 (parent #1) [Persian] refs=BQT:1086; SNS:19 | sepârdan «سپاردن ۱» : walk, trust ; separî «سپری» : past, walked by | extra: سپردن ۱
6	#3 (parent #0) [Greek] refs=POK:992 | spairen : to walk in a bouncing manner ; sphaira : a bouncing object, ball
7	  #4 (parent #3) [French] refs=None | 
8	    #5 (parent #4) [Persian] refs=MON:32 | âtmosfer «آتمسفر» : "sphere of vapor"
9	    #6 (parent #4) [English] refs=AHD | sphere ; atmosphere
10	  #7 (parent #3) [Pahlavi] refs=ETM:68 | spihr : sphere, sky
11	    #8 (parent #7) [Persian] refs=ETM:68, MON:1827 | sepehr «سپهر» : sky, fate ( See "Kuei" for another possible root)
12	#9 (parent #0) [Germanic] refs=KLN:1497 | springan : to jump
13	  #10 (parent #9) [English] refs=KLN:1497 | spring : to jump | NOTE: AHD & POK:998 claim this is from root "Spereg: to jump"
14	--- entry 1 ---
15	ROOT Sphereg -> redirect to Spereg
16	--- entry 2 ---
17	ROOT Spheud -> redirect to Peud
18	--- entry 3 ---
19	ROOT Sphîeu -> redirect to Spyeu
20	--- entry 4 ---
21	ROOT [Greek] Spinakion : spinach  (refs MON:227)
22	#1 (parent #0) [Arabic] refs=MON:227 | spânâj
23	  #2 (parent #1) [Persian] refs=MON:227 | espenâx «اسپناخ» : spinach | extra: اسفناج ، اسپاناخ
24	    #3 (parent #2) [Arabic] refs=KLN:1489; SKT:507 | isbânâx : spinach
25	      #4 (parent #3) [Spanish] refs=KLN:1489 | espinacia
26	        #5 (parent #4) [Middle Latin] refs=KLN:1489 | spinachia
27	          #6 (parent #5) [French] refs=KLN:1489 | espinard ; epinard
28	            #7 (parent #6) [English] refs=SKT:507; AHD | spinach
29	
```


## [2026-09-14T02:28:04.050Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-470.json",
 "description": "Read source JSON for page 470"
}
```


### [2026-09-14T02:28:04.086Z] TOOL RESULT

```
{
  "pdf_page": 470,
  "book_page": 440,
  "entries": [
    {
      "root": {
        "name": "Spher",
        "lang": "Indo-European",
        "refs": "POK:992",
        "gloss": "ankle, also to move fast, spread"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:992; BQT:1086; HRN:154",
          "words": [
            {
              "translit": "spar",
              "gloss": "to walk",
              "script": null
            },
            {
              "translit": "apa-spar",
              "gloss": "walk up to, trust (BQT:1086)",
              "script": null,
              "see": [
                "Apo"
              ]
            },
            {
              "translit": "us-spar",
              "gloss": "walk away, trust (HRN:154)",
              "script": null,
              "see": [
                "Ud 1"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1086; SNS:19",
          "words": [
            {
              "translit": "sepârdan",
              "gloss": "walk, trust",
              "script": "سپاردن ۱"
            },
            {
              "translit": "separî",
              "gloss": "past, walked by",
              "script": "سپری"
            }
          ],
          "script_extra": "سپردن ۱",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:992",
          "words": [
            {
              "translit": "spairen",
              "gloss": "to walk in a bouncing manner",
              "script": null
            },
            {
              "translit": "sphaira",
              "gloss": "a bouncing object, ball",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:32",
          "words": [
            {
              "translit": "âtmosfer",
              "gloss": "\"sphere of vapor\"",
              "script": "آتمسفر"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "sphere",
              "gloss": null,
              "script": null
            },
            {
              "translit": "atmosphere",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "ETM:68",
          "words": [
            {
              "translit": "spihr",
              "gloss": "sphere, sky",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "ETM:68, MON:1827",
          "words": [
            {
              "translit": "sepehr",
              "gloss": "sky, fate ( See \"Kuei\" for another possible root)",
              "script": "سپهر"
            }
          ],
          "note": null,
          "quote": {
            "text": "سیر سپهر و دور قمر را چه اختیار - در گردشند در اثر اختیار دوست",
            "poet": "Hâfez"
          }
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:1497",
          "words": [
            {
              "translit": "springan",
              "gloss": "to jump",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "KLN:1497",
          "words": [
            {
              "translit": "spring",
              "gloss": "to jump",
              "script": null
            }
          ],
          "note": "AHD & POK:998 claim this is from root \"Spereg: to jump\"",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sphereg",
        "redirect": "Spereg"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Spheud",
        "redirect": "Peud"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sphîeu",
        "redirect": "Spyeu"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Spinakion",
        "lang": "Greek",
        "refs": "MON:227",
        "gloss": "spinach"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "MON:227",
          "words": [
            {
              "translit": "spânâj",
              "gloss": null,
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
          "refs": "MON:227",
          "words": [
            {
              "translit": "espenâx",
              "gloss": "spinach",
              "script": "اسپناخ"
            }
          ],
          "script_extra": "اسفناج ، اسپاناخ",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "KLN:1489; SKT:507",
          "words": [
            {
              "translit": "isbânâx",
              "gloss": "spinach",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Spanish",
          "refs": "KLN:1489",
          "words": [
            {
              "translit": "espinacia",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Middle Latin",
          "refs": "KLN:1489",
          "words": [
            {
              "translit": "spinachia",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": "KLN:1489",
          "words": [
            {
              "translit": "espinard",
              "gloss": null,
              "script": null
            },
            {
              "translit": "epinard",
              "gloss": null,
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
          "refs": "SKT:507; AHD",
          "words": [
            {
              "translit": "spinach",
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


## [2026-09-14T02:28:05.509Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','BQT','HRN','SNS','MON','AHD','ETM','KLN','SKT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-14T02:28:06.577Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
```


## [2026-09-14T02:28:38.305Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -100; echo ---; sed -n '1,120p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T02:28:38.380Z] TOOL RESULT

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
---
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
```


## [2026-09-14T02:28:42.627Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','SKT','AHD','MON','BQT','HRN','SNS','ETM']:\n    e=d.get(k,{})\n    print(k,'|offset:',e.get('page_offset'),'|hint:',str(e.get('lookup_hint'))[:400])\n    print()\n\""
}
```


### [2026-09-14T02:28:43.722Z] TOOL RESULT

```
POK |offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d

KLN |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

SKT |offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.

AHD |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.

MON |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab

BQT |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada

HRN |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

SNS |offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image |hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.

ETM |offset: None |hint: Searched archive.org, ketabnak, noorlib, web: not found.
```


## [2026-09-14T02:28:47.614Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: *sp\" POK_full.txt | head -40"
}
```


### [2026-09-14T02:28:47.667Z] TOOL RESULT

```
79425:Root / lemma: spako- 
79439:Root / lemma: speg- 
79459:Root / lemma: speR- 
79518:Root / lemma: spend- 
79594:Root / lemma: speno- steno- p(a)steno- 
79629:Root / lemma: spergh-, spregh-, nasalized sprengh- 
79685:Root / lemma: sper-2(g-) 
79718:Root / lemma: sper-3 
79749:Root / lemma: sp(h)ei. sp(h)iav\6 sp(h)e. sp(h)a-2 
79821:Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- 
79962:Root / lemma: sp(h)e(n)d- 
79985:Root / lemma: sp(h)eng- 
79993:Root/ lemma: sp(h)eng-\ to shine derived from Root/ lemma: *(s)p(h)ereg-, (s)p(h)erag-, 
80030:Root / lemma: sp(h)erd(h)-, (s)p(h)red(h)-, nasalized sp(h)rend(h)- 
80040:Root / lemma: sp(h)erd(h)-, (s)p(h)red(h)-, nasalized sp(h)rend(h)-\ to rush; to spring; 
80093:Root / lemma: sp(h)er-1, sp(h)era- 
80107:Root/ lemma: sp(h)er-1, sp(h)era-\ to make a rash movement, to push away, to rush, 
80290:Root / lemma: sp(h)er-3 
80420:Root / lemma: sp(h)e(i)-3, 5/7A-and sphe-. spha- 
80523:Root / lemma: sp(h)e-, sp(h)a-(<S^-) 
80594:Root / lemma: sp(h)reig- 
80727:Root / lemma: sprei- spreu-
```


## [2026-09-14T02:28:48.212Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 99[0-9]\" POK_full.txt | head -20"
}
```


### [2026-09-14T02:28:48.295Z] TOOL RESULT

```
43012:Page(s): 996-998 
79627:Page(s): 990 
79654:Page(s): 998 
79683:Page(s): 990-991 
79716:Page(s): 991 
79745:Page(s): 991-992 
80091:Page(s): 995-996 
80176:Page(s): 992-993 
80288:Page(s): 993-995 
80306:Page(s): 995 
80324:Page(s): 992 
80358:Page(s): 998-999 
80592:Page(s): 999-1000 
80631:Page(s): 999 
80651:Page(s): 999
```


## [2026-09-14T02:28:49.578Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '80093,80200p' POK_full.txt"
}
```


### [2026-09-14T02:28:49.643Z] TOOL RESULT

```
Root / lemma: sp(h)er-1, sp(h)era- 

Meaning: to make a rash movement, to push away, to rush, etc.. 

Grammatical information: spijo, spf-na-mi6s:. 

Note: compare /OeA-f sprijhen, spray', further: sper- "sparrow', sper- 'rafter', sp(h)er- 

"Mistkijgelchen', sp(h)ereg-^ twitch ', spergh-^s\ch hastig bewegen', sp(h)ered(h)-^ twitch 

', sp(h)reig-^ s\xo\.z.eVi 

Comments: 

Root/ lemma: sp(h)er-1, sp(h)era-\ to make a rash movement, to push away, to rush, 

etc., derived from Root /lemma: *(s)p(h)ereg-, (s)p(h)erag-, (s)p(h)reg-{r\asay\ze6 spreng- 

) : to rush, hurry; to scatter, sprinkle. 

Material: Old Indie sphurat/^ s\.6Q>\. with dem Fufte weg, tritt, schnellt, shrugs, jerks, 

trembles, zappelt', apaspharlh /\or . Inj. "schnelle weg, entzieh dich rasch' (: Latin 

aspernarfj, apa-sphura-^\NegstoQ>er\6' (: Latin asper-), sphura- "blinking', sphurana- 

"blinking, gleaming, scintillant, flickering, sparkling', n. " twitch, sparkle, Erscheinen', 

vispharita-m^6as Schnellen'; sphurt/-'t\r\e burst out, break out, Offenbarwerden' {*sphr-t/-, 

compare Lithuanian spirti), pharpharayate 'bewegt sich heftig hin and her'; spr- 

"losmachen', sprnot/ ^wehrtab', sprnati^ slays '; 

Avestan spar{aiti) "tritt, stoftt', with /^5 "rushes, hastes', with i//"auseinandertreten, - 
stomp', sparman- n. perhaps " step, tread; kick, strike or blow delivered by the foot; 
footprint, track, shove ', np. s/pardan^ tread'; 

Armenian sparna/ ^bedmhen' (Indo Germanic sp-); 

gr. anaipu), aanaipu) (a- vowel suggestion) " twitch, wriggle ' (= Lithuanian spiriu), 
anaipsi aAAsrai, QKiprg, nr|5c( Hes. (aspiriert ocpaTpa "Ball zum Spielen'?), aspiriert acpupov 
"ankle, calcaneus ', wovonocpupa "hammer, beetle, hammer' (to ocpupov compare Old High 
German sp^/7-/7a/z"hinkend', actually "knochel-lame'); 



Latin sperno, -ere, spre-vT, -turn 'back-, fortstoften, verschmahen, despise ', aspernor, - 
a/y'trom sich weisen', asper'rouqh, harsh, abstoftend' (: Old Indie apa-sphura-); 

Old Irish se/A'calcaneus ' {*speret-s), Akk. Du. di pherid, cymr. ffer, ffern' 



Inkle bone; the heel, knuckles, a little hammer; a kind of fire-dart '; Middle Breton /ferds.; 
cymr. uffarn'2x\V\€ from * opi-sper-no-. 

Old Icelandic sperna'wlth den Fijften ausschlagen, wegstoften' (: Latin spernd). Old 
English speornan^s.. Old High German firspirniV sMb^'i an, trittfehl'; Old Icelandic sporna 
{-ada) 'with dem Fufte ausschlagen'. Old English spurnan, spornan'6s., also 
"zuriJckstoften, despise ', Old Saxon Old High German spurnan 'tread, with dem Fufte 
bump, poke'; Old High German sporndn'\N\t\r\ the calcaneus ausschlagen, dem Fufte 
bump, poke', spurnen {spurnta) ds., 'zuriJckstoften' {spurn/da 'Ar\s\.o(}>'), Old Icelandic 
spyrna "with dem Fufte bump, poke; (den foot) entgegenstemmen'; without 
prasensbildendes n:0\6 Icelandic spora'W\\h Fijften treten'. Old English sporettan'\N\t\r\ 
dem Fufte bump, poke'; Old IcelandicS/OO/y; Old English spora, spura. Old High German 
sporo' spur'; Old Icelandic Old English Old High German sporn. " footprint ', Middle High 
German spur, spciri. n. "spoor, track ', Old High German spur/- ha/z lame, hinkend, from 
horses' (see above to acpupov). Old High German (etc.) spurjan, spurren "the spoor 
nachgehen, erforschen, skillful '; Old English spearwa rw. "calf. Middle High German spar- 
golze\. "ein Teil the Beinbekleidung' (perhaps "Wadenstutzen'); with erweiterndem ^.Old 
Icelandic sparka'W\Vc\ dem Fufte bump, poke', in addition postverbal 5p5/'/r"Getramper; 

Lithuanian spiriu, sp/rt/"\N\\h dem Fufte bump, poke, urge, press, push, constrain, oblige' 
(from the heavy basis), ablaut, atsparas "\N\derstand' , spardau, -///"continual with den 
Fijften bump, poke'; Latvian S/Oe?/ "ausschlagen (of horse), with dem Fufte bump, poke'; 
spars' energy, Schwung, force '; Lithuanian S/Oa/f^s "ausgiebig; rash, hasty, agile, lively'. 
Old Prussian S/Oa/Ys "mighty', S/Oe/r/a/? "Zehballen'; but Lithuanian spurzdeti" s\c\\ with den 
Flijgeln jiggle or flutter', suspursti iroxr\ birds "in eine schnurrende Bewegung geraten', then 
generally "in heftigen rage, fury geraten, violent become' are probably onomatopoeic 
words (compare Modern High German bri\). 

References: WP. II 668 ff., WH. I 73, WH. II 572 f., Trautmann 275 f. 
Page(s): 992-993 

Root / lemma: (s)p(h)er-2, sprei- spreu- 

Meaning: to sprinkle, scatter 

Note: probably with sp(h)er-V twitch ' identical, also with per-1, above S. 809 f. 



Comments: 

Root / lemma: (s)p(h)er-2, sprei-, spreu-: to sprinkle, scatter, derived from Root/ lemma: 

*(s)p(h)ereg- (s)p(h)erag-, (s)p(h)reg- {riasay\ze6 spreng^ : to rush, hurry; to scatter, 

sprinl<le. 

Material: A. Armenian p a/'5/'zerstreut' ( *pher-), p 'aratem "zerstreue, entferne, tal<e away ' 

(compare gr. anopa(;, -a5o(;); perhaps also SyO'/e/r? 'zerstreue', S/0//''zerstreut, verstreut, 

vast, spacious' (would be *sphero-)\ 

gr. ansipoo "streue, sow, sprenge, spritze, sprijhe' (anspu), sanapKa, sanapnv), airspija
```


## [2026-09-14T02:28:58.744Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '80300,80330p' POK_full.txt; echo \"=== spergh ===\"; sed -n '79629,79690p' POK_full.txt"
}
```


### [2026-09-14T02:28:58.832Z] TOOL RESULT

```
grofte graue Erbsen', yO/res 'Schafmist'; 

with d^-extension: gr. anopOuyyia rpipoAa to 5iaxu)pn[jaTa twv aiyajv, a rivsg anupaSaq 
KaAouGiv Hes.; nisi, spardu. "Schafmisf, speAd/Z/'Ziegenmist'. 

References: WP. II 672. 
Page(s): 995 

Root / lemma: (s)p(h)er-4, (s)p(h)erag- 

Meaning: to tear; rag, snippet 

Material: Armenian p'ert'^ ragged piece' {*sperk-to-)\ Old Icelandic spigrri. "scrap, shred, 

abgerissener Streifen Tuch' (proto Germanic *sperrd)\ 

gr. anapaaau), Attic -aiTU) "tear, rend, zerre' (probably analogical for -a^w), anapaypa " 
ragged piece', arrapaYMoq "das Zerren, Reiften; cramp'; 

nasalized perhaps Old Bulgarian prgziti, prgzat/ '\acerare'. 



References: WP. II 668. 
Page(s): 992 



Root / lemma: (s)p(h)eu-d- 

Meaning: to press, hurry 
=== spergh ===
Root / lemma: spergh-, spregh-, nasalized sprengh- 

Meaning: to hurry, to spring 

Note: Erweit. from sper-' twitch, schnellen'. 

Material: Old Indie sprhayati' longs for, empfindet envy ', Avestan a-sparazata'^ax 

bestrebt'; 

gr. anspxopai ' storm along, hurry (an£px6|j£vo(; 'hasty, hasty, rash, hasty'), boisterous, 
be angry, furious ', ottspxcjo 'drange, drive', an£pxv6(; 'quick, fast, hasty', aan£px£<; Adv. 
'violent, ardent '; here cymr. ffraeth{see 996); 

Old Icelandic S/O/7/7^5 'spring, burst out, break out ', Old English Old Saxon Old High 
German springands.; Kaus. Old High German sp/'e/T^e/? 'spring make (ein horse), 
(zer)sprengen' and 'strew, distribute, spray, sprenkein'. Old Icelandic sprengja' sprinkle ', 
Old English sprengan' outspread, break, crack; burst, saen'; Middle High German sprinc 



{-g-) "spring, wellspring', Old English SyO/7>7^'Wasserqueir, engl. spr/ng'ds., Sprungfeder, 
Knospenspringen, spring '; old Ablautform *sprdgh-\n Old Icelandic S/O/'o^a "spring, run'. 

References: WP. II 675, Trautmann 278 f. 
Page(s): 998 

Root / lemma: (s)per-l 
Meaning: rafter; pole, spear 
Note: originally denominativ 

Material: Latin spams, sparum'Wurzer spear, javelin of Landvolkes as Jagd- and diirftige 
Kriegswaffe' {*spero-)\ in addition a kind offish spams, gr. arrapoc;; alb. shparr, shperdhe 
"oak' (as "timber'; /■/■from m); Germanic *speru- in Old Icelandic S/cyipA" spear, javelin'. Old 
English spereu.. Old Frisian spin, spere, sper. Old Saxon Old High German sper. Middle 
High German sperm, n.. Modern High German Speerxw., Old High German spereboum 
"aesculus'; Old Icelandic spari, sparrim. "Speller, rafter, balk, beam', sperrai. {*sparridn) 
"roof beam'. Old High German Syoa/ro" balk, beam, roof beam, shaft, pole'. Modern High 
German Sparren^ rafter'; therefrom Old Icelandic sperra'\N\t\r\ Sparren versehen; die 
Beine spreizen, aussperren, verhindern'; Old Icelandic sperra. Old English be-, ge- 
spa/77a/7"verrammeln'. Old High German Middle High German sperren^ through 
einenSperrbalken verschlieften, sperren; ausspreizen'; 

other formations Old High German spirdren^u'W^ (/-Verb as muntren, s. Schatz, 
Germanica for Siewers 367); 

without ani. 5-.' Latin par/es'waW (originally "die SeitenstiJtzen eines Zeltes '); Slavic 
*pbrg, *pert/^prop, support', with yOC»o'b-"fulcire', with za- "claudere', e.g. Old Church Slavic 
podhptrg, pret/^prop, support', zapret/" shui', russ. u-peretb "stemmen, an or against 
etwas prop, support; refl. sich whereof lean, sich wogegen sperren, strauben', zaperetb 
"versperren, verschlieften', poln. p/'zec "spreizen, lock ', Old Church Slavic podbporb, - 
yOOAa "fulcrum, baculum', russ. upor^padi, Strebepfeiler' etc. 

References: WP. II 665 f., WH. II 254, 568, Trautmann 275 f., Vasmer 2, 341 . 
Page(s): 990-991 

Root / lemma: sper-2(g-) 

Meaning: a kind of bird (sparrow?) 

Material: Gothic sparwa. Old English spearwa. Old High German spare ^ sparrow' (*proto
```


## [2026-09-14T02:29:05.654Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^sp\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-14T02:29:05.738Z] TOOL RESULT

```
978:spé-'
980:sper-4
982:spere-
983:spréot, pole (< “sprout, stem”): sPRIT; d. Middle English bouspret, bowsprit: BOwsPRIT. 3. Extended form *spreit- in Germanic *spraidjan in Old English sprédan, to spread: SPREAD. II. Basic form *sper-. 1. Suffixed form *sper-yo- in Greek speirein, to scatter: Diaspora. 2. Suf- fixed form *sper-mn in Greek sperma, sperm, seed (< “that which is scattered”): SPERM}. III. O-grade form *spor-. 1. Suffixed form *spor-d- in Greek spora, a sowing, seed: SPORE, SPORO-. 2. Suffixed form *spor-nd- in Greek sporas (stem sporad-), scattered, dispersed: SPORADIC. [Pok. 2. (s)p(hJer- 993.]
984:spere-. Ankle. Zero-grade form *spr(o)-. 1. Germanic suffixed form *spur-6n- in Old English spura, spora, spur: SPUR. 2. Nasalized form “spr-n-o- in Germanic *spurnon in Old English spurnan, spornan, to kick, strike against: SPURN. 3. Germanic suffixed form *spur- am in Middle Dutch spor, spoor, track of an animal: Spoor. [Pok. 1. sp(hJer- 992.]
985:spergh-. To move, hasten, spring. Nasalized root form *sprengh-. 1. Germanic *springan in: a. Old English springan, to spring: SPRING; b. Middle Dutch springen (> Dutch springen and Afrikaans spring), to leap: KLIP- SPRINGER, SPRINGBOK; C. Old High German springan, to jump: GELANDESPRUNG. 2. Germanic causative *sprang- Jan in: a. Old English besprengan, to sprinkle, scatter: BESPRENT; b. Old English *sprencg, snare used to catch game: SPRINGE. [Pok. spergh- 998.]
987:sping-. Also ping-. Bird’s name, sparrow, finch. Ger- manic *finki- in Old English finc, finch: FINCH. [Pok. (s)jpingo- 999.]
989:splei-. To splice, split. Extension of spel-1. 1. Germanic *fli- in: a. Old English flint, flint: FLINT; b. Norwegian flindra, splinter, akin to the Scandinavian source of Middle English flendris, bits, splinters: FLINDERS. 2. Germanic “*spii- in: a. Middle Dutch splinter, splinter: SPLINTER; b. Middle Dutch splitten, to split: SPLIT; c. Middle Dutch splissen, to splice: SPLICE; d. Middle Low German and Middle Dutch splente, splinte, splint: SPLINT. [Pok. (s)plei- 1000.]
991:spreg-. To speak. Germanic *sprek-, *spek- (with Ger- manic loss of r) in: a. Old English specan, to speak: SPEAK; b. Germanic compound *bisprekan (*bi-, about; see ambhi) in Old English bisprecan, besprecan, to speak about: BESPEAK; c. Old English spréc, spéc, speech: SPEECH. [In Pok. (s)p(h)ereg- 996.]
993:spyeu-. Also speu. To spew, spit. Expressive root. 1. Germanic *spitjan in Old English spittan, to spit:
995:spit!. 2. Germanic *speiw- in Old English spiwan, spio- wan, to spew: SPEW. 3. Germanic *spait- in Old English spatl, spittle: sPITTLE. 4. Germanic *spiit- in: a. Middle English spouten, to spout forth: spout; b. Dutch sputte- ren, to sputter, akin to the probable Low German source of SPUTTER. 5. Zero-grade form *spu- in Latin spuere, to spit: SPUTUM; CUSPIDOR. 6. Zero-grade form *(s)pyu- in Greek ptuein, to spit: HEMOPTYSIS, PTYALIN. [Pok. (s)p(hjieu- 999.] srebh-. To suck, absorb. Zero-grade form *srbh- in: a. Germanic *surp- in altered form in Dutch slurpen, to slurp, lap: SLURP; b. suffixed form *srbh-é- in Latin sorbére, to suck: ABSORB, ADSORB, RESORB. [Pok. srebh- 1001.] srenk-. To snore. O-grade form *sronk- in: a. Greek rhonkos, rhonkhos, a snoring: RHONCHUS; b. Greek rhunkhos, snout, bill, beak: RHYNCHOCEPHALIAN. [Pok. srenk- 1002.] sreu-. To flow. 1. Suffixed o-grade form *srou-mo- in Germanic *straumaz, stream, in: a. Old English stréam, stream: STREAM; b. Dutch stroom, stream: MAELSTROM. 2. Basic form *sreu- in: a. Greek rhein, to flow: RHEO-, -RRHEA; CATARRH, DIARRHEA, HEMORRHOID, RHYOLITE; b. suffixed form *sreu-mn in Greek rheuma, stream, humor of the body: RHEUM. 3. Suffixed zero-grade form *sru-dhmo- in Greek rhuthmos, measure, recurring mo- tion, rhythm: RHYME, RHYTHM. [Pok. sreu- 1003.]
```


## [2026-09-14T02:29:06.371Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sphaira\\|sphere\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T02:29:06.425Z] TOOL RESULT

```
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old English réden, condition: HATRED, KINDRED; b. Germanic *rédaz in (i) Old High German rat (> German Rat), counsel: BUNDESRAT, RATHSKELLER (ii) Old English rédels(e), opinion, riddle: RIDDLE?. 3. Zero-grade form *ra- in Germanic *radam, number (see dekm). IV. Variant (or separate root) *ri-. 1. Suffixed form *ri-tu- in Latin ritus, rite, custom, usage: RITE. 2. Suffixed form *(a)ri-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM. [Pok. 1. ar- 55.]
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM, DEVIL, (DIABOLIC), (EBLIS), ECBOLIC, EMBLEM, EPIBOLY, (HYPERBOLA), HYPERBOLE, METABOLISM, (PALAVER), PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), (PAR- LOR), (PAROL), (PAROLE), PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL?, (BALLAD), (BALLET), BAYA- DERE. 2. Suffixed o-grade form *gvols-d in Greek bolé, beam, ray: BOLOMETER. 3. Suffixed o-grade form *gwolo-sdé in Greek boulé, determination, will (< “throw- ing forward of the mind”), council: BOULE!; ABULIA. 4. Suffixed variant zero-grade form *gvele-mno- in Greek belemnos, dart, javelin: BELEMNITE. [Pok. 2. g¥el- 471.] gwela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.] gven-. Woman. 1. Suffixed form *gven-d- in: a. Germanic *kwen6n- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben (> Irish Gaelic bean), woman: BANSHEE; C. Persian zan, woman: ZENANA. 2. Suffixed lengthened-grade form *gvén-i- in Germanic *kwéniz, woman, wife, queen, in Old English cwén, woman, wife, queen: QUEEN. 3. Suffixed zero-grade form *g“n-d- in Greek guné, woman: GYNO-, -GYNOUS, -GYNY; GYNAE- CEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin gravis, heavy, weighty: GRAVE?, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form “gro-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA; b. Sanskrit guru-, heavy, venerable: GURU. 3. Suffixed form *gro-es- in Greek baros, weight: BAR?, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR. 4. Possibly *guri- in Greek bri- in compound *u(d)-bri- (see ud-). II. Suffixed extended form *g-rii-to- in Latin britus, heavy, unwieldy, dull, stupid, brutish: BRUT, BRUTE. III. Suffixed extended form *g»ri-g- in: a. Celtic *brig-o-, strength, in Italian brio, vigor: BRIO; b. Germanic *krig- in Old High German krég, chrég, stubbornness (> Ger- man Krieg, war): BLITZKRIEG, SITZKRIEG. IV. Suffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
650:kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
1165:wet-'. To blow, inspire, spiritually arouse. Related to wé-. 1. Lengthened-grade form *w6t- in Germanic suffixed form *wéd-eno-, *wéd-ono-, “raging,” “mad,” “inspired,” hence “spirit,” name of the chief Teutonic god, in: a. Old English Woéden, Woden: WoDEn; b. Old English Wod- nesdxg, ““Woden’s day”: WEDNESDAY; Cc. Old Norse Odhinn, Odin: Opin; d. Old High German Wuotan (> German Wotan), Wotan: WoTAN. 2. Lengthened variant form *wdt- in Latin vdtés, prophet, poet: vaTic. 3. Suf- fixed variant form *wat-no- in Latin vannus, a winnow- ing fan: FAN!, vAN3. 4, Oldest basic form *awet- becoming *awet- in suffixed form *awet-mo- in Greek atmos (< *aetmos), breath, vapor: ATMOSPHERE. [Pok. udé- 1113.]
1260:ARMADILLO = ar- ARMATURE ar- ARMIGER gerere ARMILLARY SPHERE al- ARMISTICE sta- ARMOIRE ar- ARMY ar- ARPENT pert ARRAIGN  ar- ARRANGE sker-3 ARRAY reidh- ARREARS re- ARREST sta- ARRIERE-BAN koro- ARRIVE rei-1 ARROGATE reg-1 ARROW arku- ARSENIC ghel-2 ARSIS wer-2 ARSON as-
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
```


## [2026-09-14T02:29:13.578Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"SPHER[A-Z]* [a-zA-Z0-9ǝé()ō*-]*\" AHD_watkins1985.txt | sort -u | head; echo \"--- spinach ---\"; grep -o \"SPINACH[ ]*[a-zA-Z0-9-]*\" AHD_watkins1985.txt | sort -u | head; echo \"--- SPRING ---\"; grep -o \"SPRING[A-Z]* [a-zA-Z0-9-]*\" AHD_watkins1985.txt | sort -u | head"
}
```


### [2026-09-14T02:29:13.719Z] TOOL RESULT

```
SPHERE al-
SPHERE gWere-2
SPHERE wet-
--- spinach ---
--- SPRING ---
SPRINGBOK bhugo-
SPRINGER spergh-
SPRINGE spergh-
SPRING pelo-
SPRING spergh-
```


## [2026-09-14T02:29:21.411Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT spar ===\"; grep -n \"spar\" BRT.txt | head -40"
}
```


### [2026-09-14T02:29:21.473Z] TOOL RESULT

```
=== BRT spar ===
3165:■übelste,  böseste"*:  dva  yaska..  -«(NDm.) I  V.  7. 70;  —  sHptibyasca  (sd.) . .  vispalibyasLa pairi  'taeibyö  \.  14.17;  —  °to«  rfuirfw- Aavö  'P.14;  —  nöil  hl . .  bvat  . .  zahistiJ anhuL.bi'ai  TTspariqm  *°/jm'^  *paosisl>mcix ya^  »riyat  daozaishum'^ . .  sondern  es  wird
4168:Pahl.-Teit  hat:  matt  an  nc-.uakih  yas  tie  äfrl- Ulf  eslet  al  kakurf  spar  ne  raset  ha^  an  yai pailäk  g'  a'  a'.  —  'I  Ob  gairLmasaakäi
4474:Pü. !  anafie  apaspäTÜnik ;  s.  noch  No.  4, 6.  — ')  Hds.  Shianisititim.  —  »)  Hds.  ainüsrilim. — 3)  Hds.  ai%sHiim.  —  1)  Hds,  anitril;  Pü. : fehlt.—  £)  Der  Text  sollte  lauten:  %TiiayaaA>m )ia%ra  raiul  a'iti/ayauliim  ya%ra  ttp>r>näyüt5 nSii  .  ,;  s.  zu  ♦aSiffflyiis'iri-.  —  *>  Hds.  airili; Pü.:  /a  fl/Ji-'  (statt  atiapäc)  apasparäulh,  erl.: kaS  nc  dabei.
4848:YL70.131;  —  astiys  *'na'>  spar>ya(%A.) Vt./o.iag; — yezi  anhat  zarynaim's  (sd.) •«//(NSf.)  V.  7.74f.         a)  n.  ein  aus
5836:—  'panqmca  srtfa  Yt  10. 113;  —  'pahe. . sparmaiiii  (sd.)  Vyt.  ^5 ;  —  °pahe  aojö Yt  z^.  68;   iV.  24;   —    hazarinm    °panam
5842:KompA.»,  E.;  AblciL  —  «i.  äifa-  m-,  ojz-J- f. ;  mp.  -(j/.  —  Pü. :  asf.  S.  noch  zu  sparman-. —  ')  Unter  den  slaora-  (sd.)  das  iweitwert- Tothte  Tier.  —  ')  Vgl.  auch  *a4bäray-,
5859:•  j.  asparana-  m.  Name  einer  Münze*>: °nS  F.  7;  —  duye  AazaaraAe  'nam  nidmat Vd.  6.
5865:•  j.  asparanö.maza-  Adj.  'durch  A^er- p fändung  eines  Asp.  geschlossen',  von Verträgen:  hö  upa.msrptS  (sd.)  hau  *zS V.4.48.
5870:•  j.    aspar^nö.mazah-   Adj.    'was    den  |
6598:yä  oder_>'J(?)  vll.  sva.  'es  geschieht,  kommt vor,  dass  ..':  asit'i^  yä  *ayar3Aa^a  sparr/a (sd.)  YL/0.  laöGl.;  —  asti'*''  yS gavasnaAe (sd.)  snäuya  jya  Yt  10. 1 28  Gl.  III)  als j  Praedilcatsverbnm  (Kopula).  Das  Praedikat ist  I)  ein  Substantiv,  das  mit  dem  Subjekt im  Numerus  und  Kasus,  oder  ein  Adjektiv, das  auch  im  Genus  kongruirt.  A)  I  im Ap.  (die  Kopula  folgt  dem  Praedikat): adam  bardiyä'  amiy  .  .  adam  xsäya'iiya* amiy  Bh.  b,  h;c-f*,  h-j^,  Bh.  7.5,  11,  16', -■3>  S'  55.  13-  4.2*,  D.(t.4;  —  adam xsaya%iy£^  amiy  asagartaiy  ""uvaxstraAyä laumäyä  Bh.2.  i4,4.2,Bh.g,;  —  adamsäm xsäya^iyt^  äham  Bh. /.  6;  —  ka"bujiy<^ ,  .paruvam  idä  xsäya'^iya"  ähJ^  Bh. /.  10; —  g  *duvitäiaranam  (sd.)  vayam  xsäya- üyä  amahy  Bh.  j.  4;  —  tyaiy  paruvam xsäya'iiyä  aha"  Bh.  7.  4;  —  kalä  pa- ruviyata'  hyä  amäxam  taumä  xsäya'iiyä (sd.)  äh(^  Bh.  j.  3 ;  —  adam  pärta''  amiy D.  77. 3 ;  —  martiyJ^  Ayo*  draujana'' ahatiy  Bh.^.5,  14;  14,  5;  —  Äj'u*  daustä <Ua*.  .  hyi^  arika''  äha*  Bh. /.  8;  2.4,  6, 3-  II,  5.4;  —  tyaisaiy  fratamä  martiyä anusiyä  äha"täi'>  Bh.  ;.  13;  J.  7,  8,  11,  13, /.  7;  —  negirt:  ya^ä  naiy  arika"  äham Bh..:^.  13;  13  ^  —  ty^  adam  naiy  bardiya'' amiy    Bh.  7.  13.  B  [)    im   jAwr.    (Die
7838:•  g.  asa-  m.  'Partei',  nur  Du.  von  den beiden  Religio  nsparteien,  der  a^uHschen und  der  daiiA^hea'^ :  ai  vä  vTs^Sng  äyöt jiaiä  ratäm  (sd.)  ahurB  valdä  mazda  aya
8259:—  Yt.j2.22,  /J-ja:  streiche  upa^ KompA.;  Ablcit.  —  ai.  üpa  Praen.,  Piaev. ; mp.  /^{sparlaii^  np.  vgl.  bäyad  (Hbh.  PSI. IZSl  — Pä.:  apar,  als  Praen.  mil^,  0,  andar; 5.  noch  No.  4.  —  '»  Wo  upa  ia  den  Hds. fehlt.  —  »)  Vgl.  Yl.  5-  SO,  wo  ana.  —  i)  Vgl V.  iS.  51.  —  «  NA.  upadarasahu;  B.  aber Pt  ^  nnr.;  Pü.:  /a.  —  S)  Wohl  verderbt.  — 6)  Granimalisch  ganz  verwahrlost.
10532:airihä  zimS  (sd.)  päsnalibya  vTspara aslaäbya   vixala  (aS.)  V,  2.  31;  32    (wo
11070:sind  getrennt:  yS  gam  ia^d  apasca  itrva- rh^ä  Y,5/,  7";  — yi  .  .  amfrstatäUm  .  . as>mcä  .  ,  dätakä  (sd.)  .  .  xsairimla  Y. g4. 1 ;  —  a  mä  alhmö  hazascä  [rw»fl] '"' äkiSäyä  (sd.)  ä?nsiä  tivilcä  Y.  2(j.  i ;  —  mos- tJm ..  sparumca  vtniiraytumca  vanaitttlmca uparatät»nt  YtJ,  36;  —  apqm  napas)  tä äps  . .  vlbaxsaiti  vätasca  . .  awidätimla c^arfnB  asaonqmca  JrmiasayS  Yt.  8.  34; Y.  j/.  2a;  —  anyS  asSI  'kwatcd  ..  vahtstä- aüä  manarthd  Y.50. 1 ;  — yada  a?»m  twTm (sd.)  anAin  maedäscä  ahurhtths  asicä  -j* armaitl  Y.3/.  4.  a)  mit  Tmesis:  srao- s)m  .  .  asimca  . .  nairimca  saahfm  Y.57. 3  (s.  dagegen  Ytio.  53).  c)  das  erste Glied  ist  ein  enkL  Pron,  pcrs. ,  das  sich auf  einen  dahinter  stehenden  Vok.  be- zichtJ*;  nur  gAw.:  yi  "hwat  mazdJ  .  . a^alBu^cä  ..  virtz^naRyücä  ..  atryamanascä . .  gSuscä  Y._5'_J.4;  —  anats  va  nBit  ahurä . .  aipmeä  . .  saranafirnJ  . .  maitatcä  hyaf vahisiMtt  Y.  2Ä  9 ;  —  yS  vi  asa  ufyäni manascä  vohü..ma2dqmcä  Y.25.3.  d)ein Glied  oder  mehrere  oder  alle  sind  rela- tivisch  gegeben;  cä  steht  dann  beim  Rel.: narSi  firasaoiträi  maibyäcä  yalibyascä  Ti rrivAan'Aöi  "dem  .  .  J^r.  und  mir  und (all)  denen,  denen  du  .  ."  Y.  2.9.  8;  — AviF  .  .  yas!ä  .  .  dadät  yascä  . .  vfväpat yaüä  . .  vöiidat  '^.32. 10;  —  kavaim kavätsm  yimca  kava^n  aipi.vokum  yimca^.. Yt,  /()•  7 1 ;  —  ya  äps  yssla  urvari  yasca asaonqm  fravasayS  Yt/o.  100;  —  hujUayB .  .  yS  .  .  anharj  yascä  hfntJ  yascä  . .  ba- vainti  Y.33.  10;  — yä  tsi  .  .  adistil yacil vohB  uxbä  /ras'l (sd.)  ntanankäyäcä  ff/ö.. y.44-^',  —  yä  var^sä  yäcä  pairj  (sd.) J//  syadi^ani  y.lcil  .  .  aryat  (sd.)  V.  ^o. 10.  a)  mit  unregelmässiger  Stellung  des ain  tifyänl  manascä  voka  .  . %hur>m  yaeihyS  xsairpmtä"^ ■«(sd.)..Y.2Ä3(s.c).  e)das st  nicht  ausdrücklich  genannt, dem  Zusammenhang  zu  ergän- )6  u.);  nur  gAw.:  atcä  ..  scarUB iva'ä  viitlsps  ..forasaosiras'ä id^f^undA"Yoj.a.      2)die
11071:Glieder  sind  verbal:  yBi  ztjvä  (nämL  hitOt) *ar»har3La  bvanticS{sA)\.4^.T.  3)bci allen;  a)  D  im  Ap.;  das  letzte  Mal  steht Uta  statt  cä:  pärsamcä  mädamcä  utä  aniyä dakyiivaf"  Bh.  /.  14.  b)  im  Aw,;  i)  die Glieder  sind  nominal ;  a)  sie  folgen  sich  un- mittelbar: nmänyasca  visyasca  santumasca Y.  if).  18  (s.  dazu  18  aA.);  —  aojasca  v»ty- 'inmca  j^armas^a  lavania  Y.  7/.  8 ;  —  sta- rasca  mäsca  >fe'<i/vi-'(7  YL72,25(s.dagegeni_j. 57);  —  vätftnca  vänmca  tnafy^mca  Jyau- humca  Yt  5.120; — hubprvtlmca  uslaMin- tlmca  vanta.bintTmca  Y.  61. 2  (s.  dagegen  7 ; Sp.  570U.);  —  maziUäsca  vahiitasca  srais- tas^a  asayS  Y.  52.  3;  —  apasca  urvaräsca xadirdsca  Y. A3;  —  asavafom  htnümca bavaniiinla  busyantimla  Yr.lS.i; — vTspayä ..slöis  haihyJica  bavqihyäica  büiyqi^yäica \.6S.i3i  —  nm3nanqmcä  vlsqm^a  satttu- nqmca  dahyunqmca  Y.  Ä  7 ;  —  damayä  anu- matayal'a  aiiuxtayaica  * aim.varstayai^a Y.Ä7;  —  d^aurunqscä  rä^aistiscä  väs- tryqscä  ßuyants  Y.  ig.  3;  Yt  ig.  8;  — ahamca  ratümca  paoirimca  tkaisim  Yt/^J. 152;  —  ha^ra  miiräca  rasnuta  uyraca dämSis  upamana  Yt/_J.  47;  —  vispss^a paiti  vansajls  vTspSsca  paiti  frasparrjJ i'JspSsca  paiti  fravaxsS  Y.  jo.  5 ; — haurva- tasca^  fiö  am)r>täta  gSuica  taSnB  gSusca urunS  ä%rasi-a  aoxtsjiämand  hadisasca  Vr. g.  5;  —  beim  Zahlwort:  navaia  navaittfca navaca  sota  navaca  Aazavra  navasSsca baivqn  Yl;_J.S9.  a)mitTmesis:*«ai/x
11601:•  y  Jazav-  m,  (auch  mit  'spart-  m.)  Name einer  Art  des  Hundegeschlechts:  hau  °z3us (GS.)  hau  visäui  . .  hau  vTspanam  . .  spa- ct^ranam  V. /J.  16;  —  spä  *ius  V.^.^j.
12785:j  —  mit  Numeruswechsel: %''ärayam  kärahyä  .  .  fyädÜ  gaumäi^ I  adifiiT  ".  .  des  Volks  .  .  was  ifanen  . JBh. /.  14;  —  tyJ'  imaiy  käram  aduruß- yast^  pasävc^  '//"  a'urJ'miadil  matUl dastayl  akunatd  ya%a  mam  iäma"  aAa* ava^ä  °»/'>  akunavam  Bh.  ^4;D  —  ö/n aoi  ibasSa  paityantu  i^yeja  .  .  yö  T  da%a ..yidf(AFn.)  daU  Y.65.8.  S.  noch Anhaug  a.  a)  zugleich  auf  das  gleiche Nomen  vorausweisend:  sparum  uldnm  . . yasla  dim  janal  .  .  spän>m  sTsdr^m  V. 13. 3.  3)  auf  ein  Relativ  als  dessen Korrelat:  yS . .  gai^i  aioAe  mfrrfmte  avi tu  °im  disyata  .  .  Y.  Ä  3;  —  yasca  .  . fatmmazS  gSus  da%at  nHl  'im  .  .  paiti.- pirfSimnB  bva  (sd.)  V. /<¥.  29;  Yt/.  18, II.  5;  —  s.  noch  Anhang  b  t.  II)  vor- ausweisend; i)  auf  eine  erläuternde nominale  Beifügung:  a  *'lm^''  iavaiti  aiwi.- vanyä  äagnS  yS  apaoi'S  ti^ImYt,S.if,  72, iZ  iäim),  aS  (^j^ffi)"';  —  ä  'im  ta  va^a ramayai  ahurS  mazda  ..tarahustnm  V.5. a  I ;  —  paiti  *'lm''' {ASQp^rfsat  sardhuitrs aridvlm  särqm  Yt.5. 90, 94  {dim) ;  —  ä  'im (ais ASa.) Jramraami  abm  vahiit^mHt.^.^; —  s.  nodi  1 1  a  und  Anhang  b  ß.  a)  mit lelativiscbem  Anschluss:  yaiaca  'im  janai .  .  yim  viptim  vä  V.  7.  52  PUZ.;  —  aOat 'im  vlspanqm  matistsm  dazdyäi  ahBmca ratBmca  yim  ahur?m  Y.  27.  i ;  tg.  la,  Vr. II.  i\.  2)  auf  ein  Relativ   als    dessen
13246:—  'i>  NA.  u',jm";  s.  aber  IF,  7.  79  und  Ntr. lur  NA.  Es  liegt  nahe  iBild.  lat.  danon/  lu vergleichen;  doch  s.  Suumek  LatLaut&For- menL  527,  —  »'.)  Pü. ;  andar  däsl  hl^l.  — 'S)  So  jedenfalls  viel  einfacher  als  bei  Gdn. BB.  15.  »59,  GlrPh.  2.  32,  Bk.  Stnd.  /.  355. Pü. ;  iaiärfi  I  hac  asläa  .  .  pahlum  dakän  pa har  t  ax'än.  —  '*)  Pü.:  o;  s.  No.  17.  ■ — >7)  PO.;  dSrend;  wegen  des  Anklangs!  — »S)  Pü.:  n7  dahua.  —  »9)  Vgl.  Yt  13.  50  usw., No.  10.  —  30)  Pü,:  spar  di-utan;  vgL  Sp.  728 in  däili.   —   ä')  Pü.;  pa  uuiaiim  i  apar  hSm.
16707:KompE. ;  Ableit.  -  ai.  rgl.  b/rnAgä-  f.  i)  'HanP, )  "■  i-adknaU,  baddhäh,  mi,  batdhau ;  np.  bandad, a)  ■Narttotittum  aus  Hanf  J) ;  np.  bang  'Bilsen- 1  *"'■"■  —  ^^-  ■  *'"'""■  —  ''  Beide  Stammformen kraut'.  —  Pii. !  mang-*),  erL :  /  vihäspi».  —  hBchst  unsicher;  s.  No.  3  und  4-  —  •>  S  53  H- t)  «h,  «gk  statt  ng,  TgL  S  36S.  47,  46  und  .  —  "  Es  wird  wohl  bandayat  gememl  sein.  — die  Var.  lo  V.  ig.  20.  41,  Yt.  13.  124,  femer  1,  «  So  F  1 ;  iSPA.  mit  Ibem.  Ausgang;  vgl.  b,ba- sparnka-,  pisöHngka:     —     ")  Vgl.  dazu  JUSTI ,      '"'""'•     NA.  bandämi.
16840:"wenn    sie  Kleid   um  Kleid    anlegen    — :  —  tntinm  ..yspara  ratiää  (sd.)  baraiti
17822:sae^antätvirshraynaiY.  26. 10; — gSuicä hudätahs  gayehyäcä  mard^nB  .  .  °itm  Y. y-  7;  2j.  a,  26.  S,  Yt  13.  87;  —  «ÄM^ zar^uStrahe  ipitämahe  asaons  -sie  Y.  6S. 22;  3. 2,  4. 23, 16. 2,  23. 2,  24-  S,  7'-  2-  Vr. /ö,  2,  YtÄ  2,  J_J.  87,  Vd.(?;  —  ahe  nars aSaonS  'Jtm  yazamaide  yS  asmffj^ativä nqma  Yt,  /. 30;  13. 95 ff.  (oft),  Y. 23. 2, 26. 5% FrW.  2. 1,  3;  —  hvSuyä  asaonyä  'sim  Yt ''5-^39!  '39f-'*;  —  kanyä  *va}>uis  asaonya [. .]  °slm  Yt  13.  141 ;  141  f.'°;  —  auch  dem AÄM.  und  andern  Gottheiten  wird  eine Fr.  KUgeschrieben**':  vispanqmca  anAqm paoiryanqm  'Sinqm  .  .  °sm  avqm  yqm ahurahe  masda  .  .  °iay5  .  .  ya  ampsanqm spintanqm  .  .  yqmca  ährö  urväzistake  .  . yqmca  sraohhe..yqmca  alnSyqmca  apH.. YtJ^.  80-86;  Y.26.2i.,  V./»?.'4; — äyese yelti  *ä  *fravaM<y)'^  ahurahe  mazdä  am»- sanqm  sparUanqm  . .  Y.  25. 2 ;  —  gaom  (statt Gen.)  agvJS-dätahe  urunB  °Sim  S.2.  I2;i2; —  sogar  den  Fravalay  selber  (!) :  aSäunqm "sinqm  uyranqm  .  .  paoiryjJkaisanqm  'si- nqrrt  nabänazdistanqm  'ünqm  '/ayU  xihaiä ayantu  ahmya  nmaneYt.i3.1s6.  A)/ra- vaHnqm  a)  (näral,  mä)  heisst  der  i .  Monat  im Jahr^:  asäunqm  'sinqmY.i. 11.  ß)(näml, ayar?)  heisst  der  19,  Monatstag:  asäunam 'sinam  uyranam  S.j.  19;  vgl. 2. 19,  Y.10.5. •)*Nach  dem  GrBd.  (s,  DsT.  ZA.  3.  500, Blocket  RHR.J2. 104)  ist  der  Mensch  aus  fünf Bestandteilen lusammengesetit:  ian,yän,  nmän, äiinai  aad /ravakr.  Vom  letzten  heisst  es; y>ti- vahr  an  i  pcs  i  Öhrmazd  i  :^aiäl,  und  über  sein Verhältnis  mm  fiß/ö»  wird  geiagt:  ruvän  S/ra. vakr  pativast,  ku  iän  rm/ä»  marnjcmtan  ne  tiniän. S.  noch  DkB.  269  {218.  6):  io  (fravahr)  haf  lan yut  bavtt  lan  hil  lör  u  aiär  mänri.  Die  Schaffung der  fr.  (bei  West;  "prolotypes,  primary  ideas of  the  good  creations")  ist  nach  Bd.  /.  8, 34.  1 zu  Beginn  des  ersten  Mitleniums  erfolgt;  nach 2.  10  f.  entscheiden  sie  sich,  'lan  tariaiihä'  gegen die  Welt  der  Driig  zu  liämpfen.  Über  ihre,  ins- besondere  kiiegeiischeTäligkeitalsSchutzgeister und  Manen  gibt  das  ihnen  gewidmete  Yt  13 Auskunft.  Ihre  Zahl  wird  Yt.  13.  59  ff.  auf  99  999 eingegeben,  vgl.  jcludra-*)  and  Mx.  4g.  16,  52. 23,  29;  weniger  bestimmt  Yt.  13.  64,  66.  All- jährlich während  der  letzten  fünf  Tage  der sechsten  (letzten)  Jahreszeit  und  der  sich  an- schliessenden fünf  Schalttage  kommen  dieManen, ihre  frühere  Heimat  zu  besuchen  (Yt.  13.  49) und  werden  dann  besonders  gefeiert  (s.  hantas- pa%niae<iaya-)ii).  Vgl.  noch  Cld.  Totenverehrung 48,  BahadoorN.  D.  Khandalawala  Cama  Mem. Vol'  205,  JN.  GIrPh.  2.  643,  SÖDEftBLOM  RHR. 3g.  229,  373,  La  vie  future  7.  Das  Nichtauf- treten  der  fr.  in  den  (eig.)  Gä%äs  (s.  unten  No.  l) ist   bemerkenswert;    zum  Teil   aber   entspricht
17881:strafen'^';  mit  Akk,  a)  II  der  Person:  mar- tiyi^  kyc^  .  ,  avam  *^uiaratam  abaram  I iSya*  .  .  avam  *'^/rasatam  (sd.)  sparsam  j Bh.^.  13;  7.  8;  —  avaiy  akifraltsdiy  (sd.) /arJjBh.4.14;  5.  b)  dcrSache,  in  Ver- bindung mit  IS.  frasa  (sd.):  yä  frasä aviSyä  yä  vä  ..  *p^nsam  (3DPM.,  als Pass,)'°*  taya  Y.jj.13.  Wertlos:  tatiBm p>nsänte  Vyi.40.
17913:frasparana-  1 00a
17934:I003  frasparflya-
18324:•  '].  (frJcnk-)  Adj.  'nach  vom,  herzuge- wendef ;  nur  ISn.  fra^a  und  NSm.  frql als  Adv.  1)  fraca  "voran,  hervor',  nur  ^ Praev.  mit  V.  Aarpt-  sva.  fra-karst-,  Y. 9.8".  2)  frqs'^  a)  'voran,  von^its': hö  mairyS .  ./f  ayanhs  frasparal  ". .  vor- wärts schnellte  er  unter  dem  Kessel  her- vor" Y.p.  11;  F.  13;  —  mit  AbL^);  vm- %raynB  .  .  yS  yr"  *lacS*'^  hamfn%ä%a  .  . ni/ainti  ".  .  der  dem  Gegner  voran- laufends*.."  Ytio.71.  b) 'herzu,  heran': ndit  iiira  .  .yr°'>  iyä/  (Sp.  270  o.)  Aagna . . "nicht  möge  hier.,  herankommen  Feindes- heer" Yt.  Ä  s6.
20719:mSi  y  tvSm  vidvä  (sd.)  Y.  48.  2 ;  — y  xsa- 'iirS  *grjhmS  hjsasat  aaüaAya  dtmäni  ma- natjhff..Jigfr)sat{zA.)Y.32.ii.  2) 'wenn' 3': ma  eis  ,  .  frarmharat  y  nsit  .  .  atnats Ytio.  uz.  a)  vorher  geht  ta  (Stverz., Sp.  612  in.):  tum  tä  daiiikävB  nipahi y  Auhnitlm  yaiayeiti  (sd.)  Yt./O.  78;  78; —  kai  tä  nara yaoidayqn  anhm  ..y  na- säum  franukarat  V.7. 2  3 ;  usw.  3 )  'dass', einen  Subjekts-  oder  Objektssatz  einleitend; a)  mit  Konj.;  a)  vorher  geht  tal:  taf  (Sp. 618  m.)  mazda  tava  xsdhr^m  y'  .  .  dähl drigaovi  (sd.)  vahyu  (wörtlich)  "das  ist (darin  besteht)  ..  deine  Macht,  dass  du  .." ^-53- 9.  ß)  voraus  geht  ta  (Sp.6i 2 m.): yäi  yO/tJ  /ramTma%a  (sd.)  y^  masya  ,  . vaxi?iili  daivS^ustä(%±)\.32.^.  b)Ver- bum  fehlt:  dastü  .  .  y  vS,  mqhra  srivTnt äradä\.28.T, —  £K//(Sp. 272  o.)^"  *aya»- haina  spar^a{sA.)  Yt  io.  129 Gl.  4)'auf dass,  so  dass,  damit';  a)  mit  Ind.:  a  ma äidSm  . .  y  sruyi  pari  (sd.)  *magaong  Y. 33- 1-  b)  mit  Konj.  (oder  Inj.):  aAyä yäsä  (sd.)  .  .  syaahana,  vaiahSui  xratüm manarvhS  y  xsnnlia  (sd.)  gSui^a  *urvq- n>m  Y.2ÄI'';  — aivä  vJspSng  äySi..y aiat  haca  jvamakT  {&A.)  Y.^J/.S;  —  tsm .,  varam i^t.) y^  fo%rdi  »r<A!/(sd.)  Y.j^. 4;  —  at  töi  myazdim  .  .  däma,  gag'hä vTspä  ..  */°*'  voAß  %raosta  (sd.)  manariha Y.J4.3";  —  ..hatayme..hutaosqin  anu- matSe  dalnayai  . .  y'^'^  ml  daSnqm  . .  zras- (sd.)ca  däl  . .  y^^  ml  vanzänüi  va^uklm dat  frasastim  YL 5.  26;  —  eaval  dbötUim ayantm  fararshacäiti {&A.)?  y'^  *frayar3ne va..  aiwyäs/isisd.)  atpAalii.g.  c)  mit Opt.:  tat  n3  ziTdvanöi (sA.)  vaoca  ..y°  jvantd vXspSiig  vauraya  (sd.)  Y.JJ.3.  a)  voraus geht  tat  (Sp.630  o.);  akyä  ..  nS  dStdl .. tat  ahya  y  tat  upa.jamyama  .  ,  Y.  ^o. 2.  d)  das  Verbura  fehlt;  frasravayö ava  diJkra  yim  dim  vasnat  *svistaih)a (sd.)  *vindän3m  nBtt  *ava  y"  *vistaliva N.  iö'".  Undeutlich:  y   ahmst  (Sp-
21114:—  yöi  aipi.kinnt>nti  vTspsm  du?mat.-m\  nöil  masyS  ..aoj0{sA.)virfzyaii  duzvarsttm .  .  mq/iayfft  ahe  y  atars  Auikim' y°  miirasat  .  .  v?r?syäti  hvarstsm  Yt.  IQ. aismwi  .  .  aipi.hr)ntaili  kavayelti  (sd.)  106;  106'.  b)  im  j-'-Satz  ist  das  Prae- daiaiti  Y.  7/.  8;  —  us  .  ,  iristtm  baray»n  dikat  weggelassen;  die  verglichenenNomina mqnaytn  ahe  y  nä  däUyJ  *däi/yrii  (sd.)  stehen  im  gleichen  Kasus:  swütö  bavähi  y *bairyeitica  . .  V.5.40; —  upa  Al  gaon^m  mazdaAz.2;i—j*9^\yt.2—^'"; — y5  hÜtaite baraiti  mqnayin  ahe  y  nä  fryö  fryäi  \vldkva  y  sästa  Yl  14. 13;  — yS  avavai vaiitaoe  ,  .  giJoii>m  vä  avi  ava.baraiti  V.  \xsva^vö  vasifite  ,  .  y'  ityri}  YtÄ6;  — j.as;  —  mqnaysn  ahe  dama  ..  nars\paiti  ifar^^a  :^araiti  y  ÜhravaY.l^.i,^; asaoiiS /ranunzaiii  i'lsppm  dusmaiimca  . .  —  mqnay^n  ahe  y  vis  alm  (Yi±m[.  asti) y  viltö  ..  %wSi»n  dasiniii  pairi  fram}r>-  Yt-ij,  aj  V.y.  45-48'*;  —  mqnay^n  bä siiiV  V.J.  4a;  —  tl  mqm  ava%a  vtnnsnte  . .  nasus  zga'iaite  y  isusY.g.afi;  46,  Ä69, y  anyftsHt  arsänä  ax'i  xludra  x/a^n'^a  21  PiiZ.'(?);  —  nsij  masyJ  .  .  aojs  suru- kqm.v?r3navainti  V.  /Ä  3a;  —  svisifm\naoiti  .  .  y  mi^rascil  YL  10.  107  •>;  — y  dTs  avai'iayat  ahurS  Vr, //.  19';  — \>H3rin'aite  vlspqin  daiähaom  y  satim aiiihä  s)mo  pälnabya  vJspara  sastaabya^kaymanqm  avava^  aj^ava.jaüi  Yx.io.2; vTxäf,a  mqnayin  ahe  y  na  masyäka  —  jahikaysi  .  .  ye/ihe  ^frafravaite  manS *xMsti  ami  visävaydnte   V.  2. 31;  7.  55;l>'°  awr?m  Y,  ^.32; — pasca  yän.dräjo  vasd
21504:'sieden,  sich  in  Siedehitze  befinden': yaihnia  (3?.)^'  fatmta  "(die  Wasser) siedeten,  flössen  über"  F.  4f-;  —  ffqs (sd.)  ayanhsjrasparat  yais'yantim  äptm *paraiihät  "..dassiedendeWasser schüttete er  um"  Y.p.ii;  —  *ya!s?ntim*'  äp>m F-^f.;  —  niioyäti  (sd.)  il . ,  ätari . .  kala yastibys  (DPf.)"  aiwyiJ  ".  .  vor  den siedenden"  Wassern"  P.  2/.
22691:vayaspara-  1358
22707:NB.  34a,  FoY  KZ.  3S-  Ö3  ('»childfl«chtend' ; aber  'Schild'  wäre  ap.  *sparar,  i.  np.  npat; auch   anapaßäpat   bei  Mesvch  dürfte  anf  ap.
24284:■  j.  vira-Dhad-  Adj.  'Männer,  Krieger an-,  überfallend':  aiiS  asparaAätö  'ahohs (NS.)  Aog.  7*.
24482:•  j.  viape  ratavö  (NP.)  'alle  Ratat/,  Be- zeichnung eines  Buchs  des  Awesta;  ge- wöhnlich ^Visparad"  genannt  (s.  dazu  GIrPh. 2.  5):  mä  eis  m!  ätihqm  taokranqm  fra- tmharät  ya  nüil  staotanqm  yesnyanqm Jma/S  (sd.)  V  r*  Yt.  JO.  I2a'>.
25353:•  g.  räd^ma-  Adj.  'zusammengehörig mit  — ,  anhängend  an  — ',  mit  haia  und AbL:  yS  'mS  aiat  Aala  "der  dem  A.  an- Mngt"  Y.  44- 1 7 ;  —  tirajs  hala  •ms  (LS.)'» ySmf  sparuha  (sd.)  fraidtm  Y.  ^J,  6.
25366:•  g.  'rana-,  runa-"  m.  'Streiter,  Kämpfer', nur  Du.",  von  den  mit  einander  im  Streit liegenden  Religionsparteicn^':  yam  x^nü- Um  (sd.)  'neibya  da  %ws  ^rä  tuxrä masdi  ayanhs  xfuita  (sd.)  "was  du  als Belohnung  den  beiden  Parteien  durch dein  rotes  Feuer,  o  M.,  durch  das  ge- schmolzene Metall  bereiten  wirst"  Y.ji.  9;
25595:•  j.  'urvata-  Adj.  -  ?  -,  bezeichnet  eine gute  Eigenschaft  des   Kameb:   uitramim •«{statt  GP.)'>  samiJiao/anqm    \.22'.y, —  ttstmhe . .  aiwijaanahe  'tu  (statt  GS.) frasparanahe  \\.14.\\.
26823:—  yS  s  Bne  pHtmn  jainti  yim  pasuLhmirve V.  y,  10;  11;  —  yB  spariam  jainti  yim pasui.hauruM  . .  V.  ij.  12;  14-16;  —  M'a asti  spa  pasus.haurvö  dailyff.gatuf'W.  13.1T, 18,  19;  —  yS  spamm  larspi'^w^m  *dasti yim  pasus.haurum  V.  y.  20;  21- yS  siine  yim  pasusJiaurve  vä  visMaurve va  astanqm  ahmar^tanqm  daaaitiW.i^.y,
26841:spar-
26844:1)  'treten,  stossen';  ma  %wä  dasna mäzdayasnii  aspake  sparSit  sparmaini  (sd.) Vyt..?5-
26845:mit/r,j  'hervorschnellen',  intrans.: /wj (sd.)  aya»h5  frasparai  Y.p.  11.
26846:mit  Vi  'auseinandertreten,  -stampfen'; aiAhh  z^mS  (sd.)  pasnäbya  vTspara  V, 2.31;  32  {wo  visparai).
```


## [2026-09-14T02:29:22.358Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG spar ===\"; grep -n \"SPAR\\|spar-\\|\\*spar\" CHEUNG.txt | head -40"
}
```


### [2026-09-14T02:29:22.416Z] TOOL RESULT

```
=== CHEUNG spar ===
22942:*spar 351 
22960:*spar ‘to hand over, entrust’ 
22963:"psp ’I- /abespar-/ ‘to hand over, entrust [+ ’w 407], give up one's honour, life; to 
22985:-spard, Gz. ispär-/ispärt, Gil. (Rsht.) ispurdoen/ispur-, Ham. espartan/espar-, Isfah. 
22986:espartän/separ-, Khuns. ispar-/ispart, Soi bé-spar ‘to hand over, entrust to’, Siv. 
22987:isperd ‘to hand over; to say’, ? Gur. (Kand.) -spär- ‘to bury’ (rather *sparH ?) 
23010:352 *spard 
23013:*spard ‘to twitch, quiver’ 
23023:*NEIR: Wa. spardanj ‘flea’ (< *spardanaci-) 
23037:*sparH ‘to tread, kick’ 
23039:*AVESTAN: YAv. spar- ‘to tread, kick’ || (+ *fra-) ‘to tread forward’ || (+ *ui-) ‘to 
23045:*MIDDLE PERSIAN: BMP spl- /spar-/ ‘to trample, tread’, BMP splyh- /sparth-/ (pass.) 
23050:*KHOTANESE: (+ *aua-) LKh. *vaspar- (vaspud-) ‘to trample on’ || (+ *a-) OKh. 
23051:*aspar- (äspid-, äspud-) ‘to tread’ || (+ *upa-) LKh. *paspar- (paspud-) ‘to trample 
23056:*upa-hispar-), MSogd. pspr’mndyy ‘fixing’ (GMS: §1100) || (+ *ni-) BSogd. ’nspr- 
23086:*IE COGNATES: Hitt. /ispar-/ ‘to trample with the feet’, Lat. spernere ‘to push away, 
23095:*sparz ? ‘to aspire to, strive’ 
33726:spar-, 352 
34915:"psp 1- /abespar-/, 351 
35541:spl- /spar-/, 352 
37227:*paspar- (paspud-), 352 
37659:*vaspar- (vaspud-), 352 
43097:-spar-, 351 
43675:-spard/-spar-, 351 
43751:ispar-/ispart, 351 
43976:espartan/espar-, 351 
44224:ispar-/ispart, 351 
47653:spar-, 351 
52156:/ispar-/, 353 
55223:*sparz 
56475:*spar 
56777:*spar 
56944:*sparH 
57508:*spard 
58079:*Hiaud, *sparz 
58239:*sparH, *xramH 
58252:*spard
```


## [2026-09-14T02:29:25.482Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22940,23100p' CHEUNG.txt"
}
```


### [2026-09-14T02:29:25.534Z] TOOL RESULT

```
*spar 351 


*span(d)/sfan(d) (?) ‘to become agitated’ 

*KHOTANESE: OKh. sphan- ‘to agitate’ = SGS: 136 

*CHORESMIAN: (+ *fra-) ? špn- ‘to cough, groan, sigh’ = Samadi: 198 

*SANSKRIT: ? spand ‘to twitch, lash out (of animals)’ (RV) = EWAia II: 773 

© The existence of this root is uncertain, as the evidence is rather limited and 


ambiguous. 
*REFERENCES: DKS: 437b; Werba 1997: 384 f. 


*spar ‘to hand over, entrust’ 

*MIDDLE PERSIAN: BMP spwit /spurd/ (ppp.) ‘conducted (away)’ || (+ *upa-) BMP 
"psp ’I- /abespar-/ ‘to hand over, entrust [+ ’w 407], give up one's honour, life; to 
commit suicide, extradite someone (to be executed, tormented)’ = DMMPP: 17a 

(+ *upa-) Pres.: IND. 2sg. BMP ’psp’lyh /abesparéh/, 3sg. BMP ’psp’lyt /abespared/, 1р1. BMP 
"bsp'I(y)m /abesparem/, 3р1. BMP ’psp’lynd /abesparénd/; Partic.: pres. BMP ‘psp К /abesparag/, perf. 
pass. BMP ’bsp’It/abespard/, BMP "pswlt /abespurd/; Inf.: BMP ’psp’Itn /abespardan/ 

*PARTHIAN: (+ *upa-) "bysp'r- ‘to hand over" = Ghilain: 75 | DMMPP: 17a 

Pres.: IND. 3pl. ’bysp’rynd; Partic.: perf. pass. 'byspwrd 

*SOGDIAN: (+ *pati-) ? SSogd. pspr- ‘to fix, compose, level’, CSogd. pepr- ‘to alight, 
rest’, MSogd. ptspr(t)- (pass) ‘to be arranged’, ? SSogd. ptspr PN (UppInd.4, 
UppInd.71, UppInd.227, etc.) 

Pres.: IND. 35р. CSogd. pcprty; Impf.: IND. 3pl. CSogd. ptysprnt; Partic.: perf. pass. SSogd. ptsprtyy; 
Pass.: pres. IND. 3sg. MSogd. ptsprtyy ‘is arranged’ 


*CHORESMIAN: (+ *upa-) bsp’ry- ‘to hand over, entrust to” = Samadi: 26 

*NWIR: NP sipär-/sipurdan, Bal. siparit/sipar- (< NP), Fariz. -spärd/-spär-, Yar. 
-spard, Gz. ispär-/ispärt, Gil. (Rsht.) ispurdoen/ispur-, Ham. espartan/espar-, Isfah. 
espartän/separ-, Khuns. ispar-/ispart, Soi bé-spar ‘to hand over, entrust to’, Siv. 
isperd ‘to hand over; to say’, ? Gur. (Kand.) -spär- ‘to bury’ (rather *sparH ?) 

*NEIR: Sh. sipör-/sipört ‘to charge, commission’ (< Pers. ?), Yzgh. s(a)pard/s(a)par-, 
Wa. s(a)por-/s(a)pord/t- ‘to hand over’, Pash. spär- ‘to entrust, commission’ (< Pers. 
?) 

*MISC: Arm. (LW) apsparem ‘I hand over? 

*SANSKRIT: ? spar ‘to save, secure; deliver; gain” > EWAia II: 773 f. 

© This amply attested root may have an IE provenance, being connected to the 
Germanic spare forms. 

«PIE *sper- ‘to deliver, secure’ — LIV: 579 | Pok.: 992 

*IE COGNATES: ON spara, OHG sparön, OSax. sparon, OE sparian, Engl. to spare 
*REFERENCES: КРЕТ. 246b; KPF II: 203; Christensen, Contributions I: 67 f., 165; Abrahamian 1936: 112, 


129; Edel’man 1971: 239; EVS: 74; Nyberg II: 27b f.; DKS: 69; WIM II/1: 77; WIM III: 110; Werba 
1997: 262 f.; Steblin-Kamenskij 1999: 323; Shahbakhsh: s.v. sipar- 


352 *spard 


*spard ‘to twitch, quiver’ 

*AVESTAN: ? OAv. sparada ‘diligence, zeal ?’ (Y 53.4). 9 The interpretation of this 
formation is extremely problematic, on which see Kellens — Pirart III: 269. Even its 
existence can be doubted, as it depends on the analysis of the word boundary. 
*KHOTANESE: LKh. spal- (spa’-) ‘to twitch’ = SGS: 135 

*SOGDIAN: BSogd. csmy ’sp’röt ‘quivering, twitching eyes’. Ф Cf. Gershevitch apud 
Bailey 1951: 36 ad spalada-jsai ‘with quivering eye’. 

*NEIR: Wa. spardanj ‘flea’ (< *spardanaci-) 

*SANSKRIT: ? spardh ‘to contend, to fight for something’ (RV+) = EWAia II: 774 

9 The connection with Skt. spardh is semantically not evident. 

«PIE *sperd'- ‘to move quickly or suddenly, run away ?' > LIV: 580 | Pok.: 995 f. 
*IE COGNATES: Hitt. /ispartmi/, Arm. sprdem ‘I escape’, OE spyrd ‘race, running- 


match’ 
*REFERENCES: DKS: 436a; Steblin-Kamenskij 1999: 315 f.; Werba 1997: 263 


*sparH ‘to tread, kick’ 

*AVESTAN: YAv. spar- ‘to tread, kick’ || (+ *fra-) ‘to tread forward’ || (+ *ui-) ‘to 
tread apart’ = Liste: 64f. 

Pres. them.: INJ. 3sg. YAv. frasparat (Y 9.11), OPT. 3sg. YAv. sparöit (Vyt 35), IMPV. 2sg. YAv. 
vispara ‘kick out, away’ (V 2.31) 

*MIDDLE PERSIAN: BMP spl- /spar-/ ‘to trample, tread’, BMP splyh- /sparth-/ (pass.) 
‘to be trampled (to death)’ || (+ *pari-) MMP pryspr- ‘to tread, trample’ || (+ *ni-) 
MMP nyspwrd (ppp.) ‘tread underfoot? = DMMPP: 282b, 254a 

Pass.: pres. IND. 3sg. BMP splyhyt /sparihed/ || (+ *pari-) Pres.: IND. 3pl. MMP prysprynd 
*KHOTANESE: (+ *aua-) LKh. *vaspar- (vaspud-) ‘to trample on’ || (+ *a-) OKh. 
*aspar- (äspid-, äspud-) ‘to tread’ || (+ *upa-) LKh. *paspar- (paspud-) ‘to trample 
on’ © SGS: 121, 13, 79 

*SOGDIAN: (+ *abi-) BSogd. Bsp’ry ‘sole (of foot)’ (GMS $370) || (+ *upa-) CSogd. 
pspr- ‘to trample on’, MSogd. p’spr- ‘fix, compose, level’ (< redupl. pres. 
*upa-hispar-), MSogd. pspr’mndyy ‘fixing’ (GMS: §1100) || (+ *ni-) BSogd. ’nspr- 
‘to walk’ 

(+ *upa-) Impf.: IND. 359. MSogd. p’spr, Pret.: tr. IND. 3sg. CSogd. psprd’rt, Partic.: perf. pass. CSogd. 
psprty ‘trampled’ || (+ *ni-) Pres.: OPT. 35р. dur. BSogd. ’nspr’y 'skwn, 3р1. BSogd. ’nspr’ynt, dur. 
BSogd. "nspr'ynt ’skwn 

*CHORESMIAN: m/sPr- ‘to tread’ || (+ *a-) ?? ’br- ‘to trod’. Ò Perhaps ’br- = ’pr- 
(MacKenzie 1975: 394; MacKenzie I: 553), with unexplained loss of -s-, Samadi, 
l.c. = Samadi: 185, 23 

*NWIR: NP sipardan/sipar- ‘to trample; to be trampled’ 

*NEIR: Oss. I. æfsæryn/æfsærst ‘to press on; to push (something in something)’, D. 
efserun/efsarst, aefsard ‘to kick with the feet’ || (+ *upa-) Sh. bispär, Khf. bispar, 


*spas 353 


Rosh. bispar, Yzgh. baspur ‘a kick’ || (+ *ni-) Sh. nixpar-/nixpud, Sariq. naxpe(j)-/ 
naxig, (Shaw) naxpor-/naXpug ‘to tread down, trample with the foot’, Wa. nasp(a)r-/ 
naspard- ‘to kick (with the feet)’. 0 The existence of Wa. bisper ‘to kick’ as cited by 
Lorimer has not been confirmed by Wa. informants, v. Steblin-Kamenskij 1999: 
250, s.v. пәѕр(ә)г-. 

*SANSKRIT: sphar ‘to push away with the foot’ (RV+)  EWAia II: 776 

«PIE *sperH- ‘to kick with the feet? = LIV: 585 f. | Pok.: 992 f. 

*IE COGNATES: Hitt. /ispar-/ ‘to trample with the feet’, Lat. spernere ‘to push away, 
despise, reject’, ON sperna ‘to kick out with the feet’, Lith. spirti ‘to kick out (of 


horses), to defy, to sting’, etc. 
*REFERENCES: IIFL П: 532; Abaev, Slovar’ I: 483; EVS: 21a, 52; DKS: 436; Werba 1997: 329 f; 
Steblin-Kamenskij 1999: 250, 457 


*sparz ? ‘to aspire to, strive’ 

*AVESTAN: OAv. ("ä)sparaz- ‘to aspire to, strive’? = Liste: 65 

MED .; Pres. them.: INJ. 3sg. OAv. "asporozata (Y 31.16). 0 Differently Humbach, Lommel ("inf."), Insler 
1975: 188 ("subst. Isg. ‘eagerness’").
```


## [2026-09-14T02:29:46.440Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sipurdan\\|sipardan\\|sipärdan\\|spurdan\\|uspar\\|us-spar\\|uz-spar\" HRN.txt | head -20; echo \"=== leaf 175 (p154) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==176' HRN.txt | head -60"
}
```


### [2026-09-14T02:29:47.526Z] TOOL RESULT

```
=== leaf 175 (p154) ===
— 154 -
694. (2)säii 'Teil, Stück; Art und Weise'; -$an gleich,
ähnlich, -sä.
Die Deutung von aw. sü^ia- (yt. 19, 44) als *Stück'
(Studien, I, 148) hat Geldner BB. XV, 254 wider-
rufon.
LW. kuid. säriy z. B. kH\sän *öü; wie?', va]suna auf
diese Weise'; afy. San; bei. sang (236).
Np. -sä^) hat das auslautende n verloren, wie äsuid,
a (No. 52), senrjso (Käs. Z. zu 1. süh) u. a. ni. Gehört
np. 'äsan 'äsä gleich, ähnlich* auch hierher?
695. säf/e 'Schatten, Schutz'.
ai. chayd' 'Schatten'; plilv. sayak,
kurd. se^ si\ bei. säig, n. saJ (340); wa;^. LW. sayd,
sar. suyä,
696. supär Tflug .
ai. phdla- Tflugscliar*, zu l^phal-, splial- *aufreissen'.
sar. spur 'Pflug .
697. Hiipävden anvertrauen, übergeben*, jüd.-pers. p1N?10,
supiirden, sipäris (sifärls).
g. vaspartmün.
aw. tis-\- 2. l/'par-; phlv. avspärtan, avspurtan. (vd. 5
(77)), spiirtltan (AV.); ai. iid -{- "lA^par- 'hinüber-
führen', utpdrana- 'Übersetzen*; vergl. lat. portäre.
af/. späral übergeben'; kurd. sipärtin.
Die Etymologie stammt von de Lagarde, ist aber
sehr unsicher. Bei siperl (No. 703) passt die An-
knüpfung an l^par- ausfüllen* besser.
698. »Ipäs 'Dank*.
phlv. späs, späsdär; arm. spas-em aufwarten, dienen',
spas 'Dienst'.
^) Np. sä *Tribut* ist dagegen au8 *sävaka- entstanden, vergl. die
Form säv (Nöldeko, Pers. Stud. II, 20 Anm. 4). In der Bedeutung
'kostbare Art Stoff* (Vis und Rämln 52 Vers 7 v. u.) wird es ebenfalls
hierher gehören.
```


## [2026-09-14T02:30:01.355Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB sipurdan/spar ===\"; grep -n \"supärden\\|sipurden\\|spärtan\\|spurtan\\|sipärdan\\|sipurdan\" HUB.txt | head -20; echo \"=== HUB spihr ===\"; grep -n \"spihr\\|sipihr\\|sipehr\" HUB.txt | head -20"
}
```


### [2026-09-14T02:30:01.422Z] TOOL RESULT

```
=== HUB sipurdan/spar ===
2554:697. Im Phi. ist apspurtan zu lesen, vgl. arm. ap-spar-em
2560:Gram. § 41, c). Fiir phi. spurtltan ist spurtan zu setzen,
5031:spurtand d. i. paz. spurd and Gl. and Ind. 156); supurz *Milz'
=== HUB spihr ===
2580:707. Np. sipihr 'Himmel' ist nach NSldeke direkt =
6076:paz. spar; sipihr 'Hininier = skr. gvifrd-; siped weiss' = zd.
6295:sipihr 'Himmer H. 707, sipBd weiss' H. 708.
7319:vgl. np. mandcihr (?) Fird. I, 95, 618; sipihr 'Himmer, phi.
7320:spihr^ ap, ^m&paiaTtjg, JSmd^ptddrjjg (Ktesias, Xenoph.
7557:*Raute' = zd. spenta-; siped Veiss' = zd. spaeta-; sipihr
```


## [2026-09-14T02:30:03.009Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD spihr/spurdan ===\"; grep -n \"spihr\\|spurd\\|abespar\\|spar-\" PHD_mackenzie.txt PHD.txt | head -30; echo \"=== NYB ===\"; grep -n \"spihr\\|spurd\\|spartan\\|spar-\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-14T02:30:03.131Z] TOOL RESULT

```
=== PHD spihr/spurdan ===
PHD.txt:166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
PHD.txt:386:e--rób [-lwp | N jārē(b)] broom. geän [HY A < А hy’; yn! | M gy’n, N jan] soul, ghost. ~ kandan: give up the ghost; moment of death. ~-abespar [-^5sp?! | N jān-sipār] reckless, desperate; devoted. ~ig [-yk! | M -yg] spiritual; vital. | ~war [-wl | (P -br), N jánwar] animate; animal.
PHD.txt:518:6 [OL < А Ч; ?w | M ’w] to, at; v. also 6h. ~ gird ámadan: gather, collect (intr.). — ham kardan: gather (tr.). ~ ham madan: gather (¿ntr.); come to an end. *óbad-, v. bastan, *óftadan. Obārdan, bär- Dwf?l-tn! | M ?wb’rd] swallow, devour. Obastan, *dbad- [NPLWN-stn! < A У npl; ^wpstn!, ^wpt- (if not Oft-, q.v.) | M ?wbyst, J ^wfst-] fall. *oftadan, Oft- Pwpt- | M *wpt'd, N uft~] fall. Gear Pwk’l] ebb. ogardan, ógàr- Pwk’l-tn'] remove, expel. *брга ['wgPy] declination, dip. Sh [KN < A kn | Mwh] so, thus; (with verbs, giving a sense of uncertainty) may, perhaps. Ohrmazd Pwhrmgd | M ^whrm(y)zd, N Hórmuzd] Ahura Mazda; astr. Jupiter; cal. 1st day of the month. -om [-wm | = M, N ~] suffix forming ordinal numbers from panjom onwards. -mand [-’wmnd | M -wmnd, N -mand] suffix forming adjectives of quality. *óréb(ih) [wlyp(yh)] disappointment. Dron ['cwlwn! | Mwrwn] hither. ад... ~: since. osán- Pws*n- | = M] throw down. óspurdan, ӧѕраг- [”zospl-tn!] tread, trample. 051°, v. awest^. Ost [220511] firm, reliable. ostigàn Pwstyk’n! | M Iwstyg^n, N ustuwàn?] firm, strong, sure, reliable. ~ih: reliability. lēš [wf | = M, N Ads] consciousness, intelligence. mih: = 68. 268 [wf | = M] death.
PHD.txt:566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
PHD.txt:1294:commit abespurdan.
PHD.txt:1354:consign abespurdan.
PHD.txt:1578:desperate gyan-abespar.
PHD.txt:1594:devoted gyan-abespar.
PHD.txt:1782:entrust abespurdan, gumārdan.
PHD.txt:1891:fate bast, bréh, spihr.
PHD.txt:1954:firmament spihr.
PHD.txt:2245:heavenly ménóg, spihrig.
PHD.txt:3687:sky asmān, spihr.
PHD.txt:3770:sphere (heaven) spihr.
PHD.txt:4045:trample spurdan, ēspurdan, wispur- dan, xwastan.
PHD.txt:4773:spéd spēdag spēdbāg spenāg spóxtan spandan Spandarmad sabuk spul spurrigih spurrig spurdan spūz spēz- spinjānagīh spozgar spūzišn sabz spazg spazgīh spar spar- sprahm sprahmag
PHD.txt:4779:spāh ALY Q335 dēbahr, spihr, Nay LAKE spaxr spahbed VP OR 0335 spas ts” суз? spāsdār Nee es. spāsdārīh uA a soda) spāsešnās TO Put 0335 debàg VW ett spāsūmand ? v€ Pus” q335 spāš AV суз?
PHD.txt:4780:spihr Vo os»
PHD.txt:4781:spihrīg uo ev spenāg wvav spig 135035 spiz- —-Q5 Q335 spīzišn 1^0 2301 spiš ^U" Q335 spitāmān 16” 10 035 spēd-dār `o тез as»
PHD.txt:5152:[103] nasrušt pev NT ` wisistan nte \ wisp 0239 \ wispurdan wed 120354 wistāxīh ^C) ҮАУ тез wistāx AWAY 19351 wastār є, 19.35 | wastārīh PR t€351 wassadēn \ 095 \ wassad 19351 wastóhmag vs? ea» 1 wistan 1112.35 | wastar, wistar ` vw», wistar- aN Y€.35|
PHD_mackenzie.txt:778:abespirdan ['psp'ltn ) = abespurdan.
PHD_mackenzie.txt:780:abespurdan, abcspar- ['/Jspwltn', 'psp'l- I M 'byspwrd, 'bysp'r-, N
PHD_mackenzie.txt:2641: .......-abespar [-)psp)il N jan-sipar] reckless, desperate; devoted.
PHD_mackenzie.txt:3856:ospurdan, ospar- Cwspl-tn ] tread, trample.
PHD_mackenzie.txt:4594: spar-,v. spurdan.
PHD_mackenzie.txt:4613:spihr [spy(y)hl I (M <spyr), N sipihr] sphere, sky, firmament, fate.
PHD_mackenzie.txt:4628:spurdan, spar· [spwltn', spl- I N sip-] tread, trample.
PHD_mackenzie.txt:5421:wispurdan, ·wispar- [wspwltn ] tread, trample.
=== NYB ===
593:api-spartan ['psp'ltn'], often with bé: to hand over (6 to) 147. 3213; to consign to, to lay down in (6) 111°; to give up (one’s honour) 4?!; to give (one’s life, rad for) 1119; to commit (oneself to death)
595:api-spartan
596:113-6, (another to death and torment) 7721, — Olr *upa-spar- and apa-spar-, and then *upa- remodelled to api- (v. apa-): MPrth ’byspwrd, pres. ?bysp?r-, Ghilain 75; Arm. lw. apspar-em (= aps- spar- < api-spar-); Paz. awa-spārdan; NP only simplex swpurdan sipdr- ‘to entrust'.
1754:expressed (nominal sentence as in the Semitic languages): man Sähpuhr hom 154; tē ke he? 737; to rād ke Dugdav he 4721. en rētak ke hast? who is this boy? 1617; Artaxsér ... nē pat giyāk hast 6?" sq.; kë zan-& hac õi hucihrtar nest ‘qua pulchrior non est mulier', who is the most beautiful of all women 259-19; ēzšān amüh hem ke ... we are of those who 5723-24, šmāh ke xtēn het 6111; sagr hend 86%, — 3. in the 3d p., together with a subst. virtually in dat., or with a pron. in cas. obl., it expresses ‘to possess’ xdnak i-t hast the house that belongs to thee 5325-26; fradandan i-5 hast the chil- dren he has 142; with ràd as in NP: Papak rüd pus-é hast 3?. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions, e. g. han- dešitar vicītār hom 125; frēftār hah 3419; matür hom 46’; kartar hom 101?’; brihenäk hend 7777; ke (cas. obl.) vitīrišn nest which is incorruptible 66°; tö hän-ic äkäh he this thou knowest 399; hayyär hend they help 106%; -š hayyaréh hénd they help him 1001-12; pat kamēstārēh + spihr hénd they offer resistance to the. Sphere 8721; ké (cas. obl.) Mihr u Mah pat pust hah which M. and M. protect 317-8, ete. — 5. auxiliary vb. forming compound tenses: būt hom, būt hend I was, they were, eto., v. Grammar; notice: HWH-nd, regularly hend, must stand for the subju. händ 14? (fut.). 335 (cond.). — 6. Wrong use of the ideogr. HWH-: a) HWH-wm for the encl. pron. lst p. sg., added to the pret. pass. in order to emphasize the agent-
3088:pattän [pt’n'] continually, uninterrupted- ly, right on to (6) 209; [ka Gäyömart hac x"& früc but dit... spihr 6 gartisn, x'aréet u mah 6 ravisn ēstāt u ~ hend when G. woke up from his sleep he saw that the vault of heaven had begun to turn, and Sun and Moon to move, and they are still (in turning and moving) BdA p. 44 5-?; possibly written PWN ZK KnS VI, 4, but the text is not sure]. — < *pati-tāvana- from pati + tav-, v. the preceding w. Parallel with the series pattāt, pattūk (v. this w.), pattān is the series with the prev. *ati-: *attāk < *ati-tävaka-, Arm. lw. atak ‘capable’: attūk < *ati-tuvaka- id.: attān < "ati- tāvana- ‘solvent’ (attānīk DkM 139—140, opp. an-attān 'insolvent'). Cf Bthl., MirM III, 15, ZsR III, 53. — Cf ham-tak, tāhēkār, tāk, tāyītan, tuvān.
3481:spahr [sp?hl] v. spihr.
3491:spihr [spyhl] 8721, spahr [sp?hl] 695. 1206, the vault of heaven, the Celestial sphere. — Paz. spihr, spihar, spehir etc. (Mx, SGV); NP sipihr. I maintain the old etymology: OIr *spidra- (Skr sviüra-) ‘brightly shimmering’ and then ‘heaven’
3492:(cf n. pr. %m10pa-6d77g). Henning identifies it (List 81; JRAS 1942, 239sg.) with MPrthPrs ‘spyr (= esper) which accord- ing to him is borrowed from Gr ogatp«. However, in this case -h- in spihr would be an inorganic insertion, which is quite improbable. Of course, the sense of spihr may have been influenced by ogaip«, but its formal independence is proved by NP sipihr which belongs to the living language. ��� As to the alternation -ih- : -ah- cf s. v. mahmäneh.
3506:spurtan [spwltn'] spar-, pres. pass. 3d p. sg. sparihét [splyhyt'], to trample (to death) 4876. 4911.14.25, — Av. (1613) spar-; NP sipurdan sipar-.
4101:Dhabhar vētvar, without etymology, in the sense of ‘contented, contentment, forbearance, patient, consoling oneself (‘consoling’ already West), resigned to the will of God’ (~ dätan ‘to console’); Hormazdyar with the same etymology as Bailey, but giving the same senses as Dhabhar (‘one who endures grief, en- during, patient, consoling, persevering’). Both lay stress on the close parallelism with a%ansand (x"arsand), of which it sometimes seems to be a mere synonym. However, the original idea underlying it must be looked for from another angle. I read it, with Dhabhar, vēt-var and derive it from OTr *vaiti-bara- ‘the willow- bringer [Av. (1314) vaéti-, NP bed, ’willow’] originally an epithet of Airyaman, the god of healing, and going back to the myth told in Vd. 22: Ahuramazdah, badly wounded and struck with 99999 maladies by Ahriman on his first on- slaught on the heavenly creation, pro- mised 1000 horses, 1000 camels, 1000 heads of cattle, 1000 sheep and “the beautiful Benediction of the Righteous" (dahma äfriti) to the god who could heal him. All declined except Airyama tišyē *Airyaman the desired(?)": he brought (barat) hair from 9 horse stallions, hair from 9 camel stallions, hair from 9 bulls, hair from 9 rams, and brought 9 willow twigs (nava vačtayo barat) and drew 9 furrows — the Phl v. adds: “and made a nirang (g. v.)”, a magic spell intended ‘to heal the wounds and stop the maladies. Apparently the willow twigs played the chief part in this nirang (of whose parti- culars we know of course nothing), thus it was quite natural to form out of it the epithet *vea$-bara- of Airyaman in his quality of the healing and relieving god. Later, Airyaman having faded away, the usage took a wider range and developed secondary nuances, but the original meaning ‘healing’ is still fairly transpar- ent in many passages, e.g. DD 36? (quoted both by Dhabhar and Hormazd-
5343:spar-: spurtan
5529:"byspwrd, *bysp’r-: apispartan
5553:‘spyr: spihr
5857:‘spyr: spihr
6807:spih(a)r, spahir: spihr sp6z-: spoxtan
6954:$van-: !sak Sveta-: spét $vitra-: spihr tanu-: tanük tarna-ka-: tarr taruna-: tarr tavat: han-tài trpra-: sapük tulà: tarāzūk udara-: *ud(a)rài ud-vat-: yuvat upäka: tapak
7402:sipihr: spihr
```


## [2026-09-14T02:30:12.456Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2545,2600p' HUB.txt; echo \"=== 7310 ===\"; sed -n '7310,7330p' HUB.txt"
}
```


### [2026-09-14T02:30:12.516Z] TOOL RESULT

```
lioh, way, manner, method* zusammen, fur das man daqq freilich *Sfin
erwarten soUte.— 73 —
skr. gasana- Torschriff (ZDMG. 47, 702) ist auch nicht
sicher. — Zu dem hier angefuhrten setigso (Shuk.
p. 147 s. V. aunbada) vgl. np. sang i sal 'Schleifstein'
(Rosen, Np. Sprachf. p. 50). Das in der Anmerkung
erwahnte np. sa Tribut = phi. sak (Matikan i 5atrang,
phi. Text p. 1, 12) ist = arm. LW. sak 'Tribut' (Elise
35, 6). Zu np. sav vgl. afgh. LW. sav a taxe, a tribute*.
697. Im Phi. ist apspurtan zu lesen, vgl. arm. ap-spar-em
'iibergebe, iiberlasse, vertraue an . Als iranische Wurzel
ist spar anzusetzen. Der Infinitiv sipdrdan (vgl. kas.
espdrtdn u. s. w.) ist vom Praesens neu gebildet;
ursprunglich steht nur der Infinitiv supurdan neben
dem Praesens sipdram (und siparam Sal. Shuk.
Gram. § 41, c). Fiir phi. spurtltan ist spurtan zu setzen,
vgl. Gl. and. Ind. 156.
698. Unsicher der Bedeutung wegen.
700. Die Bedeutung von zd. spOrdddsta- ist unsicher.
702. Zu den kas. Dialectformen mit l- stimmt jud. tat.
siipul *Milz* (Miller p. 80).
703. Dazu paz. spur perfect*, spur[ = phi. spurtk complete*
Shk. 268, phi. spur perfect' Gl. and Ind. 161, an-aspurlk
'imperfect* West, PT. 4, 40, spurikih 'completeness'
4, 328, an-avispurtk unvollendet* BB. 17, 261, arm. spar
*Ende' (/ spar 'bis ans Ende', anspar *endlos'). Np.
sipari = phi. *spartk; phi. spur = ap. *spma-; arm*
spar = ap. sparna-?
704. Arm. aspnjakan *Wirt*, aspnjaJcanufiun *Gastfreund-
schaft*. Die arm. Form setzt ein *aspinj voraus, das
zu den syrischen und mandaischen Formen stimmt.
706. Dazu paz. spuxtan to sed aside*, spuxtdr *remover ,
spoid putting aside, Shk. 267—268, arm. spuzel auf-
schieben', spuiumn 'Aufschub' (aus spoii- =■ ipsLZ.spdz-),
Phi. y^spoxtxtan'^ ist eine XJnform.
707. Np. sipihr 'Himmel' ist nach NSldeke direkt =
skr. gvitrd" Veisslich, wei3s', dazu nach Geiger afgh.
sper^ grau*.— 74 —
709. Die urspriingliche Infinitivform scheint sitadan ge-
wesen zu sein, vgl. np. sitadan (neben sitadan) = paz.
stadan, ptc. stad Min. 61. 192. Hier kommt auch der
Praesensst. stan- haufiger vor als stan-. Wrzl. ston?
712. Das Wort sitdra ist arabisch, von satara 'texit*
(N5ldeke).
713. Das in der Note angefuhrte stuar'^) *dick' stelle ich
zu zd. stavah- *Dicke*, stui-^ stvi- als 1. Glied von
Comp. (fur *5^wra-. stehend, vgl. C aland, KZ.31,267)
= *dick', skr. sthAvira- 'breit, dick, massig , sthura-
'dick, breit', sthula- grob, dick', bal. istur grob, dick*,
osset. stir gross, stark\ afgh. star great, large, big ,
kurd. stUr 'dick geschwollen* (Socin, kurd. Samml. II,
p. 312). Vgl. np. suturg (Horn Nr. 715).
714. Unsicher wegen der Bedeutung.
716. Fiir die Volksetymologie {astarvan^ jiid. pers. astar-
vund = *Maulesel-ahnlich', also aus astar^vand) liesse
sich geltend machen, dass auch im Sanskrit das SuflF.
=== 7310 ===
*Welt, Land', ap. xsad^'^a- *Reich', zd. xsad^ra- 'Reich'; cihr,
cihra 'Ursprung, Angesicht', paz. 6ihar Shk. 239, phi. cihar
Gl. and Ind. 126, mit historischer Schreibung inschr. d(i)tri,
ap. did'a- 'Stamm, Abstammung in ariya-ci^'^a' Von ari-
schem Stamme', zd. cidra- 'Same, Ursprung, Abstammung',
•in vielen Komp. z. B. zd. Manmcidra- = np. MinOdihr; zd.
gaoci^ra- = pers. Gdzihr^ ap. *gaucid^''a' = fwaid-^g
(Tab. 4), arm. Manacirh (Fsiuatiis) =Manadihr (Mos. Chor.,
Steph. Asol. 66, 67) = Manacir (Vardan 43, 44 u.s.w.),
vgl. np. mandcihr (?) Fird. I, 95, 618; sipihr 'Himmer, phi.
spihr^ ap, ^m&paiaTtjg, JSmd^ptddrjjg (Ktesias, Xenoph.
Anab., Arrian) Noldeke, Pers. Stud. I, 36, skr. gvitrd-;
ArdasTr, arm. sassanid. Artasir, arsacid. Artas^, phi. Ar-
taxsir BB. 4, 35, alter Artaxsatr (historische Schreibung')
im 3. Jhd. p. Chr.), hebr. Artaxsastd, Artaxsastd (Esra
4, 7 u.s.w.), ap. Artaxsad^'d; Bahram = phi. Vahram,
alter Varahran = zd. vered^rayna- \ zahr 'Gift*, arm. iahr
u.s.w. (siehe oben p. 71 und § 89) = zd. ^jfa&ra-; zor
'Weihwasser (Parsenwort !) == paz. zor Min. Gl. 225, phi.
zohr Gl. and Ind. 150, arm. zoh 'Opfer, syr. N'imT *Opfer-
kuchen', zd. zao&ra- 'Opferspende, Opfertrank, Weihwasser.
```


## [2026-09-14T02:30:24.313Z] TOOL CALL #21: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-14T02:30:24.371Z] TOOL RESULT

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
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-14T02:30:24.414Z] TOOL CALL #22: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T02:30:24.420Z] TOOL RESULT

```


```


## [2026-09-14T02:30:31.283Z] TOOL CALL #23: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D9%87%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%CF%83%CF%86%CE%B1%E1%BF%96%CF%81%CE%B1\" \\\n \"https://www.etymonline.com/word/sphere\" \\\n \"https://www.etymonline.com/word/spinach\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%B1%D8%AF%D9%86\" \\\n \"https://www.etymonline.com/word/atmosphere\" \\\n \"https://en.wiktionary.org/wiki/spring\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 470, roots Spher / Spinakion\" ; done"
}
```


### [2026-09-14T02:30:47.763Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2bf4a207bd3850e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/90753cbb978a68a6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dcf514bc974b3884.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5225c9d9f67b961d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1b1f23344e0d772.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5ef0b5896b47da05.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/61462814d47f9e5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ef2a6bb315be0a7.txt
```


## [2026-09-14T02:30:49.788Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### سپهر\"; grep -n -A12 -i \"Etymology\" 2bf4a207bd3850e2.txt | head -60"
}
```


### [2026-09-14T02:30:49.842Z] TOOL RESULT

```
##### سپهر
65: Etymology 1 
66-
67- 1.2.1 
68- Noun 
69-
70- 1.2.2 
71- Proper noun 
72-
73- 1.2.2.1 
74- Derived terms 
75-
76- 1.2.3 
77- Descendants 
--
80: Etymology 2 
81-
82- 1.3.1 
83- Noun 
84-
85- Toggle the table of contents 
86-
87- سپهر 
88-
89- 8 languages 
90-
91- Беларуская 
92- فارسی 
--
191: Etymology 1
192- [ edit ] 
193-
194- Inherited from Middle Persian [script needed] ( spyhl ) , [script needed] ( spyyhl ) , 𐫙𐫘𐫛𐫏𐫡 ( ʿspyr /⁠spihr⁠/ , “ sphere, sky ” ) , from Old Persian *spiθrah .
195-
196- Noun
197- [ edit ] 
198-
199- سپهر • ( sipihr / sepehr ) ( Tajik spelling сипеҳр ) 
200-
201- ( literary ) sky , heaven 
202- Synonym: آسمان ( āsmān, āsimān ) 
203-
--
227: Etymology 2
228- [ edit ] 
229-
230: Phono-semantic matching of French sphère and/or English sphere , from Ancient Greek σφαῖρα ( sphaîra ) , which is not originally related to etymology 1 above. ( Can this ( + ) etymology be sourced ?) 
231-
232- Noun
233- [ edit ] 
234-
235- سپهر • ( sipihr / sepehr ) ( Tajik spelling сипеҳр ) 
236-
237- ( physics , in compounds ) sphere (as in stratosphere )
238-
239- Retrieved from " https://en.wiktionary.org/w/index.php?title=سپهر&oldid=90947368 "
240-
241- Categories : Persian terms with IPA pronunciation 
242- Rhymes:Persian/ihr
```


## [2026-09-14T02:30:50.700Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### sphaira\"; grep -n -A20 -i \"^ *Etymology\" 90753cbb978a68a6.txt | head -60"
}
```


### [2026-09-14T02:30:50.771Z] TOOL RESULT

```
##### sphaira
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Inflection 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3 
77- Descendants 
78-
79- 1.4 
80- References 
81-
82- 1.5 
--
162: Etymology
163- [ edit ] 
164-
165- Connections with σπαίρω ( spaírō , “ to gasp ” ) or Proto-Indo-European *sperH- ( “ to kick, rebound, move convulsively ” , the original sense would be "something that rebounds" ) have been suggested, but the aspiration of σπ- to σφ- is unexplained and the semantic development is dubious. [ 1 ] [ 2 ] Nikolayev instead suggests derivation from a Proto-Hellenic *skʷʰə́řřa , from a putative Proto-Indo-European *sgʷʰer- ( “ to be round ” ) ; compare Avestan 𐬰𐬔𐬆𐬭𐬆𐬯𐬥𐬀 ( zgər ə sna , “ round ” ) and Hittite [Term?]   pl ( /⁠šū̆rita⁠/ , “ skeins of wool ” ) (a borrowing from Luwian ). [ 3 ] 
166-
167- Pronunciation
168- [ edit ] 
169-
170- IPA ( key ) : /spʰâi̯.ra/ → /ˈsɸɛ.ra/ → /ˈsfe.ra/ 
171-
172- ( 5 th BCE Attic ) IPA ( key ) : /spʰâi̯.ra/ 
173-
174- ( 1 st CE Egyptian ) IPA ( key ) : /ˈspʰɛ.ra/ 
175-
176- ( 4 th CE Koine ) IPA ( key ) : /ˈsɸɛ.ra/ 
177-
178- ( 10 th CE Byzantine ) IPA ( key ) : /ˈsfe.ra/ 
179-
180- ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈsfe.ra/ 
181-
182- Noun
```


## [2026-09-14T02:31:02.378Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### sphere\"; sed -n '1,120p' dcf514bc974b3884.txt | grep -n -i \"sphere\" | head -30"
}
```


### [2026-09-14T02:31:02.465Z] TOOL RESULT

```
### sphere
1:URL: https://www.etymonline.com/word/sphere
4:TITLE: Sphere - Etymology, Origin & Meaning
6:Sphere - Etymology, Origin & Meaning 
21: Origin and history of sphere 
23: sphere (n.) 
25: a re-Latinized spelling, attested beginning mid-15c., of Middle English spere (c. 1300) "cosmos; space, conceived as a hollow globe about the world," from Anglo-French espiere , Old French espere (13c., Modern French sphère ), from Latin sphaera "globe, ball, celestial sphere" (Medieval Latin spera ), from Greek sphaira "globe, ball, playing ball, terrestrial globe," a word of unknown origin.
29: From late 14c. in reference to any of the supposed concentric, transparent, hollow, crystalline globes of the cosmos believed to revolve around the earth and contain the planets and the fixed stars; the supposed harmonious sound they made rubbing against one another was the music of the spheres (late 14c.), Milton's sphery chime .
31: Also from late 14c. in the general sense of "a globe; object of spherical form, a ball," and in the geometric sense of "solid figure with all points equidistant from the center." The meaning "range of something, place or scene" of activity, knowledge, etc. is recorded c. 1600 (as in sphere of influence , 1885, originally in reference to Anglo-German colonial rivalry in Africa).
34: Entries linking to sphere 
36: asthenosphere (n.) 
38: layer of the Earth's upper mantle, 1914, literally "sphere of weakness" (by comparison with the lithosphere), from Greek asthenes "weak" (see asthenia ) + sphere .
40: atmosphere (n.) 
42: 1630s, atmosphaera (modern form from 1670s), "gaseous envelop surrounding the earth," from Modern Latin atmosphaera , from Greek atmos "vapor, steam" (see atmo- ) + sphaira "sphere" (see sphere ). In old science, "vaporous air," which was considered a part of the earth and a contamination of the lower part of the air (n.1).
54: ecosphere 
55: hemisphere 
56: lithosphere 
57: magnetosphere 
58: photosphere 
59: planisphere 
63: stratosphere 
65: troposphere 
74: 1520s, "bounded by or having the form of the surface of a sphere," from sphere + -ical. The sense of "pertaining to or related to a sphere or spheres" is from c. 1600. Related: Spherically. Alternative spheric (1550s) is from Late Latin sphaericus, from Greek sphairikos. Spheral 
76: stratosphere 
78: 1908, from French stratosphère, literally "sphere of layers," coined by French meteorologist Léon-Philippe Teisserenc de Bort (1855-1913) from Latin stratus "a spreading out" (from past-participle stem of sternere "to spread out," from PIE root *stere- "to spread") + French -sphè
86: late 14c., "a large mass;" mid-15c., "spherical solid body, a sphere," from Old French globe (14c.) and directly from Latin...globus "round mass, sphere, ball" (also, of men, "a throng, crowd, body, mass"), which is related to gleba "clod, lump of...Sense of "the planet earth," also "map of the earth or sky drawn on the surface of an artificial sphere" are attested from..."A globe is often solid, a sphere often hollow. The secondary senses of globe are physical; those of sphere are moral."...
90: Roundness applies with equal freedom to a circle, a sphere, a cylinder, or a cone, and, by extension, to forms that by approach...Rotundity now applies usually to spheres and to forms suggesting a sphere or a hemisphere : as, the rotundity of the earth...
94: an axis;" also "the sky, the heavens" (a sense sometimes used in English from 16c.), from Greek polos "pivot, axis of a sphere...Originally principally in reference to the celestial sphere and the fixed points about which (by the revolution of the Earth...
98: Originally in battle or sport, extended 1620s to any sphere of human activity....
112: Share sphere 
116: https://www.etymonline.com/word/sphere Copy
```


## [2026-09-14T02:31:04.379Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### spinach\"; grep -n -i \"spinach\\|Persian\\|Arabic\\|Spanish\" 5225c9d9f67b961d.txt | head -30; echo; echo \"### atmosphere\"; grep -n -i \"atmosphaera\\|Greek\\|1630\" 61462814d47f9e5d.txt | head -20"
}
```


### [2026-09-14T02:31:04.445Z] TOOL RESULT

```
### spinach
1:URL: https://www.etymonline.com/word/spinach
4:TITLE: Spinach - Etymology, Origin & Meaning
6:Spinach - Etymology, Origin & Meaning 
21: Origin and history of spinach 
23: spinach (n.) 
25: garden vegetable with thick, succulent leaves, late 14c., spinache , spinage , etc. (late 13c. as a surname), from Anglo-French spinache , Old French espinache (14c., Modern French épinard , from a form with a different suffix), from Old Provençal espinarc , which perhaps is via Catalan espinac , from Andalusian Arabic isbinakh , from Arabic isbanakh , from Persian aspanakh "spinach."
29: For pronunciation, see cabbage . In 1930s colloquial American English, it had a sense of "nonsense, rubbish," based on a famous New Yorker cartoon of Dec. 8, 1928. Related: Spinachy ; spinaceous . Popeye, the spinach-eating superman, debuted in 1929.
32: Entries linking to spinach 
38: The decline of "ch" to "j" in the unaccented final syllable parallels the common pronunciation of spinach , sandwich , Greenwich , etc. The comparison of a head of cabbage to the head of a person (disparagingly of the latter) is at least as old as Old French cabus "(head of) cabbage; nitwit, blockhead," from Italian capocchia , diminutive of capo .
68: Old English plante "young tree or shrub, herb newly planted, a shoot or strip recently sprouted from seed," from Latin planta "sprout, shoot, cutting" (source of Spanish planta, French plante), which is perhaps from an unattested verb *plantare "to drive in with the feet, push in
90: Share spinach 
94: https://www.etymonline.com/word/spinach Copy 
97: <a href="https://www.etymonline.com/word/spinach">Etymology of spinach by etymonline</a> Copy 
100: Harper, D. (n.d.). Etymology of spinach. Online Etymology Dictionary. Retrieved September 13, 2026, from https://www.etymonline.com/word/spinach Copy 
103: Harper Douglas, "Etymology of spinach," Online Etymology Dictionary, accessed September 13, 2026, https://www.etymonline.com/word/spinach. Copy 
106: Harper, Douglas. "Etymology of spinach." Online Etymology Dictionary, https://www.etymonline.com/word/spinach. Accessed 13 September, 2026. Copy 
109: D. Harper. "Etymology of spinach." Online Etymology Dictionary. https://www.etymonline.com/word/spinach (accessed September 13, 2026). Copy 
116: Dictionary entries near spinach 
122: spinach 

### atmosphere
25: 1630s, atmosphaera (modern form from 1670s), "gaseous envelop surrounding the earth," from Modern Latin atmosphaera , from Greek atmos "vapor, steam" (see atmo- ) + sphaira "sphere" (see sphere ). In old science, "vaporous air," which was considered a part of the earth and a contamination of the lower part of the air (n.1).
36: also from 1630s 
42: c. 1300, "invisible gases that surround the earth," from Old French air "atmosphere, breeze, weather" (12c.), from Latin aer "air, lower atmosphere, sky," from Greek aēr (genitive aeros ) "mist, haze, clouds," later "atmosphere" (perhaps related to aenai "to blow, breathe"), which is of unknown origin. It is possibly from a PIE *awer- and thus related to aeirein "to raise" and arteria "windpipe, artery" (see aorta ) on notion of "lifting, suspended, that which rises," but this has phonetic difficulties.
50: a re-Latinized spelling, attested beginning mid-15c., of Middle English spere (c. 1300) "cosmos; space, conceived as a hollow globe about the world," from Anglo-French espiere , Old French espere (13c., Modern French sphère ), from Latin sphaera "globe, ball, celestial sphere" (Medieval Latin spera ), from Greek sphaira "globe, ball, playing ball, terrestrial globe," a word of unknown origin.
52: According to Beekes there are no certain cognates outside Greek, but the Greek word also has been borrowed into Syrian ( espero ), Ethiopian ( spir ), Armenian ( sp'er ), and (non-Indo-European) Georgian ( spero ).
```


## [2026-09-14T02:31:14.588Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '150,280p' f1b1f23344e0d772.txt"
}
```


### [2026-09-14T02:31:14.639Z] TOOL RESULT

```
 [ edit ] 

 Persian Wikipedia has an article on: اسفناج 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 سپاناج ( sepânâj ) , اسپاناج ( espânâj ) , سپناج ( sepanâj ) , اسپناج ( espanâj ) , اسپانج ( espânaj ) , اسپنانج ( espanânaj ) , سفاناج ( sefânâj ) , اسفاناج ( esfânâj ) , سپاناخ ( sepânâx ) , اسپاناخ ( espânâx ) , اسپناخ ( espanâx ) , سپناخ ( sepanâx ) , اسپناخ ( espanâx ) , اسپانخ ( espânax ) , سفاناخ ( sefânâx ) , اسفاناخ ( esfânâx ) , اسفناخ ( esfanâx ) , اسباناخ ( esbânâx ) , اسبناخ ( esbenâx ) , سبانخ ( sabânax ) , سبانج ( sebânaj ) , اسبانج ( esbânaj ) , اسبناج ( esbanâj ) , اسپاناغ ( espânâġ ) , اسپناغ ( espanâġ ) 

 Etymology
 [ edit ] 

 Kulturwort of Iranian origin. According to Asatrian, there were probably two forms in late Middle Iranian , *ispanāg (or *ispināg ) and (the dialectal) *ispanāx (or *ispināx ), yielding Arabized forms إِسْفَنَاج / إِسْفِنَاج ( ʔisfanāj / ʔisfināj ) and إِسْفَنَاخ / إِسْفِنَاخ ( ʔisfanāḵ / ʔisfināḵ ) , which were popularized in Persian and Arabic , respectively (alternative forms with پ ( p ) are directly from Middle Iranian). The Old Iranian form would be *spināka- , *spinaka- (compare Northern Kurdish sping ), from the root *spin- (Northwestern Iranian), *sin- (Southwestern Iranian), ultimately from the Proto-Iranian *spai- ( *spi- ), from Proto-Indo-European *spey- ( “ thorn-like ” ) ( *spi- ), which are also reflected in Latin spina , Persian سنجد ( senjed ) , Ossetian сындз ( synʒ ) , синдзӕ ( sinʒæ , “ thorn ” ) , Baluchi [script needed] ( šinž ) , Central Iranian šeng , Kermani šank ( “ thorn ” ) . Also akin to Semnani esbenāγa .

 According to Cabolov, related to Northern Kurdish siping ( “ meadow salsify , possibly also spinach ” ) and Persian سپند ( sepand , “ wild rue ” ) .

 اسفناج 
 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔis.fi.ˈnaːd͡ʒ/ 

 ( Dari, formal ) IPA ( key ) : [ʔɪs.fɪ.nɑ́ːd͡ʒ] 

 ( Dari, formal ) IPA ( key ) : [ʔɪs.fɪ.nɑ́ːd͡ʒ] 
 ( Kabuli ) IPA ( key ) : [ʔɪs.fɪ.nɑ́ːd͡ʒ] 

 ( Hazaragi ) IPA ( key ) : [ʔis.fi.nɔ́ːd͡ʒ̥] 

 ( Iran, formal ) IPA ( key ) : [ʔes.fe.nɒ́ːd͡ʒ̥] 

 ( Tajik, formal ) IPA ( key ) : [ʔis.fä.nɔ́d͡ʒ] 

 Rhymes: -aːd͡ʒ 

 Readings

 Classical reading ? 

 isfināj

 Dari reading ? 

 isfināj

 Iranian reading ? 

 esfenâj

 Tajik reading ? 

 isfanoj

 Noun
 [ edit ] 

 اسفناج • ( isfināj / esfenâj ) ( plural اسفناج‌ها ( isfināj-hā / esfenâj-hâ ) , Tajik spelling исфиноҷ ) 

 spinach 
 Synonym: شومین ( šumin, šomin ) 
 1258 , Rumi , Masnavi , First Book: من سپاناخ تو با هرچم پزی 
 یا ترش‌با یا که شیرین می‌سزی man sipānāx tu bā harčam pazī 
 yā turš-bā yā kē šīrīn mē-sazī (please add an English translation of this quotation) 

 Descendants
 [ edit ] 

 Most are directly from Middle Iranian 

 → Arabic: سَبَانِخ ( sabāniḵ ) , إِسْفَانَاخ ( ʔisfānāḵ ) , إِسْفَنَاخ ( ʔisfanāḵ ) , إِسْفَنَاج ( ʔisfanāj ) , إِسْفَانَاج ( ʔisfānāj ) , سَبَانَغ ( sabānaḡ ) , سَبَانَج ( sabānaj ) Andalusian Arabic: إِسْفِنَاج ( isfināj ) , إِسْبِنَاج ( isbināj ) , إِسْبِنَاخ ( isbināḵ ) → Aragonese: espinai 
 → Catalan: espinac 
 → Occitan: espinac , espinarc ( influenced by french ) 
 → Portuguese: espinafre 
 → Spanish: espinaca → Medieval Latin: spinacium , spinachium , spinarchia ( influenced by spina ( “ thorn ” ) ) → Byzantine Greek: σπινάκιον ( spinákion ) , σπανάκιν ( spanákin ) , σπινάκι ( spináki ) Greek: σπανάκι ( spanáki ) , σπανάκιον ( spanákion ) → Bulgarian: спанак ( spanak ) 
 → Romanian: spanac 
 → Serbo-Croatian: спанаћ / spanać 

 → Italian: spinacio , spinace ( uncommon ) → Middle High German: spināt ( final - t perhaps influenced by Salat ) German: Spinat → Kashubian: szpinat 
 → Russian: шпинат ( špinat ) → Bashkir: шпинат ( şpinat ) 

 → Serbo-Croatian: шпинат / špìnāt 
 → Ukrainian: шпина́т ( špynát ) 

 → Old French: espinoche , espinache , espinarde , espinaces French: épinard , ( obsolete ) epinart 
 → English: spinach , ( obsolete ) spinage 
 → Irish: spionáiste 

 → Sicilian: spinacia 

 → Georgian: ისპანახი ( isṗanaxi ) 

 → Middle Armenian: սպանախ ( spanax ) , ասպանախ ( aspanax ) , սպաննախ ( spannax ) Armenian: սպանախ ( spanax ) 

 → Ottoman Turkish: اسفناج ( isfinâj ) , اسپناخ ( ispenâh ) , اسفاناخ ( isfânâh ) 

 → Turkic:
 Karluk: 
 Uzbek: ismaloq 

 Kipchak: 
 Kipchak: yspanac 

 Oghuz: 
 Azerbaijani: ispanaq 

 Ottoman Turkish: اسپانق , اسپناق , اسپاناق ( ispanak, ıspanak ) , اسپاناك , اسپناك ( ispanâk ) 
 Turkish: ıspanak 

 Turkmen: ysmanak 

 References
 [ edit ] 

 Dehkhoda, Ali-Akbar ( 1931– ), “ اسفناج ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 

 Asatrian, Garnik ( 2011 ), A Comparative Vocabulary of Central Iranian Dialects ‎ [1] (in Persian), Tehran: Safir Ardehal Publications, pages 43–45 

 Steingass, Francis Joseph ( 1892 ), “ اسپناج ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 

 Lokotsch, Karl ( 1927 ), Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (in German), Heidelberg: Carl Winter’s Universitätsbuchhandlung, § 126 , page 11 

 Cabolov, R. L. ( 2010 ), “siping”, in Etimologičeskij slovarʹ kurdskovo jazyka [ Etymological Dictionary of the Kurdish Language ] (in Russian), volume II, Moscow: Russian Academy Press Vostochnaya Literatura, page 263 

 Redhouse, J. W. ( 1884 ), “spinach”, in A Lexicon, English and Turkish , 3rd edition, Constantinople: A. H. Boyajian, page 703 

 Redhouse, J. W. ; Wells, Charles ( 1880 ), “ spinach ”, in Redhouse's Turkish Dictionary, in Two Parts, English and Turkish, and Turkish and English , 2nd edition, London: Bernard Quartch, 15 Piccadilly, page 306 

 Abajev, V. I. ( 1979 ), Историко-этимологический словарь осетинского языка [ Historical-Etymological Dictionary of the Ossetian Language ] (in Russian), volume III, Moscow and Leningrad: Academy Press, pages 201–202
```


## [2026-09-14T02:31:23.862Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN spinach ===\"; grep -n \"^spinach\" KLN_1966.txt KLN_1971.txt | head; echo \"=== KLN spring ===\"; grep -n \"^spring,\" KLN_1966.txt KLN_1971.txt | head; echo \"=== SKT spinach ===\"; grep -n -i \"SPINACH\\|spinachia\\|espinard\" SKT.txt | head"
}
```


### [2026-09-14T02:31:23.960Z] TOOL RESULT

```
=== KLN spinach ===
KLN_1971.txt:228857:spinach. — See next word and -aceous. 
KLN_1971.txt:228858:spinach, n. — MF. espinache , espinage (whence 
KLN_1971.txt:228865:spinachium derive also It. spinace and — with 
KLN_1966.txt:36228:spinach
KLN_1966.txt:36268:spinachium  derive  also  It.  spinace  and — with change  of  suff — O  Pro  vent;,  espinarc  and  MHG. spinal  (G.  Spinal).
=== KLN spring ===
KLN_1971.txt:89350:spring, jump’, whence the freq. saltare , ‘to leap, 
KLN_1971.txt:124849:spring, jump’. See salient and cp. saltant. For the 
KLN_1971.txt:135742:spring, leap’, Lith. lekiit , lekti , ‘to fly’, lakstyti , 
KLN_1971.txt:166170:spring, v. 
KLN_1971.txt:192570:spring, phild’, and -cidium, ‘killing’, fr. caedere, 
KLN_1971.txt:214891:spring, leap, bound’, and ttooc, gen. TtoB6q, 
KLN_1971.txt:229940:spring, intr. and tr. v. — ME, springen , fr. OE. 
KLN_1971.txt:229959:spring, n., 1) a leap; 2) source of water; source, 
KLN_1971.txt:229979:spring, v. , and buck. 
KLN_1971.txt:235695:spring, jump’. See salient. For the change of 
=== SKT spinach ===
18094:spinster,  orig.  a  woman  who  spins. <E.)  M.  E.  spinnestere.  From  A.  S.  spiim- att,  to  spin;  with  A.S.  sufBx  -^stre  (E. 'Sfer).  p.  This  sufTix  is  a  compound  one (-«•/«),  coraj-oundcd  of  the  Aryan  suf5xcs *as  and  -tar,  as  in  Low  L.  poet-astir,  L. efe-as-ter.  It  ua^i  used  in  A.  S.  i^s  in  Du.) solely  with  reference  to  the  feminine  gender, but  this  restricted  usage  was  soon  s«t  aside ID  a  great  many  M.  E.  words.  Cf.  Du. spinster,  a  spinster,  tangstert  a  female silver ;  also  E.  seamstress  (i.  c.  seam-ster- ess),  songstress  (i,  c.  songster  as),  where  the F.  fern  "•ufTix  -/xs  is  su})eradded. Spinach,  Spinago;  sec  Spins. Spindle ;  liee  Spin.
```


## [2026-09-14T02:31:25.587Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT ===\"; grep -n -i \"spinat\\|isfinag\\|espinaca\\|aspanah\\|spanak\" LKT.txt | head -20; echo \"=== AFM ===\"; grep -n \"اسفناج\\|اسپناخ\" AFM.txt AFM_pages.txt | head -10; echo \"=== PLA? ===\"; ls | grep -i pla"
}
```


### [2026-09-14T02:31:25.678Z] TOOL RESULT

```
=== LKT ===
506:ar.  isfänäg,  isfinäg  'Spinat'  [Vielleicht kommen  diese  Formen  selbst  aus  dem Lateinischen,  etwa  spitia  'Dorn'  oder besser  *spinax  SBKAW  Wien  PhhKl CXXXII,  362];  hieraus  zunächst  die  ro- manischen Formen  afrz.  espinoche,  espi- nard;  frz.  epinard,  prov.  espinar,  kat. espinac,  sp.  espinaca,  pg.  espinafre,  it. spinace,  rum.  spanac.  Mit  steter  An- lehnung an  lat.  spina  auch  im  Germa- nischen dtsch.  Spinat,  ndl.  spinazie, engl,  spinage.  Russ.  spinal,  bulg.  spa- nak,  serb.  spanac,  äech.  Spinat,  poln. szpinak.  [Devic  DEt  110/111.  Eguilaz 391.    ML  706.
5677:spanak  126
5880:Sorfoei  1838 Sorgweizen  551 so</'<';  mhd.  1927 Souchong  (Tee)  1889 Spinat  126 Stambulina  1931 Ströhzicher  1004 S<)«iS  j.  1927 Sm^^xh  194.^^ Sumach  1946 Suradain  St.  1949
=== AFM ===
=== PLA? ===
```


## [2026-09-14T02:31:31.539Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '495,515p' LKT.txt"
}
```


### [2026-09-14T02:31:31.618Z] TOOL RESULT

```
Elativform  von  sarlf  'edel,  berühmt' [s.  hier  Nr.  1852],  also  'sehr  berühmt, sehr  edel',  ergab  mit  pers.  SufBx  i  äs- räfi  'eine  Goldmünze'  [genau  so  ge- bildet wie  das  synonyme  äkbäri  von ar.  akbar  'sehr  grofa'].  Hieraus  pg. xarafim,  xerafim  'eine  Münze  aus  Ost- indien, die  300  Reis  Wert  hatte'  [Con- stancio  Dicc  974  a]  und  sicherlich  auch frz.  aigrefin  [mit  volksetymologischer Umgestaltung]  'eine  Münze,  die  früher in  Frankreich  in  Umlauf  war'  und  mit einem  nicht  seltenen  Bedeutungswandel 'Schwindler,  listiger  Mensch'  [besser  als die  Ableitung  von  einem  so  nicht  vor- handenen al-hurüfi,  das  wieder  in  Zu-
sammenhang mit  harif  'Bursche'  ge- bracht wird].    [Devic  DEt  5.
122.  Pers.  ästär:
[Ob  ursprünglich  iranisch  wie  Horn NpEt  S.  7,  Nr.  26  will,  oder  tk.  ast 'unter',  also  'Unterfutter'  ZDMG  XXIII, 272  u.  Vämbery  TktElWb  S.  21,  Nr.  23 1, bleibe  dahingestellt]  'Futter  (eines  Klei- des)'. Hieraus  über  tk.  astar  'dass.' [Kelekian  Kämüs  18a]  rum.  astar  'Fut- ter, Seihtuch'.
123.  Ar.  'asür:
'Der  Zehnte'  [von  '«snr  '10'];  hieraus frz.  achour  'eine  Steuer,  welche  die  Ein- geborenen Algeriens  an  die  französische Verwaltung  zu  zahlen  hatten'.  [Devic DEt  4.    Lammens  Rem  4.
124.  Tk.  asyk:
'Knöchel,  Knöchelchen  (auch  zum  Spie- len)'; hieraus  mit  adventivem  r  rum. ar§ic  'Knöchelchen,  Knöchelspiel';  Ab- leitg.  arqicar.
125.  Tk.  asm.i:
[Vom  Stamme  as-  'hängen']  'Rebe'; hieraus  rum.  asmaciuc,  asmafuc,  asma- pichm,  'Kerbel  Anthriscus'.
126.  Pers.  äspänäh  :
ar.  isfänäg,  isfinäg  'Spinat'  [Vielleicht kommen  diese  Formen  selbst  aus  dem Lateinischen,  etwa  spitia  'Dorn'  oder besser  *spinax  SBKAW  Wien  PhhKl CXXXII,  362];  hieraus  zunächst  die  ro- manischen Formen  afrz.  espinoche,  espi- nard;  frz.  epinard,  prov.  espinar,  kat. espinac,  sp.  espinaca,  pg.  espinafre,  it. spinace,  rum.  spanac.  Mit  steter  An- lehnung an  lat.  spina  auch  im  Germa- nischen dtsch.  Spinat,  ndl.  spinazie, engl,  spinage.  Russ.  spinal,  bulg.  spa- nak,  serb.  spanac,  äech.  Spinat,  poln. szpinak.  [Devic  DEt  110/111.  Eguilaz 391.    ML  706.
127.  Hebr.  asirüt:
Moderner  Ausdruck  'großer  Reichtum' [vgl.  assyr.  asäru  'Heil  widerfahren  las- sen' Del  HWB  148  a,  hebr.  *es^r  im Ps  1,  1:  'Glück'];  hieraus  mit  vorgesetz- tem n  [wohl  aus  dem  dtsch.  Art.]  das jüdischdeulsche  nesires  in  dem  Aus- druck :  Da  steckt  e  Nesires  'Da  ist  noch Reichtum!'  [Tendlau66.  LenzEindrl7.
128.  Tk.  at:
[Vielleicht  vom  Stamme  al  'fremd,  wild' Vämbery  TktEtWb  S.  14,  Nr.  14]  'Pferd'. Hieraus  rum.  hat  'Pferd'  in  der  Volks- poesie; bulg.  serb.  at  'Pferd,  Hengst'. Mit  pers.  pähn  'groß,  weit,  breit'  [Horn NpEt  S.  76,  Nr.  344]  wird  tk.  pehn-at 'großes  Pferd',  woraus  rum.  bahntet 'edles  tatarisches  Roß'  in  den  Volks- liedern der  Moldau,  russ.  klruss.  poln. bachmat  'dass.',   Adj,  (dial.)  bachmatif
Ar.  'atnsa.]
12
'tölpelhaft,  uiigeschickl'.  |Sain  16.  Bern SlKt\VI):?3.  Gorjajew  13.  Karlowicz  4'i3.
li."J.  Ar.  'atai^a: 'Dürsten,  nach  elw.  gierige  sein'.  Hier- aus siz.  nttaciu  'riesiger  Appetit,  Gier, Brunsf;  attaciatii  'durstig,  ängstlich'. [GrSVociSic  ^J^!7.
13(».  Ar.  atflja: rir.  atäfl  'Dreifuß';  hieraus  mit  dem ar.  Ari.  sp.  annafe,  anafrc  'Kohlen- hecken, kleiner  tragharer  Ofen'.  In  der ar.  Aussprache  von  Granada,  wo  die Iniiila  fä  ^  ij  sehr  stark  war,  er- gab sich  atifl  und  hieraus  sp.  atifle 'irdener  Dreifuß'.    [DE  1S4  u.  ^215.
```


## [2026-09-14T02:31:33.188Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '36225,36275p' KLN_1966.txt; echo \"=== leaf of that line ===\"; python3 -c \"\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\nlines=d.split('\\n')\noff=sum(len(l)+1 for l in lines[:36227])\nprint('leaf', d[:off].count('\\f'))\n\""
}
```


### [2026-09-14T02:31:34.778Z] TOOL RESULT

```
Derivatives:  spherical  (q.v.),  spheric-ity,  n. spherical,  adj.,  1)  shaped  like  a  sphere;  2)  per¬ taining  to  a  sphere  or  spheres.  —  Formed  with adj.  suff.  -al  fr.  Late  L.  sphaericus,  fr.  Gk. aox'.pixoc,  fr.  c^atpa.  See  sphere  and  adj.  suff. -ic.
Derivatives :  spherical-ly,  adv.,  spherical-ness,  n. spherics,  n.,  spherical  geometry  and  trigonometry. —  See  spheric  and  -ics. sphero-,  combining  form.  —  See  sphaero-. spheroid,  n.,  a  body  resembling,  but  not  identical with,  a  sphere.  —  Late  L.  sphaeroeides,  fr.  Gk. c9atpoEiS7)s,  ‘spherical’,  which  is  compounded
spneromerer
spinach
of  arpatpa,  ‘ball,  sphere’,  and  -osiSrjg,  ‘like’,  fr. cTSoq,  ‘form,  shape’.  See  sphere  and  -oid. Derivatives:  spheroid-al,  adj.,  spheroid-al-ly, adv.,  spheroid-ic,  spheroid-ic-al,  adjs.,  spheroid¬ icity,  n.
spherometer,  n.,  an  instrument  for  measuring  the curvature  of  a  spherical  surface.  —  F.  sphero- metre.  See  sphero-  and  -meter, spherule,  n.,  a  minute  sphere.  —  Late  L.  sphae- rula,  dimin.  of  L.  sphaera ,  fr.  Gk.  cnpatpa.  See sphere  and  -ule.
Derivatives:  spherul-ar,  spherul-ate,  adjs. spherulite,  n.,  a  spherical  group  of  minute  crystals found  in  glassy  rocks  (petrogr.)  —  See  prcc. word  and  subst.  suff.  -ite.
Derivatives:  spherulit-ic,  adj.,  spherulit-ize,  tr.  v. sphincter,  n.,  a  muscular  ring  surrounding  an opening  of  the  body  ( anat .)  —  Late  L.,  fr.  Gk. ucpiYXTrip,  ‘that  which  binds  tight,  lace,  band; muscle  closing  an  aperture’,  fr.  a^yyeiv,  ‘to bind  tightly,  press  together’,  which  is  of  uncer¬ tain  origin ;  cp.  Sphinx.  In  its  anatomical  sense, aqjiyx-rqp  was  first  used  by  Galen.  See  Joseph Hyrtl,  Onomatologia  anatomica,  p.  484. Derivatives:  sphincter-al,  sphincter-ate,  sphinc- ter-ial,  sphincter-ic,  adjs.
Sphinx,  n. ,  1)  any  Egyptian  statue  or  figure  having the  body  of  a  lion  and  the  head  of  a  man,  ram or  hawk;  specif.,  cap.,  the  huge  statue  near  the pyramids  of  Gizeh  in  Egypt,  with  a  man's  head and  a  lion’s  body;  2)  in  Greek  mythology,  a winged  monster  with  a  woman’s  head  and  lion’s body;  specif.,  the  Sphinx  of  Thebes,  who  stran¬ gled  those  unable  to  solve  a  riddle  propounded by  her;  Oedipus  succeeded  in  solving  the  riddle and  the  Sphinx  killed  herself.  —  L.  sphinx,  fr. Gk.  mplyi;,  ‘sphinx;  rapacious  person’,  lit. meaning  ‘she  that  binds’,  or  ‘she  that  strangles’, fr.  mpLYYEtv,  ‘to  draw  tight,  bind  tightly’.  See sphincter  and  cp.  criosphinx. sphragide,  n.,  Lemnian  earth.  —  L.  sphragis,  gen. -idis,  fr.  Gk.  <19 pay!?,  gen.  -ISo?,  ‘a  seal’;  so called  because  sold  in  sealed  packets.  See  next word  and  -ide.
sphragistic,  adj.,  pertaining  to  a  seal.  —  Gk. (J9pay«jT txo;,  fr.  CT9payiOTo;,  ‘sealed’,  verbal adj.  of  <T9payi£eiv,  ‘to  close  with  a  seal,  to  seal’, fr.  a9payt?,  ‘seal’,  which  is  of  uncertain  origin. For  the  ending  see  suff.  -istic. sphragistics,  n.,  the  science  of  seals.  —  See  prec. word  and  -ics.
sphygmic,  adj.,  pertaining  to  the  pulse.  —  Gk. <j9uyp.1y.61:,  fr.  O9uy,uo;.  See  sphygmus  and  adj. suff.  -ic.
sphygmo-,  combining  form  meaning  pulse.  —  Gk. 09'jypo-,  fr.  a9'jy|ioc.  See  sphygmus. sphygmogram,  n.,  record  of  the  pulse  made  by  a sphygmograph.  —  Compounded  of  sphygmo- and  Gk.  ypappa,  ‘that  which  is  written’.  See -gram.
sphygmograph,  n.,  an  instrument  for  recording the  pulse.  —  Compounded  of  sphygmo-  and  Gk.
1488  -  1489
-ypxoo;,  fr.  ypo^eiv,  ‘to  write’.  See  -graph. Derivatives:  sphygmograph-ic,  adj.,  sphygmo- graph-y,  n.
sphygmoid,  adj.,  pulselike.  —  Compounded  of sphygmo-  and  Gk.  -oei8r|<;,  ‘like’,  fr.  elSog, ‘form,  shape’.  See  -oid.
sphygmology,  n.,  the  study  of  the  pulse.  —  Com¬ pounded  of  sphygmo-  and  Gk.  -Xoyta,  fr. -X6yo ?,  ‘one  who  speaks  (in  a  certain  manner); one  who  deals  (with  a  certain  topic’).  See  -logy, sphygmomanometer,  n.,  an  instrument  for  meas¬ uring  blood  pressure  in  the  arteries.  —  Com¬ pounded  of  sphygmo-  and  manometer, sphygmometer,  n.,  an  instrument  for  measuring the  strength  of  the  pulse  beat.  —  Compounded of  sphygmo-  and  Gk.  p6tpov,  ‘measure’.  See meter,  ‘poetical  rhythm’, sphygmophone,  n.,  an  instrument  for  rendering the  pulse  beat  audible.  —  Compounded  of sphygmo-  and  Gk.  9<uvy,  ‘sound,  voice’.  See phone,  ‘speech  sound’.
sphygmoscope,  n.,  an  instrument  for  examining the  pulse  beat.  —  Compounded  of  sphygmo- and  Gk.  -axomov,  fr.  <jxo7teIv,  ‘to  look  at, examine’.  See  -scope.
sphygmus,  n.,  the  pulse  (rued.)  —  Medical  L.,  fr. Gk.  o'puypo;,  ‘pulsation’,  fr.  <j9u£eiv,  (for *<j9uy-iEw),  ‘to  beat,  pulsate’,  whence  also £-<j9uxto<;,  ‘pulseless’;  possibly  derived  fr. *sphuk-,  a  gradational  var.  of  *sphek-,  ‘to  move convulsively’,  whence  aodxEXoc,  ‘convulsive movement,  gangrene’;  see  sphacelus  and  cp. sphygmo-,  asphyxia.  See  Hofmann,  EWG.,  p. 347  s.v.  cnpu^co.
Sphyraena,  n.,  a  genus  of  pikelike  fishes  (ichthyol.) —  ModL.,  fr.  L.  sphyraena,  ‘a  kind  of  seafish’, fr.  Gk.  <J9upaiva,  ‘hammer  fish’,  fr.  mpijpa, ‘hammer’,  which  is  rel.  to  <J9upov,  ‘ankle’, ajraipeiv,  ‘to  move  convulsively’,  from  I.-E. base  *(s)p(h)er-,  ‘to  move  convulsively’.  See spurn  and  cp.  words  there  referred  to. Sphyraenidae,  n.  pi.,  a  family  of  fishes  (ichthyol.) — ModL., formed  from  prec.  word  with  suff.-idae. spica,  n.,  a  spike  (hot.)  —  L.  spica,  ‘ear  of  com’.
See  spike  and  cp.  spicate. spicate,  spicated,  adj.,  1)  forming  a  spike;  2)  ar¬ ranged  in  spikes.  —  L.  spicatus,  pp.  of  spicare, ‘to  furnish  with  ears  or  spikes’,  fr.  spica.  See prec.  word  and  adj.  suff.  -ate,  resp.  also  -ed. spiccato,  adj.,  detached  (musical  direction)  —  It., pp.  of  spiccare,  ‘to  detach,  cut  off’,  formed  with change  of  pref.  fr.  impiccare,  ‘to  hang’,  which  is of  uncertain  etymology.
spice,  n.  —  ME.,  fr.  OF.  espice  (F.  epice),  fr.  Late L.  species,  ‘spice’,  fr.  L.  species,  ‘kind,  sort’.  See species.
Derivatives:  spice,  tr.  v.,  spic-ed,  adj.,  spic-er,  n., spic-y,  adj.,  spic-i-ly,  adv.,  spic-i-ness,  n. spicery,  n.  —  ME.  spicerie,  fr.  OF.  espicerie  (F. epicerie),  fr.  espice.  See  spice  and  -ery. spick,  n.,  fat  meat  (obsol.)  — -  ME.  spyk,  fr.  OE. spic.  See  speck,  ‘fat  meat’.
spick-and-span,  adj.  —  Short  for  spick-and-span- new,  lit.  ‘nail-and-chip-new’,  fr.  spick,  a  var.  of spike,  ‘nail’,  and  span-new. spicular,  adj.,  spiculate.  —  Formed  with  suff.  -ar fr.  L.  spiculum.  See  spicule, spiculate,  adj.,  1)  having  the  shape  of  spicules;  2) covered  with  spicules.  —  Formed  with  adj.  suff. -ate  fr.  L.  spiculum.  See  spicule, spicule,  n.,  any  small  pointed  object.  —  F.,  fr.  L. spiculum.  See  next  word.
spiculum,  n.,  any  small,  sharply  pointed  organ ( zool .)  —  L.  spiculum,  ‘a  small,  sharp  point,  dart, arrow’,  dimin.  of  spicum,  a  collateral  form  of spica.  See  spica  and  -ule. spider,  n.  —  ME,  spyder,  fr.  earlier  spithre,  fr.  OE. spidra,  fr.  Teut.  *spen-prd-  (whence  also  Dan. spinder),  lit.  ‘spinner’,  formed  fr.  OE.  spinnan with  agential  suff.  -er.  Cp.  MLG.,  MDu.,  MHG., G.  spinne,  Du.  spin,  ‘spider’,  and  see  spin. Derivatives:  spider-ly,  adj.,  spider-y,  adj. spiderling,  n.,  a  young  spider.  —  Formed  fr. spider  with  dimin.  suff.  -ling, spiegeleisen,  n.,  a  variety  of  cast  iron.  —  G.,  lit. ‘mirror  iron’,  fr.  Spiegel,  ‘mirror’,  and  Eisen, ‘iron’.  The  first  element  derives  fr.  OHG.  spia- gal,  fr.  ML.  speglum,  fr.  L.  speculum  ',  see  specu¬ lum.  For  the  second  element  see  iron, spiel,  n.,  speech;  intr.  v.,  to  talk.  —  G.  Spiel, ‘play,  performance’,  spielen,  ‘to  play’,  fr.  OHG. spil,  resp.  spilon,  rel.  to  OFris.  spil,  spel,  MDu., Du.  spel,  ‘play’,  OE.  spilian,  OS.  spilon,  ON. spila,  OFris.  spilia,  MDu.,  Du.  spelen,  ‘to  play’. Cp.  the  second  element  in  bonspiel,  glockenspiel, kriegspiel,  Singspiel.  Cp.  also  spell,  ‘to  take  the place  of  (another)  at  work’, spifflicate,  spiflicate,  tr.  v.,  to  confound  (slang).
—  Of  uncertain  origin.
spiffy,  adj.,  smartly  dressed  (slang).  —  Prob.  of imitative  origin.
Derivatives:  spiff-i-Iy,  adv.,  spiff-i-ness,  n. Spigelia,  n.,  a  genus  of  plants,  the  pinkroot  (bot.)
—  ModL.,  named  after  the  Flemish  botanist Adrian  van  den  Spieghel,  Lat.  Spigelius  (1558- 1625).
spigot,  n.,  a  small  plug  or  peg.  —  ME.,  prob.  fr. OProveng.  *espigot,  dimin.  of  espiga,  ‘ear  of corn’,  fr.  L.  spica,  of  s.m.  See  spica,  spike, spike,  n.  —  ME.,  rel.  to  ON.  spikr,  ‘spike,  nail’, Swed.,  Norw.  spik,  ‘nail’,  MDu.  spicher,  Du. spijker,  ‘nail’,  OE.  spaca,  OHG.  speihha,  ‘spoke’, fr.  I.-E.  base  *(s)pei-,  *(s)pi-,  ‘something  point¬ ed’,  whence  also  L.  spica,  ‘ear  of  corn’,  spina, ‘thorn,  prickle,  backbone’,  pinna,  ‘pin;  battle¬ ment  along  the  top  of  a  wall’,  Toch.  A  spin-ae (dat.),  ‘peg’,  Gk.  ojuXag,  aiziXoc,,  ‘rock,  cliff", Lett,  spile,  ‘a  wooden  fork’,  Lith.  speigliai  (pi.), ‘thorns’,  spitna,  ‘tongue  of  a  buckle’,  OE.  spitu, ‘a  spit’.  Cp.  pinna,  spica,  spiculum,  spigot,  spine. Cp.  also  spile,  spire,  ‘a  tapering  roof’,  spit,  ‘a pointed  bar  of  iron’,  spitz,  spoke,  and  the  first element  in  spick-and-span.
Derivatives:  spike,  tr.  v.,  spik-ed,  adj.,  spik-er.
n.,  spik-y,  adj.,  spik-i-ly,  adv.,  spik-i-ness,  n. spikelet,  n.  —  Formed  fr.  spike  with  dimin.  suff. -let.
spikenard,  n.  —  ME.,  fr.  ML.  spica  nardi,  ‘spike of  nard’.  See  spike  and  nard.
Spilanthes,  n.,  a  genus  of  plants  of  the  thistle  fam¬ ily  (bot.)  —  ModL.,  compounded  of  Gk.  am- Xoq,  ‘stain’,  which  is  of  uncertain  origin,  and  of atvftog,  ‘flower’.  See  anther, spile,  n.,  a  small  plug;  a  vent  peg.  —  MLG., ‘splinter’,  rel.  to  Du.  spijl,  ‘bar,  skewer’,  MHG. spille,  ‘peg’,  ON.  spila,  G.  Speiler,  ‘skewer’,  fr. I.-E.  base  *(s)pe(i)-,  *(s)pi-,  ‘something  point¬ ed’.  See  spike.
Derivatives:  spile,  tr.  v.,  spil-ing,  n. spill,  tr.  v.,  to  cause  to  run  out;  intr.  v.,  to  flow. —  ME.  spillen,  fr.  OE.  spilian,  ‘to  destroy,  kill’, rel.  to  OHG.  spildan,  ‘to  spill’,  OS.  spildian,  ON. spilia,  ‘to  destroy’,  and  to  MDu.  spillen,  ‘to waste’,  MDu.  spalden,  OHG.  spaltan,  ‘to  split’. Sec  spall,  ‘chip’.
Derivatives:  spill-er,  n.,  spilth  (q.v.) spill,  n.,  splinter.  —  Prob.  a  blend  of  spile  and MDu.  spille,  ‘stalk,  spindle’.  See  spindle  and  cp. spillikin.
spiller,  n.,  a  fishing  line.  —  Ir.  spilear. spillikin,  also  spellican,  n.,  a  strip  of  wood  or  bone used  in  the  game  of  jackstraws;  in  the  pi.,  the game  of  jackstraws.  —  ME.  spelleken,  fr.  MDu. spilleken,  dimin.  of  spille,  ‘peg,  pin’,  which  is prob.  rel.  to  OE.  speld,  ‘splinter  of  wood’.  See spill,  ‘splinter’,  and  -kin. spilth,  n.,  1)  the  act  of  spilling;  2)  something spilled.  —  Formed  fr.  spill,  v.,  with  subst.  suff. -th.
spin,  tr.  and  intr.  v.  —  ME.  spinnen,  fr.  OE. spinnan,  rel.  to  ON.,  Swed.,  OFris.  spinna,  Dan. spinde,  Du.  spinnen,  OHG.  spinnan,  MHG.,  G. spinnen,  Goth,  spinnan,  and  cogn.  with  OSlav. pinq,  ‘I  span’,  Arm.  henum,  ‘I  weave’,  Gk. jrarog  (for  *pntos),  ‘garment’,  lit.  ‘that  which  is spun’,  cTrivSEipa  (Hesychius),  ‘plow’,  Lith.  pirn), ‘I  plait,  braid’,  spandau,  ‘I  span’,  OSlav.  pqto, ‘fetter’,  MW.  cy-ffiniden,  ‘spider’.  All  these words  are  derivatives  of  I.-E.  *spen-,  ‘to  draw, stretch,  span,  spin’,  an  -^-enlargement  of  I.-E. base  *spe(i)-,  *sp6-,  ‘to  draw,  stretch,  span, spread,  extend’;  see  Kluge-Mitzka,  EWDS.,  p. 728  s.v.  spinnen.  See  space  and  words  there  re¬ ferred  to  and  cp.  esp.  span,  v.  Cp.  also  spider, spindle,  spinster.
Derivatives:  spin,  n.,  spinn-er,  n.,  spinn-ery ,  n. spin-,  form  of  spino-  before  a  vowel, spinaceous,  adj.,  pertaining  to,  or  resembling, spinach.  —  See  next  word  and  -aceous. spinach,  n.  —  MF.  espinache,  espinage  (whence — with  change  of  suff. — MF.  espinarde,  espi- nard,  F.  epinard),  fr.  ML.  spinachia,  spinachium, which — prob.  through  the  medium  of  Sp.  espi- naca  and  Andalusian  Arab,  isbinakh— derives fr.  Arab,  isbinakh,  earlier  isfanakh,  isfanakh,  fr. Pers.  aspandkh,  ‘spinach’.  Fr.  ML.  spinachia ,
spinal
spirometer
1490  '
1491
spinachium  derive  also  It.  spinace  and — with change  of  suff — O  Pro  vent;,  espinarc  and  MHG. spinal  (G.  Spinal).
spinal,  adj.  —  Late  L.  spinalis,  ‘spinal’,  fr.  L.  spi¬ na.  See  spine  and  adj.  suff.  -al. spindle,  n.  —  ME.  spindel,  fr.  OE.  spinel,  prop, ‘an  instrument  for  spinning’,  fr.  spinnan,  ‘to spin’;  rel.  to  OS.  spinnila,  OFris.  spindel,  OS., OHG.  spinnila,  MHG.  spinnel,  G.  Spindel.  See spin  and  instrumental  suff.  -le.  For  the  -d-, which  is  epenthetic,  cp.  kindred.
Derivatives :  spindle,  intr.  v.,  spindt-ed,  adj., spindl-er,  n.,  spindl-ing,  adj.  and  n.,  spindl-y, adj.,  spindl-i-ness,  n. spindrift,  n.  —  A  var.  of  spoondrift. spine,  n.  —  ME.,  ‘thorn,  backbone’,  fr.  OF.  espine (F.  epine),  fr.  L.  spina,  ‘thorn,  spine,  prickle, backbone’,  which  is  cogn.  with  Toch.  A  spin-ae (dat.),  ‘peg’ ;  fr.  I.-E.  base  *(s)pi-,  *(s)pei-,  ‘some¬ thing  pointed’,  whence  also  L.  spica,  ‘ear  of corn’,  ON.  spikr,  ‘spike,  nail’.  See  spike  and words  there  referred  to  and  cp.  spinel,  ‘a  miner¬ al’,  spinney.  Cp.  also  the  second  element  in  por¬ cupine.  Cp.  also  fin.
Derivatives:  spin-ed,  adj.,  spine-less,  adj.,  spine- less-ly,  adv.,  spine-less-ness,  n.,  spin-y,  adj.,  spin- i-ness,  n.
spinel,  n.,  a  crystalline  mineral.  —  F.  spinelle,  fr. It.  spinella,  dimin.  of  spina,  fr.  L.  spina,  ‘thorn, spine’.  See  spine.
spinel,  n.,  yam  used  for  making  tape.  — •  G.  Spi¬ nal.
spinet,  n.,  a  primitive  harpsichord.  —  Named after  its  inventor  Giovanni  Spinetti  of  Venice (cca  1500).
spini-,  combining  form  meaning:  1)  ‘thorn’;  2) ‘backbone’.  —  Fr.  L.  spina.  See  spine, spiniferous,  adj.,  producing  spines.  — •  Com¬ pounded  of  spini-  and  -ferous.
=== leaf of that line ===
leaf 789
```


## [2026-09-14T02:31:51.452Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==528' SKT.txt | grep -n -i -A6 \"SPINAGE\\|Spinach\" | head -40; echo \"=== header ===\"; awk 'BEGIN{RS=\"\\f\"} NR==528' SKT.txt | head -5"
}
```


## [2026-09-14T02:31:52.458Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^sphere,\" KLN_1966.txt; grep -n -B2 -A12 \"^spring,  intr\" KLN_1971.txt | head -40"
}
```


### [2026-09-14T02:31:52.826Z] TOOL RESULT

```
=== header ===
errier,  a  roll of  tenants'  names,  &c.  —  Low  L,  terranus, as  in  terrarius  liber,  a  book  whei  tin  landed proi»criy  is  described.- L.  terra,  land.
territory,  domain.  (F.-L.)  F.  ter* rileire,  a  territory,  —  L,  tirritffrium,  a domain,  land  round  a  town.  ■•  L.  terra, land  ;  formed  as  if  from  a  sb.  with  crude form  territori;  i.  e.  possessor  of  land.
tiiroen,  the  same  as  terreen  (.above). And  sec  turmeric.
Terreen,  Terrene,  Terreatrial ;  see Terraoe.
Terrible ;  see  TDrrop. Terrier  (1)  and  \,i)\  see  Torraoe. Terrific ;  sec  Terror. Territory;  sec  Ternioe. Terror,  dread.  (F.-L.)    Formerly  also terrour.^V.  terretir.^L.  terrorem,  ace  of terror,  dread.  — L. //riv*^,  10  scare,  make afraid,  orig.  to  tremble      Cf.  Skt.  tras,  to tremble,  be  afraid :  Lith.  trisuti,  to  trem- ble,  Kuss.  trituli,  to  shiver.
```


### [2026-09-14T02:31:52.899Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:31:57.963Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('SKT.txt',encoding='utf-8',errors='replace').read()\ni=d.find('Spinach,  Spinago')\nif i<0: i=d.find('Spinach')\nprint('leaf',d[:i].count('\\f'))\nprint(repr(d[i-200:i+900]))\n\""
}
```


### [2026-09-14T02:31:59.043Z] TOOL RESULT

```
leaf 484
' Du. spinster,  a  spinster,  tangstert  a  female silver ;  also  E.  seamstress  (i.  c.  seam-ster- ess),  songstress  (i,  c.  songster  as),  where  the F.  fern  "•ufTix  -/xs  is  su})eradded. Spinach,  Spinago;  sec  Spins. Spindle ;  liee  Spin.\nBplne.  a  prickle.  iF.-U)  O.F.w/ thorn,  -•  L.  spina,  a  thorn,  prickle  .  ih back-bone.  Allied  to  Spike.  ^tKi^-r^ in  ihescnseof \'back-|)one*l}it  !\nspinsch,  spinage,  a  vc.\n—  L.)  Spinage  is  a  wcakci.^^  ,^i spinark.^XXaX.  spinare  (pronoonoedj aaehai),  \'  the  hcarbe  spinage,*  V! Formed  (as  if  from  Ltivf  L,  spinar. from  spitiii,  a  thorn,  bccnasc  the  fr sometimes  very  prickly  ;  so  atsi>  Spa pimica.  %  Or  <  F.  —  Span.  —  Arab  —  I O.  K.  M/;>w^r  — Span,  espinata.  ^  Kst /a«((f\'(De\\ic).\nspinet,  a  kind  of  musical  ioMfbi (K.  — llal.-L.)  So  called  becaose  « by  a  spine  or  pointed  guill    O.  F.  esfi\\\n—  Itaf.  spinetta,  a  spmet.  also  %  pril dimin.  oispina,  a  thorn. —  L.  spima.\nspinny.  .n  thicket.  (F.  — U)    Of\npinoyt,  \'a  thicket,  grove,   a  Lhon)>  (i\n'
```


## [2026-09-14T02:32:09.231Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('SKT_dli_revised.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=d.lower().find('spinage, spinach')\nif i<0:\n    for m in re.finditer('SPINACH|Spinach|spinach',d):\n        print(m.start(), repr(d[m.start()-100:m.start()+400])); break\nelse:\n    print('leaf',d[:i].count('\\f')); print(repr(d[i-100:i+600]))\n\" 2>/dev/null | head -20"
}
```


### [2026-09-14T02:32:10.456Z] TOOL RESULT

```
2253779 'wed. spinna, Dan. spindCy \nG. spinnen, Goth, spinnan. Allied to \nLith./7«-^/, to weave. See Span. \n\nSpinach, Spinage, a vegetable. \n(F. — Span. — Arab. — I’ers.^ Spinage is a \n‘ voiced ’ form of spinach. O. F. espinachc^ \nespinage, espinace. — Span, espinaca. — \nArab, aspanakh^ isjanaj\\ of Pers. origin \n(Dcvic.). % T he Ital. spinace and Span. \nespinaca are re erred, by popular etymo- \nlogy, to L. spina, a thorn ; some say the \nfiuit IS piickly, some say the leaves are so. \nSee Spine. \n\nSpindle.'
```


## [2026-09-14T02:32:16.537Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('SKT_dli_revised.txt',encoding='utf-8',errors='replace').read()\ni=2253779\nprint('leaf',d[:i].count('\\f'))\nimport re\n# find nearby page-number-like lines\nseg=d[i-6000:i+2000]\nprint([m.group(0) for m in re.finditer(r'\\n *[0-9]{3} *\\n',seg)])\n\""
}
```


### [2026-09-14T02:32:17.637Z] TOOL RESULT

```
leaf 0
['\n506 \n']
```


## [2026-09-14T02:32:21.845Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'spring,\\s*intr', d):\n    i=m.start(); print('leaf',d[:i].count('\\f')); print(repr(d[i-100:i+1400])); break\n\""
}
```


### [2026-09-14T02:32:23.101Z] TOOL RESULT

```
leaf 794
'  with  suff.  -ly  fr. spright,  erroneous  spelling  of  sprite.\nDerivative:  sprightli-ness,  n. spring,  intr.  and  tr.  v.  —  ME.  springen,  fr.  OE.\nspringan,  rel.  to  ON.,  OFris.,  Swed.  springa, Dan.  springe,  MDu.  springhen,  Du.  springen, OS.,  OHG.  springan,  MHG.,  G.  springen,  fr. I.-E.  base  *sprengh-,  a  nasalized  variant  of  base *spergh-,  ‘to  move  quickly’,  whence  OI.  sprha- yati,  ‘desires  eagerly’,  Gk.  onep xeafim,  ‘to  hur¬ ry’.  Base  *spergh-  itself  seems  to  be  an  enlarged form  of  the  primitive  base  *sper-,  *spher-,  ‘to move  convulsively;  to  scatter’,  whence  OI. sphurdti,  ‘kicks  with  the  foot’,  Gk.  07raipeiv,  ‘to move  convulsively’.  See  spurn  and  cp.  springe. Cp.  also  the  first  element  in  springbok  and  the second  element  in  klipspringer.\nDerivatives:  spring,  n.  (q.v.),  spring-er,  n., spring-ing,  adj.  and  n.,  spring-ing-ly,  adv., spring-y,  adj.,  spring-i-ly,  adv.,  spring-i-ness,  n., spring-less,  adj.,  spring-like,  adv.\nspring,  n.,  1)  a  leap;  2)  source  of  water;  source, origin;  3)  the  season  in  which  plants  spring  up and  grow.  —  ME.,  fr.  OE.  spring,  ‘springing; source  of  water’,  fr.  springan.  Cp.  MHG.  sprinc, ‘leap,  jump,  source  of  water,  fountain’,  OHG. sprung,  MHG.  sprunc,  ‘source  of  water’,  G. Sprung,  Du.  sprong,  ‘leap,  jump’,  and  see  spring, v.\nspringa],  springald,  n.,  a  young  man  (archaic).  — Formed  fr.  the '
```


## [2026-09-14T02:32:31.190Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 793 794 795; do echo \"--- leaf $n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | grep -oE \"1[45][0-9]{2}\" | head -5; done"
}
```


### [2026-09-14T02:32:32.289Z] TOOL RESULT

```
--- leaf 793 ---
1588
--- leaf 794 ---
1499
--- leaf 795 ---
```


## [2026-09-14T02:32:38.350Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 541 542 543 544 545; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -30; done 2>/dev/null | head -160"
}
```


### [2026-09-14T02:32:39.432Z] TOOL RESULT

```
=== leaf 541 ===
  ‫سابه خوش‬                                                                         ‫‪ ۷۱0‬اس‬

‫سابه بر ست د کنابه ازشخصی باشد‬                     ‫ساید = بر وزن اید » بمعنیريم آهن‬
 ‫که ببوسته فق وفجور کوارهای‌ناشاسته کند‪.‬‬             ‫است‪,‬وآن چ رکی باشدکه از آهن بیرون‌آید‪.‬‬
‫سا به زر سی ک=نابه از فق وفجور‬                     ‫سایس پنحم رواق ‪ -‬کنابه از‬
               ‫کوارهای نا شاسته کردن باشد ‪.‬‬        ‫کو کب مریخ است چه او در فلك پنجم‌میباشد؛‬
‫=شم بای ابجد وفتح رای‬
                    ‫سا به بر گ ب‬                   ‫ند که اسب رانگاه‬
                                                                  ‫ویرا‬
                                                                     ‫وسایی در عربی شگخصی‬
‫قرشت وسکون کاف »کیاهی است که چون شتر‬                              ‫دارد وتسمار ومحافظت آ نکند‪.‬‬

‫قدری اآزن بخورد بخواب رود ؛ و با بای فارسی‬           ‫مباشمع»تی‬      ‫زرن‬
                                                                      ‫وب‬‫سایش ‪۱۰‬‬
                                                                                 ‫ساییدن باشد ‪.‬‬
   ‫تهه‬ ‫سک‬ ‫وون‬
            ‫با گ‬ ‫پیر‬
                   ‫سایه پرود ‪-‬ک‬                    ‫سایگی ‏ کون الت کواف بتحتالی‬
 ‫بفراغت وآسودکی برآمده باشد ومحنت ومشقت‬            ‫و یبال شراىخورىرا گونند ‪5 ۴‬‬    ‫‪ ۰‬قدح‬   ‫رسده‬
‫نکشیده باشد ‪ -‬و کیامی هم هت که آنرا‬                            ‫وبمعنی کلاغ نیز بنظر آمده است‪.‬‬
‫از مردم مفت خور‬       ‫کنوابه‬
                           ‫بانخورش کنند ‪-‬‬          ‫سیاوس ‪ -‬بر وزن سالوی‪ ,‬اسبغول را‬
                                        ‫باشد ‪.‬‬     ‫بزر‬   ‫بی‬
                                                          ‫عفرو‬
                                                             ‫مرو‬
                                                               ‫است مع‬        ‫خنمی‬‫تآ‬‫گویند و‬
‫سا به پروران حم (‪ - )۱‬کنابه‬                                                    ‫قطونا خوانند ‪.‬‬
‫از دالهای انکور است که در خم بجهت شراب‬             ‫ساله = بر وزن مابه معروف است ‪- ۳‬‬
                                      ‫انداز ند ‪.‬‬    ‫ابه‬
                                                      ‫و نام دبوی هم بوده است ‪ -‬و جن را فسيز‬
=== leaf 542 ===
     ‫‪«۹‬‬                                                                                    ‫سابه دار‬



                ‫‪۱‬‬              ‫گرفته باشد ‪.‬‬                              ‫بکه و خوش سایه ‪. ۷‬‬
                                                                                          ‫پر ر‬
  ‫ساله شک ‪ -‬کنابه ازروشن گروروشن‬                   ‫ساله‌ذاد ‪ ۲‬ه با دال ابجد بر وزن‬
 ‫ونابه از شخصی است که‌شکننده‬
                           ‫کننده باشد ‪ -‬ک‬              ‫لاله‌زار » شخصی رگاونند که جدناشته باشد‪.‬‬
           ‫مذهب طلمت باشد یعنی کفر وزندقه‪.‬‬          ‫ساية ر‌ابلنعیم ‪ -‬کتابه اخلزیفه‬
  ‫سابه گستر دن ‪ -‬کتابه از التفات‬                                                    ‫و یادشاه است ‪۰ ۴‬‬

  ‫لمودن ویوشانیدن وینهان ساختن‌ وندسن‌وبتن‬         ‫سابه ر کاب د کنابه اژحمات باشد ‏‬
                           ‫وبد گفتن باشد ‪.‬‬                     ‫وتابه از تاحان و متاسان هم همست ‪.‬‬
                                                                                               ‫ک‬
‫نشین ‪ -‬کنابه از شنصی است که‬     ‫سانه‬               ‫سایهر و ‪ -‬بفتح رای قرشت و سکون‬
    ‫نمب و محنت روز کار ندیده و نجشیده باشد‪.‬‬        ‫واو ک‪,‬نایه از شب زندمدار باشد و کنابه ازدزد‬
  ‫سایه ود ‪-‬کنابه ازسابة درخت‌است‬                                       ‫ت ‪.‬‬   ‫ههم‬‫وعیار وشب رو‬
  ‫چه سابه وآفتاب هردو دادد ‪ -‬و کنابه از شب‬         ‫سایه زرده ‪ » ۴‬بروزن‌مایه زده ؛بمعنی‬
                           ‫وروز هم همست ‪#.‬‬        ‫سایه دار است ‪ ۰‬و آن‌کسی باشد که او را جن‬



                                          ‫بیان دوم‬

          ‫در سین بی نقطه بابای آبجد مشتمل پر شفت لفت و کنا نت‬

‫ساق خوشة کندم وجوراکوبند ؛ و باین معنی با‬          ‫بقتح اول و ثالی بالف کشده »نام‬         ‫سا‬
  ‫بای فارسی هم آمده است و بعربی جل خوانند‬                ‫شهربت که بلقیی پادشاء آن شهر بور" ‪.‬‬
                     ‫بكر جيم وسکون لام ‪.‬‬           ‫‪۰‬‬   ‫کشاده‬   ‫ورن‬   ‫‪ >.‬صم اول فر‬    ‫‪۹‬‬   ‫سیاده‬
=== leaf 543 ===
                                                                                         ‫—‬   ‫‪0‬‬
  ‫سیزیوشان بهشت‬

 ‫سپژ پا= با بای فارسی‌بالف کشیده»مردم‬              ‫گوبنذ سرمه کشیدن از میلی کهشبه (‪ )۱‬باشد‬
                  ‫شوم فدم و دامبارك پی باشد‪.‬‬       ‫روشنامی جشم را زیاده کند وه رکه ماخود دارد‬

                                                                           ‫آزچشم زخم ایمن گردد‪.‬‬
‫سبز باع ‪ -‬کنابه از تن و بدن آدمی‬
‫کنابه از آسمان هم‌هست ‪ -‬وبهشت را‬                   ‫سیخ = بکر اون وفتح‌ثالی‌وسگون‌خای‬
                                    ‫باشد ‪ -‬و‬
                                  ‫یگوزبند ‪.‬‬        ‫لبك را گونند مطلقاً خواه درآ دمی‌باشد‬      ‫شطمار‪,‬‬

‫سبز بال ‪ -‬بروزن قحط سال ‪ .‬نام نوعی‬                                                ‫در طعام ‪#.‬‬     ‫وخواه‬

‫ور است ؛ و بجای بای ابجد میم‌هم بنظر‬
                                      ‫از انگ‬        ‫سيد جين = با دال‌ایجد بروزن‌عرقحین»‬
                  ‫باشد‪.‬‬   ‫مبال‬
                             ‫آمده ات که س‬          ‫شمه مبوه‬   ‫و‬   ‫شه‬    ‫أست» وآن‬        ‫بمعنى بماچین‬

  ‫سلیعن»ی‬
        ‫سببزالی ب‪-‬روزن قحبطسا‬                      ‫بود که دخررهای فصل میوه درباغپا‬               ‫‪2‬‬
          ‫سبزبال است که نوعی از انکور است‪.‬‬                        ‫ای‬   ‫باشد ‪۱‬‬   ‫مانده‬   ‫ودرختها حایجا‬



 ‫ز ار ی » بروزن چرخ کری ‪ ,‬فصل‬                      ‫مب اج زور و‬             ‫خری‬
                                                                             ‫سبزآ‬
                              ‫سب‬
                  ‫است‬     ‫اهر‬
                            ‫هک‬‫ببند‬
=== leaf 544 ===
  ‫‪ ۷‬با ‪— ۵‬‬


‫گ بروزن نفزك‪ .‬مصفر سبز باشد‬
                          ‫سپز ل =‬                            ‫یکه‬
                                                               ‫ابه‬
                                                                 ‫زم‪-‬لکنا‬
                                                                       ‫فالك‬             ‫اون‬
                                                                                          ‫شز ب‬
                                                                                             ‫سب‬
‫‪ -‬وبمعنی صراحی شراب هم‌هست ‪ -‬و نام مرغی‬                                                               ‫باشد ‪.‬‬
‫سبز دلگ بسرخیآهخته و تاجی هم دارد‬              ‫أت‬            ‫سبز بهار = ناملحنی‌امت ازموسقی‪۱‬‬
‫مائند عدهدو" نرا بعربی شقراق (‪ )۲‬خواند ؟؛‬                    ‫سز خو ان » کنابه از آسمان اش‬
  ‫عرکاه‬
      ‫و بعضی کوبند سبزك پرنده ات که او‬
                                                         ‫‪ = ۲‬بكر الك " بمعنی‬            ‫از‬  ‫سی‬
                                                                                         ‫رزهد‬
                                          ‫نف‬
                                                        ‫امت ‪.‬که نام لحن نهم باشد از سی‬             ‫سابنزدرسبز‬
 ‫سب کار گاه = بمعتی سز طشت است‬
                  ‫تابه اآزسمان باشد‪.‬‬
                                   ‫که‬
                                                                                                   ‫لحن پاربد‪.‬‬
                                                         ‫سز ‪ = ۵۵‬بکر دال ابجد (‪ )۱‬و ظپور‬
 ‫سمز گرا = باکاف فارسی‌ورای‌فرشت(‪)۳‬‬                                       ‫آزسمان است‪.‬‬
                                                                                    ‫های هوز؛ کنابه ا‬
‫بااف کشیده ‪ .‬به‌عنی سبزقب) است‪ .‬وآن مرغی‬
‫باشد بز برخی مایل و تاح‌دار‪,‬و باتشدید رای‬                ‫سبز راع = با زای هوز بر وزن مبز‬
                                                        ‫را نیز‬        ‫سستم‪ -‬و‬
                                                                     ‫ان‬         ‫باغ ک‪۰‬نابه از‬
=== leaf 545 ===
                                                                                        ‫ره باس‬
 ‫سر کوه وقلهٌکوه باشدب وفرق‌سررا لکیفزتماند‬            ‫معروفت که منوب ببز باشد همچون سیاهی‬
 ‫سیکیار » بختماول و بای ابجد بالف‬                      ‫وسقیدی کهمنوب بسیاه وسفید است ‪ -‬وسبزی‬
 ‫کشیده و برای قرشت زده‪.‬بمعنی فارغبال باشف ‪-‬‬            ‫خوردنی را نیز گویند ‪ -‬و بمعتی صراحی شراب‬
‫و کی را نیز کویند که پبوسته شادی کند‬                   ‫هم آمده است ‪ -‬و خرمی و طراوت را لز‬
                ‫وخوشحال وصاحب اشعاش باشد‪.‬‬                                                    ‫گفته اند ‪.‬‬

‫سیکیای س با بای فارسی * کنابه از‬                       ‫سبع !لوان ‪ -‬سیعها لوان ‪ .‬هفت‬
‫کریزپای ونندوئیز براه روقده باشدت وییاد کافیرا‬         ‫رنگتطعام‌را کوبند وآن از سنتهای فرعون است‬
‫گزوند که منزل بمنزل کذارند تا خبر وغامه‬
                                      ‫ن‬                ‫‪-‬هفت طقهٌ زمين‬
                                                                    ‫‪-‬توابه از هفت‪.‬آسمان و‬
                                                                                        ‫ک‬
 ‫بیکدیگر رسان د ‪ ۰‬و این درهندوستانمتمارفت‬                                                     ‫هم هت ‪.‬‬
 ‫و‪-‬اسبی کهدرهرمنزل بجهت پيك تین کنند‪.‬‬                 ‫سبقاثه ‪ -‬بقتح اول و غین نقطه دار بر‬
 ‫‪-‬نابه ازمردم جلد ود‬
                   ‫سباك خیز ک‬                          ‫وزن مستاله » بمعنی بیعانه باشد و آن زری‌است‬
                             ‫و زود خىز باشد‪.‬‬          ‫که بش ازکار کردن بمزدور دهند ‪ - ۷‬وضم‌اول‬
‫سبگدست ‪ -‬کنابه ازشتاب و جلدی‬                                            ‫دراز قد کوشیده بالا گرواشد‪.‬‬
‫باشد در کارهابی کهبادست کنند ‪ -‬وشخص یکه‬
                                                      ‫سبك ‪ -‬بفتح اول وضم الیو سکون‬
          ‫درکارها سرعت و جلدی بکار برد ® ‪.‬‬            ‫»عروف است که در مقابل سنگن باشد‬
                                                                                    ‫کاف م‬
 ‫‪-‬برنتشم‌تر‪.‬ایبمعتیسبکیای‬
                        ‫سیگر و ف‬                       ‫وابه‌ازمردم بی‌وفارونی‌ته‌بود ‪ -‬وبمعنی‌چست‬
                                                                                                ‫‪ -‬کن‬
 ‫اکسرتیکهزپای و تند و نیز براه رونده وجله‬             ‫جرد و بی‬
                                                             ‫و شوتاهب‌‪-‬‬              ‫یل‬
                                                                                      ‫عكم‪۴‬ج و‬
                                                                                            ‫تچاي‬
```


## [2026-09-14T02:32:48.045Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"سپردن\\|سپاردن\\|سپری\" BQT_v2_pages.txt | head -20; echo \"--- leaf numbers ---\"; python3 -c \"\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor w in ['سپردن','سپاردن','سپری','سپهر']:\n    for m in re.finditer(w,d):\n        print(w,'leaf',d[:m.start()].count('\\f'))\n\" | sort -u | head -30"
}
```


### [2026-09-14T02:32:49.272Z] TOOL RESULT

```
14686:     ‫روز گار بادشاهی ‪1-۳‬‬                     ‫از سپری شدن‬      ‫بادشاهان دبشدادی و کیانی تا گناس ماد شده است ‪ .‬یں‬
22044:  ‫= اسپریز دیده ميشود‪ .‬دیزودیزه جکداانه در ادبیات مابمعنی سیاء آمد وبوبژه ازبرای اسب‌سیاه‬
32593:          ‫فاعل سپردن ‪۷‬‬   ‫امر بپردن © _ و‬     ‫‪ -‬و‬
32613:      ‫‪ - ۱‬مراداسم فاعل است ‪ .‬رك ‪ :‬سیاردن » سپردن‪+‬‬                ‫‪ :‬سپاردن » سپردن‪.‬‬   ‫رك‬    ‫®‬
32680:       ‫‪ #‬سپاردن ‪ -‬بکر اول و فتح پنجم مخفف اسپاردن (ه‪.‬م‪ ).‬؛ پهلوی ‪021۳205208‬‬
32681:       ‫[رك ‪ :‬سپردن] و ‪ ۰ 8807110502‬قی‪:‬ارمنی ‪( ۲2۳5-۳2- 0006‬تسلیم کردم » واگذار کردم)‬
32715: ‫فشرد » ماضی‌سپردن است ‪ -‬وبمعنی کوشهشبنی‬
32740:                    ‫رك ‪ :‬سپردن‪. ‎‬‬      ‫‪۴‬‬          ‫حملة دشمن آنرا محافظ اعضاء بدن قرار مبدادند ‪.‬‬
32742:      ‫‪ _¥‬از‪:‬سیر(رك‪:‬سیار) ‪ +‬دن (یسوندمصدری) رك‪:‬سپاردن ‪ ۰‬اسیاردن»سبردن‪‎.‬‬             ‫‪ - ۷‬رکه‪:‬سیردن‪.‬‬
32896:           ‫که شرم دارد خورشید اک رکنم‌سپری ‪.‬‬
32898:                                  ‫‪ ,‬اسپریز » اسپ رز ‪.‬‬     ‫رك ‪ :‬اسب ریس * صپری‬        ‫‪۴‬‬
32902:  ‫عزیز بود آزین پیش حمچنان سپریغ ‪ .‬شهیدبلخی ‪.‬لنتفر ‪٩‬س‪۸۳۲‬‏ ‪.‬‬
34732:  ‫سپریچیدن = کنابه از سکرثی‬                                    ‫برخاستن ویبدار گردبدن باشد ‪ -‬و کنابه‌ازمسافر‬
36257:‫شرور بودند و اوقات خود را بتعقیب پربان » رقص » لای زنی و باده گاری سپری میکردند ‪.‬‬
--- leaf numbers ---
سپاردن leaf 547
سپاردن leaf 548
سپاردن leaf 549
سپردن leaf 547
سپردن leaf 548
سپردن leaf 549
سپری leaf 248
سپری leaf 372
سپری leaf 551
سپری leaf 579
سپری leaf 602
سپهر leaf 152
سپهر leaf 298
سپهر leaf 476
سپهر leaf 530
سپهر leaf 544
سپهر leaf 554
```


## [2026-09-14T02:32:55.908Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 547 548; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt; done"
}
```


### [2026-09-14T02:32:56.996Z] TOOL RESULT

```
=== leaf 547 ===
 ‫سڀار‬                                                                                          ‫سوه =‬
‫سبو شکستن ‪ -‬کنابه از نومید شدن‬                       ‫پبوست مزاج درسآدمی پیدا میشود دورآابمربی‬
‫وا امیدگردیدن ‪ -‬وشراب ریختن‪ -‬ومنع شراب‬               ‫کوبند بفتح خحای بی‌قطه (‪ )۱‬وزای شطه‬         ‫حزازه‬
                                  ‫کردن باشد ‪#.‬‬
                                                    ‫دار ‪ -‬وریز چوب را لی کوبند که ازدم ارمچدا‬
‫سییوش ‪ -‬بکر اوسلکوون الى‬                            ‫شود ‪ -‬وسبوس‌آرد کندم وجو رالیز گفته‌اند ‪۱۰‬‬
‫نقطه‌دار زده » تنم‬       ‫ن‬
                         ‫یو‬‫شیده‬
                              ‫بو کش‬
                                  ‫توحتالی بوا‬
              ‫اسبغول امت که بعربی بزرقطوها گوشد‪.‬‬       ‫‪-‬کرمی باشد که در ابار گندم وجو افند‪.‬‬  ‫و‬


                                              ‫بیان سوم‬

           ‫در سین بی‌نقطه بابایفارسی مشتمل برهشتاد وهشت لفغت و کنامت‬
   ‫ندووا‬
       ‫آارن‬
          ‫حووضیکه درآن شیر انگور بفش‬                 ‫سار = بضم اولبروزن دچار ‪,‬آهن‌جفت‬
 ‫بعربی معصر خوانند ‪ - ۴‬و مطلق ظروف واوالی‬           ‫راکوبند وآن آهنی باشد سرتیز که زمین‌بآن‬
 ‫راکوبند عموماً » وظرفیکه درآن الگور کرده‬
                                                     ‫شیار کنند ‪ - ۴‬و بکسر اول‪,‬اسباب و مایحتاج‬
‫ازجابی بجایی برند خصوصاً ؛ و باين ممالی تم‬
‫ده امت خصوصاً آلات وادوات‌خانه ‪۴‬‬
                               ‫اآولمهم‬               ‫وآلات وادوات خاله باشد ازهرنوعی ‪- ۴‬وچرخی‬
          ‫فاعل سپردن ‪۷‬‬   ‫امر بپردن © _ و‬     ‫‪ -‬و‬
                                                     ‫را پگیوزنند که بدان شیر انکور گیرند ‪- ۴‬‬

                                                                      ‫)‪ (۱‬چك ‪ :‬بقتح حا ‪.‬‬


  ‫‪-‬‬       ‫‪ ( 414010‬دستهٌ خیش ) » از رة‪‎‬‬   ‫هندی باستان ‪-‬‬    ‫‪- ۴‬‬           ‫‪.‬‬   ‫رك‪ :‬سوی‬      ‫‪٩‬‬

  ‫‪( 1205 - 2۵۰‬بازکردن)؛سر یکلی]‪( 15‬خیش) «اسشق ‪«:۹۹۹6‬سپار ‪,‬کارآه نکه زمین‪‎‬‬
            ‫‪« - ۴‬سپار آلت خاله بود ‪ .‬فرخی (سیمتالی) کفت‪: ‎‬‬             ‫شکافند » «لفت فرس‪. ۷۲۱٩ ‎‬‬
      ‫کزآن مزاح ذخیره‌است رزین مزاج سپار»‪-‬‬                ‫بهاله جوبد برحالخوش وهمت خوش‬
   ‫« لفت فری ‪۵۵۱٩‬‏ ‪.‬‬
                                               ‫‪ - ۴‬ارزبشة ‪ ۲9۳8‬بمعنیلکدمال کردن ‪:‬‬
                ‫‪Henning,‬‬     ‫‪Sogdian‬‬      ‫‪loan - words..., BSOS,X,1I, p.‬‬                  ‫‏‪۰‬‬
                   ‫‪۵‬پار ‪ .‬بزبان ماوراهالنهر چرخشت بود و بعرمی هعصر > رودکی(سمرقندی) گفت ‪:‬‬
                                                                                        ‫س‬

                ‫مپرده زبر پای اسر سپارا“ ‪.‬‬            ‫از آن جان توز لختی خون رز ده‬
      ‫‪.‬‬     ‫« لت فرس ‪۷۲۱‬‬

      ‫‪ - ۱‬مراداسم فاعل است ‪ .‬رك ‪ :‬سیاردن » سپردن‪+‬‬                ‫‪ :‬سپاردن » سپردن‪.‬‬   ‫رك‬    ‫®‬

   ‫‪2‬ی‪ . 1606‬سطنزی ‪1101688‬‬    ‫‪5‬رن‬
                               ‫‪ #‬سیل ‪ -‬بکراول »کیلکی ‪» 162۹‬فریزندی وب‬
   ‫‪۱. ۰‬ص ‪ > ۸۸۲‬؛ سمنالی اأتاق‪ . 9‬سنگری و سرخه‌یی ولاسگردی ‪ . 11088‬شهمیرزادی‬
   ‫تاه « ك ‪۲ .‬ص ‪ ۸۱+‬؛ مأخون از «سبلقه (عر) م؛وحابی که بر زبر لب بالاروبد » یروت‬
                                                                             ‫‪.‬‬   ‫ملت‪).‬‬
                                                                                     ‫‪.‬سب‬
                                                                                       ‫ه»‬‫(رب‬
                                                                                           ‫شا‬

=== leaf 548 ===
  ‫رک ها‬

‫گوبند « سپای دارم»‬                   ‫که‬‫نست‬
                                         ‫ام ه‬
                                            ‫نه‬‫چمنت‬
                                                 ‫و‬                                                  ‫‪# .‬‬       ‫هت‬
‫پعنی قبزل دارم و منت پذیرم ‪ -‬و بمعنی لطف‬                       ‫سبارو ‪ = ۵۱‬بفتحاولوالی‌بالف کشیده‬
                      ‫است‪.‬‬     ‫نزآمده‬    ‫ومرحمت‬      ‫وشففت‬
                                                               ‫وثالت بواو رسیده وبکاف زده » بمعنی کبوترباشد‬
‫‏‪ ٣‬گرا اول‌رفتح رابع ‪:‬منت‬                    ‫سیاسه‬
                                                                                       ‫وجربی حمام گوبند ‪.‬‬
 ‫برکسی نهادن باشد ‪ -‬وبمعتی لطف لمودن‌وشفقت‬                      ‫آشاره‪,‬مخفف‬    ‫ولزن‬
                                                                                 ‫راو‬
                                                                                   ‫ببکر‬      ‫سیاره‬
                                      ‫کردن هم هت ‪. ۵‬‬
                                                                 ‫سی پاره است وآن بك جزو باشد اجزسزیو‬
‫=کر اول بروزن قیاسی ؛‬
                    ‫سیاسی ‪ 1‬ب‬                                         ‫و‬
                                                                      ‫ک زا‬
                                                                         ‫کلام خدا ‪ - ۴‬و بفتح اول کے‬
                                                               ‫بدان یز‬       ‫ویر‬
                                                                               ‫مش‬‫شرد‬
                                                                                   ‫که فان سازدد عنی کا‬
 ‫سیاسیان ‪ -‬بر وزن قیاسیان ک»دایدن‬
 ‫و گیابی کنند کان‌باشند‪- ۷‬وامتان‌اولین بیغمبری‬                 ‫یک اول بر وزن شکاری ‪.‬‬         ‫سیاری‬
‫را لیزکوبند که بعجم مبموث شد ‪ - ۸‬و او را‬                       ‫ماقکندم و جو را کویند ‪ ,‬وآن علفی‌باشد ميان‬
  ‫میم و کتاب اورا دساتر‪.‬‬             ‫مهآ بار می‌ناه‌ند کے‬
                                                               ‫خالی کهبخوشة کندم پیوسته است ‪ -‬و بمعنی‬
 ‫سیاناح *‪ -‬بکر اول و اتی با الف‬                                 ‫خوشءٌ کندم وجو همبنظر آمده است ‪ -‬وبهندی‬
 ‫ممتي‬     ‫ونون بالف کشده وبخای تةطه‌دار )‪ ۱‬رده‬                  ‫ینزمت شبیه بفندق و در‬   ‫چآ‬‫قوفل باشد و‬
‫‪ ۳‬وبلاو‬      ‫وآن سمز نی باشد که در‬             ‫اسفناح است»‬
                                                                   ‫عتدوستان با برکیکه آنرا پانگوبندخورند‪.‬‬
                                             ‫وثله کنند (‪.)۲‬‬     ‫سیاس ‪ ۴‬ه بکر اول بروزن قبای ؛‬
 ‫سیاوه = بکر اول وفتح واو بر وزن‬                               ‫قبول‬      ‫نی‬
                                                                          ‫عو‬‫پمشی حمد وشکر نممت بابشدم‪-‬‬

                                   ‫وشله بلاو کنند‪.‬‬    ‫چك ‪ :‬که درآش‬     ‫(‪)۷‬‬        ‫(‪ )۱‬چك ‪ :‬وبضا ‪.‬‬

   ‫زندمغان کجا رسدیر ورق‌سپاره‌ای ؟!‬                ‫‪- ۴‬هرسقطی‌بمپد تولاف‌هنر زندولی‬     ‫‪-‬رك‪ :‬سارو‪.۵‬‬       ‫‪۱‬‬


   ‫سیف اسفردگی ‪«.‬فرهنکه نظام» ‪.‬‬
       ‫‪ - ۴‬پهلوی ‪» 8805‬ارمنی ‪(P5 010-84‬خدمت‏ کردم ‪ ۰‬سپاس‌داشتم) ‪(52۳5 ,‬خدعت)‬
                           ‫‪:‬‬   ‫يان‬    ‫رگ ‪:‬‬‫« اسشق ‪ ۸۹1۰‬ورك‪:‬هوبشمان ‪ ۰ ۸۹۱‬فربکه ‪. ۵۰۲‬‬
                                                ‫‪۴‬‬



              ‫بدو بر سپاسه لینداشتم ‪.‬‬                            ‫وزآن پس که بدکرد بگذاشتم‬        ‫‪9‬‬
       ‫ابوشکور بلخی‪«.‬لفت فری*‪.*۰۲‬‬
       ‫‪ ۲‬رك ‪ :‬سپاسی ‪۸- .‬ازبرساخته‌های‬                         ‫‪ - 1‬از‪ :‬سپس ‪ +‬ی (ست) ورك ‪:‬صاسی ‪(0‬‬

       ‫فرقة آذر کیوان ‪ « :‬دختین نظر در بیان اعتقادات علمی و عملی سپاسیان"‪ .‬آغاز ذکر هذهب‬
   ‫سیاسیان پوارسیان که ابشان را ابرانیان نیز خوانند ‪ .‬گروهی هستند که ابشان را ایزدیان‬
       ‫ویزدانیانر آبادبان وسیاسیان ووشیان وانوشکان وآ ذرهوشنگیانو آذربانگویند» «دیستان‌المذاهب‬
   ‫‪.‬‬    ‫اسپناح‪‎‬‬   ‫‪:‬‬   ‫رك‬       ‫‪٩‬‬      ‫یمد ‪.‬‬    ‫‪٩ ۷‬‏ برای اطلاع ازعقاید نتسب باین‌فرفه » رك ‪ :‬دستان ص‪۷‬‬          ‫ص‬

       ‫‪ #‬سپاردن ‪ -‬بکر اول و فتح پنجم مخفف اسپاردن (ه‪.‬م‪ ).‬؛ پهلوی ‪021۳205208‬‬
       ‫[رك ‪ :‬سپردن] و ‪ ۰ 8807110502‬قی‪:‬ارمنی ‪( ۲2۳5-۳2- 0006‬تسلیم کردم » واگذار کردم)‬
        ‫از ‪‘ 52۳9۲ :‬رىش ابرالی ‪. 7203 -‬رك‪ :‬یبر گے ‪ ۰ ۵۱‬حوبشمان ‪۷٩۹‬‏ ورك ‪ :‬اسشق ‪۷۹۹‬‬
       ‫افتانی [‪(125205‬سلیم کردن)‪ .‬کردی ‪« 002419‬اسشق‌ایضا» ؛ تسلیم کردن "دادن » بامات دادن ‪.‬‬
   ‫( برهان قاطع ‪) ۱۳۱‬‬
```


## [2026-09-14T02:33:21.115Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT سپهر leaf 554 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==555' BQT_v2_pages.txt | grep -n \"سپهر\" -A3 -B3 | head -40"
}
```


### [2026-09-14T02:33:22.217Z] TOOL RESULT

```
=== BQT سپهر leaf 554 ===
38-‫وزن کلیچه ‪ .‬چیزی باشد که برروی خم شراب‬              ‫را گوبند ر آن بالای کرة ہوا امت وکر ایر‬
39-‫ومسراکنهند لان بته شود و؛بکر اول‬                                                            ‫همان ات © ‪.‬‬
40-                   ‫وفتح اول هم آمده است ‪.‬‬
41:                                                   ‫سپهر ‪ =۵6‬بروزن سیرغم ‪ ۰‬دامیکی از‬
42-‫ومعنی‌سفدد است‌وسربی‬   ‫ورزن‬
43-                          ‫سییال = ب‬                 ‫پهلوانان توران است از خوبشان افراساب‬
44-                          ‫‪۱‬‬   ‫«اسیاهید»‬   ‫‪ pD‬اسیهید» («‪.‬م‪= ).‬‬   ‫‪wm‬‏‬    ‫«صیاهید»‬     ‫مضفف‬     ‫‪۱‬‬
--
54-      ‫که مهرکان خردك و‪ -‬گاهی سپهبدان‪.‬‬                ‫‪ - ۴‬چون مطربان زندنوایخت اردشیر‬
55-  ‫د منوچهری دامفائی ‪۹۹۱٩‬‏ ‪.‬‬
56-  ‫‪ ۴‬۔ پارسی باستان ‪( 86016105‬نام سردار پارسی که در جنگه کراییکس با اسکندر‬
57:  ‫برد کرد بقول مورخان بونانی ‪ 561601706105‬و ‪ 821270105‬بود ‪.‬لفة بعنی سپهر داد ‪.‬‬
58-   ‫آسمان آفریده ) ‪ .‬پپلوی ‪ ۲1050۷7‬و ‪« 10۹‬اسشق ‪ » ۷۰۷‬و رك ‪ :‬ابران باستان ج ‪ ۲‬ص‬
59- ‫‪ . 41 -‬بقول تلد کهاین کلمه متقیماً ازسا کرت ‪( 8۳01۷-۲‬مابل بسفدی» سفید )‬                             ‫‪۸‬‬
60-   ‫آمده وبقولکایگر کلمةٌ اففانی ‪( 8۳۳3‬خاکستری‌رنگه) ازآ نجاناشی‌است «هوبشمان‪>۷۰۷‬ورك‪:‬‬
```


## [2026-09-14T02:33:22.964Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt && echo \"=== اسپناخ in BQT v1 ===\"; python3 -c \"\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor w in ['اسپناخ','اسفناج','اسپاناخ']:\n    for m in re.finditer(w,d):\n        print(w,'leaf',d[:m.start()].count('\\f'))\n\" | sort -u | head -20"
}
```


### [2026-09-14T02:33:24.201Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
=== اسپناخ in BQT v1 ===
اسپناخ leaf 330
اسفناج leaf 329
اسفناج leaf 332
اسفناج leaf 346
اسفناج leaf 358
اسفناج leaf 625
اسفناج leaf 740
```


## [2026-09-14T02:33:35.929Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==331' BQT_v1_pages.txt | grep -n \"اسپناخ\" -B4 -A10 | head -40"
}
```


## [2026-09-14T02:33:37.096Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 MON_part1.txt; echo ...; grep -c \"\" MON_part1.txt; echo \"=== search ===\"; grep -n \"اسفناج\\|آتمسفر\\|سپهر\" MON_part1.txt MON_part2.txt | head -20"
}
```


### [2026-09-14T02:33:37.119Z] TOOL RESULT

```
14-۱ و
15-اراشی آهکی عمیق خوب میرو‌بد .
16-- ۱۸۱ « کل کلاب ۷۱ >.
17-روستامی ۱۸۱ > .
18:۷ تب ره 2 اسپناخ.
19-و
20-ت که عرصه و میدان باشد»
21-و ۳
22-بیعنی اسب رز است
23-و گس اول هم آمده لت
24-اسیر سب « بسکون مين و بای اپجد »
25-بیعنی اسپ ری انت که عرصه و میدان باشد»
26-و یکس اول هر کنتانه ۴
27-آسپر سیف « بافاء بروزن‌ومعنیاسپرسب
28-است که فنا و عرصه و میدان باشد ۴ .
```


### [2026-09-14T02:33:37.206Z] TOOL RESULT

```
0 
2 

...
99339
=== search ===
MON_part2.txt:5024:معطر از تبرهٌ اسفناجیان که بصورت درختجه 
MON_part2.txt:15608:خنکی نگاهدارند. قورمهٌ اسفناج: گوشت 
MON_part2.txt:15611:نیم‌پز که شد اسفناج را هم در روغن پیاز 
MON_part2.txt:15657:شبت و اسفناج خرد کرده را در روغن و پیاز 
MON_part2.txt:26172:متعلق به ابلیس. آسمان؛ سپهر. (کد.) قوس 
MON_part2.txt:28217:مانند: کوکوی اسفناج» کوکوی بادنجان؛ 
MON_part2.txt:33382:اسفناجیان که در اکثر نقاط معتدل زمین 
MON_part2.txt:33472:تبرة اسفناجیان که زینتی است و در باغجه‌ها 
MON_part2.txt:40690:است از تبرة اسفناجیان که در سواحل در باها 
MON_part2.txt:57887:از تبرة اسفناجیان دارای ساقه و شاخه‌های 
MON_part2.txt:75158:اسفناج نر کث. درخت بی‌بره توتا ت کف 
MON_part2.txt:75210:سرخ کرده تهیه کنند و گاه در آن اسفناج 
MON_part2.txt:75309:تشك اسفناج رو کثز (گیا.) نوعی اسفناج 
MON_part2.txt:83944:امر» ولی. والی آسمان (سپهر) اول: (کد.) 
MON_part2.txt:83945:قمی ماه. والی آسمان (سپهر) دوم: (کد.) 
MON_part2.txt:83946:عطار» تیر. والی آسمان (سپهر) سوم: ( کد.) 
MON_part2.txt:83948:(کد.) شمس, آفتاب. والی آسمان (سپهر) 
MON_part2.txt:83951:آسمان (سپهر) هفتم: ( کد.) زحل» کبوان. 
MON_part2.txt:87726:بلوط و اسفناج و کلم و توت فرنگی و 
MON_part2.txt:87765:و اسفناج همراه با ویتامین ,13 می‌باشد»
```


## [2026-09-14T02:33:48.245Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 329 332; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -n \"اسفناج\" -B6 -A10 | head -40; done"
}
```


### [2026-09-14T02:33:49.348Z] TOOL RESULT

```
=== leaf 329 ===
28-عنیم اسب اندازد » منی بتازد .
29-اسیاثیر ۱ ه با بای بالف کشیده
30-ویشون زده وضم بای دیگر وسکون رای قرشت»
31-نام شهري است که انوشیروان بناکرده و طاق
32-ک وا در آن شهر سلخت ۰
33-اسپانج « با بای فارسی بالف کشیده
34:وقتح نون وسکون جبم, اسفناج باشد وآن‌سبزی
35-اسپا نگیز مهمیز را کویند و آن
36-آهنی باشد سر نیز که برپاشنة کفش و موزه‌ضب
37-کته و اس انگز شرا کرو کته که
38-سوار باشد - وامر باین‌معنی حم‌حست عنی اس وا
39-برانگیز و بجهان .
40-اسپاف - پکس اول وسکون تانی و بای
41-بالف کشده وبپاي‌زده ؛ کر انبوه وسیاه‌باشد ۸
42-خاو ع را انتاه ق گویند. که خازی. فلت
43-خوانشد ٩‏ , و حالات‌خضف مشهور است که اسه
44-باشد ؛ و با بای فارسی لیر درست است . *
=== leaf 332 ===
1-قطونا باشد ۷ » و معنی ت رکیبی آن گوش اسب ۱
2-است ۰ چه غول بدمنی کوش هم آعده است ؛
3-وجط یکونند چون ب رکه آن بگوش اسب‌شبه
4:و معنی اسفناج است »
5-و آن سبزی باش د که در
6-آش و هله کنند , سرفه
7-است‌بنابرین اسب‌غول خوانند و بضی بشپش‌تشبیه | دا نافع ات (,
8-کرده اند , و جتح اول هم درست است . اسینانج .
9-باجیم مر وزن اصفهانك »
10-بمعنی اسفناح ننک 5
11-سبزی آش باشد ۴ . اسیناخ ( اسپناج )
12-ا سید ه معروفاست و (۲) آن دانه‌ای
13-باشد که بجپت چشم زخم در آش ریزند ۵ .
14-اسیندار بمعنی شمح باشد که معشوق
--
28-هیجگاه نارم بخانه کرد مقام ازانکه خانه پراز اسیغول جانور است .
29-واسیخول در شمرمذ کور بی‌شك بمعنی ماس است . « لفت‌نامه > -
30-۴ حکیم مومن وصاحب مخزن‌الادوبه « املنج > آورده اند . « لفت‌نامه » .
31-؟ - بلت‌علمی 50102012 بانگلی 5۳18260 با 50101286, بفرانسه 60102۲05
32-با لمانی01024کوعربی اسفاناخ» وفارسی‌اسیناخ»اسیناج» اسینانج,اسپاناج.اسپانج» اسباناج» اسباناخ‌ودد
33-طبری اسینا «واژه نامه۲۸> حمه‌ازيك ربشه است. داودشرسر انطا کی‌درتذ کرخود گوید : اسفاناج
34:مرب عن‌فارسية هواسباناح * ۰ دربونانی 5۳1081108 « اختینگاس » وآن از تیر* اسفناجیان ؛
35-ودارای ربشة قرمز دنگ وب رگهای خوراکی و کلهای نرومادء آن جداست . « کل گلاب4 ۰*۲۷
36-ی فرحنگه روستایی ۱۸-۱۸۳ > . ۴ راد : اسیناج ۱ ۵ در اوستا ٩۳۵1۵‏
37-بمعتی مقدس < بارتولمه۱۹۱۹ > ۰ طبری 65۳021 « واژه‌نامه ۷۷ ۰۲ کیلکی ٩۳20-4202‏ ,
38-قظرسی نیز اسفند . 18۱98 112۲۳0812 این گیاء در اغل نفاط ابران خود روست . «فرهنگه
39-روستابی۱۸4 * . ۱ ره : اسیندبار. ۷ ر4: امیندارمة .
40-خبه از صفحة ۱۱4۹
41-پورداود . بقما ۲ : ۱۲ * پهلوی 25۳25 « اونوالا ۲۸۰ > .
42-۵ اسبله - با سیلی 212015 51۷0۲135 از ماهیان
43-استخواندار که بچةٌ ماهیان پربهارا میخورد واز همین نظر ماهی
44-مسیارمضری‌است وقسمت عمده زند گانیرا در کودالهای‌رودخانه‌ها
```


## [2026-09-14T02:33:51.188Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC/\" \"https://abadis.ir/fatofa/%D8%B3%D9%BE%D9%87%D8%B1/\" \"https://abadis.ir/fatofa/%D8%A2%D8%AA%D9%85%D8%B3%D9%81%D8%B1/\" \"https://abadis.ir/fatofa/%D8%B3%D9%BE%D8%B1%D8%AF%D9%86/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 470: Mo'in (MON) entries for اسفناج/سپهر/آتمسفر/سپردن\"; done"
}
```


### [2026-09-14T02:33:59.252Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1d64f6578b300ef7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9a7dc6f52403d93.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3cb6245e95c08010.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/693165b8a6ddcccb.txt
```


## [2026-09-14T02:34:11.532Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 1d64f6578b300ef7 e9a7dc6f52403d93 3cb6245e95c08010; do echo \"##### $f\"; grep -n \"فرهنگ فارسی معین\" -A25 $f.txt | head -40; echo; done"
}
```


### [2026-09-14T02:34:12.587Z] TOOL RESULT

```
##### 1d64f6578b300ef7

##### e9a7dc6f52403d93

##### 3cb6245e95c08010
```


## [2026-09-14T02:34:14.860Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 1d64f6578b300ef7.txt e9a7dc6f52403d93.txt 3cb6245e95c08010.txt 693165b8a6ddcccb.txt; echo \"---\"; head -40 1d64f6578b300ef7.txt"
}
```


### [2026-09-14T02:34:14.911Z] TOOL RESULT

```
21672 1d64f6578b300ef7.txt
18711 e9a7dc6f52403d93.txt
10832 3cb6245e95c08010.txt
20545 693165b8a6ddcccb.txt
71760 total
---
URL: https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC/
FETCHED: 2026-09-14T02:33:53Z
STATUS: 200
TITLE: اسفناج - معنی در دیکشنری آبادیس

اسفناج - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 اسفناج
 /~esfenAj/

 برابر پارسی : اسپناج
 معنی انگلیسی : spinach , spinage 

 دنبال کنید 

 لغت نامه دهخدا

 اسفناج. [ اِ ف َ / ف ِ ] ( اِ ) اسفاناخ. اسفناخ. اسپناج. اسپاناخ. اسپنانج. سپاناخ. رجوع به اسپناج شود : 
بابای تو چارده پسر داشت 
نی میزد و اسفناج میکاشت. ؟
 اسفناج. [ ] ( اِخ ) دهی جزء دهستان زنجان رود بخش حومه شهرستان زنجان ، 30000 گزی شمال باختر زنجان ، 3000 گزی راه آهن زنجان به تبریز. دامنه. معتدل. سکنه 530 تن. آب آن از زنجانرود و قنات. محصول آن غلات ، میوه جات ، مختصر برنج. شغل اهالی زراعت. راه آن مالرو و در غیر بارندگی اتومبیل رو است. ( فرهنگ جغرافیائی ایران ج 2 ص 13 ). 

 فرهنگ فارسی

 ( اسم ) گیاهی است سر دست. گیاهان تیر. اسفناجیان جزو دو لپه ییهای بی برگ گلهای آن خوشه یی سبز رنگ و کوچک دارای ۵ پرچم و ۵ کاسبرگ بهم چسبیده است . یا اسفناج رومی . ۱ - گیاهی است از تیر. سدابیان از نوع کواچها دارای انواع مختلف . گیاه مذکور پایا و پر شاخه و با ساق. چوبی و دارای تیغهای درشت بلند و برگهای دراز نوک تیز است . ۲ - سلمه یا اسفناج صحرایی . گیاهی از تیر. اسفناجیان از جنس سلقها که جوانه های جوان آن مانند مار چوبه مصرف میشود .
دهی در شهرستان زنجان 

 فرهنگ معین

 (اِ فَ یا فِ ) ( اِ. ) = اسپناج . اسپناخ . سپاناخ . اسپاناج : گیاهی است یک ساله دارای برگ های پهن و ساقه های سست و نازک ، در پختن آش و پاره ای از غذاها مورد ا ستفاده قرار می گیرد. ، ~ سبز شدن از کلة کسی (کن . )تعجب شدید به کسی دست دادن . 

 فرهنگ عمید

 گیاهی یک ساله با برگ های پَهن، ساقه های سست و نازک، و گل های ریز سبزرنگ که به عنوان سبزی خورده می شود. 

 فرهنگستان زبان و ادب

 {Spinacia} [زیست شناسی- علوم گیاهی] سردۀ دوپایۀ علفی یکسالۀ افراشته، بدون کرک با سه گونه که در آسیای مرکزی و غربی رشد می کنند؛ برگ های این گیاهان دمبرگ دار و متناوب و گل هایشان تکجنسی است
```


## [2026-09-14T02:34:19.262Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### سپهر\"; grep -n \"فرهنگ معین\" -A6 e9a7dc6f52403d93.txt | head -20; echo; echo \"#### آتمسفر\"; sed -n '1,60p' 3cb6245e95c08010.txt"
}
```


### [2026-09-14T02:34:19.346Z] TOOL RESULT

```
#### سپهر
69: فرهنگ معین
70-
71- (س پِ ) [ په . ] (اِ. ) ۱ - آسمان . ۲ - فلک . 
72-
73- فرهنگ عمید
74-
75- ۱. آسمان، فلک.
--
226: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
227-
228- لینک ها 
229-
230- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
231-
232- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 

#### آتمسفر
URL: https://abadis.ir/fatofa/%D8%A2%D8%AA%D9%85%D8%B3%D9%81%D8%B1/
FETCHED: 2026-09-14T02:33:57Z
STATUS: 200
TITLE: اتمسفر - معنی در دیکشنری آبادیس

اتمسفر - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 اتمسفر
 /~Atmosfer/

 مترادف اتمسفر : ( آتمسفر ) جو، فضا، هوا، محیط، شرایط، وضعیت
 برابر پارسی : ( آتمسفر ) هوابار، پناد | هواسپهر، هوابار، پناد
 معنی انگلیسی : atmosphere 

 دنبال کنید 

 فرهنگ فارسی

 ( آتمسفر ) ۱ - تود. هوایی که اطراف کر. زمین را فرا گرفته جو.این توده از گازهای مختلفی تشکیل شده : ۷۸ ازت ۲۱ اکسیژن ٠۳ اسید کربنیک ۹۴ آرگون ٠۱ ئیدرژن و گازهای دیگر مانند نئون هلیوم و غیره میباشد . ۲ - ( در فارسی ) محیط فضا وضع محیط . اتمسفر:طبقه بخاریاجو، طبقه هوا، واحدفشارهوا
آتمسفر 

 فرهنگ معین

 ( آتمسفر ) (مُ فِ ) [ فر. ] (اِ. ) ۱ - تودة هوایی که اطراف کرة زمین را فرا گرفته ، جو. ۲ - کنایه از: اوضاع و احوال . (اَ مُ فِ ) (اِ. ) نک آتمسفر. 

 فرهنگ عمید

 ( آتمسفر ) = اتمسفر ۱. طبقۀ هوا که گرداگرد کرۀ زمین را فراگرفته و از گازهای مختلف مانند ازت، اکسیژن، اسیدکربنیک، آرگن، هیدروژن، و غیره تشکیل شده، طبقۀ بخار یا جو.
۲. (فیزیک ) واحد اندازه گیری فشار یک کیلوگرم بر یک سانتی متر. 

 فرهنگستان زبان و ادب

 {atmosphere} [علوم جَوّ] یکای فشار برابر با فشار ستونی از جیوه به ارتفاع 76 سانتی متر 

 دانشنامه عمومی

 اَتمُسفِر ( از یونانی باستان، راه یافته به تمام زبان های اروپایی و بسیاری زبان های دیگر ) یا جَوّ[ ۱] ( وام واژه از زبان عربی ) یا هواسپهر ( معادل فارسی ) یا پناد و همچنین ویو ( پپارسی میانه ) یک یا چند لایه از گاز است که دور یک جسم آسمانی مانند یک سیاره، ستاره، یا قمر را احاطه کرده است. جوّ به واسطهٔ نیروی گرانش به دور شیء آسمانی نگه داشته می شود. اتمسفر فضایی پوشیده از یک یا چند گاز است که اطراف یک سیاره یا ستاره یا سنگ فضایی را پوشانده است. اگر اتمسفر از چند لایهٔ گازی تشکیل شده باشد تمام این لایه ها حکم یک محیط به هم پیوسته را داشته و از دیدگاه علمی مجموعاً یک لایه محسوب می شوند. اتمسفر کرهٔ زمین عامل زنده ماندن همهٔ موجودات زنده در روی کرهٔ زمین است و بدون آن همه موجودات زنده در روی کرهٔ زمین نابود خواهند شد. گازهایی که در اتمسفر یک سیاره یا ستاره وجود دارند ساکن نبوده و مدام در حال حرکت در لایهٔ خود هستند. اتمسفر فقط مخصوص یک سیاره نیست بلکه ستارگان و سنگ های فضایی نیز ممکن است اتمسفر داشته باشند. [ ۲] 
در اتمسفر، یک مبحث علمی جدید به نام دینامیک اتمسفر را می توان مطرح کرد. اصول و کلیات علم دینامیک اتمسفر در نیروهای وارده از طرف اتمسفر بر یک شیء پرنده در آسمان تعریف و خلاصه می شود. به طور کلی این طور می توان گفت که اتم ها و مولکول های گازهای موجود در اتمسفر زمین، درحال حرکت هستند و براساس قوانین فیزیکی، این اتم ها و مولکول ها؛ اولاً دارای انرژی هستند و ثانیاً دارای نیرو هستند؛ بنابراین هنگام برخورد با یک جسم در آسمان ( مانند هواپیما و شهاب سنگ ) از خود انرژی آزاد کرده و بر این جسم نیرو وارد می کنند. مقدار نیروی وارده از طرف اتم ها و مولکول های گازهای اتمسفر، هیچ حدّ خاصی نداشته و ممکن است باعث به عقب رفتن یک هواپیما در آسمان شده یا باعث منفجر شدن یک شهاب سنگ در آسمان بشوند. 
اصطلاح اتمسفر ستاره ای برای اشاره به بخش بیرونی یک ستاره به کار می رود و معمولاً قسمت بالاتر از کدری نور سپهر را دربر می گیرد. ستاره هایی که دمای آن ها به اندازه کافی پایین باشد ممکن است دارای اتمسفر بیرونی با مولکول های مرکب باشند. 
جوّ زمین[ ۳] [ ۴] بالاترین بخش تشکیل دهندهٔ کرهٔ زمین است که مخلوطی از گازها شامل نیتروژن ( ۷۸٪ ) ، اکسیژن ( ۲۱٪ ) ، آرگون ( ۰٫۹٪ ) و کربن دی اکسید ( ۰٫۰۳٪ ) است. اتمسفر زمین از سطح زمین آغاز شده و تا ارتفاع ۱۰٫۰۰۰ کیلومتر ( ۶٫۲۰۰ مایل ) ادامه می یابد. [ ۵] ۹۹ درصد از جوّ زمین در فاصله ۳۰ کیلومتری از سطح آن قرار دارد. اگرچه سیاره های دیگر منظومهٔ شمسی نیز هواکره دارند ولی جوّ زمین تنها جوّی است که از زندگی موجودات زنده پشتیبانی می کند. [ ۲] 
 wiki: اتمسفر 

 این نوشته برگرفته از سایت ویکی پدیا می باشد، اگر نادرست یا توهین آمیز است، لطفا گزارش دهید: گزارش تخلف 

 دانشنامه آزاد فارسی

 آتمسفر. آتمسفر (atmosphere)
(یا: آتمسفر استاندارد) در فیزیک، واحد فشار، با نماد atm. برابر با ۷۶۰ میلی متر جیوه، ۱۰۱۳.۲۵ میلی بار، و ۱۰۵×۱.۰۱۳۲۵ پاسکال(نیوتون بر متر مربع) است. مقدار فشار واقعیکه جَوِّ زمین بر اجسام وارد می آورد، حدوداً برابر همین مقدار است ودر سطح دریا و دمای صفر درجۀ سانتی گراد، استاندارد فرض می شود و در فشارهای بالا به عنوان واحد فشار به کار می رود. نیز ← جوّ wikijoo: آتمسفر 

 جدول کلمات

 آتمسفر
هواکره, جو جو 

 مترادف ها

 aerosphere (اسم) 
 جو، اتمسفر، کرهء هوا
```


## [2026-09-14T02:34:33.641Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 sper ===\"; ls incoming/WLD/; grep -n \"spher\\|sp(h)er\\|sperno\" WLD_band3.txt | head -10"
}
```


### [2026-09-14T02:34:33.705Z] TOOL RESULT

```
=== WLD Bd2 sper ===
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
803:™ Xi. Lateinisch, scfaa, aoedad — atrigo, -dre Sa cocene 114", gerpo, -ere G02". #opio, -ire 529°. -tre 544°. serra 501". sorbeo, -Gre TOK". i 264, HS", G62", aerua 462°. srex 525". uum oi a, fie 458". aperua, eparnm 665%. ed" wviat ,,orpal” 460" spatinrn i acreo, «dre (416). aibl, a i apecio, -ere G00" _ vere G6". sibilo, ire 515* epecus 600". : sibus 451%. sperno, -ere 660". éica, Sicilia 475*, epicd, epicwe GDM". siccus G06, (407*). pina O53". vido, -ere 454". spiro, -dre LI", i* widua, -eria (287), 520*. a a | rignam (478*), splendeo, -ére ((04"), 670%. acriifor, -dri 530". leo, -tre 462". spaliem 678*. . £68 giler (553), SOL. sponda 662*, a, ailicermeum (108), ° spondeo, -Ere (G62*), G65", sculpo, -ere. GOG*. wiligqaa 501". sponte G61". f gilya SOT*. aporta .. sctitum 543°, 040° stmiia (450). *pima 641° 1GR*. imilis, simul 459". #pua, -er simlin 458". equdius (441), 541°. nmplus, -plex 65", 455* fentras . om tsimpulum 455°. dagnum 612*. weco, -fire 474°. simus 519*, aldmen : ruck iat aincdrua 410 gatim 605*. it 474". fincinium | shifor GOO". wi". vine (128), 405°. fladus GOS". a”. dine S3T*. #élia 035". O7. singuli 499° stercue 641°. aedeo, ra 483°. sino, -ere 461°. werilie G40". 454". isto, -cre (08"*. #ermiz €25* aio, -re 453". witie SOO. #erno, ~tre O30". wegee 450", aifula (450*), ilernuo, -ere LOL, segestre 440°. silus ,,Moder™ 606, 451° willa 610". omen, agmentum 474° tg riinaeat’’ Gog. ofilus G12" atgnis 474%, sive, seu 189. stimulus 612°, ome d80*. nus 533%, ainguo, -ere 613". gella 455°. ag olat, £58", atipendium (47%. gemeal 430". aoter, aoorua 521". afiipes (46* aimen AGA". secs 4TT*. wipe, -dre O40". at@mi- 493°. soddliv 450". atipa G47". seriplitia 1 ol 445", etipala (417". semper 30", 485° solea, solum 532* alipulor, -dri 647T*. ecnex 414", ie 42, afiria 610°, senfing 457*. iilin, -fre GOS". atirpa G31", eeniia, -ire 406", aolero, -are 511". afiva O12", (847%). sentia 450), elidus, exdus S11", glaita (45*. sepelio, -ire 487* acium 484°. slembus 646", weplem 457". eollemnis. 42, 511". 5, shire G03* gepleresmom alat. 144. gollers G11" wfolicdur 44" aequor, i 476". sdlor, -dri G* strdgulas 639", wera G2R*, anlix S11". strimen G30". aerescum! 503, soleo, -ere 407". irfinuus 623", aeriéa, seria GAM)". sommes G23". atrepo, -ere HH", seriaa 235. soniuen, sonidri spitlat. ria 637°. aermo SZ7™. (ip. strides, -tre O51". gerd ,fiige™ 500*. fono, -ere G24". atriga, sfrightus 637%. gero aio" I, gona 100, #rizo, ~ire 1419".
```


## [2026-09-14T02:34:35.950Z] TOOL CALL #53: Bash

```json
{
 "command": "pdftoppm -f 470 -l 470 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg470 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-14T02:34:37.617Z] TOOL RESULT

```
total 28124
drwx------ 3 sfmqrb sfmqrb   12288 Sep 13 22:34 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   92443 Sep 13 21:13 391-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  129993 Sep 13 21:11 394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21316 Sep 13 21:11 394-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44712 Sep 13 21:14 400-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116049 Sep 13 21:14 400-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99858 Sep 13 21:16 404-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91913 Sep 13 21:18 411-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34177 Sep 13 21:23 412-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79667 Sep 13 21:24 414-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110116 Sep 13 21:31 417hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88133 Sep 13 21:31 417-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12361 Sep 13 21:31 417-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45082 Sep 13 21:33 421-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96996 Sep 13 21:38 428hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18073 Sep 13 21:38 428-zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21962 Sep 13 21:38 428-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  112884 Sep 13 21:41 429hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16099 Sep 13 21:41 429-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96248 Sep 13 21:43 431-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   94911 Sep 13 21:46 432-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115297 Sep 13 21:42 436-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125916 Sep 13 22:14 440-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  119070 Sep 13 22:18 442hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32445 Sep 13 22:18 442-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99953 Sep 13 22:12 444hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18325 Sep 13 22:12 444-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77093 Sep 13 22:10 445-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115375 Sep 13 22:12 446-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb  113997 Sep 13 22:18 450hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21276 Sep 13 22:18 450-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   85759 Sep 13 22:19 454-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  114246 Sep 13 22:16 457hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17873 Sep 13 22:16 457-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1227534 Sep 13 21:24 afm74-420.png
-rw-rw-r-- 1 sfmqrb sfmqrb  908713 Sep 13 21:23 afm76-421.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2451 Sep 13 22:28 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep 13 21:29 ahd430.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   46904 Sep 13 21:10 beekes410.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  207924 Sep 13 22:34 bly78-473.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1158 Sep 13 21:33 bqt1328-ftr-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1151 Sep 13 21:33 bqt1328-hdr-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1872 Sep 13 21:33 bqt1328-top-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3114 Sep 13 21:33 bqt1330-top-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb     146 Sep 13 22:00 bqt1-440.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  309946 Sep 13 21:35 bqt2123-fn-435.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95654 Sep 13 20:53 bqt390_436_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   34040 Sep 13 20:54 bqt390_436_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  124665 Sep 13 20:53 bqt390_662_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   93636 Sep 13 20:53 bqt390_662_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  537986 Sep 13 20:53 bqt390_n436.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527696 Sep 13 20:53 bqt390_n662.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  267233 Sep 13 22:02 bqt439-l254.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  171966 Sep 13 22:31 bqt469-n486-bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  620205 Sep 13 22:31 bqt469-n486.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   13019 Sep 13 22:31 bqt469-n486-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  254148 Sep 13 22:32 bqt469-n547-bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  123533 Sep 13 22:32 bqt469-n547-fn2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97094 Sep 13 22:32 bqt469-n547-hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb  583572 Sep 13 22:32 bqt469-n547.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  245067 Sep 13 22:32 bqt469-n547-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2642 Sep 13 22:32 bqt469-n547-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21513 Sep 13 21:39 build2-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19296 Sep 13 21:42 build3-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66340 Sep 13 21:06 build-389.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60725 Sep 13 21:08 build-390.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66850 Sep 13 21:11 build-391.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67328 Sep 13 21:13 build393.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65361 Sep 13 21:10 build-394.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53331 Sep 13 21:06 build-395.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49820 Sep 13 21:12 build-396.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61718 Sep 13 21:06 build-398.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55842 Sep 13 21:13 build-400.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56563 Sep 13 21:13 build-401.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45908 Sep 13 21:12 build-405.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52807 Sep 13 21:06 build-406.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63772 Sep 13 21:13 build-407.py
-rw-rw-r-- 1 sfmqrb sfmqrb   44609 Sep 13 21:22 build-412.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55188 Sep 13 21:23 build-414.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53220 Sep 13 21:24 build-415.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76184 Sep 13 21:30 build-417.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56437 Sep 13 21:35 build-418.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55739 Sep 13 21:45 build-419.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59029 Sep 13 21:41 build-422.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56950 Sep 13 21:42 build-425.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63145 Sep 13 21:40 build-426.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53942 Sep 13 21:37 build-428.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66449 Sep 13 21:40 build-429.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52975 Sep 13 21:39 build-430.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56759 Sep 13 21:42 build-431.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21413 Sep 13 21:37 build-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50426 Sep 13 21:45 build-435.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61435 Sep 13 21:55 build-438.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71845 Sep 13 22:16 build-439.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65194 Sep 13 22:13 build-440.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61144 Sep 13 22:11 build-444.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55607 Sep 13 22:10 build-445.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65723 Sep 13 22:11 build-446.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52352 Sep 13 22:17 build-447.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42400 Sep 13 22:13 build-448.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57147 Sep 13 22:17 build-450.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60619 Sep 13 22:15 build-452.py
-rw-rw-r-- 1 sfmqrb sfmqrb   86059 Sep 13 22:16 build-453.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76125 Sep 13 22:18 build-454.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80202 Sep 13 22:19 build-455.py
-rw-rw-r-- 1 sfmqrb sfmqrb   35780 Sep 13 22:11 build-458.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2291 Sep 13 20:56 c404-empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77003 Sep 13 21:01 c404-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4255 Sep 13 20:56 c404-patil.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34837 Sep 13 20:57 c404-pest.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46825 Sep 13 20:57 c404-symp2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34820 Sep 13 20:56 c404-symp.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35928 Sep 13 21:11 c412_cedar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42397 Sep 13 21:11 c412_makrome.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81867 Sep 13 21:12 c412_makrome_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54838 Sep 13 21:11 c412_meqrameh.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62842 Sep 13 21:12 c412_meq_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4665 Sep 13 21:12 c412_sedr_zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35561 Sep 13 21:12 c412_sedr_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35749 Sep 13 22:05 c442-fa8b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   26067 Sep 13 22:05 c442-fa8c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5703 Sep 13 22:04 c442-fa8.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17003 Sep 13 22:05 c442-samavar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14614 Sep 13 22:05 c442-samavar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep 13 22:04 c442-samavar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   38593 Sep 13 22:06 c442-symp-zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67256 Sep 13 22:05 c442-symp-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3627 Sep 13 20:54 crop14-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4873 Sep 13 20:54 crop18-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11820 Sep 13 21:11 crop411_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8609 Sep 13 21:11 crop411_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4088 Sep 13 21:11 crop411_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5339 Sep 13 21:28 crop419_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5380 Sep 13 21:28 crop419_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1676 Sep 13 21:28 crop419_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4192 Sep 13 21:28 crop419_d.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3506 Sep 13 21:29 crop419_grk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4444 Sep 13 21:29 crop419_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25580 Sep 13 21:26 crop428a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6915 Sep 13 21:26 crop428b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54756 Sep 13 21:26 crop428c.png
-rw-rw-r-- 1 sfmqrb sfmqrb   48027 Sep 13 21:26 crop428d.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12740 Sep 13 21:36 crop-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36288 Sep 13 22:32 crop460-fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5500 Sep 13 22:30 crop460-latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18309 Sep 13 22:31 crop460-mithere.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep 13 22:31 crop460-shamunhdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3606 Sep 13 22:30 crop460-shamun.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78410 Sep 13 22:32 crop468a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44719 Sep 13 21:39 e0-434.json
-rw-rw-r-- 1 sfmqrb sfmqrb   20203 Sep 13 20:57 edit_about.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6853 Sep 13 21:12 edit_research.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep 13 21:14 ffprof
-rw-rw-r-- 1 sfmqrb sfmqrb   49815 Sep 13 21:44 gen-420.py
-rw-rw-r-- 1 sfmqrb sfmqrb 1434288 Sep 13 21:31 irn-425.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  200105 Sep 13 21:31 irn-425.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  929137 Sep 13 22:03 kent2-448.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     146 Sep 13 22:03 kent-448.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep 13 21:57 knt-440.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep 13 21:58 knt443.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   45281 Sep 13 21:58 meta-443-knt.json
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep 13 22:33 oew459.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  120893 Sep 13 20:58 pg390b.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   39607 Sep 13 20:58 pg390b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  113843 Sep 13 20:57 pg391big.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18836 Sep 13 20:57 pg391crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81140 Sep 13 20:57 pg391.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34659 Sep 13 20:58 pg391root.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21174 Sep 13 20:58 pg391sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75438 Sep 13 20:56 pg392.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101976 Sep 13 20:57 pg393.png
-rw-rw-r-- 1 sfmqrb sfmqrb  145431 Sep 13 20:54 pg394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96039 Sep 13 20:53 pg394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72433 Sep 13 20:54 pg397.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77067 Sep 13 20:55 pg398.png
-rw-rw-r-- 1 sfmqrb sfmqrb   85891 Sep 13 21:00 pg399-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45417 Sep 13 21:00 pg399-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64776 Sep 13 20:54 pg399.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43498 Sep 13 21:00 pg399-sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb  167174 Sep 13 20:58 pg400big.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24547 Sep 13 20:58 pg400_fa_heli.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23086 Sep 13 20:58 pg400_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14689 Sep 13 20:58 pg400_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32600 Sep 13 20:58 pg400_kasak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35662 Sep 13 20:58 pg400_kasak3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22852 Sep 13 20:58 pg400_kasak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79028 Sep 13 20:57 pg400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70671 Sep 13 21:01 pg402.png
-rw-rw-r-- 1 sfmqrb sfmqrb  136264 Sep 13 20:56 pg404hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71542 Sep 13 20:56 pg404.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63962 Sep 13 20:58 pg405.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63610 Sep 13 20:57 pg406.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79866 Sep 13 20:59 pg407.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21327 Sep 13 20:55 pg408-ampus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33681 Sep 13 20:55 pg408-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78365 Sep 13 20:54 pg408.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37449 Sep 13 21:14 pg409.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100242 Sep 13 21:09 pg410hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18557 Sep 13 21:09 pg410-k2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17676 Sep 13 21:09 pg410-kadm2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6217 Sep 13 21:09 pg410-kadm.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7410 Sep 13 21:09 pg410-persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65183 Sep 13 21:08 pg410.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23704 Sep 13 21:09 pg410-q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1736 Sep 13 21:09 pg410-qedam.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64940 Sep 13 21:11 pg411_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56566 Sep 13 21:10 pg411.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161139 Sep 13 21:11 pg412_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74221 Sep 13 21:11 pg412.png
-rw-rw-r-- 1 sfmqrb sfmqrb  481466 Sep 13 21:14 pg412_uhi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35423 Sep 13 21:09 pg413.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36532 Sep 13 21:12 pg414-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74486 Sep 13 21:12 pg414.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3823 Sep 13 21:16 pg415-emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78342 Sep 13 21:16 pg415hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73449 Sep 13 21:11 pg415.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39289 Sep 13 21:17 pg416-v.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55756 Sep 13 21:17 pg417.png
-rw-rw-r-- 1 sfmqrb sfmqrb  178105 Sep 13 21:15 pg418hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87213 Sep 13 21:15 pg418.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28628 Sep 13 21:15 pg418-raj2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13818 Sep 13 21:15 pg418-raj3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6734 Sep 13 21:15 pg418-rajidan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  114625 Sep 13 21:28 pg419_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79366 Sep 13 21:26 pg419.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72677 Sep 13 21:27 pg420b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66620 Sep 13 21:27 pg420.png
-rw-rw-r-- 1 sfmqrb sfmqrb   31408 Sep 13 21:27 pg421.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66285 Sep 13 21:29 pg422.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66328 Sep 13 21:27 pg423.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74989 Sep 13 21:24 pg424.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67629 Sep 13 21:26 pg426.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154381 Sep 13 21:26 pg428hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61436 Sep 13 21:23 pg428.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7200 Sep 13 21:23 pg429-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7703 Sep 13 21:23 pg429-crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4400 Sep 13 21:23 pg429-crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168822 Sep 13 21:23 pg429hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78202 Sep 13 21:23 pg429.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81124 Sep 13 21:24 pg431.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92551 Sep 13 21:33 pg432.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74286 Sep 13 21:24 pg433.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46452 Sep 13 21:28 pg435-n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42245 Sep 13 21:28 pg435-n4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89932 Sep 13 21:28 pg435.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66400 Sep 13 21:31 pg436.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60815 Sep 13 21:36 pg437-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153828 Sep 13 21:36 pg437hi-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100480 Sep 13 21:42 pg438.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82782 Sep 13 22:03 pg439.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75018 Sep 13 22:03 pg440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  174306 Sep 13 22:04 pg442hi-442.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84851 Sep 13 22:03 pg442-p442.png
-rw-rw-r-- 1 sfmqrb sfmqrb  496661 Sep 13 22:06 pg442uhi-442.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77924 Sep 13 21:59 pg443.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70076 Sep 13 21:57 pg444.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24437 Sep 13 22:00 pg444-serom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   19924 Sep 13 22:00 pg444-sibum.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11542 Sep 13 22:00 pg445-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74593 Sep 13 22:00 pg445.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47049 Sep 13 22:03 pg446.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43874 Sep 13 22:04 pg447-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69608 Sep 13 22:04 pg447.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75433 Sep 13 22:04 pg449.png
-rw-rw-r-- 1 sfmqrb sfmqrb  145450 Sep 13 22:01 pg450hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11427 Sep 13 22:01 pg450-pechkam.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79151 Sep 13 22:00 pg450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11602 Sep 13 22:01 pg450-shangarf.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82815 Sep 13 22:05 pg451.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63836 Sep 13 21:59 pg452.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78966 Sep 13 21:58 pg453.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74797 Sep 13 22:01 pg454.png
-rw-rw-r-- 1 sfmqrb sfmqrb  102312 Sep 13 22:00 pg456-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70887 Sep 13 22:00 pg456hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33661 Sep 13 21:58 pg456.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34197 Sep 13 22:05 pg457_crop3b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21717 Sep 13 22:05 pg457_crop3c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4990 Sep 13 22:04 pg457_crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  144439 Sep 13 22:04 pg457hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79186 Sep 13 22:04 pg457.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43086 Sep 13 21:58 pg458.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68729 Sep 13 22:30 pg459.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84070 Sep 13 22:30 pg460hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80591 Sep 13 22:30 pg460.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14451 Sep 13 22:29 pg462-fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb  146281 Sep 13 22:29 pg462hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60489 Sep 13 22:29 pg462.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29574 Sep 13 22:30 pg462-sog2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20304 Sep 13 22:29 pg462-sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62814 Sep 13 22:30 pg463-v.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77174 Sep 13 22:32 pg464.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50604 Sep 13 22:30 pg465.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18202 Sep 13 22:31 pg466-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18603 Sep 13 22:31 pg466-crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15010 Sep 13 22:31 pg466-crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77713 Sep 13 22:31 pg466hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16928 Sep 13 22:32 pg466-osqof.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53053 Sep 13 22:30 pg466.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73548 Sep 13 22:31 pg467.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115827 Sep 13 22:32 pg468hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81319 Sep 13 22:32 pg468.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75634 Sep 13 22:34 pg470.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10610 Sep 13 22:31 pg472-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96623 Sep 13 22:31 pg472hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60397 Sep 13 22:31 pg472.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72343 Sep 13 22:34 pg473.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67658 Sep 13 22:32 pg475.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84381 Sep 13 22:29 pg477.png
-rw-rw-r-- 1 sfmqrb sfmqrb       0 Sep 13 22:27 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  387279 Sep 13 21:13 sem410.html
-rw-rw-r-- 1 sfmqrb sfmqrb   59726 Sep 13 21:14 u_mak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49161 Sep 13 21:14 u_meq.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34177 Sep 13 21:14 u_sedr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47858 Sep 13 21:06 write397.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59484 Sep 13 21:11 write-402.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43710 Sep 13 21:22 write409.py
-rw-rw-r-- 1 sfmqrb sfmqrb   28665 Sep 13 21:19 write410.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47575 Sep 13 21:42 write436.py
```


## [2026-09-14T02:34:40.325Z] TOOL CALL #54: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg470.png"
}
```


### [2026-09-14T02:34:40.926Z] TOOL RESULT

```

```


## [2026-09-14T02:34:40.920Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:34:56.147Z] TOOL CALL #55: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:34:56.223Z] TOOL RESULT

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


## [2026-09-14T02:35:07.127Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT context 26835-26850 ===\"; sed -n '26830,26850p' BRT.txt; echo; echo \"=== SNS spar/spurd ===\"; grep -n \"spurd\\|spar-\\|spart\\|õspurd\\|ospurd\" SNS_pages.txt | head -10"
}
```


### [2026-09-14T02:35:07.258Z] TOOL RESULT

```
=== BRT context 26835-26850 ===
haoma   nmand.paite   . .    'tiauha   *vae(tyä.-
paite  Y.5.  27,
Ableil.  —  lEt,  s.  sfinia-.  —  Vgl,  spJnaA-.— Vä.:  aiBzürtiiTA i  s.  zu  sfinta-,
j.  spanah'vant-  Adj.  'heilig,  sanctus', on  AAura:  das?mB yat  ahmi  spanö  atvan- dasB  'naauha  Yt.  /.  8.
Pü.;  *awzi)'luUiir,  erl.:  ha^  aniiai  Hl  vas  Hc afe  a^uzäyhilm.
•  j.,  g.  spanyah-,  spainyah-"  Adj.  'der beiligere';  i)  von  Göttern:  mainyü  . . yaya  'yä  uHl  mrava^  ySm  angnm  "von den  beiden  Geistern  . .,  von  denen  der heiligere  also  sprach  zu  dem  aigen"  Y. 43.  i;  —  frä  mi  "yh  *maimva  vavaia vispqm  aiaonB  stTm  Y.  ig.  9.  2)  von Menschen:  ava^a  ^ankä  'yä  yai  mqm paiti.p)r)sar3he  "so  wirst  du  heiliger  werden, wenn  .  ."  V. /<?.  7;  —  ''poumjiartm  tBm kirMBsi  "yaalum  V. /o.  13".
Kompar.  zu  sptnta-;  sd.,  auch  zEt  —  mp. spenäk  (mit  i  aus  ar.  aiyj.  —  Pü.  {lu  V.): awiütäilum,  (sonst):  miiaünli,  fa  aaaüniiiA.  — ')  Mit  sfaiii'  nur  Y.  10.  13.
•  g.  spayaOra-  n.  'Gedeihen,  Erfolg, Glück':  ada  sl  ava  drüjö  [ai/j]"  bai-aitl skgndB  '%rahya  a^  asiitä  yaojaittl  (sd.)  . . yBi  sasmil{sü.)  vatihau  sravakS  "alsdann ja  wird  fiit  die  Welt  der  I>rug  die  Zei^ Störung  des  Glücks  erfolgen '>,  aber.." Y.^.  10.
Zu  einem  Praei.  ir.  *{^d- gebildet  3>,  in  ^m ar.  *ii/aia-  Pracs.  24  -  in  imi;  Sp.  1 56 1 0  - and   *ifiA^a;   Praes.  4  oder  37  —  id  i^fä-  -
db,Google
i6i3
spar-
lusammengefallen  sein  kännen.  —  PQ. :  späh 'Heer'  -  Sü. ;  'paläkmikah  -,  wegen  des  Ad- klangs.  —  ')  S.  bav  No.'  14.  —  »)  iSt.  vgl.  Y. $3.  6  unter  fräday.  —  3)  Wie  ai.  gäyalri-, täruira;  iritidlra--a.a.;s.  nochNo.4.  —  4)  Dann vll.  mit  ai.  svälrä-  n.  {im  Nsigh.  'ähanam',  bei Olsenberg  SSE.  46.  26  'power')  lusunmen- gebörig,  das  ein  ar.  Praes.  21  'sgä-  voraus- setien  würde,  oder  -  was  das  selbe  ist  -  eine 'WurielcrwcileninB'  durcli  li;  vgl.  !irv:Ara:
•  j.  Spar- V. 'schnellen,  treten'.  Praes.  3'»
1)  'treten,  stossen';  ma  %wä  dasna mäzdayasnii  aspake  sparSit  sparmaini  (sd.) Vyt..?5-
mit/r,j  'hervorschnellen',  intrans.: /wj (sd.)  aya»h5  frasparai  Y.p.  11.
mit  Vi  'auseinandertreten,  -stampfen'; aiAhh  z^mS  (sd.)  pasnäbya  vTspara  V, 2.31;  32  {wo  visparai).
ai.   ifharäüi     np.   lipardaa.     —     Fü.  (dRn.) :
laiigandaH,   spiirtan,   sfarlan.    —    ')  So  nach
dem  ai.  Praesens.
•  j.  sparaj-a-  m.  'Spross',  von  den  Wider- haken unterhalb  der  Pfeilspitze:  asti  yä *ayat3kama  °ya  "es  kommt  vor,  dass eiserne  Sprossen  (dran,  am  Pfeil)  sind" YLjo.  129  Gl.

=== SNS spar/spurd ===
```


## [2026-09-14T02:35:09.506Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 668 sper ===\"; grep -n \"sp(h)er\\|sper-\\|sperno\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20; echo \"=== IEC ===\"; grep -n \"sphaira\\|sperō\\|sper-\" IEC.txt | head -15; echo \"=== SYN spinach/ball ===\"; grep -n -i \"spinach\" SYN.txt | head -5"
}
```


### [2026-09-14T02:35:09.600Z] TOOL RESULT

```
=== WLD Bd2 668 sper ===
1446:vesper-['^p]tilio „Pledermaus“ (viebnehr von vespertilis oder vespertmus 
1795:vorstellung des Prustens erwachsen; wesentlich dasselbe wie sper- 
2826:zur Erwagung (Pick II^ 18; s. sper-g-), 
2862:u. sper- „drehen"). 
5749:sprukstu, sprUgau, spriigti „entspringen, entwischen" usw. s. u. sper-, spretig- 
39420:„beleidigen'^, da aus *5a^r-; auch nicht nach Fick 11^ 300 zu sperno).^ ai. 
40770:zu sper- „schneidea'‘). ° ’ 
41530:Air. sernim „breite aus‘‘ (= lat. sterno ; nicht besser zu ^sper- „streuen“, 
43212:spend sper- 
43242:1. sper- „Sparren; Stange, Speer''; verbal „mit Sparren verspreizen, stiitzen, 
43243:stemmen, sich sperren", ursprgl. denominativ (s. u. sper- ,,zucken" am 
43245:tener, abgerissener Speiler" zu sper- „rei6en" nach Falk-Torp u. spjcere; 
43247:abweichend Bedeutungsvermittlung mit sp(h)er- „zucken usw.“ sucht, 
43249:sich immerhin auf die unter sper- ,,streuen" behandelten Bed.-Yer- 
43279:sper- 
43288:stoSen‘^ zusammengeflossen und von ihr formal beeinfluBt, s. ^sper- „zucken^0. 
43302:2. sper- in Yogelnamen, besonders „ Sperling 
43340:sper- 
43358:3. sper- „drehen, winden“. 
43406:sper-, sperag- — sp(h)er- 
=== IEC ===
2424:dotis (dotis), io ‘giving, gift. Cf. do-, dí- dómi, etc. Skt. cf. (redup.) dadatib; Av. daitis; Per. dad “gift, justice’; Arm. cf. -tu (in sdon-tu ‘nurse’; dzern-tu “helpful, cf. 8her-); Myc. dos-; Gk. dós beside dósis; Lat. dos, gs dotis; Venet. cf. doóto; W dawd, pl. dodion; OCS dati be- side dašta; Srb. daća ‘tax; fertility; prosper- ity’; Cz. na-dace ‘charitable foundation’; Latv. cf. pa-dots (‘subordinate’, adj. fr. *upo- °); Li. duotis, ies ‘gift
4121:v. id.; Sw. klema ‘pamper’; Cz. cf. hlem-yzd (Canal For -yZd' see ūĝā, io & cf. Lat. vesper- ügo); Li. cf. gliem-eZiai, pl. ‘molluscs’; Latv. glaimi, pl. ‘flattery’; gliemis ‘mollusc’; gliem- ezis ‘snail, mussel’
6416:ieugo (ioug-, iug-) (1) ‘move, stir, drive; strive’. Cf. WP I, 201 Skt. cf. abhi-yujàmi ‘attack’; Av. yaoz-, intr. ‘stir; be roused’; Per. yüzam, -idan ‘jump’; LW in Arm. huzem ‘stir’; Tokh. AB yuk-, A (also) ok- “defeat; Go. ga-jiukan, id.; jiuka “passion, temper’; OE cf. geocor ‘awful’; (o-gde in) MHG jouchen, jóuchen 'chase'; SG jauken, id.; ON eykr, pl.-ir fdraught-animal; eyki ‘cart’; Sw. ök, n., pl. id. *draught-animaP. (Lat. -ügo in vesper-? and lan-" is of uncertain ori- gin)
16784:speK- — sper- (spher-)
16800:sper- (spher-) (1) "seed Cf. sperió, spor- and sprio (2) Gk. cf. spérados, gs: -eos, n. id.; Br. sper, m.
16803:sper- (2) “cloth, rag” Gk. speiron, n, ‘cloth’, cf. speira, f. ‘wrapping, coil’; Icel. spjór, pl. spjarir, f. (rag, scrap’; pl. *clothes")
16804:sper- (3) “hard” Lat. cf. (?) asper, f: aspera (Crough, harsh, if fr. *aK-sper-- WH otherwise); W ffêr, adj. *dense, solid'; ffer, m. “intense cold; MHG sper & spóre, adj. hardened, withered’
16811:sper- — spid-
16880:sporos (2), see sper- E to spar, v. “box, fight w. fists’; LG sparen, v. ‘bristle, bridle’; Slovak cf. spore, adv. ‘quickly’; Li. sparüs, adj. ‘agile’
16952:spr-, cf. sprio (1), (2) and (3) and cf. sphr-, w. derivatives - Spri, io (sphrā, iə) "ball" WP II, 672 Gk. sphaira, f. id.; OE (?) spure, f. ‘heel; Li. spiras, m., spirà, f. “little ball, pellet, glo- bule, dropping of animal"; Latv. spira “animal dropping’. (For OE spure ‘heel’, see sphur- in view of Gk. sphurón 'ankle")
17006:spher-, see sper-, etc.
=== SYN spinach/ball ===
```


## [2026-09-14T02:35:21.011Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '43279,43302p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \"...\"; sed -n '43406,43450p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-14T02:35:21.091Z] TOOL RESULT

```
sper- 


Lit. s^irih^ sp^irti, spiriuos, sp\rtis „sich stemmen, stutzen“, paspirti 
„stutzen'‘, spirdaUy-yti ds. (ein Grebaude^'), „versperren, verschlieSen*’, 

lett, sperties „sich sperren, sich stemmen, sich stauen*^, lit. dtspyris ^Strebe- 
stiitze, Strebepfeiler^'j pdsparas „Stutzbalken“, spyris „Leitersprosse'‘ u. dgl. 
(im Balt, vollkommen mit der Gruppe von lit. spirti „mit dem Fu6e 
stoSen‘^ zusammengeflossen und von ihr formal beeinfluBt, s. ^sper- „zucken^0. 

Ohne anl. s~ slav, "^phrq^ *perti „stutzen'', mit podz- „fulcire“, mit m- 
„claudere^‘ (Miklosicb EWb. 240), z. B. abg. podzp^rq preti ,,stutzen^‘, m- 
prUi „schlie6en^^, russ. u-pereth „stemmen, an oder gegen etwas stiitzen; 
refl. sick woran lehnen, sich wogegen sperren, strauben^", zapereth „ver- 
sperren, verschlieBen“, poln. prsec „spreizen, sperren*', abg. podzporz^ -par a 
^fulcrum, baculum", russ. tipm „Stutze, Strebepfeiler** usw. 

Aber iiber abg. perq, pvrati „treteii" (Persson) s, u. per- „schlagen‘*'. 

Lat. paries „Wand“ (urspriinglich „die Seitenstiitzen eines Zeltes u. dgl.“, 
nicht zu tuer- „fassen**; Persson 472 f.). 

2. sper- in Yogelnamen, besonders „ Sperling 
...
sper-, sperag- — sp(h)er- 


aaO. noch Palk-Torp M.pranger, prelle^ und gegen die Verb, von anaprag- 
gan mit gr, ^Qaxsrov u. „fassen“), lett. Irankti adv. „fest anliegend‘‘ 

(lit Lw.), lit. branga „Knie im Kahn“. 

Gr. ^Q6%og „Schlinge'‘ (doch s. u. mer-^ mera^gh- „flecbten“), ^gox&og 
„Kehle, Schlund'S ^goyxog ^Luftrohre'", doch s. n. g^er- ^verschiingen^'). 

4r. sper-, sperog- „rei6en; Fetzen“. 

Aisl. spiqrr f. „Fetzen, abgerissener Streifen Tuch“ (urg. ^sperro ) ; 

gr. oTiagdooco, att -diiay „zerrei6e, zerre^' (wohl analogisch fur -dfco, 
s. Debrunner IF. 21, 224), ondgayua „abgerissenes Stiick^", oTzagayjuog „das 
Zerren, ReiUen : KrampP ; 

arm. pert „abgerissenes Stuck" {*sperq-to-). JSias. und ohne anl. s- viel- 
leicht abg. prgziti^ prqzati „lacerare" (Persson Beitr. 869, doch in Yerb. ra. 
sphereg- „zucken"). 

Fick III^ 510 = Falk-Torp n. spjcere^ Persson Beitr. 418, 869 a 1. Die 
an letzterer S telle vermutete Beziehung zu sp(li)era^g- in ai. sphUrjati usw. 
geniigt der Bed. „abgerissenes Stuck" nicht (man miiSte denn rein kon- 
struktiv auf das mit dem Zerreifien verbundene krachende Gerausch raten) ; 
germ, ''^sperro kaum als '^sper[gys-a zur Wzf. sper{d)g-. 

1, sp(h)er- jjZucken, mit dem FuUe ausschlagen, zappeln, schnellen“ (im 
Anlaut wechselt sp- und sph-^ s. Persson Beitr. 417). 

Daneben Gruppen mit der Bedeutung „streuen, saen; sprengen, spritzen, 
spruhen u. dgl.^, die teils unter der Yorstellung „mit der Hand zucken, 
schnellen^^, teils unter der der zuckenden, vibrierenden Bewegung iiber- 
haupt im letzten Grunde vervrandt sein konnen, aber doch so weit in der 
Bedeutung abfiihren, daS sie als gesonderte Sippen zur Darstellung ge- 
langen sollen; zumal die W^orte fur „spriihen, spritzen^ auch in nicht ge- 
nauer festzustellendem Umfange auch der SchallvorsteUung des Prustens 
entspringen konnten, vgl. das gleichwertige per- „spruhen, spritzen^t 
S. weiter die folgenden Gruppen: sper- „Sperling^‘; sper- „Sparren“, 
spQi)er- „Mistkugelchen^, 5p(/0ere^- „zucken“, „sich hastig bewegen^^, 

sp\h)ered[hy „zucken^, sp{}i)reig- „strotzen“.
```


## [2026-09-14T02:35:22.914Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY ===\"; grep -n \"سپهر\\|سپردن\\|اسفناج\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== AFM ===\"; grep -n \"سفناج\\|سباناخ\\|سپناخ\" AFM.txt AFM_pages.txt AFM_alt.txt 2>/dev/null | head -10; echo \"=== FVQ ===\"; grep -n -i \"spinach\\|isfanakh\" FVQ.txt | head -5"
}
```


### [2026-09-14T02:35:23.008Z] TOOL RESULT

```
=== ARY ===
10023:۰ | سپاردن» اسپاردن» سپردن
10111:سپهر | ۳۴۳
=== AFM ===
=== FVQ ===
```


## [2026-09-14T02:35:27.389Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10010,10035p' incoming/ARY/ARY_pages.txt; echo \"...\"; sed -n '10100,10125p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T02:35:27.458Z] TOOL RESULT

```
اوستایی (4۲574۸): ۸۸۰ ,۸8522 3۸
پهلوی (بابلهه): 5۸ ساکونی کهن 54000۷0 ۰:00 5831۸8۷
ی با کردی (130/5): 4 باه فریزی گهن (/(۴۴/514 0ا0): 51۸
1۹ " بلرچی (اپل الم , 6 ,ل52 آلمانی کهن (08741۸0 107 01):
افغانی (پشتو) رس 81۷1۸۱۷ ۸رد
تخاری 8 (8 70827۸4۸): 30 آنمانی (08821۸۷): لد انا ان
سانسکربت (8/5877): ی انگلیی کهن (2(/050 ۰:0۵ 8213۸۷
یرنانی 078570): 541 انگلیسی (57/ا8/0): الا ادن
لاتین (712ها): 5۳1۸ دانمارکی (0۸/[574): لول رن
گریکه (00777/0): ادن سوئدی (817570150): 5.۸
ایسلندی کهن (504010704۵7 0ا0): نروژی (/0/0050140: لاهن
[pdf page 339]
اا ‏ اااااا ‏ )گگ گگ 1
۰ | سپاردن» اسپاردن» سپردن
هلندی (7ل[ع0077)+ ول ۱۸ ان
اسلاوی کهن (ع#1ما؟ 0710767 صا0): پسگشت‌ها کید دا
52 9918 1 و 2۵08۵0
لهستانی 10/870 لد 0 00018880 و
روسی (/4۸ا۸(85). داد :2/۸052
چکه (لل280)): 570 2 (00190فتا8 ,5(۸2)
صربی (8878140): در 6243 82
بوهمی (8071611۸2): لران 50۵1۸ :۸03 ۸ ۸/702
لتونی (لتی) (/(477/14): 58785 ,583۸ برهان قاطع : . ۱.۷۹
آلبانی (/(۸ا/(مقلام: 5 5[
یادداشت: ۱
۱ واژه‌های انگلیسی 8 و 817۸0017 و آلمانی 5211۸7788 از بکه واجریشه‌ی نزدیکه به ابن
...
فرانسه‌ی کهن (ت۸/0ق۴۷ صا0): ۰ 858120 9 (76ه8) :قعتمالما02
انگلیسی کهن (5۸/0/54 010)(از فراسه کهن) 4 (128) :۸۸۲2/28
لد رن 5 (8128) :0/102/5
انگلیسی (62/0/3/0): نداد 8 ون 9 (5۳158) و
اسلاوی کهن (عالابماد #64نابل) صا0): فرهنگ معین + ۱۳۴
۸ لفت نامه دهخدا: ۱۳۳۳۳(
| جواگلسی سوازی از ۱0۷۷
اوستایی (ل487۵): پهلوی (1هال۸ه): انا ان بان
۸۷۸7 ,5۳۸۷۸31 5753۸۰ گرنیک (0077/0): 181
[pdf page 342]
۹
سپهر | ۳۴۳
ا
انگلیسی کهن (نْعلا8۸/0 ۰:02 بآ8ت8 8 97307۸
اسلاوی کهن (7۴بما؟ لام طا0):
زا لد این پسگشت‌ها ازش هت دای
لهستانی (نلقداهه): 5 0 ۶0/0520
, چکه (لع285ح): 5۸737 8 (8۸3) :02۵
۱ اسلوا کی (8101/7): ۵ 8 (03013) اد
لیتوانی (142 هلان[ 7ل): ک 2 6 (101) ۸2
۱ لدرنی (لتی) (/(/47۲): 50578 ,501081 لغت‌نامه دهخدا : ۷ و ۲۰۷۴
پروسی کهن ۶۸۹5۵۸7 ۵ا0).
پارسی پاستان (228۵1۵49 0ا0): 9۳118۸ پرتغالی (۳077010852): 3
پهلری (۳۸۶۲۲): ۰ 1188178 ,571118
سانسکریت (54(/8577): )2 پسگشت‌ها شک دا
بونانی 0788/0): 571۸۸ 9 ۶005908
```


## [2026-09-14T02:35:39.584Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk '/\\[pdf page 342\\]/,/\\[pdf page 344\\]/' incoming/ARY/ARY_pages.txt | head -70"
}
```


### [2026-09-14T02:35:40.592Z] TOOL RESULT

```
[pdf page 342]
۹
سپهر | ۳۴۳
ا
انگلیسی کهن (نْعلا8۸/0 ۰:02 بآ8ت8 8 97307۸
اسلاوی کهن (7۴بما؟ لام طا0):
زا لد این پسگشت‌ها ازش هت دای
لهستانی (نلقداهه): 5 0 ۶0/0520
, چکه (لع285ح): 5۸737 8 (8۸3) :02۵
۱ اسلوا کی (8101/7): ۵ 8 (03013) اد
لیتوانی (142 هلان[ 7ل): ک 2 6 (101) ۸2
۱ لدرنی (لتی) (/(/47۲): 50578 ,501081 لغت‌نامه دهخدا : ۷ و ۲۰۷۴
پروسی کهن ۶۸۹5۵۸7 ۵ا0).
پارسی پاستان (228۵1۵49 0ا0): 9۳118۸ پرتغالی (۳077010852): 3
پهلری (۳۸۶۲۲): ۰ 1188178 ,571118
سانسکریت (54(/8577): )2 پسگشت‌ها شک دا
بونانی 0788/0): 571۸۸ 9 ۶005908
لاتین (47100): 521۸2۸ ,5۳38 6 (5217882) نمی ده ی نا
فرانسه (ل۳87): 5۳ 5 (5711838) :002/5
اسپانبابی (52۸۷/8): ۸ 7 (8717838) دوه
ایتالیابی (۷ل۵ارلم7): 55۸ برهان قاطع + ۱.۹
رومانی (81014۸(0): 1 ان
بادداشت: 8 :
۱ بازگشت به: سپید.
‌ نت ۲ واژه‌های رومانس (برگرفته از لاتین) در این فهرست در آغاز چم "گوی" و "فلک" را داشتند و بعداً چم آنها
"کره‌ی سماوی نا جنرافباقی یز شد.
اوستایی (4۷587424): هد کردی (780/57): 51
پهلوی (۳۸]47): 0 ,8۳۳ بلرچی (اتلنال۸): 7 ,187۳
[pdf page 343]
۴ | ستاره

افغانی (پشتو) (/(۸۴0//۸): راون هلندی (0076): 7

سانسکریت (54(/577): اسلاوی کهن (۲7ا؟ /86نا7ا) 010):

,0715۷۳3۸ 537 ,8۷7۸ ۱ 0 : و اد

ارمنی (0ها(474415): 5۳17۸ روسی ((15314ا#): ی 9

گونیک (ع/0077): ۲7۲۷۳118 ,۷۷115175 لیتوانی (4(14(۷لا72/ل): ی

ایسلندی کهن (/(3۸01۸۸۳۸ صا۵): 71 517۷130715

17۷7811 لترنی (لتی) ((ماتمم: 171

ساکسونی کهن ((440 صا0): 17

فریزی کهن (/(۲-54 صا0): از پسگشت‌ها اد راد اد یا

آلمانی کهن ((05801۸ ۲7/0 ا0): 11۷۷12 9 ۶006

آلمانی (08۸17): 5 23 (۷3178) ی

انگلیسی کهن (8لا8۸0 ۰:02 11۷۷1۳ 0 (۷3118) :۸/۸02/278

انگلیسی (4ا8اا8(/0): لد با را زره 1054 عا8

دانمارکی (0۸07574): 110 4 1۲۳ :005

سوئدی (38013): 17 ۵ (11178) ت35

نروژی (۷نفا08۲/۴0/): 7 ,11۷10 بر هان قاطع پا ۱.۹۳

اوستایی (۸8:87۸04): یونانی (0728): 4
4 0 87۸3 این 47000 ۶185/۸ بشتا 57

پهلوی (741ل۳۸): فرانسه (ل7(ق۳۸): ۸7۵1
,578۸6 ,کلفقة857 اسپانیایی (82۸(/184): د اردا

اوستی (ع053871): 87۸41 ایتالیایی (۸4۸ )+ ش5753
```


## [2026-09-14T02:35:50.875Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"spar\\|spur\" SNS.txt | head -15; echo \"--- leaf19 ---\"; awk 'BEGIN{RS=\"\\f\"} NR==20' SNS_pages.txt | head -25"
}
```


### [2026-09-14T02:35:51.936Z] TOOL RESULT

```
2636:•O j jV- '0 j j*- : abispardan: nt" u 't>*'f 
2637:«?IrPfc.l55)sphurati: #&*** vlspara- /^par-: fc- 
2638:« >»j#-* : be abispardan : ^^o. _»n> rsphur- 
5320:-jjUiU^U^^j-iaSa^ixl C«i«3 fjl#->»: husparmm .J' 
5321:S~j I* ^jjji c,^**- 1 ** • • .usparum j asparam 
5460:p L3<J.&:5spurtg: **>•*»*» V 
10676:O i*o « J* • fdrj ' pjr : sparm 
10789:£ iUl ja A*. 1>M U o-l^l^iSLi^ljl^j JUi"-j Jtf -:spurz: £^10).a* 
10791:Uii/&.1623)'pllhan-: i ^ t5 ^» sparazan- : t- 
18624:Mitt*. 218) .o-l asparana- : Jb^hfy+vr-f 
29055:sparazan- 176/5 
29423:frasparaya- 177/7 
29863:a-sparanah- 66/2 
29864:asparana- 342/2 
31425:sparm 175/15 
--- leaf19 ---
                                            .       tfUJcu^UftiLttU                                                                                                                            --v L^c--,U»-U*jl



      \\/\6*S -T/IY^ -t-r/fiiS                            (e**.*-Ui)-an                         +   (   u I**   .
                                                                                                                    ^^           |



                                                                                                                                                                                                                                                    •rri
                                                                                                                                           •
                                                                                                                                               M-IV/T^ ham                            :L(4tl/b.           1773)sam :Lham-               :    4_ui    *   fc*,



     -ah§xt cJuaU ahania, ahan5ldan                                                 :   ^ a-hag5                        i
                                                                                                                                **•


     1Y/1Y^             r-'^l^)-isn+ (Pers. Stud. 10)
                       (,,*-.                            *-*-*'                                                                                                               ,
                                                                                                                                                                                  tf Ujbiloo=-S .          jJ^i* : hara-bun-iz                       ^HiA^
             .
                 o ^a,U.        j^n § ahanjisn  :  k«*-cv.                              :
                                                                                                                        -
```


## [2026-09-14T02:35:57.398Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('SNS.txt',encoding='utf-8',errors='replace').read()\ni=d.find('abispardan')\nprint('leaf',d[:i].count('\\f'))\nprint(repr(d[i-600:i+600]))\n\""
}
```


### [2026-09-14T02:35:58.530Z] TOOL RESULT

```
leaf 0
'»; jarasn \n\nir/v**(**£U.fn-rruo G &**»«■■*&,* ^l.c^b^^ \n\n. 1yiL : a-patQg: jj)<>o> To \nt*»*-9 \'tfrtjBli «»■•■«« «-T ^^^ JSi^ff/io j/^^jj \n^blpjc-tu-l : pattGglh/patGglh: ^js,^ o T >A/Ar \n\n\n\nla \n\n\n\nTo \n\n\n\n11 \n\n\n\nC-yll. C,U 4.L a j,lj \n\n\n\n\n\n\n\nXYVA \n\n\n\n■ YA/lo ^(^p^.23) \n.diiSj-i Ai[Lj : afsSyend: ***o>v ^ "i^lt jj^,^ \n\n\n\nr/U^ ■ c^/ <>- L • o-v*- ^ ! o*l» \n\n\n\n•>jy j* \n\n\n\n.f/VYtf oi^fc^b : ne afs\'aySnd: jk-o\'O- -^ \n\n»j\' i **J*<MOl \'^A-iJd^b : afsihSnidartar: ^^U^^^o,, \n\ntch B d a y j l^Lj bis/yat \'^^ sa5d: 4f -t-j^ J j"^W>=j\'f " \n\nawasihlnidan : ¥ (P. 7. SZ. iTjV-O "^w^£i,o^ \n\n•O j jV- \'0 j j*- : abispardan: nt" u \'t>*\'f \n«?IrPfc.l55)sphurati: #&*** vlspara- /^par-: fc- \n« >»j#-* : be abispardan : ^^o. _»n> rsphur- \n\n•a/A^-JjV- ■»*- : abispflrd: f^owf*\' \n. A-jlf-y . -"jb- : abisptSrend: axXwO****" \nawaspfirand :L {Gkilain. 75) *bysp\'r:^i \n\n«A/1V»5 .Aijb-i ng abispSrendc a^-^UAje^ji \n\n^Ai, v bS ( b., b-,1 b-) b-, 3 l : avistag/abistag: A*.ytM< \n\nawasta: L .c^ •oLy\'ot^U \n\n-y/»t ^.ywta-h-a/wJ i,-v^ m-iY-aa/Y^ 1/1 \n\nIf/11** \\~K/\\y£ \\/\\&<S .f \n• T6/W^ b-jlj-j; avistag zand: ^ 3 -"^f \n\n..uiM. r b.l, b_l : abistan/avistan: ***>* \n\n\n\n•■^"^\'••v\'jiLw\'^ljil: afzSygd: r**-*Sftr \nawazaet :{, (iHr.M'
```


## [2026-09-14T02:36:06.701Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"Etymology\" -A14 5ef0b5896b47da05.txt | sed -n '20,90p'"
}
```


### [2026-09-14T02:36:06.762Z] TOOL RESULT

```
81-
82- 1.2.2.1 
83- Conjugation 
84-
85- 1.2.2.2 
86- Derived terms 
87-
88- 1.2.2.3 
--
162: Etymology 1
163- [ edit ] 
164-
165- From Middle Persian [script needed] ( spūrdan, spar- /⁠spwltn', spl-⁠/ , “ to tread , trample ” ) [ 1 ] 
166-
167: This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . 
168-Particularly: “Feels like this might be from Proto-Indo-European *sperH- ( “ to kick ” ) . See also Prakrit 𑀨𑀺𑀭𑀇 ( phiraï , “ to turn, travel ” ) .”
169-
170- Verb
171- [ edit ] 
172-
173- سپردن • ( separdan ) ( present stem سپار ( sepâr ) or سپر ( separ ) ) 
174-
175- ( archaic ) to traverse , to pass 
176-
177- ( archaic ) to tread , to trample 
178-
179- Conjugation
180- [ edit ] 
181-
--
585: Etymology 2
586- [ edit ] 
587-
588- From Middle Persian [script needed] ( abespurdan, abespār- /⁠ʾp̄spwltn', 'p̄sp'l-⁠/ , “ to commit , entrust , consign ” ) , [ 2 ] from Proto-Iranian *upa- + *spar ( “ to hand over, entrust ” ) , which according to Cheung is from Proto-Indo-European *sper- ( “ to deliver, secure ” ) , though the cognates he gives, from Proto-Germanic *sparāną ( “ to be thrifty ” ) , are thought to derive from Proto-Indo-European *speh₁- ( “ to succeed, prosper ” ) instead. [ 3 ] 
589-
590- Pronunciation
591- [ edit ] 
592-
593- IPA ( key ) : [sepʰoɾˈd̪æn] 
594-
595- Verb
596- [ edit ] 
597-
598- سپردن • ( sepordan ) ( present stem سپار ( sepâr ) or سپر ( sepor ) ) 
599-
```


## [2026-09-14T02:36:48.933Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg470.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/470.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/470.png; grep -n -A6 \"Etymology 1\" /home/sfmqrb/git/rishe/data/verification/sources/web/6ef2a6bb315be0a7.txt | sed -n '1,30p'"
}
```


### [2026-09-14T02:36:49.032Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75634 Sep 13 22:36 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/470.png
65: Etymology 1 
66-
67- 1.2.1 
68- Verb 
69-
70- 1.2.1.1 
71- Usage notes 
--
194: Etymology 1 
195-
196- 7.1.1 
197- Noun 
198-
199- 7.2 
200- Etymology 2 
--
467: Etymology 1
468- [ edit ] 
469-
470- From Middle English springen , from Old English springan ( “ to spring, leap, bounce, sprout forth, emerge, spread out ” ) , from Proto-West Germanic *springan , from Proto-Germanic *springaną ( “ to burst forth ” ) , from Proto-Indo-European *spre(n)ǵʰ- ( “ to move, race, spring ” ) , from *sperǵʰ- ( “ to hurry ” ) .
471-
472- Cognates
473-
--
2779: Etymology 1
2780- [ edit ] 
2781-
2782- Noun
2783- [ edit ] 
2784-
```


## [2026-09-14T02:38:32.863Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:56:10.302Z] TOOL CALL #66: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-470.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nE = \"https://www.etymonline.com/word/\"\n\nout = {\n \"pdf_page\": 470,\n \"book_page\": 440,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------- entry 0: Spher ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Spher\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *sp(h)er- / *sperH- 'to jerk, kick out with the foot, move rapidly' (Pokorny 992-993, lemma sp(h)er-1); the 'ankle' sense comes from Gk. sphyrón, the 'spread' sense from the adjacent lemma (s)p(h)er-2 'to sprinkle, scatter' (Pok. 993-995)\",\n \"note\": \"The root is real and POK:992 is the right page, but the gloss merges two of Pokorny's lemmas. Pokorny 992-993 sp(h)er-1 = 'eine rasche Bewegung machen, wegstossen' (Skt. sphurati, Av. spar-, Gk. spairo, Lat. sperno, ON sperna, Lith. spirti); the 'ankle' meaning is carried by Gk. sphyron and OIr. seir, which is why Watkins' AHD appendix glosses the root simply 'spere-. Ankle. [Pok. 1. sp(h)er- 992]'. 'Spread/scatter' belongs to Pokorny's next lemma (s)p(h)er-2 (993-995), which Pokorny himself calls 'probably identical' with sp(h)er-1 and which Watkins keeps separate as spere- 'to strew'. LIV further splits the family into *sperH- 'to kick' (585f.) and *sper- 'to deliver, secure' (579) - a distinction that matters for node #2 below. Cross-cutting problem of this chart: Nourai runs three originally distinct things (the kick-root, the 'entrust' root, and the nasalized *sprengh- of 'spring') into one box, and hangs the Greek 'ball' word on it as well.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sp(h)er- «با پا زدن، جستن، حرکت تند کردن» (پوکورنی، صص ۹۹۲–۹۹۳) واقعی است و ارجاع نورایی به صفحهٔ ۹۹۲ درست است؛ اما معنایی که او می‌دهد دو مدخل جداگانهٔ پوکورنی را در هم آمیخته: معنی «قوزک پا» از یونانی sphyrón و ایرلندی کهن seir می‌آید (واتکینز در پیوست AHD همین را تنها معنیِ ریشه می‌داند) و معنی «پراکندن/گستردن» به مدخل بعدی (s)p(h)er-2 «افشاندن» (صص ۹۹۳–۹۹۵) تعلق دارد، هرچند خود پوکورنی این دو را «احتمالاً یکی» می‌شمارد. فرهنگ LIV نیز *sperH- «لگد زدن» را از *sper- «سپردن، واگذاشتن» جدا می‌کند. پس ادعای نورایی دربارهٔ خودِ ریشه با احتیاط پذیرفتنی است، ولی سه خانوادهٔ جدا (ریشهٔ «لگد زدن»، ریشهٔ «سپردن»، و *sprengh- انگلیسی spring) در یک جعبه ادغام شده‌اند.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/sperH-\", E+\"sphere\"],\n \"ref_check\": [\n   {\"ref\": \"POK:992\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt, 'Root / lemma: sp(h)er-1, sp(h)era-', Page(s): 992-993: 'Meaning: to make a rash movement, to push away, to rush' ... 'Avestan spar(aiti) \\\"tritt, stoesst\\\" ... np. sipardan \\\"tread\\\"' ... 'aspiriert sphyron \\\"ankle, calcaneus\\\"'. The page number is exact; the 'spread' half of Nourai's gloss belongs to the following lemma (s)p(h)er-2 'to sprinkle, scatter', Page(s) 993-995.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 992-993, lemma sp(h)er-1\", \"stance\": \"partial\",\n    \"note\": \"grep -n 'lemma: sp(h)er-1' POK_full.txt -> line 80093; 'to make a rash movement, to push away, to rush'; sphyron 'ankle' is inside this lemma, but 'spread' is the next lemma (993-995).\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 668ff., '1. sp(h)er-'\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd2_1927_dli_106624_djvu.txt line ~43420: '1, sp(h)er- \\\"zucken, mit dem Fusse ausschlagen, zappeln, schnellen\\\" (im Anlaut wechselt sp- und sph-, s. Persson Beitr. 417)' - explicitly sanctions the sp-/sph- doublet of Nourai's root name.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. spere- and spere-\", \"stance\": \"partial\",\n    \"note\": \"AHD_watkins1985.txt: 'spere-. Ankle. ... [Pok. 1. sp(h)er- 992.]' (derivatives SPUR, SPURN, SPOOR) and a separate 'spere-' ... 'Greek speirein, to scatter ... [Pok. 2. (s)p(h)er- 993.]'. Watkins keeps 'ankle' and 'strew' apart; Nourai merges them.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. spri, io (sphra, ie) 'ball'\", \"stance\": \"partial\",\n    \"note\": \"IEC.txt line 16952: 'Spri, io (sphra, ie) \\\"ball\\\" WP II, 672 Gk. sphaira, f. id.; ... (For OE spure \\\"heel\\\", see sphur- in view of Gk. sphuron \\\"ankle\\\")' - Mann does attach both sphaira and the 'ankle/heel' words to this family.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"spar; apa-spar; us-spar\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Young Avestan spar- 'to kick, tread, trample' is real: Bartholomae, AiW col. 1613, 'j. spar- V. \\\"schnellen, treten\\\"', with only two attested preverbs - fra- (fras ayanho frasparat, Y 9.11 'he shot forward from under the kettle') and vi- (vispara, V 2.31 'trample apart'); Bartholomae himself glosses 'ai. sphurati, np. sipardan'. Cheung 2007: 352 sets up Proto-Iranian *sparH 'to tread, kick' (< PIE *sperH-, LIV 585f.), with MP spar-/spurdan and NP sipardan. So 'spar : to walk' is right in substance (better 'tread, kick' than 'walk'). The two compounds Nourai adds are NOT attested Avestan words: neither apa-spar- nor us-spar- appears in Bartholomae. 'us-spar' comes from Horn, Grundriss p.154 no.697, where Horn analyses NP supurden 'anvertrauen, uebergeben' as 'aw. us- + 2. par-' (i.e. the root 'to carry across', cf. Lat. portare) - a de Lagarde conjecture Horn himself calls 'sehr unsicher', and not a form of spar-. The real ancestor of the 'entrust' sense is Middle Persian abespurdan/abespardan < Proto-Iranian *upa-spar-, which Cheung 2007: 351 keeps as a separate root *spar 'to hand over, entrust'. The glosses are also crossed: apa- is 'away' and us- is 'up/out', yet Nourai glosses apa-spar 'walk up to' and us-spar 'walk away'.\",\n \"derivation_fa\": \"فعل اوستایی spar- «لگد زدن، پای کوفتن، پایمال کردن» واقعی است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۱۶۱۳) آن را «schnellen, treten» معنی می‌کند و تنها دو پیشوند برای آن گواه دارد: fra- (frasparat در یسنا ۹٫۱۱) و vi- (vīspara در وندیداد ۲٫۳۱)؛ خود او هم‌ریشه‌های سنسکریت sphuráti و فارسی نو «سپردن» را می‌آورد. چونگ (۲۰۰۷، ص ۳۵۲) ستاک ایرانی آغازین *sparH «پای کوفتن» را از هندواروپایی *sperH- بازسازی می‌کند که از راه فارسی میانهٔ spar-/spurdan به «سپردن» رسیده است. اما دو ترکیبِ apa-spar و us-spar در اوستا گواه ندارند و در بارتولومه نیست؛ «us-spar» برگرفته از تحلیل کهنهٔ هرن (ص ۱۵۴، شمارهٔ ۶۹۷) است که «سپردن» را us- + ریشهٔ par- «گذراندن» (هم‌ریشه با لاتینی portāre) می‌دانست و خودش آن را «بسیار نامطمئن» خوانده بود. سرچشمهٔ معنی «سپردن/امانت دادن» در واقع فارسی میانهٔ abespurdan از *upa-spar- ایرانی است. افزون بر این، معانی جابه‌جا شده‌اند: apa- یعنی «دور» و us- یعنی «بالا/بیرون»، ولی نورایی برعکس معنی کرده است. حکم: با احتیاط پذیرفتنی، با اصلاح دو ترکیب.\",\n \"sources\": [W+\"Reconstruction:Proto-Iranian/sparH-\", W+\"%D8%B3%D9%BE%D8%B1%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:992\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt lemma sp(h)er-1 (pp.992-993): 'Avestan spar(aiti) \\\"tritt, stoesst\\\", with fra- \\\"rushes, hastes\\\", with vi- \\\"auseinandertreten, -stampfen\\\" ... np. sipardan \\\"tread\\\"'. Exactly the Avestan verb Nourai draws, but with fra-/vi-, not apa-/us-.\"},\n   {\"ref\": \"BQT:1086\", \"status\": \"partial\",\n    \"note\": \"Borhan-e Qate' vol.2, section 'bayan-e sevvom' (sin + pe), scan leaf 548 (printed p. ~1090-1091; Nourai's 1086 is a few pages early), s.v. سپاردن: Mo'in's footnote reads 'سپاردن - بکسر اول و فتح پنجم مخفف اسپاردن؛ پهلوی avspartan [رك: سپردن] و avspurtan؛ قی: ارمنی aps-par-em (تسلیم کردم، واگذار کردم) از spar ریشهٔ ایرانی ... افغانی sparal (تسلیم کردن)، کردی sipartin'. Mo'in gives the Iranian root spar and the Pahlavi av-/abe- prefix, but no Avestan apa-spar.\"},\n   {\"ref\": \"HRN:154\", \"status\": \"partial\",\n    \"note\": \"HRN.txt leaf 176 = printed p.154, no. 697: 'supaerden \\\"anvertrauen, uebergeben\\\" ... aw. us- + 2. par-; phlv. avspaertan, avspurtan (vd. 5), spurtitan (AV.); ai. ud + par- \\\"hinueberfuehren\\\" ... vergl. lat. portare. Die Etymologie stammt von de Lagarde, ist aber sehr unsicher.' Horn does write us- + par-, so the citation is faithful; but his root is par- 'to carry across', not spar-, and he flags the whole thing as very uncertain.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1613 s.v. spar-\", \"stance\": \"partial\",\n    \"note\": \"BRT.txt line 26841ff.: 'j. spar- V. \\\"schnellen, treten\\\". Praes. 3: 1) \\\"treten, stossen\\\" ... mit fra- \\\"hervorschnellen\\\" ... mit vi- \\\"auseinandertreten, -stampfen\\\" ... ai. sphurati, np. sipardan'. No apa-spar-, no us-spar- anywhere in the entry.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"pp. 351-352, *spar and *sparH\", \"stance\": \"partial\",\n    \"note\": \"CHEUNG.txt: '*sparH \\\"to tread, kick\\\": YAv. spar- ... (+ *fra-) ... (+ *ui-) ... BMP spl- /spar-/ ... NP sipardan/sipar- \\\"to trample\\\" ... PIE *sperH- (LIV 585f. | Pok. 992f.)' and separately '*spar \\\"to hand over, entrust\\\": (+ *upa-) BMP abespar- ... NP sipar-/sipurdan ... PIE *sper- \\\"to deliver, secure\\\" (LIV 579 | Pok. 992)'. Two roots, not one.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. spurdan, ospurdan, wispurdan, abespurdan\", \"stance\": \"supports\",\n    \"note\": \"PHD.txt: 'spurdan, spar- [spwltn, spl- | N sip~] tread, trample'; 'ospurdan, ospar- tread, trample'; 'wispurdan, *wispar- tread, trample'; 'abespurdan, abespar- [ʾpsʼpwltnʼ | M ʾbyspwrd, ʾbyspʼr-, N sipurdan, sipar-] commit, entrust, consign'. The MP continuations of the Avestan verb are exactly as drawn.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.v. spurtan and api-spartan\", \"stance\": \"supports\",\n    \"note\": \"NYB_vol2_glossary.txt: 'spurtan [spwltn] spar-, ... to trample (to death) ... Av. (1613) spar-; NP sipurdan sipar-' and 'api-spartan [ʾpspʼltn], often with be: to hand over ... Olr *upa-spar- and apa-spar-, and then *upa- remodelled to api- ... Arm. lw. apspar-em ... NP only simplex supurdan sipar- \\\"to entrust\\\"'. Nyberg is the one source that does mention an Old Iranian *apa-spar-, which is probably where Nourai's 'apa-spar' comes from - but as a reconstructed Old Iranian preverb, not an attested Avestan word.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"sepârdan; separî\",\n \"verdict\": \"plausible\",\n \"derivation\": \"NP سپردن covers two verbs that fell together. (a) separdan / separdan 'to tread, traverse, pass over' < MP spurdan, spar- 'tread, trample' (MacKenzie) < Av. spar-: the phonetic route is Av. spar- > MP spar-/spurd- (with the regular -rd- past stem) > NP sipar-/sipurd-, the infinitive sipardan being, as Huebschmann says (Persische Studien 697), 'vom Praesens neu gebildet', the older infinitive being supurdan beside the present sipaeram. (b) sepordan 'to entrust, commit, consign' < MP abespurdan, abespar- [ʾpspwltn] (Man. MP ʾbyspwrd, Parth. ʾbyspʼr-) < PIr *upa-spar-; the initial abe-/av- was lost in New Persian, leaving the simplex, and Armenian borrowed the full form as apsparem. Huebschmann corrects Horn here: 'Im Phl. ist apspurtan zu lesen, vgl. arm. ap-spar-em ... Als iranische Wurzel ist spar anzusetzen.' Cheung and Wiktionary treat (a) and (b) as two roots (*sperH- vs *sper-), so Nourai's single gloss 'walk, trust' straddles a boundary modern Iranian scholarship draws. separî 'past, elapsed, spent' belongs to the same stem family: cf. MP spurrig 'entire, complete, perfect' (MacKenzie), Paz. spur, whence NP سپری 'finished, gone by' and سپری شدن 'to come to an end'; Huebschmann 703 equates np. siparî with phl. *spurik. The script_extra سپردن ۱ is simply the modern spelling of the headword.\",\n \"derivation_fa\": \"«سپردن» در فارسی نو دو فعل هم‌آواست که به هم رسیده‌اند. نخست «سپَردن» به معنی «پیمودن، پای کوفتن» از فارسی میانهٔ spurdan (ستاک حال spar-) و آن از اوستایی spar-؛ سیر آوایی: spar- اوستایی ← spar-/spurd- پهلوی (ستاک گذشته با -rd- قاعده‌مند) ← سِپَر-/سپُرد فارسی نو. هوبشمان (پژوهش‌های ایرانی، شمارهٔ ۶۹۷) یادآور می‌شود که مصدر «سپاردن» از ستاک حال ساخته شده و صورت کهن‌تر «سپردن/سُپُردن» بوده است. دوم «سپُردن» به معنی «واگذاشتن، به امانت دادن» از فارسی میانهٔ abespurdan (پارتی ʾbyspʾr-) و آن از *upa-spar- ایرانی باستان؛ پیشوند abe-/av- در فارسی نو افتاده و ارمنی آن را به صورت apsparem وام گرفته است. هوبشمان تصریح می‌کند «در پهلوی باید apspurtan خواند ... ریشهٔ ایرانی را باید spar گذاشت». چونگ و ویکی‌واژه این دو را دو ریشهٔ جداگانه می‌دانند، پس معنی یک‌جای «walk, trust» در نمودار نورایی مرز میان دو ریشه را نادیده می‌گیرد. «سپری» نیز از همین خانواده است: پهلوی spurrīg «تمام، کامل» و پازند spur، که «سپری شدن» فارسی از آن است. حکم: با احتیاط پذیرفتنی.\",\n \"sources\": [W+\"%D8%B3%D9%BE%D8%B1%D8%AF%D9%86\", \"https://abadis.ir/fatofa/%D8%B3%D9%BE%D8%B1%D8%AF%D9%86/\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1086\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' vol.2, scan leaf 548 (printed p. ~1090-1091), Mo'in's footnote to سپاردن: 'مخفف اسپاردن؛ پهلوی avspartan [رك: سپردن] و avspurtan؛ قی: ارمنی aps-par-em (تسلیم کردم، واگذار کردم) از spar ریشهٔ ایرانی ... هوبشمان ۷۹۹ ... افغانی sparal، کردی sipartin'. Exactly the Persian-from-Iranian-*spar claim of the arrow.\"},\n   {\"ref\": \"SNS:19\", \"status\": \"supports\",\n    \"note\": \"Tavoosi, Vazhe-name-ye Shayast ne Shayast, SNS.txt s.v. abispardan: 'abispardan: ابسپردن ... (IrPfc.155?) sphurati; vispara- / spar-; be abispardan; abispurd; abisparend; awasparand: L (Ghilain 75) ʾbyspʼr'. The glossary derives the Pahlavi 'entrust' verb from spar- and cites Ghilain for the Parthian. The exact printed page could not be confirmed (refs_online records that SNS page offsets are undetermined), but the entry sits at the start of the alphabetical glossary, consistent with p.19.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.vv. spurdan / abespurdan / spurrig\", \"stance\": \"supports\",\n    \"note\": \"'spurdan, spar- [spwltn, spl- | N sip~] tread, trample'; 'abespurdan, abespar- ... commit, entrust, consign'; 'spurrig [spwlyk | (M ʾspwr), N sipari] entire, complete, perfect' - the last is the base of separî.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien 697 and 703\", \"stance\": \"supports\",\n    \"note\": \"HUB.txt line 2554: '697. Im Phl. ist apspurtan zu lesen, vgl. arm. ap-spar-em \\\"uebergebe, ueberlasse, vertraue an\\\". Als iranische Wurzel ist spar anzusetzen. Der Infinitiv sipaerdan ... ist vom Praesens neu gebildet; urspruenglich steht nur der Infinitiv supurdan neben dem Praesens sipaeram.' And '703. Np. siparî = phl. *spurik' for separî.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss p.154 no. 697\", \"stance\": \"partial\",\n    \"note\": \"'supaerden \\\"anvertrauen, uebergeben\\\" ... aw. us- + 2. par- ... Die Etymologie stammt von de Lagarde, ist aber sehr unsicher.' Horn has the word and an Avestan preverb but the wrong root, and says so.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"pp. 351-352\", \"stance\": \"partial\",\n    \"note\": \"'*NWIR: NP sipar-/sipurdan' under *spar 'to hand over, entrust', and '*NWIR: NP sipardan/sipar- \\\"to trample; to be trampled\\\"' under *sparH 'to tread, kick' - the split Nourai does not make.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha, pdf pp. 339-341, s.v. سپاردن، اسپاردن، سپردن\", \"stance\": \"supports\",\n    \"note\": \"ARY_pages.txt: entry heading '| سپاردن، اسپاردن، سپردن' with Avestan SPAR, Pahlavi SPURTAN, Sanskrit SPHUR, Latin SPERNO, Gothic/OE SPURNAN, English SPURN, German SPORN, with a note that English SPRING/SPRINGE and German SPRINGEN come from a closely related root; he cites 'برهان قاطع ۱۰۹۱' - which incidentally confirms the BQT page for سپاردن is ~1091, not 1086.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Greek\", \"words\": \"spairen; sphaira\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two words, two fates. (a) spairein (sigma-pi: spairo, aspairo) 'to gasp, struggle, twitch, writhe' is securely from this root: Pokorny 992 lists 'gr. spairo, aspairo (a- vowel prothesis) \\\"twitch, wriggle\\\" (= Lith. spiriu)', and Klein s.v. Sphyraena gives 'sphyra \\\"hammer\\\", which is rel. to sphyron \\\"ankle\\\", spairein \\\"to move convulsively\\\", from I.-E. base *(s)p(h)er-, \\\"to move convulsively\\\"'. Nourai's gloss 'to walk in a bouncing manner' is loose but not wrong in spirit. (b) sphaira 'ball' (phi) is where the chart over-reaches. Pokorny mentions it only parenthetically and with a query - '(aspiriert sphaira \\\"Ball zum Spielen\\\"?)' - because the aspiration sp- > sph- is unexplained. Watkins' AHD appendix assigns no Indo-European root to SPHERE at all (its index lists SPHERE only inside the compounds ARMILLARY SPHERE, BARYSPHERE, ATMOSPHERE). Beekes, followed by Etymonline, calls sphaira 'a word of unknown origin' with 'no certain cognates outside Greek'. Wiktionary: 'Connections with spairo or PIE *sperH- have been suggested, but the aspiration of sp- to sph- is unexplained and the semantic development is dubious'; Nikolayev instead proposes Proto-Hellenic *skwhərra < PIE *sgwher- 'to be round' (cf. Av. zgərəsna- 'round'). Because the whole right-hand half of this chart (French, English, Pahlavi, Persian) hangs on sphaira, the verdict for the node is the worse of the two.\",\n \"derivation_fa\": \"این جعبه دو واژه دارد که سرنوشتشان یکی نیست. نخست σπαίρω/ἀσπαίρω «تکان خوردن، به خود پیچیدن» که به‌روشنی از همین ریشه است؛ پوکورنی (ص ۹۹۲) آن را برابر spiriù لیتوانیایی می‌گذارد و کلاین نیز σπαίρειν را به ریشهٔ *(s)p(h)er- می‌بندد. معنایی که نورایی می‌دهد («راه رفتن جهشی») تقریبی است اما بی‌راه نیست. دوم σφαῖρα «گوی، توپ» که مشکل‌ساز است: پوکورنی آن را تنها در پرانتز و با علامت پرسش می‌آورد، زیرا تبدیل σπ- به σφ- توجیه آوایی ندارد؛ واتکینز در پیوست ریشه‌های هندواروپاییِ AHD هیچ ریشه‌ای برای sphere نمی‌آورد؛ بیکس و اتیمولوژی‌آنلاین آن را «واژه‌ای با خاستگاه ناشناخته و بدون هم‌ریشهٔ مطمئن بیرون از یونانی» می‌خوانند؛ و ویکی‌واژه پیشنهاد نیکولایف را نقل می‌کند که آن را از *sgʷʰer- «گرد بودن» (قس اوستایی zgərəsna- «گرد») می‌گیرد. چون همهٔ شاخهٔ راستِ این نمودار بر σφαῖρα استوار است، حکم گره همان حکم بدتر است: پژوهش امروزی این پیوند را رد می‌کند.\",\n \"sources\": [W+\"%CF%83%CF%86%CE%B1%E1%BF%96%CF%81%CE%B1\", E+\"sphere\"],\n \"ref_check\": [\n   {\"ref\": \"POK:992\", \"status\": \"partial\",\n    \"note\": \"POK_full.txt, lemma sp(h)er-1 (992-993): 'gr. spairo, aspairo (a- vowel suggestion) \\\"twitch, wriggle\\\" (= Lithuanian spiriu) ... (aspiriert sphaira \\\"Ball zum Spielen\\\"?)'. Pokorny supports spairein outright but puts sphaira in parentheses with a question mark.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 992-993\", \"stance\": \"partial\",\n    \"note\": \"See ref_check: spairo yes, sphaira '?'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. spere-\", \"stance\": \"contradicts\",\n    \"note\": \"grep of AHD_watkins1985.txt gives only 'SPHERE al-', 'SPHERE gWere-2', 'SPHERE wet-' - i.e. the word SPHERE appears in the index solely as part of ARMILLARY SPHERE, BARYSPHERE and ATMOSPHERE. Watkins gives Greek sphaira no Indo-European root, and does not list it under spere- 'Ankle'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966, p.1489 s.v. Sphyraena\", \"stance\": \"supports\",\n    \"note\": \"'Gk. sphyraina, \\\"hammer fish\\\", fr. sphyra, \\\"hammer\\\", which is rel. to sphyron, \\\"ankle\\\", spairein, \\\"to move convulsively\\\", from I.-E. base *(s)p(h)er-, \\\"to move convulsively\\\". See spurn' - Klein does connect the sph- words with the root, though under sphere itself he says only 'Gk. sphaira'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. spri, io (sphra, ie) 'ball'\", \"stance\": \"supports\",\n    \"note\": \"IEC.txt line 16952: 'Spri, io (sphra, ie) \\\"ball\\\" WP II, 672 Gk. sphaira, f. id.; OE (?) spure, f. \\\"heel\\\"; Li. spiras \\\"little ball, pellet\\\"'. Mann is one of the few modern comparatists who still derives sphaira from this base.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 668ff.\", \"stance\": \"silent\",\n    \"note\": \"The '1. sp(h)er- \\\"zucken...\\\"' entry notes the sp-/sph- alternation in the anlaut (Persson Beitr. 417) but the local OCR of Bd. II does not show sphaira being adduced there.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"An empty pass-through box standing for French sphere / atmosphere. The uncontroversial part of the chain is Greek sphaira > Latin sphaera 'globe, ball, celestial sphere' (Medieval Latin spera) > Old French espere (13c.), Modern French sphere; atmosphere is not inherited but coined in Modern Latin as atmosphaera in the 1630s (Greek atmos 'vapour' + sphaira) and taken into French as atmosphere. Since it carries no words and no refs, the box can only be judged on the chain it implies, which is correct as far as the French side goes; what it cannot bear is the weight of the Greek etymology above it (node #3).\",\n \"derivation_fa\": \"این جعبه تهی و صرفاً حلقهٔ واسط است و نمایندهٔ واژه‌های فرانسوی sphère و atmosphère. زنجیرهٔ بی‌مناقشه چنین است: یونانی σφαῖρα ← لاتینی sphaera «گوی، فلک» (لاتینی میانه spera) ← فرانسهٔ کهن espere (سدهٔ سیزدهم) ← فرانسهٔ نو sphère. اما atmosphère واژه‌ای موروثی نیست، بلکه در دههٔ ۱۶۳۰ در لاتینِ نو به صورت atmosphaera از ἀτμός «بخار» و σφαῖρα ساخته شد و از آنجا به فرانسه رفت. چون این جعبه نه واژه‌ای دارد و نه ارجاعی، تنها بر پایهٔ همین زنجیره می‌توان داوری کرد و در آن حد درست است؛ ضعف آن از جعبهٔ یونانی بالادست می‌آید. حکم: با احتیاط پذیرفتنی.\",\n \"sources\": [E+\"sphere\", E+\"atmosphere\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference of its own in the book.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966, p.1489 s.vv. sphere, spherical, spheroid\", \"stance\": \"supports\",\n    \"note\": \"Klein's sphere family runs consistently 'Late L. sphaericus, fr. Gk. sphairikos, fr. sphaira' and 'Late L. sphaerula, dimin. of L. sphaera, fr. Gk. sphaira' - the Greek > Latin > Romance chain the empty French box stands for.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. sphere (archived)\", \"stance\": \"supports\",\n    \"note\": \"'a re-Latinized spelling ... of Middle English spere (c. 1300) ... from Anglo-French espiere, Old French espere (13c., Modern French sphere), from Latin sphaera ... from Greek sphaira'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"âtmosfer\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"آتمسفر (also اتمسفر) is a modern European loan in Persian, taken from French atmosphere in the late Qajar / early Pahlavi scientific vocabulary, alongside the Arabic جوّ and the modern calque هواسپهر. Mo'in's dictionary tags the entry '[فر.]' - i.e. French - and glosses it 'تودهٔ هوایی که اطراف کرهٔ زمین را فرا گرفته، جو' plus the figurative 'کنایه از اوضاع و احوال'. The Persian spelling with آ reflects French [a] in an open initial syllable; the -سفر renders -sphere with س for the French [s] and ف for [f], since Persian has no /θ/ or Greek phi. Nourai's gloss 'sphere of vapor' correctly unpacks the Modern Latin compound (Greek atmos 'vapour, steam' + sphaira), which was coined in 1630s Neo-Latin as atmosphaera.\",\n \"derivation_fa\": \"«آتمسفر» (و صورت «اتمسفر») وام‌واژه‌ای اروپایی در فارسی است که در واژگان علمیِ اواخر قاجار و اوایل پهلوی از فرانسهٔ atmosphère گرفته شد، در کنار «جوّ» عربی و گَردهٔ فارسی «هواسپهر». فرهنگ معین این مدخل را با نشانِ «[فر.]» یعنی فرانسوی می‌آورد و چنین معنی می‌کند: «تودهٔ هوایی که اطراف کرهٔ زمین را فرا گرفته، جو» و نیز «کنایه از اوضاع و احوال». نگارش «آ» در آغاز، بازتاب مصوت باز فرانسوی است و «سفر» پایانی برابرنهادِ ‎-sphère است، زیرا فارسی واجِ یونانیِ φ ندارد. معنی‌ای که نورایی می‌دهد («کرهٔ بخار») ترکیب لاتینِ نو را درست می‌گشاید: ἀτμός «بخار» + σφαῖρα، که در دههٔ ۱۶۳۰ به صورت atmosphaera ساخته شد. حکم: ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D8%A2%D8%AA%D9%85%D8%B3%D9%81%D8%B1/\", E+\"atmosphere\"],\n \"ref_check\": [\n   {\"ref\": \"MON:32\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi, s.v. آتمسفر, read via abadis.ir (the print page numbers are not mapped online): 'فرهنگ معین: (آتمسفر) (مُ فِ) [ فر. ] (اِ.) ۱- تودة هوایی که اطراف کرة زمین را فرا گرفته، جو. ۲- کنایه از: اوضاع و احوال.' The tag [فر.] = French is exactly the arrow Nourai draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. آتمسفر (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"'[ فر. ]' origin tag; see ref_check.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. atmosphere (archived)\", \"stance\": \"supports\",\n    \"note\": \"'1630s, atmosphaera (modern form from 1670s) ... from Modern Latin atmosphaera, from Greek atmos \\\"vapor, steam\\\" + sphaira \\\"sphere\\\"' - confirms the 'sphere of vapor' gloss.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"sphere; atmosphere\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both English words exist and both ultimately contain Greek sphaira, but neither came into English through Modern French as the arrow implies. SPHERE: Middle English spere (c.1300) 'cosmos, hollow globe about the world' from Anglo-French espiere / Old French espere (13c.), from Latin sphaera (ML spera); the spelling was re-Latinized to sphere from the mid-15c. So the donor is Anglo-Norman/Old French, three centuries before Modern French sphere existed. ATMOSPHERE: first attested in English in the 1630s as atmosphaera, from Modern Latin atmosphaera - a learned coinage (associated with Willebrord Snel's circle) - with the modern form from the 1670s; it is not a French loan. Nourai cites AHD, but Watkins' appendix files ATMOSPHERE under wet-1 (for Greek atmos) and gives sphere no root at all, so 'AHD' does not actually license the box as drawn.\",\n \"derivation_fa\": \"هر دو واژهٔ انگلیسی واقعی‌اند و هر دو در نهایت σφαῖρα یونانی را در خود دارند، اما هیچ‌یک آن‌گونه که پیکان نمودار می‌گوید از راه فرانسهٔ نو وارد انگلیسی نشده‌اند. sphere: انگلیسی میانه spere (حدود ۱۳۰۰ م.) به معنی «فلک، گنبد تهی گرداگرد زمین» از انگلونرمن espiere / فرانسهٔ کهن espere (سدهٔ سیزدهم) و آن از لاتینی sphaera؛ املای امروزی از میانهٔ سدهٔ پانزدهم دوباره لاتینی‌مآب شد. پس وام‌دهنده فرانسهٔ کهن است، سه سده پیش از آنکه sphère فرانسهٔ نو پدید آید. atmosphere: نخستین کاربرد انگلیسی در دههٔ ۱۶۳۰ به صورت atmosphaera، مستقیماً از لاتینِ نو و نه از فرانسه. افزون بر این، ارجاع نورایی به AHD این جعبه را تأیید نمی‌کند: واتکینز ATMOSPHERE را ذیل ریشهٔ wet-1 (به سبب ἀτμός) می‌آورد و برای sphere هیچ ریشهٔ هندواروپایی قائل نیست. حکم: با احتیاط پذیرفتنی، با اصلاح مسیر وام‌گیری.\",\n \"sources\": [E+\"sphere\", E+\"atmosphere\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"AHD_watkins1985.txt s.v. wet-1: '4. Oldest basic form *awet- becoming *awet- in suffixed form *awet-mo- in Greek atmos (< *aetmos), breath, vapor: ATMOSPHERE. [Pok. udē- 1113.]' - Watkins assigns ATMOSPHERE to the atmos half only, and the index shows no root entry for SPHERE. So AHD supports the existence of the words but not the French-to-English arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966, p.1489, sphere family\", \"stance\": \"supports\",\n    \"note\": \"Klein derives the whole sphere family from Gk. sphaira through Latin sphaera / Late L. sphaericus, sphaerula.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.vv. sphere, atmosphere (archived)\", \"stance\": \"partial\",\n    \"note\": \"sphere 'from Anglo-French espiere, Old French espere (13c., Modern French sphere), from Latin sphaera'; atmosphere '1630s, atmosphaera ... from Modern Latin atmosphaera' - i.e. Old French and Modern Latin, not Modern French.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 index\", \"stance\": \"partial\",\n    \"note\": \"'ATMOSPHERE wet-' in the index; no SPHERE headword.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Pahlavi\", \"words\": \"spihr\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Middle Persian word is real: MacKenzie 1971 'spihr [spy(y)hl | (M ʾspyr), N sipihr] sphere, sky, firmament, fate', with the adjective spihrig 'heavenly'. Its origin, however, is one of the classic unsettled questions of Iranian etymology, and the modern reference works do not take Nourai's side. (i) Henning (List 81; JRAS 1942, 239ff.) identified spihr with the Manichaean Middle Persian and Parthian form ʾspyr (esper), which he took to be a borrowing of Greek sphaira - the same Greek word being demonstrably borrowed into Syriac espera, Armenian spʿer, Georgian spero and Ethiopic spir (Beekes/Etymonline list exactly these). (ii) Against this, Nyberg, Manual of Pahlavi II s.v. spihr: 'I maintain the old etymology: OIr *spiθra- (Skr svitra-) \\\"brightly shimmering\\\" and then \\\"heaven\\\" (cf. n. pr. Spithridates). Henning identifies it with MPrth/MPrs ʾspyr (= esper) which according to him is borrowed from Gr. sphaira. However, in this case -h- in spihr would be an inorganic insertion, which is quite improbable. Of course, the sense of spihr may have been influenced by sphaira, but its formal independence is proved by NP sipihr which belongs to the living language.' Huebschmann 707, following Noeldeke, says the same, adducing the Achaemenid name Spithridates/Spithradates recorded by Ctesias, Xenophon and Arrian as direct evidence for an Old Iranian *spiθra-. Wiktionary follows this line. The honest reading is therefore: -h- in spihr is the obstacle, Man. MP ʾspyr is a genuine Greek loan but probably a separate word, and Nourai's single arrow Greek > Pahlavi states as fact what is a live dispute in which the majority of handbooks are on the other side.\",\n \"derivation_fa\": \"واژهٔ فارسی میانه واقعی است: مکنزی (۱۹۷۱) می‌آورد «spihr: فلک، آسمان، سپهر، بخت» و صفتِ spihrīg «آسمانی». اما خاستگاه آن از پرسش‌های حل‌نشدهٔ ریشه‌شناسی ایرانی است و مرجع‌های امروزی جانب نورایی را نمی‌گیرند. هنینگ (JRAS ۱۹۴۲) spihr را همان ʾspyr (esper) فارسی میانهٔ مانوی و پارتی دانست و آن را وام‌واژهٔ σφαῖρα یونانی شمرد؛ همین واژهٔ یونانی به‌راستی در سریانی espērā، ارمنی spʿer، گرجی spero و حبشی spir وام گرفته شده است. در برابر، نیبرگ در «راهنمای پهلوی» (ج ۲، ذیل spihr) می‌نویسد: «من همان ریشه‌شناسی کهن را نگاه می‌دارم: ایرانی باستان *spiθra- (سنسکریت śvitra-) «سپیدفروغ» و سپس «آسمان» ... در فرض هنینگ، ـهـ در spihr درج نابه‌جا می‌بود که بسیار بعید است. البته معنای spihr ممکن است از σφαῖρα اثر پذیرفته باشد، ولی استقلال صوری آن را «سپهر» فارسی نو که واژه‌ای زنده است ثابت می‌کند.» هوبشمان (شمارهٔ ۷۰۷) به پیروی نولدکه همین را می‌گوید و نام هخامنشی Spithridates را که کتسیاس و گزنفون و آریان ضبط کرده‌اند گواه *spiθra- ایرانی باستان می‌گیرد؛ ویکی‌واژه نیز همین راه را می‌رود. نتیجه: ادعای نورایی یک‌سویه است و پژوهش امروزی بیشتر به ریشهٔ ایرانیِ «سپید» گرایش دارد.\",\n \"sources\": [W+\"%D8%B3%D9%BE%D9%87%D8%B1\", E+\"sphere\"],\n \"ref_check\": [\n   {\"ref\": \"ETM:68\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374 - refs_online.json records 'kind: catalog ... Searched archive.org, ketabnak, noorlib, web: not found', no local copy and no online copy; the page cannot be checked.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. spihr\", \"stance\": \"partial\",\n    \"note\": \"'spihr [spy(y)hl | (M ʾspyr), N sipihr] sphere, sky, firmament, fate'. MacKenzie puts the Manichaean form ʾspyr in the same entry (implying Henning's identification) but gives no etymology, so he neither states nor denies the Greek origin.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. spihr\", \"stance\": \"contradicts\",\n    \"note\": \"'spihr ... the vault of heaven, the Celestial sphere. ... I maintain the old etymology: OIr *spiθra- (Skr svitra-) \\\"brightly shimmering\\\" and then \\\"heaven\\\" (cf n. pr. Spithridates). Henning identifies it (List 81; JRAS 1942, 239sq.) with MPrthPrs ʾspyr (= esper) which according to him is borrowed from Gr sphaira. However, in this case -h- in spihr would be an inorganic insertion, which is quite improbable.'\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien 707 (and p.~74 on -θr-)\", \"stance\": \"contradicts\",\n    \"note\": \"HUB.txt: '707. Np. sipihr \\\"Himmel\\\" ist nach Noeldeke direkt = skr. svitra- \\\"weisslich, weiss\\\", dazu nach Geiger afgh. sper \\\"grau\\\"'; and in the sound-law section 'sipihr \\\"Himmel\\\", phl. spihr, ap. Spithridates, Spithradates (Ktesias, Xenoph. Anab., Arrian) Noeldeke, Pers. Stud. I, 36, skr. svitra-'.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.2, scan leaf 554, Mo'in's footnote to سپهر\", \"stance\": \"contradicts\",\n    \"note\": \"'پارسی باستان Sp(a)ithradates (نام سردار پارسی ... به یونانی Spithridates و Spithradates بود. لفظاً یعنی سپهرداد، آسمان‌آفریده). پهلوی spihr ... «اسشق ۷۰۷» ... به قول نولدکه این کلمه مستقیماً از سانسکریت śvitra- (مایل به سفیدی، سفید) آمده و به قول گایگر کلمهٔ افغانی spira (خاکستری‌رنگ) از آنجا ناشی است، «هوبشمان ۷۰۷»'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, pdf p.343, s.v. سپهر\", \"stance\": \"partial\",\n    \"note\": \"Aryanpur lists Old Persian SPITHRA, Pahlavi SPIHR, Sanskrit SVITRA and Greek SPHAIRA, Latin SPHAERA/SPERA, French SPHERE, Spanish ESFERA, Italian SFERA together in one family, with footnote 1 'بازگشت به: سپید' ('see: sepid, white') - i.e. he treats sepehr and sphaira as cognates rather than as loan and source.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"sepehr\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Pahlavi-to-Persian step itself is impeccable: MP spihr > Paz. spihr/spihar/spehir > NP سپهر sepehr 'firmament, heaven; fortune, fate', with the regular prothetic/anaptyctic vowel breaking the initial sp- cluster (as in سپاه < spah, سپاس < spas, سپید < sped). Mo'in tags the entry '[ په. ]' = Pahlavi and glosses '۱- آسمان. ۲- فلک.' The Hafez line Nourai quotes - سیر سپهر و دور قمر را چه اختیار / در گردشند در اثر اختیار دوست - uses it in precisely the 'wheeling heavens = fate' sense, and the 'fate' meaning is already in MacKenzie's Pahlavi gloss. What is disputed is the step above it (node #7): whether MP spihr is the Greek loan (Henning) or the inherited Old Persian *spiθra- 'shining, white' (Noeldeke, Huebschmann, Nyberg, Mo'in, Wiktionary). Wiktionary's entry is explicit: 'Inherited from Middle Persian spyhl ... from Old Persian *spiθrah'. It also notes a genuinely separate modern سپهر meaning 'sphere' in scientific compounds (هواسپهر, سنگ‌سپهر), which it calls 'Phono-semantic matching of French sphere and/or English sphere ... not originally related to etymology 1 above' - so the one place where Persian really does contain Greek sphaira is a 20th-century coinage, not the classical word. Nourai's own aside 'See Kuei for another possible root' shows he was aware the etymology is unsettled, but the root he points to is not the one modern Iranists propose.\",\n \"derivation_fa\": \"پلهٔ پهلوی به فارسی بی‌عیب است: spihr فارسی میانه ← پازند spihr/spihar/spehir ← «سپهر» فارسی نو به معنی «آسمان، فلک؛ بخت و روزگار»، با همان مصوت میانجی که خوشهٔ آغازین sp- را می‌شکند (چنان‌که در «سپاه» از spāh، «سپاس» از spās و «سپید» از spēd). فرهنگ معین این مدخل را با نشانِ «[ په. ]» یعنی پهلوی می‌آورد: «۱- آسمان. ۲- فلک». بیت حافظ که نورایی نقل کرده — «سیر سپهر و دور قمر را چه اختیار / در گردشند در اثر اختیار دوست» — دقیقاً همان معنی «چرخ گردون = تقدیر» را دارد و معنی «بخت» پیشاپیش در گلچین پهلوی مکنزی هست. آنچه محل نزاع است پلهٔ بالاتر است: آیا spihr پهلوی وام‌واژهٔ یونانی است (هنینگ) یا بازماندهٔ *spiθra- «درخشان، سپید» ایرانی باستان (نولدکه، هوبشمان، نیبرگ، معین، ویکی‌واژه). ویکی‌واژه صریح است: «سپهر» از فارسی میانهٔ spihr و آن از پارسی باستان *spiθrah. همان مدخل یادآور می‌شود که «سپهر» در ترکیب‌های علمی امروزی (هواسپهر، سنگ‌سپهر) واژهٔ دیگری است که در سدهٔ بیستم بر پایهٔ sphère فرانسوی ساخته شده و با سپهرِ کلاسیک ربطی ندارد. حکم: پژوهش امروزی مسیر یونانی را رد می‌کند و ریشهٔ ایرانی «سپید» را ترجیح می‌دهد.\",\n \"sources\": [W+\"%D8%B3%D9%BE%D9%87%D8%B1\", \"https://abadis.ir/fatofa/%D8%B3%D9%BE%D9%87%D8%B1/\"],\n \"ref_check\": [\n   {\"ref\": \"ETM:68\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Risheh-shenasi - no digital copy on any permitted platform (refs_online.json: 'Searched archive.org, ketabnak, noorlib, web: not found').\"},\n   {\"ref\": \"MON:1827\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi s.v. سپهر, read via abadis.ir (print pagination not mapped online): 'فرهنگ معین: (س پِ) [ په. ] (اِ.) ۱- آسمان. ۲- فلک.' The tag [ په. ] = Pahlavi confirms the Pahlavi-to-Persian arrow; Mo'in says nothing about Greek.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. سپهر (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"'[ په. ]' Pahlavi origin tag - supports the lower arrow, silent on the Greek one.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.2, scan leaf 554, Mo'in's footnote\", \"stance\": \"contradicts\",\n    \"note\": \"Mo'in's own footnote derives سپهر from Old Persian *spiθra- via the name Spithridates and cites Noeldeke's equation with Skt. svitra- 'white' - not from Greek.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. spihr\", \"stance\": \"contradicts\",\n    \"note\": \"'its formal independence is proved by NP sipihr which belongs to the living language' - Nyberg uses New Persian sepehr itself as the argument against the Greek loan.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien 707\", \"stance\": \"contradicts\",\n    \"note\": \"'Np. sipihr \\\"Himmel\\\" ist nach Noeldeke direkt = skr. svitra- \\\"weisslich, weiss\\\"'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. spihr\", \"stance\": \"partial\",\n    \"note\": \"'sphere, sky, firmament, fate' - the 'fate' sense Nourai's Hafez quotation illustrates is already Middle Persian.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 9, \"lang\": \"Germanic\", \"words\": \"springan\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Proto-Germanic *springana 'to burst forth, leap' (OE springan, OS/OHG springan, ON springa, MDu. springhen) is regularly derived from PIE *spre(n)gǵh-, the nasalized variant of *spergǵh- 'to move quickly, hurry' - Pokorny 998, lemma 'spergh-, spregh-, nasalized sprengh-', whose material is Skt. spr̥hayati 'longs for', Av. a-spərəzata, Gk. sperchomai 'storm along, hurry', ON springa, OE/OS/OHG springan. That is a root of its own, not the root of this chart. But Pokorny's own note on the lemma is 'Erweit. from sper- \\\"zucken, schnellen\\\"', i.e. *spergh- is an extension of exactly the root in Nourai's box, so the arrow is defensible as an ultimate rather than direct descent - which is what Klein, the source cited here, actually says.\",\n \"derivation_fa\": \"ژرمنی آغازین *springaną «جهیدن، ناگهان بیرون زدن» (انگلیسی کهن springan، ساکسونی کهن و آلمانی علیای کهن springan، نروژی کهن springa) به‌قاعده از هندواروپایی *spre(n)ǵʰ- می‌آید، یعنی صورت خیشومی‌شدهٔ *sperǵʰ- «شتافتن، تند حرکت کردن»؛ پوکورنی این را مدخل جداگانه‌ای در صفحهٔ ۹۹۸ می‌آورد با گواه‌هایی چون سنسکریت spṛhayati، اوستایی ā-spərəzata و یونانی σπέρχομαι. پس این ریشهٔ دیگری است، نه ریشهٔ همین نمودار. با این همه، خودِ پوکورنی در توضیح همان مدخل می‌نویسد که *spergh- «گسترشی از sper- ‹تکان خوردن، جستن›» است؛ بنابراین پیکان نورایی را می‌توان به‌عنوان تبارِ نهایی (نه مستقیم) پذیرفت — و کلاین که منبع مورد استناد همین جعبه است دقیقاً همین را می‌گوید. حکم: با احتیاط پذیرفتنی.\",\n \"sources\": [W+\"spring\", W+\"Reconstruction:Proto-Germanic/springan%C4%85\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1497\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt, leaf 794 (the leaf carrying pp. ~1496-1499), s.v. spring: 'ME. springen, fr. OE. springan, rel. to ON., OFris., Swed. springa ... fr. I.-E. base *sprengh-, a nasalized variant of base *spergh-, \\\"to move quickly\\\" ... Base *spergh- itself seems to be an enlarged form of the primitive base *sper-, *spher-, \\\"to move convulsively; to scatter\\\", whence OI. sphurati, \\\"kicks with the foot\\\", Gk. spairein, \\\"to move convulsively\\\". See spurn'. This is precisely Nourai's claim, including the *sper-/*spher- ultimate base.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 998, lemma spergh-, spregh-, nasalized sprengh-\", \"stance\": \"partial\",\n    \"note\": \"POK_full.txt line 79629: 'Meaning: to hurry, to spring. Note: Erweit. from sper- \\\"zucken, schnellen\\\". Material: Old Indie sprhayati ... Old Icelandic springa \\\"spring, burst out\\\" ... Old English Old Saxon Old High German springan ds.' - a separate lemma, but explicitly an extension of sper-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. spergh-\", \"stance\": \"partial\",\n    \"note\": \"'spergh-. To move, hasten, spring. Nasalized root form *sprengh-. 1. Germanic *springan in: a. Old English springan, to spring: SPRING ... [Pok. spergh- 998.]' - Watkins files the Germanic verb under spergh-, not under spere- 'ankle'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 675 (cited by Pokorny as WP. II 675)\", \"stance\": \"partial\",\n    \"note\": \"Pokorny's reference line for the spergh- lemma is 'WP. II 675, Trautmann 278 f.' - i.e. Walde-Pokorny treat it as its own Sippe, listed among the 'folgenden Gruppen' under 1. sp(h)er- in Bd. II 668ff.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, pdf p.341 footnote to سپاردن\", \"stance\": \"partial\",\n    \"note\": \"'واژه‌های انگلیسی SPRING و SPRINGE و آلمانی SPRINGEN از یک واج‌ریشه‌ی نزدیک به این ...' - Aryanpur likewise says spring belongs to a root 'close to' the sepordan root, not the same one.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"spring\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English spring (verb) is ME springen < OE springan, with the noun spring 'a leap; source of water; the season in which plants spring up' built on the same verb (OE spring 'springing, source of water', cf. MHG sprinc, OHG sprung). The chain Germanic > English is uncontroversial; what the chart gets only half-right is the attachment to *spher-. Nourai's own NOTE - 'AHD & POK:998 claim this is from root \\\"Spereg: to jump\\\"' - is essentially correct and modern scholarship sides with the note rather than with the arrow: Watkins files SPRING under spergh- [Pok. spergh- 998] and Wiktionary derives OE springan from PGmc *springana < PIE *spre(n)gǵh- < *spergǵh- 'to hurry'. Two small corrections to the note itself: p.998 of Pokorny is the lemma spergh-/sprengh-, not '(s)p(h)ereg-' (which is pp. 996-998, a different lemma meaning 'to twitch, burst, sprinkle'); and the two are in any case, on Pokorny's own statement, extensions of the sper- of this chart, so the arrow is not simply wrong, only indirect.\",\n \"derivation_fa\": \"فعل انگلیسی spring از انگلیسی میانه springen و آن از انگلیسی کهن springan است؛ اسمِ spring به هر سه معنی «جهش، چشمه، بهار» بر همان فعل ساخته شده (انگلیسی کهن spring «جوشش، سرچشمه»، قس آلمانی علیای میانه sprinc). زنجیرهٔ ژرمنی ← انگلیسی بی‌مناقشه است؛ آنچه نیم‌درست است پیوند آن با ریشهٔ *spher- است. خودِ یادداشتِ نورایی — که AHD و پوکورنی ص ۹۹۸ این را از ریشهٔ دیگری می‌دانند — درست است و پژوهش امروزی جانب همان یادداشت را می‌گیرد نه جانب پیکان: واتکینز SPRING را ذیل spergh- می‌آورد و ویکی‌واژه springan را از *spre(n)ǵʰ- ‹ *sperǵʰ- می‌گیرد. دو تصحیح کوچک بر خود یادداشت: صفحهٔ ۹۹۸ پوکورنی مدخل spergh-/sprengh- است نه «(s)p(h)ereg-» (که صص ۹۹۶–۹۹۸ و معنایی دیگر دارد)؛ و به گفتهٔ خود پوکورنی هر دو گسترشی از همان sper- این نمودارند، پس پیکان نادرست نیست، تنها غیرمستقیم است. حکم: با احتیاط پذیرفتنی؛ یادداشت کتاب درست است.\",\n \"sources\": [W+\"spring\", E+\"sphere\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1497\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 794 s.v. spring: 'fr. I.-E. base *sprengh-, a nasalized variant of base *spergh- ... Base *spergh- itself seems to be an enlarged form of the primitive base *sper-, *spher-'; and s.v. spring, n.: 'ME., fr. OE. spring, \\\"springing; source of water\\\", fr. springan'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. spergh-; index 'SPRING spergh-'\", \"stance\": \"partial\",\n    \"note\": \"'spergh-. To move, hasten, spring ... Old English springan, to spring: SPRING ... [Pok. spergh- 998.]'. The index line reads 'SPRING spergh-' (and 'SPRING pelo-' for the unrelated homonym). Watkins therefore confirms Nourai's NOTE, not his arrow.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 998\", \"stance\": \"partial\",\n    \"note\": \"The lemma on p.998 is 'spergh-, spregh-, nasalized sprengh-', not '(s)p(h)ereg-' (pp. 996-998); its Note reads 'Erweit. from sper- \\\"zucken, schnellen\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. spring v./n., springe\", \"stance\": \"supports\",\n    \"note\": \"See ref_check; Klein explicitly routes spring back to *sper-, *spher- through *spergh-/*sprengh-.\"}\n ]\n})\n\nout[\"entries\"].append(e0)\n\n# ---------------- entry 4: Spinakion ----------------\ne4 = {\n \"entry\": 4,\n \"root\": \"Spinakion\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"Byzantine Greek spinakion / spanakin 'spinach' - itself a borrowing; the ultimate source is Iranian *spinaka-/*spinaka- 'the thorny(-fruited) plant' (> NP اسپناخ/اسفناج), from *spin- 'thorn' < Proto-Iranian *spai-/*spi- < PIE *spey- 'sharp, pointed'\",\n \"note\": \"The whole chart runs backwards. Spinach is an Iranian culture-word that travelled west with the Arab conquest, not a Greek word that travelled east. The modern account (Wiktionary, after Asatrian, A Comparative Vocabulary of Central Iranian Dialects 2011: 43-45, Lokotsch 126, Cabolov II 263, Abaev III 201-202) reconstructs two late Middle Iranian forms *ispanag / *ispanax, giving Arabic اسفناج isfanaj and اسفناخ isfanax; Andalusian Arabic isbinax passed into Ibero-Romance (Catalan espinac, Spanish espinaca, Aragonese espinai), thence into Medieval Latin spinacium / spinachium / spinarchia (assimilated to spina 'thorn'), and only from that Medieval Latin into Byzantine Greek spinakion / spanakin, whence Modern Greek spanaki and the Balkan forms spanak / spanac. Greek spinakion is not an ancient word: the plant itself is unknown to Dioscorides and Galen and reaches the Mediterranean only in the Islamic period. Nourai's own cited source undercuts him: Mo'in's etymological footnote in Borhan-e Qate' (vol.1, to the entry اسپناخ) quotes Dawud al-Antaki's Tadhkira - «اسفاناج معرّبٌ عن فارسیة هو اسباناخ», 'isfanaj is an Arabicization of the Persian, which is asbanax' - and mentions Greek spinakion only as one more member of the list, not as the source. Klein 1489 and Skeat 507, cited further down the chart, both stop at Persian aspanakh as the origin. The lower half of Nourai's chart (Persian > Arabic > Spanish > Medieval Latin > French > English) is right and is simply Klein's chain; the top three boxes reverse it.\",\n \"note_fa\": \"کل این نمودار وارونه است. «اسفناج» واژه‌ای فرهنگی و ایرانی است که با فتوحات اسلامی رو به باختر رفت، نه واژه‌ای یونانی که رو به خاور آمده باشد. تبیین امروزی (ویکی‌واژه به پیروی از آساتریان ۲۰۱۱، لوکوچ ۱۲۶، چابولوف و آبایف) دو صورت ایرانی میانهٔ متأخر *ispanāg و *ispanāx را بازسازی می‌کند که «اسفناج» و «اسفناخ» عربی از آنها برآمده‌اند؛ صورت عربی اندلسی إسبناخ به زبان‌های ایبری رفت (کاتالان espinac، اسپانیایی espinaca)، از آنجا به لاتینِ سده‌های میانه spinacium/spinachium (با همگونی به spina «خار») و تنها از همان لاتین به یونانی بیزانسی σπινάκιον/σπανάκιν رسید که یونانی امروز σπανάκι و صورت‌های بالکانی از آن است. σπινάκιον واژه‌ای یونانی باستان نیست: دیوسکوریدس و جالینوس این گیاه را نمی‌شناسند و اسفناج تنها در دورهٔ اسلامی به مدیترانه می‌رسد. جالب آنکه منبعِ خودِ نورایی خلاف او را می‌گوید: حاشیهٔ ریشه‌شناختی معین در برهان قاطع (ذیل «اسپناخ») از تذکرهٔ داود ضریر انطاکی نقل می‌کند «اسفاناج معرّبٌ عن فارسیة هو اسباناخ» و σπινάκιον یونانی را تنها یکی از صورت‌های همان واژه می‌شمارد. کلاین (ص ۱۴۸۹) و اسکیت (ص ۵۰۷) نیز که در پایین همین نمودار نقل شده‌اند، هر دو «اسپناخ» فارسی را سرچشمه می‌دانند. نیمهٔ پایینی نمودار (فارسی ← عربی ← اسپانیایی ← لاتین میانه ← فرانسه ← انگلیسی) درست و همان زنجیرهٔ کلاین است؛ سه جعبهٔ بالایی آن را وارونه کرده‌اند. حکم: پژوهش امروزی ریشهٔ یونانی را رد می‌کند.\",\n \"sources\": [W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC\", E+\"spinach\"],\n \"ref_check\": [\n   {\"ref\": \"MON:227\", \"status\": \"contradicts\",\n    \"note\": \"Mo'in's etymological footnote in Borhan-e Qate' vol.1 (BQT_v1_pages.txt, scan leaf 332, footnote 3 to اسپناخ - the same material as his Farhang-e Farsi entry Nourai cites): 'به لغت علمی Spinacia، به انگلیسی spinach یا spinage، به فرانسه epinards، به آلمانی Spinat، به عربی اسفاناخ، و فارسی اسپناخ، اسپناج، اسپنانج، اسپاناج، اسپانج، اسباناج، اسباناخ و در طبری اسپینا ... همه از یک ریشه است. داود ضریر انطاکی در تذکرهٔ خود گوید: اسفاناج معرّب عن فارسیة هو اسباناخ. در یونانی spinakion ...'. Mo'in lists the Greek form but explicitly calls the Arabic an Arabicization of the Persian - the opposite of making Greek the root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1, scan leaf 332, Mo'in's footnote to اسپناخ\", \"stance\": \"contradicts\",\n    \"note\": \"See ref_check - 'اسفاناج معرّب عن فارسیة هو اسباناخ'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1489 s.v. spinach\", \"stance\": \"contradicts\",\n    \"note\": \"'fr. ML. spinachia, spinachium, which - prob. through the medium of Sp. espinaca and Andalusian Arab. isbinakh - derives fr. Arab. isbinakh, earlier isfanakh, isfanakh, fr. Pers. aspanakh, \\\"spinach\\\"'. No Greek anywhere in the entry; Persian is the terminus.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., p. ~506-507 s.v. Spinach, Spinage\", \"stance\": \"contradicts\",\n    \"note\": \"SKT_dli_revised.txt: 'Spinach, Spinage, a vegetable. (F. - Span. - Arab. - Pers.) Spinage is a \\\"voiced\\\" form of spinach. O. F. espinache, espinage, espinace. - Span. espinaca. - Arab. aspanakh, isfanaj; of Pers. origin (Devic).' Skeat's language-chain header ends at Persian, with no Greek stage.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europ. Woerter orient. Ursprungs, no. 126 (p.11)\", \"stance\": \"partial\",\n    \"note\": \"The headword is '126. Pers. aspanah:' followed by 'ar. isfanag, isfinag \\\"Spinat\\\" [Vielleicht kommen diese Formen selbst aus dem Lateinischen, etwa spina \\\"Dorn\\\" oder besser *spinax ...]; hieraus zunaechst die romanischen Formen afrz. espinoche, espinard; frz. epinard, prov. espinar, kat. espinac, sp. espinaca, pg. espinafre, it. spinace, rum. spanac.' Lokotsch heads the article with the Persian word (supporting Persian priority) but floats a Latin spina alternative; he never proposes a Greek source.\"}\n ],\n \"nodes\": []\n}\n\ne4[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Arabic\", \"words\": \"spânâj\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two problems. (i) Direction: Arabic did not get the word from Greek. The Arabic forms اسفاناج/اسفناج isfanaj, اسفاناخ/اسفناخ isfanax, سبانخ sabanix, سبانج sabanaj are borrowings from Middle Iranian *ispanag/*ispanax; the prosthetic ʾis- exists precisely to break the Iranian initial cluster sp-, and the ف/ب for Iranian p is the regular substitution in an alphabet with no p (cf. فیل < pil, برنامج < barnamag). Nourai's own reference (Mo'in) quotes al-Antaki calling the Arabic word 'muarrab' (Arabicized) from Persian asbanax. The Greek borrowing runs the other way and much later, from Medieval Latin into Byzantine Greek. (ii) Form: 'spanaj' is not a possible Arabic word - Arabic has no phoneme /p/ and no word-initial consonant cluster, so a form beginning sp- cannot be Arabic. What the book prints is an Iranian shape labelled Arabic.\",\n \"derivation_fa\": \"دو اشکال دارد. نخست جهت وام‌گیری: عربی این واژه را از یونانی نگرفته است. صورت‌های «اسفاناج/اسفناج»، «اسفاناخ/اسفناخ»، «سبانخ» و «سبانج» وام از ایرانی میانهٔ *ispanāg/*ispanāx‌اند؛ همزهٔ آغازین (اِ-) درست برای شکستن خوشهٔ sp- ایرانی افزوده شده و ابدال «پ» ایرانی به «ف/ب» قاعدهٔ همیشگی معرّب‌سازی است (قس «پیل ← فیل»، «برنامگ ← برنامج»). خودِ منبع نورایی، یعنی معین، از انطاکی نقل می‌کند که «اسفاناج معرّبٌ عن فارسیة هو اسباناخ». وام‌گیری یونانی در جهت وارونه و بسیار دیرتر رخ داده: از لاتین سده‌های میانه به یونانی بیزانسی. دوم صورتِ واژه: «spânâj» اصلاً واژهٔ عربی ممکنی نیست، زیرا عربی نه واج /پ/ دارد و نه خوشهٔ همخوانی در آغاز کلمه. آنچه کتاب چاپ کرده صورتی ایرانی است با برچسب «عربی». حکم: پژوهش امروزی این گره را رد می‌کند.\",\n \"sources\": [W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC\", E+\"spinach\"],\n \"ref_check\": [\n   {\"ref\": \"MON:227\", \"status\": \"contradicts\",\n    \"note\": \"Mo'in's footnote (BQT_v1_pages.txt leaf 332): 'داود ضریر انطاکی در تذکرهٔ خود گوید: اسفاناج معرّب عن فارسیة هو اسباناخ' - the Arabic word is an Arabicization of the Persian, not a reflex of Greek.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1489 s.v. spinach\", \"stance\": \"contradicts\",\n    \"note\": \"'fr. Arab. isbinakh, earlier isfanakh, isfanakh, fr. Pers. aspanakh' - Klein's Arabic forms all have the prosthetic i- and derive from Persian.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 126\", \"stance\": \"partial\",\n    \"note\": \"'126. Pers. aspanah: ar. isfanag, isfinag \\\"Spinat\\\"' - Lokotsch's Arabic forms are isfanag/isfinag, again with prosthetic i-, and he heads the article with the Persian word.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1 leaf 332, footnote 3\", \"stance\": \"contradicts\",\n    \"note\": \"'به عربی اسفاناخ، و فارسی اسپناخ، اسپناج، اسپنانج، اسپاناج، اسپانج، اسباناج، اسباناخ' - the pe-forms are listed as the Persian ones, the fe/be-forms as Arabic.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\",\n    \"note\": \"grep -n -i 'spinach|isfanakh' FVQ.txt returns nothing - the word is not Qur'anic, so Jeffery has no entry.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"espenâx\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Persian word is real, old and well attested - اسپناخ/سپاناخ/اسفناج, with Rumi already writing من سپاناخ تو با هرچم پزی (Masnavi I, 1258) - and the Persian script and variants Nourai gives (اسفناج، اسپاناخ) are correct. What is wrong is that it is drawn as a borrowing FROM Arabic. Persian is the donor, not the recipient: the Old Iranian etymon is *spinaka-/*spinaka- 'the thorny one' (from the prickly fruit of prickly-seeded spinach), built on *spin- 'thorn' (Northwestern Iranian; Southwestern *sin-) < Proto-Iranian *spai-/*spi- < PIE *spey- 'sharp, pointed' - the same root as Latin spina, Ossetian synj 'thorn', Kurdish sping, Persian سنجد. Wiktionary (after Asatrian) posits two late Middle Iranian forms, *ispanag and dialectal *ispanax, which produced Arabic اسفناج and اسفناخ respectively; the Persian variants written with پ come straight down from Middle Iranian, while اسفناج with ف is a re-borrowing of the Arabized shape back into Persian (an Arabic-mediated round trip). Mo'in's footnote lists all of these as 'همه از یک ریشه' and quotes al-Antaki for the Persian origin.\",\n \"derivation_fa\": \"واژهٔ فارسی واقعی و کهن و پرگواه است — «اسپناخ»، «سپاناخ»، «اسفناج» — و مولوی در مثنوی (دفتر یکم) می‌گوید «من سپاناخ تو، با هرچم پزی»؛ صورت‌های فارسی و گونه‌هایی که نورایی آورده نیز درست‌اند. اشکال در این است که این واژه وام‌واژه‌ای از عربی نشان داده شده، حال آنکه فارسی وام‌دهنده است نه وام‌گیرنده. صورت ایرانی باستان *spināka- «خاردار» است (به سبب دانهٔ خاردار اسفناجِ کهن)، ساخته بر *spin- «خار» (ایرانی شمال‌غربی؛ در جنوب‌غربی *sin-) از ایرانی آغازین *spai-/*spi- و آن از هندواروپایی *spey- «تیز، نوک‌دار» — همان ریشه‌ای که لاتینی spina، آسی synʒ «خار»، کردی sping و فارسی «سنجد» از آن‌اند. ویکی‌واژه به پیروی آساتریان دو صورت ایرانی میانهٔ متأخر *ispanāg و گویشی *ispanāx را بازسازی می‌کند که به‌ترتیب «اسفناج» و «اسفناخ» عربی از آنها برآمده‌اند؛ صورت‌های فارسیِ نوشته‌شده با «پ» مستقیماً از ایرانی میانه مانده‌اند و «اسفناج» با «ف» وام‌گیری دوبارهٔ صورتِ معرّب به فارسی است (رفت‌وبرگشت از راه عربی). حاشیهٔ معین همهٔ اینها را «همه از یک ریشه» می‌خواند و برای اصالت فارسی از انطاکی گواه می‌آورد. حکم: پژوهش امروزی جهت این پیکان را وارونه می‌داند.\",\n \"sources\": [W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC\", \"https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:227\", \"status\": \"contradicts\",\n    \"note\": \"Mo'in's footnote (BQT_v1_pages.txt leaf 332, footnote 3 to اسپناخ) makes Persian the source of the Arabic ('اسفاناج معرّب عن فارسیة هو اسباناخ') and treats the Greek spinakion as one more form of the same word, not its ancestor. His Farhang-e Farsi entry (abadis.ir) gives 'اسفناج = اسپناج. اسپناخ. سپاناخ. اسپاناج' with no foreign-origin tag at all - i.e. he does not mark it as a loanword in Persian.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1, leaves 329-332 (اسپانج, اسپناخ, اسپنانج)\", \"stance\": \"contradicts\",\n    \"note\": \"The headwords themselves are Persian with پ: 'اسپانج - با بای فارسی بالف کشیده و فتح نون و سکون جیم، اسفناج باشد و آن سبزی ...' (leaf 329) and 'اسپنانج - باجیم بر وزن اصفهانک، بمعنی اسفناج ... سبزی آش باشد' (leaf 332). Mo'in's footnote derives the Arabic from these.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. اسفناج (abadis.ir)\", \"stance\": \"silent\",\n    \"note\": \"'(اِ فَ یا فِ) (اِ.) = اسپناج. اسپناخ. سپاناخ. اسپاناج: گیاهی است یک ساله ...' - no origin tag (contrast [ع.] for Arabic loans, [فر.] for French ones), so Mo'in does not treat it as borrowed.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 126, headword 'Pers. aspanah'\", \"stance\": \"supports\",\n    \"note\": \"Lokotsch places the Persian word at the head of the whole European word-family, i.e. Persian is the source.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1489\", \"stance\": \"supports\",\n    \"note\": \"'... fr. Pers. aspanakh, \\\"spinach\\\"' - Persian is the ultimate origin in Klein too.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Arabic\", \"words\": \"isbânâx\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"This is the one arrow in the chart's Persian section that is right, and it is the link every western source records. Persian اسباناخ/اسپاناخ was Arabicized as إِسْبَانَاخ isbanax (also إسفاناخ isfanax, إسفناج isfanaj, سبانخ sabanix): Persian p has no Arabic counterpart and is rendered b or f, and a prosthetic ʾis- is prefixed because Arabic phonotactics forbid an initial cluster. The form that mattered historically is the Andalusian Arabic إسبناخ isbinax, since it is the Andalusian pronunciation that Ibero-Romance took over in the 12th-13th c. Klein (1489) and Skeat (507), both cited by Nourai at this box, say exactly this.\",\n \"derivation_fa\": \"این تنها پیکانِ درستِ بخش فارسیِ نمودار است و همان حلقه‌ای است که همهٔ منابع غربی ضبط کرده‌اند. «اسباناخ/اسپاناخ» فارسی در عربی به صورت «إسباناخ» معرّب شد (و نیز «إسفاناخ»، «إسفناج»، «سبانخ»): واج «پ» فارسی در عربی برابر ندارد و به «ب» یا «ف» بدل می‌شود، و همزهٔ آغازین افزوده می‌شود چون عربی خوشهٔ همخوانی در آغاز واژه نمی‌پذیرد. صورتی که در تاریخ اهمیت یافت «إسبناخ» عربیِ اندلسی است، زیرا همین تلفظ اندلسی بود که در سده‌های دوازدهم و سیزدهم به زبان‌های ایبری راه یافت. کلاین (ص ۱۴۸۹) و اسکیت (ص ۵۰۷) — هر دو در همین جعبه مورد استناد نورایی — دقیقاً همین را می‌گویند. حکم: ادعای نورایی درست است.\",\n \"sources\": [E+\"spinach\", W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1489\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt, the leaf whose catchwords run 'sphaerometer ... spinach' and whose page markers read '1488 - 1489': 'spinach, n. - MF. espinache, espinage ... fr. ML. spinachia, spinachium, which - prob. through the medium of Sp. espinaca and Andalusian Arab. isbinakh - derives fr. Arab. isbinakh, earlier isfanakh, isfanakh, fr. Pers. aspanakh, \\\"spinach\\\".' Page 1489 is exact.\"},\n   {\"ref\": \"SKT:507\", \"status\": \"supports\",\n    \"note\": \"SKT_dli_revised.txt (the 1911 revised Concise; the running number 506 stands a few lines above the entry, so the entry falls on p.506-507): 'Spinach, Spinage, a vegetable. (F. - Span. - Arab. - Pers.) ... O. F. espinache, espinage, espinace. - Span. espinaca. - Arab. aspanakh, isfanaj; of Pers. origin (Devic).'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1489\", \"stance\": \"supports\", \"note\": \"See ref_check; Klein singles out the Andalusian Arabic isbinakh as the intermediary.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat p.506-507\", \"stance\": \"supports\", \"note\": \"See ref_check; 'Arab. aspanakh, isfanaj; of Pers. origin'.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 126\", \"stance\": \"supports\", \"note\": \"'ar. isfanag, isfinag \\\"Spinat\\\" ... hieraus zunaechst die romanischen Formen' - the Arabic word is the immediate source of the Romance forms.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1 leaf 332 footnote\", \"stance\": \"supports\", \"note\": \"'داود ضریر انطاکی ... گوید: اسفاناج معرّب عن فارسیة هو اسباناخ' - Antaki names the very form isbanax as the Persian original of the Arabic.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Spanish\", \"words\": \"espinacia\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The Spanish word is espinaca (Old Spanish espinaca, from Andalusian Arabic isbinax, with popular assimilation to espina 'thorn'), and that is the form every source gives - including Klein, the reference printed in this very box: 'prob. through the medium of Sp. espinaca and Andalusian Arab. isbinakh'. Lokotsch: 'sp. espinaca'; Skeat: 'Span. espinaca'. There is no Spanish *espinacia. The printed page 440 of Nourai (rendered at 200 dpi from the PDF and archived as data/verification/sources/refs/ocr/BOOK/470.png) clearly shows 'espinacia' in the Spanish box, so the extraction is faithful and the error is the author's - most probably contamination from the Medieval Latin spinachia/spinacium in the box immediately below. Apart from the -ia, the derivation Arabic > Spanish is correct: Andalusian Arabic isbinax > Old Spanish espinaca, with es- for the Arabic prosthetic vowel and the Romance feminine -a.\",\n \"derivation_fa\": \"واژهٔ اسپانیایی espinaca است (اسپانیایی کهن espinaca از عربی اندلسی إسبناخ، با همگونی عامیانه به espina «خار») و همهٔ منابع همین صورت را می‌دهند — از جمله کلاین که ارجاعِ چاپ‌شده در همین جعبه است: «احتمالاً از راه اسپانیایی espinaca و عربی اندلسی isbinakh». لوکوچ نیز «sp. espinaca» و اسکیت «Span. espinaca» دارد؛ صورتِ *espinacia در اسپانیایی وجود ندارد. تصویر صفحهٔ ۴۴۰ چاپ کتاب (رندر ۲۰۰ dpi و بایگانی‌شده در data/verification/sources/refs/ocr/BOOK/470.png) به‌روشنی «espinacia» را در جعبهٔ اسپانیایی نشان می‌دهد؛ پس خوانشِ داده درست بوده و خطا از خودِ کتاب است، به احتمال زیاد بر اثر آمیختگی با spinachia لاتینِ جعبهٔ پایین‌تر. جز همین «ـia»، سیر عربی ← اسپانیایی درست است: إسبناخ عربی اندلسی ← espinaca اسپانیایی کهن، با es- در برابر همزهٔ عربی و پایانهٔ مؤنث رومیایی ‎-a. حکم: خطای چاپی کتاب.\",\n \"error_in\": \"book\",\n \"book_prints\": \"espinacia\",\n \"correct_form\": \"espinaca\",\n \"sources\": [E+\"spinach\", W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1489\", \"status\": \"partial\",\n    \"note\": \"Klein p.1489 s.v. spinach writes 'Sp. espinaca', not espinacia. The page supports the Arabic-to-Spanish step but not the form printed in Nourai's box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1489\", \"stance\": \"partial\", \"note\": \"'through the medium of Sp. espinaca and Andalusian Arab. isbinakh'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat p.506-507\", \"stance\": \"partial\", \"note\": \"'Span. espinaca ... The Ital. spinace and Span. espinaca are referred, by popular etymology, to L. spina, a thorn'.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 126\", \"stance\": \"partial\", \"note\": \"'kat. espinac, sp. espinaca, pg. espinafre' - espinaca again.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. spinach (archived)\", \"stance\": \"partial\",\n    \"note\": \"'from Old Provencal espinarc, which perhaps is via Catalan espinac, from Andalusian Arabic isbinakh' - Etymonline routes the word through Catalan/Provencal rather than Castilian, but the Spanish form it presupposes is espinaca.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Middle Latin\", \"words\": \"spinachia\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Medieval Latin spinachia / spinachium is the Latinization of the Ibero-Romance word in the medical and botanical Latin of the 12th-13th c. (the channel being the Salerno-Toledo translation movement, where Arabic dietetic and pharmacological works were put into Latin). Klein p.1489 gives exactly 'ML. spinachia, spinachium'; Wiktionary lists 'Medieval Latin: spinacium, spinachium, spinarchia (influenced by spina \\\"thorn\\\")'. The -ch- spelling is a device for the Arabic kha of isbinax, and the whole form was then reshaped under the influence of Latin spina 'thorn' - a folk etymology helped by the fact that the old prickly-seeded cultivar really does have spiny fruit. From this Medieval Latin come Italian spinace, Middle High German spinat (German Spinat), and - crucially for the root box of this entry - Byzantine Greek spinakion.\",\n \"derivation_fa\": \"لاتینِ سده‌های میانه spinachia/spinacium لاتینی‌شدهٔ واژهٔ ایبری‌رومیایی است در متون پزشکی و گیاه‌شناسی سده‌های دوازدهم و سیزدهم، از رهگذر نهضت ترجمهٔ سالرنو و تولدو که آثار داروشناسی و تغذیهٔ عربی را به لاتین برگرداند. کلاین (ص ۱۴۸۹) دقیقاً «ML. spinachia, spinachium» می‌آورد و ویکی‌واژه صورت‌های spinacium، spinachium و spinarchia را با یادداشت «زیر تأثیر spina ‹خار›» فهرست می‌کند. نویسهٔ ‎-ch- تدبیری برای نمایاندن «خ» عربیِ إسبناخ است و سپس همهٔ واژه زیر نفوذ spina «خار» بازسازی شده — ریشه‌شناسی عامیانه‌ای که این واقعیت به آن یاری رسانده که گونهٔ کهن اسفناج به‌راستی دانهٔ خاردار دارد. از همین لاتین، ایتالیایی spinace و آلمانی علیای میانه spinat (آلمانی Spinat) و — که برای جعبهٔ ریشهٔ همین مدخل تعیین‌کننده است — یونانی بیزانسی σπινάκιον برآمده‌اند. حکم: ادعای نورایی درست است.\",\n \"sources\": [W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC\", E+\"spinach\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1489\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt p.1489 s.v. spinach: 'fr. ML. spinachia, spinachium' and, at the end of the entry, 'Fr. ML. spinachia, spinachium derive also It. spinace and - with change of suff. - O Provenc. espinarc and MHG. spinat (G. Spinat).' Exactly the form and the parentage drawn.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1489\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Spinach\", \"stance\": \"partial\",\n    \"note\": \"SKT.txt (older impression): 'Formed (as if from Late L. spinaceus), from spina, a thorn, because the fruit is sometimes very prickly; so also Span. espinaca' - Skeat records the Latin spina reshaping that Klein and Wiktionary also note.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 126\", \"stance\": \"partial\",\n    \"note\": \"'Mit steter Anlehnung an lat. spina auch im Germanischen dtsch. Spinat, ndl. spinazie, engl. spinage' - the constant leaning on Latin spina.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 6, \"lang\": \"French\", \"words\": \"espinard; epinard\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both French forms are real and the Medieval-Latin-to-French step is Klein's own: 'MF. espinache, espinage (whence - with change of suff. - MF. espinarde, espinard, F. epinard), fr. ML. spinachia, spinachium'. Note what that says: the primary French form is espinache/espinage, and espinard is a secondary French re-suffixation of it (-ache replaced by the noun suffix -ard); modern epinard then shows the regular loss of preconsonantal s (espinard > epinard) marked by the acute accent, and is normally used in the plural, epinards. Nourai's box gives only the -ard branch and omits espinache, which matters because espinache, not espinard, is what English borrowed (see node #7). Wiktionary's descendant tree agrees: 'Old French: espinoche, espinache, espinarde > French epinard'.\",\n \"derivation_fa\": \"هر دو صورت فرانسوی واقعی‌اند و پلهٔ لاتینِ میانه ← فرانسه همان است که کلاین می‌گوید: «MF espinache، espinage (و از آنجا، با تغییر پسوند، MF espinarde، espinard و فرانسهٔ نو épinard) از ML spinachia، spinachium». نکته همین‌جاست: صورت اصلی فرانسوی espinache/espinage است و espinard پسوندگردانیِ ثانویِ آن در خود فرانسه است (جایگزینی ‎-ache با پسوند اسم‌ساز ‎-ard)؛ épinard امروزی هم افتادن قاعده‌مندِ «s» پیش از همخوان را نشان می‌دهد که با همزهٔ تیز (é) جبران شده و معمولاً به صورت جمع épinards به کار می‌رود. نورایی تنها شاخهٔ ‎-ard را آورده و espinache را انداخته است، و این مهم است چون آنچه انگلیسی وام گرفت espinache بود نه espinard (نک. گره ۷). درخت بازماندگان در ویکی‌واژه نیز همین را می‌گوید. حکم: با احتیاط پذیرفتنی.\",\n \"sources\": [E+\"spinach\", W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1489\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt p.1489: 'spinach, n. - MF. espinache, espinage (whence - with change of suff. - MF. espinarde, espinard, F. epinard), fr. ML. spinachia, spinachium ...'. Klein gives both of Nourai's French forms and their Medieval Latin parent, but makes espinard secondary to espinache.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1489\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 126\", \"stance\": \"supports\",\n    \"note\": \"'hieraus zunaechst die romanischen Formen afrz. espinoche, espinard; frz. epinard' - the same two French forms, again with the -oche/-ache type listed first.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Spinach\", \"stance\": \"partial\",\n    \"note\": \"SKT_dli_revised.txt: 'O. F. espinache, espinage, espinace' - Skeat's Old French forms are the -ache family; he does not use espinard for the English word.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"spinach\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English spinach is genuinely a French loan, but not from the box above it. It comes from the -ache form: late 14c. spinache, spinage (already late 13c. as a surname), from Anglo-French spinache / Old French espinache, espinage, espinace - which is exactly why English has -ach(e) and not -ard. Skeat p.507, the reference Nourai prints here, says so: 'Spinach, Spinage ... O. F. espinache, espinage, espinace. - Span. espinaca. - Arab. aspanakh, isfanaj; of Pers. origin (Devic)', and calls spinage 'a \\\"voiced\\\" form of spinach'. Etymonline routes the Old French word further back through Old Provencal espinarc and perhaps Catalan espinac to Andalusian Arabic isbinakh and Persian aspanakh. So the derivation English < French < Medieval Latin < Spanish < Arabic < Persian is right in outline, and only the French link is drawn through the wrong French variant. Nourai's second reference, AHD, has nothing on the word: Watkins' Indo-European appendix has no SPINACH entry at all, the word not being inherited.\",\n \"derivation_fa\": \"واژهٔ انگلیسی spinach به‌راستی وام‌واژه‌ای فرانسوی است، اما نه از جعبهٔ بالای خودش. این واژه از شاخهٔ ‎-ache آمده است: اواخر سدهٔ چهاردهم spinache و spinage (و پیش از آن در اواخر سدهٔ سیزدهم به عنوان نام خانوادگی)، از انگلونرمن spinache / فرانسهٔ کهن espinache، espinage، espinace — و دقیقاً به همین سبب است که انگلیسی ‎-ach(e) دارد نه ‎-ard. اسکیت در ص ۵۰۷ که ارجاع چاپ‌شدهٔ همین جعبه است می‌نویسد: «Spinach, Spinage ... O.F. espinache, espinage, espinace. — Span. espinaca. — Arab. aspanakh, isfanaj؛ فارسی‌الاصل (به نقل دِویک)» و spinage را صورت «واکدار‌شدهٔ» spinach می‌خواند. اتیمولوژی‌آنلاین فرانسهٔ کهن را از راه پرووانسی کهن espinarc و شاید کاتالان espinac به عربی اندلسی إسبناخ و فارسی «اسپناخ» می‌رساند. پس زنجیرهٔ انگلیسی ‹ فرانسه ‹ لاتین میانه ‹ اسپانیایی ‹ عربی ‹ فارسی در کلیات درست است و تنها حلقهٔ فرانسوی از گونهٔ نادرست کشیده شده. ارجاع دوم نورایی یعنی AHD در اینجا بی‌فایده است: پیوست ریشه‌های هندواروپایی واتکینز اصلاً مدخل SPINACH ندارد، چون این واژه موروثی نیست. حکم: با احتیاط پذیرفتنی.\",\n \"sources\": [E+\"spinach\", W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%A7%D8%AC\"],\n \"ref_check\": [\n   {\"ref\": \"SKT:507\", \"status\": \"supports\",\n    \"note\": \"SKT_dli_revised.txt, s.v. Spinach (the running page number 506 stands just above; the entry is on p.506-507): 'Spinach, Spinage, a vegetable. (F. - Span. - Arab. - Pers.) Spinage is a \\\"voiced\\\" form of spinach. O. F. espinache, espinage, espinace. - Span. espinaca. - Arab. aspanakh, isfanaj; of Pers. origin (Devic). The Ital. spinace and Span. espinaca are referred, by popular etymology, to L. spina, a thorn.'\"},\n   {\"ref\": \"AHD\", \"status\": \"not_found\",\n    \"note\": \"grep -o 'SPINACH[ ]*[a-zA-Z0-9-]*' AHD_watkins1985.txt returns nothing: Watkins' Indo-European appendix has no entry for SPINACH, since the word is a Wanderwort and not an inherited IE formation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat p.506-507\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1489\", \"stance\": \"partial\",\n    \"note\": \"'spinach, n. - MF. espinache, espinage (whence - with change of suff. - MF. espinarde, espinard, F. epinard)' - Klein too makes English spinach continue the -ache form, not espinard.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. spinach (archived)\", \"stance\": \"partial\",\n    \"note\": \"'late 14c., spinache, spinage ... from Anglo-French spinache, Old French espinache (14c., Modern French epinard, from a form with a different suffix), from Old Provencal espinarc, which perhaps is via Catalan espinac, from Andalusian Arabic isbinakh, from Arabic isbanakh, from Persian aspanakh \\\"spinach\\\".'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 126\", \"stance\": \"partial\",\n    \"note\": \"'engl. spinage' listed among the forms leaning on Latin spina.\"}\n ]\n})\n\nout[\"entries\"].append(e4)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-470.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-470.py"
}
```


### [2026-09-14T02:56:11.688Z] TOOL RESULT

```
written
```


## [2026-09-14T02:56:15.685Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-470.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 470"
}
```


### [2026-09-14T02:56:16.838Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 8, 'disputed': 5, 'confirmed': 3, 'transcription_suspect': 1}
root verdicts: {'plausible': 1, 'disputed': 1}
ref checks: {'supports': 12, 'partial': 5, 'not_checked': 3, 'contradicts': 2, 'not_found': 1}
books consulted: {'partial': 27, 'supports': 24, 'contradicts': 10, 'silent': 3} | by book: {'KLN': 11, 'LKT': 7, 'WEB': 5, 'BQT': 5, 'SKT': 5, 'PHD': 4, 'AHD': 4, 'NYB': 3, 'HUB': 3, 'ARY': 3, 'POK': 3, 'MON': 3, 'CHEUNG': 2, 'WLD': 2, 'BRT': 1, 'HRN': 1, 'IEC': 1, 'FVQ': 1}
```


## [2026-09-14T02:56:36.529Z] AGENT

Page 470 (book p. 440) verified — `data/verification/page-470.json`, `verify_check.py 470` reports 17/17 nodes, **0 PROBLEM lines**.

**Verdicts:** roots 1 plausible / 1 disputed; nodes 3 confirmed, 8 plausible, 5 disputed, 1 transcription_suspect. Ref checks: 12 supports, 5 partial, 2 contradicts, 1 not_found, 3 not_checked (ETM has no digital copy anywhere).

**Disputed / flagged**
- **Spinakion (root, entry 4)** — direction fully reversed. Spinach is an Iranian culture-word (*spināka- 'thorny', from *spin- 'thorn' < PIE *spey-); Byzantine Gk. σπινάκιον is itself borrowed from Medieval Latin ← Spanish ← Arabic ← Persian. Nourai's own source refutes him: Mo'in's footnote in Borhān-e Qāṭeʿ quotes al-Anṭākī, «اسفاناج معرّبٌ عن فارسیة هو اسباناخ».
- **#1 Arabic "spânâj"** — wrong direction, and not a possible Arabic form (no /p/, no initial cluster; the real forms are إسفاناج / إسباناخ with prosthetic ʾi-).
- **#2 Persian espenâx** — drawn as a loan *from* Arabic; Persian is the donor (Klein, Skeat, Lokotsch §126, Mo'in all agree).
- **#3 Greek sphaira** — Pokorny lists it only in parentheses with "?"; Watkins gives SPHERE no IE root; Beekes/Etymonline "of unknown origin". (σπαίρω in the same box is fine, so the node takes the worse verdict.)
- **#7 Pahlavi spihr / #8 Persian sepehr** — the Greek-loan route is Henning's minority view; Nyberg ("-h- would be an inorganic insertion, quite improbable"), Hübschmann §707/Nöldeke, Mo'in's BQT footnote (via Σπιθριδάτης) and Wiktionary all derive it from OP *spiθra- 'shining white'.

**Transcription_suspect (error in the BOOK, not the extraction)**
- **#4 Spanish "espinacia"** — printed page 440 shows *espinacia*; Klein (the box's own reference), Skeat and Lokotsch all have **espinaca**. Likely contaminated by the Medieval Latin *spinachia* below it. Page PNG archived at `data/verification/sources/refs/ocr/BOOK/470.png`.

**No extraction errors** — the JSON matches the printed page everywhere, including the empty French box.

Other notable corrections recorded in the file: Avestan *apa-spar* / *us-spar* are not attested (Bartholomae col. 1613 has only *fra-* and *vi-*; "us-spar" is Horn p.154's obsolete *us-* + √*par* analysis, which Horn himself calls "sehr unsicher"); Cheung splits *sparH* 'tread' from *spar* 'entrust', so «سپردن» straddles two roots; Nourai's own NOTE on *spring* is correct and modern scholarship sides with the note (Pok. 998 is *spergh-*, not "Spereg"); and English *spinach* comes from the *espinache* form, not *épinard*. 12 web pages archived via `fetch_source.py`.
