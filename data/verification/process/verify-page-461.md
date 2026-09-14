# Verification process log — verify-page-461


## [2026-09-14T02:27:34.442Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 461 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-461.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-461.json. Write /home/sfmqrb/git/rishe/data/verification/page-461.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 461` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:35.448Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:36.296Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:36.311Z] TOOL RESULT

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


## [2026-09-14T02:27:36.856Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-461.txt"
}
```


### [2026-09-14T02:27:36.880Z] TOOL RESULT

```
1	=== PDF page 461 (book page 431) ===
2	--- entry 0 ---
3	ROOT Smerd -> redirect to Mer 2
4	--- entry 1 ---
5	ROOT [Semitic] Š.m.š : sun  (refs KLN:1379)
6	#1 (parent #0) [Arabic] refs=KLN:1379 | šams : sun
7	  #2 (parent #1) [Persian] refs=MON:2075 | šams «شمس» : sun | extra: شمسی ، شمسه ، مُشمّس
8	#3 (parent #0) [Hebrew] refs=KLN:1379 | šemeš : sun ; šimšon : a name
9	  #4 (parent #3) [Greek] refs=KLN:1379 | Samson
10	    #5 (parent #4) [Latin] refs=KLN:1379; AHD | Samson
11	      #6 (parent #5) [French] refs=None | 
12	        #7 (parent #6) [Persian] refs=MON5:719 | Sâmson «سامسون» : a male name
13	      #8 (parent #5) [English] refs=KLN:1379 | Samson ; Sampson
14	--- entry 2 ---
15	ROOT [Arabic] S.n.`a : to make, manufacture  (refs FVA:236)
16	#1 (parent #0) [Persian] refs=MON; FVA:236 | san`at «صنعت» : industry | extra: مصنوع ، مصنوعات ، تصنّع ، صانع
17	#2 (parent #0) [Arabic] refs=KLN:108 | dâr-as-sanâ` : house of construction, factory ☞D.v.r
18	  #3 (parent #2) [Greek] refs=None | 
19	    #4 (parent #3) [Italian] refs=KLN:108; LAM:95 | darsena, arsenale : naval dockyard
20	      #5 (parent #4) [English] refs=AHD | arsenal
21	--- entry 3 ---
22	ROOT [Indo-European] Snâ : to flow, swim  (refs POK:971)
23	#1 (parent #0) [Avestan] refs=POK:971; KLN:1030; HUB:15 | snâ : wash, swim ; us-snâ : wash ☞Ud 1
24	  #2 (parent #1) [Persian] refs=BQT:1298; HRN:176; AEF:118 | šenâ «شنا» : swim ; ošnân «اُشنان» : an alkaline plant used in washing, soap | extra: اُشق
25	#3 (parent #0) [Greek] refs=AHD | něsos : island
26	  #4 (parent #3) [English] refs=None | Polynesia ; Indonesia
27	
```


## [2026-09-14T02:27:39.799Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-461.json | head -200",
 "description": "Read page 461 source JSON"
}
```


## [2026-09-14T02:27:40.621Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T02:27:41.130Z] TOOL RESULT

```
{
    "pdf_page": 461,
    "book_page": 431,
    "entries": [
        {
            "root": {
                "name": "Smerd",
                "redirect": "Mer 2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "\u0160.m.\u0161",
                "lang": "Semitic",
                "refs": "KLN:1379",
                "gloss": "sun"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "KLN:1379",
                    "words": [
                        {
                            "translit": "\u0161ams",
                            "gloss": "sun",
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
                    "refs": "MON:2075",
                    "words": [
                        {
                            "translit": "\u0161ams",
                            "gloss": "sun",
                            "script": "\u0634\u0645\u0633"
                        }
                    ],
                    "script_extra": "\u0634\u0645\u0633\u06cc \u060c \u0634\u0645\u0633\u0647 \u060c \u0645\u064f\u0634\u0645\u0651\u0633",
                    "note": null,
                    "quote": {
                        "text": "\u06cc\u0627\u062f \u0628\u0627\u062f \u0622\u0646 \u0634\u0628 \u06a9\u0647 \u0622\u0646 \u0634\u0645\u0633\u0647\u0654 \u062e\u0648\u0628\u0627\u0646 \u062a\u0631\u0627\u0632 - \u0628\u0647 \u0637\u0631\u0628 \u062f\u0627\u0634\u062a \u0645\u0631\u0627 \u062a\u0627 \u0628\u06af\u0647 \u0628\u0627\u0646\u06af \u0646\u0645\u0627\u0632",
                        "poet": "Farrokh\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Hebrew",
                    "refs": "KLN:1379",
                    "words": [
                        {
                            "translit": "\u0161eme\u0161",
                            "gloss": "sun",
                            "script": null
                        },
                        {
                            "translit": "\u0161im\u0161on",
                            "gloss": "a name",
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
                    "lang": "Greek",
                    "refs": "KLN:1379",
                    "words": [
                        {
                            "translit": "Samson",
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
                    "lang": "Latin",
                    "refs": "KLN:1379; AHD",
                    "words": [
                        {
                            "translit": "Samson",
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
                    "refs": "MON5:719",
                    "words": [
                        {
                            "translit": "S\u00e2mson",
                            "gloss": "a male name",
                            "script": "\u0633\u0627\u0645\u0633\u0648\u0646"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 5,
                    "lang": "English",
                    "refs": "KLN:1379",
                    "words": [
                        {
                            "translit": "Samson",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "Sampson",
                            "gloss": null,
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
                "name": "S.n.`a",
                "lang": "Arabic",
                "refs": "FVA:236",
                "gloss": "to make, manufacture"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "MON; FVA:236",
                    "words": [
                        {
                            "translit": "san`at",
                            "gloss": "industry",
                            "script": "\u0635\u0646\u0639\u062a"
                        }
                    ],
                    "script_extra": "\u0645\u0635\u0646\u0648\u0639 \u060c \u0645\u0635\u0646\u0648\u0639\u0627\u062a \u060c \u062a\u0635\u0646\u0651\u0639 \u060c \u0635\u0627\u0646\u0639",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "KLN:108",
                    "words": [
                        {
                            "translit": "d\u00e2r-as-san\u00e2`",
                            "gloss": "house of construction, factory",
                            "script": null,
                            "see": [
                                "D.v.r"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
```


### [2026-09-14T02:27:41.178Z] TOOL RESULT

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


## [2026-09-14T02:27:48.383Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-461.json | sed -n '200,400p'"
}
```


### [2026-09-14T02:27:49.663Z] TOOL RESULT

```
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Greek",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Italian",
                    "refs": "KLN:108; LAM:95",
                    "words": [
                        {
                            "translit": "darsena, arsenale",
                            "gloss": "naval dockyard",
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
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "arsenal",
                            "gloss": null,
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
                "name": "Sn\u00e2",
                "lang": "Indo-European",
                "refs": "POK:971",
                "gloss": "to flow, swim"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:971; KLN:1030; HUB:15",
                    "words": [
                        {
                            "translit": "sn\u00e2",
                            "gloss": "wash, swim",
                            "script": null
                        },
                        {
                            "translit": "us-sn\u00e2",
                            "gloss": "wash",
                            "script": null,
                            "see": [
                                "Ud 1"
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
                    "lang": "Persian",
                    "refs": "BQT:1298; HRN:176; AEF:118",
                    "words": [
                        {
                            "translit": "\u0161en\u00e2",
                            "gloss": "swim",
                            "script": "\u0634\u0646\u0627"
                        },
                        {
                            "translit": "o\u0161n\u00e2n",
                            "gloss": "an alkaline plant used in washing, soap",
                            "script": "\u0627\u064f\u0634\u0646\u0627\u0646"
                        }
                    ],
                    "script_extra": "\u0627\u064f\u0634\u0642",
                    "note": null,
                    "quote": {
                        "text": "\u06a9\u0646\u0648\u0646 \u0627\u062e\u062a\u0631 \u06af\u0627\u0632\u0631 \u0627\u0646\u062f\u0631 \u06af\u0630\u0634\u062a - \u0628\u0647 \u062f\u06a9\u0651\u0627\u0646 \u0634\u062f \u0648 \u0628\u0631\u062f \u0627\u0634\u0646\u0627\u0646 \u0628\u0647 \u062f\u0633\u062a",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "n\u011bsos",
                            "gloss": "island",
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
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "Polynesia",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "Indonesia",
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


## [2026-09-14T02:27:50.456Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','MON','FVA','AHD','POK','HUB','BQT','HRN','AEF','LAM','AFM','PLA','FVQ']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\""
}
```


### [2026-09-14T02:27:51.486Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start wit

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
```


## [2026-09-14T02:27:57.046Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','POK','MON','BQT','LAM']:\n    v=d[k]\n    print('===',k)\n    print('local_file:', v.get('local_file'))\n    print('page_offset:', v.get('page_offset'))\n    print('lookup_hint:', str(v.get('lookup_hint'))[:800])\n    print('scans:', str(v.get('scans'))[:300])\n\""
}
```


### [2026-09-14T02:27:58.149Z] TOOL RESULT

```
=== KLN
local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
page_offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
lookup_hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
scans: None
=== AHD
local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
lookup_hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
scans: None
=== POK
local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
page_offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
lookup_hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
scans: None
=== MON
local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
page_offset: None
lookup_hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
scans: None
=== BQT
local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
lookup_hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | Fo
scans: [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'o
=== LAM
local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt
page_offset: leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
lookup_hint: French headword in caps at line start with running heads like '2 ABRI'.
scans: None
```


## [2026-09-14T02:28:03.160Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i 'samson' KLN_1966.txt | head -20; echo ---; grep -n -i '^arsenal' KLN_1966.txt | head; echo --- ; grep -n -i 'darsena\\|dar as-sina\\|dār aṣ-ṣinā\\|sina.a' KLN_1966.txt | head -20"
}
```


### [2026-09-14T02:28:03.395Z] TOOL RESULT

```
10723:Delilah,  n.,  the  mistress  of  Samson,  who  be¬ trayed  Samson  (Judges,  chapter  16).  —  Heb. Dllildh,  lit.  ‘delicate,  languishing,  amorous’, from  the  base  of  d-l-l,  ‘to  hang  down,  to  lan¬ guish’,  whence  also  dal,  ‘low,  poor,  thin’,  dalldh, ‘hair;  thrum’  (lit.  ‘that  which  hangs  down’); rel.  to  Akkad,  da/alu,  ‘to  be  weak  or  humble", Arab,  da! la,  ‘he  was  low  or  pliant’,  tadaldala, ‘it  hung  down,  dandled’,  Ethiop.  dated,  ‘hang¬ ing  curls’.
33638:Sampson.  —  A  var.  of  Samson.
33644:Samson,  Sampson,  1)  masc.  PN. ;  2)  in  the  Bible  a. judge  distinguished  for  his  enormous  strength. —  Late  L.,  fr.  Gk.  Sap.iJ>&w,  fr.  Heb.  ShimshJn, a  name  derived  fr.  shemesh,  ‘sun’.  Cp.  Aram. shimsha,  Syr.  shemsha,  Arab,  shams  (dissimi- lated  fr.  *shamsh),  Akkad,  shamshu,  Ugar. sh-p-sh,  ‘sun’.
33645:samsonitc,  n.,  a  silver  manganese  sulfantimonite (mineral.)  —  Named  after  the  Samson  mine  in St.  Andreasberg,  Harz.  For  the  ending  see  subst. suff.  -ite.
33646:samson  post,  a  strong  pillar  in  a  ship.  —  Named after  Samson,  in  allusion  to  the  verse:  “Samson took  hold  of  the  two  middle  pillars  upon  which the  house  rested”  etc.  (Judges  16:29).
34872:Shamash,  n.,  the  chief  sun  god  of  Assyria  and Babylon.  —  Akkad,  shamash,  shamshu,  ‘sun; the  god  of  the  sun’,  rel.  to  Heb.  shemesh,  ‘sun’, Aram.shimsha,  Syr.  shemshd,Vgar.  sh-p-sh,  Arab. shams  (dissimilated  fr.  *shamsh),  of  s.m.;  prob. from  the  Semitic  base  s-m-s-m,  ‘to  be  swift’  (said of  the  quivering  sunrays).  Aram,  shumshdna, Arab,  sumsum,  Aram.  shumsh6mdna  (whence through  syncope  shumshdna,  whence  through metathesis  shushmana),  ‘ant ,  are  of  the  same base.  See  Fleischer,  Beitrage  zu  Jacob  Levy’s Worterbuch  iiber  die  Targumim,  II,  pp.  577f. Cp.  Samson.
---
3518:arsenal,  n.,  a  place  for  manufacturing  and  storing ammunition  and  weapons.  —  It.  arsenale  (Olt. arzanale),  ‘dock’,  borrowed — prob.  through  the medium  of  MGk.  d.pm]'tdkt)C, — fr.  Arab,  dar- a?-sind'ah  (whence  also  Sp.  darsena  and  It.  dar- sena,  ‘dock’),  lit.  ‘house  of  construction’,  fr.  ddr, ‘house’,  as-,  assimilated  form  of  al-,  ‘the’,  and Sind'ah,  ‘construction,  art’,  fr.  Sana' a,  ‘he  made’. For  the  ending  of  arsenal  see  adj.  suff.  -al. arsenic,  n.,  a  chemical  element.  —  OF.  (=  F.) arsenic,  fr.  L.  arsenicum,  arrhenicum,  fr.  Gk. dptrsvixov,  appevvxov,  ‘yellow  orpiment',  fr. MPers.  *zarnik,  ‘gold,  golden ;  orpiment’(whence ModPers.-Arab.  zarnikh,  ‘orpiment’),  through the  medium  of  a  Semitic  language;  cp.  Mish- naic  Heb.  zarnikh,  Syr.  zarnikhd,  ‘orpiment’. Cp.  Avestic  zaranya,  Pers.  zar,  ‘gold’,  and  the first  element  in  zermahbub,  and  see  yellow  and words  there  referred  to.  Cp.  also  jargon,  ‘a variety  of  zircon’.  Gk.  apctevtxov,  appsvtx&v, ‘orpiment’,  was  influenced  in  form  by  apcrevtxop, appevixic,  ‘male’,  fr.  ape rc;v,  ap pr,v,  ‘male’.  For the  sense  development  of  MPers.  *zarnik,  cp.  L. auripigmentum,  fr.  aurum,  ‘gold’  (see  orpiment). Derivatives:  arsenic,  arsenic-al,  adjs. arsenious,  adj.,  containing  arsenic.  —  See  ar¬ senic  and  -oils.
---
3518:arsenal,  n.,  a  place  for  manufacturing  and  storing ammunition  and  weapons.  —  It.  arsenale  (Olt. arzanale),  ‘dock’,  borrowed — prob.  through  the medium  of  MGk.  d.pm]'tdkt)C, — fr.  Arab,  dar- a?-sind'ah  (whence  also  Sp.  darsena  and  It.  dar- sena,  ‘dock’),  lit.  ‘house  of  construction’,  fr.  ddr, ‘house’,  as-,  assimilated  form  of  al-,  ‘the’,  and Sind'ah,  ‘construction,  art’,  fr.  Sana' a,  ‘he  made’. For  the  ending  of  arsenal  see  adj.  suff.  -al. arsenic,  n.,  a  chemical  element.  —  OF.  (=  F.) arsenic,  fr.  L.  arsenicum,  arrhenicum,  fr.  Gk. dptrsvixov,  appevvxov,  ‘yellow  orpiment',  fr. MPers.  *zarnik,  ‘gold,  golden ;  orpiment’(whence ModPers.-Arab.  zarnikh,  ‘orpiment’),  through the  medium  of  a  Semitic  language;  cp.  Mish- naic  Heb.  zarnikh,  Syr.  zarnikhd,  ‘orpiment’. Cp.  Avestic  zaranya,  Pers.  zar,  ‘gold’,  and  the first  element  in  zermahbub,  and  see  yellow  and words  there  referred  to.  Cp.  also  jargon,  ‘a variety  of  zircon’.  Gk.  apctevtxov,  appsvtx&v, ‘orpiment’,  was  influenced  in  form  by  apcrevtxop, appevixic,  ‘male’,  fr.  ape rc;v,  ap pr,v,  ‘male’.  For the  sense  development  of  MPers.  *zarnik,  cp.  L. auripigmentum,  fr.  aurum,  ‘gold’  (see  orpiment). Derivatives:  arsenic,  arsenic-al,  adjs. arsenious,  adj.,  containing  arsenic.  —  See  ar¬ senic  and  -oils.
```


## [2026-09-14T02:28:04.359Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'lemma: snā\\|lemma: sna' POK_full.txt | head; echo ---; grep -n -i 'snā-\\b' POK_02.txt | head -20"
}
```


### [2026-09-14T02:28:04.435Z] TOOL RESULT

```
78824:Root / lemma: sna-, sn9-(t-), snau- sn-eu- sn-et- 
79095:woo, marry, nymph, derived from a suffixed in -b^-format of Root/ lemma: sna- sna-(t-J, 
79282:woo, marry, nymph, derived from a suffixed Root/ lemma: sna- sna-(t-), snau-, sn-eu- sn- 
---
```


## [2026-09-14T02:28:08.513Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '78820,78870p' POK_full.txt"
}
```


### [2026-09-14T02:28:08.576Z] TOOL RESULT

```
References: WP. II 694, Kluge-Goetze 685. 
Page(s): 972-973 

Root / lemma: sna-, sn9-(t-), snau- sn-eu- sn-et- 

Meaning: to flow, swim; damp, nymph of waters 

Material: 1. Old Indie snati, snayate ^badei (sich)', participle snata-, Avestan snaye/te' 

washes, purifies, cleans through SpiJIen', participle snata-; o(/7)-present -snadayarr, Old 

Indie snapayat/ ^schwemmt', snapana- "zum Baden dienend (of water)'; in addition Latin 

Neptunus above S. 316; 

gr. vrixw, -opai "schwimme' (formation as apinxw, i|Jnxw under likewise; Indo Germanic 
ghor kh)\ yv\aoc„ Doric yaaoc, 'island' as "Schwimmer'; 

Latin no, nare {* sna-Jo) 'swim', Umbrian snata, snatuAkk. PI. n. "Gmecta'; Old Irish 
s/7a/77 "dasSchwimmen', cymr. nawf6s., bret. neunv/'swm'; Middle Irish s/75/io'"schwimmt, 
crawls, flows '; 

2. auf *sn9-t-base6 on Latin nato, -are "swim, flows '; Venetic FIN Nati-sd(n), *Natusis 
Modern High German Netze; cymr. naidi. "spring' {*snatia), bret. n{e)ijari\y\ corn, nyge 
"fly, swim', mcymr. dienad {* dhronata) "Tosen of Meeres', and Armenian nay'damp, fluid'; 

3. auf sn-et-, *sn-ot-base6 on probably gr. votoc; " southern wind ' ("Regenwind'), 
v6tio(;, voT£p6(; "damp', voTi(; f. " damp '; thrak. FIN N£aTO(;, S. 759? 

4. Beside sna-\\es snau- audi sneu-\ 

Old Indie snauti, participle s/7^/5-"triefen, a liquid of Korpers, particularly, specially, 
especially, particular: in particular, peculiarly, separately, extra, notably Mother's milk, 
entlassen' (present Indo Germanic *snau-tiox lengthened gradees *sneu-ti)\ gr. vaw, 
Imperf. vaTov, Aeolic vauw "flow' (*avaFju)); Zziio, yaF\oc, (Dodona) as stromend thought, 
whereof vc(ia(;, Ionian vr|ia(;, -aboc,, also yaio,, Ionian vr|i'(;, -iboc, "stream, brook-, 
Quellnymphe', Nripsuc;, Nr|pr|i5£<; (*ovaF-£po-, substantivized probably in vripov to 
Tansivov Hes., das as "Meerestiefe' to understand, comprehend sein wird; but vr|pi5a(; 
TogKoiAag nsTpag Hes. perhaps to ner- "penetrate'), reduced grade vapog (*va£p6g) 



'rinnend, flowing ', vaETwp pscov, TToAuppoo(; Hes., Attic Vok. varop m. "stream', vapa 
(*vaF£fja) " liquid, wellspring', vaa[}6q fvaFsaiJoq) " watercourse, wellspring, stream, 
brook'; Middle Irish snau, sno ' stream' {*snaua)\ 

5. from *sneu-i'co'(r\: v£U) (Fut. vsuaopai) "schwimme', lak. voa nnvn. s-vvuGsv ekexuvto 
Hes. Latin nutrio, -Tre 'suckle, nourish ', derivative from a *sneu-trTierc\. 'milk flow lassend'; 

as o^extension from sneu- one understands Middle Irish 5/7i7ao'(also FIN) 'river';
```


## [2026-09-14T02:28:10.955Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport io\nfor target,name in [(33644,'Samson'),(3518,'arsenal'),(34872,'Shamash')]:\n    ff=0\n    with open('KLN_1966.txt',encoding='utf-8',errors='replace') as f:\n        for i,line in enumerate(f,1):\n            ff+=line.count('\\f')\n            if i==target:\n                print(name,'line',target,'leaf',ff,'=> approx printed page',(ff-12)*2,'or',(ff-12)*2+1)\n                break\nEOF"
}
```


### [2026-09-14T02:28:12.159Z] TOOL RESULT

```
Samson line 33644 leaf 733 => approx printed page 1442 or 1443
arsenal line 3518 leaf 68 => approx printed page 112 or 113
Shamash line 34872 leaf 759 => approx printed page 1494 or 1495
```


## [2026-09-14T02:28:35.111Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=78824 && NR<=78900 && /Page\\(s\\)|References/' POK_full.txt; echo '--- POK_02 leaf for p971 = 971-344=627'; awk 'BEGIN{RS=\"\\f\"} NR==627' POK_02.txt | head -60"
}
```


### [2026-09-14T02:28:36.234Z] TOOL RESULT

```
References: WP. I 397, II 692 ff., WH. II 146 f., 172, 190 f., Loth RC. 46, 154 f. 
Page(s): 971-972 
Page(s): 974 
--- POK_02 leaf for p971 = 971-344=627
```


## [2026-09-14T02:28:40.737Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i '^sna\\|snā-\\|POLYNESIA\\|Polynesia' AHD_watkins1985.txt | head -20; echo '=== arsenal in AHD'; grep -n -i 'arsenal' AHD_watkins1985.txt | head"
}
```


### [2026-09-14T02:28:40.807Z] TOOL RESULT

```
965:sna-. To swim. Contracted from *snaa-. 1. Extended form *sndgh- in Greek nékhein, to swim: NEKTON. 2. Suffixed zero-grade form *(s)na-to- in Latin natdre, to swim: NATANT, NATATION, NATATORIAL, NATATORIUM; SUPER- NATANT. 3. Attributed by some to this root (but more likely obscure) is Greek nésos, island: CHERSONESE. See (s)nau-. [Pok. snd- 971.]
=== arsenal in AHD
```


## [2026-09-14T02:28:41.862Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls incoming/WLD/; grep -n 'snā-\\|snā(t)\\|sna-' incoming/WLD/WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-14T02:28:41.925Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
1104:starken Augenwimpern, dichthaarig‘‘ av. pasna- n. ,,Augenlid^‘, vgl. in nicht
3428:  Ai. pdrsni-h f., av. pasna- n. „Perse''; gr. jiregvr]^ spat. Ttxigva „Perse,
19050:lafit sich leicht ausstreichen, gleichsam zerschmelzen). Mit ai. mrd-^ mrtsna-
21688:                      sna- „flie6en'' als „Schwiniinerin''
21690:                                idg. e nicht gerecht, auch hat sna- keine
27107:ruksd- „glanzend“,                     ay.    raoxsna- „glanzend'‘                  (= ahd.      liehsen)          f.   „Licht'‘
27250:prinus alburnus und leuciscus'‘) mhd. lieJisen „hell“ {leuhsna-^ == av. raoocs-
29854:daher mit Schwund in Zs.:) av. dsna- „erfolgreich, wirksam, tiichtig'* (*<^-
30315:svacha „Brautwerberin“ {*siid-to-s oder eher *sna-tos; in ahnlicher Bed.
32244:Wb. 1060 f., Brugmann II^ 2, 799), av. dsna- Adj. „nahe“ i^^d-zd-na-, PPfP..
45962:sna- „flie6en, Feuchtigkeit'^
46259:„eilen“ (nicht zu sna- „fiie6en“, s. d.), aisl. sneggr „schnell“ (^snawwu)^ norw.
46285:(zu mhd. snu^ usw., s. u. sna- „flie6en“; erwogen von Persson Beitr. 328
46306:Erw. von sneu- neben sncm- und sna- (s. d.) „flieBen'" (Persson Wzerw. 179).
46598:„flie6en“     —   s,   u. sna- „fliefien“           Gdf. (s)midh-s-a),
```


## [2026-09-14T02:28:49.072Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '45940,46010p' incoming/WLD/WLD_Bd2_pages.txt; echo '=== page tag'; awk 'NR<=45962 && /\\[pdf page/' incoming/WLD/WLD_Bd2_pages.txt | tail -2"
}
```


### [2026-09-14T02:28:50.045Z] TOOL RESULT

```
„Anstrengung, Muhe“, fxoyJXetv j,sich anstrengen, abmuhen^', uoyj&rjQog „muh-
selig^‘; fioyXog {^po^Xog) „Hebebaum, Hebeh', poyX-sa>, -eva> „bewege
                                                                            fort               ,



lit. (^em.) smagiis „schwer zu tragen oder zu ziehen“,
                                                            lett. smags^ smagrs

„8chwer von Gewicht, iastend“. Solmsen KZ. 29, 85 f.
  Gegen die Herleitung von lat. moles, molestns, 7noUrt aus ^mog-sli-, *-sles-
(oder gar ^mogsdhes-^ dutch Vanicek^ 205, Schulze KZ. 28, 2/0
                                                                  Anm. und
Solmsen aaO., s. Vf. LE^V^b.^ s, v. und unter *mo-  „sich mxihen  .



  Gegen Verwandtschaft von ^moks                    „bald‘‘   (s. d.)   spricht   dessen Palatal
und die Bedeutung.

sna- „flie6en, Feuchtigkeit'^
                                                                         snayeite
  Ai. sndti, snayate ^,schwemmt, badet (sich)'‘, ptc. snatd-^ av.
„wascht, reinigt dutch Spulen«, Ptc. snata-, d(h)-Fvaes. snada^;
                                                                                 ai

mSpdyati „schwemmt‘S sndpana- „zum Baden dienend           (vom  Wasser)^^   (iiber

andere jp-Formen s. u.);
                                                                u. dgl.  s. Brug-
  gr. v^ycoj -ojuai 5,8chwimme‘" (Bildung wie opriyco^                                ;



mann Grdr.   11 ^ 1030, der  idg. kk^ Persson Wzerw.   27,  der  idg. gh ansetzt),

vijoog^    dor.   vdoog ^Insel*^ als jjSchwimmer*^             (s.   Brugmann BSGW^. 1899,
212 f., Grdr. 112 1^541; nach Solmsen Beitr. I 244 mit dem fruchtbaren
gr. Formans -ao- wie z. B. ytav-oog eig. „Brenner“),
   Lat. no, nare „schwimmen‘', umbr. snata, snatu acc. pi. n. „umacta“; air.
snCLm „das Schwimmen“, cymr. nawf ds., bret. neunvi 5,schwimmen“, mir.
snaim „ich sehwimme, krieche^.
   Auf *awa-^- beruht lat. nato,-are „schwimmen"‘ und arm. nay „na6, flussig'*,
auf                 wohl gr. vorog „Sudwind‘' („Regenwind“), voxiog, votegog
                                  ;      :




                                                 sna*                                   693

„iia6“     (s.   Brugmann IF. 20, 222 m. Lit.;          vdto^ nicht besser zu got. natjan
„iietzen% ahd. na^ „na6‘‘ unter idg.                              Fick III^ 291).
  DaB zur^-Erw. sn-ep- yon ai. sndp-ayati^ -ana- auch av. napta- ,,feucht^‘,
apers. Ndnag  xgi^vt] im rcbv OQoyv rrjg HeQoidog loTOQeXxai,
                     '       fj                                q)eQOVGa rd    fj


€L(poda [i. e. to vd(p^a] Hes., np. neft         Naphtha gehore (der Mangel des anl. s-
                                                           *




dann nach ar. nabQt)- „feucht“, s. nebh- ..feucht ist weniger wahrscheinlich, als
                                                           *)


da6 diese Worte anfanglich zu nehh- gehoren {Ndmag^ wenn zuverlassig, dann
=== page tag
```


## [2026-09-14T02:28:58.982Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== BRT snā'; grep -n 'snā\\|sna-\\|snāta\\|us-snā\\|usnā' BRT.txt | head -30"
}
```


### [2026-09-14T02:28:59.041Z] TOOL RESULT

```
=== BRT snā
3224:•  j.  a-daevayasna-  Adj.  'der  kein  Da^a- Verehrer  ist',  sva.  tnazdayasna-":  jahi  .  . yö  .xrudrä  fiam.ras^waydti  . .  da^'ayasna- nqm  -nanqmca  \. 18.62.
4148:vergänghchc.di.  materielle  Dasein,  Leben': kaaa  ns  iaa  .  .  agatJ  i^yejauhatat  haca °f»haot  ai'kyejanhsm  ahüm  a  V.  7p.  3 1 ; 7.52;  —  hai:a  apajäsö  .  .  i'iyejatuthata^ haca  'fihaot  atiryejanhutäitn  avi  °hü?n H.  2, 16.  2)  mit  a)  manahya-  Adj.  oder manauhs  GS.,  b)  datbitya-  Adj.,  c)  parS.- asna-  Adj.,  d)  ai>y0ah-  oder  ai'hyejakvant-
5893:•  g.  (asna-),  j.  (asna-)  Adj.  'nahe',  nur I.Ä.  und  AbS.  als  Adv.  i)  LS.  'nahe,  in der  Nähe':  asnai^a  ..düraicaW.i-j.%;  — snaihii  asnt  rnymatim  H.2.2;  20;  —  mit Abi.:  asne  vayöanai  "in  der  Nähe  des KopfsT-SJ.  a)  Abs.  'von  nahe':  asniil ..  dural  (sd.)  Y.  4j- 1 ;  —  asnuatca  jasintsm därJatca  Vyt55;  H.2.13.
5897:•  g.  asnät,  j.  asnäat-t'ä  Adv.:  s.  asna-.
5899:•  j.  asne  Adv.:  s.  asna-.
5903:Ableit.  aus  azan-,  %  33.  1.  —  Pü.  (lu  A): Iransskr.,  Sü. ;  ahahpuaya;urai-a\\  (lu  V. /J: hal  naz,rJi  (Verwechslung  mit  asna-).
7476:•  j.  äsu.yasna-  Adj.  'der  den  Y.  rasch vollziehen  kann' :  haomS  .  .  ytm  zaotänm slayata  ahurB  mazdh  °n?m  bsrizi^ä^r^m; yazata  zaota  "rtö  Yt  lo.  89.
7496:lisna-
7499:•  j.  'ä-sna-  Adj.  'angeboren,  natürlich', von  xratav-  m.  'Weisheit'  (im  Gegensatz zu  gmiSsräta-,  sd.):  «J»V  mailm..  s/g(s±) masyä  kacaiie  °nS  xrahts  yaüa  mi'inmni .  .  ha<aiu  'nasHt  xratus  "es  gibt  keinen Menschen,  dem  grössere  natürliche  Weis- heit zu  eigen  ist,  als  , ."  Yt.ro.107;  — "rum  xraiBm  tnasdaoättm  .  .  gaosS-srütim xratüm  tnazda'Mit^m  Y.  25.6;  —  'nahe xraiwö\.  22.2%;  —  Uta  kg  "fum  xratäm avaiaraiti  vSrjma  (sd.)  Yt/j.a,
7501:•  j.  'ä-sna-  Adj.  (fem.  °»<i-)  'erfolgreich, wirksam,  tüchtig':  'naca  (APn.)  viana asäunam  'nafa  manä  sae^antqm  Vr.  J/.3; —  °K.7  (APn.)  . .  mata  Yt  13. 74.  a)  bes. von  frasanfay-  f.'*:  ifä%ravaiH  'na  fra- ttitntifY.tio.-j; — nairyam  '»am  *frazain- am  Y.öS.s;  62.S,  GS.'i-i,  Yt./o.3,  108, 110,    ;Ä5;    —    'naySs^a  paili    vanhuya
7505:Tu.:  ämJlat,  ämütat'^;  Sü.(iaY.öb):  iiiiUai, (10  Y.  62):  Hisar);agunah,  —  >)  Hier  könnte auch  'äina-  vorliegen,  vgl.  5ü.  und  Gdn.  KZ. 24.  131,  der  nur  iia  äsna-  anerkennt.  9,.  aber Vr.  //.  3,  Yl.  /j.  40.  —  *)  Anscheinend  PPfP. eines  V.  'Juiütan,  zu  einem  ar.  Fraes. *,i:iM)iiäii/i ,  während  Sinilai  ein  *Simlan »orausseul,VEl.  anäan  (PüErl.  lu  V.J.  56)  neben ai.  ciiiMi.
9314:'"f  ^V  ~  ""'■"'"'^ -iT' ^^'  l,^^"  .         or    '•  J-   karsna-   m.   EN.   eines  Gläubigen: Ableit.  —  ai.  vgl.  kalpa-  m.  'Ritus'.   —    Pfi. :  i         ■      +  ,  ^        i     /  j  i        ■•       ,    « j
9315:karp,  mit  der  E?].  {für  kayak  u  karp):  pa  Ä/'  '«<'^    Ubaurvatanahe  (sd.)    awon^      des i  yazaläH  karr  u  kör,  woiu  die  np.  Erl. ;  kar  u   K.,  Sohns  des   Zb.  .  ."  Yt.  IJ.  1 06. kür  an  bUaitJ  ka  jimäit  i  hurmazd  didart  u  '      Abieil.   —   Et.?    Aus  ar.  ^karlsna-.     Vgl.  ai. suxun  hmidan  na  laväiiand'),    Sü.   (in  umge- 1      kftsnd-  Adj.  'ganz'?
9897:•  j.  gaoäÖ.srüta-  Adj.  'vom  Ohr  gehört', von  xralav-  m.  'Weisheit'  sva.  'erlernt' (im  Gegensatz  zu  'asna-,  sd.)":  äsnim xratüm  mazdaaätpm . ,  °t>m  xratütn  masda-
10173:•  j.gavasna-  m.  -?— :  asti  (Sp,  273  o.) yS  'nahe  mäuya  jya  Yt  10. 128  Gl.
10610:4.45;  4S;  —  aslm  .  .  ya  vTspanqm  . syantqm  /rasa  °'hwa  frdhanjayeiti  Yt i-j.t*''i;  —  mit  ^äsna-  (sd.)  und  gaosS.- srBta-  (sd.):  ätmm  'tum  .  .  gaosS.srai>m 'tum  Y.  25.6;  —  äsnahe  ''hwä  .  .  gaosi\- srotahe  ''%wS  Y.  22.25;  —  "'"^  ^^  äsnim 'tum    ava.baräiti    varsma   (sd.)   Yt/7-2;
10920:•  i-i  K'i  P*  xSnä-,  'sna-  V,  "kennen'. Praes.  14  (Inkoh.)  xsaäsa-,  16  (Des.) sixsnanha-,  —  Inf.  'xsnJy  °xsn>m;  PPfP.
11390:KompE.  —  ÄSn.  ma  'iay-.  —  ai.  •cU^9<,  mp. •Ä;enkLPart.— Pü.:  ir'o),  'a  und  weggelassen; Sü.:  cit,  api,  ffl  und  fehlend.  —  O  Hinterm Verbuoi  (fin.l  ist  es  nicht  nachweislich,  auch nicht  im  RV.;  s.  Bthl.  Bß,  13.  73-  — ')  iVerb.  von  onyj-,  jb/vo- mit  c-'"  s.Sp.  13SU., 137  m,  —  3)  iVerb.  von  ul^  mit  ^  s.  Sp. 385  m.,  u.  —  4)  Man  verlangte  mazäayasna- eil  vimaiö.  —  5)  Geringwertige  Stelle;  die Fügung  asnqmcil  ftazaiiitim  kommt  auch  sonst vor;  s.  Bp.  Sga'o.  und  No.  12.—  *)  Nur  ein Enldiliknm  kann  dazwischen  stehen,  vgl.  Y. p.  2.  S.  daiu  ca  No.  2.  —  7)  S.  No.  6,  — 8>  Hier  das  eiste  Mal  ßlschlich  /a.  S.  noch No.  18.  —  9)  Das  iweite  <*  sollte  bei  paraos stehen. —  »)  Hypothetisch.  Wenn  nötig!  — ")  Stall  masyasHl  vä  ahm'tt.  —  ")  Das  mehr- fache  AuftrMen  dieies  H(  |im  jAw.)  beim selben  Wort  oder  dessen  Aufireien  bei  einem Wort,  hinter  dem  es  auch  in  andrer  Bedeutung vorkommt,  ist  für  die  Entstehungsgeschichte der  jAw.  Stücke  (in  ihrer  jeliigen  Gestalt)  be- merkenswert.  Vgl.  fil  bei  äsna-:  Y.  68.  11, Yt.  10.  107.  108,  HO,  IS.  S  (No.  Sh  bei Jariya-:  Y,  62.  3,  Yt.  /J.  54,  Tg.  a6;  bei niOma-,  Y.  fo.  6j,  V.  9.  38,  F.  #  a,  Vyt.  2j; bei  %r7s:  Ny. /.  I.  P.Jp,  Vyl.^/;  bei  a7sqm: y.  3^.  8,  13.  3,  V.  rs.  49;  bei  a!.iyö:  Yt.5. 59,  72,  rs.  41.  M  (s.  No.  14).  —  >i)  Dem XPifa^ya-^^  *naomayaHt  V,  8,  17  f.  entspricht V.  8.  16  ä%rilim,  ohiie  eil.  —  '«  An  den zahlreichen  ParalleUt eilen,  da  es  sich  um ^ine  Person  handelt,  steht  stets  da%a!  ahmäi, ohne  cit.  —  'S)  Hds.  •/al;  s.  aber  K.  — >6)  Unrichtig  Sp.  473;  s.  Ntr.  —  '7)  Vgl.  Y. 4S.  et,  wo  dafür  . .  rahyä  . .  yihyä  ma  ai%is dva'Xä  steht  —  'S)  Wohl  verstümmeltes Zitat;  s.  N.  log  und  P.  t2.  —  '«  S.  daiu Dbr.  AiS.  478,  569  und  PW.  udW.  — '""i  Wofür  auch  mmn  (^=<¥1)  erscheint;  iB. Y.i2.  14. •  j.,  g.  dinS  enkl.  Part,  in  Verbindung mit  nif/V  (nasca)  oder  mäha  'auch  nicht*; i)  sva,  'gleicherweise  nicht,  ebensowenig', die  Negation  geht  voraus:  ayä  nsit  3r>^ vTsyat'l  daH'äcinä  hyat  Ts  a.d>baomä  (sd.) . . upa.jasat  Y.jo.  6 ;  —  mä  manar>ha . .  *mä'ja ka'hacina  *paiti.ßme  Vr.  22.  2.  3)  sva.
12467:daevayasna-
12483:•  j.  daeva-yasna-  Adj.  'der  die  Dalva verehrt,  anbetet';  überhaupt  'ungläubig"*: ye^he  .  .  näirika  avayi  xfudrä  Aqm.- rafktoayeiti  mazdayasnanqm  'nanqmca N.  77'';  ~  kalärö  paurvB  ämayante  (sd.) maidayasna/ibyB  va  'nalibyB  vä  V.  7.  36; 37;  —  drvafäB  'naahdYt.  5.  94;  —  huma- yak»m  'n>m  drvanttmca  ..Y\..^.\\y,  109, 5.37;  —  drvatam  'nanqm  Y.ig.  26,41, Yt5.68,  ;;.  4,6;'  —  dusmainys .'. 'n^iAP.) A.  7,  11;  —  daffnqm  'nanam  Y,  72. 1 1 ;  —
14920:•  j.  paiti.arsna-'}  Adj.  'entgegentretend, sich  zur  Wehr  setzend':  varäsahe  'nS'* tiH.dqstrahe  Yt  i4- 1 5-
15098:paitis.x^arsna-  838
15139:•  j.  paityärsna-  Adj.  'contrarius,  Gegner', mit  Akk.  verb. :  °nS  imqm  datnqm  yqm ahairim  YtÄ59.
15495:•  ].  paro-asna-  Adj.  "künftig  seiend,  kunf-  {  ^_  ,g|.  ^„^^v««-  Adj. tig":   'näi  aiiuhe pas^a  astttsca  haoaatffiaica  ■   *      t^L-.v
15762:•  j.  *paurv5.vasna-'>  Adj.  'wobei  der Wille  vorausgeht  sva.  beabsichtigt,  vor- sätzhch':  yS  näirikayi  cthravaitya  .  .  °na ^adhna  tanUm  irihyäl  V.  l6.  14;  ludrig at  Vyt  26,  40.
16115:nach   vom    sich   wendend,   sich   weithin  •  j.,  g.  'parsna- Adj. 'gefiillt,  voll':  afriti
17905:Zum  V.  sank: ■  j.  alt3m  väbm  nX  antan  maxäayasna- nam  frasastaylt  Vd.  13.    Wertlos,
18848:KompE.  —  Snpetl.  ta  ^niadyah-  •propior'  und zu  üsna-  'propinquus'.  —  ai.  nidkfha-  Adj., iDp.  nazdht.  —  zEt.  (ar.  *ncaäiil/ia-  tu  einem Praes.  3  *nä-tda-li,  lum  V.  »Airf-)  »gl.  ZDMG. 50.  686,  Bgu.  Grdr.»  /.  735.  —  Pfl.:  nazdist, (zu  Y.  33):  natäli.  —  ')  Hdi.  maidilla;  Pü.: fehlt.  —  ')  Abgesehen  von  den  luvor  aus- drucklich genannten.  PiiErl. :  afil  i  iapastän 'ram  Ort  der  Nacht  weg',  daher  DST.  ZA. 3.  142  >Ie  feu  du  campement';  s.  auch  Sp. Komm.  I.  367.
19160:Ableit.  ans  *ni-fiasna-  m.  'invidia'.
20179:■mazdayasna-
```


## [2026-09-14T02:29:00.397Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== HRN'; grep -n -i 'sina\\b\\|šinā\\|sinā\\|ušnān\\|ušnan\\|usnan\\|šenā' HRN.txt | head -30"
}
```


### [2026-09-14T02:29:00.502Z] TOOL RESULT

```
=== HRN
739:Vergl. sina (No. 792).
1206:arm. LW. ausnan 'Seifenkraut*,
8741:niyOmay (265) ; wa/. inalung, siyn. meSina, sar. madän
10330:aw. dasina- rechts*; ai. daksina-.
14838:dasina' 63.
```


## [2026-09-14T02:29:05.801Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '--- HRN 1195-1215'; sed -n '1190,1215p' HRN.txt; echo '--- HRN 730-750'; sed -n '728,752p' HRN.txt"
}
```


### [2026-09-14T02:29:05.860Z] TOOL RESULT

```
--- HRN 1195-1215
phlv. astar; ai. agvatard- 'Maulesel'.
kurd. istir, histir; bei. istal, n. hastal (438).
87. iiStur *Kameer, sutur.
aw. ustra- 'Kameel'; phlv. ustrlastän (vd. 15, 68);
ai. üstra-,
kurd. LW. (?) hustur^ sutur; bei. hustar etc. (161);
wa/. ü^tür^ siyn. stur, sar. xtiir, LW.(?).
88. eSk *Thräne .
g. sah,
aw. *asraka (vergl. skr. dgra-), *arsaka (Hörn, Indog.
Forsch., II, 136).
afy. ö^a resp. ö/a; wsl/, ya^k, sar. yujck,
Vergl. ers (No. 69).
89. iiSnän Name einer zum Waschen gebrauchten Pflanze,
Herba Alkali (AM. 28; 37 Zeile 2), sunan (DWlfi'IN,
Jer. 2, 22).
arm. LW. ausnan 'Seifenkraut*,
aw. "^aiwis'hnana- (\)^) (de Lagarde, Fers. Stud., 74).
Zu aiwis vergl. indessen unter bes-, bis- (No. 221).
90. eSnOse, isnöse 'das Niesen', senöse, sinöse, sinöse-).
germ. Vhnus bezw. /wws, vergl. ahd. niosan^ mhd.
') Die Awestaform ist von de Lagarde falsch angesetzt, der
die Lautverhältnisse verkennt.
V V
*) FR und FJ haben die folgenden Belege (nur FJ constatirt
einen Majhülvokal): (Metr. Hezej)
--- HRN 730-750
'in Bewegung geraten'.
33. äskär 'klar , äskärä, äskäre,
phlv. äskärak, äskäräk, arm. LW. askaray; aw.
*äviskära- {ävis 'offenbar, klar, y. 33, 7); vergl. skr.
äviskfta- (ai. ävis) und skr. äviskära- (spät) selbst.
af>^. xkära 'deutlich'.
34(i). äsna 'bekannt', äsnäyt,
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
```


## [2026-09-14T02:29:08.094Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'snay\\|snā-\\|sna-  V\\|us.snā\\|us-snä\\|usnä\\|snä-' BRT.txt | head -20; echo '=== HUB'; grep -n -i 'ušnān\\|ausnan\\|Seifenkraut\\|šenā\\|sinā\\|snä' HUB.txt | head -20"
}
```


### [2026-09-14T02:29:08.174Z] TOOL RESULT

```
2559:;j.  I ;  —  cayö  'tt  raocii  atjhin  . .  yö  avaha  '  v(rf'ianahe  .  .  yat  '6a  han)asSnte  paouru Sraoeayeite\.2.y);  —  'tae^va  äaxmagh'a,gaonaAe^a  (sd.)  ..  N.f*j;  "/(?);  —  saetari frV  paiii  3ya  ztma  bavainii  V.7.54;  ■ — \gätava  .  .  *'oa'>  ,  ,  N.  A;  —  yetiie  '6a "le  malsma  .  .  yaiibyö  .  .  /rasnayiinte  V. ;  mazdayasnanam  näirika  . .  *hqm.raEä:wa- J'.ii;  —  'taiiam  syao^naiiqm  yöi  V3r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, ziiiti  masyjka  V. /j.  2;  —  "täibyö  zao-  11;  —  avaoa  °oa  'V.4-50;  —  taica  °üaca 'irJbyß  ..yäakqm..  N.  7/;  —  iu>a 'tat  pu>nm    baraiti    V.  15. 49(?).  a)    mit
3374:'sd.)  sacinte  "ija  aiwi.game  V.  5. b)  'drum,  so  —  denn',  vor  Imp., Inj.,  Konj.,  Opt  und  Inf.:  tsmca..  laibyo dat  sarim  °%a  Asm  foraSua  %wa  xra^toä ^-  53-3'  —  "^'i  ^^'  västs  (sd.)  xsmat anyö  'äa  möi  sqs/a  (sd.)  veAs  vastrya  Y. 2ij.i;  3l.iS,34-7i —  °^«  «f  ii  humayd.- tara  anAm  Vr,  72.4;  4;  ~  "'ia  tu  n9 gayasca..Rya  y,4'-S'> — "^^  »■'  sasdyai (sd.)  usia  V.57. 16.  4)  anschliessend 'und';  a)  ein  Nomen:  i^a  i  Aaiiyaisd.) nare  "'^ä  jsnayö  Y.  5_J,6  3\  b)   einen
4222:yänäis  zaranaemä  (sd. )  Y.2Ä  8  £  b)  sub- stantivisch: jajA  mg . . /rabarät . .  *st»ri- naoiti  'na  *  avavat  starsm  (sd.)  . .  ya"iia  . . P.22f.  2)  vorausweisead;  i)  adjek- tivisch, a)  auf  direkte  Rede :  apasca  vajmhls yatnda'^äne  hala  °na  ga^ivya  vaca:  garS nmane  (usw.,  Y.jj.rs)  Ny.4.8;  Y.ö'5.14, Y.  10. 19.  b)  auf  ein  Relativ  als  dessen Korrelat:  °na  ^wa  yasnayazane  -na  ^wä yasna  frayazäne  yasi  ircd  yazaia  vlstäspö Yt/7,61;  —  Aauca  ^'nayiVi  nara  vohu manS  jag?r?buitarS  {anhat)  yö  .  .  ya"^a hau  yS  .  .  V.  4-48-  2)  substantivisch, a)  auf  ein  mit  ya'^anä  angeschlossenes ' Nomen,  sva.  'er,  wer  es  auch  sei,  jed- . weder':  vi.,  'tiä  sanm  mruyg  ya'kana dngvatä  rqxsyantä  "ich  entsage  der  Ge- meinschaft mit  jedwedem  feindseligen  ^r." Y.  J2.4*>.  b)  auf  einen  Satz:  tum  "na miirs^rujqm  .  .  "ä^wyqm  avaiarahi:  apa alsqm  .  .  at^d  .  .  barahi  Yl  10. 23.
4346:Pü.:  snayäwärlh.
4504:•  j.  anu-matayae-:vr,  "t^e  Inf,  '(und)  im Denken  zu  folgen,  zu  denken  gemäss  -' (Dat",  Gen.):  ya^a  azsm  /nJcayeiie  {sA) .  .  zara%ustr»m  "ISe  dagnayjt  aiiuxtJe  .  . anu.varHSe  Yt.5.18;  —  haxsaya  (sd.)  .  . frat^ma  .  .  aiähl  dasnayj  'iayaeca  , .  Y.
5038:I  xsaparäl  us  lanam   snayaeta  us  . .  pattt Yt 73.25.        [s!  noch  avi&ia  No.  5],       \°%a  yaozdayqn  (sd.)  "nach  drei  Nachten Ableit.  -  Pü.  (lu  V.  4)i  an,  (lu  H.  3,  N.  15):  \  soll  man  den  Leib  waschen  . .;  auf  diese
7120:V. /.V,  26;  —  baivan  va^anqm ,  .  urvSsnayii  vii  voku^aonahe  vä  .  .  ' . .  nisirinuyat  V,  14. 3;  2 ;  —  ant .  .  ' sac^ra  frabaröil  xrUzdranam  assmai '>re  frabarBis  voku^aot
7508:•  j.  ä-snatar-,  ä-snäftr-  m.  Bezeich- nung des  fUnften  mit  der  Waschung  und Filterung  des  Haoma  betrauten  Untere priesters  (ratai-):  üaf  *°tar/'^  (näml. iairini  a»hai)  yat  Aaomjmca  äsnayät  hao- msmca  pairi\kar>%3l  ".  ,  des  Äsn.  (Amt ist),  dass  er  den  H.  wäscht  (spült)  und filtert"  N.  75;  —  Aaoyai  *&l  naginJJ  'tarl (oäml.  däityö  gsiul)  "auf  seiner  (des Havanan)  linken  Seite '>  ist  des -^.  (ge- höriger Platz)"  N.  /p;  —  paoiryU  . .  hüva- nätam  (sd.)  . .  astayäti  . .  fiuxl^m  'tar»m N.ftj  F.7;  —  advaoa  °'irqf  Aävanäne *rai>wayati  N.  i?o(?j;   —   'tlnm  astilya
7511:Zum  V.  j»J.;  eig.  'Wischer'.  Das  a  vor  dem Suffix  slammt  aus  dem  Praes.  snaya-.  Der auHallige  Wechsel  1  wischen  •i'ia/Sr-  und 'snä%r'  hat  in  a%ai4tua-  und  a%rai'a«-  eine gewisse  Parallele.  —  ai.  •snäiar-  m.  —  Pü. : äsnaiär  (Transskr.).  —  ')  Hds.  'Kira.  —  »)  Vom Zaalar  aus  gesehen.
7538:•  j.  'äzäta-  m.  FJ<I.  eines  Gläubigen:  'Iahe karsnayanahe  asaonB  Yt/J,  108.  I
7542:•  j.,  g.  ä-zutay-  f.''  'Fett,  Schmalz':  raoy- nyqtn  i'aranhim  "suitlmca  urvaranqm  Yt. /2.3.  a)  überhaupt  sva.  'feste  Ndirung' gegenüber  der  flüssigen,  im  Gegensatz  zu ' xsi'td-  'Milch' :  pars  xsvisät  (sd.)  -zaitUca  "  1 girii mal  V.  13. z8;  — xhioaica  'sBlayaEca  ■> ^.68.2;  —  t!m  'iSdiis'''  ahurB  mq%r)m tasal  .  .  mazdä  gavei  xhildimcil  *ki'B.- umiaHbys  spmt3  säsnayä  "das  Wort  vom Fett  hat  AhM. ..  für  das  Rind  geschaffen und  die  Milch  für  die  Nahrung  begehren- den durch  sein  Gebot,  der  heilige"  Y. 29.71'.  a)  Du.  in  Verbindung  mit  xhild- Du.:  xsviöa  'zütH  yazamaide  .  .  ilzSis  .  . hamsistri  \.i6.8.  2)  'Üppigkeit,  strotzende Kraft  und  Fülle':  vaKuAlm  'zBülm*^  . . frasasttm  .  .   *p3r»ndlm  yazamaidl  Y.jS.
7741:•  j.  9r«zvo  Adv."  'wahrlich,  fürwahr'; 1)  an  der  Spitze  des  Satzteils,  vor  Vok.: fr°  asäum  spitama  ^7vam  da^at  ahurB maidä  Yt.  5.  89;  91,  95,  12.3,  13.  i,  Ij. 31.  2)  hinter  dem  Wort,  das  hervor- gehoben werden  soll;  a)  hinter  dem  Pron. pers.:  yat  tum  hs  uzsayatjha  tum  3r° zarahultra  Y.g.13;  —  aez'alia  bä  zara- 'i^ustra  ya>a  tum  jf  vasanhe  V.5. 17; z\;  —  paiti  »lam  if  ptnsat^uha  yim ahursm  mazäam  V. /^.  7,  b)  sonst: mazilt»n  ..vispanqm  tr"  sravaahamYi^N. 4.1;  —  daliiqm  »r'  yaozdaii-Xta  a^a  zX. . asti  yaozdäili^  .  .  havaya  ir'  dasnaya  V. la.  1 9.
7887:•  j.  'i'8a  Adv.  'jetzt,  nun':  abdaca  (sd.)  Ivd  darrja  akarsta  saaa  ..  '6a  i'amiti  .. ila  sadayäj  ya^  "Sa  ..  pdo?m  vamaite'^.yä  darrja  apu'^ ra  *a?i(i  V.J.24.  3)  Es 2.24;  —  fitfii  mi  'oa  *affAäJJ^m  ''^f» .  dient  dazu,  ein  oder  mehr  vorangehende vtra  Yl/J.13;  Ä54;  —  äaj  vai^uAi  'oa  Wörter  als  Zitat  zu  kennzeichnen*';  das .  ,  artdvl  sare  .  .  az'at  äyaptun  yüsämiVlJSsx  ist  dann  Subjekt  des  Satzes:  yetiAe Yt.  5.130;  131;  —  'ta  irUlanqm  urvanS  ^'oa  mazdä  yasritm  a»as/i  "ye/>Ae  \chit  die yazamaide  Y.26".7;  2,  4,  7,  Vr. /(».  i,  2',  j  Anbetung  des  .(y."Y.  2  j.i; — ya»kqm  'oa Yt.Jj.9S,  148'; — frä  U  zq'ismca . .  azsm 'alaoninqm  ärmaiH.paoiryanqm  yasmm •oa /rasnayeiiiy.21.6;'],  VytiJ; —  kaAepara.ciiiasti{zi.)\.2i.2; — ya%a  frä  'oa n5  'oa  nqma  äyatryaf  (sd.)  Yt  ZJ,  50; —   ämraot  yal  ..    'lyaSJa  sagt  aus,  dass  . ."
8478:—  mä  .  .  kaine  .  .  tarS  daxslim  pärayat (sd.)  tarö  ap?mca  (sd.)  'ramea  V./5.9; 10;  —  avi  tu  dim  disyata  (sd)  yä  apasca 'r-hca  zao>nhca  Y. A3,  a)  Du.  in Verbindung  mit  sp-  Du.;  yat  iurmaot a»haosimne  äpa  (Sh-erz.)  °vaire  Y.  9.  4; usw.  2)  mit  einer  einschränkenden Bestimmung :  aisma  .  .  yat  vä  aitaaham  . . 'ranam  yat  ätn.ciiranam  V.  ^75;  — altayh  °raya  aian^ar?}  V . S.-j ^-y  —  upa .  .  nmärum  baoiayaH  un-äsnayä  fä  .  . kamcit  v<l  hubaoi'At^manqm  °ranam  \.S. 2 ;  —  aoa  az»m  yS  ahurö  masda  °rä  bal- iasy'i  uzbamn  ".  .  die  Heilkräuter  . ."  V. JO.4;  —  ynän^m  vä  .  .  kamcit  vä  vlta- afianam(sd.)°ranainY.ij.i4; — yavanqmca vtlstranqm^a  'ranqm'a  :far?i5.bairyartqm (sd.)V.J.4;  —  'raaqm  s^awrlranqi'i  (sä.) Yt/>5S;  Vr.2/.i;  —  'rShu  paiti  barss- manyäku  Y.  2.11,  "Y't /0.14s;  —  imqmcä 'rqm  bansmanim  Y.  22.3,  a)  durch Namensnennung:  aetayh  *rayh  ya  i-aoÜ ha'jana^aia  V.  14.  4;  V.J.  3,  22.  i,  62.  9
8562:•  j.  usnäka-  m.  EN.  eines  Gläubigen; 'kake  asaonS  Yt  y.  117.
8564:•  j.  usnätay-    £    'Abwaschung':    %risa-
9316:Itehrter  Reihenfolge):  adari^ä  airotäraJca.^^  ,  ^^  karsnayana-  patr.   Adj.  'von  Karsna
9788:•  j.gao-dana,  °jiana-  n.  1)  'Milchgeföss': frä  tl  Aasaanm  xam  aam  . .  frasnaymi ''.an?m  avi  hatUaiinh  ya^  asti  puirake >rims"^e  tausend  Quellen,  die  zum  Milch- gefiss  zusammenfliessen,  das  die  Nahrung des  Kindes  ist"  V.  21. 7  ".  s)  überh. 'Gcfäss,  Napf,  Schüssel'  (nur  Komp.,  s. N.  64).
9840:ayasöis  yaont  fiairi  uxsän.>fn  bix^'^rgm (sd.)  .  .  V.  7p,  21;  —  »sj«  pas^aSa  upa- t3har?Z3m{^A^  V.p.  14;  —  catura  frasnana frasnaySit  °z3m  gava  daiäya  bis  äp>m tnazdmätaya  "vier  Waschungen  nehme  er ' vor  mit  Rindsurin,  der  vom  Rind  produ- zirt,  zwei  mit  Wasser,  das  von  Matdah geschaffen  ist"  V.  75.  22"'.
10920:•  i-i  K'i  P*  xSnä-,  'sna-  V,  "kennen'. Praes.  14  (Inkoh.)  xsaäsa-,  16  (Des.) sixsnanha-,  —  Inf.  'xsnJy  °xsn>m;  PPfP.
=== HUB
426:^abisnana^ ware zu np. *afsnan = arm. *ausnan^ osnan^)
9075:leicht ist es hier zu sn geworden, vgl. u§nan *Seifenkraut'
```


## [2026-09-14T02:29:24.560Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n '^792\\.\\|^ *792\\.' HRN.txt | head; echo '---'; grep -n 'sina ' HRN.txt | head"
}
```


### [2026-09-14T02:29:24.625Z] TOOL RESULT

```
6929:792. sinä, sinäh 'Schwimmen', sinär, sinärlden.
---
739:Vergl. sina (No. 792).
```


## [2026-09-14T02:29:26.396Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nfor fn,targets in [('HRN.txt',[739,1206]),('HUB.txt',[426,9075])]:\n    ff=0\n    with open(fn,encoding='utf-8',errors='replace') as f:\n        for i,line in enumerate(f,1):\n            ff+=line.count('\\f')\n            if i in targets:\n                off = 21 if fn.startswith('HRN') else 10\n                print(fn,'line',i,'leaf',ff,'printed p.',ff-off)\nEOF"
}
```


### [2026-09-14T02:29:27.537Z] TOOL RESULT

```
HRN.txt line 739 leaf 30 printed p. 9
HRN.txt line 1206 leaf 42 printed p. 21
HUB.txt line 426 leaf 25 printed p. 15
HUB.txt line 9075 leaf 263 printed p. 253
```


## [2026-09-14T02:29:31.558Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nff=0\nwith open('HRN.txt',encoding='utf-8',errors='replace') as f:\n    for i,line in enumerate(f,1):\n        ff+=line.count('\\f')\n        if i==6929:\n            print('HRN line 6929 leaf',ff,'printed p.',ff-21); break\nEOF\necho '--- HRN 792'; sed -n '6925,6945p' HRN.txt"
}
```


## [2026-09-14T02:29:32.524Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '405,445p' HUB.txt; echo '=== HUB 9065-9085'; sed -n '9065,9085p' HUB.txt"
}
```


### [2026-09-14T02:29:32.822Z] TOOL RESULT

```
HRN line 6929 leaf 197 printed p. 176
--- HRN 792
andere Bedeutung hat; np. nehmür 'zahllos hat die
ursprüngliche Form der Wurzel, smor-, am Besten
erhalten. Wegen phlv. ösmartan darf bei sumurdmi
nicht Entstehung im Satzsandhi angenommen werden.
792. sinä, sinäh 'Schwimmen', sinär, sinärlden.
aw. l^snClr, US snayaeta 'sich waschen'; ai. l^snä-,
sndii- 'sich baden.
oss. t. nähi 'baden', d. a^snun^ t. a^snin 'waschen*
(196).
Die Nebenformen sinäb^ sinäv, sinävtden erklären
sich entweder wie deryäw (No. 561) oder sie gehen
auf [/^S7iav' {gi\ vsio 'schwimmen', äol. raa», vavftt
'fliessen') zurück.
np. s ist im Satzsandhi oder durch Übertragung
entstanden.
793. Hnäyiten 'erkennen', Praes. sinäs-efn, shuls.
ap. /snäsatiy 'solle kennen'; phlv. snäxtav, sfinaPf,
snäsüntän.
kurd. 7fäfiin 'erkennen*, ez dinäsim.
Gehört zur arischen [/'San- (wie ap. adma, np.
*) Nirgends findet sich in den Dialekten das np. //.^_ 177 -
```


### [2026-09-14T02:29:32.884Z] TOOL RESULT

```
wahrt hat.
*) Vgl. auoh phi. stik ip sftk-pistan *with prominent breasts'
(Gl. and Ind. 160).— 15 -
ich glaube, dass st^n^ stenik zu lesen ist (die Pehlevi-
schrift unterscheidet e und i nicht), aber die Bildung
des Wortes bleibt mir trotz skr. sthEmdn- unklar.
88. Da zd. asru' = skr. rf^rw- im Np. als ars (aus "^asr)
vorliegt, ist es nicht wahrscheinlich, dass ein zd. *flf.9-
raka- (nicht *osraA;a-!), dem lautgesetzlich np. "^asra
entspr^che, durch np. ash vertreten wird. Nur konnte
Horn sagen, dass as-k neben ars steht wie x^as neben
xusru *Schwiegerniutter' (auch xasu^ xusu etc.) = skr.
gvagrii', iran. ^x^asru-. Vgl. afgh. dm *Thrane' = iran.
asru' neben afgh. x^'d^a *Schwiegermutter' = iran.
*x^asru-, Geiger, Etym. und Lautl. des Afghanischen
p. 51.
89. Arm. d$nan (nur Elise 156, 11) kann fur osnan ge-
schrieben sein ^) und so dem np. uifndn genau ent-
sprechen, mit dem es auf ap. ^usnctna- = zd. *usnana'
(vgl. zd. uS'Snd Vaschen* und wegen sn fiir sn : ap.
vasna = zd. vasna u. ahnl.) zuriickgehen k5nnte. Ap.
^abisnana^ ware zu np. *afsnan = arm. *ausnan^ osnan^)
geworden.
90. Die germanischen W5rter fiir 'Niesen' fiihrt Kluge auf
die Wurzein vorgermanisch qnus^) und ksmis zuriick."*)
Bildet man aus letzterem ein vorgerm. Substantiv
*ksnoMso- und ubertrS-gt dies ins Iranische, so erhalt
man iran. "^x^nauSa- = phi. *snOsak = np. iSnoSa.
Leider ist die Wurzel ksnus sehr hypothetisch.
92. Np. iiftddan ^fallen* aus oftatan (Gl. and Iiid. 45) von
Wrzl. pat scheint zunachst eine Bildung wie gr. nrwaig^)
von Wrzl. pet {Trl-nT-to), erweist sich aber durch phi. opastan
*) Vgl. aitsakf dSak fur osak — np. wla, arab. pers. tiSSoq 'gummi
ammoniacum'.
*) Vgl. np. afsarn = arm. auSarak, dSdrak,
') qmts — germ, hmts und fnus, vgl. N o r e e n , Abriss der
urgerm. Lautlehre p. 148.
*) Fiir ksnus setzt N o r e e n , Arkiv for Nordisk Filologie 1886,
III. p. 19 : skntts an (nach K 1 u g e ^ s Mittheilung). Beide Wurzein
sind durch Addition der yerschiedenen Formen entstanden.
*) Vgl. TTTijnoficei^ ^nrrjv Yon pta au8 ptoi (Bartholomae,
=== HUB 9065-9085
«
f) Idg. sn bleibt anl. im Zd. als sn (vgl. sniz 'schneien
= idg. snig^h), wird aber zu n im Ossetischen, Afghani-
schen und Balu5i, vgl. osset. nawr, nvar *Ader = zd.
snavare *Sehne' (phi. snavar ist nur Umschreibung des Zend-
wortes); nain 'baden*, zd. skr. sna; afgh. n^Or 'Schwieger-
tochter = bal. nasCir = skr. snusd-. So ist vielleicht
anl. sn auch im Persischen zu n geworden. Ueber sinCL,
Osna *Schwimmen* siehe oben p. 81. Inl. sn bleibt im Zend,
vgl. sasna-, im Persischen fehlen sichere Beispiele. Viel-
leicht ist es hier zu sn geworden, vgl. u§nan *Seifenkraut'
== zd. *usnana' aus us + snana- (oben p. 15).
Ueber ns = np. ng siehe § 109, c; iiber gn siehe
§ 143, b.
*) Naoh Bartholomae, Stud. II, 94 = arisoh *bhundhna-,
•j Vgl. § 9, b.— 254 -
§ 149. Im Auslaut tritt einigemal m fiir n ein: ban
= bam *Dach, Haus* (oben p. 24); Bahram — Vahram,
arm. Vahram , alter phi. Varahran, arm. Vahagn — zd.
veredrayna-; paz. awastam confidence, reliance' = phi.
apastdn, arm. apastan 'Vertrauen, Zuflucht*; pars! panam,
```


## [2026-09-14T02:29:51.532Z] TOOL CALL #24: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1298 2>&1 | head -60"
}
```


### [2026-09-14T02:29:52.619Z] TOOL RESULT

```
REF: BQT:1298  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 89  OCR-lang: fas

شمفاد -۱۹-
شمخاد ه بکراول‌بروزن بهزادءممروف وبعربی آذان‌الفار کوبند .
است. وآن درختی باشد که چوب آن در غات شمشک * - بکر اوز و فتح نانی
سختی و ملائی بود و از آن چیزها سازند ۱ - | واسکون ثالك‌وکاف , بلفت زند وپازند(۱) کاجد
و مرزنگوش را نی ز گوبند » وآن نوعی ازریحان | راکوبند و آن دانه‌ای باشد معروف که(؟)ازآن
باشد در غایت سبزی و خوشبویی ؛ و بفاح اول | روغن کیرند.
م آمده است - و کنایه از فامت خوبان هم شمذور * بنم اول بروزن پرزورء بلفت
هت , کیلانی رستنیی باشد که برکه آن ببر کهسمتر
شمخار - بکراول‌برون یار شاخهای ماند و در آشپای ترش «داخل کنند و روغن‌آن
تازه را گوبند که از درخت شمعاد برآید وب رکه درد گوش را تافعم است.
آن درمایت سبزی و لطافت وطاراوت و نزاکت شمشیر ۹ « بفتح اول بروزن نخجیر .
باشد و ازغایت با ز کی میل بجانب زمین کندلهذا معروفت و وجه تمه آن شم شیر است که‌دم
شعر!آ ترا پزلف خوبان تشبیه کرده‌اند ۲ ,وبعضی
کوبند درختی است مانند شمشاد وآاهم پیوسته
سبز وخرم میباشد وازچوب آلهم چیزهامیتراشند ی موی
وی دیگر کوبند شمشاد و شمشار هر دو یکی | ۳
است اختلاف در دال ورا شده است ۳ ۰
شمشدر ۴ « با رال و رای بی شله شمشیر
بروزن ستمگر , بلفت زند وپازند (۱)سیر براور | شیر وناخن شیر باشد چه شم بممنی دم و ؛اخن
از راکویند . هردوآمده است ۷ - وروشنایی صبح‌وآفتاب‌رانیز
شمشُر ! - با رای بی‌قطه پروزن غمزداء گوبند . ۹ 9
رستنیی باشد دوابی و آنرا مرزاگوش خوانند شمشی ر گوشتین « بممنی تبغ کوشتین
() چك: ژند ویاژند . (۷) چش: و .
‎٩‏ - پیاوی 5132108118۲ * بندهش ۱۱۹ و ۱۰۳ طبری 51305172۲ » مازندرانی
کنونی 5131512۲ و 512۲ ر510812۳ د«واژه‌نامه1۸۷ س 561۳06۲۷1۲65 3025 . شمعاد
( درتهران) - شعماد رسمی * 12000102 1۷۵۲۵2۲۷5 «نابتی ۱۹4 ورك: کل تلاب۲۰۹.
۴ - فدای آن قد وزلاش که کوبی «رو هشته است از شم‌شاد شمغار .
زسشی. «لغخت فری 6
۴ درد ح ۰.۱ ۴ - وز , 5030)8(910)2(4127۲ ( ونظایرآن) » پهلوی
6 » پیاز «,ونکر ۰۸۹ 8 - مصحف هز . ‎٩)1(771)8۱8‏ و 510280 ۰
پهلوی 60ز۳۷8 . کنجد :۰ ونر ۰.۹۸4 ‎٩‏ - بهاوی 51215۳6۲ «دب رکه ۲۱۳ >
هر اوراق مانوی (بمهاوی) ‎٩12709101۲‏ و 82۲912۲ :
.8505 ۳۲۹120 6ا1:00 ۶ اهنا ه هدند
۷ - و<ه آشته‌اق عامانه ۰
(برهان قاطع ۱۱۷)
```


## [2026-09-14T02:29:53.285Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== MON shams'; grep -n -o '.\\{0,180\\}شمس\\[.\\{0,120\\}' MON_part1.txt | head -5; echo '--- MON شمس ('; grep -n -o '.\\{0,100\\}شمس .\\{0,150\\}' MON_part1.txt | head -8"
}
```


### [2026-09-14T02:30:00.491Z] TOOL RESULT

```
=== MON shams
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,120}
                          \___exceeds complexity limits


--- MON شمس (
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,150}
                         \___exceeds complexity limits
```


## [2026-09-14T02:30:11.319Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nfor fn in ['incoming/BQT/BQT_v3_pages.txt']:\n    txt=open(fn,encoding='utf-8',errors='replace').read()\n    pages=txt.split('\\f')\n    for i,p in enumerate(pages):\n        if 'شنا' in p and ('شناور' in p or 'شنا ' in p):\n            heads=[l for l in p.split('\\n') if 'شنا' in l][:4]\n            m=re.search(r'\\[pdf page (\\d+)\\]',p)\n            print(i, m.group(1) if m else '?', ' | '.join(h.strip()[:90] for h in heads))\n            if i>120: break\nEOF"
}
```


### [2026-09-14T02:30:12.431Z] TOOL RESULT

```
42 43 ‏آمده است (۲) که آب ورزی و شناوری باشد. | ‏8 - ممحت «دناء» ‎She‏ آشنا (هم) . ‎pet‏ مق( + پهلوی
53 54 باشد که ‎ect Ok‏ دیدار آشنا را .«حافظ شیرازی 0+
84 85 شنا ‎oh‏ یک راولبروزن‌منا . معروف | است که شناوری وآب ورزی باشد . | شناب ۴ = ‎ING‏ بروزن‌ساب ۰ | بمملی شناست که آب ورزی باشد . *
89 90 شنا و۴ = باواو . بروزن و معنی ناب | اعت که شذاوری وآب ورژی بائد(۱) - و شنا | شناه ۴ | بمعتی شناواست که ‎CT‏ ورزی- وشنا کننده(۳)
120 121 ۴ شنا ‎(pe)‏ = شتاب (هم) .
442 443 کشتی ‎he‏ مه کن‌ابه از شناوری | کردن وشناور شدن باشد :
```


## [2026-09-14T02:30:13.218Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nfor fn in ['MON_part1.txt','MON_part2.txt']:\n    txt=open(fn,encoding='utf-8',errors='replace').read()\n    for pat in ['شمس','سامسون','صنعت']:\n        idxs=[m.start() for m in re.finditer(pat,txt)][:4]\n        print('==',fn,pat,len(idxs))\n        for i in idxs:\n            print('   ...',txt[max(0,i-90):i+150].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:30:14.393Z] TOOL RESULT

```
== MON_part1.txt شمس 4
   ... ر است.    مقد مه ۵    سعین :701 محمد (و. هفدهم رجب ۱۳۳۲ هجری قمری مطابق ٩‏  اردیبهشت ۱۲۹۷ شمسی. ف. ۱۳ تیر ماه ۱۳۵۰ ه.ش). فرزند مرحوم شیخ  ابوالقاسم. در شهر رشت در خانواده‌ای روحانی متولد گردید. به هنگام طفولیت  او نخست مادر و پس از پنج روز 
   ... دبیات به تدریس مشغول  شد و سه سال نیز در دانشسرای عالی به تدریس پرداخت. از آغاز سال ۱۳۲۵  شمسی که طبع لغت‌نامة علامهةٌ مرحوم علیاکبر دهخدا طبق قانون» در مجلس  شورای ملی شروع شد؛ دکتر معین به همکاری وی برگزیده شد. در دی ماه  ۴ با موافقت علام
   ... مینیأتور   مژنث   نجوم   نجاری   نسبت(اسم یاصفت منسو ب)  نظامی   نقاشی    هجری فمری  هجری شمسی  همه معانی  هندی (زبان)  هواشناسی  هواپیمایی    هست    پونانی    نشانه‌های مربوط به کتاب‌ها؛ ملفان؛ مصحفان و ناشران:    اد. ادنب پشاوری سنائی. دی
   ... ] (.) ج. ابل» شتران  ابان: معهة (ج. آب؛ آب‌ها] (.) (اخ.) ایزد  نگهبان آب. ماه هشتم از سال شمسی که  طبق تقویم کنونی مطابق با ماه دوم پاییز  است. . رور دهم هر ماه شمسی.  آب‌انبار: 2.۲ (امر.) محفظه‌ای که در  آن همواره آب خوشگوار ذخیره کنند»  م
== MON_part1.txt سامسون 0
== MON_part1.txt صنعت 4
   ...  از آن برای شستن دست  و دهان بکار برند. وضوء دست‌نماز. استنجا  کردن به آب. لطف و مهارت در صنعت.  ات اه30-02 (امر.) زاهد و با کدامن.  کسی که دست او در کار چیرگی کند؛ سخت  چایکك ماهر استاد. مستراح؛ مبرز: جایی.  قسمی جامه؛ لباده. جبةٌ آستین کو
   ... ) کرم  شب تاب.  آتشین: 202)0(1-0 (ص نس..) اشع,  آه  آتشسین پ ینحه: (6-)02012-.2 (ص‌مسر.)  صنعتگر ماهر صانع چیر ۵ دستا.  آتلیه: 6 (.) کارگاه هنر مندان» محلی  که جمعی هنرمند زیر نظر استادی به کار  پردازند.  اتمسفر: ۲ تو ده هوایی که اطراف  کر 
   ... جه بصورت ارقام و اعداد است مثل  شمارة جمعیت یک ده» یکك شهر» یک  ایالت» یکك کشور» مسحصولات صنعتی؛  مسحصولات فلاحتی» ادیان و مداهب و  بیروان آنها؛ مالبات‌ها و غیره؛ احصصائبه  (فره.) ادارة آمار: اداره‌ای که وظمفة آن  جمع آوری اطلاعات مربوط به 
   ... از تجزبة  اور ادرار به وسیلةٌ میکرب مخصوص و نیز  از تکلیس نشادر با آهکث بدست می‌آید و  در صنعت و طب مستعمل است.  امسسونیوم. صمرزممصسق ( ( ( شیم ۰ در  ترکسات آمونباک مسجموعه بنام  آمونیوم دارای خواصی شبه به خواص  فنازات قسلیایی است» یکی از ت
== MON_part2.txt شمس 4
   ... ادف فرودگان آمده.  فروردین: ه۱<3 [- فرودین» ریةٌ به  معنی فرودهای باکان] (.) ماه اول سال  شمسی و آن مدت توقف آفتاب است در  2( و مدت آن را اکنون ۳۱ روز  گر ند. نام روز نوزدهم از هر ماه شمسی  (فروردین روز).  فشرورفتن: 107-0 (مص‌ل.) به زبر  رف
   ...  و آن مدت توقف آفتاب است در  2( و مدت آن را اکنون ۳۱ روز  گر ند. نام روز نوزدهم از هر ماه شمسی  (فروردین روز).  فشرورفتن: 107-0 (مص‌ل.) به زبر  رفتن» پایین رفتن. غوطه‌ور شدن. نفود  کردن» داخل شدن.  فروز: 0752) [- افروز] (.) روشنی»  روشنایی.
   ... فضاء: 2 [ع. . ف. فضا| ((.) مکان وسیع»  زمین فراخ ساحت. (جف.) مکانی که کرة  زمین در منظومة شمسی اشغال می‌کند.  فضاحت؛ ادطاقه«۲ ۵ فضاحة | (امص.)  رسوایی  ۱0 11 ۷2:- 28 [ع. ۳  فضانوردنده] (ص‌فاء) (نو.) کسی که ۲  وسله‌ای جهنده به فضا پرواز کند.
   ... ی صنعتی و ساختن موشک‌های  سر یع السیر» شر را به فکر فضانوردی و  کشف اسرار ستارگان منظومةً شمسی که  خورشید مرکز آن است و کر خاکی ما  یکی از سبارات آن شمار می‌رود انداخت.  کشف این اسرار علاوه بر اینکه دنباهای  ناشناخته را سه انسان می‌شناساند.
== MON_part2.txt سامسون 0
== MON_part2.txt صنعت 4
   ... ی. نوی.   فر: (۲۲:] (اصت  فراورده. ()۸۲-۱۷۸۱)۵(۲۸] (امف.) فراهم  اورده. محصول ( کسافزرخ ت صنعتی )    ) (عم.) آواز گرفتن اخلاط    ۱۰ ۱  ضح. ۳ یافته.  فرا: 1*۲2 (پشف.) بر سر فعل درآید و آن در  اصل به معنی به؛ سویء در باشد. (حر. اض.)  ده زر دب
   ... .]  (حامص.) انسان‌های فضانورد با وسیله‌ای  جهنده بنام «موشکٌ» به فضا می‌روند.  بیشرفت‌های صنعتی و ساختن موشک‌های  سر یع السیر» شر را به فکر فضانوردی و  کشف اسرار ستارگان منظومةً شمسی که  خورشید مرکز آن است و کر خاکی ما  یکی از سبارات آن شما
   ... گوش و اسب  فم المعده در بجه‌ای دارد.   فن: (0)«: [ع.] (.) حال» گونه (غم.) شاخ  درحت. (ف.) صنعت؛ صشبر . فربب.» حله.  (مست.) تعمه راه (موسیقی). راه» روش 3  فناء: 007 (ع. ف. فنا] (.) (کیا.) سگک  انگور.   فناء «ع) [ع. . ف. فنا] (.) پیشگاه فراخ 
   ... روف  با تمام آن را چون برگردانند همان لفظ با  لفظی دیگر یا ترکیبی دیگر حاصل شود.  بالجمله صنعت قلب بر سه قسم است: الف -  ای ساوسو رات   بیتی يا فقره‌ای واقع شود که هر کدام قلب   دک فا ب - قلب مستوی ع ]  مصراعی یا عبارتی باشد که چون از آخر
```


## [2026-09-14T02:30:26.658Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (84,89):\n    print('===== leaf',i)\n    print(txt[i][:2500])\nEOF"
}
```


### [2026-09-14T02:30:27.741Z] TOOL RESULT

```
===== leaf 84
[pdf page 85]
NTS ke

شذاوری وآب ورزی باشد 9 - وبه‌منی ‎Asad‏
‏وشوم وهی ‎٩‏ وانگه وعار هم ‎Vali‏ -
و ولابت خرابی را نیز کویند که کی در آن
توطن نکند و خالی از ءردمان باشد - و شاخ

پوست ‎OT‏ رسمان پتاپند ‎٩‏ - و در عربی دام
قبیله است - وخيك کهنه - وپاشیدن آبرا نیز
کوند ۴ .

شنا ‎oh‏ یک راولبروزن‌منا . معروف
است که شناوری وآب ورزی باشد .

شناب ۴ = ‎ING‏ بروزن‌ساب ۰
بمملی شناست که آب ورزی باشد . *

شنار © پکسر اول بروزن‌چنار » بمعنی

لوبرا گونند که ازه از درخت پر آبد - ودر
عربی ۷ - ‎yee‏ دشمنی کردن‌باشدودشن‌داشتن
یعلی با کی وچیزی بدبودن .

شنان @ ‎ge‏ اول , ‎dite‏ آشنان امت

۱ - پهلوی ‎shan‏ ) & شاهدانه , کنف) « ناوادیا ‎٩۱۹۵‏ - شن‌در نورو کچور وزبارت

= شونگ = ‎Lonicera‏ > ثابتی ۰۱۹4 . ۴ شن پکس اول » ریگهای یار ریزه که
درکتار ‎bys‏ و رود بسیار است ؛ ماسه . ۴ _ هه شناء -- آشنا « لفت 48 = شنار

شناب ‏ شناو )¢0(=

شیتاب (ه.م ‎dan‏ اوستابی-
‎Any (ysl, os ( 8‏
هندی‌باستان - 508(اسحمام
کردن).استی 0218 (استحمام)
و ‎axsoun‏ ر ‎axsoin‏
‏(شتن) «اسشق ‎VAY‏ ورك :
هوبتمان ۷۹۲ ۰ ‎SS‏
‏۷ طبری 02500
ماد رالی ‎send eS‏ و
0 « واژه‌نامه ۰۳۰۸ ۰

۴ رل : شنا . انوا اع‌شنا

۵ _ رل : شدا :

بدر گفت مردی وی رود بار برود اندرون شوهمی بی شنار .
برشکور بلخی . «لفت فرس ‎NE‏
‎٩‏ - (عر) « شنار (بقتح اول ) عیب بدتر و عار و امر مشهور ببدی © ‎HOM ged‏
5 آیکه با شکری ‎oy‏ شوم وشنار میبرد نا شکر را تا قصی ار..
مواوی. « فرهنک نظام ‎A‏
‏# شناخفی-بکسراول وفنح‌پنجم ‎pings)‏ کزی). پرلوی 5102:1020 ؛ابرانی‌باستان-
4 بارنوامه 6004 از- 04[ «بب رکه ۰۲۲۱۷ پارسی‌بادتان ‎xshndsatiy‏ (شناختن) «
کردی 28510 ( شناختن ) ‎evar gol‏ ورك : هوبشمان ‎vay‏ ؛کیلکی ‎Shanaxtan‏ +
دالستن » ممرفت یافتن » وفوف یافتن - افرار کردن - دوستی داشتن .

===== leaf 89
[pdf page 90]
{Aa

رآن‌گیاهی باندکه بدان رخت شویند ‎٩‏ -
‎Ky‏ اولدارویی است ‎YTS‏ پیونالی فراسیون
کریند وبدیرازی کندنای کوهی خوانند. وبعضی
کوبند ‎ink‏ ممتی عربی است .

شنا و۴ = باواو . بروزن و معنی ناب
اعت که شذاوری وآب ورژی بائد(۱) - و شنا
کننده را نیز گویند(۱) .

شناه ۴

بمعتی شناواست که ‎CT‏ ورزی- وشنا کننده(۳)

بکر اول بر وزن نگاه .

. atk
‏شنت - بغتح اول و سکون ثانی و بای‎
‏وازین است که کنبذیرا‎ ath ‏ابجد, معنی کنبذ‎
‏که سلطان غازان درآذربا‎
. ۴ ‏غازان‎ LT ee ‏غازان خوانند‎
‏یکربای ابجد بروزنمجد.‎ = © eee
. ٩ ‏شنبه راگویند که روز اول هفته باشد‎

شنپلیت ۷ - بقتح اول و کون ‎GS‏

ان ساخته ‎oy‏ شنب

(۱) چش : - باشد . (۷) چش :

(۳) چش: - ‎lity‏ کنندء .

. ‏اننان (هم)‎ < ٩
. ‏رك: شنا‎ ۴
5 ‏در محل ۶« شام‎
‏ابنيةٌاسلامی وا‎

و بای ابجد مفتوخ ولام بتحتالی رسیده وبفوقالی
زد , تخمی است که محلل نفغ بائد وگل ‎OT‏
‏زردرنگ ‎cl‏ و شبیه به بهار ارنج و بوی‌نیزی
دارد . بوبیدن ‎OT‏ دفع ‎AS por‏ وآثرا کل‌راه
بند چه بیشتی در سر راهها روید.
شنیلید ۵ - با دال ابجد » بروزن‌ومعنی
شنبلیت است که کل راه رو باشد و بمربی ‎ade‏
‏کویند ؛ و بعضی کوبند شنبلید کل و ‎BCs‏
‏سورنجان است ؛ و بعضی دیگر کویند ب رکه
سورتجان است .

٩ abt

رو

بر وزن سرطویله ؛ بمعنی
اول شنبلید است و ‎OT‏ رستنیی باشد که بعریی
حلبه و بپندی میتی *۱ و بیوتالی‌فر بفه‌خوانند .
شنبه بفتح اول و ثالث بروزن خنده,
‎days‏ اسب راگویند و بعربی ‎hee‏ خوانند!۱-
و آواز شیر را یز کفته‌اند که از ‎the‏ سباع
است ‎WV‏ و بکسر ‎SNE‏ و ظپور ها ممروف است

وشنا کننده باشد .

۴ رك : لفت فری ص ‎٩‏ ورك: شنا .
۴ - دنب غازان ‏ شام غازان » چه‌غازان‌غان (۷۰۳-۹۹4)
بز٩‏ که درسه ریم فرسنگی ‎oye‏ تبربز قرار داشت + قبه‌ای‌ساخت ازعجایب
در ‎JL‏ سوم سلطنت غازان شروع و در ۷۰۲ ‎WL‏ رسید این ینارا بمدها

«شذب غازان» ‎lek‏ غازان» خواندند. «عبای‌اقبال. تاریخ مفول ص ۰۳۰۵-۳۰4 ‎٩  .‏ ع شنبه:

1 - بفال ‎ds‏ بروز ‎Aye‏ شنبد

. ‏شماید‎ oe alice  ).مه(دیلبنش‎ = ۷
. ۷۹۰ ‏دزی حجاص‎ « flores colchici autumnalis =

لبید کیر ومده روز کار خویش ببد .
«+ منوچهری دامغاتی ‎٩۱۷۷‏ .
۸ = شتبلیت. ‎ope‏ آن بیزهدنبلیده»
‎٩‏ - رك: شذبلید »

‎oe‏ . معرب ‎Fenugrec  »هلیلبند« ol‏ « رزی ج ۱ص ۷۹۰ ۲ ر آن ‎AS‏ علفی
‎Trigonella foenumgroecum (‏ ) و یکاله ‎JTL‏ زرد میباشد وبیشتر در بتانهاکاشته
میشود » بر گهای نازه وخشك آهرا در قورمه سبزی وخورشت‌های دیگر بکاربرند « ستوده ۰۱۰۹
این ‎lS‏ از ‎Los‏ شبدرها ازتير# پرواله واراتست. « کل ‎HENNE GUT‏

‏۶- «میتی ‎gare hd‏ الاصلبتای »خلوط التلفظ بهاست که‌تلفظ ‎OF‏ برغیرهندیدشوار

‏باشد بدیین صورت (میتهی)» «چك ص 4۸۳ح». ‎NY‏ مسحف «شنه» (هم.) .
```


## [2026-09-14T02:30:28.693Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(txt):\n    if 'اشنان' in p or 'أشنان' in p:\n        ls=[l.strip() for l in p.split('\\n') if 'شنان' in l][:5]\n        print(i, ' | '.join(l[:100] for l in ls))\nEOF"
}
```


### [2026-09-14T02:30:29.707Z] TOOL RESULT

```
106 چويك اشنان ) .
116 چوباك اشنان ٩‏ ( ذیل :آذریو »آذربویه » سطرونیون » عدر نا » عرطنینا »
233 اشنان است و آن زرد رنگ میباشد و بونهُ آن | ] ذد و 4 - ختح بای‌حطی: کل‌اشنان
357 اشنان پم اول پروزن نمان. کیاهی | اشنان ۵ارو - ائنان معلوم ودال | اه ه بنم اولوفتح اك » بمعنی‌اشنان
515 باشده و آن بیخ خارست که اشنان گویند .کر
516 باشد و آن سمخ خارست که‌اشنان و چوبك‌اشنان
```


## [2026-09-14T02:30:47.347Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport json,os\np='incoming/BQT/BQT_v3_pagemap.json'\nif os.path.exists(p):\n    m=json.load(open(p))\n    if isinstance(m,dict):\n        items=list(m.items())[:5]; print(items)\n        for k,v in m.items():\n            if str(v)=='1298' or str(k)=='1298': print('MATCH',k,v)\n    else: print(type(m), str(m)[:500])\nelse: print('no pagemap')\nEOF"
}
```


## [2026-09-14T02:30:48.240Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(txt[357][:2600])\nEOF"
}
```


### [2026-09-14T02:30:48.703Z] TOOL RESULT

```
[('pdf', 'data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf'), ('pdf_pages', 721), ('offset_mode', 1203), ('anchors', 34), ('map', {'1210': 1, '1211': 2, '1212': 3, '1213': 4, '1214': 5, '1215': 6, '1216': 7, '1217': 8, '1218': 9, '1219': 10, '1220': 11, '1221': 12, '1222': 13, '1223': 14, '1224': 15, '1225': 16, '1226': 17, '1227': 18, '1228': 19, '1229': 20, '1230': 21, '1231': 22, '1232': 23, '1233': 24, '1234': 25, '1235': 26, '1236': 27, '1237': 28, '1238': 29, '1239': 30, '1240': 31, '1241': 32, '1242': 33, '1243': 34, '1244': 35, '1245': 36, '1246': 37, '1247': 38, '1248': 39, '1249': 40, '1250': 41, '1251': 42, '1252': 43, '1253': 44, '1254': 45, '1255': 46, '1256': 47, '1257': 48, '1258': 49, '1259': 50, '1260': 51, '1261': 52, '1262': 53, '1263': 54, '1264': 55, '1265': 56, '1266': 57, '1267': 58, '1268': 59, '1269': 60, '1270': 61, '1271': 62, '1272': 63, '1273': 64, '1274': 65, '1275': 66, '1276': 67, '1277': 68, '1278': 69, '1279': 70, '1280': 71, '1281': 72, '1282': 73, '1283': 74, '1284': 75, '1285': 76, '1286': 77, '1287': 78, '1288': 79, '1289': 80, '1290': 81, '1291': 82, '1292': 83, '1293': 84, '1294': 85, '1295': 86, '1296': 87, '1297': 88, '1298': 89, '1299': 90, '1300': 91, '1301': 92, '1302': 93, '1303': 94, '1304': 95, '1305': 96, '1306': 97, '1307': 98, '1308': 99, '1309': 100, '1310': 101, '1311': 102, '1312': 103, '1313': 104, '1314': 105, '1315': 106, '1316': 107, '1317': 108, '1371': 164, '1372': 165, '1373': 166, '1374': 167, '1375': 168, '1376': 169, '1377': 170, '1378': 171, '1379': 172, '1380': 173, '1381': 174, '1382': 175, '1383': 176, '1384': 177, '1385': 178, '1386': 179, '1387': 180, '1388': 181, '1389': 182, '1390': 183, '1391': 184, '1392': 185, '1393': 186, '1394': 187, '1395': 188, '1396': 189, '1397': 190, '1398': 191, '1399': 192, '1400': 193, '1401': 194, '1402': 195, '1403': 196, '1404': 197, '1405': 198, '1406': 199, '1407': 200, '1408': 201, '1409': 202, '1410': 203, '1411': 204, '1412': 205, '1413': 206, '1414': 207, '1415': 208, '1416': 209, '1417': 210, '1418': 211, '1419': 212, '1420': 213, '1421': 214, '1422': 215, '1423': 216, '1424': 217, '1425': 218, '1426': 219, '1427': 220, '1428': 221, '1429': 222, '1430': 223, '1431': 224, '1432': 225, '1433': 226, '1434': 227, '1435': 228, '1436': 229, '1437': 230, '1438': 231, '1439': 232, '1440': 233, '1441': 234, '1442': 235, '1443': 236, '1444': 237, '1445': 238, '1446': 239, '1447': 240, '1448': 241, '1449': 242, '1450': 243, '1451': 244, '1452': 245, '1453': 246, '1454': 247, '1455': 248, '1456': 249, '1457': 250, '1458': 251, '1459': 252, '1460': 253, '1461': 254, '1462': 255, '1463': 256, '1464': 257, '1465': 258, '1466': 259, '1467': 260, '1468': 261, '1469': 262, '1470': 263, '1471': 264, '1472': 265, '1473': 266, '1474': 267, '1475': 268, '1476': 269, '1477': 270, '1478': 271, '1479': 272, '1480': 273, '1481': 274, '1482': 275, '1483': 276, '1484': 277, '1485': 278, '1486': 279, '1487': 280, '1488': 281, '1489': 282, '1490': 283, '1491': 284, '1492': 285, '1493': 286, '1494': 287, '1495': 288, '1496': 289, '1497': 290, '1498': 291, '1499': 292, '1500': 293, '1501': 294, '1502': 295, '1503': 296, '1504': 297, '1505': 298, '1506': 299, '1507': 300, '1508': 301, '1509': 302, '1510': 303, '1511': 304, '1512': 305, '1513': 306, '1514': 307, '1515': 308, '1516': 309, '1517': 310, '1518': 311, '1519': 312, '1520': 313, '1521': 314, '1522': 315, '1523': 316, '1524': 317, '1525': 318, '1526': 319, '1527': 320, '1528': 321, '1529': 322, '1530': 323, '1531': 324, '1532': 325, '1533': 326, '1534': 327, '1535': 328, '1536': 329, '1537': 330, '1538': 331, '1539': 332, '1540': 333, '1541': 334, '1542': 335, '1543': 336, '1544': 337, '1545': 338, '1546': 339, '1547': 340, '1548': 341, '1549': 342, '1550': 343, '1551': 344, '1552': 345, '1553': 346, '1554': 347, '1555': 348, '1556': 349, '1557': 350, '1558': 351, '1559': 352, '1560': 353, '1561': 354, '1562': 355, '1563': 356, '1564': 357, '1565': 358, '1566': 359, '1567': 360, '1568': 361, '1569': 362, '1570': 363, '1571': 364, '1572': 365, '1573': 366, '1574': 367, '1575': 368, '1576': 369, '1577': 370, '1578': 371, '1579': 372, '1580': 373, '1581': 374, '1582': 375, '1583': 376, '1584': 377, '1585': 378, '1586': 379, '1587': 380, '1588': 381, '1589': 382, '1590': 383, '1591': 384, '1592': 385, '1593': 386, '1594': 387, '1595': 388, '1596': 389, '1597': 390, '1598': 391, '1599': 392, '1600': 393, '1601': 394, '1602': 395, '1603': 396, '1604': 397, '1605': 398, '1606': 399, '1607': 400, '1608': 401, '1609': 402, '1610': 403, '1611': 404, '1612': 405, '1613': 406, '1614': 407, '1615': 408, '1616': 409, '1617': 410, '1618': 411, '1619': 412, '1620': 413, '1621': 414, '1622': 415, '1623': 416, '1624': 417, '1625': 418, '1626': 419, '1627': 420, '1628': 421, '1629': 422, '1630': 423, '1631': 424, '1632': 425, '1633': 426, '1634': 427, '1635': 428, '1636': 429, '1637': 430, '1638': 431, '1639': 432, '1640': 433, '1641': 434, '1642': 435, '1643': 436, '1644': 437, '1645': 438, '1646': 439, '1647': 440, '1648': 441, '1649': 442, '1650': 443, '1651': 444, '1652': 445, '1653': 446, '1654': 447, '1655': 448, '1656': 449, '1657': 450, '1658': 451, '1659': 452, '1660': 453, '1661': 454, '1662': 455, '1663': 456, '1664': 457, '1665': 458, '1666': 459, '1667': 460, '1668': 461, '1669': 462, '1670': 463, '1671': 464, '1672': 465, '1673': 466, '1674': 467, '1675': 468, '1676': 469, '1677': 470, '1678': 471, '1679': 472, '1680': 473, '1681': 474, '1682': 475, '1683': 476, '1684': 477, '1685': 478, '1686': 479, '1687': 480, '1688': 481, '1689': 482, '1690': 483, '1691': 484, '1692': 485, '1693': 486, '1694': 487, '1695': 488, '1696': 489, '1697': 490, '1698': 491, '1699': 492, '1700': 493, '1701': 494, '1702': 495, '1703': 496, '1704': 497, '1705': 498, '1706': 499, '1707': 500, '1708': 501, '1709': 502, '1710': 503, '1711': 504, '1712': 505, '1713': 506, '1714': 507, '1715': 508, '1716': 509, '1717': 510, '1718': 511, '1719': 512, '1720': 513, '1721': 514, '1722': 515, '1723': 516, '1724': 517, '1731': 528, '1732': 529, '1738': 531, '1739': 533, '1751': 548, '1752': 549, '1753': 550, '1754': 551, '1755': 552, '1756': 553, '1757': 554, '1758': 555, '1759': 556, '1760': 557, '1761': 558, '1762': 559, '1763': 560, '1764': 561, '1765': 562, '1766': 563, '1767': 564, '1768': 565, '1769': 566, '1770': 567, '1771': 568, '1772': 569, '1773': 570, '1774': 571, '1775': 572, '1776': 573, '1777': 574, '1778': 575, '1779': 576, '1780': 577, '1781': 578, '1782': 579, '1783': 580, '1784': 581, '1785': 582, '1786': 583, '1787': 584, '1788': 585, '1789': 586, '1790': 587, '1791': 588, '1792': 589, '1793': 590, '1797': 592, '1819': 616, '1820': 617, '1821': 618, '1822': 619, '1823': 620, '1824': 621, '1825': 622, '1826': 623, '1827': 624, '1828': 625, '1829': 626, '1830': 627, '1831': 628, '1832': 629, '1833': 630, '1834': 631, '1835': 632, '1836': 633, '1837': 634, '1838': 635, '1839': 636, '1840': 637, '1841': 638, '1842': 639, '1843': 640, '1844': 641, '1845': 642, '1846': 643, '1847': 644, '1848': 645, '1849': 646, '1850': 647, '1851': 648, '1875': 671, '1877': 674, '1878': 675, '1879': 676, '1880': 677, '1881': 678, '1882': 679, '1883': 680, '1884': 681, '1885': 682, '1886': 683, '1887': 684, '1888': 685, '1889': 686, '1890': 687, '1891': 688, '1892': 689, '1893': 690, '1894': 691, '1895': 692, '1896': 693, '1897': 694, '1898': 695, '1899': 696, '1900': 697, '1901': 698, '1902': 699, '1903': 700, '1904': 701, '1905': 702, '1906': 703, '1907': 704, '1908': 705, '1909': 706, '1910': 707, '1911': 708, '1912': 709, '1913': 710, '1914': 711, '1915': 712, '1916': 713, '1917': 714, '1918': 715, '1919': 716, '1920': 717, '1921': 718, '1922': 719, '1923': 720, '1924': 721})]
```


### [2026-09-14T02:30:49.859Z] TOOL RESULT

```
_ٍِِ
اشکو خیدن . مصدر اشکوخ است
که لفزیدن دبسردرآمدن وافتادن‌باشد , چها کر
کی را پایش از یش بدد رود و یفئد گویند
اشکوخیه .
اشکو 4 ه بن اول , بسنی شکوفه
و بهار درخت باشد - و فی و استفراغ را لبز
گویشد ۱.
اشکوه « بنم اول والث وسکون تانی
و واو و ها ء بمعنی شآن و شوکت و شکوه
وعنلمت باشد ۴ .
اشکیل؟ بکراول وثاكك وسکون‌الی
وئحتانی ولام » بمعنی اک ات وان اسبی‌بود
که دست راست وپایچپ او سفید باشد - ومکر
وحبله وفریب را نیز کویند .
اشکیل چشم - اشکیل مملوم و نتح
جیم فارسی وشم شین قرشت وسکون‌ميم. دوایی
است که آیرا عوسج کوبند جاگ بر کف ای را
بکوبند و آب آنرا بگیرند و هفت دوز درچشم
چکانند مفیدی چشم کد هم رسیده باشد زایل
گنت -
اشکیوة » بنتح اول و سکون انی
وثالث وبای حطی بواو رسیده وبدال زده» مر کب
را گوبند که درمة بل‌مفرد است ؟ .
اشمو‌سا - بفتح اول و سن بی نفطه
بالف کشیده بر وزن محمودا ۰ بلفت بونانی نوعی
از مرو باشد که آنرا بشیرازی مرورشك خوانند
و بوی‌آن کمتر از مرو خوش‌باشد .
۵ و _
6 رك . آشنا . 1
فرهنگه روستایی ۱۸۰ . ۲ - محرف اشتو
آشن ‏ بنتح اول و ثانی بر وزن کفن »
جات باز گونه پوشیده را گویند - و بمعنی
کالك هم آمده است که خربز؛ نارسیده باشد .
اشنا - بفتح اول و سکون نانی و الث
بالف کشیده , کوهر کرانمایه را گویند - وبممنی
شنا کننده و آب ورزهم آمده استه .
اشتاب ه بکر اول بر وزن محراب »
یمعنی شنا وشناوری‌باشد 6 .
اشنان پم اول پروزن نمان. کیاهی
باشد که بدان رخت شویند و بمد ازطعام‌خوردن
دست پیزبدان بشویند وآنرا بمربی‌غاسول‌خوانند
و چون آنرا بموزانند اشخارشود ٩‏ .
اشنان ۵ارو - ائنان معلوم ودال
بی نفطه بالف کشیده و رای بواو رسیده . زوفای
خشك باشد مشهور بزوفای مصری ؛ وآن.کیاهی
است دوایی شبیه بب رکه حنا » امشفا را نافع
است .
اشنو۷۵ ۰ بنشح اود و ثالث بو واو
وسکون ثانی ودال ابجد » نلم روز دوم است از
خسءة مسترقة قدیم - و بضم اول و الث
بر وزن خوشنود صاشي شنیدن باشد ای
شنبد . 4
۸
آشنوسه «. بکر اول بروزن بی‌توشه,
اه ه بنم اولوفتح اك » بمعنی‌اشنان
است که بدان رخت وجامه شویند - ونام دارومی
د صگو
نامه ۱۶ج ی در لهس
عقه درصفسه ۲ ۱
```


## [2026-09-14T02:30:58.196Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(txt[88][:2600])\nEOF"
}
```


### [2026-09-14T02:30:59.408Z] TOOL RESULT

```
[pdf page 89]
‎seas‏ © بکراول بروزن بهزاده‌معروف
است» وآن درختی باشد که چرب آن در غابت
سختی و ملسائی بود و از ‎OT‏ چیزها سازند ۱ -
و مرزنگوش را بيز کوبند . وآن نوعی ازریحان
باشد در غایت سبزی و خوشبویی ؛ و بفتح اول
هم آمده است - و کنایه از قامت خوبان هم
هت .
‎seed‏ » بکراول‌برون بیارشاخهای
تازه راکویند که از درخت شمشاد برآبد وب رکه
‎OF‏ دردمایت سبزی و لطافت وعاراوت و ‎SV‏
‎ath‏ و ازغایت فاژ کی ‎See‏ بجانب زمین کندلهذا
‎LT as‏ بزلف خویان تشبیه کرده‌اند ۴ »وبسنی
گویند درختی است مالند شمشاد وآلهم پیوسته
مبز وخرم میباشد وازچوب آلهم چیزهامیتراشند
ویضی دیگر کویند شمشاد و شم‌شار هر دو ,یکی
است اختلاف در دال ورا شده است ۳ .

‏شمشدر ۴ با دال و رای بی شطه
پروزن ستمگر » بلفت زد وپازند (۱)سیر ‎why‏
‏ییاز راگوبند .

‏شمشر | = با رای بی‌قطه بروزن غمزداء
رستتیی باشد دوابی ‎UT,‏ می‌زنگوش خوانند

‏(۱) چك: ژند ویاژند .

‎m—\tAt—

‏وبعربی آذان‌الفار گوبند .

‎vw ‏بکر اول و فتح‎ - * os
‏و سکون ثالت‌وکاف » بلغت زلد ویازند(۱) کاجد‎
‏دانه‌ای باشد ممروف که(؟)ازآن‎ oT ‏راکوبند و‎
Sey

‏شمدور = بنم اول بروزن پرزور,بلت
‎SAT‏ رستنیی باشد که ب رکه ‎OT‏ بب ‎eee‏
‎wile‏ و در آشهای نرش داخل کنند و روغن‌آن
دره کوش را دافع است.

‏شمئیر ‘ » بفتح اول ‎Olay‏ تخیر ؛
معروفت و وجه ‎OT Las‏ شم شیر است کهدم

‎۱

‏شمشیر
‏شیر ولاخن شیر باشد چه شم بمعنی دم و ناخن
هردوآمده است ۷ - وروشنابی ‎FAT are‏

‏(۷) چش: و .

‎٩‏ - پپلوی ‎shamshar‏ > بندهش ‎۱۱٩‏ ر ۱۰۳ طبری 5205118۲ ۰ مازندرانی
کتونی ‎shishar‏ و ‎Shahr, shar‏ «واژءامه ۸۷ = ‎Boxus sempervirens‏ . شمشاد
( درتهران) = ششماد رسمی  ‎tay ۱۹4 ale Evonymus japonica‏ کل کلاب۲۰۹.

‏۴ - فدای آن ‎ad‏ وزلفش که گویی

‏۴ رك: ح ۱ .
6 م ‎jly‏ «بونکر ۸6 ۰۰
پهلوی ‎kunjed‏ . کنجد ‎ab Nagy?‏

‏«رو ‎atte‏ است از شم‌شاد شمشار .
زینبی. «لفت فری ۰۱۲۵

‎«(oT lus, ( shom(a)sh(ajdar. » - ۴‏ پهلوی
‎٩‏ ممحف هز . ع90(۳۱)۵۱ و ‎Shimagh‏ ,

‎۲۱۳ oF. Shamsher ‏بهاوی‎ - ۲

‎: Shfshyr ‏و‎ shypshyr ‏در اوراق ماتوی (پپلوی)‎
Henning, A list of Middle Persian..., BSOS., IX,1.p.82.

‏۷ - وچه اشتفاق ءاميامه .

‏(برهان اطع ‎(vw‏
```


## [2026-09-14T02:31:33.982Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(txt))\nfor i in (66,68,700,701,702,732,733):\n    s=txt[i].strip().replace('\\n',' ')\n    print('=== leaf',i,':',s[:300])\nEOF"
}
```


### [2026-09-14T02:31:35.138Z] TOOL RESULT

```
leaves 903
=== leaf 66 : Asia  (Ovis  am- mon).  —  Mongolian. argand  lamp.  —  Named  after  its  inventor  Aim6 Argand,  a  Swiss  physicist  (1755-1803). Argemone,  n.,  a  genus  of  plants  of  the  poppy family  (bot.)  —  Gk.  apyEpuivT),  ‘a  kind  of  pop¬ py’,  prob.  fr.  Heb.  argamdn,  ‘purple’.  Cp.  Ak¬ kad.
=== leaf 68 : and  revert, arpeggio,  n.,  the  playing  of  the  notes  of  a  chord in  rapid  succession  instead  of  simultaneously; a  chord  on  which  the  notes  are  so  played (mus.)  —  It.,  fr.  arpeggiare,  ‘to  play  upon  the harp',  fr.  arpa,  ‘harp’.  See  harp, arpent,  n.,  an  old  French  
=== leaf 700 : r.  L.  recuperatus, pp.  of  recuperare.  See  recuperate  and  -ive. Derivative :  recuperative-ness,  n. recur,  intr.  v.  —  ME.  recurren,  fr.  L.  recurrere, ‘to  run  back,  return,  recur',  fr.  re-  and  currere, ‘to  run’.  See  current,  adj.,  and  cp.  courier, recurrence,  n.  —  Fo
=== leaf 701 : re-  and ducere,  ‘to  lead’.  See  duke  and  cp.  redoubt,  n., reduit,  ridotto. Derivatives:  reduc-er,  n.,  reduc-ihle,  adj.,  reduc- ibil-ity,  n. reductase,  n.,  any  enzyme  that  promotes  the  pro¬ cess  of  reduction.  —  Coined  from  the  abbrevia¬ tion  of  reduction  and  diastase,
=== leaf 702 : tablishment  of  Protestantism  in  the  1 6th cent.  —  See  prec.  word. re-formation,  n.,  a  new  formation.  —  Formed  fr. re-  and  formation.  See  prec.  word, refract,  tr.  v.,  to  bend  (a  ray  of  light,  sound  or heat).  —  L.  refractus,  pp.  of  refringere,  "to break  up',  fr.
=== leaf 732 : fr.  OF.  saluta- cion  (F.  salutation),  fr.  L.  salutationem,  acc. of  saliitatio,  fr.  salutatus,  pp.  of  salutare,  ‘to greet'.  See  salute,  v.,  and  -ation. Derivative:  salutation-al,  adj. salutatory,  adj.  —  L.  salutatorius,  fr.  salutatus,  fr. pp.  of  salutare,  ‘to  greet’. 
=== leaf 733 : s’,  fr.  Samnium,  which  prob.  stands for  *Sabniom  and  is  rel.  to  Sabinus,  ‘Sabine’. See  Sabine  and  subst.  suff.  -ite. Samoan,  adj.,  pertaining  to  Samoa;  n.,  an  inhabi¬ tant  of  Samoa.  —  Formed  with  suff.  -an  fr. Samoa,  name  of  a  group  of  islands  in  Polynesia. De
```


## [2026-09-14T02:32:05.447Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; python3 - <<'EOF'\nimport json,glob,re\nrows=[]\nfor fn in sorted(glob.glob('page-*.json')):\n    try: d=json.load(open(fn))\n    except: continue\n    def walk(o):\n        if isinstance(o,dict):\n            for rc in o.get('ref_check',[]) or []:\n                if str(rc.get('ref','')).startswith('KLN:'):\n                    rows.append((fn,rc.get('ref'),rc.get('status'),str(rc.get('note',''))[:200]))\n            for v in o.values(): walk(v)\n        elif isinstance(o,list):\n            for v in o: walk(v)\n    walk(d)\nfor r in rows[-25:]: print(r)\nprint('total',len(rows))\nEOF"
}
```


### [2026-09-14T02:32:06.933Z] TOOL RESULT

```
('page-87.json', 'KLN:576', 'contradicts', 'Klein s.v. fasces: \'L. fascis, prob. cogn. with Mir. basc "neckband", W. baich "load, burden", OBrit. bascauda "rinsing bowl of brass", Maced. Gk. baskioi (pl.) "bundle of wood", OE baest "inner bark ')
('page-87.json', 'KLN:152', 'partial', 'Klein p.152 s.v. basket: \'ME., fr. L. bascauda ... cogn. with L. fascis, "bundle"; see fasces. The orig. meaning of bascauda was prob. "wicker basket"\' - a cognate, not the parent form Nourai draws.')
('page-87.json', 'KLN:576', 'supports', 'Klein s.v. Fascism (line 14412): \'Fascism, n. - It. fascismo, formed fr. fascia, "bundle; political group, organization", fr. L. [fascis]\'.')
('page-87.json', 'KLN:146', 'supports', 'Klein s.v. banner: \'ME. banere, fr. OF. baniere (F. banniere) ... Goth. bandwa, prob. derives fr. I.-E. base *bendh-, "to bind". See band, "tie"\' - Klein does support Nourai here, but he is the minori')
('page-88.json', 'KLN:1109', 'not_found', "Klein 1966 has no Avestan headwords; by the leaf/page mapping in refs_online.json (leaf ≈ p/2 + 12) p.1109 falls in the range 'Norman-ize … nuance' (KLN_1966.txt leaves 566-568), which has nothing to ")
('page-89.json', 'KLN:204', 'supports', 'KLN_1966.txt:5661-5725, between the page markers \'203\' (line 5703) and \'204\' (line 5727): "bring, tr. v. — ME. bringen, fr. OE. bringan, rel. to ... Goth. briggan, fr. Teut. base *bhrenk-"; "brother, ')
('page-89.json', 'KLN:203', 'supports', 'KLN_1966.txt:5661-5725, between the page markers \'203\' (line 5703) and \'204\' (line 5727): "bring, tr. v. — ME. bringen, fr. OE. bringan, rel. to ... Goth. briggan, fr. Teut. base *bhrenk-"; "brother, ')
('page-90.json', 'KLN:182', 'supports', 'KLN_1966.txt leaf 107, which carries the printed numerals 182/183, s.v. \'board, n., table, plank\': \'… fr. I.-E. *bhr̥tóm, resp. *bhr̥etóm, fr. base *bherd-, "to cut", a -d-enlargement of base *bher-, ')
('page-90.json', 'KLN:158', 'supports', "KLN_1966.txt leaf 94 (printed numeral 157 on the leaf, so pp.157-158), s.v. 'beaver, n., a rodent of the genus Castor': '… and cogn. with L. fiber, OSlav. bebrŭ, Lith. bebrus …, W. befer, Bret. bieuzr")
('page-90.json', 'KLN:158', 'supports', 'KLN_1966.txt leaf 94 (printed 157, so pp.157-158): \'bear, n., the animal. — ME. bere, fr. OE. bera, rel. to MDu. bere, Du. beer, OHG. bero, MHG. ber, G. Bär, ON. bjǫrn, lit. "the brown animal", fr. I.')
('page-92.json', 'KLN:188', 'supports', "KLN_1966.txt line 5381 (page marker '188' at line 5389), s.v. borough: 'These words prob. derive fr. I.-E. base *bhergh-, „high“, whence also Arm. berj „high place“ ... Hitt. parkush „high“, OI. bṛhán")
('page-92.json', 'KLN:148', 'partial', "KLN_1966.txt: printed p.148 (page marker at line 4444) is the 'barbican' page; Klein there says the first element of Pers. bāla-khāna 'is rel. to Avestic bərəzant-, OI. bṛhant- „high“; see borough' — ")
('page-92.json', 'KLN:148', 'supports', "KLN_1966.txt line 4441 (printed p.147-148), s.v. barbican: 'Pers. bāla-khāna, „upper chamber, balcony on the top of a house“, lit. „a high house“, fr. bala, „high“, and khāna, „house“. The first eleme")
('page-92.json', 'KLN:148', 'partial', "KLN_1966.txt line 4441 (printed p.147-148): 'barbican, n., outer defense of a city or castle. — ME. barbecan, fr. OF. barbacan, barbican (F. barbacane), which prob. derives ult. fr. Pers. bāla-khāna, ")
('page-93.json', 'KLN:194', 'supports', 'Klein 1966, leaf carrying pp.193-194 (KLN_1966.txt line 5510) s.v. \'Brahma, Brahman\': \'OI. brahman- (neut.), "prayer, the universal soul, the Absolute" ... of uncertain origin; possibly related to OI.')
('page-93.json', 'KLN:194', 'supports', 'Klein s.v. Brahma/Brahman (leaf pp.193-194): \'Brahma, Brahman, n., 1) the impersonal world soul ... — OI. brahman- (neut.) ... Brahman (masc.), "the chief god of Hindu religion"\'; and \'Brahman, n., a ')
('page-93.json', 'KLN:614', 'supports', 'Klein s.v. fort (KLN_1966.txt line 15222, on the leaf carrying pp.613-614): \'fort, n. — F. fort, "stronghold, fort", from the adjective fort, "strong", fr. L. fortis, "strong", which is rel. to OL. fo')
('page-96.json', 'KLN:1561', 'partial', "Klein's syphilis entry says exactly what Nourai's caption says ('ModL., from the title of the work by Girolamo Fracastoro … published at Verona in 1530; so named after the hero Syphilus, a shepherd'),")
('page-98.json', 'KLN:189', 'supports', 'Klein, CEDEL s.v. bottom (KLN_1966.txt line 5416): «bottom, n. — ME. botme, botome, fr. OE. botm, ‚lowest part, depth, bottom‘, rel. to OS. bodom, ON. botn … and cogn. with OI. budhnah, Gk. [πυθμήν] ‚')
('page-99.json', 'KLN:1190', 'supports', 'Klein 1966 p. 1190 (leaf 636, page marker \'1190\' on the same leaf): "pistachio, n. — It. pistacchio (whence also F. pistache, Sp. pistacho), fr. L. pistacium, fr. Gk. πιστάκιον, \'pistachio nut\', fr. π')
('page-99.json', 'KLN:1190', 'supports', 'Klein p. 1190: "pistachio, n. — It. pistacchio (whence also F. pistache, Sp. pistacho), fr. L. pistacium" — Latin > Italian, and Italian as the radiating centre, precisely as drawn.')
('page-99.json', 'KLN:44', 'supports', 'Klein 1966 p. 44 (page marker \'44\' immediately after the entry, KLN_1966.txt line 2099), s.v. albacore: "…rel. to bikr, \'virgin, woman having first child\', from the stem of the verb bákara, \'he rose e')
('page-99.json', 'KLN:44', 'supports', 'Klein p. 44: "fr. al-, \'the\', and the collective noun bakr, \'young camels\', whence bákrah, \'young she-camel\', rel. to bikr, \'virgin, woman having first child\', from the stem of the verb bákara" — both')
('page-99.json', 'KLN:44', 'supports', 'Klein p. 44: "albacore, n., a species of tunny (zool.) — Sp. albacora, fr. Arab. albakrah, \'the young camel\', fr. al-, \'the\', and the collective noun bakr, \'young camels\'…" — Spanish, and \'the young c')
('page-99.json', 'KLN:44', 'supports', 'Klein p. 44 heads the entry "albacore, n., a species of tunny (zool.) — Sp. albacora…" — English from Spanish, as the chart draws.')
total 895
```


## [2026-09-14T02:32:12.772Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=33400 && NR<=33900 && /^[[:space:]]*[0-9]{2,4}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt | head -20; echo '--- arsenal region'; awk 'NR>=3300 && NR<=3700 && /^[[:space:]]*[0-9]{2,4}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt | head -20; echo '--- shamash region'; awk 'NR>=34700 && NR<=35000 && /^[[:space:]]*[0-9]{2,4}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt | head -20"
}
```


### [2026-09-14T02:32:13.908Z] TOOL RESULT

```
--- arsenal region
--- shamash region
```


## [2026-09-14T02:32:17.226Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '33625,33660p' KLN_1966.txt | cat -n | cut -c1-200"
}
```


### [2026-09-14T02:32:17.287Z] TOOL RESULT

```
     1	‘once’,  similis  (assimilated  fr.  *semilis),  ‘like’, semper,  ‘always’,  OSlav.  samit,  ‘himself’,  OSlav. sq,  ‘with’,  sq-sedu,  ‘neighbor’  (lit.  ‘he  who  si
     2	samekh,  samech,  n.,  name  of  the  15th  letter  of  the Hebrew  alphabet.  —  Heb.  sdmekh,  ‘support, fulcrum’,  fr.  samakh,  ‘he  leant,  supported’;  so called  in  allusion  
     3	Samian,  adj.,  pertaining  to  Samos.  —  Formed with  suff.  -an  fr.  L.  Samius,  fr.  Gk.  Sap. to?,  fr. Expo?,  ‘Samos',  name  of  an  island  in  the  Ae¬ gean  sea,  fr.  Old  Gk
     4	tum,  fr.  Gk.  e^xpivov,  prop.  neut.  of  the  adj. s^xpiTo?,  ‘woven  with  six  threads’,  which  is compounded  of  ‘six’,  and  pixo ?,  ‘thread’. See  hexa-  and  mitosis  a
     5	Sammy,  n.,  a  soldier  of  the  United  States  (slang).
     6	—  Fr.  Sammy,  dimin.  of  Sam,  fr.  Uncle  Sam, personification  of  the  U.S.
     7	Samnite,  n.,  a  member  of  the  ancient  people  in¬ habiting  Samnium  in  Italy.  —  L.  Samnites  (pi.), ‘the  Samnites’,  fr.  Samnium,  which  prob.  stands for  *Sabniom  and  
     8	Samoan,  adj.,  pertaining  to  Samoa;  n.,  an  inhabi¬ tant  of  Samoa.  —  Formed  with  suff.  -an  fr. Samoa,  name  of  a  group  of  islands  in  Polynesia. Derivative :  Samoan,  n.,
     9	Samoyed,  Samoyede,  n.  and  adj.,  name  of  a  Si¬ berian  people.  —  Russ.  Samoyed,  lit.  ‘self¬ eaters’,  used  in  the  sense  of  cannibals,  a  name given  them  by  the  Rus
    10	sampan,  n.,  a  light  Chinese  boat.  —  Fr.  Chin,  san pan,  ‘three  boards’.
    11	samphire,  n.,  1)  the  plant  Crithmum  maritimunv, 2)  the  glasswort.  —  Fr.  earlier  sampere,  sampire, fr.  F.  (herbe  de)  Saint  Pierre,  ‘St.  Peter’s  herb’. The  actual  F
    12	Derivatives:  sample,  tr.  and  intr.  v.,  sampl-er,  n., sampl-ing,  n.
    13	sampler,  n.,  needlework.  —  ME.,  fr.  OF.  essem- plaire  (F.  exemplaire),  fr.  exemple.  See  exemplar and  cp.  prec.  word.
    14	Sampson.  —  A  var.  of  Samson.
    15	samsara,  n.,  transmigration  of  souls  (Hinduism).
    16	—  OI.  samsarah,  lit.  ‘a  passing  through',  formed fr.  sam-,  ‘together",  and  Sarah,  ‘course’.  For  the first  element  see  same  and  cp.  words  there  re¬ ferred  to.  
    17	samskara,  n.,  ceremonial  purification  (Hinduism).
    18	—  OI.  sarpskdrah,  ‘preparation,  sacrament,
    19	consecration',  lit.  ‘a  making  together’,  formed fr.  sam-,  ‘together’,  and  kara-,  ‘making, maker’.  For  the  first  element  see  samsara.  The second  element  is  rel.  
    20	Samson,  Sampson,  1)  masc.  PN. ;  2)  in  the  Bible  a. judge  distinguished  for  his  enormous  strength. —  Late  L.,  fr.  Gk.  Sap.iJ>&w,  fr.  Heb.  ShimshJn, a  name  derived  fr. 
    21	samsonitc,  n.,  a  silver  manganese  sulfantimonite (mineral.)  —  Named  after  the  Samson  mine  in St.  Andreasberg,  Harz.  For  the  ending  see  subst. suff.  -ite.
    22	samson  post,  a  strong  pillar  in  a  ship.  —  Named after  Samson,  in  allusion  to  the  verse:  “Samson took  hold  of  the  two  middle  pillars  upon  which the  house  rested” 
    23	Samuel,  masc.  PN. ;  a  celebrated  judge  and  proph¬ et  (Bible).  —  Late  L.,  fr.  Gk.  Sau,ouY)X,  fr.  Heb. Shlmu'el,  lit.  ‘name  of  God’,  fr.  shem,  ‘name’, and  El,  
    24	sanable,  adj.,  curable  (rare).  —  L.  sanabilis,  ‘cur¬ able',  fr.  sanare,  ‘to  cure’,  fr.  sanus.  See  sane  and able.
    25	Derivatives:  sanabil-ity,  n.,  sanable-rtess,  n. sanative,  adj.,  curative.  —  ML.  sandtivus",  ‘tend¬ ing  to  cure’,  fr.  L.  sanatus,  pp.  of  sanare.  See prec.  word  and  -
    26	sanatorium,  n.  —  ModL.  sanatorium,  prop.  neut. of  the  L.  adj.  sanatorius,  used  as  a  noun.  See next  word.
    27	sanatory,  adj.,  curative,  tending  to  heal.  —  L. sanatorius,  fr.  sanatus,  pp.  of  sanare,  ‘to  cure, make  healthy’,  fr.  sanus.  See  sane  and  adj.  suff.
    28	-ory.
    29	sanbenito,  n.,  a  penitential  garment.  —  Sp.  sam- benito,  fr.  San  Benito,  ‘Saint  Benedict’;  so called  because  of  its  resemblance  to  the  Bene¬ dictine  scapular.
    30	sanctification,  n.  —  Late  L.  sanctificatio,  gen. -dnis,  fr.  sanctificdtus,  pp.  of  sanctificare.  See
    31	sanctify  and  -ation.
    32	sanctified,  adj.  —  Prop.  pp.  of  sanctify.  For  the ending  see  1st  suff.  -ed.
    33	Derivative:  sanctified-ly,  adv. sanctify,  tr.  v.  —  ME.  seintifien,  fr.  OF.  sainte- fier  (F.  sanctifier),  fr.  Late  L.  sdnctificare,  ‘to
    34	sanctimony
    35	iansKrit
    36	make  holy’,  fr.  L.  sdnctus ,  ‘holy’,  and  -ficdre,  fr. facere,  ‘to  make,  do’;  see  saint  and  -fy.  E. sanctify  was  influenced  in  form  by  Late  L. sanctificare.
```


## [2026-09-14T02:32:30.802Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nleaf=0\nres=[]\nfor line in open('KLN_1966.txt',encoding='utf-8',errors='replace'):\n    leaf+=line.count('\\f')\n    s=line.strip()\n    m=re.fullmatch(r'(\\d{2,4})',s)\n    if m:\n        res.append((leaf,int(m.group(1))))\nprint(len(res))\nfor r in res[:20]: print(r)\nprint('...')\nfor r in res if len(res)<40 else res[-20:]: print(r)\nEOF"
}
```


### [2026-09-14T02:32:32.022Z] TOOL RESULT

```
1114
(0, 1966)
(6, 37)
(17, 10)
(17, 11)
(18, 12)
(18, 13)
(19, 14)
(19, 15)
(20, 16)
(21, 18)
(21, 19)
(22, 20)
(23, 22)
(24, 23)
(24, 24)
(25, 25)
(25, 26)
(26, 27)
(26, 28)
(27, 29)
...
(870, 1642)
(870, 1643)
(871, 1644)
(871, 1043)
(872, 1040)
(872, 1647)
(878, 1657)
(880, 1661)
(880, 1662)
(883, 1666)
(887, 1675)
(888, 1676)
(889, 1679)
(890, 1680)
(892, 1003)
(895, 1691)
(896, 1692)
(898, 1694)
(898, 1695)
(899, 1696)
```


## [2026-09-14T02:32:37.026Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nleaf=0\nres=[]\nfor line in open('KLN_1966.txt',encoding='utf-8',errors='replace'):\n    leaf+=line.count('\\f')\n    s=line.strip()\n    m=re.fullmatch(r'(\\d{2,4})',s)\n    if m: res.append((leaf,int(m.group(1))))\ndef show(a,b):\n    print([r for r in res if a<=r[0]<=b])\nshow(55,80); show(720,750); show(750,775); show(690,710)\nEOF"
}
```


### [2026-09-14T02:32:38.251Z] TOOL RESULT

```
[(55, 82), (55, 83), (55, 84), (56, 85), (57, 86), (57, 87), (60, 92), (60, 93), (62, 96), (64, 100), (64, 101), (65, 102), (65, 103), (66, 104), (66, 105), (67, 106), (67, 107), (68, 108), (68, 109), (69, 110), (69, 111), (70, 112), (71, 113), (71, 114), (72, 115), (72, 116), (72, 117), (74, 120), (74, 121), (75, 122), (76, 123), (77, 124), (77, 125), (77, 126), (77, 127), (78, 128), (78, 129), (80, 130), (80, 131)]
[(720, 1354), (720, 1355), (721, 1356), (722, 1359), (723, 1360), (726, 1365), (729, 1373), (731, 1377), (732, 1378), (734, 1382), (739, 1391), (739, 1392), (744, 1401), (744, 1402), (745, 1405), (750, 1413)]
[(750, 1413), (752, 1416), (755, 1422), (756, 1424), (756, 1425), (757, 1426), (757, 1427), (758, 1428), (764, 1439), (764, 1440), (764, 1441), (765, 1442), (766, 1443), (766, 1445), (767, 1444), (767, 1446), (768, 1448), (769, 1449), (769, 1450), (769, 1451), (771, 1452), (771, 1453), (772, 1454), (772, 1455), (772, 1456)]
[(691, 1298), (692, 1300), (695, 1307), (696, 1309), (697, 1311), (699, 1312), (699, 1313), (700, 1314), (700, 1315), (701, 1316), (701, 1317), (702, 1318), (702, 1319), (703, 1320), (703, 1321), (704, 1322), (704, 1323), (705, 1324), (705, 1325), (705, 1326), (707, 1329), (708, 1001)]
```


## [2026-09-14T02:32:54.869Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== LAM'; grep -n -i 'darse\\|arsenal' LAM.txt | head -10; echo '=== DEV'; grep -n -i 'arsenal\\|darse' DEV.txt | head -6; echo '=== PHN'; grep -n -i 'arsenal\\|darse' PHN.txt | head -6; echo '=== LKT'; grep -n -i 'arsenal\\|darsena' LKT.txt | head -6; echo '=== SKT'; grep -n -i '^arsenal\\|arsenal' SKT.txt | head -4"
}
```


### [2026-09-14T02:32:54.974Z] TOOL RESULT

```
=== LAM
854:arzegaie, marfil, arsenal (?); ou 0/ : oliban, olinde,
1056:galanga, sébeste, abouquel (4), aumusse^ darse, etc.
1854:Arsenal. Esp : arsenal, cat. et Maj : darsanale. portug :
1859:arsenal maritime. Le r d'arsenal, selon M. Devic, est dû
1884:auteur semble donner à darsena la même étymologie qu^à atarazana. Ne
1885:serait-il pas plus natm'el de dériver darsena de s^u^l jb dâr sana^a ; com-
1886:me dans ce passage dlbn-Djobaii*: « la ville de Messine possède un arsenal,
1889:l'arsenal de Tunis spU^ jU (prol« K- 35).
3576:drasena. //; darsena;de iû^ jl^ ddr-^an'aj <m ScL^jl^
3578:que sur le littoral méditerranéen au lieu de darse on
=== DEV
65:Telle  quelle,  notre  tâche   était  suffisante;   et  le présent  volume,  nous  l'avouons  en  toute  humilité, n'a  pas  laissé  de  nous  coûter  un  long  et  persévérant travail.  Prenant  pour  base  les  publications  de  nos devanciers,  nous  y  avons  joint  les  résultats  de  nos recherches  personnelles  pendant  plusieurs  années. Aussi  trouvera-t-on  dans   ce  dictionnaire  plus   de cent  articles  sur  des  mots  dont  l'origine  orientale n'avait  jamais  été   établie  :  les   uns  peu  connus, comme  alizari,  auffe,  alquifoux,  bédégar,  ciiine,  ché- hule,  nizeré,  gamache,  orcanète,   etc.;   d'autres  plus généralement  usités,  tels  que  épinard,  estragon,  far- deau, gâche,  moise,  moire,  houle,  mortaise,  etc.  Nous avons  combattu  ou  confirmé,  à  l'aide  d'arguments nouveaux,  les  hypothèses  précédemment  émises  sur des  termes  comme  artichaut,  arsenal,  avanie,  avarie, caraque,    escarpin,    nuque,   siroc,    etc.   L'examen  de quelques  ouvrages  scientifiques  arabes,  dont  les  tra- ductions latines   étaient  fort  répandues  au  moyen âge,  mais  dont  le  texte  arabe  n'a  jamais  été  publié,
539:Arsenal.  Portug.  arsenal,  esp.  arsenal,  darsena ,  atara- zana,  atarasanal,  ital.  arzena,  arzenale,  darsena.  M.  Engel- niann  dérive  tous  ces  mots  en  bloc  de  l'arabe  iCcU-o  ^b dâr  sinaa,  maison  où  l'on  construit,  fabrique.  Il  convient de  les  séparer  en  trois  groupes  :  1"  atarazana  représente iCtLuoîl  ^b  dnr  as-sinaa,  avec  l'article  devant  sinaa.  Je suis  porté  à  croire  que  le  a  initial  de  atarazana  est  aussi !  l'article.  Assurément,  il  est  contraire  à  toutes  les  règles  de la  grammaire  arabe  de  préposer  l'article  à  un  substantif suivi  de  son  complément;  mais  dans  la  langue  populaire dâr  as-sinaa  avait  pu,  par  le  grand  usage,  arriver  à  former un  seul  mot  dont  on  ne  sentait  plus  la  composition,  ce qui  permettait  de  lui  donner  l'article  (comme  dans  :>;^Ui
542:al-maouard ,  l'eau  de  rose,  où  maouard  est  composé  de  mr7, eau,  et  ouard,  rose);  fi°  darsena  représente  dar  sitifl'a  sans aucun  article:  3°  enfin  arsenal  esi  simplement  le  moi slula précédé  de  l'article.  Je  me  range  ici  à  l'opinion  de  M.  De- iVémery,  qui  a  fait  remarquer  que  ii^LA^Îi  as-siniïa  se  dit fort  bien,  sans  le  mot  dâr,  d'un  arsenal  maritime  ^  J'ajou- terai que  Du  Gange  cite  un  mot  languedocien  arsina  qu'il explique  supellex  quœvis,  un  ustensile  quelconque.  Je  vois là  le  même  mot  as-sinaa,  employé  à  peu  près  comme  l'est aujourd'hui  notre  mot  confection  pour  telle  ou  telle  espèce de  vêtement  non  fait  sur  mesure.  Et  si  ma  conjecture  est exacte,  il  est  clair  que  le  mot  dâr  n'aurait  là  rien  à  faire. Le  r  ^arsenal,  arsina ,  est  probablement  du  à  la  pronon- ciation emphatique  du  ^>:?  5.
543:Atarazana  a  conservé  en  espagnol  le  sens  général  de fabrique.  Les  mots  congénères,  dans  les  diverses  langues. se  sont  fixés  au  sens  d'arsenal  maritime.  Cependant  on trouve,  dans  l'ancien  français,  arsanail,  rtapotheca  instru- mentorum  agriculturcÇ,  *^  dans  Du  Cange.
1195:Darse.  Esp.  et  ital.  darsena.  Pour  l'étymologie  de  dar- som,  voy.  Arsenal.
2793:Arsanail,  voy.  Arsenal.
=== PHN
1826:ARSENAL, s. m. composé, (a.)
1833:orientale du mot arsenal, que les étymologistes ne nous ex-
1838:(Leyde, 1861, in-8^), s'exprime ainsi, au mot Arsenal : « Dans
10249:Arsenal, s. m. composé. ( a. ) 44
=== LKT
1249:Auch  bind,  'ein  Hügel,  Erdwall  oder erhöhte  Batterie',  als  n.  pr.  in  Bengalen Namen  einer  militärischen  Niederlassung, 4V2  engl.  Meilen  nordwestlich  von  Cal- cutta,  die  70  Jahre  lang  (1783—1853) Hauptquartier  des  berühmten  Korps  der bengalischen  Artillerie  war.  Im  dortigen Arsenale  wurden  zuerst  mit  stumpfem Vorderende  versehene,  daher  stark  zer- reißende Geschosse  liergestellt,  die  man engl,  dum-dum,  dtsch.  Dimidumgeschosse nennt.    [Hobson-Jobson  330.
1290:[Aus  ar.  dar  'Haus',  sinä'a  'Betriebsam- keit, Handwerk,  Industrie']  'Fabrik',  be- sonders 'Waffenfabrik'  und  auch  schon ar.  'Schiffsbauhaus';  im  Türkischen  zu tershäne  korrumpiert,  als  wenn  es  von pers.  Jiänä  [s.  hier  Nr.  809]  käme.  Hier- aus it.  darsena,  siz.  tirzanä  'iniiei'es Hafenbecken',  arzanä,  arsenale,  terzana 'Zeughaus';  frz.  darse,  darsine  'kleiner Binnenhafen',  arsenal;  sp.  atarazana, atarazanal  'Schuppen',  arsenal;  pg. taracena,  tercena  'Schuppen',  arsenal; rum.  arsenal,  darsena.  Dtsch.  Arsenal, ndl.  arsenaal,  engl,  arsenal,  russ.  a?*- senal.  [Dozy  Oost  16/18.  DE  205/206. Eguilaz  304.  Gorjaiew  6.  Kluge  23. Devic  DEt  35/36.    ML  2474.
5962:arsenal  495  ■
6339:alphanette  582 alphinic  683 alquifoux  1227 aludel  2142 alvarde  242 amalgame  1378 aman  66 amhre  78 amhrette  762  b nmiral  69  a amire  afz.  69  a amuUte  866 amulette  866 anafin  1537 andouille  355 angrec  82 «wii  1568 <iw<t/f(;  20ö8 antimoine  918 arabe(sque)  89 «ra^  92 arcawne  867 archine  108 argali  96 argousin  2160 aWeie  100 ar»m  112 armadie  1343 armoise(ur)  1596 armo(i)sin  1596 «rra^e?  1708 arrofee  1725 arsenal  495 artichaut  833 ar^iei  95 assassin  839 assogue  2208 »thanor  2019 a^fcar  2075 a«a6a?  1971 ffM&^e  874 aubergine  161 «MCTtöe  afz.  1221 uufage  afz.  586.  777 auferrant  afz.  586 aw/fe  796 au^n  afz.  605 auforget  884 «M^r^  135
7013:arsenale  494
7040:I  damaschino  47 <> j  damasco  476 ]  damasto  476 I  damigiana  474 !  dammusu  siz.  480 I  c?a/ii<?  1305 I  darsena  495
=== SKT
985:M.  F.  srj,  trx.     A.S.  *«. -     rab.)   Span,  tfrima/. I.   arsenal ;    Iohj^ ;.-  jMj,  wliere  the  a- •     -ude.     Cf.  Itnl. .V.    —  ,\iab.  (/*ir  suu£ai, iction,  place  for  mfilfing •-  Amb    dtir,  a   house; tnde,  construction. .— GW,)    Late  L,  arsemmm. ic  ;  lit.  a  male  prin- ul  the  Ktrnii^c  lancy dlfTcretkl  Kxc9.~Gk, ;r,  A  male. Ard«nt.      * ■.  {vcs.  of  verb.  (E.)    See
23698:SfKUiisk  from  Arabic;  alguozll.  arsenal, bonito,  colaba^  ?,  caiaway  (carraway), cannine,  maravctli.  minaret,
```


## [2026-09-14T02:32:56.757Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== FVQ shams'; grep -n -i 'shams\\|šams' FVQ_pages.txt | head -6; echo '=== AFM sinaa'; grep -n 'صناع\\|الصناعة' AFM_pages.txt | head -5; echo '=== SYN swim'; grep -n -i 'nesos\\|island' SYN.txt | head -8"
}
```


### [2026-09-14T02:32:56.847Z] TOOL RESULT

```
=== FVQ shams
7624:A^^NH 'Abd Shams, etc. 2 It thus seems clear that the sense of
=== AFM sinaa
240:(الأستاذ) ܐܬܢ )ܪ الصناعة ورنسها ܠܚ 31 ܣܣ 4 سا <
937:يتكون مثل اليد في بعض الينابيع اكات 1:06 ملح الصناعة وهو مركب
2050:ܐܬܝܬܝ ܕ" وهو ادر 7 أوجود ٠‏ والصناعي ܘܚܝ 47 ܕܐܕ ܚܝ زهو سم
=== SYN swim
673:IsLaND MAINLAND SHORE
1100:. THE PHYSICAL WORLD IN ITS LARGER ASPECTS 29 1.25 ISLAND a j Gothis csc Lith. sala Grk. fies land Lett. sal NG de one Zi page ChSl. tok ostrovit
1105:‘ , NE island (isle uss. ostrov Rum. nel (ostrov) ae aon ( oe ae Nir. oiledn (inis) OHG sila Av. — dvaépa- W. ynys MHG tinsel Br. enez NHG  insel
1106:Words for ‘island’ reflect its relation to the water, as ‘floating’, ‘water-land’, ‘flowed around’, etc.
1110:3. Ir. inis (NIr. mostly in place names), Gael. innis, W. ynys, Br. enez, fr. a Celtic *inissi, this perh. (Strachan, quoted by Machain s.v. innis) fr. *eni- ae eee in’ (the water), fr. *sta- stand’, like other cpds. in -s{o- -sti- (Walde-P. 2.604). Pie Teoma agg sa rest Bidrag 120). y Marstrander, _ 4. ON ey, eyland, Dan. ¢, Sw. 6, OF %, gland, ME iland, NE island (with Spelling influenced by isle), Du. eiland also MHG oune ‘water, island’ (NHG
1116:Pol. wyspa (which has displaced the older ostréw except in place names) = Boh. vyspa ‘sandbank, small island’, fr. vy- ‘out’ and the root of ChSl. stipa, suti, iter. sypatt ‘pour, scatter’, hence some- thing ‘poured out, shaken out’. Cf. Pol., Russ. nasyp ‘bank of earth, dam’ fr. the same root. Miklosich 334. Briickner 639.
1121:Words for ‘mainland’, as contrasted with ‘island’, are mostly from the notion of ‘great’, ‘continuous’, or ‘firm’ land, being such adjectives combined with ‘land’ in phrases or compounds, or used substantively with ‘land’ understood. Some are simply words for ‘land’ or ‘dry land’ used par excellence for the ‘main- land’. Several, even of the former group, may also be used in the wider sense of ‘land’ vs. ‘sea’.
1123:1. Grk. fmepos, Dor. aepos, Lesh. Greppos, fr. *érep-tos, perh. : OE fer ‘shore’, NHG ufer, etc. Walde-P. 1.47. From the point of view of the islander, the use of ‘shore’ for ‘mainland’ would be natural enough. But the chronology of Greek usage makes it probable that this was not the course of development and that the meaning ‘shore’ of the Gmc. words, if they are cognate, is secondary (cf. 1.27). In Homer #repos means ‘land’ vs. ‘sea’, even applied to an island, though also ‘mainland’, as prevailingly later. (Hence “Hre:pos, the ‘mainland’ from Corcyra.) The word was also
```


## [2026-09-14T02:33:03.097Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nff=0\nfor i,line in enumerate(open('LAM.txt',encoding='utf-8',errors='replace'),1):\n    ff+=line.count('\\f')\n    if i in (1854,1884,3576):\n        print('line',i,'leaf',ff,'printed p.',ff-57)\nEOF\necho '--- LAM 1850-1895'; sed -n '1852,1892p' LAM.txt"
}
```


## [2026-09-14T02:33:03.716Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1100,1120p' SYN.txt | cut -c1-1200"
}
```


### [2026-09-14T02:33:04.183Z] TOOL RESULT

```
line 1854 leaf 84 printed p. 27
line 1884 leaf 85 printed p. 28
line 3576 leaf 152 printed p. 95
--- LAM 1850-1895
ar-roub' le quart. « Per V solidos parient arrobo de trigo ,
arrobo de ordio per XII solidos. » Texte de 1 102.
Arsenal. Esp : arsenal, cat. et Maj : darsanale. portug :
arcenal. ital: arzena, arzenale. De Monconys écrit
arsenac ; de ïpLo!) as-smd'a, construction, ouiJ^las-sa/z'a,
même sens. M. Defrémery a prouvé (i) que ces deux ex-
pressions se disent fort bien (sans le mot j\^dâr)^ d'un
arsenal maritime. Le r d'arsenal, selon M. Devic, est dû
probablement à la prononciation emphatique du ^jd s; ou
bien n'y aurait-il pas là une réminiscence de jb dâr, mai-
(1) Journal Asiatique. Avril 1867 p. 416 et 1869. Juin. 1869, note.28 ATHA
son, qui précédait habituellement Âe^îL^sina^a} (i) Peut-
être n'est-ce là qu'un des exemples, où l'article Jl al est
devenu ar (Voyez arquebuse). C'est aussi l'avis de
M. Defrémery (Journ. Asiat. T. XIII, 1869. p. 5 J7).
Âsscu^sins. Les maîtres de la science étymologique ont
décidé que ce mot dérive de ^Ll>. hachâchi, ou '^yjJL>-
hachîchî, dérivé de jLii^ hachîch, le hachich. Il est
étrange que dans toutes les formes du mot assassin les
deux ^J» ch aient disparu. En dérivant assassin de Hassan-
ben-Sabah, on évitait cette difficulté. Ajoutons qu'il est
assez rare de trouver chez les auteurs arabes le nom de
^Ll>. ou ^txl>. appliqué aux Bathéniens.
^ ^ ta
Athanor. Four des alchimistes, d% jy:i\ attannoâr , foyer,
réchaud, four portatif, et encore trou pratiqué dans le sol
. >
pour cuire le pain; tandis que ô} fourn^ {de furnus) est
un grand four en maçonnerie (2).
(1) M. de Eguilaz tire le mot espagnol atarazana de tu-Inîl at-tarsana,
ou to'UtWdi at-tarsakhâna. Mais les Arabes reconnaissent eux-mêmes que
ces mots sont pris de Titalien (Y. Bostani ,U^| Jm^/i s. y. u^)* Le même
auteur semble donner à darsena la même étymologie qu^à atarazana. Ne
serait-il pas plus natm'el de dériver darsena de s^u^l jb dâr sana^a ; com-
me dans ce passage dlbn-Djobaii*: « la ville de Messine possède un arsenal,
renfermant des vaisseaux dont le nombre est incalculable. » tj^ ^'^j
j^>JS' Ja^i^S U Jp Js%CJ^t cr^ *é^ p^ ji^* ^^ Khaldoun appelle de même
l'arsenal de Tunis spU^ jU (prol« K- 35).
(2) V. nos Synonymes Arabes N<* 917. Lejyj est d'un usage général en
Syrie, chez les gens de la campagne.AUGE 29
Aubère. Se dit d'un cheval dont le corps est couvert
```


### [2026-09-14T02:33:04.230Z] TOOL RESULT

```
. THE PHYSICAL WORLD IN ITS LARGER ASPECTS 29 1.25 ISLAND a j Gothis csc Lith. sala Grk. fies land Lett. sal NG de one Zi page ChSl. tok ostrovit
Lat.  isula
SCr. _ otok, ostrvo
} Sw. 6
ae tee OE 1g, tgland, éaland Boh. _ ostrov ae isla ME tland, vee ' = poe wyspa
‘ , NE island (isle uss. ostrov Rum. nel (ostrov) ae aon ( oe ae Nir. oiledn (inis) OHG sila Av. — dvaépa- W. ynys MHG tinsel Br. enez NHG  insel
Words for ‘island’ reflect its relation to the water, as ‘floating’, ‘water-land’, ‘flowed around’, etc.
1. Grk. vijoos, Dor. vaoos, prob. : vaxw ‘swim’, Lat. nare ‘swim’, Skt. snd- ‘bathe’, etc. Walde-P. 2.692. Brug- mann, Grd. 2.1.541. Solmsen, Beitrage 244.
2. Lat. msula (> Romance words, but Rum. insuld neolog.), etym. disputed, but perh. best taken as fem. of an adj. *en-salos ‘in the sea’ (like Grk. é-d1os) : salum ‘sea’ (or : sal, salis ‘salt’, but its use for ‘sea’ seems to be only poet.). Walde-P. 2.452. Walde-H. 1.707. The view that insula and Grk. vfjcos belong together, reflecting some Aegean word (Ernout-M. 491; Skok, Glotta 25.217 ff.), has no substantial support.
Rum. ostrov (formerly the usual word, but now displaced by insula, except lo- cally), fr. Slavic, ChSI. ostrovi, etc. (be- low, 6).
3. Ir. inis (NIr. mostly in place names), Gael. innis, W. ynys, Br. enez, fr. a Celtic *inissi, this perh. (Strachan, quoted by Machain s.v. innis) fr. *eni- ae eee in’ (the water), fr. *sta- stand’, like other cpds. in -s{o- -sti- (Walde-P. 2.604). Pie Teoma agg sa rest Bidrag 120). y Marstrander, _ 4. ON ey, eyland, Dan. ¢, Sw. 6, OF %, gland, ME iland, NE island (with Spelling influenced by isle), Du. eiland also MHG oune ‘water, island’ (NHG
aue ‘meadow’), fr. a fem. deriv. (in part + land) of the word seen in Goth. ahwa ‘river’, OE éa ‘water, river’, Lat. aqua ‘water’, etc. Walde-P. 1.34. Simi- larly OE éaland directly fr. éa.
ME, NE isle, fr. OF r. isle; OHG Zsila fr. Lat. trsula in its spoken form, MHG, NHG insel with restored n.
5. Lith., Lett. sala : Lith. salti ‘flow’, atsala ‘pool of stagnant water’, etc. Perh. for *apz-sala, like Lett. sawle for pasaule ‘world’ in certain phrases, and so ‘flowed around’ like ChSl. ostrovit. So Mihl.-Endz. 3.664.
6. ChSI. otoku (cf. Jagié, Entstehungs- gesch. 374), SCr. otok, fr. *obu-tokt, epd. of obi ‘around’ and the root of festz, teka, Lith. tektt ‘flow, run’, etc. Walde-P. - 1.715 ff. Miklosich 347 f.
ChSl. ostrovit, etc., general Slavic, fr. *obi-strovt, cpd. of ob% ‘around’ and the root of struja ‘stream’, Grk. pew ‘flow’, etc. Walde-P. 2.703. Miklosich 318. Briickner 385.
Pol. wyspa (which has displaced the older ostréw except in place names) = Boh. vyspa ‘sandbank, small island’, fr. vy- ‘out’ and the root of ChSl. stipa, suti, iter. sypatt ‘pour, scatter’, hence some- thing ‘poured out, shaken out’. Cf. Pol., Russ. nasyp ‘bank of earth, dam’ fr. the same root. Miklosich 334. Briickner 639.
7. Skt. dvtpa-, Av. dvaépa-, epd. of Skt. dvi- (Grk. &-, Lat. bi-), Av. dvaé- and the weak grade of Skt. ap- ‘water’, hence ‘having water on both sides’. Barth. 763.
. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
30 SELECTED INDO-EUROPEAN SYNONYMS 1.26 MAINLAND c Goth. aa Lith. sauszemis < = pee orepta ON meginland Lett. ctelzeme Lat. continéns Dan. fastland (CHE bi eae It. continente (terra fer- Sw. fastland SCr. _ kopno ma) OE 2o8s Boh. pevnina Fr. continent ME mayn land Pol. staly Iqd Sp. continente (tierra fir- NE mainland Russ. materik me) Du. vasteland Skt. (dvipa-) Rum. continent ORG... - Av. (karSvar-) Tr. tir MHG .... Nir. —- mdirthir, tir mor NHG  fesiland W. tir maur Br. douar braz
```


## [2026-09-14T02:33:14.502Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-14T02:33:14.560Z] TOOL RESULT

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


## [2026-09-14T02:33:15.030Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3570,3590p' LAM.txt"
}
```


### [2026-09-14T02:33:15.076Z] TOOL RESULT

```
prétend que le mot est d'origine persane. Heury traduit
dame-jeanne par Z\^^ (i) damangâna,
Dauek ou Daiik. Esp : danique. C'est la sixième par-
tie d'une drachme arabe, qui pèse douze carats. (Trévoux)
Transcription de JtlS dâniq.
Dajrse. Esp: et Cat: d'arsena* Cat: et Maj: drassana,
drasena. //; darsena;de iû^ jl^ ddr-^an'aj <m ScL^jl^
dâr-sanâ''a (2). Ce qui confirme cette dérivation , c'est
que sur le littoral méditerranéen au lieu de darse on
disait aussi darcinè et darsine.
Degré. Esp : adaraja, adraja. Esp. Cat. et Ptg : darga.
Les formes ibériques dérivent évidemment de S>-j3
daraga , degré , échelle , gradin , avec l'article 4>.j j!I ad-
daraga. Je préfère y voir aussi l'origine du français degré,
venu de a>-j^ , daraga, au moyen d'une métathèse, dont
t'esp : adraja nous offre un exemple assez approchant. L'a-
rabe ic^j^ daraga a d'ailleurs tous les sens du franc, degré.
Denab. C'est l'a du Cygne ; de ^i ^ da/za^, queue,
à cause de sa situation sur la queue de l'oiseau qui figure
(1) Qu'il signald comme vulgaire. Lenoaveaa dictionnaire français-
arabe par le P. Belot (en prépara tioix), ouvrage ti^ès complet, donne les
```


## [2026-09-14T02:33:22.642Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D9%86%D8%A7' \\\n 'https://en.wiktionary.org/wiki/%CE%BD%E1%BF%86%CF%83%CE%BF%CF%82' \\\n 'https://www.etymonline.com/word/arsenal' \\\n 'https://en.wiktionary.org/wiki/arsenal' \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B3' \\\n 'https://en.wiktionary.org/wiki/%D7%A9%D7%9E%D7%A9' ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 461 verification' ; done"
}
```


### [2026-09-14T02:33:33.392Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/549b88c51d468306.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/14ef457371a6e8c7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3731e550a460af94.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4e4b76dfeb2bb881.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1ddf8150f23ad1d7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2643629bedc9a062.txt
```


## [2026-09-14T02:33:35.976Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo '===== شنا'; grep -n -A25 -i 'Etymology' 549b88c51d468306.txt | head -60"
}
```


### [2026-09-14T02:33:36.178Z] TOOL RESULT

```
===== شنا
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Related terms 
75-
76- 1.4.2 
77- Descendants 
78-
79- 1.5 
80- References 
81-
82- Toggle the table of contents 
83-
84- شنا 
85-
86- 8 languages 
87-
88- فارسی 
89- Magyar 
90- 日本語 
--
163: Etymology
164- [ edit ] 
165-
166- Attested as Middle Persian [script needed] ( šnāz , “ swimming ” ) , from Proto-Indo-Iranian *snáHti , from Proto-Indo-European *(s)neh₂- ( “ to swim ” ) , compare Avestan 𐬯𐬥𐬁 ( snā ) and Sanskrit स्नान ( snāna , “ bathing ” ) .
167-
168- Pronunciation
169- [ edit ] 
170-
171- ( Classical Persian ) IPA ( key ) : /ʃi.ˈnaː/ 
172-
173- ( Dari, formal ) IPA ( key ) : [ʃɪ.nɑː] 
174-
175- ( Dari, formal ) IPA ( key ) : [ʃɪ.nɑː] 
176- ( Kabuli ) IPA ( key ) : [ʃɪ.nɑː] 
177-
178- ( Hazaragi ) IPA ( key ) : [ʃi.nɔː] 
179-
180- ( Iran, formal ) IPA ( key ) : [ʃe.nɒː] 
181-
182- ( Tajik, formal ) IPA ( key ) : [ʃi.nɔ] 
183-
184- Rhymes: -aː 
185-
186- Readings
187-
188- Classical reading ?
```


## [2026-09-14T02:33:36.557Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo '===== nesos'; sed -n '1,120p' 14ef457371a6e8c7.txt | grep -n -i -A12 'etymology' | head -50"
}
```


### [2026-09-14T02:33:36.621Z] TOOL RESULT

```
===== nesos
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Declension 
75-
76- 1.4.2 
77- Derived terms
```


## [2026-09-14T02:33:40.718Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; awk 'NR>120 && NR<260' 14ef457371a6e8c7.txt | grep -n -i -B2 -A14 'Etymology' | head -40"
}
```


### [2026-09-14T02:33:41.626Z] TOOL RESULT

```
62- νᾶσσος ( nâssos ) — Rhodian 
63-
64: Etymology
65- [ edit ] 
66-
67- Uncertain. Has traditionally been connected with νήχω ( nḗkhō , “ to swim ” ) from Proto-Indo-European *(s)neh₂- ( “ to flow, to swim ” ) . If its meaning “island” has developed from a more original meaning “headland, cape”, it may be, like Proto-Germanic *nasją ( “ foothill; headland, cape ” ) and Bulgarian нос ( nos , “ nose; cape, promontory ” ) , a derivation from Proto-Indo-European *néh₂s ( “ nose ” ) ; in more landsman environments, compare the developments of Minaean 𐩱𐩬𐩰 ( ʾnf , “ wall of a city ” )  from “nose” and Arabic جَزِيرَة ( jazīra , “ island ” )  apparently from “bridge”.
68-
69- However, in that case, the origin of -s- , which is not usually preserved in Greek, remains to be explained, possibly requiring a borrowing from another Indo-European  language (though Furnée suspects a Pre-Greek origin, and Beekes Aegean ). [ 1 ] 
70-
71- Pronunciation
72- [ edit ] 
73-
74- IPA ( key ) : /nɛ̂ː.sos/ → /ˈni.sos/ → /ˈni.sos/ 
75-
76- ( 5 th BCE Attic ) IPA ( key ) : /nɛ̂ː.sos/ 
77-
78- ( 1 st CE Egyptian ) IPA ( key ) : /ˈne̝.sos/
```


## [2026-09-14T02:33:43.019Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo '=== etymonline arsenal'; grep -n -i -A6 'arsenal (n' 3731e550a460af94.txt | head -30; echo '=== wikt arsenal'; grep -n -i -A8 'From Italian\\|Ottoman\\|dār aṣ' 4e4b76dfeb2bb881.txt | head -40"
}
```


### [2026-09-14T02:33:43.102Z] TOOL RESULT

```
=== etymonline arsenal
23: arsenal (n.) 
24-
25- c. 1500, "dockyard, dock with naval stores," from Italian arzenale , from Arabic dar as-sina'ah "workshop," literally "house of manufacture," from dar "house" + sina'ah "art, craft, skill," from sana'a "he made."
26-
27- The word was applied by the Venetians to a large wharf in their city, and English picked it up in this sense. The meaning "public place for making or storing weapons and ammunition" is from 1570s. The London football club (1886) was named for the Royal Arsenal , Woolwich, where the original players worked.
28- also from c. 1500 
29-
=== wikt arsenal
333: From Italian arsenale , from Arabic دَار الصِّنَاعَة ( dār aṣ-ṣināʕa , “ manufacturing shop ” ) , from دَار ( dār ) + صِنَاعَة ( ṣināʕa ) . [ 1 ] 
334-
335- Pronunciation
336- [ edit ] 
337-
338- ( Received Pronunciation ) IPA ( key ) : /ˈɑːsənəl/ , /ˈɑːsnəl/ 
339- Audio ( Southern England ) : ( file ) 
340-
341- ( General American , Canada ) IPA ( key ) : /ˈɑɹsənəl/ , /ˈɑɹsnəl/ 
--
454: Ottoman Turkish: سلاحخانه ( silâhhâne ) 
455-
456- Ukrainian: арсена́л   (uk)   m ( arsenál ) 
457-
458- Vietnamese: kho vũ khí , kho đạn dược 
459-
460- stock of weapons
461-
462- Armenian: զինանոց   (hy) ( zinanocʻ ) 
--
594: From Dutch arsenaal , from French arsenal , from Arabic دَار الصِّنَاعَة ( dār aṣ-ṣināʕa , “ manufacturing shop ” ) ; دَار ( dār ) + صِنَاعَة ( ṣināʕa ) .
595-
596- Pronunciation
597- [ edit ] 
598-
599- IPA ( key ) : [arsəˈnal] 
600-
601- Hyphenation: ar‧sê‧nal 
602-
--
785: From Arabic دَار الصِّنَاعَة ( dār aṣ-ṣināʕa , “ industry house, manufacturing shop ” ) (via Andalusian Arabic ), from دَار ( dār ) + صِنَاعَة ( ṣināʕa ) . Compare dársena and atarazana .
786-
787- Pronunciation
788- [ edit ] 
789-
790- IPA ( key ) : /aɾseˈnal/ [aɾ.seˈnal] 
791-
792- Rhymes: -al 
793-
--
```


## [2026-09-14T02:33:52.296Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo '=== Arabic شمس'; grep -n -i -A6 'Etymology 1\\|Inherited from Proto-Semitic\\|Proto-Semitic' 1ddf8150f23ad1d7.txt | head -40; echo; echo '=== Hebrew שמש'; grep -n -i -A6 'Proto-Semitic\\|Etymology' 2643629bedc9a062.txt | head -40"
}
```


### [2026-09-14T02:33:52.369Z] TOOL RESULT

```
=== Arabic شمس
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
--
186: Etymology 1 
187-
188- 6.1.1 
189- Pronunciation 
190-
191- 6.1.2 
192- Noun 
--
335: Etymology 1
336- [ edit ] 
337-
338: Inherited from Proto-Semitic *śamš- .
339-
340- Pronunciation
341- [ edit ] 
342-
343- IPA ( key ) : /ʃams/ 
344-
--
1973: Proto-Semitic *śamš- 
1974- Arabic شَمْس ( šams ) bor. 
1975- Ottoman Turkish شمس 
1976-
1977: Borrowed from Arabic شَمْس ( šams ) , from Proto-Semitic *śamš- .
1978-
1979- Noun
1980- [ edit ] 
1981-
1982- شمس • ( şems ) 
1983-
--
2072: Etymology 1

=== Hebrew שמש
70: Etymology 1 
71-
72- 2.1.1 
73- Pronunciation 
74-
75- 2.1.2 
76- Noun 
--
91: Etymology 2 
92-
93- 2.2.1 
94- Noun 
95-
96- 2.2.1.1 
97- Descendants 
--
106: Etymology 3 
107-
108- 2.3.1 
109- Verb 
110-
111- 3 
112- Yiddish 
--
219: Etymology 1
220- [ edit ] 
221-
222- השמש זורחת בשמיים 
223-
224- Root 
225-
--
230: From Proto-Semitic *śamš- .
231-
232- Pronunciation
233- [ edit ] 
234-
235- ( reconstructed Biblical ) IPA ( key ) : /ʃamʃ/ 
236-
--
```


## [2026-09-14T02:34:06.291Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%B9%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%A7%D8%B9%D8%A9' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D8%B4%D9%86%D8%A7%D9%86' \\\n 'https://www.etymonline.com/word/Polynesia' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sneh%E2%82%82-' \\\n 'https://en.wiktionary.org/wiki/Samson' ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 461 verification' ; done"
}
```


### [2026-09-14T02:34:15.017Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7a46d6a897a1a74b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3fd8005bcf5538f6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/97e8d7a64488fdfd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb77728bdede04e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/284f11b1531503e3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/91269c4b07827c1f.txt
```


## [2026-09-14T02:34:18.073Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 7a46d6a897a1a74b 3fd8005bcf5538f6 97e8d7a64488fdfd fb77728bdede04e0 284f11b1531503e3 91269c4b07827c1f; do echo \"########## $f\"; grep -n -i -A4 'Borrowed from\\|Inherited from\\|From Proto\\|From Ancient Greek\\|From Hebrew\\|From Latin\\|Reconstruction' $f | head -30; done"
}
```


### [2026-09-14T02:34:19.058Z] TOOL RESULT

```
########## 7a46d6a897a1a74b
ugrep: warning: 7a46d6a897a1a74b: No such file or directory
########## 3fd8005bcf5538f6
ugrep: warning: 3fd8005bcf5538f6: No such file or directory
########## 97e8d7a64488fdfd
ugrep: warning: 97e8d7a64488fdfd: No such file or directory
########## fb77728bdede04e0
ugrep: warning: fb77728bdede04e0: No such file or directory
########## 284f11b1531503e3
ugrep: warning: 284f11b1531503e3: No such file or directory
########## 91269c4b07827c1f
ugrep: warning: 91269c4b07827c1f: No such file or directory
```


## [2026-09-14T02:34:21.849Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 7a46d6a897a1a74b 3fd8005bcf5538f6 97e8d7a64488fdfd fb77728bdede04e0 284f11b1531503e3 91269c4b07827c1f; do echo \"########## $f\"; grep -n -i -A4 'Borrowed from\\|Inherited from\\|From Proto\\|From Ancient Greek\\|From Hebrew\\|From Latin' \"$f.txt\" | head -24; done"
}
```


### [2026-09-14T02:34:22.818Z] TOOL RESULT

```
########## 7a46d6a897a1a74b
246: Borrowed from Classical Persian صَنْعَت ( san'at ) , borrowed from Arabic صَنْعَة ( ṣanʕa ) .
247-
248- Noun
249- [ edit ] 
250-
--
725: Borrowed from Classical Persian صَنْعَت ( san'at ) , from Arabic صَنْعَة ( ṣanʕa , “ craft, trade, art ” ) ; compare Azerbaijani sənət , Bashkir сәнғәт ( sänğät ) , Kazakh санат ( sanat ) , Turkmen sungat , Uyghur سەنئەت ( sen'et ) and Uzbek sanʼat . 
726-
727- Pronunciation
728- [ edit ] 
729-
--
805: Borrowed from Arabic صَنْعَة ( ṣanʕa ) .
806-
807- Pronunciation
808- [ edit ] 
809-
--
898: Borrowed from Classical Persian صَنْعَت ( san'at ) , from Arabic صَنْعَة ( ṣanʕa ) .
899-
900- Pronunciation
901- [ edit ] 
902-
--
########## 3fd8005bcf5538f6
########## 97e8d7a64488fdfd
174: A saponin -containing “washing-herb”, a derivative of the root Proto-Iranian *snaH- ( “ to wash, swim ” ) , from Proto-Indo-European *(s)neh₂- ( “ to swim ” ) . Borrowed from Middle Iranian also into Old Armenian աւշնան ( awšnan ) and Arabic أُشْنَان ( ʔušnān ) . The preverb participating in the derivation is disputed. Old Armenian աւշնան ( awšnan ) points to *Habí- , whereas the Persian itself is more easily explainable from *uc- .
175-
176- Related to  Persian اشنه ( ošne , “ moss ” ) , which is reflected as Classical Syriac ܫܢܬܐ ( šanṯā , “ moss, lichen ” ) and Arabic أُشْنَة ( ʔušna , “ moss, lichen ” ) . شنان ( šenân ) supposedly means “ horehound ” as does  شنار ( šenâr ) . Note Arabic شَنَان ( šanān , “ raft ” ) and شَنّ ( šann ) , شَنّة ( šanna , “ water-skin; dried herb ” ) .
177-
178- Pronunciation
--
263: Persian terms derived from Proto-Iranian 
264: Persian terms derived from Proto-Indo-European 
265- Persian terms derived from Middle Iranian languages 
266- Persian terms with IPA pronunciation 
267- Rhymes:Persian/aːn 
268- Rhymes:Persian/aːn/2 syllables 
########## fb77728bdede04e0
59: 1560s, "study and description of natural objects, natural philosophy" (a sense now obsolete), from French physiologie (16c.) or directly from Latin physiologia "natural science, study of nature," from Greek physiologia "natural science, inquiry into nature," from physios "nature"
60-
61- tradition 
62-
63: late 14c., "statement, belief, or practice handed down from generation to generation," especially "belief or practice based on Mosaic law," from Old French tradicion "transmission, presentation, handing over" (late 13c.) and directly from Latin traditionem (nominative traditio) "
64-
65- plumb 
66-
67- early 14c., "a mass of lead hung on a string to show the vertical line" (mid-14c. as "the metal lead"), from Old French *plombe, plomee "sounding lead," and directly from Late Latin *plumba, originally plural of Latin plumbum "lead (the metal), lead ball; pipe; pencil," a word of
--
87: early 15c., "arranged in sequence, continuous" (a sense now obsolete); mid-15c., of persons, "expressing earnest purpose or thought, resolute," from Old French serios "grave, earnest" (14c., Modern French sérieux) and directly from Late Latin seriosus, from Latin serius "weighty,
88-
89- discrimination 
90-
91- 1640s, "the making of distinctions, act of observing or marking a difference," from Late Latin discriminationem (nominative discriminatio), noun of action from past-participle stem of discriminare "to divide, separate" (see discriminate (v.)). Sense of "making invidious distincti
########## 284f11b1531503e3
########## 91269c4b07827c1f
258: From Middle English Sampson , Sampsoun , Samson , from Latin Samson , from Ancient Greek Σαμψών ( Sampsṓn ) , from Hebrew שִׁמְשׁוֹן .
259-
260- Pronunciation
261- [ edit ] 
262-
--
279: A male given name from Hebrew .
280-
281- An English surname derived from the given name, or from Samuel + son .
282-
283- Alternative forms
--
516: Borrowed from Ancient Greek Σαμψών ( Sampsṓn ) , from Biblical Hebrew שִׁמְשׁוֹן ( Shimshon ) .
517-
518- Pronunciation
519- [ edit ] 
520-
--
609: Borrowed from Spanish Samson , from Literary Hokkien 三 孫  / 三 孙 ( sam-sun ) .
610-
611- Pronunciation
612- [ edit ] 
613-
--
```


## [2026-09-14T02:34:43.591Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo '=== sanat persian section'; grep -n -i -B3 -A6 'ṣanʕa\\|صَنْعَة' 7a46d6a897a1a74b.txt | head -40; echo; echo '=== sinaa file head'; sed -n '150,230p' 3fd8005bcf5538f6.txt | head -60; echo; echo '=== sneh2 file'; wc -l 284f11b1531503e3.txt; sed -n '1,40p' 284f11b1531503e3.txt"
}
```


### [2026-09-14T02:34:43.683Z] TOOL RESULT

```
=== sanat persian section
243- Etymology
244- [ edit ] 
245-
246: Borrowed from Classical Persian صَنْعَت ( san'at ) , borrowed from Arabic صَنْعَة ( ṣanʕa ) .
247-
248- Noun
249- [ edit ] 
250-
251- صنعت • ( sanʿat ) 
252-
--
722- Etymology
723- [ edit ] 
724-
725: Borrowed from Classical Persian صَنْعَت ( san'at ) , from Arabic صَنْعَة ( ṣanʕa , “ craft, trade, art ” ) ; compare Azerbaijani sənət , Bashkir сәнғәт ( sänğät ) , Kazakh санат ( sanat ) , Turkmen sungat , Uyghur سەنئەت ( sen'et ) and Uzbek sanʼat . 
726-
727- Pronunciation
728- [ edit ] 
729-
730- IPA ( key ) : [sɒˈnɒt] 
731-
--
802- Etymology
803- [ edit ] 
804-
805: Borrowed from Arabic صَنْعَة ( ṣanʕa ) .
806-
807- Pronunciation
808- [ edit ] 
809-
810- ( Classical Persian ) IPA ( key ) : /san.ˈʔat/ 
811-
--
895- Etymology
896- [ edit ] 
897-
898: Borrowed from Classical Persian صَنْعَت ( san'at ) , from Arabic صَنْعَة ( ṣanʕa ) .
899-
900- Pronunciation
901- [ edit ] 

=== sinaa file head
 ص ن ع ( ṣ n ʕ ) 

 16 terms 

 Etymology
 [ edit ] 

 Verbal noun of صَنَعَ ( ṣanaʕa , “ to make , manufacture ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /sˤi.naː.ʕa/ 

 Noun
 [ edit ] 

 صِنَاعَة • ( ṣināʕa )  f ( plural صِنَاعَات ( ṣināʕāt ) or صَنَائِع ( ṣanāʔiʕ ) ) 

 verbal noun of صَنَعَ ( ṣanaʕa )   ( form I ) 

 art , skill 

 occupation , profession 

 handicraft 

 trade , craft 

 manufacture 

 industry 

 Declension
 [ edit ] 

 Declension of noun صِنَاعَة ( ṣināʕa )

 singular

 singular triptote in ـَة ( -a ) 

 indefinite

 definite

 construct

 informal

 صِنَاعَة 
 ṣināʕa 

 الصِّنَاعَة 
 aṣ-ṣināʕa 

 صِنَاعَة 
 ṣināʕat 

 nominative

=== sneh2 file
5 284f11b1531503e3.txt
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sneh%E2%82%82-
FETCHED: 2026-09-14T02:34:12Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T02:34:53.628Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== CHEUNG snaH'; grep -n -i 'snaH\\|\\*snā\\|snāy' CHEUNG.txt | head -15; echo '=== PHD'; grep -n -i 'šnā\\|snʾc\\|šnāz\\|šnās' PHD.txt PHD_mackenzie.txt | head -15; echo '=== NYB'; grep -n -i 'šnā\\|snāy' NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T02:34:53.745Z] TOOL RESULT

```
=== CHEUNG snaH
22744:348 *snaH 
22760:*snaH ‘to wash, swim’ 
22858:*MIDDLE PERSIAN: BMP sn’h /snah/ ‘blow, strike, violence’ 
23531:eresnahe/eresn-, ? Fariz. -häräsin-hräsin-, Bakht. fisnädan, Yar. -rasna/-rasn-, Natan. 
24976:*NWIR: NP tisnah, Kurd. (Sul.) tinu, (Sina) tinig ‘thirsty, parched with thirst’, Bal. 
27423:*NWIR: NP gusnah, Bal. gusnag (< NP), Gz. vässe, vesse, visse, Jow. vefa ‘hungry’, 
35534:sn’h /snah/, 349 
41062:gusnah, 423 
41619:tisnah, 383 
43516:eresnahe/eresn-, 360 
58109:*snaH 
58372:*Hrau, *naij, *snaH, *tap, 
=== PHD
PHD.txt:122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
PHD.txt:135:šnāxtan ... read M... šn's-.
PHD.txt:221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:585:šimšār Lë"! | N ~] box tree. Sir [HLBA < A hlb’; $1 | M šyyr, N ~] milk. šīrēn [5/yn! | M syryn, N ~in] sweet. ~ih: sweetness. SiSag [$y$k! | N fifa) bottle, flask. škaft [Ар] = Skeft. škāftan, škāf- [sk’p-tn' | M ‘kk’ pt, N fikáftan] split, burst. Skarag [skik! | P *škr-] (bird) of prey. škarwīdan, škarw- [fklw-ytn' | M ‘fkrw-st, N fikarfidan] stumble, stagger. škastan, Sken(n)- [TBLWN-tn' < A N tbr; škstn!, škyn- | M ‘tkn-, N stkastan, fikan-] break. ^ i$n: breaking. škēbāģ [fkyp?k! | P kyb-, N #hëba] patient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] be broken. Skóf-, у. Skuftan. Skdfag [fRwpk! | N šukēfa] flower, blossom. Skoft [škwpt'] = škeft. 1$kóh [ол | M Ай] poor. --īh: poverty. *§k6h [kwh | N sukdh] dignity, majesty; fear. škuftan, &ЕбЇ- [škwp-tn! | N fukuftan] flower, blossom. Énàs-, v. Snaxtan. šnàsag [fn'sk! | P *$n*sg] knowing, knower; sense. ~ih: knowledge. šnāxtan, $nàs- [fm htn!, fie | M хіп, Чи s-, N fin-] know, recog- nize. šnāyēnīdan, šnāyēn- [sz dyn-ytn'] please, propitiate. ~išn: happiness. šnāyīdan, šnāy- [fr'd-ytn!] praise, propitiate. --i$n : praise, gratitude. šnāz [frc | (N šinā(w))] swimming. šnāzīdan, šnāz- [fr'c-ytn! | M $2? 2-, (IN šināw-)] swim. $nóhr [snwhl | М *fnwhr] gratitude, contentment. šnūmaģ [fnwmk! | M *fnwm-] satisfaction, contentment. &nó&ag [šnwšk! | N šunoša] sneeze. $nüg [šnwk' | M *fnwg] knee. šnūman [fnwmn! = Av. xsniimaine] propitiation. 86n [swn'] kind, manner. ~ig [-yk!] customary, ordinary. šūy-, v. Sustan. Sdy [std | N ~] husband.
PHD.txt:705:abuse (n.) dušnām, wad-wāzag.
PHD.txt:2140:grateful burdešnēhr, huspās, spās- dār, spāsešnās, spāsūmand.
PHD.txt:2141:gratitude āzādīh, spas, spāsdārīh, šnāyišn, šnēhr.
PHD.txt:2200:happiness farroxīh, huramih, hun- sandih, hušnūdih, šādih, šnāyēn- išn, urwāzišn, xwa(h)rih.
PHD.txt:2538:know danistan, šnāxtan, uzwārdan,
PHD.txt:2539:knowing āgāh, dānāg, dānišnēmand, šnāsag.
PHD.txt:2540:knowledge āgāhīh, danagih, dānišn, frahang, šnāsagīh.
PHD.txt:2541:known āšnāg, azd.
PHD.txt:3118:physics čihr-šnāsīh.
=== NYB
744:āšnāk [’Sn’k] well-known 78?. — MPrs »šn'g "well versed in’ (A-H II); Paz. āšnā, Skr. v. prasiddha; as to the etymo- logy cf s. v. šnartan.
3336:radišn [Iwdšn'] 1. (living thing) which is to grow: 1. pl. cas. obl. ~-dn: harvisten zāyišnān u —-än all (living things) which are to be born and to grow 88°. — 2. abstr. ~ u vaxsisn i urvarän growth and increase of the plants 899-1°. — Paz. rēšn.
3483:spas [sp’s] 1. thanks, gratitude 127%. 7026. 90°, — 2. service: vasdn vazurg ~-dn (cas. obl. as a subj.) many men serving in high positions (bahuvrihi) 1061; v. also šnās. — MPrth 'sp's ‘service’, Arm. lw. spas id.; MPrs ‘sp’s ‘service’ (S), ’sp’s ‘thanks’ (A-H II); Paz. spas with the bizarre Skr. v. tridhä-praharaka ‘threefold watch’ based on a popular etymology (sé ‘three’ + pds, g. v.); NP sipäs 1. ‘grace, favour’, 2. ‘praise, thanksgiving’; from Av. (1614) spas- ‘to observe, to attend’. — V. an-ispäs.
3654:šnas [Sn’s] pres. st. of šnāxtan, in com- pounds: spās-šnāsān (pl. cas. obl.) those understanding service = having service as their profession 71!, v. späs.
3655:šnāsak knowing, learned 213. šnāsēh knowledge 7119.
3656:šnāxtan [šn'htn'] šnas-, Ist p. sg. šnāsom [Sn’swm] 5777, to understand, to know, to recognize 615; bē ~ 715, 907. 10018; 5722 + hakar ‘whether’. — Av. (559) xénà-, pres. ašnas- = OP (Skr. jää-); MPrthPrs *$n?xin “Snäs-; Paz. Snàxtan $näs-, NP Sinäxlan šinās-.
3659:šniyišn ([šn'dšn'] propitiation, praise, homage 361. - From Av. (559) xšnav- ‘to propitiate’; the BP vb. is commonly šnāyēnītan.
3815:tušn [twšn'] silent, quiet 41°. — Av. (657) tušni-, also in compounds: tušnā-mati-, tušni-šad (658).
5222:katäma-: katam katära- (katarascit): katarcihé Kavärasman-: Karazm kaväta-: kavät kavi-: kai kavi-: kayak kavi-(usan-): Käyös kay-: citan kohrp-: karp keresaspa-: Krišāsp kū (kuda): kū kutaka-: kötak xrafstra-: xrafstr xratu-: xrat xrvidru-: xurdruš ni-xšata-: šastan xša0ra-: šahr xSa0ra-vairya-: šahrēvar pati-xSay: pätixsäi xšinaka-: šmah xŠnā-: šnāxtan xšnav: Šnāyišn (ava/avi-) xšnav-: ošntitak xšusta-: šustan x$viwra-: "šif(a)rg xUaöna-ayah-: xYan-asén xUačpal0ya-: xVēš xVafna-: xYamn x"üirizam-: xVārizm xUanat.caxra: x"andan
5695:PÉn'g: āšnāk ’P)swb: asop "wg: lēvāc ?wrd: avurtan »wr-t: ävar »yng: àivénak ?z: Az
```


## [2026-09-14T02:34:55.454Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== ARY latin index shena'; grep -n -i 'SHENA\\|SNA\\|USHNAN\\|OSHNAN' incoming/ARY/ARY_latin_index_pages.txt | head -15; echo '=== FSD arsenal'; grep -n -i '^arsenal\\|arsenal,' FSD_vol1.txt | head -5"
}
```


### [2026-09-14T02:34:55.537Z] TOOL RESULT

```
=== ARY latin index shena
351:geen yb il5 prokesae lad 52 Snag OLS cal J ailgy ly j.pe (MUNDA tla yr
963:(hla obeys Wabi, 2% Ssnagge LE al ph iS ge wlth gy Dlel 9 gy) pl sl
1088:SNA 9 pa tt MET BU gp 92 9 Sh Sy Cool od SF shee bade slat gl ,
1119:I tl 5 shoes YEE iI bay eel ead cada ot y 9 lo ci(YASNA HAPTANHATI)
2331:‘BUCK: (SNAKE) 194-195 UODZE LATVIAN) (3) 9)
3499:eel frae y silat Ly ‘oy aa (SNEZAG, SNEXR) 5 slg, » SNAOTHA)) gly! staal 52 tos .
3502:BFS ilall (SNOW : pL S) SNAW 5545 Sil NIVIS, NIK ig) IPH sp, SSNEZA !
3503:Sag FISNAR 94S 5th! GNEO 54S J pS SNE 345 xd (SHINEE 1 JT) SNEO
3504:AS cess SNEGD 545 gsi GNIEGAS 5,5 x) SNECHTAE 345 5-1 | SNAIWS
3505:sgleag NEF pay, SNE 1 jbl SNO 6533,3 (SNO :.gat y (SNEEUW :.s.:la SNAYGIS
3939:(MACKENZIE: (SPRING) 134 VESNA
3940:BUCK: 1013-1016 WIOSNA, WIOSENNY :(POLISH) gl)
3942:rrr i gb dby ‘VESNA (BOHEMIAN) oa »
4264:TIF yO ebb ily PARSNA, PARSANA (HITTITE) =a
4325:FAIRSNA GOTHIC) Sif
=== FSD arsenal
12500:ISp.J  1.  A   warehouse.  2.  A   dockyard;  naval  arsenal, al-raa'cl-ga,  1   al-ma'sj-ga;  2   fil-ma'ci-gii,  n.  [P.  I.J  1.  A tree  of  the  genus  Dipterocarpus,  yielding  a   light,  ashy- colored  wood  and  a   valuable  gum.  2.  Its  wood  or  the gum  antang.
25013:[<  L.  armamenta,  <   armo:  see  arm1,  r.]  Syn- , ar"ma-men'ta-ry,  n.  An  armory  or  arsenal, "ma-men-ta'ri-um,  1   ar'me-men-te  mines,
25480:Shook  the  Arsenal,  and  fulmined  over  Greece.
```


## [2026-09-14T02:35:10.394Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://www.etymonline.com/word/polynesia' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)neh%E2%82%82-' \\\n 'https://en.wiktionary.org/wiki/Polynesia' ; do timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 461 verification'; done"
}
```


## [2026-09-14T02:35:14.227Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== IEC sna'; grep -n -i '^sna\\|snā-\\|snāiō\\|snātos' IEC.txt | head -10; echo '=== FSD arsenal n'; grep -n -i 'ar[”\"]se-nal\\|arsenal,  n' FSD_vol1.txt | head -5; echo '=== ARY pages شنا'; python3 -c \"\ntxt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(txt):\n    if 'شنا ' in p or 'اشنان' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        ls=[l.strip() for l in p.split('\\n') if 'شنا' in l][:3]\n        print(i, m.group(1) if m else '?', ' | '.join(l[:90] for l in ls))\n\" | head -10"
}
```


### [2026-09-14T02:35:14.981Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3c0b27110f2bf2fb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b59715e3b9c1144.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3f1baae4d5da50b8.txt
```


### [2026-09-14T02:35:16.144Z] TOOL RESULT

```
=== IEC sna
11509:(nàio ‘swim, float implied in Tokh. B nask- ‘bathe’ beside ambig. Lat. no, nare, pf. navi ‘swim’, but see snā- below; Alb. ambig. cf. not, m. (swimming, floating’ and notoj, v.: Lat. natàre, qua *nàt- or *snàt-)
16523:snadho, ið ‘cut’ Mir. snaidim, pp: snasta, v. id., W naddu, inf. id. (and ‘chip, trim"); OBr. cf. nedim, s. ‘chopper’; MHG snate, s E wf. ‘wound’; G Schnate, f. 'baulk, field-boundary' beside SWGer. Schnatte, f. ‘notch’
16524:snaàdh- (1) (snád-?) ‘flow, ease; flowing, easy’. Same as (2) (?). Var: snást- Av. snad-, v. ‘wash’; OCS snadi, adv. “slightly; easily (Cz: *perhaps"); OCz. snada, f. “ease, harmony’; W cf. (variant) naws, adj. ‘soft; OCS snasti, f. Cool lit. ‘facility’); Ukr. 'es- sential, quintessence’
16526:snago, ið ‘creep’; snagos, ön ‘creeping thing’. WP II, 697 Ir. snaighim, v. id.; snag, m. ‘snail; OHG snahhan, sv. ‘creep’; OE snaca, m. ‘snake’; (G Schnake, f. ‘ringed snake; snail; whim’ from *snēg-?, in view of MHG snāke, wmf. “a reptile’). (Isophones: Du. snakken, v. “lan- guish’; ON snaka, v. 'rummage'; Norw. snak- ke, v. ‘talk’; E dial. snake, p.t. snook, v. “steaP')
16533:snar- (snaró, snarrð. Onomat.) ‘talk, growl’ Lat. narrō, āre, v. ‘tell, relate’; MHG snarre, f. “one-stringed instrument’ beside snar, gs: snarres, sm. ‘growl’; G schnarren, v. ‘creak, buzz, whizz’; Schnarre, f. ‘rattle, variety of thrush’; MHG sneren, snerren, v. ‘twaddle’
16535:snātos, à (1), iə ‘twisted; twine, twist'. Cf. snaio (1). WP II, 692 Mir & Ir. snáth, m., snáithe, f. *thread'; OBr. cf. not-nid, s. ‘needle’; Br. noed, m. coll. ‘thread’; W noden, pl. -i, f. id.; Cor. nosjen, pl. -nnow, coll. næs, f. id.; OE snod, f. ‘snood’; Latv. snåte, f. ‘sheet’; R cf. also snastí, f. (rope, rigging’, but cf. snast- above). Cf. sneio, néio, etc.
16547:snaut- ‘puny, poor, trivial, bad" Arm. nawír, adj. ‘small, slender; MHG snoede, adj. (2) ‘paltry’; Ger. schnóde, id.; Du. snood, adj. Ceicked Cf. MHG snoede (1) “arrogant, ruthless’); ON snauór, adj. *be- reft, poor
=== FSD arsenal n
=== ARY pages شنا
39 40 مردم را به سرگذشت نیا کان و تاریخ خود آشنا می‌کرد بلکه وظایف آنها را یادآور شده و روحیه‌ی | اهمیت شناخت زبانهای هند باستان در شناخت زبانپای ایرانی
150 151 ۲ | پاشنه پاشنا (به چم
173 174 اسپانیایی (5۳۸۸//5[4): اناد اشنا چک (25804): 57
326 327 زان اشنا ان نموت انا سا انگلیسی گهن (8۸01/3/7 0ا0):
383 384 ایتالپایی (/(ال7): لا اد اشنا ندرا لیتوانی (۸ا هلاب 7لل):
```


## [2026-09-14T02:35:21.694Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '16536,16546p' IEC.txt"
}
```


### [2026-09-14T02:35:21.751Z] TOOL RESULT

```
snáàtos (2) ‘swimming; flow, float; (3) washed, clean’. Cf. snaio (3) and the variant nàió, nàt-. (W. Alb. Gk. ambig.) (2) cf. OBr. di-naut, s. ‘conduit’; W nawd, adv. ‘easily’; (ambig. also in) Alb. not, s. ‘swim- ming' and in Gk. nésos, f. “island” cf. nésos plotë, f. (“floating island”: epithet of Aeolus);
snáió — sneu-
15
20
25
30
35
40
45
1234
Doric násos, as Gk. (3) Av. cf. snà-, v. “wash? beside snad-, id.; snaorom, n. ‘washing’; Umb. snata, npl. (que- ried: ^washed, clean")
```


## [2026-09-14T02:35:24.693Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo '== etymonline polynesia'; grep -n -i -A4 'Polynesia' 3c0b27110f2bf2fb.txt | head -20; echo '== wikt (s)neh2'; grep -n -i -A10 'Root\\|Derived terms' 5b59715e3b9c1144.txt | head -30; echo '== wikt Polynesia'; grep -n -i -A4 'Etymology' 3f1baae4d5da50b8.txt | sed -n '1,30p'"
}
```


### [2026-09-14T02:35:24.794Z] TOOL RESULT

```
== etymonline polynesia
1:URL: https://www.etymonline.com/word/polynesia
2-FETCHED: 2026-09-14T02:35:11Z
3-STATUS: 200
4:TITLE: Polynesia - Etymology, Origin & Meaning
5-
6:Polynesia - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
--
21: Origin and history of Polynesia 
22-
23: Polynesia (n.) 
24-
25: 1758, Latinization of French polynésie , coined 1756 by French writer Charles de Brosses (1709-1777) in "Histoire des navigations aux terres australes, contenant ce que l'on sait des moeurs et des productions des contrées découvertes jusqu'à ce jour" (the word was first used in English in a review of it), coined from Greek polys "many" (from PIE root *pele- (1) "to fill") + nēsos "island" (see Chersonese ). Related: Polynesian .
26- also from 1758 
27-
28: Entries linking to Polynesia 
29-
== wikt (s)neh2
62: Root 
63-
64- 1.1.1 
65: Derived terms 
66-
67- 1.1.2 
68- Descendants 
69-
70- 1.2 
71- References 
72-
73- Toggle the table of contents 
74-
75- Reconstruction:Proto-Indo-European/ (s)neh₂- 
--
131: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
132-
133- Proto-Indo-European
134- [ edit ] 
135-
136: Root
137- [ edit ] 
138-
139- *(s)neh₂- ( imperfective ) [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] 
140-
141- to swim 
142-
143- to float 
144-
145: Derived terms
== wikt Polynesia
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
94: Etymology 
95-
96- 2.2 
97- Pronunciation 
98-
--
222: Etymology
223- [ edit ] 
224-
225- Borrowed from French Polynésie (coined by Charles de Brosses in 1756), from Ancient Greek πολύς ( polús , “ many ” ) + νῆσος ( nêsos , “ island ” ) . [ 1 ] According to Moon Handbooks Tahiti , de Brosses first used the term to refer to all Pacific islands. The present restricted use was established by J. S. C. Dumont d'Urville in 1832. [ 2 ] 
226-
--
439: ^ Douglas Harper ( 2001–2026 ), “ Polynesia ”, in Online Etymology Dictionary , retrieved 21 January 2020 . 
440-
441- ^ Geoffery Clark (September 2003 ), “Dumont d'Urville's Oceania”, in The Journal of Pacific History ‎ [1] , volume 38 , number 2, Taylor & Francis, pages 155-161 
442-
443- Finnish
--
446: Etymology
447- [ edit ] 
448-
449- From French Polynésie .
450-
```


## [2026-09-14T02:35:37.043Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://www.etymonline.com/word/Indonesia' \\\n 'https://abadis.ir/fatofa/%D8%B4%D9%85%D8%B3/' \\\n 'https://abadis.ir/fatofa/%D8%B5%D9%86%D8%B9%D8%AA/' \\\n 'https://abadis.ir/fatofa/%D8%B4%D9%86%D8%A7/' ; do timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 461 verification'; done"
}
```


### [2026-09-14T02:35:43.170Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/29f5f1b2efb62574.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d04052edbe8af55d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/df2d832abde0516c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a71194cd0adf12ac.txt
```


## [2026-09-14T02:35:46.274Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo '== Indonesia'; grep -n -i -A3 'Indonesia (n' 29f5f1b2efb62574.txt | head -12; echo; for f in d04052edbe8af55d df2d832abde0516c a71194cd0adf12ac; do echo \"== $f\"; grep -n -A6 'فرهنگ معین\\|معین' $f.txt | head -25; done"
}
```


### [2026-09-14T02:35:47.348Z] TOOL RESULT

```
== Indonesia

== d04052edbe8af55d
49: فرهنگ معین
50-
51- (شَ ) [ ع . ] (اِ. ) آفتاب ، خورشید. 
52-
53- فرهنگ عمید
54-
55- ۱. آفتاب، خورشید.
--
245: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
246-
247- لینک ها 
248-
249- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
250-
251- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
== df2d832abde0516c
49: فرهنگ معین
50-
51- (صَ عَ ) [ ع . صنعة ] (اِ. ) ۱ - فن ، پیشه . ۲ - حیله ، چاره . 
52-
53- فرهنگ عمید
54-
55- ۱. (اقتصاد ) عملکرد هریک از مراکز تولیدی اعم از کارخانه ها و کارگاه ها: صنعت داروسازی.
--
433: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
434-
435- لینک ها 
436-
437- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
438-
439- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
== a71194cd0adf12ac
20: شنا. [ ش ِ ] ( اِ ) شناوری و آب ورزی باشد. ( برهان ). حرکت انسان یا جانور بر روی آب بوسیله تحرک بازوان و پاها. سباحت. ( فرهنگ فارسی معین ). دست و بغل در تداول شوشتر. شناوری و دست وپا زدن در آب و با لفظ کردن مستعمل و بمعنی شناور وشناگر مجاز است. ( آنندراج ). شناه. شناب. یعنی شناوری و بر این قیاس شناگر و شنابر و شناور : 
21-گرد گرداب مگرد ارت نیاموخت شنا 
22-که شوی غرقه چو ناگاهی ناغوش خوری. لبیبی.
23-همه الغریق الغریق است بانگم 
24-که من غرقه ام در شنا میگریزم. خاقانی.
25-رجوع به شناب ، شناو، شناه و شنوشود. || قسمی از اعمال ورزش در گود. ( یادداشت مؤلف ). برسم پهلوانان باستانی شنا رفتن در زورخانه. هر دو دست را بر زمین یا بر تخته شنا تکیه دادن و پاها را به عقب کشیدن و بدن را بر دو دست فرودآوردن و بربردن است بی اصطکاک با زمین تا بازوان نیروگیرد. نام ورزشی است که هندیان آن را دند گویند و آن را شنو نیز نامند. ( غیاث اللغات ) ( آنندراج ) : 
26-بیم طوفان بلا در خشکیم بیش از تری 
--
40: فرهنگ معین
41-
42- (ش ) (اِ. ) حرکت انسان یا جانور در زیر یا روی آب با کمک حرکات منظم وهمآهنگ دست و پا که انواع مختلف دارد. ، ~ی کرال معمول ترین و سریع ترین نوع شنا در آب که در آن دست ها هر بار که از آب بیرون می آیند از کنار گوش داخل آب می شوند و همزمان با آن پاها به صورت 
43-
44- فرهنگ عمید
45-
46- رفتن مسافتی در آب با حرکت دادن دست ها و پاها. 
--
140: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
141-
142- لینک ها 
143-
144- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
145-
146- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-14T02:35:56.628Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '1,10p' 29f5f1b2efb62574.txt; echo ---; cd /home/sfmqrb/git/rishe; timeout 120 python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Indonesia' --note 'page 461 verification, Indonesia < nesos'"
}
```


### [2026-09-14T02:36:00.740Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/Indonesia
FETCHED: 2026-09-14T02:35:38Z
STATUS: 200
TITLE: Indonesia - Etymology, Origin & Meaning

Indonesia - Etymology, Origin & Meaning 

 Search 
 Log in 

---
/home/sfmqrb/git/rishe/data/verification/sources/web/4b892e5ead880732.txt
```


## [2026-09-14T02:36:03.521Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i -A3 'Indonesia (n\\.)' 29f5f1b2efb62574.txt | head; echo '---wikt'; grep -n -i -A4 'nêsos\\|Greek.*island\\|Etymology' 4b892e5ead880732.txt | sed -n '1,40p'"
}
```


### [2026-09-14T02:36:03.596Z] TOOL RESULT

```
---wikt
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
141: Etymology 
142-
143- 6.2 
144- Proper noun 
145-
--
152: Etymology 
153-
154- 7.2 
155- Pronunciation 
156-
--
183: Etymology 
184-
185- 9.2 
186- Pronunciation 
187-
--
206: Etymology 
207-
208- 10.2 
209- Pronunciation 
210-
--
252: Etymology 
253-
254- 12.2 
255- Pronunciation 
256-
--
269: Etymology 
270-
271- 13.2 
272- Pronunciation
```


## [2026-09-14T02:36:06.339Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n 'Indus\\|νῆσος\\|nêsos\\|Earl\\|Logan' 4b892e5ead880732.txt | head -10; echo '--- etymonline body'; sed -n '18,40p' 29f5f1b2efb62574.txt"
}
```


### [2026-09-14T02:36:06.404Z] TOOL RESULT

```
498: (late nineteenth century) Attested circa 1850, [ 1 ] composed of Ancient Greek Ἰνδός ( Indós , “ Indian ” ) +‎ Ancient Greek νῆσος ( nêsos , “ island ” ) ; initially, in competition with Insulinde , of the same meaning, lexically constructed on a Latin basis, or in reference to the East Indies archipelago.
851: ^ J. R. Logan ( 1850 ), “The Ethnology of the Indian Archipelago: embracing enquiries into the Continental relations of the Indo-Pacific Islanders”, in J. R. Logan, editor, The Journal of the Indian Archipelago and Eastern Asia , volume 4, Singapore, pages 254, 2nd footnote : For reasons which will be obvious on reading a subsequent note, I prefer the purely geographical term Indonesia , which is merely a shorter synonym for the Indian Islands or the Indian Archipelago. We thus get Indonesian for Indian Archipelagian or Archipelagic, and Indonesians for Indian Archipelagians or Indian Islanders. I have no affection for the multiplication of semi-grecian words, and would gladly see all the nesias wiped off the map if good Saxon equivalents could be substituted. 
1802: From Dutch Indonesië , from Ancient Greek Ἰνδός ( Indós , “ Indus, India ” ) + νησιά ( nēsiá , “ islands ” ) . Spelling influenced by either English Indonesia or matching the pronunciation spelling .
1986: Latin Indus 
1999: From Indus + nēsus + -ia .
2164: Composed of Ancient Greek Ἰνδός ( Indós ) + νῆσος ( nêsos , “ island ” ) 
--- etymonline body
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of Indonesia 

 Indonesia 

 "the East Indies," 1850, from Indo- "India" + Greek nēsos "island" (see Chersonese ) + -ia . Formerly called Indian Archipelago or East Indies Islands (see Indies ). Related: Indonesian "of or from the East Indies" (1850).
 also from 1850 

 Entries linking to Indonesia 

 Chersonese 

 peninsula south of Thrace, from Greek khersonesos "peninsula," etymologically "island connected to the mainland," from khersos "dry land, mainland" + nēsos "island," also "(flooded) land near a river, alluvial land," which is of uncertain origin; traditionally from PIE root sna- "to swim," but this is now generally rejected. "As words for 'island' differ from language to language, [ nēsos ] is probably an Aegean loan (note that Lat. insula is also of unclear origin)" [Beekes]. Compare isle .

 Greek khersos is perhaps from PIE root  *ghers-  "to bristle" (see horror (n.)) if the Greek word first referred to "arid, stubbly land, and only later to land in opposition to water" [Beekes].

 Indies 

 "India and adjacent regions and islands," 1550s, plural of Indie , Indy , from Middle English Ynde (early 13c.), the usual word in Middle English for "India," from the Old French form of Latin India (see India ). Commonly applied to Asia and the East generally; later in a time of geographical confusion, it was applied to the Caribbean basin, which was distinguished from Asia proper by being called the West Indies .

 -ia
```


## [2026-09-14T02:36:20.438Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8560,8575p' BRT.txt; echo '=== search snā root'; grep -n 'sna-  V\\|snä-  V\\|snā-  V\\|V.  .waschen\\|waschen.$' BRT.txt | head -10; echo '=== page offset'; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['BRT'].get('page_offset'));print(str(d['BRT'].get('lookup_hint'))[:400])\""
}
```


### [2026-09-14T02:36:21.576Z] TOOL RESULT

```
•  j.  us«-fritay-  £  'Weihe,  feierliche  Dar- brlngung*:  yd  .  .  haomake  hutahe  daoätti 'tiiiam  (Gen.  part.  ab  Obj.)  vä  ntyezdinam V.  18. 1  z.
Pü. :  ängnh  OH  i  us  franäfl  mya^.
•  j.  usnäka-  m.  EN.  eines  Gläubigen; 'kake  asaonS  Yt  y.  117.
Et?
•  j.  usnätay-    £    'Abwaschung':    %risa-
td^w^m  frasnat!e{sd.)  ürisataüw^m  upa- srt'We  ayiyqm  (sd.)  paiti  'snäitimV.S.qZ.
Komp.:   us-\-mälay-,   %  304   II.  34.    —    Pü.:
afar  soiilniA.
•  j.  usmä'nar-  m.  EN.  eines  Gläubigen: -narahe'''* paisatake  a?aons  "des  U.,  Sohns des  P.  . ."  YtiJ.97;  120.
Eig.  'dem  die  Männer  ehrerbietig  (s.  unter i/w-Hfl-)  sind'.  —  »  Them.
•  j.  *U8y^§'>  Adv.'>  'nach  oben,  in  die Höhe':  yahmal  kaca  naiHs  iunjayut  ,  . iiüil  US'  tacS  nffit  *nisyas  "vor  dem  sich keiner  retten  kann;  mag  er  nach  der Höhe,  mag  er  nach  der  Tiefe  (laufen  sva.) sich  flüchten"  Aog.  56'ff.
NSm.'>;  Ableil.  aus  ar.  •«/,  mit  übeittagenem 13);  s.«t;  S/7'Jaß.i*p.  —  ai.  vgl.  idant-,  fem. üJici; —  Pü.!  lefa  usiA  uarat^ißv.xye  ürdhväd ürdhuacärinaK),  erl.  i  *ku  fa  luhTh  i  asmätt andar  saiiit  figSn  iayui.  —  ')  Hds.  usiqs, Ausg.  usyifs;  vgl.  die  Var.  »u  faili.yqJ  Yt.  S. 21.  —  ")  Vgl.  lu  parq}.  —  3)  Man  erwartete *usifi;  das  y  stammt  von  dem  Gegenstück *nyni.
•  j.  vtsaiti  (sd.)  ainyi!  "usyö  nöit  aiityo svistmnö  *ästryeHe  P.  57.
Man  verlangt  einen  das  Verbum  ergänzenden Inf.  Nach  V.  t8.  26  vermute  ich  uilayö,  Inf. lum  V.  j/fl-  (Praei.  %^  staya-)  mit  «r.  — Pü. :  utdärisnJh.
db,Google
409
=== search snā root
10920:•  i-i  K'i  P*  xSnä-,  'sna-  V,  "kennen'. Praes.  14  (Inkoh.)  xsaäsa-,  16  (Des.) sixsnanha-,  —  Inf.  'xsnJy  °xsn>m;  PPfP.
27118:•  j.  SM-  V.  'waschen'.  Praes.  18  siü^a; 27  snaya-,  •snya-.  —  PPfP.  mala-;  Int 'snatSe.
=== page offset
Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
```


## [2026-09-14T02:36:28.066Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '27114,27124p' BRT.txt; echo '--- nearby col numbers'; awk 'NR>=27000 && NR<=27300 && /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/ {print NR\": \"$0}' BRT.txt | head; echo '--- usnatay col'; awk 'NR>=8400 && NR<=8700 && /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/ {print NR\": \"$0}' BRT.txt | head"
}
```


### [2026-09-14T02:36:29.191Z] TOOL RESULT

```
—  yezi  mS  hau  na  ava  *'%ifa ''  aot  ava asnavät  "wenn  mich  der  Mann  dort  mit jener  Waffe  trifft"  P.  21-,  —  aka  Ti  säzdam '^jjj  "so  wehret  ihnen  denn  mit  der Waffe"  Y.31.  rS;  ~-  sfon^wa/a  '^iVa  Y. 57.  I  o,  Yt  4-  8 ;  Y.  57.  1 6 ;  —  avavaia •hisa  yaia    asma    kats.masä    Yt  77. 3o;
—  aurvantö  . .  yHi  tivaüiya  ''hlzbya  (ID.) "' fräyaiayänti  vaamna  .  .  sraostm  Y. 57-  »9-
KompE.  —  Zmn  V.  ina%-.  —  Vgl.  mp.  irüA, np.  simki);  wohl  aus  ir.  *saa%ia:  —  Pü.: snih,  Npu.:  liläi,  Sü.:  iaslram.  —  ')  Hdi. '%ii.  —  >)  Was  ist  mit  dem  Dual  gemeint?  — ])  S.  bei  DsT.  folr.  2.  266  No.,  wo  üiyär
snih,  erU:  iisyär  siläk  und  M  4  zu  Y.  $7-  29< wo  mp.  sneh  mit  np.  sinih  glosiirt  wird}  die Erläuterung  dain  iüia  "Leiter'  passt  allerdings schlechL
•  j.  SM-  V.  'waschen'.  Praes.  18  siü^a; 27  snaya-,  •snya-.  —  PPfP.  mala-;  Int 'snatSe.
'waschen,  durch  Spülen  reinigen':  snätd
F./2.
mit  a  dnwS. :  aat  *asnalar^  (sd.)  yat haomgmca  äsnayät  .  .  N.  y^.
mit  upa:  s.  Inf.
mit  US  'aus-,  abwaschen':  us  tanüm  sna- yasta  us  *7'asirä  (nämL  sm^tota)  gSui malsmana  apäca  V.5. 54.
mit  fra  i)  'abwaschen,  abspülen':  yat hi  zasta  frasnäta  (ND.)    V.  8.  40;    40;
--- nearby col numbers
--- usnatay col
8403: 398
8483: 404
8513: 406
8531: 407
8575: 409
8690: 415
8693: 416
```


## [2026-09-14T02:36:34.904Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=26800 && NR<=27600 && /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/ {print NR\": \"$0}' BRT.txt | head -20"
}
```


### [2026-09-14T02:36:36.000Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:36:40.135Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=26500 && NR<=28000 {if ($0 ~ /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/) print NR\": \"$0}' BRT.txt | head -20; echo '--- any digits-only lines count'; grep -c -E '^[[:space:]]*[0-9]{3,4}[[:space:]]*$' BRT.txt; echo '--- around 27118 leaf'; python3 -c \"\nff=0\nfor i,l in enumerate(open('BRT.txt',encoding='utf-8',errors='replace'),1):\n    ff+=l.count('\\f')\n    if i==27118: print('leaf',ff); break\""
}
```


### [2026-09-14T02:36:41.336Z] TOOL RESULT

```
--- any digits-only lines count
617
--- around 27118 leaf
leaf 887
```


## [2026-09-14T02:37:06.543Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nleaf=0; res=[]\nfor line in open('KLN_1966.txt',encoding='utf-8',errors='replace'):\n    leaf+=line.count('\\f'); s=line.strip()\n    m=re.fullmatch(r'(\\d{2,4})',s)\n    if m: res.append((leaf,int(m.group(1))))\nprint([r for r in res if 1020<=r[1]<=1040])\nEOF\necho '--- leaf content'; python3 -c \"\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport sys\nfor i in (546,547,548):\n    print('=== leaf',i, txt[i].strip().replace('\\n',' | ')[:600])\n\""
}
```


### [2026-09-14T02:37:07.861Z] TOOL RESULT

```
[(546, 1021), (547, 1022), (550, 1028), (552, 1033), (553, 1035), (554, 1036), (555, 1039), (556, 1040), (872, 1040)]
--- leaf content
=== leaf 546 appoint,  something;  to  have  room; to  be  able;  to  be  obliged’,  d-degree  of  I.-E.  base med-,  ‘to  measure,  limit’,  whence  OE.  metan,  ‘to measure’.  See  mete,  ‘to  measure',  and  cp.  words there  referred  to.  Cp.  also  mote,  ‘may’.  ■ Derivative:  must,  n. | must,  n.,  mold,  mustiness.  —  Prob.  back  forma¬ tion  fr.  musty. | must,  adj.,  frenzied,  mad  (said  of  male  elephants). | _ Hind,  mast,  fr.  Pers.  mast,  rel.  to  OI.  matta-, | ‘drunk,  intoxicated’,  pp.  of  mddati,  ‘boils,  bub¬ bles,  gets  drunk’,  fr.  I.-E.  base  *mad-,  ‘wet,  to drip’. 
=== leaf 547 ;  see  man.  Peas¬ ants  were  called  ‘little  men  ,  because  according to  the  ancient  Russian  law,  peasants  were  re¬ garded  as  minors. | muzzle,  n.,  the  projecting  part  of  the  head  of  an animal;  snout.  —  ME.  muselt,  fr.  OF.  musel  (F. museau),  fr.  ML.  musellum,  dimin.  of  musum, ’muzzle,  snout',  whence  It.  muso,  OProven?. mus,  of  s.m.;  of  unknown  origin.  Cp.  muse. Derivatives:  muzzle,  tr.  v.,  muzzt-er,  n. muzzy,  adj.,  confused;  dazed.  —  Of  unknown origin. | Derivatives:  muzzi-ly,  adv.,  muzzi-ness,  n. my,  possessive  pron.  of  the 
=== leaf 548 d  fr  prec.  word  with  suff.  -aceae. myricaceous,  adj.  —  See  prec.  w'ord  and  -aceous. myring-,  form  of  myringo-  before  a  vowel, myringa,  n.,  the  tympanic  membrane  ( anat .)  — ModL.,  fr.  ML.  miringa,  dissimilated  fr.  Late  L. meninga,  mininga,  fr.  Gk.  [xrjviyp,  gen.  [xv;- vtyyo c,  ‘membrane’.  See  meninx. myringitis,  n.,  inflammation  of  the  tympanic membrane  (med.)  —  A  Medical  L.  hybrid  coin¬ ed  fr.  myringa  and  -itis,  a  suff.  of  Greek  ori¬ gin. | myringo-,  before  a  vowel  myring-,  combining form  denoting  the  tympanic  membrane.  —
```


## [2026-09-14T02:37:16.712Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (550,551,552):\n    print('=== leaf',i, txt[i].strip().replace('\\n',' | ')[:1400]); print()\n\""
}
```


### [2026-09-14T02:37:17.706Z] TOOL RESULT

```
=== leaf 550 B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  mm  (gen.  anuan),  Gk. ovop.a  (dial,  form  ovup.a),  Alb.  emen,  L.  no- men,  OSlav.  ime  (gen.  imene,  imeni),  OPruss. emmens,  emnes,  OIr.  ainm,  OW.  anu  (pi.  enueiri), W.  enw,  Co.  hanow,  ‘name’.  Outside  Indo- European  cp.  Lapp,  namma,  Finn,  nime-.  Hung. nev,  ‘name’.  Cp.  agnomen,  allonym,  anonymous, antonomasia,  antonym,  cognomen,  cryptonym, denominate,  eponym,  Evonymus,  homonym, ignominy,  Jerome,  metonymy,  metronymic,  mis¬ nomer,  nom,  nomen,  nomenclator,  nomenclature, nominal,  nominate,  nominative,  noun,  nuncupa¬ tive,  onomastic,  onomato-,  paronomasia,  paro- nymous,  patronymic,  polyonymous,  praenomen, pseudonym,  renown,  synonym,  toponym,  trino- minal. | Derivatives:  name,  v.  (q.v.),  name-less,  adj., name-ly,  adv. | name,  tr.  v.  —  ME.  namen,  fr.  OE.  namian,  fr. nama,  ‘name’.  See  name,  n. | Derivatives:  name-able,  nam-able,  adjs.,  name- abil-ity,  n.,  nam-abil-ity,  n.,  nam-er,  n. | namesake,  n.,  a  person  having  the  same  name  as an  other.  —  Contraction  of  name's  sake.  Name¬ sake  lit.  denotes  ‘a  person  named  for  the  sake  of another’s  name'. | nan-,  form  of  nano-,  before  a  vowel. | Nancy,  fem.  PN.  —  Prob.  from  a  misdivision  of mine  Ancy  into  my  Nancy.  Ancy  is  a  dimin.  fo

=== leaf 551 of  coconut  shells, narial,  adj.,  pertaining  to  the  nares.  —  Formed fr.  nares  with  suff.  -ial. | I | nark,n.,  spy,  informer,  stool  pigeon  ( British  slang). —  From  Gypsy  nak,  ‘nose’,  fr.  Hind,  nak, ‘nose’,  fr.  OI.  nakrd,  fr.  Prakrit  nakka-,  nakka-, of  s.m.,  which  prob.  stand  for  *nas-ka-  and  are rel.  to  OI.  ndsa  (dual),  ‘nose’.  See  nose, narrate,  tr.  v.,  to  relate,  recount.  —  L.  narratus, pp.  of  narrdre,  ‘to  tell,  relate,  recount’,  prop,  ‘to make  acquainted  with’,  fr.  * gnarare ,  *narare, fr.  gnarus,  narus,  ‘acquainted  with,  knowing’,  fr. I.-E.  base  *gno-,  ‘to  know’,  whence  also  OE. cnawan,  ‘to  know'.  See  know  and  words  there referred  to  and  cp.  esp.  ignore.  For  the  ending see  verbal  suff.  -ate.  The  doubling  of  the  con¬ sonant  -r-  in  narrdre  is  a  compensation  for  the shortening  of  the  vowel  a  in  gnarus. narration,  n.  —  ME.  narraciun,  fr.  MF.  (=  F.) narration,  ‘a  relating,  recounting,  narrating’,  fr. L.  narrationem,  acc.  of  narratio,  of  s.m.,  fr.  nar¬ ratus,  pp.  of  narrdre.  See  prec.  word  and  -ion. narrative,  adj.,  1)  that  which  narrates;  2)  per¬ taining  to  narration.  —  Late  L.  narrativus,  ‘suit¬ able  for  narration’  (prob.  through  the  medium of  F.  narratif),  fr.  L.  narratus,  pp.  of  narrdre. See  narrate  and

=== leaf 552 us,  ‘birth,  des¬ cent,  origin,  race,  sort,  kind,  class’.  See  genus and  words  there  referred  to  and  cp.  esp.  naive, nascent,  natal,  native,  nature,  cognate,  connate, innate,  nee,  pregnant,  'with  child’,  and  the  sec¬ ond  element  in  puisne  and  puny. | national,  adj.  —  MF.  (=  F.),  fr.  nation.  See  prec. word  and  adj.  suff.  -al. | Derivatives:  national,  n.,  national-ism,  n.,  na- tional-ist,  n.  and  adj.,  national-ist-ic,  adj.,  na- tional-ist-ic-al-ly,  adv.,  national-ity,  n.,  national¬ ize,  tr.  v.,  national-iz-ation,  n.,  national-iz-er,  n., national-ly,  adv.,  national-ness,  n. | native,  adj.  —  ME.  natif,  fr.  MF.  (=  F.)  natif (fem.  native),  fr.  L.  ndtivus,  'born,  innate,  nat¬ ural,  primitive’,  fr.  natus,  pp.  of  nasci,  'to  be born’.  See  nation  and  -ive  and  cp.  naive,  which is  a  doublet  of  native. | Derivatives :  native,  n.,  nativ-ism,  n.,  nativ-ist,  n., nativ-ist-ic,  adj. | ! | nativity,  n.,  1)  birth;  2)  horoscope  (astral.)  — ME.  nativite,  fr.  OF.  (=  F.)  nativite,  fr.  L.  ndti- vitatem,  acc.  of  nativitas,  ‘birth’,  fr.  ndtivus.  See native  and  -ity.  Cp.  naivete,  which  is  a  doublet of  nativity. | natrium,  n.,  sodium  (chem.)  —  ModL.  See  natron and  chem.  suff.  -ium. | Natrix,  n.,  a  genus  of  snakes,  the  grass  snake (zool.)  —  L.  na
```


## [2026-09-14T02:37:24.665Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'natant,\\|natation,\\|natatory' KLN_1966.txt | head -5; python3 - <<'EOF'\nimport re\nleaf=0\nfor i,line in enumerate(open('KLN_1966.txt',encoding='utf-8',errors='replace'),1):\n    leaf+=line.count('\\f')\n    if 'natant,  adj' in line or 'natation,  n' in line:\n        print('line',i,'leaf',leaf)\n        print(line.strip()[:900]); print()\nEOF"
}
```


### [2026-09-14T02:37:26.194Z] TOOL RESULT

```
25010:natality,  n.,  1)  birth  (rare);  2)  birth  rate.  —  Form¬ ed  with  suff.  -ity  fr.  L.  natalis,  ‘pertaining  to birth’;  see  natal.  In  the  sense  'birth  rate’  the word  was  formed  directly  fr.  F.  natalite,  which derives  from  the  adj.  natal  (fr.  L.  natalis). natant,  adj.,  floating.  —  Fr.  L.  natans,  gen.  -antis, pres.  part,  of  natare,  ‘to  swim’.  See  next  word and  -ant.
25011:Derivative:  natant-ly,  adv. natation,  n.,  the  act  or  art  of  swimming.  —  L. natatio,  gen.  -unis,  ‘a  swimming’,  fr.  natatus,  pp. of  nato,  natare,  ‘to  swim’,  which  stands  for  l.-E. *snl-t-o,  enlargement  of  base  *sna-,  *sne-,  ‘to flow’.  Cp.  Arm.  nay  (for  *snlt-),  ‘wet,  liquid’; cp.  also  *snet-,  *snot-  in  Gk.  votoc,  'the  south wind,  the  south',  prop,  ‘a  rainy  wind',  v6xio;, voTcpoc,  ‘damp,  moist’.  From  the  unenlarged base  *snd-  derive  L.  no,  nare,  ’to  swim’  (for * snd-yd ),  OI.  snati,  snayate,  'bathes’  (intr.),  the second  element  in  ghrta-snd-,  ‘dipped  into  but¬ ter’,  Avestic  snayeite,  ‘washes,  cleans’,  Toch.  B naskem,  ‘they  bathe’  (tr. ),  Gk.  vrj-/e tv  (for *va-yctv),  ‘to  swim’,  Mir.  sndim,  ‘I  swim’, sniim,  'a  swimming',  MBret.  neuff,  'to  swim’, and  prob.  also  Gk.  v^ao;,  Dor.  mSosoq,  ‘island’ (for  *va-oo5,  lit.  ‘that  which  swims').  From  l.-E. *snau-,  *sneu-,  an  -u-enlargement  of  base  *snd-, derive  OI.  snauti  (pp.  snutdh),  'drips,  gives
25012:milk’,  Gk.  vdcot,  Aeol.  vatco,  vauco  (for  *vxf- ito),  ‘I  flow’.  Cp.  natant,  natatorial.  Cp.  also naiad,  naiant,  Nama,  necto-,  Nereid,  neso-, nourish,  the  first  element  in  Notogaea  and  the second  element  in  chersoneso-  and  in  Indonesia, Melanesia,  Micronesia,  Polynesia.  Cp.  also snout.  For  the  ending  of  natation  see  -ation.
25013:natatorial,  adj.,  natatory.  —  See  next  word  and adj.  suff.  -al.
25014:natatory,  adj.,  swimming;  characterized  by  swim¬ ming.  —  Late  L.  natdtorius,  ‘pertaining  to  swim¬ ming’,  fr.  L.  natatus,  pp.  of  natare.  See  natation and  adj.  suff.  -ory.
line 25010 leaf 551
natality,  n.,  1)  birth  (rare);  2)  birth  rate.  —  Form¬ ed  with  suff.  -ity  fr.  L.  natalis,  ‘pertaining  to birth’;  see  natal.  In  the  sense  'birth  rate’  the word  was  formed  directly  fr.  F.  natalite,  which derives  from  the  adj.  natal  (fr.  L.  natalis). natant,  adj.,  floating.  —  Fr.  L.  natans,  gen.  -antis, pres.  part,  of  natare,  ‘to  swim’.  See  next  word and  -ant.

line 25011 leaf 551
Derivative:  natant-ly,  adv. natation,  n.,  the  act  or  art  of  swimming.  —  L. natatio,  gen.  -unis,  ‘a  swimming’,  fr.  natatus,  pp. of  nato,  natare,  ‘to  swim’,  which  stands  for  l.-E. *snl-t-o,  enlargement  of  base  *sna-,  *sne-,  ‘to flow’.  Cp.  Arm.  nay  (for  *snlt-),  ‘wet,  liquid’; cp.  also  *snet-,  *snot-  in  Gk.  votoc,  'the  south wind,  the  south',  prop,  ‘a  rainy  wind',  v6xio;, voTcpoc,  ‘damp,  moist’.  From  the  unenlarged base  *snd-  derive  L.  no,  nare,  ’to  swim’  (for * snd-yd ),  OI.  snati,  snayate,  'bathes’  (intr.),  the second  element  in  ghrta-snd-,  ‘dipped  into  but¬ ter’,  Avestic  snayeite,  ‘washes,  cleans’,  Toch.  B naskem,  ‘they  bathe’  (tr. ),  Gk.  vrj-/e tv  (for *va-yctv),  ‘to  swim’,  Mir.  sndim,  ‘I  swim’, sniim,  'a  swimming',  MBret.  neuff,  'to  swim’, and  prob.  also  Gk.  v^ao;,  Dor.  mSosoq, 

line 37503 leaf 819
Derivatives:  superman-ism,  n.,  superman-ly, adj.,  superman-li-ness ,  n. supernal,  adj.,  heavenly,  celestial,  spiritual.  — ME.,  fr.  MF.,  formed  with  adj.  suff.  -al  fr.  L. supernus,  ‘celestial’,  fr.  super,  ‘above’.  See  super-, supernatant,  adj.,  floating  on  the  surface.  —  L. supernatans,  gen.  -antis,  pres.  part,  of  super- natare,  ‘to  swim  above’,  fr.  super-  and  nature,  ‘to swim’.  See  natation.
```


## [2026-09-14T02:37:36.575Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== AKD shamash'; grep -n -i 'sama[sš]\\|shamash\\|Sonnengott' AKD.txt | head -6; echo '=== LKT shams'; grep -n -i 'sams\\|schams\\|Sonne.*ar\\.' LKT.txt | head -6; echo '=== SKT Samson'; grep -n -i 'samson' SKT.txt WEB_vol1.txt | head -4; echo '=== RCH shams'; grep -n -i 'shams, the sun\\|shams,' RCH.txt | head -4"
}
```


### [2026-09-14T02:37:36.695Z] TOOL RESULT

```
=== AKD shamash
1019:Die  Namen  der  Wochentage  1)  'HUov  vf4iQ«,  dies  solis  usw.,  Sonn- tag, 2)  ij^iQa  ^iih'jvijg,  lunae  dies  usw.,  Jfowtag,  3)  fifiiga  'Aqiws,  Martis dies  usw.,  fi'anz.  marä\,  engl,  thtiesdaj,  deutsch  (dial.)  Äestag,  und  viell. doch  auch  Dienstag,  4)  ?/^/pa  'Egf/ov,  Mercurii  dies  usw.,  franz.  mercreAi, engl.  wednesAaj,  5)  nfxiqa  Ai.ög,  Jovis  dies  usw.,  engl,  thiirsdaj,  Donners- tag, 6)  ijf^^ga  'Aq)QoSlT>]g,  Veneris  dies  usw.,  i^mtag,  7)  i'jfii'^a  Kqövov, Satiirni  dies  usw.,  engl.  saturAaj,  niederdeutsch  safe>-dach,  gehen  durch mehrfache  Übersetzungen,  wenn  auch  nicht  unmittelbar,  so  doch  mittelbar insofern  auf  eine  Benennung  der  Tage  nach  den  babyl.  Göttern  1)  Samas, 2)  Sin,  3)  Nergal,  4)  Nabu,  5)  Mardtik,  6)  Btar,  1)  Kaimänu,  zurück, als  der  7tägigen,  auf  hellenistischem  Boden  entstandenen  Woche  eben  die 7  urspr.  babylonischen  Planetengötter  zugrunde  liegen.
=== LKT shams
34:Betrachtet  man  die  Form  der  dem  Orient  entlehnten  Wörter^,  so fallt  es  auf,  dals  diese  Entlehnungen  zwar  mehr  oder  weniger  dem  natio- nalen Lautbestande  der  betreffenden  Zeit  angeglichen,  die  Lautgesetze  aber, wie  sie  für  die  ungestörte  Entwicklung  jeder  Sprache,  etwa  für  das  Werden der  romanischen  Sprachen  aus  den  Formen  des  Vulgärlateins,  beobachtet und  festgestellt  sind,  nur  in  seltenen  Fällen  beachtet  werden.  Hier  wirken Eigentümlichkeiten  des  eigenen  und  des  fremden  Lautbestandes,  Neigung zur  vereinfachten  oder  bequemeren  Aussprache,  Assimilation  und  Dissimi- lation, volkstümliche  Anlehnung  an  bekanntere  Wortformen  und  zahlreiche fast  willkürlich  erscheinende  Ursachen  zusammen,  ohne  daß  es  möglich wäre,  eine  allgemein  gültige  Gesetzmäßigkeit  festzustellen.  Als  wichtigster Umstand  kommt  noch  hinzu,  dafs.  wie  schon  erwähnt,  die  orientahschen Grundwörter  meistens  durch  mehrere  europäische  Sprachen  hindurchgehen und  in  ihnen  immer  wieder  aufs  Neue  jene  lautlichen  Änderungen  erfahren,, ehe  sie  in  ihre  heutige,  endgültige  Form  angelangt  sind.  Als  die  wichtigste Zäsur,  welche  die  Zeiten  größerer  und  geringerer  Formänderung  der  Ent- lehnungen trennt,  muß  die  Erfindung  der  Buchdruckerkunst  bezeichnet werden;  während  bis  dahin  die  soeben  angedeuteten  Ursachen  im  Munde des  Volkes  ungehemmt  wirken,  üben  der  Buchdruck  und  die  durch  ihn bewirkten  oder  auf  ihm  sich  gründenden  Kulturerscheinungen,  unter  denen nur  die  Schule  als  bedeutsamste  genannt  werden  soll,  eine  stark  konser- vierende Wirkung  aus.  Wörter,  die  in  den  letzten  Jahrhunderten  aus  dem Orient  zu  uns  gekommen  sind,  stehen  daher  der  ursprünglichen  Grundform so  nahe,  daß  man  ohne  weiteres  ihren  fremden  Ursprung  hört  und  sieht, während  frühere  Entlehnungen  nur  noch  schwer  zu  durchschauen  sind.
41:Die  weitaus  bedeutsamste  Verbindung  des  Morgen-  und  Abendlandes im  Altertum  wurde,  wenn  von  einer  Besprechung  der  Wirkung  der  Perser- kriege in  sprachlicher  Hinsicht  abgesehen  werden  darf,  durch  den  Zug Alexanders  des  Großen  hervorgerufen.  Bis  auf  diese  Zeiten  läßt  sich  der erste  reichlichere  Abfluß  orientalischer  Begriffe  und  Wörter  in  die  griechische Sprache  und  in  den  darauf  folgenden  Jahrhunderten  ins  Latemische  zurück- führen; seitdem  erstreckt  sich  die  Wirkung  in  ununterbrochenem  Flusse bis  auf  die  heutigen  modernen  Sprachen  und  Dialekte  Europas.  Das  folgende hellenistische  Zeitalter  begünstigte  aus  hier  nicht  zu  erörternden  Gründen die  Entlehnung  orientalischen  Sprachgutes  in  hervorragendem  Maße:  die Verbreitung  des  Judentums  und  die  Entstehung  des  Christentums  gaben Anlaß  zur  Übernahme  vieler  hebräischer  und  aramäischer  Wörter  ins Griechische  und  Lateinische  [besonders  in  die  als  Kichenlatein  bezeichnete Färbung].  Mit  dem  Mittelalter  beginnt  der  Einfluß  des  Arabischen.  Nach- dem sich  der  Islam  von  den  malayisclien  Inseln  bis  zu  den  Gestaden  des Atlantischen  Ozeans  verbreitet  hatte,  war  eine  riesige  Berührungslinie  des arabischen  Sprachgebiets  mit  dem  Abendlande  geschaffen.  Der  Wortschatz der  Sprachen  der  Pyrenäenhalbinsel,  des  Spanischen,  Portugiesischen  und Katalanischen,  und  in  geringerem  Umfange  anch  der  des  ProvenzaHschen, Französischen  und  Italienischen  werden   mit  arabischen   Wörtern  derart
851:293.  Hebr.  b§s§m: 'Balsamstaude,  Balsam',  eine  Handels- ware, welche  die  Griechen  nebst  dem Namen  von  den  Phöniziern  erhielten. Gr.  ßd\aa|nov,  lat.  balsamum;  hieraus  it. balsamo,  balsimo,  asp.  blasmo,  sp.  pg. balsamo,  prov.  balme,  frz.  bäume  [aber pikardisch  bäm  'Minze'],  rum.  baisam; dtsch.  Balsam,  ndl.  balsem,  engl,  bahn; russ.  bal'sam,  bulg.  serb.  poln.  baisam, cech.  baisam,  balzam.  —  Aus  demselben Grundwort  mlat.  bisamum,  dtsch.  Bisam, cech.  poln.  pizmo  'Moschus'.  —  Vgl. noch  Balsamine,  Impatiens  Balsamina, engl,  halsamine,  baisam.  [Kluge  34  u. 54.  G.  Schvveinfurth,  Über  Balsam  und Myrrhe  1893.
1200:[Vom  Vb.  dafana  'vergraben,  begraben'] 'zurückgezogene  Frau' ;  hieraus  mit  leicht verständlichem  BedeuLungswandel  sp. adefina,  adafina,  dafina  'ein  bei  den Juden  Spaniens  früher  gebräuchlicher Ragout,  der  Freitags  auf  ein  Kohlen- becken gestellt  und  verdeckt  wurde,  um Samstags  gegessen  zu  werden',  in  er- weiterter Bedeutung  [oder  Rückkehr zur  ursprünglichen]  'verborgene,  geheime Sache'.    [DE  43/44.
1669:'Westlich';  hieraus  il.garbino,  frz. garbin 'Südwestwind'  auf  dem  Mittelmeere, prov.  garbin,  sp.  garbino  'Süd-  oder Westwind',  sp.  pg.  algarve  'fruchtbar', pg.  garabia  'Westen'.  Aus  dem  It. wurde  serb.  garbin  'Südwind'.  Jeden- falls mit  Kontamination  von  al-  arabija 'die  arabische  Sprache'  entstand  pg.  al- garabia,  pg.  algravia,  frz.  charabia  'un- verständliches Zeug,  Kauderwelsch',  frz. insbesondere  'Dialekt  der  Auvergne'.  — Aus  demselben  Stamme  ar.  garaba 'untergehen  (Sonne)'  ist  mit  präfigiertem ma-  zur  Angabe  des  Ortes  magrib  ge- bildet; der  Magreb  ist  Nordwestafrika von  Tunis  bis  Marokko;  ms  al-magribl 'der  Bewohner  des  M.'  wurde  irz. maugrebin  'dass.'.  —  Auch  der  Name der  pg.  Provinz  Algarve  ist  ar.  garb 'Westen',  daher  sp.  algarabio,  algarabia, pg.  algaravio  'Bewohner  von  Algarve'. [DE  119.  241.  Eguilaz  178.  Devic  DEt 125.    ML  3683.    Bern  SlEtWb  295.
1815:Auch  gungulän  'Sesam';  hieraus  z.  T. mit  ar.  Art.  und  mit  häutigem  Über- gange der  Vokale  ä>  e>z:  sp.  aljon- joU,  ajonjoU,  pg.  gergelim,  zirgelim,  Irz. jugeoline,  gengili.  Da  aus  dem  Samen des  Sesams  eine  rötliche  Farbe  her- gestellt wurde,  ergab  sich  noch  sp. dnzolino,  frz.  zinzolin  'rötlich-violett'. [DE  146/147.  Devic  DEt  127/128  und 230.
=== SKT Samson
WEB_vol1.txt:72313:1. [usually pi] a shackle or a chain for the feet; a chain by which a person or an animal is confined by the feet. The Philistines bound Samson with fetters of brass. —Judges xvi. 21. 2. anything that confines or restrains from motion; a restraint. Passions too fierce to be in fellers bound. —Dryden. fettered, pt., pp.; fettering, ppr- [ME. feteren, from AS. gefeterian, to fetter.] 1. to put in fetters; to shackle or confine the feet of with a chain. 2. to bind; to enchain; to confine; to re- strain motion of; to impose restraints on.
=== RCH shams
265:solar  worship,  falls  to  the  ground ;   neither  of  the names,  Sham  nor  Sj/na,  having  any  reference  to the  sun.  Sham,  by  which  that  country  is  most generally  known  to  the  Asiatics,  is  a   root  so  little connected  with  the  Hebrew  shemesh  or  the  Arabic shams,  that  no  inflexions  of  those  languages  can ever  possibly  produce  the  most  remote  analogy. Sham,  shamat,  or  shiimah,  (and  with  the  article  ash- sham  or  ashshamah,  implies  Mack,  a   Mack  mole  upon (he  face  ;   the  left  hand,  &c.  and  this  last  signifleation is  that  which  is  in  general  received  by  the  Ara- bians and  Syrians  themselves  ;   a   name,  they  say, this  country  obtained,  at  the  same  time  that  Ara- bia Felix  was  called which  implies  iho  right hand,  the  one  lying  to  the  right  and  the  other  to the  left  o<’  the  Kaaha,  or  temple  of  Mecca.  This is  the  derivation  adopted,  in  particular,  yet  with some  doi'd)t,  by  the  celebrated  Sultan  Abii’ljbdd, who  reigned  in  Syria  about  the  middle  of  the  four- teenth century  ;   and  wrote,  in  Arabic,  an  Univer- sal Histoni,  and  a   St/stem  of  Gcographi/,  Upon this  elymology,  Mr.  Bryant  observes,  “Abulfeda “   supposes,  that  Syria  is  called  Sham  quasi  sinistra.
```


## [2026-09-14T02:37:43.314Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; cat tools/verify_check.py"
}
```


### [2026-09-14T02:37:43.362Z] TOOL RESULT

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


## [2026-09-14T02:46:40.388Z] AGENT

The checker keys entries by their index in the source JSON, so entries 1–3 (entry 0 is the redirect). Now writing the verification file.


## [2026-09-14T02:56:59.791Z] TOOL CALL #75: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-461.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nout = {\n  \"pdf_page\": 461,\n  \"book_page\": 431,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": []\n}\n\nW_SHENA   = \"https://en.wiktionary.org/wiki/%D8%B4%D9%86%D8%A7\"\nW_NESOS   = \"https://en.wiktionary.org/wiki/%CE%BD%E1%BF%86%CF%83%CE%BF%CF%82\"\nE_ARSENAL = \"https://www.etymonline.com/word/arsenal\"\nW_ARSENAL = \"https://en.wiktionary.org/wiki/arsenal\"\nW_SHAMS   = \"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B3\"\nW_SHEMESH = \"https://en.wiktionary.org/wiki/%D7%A9%D7%9E%D7%A9\"\nW_SANAT   = \"https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%B9%D8%AA\"\nW_SINAA   = \"https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%A7%D8%B9%D8%A9\"\nW_OSHNAN  = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B4%D9%86%D8%A7%D9%86\"\nE_POLY    = \"https://www.etymonline.com/word/polynesia\"\nW_POLY    = \"https://en.wiktionary.org/wiki/Polynesia\"\nW_SAMSON  = \"https://en.wiktionary.org/wiki/Samson\"\nE_INDO    = \"https://www.etymonline.com/word/Indonesia\"\nW_INDO    = \"https://en.wiktionary.org/wiki/Indonesia\"\nA_SHAMS   = \"https://abadis.ir/fatofa/%D8%B4%D9%85%D8%B3/\"\nA_SANAT   = \"https://abadis.ir/fatofa/%D8%B5%D9%86%D8%B9%D8%AA/\"\nA_SHENA   = \"https://abadis.ir/fatofa/%D8%B4%D9%86%D8%A7/\"\n\nKLN_SAMSON = (\"Klein 1966 p.1379 (KLN_1966.txt leaf 733, between the printed page markers 1378 and 1382), \"\n  \"s.v. 'Samson, Sampson': “1) masc. PN.; 2) in the Bible a judge distinguished for his enormous strength. \"\n  \"— Late L., fr. Gk. Σαμψών, fr. Heb. Shimshōn, a name derived fr. shemesh, 'sun'. \"\n  \"Cp. Aram. shimshā, Syr. shemshā, Arab. shams (dissimilated fr. *shamsh), Akkad. shamshu, Ugar. sh-p-sh, 'sun'.”\")\n\nKLN_ARSENAL = (\"Klein 1966 p.108 (KLN_1966.txt leaf 68, which carries the printed page markers 108 and 109), s.v. 'arsenal': \"\n  \"“It. arsenale (OIt. arzanale), 'dock', borrowed — prob. through the medium of MGk. ἀρσηνάλης — \"\n  \"fr. Arab. dār-aṣ-ṣināʿah (whence also Sp. dársena and It. darsena, 'dock'), lit. 'house of construction', \"\n  \"fr. dār, 'house', as-, assimilated form of al-, 'the', and ṣināʿah, 'construction, art', fr. ṣanaʿa, 'he made'.”\")\n\nKLN_NATATION = (\"Klein 1966 p.1030 (KLN_1966.txt leaf 551, printed markers 1028–1033), s.v. 'natation': \"\n  \"“… which stands for I.-E. *snā-t-ō, enlargement of base *snā-, *snē-, 'to flow'. … From the unenlarged base *snā- \"\n  \"derive L. nō, nāre, 'to swim', OI. snāti, snāyate, 'bathes', … Avestic snāyeite, 'washes, cleans', \"\n  \"Toch. B naskem, 'they bathe', Gk. νήχειν, 'to swim', … and prob. also Gk. νῆσος, Dor. νᾶσος, 'island' \"\n  \"(for *νᾶσος, lit. 'that which swims') … Cp. also … the second element in chersoneso- and in Indonesia, Melanesia, \"\n  \"Micronesia, Polynesia.”\")\n\nPOK_971 = (\"POK_full.txt line 78824: “Root / lemma: snā-, snə-(t-), snāu- sn-eu- sn-et- / Meaning: to flow, swim; damp, nymph of waters”, \"\n  \"with “Page(s): 971-972” and “References: WP. I 397, II 692 ff.” — the material lists “Avestan snāyẽte 'washes, purifies, \"\n  \"cleans through Spülen', participle snāta-” and “νῆσος, Doric νᾶσος 'island' as 'Schwimmer'”. \"\n  \"Nourai's page number is exact.\")\n\ndef entry(idx, root, verdict, modern, note, note_fa, sources, refcheck, consulted, nodes):\n    return {\"entry\": idx, \"root\": root, \"verdict\": verdict, \"modern_form\": modern,\n            \"note\": note, \"note_fa\": note_fa, \"sources\": sources,\n            \"ref_check\": refcheck, \"consulted\": consulted, \"nodes\": nodes}\n\ndef node(i, lang, words, verdict, der, der_fa, sources, refcheck, consulted, **extra):\n    d = {\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n         \"derivation\": der, \"derivation_fa\": der_fa, \"sources\": sources,\n         \"ref_check\": refcheck, \"consulted\": consulted}\n    d.update(extra)\n    return d\n\n# ---------------------------------------------------------------- entry 1\ne1_nodes = [\n node(1, \"Arabic\", \"šams\", \"confirmed\",\n  \"Arabic شَمْس šams 'sun' is the regular Arabic reflex of Proto-Semitic *śamš- 'sun', with the \"\n  \"expected Arabic dissimilation of the second sibilant (*šamš > šams), exactly as Klein states; the cognates are \"\n  \"Hebrew šemeš, Aramaic šimšā, Syriac šemšā, Akkadian šamšu (the sun-god Šamaš) and Ugaritic špš. \"\n  \"Nourai's root box 'Semitic Š.m.š' is the triliteral abstraction of exactly this etymon, so the arrow root → Arabic šams is correct.\",\n  \"«شمس» در عربی بازماندهٔ مستقیم صورت سامی آغازین *śamš- «خورشید» است؛ \"\n  \"سین پایانی از راه ناهمگونی (dissimilation) جایگزین شین دوم شده است (*šamš > šams)، \"\n  \"چنان‌که کلاین تصریح کرده است. هم‌ریشه‌های آن عبری šemeš، آرامی šimšā و اکدی šamšu است. \"\n  \"ادعای نورایی درست است.\",\n  [W_SHAMS],\n  [{\"ref\": \"KLN:1379\", \"status\": \"supports\", \"note\": KLN_SAMSON}],\n  [{\"src\": \"KLN\", \"where\": \"p.1379 s.v. Samson; p.1430 s.v. Shamash\", \"stance\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 759 s.v. 'Shamash': “Akkad. shamash, shamshu, 'sun; the god of the sun', rel. to Heb. shemesh, 'sun', Aram. shimsha, Syr. shemsha, Ugar. sh-p-sh, Arab. shams (dissimilated fr. *shamsh), of s.m.”\"},\n   {\"src\": \"RCH\", \"where\": \"introduction, p. (RCH.txt line 265)\", \"stance\": \"supports\",\n    \"note\": \"Richardson/Johnson speak of “the Hebrew shemesh or the Arabic shams” as the two Semitic words for the sun — the pairing Nourai draws.\"},\n   {\"src\": \"FVQ\", \"where\": \"grep 'shams' in FVQ_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Jeffery treats only foreign vocabulary of the Qur'an; šams is native Arabic and has no entry (only 'Abd Shams in passing, line 7624).\"}]),\n\n node(2, \"Persian\", \"šams\", \"confirmed\",\n  \"New Persian شمس šams 'sun' is a straight Arabic loanword of the Islamic period, taken over with the Arabic \"\n  \"spelling and consonants; it never displaced the inherited خورشید/آفتاب but lives in learned, astronomical and \"\n  \"poetic registers and in the derivatives listed on the chart — شمسی (the solar calendar, Arabic nisba -ī), \"\n  \"شمسه (a sun-shaped rosette/ornament, as in Farrokhī's verse quoted in the book), and مُشمّس (Arabic passive \"\n  \"participle of form II, 'sunned'). Mo'in tags the word [ع.] = Arabic.\",\n  \"«شمس» در فارسی نو وام‌واژه‌ای عربی است که پس از اسلام با همان رسم‌الخط و همان صامت‌ها وارد شده \"\n  \"و جایگزین «خورشید» و «آفتاب» نشده، بلکه در زبان علمی و ادبی مانده است. معین آن را با نشانهٔ [ع.] \"\n  \"آورده و «آفتاب، خورشید» معنی کرده است. مشتقّات «شمسی»، «شمسه» و «مُشمّس» نیز همگی ساختهٔ عربی‌اند. \"\n  \"ادعای نورایی درست است.\",\n  [A_SHAMS, W_SHAMS],\n  [{\"ref\": \"MON:2075\", \"status\": \"partial\",\n    \"note\": \"Mo'in's 6-volume print pagination is not reachable online, but the entry itself is: Farhang-e Mo'in s.v. شمس (abadis.ir) reads “(شَ ) [ ع . ] (اِ. ) آفتاب، خورشید” — the Arabic-loan tag Nourai's arrow asserts. Page 2075 could not be confirmed.\"}],\n  [{\"src\": \"MON\", \"where\": \"s.v. شمس (vajehyab/abadis text of Farhang-e Mo'in)\", \"stance\": \"supports\",\n    \"note\": \"“(شَ ) [ ع . ] (اِ. ) آفتاب، خورشید.” — marked [ع.] = Arabic.\"},\n   {\"src\": \"ARY\", \"where\": \"grep شمس in ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's dictionary covers Indo-European roots of Persian only, so an Arabic loan such as شمس has no entry.\"},\n   {\"src\": \"KLN\", \"where\": \"p.1379\", \"stance\": \"supports\",\n    \"note\": \"Klein's “Arab. shams” is the immediate source of the Persian form; no separate Persian entry.\"}]),\n\n node(3, \"Hebrew\", \"šemeš; šimšon\", \"confirmed\",\n  \"Hebrew שֶׁמֶשׁ šémeš 'sun' continues Proto-Semitic *śamš- with the segholate vowel-insertion of Tiberian Hebrew \"\n  \"(*šamš > šémeš). שִׁמְשׁוֹן Šimšōn, the Danite judge of Judges 13–16, is formed from the same noun with the \"\n  \"hypocoristic/diminutive suffix -ōn, i.e. 'little sun, sun-man' — a name fittingly borne by a hero from Beth-Shemesh \"\n  \"country. Both words and the derivation šemeš → šimšōn are exactly what Klein prints.\",\n  \"عبری šémeš «خورشید» بازماندهٔ همان *śamš- سامی آغازین است که در عبری طبری به سبب قاعدهٔ \"\n  \"سگولی میان‌واکه گرفته است. نام «شمشون» (Šimšōn) از همین اسم با پسوند تصغیری/تحبیبی -ōn ساخته شده، \"\n  \"یعنی «خورشیدک، مرد خورشید»؛ وی داور بنی‌دان در سفر داوران ۱۳–۱۶ است. ادعای نورایی درست است.\",\n  [W_SHEMESH, W_SAMSON],\n  [{\"ref\": \"KLN:1379\", \"status\": \"supports\", \"note\": KLN_SAMSON}],\n  [{\"src\": \"KLN\", \"where\": \"p.1379 s.v. Samson\", \"stance\": \"supports\",\n    \"note\": \"“fr. Heb. Shimshōn, a name derived fr. shemesh, 'sun'” — verbatim Nourai's two Hebrew words and the link between them.\"},\n   {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter, p. (AKD.txt line 1019)\", \"stance\": \"supports\",\n    \"note\": \"Zimmern lists the Babylonian planet-gods behind the weekday names beginning “1) Šamaš” — the Akkadian member of the same Semitic sun-word.\"},\n   {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"no entry for shemesh/Shimshon; Jeffery covers only Qur'anic loanwords.\"}]),\n\n node(4, \"Greek\", \"Samson\", \"confirmed\",\n  \"The Septuagint rendered שִׁמְשׁוֹן as Σαμψών (Sampsṓn), the -ψ- being the Greek way of writing the Hebrew cluster \"\n  \"-mš- before -ōn and the ω rendering the Hebrew long ō. From the Greek Bible the form passed into the whole Christian \"\n  \"onomastic tradition; the chart's bare transliteration 'Samson' is the Hellenistic Greek Σαμψών. \"\n  \"(Strictly the Greek is Sampsṓn; Nourai's 'Samson' drops the psi's -p-, but that is a transliteration choice, not an error of substance.)\",\n  \"ترجمهٔ یونانی سبعینیه (سپتواژینت) نام عبری Šimšōn را به‌صورت Σαμψών آورده است؛ حرف ψ در یونانی \"\n  \"برای نمایش خوشهٔ صامتی -mš- به‌کار رفته و ω برابر واکهٔ بلند ō عبری است. از همین صورت یونانی است که نام به \"\n  \"سنّت مسیحی راه یافته است. ادعای نورایی درست است؛ تنها آوانگاری کتاب (Samson به‌جای Sampsōn) دقیق نیست.\",\n  [W_SAMSON],\n  [{\"ref\": \"KLN:1379\", \"status\": \"supports\", \"note\": KLN_SAMSON}],\n  [{\"src\": \"KLN\", \"where\": \"p.1379\", \"stance\": \"supports\", \"note\": \"“fr. Gk. Σαμψών, fr. Heb. Shimshōn” — the Hebrew→Greek step exactly as drawn.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict., s.v. Samson / Judges xvi\", \"stance\": \"supports\",\n    \"note\": \"WEB_vol1.txt line 72313 quotes Judges xvi.21 “The Philistines bound Samson with fetters of brass” — the English name is the biblical one transmitted through Greek and Latin.\"}]),\n\n node(5, \"Latin\", \"Samson\", \"confirmed\",\n  \"The Vetus Latina and Jerome's Vulgate took the Septuagint form over as Late Latin Samson, gen. Samsonis, \"\n  \"simplifying Greek -ψ- to -s- and shortening the Greek ω to o. Klein labels the immediate source of English \"\n  \"'Late L.', and this Late Latin form is the one from which all the Western European forms (Old French, Italian, \"\n  \"Spanish, German) descend.\",\n  \"لاتینی متأخّر (ترجمهٔ وولگات هیرونیموس) صورت یونانی Σαμψών را به Samson (مضاف‌الیه Samsonis) تبدیل کرد؛ \"\n  \"خوشهٔ -ψ- به -s- ساده شد و واکهٔ بلند ω کوتاه شد. تمام صورت‌های اروپای غربی از همین صورت لاتینی آمده‌اند. \"\n  \"ادعای نورایی درست است.\",\n  [W_SAMSON],\n  [{\"ref\": \"KLN:1379\", \"status\": \"supports\", \"note\": KLN_SAMSON + \" — Klein's 'Late L.' is Nourai's Latin node.\"},\n   {\"ref\": \"AHD\", \"status\": \"not_checked\",\n    \"note\": \"Nourai's AHD citations are to the 1975/76 American Heritage Dictionary main text; the only AHD text on disk is the Watkins 1985 Indo-European roots appendix, which has no Semitic proper names. The online IE-roots appendix likewise has nothing on Samson.\"}],\n  [{\"src\": \"KLN\", \"where\": \"p.1379\", \"stance\": \"supports\", \"note\": \"“Late L., fr. Gk. Σαμψών”.\"},\n   {\"src\": \"SKT\", \"where\": \"grep 'samson' in SKT.txt\", \"stance\": \"silent\",\n    \"note\": \"Skeat's Concise dictionary has no proper-name entries, so no independent word there.\"}]),\n\n node(6, \"French\", \"\", \"confirmed\",\n  \"A pass-through node with no word printed: French Samson, the ordinary French form of the biblical name \"\n  \"(and a common French surname), continues Late Latin Samson unchanged in spelling, with French stress and \"\n  \"the nasalised final syllable [sɑ̃.sɔ̃]. It is included only because the Persian name in node #7 came through French, \"\n  \"not from Hebrew or English.\",\n  \"این گره واژه‌ای نام‌برده ندارد و تنها حلقهٔ واسط است: فرانسوی Samson همان صورت لاتینی است که با تلفّظ \"\n  \"خیشومی فرانسه خوانده می‌شود. آوردن آن در نمودار فقط از آن روست که نام فارسی «سامسون» از راه فرانسه وارد شده است، \"\n  \"نه از عبری یا انگلیسی.\",\n  [W_SAMSON],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node.\"}],\n  [{\"src\": \"KLN\", \"where\": \"p.1379\", \"stance\": \"partial\",\n    \"note\": \"Klein traces English from Late Latin and says nothing about French; the French form is simply the Latin one.\"},\n   {\"src\": \"DEV\", \"where\": \"grep 'Samson' in DEV.txt\", \"stance\": \"silent\",\n    \"note\": \"Devic's dictionary of French words of oriental origin has no Samson: biblical names transmitted through the Vulgate were outside his scope.\"}]),\n\n node(7, \"Persian\", \"Sâmson\", \"plausible\",\n  \"Persian سامسون Sāmsōn as a male given name is a modern European borrowing, not a continuation of the Hebrew: \"\n  \"the long ā of the first syllable and the -ōn of the second reproduce the French pronunciation [sɑ̃sɔ̃] as rendered \"\n  \"in the 19th–20th-century Persian transcription of French names (Persian has no nasal vowels, so both nasals are \"\n  \"written out with ن). A direct loan from Hebrew or from the Arabic Islamic tradition would have given شمشون \"\n  \"Šamšūn, which is indeed the form used in Persian Bible translations — so the سامسون spelling really does mark the \"\n  \"European route Nourai draws. The chain itself is sound; only the specific reference could not be checked.\",\n  \"نام فارسی «سامسون» وام‌واژه‌ای اروپایی (از راه فرانسه) است و دنبالهٔ مستقیم صورت عبری نیست؛ \"\n  \"زیرا اگر از عبری یا از راه عربی آمده بود به‌صورت «شمشون» درمی‌آمد (چنان‌که در ترجمه‌های فارسی کتاب \"\n  \"مقدّس چنین است). الف کشیده و واو پایانی بازنمود تلفّظ خیشومی فرانسوی است. ادعای نورایی با احتیاط \"\n  \"پذیرفتنی است؛ منبع ارجاع‌شده (جلد ۵ فرهنگ معین، بخش اعلام) در دسترس نبود.\",\n  [W_SAMSON],\n  [{\"ref\": \"MON5:719\", \"status\": \"not_checked\",\n    \"note\": \"Mo'in vol. 5 is the a'lām (proper-names) volume; neither vajehyab nor abadis carries the a'lām volumes and no scan of vols 5–6 is on archive.org (only the 2-volume Adena abridgement, which omits proper names). Page 719 could not be opened.\"}],\n  [{\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt (2-vol. Adena abridgement)\", \"stance\": \"silent\",\n    \"note\": \"grep سامسون returns 0 hits — the abridgement drops the a'lām volumes entirely.\"},\n   {\"src\": \"KLN\", \"where\": \"p.1379\", \"stance\": \"partial\",\n    \"note\": \"Klein documents the Hebrew→Greek→Latin→(English) chain that stands behind the European name Persian borrowed, but says nothing about Persian.\"}]),\n\n node(8, \"English\", \"Samson; Sampson\", \"confirmed\",\n  \"Middle English Sampson, Sampsoun, Samson comes from Latin Samson (Vulgate), whence also the English surname; \"\n  \"the variant with -p- is an orthographic/epenthetic spelling that preserves the Greek psi (Σαμψών) or reflects the \"\n  \"regular English excrescent stop between -m- and -s- (cf. Thompson beside Thomson). Klein prints both, \"\n  \"with 'Sampson. — A var. of Samson.' as a separate headword — exactly the pair Nourai lists.\",\n  \"انگلیسی Samson از راه انگلیسی میانه Sampson/Sampsoun از لاتینی Samson آمده است. صورت Sampson \"\n  \"یا بازماندهٔ ψ یونانی است یا نتیجهٔ پیدایش صامت میانجی p میان m و s در انگلیسی (مانند Thompson در برابر \"\n  \"Thomson). کلاین هر دو صورت را آورده است؛ ادعای نورایی درست است.\",\n  [W_SAMSON],\n  [{\"ref\": \"KLN:1379\", \"status\": \"supports\", \"note\": KLN_SAMSON + \" Klein also has the separate headword “Sampson. — A var. of Samson.” (KLN_1966.txt line 33638).\"}],\n  [{\"src\": \"KLN\", \"where\": \"p.1379 (headwords 'Samson, Sampson' and 'Sampson')\", \"stance\": \"supports\",\n    \"note\": \"both chart forms are Klein headwords; Klein adds 'samson post' and 'samsonite' as further English derivatives.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict. (WEB_vol1.txt line 72313)\", \"stance\": \"supports\",\n    \"note\": \"quotes Judges xvi.21 for 'Samson', confirming the English name is the Vulgate/Authorized-Version one.\"}]),\n]\n\nout[\"entries\"].append(entry(\n 1, \"Š.m.š\", \"confirmed\",\n \"Proto-Semitic *śamš- 'sun' (triliteral š-m-š)\",\n \"The root box is right: Klein p.1379 and p.1430 reconstruct exactly this Semitic sun-word behind Akkadian \"\n \"šamšu/Šamaš, Ugaritic špš, Hebrew šemeš, Aramaic šimšā, Syriac šemšā and Arabic šams, and Wiktionary's \"\n \"Proto-Semitic entry gives *śamš-. The language label 'Semitic' and the gloss 'sun' are both correct. \"\n \"Klein's further guess that the base is ultimately *s-m-s-m 'to be swift' (of quivering sunrays) is his own \"\n \"speculation and is not needed for any arrow on this chart. The whole Samson branch (Hebrew → Greek → Latin → \"\n \"English/French → Persian) is uncontroversial; the only link that could not be documented is the Mo'in vol. 5 page \"\n \"for Persian سامسون.\",\n \"ریشهٔ سامی آغازین *śamš- «خورشید» (سه‌صامتی ش-م-ش) ریشه‌ای است کاملاً پذیرفته‌شده: اکدی šamšu، \"\n \"اوگاریتی špš، عبری šemeš، آرامی šimšā و عربی شمس همه از آن‌اند. برچسب زبانی (سامی) و معنای \"\n \"داده‌شده هر دو درست است. زنجیرهٔ شمشون (عبری ← یونانی ← لاتینی ← فرانسه/انگلیسی ← فارسی) نیز بی‌منازعه است؛ \"\n \"تنها صفحهٔ جلد ۵ فرهنگ معین برای «سامسون» قابل بررسی نبود.\",\n [W_SHAMS, W_SHEMESH, W_SAMSON],\n [{\"ref\": \"KLN:1379\", \"status\": \"supports\", \"note\": KLN_SAMSON}],\n [{\"src\": \"KLN\", \"where\": \"pp.1379 (Samson) and 1430 (Shamash)\", \"stance\": \"supports\",\n   \"note\": \"s.v. Shamash: “Akkad. shamash, shamshu, 'sun; the god of the sun', rel. to Heb. shemesh … Arab. shams (dissimilated fr. *shamsh), of s.m.; prob. from the Semitic base s-m-s-m, 'to be swift' (said of the quivering sunrays).”\"},\n  {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter (AKD.txt line 1019)\", \"stance\": \"supports\",\n   \"note\": \"“… nach den babyl. Göttern 1) Šamaš, 2) Sin, 3) Nergal …” — the Akkadian sun-god name of the same root.\"},\n  {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"Jeffery has no šams entry; the word is native Arabic, not a Qur'anic loan.\"}],\n e1_nodes))\n\n# ---------------------------------------------------------------- entry 2\ne2_nodes = [\n node(1, \"Persian\", \"san`at\", \"confirmed\",\n  \"New Persian صنعت ṣanʿat 'craft, industry' is Arabic صَنْعَة ṣanʿa 'craft, workmanship' (a form-I noun of \"\n  \"ṣanaʿa 'he made') borrowed with the tāʾ marbūṭa read as -at, the normal Persian treatment of Arabic feminines in \"\n  \"citation form. The whole derivational family printed on the chart is likewise Arabic morphology taken over whole: \"\n  \"مصنوع maṣnūʿ (passive participle I), مصنوعات (its Arabic broken/sound plural), تصنّع taṣannuʿ (verbal noun V), \"\n  \"صانع ṣāniʿ (active participle I). The modern sense 'industry' is a 20th-century semantic extension inside Persian.\",\n  \"«صنعت» وام‌واژه‌ای عربی است از صَنْعَة (مصدر/اسم از ریشهٔ صنع «ساختن») که با خواندن تای گرد \"\n  \"به‌صورت -at وارد فارسی شده است — همان رفتاری که فارسی با مؤنّث‌های عربی دارد. مشتقّات «مصنوع، \"\n  \"مصنوعات، تصنّع، صانع» نیز همگی صرف عربی‌اند. معین آن را با نشانهٔ [ع. صنعة] می‌آورد. معنای \"\n  \"«صنعت» به‌معنای امروزی (industry) تحول معنایی سدهٔ چهاردهم خورشیدی است. ادعای نورایی درست است.\",\n  [A_SANAT, W_SANAT, W_SINAA],\n  [{\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": \"Farhang-e Mo'in s.v. صنعت (abadis.ir): “(صَ عَ ) [ ع . صنعة ] (اِ. ) ۱ - فن، پیشه . ۲ - حیله، چاره .” — Mo'in explicitly derives the Persian word from Arabic صنعة, which is Nourai's arrow. (No page number is given in the chart.)\"},\n   {\"ref\": \"FVA:236\", \"status\": \"not_checked\",\n    \"note\": \"Nahvi, Farhang-e Vāžehā-ye ʿArabī dar Fārsī (1368/1989) has no digital copy: refs_online.json records a fresh 2026 search of archive.org, ketabnak, noorlib and the web with no result.\"}],\n  [{\"src\": \"MON\", \"where\": \"s.v. صنعت\", \"stance\": \"supports\", \"note\": \"“[ ع . صنعة ]” — Arabic ṣanʿa.\"},\n   {\"src\": \"ARY\", \"where\": \"grep صنعت in ARY_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur lists only Indo-European roots of Persian; Arabic loans are outside his scope.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n    \"note\": \"Asbaghi catalogues Persian words borrowed INTO Arabic; ṣanʿa runs the other way and is absent, which is itself confirmation that the direction on the chart (Arabic → Persian) is the accepted one.\"}]),\n\n node(2, \"Arabic\", \"dâr-as-sanâ`\", \"confirmed\",\n  \"Arabic دَار الصِّنَاعَة dār aṣ-ṣināʿa, literally 'house of manufacture', is a genitive compound of دار dār \"\n  \"'house' (Nourai's cross-reference ☞D.v.r) and صِنَاعَة ṣināʿa, the verbal noun of ṣanaʿa 'he made' — hence directly \"\n  \"from the root box. The article al- assimilates to aṣ- before the 'sun letter' ṣād, which is what produces the -s- \"\n  \"heard in all the European forms. From the 9th century on the term is the standard Arabic name of a state dockyard \"\n  \"(Ibn Jubayr uses it of Messina, Ibn Khaldūn of Tunis).\",\n  \"ترکیب عربی دار الصّناعة «خانهٔ ساختن» از دار «خانه» و صِناعة (مصدر صنع) ساخته شده است. الف‌ولام تعریف پیش از \"\n  \"حرف شمسی «ص» همگون می‌شود (al- > aṣ-) و همین سین/صاد است که در صورت‌های اروپایی بازتاب یافته است. این \"\n  \"ترکیب از سدهٔ سوم هجری نام رسمی کارخانهٔ کشتی‌سازی دولتی بوده است. ادعای نورایی درست است.\",\n  [W_ARSENAL, E_ARSENAL, W_SINAA],\n  [{\"ref\": \"KLN:108\", \"status\": \"supports\", \"note\": KLN_ARSENAL}],\n  [{\"src\": \"KLN\", \"where\": \"p.108 s.v. arsenal\", \"stance\": \"supports\", \"note\": \"“fr. dār, 'house', as-, assimilated form of al-, 'the', and ṣināʿah, 'construction, art', fr. ṣanaʿa, 'he made'.”\"},\n   {\"src\": \"LAM\", \"where\": \"pp.27–28 s.v. Arsenal, and p.95 s.v. Darse\", \"stance\": \"supports\",\n    \"note\": \"LAM.txt leaf 85 footnote: “Ne serait-il pas plus naturel de dériver darsena de دار صناعة dâr sanaʿa; comme dans ce passage d'Ibn-Djobair: « la ville de Messine possède un arsenal » … Ibn Khaldoun appelle de même l'arsenal de Tunis دار صناعة (Prol. I. 35).”\"},\n   {\"src\": \"DEV\", \"where\": \"p. (DEV.txt lines 539–543) s.v. Arsenal\", \"stance\": \"partial\",\n    \"note\": \"Devic accepts دار صناعة for Sp. atarazana and It. darsena, but argues French/Italian arsenal comes from aṣ-ṣināʿa alone, “simplement le mot ṣināʿa précédé de l'article”, without dār — a variant of the same root, so the root box is unaffected.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1290\", \"stance\": \"supports\",\n    \"note\": \"“[Aus ar. dār 'Haus', ṣināʿa 'Betriebsamkeit, Handwerk, Industrie'] 'Fabrik', besonders 'Waffenfabrik' und auch schon ar. 'Schiffsbauhaus' … Hieraus it. darsena, siz. tirzanà, arzanà, arsenale, terzana 'Zeughaus'; frz. darse, darsine, arsenal; sp. atarazana … engl. arsenal.”\"}]),\n\n node(3, \"Greek\", \"\", \"plausible\",\n  \"Empty pass-through node: the Medieval Greek form. Klein is the source of this step — he says Italian arsenale was \"\n  \"borrowed from the Arabic 'prob. through the medium of MGk. ἀρσηνάλης', a Byzantine Greek word for the Venetian/\"\n  \"Byzantine dockyard. The route is phonetically attractive because it explains the -r- of arsenal (Arabic dār-aṣ- \"\n  \"gives no r in that position), but it is not generally accepted: Etymonline and Wiktionary take Italian straight \"\n  \"from Arabic, and Devic and Lammens explain the -r- instead from the emphatic pronunciation of ṣād or from a \"\n  \"reminiscence of dār. So the node is Klein's hypothesis, not a documented Greek word-history.\",\n  \"این گرهٔ تهی، صورت یونانی میانه است. کلاین می‌نویسد که ایتالیایی arsenale «احتمالاً از راه یونانی میانهٔ \"\n  \"ἀρσηνάλης» از عربی گرفته شده است؛ این فرض وجود «r» در arsenal را توجیه می‌کند، امّا همگان آن را \"\n  \"نپذیرفته‌اند: ویکی‌واژه و اتیمانلاین ایتالیایی را مستقیماً از عربی می‌دانند و دویک و لامنس آن «r» را به تلفّظ \"\n  \"مفخّم صاد یا به بازماندهٔ «دار» نسبت می‌دهند. بنابراین این حلقه فرضیهٔ کلاین است و با احتیاط پذیرفتنی است.\",\n  [E_ARSENAL, W_ARSENAL],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node; the Greek step is Klein's (KLN:108, cited on the neighbouring nodes).\"}],\n  [{\"src\": \"KLN\", \"where\": \"p.108 s.v. arsenal\", \"stance\": \"supports\",\n    \"note\": \"“borrowed — prob. through the medium of MGk. ἀρσηνάλης — fr. Arab. dār-aṣ-ṣināʿah”; note Klein's own 'prob.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1290\", \"stance\": \"contradicts\",\n    \"note\": \"Lokotsch derives the Italian and Sicilian forms straight from Arabic and mentions no Greek intermediary at all.\"},\n   {\"src\": \"DEV\", \"where\": \"DEV.txt lines 539–543\", \"stance\": \"contradicts\",\n    \"note\": \"Devic explains the -r- from the emphatic ṣād or from dār and posits no Greek stage.\"}]),\n\n node(4, \"Italian\", \"darsena, arsenale\", \"confirmed\",\n  \"Italian darsena 'inner harbour basin' is the Arabic compound taken over whole (dār aṣ-ṣināʿa > darsana > darsena), \"\n  \"while arsenale (Old Italian arzanà, arzanale, Sicilian tirzanà, terzana) is the Venetian form in which the article \"\n  \"aṣ- was reanalysed as part of the stem and an -r- appeared. The word's home is the Venetian Arsenale, the state \"\n  \"shipyard founded in 1104, which Dante already names (Inferno XXI 7: 'Quale ne l'arzanà de' Viniziani'). \"\n  \"Both chart forms and the gloss 'naval dockyard' are correct.\",\n  \"ایتالیایی darsena «حوضچهٔ درونی بندر» همان ترکیب عربی دار الصّناعة است که یکجا وام گرفته شده، و arsenale \"\n  \"(ایتالیایی کهن arzanà، arzanale) صورت ونیزی است که در آن الف‌ولام تعریف جزء ستاک پنداشته شده و «r» نمودار \"\n  \"شده است. خاستگاه واژه کارخانهٔ کشتی‌سازی ونیز (سدهٔ ۱۲ میلادی) است که دانته نیز از آن یاد کرده است. \"\n  \"ادعای نورایی درست است.\",\n  [E_ARSENAL, W_ARSENAL],\n  [{\"ref\": \"KLN:108\", \"status\": \"supports\", \"note\": KLN_ARSENAL + \" Klein gives exactly Nourai's pair, arsenale and darsena.\"},\n   {\"ref\": \"LAM:95\", \"status\": \"supports\",\n    \"note\": \"Lammens p.95 (LAM.txt leaf 152) s.v. 'Darse': “Esp. et Cat: dársena. Cat. et Maj: drassana, drasena. It: darsena; de دار صنعة dār-ṣanʿa ou دار صناعة dār-ṣanāʿa.” The cited page is exact.\"}],\n  [{\"src\": \"KLN\", \"where\": \"p.108\", \"stance\": \"supports\", \"note\": \"“It. arsenale (OIt. arzanale), 'dock' … (whence also Sp. dársena and It. darsena, 'dock')”.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1290\", \"stance\": \"supports\",\n    \"note\": \"“Hieraus it. darsena, siz. tirzanà, arzanà, arsenale, terzana 'Zeughaus'”.\"},\n   {\"src\": \"LAM\", \"where\": \"p.95\", \"stance\": \"supports\", \"note\": \"see ref_check: Italian darsena from dār-ṣanāʿa.\"}]),\n\n node(5, \"English\", \"arsenal\", \"confirmed\",\n  \"English arsenal is first recorded c.1500 in the sense 'dockyard, dock with naval stores', taken from Italian \"\n  \"arzenale/arsenale — the Venetian Arsenale being what English travellers saw; the modern sense 'public place for \"\n  \"making or storing weapons and ammunition' is from the 1570s. Nourai's Italian → English arrow is exactly \"\n  \"Etymonline's and Wiktionary's account (some dictionaries route it through French arsenal, but the early English \"\n  \"nautical sense points to direct Italian contact).\",\n  \"انگلیسی arsenal نخستین بار حدود ۱۵۰۰ میلادی به معنای «کارخانه و لنگرگاه کشتی» از ایتالیایی arzenale \"\n  \"وام گرفته شده و معنای «زرادخانه» از دههٔ ۱۵۷۰ پدید آمده است. پیکان نورایی (ایتالیایی ← انگلیسی) همان \"\n  \"چیزی است که اتیمانلاین و ویکی‌واژه می‌گویند. ادعای نورایی درست است.\",\n  [E_ARSENAL, W_ARSENAL],\n  [{\"ref\": \"AHD\", \"status\": \"not_checked\",\n    \"note\": \"Nourai's AHD is the 1975/76 American Heritage Dictionary main text; the only AHD on disk is Watkins' 1985 Indo-European roots appendix (grep 'arsenal' returns nothing, as expected for a Semitic loan), and the 1970s AHD scans on archive.org are lending-restricted.\"}],\n  [{\"src\": \"KLN\", \"where\": \"p.108 s.v. arsenal\", \"stance\": \"supports\", \"note\": \"Klein's headword is the English word; its source is given as It. arsenale.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. arsenal (SKT.txt line 985)\", \"stance\": \"supports\",\n    \"note\": \"“arsenal … Span. arsenal … Cf. Ital. … Arab. dār ṣināʿat, place for making … Arab. dār, a house; ṣināʿat, trade, construction … Late L. arsenatum” (Skeat routes it through Spanish rather than Italian).\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1290\", \"stance\": \"supports\", \"note\": \"“Dtsch. Arsenal, ndl. arsenaal, engl. arsenal, russ. arsenal”.\"}]),\n]\n\nout[\"entries\"].append(entry(\n 2, \"S.n.`a\", \"confirmed\",\n \"Arabic root صنع ṣ-n-ʿ 'to make, manufacture' (ṣanaʿa)\",\n \"The root box is correct: صَنَعَ ṣanaʿa 'he made, manufactured' is a native Arabic triliteral, and both branches \"\n \"of the chart hang on it — the verbal noun صِنَاعَة ṣināʿa / صَنْعَة ṣanʿa 'craft' (whence Persian صنعت) and the \"\n \"compound دار الصّناعة (whence darsena/arsenale/arsenal). The only weak link on the chart is the Medieval Greek \"\n \"intermediary, which is Klein's conjecture and is rejected by Lokotsch and Devic. Nourai's own reference for the \"\n \"root (FVA:236) could not be consulted — the book has no digital copy — but Klein, Lammens, Devic, Lokotsch, \"\n \"Skeat, Etymonline and Wiktionary all agree on the substance.\",\n \"ریشهٔ عربی صنع «ساختن، پرداختن» ریشه‌ای اصیل و سه‌صامتی است و هر دو شاخهٔ نمودار از آن برمی‌آید: \"\n \"مصدر صِناعة/صَنْعة که وام‌واژهٔ فارسی «صنعت» از آن است، و ترکیب «دار الصّناعة» که از راه ایتالیا به \"\n \"darsena/arsenale و سپس arsenal انگلیسی رسیده است. تنها حلقهٔ سست نمودار، میانجی‌گری یونانی میانه است که \"\n \"فرضیهٔ کلاین است و لوکوچ و دویک آن را نمی‌پذیرند. منبع خود نورایی (FVA) نسخهٔ دیجیتال ندارد.\",\n [W_SINAA, E_ARSENAL, W_ARSENAL],\n [{\"ref\": \"FVA:236\", \"status\": \"not_checked\",\n   \"note\": \"S.M. Nahvi, Farhang-e Vāžehā-ye ʿArabī dar Fārsī (dakhīl), 1368/1989 — refs_online.json records that a 2026 re-search of archive.org, ketabnak, noorlib and the open web found no digital copy on any permitted platform.\"}],\n [{\"src\": \"KLN\", \"where\": \"p.108 s.v. arsenal\", \"stance\": \"supports\",\n   \"note\": \"“ṣināʿah, 'construction, art', fr. ṣanaʿa, 'he made'” — Nourai's root and gloss verbatim.\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1290\", \"stance\": \"supports\",\n   \"note\": \"“ar. ṣināʿa 'Betriebsamkeit, Handwerk, Industrie'”.\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir, Alfāẓ fārisiyya muʿarraba\", \"stance\": \"silent\",\n   \"note\": \"Addi Shir lists Persian words arabicised; ṣanʿa is not among them (grep الصناعة in AFM_pages.txt gives only incidental uses), confirming the word is Arabic in origin, not a Persian loan.\"}],\n e2_nodes))\n\n# ---------------------------------------------------------------- entry 3\ne3_nodes = [\n node(1, \"Avestan\", \"snâ; us-snâ\", \"confirmed\",\n  \"Bartholomae's AiW gives the Avestan verb snā- 'waschen' (present stems snāδa-, snaya-/*snya-, PPP snāta-, \"\n  \"inf. snātōe) with the very preverb Nourai prints: 'mit us ″aus-, abwaschen″: us tanūm snayasta …' \"\n  \"(Vd. 5.54), and the noun usnātay- f. 'Abwaschung' (AiW col. 408, Komp. us- + snātay-) from Vd. 8.98. \"\n  \"The verb is the Iranian continuant of PIE *(s)neh₂- 'to swim, flow' (Skt. snāti, snāyate 'bathes'); Avestan has \"\n  \"specialised it to 'wash, purify by rinsing', the ritual sense familiar from the Vendīdād purification chapters. \"\n  \"us- here is the preverb 'up, out' (Nourai's ☞Ud 1), giving 'wash off, wash out'.\",\n  \"بارتولومه در فرهنگ ایرانی باستان فعل اوستایی snā- «شستن» (ستاک حال snaya-، اسم مفعول snāta-) را آورده و \"\n  \"همین فعل را با پیشوند us- «بر، بیرون» در وندیداد ۵؛۵۴ (us tanūm snayasta «تن را بشوید») و در اسم \"\n  \"usnātay- «شستوشو» (ستون ۴۰۸) نشان داده است. این فعل دنبالهٔ ریشهٔ هندواروپایی آغازین *(s)neh₂- \"\n  \"«شنا کردن، روان بودن» است (سنسکریت snāti) که در اوستایی معنای آیینی «شستن و پاک کردن» یافته است. \"\n  \"ادعای نورایی درست است.\",\n  [W_SHENA, W_OSHNAN],\n  [{\"ref\": \"POK:971\", \"status\": \"supports\", \"note\": POK_971},\n   {\"ref\": \"KLN:1030\", \"status\": \"supports\", \"note\": KLN_NATATION},\n   {\"ref\": \"HUB:15\", \"status\": \"supports\",\n    \"note\": \"Hübschmann, Persische Studien p.15 (HUB.txt leaf 25, note 89): “… mit dem es auf ap. *usnāna- = zd. *usnāna- (vgl. zd. uš-snā ″waschen″ und wegen šn für sn: ap. vašna = zd. vasna u. ähnl.) zurückgehen könnte.” The cited page is exact and it prints Nourai's very form uš-snā.\"}],\n  [{\"src\": \"BRT\", \"where\": \"AiW col. ~1698 (BRT.txt leaf 887) s.v. snā-, and col. 408 s.v. usnātay-\", \"stance\": \"supports\",\n    \"note\": \"“j. snā- V. 'waschen'. Praes. 18 snāδa; 27 snaya-, *snya-. — PPfP. snāta-; Inf. snātōe … mit us 'aus-, abwaschen': us tanūm snayasta us *γāsirā … V.5.54”; and “j. usnātay- f. 'Abwaschung' … Komp.: us- + snātay-”.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. (AHD_watkins1985.txt line 965) s.v. snā-\", \"stance\": \"supports\",\n    \"note\": \"“snā-. To swim. Contracted from *snaə-. … [Pok. snā- 971.]”\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 692\", \"stance\": \"supports\",\n    \"note\": \"“snā- ″fließen, Feuchtigkeit″ … av. snāyeite ″wäscht, reinigt durch Spülen″, Ptc. snāta-” (WLD_Bd2_pages.txt line 45962 ff.).\"}]),\n\n node(2, \"Persian\", \"šenâ; ošnân\", \"confirmed\",\n  \"شنا šenā 'swimming' continues Middle Persian šnāz [šnʼc] 'swimming', šnāzīdan 'to swim' (MacKenzie), from Old \"\n  \"Iranian *snā- with the regular Persian change of initial sn- to šn- (Hübschmann §: 'wegen šn für sn: ap. vašna = \"\n  \"zd. vasna'); Horn no. 792 still records the older spelling sinā, sināh beside šinā, and the variants šināv/šināb, \"\n  \"which he refers either to the type daryāw or to the u-stem *snau-. اُشنان ošnān 'saltwort, the alkaline plant \"\n  \"(Salsola/Seidlitzia) burnt for washing-soda', Borhān's “کیاهی باشد که بدان رخت شویند … و آنرا بعربی غاسول خوانند”, \"\n  \"is a *snāna- 'washing(-herb)' with a preverb; Hübschmann p.15 posits Old Persian/Avestan *us-snāna- — precisely \"\n  \"Nourai's us-snā — correcting de Lagarde's *aiwiš-šnāna- which Horn had reported. Wiktionary agrees that the \"\n  \"Persian is 'more easily explainable from *uc-' while the Armenian loan awšnan points to *Habi-; the preverb is \"\n  \"therefore disputed, but the parent root and the arrow as drawn are not. The word passed on into Arabic as \"\n  \"أُشنان ʾušnān and into Armenian awšnan/ošnan.\",\n  \"«شنا» از فارسی میانه šnāz «شنا کردن» (مکنزی) و از ایرانی باستان *snā- است؛ sn- آغازین در فارسی به šn- \"\n  \"بدل می‌شود (هوبشمان: مانند ap. vašna در برابر zd. vasna). هرن (شمارهٔ ۷۹۲) هنوز صورت کهن sinā/sināh را در \"\n  \"کنار شنا می‌آورد. «اُشنان» گیاه قلیایی است که برای شستن جامه به کار می‌رفته (برهان قاطع: «بعربی غاسول \"\n  \"خوانند») و از *snāna- «شوینده» با پیشوند ساخته شده است؛ هوبشمان (ص ۱۵) آن را *us-snāna- می‌داند — دقیقاً همان \"\n  \"چیزی که نورایی رسم کرده — در برابر *aiwiš-شنانهٔ دو لاگارد که هرن نقل کرده بود. پس در پیشوند اختلاف هست، \"\n  \"امّا در ریشه نیست. این واژه به عربی (أُشنان) و ارمنی (awšnan) نیز راه یافته است. ادعای نورایی درست است.\",\n  [W_SHENA, W_OSHNAN, A_SHENA],\n  [{\"ref\": \"BQT:1298\", \"status\": \"partial\",\n    \"note\": \"Borhān-e Qāṭeʿ vol. 3: the شنا entry with Mo'in's etymological footnote stands on the leaf the v3 page-map calls printed p.1294 (pdf page 85): “شنا … معروف است که شناوری و آب ورزی باشد” with the footnote “شناب / شناو … اوستایی … هندی باستان snā (استحمام کردن)، استی … axšoun / axšoin (شستن) … ورک: هوبشمان ۷۹۲”. The exact page Nourai cites, 1298 (pdf page 89), carries شمشاد–شمشیر in this scan; the page-map is interpolated from 34 anchors over 721 pages, so a ±4-page drift is likely and the content is unmistakably the one cited. Substance supported, page number not exactly reproducible.\"},\n   {\"ref\": \"HRN:176\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p.176 (HRN.txt leaf 197), no. 792: “sinā, sināh 'Schwimmen', sinār, sinārīden. aw. √snā, us snayaeta 'sich waschen'; ai. √snā-, snāti 'sich baden' … np. š ist im Satzsandhi oder durch Übertragung entstanden.” The cited page is exact and Horn even prints the us- compound.\"},\n   {\"ref\": \"AEF:118\", \"status\": \"not_checked\",\n    \"note\": \"Khaleqi Motlaq's Asās-e Ešteqāq-e Fārsī (the Persian version of Horn+Hübschmann) is not online; refs_online.json marks it 'catalog' with no scan. Its German original (HRN) was checked instead and supports the claim.\"}],\n  [{\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict., s.v. šnāz (PHD.txt line 585)\", \"stance\": \"supports\",\n    \"note\": \"“šnāz [šnʼc | (N šinā(w))] swimming. šnāzīdan, šnāz- [šnʼc-ytnʼ | M šnʼz-, (N šināw-)] swim.” — the missing Middle Persian link between Avestan snā- and NP شنا.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien pp.15 and 253–254\", \"stance\": \"supports\",\n    \"note\": \"p.254: “ušnan 'Seifenkraut' == zd. *usnāna- aus us + snāna- (oben p.15)”, and “Über sinā, āšnā 'Schwimmen' siehe oben p.81”.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 89 (p.21) and no. 792 (p.176)\", \"stance\": \"partial\",\n    \"note\": \"For اشنان Horn (no. 89, p.21) reports de Lagarde's “aw. *aiwiš-šnāna-” and adds the footnote “Die Awestaform ist von de Lagarde falsch angesetzt, der die Lautverhältnisse verkennt” — so Horn doubts the preverb but not the root; Hübschmann's us- (Nourai's choice) is the correction.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 1, leaf 357 s.v. اشنان\", \"stance\": \"supports\",\n    \"note\": \"“اشنان … کیاهی باشد که بدان رخت شویند و بعد از طعام خوردن دست نیز بدان بشویند و آنرا بعربی غاسول خوانند و چون آنرا بسوزانند اشخار شود” — confirms Nourai's gloss 'an alkaline plant used in washing'.\"},\n   {\"src\": \"MON\", \"where\": \"s.v. شنا (abadis text of Mo'in and Dehkhoda)\", \"stance\": \"supports\",\n    \"note\": \"Dehkhoda: “شنا. [شِ] (اِ) شناوری و آب‌ورزی باشد. (برهان) … شناه. شناب …” with the Labībī and Khāqānī verses — the variants Horn lists.\"},\n   {\"src\": \"ARY\", \"where\": \"grep شنا / SNA in ARY_pages.txt and ARY_latin_index_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur has no entry for شنا or اشنان (hits are only آشنا 'acquainted' and SNAW 'snow').\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n    \"note\": \"the glossary covers the texts he edits and has šnāxtan, šnāyišn etc. but no šnāz.\"}]),\n\n node(3, \"Greek\", \"něsos\", \"disputed\",\n  \"Greek νῆσος (Doric νᾶσος) 'island' is real and correctly glossed, but the attachment to *snā- is the weak point of \"\n  \"this chart. The traditional analysis — Brugmann, Solmsen, Walde-Pokorny II 692, Pokorny 971, Klein p.1030, \"\n  \"Buck 1.25 — takes it as 'the swimmer, that which floats', from *snā- with the Greek loss of initial s- before a \"\n  \"nasal; but that very loss is the problem, since Greek normally does NOT preserve the -s- of the stem in this \"\n  \"position. Watkins in the AHD appendix Nourai cites already downgrades it: 'Attributed by some to this root \"\n  \"(but more likely obscure)'. Modern handbooks reject it outright: Etymonline s.v. Chersonese says 'traditionally \"\n  \"from PIE root sna- ″to swim″, but this is now generally rejected', quoting Beekes that νῆσος 'is probably an \"\n  \"Aegean loan'; Wiktionary heads the etymology 'Uncertain', offering either the *snā- link, a derivation from \"\n  \"*néh₂s 'nose' ('headland, cape'), or Furnée's Pre-Greek origin.\",\n  \"یونانی νῆσος (دوریک νᾶσος) «جزیره» واژه‌ای واقعی است، امّا پیونددادن آن به ریشهٔ *snā- سست‌ترین حلقهٔ این \"\n  \"نمودار است. تحلیل سنتی (بروگمان، زلمزن، والده‌پوکورنی ۲/۶۹۲، پوکورنی ۹۷۱، کلاین ۱۰۳۰، باک ۱؛۲۵) \"\n  \"آن را «شناکننده، آنچه بر آب می‌شناود» می‌داند، امّا از میان رفتن s آغازین در این جایگاه در یونانی قاعده‌مند \"\n  \"نیست. خود واتکینز (همان AHD که نورایی ارجاع می‌دهد) می‌نویسد «برخی آن را به این ریشه بسته‌اند، ولی به احتمال زیاد \"\n  \"مبهم است». پژوهش امروزی (بیکس، اتیمانلاین، ویکی‌واژه) آن را رد می‌کند و νῆσος را وام‌واژه‌ای اژه‌ای \"\n  \"(پیشایونانی) می‌داند، یا آن را به *néh₂s «بینی، دماغه» می‌بندد. پس این حلقه را باید مورد منازعه شمرد.\",\n  [W_NESOS, E_POLY],\n  [{\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 965) s.v. snā-: “3. Attributed by some to this root (but more likely obscure) is Greek nēsos, island: CHERSONESE.” The reference does list nēsos under snā-, but explicitly flags it as doubtful — the chart draws it as a plain descent.\"}],\n  [{\"src\": \"POK\", \"where\": \"Pokorny 971–972 s.v. snā-\", \"stance\": \"supports\",\n    \"note\": \"“νῆσος, Doric νᾶσος 'island' as 'Schwimmer'” — Pokorny accepts it without reservation.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 692\", \"stance\": \"supports\",\n    \"note\": \"“νῆσος, dor. νᾶσος 'Insel' als ″Schwimmer″ (s. Brugmann BSGW 1899, 212 f. …; nach Solmsen Beitr. I 244 mit dem fruchtbaren gr. Formans -σο-)”.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 1.25 'ISLAND', p.29\", \"stance\": \"partial\",\n    \"note\": \"“1. Grk. νῆσος, Dor. νᾶσος, prob. : νήχω 'swim', Lat. nare 'swim', Skt. snā- 'bathe', etc. Walde-P. 2.692” — Buck's 'prob.' already hedges.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dict. p.1234 s.v. snātos (2)\", \"stance\": \"partial\",\n    \"note\": \"“(ambig. also in) Alb. not 's wimming' and in Gk. nēsos, f. 'island' … Doric nāsos” — Mann marks the Greek form 'ambiguous'.\"},\n   {\"src\": \"KLN\", \"where\": \"p.1030 s.v. natation\", \"stance\": \"partial\",\n    \"note\": \"“and prob. also Gk. νῆσος, Dor. νᾶσος, 'island' (for *νᾶσος, lit. 'that which swims')” — again only 'prob.'\"}]),\n\n node(4, \"English\", \"Polynesia; Indonesia\", \"confirmed\",\n  \"Both are 19th-century learned coinages on Greek νῆσος. Polynésie was coined in 1756 by Charles de Brosses \"\n  \"(Histoire des navigations aux terres australes) from πολύς 'many' + νῆσος, latinised as Polynesia in English in \"\n  \"1758, and restricted to the eastern Pacific by Dumont d'Urville in 1832. Indonesia was coined c.1850 — J. R. Logan, \"\n  \"Journal of the Indian Archipelago 4 (1850) p.254, adopting G. W. Earl's suggestion — from Ἰνδός + νῆσος, \"\n  \"Logan writing that he 'would gladly see all the nesias wiped off the map'. Klein lists both under 'natation' among \"\n  \"the words containing νῆσος. The edge nēsos → Polynesia/Indonesia is beyond doubt; only the further step up to \"\n  \"*snā- (node #3) is disputed.\",\n  \"هر دو واژه ساختهٔ عالمانهٔ سدهٔ نوزدهم‌اند و بر پایهٔ یونانی νῆσος ساخته شده‌اند: Polynésie را شارل دو بروس \"\n  \"در ۱۷۵۶ از πολύς «بسیار» + νῆσος ساخت (در انگلیسی ۱۷۵۸) و دومون دورویل در ۱۸۳۲ معنای آن را محدود کرد؛ \"\n  \"Indonesia را حدود ۱۸۵۰ جی. آر. لوگان از Ἰνδός + νῆσος برساخت. پیوند این دو با νῆσος قطعی است؛ تنها \"\n  \"پلهٔ بالاتر (پیوند νῆσος با *snā-) مورد منازعه است.\",\n  [E_POLY, W_POLY, E_INDO, W_INDO],\n  [{\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"the chart gives no reference for this node; Klein p.1030 (cited on node #1) in fact names both words.\"}],\n  [{\"src\": \"KLN\", \"where\": \"p.1030 s.v. natation\", \"stance\": \"supports\",\n    \"note\": \"“Cp. also … neso-, … the second element in chersoneso- and in Indonesia, Melanesia, Micronesia, Polynesia.”\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. snā-\", \"stance\": \"partial\",\n    \"note\": \"lists CHERSONESE as the English derivative of nēsos but not Polynesia/Indonesia.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls / Webster\", \"stance\": \"silent\",\n    \"note\": \"no dedicated etymological entry found for Polynesia/Indonesia in the volumes on disk.\"}]),\n]\n\nout[\"entries\"].append(entry(\n 3, \"Snâ\", \"confirmed\",\n \"PIE *(s)neh₂- (Pokorny snā-, snə-(t-), snāu-) 'to flow, swim; wet'\",\n \"Root, language label and gloss are all correct, and Nourai's POK:971 is exact: Pokorny's lemma \"\n \"'snā-, snə-(t-), snāu-, sn-eu-, sn-et-', meaning 'to flow, swim; damp, nymph of waters', occupies pp.971–972, \"\n \"with Walde-Pokorny II 692 ff. and Watkins' 'snā-. To swim' behind it. The Iranian branch (Av. snā- 'wash' → MP \"\n \"šnāz → NP شنا, اشنان) is solid and well documented by Bartholomae, Horn, Hübschmann, MacKenzie and Mo'in's \"\n \"footnotes in Borhān-e Qāṭeʿ. The Greek branch is not: νῆσος 'island' is attached to this root only by the older \"\n \"literature (Brugmann, Solmsen, Pokorny, Klein, Buck), while Watkins already calls it 'more likely obscure' and \"\n \"Beekes/Etymonline/Wiktionary now treat it as a Pre-Greek or Aegean word — so node #3 is marked disputed and \"\n \"node #4 (Polynesia, Indonesia) is confirmed only as a descendant of νῆσος itself.\",\n \"ریشهٔ هندواروپایی آغازین *(s)neh₂- (در پوکورنی snā-) «روان بودن، شنا کردن، نم‌ناک» درست است و \"\n \"شمارهٔ صفحهٔ نورایی (۹۷۱) نیز دقیق است. شاخهٔ ایرانی — اوستایی snā- «شستن»، فارسی میانه šnāz، \"\n \"فارسی نو «شنا» و «اشنان» — به گواهی بارتولومه، هرن، هوبشمان، مکنزی و حواشی معین بر برهان قاطع استوار است. \"\n \"امّا شاخهٔ یونانی چنین نیست: پیوند νῆσος «جزیره» با این ریشه تنها در ادبیات کهن پذیرفته شده و امروز \"\n \"بیکس و دیگران آن را وام‌واژه‌ای پیشایونانی می‌دانند؛ از این‌رو گرهٔ ۳ «مورد منازعه» نشان شده است.\",\n [W_SHENA, W_NESOS, E_POLY],\n [{\"ref\": \"POK:971\", \"status\": \"supports\", \"note\": POK_971}],\n [{\"src\": \"POK\", \"where\": \"Pokorny 971–972, lemma snā-\", \"stance\": \"supports\",\n   \"note\": \"“Meaning: to flow, swim; damp, nymph of waters”; material opens with “Old Indic snāti, snāyate 'badet (sich)' … Avestan snāyeite 'washes, purifies'”.\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 692–693\", \"stance\": \"supports\",\n   \"note\": \"“snā- 'fließen, Feuchtigkeit'. Ai. snāti, snāyate 'schwemmt, badet (sich)', ptc. snātá-, av. snāyeite 'wäscht, reinigt durch Spülen' …”\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. snā- (AHD_watkins1985.txt line 965)\", \"stance\": \"supports\",\n   \"note\": \"“snā-. To swim. Contracted from *snaə-. 1. Extended form *snəgh- in Greek nékhein … [Pok. snā- 971.]”\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dictionary pp.1233–1234 (snāiō – sneu-)\", \"stance\": \"supports\",\n   \"note\": \"“snātos (2) 'swimming; flow, float; (3) washed, clean' … Av. cf. snā-, v. 'wash' beside snad-, id.; snāθrom, n. 'washing'”.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 1.25 'ISLAND', p.29\", \"stance\": \"partial\",\n   \"note\": \"cites the root for νῆσος but with 'prob.'; Buck has no separate 'swim' heading tied to Iranian.\"}],\n e3_nodes))\n\np = \"/home/sfmqrb/git/rishe/data/verification/page-461.json\"\nwith io.open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"wrote\", p)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-461.py"
}
```


### [2026-09-14T02:57:01.011Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-461.json
```


## [2026-09-14T02:57:03.406Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-461.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 461"
}
```


### [2026-09-14T02:57:04.635Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 14, 'plausible': 2, 'disputed': 1}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 13, 'partial': 3, 'not_checked': 8}
books consulted: {'supports': 32, 'silent': 11, 'partial': 8, 'contradicts': 2} | by book: {'KLN': 14, 'MON': 4, 'LKT': 4, 'ARY': 3, 'DEV': 3, 'FVQ': 2, 'WEB': 2, 'SKT': 2, 'LAM': 2, 'AHD': 2, 'WLD': 2, 'RCH': 1, 'AKD': 1, 'PLA': 1, 'BRT': 1, 'PHD': 1, 'HUB': 1, 'HRN': 1, 'BQT': 1, 'NYB': 1, 'POK': 1, 'SYN': 1, 'IEC': 1, 'FSD': 1}
```


## [2026-09-14T02:57:24.479Z] AGENT

Done. `verify_check.py 461` reports 17/17 nodes, 0 PROBLEM lines.

**Page 461 (book p. 431) — 3 entries (entry 0 = redirect `Smerd → Mer 2`, skipped), 17 nodes**

- Root verdicts: 3 confirmed. Node verdicts: **14 confirmed, 2 plausible, 1 disputed**.
- Ref checks: 13 supports, 3 partial, 8 not_checked. Books consulted: 32 supports, 8 partial, 2 contradicts, 11 silent.

Disputed / weak items:
- **Snâ · #3 Greek `něsos` "island" — disputed.** The link to *snā- survives only in the older literature (Pokorny 971, Walde-Pokorny II 692, Klein p.1030 "prob.", Buck 1.25 "prob.", Mann "ambig."). The very reference Nourai cites, Watkins/AHD, already says "attributed by some to this root (but more likely obscure)"; Beekes/Etymonline ("now generally rejected") and Wiktionary ("Uncertain") treat νῆσος as a Pre-Greek/Aegean word or a derivative of *néh₂s "nose, headland". Node #4 (Polynesia, Indonesia) is confirmed only as a descendant of νῆσος itself.
- **S.n.`a · #3 Greek (empty node) — plausible.** The Medieval Greek ἀρσηνάλης intermediary is Klein's own conjecture ("prob. through the medium of"); Lokotsch no. 1290 and Devic derive Italian straight from Arabic and explain the -r- otherwise.
- **Š.m.š · #7 Persian `سامسون` — plausible.** The European (French) route is right in substance — a Hebrew/Arabic-mediated loan would have given شمشون — but Mo'in vol. 5 (a'lām) p.719 is not digitised anywhere, so the reference itself is unchecked.

Notable ref findings: Nourai's page numbers are unusually accurate here — KLN:1379 (Samson), KLN:108 (arsenal), KLN:1030 (natation, which also names Indonesia/Polynesia), POK:971, HUB:15 (uš-snā), HRN:176 (no. 792 sinā/sināh), LAM:95 (Darse) all hit the exact printed page. Two could not be opened at all (FVA:236 and AEF:118 have no digital copy anywhere).

One near-miss worth recording: **BQT:1298** — in the Borhān vol. 3 scan the شنا entry with Mo'in's Avestan footnote sits at the page the page-map calls 1294 (pdf 85), while 1298 (pdf 89) carries شمشاد–شمشیر. The v3 page-map is interpolated from 34 anchors over 721 pages, so this is most likely map drift rather than a bad citation; marked `partial` with both readings noted.

No extraction errors: the JSON matches the chart and the printed page throughout; no `transcription_suspect` nodes, so no page images were needed. The only cosmetic point is that the Greek node in entry 1 is transliterated "Samson" where the Greek is Σαμψών (Sampsṓn) — Nourai's own simplification, noted in the derivation, not a data problem.
