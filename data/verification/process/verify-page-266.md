# Verification process log — verify-page-266


## [2026-09-06T20:34:24.344Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 266 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-266.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-266.json. Write /home/sfmqrb/git/rishe/data/verification/page-266.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 266` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:34:25.515Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T20:34:26.241Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:34:26.256Z] TOOL RESULT

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


## [2026-09-06T20:34:26.846Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-266.txt"
}
```


### [2026-09-06T20:34:26.882Z] TOOL RESULT

```
1	=== PDF page 266 (book page 236) ===
2	--- entry 0 ---
3	ROOT [Mongolian] Khan : ruler  (refs KLN:844)
4	#1 (parent #0) [Turkish] refs=KLN:844 | khan : ruler
5	  #2 (parent #1) [Persian] refs=BQT:707; MON | xân «خان ( خانسامان ، خانم )» : sir, title of respect
6	    #3 (parent #2) [Arabic] refs=KLN:844 | xân
7	      #4 (parent #3) [English] refs=KLN:844 | khan : title of respect | NOTE: AHD claims "khan" entered English from Turkish through Latin & French
8	--- entry 1 ---
9	ROOT Kharpuna -> redirect to Kahrpu
10	--- entry 2 ---
11	ROOT Khei -> redirect to Ghei 1
12	--- entry 3 ---
13	ROOT [Mongolian] Khitan : an area in north west China  (refs KLN:251)
14	#1 (parent #0) [Persian] refs=BQT:715 | xotan «خُتَن ( خَتا ، خطا ، خطان )» : poetic name for China
15	#2 (parent #0) [Sogdian] refs=SOD:174 | ğwdnyk : Khotanese
16	#3 (parent #0) [Middle Latin] refs=KLN:251 | cataya
17	  #4 (parent #3) [English] refs=KLN:251 | Cathay, Khitan, Khotan : poetic names of China
18	--- entry 4 ---
19	ROOT [Arabic] K.h.l : very fine Antimony powder used for coloring eyelids.  (refs FVA:348; KLN:46)
20	#1 (parent #0) [Arabic] refs=FVA:348 | kohl : powder for coloring eyelids, also believed to cure certain eye diseases. ; kahhâl : eye doctor ; al-kahl, alkoŭl : highly purified spirits
21	  #2 (parent #1) [Persian] refs=FVA:348; MON:2919 | kohl «کُحل» : eye powder ; kahhâl «کَحّال» : eye doctor ; kohŭl «کحول» : alcohol
22	  #3 (parent #1) [Latin] refs=KLN:46 | alcohol : spirit of wine
23	    #4 (parent #3) [French] refs=None | alcool
24	      #5 (parent #4) [Persian] refs=MON:342 | alkol «الکل» : alcohol
25	    #6 (parent #3) [English] refs=KLN:46; AHD:30 | alcohol
26	--- entry 5 ---
27	ROOT Ki 1 -> redirect to Kei 2
28	
```


## [2026-09-06T20:34:27.359Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-266.json"
}
```


### [2026-09-06T20:34:27.378Z] TOOL RESULT

```
1	{
2	  "pdf_page": 266,
3	  "book_page": 236,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Khan",
8	        "lang": "Mongolian",
9	        "refs": "KLN:844",
10	        "gloss": "ruler"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Turkish",
17	          "refs": "KLN:844",
18	          "words": [
19	            {"translit": "khan", "gloss": "ruler", "script": null}
20	          ],
21	          "script_extra": null,
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "BQT:707; MON",
30	          "words": [
31	            {"translit": "xân", "gloss": "sir, title of respect", "script": "خان ( خانسامان ، خانم )"}
32	          ],
33	          "script_extra": null,
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 2,
40	          "lang": "Arabic",
41	          "refs": "KLN:844",
42	          "words": [
43	            {"translit": "xân", "gloss": null, "script": null}
44	          ],
45	          "script_extra": null,
46	          "note": null,
47	          "quote": null
48	        },
49	        {
50	          "id": 4,
51	          "parent": 3,
52	          "lang": "English",
53	          "refs": "KLN:844",
54	          "words": [
55	            {"translit": "khan", "gloss": "title of respect", "script": null}
56	          ],
57	          "script_extra": null,
58	          "note": "AHD claims \"khan\" entered English from Turkish through Latin & French",
59	          "quote": null
60	        }
61	      ]
62	    },
63	    {
64	      "root": {"name": "Kharpuna", "redirect": "Kahrpu"},
65	      "nodes": []
66	    },
67	    {
68	      "root": {"name": "Khei", "redirect": "Ghei 1"},
69	      "nodes": []
70	    },
71	    {
72	      "root": {
73	        "name": "Khitan",
74	        "lang": "Mongolian",
75	        "refs": "KLN:251",
76	        "gloss": "an area in north west China"
77	      },
78	      "nodes": [
79	        {
80	          "id": 1,
81	          "parent": 0,
82	          "lang": "Persian",
83	          "refs": "BQT:715",
84	          "words": [
85	            {"translit": "xotan", "gloss": "poetic name for China", "script": "خُتَن ( خَتا ، خطا ، خطان )"}
86	          ],
87	          "script_extra": null,
88	          "note": null,
89	          "quote": {
90	            "text": "دو چشم شوخ تو بر هم زده ختا و ختن - بچین زلف تو ماچین و هند داده خراج",
91	            "poet": "Hâfez"
92	          }
93	        },
94	        {
95	          "id": 2,
96	          "parent": 0,
97	          "lang": "Sogdian",
98	          "refs": "SOD:174",
99	          "words": [
100	            {"translit": "ğwdnyk", "gloss": "Khotanese", "script": null}
101	          ],
102	          "script_extra": null,
103	          "note": null,
104	          "quote": null
105	        },
106	        {
107	          "id": 3,
108	          "parent": 0,
109	          "lang": "Middle Latin",
110	          "refs": "KLN:251",
111	          "words": [
112	            {"translit": "cataya", "gloss": null, "script": null}
113	          ],
114	          "script_extra": null,
115	          "note": null,
116	          "quote": null
117	        },
118	        {
119	          "id": 4,
120	          "parent": 3,
121	          "lang": "English",
122	          "refs": "KLN:251",
123	          "words": [
124	            {"translit": "Cathay, Khitan, Khotan", "gloss": "poetic names of China", "script": null}
125	          ],
126	          "script_extra": null,
127	          "note": null,
128	          "quote": null
129	        }
130	      ]
131	    },
132	    {
133	      "root": {
134	        "name": "K.h.l",
135	        "lang": "Arabic",
136	        "refs": "FVA:348; KLN:46",
137	        "gloss": "very fine Antimony powder used for coloring eyelids."
138	      },
139	      "nodes": [
140	        {
141	          "id": 1,
142	          "parent": 0,
143	          "lang": "Arabic",
144	          "refs": "FVA:348",
145	          "words": [
146	            {"translit": "kohl", "gloss": "powder for coloring eyelids, also believed to cure certain eye diseases.", "script": null},
147	            {"translit": "kahhâl", "gloss": "eye doctor", "script": null},
148	            {"translit": "al-kahl, alkoŭl", "gloss": "highly purified spirits", "script": null}
149	          ],
150	          "script_extra": null,
151	          "note": null,
152	          "quote": null
153	        },
154	        {
155	          "id": 2,
156	          "parent": 1,
157	          "lang": "Persian",
158	          "refs": "FVA:348; MON:2919",
159	          "words": [
160	            {"translit": "kohl", "gloss": "eye powder", "script": "کُحل"},
161	            {"translit": "kahhâl", "gloss": "eye doctor", "script": "کَحّال"},
162	            {"translit": "kohŭl", "gloss": "alcohol", "script": "کحول"}
163	          ],
164	          "script_extra": null,
165	          "note": null,
166	          "quote": {
167	            "text": "ای بر زعرشت پایگه ، برسرکشان رانده سپه - درچشم خضر از گرد ره ، کحل مسیحا ریخته",
168	            "poet": "Vahshî"
169	          }
170	        },
171	        {
172	          "id": 3,
173	          "parent": 1,
174	          "lang": "Latin",
175	          "refs": "KLN:46",
176	          "words": [
177	            {"translit": "alcohol", "gloss": "spirit of wine", "script": null}
178	          ],
179	          "script_extra": null,
180	          "note": null,
181	          "quote": null
182	        },
183	        {
184	          "id": 4,
185	          "parent": 3,
186	          "lang": "French",
187	          "refs": null,
188	          "words": [
189	            {"translit": "alcool", "gloss": null, "script": null}
190	          ],
191	          "script_extra": null,
192	          "note": null,
193	          "quote": null
194	        },
195	        {
196	          "id": 5,
197	          "parent": 4,
198	          "lang": "Persian",
199	          "refs": "MON:342",
200	          "words": [
201	            {"translit": "alkol", "gloss": "alcohol", "script": "الکل"}
202	          ],
203	          "script_extra": null,
204	          "note": null,
205	          "quote": null
206	        },
207	        {
208	          "id": 6,
209	          "parent": 3,
210	          "lang": "English",
211	          "refs": "KLN:46; AHD:30",
212	          "words": [
213	            {"translit": "alcohol", "gloss": null, "script": null}
214	          ],
215	          "script_extra": null,
216	          "note": null,
217	          "quote": null
218	        }
219	      ]
220	    },
221	    {
222	      "root": {"name": "Ki 1", "redirect": "Kei 2"},
223	      "nodes": []
224	    }
225	  ]
226	}
227	
```


## [2026-09-06T20:34:32.787Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T20:34:32.832Z] TOOL RESULT

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
```


## [2026-09-06T20:34:35.132Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVA','FVQ','MON','BQT','SOD','AHD','ARY','PHD','NYB','HRN','HUB','PLA','AFM','LKT','SKT','WEB','FSD','TTS','HJB','DOZ','DEV','LAM','PHN','AFA']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600])\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-06T20:34:37.275Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start wit
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
```


## [2026-09-06T20:34:42.617Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1)[:2000])\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:2500])\nprint(json.dumps(d['SOD'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T20:34:44.541Z] TOOL RESULT

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
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check
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
  "/home/sfmqrb/git/rishe/data/
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
```


## [2026-09-06T20:34:49.767Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n '^khan,' KLN_1966.txt KLN_1971.txt\necho ---\ngrep -n '^Cathay' KLN_1966.txt KLN_1971.txt\necho ---\ngrep -n '^alcohol,' KLN_1966.txt KLN_1971.txt\necho ---\ngrep -n '^kohl,' KLN_1966.txt KLN_1971.txt\necho ---\ngrep -n '^alkali,' KLN_1966.txt KLN_1971.txt"
}
```


### [2026-09-06T20:34:49.904Z] TOOL RESULT

```
KLN_1971.txt:21603:khan, ‘caravanserai’. 
KLN_1971.txt:131057:khan, n., a title of ruler in Mohammedan coun- 
KLN_1971.txt:131061:khan, n., a caravanserai. — Pers. and Arab, khan , 
---
KLN_1971.txt:41404:Cathay, n., poetic name of China. — ML. Ca - 
KLN_1966.txt:6804:Cathay,  n.,  poetic  name  of  China.  —  ML.  Ca- taya,  fr.  Khitai,  the  name  of  a  Tatar  kingdom (the  kingdom  of  the  Khitan  Tatars).  Cp.
---
KLN_1971.txt:10656:alcohol, n. — ML., fr. Arab, al-kohl, vulgar pro- 
---
KLN_1971.txt:132079:kohl, n., powder (esp. of antimony), used by East- 
---
KLN_1971.txt:11377:alkali, n. — F. alcalli (now spelled alcali), fr.
```


## [2026-09-06T20:34:50.813Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i 'cathay' KLN_1966.txt | head -20\necho === LKT\ngrep -n -i 'chan\\b\\|Khan' LKT.txt | head -30"
}
```


### [2026-09-06T20:34:50.883Z] TOOL RESULT

```
Exit code 1
6804:Cathay,  n.,  poetic  name  of  China.  —  ML.  Ca- taya,  fr.  Khitai,  the  name  of  a  Tatar  kingdom (the  kingdom  of  the  Khitan  Tatars).  Cp.
20651:Khitan,  adj.  and  n.,  Tatar.  —  Lit.  ‘of  the  king¬ dom  of  the  Khitans’,  fr.  Khitai,  name  of  a  Tatar kingdom.  See  Cathay.
(eval):3: == not found
```


## [2026-09-06T20:34:55.462Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6800,6812p' KLN_1966.txt\necho === khitan\nsed -n '20648,20656p' KLN_1966.txt\necho === khan\ngrep -n 'khan,' KLN_1966.txt | head -20\necho === alcohol\ngrep -n 'alcohol,\\|al-kohl\\|alkuhl\\|al-kuhl' KLN_1966.txt | head -20\necho === kohl\ngrep -n 'kohl,' KLN_1966.txt | head"
}
```


### [2026-09-06T20:34:55.548Z] TOOL RESULT

```
Exit code 1
Catharist,  n.,  a  member  of  any  of  various  sects aiming  at  purity  ( Eccles .  hist.)  —  ML.  Catha- rista,  fr.  Eccles.  Gk.  xaf>apumf)<;,  fr.  Gk.  xaffa- poc ,  ‘pure,  clean’;  cp.  Gk.  xaffapiaTYip,  ‘tree pruner’,  and  see  next  word.  For  the  ending  see suff.  -ist.
catharsis,  n.,  i)  purgation  ( med.)\  2)  purification of  the  emotions  by  art.  —  ModL.,  fr.  Gk.  xaffxp- csi.q,  ‘cleansing,  purification’,  from  the  stem  of xaffalpeLv,  ‘to  cleanse,  purify;  to  prune  (a  tree)’, fr.  xaffap6p,  ‘clean,  pure’,  which  is  of  uncertain origin.  Cp.  cathartic,  Catherine,  acatharsia.
cathartic,  cathartical,  adj.,  cleansing,  purifying. —  Gk.  xoefrap-uxo?,  ‘fit  for  cleansing’,  from  the stem  of  xaffalpstv.  See  prec.  word.
Derivatives:  cathartical-ly,  adv.,  cathartical- ness,  n.
Cathay,  n.,  poetic  name  of  China.  —  ML.  Ca- taya,  fr.  Khitai,  the  name  of  a  Tatar  kingdom (the  kingdom  of  the  Khitan  Tatars).  Cp.
Khitan.
cathedra,  n.,  the  seat  of  a  bishop.  —  L.,  fr.  Gk. xaffcSpa.  See  chair  and  cp.  ex  cathedra.
cathedral,  n.  —  ML.  cathedralis,  short  for  ecclesia cathedralis,  ‘church  pertaining  to  the  seat  of  a bishop’,  fr.  cathedra.  See  prec.  word  and  adj. suff.  -al.
Catherine,  Catharine,  also  Katherine,  Katharine,
fern.  PN.  —  F.  Catherine,  fr.  L.  Ecaterina,  Kate¬ rina,  fr.  Gk.  AixaTeptvT)  (whence  also  Russ. Ekaterina).  The  later  L.  spelling  Katharina  is due  to  a  connection  with  Gk.  xaftapop,  ‘pure’, the  supposed  origin  of  the  name.
Catherine  wheel.  —  So  called  from  the  spiked wheel  with  which  St.  Catherine  of  Alexandria was  tortured.
catheter,  n.,  a  surgical  instrument  used  to  draw off  fluid  from  body  cavities.  —  Late  L.,  fr.  Gk. xaffETTjp,  ‘something  let  down;  surgical  instru¬ ment  for  emptying  the  bladder’,  from  the  stem of  xalHivai,  ‘to  send  down’,  fr.  xa-rd  (see  cata-) and  isvai,  ‘to  move  forward,  throw,  send’, which  stands  for  *yi-ye-nai  and  is  cogn.  with L .jacere,  ‘to  throw’.  See  jet,  ‘to  spirt  forth’,  and cp.  synesis.
Derivatives:  catheter-ism,  n.,  catheter-ize,  tr.  v., catheter-iz-ation,  n.
(eval):3: == not found
```


## [2026-09-06T20:35:00.642Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20648,20656p' KLN_1966.txt\necho \"--- khan\"\ngrep -n 'khan,' KLN_1966.txt | head -20\necho \"--- alcohol\"\ngrep -n 'alcohol,\\|al-kohl\\|alkuhl\\|al-kuhl\\|alkoll' KLN_1966.txt | head -20\necho \"--- kohl\"\ngrep -n 'kohl,' KLN_1966.txt | head"
}
```


### [2026-09-06T20:35:00.754Z] TOOL RESULT

```
khansamah,  n.,  a  butler  {India).  —  Hind,  khan- sdman,  fr.  Pers.  khansamdn,  lit.  ‘lord  of  stores’, fr.  khan,  ‘lord’  (see  khan,  ‘title  of  ruler’),  and sdman,  ‘stores,  household’, khedive,  n.,  title  of  the  Turkish  viceroy  of  Egypt (hist.)  —  F.  khedive,  fr.  Turk,  khidiv,  fr.  Pers. khidiw,  ‘prince’,  a  derivative  of  khuda,  ‘master, prince’.
Derivatives;  khediv-al,  khedivi-al,  adjs.,  khe- divi-ate ,  n.
khidmatgar,  khidmutgar,  n.,  a  male  waiter  {In¬ dia).  —  Hind,  khidmatgar,  fr.  Pers.  khidmatgar, a  hybrid  formed  fr.  Arab.  khidmah,  ‘service’  (fr. khadama,  ‘he  served’),  with  Pers.  suff.  -gar, ‘holder,  owner’.
Khitan,  adj.  and  n.,  Tatar.  —  Lit.  ‘of  the  king¬ dom  of  the  Khitans’,  fr.  Khitai,  name  of  a  Tatar kingdom.  See  Cathay.
khoja,  khojah,  n.,  a  title  of  respect  in  Persia,  In¬ dia  and  Turkestan.  —  Turk,  khojah,  fr.  Pers. khwajah.
kibbutz,  n.,  a  collective  agricultural  settlement  in Israel.  —  Heb.  qibbhtz,  lit.  ‘gathering,  assem¬ blage’,  prop,  verbal  noun  of  qibhftz,  ‘he  gather¬ ed,  gathered  together’,  Pi‘el  of  qabhatz,  ‘he gathered’;  rel.  to  Arab,  qahada,  ‘he  grasped, seized’,
kibe,  n.,  chillblain.  —  ME.  kybe.  Cp.  W.  cibi, cibiost,  ‘chillblain’.
kibitzer,  n.,  t)  looker-on  at  a  card-game;  2)  a meddlesome  person.  —  G.  Kiebitzer  (slang),  ‘a looker-on  (at  cards)’,  fr.  kiebitzen,  ‘to  look  on’, fr.  Kiebitz,  ‘pewit,  plover’,  whence  arose  the meaning  (used  only  in  slang)  ‘a  meddlesome looker  on’.  The  birdname  Kiebitz  derives  fr. MHG.  gibi. 5,  giwis,  which  is  of  imitative  origin. Cp.  MLG.  kivit,  MDu.,  Du.  kievit,  ‘plover’,  and E.  pewit,  which  all  are  imitative, kiblah,  n.,  the  point  toward  which  the  Moham¬ medans  turn  in  prayer  (i.e.  the  Kaaba  in Mecca).  —  Arab.  qiblah,  ‘direction  to  which Mohammedans  turn  in  prayer’,  fr.  qabila,  ‘he lay  opposite,  was  in  front  of’.  See  cabal  and cp.  Kabyle.
kibosh,  n.,  in  the  phrase  to  put  the  kibosh  on,  ‘to put  an  end  to’.  —  Of  unknown  origin, kick,  intr.  and  tr.  v.,  to  strike  with  the  foot.  — ME.  kiken,  of  unknown  origin,  Cp.  kicksies. Derivatives:  kick,  n.,  a  blow  with  the  foot, kick-er,  n.
--- khan
3753:Astragalus,  n.,  a  genus  of  plants  of  the  pea  family (bot.)  —  L.  See  astragal, astrakhan,  astrachan,  n.,  the  fur  of  still-born  or young  lambs  from  Astrakhan.  —  From  As¬ trakhan  in  Russia.  The  name  of  the  city  lit. means  ‘star  of  the  caravanserai’.  See  astral  and khan,  ‘caravanserai’.
20647:which  is  rel.  to  Heb.  hamishshtm,  Aram.-Syr. hamshtn,  Akkad,  hamshdti,  ‘fifty’, khan,  n.,  a  title  of  ruler  in  Mohammedan  coun¬ tries.  —  Pers.  and  Arab,  khan,  ‘lord,  prince’,  fr. Turki  khan,  contraction  of  khaqan,  ‘ruler, sovereign’,  which  is  prob.  of  Mongolian  origin, khan,  n.,  a  caravanserai.  —  Pers.  and  Arab,  khan, ‘caravanserai,  inn’.  Cp.  astrakhan, khanate,  n.,  a  district  ruled  by  a  khan.  —  A hybrid  coined  fr.  khan,  ‘title  of  ruler’,  and  -ate, a  suffix  of  Latin  origin.
20648:khansamah,  n.,  a  butler  {India).  —  Hind,  khan- sdman,  fr.  Pers.  khansamdn,  lit.  ‘lord  of  stores’, fr.  khan,  ‘lord’  (see  khan,  ‘title  of  ruler’),  and sdman,  ‘stores,  household’, khedive,  n.,  title  of  the  Turkish  viceroy  of  Egypt (hist.)  —  F.  khedive,  fr.  Turk,  khidiv,  fr.  Pers. khidiw,  ‘prince’,  a  derivative  of  khuda,  ‘master, prince’.
34005:schatchen,  n.,  a  marriage  broker.  —  Yiddish,  fr. ModHeb.  shaddekhan,  fr.  Mishnaic  Heb.  shid- dekh,  ‘he  negotiated  or  arranged  a  marriage’, lit.  ‘he  quieted,  appeased,  pacified’,  rel.  to  Aram. sffdakh,  ‘he  was  appeased,  quiet’,  shaddekh,  ‘he appeased,  quieted’.
34942:Shekinah,  Schechinah,  n.,  the  Divine  Presence.  — Mishnaic  Heb.  shikhinah,  ‘dwelling  place  (of God)’,  from  the  base  of  shakhan,  ‘he  dwelled, abode’,  which  is  rel.  to  Aram. -Syr.  shfkhen, Arab,  sakuna,  ‘he  dwelled’,  Akkad,  shakanu,  ‘to lay,  set,  deposit’  (whence  mashkanu,  ‘dwelling place;  place;  deposit’).  All  these  verbs  are  prop. Shaph'el  (=  causative)  forms  of  the  Sem.  base k-w-n,  ‘to  stand  firm,  to  be",  and  orig.  meant  ‘he caused  to  stand,  caused  to  be  established’.
--- alcohol
2136:Alcmene,  n.,  the  mother  of  Hercules  ( Greek mythol.)  —  L„  fr.  Gk.  ’AXxp.f)VTr),  lit.  ’the  strong one’,  fr.  aXxf),  ’strength,  power’.  See  Alexander, alcohol,  n.  —  ML.,  fr.  Arab,  al-kohl ,  vulgar  pro¬ nunciation  of  al-kuhl,  fr.  a/-,  the  ,  and  kohl, resp.  kuhl,  ‘antimony  (used  for  painting  the  eye¬ lids)’,  which  is  rel.  to  Heb.  kahal  (Ezek.  23.40), ‘he  painted  the  eyelids  with  antimony’,  Aram.- Syr.  kfhal,  Ethiop.  kahala,  of  s.m.,  Aram. kuhld,  Ethiop.  kuhel,  ‘antimony’.  (Akkad,  guhlu, ‘antimony’,  is  prob.  a  WSem.  loan  word.)Its  mod¬ em  sense  (‘highly  rectified  spirits’)  is  due  to  the analogy  of  the  fineness  of  this  powder.  Cp.  kohl. Derivatives:  alcohol-ic,  adj.,  alcohol-ic-ally , adv.,  alcohol-ism ,  n.,  alcohol-ize ,  tr.  v. alcoholometer,  n.,  an  instrument  for  measuring the  alcoholic  strength  of  liquids.  —  A  hybrid coined  fr.  alcohol  and  Gk.  pixpov,  ‘measure’. See  meter,  ‘poetical  rhythm  .
5695:bromal,  n.,  a  colorless,  oily  fluid,  CBr3COH (chem.)  —  Abbreviation  of  bromine  and  alcohol, bromate,  n.,  a  salt  of  bromic  acid  (chem.)  —  See brom-  and  chem.  suff.  -ate. brome,  n.,  also  brome  grass.  —  Gk.  [Ipouop,  ‘wild oats’.  See  Bromus.
13540:crgosterol,  n„  an  alcohol,  C28H440,  occurring  esp. in  ergot  and  yeast  ( biochem .)  —  Compounded of  ergot  and  sterol.
13702:estriol,  n.,  a  crystalline  estrogenic  hormone C18H2403  (biochem.)  —  Coined  fr.  estrus  and -ol,  a  suff.  denoting  alcohol, estrogen,  n.(  a  substance  producing  estrus  (bio¬ chem.)  —  Coined  fr.  estrus  and  -gen. estrogenic,  adj.,  producing  estrus  (biochem.)  — Coined  fr.  estrus  and  -genic, estrone,  n.,  a  female  sex  hormone;  theelin  (bio¬ chem.)  —  Coined  fr.  estrus  and  suff.  -one. estrus,  oestrus,  n.,  1)  a  vehement  desire,  frenzy; 2)  the  sexual  heat  of  female  mammals.  —  L. oestrus,  ‘gadfly;  frenzy’,  fr.  Gk.  oXa-tpoq,  ‘gad¬ fly;  sting;  frenzy’,  which  is  cogn.  with  Lith. aistra,  ‘violent  passion’,  and  prob.  also  with L.  ira,  ‘anger’.  See  ire  and  cp.  the  first  element in  Oestrelata.
16344:of  animals  (chem.)  —  Coined  by  the  French physiologist  Claude  Bernard  (1813-78)  in  1848 from  Gk.  y Xuxiig,  ‘sweet’  (see  glyco-),  and  -gen. glycol,  n.,  an  alcoholic  liquid,  regarded  as  inter¬ mediate  between  glycerin  and  ethyl  alcohol, C2H4(OH)2  (chem.)  —  Formed  fr.  glycferine) and  (alcoh)ol.  Derivative:  glycol-ic,  adj. glyconic,  adj.,  pertaining  to  a  monoacid,  C6H,20, (chem.)  —  See  glycose  and  -onic.
23742:-meter,  -metre,  combining  form  denoting  a  spec¬ ified  multiple  or  fraction  of  a  meter  (e.g.  kilo¬ meter,  lit.  ‘a  thousand  meters’,  millimeter,  lit. ‘the  thousandth  part  of  a  meter’.  —  F.  -metre, fr.  mitre.  See  meter,  ‘unit  of  length’, meth-,  form  of  metho-  before  a  vowel, methane,  n.,  a  highly  inflammable  hydrocarbon, CH4  ( chem .)  —  See  methyl  and  -ane. methanol,  n.,  an  inflammable  poisonous  liquid, CH3OH  (chem.)  —  Coined  fr.  methane  and  -ol, a  suff.  denoting  an  alcohol, metheglin,  n.,  a  drink  made  of  fermented  honey. —  W.  meddyglyn,  compounded  of  meddyg, ‘physician’  (fr.  L.  medicus,  see  medical),  and llyn,  ‘juice’.
28716:phytol,  n.,  an  oily  alcohol,  C20H3,OH,  first  isolat¬ ed  from  chlorophyll  by  the  German  chemist Richard  Willstatter  (1872-1942)  (chem.)  — Coined  fr.  phyt-  and  -ol,  a  suff.  denoting  alcohol. phytology,  n.  —  Another  name  for  botany;  lit. ‘the  study  of  plants’,  compounded  of  phyto-  and Gk.  -Xoyla,  fr.  -X6yo;,  ‘one  who  speaks  (in  a certain  manner);  one  who  deals  (with  a  certain topic)’.  See  -logy.
35956:sorbitol,  also  sorbite,  n.,  an  alcohol,  C6H14Oe (chem.)  —  Sec  sorb,  subst.  suff.  -ite  and  suff.  -ol.
--- kohl
2136:Alcmene,  n.,  the  mother  of  Hercules  ( Greek mythol.)  —  L„  fr.  Gk.  ’AXxp.f)VTr),  lit.  ’the  strong one’,  fr.  aXxf),  ’strength,  power’.  See  Alexander, alcohol,  n.  —  ML.,  fr.  Arab,  al-kohl ,  vulgar  pro¬ nunciation  of  al-kuhl,  fr.  a/-,  the  ,  and  kohl, resp.  kuhl,  ‘antimony  (used  for  painting  the  eye¬ lids)’,  which  is  rel.  to  Heb.  kahal  (Ezek.  23.40), ‘he  painted  the  eyelids  with  antimony’,  Aram.- Syr.  kfhal,  Ethiop.  kahala,  of  s.m.,  Aram. kuhld,  Ethiop.  kuhel,  ‘antimony’.  (Akkad,  guhlu, ‘antimony’,  is  prob.  a  WSem.  loan  word.)Its  mod¬ em  sense  (‘highly  rectified  spirits’)  is  due  to  the analogy  of  the  fineness  of  this  powder.  Cp.  kohl. Derivatives:  alcohol-ic,  adj.,  alcohol-ic-ally , adv.,  alcohol-ism ,  n.,  alcohol-ize ,  tr.  v. alcoholometer,  n.,  an  instrument  for  measuring the  alcoholic  strength  of  liquids.  —  A  hybrid coined  fr.  alcohol  and  Gk.  pixpov,  ‘measure’. See  meter,  ‘poetical  rhythm  .
20824:Koh-i-noor,  n.,  a  famous  diamond,  one  of  the British  crown  jewels.  —  Pers.  koh-i-nur,  lit. ‘mountain  of  light’,  prop,  a  hybrid  coined  fr. Pers.  koh,  ‘mountain’,  which  is  rel.  to  Pers. kohe,  ‘hump’,  OPers.  kaufa-,  ‘mountain’,  Aves- tic  kaofa-,  ‘mountain,  hump’,  and  fr.  Arab. nur,  ‘light’  (see  Menorah). kohl,  n.,  powder  (esp.  of  antimony),  used  by  East¬ ern  women  to  darken  the  eyelids.  —  Arab. kuhl.  See  alcohol.
```


## [2026-09-06T20:35:06.277Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport io\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\ntargets={2136:'alcohol',6804:'Cathay',20647:'khan',20651:'Khitan',20824:'kohl'}\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i in targets:\n        print(targets[i],'line',i,'leaf(0-based)',leaf,'-> approx printed pages', 2*(leaf-12), 2*(leaf-12)+1)\n    leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-06T20:35:08.074Z] TOOL RESULT

```
alcohol line 2136 leaf(0-based) 35 -> approx printed pages 46 47
Cathay line 6804 leaf(0-based) 143 -> approx printed pages 262 263
khan line 20647 leaf(0-based) 455 -> approx printed pages 886 887
Khitan line 20651 leaf(0-based) 455 -> approx printed pages 886 887
kohl line 20824 leaf(0-based) 458 -> approx printed pages 892 893
```


## [2026-09-06T20:35:23.404Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor n in (35,143,455,458):\n    print('=== leaf',n)\n    print(leaves[n][:300].replace('\\n',' | '))\n    print('...TAIL...',leaves[n][-200:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T20:35:29.451Z] TOOL RESULT

```
=== leaf 35
,  n.,  son  of  Neleus  and  brother  of  Nestor in  Greek  mythology;  fig.  used  in  the  sense  of  an avenging  spirit.  —  Gk.  ’  AXacrrap,  lit .  ‘wanderer’, a  derivative  of  dXao&ai,  ‘to  wander,  roam’.  See hallucinate  and  cp.  the  first  element  in  Aleo- chara. | alas  trim,  n.,
...TAIL...  ‘young  man’,  &Xxp.ap£s  (neut.) (ibidem),  ‘strong,  powerful’. | Alcmene,  n.,  the  mother  of  Hercules  ( Greek mythol.)  —  L„  fr.  Gk.  ’AXxp.f)VTr),  lit.  ’the  strong one’,  fr.  aXxf),  ’s
=== leaf 143
,  ‘to  rob’). | Derivative:  caterpillar,  intr.  v. caterwaul,  intr.  v.  —  ME.  caterwrawen,  cater- wawen,  fr.  LG.  katerwaulen,  ‘to  cry  like  cats’, fr.  kater,  ‘male  cat’,  and  wauten,  ‘to  cry'.  The first  element  is  rel.  to  MLG..  MDu.  kalte,  ‘cat’; see  cat.  The  second  el
...TAIL... ing,  stormy’,  OSlav. severu,  'north  wind’,  Goth,  skura  ( windis ), ‘storm’,  OE.  scur,  ‘shower’.  See  shower, causalgia,  n.,  a  burning  sensation  (tried.)  —  Medi¬ cal  L.,  lit.  ‘a  b
=== leaf 455
‘stalk,  blade’, Lett,  zeiju,  ziet,  ‘to  rise’  (said  of  flowers;  also fig.)  See  chine,  ‘valley’,  and  chink,  ‘crack’. | key,  tr.  and  intr.  v.  —  ME.  keyen ,  fr.  key ,  keye, ‘key’.  See  key,  n. key,  n.  —  A  var.  of  quay. | Keziah,  i)  fern.  PN.;  2)  in  the  Bible,  one  of
...TAIL... uce’. Cp.  Cain,  Elkanah. | kinchin,  n.,  child.  —  Corrupted  fr.  G.  Kindchen, ‘little  child’,  dimin.  of  Kind,  ‘child’,  which  is  rel. to  ON.  kundr,  ‘son’.  See  kin  and  -kin. kincob, 
=== leaf 458
f  a  small  hill.  —  ME.  knot,  fr.  OE. cnoll,  ‘hill  top,  hill’,  rel.  to  ON.  knollr,  ‘hilltop’, MLG.,  MHG.,  G.  knolie,  ‘clod,  glebe,  lump', Du.  knot,  ‘turnip’,  and  to  OHG.  nollo,  Du.  nol, ‘a  hill’. | Derivative:  knoll-y,  adj. | knoll,  tr.  and  intr.  v.,  to  knell,  ring.
...TAIL... r.  MHG.  kriuzer, fr.  kriuze,  ‘cross’ ;  so  called  from  the  figure  of  a cross  stamped  upon  it.  See  cross  and  -er. kriegspiel,  n.,  a  war  game.  —  G.  Kriegsspiel,  lit. ‘war  game’
```


## [2026-09-06T20:35:46.739Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('total leaves',len(leaves))\nfor n in (437,438,439,440,441,442,443):\n    print('=== leaf',n, leaves[n][:150].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T20:35:48.373Z] TOOL RESULT

```
total leaves 903
=== leaf 437   -ory fr.  L.  invocatus,  pp.  of  invocare.  See  invoke, invoice,  n.  —  Fr.  earlier  invoyes,  pi.  of  obsolete invoy,  ‘anything  sent’,  fr.
=== leaf 438  —  ModL.,  fr.  Gk.  eEpeauovr),  ‘a wreath  of  olive  wound  round  with  wool’,  fr. slpo q,  ‘wool’,  which  is  rel.  to  gpiov,  ‘wool’  (see e
=== leaf 439 e,  adj.  —  Formed  with  suff.  -ive  fr.  L. | irrigatus,  pp.  of  irrigare.  See  irrigate, irriguous,  adj.,  moist,  irrigated.  —  L.  irriguus,
=== leaf 440 te,  ‘to  anger’,  and -able.  Derivatives :  irritabl-y,  adv.,  irritabil-ity,  n. irritancy,  n. ,  the  state  of  being  irritating.  —  Form¬ ed
=== leaf 441 timulate,  stir  up,  provoke’, prob.  freq.  of  *ir-ri-re,  ‘to  stir  up,  excite’,  fr. in-,  in’,  and  I.-E.  base  *erei-,  ‘to  set  in  motio
=== leaf 442 ains  in the  hip’,  compounded  of  Gk.  EoxEov,  ‘hipjoint’, and  itXyo ?,  ‘pain’.  See  ischium  and  -algia. ischiatic,  adj.,  ischial.  —  ML. 
=== leaf 443   represents  1)  OF. -aison  (fr.  L.  ationem,  fr.  -atus,  pp.  suff.  of  verbs in  -are)',  2)  OF.  -eison  (fr.  L.  -etionem,  fr,  - etus ,
```


## [2026-09-06T20:36:15.449Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nimport re\nfor i,l in enumerate(leaves[:20]):\n    print(i, repr(l[:90]))\nEOF"
}
```


### [2026-09-06T20:36:18.041Z] TOOL RESULT

```
0 'A  COMPREHENSIVE ETYMOLOGICAL  DICTIONARY\nOF  THE\nENGLISH  LANGUAGE\nDealing  with  the  or'
1 'ELSEVIER  PUBLISHING  COMPANY 335  JAN  VAN  GALEN STRAAT,  P.O.  BOX  211,  AMSTERDAM\nAME'
2 '\nPreface\nTo  know  the  origin  of  words is  to  know  the  cultural  history  of  mankin'
3 '  work.\nVIII\nMy  grateful  acknowledgements  are  also  due  to  the  whole  staff  of  th'
4 '  but  the  origin  of  the  respec-\nX\ntive  word  is  referred  to  by  such  vague  term'
5 'Theo- phile-Hyacinthe  Laennec  (1781-1826)  fr.  Gk.  xippo?,  ‘tawny’,  which  is  of  u'
6 'a  slight  aspira¬ tion  of  the  sound  - like  gh;  now  pro¬ nounced  like  g  in  get.'
7 'he  letters  17  .  D  ,  3  1  >  3  ,  to  indicate  their\noriginal  hard  pronunciation'
8 " ss  in English  hiss\nJ*\ndad\nd\npalatal  d\ns>\nta\n1\nan  emphatic  t\nJ;\nza'\nz\nan  emphatic  z"
9 'Auflage  von  J.  B.  Hofmann,  Heidelberg,  1938-55.\nWalde-Pokorny,  VWIS.  =  Walde,  A.'
10 'before  the  common  era\ndiet.\ndictionary\nBerb.\nBerber\ndimin.\ndiminutive\nBibl.\nBiblical\nDo'
11 'abinic\nOld  Sabinic\nOSerb.\nOld  Serbian\nOSlav.\nOld  Slavic\nOSp.\nOld  Spanish\nOsset.\nOsseti'
12 'an\nRepublics\nRuss.\nRussian\nV.\nverb\nS.\nSouth\nvar.\nvariant\nS.Afr.\nSouth  African\nveter.\nvete'
13 '  L.  bassus,  ‘thick,  fat, low’.  See  base,  ‘low’,  and  cp.  the  second  element in '
14 'nt,  efficient,  elicit,  exhibit,  Illicium,  inci¬ dent,  incipient,  inhibit,  inimical'
15 '  and  -facient. abortion,  n.,  miscarriage.  —  L.  abortio,  gen.  -onis, ‘miscarriage,'
16 ' (see  ab-),  and  tenere,  ‘to hold’.  See  tenable  and  cp.  appertain,  contain, detai'
17 '  ‘mite’. See  acarid.\naeariatre,  adj.,  bad-tempered.  —  F.,  ‘contrary, crabbed,  quar'
18 '��to  cry  out  at’.\nfr.  ad-  and  clamare,  ‘to  cry  out’.  See  claim  and cp.  declai'
19 ',  fern.  pi.  of  -aceus,  ‘belong- t®*  to,  of  the  nature  of’;  see  -aceous.  The  '
```


## [2026-09-06T20:36:32.015Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\ngrep -ho '\"ref\": \"KLN:[0-9]*\"[^}]*' page-2*.json | head -40"
}
```


### [2026-09-06T20:36:32.064Z] TOOL RESULT

```
"ref": "KLN:678",
"ref": "KLN:678",
"ref": "KLN:678",
"ref": "KLN:231", "status": "partial", "note": "KLN_1966.txt leaf 132 (printed pp. 229-231), s.v. candy: 'Shortened fr. sugar candy, fr. F. (sucre) candi, fr. It. (zucchero) candi(to), “sugar candy”, fr. Arab. qandi, “crystallized, candied”, adj. formed fr. qand, “cane sugar”, which, like OI. khaṇḍakaḥ, “candy”, is prob. of Dravidian origin.' Klein confirms the Arabic word and the route onward to French/English, but does not make Arabic borrow it from Persian, and rejects the Indo-European origin of the whole group."
"ref": "KLN:318",
"ref": "KLN:951",
"ref": "KLN:148",
"ref": "KLN:763",
"ref": "KLN:545",
"ref": "KLN:545",
"ref": "KLN:1288",
"ref": "KLN:232",
"ref": "KLN:231",
"ref": "KLN:232",
"ref": "KLN:231",
"ref": "KLN:374", "status": "supports", "note": "Klein 1966 p.374 s.v. Croat: '… cogn. with OI. giriḥ, Avestic gairi, ‚mountain‘, Alb. gur, ‚rock‘, Lith. girė, ‚forest‘' (KLN_1966.txt l.9710, the printed '374' marker falls inside this entry)."
"ref": "KLN:374", "status": "supports", "note": "Klein 1966 p.374: 'Croat, n. — Fr. earlier Chorwat, fr. Serbo-Croatian Hrvat, fr. OSlav. Churvatinu, „Croat“, lit. „mountaineer, highlander“, fr. chŭrva, „mountain“, which is rel. to OSlav., Serb. and Croatian gora …'. Klein does say what the arrow says, so the citation is faithful — but Klein's claim is itself what modern Slavistics rejects."
"ref": "KLN:368", "status": "supports", "note": "Klein 1966 p.368 s.v. cravat: 'cravat, n. — F. cravate, fr. Cravate, „Croat, Croatian“, and lit. meaning „neckcloth worn by the Croats“, fr. Serbo-Croatian Hrvat, „Croat“, fr. OSlav. Chŭrvatinu; originally meaning „necktie after the Croatian fashion“. See Croat.' (KLN_1966.txt l.9579; the entry sits between the printed page markers for 368). Note that Klein inserts Serbo-Croatian Hrvat, which the chart omits."
"ref": "KLN:111", "status": "supports", "note": "Klein 1966 p.111 (KLN_1966.txt l.3580, between the printed markers 111 and 112) s.v. asbestos: 'L. asbestos, fr. Gk. ἄσβεστος, lit. „unquenchable, inextinguishable“, fr. ἀ- (see priv. pref. a-) and σβεστός, verbal adj. of σβεννύναι, „to quench, extinguish“, which derives fr. I.-E. base *gʷes-, „to quench, extinguish“, whence also Lith. gèsti, OSlav. gašǫ, gasiti …'. Klein's own form is σβεστός/σβεννύναι — the two ν's and the correct segmentation, which the chart's 'a-sbenunai' garbles."
"ref": "KLN:35",
"ref": "KLN:543",
"ref": "KLN:1007",
"ref": "KLN:1766",
"ref": "KLN:1766",
"ref": "KLN:656",
"ref": "KLN:656",
"ref": "KLN:656",
"ref": "KLN:266",
"ref": "KLN:266",
"ref": "KLN:703",
"ref": "KLN:703",
"ref": "KLN:704",
"ref": "KLN:704",
"ref": "KLN:941",
"ref": "KLN:941",
"ref": "KLN:723",
"ref": "KLN:937",
"ref": "KLN:723",
"ref": "KLN:937",
"ref": "KLN:735",
```


## [2026-09-06T20:36:38.261Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E '^[0-9]{1,4}$' KLN_1966.txt | head -20\necho \"---count\"\ngrep -c -E '^[0-9]{1,4}$' KLN_1966.txt\necho \"--- around cathay\"\nawk 'NR>=6780 && NR<=6810' KLN_1966.txt | grep -n -E '[0-9]{3}' | head"
}
```


### [2026-09-06T20:36:41.102Z] TOOL RESULT

```
10:1966
108:3
120:1
124:1
128:1
137:1
158:1
163:1
177:1
185:37
219:1
328:1
346:3
357:1
1177:4
1213:6
1214:7
1272:8
1286:9
1322:10
---count
1185
--- around cathay
13:250
14:251
```


## [2026-09-06T20:36:46.724Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nmarks=[(i+1,int(l.strip())) for i,l in enumerate(lines) if re.fullmatch(r'\\d{1,4}',l.strip())]\ndef near(n):\n    prev=[m for m in marks if m[0]<=n][-3:]\n    nxt=[m for m in marks if m[0]>n][:3]\n    print(n, 'prev',prev,'next',nxt)\nfor n in (2136,6804,20647,20651,20824):\n    near(n)\nEOF"
}
```


### [2026-09-06T20:36:48.872Z] TOOL RESULT

```
2136 prev [(2065, 43), (2100, 44), (2114, 45)] next [(2142, 46), (2186, 49), (2216, 50)]
6804 prev [(6740, 249), (6792, 250), (6793, 251)] next [(6867, 254), (6897, 1), (6924, 256)]
20647 prev [(20593, 842), (20594, 843), (20646, 844)] next [(20658, 845), (20692, 846), (20730, 848)]
20651 prev [(20593, 842), (20594, 843), (20646, 844)] next [(20658, 845), (20692, 846), (20730, 848)]
20824 prev [(20745, 849), (20805, 850), (20817, 851)] next [(20859, 852), (20860, 853), (20911, 1967)]
```


## [2026-09-06T20:36:58.004Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- SOD Khotanese\"\ngrep -n -i 'khotanese' SOD_pages.txt | head -20\necho \"--- SOD gwdnyk\"\ngrep -n -i \"wdnyk\\|ywdnyk\\|gwdn\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T20:36:58.074Z] TOOL RESULT

```
--- SOD Khotanese
2043:                                                              languages such as Khotanese and Khwarazmian are
3295:in Manichean script (M) the Semitic sign lamed is                    Munji and (the Kafiri dialect of) Prasun. Khotanese,
3402:       aux. auxiliary           Khot. Khotanese                pro. prohibitive
3673:KT    Khotanese Texts, VI. Cambridge, 1967.                       translated from Persian.
16212:            Khotanese                                                       art. nom. sg. m. =>xwnx
38674:jewel  8526                             Khotanese      4368                    knowable    4230
--- SOD gwdnyk
7958:     aryawan ©Akk. argamanu; Aram, argwdnd                          armin
20715:    5919 nyrys- S(C)                              o*J> o~jjs"           niyoSan   (nywdn) ©Khwar. nYwdnyk  ©pi. -(
```


## [2026-09-06T20:36:59.549Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- MON kohl\"\ngrep -n 'کحل' MON_part1.txt MON_part2.txt | head -20\necho \"--- MON kahhal\"\ngrep -n 'کحال' MON_part1.txt MON_part2.txt | head -10\necho \"--- MON alkol\"\ngrep -n 'الکل' MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-06T20:36:59.647Z] TOOL RESULT

```
--- MON kohl
MON_part2.txt:11040:تاریک بی‌ابر» قبةٌ زریفت. قباء(ی) کحلی: 
MON_part2.txt:21232:کحال: 1 [ع.] (ص. |.) کسی که کحل 
MON_part2.txt:21244:کحل ادا [ع.] (مسص‌م.) سرمه کشیدن 
MON_part2.txt:21246:کحل: اعاتا [غ.] (مصل.) سرمه گون شدن 
MON_part2.txt:21256:کحل: 0 [ع.] (.) سنگک سر مه. سر مه. هر 
MON_part2.txt:21257:چه در چشم کشند برای شفای چشم. کحل 
MON_part2.txt:21259:گویند که به عنوان سرمه بکار می‌رفته؛ کحل 
MON_part2.txt:21260:مغربی» کحل زرقانو. کحل خولان: (پز.) 
MON_part2.txt:21261:حضیض یمانی. کحل فارسی: (پز.) انزروت. 
MON_part2.txt:21262:کحل کرمانی: (پز.) انزروت. 
MON_part2.txt:21263:کحلی: -(۲۰۷ [ع. ف.] (ص‌نسب.) منسوب 
MON_part2.txt:21264:به کحل؛ سرمه‌یی» سرمه رنگ. کحلی پرند: 
MON_part2.txt:21265:(کد.) تاریکی شب. کحلی چرخ: (کد.) 
MON_part2.txt:21266:سیاهی شب. آسمان اول. کحلی روز: (کد.) 
MON_part2.txt:21267:تاریکی شب. کحلی شب: (ککد.) تاریکی 
MON_part2.txt:50370:دریای بز رک اقیانوس. محیط کحلی رنگ: 
MON_part2.txt:63782:مکحل: ا۱۱0۵ [ع.] (امف.) سر مه ر بخته 
MON_part2.txt:63785:یک‌حله: (۵-)1۱60213 [ع. . مکحلة] 1( 
MON_part2.txt:70856:آسمانی: (گیا.) کحلان. مینای چمنی: ( گیا.) 
MON_part2.txt:85689:(بز.) بزرگک سیاه رگ زبرین. ورید اکحل: 
--- MON kahhal
MON_part1.txt:1959:پزشکی و کحالی استعمال می‌گر دد. 
MON_part1.txt:50522:کحال. 
MON_part1.txt:80317:شده این سنگ را سابقاً در کحالی به مناست 
MON_part2.txt:21232:کحال: 1 [ع.] (ص. |.) کسی که کحل 
MON_part2.txt:21234:سرمه کش. ضح.- در قدیم کحال به کسی 
MON_part2.txt:21239:چشم پزشکد؟ ج . کحالون» کحالین . کحال 
MON_part2.txt:21241:کحالی: ۵:۸2 (ع. ف.] (حامص.) شغل 
MON_part2.txt:21242:و عمل کحال. علم به امراض چشم؛ 
--- MON alkol
MON_part2.txt:8461:رزین تند و سوزاننده محلول در اتر و الکل 
MON_part2.txt:13384:آب و الکل قابل حل است. بهترین قطران 
MON_part2.txt:16061:حتی الکل (هنگام مستی) بکار می‌رود. قهوة 
MON_part2.txt:16739:کف شود این جسم در آب و الکل حل 
MON_part2.txt:16743:الکل شستشو می‌دهند» سیس ۳ را در 
MON_part2.txt:16745:مقداری الکل به این محلول اضافه کنند 
MON_part2.txt:16964:و برخی مسمومیت‌ها خصوصاً الکلیسم و 
MON_part2.txt:18846:الکل روی آن بریزند) در حرارت ۱۷۷ 
MON_part2.txt:18851:هزارم) ولی در الکل به خوبی حل می‌گردد 
MON_part2.txt:21226:الکلب؛ قاتل‌الکلب. اذارافی» ازاراقی»
```


## [2026-09-06T20:37:05.520Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'الکل\\s*[:؛]\\|الکل \\[\\|الکل(\\|^الکل' MON_part1.txt | head -20\necho \"--- search alcool/فر\"\ngrep -n 'الکل' MON_part1.txt | head -30"
}
```


### [2026-09-06T20:37:05.610Z] TOOL RESULT

```
7041:الکل به وسیلهٌ اسید سولفوریکك بدست 
16343:الکل: اهااه زع. الکحل ] (.) (شیم.) جسمی 
16355:الکلی: [-2101 [فر. ف.] (ص‌نسب.) شخصی 
16357:الکل باشد: مشروبات (نوشابه‌های) الکلی. 
43992:الکل با اتر که از ار فعال مواد معدنی 
75327:الکلبه» دیق» مخاطه» مخطا. 
90184:الکل حل نمیگردند ولی در آب آماس 
95728:الکل مطلوب در ۱۰۰ قسمت حاصل شود. 
96847:الکل‌های مختلف و اسیدها و ستن‌های 
--- search alcool/فر
1137:زده تهبه کنند و ۲/۵ و ۵ درصد الکل 
6781:با الکل بدست می‌آید» اترسل. (شیم.) 
6783:مولکلول الکل حاصل شود؛ اتر اکسید. 
7041:الکل به وسیلهٌ اسید سولفوریکك بدست 
7263:غذا و جز آن بکار می‌آید. اجاق الکلی: 
7264:آلتی که با الکل می‌سوزد و از گرمای آن در 
16343:الکل: اهااه زع. الکحل ] (.) (شیم.) جسمی 
16346:شامل اقسام است. مهمترین آن الکل اتیلیکك 
16349:(الکل معمولی) است که مایعی است بیرنگ 
16355:الکلی: [-2101 [فر. ف.] (ص‌نسب.) شخصی 
16356:که معتاد به نوشیدن الکل باشد. آنچه دارای 
16357:الکل باشد: مشروبات (نوشابه‌های) الکلی. 
16363:بسی‌جهت. (ق.) دروغکی. فلانی الکلی 
16933:قلیل الکلام. (گی.) ننه حوا. 
17540:دخانیات» انحصار فرروش مشروبات الکلی. 
21278:هوا اکسیژن هوا را با محلول الکل معمولی 
25644:استیلن با دود زیاد می‌سوزد. بنزین در الکل و 
30666:کزبر:القناه شعرالکلاب» ساق‌الاسود؛ 
43992:الکل با اتر که از ار فعال مواد معدنی 
43994:(شیم. پز.) محلول ید و الکل که برای التیام 
48630:بکار می‌رفته است؛ خصية الکلب البحرء 
49939:چراغ الکلی: چراغی که مادهٌ مولد حرارت 
68409:رم ۵۵ (.) نوشابه‌ای الکلی که از تقطیر 
73498:و در الکل به خوبی حل گردد و مصرت 
75327:الکلبه» دیق» مخاطه» مخطا. 
77263:نوشابه‌های الکلی دیگر که غلطت الکلی 
78940:باسیل کخ که از باسیل‌های مقاوم در الکل و 
79317:آب و الکل حل نمی‌شود و آن فراوانترین و 
79982:است؛ بل» زرغ الکلبه زقوم» پستانک» 
80775:در شرب مشروبات الکلی؛ بدی گوارش؛
```


## [2026-09-06T20:37:06.174Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21225,21270p' MON_part2.txt"
}
```


### [2026-09-06T20:37:06.224Z] TOOL RESULT

```
عنوان گل زینتی کشت می‌شوند» خانق 
الکلب؛ قاتل‌الکلب. اذارافی» ازاراقی» 
کوچوله. ضح. در برخی کتب کچوله 
مرادف با جوزالقی ذکر شده که اشتباه است. 
کچه: (۵-)۲۵۵ [- کاچه] (.) زنخ» چانه. 
کچه در آوردن: دهن کج کردن به تمسخر و 
تفای کنسن. 
کحال: 1 [ع.] (ص. |.) کسی که کحل 
(سرمه) به چشیم اشخاص می کشد؛ 
سرمه کش. ضح.- در قدیم کحال به کسی 
گفته می‌شد که هم سرمه به چشم کسان 
می‌کشید و هم جراحات و امراض چشم را 
علاج می‌کرد (قروینی. یادداشتها ۲ ۳۹ ح 
۱ طبیبی که دردهای چشم را درمان کند؛ 
چشم پزشکد؟ ج . کحالون» کحالین . کحال 
شریعت: (کذ) رسول‌اللهص. 
کحالی: ۵:۸2 (ع. ف.] (حامص.) شغل 
و عمل کحال. علم به امراض چشم؛ 
چشم پزشکی. 
کحل ادا [ع.] (مسص‌م.) سرمه کشیدن 
را. 
کحل: اعاتا [غ.] (مصل.) سرمه گون شدن 
چشم به سرشت» سیاه شدن رستنگاه پلکك. 


فرهنگ فارسی 


۱۳۳۷ 


کحل: 0 [ع.] (.) سنگک سر مه. سر مه. هر 
چه در چشم کشند برای شفای چشم. کحل 
اصبهانی (اصفهانی): (پز.) سولفورانتیمون را 
گویند که به عنوان سرمه بکار می‌رفته؛ کحل 
مغربی» کحل زرقانو. کحل خولان: (پز.) 
حضیض یمانی. کحل فارسی: (پز.) انزروت. 
کحل کرمانی: (پز.) انزروت. 
کحلی: -(۲۰۷ [ع. ف.] (ص‌نسب.) منسوب 
به کحل؛ سرمه‌یی» سرمه رنگ. کحلی پرند: 
(کد.) تاریکی شب. کحلی چرخ: (کد.) 
سیاهی شب. آسمان اول. کحلی روز: (کد.) 
تاریکی شب. کحلی شب: (ککد.) تاریکی 
شب. 
کسخ: ۵۷ ۱:0 ,1۵ (.) صورتی مهیب و 
زشت که سازند و کودکان را بدان ترسانند؛
```


## [2026-09-06T20:37:15.240Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16340,16360p' MON_part1.txt"
}
```


### [2026-09-06T20:37:15.284Z] TOOL RESULT

```
ال کردن: اه ال و سل کردن. 
(مصل.) (عم.) لاف زدن. 

الکل: اهااه زع. الکحل ] (.) (شیم.) جسمی 
آلی» مرکب از تیدروژن» اکسیژن و کرین و 
آن فرار» دارای طعم تند و سوزان است و 
شامل اقسام است. مهمترین آن الکل اتیلیکك 


(الکل معمولی) است که مایعی است بیرنگ 
و صاف با بوی نسبة خوش آیند و مزةٌ گس 
و سوزان» سبکتر از آب؛ با وزن مخصوص 
۸ در ۷۸/۲ درجه به جوش می‌آید و 
در ۱۳۰ - درجه منجمد می‌گردد. 

الکلی: [-2101 [فر. ف.] (ص‌نسب.) شخصی 
که معتاد به نوشیدن الکل باشد. آنچه دارای 
الکل باشد: مشروبات (نوشابه‌های) الکلی. 
الکن: ماه [ع.] (ص.) کسی که زبانش به 
هنگام سخن گفتن گیر کند و نتواند درست 
کلمات را ادا سازد؛ صاحب لکنت.
```


## [2026-09-06T20:37:16.644Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- BQT v2 خان headword\"\ngrep -n 'خان' BQT_v2_pages.txt | sed -n '1,5p'\necho \"--- find pdf page tags\"\ngrep -n '\\[pdf page' BQT_v2_pages.txt | head -3\ngrep -c '' BQT_v2_pages.txt"
}
```


### [2026-09-06T20:37:16.727Z] TOOL RESULT

```
--- BQT v2 خان headword
84:                   ‫متعلق بکتابخانة ملی از روی نسخهٌ خط اسدی شاعر معروف ‪ = (۱‬الایشیه)‪.‬‬
131: ‫رود کیسمرفندی)‪ .‬مسحح سعیدنفیسی بسرمايةٌ کشتراکبتفروشی ادب‪ .‬تهران‪ .‬چايخانة‬
149:        ‫مسلادی ( = سندیاد نامه)‪.‬‬    ‫‪6۹۱ ۸‬‬   ‫احمدا تش‪ .‬استانبول‪ .‬چایخانة وزارت فرهنك‬
170:                                ‫زبان فارسی‪ .‬شمارء ‪ )۱‬بسرمابةً کتابخانةٌ زوار ت‬
207:                                                                  ‫ناتل خانلری ‪ .‬تهران ‪ ۹۲۳۱‬شمسی‪.‬‬
--- find pdf page tags
41071
```


## [2026-09-06T20:37:22.506Z] TOOL CALL #24: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T20:37:22.581Z] TOOL RESULT

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


## [2026-09-06T20:37:23.068Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('leaves',len(p))\nfor i in (30,31,32,200,201):\n    print('=== leaf',i)\n    print(p[i][:200])\nEOF"
}
```


### [2026-09-06T20:37:24.810Z] TOOL RESULT

```
leaves 684
=== leaf 30
                                             ‫يان نهم‬

             ‫در جیم ابجدبا شین قرشت مشتمل‌برپانزده لغت کونامت‬
‫و آن روز ششم‌فروردین‌ماه قدیم باشد» و آن‌روز‬          ‫جش‪=-‬فتح اول و سکون ثا
=== leaf 31
‫جشن سده‬                                                                                          ‫”‪~o‬‬


‫هرکزمارندیدهبودمتعجب شد و کقت جمیم‬                             ‫‪.‬‬        ‫دربن روز جشن
=== leaf 32
 ‫==‬                                                                           ‫جدن مرد گیران‬
        ‫فارسیان‪ .‬درروز هفتم خرداد ماه کنند ‪.‬‬                          ‫روز جشنی عطظیم کرد ‪° %‬‬


=== leaf 200
   ‫ره‬      ‫سل‬                                                                                         ‫خروه‬

 ‫فقیرآنرا با خرما بکوبند وبخوردد ؛ بواینمعتی‬         ‫والث مجهول بر‬
               
=== leaf 201
  ‫خرش‬                                                                                                 ‫سم پات‬

 ‫و بمعنی شوم ونحس و نامبارك همآمده است‬               ‫جانور کی است که‌هرچه‌برزمین اف
```


## [2026-09-06T20:37:30.828Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nimport re\nfor i,leaf in enumerate(p):\n    head=leaf[:160]\n    if 'خان' in head or 'ختن' in head or 'خطا' in head:\n        print(i, ' | '.join(head.split('\\n')[:3])[:140])\nEOF"
}
```


### [2026-09-06T20:37:32.444Z] TOOL RESULT

```
165 ‫خاهاء بلا‬                                                                                              ‫و و د‬   ‫سد‬ |  | 
166      ‫ا =‬   ‫=ړ‬ |                                                                                                  ‫خانگاه ‪.‬‬ |  ‫شارزاب
176  ‫ضا‬ |   ‫با سوختن و راه رفتن در دست وایعاو‬                            ‫خجنك = نماول وفتح ثانی سوکون‬ |                                   
178      ‫‪۵‬ف‬ |  |  ‫‪۴‬‬      ‫باشد‬    ‫بزرگه و خداوند خانه‬        ‫و کدخدای‬       ‫بضم اول و الی و سکون‬       ‫خدو ‪- ۲‬‬
245   ‫خورخجیون‬                                                                                    ‫‪YAY‬‬ |  | 
247  ‫خوره‬                                                                                                ‫اس‬ |  | 
309  ‫دربو‬                                                                                                  ‫‪٩‎‬و‬ |  | ‫و کردا کرد خانه واطرا
330  ‫—‬     ‫‪0‬‬   ‫= ‪۵‬‬ |  | 
344 ‫و آنر! حب‌الخطای وحب‌اللاطین خوانند ‪ ۴‬؛‬         ‫اصاری شود ‪ -‬و دام روز ششم کالون ال خر هم‬ | ‫یکدانگ آن مسپل رطوبات‌بود ‪ -‬وکنیاامهی‌
352       ‫پوس‬ |  |                                      ‫کون طای باشد ‪.‬‬          ‫دو حتن ‪ -‬بر وزن سوختن » معروف‬
378       ‫اه‬                                                                      ‫دبوار خانه روزن شدن‬ |  | ‫آرا‬
403  ‫ردای لیل‬                                                                                   ‫م‪ ۳‬پهب‬ | ‫واگر پراو را درخانه بخور کنند جم
514  ‫ات‬        ‫او‬                                                                              ‫زیرفون‬ | ‫بکهد‌یگرباشرت کنند ‪ -‬کونایه ازخ
526   ‫—‬        ‫=‬ |                                                                                                      ‫زوهیدن‬ | 
586    ‫)‪۷۱‬ات‬ |  | ‫که بجمد و جهنده باشد ‪ -‬و نام درختی است‌در‬           ‫بمعنی ربختن باشد ‪-‬ویمعنی‬         ‫ر‬
589   ‫سکه فروختن‬ |            ‫ر‬                                            ‫‪۱‬‬                       ‫م‪۱ ۲‬ات‬ | ‫فایق باشد ‪ -‬و بمعنی ض
```


## [2026-09-06T20:37:43.580Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\""
}
```


## [2026-09-06T20:37:44.743Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nfor i in (165,173):\n    print('==== leaf',i,'printed',i+542)\n    print(p[i][:2500])\nEOF"
}
```


### [2026-09-06T20:37:45.644Z] TOOL RESULT

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


### [2026-09-06T20:37:47.595Z] TOOL RESULT

```
==== leaf 165 printed 707
‫خاهاء بلا‬                                                                                              ‫و و د‬   ‫سد‬




 ‫خان بره = بکرئاك وفتح‌بای اب‬                                ‫ووده وترلبگه را ‪۱‬‬
                                                                             ‫کوبند عموماً ‪ -‬ت‬
          ‫»نایه از بحرحمل است ‪.‬‬
                              ‫ورای قرشت ک‬                                                             ‫خصوصا ؟ ‪.‬‬
  ‫‪۰‬وی‬
    ‫ویم ک‬
        ‫خانج ‪ -‬بسکون نالك ج‬                                 ‫خامه رن = بزاای هوز بروژن جامه‬
‫باشد که طفلان بجهت جوزبازی کنند ومشتی از‬                   ‫کن » چیزی بائد کهفلم تراشیده را بدان (‪)۱‬‬
           ‫جوز بدست گرفته درآن مان اندازك ‪.‬‬
                                                                       ‫ویعری‌آنرا مقط خوالند ‪.‬‬             ‫قزطد‬
 ‫خانجه ‪ -‬اروان سوراخا‪-‬له وسرای‬
                                                            ‫خامیار ؟ = بابای حطی بروزن‌کارماز»‬
  ‫ند ‪ -‬و یز طبقی باشد ازچوب‬     ‫ککوچوكبرا‬                                     ‫خمبازه ودهان دره گروایند‪.‬‬
 ‫که آنرا نقاشی کرده باشند؛ و بان معنی بواو‬
    ‫معدوله هم آمده است که خوالجه باشد ‪٩‬‏ ‪.‬‬                ‫خامیاده ‪ - ۴‬بمنی خامیاز استکه‬
 ‫خان خرك ‪ -‬بكر اك فوتح خای‬                                                    ‫خمازه‪ .‬ودهان دره باشد ® ‪.‬‬

‫نقطه‌دار ورای بی‌اقطه وسکون‌کاف » بمعنی خان‬
                                                            ‫خان » بورزن کان ‪ .‬بادشاهان ختا‬
‫اکسهت‌کاروانرا باشد ‪ -‬وکاروانسرای کوچك را‬                  ‫و رفکتانرا کوبند هر که باشد چنانکه (‪)۷‬‬
                                       ‫نیز گفته‌اند و‬      ‫پادشاهان روم را قیصر وچ را فففورخوانند ‪-‬‬
 ‫ابجد‬      ‫ادكاول‬           ‫ر‬
                            ‫کل =‬
                               ‫ب د‬
                                 ‫خان‬                        ‫و بمعنی خانه وسرا هم هست ‪ - ۷‬وکاروانسرارا‬
                ‫ولام » اثاره بكمبةُ ممظمه است ‪-‬‬            ‫و شان عل را هم گفته اند *‬              ‫نیز گویند ‪-‬‬

‫خان غر د )‪ = (£‬بس‌کون‌ثالت وغن‬                              ‫وسل‬
                                                              ‫درآن خاله کند ع‬               ‫وهر‬
                                                                                              ‫بی ک‬
                                                                                                 ‫لجای‬
                                                                             
==== leaf 173 printed 715
                                                   ‫يبان چهارم‬
                              ‫در خای نقطه‌دار با تای قرشت مشتمل بر ده لفت‬
 ‫خقل = بفتح اول و سکون انی ولام »‬

                                                                                               ‫چن ‪. ۱‬‬    ‫ضالك‬
  ‫بمعنی فربفتن وگول زدن باشد ‪ -‬وو نلااممتی‬
 ‫است از بدخشان که اسب خوب از آنجا آورند‬                     ‫ختار بفتح‌اوز بروزن قطار‪ .‬پاك کردن‬
     ‫وسب ختلی منوب بآن ولامت است ‪- ۴‬‬
                                   ‫ا‬                         ‫باغ و کشت زارباشد اکزیاه خودرو وخاروخلاشه؛‬
      ‫واسیفول (‪ )۲‬و بزر قطونا را همگفته‌اند ‪.‬‬                                    ‫‪.‬‬   ‫اعت‬     ‫وسم اول هم اة‬


‫ختالان » بفتح‌اولوسکون‌انی‌وثالك بالف‬                            ‫شیت‬
                                                                   ‫ررا‬
                                                                     ‫قتح‬
                                                                       ‫خترق؟ = بضم اول و ف‬
 ‫کشد‪.‬و(‪)۳‬بنون زده؟ ‪.‬ام ولامتی‌است ازمضافات‬                   ‫وسکون ثانی وقاف » بلقت رومی دوابی است که‬
     ‫بدخثان که مکولاب اشتهار دارد ‪ .‬گوشد مردم‬

‫آنجا خوش صورت میباشند واسب خوب نیز از‬                                                               ‫باشد (‪. )۱‬‬
 ‫ِ‬    ‫بدا لجاست ‪6‬‬           ‫آ نا ور ندوختلی وختلاتی منوب‬


      ‫ختلی = بروزن اصلی‪ .‬منوب بختل‬                          ‫بی‬   ‫خرفه را گونند وآترا سر‬     ‫فا وجیم »‬   ‫وسکون‬


                                                                                           ‫بقلة الحمقا خوائند ‪.‬‬

      ‫و‪.‬‬     ‫‪-:‬‬    ‫چش‬   ‫»‬    ‫چك‬   ‫(‪)۳‬‬       ‫(‪ )۲‬چك‪ .‬چش‪ :‬اسفول‪.‬‬            ‫(‪ )۱‬چك“ چشس ‪ :‬بود‪.‬‬

      ‫خطا (خطای ) › تعیین معنی تامکلمه که درتواریخ و کتب ادبی اسلامی‬                  ‫‏‪ _ ١‬ختا =‬

      ‫بیار آمده » مشکل است » در هرحال بقسمت شمالی چین یعنی نواحی منچوری ‪ .‬مقولتان‬
      ‫»>‬          ‫ا‬
                  ‫خهط «‬
                      ‫وتر کتان شرقی‌اطلاق میشده وطاهراً فمای ازسیبری حم‌تحت أبن عنوان مآ مده ‪.‬م‬
       ‫با «خطان» نام طابفه‌ای از طوایف مفول است و ابن طایفه در اوایل قرن چهارم هجری تحت‬
       ‫فرمان « بولیجیآیواکی » تمام مفولستان وقسمتی از چین را تصرف کردند وهمین اوقات تام خطا‬
      ‫را بهمة ابن مالك وسیم اطلاق کردند » و قرب دوست سال فرمالروایی‌نمودند ‪ .‬سپس طايفة‬
       ‫« بوشی » ازطوایف «مالچو» بدین سرزمین حمله برد وغالب نواحی آلرا تصرف کرد در تیجه‬
       ‫مکی ازمنوبان خاندان خطا بخطة * چونفغاریه »ک
```


## [2026-09-06T20:38:12.460Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xwtn\\|ywtn\\|ywdn\\|xwdn\\|Khotan\" SOD_pages.txt | head -30"
}
```


### [2026-09-06T20:38:12.513Z] TOOL RESULT

```
2043:                                                              languages such as Khotanese and Khwarazmian are
3295:in Manichean script (M) the Semitic sign lamed is                    Munji and (the Kafiri dialect of) Prasun. Khotanese,
3402:       aux. auxiliary           Khot. Khotanese                pro. prohibitive
3673:KT    Khotanese Texts, VI. Cambridge, 1967.                       translated from Persian.
16212:            Khotanese                                                       art. nom. sg. m. =>xwnx
20654:           34: Frag. Len.; Anc. Lett. 1.9, 3.18; nYywdnw>
20713:         Mack. AI 424.6 n p427                                     5929 nywdn C =* nyw6n(),/(h)
20715:    5919 nyrys- S(C)                              o*J> o~jjs"           niyoSan   (nywdn) ©Khwar. nYwdnyk  ©pi. -(
22995:     pacuxay (pcwxy-) *»pcxw*y-, pcyw>y-                          pacxoS ©Parth. prxwdn
24200:                                                                    parxon ©<*pari-xauna\ Parth. prxwdn
28966:     saydman ^sywtn^n
28989:                                                             8770 sywtn^n S                                    ^l*&i<u&
29803:      sad                                                              suyt/dman     ©adj. ^sywtnVn
38674:jewel  8526                             Khotanese      4368                    knowable    4230
```


## [2026-09-06T20:38:12.749Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ *174 \\| 174 \" SOD_pages.txt | head -10\necho \"---\"\ngrep -n \"Khotan\" SOD.txt | head -20"
}
```


### [2026-09-06T20:38:13.255Z] TOOL RESULT

```
2841:   In 1948, a short bilingual inscription was found in               Sims- Williams, CLI, 1989, 174 n 10.
4255:    amate ^"m't'k, »mtyc                                  174 Mmtyc B, M, S                                j^jtcJj
7745:       BSTBL; TSP; SCE; GMS 585; inf. ->y, TSP 2.893           BSTBL, Vim. 120 etc.; Dhy. 174 etc.; SCE 3 etc.
33835:          STii 7.4; BSTBL, pl42-3; wyn'ncy, Dhu. 174              vision, revelation
---
3794:languages  such  as  Khotanese  and  Khwarazmian  are 
6308:Munji  and  (the  Kafiri  dialect  of)  Prasun.  Khotanese, 
6540:Khot.  Khotanese 
7225:KT    Khotanese  Texts,  VI.  Cambridge,  1967. 
36521:Khotanese 
91020:Khotanese    4368
```


## [2026-09-06T20:38:17.271Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"4368\" SOD_pages.txt | head -10\necho \"---\"\ngrep -n \"^ *4368\\| 4368 \" SOD.txt | head"
}
```


### [2026-09-06T20:38:17.330Z] TOOL RESULT

```
16210:      4368 YwSnyk       S                          o-^'cr^J*'
38674:jewel  8526                             Khotanese      4368                    knowable    4230
---
36518:4368  YwSnyk   S  o-^'cr^J*' 
91020:Khotanese    4368
```


## [2026-09-06T20:38:20.559Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16195,16230p' SOD_pages.txt\necho \"--- which leaf\"\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(t,1):\n    if i==16210:\n        print('line 16210 leaf',leaf,'printed approx',leaf-66)\n    leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-06T20:38:23.659Z] TOOL RESULT

```
            Frag. Len. 83.a4; S W, C2 pi 32 60V30                          MDii pl20.12; Hen. BSOAS 12.605n5
      4366 ywSkV B, S                                      i^-       4378 ywn-'     B                (0*lj*-)ij>f\fiO>i>sr-
           xuSkar, xwa6kar ©<*xwata-kara ^xwSk'r
           alone                                                          xwan, xun ©<*xwana ^ywn'k3, xwn-, ywt-2
                                                                          (^proclaim, 0o)wccp
           GMS 1 108, 11 24 A, 1120; TSP 2.408, 3.121; SCE                VJ 75, 89, 1060; TSP 21iii, 13; EGSii 12; AVS 76
             27; BSTBL, Intox. 27; Hen. Talcs. 486.20; JRAS
                                                                     4379 ywn-2 C                                         0->j>'
              1944, 138.5; MDii p87.17; -y, SCE 328
                                                                          yun ? ^ywnnc
      4367 yw6n B                     •xJ^^^JijJ^Jii                      (/<?)increasc
           yoSan ©<*gaudana =*crpyw5n                                     S W, C2 gloss.; AVS 98
           covering
            TSP 3.171                                                4380 YwnMy B =» ywn'k2
                                                                     4381 ywn'y B                   (u>> >-i~> j>)j *jT ■
      4368 YwSnyk       S                          o-^'cr^J*'
            xutanik, xu8anik                                              xonax (ywn'x, ywny, ywnx) ©demons, pron.
            Khotanese                                                       art. nom. sg. m. =>xwnx
                                                                          that, he
            GMS 976; Sogdica. p8-l0.11c                                   VJ; SCE; TSP; BSTBL; YwnYw, Frag. 11.2; TSP;
      4369 Ywdy     C «* Yw5>k(h)                                           GMS 1410 n pi; VJ 1509
      4370 Ywkt     B                                      >ff       4382 ywn'k1 B, S                             y.jT
III         Yokot (ywqtt) ©<*gaukrta                                      xone, xonaku (ywn'kw) ©demons, pron. art. sg,
            sulphur                                                         m. =>xwn}k, xwny
            GMS 76, 148; TSP 3.226, 229; Hen. BSOAS                       that, he
             11.69.38 "brimstone"                                         GMS 1402, 1405, 1411; VJ 1232; TSP 12.18; MDii
      4371 Ywqtt M =* ywkt                                           4383 ywnV B                                      ^
      4372 YwmV B                                  jJLs t^*^              yone    (ywn'yy, ywn*y)   ©<Av. gaona      ^ywn'k
           xumar ©<Av. vohu~mq$ra         4xwm'r
           consolation                                                    hair
           TSP 8.201-, VJ 1115; GMS 391; Frag. Len. 39.4                    Pwn>kh
                                                                          Bailey. Prolexis. 74; EGSii 90; TSP 2.296 n pl73;
      4373 Ywmr     C                                   <**>*<>_*           Ywn'y, Hen. BSOAS 11, 718; Ywn*y. SCE 302



--- which leaf
line 16210 leaf 239 printed approx 173
```


## [2026-09-06T20:38:34.868Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T20:38:34.872Z] TOOL RESULT

```


```


## [2026-09-06T20:38:38.099Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/khan",
 "prompt": "Give the full etymology sections for the English noun \"khan\" (both the ruler/title sense and the caravanserai sense), including source languages (Turkic, Mongolian, Persian, Arabic) and any mention of khagan."
}
```


## [2026-09-06T20:38:38.413Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/khan",
 "prompt": "Full etymology text for khan."
}
```


### [2026-09-06T20:38:45.411Z] TOOL RESULT

```
# Etymology of English "Khan"

## Etymology 1 (Ruler/Title Sense)

The word comes "Via late Middle English _can, chan_ from Old French _chan_, from Medieval Latin _chanis_, from Turkic \*qan, contraction of \*qaɣan."

It is cognate with Old Turkic _𐰴𐰍𐰣_ (qaɣan) and Mongolian _хаан_ (xaan), "possibly from Rouran language." The ruler meaning specifically derives from Middle Mongol _ᠬᠠᠭᠠᠨ_ (qaɣan), referencing Genghis Khan. The term functions as a "doublet of _khagan_."

## Etymology 2 (Caravanserai Sense)

This meaning comes from Arabic _خَان_ (ḵān) and Persian _خان_ (xân), both meaning "inn, caravanserai, hotel." This represents a distinct etymological path from the ruler sense, derived from Middle Eastern languages rather than Turkic-Mongolian sources.
```


### [2026-09-06T20:38:46.956Z] TOOL RESULT

```
# Khan - Etymology Summary

**Origin:** The word "khan" comes from Turkic origins, literally meaning "lord, prince." It's a contraction of *khaqan*, meaning "ruler, sovereign."

**Historical presence:** "The word has been known in the languages of Europe since 13c.; compare Medieval Latin *chanis*, Medieval Greek *kanes*, Old French *chan*, Russian *khanu*."

**Timeline:** The term entered English around 1400 as a title for sovereign princes in Tatar territories. Over time, its use broadened and degraded from a strict title to a more general mark of respect.

**Related forms:** The female equivalent, *khanum*, emerged by 1824 from Turkish *khanim*. The word also spawned derivatives like *khanate* (1799), meaning "the dominion of a khan."

**Alternative spellings:** An older variant form, *cham*, was used from the 1550s onward and similarly referred to rulers of Tatars, Mongols, and Chinese emperors.
```


## [2026-09-06T20:38:59.831Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%86",
 "prompt": "Give the Persian and Arabic entries for خان: all etymologies and senses (title/lord, house, caravanserai), and any derived terms like خانم, خانسامان."
}
```


## [2026-09-06T20:39:00.648Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Cathay",
 "prompt": "Full etymology of Cathay, including Khitan, Qidan, Medieval Latin Cataya, and mentions of Persian Khitai / Khata."
}
```


### [2026-09-06T20:39:07.557Z] TOOL RESULT

```
# Persian and Arabic Entries for خان

## Persian (خان)

**Etymology 1 - Title/Ruler:**
Borrowed from Turkic languages, first attested in Karakhanid coinage from the 900s. Means "Sir," "Mister," or historically a "khan" (nomadic ruler). Used as a politeness marker after names.

*Derived term:* خانی (xâni)

**Etymology 2 - Building/Structure:**
From Middle Persian meaning "house." Refers to a "caravanserai" or inn. Also describes "rifling" in gun barrels.

*Synonym:* کاروانسرا (kârvânsarâ)

## Arabic (خَان)

**Etymology 1 - Caravanserai:**
From Persian xân. Means "hostel," "caravanserai," or "inn."

*Derived term:* خَانَة (ḵāna)

**Etymology 2 - Verb:**
Separate root (خ و ن). Means "to betray," "to be disloyal," or "to deceive."

*Related terms:* خَائِن (traitor), خِيَانَة (betrayal)

**Etymology 3 - Ruler:**
From Old Turkic qaɣan. Means "khan," a ruler in Northern Asia.

*Derived term:* خَانِيَّة (khanate)
```


### [2026-09-06T20:39:09.014Z] TOOL RESULT

```
# Cathay: Etymology and Meaning

**Cathay** is an archaic English term referring to medieval northern China, particularly the region accessible via the Silk Road to Xi'an or Beijing.

## Etymology

The word's origins trace through multiple languages. It derives from Latin *Cathaya* (a variant of *Cataya*), which came from Old Turkic *Qïtań*. Ultimately, the term originated from the Khitan language, spoken by the Khitan people who established the Liao dynasty in 10th-century northern China.

Interestingly, linguists suggest a possible connection to Mongolian *xutga* ("knife"), indicating shared Proto-Mongolic roots.

## Modern Usage

Beyond its historical geographic sense, **Cathay** today refers to:
- A settlement in North Dakota
- An informal shorthand for Cathay Pacific Airways

The term represents "a land of mythic wonders" in Western imagination—Europeans during the Age of Exploration sought Cathay's rumored riches in gold, jewels, and spices, famously motivating explorers like Columbus in 1492.
```


## [2026-09-06T20:39:12.881Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Khotan",
 "prompt": "Etymology of Khotan: Khotanese Saka form, Sanskrit, Chinese, and whether it is related to Khitan/Cathay."
}
```


## [2026-09-06T20:39:13.886Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/alcohol",
 "prompt": "Full etymology of alcohol: Medieval Latin, French alcool, Arabic al-kuḥl, Semitic cognates, and the semantic development from antimony powder to spirits."
}
```


### [2026-09-06T20:39:17.864Z] TOOL RESULT

```
# Khotan: Dictionary Definition

Based on the Wiktionary entry provided, **Khotan** is defined as:

1. An alternative form of "Hotan"
2. The historical region corresponding to modern Hotan
3. The historical Kingdom of Khotan

## Pronunciation

The entry lists two pronunciations: "kōtän′" and "kō′tän′"

## Etymology Note

The provided content does **not** contain information about Khotan's etymology, nor does it discuss connections to Khotanese Saka, Sanskrit origins, Chinese naming, or relationships to Khitan/Cathay. The page focuses solely on the term as a proper noun referring to a geographical location and historical kingdom, with derived terms like "Khotanese" noted but not etymologically explained.

To find etymological information, you would need to consult additional sources beyond this Wiktionary entry.
```


### [2026-09-06T20:39:23.432Z] TOOL RESULT

```
# Etymology of Alcohol

The word "alcohol" has a fascinating etymological journey spanning multiple languages and centuries.

## Origin and Development

According to the Wiktionary entry, the term originated from **Medieval Latin**, transmitted through medical and alchemical texts. The word derives from Arabic "al-kuḥl" (كُحْل), which initially referred to kohl, a cosmetic powder. In Andalusian Arabic, it also appeared as "kuḥūl" (كُحُول).

The semantic evolution is particularly interesting: the term progressed "from stibnite first, then generalized in meaning to a powder obtained by triturating a material, then also to liquids obtained by boiling down, and specialized to mean spirit of wine, ethanol, in the 18th century."

## Historical Attestation

An early documented usage appears in Bartholomew Traheron's 1543 translation, where he describes "alcohol, or (as I fynde it sometymes wryten) alcofoll, for moost fine poudre" as a term used by "barbarous" Moorish authors.

By the 18th century, the chemical meaning had solidified, with modern chemical usage established after 1850.

## Modern Path

The word entered English through **Middle French** and **Middle English** "alcofol," eventually becoming the modern English "alcohol" we use today.
```


## [2026-09-06T20:39:28.928Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Kingdom_of_Khotan",
 "prompt": "What is the etymology of the name Khotan? Give the Khotanese Saka self-designation (hvatana/hvamna), Sanskrit forms, Chinese Yutian, and any statement about the name's origin. Quote relevant sentences."
}
```


## [2026-09-06T20:39:29.957Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/khotan-i-pre-islamic-history",
 "prompt": "Etymology and forms of the name Khotan (Khotanese hvatana-, hvamna-, Sanskrit, Chinese, Sogdian, Tibetan). Quote the relevant passage."
}
```


### [2026-09-06T20:39:34.125Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:39:36.939Z] TOOL RESULT

```
# Etymology of Khotan

## Khotanese Saka Self-Designation

The local people called their land "hvatäna" in Brahmi script and "Khotana" in Kharoṣṭhī script around the third century AD. Later forms included "Hvamna" and "Hvam," with the phrase "Hvam kṣīra" meaning "the land of Khotan."

## Sanskrit Forms

Under Buddhist Hybrid Sanskrit influence, locals used variants including "Gaustana," "Gosthana," "Gostana," "Godana," and "Kustana."

## Chinese Yutian

The ancient Chinese called it "Yutian" (于闐), also written as 于窴, with similar variants like "Yudun," "Huodan," and "Qudan."

## Origin Theory

Regarding the name's origin, scholar Ronald E. Emmerick stated: "My own preference is for an explanation connecting it semantically with the name Saka, for the Iranian inhabitants of Khotan spoke a language closely related to that used by the Sakas." He noted the name appears to be "an Iranian word with the common adjectival suffix -ana."
```


## [2026-09-06T20:39:43.356Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%AD%D9%84",
 "prompt": "Arabic كحل: root ك ح ل, verb kaḥala, noun كُحْل kuḥl, كَحَّال kaḥḥāl. Give etymology and Semitic cognates (Hebrew, Aramaic, Akkadian, Ethiopic)."
}
```


## [2026-09-06T20:39:44.342Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Cathay",
 "prompt": "Full etymology of Cathay and any note on Khitan/Khitai."
}
```


### [2026-09-06T20:39:50.468Z] TOOL RESULT

```
# كحل (Kohl) - Etymology and Cognates

## Etymology

The Arabic word **كُحْل** (kuḥl, "kohl/antimony") was borrowed from Aramaic **כוחלא** (kuḥlā), which itself derives from Akkadian **𒎎𒋆𒁉𒍣𒁕** (guḫlum, meaning "antimony, stibium").

## Semitic Cognates

- **Hebrew**: כָּחָל (kakhál, "kohl")
- **Aramaic**: כוחלא / ܟܘܚܠܐ (kuḥlā)
- **Akkadian**: guḫlum ("antimony, stibium")
- **Ge'ez**: ኵሕል (kʷəḥəl)

## Related Forms

The Arabic root ك ح ل produces multiple derivatives: the verb **كَحَلَ** (kaḥala, "to apply kohl"), the agent noun **كَاحِل** (kāḥil), and various other related terms describing the cosmetic substance and the action of applying it to the eyelids.
```


### [2026-09-06T20:39:51.102Z] TOOL RESULT

```
# Etymology of Cathay

**Origin:** The word "Cathay" emerged in the 1560s as a poetic designation for China, derived through Medieval Latin *Cataya* from Turkish *Khitai*, which itself came from Uighur (a Turkic language).

**Historical Source:** According to the Online Etymology Dictionary, the term traces back to "the Uighur (Turkic) *Khitai*, name of a Tatar dynasty that ruled Beijing 936-1122." This dynasty gave its name to the entire region, which eventually became the Western European term for the country.

**Linguistic Path:** The word traveled westward through multiple languages—from Uighur to Turkish to Medieval Latin—before entering English poetry and literature as a romanticized alternative name for China during the Renaissance period.

The etymology reflects historical contact between European and Asian civilizations, with the term preserving the memory of a specific ruling dynasty within its linguistic structure.
```


## [2026-09-06T20:39:58.511Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%84%DA%A9%D9%84",
 "prompt": "Persian الکل: etymology (borrowed from which language?) and meaning."
}
```


## [2026-09-06T20:39:59.451Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.cnrtl.fr/etymologie/alcool",
 "prompt": "Give the etymology history of French \"alcool\": earliest attestations, forms alcohol/alcool, the Arabic source al-kuḥl, and the semantic shift to spirit of wine."
}
```


### [2026-09-06T20:40:03.072Z] TOOL RESULT

```
# Persian الکل: Etymology and Meaning

**Meaning:** The word means "alcohol."

**Borrowed From:** According to the Wiktionary entry, الکل is "Borrowed from French _alcool_," which itself derives from Arabic. The etymology traces back through Medieval Latin to Arabic _الْكُحُل_ (al-kuḥul), ultimately originating from Akkadian.

The entry notes an interesting linguistic detail: "a direct boring from Arabic would drop the definite article _ال_ (al-), see there for more," explaining why the Persian term retains the Arabic article prefix that wouldn't normally appear in typical loanword adoption.
```


### [2026-09-06T20:40:05.564Z] TOOL RESULT

```
I appreciate your request, but I must be honest: the web page content provided contains only "Portail lexical" (Lexical Portal), which is insufficient to provide the etymology history you've asked for.

To properly address your question about French "alcool," I would need access to actual etymological sources that discuss:

- Early attestations of the term in French
- The evolution between "alcohol" and "alcool" variants
- The Arabic origin from *al-kuḥl* and its original meaning
- How the semantic range shifted from a cosmetic powder to distilled spirits

Without substantive source material, I cannot responsibly provide accurate etymological details while adhering to your requirement that responses be based solely on provided content. 

If you could share the actual lexical portal content or etymological articles about this word, I'd be happy to synthesize that information according to your specifications.
```


## [2026-09-06T20:40:12.874Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=alcohol",
 "prompt": "Give the American Heritage Dictionary entry for \"alcohol\" including its etymology (word history) line verbatim."
}
```


## [2026-09-06T20:40:13.382Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/khagan",
 "prompt": "Etymology of khagan: Old Turkic qaɣan, Mongolian, Rouran origin, relation to khan. Quote the etymology."
}
```


### [2026-09-06T20:40:18.940Z] TOOL RESULT

```
# Etymology of Khagan

According to the Wiktionary entry, the word khagan traces back to Old Turkic origins. The source states: "Ultimately from Old Turkic _𐰴𐰍𐰣_ (qaɣan)." 

The entry also notes that khagan is "a doublet of khan," meaning both words share a common etymological ancestor but diverged in form over time. The term ultimately derives from Old Turkic *qaɣan*, which became the basis for various related words across Turkic and Mongolian languages, reflecting its historical use as an imperial title among these peoples.
```


### [2026-09-06T20:40:19.224Z] TOOL RESULT

```
# American Heritage Dictionary Entry for "Alcohol"

**Definition:**
The entry provides three definitions: (1) hydroxyl compounds derived from saturated hydrocarbons with formula CnH2n+1OH, including ethanol and methanol; (2) "A colorless volatile flammable liquid, C2H5OH, synthesized or obtained by fermentation of sugars and starches" used as a solvent and in various products; and (3) intoxicating beverages containing ethanol as a group.

**Etymology Line:**
"[Medieval Latin, fine metallic powder, especially of antimony, from Arabic _al-kuḥl_ : _al-_, the + _kuḥl_, powder of antimony; see **kx̣l**]"

**Word History:**
The entry traces how the Arabic definite article "_al-_" combined with "_kuḥl_" (a powder used as eye cosmetic) became the Medieval Latin "alcohol." The term evolved through English usage from denoting fine powders to essences obtained through distillation, eventually referring specifically to ethanol in fermented liquors and ultimately to the broader class of chemical compounds known today as alcohols.
```


## [2026-09-06T20:40:28.000Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT Alkohol\"\ngrep -n -i 'alkohol\\|al-kuhl\\|al-kohl' LKT.txt | head -10\necho \"=== LKT Chan/Khan\"\ngrep -n -i '^chan\\b\\|Chan,\\|chagan\\|chakan\\|Khan' LKT.txt | head -20\necho \"=== LKT Kohl\"\ngrep -n -i 'kuhl\\|kohol' LKT.txt | head -10"
}
```


### [2026-09-06T20:40:28.074Z] TOOL RESULT

```
=== LKT Alkohol
2880:[Über  aram.  kuhlä  vielleicht  aus  ass. guhlu  ZAkkFW"  61]  'Spießglanzpulver (Schwefelblei)  zum  Färben  der  Augen- brauen, Wimpern  und  Lider'  [über  den Gebrauch  und  die  Zusammensetzung  der orientalischen  Augenschminke  vgl.HlLLE in  ZDMG  V,  236/242];  noch  im  16. Jahrhundert  ist  das  hieraus  entstandene Wort  Alcohol  in  der  Alchemie  der  ge- läufige Ausdruck  für  'trockenes,  feines Pulver',  erst  später  wurde  es  zur  Be- zeichnung des  Weingeistes  benutzt.  Die einzelnen  Formen  sind:  sp.  pg.  alquifol, alcofol,  alcofor,  alcohol,  kat.  alcofoll, frz.  alquifoux,  coheul,  alcohol,  it.  alcool, rum.  alcool;  ndl.  alkohol,  engl,  alcohol, dtsch.  Alkohol;  russ.  alkogoV.  —  [Pers. und  tk.  heißt  die  Augenschminke  übrigens sürme,  subst.  Inf.  des  tk.  Vbs.  siirmek 'glätten'  vom  Slamme  seb,  sit<>,  süp  'glatt,
7572:alkohol  1227
=== LKT Chan/Khan
836:[Pijn  38]  'Zuspeise  aus  gesalzenen  und dann  gestampften  und  getrockneten Fischchen  oder  dergl.  Hieraus  engl. balachan,  blachong  'ein  Fischgewürz  be- stimmter Art'.  [Dass.  wie  hier  Nr.  195.] [JAOS  XVII,  114-116.
1195:'Gerber',  ebenso  tk.  debbag;  hieraus rum.  täbäcar  'Loh-  oder  Rotgerber', täbäcärie  'Gerberei',  täbäci  'gerben'; bulg.  tabak  'Gerber'.  Mit  pers.  hänä 'Haus'  [s.  hier  Nr.  809]  ergab  sich  bulg. tabakhana,   serb.   tabakana  'Gerberei'.
1382:'Rauch',  duhän  sariba  'rauchen',  ebenso tk. ;  hieraus  bulg.  serb.  duhan  'Rauch- tabak', poln.  duchan,  klruss.  dochan, Cech.  dohan  'dass.'.
1958:Aus  liakän  [das  wohl  selbst  aus  dem Mongolischen  stammt],  ist  I.Name  der türkischen  und  mongolischen  Herrscher Miltfl.isiens,  etwa  'Kniser',  '■2.  eine  Art Adelsprädikat  im  heutigen  Persien  und Transkaukasien;  das  Wort  wird  in  dieser Bedeutung  nachgestellt,  z.  B.  Jahjä  Hän; hieraus  rum.  han  'Tatarenfürst';  bulg. serb.  hau,  cech.  chär},  poln.  klruss.  chan, russ.  hnn,  kagan,  kogan  'Herrscher  der Chasaren';  frz.  kan,  khan;  dtsch.  Chan. [Bern  SIEtWb  468.
1970:'Dolch';  tk.  hanger;  hieraus  bulg.  serb. handzar,  poln.  chandzinr,  koncerz, kindzal  [allein  noch  gebräuchlich] 'dass.', ßech.  koncif  'Rapier,  Stoßdegen',  russ. kinzal,  klruss.  cynhal  'Dolch',  russ. koncar,  koncan  'Schwert  mit  schmaler Klinge';  rum.  hanget;  it.  cangiaro  'Dolch mit  sehr  breiter  Schneide  und  ge- krümmtem Grift',  siz.  canciarru  'dass.', frz.  cangiar,  khanjar,  khandjar\  mit ar.  Art.  sp.  pg.  alfange  'Säbel',  frz.  (seit dem  17.  Jahrhundert)  alfange,  sp.  al- fanjazo  'großer  Säbel',  pg.  alfageme 'Dolch,  kurzes  Schwert'.   [Gorjajew  140.
2594:'Weiberhemd'  soll  das  Grundwort  zu mlat.  *ca>-cannum,  prov.  carcan,  afrz. charchan,  chercant,  frz.  carcan  'Hals- eisen' sein;  vgl.  G.  Meyer,  Etymologi- sches Wörterbuch  der  albanesischen Sprache.  Straßburg  1891.  S.  178.
3614:'Zeichen',  ebenso  tk.;  hieraus  russ.  mi- sen  'Zielscheibe,  Ziel';  frz.  nichan, dtsch.  Nischan  'tk.  Orden'.  [Gorj^ijew 211.    Devic  DEt  176.
6067:gutta-percha  712 I  gymkhana  710
=== LKT Kohl
2880:[Über  aram.  kuhlä  vielleicht  aus  ass. guhlu  ZAkkFW"  61]  'Spießglanzpulver (Schwefelblei)  zum  Färben  der  Augen- brauen, Wimpern  und  Lider'  [über  den Gebrauch  und  die  Zusammensetzung  der orientalischen  Augenschminke  vgl.HlLLE in  ZDMG  V,  236/242];  noch  im  16. Jahrhundert  ist  das  hieraus  entstandene Wort  Alcohol  in  der  Alchemie  der  ge- läufige Ausdruck  für  'trockenes,  feines Pulver',  erst  später  wurde  es  zur  Be- zeichnung des  Weingeistes  benutzt.  Die einzelnen  Formen  sind:  sp.  pg.  alquifol, alcofol,  alcofor,  alcohol,  kat.  alcofoll, frz.  alquifoux,  coheul,  alcohol,  it.  alcool, rum.  alcool;  ndl.  alkohol,  engl,  alcohol, dtsch.  Alkohol;  russ.  alkogoV.  —  [Pers. und  tk.  heißt  die  Augenschminke  übrigens sürme,  subst.  Inf.  des  tk.  Vbs.  siirmek 'glätten'  vom  Slamme  seb,  sit<>,  süp  'glatt,
7572:alkohol  1227
```


## [2026-09-06T20:40:29.866Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT alcohol\"\ngrep -n -i 'ALCOHOL' SKT.txt | head -5\necho \"=== SKT khan\"\ngrep -n -i '^KHAN\\|KHAN,\\| Khan\\b' SKT.txt | head -5\necho \"=== HJB khan\"\ngrep -n -i 'KHAN,\\|CATHAY' HJB.txt | head -10\necho \"=== DEV alcool\"\ngrep -n -i 'ALCOOL\\|alkohl' DEV.txt | head -10\necho \"=== PHN alcool\"\ngrep -n -i 'ALCOOL' PHN.txt | head -10"
}
```


### [2026-09-06T20:40:29.959Z] TOOL RESULT

```
=== SKT alcohol
23702:French  from  Arabic:  admiral,  alcohol, assassin,  barberry  (berberry),  bedouin,  calif (caliph),  cipher,  civet,  fardel?,  furl?,  ga- zelle, lute  (1),  Mamaloke  (Mameluke), mattress,  mohair  (moiic),  saflron,  sultaa.
=== SKT khan
=== HJB khan
749:Oodiiiho  de  Eredia.  Kalaea,  Llnde  Meri- diooale  et  le  Cathay,  MS.  orig.  auto- graphe  de,  reproduit  et  tradnit  par L  Janssen.    4to.    Bruxelles,  1882.
1574:The  grant,  by  Shah  'Akm,  in  1765, of  the  Dewanny  of  Bengal,  Behar,  and Orissa  to  the  Company,  transferred  all power,  civil  and  military,  in  those provinces,  to  that  body.  But  no  im- mediate attempt  was  made  to  under- take the  direct  detailed  administration of  either  revenue  or  justice  by  the agency  of  the  European  servants  of the  dompany.  Such  superintendence, indeed,  of  the  administration  was maintained  in  the  prior  acquisitions  of the  Company — viz.,  in  the  Zemindary of  Calcutta,  in  the  Twenty-four Pergunnas,  and  in  the  Chucklas (Chuckla]!)  or  districts  of  Burdwan, Midnapoor,  and  Chittagonc,  which  had been  transferred  by  tne  Nawab, Kaaim  'All  Khan,  in  1760  ;  but  in  the rest  of  the  territory  it  was  confined  to the  a£;ency  of  a  Resident  at  the Moorsnedabad  Durbar,  and  of  a 'Chief*  at  Patna.  Jiistice  was  ad- ministered by  the  Mohammedan courts  under  the  native  officials  of the  Dewanny.
1835:c.  A.D.  545. — "From  the  remoter  regions, I  speak  of  Tanista  and  other  places,  the imports  to  Taprobane  are  silk  Aloes-wood (aX^),  cloves,  sandal- wood,  and  so  forth." — Cosmos,  in  Cathay,  p.  clxxvii.
1893:There  is  reason,  however,  to  ascribe an  Indian  origin  to  the  term  ;  whilst the  practice,  apai-t  from  the  term,  is of  no  rare  occurrence  in  Indian  history. Thus  Tod  records  some  notable  in- stances in  the  history  of  the  Rajputs. In  one  of  these  (1634)  the  eldest  son of  the  Raja  of  Marwar  ran  Or^muck  at the  court  of  Shah  Jahan,  failing  in his  blow  at  the  Emperor,  but  killing five  courtiers  of  eminence  before  he fell  himself.  Again,  in  the  I8th  cen- tury, Bijai  Singh,  also  of  Marwar,  boi'e strong  resentment  against  the  Talpura prince  of  Hyderabac^  Bijar  Khan,  who nad  sent  to  demand  from  the  R&jput tribute  and  a  bride.    A  Bhatti  and  a
2157:1660. — ^'Despatches  about  this  time  ar- rived from  Mu'azEam  Khan,  reporting  his successive  victories  and  the  flight  of  Shuja to  the  country  of  Bakfaaog,  leaving  Bengal undefended. '^i[%4f^  Khdn,  in  miioL  vii. 254.
2380:c.  545.— "The  Choirelaphus  (*Hog.staff') I  have  both  seen  and  eaten." — Cosmos  In- dicopletates,  in  Cathay,  kc.,  p.  dzxv.
3160:Arabic,  Turkish,  and,  in  special  senses, into  European  languages,  and  eastward into  India,  where  it  has  generally  been adopted  into  the  vernaculars.  The popular  pronunciation  is  bdzdr.  In S.  India  and  Ceylon  the  word  is  used for  a  single  shop  or  stall  kept  by  a native.  The  word  seems  to  have  come to  S.  Euroj)e  very  early.  F.  Balducci Pegolotti,  in  his  Mercantile  Hand- book (c.  1340)  gives  Bazaiia  as  a Genoese  word  for  'market-place' {Cathay,  &c.  ii.  286).  The  word  is adopted  into  Malay  as  pdsOr,  [or  in the  poems  patara],
3428:o.  I860.— "Thus,  led  by  the  Divine  mer^, on  the  morrow  of  the  Invention  of  the  Holy Cross,  we  found  ourselves  brought  safely into  'jxrt  in  a  harbour  of  Senium,  oallea Pervuis,  over  asainst  Paradise."— Afori- gnolliy  in  Cathay^  u.  867.
4060:1330.— ''And  here  they  bum  the  tiraiU- wood  {verzino)  for  fuel  .  .  ,"~Fr.  Odoric,  in Cathay,  &c.,  p.  77.
4125:A.D.  1321.— "After  their  blessed  martyr- dom,  which  occurred  on  the  Thursday  before Palm  Sunday,  in  Thana  of  India,  I  baptised about  90  persons  in  a  certain  city  called Parocoo,  lO  davs'  journey  distant  there- from .  .  ."—Fnar  Jordanus,  in  Cathay, &c.,  226.
=== DEV alcool
356:Alcool.  Esp.  et  portug.  alcohol,  aragon.  alcofol^,  catal. (ilcofoIJ.  11  est  bien  démontré  que  l'étymologie  de  ce  mot est  l'arabe  J^=5^î  nl-kohl,  le  cobeul  ou  poudre  d'antimoine'^, dont  les  femmes,  en  Orient,  se  teignent  les  paupières.
478:-  Commerce  de  V Algérie,  p.  29  (dans  le  GJoss.  de  Do/y,  au  mot  alcool, p.  92  ).  M.  Dozy  n'a  [)as  nolo  le  Icime  alqiiijhl.
481:Alquifoux  est  donc  une  corruption  de  l'arabe  J.=^i  al- cohl,  altération  qui  paraîtrait  peut-être  difficile  a  admettre si  l'on  n'avait  les  intermédiaires  aholiol,  alcofol,  alquifol. (Voy.  Alcool.)
527:mente,  du  lait  de  coco,  de  la  sève  de  cocotier;  à  Bour- bon, c'est  de  l'alcool  de  canne  à  sucre.  Le  mot  populaire riquiqui  pour  eau-de-vie  est  peut-être  une  corruption  de 'araqï.
1259:Dans  la  terminologie  pharmaceutique,  éhxir  a  subi  une déviation  de  sens  analogue  à  celle  d'alcool;  le  mot  ne  se dit  plus  aujourd'hui  que  de  liqueurs  résultant  d'un  mé- lange de  certains  sirops  avec  des  alcoolats.
2483:Alcofol,  aragon.  voy.  Alcool.
2484:Alcofoll,  ca(aL  voy.  Alcool.
2485:Alcohol,  voy.  Alcool.
2486:Alcool.
2622:Alkohol,  voy.  Alcool.
=== PHN alcool
1206:temps, on écrit alcool sans h; mais c'est à tort : le second o est
```


## [2026-09-06T20:40:35.392Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT khan entry\"\nsed -n '1950,1962p' LKT.txt\necho \"=== LKT alcohol entry\"\nsed -n '2872,2884p' LKT.txt"
}
```


### [2026-09-06T20:40:35.451Z] TOOL RESULT

```
=== LKT khan entry
N.  pr.,  Sohn  des  Noe,  der  nach  Gen  9, 22  als  Urbild  aller  Schamlosigkeit  galt; hieraus  Jiäänta,  Jiänta,  honta  'me- retrix'  [zum  Über ^.'ang  von  tn  zu  n  vor dem  Dental  vgl.  jontef  <^  Jörn  <öß].  — OLZ  XXI,  202.
806.  Ar.  hammäl:
'Träger',  ebenso  tk. ;  hieraus  rum.  hamal 'Last-  und  Gepäckträger',  auch  mit  Meta- Ihesis  mahal,  dazu  hatnallc ;  bulg.  ha- mal, hamalin,  serb.  hamal,  poln.  hamal 'Lastträger' ;  angloind.  /mwwaMi 'Träger'; sp.  (dial.  in  Andalusien)  alhamel  'Last- tier; dessen  Führer',  it.  (dial.  in  Ligurien und  Kalabrien)  camälo  'Gepäckträger', gen.  camalä  'tragen',  prov.  camdlo,  frz. t'awte/oi 'Händler,  der  seine  Waren  markt- schreierisch anpreist',  daher  besonders 'Zeitungsjunge'.  [DE  135.  Eguilaz  187. ML  4021.  N ALLING  in  ZDMG  LI,  534. ZfromPh  XXIII,  334.  422.  RomForsch IV,  366.  Hobson-Jobson  429/430.  Bern SlEtWb  384.
807.  Ar.  hauisiu:
Vulg.  'fünfzig',  Bezeichnung  für  einen aus  der  Wüste  wehenden  Wind,  der  etwa 50  Tage  anhält;  hieraus  u.  a.  engl. kamsin,  khamsin.  —  [Andere  Ableitung aus  ostar.  ham  'Glut',  sin  'Wüste',  also 'Glut  der  Wüste'.]
Tk.  hüM.]
64
808.  Tk.  Ii��n:
Aus  liakän  [das  wohl  selbst  aus  dem Mongolischen  stammt],  ist  I.Name  der türkischen  und  mongolischen  Herrscher Miltfl.isiens,  etwa  'Kniser',  '■2.  eine  Art Adelsprädikat  im  heutigen  Persien  und Transkaukasien;  das  Wort  wird  in  dieser Bedeutung  nachgestellt,  z.  B.  Jahjä  Hän; hieraus  rum.  han  'Tatarenfürst';  bulg. serb.  hau,  cech.  chär},  poln.  klruss.  chan, russ.  hnn,  kagan,  kogan  'Herrscher  der Chasaren';  frz.  kan,  khan;  dtsch.  Chan. [Bern  SIEtWb  468.
809.  Pers.  liäu:
Auel)  hänä  'Haus'  [Horn  NpEt  S.  103, Nr.  4fi6  und  ANDKEAS  in  Festgabe  für Tlieodor  Nöldeke  zum  80.  Geburtstage. Göttingen  1916.  S.  4/6];  hieraus  tk.  han 'Herberge,  Wirtshaus',  rum.  han  'Gast- haus'.
810.  Ar.  Imiiaka:
'Halskette'  [vom  Vb.  hnnaka  'mit  einem Stricke  erwürgen';  das  Subst.  ist  wie hinaka  'Kragen'  erst  vulg.  gebräuchlich, vgl.  'Vatermörder'] ;  hieraus  siz.  it.  (dial. im  Süden)  canacca  'dass.'.    [ML  1860,
=== LKT alcohol entry
kian  Kämas  975;  vom  Stamme  kab,  kob 'anschwellen,  dick,  rund  und  hohl'  Väm- bery  TktEtWb  S.  64,  Nr.  71.  L];  hieraus rum.  cobur  'Pistolenhalfter';  bulg.  kubur, serb.  knbura  'kleine  Pistole,  Futteral  da- für', klruss.  kubur,  kobur,  russ.  kubura, kobura  'Lederfutleral,  Halfter'.  [Gorja- jew 147.    Bern  SlEtWb  636.
1224.  Ar.  kudäf:
'Schüssel,  irdener  Topf;  hieraus  mit  ar. Art.  und  Imäla  [ä  >  e]  pg.  alcadefe 'irdener  Topf,  über  den  die  zu  messenden Flüssigkeiten,  wie  Wein,  Öl  oder  dergl., gehalten  werden,  damit  das  Überfließende hinein  tröpfelt',  kat.  cadaf  [DE  78;  Con- stancio  Dicc  44  b].
1225.  Ar.  kufifa:
'Tiefer  Korb,  Tragkorb'  [aus  gr.  KÖqpivoq, lat.  cophinus  <C  lat.  cuppa,  vgl.  Lammens Farak  Nr.  1037];  hieraus  nach  der  vulg. Aussprache  mit  o  nach  einem  empha- tischen Laute  sp.  cofa,  cofe,  it.  coffa 'Mastkorb',  pg.  alcofa  'Korb',  cofo  'Kü- bel', siz.  coffa  'Marktkorb',  [mit  rom.  En- dung] it.  cöfano,  sp.  cuibano;  rum.  cofä 'Eimer,  Holzkanne'.  Afrz.  cofre,  frz. coffre,  engl,  coffer,  dtsch.  Koffer  [mit Anfügung  eines  -r  wie  in  Kaliber,  s.  hier Nr.  1030,  und  Kassiber,  hier  Nr.  1168]. Serb.  kofa  'Korb,  Mastkorb',  kofan  'Tru- he', öech.  kufr,  poln.  kufr,  klruss.  kufer 'Koffer'.  [DE  94.  Eguilaz  140.  StGlIt n,281.  GrSVociSic  232.  ML  2207  u.  4730.
1226.  Per^^.  küftäi:
'Gehackt'  [part.  pass.  von  küftän,  vgl. köftän  'stoßen,  treten'  Horn  NpEt  S.  288, Nr.  159],  hieraus  Ik.  köfte  zur  Bezeich- nung eines  Fleischgerichtes  'Fleisch- klößchen' [Kelekian  Kämus  1055  b],  rum. chiftea,  chiftelufa  'dass.',  bulg.  kufte, serb.  cufteta  'Fleischkloß'.
1227.  Ar.  knhl:
[Über  aram.  kuhlä  vielleicht  aus  ass. guhlu  ZAkkFW"  61]  'Spießglanzpulver (Schwefelblei)  zum  Färben  der  Augen- brauen, Wimpern  und  Lider'  [über  den Gebrauch  und  die  Zusammensetzung  der orientalischen  Augenschminke  vgl.HlLLE in  ZDMG  V,  236/242];  noch  im  16. Jahrhundert  ist  das  hieraus  entstandene Wort  Alcohol  in  der  Alchemie  der  ge- läufige Ausdruck  für  'trockenes,  feines Pulver',  erst  später  wurde  es  zur  Be- zeichnung des  Weingeistes  benutzt.  Die einzelnen  Formen  sind:  sp.  pg.  alquifol, alcofol,  alcofor,  alcohol,  kat.  alcofoll, frz.  alquifoux,  coheul,  alcohol,  it.  alcool, rum.  alcool;  ndl.  alkohol,  engl,  alcohol, dtsch.  Alkohol;  russ.  alkogoV.  —  [Pers. und  tk.  heißt  die  Augenschminke  übrigens sürme,  subst.  Inf.  des  tk.  Vbs.  siirmek 'glätten'  vom  Slamme  seb,  sit<>,  süp  'glatt,
99
[Tk.  kujruk.
rein,  glätten',  Causativ  süpür  silr, Vämbery  TktEtWb  S.  148,  Nr.  160.] [Mahn  EtUnt  107.  DE  42.  Eguilaz  140. Devic  DEt  13.  28/29.  Lammens  Rem 20/21.  RomForsch  IV,  364.  ML  4732. Kluge  11.
1228.  Tk.  kujruk:
```


## [2026-09-06T20:40:35.959Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DEV alcool entry\"\nsed -n '350,365p' DEV.txt\necho \"=== PHN alcool\"\nsed -n '1195,1215p' PHN.txt"
}
```


### [2026-09-06T20:40:36.013Z] TOOL RESULT

```
=== DEV alcool entry
à 9.  Zengifur,  zingifur,  uzijur,  iizufar,  azemafor,  cinabre; de  v*^3  zindjafr  ou  zoundjoiifr,  même  sens.  Le  portugais azinhavrc,  vert-de-gris,  est  certainement  le  même  mot, quoique  M.  Dozy  ait  voulu  le  rattacher  à ^l^^^  zindjâr.  (Voy. ci-dessus  azagor.^  Remarquez  que  azinhavre  sonne  presque à  l'oreille  comme  cinabre,  et  reproduit  lettre  pour  lettre l'arabe  y^J^  az-zindjnfr.  Quant  à  sa  signification,  vert-de- gns  au  lieu  de  cinabre ,  il  ne  faut  pas  s'en  étonner;  les  al- chimistes, dans  leurs  dénominations,  confondaient  presque constamment  des  substances  qui  ne  nous  seniblent  plus avoir  que  des  analogies  lointaines.  Dans  le  cas  particulier dont  il  s'agit,  je  puis  citer  à  fappui  de  ma  correction: zynfer,  vert-de-gris;  a^i'mar  "^j  vert-de-gris  et  cinabre ;aza- mar,  azemala,  qui  embrassent  également  ces  deux  signifi- cations.  N'oublions  pas  que  le  vert-de-gris  et  le  cinabre
^  Martin  Rnland  écrit  michach,  micha;  ce  sont  des  erreurs  de  lecture, d'ailleurs  faciles  à  commettre  avec  des  manuscrits  où  les  points  sur  les  i  ne sont  pas  marqués.
-  '^  Azimnr  me  paraît  ime  faute  de  copiste,  pour  nziniar.  (Voy.  ci-dessus nznfror.  )
DES  MOTS  D'OIUGIiNE  ORIENTALE.  13
(coiiroïKlii  avec  le  luiiiiuni')  lont  tous  deux  partie  de  la classe  des  zadj  ou  vitriols.
5o.  Zub,  ziibd,  zcIhJ,  beurre,  de  Jo^  zoiibd,  rneme  sens.
Alcool.  Esp.  et  portug.  alcohol,  aragon.  alcofol^,  catal. (ilcofoIJ.  11  est  bien  démontré  que  l'étymologie  de  ce  mot est  l'arabe  J^=5^î  nl-kohl,  le  cobeul  ou  poudre  d'antimoine'^, dont  les  femmes,  en  Orient,  se  teignent  les  paupières.
On  sait  que  ce  mot  a  été  employé  à  désigner  un  grand nombre  de  collyres  divers,  tels  que  yX^\  JA^,  y^s]  J^, y/yS.  jX,  etc.  Alcohol,  dans  l'ancienne  pharmacie,  se  disait de  toute  substance  porphyrisée  :  ^^Les  pierreries,  dit  Moïse Charas  ^,  les  bols,  les  terres,  le  succin,  les  dyamants  et quelques  parties  d'animaux  sont  réduits  en  poudre  impal- pable qu'on  nomme  alkohol.v  Comment,  après  ayoir  dé- signé une  poudre  sèche,  le  mot  est-il  arrivé  à  s'appliquer au  liquide  obtenu  par  la  distillation  des  matières  spiri- tueuses?  On  peut  en  voir  la  raison  dans  cette  explication citée  par  Martin  Ruland  :  r^Alkol  est  purior  substancia rei,  segregata  ab  impuritate  sua.  Sic  alkol  vini  est  aqua ardens  rectificata  et  mundissima  ^.  w  Nous  avons  un  exemple d'un  changement  pareil  dans  le  sens  moderne  ^'élixir.  (Voy. ce  mot.)
^  Les  anciens,  Pline,  Vitruve,  Gaiien,  confondent  sans  cesse  le  cinabre et  le  minium.  Dans  le  Dioscoride  latin  do  J.  Ruel  (  i5i6),  celle  confusion est  relevée  en  ces  termes  :  «  Argentum  vivuni  lit  ex  minio ,  qiiod  abusive  cin- vabaris  dicilur.55  (Lib.  V,  cap.  ci,  fol.  820  recto.)  Dans  ce  passage,  c'est  pré- cisément rinverse  qu'il  faudrait  dire,  d'après  notre  terminologie  actuelle; car  le  cinabre  est  un  sulfure  de  mercure,  et  le  minium  un  oxyde  de  plomb.
-  Àlcofol,  id  est  Anthimonium.  (Man.  lat.  du  xiv"  siècle,  n"  7i5G  de  la r)il)l.  nat.  p.  Ao.)
^  Ou  plutôt  de  sulfure  de  plomb.  (Voy.  Alquifoux.)  Le  cobeul,  en  Perso et  en  Turquie,  est  souvent  appelé  a«.™w  mrmeh,  mot  quelquefois  employé dans  les  relations  des  voyageurs  français.
■'   Pharmacopée  royale,  a'édit.  1682,  l.  P',  p.  3i',.
■■  Lexicoii  alch eniia.'  {iGHii),  p.  3o.
\U  DICTIONNAIRE  ETyMOLO(iIQUE
Alcohan.  Transcription  de  l'aral)c  ^^yt^^  al-qorân.  Al est  l'article;  aussi  dit-on  de  préférence  aujourd'hui  1r Coran.  (jUi  qorân  signiCie  proprement  lecture,  récitation. ^Le  Coran,  dans  sa  forme  primitive,  était  une  récita- tion plutôt  qu'une  lectm^e,  et   c'est   dans  ce  sens   qu'il
faut  entendre  le  verbe  i^Jj  qaraa^  dans  plusieurs  des  pas- sages où  on  l'a  traduit  par  lire.  ?5  (E.  Renan  ^)
=== PHN alcool
désignait communément certains corps réduits en poudre très*
fine; et c'est seulement par allusion à la subtilité de cette
poudre que les chimistes européens ont nommé alcohol l'esprit-
de-vin, car le nom de cette dernière liqueur n'a pour équi-
valent en arabe que i^\ ^yj \rouli' el^araqy^^ traduction lit-
térale du français. — Arnaud de Villeneuve, alchimiste et
professeur de médecine à Montpellier, passe pour avoir décrit
le premier l'art d'extraire Vakohol des liqueurs en fermentation
et découvert les acides sulfurique, muriatique et nitrique, ainsi
que l'essence de térébenthine. Ce savant, né en i a38, à Ville-
neuve en Languedoc, mourut en i3i4. — Depuis fort long-
temps, on écrit alcool sans h; mais c'est à tort : le second o est
simplement euphonique, et la lettre ^ V, qui est radicale, ne
peut être supprimée sans défigurer le mot arabe, qui se trouve
alors réduit aux seules lettres alcol et n'offre plus de sens.
ALCORAN,s. m, (a.)
fj\'^^\ \^alqourAn^ la lecture, dérivé de i^ [çarfï/f] lire. —ALC 21
Akorati signifie la lecture par excellence : cW ainsi que nous
disons la Bible, rÉcriture, en attachant à ces mots une idée de
respect tout particulier. — Code religieux, moral et politique,
des musulmans, l'AIcoran se divise en 36 cahiers ou sections,
```


## [2026-09-06T20:40:49.836Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN han\"\ngrep -n -i 'chān\\|hân\\|Herberge' HRN.txt | head -15\necho \"=== HUB\"\ngrep -n -i 'chan\\b' HUB.txt | head -10\necho \"=== PLA khan\"\ngrep -n 'ẖān\\|hān\\|khān' incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-06T20:40:49.914Z] TOOL RESULT

```
=== HRN han
=== HUB
9795:biriinT, iibersetzt von Sachan p. 57) = zd.
=== PLA khan
```


## [2026-09-06T20:40:51.276Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM khan\"\ngrep -n 'الخان\\|( خان\\|خان )' AFM_pages.txt | head -10\necho \"=== TAD\"\ngrep -n 'خان' TAD_pages.txt | head -10\necho \"=== FVQ kuhl\"\ngrep -n -i 'kuhl\\|kohl\\|antimony' FVQ_pages.txt | head -10"
}
```


### [2026-09-06T20:40:51.353Z] TOOL RESULT

```
=== AFM khan
=== TAD
697: ‫التركية تنباكووهو المعروف بالدخان ويعضهم يقول نتن من التركية « لوبون ‪6‬‬
698:                                 ‫ومعناه دخان وعرابه بعض الاطياء ‪ 2‬طباق »‪6‬‬
940:‫‪ 6‬العبراني‬      ‫خان أي فال ماف يعارت الارابي وهومشئق ‪4 2‬‬
952:             ‫ظ‬                ‫خانة‪ :‬فارسى'«خانة© مسناهبيت‬
1052:‫بومائدة وده ]نات لخانفة خل هل الكانية تزايا ‪#‬مرزادفييا عاج وقد‬
1762:           ‫طرخان ‪ --‬فارسي « ترخان‪ 6‬وهو زعم قوم معفى من الضراشب‬
2806:                        ‫ايطالى(وسسدة)م‬                  ‫وأور ‏ دخانالشحر‪-‬‬
2808:                                                              ‫دخان الشحم وغيره‬
=== FVQ kuhl
```


## [2026-09-06T20:41:01.366Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\n# leaf = printed + 21\nprint(t[103+21][:1800])\nEOF"
}
```


## [2026-09-06T20:41:01.826Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '935,960p' TAD_pages.txt"
}
```


### [2026-09-06T20:41:03.140Z] TOOL RESULT

```
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


### [2026-09-06T20:41:03.173Z] TOOL RESULT

```
                                        ‫خاتان عد وك معاة البناطان الاعفلم‬
              ‫ار‪-‬سي ترك وهو الامير والسيد ولقب سلاطين تركستان‬
                                                            ‫خفان‬
‫‪ 6‬العبراني‬      ‫خان أي فال ماف يعارت الارابي وهومشئق ‪4 2‬‬
     ‫‪0‬‬   ‫‪5‬‬          ‫َه‬   ‫هَ‬         ‫‪.‬‬          ‫‪2‬‬              ‫م‬    ‫‪6‬‬

‫الذي معناه خيم أي نصب الخيام واقام وتزل وحل وجيش ومنه حانوت اي‬
                                                                            ‫‪٠‬‬   ‫‪8‬‏‬




                                          ‫خمارة ودكان ومتزّل القوم‬
              ‫ا‬
  ‫(‪ )1‬وهوعند المولدينالغابة وفصيحه الحسر جة وهو مجتمعالشجر حرج ورحجات‬
             ‫ظ‬                ‫خانة‪ :‬فارسى'«خانة© مسناهبيت‬
‫خام‪ -‬فارسبي«خام»معناهفجويطلقعلىالرجلغيرالمجرب وعلىالثوب‬
                                                     ‫مقنن غيرالمفسول‬
                         ‫ختن ل أراي « حتا» معناعرو جع رفن‬

 ‫فارسي «خدنو» معناه امالك والامير والسيد وفيالتريمعناهوزبر‬      ‫‪5‬‬
               ‫خراطين ‪ -‬فارسي ‪ 2‬خراتين » معناه دود متكون فيالطين‬
 ‫خربق ‪ .-‬فارسي « خربق » وهو نبات ورقه كاسان الخحل ويقال لفهي‬
                                                        ‫العربية قائل الذئب‬
```


## [2026-09-06T20:41:20.972Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (174,):\n    print('==== printed',i+542)\n    print(t[i][:2600])\nEOF"
}
```


### [2026-09-06T20:41:22.963Z] TOOL RESULT

```
==== printed 716
   ‫‪۷۱۹‬‬                                                                                ‫تنس‬

‫شاخ آن مرغ‌است وازآن زهگیر تراشند ودستةٌ‬        ‫از آنجاآورند ‪ -‬ویمعنی فریبنده همبنظر آمده‬
‫‪.‬ویند خاصیتش آست که اکر‬    ‫کارد لیزسازند گ‬                                            ‫است ‪#.‬‬
‫در جابی چیزی مسموم با طعامی بزهر آغشته‬          ‫ختثیر = بابای ابجد بر وزن فلندر ‪۰‬‬
‫بیاورند اآزن شاخ علامتی ظاهرمیشود » و بسنی‬      ‫مقلی راکوبند که لاف توانگری زند وخود را‬
‫گفته اند شاخ ماراست و هر گاه ازعمر مارهزار‬       ‫ورعکس هم بنظر آمده است‬
                                                                      ‫مالدار وانماید » ب‬
‫سال بگذردشاخ برمی‌آورد » وبعضی گوبند شاخ‬              ‫یعتی توانگری که شکوء مفلی کند ‪# .‬‬
‫افعی است وبسضی دبگر کویند شاخ‌ماهی‌وال (‪)۱‬‬      ‫خقو د منم اول و الی بواو رسیده »‬
‫است * وسمتی دیگرگفته‌اند دندان جانوری‌است‪:‬‬
                                                 ‫وسنی‬
                                                    ‫شاخ گاوی است که درملك چین‌مساشد *‬
                              ‫اله (‪ )۲‬اعلم‪. ۱‬‬     ‫هگ‌راند‬
                                                        ‫گجفمتدی‬
                                                              ‫کوبند شراکخدکن‌است ‪ ۰‬و‬
‫‏‪ a‬بروزن بروانه‪ .‬حامه ولسای‬   ‫حتوانه‬
                                                ‫که در مابین ملك چین و زنگبار ملکی است‬
              ‫پشمينة دروبتان وفقیران باشد ‪.‬‬     ‫خراب ودرا نجامرغی میشود بغایت بزر که واین‬

                              ‫() چك‪ .‬چش ‪ :‬وال ‪.‬‬            ‫(‪ )۱‬چك » چش ‪ :‬زال ‪.‬‬
 ‫‪ ۱‬بیرونی در « زکرالختو » آرد ‪ :‬ک«نت سالت‌الرسل‌الواردین من قتای‌خان عنه فلم‬
  ‫نفی‌الکتب‬
          ‫اجد عندهم سبباللرغبة فيه غیرالعرق من‌السم و اله عظم جبهة شور » و هکذا کر‬
  ‫بزبادة ان هذا الثور کون بارش خرخیز » و فحن‌تری له من‌الفلظالزائد علی‌عرض‌الاصبعین مابکاد‬
  ‫یستحیل معه‌ان‌بکون عظم جبهة مع‌صفرجثة ثبران التركك وسیرالفرن اولی به‌ولوسدق ماقیللعان‬
 ‫جلبهالی الاوعال من خرخیز اولی‪,‬هلانهم اليه‌اقرب ولم بجلب من‌العراق وخرامان وقدقبل‌فیه ایض‬
  ‫مائی وسمی فلا مائاً ‪« ۰...‬الجماهر ‪ ۹۰۲۲ - ۸۰۲‬ونظراین مطالب درصيدنة‬          ‫ن‬
                                                                              ‫کهةدکر‬
                                                                                   ‫انه جب‬
  ‫بیروتی آمده ‪ .‬ارلكج‪:‬ماهر ‪ ۸۰۲‬ح ‪ . ۲‬دانشمندان قول اخیر را صحیح دانته اند » چه‬
 ‫مکنوع‌ماهیی است که بفراسوی ‪ 12۷722‬و بانگلیی ‪ 12517721‬و بلمآانی ‪ 13۷۲4‬کوبند‬
  ‫که از اسکاندیناوی مأخوذست و در اصطلاح علمی آنرا ‪ 8000201۷1 50۲6608021‬کوبند‬
  ‫واز نوع فطاس ‪ ( 5602060‬وابته بنوع وال [ رجوع به وال شو
```


## [2026-09-06T20:41:36.433Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/khan' \\\n 'https://www.etymonline.com/word/khan' \\\n 'https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%86' \\\n 'https://en.wiktionary.org/wiki/khagan' ; do\npython3 tools/fetch_source.py \"$u\" --note 'pdf page 266, roots Khan / Khitan: English khan title, Persian/Arabic khan, Turkic qagan' 2>&1 | tail -2\ndone"
}
```


## [2026-09-06T20:41:37.877Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/Cathay' \\\n 'https://www.etymonline.com/word/Cathay' \\\n 'https://en.wikipedia.org/wiki/Kingdom_of_Khotan' ; do\npython3 tools/fetch_source.py \"$u\" --note 'pdf page 266, root Khitan: Cathay < Qitan; Khotan is a separate Saka name' 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T20:41:38.600Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/36412886acf8cbda.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb6db5a59bf65f0f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bfc7359cbf854d00.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/67d40b57e25141d8.txt
```


### [2026-09-06T20:41:41.157Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d23e9c0145479801.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35481ca8ac8a7bb2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3e89c11d67c77cb6.txt
```


## [2026-09-06T20:41:45.290Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/alcohol' \\\n 'https://www.etymonline.com/word/alcohol' \\\n 'https://en.wiktionary.org/wiki/%D9%83%D8%AD%D9%84' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%84%DA%A9%D9%84' \\\n 'https://www.ahdictionary.com/word/search.html?q=alcohol' ; do\npython3 tools/fetch_source.py \"$u\" --note 'pdf page 266, root K.h.l: Arabic kuhl > ML alcohol > French alcool > Persian الکل' 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T20:41:48.292Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7512ef796f3dc239.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ad7d93151ff9988.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/62afb99e2ebecf7b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6b89e1ea873cd4c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/04d8cf9d11596b94.txt
```


## [2026-09-06T20:41:52.964Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== etymonline alcohol\"\nsed -n '1,60p' 3ad7d93151ff9988.txt\necho \"=== ahd\"\ngrep -n -i 'kuhl\\|antimony' 04d8cf9d11596b94.txt | head -5"
}
```


### [2026-09-06T20:41:53.020Z] TOOL RESULT

```
=== etymonline alcohol
URL: https://www.etymonline.com/word/alcohol
FETCHED: 2026-09-06T20:41:47Z
STATUS: 200
TITLE: Alcohol - Etymology, Origin & Meaning

Alcohol - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of alcohol 

 alcohol (n.) 

 1540s (early 15c. as alcofol ), "fine powder produced by sublimation," from Medieval Latin alcohol "powdered ore of antimony," from Arabic al-kuhul "kohl," the fine metallic powder used to darken the eyelids, from kahala "to stain, paint." The al- is the Arabic definite article, "the."

 Paracelsus (1493-1541) used the word to refer to a fine powder but also a volatile liquid. By 1670s it was being used in English for "any sublimated substance, the pure spirit of anything," including liquids.

 The sense of "intoxicating ingredient in strong liquor" is attested by 1753, short for alcohol of wine , which then was extended to the intoxicating element in fermented liquors. The formerly preferred terms for the substance were rectified spirits or brandy .

 In organic chemistry, the word was extended by 1808 to the class of compounds of the same type as this (a 1790 translation of Lavoisier's "Elements of Chemistry" has alkoholic gas for "the combination of alkohol with caloric").
 also from 1540s 

 Entries linking to alcohol 

 brandy (n.) 

 "spirits distilled from other liquors" (especially wine), 1650s, abbreviation of brandy-wine (1620s) from Dutch brandewijn "burnt wine," earlier brand-wijn , so called because it is distilled (compare German cognate Branntwein and Czech palenka "brandy," from paliti "to burn"). The Brandywine Creek in Pennsylvania, site of the 1777 Revolutionary War battle, supposedly was so named 17c. by the Dutch explorers for the color of its waters.

 In familiar use abbreviated as 
 brandy as early as 1657; but the fuller form was retained in official use (customs tariffs, acts of parliament, etc.) down to the end of 17th c., being latterly, as the spelling shows, regarded as a compound of 
 brandy + 
 wine . [OED]

 alcoholic (adj.) 

 1790, "of or pertaining to alcohol;" see alcohol + -ic . The meaning "caused by drunkenness" is attested by 1872; the meaning "habitually drunk" by 1910. The noun sense of "one who is addicted to drinking in excess, chronic drunkard, old rounder" is recorded from 1891; an earlier term for one was alcoholist (1877 in clinical writing, earlier in temperance literature this word simply meant "a drinker of alcohol"). Alcoholics Anonymous was founded 1935 in Akron, Ohio, U.S.

 alcoholism 
 chloral 
 gasohol 
 kohl 
 synovia 
 al- 
 -ol 
 See All Related Words (9) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore
=== ahd
50: [Medieval Latin, fine metallic powder, especially of antimony, from Arabic al-ku ḥ l : al- , the + ku ḥ l , powder of antimony; see kx̣l in the Appendix of Semitic roots .]
51: Word History: The al- in alcohol may alert some readers to the fact that this is a word of Arabic descent, as is the case with algebra and alkali, al- being the Arabic definite article corresponding to the in English. The second part of the word, -cohol, comes from Arabic ku ḥ l, the word for a fine powder (most often made from antimony) used as a cosmetic to darken the eyelids. In fact, ku ḥ l has given us the word kohl for such a preparation. The Arabic phrase al-ku ḥ , "the kohl," was borrowed into Medieval Latin as one word, alcohol, "ko ḥ l." From Medieval Latin it was borrowed into English in the 16th century. In English, alcohol came to refer to any fine powder produced in a number of ways, as by heating a substance to a gaseous state and then cooling it. Alcohol could also be used to refer to essences obtained by distillation. One of these distilled essences produced by alchemists and early chemists, known as alcohol of wine, was the constituent of fermented liquors that causes intoxication, and the term alcohol came to refer to this essence (what modern chemists would call ethanol ) in particular. Eventually, the liquors that contained this essence began to be called alcohol, too. In the terminology of modern chemistry, alcohol has also come to refer to the class of compounds to which ethanol belongs.
```


## [2026-09-06T20:42:26.909Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'کحول' MON_part1.txt MON_part2.txt | head -5\necho \"--- render page\"\npdftoppm -f 266 -l 266 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg266 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T20:42:28.811Z] TOOL RESULT

```
Exit code 1
MON_part2.txt:63788:مکحول: ات۳۵۱۵ [ع.] (امف.) سرمه کشیده 
--- render page
I/O Error: Couldn't open file 'EtymologicalDictionary-persian-english.pdf': No such file or directory.
```


## [2026-09-06T20:42:32.102Z] TOOL CALL #62: Bash

```json
{
 "command": "pdftoppm -f 266 -l 266 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg266\" && ls -la \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/\""
}
```


### [2026-09-06T20:42:34.826Z] TOOL RESULT

```
total 4476
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 16:42 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     132 Sep  6 16:34 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   96095 Sep  6 16:39 av_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  113038 Sep  6 16:40 av_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  103258 Sep  6 16:39 av_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22433 Sep  6 16:39 ffd61_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73736 Sep  6 16:39 ffd61.png
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb  105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb  346511 Sep  6 16:39 root262.png
-rw-rw-r-- 1 sfmqrb sfmqrb 2985742 Sep  6 16:39 skt1882.txt
```


## [2026-09-06T20:42:37.834Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg266.png"
}
```


### [2026-09-06T20:42:38.313Z] TOOL RESULT

```

```


## [2026-09-06T20:42:38.311Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T20:42:54.080Z] TOOL CALL #64: Bash

```json
{
 "command": "cd \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\"\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg266.png')\nprint(im.size)\nim.crop((1750,1830,2000,2020)).resize((750,570)).save('crop_kohul.png')\nim.crop((1180,1930,2000,2050)).resize((1640,240)).save('crop_alk.png')\n\"\nls"
}
```


### [2026-09-06T20:42:56.097Z] TOOL RESULT

```
(2550, 3300)
agents.txt
av_box2.png
av_box3.png
av_box.png
coord_pg262.png
crop_ak2.png
crop_ak.png
crop_alk.png
crop_gr.png
crop_kohul.png
crop_lat2.png
crop_lat.png
crop_me2.png
crop_me.png
crop_op2.png
crop_op.png
crop_pers.png
ffd61_crop.png
ffd61.png
jscheck.js
p262-g01.json
p263hi.png
pg261.png
pg262.png
pg263.png
pg264hi.png
pg264.png
pg266.png
root262.png
skt1882.txt
```


## [2026-09-06T20:42:58.358Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_kohul.png"
}
```


### [2026-09-06T20:42:58.389Z] TOOL RESULT

```

```


## [2026-09-06T20:43:07.119Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB alcohol\"\ngrep -n -i 'al-kuhl\\|al kuhl\\|alcohol, n\\|alkuhl' WEB_vol1.txt | head -5\necho \"=== FSD alcohol\"\ngrep -n -i 'al-kuhl\\|alkohl\\|al-koh' FSD_vol1.txt | head -5\necho \"=== FSD khan\"\ngrep -n -i 'khan.*khaqan\\|khaqan' FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt | head -5\necho \"=== TTS khan\"\ngrep -n -i 'chan\\b\\|chakan\\|kaghan' incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -15"
}
```


### [2026-09-06T20:43:07.235Z] TOOL RESULT

```
=== WEB alcohol
=== FSD alcohol
=== FSD khan
=== TTS khan
870:Abbasi  und  im  Lugati-turki  des  Fazl-ullah  Chan  (vgl.  meine 
2235:lullah  Chan);  etJcc,  e^eZ'e  =  Oheim. 
3769:kk.  nat,  ujat  =  Schanäe. 
4410:Form  chan  entstanden;  kcxunalc,  Tioparmak,  Ifovanmah, 
5959:setzen  lassen;  kotmaJc  (nach  Fazlullah  Chan's  Wörterbuch) = 
8393:baden  {^jXiy^yi  ob  Lugati  FazluUah  Chan),  in  welcher 
8792:Von  sek  existirt  nach  dem  Lugati  Fazlullah  Chan  eine 
10090:=  Fenster  (nach  Lugati  Fazlullah  Chan);  tünglüJc,  tiiuliik 
10196:tarchan,  terchan,  uig.  iarkan,  das  wir  gewöhnlich  mit  Fürst, 
10931:Fazlullah  Chan);  ^7^  =  Zierde;  ;oMawTOaZ;  =  sich  bekleiden.
```


## [2026-09-06T20:43:11.727Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4400,4420p' incoming/TTS/TTS_vambery1878_uoft_djvu.txt\necho \"---\"\ngrep -n -i 'kaghan\\|kagan\\|chakan\\|chan  =  Fürst\\|Chan (Fürst)\\|Herrscher' incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -15"
}
```


### [2026-09-06T20:43:11.787Z] TOOL RESULT

```
blase ;  Teaburmak  =  aufwühlen ;  Jeaburti  =  Auflauf,  Lärm, 
Gewühl ;  Ifoburulp  =  aufgeblasen ,  aufgedunsen ;  kapcah, 
ijsijjm^  —  hohl,  leer;  ^-«ftaw  =  gross ,  stark,  hoch  —  und 
von  diesem  dünkt  mir  nach  Weglassung  des  labialen  Aus- 


65 

lautes,  rcspectivc  Inlautes  das  mong.-türk.  Man  =  Fürst, 
Oberhaupt  entstanden  zu  sein.  Von  Man  ist  die  neuere 
Form  chan  entstanden;  kcxunalc,  Tioparmak,  Ifovanmah, 
h'ovanz  (wie  oben). 

kaz.  liohniah  =  aufstehen;    ]^obsulamak  =  sich  aufblasen,    stolz 

sein. 
It.    ,Ji'a^  =  viel,  Menge,  hundert;    ämö«^  =  Freude ;   ik:tibu-ihi — 
freudig;  Zroftra^*  =  Brücke  (vgl.  höprii). 

.)sm.  Imvuk,  kovuh,  Ä-oö^ti  =  Blase ,  Hut,  Mütze;  ^'la&a«;  =  Kür- 
bis; /(fffl&Mn«aÄ  =  anschwellen. 
---
1557:uig.  «7jX"  =  Prinz,  Herrscher,  Vorderseite,  Erster;  ilkerü,  ilrii—-
```


## [2026-09-06T20:43:17.032Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T20:43:17.074Z] TOOL RESULT

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


## [2026-09-06T20:43:19.418Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T20:43:19.463Z] TOOL RESULT

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


## [2026-09-06T20:50:17.159Z] TOOL CALL #70: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-266.json",
 "content": "{\n  \"pdf_page\": 266,\n  \"book_page\": 236,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Khan\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Old Turkic qan 'lord, prince', contraction of qaɣan 'supreme ruler'; the title itself probably taken over from the Rouran/Xianbei (para-Mongolic) chanceries of the 4th–5th c. CE\",\n      \"note\": \"The root box labels the word 'Mongolian'. That is Klein's own wording (KLN p.844: 'fr. Turki khan, contraction of khaqan, \\\"ruler, sovereign\\\", which is prob. of Mongolian origin'), and Vámbéry (TTS p.65) and Lokotsch (nr. 808) say the same: Turkish hān is the younger form of kaan/hakan, itself 'wohl selbst aus dem Mongolischen'. Modern Turcology (Wiktionary, Etymonline, Doerfer/Clauson tradition) reverses the emphasis: the attested chain is Old Turkic 𐰴𐰍𐰣 qaɣan > qan, first epigraphically Turkic (Orkhon), with the title probably borrowed into Turkic from the Rouran/Xianbei, i.e. para-Mongolic rather than Mongolian proper; Middle Mongol qaɣan is itself likely a re-borrowing. So 'Mongolian' is a defensible but out-of-date label — hence plausible, not confirmed. The gloss 'ruler' is right.\",\n      \"note_fa\": \"عنوان ریشه در نمودار «مغولی Khan: فرمانروا» است. این همان تعبیر کلاین (ص ۸۴۴) است که خانِ فارسی و عربی را از ترکی khan، کوتاه‌شدهٔ khaqan، و آن را «احتمالاً مغولی‌تبار» می‌داند؛ وامبری (ص ۶۵) و لوکوچ (شمارهٔ ۸۰۸) نیز همین را می‌گویند. اما ترک‌شناسی امروزی صورت کهن را ترکی باستان qaɣan (سنگ‌نوشته‌های اورخون) می‌داند که در ترکی به qan کوتاه شده، و خاستگاه خودِ لقب را نه مغولی معیار بلکه زبان روران/سیانبی (شبه‌مغولی) می‌شمارد؛ qaɣan مغولی میانه احتمالاً وام‌گیری دوباره است. بنابراین برچسب «مغولی» پذیرفتنی ولی کهنه است و معنای «فرمانروا» درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/khan\",\n        \"https://en.wiktionary.org/wiki/khagan\",\n        \"https://www.etymonline.com/word/khan\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:844\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 20647, immediately after the printed page marker '844': 'khan, n., a title of ruler in Mohammedan countries. — Pers. and Arab. khan, \\\"lord, prince\\\", fr. Turki khan, contraction of khaqan, \\\"ruler, sovereign\\\", which is prob. of Mongolian origin.' The page number is exact and Klein does assert both the Turkic contraction and the Mongolian ultimate origin.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"LKT\", \"where\": \"nr. 808 (Tk. hān)\", \"stance\": \"partial\", \"note\": \"'Aus hakān [das wohl selbst aus dem Mongolischen stammt], ist 1. Name der türkischen und mongolischen Herrscher Mittelasiens, etwa \\\"Kaiser\\\", 2. eine Art Adelsprädikat im heutigen Persien und Transkaukasien … hieraus rum. han, bulg. serb. han, russ. han, kagan … frz. kan, khan; dtsch. Chan.' Lokotsch agrees on Turkic ← Mongolian, but routes the European words straight from Turkish, not through Persian/Arabic.\"},\n        {\"src\": \"TTS\", \"where\": \"p. 65 (s.v. kaba/kaan)\", \"stance\": \"supports\", \"note\": \"Vámbéry: '… das mong.-türk. kaan = Fürst, Oberhaupt entstanden zu sein. Von kaan ist die neuere Form chan entstanden' — the same qaɣan > qan contraction the chart's root presupposes.\"},\n        {\"src\": \"TAD\", \"where\": \"p. s.v. خاقان (TAD_pages.txt l.936)\", \"stance\": \"supports\", \"note\": \"al-Unaysi: 'خاقان: فارسي ترك وهو الامير والسيد ولقب سلاطين تركستان' — khāqān is a Turkic title, 'the prince and lord, title of the sultans of Turkestan'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Turkish\",\n          \"words\": \"khan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Old Turkic 𐰴𐰍𐰣 qaɣan 'supreme ruler' (Orkhon inscriptions, 8th c.) lost its intervocalic -ɣ- and contracted to qa'an > qan, which in Ottoman/Chaghatay is written خان hān and is the ordinary word for a Turkic or Mongol sovereign. Vámbéry states the change explicitly ('von kaan ist die neuere Form chan entstanden'), and Klein and Lokotsch both take the underlying qaɣan to be a loan from the Mongols (i.e. the Rouran/Xianbei chanceries of the 4th–5th c.). The arrow Mongolian → Turkic is therefore defensible in Nourai's (Klein's) framework, but modern Turcology treats qaɣan as attested first in Turkic and Middle Mongol qaɣan as a re-borrowing, so the direction of the arrow is not settled.\",\n          \"derivation_fa\": \"ترکی باستان qaɣan «فرمانروای بزرگ» (سنگ‌نوشته‌های اورخون، سدهٔ هشتم میلادی) با افتادن ɣ میان دو واکه به qa'an و سپس qan بدل شد و در ترکی عثمانی و جغتایی «خان» نوشته می‌شود. وامبری همین دگرگونی آوایی را ثبت کرده است. پیکان «مغولی ← ترکی» در چارچوب کلاین پذیرفتنی است، اما در ترک‌شناسی امروزی نخستین گواهی‌ها ترکی‌اند و صورت مغولی میانه را وام‌گیری دوباره می‌دانند؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/khan\",\n            \"https://en.wiktionary.org/wiki/khagan\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:844\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.20647 (page marker 844 on l.20646): 'fr. Turki khan, contraction of khaqan, \\\"ruler, sovereign\\\", which is prob. of Mongolian origin' — exactly the Mongolian → Turkish arrow drawn here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"TTS\", \"where\": \"p. 65\", \"stance\": \"supports\", \"note\": \"'das mong.-türk. kaan = Fürst, Oberhaupt … Von kaan ist die neuere Form chan entstanden.'\"},\n            {\"src\": \"LKT\", \"where\": \"nr. 808\", \"stance\": \"supports\", \"note\": \"'Tk. hān: Aus hakān [das wohl selbst aus dem Mongolischen stammt] …' — Turkish hān from hakān, itself probably Mongolian.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"xân\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian خان xân is a straight loan from Turkic qan/hān, taken over with the Turkic dynasties of Central Asia — Wiktionary dates the earliest Persian-script attestation to Karakhanid coin legends of the 900s. In Persian it slid from 'sovereign of the Turks/Mongols' (so Borhān-e Qāṭeʿ p.707: 'خان … پادشاهان ختا و ترکستان را گویند … چنانکه پادشاهان روم را قیصر و چین را فغفور خوانند') to a mere postposed honorific after a personal name, and finally to 'Mr., sir'. The chart's parenthetic forms belong here: خانسامان xânsâmân 'butler', lit. 'lord of the stores' (خان 'lord' + سامان 'household stores'), and خانم xânom 'lady', from Turkish hanım, the feminine of han. Persian خان 'house, caravanserai' (< MP xān(ag)) is a homonym from a different source and is not part of this chain.\",\n          \"derivation_fa\": \"«خان» در فارسی نو وام‌واژه‌ای است از ترکی qan/hān که همراه با فرمانروایی سلسله‌های ترک در آسیای میانه وارد شد؛ کهن‌ترین گواهی آن سکه‌های قراخانی سدهٔ چهارم هجری است. برهان قاطع (ص ۷۰۷) می‌نویسد: «خان … پادشاهان ختا و ترکستان را گویند … چنانکه پادشاهان روم را قیصر و چین را فغفور خوانند». تحول معنایی از «پادشاه ترکان» به لقبی که پس از نام می‌آید و سرانجام «آقا» بوده است. «خانسامان» (خان + سامان) و «خانم» (از hanım ترکی، مؤنث han) نیز به همین ریشه بازمی‌گردند؛ اما «خانِ» به معنی خانه و کاروانسرا (از فارسی میانهٔ xān(ag)) هم‌آواست و از این ریشه نیست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%86\",\n            \"https://en.wiktionary.org/wiki/khan\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:707\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt \\\\f-leaf 165 = printed p.707 (offset printed = leaf + 542, checked against ختل/ختا on p.715): 'خان، بوزن کان. پادشاهان ختا و ترکستان را گویند هر که باشد چنانکه پادشاهان روم را قیصر و چین را فغفور خوانند - و بمعنی خانه و سرا هم هست - و کاروانسرا را نیز گویند'. The same page also carries خان‌خرگ, خانج, خانجه.\"},\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in (MON_part2.txt) has the khan-derived vocabulary; the volume/page is not given by Nourai so only the lemma could be checked. Mo'in's own entry الکل on MON_part1.txt l.16343 shows the same bracketed origin-tag system used for the Turkic loans.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"p. 103, nos. 465–466\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has only خان/خانه 'Haus' (no. 465: 'χān, χāne \\\"Haus\\\" … phlv. χānak … Von √khan- \\\"graben\\\"') and χānī 'Quelle'; the Turkic title خان is not in Horn, as expected for a book on native Persian etymology.\"},\n            {\"src\": \"BQT\", \"where\": \"p. 707\", \"stance\": \"supports\", \"note\": \"see ref_check — Borhān makes خان the title of the kings of Khitai and Turkestan.\"},\n            {\"src\": \"TAD\", \"where\": \"TAD_pages.txt l.936, s.v. خاقان\", \"stance\": \"supports\", \"note\": \"'خاقان: فارسي ترك وهو الامير والسيد ولقب سلاطين تركستان' — the fuller form khāqān is registered as a Turkic word in Arabic/Persian usage.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"xân\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic خان ḵān 'khan, ruler of the northern peoples' is real and is the same Turkic title, but the chart's arrow Persian → Arabic is only one of two possible routes. Klein (p.844) writes 'Pers. and Arab. khan, \\\"lord, prince\\\", fr. Turki khan' — i.e. he treats Persian and Arabic as parallel recipients of the Turkic word, not Arabic as a borrower from Persian; Wiktionary's Arabic entry (Etymology 3) likewise derives خان directly 'from Old Turkic qaɣan'. Given that Arabic met the title through the Saljuq/Ilkhanid administration, in which Persian was the chancery language, transmission through Persian is likely enough, but no source states it. Note that Arabic also has a homonymous خان 'caravanserai', which IS from Persian خانه (al-Unaysi and Wiktionary), and a root خ-و-ن 'to betray' — neither belongs here.\",\n          \"derivation_fa\": \"«خان» عربی به معنی فرمانروای اقوام شمالی واقعی است و همان لقب ترکی است، اما پیکانِ «فارسی ← عربی» تنها یکی از دو راه ممکن است. کلاین (ص ۸۴۴) فارسی و عربی را در کنار هم و هر دو را وام‌گرفته از ترکی می‌داند، و ویکی‌واژه نیز خانِ عربی را مستقیماً از ترکی باستان qaɣan می‌گیرد. چون عربی این لقب را از راه دیوان‌سالاری سلجوقی و ایلخانی که زبان دیوانش فارسی بود شناخت، میانجی‌گری فارسی محتمل است ولی در منابع تصریح نشده؛ پس با احتیاط پذیرفتنی است. «خان» به معنی کاروانسرا در عربی وام از «خانهٔ» فارسی است و ریشهٔ «خ‌ون» (خیانت) نیز جداست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%86\",\n            \"https://en.wiktionary.org/wiki/khan\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:844\", \"status\": \"partial\", \"note\": \"KLN_1966.txt l.20647 (p.844) says 'Pers. and Arab. khan … fr. Turki khan' — Klein puts Persian and Arabic side by side as joint borrowers from Turkic; he does not derive the Arabic word from the Persian one, as the arrow does.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"TAD\", \"where\": \"TAD_pages.txt ll.936–952\", \"stance\": \"partial\", \"note\": \"al-Unaysi lists خاقان as Turkic ('فارسي ترك … ولقب سلاطين تركستان') but treats the noun خان 'inn' under an Aramaic/Hebrew root and خانة as 'فارسي «خانة» معناه بيت' — i.e. he keeps the title and the caravanserai word apart, as modern lexicography does.\"},\n            {\"src\": \"LKT\", \"where\": \"nrs. 808 and 809\", \"stance\": \"partial\", \"note\": \"Lokotsch separates 808 'Tk. hān' (the title, out of hakān) from 809 'Pers. hān, auch hānä \\\"Haus\\\" … hieraus tk. han \\\"Herberge, Wirtshaus\\\"'; the Arabic title is not derived from Persian in either entry.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"khan\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"English khan 'title of respect' does not come from Arabic. It is first recorded c.1400 as can/chan, from Old French chan, from Medieval Latin chanis / Medieval Greek kanēs — the forms in which the title reached Europe with the reports of the Mongol empire (Plano Carpini, Rubruck, Marco Polo) in the 13th c. — ultimately from Turkic qan < qaɣan. Etymonline: 'The word has been known in the languages of Europe since 13c.; compare Medieval Latin chanis, Medieval Greek kanes, Old French chan, Russian khanu'; Wiktionary: 'Via late Middle English can, chan from Old French chan, from Medieval Latin chanis, from Turkic *qan'; Lokotsch nr.808 gives 'frz. kan, khan; dtsch. Chan' straight from Turkish. Nourai's own NOTE in the box already records that AHD routes the word 'from Turkish through Latin & French', and modern scholarship is unanimously on AHD's side. What Klein p.844 actually says is that Persian and Arabic khan come from Turki khan; the chart has turned Klein's list of Islamic-language forms into a transmission chain to English. (The separate English khan 'caravanserai' does come from Persian/Arabic خان, but that is the other word.)\",\n          \"derivation_fa\": \"«khan» انگلیسی به معنی لقب احترام از عربی نیامده است. نخستین کاربرد آن حدود ۱۴۰۰ میلادی به صورت can/chan است، از فرانسهٔ کهن chan، از لاتینِ میانه chanis و یونانی میانه kanēs — همان صورت‌هایی که لقب با سفرنامه‌های سدهٔ سیزدهم (پلانو کارپینی، روبروک، مارکوپولو) به اروپا رساند — و سرانجام از ترکی qan < qaɣan. لوکوچ نیز (شمارهٔ ۸۰۸) صورت‌های frz. kan, khan و dtsch. Chan را یکسره از ترکی می‌گیرد. خودِ نورایی در یادداشت جعبه آورده که فرهنگ American Heritage راه ترکی ← لاتین ← فرانسه را می‌دهد؛ پژوهش امروزی همین را می‌پذیرد و پیکانِ «عربی ← انگلیسی» را رد می‌کند. آنچه کلاین در ص ۸۴۴ گفته این است که خانِ فارسی و عربی از ترکی است، نه آنکه انگلیسی از عربی گرفته باشد.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/khan\",\n            \"https://en.wiktionary.org/wiki/khan\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:844\", \"status\": \"partial\", \"note\": \"KLN_1966.txt l.20647 (p.844) s.v. khan: Klein gives the English headword's source as 'Pers. and Arab. khan … fr. Turki khan', so he can be read as licensing an Arabic source; but he says nothing of a Persian → Arabic → English chain, and he omits the Old French/ML stage that all later dictionaries insist on.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"nr. 808\", \"stance\": \"contradicts\", \"note\": \"'hieraus rum. han …; frz. kan, khan; dtsch. Chan' — the western European forms are taken directly from Turkish, with no Arabic link.\"},\n            {\"src\": \"KLN\", \"where\": \"p.844, khansamah\", \"stance\": \"partial\", \"note\": \"'khansamah, n., a butler (India). — Hind. khansaman, fr. Pers. khansaman, lit. \\\"lord of stores\\\", fr. khan, \\\"lord\\\" (see khan, \\\"title of ruler\\\"), and saman, \\\"stores, household\\\"' — Klein's route for the khan-words that really did reach English through Persian is Persian → Hindustani → Anglo-Indian, not Persian → Arabic → English.\"},\n            {\"src\": \"HJB\", \"where\": \"searched HJB.txt for 'KHAN,' and 'CATHAY'\", \"stance\": \"silent\", \"note\": \"Hobson-Jobson's own headword could not be isolated in the OCR (the string 'Khan' occurs only inside quotations such as 'Kasim 'Ali Khan' and 'Mu'azzam Khan'); no Anglo-Indian evidence for an Arabic route was found.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Khitan\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Khitan (Chinese 契丹 Qìdān, Old Turkic Qïtań), a para-Mongolic people of southern Manchuria / eastern Inner Mongolia who ruled north China as the Liao dynasty 907–1125\",\n      \"note\": \"The people and the name are real and are the source of Cathay, so the root box is broadly right — but its gloss is wrong twice over. Khitan is the name of a people and dynasty, not of 'an area'; and the Khitan homeland was north-EAST China (Manchuria, the Liao river basin), not the north west. 'North west China' is where KHOTAN is, and that mislocation is the visible symptom of the conflation that runs through this whole entry: Nourai has merged Khitai/Khatā (Cathay, from the Khitans) with Khotan/Ḵotan (the Saka oasis city in the Tarim basin), which are two etymologically unrelated names. Mo'in's own footnote on Borhān p.715 — the page Nourai cites — states the Khitai side correctly and says nothing that would attach Khotan to it. Klein p.251 s.v. Cathay is likewise only about the Khitans.\",\n      \"note_fa\": \"قوم و نام «خِتَن/خطای» واقعی است و سرچشمهٔ Cathay هم هست، پس اصل جعبهٔ ریشه درست است؛ اما معنایی که برای آن نوشته شده دو خطا دارد: خِتان نام قوم و سلسله است نه نام یک ناحیه، و سرزمین آنان شمالِ شرقی چین (منچوری و حوضهٔ رود لیائو) بود نه شمال غربی. «شمال غربی چین» جای «خُتَن» است و همین جابه‌جایی نشانهٔ درهم‌آمیختگی سراسر این مدخل است: نورایی «ختا/خطا» (برگرفته از خِتان‌ها) را با «خُتَن» (شهر واحه‌نشین سکایی در حوضهٔ تاریم) یکی گرفته، حال آنکه این دو نام از نظر ریشه‌شناسی هیچ پیوندی ندارند. حاشیهٔ معین بر برهان قاطع ص ۷۱۵ — همان صفحه‌ای که نورایی ارجاع داده — تنها بخش «ختا» را درست شرح می‌دهد و چیزی دربارهٔ خُتَن ندارد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Cathay\",\n        \"https://www.etymonline.com/word/Cathay\",\n        \"https://en.wikipedia.org/wiki/Kingdom_of_Khotan\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:251\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.6804, immediately after the printed page marker '251' (l.6793): 'Cathay, n., poetic name of China. — ML. Cataya, fr. Khitai, the name of a Tatar kingdom (the kingdom of the Khitan Tatars). Cp. Khitan.' The page number is exact. Klein makes Khitai a kingdom of the Khitans; he does not call it 'an area in north west China' and never mentions Khotan.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BQT\", \"where\": \"p. 715, Mo'in's footnote 1 on ختا\", \"stance\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 173 = printed p.715: '۱ - ختا = خطا (خطای): … در هر حال بقسمت شمالی چین یعنی نواحی منچوری، مغولستان و ترکستان شرقی اطلاق میشده … «خطان» نام طایفه‌ای از طوایف مغول است و این طایفه در اوایل قرن چهارم هجری … تمام مغولستان و قسمتی از چین را تصرف کردند و همین اوقات نام خطا را بهمهٔ این ممالک … اطلاق کردند'. Mo'in puts the Khitans in Manchuria/Mongolia — the north east — and dates the extension of the name to the 10th c.\"},\n        {\"src\": \"KLN\", \"where\": \"p. 844/845 s.v. Khitan\", \"stance\": \"supports\", \"note\": \"'Khitan, adj. and n., Tatar. — Lit. \\\"of the kingdom of the Khitans\\\", fr. Khitai, name of a Tatar kingdom. See Cathay.' (KLN_1966.txt l.20651).\"},\n        {\"src\": \"SOD\", \"where\": \"entry 4368, printed p. ~173-174\", \"stance\": \"contradicts\", \"note\": \"Gharib glosses γwδnyk as 'xutanik, xuδanik — Khotanese', i.e. the adjective of KHOTAN, which is an Iranian (Saka) name and not the Khitan one; the very reference Nourai cites for this root belongs to the other word.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"xotan\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The node runs together two different Persian names. (a) ختا/خطا Ḵatā, Ḵatāy and the ethnonym خطان Ḵatān are genuinely from the Khitans: the Liao dynasty (907–1125) and then the Qara-Khitai of Central Asia made 'Khitai' the Muslim east's name for north China, and Mo'in's footnote on Borhān p.715 spells this out ('«خطان» نام طایفه‌ای از طوایف مغول است … همین اوقات نام خطا را بهمهٔ این ممالک اطلاق کردند'). This part is confirmed. (b) خُتَن Ḵotan is NOT from Khitan. It is the Tarim-basin oasis kingdom whose Khotanese-Saka inhabitants called it hvatana-/hvatäna- (Brahmi), Khotana (Kharoṣṭhī), later Hvamna, Hvam; Sanskritised as Gostana/Kustana, Chinese 于闐 Yutian; Emmerick connects the name with an Iranian adjective in -ana, plausibly with the ethnonym Saka. Persian خُتَن reached Persian poetry through the Silk Road as the source of musk-deer and beautiful faces, and the Hafez line the chart quotes — 'دو چشم شوخ تو بر هم زده ختا و ختن' — itself sets ختا beside ختن as two DIFFERENT places. So the Persian node's headword form ختن is put under the wrong root; only the bracketed variants ختا، خطا، خطان belong here. The gloss 'poetic name for China' fits ختا/خطا, not ختن, which is a city, never China.\",\n          \"derivation_fa\": \"این گره دو نام جداگانهٔ فارسی را یکی گرفته است. الف) «ختا/خطا» و قوم‌نام «خطان» به‌راستی از خِتان‌ها می‌آید: سلسلهٔ لیائو (۹۰۷–۱۱۲۵ م) و سپس قراختاییان آسیای میانه سبب شدند که «ختای» در جهان اسلام نام شمال چین شود؛ حاشیهٔ معین بر برهان ص ۷۱۵ همین را می‌گوید. این بخش تأیید می‌شود. ب) «خُتَن» از خِتان نیست. خُتَن شهر واحه‌ای در حوضهٔ تاریم است که مردم سکاییِ ختنی‌زبانش آن را hvatana-/hvatäna- (برهمی) و Khotana (خروشتی) و سپس Hvamna/Hvam می‌نامیدند؛ در سنسکریت Gostana/Kustana و در چینی 于闐 Yutian. امریک آن را واژه‌ای ایرانی با پسوند صفت‌ساز -ana و احتمالاً هم‌ریشه با «سکا» می‌داند. حتی بیت حافظ که خود نورایی آورده («دو چشم شوخ تو بر هم زده ختا و ختن») ختا و ختن را دو جای جدا می‌شمارد. پس پژوهش امروزی سرواژهٔ «ختن» را زیر این ریشه رد می‌کند و تنها «ختا، خطا، خطان» را می‌پذیرد؛ معنی «نام شاعرانهٔ چین» نیز از آنِ ختاست نه ختن.\",\n          \"sources\": [\n            \"https://en.wikipedia.org/wiki/Kingdom_of_Khotan\",\n            \"https://en.wiktionary.org/wiki/Cathay\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:715\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 173 = printed p.715. Mo'in's footnote on ختا reads '۱ - ختا = خطا (خطای) … بقسمت شمالی چین یعنی نواحی منچوری، مغولستان و ترکستان شرقی اطلاق میشده … «خطان» نام طایفه‌ای از طوایف مغول است' — it supports the ختا/خطا/خطان half of the node and says nothing about خُتَن, whose Borhān entry stands separately in the same alphabetical run (ختل، ختلان، ختلی، ختن، ختو on pp.715-716).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"pp. 715–716\", \"stance\": \"partial\", \"note\": \"Borhān's page 715 carries ختار، ختل، ختلان، ختلی and Mo'in's ختا footnote, page 716 ختو، ختوانه — the dictionary keeps ختا and ختن as separate headwords.\"},\n            {\"src\": \"SOD\", \"where\": \"entry 4368\", \"stance\": \"contradicts\", \"note\": \"'γwδnyk (S) xutanik, xuδanik — Khotanese' shows the Iranian name Khotan already in Sogdian, centuries before the Khitans existed; the two names cannot be the same word.\"},\n            {\"src\": \"MON\", \"where\": \"grep of MON_part1/part2 for ختن\", \"stance\": \"silent\", \"note\": \"the 2-vol Adena abridgement of Mo'in used here has no proper-name (aʿlām) volumes, so it carries no entry for Ḵotan/Ḵatā.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"ğwdnyk\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The form is correctly copied: Gharib nr. 4368 'γwδnyk (Sogdian script) = xutanik, xuδanik, \\\"Khotanese\\\"', printed at p.173/174 of the Sogdian dictionary — exactly Nourai's SOD:174, and the chart's ǧwdnyk is a faithful rendering of γwδnyk. But the word is the Sogdian adjective of KHOTAN, not of Khitan: γwδn/γwtn is the Sogdian name of the Saka oasis kingdom (Khotanese hvatana-), attested in the Ancient Letters and in Buddhist Sogdian long before the Khitans appear in history in the 4th–10th c. CE. Since the Khitans reached Central Asia only with the Liao (10th c.) and the Qara-Khitai (12th c.), a Sogdian word for 'Khotanese' cannot descend from them. The node belongs under Khotan, not under Khitan.\",\n          \"derivation_fa\": \"خودِ صورت درست نقل شده است: قریب (شمارهٔ ۴۳۶۸) γwδnyk را xutanik/xuδanik «ختنی» معنی کرده و آن در ص ۱۷۳–۱۷۴ فرهنگ سغدی است؛ یعنی همان ارجاع SOD:174 نورایی. اما این واژه صفتِ نسبی «خُتَن» است نه «خِتان»: γwδn/γwtn نام سغدیِ همان پادشاهی سکایی حوضهٔ تاریم است (ختنی hvatana-) و در «نامه‌های باستانی سغدی» و متون بودایی سغدی، سده‌ها پیش از پیدایش خِتان‌ها، گواهی شده است. چون خِتان‌ها تنها با لیائو (سدهٔ دهم) و قراختاییان (سدهٔ دوازدهم) به آسیای میانه رسیدند، واژه‌ای سغدی به معنی «ختنی» نمی‌تواند از آنان آمده باشد. این گره باید زیر ریشهٔ «خُتَن» بنشیند؛ ریشه‌شناسی نورایی رد می‌شود.\",\n          \"sources\": [\n            \"https://en.wikipedia.org/wiki/Kingdom_of_Khotan\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:174\", \"status\": \"partial\", \"note\": \"SOD_pages.txt l.16210, on the \\\\f-leaf that maps to printed p.173/174 (printed ≈ leaf − 66): '4368 γwδnyk S / xutanik, xuδanik / Khotanese / GMS 976; Sogdica, p.8-10.11c'. The page and the form check out exactly; but Gharib's gloss identifies it as the adjective of Khotan, which contradicts the root box it is drawn under.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"entry 4368 and the English index ('Khotanese 4368')\", \"stance\": \"contradicts\", \"note\": \"Gharib cites Henning, GMS 976 and Sogdica 8-10 for the word; there is no reference to the Khitans anywhere in the entry.\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, searched for hvatana/Khotan\", \"stance\": \"supports\", \"note\": \"Bailey's Khotanese material is built on the self-designation hvatana-/hvamna- 'Khotan(ese)', the Iranian etymon behind Sogdian γwδnyk — an Iranian word, not a Khitan one.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"cataya\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Medieval Latin Cataya/Cathaya is the form in which the name of north China reached Latin Europe in the 13th–14th c., through the Franciscan travellers and the Polos, who had it from Turkic and Persian Ḵitāy/Ḵatāy (Old Turkic Qïtań, Chinese 契丹 Qìdān). Klein p.251 says precisely this: 'ML. Cataya, fr. Khitai, the name of a Tatar kingdom (the kingdom of the Khitan Tatars)'. The Turkic final -ń was rendered -y in Persian and Turkic transmission (Qïtań > Ḵitāy), and Latin added the -a of a feminine place name.\",\n          \"derivation_fa\": \"لاتینِ میانه Cataya/Cathaya صورتی است که نام شمال چین در سده‌های سیزدهم و چهاردهم میلادی، از راه راهبان فرانسیسکن و خاندان پولو، به اروپای لاتین رساند؛ آنان آن را از ترکی و فارسی «ختای/خطای» گرفته بودند (ترکی باستان Qïtań، چینی 契丹 Qìdān). کلاین در ص ۲۵۱ همین را می‌گوید. ń پایانی ترکی در انتقال ترکی–فارسی به y بدل شد (Qïtań > Ḵitāy) و لاتین پایانهٔ -a نام‌های مؤنث جغرافیایی را افزود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Cathay\",\n            \"https://www.etymonline.com/word/Cathay\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:251\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.6804, just after the printed marker '251': 'Cathay, n., poetic name of China. — ML. Cataya, fr. Khitai, the name of a Tatar kingdom (the kingdom of the Khitan Tatars).'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 251 s.v. Cathay\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"SKT\", \"where\": \"searched SKT.txt for Cathay\", \"stance\": \"silent\", \"note\": \"Skeat's Concise has no entry for Cathay (it is a proper name).\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"Cathay, Khitan, Khotan\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the three words are right and the third is not. Cathay (1560s in English poetry) is from Medieval Latin Cataya/Cathaya < Turkic Qïtań/Ḵitāy < the Khitan ethnonym — Klein p.251 and Etymonline ('from Medieval Latin Cataya, from Turkish Khitai, from Uighur Khitai, name of a Tatar dynasty that ruled Beijing 936-1122') agree, as does Wiktionary ('from Latin Cathaya, variant of Cataya, from Old Turkic Qïtań … from Khitan'). English Khitan is simply the ethnonym itself, and Klein's own entry (p.844/845) says 'Khitan, adj. and n., Tatar. — Lit. \\\"of the kingdom of the Khitans\\\", fr. Khitai … See Cathay.' But Khotan is a different name altogether — the Tarim oasis kingdom, Khotanese-Saka hvatana-, Sanskrit Gostana/Kustana, Chinese Yutian — and it is not a name for China at all, poetic or otherwise. Its presence in this box, and 'north west China' in the root gloss, are the two places where the Khotan/Khitai conflation surfaces on the printed page. Klein, the reference cited, does not license it: his p.251 entry lists only Cathay and Khitan.\",\n          \"derivation_fa\": \"دو واژه از سه واژه درست است و سومی نه. Cathay (نخستین کاربرد انگلیسی در دههٔ ۱۵۶۰) از لاتینِ میانه Cataya/Cathaya و آن از ترکی Qïtań/Ḵitāy و سرانجام از قوم‌نام خِتان است؛ کلاین (ص ۲۵۱)، اتیمانلاین و ویکی‌واژه هم‌داستان‌اند. Khitan انگلیسی نیز خودِ همان قوم‌نام است و کلاین در ص ۸۴۴–۸۴۵ آن را «متعلق به پادشاهی خِتان‌ها» می‌داند. اما Khotan نامی یکسره جداست — پادشاهی واحه‌ای تاریم، به سکاییِ ختنی hvatana-، در سنسکریت Gostana/Kustana و در چینی Yutian — و هرگز نام چین، حتی شاعرانه، نبوده است. حضور آن در این جعبه و عبارت «شمال غربی چین» در جعبهٔ ریشه، دو جایی است که درهم‌آمیختگی خُتَن و ختای در صفحهٔ چاپی خود را نشان می‌دهد. مرجعی هم که نورایی آورده (کلاین ص ۲۵۱) تنها Cathay و Khitan را دارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Cathay\",\n            \"https://www.etymonline.com/word/Cathay\",\n            \"https://en.wikipedia.org/wiki/Kingdom_of_Khotan\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:251\", \"status\": \"partial\", \"note\": \"KLN_1966.txt l.6804 (p.251) covers Cathay and cross-refers to Khitan (l.20651, p.844/845: 'Khitan … Lit. \\\"of the kingdom of the Khitans\\\", fr. Khitai … See Cathay'); Klein has no entry making Khotan a name of China, so the third word in the box is unsupported by the citation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"pp. 251 and 844/845\", \"stance\": \"partial\", \"note\": \"supports Cathay and Khitan; silent on Khotan.\"},\n            {\"src\": \"HJB\", \"where\": \"HJB.txt, occurrences of 'Cathay'\", \"stance\": \"supports\", \"note\": \"Hobson-Jobson uses 'Cathay' throughout as the title of Yule's Cathay and the Way Thither, the standard collection of the medieval travellers (Odoric, Marignolli, Jordanus) through whom Cataya entered Latin; it never equates Cathay with Khotan.\"},\n            {\"src\": \"WEB\", \"where\": \"searched WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"the available Webster volume (A–) yields nothing usable for these proper names.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 4,\n      \"root\": \"K.h.l\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Semitic root k-ḥ-l 'to paint the eyelids with antimony'; Arabic كُحْل kuḥl 'antimony powder, kohl'\",\n      \"note\": \"The root, the language label and the gloss are all right as a description of Arabic كحل. What is only 'plausible' is the implicit claim that the word starts in Arabic. Klein p.46 already hedges: Arabic kuḥl is 'rel. to Heb. kāḥal (Ezek. 23.40) \\\"he painted the eyelids with antimony\\\", Aram.-Syr. kᵉḥal, Ethiop. kaḥala, Aram. kuḥlā, Ethiop. kuḥel \\\"antimony\\\"', and adds '(Akkad. guḫlu, \\\"antimony\\\", is prob. a WSem. loan word)'. Lokotsch nr.1227 and Wiktionary take the opposite view of that last point: 'Über aram. kuhlā vielleicht aus ass. guhlu' / Arabic كحل borrowed from Aramaic כוחלא, itself from Akkadian guḫlum. On the modern view the cosmetic and its name travelled Akkadian → Aramaic → Arabic, so Arabic is the transmitter to Europe rather than the origin. Everything downstream of Arabic in the chart is unaffected.\",\n      \"note_fa\": \"ریشه، برچسب زبان و معنی، همه به‌عنوان توصیف «کُحل» عربی درست‌اند. آنچه تنها «با احتیاط پذیرفتنی» است این ادعای ضمنی است که واژه از عربی آغاز شده باشد. کلاین در ص ۴۶ خود محتاط است و کُحل عربی را با عبری کَحَل (حزقیال ۲۳:۴۰)، آرامی–سریانی kᵉḥal و kuḥlā و حبشی kaḥala/kuḥel هم‌ریشه می‌داند و می‌افزاید که guḫlu اکدی «احتمالاً وام‌واژه‌ای سامی غربی است». لوکوچ (شمارهٔ ۱۲۲۷) و ویکی‌واژه درست وارونهٔ همین نکته را می‌گویند: کُحل عربی از آرامی כוחלא و آن از اکدی guḫlum گرفته شده. بنابر دیدگاه امروزی، سرمه و نام آن از اکدی به آرامی و از آنجا به عربی رفته و عربی تنها رساننده به اروپاست نه سرچشمه. باقی زنجیره پس از عربی از این نکته آسیبی نمی‌بیند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%83%D8%AD%D9%84\",\n        \"https://en.wiktionary.org/wiki/alcohol\",\n        \"https://www.ahdictionary.com/word/search.html?q=alcohol\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:46\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.2136, between the printed markers 45 and 46, s.v. alcohol: '… fr. Arab. al-kohl, vulgar pronunciation of al-kuhl, fr. al-, \\\"the\\\", and kohl, resp. kuhl, \\\"antimony (used for painting the eyelids)\\\", which is rel. to Heb. kahal (Ezek. 23.40) …'. Klein's page 46 is exact and states the root and its meaning as the box does.\"},\n        {\"ref\": \"FVA:348\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi, Farhang-e Vāžehā-ye ʿArabi dar Fārsi (1368/1989) — refs_online.json records that no digital copy exists on any permitted platform after a re-search in 2026-09; it could not be consulted.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"LKT\", \"where\": \"nr. 1227 (Ar. kuhl)\", \"stance\": \"partial\", \"note\": \"'[Über aram. kuhlä vielleicht aus ass. guhlu ZAkkFW 61] \\\"Spießglanzpulver (Schwefelblei) zum Färben der Augenbrauen, Wimpern und Lider\\\"' — Lokotsch routes the Arabic word through Aramaic from Assyrian/Akkadian, i.e. Arabic is not the origin.\"},\n        {\"src\": \"KLN\", \"where\": \"p. 46 s.v. alcohol\", \"stance\": \"supports\", \"note\": \"'(Akkad. guhlu, \\\"antimony\\\", is prob. a WSem. loan word.)' — Klein defends the West-Semitic (hence Arabic-compatible) priority that Nourai's root box assumes.\"},\n        {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. alcohol\", \"stance\": \"supports\", \"note\": \"'[Medieval Latin, fine metallic powder, especially of antimony, from Arabic al-kuḥl : al-, the + kuḥl, powder of antimony; see kḥl in the Appendix of Semitic roots.]' — AHD files the word under a Semitic root k-ḥ-l, exactly Nourai's root box.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"kohl; kahhâl; al-kahl, alkoŭl\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"كُحْل kuḥl (vulgar kuḥul/koḥl) 'finely ground stibnite used on the eyelids' is the ordinary noun of the root k-ḥ-l (verb كَحَلَ kaḥala 'to apply kohl'); كَحَّال kaḥḥāl is the regular faʿʿāl intensive/professional noun, 'kohl-applier', which in medieval Islamic medicine is the standard word for an oculist (the treatises of ʿAlī ibn ʿĪsā al-Kaḥḥāl of Baghdad, d. c.1010, are the classic example) — both are confirmed. The third item is only half right. The form is real: beside kuḥl, Andalusi Arabic had كُحُول kuḥūl, and the Latin alchemists took the phrase with the article as al-kohol; Klein p.46 records 'al-kohl, vulgar pronunciation of al-kuhl'. But the gloss 'highly purified spirits' is a European, not an Arabic, meaning: the word denoted a finely triturated powder, then any sublimate or essence, and only in 16th–18th c. European alchemy did 'alcohol of wine' come to mean spirit of wine. Pihan (Dict. étym. des mots… dérivés de l'arabe, p.20) says so flatly: 'le nom de cette dernière liqueur n'a pour équivalent en arabe que rūḥ al-ʿaraqī, traduction littérale du français'. So the chart antedates a European sense into Arabic.\",\n          \"derivation_fa\": \"«کُحْل» (در تلفظ عامیانه کُحُل/کُحل) یعنی سنگ سرمهٔ نرم‌سوده که به پلک می‌کشند، اسمِ عادیِ ریشهٔ ک‌ح‌ل است (فعل کَحَلَ)؛ و «کَحّال» صیغهٔ فَعّال پیشه‌ساز است، «سرمه‌کش»، که در پزشکی دورهٔ اسلامی واژهٔ رایج برای چشم‌پزشک بود (نمونهٔ کلاسیک: علی بن عیسی الکحّال بغدادی، درگذشتهٔ حدود ۴۰۰ ق). این دو تأیید می‌شوند. سومی نیمه‌درست است: صورتِ آن واقعی است — در عربی اندلسی «کُحول» هم بوده و کیمیاگران لاتین همان را با حرف تعریف al-kohol گرفتند، و کلاین (ص ۴۶) «al-kohl، تلفظ عامیانهٔ al-kuhl» را ثبت کرده است — اما معنی «الکل خالص» معنایی اروپایی است نه عربی: واژه نخست «گَردِ بسیار نرم»، سپس «هر تصعیدشده و عصاره» بود و تنها در کیمیای اروپایی سده‌های شانزدهم تا هجدهم «الکلِ شراب» معنی روحِ شراب یافت. پیهان (ص ۲۰) صریح می‌گوید که عربی برای «عرق» جز «روح العَرَقی»، که ترجمهٔ لفظی از فرانسه است، معادلی ندارد. پس نورایی معنایی اروپایی را به عربی پس‌فرستاده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%83%D8%AD%D9%84\",\n            \"https://en.wiktionary.org/wiki/alcohol\",\n            \"https://www.etymonline.com/word/alcohol\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:348\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vāžehā-ye ʿArabi dar Fārsi has no digital copy (refs_online.json, re-searched 2026-09); the page could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 46 s.v. alcohol; p. 851/852 s.v. kohl\", \"stance\": \"partial\", \"note\": \"'kohl, n., powder (esp. of antimony), used by Eastern women to darken the eyelids. — Arab. kuhl. See alcohol' (KLN_1966.txt l.20824); and at p.46 'Its modern sense (\\\"highly rectified spirits\\\") is due to the analogy of the fineness of this powder' — Klein makes the 'spirits' sense a later development, not an Arabic one.\"},\n            {\"src\": \"PHN\", \"where\": \"p. 20-21 s.v. ALCOOL\", \"stance\": \"contradicts\", \"note\": \"Pihan: '… désignait communément certains corps réduits en poudre très fine; et c'est seulement par allusion à la subtilité de cette poudre que les chimistes européens ont nommé alcohol l'esprit-de-vin, car le nom de cette dernière liqueur n'a pour équivalent en arabe que rūḥ al-ʿaraqī, traduction littérale du français.'\"},\n            {\"src\": \"LKT\", \"where\": \"nr. 1227\", \"stance\": \"contradicts\", \"note\": \"'noch im 16. Jahrhundert ist das hieraus entstandene Wort Alcohol in der Alchemie der geläufige Ausdruck für \\\"trockenes, feines Pulver\\\", erst später wurde es zur Bezeichnung des Weingeistes benutzt' — the 'spirits' sense is dated to post-16th-c. Europe.\"},\n            {\"src\": \"DEV\", \"where\": \"p. 13 s.v. Alcool\", \"stance\": \"supports\", \"note\": \"'Il est bien démontré que l'étymologie de ce mot est l'arabe al-kohl, le cohel ou poudre d'antimoine, dont les femmes, en Orient, se teignent les paupières.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"kohl; kahhâl; kohŭl\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"کُحل and کَحّال are straightforward Arabic loans in Persian, taken over with the Greco-Arabic medical tradition; Mo'in tags both [ع.] (= Arabic): 'کحال [ع.] (ص. اِ.) کسی که کحل (سرمه) به چشم اشخاص می‌کشد؛ سرمه‌کش … در قدیم کحال به کسی گفته می‌شد که هم سرمه به چشم کسان می‌کشید و هم جراحات و امراض چشم را علاج می‌کرد … طبیبی که دردهای چشم را درمان کند؛ چشم‌پزشک' and 'کحل [ع.] (اِ.) سنگ سرمه. سرمه. هر چه در چشم کشند برای شفای چشم'; the Vahshi couplet quoted in the box uses کحل in exactly that sense. These two are confirmed. کُحول 'alcohol' is different in kind: it is not an old Arabic loan into Persian but a modern scientific term — Arabic كُحول kuḥūl was pressed into service in the 19th–20th c. as the chemical name for alcohol, on the model of the European word that had itself come from al-kuḥl, and Persian took it in that technical register (the everyday Persian word remains الکل, node #5). Mo'in's two-volume abridgement has مکحول but no headword کحول, so the term could not be confirmed lexicographically in Persian; hence 'plausible' rather than 'confirmed'.\",\n          \"derivation_fa\": \"«کُحل» و «کَحّال» وام‌واژه‌های آشکار عربی در فارسی‌اند که همراه با سنّت پزشکی یونانی–اسلامی وارد شدند؛ معین هر دو را با نشانهٔ [ع.] آورده است: «کحّال [ع.] کسی که کحل (سرمه) به چشم اشخاص می‌کشد؛ سرمه‌کش … در قدیم کحال به کسی گفته می‌شد که هم سرمه به چشم کسان می‌کشید و هم … امراض چشم را علاج می‌کرد؛ چشم‌پزشک» و «کحل [ع.] سنگ سرمه. سرمه». بیت وحشی که در جعبه آمده نیز «کحل» را در همین معنی به کار برده است. این دو تأیید می‌شوند. اما «کُحول» به معنی الکل از گونهٔ دیگری است: وام کهن نیست بلکه اصطلاحی نو است؛ عربی در سدهٔ نوزدهم و بیستم «کُحول» را به قیاسِ واژهٔ اروپایی — که خود از الکحل آمده بود — نام شیمیایی الکل کرد و فارسی آن را در همین سطح فنی گرفت (واژهٔ روزمرهٔ فارسی همچنان «الکل» است، گرهٔ ۵). در فرهنگ دوجلدی معین سرواژهٔ «کحول» نیست، از این رو «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%83%D8%AD%D9%84\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%84%DA%A9%D9%84\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:2919\", \"status\": \"partial\", \"note\": \"The 6-volume Amir Kabir Mo'in with continuous pagination is not online, so p.2919 itself could not be opened; the corresponding entries were read in the 2-vol Adena abridgement (MON_part2.txt ll.21232-21262): 'کحال: [ع.] (ص. اِ.) کسی که کحل (سرمه) به چشم اشخاص می‌کشد؛ سرمه‌کش' and 'کحل: [ع.] (اِ.) سنگ سرمه. سرمه. هر چه در چشم کشند برای شفای چشم. کحل اصبهانی (اصفهانی): (پز.) سولفور انتیمون را گویند که به عنوان سرمه بکار می‌رفته'. Mo'in confirms the two words and their Arabic origin; کحول is not a headword there.\"},\n            {\"ref\": \"FVA:348\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi's dictionary exists (refs_online.json).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt ll.21232-21262 (کحال، کحالی، کحل، کحلی)\", \"stance\": \"supports\", \"note\": \"all tagged [ع.]; 'کحالی: [ع. ف.] (حامص.) شغل و عمل کحال. علم به امراض چشم؛ چشم‌پزشکی' — the hybrid Arabic+Persian formation shows how naturalised the loan is.\"},\n            {\"src\": \"ARY\", \"where\": \"grep of ARY_pages.txt for کحل\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary covers Indo-European roots of Persian words and has nothing on an Arabic loan.\"},\n            {\"src\": \"LKT\", \"where\": \"nr. 1227\", \"stance\": \"partial\", \"note\": \"Lokotsch notes in passing that the eye cosmetic itself is called سرمه sürme in Persian and Turkish, not kuḥl — the Arabic word is the learned/medical register in Persian, which is how Mo'in presents it too.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"alcohol\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Medieval Latin alcohol 'powdered ore of antimony, any impalpable powder' is a borrowing of the Arabic phrase al-kuḥl (article + noun) taken over as a single word, through the Latin translations of Arabic alchemical and medical works made in Spain from the 12th c. onward; a 14th-c. Paris manuscript quoted by Devic already glosses 'Alcofol, id est Anthimonium'. The Iberian forms alcofol/alquifol/alcofoll show the intermediate stage. Klein p.46 gives 'ML., fr. Arab. al-kohl', AHD 'Medieval Latin, fine metallic powder, especially of antimony, from Arabic al-kuḥl'. The chart's gloss 'spirit of wine' belongs to the later, 16th–18th c. phase of the Latin/European word (Paracelsus onwards, then alcohol vini), not to its first Latin sense.\",\n          \"derivation_fa\": \"لاتینِ میانه alcohol به معنی «گَردِ سنگ سرمه، هر پودر بسیار نرم» وام‌گیری عبارت عربی «الکحل» (حرف تعریف + اسم) است که یکجا و همچون یک واژه گرفته شد؛ راهِ آن ترجمه‌های لاتینِ آثار کیمیایی و پزشکی عربی در اسپانیا از سدهٔ دوازدهم میلادی بود. دویک از دست‌نویسی پاریسی از سدهٔ چهاردهم نقل می‌کند: «Alcofol, id est Anthimonium». صورت‌های ایبریایی alcofol/alquifol/alcofoll مرحلهٔ میانی را نشان می‌دهند. کلاین (ص ۴۶) و فرهنگ American Heritage هر دو همین را می‌گویند. اما معنی «روحِ شراب» که در جعبه آمده به مرحلهٔ متأخرترِ سده‌های شانزدهم تا هجدهم (از پاراسلسوس به بعد) مربوط است نه به نخستین معنی لاتین.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alcohol\",\n            \"https://www.ahdictionary.com/word/search.html?q=alcohol\",\n            \"https://en.wiktionary.org/wiki/alcohol\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:46\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.2136 (printed p.46): 'alcohol, n. — ML., fr. Arab. al-kohl, vulgar pronunciation of al-kuhl, fr. al-, \\\"the\\\", and kohl, resp. kuhl, \\\"antimony (used for painting the eyelids)\\\" … Its modern sense (\\\"highly rectified spirits\\\") is due to the analogy of the fineness of this powder.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"p. 13 s.v. Alcool (DEV.txt ll.356-365)\", \"stance\": \"supports\", \"note\": \"'Alcohol, dans l'ancienne pharmacie, se disait de toute substance porphyrisée' and the footnote 'Alcofol, id est Anthimonium. (Man. lat. du XIVe siècle, n° 7156 de la Bibl. nat.)'.\"},\n            {\"src\": \"LKT\", \"where\": \"nr. 1227\", \"stance\": \"supports\", \"note\": \"'noch im 16. Jahrhundert ist das hieraus entstandene Wort Alcohol in der Alchemie der geläufige Ausdruck für \\\"trockenes, feines Pulver\\\"'; the Romance forms listed are 'sp. pg. alquifol, alcofol, alcofor, alcohol, kat. alcofoll'.\"},\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. alcohol\", \"stance\": \"supports\", \"note\": \"'The Arabic phrase al-kuḥl, \\\"the kohl,\\\" was borrowed into Medieval Latin as one word, alcohol, \\\"kohl.\\\"'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"alcool\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French took the alchemists' Latin word over as alcohol (16th c.), still meaning a very fine powder, and by the classical period had reduced the spelling to alcool; Pihan protests at exactly this ('Depuis fort longtemps, on écrit alcool sans h; mais c'est à tort: le second o est simplement euphonique, et la lettre ḥ, qui est radicale, ne peut être supprimée sans défigurer le mot arabe'). Alongside it French kept the doublets alquifoux and coheul taken from Spanish/Arabic in the ore sense. The modern sense 'esprit-de-vin' spread from the alchemical phrase alcohol vini. The node carries no reference in the book, but the Latin → French step is uncontroversial and is given by Lokotsch, Devic and Pihan alike.\",\n          \"derivation_fa\": \"فرانسه واژهٔ لاتینِ کیمیاگران را در سدهٔ شانزدهم به صورت alcohol گرفت که هنوز «پودر بسیار نرم» معنی می‌داد، و در دورهٔ کلاسیک املای آن به alcool ساده شد؛ پیهان دقیقاً به همین اعتراض دارد: «مدت‌هاست alcool را بی h می‌نویسند، و این خطاست؛ o دوم تنها خوش‌آهنگ‌ساز است و حرف ح که اصلی است بی‌آنکه واژهٔ عربی را از ریخت بیندازد حذف‌شدنی نیست». در کنار آن، فرانسه دوگانه‌های alquifoux و coheul را نیز در معنی سنگ معدن از اسپانیایی و عربی نگاه داشت. معنی امروزی «عرق، روح شراب» از ترکیب کیمیایی alcohol vini گسترش یافت. این گره در کتاب ارجاعی ندارد، اما گام لاتین ← فرانسه بی‌مناقشه است و لوکوچ، دویک و پیهان هر سه آن را می‌آورند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alcohol\",\n            \"https://en.wiktionary.org/wiki/alcohol\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node; the step was checked against Pihan, Devic and Lokotsch instead (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHN\", \"where\": \"p. 20-21 s.v. ALCOOL (PHN.txt ll.1195-1210)\", \"stance\": \"supports\", \"note\": \"'Depuis fort longtemps, on écrit alcool sans h; mais c'est à tort: le second o est simplement euphonique, et la lettre ḥ, qui est radicale, ne peut être supprimée sans défigurer le mot arabe, qui se trouve alors réduit aux seules lettres alcol et n'offre plus de sens.'\"},\n            {\"src\": \"DEV\", \"where\": \"pp. 13-14 and 'Alquifoux' (DEV.txt ll.356, 481)\", \"stance\": \"supports\", \"note\": \"'Alquifoux est donc une corruption de l'arabe al-cohl, altération qui paraîtrait peut-être difficile à admettre si l'on n'avait les intermédiaires alcohol, alcofol, alquifol. (Voy. Alcool.)'\"},\n            {\"src\": \"LKT\", \"where\": \"nr. 1227\", \"stance\": \"supports\", \"note\": \"lists 'frz. alquifoux, coheul, alcohol, it. alcool, rum. alcool; ndl. alkohol, engl. alcohol, dtsch. Alkohol'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"alkol\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian الکل alkol 'alcohol' is a 19th/20th-c. loan from French alcool, taken in with European chemistry and medicine (the Dār al-Fonūn curriculum and the French-based scientific vocabulary of Qajar Iran); the pronunciation alkol with final -ol, not -ūl, betrays the French source. Wiktionary makes the point that decides the direction: 'a direct borrowing from Arabic would drop the definite article ال (al-)' — a genuine Arabic loan would have entered as کحل, so the retained ال proves the word came back through Europe. This is therefore a round trip: Arabic al-kuḥl → Medieval Latin alcohol → French alcool → Persian الکل. Mo'in tags the headword differently — 'الکل [ع. الکحل] (اِ.) (شیم.) جسمی آلی، مرکب از هیدروژن، اکسیژن و کربن …' — pointing at the ultimate Arabic etymon rather than the immediate French donor, but he tags the derivative الکلی as [فر. ف.] 'French + Persian', which shows the French route was clear to him.\",\n          \"derivation_fa\": \"«الکل» فارسی وام‌واژه‌ای است از فرانسهٔ alcool که در سدهٔ سیزدهم و چهاردهم خورشیدی همراه با شیمی و پزشکی اروپایی (برنامهٔ دارالفنون و واژگان علمی فرانسه‌بنیاد دورهٔ قاجار) وارد شد؛ تلفظ alkol با -ol پایانی، نه -ūl، خودْ گواه سرچشمهٔ فرانسوی است. ویکی‌واژه نکتهٔ تعیین‌کننده را می‌گوید: وام‌گیری مستقیم از عربی حرف تعریف «ال» را می‌انداخت و واژه به صورت «کحل» درمی‌آمد؛ ماندنِ «ال» ثابت می‌کند که واژه از راه اروپا بازگشته است. پس این یک وام‌گیری رفت‌وبرگشتی است: الکحل عربی ← alcohol لاتینِ میانه ← alcool فرانسه ← «الکل» فارسی. معین سرواژه را «الکل [ع. الکحل]» نشانه‌گذاری کرده، یعنی به خاستگاه نهایی عربی اشاره دارد نه به وام‌دهندهٔ بی‌واسطهٔ فرانسوی، ولی مشتق «الکلی» را [فر. ف.] می‌داند و همین نشان می‌دهد راه فرانسوی برای او روشن بوده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%84%DA%A9%D9%84\",\n            \"https://en.wiktionary.org/wiki/alcohol\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:342\", \"status\": \"partial\", \"note\": \"The paginated 6-vol Mo'in is not online; the entry was read in the Adena abridgement, MON_part1.txt l.16343: 'الکل: [ع. الکحل] (اِ.) (شیم.) جسمی آلی، مرکب از هیدروژن، اکسیژن و کربن و آن فرار، دارای طعم تند و سوزان است … مهمترین آن الکل اتیلیک (الکل معمولی) است'. Mo'in confirms the word and its chemical sense but tags the origin as Arabic الکحل, not French — 'partial' for that reason; his next headword 'الکلی: [فر. ف.]' does mark the French layer.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt ll.16343-16357\", \"stance\": \"partial\", \"note\": \"see ref_check: [ع. الکحل] for الکل but [فر. ف.] for الکلی.\"},\n            {\"src\": \"ARY\", \"where\": \"grep of ARY_pages.txt for الکل\", \"stance\": \"silent\", \"note\": \"Aryanpur treats only Indo-European roots of Persian words; a European chemical loan is out of scope.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"alcohol\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English alcohol is attested from the 1540s (and as alcofol already in the early 15th c.) meaning 'fine powder produced by sublimation', straight from Medieval Latin alcohol as used in alchemical writing — Bartholomew Traheron's 1543 translation glosses 'alcohol, or (as I fynde it sometymes wryten) alcofoll, for moost fine poudre'. Paracelsus extended it to volatile liquids; by the 1670s it meant 'the pure spirit of anything', and 'intoxicating ingredient of strong liquor' is attested by 1753, shortened from alcohol of wine; the chemical class sense follows in 1808. The chart draws English from Latin, which is what Klein p.46 and AHD p.30 both say; Wiktionary adds a Middle French stage for the Middle English form alcofol, which is a refinement rather than a contradiction.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی alcohol از دههٔ ۱۵۴۰ گواهی شده (و در صورت alcofol از اوایل سدهٔ پانزدهم) به معنی «پودر بسیار نرمِ حاصل از تصعید»، مستقیماً از لاتینِ میانهٔ alcohol در نوشته‌های کیمیایی؛ ترجمهٔ بارتولومیو تراهرن (۱۵۴۳) آن را چنین معنی می‌کند: «alcohol یا آن‌گونه که گاه نوشته می‌بینم alcofoll، برای نرم‌ترین پودر». پاراسلسوس آن را به مایعات فرّار گسترش داد؛ تا دههٔ ۱۶۷۰ معنی «جوهر خالص هر چیز» یافت و معنی «مادهٔ مستی‌آور مشروب» از ۱۷۵۳ گواهی شده که کوتاه‌شدهٔ alcohol of wine است؛ معنی شیمیایی امروزی از ۱۸۰۸. نمودار انگلیسی را از لاتین می‌گیرد، همان‌گونه که کلاین (ص ۴۶) و American Heritage (ص ۳۰) می‌گویند؛ ویکی‌واژه مرحلهٔ فرانسهٔ میانه را برای صورت انگلیسی میانهٔ alcofol می‌افزاید که تکمله است نه تناقض. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alcohol\",\n            \"https://en.wiktionary.org/wiki/alcohol\",\n            \"https://www.ahdictionary.com/word/search.html?q=alcohol\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:46\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.2136 (p.46): 'alcohol, n. — ML., fr. Arab. al-kohl …' — English from Medieval Latin, exactly the arrow drawn.\"},\n            {\"ref\": \"AHD:30\", \"status\": \"supports\", \"note\": \"American Heritage s.v. alcohol (archived from ahdictionary.com): '[Medieval Latin, fine metallic powder, especially of antimony, from Arabic al-kuḥl: al-, the + kuḥl, powder of antimony; see kḥl in the Appendix of Semitic roots.]' — the 1975 New College edition has the same etymology at p.30, the page Nourai cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l.23702 (list of French-mediated Arabic words)\", \"stance\": \"partial\", \"note\": \"Skeat's Concise lists alcohol among words that came into English 'French from Arabic', i.e. he inserts a French stage where Klein and AHD have Medieval Latin directly.\"},\n            {\"src\": \"LKT\", \"where\": \"nr. 1227\", \"stance\": \"supports\", \"note\": \"'ndl. alkohol, engl. alcohol, dtsch. Alkohol' derived from the same alchemical Latin word.\"},\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com, Word History s.v. alcohol\", \"stance\": \"supports\", \"note\": \"'From Medieval Latin it was borrowed into English in the 16th century.'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T20:50:17.197Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-266.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T20:50:20.900Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-266.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 266"
}
```


### [2026-09-06T20:50:24.684Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'plausible': 4, 'confirmed': 6, 'disputed': 4}
root verdicts: {'plausible': 3}
ref checks: {'supports': 7, 'partial': 7, 'not_checked': 3}
books consulted: {'supports': 17, 'silent': 7, 'partial': 9, 'contradicts': 5} | by book: {'LKT': 8, 'KLN': 4, 'MON': 3, 'DEV': 3, 'BQT': 2, 'TAD': 2, 'HJB': 2, 'SOD': 2, 'SKT': 2, 'PHN': 2, 'ARY': 2, 'AHD': 2, 'TTS': 1, 'HRN': 1, 'ISS_alt_DKS': 1, 'WEB': 1}
```


## [2026-09-06T20:50:31.496Z] TOOL CALL #72: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null | head"
}
```


### [2026-09-06T20:50:31.540Z] TOOL RESULT

```
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


## [2026-09-06T20:50:35.369Z] TOOL CALL #73: Bash

```json
{
 "command": "cp \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg266.png\" /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/266.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-06T20:50:35.437Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T20:50:53.858Z] AGENT

Page 266 (book p. 236) verified. `verify_check.py 266`: 14/14 nodes, **0 PROBLEM lines**.

**Counts** — nodes: 6 confirmed, 4 plausible, 4 disputed. Roots: 3 plausible (Khan, Khitan, K.h.l). Ref checks: 7 supports, 7 partial, 3 not_checked (FVA has no digital copy anywhere; the French `alcool` node carries no ref in the book).

**Disputed items**
- **Khitan #1** `xotan` «خُتَن (خَتا، خطا، خطان)» — Nourai merges two unrelated names. ختا/خطا/خطان really is from the Khitans (Mo'in's footnote on Borhān p.715 confirms it), but خُتَن is the Tarim oasis, Khotanese-Saka *hvatana-*, Skt. Gostana, Chin. 于闐 — and the Hafez line he quotes ("ختا و ختن") itself treats them as two places.
- **Khitan #2** Sogdian `ğwdnyk` — Gharib nr. 4368 (p.173/174, matching SOD:174) glosses it "xutanik, xuδanik, Khotanese", i.e. the adjective of Khotan, attested centuries before the Khitans reached Central Asia. Nourai's own citation contradicts his arrow.
- **Khitan #4** English `Cathay, Khitan, Khotan` — Cathay and Khitan confirmed (Klein p.251 verified verbatim); Khotan does not belong and is never a name for China.
- **Khan #4** English `khan` — not from Arabic: ME *can/chan* < OF *chan* < ML *chanis*/MGk *kanēs* < Turkic. Lokotsch nr. 808 routes the European forms straight from Turkish. The chart's own NOTE already flags AHD's route, and modern scholarship sides with AHD.

**Other notes**
- Root gloss "Khitan: an area in north west China" is wrong twice: it is a people/dynasty, and their homeland was north**east** China — the mislocation is the visible symptom of the Khotan conflation.
- Arabic node #1's third gloss, `al-kahl, alkoŭl : highly purified spirits`, antedates a European sense into Arabic (Pihan p.20 is explicit; Lokotsch dates it post-16th c. Europe).
- Klein page numbers all check out exactly (KLN:46, :251, :844) via the printed page markers in KLN_1966.txt; BQT:707 and BQT:715 verified (BQT_v2_pages.txt, printed = leaf + 542).

**Extraction errors for the owner:** none substantive. One cosmetic point — the printed page shows «کُحول» with a damma in the Persian K.h.l box; `data/extracted/batch/page-266.json` has "کحول" undiacriticised (its neighbours کُحل/کَحّال kept theirs). Page PNG archived at `/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/266.png`; 12 web sources archived via `fetch_source.py`.
