# Verification process log — verify-page-212


## [2026-09-06T14:52:00.421Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 212 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-212.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-212.json. Write /home/sfmqrb/git/rishe/data/verification/page-212.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 212` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:52:02.490Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:52:03.200Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:52:03.220Z] TOOL RESULT

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


## [2026-09-06T14:52:03.455Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-212.txt"
}
```


### [2026-09-06T14:52:03.466Z] TOOL RESULT

```
1	=== PDF page 212 (book page 182) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwhedh : to ask, wish, want  (refs POK:488)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:488; WLD:673; SYN:1471; HRN:470 | ža 3, gad : to want, wish, beg ; žaidhyemi, žadiyâmiy : I wish ; hu-jasta : well wished, blessed ☞Su 1 ; a-žasta
5	  #2 (parent #1) [Persian] refs=BQT:717,1453,1776; HRN:470 | gedâ «گدا» : beggar ; xojasteh «خجسته» : blessed | extra: فرخجسته
6	    #3 (parent #2) [Arabic] refs=FVF:565 | kadâ : beggar
7	      #4 (parent #3) [Persian] refs=FVF:565; FVA:349 | takaddî «تَکَدّی» : begging | extra: مُتَکَدّی
8	--- entry 1 ---
9	ROOT [Indo-European] Gwhen 1 : to swell, fill  (refs POK:491)  PART 1
10	#1 (parent #0) [Avestan / Old Persian] refs=ZMA:49-51 | šan, šyangh : house, household | NOTE: Cognate with "kan 1, xan, gan 1: to dig out an mound up (a shelter)"
11	  #2 (parent #1) [Pahlavi] refs=BQT:46; ZMA:49-51 | šân : house, shelter ; â-šân-ak : house ; hu-šangh : with good household ☞Su 1
12	    #3 (parent #2) [Persian] refs=ZMA:49-50; BQT:46,2395 | šan «شَن» : house ; šandaf «شَندَف» : house tambourine ☞Deru 1 ; Hŭžšang «هوشنگ» : owner of good household ☞Su 1 | extra: ـ شان ، ـ شانه ، بغ شن ، شندیز
13	گلشن ، کاشان ، کاشانه ، آشیان ، آشیانه | NOTE: See "Kweye" for another possible root of "âšîyân(eh)".
14	#4 (parent #0) [Sanskrit] refs=PRT:75 | ğanâ : ditch ; xanda : a broken lump of sugar
15	  #5 (parent #4) [Persian] refs=BQT:1544 | qand «قند» : sugar | extra: قنداغ ، قنداب ، قنددان ، قندران
16	    #6 (parent #5) [Arabic] refs=KLN:231 | qandat : sugar candy
17	      #7 (parent #6) [French] refs=None | 
18	        #8 (parent #7) [English] refs=AHD:196 | candy
19	
```


## [2026-09-06T14:52:04.948Z] AGENT

I'll read the source JSON and the reference index.


## [2026-09-06T14:52:06.234Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-212.json",
 "description": "Read page 212 source JSON"
}
```


### [2026-09-06T14:52:06.277Z] TOOL RESULT

```
{
  "pdf_page": 212,
  "book_page": 182,
  "entries": [
    {
      "root": {
        "name": "Gwhedh",
        "lang": "Indo-European",
        "refs": "POK:488",
        "gloss": "to ask, wish, want"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:488; WLD:673; SYN:1471; HRN:470",
          "words": [
            {"translit": "ža 3, gad", "gloss": "to want, wish, beg", "script": null},
            {"translit": "žaidhyemi, žadiyâmiy", "gloss": "I wish", "script": null},
            {"translit": "hu-jasta", "gloss": "well wished, blessed", "script": null, "see": ["Su 1"]},
            {"translit": "a-žasta", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:717,1453,1776; HRN:470",
          "words": [
            {"translit": "gedâ", "gloss": "beggar", "script": "گدا"},
            {"translit": "xojasteh", "gloss": "blessed", "script": "خجسته"}
          ],
          "script_extra": "فرخجسته",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "FVF:565",
          "words": [
            {"translit": "kadâ", "gloss": "beggar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "FVF:565; FVA:349",
          "words": [
            {"translit": "takaddî", "gloss": "begging", "script": "تَکَدّی"}
          ],
          "script_extra": "مُتَکَدّی",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gwhen 1",
        "lang": "Indo-European",
        "refs": "POK:491",
        "gloss": "to swell, fill"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "ZMA:49-51",
          "words": [
            {"translit": "šan, šyangh", "gloss": "house, household", "script": null}
          ],
          "script_extra": null,
          "note": "Cognate with \"kan 1, xan, gan 1: to dig out an mound up (a shelter)\"",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:46; ZMA:49-51",
          "words": [
            {"translit": "šân", "gloss": "house, shelter", "script": null},
            {"translit": "â-šân-ak", "gloss": "house", "script": null},
            {"translit": "hu-šangh", "gloss": "with good household", "script": null, "see": ["Su 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "ZMA:49-50; BQT:46,2395",
          "words": [
            {"translit": "šan", "gloss": "house", "script": "شَن"},
            {"translit": "šandaf", "gloss": "house tambourine", "script": "شَندَف", "see": ["Deru 1"]},
            {"translit": "Hŭžšang", "gloss": "owner of good household", "script": "هوشنگ", "see": ["Su 1"]}
          ],
          "script_extra": "ـ شان ، ـ شانه ، بغ شن ، شندیز\nگلشن ، کاشان ، کاشانه ، آشیان ، آشیانه",
          "note": "See \"Kweye\" for another possible root of \"âšîyân(eh)\".",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "PRT:75",
          "words": [
            {"translit": "ğanâ", "gloss": "ditch", "script": null},
            {"translit": "xanda", "gloss": "a broken lump of sugar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:1544",
          "words": [
            {"translit": "qand", "gloss": "sugar", "script": "قند"}
          ],
          "script_extra": "قنداغ ، قنداب ، قنددان ، قندران",
          "note": null,
          "quote": {"text": "شفا ز گفتهٔ شکر فشان حافظ جو - که حاجتت بعلاج گلاب و قند مباد", "poet": "Hâfez"}
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Arabic",
          "refs": "KLN:231",
          "words": [
            {"translit": "qandat", "gloss": "sugar candy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:196",
          "words": [
            {"translit": "candy", "gloss": null, "script": null}
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


## [2026-09-06T14:52:08.924Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','SYN','HRN','BQT','FVF','FVA','ZMA','PRT','KLN','AHD','MON','PHD','NYB','BRT','KNT','HUB','ARY','IEC','SKT','FSD','WEB','LKT','AFM','PLA','CHEUNG','SOD','FVQ']:\n    v=d.get(k)\n    print(k, '::', json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T14:52:11.673Z] TOOL RESULT

```
POK :: {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD :: {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN :: {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HRN :: {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT :: {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FVF :: {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
FVA :: {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
ZMA :: {"title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995", "kind": "purchase", "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; no open
PRT :: {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (al
KLN :: {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD :: {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON :: {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
PHD :: {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB :: {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT :: {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT :: {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HUB :: {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY :: {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC :: {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SKT :: {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD :: {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB :: {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
LKT :: {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
AFM :: {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA :: {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
CHEUNG :: MISSING
SOD :: {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
FVQ :: {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
```


## [2026-09-06T14:52:37.275Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


## [2026-09-06T14:52:37.287Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -80"
}
```


### [2026-09-06T14:52:37.339Z] TOOL RESULT

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
```


### [2026-09-06T14:52:37.346Z] TOOL RESULT

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


## [2026-09-06T14:52:41.993Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','SYN','HRN','BQT','KLN','AHD','IEC','BRT','KNT','PHD','NYB','ARY','MON','FVQ','AFM','PLA','LKT','SKT','FSD','HUB','PRT','FVF','FVA','ZMA','CHEUNG']:\n    v=d.get(k)\n    if not v: continue\n    print(k,'| page_offset:',v.get('page_offset'),'| local:',v.get('local_file'),'| hint:',(v.get('lookup_hint') or '')[:250])\n    print()\n\""
}
```


### [2026-09-06T14:52:44.634Z] TOOL RESULT

```
POK | page_offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' .

WLD | page_offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 1

SYN | page_offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.

HRN | page_offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

BQT | page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode

KLN | page_offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

AHD | page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are

IEC | page_offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

BRT | page_offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers 

KNT | page_offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.

PHD | page_offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

NYB | page_offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

ARY | page_offset: printed page = pdf page + 1 | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built

MON | page_offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: show

FVQ | page_offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).

AFM | page_offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').

PLA | page_offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG

LKT | page_offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.

SKT | page_offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.

FSD | page_offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.

HUB | page_offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

PRT | page_offset: None | local: None | hint: Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.

FVF | page_offset: None | local: None | hint: Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.

FVA | page_offset: None | local: None | hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.

ZMA | page_offset: None | local: None | hint: Searched archive.org, ketabnak, noorlib, web: not found.
```


## [2026-09-06T14:52:49.449Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"g\\^ᵘhedh\\|guhedh\\|ghedh-\\|jaidyemi\\|ǰaidyemi\\|jadiyamiy\" POK_full.txt | head -30\necho \"=== POK_full block ===\"\ngrep -n \"Root / lemma: g\" POK_full.txt | grep -i \"hedh\\|hen\" | head -20"
}
```


### [2026-09-06T14:52:49.508Z] TOOL RESULT

```
=== POK_full block ===
32864:Root / lemma: ghen6^-{ghon6^-) 
32877:Root / lemma: ghencf- and ghed- 
32926:Root / lemma: ghen- 
34309:Root / lemma: gol-1, lengthened grade gol-, reduktions stem gj- 
35407:Root / lemma: genu-1, gneu- {*ghenu-) 
36663:Root / lemma: ghengh- 
40002:Root / lemma: g''hen-1 
40037:Root / lemma: g''hen-2(a)-
```


## [2026-09-06T14:52:50.719Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# leaf = p - 344\nfor p in (488,491,492):\n    i=p-344\n    print('='*20,'printed',p,'leaf',i)\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-06T14:52:53.531Z] TOOL RESULT

```
434
==================== printed 488 leaf 144
 mit  den  Zähnen'  (daneben  durch  Entgleisung aus  ßQv^o),  eßgv^a :  ßgiTio))  ,beiße',  ßQvydrjv  ,beißend',  ßQV'y(,iög  , Zähne- knirschen', ßgvxsTÖQ  ,kaltes  Fieber'  (,Zähneklappern').
486
b)  air.  hrön  ^Kummer^  cjmr.  brtoyn  ^stechender  Schmerz'  (urkelt. *brügnos);
lit.  grduziu,  grduHi  ,nagen^  sugrüzinü  ^vernichten';
aksl.  gryzq,  grysti  ,nagen'  (in  andern  slav.  Sprachen  auch  von  nagendem Kummer;  hierher  wohl  auch  sloven.  grüze  PI.  f.  ^Krätze^.
Zu  gryzg  wahrscheinlich  russ.  grusth  ^Kummer',  sloven.  grüst  ,EkeP.
WP.  I  697  f.,  Trautmann  100.
j
Ohvi  und  Q^h.
^bctei{o-)  , hinschwinden,  z'ngrunde  gehen^,  auch  trans.  ^vernichten' ; gVidi-ti-s,  g^bdoi-o-  ,Untergang^
Ai.  ksindti,  ksinöti  ( :  gr.  *q)d-LvJ^-(o)j  ksdyati  ,vernichtet,  läßt  vergehen', partiz.  ksitd-h  , erschöpft'  (=  gr.  q)d'LTÖg ;  srdva-h  dksitam  =  gr.  y,Xeog  Ucfd-i- xov  ^unverwüstlicher  Ruhm^),  kslnd-h  ds.,  ksiydte  , schwindet  hin,  nimmt ein  Ende',  ksayd-h  , Abnahme,  Untergang'  (:  gr.  q)'d'örj  f.),  kHti-h  , Ver- drehen, Untergang'  (=  gr.  q)d-L(TLg  und  -?-  lat.  sitisj  vgl.  -tuSt  lat.  sittts)]
prakr.  ajjhitah-  (=  äq)d-LTog)y  jklna-  (=  ai.  kslna-)]
av.  ay^önvamndm  ,sich  nicht  mindernd'  (Kuiper  Nasalpräs.  65^);
gr.  ep.  (pMvoiy  att.  q)d-tvu)  (^cpS-ivfWy  s.  oben)  , vernichte',  meist  intr. ,schwinde  hin,  gehe  zugrunde',  cp^ivv-d-o)  , schwinde  hin,  mache  verschwin- den', Fut.  q)d'hao)  (att.  di7to(pd-taw)j  Aor.  eifdsiaa  (att.  SLTtecpd-Xaa),  icpd-t(.iriv^ qi&ffxsvog  ,vernichten',  Pass.  , zugrunde  gehen',  Partiz.  Perf.  Pass.  q}&LTÖg, (pd-ÖT}  , Schwindsucht',  (pd-laig  ds.  (s.  oben  ) ;  über  vielleicht  alte  Doppel- formen, wie  ipiv€G&aLj  xpiva^siv  , Blüten  oder  Früchte  abfallen  lassen,  ver- lieren', xpLGig'  dnwXeia  Hes.,  u.  dgl.  s.  Schwyzer  Gr.  Gr.  I  326.
Aus  dem  Lat.  wahrscheinlich  situs,  -üs  ,der  modrige  Schmutz  und Schimmel,  körperliche  Unreinlichkeit  und  alles  körperliche  und  geistige  Ver- rosten' und  suis  ,Durst'  (wenn  eigentlich  ,*Hinschwinden,  Verschmachten').
WP.  I  505 f.,  Schwyzer  Gr.  Gr.  I  326,  Benveniste  BSL.  38,  139 ff.
g^hffer-   (oder  besser  g^ider-??)  , 
==================== printed 491 leaf 147
  ,wollen'.
Gr.  d-slü)j  i-&€lo)  (zum  Präfix  s.  W-,  ö-Part.)  ,will,  wünsche',  ablautend (pakiC^ei '  d'eXei  Hes. ;  ijiL^dg)sXog  ,heftig' ;
anord.  gildra  f. ;  gildri  n.  , Falle',  gilja  ,verlocken',  aschwed.  gicel- skaper  , Unzucht';
aksL  zeleti,  ^elatij  iter.  russ.-ksl.  zalati  ,wünschen',  aksl.  zelja  , Wunsch, Sehnsucht'  (auch  ,trauern'  und  ,Trauer'  durch  Anlehnung  an  ^aU  , Schmerz' von  *^"eZ-  ,stechen').
WP.  I  692.
gbuel-  ,sich  krümmen,  von  der  geraden  Richtung  abbiegen  (auch  geistig und  sittlich)  u.  dgl.';  ghuelo-s  ,gekrümmt'.
Ai.  hvdrate  ,biegt  von  der  geraden  Richtung  ab,  macht  krumme  Wege', hvdlati  ,gerät  auf  Abwege,  strauchelt,  irrt',  juhuränd-h  , mißglückend', vihriUa-h  , schadhaft,  krank',  hrunäti  ,geht  irre',  Partiz.  hrutd-y  geneuert hvftd-',  hürchati  ,geht  schief,  gleitet,  schwankt,  fällt';  hvdras-  n.  ,Krüm- mung',  hvard-  m.  , Schlange',  vihrüt-  f.  ,Art  Schlange  oder  Wurm' ;
av.  zbardmna-  ,krumm  gehend',  zharad-a-  n.  ,Fuß  daevischer  Wesen', zharah-  n.  ,Hügel',   zürah-  n.  ,Unrecht,  Trug',   npers.  zur  , falsch;  Lüge';
gr.  q)aXl7tT€L'  uwqaivei  Hes.,  (paXög  , stammelnd,  töricht'  Hes.  und  wahr- scheinlich (pdXoQ  m.  ,hornartiger  Vorsprung  am  Helm',  vermutlich  g)oAxdg, Beiwort  des  Thersites  B.  217,  etwa  , krummbeinig' ;   vielleicht  auch  dTto-
L
490  •
(fcblLog   ,trügerisch'    (ö-stufig),    q)fjlog    ^betrügerisch^,    q)rjXi^T7jg    ;Betrüger',  v? cprjXötJ  (dor.  cpaXöcü)  betrüge';  ^^';
lat.  fallö,  -ere  ^täuschen,  betrügen;  unwirksam  machen;  sich  entziehen-  ^'-^ unbemerkt  bleiben'  (,*krumme  Wege  machen;   ausbiegen';    *ghujnö,  vgl.  - ai.  hrunäti)'j  '4-  -
lit.  nuozvelnüs  ,abschüssig'j  zvalüs  ^geschickt;  flink,  behend'  (,*sich leicht  biegend');  ablaut.  i^vünas  ,schräg,  schief  {*g'hul-),  pa^il-ti,  -au ,sich  neigen',  ir^/^wo^t  , schaukeln,  schwanken';  prazulnas  (*ghul-)  ,schräge, schief,  paMnus  ds. ;  atiülas,  -us  ,schroff,  hart,  unhöflich,  unbarmherzig' u.  dgl. ;
lett.  zveVu,  zveVu,  zvelt  ,wälzen,  fortbewegen,  umwerfen ;  schlagen',  refl. ,sich  schwerfällig  fortbewegen,  sich  wälzen,  umfallen',  zvalstities  ,wanken, schwanken',  zvatns  ,sch wankend';
aksl.  z^l^  ,böse,  schlimm',  skr.  zäo  (f.  zlä)^  russ.  zoi  (f.  zia)  ds. ;
vielleicht  *ghu-el-  aus  einem  gheu-  ,schief'  erweitert;  vgl.  ^ghu-er-  in lit,  ziirU  ,eine  Rankenpflanze
==================== printed 492 leaf 148
,das  Schwanken';  norw.  dial.  gimpa  , wippen, schaukeln',  gamp  m.  ,großer  schwerfälliger  Kerl,  plumpes  Pferd'.
Eine  kürzere  Wzf.  guhem-  vielleicht  in  aisl.  gaman  n.  ,Freude,  Lustig- keit, Wollust',  ahd.  gaman  n.  ds.,  usw.  "       ^
WP.  I  678  f.  ^^
ghuen-    ,tönen',    ghupno-s    ,Ton':    Erweiterung    von    ghau-,     s.   Persson Beitr.  191. kxm.  jain  (ghuon-ii-),  i-St.  , Stimme'  (mit  t- Epenthese) ; alb.  tosk.  Z6  , Stimme',  geg.  zd  (<  *ghuono-s)'j
russ.-ksl.  zvbnjuj  zvhnki  ,klingen,  tönen',  russ.  zvenith,  acech.  zvnieti, öech.  zniti,  altpoln.  tozniec  ds.,  ablaut.  aksl.  zvom  ,Ton',  sl.  zvqn  , Glocke',
491
hnlg'  zv^n^  ,Klang,  Schall',  zvznecb  , Glocke',  skr.  zvono,  russ.  cech.  zvon, poln.  dzwon  , Schall,  Glocke^
Baltoslav.  Wurzelerweiterung  gbueng-:
lit.  zvengiu,  zvengti  ^wiehern',  su-zvihgu,  -zvingti  ,in  Wiehern  ausbrechen^, zvangüs  ,laut,  schallend',  svdngu,  zvangeti  ,rasseln,  klingen,  klirren',  lett. zviegt  , wiehern';
aksl.  zv^go  ,verkünde',  russ.-ksl.  zvjagu  ,singe,  schwatze',  russ.  dial. zvjagü,  zvjach  ,bellen'.
Slav.  Wurzelerweiterung  gbuenk-:
aksl.  zv^kz  m.  ,Klang',  zveknqti  , tönen',  zvecati  , rufen',  skr.  zvek  ,Klang'^ poln.  zwi^k,  diwiek  , Klang,  Schall';  mit  Ablaut  aksl.  zvok^  ,Klang',  russ. zvuk,  cech.  zvuk  ,Ton,  Laut,  Schall';
Slav.  Wurzelerweiterung  gbuent-:
bulg.  zv^ntja  ,schallen,  klingen'.
WP.  I  642,  Trautmann  374.
f.  g^hen-  ,schwellen,  strotzen.  Fülle';  g^hono-s  ,üppig,  reichlich'.
Ai.  a-hand'  , schwellend,  strotzend,  üppig',  ghand-  , dicht,  dick',  m. ,kompakte  Masse';
npers.  ä-gandan  , anfüllen',  äganis  ,voll';
arm.  yogn  ,multum'  (Präp.  i  +  *o-g^hon-  oder  *o-g^hno-,  im  Präfix  o- dem  ar.  ä-  nächststehend) ;
gr.  sid-svi^g  ,reichlich,  in  Fülle',  Hes.,  edd^svsoj  ,gedeihe',  eid-iveia  , Fülle, blühender  Zustand',  dehnstufig  ion.  svdr]vi^g  , reichlich,  in  Fülle',  ion.  att. sid-rivso)  ,gedeihe,  bin  in  Blüte  und  Kraft',  svd-rjvla  f.  ,Fülle';  o-stufig IloKvcpövrrjg  =  noXvKTT^TTjg;  KXsocpövrrjg^  usw.,  red. -stufig  q)aväv '  d^eksiv Hes.,  wohl  eigentlich  ,geil  sein' ;
lit.  ganä  ,genug',  ganeti  ,genügen',  gandeti  ,genug  haben',  lett.  gana ,genug';
aksl.  gonejetb,  goneti  ,genügen',  Denomin.  von  "^gona  =  lit.  ganä]
ob  hierher  gr.  ^cpavog,  lücpvog  n.  ,reichlicher  Vorrat,  Reichtum',  äcpvsiog , begütert'  {cp  un
```


## [2026-09-06T14:53:02.278Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (145,146):\n    print('='*20,'leaf',i)\n    print(pages[i][:3500])\nEOF"
}
```


### [2026-09-06T14:53:04.816Z] TOOL RESULT

```
==================== leaf 145
rinnen,   fließen;   zerrinnen,  verschwinden',
im  ar.  Kaus.  und   im  gr.  zo-Verbum   trans.  , rinnen  lassen,  zerrinnen
lassen',  daher  gr.  , verschwinden  lassen,  vernichten'.
Ai.    k^drati   , fließt,   strömt,   zerrinnt,   verschwindet',    ksara-m   ,Wasser',
ksärayati  ,läßt  fließen',  ksälayati  , wäscht  ab'  (vgl.  Wackernagel  Ai.  Gr.  I
241);  av.  y^araiti  , strömt,  wallt  auf,  yzärayeiti  ,läßt  fließen',  mit  vi-  ,läßt
überfließen';  Weiterbildung  in  a-yzrädayeiti  ,läßt  aufwallen',  vi-yzrädayeiti
;läßt  auseinander,   überwallen' ;    umgestellt  zyar-  in  avi  fra-zyaraiti  ,fließt
herzu
zu-
wahrscheinlich arm.  jur,  Gen.  jroy  ,Wasser'  {^g^hdöro-)] gr;  att.  cpd-slQix)  {*q)d'SQia}',  lesb.  q)&8QQü},  ark.  (pd^iqqoj)),  schwachstufig  dor. (pd-aiQü)   (*q)&aQicü)   ,richte   zugrunde';    dazu    auch   g)d-6iQ  ,Laus'    (ipeigsc (pd-eiQSi  Hes.  ist  Folge  der  spätem  spirantischen  Aussprache  des  ^),  (pd'OQ&
488  f
^Verderben,  Vernichtung'  und  (als  Rest  der  älteren  Bedeut.)  ,Yerniischt oder  Verreibung    der    Farben',    ebenso    av^igj^sigo)    außer    ,zugleich   od« gänzlich   zugrunde    richten'    auch    ,lasse  Farben   ineinanderfließen',   da^ auch    ^verschmelzen,    vermischen    überhaupt',   avi.icpd-siQeadai   ;Zusaminei2 strömen'.
WP.  I  700,  Schwyzer  Gr.  Gr.  I  326,  714,    Benveniste  BSL.  38,  139  £
g^hedh-  , bitten,  begehren'.
Av.  jaiöyemi,  apers.  Jadiyämiy  ,ich  bitte';
gr.  Aor.  d-saaaad'ai  {*gVihedk-s-)  ,anflehen',  Partiz.  -d^satög  in  dnö^eavog ,verwünscht,  verschmäht',  Ttolv-d'sarog  ,sehr  ersehnt',  Pers.-N.  Oeö-S-earog böot.  0LÖ-q)SLarog]  ftö&og  m.,  tto&i^  f.  ,Sehnsucht,  Verlangen',  nod-m  ,er. sehne,  vermisse  schmerzlich,  verlange';
air.  guidiiL  ,bitte'  (=  nod-io}),  Perf.  1.  Sg.  ro-gäd,  s-Konj.  1.  PI.  gessam (usw.);  geiss  f., Verwünschung, Tabu'  {*gViedh-ti-s)]  guide,G ehet^ {*g^hodhia)'^ foigde  ,BetteW  (^uo-gediä) -,  cjmr.  gweddi  , Gebet'  (*uo-godlma) ;
lit.  geddu-ju,  -ti  ,sich  sehnen,  sehnsüchtig  suchen,  verlangen,  wollen', gedü  (und  gedziü),  gedeti  ,sich  sehnen ;  traurig  sein,  trauern' ;  Nasalpräsens pasigendü,  -gedaü,  -gesti  ,sich  sehnen;  etwas  vermissen',  ablaut.  Kausat. gadmti  ,verderben,  stören',  daher  sekundär  der  ö -Vokalismus  (statt  uo) von  gödas  ,Gier,  Habsucht;  Klette',  godits  , ha
==================== leaf 146
bgierig,  geizig',  godziüoi^ godetis  ,begehren,  wonach  dürsten,  wünschen,  begierig  sein';
im  Slav.  mit  durchgeführter  Nasalierung :  aksl.  z^zdq^  ^^dati,  acech.  Mdatil ,begehren,  wonach  dürsten',  z^zdg,  zedeti  ,cupere',  z^^da  , Durst',  poln/ zqdza  ,Begehren,  Gier,  Sehnsucht,  Wunsch';
unsicher  wegen  des  Anlautes  anord.  ged  n.  (*gadia-)   ,Sinn,  Charakter," Verlangen,   Lust',   gedlauss   , charakterlos'   vielleicht  =  ahd.  getilös,  mhd.  | getlös  ,zügellos,  mutwillig';
man  beachte  die  übereinstimmende  Gruppierung  d^eaaaad^ai  ;  Ttod^sw  = ir.  gess-am  (*guhedh-s-o-mos)  :  guidiu  (*g'^liodh-eiö).
WP.  I  673,  Trautmann  84£.,  Endzelin  Lett.  Gr.  577.
(*^Mi2ei-0  g'^hgi-,  g^bgi-d- :  g^hid-  ,hell,  leuchtend';  g^hoi-d-ro-s  ds.
Gr.  (patÖQÖg  ,klar,  hellglänzend,  leuchtend;  heiter,  vergnügt'  (=  lit. giedras),  woneben  cpaidi-  im  cpaidL(j,og  ,glänzend,  stattlich';  q)aLÖg  ,schum- merig,  dämmerig,  bräunlich,  grau'  (Gdf.  *(p(xL-J^ög  oder  -oög)'^  cparAÖg' XafiTtQÖg  Hes. ;
lit.    giedrasj    gaidrüs    ,heiter,    klar'    (davon    giedrä,    gaidrä   f.    ,schönes Wetter'),  lett.  dziedrs  ,azurblau',  ablautend  dzidrums  ,Klarheit';  lit.  gaisas  ■- i^g^hdid-so-s),  gaisa  , Lichtschein  am  Himmel',  lett.  gäiss  m.  ,Luft,  Wetter', gaiss  (*gaisus)   ,klar',   gäisma   f.  ,Licht',   lit.   gaXsras   m.   ,Lichtschein   am
489
Uimmel,    Feuersbrunst;    Zorn^,    gaXzdras    m.    , Lichtschein    am    Himmel'; ■tvohl  auch  apr.  gaylis  ,weiß*. WP.  I  665,  Trautmann  75.
g^beio-  :  g^hl-  , Ader,  Sehne,  Band' ;  gHbi-slo-  ds. Cymr.  gi-au  PL  ,Nerven,  Sehnen';
lit.  gijä  , Faden  im  Aufzug  eines  Gewebes',  lett.  dzija  , Faden,  PL Garn';
aksL  H-ca  , Sehne',  russ.  diaL  Mca  ,Kammgarn',  skr.  zica  ,Faden,  Draht, Schnur,  Saite';  die  bsl7-Formen  könnten  auch  zu  gVin9-  gehören.
g'ihislO'',
Arm.  jil  , Sehne,  Schnur';
lat.  fllum  , Faden';
lit.  gysla  ,Ader,  Sehne,  Blattrippe',  lett.  dztsla^  dztksla  ,Ader'  (die Nasalierung  in  zemait.  ginsla  ist  sekundär),  apr.  pettegislo  , Rückenader' ; aber  aksl.  züa^  russ.  i2?a,  skr.  zila  usw.  ,Ader,  Sehne'  sind  Neubildun- gen zu  zi-ca,  s.  oben.
WP.  I  670,  694,  WH.  I  497  f.,  Trautmann  87,  90.
g^bel-
```


## [2026-09-06T14:53:52.169Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== AHD watkins gwhedh =====\"\ngrep -n -i \"gwhedh\\|g\\*hedh\\|ghedh\" AHD_watkins1985.txt | head -20\necho \"===== AHD watkins gwhen swell =====\"\ngrep -n -i \"gwhen\\|g\\*hen\" AHD_watkins1985.txt | head -20\necho \"===== AHD candy =====\"\ngrep -n -i \"candy\" AHD_watkins1985.txt | head -20\necho \"===== IEC =====\"\ngrep -n \"^ghedh\\|^g̑hedh\\|^gu̯hedh\\|^gwhedh\\|^ghen-\\|^gu̯hen\" IEC.txt | head -20\necho \"===== SYN 1471 =====\"\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor p in (471,472):\n    i=p+24\n    print('---printed',p,'leaf',i); print(t[i][:1800])\nEOF"
}
```


### [2026-09-06T14:53:54.302Z] TOOL RESULT

```
===== AHD watkins gwhedh =====
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
1280:BE- ambhi BEACON bha-1 BEAD gWhedh- BEADLE bheudh- BEAM bheue- BEAN bha-bha- BEAR! bher-1 BEAR? bher-3 BEARD bhardha BEAT bhau- BEATIFIC deu-2, dhé-1 BEATIFY deu-2 BEATITUDE deu-2 BEAU deu-2 BEAUTY deu-2 BEAVER! bher-3 BECHE-DE-MER mori- BECK? bheg¥- BECKON bha-! BECOME gWa- BED bhedh-
1296:BID bheudh-, ghedh- BIDE bheidh- BIDENTATE dent- BIDONVILLE weik-1 BIENNIUM at-
1557:GAST gheis- GASTRIC gras- GASTRO- gras- GASTRULA gras- GATHER ghedh- GAUCHE weng- GAUD gau- GAUDY! gau- GauDY? gau- GAUGE ghalgh- GAUNTLET? klou- GAUR gWou- GAVEL? ghabh- GAWK ghow-é- GAYAL gWou- _ GEANTICLINE gé GEAR garwian GEGENSCHEIN gagina, skeei- GELANDESPRUNG lendh-2, spergh- GELATIN gel-3 GELATION gel-3 GELD! ghel-3 GELD2 gheldh- GELDING ghel-3 GELID  gel-3 GELIGNITE egni- GELT! gheldh- GEM gembh- GEMINATE yem- GEMINI yem- GEMMA gembh- GEMMATE gembh- GEMMULE gembh- GEMOT mdéd- GEMSBOK bhugo- GEMUTLICH mé-1 GEMUTLICHKEIT mé-1 -GEN gene- GENDARME gene- GENDER gene- GENEALOGY genoe- GENERAL gene- GENERATE genoe- GENERATION geno- GENERIC gene- GENEROUS gene- GENESIS gene- -GENESIS gene- GENIAL! gene- GENIAL? genu-2 GENICULATE genu-1 GENITAL gene- GENITIVE gene- GENITOR gene- GENIUS gene- GENOCIDE gene- GENOTYPE gene- GENRE gene- GENS gene- GENT! gene- GENTEEL gene-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
2395:TOFT deme-1 TOGA (s)teg- TOGETHER ghedh- TOIL! (s)teu- TOIL? teks- TOKEN deik- TOLA tele- TOLERATE tele- TOLL! tele- TOMB teue- TOME tem- -TOMY tem- TONE ten- TONGS denk- TONGUE dnghi TONOPLAST ten- TONSURE tem- Too de-
===== AHD watkins gwhen swell =====
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1506:FENCE gWhen-! FENNEL dhé@(i)- FENUGREEK dhé(i)- -FER bher-1 FERAL ghwer- FER-DE-LANCE ferrum FERE per-2
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1572:GUN gWhen-1 GURGITATION gWere-4 GURU gWera-2 GUSH gheu- Gust! gheu- GusT2 geus- GUSTO geus-
1962:OFFEND g¥hen-! OFFENSE gWhen-1 OFFER bher-1 OFFICE dhé-1 OFFICINAL dhé-1, op-1 OFT upo
===== AHD candy =====
===== IEC =====
===== SYN 1471 =====
1545
---printed 471 leaf 495
lsboug, hal- spouc, MHG halsbouc, lit. ‘neck-ring’, cf. ON baugr ‘bracelet’ (6.74).
NE necklace, epd. of lace (6.26), but here used in older sense ‘noose, cord’. NED sv.
Du. halssnoer, lit. ‘neck-cord’, cpd. of snoer = NHG schnur ‘cord’.
OHG, MHG halsgolt, lit. ‘neck-gold’. (Cf. Goth. jiggragulb ‘finger-ring’, 6.78).
NHG halsband (Dan. halsbaand, Sw. halsband by semantic borrowing), lit.
i 4 )
Digitized by Arya Samaj Foundation Chennai and eGangotri
446 SELECTED INDO-EUROPEAN SYNONYMS
5. Lith. kaklarysis (also ‘necktie’), fy. kaklas ‘neck’.
Lith. karicliaz, pl. of karielis ‘heaq (orig. ‘coral’), used for ‘(bead) neck. lace’ (NSB, Lalis).
Lett. kakla (gen. sg. of kakls ‘neck’) with ruota ‘adornment’ (6.71), or bante ‘band’ (fr. NHG).
6. ChSI., Russ. monisto (Russ. arch. or local) : Lat. monile (above, 2).
ChSI. grivina, fr. griva ‘mane’ : Skt, griva- ‘neck’, ete. Berneker 352,
ChSI. (late) ogrili, ozrélt, Russ. oZerel’e : ChSl. griilo, Russ. gorlo, ete. ‘throat? Miklosich 63.
Boh. ndhrdelnik, Pol. naszynik, dim, epds. of na- ‘on’ and the words for ‘throat, neck’, Boh. hrdlo, Pol. szyja,
7. Skt. kanthika- (rare), fr. kantha- ‘neck’. Also kantha-bhisd- epd. with bhas- in caus. ‘adorn’ (cf. bhisana-,
‘neckband’. 6.71). 6.81 HANDKERCHIEF ; NG pavridt Dan. lemmetgrklade Lith. nosiné 3 It. Sazzoletto, pezzuola Sw. ndsduk Lett. slaucis ‘ Fr. mouchoir NE handkerchief SCr. maramica Sp. paiiuelo Du. zakdoek Boh. kapesnitk ee batista, basma NHG faschentuch, schnupf- Pol. chustka tr. ciarstir tuch Russ. latok cadach (poced), por? hances Br. mouchouer, mouched
Words for ‘handkerchief’ are listed
only for the modern languages. Yor
such words as Grk. Xétpopaxrpoy, Lat. | mantéle, etc., which might have served \ also as handkerchiefs, see ‘towel’ (6.82). | But Lat. sidarium, lit. ‘sweat
---printed 472 leaf 496
v, etc. 2. a towel’ (gl. to Tas ygoe-tlot as 6.82); deriv. NG Wy 31282:
te uold, im. of pezza ‘piece of It. pe
roucher ‘blow the fr. Lat. mucus
of pano ‘cloth’
is sid, also ‘eambric (cloth)’,
Rum. bali Bod batiste ‘cambric’ (named for a tin Batiste de Cambrai, who de-
veloped a famous linen factory in the
13th cent.) Rum. basma (also Turk. basma ‘printed cloth’. 9 of Nit. ciarsiir (also ‘kerchief’), bor- rowed fr. NE kerchief in some dial. pronunciation. W. cadach (poced), lit. ‘pocket-cloth’, cf, cadach ‘cloth, rag, kerchief’ (= NIv. cadach ‘calico’, prob. : W. cadas, NIr. cadas, fr. ME cadas (NE caddis), with suffix after NIr. canach ‘cotton’ (?). See under ‘cotton’ (6.24). W. hances, fr. a vulgar form of NE handkerchief (cf. hanky).
Br. ‘mouchouer, mouched, borrowed (and the latter adapted) fr. Fr. mouchoir.
‘kerchief’), fr. Lokotsch
NAL ADORNMENT AND CARE
Igitized by Arya Samaj Foundation Chennai and eGangotri
447
4, Dan. lemmet¢érklede, cpd. of lomme ‘pocket’ and igrklade ‘kerchief, neck- cloth’ (cpd. of égr ‘dry’ and klede ‘cloth’).
Sw. ndsduk, lit. ‘nose-cloth’.
NE napkin (6.83), formerly used also, and still Sc., for ‘handkerchief,’ NED s.v. 2.
NE handkerchief, epd. of kerchief, ME curchef, fr. OFr. couvre-chief, lit. ‘cover-head’, a cloth for covering the head, a sort of woman’s headgear. NED s.v.
Du. zakdoek, NHG taschentuch, lit. ‘pocket-cloth’.
NHG = schnupftuch, fr. schnupfen ‘snuff’, MHG snupfen ‘puff, blow, snort’.
5. Lith. nosiné, fem. of adj. nosinis ‘of the nose’. Lett. slaucis : slaucit ‘wipe off’.
6. SCr. maramica, dim. of marama, mahrama ‘rag, cloth’, orig. ‘veil (of a married woman)’, through Turk. fr. Arab. mahrama ‘holy, forbidden, wife’ : Arab. haram ‘forbidden’. Lokotsch 1361.
Boh. kapesntk, fr. kapsa ‘pocket’.
Pol. chustka, dim. of chusta ‘(li
```


## [2026-09-06T14:54:07.305Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor p in (1470,1471):\n    i=p+24\n    if i<len(t):\n        print('---printed',p,'leaf',i); print(t[i][:1200])\nEOF\necho \"=== SYN ASK/BEG/PRAY section ===\"\ngrep -n \"16\\.6[0-9] \\|ASK$\\|PRAY\\|BEG (\" SYN.txt | head -20"
}
```


### [2026-09-06T14:54:10.262Z] TOOL RESULT

```
---printed 1470 leaf 1494
i and eGangotri
WARFARE
1393
OFr. brant. REW 1273.
5. Lith. kalawjas : OPruss. kalabian id., Lat. clava ‘club’, fr. the root in Lith. kalti ‘strike’, etc. (cf. Ir. claideb, above 3). Trautmann, Altpreuss. 351. (Walde- P. 1.437).
Lith. kardas (cf. NSB; formerly the usual word), fr. Pol. kord, cf. ChSl. kor(%)da (below, 6).
Lett. zuobens : zuobs ‘tooth’, as ‘cut- ting’, or orig. actual sword with teeth. Miihl.-Endz. 4.756.
6. ChSl. medi, etc., general Slavic, belongs in some way with Goth. méki, etc. (above, 4), but not directly fr. the attested Gmc. form (for which one would expect ChSl. méét, etc.), perh. fr. the same unknown source. Berneker 2.29 f. Stender-Petersen 221f., 507, Brickner 331.
Late ChSl. kor(ii)da, ete. (general Slavic, but no longer the usual word anywhere), fr. Pers. kard = Av. karata- (below, 7). Berneker 569. Briickner 256.
7. Skt. asi- (Av. awhi- ‘sword’ Barth. 110, but dub.) : Lat. énsis (above, 2).
Skt. khadga-, cf. W. cleddyf (above, 3).
Av. karata- ‘knife’, as weapon ‘dag- ger’ or ‘sword’ (Darmesteter ‘épée’) : karat-, Skt. kri- ‘cut’. Barth. 454.
NED s.v. brand, sb. 8.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
r } Digitized by Arya Samaj 
---printed 1471 leaf 1495
unim-
portant in contrast to the siege gun. Of the old names, some have remained the common terms, unaffected by the change of type (e.g. Fr. fusil), some are now used only or mainly for the shotgun (It. schioppo, Sp. escopeta, NHG biichse), and others have disappeared from use except with reference to earlier history, e.g. NE hackbut, (h)arquebus (= MLG hakebusse, MHG hakenbiihse, lit. ‘hook- gun’), flintlock, musket (orig. name of a bird), carbine (weapon of the carabin, for which see now Gamillscheg 184).
The words for ‘gun’ reflect their tubular form (from words for ‘tube’ or ‘cylindrical box’), their action (‘fire, throwing, shooting’), some special fea- ture of the mechanism (‘flint-lock’, etc.), the sound of the explosion (MLat. bom- barda, etc.), or they may be words for ‘weapon, machine, piece, piece of work’ used in specialized sense.
1. Byz. rndeBédos, in class. Grk. adj. ‘shooting from afar’, is the regular term for ‘cannon’ in Chalcond., e.g. 1.231 passim.
Byz. é\e86ts, usual for ‘cannon’ in Phrantzes (e.g. p. 239), is apparently due to a confusion of the preceding (so regularly in cod. Par.) with the old ékerodis (lit. ‘city-taking’) which was
CC-O0. In Public Domain.
=== SYN ASK/BEG/PRAY section ===
27460:16.61 Wrz, Wiss (vb.)
27461:16.62 Derstre (vb.)
27462:16.63 Hops (sb.)
27463:16.64 THanxs
27464:16.65 Farrarun
27465:16.66 Tru
27466:16.67 Li (sb.)
27467:16.68 Dercrir
27468:16.69 Forcive
29224:1160 SELECTED INDO-EUROPEAN SYNONYMS 16.61 WILL, WISH (vb.) Grk. (é)8éAw, BobrAopat Goth. wiljan Lith.  noréti NG 6aw ON vilja, eskja Lett.  gribat (vélet) Lat. __velle Dan. ville, énske ChSl. chotéli, chits; It. volere Sw. vilja, 6nska SCr.  htjeti Fr. vouloir OE willan, wijscan Boh.  chtéti Sp. querer ME _ wille, wisshe Pol. cheiéé Rum. voi, vrea NE will, wish, want Russ. chotet’ Ir. dithraccar Du. willen, wenschen Skt. vag-, i3- NIr. toil (in phrases) OHG  wellen, wunscen Av. vas-, i§- W. ewyllysio, mynnu MHG wellen, wollen, wiin- Br. mennout, yoult schen NHG_ wollen, wiinschen The words listed are the most com- | delAouar, 84 Aopuar, Bée\Nonar, etc., all
29256:Walde-P, 1.960, Falk-Torp 1420. (18.31, 18.35). Walde-P. 1.12. oe 16.62 DESIRE (vb.)
29310:16.63 HOPE (sb.)
29346:16.64 THANKS
29390:orion: TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1167 EL 16.65 FAITHFUL Goth. triggws Lith.  78tikimas
29408:16.66 TRUE (Or in part sb. Truth)
29444:16.67 LIE (sb.)
29473:16.68 DECEIT
29560:16.69 FORGIVE
```


## [2026-09-06T14:54:10.325Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN grep gada / hugasta / khugasta ===\"\ngrep -n -i \"gadā\\|gadâ\\|gada '\\|Bettler\\|hugasta\\|huǰasta\\|hujasta\\|xugasta\\|hu\\^gasta\" HRN.txt | head -40\necho \"=== HRN leaf for printed 470 (=491) ===\"\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nEOF"
}
```


### [2026-09-06T14:54:12.466Z] TOOL RESULT

```
=== HRN grep gada / hugasta / khugasta ===
5026:559. derves 'Bettler; arm', deryös (Vis und RämTn, S. 395,
=== HRN leaf for printed 470 (=491) ===
leaves 412
```


## [2026-09-06T14:54:25.029Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\n# find leaf containing '1471'\nfor i,pg in enumerate(t):\n    if re.search(r'\\b147[01]\\b',pg) and i>1400:\n        print('leaf',i, repr(pg[:200]))\nEOF\necho \"=== 18.35 ===\"\ngrep -n \"18\\.35\\|18\\.31\" SYN.txt | head -20"
}
```


### [2026-09-06T14:54:28.890Z] TOOL RESULT

```
=== 18.35 ===
11968:3 Ir. tenlach, tellach, NIr. teallach, deriv. of Ir. tene ‘fire’ (1.81), with suffix ach ‘place of? (fr. IE *legh- ‘lie’). Loth, MSL 18.352.
19399:5. Lith. zeskoti : ChSl., SCr. iskati, Boh. (old) jiskati (Pol. iskaé old ‘seek’, now ‘hunt lice, louse’), Russ. iskat’, Skt. is- ‘seek, wish’ (esp. with anu- ‘seek after’), Av. 7&- ‘seek’, OHG eiscon ‘in- quire, ask, demand’, OF dscian ‘at- tempt, demand, ask’, etc. (18.31). Walde-P. 1.12. Berneker 432 f.
19895:The majority of the words for ‘beggar are from verbs for ‘ask for’ (18.35). But several are in origin opprobrious epithets (like NE bum), based in part upon certain physical or mental defects.
19897:NG fnridvos, fr. {nr ‘seek, ask for’ (11.31, 18.35).
27870:In several languages the verbs for ‘please’ furnish the stereotyped polite ‘please’ (take a seat, etc.), as NE please, shortened from (may it) please you (NED s.v. please 6 c), It. per piacere, Fr. s’il vous plait. But more widespread is the use of the first singular of a verb for ‘ask, request’ (18.35), as NG zapa- cada, NHG bitte, Lith. pragau, SCr. molim, Boh. prosim, Pol. prasze, Rum. rog. Among other such phrases are Sp. hace el favor ‘do the favor’ (or simply favor), Dan. ver saa god ‘be so good’, Russ. pozaluista : pozalovat’ ‘do a favor’, Sp. sirvase (more formal than favor), refl. of servir ‘serve’.
29256:Walde-P, 1.960, Falk-Torp 1420. (18.31, 18.35). Walde-P. 1.12. oe 16.62 DESIRE (vb.)
31429:SING A Spout, CRY OuT 18.14 VaRrrous CRIES 18,21 SPEAK, TALK 18.22 Say 18,23 Be SILENT 18.24 LANGUAGE 18.25 DIALECT 18,26 WorD 18.27 DicTIONARY 18.28 NAME 18.31 Asx! (Question, Inquire) 18.32 ANSWER (vb.) 18.33 ApMiT, CONFESS 18.34 Deny 18.35 Asx?, REQUEST 18.36 Promise (vb.) 18.37 RerusE 18.38 Forbip
31824:18.31 ASK! (Question, Inquire)
31826:There is considerable interchange, in the same word or among cognates, be- tween the two notions covered by NE ask, namely 1) ask ‘question, inquire’ and 2) ask ‘request’ (ask a person to do something, and with the thing requested as object, ask aid, but for the latter now most commonly ask for, like NHG bitte wm). In such groups the develop- ment may be in either direction or from & common ‘seek’ (an answer or a thing). In the following, for the sake of brevity, the two senses are distinguished as ‘ask’! and ‘ask’. But except in words or groups in which both senses are involved ‘ask’! is understood here, and expressions for ‘ask’ are combined in 18.35.
31964:18.35 ASK?, REQUEST Grk. — alréw (Epwréw) Goth. bidjan Lith.  pragyti, reikalauti NG §q7G, wapaxadd ON bidja Lett. prasit Lat.  poscere, pelere, rogare Dan. _bede, forlange, fordre ChSl.  prositi, moliti It. domandare, (ri)chie- Sw. bedja, begdra, fordra SCr.  -moliti, iskati, traziti dere OE biddan, dscian, giwian Boh. _ prositt, Zddali Fr. demander ME bidde, aske, demaund Pol. prosic, zadaé Sp. pedir, rogar NE ask, request Russ. prosit’, trebovat' Rum. cere Du. verzoeken, verlangen Skt. yac-, (pra-)arthaya- Tr. condaigim, cuingim OHG _ bitten, eiscon Av., OPers. jad- Nir. tarraim MHG bitten, eischen, vor- W. gofyn Br. goulenn NHG bitten, verlangen, for-
31966:Several of the words for ‘ask, request’, briefly ‘ask’, are the same as, or related to, those for ‘ask, inquire’, briefly ‘ask’!, See 18.31. Others are cognate with words for ‘seek, desire’, ete. Besides the words listed, those for ‘wish, will’ are often used with the implication of a mild, or even firm, request.
31969:1. IE *prek-in words for ‘ask’ in both senses. See 18.31.
31974:NG £178, fr. class. Grk. fnréw nee (11.31). Also rarely demand require’. Grk. gpwraw ask’! (18.31) is fre- d for ‘ask’ in Hellenistic quently use times (XX, NT, pap.).
31977:Lat. rogare ‘ask’ in both senses (18.31), as ‘ask’? > Sp. rogar; Rum. ruga in polite phrase le rog, vd rog ‘please’, or refl. ‘pray’.
31978:Ir. domandare, Fr. demander ‘ask’ in both senses (18.31).
31983:W. gofyn, ‘ask’ in both senses (18.31).
31984:Br. goulenn, ‘ask’ in both senses (18.31).
31987:W. begdra, orig. only ‘desire’ (16.62). ae ascian, ME aske, NE ask, OHG on, G eischen, ‘ask’ in both Senses (18.31).
32357:OPers. pati-pars- ‘read’ (an inscrip- tion) = Av. paiti-fras- ‘ask’, cpd. of fras- ‘ask’ (18.31). Cf. Pahl. patpurs-, Sogd. péBs- ‘read’. Barth. 999. Ben- veniste, BSL 31.2.71.
33550:Goth. ana-biudan, ON bjoda, Dan. byde, Sw. bjuda, OE (ge-) béodan, ME bede (and by confusion with OE biddan ‘ask, request’, also bidde, NE bid in this sense, cf. 18.35), Du. gebieden, OHG gibiotan, MAG, NHG gebieten, in North and West Gmc. also ‘offer’ (so usually the simple verb OHG biotan, NHG bie- ten), in OE also ‘announce’ : Grk. zy- Gavouar “find out, hear’, Lith. budéti ‘wake’, ChSl. buditi ‘awaken’, Skt. budh- ‘wake, be awake, notice, be aware’, etc. Pee: 2.147, Falk-Torp 120f. Feist
```


## [2026-09-06T14:54:35.469Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nraw=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=raw.split('\\n')\n# map line -> leaf\ndef leaf_of_line(ln):\n    txt='\\n'.join(lines[:ln])\n    return txt.count('\\f')\nfor ln in (31964,19895,32357):\n    print('line',ln,'leaf',leaf_of_line(ln))\nEOF"
}
```


### [2026-09-06T14:54:38.187Z] TOOL RESULT

```
line 31964 leaf 1362
line 19895 leaf 850
line 32357 leaf 1379
```


## [2026-09-06T14:54:41.625Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (1362,1363,1364,1365,1366,1367):\n    print('==== leaf',i)\n    print(t[i][:2200])\nEOF"
}
```


### [2026-09-06T14:54:44.035Z] TOOL RESULT

```
==== leaf 1362
ht, strive, con- tend’, OHG sahhan ‘quarrel, contend’ : Goth. sakan ‘strive, rebuke’, etc.
ME withsaye, cpd. of with- (cf. above) and saye ‘say’ (18.22).
ME denye, NE deny, fr. OF r. deneier, Fr. dénier ‘refuse, disown’, fr. Lat. dénegare ‘reject, refuse’, cpd. of negare (above, 2). NED s.v.
5. Lith. ginéyti, iSsiginti (also uz-) : ginti (ginu, gyniau) ‘defend, protect, for-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1270
bid’, also refl. ‘deny’, and gintt (genu, giniau) ‘drive’, ChSl. Zena, ginati ‘drive’, etc. (10.65). NSBs.vv. Walde- P. 1.680 f.
Lett. liegt (also ‘forbid, refuse’), refi. liegties, etym. dub.; perh. as ‘restrain’ : Ukr. za-lyhaty ‘tie up, bind, pledge’, Lat. ligare ‘tie’, etc. (Walde-P. 2.400). Miihl.- Endz. 2.494.
6. ChSl. ottivrésti se (1sg. ottivriiga se; the usual rendering of dpyéouar in the Gospels), refl. of ottivrésti ‘throw away, reject’, cpd. of vrésti ‘throw’ (10.25).
ChSl. ottimetati se, and ottimétati se, refl. of ottimetati, ottimétati ‘throw away’ iter. to mesti ‘throw’ (10.25). Berneker 2.40, 53.
SCr. odricati, poricati, Russ. otricat’, epd. of od-, po-, ot- with sense ‘away, back’ and iter. forms to SCr. reéi,
SELECTED INDO-EUROPEAN SYNONYMS
ChSI. rest, ete. ‘say’ (18.22). of. prérékati ‘contradict? (Supr.).
Boh. popftti, Pol. zaprzeé sie, Zapieraé st¢, Russ., otperet’, epds. (in part Tefl.) of Boh. pitti ‘contest, dispute’, Pol, przeé Russ. peret’ ‘press, push, jostle’, ChSL piréti ‘beat, wash (by beating)’, A ‘contend, ‘strive’ : Skt. prt- ‘fight, quar- rel’, Arm. hari ‘strike’, ete. Walde-P. 2.42. Briickner 442,
Pol. przeczyé, fr. the ady. przeko
ChSI,
- ‘across, diagonally through’, Briickner
443.
7. Skt. ni-hnu-, apa-hnu-, epds. of ni- ‘down, back’, or apa- ‘away, back’, and hnu- ‘hide from, drive or take away’ (etym. dub., Uhlenbeck 362).
Skt. apa-lap-, epd. apa- (ef. above) and lap- ‘prate, chatter, talk’,
18.35 ASK?, REQUEST Grk. — alréw (Epwréw) Goth. bidjan Lith.  pragyti, reikalauti NG §q7G, wapaxadd ON bidja Lett. prasit Lat.  poscere, pelere, rogare Dan. _bede, forlange, fordre ChSl.  prositi, moliti It. domandare, (ri)chie- Sw. bedja, begdr
==== leaf 1363
rds for ‘ask’ in both senses. See 18.31.
Here as ‘ask’? Lat. poscere, Lith. pra- Sytt, Lett. prastt, ChSI. prositi, ete., gen- eral Slavic (but SCr. prositi now ‘beg; woo’).
2. Grk. alréw, prob. as ‘demand one’s share’: aloa (*alria) ‘share, fate’, at cws ‘auspicious’, atotpos ‘fated, des- tined’, etc., Osc. aeteis ‘partis’, Ay ns punishment, guilt’? (ie. ‘ones %0”/ Walde-P. 1.2.
|
vOoCAL UTTERANCE, SPEECH; READING AND WRITING
NG £178, fr. class. Grk. fnréw nee (11.31). Also rarely demand require’. Grk. gpwraw ask’! (18.31) is fre- d for ‘ask’ in Hellenistic quently use times (XX, NT, pap.).
NG rapaxaha (milder than ¢774, used ike NE I beg you, I pray you, please), fr, class. Grk. mapaxadéw (epd. of kare call’, 18.41) ‘summon, invite, exhort’, etc., late also ‘beseech’ (Polyb., NT, etc.).
3 Lat. petere (> Sp., Port. pedir), orig. (‘fly at’) ‘assail, attack’, hence geek’ and ‘ask, request’ : Grk. qérouac ‘fly’, Skt. pat- ‘fly, fall’, ete. Walde-P. 1.20, Ernout-M. 763 f.
Lat. rogare ‘ask’ in both senses (18.31), as ‘ask’? > Sp. rogar; Rum. ruga in polite phrase le rog, vd rog ‘please’, or refl. ‘pray’.
Ir. domandare, Fr. demander ‘ask’ in both senses (18.31).
It. (r2)chiedere, Rum. cere, fr. Lat. quae- rere ‘seek’ (11.31). REW 6923, 7235.
4, Ir. condaigim, cuingim, fr. *com-di- saigim, cpd. of saigim ‘go toward, seek’ (11.81). Pedersen 2.607. Thurneysen, Gram, 116,450.
Ir. guidim, mostly ‘pray’, see 22.17.
NIr. tarraim, also (and in OIr. most- ly) ‘seek’ (11.31).
W. gofyn, ‘ask’ in both senses (18.31).
Br. goulenn, ‘ask’ in both senses (18.31).
5. Goth. bidjan (bap, bédum, bidans), ON bidja, Dan. bede, Sw. bedja, OE bid- dan, ME bidde, (NE bid ‘command, in- vite’, etc. by crossing with OE béodan; Du. bidden mostly ‘pray’), OHG, MHG, NHG bitten, etym. disputed, perh. (with Secondary ablaut) : Grk. eldw ‘per- Suade’, Lat. fidere ‘believe, trust’, etc. Walde-P, 2.139, Kluge-G. 60. Falk-
ae 66. Feist 89. NED s.v. bid., vb.
W. begdra, orig. only ‘desire’ (16.62). ae ascian, ME aske, NE ask, OHG on, G eischen, ‘ask’ in both Senses (18.31).
Digitized by Arya Samaj Foundation Chennai and eGangotri
1271
OE giwian (freq. in Lindisf. Gospels) : ginam, OHG ginén, giwén, etc. 
==== leaf 1364
dra), OHG fordarén, lit. ‘cause (command) that something go forward’, deriv. of OHG fordar, etc. ‘fore, forward’. Weigand-H. 1.568. Falk-Torp 266.
6. Lith. reikalauti (mostly ‘demand’), fr. reikalas ‘necessity’ : reikétt ‘be neces- sary’ (9.93).
7. ChSl. prositi, etc., above, 1.
ChSI., SCr. molitt ‘ask, beg’, refi. ‘pray’, see under ‘pray’ (22.17).
SCr. iskatz, also ‘seek’ (the general Slavic meaning, ChSI. iskati, ete., 11.31).
SCr. traZiti, also ‘seek’ (11.31).
Boh. 2ddati, Pol. zqdaé, orig. ‘desire’ (16.62).
Russ. érebovat’, orig. ‘need’ : Chl. irébé ‘opus ut’, trébu% ‘necessary’, etc. (9.98, 9.94).
8. Skt. ydc-, perh. : OHG jehan ‘con- fess, acknowledge, say’, W. iaith ‘lan- guage’, etc. Walde-P. 1.205.
Skt. arthaya-, esp. prarthaya- (pra- arthaya-), lit. ‘strive to obtain, desire’ : artha- ‘aim, purpose’ (17.41).
Av., OPers. jad- ‘beseech, pray for’, see under ‘pray’ (22.17).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
1272 18.36 PROMISE (vb.)
Grk.  dmoxvéiopat, trayyéd- Goth. gahaitan Lith. (pri)Sadé1;
dw ON _heitan Lett. cae NG _ drbcxopat, rato Dan. love ChSl.  obéStatz Lat. prdmitlere Sw. lova SCr.  obec¢ati It. promettere OE (be)hatan Boh. _ slibiti Fy. promeltre ME _(be)hote Pol. —_obieca¢, przyrzec Sp. promelter NE promise Russ. obeSéat’, sulit! Rum. promite, fagddui Du. beloven Skt. pratijaa-, praticry Ir. duairngir, gellaim OHG  giheizan ; oru- Nir. — geallaim MHG ge-, ver-heizen, ver- W. addaw sprechen Br. gouestla NHG versprechen, verheis-
sen
Words for ‘promise’ include some meaning literally ‘undertake’ or ‘put forth’, several cpds. of verbs for ‘speak, say, call, know, hear’, derivs. of nouns for ‘vow, pledge’, and some cognates of words for ‘dear’ and ‘love’ (‘find agree- able, acceptable’ > ‘promise’).
1. Grk. tricxvéouat and (Ion., Delph., etc.) tricxoua, late Byz., NG trécxopa (cf. Grk. fut. bro-cxjoouat, 2d aor. bre- oxéunv), orig. ‘undertake’, cpd. of d7é ‘under’ with forms of icxw ‘hold, hold back’ (*si-2gh-) and éxw ‘hold, have’.
Grk. érayyé\dw ‘proclaim, announce’, but freq. also ‘promise’, cpd. of Grk. ayyeddw ‘announce’.
NG pop. 
==== leaf 1365
ion, Haridwar
W. addaw, addo, fr. ad + do ‘yes’, hence orig. ‘say yes to’.
Br. gouestla, deriv. of gouestl ‘vow, — promise, pledge, hostage’ (= W. guwysil, etc.; cf. Ir. gellaim, above).
4, Goth. gahaitan (‘call together’ and ‘promise’), ON heita, OE (be)hatan, ME (be)hote, (be)hete, (be)highte, NE arch. hight, OHG gtheizan, MHG geheizen, verheizen, NHG verheissen, epds. (or the simple form) of Goth. haitan, etc. ‘call’ (18.41) and ‘command’ (19.45). Feist 236. NED s.v. hight, vb., B2.
Dan. love, Sw. lova (ON lofa ‘allow, permit’, but NIcel. ‘promise’), Du. be- loven (MLG loven, OFris. lovia id.) : OHG gelobén ‘agree, permit’ (NHG gelo- ben ‘vow, pledge’), Goth. us-laubjan, OE G@liefan, OHG ir-louben ‘permit’, Goth. liufs, etc. ‘dear’ (16.26; cf. also words for ‘praise’ and ‘believe’ belong- ing to same group of cognates). Walde- P. 2.419, Falk-Torp 656f. Franck-v. W. 48.
NE promise, fr. the sb. promise, fr. Lat. promissum (: promittere, above, 2).
MHG, NHG versprechen, fr. OHG fir- sprehhan ‘refuse, forbid, hinder’, also ‘speak for someone, defend’ (these senses also in MHG), epd. of OHG sprehhan ‘speak’ (18.21). Paul, Deutsches Wtb. 602.
5. Lith. Zadéti, prizadéti (18.26).
1 : Zodis ‘word
VOCAL UTTERANCE, SPEECH; READING AND WRITING
Lett. suolit, apsuolit, fr. Russ. sulit' id. (below). Miihl.-Endz. 3.1137 f.
6. ChSl. obéStatz, SCr. obeéati, Pol. obiecaé, Russ. obeséat’, beside sb. ChSI. obit, etc., fr. *ob-véstati, *ob-véti : ChSI. véStati ‘speak’ (18.21). Briickner 370, 614.
Boh. sltbiti (with sb. slib), epd. of si- and libiti ‘like, love’ : ChSI. jubiti ‘love, kiss’, jubti ‘dear’ (Goth. liufs ‘dear’, etc., ef. above, Dan. love, etc.). Miklosich 171.
Digitized by Arya Samaj Foundation Chennai and eGangotri
1273
Pol. przyrzec, -rzekaé, epd. of przy- ‘to’ and rzec ‘say’ (18.22).
Russ. sulit’, prob. (through use as ‘promise well’) : ChSl. suléji ‘better’. (Briickner 525, also : ChSI. siilati ‘send’, very dub.).
7. Skt. prati-77a-, lit. ‘recognize’, cpd. of prati- ‘toward’ and jna- ‘know’.
Skt. prati-cru-, lit. ‘listen to’, epd. of prati- (cf. above) and ¢ru- ‘hear’.
18.37 REFUSE
Grk.  dapvéopac Goth. Lith.  atsakytz NG dovoduat, apverepat ON neita * Lett. liegt

==== leaf 1366
l of the words for ‘refuse’ (a re- quest, an offer, etc.) are the same as, or from the same source as, those for ‘deny’ (18.34). Others are from ‘say off, swear off, strike off’, etc.
1. Grk. dpvéouar, NG dpvodpa ‘deny’ (18.34), also ‘refuse’.
2. Lat. reciisdre, prob. orig. as law term ‘challenge, object to’, deriv. of causa ‘cause, lawsuit’. Ernout-M. 166.
It. rifiutare, for Olt. rifutare (influ- enced by fiutare ‘sniff’), fr. Lat. refutare ‘drive back, repel, disprove, refute’, cpd. like confiatdre ‘repress, confute’, perh. (*bhawt- beside *bhaud-) : ON bauta, OE béatan ‘strike, beat’. Walde-H. 1.258. REW 7165.
Fr. refuser (> Rum. refuza), Sp. re- husar, fr. VLat. *refiisare, prob. blend of recusdre and refitare (above). REW 7164. Gamillscheg 750. Diez 270.
weigern, abeslahen verweigern, abschla-
3. Ir. astoing (8sg.), lit. ‘swears off’, epd. of ess- ‘off, from’ and tongu ‘swear’ (21.24); vbl. n. eitech, whence MIv. eitchim, NIr. eitighim. Pedersen 2.652. Thurneysen, Gram. 509.
Ir. émdim (forémdim ‘be unable’), W. gomedd, cpds. of vb. seen in Ir. midiur “judge’, W. meddu ‘possess.’ Pedersen 2.578 ff. Loth, RC 38.296.
W. nacau, Br. dinach (with di- from’), cf. Br. nac’h ‘deny’ (18.34).
4. ON neita ‘deny’ (18.34), also ‘re- fuse’.
OE wipsacan ‘deny’ (18.34), also ‘re- fuse’; similarly OHG farsahhan both ‘deny’ and ‘refuse’, but more esp. in the latter sense OHG widarsahhan.
ME, NE refuse, fr. Fr. (above, 2).
ME withsaye ‘deny’ (18.34), also ‘re- fuse’.
refuser
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1274 SELECTED INDO-EUROPEAN SYNONYMS
ME denye, NE deny (18.34), also ‘re- fuse’ (NED s.v. III).
Du. weigeren (MLG wégeren > Dan. vegre only refl. with prep. ved, Sw. vdgra), OHG weigardn, MHG weigern, NHG weigern, mostly verweigern : OHG weigar, MDu. weiger, wéger ‘resisting, stubborn’, fr. the root of Goth. wethan, OHG wigan ‘fight’, etc. Walde-P. 1.232. Falk-Torp 1401. Weigand-H. 2.1229.
MHG abeslahen, abeslan (MLG af- slan > Dan. afslaa, Sw. avslé), NHG abschlagen, lit. ‘strike off, down’. Falk- Torp 14.
5. Lith. atsakyti, also ‘answer’ (18.32), lit. ‘say back’.
Lett. legit ‘deny’ (18.34)
==== leaf 1367
��say’, 18.22). Cf. NHG abweisen ‘de- cline, reject’.
7. Skt. prati-d-khyd-, epd. of prati- ‘back’ and 4a-khyd- ‘tell, inform, an- nounce’, khyd- in pass. ‘be named, be known’, caus. ‘make known, relate’.
18.38 FORBID
Grk.  azayopetw, fut. arepd, Goth. faurbiudan Lith.  (uz)drausti BOF. dzetroy ON banna, fyrirbjoda Lett.  (azz)liegt
NG draryopebw Dan. /forbyde ChSl. (vitz)branitz
Lat. _velare, prohibére, in- Sw. férbjuda SCr. zabranili terdicere OE _—forbéodan Boh. zapovédéti, zakdzati
It. proibire, vielare, in- ME sforbede Pol. zakazaé, zabroni¢ terdire NE forbid, prohibit Russ. zapretit’
Fy. défendre, interdire, Du. verbieden Skt. nisidh-, pralisidh- prohiber OHG farbiutan Ay. antara-d-mril-
Sp. prohibir, tnterdecir MHG verbieten, undersagen
Rum. oprt, interzice NHG  verbieten, untersagen
Tr. argairim, arcuillim
NIr. _coiscim, toirmeascaim
W. gwahardd
Br. difenn, berza
‘Forbid’ is often expressed by com- pounds of verbs for ‘command’ or ‘say’ with various prefixes which have come to connote exclusion, interference, ne- gation, etc. (Grk. dmo-, Lat. pro-, inter-, NE for-, NHG ver-, Slavic za-). Or words for ‘hinder, prevent’ (19.59), ‘re-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
pel’, etc. come to be used also as the verbal ‘forbid’.
1. Grk. drayopetw, epd. of a6 ‘away from’, in its use indicating exclusion, negation, and dyopebw ‘speak’. Outside of present system, supplemented by fut.
| | | |
| |
| f { }
VOCAL UTTERANCE, SPEECH; READING AND WRITING
g-ep@, HOF. G-€tov, epds. of other yerbs for ‘speak, say’ (18.21),
Grk. otk é4w ‘not permit’ (19.47) serves for the positive ‘forbid’ in Hom. (where amayopebw does not occur).
Grk. xwdtw ‘hinder, prevent’ (19.59), Jate also sometimes ‘forbid’. In NT (amaryopew does not occur; ‘forbid’ in strict sense is expressed as ‘command not’, e.g. Mk. 6.8, 8.30, etc.) kwhiw is generally rendered by OE forbéodan, NE forbid (e.g. Mt. 19.14 = Lk. 18.16, etc.), but these words are also used, like Lat. prohibére, for ‘hinder, prevent’.
2. Lat. vetdre (>It. vietare, OFr. veer, OSp. vedar), OLat. votdre, prob. : W. gwadu ‘deny’, OW guetid ‘says’. Ernout-M. 1099. Loth, RC 42.367 f.
Lat. interdicere (> It., Fr. interd
```


## [2026-09-06T14:54:50.321Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"22\\.17 PRAY\\|22\\.17\" SYN.txt | head -10"
}
```


### [2026-09-06T14:54:50.371Z] TOOL RESULT

```
19904:3. Ir. foigde ‘begging’ (related form for ‘beggar’ apparently not quotable), vbl. noun fr. epd. of guidim ‘ask for, pray’ (22.17). Pedersen 2.551.
31967:Cf. also words for ‘pray’ (22.17), of which several are the same as those listed here, and some of the others are also used in a nonreligious sense as NE pray.
31981:Ir. guidim, mostly ‘pray’, see 22.17.
31999:ChSI., SCr. molitt ‘ask, beg’, refi. ‘pray’, see under ‘pray’ (22.17).
32006:Av., OPers. jad- ‘beseech, pray for’, see under ‘pray’ (22.17).
```


## [2026-09-06T14:54:53.889Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"jad-\\|jaidy\\|guidim ‘pray\\|PRAY\" SYN.txt | sed -n 1,40p"
}
```


### [2026-09-06T14:54:53.947Z] TOOL RESULT

```
9058:Boh. snidane, Pol. sniadanie ‘break- fast’, ecpd. of siin- ‘with’ and jad-, IE *ed- ‘eat’. Berneker 273,
9062:detrvov ‘the evening meal’ jg Tendereq by vecerja; but it is entered in the list under ‘dinner’, since it is the Principa} meal in Slavic, as in) SCr, objed, Po] obiad, Russ. obed, all fr. ob(tt)jad-, per. fect. cpd. of jad-, IE *ed- ‘eat’, Berneker 273.
29266:Grk. roféw, émuroBiw, fr. dos ‘long- ing, yearning’, also ‘regret’ (for some- thing lost or absent) : déccac8ax ‘beseech ; pray for’, Ir. guidim ‘pray, ask’, Lith. gedauti ‘long for, desire’, ChSI. Zedatr ‘thirst, desire’, etc. (below, 6), Av., OPers, jad- ‘beseech, pray for or to’. Walde-P. 1.673.
31964:18.35 ASK?, REQUEST Grk. — alréw (Epwréw) Goth. bidjan Lith.  pragyti, reikalauti NG §q7G, wapaxadd ON bidja Lett. prasit Lat.  poscere, pelere, rogare Dan. _bede, forlange, fordre ChSl.  prositi, moliti It. domandare, (ri)chie- Sw. bedja, begdra, fordra SCr.  -moliti, iskati, traziti dere OE biddan, dscian, giwian Boh. _ prositt, Zddali Fr. demander ME bidde, aske, demaund Pol. prosic, zadaé Sp. pedir, rogar NE ask, request Russ. prosit’, trebovat' Rum. cere Du. verzoeken, verlangen Skt. yac-, (pra-)arthaya- Tr. condaigim, cuingim OHG _ bitten, eiscon Av., OPers. jad- Nir. tarraim MHG bitten, eischen, vor- W. gofyn Br. goulenn NHG bitten, verlangen, for-
32006:Av., OPers. jad- ‘beseech, pray for’, see under ‘pray’ (22.17).
```


## [2026-09-06T14:55:10.722Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ *46[6-9]\\. \\|^ *47[0-5]\\. \" HRN.txt | head -20\necho \"---context---\"\nawk 'NR>=1 && /^ *47[01]\\. /{print NR\": \"$0}' HRN.txt | head"
}
```


### [2026-09-06T14:55:12.387Z] TOOL RESULT

```
4256:466. yi^miT 'Quelle, Wasserbassin , x^^ (unbelegt und un-
4261:467. xäwer {/"äwer) 'Herr.
4264:468. ^äye 'Ei*.
4276:471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
9930:469. Dazu se/üden zerkratzen' (Sahn. I, 222 Vers 1659,
9933:474. Vergl. Hübschmann, ZDMG. 46, 234 No. 17.
---context---
4276: 471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
```


## [2026-09-06T14:55:14.512Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4250,4300p' HRN.txt"
}
```


### [2026-09-06T14:55:14.830Z] TOOL RESULT

```
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
etwa ;^ä»e *eine Quelle*, sondern ^^änl *die Quelle* (allg.) lesen müssen.1-4 -
Hüb.sohniann. Zr»Mü. :>. 42o.
47<.». '/jtjeffte *^'e^tÄ'i>.-T. jiüoklich". ver^l. fer[jriijeste.
aw. ''h*'i:t.<t'i'. Yrr^'l. aj'i^f't'. p^hlv. 4/a^ (Gemme
.J».v. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).
471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
itürk. /itnL'für. v.-ii:]. NOMtrkt: bei Uübschmann.
<>^at't. Elvi]]., r!^. l:'.:'.!. //tC'.ni, /i'Uc,
aw. vt-ri:l. x'^i^Ot*-: fthlv. /iff«ir id. i. ;frt<tef^) bezw.
/'td'iiw ai. Ytriji. >cj*iiid' Selbst I-Hrstininiung'.
LW. kiipi. ;f<^'r: af;. x'*'inii Oss. ;rwföi: bei. /*«*'*»
n. /»»(t*'!. /i '<»>'// i'..«oi.
Die Diirchsichtiirktrit Jt.-s Zusammenhanges mit l'^</*'
hat wohl Jas d i:eschützt : als Grundform ist etwa *?**
aw. /'adöffii' löder */»iit)'.*y'i-| anzusetzen. Nöldeic ^'
G^'A. l^SJ. .>. t«»:;i« bezweifelt die Richtigkeit 4^*^
EtvmoloKit' vielleicht nicht mit L'nreeht.
Fr. Müllers Erklärung jWZKM. 5. 6b) aus av^
*/ atö.ui/fio nach tiunem Willen sich bewegend*
schon an .>icii wenig Überzeugendes, ganz abgesehe
von der falschen awesti:?chen Xominativbildung.
47:i. yJrätnJden 'schreiten, ^ehen".
ai. l h'ntut'. knlwftfi. hrt'n/Uitr 'gehen, schreiten'.
In der Bedeutung angenehm, erfreuend* etc. ist,
wie schon Vullers gesehen hat. /jrüm ursprünglich
yu/rem. eine Ansicht, der auch Xöldeke beipflichtet
(mündliche Mitteilung».
47o. y/fi' 'Esel*, yj^ryö^ *Hase' (^^ *Eselsohr K /ercür, /«fr^^fAr«?
u. a. m.
aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
```


## [2026-09-06T14:55:33.403Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Bettler / gada ===\"\ngrep -n -i \"gadā\\|gedā\\|gedä\\|gadä\\|Bettler\\|betteln\" HRN.txt | head -20\necho \"=== HUB hujasta ===\"\ngrep -n -i \"hujasta\\|ajasta\\|jasta\\|gada\\|gedā\" HUB.txt | head -20\necho \"=== BRT jad / jaidyemi ===\"\ngrep -n \"jai%emi\\|jaiöyemi\\|jaidyemi\\|hujasta\\|ajasta\\|jad-\" BRT.txt | head -30"
}
```


### [2026-09-06T14:55:33.492Z] TOOL RESULT

```
=== HRN Bettler / gada ===
539:kez gedäl keine euder dtl-l tu nän get'ded
5026:559. derves 'Bettler; arm', deryös (Vis und RämTn, S. 395,
5278:589. dehän, dehen *Mund', dehün *Gedächtniss, Stegreif*,
8680:Torjammern', moiracik 'bettelnd' ; dazu auch np. mit st
9403:1086. vir Sinn, Verstand; Gedächtniss'-), hir, her (8,
9404:Vullers), Viru 'im Gedächtniss habend'.
9407:Et. ir. II, 183); phlv. vir, vlräk im Gedächtniss
9409:kurd. Mr 'Gedächtniss*; bei. glr 'Gedächtniss, Er-
9591:' US ^Gedächtnis, Verstand, Acht* (Hübschmann,
9654:\/fll9. {\)yäd ^Erinnerung, Gedächtniss', yädifär.
9655:aw. yäta- 'Gedächtniss (Geldner, Studien I, 10,
23312:von Herrn 6. Otto's Druckt^rei gedächte, die nioin schwer
=== HUB hujasta ===
3696:1081. Wo findet sich phi. vijastak? Ich finde tiberall nur
3830:100. Wo steht gujasiak mit u ? Ich finde nur gajastak u. s. w.
3831:und nirgends das zu erwartende v(i)jastak (das ZDMG.
5289:Jastan *springen, eilen' von einer Wzl. yas ? ; Jash 'Ungliick*,
5640:1) gajastak (auch gajistak, gajastak geschrieben) 2)
5641:Verflucht*, das als Gegensatz von np. xujasta 'gesegnet,
5642:gliieklich* (= zd. ^hujasta-) auf ein zd. *vTjasta~ zuriick-
5648:i^azand (vgl. Shk. 246, Min. Gl. 91, Aogem. 98, Gujastak
5650:zd. ^vTjasta- = phi. gajastak Verflucht* = jiid. pers. vazasta
5660:64, 8 ; Spiegel, trad. Litt. p. 389 ; Barthelemy, Gujastak Abalish
5663:*) Horn, Grundriss Nr. 1081 nennt phi. vfjastaK-, ohne es zu
5664:belegen. Das in der ZDMG. 46, 143 genannte vicastak (= vijastak)
6959:ipr, gnddram; gudastan vorbeigehen {Ruch gadaridan?), pr.
7640:skr. suvapus' (oben p. 57); xujasta gesegnet, gliicklich' =
7641:zd. ^hujasta-; xurram^) *fr5hlich*, s. oben p. 55.
8209:*scharf, spitz', tiyri- 'Pfeil'; xujasta gesegnet' = zd. */iw-
8210:jasta- neben paz. gazista verflucht' (§ 52, 1); bar^jan =
=== BRT jad / jaidyemi ===
11368:ya»kuyanqm  avantanqm  . .  ajasta  . .  da- oaiti  ". .  auch  nur  ein  ganz  geringfügiges.." V.  18.  37;  —  ahurS  .  .  vidva  yalltt  gäzrä (sd.)  sSnghanhd  Y.  48.  3.  a)  bei  alva-
13147:Mraiui'lre . .  ustaiwm  dadaifJ . .  masdäi  Y. J^J.  14;  —  ai  toi  myatä>m  ahura  imnanhä asäicä  dämä  "wir  wollen  dir,  o  Ah.,  in Ehrfurcht  das  Opfer  weihen  und  dem  Aia" Y._J4.3;  —  stütS  gard  vaAmSng . .  ahuriii dadimahicd  cTsmah'tcä  . .  Y.  4^.  1 ;  _J5.  j ;  — mitenkl.Dat(-Gen.)desPron.pers.:^aJil  tu l  mlnghäc/i .  .  düä  töi  dadsmahi  a%ä  As- mahl..  \.3ij. 4.  a  n)  im  jAw. a)  ohne Obj.  'schenken  sva,  ein  Geschenk  geben, eine  Gabe  reichen':  hs  daoS  as»m  upa.- rao'iayeUe  (sd.)  yS  drvaite  ^datäiti  P.  50; - —  yat  bä  paiti  .  .  naire  asaone  v»r}syät ("für  seine  Arbeit")  asaya  daoaiti  V,_y,  34 35;  —  yB  hs  *gaväslryavar)l {sA.)  *daidlt aSahmäi  ti.iS.  b)  mit  Obj,:  v^htksi hisvqm  dahäiti  yö  .  .  N.  77;  —  yai  nä kasvikqmcit  .  .  avartianqm  naire  asaone ajasta  ..  daoäi/i  V.iÄ'.37;  34;  —  tUtnm ,  .  yS  daoaiti  .  .  ayaptä  Jaioyanisi  Yt,  8. 49;  Ny.^.  II*';  —  da'iai  aHbyasnt  tat  avat äyapt?m   ar>dvt  YL5.  74;  »9,  9-  5.  '5-4;
15093:•  j.  paitt-ätät^e,  -ätätayae-i^  Inf.  '(und) zu  widerstehen,  zu  bestehen',  uzw,  iAxfl'ische Wesen  und  Anfechtungen;  a)  mit  Akk, •/Äf  ajastaca  tlizdi^taca  .  .  xrafstra  Yt. 21. 1.  b)  mit  Gen.:  't}e  .  .  druj5  'tSe . .  iialsiirtis  Yt.  ij.  129;  'o.Si  ^^°i  '3^^ i3S-'38'°,  142,  Y.6S.B,  60.4,  ?'■  '7'' YL(7.4i,  5.12,  y.130,  131,  136',  137'. 138',  Vr.20.  2,  V.  20.3'J,  S.2.i3i  — avaiAAi  pairikayäi  'fayaSca  paitiscapta- yaica  Y.  16.  8.
21242:Formen:  tai  möi  daidr  ahura  hy  mazää rapin(sA.)  tavä  Y.51.  18;  —  neben  einem Objektsakk. :  iahä  . .  sanm  (sA)  caränl.. *äsi»itlm  (sd.)  x/mäAam  kyatcü  mSi /iyät voxs  also  (sd.)  Y.  44. 17;  —  neben  einem Inf.:  Ayal  (zu III)  vTs}nta[sA.)  dngvantftn avS  hyaiiä  gäul  jaidyai  (sd.)  mraol  Y. ^2.14.  b)  im  jAw.;  i)  mit  Ind.;  ia} ahtnai  jasal  äyapUm  y  Alpu^rü  us.zayata Y.5,4;  7,  13,  13;  —  moiu  iai  äs  .  ,  y° fräyatayat  .  .  aoi  zqm  Yt 5.65;  —  altat il ..  aiAhe(ßp.\om)  avayam  *dqtimaM y*  %wä  didvJsma  Y.^Äi;  ' —  i'mai  .  . Stävi/Um  ^yad^tiim  maSya  viminti  .  .  y kainyS  uzvätaydnti  Yt.  ly.  59;  — ya%a/rä toa  (sd.)  amraot  y*  dim  a/iBmisd.ya  .  . adadat  Y.ig.13;  —  ankam  raya  ufar)- natshala  (nämL  asti)  y  bavainti  halat.- pu%rä  Yt/j.  15.  2)  mitKonj.:  avat ayaptim  dazdi  ml  y  bavStii  aiwi.vanyä . . vlstäsptm  ..  ydka  (Sp.  1247  u.)  aztm  ni- janäni  ..  Ytf.  117;  34,  38,  50,  S4>  S«. 73.  82.  109,  "3.  P-4,  Jj-ia',  16',  38', 32i  361  40;  —  kaimai  .  .  tat  da'inm daysty  hl  atihat  :^airyqn{%A^  a/yamtum Yl  13.  50;  —  avahela  paiti  yqnahe  y  h! da%at . .  pähave  zsvar)  Yt.i6.6i.;  —  aam ai^he  asti  usvamim  y  nä  kasvikamal . .  avarstanqm  naire  . .  ajasta  .  .  daositi  V. if^-ZTi  vgl.  noch  V.7.5'.43  unter3;  —  aval hi  masyS  arüiim  (sd.)  y  iistamm  bun/a- _y.T/V.  7,  71;  —  ä/  zaoiars(sd.)  kairim ankai  .  J  (y)^^  gä'^/'is/a  fi-asravaysiti  . . aat  hävananS  (sd.;  nämL  kairim  attkaC) y  kaom>mca  akunavat..aat*atravaxlahe y'  ätnmca  aiwi.vaxsayät ,  .  N.  72  f.;  74~ j6^.  3)  mit  Opt;    aom    aiäAe   asti
```


## [2026-09-06T14:55:41.589Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hu\\.jasta\\|hujasta\\|hu-jasta\\|jasta-\\|a\\.jasta\\|jai&y\\|jaidy\" BRT.txt | head -30\necho \"=== gad root ===\"\ngrep -n \"^jad\\|jaidi\\|'erbitten'\\|erbitten\" BRT.txt | head -30"
}
```


### [2026-09-06T14:55:41.662Z] TOOL RESULT

```
8047:•  j-.  g-  tätay-''  f.  i)  'Vermögen,  Können, Imslandsein,  Kiaff,  mit  Inf.:  Aat  vf  xsa- :^r^m  kn  'trfi'SS.)  iyao>amli  masda ya>ä *vä  ^kaxmi  (sd.)  asä  vokü  manatikä ^mydidyni  (sd.)  "habt  ihr  die  Herrsch- gewalt, habt  ihr  die  Kraft  lu  tun,  o  M., . .,  o  Asa,  o  VM. . .?"  Y. ^4.5.  2)  'Ver- mögen sva.  Habe,  Besitz,  Gut,  Reichtum'; auch  mit  obj.  und  subj.  Gen.:  mä  yave imat  timiliifm  .  ,  /ratahlt  .  .  x^iiiravatti °ti/  mä  j^ä'hravaiti  äsna  frazaintii  Y. 60.7;  —  äps  °tjm  vS  jaidyämi  pauru.- sars'iqm  . .  *frazaintimla  Y.  (fj.  1 1 ;  —  °tlm pourus.x^a'irqm  .  .  ''frazaintim  Y.  68. 1 1 ; —  kahmäi  °tim  .  .  kahmäi  ainistim  .  . baxsiJni  Yt  10.  108— 110;  —  '/Im  jaio- yanla  . .  molu  pas^aSta  . .  'tlm  baon  sivÜla Yt.5.98;  —  dazdi  ahmJk3tn  . .  'lfm  anum v)r?^r(qmnua  Yt.  ici.33;  —  ydi^a  , .  uz-
11033:yat  asti  airyanqm  daRyunqm  .  .  yatc'a asaons  zaraiuslrahe  ". .  quod  est  .  .  pro- vinciarum  .  .  quodque  (sva.  et)  . ."  YL/p. 56 ;  —  vupe  matnyava  dagva  yaloa  vannya Yt.  Jo.  97;  — y5i  vatjAsus  3  wanatahs iyHntJ  yasca  üitx  Y.Jp.  3;  —  hyat  da xyüo^anä  mJzdavqnisA.)  yä^ä  uxha  ",.fa- cinora  . .  quaequc  (sva.  et)  verba"  Y.  43. S  i  —  *gr}AmS  .  .  avAsuf  tnaraxtarS  ahya yai^a  "GrsAmas  ,.  vitae  deslructores  huius quique  (sunt)",  sva.  "Gr.  et..destnictores" Y._j2. 13; — yeTiyaaUSp.  5730.)  hsrnsmya- sattl(sd.)  mt^ahyä  yäca  hsi  ansua  Y.33. i;  —  yi  iluds  dadsniE  da%ranqm  (sd.) haüa  alätinö  y^siä  .  ,  *drigvü.d3byB  "quae debita  poscanlur..a  hdeti  (quaeque  sva.) et  ab  infidelibus"  Y.31.  14;  —  mainyus spSniStS  .  .  yaecä  xsnao/in  (sd.)  aAurjm "Spiritus  sanctissimus  . .  et  (ii)  qui  satis- faciant  . ."  Y.30.  5;  —  ya  ..  väV)r)zli .  .  yala  vaniaitl  Y.  2g.  4;  —  ya  atirayl .,  urBpayeintX  yäca  xrafä  ..  Y.4S.10; 44-  20; — y7  va  möi  na.,  dayat  ..  yqsca haxiäi  (sd.)  "qui  .  .  vir  , .  faciat . .  et  (ii) quos  .  ."  Y.  4ß.  10;  —  at  ta  vaxiya  .  .ya mazda^a  (sd.) .  ,  humqzdra  (sd.)  als  yeca ya  raocSbis  dansata  urväza  "ea  praedi- cabo  . .  quae  (sunt)  recordanda  .  „  a  bene recordante  una  cum  Asä  quaeque,  quae una  cum  luce  videatur  voluptas"  sva,  "et voluptatem  quae  .  ."  Y.^.  i;  —  zu  c: at  yül  dasva  .  .  yasca  vh  .  .  yazaitl  Y. J2.3;  —  ta  vS  mazda  ..  asäi yecä  tatbyaca'''' ärmaitl  ddi^a  insi  istsisi&A.  mit  No.  2)  xsa- %r>m  Y.$i.2.  o)durcheinenKonjunk- tionssatzmit>'<j^j  oder  Ayat,  dem  ^a  folgt; nur  gAw. :  datd?  galmcä  ajyaitimcä  (beide als  I.Glied;  Sp.567  \x^ya%aca  anhat  aps- m^m {sd.)..  Y.30. 4;  — ia'^a  ,.  zar^m (sd.) ..  carani  *ashiitm  (sd.)  xsmakqm  hyatca mSi  hyäi  Vax!  aslS  Y.  44.  17;  —  hyat vJsSnta  (sd.)  dr>gvant>m  avS  AyaÜa  gäui jaidyai  taraol  Y.32. 14.  e)  das  erste Glied  ist  relativisch  gegeben;  nur  gAw. :  yJ *u>i'qfi?m  mS'i  gairü  (sd.)  . .  dadi  asisca '  Syadiananqm  vidus  V.  28.  4.  f)  das erste  Glied  ist  nicht  ausdrücklich  genannt, vielmehr  aus  dem  Zusammenhang  zu  ergän- zen (s.  Sp,  571  u);  nur  gAw.:  ta  uxiiä  . . maeda  asaica  yufmaibya  gtml ". .  (dir),  o J/., unddem.<4j'ii.."Y.^2.9;  — /ö  d)b>naotä
11538:•  j.  jaidyamna-  Adj.  (fem.  "«3-),  PPM.: s.  gad:
13735:jaidyai  (sd.)   mraol  yS  °j
21242:Formen:  tai  möi  daidr  ahura  hy  mazää rapin(sA.)  tavä  Y.51.  18;  —  neben  einem Objektsakk. :  iahä  . .  sanm  (sA)  caränl.. *äsi»itlm  (sd.)  x/mäAam  kyatcü  mSi /iyät voxs  also  (sd.)  Y.  44. 17;  —  neben  einem Inf.:  Ayal  (zu III)  vTs}nta[sA.)  dngvantftn avS  hyaiiä  gäul  jaidyai  (sd.)  mraol  Y. ^2.14.  b)  im  jAw.;  i)  mit  Ind.;  ia} ahtnai  jasal  äyapUm  y  Alpu^rü  us.zayata Y.5,4;  7,  13,  13;  —  moiu  iai  äs  .  ,  y° fräyatayat  .  .  aoi  zqm  Yt 5.65;  —  altat il ..  aiAhe(ßp.\om)  avayam  *dqtimaM y*  %wä  didvJsma  Y.^Äi;  ' —  i'mai  .  . Stävi/Um  ^yad^tiim  maSya  viminti  .  .  y kainyS  uzvätaydnti  Yt.  ly.  59;  — ya%a/rä toa  (sd.)  amraot  y*  dim  a/iBmisd.ya  .  . adadat  Y.ig.13;  —  ankam  raya  ufar)- natshala  (nämL  asti)  y  bavainti  halat.- pu%rä  Yt/j.  15.  2)  mitKonj.:  avat ayaptim  dazdi  ml  y  bavStii  aiwi.vanyä . . vlstäsptm  ..  ydka  (Sp.  1247  u.)  aztm  ni- janäni  ..  Ytf.  117;  34,  38,  50,  S4>  S«. 73.  82.  109,  "3.  P-4,  Jj-ia',  16',  38', 32i  361  40;  —  kaimai  .  .  tat  da'inm daysty  hl  atihat  :^airyqn{%A^  a/yamtum Yl  13.  50;  —  avahela  paiti  yqnahe  y  h! da%at . .  pähave  zsvar)  Yt.i6.6i.;  —  aam ai^he  asti  usvamim  y  nä  kasvikamal . .  avarstanqm  naire  . .  ajasta  .  .  daositi  V. if^-ZTi  vgl.  noch  V.7.5'.43  unter3;  —  aval hi  masyS  arüiim  (sd.)  y  iistamm  bun/a- _y.T/V.  7,  71;  —  ä/  zaoiars(sd.)  kairim ankai  .  J  (y)^^  gä'^/'is/a  fi-asravaysiti  . . aat  hävananS  (sd.;  nämL  kairim  attkaC) y  kaom>mca  akunavat..aat*atravaxlahe y'  ätnmca  aiwi.vaxsayät ,  .  N.  72  f.;  74~ j6^.  3)  mit  Opt;    aom    aiäAe   asti
25811:'in  lichter  Flamme  brennen,  flammen': saoHntai paiii  ä^ratV.g.^ö; — a%rqmca suxrqm  saocintqm  V.  2.  8,  a)  Kaus. '(inflammare  sva.)  incitare':  gaus  jaidyäi (sd.)  . .  yi  däraohm  saolayat  avS  "das Rind  ist  zu  töten,  damit  es  den  Tod- wehrer'  {d.  i.  Haoma)  ansporne  zu  helfen" Y.^2.i4'>.
=== gad root ===
```


## [2026-09-06T14:55:50.199Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gad\\b\\|gad:\\|gad  \\|s\\. gad\" BRT.txt | head -20\necho \"=== jasta ===\"\ngrep -no \"hu[.-]\\?jasta[^ ]*\\|ajasta-[^ ]*\\|jasta-\" BRT.txt | head -20\necho \"=== search 'gesegnet' ===\"\ngrep -n \"gesegnet\" BRT.txt | head -20"
}
```


### [2026-09-06T14:55:50.299Z] TOOL RESULT

```
5830:•  j.,  g.  ast'vant-  Adj.  (fem.  'vaitt-)  'mit einem  stofflichen  Leib  versehen,  leiblich,  | stofflich,  materiell';  Ayat  'vant»m  dada uäatam  "als  du  Leben  mit  Leib  versahst" Y,_5/.  11;  —  tat  (näml.  mlidf/n)  er  mazdä vairlm  'vaits  ustänät  data  vatfhlus ^ttoiana  manar-ks ySi . .  "diesen  köstlichen (Lohn)  ja,  0  M.,  werdet  ihr  durch  das Wirken  des  VM.  dem  leiblichen  Leben (derer)  verschaffen,  die  . ,"  Y.54. 14;  — •vat  ahm  hyät  uslStiä  (sd.)  aojSrigAvat "^.43-  16;  —  ash-atjrmya%a  astva  *kqm ustanava  (sd.)  °vat  *ai^yeja/nm  paitisät Yt.  13. 1 29;  —  *vTjvähu  (sd.)  paiii  tanusti 'vh  gays  *däryeife  FTVf.4.2.  A)  sonst. nur  als  Beiwort  von  a)  stay-  (sd.) :  zara- , %ustrahe..yS paoiryö  stsis  'vadyä ..  Yt.ij.  1 Sgf«.  b)  gai^ä-  (sd.),  Sg.  und  Plur.J darfsca  (sd.)  da^at^amirixfyantim  vTspatn yam  "vaitlm  gae^qm  Yt  i<).  94;  Y.  g.  8, 37.23,  *Vd.£'>;  —  zarai:mtr5  ratus 'vai>ya  gaf^ayä  Yt.  73.  4r;  j.  89;  — kat»  %wqm  paoiryS  'vai^yäi  hunüta gai^yäi  Y.p.  3;  4;  —  m/l  m?m>cainTs gai>a  'vaitls  asake  SrB._j;  Yt/5.  41,  V. , ^^•SS;  —  "J  ^^  apqm  a'javö..  jasanli..' yavanqm  .  .  västranqm  ,  ,  gafianamüa 'vaitinqm  Yt  ^'.29;  —  V?'"  ■  ■  /rävavacä .  .  zara'iuströ  gae'iabyö  'vaiHbyS  Y.ö'j.g; P.  13;  —  ahura  mazda  mainyö  spinista däiar>  gad'^ariqm  'vaitinqm  asäum  ''" I.  7- 1.  9- 1,  lo- ".  "■  I.  '4-  I,  34,  K
8626:Komp.:  i-s\ig',  S  304  H.  3Ö;  lum  V.  zgad- (sd.  No.  3).
9936:gadötüt-
9942:•  j.*gadötGt-f,'Räubertu[n,  Räuberbande': yat  äjasät  ''ktrisasca  *°tstai'l  dasvllca handramana  Yt.  u.  6.
11537:•  j.  JaiSyant-  Adj.,  PPA.:  s.  gad-.
11538:•  j.  jaidyamna-  Adj.  (fem.  "«3-),  PPM.: s.  gad:
11600:KompE.  —  Zum  V.  gad:  —  PS.:  ia  iädil. j.  jaiui  FrD.  g:  lies  zazus.
28227:•  j.  zgad-,  zgaS"-'*  V.  'fortschwimmen'. Praes.  2  zgma-,  ^aiia-.
30147:lu  zgad:
=== jasta ===
=== search 'gesegnet' ===
14575:gesegnet':  saokqmia  baral-avantam  barat.- aya^qm . .  'Zqm  Yt  ij.  41.       2)  'befriedigt, zufrieden  gestellt':  ytiiAi  nm3naya  sraoSs .  .  'Zs  asti  faili.zanlö  Y.57. 14,         a)  'zu- frieden, wohlzufrieden':  ya%a  aüfir  amavh °%S  fraxslane  z>mä  paiti  Y, 9.  ao;  F.  2^'', Aus  ar,  'tramptha-,  S  24  aE.  —  Vgl,  %ri^fs'.  — ai,  vgl.  ,!r«/(iA'er  wird  Salt', —  Pii.:  ptdannJ), Sü, :  samidäka^.    S.  noch  No,  1.  —  ')  So  in NA.  nur  Yt.  13.  loo;   s.  aber  Pt4  lu  Y.  57, K5  lo  Y.  fl.  —  •)  Pü.  (ßlschlich):  ptdanrt. —  J)  Nach  Ki.fatlx'  la  lesen,  s.  Yt.  /.  az, Mx.  3.  1  (usw.);   aber  SWienAW,  67.  841.  5 »lebt  fiidix  :  xus7.     Wohl    lu  fifav-  (sd.),   also fil  dar  lu   lesen?,   vgl,  np,  baxlyir  nsw,     S. noch  lU  %rima-,  /rap^wa-  und  äyapla-.
30428:•  g.j.'hu-mäyä-,  j.'hu-mayä-(mask.*^a-) Adj.  'segensreich;  gesegnet':  °mälm  i)Wä iilmyazat>m  alatihääm  dadamaidt'aizAeYi segensreichen  setzen  wir  dich  ein,  als  den erfolgreichen  . ."  Y. 41. z;—  yai  hJs  (näml. däman)  'mayaca  liyäca"  äna^amaideVi. 12, 4";  —  'maya  aita  däman  *dähimaide 'maya  clsmaide  'maya  matnyämaide  *yam da^at  ahurS  mazdä  Vr.  72.4'';  —  'maya upar»ha  (sd.)  cllmaide  ahunahe  vairye?u Vr.  12. 2;   —    'maya   nö  buyati
30438:•  j.  humäyö.tara-  Adj.  'der  gesegnetere, glücklichere':  a^a  zT nS  °racd  jiye.tara/a'> anhama  yäts    spsntahe   mainySul  damqn
30439:'yat  hts  hitmayaca  .  .  cina&amatdt  "so wollen  wir  denn  noch  gesegneter  und erfolgreicher  sein  (werden) . ."  Vr.  /2.  4;  — di:a  zT  nS  'ra  at»h9n  kuittaya  (sd.)  atta däman  *d^3maide  Vr.  J2. 4.
```


## [2026-09-06T14:56:07.433Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD hujastag ===\"\ngrep -n \"hu[ˇ]*ast\\|hujastag\\|huǰastag\\|gaǰastag\\|gajastag\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD gadag/beggar ===\"\ngrep -n -i \"beggar\\|driyōš\" PHD.txt | head -20\necho \"=== NYB ===\"\ngrep -n -i \"hujastak\\|hu.astak\\|gajastak\\|gadāk\" NYB_vol2_glossary.txt | head -20\necho \"=== BRT ajasta headword ===\"\ngrep -n \"ajasta-\" BRT.txt | head"
}
```


### [2026-09-06T14:56:07.527Z] TOOL RESULT

```
=== PHD hujastag ===
=== PHD gadag/beggar ===
=== NYB ===
=== BRT ajasta headword ===
```


## [2026-09-06T14:56:10.398Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -c PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt\necho \"=== sample PHD ===\"\nsed -n '600,640p' PHD.txt\necho \"=== grep hu ===\"\ngrep -n \"^hu\" PHD.txt | head -30"
}
```


### [2026-09-06T14:56:10.460Z] TOOL RESULT

```
 340898 PHD.txt
 609465 PHD_mackenzie.txt
 920054 NYB_vol2_glossary.txt
1870417 total
=== sample PHD ===
urwāzistan 85 wādbān
*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
W
wābar [w’Al | M wbr, (N bāwar)] truth; belief. wābarīģān [w?/yk?n' | M wbryg’n) true, trustworthy. “Аһ: trustworthiness. wabz [wpc, wpz] wasp. wačast [wcst! = Av. vwacas-tasti-] strophe (of the Gathas). watéag [wck!, (bck!) | N bacca] child, baby, cub. wad [SL Y.ÀA < A sry’; wt! | M wd, N bad] bad, evil. ^ Áh : badness, evil. маа [w?t! | M wd, N bad] wind, breath, spirit; cal. 22nd day. wadag [wtk'] evil, vile, wicked. ~ih: evil, vileness. wādām [w’t?m | N bádám] almond. wādbān [w°tp’n' | N bādbān] sail.
wad-baxt 86 wānīdan
wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
wünidan 87 warz
~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
warz- 88 waxsig
warz-, —išn, v. warzidan.
warzag [ic k! | (N zvarzāw)] ploughing (ox).
warzāwand [wle'wnd | M wrewynd] having miraculous power, powerful.
warz-büm [wlcbwm] cultivated land.
warzidan, warz- [wlc-ytn' | N ~] work, act, practise; till; beget. ~išn: work, tillage.
warzigar [wlcykl | M zorzygr, N barzigar] worker, peasant.
was [KBD < A kbyr; ws | = M, N bas] much, many, enough.
P wasnād [wsn'd | = P] for, on account of. ;
wāspuhr [w’spwhl] principal.
wāspuhragān [wspwhlk’n'] 1. special, particular; 2. courtier. 7h : speciality.
wassad [wst! | N bussad] coral.
~€n [-ул! | N -in] coralline.
wastar [wstl = Av. wastra-] clothing, garment.
wastār [wst'/ | N bistār] wilful, obstinate; over-confident. Аһ: obstinacy; over-confidence.
wāstar [w’st/] pasture, fodder.
wastarag [wstlg] = wastar.
wāstaryðš [w'stlywš = Av. wástryo.ffuyant-] husbandman. —-їһ: husbandry.
was-téhmag [wstwhmk'] having many seeds.
was-xwüstag [КВ Dhw'stk!] wealthy, rich.
wasyār [wsy(k)l | N bisyār] much, many.
P маб [wš | = P] straw, fodder.
*waSag [wsk! | N ufa?] a kind of beer.
waStag [wétk'] sick, ill. „il: sickness, illness.
iwaštan, ward- [wétn', wlt- | M wštn, wrd-, N gaštan, gard-) turn,
return, wander; change.
~išn, v. wardišn.
*waštan [wštn'] = wārīdan.
waštīh [wstyh] = waštaģīh.
wattar [SL Yti, v. wad | M wtr, N EI worse, bad, evil. -īh: evil, wickedness.
wattom [wttwm] worst.
waxr [w^ hl | (P wxr-)] crooked, distorted.
Iwaxš [й | (M w?x$)) spirit.
=== grep hu ===
399:huniyāģar 45 im rēz
400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
2206:hunsand,
2333:human being dēpāy, mardómzàdag.
2334:humanity mardémih, | mardóm- zadagih.
2335:humble ērmān(ag), értan, narm.
2336:humility ērmenišnīh, értanih.
2337:hump kat,
2338:hundred sad.
2339:hunger gursagih, suy, Suy.
2340:hungry gursag, gušnag.
2341:hunting-ground wiškar.
2342:hurt (n.), v. harm.
2343:hurt (v.) bištan, (bēšīdan), rēšīdan.
2344:hurtful vēškēn.
2345:husband gādār, mérag, Soy.
2346:husbandman wāstaryēš; v. farmer.
2347:husbandry wāstaryēšīh; v. agricul- ture.
```


## [2026-09-06T14:56:19.373Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB jast ===\"\ngrep -n \"jastak\\|ǰastak\\|hujast\\|gajast\" NYB_vol2_glossary.txt NYB_vol1.txt | head -20\necho \"=== PHD asyan ===\"\ngrep -n -i \"āšyān\\|ašyan\\|nest\\b\" PHD.txt | head -20\necho \"=== PHD kandan/kan ===\"\ngrep -n \"^kandan\\|kandan,\" PHD.txt | head\necho \"=== HRN asiyan / gulsan / kasane ===\"\ngrep -n -i \"äsiyän\\|äsyän\\|asiyan\\|gulsan\\|gulšan\\|käsäne\\|kasane\\|Nest\" HRN.txt | head -20"
}
```


### [2026-09-06T14:56:19.478Z] TOOL RESULT

```
=== NYB jast ===
NYB_vol2_glossary.txt:4647:Barthélémy GA = Gujastak Abalish. Texte pehlvi publié pour la premiére fois, avec traduction, commentaire et lexique par A. Barthélémy. Paris 1887. Bibliothéque de l'École des hautes études, sciences philologiques et historiques, soixante-neuviéme fascicule.
NYB_vol1.txt:606:3 V. the little Pahlavi treatise edited by A. BAgTHÉLÉMY: Gujastak Abalish. 
=== PHD asyan ===
13:THE need for even a short Pahlavi-English dictionary has been obvious for many years, particularly to would-be students of the language. The glossarial part of Professor H. S. Nyberg’s Manual of Pahlavi is still eagerly awaited, five years after the publication of Part I, although the ‘archaistic’ tradition of transcription followed therein is no longer universally acceptable. With the partial material at present available, every serious student still has to compile his own dictionary, a formidable task with Pahlavi and made more so by the plethora of different systems of transcription in print. The present dictionary, admittedly introducing yet another transcription, is intended first to relieve the stranger to Pahlavi of the necessity of covering what is now well-travelled ground—the commonest 4,000 simple words— without a unified map, and secondly to urge the practical value of this ‘Sasanian’ transcription for his journeying further. To have included etymologies and textual references would have changed the emphasis of the work, turning it from a map to a historical atlas-cum-gazetteer, besides retarding its appearance unduly. Such a complete dictionary of Pahlavi is nowhere within sight and must remain so until many more texts are adequately edited.
42:Pahlavi letters are often distorted, or joined irregularly, in such a way that they coincide with other letters, so producing even greater ambiguity. The commonest distortions are here noted by under- or over-lining the letter value intended. ‘Thus:
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
2301:honest frárón; v. righteous.
2548:lair āšyān.
2908:nest āšyān(ag).
5295:daštān daštūnmūh daštānestān dašt, yašt yastan jadárih nišīn-!
=== PHD kandan/kan ===
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
1581:destroy abesihénidan, (afsénistan), gugān-, kandan, murnjénidan, wanidan, wimuštan, wināhidan, wišuftan.
5007:kandan, kardan kardagān kardagār *kardag, kūdak kardespās
=== HRN asiyan / gulsan / kasane ===
740:35. äsyäne, äsyän 'Nest'.
1162:Im Sähnäme reimt ist *stehe* auf nest, ist also est zu
7025:Darinesteter, Et. ir. I, 85.
8533:981. ^nest 'betrunken* 0-
8972:1034*>*» niseni *Nest* (Sahn. I, 137 Vers 146), nisemen i).
8975:hört dazu etwa auch äsyäne *Nest' (No. 35)?
9215:päz. nestj nesU,
9218:nester 'Lanzette'.
12740:küneste 81.
```


## [2026-09-06T14:56:29.409Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '735,760p' HRN.txt\necho \"=== HRN 1034 ===\"\nsed -n '8968,8985p' HRN.txt\necho \"=== HRN qand ===\"\ngrep -n -i \"qand\\|kand 'Zucker\\|Zucker\" HRN.txt | head -20"
}
```


### [2026-09-06T14:56:29.487Z] TOOL RESULT

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
=== HRN 1034 ===
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
=== HRN qand ===
286:pand auf qand^ was man kaum damals qend aussprach, zu
3538:np. teberzed (arab. tabarzad) ist Zucker, 'der so hart
9851:Geschichte des Zuckers, S. 10, 11), die Übernahme
```


## [2026-09-06T14:56:36.599Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9835,9870p' HRN.txt\necho \"=== HRN sekker ===\"\ngrep -n -i \"sekker\\|sakkar\\|khanda\\|khand\\b\" HRN.txt | head -20"
}
```


### [2026-09-06T14:56:36.671Z] TOOL RESULT

```
und eine solche glaube ich durch die an np. en(/
bieten zu können — so wird man gr. e/LintQ ohne
viel Bedauern preisgeben können. Wie so manche
anderen Wörter aus italischen Dialekten in das
Lateinische aufgenommen worden sind — z. B. bös,
sabellisch (Bersu, Die Gutturalen und ihre Ver-
bindung mit V im Lateinischen S. 139, vergl. auch
Stolz, Latein. Grammatik- S 47 Anm. 1), pahimhes,
popina, oskisch (Stolz, 55 46 Anm. 3), rüfns^ stßlus
etc. (Stolz, J5 54:^ '^5)» die mit / beginnenden Worte
lingiia, lacruma, levir etc., sabinisch (II. Seymour
Conway, Indog. Forsch. II, 157 folg.) u. a. m. ~
so ist vielleicht auch apis oskisch es Lehnwort. In
Bruttium, Lucania, Messana wurde oskiscli ge-
sprochen, Sicilien war das Honigland, der berühmte
Sitz der Bienenzucht (vergl. E. 0. von Lippmann,
Geschichte des Zuckers, S. 10, 11), die Übernahme
des oskischen Wortes in das Lateinische wäre also
durchaus nicht befremdlich. Allerdings bleibt -mp
sonst im Oskischen erhalten (vergl. R. von Planta,
Vocalismus der oskisch-umbrischen Dialekte, S. 307),
aber auch bei der Zusammenstellung mit spnl^^ ergiebt
*) Ai. admasäd' (G e 1 d n e r , Vedisohe Studien II, 1 79 folg ) passt
mehr auf die Fliege oder Wespe (wenn das ädnui- Obst ist) als auf
dip Biene.- - 2r>() —
sich für das Lateinische dieselbe Schwierigkeit, das
Schwinden des m zu erklären; Bu gge versucht dieses
letztere BB. XIV, 70. Ahd. imbi 'Bienenschwarm',
mhd. imhe *Biene* sowie gall. amella *Bienensug
(Wh. Stokes, BB. IX, 194) haben, wenn meine Ver-
mutung richtig ist, nichts mit np. eng, lat. (osk.) apis
zu schaffen; doch ist es bisher auch noch nicht
geglückt, dieselben in einer irgendwie befriedigenden
Weise mit apis zu vereinigen.
Zu np. eng etc. seien noch täl. äng und kauk.-
bergj. heng 'HummeV hinzugefügt.
=== HRN sekker ===
```


## [2026-09-06T14:56:43.491Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN candy ===\"\ngrep -n \"^candy\" KLN_1966.txt | head\ngrep -n \"khanda\\|khaṇḍa\\|kaṇḍa\\|qandi\\|qand\\b\" KLN_1966.txt | head -20\necho \"=== SKT candy ===\"\ngrep -n \"^CANDY\\|CANDY\" SKT.txt | head\necho \"=== LKT qand ===\"\ngrep -n -i \"qand\\|kand (\\|khanda\" LKT.txt | head -20"
}
```


### [2026-09-06T14:56:43.606Z] TOOL RESULT

```
=== KLN candy ===
6342:candy,  n.,  crystallized  sugar.  —  Shortened  fr. sugar  candy,  fr.  F.  (sucre)  candi,  fr.  It.  (zucchero) candi(to),  ‘sugar  candy’,  fr.  Arab,  qandi,  ’crys¬ tallized,  candied’,  adj.  formed  fr.  qand,  ‘cane sugar',  which,  like  OI.  khandakah ,  ‘candy  ,  is prob.  of  Dravidian  origin.  Cp.  Tamil  kantu, ‘candy’,  kaftu,  ‘to  harden,  condense’, candy,  tr.  and  intr.  v.,  to  crystallize  into  sugar.  — Formed  fr.  prec.  word,  on  analogy  of  F.  candir, ‘to  candy’,  back  formation  fr.  candi,  ‘sugar candy’,  which  was  mistaken  for  a  past  participle. Derivative:  can-di-ed,  adj. candytuft,  n.,  name  of  a  plant.  —  Compounded of  Candy,  obsolete  form  of  Candia,  ‘Crete’, and  tuft.  Hence  candytuft  lit.  means  ’tuft  of Crete’.
6339:upright',  fr.  candere,  ‘to  shine,  glow,  be  white  , which  is  cogn.  with  Gk.  xavSapo;,  ‘glowing coal’,  OI.  candrah,  ‘shining  glowing’,  candana ‘sandalwood’  (lit.  ‘wood  for  burning  incense’). Alb.  Gheg  hqne,  Tosk  hene,  ‘moon’  (lit.  ‘the white  one’).  All  these  words  derive  fr.  I.-E.  base *(s)qand-,  *(s)qend-,  ‘to  shine,  glow’.  Cp.  W. cann,  ‘white,  bright’,  OBret.  cant,  ‘white’, MBret.  cann,  ‘full  moon’,  which,  according  to Pedersen,  are  not  cognate  with  L.  candidus,  but loan  words  fr.  VL.  *candus,  contraction  of  can¬ didus  (see  haplology).  Cp.  candle,  candelabrum, candidate,  chandelier,  chandler,  Cicindelidae, incandescent,  incense,  sandalwood,  sandarac, sanders,  santal.
6342:candy,  n.,  crystallized  sugar.  —  Shortened  fr. sugar  candy,  fr.  F.  (sucre)  candi,  fr.  It.  (zucchero) candi(to),  ‘sugar  candy’,  fr.  Arab,  qandi,  ’crys¬ tallized,  candied’,  adj.  formed  fr.  qand,  ‘cane sugar',  which,  like  OI.  khandakah ,  ‘candy  ,  is prob.  of  Dravidian  origin.  Cp.  Tamil  kantu, ‘candy’,  kaftu,  ‘to  harden,  condense’, candy,  tr.  and  intr.  v.,  to  crystallize  into  sugar.  — Formed  fr.  prec.  word,  on  analogy  of  F.  candir, ‘to  candy’,  back  formation  fr.  candi,  ‘sugar candy’,  which  was  mistaken  for  a  past  participle. Derivative:  can-di-ed,  adj. candytuft,  n.,  name  of  a  plant.  —  Compounded of  Candy,  obsolete  form  of  Candia,  ‘Crete’, and  tuft.  Hence  candytuft  lit.  means  ’tuft  of Crete’.
=== SKT candy ===
=== LKT qand ===
8792:jarcJ7i  1762 jaiac  1778 sai'ca  1780 saZ  1802 ^alitru  1567 qandrama  1948
```


## [2026-09-06T14:56:58.699Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=raw.split('\\n')\nprint('leaf of 6342:', '\\n'.join(lines[:6342]).count('\\f'))\nEOF\necho \"=== LKT Kandis ===\"\ngrep -n -i \"kandis\\|Zuckerkand\\|1141\\.\" LKT.txt | head -20\necho \"=== AFM qand ===\"\ngrep -n \"القند\\|قند\" AFM_pages.txt | head -20"
}
```


### [2026-09-06T14:57:00.478Z] TOOL RESULT

```
leaf of 6342: 132
=== LKT Kandis ===
1470:'Zuckerwerk'  [aus  pers.  pänid,  Vb.  fänl- dän' den  Zucker  rafSnieren',  s.  SCHWARZ in  ZDMG  LXXIV,  238  u.  245];  hieraus mit  ar.  Art.  und  häufigem  Wechsel  von t  und  k  sp.  alfenique,  pg.  alfenim  'Teig aus  Zucker  und  süßem  Mandelöl',  frz. alphenic  'Kandiszucker,  Teig  aus  Mandeln und  Zucker';  frz.  penid  'sucre  tors';  in der  alten  Pharmazie  saccharum  peni- dium.    [DE  112.    Devic  DEt  27.
2504:105!2.  Ar.  kandl: Adj.  zu  kand  nach  ar.  Originalwörter- büchern  'eingedickter  Zuckerrohrsaft', wahrscheinlich  durch  zweimaliges  Ko- chen erzielter  'Rohrzucker'  [SCHWARZ in  ZDMG  LXXIV,  244];  hieraus  it.  zuc- chero  candl,  frz.  sucre  candi,  sp.  azücar cando,  pg.  candil,  dtsch.  Kandiszucker, ndl.  kandij,  engl,  kandy,  Jcandtj-sugar ; dazu  die  Vb.  it.  candire,  frz.  candir  'über- zuckern', kat.  candir  'Früchte  ein- machen' ;  dtsch.  kandieren  'verzuckern', Konditor  'Zuckerbäcker'.  [DE  247. Eguilaz  358.    ML  (3899.
2685:1141.  Mal.  käyulängit:
5787:Äafta?e  977 iCrtöajg  993 iCa^eZ  766 Zaö(//e  979 ^Tad«  984 ifßtZjne  989 i:fl/f  992 Kaffee  4005 ^^//fe;-  992 Ka filier  j.  1150 Kaftan  774 Kaj>'put(öl)  1142 Kakadu  1Ü17 Kolbehasit  St.  1026 Kalbelazguar  St.  1025 Kalbolacrab  St.  1026 kalekutischer  Hahn  1031 kalemine  mhd.  1149 Kalender  1024 Kalenter  1024 kalfatern  1022 Kaliber  1030 ifaZ//"  798 A'rtZiX-o  1031 Kalium  1029 ifaZ/e  j.  1035 ifaZo«^  1038 Ar<?jjrtfc  1039 Kamel  653 Kamelie  653 Kamelhaut  653 Kamelot(t)  653 Kampfer  1100 Kandare  1051 kandieren  1052 Kandis  fzuckerj  1052 Kantschu(k)  1042 iCao/in  1060 Kap(p)ern  978
=== AFM qand ===
1531:رتككى وجن اثاجى ' وفي بعض الاماكن « قنديل اغاحى 809 اغاجى وقره
3152:(الشَان) القسطاس 3 توزن بها الاشياء. القند تعريب كبآن وبقال فين 0
3301:فقل ان القندأوَ + الغليظ والسئ 2 الخ معرب عن > 502 ؛ القدم
3305:4 القند زر متوف قندن ومعنا كاب الله والستن مرت د ويم
3318:5 5( مالي يقال 4 قندز 35 ني ماده 1 وان
3324:وفي اللسان:« القندل بوزن جعفر الطويل ٠»‏ وهذا أصح لاله تعريب كندواله وفعناة
3899:فالمعدلي. مصلل عله في 5 من جبال سمرقند وفي 55035 - | بر
```


## [2026-09-06T14:57:09.241Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (131,132,133):\n    pg=t[i]\n    print('leaf',i,'nums:',re.findall(r'\\b2[0-9]{2}\\b',pg)[:10])\n    print(pg[:150].replace('\\n',' '))\nEOF\necho \"=== AFM around 3295-3315 ===\"\nsed -n '3295,3312p' AFM_pages.txt"
}
```


### [2026-09-06T14:57:11.441Z] TOOL RESULT

```
leaf 131 nums: ['228']
  camel with  suff.  -eer. Camelidae,  n.,  a  family  of  ruminants  (zooi.)  — ModL.,  formed  with  suff.  -idae  fr.  L.  camelus. See  camel. Cam
leaf 132 nums: ['230']
n or  index  (of  the  sundial)’,  OL.  gnoscere,  L.  nds- cere,  ‘to  know’,  Alb.  heh,  ‘you  know’  (sing.), hoh,  ‘I  know’,  OSlav.  znajq,  zn
leaf 133 nums: ['232', '233', '241']
  days.  —  L.  caniculdris,  fr. eanicula.  See  prec.  word  and  -ar. Canidae,  n.  pi.,  the  family  of  dogs,  wolves,  foxes and  jackals  (zoo
=== AFM around 3295-3315 ===
الرجال وقيل هو الكبير العظي الرأس الصغير الل م الهزول :0 :8
لمقدم والقصير العنق الشديد 0 س ٠‏ وقيل هو 00 والصلب. ٠ ٠‏ وخلاصة الى
راحقة كايا الى معنى الكلمة المونامة ܝ يننا 00 والمد. مر واللصض
والداهية وامري || لخو 0 5 ع ܘ ܪ ܐ من التصحيف فان الستداو
صقت | 37 والسندر والسندري » . .قلت ܕܠ ܟ ان القددأو 1:5
والعندأوَ مشتقّة من الفارسي ܨ ومعناه الغليظ الضخم 03906 2030
فقل ان القندأوَ + الغليظ والسئ 2 الخ معرب عن > 502 ؛ القدم
ܝܢ ܘ و 0 اميا ا مشجيع ٠‏ .1 ابرق 50 10700
تمعربة 95 ومعناه املف 05
0 -_- فس < تكلب لاه يلاها مدن ادن
4 القند زر متوف قندن ومعنا كاب الله والستن مرت د ويم
خصية ܐܐܝ قال في البرهان القاطع : 9 قنز على وزن 9 اسم ولابة في الهات
المطلة. ܕܝ 0 اسم ܦ ܬܝܬ بالعاب 0 فاتك 1150 17 من جلده فراء
2 تليسها السلاطين ويصمّع ܘܬ 0 ܐܨܒ ٠‏ وقيل الَّهُ يشبه الكل وهو
كثير الوجود في ܨ 33 ٠دقيل‏ هو كاب الماء ٠٠‏ وان ما يسمه الاطباء بجند سدسار
خصية هذا الحيوان ٠١»‏ راجع هذه اللفظة ) ٠وقال‏ ايضاً : « أكتديَكٌ ܝܫ الدال
ܟܙܡ ري شد
وفتح 5 التكلى يقال له ® ܢܗܟ ( 90 5 9 2 <
```


## [2026-09-06T14:57:32.670Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v2 leaf 174 (printed ~717) ===\"\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in (173,174,175):\n    print('--- leaf',i)\n    print(t[i][:1500])\nEOF"
}
```


### [2026-09-06T14:57:34.450Z] TOOL RESULT

```
=== v2 leaf 174 (printed ~717) ===
leaves 684
--- leaf 173
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


  
--- leaf 174
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

                              ‫() 
--- leaf 175
                                                    ‫بیان بنحم‬
                           ‫لفت‬   ‫خای نقطه دار باجیم مشتمل بر ده‬                           ‫در‬


‫باشد ‪ -‬ونام کلی حم هست (‪ )۲‬زردرنگه ومیان‬                      ‫خحا ره = سم‌اول بروزن‌شماره‪ .‬بمعنی‬
‫تب میکویند؟ ‪۰‬‬                        ‫مشود‬                     ‫ول باشد ‪ - ۱‬و بمعنی تسخر‬
                                                                                     ‫لی‬‫اند وقکم‬
                                                           ‫و مسخرکی هم آمده است ؛ و بفتح اول ایز‬
                                                    ‫ا‬                                                        ‫گفته‌اند ‪.‬‬

‫بفتح اول بر وزن کفش »‬                ‫ححشس‬

‫عردم‬        ‫وکاوی‬   ‫گردن‬   ‫آماسی و گرهی‌باشد که در‬
                                                                   ‫وبواو زده * آواز وصدای هرچیز رگاویند ‪.‬‬
‫نماند بزر گك تر‬        ‫نکند وهرچند‬      ‫بهم رسد و درد‬         ‫بفتح اول و سکون ثالی‬                 ‫خحچ؟ =‬
                                                ‫‪.‬‬   ‫شود‬       ‫در گلو‬                  ‫رجیم فارسی ‪٠‬‏ ورم ا‬


‫ححاك = بفتح‌اول‌بروزن کجك» بمعنی‬                              ‫؛ وباینمعنی‬        ‫بهم رسد ؛ وعم ارل حمامده ‪۱‬ست‬

                                                                   ‫(‪. )۱‬‬     ‫ت هم هت‬      ‫محای جم فارسی ا‬
‫قطه باشد ‪ -‬وشالیرا یز گوبند که با سرچوب‬
‫و نقطه وخال‬         ‫‪ 5‬باالگشت دست درزمدن گذارند ‪-‬‬             ‫خحته
```


## [2026-09-06T14:57:45.203Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,pg in enumerate(t):\n    if 'خجسته' in pg or 'ججسته' in pg:\n        print('leaf',i, pg.count('خجسته'))\nEOF"
}
```


### [2026-09-06T14:57:47.153Z] TOOL RESULT

```
leaf 213 1
leaf 593 1
```


## [2026-09-06T14:57:52.388Z] TOOL CALL #34: Bash

```json
{
 "command": "sed -n 1,40p tools/ref_page.py 2>/dev/null | head -40; echo ---; python3 tools/ref_page.py --help 2>&1 | head -30"
}
```


### [2026-09-06T14:57:54.050Z] TOOL RESULT

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
---
Fetch ONE cited page of a scanned reference, on demand.

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
```


## [2026-09-06T14:57:56.369Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1776 --image 2>&1 | tail -40"
}
```


### [2026-09-06T14:57:58.309Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1776.png
REF: BQT:1776  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 573  OCR-lang: fas

۱ کجیل ۱۷۷۹
محله‌ایست در تبریز , و لام قبرستانی هم هست | علیه‌الرحمه درآن قبرستان است ‎٩‏ ۰
بیان ششم
درکاف فارسی با جم فارسی مشسّمل‌برسه هت
گچ۲ < بفتح اول وسکون ثانی, خاکی | بکمانچه۴ -
اشد که آنرا پزند وبدان خانه سفیدکنند . گلچه؟ - بنتح اول وئانیمخفف: کیرا
گچات - بکر اول. بروزن و معنی | کوبند که زبان اوبفساحت جاری نباشد ؛ وباین
غجك است وآن سازی‌باشد ممروف ومشهور(٩)‏ | معنی باتشدید ثانی هم بنظر (۲)آهده است .
بیان هفتم
در کافی فارسی با دال احد مشتَمز اس دوازده لفت
کل - بفتح اول وسکون نانی » بمعنی کوبنده . 4
کدا باشد که گدایی کننده‌است- و کدایی رایز گداده - بنم: اول بروزن‌شمارهبالاخانٌ
() چش : - ومشهور . (۲) خم ۱۱:,- بنظر .
- اکنون محله‌ای درتبریز بنام محلهٌ کجیل اززهی هست. وقبرستان گجیل هم‌ممروف
بوده؛ واباغ گلتان» درمحلآن قبرستان ایجاد شدماست . تذ کرمولف‌راجع بقبرشمی‌تبریزی‌قابل
تخل است. ۴ - پهلوی » پازند 826 . معرب‌آن جص, سربانی 86858 ۰ كلمةٌ عریی - فارسی
حسن 80510[ (8(05010) ازبونانی8۳0908. 8121091808 آمده «هوبشمان *۸۹» ور4:
امشق ۰۸۹۰ کردی 811762 «زابا ص۳۹۲ > و8360 (آهك) «ژابا ص۳۵۷ ؛ در اکدی82550 <-
جیصین,کلی«معجمیات عربیه - سامیه ص۲۱۸ ور: کج. ۴ نچك ۳ غرل «فرهنگه نظام»:
زهر مو چو ن گچك: میکرد فرباد دل اصحاب میگشت از غم‌آراد,
خوارزمی « فرهنگه نظام » .
ای - رد رشیدی. در سیزوار 756 بمعنی شخ سکم عقل تاضیح ونیز لفظی است که‌با
آن بزها را میخوانند ۰ ۸« فرهنگه نظام » - 8 - بمعنی گدایی است » رك :کدا :
شکرت چو آرزو شد ز لب شکر فروشش چو عبای دوس زو تر ز شکن فروش کدکن.
مولوی «فرهنگه‌نظام». ورك : رشدی .
- بکسر اول (در لهجه مرکزی) » دراوستایی 820 (خواهش کردن.خواستن).
هندی باستان 811411 ( من خواهش میکنم ) « بارتولمه 2۸۷ > » کردی 2 42 ( کدا)
«زابا ص۳۵۷ 2 » کیلکی 4 - قس : عربی : تکدیه , و اکداه؛ آنکه از دیگران چیزی
(پول » خوردلی ویوشیدی) برای رفع حاجت طلید : «گفت (ملك) این گدای شوخ مبذر را ...
برانید . » «کلتان ص ۳۱ . بقیه درحاشيةٌ صفحهٌ ۱۷۷۷
```


## [2026-09-06T14:58:14.233Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1544 2>&1 | tail -30"
}
```


## [2026-09-06T14:58:14.821Z] TOOL CALL #37: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:717 2>&1 | tail -30"
}
```


### [2026-09-06T14:58:22.735Z] TOOL RESULT

```
را نیز کوبند - و بقتح اول بمعنی فراهم فدرون [ هم هست - وکنایه از شب تاريك باشد چه قندز
باشد - ودرعریی بمعنی‌ناز وغمزه است که‌ممشوقی | شب 8 سیاهی شب راکوبند؛ وهر کاه کویند «با
بعاش ق کند ۲ ض قندز آرد» مرادآن باشد که بشب آورد و شب
توت ت__-<<-<-<--- <<

(۱) خم ۱: برو .

۱ - بکراول وسوم و نیز بفتح اول وکسرسوم خاکی سرخ کونه که ازشهربرفه‌آرند.
رك : دزی ج۲ 4*۹ « قنبیل چیزیست شبیه پرنگه‌مکه زرد مابل بسرخی وکوبند شب‌بمنست
که در بمن بخاك مخلوط گشته بآن شکل میشود » ونزد بعی تشم نباییست» ار چمع ی کوبند تخم
سرخس است...» « تحفةً حکیم موْمن ». مابرهوف کوید: کرد ۴881212 (فر) که قرمز رنکه
است وروی میودهای گیاه 10010۶12 3801116۶2 بسا 18و01062االنطم ۷12110105 را
می‌پوشاند ۰ این گرد از در باز درهندوستان شرقی‌شناخته بود ۱ وآنرا 2 ۳2 ,0۱112 ۸270
مینامیدند وقنبیل ازهمین‌کلمه ماخون است « عقار ۰۳۲۷ ۲ - محرف (عر) « غنج‌بالم
وطمتین » کرشمه وناز . » « منتهی‌الارب ». و رك4 : تاج‌العروی و لان‌العرب .

۴ - قدز مخفف فهندز معرب کین‌دز (ه.م.) است . ۴ - فندز ( بنم اولوسوم)
«قندوز» رکی « فهرست‌مخزن‌لادوید ‎ »‏ قندس «تفی» « دزی » < کندی ۳ کندزه‌تفس»
08516۳ ( سکه آبی . کلب‌الماه ‏ پیدستر ) « دزی احاض 4۱۶ > «فولرس >.

8 - صبح فنك پوش را ابر زره درقبا برده کلاه زرش قندز شب را ز تاب .

. « خاقانی شروانی . دبوان ۲ >.
قند - بفتح اول . معرب «کند» از اسل هندی است.در سانسکریت ۷138418 یمعنی

مطلق قطعه باپاره مخصوصاً پارژفند پاتکهٌ قند. همین کلمه وارد زبانهای اروپایی‌شده:62861(ف)»
۷[ ( انگه ) , (۳۵۵۵ ( آلم ) , 62۵8010 ( اتالیایی ). درین زبانها کلمات مر بور
بچیزی گفته شود که ما درفارسی کنونی تبات کویم ؛ قند عبارست ازشکر غاب ربخته و سخت
وکلوخ شده «* هرمزدنامه ی ۲۳۷۲
```


### [2026-09-06T14:58:24.433Z] TOOL RESULT

```
no scan of BQT covers printed page 717 (see 'scans' in refs_online.json)
```


## [2026-09-06T14:58:35.236Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (176,177,178):\n    print('=== leaf',i)\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-06T14:58:37.324Z] TOOL RESULT

```
=== leaf 176
 ‫ضا‬
  ‫با سوختن و راه رفتن در دست وایعاو‬                            ‫خجنك = نماول وفتح ثانی سوکون‬
                                                              ‫نون ودال ابجد ‪ 0‬نام قصبه‌ایت درماوراءالنهر که‬
                                         ‫‪.‬‬   ‫بهم رسد‬
                                                          ‫‪۲‬‬                              ‫مولد کمال است ‪٩‬‏ ‪:‬‬
‫اول و انی بتحتانی‬
  ‫»|‬    ‫=‬    ‫‪۷۳1‬‬
                            ‫حجیر "‪۰‬یکر‬
                                  ‫‪۴‬‬          ‫‪2‬‬


                                                               ‫_ بن اول و ثالی» در نذه است‬        ‫خجی؟‬

                                                              ‫گویند‪.‬‬   ‫که لآرا چکاو کے خوانند و بعربی قبره‬
‫وجمیل وخوش صورت وصاحب حسن راگویند ؛‬
                          ‫ویضم اول هم آمده است ‪1‬‬              ‫خجو له بکر اول و فتح ثانی و لام‬
                                                              ‫وسکون واو »آبله گروانندکه ببب کارکردن‬


                                                   ‫بیان ششم‬
            ‫درخای نقطه دار ‪ ۳‬دال بی نقطه مشممل بر شانزده لغت و کنات‬

 ‫‪-‬دوای؟ جم اول ‪ ۰‬نام ذات | وصاحب ومالك را نگیوزبند ؛ وبا ذال نقطه‌دار‬
                                                                    ‫خداً خ‬
                                      ‫بارتمالی است همچو الهواله ‪ -‬و مخقف خود؟" | هم خوانده‌اند ‪.‬‬
                                                                                              ‫‪1‬‬




                                                   ‫(‪ )۷‬چك‪ .‬چش‪ :‬جوئی‪.‬‬               ‫(‪ )۱‬خم‪ -: ۱‬و‪.‬‬
  ‫روزه راه‬         ‫ده‬   ‫‪ ۰‬من آن و ‪-‬مرقند‬         ‫‪ - ۱‬شهری مشپور بماوراء النهر بر ساحل سبحون‬
  ‫در ‪ ۱4‬درجه و ‪ ۳۲‬دققهة‬               ‫ت‬
                                      ‫س)‬‫اوس‬
                                          ‫است « ممجم‌البلدان ‪ :‬خجندة » و اکنون در ترکستان (ر‬
      ‫‪ - ۴‬ظ‪ .‬مصحف«چفو»‬          ‫عرض شمالی و ‪۸٩‬‏ درجه و‪ ۲4‬دققة طول‌شرفیه ضمیمهةٌ معجم البلدان»‪.‬‬
  ‫بهلوی ‪rhic‬‏ ‪( uh -‬از ‪ :‬هو (خوب ) ‪٣‬‏ چهر(اصل نژاد ) ‪.‬‬                            ‫هرژ=ر‬
                                                                                      ‫هج‬          ‫(«‪.‬م ) ‪= ۴‬‬
   ‫اوستا_‪-»3601)1‬ل‪0‬ا«بارتولمه ‪۱۲۸۱٩‬‏ نبیر گے ‪»۹۰۱‬طبری ‪( ۲1[06‬خوش» خوب‪ .‬زیدا) «واژه‌نامه‬
  ‫‪ .‬دامفالی نیز ×‪٣[0‬‏ ‪ ,‬شهمیرزادی ‪7[1205‬؛ لفة نيك نژاد ‪ .‬خوب اصل و مجازاً بمعانی‬                            ‫‪۳‬‬
  ‫‪ ۴‬ب۔هلوی متأخر ‪: . ۷2۸۵۷۲‬هلوی
=== leaf 177
 ‫خدرگه‬                                                                                                     ‫‪a Ah‬‬


‫اول‌بروزن مهره » خرده‬         ‫حدره =‬                         ‫زراق که بظاهر خود را بیارایند‪ -‬وآلهایی‌را فیز‬
‫رىز هرچیز را گویند رک وشرارة آتش‌را لز‬‫و‬                      ‫‌دشدادو لمرود؛‬      ‫عابنییکر‬‫یخد‬
                                                                                           ‫دی‌‬
                                                                                             ‫نوا‬
                                                                                               ‫گونن که دع‬
          ‫گفته‌اند ؛ وبفتح اول همآمده اش‬                         ‫وآنها راخدای فروشان هم میگوبند با دوتحتانی‬
‫خدك ‪ .‬بفتح اووئانی بروزن کجك‪.‬‬                                                                                    ‫ورف‬
‫مطلق پل را گوبند خواه باسنگف وخشت وکچ‬                        ‫تون‬     ‫حجد او ند ‪ ۱‬ب‌ بقتح واو وسکون‬

 ‫بر رودخانه بندند و خواه با چوب وخاکد‬                                 ‫‪۰‬‬   ‫را کوند‬    ‫انه‬    ‫ویز رگ‬        ‫صاحب‬   ‫‪1‬‬   ‫ودال‬

                                 ‫بر جوی (‪# . )۱‬‬
                                                             ‫مزر گد‬        ‫بادشاه‬       ‫‪ ۴‬س‬     ‫حدایگان‬
‫سمعنی‬
    ‫بر وزن عشرنی ‪۰‬‬           ‫‪°‬‬
                                                                                            ‫وخداوند گار اعظم باشد‪.‬‬

‫بروزن بپلنگه‪ ,‬نام درختی‬      ‫‪-‬‬        ‫‪۱‬‬
                                                                 ‫حدر نق » بفتح‌اول وئانی‌بروزن‌خورنق‬
‫است بیارسخت که از چوب آن‌نیزه وتبروژین‬                       ‫بلغت رومی و بعضی گوبند بونانی عنکبوت را‬
                                                            ‫گوبند ‪ ۴‬؛ وباین‌معنی بجای نون بای حطی حم‬
                                          ‫میکویند ‪. ۷‬‬                                                ‫بنظر آ مده اف‬

                                                                               ‫(‪)۱‬چك» چش‪ :‬جوئی‪.‬‬
                            ‫وند (یوند اصاف) بمعنی صاحب (مطلقا) ‪:‬‬                    ‫‪+‬‬       ‫ا‬‫د‪:‬‬
                                                                                              ‫از‬‫‪ ۱‬خ‬
  ‫‪۶‬لتان ‪. ۸۳‬‬
           ‫گ‬                        ‫درتهند‬      ‫ر‬   ‫دست‬   ‫کنان‬    ‫لماش‬         ‫جاه‬          ‫ویشند‬
                                                                                                ‫
=== leaf 178
     ‫‪۵‬ف‬

 ‫‪۴‬‬      ‫باشد‬    ‫بزرگه و خداوند خانه‬        ‫و کدخدای‬       ‫بضم اول و الی و سکون‬       ‫خدو ‪- ۲‬‬
‫کودبانوی خاله را نکبفزته‌اند (‪)۱‬؛ وبفتح اول‬                ‫وأو » آب دهن راگونند که از آثر مزةٌ چیزی‬
                                                                                            ‫‏‪Ey‬‬
                                                          ‫ْم اول بروزن سلو کك»‬     ‫کّ خدو ك و‬
‫جدیو * ‪ -‬بکر اول و الیوسکون‬
 ‫تحتالی مجهول و واو پادشاه ‪ -‬و وزیر س‬                     ‫پراکنده و پریشان شدن طبیمت باشد از امور‬
                                                          ‫‪ -‬وفهروخشم‪-‬‬     ‫ناملام ‪ _۴‬ویمعنی رشك وحد‬
 ‫ونگانةً عصر باشد ِ‬     ‫وخداوند کار ‪ -‬و بزرگه ‪-‬‬
                                                          ‫وخجلت وشرماری نیز آهده است ‪ -‬و بمعنی‬
                                                                          ‫آزردگی وعصهٌ بیجاخوردن ه‬
‫اول وثالی وفتح رابع‬     ‫»‪ -‬بكر‬   ‫حد بور‬
                                                          ‫؛ وبفتح‌اول‬   ‫همت‬
‫یمعتی خدیو است که‬          ‫و سکون رای فرشت ‪۰‬‬                                              ‫نیز گفته‌اند ‪۲‬‬
 ‫پادشاه ‪ -‬ووزیر ‪ -‬و خداوند کار ‪ -‬وبزرگه ‪-‬‬                  ‫حد بر ه بفتح اول بروزن وزیر» بمعنی‬
                            ‫وبگانةً عصر باشد ‪٩‬‏ ‪۰‬‬
                                                           ‫حن امت که خوب ‪ -‬وخوبی ‪ -‬و خوشدلی ‪-‬‬
‫وتح‬
  ‫حد به = بکراول وسکون تانی ف‬                                                         ‫وخوش خلقی باشد‬
‫تحتالی ‪ ۰‬بمعنی مضاف است که در مقابل مطلق‬                   ‫خد یش ‪ -‬بضم‌اول کوسرثانی وسکون‬
                                               ‫باشد ‪. ۷‬‬    ‫تستالی مجمول و شین قرشت ‪ ۰‬بمعنی پادشاه‬



                                                                            ‫(‪ )۱‬چش ‪:‬گوند‪.‬‬

      ‫‪ = ١‬خو (ه‪.‬م‪« ).‬اسفاا‪ ۲ :‬ص ‪ = 64‬خذوك (بفتح اول ونيز طم آن ) ر‬
  ‫(ك‪: ‎‬‬
                          ‫ع‪ .1‬مانوی‪012۷۷ ‎‬‬
                                         ‫‪4 K1‬‬
                                            ‫لفت فرس اسدی ص‪ " ۹٥۲) ‎‬درسغدی‪W ‎‬‬
          ‫)‪(Henning, sogdian loan words , BSOS. X. 1 . 94.‬‬
   ‫؟‪ ‎‬درقرای اطراف فزو‪.‬ن ‪ ( 1002‬اضطراب وغم وحزن ) ( ازافادات‌علامه دهخدا)‪‎.‬‬
                                               ‫رکنف جوم‪‎‬‬
                                                       ‫خن ن‬
                                                          ‫‪ ۴‬اف سیف سد رات‬
                ‫ز آنکه خد
```


## [2026-09-06T14:58:55.035Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[175])\nEOF"
}
```


### [2026-09-06T14:58:57.082Z] TOOL RESULT

```
                                                    ‫بیان بنحم‬
                           ‫لفت‬   ‫خای نقطه دار باجیم مشتمل بر ده‬                           ‫در‬


‫باشد ‪ -‬ونام کلی حم هست (‪ )۲‬زردرنگه ومیان‬                      ‫خحا ره = سم‌اول بروزن‌شماره‪ .‬بمعنی‬
‫تب میکویند؟ ‪۰‬‬                        ‫مشود‬                     ‫ول باشد ‪ - ۱‬و بمعنی تسخر‬
                                                                                     ‫لی‬‫اند وقکم‬
                                                           ‫و مسخرکی هم آمده است ؛ و بفتح اول ایز‬
                                                    ‫ا‬                                                        ‫گفته‌اند ‪.‬‬

‫بفتح اول بر وزن کفش »‬                ‫ححشس‬

‫عردم‬        ‫وکاوی‬   ‫گردن‬   ‫آماسی و گرهی‌باشد که در‬
                                                                   ‫وبواو زده * آواز وصدای هرچیز رگاویند ‪.‬‬
‫نماند بزر گك تر‬        ‫نکند وهرچند‬      ‫بهم رسد و درد‬         ‫بفتح اول و سکون ثالی‬                 ‫خحچ؟ =‬
                                                ‫‪.‬‬   ‫شود‬       ‫در گلو‬                  ‫رجیم فارسی ‪٠‬‏ ورم ا‬


‫ححاك = بفتح‌اول‌بروزن کجك» بمعنی‬                              ‫؛ وباینمعنی‬        ‫بهم رسد ؛ وعم ارل حمامده ‪۱‬ست‬

                                                                   ‫(‪. )۱‬‬     ‫ت هم هت‬      ‫محای جم فارسی ا‬
‫قطه باشد ‪ -‬وشالیرا یز گوبند که با سرچوب‬
‫و نقطه وخال‬         ‫‪ 5‬باالگشت دست درزمدن گذارند ‪-‬‬             ‫خحته ‪ = ۲‬ض‌اول وفتح‌ثانی‌وسکون‬
               ‫سقدیرا یز گوبند که درچشم افتد ‪.‬‬                 ‫سین بی‌نقطه وفوقانی‌مفتوح» بمعنی‌مبارك ومیمون‬
                                   ‫(‪ )۲‬چس ‪ :‬کلی است‬                      ‫آمده است‪.‬‬      ‫)‪ ۱‬چكڭ» چش‪:‬‬



  ‫درق را بپانزده هزار دینار [ک] بنتدلد درمدتی خجاره»‬                       ‫‪* - ۱‬رباز فروختن او یمی‬
 ‫= هو = خوب )‬              ‫از‪ :‬خ ( بشو‬      ‫‪۴‬‬             ‫خجش(ھ‪.(.6. .‬‬       ‫‪۳‬‬    ‫‪۳‬‬            ‫«ئارىخ سستان‪۹۸۳‬؟‪.‬‬

      ‫جته؛ اوستا ‪uh - [2052‬‏ « اسفاا ‪ :‬ص ‪۷٩.‬‏ از ربشه اوستابی‪ ( )[028(02‬خواهش‪.‬‬
                                                                             ‫‪+‬‬
  ‫‪.‬‬    ‫ابر لندی ‪uidiug‬‏ (خواهس میکنم)» در ترحجمه و تفسس بهلوی ‪natsahZ‬‏‬                      ‫کردن ‪ ۰‬درخواستن)‪.‬‬

      ‫ه« بارتولمه ‪ .»۷۸4‬خجته لفة بمعتی تك‌خواسته ‪ .‬متبرك » مبارك؛ ضد «گسسته»‬                                    ‫‪0‬‬
                                                                       ‫رك‪ :‬همیثه بهار‪:‬‬         ‫‪۴‬‬             ‫(ملعون)‪.‬‬

                      ‫بر ربخت فرابةً می حدری‬                           ‫بربرك سپید باسمین تر‬
                     ‫بر گردن کوتشز پرعطری‪.‬‬                             ‫جنبید سر خجته تتوالد‬
  ‫« منوچهری دامفالی ‪۱٩*.‬‏‬                                                             ‫خجج (ه‪.‬م‪).‬‬    ‫=‬   ‫‏‪e‬‬



                                                                                                ‫بقبه از صفحهٌ ‪۹۱۷‬‬
      ‫است‬    ‫وسط آن م نجرف‬    ‫اما چون‬     ‫کشت‬        ‫عاج وی‬   ‫‪.‬‬   ‫شمالی دیده مشود‬        ‫درحه عرص‬       ‫‪6‬‬     ‫درحجنوبت‬

                                           ‫و دلدان امل ماوی‬         ‫بکارمیرود‬     ‫فقط برای ساختن اشاء کوچك‬

                                           ‫مزبوررا گاه درتر سنات بکاربرلد ‪ ۰‬دندان هر دور درفرون وسعلی‬

                                            ‫بعنوان سنگه‌محك برای‌تشخیص وجود زهر در غذا بکار میرفت‬
             ‫بروال و ختوی آن‬                                   ‫»اروی بزر که»‪.‬‬
                                                                            ‫« دائرة المعارف بریتانیا «ل‬
```


## [2026-09-06T14:59:17.140Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,pg in enumerate(t):\n    if 'آشیان' in pg or 'آشيان' in pg:\n        print('leaf',i)\nEOF"
}
```


## [2026-09-06T14:59:17.611Z] TOOL CALL #41: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2395 2>&1 | tail -25"
}
```


### [2026-09-06T14:59:18.725Z] TOOL RESULT

```
leaves 777
leaf 12
leaf 257
leaf 268
leaf 271
leaf 377
leaf 446
leaf 514
leaf 607
leaf 733
leaf 774
```


### [2026-09-06T14:59:26.537Z] TOOL RESULT

```
۹ - دراوست 2ط(ع)5(80ی180] . ممنی لفظی اين‌کلمه بقول پوستی دردام‌نامذایرانی
چنین است : کی که منازل خوب فراهم سازد. ینام مرکب‌از: هوش + هنگه. چنانکه برخی
پنداعته‌اند لیست. . هاید قول فردوسی که گوید:

گرانمایه را نام هوشنگه بود توگفتی همه هوش وفرهنگه بود .

«شاهنامة بخ ج۱ ص۰۱۹
سبب لغت سازی و وجه اشتقاق عامیانهٌ من کود شده باشد درهر جای اوستا ( باستشنای فروردین
بشت) که ازهوشنگك ذ کری رفته » باصفت 0278011812 بعنی پیشداد باد شده؛ وپرشداد بِضی
کی که درپیش فالون گذارد ودادگری مود با اول واضع فالون (رك : پیشداد). رك: پورداود.
بشتها ۱ ص۹-۱۷۸. داستان هوشنگه درشاهنامهٌ فردوسی (بخ۱ ج۱ اص۲-۱۹) آهده است.

۴ - این معانی برساختهٌ فرقةٌ آذرکیوان است « در نامه آلین داد » نام وخشور دیوبند .
طهمورت آمده که «وشنگه بای هوز مضمومه بواو «جهول وشین منقوطه بذون زده وبکاف عجمی
موفوف امراول راکوبند ولیز بمعنی هوش وخرد وآهنگه وادبست (ظ. ادب) آمده.» « شارستان
چوار چمن ص۲۹*. ۴ - ر4: ح۱. ۴ - این معنی با نام او- چنانکه درح۱ گفته
شد - ارتباط دارد . * - همه شاهان باستانی درنظر فرقهٌ آذرکیوان پیفه‌برند . شارستان
چپارچمرم عنوان ترجمهٌ احوال هوشنگه را چنن آوردم : ۸« ذکر افطل‌الایاء وخشور شهنشاه
هوشنگه» «دارستان چمارچمن ص۲۹ ‎٩‏ - برساخته فرقهٌ آذرکیوان .

۷ -ار4: ح ۱ ورك: پیشداد . ۸ - همان مفهوم اول است . رك : ح۱ :۰

. ‏ظ. برساختهة فرقهٌ آنرکپوان‎ - ٩
```


## [2026-09-06T14:59:40.343Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[257])\nEOF"
}
```


### [2026-09-06T14:59:41.896Z] TOOL RESULT

```
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
تحريك نماید - و سکون را بعنی سرشته کرد
وبهم بر آمیخت و تحرزيك نمود و برانگیزانید .
] غار۵ن س فتح دا و سکون نون .
یعنی سرشتن وبرانگیزانیدن و تحريك نمودن -
وفرو شدن و فروکردن هم باشد بزمین و غیره .
غار بدن - بروزن پاشایدن. بمعنی
آغاردن اس ت که سرشتن و تحربك نمودن وغبره
باشد - و فرء کردن نم بود بزمین با بر جای
۳
آغاز ب,بازای نقطه‌دار بروزن آواز .
بىمنی صدا و ندا باشد - و ابتدای کارها را نیز
گویند - و بمنی ضصد واراده هم آعدماست ۳ -
و امربایین عمتی هم هست نی قصد کن و ارادء
نمای . 3
آ غاه - بروزن‌آوازه ‏ دست‌افزارست
کفش دوزانرا - و دوالی را نیز گوین که مابن
چرم و روی کفش دوزندنا آب و خاكبدرون کفش
نوّود .
] غاز یف - - بکسر زا وسکون تعتانی
و دال ؛ بعنی ابتدا کرد و قصد و اراده نمود .
آغار بدن بروزن آشامدن » ,سنی
قصد و اراده نمودن - و اتداء کردن.
آغال - بسکون لام » پیشی آشفته
کردایدن و برآشفته ساختن باشد شخسی را بر
۴ - ۷۵۲۱۱۵۱۵۸۵ 5ز۳۱۷۵۳۵۵.
نی نوخود کی‌مرء آن‌باش ی کهخودرا چون‌خلیل
```


## [2026-09-06T14:59:49.322Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[256][-2500:])\nEOF"
}
```


### [2026-09-06T14:59:50.950Z] TOOL RESULT

```
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
کله 212۳ و ننوا 101۷610 پابتخت آن بودند . نضت باجکگزار دوأت بابل بود ولی بمتعا
ستقل شد . نضتی پلدشاه آشور تکلات بالازار 168124101212226 اول است که در حدود
۰ ق . م سلطنت داشت. وی قوم هتیرا مفلوب کرد ودر کتیبه‌ای میبالد که ۲ لت وشاهان
آها را مفلو بکرده . دوات آشور در زمان سلسلهٌ بارکن ۲۲۲ - ٩۱۰‏ ق .م » باعلی درجهٌ
شوکت رسید . سناخربب پسر سارکن (۷*۵ - 5۸۱) بابل وبخش اعظم فیلیفیه را تصرف کردو
بمصر سپاه برد . آسوربانی بال ( ٩۲۹ - ۹۹٩‏ ) در عیان شهرباران آشور بیمانند است . وی
مصرو کلدء و عیلام را عسخر کرد . چون بنیاد حکومت آشور بروحشت و هرای ود وم مثل
نابعه وهی‌جوار ازاو نفرت داشتند وبنابراین دائماً یه
باهم هتحد میشدند ورات‌طفان برهی افراشتنک.
دولت آشور از بی جنکید بنیه‌اش تحلیل‌رفت .
چنانکه چندهال پي از مر کث آسوربانی پال‌قوم
سکه 564206 از ارویا حر کت کرده شام راساد
تطاول داد . ماد و بابل این سانجه را غنیمت
دانستند و پآشورتاختنبد ؛ نیلوا پایتخت را سخیر و با خالیکسان و دولت یدز عنقرض کرد ند
٩۱۲(‏ ق . م) « تارخ ملل شرق و یونان . آلبی‌ماله و ژول ابزاك . ترجمهةٌ حزبرص ۸-۹ .
( فصو یر) هنر آشور :۷- شکارشیر»- آسور بانی‌پال۳- فرشته درتعقیب غول4- آسودنات سیرپلا
۵ باد جنوب‌غربی» برنجین ۹- فهرمان درحالخفه کردن شیر ۷- شیربر نجین ۸ شیرمادشمجروح.
```


## [2026-09-06T15:00:09.906Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:00:09.915Z] TOOL RESULT

```


```


## [2026-09-06T15:00:11.983Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1707\" BRT.txt | head -5\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,pg in enumerate(t):\n    if re.search(r'\\b170[5-9]\\b',pg):\n        print(i, re.findall(r'\\b17[01][0-9]\\b',pg)[:6])\nEOF"
}
```


### [2026-09-06T15:00:13.979Z] TOOL RESULT

```
28383:1707  iayana-  —  äoiSrö.pana-  1708
928 ['1712', '1706', '1707', '1708']
929 ['1709', '1712', '1700']
```


## [2026-09-06T15:00:17.252Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28383,28420p' BRT.txt"
}
```


### [2026-09-06T15:00:17.314Z] TOOL RESULT

```
1707  iayana-  —  äoiSrö.pana-  1708
'Nett*(?;  1.  Hbk.  PSt.  101,  Horn  GIrPh. /b.'aÄ  bätmmaiti  /•  vyOvaiti  bärn^B  ". .  zur .'.■f^™L«?^':  "«^"N.''r  ''ä/^^''  7>^n^  F«"de  (der  Menschen)  .  ."  Yt  J7.6. Jy.  m.d  A>.  1 ')  D.  i.  x/^.,  S  IsÄ  n  b ;  ..  No.  ..       ^"■"  ^-  '-^''-  "  ^e'"  "^''■^■■ 3.  — »xisUmiDI,  wenn  ricblig,  MS  den  Formen  P-  *""■  '■  '*^  ^■
mit  «r.  «i*,  S  «S;  Wsch  S  jj-  i-  —  <>  So  •  j.  älma-  m.  'Schluck':  5«f  !7j  •man «»!."""  '?^*''-.  ^  ''"'°^'  *  '"-^'u'  "■  ~  >/  '■■*  ^•<^-  ■  upa„Aarxaaa  V.5  51. '
S)    Hds.  iititi   mit  Pa.  manun;    oosicber.     —        %„„  v     -  s  j-      rr_  1,'  \-  1
«  XA.  J,>y  i   ..  .b„  J  No.  6  .nd  V.  3,.  3.       ä".!- 'C  ~     fc    tj  ZS^ '  ~  ^
—  7)  So  E  I.     VgL  Ol.  kfayama,  dos  »ich  lu  ^
/ocama  wieaL>'j/Jmai?iD  j-atamaiatverhält;    •     j-     älman-     IL     TCot,     ScheJsse':      'ma
E.  die  ai.  Konjunktive  i/ayak,  ifayat.  —  ^)  Die    F.  Jg.
Bed.  nach  P&.:  afiar  mäniht  Atnä.  —  9)  Pn,:  ■       Vgl. /r<ijji«(r<i-i).  —  PSL: /^iwf.in  Aw.-Buchit.
afar  mänind.  3.  Plur.  _  ■)  frisch  Btic  Stod.  3.  9.
•  j.  layana-  n.  'Wohnstätte,  Aufenthalt,!  P-  '^y^™  *<>-  f-  gemeint  Ut  hyiHm,  s. HeimatC  Sp.  .717  o.  No.  ..
KompE.  ~  «nn.  LW.  ifn  'Dorf'.  '  •  j.   ■ä^n^l   F.  5.
,,  „  Pü.:  In.
•  1-,  g.  'sav-  V.;  s.  unter  nyav-.  ■     ,  .t  ,.
°  -^  •  j.  hmna-  n,  'Zier.
•  j. 'sav-V.,  nur  mit  fl/a*! 'ritzen'.  Praes.3       KompA.  (a.  aiimnS,'],  —  El? Ä*«-.  j.  •«:  s.  »-ia-  L
wXh^i^-.hBimqmtqmaiwihalmwrya  »  \.  ia  ..  vupa  dämqn  paifi.vamai  »»So
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
•  J;  I^^ .-"/■'  "''.*'''"  '".*""."'  ''''.^'  *"""-  i  ^'Ä'-:  -^>r^-  -  •>  Kein  »elbständige»  Wot., Sich  behaglrch':  ^fl^fl  «J  öw^affi  /•  «an^       sondern    aus    einem    Komp.    losgelöst,    TgL
anO  Y.Ö'o.  IJ'>;  *F.5".         |      üArS.baxia-  usw.;  Bthl.  1F.  //.  S- ):  lam.  '"^^'n  NA.^i"  1'  i  •  i-  ä5i*r5.baxta-  Adj.  (fem.  -W-)  'den '  Hds.  saiiö.    Besiimmting  un-  (einzelnen)   Heimstätten   zugewiesen,^  be- !  stimmt' :   apqm    napas?  th  aps  . .  'tä   vT-
'sich  zu  freuen':   iala  s'',l"'x/aitt  Yt.Ä'.34-
```


## [2026-09-06T15:00:43.508Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%AF%D8%A7",
 "prompt": "Give the full Persian (Classical/Iranian Persian) entry for گدا: etymology, meaning, any Middle Persian/Avestan antecedents, and any note about Arabic borrowing (تكدية/كدية). Quote the etymology verbatim."
}
```


## [2026-09-06T15:00:44.966Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%AC%D8%B3%D8%AA%D9%87",
 "prompt": "Give the full Persian entry for خجسته: etymology (Middle Persian, Avestan forms), meaning. Quote verbatim."
}
```


### [2026-09-06T15:00:50.212Z] TOOL RESULT

```
# Persian Entry for خجسته

## Etymology
The page notes: "(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)" No Middle Persian or Avestan forms are provided.

## Meaning
The word is an adjective with the primary definition: "fortunate, auspicious"

## Example Citation
A usage example from circa 1260s by Rumi is included: "Very fortunate the sin which the man committed: do not rose-leaves spring from a thorn?"

## Derived Terms
- خجستگی (xojastegi) - meaning "auspiciousness"

**Note:** The etymology section explicitly lacks the Middle Persian and Avestan information you requested. This historical linguistic data is not included in the current Wiktionary entry.
```


### [2026-09-06T15:00:50.308Z] TOOL RESULT

```
# Persian Entry for گدا

## Etymology
The Wiktionary entry states: "Compared with Avestan _gaδa_ ('robber'), Pashto _غل_ (ǧal, 'thief'), although the Middle Persian reflex of this root is [script needed] (gēg, 'thief')."

The entry does not mention Arabic borrowing or the terms تكدية/كدية.

## Meaning
**گدا** (gedâ) functions as a noun with two primary definitions:

1. **Beggar; supplicant** — The primary literal sense, illustrated with classical Persian poetry examples from Hafez (c. 1390) and contemporary usage.

2. **Stingy person; miser** — A figurative sense denoting someone miserly or unwilling to give.

## Pronunciation
- Classical Persian: /ɡaðɑː(j)/
- Iranian Persian: /ɡedɒː/

The entry demonstrates the word's presence across Persian dialects (Dari, Iranian, Tajik) with corresponding pronunciation variations.
```


## [2026-09-06T15:00:59.315Z] TOOL CALL #49: WebSearch

```json
{
 "query": "Persian گدا gadā etymology Avestan gaδa robber Hasandust beggar"
}
```


## [2026-09-06T15:01:01.967Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor w in ['گدا','خجسته','قند','گلشن','آشیان','هوشنگ','آکندن']:\n    hits=[i for i,pg in enumerate(t) if w in pg]\n    print(w, hits[:12])\nEOF"
}
```


### [2026-09-06T15:01:06.676Z] TOOL RESULT

```
Web search results for query: "Persian گدا gadā etymology Avestan gaδa robber Hasandust beggar"

Links: [{"title":"BEGGING - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/begging-pers/"},{"title":"Avestan - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/Avestan"},{"title":"گدا Meaning in English » گدا in English","url":"https://urdutoenglishdictionary.com/%DA%AF%D8%AF%D8%A7-meaning-in-english/"},{"title":"Aeshma","url":"https://en.wikipedia.org/wiki/Aeshma"},{"title":"GĀH - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/gah/"},{"title":"City University of New York (CUNY) City University of New York (CUNY)","url":"https://academicworks.cuny.edu/cgi/viewcontent.cgi?article=1201&context=qc_pubs"},{"title":"دیوانه / dēvāna - واژه‌باز / vājabāz - WordPress.com","url":"https://vajabaz.wordpress.com/2020/04/30/%D8%AF%DB%8C%D9%88%D8%A7%D9%86%D9%87-devana/"},{"title":"BAGA i. General - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/baga-an-old-iranian-term-for-god-sometimes-designating-a-specific-god/baga-i-general/"},{"title":"www.cambridge.org","url":"https://www.cambridge.org/core/product/492A05DE1E05B5006DBBA4DA151D1F3D"}]

Based on the search results, I found some relevant information about the Persian word گدا (gadā) and its etymology:

Persian gadā means "beggar, begging", and this word has been borrowed into Arabic. The Arabic mokaddī (abstracts: takdīa, kodya "begging") is clearly derived from Persian gadā "beggar, begging".

Regarding the Avestan connection you mentioned, the search results do provide evidence of an Avestan root related to robbery. From Avestan gaδ- there is attested Sogdian γδ- /γaδ-/, found in forms meaning theft, with related nouns for 'theft'. This suggests a connection between the Avestan gaδ- (robber) and the Persian gadā (beggar).

However, I was not able to find specific information about "Hasandust" in the search results. If you have additional details or sources about this term or reference, I could search for more information to provide a more complete answer about the etymological connections you're asking about.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-06T15:01:08.626Z] TOOL RESULT

```
leaves 545
گدا [123, 172, 375, 481]
خجسته []
قند []
گلشن []
آشیان []
هوشنگ []
آکندن [65]
```


## [2026-09-06T15:01:15.791Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/begging-pers/",
 "prompt": "Quote verbatim everything the article says about the etymology of Persian gadā 'beggar' and about the Arabic words mokaddī, takdīa, kodya, and any Avestan/Middle Persian antecedents."
}
```


## [2026-09-06T15:01:17.007Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (481,375):\n    idx=t[i].find('گدا')\n    print('=== leaf',i)\n    print(t[i][max(0,idx-900):idx+900])\nEOF"
}
```


### [2026-09-06T15:01:17.894Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:01:19.639Z] TOOL RESULT

```
=== leaf 481
[pdf page 482]
۹
مه مهتر / ۴۳۸۳
لاتین (/712بمل): ,۸۸610 هتیت (4177778): 1106۸۰
فرائسه (ا888(/0: 3 انا
اسپانیایی (32۸15[7): دا انا پسگشت‌ها 5
ایتالپایی ((طل7): 11( و 2۶050000
آلمانی کهن ((227۵4۸ الا (ا0): 0 (0۸613) تدارا مت
لدم شا 1 (۸/8۲۸310) ۰ قل2لاقق لا
آلمانی (058۸4۸): قرده دا برهان قاطع + یدیما
یادداشت.
چم این واژه در ارمنی: گدایی کردن.
اوستایی (/(4۳37: ,۱۳۸2۸0۲1 ,۸1۸820 گرتیکه (0072/0): 8ا[211
۵ ایسلندیکهن (0۵(/0/0۸0 )+
پارسی باستان (۳8۵/(۷ 010): ۴۲۲۵
۸ ۸ ۸819 ۸3,۹۸1 ۹۸1۸7777۷ ساکسونی کهن (540(0 0۲0): ۰ ,2/1811
پهلری (/( ان ۳): ,۸1۸۹1151 ,۱۸9 ,۸4833 آلمانی کهن (0872/۸2 1024ظ 010):
ادا : 167177 11113711
کردی (8015]1)): 3 ان انگلیسی کهن (84/ل800 010): ۰ 341۳8
افغانی (پشتر) (/47011۸(7): ۸ انگلیسی (/8۸05): ۰ بقلآ۷11616 ,1111678
تخاری ۸ (۸ ۸0 70277۸): 1۸ از اب۱۲
تخاری 8 (8 ((4ل7052۸). ۸ دانمارکی (2۸(/377): ان نان ان ۱
بچهر . سانسکریت (7ل54//568): ۸ سوندی (570521587): ده نی ۱۱
ت و ۷۸۵13۲ نروژی (40ا ۰:۵۵ ۱5 ,۱6۷5
ارمنی (/(1۸4//ظ/۵/۸: ۹۹ * بدا ایرلندی کهن (للفن۸/ صا0): 31۸165 ,11۸06
پرنانی 0280): ۰ 118047,017 ,1186۸8 گالی (لل5للهه): ۳10
لائین 77 1۸01878 ,۱۸۵۲۷۵ ولزی (5]7ل5/): ان ۱یا
فرائسه (270/7ق/8: ی ان برتونی (8786700۷): 8878
اسپانیایی (52۸137): زد ونان آلبانی رامزبیمهتم: ۰ 1۸2111 بل ۸«
ابتالیایی (74۵۸۷): زین ان
=== leaf 375
[pdf page 376]
۲- شاید واژه‌ی انگلیسی 811۸۸18 و واژه‌های همریشه‌ی آن در زبان‌های ژرمنی هم از همین ريشه باشند.
پهلرق (1ا2۸): ترا ادن 007۸
کردی (574/)): ندادن ساکسونی کهن (/(24:0 ۰:00 0107۸
بلوچی (اقلنال8۸): آلمانی کهن (/(4ل022 ۷/07 صا0):

را 6 81102۸6 ۰ . 1027721 ۰"
سانسکریت (5۷87077): آلمانی (6570/۸01): نان
8 01101[ " انگلیسی کهن (40ط2۸0 0ا0): 801027084
آرمنی (47487424): 100 انگلیسی (4ل5/ا8(/0): 00
یونانی (24ق07): نروژی (/(۸۷08۲801۸: دی نی
۹ 7 ,621818
لاتین (/4712): داد اند پسگشت‌ها رگد ی
فرانسه (۳8(70): 100 7 20020
اسپانیایی (3ق52۸(۷/3): 3 زار 4 (۲۵۵) +8407
ایتالیایی ((فلله): 00 9 (ق۸) تراد کم
پرتغالی (۳0877010295): ای زدل زد 3 (۲0-۲0) :0102/5
گرتبکه 007/0 لا نی 4 (۵۸۵) 7
ایسلندی کهن ‏ (01041۸2/(م5 صا0): برهان قاطع : ۱۶۷
یادداشت:
۱- هیچگدام از پسگشت‌های من اشاره‌ای به خریشی واژه‌های ایرانی این فهرست با دیگر واژه‌های این فهرست
ی نکرده‌اند و بهمین دلیل جلو واجریشه‌ی هند و اروپایی (شاید) آورده‌ام. :
۰ ۲ چم این رازه در زبانهاي رومانس و پونانی و انگلیسی: ذوب کردن» آبسان کردن.

چم این واژه در زبان‌هاْْرفنی: جاری شدن.
اوستایی (45897427): نان اوستی (05987/2): عم
پهلری (۳۸/]4۷7): 537 کردی (]8/15/). ادا ان
```


## [2026-09-06T15:01:28.996Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.iranicaonline.org/articles/begging-pers/' --note 'page 212, root Gwhedh, Persian gedā -> Arabic takaddī' 2>&1 | tail -20"
}
```


### [2026-09-06T15:01:33.762Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/da5e5294d5401bbf.txt
```


## [2026-09-06T15:01:36.299Z] TOOL CALL #54: Bash

```json
{
 "command": "grep -o -i -n \".\\{500\\}gad[aā].\\{800\\}\" /home/sfmqrb/git/rishe/data/verification/sources/web/da5e5294d5401bbf.txt | head -5"
}
```


### [2026-09-06T15:01:36.360Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:01:38.699Z] TOOL CALL #55: Bash

```json
{
 "command": "wc -c /home/sfmqrb/git/rishe/data/verification/sources/web/da5e5294d5401bbf.txt; head -60 /home/sfmqrb/git/rishe/data/verification/sources/web/da5e5294d5401bbf.txt"
}
```


### [2026-09-06T15:01:38.785Z] TOOL RESULT

```
2147 /home/sfmqrb/git/rishe/data/verification/sources/web/da5e5294d5401bbf.txt
URL: https://www.iranicaonline.org/articles/begging-pers/
FETCHED: 2026-09-06T15:01:33Z
STATUS: 200
TITLE: BEGGING - Encyclopaedia Iranica

BEGGING - Encyclopaedia Iranica Skip to main content 
 Search Iranica...

 search in 8,977 entries of Encyclopædia Iranica. 

 Close Search 

 search 
 account 
 Menu 

 Explore 
 News & Events 
 Editorial Current Board 
 Former Boards 

 Authors 
 Style Guide 
 About About Iranica 
 Ehsan Yarshater 
 Advisory Board 
 Board of Directors 
 FAQ 
 Contact 

 Donate 
 search 

 account 

 BEGGING

 Browse Iranica 

 BEGGING

 Last Updated November 10, 2016

 Print Detail Vol. IV, Fasc. 1, pp. 80-84

 Published December 15, 1989

 Print

 cite 
 share 

 BEGGING, Pers. gadāʾī , takaddī (Ar. also kodya , takdīa ), soʾāl .
 i. In the early centuries of the Islamic period 
 ii. In Sufi literature and practice 
 iii. In later Iran 

 Bibliography

 Cite this article
```


## [2026-09-06T15:01:42.981Z] TOOL CALL #56: Bash

```json
{
 "command": "for u in 'https://www.iranicaonline.org/articles/begging-i/' 'https://www.iranicaonline.org/articles/begging-in-the-early-centuries-of-the-islamic-period/'; do python3 tools/fetch_source.py \"$u\" --note 'page 212, Gwhedh, Persian gedā -> Arabic kodya/takdīa' 2>&1 | tail -3; done"
}
```


### [2026-09-06T15:01:51.821Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/56de61c5abdf368c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8667cdf9f91b0e2e.txt
```


## [2026-09-06T15:01:54.420Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 56de61c5abdf368c.txt 8667cdf9f91b0e2e.txt; do echo \"== $f\"; head -5 $f; grep -o -i \".\\{300\\}gadā.\\{600\\}\" $f | head -3; done"
}
```


### [2026-09-06T15:01:56.077Z] TOOL RESULT

```
== 56de61c5abdf368c.txt
URL: https://www.iranicaonline.org/articles/begging-i/
FETCHED: 2026-09-06T15:01:48Z
STATUS: 200
TITLE: BEGGING i. In the Early Centuries of the Islamic Period - Encyclopaedia Iranica

okaddī (abstracts: takdīa , kodya “begging”), found in adab literature (e.g., in Jāḥeẓ, with his Ketāb ḥīal al-mokaddīn , cf. Ch. Pellat, “Nouvel essai d’inventaire de l’œuvre ğaḥiẓienne,” Arabica 31, 1984, p. 149, no. 148) from the 3rd/9th century on­wards, and this is clearly derived from Persian gadā “beggar, begging” (see C. E. Bosworth, The Mediaeval Islamic Underworld. The Banū Sāsān in Arabic Society and Literature , Leiden, 1976, I, p. 40, II, p. 244; Pellat, “Mukaddī,” in EI 2 ); while the post-classical Arabic verb darwaza “to wander round, beg,” whence motadar­wez “beggar,” goes back either to Persian darvāza “gate” with the idea of going round begging from door to door (see Dozy, Supplément aux dictionnaires arabes , I, p. 438) or to Persian daryūza from (Parthian) yūz – “to seek” (Persian jūy -). Moreover, among the Banū Sāsān, the generic name for the beggars, rogues, quacks, t
== 8667cdf9f91b0e2e.txt
URL: https://www.iranicaonline.org/articles/begging-in-the-early-centuries-of-the-islamic-period/
FETCHED: 2026-09-06T15:01:51Z
STATUS: -1
TITLE:
```


## [2026-09-06T15:02:02.553Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0ed%CA%B0-",
 "prompt": "Does this reconstruction page exist? Give the gloss, the descendants (especially Avestan/Old Persian, Greek, Old Irish, Slavic), and any references (Pokorny page)."
}
```


## [2026-09-06T15:02:03.578Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/candy",
 "prompt": "Quote the full etymology of 'candy' verbatim, including the Arabic, Persian and Sanskrit forms and dates."
}
```


### [2026-09-06T15:02:08.846Z] TOOL RESULT

```
# Proto-Indo-European Root *gʷʰedʰ-

**Yes, this reconstruction page exists.**

## Gloss
The root means "to request, pray, ask for."

## Key Descendants

**Greek:** Ancient Greek πόθος (póthos) and ποθέω (pothéō)

**Old Irish:** geiss ("curse, taboo") and guide ("prayer")

**Slavic:** Proto-Slavic *žę̄dàti and related forms in modern Slavic languages

**Baltic:** Lithuanian pasigèsti ("to miss") and gedė́ti ("to mourn")

**Germanic:** Proto-Germanic *bedō ("request, plea")

**Sanskrit:** गाध (gādha, "desire, cupidity")

## References

The page cites three scholarly sources: Pokorny's *Indogermanisches etymologisches Wörterbuch* (1959, page 488), Derksen's *Etymological Dictionary of the Slavic Inherited Lexicon* (2008, page 560), and Rix's *Lexikon der indogermanischen Verben* (2001, page 217).
```


### [2026-09-06T15:02:09.975Z] TOOL RESULT

```
# Etymology of "Candy"

According to the Online Etymology Dictionary, the word "candy" originates from the late 13th century. Here's the key linguistic journey:

"late 13c., 'crystallized sugar,' from Old French _çucre candi_ 'sugar candy,' ultimately from Arabic _qandi_, from Persian _qand_ 'cane sugar,' probably from Sanskrit _khanda_ 'piece (of sugar)'"

The term traveled westward through multiple language families—beginning in Sanskrit, passing through Persian and Arabic, then entering Old French before arriving in Middle English. The sense of the word expanded over time, particularly in American usage by the late 1800s, to encompass any sugar-based confection rather than just crystallized sugar specifically.
```


## [2026-09-06T15:02:17.608Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%AF",
 "prompt": "Give the Persian and the Arabic entries for قند: etymology (Sanskrit khaṇḍa, Middle Persian, direction of borrowing between Persian and Arabic), meanings, and derived terms. Quote verbatim."
}
```


## [2026-09-06T15:02:19.127Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%84%D8%B4%D9%86",
 "prompt": "Give the Persian entry for گلشن: etymology (what is the second element -شن, any Avestan/Middle Persian antecedent), meaning. Quote verbatim."
}
```


### [2026-09-06T15:02:24.077Z] TOOL RESULT

```
# Persian and Arabic Entries for قند

## Etymology

**Sanskrit Origin:** Both entries trace to Sanskrit खण्ड (khaṇḍa), meaning "scrap, broken piece, candied sugar, dried molasses."

**Direction of Borrowing:** The Arabic entry states the word comes "From Persian _کند_ (kand, 'candied sugar')." However, the Persian entry indicates it was "Borrowed from Arabic _قَنْد_ (qand), displacing older _کند_ (kand)." This suggests Arabic borrowed from Persian initially, then the Arabicized form later influenced Persian.

## Meanings

**Arabic:** "rock sugar (originally: the solidified sap of the sugarcane)"

**Persian:** "sugar cube"

## Derived Terms

**Arabic:** No derived terms listed in the Arabic section.

**Persian:** 
- قندی (qandi)
- قندان (qandân)
- کله‌قند (kalle-qand)
- چغندر قند (čoġondar-e qand)
```


### [2026-09-06T15:02:25.942Z] TOOL RESULT

```
# Persian Entry for گلشن

**Etymology:**
The word is formed from "گل" (gul) + "شن" (šan). The document does not provide information about Avestan or Middle Persian antecedents for the "-شن" element.

**Meaning:**
According to the entry, گلشن means "(archaic) flowerbed; rose-garden." Synonyms listed include چَمَن (čaman), گُلِسْتَان (gulistān), گُلْزَار (gulzār), and خِیَابَان (xiyābān).

**Verbatim Quote:**
"From _[گل](/wiki/%DA%AF%D9%84#Persian "گل")_ (gul) +‎ _[شن](/wiki/%D8%B4%D9%86#Persian "شن")_ (šan)."
```


## [2026-09-06T15:02:33.158Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%86",
 "prompt": "Give the Persian entries/suffix for شن (šan): etymology, meaning, Middle Persian/Avestan antecedents, related terms (گلشن, کاشان). Quote verbatim."
}
```


## [2026-09-06T15:02:35.164Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B4%DB%8C%D8%A7%D9%86%D9%87",
 "prompt": "Give the Persian entry for آشیانه: etymology (Middle Persian āšyān, Avestan, Proto-Iranian root), meaning. Quote verbatim."
}
```


### [2026-09-06T15:02:39.777Z] TOOL RESULT

```
# Persian شن (šan) - Suffix Entry

**Etymology:** Potentially connected to Proto-Indo-European *tḱey-m̥no-, from root *tḱey- ("to cultivate, settle, live"). The entry notes comparisons with Avestan 𐬱𐬀𐬌𐬌𐬀𐬥𐬀 (šaiiana, "place of residence") and Old Armenian շէն (šēn).

**Meaning:** The suffix denotes "[place](/wiki/place "place")" with synonyms گاه (gāh) and کده (kade).

**Related Terms:** The document provides two derived examples:
- گلشن (golšan) - "flowerbed rose-garden; place of flowers"
- تبشن (tabšan) - "hotspring, place of heat"

The entry additionally mentions آویشن (āvīšan), meaning "thyme, [flower that grows near] water-places," though it notes the intermediate کاشان is not explicitly listed in this section.
```


### [2026-09-06T15:02:40.169Z] TOOL RESULT

```
# Persian Entry for آشیانه

Based on the Wiktionary page provided, here is the available information:

**Word:** آشیانه (âšiyâne)

**Meaning:** The entry defines this noun as **"nest"**

**Etymology:** The page does not include etymological information tracing the word to Middle Persian āšyān, Avestan, or Proto-Iranian roots. Only the modern Persian entry and its alternative forms are documented on this particular Wiktionary page.

The page does include a cultural reference—a song lyric using the variant "آشیونه" (Ashiyouneh) where the word metaphorically refers to "nest" or "beloved."
```


## [2026-09-06T15:02:53.641Z] TOOL CALL #64: Bash

```json
{
 "command": "ls site/pages/212.jpg 2>/dev/null; pdftoppm -f 212 -l 212 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg212 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:02:56.033Z] TOOL RESULT

```
site/pages/212.jpg
total 912
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:02 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    264 Sep  6 10:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
```


## [2026-09-06T15:02:58.363Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg212.png"
}
```


### [2026-09-06T15:02:58.772Z] TOOL RESULT

```

```


## [2026-09-06T15:02:58.769Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:03:16.778Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 212 -l 212 -r 500 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg212hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg212hi.png'); print(im.size)\nw,h=im.size\n# node 3 Persian box around y ~ 990/2200 of full page; crop region\nim.crop((int(w*0.44),int(w*0.0)+int(h*0.44),int(w*0.80),int(h*0.48))).save('crop1.png')\nim.crop((int(w*0.20),int(h*0.145),int(w*0.50),int(h*0.205))).save('crop2.png')\n\"; ls"
}
```


### [2026-09-06T15:03:21.284Z] TOOL RESULT

```
(4250, 5500)
agents.txt
bqt1854.png
bqt2023.png
crop1.png
crop2.png
pg201.png
pg204.png
pg206.png
pg207.png
pg208.png
pg209.png
pg211.png
pg212hi.png
pg212.png
pg213.png
pg214.png
pg215.png
```


## [2026-09-06T15:03:23.779Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop1.png"
}
```


### [2026-09-06T15:03:23.795Z] TOOL RESULT

```

```


## [2026-09-06T15:03:26.730Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg212hi.png'); w,h=im.size\nim.crop((int(w*0.44),int(h*0.470),int(w*0.80),int(h*0.500))).save('crop3.png')\n\""
}
```


### [2026-09-06T15:03:28.858Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:03:31.235Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop3.png"
}
```


### [2026-09-06T15:03:31.250Z] TOOL RESULT

```

```


## [2026-09-06T15:03:40.568Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:03:40.623Z] TOOL RESULT

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


## [2026-09-06T15:03:54.877Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 p673 (leaf 682) ===\"\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in (681,682):\n    print('--- leaf',i)\n    print(t[i][:1800])\nEOF"
}
```


### [2026-09-06T15:03:56.683Z] TOOL RESULT

```
=== WLD Bd1 p673 (leaf 682) ===
leaves 895
--- leaf 681
                                                                                                 ,                                      ,




                                                               g«hedh-                                                               (573


  Hierher auch                gr.       dewog „Beschimpfung, Schande" (<( *y*edhsno- Brug-
mann-Thumb GrGr. 116, aus *(fiend1tno- zw. Johansson aaO. 57),                                                              devva^oj
.,beschimpfen, verhohnen"?                       S.       auch unter g'iou- ,,Mist“.
   Schw. dial. Jcvadda „in Stiicke sehlagen, zermalmen" nd. quaddcren ds.,
woraus dan. dial, hvaddre ds., kvadder „kleine Stiicke", anfrk. quezzon
„allidere“, mnd. quetscn „quetschen", afr. quetscne „Quetschung“, mhd.
quetsen, quetschen „schlagen, stofien, quetschen".
    Fraglich bleibt, ob mit Zupitza G. 87. Brugmann IF. 6, 103, v. Grien-
berger SBdWienerAk. 142, YII1 172, Johansson aaO. 56, ahd. quist „Yer-
derben, Yernichtung", got. qistjan fmqistjan , ahd. firquistnn , arquistan mnd.
                                                           ,                                                                 ,


quistcn „verderben, vernichten" hierher zu ziehen ist; s. auch u. qhais- .,haften
bleiben", g'ics- „erloschen“ und (field- .,uberwilltigen“ Ahd. quid, ledt „Kot",                —
                                                                     u
lit. (jvda „Schande“, die Johansson mit andern hierherstellt, s. u. g /ni- .Mist".

   Lit. gendit, g'esti ..Schaden                 nehmen, verderben, zugrunde gehen", gadinii                                            ,

gnd'tnti           verderben, beschiidigen, storen'         pagodas ..Yerderben", lett. jinstu
                 
--- leaf 682
674                                             gnebh. guabh           — gueb(k)-
l.       g“ebli-, g“abli- „eintauclien,                        versenken, versinken".
   Gr. pun no ..tauche ein", parffjvai, ftncfi] „das Eintauclien, Fiirben", fia<pe i>,'
,,Farber" (aol. jinxeiV               Hes. nacli dvmop das selber Kreuzung
von pdm co mit dido: pmafto umgestellt aus pamiQay. Boisacq 1100; gegen
Fick I 4 34, 401. Bechtel Hauptprobl. 114, wo auch yicpvoa boot. pscpvga,                      ,


kret. gortvn. dscpvga, lak. dkpovga ..Briicke. Damm" ) mit Unrecht angereiht
                                                       l



werden. Als maked. Entsprechungen fafit Fick KZ. 42, 147 ydfSeva o^v/Mipia.                              •




ijroi TOL'fiha Hes. unci yvfia   y.oivpjiq letzteres, da fivmco als Stiitze fiir
                                                          '
                                                                       ;


v            besonders fraglic.h);
         wegfiillt,
  anord. k vrfja fund kefja nach dem Praet. kof aus *krof) trans. ..nieder-
driicken. untertauchen, ersticken", kvef „Katarrh", kvafna intr. ..ersticken".
knf n. ..das Untertauchen, Schwimmen unter Wasser: Meer". aschw. kraf
„Tiefe", anord. kvcefo (idg. e!), kg fa trans. ..ersticken", mhd. crqueben ..er-
sticken" (= anord. kvcfju ) 2                        ).       S.   Fick BB. 2, 189.     Wb. I 4 33f., 196, 399,
Zupitza GG. 83.
  Eine vielleicht verwandte, aber nur die Bed. ,,tief" aufweisende Wz.
*yWrmbh-.            zeigt das Arische (wobei im ai. das   der Tiefstufe                       (j


oder o-Stufe                   durcbgeftihrt         ist.      gegeniiber av. j der e-Stufe)        :   ai.   gabhird-,
(jumbhlrd- „tief", tjumbht              yamhhdra- n. ,
```


## [2026-09-06T15:04:05.449Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[680][:2600])\nEOF"
}
```


### [2026-09-06T15:04:07.518Z] TOOL RESULT

```
672                                                           g“et-       — g»edh-

2. g“et-                „Harz“.
            n. „Lack, Gummi“, lat. bitumen ,,Erdharz, Erdpeeh" (aus den
            Ai. jcUu
Dialekten entlehnt s. Ernout El. dial. 28, 68), gall, betulla, betula „Birke“,
mir. bethe „buxus“, cymr. beclw „betula“, corn, bedeiven „populus“, bret.
bexucn „betula" (benannt, weil „ bitumen ex ea Galli excoquunt", Plinius
XFI. XYI 75 s. Thurneysen IF. 21, 175), ags. Juclt cuiclu, cweodo, cirudu
„mastix“, akd. cnti ,,gluten“, mhd. kiile, tut, nhd. butt, kitt ,,Kitt“ (DWb. 5,
860 f); ablautend norw. kctitfa ,,Harz‘, schw. kudu „Harz“, adan. kvade ,
norw. dial, kvcede „Saft, der aus Birkenrinde gebrannt wird“; norw. koda,
kvceda ,,Biestmilch“.
    Bugge KZ. 19, 428 f, Kluge Festgr. an Boethlingk 60, Fick III 4 60,
Falk-Torp 513 mit 1496, 600.
    Recht zweifelhaft ist Scheftelowitz’ (BB. 29, 15) Anreihung von arm.
k if. kfan Milch", phantastisch Petersson Heteroklisie 62 ff. und LUA 1922,
                            ,



1   ff.. der nocli lit. ginturas, guVaras „Bernstein“, gr. Serg „Fackel“ u. arm.
        1



hath ,,Tropfen" und kath'u                              ,,   Milch'
                                                                      1
                                                                           auf sein idg. Paradigma                       *(fieiu,
*g‘ietnes zuriickfiikrt.


3. gjet- „reden,                           sprechen".
            Arm. ko6em      nennen, herbeirufen, einladen", koc „Einladung"
                                         ,,rufen,
(wabrscheinlich             postverbale  nomen
                                          got. qipan „sagen, sprechen, reden,
                                                                          ,


nennen", aisl. kitedu „einen Laut geben, auBern, klingend vortragen, rezi-
tieren, sagen, nennen", ags. ciuedan „reden, sprechen, sagen, nennen, er-
klaren", afr. qnetha , .sagen, sprechen, bedeuten", as. quad an, ahd. quedan ds.;
aisl. kvidr „Spruch, Gerode", as. quidi st. m. „Rede. Wort"; aisl. kucdiu

..begriiBen, anreden, fordern, aufbieten", as. queddian, ahd. chetten „be-
griiBen" (d. h. „zum Reden bringen", s. Xeckel Eddaglossar p. 95), woraus
knqp „Forderung. Vorladung, Verpflichtung" retrograd gebildet ist, siehe
    Wessen TJUA. 1914 p. 128 u. vgl. arm. koc.
      Liden Arm. Stud. 6Sf., 133 (mit Lit.!), Fick III 4 o 9 f                                         . ,
```


## [2026-09-06T15:04:22.377Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"jaidyemi\\|jadiy\\|guidiu\\|d-eaaaad\\|gedauti\\|gedauju\" incoming/WLD/WLD_Bd1_pages.txt | head -10\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,pg in enumerate(t):\n    if 'gedauti' in pg or 'guidiu' in pg or 'jaidyemi' in pg:\n        print('leaf',i, pg[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T15:04:24.247Z] TOOL RESULT

```
63762:   Av. jaidyemi, ap. judiynmiy ,.ich bitte": gr. Aor. dtooaodai anflehen ', Pte.                          ,
leaf 681                                                                                                  ,
```


## [2026-09-06T15:04:26.444Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '63750,63790p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:04:26.505Z] TOOL RESULT

```
                                                                          ,
                                                                                                                             <


glut „zugrunde gehen“ laber lit. gedeti „trauern“                                          s.   u. gVdiedli-       Litton'',         be-
gehren“).            Ygl. Miihlenbach-Endzelin                     I      699 m. Lit.
   Fick III 1 60, Falk-Torp 600, 603, 610, 1505, Brugmann IF. 6, 103. Zu-
pitza G. 87, Johansson aaO.
  Nicht hierher               (trotz      Fick II 4 106)           ir .       qand „knapp, karg. enge".


gl'hedh- „bitten, begehren“.
   Av. jaidyemi, ap. judiynmiy ,.ich bitte": gr. Aor. dtooaodai anflehen ', Pte.                          ,




-dsorog in dnodeorug , verwiinscht, verschmaht, verachtet", nokvdeorog sehr                                                      ,




ersehnt ', Pers.-Y. Geo-deorog, boot. Gw- efttorog, nddog m., nodi) ,,Sehn-
sucht, Verlangen      nodeco ,,erselme. vermisse schmerzlich, verlange“; air.
                                1


                                    ,


guidim         ,.bitte“       (= nodeco      ,   Pf. ro-gcld , s-Konj. pi. gessenn (usw.,                              s.    Peder-
sen II 550 f.), guide ..Gebet"                   (
                                                     g'ihodhia      :     foigde ,,Betteln" aus *iio-ged)a; hir-
nuigdc             cymr. giceddi Gebet" (* iio-godimci Osthoff IF. 27, 172).
               .,Gebet‘),                                 ,.


Lit. gedau-ju,      „sicli sehnen, sehnsiichtig suchen, verlangen, wollen",
                          -ti

gedii (und gedziii), gcdijti „sich sehnen; traurig sein, trauern" (hierher
```


## [2026-09-06T15:04:31.151Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nn=63762\nleaf='\\n'.join(lines[:n]).count('\\f')\nprint('leaf(0-based)',leaf,'=> printed approx', leaf+1-9)\n# print header of that leaf\nt='\\n'.join(lines).split('\\f')\nprint(t[leaf][:150])\nEOF"
}
```


### [2026-09-06T15:04:32.988Z] TOOL RESULT

```
leaf(0-based) 681 => printed approx 673
                                                                                                 ,                                      ,
```


## [2026-09-06T15:04:38.591Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"jadiy\\|^jad-\\|jad-\" KNT.txt | head -10\necho \"=== IEC ===\"\ngrep -n \"gedh-\\|hedh-\" IEC.txt | head -10\necho \"=== MON gada/qand ===\"\ngrep -n \"گدا\\|خجسته\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-06T15:04:38.700Z] TOOL RESULT

```
1282:dh (imv.), OP jadiy, Skt. jaht (Skt. 7 by
1528:*gthen- in ajanam ‘I smote’, *g*hn- in jadiy ‘do thou smite’, -jata ‘slain’.
2404:„ рту. *g*hn-dhi, OP jadiy, Skt. jaht; so alko 2d pi, imv. *o*hn-le, OP jata, and 3d sg. imf. mid. *egthn-lo, OP patiy-ajalà| imf. *eg*hen-m, OP ajanam, Skt. áhanam (with antevocalic de- velopment of m, $07.11), whence with the- matic vowel 3d рі. OP -ajana" in avajana* and perhaps the restored subjunctive 3d pl. i-Janá"tty.
2486:pIE *g*hedh- in pAr. *fadhja-, Av. Jaiüyeiti, OP — 4 jadiyāämiy 1 entreat’. |
2561:I. The primary ending -mi is attached directly to non-thematic stems, as in pIE *es-mz, Skt. dsmz, Av. ahmi, ОР amiy. The ending of thematic stems was the lengthening of the thematic vowel o, as in Lat. ferd, Gk. феро; but to this -б there was added in Aryan the ending -mz, as in Skt. bhdra-mt, Av. barümi, ОР pari-barümiy. Other OP examples: parsimiy, Skt. prechámi; dárayamiy, Skt. dhard- ydmi; vatndmty, jadiyämiy.
2604:I. The second smgular active of thematic stems is the stem without suffix: jivà, Skt. jiva; pari-bará, Skt. bhára, Gk. $€pe; parsa, Skt. prechd, Lat. posce. That of non-thematic stems has an accented -dhi, attached to the zero grade of the root: pIE *i-dht, OP -idiy in paraidiy and paridiy, Skt. tht, Gk. 16; pIE *gthn-dht, OP jadiy, Skt. jaht; OP pädiy, didiy (5129), G-rsnudiy.
2663:D. As double object, one of the person and the other of the thing: DB 1.44f айа xšaçam tya Gaumdta hya magus айта Kabügiyam ‘this king- ship which Gaumata the Magian took away from Cambyses’ or ‘of which Gaumata deprived Cam- byses’; so also 1.46f, 59, 65f, and its passive in 1.49f hya атат Gaumàlam Шат magum тёасат ditam салтта ‘who might make that Gaumata the Me- dian deprived of the kingship’, DB 4.65 лау Skaurim (= skaubim) пай tunwatam züra akuna- vam ‘neither to the weak nor to the powerful did І do wrong’. DPd 20-2 айа adam yànam jadiya-
2763:I. The pronouns haw, ava-, -fim, -dim, and their forms are often used to refer back to a pre- ceding phrase or relative clause; a preceding phrase is usually in the nominative, as in DB 2.30f Ката kya hamiçiya тапа nary gaubatary avam jadiy ‘the rebel army which does not call itself mine—that do thou smite’, but sometimes in its own proper case, as in DB 2.84 kdram hamiciyam hya mand naty gaubdtaiy атат jatà ‘the rebel army which may not call itself mine—that do ye smite’.
2944:I, Commands, addressed to men; very common, cf. parsà DB 4.38, 69, jadiy DB 2.31 etc., kusuvà DNb 50. In jwā DB 4.56, 75, the command ap- proaches a wish in value; in má . . . raréatuy DNb 60, the negative command seems to become a threat. In varnavatàm DB 4.42, 53, the man ad- dressed is not subject, but object.
3059:IV. When а verb takes two accusatives, one denoting а person and the other a thing, the order is variable; with di- ‘take away from’, DB 1.46 (both objects follow; ef. passive in DB. 1.50, where both nouns precede); DPd 20-2 atta adam убпат jadiyimiy Áuramazdàm ‘this as a boon I beg of Ahuramazda’, DNa 53f айа adam Aura- mazdám jadiyãämīiy.
=== IEC ===
1055:bhādh- ‘hurt, sicken, repel, nauseate’. Cf. WP II, 130. Cf. bhedh-, bhodh- Skt. (ambig.) badhe ‘repel, harry’; badháh ‘tormentor’; bādhā ‘pain’; Gk. péthō ‘suffer’ is isophonic, but EB and JBH otherwise; Br. cf. bæz ‘dunce’; W boddi, 3s. bawdd ‘drown’ is isophonic, but uncertainly fr. *bhādh-; Li. bostu, inf. bosti, pf. bodau ‘tire, bore; be tired, be bored’; bodùs ‘nauseating’. (The Skt. mp. bibhadse "am sickened' in- dicates *bh- and *-dh-)
2728:dhedh- ‘nurse’ Per. dade, id.; cf. S.It. deda, id.; Gk. cf. (*-é-) Tēthús (nurse of Hera) and (alleged) téthe ‘nurse’; Ir. cf. deol, diúl ‘suckling’, isophonic w. Gk. thēlé, see dhēl-; cf. also Ir. dedel ‘she-calf
2756:dhēiô dhēmi (2) ‘put, lay’. Cf. dhídhemi, dhesnos, dhetis, dhētos, etc. WP I, 827-820 and cf. also dhedh-, dhesio Ober da-; Tokh. AB Gs, B tes- (= Skt. dhàsyàmi: Arm. edic: Gk. thésó: Li. désiu &
15512:skedh- (skhedh-?) ‘cut, hurt’. (Phonol. am- big.). Cf. skedhros, skhidros Gk. cf. a-skethés, adj. *un-harmed'; Latv. Ske- dens “split stick’; Li. cf. skederé, f. ‘chip’; (long-gde in) Olr. scíss, Ir. scíos, f. (fatigue, if from a type *sked(h)sa)
=== MON gada/qand ===
MON_part2.txt:1484:درخور غریب. هر چیز سزاوار به گدایی و 
MON_part2.txt:3714:نقطهٌ گداز و نقطةً جوش غیر فلزها پست 
MON_part2.txt:5012:گداختن سیم و زر در ااتش جهت امتحان. 
MON_part2.txt:5209:جانگدازن رقت آور. ضح.- در عربی بجای 
MON_part2.txt:5399:اصل به معنی «پیش» بوده: فرخجسته. (یشف.) 
MON_part2.txt:5963:خجسته. مبار ث. میمون. زیبا. جمیل. 
MON_part2.txt:6006:خجسته. گل هميشه بهار. 
MON_part2.txt:6040:ببا رک طالم؛ خجسته اقبال؛ سعید. 
MON_part2.txt:6944:فروگداردن: 0:27490:-۱ (مصم.) ترک 
MON_part2.txt:9191:آن گداخته می‌شود.
```


## [2026-09-06T15:04:55.008Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA qand ===\"\ngrep -n \"قند\\|qand\\|kand \" incoming/PLA/PLA_pages.txt | head -20\necho \"=== FVQ qand/kudya ===\"\ngrep -n -i \"qand\\|kudya\\|kadā\" FVQ_pages.txt | head -10\necho \"=== SKT candy ===\"\ngrep -n -i \"candy\" SKT.txt | head -5\necho \"=== HJB candy ===\"\ngrep -n -i \"^CANDY\\|CANDY,\" HJB.txt | head -5"
}
```


### [2026-09-06T15:04:55.112Z] TOOL RESULT

```
=== PLA qand ===
6817:>          -    dabbüs:           ein       Ort    zwischen             Buchara          u.    Samarkand        pers.      2,
8161:>b_,               -    zarafkand:              "eine       Melodie"           aus     pers.         Pr     zirafkand         7,
9375:SI,         -        amargand:               "Transoxanien"                MP.         zoo          samarkand          ° ap.        kanta       10,
12402:>        -        gand:        "Kandis"                        pers.„> kand                  8       skr.   khand,      frz.       candi,      engl.
12426:qandfir                                                                     222                                                        awälib
12689:el             _ kagägand                 = gazkand                a.        v.
=== FVQ qand/kudya ===
=== SKT candy ===
23652:French  from  ttaUtn  from  Aratk Sanskrit:  candy.
=== HJB candy ===
4064:BREECH-CANDY,
4067:BREECH-CANDY,  n.T>.  A  locality on  the  shore  of  Bombay  Island  to  the north  of  Malabar  Hill.  The  true  name, as  Dr.  Murray  Mitchell  tells  me,  is  be- lieved to  be  Ji,urj-khddi,  *  the  Tower  of the  Creek.'
5068:CANDY.
5080:(1)  CANDY,  n.p.  A  town  in  the  hill country  of  Ceylon,  which  became  the deposit  of  the  sacred  tooth  of  Buddha at  the  banning  of  the  14th  century, and  was  adoptea  as  the  native  capital about  15d2.  Chitty  says  the  name  is unknown  to  the  natives,  who  call  the place  Maha  nuveniy  ^g^reakt  city.'  The name  seems  to  have  arisen  out  of  some misapprehension  by  the  Portuguese, whicn  may  be  illustrated  by  the  quota- tion from  Valentijn.
5085:1681.—"  The  First  is  the  City  of  Candy,  so generally  called  by  the  Chriituins^  probably from  Conde,  which  in  the  Chinffnlays  Lan- giiage  signifies  SillSf  for  among  them  it  is situated,  but  by  the  InhabifaEints  called fftngodafful-neure,  as  much  as  to  say  'The City  of  the  Ghingulay  people, 'and  Mauneur^ surnifying  the  *  Chief  or  Koyal  City.'" — R. Knox,  p.  5.
```


## [2026-09-06T15:05:03.545Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nn=12402\nleaf='\\n'.join(lines[:n+1]).count('\\f')+1\nprint('leaf(1-based)',leaf,'printed',leaf-15)\nprint('\\n'.join(lines[12396:12412]))\nEOF\necho \"=== SKT CANDY entry ===\"\ngrep -n \"Candy, sugar\\|CANDY, sugar\\|Candy,\" SKT.txt | head -5\ngrep -n -i \"candi, sugar\\|sugar-candy\" SKT.txt | head -5"
}
```


### [2026-09-06T15:05:08.003Z] TOOL RESULT

```
leaf(1-based) 236 printed 221

u        - ganb;               "Hanf,               Bindfaden"
                                                             _ pers.                              „5 kanaf 72,

     =
>        -        gand:        "Kandis"                        pers.„> kand                  8       skr.   khand,      frz.       candi,      engl.
                 candy,        dtsch.                  Kandis       9,


5 - gandaz:                                "Seehund"               pers.      102,

>= - gandaz’ : eine                                      Stadt             pers.           5 6° kohan-def              1           mp.   ır sa kahwan
                 + de? mp.                        &diz         "Festung"              12     s.      Sabdiz.



=== SKT CANDY entry ===
```


## [2026-09-06T15:05:12.192Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"khanda\\|khand,\\|khandas\\|candi\" SKT.txt | head -10"
}
```


### [2026-09-06T15:05:12.247Z] TOOL RESULT

```
66:There  is  one  point  to  which  I  wish  to  draw  especial  attention.  Bf the  advice  of  a  friend,  I  procured  a  copy  of  a  Dictionary  of  English Etymology  by  the  Rev.  J.  Oswald,  written  on  an  unusual  but  excellent plan.  The  author  airanges  all  the  derivatives  of  the  Latin  cedtn under  the  heading  of  the  Latin  cedOy  so  that  words  such  as  acctdt^ concede^  recede^  succeed,  are  all  presented  to  the  eye  at  a  glance.  The advantage  of  such  an  arrangement  is  obvious,  and  I  at  once  de- termined to  adopt  it,  merely  substituting  the  representative  English word  cede  for  the  Latin  cedo,  and  so  in  other  cases.  At  the  same time,  I  adopted  two  very  considerable  improvements :  (i)  the  retention of  the  alphabetical  order  for  the  derived  words  accedcy  concede^  ftc^ with  a  cross-reference;  and  (a)  the  extension  of  the  principle  to words  of  English  and  Scandinavian  origin.  Mr.  Oswald  gives  the words  only  under  the  primary  form,  which  is  a  great  inconvenience, seeing  that  this  is  often  precisely  what  one  does  not  know ;  and,  yoA for  want  of  the  cross-reference,  he  omits  the  derivative  anctsler altogether.  At  the  same  time  I  have  found  his  book  very  useful,  as far  as  relates  to  that  part  of  our  language  which  is  of  classical  origin. With  respect  to  words  of  Teutonic  origin  it  is  practically  valueless; thus  the  only  word  given  under  W  is  the  word  wonder.
156:tomatbie  Proven^ale. Rnss. — Ku>sian;  as  in  KcifTsDict.,  187^. St:and. — Scandinavian;  nvd  as  a  general
161:L^Qlch.  German,  an^l  Scandinavian. Turk. — Turkish;   as  in  Zenker's  Dict^
2792:Cannel-ooal ;  see  Candid.
3225:Ceneer;  see  Candid.
8891:hustings.  (Scand.)  The  ntod.  nse  is incorrect ;  k  is  properly  Mui/mg;  sing., and  means  a  council,  an  assembly  for  the choice  of  a  candidate.  M.  £.  ktistin^. A  S.  hthtittg.^\cc\.  kiis]ttng,  a  council, meeting.  —Ice!.  hUs,  a  house ;  |»/*^,  a  thing. aUo  un  assembly ;  see  Thing.  Cf.  Swed. and  Dan.  tittff,  the  same  as  Icel.  )finj^\  and the  Swed.  form  better  accounts  for  the  £. form. huswife.  (E.)    I.e.  keusewife.
9134:Inoandesoent ;  see  Candid.
9139:Incendiary,  Inoenae :  see  Candid.
11190:marry-  0'-  —  I-)  M  E.  marten,  m  F, marier.  —  L  maritare^  to  marry.  <—  L.  mart- tujt  a  husband  ;  see  marital  (above). Mash,  to  beat  into  a  mixed  ma&s.  (E.  er Scand.)  A  maiA  is  properly  a  mtxtnre; and  to  masA  was,  formerly,  to  mi\.  We find  A.  S.  maxwyrtt,  mash-wort,  new beer;  so  that  the  word  may  l>e  English; but  it  is  commoner  in  Scandinavian.  Cf. Swed.  dial,  mask^  Swcd.  tnasi,  brewer's grains,  whence  masJka,  to  mix,  Dan.  and North  Fries,  mask,  grains,  mash.  Don. masJke,  to  mash,  fatten  pigs  with  grains.  + G.  meisch,  a  mash,  metscheH.  to  mash. The  sb.  form  appears  to  be  the  original. I'erha[t^  alliett  to  Mix.  Cf.  also  Gael. and  Irish  mas^,  to  mix,  infuse,  steep; Lithuan.  maixzyti,  to  stir  things  in  a  pot, from  mtJS'fit  to  mix.
18833:Sugar.  ( F.  -  Spaa.  -  Arab  -  Pers,  -  Skt) F.  i«<-fr.  — Span,  djrwidr.  —  Arab,  assokkar; put  for  a/,  the,  wWar./dA^ar,  sugar.  — Per», «Aa>tdr.»Skt.  farkarxi,  gravel,  also  candied ■ugar.  Prob.  allied  to  Skt.  karkara,  hard, eacoharine-  (F. -L.-Gk.-Skt.)  F. Kucharin,  adj.,  from  L.  sotckartfrt,  sugar.* fjk.  aoKxopov.^aki.  farkard  (above).
```


## [2026-09-06T15:05:19.891Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"candy[^|]\\{0,300\\}\" FSD_vol1.txt | grep -i \"arab\\|pers\\|sanskr\" | head -5\necho \"=== WEB ===\"\ngrep -n -o \"candy[^|]\\{0,250\\}\" WEB.txt 2>/dev/null | grep -i \"arab\\|pers\" | head -5\nls WEB* 2>/dev/null"
}
```


## [2026-09-06T15:05:21.853Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%AF%D9%8A%D8%A9",
 "prompt": "Give the Arabic entry for كدية (kudya): meaning, etymology, root, and any related verb كدّى / تكدية. Does it say it is from Persian?"
}
```


### [2026-09-06T15:05:22.444Z] TOOL RESULT

```
=== WEB ===
WEB_vol1.txt
```


### [2026-09-06T15:05:27.930Z] TOOL RESULT

```
# Arabic Entry for كدية (kudya)

Based on the Wiktionary content provided, there is **no Arabic entry** shown for this word. The page only contains entries for:

1. **Egyptian Arabic** - defined as "The chief celebrant at a zar"
2. **Moroccan Arabic** - defined as "hill"

## Etymology Information

The Moroccan Arabic entry states it was "Inherited from Arabic _كُدْيَة_ (kudya)," but the actual Classical Arabic entry with detailed etymology is not included in this page content.

**Persian origin claim:** The provided text does not mention Persian as a source. The Moroccan Arabic section only references inheritance from Arabic itself, with no etymological chain to Persian documented here.

To find information about Persian origins or related verb forms (كدّى / تكدية), you would need to access the full Arabic dictionary entry on Wiktionary, which is not displayed in this excerpt.
```


## [2026-09-06T15:05:32.181Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"andy[^|]\\{0,300\\}\" FSD_vol1.txt | grep -i \"arab\\|Pers\\.\\|Skt\" | head -5\necho \"=== WEB_vol1 ===\"\ngrep -n -o \"candy[^|]\\{0,250\\}\" WEB_vol1.txt | grep -i \"arab\\|pers\" | head -5\necho \"=== AFM alt qand ===\"\ngrep -n \"القند\" AFM.txt AFM_alt.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T15:05:33.952Z] TOOL RESULT

```
=== WEB_vol1 ===
85453:candy of a firm, jellylike consistency, made of sweetened gum arabic or gelatin, usually colored, flavored, and covered with sugar.
=== AFM alt qand ===
AFM.txt:5059:(الشَان) القسطاس 3 توزن بها الاشياء. القند تعريب كبآن وبقال فين 0 
AFM.txt:5283:فقل ان القندأوَ + الغليظ والسئ 2 الخ معرب عن > 502 ؛ القدم 
AFM.txt:5288:4 القند زر متوف قندن ومعنا كاب الله والستن مرت د ويم 
AFM.txt:5317:وفي اللسان:« القندل بوزن جعفر الطويل ٠»‏ وهذا أصح لاله تعريب كندواله وفعناة 
AFM_alt.txt:5095:(القند) عسل قصب السگر اذا جټد معرب کند وهو قصب السك ومن 
AFM_alt.txt:5100:# (القنْدأوٌ) قال الاب انستاس ( اشرق )٠٠۳:‏ : « القند أو والس دأو 
AFM_alt.txt:5103:من العاني الكثيرة وقال : « القند أو السئ الغذاء 8 الخلق والغلظ والقصار من 
AFM_alt.txt:5115:الوارد ) ٠‏ قلت المندر معرب فندز ومعناة كاب الاء والقندس معرب كندسك ومعناء 
AFM_alt.txt:5143:جړ (الندّل والقتادل والقندويل ) عضي ا ل الاٍ یل والدوات (القاموس) : 
AFM_alt.txt:5455:# (أككنْدأو) الل الغلبظ تعريب كنده وهو لفة فى القندأو
```


## [2026-09-06T15:05:49.680Z] TOOL CALL #83: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%DA%AF%D8%AF%D8%A7' \\\n 'https://en.wiktionary.org/wiki/%D8%AE%D8%AC%D8%B3%D8%AA%D9%87' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0ed%CA%B0-' \\\n 'https://www.etymonline.com/word/candy' \\\n 'https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%DA%AF%D9%84%D8%B4%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A2%D8%B4%DB%8C%D8%A7%D9%86%D9%87' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 212 (Gwhedh / Gwhen 1) verification' 2>&1 | tail -1; done"
}
```


## [2026-09-06T15:05:50.840Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=candy",
 "prompt": "Give the etymology of 'candy' as printed in the American Heritage Dictionary entry (the bracketed etymology), verbatim."
}
```


### [2026-09-06T15:05:54.214Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2137cc50c95e6c21.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65131a5fa342e274.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ca8e9285760ed102.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee0fede926dfc14c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8519f5d3fd26aba0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/29d474ebc61eac9b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d4f375dc4698aea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6755bad55ff76f92.txt
```


### [2026-09-06T15:05:59.155Z] TOOL RESULT

```
# Etymology of "Candy"

According to the American Heritage Dictionary entry, the bracketed etymology states:

"[Middle English _candi_, crystallized cane sugar, short for _sugre-candi_, partial translation of Old French _sucre candi_, ultimately from Arabic _sukkar qandī_ : _sukkar_, sugar + _qandī_, consisting of sugar lumps (from _qand_, lump of crystallized sugar, from an Indic source akin to Pali _kaṇḍa-_, from Sanskrit _khaṇḍakaḥ_, from _khaṇḍaḥ_, piece, fragment, perhaps of Munda origin).]"
```


## [2026-09-06T15:07:00.044Z] TOOL CALL #85: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.ahdictionary.com/word/search.html?q=candy' --note 'pdf 212, AHD:196 candy etymology' 2>&1 | tail -1\npython3 tools/ref_page.py BQT:1453 2>&1 | tail -18"
}
```


### [2026-09-06T15:07:07.623Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bbea6a9d6e47ed54.txt
هت موکل بر زمین . و بی دیگر کوبند فرخشه رشتهٌ قطایف (۶)
فر خسته - بفتح اول وئاك بروزن سر است .
() چك :کلیت . (۲) چك : قطائف . (۳) چك : بوزن .
(2) چك : قطائلف .
۱ از :فر (پیشوند) ۳ خجته (۸.م.) « اسشق ۸*۷ *.
۴ - این غم دل برد يك ره چون هزبمت گشت برد
فراخجته فر فروردین پدید آورد ورد -
غتابری رازی « ترجمان‌البلاغه ص ۱۳ >
۴ از : فرخج(رك : فرخج) ی ( اسم مصدری ). ,۴ - از: فر(پیشوند) مل
خته («.م.) « فرخته کشتة برزمین کشیده بود . ابوالعبای عباسی کوید :
او می‌خورد بشادی وکام دل دشمن تزا رکشته و فرخته. > لغت فری ۰۶4۹۵
8 > پرخش (.م.) ۰ ۹ ‌- بان همنی «فرخشه ۰ قطابف باشد. زمان‌ماوراءالنهش
است . رود کی (سمرقندی) کوید :
باکا که بره است و فرخته برخواش وب ی کا که جوین‌نان همی‌نياید سیر.»
« لغت فری ۷
۷ - مصحف و مبدل « فرخته > (ه.م.). ۸ مصحف « وخشور » (ه.م.) از
دسایر « فرهنگه دساتیر ۲۵۹ . ‎-٩‏ رد : فرخشته وح۶ .
```


## [2026-09-06T15:07:27.407Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('LKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf='\\n'.join(lines[:2505]).count('\\f')\nprint('LKT leaf',leaf,'printed',leaf-26)\nlines2=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor n in (7640,8209,5641):\n    print('HUB line',n,'leaf',' '.join(lines2[:n]).count('\\f'), 'printed', '\\n'.join(lines2[:n]).count('\\f')-10)\nEOF"
}
```


### [2026-09-06T15:07:29.760Z] TOOL RESULT

```
LKT leaf 112 printed 86
HUB line 7640 leaf 225 printed 215
HUB line 8209 leaf 240 printed 230
HUB line 5641 leaf 170 printed 160
```


## [2026-09-06T15:07:37.678Z] TOOL CALL #87: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg212.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/212.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-06T15:07:37.759Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T15:07:39.581Z] AGENT

Now writing the verification file.


## [2026-09-06T15:13:53.909Z] TOOL CALL #88: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-212.json",
 "content": "{\n  \"pdf_page\": 212,\n  \"book_page\": 182,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gwhedh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷʰedʰ- 'to ask, pray, beg for, desire'\",\n      \"note\": \"Pokorny 488 gʷhedh- 'bitten, begehren'; Walde-Pokorny I 673; Watkins/AHD 'gʷhedh-. To ask, pray. [Pok. gʷhedh- 488]'. The root name, the language label (Indo-European) and the gloss 'to ask, wish, want' are all correct, and Pokorny's very first witnesses are the Iranian forms Nourai puts in node #1. The one systematic oddity on this chart is notational: Nourai prints Avestan/Old Persian ǰ as 'ž' in ža 3, žaidhyemi, žadiyâmiy, a-žasta, while writing 'hu-jasta' with j in the same box — the standard transliterations are ǰaiδyemi, ǰadiyāmiy, aǰasta-, huǰasta-. That inconsistency is in the printed book (checked on the page image, copied to data/verification/sources/refs/ocr/BOOK/212.png); the JSON extraction is faithful.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *gʷʰedʰ- «خواستن، درخواست کردن، دعا کردن» است؛ پوکورنی ص۴۸۸ آن را با همین معنی «bitten, begehren» آورده و والده-پوکورنی (ج۱ ص۶۷۳) و واتکینز (AHD) نیز همین را می‌گویند. نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است و ادعای او دربارهٔ گواهان ایرانی (اوستایی و پارسی باستان) عیناً همان چیزی است که پوکورنی در سرِ همان مدخل آورده است. تنها نکتهٔ املایی این است که نورایی «ج» اوستایی (ǰ) را گاه «ž» نوشته است؛ این خطای چاپی خودِ کتاب است، نه خطای خوانش اسکن.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0ed%CA%B0-\",\n        \"https://www.iranicaonline.org/articles/begging-i/\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:488\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 145 (printed 488): 'gʷhedh- ,bitten, begehren'. Av. jaiδyemi, apers. Jadiyāmiy ,ich bitte'; gr. Aor. θέσσασθαι ...; air. guidiu ,bitte'; lit. gedauju ...; aksl. žędati ... WP. I 673.' Exactly the root, gloss and page Nourai cites.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 673 (WLD_Bd1_pages.txt leaf 681)\", \"stance\": \"supports\", \"note\": \"'gʷhedh- „bitten, begehren“. Av. jaidyemi, ap. jadiyamiy „ich bitte“: gr. Aor. θέσσασθαι ... air. guidim „bitte“ ...' — the source Pokorny himself refers to.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷhedh- (AHD_watkins1985.txt line 545)\", \"stance\": \"supports\", \"note\": \"'gʷhedh-. To ask, pray. 1. Germanic *bidjan ... [Pok. gʷhedh- 488, 2. bhedh- 114.]' — same root, same gloss, same Pokorny page.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, searched for ghedh-/gʷhedh- headwords\", \"stance\": \"silent\", \"note\": \"grep '^ghedh-|^gu̥hedh-' in IEC.txt returns nothing; Mann has no entry for this root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ža 3, gad; žaidhyemi, žadiyâmiy; hu-jasta; a-žasta\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan verbal root ǰad- (Bartholomae's gad-, AiW; cf. the participles ǰaiδyant-, ǰaiδyamna- 'asking', which Bartholomae files under 'gad-') and Old Persian jad- 'to ask, entreat' continue PIE *gʷʰedʰ- with the regular Indo-Iranian palatalisation of *gʷʰ before a front vowel to *ǰʰ > Iranian ǰ, and *dʰ > Avestan δ intervocalically (hence Av. ǰaiδyemi vs OP jadiyāmiy, where OP keeps d). Kent's Lexicon derives it explicitly: 'pIE *gʷhedh- in pAr. *jadhya-, Av. ǰaiδyeiti, OP jadiyāmiy “I entreat”' (attested DPd 20-2 'ima adam yānam jadiyāmiy Auramazdām' = 'this as a boon I beg of Ahuramazda'). The past participle *ǰasta- 'asked (for), desired' gives the compounds a-ǰasta- 'not asked for' (attested Vd. 18.37) and *hu-ǰasta- 'well asked for, blessed' — the latter is not itself attested in the Avesta and is starred by Hübschmann (*hu-jasta-), reconstructed backwards from Middle Persian huǰastag / NP xojaste and its antonym Pahl. gaǰastag < *vi-ǰasta- 'accursed'. Nourai's 'ža 3' and 'žaidhyemi, žadiyâmiy, a-žasta' are his own spellings with ž for ǰ; the printed page shows exactly these forms, so the extraction is faithful and the inconsistent transliteration is the book's.\",\n          \"derivation_fa\": \"ستاک فعلی اوستایی ǰad- (نزد بارتولمه gad-) و پارسی باستان jad- «خواستن، درخواست کردن» بازماندهٔ ریشهٔ هندواروپایی *gʷʰedʰ- است: *gʷʰ در هندوایرانی پیش از واکهٔ پیشین به ǰ کامی شده و *dʰ در اوستایی میان دو واکه به δ نرم شده است؛ از این‌روست که در اوستا ǰaiδyemi و در پارسی باستان jadiyāmiy «من درخواست می‌کنم» داریم (کتیبهٔ DPd: ima adam yānam jadiyāmiy Auramazdām). صفت مفعولی *ǰasta- «خواسته‌شده» دو ترکیب می‌سازد: a-ǰasta- «ناخواسته» (وندیداد ۱۸٫۳۷، بارتولمه) و *hu-ǰasta- «نیک‌خواسته، مبارک» که خودِ آن در اوستا گواهی نشده و هوبشمان آن را با ستاره بازسازی کرده است. ادعای نورایی درست است؛ تنها نگارش «ž» به‌جای «ǰ» خطای چاپی خودِ کتاب است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0ed%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:488\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 145: 'gʷhedh- ,bitten, begehren'. Av. jaiδyemi, apers. Jadiyāmiy ,ich bitte'' — Nourai's two verb forms verbatim.\"},\n            {\"ref\": \"WLD:673\", \"status\": \"supports\", \"note\": \"WLD_Bd1_pages.txt leaf 681 = printed 673: 'gʷhedh- „bitten, begehren“. Av. jaidyemi, ap. jadiyamiy „ich bitte“'. The page number Nourai gives is exact.\"},\n            {\"ref\": \"SYN:1471\", \"status\": \"supports\", \"note\": \"Buck's p.1471 (§22.17 PRAY) lies beyond the local scan, which stops at ~p.1444; but Buck §16.62 DESIRE (SYN.txt line 29266, printed p.1161) gives the same group: 'Grk. ποθέω ... : θέσσασθαι ‘beseech, pray for’, Ir. guidim ‘pray, ask’, Lith. gedauti, ChSl. žedati, Av., OPers. jad- ‘beseech, pray for or to’. Walde-P. 1.673', and §18.35 (p.1272) lists 'Av., OPers. jad- ‘beseech, pray for’, see under ‘pray’ (22.17)' — i.e. the page Nourai cites is indeed Buck's treatment of this root.\"},\n            {\"ref\": \"HRN:470\", \"status\": \"supports\", \"note\": \"Horn's numbers here are entry numbers, not pages (his book stops at p.391). HRN.txt line ~4276, entry '470. xujeste ‘gesegnet, glücklich’, vergl. ferxujeste. aw. *hujasta-. Vergl. ajasta-.' — covers hu-jasta and a-jasta of this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW cols. ~1093 and 1150 (BRT.txt lines 11537-11538, 8047)\", \"stance\": \"supports\", \"note\": \"'j. ǰaiδyant- Adj., PPA.: s. gad-' and 'j. ǰaiδyamna- Adj. ..., PPM.: s. gad-'; the finite form appears in the citation 'āpǝ̄s ... vō ǰaiδyāmi' (Y. 65.11). Bartholomae's headword for the verb is gad- 'erbitten'. a-ǰasta- is quoted at V.18.37 ('naire ašaone aǰasta .. daoaiti').\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, § on Iranian verb stems (KNT.txt line 2486)\", \"stance\": \"supports\", \"note\": \"'pIE *gʷhedh- in pAr. *jadhya-, Av. ǰaiδyeiti, OP jadiyāmiy “I entreat”'; text example DPd 20-2 'ima adam yānam jadiyāmiy Auramazdām “this as a boon I beg of Ahuramazda”' (KNT.txt line 3059).\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 160, 215, 230\", \"stance\": \"partial\", \"note\": \"'xujasta ‘gesegnet, glücklich’ = zd. *hujasta- neben paz. gazista ‘verflucht’' (p.230) and 'gajastak ... als Gegensatz von np. xujasta ‘gesegnet, glücklich’ (= zd. *hujasta-) auf ein zd. *vījasta- zurückführt' (p.160). Hübschmann stars the Avestan form: hu-ǰasta- is a reconstruction, not an attested Avestan word.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"gedâ «گدا»; xojasteh «خجسته»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"xojaste خجسته 'blessed, auspicious' is a straightforward and well-attested descendant: Av. *hu-ǰasta- 'well-wished-for' > MP huǰastag > NP xojaste, with hu- > xo- (the regular Persian treatment of Old Iranian hu- 'good', as in xoš, xor-) and loss of the MP -ag ending to -e; its antonym is Pahl. gaǰastag < *vi-ǰasta- 'accursed', and the intensive compound far-xojaste فرخجسته (Nourai's extra form) is far/farr- + xojaste, exactly as Mo'in notes at Borhan p.1453. Mo'in's footnote in Borhan-e Qate' (p.717-718) spells out the same chain from the Avestan root ǰad-. gedā گدا 'beggar' is the more doubtful half. Mo'in (Borhan p.1776 footnote) derives it precisely as Nourai does — 'در اوستایی gad (خواهش کردن، خواستن) ... بارتولمه AiW', with Kurdish gadā — so a nomen agentis *gadā(g) 'one who asks' from the same *gʷʰedʰ- root. Modern Wiktionary, however, prefers a different Iranian etymon, comparing Avestan gaδa- 'robber' (cf. Av. *gaδōtāt- 'Räuberbande', AiW) and Pashto ġal 'thief', with a semantic path 'robber' > 'vagrant' > 'beggar'; that requires -δ- rather than -d- and is not the *gʷʰedʰ- root. Both etymologies are live; Nourai follows the older Persian (Mo'in/Bartholomae) view.\",\n          \"derivation_fa\": \"«خجسته» بی‌گمان از اوستایی *hu-ǰasta- «نیک‌خواسته» است: از راه فارسی میانهٔ huǰastag به فارسی نو رسیده؛ پیشوند hu- ایرانی باستان در فارسی به xo- بدل شده (مانند خوش، خور) و پسوند -ag پهلوی به -هٔ فارسی. متضاد آن gaǰastag «ملعون» (< *vi-ǰasta-) است و «فرخجسته» نیز، چنان‌که معین در حاشیهٔ برهان قاطع ص۱۴۵۳ می‌گوید، از «فر» + «خجسته» ساخته شده است. اما «گدا» دو ریشه‌شناسی رقیب دارد: معین در حاشیهٔ برهان (ص۱۷۷۶) آن را از ریشهٔ اوستایی gad «خواهش کردن، خواستن» می‌داند (با استناد به بارتولمه) و کردی gadā را گواه می‌گیرد — همان که نورایی آورده است؛ ولی ویکی‌واژه آن را با اوستایی gaδa- «راهزن» و پشتوی ġal «دزد» می‌سنجد و تحول معنایی «راهزن ← ولگرد ← گدا» را پیشنهاد می‌کند. پس این بخش با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%AF%D8%A7\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%AC%D8%B3%D8%AA%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:717\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' (Mo'in) vol. 2, BQT_v2_pages.txt leaf 175 (the page whose footnote continues 'بقیهٔ صفحهٔ ۷۱۷'), s.v. خجسته 'بمعنی مبارک و میمون'; Mo'in's footnote: 'خجسته؛ اوستا [*huǰasta] ... از ریشهٔ اوستایی ǰad- (خواهش کردن، درخواستن) ... «بارتولمه AiW». خجسته لغةً بمعنی نیک‌خواسته، متبرک، مبارک؛ ضد «گجسته» (ملعون).'\"},\n            {\"ref\": \"BQT:1453\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:1453 (v3 pdf 245), s.v. فرخجسته, footnote 1: 'از: فر (پیشوند) + خجسته (ه.م.)' — supports the extra form فرخجسته shown in this box.\"},\n            {\"ref\": \"BQT:1776\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:1776 (v3 pdf 573), s.v. گدا/کدا 'باشد که گدایی کننده است'; Mo'in's footnote: 'بکسر اول (در لهجهٔ مرکزی)، در اوستایی gad (خواهش کردن، خواستن)، هندی باستان ... (من خواهش می‌کنم) «بارتولمه AiW»، کردی gadā (گدا) «ژابا ص۳۵۷» ... قس: عربی: تکدیه، و اکداء' — exactly Nourai's arrow, including the hint at the Arabic derivative.\"},\n            {\"ref\": \"HRN:470\", \"status\": \"supports\", \"note\": \"Horn entry 470 (HRN.txt line ~4276): '470. xujeste ‘gesegnet, glücklich’, vergl. ferxujeste. aw. *hujasta-.' Covers xojasteh and farxojasteh but says nothing about gedā.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 215, 230\", \"stance\": \"supports\", \"note\": \"'xujasta ‘gesegnet, glücklich’ = zd. *hujasta-' — Hübschmann's independent confirmation of the Persian word's Avestan source.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss, entry 470; grep for 'Bettler' turns up only no. 559 derveš\", \"stance\": \"partial\", \"note\": \"Horn has xujeste but no entry for gedā; his only 'Bettler' word is derveš (no. 559), so Horn is silent on the beggar-word.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, searched گدا and خجسته as headwords\", \"stance\": \"silent\", \"note\": \"Aryanpur's Persian IE-roots dictionary has no headword گدا or خجسته (the four hits for گدا are incidental occurrences in other entries).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"kadâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The direction of borrowing Nourai draws — Persian gedā into Arabic — is the accepted one. C. E. Bosworth in Encyclopaedia Iranica (BEGGING i, 1989) writes that Arabic 'mokaddī (abstracts: takdīa, kodya “begging”), found in adab literature (e.g. in Jāḥeẓ, with his Ketāb ḥīal al-mokaddīn ...) from the 3rd/9th century onwards ... is clearly derived from Persian gadā “beggar, begging”' (citing Bosworth, The Mediaeval Islamic Underworld: The Banū Sāsān, Leiden 1976, I 40, II 244, and Pellat, 'Mukaddī', EI²). Arabic re-analysed the Persian noun as a hollow/defective triliteral k-d-y and built a form II verb kaddā 'to beg' with the noun kudya كُدْية 'begging' and the participle mukaddī مُكَدّي 'beggar'. The reservation is the form Nourai prints: 'kadâ' is not a lexical Arabic noun meaning 'beggar' — it stands for the verbal stem كدّى kaddā; the classical Arabic dictionaries' كُدْية kudya also carries the older concrete sense 'hard patch of ground', so the native lexicographers treated the group as Arabic. Nourai's arrow is right; his citation form is a stem, not an attested noun.\",\n          \"derivation_fa\": \"جهت وام‌گیری‌ای که نورایی رسم کرده است — از فارسی «گدا» به عربی — پذیرفتهٔ پژوهش امروزی است: بازورث در دانشنامهٔ ایرانیکا (مدخل BEGGING) می‌نویسد که «مُکدّی» عربی و مصدرهای «تکدیه» و «کُدیه» که از سدهٔ سوم هجری در ادب عربی (از جمله در «کتاب حیل المکدّین» جاحظ) دیده می‌شوند «آشکارا از فارسی gadā گرفته شده‌اند». عربی این نام فارسی را چون ریشهٔ سه‌بخشی ک-د-ی بازتحلیل کرد و از آن فعل باب دوم «کدّی» و اسم «کُدیه» و اسم فاعل «مُکدّی» ساخت. تنها اشکال، صورتی است که نورایی آورده: «kadâ» واژهٔ عربی مستقلی به معنی «گدا» نیست، بلکه ستاک فعلی کدّی است. پس ادعای نورایی با اصلاح صورت واژه پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.iranicaonline.org/articles/begging-i/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVF:565\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi (Tehran 1347) is catalogued in refs_online.json as kind 'website' (noorlib.ir viewer, login/browser needed); no page text obtainable here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Encyclopaedia Iranica\", \"where\": \"BEGGING i. In the Early Centuries of the Islamic Period (C. E. Bosworth), Vol. IV/1 pp. 80-84\", \"stance\": \"supports\", \"note\": \"'... Arabic mokaddī (abstracts: takdīa, kodya “begging”) ... and this is clearly derived from Persian gadā “beggar, begging” (see C. E. Bosworth, The Mediaeval Islamic Underworld ... I, p. 40, II, p. 244; Pellat, “Mukaddī”, in EI2)'.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-Alfaz al-Farisiyya al-Mu'arraba, searched كدية / تكدية / مكدي\", \"stance\": \"silent\", \"note\": \"grep over AFM.txt / AFM_alt.txt / AFM_pages.txt finds no entry for the k-d-y begging group; Addi Shir lists قند but not كدية.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein, searched 'kudya', 'mukaddi'\", \"stance\": \"silent\", \"note\": \"Klein covers only Arabisms that reached European languages; the beggar-word is not in KLN_1966.txt.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"takaddî «تَکَدّی»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian تکدّی takaddi 'begging' is the Arabic form-V verbal noun تَكَدٍّ takaddin of the denominative كدّى kaddā built on the borrowed Persian gedā — so it is a classic Persian → Arabic → Persian round trip: NP gedā > Arab. kaddā / kudya (3rd/9th c., Jāḥeẓ's Ketāb ḥiyal al-mukaddīn) > the Arabic masdar takaddī, re-borrowed into New Persian as the learned/formal word for 'begging' (Persian keeps gedā'i as the native synonym). Nourai's extra form مُتَکَدّی motakaddi is the corresponding form-V active participle 'one who begs'. Encyclopaedia Iranica heads the whole article 'BEGGING, Pers. gadāʾī, takaddī (Ar. also kodya, takdīa), soʾāl', i.e. it treats takaddī exactly as the Arabic-shaped Persian term for the same thing.\",\n          \"derivation_fa\": \"«تکدّی» مصدر باب تفعّلِ عربی از فعل «کدّی» است که خود از وام‌واژهٔ فارسی «گدا» ساخته شده؛ بنابراین یک وام‌گیری دوسویه (فارسی ← عربی ← فارسی) است: gadā فارسی در سدهٔ سوم هجری وارد عربی شد (کتاب حیل المکدّین جاحظ)، عربی از آن «کدّی، کُدیه، مُکدّی» ساخت و مصدر «تکدّی» دوباره به فارسی بازگشت و امروز واژهٔ رسمیِ «گدایی» است. «مُتکدّی» نیز اسم فاعل همان باب است. دانشنامهٔ ایرانیکا سرمدخل خود را «BEGGING, Pers. gadāʾī, takaddī (Ar. also kodya, takdīa)» گذاشته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.iranicaonline.org/articles/begging-pers/\",\n            \"https://www.iranicaonline.org/articles/begging-i/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVF:565\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari (FVF) exists only as a noorlib.ir page-viewer needing a browser session; not readable here.\"},\n            {\"ref\": \"FVA:349\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989): refs_online.json records that no digital copy was found on archive.org, ketabnak or noorlib.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Encyclopaedia Iranica\", \"where\": \"BEGGING (article head) and BEGGING i (Bosworth)\", \"stance\": \"supports\", \"note\": \"'BEGGING, Pers. gadāʾī, takaddī (Ar. also kodya, takdīa), soʾāl' and 'the abstracts takdīa, kodya “begging” ... clearly derived from Persian gadā'.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (Mo'in) p.1776, footnote to گدا\", \"stance\": \"supports\", \"note\": \"Mo'in ends the etymological footnote on گدا with 'قس: عربی: تکدیه، و اکداء' — he himself points from Persian گدا to Arabic تکدیه, which is the arrow Nourai draws.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Gwhen 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷʰen- 'to swell, abound, be full'\",\n      \"note\": \"The root box itself is right: Pokorny 491 has 'gʷhen- ,schwellen, strotzen, Fülle‘; gʷhono-s ,üppig, reichlich‘' with Skt. ā-ghaná-, ghaná-, Gk. euthenéō and — the Iranian witness Nourai does NOT use — 'npers. ā-gandan ,anfüllen‘, āganiš ,voll‘'; Watkins/AHD likewise: 'gʷhen-2. To swell, abound. [Pok. 1. gʷhen- 491].' What is wrong on this chart is not the root but both branches hung under it. Branch A (šan / šyaŋha / āšiyān / golšan / kāšān / Hušang) belongs to the 'dwell, settle' root *ḱey-/*tḱey-: Bartholomae AiW col. 1707 gives 'j. šayana- n. ‚Wohnstätte, Aufenthalt, Heimat‘' (Armenian loan šēn 'village'), Mo'in's own footnote in the Borhan page Nourai cites (BQT:46) derives آشیان from 'ā- + šyāna- بمعنی جای و سرای، بارتولمه ۱۷۰۷', and Wiktionary's Persian suffix -šan is 'from *tḱey- “to cultivate, settle, live”, cf. Avestan šaiiana- “place of residence”'. Nourai's own NOTE ('See Kweye for another possible root of āšīyān(eh)') points at exactly this, and modern scholarship takes that side without hesitation. Branch B (Skt khaṇḍa > qand > candy) is a real and well-documented chain word-for-word, but its head is not Indo-European at all: AHD calls khaṇḍaḥ 'piece, fragment' 'perhaps of Munda origin' and Klein 'prob. of Dravidian origin (cp. Tamil kaṇṭu “candy”)'. So the root is confirmed but neither branch actually descends from it. Page image kept at data/verification/sources/refs/ocr/BOOK/212.png.\",\n      \"note_fa\": \"خودِ ریشه درست است: پوکورنی در ص۴۹۱ ریشهٔ *gʷʰen- «آماسیدن، پُر شدن، فراوانی» را آورده و از ایرانی هم «فارسی نو ā-gandan (آکندن) و āganiš (آکنده)» را گواه گرفته است؛ واتکینز نیز همین را می‌گوید. اما هیچ‌یک از دو شاخه‌ای که نورایی زیر این ریشه آویخته است به آن نمی‌رسد. شاخهٔ نخست (شن، شیانگه، آشیان، گلشن، کاشان، هوشنگ) از ریشهٔ *ḱey-/*tḱey- «آرمیدن، جای گرفتن، سکنا گزیدن» است: بارتولمه در ستون ۱۷۰۷ فرهنگ ایرانی باستان «šayana- به معنی جایگاه، خانه، میهن» را آورده و معین نیز در همان صفحه‌ای از برهان قاطع که نورایی ارجاع داده (ص۴۶) «آشیان» را «مرکب از پیشوند ā و šyāna- به معنی جای و سرای، بارتولمه ۱۷۰۷» دانسته است؛ خودِ نورایی هم در یادداشت نمودار به ریشهٔ «Kweye» اشاره کرده است. شاخهٔ دوم (خَنْدَهٔ سنسکریت ← قند ← candy) زنجیرهٔ وام‌گیری‌اش درست است، ولی سرِ آن اصلاً هندواروپایی نیست: فرهنگ AHD خَنْدَه را «شاید از خاستگاه مونداـ» و کلاین آن را «احتمالاً دراویدی» می‌داند. پس ریشه درست است ولی پیوند هر دو شاخه به آن نادرست.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B4%D9%86\",\n        \"https://www.ahdictionary.com/word/search.html?q=candy\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:491\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 148 (printed 491): 'gʷhen- ,schwellen, strotzen, Fülle‘; gʷhono-s ,üppig, reichlich‘. Ai. a-ghaná- ,schwellend, strotzend, üppig‘, ghaná- ,dicht, dick‘ ...; npers. ā-gandan ,anfüllen‘, āganiš ,voll‘; arm. yogn ,multum‘; gr. εὐθενής ...' — root, gloss and page exactly as cited. Note that Pokorny's Iranian witness is āgandan, not šan or khaṇḍa.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷhen-2 (AHD_watkins1985.txt line 545)\", \"stance\": \"supports\", \"note\": \"'gʷhen-2. To swell, abound. Suffixed form *gʷhen-eyo- in Greek euthenein ... [Pok. 1. gʷhen- 491.]' — same root, gloss and Pokorny page.\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I (via Pokorny's own back-reference on p.491)\", \"stance\": \"partial\", \"note\": \"Pokorny's entry for this root closes with the WP reference; the local WLD Bd. I scan confirms the volume covers the gʷh- series (leaf 681 = p.673), but no Iranian 'house' word or Sanskrit khaṇḍa is listed anywhere under this root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"šan, šyangh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"There is no Avestan or Old Persian word *šan; what Avestan actually has is šayana- n. 'Wohnstätte, Aufenthalt, Heimat' (Bartholomae, AiW col. 1707, with the Armenian loanword šēn 'village'), a -ana- derivative of the verb šay-/sōi- 'to lie, rest, dwell' (Gathic syā-), i.e. PIE *ḱey-/*tḱey- 'to lie down, settle' — the root Nourai himself cross-references as 'Kweye'. 'šyangh' is the second element of the Avestan proper name Haošyaŋha- (the first Pēšdādian king), which Mo'in, following Pourdavoud, glosses in the Borhan footnote as 'کسی که منازل خوب فراهم سازد' ('he who provides good dwellings'), i.e. hu- 'good' + a *šyaŋha- of the same 'dwelling' family; the second element is in fact contested (others attach it to Av. saŋh- 'to pronounce'). Either way the family belongs to *ḱey-, not to *gʷʰen- 'to swell': Pokorny p.491 lists no Iranian 'house' word under this root, and *gʷʰen- would give Iranian ǰan-/gan-, not šan-. Nourai's own NOTE ('cognate with kan 1, xan, gan 1: to dig out and mound up (a shelter)') and his cross-reference to Kweye show he was aware of the alternatives; modern scholarship takes the Kweye side. The whole branch rests on ZMA (Jonaydi, Zendegi va Mohajerat-e Aryaian), a popular, non-academic work.\",\n          \"derivation_fa\": \"در اوستایی و پارسی باستان واژه‌ای به صورت *šan «خانه» وجود ندارد؛ آنچه هست šayana- «جایگاه، خانه، میهن» است (بارتولمه، فرهنگ ایرانی باستان، ستون ۱۷۰۷، همراه با وام‌واژهٔ ارمنی šēn «ده») که مشتقِ ‑ana- از ستاک فعلی šay-/sōi- «آرمیدن، ساکن شدن» (گاهانی syā-) است، یعنی از ریشهٔ هندواروپایی *ḱey-/*tḱey- — همان که خود نورایی با نام «Kweye» به آن ارجاع می‌دهد. «شیانگه» نیز جزء دوم نام اوستایی Haošyaŋha- (هوشنگ) است که معین به پیروی از پورداود آن را «کسی که منازل خوب فراهم سازد» معنی کرده است. در هر حال این خانواده به ریشهٔ *gʷʰen- «آماسیدن» نمی‌رسد: پوکورنی در ص۴۹۱ هیچ واژهٔ ایرانی به معنی «خانه» زیر این ریشه نیاورده و *gʷʰen- در ایرانی به ǰan-/gan- می‌انجامد نه šan-. پژوهش امروزی این پیوند را رد می‌کند و همان ریشهٔ «آرمیدن/سکنا گزیدن» را می‌گیرد؛ تکیهٔ نورایی هم بر کتاب غیردانشگاهی «زندگی و مهاجرت آریاییان» فریدون جنیدی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ZMA:49-51\", \"status\": \"not_checked\", \"note\": \"Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian (Bonyad-e Neyshabur 1374): refs_online.json records 'purchase only; no open copy found on archive.org, ketabnak, noorlib or the open web'. It is also not an etymological reference of standing.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1707 (BRT.txt line ~28400)\", \"stance\": \"contradicts\", \"note\": \"'j. šayana- n. ‚Wohnstätte, Aufenthalt, Heimat‘. KompE. — arm. LW. šēn ‚Dorf‘' — filed under the verb šay- 'to lie, dwell', not under any gʷhen- root; Bartholomae has no Avestan *šan.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny p.491, s.v. gʷhen- 'schwellen, strotzen, Fülle'\", \"stance\": \"silent\", \"note\": \"The entry lists Skt. ā-ghaná-/ghaná-, Arm. yogn, Gk. εὐθενής, Lith. ganà, aksl. goněti and NPers. ā-gandan — no Iranian word for 'house' anywhere.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian Lexicon, searched for šan-/šyan-\", \"stance\": \"silent\", \"note\": \"No Old Persian word of this shape is in Kent's lexicon; the language label 'Old Persian' on this box has no support.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"šân; â-šân-ak; hu-šangh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the three forms are genuine Middle Persian words, but they belong to the 'dwell' root, not to *gʷʰen-. MacKenzie's Concise Pahlavi Dictionary p.14 has 'āšyān(ag) [ʾsydʼn(k) | (M ʾhyʾng), N āšyāna] nest, lair' — that is Nourai's 'â-šân-ak', more accurately āšyānag, from *ā- + šyāna- 'dwelling place' (Av. šayana-, Bartholomae AiW 1707) with the MP diminutive/nominal -ag. 'hu-šangh' is the Pahlavi royal name Hōšang < Av. Haošyaŋha-, whose second element Mo'in (after Pourdavoud) glosses in Borhan p.2395 as 'one who provides good dwellings' — again from the 'dwelling' family. A bare Pahlavi *šān 'house, shelter' is not in MacKenzie or Nyberg; it is an abstraction from the New Persian suffix -šan/-šān. Middle Persian for 'house' is mān, xānag, wis. So the forms are (mostly) real, the internal analysis is defensible, and only the attachment to 'Gwhen 1: to swell, fill' is wrong.\",\n          \"derivation_fa\": \"دو صورت از سه صورت این جعبه واژه‌های راستین فارسی میانه‌اند، اما به ریشهٔ «آرمیدن/سکنا گزیدن» می‌رسند نه به *gʷʰen-. مکنزی در فرهنگ کوچک پهلوی (ص۱۴) āšyān(ag) «آشیانه، لانه» را آورده است — همان «â-šân-ak» نورایی — که از *ā- + šyāna- «جای، سرای» (اوستایی šayana-، بارتولمه ستون ۱۷۰۷) با پسوند ‑ag پهلوی ساخته شده. «hu-šangh» نیز نام شاهیِ پهلوی Hōšang < اوستایی Haošyaŋha- است که معین به نقل از پورداود در برهان ص۲۳۹۵ آن را «کسی که منازل خوب فراهم سازد» معنی کرده است. اما *šān تنهای پهلوی به معنی «خانه» نه در مکنزی هست و نه در نیبرگ؛ واژهٔ پهلوی «خانه» mān، xānag و wis است. پس صورت‌ها بیشترشان درست‌اند و تنها پیوند آنها به ریشهٔ «آماسیدن» نادرست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:46\", \"status\": \"contradicts\", \"note\": \"Borhan-e Qate' vol. 1, BQT_v1_pages.txt leaf 256, s.v. آشیان 'خانهٔ مرغان - و سقف خانه باشد'; Mo'in's footnote 4 reads 'مرکب از پیشوند ā و šyāna- بمعنی جای و سرای، ارمنی [šēn] (بمعنی ده، قریه) «بارتولمه ۱۷۰۷»' — the page Nourai cites derives the word from Av. šyāna-/šayana- (AiW col. 1707), i.e. from the 'dwell' root, not from a 'swell, fill' root.\"},\n            {\"ref\": \"ZMA:49-51\", \"status\": \"not_checked\", \"note\": \"Jonaydi's Zendegi va Mohajerat-e Aryaian: no open copy exists (refs_online.json: 'purchase only').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, A Concise Pahlavi Dictionary, p. 14 s.v. āšyān(ag)\", \"stance\": \"partial\", \"note\": \"'āšyān(ag) [ʾsydʾn(k) | (M ʾhyʾng), N āšyāna] nest, lair' — confirms Nourai's â-šân-ak as MP āšyānag, but MacKenzie has no simple šān 'house' (his words for house are mān, xānag, wis).\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary), searched šān / āšyān / hušang\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt returns no headword for any of the three forms.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1707\", \"stance\": \"contradicts\", \"note\": \"šayana- 'Wohnstätte' is filed under the verb šay- 'to lie, dwell'; the Middle Persian forms continue it, so the ultimate root is *ḱey-, not *gʷhen-.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"šan «شَن»; šandaf «شَندَف»; Hŭžšang «هوشنگ»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Persian material is real and correctly grouped with itself, but not with this root. Persian شن /-شن /-شان /-شانه is a productive suffix of place: Wiktionary derives it from PIE *tḱey- 'to cultivate, settle, live', citing Avestan šaiiana- 'place of residence' and Old Armenian šēn, and gives گلشن golšan 'place of flowers, rose-garden' and تبشن tabšan 'hot spring' as examples; the same element is in کاشان/کاشانه kāšān(e) and, with the prefix ā-, in آشیان/آشیانه āšiyān(e) 'nest' < MP āšyānag (MacKenzie p.14) < *ā-šyāna-. Horn's Grundriss no. 35 says the same in 1893: 'āsyāne, āsyān ‚Nest‘. ā + aw. šōi- bezw. gāth. syā- ‚ruhen‘, oder wohl bereits ‚wohnen‘ (Nöldeke)'. Nourai's own NOTE on this box concedes the point ('See “Kweye” for another possible root of “āšīyān(eh)”'); modern scholarship takes the Kweye (*ḱey-) side for the whole set, so the arrow from 'Gwhen 1: to swell, fill' fails. Hušang هوشنگ is Av. Haošyaŋha- > MP Hōšang, and Mo'in in the very page cited (BQT:2395) reports Pourdavoud's gloss 'کسی که منازل خوب فراهم سازد' — which does support Nourai's rendering 'owner of good household'. Note also a printed error: the book sets the name as 'Hŭžšang' with a stray ž (see the page image); the Persian is هوشنگ = Hōšang/Hūšang, and the JSON reproduces the printed form faithfully.\",\n          \"derivation_fa\": \"مادهٔ فارسی این جعبه راستین است و اعضایش به‌درستی کنار هم نشسته‌اند، ولی به این ریشه نمی‌رسند. «شن / ـ شن / ـ شان / ـ شانه» پسوند مکان است و ویکی‌واژه آن را از ریشهٔ *tḱey- «سکنا گزیدن، آباد کردن» می‌داند و اوستایی šaiiana- «جایگاه» و ارمنی کهن šēn را گواه می‌آورد؛ نمونه‌ها: «گلشن» (جای گل)، «تبشن» (چشمهٔ گرم)، «کاشان/کاشانه» و با پیشوند ā-: «آشیان/آشیانه» از فارسی میانهٔ āšyānag (مکنزی ص۱۴) از *ā-šyāna-. هرن نیز در ۱۸۹۳ (شمارهٔ ۳۵) همین را گفته است: «āsyāne از ā + اوستایی šōi-/گاهانی syā- به معنی آرمیدن یا سکونت گزیدن». خودِ نورایی هم در یادداشت همین جعبه به ریشهٔ «Kweye» اشاره کرده است؛ ریشه‌شناسی امروزی همان را می‌پذیرد و پیوند به «Gwhen 1» را رد می‌کند. «هوشنگ» از اوستایی Haošyaŋha- و فارسی میانهٔ Hōšang است و معین در همان صفحهٔ ۲۳۹۵ برهان، به نقل از پورداود، آن را «کسی که منازل خوب فراهم سازد» معنی کرده که با ترجمهٔ نورایی می‌خواند. یک نکتهٔ چاپی هم هست: کتاب این نام را «Hŭžšang» با «ž» زائد چاپ کرده است؛ صورت درست Hōšang/Hūšang است و خوانش اسکن درست بوده — خطا از خودِ کتاب است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"Hŭžšang\",\n          \"correct_form\": \"Hūšang / Hōšang (هوشنگ)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%D9%86\",\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%84%D8%B4%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B4%DB%8C%D8%A7%D9%86%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ZMA:49-50\", \"status\": \"not_checked\", \"note\": \"Jonaydi, Zendegi va Mohajerat-e Aryaian — no open copy (refs_online.json: purchase only).\"},\n            {\"ref\": \"BQT:46\", \"status\": \"contradicts\", \"note\": \"BQT_v1_pages.txt leaf 256, footnote to آشیان: 'مرکب از پیشوند ā و šyāna- بمعنی جای و سرای ... «بارتولمه ۱۷۰۷»' — Mo'in derives it from the 'dwelling' root, which is Nourai's own alternative 'Kweye'.\"},\n            {\"ref\": \"BQT:2395\", \"status\": \"partial\", \"note\": \"ref_page.py BQT:2395 (v4), s.v. هوشنگ, footnote 1: 'در اوستا Haošyaŋha-. معنی لفظی این کلمه به قول پورداود ... چنین است: کسی که منازل خوب فراهم سازد. به نام مرکب از: هوش + هنگ چنان که برخی پنداشته‌اند نیست.' Supports the gloss 'owner of good household' but says nothing that would attach the name to a 'swell, fill' root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie, no. 35 (HRN.txt line 740)\", \"stance\": \"contradicts\", \"note\": \"'35. āsyāne, āsyān ‚Nest‘. ā + aw. šōi- bezw. gāth. syā- ‚ruhen‘, oder wohl bereits ‚wohnen‘ (Nöldeke, mündliche Mitteilung).' Horn also asks at no. 1034 (nišēm 'Nest') whether āsyāne belongs with nišastan — again the *ḱey- family.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 14\", \"stance\": \"partial\", \"note\": \"'āšyān(ag) ... nest, lair' confirms the Middle Persian ancestor of آشیان/آشیانه but gives no 'swell' connection.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, searched گلشن / کاشان / آشیان as headwords\", \"stance\": \"silent\", \"note\": \"Aryanpur's Persian IE-roots dictionary has no headword for any of them.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"ğanâ; xanda\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Neither Sanskrit word supports the arrow. (a) 'ğanâ : ditch' is not a Sanskrit lexeme the dictionaries know; the Sanskrit words for 'ditch, pit, mine' are khā-, khani-, khāta-, from the verb khan- 'to dig' — the family Nourai alludes to in his own note on node #1 ('kan 1, xan, gan 1: to dig out'). khan- is not from *gʷʰen- 'to swell': the *gʷʰen- reflexes in Sanskrit are ā-ghaná- 'swelling, abundant' and ghaná- 'dense, compact mass' (Pokorny 491), which is a quite different word. The printed page really does read 'ğanâ' (page image kept), so the extraction is faithful and the odd form is the book's. (b) khaṇḍa- खण्ड 'piece, fragment; a lump of candied sugar' (with the derivative khaṇḍaka-) is a real and central word — it is the true source of qand/candy — but it is not inherited Indo-European at all: AHD s.v. candy calls khaṇḍaḥ 'piece, fragment, perhaps of Munda origin', and Klein (p. 230-31 s.v. candy) says Arab. qand and 'OI. khaṇḍakaḥ “candy” is prob. of Dravidian origin. Cp. Tamil kaṇṭu “candy”, kaṭṭu “to harden, condense”'. So the words below this box are genuine, but their attachment to PIE *gʷʰen- is rejected by modern scholarship.\",\n          \"derivation_fa\": \"هیچ‌یک از دو واژهٔ سنسکریتِ این جعبه پیوند نمودار را نمی‌رساند. نخست، «ğanâ» به معنی «گودال» واژه‌ای نیست که فرهنگ‌های سنسکریت بشناسند؛ واژه‌های سنسکریت برای «گودال، کان» khā-، khani- و khāta- از ستاک khan- «کندن» است — همان خانواده‌ای که خود نورایی در یادداشت گرهٔ نخست («کن، خن، گن») به آن اشاره کرده — و khan- از *gʷʰen- «آماسیدن» نیست؛ بازتاب‌های سنسکریتِ *gʷʰen- نزد پوکورنی ā-ghaná- و ghaná- «انبوه، توده» است. صفحهٔ چاپی هم عیناً «ğanâ» دارد، پس خطای خوانش اسکن نیست بلکه صورتِ خودِ کتاب است. دوم، khaṇḍa «پاره، تکه؛ قند» واژه‌ای راستین و در واقع سرچشمهٔ «قند» و candy است، ولی هندواروپایی موروثی نیست: فرهنگ AHD آن را «شاید از خاستگاه موندا» و کلاین (ص۲۳۰-۲۳۱) آن را «احتمالاً دراویدی، قس تامیلی kaṇṭu قند و kaṭṭu سفت شدن» می‌داند. پس پژوهش امروزی پیوند این شاخه را به ریشهٔ *gʷʰen- رد می‌کند.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"ğanâ : ditch\",\n          \"correct_form\": \"Skt khā-/khani-/khāta- 'ditch, pit' (from khan- 'to dig')\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/search.html?q=candy\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PRT:75\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958) is lending-only on archive.org (refs_online.json kind 'archive_restricted'); no readable copy here, so his page 75 could not be checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.491 s.v. gʷhen-\", \"stance\": \"contradicts\", \"note\": \"The Sanskrit reflexes Pokorny lists are 'a-ghaná- ‚schwellend, strotzend, üppig‘, ghaná- ‚dicht, dick‘, m. ‚kompakte Masse‘' — neither a word for 'ditch' nor khaṇḍa.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein, A Comprehensive Etymological Dictionary, pp. 230-231 s.v. candy\", \"stance\": \"contradicts\", \"note\": \"'... fr. Arab. qandi ... adj. formed fr. qand “cane sugar”, which, like OI. khaṇḍakaḥ “candy”, is prob. of Dravidian origin. Cp. Tamil kaṇṭu “candy”, kaṭṭu “to harden, condense”.'\"},\n            {\"src\": \"AHD\", \"where\": \"American Heritage Dictionary online, s.v. candy\", \"stance\": \"contradicts\", \"note\": \"'... from qand, lump of crystallized sugar, from an Indic source akin to Pali kaṇḍa-, from Sanskrit khaṇḍakaḥ, from khaṇḍaḥ, piece, fragment, perhaps of Munda origin.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"qand «قند»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian قند qand 'loaf/crystallised cane sugar' does come from Sanskrit khaṇḍa- 'piece, lump (of sugar)', as Nourai draws — the transmission being the sugar trade out of India from Sasanian times on (Persia had cane-sugar refining at Gondēšāpur by the 6th c.). The refinement modern sources add is the shape of the word: the older Persian form is کند kand (with k-), the direct rendering of Skt khaṇḍa; قند with q- is the Arabicised spelling that came back into Persian from Arabic. Mo'in says exactly this in the page Nourai cites: 'قند - بفتح اول. معرّب «کند» از اصل هندی است. در سانسکریت khaṇḍa بمعنی مطلق قطعه یا پاره، مخصوصاً پارهٔ قند'; Wiktionary's Persian entry likewise: 'Borrowed from Arabic قَنْد (qand), displacing older کند (kand)', while the Arabic entry has 'From Persian کند (kand)'. Nourai's derived forms قنداغ، قنداب، قنددان، قندران are ordinary Persian compounds of qand, and the Hāfez couplet he quotes ('که حاجتت به علاج گلاب و قند مباد') attests the word.\",\n          \"derivation_fa\": \"«قند» فارسی به معنی «شکر بسته و کلوخه‌شده» چنان‌که نورایی رسم کرده از سنسکریت khaṇḍa «پاره، تکه (قند)» است و راه انتقالش بازرگانی نیشکر از هند بوده است (پالایش نیشکر در گندی‌شاپور از سدهٔ ششم میلادی رواج داشت). تنها نکته‌ای که پژوهش امروزی می‌افزاید صورت واژه است: صورت کهن‌تر فارسی «کند» (با ک) است که برگردان مستقیم khaṇḍa است و «قند» با «ق» صورت معرّب آن است که از عربی به فارسی بازگشته. معین در همان صفحه‌ای که نورایی ارجاع داده می‌نویسد: «قند ... معرّب کند از اصل هندی است. در سانسکریت khaṇḍa بمعنی مطلق قطعه یا پاره، مخصوصاً پارهٔ قند»؛ ویکی‌واژه نیز همین را می‌گوید. مشتق‌های قنداغ، قنداب، قنددان و قندران ترکیب‌های عادی فارسی‌اند و بیت حافظ گواه کاربرد واژه است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%AF\",\n            \"https://www.etymonline.com/word/candy\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1544\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:1544 (v3), Mo'in's footnote s.v. قند: 'قند - بفتح اول. معرّب «کند» از اصل هندی است. در سانسکریت khaṇḍa بمعنی مطلق قطعه یا پاره، مخصوصاً پارهٔ قند یا تکهٔ قند. همین کلمه وارد زبانهای اروپایی شده: candi (ف)، candy (انگ)، Kandis (آلم)، candito (ایتالیایی) ... «هرمزدنامه ص۲۳۷»' — the whole chain Nourai draws, in the very page he cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, p. 221\", \"stance\": \"supports\", \"note\": \"'qand: „Kandis“ ← pers. کند kand; skr. khand; frz. candi, engl. candy, dtsch. Kandis.'\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss, searched qand / Zucker\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss treats inherited Iranian vocabulary; qand is not among his entries.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, searched قند as headword\", \"stance\": \"silent\", \"note\": \"No headword قند in Aryanpur.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Arabic\",\n          \"words\": \"qandat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic قَنْد qand 'solidified cane-sugar juice, rock sugar' is a Persian loanword, exactly as the arrow says, and it is the form from which the European words were taken (through the nisba adjective قَنْدِيّ qandī in the phrase سُكَّر قَنْدِيّ sukkar qandī 'sugar in lumps'). Addi Shir: '(القند) عسل قصب السكر اذا جمد، معرّب کند' ('al-qand: the juice of sugarcane when it has set, Arabicised from [Persian] kand'); Asbaghi p.221 the same. Nourai's citation form 'qandat' is the noun with tā' marbūṭa (قَنْدَة, a single lump), a legitimate variant but not the usual dictionary headword — Klein and AHD cite qand and the adjective qandī. Klein p.230-31 differs from Nourai on one point only: he does not name Persian as the intermediary, taking Arab. qand straight to a Dravidian source.\",\n          \"derivation_fa\": \"«قَنْد» عربی به معنی «عسل نیشکر چون ببندد، شکر کلوخه» دقیقاً چنان‌که نورایی نشان داده وام‌واژه‌ای از فارسی است و همین صورت است که از راه صفت نسبی «قَنْدیّ» در ترکیب «سُکَّر قَنْدیّ» به زبان‌های اروپایی رفته است. ادّی شیر در «الالفاظ الفارسیة المعرّبة» می‌نویسد: «(القند) عسل قصب السکر اذا جمد، معرّب کند»؛ اصبغی نیز در «وام‌واژه‌های فارسی در عربی» (ص۲۲۱) همین را می‌آورد. صورتی که نورایی نوشته («qandat») همان «قَنْدة» با تای گرد است — گونه‌ای درست ولی نه صورت سرمدخلی. کلاین تنها در یک نکته با نورایی اختلاف دارد: او واسطهٔ فارسی را نام نمی‌برد و قندِ عربی را یکسره به خاستگاهی دراویدی می‌رساند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%AF\",\n            \"https://www.ahdictionary.com/word/search.html?q=candy\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:231\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 132 (printed pp. 229-231), s.v. candy: 'Shortened fr. sugar candy, fr. F. (sucre) candi, fr. It. (zucchero) candi(to), “sugar candy”, fr. Arab. qandi, “crystallized, candied”, adj. formed fr. qand, “cane sugar”, which, like OI. khaṇḍakaḥ, “candy”, is prob. of Dravidian origin.' Klein confirms the Arabic word and the route onward to French/English, but does not make Arabic borrow it from Persian, and rejects the Indo-European origin of the whole group.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, p. 221 (PLA_pages.txt leaf 236)\", \"stance\": \"supports\", \"note\": \"'qand: „Kandis“ ← pers. kand ← skr. khand' — Arabic qand explicitly classed as a Persian loanword.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-Alfaz al-Farisiyya al-Mu'arraba (AFM_alt.txt line 5095)\", \"stance\": \"supports\", \"note\": \"'(القند) عسل قصب السكر اذا جمد معرب کند وهو قصب السكر' — 'Arabicised from kand'.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch, entry 1052 (printed p. 86)\", \"stance\": \"supports\", \"note\": \"'1052. Ar. kandī: Adj. zu kand nach ar. Originalwörterbüchern „eingedickter Zuckerrohrsaft“ ... hieraus it. zucchero candi, frz. sucre candi, sp. azúcar cando, dtsch. Kandiszucker, ndl. kandij, engl. candy ...'\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box for the Romance stage, and it is correctly placed: the Arabic phrase سُكَّر قَنْدِيّ sukkar qandī reached the West through the Mediterranean sugar trade as Italian zucchero candi(to) and Old French (su)cre candi 'sugar candy' (13th c.), whence the French verb candir 'to candy'. Klein: 'fr. F. (sucre) candi, fr. It. (zucchero) candi(to), “sugar candy”, fr. Arab. qandi'; AHD: 'partial translation of Old French sucre candi, ultimately from Arabic sukkar qandī'. Lokotsch no. 1052 lists the same set (frz. sucre candi, it. zucchero candi, dtsch. Kandiszucker).\",\n          \"derivation_fa\": \"این جعبهٔ خالی حلقهٔ رومانسِ زنجیره است و درست جای گرفته: ترکیب عربی «سُکَّر قَنْدیّ» از راه بازرگانی شکر در مدیترانه به ایتالیایی zucchero candi(to) و فرانسهٔ کهن (su)cre candi «قند» (سدهٔ سیزدهم میلادی) رسید و از آن فعل فرانسوی candir «قندپوش کردن» ساخته شد. کلاین و فرهنگ AHD و لوکوچ (شمارهٔ ۱۰۵۲) هر سه همین را می‌گویند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/candy\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; the link is covered by the references on the adjacent Arabic and English boxes (KLN:231, AHD:196).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, pp. 230-231 s.v. candy\", \"stance\": \"supports\", \"note\": \"'fr. F. (sucre) candi, fr. It. (zucchero) candi(to), “sugar candy”, fr. Arab. qandi ... F. candir, “to candy”.'\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch entry 1052 (p. 86)\", \"stance\": \"supports\", \"note\": \"'hieraus it. zucchero candi, frz. sucre candi ... dazu die Vb. it. candire, frz. candir „überzuckern“.'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"candy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English candy is first recorded in the late 13th century as (sugre-)candi 'crystallised cane sugar', shortened from sugar candy, a partial translation of Old French sucre candi < Italian zucchero candi(to) < Arabic sukkar qandī < qand < Persian kand/qand < Sanskrit khaṇḍa. Etymonline: 'late 13c., “crystallized sugar”, from Old French çucre candi “sugar candy”, ultimately from Arabic qandi, from Persian qand “cane sugar”, probably from Sanskrit khanda “piece (of sugar)”'; AHD (Nourai's own reference, p.196 of the 1975 New College edition) prints the same bracket. The verb 'to candy' is a later back-formation from candi, which was mistaken for a past participle (Klein). The American widening of the sense from 'crystallised sugar' to any sweet dates from the late 19th century.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی candy نخستین بار در اواخر سدهٔ سیزدهم میلادی به صورت (sugre-)candi «شکر بلورین» ثبت شده که کوتاه‌شدهٔ sugar candy است و آن نیز برگردان نیمه‌ترجمه‌ای از فرانسهٔ کهن sucre candi < ایتالیایی zucchero candi(to) < عربی «سُکَّر قَنْدیّ» < «قَنْد» < فارسی کند/قند < سنسکریت khaṇḍa است. اتیمآنلاین و فرهنگ AHD (همان مرجعی که نورایی داده) هر دو همین زنجیره را می‌آورند. فعل to candy بعدها با گَشتِ واژگانی از candi ساخته شد که آن را صفت مفعولی پنداشتند (کلاین). گسترش معنایی آن در آمریکا از «شکر بلورین» به هر شیرینی از اواخر سدهٔ نوزدهم است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/candy\",\n            \"https://www.ahdictionary.com/word/search.html?q=candy\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:196\", \"status\": \"supports\", \"note\": \"Nourai's AHD numbers below 1505 are pages of the 1975 New College main dictionary, where 'candy' falls on p.196. The 1975 text is not open online, but the current AHD entry (ahdictionary.com, archived) carries the same etymology: '[Middle English candi, crystallized cane sugar, short for sugre-candi, partial translation of Old French sucre candi, ultimately from Arabic sukkar qandī : sukkar, sugar + qandī, consisting of sugar lumps (from qand, lump of crystallized sugar, from an Indic source akin to Pali kaṇḍa-, from Sanskrit khaṇḍakaḥ, from khaṇḍaḥ, piece, fragment, perhaps of Munda origin).]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, pp. 230-231 s.v. candy\", \"stance\": \"supports\", \"note\": \"'candy, n., crystallized sugar. — Shortened fr. sugar candy, fr. F. (sucre) candi ... fr. Arab. qandi'; and 'candy, tr. and intr. v. ... back formation fr. candi, “sugar candy”, which was mistaken for a past participle.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary, searched CANDY\", \"stance\": \"silent\", \"note\": \"The concise edition has no separate 'candy' entry (only 'Sugar. (F. — Span. — Arab. — Pers. — Skt.)'), so Skeat is silent here.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary vol. 1, searched candy\", \"stance\": \"silent\", \"note\": \"The OCR of vol. 1 does not yield a readable bracketed etymology for the headword candy.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T15:13:53.951Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-212.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T15:13:58.219Z] TOOL CALL #89: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-212.json > /dev/null && echo JSON-OK && python3 tools/verify_check.py 212"
}
```


### [2026-09-06T15:14:00.713Z] TOOL RESULT

```
JSON-OK
nodes verified: 12/12
node verdicts: {'confirmed': 6, 'plausible': 2, 'disputed': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'not_checked': 8, 'contradicts': 2, 'partial': 2}
books consulted: {'supports': 13, 'partial': 4, 'silent': 11, 'contradicts': 6} | by book: {'KLN': 4, 'BRT': 3, 'HRN': 3, 'ARY': 3, 'KNT': 2, 'HUB': 2, 'Encyclopaedia Iranica': 2, 'AFM': 2, 'POK': 2, 'PHD': 2, 'PLA': 2, 'LKT': 2, 'BQT': 1, 'NYB': 1, 'AHD': 1, 'SKT': 1, 'FSD': 1}
```


## [2026-09-06T15:14:22.809Z] AGENT

Page 212 (book p. 182) verified — `data/verification/page-212.json`, `verify_check.py 212` reports 0 PROBLEM lines.

**Counts:** 12/12 nodes — confirmed 6, plausible 2, disputed 4; both roots confirmed. Ref checks: 10 supports, 2 partial, 2 contradicts, 8 not_checked (FVF, FVA, ZMA, PRT have no accessible copy).

**Disputed / flagged**
- **Gwhen 1 #1 (Av./OP `šan, šyangh` "house")** — no Avestan *šan exists; Bartholomae AiW col. 1707 has `šayana-` "Wohnstätte" under the verb *šay-* "to dwell" (PIE *ḱey-/*tḱey-), not *gʷʰen- "to swell". Only source is ZMA (Jonaydi), unavailable and non-academic.
- **Gwhen 1 #2 (Pahlavi `šân, â-šân-ak, hu-šangh`)** — MP `āšyānag` is real (MacKenzie p.14) but continues *šyāna-* "dwelling"; a bare Pahlavi *šān "house" is in neither MacKenzie nor Nyberg. BQT:46, the page Nourai cites, actually contradicts him (Mo'in: "مرکب از پیشوند ā و šyāna- ... بارتولمه ۱۷۰۷").
- **Gwhen 1 #3 (Persian `šan/golšan/kāšān/āšiyān`)** — same problem; Horn no. 35 and Wiktionary both put the -šan suffix under *tḱey- "settle". Nourai's own NOTE ("see Kweye") concedes it.
- **Gwhen 1 #4 (Sanskrit `ğanâ, xanda`)** — `khaṇḍa` is non-IE (AHD "perhaps of Munda origin"; Klein "prob. Dravidian"); `ğanâ` "ditch" is not a Sanskrit word the dictionaries know (Skt has khā-/khani-/khāta- from khan- "dig").

**Book misprints (extraction is faithful — no data fix needed)**
- `Hŭžšang` for هوشنگ (stray ž); correct Hūšang/Hōšang.
- `ğanâ` for the Sanskrit "ditch" word.
- Avestan ǰ written `ž` in `ža 3 / žaidhyemi / žadiyâmiy / a-žasta` while `hu-jasta` in the same box uses j.

**Notable confirmations:** POK 488 + WLD I 673 + Kent's lexicon give Av. ǰaiδyemi / OP jadiyāmiy verbatim; Horn no. 470 and Mo'in (BQT 717/1453) confirm xojaste/farxojaste < Av. *hu-ǰasta-; Iranica (Bosworth, BEGGING i) confirms Persian gadā → Arabic kudya/takdīa → Persian تکدّی; Mo'in (BQT 1544), Asbaghi p.221, Addi Shir, Lokotsch 1052, Klein 230-31, Etymonline and AHD confirm the whole khaṇḍa → kand/qand → Arabic → French → candy chain. `gedâ` itself is only *plausible*: Mo'in derives it from Av. gad- "to beg" as Nourai does, but Wiktionary prefers Av. gaδa- "robber".

No extraction errors found; page image archived at `data/verification/sources/refs/ocr/BOOK/212.png`.
