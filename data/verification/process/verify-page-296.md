# Verification process log — verify-page-296


## [2026-09-06T22:30:01.271Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 296 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-296.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-296.json. Write /home/sfmqrb/git/rishe/data/verification/page-296.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 296` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:30:02.796Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T22:30:03.584Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:30:03.601Z] TOOL RESULT

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


## [2026-09-06T22:30:03.763Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-296.txt"
}
```


### [2026-09-06T22:30:03.796Z] TOOL RESULT

```
1	=== PDF page 296 (book page 266) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kweye, Qweye : quiet, comfortable  (refs KLN:1740; POK:638)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:638; KLN:1740; KNT:210; ZFS:51 | šâ 3, šyâ 2 : to rest ; â-šyâ : resting place, nest ; šâiti 2, šyâtî : happiness, peace
5	  #2 (parent #1) [Persian] refs=HRN:6,169; BQT:46,1222 | ašîyâneh «آشیانه» : nest ; šâd «شاد» : happy | extra: آشیان ؛ شادی ، شادمان | NOTE: See "Gwhen 1" for another possible root of "âšîyân(eh)"
6	#3 (parent #0) [Latin] refs=AHD | quiĕs : quiet ; trans-quillus : calm
7	  #4 (parent #3) [English] refs=None | quiet, tranquil
8	#5 (parent #0) [Germanic] refs=AHD; KLN:1740 | hwîlô : resting period, a length of time
9	  #6 (parent #5) [English] refs=None | while
10	--- entry 1 ---
11	ROOT Kwi 1 -> redirect to Kwo
12	--- entry 2 ---
13	ROOT Kwi 2 -> redirect to Kwe
14	--- entry 3 ---
15	ROOT [Semitic] K.w.n : to be, to stand firm  (refs KLN:1433; SAP:716)
16	#1 (parent #0) [Arabic] refs=SAP:1454 | k.w.n : to become, to be, to exist
17	  #2 (parent #1) [Persian] refs=MON; FVA:359; FSF:265 | makân «مکان» : place ; kâenât «کائنات ، کاینات» : beings, world ; takvîn «تکوین» : creation ; kon «کن» : short for Arabic phrase "kon fayakun" | extra: کاف و نون
18	#3 (parent #0) [Semitic] refs=KLN:1433; AKD:30 | s.k.n : to lay, set, deposit
19	  #4 (parent #3) [Arabic] refs=SAP:716 | 
20	    #5 (parent #4) [Persian] refs=MON |  | extra: سکون ، ساکن ، مسکن ، مُسکن ، تسکین ، مِسکین
21	  #6 (parent #3) [Hebrew] refs=KLN:1433 | šekinah : standing calm, dwelling place (of God)
22	    #7 (parent #6) [Arabic] refs=MON:1902 | 
23	      #8 (parent #7) [Persian] refs=MON:1902 | Sakîneh «سکینه» : "calm, peaceful" | NOTE: a female name
24	
```


## [2026-09-06T22:30:06.672Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-296.json",
 "description": "Read source JSON for page 296"
}
```


### [2026-09-06T22:30:06.712Z] TOOL RESULT

```
{
  "pdf_page": 296,
  "book_page": 266,
  "entries": [
    {
      "root": {
        "name": "Kweye, Qweye",
        "lang": "Indo-European",
        "refs": "KLN:1740; POK:638",
        "gloss": "quiet, comfortable"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:638; KLN:1740; KNT:210; ZFS:51",
          "words": [
            {"translit": "šâ 3, šyâ 2", "gloss": "to rest", "script": null},
            {"translit": "â-šyâ", "gloss": "resting place, nest", "script": null},
            {"translit": "šâiti 2, šyâtî", "gloss": "happiness, peace", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:6,169; BQT:46,1222",
          "words": [
            {"translit": "ašîyâneh", "gloss": "nest", "script": "آشیانه"},
            {"translit": "šâd", "gloss": "happy", "script": "شاد"}
          ],
          "script_extra": "آشیان ؛ شادی ، شادمان",
          "note": "See \"Gwhen 1\" for another possible root of \"âšîyân(eh)\"",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "quiĕs", "gloss": "quiet", "script": null},
            {"translit": "trans-quillus", "gloss": "calm", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "quiet, tranquil", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN:1740",
          "words": [
            {"translit": "hwîlô", "gloss": "resting period, a length of time", "script": null}
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
            {"translit": "while", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kwi 1",
        "redirect": "Kwo"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kwi 2",
        "redirect": "Kwe"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "K.w.n",
        "lang": "Semitic",
        "refs": "KLN:1433; SAP:716",
        "gloss": "to be, to stand firm"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "SAP:1454",
          "words": [
            {"translit": "k.w.n", "gloss": "to become, to be, to exist", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON; FVA:359; FSF:265",
          "words": [
            {"translit": "makân", "gloss": "place", "script": "مکان"},
            {"translit": "kâenât", "gloss": "beings, world", "script": "کائنات ، کاینات"},
            {"translit": "takvîn", "gloss": "creation", "script": "تکوین"},
            {"translit": "kon", "gloss": "short for Arabic phrase \"kon fayakun\"", "script": "کن"}
          ],
          "script_extra": "کاف و نون",
          "note": null,
          "quote": {
            "text": "دو گیتی پدید آمد از کاف و نون - چرا نی بفرمان او در نه چون",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Semitic",
          "refs": "KLN:1433; AKD:30",
          "words": [
            {"translit": "s.k.n", "gloss": "to lay, set, deposit", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "SAP:716",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "سکون ، ساکن ، مسکن ، مُسکن ، تسکین ، مِسکین",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Hebrew",
          "refs": "KLN:1433",
          "words": [
            {"translit": "šekinah", "gloss": "standing calm, dwelling place (of God)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Arabic",
          "refs": "MON:1902",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:1902",
          "words": [
            {"translit": "Sakîneh", "gloss": "\"calm, peaceful\"", "script": "سکینه"}
          ],
          "script_extra": null,
          "note": "a female name",
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T22:30:07.368Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:30:07.404Z] TOOL RESULT

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


## [2026-09-06T22:30:49.759Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','POK','KNT','ZFS','HRN','BQT','AHD','SAP','MON','FVA','FSF','AKD','FVQ','BRT','PHD','NYB','HUB','ARY','PLA','LKT']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\"",
 "description": "Inspect refs_online metadata"
}
```


### [2026-09-06T22:30:51.451Z] TOOL RESULT

```
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== ZFS {"title": "Mohsen Abolghasemi, Zaban-e Farsi va Sargozasht-e An, Hirmand 1375/1996", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand. Other Abolghasemi titles are open on archive.org and parsianjoman, not this one."}
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only. Google Books no-view records 4y
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page 
== AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by semantic field; Akkadia
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
```


## [2026-09-06T22:30:56.892Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- POK_02 leaf 294 (p.638) ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==295' POK_02.txt | head -60\necho \"=== grep quies in POK_full ===\"\ngrep -n \"tranquillus\" POK_full.txt | head -20"
}
```


### [2026-09-06T22:30:58.549Z] TOOL RESULT

```
--- POK_02 leaf 294 (p.638) ---
tlich  nicbtidg.  Herkunft. Ai.  khädati  ,zerbeißt,  kaut',  npers.  xäyad  ds.,  könnten  zu  arm.  xacanem  ,beiße'  gehören, aber  auch  mit  sekundärer  expressiver  Aspiration  als  *lmd-  zu  lit.  kdndu  , beiße'  (etwas anders  oben  S.  560).  Zur  gleichen  Wurzel  ken-  (oben  559  ff.)  könnte  ai.  khdnati  , gräbt*, Inf.  khdni-tum,  Partiz.  khätd-  {*khn-to-)  gehören,  samt  den  Neubildungen  khä-  n.  , Höhle', ä-khü-  , Maulwurf,  khä-  .Brunnen'  =  av.  Nom.  Akk.  PL  äcä  ds. ;  ai.  khani-  ,wühlend',  f. , Mauseloch'  =  av.  kani-  , Graben';  av.  apers.  kann-  ,graben'  (k-  aus  kh-  aus  den  Kompo- sitis  mit  us-,  kam-).  Der  Anlaut  von  gr.  xäcpäv,  xrjcpTJv  , Drohne',  xcotpög  »stumpf,  taub' ist  unsicher,  ebenso  der  von  ksl.  chabiti  , verderben',  chabem  ,elend',  wie  auch  der  von ksl.  chomg-tb  , Kummet',  von  Specht  zu  lat.  hämus  {*khä-mo-)  , Haken',  gr.  /«^(i?  .ge- krümmt' (und  Jtfa/3d?  ds.)  gestellt  (anders  oben  S.  555).  Zum  Problem  der  Tenues  Aspi- ratae,  die  z.  T.  gewiß  als  sekundär  expressiv  aufzufassen  sind,  vgl.  Hj.  Frisk,  Göteborgs Högsk  Arsskr.  1936:  2,  S.  38ff.,  Specht  Idg.  Dekl.  251  ff.  Zum  slav.  anlautenden  ch- vgl.  V.  Machek  Slavia  16  (1938),  161  ff.  und  J.  J.  Mikkola  Urslav.  Gramm.  174ff.
Zahlreiche  ai.  Wörter  nichtidg.  Herkunft  mit  anlaut.  kh-^  darunter  die  oben  erwähnten, bei  Kuiper,  Proto-Munda  47  ff.
kiialo-s  ,eine  größere  Fischart*,  s.  unten  unter  (s)k^alo-s.
k^as-io-,  ~lo-  , Flechtwerk,  geflochtener  Korh'.
Lat.  quälum  (quallus)  ,geflochtener  Korb*  (*kuaslom^  vgl.  das  Deminutiv :) quäsiUus,  -um  ,Körbchen,  Wollkörbchen*  (mit  emphatischem  -ss-)  ;
abg.  ko§h  ,Korb*  (^k}^as-io-s),  russ.  ko§  ,Korb,  Fischreuse;  Hürde*  usw., ■  auch  ksl.  kosar(j)a  ,Hürde*  usw.,  russ.  koseh  ,Korb,  Brotsack*.
WP.  I  507,  Trautmann  119,  WH.  II  397.
j.  ic"e  enklit.  ,und*  aus  ,*irgendwie*,  wie  auch  zum  Pron.-St.  klio-y  k^e-  des  Inter- rogativums  und  Indefinitums  im  selben  Verhältnis  stehend,  wie  *ke jhier*  zu  Zco-,  ke-  , dieser*.  Damit  identisch  kV^e  hinter  Formen  vom Interrogativ-Indefinit-Stamme  zur  Verstärkung  des  indefiniten  Sinnes.
Ai.  ca,  av.  ca^  ap.  cä  enklit.  ,und*;  1yd.  -k  ,und*;  gr.  xe  ,und*;  venet. -ke^  lepont.  -pe,  piken,  -p ;  lat.  -que ;  ne-que  =  osk.-umbr.  nep,  neip  ,neque' =  air.  na-chj  mcymr.  usw.  nac  ,nicht*  (zum  a  aus  e  s.  unter  ne  ,nicht*), vgl.  lat.  atque  ,und  dazu*  (ad-\-que)  =  umbr.  «p(e)  ,ubi,  cum*;  got.  ni-h (usw.,  s.  unter  ne)  ,nicht*;  (s.  auch  ahd.  usw.  noh  unter  *nu  ,nun*);  bulg.  ce ,aber,  und,  daß,  weil*,  öech.  alt  a-ce,  ac  ,wenn*,  poln.  acz  , obgleich,  obwohl*;
den  indefiniten  Sinn  verstärkend  z.  B.  ai.  kds-ca,  av.  cis-ca  ,wer  irgend, welcher  irgend*,  in  Relativsätzen  mit  dem  Rel.-Fron.  ya-]  av.  cü-ca  auch ,jeder  beliebige*;
arm.  -k  z.  B.  o-k  ,irgendwer*  (wenn  Abfall  des  e  von  *kV[e  vor  der  Palata- lisi
=== grep quies in POK_full ===
```


## [2026-09-06T22:30:58.659Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD kwyeh / kweie ===\"\ngrep -n -i \"tranquil\" AHD_watkins1985.txt | head -20\necho \"=== AHD while ===\"\ngrep -n -i \"hwilo\\|hwīlō\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T22:30:58.722Z] TOOL RESULT

```
=== AHD kwyeh / kweie ===
650:kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
2400:TRAIN OIL dakru- TRAIT tragh- TRAITOR d6- TRAJECT yé TRAMMEL macula, trei- TRAMP der-! TRAMPOLINE der-1 TRANCE ei-1 TRANQUIL kweie-2 TRANS- tere-2 TRANSACT ag- TRANSCEND skand- TRANSCRIBE  skribh- TRANSDUCER deuk- TRANSECT sek- TRANSFER bher-1 TRANSFIGURE dheigh- TRANSFIX dhig¥- TRANSFUSE gheu- TRANSGRESS ghredh-
=== AHD while ===
```


## [2026-09-06T22:31:05.238Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"qui[eē]s\" POK_full.txt | head -20\necho \"---- POK_01/02/03 grep tranquillus ----\"\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"## $f\"; grep -n \"tranquillus\\|tranquill\" $f | head -5; done"
}
```


## [2026-09-06T22:31:07.264Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 p.1740 area: while / KLN_1971 shekinah ===\"\ngrep -n \"hwīlō\\|hwilo\" KLN_1966.txt | head -10\necho \"=== KLN 1971 while ===\"\ngrep -n \"^while\\|while (n\" KLN_1971.txt | head -10"
}
```


### [2026-09-06T22:31:07.962Z] TOOL RESULT

```
6534:acquiesce ' about Modern High German Art), Middle High German arl. Modern High 
17840:unruled mhas probably arisen from participle dammaintr. Old Irish dam- " acquiesce, 
19703:"*acquiescence' (/dial.?); 
20375:'funeral, obsequies; grave, burial mound', racpn ' funeral, grave', Ta(ppo(; ( *(i!^np^-ro-s) f. 
22291:steady acquiescence ');„/c>-present Old Indie dhayate^ places for oneself ' (= Latvian deju, 
52584:'; Old pers. siyati-s^ complacency ' (= Latin quies), Avestan sa///-5 "pleasure, joy' {s- = sy-, 
52591:Latin quies, -etis' tranquility ', quie-sco, -scere, -vT, -turn 'rest', with formants -/c»-(as 
66180:"quinquies'; -/77- after dem Kardinale, as also das /7from Quinctius and quinctus); Old High 
---- POK_01/02/03 grep tranquillus ----
## POK_01.txt
## POK_02.txt
4715:lat.  quieSy  -etis  ,Ruhe',  quie-scOj  -scere,  -vij  -tum  , ruhen',  mit  Formans -lo-  (wie  germ.  *hwil-)  tranqullus,  tranquillus  , ruhig'  {trans-{- k^llos)]
## POK_03.txt
```


### [2026-09-06T22:31:08.021Z] TOOL RESULT

```
=== KLN 1966 p.1740 area: while / KLN_1971 shekinah ===
=== KLN 1971 while ===
125295:while’, formed fr. inter , ‘between’ (see inter, 
178549:while teaching in the Lyceum. 
211003:while baking; 2) the clay of which it is made. — 
214605:while playing a musical instrument’, fr. schnur - 
266588:while, n. — ME. whil, while, fr. OE. hwil, ‘space 
266602:whiles, conj. (archaic), while. — ME. - whiles (in
```


## [2026-09-06T22:31:10.195Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '52570,52605p' POK_full.txt"
}
```


### [2026-09-06T22:31:10.244Z] TOOL RESULT

```
line, build ', probably also kir. koju, kojfty^ instigate, prepare something evil', as gr. cpovov 
noisTv "murder instigate '), poln. dial, /ro/ics/i^ "succeed, proceed, go ahead'. 

A 5- further formations in Avestan kaes- (with Praverbien) " to place together, heap up, 
pile, arrange ', fra- "prepare, make ready ', i//-" prepare, get ready ' (Bartholomae Wb. 
429). 

References: WP. I 510, WH. II 406, Berneker538, Trautmann 124. 
Page(s): 637-638 

Root / lemma: Iceia-, k''lie-{*IC'ehu-es) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to rest quietly, quiet, peaceful 

Material: Old Indie cira-m^ indecisiveness, delay', cira-^ lasting, continuing; ongoing, long 
'; Old pers. siyati-s^ complacency ' (= Latin quies), Avestan sa///-5 "pleasure, joy' {s- = sy-, 
compare gathav. syeitibyd), Avestan syata-, sata- " pleases ' (= Latin quietus), a-sata- " 
unhappy ' (= Latin inquietus), Flapu-aaTK;, Avestan saista- " most cozily, most gratifyingly ', 
np. sao' "blithe, glad', oss. ancayun^x^^'C; sogd. sV gleeful '; 

Armenian han-gcim^\ lie, rest ', han-gisV tranquility ' {-g'h from *-k"i-)\ 

Latin quies, -etis' tranquility ', quie-sco, -scere, -vT, -turn 'rest', with formants -/c»-(as 
Germanic 77by/7-) tranquTius, tranquiiius' peaceful' {trans + kfios); 

Maybe alb. ^e/e "quiet' a Latin loanword. 

Gothic tveila. Old English fiwJl, Old High German (ii)wJla " while, time'. Old Icelandic 
/7i//7a "couch, bed, place for resting ', hvlld' tranquility ', Gothic fveiian' stay, linger, 
hesitate, cease'. Old English HwaiaUH, Old High German wTion, -en' stay, linger'; 

Old Church Slavic pokojb " tranquility ', pokojg, pokojiti' calm, appease ', pocijg, pociti 
"rest'; 

Tocharian B sa/e"rich' (: Avestan syata-' pleases '); 

Lycian tezi' sarcophagus ' from *k"jetis{'7), Pedersen Lycian and Hittite 50.
```


## [2026-09-06T22:31:12.027Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==295' POK_02.txt | grep -n \"k\\^ei\\|siyati\\|šyāta\\|sa/ti\\|Ruhe\" | head\necho \"--- around line 4700-4730 of POK_02 ---\"\nsed -n '4700,4730p' POK_02.txt"
}
```


### [2026-09-06T22:31:13.632Z] TOOL RESULT

```
--- around line 4700-4730 of POK_02 ---
Wurzelerweiterung  k"eis-,  k"eit-  (vgl.  oben  ai.  cüj  citi-):
Air.  ad-cl  (*k^is-e-t)  ,sieht*,  clall  f.  , Verstand'  ==  cymr.  pwyllj  bret. poell  ds.  (*k}^eis-lä)y  usw.  (Lewis-Pedersen  350);
ai.  cBtatiy  ciketati  ,hat  acht  auf  etwas,  nimmt  wahr*,  Perf.  cikita^  Partiz. cikitvdn  ,verstehend,  wissend*,  av.  cikid-vä  , überdenkend,  überlegend*,  ai. citti-  f.  , Denken,  Einsicht*,  av.   cisti-  ds.,  ai.  cintä  , Gedanken,  Sorge*;
abg.  c&^Q,  cisti  ,zählen,  rechnen.  Geschriebenes  lesen ;  ehren',  *k^i-t-ti-  > chsth  (=  ai.  citti-h)  , Verehrung,  Ehre';  mit  anl.  s-  lett.  äJcietu,  skitu,  SUist , meinen',  Impers.  , scheinen',  sÄ:ai^i^  , zählen,  Gebete  aufsagen',  lit.  skait-au, -yti  jZählen,  lesen'.
WP.  I  508  f.,  Trautmann  113,  124,  135,  138,  Schwjzer  Gr.  Gr.  686,  697.
k'Xei-  ,aufschichten' ;  daher  ,aufhäufen,  sammeln',  ,der  Ordnung  nach  auf oder  zu  einander  legen',  ,aufbauen',  abgeschwächt  ,machen'. Ai.  cinöti^  cdyati  ,schichtet,  reiht;    sammelt,  häuft  an;    fügt  zusammen, baut  auf,  cdya-  m.  ,  Anhäufung,  Haufe,  Aufwurf;  kdya-  m.  ,Leib,  Körper* (eig.    ,*Gliederbau*;    oder    ,*Masse*?);    citä    ,Schicht,    Holzstoß,   Scheiter- haufen*, citi-  f.  , Anhäufung,  Schicht,  Scheiterhaufen',  clti-  f.  ,das  Sammeln' ; av.  kay-^  cayeitij  cinvaiti  ,(*legere)  aussuchen,  wählen*  mit  vi-  ,scheiden,
638  '
distinguereS  mit  harn-  .colligere,  (Schrittlängen)  aneinanderlegen* ;  np.  Sidat jSammeln* ;
gr.  Ttoieo)  ,mache*  (arg.-böot.  iTtoifvjas  u.  dgl.),  dann  auch  , dichte',  Deno-^ minativ  eines  *7toL-f6-g  , aufbauend,  machend'  (vgl.  dQTO-Ttoiög  ,Bäcker*)*^
abg.  ^im  (wahrscheinlich  w-St. :    ai.  cinö-ti,   av.  cinvaitij   doch  im  Slar, mit  l  der  ersten  Silbe,  wie  ai.  citi-)  , Ordnung,  Reihe,  Rang',  ciniti  ,ordnen reihen,    bilden',    wohl    auch   klr.    kojüj   kojity   ,anzetteln,   bereiten   (etwas Böses',  wie  gr.  g)6vov  tvolscv  ,Mord  anstiften'),  poln.  dial.  koic  sie  ,gelingeii  ' vonstatten  gehn'.
Eine  s-Weiterbildung  in  av.  kae§-  (mit  Präverbien)  ,struere',  frä-  ,2n- richten,  bereiten',  vi-  ,zu-,  herrichten'  (Bartholomae  Wb.  429).
WP.  I  510,  WH.  II  406,  Berneker  538,  Trautmann  124.
k"eid-,  kniie-  , behaglich  ruhen',  k^iie-t-s  ,Behagen',  k^iie-to-s  ,froh*, k^i-lo-  ,ruhig'.
Ai.  cird-m  , Zögern,  Verzögerung',  cird-  ,langdauernd,  lang';  apers.  siyäti-s ,Wohlbehagen'  (=  lat.  quies\  av.  säiti-s  , Freude'  (§-  =  sy-,  vgl.  gathar. syeitihyö)y  av.  syäta-,  säta-  ,erfreut'  (=  lat.  quietus),  a-säta-  ,unfroh' (=  lat.  inquietus),  Uagv-aarLgy  av.  säista-  ,behaglichst,  erfreulichst',  np. säd  ,froh',  oss.  ancayun  , ruhen';  sogd.  ft  ,freudig';
arm.  Jian-gcim  ,ich  ruhe',  han-gist  ,Ruhe'  (-gi-  aus  *-k]!:i-)]
lat.  quieSy  -etis  ,Ruhe',  quie-scOj  -scere,  -vij  -tum  , ruhen',  mit  Formans -lo-  (wie  germ.  *hwil-)  tranqullus,  tranquillus  , ruhig'  {trans-{- k^llos)]
got.  hveila,  ags.  hwllj  ahd.  (h)wlla  ,Weile,  Zeit',  aisl.  hvlla  ,Ruhebett', hvlld  ,Ruhe^,  got.  Iveilan  ,weilen,  zögern,  aufhören',  ags.  Hwäla  MN,  ahd. wilön^  -en  ,weilen,  sich  aufhalten';
aksl.  pokoj'b  ,Ruhe',  pokojg,  pokojiti  ,beruhigen',  jpocijg,  pociti  ,ruhen';
toch.  B  säte  ,reich*  (:  av.  syäta-  , erfreut') ;
lyk.  tezi  , Sarkophag'  aus  *k]tjetis  (?),  Pedersen  Lyk.  und  Hitt.  50.
WP.  I  510,  WH.  II  406,  Trautmann  124.
kUek-,  k)iök-,  k'^ek-s-  ,erscheinen;  sehen;  zeigen'.
Ai.  käsate  , erscheint,  glänzt,  leuchtet',  cakääüi,  cakäSydte  ,leuchtet, schaut',  kasa-  m.  , Sichtbarsein,  Schein';
av.  äkasat  ,erblickte';  npers.  ägäh  ,kundig',  nigäh  , Anblick';  «-Erwei- terung k'^eks- :  ai.  cdste  (3.  PI.  caksate)  ,erscheint ;  erblickt',  in  Kompositis auch  ,ankündigen,  zeigen',  caksas-  n.  , Schein,  Gesicht',  caksu-  ,sehend', n.  ,Helle,  Gesicht,  Auge';  av.  6as(te,  -äite)  ,lehren'  (eig.  ,gewahr  werden lassen'),  mpers.  cäsltan  ,lehren',  av.  apers.  casman-  n.  ,Auge',  npers.  ^asm  ds. ;
gr.  ThfxwQ,  jünger  tsxiiccq  (nach  TS'AfxaLQcj)  ,Zeichen,  Merkmal'  (*Ä^«£- w[ö]r-?);  anders  Schwyzer  Gr.  Gr.  I  326;
m
WF  639
K  jnit  tönendem  Auslaut  aksl.  kazg,  kazati  ,ze]'gen,  mahnen*,  u-kaz%  ^^it6-
K.       Jfit?^^'   (^^^^  kaznh  jdöy^a,  Anordnung*),   wohl   idg.  '^klJteg-  neben  *k^ek-? mt  WP.  I  510  f.,  Schwyzer  Gr.  Gr.  I  326,  519.
t  ^  knCl-,  k'AelQ-  ^drehen,  sich  drehen,  sich  herumhewegen,  fürsorglich  um jemanden  herum  sein,  wohnen^  u.  dgl.;  k'Aelo-,  k'^olo-  ,Drehung, Rad',  k'Aol-so-  ,Hals'  (lat.  ir.  germ.),  k^ekV.lo-,  k^oklilo-(?)  ,Rad^
Ai.  cdratiy  calati  ,bewegt  sich,  wandert,  weidet,  treibt'  usw.  (schwere Basis  in  cdritum,  caritd-,  clrnd-;  caritra-  n.  ,Fuß,  Bein',  carcürydmäna-, cürti-j  auch  wohl  tuvi-kürmi-  ,tatkräftig'),  dehnstufig  cära-  m.  ,Gang',  usw. ; ar.  Saraiti  ,versatur,  obliegt  einer  Tätigkeit'  usw.,  caräna-  ,Feld',  apers. parikarä  ,pflege!  cole!*;
```


## [2026-09-06T22:31:29.849Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT siyati ===\"\ngrep -n \"šiyāti\\|siyāti\\|siyati\" KNT.txt | head -20\necho \"=== BRT saiti / syata ===\"\ngrep -n \"šyāta\\|šāiti\\|syāta\\|sāiti\" BRT.txt | head -30"
}
```


### [2026-09-06T22:31:29.932Z] TOOL RESULT

```
=== KNT siyati ===
4082:23 duvaistam : šiyātiš :axSata :hauvei =’
4518:1 baga : vazraka : Auramazda : hya : ima 2 m : bümim : ada : һуа : avam : asm 3 апат : айа : hya : martiyam : ada : 4 hya : šiyātim : ada : martiyaby
=== BRT saiti / syata ===
```


## [2026-09-06T22:31:31.626Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN entries ===\"\ngrep -n \"^ *6\\. \\|^ *169\\. \" HRN.txt | head\necho \"=== HRN sad/asijan ===\"\ngrep -n -i \"âšijân\\|asijan\\|āšiyān\\|sâd \\|šâd \" HRN.txt | head -20"
}
```


### [2026-09-06T22:31:31.689Z] TOOL RESULT

```
=== HRN entries ===
490:6. abiSy^ur, abisxurdy äb/ifr (geschrieben und früher ge-
10035:6. ahöklnltan Verunreinigen, beschmutzen', ähökinttär
10940:169. i^urmah 'VoHmond' (AW.-Komm.).
21413:6. astor 720.
21578:6. isiorr 720.
21943:6. ?7<<;d 1098.
22044:6. ijtiBaj 428.
=== HRN sad/asijan ===
```


## [2026-09-06T22:31:40.234Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## HRN printed p.6 (leaf 27) ##########\"\nawk 'BEGIN{RS=\"\\f\"} NR==28' HRN.txt\necho \"########## HRN printed p.169 (leaf 190) ##########\"\nawk 'BEGIN{RS=\"\\f\"} NR==191' HRN.txt"
}
```


### [2026-09-06T22:31:41.892Z] TOOL RESULT

```
########## HRN printed p.6 (leaf 27) ##########
6 -
phlv. evar (vd. 5 (146) Gl., Men.), päz. äwar^),
evarih (vd. 5 (146) Gl.). (Darmesteter, Et. ir. I, 251).
phlv. evar führe ich auf ap. *adi -+- [/'var- zurück;
adi (ai. adlii) kommt auch noch in estäden (und
vielleicht in evän, evar (^INZ^N Jer. 5, 6) vor (vergl.
KZ. 32, 581).
17. ärey 'Hass, Feindschaft*, rey,
ap. araika- Teind'; aw. ara^ka-.
Statt ärey ist vielleicht erey zu verbessern (dann
wäre rey die lautgesetzliche Form); die altpersische
Form könnte andernfalls natürlich auch äraika- gelesen
werden.
18. äz 'Begierde' (z. B. Vis und RämTn, Seite 47 Vers 14),
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
deutung *Ehre, Achtung* (GF.), anäzarm (Men.), vergl. Vis und Kämln,
Seite 32 Vers 12, 86 Vers 3 v. u.
########## HRN printed p.169 (leaf 190) ##########
— 169 —
Stützhülz (am Joch)'); arm. .sami\/v 'Stirnliolz des
Ochsenjoches (de Lagarde, No. 19:^8) i).
Xp. sim *Silber , sitnm 'silbern' (phlv. usltn, astnnn)
dagegen ist bekanntlich griechisches Lehnwort (vergl.
zuletzt Nöldeke, Pers. Stud. II, 45).
765. sl/inury 'Greif, Adler; N. pr.', vergl. STn\duxt,
aw. saenö mereyö- *Adler' ; phlv. stnmuro, seiw murük
(Yätkrtr-r Zar. S. ()4).
ai. ^ijefui' Talke*; arm. ein milvus (H. No. 280).
S,
766. Süx 'Zweig, Ast; Hörn (des Stieres), Greweih'.
ai. rdkhä' 'Zw^eig, Ast*; phlv. säk (West 111, 118
Note 1), natak]sak (Bund.) d. i. säx; arm. cu/ (H.
No. 279); lit. szakfi.
LW. kurd. säy; aty. ^ä/; bei. mh 'Hörn, afrt/ 'Ast*;
wa;K. soZ/, sar. so^ 'Zweig', wa;!r. mo, sar. xdo 'Geweih'.
Vergl. zuletzt Bartholomae, Studien II, 41 folgg.
767. Häd 'fröhlich, heiter , sadt,
ap. siyäti- 'Behagen, Freude*^); aw. säiti-; phlv. sät,
sätlh; lat. vergl. quietus, quies.
088. äncad 'Stille', d. ancayim, t. ancain *ruhen* (24).
768. Hiiiu 'Abendmahlzeit, Nachtessen*.
aw. x^^f^W^'"'» phlv. säm (y. 61 (19) = 62, 7).
LW. kurd. säm *Abend'; af;^. süme Zeit zwischen
Mitternacht und Tagesanbruch; Nachtessen, Leichen-
schmaus', mä\xäm 'Abend' (?); bei. säm 'Hauptmahlzeit,
Abendessen* (259); sar. /?/w, yidg. säm.
') Nichts wesentlich Neues bringt Bugge, KZ. H2, 24.
Als Betonung von aw. simä" muss natürlich oxytonale angenommen
werden. Das Wort ist mit den von Bartholomae, BB. XVII, 114 folg.
gesammelten zusammen zu beurtheilen.
*) Und wohl auch zugleich *Wohnstätte*, vergl. Bartholomae,
Arische Forschungen, II, 102.
```


## [2026-09-06T22:31:57.192Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Nest\" HRN.txt | head -20\necho \"---- p.5 leaf26 ----\"\nawk 'BEGIN{RS=\"\\f\"} NR==27' HRN.txt | head -50"
}
```


### [2026-09-06T22:31:59.228Z] TOOL RESULT

```
740:35. äsyäne, äsyän 'Nest'.
8972:1034*>*» niseni *Nest* (Sahn. I, 137 Vers 146), nisemen i).
8975:hört dazu etwa auch äsyäne *Nest' (No. 35)?
---- p.5 leaf26 ----
5 -
gesetzlich unmögliche Etymologie Spiegel' s (Keil-
inschriften 2, 238, Ar. Periode 284) findet sich noch bei
Bechtel, Hauptprobleme, 163.
12. äräm *Ruhe*, ärarmden, arätnis, nu^'0'nN (jüd.-pers.
Bibelübs. ^).
aw. äramayat *er erfreute'; phlv. aramUan, äräni
*Ruhe'.
af/. bei. (18) LW. äräm,
Vergl. räm (No. 604).
\^. ärd 'Mehl'.
\ Käs. ort, ürt, vergl. auch s. v. äsyäh : ör, ä/-, ir,
aw. asa- gemahlen', anasa- (Hübschniann ZDMG.
38, 428); phlv. ärd ^Mehl'.
kurd. är, ärd (Jaba-Justi), ärf, irt (Houtum-
Schindler); af/. öra; bei. ärt n. arf (15); arm. aZ^wr
*Mehr, ahxm 'mahlen* (unsicher, H. No. 7).
14. uren *Elle', äreng^ ärenj,
phlv. äranj (PPGL).
oss. arm-arün *Elle'; sar. yovn 'Ellbogen*; gr. wXsvfj;
lat. ulna.
Vergl. aw. radni- in frara&nidrajö^); phlv. eratn (?);
ai. aratni' 'Elle'.
Die neupersischen Worte werden richtiger mit ä
(bezw. e) zu schreiben sein.
15. äroy (AM. S. 95 Zeile 2), üröq *das Rülpsen , äröytden,
röy,
gr. BQsvyo/Liai 'rülpsen*; lat. ructäre^ ructus 'das
Rülpsen*; lit, raugmi, rugiü 'rülpsen'; ksl. rygayq;
ags. rocetan (Hörn).
Zu arm. orc 'Speichel, Erbrochenes*, orcam erbrechen,
rülpsen* vergl. H. No. 233 und Bartholomae, Studien
n, 134.
16. äri 'fürwahr.
Käs. ore, dre^ drl.
^) Die Endung -ist ist bekanntlich im Afghanischen in der Form
'ist und -ast nicht selten.
*) Bartholomae BB. 17, 111 Anmerkung.
```


## [2026-09-06T22:32:03.885Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '735,760p' HRN.txt\necho \"=== which leaf/page is line 740 on? ===\"\nawk 'BEGIN{RS=\"\\f\"} /35\\. äsyäne, äsyän/{print \"leaf(1-based)=\"NR; print substr($0,1,200)}' HRN.txt\necho \"=== 1034 nisem ===\"\nsed -n '8965,8985p' HRN.txt"
}
```


### [2026-09-06T22:32:05.674Z] TOOL RESULT

```
ap. *ä(x)snäka- 'bekannt'; phlv. äsnäk.- 9 ~
34(2). äänä, äsnäh 'Öchwinuner, Schwimmerei', üsnäh^ dsnäiv,
aw. ai. ä -f- [/'snä-, nur in der Bedeutung Vaschen' ;
vergl. aber aw. asnätar-, skr. äsnäna- (*Bad').
Vergl. sina (No. 792).
35. äsyäne, äsyän 'Nest'.
a + aw. Ksö- bezw. gäi>. syä- ruhen' ^), oder wohl
bereits wohnen'^). (Nöldeke, mündliche Mitteilung).
Aber das y ist auffällig, vergl. np. süd,
36. üyärden, ayäriden Verschlingen*.
ai. ä + l/^gar- {jacjdrd) verschlingen' ; lat. coräre,
wa;^. nez-yar-am verschlingen*.
In der Bedeutung Verschlingen' vermag ich das Wort
nicht zu belegen. Bei AM., wo es sehr häufig vor-
kommt, bedeutet es immer vermischen, einweichen in'.
In der letzten Bedeutung könnte es zu skr. l/^ghar-,
ghdrati 'besprengen, beträufeln* gehören^).
37. äftäh *Sonne, ixDS'X (jüd.-pers.).
skr. "^ahha + tapa- (vergl. No. 3).
kurd. LW. a^taw (Houtum-Schindler), ätätv etc.
(Jaba-Justi).
38. äfdutn 'letzter', nur im Mujmil ettevärT;^ (ed. Mohl,
Journ. asiat. 1841, S. 178)^), vergl. hafdum zuletzt*^).
«) Hübschmann, ZDMG. 38, 431.
') Bartholomae, Arische Forsch ungren II, 102.
*) Dazu wohl auch äyisten, z. B. AM. 14 Zeile 16, 193 Zeile 11.
=== which leaf/page is line 740 on? ===
leaf(1-based)=31
- 9 ~
34(2). äänä, äsnäh 'Öchwinuner, Schwimmerei', üsnäh^ dsnäiv,
aw. ai. ä -f- [/'snä-, nur in der Bedeutung Vaschen' ;
vergl. aber aw. asnätar-, skr. äsnäna- (*Bad').
Vergl. sina (No.
=== 1034 nisem ===
1034. niseb Unteres; unten'.
aw. *mxsvaepa-, vergl. x^^^W^' (No. 799) ; phlv.
n(i)Sep (AV.), n(i)sepitan^ n(i)sepmd 'sie gehen unter*
(Salemaifn, Mel. asiat. IX, 238), vergl. v(i)seft, 'Ver-
lorenes Sprachgut*, No. 229.
>) VergL Rückert, ZDMa. 10, 138.
2J Vergl. besonders äähn. II, 765 Vers 11 ; auch II, 611 Vers 1601.— 232 -
1034*>*» niseni *Nest* (Sahn. I, 137 Vers 146), nisemen i).
Doch wohl auch zu np. nisesten (No. 1033), wenn-
schon die Erklärung der Formen schwierig ist. Ge-
hört dazu etwa auch äsyäne *Nest' (No. 35)?
skr. LW. niglmana" (PärasTpr. ed. Weber, No. 433).
1035. neft ^Naphta .
aw. napta- *feucht' ; ai. l/^nabh-, ndbhatB 'spalten,
platzen; hervorquellen*.
LW. ar. naft; kurd. nefte; bei. n. napt 'Donnerkeil,
Blitzstrahl, Kanone' (No. 177) gehört aber wohl nicht
hierher.
Arische Doppelformen naph- und nabh-, vergl.
Hörn, KZ. 32, 584 No. 16.
1036. fUgasten malen', Praes. nigär-em, nigarld^n^ nigär
```


## [2026-09-06T22:32:28.503Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT charset sample ===\"\ngrep -n -i \"sy.ta-\\|sāiti\\|s.iti\" BRT.txt | head -20\necho \"=== BRT 'Behagen' ===\"\ngrep -n \"Behagen\" BRT.txt | head -20"
}
```


### [2026-09-06T22:32:28.575Z] TOOL RESULT

```
=== BRT charset sample ===
182:Ich  hatte  zunächst  die  Absicht,  unter  jedem  altpersischen  Wort  dessen  assyrische und  elamische  (skythische,  medische,  neususische)  Übersetzung  anzuführen,  bin aber  wieder  davon  abgekommen,  weil  ich  mir  keine  besondere  Förderung  dadurch versprechen  kannte,  und  habe  mich  darauf  beschränkt,  für  einzelne  Stellen  auf jene  Übersetzungen  zu  verweisen.  Es  mag  vielleicht  dieses  Verfahren  dem  oder jenem  folgewidrig  erscheinen,  weil  ich  ja  für  die  awestischen  Texte  die  'Tradition' durchgängig  herangezogen  habe.  Aber  man  wird  doch  auch  nicht  verkennen,  welch gewaltiger  Unterschied  zwischen  den  beiderseitigen  Übersetzungen  besteht.
191:Ich  würde  bei  solcher  Sachlage  sinnloser  Raumvergeudung  geziehen  werden müssen,  hätte  ich  bei  jedem  Wort  die  ganze  Reihe  der  gleichen  oder  ähnlichen Fundatellen  aufgeführt  Wohl  aber  muss  man  gegebenen  Falls  in  der  Lage  sein, aUe  Belege  eines  Worts  bequem  einzusehen.  Diesem  Zweck  soll  die  nachstehende Konkordanz  dienen,  in  der  ich  nur  jene  Stellen  nicht  berücksichtigt  habe,  die sich  deutlich  als  Anführungen  aus  anderen  bekannten  Avestatexten  ■ —  insbesondere den  ^aSischen  —  kennzeichnen;  z.B.  Y.7.a4f.  -von  yehya  bis  _)'(i7'?(=  Y.  4:5.  7a und  41.  ${.),  N.  71  (Blatt  147,  Z.  14 ff.)  von  am>sa  sp»nta  bis  jasaiti  (=  Y.  Ä3f.); wo  es  nötig  schien,  habe  ich  das  Sigel  Z.  (Zitat)  verwendet  —  Das  Zeichen  :  soll
2408:0  bei  Textanfiihrungen  schliesst  von  mir  ergänzte  Wörter  ein,  während  die  mit  []  einge- schlossenen zu  beseitigen  sind.
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
2483:—  para  ahtnSi  .  .  cinasti  ya%a  ^aitavS x'aitäifm  (sA)  Y.20.  i,  3)  auf  ein Relativum  als  dessen  Korrelat;  a)  adjek- tivisch: ahmili  naemäi  uzjasäitt  mtiro  .. yahtnai  naimanqm  mOiröJruxl  nai-ia  .  . paiti.päiti  Yt  /0. 1 9 ;  —  aÄ  . .  alsam  narqm yöi  kacahi  Yt/7.6;  —  mffirpm  ahyä *madahyä  (sd.)  yä  .  .  uräpayHntl  (sd.)  Y. Jt^.io;  —  Svat  A3  nü  ankuyaite  .  .  cvat ahmäi  naire  m^tm  aahat  yÖ  .  .  frama- r,UU\.4-4t;  Y.62. 1,  Yt.  10.137;  —  "^^ dussar^hahe  . .  manö  3at  ahe  .  .  mane  yö ml  dussatahö  hutaite  Y./0.12  (s.b);  — ipas  vloaSa  .  ./rS  *aAhe  vXsaiti  mt>rö ..
2600:yätumantJhe  jasaiti  •'.  .  der  verfällt  in  die  's^'"   ^■'0^'>;    —  .la/  t,f  sra-.a  dr?n-j;.\in
2643:•  j.  aenaahe,  g.  +''oaöhe  Inf.  'einem (GÜubigen)  Gewalt  anzutun,  an  ihm  Ge- walttat zu  verüben'  a)  mit  Akk.:  hyal  mäi ärfg7-i'j  dläar>iat3  (sd.)  'nariAl  Y.  4^.  7  ;  I —yi  rä  mäi  yä  gaf^<i  (fazdg(sd.)  'naiihg\ \.46.B.  b)  mit  Gen.:  naeÜlcä  *atiha jässiti  .  .  mahrküi  (sd.)  ndit  -nanke  Y. (»5. II.  c)  mit  Pianü  und  Akk.:  Ayat •^natike  dng^'atö  S»ana  i^yPng  arghaya  (sd.) Y.^2.i6.
2663:dva   danart  .  .  'va    (statt   ASn.!)    danan  ayar»   äjasaiti  °va  vä  xsapa  Aog.  5/;  —
2743:•  j.  aesmö.barvtay-  f.  'Darbringuog  von  isa^ta  Yt.  i^.  53;  — yff  naeeim  isaiti  huna- Brennholz':  alvayacif  °niii  (IS.)'*  aiva-  ranqm'V.ij.i9;Aog.48;  —  äiä ..Ayämii , . yacit  bar7sm3.stir?iH  Y.24~  aiavanö  tnsyä  istsm^^  rJiVl'(sd,)  Y.  40. 4;
2768:mit  paiti  i)  'streben  nach  — ,  begeh- ren': a)  mit  Akk,:  tafca  yä  kasu.xratul ,  masyöjcrdkwqm  (sd.)  nöit  paitiSaiti  V.  7, I  59.  b)  mit  Gen.:  s.  AbsoL  a)  'sich befleissigen,  betätigen',  mit  Akk.'>:  paiti- sata  (2P.)  mazdayasna  sraoiahe  a/yeke '  yasmm  Y.  37. 13;  —  staota  yesnya  yaza- maide  .  .  dadräna  paitHäna  paitiima- .  r^mna  Y.  55. 6 ;  —  six/anlfm  sa/ayaitt^m paitisant^m  Vyt52,  *P- /?  (wo  °Ä«- ,ljm)'i^.  3)  'erfahren,  erleben':  iaia lUli  (sd.)  *paitUäma  '*>  frya  paiti  tanvi ,  Yt.  i7, 10.  a)  bes. 'zur  Vergeltung,  zum Dank  erfahren,  empfangen':  kä>:ä..kä%3 .  (sd.)  saidyäi  yS  I  paitisift  Y.44.2 ; — ya^a ahmya  amtsa  spmta  sraoläoa  aiyäoa paitisqn  . .  yasnqsca  vahmqsca  Y.  öb.6.
2847:Abi  "t,  >     'irV'  *  i>  "^  PS  .  "  ',  ■    -f  _  '*'"*•  gross  machend  :  pattistitie  üismahe
2877:anrufen';  aoxtö  rattis  aoxtö  sraoiävarjzö ci'iqm  frä^wfrisaiti  (sd.)  "der  (zu  dem Zweck)  angerufene  R.  .."  V.  7.  7 1 ;  5.  26'; —  yezi  .  .  apsrmSyukö  .  .  aoxtö  vä  Ae aoxte  '^wat  pairi.^auAa  "wenn  .  .  das Kind  .,  oder  angerufen  zu  ihm  sagt:  Ich will  dich  begleiten'"  N.  7;  7(?).  *aojaite V.  Ä'.8oPüZ.(?).  .
3074:urvilnö    tffKö.hva    *mxansaiti   "der   zerrt
3098:Komp.  mit  LS.  im  i.  Glied  0,  eig.  'des  Wagen an  der  Spitie  geht'.  —  ")  Vgl.  ai.  a^te',
3170:Uta  %rayam  vahiltanqm  amiiyS  (sd.) bw^ata  . .  "^raj/am  'tatiqm  aiwi'hyö  buyata V.J.V  17;  —  'y,i  maiyä  Uä  (APn.)  daniö vaxhnii  dagi5jsuitif(%A..)  Y._32.  4; —  aya *mainiv3  varatä  (sd.)  yi  dngvH  'tä Timyö  . .  Y.  30. 5 ;  —  yi  ..  yazli  apä  . . 'bm    mantüm    (sd.)    Y.j;^.  4.  a)    mit
3207:seitigen' :ya%a  nöil*aiti  nüsitica'^ *airi^a "dass  sie  nicht  durch  Beseitigen  und  Ver- bergen Schaden  nehmen"  N.  6j  (?).
3296:doppelt: 'et  ,  ■  et':  a^ra  aö-  frajasaiti baxta{sd.)  fl'>°  nijasaiti  V.5.8;  —  am»sa sptntl  , .  ao°  M-lta  (sd.)  ao°  büta  haca vanhaot  manaifhöYx.ii.\2.
3376:einleitend  'so';  a)  hinter _)■«/  'wenn':  yat  A3 aexta  asfa  . .  °i^fl  *Aa  ''xsayde . .  haxtsit (sd.)  N.^;  —  yas3  '^wä  ..jasaiti  vq'^waiSö .  .  °iJo  imam  vacö  dnnjaySÜ  °^ii  .  .  Yt. ;_;. ao.  b)  hinter _)'«/:  yezi  vaH ..taur- vayo  . .  *^a  ima  naminis  framrava  YL ;.  lof.;  Nik.  2;  —  nachgestellt:  yai  .  . irisyeiti  aiiiAa^  Aaca  syadä^navartza  {&A.) ''ia  bavainti  pjsöJa/waV.  13.38.  c)  hin- ter _)'ffoJ»V  'sofern':  *ya(töil(sd.)  ..asrävayo Ayat  ">«  ..  ästryeitiH.44-  |.N,5o:  lies iia;  —  N.  io:  lies  o^ra.)
3432:•  j.,  g.  a'^Tä  Adv,  1)  räumlich  'hier;  da- hin' :  °ra  pasiaHa  vazaile  vats  . .  värsmca ..  avi  asä  Yt.Ägs;  /p.69;  —  «a/  °ra vicarmti  .  .  yty.49;  V.  J7,s; — yai  °ra para.jasaiti  ..  ya^ra  .  .  Ytio.ioi;  — *'fa')  *a'^viayaM/tJin (s<i.) yaira ..N.  10 ; — 3fl/  '^wa  °ra  spmta  . .  nuryja  . .  vTian/t Y./O.ii;  —  mü  "ra  frakavS  , .  V.s.ag; —  'ra  ml  urvarä  raoimti  V.j.ig;  Vyt. ^5(1*).  43'>  —  °ra  (ava.  'bei  ihm')  anät frajasaiti  baxta{&d.)V.^.i;  —  'rä  tu  ars- ärJi/isd.)  iär..ya>rJ..\. 46.16.  a)mit Gen.":  °r3  avAqm  {apqm)  hqm.bavainli dra  udra  "ibi  hanim  (aquarum)  .  ."  V. JJ'S'-  2)  zeitlich  'dann,  da',  hinter einem  Nebensatz  mit  yal,  hyap'>:  hyat  tu mazda  paourvim  gaihsscä  tais  .  .  °rä *vääm  barain ..  ^ins.vaea  (sd,)  vü  Y.31. 12;  —  aat  yat  mtirö  fravazaite  . .  -ra  .. darizayäli  VtiO.48.
=== BRT 'Behagen' ===
5164:—  Sal  dli  ävaidayamahi  . .  "vatthe  Y.4. 6.  a)  ellipt:  'vaiiihe..  timänS.paite'^xa Hilfe!  Hausherr"  V./Ä19;  31,22.  LS. avöaüs  Inf.  sbes.  2)  'Ergötzen,  Behagen' (nur  Komp.).
6348:•  j.  aäa.x''ä*i^-"  Adj.  'der  das  Behagen, Glück  des  Ala  gewährt' (?),  von  Bergen: gairlm  usi.darmjin    ..    "rim  Y,  1'.  14;  —
6362:•  j.  a-säite'*  Inf.  'sich  zu  freuen,  behag- lich zu  fühlen':  ya'iia  vätS ..  vJsp^m  ahUm .  .frähatica  .  .  aiwüa  as°  Jsmayäiti  "wie der  Wind . .  die  ganze  Welt . .  in  Behagen versetzt"  A.  4-  6-
11338:•  g.  CiSriLavah-,  j,  ^Äiftra.avah- "  Adj. 'deutliches,  augenfälliges  Ergötzen,  Behagen schaffend':  at  tsi  atrSm  ahurä  usSmakJ.. ^aslstjm  imavaithm  f/ö((sd.)  raparUE  'vav- h)m  ai  .  .  "von  deinem  Feuer  {Ätar),  o Ah.,  . .,  dem  verheissenen ,  machtvollen, wünschen  wir,  dass  es  dem  Getreuen  augen- fälliges Behagen  (schaffe),  aber.,"  ^.34. 4*>;  —    narqm  ..  *°Z'anhqm  Ny.j.  10'*.
16318:•  j.  pourus-x'^Sra-  Adj,  {fem,  'rä-)  'der  j viel  Behagen,  Glück,  Wonne  gewährt':, alis  'ra  Yt.  15.54;  —  kahmsi  istlm  °rqm\ azim  baxsäni  Yt/o.io8;  Y.6Ä11-
24443:•  j.  vispa  Jt'aÖTa-  Adj.  'der  alles  Behagen, Glück,  alle  Wonne  besitzt  und  gewährt":
```


## [2026-09-06T22:32:30.837Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/git 2>/dev/null; cd /home/sfmqrb/git/rishe\ngrep -rl \"Gwhen\" data/extracted/batch/ | head\necho \"---\"\npython3 - <<'EOF'\nimport json,glob,os\nfor f in sorted(glob.glob('data/extracted/batch/page-*.json')):\n    try: d=json.load(open(f))\n    except: continue\n    for e in d.get('entries',[]):\n        n=e.get('root',{}).get('name','')\n        if n and n.lower().startswith('gwhen'):\n            print(f, json.dumps(e,ensure_ascii=False)[:1500])\nEOF"
}
```


### [2026-09-06T22:32:32.801Z] TOOL RESULT

```
data/extracted/batch/page-365.json
data/extracted/batch/page-262.json
data/extracted/batch/page-121.json
data/extracted/batch/page-215.json
data/extracted/batch/page-546.json
data/extracted/batch/page-212.json
data/extracted/batch/page-548.json
data/extracted/batch/page-92.json
data/extracted/batch/page-393.json
data/extracted/batch/page-246.json
---
data/extracted/batch/page-212.json {"root": {"name": "Gwhen 1", "lang": "Indo-European", "refs": "POK:491", "gloss": "to swell, fill"}, "part": 1, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan / Old Persian", "refs": "ZMA:49-51", "words": [{"translit": "šan, šyangh", "gloss": "house, household", "script": null}], "script_extra": null, "note": "Cognate with \"kan 1, xan, gan 1: to dig out an mound up (a shelter)\"", "quote": null}, {"id": 2, "parent": 1, "lang": "Pahlavi", "refs": "BQT:46; ZMA:49-51", "words": [{"translit": "šân", "gloss": "house, shelter", "script": null}, {"translit": "â-šân-ak", "gloss": "house", "script": null}, {"translit": "hu-šangh", "gloss": "with good household", "script": null, "see": ["Su 1"]}], "script_extra": null, "note": null, "quote": null}, {"id": 3, "parent": 2, "lang": "Persian", "refs": "ZMA:49-50; BQT:46,2395", "words": [{"translit": "šan", "gloss": "house", "script": "شَن"}, {"translit": "šandaf", "gloss": "house tambourine", "script": "شَندَف", "see": ["Deru 1"]}, {"translit": "Hŭžšang", "gloss": "owner of good household", "script": "هوشنگ", "see": ["Su 1"]}], "script_extra": "ـ شان ، ـ شانه ، بغ شن ، شندیز\nگلشن ، کاشان ، کاشانه ، آشیان ، آشیانه", "note": "See \"Kweye\" for another possible root of \"âšîyân(eh)\".", "quote": null}, {"id": 4, "parent": 0, "lang": "Sanskrit", "refs": "PRT:75", "words": [{"translit": "ğanâ", "gloss": "ditch", "script": null}, {"translit": "xanda", "gloss": "a broken lump of sugar", "script": null}], "script_extra": null, "note": null, "
data/extracted/batch/page-213.json {"root": {"name": "Gwhen 1", "lang": "Indo-European", "refs": "POK:491", "gloss": "to swell, fill"}, "part": 2, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan / Old Persian", "refs": "POK:491; HRN:194; BRT:583; ZMA:49", "words": [{"translit": "kan 1, xan, gan 1", "gloss": "to dig dirt out and mound it up", "script": null}, {"translit": "čât", "gloss": "well", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Pahlavi", "refs": "HRN:194; BQT:1707; SNS:8,155", "words": [{"translit": "kantan, xandan", "gloss": "to dig", "script": null}, {"translit": "kandak", "gloss": "a dug-in house", "script": null}, {"translit": "xânîg", "gloss": "spring, water pond", "script": null}, {"translit": "čâh", "gloss": "well", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 3, "parent": 2, "lang": "Persian", "refs": "BQT; HRN:186; FVF:593", "words": [{"translit": "kandan", "gloss": "to dig", "script": "کندن ( کان )"}, {"translit": "kandak", "gloss": "places dug out in a house", "script": "کَنَدَک"}, {"translit": "kandŭk", "gloss": "grain silo, bee hive", "script": "کندوک"}], "script_extra": "کندوله ، کندوج ، کندو ، کندره ، کندور", "note": null, "quote": {"text": "ده و دو هزار انگبین کندره - به دژ ها کشند آنهمه یکسره", "poet": "Ferdowsî"}}, {"id": 4, "parent": 3, "lang": "Greek", "refs": "SKT:217", "words": [{"translit": "konda, kondu", "gloss": "a drinking vessel", "script": null}], "script_extra": null, "note": "Der
data/extracted/batch/page-214.json {"root": {"name": "Gwhen 1", "lang": "Indo-European", "refs": "POK:491", "gloss": "to swell, fill"}, "part": 3, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan / Old Persian", "refs": "POK:491; HRN:194; BRT:583", "words": [{"translit": "kan 1, xan, gan 1", "gloss": "to dig dirt out and mound it up", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Avestan", "refs": "POK:491; HRN:194", "words": [{"translit": "â-kand, â-gand", "gloss": "to fill", "script": null, "see": ["Apo"]}, {"translit": "aiwi-kand", "gloss": "to throw away", "script": null, "see": ["Ambhi"]}, {"translit": "para-kan", "gloss": "spread around", "script": null, "see": ["Per 1"]}, {"translit": "paiti-kan", "gloss": "front digger, arrow", "script": null, "see": ["Per 3"]}], "script_extra": null, "note": null, "quote": null}, {"id": 3, "parent": 2, "lang": "Persian", "refs": "BQT:1526; FFD:26", "words": [{"translit": "âkandan", "gloss": "to fill", "script": "آکندن ( آگندن )"}, {"translit": "kažâkand", "gloss": "silk-filled.", "script": "کژاکند ( قزاگند )", "see": ["Kaž"]}, {"translit": "afkandan", "gloss": "to throw, drop", "script": "افکندن ( افگندن ، ـ افکن )"}, {"translit": "parâkandan", "gloss": "to spread around", "script": "پراکندن ( پراگندن )"}, {"translit": "paykân", "gloss": "arrow", "script": "پیکان"}], "script_extra": null, "note": null, "quote": null}, {"id": 4, "parent": 1, "lang": "Old Persian", "refs": "KNT:178", "words": [{"translit": "ni-kan
data/extracted/batch/page-215.json {"root": {"name": "Gwhen 2", "lang": "Indo-European", "refs": "POK:492", "gloss": "to strike, hurt"}, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan", "refs": "POK:492; HRN:204; BQT:324; FFD:25", "words": [{"translit": "žata 2, jan, gan 2, gaz,gaš", "gloss": "to hit, harm, bite", "script": null}, {"translit": "â-ža-ta 2", "gloss": "harmed", "script": null}, {"translit": "vî-jainti", "gloss": "to sting, harm", "script": null, "see": ["Wi"]}, {"translit": "varathra-ğam", "gloss": "demon killer", "script": null, "see": ["Wer 3"]}], "script_extra": null, "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Persian", "refs": "HRN:204; BQT:324,1007,1812; FSF:26", "words": [{"translit": "zadan", "gloss": "to hit, strike", "script": "زدن"}, {"translit": "âzdan", "gloss": "to poke", "script": "آزدن"}, {"translit": "gazîdan", "gloss": "to sting", "script": "گزیدن ٢ ( گزیدن ، گشتن ٢ ، گزند )"}, {"translit": "Bahrâm", "gloss": "\"demon killer\", a male name", "script": "بهرام"}], "script_extra": "آژدن ، آژندن ، آژیدن ، آجدن ، آجیدن", "note": null, "quote": {"text": "به داغی جگرشان کنی آژده - که بخشایش آرد بر ایشان دده", "poet": "Ferdowsî"}}, {"id": 3, "parent": 0, "lang": "Old Persian", "refs": "KNT:184,185", "words": [{"translit": "jan", "gloss": "to strike", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 4, "parent": 3, "lang": "Old Persian", "refs": "HRN:231", "words": [{"translit": "ni-jan", "gloss": "to strike down, to put (somebody) down",
```


## [2026-09-06T22:32:51.382Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"erfreut'\\|'erfreut\" BRT.txt | head -20\necho \"=== grep sy.ta ===\"\ngrep -n -E \"s[yv][äa][lti][aео]-\" BRT.txt | head -20\necho \"=== grep 'Behagen, Freude' ===\"\ngrep -n \"sSiti\\|säiti\\|s3iti\\|saiti-\" BRT.txt | head -20"
}
```


### [2026-09-06T22:32:51.456Z] TOOL RESULT

```
18341:•  j.  friO'a-  Adj.  (fem.  -äa-)  i)  'erfreut, froh,  sich  freuend  an'  (Gen,):  -"ham (näml.  da^am)  gSusca  väsirahe:a  Yt.  13. 100.  2)  'geliebt,  lieb,  beliebt':  fryS '■'äo/ai/i.zaniJY.3j.$4;  Yt.(?.43,  V.iff.40; —frya  '%a  (NS(.)paiti.san/aYt.lS-$6;  — iU  "Sja  (NPf.)  JiaiHsantä  buyata  (sd.)  Yt. 13. 147;  —  'äd«  haitim  fri%S.larqm  (sd.) H.  2. 14;  —  '%a  (VSf)  spmta  ärmaite  V. 2.  10;  —  Uta  tl  . .  afrmämi  .  .  'äfl(ISf.) dahma  a/riii  V.  22,  5,
=== grep sy.ta ===
=== grep 'Behagen, Freude' ===
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
3663:—  5rJ5r?»i  (sd.)  .  .  Aapla  tar^a  'kahe V.75,4s;  —  yat  .  .  mazdayainS  'kS  avt hl  hapia  sania  frajasäiti  .  .  aiwyarahänS {sA^  paUis  he  ma^yäi  bBjyaman!!  VA-iS;
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
4190:•  '].  a-ohvä-,  g.  a-hvä-"  f.  i)  'Antrieb des  Willens,  Schaffensdrang,  Lebenskraft' : pairika  yä  duzyäirya  vlspahe  atiksui  .  . ' faröit pairi'in^misA.)  anhvqm  avaAisiiyät\ (sd.)  Yt.Ä54;  —  ava  m!  3zis  .  .  par5it\ fairrbnpm  (sd.)  arihvqm  ava.d}nnqn  sada- 1 yäfi  (sd.)  V.  i5. 19.  2)  'Antrieb  derl Seele,  innerlicher  — ,  Gemütsdrang,  Ge-j müt'"':  kal..*manS  asti  vT/aymii'tfm{s±) anhvqm  vjmar3zist?m  (sd.)  VL  /.  2 ;  —  ' virtzvatca  (sd.)  mat^  vansvatica  attuAa  j 'W.  62,10;  —  ye  kvam  ankvam  yaozdaite\ humatsilia  .  .  V.  ^.2i^>;  si  *PÜZ.,  lO.  19  I PüZ.;  —  dusx'arpnä  . .  asH5  asti  auuhaya  \ (LS.)  ".  .  ist  unfroh  in  seinem  Gemüt"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"  Yt  /o.  9;  —  fora  vi  räki  am?sä spmtn  yasmmcä  rahmtmcä  firä  mana»hä ..  vaiaahä  ..  syat>^anä  ..  dw^iy«  (IS.) » Y.7/.18.
5158:—  °vhsca  rafttSsca  Yt.^.  1;  —  jasäiti  tS 'vaahaica  ra/iianhai^a  . .  sraoSd  Yt  /.  9;
5971:mit  ä  dnwS,  4  a;  yezi  näil  paitiiaraiti *%rl  vs  äsäiti  ayar»jiräjö  (sd.)  vä  vastryä£ N.  69;  ^2,  43,  <V?,  log'''.
8518:•  j.  'usant-  Adj.  (fem.  °saiti-),  PPA.:  s. vas-.
8520:•  j,  *usant-  Adj.  (fem.  °saiti-),  PPA.:  s. 'vah:
8996:•  j.  ka'Sa,  g.  ka'dä  Adv.,  an  der  Spitze des  Satzes;  i)  'wann?':  'da  yavä  kv5 ai^hat  yi  .  .  \.2(f.  9;  4^.  3,  4Ä  9,  10*, n;  —  '^'oa  nS  arsa  ..  apayif  .  .  '6a  nS fraourvassayäiti  Yt/o.  86; —  *oa  na  aoi uzyarät  tiitryS  .  ,  Ha  xä  ..  tacSnii  YtÄ 5;^°s<i  nS  avi  vyarät  Hsirys ..°aa  xä.. yzärqm  Yt.  AI  42;  —  'ua  hS  avi  iljasäi nmänS-paitis  'aa  säiti .  .  Yti/.  10;  —  'oa nff  aAmäi  asanhalid  .  .  pailijasätd  izä(a
10012:von  den  ASp.  besucht  ist"  G,  2.'hraigta':  ya  mqm  ams  jamayeiti  yo  ..\\, 8.  a)  Des.  'hin  cu  kommen,  hin  zu  ge-  ly.  zo.  Undeutlich:  jimsp^  F.  ly,  — langen  suchen':  mmB  ..aSai  *jih3l^^  aku-  jasäiti  YX.4-i*-  VSIK.  ja-jmvak-  sbes. mn  Ny.M.  2)nutLok,;  namn..aSa-        mita/rt  i)'wegkommen,weggehenvon-'
10090:Des.  '(zu  gewinnen,  zu  erlangen  suchen sva.  fUr  seinen  Zweck)  ausfindig  zu  machen suchen':  yeiica  vaccill  a!s3  nä  hanq> aaa^qm  (?)  *jijiiaauAa  pinsanuha  aOaia (sA,  3)  aisa  yä  kaine  hanqm  aäal^qm *ßjis/fiti  pinsäiti  "und  wenn  der  Mann sagt:  'such  eine  Alte ..  ausfindig  zu  machen, frag  sie!'  —  das  Mädchen  sucht  dann  .." V.,5.,3f.
11597:•  j.  Jasant-'^  Adj.  (fem.  'saitl-,  'säiti'), PPA. :  s.  gam-.
14348:Vyt.  5/;  — yS  tl  jasäiti  aimsamm  .  .  Vl 4-1;  2.iz',Vyt^,  18',  i9,32\35^3^,39> 41,  5',  52  i.St,  58.  [Y.  19.  58:  lies
15197:•  j-,  g.  pa9ä-  f.  'Pfad,  Weg':  ■■^?«  x'ä- sijt/lm  (sd.J  Ny.  /.  8;  —  '>ajS  s^äsmayj FrW.5. 1 ;  —  catanrü  ptr^rA  (sd.)  vi'iiira- ysis  avi  ''i:qm  katarasät  YL74;.44;  — äat  yasp  'iws  .  .  ''iqm  jasäiti  vq'kwafsö "wenn  zu  dir  an  den  Weg  herankommt (sva.  dir  in  den  Weg  tritt)  ein  Strauch- dieb" Yt  13.  2o;  —  hat  ta  '"ha  frayqn pasvqm  vä  . .  "sollen  diese  Wege  be- gehen .,?"  V.  A'.  14;  15,  ig,  23; —  iiiritim taaa  aitä  'ha  vlvä'iayaritu  .  .  spätem  V, iV.  16;  17,  18;  — yi  ■  ■  kambist}mca  atte ''i:a  frayqn  pasvasca  .  .  V.j.is; — hu^a ,  .  aiaonqm  "'ia  (NS.?)  .  .  ku%a  Jrjatqm Yt4.4.  '  a)  AS.  mit  V.  d,}-  und  Inf. '(Jemandem)  den  Weg  freigeben,  es  (ihm) freistellen  zu  — ">:  hyat  aßyäi  dada  -^qm Tiis/ryiil  vä  äi/i(sd.)  "als  du  es  ihm  (dem Rind)  freistelltest  .  .  zu  .  ."  Y.  31.  9.
16991:K  zu  sehr  in  die  Länge  ziehend"  Yt.  10. 138; —  binstm  baräi  saota  väam  hii'tpmnd pasca  'ma  YLJ7.  61;  —  yö  'ma  *aivah- mat  naimat  hamsrisäiti  hqm  va  dansa- yeili  N.  pp;  —  yat  patri  °ma  hanjasante N.  6"2;  —  tim  yazäi . .  haomayff  {sdi.)  gava 'mana  Ny.  /.  16;  —  aao'ira^  .  .  'ma'  äytse yesti  sao^ra  haoaJar^sma  .  .  'ma  hala.- saehra  äyese  yesti  akmya  sadhre  imai  '""^ .  .  ana  'mana  imqm  zaoirqm  .  .  ha%a.- zao^rfm  imai  '«"^  Syae  ydti  Y.  2.  i;  —
17086:•  j.  bänav-  m.  'Lichtstrahl,  Strahl':  tifirim .  .  darat  vyävant^m  (sd.)  -«aJj'ff  (alslnstr.) *raoxSmbyS  anahitaHbyS  Yt*.  2;  —  as? srire . .  bänummti  säiti  vyävaiti  (sd.)  °nubyS (alslnstr.)  Yt/7.6;— df^ra/  hala  'nuwe^y^ aisma  frasaocayahi  {sA)  V.  Ä  75.
18360:—  "fyeAe  väaütahe  astdi/isd.)  Y.  IJ.2;  — buyama  ahurahe  .  .  'rya  (NPm.)  väziita astayS  Y.70.  4;  —  al  n5  asd  "ryiJ  (IS.)'' dazdysi  Aäkurmä  (sd.)  Y,  44- 1 ;  —  sraosS ■  •  'ryS  /ri'i>B  faiti.zanlöY.§-j.^\;  —  °rya (NSf.)  /ri>a  paitisanla  Yt.  (5.36;  —  tnä zT  ahmi  ninäne  . .  °rlm  vaocata  mqm  yim ahunm  mazdqm  yaha  mS  n5it  Stars  .  . 'ryS  atahat  "nicht  sollt  ihr  mich  in  dem Hause  freund  heissen  .  .,  wo  nicht  das Feuer  freund  ist"  P.  /?;  Vyt  5/,  F.  13  (wo °rint);  —  kdha  säiti  (sd.)  *pailisäma  °ryj (APn.)  paili  tanvi  Yt./?.  10.
18471:•  g.  naedä,  j.  naeJIa  neg.  Part,  'und  nicht, noch',  zum  Anschluss  eines  Satzes  oder Sauteils:  mihtym  ..yS ..mjainti  Aam^n%7 °'ha  manyete  (sd.)  jaynvh  naiha-Hm  ymqm sadayäti  (sd.)  Yt.  lo.  7 1 ;  —  ahmäi  nalmai uzjasäiti  mihrS yoAmäi  tta^manqm  mt'hrS.- druxl  '\a  mainyu  paiti.paite  [sA)  YtJO. ig.        a)  bes.  hinter  einer  andern  Negation:
19037:jAw.;  zu  1);  a)  das  Verbum  ist  indi-  n"^  . .  rta^a.äm  anyqm  . .  Y.  2.  ^y-  —  es kativisch:  n°  data  aAmt  «'  asts  (sd.)  ist  eine  Verbalform  entsprechend  der  des mpntS  .  .  V.  2. 3;  —  «•  As  ao^  pairi.-  vorhergehenden  positiven  Satzes  zu  er^ z'tfSiä»»' V,ip.3;  Yt5.93;  —  n°tatii^ar»nS\gä.ta.ta:  ap)rmäyu  aAmi  n'  p?r)näyu  (sA) pairi.abaom  Yt.7p.57;  —  "^"^  ^^l  n°  pairi.-\Yt  ig.43;  —  /W  äp^m  jainti..n'  avaha Jräsa  (sd.)  .,  *p3r>saAi  . .  Y.p.  25;  —  nava\  m3r>tS  V,5.  37;  38;  —  avi  ''ainyS  *'surun- Al  asti  ciha  .  .  n°  he  asti  yaozdühnm  V.  I  vaili  n'  ainys  N.  24;  P-i?;  —  nisriti 3-39',  —  "'  '?'"  ä^ravöpührim  (sd.) '^aStaAe  ästryeiti  n'  anisriti  N.ii; —  mosu nai^a  *daste  Aapu^nm  Y.70. 15; — na!cisca\tat  äs  n'  darrf>m  Yt5.  65;  —  sumnaoiti aitiAi  (Sp.  8  o.)  yasäiti  xyänäi  n'  snähai  ,*zaeta  upa.sraotara7tqm   n°  *upajraotärS
20623:' —  yat  aHjö  zaota  frayasäiti  °daht  *ayq N.  81;  —  al  töi  'diin  ahurä  tamanhs  asäicil dilmä(sä.)  Y.^^.  3.
```


## [2026-09-06T22:32:52.875Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD sad / asyan ===\"\ngrep -n -i \"^šād\\|šād \\|šādīh\\|āšyān\\|āšiyān\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"\ngrep -n -i \"šāt\\|šādīh\\|āšyān\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T22:32:52.934Z] TOOL RESULT

```
=== PHD sad / asyan ===
PHD.txt:221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
PHD.txt:578:šādurwān [P?wlw’n! | N ~] dais, platform; basin, pond, fountain.
PHD.txt:655:wistardan, wistar- [wstl-tn! | N gustardan] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bile. wišād [SLYTWNt', Р! | M wid, N gušād] open, wide, loose. wišādan, *wišāy- [SLYTWN-tn! < A У šrh; wPtn! | M шурап, (wys?h-), N gušādan, gušāy-) open, loose, free. wišād-dar [.SL Y TWNt! BBA] hospitable. wišād-dwārišnīh [zP??! dzb?lšnyh) going about ‘open’, i.e. without kustīg, or šabīg. | wišān- [w®n- | = P] shake down. *wišāy-, v. wišādan. wiškar [zo£hl | N bisgar(d)] hunting-ground, wilderness. wiškīdan, wiškin(n)- [wfkytn!, wškn-] divide, separate. ~išn: separation. wiskofag [wskwpk' | N biškēfa] blossom. wiškuftan, wiSk6f- [vvškup-tn! | J guškuftn, gwškwß-] blossom; hatch. wišūb-, —išn(-īģ), v. wišuftan. wišoūmand [w%wmnd] poisonous, venomous. wišūdag [wiwtk' | (M ghwdg)] abortion, daevic creature. wišūdan [wswtn'] bear daevic offspring. wišuftan, wišūb- (zfwp-tn! | M wiwb-, N *gusuftan] disturb, destroy. ~isn: destruction. ~1&п16 : destructible. *wixSay- [whsd-} forgive, forbear. ~iSn(ih): forbearance. ~išnīg : forbearing. lwiyaban [20(у) р?п! | Р шуп, N bīābān] desert. *wiyābān [wyd’p’n'] astray, wandering; deluded. ~ih: delusion, deception. wiyaban|garih [wyd"Pnklyh] deception. ~ig [-vk'] wandering, itinerant. wiyāftan, *wiyüb- [wd ptn! | M wy’b-] open (the mouth). wiyan [wyd?n! | M wy’n, N giyān] tent. wiyiz- [wydwe-] loosen, undo. *wiyufs- [wdwps-] make merry. ~išn: merry-making. ~iìšnīg : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-ytn'] tremble, quake. -išn: quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption.
PHD.txt:2509:joy farroxih, šādīh, urwahm(an)ih.
PHD.txt:2548:lair āšyān.
PHD.txt:2908:nest āšyān(ag).
PHD.txt:4568:šādurwān
=== NYB ===
1420:dvaristan [dwb'lstn'], dvaritan [dwb'lytn'] to run, to rush, of enemies and demoniac beings 2518 ete. passim; — andar ~. to rush, to come dashing (6 into the presence of) 7526; to make an onslaught, of Ahri- man and the demons at the beginning of the world 933.13, 9519, 10318; to make an assault upon (6) 1142; — apāc ~ to run back 1024; apar ~ to coil upwards (up a tree) 4012; — bē ~ to dash off 422, 10211.14.20; — frāc ~ to rush forth 25%; to spring forth (hac from) 9674. 9819. — Av. (765) dvar- ; Paz. duärestan, dvärestan. dvarišn [dwb'lin'] the act of running; as pred.: has to run, or is running 6811-12, dvārišnēh det. v. n. = the preceding w.: višāt- ~ the act of running about with loose, open clothes 69%, v. višat. dväzdah [dw’cdh; figure] twelve; han 4 12 axtar, 12 axtarān etc., v. axtar; dväz- dahān [dw’cdh’n'] the Zodiac 57. [12-n!] Ti: i dvàzdahom [dwb’cdhwm; 12-wm] the twelfth 8216, 844, E
1424:who is the messenger from this being [the Creator just mentioned] is good 5711; etc. passim; — anticipates a clause with kū ‘that’ 521.7132, 5320; ~ ku the fact is that 52"; a rel. clause: ~ +-t... pursit 7614; ~ ce that which 11214; — forms a rel. attribute: ~ i vas kayak u karap 5525; — forms possessives of the pers. pronouns: ~ % man zan my wife 3215; ~ i tō pus thy son 5213-15; ~ 4 tē separated by other parts of the sentence from its headw. 60°; — pat ~ dāštan 5012, v. dāštan; pat ~ šātēhē for joy over this 412°; pat ~ ku... adak-ic although ... yet 5525-26; ~~ rād for that reason 795 ete.; — cigon ~ i den göbet as the pertinent passage of the Scripture says 5323 etc.; čvak — i paitäk ku one (event) is that which is revealed, namely that 385-17, — 2 HWHw-yt! (ideogr. for the 2nd p. pl. of h- ‘to be’) wrongly for ēt: pat ~ dästan 25°. — 3. ē: ēvak ~ (i) paitäk 36% and passim 41-54; ~ rād ce because 9422. — Av. (12 sqq.) aéta-, OP aita-; MPrth ‘yd; MPrs ?yd. The form é in BP is confirmed by the wrong ideogr. HWHw-yt', but it is note- worthy that this pron., wherever it is phonetically written in BP, has the form é (also in FrP 25). In Paz. there is no trace of & (ed), since the only form occurring there is ē with the pl. ēšgn, which is also used as the pl. of õi, ētšān having totally disappeared; NP has only 6, pl. ēšān. This esqn can neither be derived from ët nor from öisän; it must reflect the Olr. gen. pl. *atšām (Av. aēšam) of *ayam (Av. ayem, aēm) whence in Milr "aš enlarged with the Milr pl. ending -än. The most probable expla- nation of BP ē is, therefore, that it is not a mutilation of é& but the gen. sg. of *ayam: ahya. This being so, it would seem to be most advisable simply to give č as the normal equivalent of HN’, which would best explain the widely spread use of HN’ as the ideogr. for homonyms, v. below.
2381:Mahlāh/Mahlāi [m’hl’s 9522, m’hl’y 96°] and Mahliyānāh [m’hlyd’n’h 95”. 965]; Malhà and Malhiyánài [mlh’ — mlhy?n?y] 951? gl.; Mihréh and Mihriyānēh [mtr'yh — mtr'yd’nyh] 634; Misēh [msyh — no fem.] 471: the first human couple, which arose from the sperm which Gäyömart, the Primeval Man, left on the soil when he was killed by Ahriman. — A great variety of forms: A. 1. Mahlé — Mah- liyānē [mhlyd — mhly’nyd] BdA p. 101°; Arab mhl’ — mhlynh (Mas‘üdi, Tanbih 93); — 2. with metathesis of -hl- > th-: *Malhēh — *Malhānā [mlhyh — mlh’n’] DD ch. 36%; Arab mlhy — mih’ny (Birüni, Chron. 99); of this type is prob- ably also Mari - Māryānah Tab. I. 147;— 3. with -$- instead of -Al-, -Ih-, and lengthening of the preceding a: Mašik — Māšyānē [m?$yk — m'šy'nyd] BdA p. 101!5 sq., *Māšīk - *Māšyānīk ibd. p. 1054; Tab. also m’®#. — B. Mihréh - Mihriyäneh, BdJ 33° Mihr [mtr'] - Mihriyän [mtr'y’n] (in other places Maše — Māšēnē): 1. with -s- for -hr-: Misäi — Mišiyānē [mšy — mšyd'ny] BdA y. 10514-15, Miša ibd. 1059. 1072; mšyh — máyd'wy DD ch. 69. 76 = Cod. K 35
3622:Sat [8°t'] glad, happy 2'%. 312, 255. — Av. (1716) šyāta-, šāta-; OP Siyäta- ‘peaceful, happy’, štyāti- ‘peace, happiness’; Ps. :ty; MPrthPrs $’d; Paz. säd; NP sad.
4204:Visp-šāt [š?t'] -Xösröi the name of a town 1142, — “All-glad is Khosroi''; v. šāt.
4219:višātan [wš'tn'; SLYTN-tn'] višay- or vi$-, to open, to let loose, to release: tô hàn i har 2 brätar i bastak viš(āy)ē [ŠLYTN- d, with final -d for -y as often occurs in the inscriptions after an ideogr.] thou wilt release thy two captive brothers 913; pt. visät loose, running without its rider, of horses 228; v. also the next w. — vi + Av. (1800) häy-; MPrth pt. wyš*d, pres. wyš*h-, pt. also gws’d, Ghilain 88; FrP 21 pres. in most MSS wšyt' wš(y)m, but Codd. U, U, wš*dt' wš*dm = visdyet, visayem ; Paz. kušādan kusäend (but subst. vašādai < visätakeh ‘open space’); NP gušādan gušāy-.
4220:višāt-dvārišnēh [wš't' dwb'linyh] the act of running “loose”, that is: with only the sacred garment (sudreh, in Phl Vd. šapīk) on, but without the sacred thread (kusti) 6912. V. Bharucha in Skr Mx, n. 8, and Modi, Ceremonies 181—190.
5386:Syäta, šāta: Sat
7021:āšyānah: *āyiyān
7185:gušadan, gušāy-: višātan
7433:šād: šāt
```


## [2026-09-06T22:33:02.010Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"āyiyān\\|āšiyān\\|\\*āšiyān\\|ašiyan\" NYB_vol2_glossary.txt | head\necho \"=== NYB grep asyan entry ===\"\ngrep -n -i \"syan\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T22:33:02.069Z] TOOL RESULT

```
329:aivān(ak): read āyiyān(ak).
773:Aiviyàn Ptwbyw'n'] = Āspiyān (g. v.) 11627. — Paz. Á0wyànq (Aog.). As to the spelling -yw?- for -4yā- cf s. v. āyiyān.
845:*āyiyān [’dyw’n'], *āyiyānak [Pdyw'nk'] a bird’s nest 409-16-25, — Reading hypo- thetical; I identify the w. with MPrth ’hy’ng = ähiyänag ‘nest’ (A-H III) < "a0iyan-, borrowed in SW and subjected there to the usual alternation -h- : -y-. The genuine SW form is found in NP 4é- yanah < "čdOyčna-, with -0y- in contact- ual position > -sy-. As to the spelling -yw- for -iy- cf apiyuat, giyäk, niyandar.
7021:āšyānah: *āyiyān
=== NYB grep asyan entry ===
1538:Frangräsiyäk [plngl”syd*k], Frangräsiyäp [plngl()syd’p]n. pr. 462°. 9923-25. Slightly transformed transliteration of Av. (986) Frayrasyan, nom. -ase < *-asyd; v. also Fräsiyäk.
2131:jāyišn [y?dšn'], 70!? jahišn [yhšn'] For- tune, luck, dispensation 2?!. 145; ~ u zaman <i> brihenišn rād 14'?, v. zaman; murvāk ~ i névak augury (and) good Fortune (i.e., good Fortune revealed through augury) 18!; pat névak ~ <u> yazdän hayyārēh with good fortune and the help of the gods 121-4; 121°; pat ~ hayyārēh i pat martömän xrat veh For- tune (giving aid to =) favouring men, wisdom is the best thing [she gives] 7012-13, Skr. v. siddheh sahāyatāyai ma- nusyanam buddhih uttamā; cf ke [for ka] ~ hayyär pat martömän cis + xrat veh when Fortune (is a helper to =) favours men, wisdom is the best of things PT 675-5, with the explanation cé hakar par- kast xvāstak be šavēt aivāp cahārpād be mirét xrat bē mānēt for if wealth dwindles and is lost or animals die wisdom remains; pātixšāi han névaktar i... xrat u dānišn nēvak api-$ ~ hayyäreh apāk that ruler
2161:kai [kd] king, sovereign, the title of the ancient kings of Eastern Iran: —-Kavät, the founder of the. dynasty; ~-X6sr61, ~-Luhrasp, ~-Vistasp, cf Käyös; pl.cas. obl. kayān [kd’n'] 2727, zuarrah i —-ān, ~-dn xLarrah, v. xuarrah; Artaxser is addressed as ~ before becoming king 618; — the seven assistants of Saosyant who perform the eschatological actions are called ~ 64; also Krišāsp 997°; cf also s. v. Xosrči. — Av. (442 sg.) kavi-; MPrth kw, pl. cas. obl. q’w’n ‘giant’; Prs on coins kd, kdy = FrP 12, with the explanation mas ‘great’; Paz. ka; NP kai ‘great king’ and borrowed from the NW language kav ‘valiant, grand, of fine figure’.
3463:10610.14. 11017. — Av. (1551 sq.) saosyant-, |
5145:frabdö.dräjah: fravd fraca, fraš: frāc fradašafšū: Frādatafš Fradat-xUaronah-: Fradat-xUarrah fračšta: frayist Franrasyan: Frangrasi- yak fra-pad-: frabd, fravd ä-fras-: äfräs a-fray-: äfritan Frašaoštra-: Frašostr Fraš.ham.varota: fraša- vart frašna-: frašn frašč.koroti-: fraš-kart fratoma: fratom fra-vaka: Fravak fravaši-: fravahr, fravaš fravašinam: fravartür frayah: Fray-zist frazanti-: frazand Frazdanu-: Frazdàn
5180:Haosyanha-: HöSang
```


## [2026-09-06T22:33:02.861Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /1716/{print NR\": \"substr($0,1,120)}' BRT.txt | head -20"
}
```


### [2026-09-06T22:33:04.529Z] TOOL RESULT

```
933: '■  V.  13. 33-
Komp.  mit  AS.  im  1.  Glied.  ~  Fa.:  iiinün varz,  er!.!  /  k-mmd  ai  ö  bun.  —  O  So  K
```


## [2026-09-06T22:33:23.016Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 894 895 896 897 898; do echo \"###### leaf(0-based) $n ######\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | head -c 1500; echo; done"
}
```


### [2026-09-06T22:33:24.798Z] TOOL RESULT

```
###### leaf(0-based) 894 ######
�  surunuyS  nd  .. yasnahe  xlnuya  nS  . .  yasnahe  YL 10. 3a; —  surunaoiti  saota  upa.sraotaranqm  N. 21.  Ausser  Zusammenhang:  smnaoiti, sravat  F. /2"*.  II)  Kaus,  ('etwas  zu Gehör  bringen'  sva.)  i)  'verkünden, predigen':  tnrüiti  yS  v3  xraffui  xsms- kakyS  a.mananhä  (sd.)  jr?/  vjHdyai (sd.)  yd^ä  r  srSvayaema  Y.  49.  6 ;  — s.  noch  In£  2)  'aufsagen,  rezitiren'; Med.  in  pass.  Sinn;  als  PPfP.  dazu  dient sruta-:  srävaylH! staola yesnya  P. /J;  —  yä ahmät  staoia  yasnya  srävaymi  ahuiam'a vairfm  srävayeni  astmca  vahist»m  ^husra- vSm  (sd. )  Ny.4. 8 ;  —  yeti . .  xsvas  vaAiärm {sA)*srävayätiü.^o; — yasca  ml..bayqm ahunake  vairyehe .  ./rä  vä  drsn/ayö  sräva- yäi  fra  va  srSvayS  {Sp.  1642  o.)  yatäite Y.lff.6;  —  srävayamnät  paiti  ahunät vairyat  A.  4.  j ;  —  Hä  ml  6aya  afatnahe vairyehe ..  anapyB^a  {&A)  anapisüta  srä- vayamna  Y.ig.y,  y,^yaozdä^r?m  srä- vaySil  "du  sollst  die  Purifikation  (auf- sagen sva.)  durch  Aufsagen  (der  dafilr vorgeschriebenen  Formeln)  vollziehen"  V, u.  2  '^.  insbes.  a)  vom  Au&agen  der Gä%ä%:  ahnyästa  matdayasna  gä^ä  srä- vaya/ nSii  anaiwyasta  (sA.)  N-A^;  — yBi .  .  matüyanqm  (sd.)  parä  s^arHöit  *gä^ä nöii  *sravayeinti  N.  25;  26",  *J7 '",  V./Äj;
dby  Google
1641  srav-  mit  atwt  -
—  *anSsl?r>tö . .  ava  yh  *anyä  (jüia\.gähä) srävaysit  ^.46,  30;  4S;  —  ya  gä^ä *af
###### leaf(0-based) 895 ######
 vä vpa.srunvanH  *yat  vä  *yasn?m  ''yazamnahe "die  ihn  (näml,  den  Zaotar)  hören,  wenn er  mit  mittelstarker  Stimme  (den  AAV.) oder  aber  den  Y.  betet"  N. b)  von  den  Gä%äs:  sraosö  .  .  yö paoiryS  g^ä  frasrävayai  yä  panca  Y. 57.  S;  —  zaotar^ (id.)  kairim  ..*gä%asca frasrävayaiti  N,  72 ; "  Vd.  12 ;  —  käia  zaota (sd.)  gäiiä  frasrävayaiti  N.  j_j,  c)  ohne Objekt  sva.  'die  vorgeschriebenen  Gebete Lufsagen':  */rasravay5'^'>  ratufris  nsil asrävayS  N. /04;  Vd,  2/(?).  2)  'etwas
zusagen,  bewilligen':  frasrävayS  ava dahra  yim  dim  vaiaät  *7vislainia  (sd.) ^vindämm  N.16,
mit  vX  1)  'vernehmen,  hören',  mit  Gen. der  Person:  yat  hl  nasdÜtJ  dahmö  vi.- srunvaiti  yaval  vä  aim  alm  havalibya •Miya  "so  dass  ihn  der  nächstbefindliche D.  oder  irgend  ein  beliebiger  mit  seinen Ohren  hören  kann"  N.  27.  2)  Pass, 'zu  Gehör  gebracht,  bekannt  werden durch  — '  {paiti  mit  Lok.):  zard^ultra  .  . yahmi  paiti  vtspim.maäinm  *ahmjravs id.)  vxsruyata  Yty.  91.
ai,  iraval,  irfla,  irölu,  sj-tiiti*l'i,  iäh-üfalt,  irü- yitt,  h-ätiäyali,  iravi,  hiiruma,  irutäk;  sbal. sunant  'sie  hören';  Dp,  saräyad  'er  singt,  vgL hautvad  'et  hört'  (Sp,  559  u.  No.).  —  Pü,: aigösilan,  (fiiis  Kaus.):  iräyilan;  a.  noch  No, 2-S.  7.  9f-i  1*^-.  18  f-.  23-25-    —    ■'  S.  dazu
dby  Google
1043  srava-  —
J  Tjt  lu  a.  Du  >r.  Praese
###### leaf(0-based) 896 ######
  duye vatfAauca  miide  vatikäula  'vahe^'^  A. /.  1 1.  [Yl  13.  gi :  lies  aÄM.jraoff.]
I  KompE-i  Ableit  (».  srävahyfif!^  —  Znm  V. srttV;  —  Pü.:  trav,  Sü.;  uküh,  (lu  Y.  34)% saratBaü;  t.  noch  No.  i  f.,  5-8.  —  >)  Pü.:  /«
I      an  stäyiSn,  Sü.:  vadanfna.  —  »)  PO.  (für  y"  r*
■     sr'') :   kc  rS  träyind,    Sü. :  yi  ditdam  samädi-
ianä.  —    3)   Die  Dreiheit  '      '      "
und  IUI-  bildet,  wie  yasna-,  ■Doiah-  nnd  iyait. \anar  in  Y.  34.  I ,  nur  eine  Variante  der bekannten  Dieiheit  manah-,  va!ak-,  fyaiAana: irat/aA-  vertritt  va^aA-.  —  4)  Nach  der  n-Dekl. —  S)  Pü.!  aarnb  statt  dd  ra  b  =  irav.  — 6)  Hds.  irävaoitm  und  irauaalum  (T);  Pfi. : srav,  erL ;  afasläi ;  s.  No.  7.  —  7)  PS. :  rrav, erl.:  apasläk  u  tand;  5.  No.  6,  —  8)  Pö.: nänükih,  Sü. :  ktrti^.  — ■  9)  Them.
j.  sroiiS  V.  tg.  42 :  s.  onter  irä-.
I-  •
Ä  Vd,  .
•  j.  srask-  V.  'triefen'.  Praes.  2  srasca-, 30  (Kaus.)  iraseaya-.
i)  'triefen,  abtriefen  von  -'  (Gen.  statt AbI.),vonfcttenSpeisen:a»^«iF(Sp.357f.) srasfintls  :^an^ä'V.3.2<}.  aa)  trief- regnen sva.  triefenden  Regen  fallen  lassen, veranlassen',  persänl.:  tnlsti  zl  ml  kim  .. var?ntal{si.)^a  sna^intal'a  srasctttta^a (3PPM.,  näml.  arsäna)  *fyankuntaica  Yt 5.  lao;  —  haca  xsafnB  varmtya  .  ,  sra- scirttyä  "in  einer  Nacht,  die  (sva.  in  der es
###### leaf(0-based) 897 ######
a-  Adj.  (fem.  T3-)  i)  "schön anzu  sehen,  schön' ;  a)  vom  schönen Äussern  der  Menschen  und  Götter:  virahe kihrpa  ,.  'rahe  YX.14.2T,  17;  —  kainlnö kihrpa  'rayä  Yt.  5.  64,  H.  2.  9;  —  'rB ahi  tara^uilra  huktntB  ahi  . .  kvascvB darrj^.bäiäus  Yi.i-].%z;  —  kikrpasla  ,. 'ra  amisanqm  sppntanqm  Yl  y .  8 1 ;  F.  72 ;
—  'r?m  .  .  bavilki  yaha  .  .  Az.  3;  — dämqn .. pouruca  'raca  Yt7ß.  loj  —  Sat mqm  .  .  'rqm  Aaitrm  srtrSJarqm  . .  H. 2.14;  —  'räsca  Q)  vohu  tnanS  rätaca vanuAi  V.  ig.  1 9  (?) ;  —  usqm  'rqm  G.  5,  J ;
—  °ra  dityha  ahurahe  masdi  V.ig.  13';  30, *F.^e";  —  yima  'ra  (VS.)  V.  2. 3,  9,  »2; 3 ;  — yimäi  'rät  V,  2.  2 ;  —  AaomS  fräimis .  .  °rS  Y.57. 19;  —  oHÜ  vanuhi  'ra  Yt. y.  107;  — a«  •«  (VSf.)  Yt.  77. 6,  60,  61;
—  satavalsB ..'rS  Yt.1j.44;  Äg;  —  aiä -ra  (VSd.)  Y.  j5.  3 ;  —  vsiahe  kihrpa . .  -raht Yt.  74.  2;    —    dalnayai   'rayüi  Yt.  70,  64;
—  upa  tqm  'rqm  manao%rim  Yt.5.  la?;  — 'ra..daimäna  YL70.107;  —  ■'ra(NDm.) vä  aahm  bäzava  (sd.)  Yt.  5. 7.  b)  von Tieren:  aspahe  hhrpa  .  .  'rahe  YtÄ  18; Yt.  14.  7,  23,  25.         c)  sonst:  unaranam
'ranqm  V,  18.  63,  Yt  7<S.  6;  V.  ig.  18, Vyt  22;  —  'rasla  asB.iöi^räs^a  Yt.  8.  4a, V.7.  30;  —  °rä  baninava  Ytjo.  13;  — harayä  birizB  'rayä  Ytp.3,  77.24;  — ^annanuhaifi^sA^
###### leaf(0-based) 898 ######
ü-  wird  in  die  ö-DekL  überführt.  —  »)  Oder auch  der  beiden  Hände;  s.  Dbr.  V^S.  i, 143.  —  i)  NA.  h»t  dRn.  irvf,  srvf,  irnit;  s. aber  die  Var.  Vgl,  auch  srvT.itäy.  —  4)  D.  L inaie  [S  36S,  19),  die  them.  Form  gegenüber irvT.  —  5)  Pü. :  fehlt.
•  j.  srui-  Adj,  'hörend'.
KompA.,  E.  —  Zum  V.  irav —  ai.  'im/-,  imf.
—  5.  auch  zD  aimlim.
•  j.  sruta-"  Adj.  (fem.  •«-)  i)  'gehört*; a)  sva-  'dass  es  gehört  wird,  hörbar*  1  a/ijrs va  hl  dahmB  'tS  g-ä^S  da^aiti  *ratufril asruts  (sd.)  (arahtfril)  N.  25.  b)  sva. 'von  dem  man  hört,  bekannt,  berühmt': akurS  matdh  . .  Hö  atryene  ''vaijahe  . . yitnl!  xlaäB ..'IS  atryene  *valjaie  V.2.20; Y.p.  14;  —  'ta  F.  12.  j)  'zu  Gehör gebracht,  aufgesagt':  s.  srav-  Sp.  1641  o.
KompA.,  E.  —  PPfP.  tum  V.  trav.  —  ai. imtd-  Adj.,  mp.  srüt,  —  Fn.  (lu  1  a):  srüt, (iQ  I  b):  nämli,  {zu  3):  s.  Sp.  16*3,  No.  ig. 33,  35.  —  >)  Mit  H  V.  2.  30,  Y.  p.  14  und im  Komp.  nxit/rä  und  vT.
•  j.  srütatfaSri-  f.  EN.  der  Mutter  des Ux^atjrsta  (sd.)*':  katiyä  'f^ryS  a/acnyä YL/J.141.
*)  lodern  «ie  im  See  K^aaya  badend  von  dem dort  aufbewahrten  Samen  Zara%uitras  befruchtet wird;  s.  unter  xhidra-,  wo  Litt.
Eig.  'die  einen  berühmten  Vater  hat'<);  statt irula-f  nach  dem  Muster  von  tridaf-fAri-, JusTl  NB.  31 1.  —  «)  Im  Mp.  nifl
```


## [2026-09-06T22:33:31.024Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 928 929 930 931 932; do echo \"###### leaf $n ######\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | head -c 2500; echo; done"
}
```


### [2026-09-06T22:33:32.785Z] TOOL RESULT

```
###### leaf 928 ######
   der  Stelle   eine  Anspielung  auf  Wergeid;
•  j,  Saetö.frä^ana-  Adj.  (fem.  'nä-)  'das Geld,  Vermögen  mehrend';  aridvXm  saram ..■n.m\.65.^.
Pü.!  ji'äslai /räx'enJiär.
j.iao/tt  Vyt.iö:  lies  iyaa%aa;  s.  Sp.  1712  u. j.  iailayö:  s.  unter  silay:
•  p.  naiy   "Sakaurim    naiy   ^^"huvalam züra''  (sd.)  akunavaiu  Bh.  4. 1 3.
Vgl.  zu  zürah:  Jn.  JAOS.  24.  92  versichert, es  stehe  tatsächlich  iH'ui^ill:)m''  auf  dem Stein.
•  j.  sanman-  n.  'Wurf':  mit  dim  arstSis .  .  nsit  Uaos  .  .  ava.as'naoili  •maoyS  (DP. statt  IP.)  yahmäi  . .  "nicht  trifft  man  ihn mit  der  . ,  Lanze,  nicht  mit  des  . .  Pfeiles Würfen,  ihn,  dem  .  ."  Yt  10.  24.
Et.?  ■)  Wenn  richtig,  muss  nm  ans  ir.  dm  her- ^'o^geEangen  sein;  s.  i.a  läinman-.  — '}  Viett- los  Gdn,  3yt,  36.
•  j.  sam-  V.,  nur  mit  a  'einschlürfen, schlucken'.     Praes.  2  /ama-,
paoiryehe    *mt^Sxtaht    Jrf    *malsma.- samqn    asamst    bityeke    *xsvas  .  .   "beim
äay-  1706
ersten  falschen  Wort  soll  er  drei  Schluck Harn  schlucken  .  ,"  V.g.
Aus  ar.  »xsam'  oder  •:fjom-.  —  Vgl.  np.  äiä-
j.  maesma  samqn  P.  g:  lies  miutma.s'. •  '}.,  g.  äay-  V.  'wohnen'.    Praes.  1  say-i sy-''>,  xsay''>^,  4  saya-.    —    PPfP.  'Uta-, Inf.  •/(/*,  •iiliy  'xsdi^ne^.
i)  'sich  wo  (Lok.)  aufhalten,  wohnen, weilen':  a'hra  .,yahr3  matdä  varjd^mqm (sd.)  jiift/r  V.4O'.  16;  —  ^wävqi ..  hädi- möi  {sd.)  ../jiqs  Y.44.9;  —  ^rizaf  (sd.) pd^S  yaisS  mazdä  ..  *salin  Y..7J.  5; —  maihanyä  yähva  mi%rS.drvjS  *syeili (3PPA.)'>  "die  Behausungen  ,  .,  in  denen die  .  .  wohnen"  Yt.  70.  38;  *F,  5^';  — o^anvaitls  asahe  vfr?zS .  .  yaAii  irislanqm I  urvqnS  "säyante  Y.  t6.  7.  a)  'bei  Jemand (Akk.)  Wohnung  haben  sva.  vorhanden sein'(?):^'OT  j>ftV«(3PPA.)4'  daityS.i/ma(%A.) yasnasia   vahmasca   Yt.  ;4. 48.  3)  'auf
Jemands  Seite  stehen,  halten  zu  — .  es halten  mit  — ';  a)  mit  Instr.:  manyoHbyS fsd.)  .  .  yäis  (als  Subj.)  . .  gaobis  ^iyätUl ".  .  die  es  mit  dem  Rind  halten"  Y. i2. 3,  b)   mit  hah  und  Abi.:  tim   at
yasnanqm  paunatatä  yasamaldl  ysi  gfui hacä  syeMl  ".  .  der  Gebete  derer,  die  es mit  dem  Rind  halten"  Y.  jj.  a.  c)  mit ä  imd  Abi.:  dr?gvh  .  .  a/iyä  /yao%anäi/ akut  J  *syqs^^  mananhs  "der  Drug- genösse,  der  es  in  seinem  Tun  mit 
###### leaf 929 ######
imqmtqmaiwihalmwrya  »  \.  ia  ..  vupa  dämqn  paifi.vamai  »»So
(sd.)  saranamya  V.2. 10.  ^dus.cihrayä  Yt  79.94.
Ans  ar. Viit«-,  u-'Erweitening'  (Praes.  ao)  zu'  i--a_  \   ■        ■*         oit   u
ai.  iai-  V.  -schneiden'.    -    PQ.:  an  fn  JmTi   *   J-.   E-    äolSra-  n.    i)   im   jAw.   -Wohn-
lu/t  (s.  Dp.  luj/an)  Ja  türäiSmaaä  i  iorren.        platz,   Heimslätte':  >a*J/   'raAe   boxtSmn
.  j.  Sä-   ,)   Adj.  (auch  fem.)  'froh,  sich  /Ü-Zrl«  Yt  Ä  i ;  ~  <W«Ä  -r^paitim..
behaglich  fühlend':  n^,V  ^r  r«  zä  /J  (NSf.)  -^'"'  '"*«"'«  «''^?"'  ^'^^  '^'  "  '"''''"^;
>J   darrra  akarsta  säm  "denn  nicht  -^^nqm  yü^anqm  'ranam  ..  masyän^m  Yt.
die  Erde  froh,  die  lang  ungepflügt  dalag"  1  '^^^'  "  /'  ""f     '"'l^^.^  ,  *^  '."'"^
V.J.  .4-  >)  f.  'Freude.  Behafen'  (n^  "^^^    V'"    ^^^UZ\  ^<*^*->=  .^'*"^'
Komp.).  [N.  wi:  lies  /a,y>^-]  ^f«f  •'*''  »«S;« (DS.) ",  W  ««A  -r^^^a
KompE.  —   Zum  V.  Syä-.  -  VgL  iäüla-.  -    (LS-)-  asanhatca  -rOatca,  Oia. .  'ra,  asasfa
Fa.:  Aa^ an  i  äiänTA.  ,TJs^a,    asavAqmca    'ranqmca.  a)    im
j.  iäimnö  H.  j^:    ».  anva /rahiimna-,    Sp.   gA\?.  'Landkreis,  Gau"';  *3  sl  d»min»m
1008.  ;'j»M  »3  •«/«  iiJ  dahyum  vä  ädät  duntä-
•  j,  SäJsta-  Adj.  'der  erfreulichste,  behag- '  (sd.)i5l..  Y.J/.  r8;  —  d»manaAyä  xsa^r?m lichste':  kva  paoirlm  atAhh  s>tnS  't^m  ^•rahyj  va  dahy^s  va  Y. j/.  16;  —  at (NSn.)  "wo  auf  dieser  Erde  ist  es  erstens  '  tsi^  drsgva  . .  ga  frdntdis  (sd.)  'rakyJ  vJ am  behaglichsten?"  V.j.i.  \dahySul vä  Y.4ÖI4.
KompE  —  Sapeil.  ta  sä-.  —  Aus  ar. ' k'iä',  i]istha- 1  KompA.,  E. ;  Ableit.  —  Zom  V.  Say:  —  aL (S  Sr),  lum  VtM%.*Xiäiati;  Bthl. IF./.''73.  —  ,  ii/lta-  n.  —  Pü.:  reiiutäi,  {lu  i):  trtnsskr. Pü.:  tu  /ralum  in  tamU  äiinlum,  erl.:  6u  ,  (sii!r)i),  Sü,  (überall):  deiai.  —  ')  Uathem., minük  i  samii  äsin'ih  hal  ci  vii.  1      an  ataiihalt'a  angeglichen.  —  ')  Sva.  im  jAw.
.  j.  säta-  Adj.,  PPfP.:  s.  iyä-.  j     ■«^"^'  ^^-  "•"  **■  "  ■»  ^^  "  '"^'y"-
•  j.  sätay-  £:  s.  unter  ^yitay-.  !•  j.'"äoi»r5'Hn-)'WohnpUtz,Heimstätte':
•  J;  I^^ .-"/■'  "''.*'''"  '".*""."'  ''''.^'  *"""-  i  ^'Ä'-:  -^>r^-  -  •>  Kein  »elbständige»  Wot., Sich  behaglrch':  ^fl^f
###### leaf 930 ######

'die    betten    um   dabei  zu  wohnen';    s.  dacu
Dbr.  AiS.  4iä>  419-
•  j.  siti  Inf.  'zu  wohnen'.
KompE.  —  Zum  V.  lay.  —  Vgl.  Siiay-. p.  'Um,  'iil;  1.  hay-. j.  iuqs  F.  750:  lies  Ivqt;  s. ^m/- mit  No. 6.
•  j.  satay-  f.  'Bewegen;  Sichbewegen', KompE.  —  Zum  V.  •ion-.  —  n.  eyutay-  f.  — Vgl  'atmisüili,  'iülöit  Inf.
•  j.  "sutasme"*  F.  5.
Pü.:  danmi.  —  ')  Voransgeht  imtini  (statt xsusl?m\  Das  lässt  auf  *xsiistasmt,  LS.  aus xsusla-iam-  f.  'aufgeweichlcr  Lehm'  schliessen.
•  j.  'sütöii'^  Inf.  'zu  gehen', mit  apa  'nach   hinten   weg  zu  gehen';
nasca  pascalta  *käu  nS  akmat  kaca  gataot isalta  frasütöit  ttsit  apalüiStt  '^rayqmana gämanqm  "und  dann  wird  der  Mann  nicht mehr  fähig  sein,  sich  von  diesem  Ort  nach vom  oder  hinten  zu  entfernen,  auch  nicht drei  Schritte"  P.:;^.
Syao^tia- A  17 10
mit  /rs  'nach   vom   weg   zu   gehen': 3.  eben.
Zum  V.  iaii-.  —  Vgl.  aifiiäiay:  —  Fü.:  ^är, /räc  lovOniA.  —  ■)  Man  erwarlete  aber  den Gen.  'liU;  Tgl.  haxidil  nnd  aä-  No.  1.
•  j.  äud-  m.  'Hunger*:  dva  yaska  ..yasca "hs  (NP.)  yai^a  tar/nS  V.  7,  70;  —  ay^m °%fm  tarsnimca  Ytig.g6;  69,  F.5;  — vanäi  Aaurväsca  aminläs^a  nva  'opm'a tarltumca  Yt  ig.  96 ;  p.  10.
al  ipidA-  f.  (vgl.  S  393);  mp.  (Pü.)»),  nbal. hil,  woss.  s!i.  —  1)  Them.  —  ')  S.  PiL  tu a/r&yani-  mit  No.  3.
j./tä  Vä  Süsa  Yt  /,  17:  S.  vnUt /raiüsan-.
j.  hutfm  F.  J:  lies  xhitlim.
•  j.  "ätuiti"'  (f.)  'Preisen,  Lobpreisung":
F-5-
Pü.:  släyiiH.    —    0  Kein  selbständige»  Wort
einem  Komp.  losgeschalt,  vgl  niitulay- ;  Bthl. IF.  //.   133.
).  /nooäna    Vyt,  4O:    lies    syaa%na;     s.    Sp. 1712  u.
•  j,  Snav-  n.  'Knie':  s.  unter  Inav. KompE.
•  j.  äyaoftna-'*,  '{hana-"',  j.,  g.  -^ana-"  n. 'facinus;Tun,Handehi,Wirken;  Tat,  Hand- lung, Werk;  Tätigkeil;  Wirksamkeit';  a)  im gAw.:  at  yJ  varslä  ytlcä  pairl  ät/  (Sp, 862  u.)  °ianä  V.  ßo.  10;  —  Ayaf  f  .  . vsnzimälä  yä  hätqm  ''^arian^m  laMilä Ryät  ubsibyä  ahubyä  Y.  ^5. 3 ;  —  ^ya%ä *5il  ihä  vaniaitl .  .  ratül  '^anä  rmUtä (sd.)  Y.33.1;  —  *vJdll»mnäi {'iA.)  liäci^.. '^anäii'  vaAiilfm  Y.  5/.  i;  —  vSstryS '%anäii  gr?ivB  Y.57.  5;  —  '%anBi  sppnttm ahur?m\.46.^;  —  aäm  •%anäi/d>6qxaitr (sd.)  ärm
###### leaf 931 ######
ists  triiväsca  .  *varsta  aisqm  °'kantm\ca\  aahölrisbm *%anäcä  vaola  '^.34. 15  (Sp.  375  u,);  —  N.  2g;  —  *ar>dus  hl  •%a/t»m  N.  42;  — gavSi  ärBil*ä  *sSndä  (sd.)  a^Ji/  '"kanäisca  kvar>xsalt3m  .  .yazamaide . .  vacaca  '^naca ar^häiScä  yS  Is  sSnghs  .  .  Y.57.14;  —  zaohräliyasca  Ny.i.iö;  —  ai/iAä  dainayä kyat  .  .  mazds  .  .  gai^as^S  ta^S  dalnas-  j  mqs  vaca  da^Snake  mit  '^när/  apayantafu (^Ä)ca  ..  ''Sonata  ssngkqsca  Y. 31. 11;  —  ■  (S*p.  71  m.)  Y.p.  31;  —  mit  näherer  Bc- nSii  na  manä  .  .  sSngha  .  .  xraiavö  .  .  Stimmung  durch  ein  Adj.:  hrarlianqm varanä  (sd.)  .  .  uxha  . .  "SanJ  .  .  dainä  '^nanqm  vanzüi  pairi  .  .  dulvarstanqm urvqnS  kacainlEY.4S-3.         a)  insbes.  im  ■ 'äMiwa»!    var?zai    Vr.  /J.  i;    V,  JÄ  17';
Gegensatz  zu  Denken  und  Sprechen  (od. ähnl.):  yS  hsi  mainyU  '^anaisca  unahs (sd.)  Y.3I.21;  —  Avd  ..  ahm  vacar^ka •"^ana/a    hapn   Y. 31.33;  36.  i,;    —    iqm
vupaca  hvarsta  '%na  yazamaide varitaca  varisyamnaca  Y.  57.  4;  V.J.  42; —  par»ts.tanunam  '"inanam  usvaritayS V.  7. 52  PüZ.;  —  ara^wyaca  '^na  Y.3.40;
daBnqtn   .  .   armatlis    uxMis    '%ana    >m\  —    '%na  ya    narö.vaipaya    V.  i.i
daidyat  (Sp.  724  u.)    Y.44-  10;  $3.  i;   — ' 'ä«j  ya  nasuspaya  V.  /.  12;  —  '%iia  ya
hyat  da  °Sb«J  (sd.)  mlzdavqn  yaca    ux'üä  nasuspacya  V. /.  16;    —    narsni    °ina   A.
Y.  415.5;    —    ^aif  '%anäi/  Ä(«'aj(sd.):r5  |_j.  13;  —  daina    mäzdayasni/  .  .  *spayati
afaÄya   nqsvä  pa%!!  Y.57.13;  — ySi  v}\anapfrri)m  '^n^m  V.J.  41;  39,  Vd.  2;  —
syaoianail  sarvnß  (sd.)  .  .  *hiBva  uxZäis  ys  nairikaya  ci^ravaityä  ..  paurvö.vasfut
vatthiuS  manarahs  Y.57.  3;   —  vahist?m\*%na    tanüm    iri^yät    V.  16.  n;  *\yt  26,
iitzia  ux&ai/.,^änß  ..  armatui^  sasßidya'^40;    —    s.  noch   unter  a.         a)   insbes.
*%ian3  v»rfgyat(&A.)Y.4y.3; — y}  däi  manS  ,\m  Gegensatz    zu   Denken  {manak-)    und
vahyB . .  aiyas{%d.)ca  hvS  da&tqm  "^anair'ä  I  Sprechen   {vacah-);    s.   zum  Wortlaut  der
valatihaca    Y.48.^;   —   /^i'il  /w/r  B*33j/;Stcllen  Sp.  1139a  und  1341  0.:  rfuüwaif
*^ana  dama  ahm  spsnvat  (sd.)  Y.  5  j.  2 1 ;  1  sanm    mruyi  .  .  vT  manSbU  .  .  vaciiis  . .
— ya  *%anäyä  vaianha yä yasna  amfnta-   '
###### leaf 932 ######
'■  V.  13. 33-
Komp.  mit  AS.  im  1.  Glied.  ~  Fa.:  iiinün varz,  er!.!  /  k-mmd  ai  ö  bun.  —  O  So  K  1, L4,  Pt2;  NA.  "S«üPflr'.  —  »)  Vgl.  N./Oj.— 3>  Die  Worte  viT?tyäl  sy'  sind  Glosse  zu  ly'.
•  j.  äyaolhiö.tät-  f.  \lyao%TiaXwxD.,  d.  i.) 'die  mit  dem  Wort  iyao^ananam  be- ginnende Stelle,  die  Stelle  'syao%ananqm' des  ^/;««(j;'a»»yagebets':  *'täitya^^  (LS.) *hävanaHbya  paitt.jatiAsit  "bei  der  Stelle fy'  soll  er  sich  zum  Mörser  begeben" N.  1?/;  —  /rä  ml  spanyä  manivä  vavaca (sd.)  iiTspqm  asaonö  stlm  .  .  'tättya  syao- 'i^nanqm  aahiuS  mazääi  ". .  mit  der  Stelle sy,  (nämlich):   ^iy.  a.  m.'"  Y.ig.g.
VgL  us/a/äl-  2.  —  Pü. :  /a  syai>%anaHqni  ra- -jiisniA,  pa  tanisn  rauiiiniA.  —  ■)  Hds.  '%an3.'.
•  g.  Syaoman-  n.  Tat,  Werk':  drüjasca fairimatsisiä  -mam  (NP.)  aipj  daibitänä (Sp.  761  0.)  Y.y2.  3.
Zum  V.  lyo"-  —  Vgl.  !yao%na-.  —  Pü.:  ri- jecnel  man,  Sü. :  fracärayali  mayi.  Man  trennte ofTenbar  lyao  mqm[
•  g.  lyant-  Adj.,  PPA.:  s,  siay-.
•  p.  äiyav-,  g,  Syav-,  j.,  g.  äav-'>  V. 'sich  in  Bewegung  setzen'.  Praes.  i  syav-, sav- :  A»-'*,  2  siyava-,  14  iüsa-'*,  30  (Kaus.) /ävaya-;  j-Aor.  i   /ae/-;  Per  f.  i   suiu-*\
—  PPfP.  •su/a-.  Int  'sBi/i,  's'BtBit,  syao-
1)  'sich  in  Gang,  Marsch  setzen,  pro- Acisci',  miliüLiisch;  i)  ohne  Zielangabe: pasävn^  dadarlis  asiyav^  ya%ä  arminam parärast^  .  .  Bh.  2.  7;  lo,  6,  14,  _J.  3,  11; — pasäzJ'  vistäspa^  *äyasatä  avam  iäram aHyav<^  "da  zog  V.  jenes  Heer  an  sich, er  setzte  sich  in  Marsch"  Bh.j.  1;  — Pasav^  viväna*  hadä  Itärä  nipadiy  (sd.) tyaiy    aHyavJ*  Bh.^.  11.  a)    mit  Inf.:
kauv  kära^  asiyavJ'  .  .  hamaranam  ear- tanaiy    Bh.  ^.  9.  2)    mit    Zielangabe
durch  a)  AkL  'nach  .  .':  pasav^  ka'bü- jiyaf'  mudrSyam  asiyav<^  ya%ä  . .  mu- dräyam   asiyavc^  .  .  Bh.  I.  10;  _y.  6',  5.1;
—  adam  babirum  asiyavam  Bh. /.  19,  18, 2. 1 ;  1 3 ;  —  vahyazdäti^  hadä  kamnaibis *asb3raibis  amu^t/'  aHyavJ'  *pisiyä^uv3- däm  Bh.5. 7.  a)  Adv,  statt  Akk.:  fra- variis  . .  amuh<^  rag!  nämä"  dahyäul  .  . avadä  asiyavJ'  Bh.  2.  13.  b)  abiy und  Akk,,  uzw.  a)  'nach  .  .':  ^vfda*' famä  ..  asiyavc^  abiy  bsbirum  Bh.j.  14; 2. 1,  J.  4.  ß)  'gegen  — ',  in  feindlichem Sinn:  adam  b�
```


## [2026-09-06T22:33:42.377Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 933 934 935; do echo \"###### leaf $n ######\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | head -c 3000; echo; done"
}
```


### [2026-09-06T22:33:44.231Z] TOOL RESULT

```
###### leaf 933 ######
b  der  NA.;  doch  s.  die Var,  —  4)  S  'Oa  L  3  "E-  —  S>  S  '^7-  »• Pü.:  s.  m  öai'fl-,  —  *)  Hds.  i»}/.  Pö.  bat nur  eine  nndeuüicbe  Erläutemne.  Da*  Wott ist  wahncheinlicb  m\X /raiutaiä  V.  4.  17  m- sammen zubringen.  —  7)  Pö.:  raflatt  statt  n>- ainUnH.  —  »)  Pb.;  tadäriin.  —  «  Theni.  — w)  Pü.!/räf  «lUan.  —  11)  So  E  I.  ^K./ra- iav:  —  ■»>  Pü.:  pa  fräe  iavihüh,  erl.:  ia  ä/ o/?  ö  *orwn  («/]  *arÄf , .  . —  "J>  Po.:  ir,.fräc ramit  lik  nun .  .fräi  raweiät  hoc  nin/rä?.  — '*)  Pa.  X  pa  .  •  /räc  rawiliüh.
g.   syä-,  j.  Sä-'*  V.  'sich  freuen'.
(iSOPfA.)  Yt  Ä  II  (=;o.  55,  74,  wolPraes.  I  o-ä-.  —  PPfP.  jr>j/tf-,  f'ä/'.i-;  Inf iüs').  ß)   am   und  Akk.;    na  tat  fra-  sätti,  VjW,  'litte.
susaili"''>  hactt  jafnavB  raonqtn  avi  bans-  i)  'sich  freuen',  absoL:  Auxsdhräis  Jm^ navS   gairinqm    V.  5.  2.  f)    a    und  rqm  (&±) . .  rämqmcä  äil  äadäta  syeitibyö
Akk.:  yims' fralüsat  raocä  a  ..  V.  s.lvliibyJ  Y. ^.8;  —  iatsm^da^aiti  urvä- 10.  a)   'herangehen,    -kämmen  von—   n?m  asaonS  *irlri^änaAe  "boh  macht  (es)
her"  (^«f'i»  mit  AbL  oder  Gen.  statt  Abi.):;  die  Seele  des  verstorbenen  Gläubigen" aat/ralasat..arfdvl..kaca  da'^usa^  masdä  .'P.24*^;  3^*^;  —  s.  noch  InC  2) 'sich
Yt5.  7;  88  (wo  'iusat);  —  fravasays  ..  ya  1  freuen,  Freude  haben  an— '(Lok.):  tamakl .  .fraiüssnte  banhivö  (sd.)  avari/ie  asnS  Yt  (sd.)  syäma  *ahura.masda  rtsmahi  usSinahi 13.^3.  a)Kaus.'heranbewegen,-briiigen,|»wMaw^ir  vlsamaidl  \.$8.z;  —  ^vS  $T nähern':  aaj  ta  aps  */rafärayati">  sata-\mq%r5  lyStS  yS  vTdull  mravaitl  "und vaesB  avi  kaftöAarfsvairJi  \t.8.% — fra  er,  der  Prophet,  ist  ja  froh  (über  jeden.', va  a/fl  (sd.)  va  sävayeili  V.103''^;  — |  der  dem  Wissenden  (davon)  Kunde  gibt" /rasavay(l(,t^xdi.  Spim,  nachPü.)"'  *aiwi.- 1  Y.  5/.  8;  F.  5. game  raivfris  paiti  tiöit  afraiävayd  "wenn  j      mit  </:  s.  InE
man  im  Winter  (das  Wasser  zum -ffarMMfl«)  woss.  ancayun  'ruhen',  np.  fjrf'troh'.  —  Pü. hinzubringt,  ist  man  R.,  nicht  aber,  wenn  '""  ^H'.,\"Z^\  »Ä^'^  l/^iw  ' mans  nicht  tut    N.JO^.  3)  'weggehen,       .)  j  pa  2,  —  >)  Vgl.  V.  60.  11.
sich  entfernen  von  -'  {ha^a  mit  AbL):  ,  äyita-,  j.  Säta-  Adj.,  PPfP.:  s.  lya-. vaiiKintum  ahmat  hala  :^armö  mtrr^ake      KompE.
hhrpa  framsat  Yt.  19.  34.  4)  '"  Gang  ,  äiyätay-,  j.  Sätay-  f.  'Freude,  Wohl- kommen', Kaus.  'm  Gang  bnngen,  halten',  behagen.  Glück':  :fq/mm  mazdalat»m  .. 'äitim  pasva  vlrayä  Vr.  7.  3 ;  —  upa  aitam xlapamm  avavat  't:is  uma  *isaiti  "in dieser  Nacht  erlebt  die  Seele  soviel  Freude " H.  2.  2;    —    \tc^ura*mazdä  .  .  hyj'    ■
a)  von  der  Schlacht:  miir?m  . .  yd fra
###### leaf 934 ######
s besitzt"  :/3>'«Ä(J  a^mi  däläca  %rätäla  ahmi 'taca  mainyuica  ahmi  spmtö.UmS  Yt.  1.  12; —  'ta  nama  ahmi  inSisia  nama  ahmi Yt.M3.  '
Zum  V.  xlai-;  Uutgesetilich  wäre  xlnär (Satiankult-)  oder  Jnif  (SatünUutsform); zum  i  vgl.  S  JJ".  —  Pü-i  inisai,  erl,:  «/ u  zyan  zyän  u  tut  atidar  äanem.  —  ■)  Aber die  Belegstellen  (Yt.  7.  13  f.)  haben  nur  ge- ringen Wert
•  j.  znöista-  Adj.  'der  die  beste  Kenntnis besitzt':  zniia  nama  ahmi  'ta  (statt  NSm.) nama  ahmi  Yt/.  13.
Aus  ar.  *tnali)ist/ia-7  Soll  den  Superl.  in  inä- lar-  (sd.)  vorstellen.  Geringe  Stelle.  —  Pü.; Snäsiii/um,  erL:  lüf  u  lyän  6  snästm.
•  j.  *znu.barflz-'>  f.  'Kniehohe,  -tiefe"': 'barasO  n»r?b»r>zB  *gairiJnns5  mSn!>  (sd.) FrBy.
NpiL:  zänüMli.  —  0  Hdi.  lanö.i'. —  ")  Oder Adj.
I  h,
•  j.,  g.  'ha-  Pron,  dem.  (fem,  hl-,  hl-) 'dieser';  nur  j.  hä  NSm.'>,  g.  hl  NSf."  '>, j.,  g.  ha  NSf",  j.  As,  hs,  hat'  NSm.''; I)  in  starkdeiktischer  Verwendung  'der hier'  (beim  Sprechenden);  an  der  Spitze des  Satzes:  hä  iiaiahul  sraosö  afyB  "hier ist  der  gute  .  .  Sr"  Vr.  /2. 1 ;  —  auf  die a.  Person  gehend:  yS  k)mSi  .  .  aittm äasli:  hä  ml  bara  aismaca  bar»smaca ",  .:  Du  da,  bring  mir  .  ."  N.  ios\  —  h5 im  Gegensatz  zu  hiu:  hö  upa.mpnts (Sp.  II 43  m.)  hau  asp3r>nS.maa  hau  .  , V..,/.48.  II)  in  schwachdeiktischerVer- wendung;  1)  auf  Zuvorgenanntes,  Voraus- gehendes (Wort  oder  Satz)  zurück- weisend; i)  auf  ein  Substantiv  oder subst  Pron.;  a)  substantivisch;  a)  im Hauptsatz,  a)  an  der  Spitze:  päurvS  .  . hs  ava>a{iÄ.)  vazata  Yt.  5.  61  C;  Ä  15', 46,  11-2*,  /9.43.  94',  Y.5.a4,  V.2.10, 9.  a;  —  mprsyahe  kihrpa  vänynahe  .. hd  agvS  usianavatqm  ilva.vasma  apayeitt hascit  vä  nSil  vä  Yt  t4- 19  f;  —  fsumi (sd.)  hs  ptä  gSuScä  . .  hf(s.  hya  nä  ßamä ni^anharatü   kJ   aiwyäxsayata   Y.  jÄ  4;
—  vatthus  sraesS . .  hScä  iia  ySt^wä  (sd.) *asia  Y.  27. 6;  —  äs  hau  as  .  .  yS  .  .  hö bä  ai^B  (Sp.  33  f )  äs  . .  aAmair/s  . .  V. p.  51  f.;  —  Alf  (s.Sp.  1730  ai.)b3 ..paoiryS yat  nä  .  .  nsit  äatäiti  hs  mqm  ava%a vfrmfliti  V.j(y.34f;  38;  —  sraolim  .. hs  nSil  iarfis  *franämaile  . .  frä  ahmäl pars  .  .  da!va  .  .  mmanie  Y. 57.  18;  — ärmaitlm  .  .  vartmaidl  (Sp.  1361  o.)  hä nS  avhai  Y.J2,  3;  —  vldäitlm  .  .  hä  xl pouräl  .  .  väuräHf{Sp.  1361  u)  Y.47.6;
—  aridvT  sära  anähita  . ,  hä  Al  mathim nyäsaia  Yt  5-  I37;  65,  Y.  ß'j.  5«,  V.  18. i6,5.48^(?);  — ■   haraifi  bars:   ha  hama
päirisäite  ..  Vtig.i  (vgl.  ß);  —  s.  noch V.7.79,  Y./o.is  (Sp.  1730  o.);  —  im Nachsatz:  äal  yaj  a%ra  para./asaiti  va- zimnü  ..  hs  paoiryS  galqm  nijainti  Yt /o.  loi,  ß)    hinter  dem    ersten  Wo
###### leaf 935 ######
egriff  ist  zuvor
nicht  genannt,  aber  durch  den  Zusammen- hang hinreichend  angedeutet:  kuha  .  . masyäka  Aqm.valtiante  .  .  yöt  Aqm.nasüm .  ,  tanüm  yaoidaihyqni  .  .  äat  ha  druxs avastrynte  ..V.g.  1-^13.  b)  im  Nebi satz:    a   tat  mprryitn  uzvazaite  .  ,  nä   tat
ß-aiusaiti  .  .  upa  tarn  vanam  aiili  yam hs  min-jS ..  V.j.if.  Anhang.  'Äa- (subst.)  steht  an  Stelle  des  Pron.  rel.  in einenn  Satz,  der  einem  vorausgehenden Relativsatz  inhaltlich  koordinirt  ist*':  yat nmänö.paitim  vindätna  ..yö  nS  hub)r?tqm barat  frazaintimla  hd  v»r3zyat  YL  73.  40; — ■  aiim  srvanm  .  ,  yim  upairi  k>r»saspB ayanha  pitüm  pacata  . .  tafsaica  h  S  uiatryH afUatia    Y.p.  II.  2)    auf  ein   Relativ
als  dessen  Korrelat,  substantivisch:  ys ahm  staeiti  hS  tnqm  staoilt  hOi  .  .  H. '■3't  V.J.  31-',  Yt.  J7. 2;  —  yS  tiä  Ais Aub»rflä  *barai  .  .  Aö  atvAätti  zatusttmB Yt.  13. 18.  3)  auf  einen  Satz;  substan-
tivisch, in  Kongruenz  mit  dem  Praedikat: ia^(Sp.436o.)  aSava ..v3nghaidrigvant>mi
Aa  sT  anhlus  vaauAl  vista  (Sp.  1315  u.) aifrftis  Y.4S.2;  —  ^a%7VärlS  sata  upä- zananqm  upszött  .  .  ha  Ai  asti  a&a  ha Al  asti  ap^rvtisV. S.  loj.  2)  voraus- weisend; i)  aut  den  Inhalt  eines  Kon- junktivs atze  s;  substantivisch,  in  Kongruenz mit  dem  Praedikat:  hä  ahmai  aSii »rmävi tat  ahmäi  jasat  ayaptim  yai  Al  puirJ us.sayata  . .  V.p.  4.  2)  auf  ein  Rela- tivum  als  dessen  Korrelat,  a)  substan- tivisch: As  äats  aspi/i  upa.raötayeile  (sd.) yS  drvaite  dalaiti  P.50;  —  As  As  aahat \.,yS..  as»m  aparaohayeite  (sd.)?  .  .  hS I  (zugleich  zurückweisend)  ba  anhat  .  .  yS [fiasumaitlnt  ap?m  .  . /rabarailiN  .y.-}Zi.; '  —  *Janyüil . .  ha  (zugleich  zurückweisend) >ya  dapta  apaiiasyHH  Y.io.  15.  a)  Die
Beziehung  ist  ungenau:  hS para  mtntä . . kS pasca  mirsts  mainyava  datva  frabavainti yat  masyö  masim  xsudra  avi  franhirssaiti V.  i^.  32;  —  hs  bä  trn  altaihm  arlnqm paoiryS  yat  na  . .  naire . .  tWil  daoäiti  V.  iS. 34.  b)  adjektivisch,  nur  mit  nar-  (Sp. 1051  ra.):  ^vai  hö^  nä'  asayeiti  .  .  ä/ai ahmäi  naire  miidtin  a»kal  yS  .  .  ra/i- "kv/irum  .  .  framaräite  A.  4-4f.;  ßf-'i  V. 15.47.  2  a)   auf  eine  erläuternde  oder
ergänzende  Beifügung  mit  relativischem  An- !  schluss;  a)  substantivisch:  hs  zT^ahumaca .  .  yS  ahurS  matdä  Vr.2,  7J  —  ha  tl  nS hui'öi'hsma  (sd.)  Aa  nS  utayuitlm  däi  . . bfrix'ii  (^d.)  Y.4K6;  —  ha  yaoida..ya dalna  ¥.5,21;  —  äat  Ai  Aa  paitiJa-vata yä  daüi  druxs  V.  i^.  31 ;  —  äat  hs  yS Aaomahe  »iflSö^. .  Y.  JO.  8,  Yt.  i/.  5;  —  hS \yB  duida  anrS  mainyus  V.ig.  i,  44,  Yt ij.  19.  b)  adjektivisch;  ya^a  hi/  hs na  yazata  yB  asava  taraiustrS  Yt  ij.  41; —  Ja/  Aä  druxi ya  nasul .  .  Y.S.  70O, 5. 15
```


## [2026-09-06T22:33:56.730Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"###### KNT leaf 225 (p.210) ######\"\nawk 'BEGIN{RS=\"\\f\"} NR==226' KNT.txt | head -c 3000"
}
```


## [2026-09-06T22:33:57.367Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN_1971 while entry ===\"\nsed -n '266585,266600p' KLN_1971.txt\necho \"=== KLN_1971 shekinah ===\"\ngrep -n -i \"shekinah\\|Shekhinah\" KLN_1971.txt | head"
}
```


### [2026-09-06T22:33:58.503Z] TOOL RESULT

```
###### KNT leaf 225 (p.210) ######
BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11.
brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. @parnp ‘clan-brother’, Lt. frater, OCS bratru, Gt. brobar, pIE *bhráter- (862, 875.111, $128, $154.П). баі nsm. ($124.5, 5186.1) DB 1.29f, 39f.
brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. deriv. brahmanyd- ‘religious’, to pIE root *bhergh- (see OP bard-; $75.1II, §95, $120, 5155.11; Henning, TPS 1944.108-18). For other views, see Kent, Lg. 13.301; Hartmann, OLZ 40.145-60; Nyberg, Rel. 367, 478; Hz. AMI 8.69, Apl 116-8 (to Av. barag- ‘to welcome’, barag- ‘rite’, Бәтәгба- ‘beloved’; wrongly, since this would give OP *bragman-); Christensen, Essai sur la démonologie iranienne 40-1; Henning, BSOS 10.506; Abayev, Iranskie Yazyki 1.134; Scherman, JAOS 65.141-3 n.23. Cf. also О. M. Dalton, Treasure of the Oxus 94-5. On form and meaning of РЫ. brahm brahmak, see Henning, TPS 1944. 108-18. brazmaniya nsm. ХР 41, 51, 54 (hardly brazmaniy isn. modifying arid; also not -niy apn. ‘divine’ with Sen 155, nor adn. in elliptic dual with Pisani, see under aria-).
т°, of dubious meaning, Se 1; taken by Justi, IFA 17.112, to be an abbreviation for OP *méraka ‘seal’, NPers. maráh.
та-, stem of ist person pron. in obl. cases of sg.; see adam.
mà conj. ‘not’, in prohibitions ete.: Av. Skt. mà, Gk. шӯ, pIE *mé ($109, §191.1, §292b). With subj.: DNb 55 (mé-taty), 58. With opt.: DB 4.59, 69, 79°; DPd 18, 19 bis, 20; XPh 39. With
201
inj.: DB 4.54; DPe 21; DNa 58, 59, 60; DNb 52 (mà-lay). With imv.: DNb 60. With lost verbs: DNb 57, DSq 4 bis; with restored subj. A'Sa 5^ bis, A?Ha 7, 7°. See also mdtya.
mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
таш- vb. ‘flee’: meaning established by Мат. and АКК. versions (Hüsing, KZ 38.258); probably to Skt. munthate ‘flees’ (Jn. JAOS 38.122). атида imf. ($211) DB 2.2, 71; 3.41f, 71.
Maka- sb. ‘Maka’, a province of the Persian Empire (lit. on location given in JAOS 56.217-8): Elam. ma-ak-qa, АКК. ma-ak, cf. Gk. pl. Мака ($99, $1322, SI4LITD. See also Mactya-. Maka nsm. DB 1.17; DPe 18.
magu- sb. ‘Magian’, member of a priestly order of Media: Flam. ma-ku-i3, АКК. ma-qu-&u, Gk. Méyos ($153.1). Uncertain material on mean- ing and etymology, Kónig,
```


### [2026-09-06T22:33:58.586Z] TOOL RESULT

```
=== KLN_1971 while entry ===

Derivatives: Whigg-ery, n.. Whig g- is h, adj., 
Whigg-ish-Iy , adv., Whigg-ish-ness , n. 
while, n. — ME. whil, while, fr. OE. hwil, ‘space 
of time, while’, rel. to OS. hwil, OFris. hwile, 
OHG. hwila , MHG. wile, G. Weile, Goth. 
heila, ‘space of time, while’, orig. ‘rest’, ON. 
kvila, ‘bed’ (lit. ‘resting place’), kvild, ‘rest’, fr. 
I.-E. base *q w eye -, *q w i(y)e-, ‘to rest, repose, be 
comfortable’, whence also Avestic shaitish, 
‘joy’, OPers. shiyatish, ‘joy’, L. quies, ‘rest, re- 
pose, quiet’, tranquillus (for *trdns-quilnos), 
‘quiet, still \ Arm. kan-gist, ‘rest’ (fr. pref. han- 
and gi, fr. base *q w i-), OSlav. po-koji, ‘rest’, po- 
citi, ‘to rest’. Cp. whilom, whilst, awhile. Cp. 
also quiet, n., and words there referred to. 
=== KLN_1971 shekinah ===
214381:Schechinah, n. — See Shekinah.
```


## [2026-09-06T22:34:04.176Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"Shekinah\" KLN_1971.txt | head\necho \"---\"\ngrep -n -i \"shekinah\\|Shechinah\" KLN_1966.txt | head"
}
```


### [2026-09-06T22:34:04.251Z] TOOL RESULT

```
214381:Schechinah, n. — See Shekinah. 
---
34006:Schechinah,  n.  —  See  Shekinah.
34942:Shekinah,  Schechinah,  n.,  the  Divine  Presence.  — Mishnaic  Heb.  shikhinah,  ‘dwelling  place  (of God)’,  from  the  base  of  shakhan,  ‘he  dwelled, abode’,  which  is  rel.  to  Aram. -Syr.  shfkhen, Arab,  sakuna,  ‘he  dwelled’,  Akkad,  shakanu,  ‘to lay,  set,  deposit’  (whence  mashkanu,  ‘dwelling place;  place;  deposit’).  All  these  verbs  are  prop. Shaph'el  (=  causative)  forms  of  the  Sem.  base k-w-n,  ‘to  stand  firm,  to  be",  and  orig.  meant  ‘he caused  to  stand,  caused  to  be  established’.
```


## [2026-09-06T22:34:16.464Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /Shekinah,  Schechinah/{print \"leaf(1-based)=\"NR}' KLN_1966.txt\necho \"--- page markers near ---\"\nsed -n '34900,34960p' KLN_1966.txt | grep -n \"14[0-9][0-9]\\|^ *1[0-9][0-9][0-9]\" | head\necho \"--- raw context ---\"\nsed -n '34930,34950p' KLN_1966.txt"
}
```


### [2026-09-06T22:34:18.395Z] TOOL RESULT

```
leaf(1-based)=762
--- page markers near ---
--- raw context ---
sheep,  n.  —  ME.  scheep,  sheep,  fr.  OE.  sceap, seep,  rel.  to  OS.  snip ,  OFris.  skip,  OS.  scap, MLG.  schap,  MDu.  scaep,  Du.  schaap,  OHG. scaf,  MHG.  scliaf  G.  Schaf;  of  uncertain  origin. Cp.  the  first  element  in  shepherd.
sheer,  adj.,  bright,  clear.  —  ME.  schere,  ‘bright, clear,  free’,  fr.  skere,  fr.  ON.  skserr,  ‘bright,  clear, pure’  (whence  also  Dan.  sk(j)zr,  Swed.  skar, ‘light  red’),  which  stands  in  gradational  relation¬ ship  to  ON.  skirr,  Swed.  skir,  ‘bright’,  OE.  scir (whence  dial.  E.  shire,  ‘bright’),  OS.  skiri,  OFris. skire,  MLG.,  MHG.  schir,  G.  schier,  Goth. skeirs,  ‘clear,  pure’,  ON.  skira,  OE.  sciran, OFris.  skiria,  MLG.  schiren,  ‘to  cleanse,  purify, clear,  explain’,  fr.  I.-E.  base  *ski-,  ‘to  glimmer, shine’.  See  shine,  v.
Derivatives:  sheer,  adv.,  ‘completely’,  sheer-ly, adv.
sheer,  intr.  v.,  to  deviate  from  its  course  (said  of  a ship).  —  Fr.  Du.  scheren,  ‘to  shear;  to  move aside’,  which  is  rel.  to  shear  (q.v.)
Derivative:  sheer,  n.,  deviation  from  a  course.
sheet,  n.,  piece  of  cloth;  piece  of  paper.  —  ME. schete,  shete,  fr.  OE.  sciete,  scyte,  scete,  itself derived  fr.  OE.  sceat,  Tap,  bosom,  surface;  piece of  cloth’,  which  is  rel.  to  ON.  skaut,  ‘seam,  hem of  a  garment’,  Goth,  skauts,  of  s.m.  M  Du.  scoot, Du.  schoot,  ‘bosom,  lap’,  OHG.  SC030,  scoya, MHG.  schos,  G.  Schofi,  of  s.m.,  and  prob.  also to  OE.  sceotan,  ‘to  shoot'.  See  shoot  and  cp. sheet,  ‘rope’.  Cp.  also  scuttle,  ‘hatchway’. Derivatives :  sheet,  tr.  v.,  sheet-ed,  adj.,  sheet-er, n.,  sheet-ing ,  n.
sheet,  n.,  rope  fastened  to  a  sail.  —  ME.  shete, fr.  OE.  sceata,  ‘lap,  bosom,  piece  of  cloth;  foot of  a  sail’,  rel.  to  sceat.  Tap,  bosom,  piece  of cloth’,  ON.  skaut.  Tope  fastened  to  a  sail’,  Du. schoot,  G.  Schote,  of  s.m. ;  see  sheet,  ‘piece  of cloth'.  It.  scotta,  Sp.  escota,  F.  escote  (now ecoute),  of  s.m.,  are  Teut.  loan  words. Derivative:  sheet,  tr.  v.
Sheffield  plate,  plate  of  copper  between  two  sheets of  silver.  —  Named  after  Sheffield,  Yorkshire, where  it  was  first  made.
shehitah,  also  shehita,  shechitah,  schechita,  n.,  the ritual  slaughtering  of  animals  or  poultry  for  use of  food  (Jewish  Religion).  —  Heb.  shehita11, ‘slaughtering’,  verbal  n.  of  shahdt,  ‘he  slaughter¬ ed’,  which  is  rel.  to  Aram.  shlhat,  Arab,  sahata, ‘he  slaughtered’,  Akkad,  shakhatu,  ‘to  flay’.  Cp. shohet.
sheik,  sheikh,  n.,  the  head  of  an  Arab,  family, tribe  or  clan.  —  Arab,  shaykh,  ‘an  old  man, elder,  chief’,  from  the  base  of  shakha,  ‘he  grew old’.
Sheila,  fem.  PN.  —  Irish  equivalent  of  Celia,  ab¬ breviation  of  Cecilia.  See  Celia,  Cecilia.
shekel,  n.,  an  old  Jewish  unit  of  weight  and  mon¬ ey.  —  Heb.  sheqel,  lit.  ‘weight’,  from  the  stem of  shdqal,  ‘he  weighed,  weighed  out  a  price, paid’,  whence  also  mishqal,  ‘weight’;  rel.  to Aram.  tsqal,  ‘he  weighed’,  Bibl.-Aram.  teqel, Aram,  tiqld,  ‘shekel’,  Arab,  thaqula,  ‘was  heavy’, thaql,  ‘load’,  Ethiop.  saqala,  ‘he  hung  up,  weigh¬ ed’,  Akkad,  shaqalu,  ‘to  weigh,  to  pay’,  shiqlu, ‘shekel’.  Cp.  siglos,  miskal.
Shekinah,  Schechinah,  n.,  the  Divine  Presence.  — Mishnaic  Heb.  shikhinah,  ‘dwelling  place  (of God)’,  from  the  base  of  shakhan,  ‘he  dwelled, abode’,  which  is  rel.  to  Aram. -Syr.  shfkhen, Arab,  sakuna,  ‘he  dwelled’,  Akkad,  shakanu,  ‘to lay,  set,  deposit’  (whence  mashkanu,  ‘dwelling place;  place;  deposit’).  All  these  verbs  are  prop. Shaph'el  (=  causative)  forms  of  the  Sem.  base k-w-n,  ‘to  stand  firm,  to  be",  and  orig.  meant  ‘he caused  to  stand,  caused  to  be  established’.
sheldrake,  n.  —  For  sheld-drake,  lit.  ‘shield  color¬ ed  drake’;  so  called  in  allusion  to  the  variegated markings  on  the  bird,  which  remind  one  thepaint- ings  on  a  shield.  See  shield  and  drake.  For  sense development  cp.  G.  schildern,  ‘to  paint,  depict’, fr.  Schild,  ‘shield’.
shelf,  n.,  a  slab  of  wood,  etc.,  fixed  horizontally
to  a  wall;  a  ledge.  —  ME.  schelfe,  shelf e,  fr.  OE. scylfe,  ‘plank,  bench,  shelf’,  rel.  to  MLG.  schelf, ON.  skjblf,  ‘bench’,  and  cogn.  with  L.  scalpere, ‘to  cut,  carve,  scrape’,  sculpere,  ‘to  carve’,  Gk. oxaXoy,  ‘mole’  (lit.  ‘the  digger'),  oxdXotjj, ‘pale,  stake’,  fr.  I.-E.  base  *(s)qel(e)-p,  a  -^-en¬ largement  of  base  *(s)qel-,  ‘to  cut,  cleave,  split’. See  shell  and  cp.  scalpel,  Scolopax,  sculptor, sculpture.  Cp.  also  scale,  ‘weighing  instrument’, and  words  there  referred  to.  Cp. — without  initial j — OI.  klptah,  ‘arranged’,  kalpate,  ‘is  arranged’, kalpayati,  ‘arranges,  allots’,  Avestic  hu-kerepta-, ‘well-formed’,  Goth,  halbs,  OE.  healf,  ‘half’, prop,  ‘cut  off,  divided’.  See  half  and  cp.  colter. Derivatives;  shelf,  tr.  v.,  to  put  on  a  shelf,  shelf¬ ful,  shelf-y,  adjs.
shell,  n.  —  ME.  schelle,  shelle,  fr.  OE.  sciell,  rel. to  Goth,  skalja,  ‘tile’,  orig.  ‘anything  scalelike, shingles’,  OE.  scealu,  ‘shell,  husk’,  and  cogn. with  OSlav.  skolika,  ‘shell’,  Russ,  skala,  ‘bark, rind’ ;  fr.  I.-E.  base  *(s)qel-,  ‘to  cut,  cleave,  split’. See  scale,  ‘weighing  instrument’,  and  cp.  words there  referred  to.  See  also  shelf.
Derivatives:  shell,  tr.  and  intr.  v.,  sheU-ed,  adj., shell-ing,  n.,  shell-y,  adj.
shellac,  n.  and  tr.  v.  —  A  compound  of  shell  and lac,  ‘a  red  resinous  substance’ ;  loan  translation of  F.  tuque  en  ecailles,  lit.  ‘lac  in  plates’, sbelta,  n.,  secret  slang  of  Irish  tinkers.  —  Of  un¬ known  origin.
shelter,  n.  —  ME.  scheldtrome,  sheldtrume,  shel- trome,  sheltroun,  fr.  OE.  scildtruma,  lit.  ‘a  troop with  shields’,  fr.  scild,  ‘shield’,  and  truma,  ‘troop, band,  legion’,  which  is  rel.  to  getrum,  ‘troop, multitude’,  trum,  ‘firm,  strong’.  See  shield  and trim.
Derivatives:  shelter,  tr.  and  intr.  v.,  shelter-ed, adj.,  shelter-er,  n.,  shelter-y ,  adj. shelty,  sheltie,  n.,  a  Shetland  pony.  —  Fr.  Shelty, abbreviation  of  Shetland ,  which  is  a  metathesis of  Shetland.
```


## [2026-09-06T22:34:28.574Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /while,  n\\.  —  ME\\.  whil/{print \"while leaf=\"NR}' KLN_1966.txt\nawk 'BEGIN{RS=\"\\f\"} /Shekinah,  Schechinah/{print \"shek leaf=\"NR}' KLN_1966.txt\necho \"--- klein while entry ---\"\ngrep -n \"while,  n\\.  —  ME\\.  whil\" KLN_1966.txt\n"
}
```


### [2026-09-06T22:34:30.151Z] TOOL RESULT

```
shek leaf=762
--- klein while entry ---
```


## [2026-09-06T22:34:36.969Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"KLN_1966 leaves:\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' KLN_1966.txt\necho \"--- leaf 915 head ---\"; awk 'BEGIN{RS=\"\\f\"} NR==915' KLN_1966.txt | head -c 600\necho; echo \"###### AKD printed p.30 (leaf 38) ######\"\nawk 'BEGIN{RS=\"\\f\"} NR==39' AKD.txt | head -c 2500"
}
```


### [2026-09-06T22:34:38.747Z] TOOL RESULT

```
KLN_1966 leaves:
903
--- leaf 915 head ---

###### AKD printed p.30 (leaf 38) ######
(nab.  u.  palm.)  "pklä  als  Beamtentitel,  desgl.  südarab.  'fM.  akk.
ahriqqu  od.  abrihi  Weiser,  Kundiger  (wohl  <<  sum.  ahrik)  :  >  viell. hebr.  'abrek  Gen.  41,48  (falls  dies  Wort  nicht  doch  vielmehr  ägypt.  Ur- sprungs ist).
aklf.  lamädu  lernen,  spez.  auch  vom  Erlernen  eines  Kuusthand- werks,  einer  Wissenschaft  :  davon  viell.  beeinflußt  der  Gebrauch  von  lämad in  diesem  techn.  Sinne  im  Hebr.,  wozu  auch  neuhebr.  tahnud,  Talmud, gehört.  Insbesondere  aber  wird  aram.  falmidä  Schüler  O  Späth ebr. talmid,  sowie  arab.  tilmid  i.  S.  v.  Gehilfe  des  Schmieds)  schon  der  Form nach  nur  als  <C  akk.  *talmidu,  das  als  solches  allerdings  noch  nicht  zu belegen  ist,  zu  gelten  haben.  [akk.  hakdmu  verstehen,  begreifen,
ist  dagegen  viell.  <;;  westsem.  (hebr.  häkam,  aram.  häkam,  arab.  hakania).]
akk.  samäru  singen  (wohl  auch  zugleich  spielen),  zammeru  Sän- ger :  ]>•  vieU.  hebr.  zimmrr  singen  und  spielen,  aram.  sdmar,  zammartä Flötenspielerin  O  wohl  arab.  zamnulrat  Flötenspielerin,  mizmiir  Flöte).
akk.  nigfitu,  ningütu  (vieU.  von  St.  nagu  klingen  od.  ä.)  Spiel, Musik  :  ^  viell.  hebr.  nägan,  niggcn  spielen,  ndgind  Saitenspiel.
akk.  imbftbu  Flöte  :  >  aram.  'abbfibä  (mand.  'ambühä)  Flöte,  Kohr O  wohl  arab.  ""unbrib  Eohr),  sowie  ambubajae  Flötenspielerinnen,  bei  Horaz, wie  endlich  wohl  auch  'Aßüßae  als  Name  des  Adonis  in  Perge.  akk.
1)  Damit  ist  viell.  urverwandt  akk.  Saratu,  hebr.  sarat,  aram.  sirat,  aiab.  Sarata einschneiden,  eini'itzen.
      30      
halhallatu  wahrscli.  Flöte,  halalu  flöten  :  davon  wohl  beeinflußt  hehr. halil  Flötei.  akk.  tahalu,  tapalu  wahrsch.  Tamburin  :  >  wohl
aram.  hihla  (>  arab.  fabl).  [aide,  timhuttu  ein  Musikinstrument,
wahrsch.  ein  Saiteninstrument  (urspr.  wohl  Ring,  Reif)  viell.  <  west- sem.,  s.  oben  S.  20  zu  dem  wohl  damit  identischen  timhuttu  Siegel]
S.  ferner  zu  weitereu  Bezeichniuigen  von  Handwerken,  Künsten  und sonstigen  Berufstätigkeiten  noch  S.  24  zu  dajjanu  Richter,  S.  7  zu purtdu Eilbo^te,  S.  49  zu  asü  Arzt,  S.  40  zu  iJckaru  und  irrüu  Laudmann, S.  40  zu  scikinu  Gärtner,  S.  41  zu  allallu  und  nüqidu  Hirt,  S.  14  f.  zu mdti  jagen,  arru  Vogelfänger,  hfiru  Fischer,  S.  45  zu  malalju Schiffer,  S.  39  zu  nuhatimmu  Bäcker.
```


## [2026-09-06T22:34:47.732Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sakänu\\|sakanu\\|maskanu\\|maskänu\\|maSkanu\\|Sakänu\\|sakinu\\|sakin\" AKD.txt | head -20"
}
```


### [2026-09-06T22:34:47.777Z] TOOL RESULT

```
238:akk.  maskanu  Pfand'  :  >.  aram.  maskönä,  meskänä,  maskäna  Pfand, masken  zum  Pfand  geben   (>>  arab.  muskän  Pfand,  massaka  bürgen).
240:1)  Eig.  Depositum,  von  Sakänu  niederlegen,  wie  hebr.  tasüviet-jsd  von  siim;  also nicht  von  msk  abzuleiten.  In  iilterer  Zeit  hat  maSkami  auch  die  Bed.  Lagerhaus, Speicher;  daraus  wohl  sicher  durch  Entlelmung  hebr.  miskanot  Vorratshäuser.  S.  auch noch  unten  S.  30  zu  Sakänii.
```


## [2026-09-06T22:34:55.661Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==40' AKD.txt | head -c 3000"
}
```


### [2026-09-06T22:34:57.107Z] TOOL RESULT

```
en,  spez.  auch  vom  Wohnung, Lager  usw.  aufschlagen  :  ^  viell.,  dann  freilicli  früh,  hebr.  .idkan,  aram. s9]:en  wohnen,  seknä,  safewfc  Wohnung,  arab.  salcana  ruhen,  wohnen;  frag- lich ob  dazu  etwa  auch  griech.  axtjvi)  gehört.
akk.  bfihu  Tor  :  >  aram.  hlM  (>  arab.  höh  u.  viell.  späthebr.  hah Ps.  90,12).  akk.  daltu,  st.  c.  dalat  Türflügel,  Tür  (vieU.  von  edelu
verriegeln)  :  >  viell.,  dann  freilich  sehr  früh,  hebr.  dälet,  dalt-,  auch dal,  phöu.  dl  oder  dl[t]  und  im  Buclistabenn.  /idKra,  sowie  wohl  auch  in Si).Tog  Sclireibtafel.  Aus  einem  spätbabyl.  *daf<tu  für  daltu  vieU.  >  jüd.- aram.  (auch  ägypt.-aram.)  dasSa  Türflügel.  akk.  cdiltu  Tür  (eig.  die
Yerriegelnde)   :  >■  viell.   syr.  PL   'edlätä,   'üdlrtta  Türflügel.  akk.
sirru  Tür  Zapfenloch  (viell.  ■<  sum.  sara)  :  >  späthebr.  .s/r,  aram.  t;7rri, mrtä,  sajartri  {sajärtä)  O  arab.  sir).
akk.  sikkiiru  Riegel  :  >  wohl  aram.  sUckdrO,  sukkara;  viell.  aus akk.  sekeru  verstopfen,  versclüießen,  überhaupt  >>  der  St.  skr  im  Hebr., Aram.  und  Arab.  akk.  mrdilu  Riegel  (von  edclu  verriegeln)  :  noch
unsicher,  ob  >  syr.  maddsla  Riegel,  oder  ob  dies  -<  griech.  fidvSalog  (und dies  viell.  <;  akk.  mcd'du).  akk.  sigaru  Riegel,  Schloß  (wahrech.  <<
sum.  sigar\  (vgl.  schon  oben  S.  15  zu  sigaru  Käfig,  Hundehalsband)  :  >» viell.  früh  sgr  verschließen,  im  Hebr.  und  Aram.  (arab.  viell.  als  sgn).
1)  Dagegen  ist  der  St.  halrdu  durchbohren,  aushöhlen,  natürlich  gemeinsemitisch; vgl.  noch  unten  S.  38  zu  halhallatu  Fußrmg.
      31      
akk.  asl'uppu,  ashippatu  Tür  schwelle  :  >  aram.  "eshiptä,  'iskujdd (^  arab.  'usltiffat).  —  In  älterer  Zeit  wohl  aucli  aus  akk.  aslmppu  bezw. sakkapu  ^  hebr.  niasqöp  Oberschwelle,  Säqep.  &dqüplm  Tür-  bezw.  Fenster- rahmen, akk.  sippu  Schwelle  (viell.  <^  sum.  sig,  zib)  :  >  wohl hebr.  sap,  sipp-,  phön.  sp,  aram.  sippä.  akk.  l/iüu  Tragbalken, Türsims  :  >  syr.  kettd.
akk.  ammatu  ein  Türteil,  wohl  Türpfosten  od.  ä.  (eig.  wohl  identisch mit  ammatu  Elle)  :  ^  wohl  hebr.  PI.  'aninidt  als  Türteil  Jes.  6,4.  akk.
manzazu  Pfosten  (von  naxdzu  stehen)  :  >  (bezw.  aus  i.  manzaztu)  viell. hebr.  maznzd  Türpfosten.
akk.  «j-säy?  Grund,  Fundament  eines  Baues  :  ^  wohl  aram.  \t,is'dfd, PL  'itSIajjä  O  arab.  'uss  Fundament,  'assasa  gründen).  Auch  im  Hebr. viell.  in  Spuren.  Zu  akk.  asitu  Pfeiler
```


## [2026-09-06T22:35:08.473Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sdkan\\|idkan\\|.dkan,  aram\" AKD.txt | head\necho \"---- context ----\"\ngrep -n \"aufschlagen\" AKD.txt | head\nsed -n '250,262p' AKD.txt"
}
```


### [2026-09-06T22:35:08.553Z] TOOL RESULT

```
405:akk.  Sakfinu  niederlegen,  niedersetzen,  spez.  auch  vom  Wohnung, Lager  usw.  aufschlagen  :  ^  viell.,  dann  freilicli  früh,  hebr.  .idkan,  aram. s9]:en  wohnen,  seknä,  safewfc  Wohnung,  arab.  salcana  ruhen,  wohnen;  frag- lich ob  dazu  etwa  auch  griech.  axtjvi)  gehört.
---- context ----
405:akk.  Sakfinu  niederlegen,  niedersetzen,  spez.  auch  vom  Wohnung, Lager  usw.  aufschlagen  :  ^  viell.,  dann  freilicli  früh,  hebr.  .idkan,  aram. s9]:en  wohnen,  seknä,  safewfc  Wohnung,  arab.  salcana  ruhen,  wohnen;  frag- lich ob  dazu  etwa  auch  griech.  axtjvi)  gehört.
akk.  giitu  Tafel,  Urkunde  (<<;  siun.  gida  eig.  wohl  lange  Tafel): >>  aram.  gitfä,  geUä  Urkunde,  Testament,  Scheidebrief  O  arab.  qitt  Buch, Scheck).  akk.  nijäru  Papyrusurkunde  (auch  im  Akk.  viell.  Fremdw.) :
>  neuhebr.  najär  Papier,  Pergament.  akk.  urMnu  Scliilf,  Papyrus-
1)  Ob  viell.  auch  so,  und  nicht  als  pron.  dem.,  das  dnh  in  der  Aufschrift  zu  der Geschäftsurkunde  des  aram.  Pap.  28  (Nr.  30)  aus  Elephantitie  aufzufassen  ist?
2)  Weniger  sicher  ist,  ob  etwa  auch  neuhebr.  sdhcr  i  Quittung  hierher  zu  ziehen  ist.
3*
      20      
Urkunde  :  >  wohl  aram.  'urbänä,  'arhänä  Schilf,  Papyrus.  S.  uoch unten  S.  56  zu  urhänu.
Das  übliche  akk.  Wort  für  Siegel,  hmuJchi,  hat,  wie  es  scheint, nur  im  Armen,  als  hiiJc'  Eingang  gefundeh.
[Dagegen  liegt  hebr.  fabhaat,  aram.  tib'ä,  fdb'ä  Siegelring  (das  wohl auf  ägypt.  db'-t  Siegel,  zui'ückgeht)  im  Akk.  wohl  nur  als  westsemit.  Fw. in  der  Form  titnhui,  timbuttu  vor.  i  S.  auch  noch  unten  S.  30  zu  tim- buttii  als  Musikinsti'ument.]
akk.  maklmru  Habe,  Besitz,  mit  der  Nebenform  namJmrru  :  >  wohl liebr.  mäkar  verkaufen  O  ägypt.  mJcr''  Kaufmann),  mäher  u.  mimlcär  Ver- kauf, Ware,  syr.  m^kar  kaufen.    S.  femer  oben  S.  16  zu  tantJcaru  Kaufmann.
akk.pron.  indef.  memeni  (so  namentlich  später  neben  dem  in  älterer Zeit  dafür  üblicheren  minimv)  „irgend  etwas"  i.  S.  v.  Besitz,  Habe  :  > walu'sch.,  der  Form  nach  aber  wohl  das  aram.  pron.  indef.,  späthebr.  iiiämon (Sir.  31,8),  aram.  mamöna,  neutest.  fiafjwväg  „Mammon".
akk.  nikasu^  Habe,  Vermögen  :  >  aram.  niksm  Schätze,  Reich- tum O  wahrsch.  erst  späthebr.  ndhäsim),  viell.  auch  südarab.  nskm.
akk.  nisirfu  Schatz  (von  nasäru  bewahren)  :  fraglich,  ob  etwa  hier- auf liebr.  'dsär,  PI.  'dsärot,  aram.  'au-prä  Vorrat,  Schatz,  zurückgellt.  ^
```


## [2026-09-06T22:35:19.239Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ sakina ===\"\ngrep -n -i \"sakina\\|Shekinah\\|sakīna\" FVQ_pages.txt | head -20\necho \"=== FVQ miskin ===\"\ngrep -n -i \"miskin\\|miskīn\" FVQ_pages.txt | head -10"
}
```


### [2026-09-06T22:35:19.315Z] TOOL RESULT

```
=== FVQ sakina ===
398:Tawral^ Injll, Sakina, Firdaus, Jahannam, are equally familiar to all
6392:ideogram 11114 33 sakina, 5 so that an Aram, origin of the Arabic
6404:The Shekinah.
6405:The question of the Shekinah in the Qur'an has been discussed at
=== FVQ miskin ===
9514:(Miskin).
```


## [2026-09-06T22:35:20.428Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF کاف و نون / کن ===\"\ngrep -n \"کاف و نون\\|کن ٔ\\|کن،\" FSF_pages.txt | head -10\necho \"=== FSF page 265 area ===\"\ngrep -n \"کاف\" FSF_pages.txt | head -20"
}
```


### [2026-09-06T22:35:20.495Z] TOOL RESULT

```
=== FSF کاف و نون / کن ===
17575:         ‫دو گیتی پدید آمد از کاف و نون‬                                      ‫زهره‌شان بکفد‪.‬‬
=== FSF page 265 area ===
2797:‫گشتاسب برد‪ .‬آنگاه کهآندو باهمروبرو‬              ‫به الف و نون «های» حرکت به «کاف»‬
4419:‫سواری میان لاغر و بر فراخ‬                         ‫بدکنش (با پیش کاف تازی وکسر نون)‪:‬‬
5071:        ‫‪-۱‬کافی‪ .‬باهندازه» به قدر کفایت‪:‬‬                            ‫پسد (باپیش اول و تشدید سین)‬
6694:‫(سیاست‌نامه ‪ :)۸۱‬کهملک بکافر بپاید و با‬                                           ‫چیزی بودن‪:‬‬
8467:         ‫شد از بی‌شبانی رمه تال و مال‬          ‫دل که ز بانگ یلان کافته‬
8471:                                               ‫بدندی» لب از تشنگی کافته‬
8529: ‫اسم صوت‪ .‬صدای شکستن یشاکافتن‬                                 ‫‪-_۱‬تخته تکه پارچه قواره‪:‬‬
8583:‫ترگ (باکاف پارسی ‪-‬در فرهنگ‌ها معمولاً با‬           ‫(جهانگیری ‏ برهان) جهانگیری همان بیت‬
8584:                      ‫کاف تازی آمده است)‬              ‫را کهدر صحاح آمده شاهد آورده است‪:‬‬
9619:      ‫بکافید بسی‌رنج پهلوی ماه‬
9990:                            ‫سکاف‬
10051:                             ‫خوش بیان‪:‬‬       ‫چیره در پیوند به «ی» به کاف پارسی بدل‬
11186:                                          ‫دام‬                         ‫مکافات بدگر کنی نیکوی‬
13888:               ‫‪...‬زفر بگشاده چون نکافریده‬                    ‫نباید که باشد جهانجوی زفت‬
14253:           ‫شکافت و بچه را بیرون کشید‪.‬‬          ‫گواه برای واژۀ زه به معنی فرزند از‬
14720:                        ‫سپه کش (بازبر کاف)‬           ‫معنی مهمان‪ ,‬راهگذر بکار می‌برد‬
14746:‫ناحیت‌ها و روستاها بسیار است و قصبهً‬                ‫پهلوی رودابه را شکافتند تاکودک را‬
15613: ‫کافر عشق بودگرنشود باده‌پرست‬                   ‫بداد ارمیدن دل تيز را‬
17515:                                        ‫کاف‬               ‫دگر گفت کاری گران آورید‬
17517:           ‫شکاف تراک (لغت فصرحس»‬                   ‫گچ و خشت و سنگ گران آورید‬
```


## [2026-09-06T22:35:24.881Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6370,6430p' FVQ_pages.txt"
}
```


### [2026-09-06T22:35:24.941Z] TOOL RESULT

```
into Arabic from Syriac as most other wine terms did, on the other
hand it may be a common derivation from early Semitic (Guidi,
Delia Sedfi, 603).
(Sakatia).
Of frequent occurrence.
To dwell.
Besides the simple verb we find ,Os*.>i, the participles y u* and
4, and the nominal forms AX-"- and
Zimmern, Akkad. Freindw, 30, thinks that the origin was Mesopo-
tamian. The Akk. sakdnu meant to settle in a place (niedcrlegen, nieder-
setzen), and was particularly used of dwelling somewhere. This, he
thinks, was the origin on the one hand of the other Semitic forms,
e.g. Heb. 13$; Phon. pttf; Syr. ^an ; and Ar. x , and,
perhaps on the other hand, of the Gk. crKrfvri tent (though in view of
the evidence in Boissacq, 875, this is doubtful).
(Sikkln).
xii, 31.
A knife.
Noldeke, Mand. Gramm, 125 n., had noted that it was a borrowed
word, comparing it with Heb. ^3& ; Syr. Jli^CD, and Mand. WID^O
and W20. 3 The Heb. ^32? is a loan-word from Aram, and the
Aram, word is also the source of the Gk. orvKivr] 4 and the Phlv.
ideogram 11114 33 sakina, 5 so that an Aram, origin of the Arabic
word is fairly certain, though whether from Syr. or O.Aram, it is
difficult to decide (cf. Guidi, Delia Sede, 581).
1 M. Muller, Asien und Europa, 1893, p. 102. Cf. Erman-Grapow, v, 410.
2 Levy, Fremdw, 81, and Lagarde, Mittheilungen, ii, 357.
3 Fraenkel, Fremdw, 84, says : " <>C- 1st seiner ganzen Bildung nach als Lehn-
wort dentlich, es hat ferner im Arabischen keine Ableitung und ausserdem 1st die
Lautverschiebungsregcl darin gegeniiber ]^3ttT deutlich verletzt."
4 Levy, Fremdw, 176.
6 PPGl, 201.174 FOREIGN VOCABULARY OF THE QUR ? AN
(Saklna).
ii, 249 ; ix, 26, 40 ; xlviii, 4, 18, 26.
The Shekinah.
The question of the Shekinah in the Qur'an has been discussed at
length by de Sacy x and by Goldziher, 2 and we need do no more here
than briefly summarize the results.
Th^e word occurs only in late Madinan passages and Appears to
have been a technical term learned by Muhammad at a relatively
late/period. In ii, 249, it refers to the sign whereby the Israelites
were to recognize Saul as their king, but in all the other passages
it is some kind of assistance sent down to believers from Heaven.
Now there is a genuine Arabic word AlxX^. meaning tranquillity,
from S&~ to rest, be quiet, and the common theory of the exegetes
is that this is the word used here. This, however, will hardly fit ii, 249, 3
and even in the other passages it is obvious that something more than
merely tranquillity was meant, so that many thought it had the special
meaning of ^-aj. 4 There was some doubt as to the vowelling of the
word, for we find k^L*-, ^x_X^, and <^-X^ beside the usual
<X-S (TA, ix ; 238; LA, xvii, 76). There can be little doubt,
however, that we have here the Heb. Pir^C?, 5 though possibly through
the Syr. lAl*O. 6 Muhammad would have learned the word from the
People of the Book, and not quite understanding its significance, have
associated it with the genuine Arabic word meaning tranquillity,
and this gives us the curiously mixed sense of the word in the Qur'an.
*' *>
*}L<, (Saldm).
Of very frequent occurrence, cf. iv, 96 ; v, 18 ; vi, 54, etc.
1 JA 1829, p. 177 if. 2 Abhandlungen, i, 177-204, and RHR, xxviii, 1-13.
So the Commentators admit that it means tranquillity in all passages savo ii, 249.
```


## [2026-09-06T22:35:26.401Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17555,17600p' FSF_pages.txt\necho \"=== which pdf page ===\"\nawk 'BEGIN{RS=\"\\f\"} /دو گیتی پدید آمد از کاف و نون/{print \"block=\"NR; }' FSF_pages.txt\ngrep -n \"\\[pdf page\" FSF_pages.txt | awk -F: '$1>17400 && $1<17700' | head"
}
```


### [2026-09-06T22:35:28.090Z] TOOL RESULT

```
‫همی پوست گفتی بروبر بکفت‬                                                      ‫است‪( ».‬برهان)‬
 ‫(‪)۲-۵۵۱-۳۴۴‬‬
                                                                   ‫بفرمود تا آب نار آورند‬
                     ‫(رودکی‪ .‬نفیسی‪:)۱۷4 .‬‬           ‫همان ترة جویبار آورند‬
       ‫کفیدش دل از غم چو آن کفتهنار‬                            ‫کجاتره‌گر کاشنی خواندش‬
‫کفیده شود سنگ تیمارخوار‬                             ‫تبش خواست کز مغز بنشاندش‬
                          ‫(اسدی ‪:)۰۲-۰۲‬‬             ‫(پرویز ‪)۲۲۵۲‬‬
                                               ‫‪raf‬‬                             ‫کافته‪ .‬کفته‪ .‬کنیده‬

  ‫تا ای خو چاو‬                   ‫چک‬
                                  ‫کی‬                            ‫من اکنون ز طبعم بهار آورم‬
  ‫مر کے کک ن‬                                         ‫مرین شاخ نورا بهبار آورم‬
 ‫«فیکون» پس شد موجود شد خلق شد‪.‬‬                                              ‫به باد هکنر‬
                                                                 ‫فگالنم بر اوی‬
 ‫اینافسانه درقرآن سور؛ نحل ایةآ‪۴‬م‪۲‬ده‬                 ‫ز ابر سخن درفشانم بر اوی‬
‫است «انماقولنا لشیء اذا اردناه ان‌نقول‬               ‫(سیاست‌نامه ‪ :)۵۳‬هر کهدر آن مجلس بود‬
                               ‫لفهیککنون»‪:‬‬       ‫وتان آن بیمبودکه‬
                                                                ‫راس‬
                                                                  ‫وتشوسی‬
                                                                       ‫انزهیب‬
         ‫دو گیتی پدید آمد از کاف و نون‬                                      ‫زهره‌شان بکفد‪.‬‬

 ‫چرانی به‌فرمان او در نه چون‬                                               ‫کافته‪ ,‬کفته‪,‬کفیده‬
‫)‪(۴14-۴۵-۶‬‬                                           ‫به‌ترتیب اسم مفعول از کافتن؛ کفتن‪:‬‬
                            ‫(ناصر ‪:)۵۵۳-۴‬‬                                             ‫کفیدن‪:‬‬
     ‫چو نشناسی که از نخست به ابداع‬                          ‫ز دیوان بسی شد به پیکان هلاک‬
‫فعل نخستین ز کاف رفت سوی نون‬                          ‫بسی زهره کفته فتاده به خاک‬
                                       ‫کافیدن‬        ‫(‪)۳۰۶۴۲-۵۲/۷۳‬‬
                         ‫به کافتن نگاه کنید‪.‬‬                                ‫(اسدی ‪:)۸۸۱-۶‬‬
                                         ‫کالید‬                   ‫چو باران نبودی» جگر نافته‬
                      ‫‪-۱‬قالب هرچیز‪:‬‬                  ‫بدندی» لب از تشنگی کافته‬
    ‫[جمشید] بفرمود پس دیو ناپاک را‬                                         ‫(ناصر ‪:)۰۵۱-۰۱‬‬
‫خاک را‬       ‫منیختن‬
                  ‫بدهرآآب ا‬                               ‫گل سرخ نکوفته بربار گویی‬
      ‫هرآنج ازگل آمد چو بشناختند‬                     ‫برون کرده حوری سر از سبز چادر‬
 ‫سبک خشت را کالبد ساختند‬                                                     ‫(مسعود ‪:)۸۱۱‬‬
 ‫)‪(۱-1-0‬‬                                                             ‫جهب‬
                                                                       ‫عد ن‬
                                                                          ‫ارمدنانه ش‬
                                                                                   ‫انشک‬
                         ‫(اسدی ‪:)۰۳۲-۹۷‬‬              ‫گر دل کمفنیده نار شود‬
           ‫الکبزد شد به در‬
                         ‫هر آن خکشت‬                                       ‫(ویس ‪:)۳۶۲-۰۷۱‬‬
‫بر آن کالبد بازناید دگر‬                                        ‫پآسنگه تازیانه زدش چندان‬
                            ‫‪ ۲‬جسم»؛ جسد‪:‬‬             ‫ابر پشت و سرین و سینه و ران‬
             ‫این آژدها‬         ‫ترسم که در‬                     ‫که اندامش چو ناری شد کفیده‬
=== which pdf page ===
block=358
```


## [2026-09-06T22:35:41.742Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 آشیان ===\"\ngrep -n \"آشیان\" BQT_v1_pages.txt | head -10\necho \"=== pdf page tags around ===\"\ngrep -n \"pdf page\" BQT_v1_pages.txt | head -3"
}
```


### [2026-09-06T22:35:41.823Z] TOOL RESULT

```
=== BQT v1 آشیان ===
248:فارسی سروسامانی عیدهد » خانه و آشیان؛ دیرین [نها را نمودارمیسازد مثلا
8110:شا فه ۱ - بروزن‌تلزبانه.بمعنیآشیان
8668:< له بااول مضموم حرفی باشد ذٍی مضلب که ب رکوههای بلند آشیانه کند و بغایت قوی و بز رکه
8784:آشیان جانوران شکاربرا کوبند حمیویاز وشاهین
8800:و الموت را م رکب از آله بممنی عقاب وموت مخطف آموت بمعتی آشیان دادتة اند .
13676:بمعنی آشیان باشد ۴ و چون عقاب در جا های
13678:بلئد آشیان مبکند آن قلعه را بدین‌نام خواندند
17157:باشد و آن برنده است در سقف خانها آشیان
20442:و دال ایسد » بسعئی آشیان باشد که جا و مقام
24699:سرخ عیباشدو درسقف خاهاآشیان میکند واو را
=== pdf page tags around ===
```


## [2026-09-06T22:35:43.807Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 شاد ===\"\ngrep -n \"شاد ‪\\|‏شاد\\|^.*شاد.*خرم\" BQT_v2_pages.txt | head -10\necho \"=== count leaves v2 ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v2_pages.txt\ngrep -n \"pdf page\" BQT_v2_pages.txt | head -3"
}
```


### [2026-09-06T22:35:45.824Z] TOOL RESULT

```
=== BQT v2 شاد ===
6872:  ‫لے‬               ‫شاه جپان شادمان و خرم و خندان‬               ‫بيذ چند بتادی‬          ‫رشدد‬
16768:‫دلیر فلكت هکنابه از کرکب عطارد‬                                                             ‫ارم کوفته باشاد ‪.‬‬
22281:               ‫میخور و شادی کن و خرمنشین ‪.‬‬                  ‫يتن‬
23067:‫گونند هش نگین انوشیروان چنین بوده که‬                           ‫و خوش وشاد و خرم را نیز گفته اند ‪ - ۳‬و نام‬
32424:‫و کی را نیز کویند که پبوسته شادی کند‬                   ‫هم آمده است ‪ -‬و خرمی و طراوت را لز‬
35198:         ‫سر شاد ‪ ۰ ۰‬بر وزن خروار ب‬                                            ‫سر سیژ‪= ۴‬بفتح الت و سکون‌بای ابجد‬
=== count leaves v2 ===
683
```


## [2026-09-06T22:35:51.909Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"v1 leaves:\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v1_pages.txt\nhead -5 BQT_v1_pages.txt\necho \"=== which block has آشیان at line 8110 ===\"\nawk 'NR<=8110' BQT_v1_pages.txt | tr -cd '\\f' | wc -c"
}
```


### [2026-09-06T22:35:53.963Z] TOOL RESULT

```
v1 leaves:
777
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
=== which block has آشیان at line 8110 ===
257
```


## [2026-09-06T22:35:56.343Z] TOOL CALL #42: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:46 2>&1 | head -60"
}
```


### [2026-09-06T22:35:58.263Z] TOOL RESULT

```
no scan of BQT covers printed page 46 (see 'scans' in refs_online.json)
```


## [2026-09-06T22:36:04.589Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\" | head -40"
}
```


### [2026-09-06T22:36:06.232Z] TOOL RESULT

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
```


## [2026-09-06T22:36:15.096Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 255 256 257; do echo \"##### v1 leaf $n #####\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v1_pages.txt | head -c 1800; echo; done"
}
```


### [2026-09-06T22:36:17.304Z] TOOL RESULT

```
##### v1 leaf 255 #####
ی آشنا کر
خابة سک آنی است ۷ . خالهرا نیز گویند چنانکه گوبند «اين عمارت سه
آ ش لقن * کنابهازآنت کهکیرا | آشکوب است» بمنی مه حرتبه است - و بمعنی
چینه دبوارهم آمده اسث یمنی هر مرتبه که از
از عراعه آزارکسی رانگرانه: . < با ِ
سم ۲ 9 ار گنارند - وآسمادا نی کوینه  ٩‏
] شتی خواده - حلوا و طعاسی را یو ین 7
گوند که بعد از آفتی:.مسان دوستان بپز ند ۳ ح بفتح شالث بر وزن و۳9
مرن زارد مخذف « آشامد » باشد که ماضی آشامیدنست .
: ]شتا » بسکون ثاث و نون بالف
کید . ممروفت که قض ببگاله باشد ۴ -
تلور اه هو وا ليز گونن که شتا کننده
باشد - و شناوری و آب ورزی را هم گفته‌اند ۴
) شتینه پروزن و هعنی اشامت
۲ شفته » بنم نك بر وزن آلفند . بهم
برآهده و پریشان حال - و عاشق را گویند ۷
اشکو - باکاف بروزن چارسو ؛ مخفف
آشکوب است که هر مرنبه ازیوششی خانه‌باشد .
آ شکوب ؟. بروزن‌خا کروب . بمعنی
آسمانه و سقف خانه باشد - وهر موتبه ازیوشش
- وودمطنان خنصی است که بذانه شامای از
تحضق باخود آورده باشد وباشاهد وحدنتی رابطة
آشنایی بود .
] شناب « بر وزن ماعتاب . بمعنی
قتایی اد که اتتوزی و فا کففد اسخ 9 :
آشنا گر « بفتم کاف فارسی و سکون
۱ کند بیستر. جندبادستر , قندقیری* مخز
##### v1 leaf 256 #####
آشناو ۳ ف_
رای فرشت ۰ بمعنی شناور باش که شناکننده | شور و فتده و غوغا - و بمعتی فاعل و امر باین
۳ ۱ .
است چین معتی هم هست . ٩۶‏
/ و - بسکون واو » بمعنی شناور ] شوردن « بارا ودال بی‌تقطه بروزن
متفه ۷ : 1
۱ آشنا ور- ۰ می آخشا گر ی ات
0 4 ۳ 2 عصی و خسمس مودن باشد ۴ .
آشوغ ب بروزن‌آروغ , شخص‌مجهول
غیر عمروف را گویند .
۲ شوفتی ۴ با فا بروژن واسوختن ,
یمنی آشفتن و مهم سس آمدن باشد .
] شبان ۴ » بایای حطی بروزن ما کبان,
خابةٌ مرغان (۱)- وسقف خانه باشد . .
آ شناه د بروزن‌یادشاه , بععنی‌شنا کردن
باشد - و شناکنندة را نیز گوبند ٩‏ ۰
! شو ه منم الث وسکون واو . مخفف
1 ۱[ ۰ بمعنی هم
برآحدن ۱ است کهبعربی «مدغله» گونند - ویمعتی
(۱) چك : د را گوشد 2
۱ - ره : آشتا. ۴ - نیز آشفتن خوا بکسی را : مرادل نامد که اسان‌را بیدار کنم
وخواب برایشان بباشورم . «نفیرابوالفتوح بنقل‌لفت‌نامه». ۳ ره : آشفتن. ۴ - مرکب از
پیشوند 2 و511812108 پمعنی جای وسرای » ارمتی 51360 (بمعنیده » قربه) «بارتولمه ۱۷۰۷*.
آشور - ۸65۲۲2 . بپلوی ۸۹۵۶ < ما رکوارت . شهرستانها بند ۵۲ ص۷۱ »؛
مملکتی در. آسیای فدیم ۰ بن ماد . بل در جوز رود دجله و مناوب شهر‌هایآسور کناک۸5:
کله 212۳ و ننوا 101۷610 پابتخت آن بو
##### v1 leaf 257 #####
۰- 1 حه
شا فه ۱ - بروزن‌تلزبانه.بمعنیآشیان
است که خانهٌ مرغان - و سقف خانه باشد  )۱(‏
| شینه - بروزن خاکینه , تخم مرغ را
و
| شیهه - با های هوز بروزن پاکیزه .
صدا و یه اسب را کویند و بعربی « صهیا ۰
خوانند .
| صف « بفتم صاد و سکون فا . دنم
پسر برخیاست و اویکی از علمای بنی‌اسرائیل و
وزیر سلیمان علیه‌اللام بود وعلوم غریبه وسیمیا
باو منسوب است - و در صحاح الادوبه بمعنی
و باین ممتی بفتح همزه نیز آمده است . گویند
آين لت عبری است .
) طر یال » باطا ورای بی‌نقطه ودولام
بروزن چار دبوار » بلفت دومی رستنی باش که
آ را جعربی « عیشةالبرس» ۴ خواند و نخم آن
را استعمال کنند و آن‌ببزرگی تخم کرفی‌است »
وکبود رنگ میباشد» و بغایت تلخ بود ۰ بهق و
برس را تافع است . و اکر بکوبند و دد بینی
زن آیتن بدمند بچه بندازد ؛ و بعضی گویند
غاد - با غن تقطه‌رار بر وزن نالچار »
هر چیزینم کشده و خسیده از آب با از خون
بود - و فرو شدن نم باشد بزمین و آمیخته - و
بهم پیوسته و سرشته را نیز گویند - و بمعنی‌بر
انگخته و تحريك کرده هم آعده است که بعربی
اغراء خوانند .
آغارد بفتح را وسکون دال بی‌نقطه,
بعنی بهم بيامیزد وسرشته کند و بر انگیزاند و
تحريك نماید - و سک�
```


## [2026-09-06T22:36:41.924Z] TOOL CALL #45: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T22:36:41.930Z] TOOL RESULT

```


```


## [2026-09-06T22:36:45.850Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B4%DB%8C%D8%A7%D9%86%D9%87",
 "prompt": "Give the full Persian etymology section for آشیانه (and آشیان if present): what Middle Persian / Old Iranian / Proto-Iranian forms are given, which root, and which sources are cited (Hasandust, MacKenzie, Nyberg…)."
}
```


## [2026-09-06T22:36:47.561Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D8%AF",
 "prompt": "Give the full Persian etymology for شاد (šād) 'happy': Middle Persian, Old Persian, Avestan, Proto-Iranian and PIE root forms, and cited sources."
}
```


### [2026-09-06T22:36:49.932Z] TOOL RESULT

```
Based on the webpage content provided, **no etymology section is present** for آشیانه (âšiyâne) or its alternative form آشیان (âšiyân).

The page displays only:
- Alternative forms
- Pronunciation information
- Noun definition ("nest")
- A song lyric example

There are no Middle Persian, Old Iranian, Proto-Iranian forms, etymological roots, or citations from sources like Hasandust, MacKenzie, or Nyberg included in this Wiktionary entry.
```


### [2026-09-06T22:36:54.018Z] TOOL RESULT

```
# Persian Etymology of شاد (šād) "happy"

Based on the Wiktionary entry, here is the etymological chain:

**Middle Persian:** شʾت' (šʾt' /šād/)

**Old Persian:** 𐏁𐎡𐎹𐎠𐎫 (š-i-y-a-t /šiyāta-/)

**Proto-Iranian:** *šyaHtas ("happy")

**Proto-Indo-Iranian:** *čyaHtas

**Proto-Indo-European:** *kʷyeh₁-to-s, derived from the root *kʷyeh₁- meaning "peace, rest"

The entry notes this adjective derives from the verb شادیدن (šādīdan). The etymological progression shows the word's evolution across Indo-European language families, with the core meaning relating to a state of peace or rest that developed into the modern sense of happiness or cheerfulness.
```


## [2026-09-06T22:36:59.298Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7yeh%E2%82%81-",
 "prompt": "Full content: the root's gloss, derived terms (Latin quies, tranquillus, Germanic *hwīlō, Avestan/Old Persian šiyāti-, Persian šād), and any notes/references."
}
```


## [2026-09-06T22:37:00.129Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/while",
 "prompt": "Give the full etymology of 'while' (n.), including the Proto-Germanic form and the PIE root, and any related words listed (quiet, tranquil)."
}
```


### [2026-09-06T22:37:05.819Z] TOOL RESULT

```
# Proto-Indo-European Root *kʷyeh₁-

This reconstructed root carries the meanings "to rest" (verb) and "rest, peace" (noun). It's a foundational element in Indo-European language families.

## Key Derived Terms

The root produced numerous descendants across language branches:

**Latin derivatives** include "quiēs" (rest) and "quiētus" (quiet), as well as the compound "tranquillus."

**Germanic forms** stem from Proto-Germanic *hwīlō, which eventually yielded English "while" and related terms.

**Iranian languages** show "šiyāti-" (happy) in Old Persian and Avestan, evolving into Persian "šād" (happy/joyful).

**Slavic cognates** appear in Proto-Slavic forms like *kojiti* (to soothe) and *pokojь* (peace).

**Other branches** include Albanian "sillë," Armenian "hangčʻim" (to rest), and Celtic forms like Welsh "gorffwys."

## Linguistic Significance

The root demonstrates the comparative method underlying Indo-European reconstruction—scholars identify consistent sound correspondences across documented languages to hypothesize earlier forms that predate written records.
```


### [2026-09-06T22:37:07.858Z] TOOL RESULT

```
# Etymology of "While" (Noun)

**Origin Chain:**
Old English *hwile* (accusative of *hwil*) → Proto-Germanic *\*hwilo* → PIE *\*kwi-lo-* (suffixed form)

**Root Meaning:**
The term traces to the PIE root *\*kweie-*, which means "to rest, be quiet." The semantic shift occurred in Germanic languages, where "period of rest" evolved into "period of time."

**Key Historical Forms:**
- Old Saxon *hwil*
- Old Frisian *hwile*
- Old High German *hwila*
- German *Weile*
- Gothic *hveila*

**Related Cognates:**
Old Norse forms include *hvila* (bed) and *hvild* (rest), demonstrating the original sense of repose underlying the temporal meaning.

**Modern Derivatives:**
The noun survives primarily in formulaic expressions like "all the while" and "worthwhile," though largely superseded by the word "time" in contemporary usage. The conjunction form developed from Old English *þa hwile þe* (literally "the while that"), and variants like *whiles* (13th century) and *whilst* (14th century) emerged subsequently.
```


## [2026-09-06T22:37:13.978Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%83%D8%A7%D9%86",
 "prompt": "Give the Arabic etymology of مكان (makān) 'place': which root is it assigned to (ك و ن or م ك ن), and what do the notes say about the debate? Also any Persian section."
}
```


## [2026-09-06T22:37:15.860Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B3%D9%83%D9%8A%D9%86",
 "prompt": "Give the Arabic etymology of مسكين (miskīn): is it derived from the root س ك ن, or borrowed from Akkadian muškēnu / Aramaic? Quote the etymology and cited sources. Also mention descendants (Persian مسکین, Italian meschino, French mesquin)."
}
```


### [2026-09-06T22:37:19.652Z] TOOL RESULT

```
# Arabic Etymology of مكان (makān)

**Root Assignment:** The word is assigned to the root **ك و ن** (k w n).

**Etymology Explanation:** According to the Wiktionary entry, مكان is a "noun of place from the verb كَانَ (kāna)." The document notes cognates in Hebrew _מָכוֹן_ (mɔḵōn) and Ge'ez _መካን_ (mäkan), supporting the Semitic root classification.

**Notable Point:** The article does not mention a debate between competing root theories (ك و ن vs م ك ن). It straightforwardly identifies the single root as ك و ن with 11 related Arabic terms listed.

**Persian Section:** The page includes a Persian entry showing **مکان** (makân) as a descendant from Arabic, with further language derivatives listed (Bengali, Gujarati, Hindustani, Kashmiri, and Punjabi forms also derived from the Persian).
```


### [2026-09-06T22:37:22.475Z] TOOL RESULT

```
# Etymology of مسكين (miskīn)

Based on the Wiktionary entry, this word is **borrowed from Akkadian**, not derived from the Arabic root س ك ن.

## Etymology Source

The page states: "Probably from Classical Syriac _meskēnā_ ('poor, miserable, wretched'), from Akkadian _muškēnum_ ('commoner, poor')."

The word also "passed into Hebrew _miskēn_ ('miserable') and via Aramaic _meskēnā_" into other languages.

## Key Sources Cited

The entry references scholarly works including:
- Fraenkel, Siegmund (1880) on rare vocabulary in Arabic poetry and the Qur'an
- Jeffery, Arthur (1938) on foreign vocabulary in the Qur'ān
- Nöldeke, Theodor (1910) on Semitic linguistics

## Notable Descendants

The word spread widely through medieval trade networks:
- **Persian**: مسکین (meskin)
- **Italian**: meschino
- **French**: mesquin (via Italian)
- **Spanish**: mezquino
- **Swahili**: maskini
- **Indonesian/Malay**: miskin

This represents a fascinating example of Akkadian's linguistic influence persisting through Semitic languages into European vocabulary.
```


## [2026-09-06T22:37:29.425Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%83%D9%8A%D9%86%D8%A9",
 "prompt": "Give the Arabic etymology of سكينة (sakīna): is it a native noun from س ك ن or a loan from Hebrew/Aramaic šəḵīnā? Quote the etymology and cited sources, plus the Persian descendant."
}
```


## [2026-09-06T22:37:30.757Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%A9%D7%9B%D7%99%D7%A0%D7%94",
 "prompt": "Give the Hebrew etymology of שכינה (shekhinah): from which verb/root, and any note about relation to Akkadian šakānu or the Semitic root k-w-n."
}
```


### [2026-09-06T22:37:35.738Z] TOOL RESULT

```
# Hebrew Etymology of שכינה

Based on the Wiktionary content provided:

The word שכינה (sh'khiná) derives from the Semitic root **שׁ־כ־ן** (sh-k-n). It is specifically "the verbal noun of שָׁכַן (shakhán, 'to dwell')."

The page does not mention any connection to Akkadian šakānu or the alternative Semitic root k-w-n. The documented etymology focuses solely on the sh-k-n root and its relationship to the verb meaning "to dwell" or "to reside."
```


### [2026-09-06T22:37:35.836Z] TOOL RESULT

```
# Arabic Etymology of سكينة (sakīna)

Based on the Wiktionary entry, the word has **two distinct etymologies**:

## Etymology 1: Native Arabic Formation with Semantic Loan
The first meaning (inner peace, tranquility) comes from "an Arabic formation from the root س ك ن (s k n), but religious meanings are a semantic loan from Hebrew שְׁכִינָה (shəḵīná)."

This indicates the word structure is Arabic, but the religious sense was influenced by Hebrew.

## Etymology 2: Alternative Form of "Knife"
The second meaning (knife) is "alternative form of سِكِّين (sikkīn)," representing a purely Arabic derivation.

## Cited Sources
The entry references several scholarly works including works by Geiger (1833, 1902), Jeffery (1938), and Nöldeke (1910)—all examining the Hebrew-Arabic linguistic connection in Quranic vocabulary.

## Persian Descendant
**The Wiktionary entry does not list any Persian descendants.** Only Maltese and various Arabic dialects (Egyptian, Hijazi, South Levantine, Tunisian) are mentioned as descendants from Etymology 2.
```


## [2026-09-06T22:37:41.365Z] TOOL CALL #54: WebSearch

```json
{
 "query": "Semitic root šakānu shaphel causative of kwn \"to be\" Klein Shekinah etymology criticism"
}
```


## [2026-09-06T22:37:43.407Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%83%D9%86",
 "prompt": "Arabic سكن (sakana) 'to dwell, be still': give the etymology (Proto-Semitic root, cognates: Hebrew shakhan, Akkadian šakānu), and any note about relation to k-w-n."
}
```


### [2026-09-06T22:37:49.041Z] TOOL RESULT

```
# Etymology of Arabic سكن (sakana)

## Root and Cognates

The word derives from the **Semitic root س ك ن (s k n)**. According to the Wiktionary entry, it is "Cognate with Hebrew שכן, Akkadian šakānum ('to place, to put, to set, to establish') and Ugaritic škn ('to establish')."

## Meanings

The verb has multiple related senses: "to be still, to be tranquil, to be peaceful" and "to live, to reside, to inhabit." A noun form means "dwelling, abode, habitation."

## Note on k-w-n

The entry does not mention any relationship between سكن and the root k-w-n. The documentation focuses solely on the س ك ن (s k n) root and its Semitic cognates across Hebrew, Akkadian, and Ugaritic languages.
```


### [2026-09-06T22:37:49.206Z] TOOL RESULT

```
Web search results for query: "Semitic root šakānu shaphel causative of kwn "to be" Klein Shekinah etymology criticism"

Links: [{"title":"Sakina","url":"https://en.wikipedia.org/wiki/Sakina"},{"title":"Balashon - Hebrew Language Detective: shechinah and scene","url":"https://www.balashon.com/2020/06/shechinah-and-scene.html"},{"title":"Hebrew Word of the Week —Shekinah שְׁכִינָה - More Than Just Glory - Beit Hallel Israel","url":"https://www.beithallel-israel.org/hebrew-word-of-the-week_shekinah_more-than-just-glory/"},{"title":"Shekhinah","url":"https://en.wikipedia.org/wiki/Shekhinah"},{"title":"Shekinah | Encyclopedia.com","url":"https://www.encyclopedia.com/philosophy-and-religion/judaism/judaism/shekinah"},{"title":"K-P-R","url":"https://en.wikipedia.org/wiki/K-P-R"},{"title":"Shekhinah | Encyclopedia.com","url":"https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/shekhinah"},{"title":"Shekhinah (disambiguation)","url":"https://en.wikipedia.org/wiki/Shekhinah_(disambiguation)"},{"title":"Multi-Tape Two-Level Morphology: A Case Study in Semitic Non-linear Morphology","url":"https://arxiv.org/pdf/cmp-lg/9407023"}]

Based on the search results, I found relevant information about Klein's etymology of Shekinah:

Klein writes that the root is the Shaph'el form of the root כון - "to be, set up, be established." This refers to the Hebrew word Shekinah, which derives from the root שכן, meaning "to dwell, settle down," so the shekinah is literally "the dwelling place (of God)."

The search results show that the standard etymology connects Shekinah to the Semitic root š-k-n meaning "to settle, inhabit, or dwell," rather than treating it primarily as a Shaph'el (causative) form derived from the root kwn ("to be"). However, Klein appears to propose an alternative etymological analysis that traces it back to kwn through a causative formation.

Unfortunately, the search results did not contain specific information about Klein's proposed etymology involving šakānu as a Shaph'el causative, nor did they include scholarly criticism of this particular etymological proposal. To find more detailed information about the criticism of Klein's etymology, you may need to consult specialized etymological dictionaries or academic papers on Hebrew and Semitic linguistics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T22:37:56.028Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.balashon.com/2020/06/shechinah-and-scene.html",
 "prompt": "What does this post say about the etymology of shechinah/shakhan, Klein's Shaph'el-of-kun proposal, Akkadian shakanu, and Greek skene? Quote the key sentences."
}
```


## [2026-09-06T22:37:59.191Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%86",
 "prompt": "Arabic كان (kāna) 'to be': give the etymology (root ك و ن, Proto-Semitic *kwn, cognates Hebrew כון kūn, Akkadian kânu), the derived terms listed (تكوين takwīn, كائن kāʾin, مكان makān, كن kun), and the Qur'anic imperative kun fa-yakūn if mentioned."
}
```


### [2026-09-06T22:38:02.510Z] TOOL RESULT

```
# Etymology of Shechinah and Related Terms

**Shechinah etymology:**
The post states: "It derives from the root שכן, meaning 'to dwell, settle down,' so the _shekinah_ is literally 'the dwelling place (of God).'"

**Klein's Shaph'el-of-kun proposal:**
"Klein writes that the root is the _Shaph'el_ form of the root כון - 'to be, set up, be established.'"

**Greek skene connection:**
The author notes that C. F. D. Moule proposes the Greek word _skēnḗ_ (tent) "may have been influenced by the Hebrew root שכן meaning 'dwelling.'" However, the post clarifies this isn't necessarily direct etymology but rather Moule's theory about "Greek words whose use, or at least frequency, may have been suggested by a certain (perhaps fortuitous) similarity of sound or spelling to certain Semitic words."

**Akkadian connection:**
The post does not discuss Akkadian shakanu.
```


### [2026-09-06T22:38:05.587Z] TOOL RESULT

```
# كان (kāna) - Etymology and Derivations

**Etymology:**
The verb كان derives from the root "ك و ن" (k w n). Its ancestry traces to Proto-Semitic *kawan- ("to be or exist in a place"), with cognates appearing in Hebrew and other Semitic languages.

**Primary Meaning:**
This verb functions as a copulative verb meaning "to be," taking an accusative case predicate. It also serves as an auxiliary verb for forming various past and future tenses.

**Notable Qur'anic Usage:**
The text references the famous imperative form: "كُنْ فَيَكُونُ" (kun fa-yakūnu) - "Be, and it is" - appearing in Qur'an 40:68, where God commands creation into existence.

**Key Derived Terms:**
Related formations include:
- كائن (kāʾin) - existing, present
- مكان (makān) - place, location  
- تكوين (takwīn) - formation, composition

**Linguistic Notes:**
Unlike Indo-European copulative verbs, كان uniquely governs an accusative predicate rather than nominative case, reflecting Semitic grammatical structure.
```


## [2026-09-06T22:38:16.346Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"سکینه\" \"مکان\" \"تکوین\" \"کائنات\" \"تسکین\" \"مسکین\"; do echo \"=== $w ===\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done\necho \"--- sample سکینه ---\"; grep -n \"سکینه\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T22:38:18.459Z] TOOL RESULT

```
=== سکینه ===
MON_part1.txt:2
MON_part2.txt:1
=== مکان ===
MON_part1.txt:92
MON_part2.txt:140
=== تکوین ===
MON_part1.txt:6
MON_part2.txt:2
=== کائنات ===
MON_part2.txt:2
MON_part1.txt:2
=== تسکین ===
MON_part2.txt:11
MON_part1.txt:11
=== مسکین ===
MON_part1.txt:4
MON_part2.txt:2
--- sample سکینه ---
MON_part1.txt:5425:مة. حشونت» نندی. سکینه» وقار. حلم 
MON_part1.txt:78775:سکینه: (0-)21172و [ع. سکننة معر.] (ا.) 
MON_part2.txt:22558:تابوت سکینه قرار داشتند و بال‌های کروبی
```


## [2026-09-06T22:38:24.146Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '78770,78785p' MON_part1.txt\necho \"=== مسکین ===\"; grep -n \"مسکین\" MON_part1.txt | head -5\necho \"=== تکوین ===\"; grep -n \"تکوین\" MON_part1.txt | head -6\necho \"=== کائنات ===\"; grep -n \"کائنات\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T22:38:24.244Z] TOOL RESULT

```
سکیز: 2 (امص.) جست» آلیز. جفته» 
سکیزه: (0-)6122: (امص.) جست و خیز. 
جفتک‌اندازی. 
سک‌ین: 2112 [عْ.] (.) کارد جاو. 
قلمتراش؛ ج. سکاکین. 
سکینه: (0-)21172و [ع. سکننة معر.] (ا.) 
آرام» آرامش. وقار طماأنینه. آنچه دل را 
قوی گرداند و اطمینان بخشد. (فا.) روح 
القدس» کلمه. 


نگ: ‏ 8 (.) (جان.) بستانداری از راستة 
گوشتخواران که سردستهٌ تیرة خاصی بنام 
تیرةٌ سکگك‌سانان‌می‌باشد. این جانور اهلی و 
دارای دندان‌های آسبای قوی است ولی بر 
خلاف گربه چنگال‌هایش کند و همیشه 
=== مسکین ===
10244:مفلس» مسکین؛ ج. ارامل و ارامیل و اراملة. 
43579:تمسکن: 0 [ع ۰] (مص‌ل.) مسکین 
78732:مسکین شدن (غم.) (امص.) مسکنت» فقر 
89240:حکم شرع به درویش و مسکین دهند در راه 
=== تکوین ===
6856:چگونگی تکوین کرات و اجرام سماوی و 
7511:اجرام سماوی و حوادث جوی تکوین 
7864:اخص از تکوین است زیرا تکوین عبارت از 
34304:تکوین (تورات). ضح.- در قدیم «پیدایی» به 
43010:تکوین: حزبحه) [ع.] (مص م.) هست کردن؛ 
78118:از اجزای تورات: سفر تکوین» سفر 
=== کائنات ===
MON_part1.txt:97742:علامت‌علامات آسمانی: کائنات الجو. " 
MON_part1.txt:98024:(کد.) روشنایی صبح. علم کائنات: (گد) 
MON_part2.txt:15682:قوس قزح: یکی از حوادث جوی (کائنات 
MON_part2.txt:30730:بسیار عمیق باشد. یکی از انوع کائنات جو و
```


## [2026-09-06T22:38:34.814Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY شاد / آشیانه ===\"\ngrep -n \"شاد\\b\\|آشیان\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY latin index ===\"\ngrep -n -i \"SAD\\|ASIYAN\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== CHEUNG *šyaH / šyā ===\"\ngrep -n \"šyaH\\|\\*šiaH\\|šiiā\\|šyā\" CHEUNG.txt | head -10"
}
```


### [2026-09-06T22:38:34.889Z] TOOL RESULT

```
=== ARY شاد / آشیانه ===
994:(حتی انسانهای خوب) پس از مرگك جایی سرد و تاریکك است که در آن نه شادی وجود دارد نه امید.
1641:یونانی (015/0): سس اسلاری کهن (16لاشاد بل#نائل طا0):
2462:گرتبک (007[410): 3 ان لهستانی (ط5/-۳0): هتشاد
3154:لاتین (۸710): شاد د دیا آلمانی کهن (۷ل087014 07 آتز صا0):
3756:‌ ۰ معلی این واژه در زبان لاتین: شاد و خرم کردن.
5064:چم‌های این واژه در زبان‌های این فهرست: جست و خیز» شادی» ورجه ورجه؛ غوکك» وزغ» تند.
5122:ایرندی کهن (لولها 01): 1 4 (38) ات شاد ها
5716:اسلاوی کهن (12اشاد تلعقتانل صام). 599 رو نت
6239:اسلاوی کهن (6اآشاد ۲ع نان صام): برهان قاطع : ۳۳
8318:کردی (8۵1/57). 12 اسلاری کهن (72شاد 2770767 0ا0):
=== ARY latin index ===
183:SFIS a 29h SHUT Obj OF tay gh Sad oy WL] SF alle gy or So
271:22 GS Milne 9 goa slar gel dy Sg sad 990 OU 9 alea o Sealed J bab}
346:99 Saas So gry Syl 29 Fo yh lis) y ate pb Kars y obj op! Sad col
392:“oy BE Sas roe lly piyl oT gb sadly paaia y parglt close »»
453:Yee sad cent hundert honderd hundra
778:Cee SB 9 tla yp gad SlealEl g EF sLils y OLIT JLLt jl sade (4 03» GUTES
822:sceel Ba gd BB+ 58> WOL5 op! 4 DL Some Gar (sade AU Se re
926:Ar dle 92 SCI Furs ily ule yal ply cash gba hl yoo Sight 4 Sadey EL
1010:eel (ALS yy) WIKPOTIS oh sad) 9 by age IS cao b egehh gies 4 Wik what
1177:PS sbagge SSNs Soy Obj sad tate ye OT 32 ET gly yyl y ta peat wb SL
=== CHEUNG *šyaH / šyā ===
29300:*NWIR: Gur. (Kand.) -3y- subj. ‘to collapse, be destroyed’ (in yanät béšyāū ‘Möge
```


## [2026-09-06T22:38:36.292Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB shad / asyan ===\"\ngrep -n \"35\\. \\|767\\. \" HUB.txt | head -10\necho \"=== IEC kwei / SYN ===\"\ngrep -n -i \"quies\" SYN.txt | head -5\ngrep -n -i \"hwilo\\|qui.s.*rest\" IEC.txt | head -5"
}
```


### [2026-09-06T22:38:36.422Z] TOOL RESULT

```
=== HUB shad / asyan ===
605:135. Np. ostdm, ustam *fidus, securus' passt besser zu
1038:235. Horn's Zusammenstellungen sind hochst bedenklich.
1771:435. Lies bal. cot (statt 6ol), Dass es Lehnwort ist, habe
2368:635. Hier fehlt arm. LW. aroir Messing (aus arsacid. *roJ)
2638:735. In den Nachtrftgen wird richtig bemerkt, dass surod
3022:835. Np. Uastan *abnehmen, weniger werden' passt in der
3341:935. Skr. gddhUma^ wird volksetymologische Anlehnung
3577:1035. Das ptc. pass, einer Wrzl. nabh wiirde im Avesta
3911:235. Aus dem A vesta?
5094:§35. Ausnahmen:
=== IEC kwei / SYN ===
25079:W. peidio, through an earlier sense of ‘suffer, endure’ fr. VLat. *patire, Lat. pait id. with development through ‘sub- mit to, acquiesce in’ (attested in Lat.), ‘cease resistance’. Loth, Mots lat. 194.
7646:koquios, io (koquius) “head, knob, topknot, tuft, crest. Cf. WP I, 384 Skt. kacah “head of hair’; cf. kačuh, kacvih (an edible root:colocasia); Arm. koč 'knuckle- bone; ankle; block; name of various plants'; Gk. kóttos 'gaming-die'; kótte “head”; cf. synth. cpd. kóssuphos, kótt- ‘blackbird’; ksu- ló-kotta ‘woodcock’; Mod. Gk. kótsos 'chig- non”; kótsi ‘ankle’; kotsáni “stem, trunk’; Alb. kacé 'corncob', kaga-, in various cpd. names of creatures; Ir. coc ‘tuft, crest, headdress’; W cob, f. ‘tuft beside cop, m. ‘summit’; cobyn ‘tuft, branch’; Pol. kok ‘chignon’; Blg. kok ‘plait’; OCS cf. vrů-koči ‘chignon, plait’; Pol. war-kocz, Cz. vr-koč, id. (see urKs-); Big. koc ‘ankle’; R cf. kocan, kócení “head of cab- bage’. (Note: the Mod. Gk. forms and those of
12141:-om, adverbial extn. to adjectives of type -08, -à, -0m Skt. cf. Sighr-ám, saty-áàm, kàm-am; dhruv-ám; Hitt. hand-an (truly! fr. handas 'true); Gk. mikr-ón, dérón, né-on, etc: Lat. par-um, ver- um; Go. sum-an “formerly; partly) beside -a in alja, iupa, uta, inna, afta, faírra; Sw. inn-an (inside, but for innan ‘before’ see enanti above); undan ‘away’; OCS (and com. SL.) mal-o, nov-o; Li. pirm-a “at first’. A dat. pl. type used adverbially arises in OE hwilom “at times’; Latv. steidzams ‘hastily’
14087:quiëið ‘rest, cease’. WP I, 510. Cf. queil-. (Iranian ambig. cf. qusati-) Av. (ambig.) Say-, v. ‘rejoice’; šāitis, f. joy"; OPer. Siyata-, adj. “peaceful”; Siyàtis, f. ‘peace’; (Alb. cf. (? variant) kuaj, koj, v. “feed — an infant < *queio); Lat. quiesco, pf: quievi, v. “be quiet, cease’, cf. OLat. quies, Lat. quietus, adj. “quiet, tame, content’; quies, gs: quietis, f. ‘repose, inaction, peace’; OCS cf. po-Cijo, -Citi, v. ‘subside, cease, fall asleep’; R po-čiť, inf. “lie, rest’; OCS po-čitije, n. ‘quietude, repose’, fr. *-quietiio-)
14403:rameió ‘quieten, appease, pacify; rest, ac- quiesce, subside’. See following entries. Radi- cal: ram-. WP II, 372 Skt. ramáyami, v. “set at rest; rest, stay, enjoy’; (short grade in) ramáyami, v. “delight? & Av. ram-, v. ‘rest, enjoy oneself; ramaye(imi), v. ‘quieten’; ON róma, v. (1) ‘assent’; roema, v. ‘approve of; Li. romiü, Eti, v. ‘quieten; ac- quiesce' beside roméju, Eti, v. ‘subside’; (short grade in) raméju, eti, v. ‘subside, abate’; Latv. raminat, inf. ‘tame’ beside ràmit, inf. 'cas- trate’. Denom. in Gk. erémázo am deserted'
```


## [2026-09-06T22:38:44.692Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC queil- ===\"\ngrep -n \"queilos\\|queil-\\|queilo\" IEC.txt | head -5\necho \"=== WLD Bd1 p.510 ===\"\ngrep -n \"tranquillus\\|hveila\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T22:38:44.756Z] TOOL RESULT

```
=== IEC queil- ===
13917:queilos, à, is “pause, rest, time, period; leisure, recreation’. WP I, 510 Skt. cf (z-gde) Ciráb, adj. ‘long-standing’; (o- gde) kelih, f. ‘sport’; Oss. cál, Dig. cálá *meal- time; hospitality; Gk. (z-gde) cf. ktílos, adj. (tame, mild”, fr. *d(e)-quil- ?); Alb. sill, m., sillë, cill&, cilë, f. "breakfast, Iunch" 7 Br. pwell, m. (1) (stop, restraint", cf. Lat. tran-quillus, but cf. quieió and cpds.); Go. hweila, OHG hwila, OE hwil, ON hvíla, f. *while, time, period'; OCz. bila, f. ‘time’; cf. Morav. v-číl ‘now’. Cf. quil- (4)
13920:(queiolos, see queilos)
14064:(penis; sic, as Skt.); (Lat., if fr. Umbrian or Oscan (?) pilum ‘javelin’; ambig. < *pil-, peil-); Br. pill, m. ‘chip’; W pill, pl. -ion, m. (2) ‘stem, shaft" (ambig. LW?); Li. kylis, gs: io, m. ‘wedge’; Latv. kilis, id. (NB: much of the evidence for this entry is ambiguous) quilos, à (3) ‘filth’. Cf. quin- (4) Gk. tílos, m. "liquid filth'; tilaí, fpl. 'sweep- ings’; cf. spa-tila, cpd. ‘diarrhoea’; Lat. cf. quis-quiliae, fpi. ‘rubbish’; ster-quilinum, n. *dungheap'; Latv. (?) cila, f. ‘sod, clod' (quilos (4), variant of type queilos, but cf. also quiëðið and cpds.) Cf. Lat. tran-quillus ‘calm’ (but the value of JL is ambig.) quim- ‘tax, payment’. Cf. quiio, quoinà and next Gk. timé, f. “price, value, rank, penalty’; MIr. cím ‘silver tax, tribute’. (Isophonic: Arm. kimk (2) “fancy”; E whim beside ON hvim- leiór, adj. ‘loathsome’ and hvimsi “nonpluss- ed). Verbal extn. in Gk. timáo “value, esti- mate’; Alb. çmoj, v. id. See Supt:Qu quin- (1) ‘quantum, part’. Cf. quoina, quid, etc. Skt. cf. Cinómi, v. (2) ‘amass’; Gk. tíno, v. “pay, repay’; Ir. cf. cion, pl. -ta, m. (1) ‘share’ quin- (2) ‘regard, observe’. Cf. quiió , quí- quëið. (Variant quines-) Skt. Cinómi, v. (1) ‘perceive, search for”; Av. CGinas(mi), 3s. mp: Cista, v. “present, declare, teach’; cf. Cinas, obl: Cináh-, n. ‘desire’; Arm. cf. Knin, s. ‘examination, discussion’; knnem, v. ‘examine, discuss’; Ir. cf. cion, gs: ceana, m. “attention, respect’; Lat. cf. ne-quino Cam unfit, unworthy'. Fest.) l quin- (3) ‘nod, move’. Cf. kin-. (Gk. and SI. evidence ambig.) Gk. cf. (?) tinássō, v. ‘shake, move’; tín-agma ‘move, jolt’; Lat. cf. ocquiniscō, con-°, v. ‘bow — the head’; Cz. (?) čnět, Cnít, v. jut out quin- (4) ‘dirt Gk. pínos, m. id.; cf. pinarós, adj. ‘dirty’; Lat. cf. in-quino, äre beside (Fest.) cünio, ire, v. ‘defile’; Ir. (?) cion, m. (2) ‘sin’; Li. (?) kinis, gs: -io, m. “filthy place, den'; kiné, f. “dry patch in fenland' qui-né (-nə, -n) ‘that not, lest; however,
14087:quiëið ‘rest, cease’. WP I, 510. Cf. queil-. (Iranian ambig. cf. qusati-) Av. (ambig.) Say-, v. ‘rejoice’; šāitis, f. joy"; OPer. Siyata-, adj. “peaceful”; Siyàtis, f. ‘peace’; (Alb. cf. (? variant) kuaj, koj, v. “feed — an infant < *queio); Lat. quiesco, pf: quievi, v. “be quiet, cease’, cf. OLat. quies, Lat. quietus, adj. “quiet, tame, content’; quies, gs: quietis, f. ‘repose, inaction, peace’; OCS cf. po-Cijo, -Citi, v. ‘subside, cease, fall asleep’; R po-čiť, inf. “lie, rest’; OCS po-čitije, n. ‘quietude, repose’, fr. *-quietiio-)
=== WLD Bd1 p.510 ===
32144:-turn „ruhen“, mit Formans - lo - (wie germ. *Jmil-) tranquilus, tranquillus
```


## [2026-09-06T22:38:50.068Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '32130,32160p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T22:38:50.129Z] TOOL RESULT

```
Brugmann BSGW. 41 (1889) 3Gff., Ostlioff BB. 24, 119, Meringer IF. 17, 
155f. — Eine s-Weiterbildung in av. lacs (mit Praeverbien) „struere", 
fra- ..zurichten. bereiten", v7- „zu-, herrichten" (Bthl. Wb. 429 der auch 
gr. rroi'fo- durum aus *iioio-fo- deuten mbchte). 

q“eie- „behaglich ruhen" (q'ioi-, q~7-). 

Ai. cird-m „Z6gern, Verzogerung", cird-h ,,langdauernd, lang - (Osthoff 
MR. IY 151 f.); ap. siyati-s „Wohlbehagen“ (= lat. quits), av. saiti-s „Freude ; ‘ 
(»- = iy-, vgl. gathav. syeitibyo), av. syata-, sata- „erfreut“ (= lat. quietus), 
asiltn- „unfroh‘ : f= lat. inquictus), IJagv-aaTig, av. sdista- „behaglichst, er- 
freulichst" (s. zuletzt Bgm. BSGW. 65, 193), np. sad „f‘roh u , oss. angayun 
..ruhen" fs. zur ar. Gruppe Johansson De der verb. 12, Bgm. II 1 280, Fick I 4 
393, Bthl. Grdr. Phil. I 38); lat. quits, -etis „Ruhe“, quie-sco, -scere, -vi, 
-turn „ruhen“, mit Formans - lo - (wie germ. *Jmil-) tranquilus, tranquillus 
,,ruhig“ (trims in der Bed. von frz. i ires, + q'illos ; s. Yf. LEWb. 2 s. v., 
Bgm. II 2 1, 361); got. heilu, ags. hwll, ahd. ( h)wila „Weile, Zeit“, aisl. 
hvlla „Ruhebett“, hvild „Ruhe“, got. heilan „weilen, zogern, aufhoren", 
ags. Hwada MY, ahd. wllon, -en „weilen, sich aufhalten"; a.ks\. pokojs „Ruhe", 
pokojq, pokojiti „beruhigen, zufriedenstellen“, pocijn , pociti „ruhen“ (slav. 
Zubehor bei Berneker 166, 538 f.). Z. B. Vf. LEWb. 2 u. quits. 

Uber gr. re -tiypai „bin betrtibt" s. aber u, q'iei- „worauf achten". 

q°ek-, q?ok-, q“ek-s- .,erscheinen; sehen; zeigen“. 

Ai. karate ..erscheint, glanzt, leuchtet“ (nicht mit reinem Yelar zu *kok- 
tu-s, s. d.), akacya „im Erschauen", eukaciti, cakagydte „leuchtet, schaut“, 
kaga-h „Sichtbarsein, Schein“; 

av. dkasaf „erblickte“; np. ug/lh „kundig - ‘, niqah „Anblick“ (fiber ai.
```


## [2026-09-06T22:39:06.261Z] TOOL CALL #64: Bash

```json
{
 "command": "ls site/pages/296.jpg 2>/dev/null; pdftoppm -f 296 -l 296 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg296 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T22:39:08.423Z] TOOL RESULT

```
site/pages/296.jpg
total 124904
drwx------ 5 sfmqrb sfmqrb    12288 Sep  6 18:39 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      880 Sep  6 18:36 agents.txt
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
-rw-rw-r-- 1 sfmqrb sfmqrb   332775 Sep  6 18:33 bqtv2_289_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9689 Sep  6 18:33 bqtv2_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   726576 Sep  6 18:33 bqtv2_n289.jpg
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
-rw-rw-r-- 1 sfmqrb sfmqrb    63778 Sep  6 18:33 build290b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68833 Sep  6 18:30 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2612 Sep  6 18:28 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13418 Sep  6 18:28 c_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8430 Sep  6 18:28 c_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11245 Sep  6 18:28 c_katrang.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6717 Sep  6 18:28 c_katvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28872 Sep  6 18:28 c_katvar_zoom.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    51742 Sep  6 18:33 e2.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb    50446 Sep  6 18:33 mk292b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41011 Sep  6 18:29 mk294.py
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
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:33 p290
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
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77133 Sep  6 18:28 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56184 Sep  6 18:39 pg296.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   132637 Sep  6 18:38 sns_n155.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129771 Sep  6 18:38 sns_n156.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   130970 Sep  6 18:38 sns_n90.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   531356 Sep  6 18:38 sns_n90_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   124445 Sep  6 18:38 sns_n92.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   522585 Sep  6 18:38 sns_n92_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   495290 Sep  6 18:38 sns_n92_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   351684 Sep  6 18:35 tad_n59.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   342929 Sep  6 18:35 tad_n59_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   242025 Sep  6 18:34 tad_n60_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   282364 Sep  6 18:34 tad_n60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   335678 Sep  6 18:34 tad_n60_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   276093 Sep  6 18:34 tad_n61.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332662 Sep  6 18:34 tad_n62.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 18:35 tad_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   265879 Sep  6 18:35 tad_n65_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


## [2026-09-06T22:39:12.012Z] TOOL CALL #65: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/296.jpg"
}
```


### [2026-09-06T22:39:12.030Z] TOOL RESULT

```

```


## [2026-09-06T22:39:27.036Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT while/quiet/tranquil ===\"\ngrep -n \"^WHILE\\|^QUIET\\|^TRANQUIL\\|WHILE,\\|QUIET,\\|TRANQUIL,\" SKT.txt | head -10\necho \"=== AFM سكينة / مسكين ===\"\ngrep -n \"سكينة\\|مسكين\\|شكينة\" AFM_pages.txt | head -10\necho \"=== TAD سكينة ===\"\ngrep -n \"سكينة\\|مسكين\" TAD_pages.txt | head -10"
}
```


### [2026-09-06T22:39:27.110Z] TOOL RESULT

```
=== SKT while/quiet/tranquil ===
=== AFM سكينة / مسكين ===
3567:3 | ܐ( )6 تيرد ܥܘ كلد كاه ܐܢܘ مسكين9:4
3657:غيده المخرقة اختلاق التكذب وهي كلمة ܙܝ على الخراق كاك.سكن على المسكين
=== TAD سكينة ===
```


## [2026-09-06T22:39:32.652Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA miskin / sakina ===\"\ngrep -n -i \"miskin\\|miskīn\\|sakina\\|sakīna\\|Sekina\" AFA.txt | head -10\necho \"=== SKT sample headwords ===\"\ngrep -n -i \"^while\\|^quiet\\|^tranquil\\| while\\. \" SKT.txt | head -10\ngrep -n \"TRANQUIL\" SKT.txt | head -5"
}
```


### [2026-09-06T22:39:32.741Z] TOOL RESULT

```
=== AFA miskin / sakina ===
=== SKT sample headwords ===
512:while  of  esff-*^-
```


## [2026-09-06T22:39:38.921Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"tranquillus\" FSD_vol4.txt FSD_vol3.txt WEB_vol1.txt 2>/dev/null | head -5\necho \"--- while ---\"\ngrep -n \"AS. hwil\\|hwil,  time\\|hwil, time\" FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head -5"
}
```


### [2026-09-06T22:39:39.004Z] TOOL RESULT

```
FSD_vol4.txt:38166:Syn  alia},  appeaa  ,   assuage,  calm,  compose,  hush,  lull, moderate,  pacify,  quell,  quiet,  soothe,  still  See  allav  — Ant  agitate,  alarm,  arouse,  disturb,  excite.  Inflame,  rouse, stimulate,  stir  —   tran"qull-l-za'[or  -sa'Itlon,  n   The  act of  tranqulllzlng,  or  the  state  of  being  tranqulllzed  tran"- qull-ll-za'(or  -sa'Iflont  —   tran'qulM2"er  or  -ls"er,  n tran'qull-llz"er  or  -Ils"crt  —   fran'qulI-l2"Ing-[or  -Is"- lng-}Iy,  adp  Jn  a   tranquilizlng  manner,  In  a   manner  calcu- lated to  tranqulllze  tran'quiI-l{z"Jag-ror  -lls"lng-]lj  t. tran-qull'Ii-ty,  1   traij-kwilVti,  2   tr^n-kwll'i-ty,  n   1. The  state  or  quality  of  being  tranquil,  freedom  from or  superiority  to  all  disturbing  influences,  calmness 2   Freedom  from  motion  or  physical  disturbance,  a state  of  rest,  quiet,  as,  the  tranquillity  of  pathless  w   oods [   <   F   tranquillite,  <   L   tranqmlliias,  <   tranquillus, quiet  ]   Syn  see  calmness,  rest tran-qull'lu,  1   tran-kwll'lo,  2   tran-kwil'lc  a   &,  adc  [It  J Mus  Tranquil  tranquilly  a   direction  to  the  performer trans-,  1   trans-  or  tranz-,  2   trans-  or  tran^-,  prefix Used  chiefly  in  words  of  Latin  origin  It  denotes  (1) over,  across,  beyond,  through,  as  designating  relatively position  or  place,  as  In  transmit,  transler,  transplant, traiwcend,  etc  ,   (2)  absolute  change,  as  In  tratisform,  lrans~ substantiate,  etc  ,   (3)  tiansversely,  crosswise  or  across  In some  scientific  or  technical  terms,  as  In  tran^frontal,  trans- process,  tran^ductor,  tranmcdian  It  is  an  English  forma- tive, as  In  tran^earth,  tranAv lew,  etc,  and  Is  used  also with  adjectlv  es  of  place  In  opposition  to  cis-  w   1th  the  mean- ing •*  across  ”   or  *   to  the  other  side  of  **  as  In  tran^mundane, transpontine  etc  In  organic  chemlstrj  It  Is  used  as  a   desig- nation or  Indication  of  an  allolsomcrlc  compound  in  which si  ntiar  groups  arc  on  opposite  sides  of  the  doubly  linked carbon  atoms,  as,  trans-ethylene-dlcarboxyllc  acid  (fumarlc acidj  (COiHjCH
--- while ---
FSD_vol4.txt:55399:WMch  was  formerly  used  merely  to  introduce  a   relative clause,  and  was  followed  by  a   personal  pronoun  In  the  body of  the  clause  as  the  man  which  misfortune  had  Impover- ished him  The  dialectic  use  of  which  is  an  Introductory expletive,  or  as  an  equivalent  to  and  (as  in  which  I   wish  to remark”),  may  be  traced  to  this  origin  [<  AS  hwilc, which,  <   hwd,  who,  -r  die,  -Ij  ]— the  which  [Archaic], same  as  which  (relatlv  e   pronoun)  with  Increased  definite- ness of  reference  w.  Is  w.?  which  Is  the  person  or  thing mentioned  or  Intended’  a   form  of  asking  for  definite  dis- tinction and  description  of  one  individual,  or  more  than  one, among  two  or  more
```


## [2026-09-06T22:39:44.030Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=356 && NR<=360 {print \"=== block \"NR\" ===\"; print substr($0,1,300)}' FSF_pages.txt\necho \"== total blocks ==\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' FSF_pages.txt"
}
```


### [2026-09-06T22:39:46.912Z] TOOL RESULT

```
=== block 356 ===
                                            ‫‪"ar‬‬                                         ‫کاربند‬


                                  ‫کارگاه‪:‬‬         ‫(سیاست‌نامه ‪ :)۸۵‬پادشاه بیدار است و به‬
        ‫چگوشتاسپ آ
=== block 357 ===
                                             ‫‪"ar‬‬


                                        ‫کاف‬               ‫دگر گفت کاری گران آورید‬
        ‫اح)‪:‬‬
           ‫شکاف تراک (لغت فصرحس»‬                   ‫گچ و خشت و
=== block 358 ===
                                               ‫‪raf‬‬                             ‫کافته‪ .‬کفته‪ .‬کنیده‬

  ‫تا ای خو چاو‬                   ‫چک‬
                                  ‫کی‬                            ‫من اکنون ز طب
=== block 359 ===
‫کام‬                                         ‫‪۳۵۵‬‬


‫[هدیة فراوان] فرستاد نزدیک دستان سام‬                                    ‫می‌گوییم‪ :‬برادر تنی‪:‬‬

 ‫که خلعت مرازین فزون بودکام‬       
=== block 360 ===
                                            ‫‪۳۵٦‬‬                                         ‫کام‪‎‬‬



‫ز پیش بودم بیمو اميد دشمن و دوست‬                       ‫تناز خوی پرآب و همهکام خاک‬
‫به رنج دوستم اکن
== total blocks ==
484
```


## [2026-09-06T22:40:00.150Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/quiet",
 "prompt": "Give the etymology of 'quiet' (n./adj.) and any note on 'tranquil': Latin quies/quietus, PIE root, and Old Persian/Avestan cognates if mentioned."
}
```


## [2026-09-06T22:40:01.496Z] TOOL CALL #71: WebSearch

```json
{
 "query": "حسن‌دوست ریشه‌شناسی آشیان آشیانه فارسی میانه āšyānag اوستایی šay- خانه"
}
```


### [2026-09-06T22:40:06.366Z] TOOL RESULT

```
# Etymology of "Quiet"

## Noun and Adjective

**Quiet (n.)** dates to c. 1300, derived from Old French *quiete* and Latin *quies* (genitive *quietis*), meaning "rest, repose, peace." The adjective form emerged in the late 14c. from the same Latin root *quietus*, meaning "calm, at rest."

Both trace to the PIE root **\*kweie-**, defined as "to rest, be quiet."

## Latin Origins

The etymological entry states: "from Latin *quies* (genitive *quietis*) 'a lying still, rest, repose, peace' (from PIE root \*kweie- 'to rest, be quiet')."

## Note on "Tranquil"

The page's related-words section indicates *tranquillitas* (Latin) shares conceptual ground with *quiet*, though it derives from *tranquillus*, likely combining *trans-* with an adjective from the same PIE root \*kweie-.

**Cognates from Old Persian or Avestan are not mentioned** in the provided content.
```


### [2026-09-06T22:40:10.522Z] TOOL RESULT

```
Web search results for query: "حسن‌دوست ریشه‌شناسی آشیان آشیانه فارسی میانه āšyānag اوستایی šay- خانه"

Links: [{"title":"ریشه‌شناسی عامیانه - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C_%D8%B9%D8%A7%D9%85%DB%8C%D8%A7%D9%86%D9%87"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"حسن‌دوست: نوشتن «فرهنگ ریشه‌شناختی زبان فارسی» 16 سال زمان برد - ایبنا","url":"https://www.ibna.ir/news/232985/%D8%AD%D8%B3%D9%86-%D8%AF%D9%88%D8%B3%D8%AA-%D9%86%D9%88%D8%B4%D8%AA%D9%86-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-16-%D8%B3%D8%A7%D9%84-%D8%B2%D9%85%D8%A7%D9%86-%D8%A8%D8%B1%D8%AF"},{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"},{"title":"کتاب فرهنگ ریشه‌شناختی زبان فارسی (جلد 5)","url":"https://fanuus.org/library/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-5/"}]

Based on the search results, I found relevant information about Mohammad Hasandoust and his etymological work on Persian:

Mohammad Hasandoust is a researcher and specialist in ancient Iranian languages, and an affiliated professor at Shahid Beheshti University.

Hasandoust is the author of "Farhang-e Riešhešenāxti-ye Zabān-e Fārsi" (Etymological Dictionary of Persian Language), which was published in five volumes in 1393 by the Academy of Persian Language and Literature. The book was recognized as a selected work in the thirty-third edition of Iran's Book of the Year award in the "Ancient Languages" category.

Previously, in 1383, the first volume of a dictionary with the same name, authored by Hasandoust and containing the letters "Ā – T," was published by the Academy of Persian Language and Literature.

The main text of the Etymological Dictionary of Persian contains 2,955 pages across volumes one through four, with 5,514 entries.

This comprehensive etymological dictionary represents significant scholarly work on the historical roots and linguistic development of Persian vocabulary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T22:40:19.011Z] TOOL CALL #72: Bash

```json
{
 "command": "grep -n \"ʾhyʾng\\|ahyanag\\|āhyānag\\|hyʾng\" /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dmmpp.txt | head -5"
}
```


### [2026-09-06T22:40:19.056Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:40:26.621Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7yeh%E2%82%81-\" \\\n \"https://www.etymonline.com/word/while\" \\\n \"https://www.etymonline.com/word/quiet\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B4%DB%8C%D8%A7%D9%86%D9%87\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 296 (book 266), roots Kweye/Qweye and K.w.n — verification of PIE *kʷyeh₁- 'to rest', Lat. quies/tranquillus, Gmc *hwīlō>while, OP šiyāti->NP šād, and NP āšiyāne\" 2>&1 | tail -3\ndone"
}
```


### [2026-09-06T22:40:30.297Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5980e08cafa41299.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f2474957a6281bc1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06c2172b62476ca9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/40092241ed204015.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6755bad55ff76f92.txt
```


## [2026-09-06T22:40:36.597Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D9%83%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%83%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%83%D9%8A%D9%86%D8%A9\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D9%83%D9%8A%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D7%A9%D7%9B%D7%99%D7%A0%D7%94\" \\\n \"https://www.balashon.com/2020/06/shechinah-and-scene.html\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 296 (book 266), root K.w.n — Semitic k-w-n / s-k-n, Arabic makan/takwin/sakina/miskin, Hebrew shekhinah\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T22:40:41.322Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1da60372d70a48bc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/34f05201cfb6f1c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/97d1b4ecc319518b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ccfa0a38e661fd11.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5da3e1693b8b883a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f44d98f60d94774c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/33e0ba0fff1f894b.txt
```


## [2026-09-06T22:40:44.526Z] TOOL CALL #75: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T22:40:44.563Z] TOOL RESULT

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


## [2026-09-06T22:42:08.896Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk -v N=930 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | head -c 2200\necho; echo \"=== search sayana ===\"\ngrep -n \"sayana-\\|äayana\\|Sayana\" BRT.txt | head -5\necho \"=== KLN_1966 last leaf ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==903' KLN_1966.txt | head -c 300"
}
```


### [2026-09-06T22:42:10.887Z] TOOL RESULT

```
imqmtqmaiwihalmwrya  »  \.  ia  ..  vupa  dämqn  paifi.vamai  »»So
(sd.)  saranamya  V.2. 10.  ^dus.cihrayä  Yt  79.94.
Ans  ar. Viit«-,  u-'Erweitening'  (Praes.  ao)  zu'  i--a_  \   ■        ■*         oit   u
ai.  iai-  V.  -schneiden'.    -    PQ.:  an  fn  JmTi   *   J-.   E-    äolSra-  n.    i)   im   jAw.   -Wohn-
lu/t  (s.  Dp.  luj/an)  Ja  türäiSmaaä  i  iorren.        platz,   Heimslätte':  >a*J/   'raAe   boxtSmn
.  j.  Sä-   ,)   Adj.  (auch  fem.)  'froh,  sich  /Ü-Zrl«  Yt  Ä  i ;  ~  <W«Ä  -r^paitim..
behaglich  fühlend':  n^,V  ^r  r«  zä  /J  (NSf.)  -^'"'  '"*«"'«  «''^?"'  ^'^^  '^'  "  '"''''"^;
>J   darrra  akarsta  säm  "denn  nicht  -^^nqm  yü^anqm  'ranam  ..  masyän^m  Yt.
die  Erde  froh,  die  lang  ungepflügt  dalag"  1  '^^^'  "  /'  ""f     '"'l^^.^  ,  *^  '."'"^
V.J.  .4-  >)  f.  'Freude.  Behafen'  (n^  "^^^    V'"    ^^^UZ\  ^<*^*->=  .^'*"^'
Komp.).  [N.  wi:  lies  /a,y>^-]  ^f«f  •'*''  »«S;« (DS.) ",  W  ««A  -r^^^a
KompE.  —   Zum  V.  Syä-.  -  VgL  iäüla-.  -    (LS-)-  asanhatca  -rOatca,  Oia. .  'ra,  asasfa
Fa.:  Aa^ an  i  äiänTA.  ,TJs^a,    asavAqmca    'ranqmca.  a)    im
j.  iäimnö  H.  j^:    ».  anva /rahiimna-,    Sp.   gA\?.  'Landkreis,  Gau"';  *3  sl  d»min»m
1008.  ;'j»M  »3  •«/«  iiJ  dahyum  vä  ädät  duntä-
•  j,  SäJsta-  Adj.  'der  erfreulichste,  behag- '  (sd.)i5l..  Y.J/.  r8;  —  d»manaAyä  xsa^r?m lichste':  kva  paoirlm  atAhh  s>tnS  't^m  ^•rahyj  va  dahy^s  va  Y. j/.  16;  —  at (NSn.)  "wo  auf  dieser  Erde  ist  es  erstens  '  tsi^  drsgva  . .  ga  frdntdis  (sd.)  'rakyJ  vJ am  behaglichsten?"  V.j.i.  \dahySul vä  Y.4ÖI4.
KompE  —  Sapeil.  ta  sä-.  —  Aus  ar. ' k'iä',  i]istha- 1  KompA.,  E. ;  Ableit.  —  Zom  V.  Say:  —  aL (S  Sr),  lum  VtM%.*Xiäiati;  Bthl. IF./.''73.  —  ,  ii/lta-  n.  —  Pü.:  reiiutäi,  {lu  i):  trtnsskr. Pü.:  tu  /ralum  in  tamU  äiinlum,  erl.:  6u  ,  (sii!r)i),  Sü,  (überall):  deiai.  —  ')  Uathem., minük  i  samii  äsin'ih  hal  ci  vii.  1      an  ataiihalt'a  angeglichen.  —  ')  Sva.  im  jAw.
.  j.  säta-  Adj.,  PPfP.:  s.  iyä
=== search sayana ===
3922:•  j,  aiwi-sayana-  n,  'Bewohaen':  yaha . .  *aiwUayama  darr/a  -na  . .  b>nymyS.- siabm  (sd.)  H\.to.^^.
5583:•  j.  airyö.sayana-  n. 'arischer  Wohnsitz,  .j^g. aurvant-, aourvant-" Adj. 'schnell; W.  der  Arier':  vJspjm  .  .  'fvm  Yt  10.  13.  tapfer,  Held':  '7-at"  F.  7;  —  /laomo  aeibis
10175:•  j.  gav-a'äayana-  Adj.  'die  Wohnstätte [  der  Rinder  bildend,  von  Rindern  bewohnt':
13334:Komp.:  *däi(yi.iipa'sayana- Adj.-'t-iat^ ;  S  z6j, —  ^upa-sayana-  n.,  znm  V.  liy-l  ii.  itiyaiia-. n.  —  V&.:däiaa/>aiihi{i)iavc;  Npä.:  6a  ulirüA pusß  bid,  mit  der  Etl.  1  ka  fas  az  vaki  1  afriix- lan  läaim  nihatid  an  puiS  ('Uoterslüliung').
13812:*>   Vgl.    Bd.  74-  19:    J'^a^   (in    Aw.-Buchst.) i/  xärpuSt   (=  np.  xStpasi  'Igel')  i^änend',    lg. £Ü    gilt    der    Igel    als    .ipezi elter   Gegner    der Ameisen ;  iäiak  fa  AamislJriA  1  mör  i  i/änai  t:s da    eslel,    H^ön   xdwet   ku    iälai    Aar  *iärak  *i  1 andar  mar  xSHoi  i  mizet  (ü)  lOCO  mar  iaHft. KorapA.   —   Et.?    Vgl.    HORN   KZ.  J^.  437, 1 HBM.AGT.AI4l.VI!.Va/+»fl*fl.'derRch]imme Haken  (Stacheln)  hat'7  -  mp.  (Pü.):  iüSal;  np.  I £uia;  A3;similation  der  silbenanl.  Kons. ■  j.  duzakö.sayana-  Adj.  'wo  der  Auf- enthalt, dieHeimat  desIgels  isf :  i'alk^ntim (sd)  yim  -mm  V,  /.  9.
=== KLN_1966 last leaf ===
��true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) .
veratral,  n.,  the  radical  C9H10O4  (chem.)  —  Form¬ ed  with  adj.  suff.  -al  fr.  L.
```


## [2026-09-06T22:49:14.817Z] TOOL CALL #77: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p296 && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p296/build.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Kweye, Qweye\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *kʷyeh₁- (older notation *kʷei̯ə-, *kʷi̯ē-) 'to rest, be quiet, be at ease'\",\n \"note\": (\"The root box is copied almost verbatim from Klein: s.v. 'while' Klein posits 'I.-E. base *qʷeye-, \"\n          \"*qʷi(y)e-, to rest, repose, be comfortable' — hence Nourai's twin heading 'Kweye, Qweye' and the \"\n          \"gloss 'quiet, comfortable'. Pokorny 638 has the same root as kʷei̯ə-, kʷi̯ē- 'behaglich ruhen' with \"\n          \"the derivatives kʷi̯ē-t-s 'Behagen', kʷi̯ē-to-s 'froh', kʷi-lo- 'ruhig'; Watkins/AHD lists it as \"\n          \"kʷeiə-² 'to rest, be quiet' [Pok. kʷeis- 638]; current Wiktionary writes it *kʷyeh₁-. Root, \"\n          \"language label and gloss are all correct. The only weak point on this chart is the word \"\n          \"'â-šyâ / âšîyâneh' (nodes 1 and 2): the rest of the tree (Lat. quiēs/tranquillus, Gmc. *hwīlō > \"\n          \"while, Av. šyāta-/OP šiyāti- > NP šād) is textbook.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *kʷyeh₁- «آرمیدن، آسودن، در آسایش بودن» (در نگارش کهن‌تر *kʷei̯ə-/*kʷi̯ē-). \"\n             \"پوکورنی (ص ۶۳۸) آن را kʷei̯ə- «به آسودگی آرمیدن» می‌آورد و واتکینز در پیوست فرهنگ American Heritage \"\n             \"همان را kʷeiə-² «آرمیدن، آرام بودن» ثبت کرده است. صورت دوگانهٔ «Kweye, Qweye» و معنای «quiet, comfortable» \"\n             \"را نورایی عیناً از کلاین (ذیل while) گرفته است. ادعای نورایی دربارهٔ خودِ ریشه و برچسب زبانی و معنا درست است؛ \"\n             \"تنها نقطهٔ سست این نمودار واژهٔ «آشیانه» است (گره‌های ۱ و ۲).\"),\n \"sources\": [\n   W+\"Reconstruction:Proto-Indo-European/k%CA%B7yeh%E2%82%81-\",\n   \"https://www.etymonline.com/word/quiet\",\n   \"https://www.etymonline.com/word/while\",\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:638\", \"status\": \"supports\",\n    \"note\": (\"POK_02.txt leaf 294/295 (printed p.638): 'kʷei̯ə-, kʷi̯ē- „behaglich ruhen“, kʷi̯ē-t-s \"\n             \"„Behagen“, kʷi̯ē-to-s „froh“, kʷi-lo- „ruhig“ … apers. šiyāti-š \"\n             \"„Wohlbehagen“ (= lat. quies), av. šāiti-š „Freude“ …, av. šyāta-, šāta- \"\n             \"„erfreut“ (= lat. quietus) …, np. šād „froh“ … lat. quies, -etis „Ruhe“ … \"\n             \"mit Formans -lo- (wie germ. *hwil-) tranqui(l)lus … got. hveila, ags. hwīl, ahd. (h)wīla \"\n             \"„Weile, Zeit“'. Grep pattern: grep -n 'tranquillus' POK_02.txt (line 4715).\"),},\n   {\"ref\": \"KLN:1740\", \"status\": \"supports\",\n    \"note\": (\"The local KLN_1966.txt scan stops at 'veratral' (leaf 903), so the entry was read in the \"\n             \"one-volume 1971 edition, KLN_1971.txt line 266588 s.v. 'while, n.': 'fr. OE. hwil … Goth. \"\n             \"hveila, ‘space of time, while’, orig. ‘rest’, ON. hvila, ‘bed’ (lit. \"\n             \"‘resting place’), hvild, ‘rest’, fr. I.-E. base *qʷeye-, *qʷi(y)e-, ‘to rest, \"\n             \"repose, be comfortable’, whence also Avestic shaitish, ‘joy’, OPers. shiyatish, \"\n             \"‘joy’, L. quies … tranquillus'. That is Nourai's root box word for word; p.1740 of the \"\n             \"1966 two-volume edition is the 'while' page (leaf 762 of KLN_1966.txt = printed p.1433, \"\n             \"two printed pages per leaf, checked against 'Shekinah' below).\"),},\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 510\", \"stance\": \"supports\",\n    \"note\": (\"WLD_Bd1_1930_dli_70244_djvu.txt line 32134ff.: 'qʷeie- „behaglich ruhen“ (qʷiei-, qʷī-). \"\n             \"Ai. cirá-m …; ap. šiyāti-s „Wohlbehagen“ (= lat. quies), av. šāiti-s „Freude“ …, \"\n             \"np. šād „froh“ …; lat. quies, -etis „Ruhe“ …, mit Formans -lo- (wie germ. *hwil-) \"\n             \"tranquilus, tranquillus …; got. hveila, ags. hwīl, ahd. (h)wīla „Weile, Zeit“'. \"\n             \"Pokorny 638 is a verbatim reprint of this.\"),},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kʷeiə-²\", \"stance\": \"supports\",\n    \"note\": (\"AHD_watkins1985.txt line 650: 'kʷeiə-². To rest, be quiet. I. Suffixed zero-grade variant form \"\n             \"*kʷi-lo- … 1. Germanic *hwīlō in: a. Old English hwīl, while: WHILE … 2. Possibly Latin \"\n             \"tranquillus, tranquil … II. Variant form *kʷyē- (< *kʷyes-) in Latin quiēs, quiet … \"\n             \"[Pok. kʷeis- 638.]'\"),},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. quiēiō / queilos\", \"stance\": \"supports\",\n    \"note\": (\"IEC.txt line 14087: 'quiēiō “rest, cease”. WP I, 510. Cf. queil-. Av. šay-, v. \"\n             \"“rejoice”; šāitis, f. “joy”; OPer. šiyāta-, adj. “peaceful”; šiyātis, f. \"\n             \"“peace”; … Lat. quiēscō … quiēs … OCS po-čijǫ'; and line 13917 'queilos … Go. hweila, \"\n             \"OHG hwīla, OE hwīl, ON hvíla … cf. Lat. tran-quillus'.\"),},\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Avestan / Old Persian\",\n \"words\": \"šâ 3, šyâ 2; â-šyâ; šâiti 2, šyâtî\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n   \"Two of the three items are exactly right, the middle one is not. (a) 'šâ 3, šyâ 2 to rest' = \"\n   \"Bartholomae's Av. verb 'g. šyā-, j. šā- „sich freuen“' (AiW col. 1715f.), a set root with \"\n   \"present šā-/šyā-, PPfP. šyāta-/šāta-, Inf. šāitī/šāitē; Gathic keeps the -y- (šyeitibyō), Younger \"\n   \"Avestan simplifies šy- > š-, whence Nourai's homonym numbers. (b) 'šâiti 2, šyâtî: happiness, peace' = \"\n   \"Av. šāiti- f. / Gathic šyātay- 'Freude, Wohlbehagen, Glück' (AiW 1717) and OP šiyāti- f. 'happiness' \"\n   \"(Darius, DNa/DSf 'hya šiyātim adā martiyahyā “who created happiness for man”'), plus the adj. \"\n   \"OP šiyāta-. Both go back to *kʷyeh₁-ti- / *kʷyeh₁-to- and are the exact equations of Lat. quiēs and \"\n   \"quiētus (Pokorny 638). (c) 'â-šyâ: resting place, nest' is NOT an attested Avestan or Old Persian word: \"\n   \"Bartholomae's Avestan lexicon has no ā-šyā-; the nearest thing is the infinitive ā-šāite 'sich zu \"\n   \"freuen, behaglich zu fühlen' (AiW col. 349, Ā.4.6), which means 'to rejoice', not 'nest'. Nourai has \"\n   \"back-formed it from Horn's suggestion (Grundriss no. 35) that NP āšyāne = 'ā- + Av. √šō- resp. Gathic \"\n   \"šyā- “to rest”, or perhaps already “to dwell”', a suggestion Horn credits to a verbal \"\n   \"communication from Nöldeke and immediately qualifies ('aber das y ist auffällig'). The word \"\n   \"'dwelling, nest' in fact belongs to Bartholomae's other, homophonous root šay- 'wohnen' (AiW 1704ff., \"\n   \"whence šayana- n. 'dwelling', šiti-, šōiθra- 'Wohnplatz', Arm. šēn) — a different PIE root — so this \"\n   \"third item is disputed and drags the node's verdict down.\"),\n \"derivation_fa\": (\n   \"دو جزء از سه جزء این گره درست است. نخست، «šâ ۳، šyâ ۲» همان ستاک اوستایی šyā-/šā- «شادمان بودن، آسودن» \"\n   \"است که بارتولمه در فرهنگ ایرانی باستان (ستون ۱۷۱۵ به بعد) با صفت مفعولی šyāta-/šāta- و مصدر šāitī آورده است؛ \"\n   \"در گاهانی -šy نگه داشته می‌شود و در اوستایی متأخر به -š ساده می‌شود. دوم، «šâiti ۲، šyâtî» همان šāiti-/šyāti- \"\n   \"اوستایی «شادی، آسایش» و šiyāti- پارسی باستان (در سنگ‌نبشته‌های داریوش: hya šiyātim adā martiyahyā) است که \"\n   \"با quiēs و quiētus لاتین دقیقاً برابر است. اما جزء سوم، یعنی «â-šyâ به معنی جایگاه آرمیدن، آشیانه»، واژه‌ای \"\n   \"اوستایی یا پارسی‌باستان نیست و در فرهنگ بارتولمه چنین صورتی وجود ندارد؛ نورایی آن را از حدس هرن (بند ۳۵) \"\n   \"بازسازی کرده که خود هرن آن را از قول شفاهی نُلدکه آورده و بی‌درنگ تردید کرده است («اما این y جای شگفتی دارد»). \"\n   \"مفهوم «خانه و آشیانه» در واقع به ستاک همنام دیگری، یعنی šay- «سکونت گزیدن» (بارتولمه ستون ۱۷۰۴ به بعد، \"\n   \"با مشتقات šayana- «جایگاه»، šōiθra- «شهر، جایگاه»، ارمنی šēn) می‌رسد که ریشهٔ هندواروپایی دیگری دارد. \"\n   \"بنابراین این جزء پذیرفتنی نیست و حکم کل گره را «رد شده» می‌کند.\"),\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/k%CA%B7yeh%E2%82%81-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:638\", \"status\": \"supports\",\n    \"note\": (\"Pokorny p.638 lists 'apers. šiyāti-š „Wohlbehagen“ (= lat. quies), av. šāiti-s \"\n             \"„Freude“ (š- = šy-, vgl. gathav. šyeitibyō), av. šyāta-, šāta- „erfreut“' — \"\n             \"supports (a) and (c=šāiti/šyāti) but says nothing of any ā-šyā- 'nest'.\"),},\n   {\"ref\": \"KLN:1740\", \"status\": \"partial\",\n    \"note\": (\"Klein s.v. 'while' cites 'Avestic shaitish ‘joy’, OPers. shiyatish ‘joy’' only; \"\n             \"no verb 'to rest' form and no ā-šyā-.\"),},\n   {\"ref\": \"KNT:210\", \"status\": \"partial\",\n    \"note\": (\"Kent's Old Persian lexicon: printed p.210 (KNT.txt leaf 225) is the b-/m- stretch (brātar-, \"\n             \"brazmaniya-, mā-, magu-), so the page number is off by a few; šiyāti- itself is attested in \"\n             \"Kent's texts (KNT.txt line 4082 'duvaištam šiyātiš axšatā hauvai', line 4518 DNa/DSf 'hya \"\n             \"šiyātim adā martiyahya'). The OP word Nourai wants is real and in Kent, but not on p.210.\"),},\n   {\"ref\": \"ZFS:51\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Zaban-e Farsi va Sargozasht-e An — no digital copy on any permitted platform (refs_online.json: 'Not found').\"},\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1715f., 1717; cf. col. 1704ff. and col. 349\", \"stance\": \"partial\",\n    \"note\": (\"BRT.txt leaf 933: 'g. šyā-, j. šā- V. „sich freuen“. Praes. 1 š(y)ā-. — PPfP. šyāta-, \"\n             \"šāta-; Inf. šāitī, šāitē' and 'g. šyātay-, j. šātay- f. „Freude, Wohlbehagen, Glück“'; \"\n             \"leaf 929: 'j. šā- 1) Adj. „froh, sich behaglich fühlend“ … Zum V. šyā-'. But leaf 928 \"\n             \"has a SEPARATE root 'j., g. šay- V. „wohnen“' with šōiθra- 'Wohnplatz, Heimstätte', \"\n             \"šiti- Inf. 'zu wohnen' and the compounds airyō.šayana- 'arischer Wohnsitz' (line 5583), \"\n             \"aiwi-šayana- 'Bewohnen' (line 3922). There is no ā-šyā- 'nest' anywhere in Bartholomae; only \"\n             \"'j. ā-šāite Inf. „sich zu freuen, behaglich zu fühlen“' (line 6362).\"),},\n   {\"src\": \"KNT\", \"where\": \"Old Persian texts, DNa 1-8 / DSf\", \"stance\": \"supports\",\n    \"note\": (\"KNT.txt line 4518: 'baga vazraka Auramazdā hya imām būmim adā hya avam asmānam adā hya \"\n             \"martiyam adā hya šiyātim adā martiyahyā' — OP šiyāti- 'happiness' confirmed.\"),},\n   {\"src\": \"HRN\", \"where\": \"no. 35, p. 9 (Nourai cites p.6)\", \"stance\": \"partial\",\n    \"note\": (\"HRN.txt leaf 31 (printed p.9): '35. āsyāne, āsyān ‚Nest‘. a + aw. √šō- bezw. gāth. \"\n             \"šyā- ‚ruhen‘, oder wohl bereits ‚wohnen‘ (Nöldeke, mündliche Mitteilung). \"\n             \"Aber das y ist auffällig, vergl. np. šād.' — this is where Nourai's ā-šyā comes from, hedged \"\n             \"by Horn himself.\"),},\n ],\n})\n\ne0[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"ašîyâneh «آشیانه»; šâd «شاد» (+ آشیان ؛ شادی ، شادمان)\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n   \"شاد is confirmed beyond doubt; آشیانه is not. (1) NP šād 'happy' < MP šād (Book Pahlavi šʾt', \"\n   \"Manichaean MP/Parthian šʾd, Pāzand sād) < OP šiyāta- / Av. šyāta- 'pleased' < Proto-Iranian *šyāHta- < \"\n   \"PIE *kʷyeh₁-to-s; intervocalic Old Iranian -t- after a long vowel voices to -d- in New Persian \"\n   \"(MP šāt > NP šād), exactly as in Nyberg's entry 'šāt ‘glad, happy’ — Av. (1716) šyāta-, šāta-; \"\n   \"OP šiyāta- ‘peaceful, happy’, šiyāti- ‘peace, happiness’; MPrth/MPrs šʾd; Paz. sād; NP \"\n   \"šād'. The derivatives شادی (< MP šādīh) and شادمان (< MP šādmān, with the -mān suffix) follow \"\n   \"regularly. (2) NP āšiyān(e) 'nest, roof-space' is a different problem. Horn (no. 35), on Nöldeke's \"\n   \"oral suggestion, analysed it ā- + šyā- 'to rest', and Nourai follows him; but Horn flagged the -y- as \"\n   \"anomalous and himself asked (no. 1034b, s.v. nišēm 'nest') whether āšyāne does not rather belong with \"\n   \"nišastan. Mo'in's own etymological footnote in the very Borhān-e Qāṭeʿ page Nourai cites (vol. 1, \"\n   \"p. 46 s.v. آشیان) derives it 'from the prefix ā- + šyāna meaning place, dwelling; Armenian šēn \"\n   \"‘village’ — Bartholomae 1707', i.e. from Av. šay- 'to dwell' (šayana- n. 'dwelling'), a wholly \"\n   \"different root. Nyberg goes further: Book Pahlavi *āyiyān(ag) 'a bird's nest' is 'MPrth ʾhyʾng = \"\n   \"āhiyānag ‘nest’ < *āθiyān-, borrowed in SW and subjected there to the usual alternation -h- : \"\n   \"-y-. The genuine SW form is found in NP āšyānah < *āθyāna-, with -θy- in contactual position > -šy-' — \"\n   \"a Parthian h- that a *šy- of the 'rest' root could never yield. Nourai's own chart note ('See \"\n   \"“Gwhen 1” for another possible root') shows he knew the word was contested; the modern \"\n   \"preference (Mo'in, Bartholomae, Nyberg) is against the *kʷyeh₁- route, so the word is disputed.\"),\n \"derivation_fa\": (\n   \"«شاد» بی‌گمان درست است، «آشیانه» نه. یک: فارسی نو «شاد» از فارسی میانهٔ šād (پهلوی کتابی šʾt'، \"\n   \"پارتی و فارسی میانهٔ مانوی šʾd، پازند sād) و آن از šiyāta- پارسی باستان و šyāta- اوستایی «شادمان» است، \"\n   \"از ایرانی آغازین *šyāHta- و در نهایت از *kʷyeh₁-to-s هندواروپایی؛ ت پایانیِ فارسی میانه پس از واکهٔ بلند \"\n   \"در فارسی نو به د نرم شده است (šāt > šād). نیبرگ (واژه‌نامهٔ پهلوی) همین را می‌گوید و به ستون ۱۷۱۶ بارتولمه \"\n   \"ارجاع می‌دهد. «شادی» از šādīh پهلوی و «شادمان» از šādmān پهلوی نیز قاعده‌مندند. دو: اما «آشیان/آشیانه» \"\n   \"مسئله‌دار است. هرن (بند ۳۵) به نقل شفاهی از نُلدکه آن را «آ + شیا (آرمیدن)» گرفته و نورایی همان را آورده، \"\n   \"ولی خود هرن به ناهمخوانی y اشاره کرده و در بند ۱۰۳۴ب (ذیل نشیم) پرسیده که آیا آشیانه به «نشستن» بازنمی‌گردد. \"\n   \"معین در همان صفحهٔ برهان قاطع که نورایی بدان ارجاع داده (ج ۱ ص ۴۶) در حاشیه می‌نویسد: «مرکب از پیشوند آ و \"\n   \"šyāna به معنی جای و سرای، ارمنی šēn (به معنی ده، قریه)، بارتولمه ۱۷۰۷» — یعنی از ستاک اوستایی šay- «سکونت \"\n   \"گزیدن». نیبرگ نیز صورت پهلوی را *āyiyān(ag) خوانده و آن را با āhiyānag پارتی از *āθyāna- دانسته است؛ صورت \"\n   \"پارتی با h هرگز نمی‌تواند از *šy- ستاک «آرمیدن» بیاید. خود نورایی هم در یادداشت نمودار به ریشهٔ دیگری \"\n   \"(Gwhen 1) اشاره کرده است. پژوهش امروزی (معین، بارتولمه، نیبرگ) ریشهٔ *kʷyeh₁- را برای «آشیانه» رد می‌کند.\"),\n \"sources\": [W+\"%D8%B4%D8%A7%D8%AF\", W+\"%D8%A2%D8%B4%DB%8C%D8%A7%D9%86%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:6\", \"status\": \"not_found\",\n    \"note\": (\"HRN.txt leaf 27 = printed p.6 carries entries 17-21 (ārey, āz, āzād, āzār, āzmūdan) — nothing \"\n             \"relevant. The entry Nourai means is Horn no. 35 'āsyāne, āsyān ‘Nest’' on printed p.9 \"\n             \"(leaf 31). Page number miscited by three.\"),},\n   {\"ref\": \"HRN:169\", \"status\": \"supports\",\n    \"note\": (\"HRN.txt leaf 190 = printed p.169, no. 767: 'šād ‚fröhlich, heiter‘, šādī. ap. šiyāti- \"\n             \"‚Behagen, Freude‘; aw. šāiti-; phlv. šāt, šātīh; lat. vergl. quietus, quies.' Exactly \"\n             \"Nourai's arrow.\"),},\n   {\"ref\": \"BQT:46\", \"status\": \"contradicts\",\n    \"note\": (\"BQT_v1_pages.txt leaf 256 (printed p.46), s.v. آشیان: 'آشیان … بایای حطی بروزن ماکیان، خانهٔ \"\n             \"مرغان — و سقف خانه باشد', with Mo'in's footnote 4: 'مرکب از پیشوند آ و šyāna به معنی جای و \"\n             \"سرای، ارمنی šēn (به معنی ده، قریه) «بارتولمه ۱۷۰۷»'. Leaf 257 (p.47) has آشیانه. Bartholomae \"\n             \"col. 1707 is the šay- 'wohnen' article, NOT col. 1716 (šyā- 'sich freuen'): the reference \"\n             \"Nourai cites gives a different root for آشیان.\"),},\n   {\"ref\": \"BQT:1222\", \"status\": \"not_checked\",\n    \"note\": (\"p.1222 falls in Borhān vol. 3 (ش–ل, printed pp. 1208-1925), whose local OCR \"\n             \"(incoming/BQT/BQT_v3_pages.txt) is too poor at that page to read the شاد entry; Horn 767 and \"\n             \"Nyberg cover the same claim.\"),},\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.v. šāt and *āyiyān\", \"stance\": \"partial\",\n    \"note\": (\"NYB_vol2_glossary.txt line 3622: 'šāt [šʾt’] glad, happy … — Av. (1716) šyāta-, šāta-; OP \"\n             \"šiyāta- ‘peaceful, happy’, šiyāti- ‘peace, happiness’; … MPrth/MPrs šʾd; Paz. \"\n             \"šād; NP šād' — supports شاد. But line 845: '*āyiyān [ʾdywʾn’], *āyiyānak … a bird’s nest \"\n             \"… I identify the w. with MPrth ʾhyʾng = āhiyānag ‘nest’ … < *āθiyān- … The genuine SW \"\n             \"form is found in NP āšyānah < *āθyāna-, with -θy- in contactual position > -šy-' — contradicts \"\n             \"the āšiyāne arrow.\"),},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.13\", \"stance\": \"silent\",\n    \"note\": (\"PHD.txt line 221: 'āšyān(ag) [ʾsyʾn(k) | (M ʾhyʾng), N āšyāna] nest, lair' — MacKenzie gives \"\n             \"the Manichaean form ʾhyʾng (Nyberg's evidence) but no etymology; PHD.txt line 2908 'nest \"\n             \"āšyān(ag)'. Silent on the root.\"),},\n   {\"src\": \"HRN\", \"where\": \"no. 1034b, p. 232\", \"stance\": \"contradicts\",\n    \"note\": (\"HRN.txt line 8972ff.: '1034b. nišem ‚Nest‘ (Šāhn.) … Doch wohl auch zu np. nišastan \"\n             \"(No. 1033) … Gehört dazu etwa auch āsyāne ‚Nest‘ (No. 35)?' — Horn himself doubts his \"\n             \"own no. 35.\"),},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.v. شاد / آشیان\", \"stance\": \"supports\",\n    \"note\": (\"Mo'in's Borhān footnote (above) is his etymological statement for آشیان; for شاد his lexicon \"\n             \"tags the word Pahlavi, in agreement with Horn and Nyberg.\"),},\n ],\n})\n\ne0[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Latin\",\n \"words\": \"quiĕs; trans-quillus\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Lat. quiēs, quiētis f. 'rest, repose' continues the lengthened variant *kʷyē- (< *kʷyeh₁-s-) and is the \"\n   \"morphological twin of OP šiyāti- (Pokorny: 'apers. šiyāti-š „Wohlbehagen“ (= lat. quies)'); the \"\n   \"derived stative quiēscō, -ere, quiēvī, quiētum 'to rest' gives the PPP quiētus 'calm', matching Av. \"\n   \"šyāta-. Tranquillus 'calm' is trāns- (intensive, as in French très 'very') + *kʷi-lo- 'quiet', the same \"\n   \"-lo- suffix seen in Germanic *hwīl-, so Nourai's hyphenation 'trans-quillus' reproduces Pokorny's own \"\n   \"analysis '(trans- + kʷilos)'. Watkins hedges only slightly ('Possibly Latin tranquillus').\"),\n \"derivation_fa\": (\n   \"quiēs لاتین «آسایش، آرامش» دنبالهٔ گونهٔ کشیدهٔ *kʷyē- (از *kʷyeh₁-s-) است و از نظر ساخت جفتِ دقیقِ \"\n   \"šiyāti- پارسی باستان است؛ پوکورنی خود می‌نویسد «apers. šiyāti-š = lat. quies». فعل quiēscō و صفت مفعولی \"\n   \"quiētus «آرام» نیز با šyāta- اوستایی برابر است. tranquillus از trāns- (در معنای تأکیدی، مانند très فرانسه) \"\n   \"و *kʷi-lo- «آرام» ساخته شده، با همان پسوند -lo- که در *hwīl- ژرمنی دیده می‌شود؛ پس جداسازی «trans-quillus» \"\n   \"در کتاب همان تحلیل پوکورنی است. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/quiet\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": (\"AHD_watkins1985.txt line 650, kʷeiə-²: 'Possibly Latin tranquillus, tranquil (trāns-, across, \"\n             \"beyond) : TRANQUIL. II. Variant form *kʷyē- (< *kʷyes-) in Latin quiēs, quiet (> quiētus, calm, \"\n             \"retiring), and in requiēs … : COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT.'\"),},\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 638\", \"stance\": \"supports\",\n    \"note\": \"'lat. quies, -etis „Ruhe“, quie-scō, -scere, -vī, -tum „ruhen“, mit Formans -lo- (wie germ. *hwil-) tranqui(l)lus „ruhig“ (trans- + kʷilos)'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. quiēiō and queilos\", \"stance\": \"supports\",\n    \"note\": \"'Lat. quiescō, pf: quievi … OLat. quies, Lat. quietus, adj. “quiet, tame, content”' (line 14087); 'cf. Lat. tran-quillus, but cf. quiēiō and cpds.' (line 13917).\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 4, s.v. tranquillity\", \"stance\": \"supports\",\n    \"note\": \"FSD_vol4.txt line 38166: 'tranquillity … [< F. tranquillité, < L. tranquillitas, < tranquillus, quiet]'.\"},\n ],\n})\n\ne0[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"English\",\n \"words\": \"quiet, tranquil\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Both are Latin borrowings, not native words. 'Quiet' (n.) is attested c.1300 from Old French quiete \"\n   \"and directly from Latin quiēs (gen. quiētis); the adjective (late 14c.) is from Lat. quiētus. \"\n   \"'Tranquil' entered English in the 15th c. from Latin tranquillus, partly through French tranquille. \"\n   \"The Latin > Old French > Middle English route is uncontroversial.\"),\n \"derivation_fa\": (\n   \"هر دو واژه وام‌واژهٔ لاتینی‌اند و انگلیسی بومی نیستند. quiet (اسم) از حدود ۱۳۰۰ میلادی از فرانسهٔ کهن quiete \"\n   \"و مستقیماً از quiēs لاتین آمده و صفت آن (اواخر سدهٔ چهاردهم) از quiētus است؛ tranquil در سدهٔ پانزدهم از \"\n   \"tranquillus لاتین (تا اندازه‌ای از راه tranquille فرانسه) وارد شده است. این زنجیره بی‌مناقشه است و ادعای \"\n   \"نورایی درست.\"),\n \"sources\": [\"https://www.etymonline.com/word/quiet\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no reference in the book; checked against Etymonline s.v. quiet and Watkins/AHD instead.\"},\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, kʷeiə-²\", \"stance\": \"supports\",\n    \"note\": \"The English words listed under the root are 'COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT' and 'TRANQUIL'.\"},\n   {\"src\": \"FSD\", \"where\": \"vol. 4 s.v. tranquillity\", \"stance\": \"supports\",\n    \"note\": \"'< L. tranquillitas, < tranquillus, quiet' — the Latin source of the English word.\"},\n ],\n})\n\ne0[\"nodes\"].append({\n \"id\": 5,\n \"lang\": \"Germanic\",\n \"words\": \"hwîlô\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Proto-Germanic *hwīlō f. 'rest, period of rest' < PIE *kʷi-lo- (zero grade of *kʷyeh₁- with the same \"\n   \"-lo- suffix as Lat. tranquillus). The original 'rest' sense is still visible in Old Norse hvíla 'bed, \"\n   \"resting place' and hvíld 'rest' and in Gothic ƕeilan 'to cease, tarry'; elsewhere it shifted to 'span \"\n   \"of time' (Goth. ƕeila, OE hwīl, OHG (h)wīla, Ger. Weile). Nourai's gloss 'resting period, a length of \"\n   \"time' captures exactly that double sense.\"),\n \"derivation_fa\": (\n   \"ژرمنی آغازین *hwīlō «آسایش، هنگام آسودن» از *kʷi-lo- هندواروپایی است، یعنی درجهٔ صفر ریشهٔ *kʷyeh₁- با \"\n   \"همان پسوند -lo- که در tranquillus لاتین دیده می‌شود. معنای نخستین «آسودن» هنوز در نروژی باستان hvíla \"\n   \"«بستر، جای آرمیدن» و hvíld «آسایش» و در گوتیک ƕeilan «درنگ کردن، بازایستادن» پیداست، ولی در دیگر \"\n   \"زبان‌های ژرمنی به «مدت، زمان» تحول یافته است (گوتیک ƕeila، انگلیسی باستان hwīl، آلمانی Weile). \"\n   \"معنای دوگانه‌ای که نورایی آورده درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/while\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 650: 'Suffixed zero-grade variant form *kʷi-lo- (< *kʷiə-lo-). 1. Germanic *hwīlō in: a. Old English hwīl, while: WHILE; b. Old English hwīlum, sometimes: WHILOM.'\"},\n   {\"ref\": \"KLN:1740\", \"status\": \"supports\",\n    \"note\": (\"Klein s.v. 'while' (KLN_1971.txt line 266588; = p.1740 of the 1966 ed.): 'fr. OE. hwil … rel. to \"\n             \"OS. hwil, OFris. hwile, OHG. hwila, MHG. wile, G. Weile, Goth. ƕeila, ‘space of time, \"\n             \"while’, orig. ‘rest’, ON. hvila, ‘bed’ (lit. ‘resting place’)'.\"),},\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 638\", \"stance\": \"supports\",\n    \"note\": \"'got. hveila, ags. hwīl, ahd. (h)wīla „Weile, Zeit“, aisl. hvīla „Ruhebett“, hvīld „Ruhe“, got. hveilan „weilen, zögern, aufhören“'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. queilos\", \"stance\": \"supports\",\n    \"note\": \"IEC.txt line 13917: 'queilos, ā, is “pause, rest, time, period; leisure”. WP I, 510 … Go. hweila, OHG hwīla, OE hwīl, ON hvíla, f. “while, time, period”'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 510\", \"stance\": \"supports\",\n    \"note\": \"'got. hveila, ags. hwīl, ahd. (h)wīla „Weile, Zeit“, aisl. hvīla „Ruhebett“, hvīld „Ruhe“'.\"},\n ],\n})\n\ne0[\"nodes\"].append({\n \"id\": 6,\n \"lang\": \"English\",\n \"words\": \"while\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"OE hwīl f. 'space of time' (accusative hwīle used adverbially) > ME whil, while > Mod.E while. The \"\n   \"conjunction grew out of OE þā hwīle þe 'the while that'; the genitive-adverb whiles (13th c.) gave \"\n   \"whilst (14th c.) with excrescent -t. As a noun it now survives mainly in fixed phrases ('all the \"\n   \"while', 'worthwhile'), the sense 'period of time' having been taken over by time.\"),\n \"derivation_fa\": (\n   \"انگلیسی باستان hwīl «مدت، هنگام» (صورت مفعولی hwīle در کاربرد قیدی) به انگلیسی میانهٔ whil/while و از آنجا \"\n   \"به while امروزی رسیده است. حرف ربط while از ساخت þā hwīle þe «آن مدت که» پدید آمده و صورت قیدیِ اضافی \"\n   \"whiles (سدهٔ سیزدهم) با افزودن t پایانی به whilst (سدهٔ چهاردهم) بدل شده است. این زنجیره یکسره پذیرفته شده \"\n   \"است و ادعای نورایی درست.\"),\n \"sources\": [\"https://www.etymonline.com/word/while\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference printed on the node; verified against Etymonline s.v. while, Klein s.v. while, and Watkins/AHD kʷeiə-².\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. while, n. (1966 ed. p.1740)\", \"stance\": \"supports\",\n    \"note\": \"'while, n. — ME. whil, while, fr. OE. hwil, ‘space of time, while’ … Cp. whilom, whilst, awhile.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, kʷeiə-²\", \"stance\": \"supports\",\n    \"note\": \"'Germanic *hwīlō in: a. Old English hwīl, while: WHILE'.\"},\n ],\n})\n\n# ---------------------------------------------------------------- entry 3\ne3 = {\n \"entry\": 3,\n \"root\": \"K.w.n\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Proto-Semitic *kwn 'to be firm, to be, to exist' (Akk. kânu, Heb. kūn, Arab. kāna)\",\n \"note\": (\"The root box is again Klein verbatim: at p.1433, s.v. 'Shekinah', Klein speaks of 'the Sem. base \"\n          \"k-w-n, ‘to stand firm, to be’'. A Proto-Semitic root *kwn 'to be (firm), to exist' is \"\n          \"universally accepted (Akkadian kânu 'to be firm, established', Hebrew כון kūn 'to be firm, \"\n          \"established' with the Hiphil hēkīn 'to prepare', Ugaritic kn, Arabic kāna 'to be'). The label \"\n          \"'Semitic' and the gloss are correct. What is Nourai's (i.e. Klein's) own is the further claim \"\n          \"that s-k-n is a causative Šaphʿel of this root — see node 3.\"),\n \"note_fa\": (\"ریشهٔ سامی آغازین *kwn «استوار بودن، بودن، هستی داشتن» ریشه‌ای پذیرفته‌شده است: اکدی kânu «استوار \"\n             \"بودن»، عبری כון kūn، اوگاریتی kn، عربی کان. برچسب «سامی» و معنای «to be, to stand firm» درست است و \"\n             \"نورایی آن را عیناً از کلاین (ص ۱۴۳۳، ذیل Shekinah: «ریشهٔ سامی k-w-n به معنی استوار ایستادن، بودن») \"\n             \"گرفته است. آنچه ویژهٔ کلاین (و به پیروی او نورایی) است، ادعای دیگری است: اینکه ریشهٔ س‌ک‌ن صورت \"\n             \"شَفعَلِ (سببیِ) همین ریشه باشد؛ نگاه کنید به گرهٔ ۳.\"),\n \"sources\": [W+\"%D9%83%D8%A7%D9%86\", W+\"%D7%A9%D7%9B%D7%99%D7%A0%D7%94\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1433\", \"status\": \"supports\",\n    \"note\": (\"KLN_1966.txt leaf 762 = printed p.1433 (two printed pages per leaf), s.v. 'Shekinah, \"\n             \"Schechinah, n., the Divine Presence. — Mishnaic Heb. shekhīnāh … All these verbs are prop. \"\n             \"Shaph‘el (= causative) forms of the Sem. base k-w-n, ‘to stand firm, to be’, and \"\n             \"orig. meant ‘he caused to stand, caused to be established’.' Exactly Nourai's root box.\"),},\n   {\"ref\": \"SAP:716\", \"status\": \"not_checked\",\n    \"note\": \"Sayyah's Persian translation of al-Munjid — purchase-only PDF (fidibo), no accessible copy (refs_online.json 'kind': 'purchase').\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.1433\", \"stance\": \"supports\",\n    \"note\": \"as quoted above; Klein is the source Nourai is following here.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery p.173, s.v. sakana\", \"stance\": \"silent\",\n    \"note\": (\"FVQ_pages.txt line ~6373: '(Sakana). Of frequent occurrence. To dwell … Zimmern, Akkad. \"\n             \"Fremdw. 30, thinks that the origin was Mesopotamian.' Jeffery discusses s-k-n but never \"\n             \"connects it with k-w-n.\"),},\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Arabic\",\n \"words\": \"k.w.n\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Arabic ك و ن (k-w-n), verb كَانَ kāna / يَكُونُ yakūnu 'to be, to become, to exist' — a hollow (medial \"\n   \"waw) root, imperfect yakūn with contraction of *-awu- to -ū-, imperative كُنْ kun. It continues \"\n   \"Proto-Semitic *kwn 'to be (firm)' directly and is cognate with Akkadian kânu, Hebrew kūn, Ugaritic kn. \"\n   \"Nourai's gloss 'to become, to be, to exist' is the standard dictionary definition.\"),\n \"derivation_fa\": (\n   \"ریشهٔ عربی ک‌و‌ن، فعل «کانَ / یکونُ» به معنی «بودن، شدن، هستی داشتن»، ریشه‌ای اجوف واوی است: در مضارع \"\n   \"*-awu- به ū کشیده بدل می‌شود (یکون) و امر آن «کُن» است. این ریشه بازماندهٔ مستقیم *kwn سامی آغازین است و \"\n   \"با kânu اکدی، כון عبری و kn اوگاریتی هم‌ریشه است. معنایی که نورایی آورده همان تعریف فرهنگ‌های عربی است و \"\n   \"ادعای او درست است.\"),\n \"sources\": [W+\"%D9%83%D8%A7%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"SAP:1454\", \"status\": \"not_checked\",\n    \"note\": \"Sayyah / al-Munjid in Persian, vol. 2 p.1454 — purchase-only, no accessible digital copy.\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.1433\", \"stance\": \"supports\",\n    \"note\": \"Klein's 'Sem. base k-w-n, ‘to stand firm, to be’' is precisely this Arabic/Semitic root.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.v. تکوین\", \"stance\": \"supports\",\n    \"note\": \"MON_part1.txt line 43010: 'تکوین: [ع.] (مص م.) هست کردن' — Mo'in treats the k-w-n derivatives as Arabic with the sense 'to bring into being'.\"},\n ],\n})\n\ne3[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"makân «مکان»; kâenât «کائنات ، کاینات»; takvîn «تکوین»; kon «کن» (+ کاف و نون)\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"All four are Arabic loanwords in Persian, all built on ك و ن. مکان makān is the ism al-makān (noun of \"\n   \"place) of kāna, 'the place where something comes to be'; it is cognate with Hebrew מָכוֹן māḵōn and \"\n   \"Geʿez መካን mäkan, though Arab grammarians, misparsing the m- as radical, also produced a secondary root \"\n   \"م ك ن with تَمَكَّنَ/مَكَّنَ — Nourai's assignment to k-w-n is the etymologically correct one. کائنات \"\n   \"kāʾināt is the sound feminine plural of the active participle كَائِن kāʾin 'existing (thing)', hence \"\n   \"'beings, the created world'; the Persian spelling کاینات simply drops the hamza seat. تکوین takwīn is \"\n   \"the maṣdar of form II kawwana 'to bring into being', hence 'creation, formation' (Persian also uses it \"\n   \"for the Book of Genesis, سفر تکوین). کن kon is the imperative kun of kāna, quoted from the Qurʾānic \"\n   \"creation formula كُنْ فَيَكُونُ 'Be! — and it is' (Q 2:117, 16:40, 36:82, 40:68); in Persian poetry the \"\n   \"two letters of that word are personified as کاف و نون, exactly as in Ferdowsi's line quoted on the \"\n   \"chart, 'دو گیتی پدید آمد از کاف و نون'.\"),\n \"derivation_fa\": (\n   \"هر چهار واژه وام‌واژهٔ عربی از ریشهٔ ک‌و‌ن‌اند. «مکان» اسم مکان از «کان» است، یعنی «جایی که چیزی در آن \"\n   \"هست می‌شود»؛ با מכון عبری و መካን گعزی هم‌ریشه است. (نحویان عرب گاه میمِ آغازین را اصلی پنداشته و ریشهٔ \"\n   \"فرعی م‌ک‌ن با «تمکّن» و «مکّن» ساخته‌اند، ولی نسبت دادن آن به ک‌و‌ن که نورایی کرده درست است.) «کائنات» \"\n   \"جمع مؤنث سالم اسم فاعل «کائن» است، یعنی «هستی‌ها، جهان آفریده»؛ املای «کاینات» تنها کرسیِ همزه را انداخته \"\n   \"است. «تکوین» مصدر باب تفعیل (کوّن) به معنی «هست کردن، آفرینش» است و در فارسی «سِفر تکوین» نیز از همین‌جاست. \"\n   \"«کن» صیغهٔ امر «کان» است، برگرفته از عبارت قرآنی «کُن فَیَکون» (بقره ۱۱۷، نحل ۴۰، یس ۸۲، غافر ۶۸)؛ در شعر \"\n   \"فارسی دو حرف این کلمه را «کاف و نون» خوانده‌اند، چنان‌که در بیت فردوسی در همین نمودار: «دو گیتی پدید آمد از \"\n   \"کاف و نون». ادعای نورایی در همهٔ این موارد درست است.\"),\n \"sources\": [W+\"%D9%85%D9%83%D8%A7%D9%86\", W+\"%D9%83%D8%A7%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": (\"MON_part1.txt line 43010 'تکوین: [ع.] (مص م.) هست کردن' — Mo'in marks it Arabic; مکان and \"\n             \"کائنات are likewise given as Arabic loans in Mo'in's lexicon (MON_part1/part2 passim, e.g. \"\n             \"line 97742 'کائنات الجو').\"),},\n   {\"ref\": \"FVA:359\", \"status\": \"not_checked\",\n    \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368) — catalogue record only, no digital copy found (refs_online.json).\"},\n   {\"ref\": \"FSF:265\", \"status\": \"partial\",\n    \"note\": (\"The entry exists in Noushin's Vazhe-namak but at a different page of the copy on disk: \"\n             \"FSF_pages.txt block 358 (running head of block 359 = printed p.355, so block 358 = p.354) \"\n             \"s.v. کاف و نون: '«فیکون» پس شد، موجود شد، خلق شد … این افسانه در قرآن سورهٔ نحل آیهٔ ۴۰ آمده \"\n             \"است «انما قولنا لشیء اذا اردناه ان نقول له کن فیکون»', followed by the very line Nourai \"\n             \"quotes, 'دو گیتی پدید آمد از کاف و نون / چرا نی بفرمان او در نه چون'. Content supports \"\n             \"Nourai exactly; the page number belongs to another printing.\"),},\n ],\n \"consulted\": [\n   {\"src\": \"FSF\", \"where\": \"Vazhe-namak, s.v. کاف و نون (block 358 = p.354 of the archive.org scan)\", \"stance\": \"supports\",\n    \"note\": \"as quoted above — Noushin glosses the Shahnameh line by the Qurʾānic kun fa-yakūn.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. تکوین, کائنات\", \"stance\": \"supports\",\n    \"note\": \"MON_part1.txt lines 43010, 97742 — both tagged [ع.] (Arabic).\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.1433\", \"stance\": \"supports\",\n    \"note\": \"Klein's k-w-n 'to stand firm, to be' is the root all four Persian loans belong to.\"},\n ],\n})\n\ne3[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Semitic\",\n \"words\": \"s.k.n\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"The words are real and the gloss is Klein's own ('Akkad. shakānu, ‘to lay, set, deposit’'), but \"\n   \"the ARROW — that s-k-n is derived from k-w-n — is a minority analysis. Klein states it explicitly on \"\n   \"the page Nourai cites: Heb. šākan, Aram.-Syr. šəḵēn, Arab. sakuna and Akk. šakānu 'are prop. Shaphʿel \"\n   \"(= causative) forms of the Sem. base k-w-n … and orig. meant ‘he caused to stand, caused to be \"\n   \"established’'. This is a 19th-century style š-causative (Šaphʿel) etymology. Modern Semitic \"\n   \"lexicography does not follow it: Proto-Semitic *ŝkn / *škn 'to place, to settle, to dwell' (Akk. \"\n   \"šakānu, Ugar. škn, Heb. šāḵan, Arab. sakana, Geʽez sakana) is treated as an independent root, and \"\n   \"the standard dictionaries derive šəḵīnāh from šāḵan alone with no mention of k-w-n. Zimmern, whom \"\n   \"Nourai also cites, likewise derives the West Semitic forms from Akkadian šakānu with no k-w-n link. \"\n   \"Verdict: plausible — the etymon and gloss are right, the parent arrow is Klein's private analysis.\"),\n \"derivation_fa\": (\n   \"خودِ واژه‌ها و معنای «نهادن، گذاشتن، ودیعه نهادن» درست است (این تعریف را نورایی از کلاین گرفته)، اما پیکانِ \"\n   \"اشتقاق — یعنی برآمدن س‌ک‌ن از ک‌و‌ن — نظری اقلیتی است. کلاین در همان صفحه‌ای که نورایی ارجاع داده می‌نویسد که \"\n   \"šākan عبری، šəḵēn آرامی-سریانی، «سکن» عربی و šakānu اکدی همگی صورت شَفعَل (سببی) ریشهٔ سامی k-w-n اند و در \"\n   \"اصل معنی «استوار کردن، برپا داشتن» داشته‌اند. این‌گونه تحلیلِ سببیِ ش‌دار از سنّت سدهٔ نوزدهم است. \"\n   \"ریشه‌شناسی امروزی آن را نمی‌پذیرد: *škn سامی آغازین «نهادن، سکونت گزیدن» ریشه‌ای مستقل شمرده می‌شود و \"\n   \"فرهنگ‌های معیار «شکینه» را تنها از «شاکَن» می‌گیرند و نامی از ک‌و‌ن نمی‌برند. زیمرن هم که نورایی به او \"\n   \"ارجاع داده، صورت‌های سامی غربی را از šakānu اکدی می‌گیرد و سخنی از ک‌و‌ن ندارد. پس: با احتیاط پذیرفتنی.\"),\n \"sources\": [W+\"%D8%B3%D9%83%D9%86\", W+\"%D7%A9%D7%9B%D7%99%D7%A0%D7%94\", \"https://www.balashon.com/2020/06/shechinah-and-scene.html\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1433\", \"status\": \"supports\",\n    \"note\": (\"KLN_1966.txt leaf 762 (p.1433) s.v. Shekinah: 'Akkad. shakānu, ‘to lay, set, deposit’ \"\n             \"(whence mashkanu, ‘dwelling place; place; deposit’). All these verbs are prop. \"\n             \"Shaph‘el (= causative) forms of the Sem. base k-w-n.' Nourai's gloss for s.k.n is Klein's \"\n             \"words verbatim, and the k-w-n > s-k-n arrow is Klein's claim.\"),},\n   {\"ref\": \"AKD:30\", \"status\": \"partial\",\n    \"note\": (\"Zimmern p.30 (AKD.txt line 405, at the head of leaf 40 = end of printed p.30; cross-referenced \"\n             \"from p.20 n.1 'S. auch noch unten S. 30 zu šakānu'): 'akk. šakānu niederlegen, niedersetzen, \"\n             \"spez. auch vom Wohnung, Lager usw. aufschlagen : > viell., dann freilich früh, hebr. šākan, \"\n             \"aram. šəkēn wohnen, šeknā, šəkīntā Wohnung, arab. sakana ruhen, wohnen'. Supports the gloss \"\n             \"and the Akkadian>West-Semitic spread, but says nothing about k-w-n — and makes the Hebrew/\"\n             \"Arabic forms loans from Akkadian rather than inherited causatives.\"),},\n ],\n \"consulted\": [\n   {\"src\": \"AKD\", \"where\": \"Zimmern p.30 (and p.20 n.1 on maškanu)\", \"stance\": \"partial\",\n    \"note\": (\"AKD.txt line 240: 'Eig. Depositum, von šakānu niederlegen … also nicht von mšk abzuleiten. \"\n             \"In älterer Zeit hat maškanu auch die Bed. Lagerhaus, Speicher; daraus wohl sicher durch \"\n             \"Entlehnung hebr. miškanōt Vorratshäuser.'\"),},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery p.173 s.v. sakana\", \"stance\": \"partial\",\n    \"note\": (\"'Zimmern, Akkad. Fremdw. 30, thinks that the origin was Mesopotamian. The Akk. šakānu meant \"\n             \"to settle in a place (niederlegen, niedersetzen) … This, he thinks, was the origin on the one \"\n             \"hand of the other Semitic forms, e.g. Heb. שכן; Phoen. שכן; Syr. ܫܟܢ; and Ar. سكن' — the same \"\n             \"root history, again without k-w-n.\"),},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.1433\", \"stance\": \"supports\",\n    \"note\": \"the Šaphʿel analysis, quoted above.\"},\n ],\n})\n\ne3[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"Arabic\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"An empty pass-through box: the Arabic reflex of Semitic s-k-n, i.e. سَكَنَ sakana / يَسْكُنُ yaskunu \"\n   \"'to be still, to be at rest; to dwell, inhabit', with سُكُون sukūn 'stillness', سَاكِن sākin \"\n   \"'dwelling/still', مَسْكَن maskan 'dwelling', تَسْكِين taskīn 'calming' (form II). The Arabic root is a \"\n   \"regular continuation of Proto-Semitic *škn, cognate with Hebrew šāḵan, Ugaritic škn and Akkadian \"\n   \"šakānu; the semantic split 'set down' > 'be still' / 'settle, dwell' is common to the whole family.\"),\n \"derivation_fa\": (\n   \"این خانه در نمودار تهی است و تنها بازتاب عربیِ ریشهٔ سامی س‌ک‌ن را نشان می‌دهد: «سَکَنَ/یَسکُنُ» به معنی \"\n   \"«آرام گرفتن؛ سکونت گزیدن»، با مشتقاتی چون سکون، ساکن، مسکن و تسکین. این ریشهٔ عربی دنبالهٔ قاعده‌مند *škn \"\n   \"سامی آغازین است و با שכן عبری، škn اوگاریتی و šakānu اکدی هم‌ریشه است؛ تحول معنایی «نهادن» به «آرام گرفتن» \"\n   \"و «سکنا گزیدن» در سراسر این خانوادهٔ زبانی دیده می‌شود. ادعای نورایی در این حلقه درست است.\"),\n \"sources\": [W+\"%D8%B3%D9%83%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"SAP:716\", \"status\": \"not_checked\",\n    \"note\": \"Sayyah / al-Munjid in Persian — purchase-only; not accessible.\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.1433\", \"stance\": \"supports\",\n    \"note\": \"'Arab. sakuna, ‘he dwelled’' is listed beside Heb. šāḵan and Akk. šakānu.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery p.173 s.v. sakana\", \"stance\": \"supports\",\n    \"note\": \"'(Sakana). Of frequent occurrence. To dwell. Besides the simple verb we find … the participles … and the nominal forms …' — the Arabic root and its derivatives.\"},\n   {\"src\": \"AKD\", \"where\": \"Zimmern p.30\", \"stance\": \"supports\",\n    \"note\": \"'arab. sakana ruhen, wohnen' listed among the reflexes of Akk. šakānu.\"},\n ],\n})\n\ne3[\"nodes\"].append({\n \"id\": 5,\n \"lang\": \"Persian\",\n \"words\": \"(no transliterations; script only: سکون ، ساکن ، مسکن ، مُسکن ، تسکین ، مِسکین)\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"Five of the six are straightforward Arabic loans in Persian from س ك ن: سکون sokūn 'stillness' \"\n   \"(maṣdar), ساکن sāken 'still; resident' (act. participle), مسکن maskan 'dwelling' (noun of place), \"\n   \"مُسکّن mosakken 'sedative' (form II act. participle mu-sakkin), تسکین taskīn 'calming, sedation' (form \"\n   \"II maṣdar). The sixth, مسکین meskīn 'poor, wretched', only looks like a mafʽīl of the same root: \"\n   \"the Arabic miskīn is itself a borrowing — from Aramaic/Syriac meskēnā, ultimately Akkadian muškēnum \"\n   \"'commoner, dependant' — which was secondarily reanalysed inside Arabic as belonging to s-k-n (whence \"\n   \"the Arabic denominal maskana 'poverty'). Fraenkel, Nöldeke and Jeffery all treat it as a loan, and the \"\n   \"same word travelled on to Italian meschino, French mesquin, Spanish mezquino. So the Persian words are \"\n   \"all correctly shown as coming through Arabic, but for مسکین the ultimate origin drawn on the chart is \"\n   \"wrong; hence 'plausible' rather than 'confirmed'.\"),\n \"derivation_fa\": (\n   \"پنج واژه از شش واژه وام‌واژهٔ روشنِ عربی از ریشهٔ س‌ک‌ن‌اند: «سکون» (مصدر)، «ساکن» (اسم فاعل)، «مسکن» \"\n   \"(اسم مکان)، «مُسکّن» (اسم فاعل باب تفعیل) و «تسکین» (مصدر باب تفعیل). ششمی، یعنی «مسکین»، تنها به ظاهر \"\n   \"بر وزن مَفعیل از همین ریشه می‌نماید: «مسکین» عربی خود وام‌واژه است، از meskēnā آرامی/سریانی و در نهایت از \"\n   \"muškēnum اکدی به معنی «فرودست، عامی»، که سپس در درون عربی به ریشهٔ س‌ک‌ن بازتحلیل شده است (و از همین \"\n   \"بازتحلیل «مسکنة» ساخته شده). فرنکل، نُلدکه و جفری همگی آن را وام‌واژه می‌دانند و همین واژه به meschino \"\n   \"ایتالیایی، mesquin فرانسوی و mezquino اسپانیایی نیز راه یافته است. پس مسیر «عربی ← فارسی» برای همهٔ این \"\n   \"واژه‌ها درست است، ولی خاستگاه نهاییِ «مسکین» در نمودار نادرست است؛ از این رو حکم «با احتیاط پذیرفتنی».\"),\n \"sources\": [W+\"%D9%85%D8%B3%D9%83%D9%8A%D9%86\", W+\"%D8%B3%D9%83%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": (\"Mo'in's lexicon marks all of these as Arabic; e.g. MON_part1.txt line 43579 'تمسکن: [ع.] \"\n             \"(مص‌ل.) مسکین …' and line 78732 'مسکین شدن … مسکنت، فقر'. Mo'in does not give miskīn's \"\n             \"pre-Arabic history.\"),},\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.v. مسکین / تمسکن\", \"stance\": \"supports\",\n    \"note\": \"MON_part1.txt lines 43579, 78732 — Arabic tag, no further etymology.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, s.v. miskīn (index, FVQ_pages.txt line 9514)\", \"stance\": \"partial\",\n    \"note\": \"Jeffery has a Miskīn entry in the Foreign Vocabulary — i.e. he classes the Qur'anic مسكين as a borrowing, not a native s-k-n formation.\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.1433\", \"stance\": \"silent\",\n    \"note\": \"Klein's Shekinah article lists Arab. sakuna 'he dwelled' but says nothing of miskīn.\"},\n ],\n})\n\ne3[\"nodes\"].append({\n \"id\": 6,\n \"lang\": \"Hebrew\",\n \"words\": \"šekinah\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Mishnaic/Rabbinic Hebrew שְׁכִינָה šəḵīnāh 'the indwelling (Presence) of God', a qəṭīlāh-type verbal \"\n   \"noun of שָׁכַן šāḵan 'he dwelt, settled' (Biblical Hebrew, e.g. of God dwelling in the Tabernacle \"\n   \"מִשְׁכָּן miškān). The word is not Biblical; it is the Rabbinic abstraction used in the Targums to \"\n   \"avoid anthropomorphism. Nourai's gloss 'standing calm, dwelling place (of God)' is Klein's ('dwelling \"\n   \"place (of God)') with the 'standing calm' added from the k-w-n analysis. The derivation from s-k-n \"\n   \"itself is universally accepted; only the further step back to k-w-n (node 3) is contested.\"),\n \"derivation_fa\": (\n   \"«شکینه» (שְׁכִינָה) واژه‌ای از عبریِ میشنایی/ربّانی است به معنی «حضور و سکونت خداوند»، و اسم مصدرِ فعل \"\n   \"שָׁכַן šāḵan «سکونت گزید» است (همان ریشه‌ای که מִשְׁכָּן miškān «خیمهٔ عبادت» از آن است). این واژه در \"\n   \"تورات نیامده و ساختهٔ سنّت ربّانی و ترگوم‌هاست تا از تشبیه خداوند به انسان پرهیز شود. معنایی که نورایی \"\n   \"آورده («آرامِ برجا، جایگاه سکونت خداوند») ترکیبی است از تعریف کلاین و تحلیل ک‌و‌نِ او. اشتقاق شکینه از \"\n   \"ریشهٔ ش‌ک‌ن مورد اتفاق همه است؛ تنها گام پیشین (بازگرداندن ش‌ک‌ن به ک‌و‌ن، گرهٔ ۳) محل مناقشه است.\"),\n \"sources\": [W+\"%D7%A9%D7%9B%D7%99%D7%A0%D7%94\", \"https://www.balashon.com/2020/06/shechinah-and-scene.html\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1433\", \"status\": \"supports\",\n    \"note\": (\"KLN_1966.txt leaf 762 (p.1433): 'Shekinah, Schechinah, n., the Divine Presence. — Mishnaic \"\n             \"Heb. shekhīnāh, ‘dwelling place (of God)’, from the base of shākhan, ‘he dwelled, \"\n             \"abode’, which is rel. to Aram.-Syr. shəkhēn, Arab. sakuna, ‘he dwelled’, Akkad. \"\n             \"shakānu …'.\"),},\n ],\n \"consulted\": [\n   {\"src\": \"AKD\", \"where\": \"Zimmern p.30\", \"stance\": \"supports\",\n    \"note\": \"'hebr. šākan, aram. šəkēn wohnen, šeknā, šəkīntā Wohnung' — the Hebrew/Aramaic noun of the same root.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery pp.174-5 s.v. sakīna\", \"stance\": \"supports\",\n    \"note\": \"'There can be little doubt, however, that we have here the Heb. שכינה, though possibly through the Syr. ܫܟܝܢܬܐ.'\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.1433\", \"stance\": \"supports\",\n    \"note\": \"as quoted above.\"},\n ],\n})\n\ne3[\"nodes\"].append({\n \"id\": 7,\n \"lang\": \"Arabic\",\n \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"The empty box is Arabic سَكِينَة sakīna, the Qur'anic word (Q 2:248; 9:26, 40; 48:4, 18, 26) for the \"\n   \"divine tranquillity/presence 'sent down' upon the believers. Jeffery's verdict, still the standard \"\n   \"one, is that Arabic had a genuine faʿīla-noun sakīna 'tranquillity' from sakana, but that the Qur'anic \"\n   \"usage is the Hebrew Shekinah: 'Now there is a genuine Arabic word سكينة meaning tranquillity, from سكن \"\n   \"to rest, be quiet … This, however, will hardly fit ii, 249 … There can be little doubt that we have \"\n   \"here the Heb. שכינה, though possibly through the Syr. Muhammad would have learned the word from the \"\n   \"People of the Book, and not quite understanding its significance, have associated it with the genuine \"\n   \"Arabic word meaning tranquillity.' Modern Wiktionary phrases it as an Arabic formation from س ك ن \"\n   \"whose religious meanings are a semantic loan from Hebrew. So Nourai's arrow Hebrew > Arabic is right \"\n   \"for the meaning but not for the form, which is native: 'plausible' rather than 'confirmed'. (Mo'in \"\n   \"seems to agree: his lexicon entry tags سکینه '[ع. سکینة معرّب]'.)\"),\n \"derivation_fa\": (\n   \"این خانهٔ تهی همان «سَکینة» عربی است، واژهٔ قرآنی (بقره ۲۴۸؛ توبه ۲۶ و ۴۰؛ فتح ۴، ۱۸، ۲۶) به معنی آرامشی \"\n   \"که بر مؤمنان «فرو فرستاده» می‌شود. داوری جفری، که هنوز داوری معیار است، چنین است: در عربی واژه‌ای اصیل بر \"\n   \"وزن فَعیلة از «سکن» به معنی «آرامش» هست، اما کاربرد قرآنی آن همان «شکینه»ی عبری است و «تردیدی نیست که \"\n   \"اینجا با שכינה عبری سروکار داریم، شاید از راه سریانی»؛ پیامبر آن را از اهل کتاب شنیده و با واژهٔ اصیل عربیِ \"\n   \"هم‌آواز درآمیخته است. ویکی‌واژه نیز آن را «ساختی عربی از ریشهٔ س‌ک‌ن که معانی دینی‌اش وام معنایی از عبری \"\n   \"است» می‌داند. پس پیکانِ «عبری ← عربی» در نمودار از نظر معنا درست است ولی از نظر صورت نه؛ از این رو «با \"\n   \"احتیاط پذیرفتنی». معین هم در فرهنگ خود سکینه را «[ع. سکینة معرّب]» نشانه‌گذاری کرده است.\"),\n \"sources\": [W+\"%D8%B3%D9%83%D9%8A%D9%86%D8%A9\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1902\", \"status\": \"partial\",\n    \"note\": (\"Mo'in vols 5-6 (Aʿlām) are not online with page numbers, so p.1902 itself could not be opened; \"\n             \"Mo'in's lexicon entry is on disk and supports the substance: MON_part1.txt line 78775 \"\n             \"'سکینه: [ع. سکینة معر.] (اِ.) آرام، آرامش، وقار، طمأنینه. آنچه دل را قوی گرداند و اطمینان \"\n             \"بخشد. (فا.) روح‌القدس، کلمه.'\"),},\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary, pp.174-5 s.v. sakīna\", \"stance\": \"supports\",\n    \"note\": (\"'The word occurs only in late Madinan passages and appears to have been a technical term \"\n             \"learned by Muhammad at a relatively late period … There can be little doubt, however, that we \"\n             \"have here the Heb. שכינה, though possibly through the Syr.' — exactly Nourai's Hebrew>Arabic \"\n             \"arrow.\"),},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. سکینه\", \"stance\": \"supports\",\n    \"note\": \"MON_part1.txt line 78775, quoted above; the tag 'معر.' marks it as an arabicised (borrowed) form.\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.1433\", \"stance\": \"partial\",\n    \"note\": \"Klein lists Arab. sakuna under the same root but does not discuss sakīna or the borrowing of the Shekinah concept.\"},\n ],\n})\n\ne3[\"nodes\"].append({\n \"id\": 8,\n \"lang\": \"Persian\",\n \"words\": \"Sakîneh «سکینه»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Persian سکینه Sakine is the Arabic sakīna borrowed unchanged, with the regular Persian treatment of \"\n   \"Arabic tāʾ marbūṭa as -e (sakīnat- > sakīne). As a common noun Mo'in glosses it 'آرام، آرامش، وقار، \"\n   \"طمأنینه' and, in religious use, 'روح‌القدس' (the Holy Spirit); as the female given name it is borne \"\n   \"above all by Sakīna bint al-Ḥusayn, whence its popularity in Shi'i Iran. Nourai's gloss and his note \"\n   \"'a female name' are both correct; the word reaches Persian through Arabic exactly as the chart shows.\"),\n \"derivation_fa\": (\n   \"«سکینه» فارسی همان «سکینة» عربی است که بی‌تغییر وام گرفته شده و تای مربوطهٔ عربی، بنا بر قاعدهٔ همیشگی، \"\n   \"در فارسی به «ـه» بدل شده است. معین آن را «آرام، آرامش، وقار، طمأنینه» و در کاربرد دینی «روح‌القدس» معنا \"\n   \"کرده است. به عنوان نام زنانه پیش از همه نام سکینه بنت‌الحسین است و از همین‌رو در ایران شیعی رواج یافته \"\n   \"است. هم معنایی که نورایی آورده و هم یادداشت «نام زنانه» درست است و مسیر عربی ← فارسی همان است که در \"\n   \"نمودار آمده.\"),\n \"sources\": [W+\"%D8%B3%D9%83%D9%8A%D9%86%D8%A9\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1902\", \"status\": \"partial\",\n    \"note\": (\"The Aʿlām volumes are not digitised page-by-page; Mo'in's lexicon entry (MON_part1.txt line \"\n             \"78775) 'سکینه: [ع. سکینة معر.] (اِ.) آرام، آرامش، وقار، طمأنینه …' confirms the Arabic origin \"\n             \"and the sense Nourai gives, but p.1902 itself could not be opened.\"),},\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. سکینه\", \"stance\": \"supports\",\n    \"note\": \"line 78775, quoted above — '[ع. سکینة]', 'آرام، آرامش، وقار'.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery pp.174-5\", \"stance\": \"supports\",\n    \"note\": \"gives the Arabic word from which the Persian name is taken, and its Hebrew background.\"},\n ],\n})\n\nout = {\n \"pdf_page\": 296,\n \"book_page\": 266,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [e0, e3],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-296.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p296/build.py"
}
```


### [2026-09-06T22:49:17.115Z] TOOL RESULT

```
written
```


## [2026-09-06T22:49:22.493Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-296.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 296"
}
```


### [2026-09-06T22:49:24.349Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'disputed': 2, 'confirmed': 9, 'plausible': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'partial': 6, 'not_checked': 7, 'not_found': 1, 'contradicts': 1}
books consulted: {'partial': 7, 'supports': 29, 'silent': 2, 'contradicts': 1} | by book: {'KLN': 8, 'MON': 6, 'FVQ': 6, 'AKD': 3, 'HRN': 2, 'POK': 2, 'IEC': 2, 'FSD': 2, 'AHD': 2, 'BRT': 1, 'KNT': 1, 'NYB': 1, 'PHD': 1, 'WLD': 1, 'FSF': 1}
```


## [2026-09-06T22:49:47.440Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-296.json` written; `verify_check.py 296` → 14/14 nodes, **0 PROBLEM lines**.

**Page 296 (book p. 266) — 2 roots, 14 nodes**
- Root verdicts: confirmed 2. Node verdicts: confirmed 9, plausible 3, disputed 2.
- Ref checks: supports 9, partial 6, not_checked 7 (SAP, FVA, ZFS have no accessible copy), not_found 1, contradicts 1. 15 books consulted.

**Disputed**
- *Kweye* #1 — Av./OP `â-šyâ` "resting place, nest": not an attested form. Bartholomae has no `ā-šyā-` (only `ā-šāite` "to rejoice"); Nourai back-formed it from Horn no. 35, which Horn himself hedges. The other two items (šyā-/šā- "rejoice", šāiti-/šiyāti-) are fully confirmed by POK 638, BRT col. 1715–17 and Kent.
- *Kweye* #2 — Persian `آشیانه`: شاد is rock-solid (Horn 767, Nyberg, POK), but آشیان is contested. **Mo'in's own footnote on the very page Nourai cites (BQT vol. 1 p. 46) contradicts him**: "آ + šyāna 'place, dwelling', Arm. šēn — Bartholomae 1707", i.e. Av. *šay-* "dwell", not *šyā-* "rest". Nyberg (*āyiyān(ag)* < *\*āθyāna-*, Parthian *āhyānag*) also excludes the *kʷyeh₁-* route.

**Plausible**
- *K.w.n* #3 — `s.k.n` from `k.w.n`: Klein p. 1433 says exactly this (Šaphʿel causative of k-w-n), so the ref supports; but modern Semitic lexicography treats *škn as an independent Proto-Semitic root, and Zimmern (AKD 30) makes no k-w-n link.
- *K.w.n* #5 — Persian سکون/ساکن/مسکن/مسکّن/تسکین fine, but **مسکین** is an Akkadian *muškēnum* → Aramaic *meskēnā* loan reanalysed under س ك ن (Fraenkel, Nöldeke, Jeffery).
- *K.w.n* #7 — Arabic سكينة: form is a native faʿīla from س ك ن; only the Qur'anic *sense* is the Hebrew Shekinah (Jeffery pp. 174–5). Arrow right for meaning, not for form.

**Citation slips in the book (not extraction errors)**
- HRN:6 → the āšiyān entry is Horn no. 35, printed p. 9. KNT:210 → p. 210 is the b-/m- range; šiyāti- is in Kent's texts elsewhere. FSF:265 → the کاف و نون entry is at p. 354 of the available scan (different printing); content matches exactly, including the Ferdowsi line.

**Extraction errors: none.** I read `site/pages/296.jpg`; the JSON reproduces the printed chart faithfully (words, scripts, refs, the Ferdowsi couplet, and the "Gwhen 1" cross-note, which is Nourai's own alternative — Av. *šan/šyangh* "house", the route modern sources actually favour).

11 web pages archived via `fetch_source.py` (Wiktionary شاد / آشیانه / *kʷyeh₁- / كان / مكان / سكن / سكينة / مسكين / שכינה, Etymonline while + quiet, Balashon).
