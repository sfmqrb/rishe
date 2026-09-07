# Verification process log — verify-page-323


## [2026-09-07T15:49:17.313Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 323 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-323.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-323.json. Write /home/sfmqrb/git/rishe/data/verification/page-323.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 323` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:19.364Z] AGENT

I'll start by reading the instructions and the input files.


## [2026-09-07T15:49:20.075Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:20.088Z] TOOL RESULT

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


## [2026-09-07T15:49:20.780Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-323.txt"
}
```


### [2026-09-07T15:49:20.794Z] TOOL RESULT

```
1	=== PDF page 323 (book page 293) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Me 2 : to measure; Měnôt: moon used to measure time  (refs POK:703, 731)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:703,731; SYN:54,877,1010 | mâ 1 : to measure ; mâh, mâhya : moon, also month ; mâh-tab : moonshine ☞Tep
5	  #2 (parent #1) [Persian] refs=POK:731; BQT:1956,1958; SNS:37,113 | mâh «ماه» : moon, also month ; mahtâb «مهتاب» : moonshine
6	  #3 (parent #1) [Old Persian] refs=KNT:201 | fra-ma-na : to measure beforehand, decide, order ☞Per 1 ; â-mâ : extend
7	    #4 (parent #3) [Persian] refs=BQT:1470; FFD:66 | farmân «فرمان» : order | extra: فرمودن ، فرمایش ، فرمانده
8	  #5 (parent #1) [Avestan] refs=HRN:80,233; BQT:37; FFD:25 | paiti-mâ : measure ☞Per 3 ; âiz-mâ, uz-mâ-ta : measure, test ; ni-mâ : measure down, display ☞Nî 1
9	    #6 (parent #5) [Persian] refs=BQT:37,448,2171 | paymŭdan «پیمودن» : to measure, walk ; âzmŭdan «آزمودن ( آزمایش ، آزمون )» : to test ; nomŭdan «نمودن» : to show | extra: پیمان ، پیمانه ، هواپیما ؛ نما ، نمایش ، نمودار ، نماینده
10	#7 (parent #0) [Greek] refs=AHD | metron : measure ; dia-metros : (line) that measures across, diameter ☞Dwo
11	  #8 (parent #7) [French] refs=AHD:865 | metre
12	    #9 (parent #8) [Persian] refs=MON:3800 | metr «متر»
13	    #10 (parent #8) [English] refs=AHD | meter, diameter, geometry
14	#11 (parent #0) [Latin] refs=None | 
15	  #12 (parent #11) [English] refs=None | measure, dimension, semester
16	#13 (parent #0) [Germanic] refs=AHD | 
17	  #14 (parent #13) [English] refs=None | meal, moon, month, Monday
18	
```


## [2026-09-07T15:49:21.097Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-323.json"
}
```


### [2026-09-07T15:49:21.121Z] TOOL RESULT

```
1	{
2	  "pdf_page": 323,
3	  "book_page": 293,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Me 2",
8	        "lang": "Indo-European",
9	        "refs": "POK:703, 731",
10	        "gloss": "to measure; Měnôt: moon used to measure time"
11	      },
12	      "part": 1,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Avestan / Old Persian",
18	          "refs": "POK:703,731; SYN:54,877,1010",
19	          "words": [
20	            {"translit": "mâ 1", "gloss": "to measure", "script": null},
21	            {"translit": "mâh, mâhya", "gloss": "moon, also month", "script": null},
22	            {"translit": "mâh-tab", "gloss": "moonshine", "script": null, "see": ["Tep"]}
23	          ],
24	          "note": null,
25	          "quote": null
26	        },
27	        {
28	          "id": 2,
29	          "parent": 1,
30	          "lang": "Persian",
31	          "refs": "POK:731; BQT:1956,1958; SNS:37,113",
32	          "words": [
33	            {"translit": "mâh", "gloss": "moon, also month", "script": "ماه"},
34	            {"translit": "mahtâb", "gloss": "moonshine", "script": "مهتاب"}
35	          ],
36	          "note": null,
37	          "quote": null
38	        },
39	        {
40	          "id": 3,
41	          "parent": 1,
42	          "lang": "Old Persian",
43	          "refs": "KNT:201",
44	          "words": [
45	            {"translit": "fra-ma-na", "gloss": "to measure beforehand, decide, order", "script": null, "see": ["Per 1"]},
46	            {"translit": "â-mâ", "gloss": "extend", "script": null}
47	          ],
48	          "note": null,
49	          "quote": null
50	        },
51	        {
52	          "id": 4,
53	          "parent": 3,
54	          "lang": "Persian",
55	          "refs": "BQT:1470; FFD:66",
56	          "words": [
57	            {"translit": "farmân", "gloss": "order", "script": "فرمان"}
58	          ],
59	          "script_extra": "فرمودن ، فرمایش ، فرمانده",
60	          "note": null,
61	          "quote": null
62	        },
63	        {
64	          "id": 5,
65	          "parent": 1,
66	          "lang": "Avestan",
67	          "refs": "HRN:80,233; BQT:37; FFD:25",
68	          "words": [
69	            {"translit": "paiti-mâ", "gloss": "measure", "script": null, "see": ["Per 3"]},
70	            {"translit": "âiz-mâ, uz-mâ-ta", "gloss": "measure, test", "script": null},
71	            {"translit": "ni-mâ", "gloss": "measure down, display", "script": null, "see": ["Nî 1"]}
72	          ],
73	          "note": null,
74	          "quote": null
75	        },
76	        {
77	          "id": 6,
78	          "parent": 5,
79	          "lang": "Persian",
80	          "refs": "BQT:37,448,2171",
81	          "words": [
82	            {"translit": "paymŭdan", "gloss": "to measure, walk", "script": "پیمودن"},
83	            {"translit": "âzmŭdan", "gloss": "to test", "script": "آزمودن ( آزمایش ، آزمون )"},
84	            {"translit": "nomŭdan", "gloss": "to show", "script": "نمودن"}
85	          ],
86	          "script_extra": "پیمان ، پیمانه ، هواپیما ؛ نما ، نمایش ، نمودار ، نماینده",
87	          "note": null,
88	          "quote": null
89	        },
90	        {
91	          "id": 7,
92	          "parent": 0,
93	          "lang": "Greek",
94	          "refs": "AHD",
95	          "words": [
96	            {"translit": "metron", "gloss": "measure", "script": null},
97	            {"translit": "dia-metros", "gloss": "(line) that measures across, diameter", "script": null, "see": ["Dwo"]}
98	          ],
99	          "note": null,
100	          "quote": null
101	        },
102	        {
103	          "id": 8,
104	          "parent": 7,
105	          "lang": "French",
106	          "refs": "AHD:865",
107	          "words": [
108	            {"translit": "metre", "gloss": null, "script": null}
109	          ],
110	          "note": null,
111	          "quote": null
112	        },
113	        {
114	          "id": 9,
115	          "parent": 8,
116	          "lang": "Persian",
117	          "refs": "MON:3800",
118	          "words": [
119	            {"translit": "metr", "gloss": null, "script": "متر"}
120	          ],
121	          "note": null,
122	          "quote": null
123	        },
124	        {
125	          "id": 10,
126	          "parent": 8,
127	          "lang": "English",
128	          "refs": "AHD",
129	          "words": [
130	            {"translit": "meter, diameter, geometry", "gloss": null, "script": null}
131	          ],
132	          "note": null,
133	          "quote": null
134	        },
135	        {
136	          "id": 11,
137	          "parent": 0,
138	          "lang": "Latin",
139	          "refs": null,
140	          "words": [],
141	          "note": null,
142	          "quote": null
143	        },
144	        {
145	          "id": 12,
146	          "parent": 11,
147	          "lang": "English",
148	          "refs": null,
149	          "words": [
150	            {"translit": "measure, dimension, semester", "gloss": null, "script": null}
151	          ],
152	          "note": null,
153	          "quote": null
154	        },
155	        {
156	          "id": 13,
157	          "parent": 0,
158	          "lang": "Germanic",
159	          "refs": "AHD",
160	          "words": [],
161	          "note": null,
162	          "quote": null
163	        },
164	        {
165	          "id": 14,
166	          "parent": 13,
167	          "lang": "English",
168	          "refs": null,
169	          "words": [
170	            {"translit": "meal, moon, month, Monday", "gloss": null, "script": null}
171	          ],
172	          "note": null,
173	          "quote": null
174	        }
175	      ]
176	    }
177	  ]
178	}
179	
```


## [2026-09-07T15:49:23.962Z] AGENT

Let me check the source matrix and refs index.


## [2026-09-07T15:49:25.374Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-07T15:49:25.420Z] TOOL RESULT

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


## [2026-09-07T15:49:27.367Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','KNT','HRN','BQT','MON','AHD','FFD','SNS','KLN','WLD','PHD','NYB','HUB','IEC','ARY','CHEUNG','BRT','SKT','WEB','FSD']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400])\n    print()\n\""
}
```


### [2026-09-07T15:49:28.709Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 

CHEUNG null

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-09-07T15:49:33.784Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','KNT','HRN','BQT','MON','AHD','FFD','SNS','BRT','PHD','IEC','WLD','KLN']:\n    v=d.get(k) or {}\n    print('==',k)\n    for f in ['local_file','page_offset','lookup_hint','scans']:\n        if v.get(f): print('  ',f,':',str(v[f])[:600])\n\""
}
```


### [2026-09-07T15:49:35.074Z] TOOL RESULT

```
== POK
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
== SYN
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== KNT
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
   page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== HRN
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== BQT
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmq
== MON
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
== AHD
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
== FFD
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt']
   page_offset : 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
   lookup_hint : Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
== SNS
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
   page_offset : 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
   lookup_hint : grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== BRT
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== IEC
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== WLD
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sou
   page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
   lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== KLN
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-07T15:49:40.387Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 70[0-9]\" POK_full.txt | head -30; echo ---; grep -n \"Page(s): 73[0-2]\" POK_full.txt | head -30"
}
```


### [2026-09-07T15:49:40.455Z] TOOL RESULT

```
57405:Page(s): 700 
57443:Page(s): 700 
57457:Page(s): 700 
57472:Page(s): 700 
57494:Page(s): 701 
57508:Page(s): 701-702 
57756:Page(s): 700-701 
57841:Page(s): 706-707 
57891:Page(s): 707 
57990:Page(s): 705-706 
58001:Page(s): 706 
58096:Page(s): 708-709 
58296:Page(s): 709 
58642:Page(s): 702 
58673:Page(s): 702-703 
60692:Page(s): 707 
60768:Page(s): 703 
60802:Page(s): 703 
60974:Page(s): 703-704 
61010:Page(s): 704 
61081:Page(s): 704-705 
---
59350:Page(s): 730 
59416:Page(s): 730 
59449:Page(s): 730-731 
59468:Page(s): 731 
59767:Page(s): 732 
59794:Page(s): 732-733 
61109:Page(s): 731-732 
61760:Page(s): 731
```


## [2026-09-07T15:49:41.043Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: mē\" POK_full.txt | head -40"
}
```


### [2026-09-07T15:49:41.097Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T15:49:43.527Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '60740,60830p' POK_full.txt; echo \"=====731=====\"; sed -n '61090,61130p' POK_full.txt; echo \"=====59460=====\"; sed -n '59440,59480p' POK_full.txt"
}
```


### [2026-09-07T15:49:43.614Z] TOOL RESULT

```
From PIE the prohibitive partiele passed to Altaie: 

Protoform: *ma 



Meaning: a negative particle 

Turkic protofomn: *-ma- 

Tungus protoform: *-me 

Korean protofomn: *nno-t 

Japanese protofomn: *-ma- 

Note: 0CH51 2, 57. A monosyllabic root, but, unlike the 1st p. pron. or the accusative 

particle, it did not undergo denasalization in PA. This may be explained by the fact that it 

was in most cases already incorporated into the verbal form as a suffix. It is interesting to 

note Mong. *bui, *bu'neg. particle' - which may be originally the same morpheme, but 

functioning as a separate word and thus subject to the rule *mV > *bV. 

References: WP. II 236 f. 
Page(s): 703 

Root / lemma: me-2, m-e-t- {hame-) 

l\^eaning: to reap 

Note: 

Root/ lemma: me-2, m-e-t- {hame-): to reap derived from Hittite hamesh{a)-, hameshant-^ 

spring, season between winter and summer '. 

Material: 

Hittite hamesh{a)-, hameshant-^ spring, season between winter and summer'. 

gr. aijaw 'mow, cut, bite', ameto-s m. "harvest', ametu-s f. "id.', ameter m. "reaper', ameta- 

s m. "sickle' 

Maybe Tokharian: B matre 'sharp' (Adams 448) 

Indo Germanic */77e/- stands besides *me-{or *ame-) in Old High German maen^mow', 
Old English mawands.; Old High German mato-screch^ Wiesenhijpfer, locust, 
grasshopper'. Modern High German A^a//e "meadow which is mowed ', Old English meed 
f. "meadow, willow ' ( *msedwu), engl. meadow. Old Swedish maf^6s. 

Latin meto, -ere, messum' to reap, mow, crop, gather, collect, harvest ' (/77e'55c»/'"reaper, 
mower'); cymr. med/'ds., acorn, m/d/7' a reaper ', Old Irish me/th/eora/" reapers ', Middle 
Irish me/fhe/'a party of reapers', acymr. medelds., anter-metelic' half-pruned ', Middle 
Irish o'e-/r7es5 "scissors' ("double knife '); Old High German /77ao'" reaping, harvesting, 
mowing, hay harvest'. Old English maed^ the mowing, the mowed hay ' (= gr. apHTO^ " the 
reaping ', originally *a|JC(TO(;). 
References: WP. II 259, WH. II 82 f. 
Page(s): 703 



Root / lemma: meig- (or melag-1) {*melagh-) 

Meaning: to pluck; to milk 

Grammatical information: present melg-mi, PI. mjg-mes, participle Perf. Pass, rrilg-to- 

Material: Old Indie marsti, marjati, mrjati^ wipes, rubs down, polishes, purifies, cleans', 

participle Perf. mrsta-, 5-present mrksatT glides, rubs, curries ', mrksayati, mraksayatT 

coats '; 

common Old Indie gh- > ks- : Avestan gh- > xs- > s- : gh- > z-, z- 

Avestan marazaiti, msrszaitT berijhrt streifend ', zasta-marsta-^ durch Handschlag (d. i. 

BeriJhrung der Hande) geschlossen (Vertrag) '; a^present Old Indie mrdati, mrc/ayat/"\s 

gracious, verzeiht, verschont', Avestan merezda-^ forgive ' {msrezdika-, marzdika-^ taking 

pity ', n. " mercifulness '); these Aryan words can also contain *merg-\ Old Indie nir-marga- 

/7 shows lacking palatal guttural) ' Verwischung; Abgestreiftes, Abfall ', ni-mrgra-^ nestlling 

up ', vi-mrgvani. "clean, neat, tidy', apamargah-^ Achyranthesaspera ' (J. Schmidt KZ. 25, 
=====731=====
(Lesbian pnvvoc;), Nom. Ionian \iz\c,, Doric \xr\(;, m. ' month ' {*mens), \xryjx\ (*|jr|vaa) 'moon'; 
alb. muai^ month ' ( */77d/7- from Indo Germanic *men-); lat mens/sm. ' month ' 
(conservative Gen. PI. mens-um), menstruus^ monthly ' (GN Mena\s gr. loanword), 
seme(n)stris^ 6-month, half-years of age, six-month-old ', Umbrian menzne^ mense '; Old 
Irish mT{*mens), Gen. mTs{*mensos), cymr. acorn, mis, bret. /77/z' month '; Gothic mena. 
Old Icelandic man!. Old English mona. Old Saxon Old High German /77a/7c»'moon' {-en- 
stem); Gothic menot^s. Old Icelandic manadr. Old English monad. Old Saxon manuth. Old 



High German manot, Modern High German month {*mendt-), Lithuanian menuo{*mendt), 
menes/sm. 'moon, month ', Latvian menes{/)s^ moon, month ' (dial. Lithuanian menas 
from a neutr. *menos). Old Prussian men/'ns' moon'; Old Bulgarian mes^cbm. 'moon, 
month ' ( *mes-n-ko-)\ 

Tocharian A man^ month ', man nkat'moon' (= ' month god '), B mene' month ', mem 
'moon'. 

References: WP. II 271 f.. WH. II 71 f., Trautmann 179 f., Brandenstein Studien 11 f. 
Page(s): 731-732 

Root / lemma: meuA^-, mauA^-, mud'^- 
Meaning: to complain or care about smth. 

Material: Npers. moja^ lament' (-/from -cf-, compare:) must' lament ' (-s/-from -d'^sf); gr. 
|j09o(; m. ' discourse ', nuGsopai ' speak, think; consider'; Gothic maudjan, ga-maudjan' 
remind sb'; Lithuanian maudziu, mausti' long, want strongly ', apmaudas' displeasure, 
care '; Old Bulgarian mysib 'thought, notion' ( *mud-slio-)\ perhaps nir. smuainidh' thinks '. 
References: WP. II 255 f., Trautmann 171 f. 
Page(s): 743 

Root/ lemma: ma-r. Gen. ma-n-es, mQtos 

Meaning: hand 

Grammatical information: heteroklitischer r/n-siem 

Material: On the r- nominative are based: gr. piapn f. 'hand', supapnt; ' manageable ', 

Ijapic;, -£U)c; m. ' liquid measure, measurement of fluid quantities '; alb. /77a/r'take, receive, 

=====59460=====
Lithuanian minkau, -///"(dough) knead', m/'nkstas 'soh', ablaut, mankau, -yti{= 
Germanic *mangjan), Latvian /77/b/7" tread', m?ksts^soi\!\ 

Old Church Slavic m§kh-kh 'soft', *m§kngtr become soft ', o-mg-citr soften ', russ. 
mjakis^ the softness of bread ', ablaut. Old Church Slavic mgka^vc\ea\, flour' (Serbo- 
Croatian muka, russ. muka6s.), mgka'agony' (Serbo-Croatian muka6s.) etc.; 

References: WP. II 368, WH. I 508, II 3, 23 f., Trautmann 184 f. 
See also: compare the similar roots mahk- and mahg-. 
Page(s): 730-731 

Root / lemma: mehng- 
Meaning: pretty, beautiful; useful thing (?) 
Note: only nominal 

Material: Old Indie manju-, mahjula-^ beautiful, mellifluous', mahgala-u. "good omen, 
luck'; osset. /77a/7^ "deceit'; gr. payyavov n. " magical cure, magic potion; philtre, war 
machine ' etc. (out of it borrowed Latin manganum^ machine ', alb. mange^ hemp-bray ' 
etc.. Middle High German mange^ catapult'. Modern High German Mange(l)^ mangle, 
machine for smoothing and ironing cloth '), gr*|jaYYU)v (out of it Latin mango^ a monger, 
slavedealer '), (jayyavEuu) "cheat, deceive, swindle; betray, be disloyal; gull, fool' etc.; 
Middle Irish meng^ deception, artifice', mengach' treacherous '; from Modern High 
German mange 6emes Old Prussian manga' whore ', Lithuanian manga' naughty 
person'; Tocharian A mahk 'b\ar(\e, fault, error'. 



References: WP. II 233, WH. II 28 f. 
Page(s): 731 



Root / lemma: mehn-1 

Meaning: to tower 

Material: Avestan framanyente {: Latin pro-minere) " they obtain projection ', mati- {*mnti-) " 

protrusion of mountain range'; 

Latin e-mineo, -ere' to stand out, project, reach upward ', im-minere' to project over,
```


## [2026-09-07T15:49:49.430Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '60900,61010p' POK_full.txt"
}
```


### [2026-09-07T15:49:49.476Z] TOOL RESULT

```
There "small cattle' could be an old nominalization of an Adj. meaning "small', one 
compares further Old Bulgarian malt ( *mdlo-) "small, little' (whereof kir. mal'i. collective 
"young sheep', etc.), Latin malus'evW, bad' (as small'), Oscan mallom, mallud^ malum ' 
(with expressive //?); 

with ani. 5- Gothic smals{*sm9-lo-). Old High German Old Saxon smal. Old English smael 
"small, little, narrow, tight, slim, slender, thin ', Old Icelandic smaleu. "small animal'. Old 
High German smala-noz, smaiaz fihu. Middle High German smal-noz, smal-vihe^6s., 
young animal ', Middle High German s/77a/-/7//'/e "herdsman, shepherd for small cattle'. 



References: WP. II 296, WH. II 20. 
Page(s): 724 



Root / lemma: me-3, m-e-t- 

Meaning: to measure 

Material: Old Indie mati, m/mat/"r(\\Q>t', m/fa-' measured, calculated ', matrai., mafra-n. " 

measure ', mana-n. 'the measuring, measure ' (: Czech men), mati-i. " measure, right 

cognition ' (= gr. mhtk;. Old English meed), upa-mati-' allocation ', mit'h ' measure, weight, 

cognition ', prakr. mettamAs. (= Old Indie *mitram)\ about mayas. 1. ma-\ 

Avestan ap. ma-^ measure ', participle -mlta-, -mata-, ap. fra-mafar-'\or6, master', 
Avestan m/f/- ' measure, weight, value, worth '; 

alb. mat, mas{*matid) " measure ', mate^ measure ', mdt{*meto-) "year, weather', 
matem^ raise the hand to strike, throw, cast' ('gauge = aim'); 

Maybe alb. moshe^ age '. 

Irish to-math-{e.g. 3. Sg. do-math/) "threaten'; 

gr. iJETpov " measure ' (after Brugmann Grundr. I|2 1, 342 as Old Indie d-a-tra-m "gift' to 
*dd-); mhtk; "plan, artifice', |jr|Tiau) " decide ', pr|TiC(0|jai " think up, dream up; invent '; 

Latin metior, -Tn, mensus sum (rhyme meaning to pensus) " measure, gauge ', whereof 
probably /77e/75a "table, a table, meal, course, a money-changer's counter, a sacrificial 
table, alter ' = Umbrian mefe^ measure ', mefa' a cake, pancake (flour, made up with milk 
or oil, and baked) ' as subst. Fem. of participle Perf. Pass.; 

mcymr. medru^ ein Ziel treffen, to be able ', to medr^ dexterity ' (: gr. [jsipov?); gall. 
matar/s^ spear, lance'; perhaps here acymr. maut. Middle Breton meut{*md-ta), ncymr. 
bawd' thumb ' (as measure?); 

Old English maedi. " measure '; Gothic me/am. " bushel '; Old Icelandic msef/rm. 6s., 
Old English maele, mele' paten '; Old Icelandic maela' measure '; Gothic melu. "time'. Old 
Icelandic mar measure, moment, time, repast, meal'. Old English mse/6s.. Old High 
German ma/' moment, repast, meal'. Modern High German ma/'meaV; 

Lithuanian metas'year, time, measure ', Old Prussian mettan'year', Latvian m^ts 
"stretch of time' (vocal as gr. iJEipov to beurteilen); in addition (*gauge > *aim > throw) 



Lithuanian metu, mesti, Latvian metu, mest'Vnrow', Iterat. Litliuanian metyt, Latvian metat 
" throw to and fro '; Old Prussian metis= Lithuanian metis vn. " throw, shot'; mastasm. " 
measure ', matasm. 6s., mafuof/" measure ', pamafas' foundation ' etc.; 

Old Church Slavic mefg, /77e5//" throw', slov. motati^ wind up, roll up ', russ. -Church 
Slavic Iterat. vbmetat/^ throw', slov. met^ throw, shot', etc.; Old Church Slavic mera' 
measure ', meriti^ measure '; Czech old men^ measure ' (: Old Indie mana-), russ. metitb 
"aim; strive ', etc.; 

Tocharian A me-, B mai- " measure '. 

References: WP. II 237 f., WH. II 70 f., 81 f., Trautmann 179, 183; related with 1. med-. 
Page(s): 703-704 

Root / lemma: me-4, mo- 
Meaning: big, important 

Material: Positive me-ro-s, mo-ro-s. gr. -pu)pO(; in £YX£cri-p(jopo(; 'big, large (?) in 
Speerwerfen ' , Old Irish mdr{dirom the comparative), mar^b\Q, large', cymr. mawr^b\i^, 
large', bret. meur6s., gall. -maros\n proper name as Nerto-maros {'b\g, large in power'); 
with eOld High German -mar\n names as Vo/k-maretc, further the denominative 
Germanic *merjan'* depict, portray, praise as great ', from which ' proclaim, announce ': 
Gothic merjan. Old Saxon marian. Old High German maren. Old Norse maera^ announce, 
declare ', wherefore Modern High German Mar, Marchen , as well as the post-verbal Adj. 
Old High German Old Saxon /775/7" illustrious, gleaming'. Old English maere. Old Norse 
mgerr6s., Gothic waila-mereis^ von gutem Ruf '; 

Slavic -merb in names as Vladi-merh; 

md-/o-\n cymr. mawr laudation ', /770//" praise, laud' (out of it Old Irish /77c»/^/''praise'), 
bret. meuliffAs:, 

comparative *me-jes, -is, respectively (with the zero grade of superlative suffix) m9-jes, 
me-fs: 0\d Irish mau, out of it mou, mo (from * mo-ids); cymr. mwy, corn, moy, bret. mui 
"more' from *meis, an abstract formation in proto Celtic -antT{ *mantT\xoxr\ ma-anti) in Old 
Irish /77e//"greatness, bulk, extent', acymr. pamint<g\. " in what manner, to what degree, 
how greatly, how, how much ', ncymr. /77a/>7/ "greatness, bulk, extent', corn, myns. Middle 
Breton nbret. ment, perhaps Oscan mais {*m9-is-) Adv. "more', maimas^ maximae ' 
(probably from *mais[e]mo-), GN Maesius^ Maius ', Umbrian mestrui. " maior ' (from 
*maistera); Gothic /77a/s"magis', maiza^ maior', maists^ maximus ', Old Icelandic meir{i) 



'more', Old English ma, mara, msest, Old Saxon mer, mero, mest, Old High German mer, 
mem, meist. Old Prussian muisieson My. "more' {mu/s irom* ma- /s-); Tocharian A msnt 
"as', B manfs'so' (= Old Irish me/'f?). 

References: WP. II 238, 292, WH. II 14. 
Page(s): 704
```


## [2026-09-07T15:49:56.737Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '61055,61095p' POK_full.txt; echo \"==== search mehnot\"; grep -n \"lemma: mehno\\|lemma: mehn-2\\|mehnot\\|mehn-s\" POK_full.txt | head"
}
```


### [2026-09-07T15:49:56.807Z] TOOL RESULT

```
from ograde Perf. grown; Mouaa " Muse, any of nine goddesses who are associated witli 
inspiration and creativity for the arts (Greel< Mythology) ' here or to men6'^-7 

auf a participle *|jaT6(; based on piaTEuw "search, seek, suche auf; strive '; participle 
*[^aa^6q, where after also (jaoTsuu) = paTsuu); [iaizi ^htsT Hes.; 

Latin mos, /77d/7s'custom| habit; mood| manner| fashion; character (pl.)| behavior] 
morals 



', morosus 'stubborn '; 

Gothic mdl=>s{-d-) " courage, rage, fury' {modags' angry, irate'). Old High German 
Middle High German muot^ power of senses; ghost, courage, rage, fury, lust, resolution, 
decision ', Modern High German Mut, Gemut, Old English mod 6s., Old Icelandic modr 
'rage, fury'; 

Balto-Slavic 'Vr75/d 'perceive, feel, sense ' in Latvian matu, masf perceive, feel ', 
originally iterative Lithuanian matau, matyti^see\ Latvian matu, mafftleeV, Lithuanian 
matrus^ careful '; based on a Subst. */77c»//'c»- Church Slavic mostrjg, motriti' observe] 
watch| look at| see; test; consider ', etc.; in addition probably Old Bulgarian si^-mejo, -meti 
'venture, risk'. 

References: WP. II 238 f., WH. II 114 f., Trautmann 171; probably to mo-, mo-lo-. 
Page(s): 704-705 

Root / lemma: menot. Gen. meneses, from which menes-, mens- mes-, men- 
Meaning: month; crescent 
Grammatical information: m. 

Note: probably as personified ' time measurement ' to me-^ measure '. 
Material: Old Indie mas, masa-m., Avestan ma. Gen. marjhd, npers. /77a/7'moon, month '; 
Armenian amis. Gen. amsoy^ month ' {*mensos); gr. Attic neologism ppv, to Gen. \xv\y6c, 
(Lesbian pnvvoc;), Nom. Ionian \iz\c,, Doric \xr\(;, m. ' month ' {*mens), \xryjx\ (*|jr|vaa) 'moon'; 
alb. muai^ month ' ( */77d/7- from Indo Germanic *men-); lat mens/sm. ' month ' 
(conservative Gen. PI. mens-um), menstruus^ monthly ' (GN Mena\s gr. loanword), 
seme(n)stris^ 6-month, half-years of age, six-month-old ', Umbrian menzne^ mense '; Old 
Irish mT{*mens), Gen. mTs{*mensos), cymr. acorn, mis, bret. /77/z' month '; Gothic mena. 
Old Icelandic man!. Old English mona. Old Saxon Old High German /77a/7c»'moon' {-en- 
==== search mehnot
59503:Root / lemma: mehn-2
```


## [2026-09-07T15:50:04.109Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 54 877 1010; do leaf=$((p+24)); echo \"=== SYN printed p.$p (leaf $leaf) ===\"; awk -v n=$((leaf+1)) 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | head -60; done"
}
```


### [2026-09-07T15:50:05.443Z] TOOL RESULT

```
=== SYN printed p.54 (leaf 78) ===
b. used first of a sharp cliff. Cf. rupes ‘cliff’ : rumpere ‘break’. Walde-P. 2.474. Ernout-M. 899.
Lat. petra, an early loanword fr. Grk. mérpa ‘rock’, becoming the pop. word for ‘stone’, whence the usual Romance words. Ernout-M. 765. REW 6445.
MLat., It. rocca ‘citadel, lofty for- tress’, It. roccia ‘rock’, OFr. roke, rocque ‘castle on a rock’ (> ME rocke ‘rocky clif?, NE rock, MDu. rotse, Du. rots) Fr. roche (whence also Toc), rocher Sp. roca, Rum. rocd, of unknown anit iad 7357. NED s.v. rock, sb,
ee see me loanword fr, Slav- ‘atandt Denes ee oe , fr. stati
ic,
3. Ir. cloch ‘stone’, W.
py ¢ cliff’ (mostly in place ea
names), etym.?
Digitized by Arya Samaj Foundation Chennai and eGangotri
YSICAL WORLD IN ITS LARGER ASPECTS 51
Stokes 73 (*kluka-, fr. same root as Goth. hallus ‘rock’, etc., but ??).
Ir. lia, gen. liach (Br. liac’h ‘stone mon- ument’), fr. *lipenk- or the like, and so perh. : Lat. lapis (above, 2). Pedersen 2.100. Loth, RC 44.293 (but doubtful of outside connection).
Ir. carric, NIr. carraig ‘rock’, W. car- reg ‘stone’, Br. karreg ‘rock’ (cf. also Ir. carrach ‘scabbed, mangy’), and with this the group It. craic, crec, NIr. craig and creag, W. craig ‘rock’ (NE crag fr. Gael.), prob. with primary Celtic sense of ‘rough, rugged’, fr. different extensions of *kar- in Ir. crach ‘harsh, rough’, Skt. karkara-, Goth. hardus ‘hard’, ete. (15.74). Loth, RC 48.401 ff. Walde-H. L051.
W. maen, Corn. men, Br. maen ‘stone’ : NIr. magen ‘place’, Ir. mag ‘plain, field’ (1.23). Pedersen 1.96. Walde-P. 2.258. Development fr. (stony) ‘field’ to ‘stone’?
Ir. all ‘rock, cliff? : OHG felis, be- low, 4.
4. Goth. stains, ON steinn, OE stan, OHG stein, etc., the general Gmc. word for ‘stone’ and in the earlier periods also ‘rock’ : Grk. oria ‘pebble’, creap ‘stiff, fat’, Skt. stya- ‘stiffen’, ChSI. sténa ‘wall’, SCr. stijena ‘rock’, etc. ‘Stone’ fr. ‘stiff, solid’. Walde-P. 2.610 ff. Feist 447, Falk-Torp 1157.
Goth. hallus ‘rock’ (so only once for aérpa, which is otherwise rendered, like AiGos, by stains), ON hallr ‘large stone’, also ‘slope, hill’ (cf. adj. hallr ‘sloping’), OE heall ‘stone, rock’ (rare except in proper names), prob. : Lat. collis ‘hill’, Lith. kalnas ‘mountain’, ete. (1.22), with development through ‘cliff’. Feist 241. Otherwise Walde-P. 1.434, 454, Falk-Torp 395, 1480.
Dan. klippe, Sw. klippa ‘rock’, fr. NHG klippe ‘cliff? : ON klif, O
=== SYN printed p.877 (leaf 901) ===
ossibly, though not neces- sarily, influenced by forms of Lat. ponere like positus. REW 6308. Gamillscheg 710.
Fr. placer, deriv. of place ‘place’ (12.11).
Rum. bdga, esp. ‘put in, thrust in’, with numerous idiomatic uses similar to those of NG Bétw (above, 2), or its cpd. prétw (bazo) ‘put in’. Some connection with the latter seems likely, though no explanation of the Rum. g is apparent. Tiktin 143 mentions Bétw, but not pata.
4. Ir. cuirim (suppl. vb. fo-cerd-) ‘throw’ and ‘put’, NIr. cuirim ‘put’, perh. : Grk. cxalpw ‘skip, frisk’, Skt. kard- ‘jump’, in any case with Irish de- velopment of ‘put’ from ‘throw’. Walde- P. 2.567. Pedersen 2.498 ff. ae
Ir. fo-rimim, fuirmim : Goth. rims ‘rest’, Lith. rimti ‘become quiet’, Grk. aptua ‘gently’, Skt. ram- ‘stand still, rest’, IE *rem-. Walde-P. 2.372. Pe- dersen 2.602. Laws, Gloss. 482.
W. dodi, etym.? (Morris Jones 332, fr. IE *d6- ‘give’ or *dhé- ‘place’; not In
,
Digitized by Arya Samaj
gpATI AL RELATIONS:
tokes with by walde-P 0 Oe Sto
duded either) V. oso 1 han ((hrous 36 fies yseD 4° pede al
rw gossol, prob. 2 deriv.
: Te jn -otd, for which cf. change to mase. gen- al nouns, Morris Jones dj. *9988) this fr. *upo-sto-, W. rhos, fr. *pro-slo-, f IE *sia- ‘stand’ Language
yerb ') of an & olr. T0ss;
‘1 derivs. 0 and ae 04). G.S. Lane,
Jakaat, fr. Lat. locare (above, 3).
Mots lat. 180. Goth (ga)saijan, ON setja, Dan.
walle Sw. salle, OF sellan, eal ee os ae Du. zellen, OHG sezzen, NHG seizen, uans, of Goth. sitan ‘sit’, etc. (12.13).
Goth, (ga)lagjan, ON leggja, Dan. logge, Sw. 1agg4, OE lecgan, ME leye, NE lay, Du. leggen, OHG leggan, NHG legen, caus. of Goth. ligan ‘lie’, etc. (214).
Dan, siille, Sw. stdlla, OHG stellan, MHG, NHG stellen (OE stellan mostly ‘stand’), fr. *stalljan : Grk. oré\\w ‘make ready, fit out? and ‘send’, Skt. sthal- tant (Dhatup.), etc., IE *stel- beside ‘a-‘stand’, Walde-P. 2.643 ff. Falk- Torp 1167, Weigand-H. 1.963.
he 12.13 tk, NG a KaOnuat (Sonat) Goth. sitan We aes ON  sitja It, Dan. idd A sidde Ir, re a, Sw. sitta p. seo OE itt Tm, gears e8lar sentado = ME wilie ‘ a “a saidim NE sit a wu Bue zitten "  eisledd sizz i Qezq MEG meat The HG  sitzen gro Words for ‘sit? belo - . ps Tepresentin ‘ong to inherited l. Ips & IE *sed- and Bo
Douta\p 7k Walde-P. 2.493 ff. Er-
Gtk. 3 (beside shs, os, Spa ‘seat’)
Foundation Chennai and eGangotri
PLACE, FORM, SIZE 833
ME pute, NE put (same word as pul in golf with differentiated pronuncia- tion), fr. OE *putian, polian, pyten ‘thrust, push’ : Sw. dial. putia ‘strike, knock’, Norw. dial. pota ‘prick, poke’, etc., perh. of imitative origin. Walde-P. 2.119. Falk-Torp 841. For the full phonetic and semantic history in Eng- lish, cf. NED s.v. put, vb."
=== SYN printed p.1010 (leaf 1034) ===
oubt).
Lat. vetus, vetustus, dim. vetulus (> VLat. veclus > It. vecchio, Fr. vieux, Sp. viejo, Rum. vechiu), Lat. veterdnus ‘veter- an’ (> vetraénus > Rum. bdirin); OLith. velugas, Lett. vecs; ChSl. vetticht in the Gospels ‘ranarés’.
3. Derivs. of IE *§er- perh. orig. ‘be- come old, ripe, frail, etc.’, vb. forms os Skt. jarati ‘makes frail, causes to age,
; r ws old’
; os frail, decays, Bro ,
! ese ‘ripen’, ete. Walde-P. Sl.
mostly of men, ‘old, re- ostly sb. ‘old man’, pl. + of things as shield,
tare c.; NG yépurs yépovras, “YépOS prone
f. ‘ pepat0s (
oman j e); jarant- ‘not tweak ed b: age’, ete. Fee. bs (NG pop. mahsos, mostly of things; of persons only in de- rogatory sense as matavOpwros worth- less fellow, rascal’), fr. adv. wadau ‘of old, Jong ago’ : THAE, Lesb. mfdue ‘far away’, W. pell ‘far distant’, Skt. carama- ‘the last’, ete, Walde-P. 1.517.
(tk. épxatos, lit. ‘belonging to the be- ginning’, hence ‘ancient, old’, fr. apx7 ‘beginning’ (14.25).
5, Fr, ancien (> NE ancient), both mostly with reference to things ‘of for- mer times’, but also in Fr. and formerly in NE ‘old’ of persons, fr. deriv. of Lat. anle ‘before’. REW 494. NED s.v. ancient.
6. NIr. gosta, lit. ‘aged’ (: aois ‘age’, a but now most general word for
NI, crionna, properly ‘wise, ex-
eg but commonly ‘old’ of per-
a, po MI. crinda ‘prudent,
es Meyer, Contrib. 518), orig.?
oh ae with crin ‘withered, shrunk,
iia , Old’, as sb. ‘dry wood fagots’? ¢ latter of. Pedersen 2.498.
TIME
Digitized by Arya Samaj Foundation Chennai and eGangotri
959
Br. koz, Corn. coth, cf. Gall. Cottos, etym.? Henry 78.
7. Goth. fairneis (‘radatés’), ON forn (‘old’ and ‘of old, of former times’), OF fyrn ‘ancient’, OHG firni, MHG virne (‘old’ and of persons ‘experienced, wise’) : Goth. af fairnin jéra ‘of the pre- vious year’, Lith. pernaz ‘in the pre- vious year’, etc., all fr. *per- in Skt. para-, OF feor ‘far, distant’, Grk. repa ‘beyond’, etc. Walde-P. 2.31. Feist 140.
Goth. albeis (‘yépw’ and neut. pl. ‘ra apxeta’), OF eald, ME, NE old, Du. oud, OHG-NHG ald, all lit. ‘nourished, grown’ fr. the root of Goth. alan ‘grow up’, ON ala, Lat. alere ‘nourish’. Walde- P. 1.86.
ON gamail (of persons), Dan. gammel, Sw. gammal, OE gamol mostly of persons (but also of sword in Beowulf), etym. dub., but prob. as orig. ‘of many winters’ : Lat. hiems, Ir. gemred ‘winter’, etc. (14.64). Walde-P. 1.547. Falk-Torp 298f. Hellquist 269.
8. ChSl. starz (in Gospels ‘peoBirns, yépwv’), ete., general Slavic :: Lith. storas ‘thick, bulky’, ON stdrr ‘large, big’, fr. the root *sta- ‘stand’, semantic develop- ment from ‘standing (firm)’ to ‘solid’, whence ‘large’ and ‘old’. Walde-P.
2.607.
9. Skt. sana-, Av. hana-, above, 1. ’ Skt. jirna-, above, 3.
Skt. vrddha- ‘grown’, pple. of vrdh- ‘grow’, often used of ‘old’ persons.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Me So Ns ee eee ee
Digitized by Arya Samaj Foundation Chennai an
```


## [2026-09-07T15:50:14.748Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"MOON\\b\" SYN.txt | head -20; echo ---; grep -n \"MEASURE\" SYN.txt | head -20; echo ---; grep -n \"MONTH\" SYN.txt | head -20"
}
```


### [2026-09-07T15:50:14.819Z] TOOL RESULT

```
1669:1.53 MOON Grk.  cedjvn Goth. ména Lith. ménuo, ménulis NG  devyapt (cedrv7 lit.) ON mani (poet.), tungl Lett. ménesis Lat. lina Dan. maane ChSl. luna, mésgct It. luna Sw. mane SCr.  mjesic Fr. lune OE mona Boh. _mésic Sp. -luna ME mone Pol.  ksigzyc Rum. lund NE moon Russ. luna Ir. ésce (luan) Du. maan Skt. (mGs-), candra-, ¢a- Nir. gealach, ré (éascd) OHG wmédno ¢cin-, etc. W. Ueuad, lloer MHG mane Av. mah- Br. loar NHG mond
---
22421:12.54 MEASURE (vb.) hope Goth. mitan Lith. matuoli, mieruott pees ON mela Lett. merit métiré Dan. maale ChSl.  mériti pzere Sw. miata SCr.  mjeriti i OE metan Boh. méritt ; file ME mete, mesure Pol. —-mierzyé oma NE measure Russ. merit’ Neate, Du. —_meten Skt.  md- mesur(o) OHG mezzan Av.  ma- muzula MHG mezzen All th NHG ~ messen he of a for ‘measure’ are from Skt., Av. md-; Grk. sb. pérpov (: Skt. aby relate d E roots, themselves prob- | ma-tra-~m as Skt. da-ira-m : Av. dda-6ra- LT oy timately . m) whence vb. perpéew; Lat. mélirt liter mostly the nouns and verbs, the | through a sb. *méti- (cf. OE med ‘meas- n Indo. Tani Tough the nouns, except | ure’, Grk. paris ‘plan, wisdom’), VLat. OUt-M, e Walde-P. 2.237. Er- | *matire (>Sp., Port. medir), pple. Ton 6g Be REW 5508, 5552. Falk- | ménsus (hence ménsura sb. and late de-
---
25680:14.71 MONTH
```


## [2026-09-07T15:50:19.312Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=1640 && NR<=1700' SYN.txt | grep -nE \"^[0-9]{1,4}$|PHYSICAL|Digitized\" | head; echo \"--- context 1669\"; sed -n '1660,1690p' SYN.txt"
}
```


### [2026-09-07T15:50:20.723Z] TOOL RESULT

```
4:: ar Digitized by Arya Samaj Foundation Chennai and eGangotri
5:THE PHYSICAL WORLD IN ITS LARGER ASPECTS 53
36:Digitized by Arya Samaj Foundation Chennai and eGangotri
37:THE PHYSICAL WORLD IN ITS LARGER ASPECTS 55
--- context 1669
o4 SELECTED INDO-EUROPEAN SYNONYMS
1.52 SUN
Lo” i ial. aféAtos, Goth. sauzl, sunnéd Lith.  saulé So oe : ON _ sdl, sunna Lett. saule NG — #Xos Dan. sol Ch&Sl. _ sliintce Lat. sol Sw. sol SCr.  sunce It. sole OE sunne, sunna Boh. — slunce Fr. soleil ME sonne Pol. slovice Sp. sol NE sun Russ. solnce Rum. soare Du. zon Skt. suar (Ved.), strya-, Ir. grian OHG = sunna ravi-, etc. NIr. = grian MHG sunne Av. hvara, gen. hird and W. haul NHG __sonne x’éng Br. heol
Nearly all the usual words for ‘sun’ belong to a single inherited group.
1. IB *sawel-, etc., a group with vow- el gradation, parallel /- and n- forms (the Slavic fr. *sulno- with added dim. suffix), and variation in gender. Walde-P. 2.446. Ernout-M. 950f. Falk-Torp 1105. Feist 412, 460. Here belong all the words listed except the following.
2. Ir. grian, NIr. grian, fr. *greina, prob. formed fr. the weak grade of IE *g’her- seen in words for ‘hot, heat’, as Nir. gor, NE warm, Grk. Oepyds, Skt. gharma-, etc. This connection is ques-
tioned by Pedersen, KZ 38.197 (Walde- P. 1.688). But cf. esp. Skt. ghrna- ‘heat? and ‘sunshine’, and (fr. Skt. gharma-) Hind. ghém ‘sunshine’, Gypsy gam, k‘am ‘sun’ (Sampson, Dial. of Gypsies of Wales, 166).
3. Skt. ravi-, perh. the commonest class. word for ‘sun’, Arm. arev ‘sun’.: Skt. aruna-, arusa- ‘reddish’ (both often applied to the sun), Av. aurusa- ‘white’. Walde-P. 2.359. Uhlenbeck 246.
Among other Skt. words for ‘sun’ are : bhana- fr. bha- ‘shine’, bhas-kara-, lit. ‘light-making’, dina-kara- lit. ‘day-mak- ing’, arka- fr. arc- ‘shine’.
1.53 MOON Grk.  cedjvn Goth. ména Lith. ménuo, ménulis NG  devyapt (cedrv7 lit.) ON mani (poet.), tungl Lett. ménesis Lat. lina Dan. maane ChSl. luna, mésgct It. luna Sw. mane SCr.  mjesic Fr. lune OE mona Boh. _mésic Sp. -luna ME mone Pol.  ksigzyc Rum. lund NE moon Russ. luna Ir. ésce (luan) Du. maan Skt. (mGs-), candra-, ¢a- Nir. gealach, ré (éascd) OHG wmédno ¢cin-, etc. W. Ueuad, lloer MHG mane Av. mah- Br. loar NHG mond
1. IE *ménes-, *mén(n)s- ‘moon’ and | ‘moon’, ménesis ‘month’), Lett. ménesis,
‘month’, presumably fr. *mé- ‘measure’. Walde-P. 2.271f. Ernout-M. 607 f. Walde-H. 2.71. Berneker 2.51.
Here belong: (1) with the same form in both senses, Lith. ménuo, etc. (but here also with differentiation ménulis
ChSl. mésect (but mostly ‘month’; luna more common for ‘moon’), SCr. mjesic, Boh. mésic, Skt. mas- (as in Rigveda, later mostly ‘month’, rarely ‘moon’), Av. mah- (OPers. mah- ‘month’), NPers. mah-, Toch. A maf, or for ‘moon’ maf
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 55
+ (nat ‘god, goddess’ used as a de- eS ay (2) with differentiation, all the Gme. forms, as Goth. ména ‘moon’, ménops ‘month’, NE ade month, etc.; Toch B mem ‘moon eae ‘month’ (so Benveniste, Festschrift Hirt. 2,234, but S. Levi, Fragments Koutsch. 1.121 gives ‘lune’ for both forms).
Elsewhere, namely in Greek, Italic, Celtic, Albanian, Armenian, and in some of the Slavic languages, the words of this group have persisted only in the sense of ‘month’ (Grk. piv, Lat. ménsis, Ir. mi, etc.; 14.61) and have been displaced in the sense of ‘moon’ by other words, most of them from the notion of ‘brightness’ as follows.
2. Grk. cedqvn, Dor. ceddéva, Lesb. cedavva : oédas ‘light, brightness’ (of fire or the heavenly bodies). Walde-P. 2.531. Boisacq 858.
NG g¢eyyap:, dim. of Grk. déyyos ‘light, splendor’ (of daylight or moon- light).
3. Lat. lina, fr. *leuksna- (cf. Praen. losna) : Lat. lia, lamen ‘light’, Grk. Aeuxds ‘bright’, Av. raoxsna- ‘light’, OPruss. lauxnos ‘stars’, ete. Here also as ‘moon’, Ch§l., Russ. luna, Arm. lusin, Ir. wan, (poet.; Thurneysen, Z. deutsch, Wortf. 1.189) and, fr. a parallel form of
the root, W. lleuad, lloer, Br. loar? Walde-P. 2.408 ff. Ernout-M. 570 ff.
From Lat. lina come It., Sp. luna, Fr. lune, and Rum. lund, the last both ‘moon’ and ‘month’, because of the double sense of Slavic més¢ci. —
4, Ir. ésce, NIr. éasca : Osc. eiduis, Lat. idus ‘ides’? Walde-P. 1.103.
NIv. gealach ‘moon’ also ‘light, bright- ness’, fr. geal ‘bright, white’ (15.57).
Ir. ré ‘period of time’, NIr. also esp. ‘moon’ Av. ravah- ‘space, room’, etc.(?). Wendryes, RC 28.141.
5. ON tungl, replacing manz in prose, beside himun-tungl ‘heavenly body’ : Goth. tuggl, OE tungol ‘heavenly body’, root connection? Walde-P. 1.792. Feist 481 f.
6. Pol. ksiezyc, displacing miesiac in the sense of ‘moon’, dim. of ksiqdz in its older meaning ‘prince’ (19.35). As the sun was the lord of the day, the moon of the night, the latter was the lesser ‘prince’. Briickner 277.
7. Skt. candra-, also (combined with mdas-) candramas- : (¢)candra- ‘bright’, (¢)cand- ‘shine’, Lat. candére ‘shine’, Alb. haéné ‘moon’, etc. Walde-P. 1.352.
Skt. cacin-, fr. gaga- ‘hare’, after the supposed resemblance of the markings on the moon.
```


## [2026-09-07T15:50:26.171Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22415,22440p' SYN.txt; echo \"======= MONTH\"; sed -n '25670,25700p' SYN.txt"
}
```


### [2026-09-07T15:50:26.233Z] TOOL RESULT

```
V. fu : Lat. tumere ‘swell, be swoll- a, fr, an extension of the root *éu- in Sut, fduli ‘is strong’, ChSl. tyéz “become fat’, etc, Walde-P. 1.708. Ernout-M. 1064.
Br. kreski, prob. fr. Lat. créscere. Henry 81. Loth, Mots lat. 154 (with sme question on account of the short vorel),
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 877 5. ME growe, NE grow, Du. groeien, but OE gréwan, ON gréa, OHG gruoan only ‘grow’ (of plants), ‘spring up, be- come green, etc.’ : MHG gruose ‘shoot of a plant, sap’, Goth., ON, OHG gras OE graes ‘grass’, ON grenn, OE gréne, OHG gruoni ‘green’, Lat. gramen ‘grass’. Walde-P. 1.645f. NED s.v. grow, vb. 6. ChSl. rasti, etc., general Slavic (Pol. r6sé replaced in present by rosnqé), fr. *ord(h)-t-, prob. : Lat. arduus ‘steep, high’, Ir. ard, Av. aradwa- ‘high’. Walde-P. 1.149. Briickner 463.
7. Skt. vrdh- act. and caus. ‘make grow or thrive, elevate’, mid. ‘grow, thrive’, Av. varad- act. (and mid.) ‘make grow or thrive, increase’, mid. and pass. ‘grow, thrive’ : ardhva- ‘up- ward, upright, raised, elevated’, Grk. dps ‘upright, straight’, Slavic roditi ‘bear’. Walde-P. 1.289.
Skt. rudh-, ruh-, Av. rud- (pres. 3pl. Skt. rodhanti, Av. raodanti) : Goth. liu- dan ‘grow up’ (of seed, Mk. 4.27), OK léodan, OHG ar-liotan ‘spring, grow’ (of plants), ON lodinn ‘grown over, hairy’. Walde-P. 2.416.
12.54 MEASURE (vb.) hope Goth. mitan Lith. matuoli, mieruott pees ON mela Lett. merit métiré Dan. maale ChSl.  mériti pzere Sw. miata SCr.  mjeriti i OE metan Boh. méritt ; file ME mete, mesure Pol. —-mierzyé oma NE measure Russ. merit’ Neate, Du. —_meten Skt.  md- mesur(o) OHG mezzan Av.  ma- muzula MHG mezzen All th NHG ~ messen he of a for ‘measure’ are from Skt., Av. md-; Grk. sb. pérpov (: Skt. aby relate d E roots, themselves prob- | ma-tra-~m as Skt. da-ira-m : Av. dda-6ra- LT oy timately . m) whence vb. perpéew; Lat. mélirt liter mostly the nouns and verbs, the | through a sb. *méti- (cf. OE med ‘meas- n Indo. Tani Tough the nouns, except | ure’, Grk. paris ‘plan, wisdom’), VLat. OUt-M, e Walde-P. 2.237. Er- | *matire (>Sp., Port. medir), pple. Ton 6g Be REW 5508, 5552. Falk- | ménsus (hence ménsura sb. and late de-
e —-— = . teker 2.50, nom. ménsirare >It. misurare, Fr.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
878
mesurer, Rum. mdsura); ON mela, Dan. maale (ON mal, Dan. maal, Sw. mdl ‘measure, point of time, meal, etc.’); Lith. matuoti; ChSI. sb. méra, whence vb. mériti, etc., general Slavic (hence Lith. mieruolt, Lett. mérit); here (?) Toch. A me- (SSS 456, but B form lacking).
W. mesur, mesuro, Br. muzula, fr. sbs. W. mesur, Br. muzul, MBr. mesur, fr. Lat. ménsura. Loth, Mots lat. 187.
ME mesure, NE measure fr. Fr. me- surer.
SELECTED INDO-EUROPEAN SYNONYMS
2. IE *med- in words for ‘measure’ and esp. ‘measure, estimate with the mind, reflect.’ Walde-P. 2.259. Bp. nout-M. 599. Walde-H. 2.55 f. Feist 363.
Tr. domidiur (vbl. noun tomus, Ny. tomhas, hence témhaisim), epd. of midiur ‘judge’; Goth. mitan, OB metan, OHG mezzan, etc., general Gmc. (but ON meta ‘value, estimate’) : Grk. Hédouat ‘be mindful of’, Lat. medérz ‘care for’, esp. ‘heal’, meditarz ‘reflect upon’.
12.55 LARGE, BIG (GREAT)
Grk, péyas Goth. mikils Lith. didis, didelis NG peyddos ON storr, mikill Lett. Liels
Lat. magnus, grandis Dan. stor ChSl.  velijt, velikit It. grande, grosso Sw. slor SCr. _velik
Fr. grand, gros OE micel Boh.  vel(i)ky
Sp. grande ME mikel, grete (bigg) Pol. wielki
Rum. mare NE large, big (great) Russ.  bol’§oj (velikij) Ir. mar, bras(s), oll Du. groot Skt. mahant-, mah- NIr. mar OHG = mihhil, groz Av. mazant-, maz-, W. mawr MHG gréz, michel masan-; OPers. Br. bras NHG gross vazarka-
Many of the words for ‘large, big’ be- long to inherited groups, one of them so widespread as to leave no doubt that it reflects the chief IE expression for ‘great, large’ with the familiar extensions be- yond the notion of size.
Yet this group is represented in the present European languages only by NG Heyahos or by dialect forms like NE mickle and muckle (also NE much but no longer used of size). As Lat. magnus was replaced by grandis, so Goth. mikils, OE micel, etc., were replaced in Scan- dinavian by ON storr, Dan., Sw. stor, in West Gme. by the group represented by NE great, which in turn is now used mostly in secondary senses or with emotional value, and with reference to size, except in certain phrases, com- pounds, and place names, is replaced by large or its more colloquial and expres- sive equivalent big.
The words not of the inherited groups reflect such diverse notions as ‘thick, coarse’, ‘abundant, spacious’, ‘swollen’, ‘strong’, etc.
======= MONTH
served intact by the British
TIME
Digitized by Arya Samaj Foundation Chennai and eGangotri
1009
Celts, that is in W., Br., and Corn. (Corn. de sil, de lun, etc., Williams 88), but furnish only three of the Ir. names, namely lwan ‘Monday’, mdirt ‘Tues- day’, satharn ‘Saturday’.
The Latin planetary names were also adopted by the Gmc. peoples (except the Goths in the East), only put into Gme. form—a simple procedure in the case of diés Solis and diés Liinae, but for the next four involving a somewhat less ob- vious identification of Roman and Ger- manic gods. For Saturday the Lat. Saturnus was retained, at least in Anglo- Frisian and Low German (OF seter(n)- deg, OFris. saterdei, Du. zaterdag). Scandinavian shows a native substitu- tion, ON laugardagr, Dan. Igrdag, Sw. lérdag, lit. ‘bathday’ (: ON laug ‘bath’), also ON fvdttdagr ‘washday’ (: ON pvattr ‘washing’), both referring to the same custom (Falk-Torp 682). High German has the eccl. name, OHG sam- baztag, NHG samstag (cf. above), be- side the new term OHG sunninaband, NHG sonnabend, which orig. applied only to the eve preceding Sunday. The planetary name for Wednesday is lack- ing in High German, where OHG miit- wocha, NHG mittwoch is prob. of eccl. origin (cf. above). MHG erintac, ertac (Bavar. ertag) may represent a Goth. *areinsdags, fr. Grk. “Apews jpépa (Kluge- G. 105).
Nicel. is peculiar among the Gmc. languages in retaining only two of the planetary names, sunnudagur and md- nudagur, and in having two numeral names, pridjudagur for Tuesday and fimtudagur for Thursday. Wednesday is midvikudagur like NHG mittwoch, Saturday is laugardagur ‘washday’ as in the other Scandinavian languages, and Friday is fostudagur ‘fastday’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1010 SELECTED INDO-EUROPEAN SYNONYMS
14.71 MONTH
Grk. opi Goth. méndps Lith. ménesis, ményo NG Lives ON manadr Lett. ménesis
Lat. ménsis Dan. maaned ChSl.  mésect
It. mese Sw. mdnad SCr. — mjesec
Tr. mois OE monad Boh. mésic
Sp. mes ME mon(e)th Pol. miesiac Rum. lund NE month Russ. mesjac
Ir. mi Du. maand Skt. mdas-, masa- NIr. mi OHG mandot Av., OPers. mah- W. mis MHG manét Toch. A mai, B mee Br. miz NHG = monat
TE *ménes-, *mé(n)s- ‘moon’ and ‘month’, prob. fr. *mé ‘measure’. Walde-P. 2.271f. Ernout-M. 607f. Walde-H. 2.71.
While the words of this group have in many languages been replaced by others in the sense of ‘moon’, they have per- sisted nearly everywhere as the words for ‘month’. In Gme. a separate set of re- lated forms distinguishes ‘month’ fr. ‘moon’, as Goth. méndps vs. ména ‘moon’, OF ménad vs. mona ‘moon’, etc. There is a similar but incomplete differ- entiation in Lith., where ménulis is only ‘moon’ and ménesis mostly ‘month’, but ménuo in both senses. See also 1.53.
The only word in the list which does not belong to the group above is Rum. lund, fr. Lat. lana ‘moon’, in which the identification of ‘moon’ and ‘month’ is repeated, doubtless owing to the identity in Slavic (ChSI. mésect, etc.).
14.72. Names of the months. Pre- vious to the widespread, though still in- complete, Eur. adoption of the Lat. names, there was the utmost diversity. In ancient Greece alone there were doz- ens of different local calendars (cf. Pauly- Wissowa 10.1575 ff.). There was no agreement between the old Gmc. names (even the OHG lists vary somewhat), nor between Indic and Iranian, not even be- tween the Ay. and OPers. names. Nei- ther the modern Lith. literary names, a
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar a eee
recent coinage (Senn, Sprachl. 168), nor the diverse olderand dialectic f. orms (Her- mann, Gott. Nachr. 1929.97) agree with the older, now obs., Lett. names. Among the native Slavic names, which are still current except in Russ., there are a few cases of agreement between Boh. and Pol., and a few others of common words applied to different months (e.g. listopad, lit. ‘leaf-falling’, in SCr. ‘October’, Boh., Pol. ‘November’; Boh. kvéten ‘May’ = Pol. kwiecier ‘April’, orig. ‘flower- month’), but, on the whole, great diver- sity.
In general, the month-names are based upon religious festivals (so most of the Grk. and some of the Celtic and Gmc.) or upon some characteristic fea- ture of the weather, vegetation, har- vest, etc.
The enumeration and discussion of these so diverse month-names (even if one chose for the Greek only the Attic or for OHG only those prescribed by Charlemagne) would require so much space that it seems best here to consider only the Lat. names and their spread.
The Lat. names were adj. forms with ménsis ‘month’ understood. Since the Roman year orig. began with March, the numeral derivs. which served is July-December, were Quinctilis ‘fifth for July, Sextilis ‘sixth’ for August (these later replaced by Idlius and Augustus 0 honor of Julius Caesar and Augustus),
aay oR eS Ae et ee ae
i a hen
October, November, December novem-ri-s, *decem-ri-s, f medial mr to mbr,
order beginning with Janu- Fe er eidesoon naisly the names of gods or g dTa RABE. Janus, Mars, Mava, an nel neces arius, the last month of the o ca en ar, yas the ‘month of PUAN NOH, fr. februdre ‘cleanse, purify (Ernout-M. 34], Walde-H. 1.472). Aprilis, prob. f, an Btruscan name based on a short form of Grk. Adpodirn. Benveniste BSL 32.70 ff. Cortsen, Glotia 27.270 ff.
The Roman names have persisted in all the Romance languages. But most of the Rum. forms go back, partly through Slavic, to the later Grk. bor- rowed forms. And elsewhere there are various formal peculiarities, e.g. for tinudrius VLat. cenudrius (> It. gen- naio, Sp. enero); for augustus VLat.
```


## [2026-09-07T15:50:34.019Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"framānā\\|framana\\|framāna\\|fram-\" KNT.txt | head -20; echo \"=== ma-\"; grep -n \"^mā-\\|^ma- \\|^māh\\|mā- 'measure\\|to measure\" KNT.txt | head -20"
}
```


### [2026-09-07T15:50:34.084Z] TOOL RESULT

```
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
=== ma-
5754:mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
```


## [2026-09-07T15:50:40.315Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=5754' KNT.txt | tr -cd '\\f' | wc -c; echo \"--- framānā entry\"; grep -n \"framānā\\|framanà\\|framànà\\|framātar\\|framàtar\" KNT.txt | head"
}
```


### [2026-09-07T15:50:41.643Z] TOOL RESULT

```
225
--- framānā entry
4130:28 camaly :? uSiy : ша : framànà : yabamai
```


## [2026-09-07T15:50:47.208Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^framā\\|^frama\\|^fram\" KNT.txt | head -20; echo \"=== leaf boundaries: find printed page numbers near lexicon\"; awk 'BEGIN{RS=\"\\f\"} NR>=210 && NR<=232 {print \"LEAF \" NR-1 \" :: \" substr($0,1,150)}' KNT.txt"
}
```


### [2026-09-07T15:50:48.574Z] TOOL RESULT

```
744:framdtéram A*Pa 8, for the common framátüram.
5702:framatar- sb. ‘master, lord’ (‘giver of judicial decisions’, ace. to Hz. ApI 150-4): fra- + root mā- + agent suffix -tar- (5154.1). framatéram asm. (§124.VI, $1861) DNa 7f; DSe 7; DSf 5; DE 11; XPa 5; XPb 11; XPe 5; XPd 8; ХР? 7f; XPh 6; XE 11; XV 9; A'Pa 8°; A?He 7. frama- ібгат (852.111) A?Pa 8.
5703:framána- sb. ‘command’ (judgment, deci- sion’, acc. to Hz. ApI 144-50): РЫ. framán, NPers.
=== leaf boundaries: find printed page numbers near lexicon
LEAF 209 :: it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
tanii- sb. �
LEAF 210 :: 1) XPh 23.
tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) AmH 5; AsH 13°. tyà npf. DB 1.13, 18; 2.6; 4.33; DPe 9, 14f; DSf 45. tyaiy as npf. (§258.
LEAF 211 ::  word of uncertain meaning, Sb 3.
Sanuvaniya- sb. ‘bowman’: deriv. ($144.IV) of stem in Av. Üanvar/n- ‘bow’, ef. Skt. dhanvan- ‘bow’ (583
LEAF 212 :: fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3
LEAF 213 :: 5-6).
Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk.
LEAF 214 :: Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
Daha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; 
LEAF 215 :: rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DS
LEAF 216 :: e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘n
LEAF 217 :: n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (suppl
LEAF 218 :: with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of
LEAF 219 :: ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte. pass. ($242.1) DNb 54 (dubious con]. of Kent, Lg. 15
LEAF 220 :: tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69
LEAF 221 :: r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II); see also hamapilar-. pita пет. ($86.П, $124.5, $186.1T) DB 1.4 b
LEAF 222 :: -. — fra&aram asn. XPf 26f, 37.
Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-ra-da, АКК. pa-ra-da-’ ; perhaps thematic noun- stem (§14
LEAF 223 :: 1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. 
LEAF 224 :: 2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54, 60, 68, 86, 97^; 3.6, 17, 37, 45, 62, 67 (written ar?r^, 854.11), 87
LEAF 225 :: BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11.
brdtar- sb. ‘b
LEAF 226 :: 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 1
LEAF 227 :: ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48,
LEAF 228 :: so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a province: Elam. mu-is-sa-ri-ia, АКК. mi-sir (S6, §76.V).
(1
LEAF 229 :: d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass.
LEAF 230 :: am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $
LEAF 231 :: 1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71,
```


## [2026-09-07T15:50:52.769Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=5702' KNT.txt | tr -cd '\\f' | wc -c; echo \"---\"; sed -n '5700,5712p' KNT.txt"
}
```


### [2026-09-07T15:50:54.163Z] TOOL RESULT

```
222
---
frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl. -thama- in Skt. prathamd- ‘first’. Cf. also uradara-. — fra&aram asn. XPf 26f, 37.
Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-ra-da, АКК. pa-ra-da-’ ; perhaps thematic noun- stem (§141) to fra- + *dà-, with vriddhi ($126), cf. Av. früd- ‘to further, increase’ (ТИМ. AiW 1012), but more probably hypocoristie to a com- pound name ($164.П1; Bthl. AiW 1018) of which the prior part was the participial stem to the same compound verb (§162), ef. Av. adj. fradat.qaéa- ‘prospering the household’, sb. frddaj.fsav- ‘Pro- moter of flocks’ (name of a divinity; Bthl. AiW 1013-4). Not with Sen 52 (fra- + OP *ad- ‘drive’, Av. azaiti, Skt. djati, Lt. agit), nor with Justi, INB 101 (fra- + had- ‘sit’, with loss of intervocalic -h-). Fraéda nsm. DB 3.12; 4.23; ОВ] 1.
framatar- sb. ‘master, lord’ (‘giver of judicial decisions’, ace. to Hz. ApI 150-4): fra- + root mā- + agent suffix -tar- (5154.1). framatéram asm. (§124.VI, $1861) DNa 7f; DSe 7; DSf 5; DE 11; XPa 5; XPb 11; XPe 5; XPd 8; ХР? 7f; XPh 6; XE 11; XV 9; A'Pa 8°; A?He 7. frama- ібгат (852.111) A?Pa 8.
framána- sb. ‘command’ (judgment, deci- sion’, acc. to Hz. ApI 144-50): РЫ. framán, NPers.
OLD PERSIAN
fürmán; fra- + mä- + suffix -nà- ($128, $1471), ef. Skt. pramána-m ‘measure, standard’. — framánà nsf. DNa 57; DNb 28; DSj 3°, framánáyà isf. DNb 37.
fravata adv. ‘forward, downward’: Phl. frót, NPers. fáród јато; from *frava-, extension of fra- as in Gk. rpõros ‘first’ from *proya-, + -tos as in amata (§191.1I; JAOS 51.204, 53.15; Bv. BSLP 30.1.59; hardly with Kénig, Burgbau 51; not identical with Skt. isf. pravátà ‘downhill’). DSf 23f, 28.
Frovartz- sb. ‘Phraortes’, a Median rebel: Elam. pir-ru-mar-t-18, Akk. pa-ar-ti-mar-ti-1§ Gk. Ppadprys: identical either with Av. frava&i- ‘guar- dian angel, soul’, from fra- + var- ‘protect’ + -ti- (S31, 8152.11) as ‘Protection’, or with Av. fraoroti- "Siehbekennen zu’, from fra- + var- ‘choose (re- ligiously)’ + -й- (Bthl. AIW 991, 992, 976; Nyberg Rel. 334-5, prefers second view); as man’s name, probably liypocoristic of a longer compound ($164.1). — Fravarti$ пата. DB 2.14, 66, 71, 73; 4.18; DBe 1f. Fravartim asm. DB 2.17. Fravar- tas gsm. DB 2.69, 93.
fras- vb., see јтаб-.
fraša- adj. ‘excellent’ (‘tauglich’, König Burg- bau 48, Brd. АКМ 39.87): Av. frasa- ‘directed toward, useful’, formed on adv. fraša to frünk-, Skt. adv. praca to ртайс-, from pra- + añe- (Bthl. AiW 1006-7); the irregular -3- for -s- of Sy- may be a contamination of *frasa- and *frasya- (otherwise ВБ. IF 2,266-7; borrowed from Aves- tan aec. to Hz. ApI 162). Hz. ApI 156-65 (recant- ing derivation from fra- + záy- ‘shine’, ‘brilliant’, AMI 3.1-11) takes as deriv. of pra-, through an idiom of racing or fighting, as 'extra (certamen), hors (concours)’, and therefore "incomparable, su- preme’. Cf. also Hz. RHRel. 113.26; Bailey, BSOS 6.595-7; Kent, Lg. 15.169. — frasam nsn. DSa 5, DS] 6 (see frasta-, for reading). frasam asn. DNb 2; DSf 56, 56f; DSo 4^; DSs 1°.
frašta DSa 5, DS] 6: discussed by Bv. ВІР 30.1.63-4, Gr. $103, Gray AJP 53.67, Brd. WZKM 39.20-1; but fra$am @adaydlary and not frašta ðadayämaiy ($54.11) should be read in both pas- sages (Hz. AMI 3.9-10, ApI 156-8). See under frasa-.
(mu. em lere Am ee шшш. ште у. mi ease e +
LEXICON 199
```


## [2026-09-07T15:51:04.063Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==224' KNT.txt | head -c 3000; echo; echo \"@@@@@ TAIL\"; awk 'BEGIN{RS=\"\\f\"} NR==224' KNT.txt | tail -c 800"
}
```


### [2026-09-07T15:51:05.343Z] TOOL RESULT

```
1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
ba*d- vb. ‘hind’: Av. band-, Skt. bandh-, Gt. bindan, pIE *bhendh-. See also badaka-. basta (NPers. bäst) nsm. past pte. pass. (867, $85, 5120, $122, 5182.1, 52421) DB. 1.82; 2.75, 90; 5.26. basta apm. DB 3.88".
ba"daka- sb. ‘subject, servant’ (cf. König, Кыр 64): Phi. bandak, NPers. bändäh; deriv. (§146.1T) of OP *ba"da- ‘bond, fetter’, Av. banda-, Skt. bandhd-, to pIE root *bhendh- (OP ba"d-; $39, $75.11, $111, §122, 8132.1). bada
@@@@@ TAIL
B 2.65. Варта lsm. DB 1.78, 81;
200 OLD PERSIAN
2.5, 6; 3.79, 88, 92; 4.2; DBd 7f; DBi 11 (written Bab*raw, $22); DSf 33 as loc. with усій, 33 as abl. with Ласа (hardly a real abl., corresponding to Av. -aut despite Hz. AMI 3.55n, Kent ЈАО 53.16).
Bābirwiya- adj. ‘Babylonian’: deriv. ($144.- ПТ) to preceding. — Bábiruviya nsm. DB 1.77, 79; 8.81; 4.13; DSf 20. Babiruviyam asm. DB 3.86. Babiruviyé npm. DB 3.78; DSf 53f. Bäbiruviyä apm. DB 3.88.
bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, $75.III, 5226.1) DB 1.2
```


## [2026-09-07T15:51:17.588Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 225 226 227; do echo \"##### awk block $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | grep -oE \"(LEXICON [0-9]+|[0-9]+ OLD PERSIAN)\" ; done"
}
```


### [2026-09-07T15:51:18.871Z] TOOL RESULT

```
Exit code 1
##### awk block 225
##### awk block 226
202 OLD PERSIAN
##### awk block 227
```


## [2026-09-07T15:51:23.671Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==226' KNT.txt | grep -n \"202 OLD PERSIAN\\|mā- vb\\|^mā-\\|framā\" | head"
}
```


### [2026-09-07T15:51:25.203Z] TOOL RESULT

```
9:mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
17:202 OLD PERSIAN
```


## [2026-09-07T15:51:31.367Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 80 233; do n=$((p+21+1)); echo \"##### HRN printed p.$p (awk block $n)\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | head -60; done"
}
```


### [2026-09-07T15:51:32.824Z] TOOL RESULT

```
##### HRN printed p.80 (awk block 102)
— 80 -
357. 2^^'*^^ ^Handwerk, Gewerbe'.
aw. vergl. pistro- 'Gewerbe*; phlv. pesak.
358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
aw. "^paiti + 2 [/"gar' (ai. praii + gar- bedeutet auch
nur 'anrufen, begrüssen, antworten).
Spiegel, Ar. Periode, 229.
Bartholomae meint, man könne auch an Ableitung
von ai. prati + [^har- denken (vergl. pratihdrana- und
die Bedeutung von lat. ohjicere), Ai. h entspricht ja
sowohl indogermanischem gji wie g2h,
peiyäni s. peyäm (No. 348).
359. peig (peik) Tussgänger, Häscher, Bote', arab. faij,
aw. "^padika-,
de Lagarde, Ges. Abh. 74; Nöldeke, Tabari-
Übers. 448, Note 2, vergl. auch Denkschr. WAW.
Band 38, 14.
360. peikär, peigär *Kampf'.
aw. *paitikära' vergl. paiti.akerenaot (vd. 2, 6);
phlv. patkär 'Kampf (z. B. vd. 5 (33) GL), patkäritan
'Köcher, (z. B. vd. 4 (137)), patkärok (AV.).
arm. LW. payUar *Kampf' .
361. peiker *Bild'.
Sii^. patikara- 'Bild'; iphlv, patkar (Bund.), arm. LW.
pafker.
362. peikän 'Pfeilspitze, Pfeil'.
aw. paiti -\- [/kan- (?); arm. LW. paikan\daran
de Lagarde, No. 1834.
vergl. serb. LW. pHk 'Pfeilzeichen der fahrenden
Leute (Miklosich, Denkschr. WAW. Band 38, 11);
während peik 'Bote, Laufbursche' (ib. Band 35, 144
und 38, 11) zu np. peik (No. 359) gehört.
363. pei/imiden'mQ^^Gn\ zeigen', Prsies. peimäy-emj peimäny
peimäne^).
*) An der letzten Stelle wie auch sonst (z. B. IIT, 1642, Vers 2,
Calc, 1708, V. 3765) ist in der VuUers-Landauer'schen Ausgabe
h^ in p^ zu ändern.
«) Eine *Masft' (HohlmassJ, z. B. Jnnn ZKM. V, 302.
##### HRN printed p.233 (awk block 255)
— 233 —
kurd. LW. tiem; afy. lünd 'feucht'; bei. wami *Tau,
Neber (252).
1040. nemäfi 'Gebet', TNOi: (Is. 1, 14).
aw. vergl. nemah- 'Gebet; ai. /ia/zias- ; phl v. nawäc
(päz. namaS).
LW. kurd. nimlz, nirm *Gebet'; afy. nmünj ; bei.
namäs, nawäs (251).
Da alle neuiranischen Formen auf die mittel-
persische charakteristische Neubildung natnäc zu-
rückgehen, so halte ich dieselben sämmtlich für
Lehnwörter.
Fr. Müller, (WZKM. 5, 67) nimmt als Grundform
ap. *namascij/ an; aber ap. sc konnte im Neuper-
sischen doch nicht zu ^ werden. Diesen Lautüber-
gang durch np. d^^, niz zu stützen, ist verfehlt.
1041. nemed grober Teppich, Filz', ar. LW. namat.
aw. netnata^j nimata- *Stroh, Gras'; phlv. nanmt
V
'Stroh, Gras*^); grober Teppich' (Säy. näääy. II, 101).
1042. numüdmi 'zeigen; erscheinen', Praes. numäy-em,
numüdar, numün^), Dt^'^NDi: (Qiss. Dan.).
ni + i^fnä-; phlv. n(i)mütan 'zeigen, erscheinen',
n(i)mayisn, n(i)mütär,
oss. d. niniäyun, t. njmam 'rechnen, zählen' (176);
sar. si/n. namäy-em 'sich zeigen, erscheinen*.
1048. numed 'hoffnungslos'.
phlv. anömet 'hoffnungslos'; vergl. ötwed, umed
(No. 109).
Der Bedeutung nach eine Doublette zu na-umed.
Die PehlevT-Schreibung D^DIWN, das doch gewiss
nicht anaumet gelesen werden kann, ergiebt wohl
auch für die Suffixendung I^DW die Lesung -ömajid,
^) Vd. 3 (121 J ist besser *auf lauter spitzige Gräser* als *auf'
lauter stachelichte Teppiche' (Geiger, ZDMG. 34, 425).
^) In den Dialekten ist die Praesensbildung auf -ün die alleinige,
vergl. Käs. V. bdnumön (Im^pt.)^ '/..bänemön^ K, ronmötr, ähnlich finden
sich im kauk.-bergjäd. vom Inf. f ermüde der Impt. ferrnün und das
Praes. mi-fermünum gebildet.
```


## [2026-09-07T15:51:38.696Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==103' HRN.txt | head -20; echo \"===== azmudan\"; grep -n \"azmüden\\|äzmüden\\|azmüdan\\|äzmüdan\\|azmäy\\|äzmäy\" HRN.txt | head"
}
```


### [2026-09-07T15:51:40.146Z] TOOL RESULT

```
— 81 —
aw. *paiti' -p l/^mö- ; phlv. patmay^d (AV.), patman,
patmänih^ patmänak 'Mass'.
kurd. piwdn messen; wa/. piHmiHam 'nachahmen,
nachmachen' (?).
)4. peiwesten ^vorbinden', Praes. peitvend-em, peiwend,
aw. "^paiti- 4- \/hnfid' (s. No. 219) ; phlv. patwastan,
patwand Band*.
kurd. pevandn *kleben .
55. plh *Talg, Fett', ^S (Is. 1, 11); vergl. ferhih (No. 813).
ap. ^pi^u-; aw. pitu- 'Speise*; phlv. pxh bezw. pih;
ai. pitü'. Vergl. np. ferbih (No. 813).
aw. pjvah' ^) 'Fett'; ai. pfvas- *Fett, Speck'; kurd. ptü
'Talg (ZDMG. 88, 57); oss. d, ßti, t. fite Tett, Speck'
(289); bei. pT<j, n. pty (298); wa/. j>7/ 'Biestmilch'
dagegen gehören zu paz. j>^y (lies piy) *Fett' (West,
Sik. gura.-Glossar) , das aus *pivaka' entstanden ist
(vergl. Hörn, KZ. 32, 584 No. 17).
T.
)6. tä *bis; damit*.
===== azmudan
650:äzmä, äzmäyis\ li'^NQilN (Is. 7, 12).
653:bei. äzmäyag (LW.), n. äzmainay (23).
20169:äzmäyag 21.
```


## [2026-09-07T15:51:42.290Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '640,660p' HRN.txt; echo \"--- leaf?\"; awk 'NR<=648' HRN.txt | tr -cd '\\f' | wc -c"
}
```


### [2026-09-07T15:51:43.625Z] TOOL RESULT

```
ahmend, azver {äzür),
aw. asi- 'Gier ; phlv. äs, äzmand, äzvar,
19. äzäd *frei', äzöde.
.^^x^^ aw. äzäta- *frei, edel*; phlv. azät, arm. LW. azat,
azatak, vergl. atarrj tXsv&soia sc. napd Ils()(T(ag (Hes.).
kurd. aza *brav, tapfer* (Houtum-Schindler).
20. äzär Xeid*, azärden^ azdris; äzerden^ äzerm^).
aw. a + [/'zar-j azärayeiMi sie peinigen' ; phlv. äzär,
äzartan etc.; ai. [/har- 'zürnen.
21. äzmUden 'erproben, versuchen', Praes. äzwäy-em,
äzmä, äzmäyis\ li'^NQilN (Is. 7, 12).
phlv. özmütan, özmay(i)sn es ist zu versuchen' (vd. 5
(146) GL), 'Versuch' (Men. 60, 14, K 43).
bei. äzmäyag (LW.), n. äzmainay (23).
aw. *a (oder nach dem Pehlevi wohl ava) + uz +
i/'mä'.
^) Np. aver *wahr, Wahrheit*, äverl brauchen nur Pazendworte
zu sein; doch bin ich über Sahn. I, 35 Vers 19 noch nicht im Klaren
{reftäwerl wäre eine sehr bedenkliche Bildung). Etwa: *"Wir müssen als
Köche zum Sah gehen — fürwahr! und dann ein Mittel ersinnen etc. ?
*) Im Pehlevi auch schon in der kaum hierher gehörenden Be-
--- leaf?
27
```


## [2026-09-07T15:51:57.181Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آزمودن\" BQT_v1_pages.txt | head -5; echo \"=== paymudan\"; grep -n \"پیمودن\" BQT_v1_pages.txt | head -5; echo \"=== leaf/pdf tags near\"; grep -c \"\" BQT_v1_pages.txt"
}
```


### [2026-09-07T15:51:57.262Z] TOOL RESULT

```
4157:آزمودن »]زوری » آسان »]سایش »آستانه » آستین » آسودن؛ [سیابان»
7683:۴ ره : آزمایش وآزمودن » درذیل .
7685:ما2۵ < اووالا ۲۳ > رك : آزمودن . ه آزعودی _ ارمتا 217702
=== paymudan
=== leaf/pdf tags near
32486
```


## [2026-09-07T15:51:59.950Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7660,7700p' BQT_v1_pages.txt; echo \"=== markers\"; grep -n \"pdf page\" BQT_v1_pages.txt | head -3"
}
```


### [2026-09-07T15:52:00.020Z] TOOL RESULT

```
پنجره ساخته باشند و از ععب آن وان نگاه
(۱) چب ۲ , چش : آکندن .
آژنگه
کرد . *
] ز هثل » بامیم بروزن پای‌بنده خداوند
حرص داز باشد یمنی حریص وصاحب خواهش »
چهنند بمعنی صاحب وخداوند است . #
| د هون بر وزن واژگون , آزما
و امتحان رااگوینب ۴ ۰
]زر ند - با زای فارسی بر وزن یایند ء
کلی باش که بر روی خشت به نکنند و خشت
دیگر بربالای آنگذارند ‏ وگل و لای‌ته حوض
و جوی را نیز کوبند - و کلابه را هم گفتهاند .
آجیده کردن باشد .
 یتع‎
! ز ثف ین » بروزن‌واخندسن, درمیان
]زر زگ ت‌ بفتح ال وسکون رابع‌وکاف
فارسی , چين و شکنجی را کوین دکه بر روی
و آندام مردم اند خواه از ری و خواه ازروی
بسیاراست ؛ یکی دو مثال که بعض فرهنگها برای آزرنگه با زاه میآورند عن‌بسش شواهد آنرنگه
است و اما معنی خیار سب زکه باين کلمه داده اند پی شك اشتباهی است که ظاهرا تخت صلحب
اداة الفشلاء را دست داده است و مثشاء اشتباه کلمةٌ بادرنگه بوده که برای تعبی وزن آنرنگ دد
سخه ای دیده و آرا معنی‌کلمة آذرنگ صو رکرده است . < لفت نامه 5
۴ ره : آزمایش وآزمودن » درذیل .
ه آزمایش پهلوی صلاوز202ه مرکب از 2 + ۳2 « تب رک ۰۸ صه
ما2۵ < اووالا ۲۳ > رك : آزمودن . ه آزعودی _ ارمتا 217702
م رکب از پیشوند 21 ( < 2ل1 که در پارسی دز» شده) و 118 بمعنی انداز هک فتن ؛ تجربه
کردن » آزما شکردن .
بفیه از صفحةٌ ۳۹
است و در بهلوی نیز 320( بممنی پیری آمده که در ثرهنگهای فارسی هم بمعنی پس
وفرتوت باد شده . فلم ولقب پدر رستم» «زال» و «زر» هر دو از بك ریشه و بيك معتی است ممتی
فرتوت . پس ازرمه بعنی پیر ناشدنی: و فرسوده فا کشتنی و آزدمیدخت لفة یعتی ( دختی ) پیر
نشدنی با دخث همشه جوان « فاب اس ۳۱۷-۳۱۱ ح » ابنکه بسضی آنرا مضفف آزرمین دخت
( دختر شرمگن ) دانته‌اند مبتنی بر فقه ال عامیانه است .
۳ ِِ رك: از غ.رود 5 با زای هوژ بر وزن ساطور »
صاحب حرص و آز را کونند که حریص باشد .
این لفظ م رکب است حمجو گندور و رنجور -
و بممنی هوسناله هم گفته‌اند ؛ و بر وزن داد کر
آمده‌است که ساحب و خداوند حرص و شره
واز باشده چه آز بمعنی حرص است و وربمعنی
صاحب وخداوند . *
=== markers
```


## [2026-09-07T15:52:07.084Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=7683' BQT_v1_pages.txt | tr -cd '\\f' | wc -c; echo \"--- v1 leaves total\"; tr -cd '\\f' < BQT_v1_pages.txt | wc -c"
}
```


### [2026-09-07T15:52:08.977Z] TOOL RESULT

```
247
--- v1 leaves total
776
```


## [2026-09-07T15:52:15.065Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 666 667 668 669 670; do echo \"### leaf $n\"; awk -v k=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==k' BQT_v1_pages.txt | grep -oE \"پیمو[^ ]*|پیمان[^ ]*|بقیه از صفح[^\\n]{0,20}\" | head -5; done"
}
```


## [2026-09-07T15:52:16.268Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT']['scans'],ensure_ascii=False,indent=1))\nprint(d['BQT']['page_offset'])\n\""
}
```


### [2026-09-07T15:52:16.280Z] TOOL RESULT

```
### leaf 666
### leaf 667
### leaf 668
### leaf 669
### leaf 670
پیمان
```


### [2026-09-07T15:52:17.674Z] TOOL RESULT

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
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-09-07T15:52:20.048Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پیمودن\\|پیموذن\\|پیمودذن\" BQT_v1_pages.txt | head; echo \"=== leaf 670 dump\"; awk 'BEGIN{RS=\"\\f\"} NR==671' BQT_v1_pages.txt | head -70"
}
```


### [2026-09-07T15:52:21.501Z] TOOL RESULT

```
=== leaf 670 dump
شطالی باشد .3
ی اد بایای حطی» بروزن وععنی
بیشکار است ت که خادم و خدستکار اک رد
ومزدور وش دست‌باشد ویمصی بیشاب و شاش
هم هست که بمربی بول گویند- و قاروره پیماررا
نیز گفته‌اند وآن شیشه‌ای باشد که بول بیمار را
درآن کنند و پیش طبیب برند » و بممنی آخر
بجای حرف آخر نون هم آمده است
پیشیاده - با ثالی مجپول بر وزن‌هیج
کاره؛ خواتجه وطبقی را گوبند که تعلات 4
در آن کنند و بمجلی آورند ٩‏ .#
بیفاد ه- باغن نقطه‌دار بروزن مخوارد:
طعنه وسرزنش وبهتان را گویند ۴ .
بغا له بر وزن بنگاله» قدح و کاسةٌ
را
هرزه هم آمده اس ۴ ۰
0 غلوش ه
کلی است‌از جنس سوسن و آنرا سوسن آسمان
کون خوانند و بر کنارهای آن خالهای سیاه
وچینهای کوچك افتاده است
دغله- ار وزن زنگله
چ‌
« بالام بروزن نیم جوش »
1 بمعنی کنج
و کوشةٌ خانه باشد - و کنج و كوشة چشم را لیز
گویند. وبمعنی براحه : دز آمده اسن که قض
راه باشد ٩‏ #
لماگنس بروزن هدن , سداب را گونند:
و آنگیاهی باشد دوابی مانند بودنه» و خوردن
11 ِِ_ قوت باه و یت ها و ی آن
۲ اول و ضم ثالث» بروزن
ومعنی پیکو باشد و آن ولامتی‌است مشهور- ونام
بیغان - بکر اول وثانی مجهول‌بروزن
ایمان» ترط و عهد وپیمان راکویند - و بممتی | هر که پادشاه آن ولابت شود ۸ - و بکر اول
ظ,. مصحف پیشپاره (معرب آن فیشفارج) . د: پیش باره .
؟ - اومتا821 1 ۵02 (حندی باستانی82 +۳261 آواز دادن» ملام دادن باسخ
دادن) . بارتي‌لمد صور کر اه این کلمهرا مشتق ازهندی باستان 12۳ +0221 ( 2۶ظ
فک رکردن) دانست. «اسشق ۳۵۸ راد: سفاره.
ی ۵ - مقلوپ : پلنوش (« .م).
٩‏ -همرثْهة بفوله . ۲ - جوالیقی کوید : «فال ابوبکر: الفیجن» السداب. لفة
شامية و لا احسبها عربية صحيحة. قال ابوبکر: و لااعلم للسداب اسماً عربباً لاهل الحجاز ۰ الا ان
اهل الیمن سمونه «الختف». «المعرب ص ٩۲4۲‏ . ۸ - عنوان جبفو باسفر ( که اغلب
بقلط بیغو وپیغونوتثه و خوانده میشود) بحکام خلخ اطلاق شده. ابن خردادبه (س ۱5) کوب د که
ملاطین ترك و تبت وخزر « حافان » خوانده میشوند « باستثنای پادشاه خرلخ که جبفوبه نامیده
میشود .» بقول کاشفری ]11 . ۲۵ یففو عنوانی بود دو درجه یابین‌تر از خاقان . عنوان ,بفو
0 ( کاغنری]]] .2]800:۳6از ۷2۳۵00) را بامد از نام قبلهباغو 72028۳00
تمیزداد. قببلهة اخبر درسمت شرقی‌ثر بن قای وتانار جا داشته‌اند (کاشفری آ .۲۸». برای اطلاعات
بیشتر" رك : : میلورسکی . حور العالم ص ۰۳۸۸
‌ پیشی - از: پیش اد ی (حصدری)؛ سبقت. . نقدم: : بیی گرفتن سیقت جستن؛ میتی
ریسی تقدم و تأخر: «پیدا کردن حال منقدمی ومتأخری که پیشی وپسی بود: پیشی ویسی ۳
بود بابطبع بود بابشرف بود...» «دانشنامه ص ۹۸».
۲ مصحف : یب انه.
بقه درصفحً 140
```


## [2026-09-07T15:52:28.602Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for k in 672 673; do echo \"#### block $k\"; awk -v k=$k 'BEGIN{RS=\"\\f\"} NR==k' BQT_v1_pages.txt | head -70; done"
}
```


### [2026-09-07T15:52:29.904Z] TOOL RESULT

```
#### block 672
وشرط را گونند ۳
لیتا- بکسر اول بر وزن جیفه » چوبی
باشد بوسده در ولابت خوزسنان و آن را دای
ی ۲ بکاربرند بمنی باستگه و چشماق آش
درآن زننه 2
ییگاد ۴ - بنتح اول وکاف فارسی‌بروزن
نی‌زار , جنک وجدال را کویند - و بمعنی قصد
واراده هم هست ۳0
کار بر ستان - کنابه از مردمان
جنگجو باشد . 4
٩‏ بیغو (مرکی), مرغ شکاری‌شبیه بشاهین. «جفتابی۱۸۷. ۴ - همریشة بیفوله. ۴ - رك:
بیغان‌وبیمان . ۴ - بیکار ویرگار » ازاوستابی 0۵016278 ۵» پهلوی024۵ (جنگ),
ارحنی اسف (جنگه) «اسدق ۰۳۹۰ دیب رکه۱ ۰*۱۸ . ۵ ومجازآبممنی جدلوسخن‌بهوده:
بهستیش بابد که خستو شوی ز گفتار پیکار _مکسوشوی. فردوسی طوسی.
«تاحیت سپاهان ومردم‌آن جهانیان را عبرتی تمام‌است» باب که جوایی جزم فاطم دهیدنه
عشوه و یبکار.» تیف ۶ب ٩۲۱‏ ۰
۵ پيك بفتح اول وکاف فارسی باکاف تازی, ازاوستابی ۳20112 ۵ لفة بمعنی پیادم
۱ معرب آن‌فیج .سشق ۳۵۹.
‌ یکان - بفتح اول . اوستایی (9) 0هع + 02161 (180 کندن). ارمنی [مه‌اعم
0 « استق ۲ ۶ , پهلوی 0 « اونوالا ۲ده » ؛ توكك تيز تس و دیزه ح
ین و ستسان:
پرندمایست شکاری از جنس باشه ۱ -و بمنی
یود » بنتح اول و شم ثالث بر وزن
طیفور , دهان تنکه و مرطبان کوچك و امثال
آن را گوبند , وبکسس اولعم درست است .
فیقو له بی وزن زنگوله , بمعنی
پیغله است که کنج و كوشة خانه- وکنج. و كوشة
چشم باشد- و بیراهه رانیژ گویند که نقض راه
رت ۳۹
فیقون ‏ بروزن میمون ؛ عبد و پیمان
بقبه از صفحه 444
۱ ۵ پیشیی - از: پیش + ین (نسبت)؛ مقدم. سایق» قدامی - کهنه عتیق. عم پیشی »
علم الهی و ماجمد الطبیمه : «اما علم نظاری سه گونه است: یکی را علم برین خوانند وعلم پیشین
وعلم آفچه سیبر, طبیمت است خوانند...» « دانشنامه ص ٩٩‏ .
۵ پیغام - بفتح اول. هم‌ریشه وهم محنی پیام «اسشق ص ۸۰ ر: پیلم وپیتام. درزبا کی
00 «کربرسن ۰۹۰ ,کیلکی صفاو(26 .
۵ یغامیر وعخفف آن یغمبر ار بات اب ام بیغام ۳ بر (مخنف
برنده)" دراستی ۳6610171۳26 با 02011۳0۳6۲ « . است ۱۲ » »گیلکی ۳۹
رسول . کبکه پیفام می‌برد یامی‌آورد-. کس یکه ازجاب خدا مأمور هدابت خلق است : «ازهر
اين همی عیراث ماند علم پیغمبر بوصی و از وصی بامام و از اما بحجت » «کنف سپ ۱
سجتاای ص 1۱۵؟.
۵ یخامیری و پیخمبری - م رکب از: ییفامبر (پیغمبر) ۳+ ی ( مصدري )؛ رسالت ؛
یفام بردن- نبوت: «بسیاری پیغمبران‌بمین برشریمت پیغمیزان پیشین بودند وغدتی برآن شریمت
همی کار کردند ؛ وبه پیذامبری رسیدند.» < کشف المحجوب سجسانی ص۷*.
#### block 673
بان. مقراضه
دو شاخ باشد
فیکانی » با کاف بر وزن شبطانی .
نوعی از لعل و فیرءزه باشد ۷ - و جنشی از
توشادر ح‌ هست که برشکل و هبات بان واقم
میئودو نها رالعل پیکانی‌وفيروزة پیکانی ونوشادر
پیکانی گویند .
لیگ ر ۴ - بروزن قیصرقالب وکالبدوجله
و صورت هرچبز را گونند ۲
پیکران در خشی» بکسر دون .
۱۳3 ی را گوشه ‏
ی 16
میان ملك وملکوت .
بیاث رد ایگان» کنابه ازماه است که
قمر باشد - و کنایه از سوداگر - و رامگذ.ی
هم هست- وباد صبارا نیز گویشد .
ی کردن امیك. کنابه از فاامیب
شدن باشد.
بیگرستاتن. ین را 9 وان
باجام از از آن جک محصوي مقداری ّ
وبارواح از آن حیثیت که‌نورانی است وآنرا عالم
مثال نفوی منطیمه وخیال منفصل و ارض حفیقی
خوانند ؟ .
2 44٩ --
پیگر گاو- کنابه از صراحیی باشد
ات کار
بیاك فلاث » کناب ازماه است که فمر
باشك , ۰
یی گم کردن « منم کان فارسی .
کنابه از کاری است که کسی بی‌بمطلب و مقصد
این کس نبرد .
پیکناد » بفتح کاف بروزن پیوند, ماضی_
پیوسن ودر سلك در آوردن باشد «عنی پیومست
و در سلك درا ورد وجمع نمود - و بکر اول
بروزن ربوند مقامی استاز توران زمین ۴ .
ایکندن - بر وژن و حعنی پیوستن
باشد- وبمعنی جمم کردن ودر سك کشیدن هم
همست ۵ .
فی کود کردن- کنابه از بی ندان
شدن امست
بل ای ی فا
جانوری. عمروف باشد -
و بممنی کیسه و خربطه
و گرهاید کته اند .
و ازین است که غدود را
دشتیبل گویند چه دذت
بمعتی زشت و بد و سل
بمعنیگره باشدیعنی گره
زشت و بد» چنانکه در
جای خود آمده است - یل
ز بهر دیدة خصم تو لمل پیکالی.
دحافنا شیرازی ص قکه».
۲ «اسثق ۰۳۹۱ .
۴ - رك : بیکند.
هرآنجه قارون آنرا بعمرها يکند.
رود کی سمرقندی. ۶ جهانگیری؟.
مشتق‌است ست «تفس» . رك: بان برتیا .
```


## [2026-09-07T15:52:38.884Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for k in 674 675 676 677 678; do echo \"#### block $k\"; awk -v k=$k 'BEGIN{RS=\"\\f\"} NR==k' BQT_v1_pages.txt | grep -oE \"\\-\\- ?[۰-۹]+ ?\\-\\-|پیم[^ ]*|بيم[^ ]*|پیمو[^ ]*\" | head -12; done"
}
```


### [2026-09-07T15:52:40.223Z] TOOL RESULT

```
#### block 674
#### block 675
پیمایند
#### block 676
پیمان]
#### block 677
#### block 678
```


## [2026-09-07T15:52:42.227Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==676' BQT_v1_pages.txt | head -80"
}
```


### [2026-09-07T15:52:43.635Z] TOOL RESULT

```
بح
«یینکی» برروزن زیر کی غذودنی باشد
ین ۱ با نون بروزن لموء کشك‌باشد
که دوغ نرش خشك‌شده‌است‌ویعربی اقطوبتر کی
چکده رانیز گونشد که
روغن آ ترا نگرفته باشند ۰
ا۶ ۰
بنو له یپ مسکون‌کاف» سمعنئی بیتواست
که قروت و کشك باشد؟ .
پینو وا با واو بروزن گیسوها ۰ 9
آش است .
لیفه _ « بروزنکینه, پارچه که بر کفش
وجامه وخرقه دوزند- وپوست دست ویا واعضارا
یز گوبند که بسبب کار کردن سخت وسطبر شده
باشد .
بو ِ بقتح اول و تانی بواو کشیده ,
کلوخ را کونند که پارچپای گل خشكث شده‌باشد.
و با ثالث مجهول‌مرضی است که آنرا رشته گویشد
وازاعنای آدمی ۳ هی آ بد.
بو‌ار بروزن شیراز» شیر ه راگوننده
فقروت خوانند - وماست
وآنرا مرغ عیسی خوانند .
یواسته آم بروزن پبراسته . برج قلمه
وحصار -- وفصیل را گویه ,
یوس ه بکر اول و واو مجهول بر
وزن ف-وی, بمعنی انتظلار باشد- وطمم و توقعوا
فلز گویت ۳
لیو ست ع»_بفتح اول بر وزن لی‌بست ۰
ییعنی سوسته است که همیشه ودأیم وهدام باشلس
ویمعنی پیوند هم هست که ماضی پیوسئن وپیود
کردن و الحاق باشد- و باسطلاح .-حنفین‌وسول
سالك است از قید شید بدرجهٌ اطلاق حققت
اسدای ای فان لس ای
شد ۵ .
پیوستگان + مر کباترا گونند همچو
نبات وجماد وحیوان ٩‏ .»
مق ست4 » بروزن برجسته, بمعنی‌هميشه
ودایم باشد - ویمعنی پیوند کرده شده و در عم
پسته ‏ وبلا فاسله هم‌آمده است - و کسی رالیز
کون د که از بیاری کریستن تواند مخن گفتن
وگن کوند گر برمخنش أفد رد
. مازندرانی کتونی
برادران را بوسف چو داد گندم وجو
اگر بناعت مزجاه . پشم و پینو بود
۳ - رشك: سنو .
۴ رژد: سوس.
فرهنگه دساتس .
۵ _ ره :
نبود گندم وجولیر جز تیک
سوزنی‌سمر قندی. #جهانگیری».
1 - <هع پوسته » مر کب این سیط,
ت [ رك : پیمان] ,
نیب رک ۰۱۸۳ ؛ ملحق شدن,
```


## [2026-09-07T15:52:47.909Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==675' BQT_v1_pages.txt | head -90"
}
```


### [2026-09-07T15:52:49.312Z] TOOL RESULT

```
پیل معلق در عوا
یل معلق درد هو کناب اژابیباهد
یی سه بر وزن زیلو ؛چویی .که بدان
مسواگ کنند وعریان اراك خوانند - و بار درخت
ارالك را نز گفته‌اند .
بیلو ) بفتح ثالت بر وژن بینوا ؛ دارو
فروش وعطار باشدا .
پیلو ار ۲ ت بسکون ثالث بروزن‌یشکاره
کتابه ازسیار بسیارباشد .
بو اه - بر وزن‌بیابایه ؛ مرغکی‌است
یله سس با ثانی مجهول بوزن حیله ,
اسل ابرمشم و غوزه ابرشم که کرم تنیده باشد
-رکرم ابرشم رادیز گویند ۴ و مطلقخر یضرا
هم کفته‌اند - ونوعی ا زگیاه ودارو باشد سوچشم
وبلك چشم را نیز بطریق تشبیه میگوبند - وهر
کره را گونند عموما - و گرهیرا کویندخصوسا
که درمیان دتبل بهم میرسد و ا آلرا بر لماور ند
دلیل نيكٌ نمیشود - وچرلك وربمی که‌ازمیان زخم
برمی آ ید وروان میشود - وسحرا و زمین خشك
< 46۵
شده باشد بمنی از دوطرف آن زمین دو رودخانه
میرفته باشد با يك رودخانه در شاخ شود و آن
زمین درمیان درابد - و بمعنی پیکان جر حم
امفط امن
فبله و د - بانانیمجهول بروزن‌تيش هکره
شخصی که دارو واجنای عطاری وسوزن و آبر‌شم
ومهره و امثال ان خانها گرداند وفروشده ِ
بل‌هوالی «کنابه از ابر باشد که
عربان سحاب گویند .
یمان - با میم بروزن کیوان, شرط
وعهد - و خویش وپیوند | گوید.
آداب جهانداری از مه بادکه‌اواين پیغعبرعجمان
9 3
لیها ٩4‏ ح بر وزن میخانه ؛ نلرفی که
بدان چیز ها پیمایند و انرا بعربی قفیز بروژن
مویز گوشد - ۳ قدح شرابخوریران ز گفته‌اند.
بیمانه بر شدن « کنانه ازصرباخر
رسیدن باشد .*
۴ از: پبل + وار(بار) مانند: خروار»
ومشانهةٌ علوی مردند.» «سهقی صس ۱۳۷*.
۴ بهمه شهر بود ازاو آذین
۵ - چو دریته باشد چهداند کسی
در بریشم چو کرم پبله زمن 5
عنصری بلخی. د لت فرس * 4۱-8؟.
که جوهر فروش است ببا پیلمور ؟
سندی . کلتان .٩‏
۷ - ازبرساختدهای‌فرقة آذر کیوان.
«کاف» . حصلهً ارمغان سال۱۲ ش ۸-۷؟ .
(بر هان فاطع۱۱ )
```


## [2026-09-07T15:53:03.506Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for k in 671 672 673 674 675 676 677; do echo -n \"block $k: \"; awk -v k=$k 'BEGIN{RS=\"\\f\"} NR==k' BQT_v1_pages.txt | grep -oE \"[۰-۹]{3}\" | tr '\\n' ' '; echo; done"
}
```


### [2026-09-07T15:53:04.840Z] TOOL RESULT

```
block 671: ۳۵۸ ۰۳۸ 
block 672: ۱۸۷ ۰۳۹ ۳۵۹ ۰۹۰ 
block 673: ۰۳۹ 
block 674: 
block 675: ۱۳۷ 
block 676: ۰۱۸ 
block 677: ۱۹۶ ۳۳۵ ۳۹۵
```


## [2026-09-07T15:53:18.633Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n \"pdf page\" FFD_pages.txt | sed -n '25,35p'; echo \"=== page 25 (pdf 30)\"; awk 'BEGIN{RS=\"\\f\"} /pdf page 30\\]/' FFD_pages.txt | head -60"
}
```


### [2026-09-07T15:53:20.083Z] TOOL RESULT

```
567:[pdf page 25]
592:[pdf page 26]
636:[pdf page 27]
662:[pdf page 28]
666:[pdf page 29]
685:[pdf page 30]
709:[pdf page 31]
735:[pdf page 32]
760:[pdf page 33]
795:[pdf page 34]
819:[pdf page 35]
=== page 25 (pdf 30)
[pdf page 30]
ماده‌های ماضی و مضارع فارسی دری - ا اس ۲۵
8 صورت بالانلرهٌ ريشهٌ 7210 است. ريشةٌ 730 «استراحت کردن» معنی می‌دهد. از
ريشهٌ 1318 «آرمیدن» و «رامیدن» هم آمده‌اند.
۱ آزاردن
آزارد + فارسی میانه 22374 < ایرانی باستان 3-227-12*. 8 پیشوند فعلی است >
آراست. 237 ريشه است به معنی «تحریک کردن» و 12 پسوند است. برای 12 > آراست.
آزار« فارسی میانه 2227 < ایرانی باستان 3-237-0*. برای 2 -> آرای.
«آرّرد»» که امروزه به ضم ز تلفظ می‌شودء» مخفف «آزار» است.
آزدن, آژدن
آزد « ایرانی باستان ۴2-70-18 برای 18 -> آراست. 2 پیشوند فعلی است. 8[ صورت
ضعیف ريشةٌ 8/180 است. 8/188 به معنی «ازدن» است. «آژد» از پهلوی اشکانی وارد
فارسی دری شده است.[ ایرانی باستان در پهلوی اشکانی #ودر فارسی میانه 7 شده
است.
آزن « ایرانی باستان 20[-3*. آژن < پهلوی اشکانی 0ه37* < ایرانی باستان 80[-3*.
آزمودن
آزمود < فارسی میانه ۰320084 02130. صورت اصلی 02804 است از پیشوند فعلی
2 که به فارسی میانه نرسیده و 134 . 8 به قیاس با 8739 8730 به جای 30 آمده
است. صورت ایرانی باستان این ماده 1 - ۳3 - 2* بوده است. ريشه (133)7 به معنی
«اندازه گرفتن» است. برای 1۵ آراست.
آزمای + فارسی میانه 2203 23 < ایرانی باستان 2-ر2-3*. برای 2-> آرای.
آسودن
آسود + فارسی میانه 3800.
آسای + فارسی میانه 3837.
```


## [2026-09-07T15:53:27.695Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && awk 'BEGIN{RS=\"\\f\"} /pdf page 71\\]/' FFD_pages.txt | head -60; echo \"===== search farmudan\"; grep -n \"فرمودن\\|فرمود\" FFD_pages.txt | head"
}
```


### [2026-09-07T15:53:29.156Z] TOOL RESULT

```
[pdf page 71]
و فعلهای فارسی دری
ماده مضارع.
فرست س فارسی میانه 1۳681 ج ایرانی باستان - ها5زه ۳ *: فرستاده. قاقنه۲؟ صفت
[ مفعولی گذشته است از پیشوند فعلی 8 و هاگٌذ: صفت مفعولی گذشته از فا صورت
ضعیف ريشهٌ قَة: «روانه‌شدن ‏ وکردن» و برای پسوند 2 > آراست.
قرشته از 121512-1۵ آمده است.
فرسودن
فرسودن. فرسای در فارمسی دری بسیط است. اما از نظر تاریخی از پیشوند 2 و
«سودن» و «سای) ساخته شده است + سودن.
فرمودن
فرمود « فارسی میانه 1۳۵7004 + 1۳2۵034 < ایرانی باستان 1۳۵-3-12*. برای 12 -> .
آراست. 178 پیشوند فعلی است. 33 ريشه است به معنی «اندازه گرفتن». 1۳۵/14 به‌قیاس
با فعلهایی چون 8737 و ۹۳84 به وجود آمده است. :
فرمای < فارسی میانه 172۵08 < ایرانی باستان ۴1۳۵-3-8 12 نشانه‌ای برده که
برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است.
فروختن
فروخت < فارسی میانه 1۳071 < ایرانی باستان 1۵-0-1۵ *. برای ۵ > آراست. ۲۵
پیشوند فعلی است. 1 صورت اصلی 0 است. ۴ پیش از 1 به # بدل شده است. ۷1
صورت ضعیف ۷۷۵و آن به معنی «گفتن» است. ۱
فروش دج فارسی میانه 1۳05 ج 105 «<ایرانی باستان ۲۳۵-۵55 *. ‎٩‏ برای ساختن
ريشةٌ جدید به کار می‌رفته و 1 پیش از 5 به #بدل شده است.
فرهیختن
فرهیخت + فارسی میانه 1۳80451 < فارسی باستان 0۵-1۵ -1۳۵*. < ایرانی باستان

===== search farmudan
1794:فرمودن
1795:فرمود « فارسی میانه 1۳۵7004 + 1۳2۵034 < ایرانی باستان 1۳۵-3-12*. برای 12 -> .
```


## [2026-09-07T15:53:34.730Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && echo \"=== v4 pdf 39 (printed 1956)\"; awk 'BEGIN{RS=\"\\f\"} /pdf page 39\\]/' BQT_v4_pages.txt | head -50"
}
```


### [2026-09-07T15:53:36.749Z] TOOL RESULT

```
=== v4 pdf 39 (printed 1956)
[pdf page 39]
ماور -۱۹۵۹-
و نای قرشت بروزن آمیزکار»‌ش ی کل راگوبند است که يك حسه ازدوازده حسةٌ سال‌باشد » وآن
که بمد از عقل کل است . گاهی سی روز وکاهی بیست ونه روز میباشد ؛

هاود - بح واو بروزن باور . مشنف | « بودت آفتاب را نیز کوبند در يك برج - ونم

میاور است که منم از آوردن باشد ‎٩‏ - روزدوازدهم بود ازهرماه شمسی - ونام فرشته‌ای

هاه - پروزن شاه ۰ بممتی‌بیر اسفرات | هم هت که موکل است برجرم قمر یمتی‌فرس

که عربان قمر خواشد ۴ - و ترجمةٌ شهر هم ماه و تدیین و مصالح روز ماه که روز دوازدهم

هت وآن از دیدن علالی: تا دیدن هلال دیگی | بود از ماه شمسی باو تعلق دارد - و بزبان
۹ - رك :آوردن . ۴ سمانگه (ه.م.) ورك: ماس, ماج. دراوستا وپارسی‌باستان

و۸۳ . سانکریت 3328 (ماء» قمس)» کردی 3360 ( قمر؛ شهر [عریی] ) «ژاباس ۰۴4۰۹
ماه در ابران باستان . علاوه بر اطلاق اد رم ۱
بجرم قمر» بفرشته‌ای ( ایزدکرة هاء) و و و ی رش چا

لاه یس راراد خر کی ی
ستوده ومورد تعظیم وتکریم بوده‌است. ِ ! رخوهس تا وم و
چه در شب تار در برایر تاریکی: که رس سس ماد
جهانر! درپردة تیره پیچیده » دیدگان پل رگ ۵
آدمی‌را از دیدار محروم میدارد , ماه وخ ان ات بت
یگانه جراغ آسای است که برد ی 0
غلمت را دریده راز نهای منرت اوه ی
را فاش میکند . درتیربشت( بشت۸ ) و
بند۱ومهربشت بنده ۱۸ وغیرهمخصوضاً ور و ید
ماه مورد تعظیم قرارگرفته‌است . غالباً ۵ اد و ۳ ۳
:ماه تشکیل دهندغ تخمه .و تژادستوران شتاه‌دو
غناخته شده است ( نا ۱ بند ۰۱۱ ات 2 3
سنا ‎۱٩‏ بند ۸ وغیره ) ونیز دراوستا
عربی گیاه و رستنی خوانده شده ( ماء حالات مختلف ماه
بشت باد 4 ) - رو دوازدهم. هر ماه را بمناسبت تقدیس اسم ماه و فرشتةٌ انگهبان او بدین دام
خوآنده اند » ویبرونی در فهرست روز های ابرانی این روز را « ماه > و در سغدی « ماخ > و در
خوارزمی « ماه » با دکرده . زرتشتیان نیز این روز را ۸ ماه » خواشد :

ماه روز ای بروی خوب چو ماه باده لمل معکبوی بضواه
گت روشن چوماه بزم که کشت نام این روز ماه وروی تو ماه.
* مود سعد ص۹۹۲

هایکه ( ماه ) در اوستا هم بمعتی ساره معروف است و هم امم مدت سی‌روزست که قمردر ۱۹
روز ازآن در افزایش است :و۱۵ روز درکاهش (کاتها , بسنا 44 بند ۳ ) ورك : روز شماری بقلم
نگارندء م۷۹۳۳ ؛ اسشق ۹۹۸ # بمعنی شهرعریی ( سی‌روز ) درپهلوی د[528 : 18808
اوتوالا 6۱۳ >.
```


## [2026-09-07T15:53:42.745Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for p in 40 41 42; do echo \"=== v4 pdf $p\"; awk -v P=\"pdf page $p]\" 'BEGIN{RS=\"\\f\"} index($0,P)' BQT_v4_pages.txt | grep -oE \"مهتاب[^ ]*|ماهتاب[^ ]*|\\-[۰-۹]+\\-\" | head -8; done"
}
```


### [2026-09-07T15:53:44.016Z] TOOL RESULT

```
=== v4 pdf 40
-۱۹۵۷-
=== v4 pdf 41
-۱۹۱۸-
ماهتاب
مهتاب
مهتاب
=== v4 pdf 42
-۱۹۵۹-
```


## [2026-09-07T15:53:46.702Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk -v P=\"pdf page 41]\" 'BEGIN{RS=\"\\f\"} index($0,P)' BQT_v4_pages.txt | grep -n -B3 -A6 \"مهتاب\" | head -40"
}
```


### [2026-09-07T15:53:48.322Z] TOOL RESULT

```
17-و مدور و صیقل زده از طلا ونقره و اغیره ۴ - ماهر وزه ۸ - بکون ثالك بروزن
18-وسوزلیرالیز کوبند که‌بربك سرآن کلوله‌ای‌باشد | چارروزه » بمعنی سال مه باشد که بعریی تازیخ
19-() خم۱: میباشد . () جك : ژند ویاژند .
20:#مهتاب ( مخفف ) از : ماه (ه.م )۳ تاب ( کرمی » نو ) لغة بممتی لور ماه
21-و مجازاً جرم ماه :
22:ا زکوتهی بخت ندارم امید ‏ که بوبرانةٌ من پرتومهتاب افند . سائب‌تبرنزی «فرهنگه نظام» -
23-۴ - ماهچه , شکل علالی بود که بر سر علمها و چنرهای پادشاهان سلجوقی و امرای
24-دیگر ترك بعد آزایشان منصوب بوده . ذکر ماء علم وماهچهٌ چتر در اشعار شعرای معاصرسلاجقه
25-و ,خوارزمشاهیان بسیار د,ده میشود. خاقانی در مدح علاءالداین تکش خوارزمشا هگوید :
26-ماهچهٌ چتر او قامةٌ کردون کشاد مورچة تیغ او ملك ملیما ن کرفت.
27-رك : مجلهٌ ایران امروز ۱۰:۲ , چند فابدة ادبی بقلم آقای عبای اقبال ؛ ورك : مهچه -
28-۴ عمانه (و.م.) ماه (.م.) ۴ ماه خرکاهی « بهاز عجم > 8 اهز .
```


## [2026-09-07T15:53:54.133Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for p in 253 254 255; do echo \"=== v4 pdf $p\"; awk -v P=\"pdf page $p]\" 'BEGIN{RS=\"\\f\"} index($0,P)' BQT_v4_pages.txt | grep -oE \"\\-[۰-۹]+\\-|نمودن|نمود[^ ]*|نمای[^ ]*\" | head -10; done"
}
```


### [2026-09-07T15:53:55.516Z] TOOL RESULT

```
=== v4 pdf 253
نمودار
نمودن)
=== v4 pdf 254
-۹۱۷۱-
نمایان
نموداری
نمودن»
نموده
نموداز
نمودار
نمودنی
نمایش
نمودار
=== v4 pdf 255
نموده
نمودن
نمودن
```


## [2026-09-07T15:53:57.984Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk -v P=\"pdf page 254]\" 'BEGIN{RS=\"\\f\"} index($0,P)' BQT_v4_pages.txt | grep -n -A3 -B3 \"نمودن\" | head -50"
}
```


### [2026-09-07T15:53:59.258Z] TOOL RESULT

```
12-۲ - و نیزنونه , مقدارکم ازچیز ی که دال بربسیار باشد -
13-ی نموعك « جهانگیری» « محیط اعظم > رك : موعك .
14-۴ س تمونك (هم.) 8 - مصحف « تبو4 > (ه.م.)
15:‎٩‏ از : نمون ( از «نمودن» » قس : نمونش [ اسم مصدر بقلم انگارنده ی ۳۲-۳۱])
16-
17-+ ( پوند سبت وانصاف)؛ معرب‌آن نیز «نمونه» «دزی اج ۲ص ۲:۷۳۷. کردی 2672086
18-
--
33-‏عبدالقادر ۸/۲۹۰۷ ؛ فولری ]1 . ص ۱۳۵۲ . معنی اخیر بنظر میرسد که باگروه لغات سغدی
34-
35-بقیه ور حاشيةٌ صفحٌ بعد
36:نمودنی - لغة و در لهجةٌ مرکزی یکسر اول (نیز جشم وقتح اول تلفظ شود) وفتح -
37-چهارم ؛ از : نمو + دن ( پوند مصدری ) « دارمتر . تتبعات اج اص ۱۹۷ ۰ ۲۸۳ ۰ پپلوی
38-
39-2 > ایرانی‌باستان.-(9) ۳122 83 ( جزو اول پیشوند بمعنی فرودء پایین ؛ وجزو دوم
--
41-استی 23832708 , 8180218 ( حاب کردن » شمردن ) » سربکلی » شغنی 670-/[881738
42-( نمودار شدن , ظاهرشدن) «اسشق ۱۰۸۷ > ؛ نشان دادن » اظهار کردن , اراله دادن +
43-
44:صالح وطالح متاع خوبش نمودند تا که قبول افتد وکه در نظرآید؟
45-« حافظ غیرازی ص ۹۵۹۷ ۰
46-
47--کردن : احان نماید وننید منت منت نهاد هر که نمود احان .
```


## [2026-09-07T15:54:06.315Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for p in 262 263 264; do echo \"=== v3 pdf $p\"; awk -v P=\"pdf page $p]\" 'BEGIN{RS=\"\\f\"} index($0,P)' BQT_v3_pages.txt | grep -oE \"\\-[۰-۹]+\\-|فرمان[^ ]*|فرمود[^ ]*\" | head -10; done"
}
```


### [2026-09-07T15:54:07.733Z] TOOL RESULT

```
=== v3 pdf 262
فرمان۳-روا
فرمودن
فرمان
فرمان
=== v3 pdf 263
فرمودی
فرماندار
فرمود
=== v3 pdf 264
```


## [2026-09-07T15:54:10.252Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk -v P=\"pdf page 262]\" 'BEGIN{RS=\"\\f\"} index($0,P)' BQT_v3_pages.txt | grep -n -B2 -A6 \"فرمان\" | head -60"
}
```


### [2026-09-07T15:54:11.558Z] TOOL RESULT

```
59-
60-‏رفت برون میر رسیده فرم
61:۴ - از: فرمان۳-روا (هم) .
62-
63-‏پخچ شده بوق و دریده علم.»
64-۵ _ مخطف «ذاربومد © و «فربومد > (ختح‌اول)
65-
66-‎. ۳۳۹ ‏فری‎ cal?
67-
--
83-‎Oo‏ قرمای - ‎ch‏ اول ء اسم از « فرمودن » ؛ پهلوی ۳81080] ( امر )ءایرائی‌باستان
84-3 -« بارتولمه ۹۸۸ » < پب رکه ۷۷ > ارمنی ع ‎braman‏ « اسشق- هوبشمان۸۲»»
85:آورامانی 9870080 « رك . اورامان ۱۲۲ » معرب ‎oT‏ « فرمان » و جمع عربی «فرامین»#حکم
86-‎ply‏ ؛ حکم ی که از جالب شخصی بزرکه صادرگردد:
87-
88-‏مهتری در قبول فرماست
89-- توقیم ‎lak‏ - پرواله .
90-
91:‏ترك فرمان دلیل حرمانست.
92-
93-‎ta ‏«کلتان‎
94-
95-
```


## [2026-09-07T15:54:19.985Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^mē-\\|^me-\\|MEASURE\\|mēns-\\|menot\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T15:54:20.043Z] TOOL RESULT

```
730:tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek Aulé, wood, matter) substance, stuff, matter: MATERIAL, MATTER. 5. Greek compound Démétér, name of the goddess of produce, especially cereal crops (dé-, possibly meaning “earth”): DEMETER. [Pok. mdter- 700.] math-. Worm. With uncertain preform, but clearly re- lated, is Old English moththe, moth: motu. [Pok. 1. math- 700.] [Mawort-. Name of an Italic deity who became the god of war at Rome (and also had agricultural attributes), hence also the name of the planet Mars (doubtless from its red color, the color of blood). Latin Mars (stem Mart-), Mars: MARCH, MARS, MARTIAL, MARTIAN.] mazdo-. Pole, rod, mast. Germanic *mastaz in Old Eng- lish mest, mast: MAST}. [Pok. mazdo-s 701.] me-1. Oblique form of the personal pronoun of the first person singular. For the nominative see eg. 1. Germanic *mé- in Old English mé (dative and accusative): ME, MYSELF. 2. Possessive adjective “mei-no- in Germanic *min- in: a. Old English min, my: MINE?, My; b. Middle Dutch mijn, my: MYNHEER. [Pok. 1. me- 702.] me-2, In the middle of. 1. Suffixed form *me-dhi in Germanic *mid- in Old English mid, among, with: MID- WIFE. 2. Suffixed form *me-ta in Greek meta, between, with, beside, after: META-. See also medhyo-. [Pok. 2. me- 702.] mé-1, Expressing certain qualities of mind. Contracted from *meo-. 1. Suffixed o-grade form *mé6-to- in Ger- manic *méthaz in (i) Old English méd, mind, disposition: MooD! (ii) Old High German muot, mind, spirit, in German Gemiit, spirit, feelings, temperament: GEMUT- LICH, GEMUTLICHKEIT. 2. Perhaps Latin més (< *mé-s-), wont, humor, manner, custom: MORAL, (MORALE), MORES, MOROSE. [Pok. 5. mé- 704.] m6-2, To measure. Contracted from *meo-. I. Basic form mé-. 1. Suffixed form *mé-lo- in Germanic *mélaz in Old English m#l, “measure, mark, appointed time, time for eating, meal”: MEAL?; PIECEMEAL. 2. Suffixed form *mé-ti- in Latin métiri, to measure: MEASURE, (MEN- SURAL); (COMMENSURATE), DIMENSION, IMMENSE. 3. Possibly Greek metron, measure, rule, length, propor- tion, poetic meter (but this is referred by some to med-): METER!, METER?, (METER?), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRO- NOME. 4, Suffixed form *mé-trd- in Sanskrit mdtrd, a measure: MAHOUT. II. Extended and suffixed forms *mén-, *mén-en-, *mén-s-, *mén-dt-, moon, month (an ancient and universal unit of time measured by the moon). 1. Germanic *ménén- in Old English ména, moon: Moon; (Monpay). 2. Germanic *ménéth- in Old English ménath, month: MONTH. 3. Greek mén, méné, month: AMENORRHEA, CATAMENIA, DYSMENORRHEA, (MENARCHE), MENISCUS, MENOPAUSE. 4. Latin ménsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMES- TRIAL, SEMESTER, TRIMESTER. [Pok. 3. mé- 703, ménot- 731. fen Big. Contracted from *meo-. 1. Suffixed (compara- tive) form *mé-is- in Germanic *maiz6n- in Old English mara, greater, and madre (adverb), more: MORE. 2. Suf- fixed (superlative) form *mé-isto- in Germanic *maista- in Old English m&st, most: Most. 3. Suffixed o-grade
1839:MEAN3 = medhyo- MEASLES smé- MEASURE mé-2
```


## [2026-09-07T15:54:41.257Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD\"; grep -nE \"^m(a|ā)h|^framā|^framu|^nimū|^nimu|^paymū|^patmā|^ōzmū|^ozmū|^uzmū|^māh\" PHD.txt | head -20; echo \"=== PHD_mackenzie\"; grep -nE \"^māh|^framān|^framūdan|^nimūdan|^paymūdan|^ōzmūdan\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-07T15:54:41.323Z] TOOL RESULT

```
=== PHD
441:mah [B YRH < А b-yrh;mh| = М, N ~] moon, month; cal. 12th day.
442:mahig [m’hyk' | M m'hyg, N mahi] fish; astr. Pisces.
443:māhīgān [BYRH-, m'hykEn! | M whyg’n, N māhiyān] month.
444:mahist [msst!, mhst! | M mhyst, N ~] greatest. makóg [mkwk' | M mkwg, N mako(k)] boat. mālīdan [m’lytn' | N ~] = muštan.
4672:framāy-
4674:framān framādār framēš
4896:mah māhīgān māhīg mayān mayanag mayānjīgīh mayānjīg mehmānīh mehmān māzdēsn māyišn zan-!
=== PHD_mackenzie
```


## [2026-09-07T15:54:45.337Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"framūdan\\|framān \\|framān\\[\\|nimūdan\\|paymūdan\\|patmūdan\\|ōzmūdan\\|uzmūdan\\|patmān\\|paymān\" PHD.txt | head -20"
}
```


### [2026-09-07T15:54:45.395Z] TOOL RESULT

```
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
2381:immoderate apaymān; у. deficiency.
2835:moderate paymānīg.
2836:moderation paymān(īgīh).
3258:proportion paymānag.
3642:show nimūdan.
4602:paymānag paui paymog paymoz- paymozan paymüdan padisay padist padiš
4615:pattügih pattüg paywastan paywastag pattüdan pahikar 1-2pahikar- pahikardan pahikāf- pahikāftan pahikob- pahikoftan pahikar pahikaf- pahikafián pahikaftan payrastan payrog pahrmāh- pahrmāhāgīh pahrmāhišn paymāy- paymānīgīh paymānīg
4674:framān framādār framēš
5057:kār- wing! *kār-ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd
```


## [2026-09-07T15:54:52.397Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"nimūdan[^|]\\{0,60\\}\\|nimāy-[^|]\\{0,40\\}\\|ōzmūdan[^|]\\{0,60\\}\\|uzmūdan[^|]\\{0,60\\}\" PHD.txt | head -10; echo \"=== NYB\"; grep -n \"nimūtan\\|nimūdan\\|paymūtan\\|framūtan\\|ōzmūtan\\|uzmūtan\\|māh \" NYB_vol2_glossary.txt | head -12"
}
```


### [2026-09-07T15:54:54.396Z] TOOL RESULT

```
514:nimāy- [nmwtn', nmd- 
3642:nimūdan.
5164:nimāy- -AAG A namāz °з^6 \ wimēhgen 1 5^6 nimü
=== NYB
262:aeürénitan [>c*lynytn'] to make ineffec- tive: bé acdrénét (sc. your work) with the explanation akartārēh-ic 6 šmāh dahét he will create ineffectiveness for you, he will make your work inefficacious 45?. — Den. of a-cär, v. car. V.s.v. axtäyisneh.
356:a-kartaréh [’krt’lyh] inactivity: šmāh dahēt gl. to bē acārēnēt (g. v.) 45?. — V. kartār, kartàreh.
746:āšnavišnēh [ŠMHn-šnyh] det. v.n. in compounds: pas hac én gobišn ~ after having heard this speech 518, with the gl. ka šmāh én gobišn āšnūt; pat han gobišn ~ 5119, with the gl. ka ētšān han gobišn āšnūt būt. — Paz. šnavašni (SGV, Mx).
772:ätur-söc [twrswc'] setting fire to, igniting; an [ZK] šmāh hat ~ another shall set fire to you [O plants!] 951-2, with the gl. ka-š apar nihend à frac girät when one puts [them, viz. the plants] on it (viz. the fire) it shall envelop [them]. — V. sóxtan.
835:reluctancy: atün hàn i kart (v. ?kartan) ~ dahét he will create unwillingness with regard to what you have instituted 45), with the following gl. explaining ~: kū šmāh xvēš rād ne tuvān zuästan, kas šmāh rād ne xvāhēt ‘~ means that you are incapable of an act of will for your own sake and nobody will be willing (to act) for your benefit’ (you will be diffident and inefficient, and nobody will work for you) 45*3; the gist of Yam's speech is expressed in the gl. 452, v. acārēnītam.
878:bag [bg, bk'; inser. bgy, Prs RHY”, Prth ’LH?] 1. god 381! [bk', a quotation from Y. 1019]; pl. eas. obl. —-an [bg?n!] 75! (opp. dēvān). 1131?; garān —-än kof the mountain of the mountain gods 20? (v. s. v. gar). — 2. lord: Ohurmazd ~O. the Lord, of the supreme god 211’. 2224; — of kings: Käyös ~ 458; ~ Päpak HajA:4. B:4. SPrs:8. Prth:8; ~ Artaz- šahr HajA:3. B:3. SPrs:6. Prth:6; 1091, 111%; ~ Sähpuhr HajA:1. B:1. SPrs:4. 11. Prth:4. 6. 8. P1:1. P2:9; ~ Ohurmazd P1:3; ~ Xēsrēi 10921; pitar ~ P1:10; — pl. cas. obl. —-än [SRHY?-n, bg'n'] as a pl. majestatis: öisän —-ān Šahpuhrv P 2:8, without the king's name Pl:4; šmāh ~-dn addressing the king
972:the v. n. and the pt.: bé tacét, bé tacitan, bé tacióneh (e.g. 564); be šutan to go away, to disappear, bē šutak gone, van- ished 5?; etc. — b) denoting the per- fective aspect of the act, viz. that it comes to an end, or has its limit: with the pret. it gives it the sense of an act completed in the past, as in French the passé défini or in Lat. the perfectum historicum; with the pres. it denotes the completion of the aet in the future (Milr. has no special future tense); it is very often put before an imp., giving the order a peremptory force; also used in other expressions implying an act of will, cf apdyistan and framūtan; in this sense it does not stand together with an inf., or with a pt., nor with a negation, nor with other preverbs (which themselves give a_ perfective sense): be bavét he will be, but nē bavēt he will not be. The functions a) and b) are often difficult to keep apart. — 3. prep. a) except, but: hec zvandak apdc bà nē mānēt be hàn i ēvak Arjāsp no one but A. alone 2926-27; 2415-16; 964; cärak be man an kas xYāstan nē tuvān it is not possible to request a means from any other than me 34?; followed by a sub- ordinate clause: nisem nē vindät bē ka
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
1754:expressed (nominal sentence as in the Semitic languages): man Sähpuhr hom 154; tē ke he? 737; to rād ke Dugdav he 4721. en rētak ke hast? who is this boy? 1617; Artaxsér ... nē pat giyāk hast 6?" sq.; kë zan-& hac õi hucihrtar nest ‘qua pulchrior non est mulier', who is the most beautiful of all women 259-19; ēzšān amüh hem ke ... we are of those who 5723-24, šmāh ke xtēn het 6111; sagr hend 86%, — 3. in the 3d p., together with a subst. virtually in dat., or with a pron. in cas. obl., it expresses ‘to possess’ xdnak i-t hast the house that belongs to thee 5325-26; fradandan i-5 hast the chil- dren he has 142; with ràd as in NP: Papak rüd pus-é hast 3?. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions, e. g. han- dešitar vicītār hom 125; frēftār hah 3419; matür hom 46’; kartar hom 101?’; brihenäk hend 7777; ke (cas. obl.) vitīrišn nest which is incorruptible 66°; tö hän-ic äkäh he this thou knowest 399; hayyär hend they help 106%; -š hayyaréh hénd they help him 1001-12; pat kamēstārēh + spihr hénd they offer resistance to the. Sphere 8721; ké (cas. obl.) Mihr u Mah pat pust hah which M. and M. protect 317-8, ete. — 5. auxiliary vb. forming compound tenses: būt hom, būt hend I was, they were, eto., v. Grammar; notice: HWH-nd, regularly hend, must stand for the subju. händ 14? (fut.). 335 (cond.). — 6. Wrong use of the ideogr. HWH-: a) HWH-wm for the encl. pron. lst p. sg., added to the pret. pass. in order to emphasize the agent-
1760:4. partitive: hac fradandan + han mart kasé anyone of the children of that man 25; hac šmāh xiönän ke hast ke ...? 25” ete.; fratom hac ax" i astomand 53%; xuastom hac z"arisnàn the most delicious of dishes 7413; ete. — 5. in comparison ‘than’: hac apārīk kanicakän āžarmīktar 422; Zarristan ke... zan-ē hac či hucihr- tar nest 259-19; hac tē veh 411; kū-š suk mas būt hac apdrik gāv 492°; more emphatically yuvattar (g. v.) hac hàn + huhömikän homtar 40°’. — 6. causative: hac hàn dušxvār sahist by this he was very much shocked 4?-?; hac hàn 1 devan sārēnišn 3774-25 : causal conj. : hac hàn cigon because 4511; hac han i with a nominal clause 48!. — 7. forming adverbs: hac pas, hac pes, hac be, hac apar (hacapar), hacadar; prepositions: pas hac, peš hac (= patiš hac 368), yuvat hac, bé hac; frame prepositions: hac. . . rād owing to 1525-26; hac .. . bérén 20%; hac . . . yuvatāk 76°. — Av. (1746 sqq.) hacé; OP haca; MPrth ^c, "Z; MPrs 'c, "z; Paz. ez (eži-ca); NP az.
1878:handäcak [hnd’ck'] measure; ~ nimūtan to measure 1109. — From handāxtan (g. v.); NP andäzah; Talm. lw. hndz? ‘calcu- lation’; Syr. lw. handäzä ‘that. which is measured'.
2081:Hušētarmāh [hwšytlm”h] the second ap- ocalyptic son of Zartuxšt who will appear after Hušētar: 7114, 988-14.16, 999. 11017. — Paz. Huseöarmäh; from Av. (384) Uz- šyat.nomah-, cf the spelling ?wšytnms DkM 44! (-ms inverse spelling of -mah).
```


## [2026-09-07T15:55:02.728Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"paiti\\.mā\\|paitima\\|uz\\.mā\\|uzma\\|ni\\.mā\\|nima-\\|1136\\|1138\" BRT.txt | head -20; echo \"=== search mah- moon\"; grep -n \"māh-\\|'Mond'\\|Mond, Monat\" BRT.txt | head -20"
}
```


### [2026-09-07T15:55:02.797Z] TOOL RESULT

```
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
8665:•  p.  uzma-  Adj.  'was  ausserhalb,  über der  Erde  gelegen  ist"^  nur  LS.  uzmayä  in der  Verbindung  mit  patiy  ^kar-,  euphero. sva. 'kreuzigen  (lassen)' ";.jr'iZ(Äi«/«SOTiyi?- patiy  akurtavam  Bh.j.8;  2.13,  14,  J.  14.
9153:—  yai  nurm  yas'/ö  kprj/iam/ii  Yt  /j. 56  (?)""  ^)  I  mit  pa/iy  und  Lok.:  afa- dasis  usmayiipatiy  (sd.)  akuiui7<am  Bh. 3-  8;  2.  13,  14;  —  uzmayäpatiy  (sd.) *akariy,^tii"^  Bh._J.141.  7)  mit  äi  und Akk.:  yat  .  .  an.lpm  (sd,)  äi  sp3m\ kpr^naoiti  V.  j.  4;  4,  b)  'Jemanden, (AkL)  wegschaffen,  wegbringen,  losbringen  | von  — ',  mit  kaca  und  Abi.:  ku^a  hiS\ az?m  kfr?naväni  hala  avatihät  drujal V. /p.  la.  4)  'Jemandem  (Dat,  Gea, Lolc)  etwas  machen,  schaffen,  verschaffen
13867:759  Muzmanah-  —  dsbffz-  760
14118:verwendet  V.5. 62,  wo  drvantll);  —  al<A- xsä^rSng  dus^^adkatong  dusvalanM  dui- daHiitig  *duzmanargks  'gvots  (AP.)  Y.  4g. ii\  43- ^Si  45- T,  —  *°g^sj3Öyö  V. 30.11, 31.  14.  b)  im  jAwr.:  yat  aiava  para.- irüiyaH  .  .  tüirlm  gäma  frabarat  yB  nars alaonS  urva  anayragsna  raocBhva  nidmäl .  .  yai  'vä  ava.^mirytie  .  .  tairim  gäma frabarat  yS  nari  "vatö  urva  anayralt'va timBhva  nidalat  H.  2.  1,  15  und  19,  33; 25,  26;  —  a  dim  aoxia  p)r?sö  pourvB aiava  para.irt^yl!  iä^a  asäum  para.- irtiyS  kaka  asäum  apa.jasS  .  .  ä  dim aoxta  ptnsö  pourvB  °vS  (statt  NS.)  ava.- m^rpts  ia%a  'v5  (ys.)ava.*miryarjÄa  iaha <frM/ö(Sp.  781  m.)  apc/assU.  2.  16  und  34; —  :^ar3hanqm  hl  ^baratqm  sarpmayehi tat  näiriiayäi  .  .  asaonyai  :^ar3k>in  .  . 3?ar»kanqm  hl  ^bantqm  (sd.)  viSayäatla . .  tat  Jahikayai  . .  'vattyäi  ^ariinn  H. 2.18  und  36;  —  'vä  V.Ä6,  Vr.22.z;  — 'vaniim  Y.Ä  5,  YL/.28';  —  'vaiU  V.ig. 29;  —  'vataica  Yt.ro.  a;  —  'vatat  \t. 10.2;  —  'vatq»i'V.iS.'j6,  ig.30,'Vt3.4, 4.4,  II. 4.  2)  sonst;  a)  im  gAw.:  hyat akSyä  (sd.)  'guaitl  uitä  yS  ai'^m  dädre Y.5/.8''; — yascä  dS^Png 'gvatS  dadät"
19777:1138
19841:1136
19881:1138
20909:1225  ya-nB  —  ya- Schluss  1136
23344:'tsm  manS  (Sp.  11380.)  Y.J7.7.  a)mit Dat  oder  Gen.  'für  -':  agn/ta  (sd.)  vacä sSnghamahX  aiibyö  .  .  atcil  a^byö  'ta Worte  . .  denen  sehr  genehm  . ."  Y.
26975:—  s.  noch  Y.  28. 1 ,  47. 1  bei  3.  2)  von Menschen;  yS  nh  pnsBs  savanhs  pa%ff slseii  (sd,) . .  ar)drS  %wltvqs  (sd.)  huzPntus» •ts  mazda  Y.  4j.  3;  —  fivB  «r  afa  'iJ irixbm  ..harS(sA)  mainyü  *aAamMs  (sd.} urva'hB  Y.44.2J'; —  asa.,yekyä  hlisäui (sd)  na  °tll'^.48.T,  —  ärmatSiS  nä  'tö hvs  .  .  as>m  spSnvat  (sd.)  Y.  5/.  2 1 ;  — . .  *mainySu{cS  *vanhSt^  . .  data  'toÄyS^a taris  iyaohanä  yehyä  urvä  alä  haiaiti (sd.)  pairigttiki  {%A^  Y.J4.2«;  —  dazu auch;  saosyants  dfng  {Sp.  684  m.)  patsis °ta  dalna  urvalis .."V. 45.11.  3)  sonst, von  Mainyav  (Sp.  1136  u.):  'tä  mainyü rahistäcü  manat?/ta  , .  syao%anaca  7'aeari~ kilc3  Y.  47. 1 ;  —  *mainyJul .  .  'tahya  .  . ^yaoiana  Y.  2S.  1*';  —  von  ärmatay-'" (Sp.  335  u.):  'fam  v!  armaitlm  var>uhTm vanmaidl  (Sp.  1*361  u.)  Y.32.  2.  b)  im jAw.  (und  YHapt.);  i)  von  Gottheiten; a)  von.^y?;jA7>''HStvcrz,Sp.  336  u.):  °tqm armaitlm   vatiuhim    Virmi  Y.  J2.  2;usw,;
26976:—  'ta  (Nom.,  auch  als  Vok.;  so  auch SrB._5  zu  lesen*'),  °taya,  'tayäi,  'tarit (so  auch  YL7.  21  zu  lesen)".  b)  mit mainyav-  (Stverz.  Sp.  1138  u.):  avanayeni "tim  maiiiyBm  . .  uspatayeni  anrim  tnatn- yUm  Yt.  ip.  44;  usw.  —  'tD,  °tasca,  'täi, °tahe  ".  c)  mit  airaia-^  (Stverz.  Sp. 1450.);  a)  'mYHapt.:  as»m  at  vahist^m.. hyai  °t>m  am>hm  Y.3y.  4 ;  —  'tJng  am^sSng yavaijyd  yavalsvs  Y.^jp.  3.  ß)  sonst: amilatibyS  'ta^byU  Vr.  II.  i ;  usw.  —  'tsm; Ha,  °ta,  °tq,  'ff,  'tanqm  — .  d)  von andern  Gottheiten:  'tpm  aAurim  masdqm . .  *'t}^'>  amisS  spmtS  yazamaide  Vr.  ig.  i ;
29472:naisim  vamavätaiy  duruxlam  (Sp.  767  m.)  mainySui  dSmqn  yat  ir/(APn.)  , .  anaä-ä- *maniyitaiy  Bh.  4. 8;  —  äh^ind' ..  *a>ia-  maide  Vt.  12. 4.  «)  Der  Begriff  auf  den ya/ä  abiy  mim  adamsim  avajaimm  Bh.  j  sich  h'  zurUckbezieht,  ist  zuvor  nicht  ge- /.  17;  ^-gaumäiam  .  .  kärJ' Hm . . atarsd'inxaoX,  aber  aus  der  Sachlage  eikenntlicb: EL  /.  13;  —  aniyaf'  apiyä  *äkyata  api- ,  mt^rfm  . .  yd  dai^hSus  rqxsyqihyi  para litn^''  paräbari^  Bh.  i.  19;  —  rtäV-  rausta  baraili  .  .  avar»%i  hls  (APm., taxmam  agariayi^ .  ■  duvarayätnaiy  basti/'  1  näml.  regionis  incolas)  fl/iwKCtCSp.  140710.) adilriy  haruvt^sim  kär^  avaifia*  pasä-  Ytio.i-j;  —  »oÄT/*^»'Sa  . .  jfl/{Sp.  1581  u.) va''iiin  arbairäyä  uzmayapatiy  akutMvam  yaia    Alm  (ASn,   'es')*'   ädar?    mafyäka
29477:/(APm.)  uzmayäpatiy  aiuna: j.Z.  b)  im  gAw.:  kdkiS  a/ili  dntpin dyqm  zastayö[%A.y^ nJ hlm{hSsi) mfrqidyai (Sp.  1083  C)  Y.44.1^;  —  kd^il  .'.  gqm i/as^it  yS  hJm^  ahmäi  .  .  stdi  myst  (Sp.
=== search mah- moon
20338:•  j.,  g.,  p.  mah'  m.  i)  'Mond',  auch  als Gottheit*':  avat  hvan  .  .  käu  ma  .  .  ave stärS  V.p.  41 ;  —  yat  ml  starS  .  .  kacilnie (sd.) paraca  mä  ..YtS.i;  —  stärS  mSahS (NS.?)''  *ki>an  anayra  *rao^ä  FrBy.;  — i.7»hqm  (yä.m\.  fravaHnqm)  raya . .  hvars . . mä  ava  pa%a  aiiti  . .  stärS  Yt.  13.  r  6 ;  — upa  tairam  AaraihyA  .  .  yat  tnl  aiwits urvispnli  staras^a  mis^a  hvanla  Yt./2,as; V.  2. 40;  —  strSuÜca  mäahsmca  hvar?ca Y.  2.  II,  7/.  9,  G.^.6,  Yt/O.  I4s;  V.  ir.  i, 2  (statt  NS.),  7.  52  (statt  NS.),  VyL  43;  — haca  manhsm  (statt  AbL)  V.//.10;  — fravalayö  .  .  yä  strqtn  mäahS  (GS.)  hürB .  .  pa%S  dalsaym  Yt /J.  57;  Y./.  16;  — yazai  hax^r)mca  yat  asti  . .  antan  maf?- h)mca  hvanca  Yt  6.<,\8.\;  —  kj  yä  mil ux^äti  tunfsaitx  Szcß/(sd,)  Y.  .^3;  — pancaJasa  (sd.)  mä  ux^eiti  panla.dasa mh  mnßatti  Yt?.  3;  z',  F.  (?;  —  yai mätshtm  (statt  NS.)  raoxlne  täpayeiti  Yt. 7. 4;  —  raoxsrum  mafihtm  aiwi.vainsm Yt7. 3;  3^;  —  tanüm  .  .  yaha  maaAs hväraexmS  {sA.)  Yt. /0,14a;  —  ragnna- vatitwt  bavähi  yä^a  mävh^m  (statt  NS.) Az.  6;  Vyt  4;  — yatai  mäahgm  ffoaa^r^m bay»m  raSvanttm  i^annaauAantpm  YL7. 5, S.2.  12;  Yt7.3,  6,  -TZ- 33,  Y./6.4;  — mäahahe'^  gaoc^rahe  Vt?,  o;  Y.  j.  11, N.  47;  —  mmS  mänhai^^  gaocÜiräi  Yt. 7. 1 ;  —  uzayara  usTra  mnnha  (VS.) '' gaoHhra  V.  21. 9.  a)  mäahahe''^  (näml. ayari)  heisst  der  12,  Monatstag:  mäis- hahe^^  gaoevirake  S.  j.  12;  vgl.  2.1a,  Y. 16.  i,,  2)  'Monat':  dasa  ava%ra  tnäKhö (NP.)  zayana  dva  hqtiüna  V.  /.  3 ;  —  hapta
```


## [2026-09-07T15:55:09.661Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20330,20342p' BRT.txt | cut -c1-200; echo \"=== messen\"; grep -n \"'messen'\\|,messen'\\|messen\\b\" BRT.txt | head -20"
}
```


### [2026-09-07T15:55:09.722Z] TOOL RESULT

```
•  ').  mäzdayaanay-  Adj.  (auch  fem.)  'den .it/aidä^anbetem  zugehörig  (usw.),  mazda- ^arnisch';  i)  von  viir-  f.:  ..Aafnqm  avazSit •nis  avi  vUS  V.  iS.ia;Y.J2.  y,  —  / *avaAi
mäh-
r7o
VUpayäi  vTse  •ne(?)  Y.6S.J4.  2)  von
'dafnä-  (Stvcrz.) :  dama  °ni!',  damqm  'nlm, daBiayä  °nsii,  dagnayai  'ttüit,  dalne  'ne (VS.).  a)  als  Subst.  sva.  mazdayasna-: ahmi  nmSne yat  '/tüilV.ß,  45,  46,  59,  A4, '3-  
Ableit  {mit  ff ddiii)  aus  maidayaina-. —  Fü.: mätdayasn').  —  ■)  Meist  madddtn  oder m  a  ddt  n  geschrieben,  5.  ^matdayasna-  No.  t.
•  j.  mäzdräjah'ya-  n.  'Dauer  eines Monats':  antarst  tialmat  'hfm  "innerhalb (d.  i.  vor  Ablauf)  eines  Monats"  V,  5. 43;  —  ^rix^apanm  vS  'hfm  vä  V.5. la;  42.
Ableit.  »US  "mäi^ixa  mäh;  %  304  II.  lyräjah- Adj.  'einen  Monat  dauernd'.  —  Fü.:  mäk drahttäi.
•  j.,  g.,  p.  mah'  m.  i)  'Mond',  auch  als Gottheit*':  avat  hvan  .  .  käu  ma  .  .  ave stärS  V.p.  41 ;  —  yat  ml  starS  .  .  kacilnie (sd.) paraca  mä  ..YtS.i;  —  stärS 
dby  Google
II7I
mahya-
^iiiti  AtjminS  manha'^  (NP.)  panla  xayana asianisd.)  V. /.  3PÜZ.;  —  ^ri^  m,hMs (AP.)  V.  7- 14;  1 5, :?.  33  PüZ,  12. 8, 15. 45, Vd.  ig;  —  sar^aAe  viinhs  (GS.)  FrW.  8.  i ; 
=== messen
5317:•  j.  a-ra9Twya-  'unzeitig;  unangemessen, ungebührlich':  'wya  daxsta  "wimla  gar)- m3um  V. /.  18;  17;  —  ra%wyanqm  .  . syaohnanqm  . .  aoäityanqm  •wyanqm  dui- varstanam  iyao^nanam  Vr.  15.1;  —  °wya Vyt.47'-(?),  4^C?)-  '
6571:unversicglich  zu  gemessen  gab"  Yt.  i^.  martiyt  tyaiy  *adakly(^^i,)  avadä  aha' tu '' 32  (?);  —  negirt:  nava{%d..)  hi asti  ci^ia  . .  Bh.4.18;  — yätä  adam  babirauv  rihatn tiöit  Ae  asti  yaozda'irfm  V._J.  39;  39;  —  .  "während  dem  dass  ich  mich  in  Babylon nalas  aitihe  asti  uzvanznn  "es  gibt  dafür  '  aufhielt"  Bh.  2.  2 ;  3. 13.  B)  im  Awf. kein  Wiedergutmachen"  V.  18.  57;  — yesi '  a)  vispa . .  yä  kmii  haptS.karivShva  "alles
8843:S4-J3',  —  *a/  aitahe  paiti  .  .  axaBa  V. JÄ68; — /fl/(ASn.)*'  alsa  nätrika paoifim :^ar»%anam  c^aräl  "was  soll  die  Frau  als erste  Speise  gemessen?"  V.5.S0;  —  Ictm (ASn.)3>  haxa  ha^  "baraiti  (sd.)  Y.tfa.S; 20,4;  —  kJng  ä  vaiihSus  fimat  mananhd /isti/{sd.)  "wer  sind  sie,  bei  denen  . ,"  Y. 4^.11;  —  kahmäi  fradaesayS  damqm  V. 2,1',  i;  —  ^Mahmäi*^  tg  alvahmi  paiti vals  . .  H.  1. 1 ;  —  kaAmai  vlvtduyi  (sd.) vasT  Y.  4j.  9;  —  las  akJ  kahya  akJ (sd.)  Y.^5.7;  —  kaht  vaca  vanni  kahe vaca  .  .  i  ana  vaca  vanäni  V.  ig.  8  f. ;  — kahmilt  haca  usahinanqtn  gaisanqm  ratu- fril  frajasaiti  (sd.)  "von  welchem  (Zeit- punkt) an  .  ."  '^{.46;  4-j~^o^;  —  k}  .. kä  (ISm.)  sp3ntä  ärmaitis  isA.)  "wer  .  .?, mit  wem  ,  ,?"  Y.5/.  ri;  —  kaSibyS  a^äi (sd.)  vohs  jimat  manaaha  Y.  46. 3 ;  44. 6.  a)    'wer    (von    zweien)?':    ku^rü
17209:•  j.  bar9zi-mita-"  Adj.  'hochgemessen, hochgebaut':  nman?m  ..  't>m  Yt/o.  30; —  Hahe  nmanahe  Yt  IQ.  z8.
19581:•  j.  ^mad-  V.  'zumessen'.    x-Aor,  i  mas-. 'zumessen,  zuteilen':  asakya  ysm  (sd.)
20271:•  j.,g.  (,p.)  'mä(y)- V,  'messen'.  Fraes. 27 maya-;  Perf.  i  mim-.  —  PPfP,  'mita-, •mlta-,  maia-,  PFP.  'mi^wa-,
20272:i)  'messen,  bilden,  bauen':  am»sa  spitUa e&ät  milta  aiat  büta  kaca  vaahaot  inana- t^Aaj". .  gebildet  und  hervorgegangen  aus . ." Vr.  77. 12;  —  'mita-.  2)  'ausmessen mit  — ,  vergleichen':  'mthwa-.
20276:mit  frä  i)  'als  Norm  au&tetlen,  an- ordnen, befehlen';  yät  ySsia  framTma%a (3PPfA.)-'>  ya  Moiya . .  vaxlmtz dafvdsuitä (sd.)  "seitdem  ihr  das  verfügt  habt, dass . ."  Y.  J2. 4",  s)  Med.  'sich  messen, erproben  an  — ':  'framata-.  3)  'ver- bilden, umbilden,  verwandeln  in  — '  (Instr.): yal  barata  aursm  mainySm  framitim aspahe  kshrpa  "dass  er  den  AM.  ritt,  den in  Rossgestalt  verwandelten"  Yt75. 29.
21541:Ableit.  —  Eig.  'was  (vom  Schicksal)  gewährt, lUgewieseQ  isl'  (s.  iai.'a-);  l'PfP.  lum  V.^am-, vgl.  IF. //.  141  undj'Jmi- mit  No.  1.  — wp.yäl, yälak  m  yälg^  (Päz.  jSdangS),  yälaigäw 'Yvt- Sprech,  Sachwalter'  ;s.  Hbm.  AGr.  l.  231,  IFAni. Ä43*'-  —  Pü-!  bahr{i  gehänX  »"äslak  {i gtili). —  >)  Um  danach  dessen  Wohltätigkeitsstnn zu  bemessen.  —  >)  Aber  die  eigentliche  Be- deutung des  mp.  Worts  ist  anders  als  dort lu  beslimmen.  Falsch  KZ.  j/.  553.  —  S. übrigens  auch  zu  vazö.v^'ieya-  No.  3.
25099:•  j.  •ra^'wya-  Adj.  (fem.  'ya-)  'was  der gegebenen  Zeit  entspricht,  angemessen  ist, was  sich  zur  gegebenen  Zeit  und  im  ge- gebenen Fall  gehört':  ya^a  'ya  (NSf) vanna  (Sp.  1372  u.)  V.jj.  46;  —  mthnm .  .  yS  .  .  fravazaite  .  .  'ya  (IS.)  *äxra (sd.)  Aaämnff  Yt/0. 67;  —  yas3  ^wa aextö.nämana  yasna  'ya  (IS.)  vom  yazaite Yt  J0.3o;3i3,  56;  —  'yi  uxlä  F.jf.;  — vavan9  buye  'ya  manaaha  'ya  valargAa 'ya  ^aohna  A.  7, 1 1 ;  —  sonst  neben däitya'{sd.):  viovä  däilyqm ..  *yqm  ävisiim ". .  die  in  rechter  Fonn , ,,  zu  rechter  Zeit ach  vollziehende  Weihe"  Vr,  77.19; —  '^*'- yanqm  'yanqm  kvarstanqm  fyao%nanqm varttäi  pairi  a%3ityanam  ard^wyanam vansäi  Yx.15.  i;  —  argdvlm  .  .  yä  .  . iäirümqm  daitim  'wjtn  patma  ava.baraiti ". .  die  den  Umständen  und  der  Zeit  ent- sprechende Milch  .  ."  Y,  6j.  2 ;  —  in  der Rechtssprache  :f/di>V<i  'ya(APn.)/rSrai^ya (sd.)  F.^e.
28947:I)  mit  Abi.  (oder  dessen  Vertreter)  *'  zur Angabe  des  Punktes ,  von  dem  aus etwas  erfolgt  oder  gemessen  wird;  'ab, ex';  i)  räumlich  'von  ~  aus,  an,  her,  weg; fort  von  — ;  heraus  aus  — ';  mit  der  An- schauung des  'von  —  her"  verknüpft  sich die  des  Ursprungs,  aber  auch  der  Ver- mittlung und  des  Zusammenhangs;  a)  im jAw.;  a)  bei  Verben*';  «)  der  Bewegung: yaoMya  taanti  ('ruunt')  aps  zrayarfhal  h' püitikst  avi  srays  vouru-kalitii  V.5. 19; Y-Ö5.3;  — y>-ai'asa»'fc Cprovehitur")  mihrd .  .  Ä*  raffxßnSt  *garS  nmilnat  Yt  lO.  1 24; —  isavasHt  .  .  hu%axtat  h'  'hanvanät  .  . vas^mna  Yt.10.39;  —  zar^tva^t..vat3inna h'  bäzubyS  Yt/0. 39;  39;  —  hukairjm barytS  . ,  yahmat  ml  h'  fratga%aite  ('pro- ruit')  andvi  Ytj.  96; —  w.^a/a/Cevasit') frat^rast  . ,  xrayaahat  A'  Vffurukaiai  Yt. ^9-STi   —   apa.dvarai  Cabscessit^)  anrB
```


## [2026-09-07T15:55:18.030Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20271,20300p' BRT.txt"
}
```


### [2026-09-07T15:55:18.076Z] TOOL RESULT

```
•  j.,g.  (,p.)  'mä(y)- V,  'messen'.  Fraes. 27 maya-;  Perf.  i  mim-.  —  PPfP,  'mita-, •mlta-,  maia-,  PFP.  'mi^wa-,
i)  'messen,  bilden,  bauen':  am»sa  spitUa e&ät  milta  aiat  büta  kaca  vaahaot  inana- t^Aaj". .  gebildet  und  hervorgegangen  aus . ." Vr.  77. 12;  —  'mita-.  2)  'ausmessen mit  — ,  vergleichen':  'mthwa-.
mit  ä  Med.  'sich  erproben,  als  tUchtig  I
erweisen,  seine  BeMiigung  ausweisen': amsts  xT  aus  yava^a  . ,  "der  ist  erprobt für  immer  . ."  ¥.7.39;  —  am3ta  F.tf; —  II  ha^a  paruviyalcr  ämätä  amahy  "vor Alteis  haben  wir  uns  als  tUchtig  erwiesen*' Bh.  7. 3  ■',  a)  'seine  Befähigung  erweisen an  — '  (Dat.):  AatSrS*^  paurvS  Smayänte masäayasnaHbyS  vS  daffvayasna^ibyS  väf . .  darvayamaiibyB  paurvS  . .  SmayayatUa (3POM.)  yaäsa  , .  "an  welchen  von  beiden sollen  sie  zunächst  ihre  Befähigung  (zur Chirurgie)  zu  erweisen  suchen,  an  Af.  oder D.7  . .  An  D.  sollen  sie  eher  ihre  Be- fähigung zu  erweisen  suchen  als  . ,"  V. 7. 36£;  —  ungrammatisch:  itsit  staotanqm yesnyanqm  amats  vJsperafavS{%o\[häsae,'a^ "der  nicht  die  Befähigung  erwiesen  hat  fUr den  Vortrag  der  StY.  (und)  der  VR."  Yt
70.  133.
mit  frä  i)  'als  Norm  au&tetlen,  an- ordnen, befehlen';  yät  ySsia  framTma%a (3PPfA.)-'>  ya  Moiya . .  vaxlmtz dafvdsuitä (sd.)  "seitdem  ihr  das  verfügt  habt, dass . ."  Y.  J2. 4",  s)  Med.  'sich  messen, erproben  an  — ':  'framata-.  3)  'ver- bilden, umbilden,  verwandeln  in  — '  (Instr.): yal  barata  aursm  mainySm  framitim aspahe  kshrpa  "dass  er  den  AM.  ritt,  den in  Rossgestalt  verwandelten"  Yt75. 29.
mit  vJ^  'missbilden,  umstalten':  vX- mlta',
ai.  miTnile;  mitik;  np.  patmäyad  'er  misit', »üBiöj'flrf'er  teiel'.  ätiaöj'.irf 'er erptobt';  ows. amain  'erbaoen.  —  PO.  (in  V./,  F.  S):  ezmä- yün,  Hmüli^ai),  (zu  Vr.  //):  mäiatiA  'Mutter- schaft'; s.  noch  No.  4-  —  ')  Nach  Aia>R£AS bei  HüsiNG  KZ.  3S.  255  ist  statt  ämäiä  viel- mehr ädälä  (zu  'ätj/a-)  lu  lesen.  In  Bh.  /.  3 sind  die  drei  ersten,  in  Bh.  a  der  zweite Buchstabe  lerstSrt  —  ')  Statt  iaiäraiiiyi.  — J'  S  3S4\  »■  lOcl'  vai>räai%ä.  —  0  ke  .  .  al frä!  mimht  vartmct,  erl:  tuS  afe  frifil  vai mtniht  api  3  vinSt  iartatt  varleiüt.  —  S)  Vgl, noch  "iiimä.
.  j.  '«a(^)-  f.  'Mass'.  {mam  V.5.60,
61 :  lies  avi.mqm;  —  "mäi,  "mä  F.  6:  sbes.j
KompEX  (s.  n^moiR,  yiAa-m^m).  —  Zum  V.
mäj'):  —  ai.  ma(y)-  f.  —  Pü.;  fiaimä>t(ai).
•  j.  "mal  F.  6.
Angebt.  'Mass',  nach  Pü. :  patmän.  Die  Beleg- stelle vlsp>m  mäi  (Pä-:  karvisp  patmän,  aber NpB.:  tamäm  mäi)  aaiike  ist  aus  visptmäi a^ukt  verderbt;  t.  Ny.  4-  !$■  Yt  10.  5.
•  j.  mä-£im  neg.  Part,  'verstärktes  'ma '/*^',  mit  Imp."':  slaomaca  raxar^a  (sd.)
dby  Google
baranta  .  .  m°  gjrxSni  pärayantu ''  kaia
ahmai  nmanSt  Yty.  157.
ai.  vgL  m&läm  neg.  Put.  —  Vgl.  mAaMm.  — <)  BeguDsligt  durch  den  Imp.  der  voiher- gehenden  positiven  Säue.
•  j.  mäta-  Adj-,  PPfP.:  s.  'otjO")-. KämpE.
•  j.  'mätar-  m.  'der  misst,  Messer':   Vöi
KompE.  —  Ziun  V.  mö(^)..  —  ai,  milar-  m.  ■ —  PQ.:  palmän  'MaKs'.  —  ')  Bei  der  Viel-  i deutigkeit  des  Anigangs  'la  nicht  sicher  be- stimmbar.
•  ].,  g.  (,  p.)  'mätar-  f.  'Mutter*:  yai  pits .  .  'ta  vä  paradrUyäti  hat  a^qm  upa.- manaytn  (sd.)  pukrS  haia  pilarvm  duyta^ haca  Uanm  V.  12. 1 ;  3,  F.  2,  6;  —  pita  tl (näml.  asöis)yS  ahurB  masdh . .  °la  ärmaifi/ brata  .  .  Yt.  77.  16;  —  apaiiä  .  .  'larS (VP.)  /aayff  (sd.)  Y.  JÄ  5;  —  von  Mutter- tieren :  apatca  vä  aztfäl  . .  'Urqlüä  (AP.) ..  agft^a  (sd.)  Y.jtf.5.
KompE.  —  ai.  mätär-  f.,  np,  mädar.  —  Pii, : niälar;  s.  noch  No.  I.  —  •)  Zu  Y.  jS.  5 werden  die  Worte  von  Pii.  als  EN.  genommen und  traniskribirl  1  dabei  zu  mäOrqi  die  Erl.: äf  andar  hamiandUniA  (Sü,:  samiandhi)  i  an narSn  u  mälaiäit  idxmäk  (Samenflüssigkeit); lu  mälare  jSayS  die  Erl.:  lä  (Milch);  vgl.  lu ma^tanl-  *).
•  p.  mä-tya'*  neg.  Konjn.  mit  Konjv.; 1)  hinter  einem  regierenden  Satz  mit  ava- hyarädiy  'dass  nicht,  damit  nicht':  ava- hyarädiy  naiy  nipistam  tn'  hyi^  . .  avahyH paruv  *%aday^  (sd.)  Bh,  4-8;  —  ava- hyarädty{sA.)  käram  aväjamyä''  "tya^mam xsnäsätiy  (sd.)  tyt^ . .  Bh.  i,  13,  2)  ohne regierenden  Satz,  sva,  V/Ä:  /j-a*  manä kartam  varnavatäm  ^uväm  m°  *draujT- yshy  {s^)  Bh.  ^.  6;  —  tuvam  kä  hya* aparam  itnäm  diptm  vainähy  . .  m'  vika- nähy  "du,  wer  es  auch  sei,  der  du  später diese  Inschrift  sehen  wirst  . .,  zerstöre  sie nicht"  Bh.4. 15.
j.  "«DO-gm  Vyt.  JO;  %.  "aita.in'.
•  j.  mä-3a  prohib.  Part,  'und  nicht,  neve', den  oder  die  letzten  von  zwei  oder  mehr gleichgeordneten  Satzteilen  mit  'ma  '/tij' einleitend  und  anschliessend;  i)  mit  Inf.: mä  ns  npB  duMananhe  mä'>  ..m'  nS  ahmt
fi-iüäiü  (sd.)  yS  ..  m'  nS  . .  Y.65.  7;  — mä  apaima  ..  mä  manaaha  mä' ia'^aiina  paitt./ime (sd.)  Vr.22. 3.  i)  mit Ellipse  des  Verbs:  mn  iuyama  ssdreÄricö
mä* . .  m'  (näml.  'soll  es  geschehen")  ya/ «J  uyra.bäxäu!  nivana^  Yt  10, 75.
KompA.   —    Pü.!  mä.    —    i)  So  K7a;  NA.
```


## [2026-09-07T15:55:31.644Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=20200 && NR<=20345' BRT.txt | grep -nE \"^\\s*[0-9Il|rOo]{3,4}\\s*$|^[0-9]{4}\" | head -20; echo \"--- raw candidates\"; sed -n '20200,20345p' BRT.txt | grep -nE \"11[0-9][0-9]|I1[0-9]\" | head"
}
```


### [2026-09-07T15:55:32.926Z] TOOL RESULT

```
29:1164
56:1166
133:r7o
141:II7I
--- raw candidates
29:1164
56:1166
```


## [2026-09-07T15:55:41.737Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^meter,\" KLN_1966.txt | head -3; grep -n \"^measure,\" KLN_1966.txt | head -3; grep -n \"^month,\" KLN_1966.txt | head -3; grep -n \"^meal,\" KLN_1966.txt | head -3; grep -n \"^semester,\" KLN_1966.txt | head -3; grep -n \"^dimension,\" KLN_1966.txt | head -3; grep -n \"^diameter,\" KLN_1966.txt|head -3; grep -n \"^geometry,\" KLN_1966.txt|head -3; grep -n \"^Monday,\" KLN_1966.txt|head -3; grep -n \"^moon,\" KLN_1966.txt|head -3"
}
```


### [2026-09-07T15:55:41.934Z] TOOL RESULT

```
23737:meter,  n.,  1)  one  who  measures;  2)  an  instrument for  measuring.  —  Formed  fr.  mete,  ‘to  measure’, with  agential  suff.  -er.
23738:meter,  metre,  n.,  poetical  rhythm.  —  ME.  metre, fr.  OF.  metre  (F.  metre),  fr.  L.  metrum,  fr.  Gk. pixpov,  ‘measure,  meter’,  which  is  rel.  to  prjxpa (Hesychius),  ‘lot,  portion’,  fr.  I.-E.  base  *me-, ‘to  measure’,  whence  also  OI.  mati  (fr.  I.-E. *me-ti),  mirndti,  ‘measures’,  matram  (neut.), matrd  (fem.),  ‘measure’,  Avestic,  OPers.  ma-,  L. metiri,  ‘to  measure’.  Cp.  matra.  Metis,  mensal, ‘pertaining  to  the  table’,  and  the  second  element in  castrametation,  firman,  mahout,  vimana.  For derivatives  of  base  *med-,  a  -rf-enlargement  of base  *me-,  see  meditate.
23740:meter,  metre,  n.,  the  unit  of  length  in  the  metric system.  —  F.  mitre  (see  prec.  word) ;  introduced in  France  as  a  name  of  measure  in  1791.
23245:measure,  n.  —  ME.  mesure,  fr.  OF.  (=  F.)  me- sure,  fr.  L.  mensura,  ‘measure’,  fr.  mensus,  pp. of  metiri,  ‘to  measure’.  See  mete,  ‘to  measure’, and  -ure  and  cp.  meter,  ‘poetical  rhythm’.  Cp. also  admeasure,  immeasurable,  measure,  men¬ surable,  mensurate,  commensurable,  dimension, immense.  Cp.  also  1  st  mensal.
24356:month,  n.  —  ME.  moneth,  month,  fr.  OE.  monad, rel.  to  OS.  manuth,  ON.  manadr,  Dan.  manned, Swed.  manad,  Norw.  maanad,  OFris.  monath, MDu.  mdnet,  Du.  maand,  OHG.  manod,  MHG. manat,  G.  Monat,  Goth,  menojrs,  ‘month’,  and to  OG.  mona,  etc.,  ‘moon’.  See  moon  and  subst. suff.  -th.
23231:meal,  n.,  edible  grain.  —  ME.  mele,  fr.  OE.  me  hi, rel.  to  OS.  me/e,  ON.,  Swed.,  Norw.  mjdl,  Dan. met  OFris.  mele,  MDu.  mele,  Du.  meet,  OHG. melo,  MHG.  mel,  G.  Mehl,  ‘meal’,  orig.  ‘that which  is  ground’,  and  rel.  to  OS.,  OHG.,  Goth. malan,  ON.,  Swed.  mala,  Dan.  male,  MDu.,  Du. malen,  MHG.  main,  G.  malen,  ‘to  grind’,  fr. I.-E.  base  *(s)mel-,  ‘to  rub,  grind’,  whence  also Toch.  A  malyw,  B.  mely,  ‘to  press,  tread  under foot’,  Hitt,  mallanzi,  ‘they  grind’,  miyalli,  ‘mill'. Arm.  malem,  ‘I  crush,  bruise’,  Gk.  paXaxdq, ‘soft’,  puXx;,  later  uoXoc,  ‘mill’.  Alb.  miel,  ‘meal, flour’,  L.  molere,  ‘to  grind’,  mola,  ‘millstone, mill’,  OSlav.  meljQ,  mUti,  Lith.  malit,  maid, Lett,  mafu,  malt,  ‘to  grind’,  Lith.  miltai,  OPruss. meltan,  Lett,  mild,  ‘meal’,  OSlav.  moll,  Goth. maid,  ON.  molr,  Norw.  mol,  Dan.  mol,  Swed. mal,  ‘moth’,  OE.  mzlsccafa,  ‘malshave’  (cater¬ pillar),  OHG.  miliwa,  milwa,  MHG.  milwe,  G. Milbe,  ‘mite’,  lit.  ‘a  grinding,  powder-making animal’,  OHG.  gimulli,  G.  Gemuil,  ‘moldering dust’,  OIr.  melim,  ‘I  grind’,  W.  malu,  Bret. malaf,  ‘to  grind’,  MW.  blawt,  ModW.  blawd, ‘meal’.  From  *mel-d,  *mled-,  *mld-,  -d-e n- largements  of  base  *(s)mel-,  ‘to  rub,  grind’, derive  OI.  mrduh,  ‘soft,  tender,  mild’.  Arm. melk  (for  *meldw-i-),  ‘soft,  slack’,  Gk.  pXaSapoq (for  VXaSxpoc),  pXa86?  (for  ♦p.XaSiip),  ‘loose, spongy’,  piXSetv,  ‘to  melt,  make  liquid’,  dy.aXSu- vstv,  ‘to  crush,  destroy’,  L.  mollis  (for  *mold  -is), ‘soft*.  OPruss.  maldai  (pi.),  ‘boys,  lads'  (for
11445:dimension,  n.  —  F.,  fr.  L.  dimensidnem,  acc.  of dimensio,  ‘a  measuring’,  fr.  dimensus,  pp.  of dimetiri,  ‘to  measure  out’,  fr.  di-,  ‘apart’,  and metiri,  ‘to  measure’.  See  measure  and  -ion. Derivatives:  dimension-al ,  adj.,  dimension-al- ity,  n.,  dimension-al-ly,  adv. dimensionless,  adj.  —  Formed  fr.  dimension  and -less;  first  used  by  Milton, dimerous,  adj.,  having  two  parts.  —  Formed  fr. di-,  ‘two’,  Gk.  pepo?,  ‘part’  (see  mero-),  and  suff. -ous  (fr.  L.  -dsus).  See  mero-. dimeter,  n.,  a  verse  consisting  of  two  measures (prosody).  —  Late  L.  dimeter,  fr.  Gk.  SipsTpo?, ‘(a  verse)  having  two  measures’,  fr.  81-  (see  di-, ‘two’)  and  pixpov,  ‘measure’.  See  meter,  ‘poetical rhythm’.
11252:diameter,  n.  —  OF.  diametre  (F.  diametre),  fr. L.  diametros,  fr.  Gk.  SiapiExpog  (scil.  '(p<y.u.y.r), lit.  ‘a  diametral  line’.  See  dia-  and  meter,  ‘poet¬ ical  rhythm’.
24237:Monday,  n.  —  ME.  monenday,  moneday,  fr.  OE. monandxg,  lit.  ‘day  of  the  moon’,  fr.  mono, ‘moon’,  and  dxg,  ‘day’ ;  cp.  ON.  manadagr,  Dan. mandag,  Swed.  mandag,  Norw.  maandag,  OFris. monendei,  Du.  maandag,  OHG.  manetag ,  MHG. monlac,  mantac,  G.  Montag.  These  words  are prop,  loan  translations  of  L.  Lunae  dies,  ‘the day  of  the  moon’  (whence  It.  lunedi,  OF.  lunsdi,
24364:moon,  n.  —  ME.  mone,  moone,  fr.  OE.  mona,  rel. to  OFris.  mona,  OS.,  OHG.  mano,  ON.  mdni (whence  Dan.  and  Norw.  maane,  Swed.  mane, MDu.  mane,  Du.  maan,  MHG.  mane,  G.  Mond, Goth,  mena,  ‘moon’,  and  cogn.  with  Ol.  mas-, mdsah,  ‘moon,  month’,  Avestic  md,  ModPers. mah,  of  s.m.,  Toch.  A  man,  ‘moon,  month’,  B mehe,  ‘month’,  mem,  ‘moon’.  Arm.  amis,  gen. amsoy,  ‘month',  Gk.  {cryr,,  ‘moon’,  p:qv,  gen. prjvis,  ‘month’,  Alb.  muai ,  ‘month’,  L.  mensis, ‘month’,  OSlav.  mesQd,  ‘moon,  month’,  Lith. menesis,  menuo,  of  s.m.,  Lett,  meness,  ‘moon’, menesis,  ‘month’,  OPruss.  menig,  ‘month’,  OIr. mi,  gen.  mis,  W.  and  OCo.  mis,  Bret,  miz, ‘month’.  All  these  words  derive  fr.  I.-E.
```


## [2026-09-07T15:55:51.038Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^meal,  n.,  repast\\|meal,  n.,  a  repast\\|^semester\\|semester,\" KLN_1966.txt | head -5; echo \"===\"; sed -n '23232,23236p' KLN_1966.txt | cut -c1-1200"
}
```


### [2026-09-07T15:55:51.114Z] TOOL RESULT

```
34338:seamster,  also  sempster,  n.,  a  person,  esp.  a man,  employed  in  sewing.  —  ME.  semester, semster,  fr.  OE.  seamestre,  formed  fr.  seam (see  seam)  with  fem.  agential  suff.  -estre  (see -ster).
34519:Semele,  n.,  the  daughter  of  Cadmus  and  the mother  of  Dionysus  (Greek  mythol.)  —  L.,  fr. Gk.  SsuiXr,,  a  Thraco-Phrygian  earth  goddess, fr.  Phrygian  ZsqcXco,  ‘mother  of  the  earth’.  See Franz  Altheim,  Geschichte  der  lateinischen Sprache,  p.  132.  Phryg.  Ze|zeXo>  is  prob.  cogn. with  OSlav.  zemlja,  ‘earth’,  L.  humus,  ‘earth, ground,  soil'.  See  humus, semen,  n.  —  L.  semen,  ‘seed’,  cogn.  with  OSlav. simg,  OPruss.  semen,  ‘seed’,  Lith.  semens  (pi.), ‘seed  of  flax’,  OS.,  OHG.  samo,  ‘seed’,  MHG. same,  G.  Same,  of  s.m. ;  fr.  I.-E.  base  *se(i)-,  ‘to sow’.  Cp.  L.  serere,  ‘to  sow’,  which  derives  fr. *si-sd,  reduplication  of  the  original  base  *se-. See  sow,  v.,  and  cp.  seme,  seminal,  seminary, semination,  disseminate,  inseminate.  Cp.  also season.  For  the  ending  of  semen  see  suff.  -men. semester,  n.,  a  period  of  six  months.  —  G.  Se¬
===
95Z
953
sense  development  cp.  Rum.  tandr,  young  ,  fr- L.  tener,  ‘soft,  tender’),  OPruss.  maldaisin  (acc.), ‘youngest’,  maldian,  ‘foal’,  OSlav.  mladu,  Russ. molodH,  ‘young’,  OE.  meltan,  mieltan,  ‘to  melt', prob.  also  OIr.  meldach,  ‘pleasant’.  From  base *mel-dh-,  a  -^-enlargement  of  base  *mel-,  de¬ rive  Gk.  paXffaxo?,  ‘soft’,  OE.  melde,  OS. maldia,  OHG.  melta,  molta,  multa,  MHG.,  G. melde,  ‘orach’,  Goth,  mildeis,  OE.  milde,  mild  . (OIr.  meldach  and  the  Balto-Slav.  words  cited above  as  derivatives  of  base  *mel-d-,  could  also be  derived  from  base  *mel-dh-.)  Cp.  amalgam, Amalthaea,  ambly,  blenno-,  blite,  emollient, emolument,  immolate.  Maelstrom,  malaco-  ma¬ lax,  malt,  meldometer,  mellow,  melt,  ‘to  dissolve’, mild,  mildew,  mill,  millet,  milt,  moil,  molar, ‘grinding’,  mold,  ‘soil’,  mole,  ‘false  conception’, molinary,  mollify,  Mollugo,  mollusk,  mouille, moulin,  mulch,  muliebrity,  mull,  ‘to  powder’, mull,  ‘a  snuff  box’,  mullein,  muller,  mullet,  ‘star’, multure,  mylo-,  ormolu.
Derivatives:  meal-y,  adj.,  meal-i-ness,  n. meal,  n.,  food  taken  at  one  time.  —  ME.  mele,  fr. OE.  mil,  ‘mark,  sign ;  measure;  fixed  time;  time for  taking  food,  meal’,  rel.  to  ON.  mal,  ‘meas¬ ure,  time,  meal’,  OFris.  mel(tid),  (time  of) meal’,  Du.  maal,  ‘time;  meal’,  OHG.,  MHG-. mal,  ‘time;  meal',  G.  Mal,  ‘time’,  Mahl,  meal  , Goth,  mel,  ‘time;  hour’,  fr.  I.-E.  base  *me-,  to measure’.  See  meter,  ‘poetical  rhythm  . Derivative:  meal,  tr.  v.,  to  have  a  meal.
-meal,  suff.  denoting  quantity  taken  at  one  time; now  used  only  in  piecemeal.  —  ME.  -mele,  fr. OE.  -mxlum,  dat.  pi.  of  OE.  mil,  ‘measure’. See  meal,  ‘food’.
```


## [2026-09-07T15:55:55.700Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34520,34524p' KLN_1966.txt | cut -c1-900"
}
```


### [2026-09-07T15:55:55.754Z] TOOL RESULT

```
mester,  fr.  F.  semestre,  fr.  L.  seme(n)stris  (for *sex-mens-tris),  ‘of  six  months,  half-yearly’,  fr. sex,  ‘six’,  and  mensis,  ‘month’.  Cp.  L.  menstruus, ‘pertaining  to  a  month,  monthly’,  interme(ri)- stris,  ‘between  two  months’,  and  see  six  and moon.  Cp.  also  menses,  trimester, semi-,  combining  form  meaning  ‘half’.  —  ME., fr.  L.  semi-,  ‘half’,  which  is  cogn.  with  OI.  sami, ‘half’,  a-samih,  ‘not  a  half,  complete’,  Gk. ‘half-’,  (for  *'qjxi-TUi;),  ‘half’,  OE.  sam-,
OHG.  sami-,  ‘half’  (cp.  e.g.  OE.  sam-ewieu, OHG.  sami-quek,  ‘half-alive’).  Cp.  hemi-  and the  first  element  in  sesqui-,  sesterce.  Cp.  also  the first  element  in  sandblind. semi-annual,  adj.,  half-yearly.  —  Compounded  of semi-  and  annual.
semibreve,  n.,  a  note  equivalent  to  half  the  length of  a  breve  (music).  —  Compounded  of  semi-  and breve.
semicha,  also  semichah,  n.  —  See  semikah. semicircle,  n.,  a  half  circle.  —  Compounded  of semi-  and  circle.
semicolon,  n.,  a  punctuation  mark  (;).  —  A  hy¬ brid  coined  fr.  L.  semi-,  ‘half’,  and  Gk.  x£>Xov, ‘limb,  part’.  See  semi-  and  colon,  ‘punctuation mark’.
```


## [2026-09-07T15:56:04.570Z] TOOL CALL #57: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T15:56:04.575Z] TOOL RESULT

```


```


## [2026-09-07T15:56:09.429Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meh%E2%82%81-",
 "prompt": "What is the reconstructed PIE root, its meaning, and which descendants/derived terms are listed (especially Proto-Indo-Iranian, Avestan, Greek metron, Latin metior, Germanic *mēlą)?"
}
```


## [2026-09-07T15:56:10.281Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%AA%D8%B1",
 "prompt": "For the Persian entry متر (metr): what etymology is given (borrowed from which language)? Quote it."
}
```


### [2026-09-07T15:56:15.061Z] TOOL RESULT

```
# Etymology of Persian متر (metr)

According to the Wiktionary entry, Persian متر (metr) is **borrowed from French**. 

The exact quote from the etymology section states:

> "Borrowed from French mètre."

This borrowing is traced back through an etymology tree that ultimately derives from Proto-Indo-European roots via Ancient Greek and Latin.
```


### [2026-09-07T15:56:17.091Z] TOOL RESULT

```
# Proto-Indo-European Root *meh₁-

**Reconstructed Root:** *meh₁-

**Meaning:** "to measure"

## Key Descendants and Derived Terms:

**Proto-Indo-Iranian:**
- *mimáHti ~ *mimHati (reduplicated present form)
- Sanskrit: mímāti, mímīte
- Old Avestan: framīmaθā (2pl. ind./subj.)

**Greek:**
- Ancient Greek: μέτρον (métron) from *mh₁-tro-m, meaning "measurement"

**Latin:**
- mētior (denominative verb) from *mētis
- mēta ("goal, boundary")

**Germanic:**
- Proto-Germanic: *mēlą from *meh₁-lo- ("measurement, time")

**Etymology Note:** 
This root represents "a phonetical variant of *med- through the 'Kortlandt effect,' which posits that *d becomes *h₁ under certain conditions."

The root generated approximately 103 derived terms across Indo-European languages, reflecting its semantic centrality to concepts of measurement, time, and extent.
```


## [2026-09-07T15:56:21.638Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/meter",
 "prompt": "Give the full etymology of meter/metre (unit of length and poetic measure), including the French mètre and Greek metron chain and the date of the French coinage."
}
```


## [2026-09-07T15:56:23.817Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%85%D9%88%D8%AF%D9%86",
 "prompt": "For Persian پیمودن (peymudan): give the full etymology (Middle Persian form, Proto-Iranian, prefix, root) and the meaning. Quote it."
}
```


### [2026-09-07T15:56:26.829Z] TOOL RESULT

```
# Etymology of Meter/Metre

The word has two distinct etymological paths:

**Poetic Measure (n.1):** Derives from Old English *meter* via Latin *mētrum* and Greek *metron* meaning "measure" or "verse," tracing back to the PIE root *me- "to measure."

**Unit of Length (n.2):** Developed later in 1797, originating from French *mètre* (18th century), which itself derived from Greek *metron* "measure." The French Academy of Sciences created this unit for a decimal-based system of weights and measures, building on work begun in 1670 by French clergyman Gabriel Mouton.

Both ultimately share the same Greek and Latin roots connected to measurement, though the unit of length represents a later application coined specifically for the metric system. The French *mètre* served as the crucial intermediary that transformed the classical linguistic concept into a standardized measurement unit.
```


### [2026-09-07T15:56:29.676Z] TOOL RESULT

```
# Etymology of Persian پیمودن (peymudan)

**Full Etymology Chain:**

The word derives from Middle Persian *ptmwtn'* (paymūdan, paymāy-), meaning "to measure." This traces back to Proto-Iranian combining *pati-* (a prefix) and *maH-* (meaning "to measure"). The root *maH-* ultimately descends from Proto-Indo-European *meh₁-*, also meaning "to measure."

**Direct Quote:**
"From Middle Persian [script needed] (ptmwtn', ptmʾd- /⁠paymūdan, paymāy-⁠/, 'to measure'), ultimately from *pati-* and *maH-* ('to measure')"

**Meaning:**
The verb encompasses multiple senses: to measure, to traverse or travel through, to go through or undergo, to quaff or drink, and in Tajik specifically, to relate or narrate.
```


## [2026-09-07T15:56:34.863Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%85%D9%88%D8%AF%D9%86",
 "prompt": "For Persian نمودن (nomudan/nemudan): give the full etymology (Middle Persian, Proto-Iranian prefix + root) and meanings. Quote it."
}
```


## [2026-09-07T15:56:36.166Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B2%D9%85%D9%88%D8%AF%D9%86",
 "prompt": "For Persian آزمودن (āzmudan): give the full etymology (Middle Persian form, Proto-Iranian prefix(es) + root) and meanings. Quote it."
}
```


### [2026-09-07T15:56:40.971Z] TOOL RESULT

```
# Persian نمودن (nomudan/nemudan)

## Etymology

The word derives from Middle Persian *nmwtn'* (/nimūdan/, "to show, guide"), which combines Proto-Iranian elements: the prefix *ní-* ("in, down") plus *maH-* ("to measure"). These trace back to Proto-Indo-Iranian *ní* and Proto-Indo-European *meh₁-* (both meaning "to measure" or "in, down").

The entry notes: "from Middle Persian [script needed] (nmwtn' /⁠nimūdan⁠/, 'to show, guide'), from Proto-Iranian _*ní-_ + Proto-Iranian _*maH-_ ('to measure')."

## Meanings

The verb has three primary definitions:

1. **To show**, to cause to appear, to exhibit
2. **To appear**, to seem
3. **(in compounds)** To do, make

The usage notes explain that in formal Persian speech, نمودن can substitute for کردن (kardan) in compound verbs to avoid repetition.
```


### [2026-09-07T15:56:41.373Z] TOOL RESULT

```
# Persian آزمودن (āzmudan)

## Etymology
The provided Wiktionary article does not include etymological information about the Middle Persian form or Proto-Iranian components of this word.

## Meanings
The verb آزمودن has six primary definitions:

1. "to test"
2. "to try"
3. "to experiment"
4. "to prove"
5. "to examine"
6. "to experience"

## Historical Citation
The entry includes a quote from Rūmī's Masnavi (c. 1260s): "When I travelled, the Way tried me: what was the present I brought (home) from this travelling?"

The article documents the present stem as **آزما** (âzmâ) and lists related terms including âzmâyeš (test/trial), âzmun (exam), and âzmude (experienced).
```


## [2026-09-07T15:56:46.067Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%85%D8%A7%D9%86",
 "prompt": "For Persian فرمان (farmān): give the full etymology (Old Persian framānā, Middle Persian framān, prefix fra- + root mā-) and meanings. Quote it. Also mention any note about Arabic firmān or English firman."
}
```


## [2026-09-07T15:56:46.812Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%87",
 "prompt": "For the Persian entry ماه (māh): give the etymology (Middle Persian, Old/Proto-Iranian, PIE) and the meanings (moon, month). Quote it."
}
```


### [2026-09-07T15:56:51.423Z] TOOL RESULT

```
# Persian فرمان (farmān)

## Etymology

The word فرمان originates from **Old Persian framānā** ("command"), which derives from **Middle Persian framān**. The formation consists of the prefix **fra-** combined with a root **mā-**, ultimately tracing back to Proto-Iranian *framaHanaH and Proto-Indo-European *meh₁- ("to measure").

## Meanings

According to the Wiktionary entry, فرمان has three primary definitions:

1. "command, order" (with computing context)
2. "decree, edict"
3. "steering wheel" (of a car)

## Notes on Related Forms

The entry documents descendants in multiple languages. The English word **firman** derives from Ottoman Turkish, which itself borrowed the term from Persian. The Arabic **فَرْمَان** (farmān) is also listed as a descendant of the Persian form, demonstrating the term's widespread adoption across languages in the Islamic world and beyond.
```


### [2026-09-07T15:56:53.706Z] TOOL RESULT

```
# Persian ماه (māh) - Etymology and Meanings

## Etymology

The word ماه derives from Middle Persian 𐭡𐭩𐭥𐭧 (byʿḥ /māh/), which came from Old Persian 𐎶𐎠𐏃 (m-a-h /māhaʰ/). This traces back to Proto-Iranian *mā́Hah and ultimately to Proto-Indo-European *mḗh₁n̥s meaning "moon, month."

## Meanings

According to the Wiktionary entry, ماه has three primary definitions:

1. **Moon** - the celestial body
2. **Month** - a unit of time
3. **Beautiful person** (poetic/figurative sense) - used to describe a beloved or a beautiful individual, comparable to how Arabic uses قمر (qamar) poetically

The entry notes: "For the poetic sense 'beautiful person,' compare the semantics of Arabic قَمَر (qamar, 'Moon; (in poetry) beautiful person')."
```


## [2026-09-07T15:56:59.696Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%87%D8%AA%D8%A7%D8%A8",
 "prompt": "For Persian مهتاب (mahtāb): give the etymology (compound of which elements) and meaning. Quote it."
}
```


## [2026-09-07T15:57:01.773Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BC%CE%AD%CF%84%CF%81%CE%BF%CE%BD",
 "prompt": "For Ancient Greek μέτρον: give the etymology (PIE root, suffix) and meaning, and note any alternative derivation from *med-. Also is διάμετρος listed as a derived term?"
}
```


### [2026-09-07T15:57:04.331Z] TOOL RESULT

```
# Etymology and Meaning of Persian مهتاب (mahtāb)

**Etymology:** The word is "a compound of مه (mah) + تاب (tâb)," meaning moon plus light/radiance.

**Meaning:** The term denotes "moonlight."

**Quotation:** Here's an example from the poet Nima Yooshij's work "Mi-tarâvad Mahtâb": "می‌ترواد **مهتاب** / می‌درخشد شب‌تاب" (The moonlight fades / the nightlight shines).
```


### [2026-09-07T15:57:06.805Z] TOOL RESULT

```
# Etymology and Meaning of μέτρον

**Etymology:** According to the Wiktionary entry, μέτρον derives from Proto-Indo-European "*meh₁-" ("to measure") plus the suffix "-τρον" (-tron).

**Meaning:** The word has three primary senses:
1. "Something used to measure: measure, rule, weight"
2. "Length, width, breadth"
3. In music and poetry contexts: "metre"

**Regarding *med-:** The entry does not mention any alternative derivation from *med-. The etymology provided focuses exclusively on the *meh₁- root.

**Regarding διάμετρος:** No, διάμετρος is not listed among the derived terms shown in this entry. The derived terms listed are: μετρέω, μετρητός, -μετρία, μετρικός, μέτριος, and τετράμετρος.
```


## [2026-09-07T15:57:15.126Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meh₁-\" \\\n \"https://en.wiktionary.org/wiki/متر\" \\\n \"https://www.etymonline.com/word/meter\" \\\n \"https://en.wiktionary.org/wiki/پیمودن\" \\\n \"https://en.wiktionary.org/wiki/نمودن\" \\\n \"https://en.wiktionary.org/wiki/آزمودن\" \\\n \"https://en.wiktionary.org/wiki/فرمان\" \\\n \"https://en.wiktionary.org/wiki/ماه\" \\\n \"https://en.wiktionary.org/wiki/مهتاب\" \\\n \"https://en.wiktionary.org/wiki/μέτρον\" ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 323, root Me 2 (to measure) — PIE *meh1-, Av/OP ma-, mah-, NP mah/mahtab/farman/paymudan/azmudan/nomudan/metr, Gk metron, Fr metre' 2>&1 | tail -2\ndone"
}
```


## [2026-09-07T15:57:17.367Z] TOOL CALL #69: Bash

```json
{
 "command": "pdftoppm -f 323 -l 323 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg323 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T15:57:20.260Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5503de5d2f95a00a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0dd85290db568cb6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a8c38b3bd60d8dbd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e64bef261ce1c736.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2673d00b315d8145.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/58519f6543c27655.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9e3e3b837a1f05cd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd71b8262d4811df.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1543ee2dfdd393e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f7e544d28ba91e30.txt
```


### [2026-09-07T15:57:22.349Z] TOOL RESULT

```
total 800
drwx------ 2 sfmqrb sfmqrb   4096 Sep  7 11:57 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    251 Sep  7 11:49 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb  19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb  40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb  97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb 163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb     40 Sep  7 11:49 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1308 Sep  7 11:54 v2001.txt
```


## [2026-09-07T15:57:25.106Z] TOOL CALL #70: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg323.png"
}
```


### [2026-09-07T15:57:25.612Z] TOOL RESULT

```

```


## [2026-09-07T15:57:25.608Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-07T15:57:42.801Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"māh\\|mah\\b\\|māhīg\" SNS.txt | head -15; echo \"=== SNS_pages\"; grep -n \"māh\" SNS_pages.txt | head -10"
}
```


### [2026-09-07T15:57:42.859Z] TOOL RESULT

```
5622:(AiJ/b. 384)uxsyat-namah-: £» 
5885:• Y/f^ ^IU <(S «-aU: amah hem: _**.- *> 
13718:asah-, masan-, mas-, raaz- : fc-mah : i>#?j** 
15696:•vmah I kamisti ^^ „ ' ' 
15699:J ^:vmah vizarisn: u*^, ^ 1( 
29194:mah- 113/2 
29643:uxsyat-namah 71/14 
30776:x v arsedar mah 71/8 
32026:MSdGgmah 253/1 
33887:amah/araag 232/3 
33888:amah hem 74/5 
=== SNS_pages
```


## [2026-09-07T15:57:48.504Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^mah\\|mah- :\\|mah:\\|mah \" SNS.txt | sed -n '1,30p'; echo \"=== around 15696\"; sed -n '15690,15705p' SNS.txt"
}
```


### [2026-09-07T15:57:48.556Z] TOOL RESULT

```
5885:• Y/f^ ^IU <(S «-aU: amah hem: _**.- *> 
13718:asah-, masan-, mas-, raaz- : fc-mah : i>#?j** 
15696:•vmah I kamisti ^^ „ ' ' 
15699:J ^:vmah vizarisn: u*^, ^ 1( 
29194:mah- 113/2 
29643:uxsyat-namah 71/14 
30776:x v arsedar mah 71/8 
31990:mahraanih 239/14 
32026:MSdGgmah 253/1 
32298:mahm3n 237/1 
32299:mahraantar 237/5 
33888:amah hem 74/5 
=== around 15696

1Y/T^ .^£»i :namak:3^l 

~ , " 4 ""*<* "** ested: »«U, „*, . T ,_y_, 

««-.**. wy^ h:>Mrap£ . 208)v . + 
•vmah I kamisti ^^ „ ' ' 

■» *^: vinah viaardan: MU«j ^>. 
J ^:vmah vizarisn: u*^, ^ 1( 



To
```


## [2026-09-07T15:57:55.518Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mah\" SNS_pages.txt | head -20"
}
```


### [2026-09-07T15:57:55.570Z] TOOL RESULT

```
2221:           16/ T -^       U£W>. 562)xlvas. mahya-:^- .o«I«j*T
3574:                             (AiJ/b.      384)uxsyat-namah-: £»
3717:                .^_T/U^ (•$* :Jj) .»>l fj*:hOmyazad:                     W'Hf                                            •   Y/f^ ^IU <(S«-aU: amah hem:                                       _**.- *>
9532:,u   .~          (          <j* *) <***                                                     T*       jj^» l*^ jJ j^U'j'jjle-l^j^j ^hf^ :mahraspand:
9539:                                                                                                                   Yl/TY^ .1>di*-l.** :mahraspand, it:                           *mo*m?£
9611:asah-, masan-, mas-, raaz-   :                                  fc-mah        :    i>#?j**                                                                     /'»
9773:         (Mtr.Man.    **              r^-i-l **! V "' 45)            Ui^i. 1146) raarka-: o^is-*^ maraka-/mahrka- : b~
9848:                                                                              {AiWb. 1146) marka-: l^j-1^ maraka-/mahrka-         fc-                                                             :
11296:                         Burzmihr:"**^)^"                       •vmah I kamisti                   ^^           „                  '         '
11308:                                                   A*~o»>                   J   ^:vmah vizarisn:                     u*^,                   ^         1(             To
12988:    Ai^LJoj^/tgOsurvan amahraspand:^^^^^                                                -jl^ol^i j>J r L<"jff              1j/   ^^"iU G5us urva-                                     :       U
15139:                           mah- 113/2
15318:uxsyat-namah 71/14       karana- 212/17
15325:                                                              xsvas. mahya- 37/9       gaya- 301/14
15683:xist 36/1                x v 3his xvastan 58/9               xv arsedar mah 71/8         yasn 315/3
16013:mahraanih 239/14             mazdist 241/17                     raiySnag 237/12           naxun 258/3
16016:ma£Sg 254/11                 MSdGgmah 253/1                     mOr 248/4                 nazuklh 259/6
16043:kaned 22/11-14-16        kS-s3n 249/18                        kun&n 266/5            mahm3n 237/1
16044:kanend 22/11-14          k5-t 249/13                          kun§nd 219/14-266/9    mahraantar 237/5
16196:                                                                 getog xrid 180/8         gosurvan amahraspanc
```


## [2026-09-07T15:58:06.623Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%85%D8%AA%D8%B1",
 "prompt": "What does Mo'in's Farhang-e Farsi (فرهنگ معین) entry for متر say, including any origin tag such as [فر.] (French)? Quote the entry text."
}
```


## [2026-09-07T15:58:07.998Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2218,2224p' SNS_pages.txt; echo \"=== ARY check\"; grep -n \"ماه\\b\" incoming/ARY/ARY_pages.txt | head -5; grep -n \"MAH\\|MEASURE\\|METER\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T15:58:08.065Z] TOOL RESULT

```
      ^b-jl Jli »-, c#z~±j a;i5           .iU^ :xsvasmangug: 3 *\? *<->-*> t$~i
                                                                                                          \Sijti 9 (0rPE. 300.) v§d                                     :    ^jjl         vindatir^j^
                                                                                                          ro/TT *5 (A/ti'.«an.II,52)wndyh:jjt                                               UtVi. 1449),
           16/ T -^       U£W>. 562)xlvas. mahya-:^- .o«I«j*T

                                                                                                        I xil, *jU- *_»*_ j aiU-T^iju a-f L-^SLiT "                      wjSiT , wjiil
      i_-_ j    c— i!U *3'j ci *-* :xlvasm5nghug:
=== ARY check
180:و اسب‌سواران ماهری پودند. این مردم در طی هفت قرن (از سده‌ی ششم تا سیزدهم پس از میلاد) طی
293:است. واژه‌های همریشه‌ی دیگر نیز در شناخت ماهیت هند و اروپائیان سودمنداند: واژه‌های مشترک
296:«ماهی آزان (5۸14۸/1030) و «ییده (/۷11-1-07) و «بلوط» (0۸74) و «زنبور؛ (81312) و «اردکث»
302:همریشه» همگی دارای بک معنی نیستند. واژه‌های معدودی مانند «مادر» و دماه» و «گاو» در همه
492:لن ماه 0 ۵ ۱۲ 8۵۵۲۵6
5387:TMA, TEMNOTA — (RUSSIAN) (gs TATHRA, TEMAH (AVESTAN) (gl!
8454:DESETU : DASAMA, DASAMAH.
13248:AMA, AMAH, EMA (PAHLAVI) Shy AHMAKEM, AHMA :(AVESTAN) ol!
13279:METER (GREEK) gb y MAT, MATH, MAS «(BALUCHI) gs
13465:| MEsect - MAWNGH, MA, MAH.
13466:MEsic (CZECH) Se MAH HOLD PERSIAN) joel gs),
13467:| MJESIC (SERBIAN) 9 po MAH (PAHLAVI) 5 shy,
13494:age (OLD CHURCH SLAVIC) (5 53%! MAH, MA MAVESTAN) gles!
13495:MISECI MAH (OLD PERSIAN) Jlen\y .g)\,
13497:MESJAC, MIESIATS :(RUSSIAN) .o3) MAH, MAHAK, MAHIGAN
```


### [2026-09-07T15:58:10.513Z] TOOL RESULT

```
# Mo'in's Farhang-e Farsi Entry for متر

According to the webpage, the entry includes an origin tag **[فر.]** (French) and states:

"نواری باریک و درجه‌بندی شده از فلز، پارچه یا جنس دیگر که برای اندازه گیری طول و عرض اشیاء"

The entry defines متر as a thin, graduated strip made of metal, fabric, or other material used for measuring length and width of objects. It also notes that as a unit of length, it approximately equals one forty-millionth of Earth's meridian, with related terms for square meter (unit of area) and cubic meter (unit of volume).
```


## [2026-09-07T15:58:18.659Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13460,13500p' incoming/ARY/ARY_latin_index_pages.txt; echo \"--- pdf tag\"; awk 'NR<=13470' incoming/ARY/ARY_latin_index_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1"
}
```


### [2026-09-07T15:58:19.967Z] TOOL RESULT

```
‘MANEO, MANERE LATIN) oS
[pdf page 462]
|
FY | Cyd po 4) ole
i HOLD CHURCH SLAVIC) oS 3%! AVESTAN) ply!
| MEsect - MAWNGH, MA, MAH.
MEsic (CZECH) Se MAH HOLD PERSIAN) joel gs),
| MJESIC (SERBIAN) 9 po MAH (PAHLAVI) 5 shy,
MESIC (BOHEMIAN) gus y MEH KURDISH) (53,5
MESIAC (SLOVAK) $1 U1 -MEY 4AFGHANI) (3.4) gli!
(LITHUANIAN) gl 3 MAN x(TOKHARIAN A) A 5 ,\55
MENUO, MENULIS MEM :(TOKHARIAN B) B .5,\55
MENESS LATVIAN) (3) gig MAS, MASAS —_«(SANSKRIT) <, Sts
MT HOLD IRISH) aS 543 p\ MENE, MEN (GREEK) li
MIS (WELSH) 53 MENA AGOTHIC) S35
MIZ ABRETON) 3.2 (OLD SCANDINAVIAN) 95 5-40!
MUAL ALBANIAN) git MANI
MANO —-{OLD SAXON) SiS
REFERENCES both MONA (OLD FRISIAN) «4S 52.5
POKORNY, SSS~*~*«SL: MANO:(OLD HIGH GERMAN) oS aT
BARNHART: (MOON) 676 MOND (GERMAN) glT
DELAMARRE: (LUNE) 186 MONA (OLD ENGLISH) eS p-sSil
MACKENZIE: (MOON) 124 MOON ENGLISH) cendSi\
BUCK: 54.55 MANE © (DANISH) lait
AMINDAROV: (MOON) 256 MANE SWEDISH) Gobype
yaar sbi ob, MANE NORWEGIAN) Pe sal
- MaaN TGR ure) ate
Jentloal
"Ye aaa Seed” pa)" Sty Chad” 9 4) WL" edly aul a te cltoks Abe?
1 ae 6 oa oe Ab tal pS eh bi Sel play sae cog yy! 24h dd
ails
ee
[pdf page 463]
(Sle parity SU att pe adele | TPF
age (OLD CHURCH SLAVIC) (5 53%! MAH, MA MAVESTAN) gles!
MISECI MAH (OLD PERSIAN) Jlen\y .g)\,
MIESIAC A(POLISH) Sling) (PAHLAVI) 5 gay
MESJAC, MIESIATS :(RUSSIAN) .o3) MAH, MAHAK, MAHIGAN
MEsic (CZECH) Soy MEH (KURDISH) 2,5
MESECU (BULGARIAN) «5,4, MYASHT (AFGHAND) (3-4) gsi!
MJESEC (SERBIAN) «9. p# MAN -(TOKHARIAN A) A 5,53
--- pdf tag
[pdf page 462]
```


## [2026-09-07T15:58:26.832Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -nE \"^mē-|^me-|^mētrom|^mēnos|^mēns|^mēnōt|^mētis\" IEC.txt | head -20"
}
```


### [2026-09-07T15:58:26.875Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T15:58:28.517Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mēnōt\\|menot\\|mēnes\" WLD_band3.txt | head -10; echo \"=== Bd2\"; grep -n \"^mē- 'messen'\\|mē-, messen\\|messen\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-07T15:58:28.569Z] TOOL RESULT

```
=== Bd2
12123:bhilo- etwa „in gutem Sinne ebenmaBig, angemessen, gut, freundlich“.
12128:sonennamen; ahd. bil-lrih „ebenma6ig, angemessen, geziemend^^; mhd.
12134:vermutlich, als Ableitung eines                   Yerbums ^bildn und               *biljan   „angemessen
14812:fugen“, ersteres fiir aisl. makr, ahd. gmah usw. und lit. megti ^angemessen.
15182:IP. 18,211 m. Lit.   als „zugemessenes“ zu lat. modus usw.).
15498:2,       me- „messen, abmessen“.
15504:           ma- „messen“, Ptc. -mda-^ -mdta-^ ap. fra-mdtar- „Gebieter‘^
15522:auch ? mafern „erhebe die Hand zum Schlage, werfe^^ („abmessen = zielen")
15524:   lat. mttior^ -i) /, mensus sum „messen,    abmessen, woven wohl mensa
15540:mPJe ,,KapP; aisl. m^la „messen“ (ein versch. Wort ist trotz Grienberger
```


## [2026-09-07T15:58:33.164Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15496,15512p' incoming/WLD/WLD_Bd2_pages.txt; echo \"--- leaf/printed\"; awk 'NR<=15498' incoming/WLD/WLD_Bd2_pages.txt | tr -cd '\\f' | wc -c; echo \"=== menot in Bd2\"; grep -n \"mēnōt\\|menot-\\|Monat, Mond\\|„Monat\" incoming/WLD/WLD_Bd2_pages.txt | head -5"
}
```


### [2026-09-07T15:58:34.494Z] TOOL RESULT

```
mann II ^ 3, 827).

2,       me- „messen, abmessen“.
     Ai. 7ndi/\  mimed i         mitd- „geniessen*\ matra^ mdtni- n.
mafia-       n. j.das Messen,              Ma6‘'    (
                                                        :   cech. m^^ri)^ mfdi- „Mab, richtige Erkennt-
nis‘*'    (=     gr. jurjjig,       lat.   meti-or^         ags.   mmd)^ ahhi-mnti- ^jlfachstellung, An-
schlag“, miti- „Ma6, Gewicht, Wert“,                                 prakr. mettam ds. (=ai. "^mitram)'^
           ma- „messen“, Ptc. -mda-^ -mdta-^ ap. fra-mdtar- „Gebieter‘^
     av. ap.
av. miti-  „MaB, Gewicht, ^yert‘^
   Gr. fxeTQov „Ma6^‘ (nach Brugmann I^ 635, 11^ 1, 342, IF. 18, 436 wie
ai. d-d-tra-m zu         anders Saussure Msl. 6, 246 ff.: idg. ^metrom aus
'^med-trom zur Wzf. med-; nicht nach Blankenstein Unt. 42, 111    von einer                  :



--- leaf/printed
241
=== menot in Bd2
17875:inenes- [mens-] der nom. sg. '^mens wurde            und menot „Monat'‘.
17883:Arm. St. I 18, Arm. Gr. I 417) amis, gen. amsoy „Monat“; gr.                     firivog
17885:va mit dems. Suffix        wie ^oelaovd^ oeliqvyf) ,,Mond“; alb.       „Monat'\
38589:Pfliicken geeignef', soil. „Monat‘'; formell unannehmbar Fick III^ 79; der-
```


## [2026-09-07T15:59:08.063Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://vajehyab.com/moein/متر' --note 'page 323, node 9: Mo\\047in entry for متر, origin tag [فر.] French' 2>&1 | tail -2; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg323.png data/verification/sources/refs/ocr/BOOK/323.png && ls -la data/verification/sources/refs/ocr/BOOK/323.png"
}
```


### [2026-09-07T15:59:09.691Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ba472cd5751ea060.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 72193 Sep  7 11:59 data/verification/sources/refs/ocr/BOOK/323.png
```


## [2026-09-07T15:59:12.679Z] TOOL CALL #81: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T15:59:12.717Z] TOOL RESULT

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


## [2026-09-07T15:59:24.280Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -nE \"^mē|^me[^a-z]|mētrom|mēnos|mēnō\" IEC.txt | head -20; echo \"--- try measure\"; grep -n \"measure'\" IEC.txt | head -8"
}
```


### [2026-09-07T15:59:24.342Z] TOOL RESULT

```
10411:mē (2) (me, men, mene, mone, mnë), acc. prn. *me' (dat. also in some languages) Skt. enclitic må, id.; Romani man, acc. & dat. id.; Av.màm, mā, id.; Ober, -mā, acc. id.; Oss. må, män, acc. & dat., id.; Gk. emé, mé, acc. id.; Doric cf. emín, emine, dat. id. (vocalism obscure); Alb. mue, mua, acc. & dat., id.; weak form: mé, id. (as Fr. moi: me); Lat. mē, acc. id.; Ligurian in Rumansch (?) enclitic:
10456:mēghos (1) ‘pleasant; pleasure’. Cf. WP II, 256 Skt. cf. mahinah "etad Ir. míog, m. ‘smile’ (cf. smég- for the Ir. doublet smíog, id.); OE cf. mægp (2) ‘desire’; Li. mëgüs ‘desirous’;
10468:meĝ- (məĝ-) ‘great, big’. Cf. meĝəlos, măĝ- (3). WP II, 257 Arm. mec, i, av, id.; Hitt. cf. mekkis, cpds. mak-, id. consonantism problematical; cf. also Hitt. makkess(mi) ‘become great; Myc. me- zo(n), mezana-, meki(s)ta- ‘greater; great-; greatest; Gk. mégas, n: méga, adj. ‘big, great’; méga, adv.; cf. meízoón ‘bigger’; mégistos “big- gest; Alb. (r-gde) i madh, f: e madhe, pl. té mëdhenj, fpl: të mëdhaja; Lat. magis, adv. ‘more’; Ir. cf. mi-adh (‘honour , if: Gk. mége- thos ‘greatness’: OBr. muoed ‘pride’); OBr. moi, mui, Br. mül, Cor. moy, W mwy, comp. (*more', fr. *megio-); ON mjok, adv. ‘greatly, very; almost. (The consonantism of Hitt. mekkis, and of Skt. mahá-, etc. is problemati- cal)
10469:me£olos, à (extn. of type me$-, q.v. and cf. mág- (3)). WP II, 257 Av. (?) cf. maroz ‘big’; Gk. megále, f. id. beside voc. sg. m: mégale, cpds: mégalo-; Oghamic maglus ‘prince’; MIr. mál, adj. ‘noble’; m. ‘prince’; Gaul. magalo-, magilo- ‘prince’; OBr. mael, m. “soldier”; Br. (?) mal? ‘smart, clever’; Go. mikils, E Fris. michel, MHG michel, OE micel, ON. mikill “big, great
10470:me$gont- ‘size, quantity’. Cf. me£-, etc. and unrelated moghont- Olr. mælt, Ir. méid, m. f. ‘quantity’; OW meint, W maint, f. ‘quantity, size, amount’; cf. cy- faint “how much’; Cor. kem-mys, ke-myns
10473:meëarg, ið “magnify, esteem, exaggerate’. Cf.
10474:me$£-, etc. Arm. mecarem ‘esteem, extol; Gk. megairo (?) ‘belittle, begrudge’, but cf. *smegros (sme- gero-); Olr. c£. maer, m. ‘nobleman’; OW maer, pl. meirri, m. *major-domo'
10487:me$oró, ið — méio
10522:meK-? Cf. māk- (3) and maK-, maĝ-, me?- Only thus in Hitt. mekkis ‘big, great. Note -kk-, but cf. mag-, etc. W maith, adj. ample, long’ and Lat. mactus ‘extolled’ are ambig. A formula of type *meKhis (máKh-) is no more than an attempt to reconcile the Hittite form mekkis, cpds: mak- “big, great" with Gk. mégas, Pamphylian méas, obl. meiálo-, from an al- leged mheial- according to A. Heubeck, with the forms represented by Skt. máhih, Av. maz-, Tokh. mak-, Phryg. maz-, Alb. i madh, and Lat. magis, maior, cf. *ekho (aKh-), *Khe- nus, *dhukhtër, etc.)
10610:mēnā ‘(epithet of) moon’. Cf. méns, etc. Lat. Ména ‘goddess of menstruation’; Gk. méné, f. ‘moon’; MHG mane, sf ‘moor be- side man, mone, id. (MHG mane is also a wf., but Go. mēna ‘moon’ is a wm., gs *ménins)
--- try measure
1527:bhorm- (bhormos, à, is, io) “burden; bearer, holder, container’. Cf. bhero Gk. phormós "basket, corn-measure'; Alb. barrë “load; Go. barms (i-st.); OHG OS barm ‘Jap’; OE bearm ‘lap; possession’; G (uml.) Berme (‘ramp of bulwark’. LW in Fr. berme, OFr. barme); ON cf. barmtog “haul-rope. (Isophonic forms, of uncertain kinship, are the following: Gk. phormís ‘faggot; Alb. barmë “inner bark’; Ger. Barm, Barmen ‘crowd, pack’; Barmen, Bärme ‘barm, yeast’; ON barmr ‘brim’; barmi ‘brother’; Ukr. brama sic ‘gate’). WP II, 164
2856:dheudhis, io “tube, pipe? (?) Gk. teuthís ‘cuttlefish; endive’; Ger. Teut "ttankard-measure'; MHG cf. Guten “blow, sound”
10066:WP II, 418. Cf. Iub- (3) & lubh- OE leap, m. ‘basket; peck-measure'; ON laupr “basket, box’; MHG cf. louft, sm. “shell, pod’; löufel, f. ‘nutshell’; Cz. Slovak, Srb. lub, m. “bark; casing’; R lub, gs -u, m. llime-bark'; cf. OCS lubinü, adj. “of bark’; Blg. lub ‘rim of sieve or drum’
10417:medo (1) measure, apportion, reward, deter- mine, fix’. WP II, 259 Oss. cf. ní-main, v., -mad, pp. (count; honour; Arm. met, gs meti, i-st. “moment; point; weight beside (mod.) met Cdue, measure’. Kerestegian); Hitt. mitaimi (metaimi) ‘fix, determine’; Gk. médo, fut. medésomai, v. ‘re- gulate, control" beside médomai ‘reflect, con- sider”; cf. medon, gs. -ontos ‘ruler, guardian’; médimnos 'bushet'; Lat. cf. (?) mereo, ere & mereor, eri “earn, deserve); mer-ces, gs -cédis (price paid', lit. ‘given measure'?); mers Ar merx, gs mercis, f. ‘thing, affair, goods’ cf. also mere-trix ‘whore’; meditor, åri ‘think, practice’. (The alternation of med- and mer- is of uncertain origin, but cf. meridiës, meren- da, mercëdonius mensis, where mer- repre- sents *medh-, and Mercurius, in which mer- seems to represent *med-); Osc. meřs ‘law’; med-díss, Latinized in meddix judge'; cf. Osc. a-miricatud ‘without reward’; mersto ‘just; Umb. cf. mersuva, f. adj. ‘right’; OIr. midiur, midim, v. ‘adjudge, measure, plan’; med, acc. sg. mid, f. ‘scale, balance? (also ‘measure, weight); Ir. meadhaim, v. ‘weight, assess; re- flect upon’; Go. mitan, sv 5 ‘measure’ beside mitón, denom. ‘think, ponder; MHG mézzen
10701:(mét-, see métis *measure', and next. For Lat. meta, if dialectal for *moita, see moit-, etc., in view of Li. miétas “post, pale’, etc.)
10976:modios, io (grain-measure'. See next, and cf. med- Lat. modius, m. id.; cf. MHG metze, f. ‘corn- measure as milling-fee'; Latv. maZs m. id. (LW in Ir. muidhe, f. jug; Gael. ‘churo’; MHG mut, müt, mutte, mütte)
12570:Vedic pad, pàd, m. id. beside pada, padbhis “on foot: Skt. padáh, ám, mn. ‘step, pace’, cf. pade pade ‘at every step’; pádyah, adj. “foot-?; padyà, f. ‘track’; Av. paiðya, f. ‘foot’; paiðyð, adj. “foot-?; páda, s. ‘land’; Ober pada-, s. ‘footing, step, station’; pada, s. ‘foot; Per. pay, s. ‘foot; paye, s. ‘ground, basis’; pà-, cpds.; Oss. fád ‘footstep’; fad ‘foot; fäz, adj. Cat, plain’, fr. *pedio-); fäzä ‘plain’; Tokh. A pe, B pai, s. ‘foot; Arm. het, hetk, g: hetoç, ab. -ovk ‘footstep’; het, adj. ‘last’; heti, he- tisn, adv. *on foot; heto ‘after’; Hitt. pedan, s. ‘place’; pedesi, adv. “on the spot’; (o-gde in) pata-, for *pada- ‘foot’; Gk. pezis, gs: pezidos, f. “foot, sole, edge’; pédé, péza, f. “foot, sole, base, edge, parapet'; pezós, adj. ‘pedestrian’; Myc. Gk. pédon ‘land’; pédoi, adv. *on the ground’; Aeol. Lesb. peda, Sapph. Dor. ped-, Arc. pe, prp. (after: Arm. het, heto); pesdàj, pezé, adv. “on foot; cf. hexá-pedos, adj. ‘six- footed’; (o-gde in) poús, gs: podós, m. ‘foot; Lat. pēs, gp: pedum, m. id.; peda f. ‘pace’, cf. also la-pes, -pidis (? “catch-fooP hence 'stone"); pedes, adv. “on foot; prope ‘near’; cf. also pro-pere, adv. (*quickly', if for *pro- pedi); peior, adj. ‘worse’; cf. op-pidum, n. ‘walled town’; LLat. acu-pedius 'swift-footed"; centi-pedium 'centipede'; Umb. peti, adv. “by the foot? beside perum, adv. (‘to the ground”, cf. Lat. pessum); Gallo-Lat. cand-etum, if for *cant-edom (*100-foot measure’. Thus R. Gar- nett 1843); Olr. ed, m. (a measure of distance’; cf. also éiss, f. (track, trace, fr. *pedsi-); ON fet, n. *pace, foot-measure'; fit, pl: fitjar, f. ‘webbed foot; ley’; Sw. fját, n. ‘footstep’; (o- gde in) OHG fuoss, OE fót, Du. voet, ON fótr, m. *foot'; Li. pedà, f. ‘sole, pace, foot- measure’; péde, pédZià, f. (stand, base’; pl. *stilts); -pedis, adj. (“*-fooP in cpds.); (o-gde in) pádas, m. “sole; threshing-floor; oven floor’; Latv. pēda, f. ‘sole, footstep, track’; pec, prp. (for *pēds 'after); (o-gde in) pads, m. ‘floor. Verbal extns. in Av. paióye(imi), v. *go'; Hitt. pedahi, v. ‘fetch’; Gk. pedáo, v. ffet- ter beside o-pédéo, v. (false ‘Doric’: opadéo) (follow, attend’, if for *soqu-ped-); ON feta, sv. 3 ‘step’ beside fzeta (here?) “have dealings with’; OHG cf. gi-fezzan, v. “collapse, decay’;
15131:seiquos, à (seikos, a?) 'sifting-basket, seed- lip’. Cf. seiqu-, soiqu- OHG cf. siha, f. ‘sieve’; LG Sih, f. id.; Li. siekas, saikas, m. “basket; a grain-measure'; cf. seikiu, e. v. ‘measure by capacity’; Latv. sieks, m. (a capacity measure). (Hybridism is possible between a type *seik- and a type *seiqu-)
```


## [2026-09-07T15:59:29.384Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -nE \"^mētis|^méns|^mēns|^métis|^mèns\" IEC.txt | head; echo \"---\"; sed -n '10695,10712p' IEC.txt; echo \"=== mens\"; grep -n \"méns, \" IEC.txt | head -3"
}
```


### [2026-09-07T15:59:29.453Z] TOOL RESULT

```
10706:métis ‘measure, judgment. metros, mot-
---
40
45
762
stout; OE mæst, m. ‘mast’, i.e. ‘acorns, beechnuts'; maestan, v. ‘fatten — animals’; G cf. also Mast-darm ‘gut. (Gmc. forms fr. *mast-, or fr. *most-)
met (metm) (1) *by, with, after" WP II, 236 Skt. cf. agni-mát (fiery, but cf. mnt-. Am- big.); Av. mat, prep. & postp. ‘by, witht’; Arm. -me, suff. in ont at-me “on the right; i çax- me “on the left; Myc. cf. meta, w. dat. ‘with’; Gk. metá, w. gen. ‘with’; dative “among”; ac- cus. ‘after’; cf. also mét-eimi "be with’; Alb. me, prep. ‘with’; Lat. ego-met, emph. ‘I my- self; sua-met ‘by its own force’; Umb. cf. pus- me ‘to whom’; Go. mip, mid, OHG miti, mit, OE mid, ON meór, með ‘with’. In sense from" cf. Skt. mat ‘from me’ (abl. sg. inflectn.)
met (meti) (2) “till, as far as'. (Same as (1)?) Thess., Gk. dial. mes, id. beside més-pha, -podi, id.; Arm. (ambig.) -me, in im-mg (“from my ..: but cf. met (1); NAIb. mje ‘till’; Umb. cf. pus-me, prn. ‘to whom’; W med, prep. ‘to, as far as”
(mét-, see métis *measure', and next. For Lat. meta, if dialectal for *moita, see moit-, etc., in view of Li. miétas “post, pale’, etc.)
metaàio (freq. of type meto, q. v.) ‘fling, cast". See next Lat. cf. castra-metor, -metaris ‘pitch camp’; OCS (and com. Sl.) razmëtajo “cast about: Cz. roz-mitat, inf. wd: Latv. metàju, id.
metolos, à (metil-) ‘cast, throw, dash, throw- ing-instrument',. See next Lat. metula, metila & metella “basket of stones to throw down on attackers’; OCS metla ‘lash’; Slovak metla ‘lash; besom’ (and com. SI). (For Slovak metel ‘snowstorm? see ment(h)-)
metoris, à ‘missile. (Celtic variant of type metolos, q. v.). Cf. WP II, 230 Gallo-Lat. mataris, matara, f. *pike, javelin', fr. Se, + *-o- as under geronos, q.v.)
(meti, see met (1) & (2))
métis ‘measure, judgment. metros, mot-
Skt. màtib, f. id.; Arm. mitK, gen. mtac, ab. mtawk (pl. form) ‘mind’; Gk. métis, gs -ios & -idos, f. wisdom, judgment; Alb. mot, m. (obs. *time'; mod. “year, weather); Lat. cf.
Cf. metos,
763
métior, -iri, v. ‘measure, judge’; OE m&pþ, f. “measure, degree, right, lot, rank, respect; OS cf. math-mundi, adj. “gentle, kind"; Finn. LW miete ‘though?
meto, ið (metaio, met-) “sweep, cast, fling, scythe, mow, reap’. WP II, 259 Lat. meto, ére ‘mow, reap’; OBr. met-, id.; Br. médi, midi, inf. id.; cf. koat-méd “forest clearing’; W medi, inf. ‘reap’; Cor. mejy, mijy, id.; Ir. cf. meitheamh, m. ‘June’; meitheal, m. “band of reapers; OE mæb, n. s. ‘mowing, matb’; MHG màde, wf. id.; G cf. maden ("fer- tilizze w. mud'. Gmc. forms with *-&-); OCS meto, mesti ‘sweep; throw? beside metajo, metno, v. ‘throw’; Li. metu, mesti, v. id.; cf. metus, adj. ‘restive’; Latvian metu, mest, v. as Li. Cf. métos
metos (1) “measure, estimate, period, year. Cf. motos, métis, metros. WP II, 237. (Ir. am- big. cf. med-) Lat. cf. metellus, m. ‘mercenary’; MIr. cf. mess *judgment, estimate’; Li. métas ‘time’; métai, pl. ‘year’; Latv. mets “age, project, quality, essence’
=== mens
10610:mēnā ‘(epithet of) moon’. Cf. méns, etc. Lat. Ména ‘goddess of menstruation’; Gk. méné, f. ‘moon’; MHG mane, sf ‘moor be- side man, mone, id. (MHG mane is also a wf., but Go. mēna ‘moon’ is a wm., gs *ménins)
10656:ménulos, ios ‘moon; of the moon’. Cf. méns, etc. Hiero-Hitt. ménulas ‘moon’; Li. menülis, gs. -jo, m. id.
```


## [2026-09-07T15:59:35.721Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:06:28.802Z] TOOL CALL #84: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk323.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nS_PIE   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meh₁-\"\nS_MAH   = \"https://en.wiktionary.org/wiki/ماه\"\nS_MHT   = \"https://en.wiktionary.org/wiki/مهتاب\"\nS_FRM   = \"https://en.wiktionary.org/wiki/فرمان\"\nS_PYM   = \"https://en.wiktionary.org/wiki/پیمودن\"\nS_NMD   = \"https://en.wiktionary.org/wiki/نمودن\"\nS_AZM   = \"https://en.wiktionary.org/wiki/آزمودن\"\nS_METRO = \"https://en.wiktionary.org/wiki/μέτρον\"\nS_METR  = \"https://en.wiktionary.org/wiki/متر\"\nS_ETY   = \"https://www.etymonline.com/word/meter\"\nS_MON   = \"https://vajehyab.com/moein/متر\"\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Me 2\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *meh₁- 'to measure' (Pokorny mē-3, pp. 703–704), with the extended stem *mēh₁-n-ōt- / *mḗh₁n̥s 'moon, month' (Pokorny mēnōt, pp. 731–732)\",\n  \"note\": \"Root, language label and both glosses are right. Nourai's chart label 'Me 2' and the pair of Pokorny page numbers are lifted straight from Watkins/AHD, whose entry reads 'mē-2. To measure. Contracted from *meə-. … [Pok. 3. mē- 703, mēnōt- 731.]' — i.e. exactly POK:703 + POK:731. Pokorny 703–704 has 'Root/lemma: mē-3, m-e-t-: to measure' with Av./OP mā- 'measure', OP fra-mātar- 'lord, master', Gk. métron, Lat. mētior, Gmc. *mēlaz, Toch. A me- 'measure'; Pokorny 731–732 has 'Root/lemma: mēnōt, Gen. mēneses … Meaning: month; crescent … Note: probably as personified \\\"time measurement\\\" to mē- \\\"measure\\\"', listing 'Old Indic mās, māsa-, Avestan mā(h), npers. māh \\\"moon, month\\\"'. So Nourai's second head-form 'Měnôt: moon used to measure time' reproduces Pokorny's lemma and Pokorny's own note about the motivation. The only modernisation needed is notational: today the root is written with the laryngeal, *meh₁-; Wiktionary records a minority view (Kortlandt) that *meh₁- is a phonetic variant of *med- 'to measure, take appropriate measures'.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *meh₁- «اندازه گرفتن، پیمودن» (پوکورنی ذیل mē-3، صص ۷۰۳–۷۰۴) و ستاک گستردهٔ آن *mḗh₁n̥s / *mēh₁-n-ōt- «ماه (قمر)، ماه (شهر)» (پوکورنی ذیل mēnōt، صص ۷۳۱–۷۳۲). نام «Me 2» و هر دو شمارهٔ صفحهٔ پوکورنی که نورایی آورده، عیناً از فرهنگ ریشه‌های هندواروپایی واتکینز (AHD) گرفته شده است که ذیل mē-2 «اندازه گرفتن» به «Pok. 3. mē- 703, mēnōt- 731» ارجاع می‌دهد. پوکورنی خود در ذیل mēnōt یادآور می‌شود که این واژه گویا «سنجهٔ زمان» شخصیت‌یافته و برگرفته از mē- «اندازه گرفتن» است؛ پس تعبیر نورایی («ماه، ابزار سنجش زمان») درست است. تنها اصلاح لازم نگارشی است: امروز ریشه را با حنجره‌ای *meh₁- می‌نویسند. ادعای نورایی درست است.\",\n  \"sources\": [S_PIE],\n  \"ref_check\": [\n    {\"ref\": \"POK:703\", \"status\": \"supports\", \"note\": \"POK_full.txt (grep -n 'lemma: me-3'): 'Root / lemma: me-3, m-e-t- | Meaning: to measure … Avestan ap. mā- \\\"measure\\\", participle -mīta-, -māta-, ap. fra-mātar- \\\"lord, master\\\" … Gr. μέτρον \\\"measure\\\" … Latin metior … Page(s): 703-704'.\"},\n    {\"ref\": \"POK:731\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: mēnōt, Gen. mēneses, from which mēnes-, mēns-, mēs-, mēn- | Meaning: month; crescent | Note: probably as personified \\\"time measurement\\\" to mē- \\\"measure\\\" | Material: Old Indic mās, māsa- m., Avestan mā(h), Gen. mā̊ŋhō, npers. māh \\\"moon, month\\\" … Page(s): 731-732'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. mē-2\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt: 'mē-2. To measure. Contracted from *meə-. I. Basic form mē-. 1. Suffixed form *mē-lo- in Germanic *mēlaz in Old English mǣl … MEAL²; PIECEMEAL. 2. Suffixed form *mē-ti- in Latin mētīrī, to measure: MEASURE, … DIMENSION, IMMENSE. 3. Possibly Greek metron … II. Extended and suffixed forms *mēn-, *mēn-en-, *mēn-s-, *mēn-ōt-, moon, month … [Pok. 3. mē- 703, mēnōt- 731.]' — the source of Nourai's whole chart.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 237 f. and II 271 f.\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt: '2. mē- „messen, abmessen“. Ai. māti, mímāti … mātrā … av. ap. mā- „messen“, Ptc. -māta-, ap. fra-mātar- „Gebieter“ … Gr. μέτρον „Maß“ (… anders Saussure MSL 6, 246 ff.: idg. *metrom aus *med-trom zur Wzf. med-)'; and at II 271 'mēnes- [mens-] … und mēnōt „Monat“'. Pokorny cites exactly 'WP. II 237 f.' and 'WP. II 271 f.'\"},\n    {\"src\": \"SYN\", \"where\": \"p. 54 (§1.53 MOON) and p. 1010 (§14.71 MONTH)\", \"stance\": \"supports\", \"note\": \"Buck: 'IE *ménes-, *mén(n)s- \\\"moon\\\" and \\\"month\\\", presumably fr. *mē- \\\"measure\\\"' (1.53); '*ménes-, *mē(n)s- \\\"moon\\\" and \\\"month\\\", prob. fr. *mē \\\"measure\\\"' (14.71).\"},\n    {\"src\": \"IEC\", \"where\": \"pp. 762-763\", \"stance\": \"partial\", \"note\": \"Mann has no verbal root *mē-; the family is split among nominal head-words: 'métis \\\"measure, judgment\\\" … Lat. métior, -iri … OE mæþþ \\\"measure\\\"', 'metos (1) \\\"measure, estimate, period, year\\\"', 'mēnā \\\"(epithet of) moon\\\"', 'ménulos \\\"moon\\\"'. Same material, different arrangement.\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"].append\n\nN({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"mâ 1; mâh, mâhya; mâh-tab\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Av./OP mā(y)- 'to measure' is the direct outcome of PIE *meh₁-: the long ā of Indo-Iranian *mā- is the regular reflex of *meh₁ before a consonant, and the y-present maya- shows the laryngeal-hiatus filler (Bartholomae, AiW col. 1166: '¹mā(y)- V. \\\"messen\\\". Praes. maya-; Perf. mim-. PPfP. mita-, mīta-, māta-'; Kent, Old Persian p.201: 'mā- vb. \\\"measure\\\": Av. Skt. mā-, Lt. mētior \\\"I measure\\\"'). Av. māh- (nom. mā, gen. mā̊ŋhō) 'moon, and month' and OP māh- 'month' go back not to the bare root but to the s/t-extended stem *mḗh₁n̥s ~ *mēh₁-n-es-, Indo-Iranian *mā́Hah, with the regular Iranian development *-ns- > -h- (cf. Skt. mās-, Gk. mḗn, Lat. mēnsis); this is Pokorny's separate lemma mēnōt, which he himself derives from mē- 'measure', so Nourai's arrow root→node is sound. Av. māhya- (attested in the compound xšvaš.māhya- 'six-monthly', AiW 562) is the adjectival derivative and justifies Nourai's second citation form. The third item, 'mâh-tab: moonshine', is the weak link: no Avestan or Old Persian compound *māh-tāp- is attested. Persian مهتاب is a New Persian compound of مه/ماه + تاب (present stem of تافتن 'to shine', from Iranian *tāp-, Nourai's root Tep), i.e. it belongs one box lower, in the Persian node, where Nourai also (correctly) prints it. Placing it in the Avestan/Old Persian box is an anachronism, not a wrong etymology.\",\n \"derivation_fa\": \"ستاک اوستایی و پارسی باستان mā(y)- «اندازه گرفتن» بازماندهٔ مستقیم ریشهٔ هندواروپایی *meh₁- است؛ آی کشیدهٔ هندوایرانی *mā- دستاورد قاعده‌مند *meh₁ در برابر همخوان است و ستاک حالِ maya- نشانهٔ همان حنجره‌ای است (بارتولومه، ستون ۱۱۶۶؛ کنت، فارسی باستان ص ۲۰۱). واژهٔ اوستایی māh- (فاعلی mā، اضافی mā̊ŋhō) و پارسی باستان māh- «ماه» نه از خودِ ریشه، بلکه از ستاک گسترده‌ٔ *mḗh₁n̥s (هندوایرانی *mā́Hah) می‌آید؛ در ایرانی *-ns- به قاعده به -h- بدل شده است (قس سنسکریت māsa-، یونانی mḗn، لاتینی mēnsis). صفت اوستایی māhya- نیز در ترکیب xšvaš.māhya- «شش‌ماهه» گواه دارد. اما بند سوم، «mâh-tab»، لغزش است: هیچ ترکیب اوستایی یا پارسی باستانِ *māh-tāp- در دست نیست؛ «مهتاب» ترکیبی فارسی نو از «مه/ماه» و «تاب» (ستاک حال تافتن) است و جای آن همان خانهٔ فارسیِ پایین‌تر است که نورایی خود هم آورده. پس ادعای نورایی درست است مگر در جای‌گذاری «مهتاب» که یک دورهٔ زبانی زودتر نشانده شده است.\",\n \"sources\": [S_PIE, S_MAH, S_MHT],\n \"ref_check\": [\n   {\"ref\": \"POK:703\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. mē-3: 'Avestan ap. mā- \\\"measure\\\", participle -mīta-, -māta-, ap. fra-mātar- \\\"lord, master\\\", Avestan miti- \\\"measure, weight, value\\\"'.\"},\n   {\"ref\": \"POK:731\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. mēnōt (pp.731-732): 'Old Indic mās, māsa- m., Avestan mā(h), Gen. mā̊ŋhō, npers. māh \\\"moon, month\\\"'.\"},\n   {\"ref\": \"SYN:54\", \"status\": \"supports\", \"note\": \"SYN.txt §1.53 MOON (printed p.54): table gives 'Av. mah-' and the discussion 'Skt. mās- …, Av. mah- (OPers. mah- \\\"month\\\"), NPers. mah-'; 'IE *ménes-, *mén(n)s- … presumably fr. *mē- \\\"measure\\\"'.\"},\n   {\"ref\": \"SYN:877\", \"status\": \"supports\", \"note\": \"SYN.txt §12.54 MEASURE (vb.), printed p.877-878: table lists 'Skt. mā-, Av. mā-'; discussion 'All the words for \\\"measure\\\" are from Skt., Av. mā-; … Walde-P. 2.237'.\"},\n   {\"ref\": \"SYN:1010\", \"status\": \"supports\", \"note\": \"SYN.txt §14.71 MONTH, printed p.1010: 'Av., OPers. mah-' in the table; 'IE *ménes-, *mē(n)s- \\\"moon\\\" and \\\"month\\\", prob. fr. *mē \\\"measure\\\"'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1166 s.v. ¹mā(y)-; col. 1170 s.v. māh-; col. 562 s.v. xšvaš.māhya-\", \"stance\": \"partial\", \"note\": \"AiW col. 1166: '• j., g. (,p.) ¹mā(y)- V. \\\"messen\\\". Praes. maya-; Perf. mim-. — PPfP. mita-, mīta-, māta-'; col. 1170: '• j., g., p. māh- m. 1) \\\"Mond\\\", auch als Gottheit … 2) \\\"Monat\\\"'. Bartholomae has mā- and māh- but no compound *māh-tāp- anywhere — hence 'partial'.\"},\n   {\"src\": \"KNT\", \"where\": \"p. 201 s.v. mā-\", \"stance\": \"supports\", \"note\": \"KNT.txt: 'mā- vb. \\\"measure\\\": Av. Skt. mā-, Lt. mētior \\\"I measure\\\". ā + mā- \\\"extend\\\" … fra- + mā- \\\"command\\\"' — Old Persian root confirmed.\"},\n   {\"src\": \"ARY\", \"where\": \"printed pp. 463-464 (pdf 462-463), entry ماه\", \"stance\": \"supports\", \"note\": \"ARY_latin_index_pages.txt: the ماه entry equates 'MAH, MA (AVESTAN) … MAH (OLD PERSIAN) … MAH, MAHAK, MAHIGAN (PAHLAVI) … MENE, MEN (GREEK) … MENA (GOTHIC) … MOON (ENGLISH)' and cites 'POKORNY … BARNHART: (MOON) 676 … MACKENZIE: (MOON) 124 … BUCK: 54, 55'.\"}\n ]\n})\n\nN({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"mâh «ماه»; mahtâb «مهتاب»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP ماه māh 'moon; month' continues MP māh (Book Pahlavi written with the Aramaic ideogram BYRH beside phonetic mh; MacKenzie, CPD p.53: 'māh [BYRH < A b-yrḥ; mh] moon, month; cal. 12th day'), from OP/Av. māh-, Proto-Iranian *māHah < PIE *mḗh₁n̥s. The word has been phonologically inert since the Old Iranian period: long ā is preserved, and final -h is the reflex of the old s-stem, so Nourai's single arrow Av./OP → NP is exactly right. مهتاب mahtāb 'moonlight' is a New Persian compound, mah- (the shortened combining form of ماه) + تاب tāb, the present stem of تافتن 'to shine, glow' (MP tāftan, tāb-, from Iranian *tāp-, Nourai's root Tep) — Mo'in's footnote in Borhan-e Qate' p.1958 spells this out. Semantically 'moon-shining' > 'moonlight' > (by metonymy) 'the moon itself'.\",\n \"derivation_fa\": \"«ماه» فارسی نو ادامهٔ māh فارسی میانه است (در پهلوی کتابی با هزوارش BYRH و نیز به‌صورت آوایی mh؛ مکنزی، فرهنگ کوچک پهلوی ص ۵۳: «māh: moon, month»)، و آن از māh- پارسی باستان/اوستایی، ایرانی باستان *māHah و سرانجام هندواروپایی *mḗh₁n̥s. این واژه از دورهٔ ایرانی باستان تا امروز دگرگونی آوایی نیافته است: آی کشیده برجاست و های پایانی بازماندهٔ ستاک s است؛ پس یک پیکان از اوستایی/پارسی باستان به فارسی نو، چنان‌که نورایی کشیده، درست است. «مهتاب» ترکیبی فارسی نو است از «مه» (صورت کوتاه‌شدهٔ ماه در ترکیب) و «تاب» (ستاک حال تافتن، از فارسی میانهٔ tāftan/tāb-، ایرانی *tāp-)؛ حاشیهٔ معین بر برهان قاطع ص ۱۹۵۸ همین را می‌گوید: «مهتاب (مخفف) از: ماه + تاب (گرمی، نور) لغةً بمعنی نور ماه و مجازاً جرم ماه». ادعای نورایی درست است.\",\n \"sources\": [S_MAH, S_MHT, S_PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:731\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. mēnōt: '… npers. māh \\\"moon, month\\\"' — Pokorny lists the New Persian form itself.\"},\n   {\"ref\": \"BQT:1956\", \"status\": \"supports\", \"note\": \"BQT vol.4 pdf p.39 (= printed ~1955-1956), headword ماه, Mo'in's footnote: 'سمانگه (ه.م.) ورك: ماس, ماج. دراوستا وپارسی‌باستان … سانسکریت māsa (ماه، قمر)، کردی māng (قمر؛ شهر)' followed by his long excursus 'ماه در ایران باستان'.\"},\n   {\"ref\": \"BQT:1958\", \"status\": \"supports\", \"note\": \"BQT vol.4 pdf p.41 (printed 1958), footnote: '#مهتاب ( مخفف ) از : ماه (ه.م ) + تاب ( گرمی ، نور ) لغة بممتی نور ماه و مجازاً جرم ماه' — exactly Nourai's māh + tāb (☞Tep).\"},\n   {\"ref\": \"SNS:37\", \"status\": \"partial\", \"note\": \"SNS_pages.txt index line 'xšvaš. mahya- 37/9' and the glossary entry '(AiWb. 562) xšvaš. mahya-' — i.e. Nourai's 37 points to the Avestan xšvaš.māhya- 'six-monthly' cited in Tavoosi's glossary, which underlies his form 'mâhya' (node #1) rather than NP māh; the OCR of this book is too poor to read the surrounding page.\"},\n   {\"ref\": \"SNS:113\", \"status\": \"partial\", \"note\": \"SNS_pages.txt index line 'mah- 113/2' — the glossary does index a form mah- at text 113/2, so the citation is real, but the Persian/Pahlavi OCR is unreadable and the printed page numbers could not be recovered.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 53 s.v. māh\", \"stance\": \"supports\", \"note\": \"PHD.txt: 'māh [B YRH < A b-yrh; mh] = M, N ~] moon, month; cal. 12th day' — MacKenzie explicitly equates the Manichaean and New Persian forms with MP māh.\"},\n   {\"src\": \"HRN\", \"where\": \"silent for māh/mahtāb\", \"stance\": \"silent\", \"note\": \"grep -n 'mahtab\\\\|mähtäb\\\\|mäh ' HRN.txt returns no numbered entry for māh or mahtāb; Horn treats only the verbal compounds of mā- (nos. 21, 363, 1042).\"},\n   {\"src\": \"ARY\", \"where\": \"printed pp. 463-464, entry ماه\", \"stance\": \"supports\", \"note\": \"Aryanpur's ماه entry lists the whole IE moon/month family (Avestan MAH/MA, OP MAH, Pahlavi MAH/MAHAK/MAHIGAN, Gk MENE, Lat. via MESECU etc., Eng. MOON) with references 'POKORNY … MACKENZIE: (MOON) 124 … BUCK: 54, 55'.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab, s.v. مهتاب/ماه\", \"stance\": \"supports\", \"note\": \"Mo'in's dictionary gives ماه without a foreign-origin tag (native Iranian) and مهتاب as the compound 'نور ماه'.\"}\n ]\n})\n\nN({\n \"id\": 3, \"lang\": \"Old Persian\",\n \"words\": \"fra-ma-na; â-mâ\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both are prefixed formations on the OP verb mā- 'to measure' and both are attested in the Achaemenid inscriptions. (a) framānā- f. 'command' (DNa 57, DNb 28, DSj 3, isf. framānāyā DNb 37) = fra- 'forth, before' + mā- + the abstract suffix -nā-, literally 'a measuring-out beforehand' > 'ordinance, decree'; the compound verb fra-mā- is glossed 'command' ('decide, judge' per Herzfeld) and yields also framātar- 'master, lord' ('giver of judicial decisions'). Kent compares Skt. pramāṇa-m 'measure, standard', which is the same compound in Indic and clinches the semantic path measure > decide > order. (b) ā + mā- 'extend', attested in the past participle āmāta- (npm. āmātā, DB 1.7, DBa 11) used substantivally 'noble' — 'of extended (i.e. long-measured) lineage'. Nourai's glosses 'to measure beforehand, decide, order' and 'extend' are Kent's own wording.\",\n \"derivation_fa\": \"هر دو صورت، ساخت‌های پیشوندی فعل پارسی باستان mā- «اندازه گرفتن» است و هر دو در سنگ‌نوشته‌های هخامنشی گواه دارد. یک) framānā- «فرمان» (DNa ۵۷، DNb ۲۸، DSj ۳) از پیشوند fra- «پیش، فراپیش» + mā- + پسوند سازندهٔ اسم معنی -nā-، یعنی «پیش‌اندازی، از پیش سنجیدن» و از آنجا «حکم، دستور»؛ همین ستاک framātar- «سرور، فرمانده» را هم می‌سازد. کنت آن را با pramāṇa-m سنسکریت «اندازه، معیار» می‌سنجد که همان ترکیب در هندی باستان است و زنجیرهٔ معنایی «سنجیدن ← داوری کردن ← فرمان دادن» را روشن می‌کند. دو) ā + mā- «کشیدن، گستردن» که در صفت مفعولی āmāta- (در DB ۱٫۷ و DBa ۱۱) به معنی «نژاده» به کار رفته، یعنی «دارای تبار درازْ‌اندازه». تحول معنایی و ساخت هر دو، همان است که نورایی آورده؛ ادعای نورایی درست است.\",\n \"sources\": [S_FRM],\n \"ref_check\": [\n   {\"ref\": \"KNT:201\", \"status\": \"supports\", \"note\": \"KNT.txt, Lexicon p.201 (the block ends with the running head '202 OLD PERSIAN'): 'mā- vb. \\\"measure\\\": Av. Skt. mā-, Lt. mētior \\\"I measure\\\". ā + mā- \\\"extend\\\": āmātā npm. past ptc. pass. \\\"noble\\\" DB 1.7; DBa 11. fra- + mā- \\\"command\\\" (\\\"decide, judge\\\", acc. to Hz. ApI 154-6; \\\"plan,\\\" Hinz, ZDMG 95.233-5); see also framātar-, framānā-.' Both of Nourai's forms and both glosses are on the cited page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"pp. 198-199 s.v. framātar-, framāna-\", \"stance\": \"supports\", \"note\": \"KNT.txt: 'framāna- sb. \\\"command\\\" (judgment, decision, acc. to Hz. ApI 144-50): Phl. framān, NPers. fārmān; fra- + mā- + suffix -nā- (§128, §147.I), cf. Skt. pramāṇa-m \\\"measure, standard\\\". framānā nsf. DNa 57; DNb 28; DSj 3, framānāyā isf. DNb 37.'\"},\n   {\"src\": \"BRT\", \"where\": \"col. 1166 s.v. ¹mā(y)-, sub 'mit ā' and 'mit frā'\", \"stance\": \"supports\", \"note\": \"AiW: 'mit ā Med. \\\"sich erproben, als tüchtig erweisen\\\" … hacā paruviyata ā-mātā amahy \\\"vor Alters haben wir uns als tüchtig erwiesen\\\" Bh. 1.3'; 'mit frā 1) \\\"als Norm aufstellen, anordnen, befehlen\\\": … framīmaθā … Y.32.4'. Bartholomae reads OP ā-mātā as 'proved worthy' rather than Kent's 'noble/extended', a difference of gloss only.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 237\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt s.v. 2. mē-: 'av. ap. mā- „messen“, Ptc. -mīta-, -māta-, ap. fra-mātar- „Gebieter“'.\"}\n ]\n})\n\nN({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"farmân «فرمان»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"OP framānā- > MP framān > NP فرمان farmān 'order, decree' — a straight line with only the ordinary Middle-to-New Persian changes: initial fra- > far- (anaptyxis breaking the fr- cluster, as in fra-bara- > farbar, frāz > farāz), loss of the final vowel, and shortening of the abstract suffix. MacKenzie records 'framān [plmʾn' | M frmn, N farmān] order, command'. The chart's extra Persian forms in the box belong to the same MP verb framūdan, framāy-: فرمودن < MP framūdan < Iranian *fra-mā-ta- (Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p.66: 'فرمود < فارسی میانه framūd/framād < ایرانی باستان *fra-mā-ta … mā ریشه است به معنی اندازه گرفتن'; the present stem farmāy- < *fra-mā-ya-), فرمایش the verbal noun, فرمانده = farmān + deh 'giver of orders'. The word travelled outward as well: Ottoman Turkish ferman, Arabic فرمان/فرامين, and via Turkish into English 'firman' — a Persian export, not a loan.\",\n \"derivation_fa\": \"زنجیره یکدست است: پارسی باستان framānā- ← فارسی میانه framān ← فارسی نو «فرمان». دگرگونی‌ها همان تحولات معمول میانه به نو است: پیشوند fra- با میانجی‌گیریِ واکه به far- بدل شده (قس frāz > فراز) و واکهٔ پایانی افتاده است. مکنزی: «framān [plmʾn'] order, command». صورت‌های افزودهٔ همان خانه نیز از همین ستاک‌اند: «فرمودن» از framūdan فارسی میانه و ایرانی باستان *fra-mā-ta (ابوالقاسمی، فعل‌های فارسی دری ص ۶۶: «فرمود < فارسی میانه framūd/framād < ایرانی باستان *fra-mā-ta … mā ریشه است به معنی اندازه گرفتن»)، ستاک حال «فرمای» از *fra-mā-ya-؛ «فرمایش» اسم مصدر و «فرمانده» از فرمان + دِه. این واژه سپس معرّب شد («فرمان»، جمع «فرامین») و از راه ترکی عثمانی به انگلیسی firman رفت؛ یعنی وام‌دهنده است نه وام‌گیرنده. ادعای نورایی درست است.\",\n \"sources\": [S_FRM],\n \"ref_check\": [\n   {\"ref\": \"BQT:1470\", \"status\": \"supports\", \"note\": \"BQT vol.3 pdf p.262 (printed ~1470), Mo'in's footnote s.v. فرمان: 'فرمان — بفتح اول، اسم از «فرمودن»؛ پهلوی framān (امر)، ایرانی باستان *fra-mā-na «بارتولمه ۱۱۸۸» … ارمنی hraman «هوبشمان ۸۲» … معرب آن «فرمان» و جمع عربی «فرامین»؛ حکمی که از جانب شخصی بزرگ صادر گردد'.\"},\n   {\"ref\": \"FFD:66\", \"status\": \"supports\", \"note\": \"FFD_pages.txt pdf p.71 = printed p.66: 'فرمودن — فرمود « فارسی میانه framūd + framād < ایرانی باستان *fra-mā-ta. fra پیشوند فعلی است. mā ریشه است به معنی «اندازه گرفتن» … فرمای < فارسی میانه framāy < ایرانی باستان *fra-mā-ya'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 32 s.v. framān, framūdan\", \"stance\": \"supports\", \"note\": \"PHD.txt: 'framān [plmʾn' | M frmn, N farmān] order, command; a minor degree of sin. ~-burdār … framūdan, framāy- [plmwtn', plmʾd- | M prmʾdn, prmy-, N far~] order, command.'\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.v. framūtan\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt cross-references 'framūtan' under the perfective particle bē ('also used in other expressions implying an act of will, cf. apāyistan and framūtan'), confirming the MP infinitive framūtan/framūdan.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien no. 82 (cited by Mo'in)\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote at BQT 1470 cites Hübschmann p.82 for Armenian hraman as a borrowing from the Iranian framān — an independent witness to the MP form.\"}\n ]\n})\n\nN({\n \"id\": 5, \"lang\": \"Avestan\",\n \"words\": \"paiti-mâ; âiz-mâ, uz-mâ-ta; ni-mâ\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"âiz-mâ, uz-mâ-ta\",\n \"correct_form\": \"âuz-mâ (i.e. *ā-/ava- + uz- + mâ-), uz-mâ-ta\",\n \"derivation\": \"The three items are the prefixed pre-forms that the Persian verbs of node #6 presuppose, and Bartholomae himself groups them under the root: at AiW col. 1166, under ¹mā(y)- 'messen', he notes 'np. patmāyad \\\"er misst\\\", nimāyad \\\"er zeigt\\\", āzmāyad \\\"er erprobt\\\"' and the Pahlavi-version glosses 'ezmāyūn', 'nimūti', 'paitimā(i)' — i.e. paiti-mā-, uz-mā-, ni-mā- are recognised Iranian compounds of mā-, even though Avestan itself attests only the simplex and the frā-compound (framīmaθā, Y.32.4). Two caveats. (1) The bare Avestan compounds *paiti-mā-, *ni-mā- are reconstructions from Middle Persian, not quoted Avestan text; Bartholomae's ²mā- f. 'Maß' is glossed in the Pahlavi version by patmān, which is the actual evidence. (2) The form 'âiz-mâ' printed in the book (and faithfully extracted) is not a possible Iranian shape. Horn no. 21 derives āzmūdan from 'aw. *ā (oder nach dem Pehlevi wohl ava) + uz + √mā-', i.e. *ā-uz-mā- / *ava-uz-mā-; Abolghasemi (FFD 25) has simply *uz-mā-ta with ā- restored by analogy. So the book's 'âiz-' should be 'âuz-' (ā+uz), with -uz- the preverb 'up, out'. The printed page 323 (see data/verification/sources/refs/ocr/BOOK/323.png) shows 'âiz-mâ' plainly: the misprint is Nourai's, not the extraction's. Nourai's second item 'uz-mâ-ta' is exactly the form the modern handbooks give, so the two variants in his box are really the same compound with and without the ā-.\",\n \"derivation_fa\": \"این سه صورت، ساخت‌های پیشوندیِ پیش‌فرضِ فعل‌های فارسی خانهٔ بعد است و بارتولومه هم آنها را زیر همین ریشه می‌آورد: در ستون ۱۱۶۶ فرهنگ ایرانی باستان، ذیل ¹mā(y)- «سنجیدن»، می‌نویسد «np. patmāyad، nimāyad، āzmāyad» و گزارش‌های پهلوی «ezmāyūn، nimūti، paitimā(i)» را نیز نقل می‌کند؛ یعنی paiti-mā-، uz-mā-، ni-mā- ترکیب‌های شناخته‌شدهٔ ایرانی‌اند، هرچند در متن اوستا تنها ستاک ساده و ترکیب با frā- (framīmaθā، یسنا ۳۲/۴) گواه دارد. دو نکته: نخست، *paiti-mā- و *ni-mā- بازسازی از روی فارسی میانه‌اند نه شاهد اوستایی؛ گواهِ واقعی، برگردان پهلویِ patmān برای ²mā- «اندازه» است. دوم، صورت «âiz-mâ» که در کتاب چاپ شده صورتی ناممکن است: هرن (شمارهٔ ۲۱) «آزمودن» را از «aw. *ā (یا به گواهی پهلوی ava) + uz + √mā-» می‌گیرد و ابوالقاسمی (ص ۲۵) از *uz-mā-ta. بنابراین «âiz-» باید «âuz-» (ā+uz) باشد. تصویر صفحهٔ ۳۲۳ چاپی (ذخیره‌شده در data/verification/sources/refs/ocr/BOOK/323.png) همان «âiz-mâ» را نشان می‌دهد؛ پس خطای چاپی کتاب است، نه خطای خوانش اسکن. صورت دوم نورایی، «uz-mâ-ta»، دقیقاً همان است که کتاب‌های امروزی می‌آورند.\",\n \"sources\": [S_PYM, S_NMD, S_AZM],\n \"ref_check\": [\n   {\"ref\": \"HRN:80\", \"status\": \"supports\", \"note\": \"HRN.txt printed pp.80-81, no. 363: 'pei/imūden \\\"messen; zeigen\\\", Praes. peimāy-em, peimā, peimāne … aw. *paiti- + √mā-; phlv. patmāyad (AV.), patmān, patmānīh, patmānak \\\"Mass\\\". kurd. piwān \\\"messen\\\"' — Nourai's paiti-mā exactly.\"},\n   {\"ref\": \"HRN:233\", \"status\": \"supports\", \"note\": \"HRN.txt printed p.233, no. 1042: 'numūden \\\"zeigen; erscheinen\\\", Praes. numāy-em … ni + √mā-; phlv. n(i)mūtan \\\"zeigen, erscheinen\\\", n(i)mayišn, n(i)mūtār' — Nourai's ni-mā exactly.\"},\n   {\"ref\": \"BQT:37\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 247 = printed p.37 (the page also carries the continuation note 'بقیه از صفحهٔ ۳۹'), Mo'in's footnote s.v. آزمودن: 'آزمایش پهلوی ōzmāyišn مرکب از uz + mā … آزمودن … مرکب از پیشوند uz و mā بمعنی اندازه گرفتن؛ تجربه کردن، آزمایش کردن'.\"},\n   {\"ref\": \"FFD:25\", \"status\": \"supports\", \"note\": \"FFD_pages.txt pdf p.30 = printed p.25: 'آزمودن — آزمود < فارسی میانه uzmūd/ōzmūd. صورت اصلی uzmūd است از پیشوند فعلی uz … صورت ایرانی باستان این ماده *uz-mā-ta بوده است. ریشهٔ mā(y) به معنی «اندازه گرفتن» است' — the printed source of Nourai's 'uz-mâ-ta'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1166 s.v. ¹mā(y)- and ²mā- f. 'Maß'\", \"stance\": \"partial\", \"note\": \"AiW col. 1166 note: 'ai. mímīte; mitíḥ; np. patmāyad \\\"er misst\\\", nimāyad \\\"er zeigt\\\", āzmāyad \\\"er erprobt\\\"; oss. amain \\\"erbauen\\\". — PÜ. (in V.7, F.8): ezmāyūn, [n]imūti(?)'; and s.v. ²mā- f. 'Maß' — 'PÜ.: paitimā(i)'. So Bartholomae attaches all three Persian verbs to Av. mā(y)- but quotes the compounds only from the Pahlavi version, not from Avestan text — the reason for 'partial'.\"},\n   {\"src\": \"PHD\", \"where\": \"pp. 32, 66, 68 s.v. framūdan, nimūdan, paymān/paymūdan\", \"stance\": \"supports\", \"note\": \"PHD.txt: 'paymān [ptmʾn' | M pymʾn, N ~] measure, period; moderation; treaty … paymūdan, paymāy- [ptmwtn', ptmʾd- | N ~] measure'; 'nimāy- [nmwtn', nmʾd-]'; English index 'show nimūdan'. MacKenzie's Pahlavi forms are the direct continuants of *paiti-mā-, *ni-mā-.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. handācak\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt: 'handāčak [hndʾck'] measure; ~ nimūtan to measure 110⁹' — an actual Pahlavi attestation of nimūtan in the measuring sense, i.e. the sense Nourai gives ni-mā ('measure down, display').\"},\n   {\"src\": \"CHEUNG\", \"where\": \"silent\", \"stance\": \"silent\", \"note\": \"grep for 'māy', 'paitimā', 'uzmā' in CHEUNG.txt returns no root entry for *maH- in the material available here; the Etymological Dictionary of the Iranian Verb could not be consulted for this root.\"}\n ]\n})\n\nN({\n \"id\": 6, \"lang\": \"Persian\",\n \"words\": \"paymŭdan «پیمودن»; âzmŭdan «آزمودن ( آزمایش ، آزمون )»; nomŭdan «نمودن»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three are MP compounds of mā(y)- inherited unchanged into New Persian, with the regular past stem in -ūd- < Old Iranian *-māta- (long ā before the participial -ta- gives MP -ū-, cf. sūd < *sū̆ta-) and the present stem in -māy- < *-mā-ya-. (a) پیمودن paymūdan, pres. پیمای- < MP paymūdan, paymāy- (ptmwtn') < *pati-mā- 'measure off'; hence پیمان 'covenant' (literally 'measure, moderation', MP paymān) and پیمانه 'measuring vessel'; the sense 'walk, traverse' is a Persian extension ('to measure out a road'), and هواپیما 'aeroplane' is a modern coinage 'air-measurer'. (b) آزمودن āzmūdan, pres. آزمای- < MP ōzmūdan/uzmūdan (Horn: phlv. ōzmūtan, ōzmāyišn) < *(ā-)uz-mā-ta- 'measure up, take the measure of' > 'to test'; hence آزمایش, آزمون, آزموده. (c) نمودن nomūdan/nimūdan, pres. نمای- < MP nimūdan (nmwtn') < *ni-mā- 'measure down, set out' > 'show, display'; hence نما, نمایش, نمودار, نماینده. The prefix vowels behave exactly as expected: pati- > pay- with loss of intervocalic t and i > y, ni- > ni-/no-, uz- > (ā)z-.\",\n \"derivation_fa\": \"هر سه، ترکیب‌های فارسی میانه از ستاک mā(y)- اند که بی‌دگرگونی به فارسی نو رسیده‌اند؛ ستاک گذشته با -ūd- از ایرانی باستان *-māta- (آی کشیده پیش از -ta- در فارسی میانه به او بدل می‌شود) و ستاک حال با -māy- از *-mā-ya-. یک) «پیمودن»، ستاک حال «پیمای»، از paymūdan/paymāy- فارسی میانه و *pati-mā- ایرانی باستان «اندازه گرفتن»؛ از همین ریشه «پیمان» (در فارسی میانه paymān «اندازه، میانه‌روی، عهد») و «پیمانه»؛ معنی «راه رفتن» گسترش معنایی فارسی است («راه را پیمودن») و «هواپیما» ساختِ نوِ «سنجندهٔ هوا». دو) «آزمودن»، ستاک حال «آزمای»، از ōzmūdan/uzmūdan فارسی میانه (هرن: phlv. ōzmūtan، ōzmāyišn) و *(ā-)uz-mā-ta ایرانی باستان «فراسنجیدن» و از آنجا «آزمودن»؛ مشتقات «آزمایش، آزمون، آزموده». سه) «نمودن»، ستاک حال «نمای»، از nimūdan فارسی میانه و *ni-mā- «فرودسنجیدن، برنمودن» و از آنجا «نشان دادن»؛ مشتقات «نما، نمایش، نمودار، نماینده». تحول پیشوندها نیز قاعده‌مند است: pati- ← پی (با افتادن ت میان‌واکه‌ای)، ni- ← نِ/نُ، uz- ← (آ)ز. ادعای نورایی درست است.\",\n \"sources\": [S_PYM, S_NMD, S_AZM],\n \"ref_check\": [\n   {\"ref\": \"BQT:37\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 247 = printed p.37, Mo'in s.v. آزمودن: 'آزمودن … مرکب از پیشوند uz (< uz که در پارسی [آ]ز شده) و mā بمعنی اندازه گرفتن؛ تجربه کردن، آزمایش کردن' and s.v. آزمایش 'پهلوی ōzmāyišn مرکب از uz + mā'.\"},\n   {\"ref\": \"BQT:448\", \"status\": \"partial\", \"note\": \"In the scan on disk (BQT_v1_pages.txt) p.448 is the پیغام/پیغامبر page and the پیمان / پیمانه / پیمودن entries fall two-three pages later (leaf 675, printed ~451; leaf 673 carries the running head '449'). The entries themselves are there — 'پیمانه … ظرفی که بدان چیزها پیمایند' with the پیمان headword — but the pagination of Nourai's Amir Kabir printing is a couple of pages ahead of this reprint, and the پیمودن lemma itself is lost in the OCR gap between leaves 675 and 676.\"},\n   {\"ref\": \"BQT:2171\", \"status\": \"supports\", \"note\": \"BQT vol.4 pdf p.254 (printed 2171), Mo'in's footnote s.v. نمودن/نمودنی: 'پهلوی nimūtan > ایرانی باستان *ni-māta(?) (جزو اول پیشوند بمعنی فرود، پایین؛ و جزو دوم …) … سریکلی، شغنی namāy- (نمودار شدن، ظاهر شدن) «اشتق ۱۰۸۷»؛ نشان دادن، اظهار کردن، ارائه دادن' and 'نمون (از «نمودن»)'.\"}\n   ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"pp. 66, 68 s.v. nimāy-/nimūdan, paymān, paymūdan\", \"stance\": \"supports\", \"note\": \"PHD.txt: 'paymūdan, paymāy- [ptmwtn', ptmʾd- | N ~] measure'; 'nimāy- [nmwtn', nmʾd-]'; 'paymān … measure, period; moderation; treaty. ~ag [-k' | N ~a] period, measure, proportion' — the MP ancestors of پیمودن، پیمان، پیمانه.\"},\n   {\"src\": \"HRN\", \"where\": \"nos. 21 (p.6), 363 (pp.80-81), 1042 (p.233)\", \"stance\": \"supports\", \"note\": \"Horn no. 21 'āzmūden \\\"erproben, versuchen\\\", Praes. āzmāy-em … phlv. ōzmūtan … aw. *ā (oder nach dem Pehlevi wohl ava) + uz + √mā-'; no. 363 'pei/imūden \\\"messen; zeigen\\\" … aw. *paiti- + √mā-; phlv. patmāyad, patmān \\\"Mass\\\"'; no. 1042 'numūdan \\\"zeigen; erscheinen\\\" … ni + √mā-; phlv. n(i)mūtan'.\"},\n   {\"src\": \"FFD\", \"where\": \"printed pp. 25 and 66\", \"stance\": \"supports\", \"note\": \"Abolghasemi p.25 s.v. آزمودن: 'آزمود < فارسی میانه uzmūd/ōzmūd … صورت ایرانی باستان این ماده *uz-mā-ta بوده است. ریشهٔ mā(y) به معنی «اندازه گرفتن» است'; p.66 s.v. فرمودن gives the parallel *fra-mā-ta.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 1166 s.v. ¹mā(y)-\", \"stance\": \"supports\", \"note\": \"AiW note: 'np. patmāyad \\\"er misst\\\", nimāyad \\\"er zeigt\\\", āzmāyad \\\"er erprobt\\\"' — Bartholomae lists precisely these three New Persian verbs under the root.\"}\n ]\n})\n\nN({\n \"id\": 7, \"lang\": \"Greek\",\n \"words\": \"metron; dia-metros\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Gk. μέτρον 'measure, rule, length; poetic metre' is *mh₁-tro-m, the root in zero grade plus the instrument suffix -τρον (the same formation as ἄρο-τρον 'plough'); Brugmann and Wiktionary both analyse it this way, comparing Skt. mā-tra-m 'measure' (Pokorny: 'gr. μέτρον \\\"measure\\\" (after Brugmann … as Old Indic dā-tra-m \\\"gift\\\" to *dō-)'). διάμετρος (γραμμή) is a transparent Greek compound, διά 'across, through' (Nourai's root Dwo) + μέτρος, 'the line that measures across', hence 'diameter'; it is Euclid's term (Elements I, def. 17). One reservation, which the chart does not record: Watkins flags μέτρον as only 'possibly' from *mē- ('but this is referred by some to med-'), and Walde-Pokorny cite Saussure's *med-trom > *metrom; Wiktionary's Ancient Greek entry gives *meh₁- + -τρον without alternatives, and notes that even *meh₁- may itself be a variant of *med-. Modern scholarship therefore sides with Nourai, with the med- option surviving as a minority reading.\",\n \"derivation_fa\": \"یونانی μέτρον «اندازه، معیار، وزن شعر» از *mh₁-tro-m است: ریشه در درجهٔ صفر به‌همراه پسوند ابزارساز -τρον (همان ساختِ ἄρο-τρον «گاوآهن»)، هم‌ساخت با mā-tra-m سنسکریت «اندازه». پوکورنی نیز همین را می‌گوید: «gr. μέτρον \\\"measure\\\" (به گفتهٔ بروگمان مانند dā-tra-m سنسکریت نسبت به *dō-)». διάμετρος ترکیبی روشن است از διά «از میان، سرتاسر» (ریشهٔ Dwo نزد نورایی) و μέτρος، یعنی «خطی که از میان می‌سنجد» و از آنجا «قطر»؛ اصطلاح اقلیدس است. یک نکتهٔ احتیاطی که در نمودار نیامده: واتکینز μέτρον را «شاید» از *mē- می‌گیرد و می‌افزاید که برخی آن را به *med- می‌برند؛ والده-پوکورنی هم نظر سوسور (*med-trom) را نقل می‌کنند. ویکی‌واژه بی‌درنگ *meh₁- + -τρον می‌دهد. پس پژوهش امروزی جانب نورایی را می‌گیرد و رأی *med- در اقلیت است.\",\n \"sources\": [S_METRO, S_ETY, S_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. mē-2: '3. Possibly Greek metron, measure, rule, length, proportion, poetic meter (but this is referred by some to med-): METER¹, METER², (METER³), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRONOME.' Nourai's node (including dia-metros) is straight out of this list, but Watkins hedges with 'Possibly', which the chart does not reproduce — hence 'partial'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 703-704 s.v. mē-3\", \"stance\": \"supports\", \"note\": \"'gr. μέτρον \\\"measure\\\" (after Brugmann Grundr. II 1, 342 as Old Indic dā-tra-m \\\"gift\\\" to *dō-); μῆτις \\\"plan, artifice\\\"'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 237\", \"stance\": \"partial\", \"note\": \"WLD_Bd2_pages.txt: 'Gr. μέτρον „Maß“ (nach Brugmann … wie ai. dā-tra-m zu … anders Saussure MSL 6, 246 ff.: idg. *metrom aus *med-trom zur Wzf. med-)' — records the competing *med- derivation.\"},\n   {\"src\": \"KLN\", \"where\": \"vol. II p. 962 s.v. meter, metre 'poetical rhythm'\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt: 'meter, metre, n., poetical rhythm. — ME. metre, fr. OF. metre (F. mètre), fr. L. metrum, fr. Gk. μέτρον, \\\"measure, meter\\\", which is rel. to μῆτρα … fr. I.-E. base *mē-, \\\"to measure\\\" … Avestic, OPers. mā-, L. metīrī, \\\"to measure\\\".' Klein also lists 'firman, mahout' among the cognates — the same Iranian family as this chart.\"},\n   {\"src\": \"KLN\", \"where\": \"vol. I p. 452 s.v. diameter\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt: 'diameter, n. — OF. diametre (F. diamètre), fr. L. diametros, fr. Gk. διάμετρος (scil. γραμμή), lit. \\\"a diametral line\\\". See dia- and meter, \\\"poetical rhythm\\\".'\"}\n ]\n})\n\nN({\n \"id\": 8, \"lang\": \"French\",\n \"words\": \"metre\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French mètre is a learned borrowing: Latin metrum (from Gk. μέτρον) gave OF metre 'poetic measure' in the 12th c.; the same word was then re-used as the name of the new decimal unit of length. The unit was named in 1791-1793 by the commission of the Académie des sciences (Borda, Lagrange, Laplace, Monge, Condorcet), building on Gabriel Mouton's 1670 proposal, and defined as one ten-millionth of the quarter-meridian. Klein: 'meter, metre, n., the unit of length in the metric system. — F. mètre (see prec. word); introduced in France as a name of measure in 1791.' The chart's parent arrow Greek → French is therefore right, though the route runs through Latin metrum, which Nourai's diagram passes over silently.\",\n \"derivation_fa\": \"«متر» فرانسوی وام‌واژه‌ای عالمانه است: لاتینی metrum (از μέτρον یونانی) در سدهٔ دوازدهم به فرانسوی کهن metre «وزن شعر» رسید و همان واژه در ۱۷۹۱–۱۷۹۳ به فرمان کمیسیون فرهنگستان علوم فرانسه (بوردا، لاگرانژ، لاپلاس، مونژ، کندرسه) نام یکای دهدهی درازی شد و برابر یک ده‌میلیونیم ربع نیم‌روزان زمین تعریف گردید. کلاین: «F. mètre … introduced in France as a name of measure in 1791». پس پیکان یونانی ← فرانسوی درست است، هرچند راهِ آن از لاتینی metrum می‌گذرد که نمودار نورایی از آن نام نمی‌برد.\",\n \"sources\": [S_ETY],\n \"ref_check\": [\n   {\"ref\": \"AHD:865\", \"status\": \"not_checked\", \"note\": \"Nourai's page 865 is not in the Indo-European appendix (pp.1505-1550) but in the main A-Z of the 1976 AHD New College Edition, i.e. the dictionary entry for 'meter'; the 1970s AHD scans on archive.org are lending-only (djvu.txt returns 401), and the open Watkins 1985 volume has only the root list. Could not be verified; the claim itself (French mètre < Greek metron) is uncontroversial and is confirmed by Klein and Etymonline.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"vol. II p. 962 s.v. meter, metre (unit of length)\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt: 'meter, metre, n., the unit of length in the metric system. — F. mètre (see prec. word); introduced in France as a name of measure in 1791.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mē-2\", \"stance\": \"supports\", \"note\": \"The Greek-based derivatives METER¹/METER²/-METER are all listed under mē-2, sub 'Possibly Greek metron'.\"}\n ]\n})\n\nN({\n \"id\": 9, \"lang\": \"Persian\",\n \"words\": \"metr «متر»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian متر metr is a 20th-century loan from French mètre, taken over with the metric system in the late Qajar/early Pahlavi period (the metric units were made official in Iran by the law of 1304 Sh./1925 and the Farhangestān kept the French forms). The final consonant cluster -tr is retained, as in other French loans of the same wave (تئاتر teātr, لیتر litr, سانتیمتر), which is itself the mark of a modern learned borrowing rather than an older Arabic- or Turkish-mediated one. Mo'in tags the word [فر.] = French. So this is a round trip of sorts: the ultimate root is the same *meh₁- that gave Persian its own پیمودن and ماه, but متر re-entered Persian from Europe, not by inheritance.\",\n \"derivation_fa\": \"«متر» فارسی وام‌واژه‌ای است از mètre فرانسوی که در سدهٔ چهاردهم هجری خورشیدی همراه با نظام متری به فارسی آمد (یکاهای متری با قانون ۱۳۰۴ در ایران رسمی شد). خوشهٔ همخوانی پایانی -tr نگه داشته شده است، همچون دیگر وام‌واژه‌های همان دوره: «تئاتر»، «لیتر»، «سانتی‌متر»؛ و همین نشانهٔ وام‌گیری نوِ عالمانه است، نه وام‌گیری کهنِ از راه عربی یا ترکی. معین آن را با نشانهٔ [فر.] یعنی فرانسوی می‌آورد. پس در حقیقت نوعی رفت‌وبرگشت است: ریشهٔ نهایی همان *meh₁- است که «پیمودن» و «ماه» فارسی نیز از آن است، اما «متر» از اروپا به فارسی بازگشته و میراثی نیست. ادعای نورایی درست است.\",\n \"sources\": [S_METR, S_MON],\n \"ref_check\": [\n   {\"ref\": \"MON:3800\", \"status\": \"partial\", \"note\": \"Mo'in's 6-volume pagination cannot be mapped online (the refs index notes 'Page numbers cannot be mapped online'), but the entry itself is verifiable: vajehyab.com/moein/متر gives 'متر [فر.]' with the definitions 'نواری باریک و درجه‌بندی شده از فلز، پارچه یا جنس دیگر که برای اندازه‌گیری طول و عرض اشیاء …' plus متر مربع and متر مکعب. The [فر.] tag is exactly Nourai's claim (French > Persian).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/متر\", \"stance\": \"supports\", \"note\": \"Origin tag '[فر.]' (فرانسوی) on the headword متر.\"},\n   {\"src\": \"KLN\", \"where\": \"vol. II p. 962 s.v. meter (unit)\", \"stance\": \"supports\", \"note\": \"Confirms the donor form and its 1791 date, i.e. that any Persian متر must be a post-1791 borrowing.\"}\n ]\n})\n\nN({\n \"id\": 10, \"lang\": \"English\",\n \"words\": \"meter, diameter, geometry\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three reach English through French from Greek, as the chart's arrow says, though only the first goes through mètre itself. (a) meter/metre 'unit of length', 1797, from F. mètre (1791); the older meter 'poetic rhythm' is OE meter < L. metrum < Gk. μέτρον. (b) diameter, late 14th c., from OF diametre < L. diametros < Gk. διάμετρος — i.e. through Old French, not through the modern unit-name. (c) geometry, late 14th c., from OF geometrie < L. geometria < Gk. γεωμετρία 'land-measuring' (γῆ 'earth' + -μετρία), the discipline named from the surveying of Egyptian fields (Herodotus II.109). Watkins lists exactly METER, -METER, DIAMETER, GEOMETRY under mē-2, so Nourai's box reproduces the AHD derivative list; the only imprecision is that 'French' here has to be read as Old French for diameter and geometry.\",\n \"derivation_fa\": \"هر سه واژه، چنان‌که نمودار می‌گوید، از یونانی و به میانجی فرانسوی به انگلیسی رسیده‌اند، اما تنها نخستین از راه خودِ mètre. یک) meter «یکای درازی» در ۱۷۹۷ از mètre فرانسوی (۱۷۹۱)؛ meter کهن‌تر به معنی «وزن شعر» از انگلیسی کهن meter، لاتینی metrum و μέτρον یونانی است. دو) diameter در پایان سدهٔ چهاردهم از diametre فرانسوی کهن، لاتینی diametros و διάμετρος یونانی — یعنی از فرانسوی کهن نه از نام یکای نو. سه) geometry در پایان سدهٔ چهاردهم از geometrie فرانسوی کهن، لاتینی geometria و γεωμετρία یونانی «زمین‌پیمایی»، نامی که از مساحی کشتزارهای مصر برخاسته است. واتکینز نیز همین چهار واژه METER، -METER، DIAMETER، GEOMETRY را ذیل mē-2 می‌آورد؛ پس فهرست نورایی همان فهرست AHD است و تنها بی‌دقتی این است که «فرانسوی» برای دو واژهٔ دوم و سوم باید «فرانسوی کهن» خوانده شود.\",\n \"sources\": [S_ETY, S_METRO],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. mē-2, sub 3 (Greek metron): 'METER¹, METER², (METER³), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRONOME' — all three of Nourai's words are in the list.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"vol. I p. 452 (diameter), vol. II p. 962 (meter)\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt: 'diameter, n. — OF. diametre (F. diamètre), fr. L. diametros, fr. Gk. διάμετρος (scil. γραμμή), lit. \\\"a diametral line\\\"'; 'meter, metre, n., the unit of length in the metric system. — F. mètre'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, root list\", \"stance\": \"supports\", \"note\": \"As quoted above.\"}\n ]\n})\n\nN({\n \"id\": 11, \"lang\": \"Latin\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box: the Latin members of the family that feed the English node below. Two Latin stems are involved. (1) mētīrī, mēnsus sum 'to measure' < *mē-ti- (Pokorny: 'Latin metior, -īrī, mēnsus sum … \\\"measure, gauge\\\"'), with the derivatives mēnsūra 'a measuring' and dīmētīrī, dīmēnsiō 'a measuring out'. (2) mēnsis 'month' < *mēns-, the same s-stem extension as Av. māh- and Gk. mḗn, whence sēme(n)stris 'of six months'. Nourai leaves the box wordless (he does this whenever the intermediate forms are recoverable from the English derivatives), and it is faithfully extracted as empty; the printed page shows the box with no headword and no reference.\",\n \"derivation_fa\": \"خانه‌ای بی‌واژه و گذرگاهی است: تنها برای رساندن اعضای لاتینی خانواده به خانهٔ انگلیسیِ زیر آن. دو ستاک لاتینی در کار است: یک) mētīrī / mēnsus sum «سنجیدن، پیمودن» از *mē-ti- (پوکورنی: «Latin metior, -īrī, mēnsus sum \\\"measure, gauge\\\"») با مشتقات mēnsūra و dīmēnsiō؛ دو) mēnsis «ماهِ شهر» از ستاک s دارِ *mēns- — همان گسترشی که در māh- اوستایی و mḗn یونانی دیده می‌شود — و از آن sēme(n)stris «شش‌ماهه». نورایی این خانه را بی‌واژه گذاشته است (شیوهٔ او در جایی که صورت میانی از مشتقات انگلیسی بازیافتنی است) و استخراج داده نیز درست همان تهی بودن را نشان می‌دهد؛ تصویر صفحهٔ چاپی هم خانه‌ای بی‌سرواژه و بی‌ارجاع است.\",\n \"sources\": [S_PIE, S_ETY],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box (refs=None in the JSON; the printed box carries no book icon).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 703-704 s.v. mē-3\", \"stance\": \"supports\", \"note\": \"'Latin metior, -īrī, mēnsus sum (rhyme meaning to pensus) \\\"measure, gauge\\\", whereof probably mēnsa \\\"table …\\\" = Umbrian mefa'; and pp.731-732 s.v. mēnōt: 'lat. mensis m. \\\"month\\\" …, menstruus \\\"monthly\\\" …, seme(n)stris \\\"6-month, half-year\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"vol. II p. 949 s.v. measure; vol. I p. 449 s.v. dimension\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt: 'measure, n. — ME. mesure, fr. OF. (= F.) mesure, fr. L. mensura, \\\"measure\\\", fr. mensus, pp. of metiri'; 'dimension, n. — F., fr. L. dimensiōnem … fr. dimensus, pp. of dimetiri, \\\"to measure out\\\", fr. di-, \\\"apart\\\", and metiri'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mē-2 sub I.2 and II.4\", \"stance\": \"supports\", \"note\": \"'2. Suffixed form *mē-ti- in Latin mētīrī, to measure: MEASURE, (MENSURAL); (COMMENSURATE), DIMENSION, IMMENSE'; '4. Latin mēnsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMESTRIAL, SEMESTER, TRIMESTER'.\"}\n ]\n})\n\nN({\n \"id\": 12, \"lang\": \"English\",\n \"words\": \"measure, dimension, semester\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The three Latin-route English words, all in Watkins's list under mē-2. measure: ME mesure, from OF mesure < L. mēnsūra 'a measuring', from mēnsus, pp. of mētīrī. dimension: from French, from L. dīmēnsiōnem, from dīmēnsus, pp. of dīmētīrī 'to measure out' (dis- 'apart' + mētīrī). semester: from German Semester < French semestre < L. sēme(n)stris (for *sex-mēns-tris) 'of six months, half-yearly', sex 'six' + mēnsis 'month' — so this one comes from the *mēn-s- 'month' branch rather than from the verb, which is why Nourai's Latin box, left unlabelled, can carry all three. Klein's entries give exactly these chains.\",\n \"derivation_fa\": \"سه واژهٔ انگلیسیِ راهِ لاتینی که هر سه در فهرست واتکینز ذیل mē-2 آمده‌اند. measure از mesure انگلیسی میانه، از mesure فرانسوی کهن و mēnsūra لاتینی، خود از mēnsus صفت مفعولی mētīrī. dimension از فرانسوی و dīmēnsiōnem لاتینی، از dīmēnsus صفت مفعولی dīmētīrī «برون‌سنجیدن» (dis- «جدا» + mētīrī). semester از Semester آلمانی، از semestre فرانسوی و sēme(n)stris لاتینی (از *sex-mēns-tris) «شش‌ماهه» یعنی sex «شش» + mēnsis «ماه»؛ پس این واژه از شاخهٔ *mēn-s- «ماه» می‌آید نه از فعل، و همین است که خانهٔ لاتینیِ بی‌سرواژهٔ نورایی می‌تواند هر سه را در خود بگیرد. مدخل‌های کلاین دقیقاً همین زنجیره‌ها را می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [S_ETY, S_PIE],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is given for this box in the book (refs=None); verified against Klein and Watkins instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"vol. II p. 949 (measure), vol. I p. 449 (dimension), vol. II p. 1408 (semester)\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt: 'measure … fr. L. mensura … fr. mensus, pp. of metiri'; 'dimension … fr. L. dimensiōnem … fr. dimetiri, \\\"to measure out\\\"'; 'semester, n., a period of six months. — G. Semester, fr. F. semestre, fr. L. seme(n)stris (for *sex-mens-tris), \\\"of six months, half-yearly\\\", fr. sex, \\\"six\\\", and mensis, \\\"month\\\" … and see six and moon.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mē-2\", \"stance\": \"supports\", \"note\": \"MEASURE and DIMENSION under I.2 (Latin mētīrī); SEMESTER under II.4 (Latin mēnsis).\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. measure\", \"stance\": \"supports\", \"note\": \"Skeat likewise takes measure from OF mesure, L. mensura, from metiri 'to measure', with the root given as MA 'to measure'.\"}\n ]\n})\n\nN({\n \"id\": 13, \"lang\": \"Germanic\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Another empty pass-through box, standing for the inherited (non-borrowed) Germanic forms. Watkins names three: *mēlaz < *mē-lo- 'measure, mark, appointed time' (> OE mǣl), *mēnēn- 'moon' (> OE mōna) and *mēnēth- 'month' (> OE mōnath) — the last two from the *mēn- extension. Germanic is the one branch that keeps the moon/month pair formally distinct (Goth. mēna 'moon' vs. mēnōþs 'month'), which is why Buck treats it separately at §1.53 and §14.71. The box is printed with the AHD reference and no headword, exactly as extracted.\",\n \"derivation_fa\": \"خانهٔ گذرگاهیِ بی‌واژهٔ دیگری، نمایندهٔ صورت‌های موروثی (نه وام‌گرفتهٔ) ژرمنی. واتکینز سه صورت را نام می‌برد: *mēlaz از *mē-lo- «اندازه، نشان، هنگام مقرر» (← mǣl انگلیسی کهن)، *mēnēn- «ماه/قمر» (← mōna) و *mēnēth- «ماهِ شهر» (← mōnath)، دو تای اخیر از ستاک گستردهٔ *mēn-. ژرمنی تنها شاخه‌ای است که این دو معنی را در دو صورتِ جدا نگه داشته است (گوتی mēna «قمر» در برابر mēnōþs «ماه شهر») و همین است که باک آن را در دو بندِ ۱٫۵۳ و ۱۴٫۷۱ جداگانه می‌آورد. خانه در چاپ کتاب با ارجاع AHD و بی‌سرواژه آمده، درست همان‌گونه که استخراج شده است.\",\n \"sources\": [S_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. mē-2: '1. Suffixed form *mē-lo- in Germanic *mēlaz in Old English mǣl … MEAL²; PIECEMEAL' and 'II. … 1. Germanic *mēnēn- in Old English mōna, moon: MOON; (MONDAY). 2. Germanic *mēnēth- in Old English mōnath, month: MONTH.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 703-704 and 731-732\", \"stance\": \"supports\", \"note\": \"'Gothic mēla m. \\\"bushel\\\"; Old Icelandic mælir … Old Icelandic mæla \\\"measure\\\"; Gothic mēl n. \\\"time\\\", Old Icelandic mál \\\"measure, moment, time, repast, meal\\\", Old English mǣl' (703); 'Gothic mena, Old Icelandic mani, Old English mōna … \\\"moon\\\"; Gothic mēnōþs, Old Icelandic mánaðr, Old English mōnað … \\\"month\\\"' (731).\"},\n   {\"src\": \"SYN\", \"where\": \"pp. 54 and 1010\", \"stance\": \"supports\", \"note\": \"Buck §1.53: '(2) with differentiation, all the Gmc. forms, as Goth. mēna \\\"moon\\\", mēnōþs \\\"month\\\"'; §14.71: 'In Gmc. a separate set of related forms distinguishes \\\"month\\\" fr. \\\"moon\\\"'.\"}\n ]\n})\n\nN({\n \"id\": 14, \"lang\": \"English\",\n \"words\": \"meal, moon, month, Monday\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The inherited Germanic quartet. moon: OE mōna < PGmc *mēnōn- < *mēh₁-n-, cognate with Av. māh-, NP ماه — so English moon and Persian māh are strict cognates, one of the neat pairs this chart is built to display. month: OE mōnath < PGmc *mēnōþ- < *mēh₁-n-ōt- (Pokorny's mēnōt lemma). Monday: OE mōnandæg 'day of the moon', a calque of Latin lūnae diēs made in the Roman period. meal: this is meal² 'repast', OE mǣl 'mark, sign; measure; fixed time; time for taking food' < PGmc *mēlaz < *mē-lo- 'a measured-out (time)' — the sense went 'measure' > 'appointed time' > 'mealtime' > 'meal', and the old sense survives in piecemeal (OE -mǣlum). It must not be confused with meal¹ 'ground grain', which Klein derives from a quite different base *(s)mel- 'to rub, grind' (Latin molere). Nourai's bare 'meal' is right for meal², i.e. the word Watkins actually lists.\",\n \"derivation_fa\": \"چهارگانهٔ موروثی ژرمنی. moon از mōna انگلیسی کهن، ژرمنی *mēnōn- و *mēh₁-n-، هم‌ریشه با māh- اوستایی و «ماه» فارسی — یعنی moon انگلیسی و «ماه» فارسی هم‌ریشهٔ راستین‌اند و همین‌گونه جفت‌ها است که این نمودارها برای نشان دادنشان ساخته شده‌اند. month از mōnath انگلیسی کهن، ژرمنی *mēnōþ- و *mēh₁-n-ōt- (همان سرواژهٔ mēnōt پوکورنی). Monday از mōnandæg «روز ماه»، گرته‌برداری از lūnae diēs لاتینی در دورهٔ رومی. meal همان meal² «خوراک، وعدهٔ غذا» است، از mǣl انگلیسی کهن «نشان؛ اندازه؛ هنگام مقرر؛ هنگام خوراک»، ژرمنی *mēlaz از *mē-lo- «زمانِ اندازه‌گرفته»؛ تحول معنایی: «اندازه» ← «هنگام مقرر» ← «هنگام خوراک» ← «خوراک»، و معنی کهن در piecemeal برجاست. آن را نباید با meal¹ «آرد» درآمیخت که کلاین از ریشهٔ جداگانهٔ *(s)mel- «سودن، آسیا کردن» (لاتینی molere) می‌گیرد. «meal» بی‌قید نورایی برای meal² درست است، یعنی همان واژه‌ای که واتکینز آورده. ادعای نورایی درست است.\",\n \"sources\": [S_PIE, S_MAH],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this box in the book (refs=None); the parent Germanic box carries the AHD citation, which covers all four words.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"vol. II p. 946 (meal 'food'), p. 968 (moon), p. 964 (month), p. 962 (Monday)\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt: 'meal, n., food taken at one time. — ME. mele, fr. OE. mǣl, \\\"mark, sign; measure; fixed time; time for taking food, meal\\\" … fr. I.-E. base *mē-, \\\"to measure\\\". See meter, \\\"poetical rhythm\\\"'; 'moon, n. — ME. mone … fr. OE. mōna … cogn. with OI. mās-, māsah, \\\"moon, month\\\", Avestic mā, ModPers. mah, of s.m.'; 'month, n. — ME. moneth … fr. OE. mōnað … and to OE. mōna, etc., \\\"moon\\\"'; 'Monday, n. — ME. monenday … fr. OE. mōnandæg, lit. \\\"day of the moon\\\" … prop. loan translations of L. Lunae dies'.\"},\n   {\"src\": \"KLN\", \"where\": \"vol. II p. 946 s.v. meal 'edible grain'\", \"stance\": \"partial\", \"note\": \"The homonym meal¹ is expressly separated: 'meal, n., edible grain. — ME. mele, fr. OE. melu … orig. \\\"that which is ground\\\" … fr. I.-E. base *(s)mel-, \\\"to rub, grind\\\"' — so only meal² belongs on this chart.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mē-2\", \"stance\": \"supports\", \"note\": \"'Old English mǣl, \\\"measure, mark, appointed time, time for eating, meal\\\": MEAL²; PIECEMEAL … Old English mōna, moon: MOON; (MONDAY) … Old English mōnath, month: MONTH.'\"}\n ]\n})\n\nout = {\n  \"pdf_page\": 323,\n  \"book_page\": 293,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [entry]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-323.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk323.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-323.json > /dev/null && echo \"JSON valid\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 323"
}
```


### [2026-09-07T16:06:30.752Z] TOOL RESULT

```
ok
JSON valid
nodes verified: 14/14
node verdicts: {'plausible': 1, 'confirmed': 12, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 19, 'partial': 5, 'not_checked': 4}
books consulted: {'partial': 4, 'supports': 36, 'silent': 2} | by book: {'KLN': 9, 'AHD': 5, 'BRT': 4, 'PHD': 4, 'POK': 3, 'KNT': 2, 'ARY': 2, 'HRN': 2, 'MON': 2, 'WLD': 2, 'NYB': 2, 'HUB': 1, 'CHEUNG': 1, 'FFD': 1, 'SKT': 1, 'SYN': 1}
```


## [2026-09-07T16:06:38.142Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^MEASURE\\|Measure, sb\\|MEASURE,\" SKT.txt | head -5; grep -no \"MEASURE.\\{0,260\\}\" SKT.txt | head -3"
}
```


### [2026-09-07T16:06:39.455Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T16:06:43.042Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -in \"measure\" SKT.txt | head -5 | cut -c1-400; echo \"---size\"; wc -l SKT.txt"
}
```


### [2026-09-07T16:06:43.096Z] TOOL RESULT

```
711:Anker,  a  liquid  measure.   (Daul anle^    the    same.  +  Swcd,    OfthMrt ;
1443:Barometer,  for  measuring  the the  air.  (Gk.)   Gk.  ^o^o-,  for  ^opor, and  fAirpar,  a  measure  ;  see  Metre,
2517:Bushelt  a  measure ;  see  Pyx.
2551:Cab  (3^.  a  Heb.  measure.  (Heb.)  Heb. ^ab,  the  JSlh  part  of  an  ephah.  ITie  literal sense  is  'hollow ;'  cf.  Heb.  qtibab^  to  form in  the  shajie  of  a  vault ;  see  Aloove.
2628:chaldron,  a  coal  measure.  (F.  —  L.) O.  F.  iMaidrtm,  orig.  a  caldnxi ;  lee Caldron.
---size
24055 SKT.txt
```


## [2026-09-07T16:06:46.749Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -in \"^Measure\\|Measure  (F\\|Measure.  (F\" SKT.txt | head; echo \"=== metre\"; grep -in \"Metre\" SKT.txt | head -5 | cut -c1-500"
}
```


### [2026-09-07T16:06:46.809Z] TOOL RESULT

```
2628:chaldron,  a  coal  measure.  (F.  —  L.) O.  F.  iMaidrtm,  orig.  a  caldnxi ;  lee Caldron.
11314:Measure.  (F.— L)  M.E.  mesurt^ O.  F.  mtsttrt.'^L.  meustn^^  measure. «L. mrw.r«j,pp.  of  mettri.  to  measure.  (^MA.) Allied  to  Mete.
15282:bushel,  a  measure.  (F.  —  L  —  Gk.) M.  E.  6mhel.  -  O.  F.  boissfl.  -  Low  L. bmctllui,  bmicllusx  a  bushel.  —  Low  L. huitulus,  a  small  box.  —  Low  !>.  buisida.  a form  of  buxida,  ace.  of  bitxu,  a  box.  ••  Gk* vvftr.  a  box  (above).
23902:Cs«S,  limit,  measure.  (F.  —  L.)  In I  Hen.  IV.  ii.  1.  S,  Orig.  a  tax,  rate, rating,  asse&sment;  see  Spenser,  State  of Ireland,  Globe  cd.,  p.  643,  col.  1.  From uss^  verbi  to  lato;  wfajch  is  short  for Aaaeaa.
=== metre
1443:Barometer,  for  measuring  the the  air.  (Gk.)   Gk.  ^o^o-,  for  ^opor, and  fAirpar,  a  measure  ;  see  Metre,
7526:geometry.  (F.  -  L  -  Gk.)  O,  F. gtonutrit.  —  L.  gtomctria.  —  G  k  ffaitfrpia, land -measurement.  — Gk.  7ca>-  (as  above); •furpia,  measurement,  from  y^rpiw,  1  mea- sure, ftirpov,  a  measure;  see  Metre.
8651:—  Gk.  i^ofiMTpot,  orig.  an  adj.,  i.e  hai six  measures  or  feet  — Gk.  I^,  six  ;  ^j a  measure,  metre.
9035:Iambic,  a  certain  metre,  a  short  uidalong srllable  {v -).  (L.  — fjk.)  V.  tamdifus.^ Gk.  InfiffiH&f.^Ok,  tafi^ot,  an  iambic  foot, iambic  vcise,  lampoon.  So  called  from UK  in  utiric  poetry.  »  Gk.  Hwrttr,  to thiow.  cast  (hence  attack).  Allied  to JeHi).
11485:Metrei,  Meter,  rhythm,  Tcr».  (F
```


## [2026-09-07T16:06:59.794Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\np=\"data/verification/page-323.json\"\nd=json.load(open(p))\nnodes={n[\"id\"]:n for n in d[\"entries\"][0][\"nodes\"]}\nfor c in nodes[12][\"consulted\"]:\n    if c[\"src\"]==\"SKT\":\n        c[\"where\"]=\"p. 331 s.v. Measure (SKT.txt line 11314)\"\n        c[\"note\"]=\"SKT.txt: 'Measure. (F.—L.) M.E. mesure, O.F. mesure.—L. mensura, measure.—L. mensus, pp. of metiri, to measure. (√MA.) Allied to Mete.' Skeat's root '√MA' is Nourai's Me 2.\"\nnodes[10][\"consulted\"].append({\"src\":\"SKT\",\"where\":\"s.v. geometry (SKT.txt line 7526)\",\"stance\":\"supports\",\"note\":\"SKT.txt: 'geometry. (F.-L.-Gk.) O.F. geometrie.—L. geometria.—Gk. γεωμετρία, land-measurement.—Gk. γεω- (as above); -μετρία, measurement, from μετρέω, I measure, μέτρον, a measure; see Metre.' Confirms the Old-French route for geometry.\"})\nwith io.open(p,\"w\",encoding=\"utf-8\") as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 -m json.tool data/verification/page-323.json > /dev/null && python3 tools/verify_check.py 323"
}
```


### [2026-09-07T16:07:01.568Z] TOOL RESULT

```
ok
nodes verified: 14/14
node verdicts: {'plausible': 1, 'confirmed': 12, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 19, 'partial': 5, 'not_checked': 4}
books consulted: {'partial': 4, 'supports': 37, 'silent': 2} | by book: {'KLN': 9, 'AHD': 5, 'BRT': 4, 'PHD': 4, 'POK': 3, 'KNT': 2, 'ARY': 2, 'HRN': 2, 'MON': 2, 'WLD': 2, 'NYB': 2, 'SKT': 2, 'HUB': 1, 'CHEUNG': 1, 'FFD': 1, 'SYN': 1}
```


## [2026-09-07T16:07:21.795Z] AGENT

Page 323 (book p. 293) verified — `data/verification/page-323.json`, `verify_check.py 323` clean (0 PROBLEM lines).

**Counts** — 1 entry, root `Me 2` = confirmed; 14 nodes: 12 confirmed, 1 plausible, 1 transcription_suspect. Ref checks: 19 supports, 5 partial, 4 not_checked. 37 supporting `consulted` entries across 16 books.

**Flagged items**
- `#5 [Avestan] âiz-mâ, uz-mâ-ta` — **transcription_suspect, error_in: book**. The printed page really does read `âiz-mâ` (page PNG saved to `data/verification/sources/refs/ocr/BOOK/323.png`), so the extraction is faithful; the form is impossible. Horn no. 21 gives `aw. *ā (oder nach dem Pehlevi wohl ava) + uz + √mā-` and Abolghasemi FFD 25 gives `*uz-mā-ta`, so the book's `âiz-` is Nourai's misprint for `âuz-` (ā + uz). His second variant `uz-mâ-ta` is exactly right.
- `#1 [Avestan/Old Persian] mâh-tab` — **plausible** (node downgraded for this one word). Av. `mā(y)-` and `māh-` are solid (Bartholomae col. 1166, 1170; Kent p.201; Pokorny 703/731), but no Old Iranian `*māh-tāp-` exists: مهتاب is a New Persian compound (مه + تاب < تافتن), which Nourai also prints correctly one box lower. Anachronistic placement, not a wrong etymology.
- `#7 [Greek] metron` — kept confirmed, but noted that Nourai's own source hedges: AHD reads "**Possibly** Greek metron … (but this is referred by some to *med-*)", and Walde-Pokorny II 237 cite Saussure's `*med-trom`. Modern consensus (Wiktionary, Beekes-style `*mh₁-tro-m`) sides with Nourai.

**No extraction errors found** — all 14 nodes, refs, scripts and `script_extra` strings match the printed page.

**Notable ref findings**: KNT:201 is exact (`mā- vb. "measure" … ā + mā- "extend" … fra- + mā- "command"`). POK:703+731 and the label "Me 2" are lifted verbatim from Watkins/AHD (`[Pok. 3. mē- 703, mēnōt- 731.]`). SYN:54/877/1010 = Buck §1.53 MOON / §12.54 MEASURE / §14.71 MONTH, all three pages correct. BQT:37, 1470, 1958, 2171 and FFD:25, 66 all confirmed with Mo'in's/Abolghasemi's own footnotes. Two partials worth recording: **BQT:448** — in the scan on disk پیمان/پیمانه/پیمودن sit at ~p.451, three pages after Nourai's number (his Amir Kabir printing runs slightly ahead; the پیمودن lemma itself falls in an OCR gap). **SNS:37, 113** — the glossary index does carry `xšvaš. mahya- 37/9` and `mah- 113/2`, so the citations are real (37 supports his form `mâhya`), but that book's OCR is unreadable. **AHD:865** not checked — it is a main-dictionary page of the 1976 New College Edition, lending-only on archive.org.
