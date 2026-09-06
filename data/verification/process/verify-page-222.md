# Verification process log — verify-page-222


## [2026-09-06T15:12:51.314Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 222 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-222.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-222.json. Write /home/sfmqrb/git/rishe/data/verification/page-222.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 222` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:12:52.906Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:12:53.615Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:12:53.651Z] TOOL RESULT

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


## [2026-09-06T15:12:54.320Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-222.txt"
}
```


### [2026-09-06T15:12:54.333Z] TOOL RESULT

```
1	=== PDF page 222 (book page 192) ===
2	--- entry 0 ---
3	ROOT [Semitic] H.r.m : to forbid  (refs FVA:98)
4	#1 (parent #0) [Arabic] refs=KLN:703; FVA:98 | harâm : forbidden ; harîm : forbidden area ; harem : private quarters ; ihrâm : prohibition ; Moharram : the month of fasting
5	  #2 (parent #1) [Persian] refs=FVA:98 | harâm «حَرام (محروم، تحریم، مَحرّم)» : forbidden ; harîm «حَریم (حَرَم)» : territory, protected area ; hermân «حرمان» : prohibition, disappointment ; hormat «حُرمت (احترام ، محترم)» : dignity, respect ; ehrâm «إحرام» : entering a respectful state, pilgrim's dress ; Moharram «مُحَرَّم» : a month when certain acts are forbidden
6	  #3 (parent #1) [English] refs=KLN:703, TYL:568 | harem : women's quarters in a house ; ihram : pilgrim's dress ; Moharram : a lunar month
7	  #4 (parent #1) [Spanish] refs=KLN:704 | harmathan : forbidden, evil, a bad Sahara wind
8	    #5 (parent #4) [English] refs=KLN:704 | harmattan : a type of (bad) Sahara wind
9	  #6 (parent #1) [Spanish] refs=KLN:941 | marrano : forbidden, pork, pig
10	    #7 (parent #6) [English] refs=KLN:941 | marrano : a Jew converted to Christianity
11	#8 (parent #0) [Hebrew] refs=KLN:723,937 | hěrem : forbidden ; mohoram-atta : you are under ban
12	  #9 (parent #8) [English] refs=KLN:723,937 | herem : biblical ban, excommunication ; maranatha : curse
13	--- entry 1 ---
14	ROOT [Arabic] H.s.n : to be kind, to do good things  (refs FVA:101)
15	#1 (parent #0) [Arabic] refs=FVA:101; HJB:419 | hosn : beauty, goodness ; Hasan, Hosayn : names of Mohammad's grandsons martyred in Karbalâ battle. ; Yâ-Hasan! Yâ-Hosayn! : cry of Moslems at procession of Moharram.
16	  #2 (parent #1) [Persian] refs=FVA:101 | hosn «حُسن» : goodness, beauty, advantage ; Hasan «حَسَن (حسین، محسن، احسان)» : name(s) ; ahsan «احسن (تحسین)» : (word of) admiration
17	  #3 (parent #1) [Hindustani] refs=HJB:419 | 
18	    #4 (parent #3) [English] refs=AHD:626; FSD:1166; KLN:735 | Hobson-jobson : corruption of Arabic phrase "Yâ-Hasan Yâ-Hosayn!" referring to a crowd excitement.
19	
```


## [2026-09-06T15:12:54.456Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-222.json"
}
```


### [2026-09-06T15:12:54.471Z] TOOL RESULT

```
1	{
2	  "pdf_page": 222,
3	  "book_page": 192,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "H.r.m",
8	        "lang": "Semitic",
9	        "refs": "FVA:98",
10	        "gloss": "to forbid"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Arabic",
17	          "refs": "KLN:703; FVA:98",
18	          "words": [
19	            {"translit": "harâm", "gloss": "forbidden", "script": null},
20	            {"translit": "harîm", "gloss": "forbidden area", "script": null},
21	            {"translit": "harem", "gloss": "private quarters", "script": null},
22	            {"translit": "ihrâm", "gloss": "prohibition", "script": null},
23	            {"translit": "Moharram", "gloss": "the month of fasting", "script": null}
24	          ],
25	          "script_extra": null,
26	          "note": null,
27	          "quote": null
28	        },
29	        {
30	          "id": 2,
31	          "parent": 1,
32	          "lang": "Persian",
33	          "refs": "FVA:98",
34	          "words": [
35	            {"translit": "harâm", "gloss": "forbidden", "script": "حَرام (محروم، تحریم، مَحرّم)"},
36	            {"translit": "harîm", "gloss": "territory, protected area", "script": "حَریم (حَرَم)"},
37	            {"translit": "hermân", "gloss": "prohibition, disappointment", "script": "حرمان"},
38	            {"translit": "hormat", "gloss": "dignity, respect", "script": "حُرمت (احترام ، محترم)"},
39	            {"translit": "ehrâm", "gloss": "entering a respectful state, pilgrim's dress", "script": "إحرام"},
40	            {"translit": "Moharram", "gloss": "a month when certain acts are forbidden", "script": "مُحَرَّم"}
41	          ],
42	          "script_extra": null,
43	          "note": null,
44	          "quote": {
45	            "text": "روا مدار خدایا که در حریم وصال - رقیب محرم و حرمان نصیب من باشد",
46	            "poet": "Hâfez"
47	          }
48	        },
49	        {
50	          "id": 3,
51	          "parent": 1,
52	          "lang": "English",
53	          "refs": "KLN:703, TYL:568",
54	          "words": [
55	            {"translit": "harem", "gloss": "women's quarters in a house", "script": null},
56	            {"translit": "ihram", "gloss": "pilgrim's dress", "script": null},
57	            {"translit": "Moharram", "gloss": "a lunar month", "script": null}
58	          ],
59	          "script_extra": null,
60	          "note": null,
61	          "quote": null
62	        },
63	        {
64	          "id": 4,
65	          "parent": 1,
66	          "lang": "Spanish",
67	          "refs": "KLN:704",
68	          "words": [
69	            {"translit": "harmathan", "gloss": "forbidden, evil, a bad Sahara wind", "script": null}
70	          ],
71	          "script_extra": null,
72	          "note": null,
73	          "quote": null
74	        },
75	        {
76	          "id": 5,
77	          "parent": 4,
78	          "lang": "English",
79	          "refs": "KLN:704",
80	          "words": [
81	            {"translit": "harmattan", "gloss": "a type of (bad) Sahara wind", "script": null}
82	          ],
83	          "script_extra": null,
84	          "note": null,
85	          "quote": null
86	        },
87	        {
88	          "id": 6,
89	          "parent": 1,
90	          "lang": "Spanish",
91	          "refs": "KLN:941",
92	          "words": [
93	            {"translit": "marrano", "gloss": "forbidden, pork, pig", "script": null}
94	          ],
95	          "script_extra": null,
96	          "note": null,
97	          "quote": null
98	        },
99	        {
100	          "id": 7,
101	          "parent": 6,
102	          "lang": "English",
103	          "refs": "KLN:941",
104	          "words": [
105	            {"translit": "marrano", "gloss": "a Jew converted to Christianity", "script": null}
106	          ],
107	          "script_extra": null,
108	          "note": null,
109	          "quote": null
110	        },
111	        {
112	          "id": 8,
113	          "parent": 0,
114	          "lang": "Hebrew",
115	          "refs": "KLN:723,937",
116	          "words": [
117	            {"translit": "hěrem", "gloss": "forbidden", "script": null},
118	            {"translit": "mohoram-atta", "gloss": "you are under ban", "script": null}
119	          ],
120	          "script_extra": null,
121	          "note": null,
122	          "quote": null
123	        },
124	        {
125	          "id": 9,
126	          "parent": 8,
127	          "lang": "English",
128	          "refs": "KLN:723,937",
129	          "words": [
130	            {"translit": "herem", "gloss": "biblical ban, excommunication", "script": null},
131	            {"translit": "maranatha", "gloss": "curse", "script": null}
132	          ],
133	          "script_extra": null,
134	          "note": null,
135	          "quote": null
136	        }
137	      ]
138	    },
139	    {
140	      "root": {
141	        "name": "H.s.n",
142	        "lang": "Arabic",
143	        "refs": "FVA:101",
144	        "gloss": "to be kind, to do good things"
145	      },
146	      "nodes": [
147	        {
148	          "id": 1,
149	          "parent": 0,
150	          "lang": "Arabic",
151	          "refs": "FVA:101; HJB:419",
152	          "words": [
153	            {"translit": "hosn", "gloss": "beauty, goodness", "script": null},
154	            {"translit": "Hasan, Hosayn", "gloss": "names of Mohammad's grandsons martyred in Karbalâ battle.", "script": null},
155	            {"translit": "Yâ-Hasan! Yâ-Hosayn!", "gloss": "cry of Moslems at procession of Moharram.", "script": null}
156	          ],
157	          "script_extra": null,
158	          "note": null,
159	          "quote": null
160	        },
161	        {
162	          "id": 2,
163	          "parent": 1,
164	          "lang": "Persian",
165	          "refs": "FVA:101",
166	          "words": [
167	            {"translit": "hosn", "gloss": "goodness, beauty, advantage", "script": "حُسن"},
168	            {"translit": "Hasan", "gloss": "name(s)", "script": "حَسَن (حسین، محسن، احسان)"},
169	            {"translit": "ahsan", "gloss": "(word of) admiration", "script": "احسن (تحسین)"}
170	          ],
171	          "script_extra": null,
172	          "note": null,
173	          "quote": {
174	            "text": "مُرد مُحسن لیک احسانش نمرد - نزد یزدان دین احسان نیست خُرد",
175	            "poet": "Molavî"
176	          }
177	        },
178	        {
179	          "id": 3,
180	          "parent": 1,
181	          "lang": "Hindustani",
182	          "refs": "HJB:419",
183	          "words": [],
184	          "script_extra": null,
185	          "note": null,
186	          "quote": null
187	        },
188	        {
189	          "id": 4,
190	          "parent": 3,
191	          "lang": "English",
192	          "refs": "AHD:626; FSD:1166; KLN:735",
193	          "words": [
194	            {"translit": "Hobson-jobson", "gloss": "corruption of Arabic phrase \"Yâ-Hasan Yâ-Hosayn!\" referring to a crowd excitement.", "script": null}
195	          ],
196	          "script_extra": null,
197	          "note": null,
198	          "quote": null
199	        }
200	      ]
201	    }
202	  ]
203	}
204	
```


## [2026-09-06T15:12:59.923Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVA','FVQ','KLN','TYL','HJB','AHD','FSD','AFM','PLA','AFA','LKT','WEB','SKT','DOZ','DEV','PHN','LAM','MON','BQT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-06T15:13:00.737Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && cat data/verification/sources/SOURCE_MATRIX.md | head -120"
}
```


### [2026-09-06T15:13:01.819Z] TOOL RESULT

```
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

TYL {"title": "W. Taylor, Arabic Words in English (S.P.E. Tract XXXVIII), Oxford 1933", "edition_found": null, "kind": "hathitrust_fullview", "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.b4089843 (S.P.E. Tracts nos. 31-40 bound volume incl. Tract XXXVIII, rightsCode pdus = full view in the US; record 000519279) ; mdp.39015005310308 (nos. 36-58) search-only", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_LeedsStudiesInEnglish_ArabicWordsInBenJonson_pp44-50.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incom

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start wit

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


### [2026-09-06T15:13:01.871Z] TOOL RESULT

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


## [2026-09-06T15:13:07.300Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '120,240p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:13:07.340Z] TOOL RESULT

```
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
```


## [2026-09-06T15:13:08.583Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['KLN','HJB','AHD','FSD','TYL']:\n    v=d[k]\n    print('==',k)\n    for f in ['local_file','page_offset','lookup_hint','scans','notes']:\n        print(' ',f,':',json.dumps(v.get(f),ensure_ascii=False)[:800])\n\""
}
```


### [2026-09-06T15:13:10.266Z] TOOL RESULT

```
== KLN
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt"
  page_offset : "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."
  scans : null
  notes : "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)"
== HJB
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt"
  page_offset : "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers."
  scans : null
  notes : ""
== AHD
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt"
  page_offset : "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page."
  lookup_hint : "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."
  scans : null
  notes : "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt."
== FSD
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt"
  page_offset : "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."
  scans : null
  notes : "Nourai cites 1940; page numbers in the New Standard were stable 1913-1940s (single-volume pagination 1-2814 continues across the DLI volumes). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt"
== TYL
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_LeedsStudiesInEnglish_ArabicWordsInBenJonson_pp44-50.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_BenJonson_pages.txt"]
  page_offset : null
  lookup_hint : "Not on IA (searched 'arabic words in english', 'society for pure english tract 38'); Google Books record has no view. Taylor's related 'Etymological List of Arabic Words in English' (1933) id QmBbAAAAIAAJ is snippet only."
  scans : null
  notes : "RE-SEARCH 2026-09: the tract itself is full view on HathiTrust (US) — download in a browser (host is IP-blocked). Only a related article (Taylor, 'Arabic Words in Ben Jonson', Leeds Studies in English 3, 1934) was downloadable here; it is NOT the tract. Not on archive.org/Google Books."
```


## [2026-09-06T15:13:14.552Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in harem harmattan marrano herem maranatha ihram \"Hobson-Jobson\" hobson; do\necho \"=== $w\"; grep -n -i \"^$w\" KLN_1966.txt | head -5\ndone"
}
```


### [2026-09-06T15:13:16.318Z] TOOL RESULT

```
=== harem
17209:harem,  n.,  women’s  section  in  an  Oriental  house. —  Arab,  hartm,  ‘sacred,  forbidden’,  fr.  harama , ‘he  forbade’,  haruma,  ‘was  forbidden’,  rel.  to Ethiop.  harama,  ‘he  prohibited  from  common use,  he  devoted  to  God’,  Heb.  heherfm,  ‘he banned,  devoted  to  destruction,  excommunicat¬ ed’,  herem,  ‘person  or  thing  devoted  to  destruct¬ ion’.  See  herem  and  cp.  words  there  referred  to. Cp.  also  harmattan,  ihram,  Muharram.
=== harmattan
17225:harmattan,  n.,  a  dry  wind,  charged  with  dust, blowing  from  the  Sahara  to  the  Atlantic  coast. —  Sp.  harmatan,  fr.  Fanti  haramata,  fr.  Arab. hardm,  ‘a  forbidden  thing’,  used  in  the  sense  of ‘an  evil  thing’,  from  the  stem  of  harama,  ‘he  for¬ bade’,  haruma,  ‘was  forbidden’.  See  harem. Harmonia,  n.,  the  wife  of  Cadmus  in  Greek  my¬ thology.  —  L„  fr.  Gk.  'Appovta,  lit.  ‘concord’. See  harmony.
=== marrano
=== herem
=== maranatha
=== ihram
18694:ihram,  n.,  the  dress  consisting  of  two  white  cloths worn  by  Mohammedan  pilgrims  to  Mecca.  — - Arab,  ihrdm,  ‘prohibition,  interdiction’,  prop, inf.  of  dhrarna,  ‘he  prohibited,  interdicted’,  4th conjugation  of  hdrama,  ‘he  prohibited’.  See harem.
=== Hobson-Jobson
17906:hobson-jobson,  n.,  a  festal  excitement.  —  Cor¬ ruption  of  Arab,  ya  Hasan !  ya  Husayn  I  ‘O Hasan!  O  Husain!’,  cry  of  the  Mohammedans at  the  procession  of  the  Moharram.  See  Yule and  Burnell,  Hobson-Jobson,  p.  419.
=== hobson
17906:hobson-jobson,  n.,  a  festal  excitement.  —  Cor¬ ruption  of  Arab,  ya  Hasan !  ya  Husayn  I  ‘O Hasan!  O  Husain!’,  cry  of  the  Mohammedans at  the  procession  of  the  Moharram.  See  Yule and  Burnell,  Hobson-Jobson,  p.  419.
17907:Hobson's  choice,  n.  —  So  called  after  Thomas Hobson  (died  in  1631),  who  had  livery  stables  at Cambridge  and  let  out  horses  to  customers  on the  condition  that  they  had  to  take  the  animal standing  in  the  stable  nearest  to  the  stable  door, hock,  n.,  the  joint  in  the  hind  leg  of  a  horse.  — ME.  hough,  hoch,  fr.  OE.  hoh,  ‘heel’,  rel.  to  the first  element  in  ON.  ha-sin,  OE.  hoh-sinu,  ‘hock sinew’,  OHG.  hahsa,  MHG.  hahse,  G.  Hachse, ‘hock’,  ON.  hzll,  OE.  hsela,  ‘heel’,  and  cogn. with  OI.  kaksah,  kakfd,  Avestic  kasha,  ‘armpit’, L.  coxa,  ‘hip’,  Lith.  k'mka,  kenkle,  ‘knee  joint’, cinksla,  ‘knee  sinew’,  OIr.  coss,  ‘foot’.  Cp.  bough. Cp.  also  heel.  Cp.  also  coxa.  For  the  second element  in  ON.  hd-sin,  OE.  hoh-sinu,  see  sinew. Derivative:  hock,  tr.  v.,  to  hamstring, hock,  n.,  white  Rhenish  wine.  —  Orig.  ‘wine  of Hochheim’,  abbreviation  of  obsol.  hockamore, ‘wine  of  Hochheim’,  fr.  G.  Hochheimer,  fr.
```


## [2026-09-06T15:13:20.723Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"marrano\\|maranatha\\|Marrani\" KLN_1966.txt | head -10\necho \"=== herem\"\ngrep -n \"^herem\\|herem,\" KLN_1966.txt | head -10"
}
```


### [2026-09-06T15:13:20.798Z] TOOL RESULT

```
3026:anusim,  n.  pi.,  Jews  converted  to  another  faith by  force;  specif,  the  marranos.  —  Heb.  finustm, ‘those  compelled  (to  give  up  their  faith)’,  pi.  of antis,  pass.  part,  of  anas,  ‘he  compelled,  con¬ strained’,  which  is  rel.  to  Aram,  finds,  Syr.  irtds, of  s.m.
17630:Derivative:  hereditari-ly,  adv. heredity,  n.,  the  transmission  of  bodily  and  mental characters  of  parent  to  offspring.  —  F.  heredite, fr.  L.  hereditatem,  ace.  of  hereditas,  ‘heirship’, fr.  heres,  gen.  heredis,  ‘heir’.  See  heir  and  -ity. Hereford,  n.,  name  of  a  breed  of  red  and  white beef  cattle.  —  So  called  because  first  bred  in Herefordshire  in  England, herem,  n„  Biblical  ban,  excommunication.  — Heb.  herem,  ‘person  or  thing  devoted  to  destruc¬ tion’,  rel.  to  heherim,  ‘he  banned,  devoted  to destruction,  excommunicated’,  Aram,  ahdrtm, ‘he  banned;  excommunicated’,  Arab,  harama, ‘he  forebade’,  haruma,  ‘was  forbidden’,  harim, ‘sacred,  forbidden’,  Ethiop.  harama,  ‘he  pro¬ hibited  from  common  use;  he  devoted  to’,  Ak¬ kad.  haramu,  ‘to  dedicate’,  harimtu,  ‘a  dedicated woman,  a  female  hierodule’.  Cp.  maranatha, marrano.  Cp.  also  harem  and  words  there  re¬ ferred  to.
22878:Marah,  n.,  the  first  oasis  reached  by  the  Israelites after  passing  through  the  Red  Sea.  The  waters were  bitter,  but  Moses  sweetened  them.  See  Ex. 15:  23-25;  Nu.  33,  8:9.  —  Heb.  Mara1*,  prop, fern,  of  mar,  ’bitter’,  used  as  a  noun,  from  the root  of  mar  (contraction  of  marar),  ‘was bitter’,  whence  also  mor,  ‘myrrh’,  merdrah,  ‘gall, gallbladder',  mirerdh,  ‘gall’,  nfrdrtm,  ‘bitter herbs’,  mlrirt,  ‘bitter’,  memer ,  msr  truth,  ‘bitter¬ ness’,  Mishnaic  Heb.  marah,  'gall  (lit.  ‘the bitter  organ’).  See  myrrh, maranatha,  n.,  a  curse.  —  Gk.  [xapavxffx,  usually explained  as  transliteration  of  Aram,  maran atha,  ‘the  Lord  has  come’,  or  'O  Lord,  come  . But  the  association  of  puxpavaffa.  with  avaffefza in  ivailqiz,  uapavaffa,  ‘let  him  be  ana¬ thema,  maranatha’  (1st  Corinth.  16:22),  makes it  probable  that  the  words  Avxfleux.  jxapxvaffa express  a  double  or  intensified  curse.  It  is  very probable  that  p.apavaffa  is  the  transliteration of  Heb.  mohoram  atta1*,  ‘thou  art  put  under  the ban',  the  short  Qamatz  in  the  first  syllable  of  the word  mohdram  having  been  mistaken  for  the long  one  (=  a)  and  the  letter  n  (=  h),  which has  no  exact  equivalent  in  the  Greek  alphabet, having  been  dropped  in  the  transliteration.  The omission  of  the  letter  n  is  the  rule  in  the  trans¬ literation  of  PN.’s  in  the  LXX.  Cp.  e.g.  ’Evtby., translit.  of  -pin  ( HdnSkh ),  Nioe,  translit.  of  113 (No*h),’ load*,  translit.  of  jr?*’  (Yitzhak),  Za- pa,  translit.  of  mi  (Zdrab,  Zarab),  ’0<p£p, translit.  of  1311  Ufepher),  2aX7ra<*8,  translit.  of inaSii  ( Tztlophbad ),  ’AyTL  translit.  of  ’311
22880:(Haggt),  ’  Ayy'zIoc,  rendering  of  \3TI  (Ilaggdy). The  Hebrew  word  moboram  is  the  Hoph'al  (= passive  of  the  causative)  part,  of  harbm,  ‘he devoted,  banished’,  which  is  rel.  to  Arab,  bdru- ma,  ‘was  forbidden,  unlawful’;  see  herem  and cp.  harem.  For  the  change  of  m  to  n  cp.  marrano. The  identification  of  [zapavaffa  with  Heb.  mo¬ il  or  am  atta1*  is  supported  by  the  fact  that  the  LXX usually  renders  the  Heb.  noun  herem  (e.g.  in Lev.  27 :  28,  29)  by  avaffsp-a  (see  anathema)  and the  verb  heberim  (e.g.  in  Nu.  21 :  2,3)  by  avaffs- [xaTt^Eiv  (see  anathematize).
22983:marram  grass,  bent  grass.  —  ON.  maralmr,  lit. ‘sea  grass’,  fr.  mart,  ‘sea’,  and  halmr,  ‘straw’. See  mere,  ‘sea’,  and  haulm, marrano,  n.,  Jew  or  Moor  converted  to  Chris¬ tianity.  —  Sp.,  ‘pig,  hog’,  fr.  Arab,  hdruma,  ‘was forbidden’.  The  pig  was  called  the  ‘forbidden animal’,  from  the  fact  that  the  eating  of  pork  is forbidden  by  Jewish  and  Moslem  religious  law. Cp.  (Andalusian)  Sp.  maharrana,  ‘fresh  bacon, salt  pork’,  which  derives  fr.  Arab.  muhdrramah, fern,  of  muharram,  ‘anything  forbidden’,  pass, part,  of  harrama.  See  harem  and  herem.  For  the change  of  m  to  n  cp.  maranatha. marriage,  n.  —  ME.  mariage,  fr.  OF.  (  =  F.) mariage,  fr.  VL.  maritaticum  (occurring  in  a text  from  the  year  1062),  fr.  L.  maritatus,  pp.  of maritare,  ‘to  wed,  marry,  give  in  marriage’.  It. maritaggio,  Sp.  maridaje,  ‘marriage’,  also  derive fr.  VL.  maritaticum.  See  marry  and  -age. marron,  n.,  the  European  chestnut.  —  F.  See maroon,  ‘brownish  red’.
=== herem
17209:harem,  n.,  women’s  section  in  an  Oriental  house. —  Arab,  hartm,  ‘sacred,  forbidden’,  fr.  harama , ‘he  forbade’,  haruma,  ‘was  forbidden’,  rel.  to Ethiop.  harama,  ‘he  prohibited  from  common use,  he  devoted  to  God’,  Heb.  heherfm,  ‘he banned,  devoted  to  destruction,  excommunicat¬ ed’,  herem,  ‘person  or  thing  devoted  to  destruct¬ ion’.  See  herem  and  cp.  words  there  referred  to. Cp.  also  harmattan,  ihram,  Muharram.
17630:Derivative:  hereditari-ly,  adv. heredity,  n.,  the  transmission  of  bodily  and  mental characters  of  parent  to  offspring.  —  F.  heredite, fr.  L.  hereditatem,  ace.  of  hereditas,  ‘heirship’, fr.  heres,  gen.  heredis,  ‘heir’.  See  heir  and  -ity. Hereford,  n.,  name  of  a  breed  of  red  and  white beef  cattle.  —  So  called  because  first  bred  in Herefordshire  in  England, herem,  n„  Biblical  ban,  excommunication.  — Heb.  herem,  ‘person  or  thing  devoted  to  destruc¬ tion’,  rel.  to  heherim,  ‘he  banned,  devoted  to destruction,  excommunicated’,  Aram,  ahdrtm, ‘he  banned;  excommunicated’,  Arab,  harama, ‘he  forebade’,  haruma,  ‘was  forbidden’,  harim, ‘sacred,  forbidden’,  Ethiop.  harama,  ‘he  pro¬ hibited  from  common  use;  he  devoted  to’,  Ak¬ kad.  haramu,  ‘to  dedicate’,  harimtu,  ‘a  dedicated woman,  a  female  hierodule’.  Cp.  maranatha, marrano.  Cp.  also  harem  and  words  there  re¬ ferred  to.
```


## [2026-09-06T15:13:36.418Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\ntargets={'harem':17209,'harmattan':17225,'herem':17630,'maranatha':22878,'marrano':22983,'hobson-jobson':17906}\n# build cumulative formfeed count by line\ncum=0\nff=[]\nfor l in lines:\n    ff.append(cum)\n    cum+=l.count('\\f')\nfor k,v in targets.items():\n    leaf=ff[v-1]\n    print(k,'line',v,'leaf',leaf,'-> printed approx p',2*(leaf-12),'/',2*(leaf-12)+1)\nEOF"
}
```


## [2026-09-06T15:13:37.125Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"HOBSON-JOBSON\" HJB.txt | head -10"
}
```


### [2026-09-06T15:13:38.252Z] TOOL RESULT

```
harem line 17209 leaf 379 -> printed approx p 734 / 735
harmattan line 17225 leaf 379 -> printed approx p 734 / 735
herem line 17630 leaf 389 -> printed approx p 754 / 755
maranatha line 22878 leaf 503 -> printed approx p 982 / 983
marrano line 22983 leaf 505 -> printed approx p 986 / 987
hobson-jobson line 17906 leaf 395 -> printed approx p 766 / 767
```


### [2026-09-06T15:13:38.301Z] TOOL RESULT

```
39:["  Wee  have  forbidden  the  severall  Faotoryes  from  wrighting  words  in this  languadge  and  refrayned  itt  our  selves,  though  in  bookes  of  ooppies we  feare  there  are  many  which  by  wante  of  tyme  for  perusall  we  cannot rectefie  or  expresse."— Sm^t  Factors  to  Comi;,  Feb.  26, 1617:  L  O.  Beoords : O.  C.  No.  450.  (Evidently  the  Court  had  complained  of  a  growing  use  of "Hobson-Jobsons.")]
50:HOBSON-JOBSON
7681:CX)W-ITOH,  s.  The  irritating  hairs on  the  pod  of  the  common  Indian climbing  herb  Mucuna  pruriens^  D.C., N.  O.  Legumino9a€y  and  the  plant itself.  Both  pods  and  roots  are  used in  native  practice.  The  name  is  doubt- less the  Hind,  hewdnch  (Skt.  kapi- kachchhu\  modified  in  Hobson-Jobson fashion,  by  the  *  striving  after  meaning.'
9107:CX)WEI>,  participle.  To  brow-beat, to  cow ;  and  cowed,  brow-beaten,  set- down.  This  is  a  capital  specimen  of Anglo-Indian  dialect.  Dam  Jchdnd, '  to eat  one's  breath,'  is  a  Hind,  idiom  for *to  be  silent.'  Hobson-Jobson  converts this  into  a  transitive  verb,  to  damkhdOj and  both  spelling  and  meaning  beinff affected  by  £nglish  suggestions  of sound,  this  comes  in  Anglo-Indian use  to  imply  cowing  and  sUmcing.  [A more  probable  derivation  is  from Hind.  dhamkandLl  *to  chide,  scold, threaten,  to  repress  by  threats  or  re- proof {PlatU,  E.  Dtct).]
9544:FALAUN,  B.  Ar.  faldn,  fuldn,  and H.  fiUdna,  faldnoy  *such  an  one,'  *a certain  one*^;  Span,  and  Port  /uiano, Heb.  Fuluni  (Ruth  iv.  1).  In  Elphin- stone's  Life  we  see  that  this  was  the  term by  which  he  and  his  friend  Strachey used  to  indicate  their  master  in  early days,  and  a  man  whom  they  much respected,  Sir  Barry  Close.  And  gradu- ally, by  a  process  of  Hobson-Jobson, this  was  turned  into  Forlorn.
11164:HOBSON-JOBSON,
11177:HOBSON-JOBSON.
11467:IMAUMBABRA,  s.  This  is  a hybrid  word  Imdm-hdrd,  in  which the  last  part  is  the  Hindi  bdrd^  *an enclosure,'  &c.  It  is  applied  to  a  build- ing maintained  by  Sni'a  communities in  India  for  the  express  purpose  of celebrating  the  mohmmm  ceremonies (see  HOBSON-JOBSON).  The  sepulchre of  the  Founder  and  his  family  is  often combined  with  this  object.  The  Im- ambara  of  the  Nawab  Asaf-ud-daula at  Lucknow  is,  or  was  till  the  si^  of 1858,  probably  the  most  magnincent modem  Oriental  structure  in  India. It  imited  with  the  objects  already mentioned  a  mosque,  a  college,  ancl apartments  for  the  members  of  the religious  establishment.  The  great  hall is  "  conceived  on  so  ^nd  a  scale,"  says Fergusson,  **  as  to  entitle  it  to  rank  with the  l)uilding8  of  an  earlier  age."  The central  part  of  it  forms  a  vaulted  apart- ment of  162  feet  long  by  53^  wide.
22908:UPPEB  BOGEB,  s.  This  happy example  of  the  Hobson-Jobson  dialect occurs  in  a  letter  dated  1756,  from Cajit.  Jackson  at  Syrian  in  Burma, which  is  given  in  Dalrymple's  Oriental Repertory,  i.  192.  It  is  a  corruption of  the  Skt.  yuva-rdjay  *  young  King,^ the  Caesar  or  Heir- Apparent,  a  title borrowed  from  ancient  India  by  most of  the  Indo-Chinese  monarchies,  and which  we  generally  render  in  Siam  as the  '  Second  King.'
22909:UBZ,  UBZEE,  and  vulgarly XJBJEE,  s.  P.— H.  'arz  and  \im, from  Ar.  *arzy  the  latter  a  word  having an  extraordinary  variety  of  uses  even for  Arabic.  A  petition  or  humble representation  either  oral  or  in  writing ; the  technical  term  for  a  request  from an  inferior  to  a  superior ;  *a  sifflication^ as  one  of  Sir  Walter  Scott's  characters calls  it.  A  more  clalx)rate  form  is ^arz-ddshty  'memorializing.'  This  is used  in  a  very  barbarous  form  of Hobson-Jobson  below.
```


## [2026-09-06T15:13:50.861Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('HJB.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\ncum=0; ff=[]\nfor l in lines:\n    ff.append(cum); cum+=l.count('\\f')\nfor v in (11164,11177):\n    print('line',v,'leaf',ff[v-1],'-> printed ~', ff[v-1]-35, 'to', ff[v-1]-51)\nprint('----')\nprint('\\n'.join(lines[11160:11180])[:3000])\nEOF"
}
```


### [2026-09-06T15:13:53.655Z] TOOL RESULT

```
line 11164 leaf 470 -> printed ~ 435 to 419
line 11177 leaf 470 -> printed ~ 435 to 419
----
1712.—'*.  .  .  substantiam  obtinet  ponde- rosara,  instar  rapae  solidam  canaidissi- mamque,   plenam  suooi  pingnia,  albivimi,
HIRAVA.
419
HOBSON-JOBSON,
foetidiasimi,  porraoeo  odore  nares  horrid^ f  erientis ;  qui  ex  o&  ooUectus,  Penis  Indisque Hingli,  Europaeis  Aaa  foetida  appellatar." —3kg,  Kaempfer  Amoen,  Exotic,  ilsj,
1726.—"  Hiog  or  Ana  Foetida,  otherwise called  Deiril's-duiig  {Duiveladrek),'* — Vcden- tijn,  iv.  146.
1867.—"  Whilst  riding  in  the  plain  to  the Nf£.  of  the  city  (Candahar)  we  noticed sereral  assafcetida  plants.  The  assafcetida, called  hang  or  hiniBr  by  the  natives,  gprows wild  in  tiie  sandy  or  gravelly  plains  that form  the  western  part  of  Afghanistan.  It is  never  cultivated,  but  its  peculiar  gum- resin  is  collected  from  the  plants  on  the deserts  where  they  gprow.  Tnejproduce  is for  the  most  pajrt  exported  to  Hindustan." — Bdieuf,  Journal  of  a  Pol,  Misnon,  Ac., p.  270.
HIBAVA,  n.p.  Malayal.  Iraya, The  name  of  a  very  low  caste  in Malabar.  [The  Iraya  form  one  section of  the  Gheirumar^  and  are  of  slightly higher  social  standing  than  the  PtUayar (see  POLEA).  "  Their  name  is  derived from  the  fact  that  they  are  allowed to  come  only  as  far  as  the  eaves  (ira) of  their  employers*  houses."  (Logan, Malabar,  i.  148.)]
1510.— "La  sexta  sorte  (de*  Gentili)  se chiamSo  Hirava,  e  questi  seminano  e  rao- ooglieno  il  nao,"—Varthema  (ed.  1517,  f. 43v).
rmBBAWEN,  s.  The  Musulman pii^im  dress ;  a  corruption  of  the  Ar. thrdm.  Burton  writes :  ^^AUIkrdm, literally  meaning  *  prohibition'  or 'making  unlawful,'  equivalent  to  our 'mortification,'  is  appued  to  the  cere- mony of  the  toilette,  and  also  to  the dress  itself.  The  vulgar  pronounce the  word  ^herdm,  or  *tehram.*  It  is opposed  to  ihldlj  '  making  lawful,'  or *  returning  to  laical  life.'  The  further from  Mecca  it  is  assumed,  provided that  it  be  diiring  the  three  months  of Hajj,  the  greater  is  the  religious  merit of  the  pilgrim ;  consequently  some come  from  India  and  Egypt  in  the dangerous  attire"  (Pilgrimage,  ed.  1893, ii.  138,  note).
[1813.  —  " .  .  .  the  ceremonies  and penances  mentioned  by  Pitts,  when  the Aq;e»,  or  pilgrims,  enter  into  Hixrawen, a  ceremony  from  which  the  females  are exempted ;  but  the  men,  taking  off  all  their clothes,  cover  themselves  with  two  hizra- WBDM  or  laige  white  wrappers.  .  .  ." — Forbet, Or.  Man,  ii.  101,  2nd  ed.]
H0B80N-J0B80N,  s.  A  native festal    excitement ;     a    tamdsha    (see
TIJMA8HA) ;  but  especially  the  Mo- harram  ceremonies.  This  phrase  may be  taken  as  a  typical  one  of  the  most highly  assimilated  class  of  Anglo- Indian  argot,  and  we  have  ventured to  borrow  from  it  a  concise  alternative title  for  this  Glossary.  It  is  pec
```


## [2026-09-06T15:13:57.144Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11177,11182p' HJB.txt | head -c 3000"
}
```


### [2026-09-06T15:13:57.196Z] TOOL RESULT

```
HOBSON-JOBSON.
4fi0
HOG-DEEB,
c  1680.—"  Nine  davea  they  wander  up and  downe  (shaving  all  that  while  neither head  nor  board,  nor  seeming  ioyfull),  inces- santly calling  out  HuBBaii,  BUfBan  I  in  a
melancholy  note,  so  long,  so  fiercely,  that many  can  neither  howle  longer,  nor  for  a month's  space  recover  their  voices."— <Sir  T. Herbert,  261.
1653.—".  .  .  ils  dressent  dans  les  rues des  Sepulchres  de  pierres,  qu'ils  oouronnent de  Lampes  ardentes,  et  les  soirs  ils  y  vont dancer  et  sauter  crians  Hnisan,  HoaMain, Hoiuwain,  Hftiman  .  .  ."— 2>e  la  Boullaye- h-Gouz,  ed.  1657,  p.  144.
```


## [2026-09-06T15:13:59.212Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=11176 && NR<=11177' HJB.txt | head -c 2500"
}
```


### [2026-09-06T15:14:00.957Z] TOOL RESULT

```
1618. — '^  .  .  .  e  particolarmento  delle donne  che,  battondosi  il  petto  e  faoendo gesti  di  grandissima  oompassione  replicano spesso  con  gran  dolore  quegli  ultimi  vend  di certi  loro  cantici :  Vah  Hussein  1  ''^ Hnssein  I  "—P,  della  V(UU,  i,  ^2.
HOBSON-JOBSON.
```


## [2026-09-06T15:14:02.664Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=11174 && NR<=11175' HJB.txt | head -c 2500"
}
```


### [2026-09-06T15:14:04.254Z] TOOL RESULT

```
"The  commonalty  of  the  Mussalmans, and  especially  the  women,  have  more  regard for  the  memory  of  Hasan  and  Husein,  than for  that  of  Muhammad  and  Ids  khalifs.  The heresy  of  making  Ta'ziyas  (see  TAZEEA)  on the  anniversary  of  the  two  latter  inuSEms,  is most  common  throughout  India :  so  much so  that  opposition  to  it  is  ascribed  by  the ignorant  to  blasphemy.  This  example  is followed  by  many  of  the  Hindus,  especially the  Mahrattas.  The  Muharram  is  celebrated throughout  the  Dekhan  and  Malwa,  with greater  enthusiasm  than  in  other  parts  of India.  Grand  preparations  are  made  in every  town  on  the  occasion,  as  if  for  a  festi- val of  rejoicing,  rather  than  of  observing the  rites  of  mourning,  as  they  ought.  The observance  of  this  custom  has  so  strong  a hold  on  the  mind  of  the  commonalty  of  the Mussulmans  that  they  believe  Muhammad- anism  to  depend  merely  on  keeping  the memory  of  the  im^ms  in  the  above  manner." —Mir  ShaAamat  *Ali,  in  J,R,  As,  Soc,  xiii. 369.
We  find  no  literary  quotation  to exemplify  the  phrase  as  it  stands. [But  see  those  from  the  Orient.  Sporting Mag.  and  Nineteenth  Century  below.] Those  which  follow  show  it  in  the process  of  evolution :
```


## [2026-09-06T15:14:05.940Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=11172 && NR<=11173' HJB.txt | head -c 2500"
}
```


### [2026-09-06T15:14:07.816Z] TOOL RESULT

```
H0B80N-J0B80N,  s.  A  native festal    excitement ;     a    tamdsha    (see
TIJMA8HA) ;  but  especially  the  Mo- harram  ceremonies.  This  phrase  may be  taken  as  a  typical  one  of  the  most highly  assimilated  class  of  Anglo- Indian  argot,  and  we  have  ventured to  borrow  from  it  a  concise  alternative title  for  this  Glossary.  It  is  pecidiar to  the  British  soldier  and  his  surround- ings, with  whom  it  probably  originated, and  with  whom  it  is  by  no  means obsolete,  as  we  once  supposed.  My friend  Major  John  Trotter  tells  me that  he  has  repeatedly  heard  it  used by  British  soldiers  in  the  Punjab ;  and has  heard  it  also  from  a  regimental Moonshee.  It  is  in  fact  an  Anglo- Saxon  version  of  the  wailings  of  the Mahommedans  as  they  beat  their breasts  in  the  procession  of  the  Mo- harrwmr—''Y&  Hasaa!  Y&  Hosain!' It  is  to  be  remembered  that  these observances  are  in  India  by  no  means confined  to  Shi'as.  Except  at  Luck- now  and  Murshidabad,  the  great  ma- jority of  Mahommedans  in  that  country are  professed  Sunnis.  Yet  here  is  a statement  of  the  facts  from  an  unex- ceptionable authority :
```


## [2026-09-06T15:14:14.881Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"hobson.jobson\" FSD_vol2.txt | head -5"
}
```


### [2026-09-06T15:14:14.936Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:14:15.478Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"harmattan\\|marrano\\|maranatha\" SKT.txt LKT.txt DEV.txt PHN.txt WEB_vol1.txt 2>/dev/null | head -20"
}
```


### [2026-09-06T15:14:15.544Z] TOOL RESULT

```
LKT.txt:3255:'Schein';  hiei'aus  mit  roman.  Endung sp.  wrtnvjHo'chrisIlicli  gewordener  Jude' : man  nahm  an,  daß  die  Marranos  nur zum  Schein  übergetreten  seien;  pg. marrano,  marräo.  [Andere  Ableitung ZDMG  XXIII,  637  ]
LKT.txt:3454:'Verbotenes'  [part.  pass.  II  fem.  des  Vbs. harama,  s.  hier  Nr.  819];  hieraus  sp. (dial.  Andalusien)  muharrana  'frische Speckseite',  sp.  marrano  'Schweine- fleisch', marrana  'frisches  Schweine- fleisch', pg.  marrao  'ganz  kleines Schwein',  marra  'frisches  Fleisch  davon'. —  [Dagegen  muß  warrano'übergetretener Jude'  anderen  Ursprungs  tein,  s.  hier Nr.  1412.]    [Eguilaz  446.    ML  5636.
LKT.txt:8259:marrano  1412
WEB_vol1.txt:112720:Cies of na? ”. [Maracana Mar’a. pect in Brazil; Rr eE] SAE ar anath’4, + Same as maypop. axe Maran atha Wot: maranatha, from Ara- fon to the jo, the Lord cometh.] an invo- ord, sometimes regarded as
```


## [2026-09-06T15:14:20.500Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3248,3262p' LKT.txt\necho \"==========\"\nsed -n '3448,3460p' LKT.txt\necho \"===== nr 819 (harama)\"\ngrep -n \"819\\.\" LKT.txt | head -20"
}
```


### [2026-09-06T15:14:20.567Z] TOOL RESULT

```
1409.  Ar.  innrassi:
Auch  mirassa  'Gießkanne"';  hieraus  siz. marascia  'Ölkrug'  oder  'anderes  Gefäß in  dieser  Form'.    [GrSVociSic  240.
1410.  Ar.  marliüt:
'Gebunden'  [pari.  pass.  von  rahata 'binden,  fromm  sein'];  hieraus  frz. marabout  'Einsiedler',  ein  heiligmäßiger Mann,  der  nach  seinem  Tode  in  einer Kapelle  begraben  wird  und  dort  Ver- ehrung findet;  das  Wort  wird  auch fälschlich  auf  diese  Grabkapelle  selbst bezogen ;  sp.  morabito,  pg.  marabuto, rum.  marabut  'Einsiedler',  siz.  mura- bitu  'Abstinenzler';  engl,  maraboot; ferner  wegen  des  ernsthatten  Aussehens des  Vogels  sp.  marabA  'Riesenstorch vom  Senes^al  oder  aus  Indien,  Lepto- ptilus  argaia  Gray.',  dtsch.  Marabu,  engl. marabou.  —  Dagegen  muß  sp.  morabito 'Seemann'  auf  ar.  muräkibi  'dass.'  zu- rückgehen. [Devic  DEt  157.  Eguilaz  443. GrSVociSic  242.
1411.  Ar.  mardakiis:
'Majoran'  [wohl  selbst  fremden  Ur- sprungs, etwa  lat.  amaracutn],  vulg. Aussprache  mardadüs;  hieraus  sp.  al- moraduj,  almoradux  [worin  früher  x wie  s  gesprochen  wurde],  kat.  moradux 'Majoran.'  [DE  174.  Eguilaz  236.
1412.  Hebr.  mar'e:
'Schein';  hiei'aus  mit  roman.  Endung sp.  wrtnvjHo'chrisIlicli  gewordener  Jude' : man  nahm  an,  daß  die  Marranos  nur zum  Schein  übergetreten  seien;  pg. marrano,  marräo.  [Andere  Ableitung ZDMG  XXIII,  637  ]
1413.  Ar.  uiarfaka:
'Kissen';  hieraus  sp.  marfaga.  märaga, almarrega,  pg.  almäfega  'grobe  Woll- decke' [früher  als  Zeichen  der  Trauer getragen,  Gonstancio  Dicc  55  b],  kat. marfega  'Slrohsack',  Ableitung  marfe- gassa  'Schlampe',  prov.  marrego  'Stroh- sack'. [DE  158.  Eguilaz  215/216.  ML 5350.
1414.  Ar.  iiiarfüd: 'Zurückgewiesen'  [part.  pass.  von  rafa- da]\  hieraus  sp.  pg.  marfuz  'gemein, werllos'  [z.  B.  Don  Quijote  I,  cap.  XL, in  der  Collecciön  de  autores  espanoles  III. Leipzig.  S.  283  Mitte] ;  kat.  marfus,  it. (alt)  malfusso,  (dial.  Neapel)  maj-fuso, sard.  (log.)  marfusu  'verworfen,  schur- kisch'. [DE  391/392.  WAGNER  in  Herrigs Archiv  CXL,  243.
1415.  Ar.  marg:
'Wiese,  Sumpf;  hieraus  siz.  margiu 'sumpfiger  Ort,  Sumpf,  früher  'Wald- land' ;  sp.  ahnarcha,  armajal,  pg. almarge,  almargem  'Stadt  in  flachem Lande'.  [Eguilaz  214.    GrSVociSic  240.
113
[Ar.  margan.
==========
Part,  praes.  III  des  Vbs.  gära  [s.  hier 669]  'einen  kriegerischen  Zug  machen, eine  gära  veranstalten',  also  'Krieger'; hieraus  mit  ar.  Art.  sp.  pg.  almogävar 'leicht  bewaffneter  Krieger,  leichte  Rei- terei', kat.  almogaver.  Dazu  ar.  mugä- wara  'Kriegszug' ;  hieraus  asp.  almogava 'kriegerischer  Zug'.  [DE  172.  Eguilaz  233.
1497.  Ar.  muhajjar:
'Stoff  aus  Ziegenhaar';  hieraus  zur  Be- zeichnung von  allerlei  Stoffen  it.  moca- jardo,  mocajarro,  camojardo,  frz.  mouca- yarde;  russ.  muhnjar,  poln.  muchair; hieraus  dtsch.  Macheier.  Engl,  mohair, frz.  moiri,  it.  amuerre,  sp.  muer,  muarS, dtsch.  Mohär,  Moir^,  Mohr.  Vb.  frz. moirer  'einen  Stoff  moirieren'.  [Kluge 293.  Mikl  SIEtWb  204a.  ML  5635  u. 5640.    ZfromPh  X,  575.    MWiD  95.
1498.  Ar.  muhakk: 'Probierstein  für  Edelmetalle',  tk.  mehak, mehek  [Kelekian  Kärnüs  1130aJ,  vulg. mehenk  [ebenda  1254a]  'dass.';  hieraus
rum.  mehenghiü  'Probierstein;  durch- trieben, schlau'.
1499.  Ar.  uiiiharrania:
'Verbotenes'  [part.  pass.  II  fem.  des  Vbs. harama,  s.  hier  Nr.  819];  hieraus  sp. (dial.  Andalusien)  muharrana  'frische Speckseite',  sp.  marrano  'Schweine- fleisch', marrana  'frisches  Schweine- fleisch', pg.  marrao  'ganz  kleines Schwein',  marra  'frisches  Fleisch  davon'. —  [Dagegen  muß  warrano'übergetretener Jude'  anderen  Ursprungs  tein,  s.  hier Nr.  1412.]    [Eguilaz  446.    ML  5636.
1500.  Ar.  muharrig: 'Spaßmacher'  [von  haraga  'sprechen, plaudern',  harräg  'Spaß',  vgl.  darüber Carlo  Gi  af  v.  Landsberg,  Jeder  tut,  was ihm  paßt,  denn  reden  werden  die  Leute immer.  Festgabe  zu  seinem  40jährigen Jubiläum  als  Orientalist.  Leiden  1909. S.27/29];  hieraus  sp.  moharrache  'dass.'; Begriff  u.  Wt.  ist  jedenfalls  von  den Damaszener  Umajjaden  nach  Spanien mitgebracht  worden.  —  ,In  Damask  ist harg  der  Spaß,  und  fann  at  tahrlg  ist die  Kunst,  eine  drastische  Erzählung  so vorzutragen,  daß  die  Zuhörer  belustigt werden.  Dies  geschieht  durch  eine  maß- lose Übertreibung  bei  Darstellung  der Gefühle,  verbunden  mit  einer  karikatur- artigen Mimik  und  Gestikulation.  Das Tahrig  gehört  neben  Musik,  Tanz, Taschen-  und  Schattenspiel  zu  den  Be- lustigungen einer  größeren  Damaszener Abendgesellschaft.  —  Der  Meister  Mo- harrig,  oft  ein  ganz  vortreff  licher  Ko- miker, ist  jedenfalls  eine  weit  erquick- lichereErscheinung  als  unser  langweiliger Deklamator  im  schwarzen  Frack  und weißen  Handschuhen.  Bei  öffentlichen Aufzügen  ist  er  der  Harlekin,  phan- tastisch gekleidet,  mit  geschwärztem  Ge- sicht und  den  Fuchsschwänzen  auf  dem spitzen  Filzhut. "  WETZSTEIN  in  ZDMG XXII,  132.  —  [DE  307/308.
1501.  Ar.  luuhätara:
'Gefahr,  Risiko'  [vom  Vb.  hatara  III 'wagen,  riskieren'],  eigentlich  bai^  mu- hätara  'ein  gewagter  Kauf,  d.  h.  einer, bei  dem  man  ein  Risiko  eingeht.  Hieraus sp.  mohatra,  pg.  mofatra  'wucherischer Verlrag'.    [DE  316.    Eguilaz  456.
1502.  Ar.  muhräz:
Auch  »nVirS? 'Schusterahle';  hieraus  mit ar.  Art.  u.  Imäla  [ä  >  e]  pg.  almofrez 'dass.'  [Constancio  Dicc  57  b],  wohl  auch sp.  almarada  'Ahle  des  Halfasohlen- schusters,  Stilett';  jedoch  kann  pg.  al- mofate  'Ahle'  [Constancio  Dicc  57  a] nicht,  wie  DE  170/171  meint,  durch vielfache  Änderung,  hieraus  entstanden sein,  sondern  muß  mit  Eguilaz  232  auf
121
===== nr 819 (harama)
1981:819.  Ar.  harüni:
4122:1819.  Ar.  samüm:
```


## [2026-09-06T15:14:29.570Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1981,1995p' LKT.txt\necho \"===== harmattan in LKT\"\ngrep -n -i \"harmat\\|harmattan\" LKT.txt | head"
}
```


### [2026-09-06T15:14:29.629Z] TOOL RESULT

```
819.  Ar.  harüni:
'Verboten';  dasjenige,  wozu  der  Zutritt verboten  ist,  also  der  'Frauenraum'  und schließlich  'die  Frauen'  selbst;  ebenso tk.  harem  ;  hieraus  rum.  haretn,  STp.  Haren, pg.  frz.  engl,  harem,  ndl.  dtsch.  Harem; bulg.  serb.  hurem,  öech.  harim,  poln. harem,  russ.  gar^m.  In  der  ursprüng- lichen Bedeutung  'unerlaubt'  ist  aus  dem Tk.  rum.  haram  'nichtsnutzig,  ungesetz- lich' geworden.
820.  Pers.  häräiuzädä: 'Bastard,  Hurensohn'  [aus  ar.  haräm, s.  hier  Nr.  819,  und  zädä  'geboren',  s. hier  Nr.  69b];  hieraus  angloind.  haram- zadeh,  in  Indien  ein  allgemein  gebrauch-
65
[Ar.  harätni.
lieber  Ausdruck  der  Verachtung  [Slang Dictionary.^'  1864.  S.  151].
821.  Ar.  haräml:
'Räuber'  [vom  gleichen  Stamme  wie Nr.  819];  hierzu  der  plr.  harämija;  hier- aus in  singl.  Bedeutung  bulg.  aramija 'Dieb',  serb.  klruss.  harämija  'Dieb, Straßenräuber'.  —  Aus  Jj,arämt  und  tk. bas,  s.  hier  Nr.  260,  wurde  rum.  ha- rämbaf  'Räuberhauptmann',  vielleicht auch  bulg.  grabez  'Straßenraub'.
822.  Tk.  harar:
'Große  Satteltasche  aus  Ziegenleder,  die man  den  Lasttieren  aufladet'  [Kölekian Käniüs  534a];  hieraus  rum.  arar  'Plane, Wagendecke'.
823.  Ar.  liarba:
'Lanze',  aber  auch  die  'eiserne  Lanzen- spitze' an  der  etwa  4  m  langen  Be- duinenlanze mizrak  [s.  hier  Nr.  1476; vgl.  FISCHER  in  MSOS  II,  233];  hier- aus mit  ar.  Art.  it.  labarda,  alabarda, frz.  hallebarde,  sp.  pg.  alabardo  'Helle- barde', pg.  hallabarda,  mhd.  mit  Volks- etymologie helmbarte.  Dazu  siz.  lapar- deri  'Gauner,  Erpresser,  Betrüger',  la- parduni  'Drohne'  [man  war  der  Mei- nung, die  Hellebardiere  lebten  vom  er- preßten Gute  anderer].  Mit  vorgesetztem mu  des  Partizips  ergibt  sich  ar.  *muharba, hieraus  sp.  moharra  'Lanzenspitze'. Über  das  Tk.  wurde  rum.  arbiu  'Lade- stock'.   [DE  316     ML  4040.
824.  Pers.  härbuz:
"Melone'  [aus  'här  'Esel'  Horn  NpEt S.  104,  Nr.  473  "und  buz  'Ziege'  ebenda S.  49,  Nr.  213,  also  'Eselsziege',  nicht 'Eselsgurke',  wie  Horn  NpEt  S.  105  hat; die  dort  in  Anm.  1)  fehlende  Band-  und Seitenzahl  in  Brugsch,  Reise  der  K. Preuß.  Gesandtschaft  nach  Persien,  ist: Bd.  I,  S.  334/336.  Übrigens  scheint  sich BRUGSCH  die  dort  erzählte  „nicht  sehr geistreiche"  Volksetymologie  des  Wts. nicht  haben  aufbinden  lassen,  da er  sie  selbst  als  eine  „einfältige  Ge- schichte' bezeichnet];  ebenso  Ik.karpiiz [vgl.  ngr.  KapTTOüöia];  hieratis  rum.  car- puz,  carpus  'Melone,  Cucurbita  citrullus', bulg.  serb.  karpuz,  serb.  karpuza,  poln. karbuz,  garbuz,  harbuz,  arbuz,  klruss. garbuz,  russ.  arbuz  'Wassermelone'. [Gorjajew  5.    Bern  SlEtWb  491.
825.  Ar.  harg:
===== harmattan in LKT
```


## [2026-09-06T15:14:38.165Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt; do echo \"== $f\"; grep -n -i \"hobson\" $f | head -4; done"
}
```


## [2026-09-06T15:14:39.643Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"ihram\\|hirawen\\|harem\" AID.txt RCH.txt 2>/dev/null | head -8\necho \"=== AHD watkins\"\ngrep -n -i \"hobson\" AHD_watkins1985.txt | head -3"
}
```


### [2026-09-06T15:14:40.277Z] TOOL RESULT

```
== FSD_vol1.txt
65622:Syn.:  election,,  option,  preference,  selection,  volition Option  Is  the  right  or  privilege  of  choosing;  choice  may be  either  the  right  to  choose,  the  act  of  choosing,  or  the thing  chosen;  volition  is  the  determination  to  perform the  act  or  attain  the  end  which  has  become  the  object  of choice.  See  alternative  —   Prep.:  a   choice  between  (or betioixl)  two:  by  vote  or  lot;  of,  among,  out  of,  or  from  among many;  for  the  service;  best  choice  for  him.—  at  choice,  at one’s  wish.—  choIce'*drawn"t,  a.  Carefully  selected.—  c.» note,  n.  Mus.  One  of  several  notes  printed  together  on  a score  so  that  a   singer  may  take  his  choice  of  them.—  c.  (reac- tion, n.  Psychol.  A   reaction  Involving  choice  between  dif- ferent stimuli.—  Hobson's  c.,  this  or  nothing;  something with  no  alternative.  Thomas  Hobson,  a   livery-stable  keep- er of  Cambridge,  England,  who  required  his  customers  to take  the  horse  nearest  the  door.]  —   to  be  at  one’s  c.t,  to behave  as  one  prefers.— with  c.  1.  As  one  prefers.  2. In  a   discriminating  or  refined  manner.— without  c.,  with- out discrimination;  promiscuous  —   cholce'ful,  a.  [Rare.] 1.  Fickle;  changeable.  2.  Varied.—  cholce'less,  a.  [Rare.]
== FSD_vol2.txt
46590:navy:  rc.signed  in  1903;  with  seven  companions  sank  the collier  "Merrimae"  in  an  attempt  to  bottle  up  Admiral Cervera's  fleet  in  the  mouth  of  Santiago  harbor,  June  3, 1898:  member  of  Congress,  1907-15;  author  and  lec- turer. 2.  Thomas  (1544-‘  /il631),  an  English  liveryman. See  Hobson’s  choice,  under  choice. hob'.sondob'son,  l   heb'san'lob'sen;  2   hflb'son-jOb'son,  n. tAnglO'Ind.]  Name  of  the  annual  celebration  of  the  Muha- ram  of  the  Shiah  Muslems,  their  name  being  a   corruption of  the  cry  of  "   Ai  Hasan!  A1  Hosainl  ”   raised  at  the  great procession  on  the  10th  day  of  the  solemnity.  Yule  and Bdknbll  Hobsen^Jobson  p.  419.  [J.  m.  ’03.] hob'stap",  n.  See  under  hob',  ?i.
== FSD_vol3.txt
== FSD_vol4.txt
104625:Maryland,  died.  1899:  John  H   Copleston,  English  Journal-  1695:  Xaval  Constructor  R   P   Hobson
```


### [2026-09-06T15:14:40.356Z] TOOL RESULT

```
AID.txt:2758:Harem.  [Hindustdni  harim ,   from  the Arabic  haratn ,   sacred,  forbidden.] The  portion  of  a   house  which  is reserved  for  the  women  of  a   family  ; thence  the  women  themselves,  the wives  and  concubines  of  a   Musal- mdn  collectively.
=== AHD watkins
```


## [2026-09-06T15:14:46.503Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\ncum=0; ff=[]\nfor l in lines:\n    ff.append(cum); cum+=l.count('\\f')\nprint('leaf',ff[46589])\nEOF\nsed -n '46580,46592p' FSD_vol2.txt | grep -o \"11[0-9][0-9]\" | head\necho \"---context---\"\nsed -n '46585,46589p' FSD_vol2.txt | head -c 800"
}
```


### [2026-09-06T15:14:48.394Z] TOOL RESULT

```
leaf 456
1166
---context---
2.  [Rare.]  To  clink  glasses  in  drinking.  lio!j'sand!Hob"t; hob'»a»nob"t;  liob'sor*n«ll}"|. hob'nob",  adti.  [Archaic.]  1.  Take  it  or  leave  It:  a   familiar form  of  invitation  in  drinking.  2,  Hit  or  miss;  at  random. [   <   AS.  habhan,  have,  +   nabban,  not  have.]
Sio''bo,  1   hS'bo;  2   hO'bo,  n.  [U.  S.J  An  idle,  shiftless,  wandering workman,  ranking  scarcely  above  the  tramp.  —   ho'bo- !sm,  n.
Ho 'bo-ken,  1   hO'bo-ken;  2   ho'bo-kto,  n.  A   city  in  Hudson county,  N.  .T.,  opposite  New  York  city.
Iiob''o-niok'ko,  1   hob'o-mok'o;  3   hOb'o-mdk'o,  ».  [Am. Ind.]  An  evil  spirit;  a   devil.
Hob 'son,  1   heb'san;  2   hdb'son,  n.  1.  Efchraond  Pearson (s  /   II 1 870-  ) ,   a   mechanical  engineer  in  the  United
```


## [2026-09-06T15:14:55.882Z] TOOL CALL #24: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:14:55.890Z] TOOL RESULT

```


```


## [2026-09-06T15:14:59.200Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/harem",
 "prompt": "Full etymology of harem: Arabic source, route into English (Turkish?), dates."
}
```


## [2026-09-06T15:15:00.260Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/harmattan",
 "prompt": "Full etymology of harmattan: language of origin, whether via Spanish, Twi/Fante, Arabic haram, date of first attestation."
}
```


### [2026-09-06T15:15:04.442Z] TOOL RESULT

```
# Etymology of Harem

**Arabic Origin:**
The word traces back to Arabic *haram*, which originally meant "something forbidden or kept safe," derived from the root of *harama* meaning "he guarded, forbade."

**Route into English:**
The term entered English through Turkish *harem* in the 1630s, referring to "part of a Middle Eastern house reserved for women." By 1784, it was used in English to describe "wives, female relatives and female slaves in a Middle Eastern household."

**Key Dates:**
- **1630s**: First appearance in English
- **1911**: Introduction of the harem-skirt in fashion
- **1921**: Harem pants first attested; became fashionable around 1944

The journey demonstrates the word's transmission from Arabic through Turkish intermediaries before adoption into English vocabulary during the early modern period.
```


### [2026-09-06T15:15:05.462Z] TOOL RESULT

```
I've reviewed the web page content provided, but it appears to be the header, navigation, and footer of the Etymonline website rather than an actual etymology entry. The page doesn't contain specific information about the word "harmattan" or its etymology.

To answer your question about harmattan's origins, language of origin, Spanish/Twi/Fante/Arabic connections, and first attestation date, I would need the actual etymology entry from Etymonline, which isn't included in the content you've shared.

If you could provide the actual harmattan entry from the dictionary, I'd be happy to extract and summarize that etymological information while following your specified guidelines.
```


## [2026-09-06T15:15:07.943Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/harmattan",
 "prompt": "Etymology of harmattan: source languages (Spanish? Twi/Fante/Akan? Arabic haram?), forms cited, dates."
}
```


## [2026-09-06T15:15:09.154Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/marrano",
 "prompt": "Etymology of English/Spanish marrano: is it from Arabic muharram 'forbidden' or Hebrew, and how does the 'converted Jew' sense relate to 'pig'?"
}
```


### [2026-09-06T15:15:12.710Z] TOOL RESULT

```
# Harmattan Etymology

The word "harmattan" derives from **Twi (Akan language)** _haramata_ or a related term, which also influenced the Spanish _harmatán_.

The ultimate origin remains uncertain, though some scholars propose an **Arabic source**. The Arabic word _حَرَام_ (ḥarām, meaning "accursed thing") has been suggested as a possible root.

**Key etymology chain:**
- Twi/Akan → English/Spanish
- Possible Arabic origin (unconfirmed)

The Wiktionary entry notes this etymological uncertainty: "The ultimate origin is supposed by some to be an Arabic word, but which one is uncertain."
```


### [2026-09-06T15:15:16.358Z] TOOL RESULT

```
# Etymology of "Marrano"

Based on the Wiktionary entry, the word's origin is clearly documented:

**Arabic Source:** The term derives from Arabic مُحَرَّم (muḥarram), meaning "forbidden." This etymology appears consistently across multiple language sections—Spanish, Italian, and Portuguese all trace the word back to this Arabic root.

**Connection to "Pig":** In Spanish, the primary definition is "pig," with the etymology explicitly stating it refers to "pigs" as forbidden animals in Islamic tradition. The entry notes: "Borrowed from Arabic مُحَرَّم (muḥarram, 'forbidden') as referring to pigs."

**Link to "Converted Jew":** The derogatory historical sense—referring to Jews who converted to Catholicism—appears to be a secondary application of the term. By calling converted Jews "marrano" (literally "forbidden" or "pig"), Spanish speakers applied an insulting epithet that originally designated ritually forbidden swine.

The document makes no mention of Hebrew origins. The semantic progression moves from the Arabic word for "forbidden" → the forbidden animal (pig) → a derogatory label for religious converts.
```


## [2026-09-06T15:15:33.054Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/maranatha",
 "prompt": "Etymology of maranatha: Aramaic maran atha 'our Lord come' vs Klein's Hebrew mohoram atta 'you are under ban'. What does Wiktionary say, and is the curse interpretation mainstream?"
}
```


## [2026-09-06T15:15:35.288Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AD%D8%B1%D9%85#Arabic",
 "prompt": "Arabic root ح ر م: verb harama/haruma meanings, derived nouns haram, harim, hurma, ihram, muharram, hirman. Also Proto-Semitic reconstruction if given."
}
```


### [2026-09-06T15:15:38.221Z] TOOL RESULT

```
# Maranatha Etymology: Wiktionary's Account

According to Wiktionary, **maranatha derives from Aramaic**, specifically:

> "Aramaic מרנא תא ('Lord, come!') or מרן אתא ('our lord has come')"

The entry presents the term as originating through Ancient Greek intermediary forms before reaching Latin.

## Regarding the "Curse" Interpretation

The Wiktionary article provided contains **no mention of a curse interpretation** or Klein's Hebrew theory ("mohoram atta"). The entry focuses exclusively on the Aramaic meaning as a religious invocation or proclamation rather than a curse.

This suggests that if the curse interpretation exists in scholarly discourse, it is not featured in this particular Wiktionary entry. To determine whether it represents a mainstream academic view would require consulting additional sources beyond what's presented here.
```


### [2026-09-06T15:15:42.783Z] TOOL RESULT

```
# حرم (Haram) - Wiktionary Summary

## Arabic Root ح ر م

The Arabic root **ḥ r m** generates multiple related terms with interconnected meanings centered on concepts of sacredness and prohibition.

## Core Verb Forms

**حَرُمَ (ḥaruma)** and **حَرِمَ (ḥarima)** - Form I verbs with meanings including:
- "to be sacred, sacrosanct, inviolable"
- "to be forbidden, prohibited, unlawful"

**حَرَّمَ (ḥarrama)** - Form II verb meaning "to declare sacred" or "to forbid/interdict"

## Derived Nouns

**حَرَم (ḥaram)** - Functions as both adjective ("forbidden, sacred") and noun:
- Sacred object or possession
- Wife
- Sanctuary/sacred precinct (notably "al-ḥaramayn" - Mecca and Medina)

**حِرْم (ḥirm)** - "Deprivation; excommunication; pilgrim's cloak"

**حُرْم (ḥurm)** - "Anything sacred"

**إِحْرَام (iḥrām)** - Pilgrim's ritual state of consecration

**مُحَرَّم (muḥarram)** - "Sacred month" (first Islamic month)

## Linguistic Spread

The term traveled through Ottoman Turkish, Persian, and Urdu, eventually entering European languages including English "harem" via Turkish intermediaries.
```


## [2026-09-06T15:15:48.993Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in حرمان حرمت احرام محرّم; do echo \"== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done\necho \"=== BQT v2 حرام\"\ngrep -n \"حرام\" BQT_v2_pages.txt | head -5"
}
```


### [2026-09-06T15:15:50.662Z] TOOL RESULT

```
== حرمان
MON_part1.txt:5
MON_part2.txt:4
== حرمت
MON_part2.txt:12
MON_part1.txt:16
== احرام
MON_part2.txt:3
MON_part1.txt:8
== محرّم
MON_part1.txt:0
MON_part2.txt:0
=== BQT v2 حرام
608:‫نادوخته راکوبند" ‪ -‬وبمعنی‌قبای پوشیدنی هم‬                                                       ‫حرامزاده را کوبند ‪۰‬‬
8514:                                                            ‫که درمقابل حرام باشد ‪ -‬وبمعنی مصطکی هم‬
12348:                                                                       ‫حرامزاده رااگویند ؛ ویض اول هم آمده است‪.‬‬
12633: ‫و(‪)٤‬‏ سياه رنگ و تره باشند‬     ‫یکبودی همابل‬           ‫هم آمده‬    ‫و بقتح اول‬         ‫؛‬       ‫حرامزاده را گونند ‪۴‬‬
12649:              ‫رك‪:‬خشود ‪ «- ۴ .‬خشوك‪ ,‬حرامزاده باشد ‪ .‬مذجيك (ترمذی) گوید ‪:‬‬                                    ‫‪۴‬‬
```


## [2026-09-06T15:15:54.380Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"حرمان\" MON_part1.txt | head -6\necho \"---\"\ngrep -n \"حرمت\" MON_part1.txt | head -8"
}
```


### [2026-09-06T15:15:54.455Z] TOOL RESULT

```
21551:پر از باس و حرمان و بدیختی داند؛ مق. 
30444:مسحرمان اسرار» اولیای مستور. ملایکةٌ 
53063:حرمان: ۵*5۰ [ع.] (مصل.) بی‌بهره 
73535:محرمانةٌ دو یا چند تن با یکدیگر. 
94260:چیزی که موجب این ناتوانی یا حرمان است. 
---
2917:مهربانی» محست. حرمت» احترام» عرت. باد» 
7721:احترام: «قعه [ع.] (مسصم ۰ حرمت 
7722:داشتن» بزرگک داشتن. (امسص.) حرمت» 
7910:حرمت شدن, در حرمتی در آمدن که هتکك 
8907:حرمت» باس. تأدیب» تنبیه. دانشی است که 
9201:ذمه) حقوق» حرمت‌ها» آیروها. 
9840:قدر» ر تبه» مر تمه» درجه چاه مقام. حرمت» 
15803:(امص.) زرخداف؛ حرمت. احسان» انعام؛
```


## [2026-09-06T15:15:59.593Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '53060,53066p' MON_part1.txt\necho \"=== حرمت entry\"\ngrep -n \"^حرمت\\|حرمت: \" MON_part1.txt MON_part2.txt | head -5\necho \"=== احرام\"\ngrep -n \"احرام: \\|^احرام\" MON_part1.txt MON_part2.txt | head -5\necho \"=== حسن / احسن\"\ngrep -n \"^حسن: \\|حسن: .*\\[ع\" MON_part1.txt MON_part2.txt | head -5\ngrep -n \"احسن: \" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T15:15:59.746Z] TOOL RESULT

```
پردگیان؛ برده‌نشینان» زنان عقدی و صیغه و 
کنیزان مرد؛ ج. احرام. 

حرمان: ۵*5۰ [ع.] (مصل.) بی‌بهره 
بودن» بی‌روزی ماندن. (امص.) بی‌بهرگی» 
بی نصیبی» نومیدی. 

=== حرمت entry
MON_part2.txt:36666:حرمت او را نگهداشتن» جانب او را مراعات 
MON_part2.txt:47406:حرمت آن مورد شک و خلاف است). 
MON_part2.txt:89047:هتکك حرمت: : شکستن "حرمت» بی‌احترامی 
MON_part1.txt:7910:حرمت شدن, در حرمتی در آمدن که هتکك 
MON_part1.txt:8907:حرمت» باس. تأدیب» تنبیه. دانشی است که 
=== احرام
MON_part1.txt:7907:احرام: سقعه [ع.] (.) ج. 0 و حریم: 
MON_part1.txt:7908:احرام: اور ارت [ع. ۰[ (مص‌ل ۳ له حصج 
MON_part1.txt:8102:احرام (در حج). 
MON_part2.txt:63205:احرام عمره و حج؛ ج. مقصر ین. 
=== حسن / احسن
MON_part2.txt:49538:محسن: ۱۵۲۵۸۸ [ع.] (امف.) احسان شده؛ 
MON_part1.txt:7982:احسن: 251 [ع.] (رص.) نیکوتر) بهتر) 
MON_part1.txt:53324:حسن: ِ [ع. ۰] (امص.) زیابی» جمال» 
MON_part1.txt:7982:احسن: 251 [ع.] (رص.) نیکوتر) بهتر) 
MON_part1.txt:7983:اعلی» احمد» اولی. به نحو احسن: به بهتر ین
```


## [2026-09-06T15:16:11.632Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"^Muharram\\|Muharram,\" KLN_1966.txt | head -3\necho \"=== AFM/Asbaghi? not relevant. Check RCH for hosn/hasan\"\ngrep -n -i \"hosn\\|husn\" RCH.txt | head -5"
}
```


### [2026-09-06T15:16:11.706Z] TOOL RESULT

```
22983:marram  grass,  bent  grass.  —  ON.  maralmr,  lit. ‘sea  grass’,  fr.  mart,  ‘sea’,  and  halmr,  ‘straw’. See  mere,  ‘sea’,  and  haulm, marrano,  n.,  Jew  or  Moor  converted  to  Chris¬ tianity.  —  Sp.,  ‘pig,  hog’,  fr.  Arab,  hdruma,  ‘was forbidden’.  The  pig  was  called  the  ‘forbidden animal’,  from  the  fact  that  the  eating  of  pork  is forbidden  by  Jewish  and  Moslem  religious  law. Cp.  (Andalusian)  Sp.  maharrana,  ‘fresh  bacon, salt  pork’,  which  derives  fr.  Arab.  muhdrramah, fern,  of  muharram,  ‘anything  forbidden’,  pass, part,  of  harrama.  See  harem  and  herem.  For  the change  of  m  to  n  cp.  maranatha. marriage,  n.  —  ME.  mariage,  fr.  OF.  (  =  F.) mariage,  fr.  VL.  maritaticum  (occurring  in  a text  from  the  year  1062),  fr.  L.  maritatus,  pp.  of maritare,  ‘to  wed,  marry,  give  in  marriage’.  It. maritaggio,  Sp.  maridaje,  ‘marriage’,  also  derive fr.  VL.  maritaticum.  See  marry  and  -age. marron,  n.,  the  European  chestnut.  —  F.  See maroon,  ‘brownish  red’.
24598:Muharram,  also  Moharram,  n.,  the  first  month  of the  Mohammedan  year.  —  Arab,  muharram ,  lit. ‘sacred,  forbidden’,  pass.  part,  of  harrama,  ‘he forbade’,  II  (=  intensive)  conjugation  of  hd- rama,  ‘he  forbade’,  haruma,  ‘was  forbidden’.  See harem,  herem.
=== AFM/Asbaghi? not relevant. Check RCH for hosn/hasan
2708:An  incomparable  man;  the  one  of  ones;  a   phosnix.
8871:A   aghsaUf  (pi.  of  ghusn)  Branches.  Ighsan^  (iv of  ^^«ae)  Growing  large  in  the  grain  (a  bunch  of  grapes).
13836:A   *J:-Jy  iydlat  (from  Jjl),  Governing.  Dominion,  prefec- ture, administration,  rule.  husn^i  iydlaij  Good  go- vernment. p   iyalai  kardan^  To  govern,
33688:gant. Husny  Beauty.  Goodness,  elegance. husn^i  ikhtiyar  (or  iradal)y  Free-wjll.  uljl
33689:husn-i  addby  Good  manners,  ^   husn^i  bi  nazir,
```


## [2026-09-06T15:16:19.323Z] TOOL CALL #35: Bash

```json
{
 "command": "pdftoppm -f 222 -l 222 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg222 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:16:21.981Z] TOOL RESULT

```
total 2236
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:16 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    462 Sep  6 11:14 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
```


## [2026-09-06T15:16:24.891Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg222.png"
}
```


### [2026-09-06T15:16:25.379Z] TOOL RESULT

```

```


## [2026-09-06T15:16:25.376Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:16:38.810Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 222 -l 222 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg222hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg222hi.png'); print(im.size)\n# scale factor from 200dpi page (1700x2200) to 400dpi\nim.crop((1400,760,2500,920)).save('c_herman.png')\nim.crop((800,1520,2000,1620)).save('c_harmathan.png')\n\""
}
```


### [2026-09-06T15:16:42.110Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T15:16:44.114Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_herman.png"
}
```


### [2026-09-06T15:16:44.128Z] TOOL RESULT

```

```


## [2026-09-06T15:16:47.122Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg222hi.png')\nim.crop((2100,830,2700,930)).resize((1200,200)).save('c_herman2.png')\nim.crop((850,1620,2100,1740)).save('c_harmathan.png')\n\""
}
```


### [2026-09-06T15:16:49.425Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:16:51.089Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_herman2.png"
}
```


### [2026-09-06T15:16:51.102Z] TOOL RESULT

```

```


## [2026-09-06T15:16:55.641Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_harmathan.png"
}
```


### [2026-09-06T15:16:55.653Z] TOOL RESULT

```

```


## [2026-09-06T15:17:05.995Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AD%D8%B3%D9%86#Arabic",
 "prompt": "Arabic root ح س ن: verb hasuna, noun husn, adjective hasan, elative ahsan, ihsan, name Hasan / Husayn. What meanings and derivations are given?"
}
```


## [2026-09-06T15:17:07.940Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%97%D7%A8%D7%9D",
 "prompt": "Hebrew חרם (herem): meaning 'ban, devoted thing, excommunication', root ח־ר־ם, cognates with Arabic haram? What does the entry say?"
}
```


### [2026-09-06T15:17:12.843Z] TOOL RESULT

```
# Arabic Root ح س ن (Ḥ S N): Meanings and Derivations

## Verb Forms

**Form I (حَسُنَ - ḥasuna):**
"to be or become good, to better, to improve" and "to be or become pleasant or agreeable"

**Form II (حَسَّنَ - ḥassana):**
"to improve, to ameliorate, to better, to polish, to embellish" and "to beautify, to adorn"

## Noun (حُسْن - ḥusn)

The verbal noun encompasses "goodness," "prettiness," "beauty," "charm," "glory," and "finesse"

## Adjective (حَسَن - ḥasan)

Means "good, fine, well," "pretty, beautiful," "handsome," and in hadith terminology, "acceptable"

## Elative & Derived Forms

**Elative (أَحْسَن - ʔaḥsan):** Comparative/superlative form meaning "better/best"

**Name (حَسَن - Ḥasan):** A male given name referring to Hasan ibn Ali, grandson of Muhammad and second Shia Imam

The root demonstrates semantic progression from general improvement and goodness to specific aesthetic and moral qualities across Semitic languages.
```


### [2026-09-06T15:17:13.829Z] TOOL RESULT

```
# חרם (Herem) - Wiktionary Entry Summary

The entry defines **חרם** (khérem) as a Hebrew masculine noun with these primary meanings:

> "excommunication (act of excommunicating or ejecting), anathema, taboo, dedication, consecration"

**Linguistic Details:**
- **Root:** ח־ר־ם (kh-r-m)
- **Cognate:** The entry notes it should be compared with Arabic ح ر م (ḥ r m)
- **Pronunciation:** /ˈχeʁem/ in Modern Israeli Hebrew

**Biblical Context:**
The entry includes Joshua 6:17 from the Tanach, illustrating the term's usage regarding Jericho—the city is described as "devoted to the LORD for destruction," with specific prohibitions against taking devoted items.

**Yiddish Connection:**
The term descended into Yiddish as **חרם** (kheyrem), where it retains the meaning of "excommunication, expulsion from the Jewish community."

The Hebrew-Arabic connection you noted is indeed acknowledged in the entry's etymology section.
```


## [2026-09-06T15:17:20.573Z] TOOL CALL #44: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/harem\" \"https://en.wiktionary.org/wiki/harmattan\" \"https://en.wiktionary.org/wiki/marrano\" \"https://en.wiktionary.org/wiki/maranatha\" \"https://en.wiktionary.org/wiki/%D8%AD%D8%B1%D9%85\" \"https://en.wiktionary.org/wiki/%D8%AD%D8%B3%D9%86\" \"https://en.wiktionary.org/wiki/%D7%97%D7%A8%D7%9D\"; do python3 tools/fetch_source.py \"$u\" --note \"page 222, roots H.r.m / H.s.n: checking harem/harmattan/marrano/maranatha/herem and Arabic roots h-r-m, h-s-n\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:17:25.372Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/71ecacbc9a2122b1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec442a41ad0dfafa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bf04c02bb8b3370c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/253449a0b12fd60b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77e5b3a0d7f95a3e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/61ba4be21a270d30.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b16828a8b6e9b58a.txt
```


## [2026-09-06T15:17:29.573Z] TOOL CALL #45: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg222.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/222.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/222.png\necho \"=== verify_check help\"\nsed -n '1,60p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:17:29.663Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 84108 Sep  6 11:17 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/222.png
=== verify_check help
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


## [2026-09-06T15:17:32.152Z] TOOL CALL #46: Bash

```json
{
 "command": "sed -n '60,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:17:32.206Z] TOOL RESULT

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


## [2026-09-06T15:18:26.848Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== AID hobson\"; grep -n -i \"hobson\" AID.txt | head -3\necho \"== WEB_vol1 hobson\"; grep -n -i \"hobson.jobson\\|hobson-jobson\" WEB_vol1.txt | head -3\necho \"== RCH harim/haram\"; grep -n \"haram,\" RCH.txt | head -4\npython3 - <<'EOF'\nfor f,ln in [('AID.txt',2758),('RCH.txt',33688),('WEB_vol1.txt',112720)]:\n    txt=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    cum=0\n    for i,l in enumerate(txt):\n        if i==ln-1: print(f,'line',ln,'leaf',cum); break\n        cum+=l.count('\\f')\nEOF"
}
```


### [2026-09-06T15:18:29.980Z] TOOL RESULT

```
== AID hobson
== WEB_vol1 hobson
== RCH harim/haram
526:lady  had  perplexed  the  faculty.  Avicenna  supposed  it  to  be  |   mas suk  nor  khat  are  of  Persian  or  Nagree  original,  being concealed  love;  and,  in  the  idea  that  the  fair  object  might  be  •   both  adopted  from  the  Arabic.  [N.  B.  in  the  printed  trial  f//j- one  of  the  ladies  of  llie  king’s  haram,  he  desired  the  chamber-  !   masouk  is  the  word  used,  which  is  an  error.]  It  may  also  be lain  to  de.scribe  the  curiosities  of  (he  palace,  whilst  he  felt  the  i   observed,  that  many  of  the  witnesses  who  are  examined  in  the prince’s  pulse.  On  the  mention  of  a   particular  apartment,  he  |   IMoors,  in  the  Nagree,  and  in  the  Bengal  dialects,  use  a   variety perceived  an  uncommon  emotion  in  hi.s  patient ;   but  tbe  naming  ^   of  Arabic  words;  sikkah  dazeat,  a   silver  ink-standish  ;
33252:hired,  (III  of  Being  scarce  of  milk  (a  camel),  harim.  jlb  bUadu  U   haram,  ddecca.  ^1
33256:of  rain  (a  season),  (pi.  of  A)j>.  harid),  Living  far  from  firiends.  os'  shahru  'I  haram,  The  sacred  month  Muharram.
33264:matjidu'l  haram,  The  temple  of  Mecca.  aUI  haramu 'Hah,  So  help  me  God !   p   (*!/^  haram  kardan.  To  make unlawful,  to  interdict  TjS  prohibit  or  prevent  from  sleeping.
AID.txt line 2758 leaf 135
RCH.txt line 33688 leaf 659
WEB_vol1.txt line 112720 leaf 1147
```


## [2026-09-06T15:24:00.360Z] TOOL CALL #48: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk222.py",
 "content": "# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n  \"pdf_page\": 222,\n  \"book_page\": 192,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"H.r.m\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic *ḥ-r-m 'to separate, set apart, declare forbidden/sacred'\",\n      \"note\": \"The consonantal root ḥ-r-m is genuinely common Semitic, not Arabic-only: Akkadian ḫarāmu 'to separate, dedicate' / ḫarimtu 'hierodule', Hebrew ḥērem 'ban, thing devoted to destruction' with the causative heḥĕrīm, Aramaic aḥrēm 'he banned, excommunicated', Ge'ez (Ethiopic) ḥarama 'he prohibited from common use, devoted to God', Arabic ḥarama / ḥaruma 'to forbid, be forbidden'. Nourai's language label 'Semitic' and gloss 'to forbid' are correct, though the root's semantic core is 'set apart' — whence both 'forbidden' (Arabic ḥarām) and 'sacred' (ḥaram al-šarīf, Hebrew ḥērem 'devoted to YHWH'). The two branches Nourai draws (Arabic, Hebrew) are the two best-attested ones. The only quarrel with the chart is inside individual nodes (see #4, #7, #9), not with the root.\",\n      \"note_fa\": \"ریشهٔ سه‌حرفی ح‌ر‌م ریشه‌ای سامی مشترک است، نه تنها عربی: در اکدی ḫarāmu «جدا کردن، وقف کردن»، در عبری ḥērem «تحریم، چیزِ وقف‌شده برای نابودی»، در آرامی aḥrēm «تکفیر کرد»، در حبشی (گعز) ḥarama «از استفادهٔ همگانی بازداشت»، و در عربی حَرَمَ/حَرُمَ. معنای بنیادی ریشه «جدا کردن و کنار نهادن» است که از یک سو به «حرام» و از سوی دیگر به «حَرَم/مقدّس» انجامیده است. برچسب زبانیِ «سامی» و معنای «منع کردن» که نورایی آورده درست است؛ اختلاف‌ها در گره‌های جزئی است، نه در خودِ ریشه.\",\n      \"sources\": [\n        W + \"%D8%AD%D8%B1%D9%85\",\n        W + \"%D7%97%D7%A8%D7%9D\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"FVA:98\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989): no digital copy exists on archive.org, noorlib, ketabnak or elsewhere (refs_online.json: 'RE-SEARCH 2026-09: still no digital copy on any permitted platform'). Not checkable.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 17630, s.v. 'herem' (1966 2-vol. p. ~754 = the p.723 of Nourai's 1-vol. printing)\", \"stance\": \"supports\", \"note\": \"'herem, n., Biblical ban, excommunication. — Heb. herem ... rel. to heherim ..., Aram. aharim, 'he banned; excommunicated', Arab. harama, 'he forebade', haruma, 'was forbidden', harim, 'sacred, forbidden', Ethiop. harama ..., Akkad. haramu, 'to dedicate', harimtu, 'a dedicated woman' — i.e. exactly the pan-Semitic root Nourai posits.\"},\n        {\"src\": \"LKT\", \"where\": \"no. 819 (LKT.txt line 1981), 'Ar. ḥarām'\", \"stance\": \"partial\", \"note\": \"Lokotsch gives only the Arabic branch: \\\"'Verboten'; dasjenige, wozu der Zutritt verboten ist, also der 'Frauenraum' und schließlich 'die Frauen' selbst\\\" — supports the Arabic side of the root but says nothing about Hebrew/Akkadian.\"},\n        {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt, grep 'حرام'\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' treats only Persian words; the hits (حرامزاده etc.) are compounds, no etymological footnote on the Arabic root itself.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"harâm; harîm; harem; ihrâm; Moharram\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five are regular derivatives of the Arabic Form-I verb ḥarama 'he forbade' / ḥaruma 'was forbidden, was inviolable'. ḥarām (فَعَال pattern) = 'forbidden, unlawful'; ḥarīm (فَعِيل, 'that which is made inviolable') = the inviolable precinct of a house, hence the women's apartments, whence also the by-form ḥaram 'sacred precinct' (al-Ḥaram al-Šarīf, al-Ḥaramayn = Mecca and Medina); iḥrām is the Form-IV maṣdar of aḥrama 'he made (something) forbidden to himself', used for the pilgrim's state of consecration and, by metonymy, for the two seamless white cloths worn in it; muḥarram is the Form-II passive participle of ḥarrama 'he declared forbidden', hence 'the forbidden (month)', the first month of the Muslim year, in which pre-Islamic Arabia already banned warfare. Nourai's entry 'harem' inside the Arabic box is the European form rather than an Arabic one (Arabic has ḥarīm/ḥaram); that is a presentational slip, not an etymological error.\",\n          \"derivation_fa\": \"هر پنج واژه مشتق‌های قاعده‌مند فعل عربی حَرَمَ/حَرُمَ «منع کرد، ناروا شد» هستند: «حرام» بر وزن فَعال یعنی ناروا؛ «حریم» بر وزن فَعیل یعنی جای مصون و ممنوع‌الورود و از همین‌جا «حَرَم» شریف و حرمین؛ «إحرام» مصدر باب افعال از أحرم «بر خود حرام کرد» که هم به حالت تقدّس حاجی و هم به جامهٔ دوندوختهٔ او گفته می‌شود؛ و «مُحَرَّم» اسم مفعول باب تفعیل از حرَّم، یعنی ماهی که در آن جنگ حرام است. تنها نکته آنکه صورت harem در جعبهٔ عربی در واقع صورت اروپایی واژه است، نه عربی (عربی حَریم/حَرَم دارد)؛ این لغزشی در نمایش است نه در ریشه‌شناسی. ادعای نورایی درست است.\",\n          \"sources\": [W + \"%D8%AD%D8%B1%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:703\", \"status\": \"supports\", \"note\": \"Klein s.v. 'harem' (KLN_1966.txt line 17209; 1966 2-vol. p. ~734, = p.703 of the 1971 one-volume printing Nourai cites): 'harem, n., women's section in an Oriental house. — Arab. ḥarīm, sacred, forbidden, fr. ḥarama, he forbade, ḥaruma, was forbidden ... Cp. also harmattan, ihram, Muharram.' Klein's ihram entry (line 18694) and Muharram entry (line 24598) give exactly Nourai's other three words.\"},\n            {\"ref\": \"FVA:98\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vazheha-ye Arabi dar Farsi has no digital copy (see refs_online.json).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 819, 'Ar. ḥarām'\", \"stance\": \"supports\", \"note\": \"\\\"'Verboten' ... also der 'Frauenraum' und schließlich 'die Frauen' selbst; ebenso tk. harem\\\" — the same ḥarām > 'women's quarters' development.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson, RCH.txt lines 33252-33264, s.v. ḥaram / ḥarīm\", \"stance\": \"supports\", \"note\": \"'shahru 'l ḥaram, The sacred month Muharram'; 'masjidu'l ḥaram, The temple of Mecca'; 'ḥaram kardan, To make unlawful, to interdict' — the Arabic family as Nourai lists it.\"},\n            {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary, AID.txt line 2758 s.v. Harem\", \"stance\": \"supports\", \"note\": \"'Harem. [Hindustani harim, from the Arabic haram, sacred, forbidden.] The portion of a house which is reserved for the women of a family.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"harâm «حَرام (محروم، تحریم، مَحرّم)»; harîm «حَریم (حَرَم)»; hermân «حرمان»; hormat «حُرمت (احترام ، محترم)»; ehrâm «إحرام»; Moharram «مُحَرَّم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All of these are post-conquest Arabic loans in New Persian (7th-9th c. CE onwards), taken over with the Arabic morphology intact and only lightly re-pronounced: Ar. ḥarām > NP harâm; ḥarīm > harîm; ḥirmān (the maṣdar of ḥarama 'to deprive') > NP hermân/hirmân, in Persian usage narrowed from 'deprivation' to 'disappointment, being left empty-handed' — exactly the sense in the Hâfez bayt Nourai quotes ('… raqīb maḥram o ḥermān naṣīb-e man bāšad'); ḥurma(t) 'inviolability, sanctity' > NP hormat, where Persian keeps the Arabic tāʾ marbūṭa as a spoken -t and the sense slides 'inviolability' > 'dignity, respect' (whence the Arabic-pattern Persian derivatives احترام ehterâm, محترم mohtaram); iḥrām > ehrâm; muḥarram > Moharram. The bracketed forms محروم maḥrūm (Form-I passive participle), تحریم taḥrīm (Form-II maṣdar) and محرّم muḥarram belong to the same root and are likewise borrowed whole. Persian did not derive them internally — it imported the Arabic derivational output.\",\n          \"derivation_fa\": \"همهٔ این واژه‌ها وام‌واژه‌های عربی در فارسی نو پس از اسلام‌اند (از سدهٔ نخست هجری به بعد) که با ساخت صرفی عربی و تنها با اندکی دگرگونی تلفظ وارد شده‌اند: «حرام» و «حریم» بی‌تغییر؛ «حِرمان» مصدر حَرَمَ به معنی «بی‌بهره ماندن» که در فارسی به «ناامیدی و محرومیت» تخصیص یافته — همان معنایی که در بیت حافظ («رقیب محرم و حرمان نصیب من باشد») دیده می‌شود؛ «حُرمت» از حُرمة عربی «مصونیت، قداست» که در فارسی به «احترام و بزرگی» گراییده و از آن احترام و محترم نیز به کار رفته است؛ «إحرام» مصدر باب افعال و «مُحَرَّم» اسم مفعول باب تفعیل. صورت‌های داخل کمانک (محروم، تحریم، محرّم) نیز از همین ریشه و همه به‌صورت آماده از عربی وام گرفته شده‌اند، نه ساختهٔ فارسی. معین در فرهنگ خود همهٔ اینها را با نشان [ع.] یعنی عربی می‌آورد؛ ادعای نورایی درست است.\",\n          \"sources\": [W + \"%D8%AD%D8%B1%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:98\", \"status\": \"not_checked\", \"note\": \"No digital copy of Nahvi 1368 (see refs_online.json); the claim itself (Arabic ḥ-r-m words as Persian loans) is however confirmed by Mo'in below.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 53063 (حرمان), line 7907-7908 (احرام), and the احترام entry at line 7721\", \"stance\": \"supports\", \"note\": \"Mo'in tags each with [ع.] = Arabic: 'حرمان: [ع.] (مص ل) بی‌بهره بودن، بی‌روزی ماندن. (امص.) بی‌بهرگی، بی‌نصیبی، نومیدی' — the very 'prohibition > disappointment' sense Nourai gives; 'احرام: [ع.] (مص ل) … حج'; 'احترام: [ع.] … حرمت داشتن، بزرگ داشتن'.\"},\n            {\"src\": \"RCH\", \"where\": \"RCH.txt lines 33252-33264 (ḥaram, ḥarīm, ḥaram kardan)\", \"stance\": \"supports\", \"note\": \"Richardson's Persian-Arabic dictionary lists the whole family as current Persian, e.g. 'P ḥaram kardan, To make unlawful, to interdict'.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt, grep 'حرام'\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' (a dictionary of Persian words) has no entry for the Arabic loans themselves; only compounds such as حرامزاده appear, without Mo'in etymological footnotes on the root.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"harem; ihram; Moharram\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"ihram (first in English travel writing on the Hajj) and Moharram/Muharram are indeed straight borrowings of Arabic iḥrām and muḥarram, as Klein states. harem, however, did not come into English directly from Arabic: it is first attested in the 1630s in accounts of the Ottoman court and comes through Ottoman Turkish harem (itself from Arabic ḥarīm/ḥaram), which is why English has -e- rather than the -ī- of ḥarīm; Lokotsch likewise routes rum./sp./frz./engl. harem through Turkish, and Whitworth notes an Indian route through Hindustani harīm for the Anglo-Indian usage. Nourai's Arabic→English arrow is therefore right in substance but skips the Turkish (and, in India, Hindustani) transmitters.\",\n          \"derivation_fa\": \"«احرام» و «محرّم» در انگلیسی مستقیماً از عربی گرفته شده‌اند (نخست در سفرنامه‌های حج)، اما harem از راه ترکی عثمانی harem به انگلیسی رسیده است و نخستین کاربرد آن در دههٔ ۱۶۳۰ در گزارش‌های دربار عثمانی است؛ همین گذر از ترکی است که مصوّت e را به جای ī عربیِ «حَریم» توضیح می‌دهد. لوکوچ نیز صورت‌های اروپایی را از ترکی می‌گیرد و ویتورث برای کاربرد انگلیسی‌ـ‌هندی، واسطهٔ هندوستانی harīm را می‌آورد. بنابراین پیکان «عربی ← انگلیسی» نورایی در اصل درست است ولی حلقهٔ واسطهٔ ترکی را نادیده گرفته؛ با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/harem\", W + \"%D8%AD%D8%B1%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:703\", \"status\": \"supports\", \"note\": \"Klein s.v. harem (KLN_1966.txt line 17209) derives English harem straight from 'Arab. ḥarīm', and s.v. ihram (line 18694) 'Arab. iḥrām, prohibition, interdiction, prop. inf. of aḥrama' and s.v. Muharram (line 24598) 'Arab. muḥarram, lit. sacred, forbidden' — i.e. Klein backs Nourai's direct arrow (Klein, unlike OED/Etymonline, omits the Turkish stage).\"},\n            {\"ref\": \"TYL:568\", \"status\": \"not_checked\", \"note\": \"W. Taylor, Arabic Words in English (S.P.E. Tract XXXVIII, 1933): not on archive.org or Google Books; HathiTrust full view is US-browser-only and the host is IP-blocked here (refs_online.json TYL note). Only a different Taylor article is on disk.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 819\", \"stance\": \"partial\", \"note\": \"\\\"ebenso tk. harem; hieraus rum. harem, sp. Haren, pg. frz. engl. harem, ndl. dtsch. Harem\\\" — Lokotsch has the European words come from Turkish, not straight from Arabic.\"},\n            {\"src\": \"AID\", \"where\": \"AID.txt line 2758 s.v. Harem\", \"stance\": \"partial\", \"note\": \"'[Hindustani harim, from the Arabic haram]' — a third route (via India) for the Anglo-Indian use.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/harem\", \"stance\": \"partial\", \"note\": \"'entered English through Turkish harem in the 1630s' — direct Arabic > English is not the modern account.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Spanish\",\n          \"words\": \"harmathan\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"Two problems. (a) Form: no Spanish word 'harmathan' exists — Spanish has harmatán (Klein prints 'Sp. harmatan'), and Spanish orthography does not use -th-. The printed page of Nourai (pdf p. 222) itself reads 'harmathan', so the extraction is faithful and the misprint is the author's, probably an eye-slip from the English spelling harmattan. (b) Route: even Klein, whom Nourai cites, does NOT derive the Spanish word directly from Arabic — 'Sp. harmatan, fr. Fanti haramata, fr. Arab. ḥarām, a forbidden thing, used in the sense of an evil thing'. The wind-name reached European languages from the Akan (Twi/Fante) coast of West Africa in the 17th c.; whether the Akan word is ultimately the Arabic ḥarām borrowed across the Sahel is only a conjecture (Wiktionary: 'the ultimate origin is supposed by some to be an Arabic word, but which one is uncertain'). So the arrow Arabic→Spanish, with the Fante link deleted, is at best partial.\",\n          \"derivation_fa\": \"دو اشکال در این گره هست. نخست صورت واژه: در اسپانیایی harmatán است نه harmathan؛ اصلاً خوشهٔ th در املای اسپانیایی راه ندارد و کلاین هم harmatan نوشته است. تصویر صفحهٔ چاپی کتاب (صفحهٔ ۲۲۲ پی‌دی‌اف) نشان می‌دهد که خودِ کتاب harmathan چاپ کرده است؛ پس خطای خوانش اسکن نیست، خطای چاپیِ نویسنده است. دوم مسیر وام‌گیری: حتی کلاین که مأخذ نورایی است این واژه را مستقیم از عربی نمی‌گیرد، بلکه «اسپانیایی harmatan از فانتی haramata از عربی حرام» می‌آورد؛ یعنی حلقهٔ زبان آکان (توی/فانته) در غرب آفریقا حذف شده است و خاستگاه عربیِ نهایی هم تنها یک حدس است. بنابراین پیکان «عربی ← اسپانیایی» ناقص است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"harmathan\",\n          \"correct_form\": \"harmatán (Klein: 'Sp. harmatan')\",\n          \"sources\": [W + \"harmattan\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:704\", \"status\": \"partial\", \"note\": \"Klein s.v. harmattan (KLN_1966.txt line 17225): 'a dry wind, charged with dust, blowing from the Sahara to the Atlantic coast. — Sp. harmatan, fr. Fanti haramata, fr. Arab. ḥarām, a forbidden thing, used in the sense of an evil thing, from the stem of ḥarama'. Klein has the word and the ultimate Arabic etymon but (i) spells the Spanish harmatan and (ii) inserts Fanti between Arabic and Spanish.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"grep 'harmat' in LKT.txt — no hit\", \"stance\": \"silent\", \"note\": \"Lokotsch's dictionary of European words of Oriental origin has no harmattan entry at all, although it covers ḥarām (no. 819) — i.e. he did not accept it as an Arabism.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/harmattan\", \"stance\": \"partial\", \"note\": \"'From Twi (Akan) haramata … which also gave Spanish harmatán. The ultimate origin is supposed by some to be an Arabic word, but which one is uncertain' — Arabic origin is a hypothesis, and the Spanish form is harmatán.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"harmattan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English harmattan 'the dry dusty NE wind that blows off the Sahara over the Guinea coast between November and March' is first recorded in the 1670s-1690s in accounts of the Gold Coast. Klein (the source Nourai cites) does route it through Spanish (harmatan < Fante haramata), and that is what the chart's Spanish→English arrow says, so the arrow is defensible; but the modern account (OED, Wiktionary) makes English take the word directly from Twi/Fante haramata through the coastal trade, with Spanish as a parallel borrowing rather than the transmitter. The word's shape (double -tt-, final stress) is the same either way.\",\n          \"derivation_fa\": \"harmattan در انگلیسی نام بادِ خشک و غبارآلودی است که از اواخر پاییز تا اسفند از صحرا بر ساحل گینه می‌وزد و نخستین کاربردهای آن به دههٔ ۱۶۷۰–۱۶۹۰ در گزارش‌های ساحل طلا بازمی‌گردد. کلاین — که مأخذ نورایی است — آن را از اسپانیایی harmatan می‌گیرد و از این‌رو پیکان «اسپانیایی ← انگلیسی» چارت دفاع‌پذیر است؛ اما دیدگاه امروزی (آکسفورد و ویکی‌واژه) انگلیسی را مستقیم وام‌گیرندهٔ واژهٔ توی/فانتهٔ haramata از راه بازرگانی ساحلی می‌داند و اسپانیایی را وام‌گیرندهٔ موازی، نه واسطه. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [W + \"harmattan\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:704\", \"status\": \"supports\", \"note\": \"Klein s.v. harmattan (line 17225) does make English harmattan continue 'Sp. harmatan' — the chart's Spanish→English arrow is exactly Klein's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/harmattan\", \"stance\": \"partial\", \"note\": \"'From Twi (Akan) haramata …, which also gave Spanish harmatán' — Spanish as a sister borrowing, not the transmitter.\"},\n            {\"src\": \"LKT\", \"where\": \"grep 'harmat' — no hit\", \"stance\": \"silent\", \"note\": \"no entry; Lokotsch does not list harmattan among European Orientalisms.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (A-M volume), grep 'harmattan'\", \"stance\": \"silent\", \"note\": \"no usable hit in the OCR of Webster's vol. 1.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Spanish\",\n          \"words\": \"marrano\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Spanish marrano 'pig, pork' is generally taken from Arabic — but from the participle, not the bare verb: Andalusi Arabic muḥarram(a) 'forbidden (thing)', Form-II passive participle of ḥarrama, whence Andalusian Spanish maharrana 'fresh bacon, salt pork' and, with loss of the unstressed first syllable, marrano/marrana 'pig'. Klein derives it more loosely 'fr. Arab. ḥaruma, was forbidden', explaining that 'the pig was called the forbidden animal, from the fact that the eating of pork is forbidden by Jewish and Moslem religious law' — the same idea. Lokotsch (no. 1499) sets it out in full: 'Ar. muḥarrama, Verbotenes … hieraus sp. (dial. Andalusien) muharrana … sp. marrano Schweinefleisch'. The semantic path 'forbidden' > 'the forbidden meat' > 'pig' is thus well supported; Corominas' alternative (an onomatopoeic/Romance origin) is a minority view.\",\n          \"derivation_fa\": \"واژهٔ اسپانیایی marrano «خوک، گوشت خوک» را عموماً از عربی می‌دانند، اما از اسم مفعول باب تفعیل نه از فعل مجرد: عربیِ اندلسی مُحَرَّمة «چیز حرام» که نخست به صورت maharrana «گوشت خوکِ تازه/نمک‌سود» در گویش اندلس و سپس با افتادن هجای نخست به marrano بدل شده است. کلاین آن را ساده‌تر از حَرُمَ می‌گیرد و توضیح می‌دهد که خوک را «جانور حرام» می‌نامیدند، و لوکوچ (شمارهٔ ۱۴۹۹) همین زنجیره را با صورت‌های میانی می‌آورد. پس تحول معنایی «حرام ← گوشت حرام ← خوک» مستند است و ادعای نورایی درست.\",\n          \"sources\": [W + \"marrano\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:941\", \"status\": \"supports\", \"note\": \"Klein s.v. marrano (KLN_1966.txt line 22983): 'Sp., pig, hog, fr. Arab. ḥaruma, was forbidden. The pig was called the forbidden animal … Cp. (Andalusian) Sp. maharrana, fresh bacon, salt pork, which derives fr. Arab. muḥarramah, fem. of muḥarram, anything forbidden, pass. part. of ḥarrama.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1499 (LKT.txt line 3454), 'Ar. muḥarrama'\", \"stance\": \"supports\", \"note\": \"\\\"'Verbotenes' [part. pass. II fem. des Vbs. harama, s. hier Nr. 819]; hieraus sp. (dial. Andalusien) muharrana 'frische Speckseite', sp. marrano 'Schweinefleisch' … pg. marrão\\\" — with the cross-reference to the same root no. 819.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/marrano (Spanish section)\", \"stance\": \"supports\", \"note\": \"'Borrowed from Arabic مُحَرَّم (muḥarram, forbidden) as referring to pigs'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"marrano\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English marrano (in English since the 16th-17th c., in modern use since Jewish historiography of the 19th c.) 'a Spanish or Portuguese Jew forcibly converted to Christianity, suspected of secretly keeping Judaism' is taken from the Spanish word of node #6, i.e. it is the abusive epithet 'pig' applied to the conversos — precisely because pork was the food they were made to eat to prove their conversion. Klein and Wiktionary both take this line and the chart follows them. It should be noted that this is not unanimous: Lokotsch (no. 1499) explicitly refuses it — 'Dagegen muß marrano (übergetretener Jude) anderen Ursprungs sein, s. hier Nr. 1412' — and at no. 1412 derives it from Hebrew mar'e 'appearance, Schein' + Romance ending, 'because the marranos were supposed to have converted only in appearance'; Corominas too calls the Spanish word's origin uncertain. Hence plausible rather than confirmed.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی marrano به معنی «یهودی اسپانیایی یا پرتغالیِ به‌زور مسیحی‌شده که پنهانی بر دین خود مانده بود» همان واژهٔ اسپانیایی گرهٔ پیشین (خوک) است که به‌عنوان دشنام بر «کُنوِرسو»ها نهاده شد، از آن‌رو که برای اثبات مسیحی‌شدنشان وادار به خوردن گوشت خوک می‌شدند؛ کلاین و ویکی‌واژه همین را می‌گویند و نورایی از آنان پیروی کرده است. اما این نظر اجماعی نیست: لوکوچ در شمارهٔ ۱۴۹۹ صریحاً آن را رد می‌کند و در شمارهٔ ۱۴۱۲ واژه را از عبری مَرْئه «ظاهر، نمود» می‌گیرد، چون گمان می‌رفت مارانوها تنها به‌ظاهر گرویده‌اند. پس این گره با احتیاط پذیرفتنی است.\",\n          \"sources\": [W + \"marrano\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:941\", \"status\": \"supports\", \"note\": \"Klein's headword is precisely 'marrano, n., Jew or Moor converted to Christianity. — Sp., pig, hog, fr. Arab. ḥaruma' — the sense and the derivation Nourai draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"nos. 1499 and 1412 (LKT.txt lines 3454, 3255)\", \"stance\": \"contradicts\", \"note\": \"no. 1499: 'Dagegen muß marrano \\\"übergetretener Jude\\\" anderen Ursprungs sein, s. hier Nr. 1412'; no. 1412: 'Hebr. marʾe: Schein; hieraus mit roman. Endung sp. marrano \\\"christlich gewordener Jude\\\": man nahm an, daß die Marranos nur zum Schein übergetreten seien'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/marrano\", \"stance\": \"supports\", \"note\": \"the converso sense is presented as a secondary, insulting application of the 'pig' word, itself < Arabic muḥarram.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Hebrew\",\n          \"words\": \"hěrem; mohoram-atta\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"ḥērem (חֵרֶם) is solid: a Biblical Hebrew noun 'that which is devoted/banned, thing under the ban', from the root ḥ-r-m, with the causative heḥĕrīm 'he devoted to destruction, banned' (Joshua 6:17 on Jericho; Lev. 27:28-29), later 'excommunication' in rabbinic and modern Hebrew (Yiddish kheyrem). It is the exact Hebrew counterpart of Arabic ḥarām, and this arrow from the common Semitic root is correct. mohŏram attā(h) is a different matter: it is not a quoted Biblical phrase but a form Klein reconstructs — mohŏram is the Hophʿal (passive-causative) participle of heḥĕrīm, so 'thou art put under the ban' is morphologically impeccable Hebrew, but the phrase itself is Klein's conjectural retro-version of Greek maranatha, not an attested Hebrew expression. Hence the node as a whole is only plausible.\",\n          \"derivation_fa\": \"«حِرِم/ḥērem» عبری واژه‌ای است استوار: اسمی از ریشهٔ ح‌ر‌م به معنی «چیزِ تحریم‌شده و وقف‌شده برای نابودی» با فعل سببی هِحِریم (یوشع ۶:۱۷ دربارهٔ اریحا؛ لاویان ۲۷:۲۸–۲۹) که بعدها در عبری خاخامی و نو معنی «تکفیر» یافت و در یدیش kheyrem شد؛ این واژه همتای دقیق «حرام» عربی است و پیکان آن از ریشهٔ سامی مشترک درست است. اما mohŏram attā عبارتی نقل‌شده از تورات نیست، بلکه صورتی است که کلاین بازسازی کرده: mohŏram اسم مفعول باب هُفعَل از هِحِریم است و از نظر صرفی بی‌عیب، ولی خودِ عبارت شاهد متنی ندارد و تنها فرضیهٔ کلاین برای توضیح maranatha یونانی است. از این‌رو این گره با احتیاط پذیرفتنی است.\",\n          \"sources\": [W + \"%D7%97%D7%A8%D7%9D\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:723\", \"status\": \"supports\", \"note\": \"Klein s.v. herem (KLN_1966.txt line 17630): 'Heb. ḥerem, person or thing devoted to destruction, rel. to heḥerim … Arab. ḥarama … Akkad. ḥaramu, to dedicate' — Nourai's Hebrew node verbatim.\"},\n            {\"ref\": \"KLN:937\", \"status\": \"supports\", \"note\": \"Klein s.v. maranatha (line 22878-22880): 'It is very probable that μαραναθα is the transliteration of Heb. mohoram attā, thou art put under the ban … The Hebrew word moḥoram is the Hophʿal (= passive of the causative) part. of ḥarām, he devoted, banished' — the source of Nourai's second word, and Klein flags it himself as a probability, not a fact.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/חרם\", \"stance\": \"supports\", \"note\": \"'excommunication …, anathema, taboo, dedication, consecration', root ח־ר־ם, 'compare Arabic ح ر م', with Joshua 6:17 quoted — the ḥērem half of the node.\"},\n            {\"src\": \"LKT\", \"where\": \"grep 'herem' in LKT.txt\", \"stance\": \"silent\", \"note\": \"Lokotsch covers only European loanwords; no Hebrew ḥerem entry.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"herem; maranatha\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"herem is fine: an English (Judaic-studies) borrowing of Hebrew ḥērem, 'the Biblical ban; rabbinic excommunication', used in English since the 17th c. maranatha is where the chart goes wrong. The word is Greek μαρανα θα in 1 Corinthians 16:22, universally read today as Aramaic — either מָרַנָא תָא māranā thā 'Our Lord, come!' or מָרַן אֲתָא māran ăthā 'Our Lord has come' — and it means an invocation, not a curse. The 'curse' gloss comes only from its position next to anathema in the same verse ('let him be anathema; maranatha'), which older English versions read as one formula. Klein's derivation from a Hebrew mohŏram attā 'thou art under the ban' (which Nourai reproduces) is an ingenious minority conjecture that modern lexicography and New Testament scholarship do not follow. So: the herem word is confirmed, the maranatha word is disputed, and per the rules the node takes the worse verdict.\",\n          \"derivation_fa\": \"واژهٔ herem در انگلیسی وام‌واژهٔ عبری ḥērem است («تحریم کتاب‌مقدسی، تکفیر») و درست است. اما maranatha نادرست نهاده شده: این واژه در رسالهٔ اول قرنتیان ۱۶:۲۲ به یونانی μαρανα θα آمده و امروزه همگان آن را آرامی می‌دانند: مارَنا تا «ای خداوند ما، بیا!» یا مارَن أتا «خداوند ما آمده است» — یعنی دعا و ندا، نه نفرین. معنای «نفرین» تنها از همنشینی آن با anathema در همان آیه پدید آمده است. اشتقاق کلاین از عبریِ فرضی mohŏram attā «تو تحریم شده‌ای» که نورایی نقل کرده، حدسی هوشمندانه اما اقلیّتی است و پژوهش امروزی آن را نمی‌پذیرد. پس این گره از نظر واژهٔ maranatha رد می‌شود.\",\n          \"sources\": [W + \"maranatha\", W + \"%D7%97%D7%A8%D7%9D\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:723\", \"status\": \"supports\", \"note\": \"Klein's 'herem, n., Biblical ban, excommunication' (line 17630) is Nourai's first word and gloss exactly.\"},\n            {\"ref\": \"KLN:937\", \"status\": \"supports\", \"note\": \"Klein s.v. maranatha does argue the Hebrew mohoram attā origin, so Nourai reports his source faithfully; but Klein himself opens 'Gk. μαραναθα, usually explained as transliteration of Aram. maran atha, the Lord has come, or O Lord, come' before offering his own alternative.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/maranatha\", \"stance\": \"contradicts\", \"note\": \"'From Aramaic מרנא תא (Lord, come!) or מרן אתא (our lord has come)', via Greek and Latin; no Hebrew-ban etymology and no 'curse' sense.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, WEB_vol1.txt line 112720 s.v. Maran atha\", \"stance\": \"contradicts\", \"note\": \"OCR: 'Maran atha … maranatha, from Ara[maic] … the Lord cometh … an invo[cation]' — Webster too glosses it as an invocation from Aramaic.\"},\n            {\"src\": \"SKT\", \"where\": \"grep 'maranatha' in SKT.txt\", \"stance\": \"silent\", \"note\": \"no entry in Skeat.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"H.s.n\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root ح س ن (ḥ-s-n) 'to be good, beautiful, fine'\",\n      \"note\": \"The root is real and the language label right. The gloss is slightly skewed: the base verb ḥasuna means 'to be/become good, beautiful, agreeable' (whence ḥusn 'beauty, goodness', ḥasan 'good, handsome'); 'to do good things, to be kind' is the sense of the Form-IV verb aḥsana, from which iḥsān 'beneficence' — one of the bracketed Persian derivatives on this page. So Nourai has glossed the root by its derived-stem meaning. Everything hanging from the root on this page is Arabic morphology plus one Anglo-Indian curiosity.\",\n      \"note_fa\": \"ریشهٔ ح‌س‌ن واقعی است و برچسب «عربی» درست. تنها معنایی که نورایی برای ریشه آورده اندکی جابه‌جاست: فعل مجرد حَسُنَ یعنی «نیکو و زیبا شد» (از آن حُسن «زیبایی، نیکویی» و حَسَن «نیکو»)، حال آنکه «نیکی کردن و مهربانی» معنای باب افعال، أحسَنَ، است که «احسان» از آن ساخته شده — و احسان خود یکی از مشتق‌های فارسیِ همین صفحه است. پس نورایی ریشه را با معنای بابِ مزیدفیه معنا کرده است. باقیِ چارت درست است.\",\n      \"sources\": [W + \"%D8%AD%D8%B3%D9%86\"],\n      \"ref_check\": [\n        {\"ref\": \"FVA:101\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vazheha-ye Arabi dar Farsi: no digital copy available (refs_online.json).\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/حسن (Arabic)\", \"stance\": \"partial\", \"note\": \"'حَسُنَ (ḥasuna): to be or become good, to better, to improve; to be or become pleasant or agreeable'; noun حُسْن 'goodness, prettiness, beauty, charm'; adj. حَسَن 'good, fine, pretty, handsome' — i.e. 'good/beautiful', with 'do good' belonging to أحسن.\"},\n        {\"src\": \"RCH\", \"where\": \"Richardson, RCH.txt line 33688\", \"stance\": \"supports\", \"note\": \"'Husn, Beauty. Goodness, elegance. husn-i ikhtiyar …, husn-i adab, Good manners' — the root's core sense as current in Persian-Arabic usage.\"},\n        {\"src\": \"MON\", \"where\": \"MON_part1.txt line 53324\", \"stance\": \"supports\", \"note\": \"'حسن: [ع.] (امص.) زیبایی، جمال' — Mo'in glosses ḥusn as 'beauty, comeliness' and marks it Arabic.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"hosn; Hasan, Hosayn; Yâ-Hasan! Yâ-Hosayn!\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"ḥusn is the verbal noun of ḥasuna 'to be good/beautiful'; ḥasan is the corresponding adjective 'good, handsome', used as a personal name — Ḥasan b. ʿAlī (d. 50/670), the Prophet's elder grandson; Ḥusayn is its diminutive (ḥusayn 'little Ḥasan', فُعَيْل pattern), the name of the younger grandson killed at Karbalāʾ on 10 Muḥarram 61/10 October 680. The ritual lament 'Yā Ḥasan! Yā Ḥusayn!' cried by mourners beating their breasts in the Muḥarram (ʿĀshūrāʾ) processions is thus literally 'O Ḥasan! O Ḥusayn!' — an Arabic vocative phrase, not a lexeme, and it is the phrase Yule & Burnell and Klein both quote. Nourai's account of all three is accurate; only 'martyred in Karbalâ battle' is loose for Ḥasan, who was poisoned in Medina.\",\n          \"derivation_fa\": \"«حُسن» مصدر فعل حَسُنَ است؛ «حَسَن» صفت همان فعل به معنی «نیکو، زیبا» که نام حسن بن علی (درگذشتهٔ ۵۰ ق) شده، و «حُسَین» مصغّر آن بر وزن فُعَیْل یعنی «حسنِ کوچک»، نام نوادهٔ کهتر پیامبر که در دهم محرّم سال ۶۱ ق در کربلا کشته شد. ندای «یا حسن! یا حسین!» که عزاداران در دسته‌های محرّم بر سینه‌زنان سر می‌دهند، عبارتی است عربی (منادا) نه یک واژه، و همان است که یول و برنل و کلاین نقل کرده‌اند. گزارش نورایی درست است؛ تنها این نکته که امام حسن در کربلا شهید نشد بلکه در مدینه مسموم شد.\",\n          \"sources\": [W + \"%D8%AD%D8%B3%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:101\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi 1368.\"},\n            {\"ref\": \"HJB:419\", \"status\": \"supports\", \"note\": \"Hobson-Jobson p. 419 (HJB.txt leaf 470, the running head '419' stands on the same leaf, line 11172): the phrase 'is in fact an Anglo-Saxon version of the wailings of the Mahommedans as they beat their breasts in the procession of the Moharram — \\\"Yā Hasan! Yā Hosain!\\\"' — Nourai's third word verbatim, including his spelling Hosayn/Hosain.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 17906 s.v. hobson-jobson\", \"stance\": \"supports\", \"note\": \"'Corruption of Arab. yā Ḥasan! yā Ḥusayn! O Hasan! O Husain!, cry of the Mohammedans at the procession of the Moharram.'\"},\n            {\"src\": \"RCH\", \"where\": \"RCH.txt line 33688\", \"stance\": \"supports\", \"note\": \"'Husn, Beauty. Goodness, elegance' — the first word of the node in the same sense.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/حسن (Arabic)\", \"stance\": \"supports\", \"note\": \"'حَسَن (Ḥasan): a male given name … referring to Hasan ibn Ali, grandson of Muhammad'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"hosn «حُسن»; Hasan «حَسَن (حسین، محسن، احسان)»; ahsan «احسن (تحسین)»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Again whole-cloth Arabic loans in New Persian from the Islamic period on. حُسن hosn keeps the Arabic maṣdar with its meaning 'beauty, goodness', and Persian adds the idiomatic extension 'advantage' in phrases such as حسن نیت, حسن انجام کار. حَسَن Hasan, حسین Hosayn, محسن Mohsen (Form-IV active participle muḥsin 'benefactor') and احسان Ehsân (Form-IV maṣdar iḥsān 'beneficence') are all borrowed as personal names or abstracts. احسن ahsan is the Arabic elative (أَفْعَل pattern) 'better, best', used in Persian in the frozen phrase به نحو احسن 'in the best way' — Nourai's gloss '(word of) admiration' fits the exclamatory use rather than the grammar; تحسین taḥsīn is the Form-II maṣdar 'praise, applause'. Mo'in marks every one of these [ع.] = Arabic.\",\n          \"derivation_fa\": \"این‌ها نیز وام‌واژه‌های عربی در فارسی نوی دورهٔ اسلامی‌اند: «حُسن» با همان معنای مصدری «زیبایی و نیکویی» که در فارسی افزون بر آن معنای «مزیّت» هم گرفته است (حسن نیت، حسن انجام کار). «حسن، حسین، محسن (اسم فاعل باب افعال: نیکوکار) و احسان (مصدر همان باب)» همه به‌صورت نام یا اسم معنا وام گرفته شده‌اند. «احسن» اسم تفضیل عربی بر وزن أفعَل یعنی «نیکوتر/نیکوترین» است که در فارسی بیشتر در ترکیب «به نحو احسن» به کار می‌رود؛ معنای «کلمهٔ تحسین» که نورایی آورده به کاربرد ندایی آن نظر دارد نه به صرف واژه. «تحسین» نیز مصدر باب تفعیل است. معین همهٔ اینها را با نشان [ع.] آورده است؛ ادعای نورایی درست است.\",\n          \"sources\": [W + \"%D8%AD%D8%B3%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:101\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi 1368; the substance is confirmed from Mo'in below.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 53324 (حسن) and line 7982 (احسن)\", \"stance\": \"supports\", \"note\": \"'حسن: [ع.] (امص.) زیبایی، جمال'; 'احسن: [ع.] (رص.) نیکوتر، بهتر، اعلی … به نحو احسن: به بهترین …' — Arabic tag and elative grammar, matching the analysis above.\"},\n            {\"src\": \"RCH\", \"where\": \"RCH.txt line 33688-33689\", \"stance\": \"supports\", \"note\": \"'Husn, Beauty. Goodness, elegance. husn-i ikhtiyar (or iradat), Free-will. husn-i adab, Good manners' — the loan fully naturalised in Persian phraseology.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt (ح section)\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' does not lemmatise Arabic loans such as حسن/احسن, so no footnote by Mo'in there.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Hindustani\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"An empty pass-through box standing for the Indian stage of the transmission. What it represents is real: the Muḥarram/taʿziya mourning processions were (and are) held all over Muslim India — Yule notes that in India they are 'by no means confined to Shiʿas' — and the Arabic cry Yā Ḥasan! Yā Ḥusayn! was heard in Hindustani-speaking surroundings by British soldiers, who reshaped it. Strictly, though, nothing was borrowed INTO Hindustani as a word: the phrase stayed Arabic (as a liturgical cry) and it is the Anglo-Indian soldiers' ear, not the Hindustani lexicon, that produced 'Hobson-Jobson'. Hence plausible rather than confirmed: the box marks a place and a milieu rather than a linguistic form.\",\n          \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ مرحلهٔ هندی انتقال است. آنچه نشان می‌دهد واقعی است: دسته‌های عزاداری محرّم و تعزیه در سراسر هند مسلمان برپا می‌شد — یول تصریح می‌کند که در هند این آیین‌ها «به‌هیچ‌روی ویژهٔ شیعیان نبود» — و سربازان بریتانیایی ندای عربیِ «یا حسن یا حسین» را در محیط اردوزبان/هندوستانی شنیدند و آن را دگرگون کردند. اما به‌دقت سخن بگوییم، واژه‌ای وارد هندوستانی نشد: عبارت همچنان عربی و آیینی ماند و آنچه Hobson-Jobson را ساخت گوشِ انگلیسیِ سرباز بود نه واژگان هندوستانی. پس این گره جای و فضا را نشان می‌دهد نه یک صورت زبانی، و با احتیاط پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"HJB:419\", \"status\": \"partial\", \"note\": \"Hobson-Jobson p. 419 (HJB.txt line 11172) supports the Indian setting — 'It is peculiar to the British soldier and his surroundings, with whom it probably originated … Major John Trotter tells me that he has repeatedly heard it used by British soldiers in the Punjab' — but Yule labels the phrase Anglo-Indian argot, not a Hindustani word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"HJB.txt lines 11172-11175, p. 419-420\", \"stance\": \"partial\", \"note\": \"Yule quotes Mīr Shahāmat ʿAlī on the Muharram in India and the ta'ziya, showing the milieu, but gives no Hindustani lexeme.\"},\n            {\"src\": \"AID\", \"where\": \"grep 'hobson' in AID.txt — no hit\", \"stance\": \"silent\", \"note\": \"Whitworth's Anglo-Indian Dictionary has no such entry.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"Hobson-jobson\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English 'hobson-jobson' (attested from the early 19th c. in British-Indian army slang, e.g. 'Hosseen Gosseen, Hossy Gossy, Hossein Jossen' in earlier garbled spellings) is a rhyming-reduplication distortion of the Muḥarram cry Yā Ḥasan! Yā Ḥusayn!, assimilated to the ordinary English surname Hobson (and to the pattern of Hobson's choice). It came to mean 'a native festal excitement, a tamāshā, especially the Muharram ceremonies', and Yule & Burnell borrowed it in 1886 as the title of their glossary, whence its modern technical use for any such phonetic naturalisation of a foreign word. All three of Nourai's references say this; his gloss 'referring to a crowd excitement' is Yule's 'a native festal excitement'.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی hobson-jobson که از اوایل سدهٔ نوزدهم در زبان سربازان بریتانیایی در هند دیده می‌شود (با صورت‌های پیشین‌تر و مغشوش‌تری چون Hosseen Gosseen و Hossy Gossy)، دگرگون‌شدهٔ ندای محرّمِ «یا حسن! یا حسین!» است که با قافیه‌سازی و همگونی با نام خانوادگی رایج انگلیسی Hobson (و ترکیب Hobson's choice) به این شکل درآمده است. معنای آن «شور و غوغای جشن بومی، به‌ویژه آیین‌های محرّم» شد و یول و برنل در ۱۸۸۶ آن را عنوان واژه‌نامهٔ خود کردند؛ از همین‌رو امروزه به هر گونه بومی‌سازیِ آواییِ واژهٔ بیگانه «هابسن‌ـ‌جابسن» می‌گویند. هر سه مأخذی که نورایی آورده همین را می‌گویند؛ ادعای او درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD:626\", \"status\": \"not_checked\", \"note\": \"Nourai's AHD page numbers below 1500 are main-dictionary pages of the 1975/76 New College Edition, which is not open online (refs_online.json: 'no open scan of the New College Edition'); the local AHD file is only Watkins' Indo-European roots (grep 'hobson' → no hit, as expected, this being no IE root).\"},\n            {\"ref\": \"FSD:1166\", \"status\": \"supports\", \"note\": \"Funk & Wagnalls New Standard, FSD_vol2.txt line 46590, and the running page number 1166 stands on that leaf: 'hob'son-job'son, n. [Anglo-Ind.] Name of the annual celebration of the Muharram of the Shiah Muslems, their name being a corruption of the cry of \\\"Ai Hasan! Al Hosain!\\\" raised at the great procession on the 10th day of the solemnity. Yule and Burnell Hobson-Jobson p. 419.' — the page and the content are exactly as cited.\"},\n            {\"ref\": \"KLN:735\", \"status\": \"supports\", \"note\": \"Klein s.v. hobson-jobson (KLN_1966.txt line 17906; 1966 2-vol. p. ~766 = p.735 of the one-volume printing): 'a festal excitement. — Corruption of Arab. yā Ḥasan! yā Ḥusayn!, cry of the Mohammedans at the procession of the Moharram. See Yule and Burnell, Hobson-Jobson, p. 419.' Note that Klein himself points to HJB:419, the page Nourai cites on the parent node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p. 419 (HJB.txt line 11172)\", \"stance\": \"supports\", \"note\": \"'HOBSON-JOBSON, s. A native festal excitement; a tamāsha …, but especially the Moharram ceremonies … we have ventured to borrow from it a concise alternative title for this Glossary.'\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol2.txt p. 1166\", \"stance\": \"supports\", \"note\": \"see the quotation in ref_check — an independent dictionary with the same derivation.\"},\n            {\"src\": \"WEB\", \"where\": \"grep 'hobson-jobson' in WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"no legible hit in the OCR of Webster's vol. 1.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-222.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\n"
}
```


### [2026-09-06T15:24:00.391Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk222.py (file state is current in your context — no need to Read it back)
```


## [2026-09-06T15:24:04.314Z] TOOL CALL #49: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk222.py && python3 -m json.tool data/verification/page-222.json > /dev/null && echo JSON_OK && python3 tools/verify_check.py 222"
}
```


### [2026-09-06T15:24:06.879Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 13/13
node verdicts: {'confirmed': 6, 'plausible': 5, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 12, 'not_checked': 6, 'partial': 2}
books consulted: {'supports': 16, 'silent': 9, 'partial': 6, 'contradicts': 3} | by book: {'LKT': 7, 'Wiktionary': 7, 'RCH': 4, 'AID': 3, 'WEB': 3, 'MON': 2, 'BQT': 2, 'HJB': 2, 'Etymonline': 1, 'SKT': 1, 'KLN': 1, 'FSD': 1}
```


## [2026-09-06T15:24:22.976Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-222.json` written; `verify_check.py 222` reports 13/13 nodes, 0 PROBLEM lines.

**Page 222 (book p. 192), 2 entries, 13 nodes**
- Root verdicts: confirmed 2 (Semitic ḥ-r-m; Arabic ḥ-s-n)
- Node verdicts: confirmed 6, plausible 5, transcription_suspect 1, disputed 1
- Ref checks: supports 12, partial 2, not_checked 6 (FVA = Nahvi, no digital copy anywhere; TYL = Taylor's S.P.E. tract, HathiTrust-only; AHD:626 = New College main dictionary, not open online)

Flagged items:
- **H.r.m / #4 Spanish "harmathan" — transcription_suspect (error_in: book).** No such Spanish word; Klein (KLN:704) prints "Sp. harmatan" (mod. harmatán); -th- is impossible in Spanish orthography. The printed page (pdf p.222, image saved to `data/verification/sources/refs/ocr/BOOK/222.png`) itself reads "harmathan", so the extraction is faithful and it is Nourai's misprint. The same node also drops Klein's Fante link (Arab. ḥarām → Fanti haramata → Sp.), so the arrow is only partial anyway.
- **H.r.m / #9 English "maranatha" — disputed.** Consensus (Wiktionary, Webster) reads 1 Cor 16:22 μαρανα θα as Aramaic *māranā thā* "Our Lord, come!" — an invocation, not a curse. Klein's Hebrew *mohŏram attā* "you are under ban" (KLN:937, which Nourai copies) is a minority conjecture; Klein himself concedes the Aramaic reading is the usual one. The other word in the node, *herem*, is fine.

Other notable (non-flagged) findings: English *harem* is via Ottoman Turkish (1630s), not straight from Arabic as drawn (Klein omits Turkish too); *harmattan* is from Twi/Fante directly per OED/Wiktionary, with Spanish a parallel borrowing; Lokotsch no. 1412 contradicts the *marrano* "converted Jew" arrow (he derives it from Hebrew *mar'e* "appearance"), so node #7 is only plausible; the H.s.n root gloss "to be kind, to do good things" is really the Form-IV (aḥsana) sense, not the base verb's.

**No extraction errors found** — the JSON matches the printed page throughout (including the Hâfez and Molavî couplets; the only differences are dropped short vowels, e.g. book حِرمان vs JSON حرمان).
