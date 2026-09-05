# Verification process log — verify-page-109


## [2026-09-05T17:27:02.530Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 109 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-109.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-109.json. Write /home/sfmqrb/git/rishe/data/verification/page-109.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 109` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T17:27:04.091Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T17:27:04.802Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T17:27:04.818Z] TOOL RESULT

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


## [2026-09-05T17:27:05.168Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-109.txt"
}
```


### [2026-09-05T17:27:05.193Z] TOOL RESULT

```
1	=== PDF page 109 (book page 79) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dâ 2, Dânu : to flow; river  (refs POK:175)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:175; IRN:123 | dânu : river, water ; nâv-dân : water river (path), gutter ☞Na 1 ; danuva : to flow ; Dânavo : Danube river
5	  #2 (parent #1) [Persian] refs=IRN:123 | nâvdân «ناودان» : gutter
6	  #3 (parent #1) [Greek] refs=POK:175; IRN:123; MON5:772 | Dânao : Danube | NOTE: This word apparently entered European languages through Scythians (7th century B.C.) or Iranian immigrants in Greece.
7	    #4 (parent #3) [French] refs=None | Danube
8	      #5 (parent #4) [Persian] refs=MON5:516 | Dânŭb «دانوب»
9	      #6 (parent #4) [English] refs=FSD:652 | Danube | NOTE: AHD derives this through Latin "Dânuvius"
10	--- entry 1 ---
11	ROOT Dabh -> redirect to Dâ 1
12	--- entry 2 ---
13	ROOT Dâbh -> redirect to Dâ 1
14	--- entry 3 ---
15	ROOT Dâbhar -> redirect to D.b.r
16	--- entry 4 ---
17	ROOT Dabhn -> redirect to Dâ 1
18	--- entry 5 ---
19	ROOT Dâi -> redirect to Dâ 1
20	--- entry 6 ---
21	ROOT Dakru -> redirect to Akru
22	--- entry 7 ---
23	ROOT Dânu -> redirect to Dâ 2
24	--- entry 8 ---
25	ROOT Dap -> redirect to Dâ 1
26	--- entry 9 ---
27	ROOT [Semitic] Daqal : fruit of palm tree, date  (refs None)
28	#1 (parent #0) [Arabic] refs=KLN:403; SAP:471 | daqal : inferior date palm
29	  #2 (parent #1) [Persian] refs=MON:1543 | daqal «دقل» : date
30	#3 (parent #0) [Greek] refs=KLN:403 | daktulus : date
31	  #4 (parent #3) [Latin] refs=AHD:337 | dactylus : date
32	    #5 (parent #4) [French] refs=None | datte
33	      #6 (parent #5) [English] refs=None | date 1 : fruit
34	--- entry 10 ---
35	ROOT Dayânu -> redirect to Dînu
36	
```


## [2026-09-05T17:27:08.848Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-109.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\n\"",
 "description": "Dump source JSON for page 109"
}
```


## [2026-09-05T17:27:09.265Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T17:27:10.756Z] TOOL RESULT

```
{
 "pdf_page": 109,
 "book_page": 79,
 "entries": [
  {
   "root": {
    "name": "Dâ 2, Dânu",
    "lang": "Indo-European",
    "refs": "POK:175",
    "gloss": "to flow; river"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan / Old Persian",
     "refs": "POK:175; IRN:123",
     "words": [
      {
       "translit": "dânu",
       "gloss": "river, water",
       "script": null
      },
      {
       "translit": "nâv-dân",
       "gloss": "water river (path), gutter",
       "script": null,
       "see": [
        "Na 1"
       ]
      },
      {
       "translit": "danuva",
       "gloss": "to flow",
       "script": null
      },
      {
       "translit": "Dânavo",
       "gloss": "Danube river",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Persian",
     "refs": "IRN:123",
     "words": [
      {
       "translit": "nâvdân",
       "gloss": "gutter",
       "script": "ناودان"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 1,
     "lang": "Greek",
     "refs": "POK:175; IRN:123; MON5:772",
     "words": [
      {
       "translit": "Dânao",
       "gloss": "Danube",
       "script": null
      }
     ],
     "script_extra": null,
     "note": "This word apparently entered European languages through Scythians (7th century B.C.) or Iranian immigrants in Greece.",
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "French",
     "refs": null,
     "words": [
      {
       "translit": "Danube",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Persian",
     "refs": "MON5:516",
     "words": [
      {
       "translit": "Dânŭb",
       "gloss": null,
       "script": "دانوب"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 4,
     "lang": "English",
     "refs": "FSD:652",
     "words": [
      {
       "translit": "Danube",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": "AHD derives this through Latin \"Dânuvius\"",
     "quote": null
    }
   ]
  },
  {
   "root": {
    "name": "Dabh",
    "redirect": "Dâ 1"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Dâbh",
    "redirect": "Dâ 1"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Dâbhar",
    "redirect": "D.b.r"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Dabhn",
    "redirect": "Dâ 1"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Dâi",
    "redirect": "Dâ 1"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Dakru",
    "redirect": "Akru"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Dânu",
    "redirect": "Dâ 2"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Dap",
    "redirect": "Dâ 1"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Daqal",
    "lang": "Semitic",
    "refs": null,
    "gloss": "fruit of palm tree, date"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Arabic",
     "refs": "KLN:403; SAP:471",
     "words": [
      {
       "translit": "daqal",
       "gloss": "inferior date palm",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Persian",
     "refs": "MON:1543",
     "words": [
      {
       "translit": "daqal",
       "gloss": "date",
       "script": "دقل"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Greek",
     "refs": "KLN:403",
     "words": [
      {
       "translit": "daktulus",
       "gloss": "date",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Latin",
     "refs": "AHD:337",
     "words": [
      {
       "translit": "dactylus",
       "gloss": "date",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "French",
     "refs": null,
     "words": [
      {
       "translit": "datte",
       "gloss": null,
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
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "date 1",
       "gloss": "fruit",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    }
   ]
  },
  {
   "root": {
    "name": "Dayânu",
    "redirect": "Dînu"
   },
   "nodes": []
  }
 ]
}
```


### [2026-09-05T17:27:10.788Z] TOOL RESULT

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


## [2026-09-05T17:27:35.509Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IRN','MON','FSD','KLN','SAP','AHD','BRT','KNT','HRN','HUB','PHD','WLD','SYN','IEC','LKT','SKT','WEB','AFM','PLA','FVQ','ARY','BQT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Read refs_online metadata"
}
```


### [2026-09-05T17:27:37.206Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/n
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
```


## [2026-09-05T17:27:41.647Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','FSD','KLN','MON','IRN','AHD','BRT','WLD']:\n    v=d[k]\n    print('==',k, {kk:v.get(kk) for kk in ['local_file','page_offset','lookup_hint','scans']})\n\"",
 "description": "Page offsets for key refs"
}
```


### [2026-09-05T17:27:43.472Z] TOOL RESULT

```
== POK {'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", 'scans': None}
== FSD {'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.", 'scans': None}
== KLN {'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", 'scans': None}
== MON {'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'scans': None}
== IRN {'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt'], 'page_offset': '222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.', 'lookup_hint': "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", 'scans': [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf', 'first_printed': 1, 'last_printed': 210, 'pdf_offset': 11, 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt'}]}
== AHD {'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", 'scans': None}
== BRT {'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.", 'scans': None}
== WLD {'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.", 'scans': None}
```


## [2026-09-05T17:27:46.335Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: dānu\" POK_full.txt | head -20\necho \"---- surrounding\"\ngrep -n -i \"dānu\" POK_full.txt | head -30\necho \"==== POK_01 leaf for p.175 = leaf 183\"\nawk 'BEGIN{RS=\"\\f\"} NR==184' POK_01.txt | head -80"
}
```


### [2026-09-05T17:27:47.994Z] TOOL RESULT

```
---- surrounding
==== POK_01 leaf for p.175 = leaf 183
kk.  ö(pQvg)f  M fm^brü  Gen.  PL  ,supercilia';    unklar  sind  mir.  PL   abrait  (*abrant-es  oder  -^' *abranti)  , Augenlider,    Brauen',   desgleichen    mbr.    abrant   ,Braue',    cjmr.    ^ amrant  ,Augenlid',  die  Specht  (Dekl.  83,  162)  zu  lat.  fröns  ,Stirn'  stellen möchte;  aber  Vokalismus  und  Bedeutung  weichen  ab;
173
^trs.  hrü,  aisl.  hrürij  PL  brynn  ^B^-aue^  (kons.  St.,  aus  *brutoün-,  vgl. *ULiuiün,  tungo,  kontrahiert  und  dadurch  zur  flexivischen  Sonderentwicklung geUaügt).
lit.  hruvis  m.  ,Braue^,  zem.  auch  h-unes  PL,  apr.  xüiihri  f.  ,Wimper^  (scheint Umstellung  aus  Hruiui);
^\)cr,  bnvh  (ursprünglicher  Nom.  *bry,  wie  kry  :  kr^v^)^  skr.-ksl.  obvhiih, skr.  obwa  usw.  ^Braue^
Kine  e-Abl.  bkriie-  mit  silbisch  gewordenem  r  sieht  Trautmann  KZ.  44, 223  in  lit.  birwe  =  bruvis.
Toch.  A  'pärwän-j  B  pämoäne  (Dual)  ^Augenbrauen^
WP.  11  206  f.,  Trautmann  38.
2.  hhrü'f  bhreu-  ,Balken,  Prügel^;*  auch  als  Übergang  über  ein  Gewässer: ,Brücke^
Aisl.  &rü  f.  ^rücke*;  aisl.  bryggia  , Landungsplatz,  Hafendamm^  ndd. brügge  ds.,  ahd.  brucca^  as.  -bruggia,  ags.  brycg  ,Brücke^,  bair.  Bruch ,Bretterbank  am  Of  en^  ags.  brycgian  ,pflastern^  (ursprgl.  mit  Holzprügeln), Schweiz,  brügi  (ahd.  *brugi)  ,Holzgerüst^,  brügel  ,Holzscheit^,  mhd.  brügel ,Knüttel^,  nhd.  Prügel  (,Brücke^  ist  also  ,Balken;  Knüppelweg^) ;
gall.  briva  ,Brücke^  (Hhreua)]
abg.  br^v^no  ,Balken^,  skr.  brv  f.  ,Balken^  Stegbrücke^  (usw.,  s.  über  die slav.  Formen  Berneker  92).
Unklar  ist  der  Guttural  in  den  germ.  Formen:  *brugi-  aus  Hruui-, oder  k-  Suffix?  S.  Kluge^i  unter  ^Brücke'  und  Specht  Dekl.  2113  f^^  ^er Zusammenhang  mit  1.  bhrü-  annimmt.
WP.  II  207.
bhrüg-  ,Frucht;   genießen,  gebrauchen^,  vielleicht  ältest  ,sich  Früchte  zum
Genüsse  abbrechen  oder  abstreifen^  und  dann  zu  *bhreu-   ,schneiden'
(vgl.  dort  zur  Bed.  ai.  bhdrvati  ,kaut,  verzehrt^,   auch  bsl.   *bhreu-q-,
-k-  ^darüberstreifen,  abbröckeln').
Lat.  früx,  -gis  f.  ,Fruchf  ==  umbr.  Akk.  PL  frif^fri  ,fragesS  \^i.  frügl
(Dat.  *,zum  Gebrauche^  =)  ,tauglich^,  fruorj  -i,  früctus  und  fruitus  siim
.genieße'^   (aus  *früguor,   das  für  *frügor   eingetreten   ist?),  früniscor  _,ge-
nieße'  {^früg-nlscoi^,  frümentum  ^Getreide',  osk.  fruktatiuf  (^frügetätiöns)
,früctus^
Got.   brükjan,    ahd.    brühhan,    as.    brükan,    ags.  brücan   ,brauchen^^   got. brüksj  ahd.  brühlii,  ags.  bryce  ,brauchbar^ WP.  II  208,  WH.  I  552  f.
i
174
hhrugh-no-  ^Zweig^  Stengel^  vielleicht  in   Beziehung-  zu   hlireii-  ,sprießenc Cymr.    hrioyn-en   f.    ,Binse^;   acorn.    brunnen   gl.    juncus^   scirpus^,  brej hroenn-enn  ds.  (aus  urk.   *hrugno-)]  ags.  hrogn{e)  f.,  ^Zweig,  Busch^,  noi* dial.  hrogn{e)  ^Baumzweig,  Kleestengel,  Himbeerstrauch^ WP.  II  208.
bhudh-m(e)n     ,Boden^;     einzelsprachlich    teils     zu     *bhudh-mo-,     teils .  i^ *bhudh-no-j  daneben  mit  schon  idg.  Metathese  *bhundho-  >  *bhnnd(A
Ai.  budhnd-h  ,Grund_,  Boden^;  av.  Mnö  ds.  (*bJiundhno-
```


## [2026-09-05T17:27:54.527Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=185 && NR<=187 {print \"=== leaf(1-based) \" NR \" ===\"; print}' POK_01.txt | head -120"
}
```


### [2026-09-05T17:27:55.953Z] TOOL RESULT

```
=== leaf(1-based) 185 ===
),  daraus  ent lehnt  arm.  bun  ds.,  während  arm.  an-dund-lc  ^Abgrund^  aus  *bhundl assimiliert  scheint.  Aus  uriran.  *bundhas  stammt  tscherem.  pundas  ^Boden^
Gr.  Ttv&^rjv  (*cpvd'-)  m.  ,Boden,  Fuß  eines  Gefäßes^  nvvöa^  m.  ds.  (f (pvvda^  nach  Ttv-d-f-ii^v,  Schwyzer  Gr.  Gr.  I  71,  333).
Maked.  ON  TLvöva  (*bhudhna),  dissimil.  Kvöva?
Lat.  fundus,  -l  m.  ,Boden  eines  Gefäßes,  Grund^  {*bhundhos)j  profundvS\ ,t\Qi'  =  mir.  bond,  bonn  m.  ^Sohle,  Grundlage,  Stützet
Ahd.  bodam,  nhd.  Boden,  as.  bodom,  ags.  *bodm  >  mengl.  bothem  ml neben  ags.  botm  m.  >  engl,  bottom  und  ags.  bodan  ,Boden,  Grund^,  an.^ botn  ,Boden^,  ags.  bydme  ,Schiffsboden^  neben  bytme,  bytne  ds.,  aisl.  bytna ,m  einen  Boden  enden^,  mit  unklarem  Dental  Wechsel;  es  scheint  ein  urgerm. *bupma-  zugrunde  zu  liegen,  das  wohl  analogisch  zu  erklären  ist;  vgl. Petersson  Heterokl.  18,  Sievers-Brunner  167,  Kluge ^^  unter  siedeln.  Über nhd.  Bühne,  ursprgl.  ,Bretterboden',  angebl.  aus  germ.  *buni,  idg.  Hudhniä, s.  Kluge  ^^  unter  Bühne.
WP.  II 190,  WH.  I  564f.,  867,  Porzig  WuS.  15,  112 ff.  (dagegen  Kretschmer Gl.  22,  116);  vgl.  auch  Vendryes  MSL.  18,  305ff.
hhügO'Sf  Koseform  bhukko-s  ,Bock^  (fem.  auf  -ä  ,Ziege^).
Zigeun.  biczni  ,Ziege'^;  av.  büza  m.  , Ziegenbock*",  npers.  buz  ,Ziege^ ,Bock^;
arm.  buz  ,Lamm^;
mir.  bocc,  pocc,  nir.  boc,  poc,  cymr.  bwch,  com.  boch,  bret.  bouch ,Bock^,  dazu  mir.  boccänach  ,Gespenst^;
germ.  '^bukka-  (nach  Pedersen  Litteris  7,  23  f.  aus  dem  Kelt.  entlehnt?) in  aisl.  bukkr,  bokkr,  bokki,  ags.  bucca,  nengl.  buckj  ahd.  mhd.  boc,  -ckeSf nhd.  Bock.
Das  im  Konsonantismus  abweichende  ai.  bukka-h  ,Ziegenbock^  (unbelegt) ist  wohl  von  bukkati  ,bellt^  (s.  unter  1.  beu-,  bu-)  beeinflußte  hypochoristische Umbildung  eines  *bhüja-  =  av.  büza-.  Auch  npers.  dial.  boca  ,junge  Ziege', päm.  buc,  bü^  scheinen  Ergebnis  ähnlicher  Umbildung  zu  sein.
WP.  II  189  f.,  Pedersen  Litteris  7,  23  f.,  Martinet  Gemination  182.
D.
dS'  .Hüssig-,  fließen^  dänu-  f.  ,Fluß^
Ai.  dä-na-  n.  .die  beim  Elefanten  zur  Brunstzeit  aus  den  Schläfen uuellende  Flüssigkeit^,  dd-nu-  n.  f.  jede  träufelnde  Flüssigkeit,  Tropfen, Tau^7  av.  dä-nu-  f.  ,Fluß,  Strom*^,  osset.  don  ,Wasser,  Fluß^;  russ.  FIN  Don^ crräcisierter  skyth.  FIN  Tava'ig]  die  russ.  FIN  Dniepr  und  Dniestr,  alt  Dana- pris  und  Danastius  aus  skyth.  *Dä7iu  apara  ,hinterer  Fluß^  und  *Dänu nazdya-  ^vorderer  Fluß^;  av.  YN  Dänavö  Fl.  ,Flußanwohner^  (im  Rgveda Zu  Wasserdämonen  geworden,  fem.  GN  Dänu-),  skyth.  Nomadenvolk,  auch in  Griechenland,  daher  (?)  gr.  VN  Javaoij  ägypt.  Danuna ;  mit  Formans  -mo- arm.  tamuk  ,feucht,  benetzt^,  tamkanam  fyQalvu),  madefio^  und  vermutlich o-r.  ör]fj.6g  (urgr.  Q  oder  r]?)  ,Fett  von  Tieren  und  Menschen^,  womit  alb. dhj
=== leaf(1-based) 186 ===
 ame  yFettj  Speck,  Talg^  in  noch  nicht  geklärter  Weise  zusammenhängt; das  Fett  kann  als  das  beim  Braten  flüssig  werdende  benannt  sein  (vgl. aksl.  loj  ,adeps'^  :  lijati  ,gießen^).  Hierher  auch  kelt.  Dänuvius  ,Donau'^, gall.  ON  Condäte  ,Confluens^;  sechs  engl.  Fl  Don  (*dänu-)j  cymr.  FIN Donwy  (*dänuuia).
Benveniste  stellt  zu  arm.  tam-uk  noch  hett.  dame{ii)k-  ,als  Regen  fallen' (BSL  33,  143).  -
WP.  I  763,  M.Förster  Tkemse  145 f.,  Kretschmer  Gl.  24,  1  ff.,  15 ff., Mel.  Pedersen  76  ff.,  Benveniste  BSL  33,  143.
da  :  dg-  und  däi-  :  d9i  :  di-  ,teilen,  zerschneiden,  zerreißen',  ursprgl.  athemat. Wurzelpräsens;    Nominalbildungen    dä-mo-s  f.  ,Volksabteilung',   dä- ter-   ,Zerleger',   dä-tro-m  ,Zugeteiltes',   dä-tu-   ,Teil',   ddi-lO'  ,Teil-, di-t-  ,Zeitabschnitt'. Ai.  däfi,  dydti  ,schneidet  ab,   mäht,   trennt,  teilt',  Partiz.  dind-h,  ditd-hj komponiert  ava-ttah  ,abgeschnitten',  diti-h  ,das  Verteilen',  dänam  ,das  Ab- schneiden', dändm  n.  , Verteilung,  Teil',  dätu  n.  ,Teil',  dätdr-  m.  (=  Sai- 'TQÖg)    ,Schnitter',    däträm    , Zugeteiltes',    dätram    n.    ,Sichel',    npers.    dära ,Gehalt',  das  ,Sichel';  ai.  dayä  ,Teilnahme,  Mitgefühl'  =  ddyate  (^ddi-etai) ,teilt,  nimmt  Anteil,  hat  Mitgefühl;  zerstört'.
gr.  daioiiai  med.  ,teile,  verteile'  mit  wohl  nach  Fut.  daiaoi  und  den folgenden  Worten  bewahrtem  i  (lautgesetzlich   ddrjTat  Konj.  0  375  ,wird
176
zerstört);  daig^  -rög,  dairrj,  hom.  auch  daityq,  -voq  ,Portion^  Mahl^  Opfer'  (; dätu)]    SairvfKbv  ^Gast'  (als  ^dem  Mahle    beiwohnend'),   dairgög  ,der   Y^ Schneider' (:  ai.  c^ä^ar-),   daitgöv  jPortion^  (:  Si.i.  dätrdm]    das   ai   dieser  i Worte  ist  teils  lautgesetzlich  —  äi,  di  — ,  teils  analogisch,  wie  im  kr? Perf.    dedaia^ai    zu    öarso^uaL,    vgl.    auch    kret.   daTaig    ^Teilung',    xa^? daiaxal  ^Verteiler  von  Früchten'),  daivvj^i  ,bewirte^  wohl  auch  Salftcov ,Gott,  Göttin;  Geschick'  (eigentlich  ,zuteilend;  oder  ,Totengott  als  LeicheJ fresser',  Porzig  IF.  41,  169 ff.,  Kretschmer  Gl.  14,  228 f.;   über  des  Arcl lochos  daliJ,cov  ^darjf.Lcov''  s.  u.  *dens-  ,hohe   Geisteskraft');    öalZw,  Fut.  -[ Aor.  -fa  ,teilen,  zerschneiden,  zerstören'  (auf  Grund  eines  *dä-J^6-g  ,z^ schnitten,  zerstört'),  U-öaxog'  dtöialQsrog  Hes.y  ödvog  n.  ,Zins,  Wucher' (s Grund  eines  Partiz.  *dd-n6-s  =  ai.  dind-hj  vgl.  ddvag'  fisglöag)]
gall.  arcanto-danos  ,monetarius'  als  ,das  Silber  verteilend'.
Mit  Formans  -mo-  :  dämos  f.  ,Volk' :  gr.  dfjf.Log,  dor.  öänog  m.  ,(Voll abteilung)  Volk,  Gebiet;  in  Atben  der  einzelne  Gau',  air.  däm  f.  ,Gefolj Schaft,  Schar',
=== leaf(1-based) 187 ===
  acymr.  dauii  ,cliens',  ncymr.  daw^  daiof  ,Schwiegersohn4 offenbar  alter  fem.  o-Stamm;  dazu  hett.  da-ma-a-is  (damai§?)  ,ein  Andere Fremder',  aus  ,*fremde  Leute',  ursprgl.  ,*Volk',  Pedersen  Hitt.  51  ff.
Mit  Formans  -lo-  vielleicht  aksl.  däh  ,Teil'  (*ddi-lo-)  (s.  unter  *di , spalten');  über  air.  fo-dälim  usw.  s.  ebendort.  Hierher  gehört  wohl  auci got.  dails  ,Teil',  runeninschr.  dali]lipun  ,teilten',  aisl.  deillj  ags.  dcel,  ahc teil  m.  ,Teil';  aisl.  deila  f.  ,Teilung,  Zwiespalt',  ahd.  teila  f.  ,Teilun^ aisl.  deila j  ags.  döelan,  ahd.  teilan  ,teilen'  usw.  Sie  können  kaum  aus  dei SlaA^,  wohl  aber  aus  dem  Ven.-IUyr.  stammen,  da  die  Wzlform  "^ddi-  ii südillyr.  PN  Dae-tor  bezeugt  ist.  Eine  Nebenform  idg.  dhdi-  neben  ddi Aväre  unglaubhaft.
Mit  Tiefstufe  di-  :  arm.  ti.  Gen.  tioy  ^Alter,  Jahre,  Tage,  Zeit'  {*di-t[^ oder  *dl-to-y  "^di-tä),  ahd.  zU  f.  (n.  Isidor),  as.  ags.  tid,  anord.  tid  f.  ,Zeit Stunde'  {*tip-,  idg.  *dl-t-,  ursprgl.  ,Zeitabschnitt'),  dazu  anord.  fidr  ^üblich^ häufig',  ags.  tldan  ,vorfallen',  anord.  tida  ,trachten,  streben';  anord.  tl-i ,zerpflücken,  einzeln  herausnehmen,  ausscheiden,  reinigen';
über  got.  til  ,passend'  usw.  s.  unter  2.  ad-,  über  got.  dails  unter  3.  <ZeZ;|
hierher    dagegen    ahd.   zlla   ,Reihe,    Linie'^    westfäl.    tue   ,Garbenreihe';J nhd.  Zeile,  wohl  aus  *tld-ld-.
p-Er Weiterung  däp-,  dQp-:  dop-no-,  -ni-  , Opfermahl': ai.  däpayati  ,teilt';  arm.  taun  (*dap-ni-)  ,Fest';  gr.  ddjtTü)  {*da7ti(ü)\ .zerreiße,  zerfleische,  zerlege',  mit  Intensivredupi.  Sagdamü)  ,zerreiße, {yiTTjfAaTa)  verprasse',  öanavri  f.  ,Aufwand,  besonders  aus  Bewirtung  (;  dafi} erwachsender',  dartavog  ,verschwenderisch',  öartaväa}  ,wende  auf  (daraus^ lat.  dapinö  ,tische  auf),  öaipdög  (Empedokles),  öayjdrjg  ,(*verschwenderisch)j
üppi^;
177 reichlich;    freigebig^;    lat.    daps    /^Portion)    Mahl^   Schmaus,    bes.
'  f  »niiahl*  dammim  ^Verlust,  Schaden,  Nachteil,  Geldbuße^,  damnösus  ,ver- A  blich^  (*dap-no-  :  öaTiavt],  anders  Pedersen  Hitt.  42);  anord.  tafn  (*dap- )  Opfertier,  OpfermahF,  vgl.  den  germ.  GN  Tanfana  (Tacit.),  wenn US  *tafnana,  Marstrander  NTS.  1,  159.
Aus  dem  Genn.  reiht  man  noch  vieles  an,  was  eine  Bed.-Entw.  von «erteilen^  zu  ,zerreißen,  zupfen,  kurz  betasten,  kurze  täppische  Bewegun- gen machen^  u.  dgl.  voraussetzen  würde;  am  nächsten  der  Bed.  von  öa- naväv  damnum  kommt  aschw.  tappa  und  iapa  ,ein  Ende  machen,  ver- lieren^;  aisl.  tapa  ds.;  afries.  tapia  ,zupfen^,  ags.  tssppe  f.
```


## [2026-09-05T17:28:17.059Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT dānu (col ~732?) ===\"\ngrep -n \"dānu\\|dänu\\|Dānavō\\|Dänavö\\|Flußanwohner\\|Fluss, Strom\" BRT.txt | head -20\necho \"=== KNT ===\"\ngrep -n -i \"danu\" KNT.txt | head -10\necho \"=== AHD watkins da- / danu ===\"\ngrep -n -i \"danu\\|DANUBE\" AHD_watkins1985.txt | head -20\necho \"=== IEC ===\"\ngrep -n -i \"dānu\\|Danuvius\" IEC.txt | head -10\necho \"=== WLD Bd1 p.763 ===\"\ngrep -n -i \"Danuvius\\|Dänuvius\" incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-09-05T17:28:17.179Z] TOOL RESULT

```
=== BRT dānu (col ~732?) ===
9404:/laca  'van  yail  hapia  V.6i,^;  —  vispähu  Kömem':    aLdänunamca    (sd.)   yav<.
10879:•  j.  xStävay-  Adj.  'zur  Familie  der Xstavay  gehörig,  Xstavi-^a.nvi^ -.  ysi  taxma 'vayS  dänubyö  azm  pilana  Yt  13. 37 ;  38.
11889:•  j.  taJia  Adv.  i)  'dann,  alsdann':  yat.. altma  aisa  mlirika  f  apührJm  (sd.)  tiija- ja/V.5.45;  8.'36;  —  ä^ritim  f  ..vlväla- yantu  V.Ä16;  17,  18;  —  /•  kunavd  .  . Jata  paiiyante  Ytio.  113;  —  avavat  f ya>a  cd^wärS  »niavs  Y.g.sq.  a)  es geht  ein  Satz  mit  ^«i  'wenn' voraus:  _>'«( nasus  anaiwiynixta  .  .  f  dim  .  .  %ris maygm  avakanaym  V.  1^.37.  b)  es folgt  ein  Satz  mit  yat  'wenn';  P  nS  jam- yat  avairihe  .  .  yat  bfnz?m  baräi  ai'tra viläm  Yt.io.113'*.  2)  'damals,  da": yüzsm  f  taurvayata  ibalsä  dänunqm  Yl 7J.38;  38;  —  im  Wechsel  mit  tat  (sd,); f  dim  ahurS  mazdä  avqn  (Sp.  112  m.)  .. tat  aps  uruarisla  Yt, Ä7;  — fravasayS .. yi  .  .  tatja  nijasfn  (Sp.  500  m.)  xslreiwyö *tat  ySi .  .  xitavayS  .  .  aztn  pisana  Yt.  13. 37.  a)  mit  folg.  yat  'als':  fravasayS yil  /°  sriowa  histinta  yat  *maityu  damqn dai'nt9m  Yt. /j.76,  3)  'alsdann,  ferner'; ya  haca  da^ayasnaHbyS  . .  apa.bara  (sd) aya  raiufrisf  yat  paiti.banHti  "was  man . ., damit  ist  man  r.\  ferner  {mit  dem),  was.." N._54;  —  caturqm  asvqm  *'kahmaiHi  t' */rayafvAqm  (sd.)  N.öj.  4)  'so,  derartig'; es  folgt  ya%a:  t  ayaos  (sd.)  ya%a  .  .  Yt Ä 1 4^.         Undeutlich:  k^a  nara  t°  mara
11894:'damit,  auf  dass'  vorher:  yat  yavo  (sd.) pourus  baväf  aha  ma'hnm  *t'  ^  mairyat ^•3-a-  3)  'damals,  da',  ini  Wechsel mit  ta6a  (sd.)*':  tala  dim  akurS  mazdä avqn  (Sp.  1 1 2  m.)  . .  t°  apu  urvaras<a  YL 8."];  —  fravasayS  .  .  yä  .  .  laoa  nijasm (Sp.  500  m.)  xÜiviwyS  *pi^  yöi  taxma xstävayB  dänubyS  az>n  pthnh  Yt.  13. 37.  4)  'dann,  alsdann':  yas>  t  *api- vataiti  (sd.)  parmtarim  (sd.)  issil  N. 12.  a)    zusammen    mit    aaf:    US  patti
13405:•  j.  dänu.drä]ah-  Adj.  'von  der  Länge
15270:•  j.  pantay-  m. ;  j.,  g.  pa3^  m.,  f."  1)  Tfad, Weg':  °%qmca  ''vTlanni  . .  '^amcä  hanja- manä  Y.42. 1;  Ytn.4,  *VyL54; — pairi- %wB  bavaiti  'ti  (NS.)  ytm  dänus  paiti Aog.  77;  —  avaisqmca  "^J  (AP.)  phntS yitn  ismti  mihrS.dru/s  Yt.  10.  45 ;  —  yqm °'hB  aiti  Aaomö  frasmU^LS.^y, — ät^hqm (näml.  fravasinqm)  raya  .  .  kvar»  ava •5fl(lS.)  aa'ft"  Yt. /^.  16;  16'; — /ravasayd . .  yi  .  .  apqm  .  .  srfri  'äJ  äaBayänti  .  . äat  tä  nOrqtn  fralacinti  masdt^atsm  paiti "tqm  (AS.)  Yt7^.53t;  57;  —  ma  dim p)r?s3 .  .yim  xnjant?m  . .  "Iqm  atwihtn  (Sp, 1 49  m.)  H.a.  1 7 ;  Vyt42 ;  — yS  (näml.  tiltryö) avatat  fravatäite  .  .  daraiurvatsfm  paiti 'tqm  YLÄ35;  —  gaus  . .  varai^itn (sd.) 'tarn  axatte  Ytio.38;  V,j.  11;  —  'hqm (als  Kasus  des  Ziels)  zrvBJstanam  jasaiti yasla  drvaite  yasca  asaone  V.  j^.  29;  — yagsqm  (nämL  amjlanam)  raoxinätihB 'ianö{tiP.)  ävayatqm  avi'xai)%räYtiJ.84; ^^■3;  —  yS*  "äa  (IS.)  usbarmte  (sd.) spänasia  .  .  V.  Ä  14;  —  *xiäyete  .  . *utdarjhucit  °äo  haxtsit  (sd.)  N.  5;  — yaihe  (nämL  mi^raAe)  datna  mazdayasnis jc'jfc(sd.)  '^?  rälaiü  Yt/O.  68;  F.  jo;  — pairi  Sl .  .  tni^irS  frälayat  'tqm  (AS.)  Yt 8.  7;  38,  10.  y,  —  airi/B(sd.)  'tatitm  yaia jahika  V.i_j,48;  — yesi  äf!  anhat  aniarat nofmat  oHe  '%a  (als  AP.)  V.Ä'104;  — k<&a  nö  fraourvaaayäiti  alahe  (sd.)  paiti 'tarn'''!  Yt, /o.  86;  —  AämB.syao^na  tl  .  . bavainii  asahe paiti  'tqm'^'V.4-4y^yt-4'^', —  ä'ji/  syao%a»äis  AitvascS  (sd.)  asahyä nqsvh  '%B'''>  (GS.)  Y.jr.  13;  —  afvü  'tä yö  asahe^^  vTspe  anyailqm  apantam  (sd.) Y.  72. 1 1 ;  —  iisa  nä  asä  '^B  vanhius ji^altSng  (sd)  mananhB  Y.34- 1>;  —  tarn ,  .  vistäspB  ,  .  nqiat  vanhSuS  padibls^ manatths yqm  astim  (sd.) ..  Y.57.  »6;  — dät3Ä5{%±)  ?r>eOs  °iia..Y.S3-  2.  a)  mit Angabe  des  wohin?  durch  a)  Lok.:  a  pai^l ..  iA«a«ff(ir?  "auf  dem  Weg  zum  Haus,." Y.  50. 4.  ß)  ä  mit  Akk. :  »nzüs  . .  pahd . .  halhyTng  (sd.)  *J  jflj  Y.  43. 3.  t)  ^  ™'t Abi.:  uj^i  ä  mzüi  (sd.)  «äff  ya^  . .  Y.
19311:3a; —  daevanqm  anSyantqm  ahmaUa  'näi aimäiüi  °tiahe  nmans.palSe  Y.  52,  2 ;  Yt  15. t*;-~fpfvru'^wa,.aora  mainyB kaca  °nat V.  11.10;  — yaoiääta..bun  'na  V. i/.a;  1, 4,  12.2;  —  yat  aiiS  nä yS yaoldi^tyS  hala aHiiyd  'naiiiyö  xshats . .  psrayst  V.g.  39; 40,  13.22;  —  yat . .  aiiqmUt  •»anqm[ca] caratB  dva . .  V.  y.  49 ; — vTspanqm  akmya •ne  nabänasdistanqm  Y.  26'.  7 ;  —  *katämS *naAe*'>  a%auruntm  (sd.)  pärayai  N.  /;  Yt 2.11;  —  t^a.vasatfitha  avi  'tarn  airya- maim  V.  22.  7;  13;  —  tum  . .  sara%uhra *nahe  pourusaspahe'H.  g.\y,  V. /p.  4,  46, Yt  i^.  36;  —  olsmanqmHt  .  ,  vazyäi/  .  . ratsui  'tarn  fränäiayata  A. j.  5:5;  —  us3.- hista  haia  gätvs/rasasa  haca  d^mänSi'-'' Yt  16.2;  —  yavat . .  späna  dt/  hapta  'tia *pairiJ(üahi{sA.)  bavqn  V.J5.4S;  — fratara (sd.)  haca  'na  v>r3syqn  .  .  V.iö.^;  — nistara.naOnal  'nahe  V.  17.  7 ;  6. 43,  g.  33, Yt//.  60;  —  mahsmya  'naÄe  N.yX;  — parepasca  'nahe  V.  y.  45,  46;  45;  —  k»m kfmHl  aipi  'ne  gatu  *saSe  Yt5. 102;  — raocamtn  paiti  'nahe  V.  7. 14;  —  ysi  °nä hqm.6arämahi  .  .  ätnmca  .  .  3at  paslalta ahe  'nahe  spa  vä  na  vä  iriäyäj  .  .  us haca  aHbyS  'naiiby3  baraym  . .  ätnmia  . . ku%a..älr7m  aiti  barqn  ava  aitim  'rum..1 V.5-39-4i;5'33';  —  '""  '»"^^  vfti  vTsi hr3yff  kata  (sd.)  uedat^yan  aetahe  yat iristahe  V.  5.  10;  —  ahe  'nahe  upa.- %'Ui»nsqn  (sÄ)  upa^w3T»tayqn  V,  Ä  10; — yui  .  .  iristim  upaJi?r3%wSJar3m  (sd.) avajtanqn  ava  .  .  iristim  baraytn  avaha 'mm  himaym  upa  .  .  'ntm  baötayqn  . . yezi  . .  *fum  upaJ>jr3%ws.tanm  avaxanqn ava  ..  °n3m  baraytn  V.  4",  af.;  —  ratu- fris  havS  yä  'nahe  *paitiricyehe  (sd.) ^■55-  8)  bes.  im  Gegensatz  zu  Ge- meine, Gau  und  Land*);  'vsa%Pi:^..yS  hu- dänul  damanahya^  xla'hr?m  idßirahya vä  dahySu/  vä  . .  frada%äi  (sd.)  aspfrazats Y.31. 16;  —  3  eJ  'mmf'  vUsm  vä  ist^rtm vä  dahyüm  vä  ädat  dusitäcä  (sd.)  .  ,  Y. ,3/.  18;  —  im  jAw.:  mikrS  .  .  ahmäi frasanäayäti  'tamca  vfs^m^a  zantümca dahyümca  daiiihusasilmca  Yt/o.  87;  18, Y.  62. 5,  V.  Ä  1 03,  N.  6';  —  «5 ..  ahmt  'ne .. aähe  vSse  . .  ahmt  *zantvlf  . .  a^he  da^kvB ftim  vaoSata  . .  ahurpm  P./7;  Y.5.  aS,  Vr, 12.  5,  N.(?;  —  *'nyaca  (LS.)*'  vjsyaca  tarda- vaca  *da^havaca  Vr. /2.  gj  —  yujyastTm haia  *'näp'>  a^a  [. .]  vTsal  ha%r?m  {ha&i)
20775:12.  zu  3)  AvS  mä  rtä  srava  mSnndat (sd.)  yS  acistgm  *vamaAhl  (sd.)  aogfdä gqtn  . .  yasca  ää'hSng  dngvats  dadat yascä'  ..  Y. 32.10;  2g.<); —  kB  AvS yS mä  arfdrS  cSi^at  .  .  Y.46.');  —  pfrtsa avap  ya%ä  hvB  yS  Audänui  . .  x^a- SrjjM  ..  fradahäi  (sd.)  asp>r3satä  ..  yada hvB  (zu  1)  anAat  Y.31. 16;  —  kvB.,y5  nä inzsi  savatshB  pa%ö  siMt  (sd.)  Y.  43. 3;  —  hvS  . .  yaAmai  zavSng  jinta  25.3; —  5.  aocbY.49. 5  im  Anhang.         b)  'Äa-
21895:Verszeile:  y  tX>läyär»A3  {sd.}  is^  xsa- ärwwÄr  tavawhqm  Y.2&9;  —  y  aiiiyB ahura  aogB  (sd)  ^Ua  aiü  xü&rjm^  Y. 2g.  loj  11;  —  y  taha  taurvayaia  vtrr- %nm  dänunqm  "ihr  seid  es,  die  damals.." Yti^.  38;  38;  —  y  va^uhi  nisrinaeta mr^rarftavUa  . .  Yt  13. 34;  —  •hmat Maffia  baxiayaia  Vjrt  8.  a)  vor  dnem attributiven  Relativ:  y  ySi  mafyaba  V, 7.5s;  F.rff;  —  y  yBi  matdayasna  V. 7.71.  3)  sonst  belieb^:  f^irym  tBÜ .•ztmät  3?ama  ..  ditfata  Ny.^.  11;  — rumH,yu^iam  ns-.j  np.'MM'»'^  ^ JT  '^"'  xiayamni raUSt.. rnui*«.— VgLS2<5i').  — Pu.:fc«i*,;Y.Äy.ai;  —  tai  nB  däyata  y  yatata  Y.
23550:•  j.,  g.  västra-  n.  'Weide';  i)  'was  das Vieh  weidet,  Gras,  Futter':  pars  *wmS  .. *da>ihsui  aaÄaj  dfrptj(sd.)  *r>m  V.2. 34; —  gSmia  "roAeca  YLjj.  100',  ig.  SA;  — I  Hat  .  .  ahe  nmänake  frapObwS  gaui  .  . \frapiiiwS  'nm  V.J.  3;  — gavsi  .  .  fral^- yamaht  räma^  °r?tncä  dazdyai  (sd.)  Y, J5.  4;  —  ahurahyi ..yasramila  vahm^mlä .  .  gsulca  'rsm  Y.JJ.  7;  —  gavSi  .  .  hyat htm  data  .  .  hads  'rS  gaodaya  %waxilT (sd.)  Y.  2g.  3;  —  'r>m  btnttm  (sd.)  gtrue ..gaodäyüm  nanm  Vr.z,  11;  —  :^ar>h»mca naire  .  .  'nmca  gave  huhhnhe  V.5.30;  — ■ \yavö  mi  maiys  ^arat  'rym  gave  Au^anhe I  V.5.30; —  yavaca  'raca  V.7.32;  —  yat !  bä  paiti  fraiit>m  kärayätt  .  .  yavanamca '  'ranqm(als  Obj.)/a  urvaranqmca  i^arihs.- bairyanqm  ".  .  Getreide  und  Gräser '  lind  Pflanzen  mit  essbaren  Früchten" iV.  J.  4;  g.  53;  —  as.danunqm(sd.)ca ,yavariqm  kasu.dänunqmca  °nanqm  Yt  S. \  39.  2)    'wo  das  Vieh  weidet,  Weide-
23653:•j.'vara^ra-n.  \y^^K':yäi3m..taurva- yata  'tym  dänunamyt.l3.^Z.  2)  'sieg-
28122:•  j.  zsm.fraStih-  Adj.  'von  der  Breite  der Erde,  so  breit  wie  die  Erde':  mi^nm  .  . yj  '%S  aiwyäiti  Yt/0.95;  —  °%S  niaf- ha/am  Yt  10.  44;  —  aisi/  badaza  . . '^aaAa  (APn.)"  dänu.drajar)ha  hvan.- bartzanha  "der  Aiay  Heilmittel . .,  die  so breit  wie  die  Erde,  so  lang  wie  die  Russe, so  hoch  wie  die  Sonne  sind"  Y.  60. 4.
28717:I  hye^  avahyä  kärahyä  mdküt^  ähc^  .  . Aauv(zat)..  Bh.j.  11;  s.nochBh.J.  19,  2.6, i2,_j.6,  9  (Sp.  i730u.).l  ß)  substan- tivisch: käuca  *anayä  »arä  vahu  manö jäginbuitarB  anhat  yS  gSui  uru^wari hqm.pä/räiti  (sd.)  ya'ha  hau  yS  nSit  iia V.^.48;  —  a/  hau  as  . . yS  ml asadayat . . V.5.S1;  J7.a;  —  nSii  hau  *taxm5  yH mit  *aj'a  *taxmd  F.  47;  46,  48,  26;  — pairi%wS  bavaiH  pantä  yim  dänus  päiti *häu^  dit  atvö  apairi%ws  yS  vayaos anamansdikahe  Aog.  77.  3)   auf  den
30617:46-  6;  —  p>nsä  aval  ya'hä  hvd  (zu  2  1  a) yi  hudänul . .  /rada^äi  (sd.)  asfifrvgatJ ^uiavas  (sd.)  , .  yada  h'  aahai  Y.  ?;. b)  adjektivisch,  nur  mit  na  (Sp.
30625:yi  hui  dadat  ..  Y.2(?.  9;  —  p^r^s/t  avat\»  j-  ^^a',  nur  KompA.:  sva.  Au"  (sd.). ya:ia  A'  y}  Audänus. .  asp^matä  Y.ji.  16;       ^^l-  ''"'"'■.  •*='*"°-
=== KNT ===
2425:On далай) as alternative to danu[vattyl, see §216; on d-zsnautzy and forms, see $208.
2514:OP danulvatiy|, Skt. dhánvati, stem pAr. dhan- va-; unless we should restore OP батат], like Skt. dhanulé, stem pIE *dhn-nu- (varying with -neu-, $210.I].!
3311:DPb = Danus, PERsEPOLIS в: OP only, in one line, on the garment of Darius; now in the Cabinet des Médailles of the Bibliothèque Na- tionale, Paris. Tm. Lex. 35-6 (1908); Wb. KIA xvi, 80-1; Sen, OPI 89 (1941).
3318:DN = Danus, Nags-1-Rustam: Some miles north of Persepolis, on the south face of a steep ridge known as Husain Küh or ‘Mountain of Husain’, there are four gigantie niches, cut in the shape of Greek crosses, and serving as en- trances to the tombs lying in the rock behind them. The second from the east is the tomb of Darius I, and bears inscriptions.
3344:DSo = Danus, Susa o: Bilingual, on a marble plaque; OP in 4 lines, АКК. in 5 lines. Scheil 21.50-60 No. 14 (1029); Kent, JAOS 51.221 (1931); Вга. WZKM 39.59-60 (1932); Sen, OPI 132 p (1941); Hinz, ZDMG 95.255-7 D?8d (1941).
4405:rauta : tya : Mudràyaly : danuvatiy : ab
5514:idan- vb. ‘flow’: Skt. dhdn-vati. датира] DZe 9 (or danu[taiy] mid., Wb. KIA 104, after al- ternative suggestion of Bthl. AiW 683); $216, §216.n1.
=== AHD watkins da- / danu ===
=== IEC ===
=== WLD Bd1 p.763 ===
79864: dhanvan- „trockenes Land" (s. *dhen- „Flache“). Danuvius „Donau“ kelt.
```


## [2026-09-05T17:28:38.153Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT headword dānu ===\"\ngrep -n \"j\\. dänu\\|dänu-\\s*f\\|'Fluss'\\|,Fluss'\\|Fluss\" BRT.txt | grep -i \"dänu\\|danu\" | head -10\necho \"=== grep dänu. lines ===\"\ngrep -n \"dänu\" BRT.txt | head -20"
}
```


### [2026-09-05T17:28:38.217Z] TOOL RESULT

```
=== BRT headword dānu ===
=== grep dänu. lines ===
9404:/laca  'van  yail  hapia  V.6i,^;  —  vispähu  Kömem':    aLdänunamca    (sd.)   yav<.
10879:•  j.  xStävay-  Adj.  'zur  Familie  der Xstavay  gehörig,  Xstavi-^a.nvi^ -.  ysi  taxma 'vayS  dänubyö  azm  pilana  Yt  13. 37 ;  38.
11889:•  j.  taJia  Adv.  i)  'dann,  alsdann':  yat.. altma  aisa  mlirika  f  apührJm  (sd.)  tiija- ja/V.5.45;  8.'36;  —  ä^ritim  f  ..vlväla- yantu  V.Ä16;  17,  18;  —  /•  kunavd  .  . Jata  paiiyante  Ytio.  113;  —  avavat  f ya>a  cd^wärS  »niavs  Y.g.sq.  a)  es geht  ein  Satz  mit  ^«i  'wenn' voraus:  _>'«( nasus  anaiwiynixta  .  .  f  dim  .  .  %ris maygm  avakanaym  V.  1^.37.  b)  es folgt  ein  Satz  mit  yat  'wenn';  P  nS  jam- yat  avairihe  .  .  yat  bfnz?m  baräi  ai'tra viläm  Yt.io.113'*.  2)  'damals,  da": yüzsm  f  taurvayata  ibalsä  dänunqm  Yl 7J.38;  38;  —  im  Wechsel  mit  tat  (sd,); f  dim  ahurS  mazdä  avqn  (Sp.  112  m.)  .. tat  aps  uruarisla  Yt, Ä7;  — fravasayS .. yi  .  .  tatja  nijasfn  (Sp.  500  m.)  xslreiwyö *tat  ySi .  .  xitavayS  .  .  aztn  pisana  Yt.  13. 37.  a)  mit  folg.  yat  'als':  fravasayS yil  /°  sriowa  histinta  yat  *maityu  damqn dai'nt9m  Yt. /j.76,  3)  'alsdann,  ferner'; ya  haca  da^ayasnaHbyS  . .  apa.bara  (sd) aya  raiufrisf  yat  paiti.banHti  "was  man . ., damit  ist  man  r.\  ferner  {mit  dem),  was.." N._54;  —  caturqm  asvqm  *'kahmaiHi  t' */rayafvAqm  (sd.)  N.öj.  4)  'so,  derartig'; es  folgt  ya%a:  t  ayaos  (sd.)  ya%a  .  .  Yt Ä 1 4^.         Undeutlich:  k^a  nara  t°  mara
11894:'damit,  auf  dass'  vorher:  yat  yavo  (sd.) pourus  baväf  aha  ma'hnm  *t'  ^  mairyat ^•3-a-  3)  'damals,  da',  ini  Wechsel mit  ta6a  (sd.)*':  tala  dim  akurS  mazdä avqn  (Sp.  1 1 2  m.)  . .  t°  apu  urvaras<a  YL 8."];  —  fravasayS  .  .  yä  .  .  laoa  nijasm (Sp.  500  m.)  xÜiviwyS  *pi^  yöi  taxma xstävayB  dänubyS  az>n  pthnh  Yt.  13. 37.  4)  'dann,  alsdann':  yas>  t  *api- vataiti  (sd.)  parmtarim  (sd.)  issil  N. 12.  a)    zusammen    mit    aaf:    US  patti
13405:•  j.  dänu.drä]ah-  Adj.  'von  der  Länge
15270:•  j.  pantay-  m. ;  j.,  g.  pa3^  m.,  f."  1)  Tfad, Weg':  °%qmca  ''vTlanni  . .  '^amcä  hanja- manä  Y.42. 1;  Ytn.4,  *VyL54; — pairi- %wB  bavaiti  'ti  (NS.)  ytm  dänus  paiti Aog.  77;  —  avaisqmca  "^J  (AP.)  phntS yitn  ismti  mihrS.dru/s  Yt.  10.  45 ;  —  yqm °'hB  aiti  Aaomö  frasmU^LS.^y, — ät^hqm (näml.  fravasinqm)  raya  .  .  kvar»  ava •5fl(lS.)  aa'ft"  Yt. /^.  16;  16'; — /ravasayd . .  yi  .  .  apqm  .  .  srfri  'äJ  äaBayänti  .  . äat  tä  nOrqtn  fralacinti  masdt^atsm  paiti "tqm  (AS.)  Yt7^.53t;  57;  —  ma  dim p)r?s3 .  .yim  xnjant?m  . .  "Iqm  atwihtn  (Sp, 1 49  m.)  H.a.  1 7 ;  Vyt42 ;  — yS  (näml.  tiltryö) avatat  fravatäite  .  .  daraiurvatsfm  paiti 'tqm  YLÄ35;  —  gaus  . .  varai^itn (sd.) 'tarn  axatte  Ytio.38;  V,j.  11;  —  'hqm (als  Kasus  des  Ziels)  zrvBJstanam  jasaiti yasla  drvaite  yasca  asaone  V.  j^.  29;  — yagsqm  (nämL  amjlanam)  raoxinätihB 'ianö{tiP.)  ävayatqm  avi'xai)%räYtiJ.84; ^^■3;  —  yS*  "äa  (IS.)  usbarmte  (sd.) spänasia  .  .  V.  Ä  14;  —  *xiäyete  .  . *utdarjhucit  °äo  haxtsit  (sd.)  N.  5;  — yaihe  (nämL  mi^raAe)  datna  mazdayasnis jc'jfc(sd.)  '^?  rälaiü  Yt/O.  68;  F.  jo;  — pairi  Sl .  .  tni^irS  frälayat  'tqm  (AS.)  Yt 8.  7;  38,  10.  y,  —  airi/B(sd.)  'tatitm  yaia jahika  V.i_j,48;  — yesi  äf!  anhat  aniarat nofmat  oHe  '%a  (als  AP.)  V.Ä'104;  — k<&a  nö  fraourvaaayäiti  alahe  (sd.)  paiti 'tarn'''!  Yt, /o.  86;  —  AämB.syao^na  tl  .  . bavainii  asahe paiti  'tqm'^'V.4-4y^yt-4'^', —  ä'ji/  syao%a»äis  AitvascS  (sd.)  asahyä nqsvh  '%B'''>  (GS.)  Y.jr.  13;  —  afvü  'tä yö  asahe^^  vTspe  anyailqm  apantam  (sd.) Y.  72. 1 1 ;  —  iisa  nä  asä  '^B  vanhius ji^altSng  (sd)  mananhB  Y.34- 1>;  —  tarn ,  .  vistäspB  ,  .  nqiat  vanhSuS  padibls^ manatths yqm  astim  (sd.) ..  Y.57.  »6;  — dät3Ä5{%±)  ?r>eOs  °iia..Y.S3-  2.  a)  mit Angabe  des  wohin?  durch  a)  Lok.:  a  pai^l ..  iA«a«ff(ir?  "auf  dem  Weg  zum  Haus,." Y.  50. 4.  ß)  ä  mit  Akk. :  »nzüs  . .  pahd . .  halhyTng  (sd.)  *J  jflj  Y.  43. 3.  t)  ^  ™'t Abi.:  uj^i  ä  mzüi  (sd.)  «äff  ya^  . .  Y.
19311:3a; —  daevanqm  anSyantqm  ahmaUa  'näi aimäiüi  °tiahe  nmans.palSe  Y.  52,  2 ;  Yt  15. t*;-~fpfvru'^wa,.aora  mainyB kaca  °nat V.  11.10;  — yaoiääta..bun  'na  V. i/.a;  1, 4,  12.2;  —  yat  aiiS  nä yS yaoldi^tyS  hala aHiiyd  'naiiiyö  xshats . .  psrayst  V.g.  39; 40,  13.22;  —  yat . .  aiiqmUt  •»anqm[ca] caratB  dva . .  V.  y.  49 ; — vTspanqm  akmya •ne  nabänasdistanqm  Y.  26'.  7 ;  —  *katämS *naAe*'>  a%auruntm  (sd.)  pärayai  N.  /;  Yt 2.11;  —  t^a.vasatfitha  avi  'tarn  airya- maim  V.  22.  7;  13;  —  tum  . .  sara%uhra *nahe  pourusaspahe'H.  g.\y,  V. /p.  4,  46, Yt  i^.  36;  —  olsmanqmHt  .  ,  vazyäi/  .  . ratsui  'tarn  fränäiayata  A. j.  5:5;  —  us3.- hista  haia  gätvs/rasasa  haca  d^mänSi'-'' Yt  16.2;  —  yavat . .  späna  dt/  hapta  'tia *pairiJ(üahi{sA.)  bavqn  V.J5.4S;  — fratara (sd.)  haca  'na  v>r3syqn  .  .  V.iö.^;  — nistara.naOnal  'nahe  V.  17.  7 ;  6. 43,  g.  33, Yt//.  60;  —  mahsmya  'naÄe  N.yX;  — parepasca  'nahe  V.  y.  45,  46;  45;  —  k»m kfmHl  aipi  'ne  gatu  *saSe  Yt5. 102;  — raocamtn  paiti  'nahe  V.  7. 14;  —  ysi  °nä hqm.6arämahi  .  .  ätnmca  .  .  3at  paslalta ahe  'nahe  spa  vä  na  vä  iriäyäj  .  .  us haca  aHbyS  'naiiby3  baraym  . .  ätnmia  . . ku%a..älr7m  aiti  barqn  ava  aitim  'rum..1 V.5-39-4i;5'33';  —  '""  '»"^^  vfti  vTsi hr3yff  kata  (sd.)  uedat^yan  aetahe  yat iristahe  V.  5.  10;  —  ahe  'nahe  upa.- %'Ui»nsqn  (sÄ)  upa^w3T»tayqn  V,  Ä  10; — yui  .  .  iristim  upaJi?r3%wSJar3m  (sd.) avajtanqn  ava  .  .  iristim  baraytn  avaha 'mm  himaym  upa  .  .  'ntm  baötayqn  . . yezi  . .  *fum  upaJ>jr3%ws.tanm  avaxanqn ava  ..  °n3m  baraytn  V.  4",  af.;  —  ratu- fris  havS  yä  'nahe  *paitiricyehe  (sd.) ^■55-  8)  bes.  im  Gegensatz  zu  Ge- meine, Gau  und  Land*);  'vsa%Pi:^..yS  hu- dänul  damanahya^  xla'hr?m  idßirahya vä  dahySu/  vä  . .  frada%äi  (sd.)  aspfrazats Y.31. 16;  —  3  eJ  'mmf'  vUsm  vä  ist^rtm vä  dahyüm  vä  ädat  dusitäcä  (sd.)  .  ,  Y. ,3/.  18;  —  im  jAw.:  mikrS  .  .  ahmäi frasanäayäti  'tamca  vfs^m^a  zantümca dahyümca  daiiihusasilmca  Yt/o.  87;  18, Y.  62. 5,  V.  Ä  1 03,  N.  6';  —  «5 ..  ahmt  'ne .. aähe  vSse  . .  ahmt  *zantvlf  . .  a^he  da^kvB ftim  vaoSata  . .  ahurpm  P./7;  Y.5.  aS,  Vr, 12.  5,  N.(?;  —  *'nyaca  (LS.)*'  vjsyaca  tarda- vaca  *da^havaca  Vr. /2.  gj  —  yujyastTm haia  *'näp'>  a^a  [. .]  vTsal  ha%r?m  {ha&i)
20775:12.  zu  3)  AvS  mä  rtä  srava  mSnndat (sd.)  yS  acistgm  *vamaAhl  (sd.)  aogfdä gqtn  . .  yasca  ää'hSng  dngvats  dadat yascä'  ..  Y. 32.10;  2g.<); —  kB  AvS yS mä  arfdrS  cSi^at  .  .  Y.46.');  —  pfrtsa avap  ya%ä  hvB  yS  Audänui  . .  x^a- SrjjM  ..  fradahäi  (sd.)  asp>r3satä  ..  yada hvB  (zu  1)  anAat  Y.31. 16;  —  kvB.,y5  nä inzsi  savatshB  pa%ö  siMt  (sd.)  Y.  43. 3;  —  hvS  . .  yaAmai  zavSng  jinta  25.3; —  5.  aocbY.49. 5  im  Anhang.         b)  'Äa-
21895:Verszeile:  y  tX>läyär»A3  {sd.}  is^  xsa- ärwwÄr  tavawhqm  Y.2&9;  —  y  aiiiyB ahura  aogB  (sd)  ^Ua  aiü  xü&rjm^  Y. 2g.  loj  11;  —  y  taha  taurvayaia  vtrr- %nm  dänunqm  "ihr  seid  es,  die  damals.." Yti^.  38;  38;  —  y  va^uhi  nisrinaeta mr^rarftavUa  . .  Yt  13. 34;  —  •hmat Maffia  baxiayaia  Vjrt  8.  a)  vor  dnem attributiven  Relativ:  y  ySi  mafyaba  V, 7.5s;  F.rff;  —  y  yBi  matdayasna  V. 7.71.  3)  sonst  belieb^:  f^irym  tBÜ .•ztmät  3?ama  ..  ditfata  Ny.^.  11;  — rumH,yu^iam  ns-.j  np.'MM'»'^  ^ JT  '^"'  xiayamni raUSt.. rnui*«.— VgLS2<5i').  — Pu.:fc«i*,;Y.Äy.ai;  —  tai  nB  däyata  y  yatata  Y.
23550:•  j.,  g.  västra-  n.  'Weide';  i)  'was  das Vieh  weidet,  Gras,  Futter':  pars  *wmS  .. *da>ihsui  aaÄaj  dfrptj(sd.)  *r>m  V.2. 34; —  gSmia  "roAeca  YLjj.  100',  ig.  SA;  — I  Hat  .  .  ahe  nmänake  frapObwS  gaui  .  . \frapiiiwS  'nm  V.J.  3;  — gavsi  .  .  fral^- yamaht  räma^  °r?tncä  dazdyai  (sd.)  Y, J5.  4;  —  ahurahyi ..yasramila  vahm^mlä .  .  gsulca  'rsm  Y.JJ.  7;  —  gavSi  .  .  hyat htm  data  .  .  hads  'rS  gaodaya  %waxilT (sd.)  Y.  2g.  3;  —  'r>m  btnttm  (sd.)  gtrue ..gaodäyüm  nanm  Vr.z,  11;  —  :^ar>h»mca naire  .  .  'nmca  gave  huhhnhe  V.5.30;  — ■ \yavö  mi  maiys  ^arat  'rym  gave  Au^anhe I  V.5.30; —  yavaca  'raca  V.7.32;  —  yat !  bä  paiti  fraiit>m  kärayätt  .  .  yavanamca '  'ranqm(als  Obj.)/a  urvaranqmca  i^arihs.- bairyanqm  ".  .  Getreide  und  Gräser '  lind  Pflanzen  mit  essbaren  Früchten" iV.  J.  4;  g.  53;  —  as.danunqm(sd.)ca ,yavariqm  kasu.dänunqmca  °nanqm  Yt  S. \  39.  2)    'wo  das  Vieh  weidet,  Weide-
23653:•j.'vara^ra-n.  \y^^K':yäi3m..taurva- yata  'tym  dänunamyt.l3.^Z.  2)  'sieg-
28122:•  j.  zsm.fraStih-  Adj.  'von  der  Breite  der Erde,  so  breit  wie  die  Erde':  mi^nm  .  . yj  '%S  aiwyäiti  Yt/0.95;  —  °%S  niaf- ha/am  Yt  10.  44;  —  aisi/  badaza  . . '^aaAa  (APn.)"  dänu.drajar)ha  hvan.- bartzanha  "der  Aiay  Heilmittel . .,  die  so breit  wie  die  Erde,  so  lang  wie  die  Russe, so  hoch  wie  die  Sonne  sind"  Y.  60. 4.
28717:I  hye^  avahyä  kärahyä  mdküt^  ähc^  .  . Aauv(zat)..  Bh.j.  11;  s.nochBh.J.  19,  2.6, i2,_j.6,  9  (Sp.  i730u.).l  ß)  substan- tivisch: käuca  *anayä  »arä  vahu  manö jäginbuitarB  anhat  yS  gSui  uru^wari hqm.pä/räiti  (sd.)  ya'ha  hau  yS  nSit  iia V.^.48;  —  a/  hau  as  . . yS  ml asadayat . . V.5.S1;  J7.a;  —  nSii  hau  *taxm5  yH mit  *aj'a  *taxmd  F.  47;  46,  48,  26;  — pairi%wS  bavaiH  pantä  yim  dänus  päiti *häu^  dit  atvö  apairi%ws  yS  vayaos anamansdikahe  Aog.  77.  3)   auf  den
30617:46-  6;  —  p>nsä  aval  ya'hä  hvd  (zu  2  1  a) yi  hudänul . .  /rada^äi  (sd.)  asfifrvgatJ ^uiavas  (sd.)  , .  yada  h'  aahai  Y.  ?;. b)  adjektivisch,  nur  mit  na  (Sp.
30625:yi  hui  dadat  ..  Y.2(?.  9;  —  p^r^s/t  avat\»  j-  ^^a',  nur  KompA.:  sva.  Au"  (sd.). ya:ia  A'  y}  Audänus. .  asp^matä  Y.ji.  16;       ^^l-  ''"'"'■.  •*='*"°-
```


## [2026-09-05T17:28:39.071Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN date ===\"\ngrep -n \"^date,\" KLN_1966.txt | head\ngrep -n \"daqal\\|diqla\\|dikla\\|deqel\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-05T17:28:39.142Z] TOOL RESULT

```
=== KLN date ===
10373:date,  n.,  fruit  of  the  palm  tree.  —  OF.  date  (F. datte),  fr.  OProven?.  datil  (or  fr.  It.  dattero),  fr.
KLN_1971.txt:64525:of Sem. origin. Cp. Heb. deqel, Aram, diqld, 
KLN_1971.txt:64526:Syr. deqld , Arab, daqal, ‘date palm’, and Heb. 
KLN_1966.txt:10374:L.  dactylus,  fr.  Gk.  SxxxuXo?,  ‘date’,  which  is of  Sem.  origin.  Cp.  Heb.  deqel,  Aram,  diqld, Syr.  deqlA ,  Arab,  ddqal,  ‘date  palm’,  and  Heb. Diqldh,  name  of  a  region  in  Arabia,  rich  in  date palms  (see  Gen. 10:27  and  I  Chron.i:2i).  The form  of  Gk.  SdcxxuXo?,  ‘date’,  was  influenced by  a  folk-etymological  association  with  Saxxu- Xo q,  ‘finger’,  suggested  by  the  fingerlike  shape of  the  date.
```


## [2026-09-05T17:28:53.750Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN leaf for line 10373 ===\"\nawk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"date,  n.,  fruit  of  the  palm\")>0) print \"leaf(1-based)=\"n}' KLN_1966.txt\necho \"=== context ===\"\nsed -n '10360,10385p' KLN_1966.txt"
}
```


## [2026-09-05T17:28:55.426Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD Danube ===\"\ngrep -n \"Danube\" FSD_vol1.txt | head -10\necho \"=== AHD watkins dactyl ===\"\ngrep -n -i \"dactyl\\|dekm\\|date\" AHD_watkins1985.txt | head -10\necho \"=== LKT ===\"\ngrep -n -i \"daqal\\|Dattel\\|dactylus\" LKT.txt | head -10"
}
```


### [2026-09-05T17:28:55.505Z] TOOL RESULT

```
=== KLN leaf for line 10373 ===
leaf(1-based)=223
=== context ===
Darwinism,  n.,  the  theory  of  the  origin  of  species propounded  by  Charles  Robert  Darwin.  —  See prec.  word  and  -ism.
darzee,  n.,  a  tailor.  —  Hind,  darzi,  ‘tailor’.  See Druse.
dash,  tr.  and  intr.  v.  —  ME.  dasshen,  of  Scand. origin.  Cp.  Swed.  daska,  Dan.  daske,  ‘to  beat, strike’,  Swed.,  Dan.  dask,  ‘a  blow’. Derivatives:  dash,  n.,  dash-er,  n.,  dash-ing,  adj., dash-ing-ly,  adv.,  dash-y,  adj.
Dashahara,  n.,  the  ‘ten  days  festival’  (Hindu  reli¬ gion).  —  OI.  ddsahara,  lit.  ‘that  which  takes  away ten  (sins)’,  fr.  ddsa,  ‘ten’,  and  hard,  fem.  of  hara, ‘that  which  takes  away’,  from  the  stem  of  harati, ‘brings,  carries,  takes  away,  robs’.  OI.  ddsa  is cogn.  with  Gk.  8£xa,  L.  decern,  Goth,  taihun, OE.  tien,  ten,  ‘ten’;  see  ten.  OI.  harati  derives fr.  I.-E.  base  *gher-,  ‘to  seize,  take’,  whence  also Gk.  ycip,  ‘hand’;  see  chiro-  and  cp.  the  second element  in  vihara.
dasi,  n.,  a  female  slave;  a  concubine  (Hinduism). —  Hind.,  fr.  OI.  ddsi-,  ‘female  slave’,  which  is rel.  to  dasah,  ‘demon,  enemy,  barbarian,  slave, servant’,  and  prob.  also  to  dasyuh,  ‘demon, enemy  of  the  gods,  barbarian’,  dasyah,  ‘bon¬ dage,  servitude’.  Cp.  the  second  element  in devadasi.
Dasiphora,  n.,  a  genus  of  plants  of  the  family Rosaceae  (bot.)—  ModL.,  irregularly  formed  fr. Gk.  8a wjq,  ‘thick  with  hair,  hairy,  bushy',  and -<p6poi;,  ‘bearing’,  which  is  rel.  to  <p£peiv,  ‘to bear’.  See  dasy-  and  -phore.  The  exact  form  of the  word  should  have  been  Dasyphora.
dastard,  n.,  a  coward,  —  ME.,  prob.  formed with  the  pejorative  suff.  -ard  fr.  c last,  which  is equivalent  to  dased,  pp.  of  dasen,  ‘to  daze’.  See
daze  and  cp.  ON.  dsstr,  ‘out  of  breath, exhausted’.
Derivatives:  dastard-ly,  adj.,  dastard-li-ness,  n. dasy-,  combining  form  meaning  ‘thick,  hairy, rough’.  —  Gk.  Sanu-,  fr.  Sami?,  ‘thick  with  hair, hairy,  bushy,  thick,  dense,  rough’;  which  stands for  *dnsus  and  is  cogn.  with  L.  densus,  ‘crowd¬ ed,  dense’.  See  dense  and  cp.  the  first  element in  Dasiphora.
Dasylirion,  n.,  a  genus  of  plants  of  the  lily  family (bot.)  —  ModL.,  compounded  of  dasy-  and  Gk. Xetpiov,  ‘lily*.  See  lily  and  cp.  words  there referred  to.
dasymeter,  n.,  an  instrument  for  measuring  the density  of  gases.  —  Compounded  of  dasy-  and Gk.  pixpov,  ‘measure’.  See  meter,  ‘poetical rhythm".
Dasypus,  n.,  a  genus  of  armadillos  (zool.)  — ModL.,  fr.  Gk.  Sacju7rou?,  ‘a  hare’,  lit.  ‘the hairy-footed  animal’,  fr.  dasy-  and  rot)?,  gen. no8o?,  ‘foot’.  See  dasy-  and  -pod. Dasystephana,  n.,  a  genus  of  plants  of  the  gentian family  (bot.)  —  ModL.,  compounded  of  dasy- and  Gk.  axccpavoi;,  ‘crown’.  See  Stephanos, dasyure,  n.,  any  of  small  marsupial  mammals  of Australia.  —  Compounded  of  dasy-  and  Gk. oup£,  ‘tail’.  See  uro-,  ‘tail-’, data,  n.  —  PI.  of  datum  (q.v.) date,  n.,  a  given  point  of  time.  —  ME.,  fr.  OF. (=  F.)  date,  fr.  ML.  data  (scil.  littera)  (whence also  It.,  Proven?.,  Sp.  data),  lit.  ‘(letter)  given’, prop.  fem.  pp.  of  L.  dare,  ‘to  give’.  This  term derived  fr.  L.  datum  (neut.  pp.  of  dare),  the  first word  used  in  letters  to  indicate  the  place  and time  of  writing  as  e.g.  datum  Romae  pridie Kalendas  Maids,  ‘given  (i.e.  written)  at  Rome on  the  last  day  of  April’.  L.  dare  is  rel.  to  dos, ‘marriage  portion,  dowry’,  do-num,  ‘gift’,  dond, donare,  ‘to  give  as  a  present’,  fr.  I.-E.  base  *dd-, *d1-,  ‘to  give’,  whence  also  OI.  da-da-ti,  ‘gives’, Avestic  dadaiti,  of  s.m.,  OI.  da-tar-,  da-tar-, ‘giver’,  da-tram,  ‘gift’,  Gk.  8i-Bco-pi,  ‘I  give’, Sd)-T(0p,  Sco-xrjp,  So-xrjp,  ‘giver’,  8£>-pov,  Sto- t(vt),  8<o;,  ‘gift’,  S6-m;,  ‘a  giving;  gift’,  Bo-xo; (verbal  adj.  of  Si-Sto-ptt),  ‘given’,  OSlav.  dati,  ‘to give’,  da-ru,  ‘gift’,  da-ni,  ‘tax’,  da  mi,  ‘I  shall  give’, Lith.  duomi,  ‘I  give’,  OPruss.  dost,  ‘gives’,  Arm. ta-m,  ‘I  give’,  tu-r,  ‘gift’,  Alb.  Sa-sc,  ‘I  gave’. Cp.  add,  addendum,  anecdote,  antedate,  anti¬ dote,  apodosis,  condone,  dado,  dation,  dative, die,  ‘cube’,  donation  and  words  there  referred to,  dose,  dosimeter,  dosology,  dot,  ‘marriage portion’,  dower,  dowry,  edit,  irredenta,  post¬ date,  reddendum,  reddition,  render,  rendition, sacerdotal,  subdititious,  surrender,  tradition, traitor,  treason.  Cp.  also  mandate,  command, commend,  countermand,  demand.  Cp.  also  the second  element  in  vend.
Derivatives:  date,  tr.  and  intr.  v.,  dat-able,  adj., dat-er,  n.,  dat-ing,  n.
date,  n.,  fruit  of  the  palm  tree.  —  OF.  date  (F. datte),  fr.  OProven?.  datil  (or  fr.  It.  dattero),  fr.
L.  dactylus,  fr.  Gk.  SxxxuXo?,  ‘date’,  which  is of  Sem.  origin.  Cp.  Heb.  deqel,  Aram,  diqld, Syr.  deqlA ,  Arab,  ddqal,  ‘date  palm’,  and  Heb. Diqldh,  name  of  a  region  in  Arabia,  rich  in  date palms  (see  Gen. 10:27  and  I  Chron.i:2i).  The form  of  Gk.  SdcxxuXo?,  ‘date’,  was  influenced by  a  folk-etymological  association  with  Saxxu- Xo q,  ‘finger’,  suggested  by  the  fingerlike  shape of  the  date.
dation,  n.,  the  act  of  giving  (law).  —  L.  dal  id, gen.  -dnis,  ‘a  giving’,  fr.  datus,  pp.  of  dare,  ‘to give’.  See  date,  ‘point  of  time’,  and  -ion. Datisca,  n.,  a  genus  of  plants  (bot)  —  ModL.,  of unknown  origin.
dative,  adj.  and  n.  —  L.  dativus  (casus),  loan translation  of  Gk.  Botixy)  (nrCxnc),  ‘the  dative case’;  fr.  dativus,  ‘pertaining  to  the  act  of giving’,  fr.  datus,  pp.  of  dare,  ‘to  give’.  See  date, ‘point  of  time’,  and  -ive.
Derivatives:  dativ-al,  adj.,  dative-ly,  adv. datolite,  n„  a  translucent  calcium  borosilicate (mineral.)  —  Formed  from  the  stem  of  Gk. Saxetc&ai,  ‘to  cut  in  two,  divide,  distribute’, and  X1&04,  ‘stone’.  Gk.  Saxeiahai  prob.  derives fr.  I.-E.  base  *dl-t-,  a  -/-enlargement  of  base *dai-,  *dl-,  *d1-,  ‘to  cut  off,  separate,  divide, distribute’,  whence  OI.  ddti,  dyati,  ‘cuts,  sepa¬ rates,  divides’,  da-yate,  ‘divides’,  Gk.  SodeaOai, ‘to  divide,  distribute;  to  feed  on’,  Salpcov,  "god, goddess’,  lit.  ‘divider,  distributor  (of  men’s destinies)’.  See  demon  and  -lite. datum,  n,,  something  given  or  assumed.  —  L. datum,  neut.  pp.  of  dare,  'to  give’.  See  date, ‘point  of  time’,  and  cp.  data.
Datura,  n,,  a  genus  of  plants  of  the  potato  family (hot.)  —  ModL.,  fr.  Hind,  dhatura,  fr.  OI.  dhat- turah ,  dhusturah,  ‘thorn  apple’,  which  is  cogn. with  the  second  element  in  OE.  dweorge-dwostle, ‘penny  royal’,  and  possibly  also  with  L.  festuca, ‘stalk,  stem,  straw’.  See  festuca. daub,  tr.  and  intr.  v.  —  ME.  dauben,  fr.  OF. (=  F.)  dauber,  ‘to  plaster’,  fr.  L.  dealbdre,  ‘to whiten,  whitewash,  plaster’,  fr.  de-  and  albare, ‘to  whiten’,  fr.  albus,  ‘white’.  See  alb. Derivatives:  daub,  n.,  daub-er,  n.,  daub-ery,  n., daub-ing,  n.,  daubster,  n.,  daub-y,  adj. dauberite,  n.,  basic  uranium  sulfate  (mineral.) Named  after  H.  Dauber,  who  analyzed  it.  For the  ending  see  subst.  suff.  -ite. daubreeite,  daubreite,  n„  a  hydrous  bismuth  oxy¬ chloride  (mineral.)  —  Named  after  the  French mineralogist  Gabriel-Auguste  Daubree  (1814- 96).  For  the  ending  see  subst.  suff.  -ite. daubreelite,  n.,  a  chromium  iron  sulfide  (mineral.) —  Named  after  Daubree.  See  prec.  word  and the  combining  form  -lite.
Daucus,  n.,  a  genus  of  plants,  the  carrot  (bot.)  — L.  daucus,  daucum,  fr.  Gk.  Bauy.oq,  SaOxov,  a kind  of  parsnip',  which  is  rei.  to  Thessalian  Gk. Sauxya,  Gk.  Bacpw],  ‘laurel’.  See  Daphne, daughter,  n.  —  ME  doghter,  dohter,  fr.  OE.  deb¬ tor,  dohter,  rel.  to  OS.  dohtar,  ON.  dottir.
uaunt
debarrass
OFris.,  Du.  dochter,  OHG.,  MHG,  tohter,  G. Tochter,  Goth,  dauhtar,  ‘daughter’,  and  cogn. with  OI.  duhitd,  Avestic  dugeda-,  duydar-,  Toch. A  ckacar,  B  tkacer ,  Arm.  dustr,  Gk.  -&uyaTr,p, OSlav.  duSti,  OPruss.  duckti,  Lith.  dukte, ‘daughter’.
Derivatives :  daughter-hood,  n.,  daughter-ly,  adj., daughter-li-ness,  n.
daunt,  tr.  v.  —  ME.  daunten,  fr.  OF.  danter,  don- ter  (F.  dompter),  fr.  L.  domitdre ,  ‘to  tame,  sub¬ due’,  freq.  of  domare  (pp.  domitus),  ‘to  tame, subdue,  vanquish,  conquer’,  lit.  ‘to  accustom to  the  house’,  fr.  domus,  ‘house’.  See  dome, ‘building’,  and  cp.  indomitable.  Cp.  also  tame. Derivatives:  daunt-er,  n.,  daunt-ing,  adj.,  daunt- ing-ly,  adv.,  daunt-ing-ness,  n.,  dauntless  (q.v.). dauntless,  adj.  —  Formed  fr.  the  ME.  noun  daunt, fr.  daunten  (see  daunt)  with  suff.  -less;  first  used by  Shakespeare.
Derivatives:  dauntless-ly,  adv.,  daunt!ess-ness,n. dauphin,  n.,  the  title  of  the  eldest  son  of  the  king of  France.  —  F.,  lit.  ‘dolphin’,  translation  of L.  Delphinus,  lit.  ‘dolphin’,  orig.  a  name  borne by  Guigo  IV,  count  of  Vienne  (died  in  1142) and  by  his  successors.  The  name  Delphinus  was chosen  in  allusion  to  the  three  dolphins  repre¬ sented  in  the  coat  of  arms  of  the  lords  above mentioned.  Hence  the  province  owned  by  them came  to  be  known  as  Delphinatus  in  Latin (whence  F.  Dauphine).  See  dolphin, dauphine,  n.,  a  dauphiness.  —  F.  dauphine,  fern, of  dauphin.  See  dauphin.
```


### [2026-09-05T17:28:55.571Z] TOOL RESULT

```
=== FSD Danube ===
7276:rld’l-a,  n.  pi.  A   group  of  Protozoa,  Important  because  para-  A’da  Ka-leh’,  1   a’da  ka-le';  2   a'da  ka-16'.  An  Island  In  the sltlc  In  the  cells  of  the  higher  vertebrates,  chiefly  infesting  Danube  river,  situated  W   m.  below  Orsova,  and  above  the
34317:—   balk'sday",  n.  [Local,  Eng.]  A   day  lost  In  demurrage while  handling  a   ship's  cargo.—  b.dlne,  n.  1.  Id  billiards, a   line  partitioning  off  a   space  in  the  corner,  along  the  sides, or  around  the  entire  edge  of  the  table.  Connected  with this  Is  the  b. dining,  used  in  carom  billiards,  consisting  of eight  short  lines,  two  in  each  corner,  intersecting  the  balk- line and  dividing  the  table  Into  nine  panels  all  of  which, save  the  center  one,  are  known  as  balks,  shot?  In  which  are subject  to  certain  limitations.  2.  In  athletics,  a   line  prog- ress beyond  which  counts  as  a   trial.—  b.spockct,  n.  One  of the  two  corner  pockets,  in  English  use  at  the  foot,  in  America, at  the  head  of  the  billiard-table.—  b.*stafT,  n.  A   quarter- staff.—  to  double  la  b.  (.Billiards),  to  pocket  by  first  driv- ing the  spot-ball  to  a   cushion,  both  this  ball  and  the  cue-ball being  within  the  balk-lino.—  balk'ishf,  a.  Rough;  uneven. Bal-kan'*  1   bal-kan'  or  bol'kan;  2   bal-kan'  or  bal'kan,  a. Pertaining  to  the  peninsula  south  of  the  Danube  river between  the  Adriatic  and  the  Aegean  and  Black  seas, about  188,000  sq.  m.;  it  contains  Bulgaria,  Jugoslavia, Albania,  Constantinople,  Dobrudj a,  and  Greece.
52356:Bul-ga  'ri-an,  1   bul-ge'n-en;  2   bul-ga'ri-an,  a.  Of  or pertaining  to  (1)  the  Bulgars,  or  (2)  Bulgaria,  south  of the  Danube  and  west  of  the  Black  Sea.  BuI-gar'Ic*.
58048:In  ancient  Rome:  sometimes  used  as  a   word  of  reproach  or  bank  of  the  Danube;  headquarters  of  Valentinlan;  destroyed
83708:Csal-Uls'ten,  1   tfhal-kls'ten .   2   chl-kls'tCn,  n.  A   district  In Hungary  between  the  Danube  and  the  Thelss;  340  sq.  m. Csa-nad',  1   tfho-nod';  2   chq-nad',  n.  A   county  in  E.  Hun- gary; 699  sq.  m.;  capital,  Csanad.
85782:or  Getae,  a   Thracian  people  living  between  the  lower Danube  and  the  Karpathian  mountains:  in  blood  and speech  probably  Aryan.  II.  n.  A   native  or  inhab- itant of  Dacia.
86476:d an 'gle •monkey,  l   dangl»mun  j;  2d&o'CI*m6n  y,n.  Early  Danube*,  1   dan'ytlb;  2   dkn'yub  (G.  Do'nau,  1   dO'nau;  2 Chinese  bronze  coins,  often  used  ft s   danglers  on  musical  In-  d6,n  “   tf  {A^  u'tir.l  A   river  of  Europe,  flowing stru  m   en  ts,  hen  ceth  o   n   am  o.  2,000  m.  from  Baden,  through  Germany,  Austria,  Hungary,
86479:the  uppermost  group  of  strata  comprised  in  the  Upper  Crc-  Dt0oi-  bordering  ^n^tbe  river  Danube -the  Danublan
89575:All  great  rivers,  as  the  Nile,  the  Mississippi,  the  Ganges,  tho Danube,  have  their  deltas;  but  the  largest  river  in  the  world,  tho Amazon,  is  an  exception  to  this  rule.
=== AHD watkins dactyl ===
43:In my article “The Indo-European Origin of English” in the first edition of The American Heritage Dictionary of the English Language, I wrote that “a reconstructed grammar and dictionary cannot claim any sort of completeness, to be sure, and the reconstruction may be changed because of new data or better analysis.” The present revised edition of The American Heritage Dictionary of Indo-European Roots stands as eloquent testimony to the accuracy of that statement. Indo-European studies have not stood still between the 1960’s and the 1980’s, and both advances in theory and an increase in the database have made a thoroughgoing revision not merely possible but necessary. Many new roots have been added. In part, this is in order to include and extend the etymologies of words new to The American Heritage Dictionary: Second College Edition; in part, it is to provide a superior account of the histories of previously existing words. Advances in printing technology have now made it both feasible and economical to present in a work for the general public the sounds and forms of Proto-Indo-European in a manner consistent with current usage in the field. Few entries in the dictionary have escaped revision. Old etymologies have been revised and brought into line with current thinking, and new etymologies have been proposed where it seemed proper to do so. The introductory essay has also been revised and brought up to date.
115:these, where a word is attested in several traditions, it is still customary to call it Indo- European, even though it may not date from the remotest reconstructible time. It is in this sense, universally accepted by scholars, that the term Indo-European has been used in this Dictionary.
127:complete agreement on the numerals from two to ten: dwo- (*duw6), trei- (*treyes), kvetwer- (*k”etwores), penk”e, s(w)eks, septm, oktd(u), newn, dekm. For the nu- meral “one” the dialects vary. We have a root sem-' in some derivatives, while the western Indo-European languages Germanic, Celtic, and Latin share the form oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
139:The names for a number of different trees are widely enough attested to be viewed as Proto-Indo-European in date. The general term for tree and wood was deru. The origi- nal meaning of the root was doubtless “to be
173:It was probably not long before the disper- sal of the Proto-Indo-European community that the use of the wheel and wheeled trans- port was adopted. Despite the existence of widespread word families, most terms relat- ing to wheeled vehicles seem to be metaphors formed from already existing words; they are not primitives or primary vocables. So the word for AXLE (aks-) may mean simply “a pivotlike juncture”; the NAVE or hub of the wheel (nobh-) is the same word as NAVEL. This is clearly the case with WHEEL itself, where the widespread *k(e)-k“l-o- is an ex- pressive derivative of a verb (k"el-') meaning “to revolve or go around.” Other words for “wheel” are dialectal and again derivative, like Latin rota from a verbal root ret-, “to run.” A root wegh-, “to go, transport in a vehicle” (WAGON), is attested quite early, though not in Hittite. This evidence for the late appearance of the wheel agrees with archaeological findings that date the distri- bution of the wheel in Europe to the latter
175:part of the fifth millennium B.c., the latest possible date for the community of Proto- Indo-European proper.
188:A number of metaphorical expressions ap- pear to be creations of ancient, even Indo- European date. Thus the verb dheg"h-, “to burn, warm,” forms derivatives in Latin and Celtic which mean “to keep warm, cherish,” and refer especially to the duties of the pious son toward his aged parent. Latin terra, “earth” (TERRAN), is historically a trans- ferred epithet, “dry (land),” from ters-, “to dry.”’ One securely reconstructible Indo- European place name rests squarely on a metaphor: *Piwer-id in Greek Pieria (PIE- RIAN SPRING) and [wer-ion-, the prehistoric Celtic name for Ireland (Gaelic Eire, Erin), both continue an Indo-European feminine adjective *piwer-ia, “fat,’’ metaphorically “fertile,” from peie-, the same root which gives English FAT.
194:Archaeologists have not in fact succeeded in locating the Indo-Europeans. An artifact other than a written record is silent on the language of its user, and prehistoric Eurasia offers an abundant choice of culture areas. Archaeologists are generally agreed that the so-called Kurgan peoples, named after the Russian word for their characteristic “bar- row” or “tumulus” grave structure, spoke an Indo-European language. Some time around the middle of the fifth millennium B.c., these people expanded from the steppe zone north of the Black Sea and beyond the Volga into the Balkans and adjacent areas. These Kur- gan peoples bore a new mobile and aggressive culture into Neolithic Europe, and it is not unreasonable to associate them with the coming of the Indo-Europeans. But the Kur- gan peoples’ movement into Europe took place in distinct waves from the fifth to the third millennium B.c. The earliest so far discovered might be compatible with a rea- sonable date for Proto-Indo-European, that is, a date sufficiently long ago for a single language to develop into forms as divergent as Mycenean Greek and Hittite as they are historically attested by the middle of the second millennium B.c. But the later Kurgan immigrations after 4,000 B.c. are too late to be regarded as incursions of speakers of un- differentiated Proto-Indo-European. The archaeological evidence for the later waves of Kurgan migrations points to their having had an Indo-European culture, but the lan- guages spoken by the later Kurgan peoples must have been already differentiated Indo- European dialects, some of which would doubtless evolve into some of the historical branches of the family tree. We must be content to recognize the Kurgan peoples as speakers of certain Indo-European languages and as sharing a common Indo-European cultural patrimony. The ultimate “cradle” of the Indo-Europeans may well never be known, and language remains the best and fullest evidence for prehistoric Indo- European society.
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old English réden, condition: HATRED, KINDRED; b. Germanic *rédaz in (i) Old High German rat (> German Rat), counsel: BUNDESRAT, RATHSKELLER (ii) Old English rédels(e), opinion, riddle: RIDDLE?. 3. Zero-grade form *ra- in Germanic *radam, number (see dekm). IV. Variant (or separate root) *ri-. 1. Suffixed form *ri-tu- in Latin ritus, rite, custom, usage: RITE. 2. Suffixed form *(a)ri-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM. [Pok. 1. ar- 55.]
342:flagitdre, to demand importunately: FLacitious. [Pok. bhlag- 154.] bhlagh-men-. Form, ritual form. Sanskrit brahmd, brah- man-, priest, and brahma, bréhman-, prayer: BRAHMA!, BRAHMAN, (BRAHMIN). [Pok. bhlagh-men- 154.] bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man bracc(h)o, dog that hunts game by scent: BRACH. 2. Suffixed form *bhrag-ro- in Latin fragrdre, to smell: FLAIR, FRAGRANT. [Pok. bhrag- 163.] bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. Germanic *brekan in: a. Old English brecan, to break: BREAK; b. Old English bréc, a break- ing: BREACH; c. Old High German brehhan, to break, akin to the Germanic source of Italian breccia, breccia: BRECCIA; d. Old French breier, to break: BRAY?; e. Old French brier (dialectal) and broyer, to knead: BRIOCHE. 2. Germanic *brak-, bushes (< “that which impedes motion”), in Old Norse *brakni, undergrowth, akin to the probable Scandinavian source of Middle English brake(n), bracken: BRACKEN, BRAKE’, BRAKE‘, 3. Nasal- ized zero-grade form *bhr-n-g- in Latin frangere, to break: (FRACTED), FRACTION, (FRACTIOUS), FRACTURE, FRAGILE, FRAGMENT, FRAIL!, FRANGIBLE; ANFRACTU- OUS, CHAMFER, DIFFRACTION, (INFRACT), INFRANGIBLE, INFRINGE, OSSIFRAGE, REFRACT, (REFRAIN?), (REFRIN- GENT), SAXIFRAGE, SEPTIFRAGAL. 4, Latin suffrdgdri, to vote for (? < “to use a broken piece of tile as a ballot”), hence suffrdgium, the right to vote: SUFFRAGAN, SUF- FRAGE. [Pok. 1. bhreg- 165.] bhréi-. Also bhri-. To cut, break. 1. Possibly Latin fricdre (> French frotier), to rub: FRAY?, FRICATIVE, FRICTION, FROTTAGE; AFFRICATE, DENTIFRICE. 2. Possi-
=== LKT ===
431:'Schweiß',  ^arak  at-lamr  'Schweiß  der Datteln',  d.  h.  Datlelsaft,  ein  berauschen- des Getränk.  In  Ostindien  heißt  'arak ein  starkes  Getränk,  das  aus  gegorenem Reis,  Zucker  und  Kokosnüssen  zube- reitet wird.  Nach  Europa  ist  das  Wort gekommen,  nachdem  im  mal.  Archipel Kolonien  errichtet  waren.  Daher  haben Italiener  und  Spanier,  die  dort  keine besaßen,  das  Wort  auf  anderem  Wege erhalten.  Sp.  arac,  altsp.  arrequi(n), frz.  arakj  rack,  pg.  araquc,  araca,  rak, engl,  arrack,  rack,  ndl.  arak,  dtsch. Arrak.  Aus  dem  ar.  Adjektiv  'araki wohl  das  frz.  Argot  woit  riquiqui 'Schnaps'.  Die  tk.  Form  ist  ebenso  raki, woraus  rum.  rachiü  'Branntwein',  rachier 'Branntweinbrenner',  racliierie  'Brenne- rei'. Russ.  arak.  [Kluge  22.  Hobson- Jobson  36/37.  DE  196/197.  Devic  DEt 33/34.  Gorjajew  5.  —  J.  de  Sousa,  Vesli- gios  da  lingua  arabiga  em  Portugal.  Col- lecijäo  etimologica  das  palavras  e  nomes portugueses  que  tem  origen  arabiga.  Lis-
697:'Finger',  Einheisnomen  banäna;  wahr- scheinlich Grundwort  zu  der  Bezeich- nung Banane  für  die  Frucht  der  Musa paradisiaca  L.  oder  Musa  sapientum  L. [Musa  übrigens  aus  ar.  mauz,  müz  'Baum, und  Frucht  der  Musa'],  doch  wurde  der Name  zuerst  im  Kongogebiete  gehört [obwohl  der  Bantu-Name  dafür  bi-tebbe oder  ähnhch  lautet]  und  um  die  Mitte des  16.  Jahrhunderts  nach  Europa  ge- bracht; sp.  pg.  banana,  it.  banano,  rum. bananä,  frz.  banane  'Pisangfrucht',  ba- nanier  'Pisangbaum',  ndl.  banaan,  engl. banana,  dtsch.  Banane,  russ.  banan.  — Nach  einem  Vorschlage  von  HÜMMEL, soll  Banane  von  babyl.  banu  'süß  schmek- ken,  gut  sein'  [wohl  banu  II,  1)  bei  Del HWB  180  a]  kommen,  wovon  auch  über *bana  das  ar.  bala  'Dattel'  abgeleitet wird.  [Kluge  35.  Hobson-Jobson  56. E.  Werth,  Zur  Natur-  u.  Kulturgeschichte der  Bananen.  In  Festschrift  zu  Eduard Hahns  60.  Geburtstage.  Stuttgart  1917.. S.  22—58.   MWiD  130.
1219:'Schlechte  Dattelsorte'  [syr.  deklä,  aram. dikla  BrLexSyr  164  a],  hieraus  mit  volks- etymologischer Umgestaltun.üT  gr.  bcxK- TuXoc;;  hieraus  wohl  über  mlat.  dactylus die  romanischen  Formen  it.  dattero, sp.  dätü,  frz.  datte  [aber  rum.  curmalä, s.  hier  Nr.885 ;  pg.  tamara,  s.  hier  Nr.201 3], ferner  in  den  germanischen  Sprachen engl,  date  [aus  afrz.  date],  ndl.  schvved. dadel,  dän.  daddel,  dtsch.  Dattel  und im  Slavischen  poln.  dal-tyl  (u.  drzeivo daktylowe),  Cech.  daktyl,  datle  (u.  datlov- nik,  daktylovnik)  [aber  russ.  usw.  finik].
2131:'Dattel',  ebenso  tk.  hurma  [Kelekian Kämüs  537  a];  hieraus  rum.  curmal 'dass.',  curmalä  'Dattelpalme' ;  bulg. hurma,  furnia,  serb.  hurma,  urma  'Dattel', russ.  kurma  'dass.,  Dattelpalme'.  [Bern SlEtWb  406.
4297:'Ein  Affe  Hylobates  syndactylus  Wagn.' [Pijii  147];  hieraus  trz.  engl,  siamang, dlsch.  Siamang  'derselbe  Langarmaffe'. [Devic  DEt  207.   JAOS  XVIII,  101/102.
4532:'Dattel',  Einheitsnomen  tamra\  hieraus sp.  pg.  tamara  'Dattel'  und  Ableitungen. —  Aus  tamr  hindl  'ind.  Dattel,  Tama- riscus  indica'  entstand  it.  tamarmdo, frz.  tamarin,  sp.  tamarindo,  pg.  tama- rinho,  rum.  tamarinda;  ndl.  tamarmde, engl,  tamarind,  dtsch.  Tamarinde.  Eine lat.  Ableitung  aus  tamr  ist  lat.  tamaris- CHS,  woraus  z.  B.  engl,  tamarisk,  dtsch. Tamariske;  kat.  tamarit,  sard.  tamaritfu. [DE  347.  EguÜHZ  502.  Devic  DEt  214 u.  215.  ML  85.53.  Herrigs  Archiv  CXL. 240.
5009:Hylobates  syndactylus 1898
7428:dactylus  465 damascenus  476 datura  512 rfoimm  2222 doronicum  486
```


## [2026-09-05T17:29:16.348Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 179 213 223; do echo \"=== leaf(1-based) $L first 200 chars ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -c 300; echo; done\necho \"=== any explicit page numbers? ===\"\ngrep -n \"^[0-9]\\{3\\}$\" KLN_1966.txt | head -5"
}
```


### [2026-09-05T17:29:17.920Z] TOOL RESULT

```
=== leaf(1-based) 179 first 200 chars ===
 coeno-).  Cp.  1st  con-,  contra-, count,  ‘title  of  nobility’.  Cp.  also  y-. coma,  n.,  a  state  of  insensibility.  —  ModL.,  fr. Gk.  xolpta,  ‘a  deep  sleep,  lethargy’,  which  is  prob. rel.  to xotpxv,  ‘to  put  to  sleep’,  xeiaOou,  ‘to  lie',  fr. I.-E,  base  ke
=== leaf(1-based) 213 first 200 chars ===
,  a  dupe.  —  Perhaps  abbreviation  of cullion.
culm,  n.,  stalk,  stem.  —  L.  culmus,  ‘stalk,  stem’, cogn.  with  Gk.  xxaxuo?,  xx'Axirr,,  ‘reed’,  OSlav. slama,  Russ,  soldma,  ‘straw’,  OPruss.  salme, Lett,  salms,  ‘blade  of  straw’.  Cp.  calamary, Calumet,  cha
=== leaf(1-based) 223 first 200 chars ===
n,  of s.m.  See  tetter  and  cp.  dartre.  Cp.  also  darn.
darter,  n.,  1)  one  who,  or  that  which,  darts;  2)  the name  of  various  fishes.  —  Formed  from  the  verb dart  (see  dart,  n.)  with  agential  suff.  -er.
dartle,  intr.  v.  —  Formed  from  the  verb  dart  (see dart,
=== any explicit page numbers? ===
3331:100
3332:101
3371:102
3385:103
3422:104
```


## [2026-09-05T17:29:17.941Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 1219 context ===\"\nsed -n '1210,1225p' LKT.txt\necho \"=== AFM daqal ===\"\ngrep -n \"دقل\" AFM_pages.txt TAD_pages.txt ARB_mo3rb.txt 2>/dev/null | head -10\necho \"=== MON daqal ===\"\ngrep -n \"دقل\" MON_part1.txt | head -10"
}
```


### [2026-09-05T17:29:18.030Z] TOOL RESULT

```
=== LKT 1219 context ===
461.  Ar.  dai'a:
'Grundstück,  Weiler,  kleines  DorP;  hier- aus mit  ar.  Art.  ohne  Assimilation  kat. sp.  pg.  aldea,  pg.  aldeia  'Dorf,  Weiler'; frz.  akUe  'Flecken  oder  Dorf  in  den Besitzungen  in  Afrika  und  Indien'. [DE  97.  Eguilaz  Uis.  Devic  DEt  15. Lammens  Rem  9/10.    ML  2460.
462.  Pers.  däjä:
'Amme'  [Horn  NpEt  S.  119,  Nr.  539], auch  tk.  daje-^  hieraus  rum.  claicä,  doicä 'dass.'.
463.  Ar.  da'if :
'Schwach',  tk.  za^i.f;  hieraus  rum.  zaif 'unwohl,  schwach',  zuiflic  'Schwäche'. [Löbel  EITAP  100.
464.  Ar.  dä'ira :
'Kreis'  [vom  Vb.  dära  'rund  herum- gehen, umkreisen'],  tk.  da^ire;  hieraus rum.  daerea  'Trommel',  dairca  'Schellen- trommel'.
465.  Ar.  dakal:
'Schlechte  Dattelsorte'  [syr.  deklä,  aram. dikla  BrLexSyr  164  a],  hieraus  mit  volks- etymologischer Umgestaltun.üT  gr.  bcxK- TuXoc;;  hieraus  wohl  über  mlat.  dactylus die  romanischen  Formen  it.  dattero, sp.  dätü,  frz.  datte  [aber  rum.  curmalä, s.  hier  Nr.885 ;  pg.  tamara,  s.  hier  Nr.201 3], ferner  in  den  germanischen  Sprachen engl,  date  [aus  afrz.  date],  ndl.  schvved. dadel,  dän.  daddel,  dtsch.  Dattel  und im  Slavischen  poln.  dal-tyl  (u.  drzeivo daktylowe),  Cech.  daktyl,  datle  (u.  datlov- nik,  daktylovnik)  [aber  russ.  usw.  finik].
466.  Ar.  dakika:
[Vom  Vb.  dakka  'kleinschlagen']  'Augen- blick, Minute',  auch  tk. ;  hieraus  rum. dicä  'Augenbhck',  adica  'nämlich,  eigent- lich'.
467.  Tk.  dal:
'Weide'  [vom  Stamme  tal  'hin-  und herbewegen'  Vambery  TktEtWb  S.  142, Nr.  152  11];  hieraus  russ.  tal'  'dass., Salix  arenaria'.    [Gorjajew  360.
468.  Hebr,  (ial:
'Schlapp,  schwach';  im  neueren  Sprach- gebrauch 'leer,  arm'  [Ave-L.  IV,  353]; dazu  das  Abstraktum  dallü^  'Armut', hieraus  judendtsch.  Dalles  'Armut;  Tage, an  denen  man  kein  Geld  hat',  vgl.  das Sprichwort:  Dalles  macht  paslus  'Armut führt  zu  unrechten  Handlungen'.  —  Im jidd.  mit  Übergang  vom  Abstrakten  zum Konkreten:  dallos  'Armer'.  [Hirnbaum HebrEl  54.
=== AFM daqal ===
ARB_mo3rb.txt:20069:أندد يل اليد دقل لم فليميرونا حاجمهم ساعة ! فقَال له : إن جماجمهم ليست بقحَار نتعار » 
ARB_mo3rb.txt:28633:دقل 
AFM_pages.txt:1882:عد (الرَأند) شجر طَيَب الرانحة من سجر البادية دقل هو الا ܝܨ¿ ܪܝܐ[ الفار وقد
=== MON daqal ===
62153:دقل: ادرهه [ع.] 0( (گیا.) خرمای ند و
```


## [2026-09-05T17:29:26.384Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<10380 && /^[0-9]{2,4}$/ {ln=NR; v=$0} END{}' KLN_1966.txt\ngrep -n \"^[0-9]\\{2,4\\}$\" KLN_1966.txt | awk -F: '$1>10250 && $1<10500' | head -20"
}
```


## [2026-09-05T17:29:27.287Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '62150,62156p' MON_part1.txt\necho \"=== ARB ===\"\nsed -n '28625,28645p' ARB_mo3rb.txt"
}
```


### [2026-09-05T17:29:28.766Z] TOOL RESULT

```
10312:400
10326:401
10343:402
10344:403
10389:404
10404:405
10435:406
10436:407
```


### [2026-09-05T17:29:28.821Z] TOOL RESULT

```
بساریکد‌بینی. دقت نسظر: باریکداینی» 
خر ده‌سنی. 

دقل: ادرهه [ع.] 0( (گیا.) خرمای ند و 
پست. خرما. 

دقمصه: (6-)02(۵5۵ [محر. ع. . مجمصه ] 
=== ARB ===








دقل 


فيلور ؟45؟:١‏ 


قاوس 6١1:غ‏ 4 لا08:”ة 
قآر #14:م 

فارورة م9" :؟؟ 

١:85 تأزرزة‎
```


## [2026-09-05T17:29:43.397Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT around 13405 ===\"\nsed -n '13395,13415p' BRT.txt\necho \"=== leaf number for that line ===\"\nawk 'NR<=13405' BRT.txt | grep -c $'\\f'"
}
```


### [2026-09-05T17:29:45.298Z] TOOL RESULT

```
=== BRT around 13405 ===
•  j.  ^dänav-  £  ' (Getreide) koro'.
KompE.  —  zEl.  s.  unter  dänd^karS-.
•  j,  dänazväza-  m.  andrer  Name  für  den abpr»t-{sA.y.  . .  paoiryd ..  kSvarttlit3m{&Ai)  ., astayeiti  .  .  tüirlm  'stm  N.  82.
Wahrscheinlich  verderbtes  Wort;  T  hitVJjuiB.
—  Pü.!  pa röi viÜnilSrih'}  "für das  Amt  dessen, der  den  Fluss  (aus  dem  das  Wasser  geholt werden  soll)  aassucht";  erl.;  pa  äiariiA.  — >l  Nach  DsT.  ZA.  3.  133,   Blocket  Lex,  88
mehr  .
ules
•  j.  (0n5.kars-Adj.'(Getreide)kömer(ver)- schleppend',  Bezeichnung  einer  Ameisen- art*': maoirJm  °spm  Y.iö.ia; — maoirinam ■!„nqm  V.J4.S.  'i«  73-
*)  Die  Zoologen  des  Awesta  haben  offenbar die  Puppen,  die  die  Ameisen  in  die  Sonne  tragen, für  geraubte  Getreidekürner  angesehen.
Komp.:  'däiiä'f.  'Getreldekom';  ai.  ./4ono- f., mp.  a'iin,  np.fl'JHo;  H-Vari-Adj.  (aus  ir. '.iz-i-, IF.  5.  261),  zum  \.'tatl-;  mp.,  np.  'iü;  vgl. yäri.iarJi:  —  mp.  (Pü.)  däa  kii,  np.  dinaiis.
•  j.  dänu.drä]ah-  Adj.  'von  der  Länge
eines  Flusses,  so  lang  wie  die  Flüsse': aisis  bassaza  . .  sim.fi-a^anha  (sd.)  'ja»ha (APn.)'>  kvar3.bamai9ha  Y.  60. 4.
Pü.:  rol  draknäk.  —   ')  Tbem.
•  j.,  g.  'däman-,  d^man-''  n."  i)  im gAw.  'Stätte,  Wohnstatte'  in  eschato- logischcm  Sinn,  Plur.:  ai  hsi  'mqm  (NP.) ^■uiaAmT  a  dam  (Sp.  684  o.)  ahurä  Y. 4(9.  7  j  —  drüjh  kvS  -man  (AP.)  *haB>!ahy<'t gät  (sd.)  ".  .  zu  den  Wohnstätten  derer, die3>  .  ."  ^.46.(>.  2)  im  jAw.  'Ge- schöpf, geschatfenes  Wesen';  Sing,  und Du.  auch  kollektiv  von  der  Gesammtheit des  Geschaffenen,  'Schöpfung';  pauaSa  . . yat    mainyü    'man  (AP.)    dakU?m  yasta
dby  Google
73S
—  Mämay-  736
sppnie  mainyui  yasca  a»rd  ¥.57.17;  Yt.  xfaisa  Atn-anam  'mtrttamY.S  s;¥iVi.4.3; jy.  76,  /5.  3;  —  ■!'.»  °ma  (als  AD.)  .  .  —  avU  'man  asai-anö  yazamaide  yä  hmti jasca  dairal  sppntd  mainyui  yasca  daial  paoirySjiäta  paoiryS.fraiwarsta  amäatca .. at^rS  mainyu/ \t  t^.  43;  —  zara^uitra  Vr.7.4;  —  pauna  data  °man  aIaonls\. . ,  yS  . .  i'friirrojastfinö  abavat  mainiva  16.3;  \1.11.2,  VyL^j;  —  asa.paoiryjis^a •man  (GS.)  ¥.5.15;  \.ig.\z-,  —  fra-  'mSbls\.ig.\^\  Vr,;<?.2;  —  manas.paoir- rasayö  . .  h^titi  ySsktnsbmä  uvayä  *maini-  y(üibyB  °mabyS  Y.  Z^.  12;  Vi.  ig.  i ;  —  ^a/ vä  'man  VLy-76;  —  ^lyS  >wdr?!tira\'ma  (AS.)  asava  yaozdäir m  YL^.a;  — ya  vispa  'iwjrpsatS  'man  (AP.)  \. ^■j.2;\yaozdätimm  ankam  'manqm  vahisiqm  \'i. Yt./9.94;  —  aam  vTsfianqm  'manqm'  10.^2;  —  tisirlm  . ,  yS  ..  nafmiaiii  (sd.) nipäta  ahmt  Yt/O.54;  54;  — fravasaysX . .  vTspSst  13  'man  baZsasyatica  YtÄ43; vUpä  *'mqm  (AP.)  savavuhaitis  (sA)  V.  |  —  kihrpa  avavats  *sraya  (sd.)  ya'ia  'man '9-ZTi  —  tsm  ..yazat»m  ..'mdhu  iftistfm'.  sraäläis  H.  2.  9;  YLJO.141;  — '  anra mnr>m  yatäiSx.lo.6; — y5i  "i^wä  vamm  '  mainyS  janäni   'ma  dalvsJlUm  .  .  paili
'mshu  ahüm  ratUmca  gaghanqm  Yt.  jo. 9«;  — yat  dim  'mabyS  Bnasti  masda  Ha t?m  yaf  ahmäi  'man  Y.  19.  i4(?)*';  la";
—  uslra  kvartxiaBa  . ,  raexlmm  iuryna- vähi  'mahva  V.  27.  5;  - —  vayaol ,  .  tara- '^t5  (Stverz.)  anyäii  'man  Y.  22.  24;  usw.;
—  nrmasf  lg  ahura  . .  "i^rlscii  pars  anyäis  ■ 'man  Ny.  J.  i ;  —  ahur?m  mazdqm  main- yaom  mainyavanqm  'manqm.. zara'iusfr?m\ spitamtm  gai%tm  gaii^yanam  'manqm  .  .  j ahümla  ratamcaVt.2.4;  Vd.2o;  —  ahurahe' mazdä ya'ha  'man  da'hatYt.ip.io;  —  vlspe\ te aAur3iiX3.V.YoV^..vanuATs  'man  asdonis .  .  y3il  dadaha  Y.  ji.  10;  Vr.  72.  4;  — . sraos^m  .  .  yS  .  .  nipaitt  mazda  'man  Y. , 57.16;  16,  31;  —  paoirys  mazd\ (GS.)  Y.57.  2;  —  ya'ia  aam  ammxtlm ava.barani  avi  mazda  'mabyB  Uta  aam apa.barani  uva  fu'itmca  tarsmmca  hala mazda  'mabyö  Yt9.9r.;  gf.^;  —  iir?hqm 'manqm  yai  ahurahe  mazda  Yt  7(),  1 8 ;  — ahuTTm  mazdqm  .  .  äätärfm  vahinqm 'manqm  Y.  16.  \\  —  vTspais  . .  yäii  sp?n- tahe  mainySu!  'man  Yt.Ä48;  lo.  142,  V. 5- 33t  'J-^S,  VyL5/;  —  vTspanqmca  ippn- tahe  mainySui  'manqm  aiaonqm  asaoni- nqmca^^  asahe  ra'^wqm\.i.\6;  —  avasö.- xid^rS  hyat  drvä  ..  nizbprttö  haia  spgntahe mainyius   'mabyS  Y,  Ä  6;   27.  2,  Vr.  72.  4;
=== leaf number for that line ===
420
```


## [2026-09-05T17:29:46.494Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN navdan ===\"\ngrep -n -i \"nävdän\\|näudän\\|navdan\\|naudan\\|Dachrinne\\|Traufe\" HRN.txt HUB.txt | head -10\necho \"=== BQT navdan ===\"\ngrep -n \"ناودان\" BQT_v2_pages.txt BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -10\necho \"=== MON navdan ===\"\ngrep -n \"ناودان\" MON_part2.txt MON_part1.txt | head -5\necho \"=== ARY nav ===\"\ngrep -n \"ناودان\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-05T17:29:46.602Z] TOOL RESULT

```
=== HRN navdan ===
HUB.txt:1431:eingiessen, traufein*, parisindati *umgiessen', visincati
HRN.txt:8886:1024. näv Wasserkanal; Schiffchen', nävdän.
=== BQT navdan ===
incoming/BQT/BQT_v3_pages.txt:5979:پمعنی ناودان باشد - و سوراخی را نیز گویند که
incoming/BQT/BQT_v3_pages.txt:7689:خری که آبخورش زبر ناودان‌صیر
incoming/BQT/BQT_v3_pages.txt:22375:آدمی‌زاد است ۴ را گویند؟ - وناودانی‌رانیز گفته‌الد کهب ر کنارهای
incoming/BQT/BQT_v3_pages.txt:40429:وناودانی هم دارد ماتند جرغتو وبلبله و مشك
BQT_v1_pages.txt:6037:کفتماند - ویمعنی ناودان هم(۱) » آمده است .
BQT_v2_pages.txt:17666:‫عمش کنن را منخص سازند ‪ -‬ویمعئی درشادی‌غم‬                  ‫‪ ۰‬و عصی یخی را گوند که درزیر‌ناودان‬           ‫گوند‬
BQT_v2_pages.txt:20553:‫ناودان و امثال آن باشد ؛ وبفتح ثالث نیزآعده‬                ‫وشیرازبان لندیدن‌بضملاممیگویند وخراسالیان‌لیز‪.‬‬
BQT_v2_pages.txt:37612:                         ‫ناودان کوچك ‪.‬‬                  ‫بتقدیم قاف برلام هم بنظر آمده اسستقکلهیس‬
incoming/BQT/BQT_v4_pages.txt:5251:ونگین هم‌آمده است . مورد آب وغیره۴ - و بمعنی‌ناودان هم بنظرآمده‌است
incoming/BQT/BQT_v4_pages.txt:7711:و تحتانی » بمعتی نانغواء است که زئیان باشد . | کوچك - وناودان ‎٩‏ بام خانه - و آنچه کندم
=== MON navdan ===
MON_part2.txt:10015:مخارجه عمارت. ناودانی که بر کنارهای بام 
MON_part2.txt:11521:است که با نیم‌شیار قحف طرف دیگر ناودان 
MON_part2.txt:53114:ناودانی است که آن جمع 
MON_part2.txt:67846:آب. ناودان. 
MON_part2.txt:70161:1( آب راهه» آب گذر. ناودان؛ ج. با فا 
=== ARY nav ===
```


## [2026-09-05T17:30:01.390Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 1024 ===\"\nsed -n '8880,8900p' HRN.txt\necho \"=== HRN leaf ===\"\nawk 'NR<=8886' HRN.txt | grep -c $'\\f'"
}
```


### [2026-09-05T17:30:03.190Z] TOOL RESULT

```
=== HRN 1024 ===
arm. nkan iyygvcplac *unter der Asche gebackenes
Brot'; vergl. chorasm. pekend (Vullers); hei. nagan,
n. nayan *Brot', nagan[pad *Bäcker* (249) ; minj. nayan;
phlv.-päz. nän (PPGl.).
Also zu l/^kan- + ^h ursprünglich '(unter die heisse
Asche) Vergrabenes* (zuerst de Lagarde)?
1024. näv Wasserkanal; Schiffchen', nävdän.
ap. näviyä' 'Flottille'; aw. navOza^ 'Schiffer* (Bar-
tholomae, ZDMG. 46, 294 Anm. 3), vergl. nävaya-
'fliessend'; phlv. nävfäk (aw. nävaya-), nävTcak (Bund.);
ai. näV' 'Schiff, Kahn, Nachen*, vergl. nävyä- *Strom*.
kurd. LW. nav; oss. LW. d. navä, t. nau- 'Schiff';
arm. nav 'Schiff*, navem 'schiffen* (H. No. 216).
naf 'Schilf*, vergl. tiäüej siehe unter nei (No. 1060).
*) Justi vergleicht ZDMG. 46, 282 arm. N. pr. Anak^ aber gegen
seine Lesung der betr. Gemme sprechen die voUständig deutlichen
Buchstaben auf dem Steine.
«j Vergl. Bartholomae, BB. XVII, 132.230 —
V
1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
Vers 586).
=== HRN leaf ===
243
```


## [2026-09-05T17:30:03.691Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=420 && NR<=421' BRT.txt | grep -o \"dänu[^ ]*\" | head -20\necho \"--- search headword bullets with dänu in leaves 418-422 ---\"\nawk 'BEGIN{RS=\"\\f\"} NR>=417 && NR<=422 {print \"LEAF \" NR; print}' BRT.txt | grep -n \"dänu\\|Dänav\\|Fluss\" | head -20"
}
```


### [2026-09-05T17:30:05.498Z] TOOL RESULT

```
--- search headword bullets with dänu in leaves 418-422 ---
88:•  j.  däityä-  f.  Name  eines  Flusses**  in AiryanaVa^ah  (sd.):  tarn  yazata  ..  zatri.- vairil  *pasne  apö  "yayh  Vt5. 112;  g.f), I/.61; — mmS ape  'yayaYti.21.  a)sonst mit  vatiuhi-:  äpS  vanuAli'  .  .  vaahuyh 'yayä  V.  ig.  2;  —  tarn  yazata  .  .  zara- ^uHrS  airyene  valjaki  vauhuyä  °yays  ". .  in dem  arischen  Vaijah  der  guten  D"  Yt 5.104;  17, /5-«.  V./.z,  2.20'.
155:•  j.  'dänav-  f.  'Fluss,  Strom':  ■'nus  . .  *frä bunät  laHntis  "ein  aus  der  Tiefe  (der  Erde) her  strömender  Fluss"  Aog.  77.  IN.  52: lies  dainunam\
165:—  Pü.!  pa röi viÜnilSrih'}  "für das  Amt  dessen, der  den  Fluss  (aus  dem  das  Wasser  geholt werden  soll)  aassucht";  erl.;  pa  äiariiA.
```


## [2026-09-05T17:30:23.011Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /\\[pdf page 134\\]/' incoming/IRN/IRN_pages.txt | head -60"
}
```


### [2026-09-05T17:30:24.790Z] TOOL RESULT

```
[pdf page 134]
نام‌های ایرانی در پیرامون دریای سیاه ۱۳۳
واقع شده است ومقصود از روم د رکتاب‌های پهلوی‌هميشه آسیای صغیر و بیزانس
بوده است .

اما خشین در واژه‌های پارسی از جمله در برهان قاطع بدو صورت چنین
آمده است:

«خشین هرچیزی که به کبودی مایل و سیاه‌رنگ و تیره باشد» .

«خشی: چیزی را گوین د که سفیدی‌آن به نهایت رسیده باشدیعنی سفید سفید
وبعضی گویند بمعنی‌خشینه اس ت که سیاه تیره‌رنگك وبکبودی مایل باشد» . دراینجا
نیز چنانکه دیده می‌شوداین‌واژه» هم‌بمعنی درخشان آورده شده که همان 352622
است و هم بمعنی‌ناد رخشان‌و تیر ه که همان 2732682 کهن است . بناپراین ا وکسن
اه از واژ 22360 ایرانی گرفته شده و سپس نام باستانی آن ترجمه گشته و در
زبانهای مختاف دریای سیاه نامیده شده است.

تعداد زیادی از نام رودهای بزرگك و کوچککه اطراف دریای سیاه نیزريشه
و بن ایرانی دارند.بزرگترین این رودخانه‌هادانوب اس تکه‌از جنگل سیا‌سرچشمه
می‌گیرد و از آلمان و اتریش و هنگری و یوگسلاوی‌و رومانی می گذردوبدریای
سیاه فرو میریزد. این رودخانه در سیر خود در آلمان 4022 » درچکسلوا کی
( » در بلغارستان و یوگسلاوی 40:3۷ و درهنگری 4072 نامیده می‌شود
و همه این نامها از ريشة 4300 اوستایی بمعنی رود و 1221۷2 فارسی باستان
بمعنی جاری شدن است.

د کیب فارسی باستا ن کاتال سوئٌز که بفرمان داریوش بزرگ کنده شده
است واژهٌ 428۷2 در جملةٌ زیر بکار رفته است:

اواج نحل وند‌وق7 1 ۶2 ها۵+ حصسقد دقعام عمط

یعنی از «پیراو» نام رود ی که در مصر جاریست .

ريشه ص43 در یک واژه فارسی امروزی نیز باقی است و آن واژه «ناودان»
اس ت که م رکب است از ۹32+ 2۷. واژْهٌ ناو در فرهنگك‌های فارسی بمعنی‌چوی
```


## [2026-09-05T17:30:25.481Z] TOOL CALL #23: Bash

```json
{
 "command": "pdftoppm -f 109 -l 109 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg109 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T17:30:27.652Z] TOOL RESULT

```
total 33288
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 13:30 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63543 Sep  5 13:30 pg109.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


## [2026-09-05T17:30:46.567Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /دانوب|ناودان/ {match($0,/\\[pdf page [0-9]+\\]/); print substr($0,RSTART,RLENGTH); print substr($0,1,120); print \"---\"}' incoming/IRN/IRN_pages.txt | head -40"
}
```


### [2026-09-05T17:30:48.216Z] TOOL RESULT

```
[pdf page 13]
[pdf page 13]
۲ ایرانویچ
افغانستان و:ایران و آسیای کوچک رفته‌اند . اما ف�
---
[pdf page 25]
[pdf page 25]
23 ایرانویج
آمده است. ایران که‌م رکز جهان است نصیب‌ایرج می�
---
[pdf page 134]
[pdf page 134]
نام‌های ایرانی در پیرامون دریای سیاه ۱۳۳
واقع شده است ومق
---
[pdf page 135]
[pdf page 135]
۱۳4 ایرانویج
آب یا هرچیز دراز و بیان تهمی است و «دان» بمعنا
---
[pdf page 212]
[pdf page 212]
فهرست کسان ... ۲۰۱
ی
خاتون (زن خاقان ترکد) ‎۱۸٩‏ دارستر وود 
---
[pdf page 213]
[pdf page 213]
۰۲ ایرا نویج

دریاچه چیچست وه (- ۱۰۳ ۱۹۲ دشت‌گردان ۱۳

دریا�
---
[pdf page 214]
[pdf page 214]
فهرست ان ... 5 ۳۰۳
دینور ۱۹۳-۱۹۶ رود دونتز ۱۲۶
دیودورسیسیلی �
---
```


## [2026-09-05T17:30:52.024Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /\\[pdf page 135\\]/' incoming/IRN/IRN_pages.txt | head -25"
}
```


### [2026-09-05T17:30:53.658Z] TOOL RESULT

```
[pdf page 135]
۱۳4 ایرانویج
آب یا هرچیز دراز و بیان تهمی است و «دان» بمعنای جریان آب است و بررویهم
بمعنی چیز میان‌تهی اس تکه‌آب درآن جاری باشد و دانوب بمعنی آب جاری است
و شکل بلغاری و یوگسااوی‌این واژه که 1002۷ است ترکیب آنرا بهتر نشان
می‌دهد.

«دن» 42۳ در زبان ایرانی آس ی کنونی‌نیز بمعنی رود است و تعداد زیادی
از نام‌های رودهای تفقاز شمالی بادن 40 ختم می‌شوند مانند » فیاگك دن »
گیزیل‌دن» آردن و غیره.
واژه 120 بصورت 408 در رودخانه‌های‌بزرگك دیگر نیز دیده می‌شودمانند
رود 40۳ که بدریای آزوف می‌ريزد و بصورت مرکب در نام‌رودهای دیگرآمده
بانند «0عفصل وتاوه‌نطل که بدریای سیاه می‌ریزند و 400612 که از رودهای
روسیه جنوبی است واين واژه حتی در رود 402۶ که بدریای چین می‌ریزد نیز
دیده می‌شود .
ناحیه تنگه "کرج 16700 که دریای آزوف را بدریای سیاه می‌پیوندد و
شهر ی که در کنارآن بوده است؛درروزگا ران کهن نهم1162ص2م با نم 2علناصد0
نام داشته است ونیز رودی که امروز بنام 2 يا [080م معروف است همین‌نام را
داشته است .,
نام « پنت یکاپه » نیز ایرانی است و ترکیب یافته است از واژه‌های
2+ 0220 وااصدم در زیان اوستایی‌بمعنی راه است . دراوستا درمهریشت چنین
آمده است :
1 510۴۵ 61 مد داد قلمقم خععاة ناندعدل ممقاصدم راکمه
از نج
که معنی آن چنین است: راست‌ترین راه رامی‌دهد آتش بزدا اهورا به کس ی که
```


## [2026-09-05T17:31:06.223Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T17:31:06.230Z] TOOL RESULT

```


```


## [2026-09-05T17:31:09.516Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Danube",
 "prompt": "Full etymology of Danube: Latin Danuvius, Celtic, Iranian/Scythian dānu-, Greek forms."
}
```


## [2026-09-05T17:31:10.391Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Danube",
 "prompt": "Etymology of Danube: give the full chain (Latin Danuvius, Celtic, Proto-Indo-European *deh2nu-, Iranian/Scythian), and any mention of Greek forms and Old French."
}
```


### [2026-09-05T17:31:13.767Z] TOOL RESULT

```
# Etymology of Danube

The Danube's name traces back through multiple linguistic layers. According to the Online Etymology Dictionary, the term comes "from Latin _Danuvius_ (Late Latin _Danubius_), from Celtic _\*danu(w)-yo-_, from PIE _\*danu-_ 'river.'"

The word shares a common root with other European river names like the Don, Dnieper, and Dniester, all deriving from the Proto-Indo-European term for "river." The name appears across different languages as German _Donau_, Hungarian _Duna_, and Russian _Dunaj_, reflecting the river's cultural significance across Central and Eastern Europe.
```


### [2026-09-05T17:31:17.848Z] TOOL RESULT

```
# Etymology of Danube

The word "Danube" traces back through multiple language layers:

**Latin Foundation:** The term derives from Latin *Dānubius*, which was borrowed from earlier sources.

**Celtic Origin:** Latin inherited it from Proto-Celtic *Dānowyos*, described as "an extended form of the river-name *Dānu*," connecting to Welsh river names like *Donwy*.

**Proto-Indo-European Root:** The Celtic forms ultimately stem from Proto-Indo-European *déh₂nu*, meaning "river, river goddess," which relates to the root *dʰenh₂-* meaning "to set in motion; to flow."

**Related Language Forms:** The etymology notes cognates across Indo-European languages, including Persian *danidan* (to hasten), Ossetian *don* (water/river), and Sanskrit *dhánvati* (it flows). These connections reflect the ancient river-name's wide distribution across Eurasian language families.

**Medieval French:** The English word was borrowed from Middle French *Danube*, which inherited it from Old French forms attested since the mid-12th century, ultimately preserving the Latin transmission of the Celtic river-name.
```


## [2026-09-05T17:31:25.295Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88%D8%AF%D8%A7%D9%86",
 "prompt": "Persian ناودان: etymology — what is it composed of (نav + dān)? What does -دان mean? Any Middle Persian form?"
}
```


## [2026-09-05T17:31:27.926Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B4%CE%AC%CE%BA%CF%84%CF%85%CE%BB%CE%BF%CF%82",
 "prompt": "Ancient Greek δάκτυλος: full etymology section — is it Pre-Greek per Beekes? Any Semitic connection (Aramaic diqlā, Arabic daqal, Hebrew deqel) mentioned? Meaning 'date (fruit)'?"
}
```


### [2026-09-05T17:31:31.285Z] TOOL RESULT

```
# Persian ناودان (nâvdân)

## Composition

The word is composed of two Persian elements:

- **ناو** (nâv) - meaning "boat" or "ship"
- **دان** (dân) - a suffix denoting a place or container

## The -دان Suffix

The suffix "-dān" functions as a locative marker in Persian, meaning "place of" or "container for." In this context, it transforms the root into a noun indicating a receptacle or channel.

## Middle Persian Origins

According to the etymology section, the word derives from Middle Persian roots:
- "nʾw" evolved into modern Persian ناو (nâv)
- "YDOYTWN-stn'" developed into modern Persian دان (dân)

## Meanings

The resulting compound **ناودان** refers to:
1. "gutter" or "drainpipe" (current usage)
2. "canal" or "aqueduct" (obsolete sense)

The semantic progression reflects how a boat-related term became associated with water channels and drainage systems.
```


### [2026-09-05T17:31:32.826Z] TOOL RESULT

```
# Etymology of δάκτυλος

According to the Wiktionary entry, the ancient Greek word has an uncertain origin. The source states: "Uncertain; probably Pre-Greek. Possibly related to Latin digitus, though the details are unclear."

Regarding Semitic connections, the entry confirms these are documented. It explains that the "date" meaning likely came through folk etymology from Semitic sources, specifically mentioning: "Arabic daqal, 'variety of date palm' or Hebrew deqel, 'date palm'."

The entry does not mention Aramaic. The word's primary meaning is "finger," with secondary meanings including toe, a unit of measurement, and the metrical dactyl. The fruit sense (date) represents a distinct semantic development based on this Semitic influence.
```


## [2026-09-05T17:31:48.003Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%82%D9%84",
 "prompt": "Arabic دقل (daqal): meanings and etymology. Also any Persian entry for دقل. Is it 'inferior date palm'? Related to Hebrew deqel / Aramaic diqlā?"
}
```


## [2026-09-05T17:31:49.946Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%A9h%E2%82%82nu",
 "prompt": "PIE *déh₂nu: meaning, descendants (Avestan dānu-, Ossetian don, Sanskrit dā́nu-, Scythian, Celtic Dānuwyos), and whether Greek Danaoi is listed."
}
```


### [2026-09-05T17:31:54.457Z] TOOL RESULT

```
# Arabic دقل (daqal) - Etymology and Meanings

## Meanings

The word has two primary senses:

1. **A variety of dates** (fruit and tree) - The meaning has shifted historically. Anciently it denoted date palms producing abundant but inferior-quality dates, "often characterized by being hard, small, or having a meager ratio of flesh compared to its pit." In modern usage, it refers to a supreme date variety, particularly the popular دَقَلَة النُور (daqala(t) an-nūr).

2. **A mast or ship part** - The term refers to "topgallant, topmast, mast tree, mainmast."

## Etymology

The word derives from Proto-West Semitic *daqal-. Notably, the mast sense appears influenced by semantic borrowing from Aramaic דִקְלָא (diqlā, "date palm; topgallant"), though related terms appear in other Semitic languages including Mehri and Soqotri.

The Hebrew דֶּגֶל (déḡel, "flag") is etymologically related to Akkadian dagālu ("to look at"), representing a separate semantic development.
```


### [2026-09-05T17:31:55.583Z] TOOL RESULT

```
# Proto-Indo-European *déh₂nu

Based on the Wiktionary article, **\*déh₂nu** is a reconstructed Proto-Indo-European noun with two meanings:

1. **River**
2. **River goddess**

## Key Information

The word is grammatically classified as a neuter, athematic, amphikinetic u-stem noun.

## Documented Descendants

The article traces descendants across multiple language families:

- **Proto-Celtic:** \*Dānu (with further derivatives like \*Dānowyos)
- **Proto-Indo-Iranian:** \*dáHnu
  - **Sanskrit:** दानु (dā́nu)
  - **Proto-Iranian:** \*dáHnu

## Important Note

The webpage provided does **not** list Greek Danaoi as a documented descendant of \*déh₂nu. The descendants section only explicitly mentions Celtic and Indo-Iranian branches. Any connection to Greek Danaoi would require sources beyond this particular Wiktionary entry.

The entry cites J. P. Mallory and D. Q. Adams's *Oxford Introduction to Proto-Indo-European* as its reference source.
```


## [2026-09-05T17:31:59.633Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg109.png"
}
```


### [2026-09-05T17:31:59.984Z] TOOL RESULT

```

```


## [2026-09-05T17:31:59.981Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T17:32:44.352Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol1 leaf of Danube line 86476 ===\"\nawk 'NR<=86476' FSD_vol1.txt | grep -c $'\\f'\necho \"=== page markers near ===\"\ngrep -n \"^[0-9]\\{3\\}$\" FSD_vol1.txt | awk -F: '$1>86300 && $1<86700' | head\necho \"=== Danube entry text ===\"\nsed -n '86476,86480p' FSD_vol1.txt | cut -c1-900"
}
```


## [2026-09-05T17:32:44.498Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=date",
 "prompt": "Give the etymology of 'date' meaning the fruit (date2), and of 'Danube' if present."
}
```


### [2026-09-05T17:32:45.958Z] TOOL RESULT

```
=== FSD vol1 leaf of Danube line 86476 ===
700
=== page markers near ===
86301:651
86425:652
86691:654
=== Danube entry text ===
d an 'gle •monkey,  l   dangl»mun  j;  2d&o'CI*m6n  y,n.  Early  Danube*,  1   dan'ytlb;  2   dkn'yub  (G.  Do'nau,  1   dO'nau;  2 Chinese  bronze  coins,  often  used  ft s   danglers  on  musical  In-  d6,n  “   tf  {A^  u'tir.l  A   river  of  Europe,  flowing stru  m   en  ts,  hen  ceth  o   n   am  o.  2,000  m.  from  Baden,  through  Germany,  Austria,  Hungary,
Dangs,  1   5S05k?ind.a^Bnn(?i!ie  m   A   hUly  trflCt  lD  Bombay  Jugoslavia,  Bulgaria,  and  Roumanla  to  the  Black  Sea.  2.  A
D»'n^n“  1 dPm"  i:  2   dVnKcn  d.  CM.  Of  or  pertnlnlns  to  .S!  l* d^tt'blSnT'  BeTdnnlnn
the  uppermost  group  of  strata  comprised  in  the  Upper  Crc-  Dt0oi-  bordering  ^n^tbe  river  Danube -the  Danublan
A   Danish  Idiom  Dan'rcrsTl  dan'var:;  2   din’verj,  n.  A   manufacturing  town Dan'lc?.  l   dayn'ye!  ”fi^  2   di“  y^  n.  1.  A   maacullne  'ounty’  Mas3"  tome  ot  tie  poct  Whltt,cr  ,or
```


### [2026-09-05T17:32:51.196Z] TOOL RESULT

```
# Etymology Response

## Date (the fruit)

According to the dictionary entry, the etymology of "date" (meaning the fruit) traces back through multiple languages: "Middle English, from Old French, from Old Provençal _datil_, from Latin _dactylus_, from Greek _daktulos_, finger, date (from its shape)."

The Greek origin is particularly interesting—the word originally meant "finger," with the fruit receiving this name based on its physical resemblance to that body part.

## Danube

The Danube is not mentioned anywhere in the provided web page content, so I cannot offer an etymology for that term based on this source material.
```


## [2026-09-05T17:33:03.683Z] TOOL CALL #36: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/Danube\" \\\n \"https://en.wiktionary.org/wiki/Danube\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88%D8%AF%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%CE%B4%CE%AC%CE%BA%CF%84%CF%85%CE%BB%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%82%D9%84\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%A9h%E2%82%82nu\" \\\n \"https://ahdictionary.com/word/search.html?q=date\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 109, roots Dâ 2/Dânu and Daqal: Danube chain, nâvdân, Greek daktulos/Arabic daqal\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T17:33:07.071Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3a3b6d7497c1e1f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6c9085bc41e57c54.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e546ea4c1a33db8f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2c4e9682f4b18a5b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/927eda0ce5233ae6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/196c8250a01f8342.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/18da60ec4a0e2821.txt
```


## [2026-09-05T17:33:21.794Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== WLD Bd1 Danuvius printed page ==\"\nawk 'NR<=79864' incoming/WLD/WLD_Bd1_pages.txt | grep -c $'\\f'\nsed -n '79860,79868p' incoming/WLD/WLD_Bd1_pages.txt | cut -c1-500\necho \"== SYN Danube/river ==\"\ngrep -n \"Danube\" SYN.txt | head -3\necho \"== IEC danu ==\"\ngrep -n -i \"^danu\\|dānu\\|Donau\" IEC.txt | head -5\necho \"== AHD watkins da-nu ==\"\ngrep -n \"^da\\|dhen\" AHD_watkins1985.txt | head -8"
}
```


### [2026-09-05T17:33:23.560Z] TOOL RESULT

```
== WLD Bd1 Danuvius printed page ==
857
 144, Yf. LEWb. s. v. (wo iiber andere Deutungen von fons).
                2

   Fernzuhalten sind gr. dig, dt. Dime (s. dheti- „stieben") und ai. dhanus
 dhanvan- „trockenes Land" (s. *dhen- „Flache“). Danuvius „Donau“ kelt.
 Entw. aus * dhonu-1              Ygl. vielmekr oben                       S. 763.
                                                        dhen-                                                                          853

                                                                                                 11
== SYN Danube/river ==
1390:From Lat. rivus (through rius) come Sp. rfo ‘river’ (Olt. rio ‘brook’ and ‘riy- er’, OF r. ri ‘brook’), Rum. rité ‘river’ (now fluviu for large rivers like the Danube). Dim. forms for ‘rivulet, brook’, Lat. rivolus, It. rivolo, Rum. rviilet, It. ruscello, Fr. ruisseau, REW 7341, 7338a. Gamillscheg 777.
== IEC danu ==
== AHD watkins da-nu ==
202:dail-. To divide. Northern Indo-European root.
355:da-. To divide. Contracted from *dag-. Variant *dai- from extended root *dagi-. 1. Root form *dai- in Greek daies- thai, to divide: GEODESY. 2. Suffixed variant form “di-t- in Germanic *tidiz, division of time, in: a. Old English tid, time, season: TIDE!; EVENTIDE; b. Old English de- nominative tidan, to happen (< “to occur in time”): TIDE?; c. Old Norse tidhr, occurring: TIDINGS. 3. Suffixed variant form *di-mon in Germanic *tim6én- in Old Eng- lish tima, time, period: TIME. 4. Suffixed form *dd-mo-, perhaps “division of society,” in Greek démos, people, land: DEME, DEMOS, DEMOTIC; DEMAGOGUE, DEMIURGE, DEMOCRACY, DEMOPHOBIA, ENDEMIC, EPIDEMIC, PAN- DEMIC. 5. Suffixed form *dai-mon-, divider, provider, in Greek daimén, divinity: DEMON. [Pok. dé- 175.]
356:dail-. To divide. Northern Indo-European root. 1. Ger- manic “dailjan in Old English d%lan, to share: DEAL. 2. Germanic *dailaz in Old English dal, portion, lot: DOLE!, 3. Germanic prefixed form *uz-dailjam, “a por- tioning out,” judgment (*uz-, out; see ud-), in Old English ordal, lot, apportionment: ORDEAL. [In Pok. da- 175.]
357:daiwer-. Husband’s brother. Latin Jévir, husband’s brother: LEVIRATE. [Pok. ddiur 179.]
358:dakru-. Tear. 1. Germanic *tahr-, *tagr- in: a. Old Eng- lish téar, tehher, tear: TEAR2; b. Middle Low German tran, tear, drop: TRAIN OIL. 2. Suffixed form *dakru-ma in Latin lacrima (Old Latin dacruma), tear: LACHRYMAL. [Pok. dakru- 179.]
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
1526:FOLIAGE bhel-3 FOLICOLOUS _bhel-3 FOLIO bhel-3 FOLIUM bhel-3 FOLKMOTE mdd- FOLLICLE bhel-2 FOLLICULITIS bhel-2 FOMENT dheg¥h- FOMITE dheg¥h- FOND? bhudh- FONDANT gheu- FONDUE gheu- FONT! dhen-1 FONT? gheu- FOOD pa-
```


## [2026-09-05T17:33:24.985Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== MON danub ==\"\ngrep -n \"دانوب\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -5\necho \"== MON navdan headword ==\"\ngrep -n \"ناودان:\" MON_part2.txt | head -5\ngrep -n \"^ناودان\\|ناودان \\[\" MON_part2.txt | head -5\necho \"== SKT date ==\"\ngrep -n \"^date\" SKT.txt | head -5\necho \"== DEV/PHN datte ==\"\ngrep -n -i \"datte\\|dattier\" DEV.txt PHN.txt | head -5\necho \"== WEB date fruit ==\"\ngrep -n -i \"dactylus\" WEB_vol1.txt LEW_1910.txt LAT.txt | head -5"
}
```


### [2026-09-05T17:33:25.117Z] TOOL RESULT

```
== MON danub ==
== MON navdan headword ==
73548:ناودان: 2۰-۱ (امر.) جایی که در آن ناو 
53114:ناودانی است که آن جمع 
73548:ناودان: 2۰-۱ (امر.) جایی که در آن ناو 
74121:ناودان ننض و بر روی استخوان زند اعلی 
== SKT date ==
4637:date  (»>.  fruit  of  the  palm.  (F.-L.- Gk.>  M.  F-.  dare.  -O.  F.  iiatd  (F.  (iatu\ a  date.-L.  dmfyium,  ace.  of  da<tytu%.^ Gk.  &i«TwXot.  a  <laic.  Pfob.  «#/  allictl  to SojvrvAot  aboNC.  but  of  Semitic  ori|frn.
== DEV/PHN datte ==
DEV.txt:1226:-  Ifist.  nul.  t.  i",  1"  partie,  p.  53-58.  MM.  Cammas  et  André  Lefèvro ont  eu  tort  d'écrire  downs  par  un  s  au  singulier  :  cr  C'est  le  doiuns ,  qui  diffère du  dattier  par  la  conformation  et  par  le  fruit.  •>■'  {Voy.  en  Egypte,  dans  le  Tour du  monde,  1'°  série.  i863,  p.  -209.)
DEV.txt:1367:FouTAH.  Portug.yô/a.  Le  nom  de  cette  étoffe  (ou  vête- ment) est  persan  :  »:iysfoutah;  mais  il  a  surtout  été  répandu par  le  commerce  arabe.  Les  Arabes  écrivent  é^^foufa. Ce  fut  de  bonne  heure  un  objet  d'échange  avec  les  tribus africaines  et  océaniennes.  Dans  un  ouvrage  du  x^  siècle de  notre  ère  intitulé  Jsi^l  o*.j1:^  Merveilles  de  finde,  on voit  un  navire  arabe  commerçant  avec  des  nègres,  payer le  prix  des  esclaves  avec  ce  produit  de  l'industrie  orien- tale :  rvw^i  ci^i»Jî^  r^^^  i^iojiJij  /©-g-Aïa^j  (^^x^iiJj  î^et  nous  en achetâmes  ayec  des, foutahs ,  des  dattes  et  des  bagatelles,  w (Man.  appart.  à  la  collect.  de  M.  Schefer,  p.  8.)  (Voir  sur ce  mot  Dozy,  Gloss.  p.  270,  et  S.  de  Sacy,  Chrest.  ar. t.  F,  p.  1  96.)
DEV.txt:1579:JuBis,  Terme  de  commerce.  Raisins  secs  en  caisse.  C'est une  altération  de  l'arabe  L^-y^'^  zebib,  raisin  sec,  comme  le prouvent  les  vieilles  formes  azebit,  auzibet  :  «  Pro  cargua de  azebits  seu  racemis,  ?5  dit  un  vieux  tarif  de  Carcassonne, cité  dans  Du  Gange.  Ces  dernières,  ainsi  que  l'espagnol nzebibe,  acebibr,  ont  gardé  l'article  al^  dont  le  l  s'assimile au  z  suivant  :  az~zebïb.  En  portugais,  acipipe  a  pris  une  si- gnification plus  générale,  celle  de  menues  friandises  propres à  aiguiser  rappétit,  à  rafraîchir.  Diverses  contrées  musul- manes, ne  buvant  pas  de  vin,  livraient  leurs  raisins  séchés au  commerce,  et  cet  aliment  était  fort  estimé  des  Arabes; Razi  le  regarde  comme  plus  nutritif  que  la  datte  :  «-.vH>y^ A^-o  t «xil^  ^^yï]  -«Oi  J^Xi  IX  ^ô^j^_  ^  ff  Le  raisin  sec  n'obstrue point  comme  fait  la  datte,  bien  que  plus  nourrissant qu'elle.:)?  (M an.  arabe  déjà  cité,  fol.  63  verso.)
DEV.txt:1611:creuse  symétriquement  sur  une  surface  plane,  et  dans lesquels  on  pose  des  cailloux  ou  des  noyaux  de  datte  en guise  de  pions,  comme  pour  le  jeu  de  dames  :  '<Jii^  khar- bcga.f^  (Cherbonneau,  Dict.  franc. -arab.  pour  la  conversa- tion en  Algérie.)
DEV.txt:2177:lliiole  et  les  anciens  botanistes  ra[)|)ellent  lamar  tndi.  Dans un  passage  de  Marco  Polo  cité  par  M.  Littré,  on  lit  tama- ramli :  «Si  donnent  aux  marcheans  à  faire  et  à  boire  une chose  qui  a  nom  tamamndi,  qui  leur  fait  aller  hors  ce (pi'ils  ont  au  ventre,  w  En  effet,  le  tamarin  ou  fruit  du  ta- marinier a  été  souvent  employé  pour  faire  avec  la  casse un  liquide  laxatif ^  C'est  Tarbre  ^^ùJJ>  ^Ji  tamr  hindi,  datte indiemie.  Le  tamarinier  n'est  pas  un  dattier  et  n'offre  au- cune ressemblance  avec  un  arbre  de  cette  espèce;  mais son  fruit  est  une  gousse  qu'on  a  pu  comparer  à  la  datte. Le  mot  tamr,  datte,  se  retrouve  dans  l'espagnol  tumaras, (rochet  de  dattes.
== WEB date fruit ==
WEB_vol1.txt:48559:dag’tyl, n. [L. dactylus; Gr. daktylos, a finger, a measure of length, a dactyl.]
WEB_vol1.txt:48564:3. same as dactylus. —
WEB_vol1.txt:48624:ley Pholas dactylus, a European piddock.
WEB_vol1.txt:49488:ae palm; Es dactylus; Gr daktylos, a date, lit., a finger, so named from its shape.]
WEB_vol1.txt:70780:know. pels 2. to love. [Obs.] ocka fan’cy-free, a. 1. free to fall in love; not mar- ried, engaged, etc. 2. carefree, fan’cy līne, in nautical usage, a line rove through a block at the jaws of a gaff, used as a downhaul. fan’cy-sick, a. love-sick. fan’cy-wòrk, 7. ornamental knitting, crochet- ing, tatting, embroidery, ete. fan-dañ’gō, n. [Sp., from the African name.) 1. a lively Spanish dance in rhythm varying from slow to quick three-quarter time. It is danced by couples, who hold castanets or sometimes tambourines. 2. music in triple time, suitable for such a dance. p 3. a ball or dance; hence, any noisy enter- tainment; a merrymaking. fane, 7. [L. fanum, a sanctuary, a temple, from farı, to speak, consecrate.] a temple or church. [Archaic or Poet.] |, : From men their cities, and from gods their fanes. —Pope. fāne, n. 1.a weathercock; a vane. [Obs.] 2. a flag. [Obs.] fa-ne’ga, n. [Sp.] the Spanish bushel. fan’fare, n. [Fr. fanfare, a sounding of trumpi ets; Sp. fanfarria, bluster, vaunting, from T. farfar, talkative] e auii of trumpets; also, a noisy or showy display. fan/ia-ron n. (Fr. fanfaron; Sp. fanfarron, $ blusterer.] a swaggerer; a boaster; a vain pr tender. fan- far-on-āde’, 7. 2. fanfare. gangoor 2 a narmi tyodactylus gecko, 5 rays Sound lobes used for adhering fang, v.t. [ME. fangen, fongen; AS. fon, to
```


## [2026-09-05T17:33:41.825Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== MON navdan ==\"\nsed -n '73545,73552p' MON_part2.txt\necho \"== SKT page ==\"\ngrep -n \"^[0-9]\\{2,3\\}$\" SKT.txt | awk -F: '$1>4500 && $1<4700' | head -4\nsed -n '4635,4640p' SKT.txt\necho \"== ARY nav/danu ==\"\ngrep -n \"ناو\\b\\|دانوب\" incoming/ARY/ARY_pages.txt | head -5\necho \"== BQT navdan headword v4 ==\"\ngrep -n \"ناودان\" incoming/BQT/BQT_v4_pages.txt | head -3"
}
```


### [2026-09-05T17:33:43.778Z] TOOL RESULT

```
== MON navdan ==
ناوخدا: ۱-3 [- ناخدا| (ص‌مر. امر.) 
ملاح» کشتیبان. 

ناودان: 2۰-۱ (امر.) جایی که در آن ناو 
(ممر سفالین آب) گذارند (رشیدی). ممر 
آب (اطلاق محل به حال). ممر خروج آب 
پشت بام که از سفال یا آهن سفید سازند. 
جوی» نهر. مجرایی که گندم از دول به 
== SKT page ==
4548:105
Da06 ;  see  Dart.
Daotyl.  ^L.  -  Gk.^ metrical  foot  marked  - a  Anger,  a  dactyl.     See  Toe.
date  (»>.  fruit  of  the  palm.  (F.-L.- Gk.>  M.  F-.  dare.  -O.  F.  iiatd  (F.  (iatu\ a  date.-L.  dmfyium,  ace.  of  da<tytu%.^ Gk.  &i«TwXot.  a  <laic.  Pfob.  «#/  allictl  to SojvrvAot  aboNC.  but  of  Semitic  ori|frn.
Dad    (C*     VV.  tad  Irish  daid^  Hret.  /«/, /*/.  father -fCk.  T'"n,  Skt.  ftiJd  dad.
BiiHbdil ;  see  Aaphodol.
Dagger.  (,C.)    ^L  1'«  du^rt ;  allied  to
== ARY nav/danu ==
86:نژادی بر سایرین برتری کامل داشتند. چون در آلمان و اسکاندیناوی اینگونه مردم فراوان ترند؛ آنها
95:پست‌تر از آریایی‌های ناب (یعنی آلمانی‌ها و اسکاندیناوی‌ها) بودند؛ تا چه رسد به ایرانی‌ها و
113:ارتش و فناوری وگسترش از راه کوچگری را میسر نمود. بنابراین دیدمان (17733083) مردمان این
655:(5۸۸/۸71۸07) نه تنها در کرانه‌های رود دانوب کوج نشین شدند پلکه در قرن دوم میلادی برای
785:اسکاندیناوی: دانمارکی» نروژی» سوئدی» و ایسلندی (با هم حدود ۲۰ میلیون نفر). کهن‌ترین متون
== BQT navdan headword v4 ==
5251:ونگین هم‌آمده است . مورد آب وغیره۴ - و بمعنی‌ناودان هم بنظرآمده‌است
7711:و تحتانی » بمعتی نانغواء است که زئیان باشد . | کوچك - وناودان ‎٩‏ بام خانه - و آنچه کندم
7734:(زورق ) , 888 (قنات » ناودان ؛ راه آب ) « ژابا صس 4۱۷ ‎٩‏ - رك : ناودان .
```


## [2026-09-05T17:33:53.229Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7725,7745p' incoming/BQT/BQT_v4_pages.txt\necho \"=== pdf page tag ===\"\nawk 'BEGIN{RS=\"\\f\"} /ژابا/ && /ناودان/ {match($0,/\\[pdf page [0-9]+\\]/); print substr($0,RSTART,RLENGTH)}' incoming/BQT/BQT_v4_pages.txt | head -3"
}
```


### [2026-09-05T17:33:55.035Z] TOOL RESULT

```
۹ ر3 : نانوا. ۴ < بانخواء (همم.) ۴ - «نان ونمکدان شکتن ۰
حرام نمکی کردن > « زشیدی > ۴ - رشیدی گوبد : « نانیوشان » ناشنیده و بی‌خبر >
عرچند لغة ترکیبی صحیح است از : نا( انفی . سلب )+ نیوشان ( صفت فاعلی از نیوشیدن ).
ولی‌شاهدی‌ندارد , ظ . مصحف «ناپیوسان» (ه.م.) * - پارسی باستان -82۷1918 (جهاز).
اوستا -88۷9228 ( کشتی ران ) , هندی باستان -82۷ ( کشتی» قایق کرجی ) » ارمنی 18۷
(کعشتی )۰ 88۷602 ( سفر دربا کردن ) « اسشق ۱*۲۶ » هوبشمان کوید : اوستا -18۷228

ارمتی ع 827 ( کنتی ران ) < -اسکریت -78۷2[4 *لانینی 82۷1818 2 ( در
‎ ) ۴‏ هویشمان ۰۱۶۲۶ استی 321 ( کشتی ) «ککه . است ۰۱۲۷ کردی 88۷
(زورق ) , 888 (قنات » ناودان ؛ راه آب ) « ژابا صس 4۱۷ ‎٩‏ - رك : ناودان .
۷ <ناوکه (هم.) :
در تحیر طفل میزد دست و پا آب می برش بناو آسیا .
عطار نیشابوری * رشیدی >.

۸ - چنین است در رشیدی بنقل ازسروری ! درفرهنگه نظام « ومثل جوبك یشت آدمی
بمنی کودیی که برقفرات پشت است, ومثل گودی میان دوکفل فربه اسب ...؟ وهمین صحیح‌است
(ر3 : مازن) ر3 : ناو4 . ‎٩‏ - رك4 : ناویدن . *- در رشیدی آمده است . از :
- تلو (هم.) ۳+ آنیدن (پسوند مصدر متمدی ) » متعدی « ناویدن » (ع.م.)

* نافوا - بسکون سوم *< نانبا « فولرس ]] ۶۱۲۸۹ » از : نان وا ( پسوند پا
قی *کردی 038 - 228 ( بان پزخانه ) « ژابا ی 2۱۹ > ؛ پزنده و فروشندة نان :
=== pdf page tag ===
[pdf page 193]
[pdf page 194]
```


## [2026-09-05T17:34:12.615Z] TOOL CALL #41: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T17:34:12.652Z] TOOL RESULT

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


## [2026-09-05T17:35:43.428Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== KLN Danube ==\"; grep -n \"Danube\\|Danub\" KLN_1966.txt | head -3\necho \"== SKT Danube ==\"; grep -n \"Danube\" SKT.txt | head -3\necho \"== DEV/PHN Danube ==\"; grep -n \"Danube\" DEV.txt PHN.txt LAM.txt 2>/dev/null | head -3\necho \"== WEB Danube ==\"; grep -n \"Dan'ube\\|Danube,\" WEB_vol1.txt | head -3\necho \"== FVQ/AFM daqal ==\"; grep -n \"daqal\\|dakal\\|diql\" FVQ_pages.txt AFM_pages.txt PHN.txt 2>/dev/null | head -5\necho \"== LEW/LAT dactylus ==\"; grep -n \"dactylus\" LEW_1910.txt LAT.txt | head -3\necho \"== FSD date fruit ==\"; grep -n \"dactylus\" FSD_vol1.txt | head -3"
}
```


### [2026-09-05T17:35:43.573Z] TOOL RESULT

```
== KLN Danube ==
10300:Danaiis,  n.,  a  king  of  Argos,  who  commanded  his fifty  daughters,  the  Danaides,  to  murder  their husbands  on  the  wedding  night  ( Greek  mylhol.) —  L.  Danaus,  fr.  Gk.  Aavaop  (whence  the  pi. Aavaoi, ‘theDanaans’,  i.e.  ‘descendants  or  sub¬ jects  of  Danaiis’,  whence  ‘the  Greeks’,  in  gen¬ eral),  which  prob.  derives  fr.  Heb.-Phoen.  Dan, and  lit.  means  ‘one  who  judges’;  see  Dan,  PN., and  cp.  Danae,  Danaides.  This  etymol.  is  cor¬ roborated  by  the  fact  that  the  myth  of  Belus and  the  Danaides  “records  the  early  arrival  in Greece  of  Helladic  colonists  from  Palestine” (quoted  from  Robert  Graves,  ‘The  Greek Myths’,  I,  p.203.  Penguin  Books).  For  other Greek  mythological  names  of  Hebrew  origin cp.  Cadmus,  Niobe.  —  According  to  Kretsch¬ mer,  Glotta  24,  15  fT.,  the  Danaans  are  identical with  the  men  of  Tanaus,  king  of  the  Scythians, who  allegedly  came  to  Argos  in  the  15th  cent. B.C.E.  and  became  blended  with  the  Greeks. Kretschmer  also  assumes  that  there  is  a  relation¬ ship  between  Tanaus  and  the  river  names  Tanais and  L.  Danubius  (whence  F.  and  E.  Danube), and  Ddnu-,  name  of  an  Indo-Iranian  people. See  Frisk,  GEW.,  I,  p.347  s.v.  Aavaot  and  cp. Albert  Camoy,  Dictionnaire  etymologique  de la  mythologie  greco-romaine,  p.42  s.v.  *Da- naos.  —  Cp.  Danae,  Danaides.
10745:Delphinium,  n.,  a  genus  of  plants,  the  larkspur (bot.)  —  ModL.,  fr.  Gk.  SeXipfiaov,  ‘larkspur’, fr.  SeXtpfi;,  gen.  SsXcpivo?,  ‘dolphin’  (see  dol¬ phin);  so  called  from  the  shape  of  its  flowers, which  resemble  a  dolphin, delta,  n.,  1)  name  of  the  4th  letter  of  the  Greek alphabet ;  2)  triangular  area  formed  at  the  mouth of  some  rivers,  as  of  the  Danube.  —  Gk.  SiXza., fr.  Fleb.-Phoen.  ddleth;  see  daleth.  The  a  was added  because  a  Greek  word  cannot  end  with a  x;  cp.  alpha  and  words  there  referred  to. deltafication,  n.,  the  formation  of  a  delta.  — • Formed  fr.  delta  and  -fication. deltaic,  adj.,  forming  a  delta.  —  Formed  fr.  delta with  suff.  -ic.
32752:Rhaetia,  n.,  name  of  an  ancient  Roman  province situated  between  the  Danube,  the  Rhine  and  the Po.  —  L.,  fr.  Rhaeti  (pi.),  ‘the  Rhaetians’. Derivatives:  Rhaeti-an,  adj.  and  n.
== SKT Danube ==
== DEV/PHN Danube ==
== WEB Danube ==
49223:Da-nia/h3 5 A soua biän, a. of the Danube, a river in nF amn Europe, or the regions and peoples
== FVQ/AFM daqal ==
== LEW/LAT dactylus ==
LAT.txt:15707:dactylus, -i n. : eaprunt au gr. BaxxuXoC deaeur <5 dans les langues
== FSD date fruit ==
62557:chan'ga,  1   cfhan'ga;  2   ch&n'ga,  n.  A   mole-cricket  ( Scaptcr - iscus  dldactylus),  which  Infests  and  destroys  corn,  cabbage, turnips,  lawns,  and  general  crops  In  South  America,  the West  Indies,  etc.,  and  attacks  sugar-cane  and  tobacco  In Porto  Rico.  [Porto  Rico.]
64722:cblck'chack,  1   dhik'tfhak;  2   chlk'chiik,  n.  The  gecko [Ptyodactylus  gecko) .   [<  its  cry.]
85830:2.  Anat.  A   finger  or  toe;  a   digit.  3.  Zool.  A   dactylus.  Da'da,  I   da'da;  2   da'da,  n.  A   scbool  of  art  and  litera-  D.  A.  G.,  a&5r.  Deputy  Adjutant-general. 4.  Same  as  dactylus,  3.  5.  A   Unit  of  measure  of  the  ture  founded  in  Zurich,  Switzerland,  in  1916,  which  Da  Ga'ma,  Vas'co.  See  Gama.
```


## [2026-09-05T17:35:55.310Z] TOOL CALL #43: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg109.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/109.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-05T17:35:55.380Z] TOOL RESULT

```
total 3116
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 13:35 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-05T17:43:20.043Z] TOOL CALL #44: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk109.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%A9h%E2%82%82nu\"\nW_DAN = \"https://en.wiktionary.org/wiki/Danube\"\nE_DAN = \"https://www.etymonline.com/word/Danube\"\nW_NAV = \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88%D8%AF%D8%A7%D9%86\"\nW_DAK = \"https://en.wiktionary.org/wiki/%CE%B4%CE%AC%CE%BA%CF%84%CF%85%CE%BB%CE%BF%CF%82\"\nW_DQL = \"https://en.wiktionary.org/wiki/%D8%AF%D9%82%D9%84\"\nAHD_D = \"https://ahdictionary.com/word/search.html?q=date\"\n\ndoc = {\n \"pdf_page\": 109,\n \"book_page\": 79,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n\n # ------------------------------------------------------------------ entry 0\n {\n  \"entry\": 0,\n  \"root\": \"Dâ 2, Dânu\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *deh₂- / *dā- 'to flow, be liquid', u-stem *déh₂nu- (Pokorny dānu-) f. 'river'\",\n  \"note\": \"Pokorny IEW p.175 (POK_01 leaf 185) prints exactly the root Nourai gives: \\\"dā- 'flüssig, fließen'; dānu- f. 'Fluß'\\\", with Skt dā-nu- 'dripping liquid, dew', Av. dānu- f. 'Fluß, Strom', Ossetic don 'water, river', Russian Don / Scythian Tanais, Dnieper and Dniester from Scyth. *Dānu apara- 'hinterer Fluß' and *Dānu nazdya- 'vorderer Fluß', and \\\"Hierher auch kelt. Dānuvius 'Donau'\\\". Root, language label ('Indo-European') and gloss are therefore all correct, and Nourai's two-part gloss 'to flow; river' mirrors Pokorny's two-part lemma. Modern notation writes *déh₂nu 'river, river goddess' (Mallory-Adams, Wiktionary), usually taken as a u-stem beside the verbal root *dʰenh₂- 'to set in motion, run, flow' (Skt dhánvati, OP danuvatiy). Watkins/AHD does not list this root at all — its 'dā-. To divide' with the same Pokorny page 175 is the homonymous root of the next IEW entry, so an 'AHD' citation would not help here.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *deh₂- «روان بودن، جاری شدن» و ستاک اسمی آن *déh₂nu- «رود» در پوکورنی (صفحهٔ ۱۷۵) دقیقاً به همین دو معنا آمده است؛ بازماندهٔ آن در اوستایی dānu- «رود، رودخانه»، سنسکریت dānu- «قطره، مایع»، آسی don «آب، رود» و نام رودهای دون، دنیپر و دنیستر (از سکایی *Dānu apara- و *Dānu nazdya-) دیده می‌شود. در ریشه‌شناسی امروزی این ستاک را به ریشهٔ فعلی *dʰenh₂- «به حرکت درآوردن، جاری شدن» پیوند می‌دهند. ادعای نورایی دربارهٔ خود ریشه درست است؛ مشکل در دو شاخهٔ درونی نمودار («ناودان» و میانجیگری یونانی) است.\",\n  \"sources\": [W_PIE, W_DAN, E_DAN],\n  \"ref_check\": [\n    {\"ref\": \"POK:175\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 185 (printed p.175), under the letter D: \\\"dā- 'flüssig, fließen'; dānu- f. 'Fluß'. Ai. dā-na- ... dā-nu- ... av. dā-nu- f. 'Fluß, Strom', osset. don 'Wasser, Fluß'; russ. FlN Don, gräzisierter skyth. FlN Tanaïs\\\". Exactly Nourai's root box.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.175 (POK_01.txt leaf 185)\", \"stance\": \"supports\",\n     \"note\": \"\\\"dā- 'flüssig, fließen'; dānu- f. 'Fluß'\\\" with WP. I 763 as its Walde-Pokorny reference.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 763, cross-referred from Bd. I 853 s.v. dhen- (WLD_Bd1_pages.txt line 79864)\", \"stance\": \"supports\",\n     \"note\": \"s.v. dhen-: \\\"Dānuvius 'Donau' kelt. Entw. aus *dhonu-? Vgl. vielmehr oben S. 763\\\" — WP treats the material at I 763, the page Pokorny cites for dā- 'fließen'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 pp. 15-16, roots dā- and dhen-¹\", \"stance\": \"silent\",\n     \"note\": \"grep '^da' / 'danu' in AHD_watkins1985.txt: no *dānu- 'river' root; Watkins' \\\"dā-. To divide ... [Pok. dā- 175]\\\" is the homonym, and \\\"dhen-¹. To run, flow ... Latin fons [Pok. 1. dhen- 249]\\\" has no river noun.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, grep 'dānu' / 'Danuvius'\", \"stance\": \"silent\", \"note\": \"no hits in IEC.txt.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 1.36 'river'\", \"stance\": \"silent\",\n     \"note\": \"SYN.txt mentions the Danube only as an example of a large river under Lat. rivus (line 1390); no etymology of the name.\"}\n  ],\n  \"nodes\": [\n\n   {\n    \"id\": 1,\n    \"lang\": \"Avestan / Old Persian\",\n    \"words\": \"dânu; nâv-dân; danuva; Dânavo\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"Two of the four items are right and two are not. (a) Av. dānu- f. 'river, stream' is genuine: Bartholomae AiW col. ~735 has \\\"j. dānav- f. 'Fluß, Strom'\\\" citing Aog. 77 (\\\"a river welling up out of the depth of the earth\\\"), and the derivative dānu.drājah- 'as long as the rivers' (Y. 60.4); it continues PIE *déh₂nu and lives on in Ossetic don and the Scythian hydronyms Tanais, Dāna-pris (Dnieper), Danastius (Dniester). (b) OP danuv- 'to flow' is also genuine: Kent's lexicon has \\\"dan- vb. 'flow' ... danu[vatiy] DZc 9\\\" — Darius' Suez-canal inscription, rauta tya Mudrāyā danuvatiy 'the river that flows in Egypt'; Kent compares Skt dhánvati, i.e. he puts it under the byform root *dʰenh₂-, so this verb stands beside *dānu- rather than under it (short a, not ā). (c) nāv-dān is NOT an Avestan or Old Persian word — it is New Persian and belongs in node 2; nothing of the kind is attested in Bartholomae or Kent. (d) Av. Dānavō is not the Danube: Pokorny p.175 glosses it \\\"av. VN Dānavō Fl. 'Flußanwohner'\\\", the name of a hostile Turanian tribe of river-dwellers (Yt 13.37-38 yūžəm taδa taurvayata vərəθrəm dānunąm 'you who then overcame the might of the Dānus'), which the Rigveda turned into water demons (fem. GN Dānu-). Nourai has read Pokorny's ethnonym as a river name.\",\n    \"derivation_fa\": \"از چهار صورت این جعبه، دو تا درست است و دو تا نادرست. اوستایی dānu- «رود، رودخانه» در فرهنگ ایرانی باستانی بارتولومه (ستون ۷۳۵) ثبت است، و پارسی باستان danuvatiy «جاری می‌شود» در کتیبهٔ کانال سوئز داریوش بزرگ آمده است (کنت، واژه‌نامه)؛ اما کنت آن را با سنسکریت dhánvati می‌سنجد، یعنی زیر ریشهٔ دیگری *dʰenh₂-. در مقابل، «ناودان» هرگز واژه‌ای اوستایی یا پارسی باستان نبوده و فارسی نو است؛ و Dānavō در پوکورنی نام دانوب نیست بلکه نام قومی تورانی به معنای «کناررودنشین» است (یشت ۱۳، ۳۷–۳۸). پس نورایی در خواندن پوکورنی دچار خطا شده است.\",\n    \"sources\": [W_PIE],\n    \"ref_check\": [\n      {\"ref\": \"POK:175\", \"status\": \"partial\",\n       \"note\": \"POK_01.txt leaf 185: supports av. dā-nu- f. 'Fluß, Strom' and has \\\"av. VN Dānavō Fl. 'Flußanwohner' (im Rgveda zu Wasserdämonen geworden, fem. GN Dānu-)\\\" — i.e. a people-name, not the Danube; the Danube is given separately as \\\"kelt. Dānuvius\\\" (leaf 186). Nothing on nāv-dān or on danuva.\"},\n      {\"ref\": \"IRN:123\", \"status\": \"supports\",\n       \"note\": \"Farahvashi, Iranvij (IRN_pages.txt pdf p.134 = printed p.133 in the 6th printing; Nourai's p.123 is the 1368 pagination): \\\"همه این نامها از ریشهٔ dānu اوستایی بمعنی رود و danuva فارسی باستان بمعنی جاری شدن است», and quotes the Suez inscription for danuva. This is where Nourai's four items come from.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW col. ~735 (BRT.txt leaf 420) s.v. dānav-\", \"stance\": \"supports\",\n       \"note\": \"\\\"j. dānav- f. 'Fluß, Strom': °nus .. frā bunāt ... 'ein aus der Tiefe (der Erde) her strömender Fluß' Aog. 77\\\"; also dānu.drājah- 'von der Länge eines Flusses' Y.60.4.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. dan- (KNT.txt line 5514) and DZc 9 text (line 4405)\", \"stance\": \"partial\",\n       \"note\": \"\\\"dan- vb. 'flow': Skt. dhán-vati. danu[vatiy] DZc 9\\\"; text \\\"rauta tya Mudrāyā danuvatiy\\\". Confirms the OP verb but files it with Skt dhánvati (*dʰenh₂-), not with dānu-.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1024, p.230 (HRN.txt line 8886)\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"1024. nāv 'Wasserkanal; Schiffchen', nāvdān. ap. nāviyā 'Flottille'; aw. nāvaza- 'Schiffer' ... ai. nāv- 'Schiff'\\\" — nāvdān belongs to nāv 'boat/channel', with no Old Iranian *dānu in it.\"}\n    ]\n   },\n\n   {\n    \"id\": 2,\n    \"lang\": \"Persian\",\n    \"words\": \"nâvdân «ناودان»\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"The word itself is real — NP ناودان nāvdān 'gutter, roof drainpipe' (older also 'aqueduct, water channel') — but the analysis of its second element is not the received one. Persian nāvdān is nāv 'trough, hollowed channel, small boat' (< MP nāw, OP nāviyā-, Av. nāvaza- 'boatman', Skt nāv- 'ship', PIE *neh₂u-) + the productive suffix -dān 'container / place of' (namakdān 'salt-cellar', qalamdān 'pen-case'), which goes back to the stem of MP dāštan 'to hold' (Wiktionary: MP <YDOYTWN-stn'>). Mo'in defines the word by that very analysis: \\\"جایی که در آن ناو (ممر سفالین آب) گذارند\\\" — 'the place where one sets the nāv (the earthenware water-conduit)'. Nourai's -dān = dānu 'river' comes straight from his source Farahvashi, who writes \\\"«ناو» بمعنای جوی آب ... و «دان» بمعنای جریان آب است\\\"; that is an isolated view, not shared by Horn, Mo'in or Wiktionary. Phonetically nothing decides it (both *dāna- and *dānu- would give NP -dān), so the case rests on the morphology, and the container-suffix -dān is the one Persian actually has in dozens of nouns.\",\n    \"derivation_fa\": \"«ناودان» واژه‌ای اصیل فارسی است، اما تجزیهٔ نورایی پذیرفتنی نیست. مرکب است از «ناو» (از فارسی میانهٔ nāw، پارسی باستان nāviyā-، اوستایی nāvaza- «کشتی‌ران») به معنای جوی و ناودانی میان‌تهی، به‌علاوهٔ پسوند «‌دان» که پسوند ظرف و جایگاه است (نمکدان، قلمدان) و به ستاک «داشتن» فارسی میانه بازمی‌گردد. معین خود همین تحلیل را دارد: «جایی که در آن ناو (ممر سفالین آب) گذارند»، و هرن نیز آن را ذیل «ناو» آورده است. برداشت «دان = جریان آب» از فره‌وشی (ایرانویج) گرفته شده و دیدگاهی تک‌افتاده است؛ بنابراین پژوهش امروزی این پیوند را رد می‌کند.\",\n    \"sources\": [W_NAV],\n    \"ref_check\": [\n      {\"ref\": \"IRN:123\", \"status\": \"supports\",\n       \"note\": \"Iranvij, IRN_pages.txt pdf p.135 (printed 134): \\\"«ناو» بمعنای جوی آب یا هرچیز دراز و میان‌تهی است و «دان» بمعنای جریان آب است\\\"; the previous page adds \\\"ریشهٔ dānu در یک واژهٔ فارسی امروزی نیز باقی است و آن واژهٔ «ناودان» است که مرکب است از nāv + dān\\\". Nourai reproduces his source faithfully.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 1024, p.230 (HRN.txt line 8886)\", \"stance\": \"contradicts\",\n       \"note\": \"nāvdān is listed as a derivative of nāv 'Wasserkanal; Schiffchen' (ap. nāviyā, aw. nāvaza-, ai. nāv-); no dānu- anywhere in the article.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. ناودان (MON_part2.txt line 73548)\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"ناودان: (امر.) جایی که در آن ناو (ممر سفالین آب) گذارند (رشیدی). ممر آب ... ممر خروج آب پشت بام\\\" — -dān taken as the place/container suffix.\"},\n      {\"src\": \"BQT\", \"where\": \"Mo'in's footnote s.v. ناو, Borhan vol.4 (BQT_v4_pages.txt pdf p.194, line 7734)\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"پارسی باستان nāviyā- (جهاز)، اوستا nāvāza- (کشتی‌ران)، هندی باستان nāv- ... کردی nāw (قنات، ناودان، راه آب) ... رک: ناودان\\\" — Mo'in cross-refers ناودان to ناو 'boat/channel'.\"},\n      {\"src\": \"ARY\", \"where\": \"grep ناودان in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no entry found.\"}\n    ]\n   },\n\n   {\n    \"id\": 3,\n    \"lang\": \"Greek\",\n    \"words\": \"Dânao\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"Greek had no river name *Dánao- for the Danube. The classical Greek names of the river are Ἴστρος (Istros, Herodotus, for the lower course) and, from the Roman period, Δανούβιος / Δανούιος, itself taken over from Latin. 'Dânao' is Nourai's rendering of Pokorny's \\\"gr. VN Δαναοί\\\" — the Homeric name of the Danaans, i.e. the Greeks — which Pokorny (following Kretschmer, Glotta 24) tentatively links to the Scythian tribal name Dānavō 'river-dwellers' and to Egyptian Danuna: \\\"skyth. Nomadenvolk, auch in Griechenland, daher (?) gr. VN Δαναοί\\\". That is an ethnonym, flagged as uncertain by Pokorny himself, and not a name of the Danube. The river name in fact reached the West through Celtic, not Greek: Latin Dānuvius (Caesar, BG 6.25) < Proto-Celtic *Dānowyos, an extended form of *Dānu (cf. Welsh river Donwy, the several English rivers Don). Nourai's attached NOTE — that the word entered Europe from the Scythians in the 7th c. BCE or via Iranian immigrants in Greece — is right about the ultimate Iranian source (this is the standard account) but wrong in making Greek the transmitting language.\",\n    \"derivation_fa\": \"در یونانی هیچ‌گاه نام رود دانوب Dánao- نبوده است؛ یونانیان این رود را Ἴστρος (ایستروس) و در دوران رومی Δανούβιος (وام‌گرفته از لاتین) می‌خواندند. آنچه نورایی «Dânao» نوشته، همان Δαναοί پوکورنی، یعنی نام قومی یونانیان در اشعار هومر، است که پوکورنی با تردید آن را به نام قوم سکایی Dānavō پیوند می‌دهد. نام رود از راه سلتی *Dānowyos به لاتین Dānuvius و از آنجا به زبان‌های اروپایی راه یافته، نه از راه یونانی. یادداشت خود نورایی دربارهٔ خاستگاه سکایی/ایرانی نام درست است، ولی واسطهٔ یونانی نادرست است. (صورت چاپی کتاب هم دقیقاً «Dânao : Danube» است؛ پس خطا از کتاب است نه از خوانش اسکن.)\",\n    \"sources\": [W_DAN, E_DAN, W_PIE],\n    \"ref_check\": [\n      {\"ref\": \"POK:175\", \"status\": \"contradicts\",\n       \"note\": \"POK_01.txt leaf 185-186: \\\"skyth. Nomadenvolk, auch in Griechenland, daher (?) gr. VN Δαναοί, ägypt. Danuna\\\" — a people-name, marked doubtful; and separately \\\"Hierher auch kelt. Dānuvius 'Donau'\\\". Pokorny nowhere makes Δαναοί a name of the river.\"},\n      {\"ref\": \"IRN:123\", \"status\": \"partial\",\n       \"note\": \"Farahvashi (pdf p.134) derives Donau/Dunav/Duna directly from Av. dānu + OP danuva and adds \\\"دانوب بمعنی آب جاری است\\\" — an Iranian etymology, but no Greek intermediary anywhere in his account.\"},\n      {\"ref\": \"MON5:772\", \"status\": \"not_checked\",\n       \"note\": \"Mo'in vol. 5 (a'lam) is not available locally or online (refs_online.json: only the 2-vol lexicon abridgement was obtainable; vajehyab carries no page numbers and no a'lam volumes).\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein p.399 s.v. Danaüs (KLN_1966.txt line 10300)\", \"stance\": \"partial\",\n       \"note\": \"\\\"According to Kretschmer, Glotta 24, 15 ff., the Danaans are identical with the men of Tanaus, king of the Scythians ... Kretschmer also assumes that there is a relationship between Tanaus and the river names Tanais and L. Danubius (whence F. and E. Danube), and Dānu-, name of an Indo-Iranian people.\\\" Klein records the connection but as Kretschmer's hypothesis about an ethnonym; his own preference is a Hebrew-Phoenician Dan.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 853 s.v. dhen- (WLD_Bd1_pages.txt line 79864)\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"Dānuvius 'Donau' kelt. Entw. aus *dhonu-? Vgl. vielmehr oben S. 763\\\" — Walde-Pokorny too route the river name through Celtic.\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.175-176\", \"stance\": \"contradicts\", \"note\": \"see ref_check; Δαναοί = Volksname, Dānuvius = Celtic.\"}\n    ]\n   },\n\n   {\n    \"id\": 4,\n    \"lang\": \"French\",\n    \"words\": \"Danube\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"French Danube is genuine and is indeed the immediate source of the English name, but its parent is Latin, not Greek. Latin took Dānuvius from Celtic *Dānowyos in the late Republic (Caesar, BG 6.25 'Danuvius'); Late Latin/Medieval Latin levelled it to Dānubius, whence Old French Danube, attested from the middle of the 12th century, with regular loss of the Latin case ending and -ūvi- > -ub-. Nourai's own French box carries no reference, and the arrow drawn into it from the Greek box is the part that fails (see node 3); the form and the language label are right.\",\n    \"derivation_fa\": \"صورت فرانسوی Danube درست است و همین صورت سرچشمهٔ مستقیم واژهٔ انگلیسی است؛ اما نیای آن لاتین Dānuvius است (که رومیان از سلتی *Dānowyos وام گرفتند؛ نخستین گواهی در کتاب کایوس یولیوس سزار)، نه یونانی. در لاتین پسین Dānubius شد و از میانهٔ سدهٔ دوازدهم در فرانسوی کهن به صورت Danube دیده می‌شود. پس این حلقه با احتیاط پذیرفتنی است: واژه درست است و خطا در پیکانی است که از جعبهٔ یونانی به آن کشیده شده است.\",\n    \"sources\": [W_DAN, E_DAN],\n    \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"Nourai gives no reference on the French box; checked instead against Wiktionary (Middle French Danube < Latin Dānubius) and Etymonline (\\\"from Latin Danuvius (Late Latin Danubius), from Celtic *danu(w)-yo-\\\").\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein p.399 s.v. Danaüs\", \"stance\": \"supports\",\n       \"note\": \"\\\"L. Danubius (whence F. and E. Danube)\\\" — Klein routes French and English through Latin.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, grep 'Danube'\", \"stance\": \"silent\",\n       \"note\": \"no hit; Devic covers only French words of Arabic/Persian/Turkish origin, so the Danube falls outside his scope. Same for PHN and LAM.\"}\n    ]\n   },\n\n   {\n    \"id\": 5,\n    \"lang\": \"Persian\",\n    \"words\": \"Dânūb «دانوب»\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Modern Persian دانوب Dānūb is a recent geographical loan of the Western name, taken over with the -b of the Latin/French form rather than the -u of German Donau or the -j of Russian Dunaĭ; French was the usual channel for European geography in 19th-20th c. Persian (as it was for the whole اعلام apparatus of Mo'in's vols. 5-6), so Nourai's French > Persian arrow is the likeliest route, but Arabic الدانوب al-Dānūb and Ottoman Turkish could equally have carried the same shape, and the citation that would settle it (Mo'in vol.5 p.516) is not available. Marked plausible for that reason, not because anything in the form is wrong.\",\n    \"derivation_fa\": \"«دانوب» در فارسی نو وام‌واژه‌ای جغرافیایی و نو‌آمد است. صورت آن با «ب» پایانی به فرانسوی Danube و لاتین Dānubius می‌ماند و نه به آلمانی Donau یا روسی Dunaĭ؛ و از آنجا که اصطلاحات جغرافیایی اروپایی در سدهٔ سیزدهم و چهاردهم هجری بیشتر از راه فرانسه وارد فارسی شده‌اند، دیدگاه نورایی محتمل است؛ اما امکان میانجیگری عربی (الدانوب) یا ترکی عثمانی نیز هست و ارجاع نورایی (معین، جلد ۵، ص ۵۱۶) در دسترس نبود. پس با احتیاط پذیرفتنی است.\",\n    \"sources\": [W_DAN],\n    \"ref_check\": [\n      {\"ref\": \"MON5:516\", \"status\": \"not_checked\",\n       \"note\": \"Mo'in vol. 5 (اعلام) is not on disk and not online: refs_online.json records that only a 2-vol lexicon abridgement (MON_part1/2.txt) could be obtained, and grep 'دانوب' finds nothing in it; vajehyab/abadis carry the lexicon volumes only, without page numbers.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1/2.txt (2-vol abridgement), grep دانوب\", \"stance\": \"silent\",\n       \"note\": \"no hit — the abridgement drops the proper-name volumes, which is exactly where Nourai's citation lies.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt line 655\", \"stance\": \"partial\",\n       \"note\": \"Aryanpur mentions \\\"کرانه‌های رود دانوب\\\" in his historical introduction, confirming دانوب as the current Persian form, but gives no etymology of the Persian word.\"}\n    ]\n   },\n\n   {\n    \"id\": 6,\n    \"lang\": \"English\",\n    \"words\": \"Danube\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"English Danube is a borrowing of Middle French Danube (Wiktionary; Etymonline \\\"from Latin Danuvius (Late Latin Danubius)\\\"), i.e. Latin Dānuvius/Dānubius > Old-Middle French Danube > English, which is precisely the chain Nourai draws once the spurious Greek station is removed. His own NOTE — \\\"AHD derives this through Latin 'Dânuvius'\\\" — is not a rival account but the same chain stated one step deeper, and it is the correct one; Klein (p.399) likewise writes \\\"L. Danubius (whence F. and E. Danube)\\\".\",\n    \"derivation_fa\": \"واژهٔ انگلیسی Danube وام‌گرفته از فرانسوی میانه Danube است که خود از لاتین Dānuvius/Dānubius می‌آید؛ یعنی دقیقاً همان زنجیره‌ای که نورایی کشیده است اگر حلقهٔ یونانی را برداریم. یادداشت خود او که «AHD آن را از راه لاتین Dānuvius می‌گیرد» رقیب این رای نیست بلکه همان زنجیره در لایهٔ عمیق‌تر است و درست است. ادعای نورایی دربارهٔ این گره درست است.\",\n    \"sources\": [W_DAN, E_DAN],\n    \"ref_check\": [\n      {\"ref\": \"FSD:652\", \"status\": \"partial\",\n       \"note\": \"Funk & Wagnalls vol. I p.652 (FSD_vol1.txt line 86476, between the page markers '652' at line 86425 and '654' at 86691): \\\"Danube ... (G. Do'nau ...) A river of Europe, flowing 2,000 m. from Baden, through Germany, Austria, Hungary, Jugoslavia, Bulgaria, and Roumania to the Black Sea.\\\" The page and headword are exactly as cited, but it is a gazetteer entry with no etymology, so it cannot support the French arrow.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein p.399 s.v. Danaüs\", \"stance\": \"supports\",\n       \"note\": \"\\\"L. Danubius (whence F. and E. Danube)\\\"; Klein has no separate 'Danube' headword (grep 'Danube' in KLN_1966.txt gives only Danaüs, delta and Rhaetia).\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, grep 'Danube'\", \"stance\": \"silent\", \"note\": \"no entry — Skeat's Concise omits proper names.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. Danubian (WEB_vol1.txt line 49223)\", \"stance\": \"silent\",\n       \"note\": \"only the adjective \\\"Danubian ... of the Danube, a river in ... Europe\\\", no etymology.\"}\n    ]\n   }\n  ]\n },\n\n # ------------------------------------------------------------------ entry 9\n {\n  \"entry\": 9,\n  \"root\": \"Daqal\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Proto-West-Semitic *daqal- 'date palm'\",\n  \"note\": \"The Semitic root box is sound: Hebrew דֶקֶל deqel, Aramaic דִקְלָא diqlā, Syriac deqlā, Arabic دَقَل daqal, with Mehri and Soqotri cognates, all 'date palm'; Klein p.403 s.v. date lists precisely this set, and adds the Hebrew place-name Diqlāh 'a region in Arabia, rich in date palms' (Gen. 10:27, 1 Chron. 1:21). Nourai's gloss is a shade off: the Semitic word denotes the palm TREE (and in Arabic specifically a poor variety of it), the fruit being named from the tree. Nourai attaches no reference to the root box itself; the supporting citation (KLN:403) sits on the Arabic and Greek nodes.\",\n  \"note_fa\": \"ریشهٔ سامی *daqal- به معنای «درخت خرما» پذیرفته است و در عبری deqel، آرامی diqlā، سریانی deqlā و عربی دَقَل دیده می‌شود؛ کلاین (ص ۴۰۳) همین مجموعه را می‌آورد. تنها نکته آنکه معنای نخستین این ریشه «درخت خرما» است نه «میوهٔ خرما»، و نام میوه از نام درخت گرفته شده است. نورایی برای خود جعبهٔ ریشه مأخذی نیاورده است.\",\n  \"sources\": [W_DQL, W_DAK],\n  \"ref_check\": [\n    {\"ref\": \"(none cited on the root box)\", \"status\": \"not_checked\",\n     \"note\": \"Nourai gives refs=None for the Semitic root; the claim was checked instead against KLN:403 (cited on the nodes) and Wiktionary's Proto-West-Semitic *daqal-.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein p.403 s.v. date 'fruit of the palm tree' (KLN_1966.txt line 10373; page markers '403' at line 10344, '404' at 10389)\", \"stance\": \"supports\",\n     \"note\": \"\\\"Cp. Heb. deqel, Aram. diqlā, Syr. deqlā, Arab. dáqal, 'date palm', and Heb. Diqlāh, name of a region in Arabia, rich in date palms.\\\"\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 465 (LKT.txt line ~1219)\", \"stance\": \"supports\",\n     \"note\": \"\\\"465. Ar. daqal: 'Schlechte Dattelsorte' [syr. deklā, aram. diqla BrLexSyr 164a]\\\".\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, grep daqal/diql\", \"stance\": \"silent\", \"note\": \"no entry — the word is not a Qur'anic loan.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, grep دقل\", \"stance\": \"silent\",\n     \"note\": \"no headword دقل (the one hit in AFM_pages.txt line 1882 is inside an unrelated article); consistent with the word being native Semitic, not a Persian arabicism.\"}\n  ],\n  \"nodes\": [\n\n   {\n    \"id\": 1,\n    \"lang\": \"Arabic\",\n    \"words\": \"daqal\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Arabic دَقَل daqal is the ordinary Arabic continuation of Proto-West-Semitic *daqal-: classically 'a poor kind of date palm and its fruit' (dates that are hard, small, or with little flesh round the stone) — exactly Nourai's 'inferior date palm'; in modern usage the value judgement has reversed and daqla(t) an-nūr is a prized variety. The homophonous nautical daqal 'mast, topmast' is a separate semantic loan from Aramaic diqlā (the palm trunk as ship's mast). No sound change is involved between the Semitic root and the Arabic word: the triliteral d-q-l is inherited straight.\",\n    \"derivation_fa\": \"عربی دَقَل دنبالهٔ مستقیم ریشهٔ سامی غربی *daqal- است و در عربی کلاسیک به معنای «نخل پست و خرمای نامرغوب» است؛ هیچ دگرگونی آوایی در میان نیست و سه‌حرفی د‌ق‌ل عیناً به ارث رسیده است. معنای دیگر آن ایعنی «دکل کشتی»ې وام‌گیری معنایی از آرامی diqlā است. ادعای نورایی درست است.\",\n    \"sources\": [W_DQL],\n    \"ref_check\": [\n      {\"ref\": \"KLN:403\", \"status\": \"supports\",\n       \"note\": \"Klein p.403 s.v. date: \\\"Arab. dáqal, 'date palm'\\\" listed beside Heb. deqel and Aram. diqlā.\"},\n      {\"ref\": \"SAP:471\", \"status\": \"not_checked\",\n       \"note\": \"Sayyah's Persian translation of al-Munjid is a purchase-only ebook (refs_online.json: fidibo, no free copy); could not be consulted.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.403 s.v. date (fruit)\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 465\", \"stance\": \"supports\",\n       \"note\": \"\\\"Ar. daqal: 'Schlechte Dattelsorte'\\\" — the same 'inferior date' sense Nourai gives.\"},\n      {\"src\": \"FVQ\", \"where\": \"grep daqal/dakal in FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"no hit.\"}\n    ]\n   },\n\n   {\n    \"id\": 2,\n    \"lang\": \"Persian\",\n    \"words\": \"daqal «دقل»\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"NP دقل daqal is a straightforward Arabic loan into Persian, taken over without phonetic change (the q of ق kept, no vowel adjustment) and with the Arabic sense intact: Mo'in's entry reads \\\"دقل: [ع.] (گیا.) خرمای بد و پست. خرما\\\" — marked [ع.] 'Arabic', botanical, 'a bad, inferior date; date'. Nourai's gloss 'date' is thus a simplification of 'inferior date'; the direction of borrowing (Arabic > Persian, not a Persian word arabicised) is right, and no Persian dictionary claims it for the native stock — Addi Shir, who collects Persian words in Arabic, has no دقل.\",\n    \"derivation_fa\": \"«دقل» در فارسی وام‌واژه‌ای عربی است که بدون دگرگونی آوایی وارد شده است؛ معین آن را با نشانهٔ [ع.] می‌آورد: «دقل: [ع.] (گیا.) خرمای بد و پست». پس جهت وام‌گیری (عربی ← فارسی) درست است و این واژه معرّب نیست؛ ادعای نورایی درست است، فقط معنای «خرمای پست» را به «خرما» ساده کرده است.\",\n    \"sources\": [W_DQL],\n    \"ref_check\": [\n      {\"ref\": \"MON:1543\", \"status\": \"supports\",\n       \"note\": \"Mo'in's entry, found in the 2-vol abridgement (MON_part1.txt line 62153): \\\"دقل: [ع.] (گیا.) خرمای بد و پست. خرما.\\\" — the wording matches Nourai's node exactly; the page number 1543 belongs to the 6-vol edition and cannot be checked against the abridgement, which has no pagination.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt line 62153 s.v. دقل\", \"stance\": \"supports\", \"note\": \"see ref_check; the [ع.] tag marks it an Arabic loan.\"},\n      {\"src\": \"BQT\", \"where\": \"grep دقل in BQT_v1/v2/v3/v4_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"no headword found — Borhan-e Qate' does not treat this Arabic word.\"},\n      {\"src\": \"ARY\", \"where\": \"grep دقل in ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"no entry — Aryanpur covers only the Indo-European stock of Persian, so an Arabic loan is correctly absent.\"}\n    ]\n   },\n\n   {\n    \"id\": 3,\n    \"lang\": \"Greek\",\n    \"words\": \"daktulus\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Greek δάκτυλος means 'finger' and, from Theophrastus and Hellenistic writers on, also 'date'. Klein (p.403), Lokotsch (no.465) and Skeat all derive the 'date' word from the Semitic *daqal/diqlā, reshaped to look like the native word: Klein, \\\"The form of Gk. δάκτυλος, 'date', was influenced by a folk-etymological association with δάκτυλος, 'finger', suggested by the fingerlike shape of the date\\\"; Lokotsch, \\\"hieraus mit volksetymologischer Umgestaltung gr. δάκτυλος\\\". That remodelling is what makes the phonetics possible (Semitic q > Greek k, insertion of -t- and of the -ulos ending on the model of the body-part noun). But it is not the consensus: Wiktionary, following Beekes, calls δάκτυλος 'finger' itself Pre-Greek and admits Semitic influence only for the fruit sense, while AHD and Webster keep the older explanation that the date is simply named after the finger, with no Semitic input at all. So Nourai's arrow is a respectable minority position, hence 'plausible' rather than 'confirmed'. Note also that the borrowing, if real, is a loan of the Semitic word into Greek (both boxes hang directly from the root in Nourai's chart), not a derivation of Greek from Arabic daqal, which is far too late.\",\n    \"derivation_fa\": \"یونانی δάκτυλος نخست به معنای «انگشت» است و از دوران تئوفراستوس به بعد به معنای «خرما» نیز به‌کار رفته است. کلاین، لوکوچ و اسکیت معنای «خرما» را وام‌واژه‌ای سامی (*daqal / diqlā) می‌دانند که بر اثر ریشه‌شناسی عامیانه به قالب واژهٔ «انگشت» درآمده است؛ اما بیکس و ویکی‌واژه خود واژهٔ یونانی را پیشایونانی می‌شمارند و AHD و وبستر نام میوه را فقط استعاره از شکل انگشت می‌دانند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n    \"sources\": [W_DAK, AHD_D],\n    \"ref_check\": [\n      {\"ref\": \"KLN:403\", \"status\": \"supports\",\n       \"note\": \"Klein p.403 s.v. date: \\\"fr. L. dactylus, fr. Gk. δάκτυλος, 'date', which is of Sem. origin. Cp. Heb. deqel, Aram. diqlā, Syr. deqlā, Arab. dáqal, 'date palm' ... The form of Gk. δάκτυλος, 'date', was influenced by a folk-etymological association with δάκτυλος, 'finger'.\\\"\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. date (2) 'fruit of the palm' (SKT.txt line 4637, p.~105-106)\", \"stance\": \"supports\",\n       \"note\": \"\\\"Gk. δάκτυλος, a date. Prob. not allied to δάκτυλος above [= finger], but of Semitic origin.\\\"\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 465\", \"stance\": \"supports\",\n       \"note\": \"\\\"hieraus mit volksetymologischer Umgestaltung gr. δάκτυλος\\\".\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's 2nd ed., s.v. date (fruit) (WEB_vol1.txt line 49488)\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"L. dactylus; Gr. daktylos, a date, lit., a finger, so named from its shape\\\" — no Semitic source.\"},\n      {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. date²\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"from Latin dactylus, from Greek daktulos, finger, date (from its shape)\\\" — the metaphor, not a loan.\"}\n    ]\n   },\n\n   {\n    \"id\": 4,\n    \"lang\": \"Latin\",\n    \"words\": \"dactylus\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Latin dactylus is a straight borrowing of Greek δάκτυλος, taken over with the Greek stem and the second-declension ending, and it carries the 'date' sense in Latin technical prose (Pliny, NH 13, uses dactyli of the long thin dates). Ernout-Meillet: \\\"dactylus, -i n.: emprunt au gr. δάκτυλος\\\"; Klein and Skeat give the same step (Skeat: \\\"L. dactylum, acc. of dactylus\\\"). This is an ordinary learned Greek-into-Latin loan, with no sound change beyond the substitution of Latin y/u for Greek υ.\",\n    \"derivation_fa\": \"لاتین dactylus وام‌گیری مستقیم از یونانی δάκτυλος است که با پایانهٔ صرفی لاتین درآمده و در متون فنی (پلینی، تاریخ طبیعی دفتر ۱۳) به معنای خرما به‌کار رفته است؛ ارنو‌مییه می‌نویسد: «emprunt au gr. δάκτυλος». ادعای نورایی درست است.\",\n    \"sources\": [AHD_D, W_DAK],\n    \"ref_check\": [\n      {\"ref\": \"AHD:337\", \"status\": \"partial\",\n       \"note\": \"Page 337 of the 1975/76 AHD New College edition is not open online (refs_online.json: the 1970s AHD scans are lending-only). The current AHD text for date² does give \\\"from Latin dactylus, from Greek daktulos\\\", which is the step Nourai cites it for; but AHD adds \\\"finger, date (from its shape)\\\", i.e. it does not endorse the Semitic origin behind the Greek node.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. dactylus (LAT.txt line 15707)\", \"stance\": \"supports\",\n       \"note\": \"\\\"dactylus, -i n.: emprunt au gr. δάκτυλος\\\".\"},\n      {\"src\": \"KLN\", \"where\": \"Klein p.403 s.v. date (fruit)\", \"stance\": \"supports\", \"note\": \"\\\"fr. L. dactylus, fr. Gk. δάκτυλος, 'date'\\\".\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. date (2)\", \"stance\": \"supports\", \"note\": \"\\\"L. dactylum, acc. of dactylus\\\".\"}\n    ]\n   },\n\n   {\n    \"id\": 5,\n    \"lang\": \"French\",\n    \"words\": \"datte\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"French datte 'date' continues Latin dactylus, but by the southern route rather than directly: Klein p.403 has \\\"OF. date (F. datte), fr. OProvenç. datil (or fr. It. dattero), fr. L. dactylus\\\", and Lokotsch no.465 lists \\\"it. dattero, sp. dátil, frz. datte\\\" together as the Romance continuations of Medieval Latin dactylus. The medieval French form is date (13th c., the form English borrowed); the modern spelling datte with -tt- and the feminine -e is later, and served to keep the fruit apart from date 'point of time' (< ML data 'given'). Nourai's arrow Latin > French is therefore right in substance; the trade route through Provence/Italy is the detail his chart omits.\",\n    \"derivation_fa\": \"فرانسوی datte «خرما» دنبالهٔ لاتین dactylus است، اما نه به‌طور مستقیم: کلاین آن را از راه پروانسالی کهن datil یا ایتالیایی dattero می‌داند. صورت فرانسوی کهن date بوده و نوشتن آن با دو «t» در دوران جدیدتر و برای جدایی از date «تاریخ» رواج یافته است. ادعای نورایی درست است.\",\n    \"sources\": [AHD_D],\n    \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"no reference on the French box; checked against KLN:403, Skeat and Lokotsch 465 instead.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.403 s.v. date (fruit)\", \"stance\": \"partial\",\n       \"note\": \"\\\"OF. date (F. datte), fr. OProvenç. datil (or fr. It. dattero), fr. L. dactylus\\\" — Latin reaches French via Provence/Italy, not directly.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 465\", \"stance\": \"supports\",\n       \"note\": \"\\\"hieraus wohl über mlat. dactylus die romanischen Formen it. dattero, sp. dátil, frz. datte\\\".\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, grep 'datte'\", \"stance\": \"silent\",\n       \"note\": \"datte occurs only inside other articles (foutah, jubis, tamarin); Devic has no article on datte itself, since he treats it as Greek-Latin rather than an orientalism.\"}\n    ]\n   },\n\n   {\n    \"id\": 6,\n    \"lang\": \"English\",\n    \"words\": \"date 1\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"English date 'the fruit' is Middle English date, borrowed from Old French date (Klein: \\\"OF. date (F. datte)\\\"; Skeat: \\\"M.F. date. — O.F. date (F. datte)\\\"; Lokotsch: \\\"engl. date [aus afrz. date]\\\"). Strictly the source is the Old French form date, not the modern French datte, which is why English kept a single -t-; Nourai's 'French' box is right as long as it is read as Old French. The homonymy with date 'point of time' (Klein p.403, from Medieval Latin data (littera) 'given (letter)', from dare) is purely accidental — hence Nourai's numbering 'date 1'.\",\n    \"derivation_fa\": \"انگلیسی date «خرما» از فرانسوی کهن date وام گرفته شده (نه از صورت امروزی datte)، و به همین سبب در انگلیسی یک «t» دارد؛ کلاین، اسکیت و لوکوچ هر سه همین را می‌گویند. همآوایی آن با date «تاریخ» (از لاتین میانه data littera) تصادفی است و نورایی به درستی آن را «date 1» شماره زده است. ادعای نورایی درست است.\",\n    \"sources\": [AHD_D],\n    \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"no reference on the English box; checked against KLN:403, Skeat s.v. date (2), Lokotsch 465 and the AHD online entry.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.403 s.v. date (fruit) and date (point of time)\", \"stance\": \"supports\",\n       \"note\": \"\\\"date, n., fruit of the palm tree. — OF. date (F. datte)\\\"; the separate entry \\\"date, n., a given point of time. — ME., fr. OF. (= F.) date, fr. ML. data (scil. littera)\\\" confirms the two are unrelated.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. date (2) (SKT.txt line 4637)\", \"stance\": \"supports\",\n       \"note\": \"\\\"date (2), fruit of the palm. (F.-L.-Gk.) M.F. date. — O.F. date (F. datte), a date.\\\"\"},\n      {\"src\": \"LKT\", \"where\": \"no. 465\", \"stance\": \"supports\", \"note\": \"\\\"engl. date [aus afrz. date]\\\".\"}\n    ]\n   }\n  ]\n }\n ]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-109.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk109.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-109.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 109"
}
```


### [2026-09-05T17:43:24.399Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 12/12
node verdicts: {'disputed': 3, 'plausible': 3, 'confirmed': 6}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 4, 'supports': 5, 'contradicts': 1, 'not_checked': 6}
books consulted: {'supports': 15, 'partial': 4, 'contradicts': 8, 'silent': 9} | by book: {'KLN': 7, 'SKT': 4, 'LKT': 4, 'MON': 3, 'ARY': 3, 'HRN': 2, 'BQT': 2, 'DEV': 2, 'WEB': 2, 'BRT': 1, 'KNT': 1, 'WLD': 1, 'POK': 1, 'FVQ': 1, 'AHD': 1, 'LAT': 1}
```


## [2026-09-05T17:43:32.858Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'PY'\nimport io\np='data/verification/page-109.json'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace('معنای دیگر آن ایعنی «دکل کشتی»ې وام‌گیری','معنای دیگر آن، یعنی «دکل کشتی»، وام‌گیری')\ns=s.replace('\"words\": \"Dânūb «دانوب»\"','\"words\": \"Dânŭb «دانوب»\"')\nio.open(p,'w',encoding='utf-8').write(s)\nPY\ngrep -c \"ې\" data/verification/page-109.json; python3 -m json.tool data/verification/page-109.json >/dev/null && echo OK && python3 tools/verify_check.py 109 | tail -6"
}
```


### [2026-09-05T17:43:34.863Z] TOOL RESULT

```
0
OK
nodes verified: 12/12
node verdicts: {'disputed': 3, 'plausible': 3, 'confirmed': 6}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 4, 'supports': 5, 'contradicts': 1, 'not_checked': 6}
books consulted: {'supports': 15, 'partial': 4, 'contradicts': 8, 'silent': 9} | by book: {'KLN': 7, 'SKT': 4, 'LKT': 4, 'MON': 3, 'ARY': 3, 'HRN': 2, 'BQT': 2, 'DEV': 2, 'WEB': 2, 'BRT': 1, 'KNT': 1, 'WLD': 1, 'POK': 1, 'FVQ': 1, 'AHD': 1, 'LAT': 1}
```


## [2026-09-05T17:43:50.849Z] AGENT

Page 109 (book p. 79) verified. `verify_check.py 109`: 12/12 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed. Nodes: 6 confirmed, 3 plausible, 3 disputed. Ref checks: 5 supports, 4 partial, 1 contradicts, 6 not_checked. 9 redirect entries skipped.

**Disputed**
- *Dâ 2/Dânu* #1 (Avestan/OP `dânu; nâv-dân; danuva; Dânavo`) — Av. dānu- (Bartholomae col. ~735) and OP danuvatiy (Kent, DZc 9) are genuine, but nāv-dān is New Persian, not Old Iranian, and Pokorny's *Dānavō* is a Turanian **people**-name ('Flußanwohner', Yt 13.37-38), not the Danube.
- *Dâ 2/Dânu* #2 (Persian `ناودان`) — word is real, but -dān is the container/place suffix (Horn no. 1024; Mo'in "جایی که در آن ناو … گذارند"; Wiktionary < MP dāštan), not dānu 'river'. Nourai follows Farahvashi (Iranvij), an isolated view.
- *Dâ 2/Dânu* #3 (Greek `Dânao`) — Greek never called the Danube that; this is Pokorny's Δαναοί (the Danaans, an ethnonym, flagged "?"). The river name went Celtic *Dānowyos > Lat. Dānuvius > OF Danube; no Greek stage.

**Plausible**: French Danube (parent is Latin, not Greek); Persian دانوب (French route likely but MON5:516 unavailable); Greek daktulos < Semitic (Klein/Skeat/Lokotsch support; Beekes/AHD/Webster prefer 'finger' metaphor).

**No extraction errors.** The printed page (rendered, copied to `data/verification/sources/refs/ocr/BOOK/109.png`) matches the JSON exactly, including "Dânao : Danube" — that error is Nourai's, not the scan's.

**Notes on Nourai's page cites**: KLN:403 and FSD:652 are exactly right (verified against page markers). IRN:123 lands on pp. 133-134 in the 6th printing on disk (10-page offset from the 1368 edition Nourai used) — the content matches word for word. Not checkable: MON5:772, MON5:516 (Mo'in vols. 5-6 not obtainable), SAP:471 (purchase-only), AHD:337 (1975 AHD lending-only; substituted the current AHD text).

7 web pages archived via `fetch_source.py`.
