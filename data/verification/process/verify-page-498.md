# Verification process log — verify-page-498


## [2026-09-14T03:08:59.615Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 498 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-498.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-498.json. Write /home/sfmqrb/git/rishe/data/verification/page-498.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 498` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:09:00.569Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:09:01.352Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:09:01.366Z] TOOL RESULT

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


## [2026-09-14T03:09:01.922Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-498.txt"
}
```


### [2026-09-14T03:09:01.957Z] TOOL RESULT

```
1	=== PDF page 498 (book page 468) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Teku 1, Tekw : to run, flow  (refs POK:1059)
4	#1 (parent #0) [Avestan] refs=POK:1059; BQT:503 | tak, taka, tač : to run ; tačaiti : runs
5	  #2 (parent #1) [Persian] refs=BQT; MON:5176; IEC:1372 | tâxtan «تاختن» : to ride fast ; tâzîdan «تازیدن ( تازان ، تازیانه )» : to ride fast ; takîdan «تکیدن ( تک ، تکاپو ، تکاور )» : to run ; ham-tak «هم تک ، هم تگ» : road companion
6	#3 (parent #0) [Avestan] refs=BQT:380; HRN:66 | pairi-tak : to run around ☞Per 1
7	  #4 (parent #3) [Persian] refs=None | pardâxtan «پرداختن ( پرداز )» : to pay, to do, to attend
8	#5 (parent #0) [Avestan] refs=BQT:128; HRN:27 | ham-tač, ham-tak : to throw ☞Sem 1
9	  #6 (parent #5) [Persian] refs=None | andâxtan «انداختن» : to throw, measure, think ; andâzeh «اندازه» : size
10	  #7 (parent #5) [Pahlavi] refs=None | handâčak : throw, measure
11	    #8 (parent #7) [Arabic] refs=None | 
12	      #9 (parent #8) [Persian] refs=BQT:2379; HRN:27 | hendeseh «هندسه» : science of "size measurements" ; mohandes «مهندس» : engineer
13	#10 (parent #0) [Avestan] refs=POK:1059 | vi-taxti : to melt (run apart) ☞Wi
14	  #11 (parent #10) [Persian] refs=NYB:217; BQT:1777 | godâxtan «گداختن» : to melt | NOTE: Compare with derivations from root "Dhogh:to heat"
15	#12 (parent #0) [Avestan] refs=POK:1059 | tačar : road ; tačan : haste, hurry ; tahra : swift
16	  #13 (parent #12) [None] refs=None |  | NOTE: box is printed entirely blank in the source (outlined box, no header text or content)
17	#14 (parent #0) [Old Persian] refs=POK:1059 | taxša : a type of bow & arrow
18	  #15 (parent #14) [Persian] refs=BQT:476 | taxš «تخش» : bow and arrow
19	#16 (parent #0) [Greek] refs=AHD:1545 | toxon : bow and arrow
20	  #17 (parent #16) [Latin] refs=AHD:1359 | toxicum : poison for arrows
21	    #18 (parent #17) [English] refs=None | toxic
22	--- entry 1 ---
23	ROOT Teku 2 -> redirect to Tex
24	--- entry 2 ---
25	ROOT Tekw -> redirect to Teku 1
26	
```


## [2026-09-14T03:09:04.425Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-498.json | head -200",
 "description": "Read source JSON for page 498"
}
```


### [2026-09-14T03:09:04.495Z] TOOL RESULT

```
{
  "pdf_page": 498,
  "book_page": 468,
  "entries": [
    {
      "root": {
        "name": "Teku 1, Tekw",
        "lang": "Indo-European",
        "refs": "POK:1059",
        "gloss": "to run, flow"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1059; BQT:503",
          "words": [
            {"translit": "tak, taka, tač", "gloss": "to run", "script": null},
            {"translit": "tačaiti", "gloss": "runs", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT; MON:5176; IEC:1372",
          "words": [
            {"translit": "tâxtan", "gloss": "to ride fast", "script": "تاختن"},
            {"translit": "tâzîdan", "gloss": "to ride fast", "script": "تازیدن ( تازان ، تازیانه )"},
            {"translit": "takîdan", "gloss": "to run", "script": "تکیدن ( تک ، تکاپو ، تکاور )"},
            {"translit": "ham-tak", "gloss": "road companion", "script": "هم تک ، هم تگ"}
          ],
          "note": null,
          "quote": {
            "text": "ما و مجنون بره بادیه هم تگ بودیم - قدمی چند زهمراهی ما دور افتاد",
            "poet": "Sharîf"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:380; HRN:66",
          "words": [
            {"translit": "pairi-tak", "gloss": "to run around", "script": null, "see": ["Per 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "pardâxtan", "gloss": "to pay, to do, to attend", "script": "پرداختن ( پرداز )"}
          ],
          "note": null,
          "quote": {
            "text": "به جنگ زمین سربسر تاختی - کنون به آسمان نیز پرداختی",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:128; HRN:27",
          "words": [
            {"translit": "ham-tač, ham-tak", "gloss": "to throw", "script": null, "see": ["Sem 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "andâxtan", "gloss": "to throw, measure, think", "script": "انداختن"},
            {"translit": "andâzeh", "gloss": "size", "script": "اندازه"}
          ],
          "note": null,
          "quote": {
            "text": "نباید سخن گفت ناساخته - نشاید بریدن نینداخته",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "handâčak", "gloss": "throw, measure", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Arabic",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT:2379; HRN:27",
          "words": [
            {"translit": "hendeseh", "gloss": "science of \"size measurements\"", "script": "هندسه"},
            {"translit": "mohandes", "gloss": "engineer", "script": "مهندس"}
          ],
          "note": null,
          "quote": {
            "text": "یکی در ز آهن برو ساخته - مهندس بر آنگونه پرداخته",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1059",
          "words": [
            {"translit": "vi-taxti", "gloss": "to melt (run apart)", "script": null, "see": ["Wi"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "NYB:217; BQT:1777",
          "words": [
            {"translit": "godâxtan", "gloss": "to melt", "script": "گداختن"}
          ],
          "note": "Compare with derivations from root \"Dhogh:to heat\"",
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1059",
          "words": [
            {"translit": "tačar", "gloss": "road", "script": null},
            {"translit": "tačan", "gloss": "haste, hurry", "script": null},
            {"translit": "tahra", "gloss": "swift", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": null,
          "refs": null,
          "words": [],
          "note": "box is printed entirely blank in the source (outlined box, no header text or content)",
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:1059",
          "words": [
            {"translit": "taxša", "gloss": "a type of bow & arrow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "BQT:476",
          "words": [
            {"translit": "taxš", "gloss": "bow and arrow", "script": "تخش"}
          ],
          "note": null,
          "quote": {
            "text": "همه بنده در پیش رخش منند - جگر خستهٔ تیغ و تخش منند",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Greek",
```


## [2026-09-14T03:09:05.192Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T03:09:05.236Z] TOOL RESULT

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


## [2026-09-14T03:09:21.913Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '200,300p' data/extracted/batch/page-498.json; echo ===; ls data/verification/ | head -30; echo ===; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "Rest of JSON and sample output format"
}
```


### [2026-09-14T03:09:22.983Z] TOOL RESULT

```
Exit code 1
          "lang": "Greek",
          "refs": "AHD:1545",
          "words": [
            {"translit": "toxon", "gloss": "bow and arrow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Latin",
          "refs": "AHD:1359",
          "words": [
            {"translit": "toxicum", "gloss": "poison for arrows", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "toxic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Teku 2",
        "redirect": "Tex"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Tekw",
        "redirect": "Teku 1"
      },
      "nodes": []
    }
  ]
}
(eval):1: == not found
```


## [2026-09-14T03:09:23.680Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nr=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','HRN','NYB','MON','AHD','IEC']:\n    print(k, json.dumps(r.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Ref online info for cited abbreviations"
}
```


### [2026-09-14T03:09:24.771Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open
```


## [2026-09-14T03:09:27.665Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:2500])\n\"",
 "description": "Sample verification output format"
}
```


### [2026-09-14T03:09:28.612Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
  "https://en.wiktionary.org/wiki/pectus"
 ],
 "ref_check": [
  {
   "ref": "POK:792",
   "status": "partial",
   "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. peg-",
   "stance": "supports",
   "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit p
```


## [2026-09-14T03:09:28.937Z] TOOL CALL #8: Bash

```json
{
 "command": "awk 'BEGIN{RS=\"\\f\"} NR==1067' data/verification/sources/refs/POK_01.txt | head -80",
 "description": "POK page 1059 (leaf = p+8)"
}
```


### [2026-09-14T03:09:29.925Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:09:34.790Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json\nr=json.load(open('data/verification/sources/refs_online.json'))\nprint(r['POK']['page_offset']); print(r['POK'].get('lookup_hint'))\nprint('---BQT'); print(r['BQT']['page_offset']); print(r['BQT'].get('lookup_hint'))\nprint('---HRN'); print(r['HRN'].get('lookup_hint'))\nprint('---NYB'); print(r['NYB']['page_offset'])\nprint('---IEC'); print(r['IEC']['page_offset'])\nprint('---AHD'); print(r['AHD'].get('page_offset'), r['AHD'].get('lookup_hint'))\n\"",
 "description": "Page offsets"
}
```


### [2026-09-14T03:09:36.781Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
---BQT
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
---HRN
Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
---NYB
Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---IEC
TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---AHD
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
```


## [2026-09-14T03:09:40.790Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'lemma: tek' POK_full.txt | head -20; echo ===; grep -n 'Page(s): 1059' POK_full.txt | head",
 "description": "Find Pokorny tek- root"
}
```


### [2026-09-14T03:09:40.855Z] TOOL RESULT

```
Exit code 1
84963:Root / lemma: tek-1 
84986:Root / lemma: tek-2 
85013:Root / lemma: tek-3 
85088:Root / lemma: tek"- 
(eval):1: == not found
```


## [2026-09-14T03:09:42.150Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'te\\(k\\|q\\)u̯-' POK_03.txt | head -20",
 "description": "grep tekʷ in POK_03"
}
```


### [2026-09-14T03:09:42.209Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:09:44.352Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '85085,85160p' POK_full.txt",
 "description": "Pokorny tekʷ- entry"
}
```


### [2026-09-14T03:09:44.418Z] TOOL RESULT

```
1; Specht Indo Germanic Dekl. 239 f., Leumann Kratylos 1, 29. 
Page(s): 1058-1059 

Root / lemma: tek"- 

Meaning: to run; to flow 

Material: Old Indie takti^ hurries, schieftt dahin', takta-, /a/r^- "hurrying, rash, hasty', takva- 

ds.; aKa//r^-"herabflieftend'; Avestan tacaiti' running, hurries; flows ', participle -taxta-, np. 

taxtan'run', hantac/na- ^zusamrr\eni\\eQ>end' (= Lithuanian tekinas^ running '), Avestan vi- 

taxt'h f. "das Zerflieften, Schmelzen' (= Inf. Slavic *tekti)\ here perhaps as 



'dahinschieftend': iran. (skyth.) *tahsa- {npers. taxs) "arrow, bow', from which gr. to^ov ds., 
Latin taxus^ yew' (Benveniste Mel. Boisacq 1, 37 ff., Mayrhofer 1, 467 f.); 

Avestan taka- m., np. /a/r'run, flow' (= Lithuanian takas, Slavic tokh); Avestan tacar- n. 
"run, flow, pathway', /5da/7- "hurrying'; /ad/'-ap- "running water (containing)', iran. *tahra- 
"quick, fast'; 

alb. /7oye/r" pursue'; 

Maybe alb. ndjej^ smell, perceive, feel (the hunt?)', ndjenje^ feeling '.' 

Old Irish techid^ flees ' (Perf. o-grade taich), ateoch^ beg ' {*ad-tek"'d^{ake meine 
Zuflucht'); brit. PN Vo-tepo-rTx, mcymr. ^oo'ep "Zufluchf, /©it'e/ "escape'; bret. tec'hetl\ee', 
mcymr. 3. Sg. Konj. /7y/y-o'e'c/7c»'wer nicht flieht' (brit. c/7from ks, s-Subjunktivstamm); 
Irish intechu. "way' ( *enitek"om, compare Old Church Slavic tekh "run, flow'); 

Gothic A'/^s "servant, farmhand' (= Old Indie takva-, actually " runner', compare Latvian 
teksn/s ^ Auiwarter, Bedienter'), Proto Norse A'eM/5/?"Lehensmann', Old English deofiA^), 
Old High German deo^ farmhand, servant', Fem. Gothic f^/m, Old Icelandic Ay, f^Ir, Old 
Saxon fh/m, thiu. Old English deowu, deowe{n). Old High German diu, diuwa' bondmaid, 
maid ' ( *tek-uT, development moviertes Fem. to *teku6-s, or to *tek'u-s. Old Indie taku-)\ 
with derivative as Gothic widuwairna^ orphan ' *t^ewerndn\v\ Old Icelandic ^erna' slave ', 
Old Saxon thiorna. Old High German diorna "virgin'. Modern High German Dime; n- 
extension in Old English deowen' bondmaid ', Old Icelandic ^yo/7/7 "servant', whereof 
*l=>ewandn^ serve ' in Old Icelandic t^ena, t^jdna. Old High German dionon, dionen^ serve 
'; Gothic a/7aA'/M/5/7 "subjugate, zum Sklaven machen'. Old English deowian. Old Icelandic 
Pjads.; lengthened gradees collective Gothic t^ewisau. PI. "servant, Knechte' {*tekueso-)\ 

Lithuanian teku, -et/^run, flow, rinnen; aufgehen (from the sun); marry (from the wife, 
woman)', Latvian teku, tecet \un'; Old Prussian tackelis, Lithuanian tekelas, Latvian teciels 
m. "grindstone, whetstone'; Lithuanian /e/r/77e"wellspring, river', //o/ra " estuary'; Latvian 
teksn/sm. "Bedienter'; Old Church Slavic tekg, test/" rpexeiv ', serb. tecem, /ec/"flow', etc.; 
Lithuanian takas^ path, track ', Latvian taks6s., Lithuanian Jtakas' estuary '; Old Church 
Slavic tokb ' puaiq ', potokh " x£iMC(PPO<; '; Tocharian B cake "river'; Hittite ua-tku-zi 
"springf. 

References: WP. I 715 f., Trautmann 316 f., Vasmer3, 89, 113 f., Mayrhofer 1, 466 f. 
Page(s): 1059-1060 



Root / lemma: telegh- 
Meaning: to hit 

Material: Old Indie tarh- {trnedhi, Perf. tatarha, participle trdha-) "shatter, crunch '; 
Lithuanian 5^-/a/z//"durchprugeln', /5/iy//"thrash', /e/z// "thrash, throw'; Latvian talzTt, talstTt 
"durchprugeln"; with zweisilbiger root form Lithuanian telezi-ju, -y//"vast, grand 
durchprijgeln', talazuoti^ babble, chatter ' (meaning as Modern High German Klatschen), 
talazius " babbler '. 

References: WP. I 741, Mayrhofer 1, 522; 
See also: compare under telek-. 
Page(s): 1 062 

Root / lemma: telek- 

Meaning: to push, hit 

Note: only Celtic and baltoslavisch
```


## [2026-09-14T03:09:57.007Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD Watkins tekw\"; grep -n -A25 '^tek[ʷw\"]*-' AHD_watkins1985.txt | head -60; echo \"=== AHD grep teku\"; grep -n 'toxic\\|toxon\\|tek*ʷ' AHD_watkins1985.txt | head -20",
 "description": "AHD Watkins tekw root"
}
```


### [2026-09-14T03:09:57.085Z] TOOL RESULT

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/b6jstd4oy.txt

Preview (first 2KB):
=== AHD Watkins tekw
1073:tek-. To beget, give birth to. 1. Suffixed form *tek-no-, child, in: a. Germanic *thegnaz, boy, man, servant, warrior, in Old English thegn, freeman, nobleman, mili- tary vassal, warrior: THANE; b. possibly Germanic *the- wern6, girl, in Old High German thirona, diorna (> German Dirne), girl: DIRNDL. 2. Reduplicated form *ti-tk-, metathesized in Greek tiktein, to beget, and suffixed o-grade form *tok-o- in Greek tokos, birth: OXYXTOCIC, POLyTocous, TocoLocy. [Pok. 1. tek- 1057.]
1074-teks-. To weave; also to fabricate, especially with an ax; also to make wicker or wattle fabric for (mud-covered) house walls. 1. Latin texere, to weave, fabricate: TEXT,
1075-TISSUE; CONTEXT, PRETEXT. 2. Suffixed form *teks-/é in:
1076-69
1077-temp-
1078-a. Latin téla, web, net, warp of a fabric, also weaver’s beam (to which the warp threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in Old High German dahs (> German Dachs), badger but more likely borrowed from the same pre- Indo-European source as the Celtic totemic name Tazgo-, Gaelic Tadhg, “‘badger’”): DACHSHUND. [Pok. tekth- 1058.] tekv-. To run, flee. Suffixed o-grade form *tokv-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, bow, also (in the plural) bow and arrow (< “that which flies’): Toxic. [Pok. tekz- 1059.] tel-. Ground, floor, board. 1. Germanic *thil-j6- in Middle Low German and Middle Dutch dele, plank: DEAL?. 2. Suffixed form *tel-n- in Latin tellii
...
</persisted-output>
```


## [2026-09-14T03:09:59.598Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd1 715\"; grep -n 'tek.u̯-\\|teku̯-\\|tequ-' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head; echo \"=== KNT taxs\"; grep -n 'taxš\\|taxsa\\|tak-\\|tač' KNT_full.txt | head -20",
 "description": "WLD and Kent"
}
```


### [2026-09-14T03:09:59.689Z] TOOL RESULT

```
=== WLD Bd1 715
45147:entw. moviertes Fem. zu *teqiw-s , oder zu *tequ-s : ai. tdkn-h ); mit Abl. 
=== KNT taxs
3547:taxsacd. 
5073:in Elam. $t-18-Sa-an-tak-ma (the tr of АКК, &- 
5081:OP Arta-zšaçã, Elam. îr-tak-ša-aš-ša, Akk. ar-ta- 
5082:ak-Sa-as-su (Vases b and c; ar-tak-Sat-su in 
5857:lazi- ‘be active’, pres. ha-taxšalaiy (see Lex., 
10796:imf. hamataxsaiy hamataxíatà hamatazsa"td, 
11430:ham-adárayavy, ham-ataxsary, patiy-axrSayaiy. 
11473:bata, ham-ataxsatd, dyasatd, |a|h[yat]à, adalrayat|a, 
12701:taxsalaty anu-dim [ha]kartahyà avaéd-dim pariba- 
14396:vaušahyā Artaxsagahya XShyà puça Artaxšaçahyű 
14483:taxsatary anu-dim |hajkartahya avaba-dim pariba- 
16734:68 m : patiyübaram : vasnà : Auramazdáha : ima : adam : akunavam : adam : hamataxsaty : 
21630:2 ürayavaufahyü : Artaxšaçāhyā : XShya : 
21631:puça : Artaxsagahyà : Xšayārcahyā : XShya : 
21669:adam : Artaxšaçā : XS : vazraka : XS XSyani : 
21685:1 : Haxamanisiya : дану : Artaxsaga : 
21709:1 adam : Artaxšaçā : XS : vazraka : XS : 
21712:Нахаташ&уд. бабу. : Artaxšaçā : XŠ : 
21743:3 hyà : XShy& : puça : Artaxšaðrahyā : 
21795:5 & : hya : Artaxšaçām : XSm : akunaug : ai
```


## [2026-09-14T03:10:14.484Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN leaf 87 (p.66)\"; awk 'BEGIN{RS=\"\\f\"} NR==88' HRN.txt | head -60",
 "description": "Horn p.66"
}
```


## [2026-09-14T03:10:15.443Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN leaf p.27\"; awk 'BEGIN{RS=\"\\f\"} NR==49' HRN.txt | head -60",
 "description": "Horn p.27"
}
```


### [2026-09-14T03:10:15.462Z] TOOL RESULT

```
=== HRN leaf 87 (p.66)
— m —
np. per7' soll auch *Blatt' bedeuten, wie ai. parnd- ;
vgl. ebenso g. par^ kurd. per, af;'. pur, bei. pan (442),
wa;^. paU^ sar. porÄ-, si/n. />arjr (aus "^parnaka-).
294. /mr Voll'.
aw. perena- Voll*; phlv. pur; ai. pmrid-,
LW. kurd. afy. bei. (210) pyr, wa/. sar. pur 'voir.
Ich sehe nicht ein , weshalb auch Geiger, Laut-
lehre des BalücT, np. piir 'v o 1 V statt von aw. perena-^
ai. pfirnd' VolF von ap. pan^-, aw. pouru-, ai. puni-
Viel' ableitet, deren Bedeutung nicht passt. Laut-
lich mussten ja allerdings beide Worte schon im
Pchlevr zusammenfallen , aber pur 'viel' ist hier
bereits aufgegeben. Wenn der Kommentar z. B. aw.
pouru.mahrku' mit pnrmarg wiedergiebt, so hat er
voll Tod\ nicht 'viele tödtend' gemeint ; denn anderen-
falls hätte er rasmarg übersetzen müssen.
295. perfuf enden zerstreuen; erschrecken, pergenden,
phlv. pargantan (Bund.).
ap. "^para -\~ y/kan- (?). Der Bedeutungswechsel ist
allerdings sehr auffällig. Vergl. efgenden (No. 103).
296. pertew 'Glanz*.
para j- ^fap-^ vergl. np. fäßen (No. 372).
297. perdayten 'ausführen, ausleeren; streben, sich be-
mühen* ; Praes. ,perdazem.
phlv. parda/tan (AV.).
aw. *para + l^tac-; Bedeutungswechsel wie bei
end (Ixten (No. 117). Die np. Bedeutung 'ausleeren'
lässt sich aus 'weglaufen lassen' erklären.
von Stackeiberg (briefl. Mitteilung) vergleicht
oss. t. fäldä/jn 'wenden' (ZDMG. 41, 574 Anm. 3),
dessen Bedeutung sich mit der von V^tac- {-\- pard)
unschwer vermitteln lässt.
298. perest 'Verehrer , verehrend*, perestTde7i , perestür^
perestis.
```


### [2026-09-14T03:10:16.456Z] TOOL RESULT

```
=== HRN leaf p.27
— 27 —
arab. LW. hinzamn 'Menschenmenge' (de Lagaide,
Armen. Studien, No. 1235).
115. en^lden zerschneiden, zerstückeln', Praes. enjln-em,
ap. *Aam + [/cay- (aw. und ai. 'zusammenlegen,
ansammeln etc.') ; phlv. ancUan bezw. han- , anj-
^krümmen, zusammenziehen (Bund.).
Zu dem Bedeutungs Wechsel vergl. np. ciden 'sam-
meln; schneiden'.
116. end *so viel, einige'; vergl. endek, endi, bes]end.
phlv. and 'so, so viel', andak Venig',
kurd. hind 'so viel', hindik 'wenig'.
Vom Pronominalstamm er-, aber nicht gleich aw.
avant-, phlv. havand, vd. 15 (48).
117. endäyiten * werfen', Praes. endäz-em, endaz 'Plan,
Absicht', endüze 'Mass'.
phlv. andäytan 'werfen'; sinnen* (Bund.), andäcak
*Mass', andäöUan erwägen , ermessen', andäc(i)sn
'Meinung ; arm. LW. amiacem 'überlegen', arab. LW.
muhandis 'Feldmesser', hmdasat 'Geometrie' u. a. m.
(de Lagarde, Arm. Stud., No. 116).
aw. hqm + {/^tac- ; Bedeutungswechsel wie auch bei
np. perdä/ten (No. 286).
118. endäm 'Körper, Glied'.
aw. hondäma- 'Glied' ; phlv. andäm, arm. LW. andam.
119. {i)ender 'm\ vergl. enderün,
ap. a(n)tar 'in, innerhalb'; aw. antare; phlv. andar^);
ai. antdr; arm. vergl. ender/c, ^nterk 'Eingeweide'
(H. No. 109).
Steht enderün für enderän (zu ün für an vergl. gerdün
No. 904), wozu man z. B. Sahn. I, 61 Vers 525 ver-
gleiche 2)? Vergl. jNTD, Ps. 68, 7, 8 (Grill).
120. {2)'ender in peder\euder {ped]ender), mader]ender
{mäd\ender)^ beräder]ender, /'aher]ender etc. 'Stief-'.
skr. antard' 'anderer, verschieden von'; osset. ändär
'andere, fremd' (20); got. anpar; lit. antras.
^) Phlv. andarg ist Unsinn.
') Das Pehlevi hat auch schon andarün (für aw. aw/ara-).
```


## [2026-09-14T03:10:34.942Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB p.217 (leaf 225)\"; awk 'BEGIN{RS=\"\\f\"} NR==226' NYB_vol2_glossary.txt | head -60",
 "description": "Nyberg p.217"
}
```


### [2026-09-14T03:10:36.003Z] TOOL RESULT

```
=== NYB p.217 (leaf 225)
ul ~ the flaming up, the shining forth, of the dawn 44!?,
lyaxšitan to grow 40". — Av. (1337 sq.) Iyaxs-, v. also varšišn.
2vaxSitan to flame, to blaze 1%, — Av. (1338) *vaxš- ‘to sparkle’ (of fire), ‘to spurt’ (of water); MPrth was ‘to be kindled, blaze’ (MHC); v. ?vax$, vaxšiš- néh, vaxsénitan.
vaxš-var [whšwl] prophet 1115. — ‘Bearer of the Word, or the (divine) message’, v. lvaxš.
vaxšvarčh prophethood 454-7,
vāyēndak [w'yndk'] flying creature, pl. cas. obl. —-än, enumerated after murvān 802. — Pres. pt. of Av. (1356) Wvay- ‘to fly’.
vizčnitan [w’cynytn'] to bring, to take a p. to a place (andar) 49?’; to lead (a horse) up to (0) a p. 5413-15; à tē pat ulēh ul vāzēnēm we shall carry thee up in the air 60%. — Caus. of väzitan.
vāzēnītār one who draws, pulls: asp i rahy ~ a chariot-horse 581”.
vāzišn v.n. of vāzītan (g. v.), pred. 1211’: dast + vat nē ~ it is necessary not to play the game badly.
vazitan [wcytn'] to travel, to ride: tē... ké vazäh [subju. 2nd p. sg. = ind.] pat vài i dérang-x"atà$ thou ... who ridest on the long-dominating Wind 9914-15, — Av. (1386) vaz-; MPrth. pres. wz- ‘to blow’ of the wind’, ‘to move, to go’ (MHC); Ghilain 52.70, cf Verbum 170; Paz.
Vaz-var
vazidan (Aog.); NP vazidan, bazidan ‘to blow’. V. also vaz-var.
vazitan [w’cytn'] caus. of the preceding v., to move: 1. trans. catrang — to play at chess 11915, 121%, — 2. intrans. to travel, to ride (= vazitan) 519-14. 6019, — Cf MPrth pdw’z ‘suite, followers’, pres. prw’z- ‘to cause to fly’, Ghilain 70; NP bazidan, büxtan ‘to play; to fly’.
vazr [wzl] mace 851%, — Av. (1392) vazra-; Paz. vazr(a); NP gurz; also, with meta- thesis, varz (q. v.).
"| vazurg [LB”, Prth RB’; wewrg, inscr.
welk-] great, big, high, lofty, passim; regularly placed before its head w., seldom: after (41?. 724); in titles great, chief: ~ framatar (g. v.); ~ šahridar (q.v.); — subst., pl. cas. obl. ~-dn the magnates HajA:6 [RB’n]. B:6 [welk’n]. 42. 1133, 16? [wewlg'n'], v. Christensen, Sass. 100. 110sq. — OP vazrka-; MPrthPrs wzrg; Arm. lw. vzurk, vzork, vzruk; Paz. guzurg, guzarg; NP buzurg. No comp. and sup.; for these forms meh, mahist are used; v.s. v. mas.
vazurgakän [LB’-k’n'] pl. cas. obl. of vazurg: (0) Col xakan u ~ to the Khakan of C. and his magnates 11323. — Cf váspuhr : lydspuhrakan (g. v.).
vazurgēh [wewlgyh, LB’-yh] greatness 517.26, size 151.
vazurg-kunišn [LB’ kwnšn'] of great achievements, executor of grand achieve- ments; pl. cas. obl. —-än 1068.
Vazurg-mihr [wewlgmtr'] n. pr. the fa- mous Grand Vizier of Khösröi I (531— 579): 118-121.
vazurg-späs [LB? sp’s] of lofty service, performing high duties, pl. cas. obl. —-än 106!, v. späs.
| vazurg-x"arrah [LB’ GDH] of great glory,
of Yam 44%.
vaz-var [wcwl] safe for traffic: puhl 4 ~ 1147. — V. vazitan,
www.parsianjoman.org | ool wok
vecak
208
vét-varéh
[vēcak [wyck'] lot, share, portion ; combat (as if it were a casting of lots between the combatants): rasnik ~ pitched battle FrP 14; v. nem-vecak. — From !vertan; Arm. lw. vičak ‘lot (e. g. in casting of lots), portion; position; fate, possession, dio- cese’; Ps. wyc ‘priest’, wycyhy �
```


## [2026-09-14T03:10:36.645Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC leaf 701\"; awk 'BEGIN{RS=\"\\f\"} NR==702' IEC.txt | grep -n -i 'tek\\|tok\\|tak' | head -30; echo \"--- headers\"; awk 'BEGIN{RS=\"\\f\"} NR==702' IEC.txt | head -5",
 "description": "Mann IEC col 1372"
}
```


### [2026-09-14T03:10:37.805Z] TOOL RESULT

```
=== IEC leaf 701
11:sphéros (2) ‘dashing, violent’. Cf. sphelos, spheio. (Skt. ambig.). WP II, 656 Skt. spharáh, adj. (2) “loud, strong, vehement: cf. phalah, m. ‘leap’; Tokh. A cf. spar- (a bird); Ir. cf. spéir, f. (2) ‘liveliness’; Li. spērùs, adj. ‘lively’; Latv. cf. spérigs, adj. ‘pugnacious’
--- headers
helós, adj. (vigo- rous’: OCS spélü ‘mature’: Cz. do-spély *adult) (Hes.); OCS spéjo, -ati, v. “further, prosper’; — se ‘thrive’; Li. spēju, su-speju, inf. speti, -spëti “have time; mature; succeed'; Latv. spēju, spēt, v. ‘be able’; spēja, f. ‘power, ability’; spējš, adj. “sudden
sphēlos ‘strong, vigorous’. Cf. sphéros, spheio. (Skt. ambig.) Skt. (ambig.) spharáh, adj. ((2) “loud, strong’, fr. *sphel- or *sphér-); cf. also phàálah, m. ‘leap’; Hes. spheélós, adj. ‘vigorous, agile; W ffil, m. ‘dash, rush’; OCS spëlú, adj. ‘ripe, mature’; Cz. do-spély, adj. tadult
sphén- ‘chip, wedge’. (Variant sphån- ?) Gk. sphén, gs. As, m. (^wedge'. Doric not recorded); MHG spàn, sm. ‘chip’; ON spánn, pl. spænir, & spónn, pl. spoenir, m. (“chip; target; spoon’, cf. OE spón, m. ‘chip’ and Eng. spoon); Sw. spån, m. ‘chip; shingle-board'; Fris. spoen, id.
spher-, see sper-, etc.
spheris, sphern- “heel; ankle Olr. & Ir. seir, dual: di-pherid, f. (heel. For *sph- cf. sine ‘teat’, cpds. -phne); W ffern, pl. au f. 'ankle-bone'; Ir. cf. speir, f. id. (and "bock"
```


## [2026-09-14T03:10:45.990Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB leaf 236\"; awk 'BEGIN{RS=\"\\f\"} NR==236' NYB_vol2_glossary.txt | tail -20; echo \"###\"; grep -n 'vitä\\|vitāx\\|vitax\\|gudäx\\|gudax\\|vitaxtan' NYB_vol2_glossary.txt | head -20",
 "description": "Nyberg witāxtan"
}
```


### [2026-09-14T03:10:47.065Z] TOOL RESULT

```
=== NYB leaf 236
216
vitartan
MPrs w(y)šwb- (A-H II), Verbum 184; Paz. vašēftan vaščv- (Mx, SGV); NP kusüftan kusüf- ‘to scatter, to dissolve’. The original labial at the end of the st. is uncertain: Skr ksubh- ‘to tremble, to be excited’, OIr *xsaub- or *xsaup- (*xšauf- probably through influence of the pt. "xašufta- < "ašupta-).
višūtak [wšwtk'] progeny, brood, of Ahrimanic beings, pl. cas. obl. —-ān 7622. 77°. From
višūtan to produce progeny, to breed, of Ahrimanie beings 7678, 777. — vi + Av. (1782) šhav-; Paz. vašūdan.
vitarg [wtlg] narrow passage 48?5-?6; pass, defile 8713 (pl. <-hā).!-19; path 201$, 76°. — < *vitar-ka-, v. next w.; Pas. vadarg ; cf. MPrs wdr (A-H II).
vitartan [wtltn'], viturtan [wtwltn'], vi- taštan [wtštn'], vitir- [wtyl-] to pass: andar dašt bē vitart passed over the plain 318; pat kustak + deh vitart passed outside the village 619-17; to pass by 7!1.15.22; bē vitast drove ahead 71’; to cross a bridge 7225.27; to go through a stream 101%. 10323; kë vitīrēndv the passers-by 12815; — pt. vitart, viturt deceased: vitart coll. the deceased 837. 8413; viturtān martūmān 10517. — Av. (640) vi-tar- = OP; MPrth w(y)drdn w(y)dr- (S, MHC); MPrs pres. wdyr- (S); Ps. pt. wilty, pres. wtyl-, wtl-; Paz. vadardan vadirdan, pres. vadar-, va- der-, vadir-; NP guöastan guóar-. Verbum 206, Ghilain 57.
vitārēnītan [wt'lynytn'] to cause a p. to take a p. away from: Kat-Xēūsrēt ke hac vài i dérang-x"atà& vitārēnēi K. whom he (Saošyant) will take down from the Long- dominating Wind (who had been trans- formed into a camel on which K. is riding, v. 9911-1002) 1065.
vitirtan [wt'ltn'] 1. caus. of vitartan, to cause to pass: dātār han i Zartuxst zx'"arrah tar mätist ārak 6 Zartuxst vitārt the Creator sent Z.’s x“arrah (g. v.) down
www.parsianjoman.org | ool wok
vitartan
to Z. through the line of his maternal grandmother 3619-11, cf 3817-18, — 2. intens. of vitartan: vitartan % Cinvat puhl to cross the Ch. bridge 64!?; the arrow ditikar sok bé vitärt pierced through to the other side 371, pat pušt be vitārēt (pres. hist.) pierced through and came out through the back 292-3, pat dil be vitārēt penetrated into the heart 2521-22, — MPrthPrs wyd’rdn w(y)d’r-; MPrs also pt. wd’$, Verbum 192; NP guöärdan or guöästan, guóür-.
vitávane (inscr. Prth) [wt’wny] shooting range HajA:1 = Prs tigrähy (g.v.); FrP 25 = vindak-vitav (g. v.). - < vi + *tavana- from tav-, v. s. v. tuvām; as to the ending -é v.s. v. Site.
vitāxtak [wt'htk'] molten 101?9. 1022. 108%, from
vitaxtan vitdc- trans. to melt: bé witäcet 10177, — Caus. of vi + Av. (624 sq.) tak-; MPrth wdxtn, wdc- and wd’c- (MHC), Ghilain 50; MPrs. wdc- (8), Verbum 169; Paz. vadáxtan vadāž- (SGV); NP gudāx- tan gudäz- ‘to liquify’.
vitir [wtyly] thoroughfare F: 6.
vitirän pt. of vitartan, passing away: hac gētē ~ bavend 12071.
vitirišn perishableness, corruptibility 66°.
vitīrišnēh det. v. n.: bē ~ the passing away, decease 6516-17, 7412-13,
vitist
###
1004:rarudenc; patron. Prth 1. 28 = Prs 1. 24 bythškn, Gr. v. rırıdıyav; Paikuli = KZS. Arm. lw. bdeašx (Hübschmann, AG 119 sg.). Georg: Armazi bilinguis (Nyberg, Eranos 44, 1946, 228-243; 233 sqq.) bthš, Gr v. nırıadEng also on gems found there (l.c.; v. also Eränsahr 169), Armazi “Aram.” inscr. (Altheim & Stiel, FuF 35, 1961, 172-178) pyihš; native K art'veli patiaxsi, pitiaxši (Hübschmann, Tschen- keli). Syr. lw. ptahšā, ptakša (often faultily vocalized), aftakšā (Hoffmann, Auszüge p. 34 n. 275). Amm. Marc. XXIII, 6: 14 vitaxae (“id est magistri equitum"), Gr. Hesych. Btorač, read Birač. In dealing with its etymology the indigenous form bythš should; as a matter of course, be given preference before any deviating forms in foreign languages. In its oldest form it is, however, found in Arm bdea&r < *bdiaxs: -d- must be secondary (an original d would have given 7) and go back to a f, voiced because of its proximity to the preceding b, which consequently must be the original initial consonant, not p (pt- would have re- mained); this phonetic state is cogently conclusive in favour of an original form "bitiyaxši-. The first element is *bitīya- ‘the second’, NW form of "dvitiya; Av. (963 sg.) bitya-, MPrth. bdyg (Nyberg, l. e. 237 n. 2; Henning, Iranistik 62 n. 2); the second element has been explained by Pagliaro (RSO XII, 1929, 164 sqq.) as *axsi- ‘eye’ (in Av. derivatives, v. also apaxš); *bītīya-axši- ‘the second eye’ of the King, based on the idea, well attested by the classical authors. and well ana- lysed by P., of the King’s officials as his “eyes”. Thus any etymology starting from initial ptt- is peremptorily excluded; pit- for bit- must be due to a secondary development in the borrowing languages. Pagliaro, l.c. 160-168; Eilers IIJ V, 1962, 209 sq. (quotes Armazi pythé, but ignores bihš!); Benveniste, Titres 65; Rundgren, OrSu XII (1963), 1964, 89-98 (oh!); ete.
3643:šītē (Prth) [Syty] a cairn HajA: 7.9.10. 13 = Prs citak with Prth §- for c-, v. s. v. šihr. — The ending -é here and in vitävane (q. v.) is probably spurious, at all events not known from other Prth. nouns (ākasī, g. v., is a special case) nor explicable from a Prth. point of view. Most probably the Sass. redactor of the inscription simply took over his habitual Prs. spell- ing of substantives with a silent final -y.
3769:täxtan [t’htn'] tāc- [t’c-] to run 319. 2819, 9817. — Av. täcaya- intens. of tak-, v. tacitan; NP tartan tüz-; v. also vitāxtan.
4169:[vindak [wndk'] shot, in ~ vitav [wtw'] shooting range, explained by vitävan (g. v.) FrP 25. — Evidently from the pres. stem of vistan (q. v.) which is not attested elsewhere in phonetic spelling].
4245:to Z. through the line of his maternal grandmother 3619-11, cf 3817-18, — 2. intens. of vitartan: vitartan % Cinvat puhl to cross the Ch. bridge 64!?; the arrow ditikar sok bé vitärt pierced through to the other side 371, pat pušt be vitārēt (pres. hist.) pierced through and came out through the back 292-3, pat dil be vitārēt penetrated into the heart 2521-22, — MPrthPrs wyd’rdn w(y)d’r-; MPrs also pt. wd’$, Verbum 192; NP guöärdan or guöästan, guóür-.
4247:vitāxtak [wt'htk'] molten 101?9. 1022. 108%, from
4248:vitaxtan vitdc- trans. to melt: bé witäcet 10177, — Caus. of vi + Av. (624 sq.) tak-; MPrth wdxtn, wdc- and wd’c- (MHC), Ghilain 50; MPrs. wdc- (8), Verbum 169; Paz. vadáxtan vadāž- (SGV); NP gudāx- tan gudäz- ‘to liquify’.
5389:täcaya-: täxtan tafnah-, tafnu-: täp (vi-)tak-: vitäxtan taka-: tak taxma-: tahm tanu-: tan tanu.pereda-: tanā- puhrak l taoš-, tusa-: tuhīkēh
6159:wde-: vitāxtan
6840:vadaxtan, vadaž-: vitäx- tan
7164:gudäxtan, gudäz-: vitäx- tan
```


## [2026-09-14T03:10:47.875Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC tek\"; grep -n \"^tek\\|^tok\\|tek[u\\\"ʷ]*-, v\\|teku- \" IEC.txt | head -20",
 "description": "Mann tekw entry"
}
```


### [2026-09-14T03:10:47.931Z] TOOL RESULT

```
=== IEC tek
18269:tek- (2) (teko, tekmi) “run, flow'. (Var: teks-). WP I, 715 Skt. tákami, tákmi, v. ‘rush, hurtle'; Av. tak-, tac-, v. ‘run, flow’; (variant in) Oss. tàxín, v. ‘fly’; Per. tàxtan, inf. ‘gallop; attack’; Tokh. B. cf. cake, n. ‘river’; Alb. cf. f-tíkem, v (‘run dry', fr. *apo-tek-); (variant) Mlr. techim, Ir. teichim, v. “tun, flee? and in Br. techi, inf. id.; OCS teko, testi, v. ‘flow’; OCz. teku, teci, v. ‘gallop; flow’; Li. tekù, éti, v. ‘run, hurry, flow’; Latv. teku, tecēt, v. ‘flow; leak, run’. Long- gde-in Per. tāxtan beside tāzīdan ‘gallop; at- tack’; Oss. tagd, adj. ‘quick’; Gk. tékō, tr. ‘melt, soften, soak’; intr. (“pine away’. Inf: takënai); Ir. cf. tíoch, pl. -ra, m. (“bead of sweat, fr. *teks-); Cz. tékat, inf. ‘run’; cf. u-ték, m. ‘flight’; Li. cf. tékme, f. ‘stream’; Latvian tece, f. “leak; fen, lowland’. Cf. WP I, 701. Nominal forms of type tekos, a in OCS tekü, m. ‘run’; cf. teklí, f. ‘resin’; Li. teküs, adj. ‘flowing, liquid”; Latv. teka, f. ‘footpath’. Cf. tokos A Per. ham-tag 'fellow-traveller
18271:tek- (4) (teko, ið) ‘touch’. Cf. tik-, tink-
18273:Tokh. B täk-, tek-, v. id.; Lat. cf. (?) per-tica, f. ‘pole’; Li. cf. man tenka, inf: tekti, v. “befalP
18275:tekolos, tekoros (1) ‘pleasant’. Cf. tek- (1) and tenk- Olr. & Ir. tacair, adj. ‘suitable’; Icel. ball ‘pleasant, docile’; MHG (variant) dere ('suit- able’, fr. *tekrios). O-grade radical in Ir. toich, gs: tocha, adj. ‘pleasing, acceptable
18276:tekolos (teklos, tekoros) (2) ‘running, flow- ing; run, flow'. Cf. tek- (2) Skt. takram, n. “buttermilk and water”; Ir. cf. tachar, m. ‘flight’; OFris. thial, s. ‘wheel’; OCS tekli, f. ‘resin, pitch’; Blg. tekál, id.; Pol. ciekły, adj. "liquid, fluid’; Cz. cf. roz-tekly ‘fluid, un- stable’; Li. tekalas, m. Clud Lalis: Eng.- Lith.); cf. tekelas, tekylas, m. ‘grindstone’; te- kinis, gs: -io, m. ‘wheel’
18278:tektos (1) ‘flowing, running; flow, run, gait. Cf. tek- (2) Skt. taktáh, pp. “having gushed’; Per. tàxt, s. “attack, gallop’; Olr. techt f. ‘going���; m. *mes- senger’; Ir. (only) teacht, m. ‘envoy’; W taith, pl: teithiau, f. ‘journey’; Br. tiz, m. ‘going, gait
18279:tektos (2), see tek- (1) and tok- Ir. teachta, adj. “suitable, proper": Li. téktas, adj. (“befallen?. NSB);
18280:tekuos ‘runner, servant, slave’. WP I, 716.
18292:teksmn-, teKsmo(n), (toksm-) “shapeu ob- ject’. Cf. teKslos, tekso Per. tasme, s. ‘rawhide thong”; Hitt. cf. taksan, n. ‘joint; adv. ‘together’; Lat. temo, gs: -monis, m. “cart-shaft; thwart; sub-temen, gs: -inis, n. ‘woof
18295:tekstos, å, om “shaped; shaped object, carv-
18717:tokol-, tokor- (1) “spin, turn; spinner, turn- er'. Cf. tek- (2) & tekolos (1) Ir. tochraim, v. (1) ‘wind — thread; OCS, R tókarí, m. *turner'; Li. cf. tákilas, m. *grind- stone, wheel of lathe'. Ir. cf. tochras, m. 'coil- ing”
18718:tokolos, is (tokor-) (2) “touching; touch’. CT. tek- (4) Skt. cf. takarih, f. ‘clitoris’; Ir. tochar, m. “meeting; assembly’; beside tochraim, v. (2) “meet, happen”
18719:tokora (?) Skt. takila, f. (a herb or drug); Alb. takér, f. *marshmallow?
18720:tokos, us (1) ‘flowing, running; flow, run’. WP I, 716. Cf. tek- (2) Skt. tákus, adj. ‘rushing’; (e-gde in) tákmi, v. ‘tush’; Av. takom, n. ‘run, flow’; tako, adj. ‘running’; Per. tag, s. (2) ‘race’; Tokh. B. cake ‘river’; Arm. cf. v-tak, i, av, s. (brook, fr. apo-tok-: OCS po-tokü, id.); OCS (and com. Sl.) tokü, m. ‘flow’; Li. tákas, m. ‘path’; taküs, adj. ‘fluid’; cf. also pra-taka, f. channel; Latv. taks, m. ‘path’
18722:tokos (2) ‘hat’ Ober. cf. taka-bara-, adj. ‘wearing a bat: Br. tók, pl. toku, m. (hať. LW in Fr. toque)
18723:toksið ‘tap, beat, pulsate’ Alb. cf. ndesh, v. (‘strike, clash with, meet, fr. *en-9); Li. taksiù, éti, v. “beat, throb, tick’. (Isophonic in R tošiť, inf. ‘nauseate’, fr. *toks- or *taks-)
18724:toksos "runner: (furry) animal" Cf. tek- (2) and teksko. WP I, 717 Oss. täx, s. ‘gush, excitement’; (Gin. inf. “fly; cf. täx-sal, -salä, s. (a smal! furry animal); OHG dahs, G Dachs, pl. Dächse, m. ‘badger’; (Gmc.
18727:toksos (1) “firm, strong’. (OPer. Av. *teksmo- or *toksmo-) Oss. tax, adj. ‘firm’; Br. tæch, adj. “filling, satisfying’; cf. Av. Ober, taxmo, taxma- ‘brave’
18736:toksos — tom
```


## [2026-09-14T03:10:56.365Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nidx=t.find('vitaxtan vitdc- trans. to melt')\nleaf=t[:idx].count('\\f')\nprint('NYB leaf',leaf, 'printed ~', leaf-18)\ni=open('IEC.txt',encoding='utf-8',errors='replace').read()\nj=i.find(\"tek- (2) (teko, tekmi)\")\nlf=i[:j].count('\\f')\nprint('IEC leaf',lf)\nEOF",
 "description": "Compute leaf/page numbers"
}
```


### [2026-09-14T03:10:57.644Z] TOOL RESULT

```
NYB leaf 235 printed ~ 217
IEC leaf 755
```


## [2026-09-14T03:11:02.353Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==756' IEC.txt | grep -o '13[0-9][0-9]\\|14[0-9][0-9]' | head; echo \"--- first/last lines\"; awk 'BEGIN{RS=\"\\f\"} NR==756' IEC.txt | head -3; echo ...; awk 'BEGIN{RS=\"\\f\"} NR==756' IEC.txt | tail -3",
 "description": "IEC leaf page numbers"
}
```


### [2026-09-14T03:11:03.490Z] TOOL RESULT

```
1373
--- first/last lines
ygo, inf. "cover
ték- (1) “pleasant; pleased; pleasure’. Cf. tekəlos (tekəros) & tenk- (2) Olr. tig, tich, adj. (seemly; pleasant’, fr. *te- kus); Ir. cf. teachta, adj. ‘suitable’; W teg, adj. ‘fair, beautiful’; Cor. tek, id.; cf. tegen, pl. tegennow, s. ‘jewel; ON pega, f. (Cgift', fr. *tekà) beside (long-gde) adj. pægr ‘agreeable, acceptable’; mod. bága, f. “advantage, inter- est’; ON paegja, tr. ‘make acceptable’; W cyn- nig, v. ‘propose’; mell-tigo, v. ((curse', fr. *meli-"); (variant w. doubling) OS thiggian, OE picgan, wv. “accept, receive’; Srb. cf. tëk, Slovene ték, m. ‘liking, appetite’; Srb. tečan, adj. ‘likable, tasty’; Cz. cf. vý-tečný *excellent'; netečný ‘indifferent’; Li. cf. tékit! “please! do accept"; impers. in man tenka, inf: tekti “it falls to my lot
tek- (2) (teko, tekmi) “run, flow'. (Var: teks-). WP I, 715 Skt. tákami, tákmi, v. ‘rush, hurtle'; Av. tak-, tac-, v. ‘run, flow’; (variant in) Oss. tàxín, v. ‘fly’; Per. tàxtan, inf. ‘gallop; attack’; Tokh. B. cf. cake, n. ‘river’; Alb. cf. f-tíkem, v (‘run dry', fr. *apo-tek-); (variant) Mlr. techim, Ir. teichim, v. “tun, flee? and in Br. techi, inf. id.; OCS teko, testi, v. ‘flow’; OCz. teku, teci, v. ‘gallop; flow’; Li. tekù, éti, v. ‘run, hurry, flow’; Latv. teku, tecēt, v. ‘flow; leak, run’. Long- gde-in Per. tāxtan beside tāzīdan ‘gallop; at- tack’; Oss. tagd, adj. ‘quick’; Gk. tékō, tr. ‘melt, soften, soak’; intr. (“pine away’. Inf: takënai); Ir. cf. tíoch, pl. -ra, m. (“bead of sweat, fr. *teks-); Cz. tékat, inf. ‘run’; cf. u-ték, m. ‘flight’; Li. cf. tékme, f. ‘stream’; Latvian tece, f. “leak; fen, lowland’. Cf. WP I, 701. Nominal forms of type tekos, a in OCS tekü, m. ‘run’; cf. teklí, f. ‘resin’; Li. teküs, adj. ‘flowing, liquid”; Latv. teka, f. ‘footpath’. Cf. tokos A Per. ham-tag 'fellow-traveller
...
tekolos (teklos, tekoros) (2) ‘running, flow- ing; run, flow'. Cf. tek- (2) Skt. takram, n. “buttermilk and water”; Ir. cf. tachar, m. ‘flight’; OFris. thial, s. ‘wheel’; OCS tekli, f. ‘resin, pitch’; Blg. tekál, id.; Pol. ciekły, adj. "liquid, fluid’; Cz. cf. roz-tekly ‘fluid, un- stable’; Li. tekalas, m. Clud Lalis: Eng.- Lith.); cf. tekelas, tekylas, m. ‘grindstone’; te- kinis, gs: -io, m. ‘wheel’
téksKó, variant of type tek- (2), q. v. (Variant: teks-) Br. techi, inf. ('flee', fr. *teksK- or *teks-); tech, téach, m. ‘flight’; OCS tésto, těštiti, v. “mel; Li. tešku, eti, v. ‘drip’ beside tekstu, inf. tekSti, v. 'spurt'. Cf. (variant) teks- in Per. taxtan, inf. ‘gallop; attack’; Oss. Gin. v. ‘fly’; täx, s. ‘gush, stir’; Av. taxmo, adj. “swift; Icel. bjósnast, v. ‘rush, dash?
tektos (1) ‘flowing, running; flow, run, gait. Cf. tek- (2) Skt. taktáh, pp. “having gushed’; Per. tàxt, s. “attack, gallop’; Olr. techt f. ‘going�
```


## [2026-09-14T03:11:14.202Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in 'انداختن' 'تخش' 'پرداختن'; do echo \"=== $w\"; grep -n \"$w\" BQT_v1_pages.txt | head -5; done",
 "description": "grep BQT vol1 headwords"
}
```


### [2026-09-14T03:11:15.233Z] TOOL RESULT

```
=== انداختن
948:- 9۲۷ (جوشیدن)» - ۲۵10 (انداختن» افکندن)» - 2۱70 (جامه -
7292:بادشاهی آن دبار را برانداختند وخود 4« و | | ۲۶ ۶ ]<< ۱
8646:آ یز - بروزن‌فالیز» جفته ولگدانداختن
9190:را یز گون که فاعل نوشیدن وکشیدن وانداختن
9211:بعمنی توشیدن- و کشیدن باشد. ویمعنی انداختن
=== تخش
12562:درد دندانرا تخشف دهد » وسارت دیگی آرا
15337:بمعتی خوب و جزو دوم از مصدر توخشیتن (تخشیدن) بدمنی کوشیدن و ورزیدن است . هوتخش .
29057:۴ رك: تخشیدن.
29074:تخشیدن؟ بر وزن لخشیدن»یمعتی
29090:تقد تییغ و تخش منند ,
=== پرداختن
12087:ساختن و پرداختن و آماده و مهیا کردن .
24544:پرداختن باشدا - وبممنی‌پاییدن بعنی‌ثبات‌داشتن
24555:۳ - رك : پرداختن :
24584:۱ رك : پرداختن .
24867:+ عاجز شده باشد؟ . و بمتی پرداختن همآمده است 6».
```


## [2026-09-14T03:11:15.681Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'pdf page' BQT_v1_pages.txt | head -3; echo ===; grep -c '' BQT_v1_pages.txt; echo ===; grep -n 'تک' BQT_v1_pages.txt | head -5",
 "description": "Check BQT vol1 structure"
}
```


### [2026-09-14T03:11:15.744Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-14T03:11:20.176Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport io\nlines=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ndef leafof(ln):\n    txt='\\n'.join(lines[:ln])\n    return txt.count('\\f')\nfor ln in [29074,29090,24544,29057]:\n    print(ln, 'leaf', leafof(ln), repr(lines[ln-1][:100]))\nEOF",
 "description": "Find leaves for BQT hits"
}
```


### [2026-09-14T03:11:21.264Z] TOOL RESULT

```
29074 leaf 702 'تخشیدن؟ بر وزن لخشیدن»یمعتی'
29090 leaf 702 'تقد تییغ و تخش منند ,'
24544 leaf 604 'پرداختن باشدا - وبممنی\u200cپاییدن بعنی\u200cثبات\u200cداشتن'
29057 leaf 701 '۴ رك: تخشیدن.'
```


## [2026-09-14T03:11:26.102Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== leaf 702\"; awk 'BEGIN{RS=\"\\f\"} NR==703' BQT_v1_pages.txt | head -60",
 "description": "BQT leaf 702"
}
```


## [2026-09-14T03:11:27.505Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== leaf 604\"; awk 'BEGIN{RS=\"\\f\"} NR==605' BQT_v1_pages.txt | head -60",
 "description": "BQT leaf 604"
}
```


### [2026-09-14T03:11:27.671Z] TOOL RESULT

```
=== leaf 702
۳۹
تخشیدن؟ بر وزن لخشیدن»یمعتی
بالاشتن باشد .
تخله « بقتح اول و لام د سکون ثانی »
بمعنی نملین و عصاباشد9 - وریزه و خرد؛ هر
چیز را لیز گویند .
از
ام ۱۷ ینم اول وفتح نانی و سکون
میم , پارچه‌ای باشد که نثارچینان بر سر چوب
بندند وبدان از حوا نثار بربایند - وبسکون انی
دانه۷ -واصل هرچیزباشد- ومرضی‌را نی زکوبند
که بعریی هیضه خوانند - و مطلق بیشه را نیز
کفته‌اند اعم از ما کیان وغیرما کیان و بمعنی
رآب پشت هم هت که مادم وجودحوانات
است - و بمعنی‌اصل دنسبت ونژادنیز آمده است.
دارد ۹
همه ده در دش رخش منند
تقد تییغ و تخش منند ,
«شاهنامه بخ ج۲ ص۹۹ ۶*.
۴_نعت‌فاعلی(صفت مشبهد) از تخشیدن,پهلوی 50816لا) «مسینا۲:۱4۹» بازند 01015532,«اسشق
۷۷ : نفشدن . ۴ رکه : تخش و رك : تختیدن  .‏ ؟ - قس: پارسی باستان
آزاهنایها ۵۳۵ 15212 ۱112712)2بار ولمه. تبعات[]۱2*»۲۰) !رب اوستابیت۵۷21:۵),
028 ( غیور » باهمت ) » ۷۵50۵0 , هادافندای ۱۱۳۷2 . بهلوی0۸۵1080,
هندی باتال ۷۵15]25) «قوه» نیرو» «اسشق ۳۷۷ «هسینا ۱4٩‏ : 4۲ «مزدسنا 40۸ .
۵ - اندر فنائل تو عدم کوبی چون تخلةٌ کلیم ییمبر شد. هنجيك ترمذی.
«لوت فری ۷۸ ظ ‏ کلمه ممحف نخله است. (علامه دهشدا).
۱ - پهلوی ۵1070) و ۱۵۲۷ (بذر نخم) < تیب رکه ۲۷۹ و ۵00) « اسشق ۰۰۳۷۸
«سینا ۱4۹ : ۲ , 4۵1010 شکل تلفظ شمال غربی از ابرانی باستان 120175۳028 6 , اوستابی
120128 د< بارتولمه ۱۲۳ > و 8610 , از پلرسی باسنان 211502) « بارتولمه ابا * » از
نها > از 2۱2۳702) ۵ تلفظ جتوب غربی است. در ارمتی 401170 « تیب رک ابما»» در
بازند 110067 .هندی باستانی ۸۵۳027 , کردی 4۵5 »وخی 2810۳70) .سربکلی ۵8107
بودغا 081001710) «اسشق اینا» ؛فریزندی وبرنی ونطنزی 0210) (تخم مرغ) «2 .۱ص ۰۳۸۸
سرخهٌ وشهمبرزادی نیز 4010 4۰ .۲س ۱۸4 طبری 1110 (نخم . بذر) «صاب طبری» «واژه
نامه ۲۵٩‏ :
۷ - هرآنکه تشم بدی کشت وچشم یکی داشت ‏ .دماغ ببهده پخت و خیال باطل بست .
«کلستان ۲۹ ».
```


### [2026-09-14T03:11:28.715Z] TOOL RESULT

```
=== leaf 604
پردا
پرد بمنی يك لای و دو لای با يك ته و دوثه -
ویمعنی خواب همآمدء است مانند خواب مخمل
و جوی آب بائد؟ - و بکسر اول و فتح ثالی
ممعنی گردد باش د که مشتق از کردیدن است.
پر دا « بر وزن و ممنی فردا باشد که
در عربی غد گوبند .
پرداخت ؟ - بر وزن اقاخت. ماضی
خالی کردن و فارغ کشتن باشد بمنی خالی کرد
و فارغ کشت و ماضیآراستن و جلا دادن و در
ساختن ومرنب کرداییدن هم هست یعنی آراست
وجلا داد ودر ساخت ومرتب گردانید. واشان
ویر ابشان پرداز ومصنوعات خودرا نیز گویند
و گاهی در تهبیح و تین کسی هم استعمال
کنند چنانکه کوبند «دبدی و شنیدی که چه
پرداخت ؟ »
پرداختی "هبروزن سر باختن؛ بمعنی
فارغ کشتن از علایق - و برداشتن و رفع
نمودن - و باخی رمسیدن و تسام خدن
توخود راکمان برده‌ای درخرد
و ترك دادن‌باشد - و بممتیآرامتن - ومشفول
شدن - وتوجه نمودن - ومقید کردبدن - و با
کسی درساختن - وبرانگیختن حم آمده است -
وجلا دادن - و مرئب کرداندن رائیز گویند که
مجموع شانزده ممنی باشد .
خالی کشته م وفارغ شده از جمیم علایق وعواید
باشد - و بمعنی ساخته - وآرامته - و مشفول
کردیده - و انگیخته. وتركك داده- ودور کرد
وحلا داده - وصقل کرده هم آمده است. 4
پرداس «» بر وزن کربای » بمعنی
پرداختن باشدا - وبممنی‌پاییدن بعنی‌ثبات‌داشتن
و بسیار ماندن همآمده امت۷ ۰
پردال س_ بر وزن ومعنی پر کال امت
کهال دایر» کشدن باشد۸ ۰
بر دحت - ختح الث بر وزن‌سرسخت»
مخفف برداخت است بمنی خالی کرد و فارغ
شلات و آراست ّ وححللا داد ت دمرفب گردانید ۳۹
ودرساخت؟ .
انابی که پرشد دک رکی برد.
۴ اکنون در گیلکی ۳۸۵۲0 کویند
۴ پپلوی
۳ - رك : پرداختن :
4 اسم مفعول از پ‌داختن ( ۳ ,
۱ وگ:: مرول (حاشبه) ,
۵ رل : ی رکار .
«لنت نامه > .
```


## [2026-09-14T03:11:46.094Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD\"; grep -n 'handāxtan\\|handāz\\|pardāxtan\\|witāxtan\\|wid̄āxtan\\|tāxtan\\|handāzag\\|taxš' PHD.txt PHD_mackenzie.txt | head -30",
 "description": "MacKenzie Pahlavi forms"
}
```


### [2026-09-14T03:11:46.149Z] TOOL RESULT

```
=== PHD
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
PHD.txt:393:handāxtan 42 hanjidan
PHD.txt:394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
PHD.txt:539:pahikdftan 64 pardāxtan
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:541:pardāxtan 65 pāsbānīh
PHD.txt:595:~ih: bitterness. taxt [2А | N ~] throne. ~ag [-#! | N ~a] tablet, plank, (chess) board. taxtan, taz- [Phtn', tc- | M rem, tz-] run, flow. išnīh : flow. tāxtan, taz- [?Аїп!, Pc- | M Рс-, N ~] cause to run, flow; chase; pour. taxt-gàh [?hig’h | N <] couch. taz-, —išnih, v. taxtan. táz-, v. tāxtan, tazāģ [tc’k'] flowing, running. tāzānaģ [P enh | N tāz(y)āna] whip. tazënidan, tazën- [tcyn-ytn'] = tāxtan. tazidan, taz- [tc-ytn'] = taxtan. Itázig [Pcyk! | N tázi] swift, fast. "Táüzig [Pcyk! | N tāzi] Arab. tēmār [tym] | M tym’r, N ~] sorrow, grief, care. ltërag [tylk' | N tēra] dark, turbid. *térag [tylk'] (mountain) peak, summit. téx [tyh | N téy] sharp edge, ridge; ray. Mēz [tye | M tyz, N ~] quick. ~ih: speed. *téz [tye | (P tyj), N ~] sharp. ~ih: sharpness. *tidag [tytk' | (N dida)] pupil (of eye). tigr [HTY A < А Шу; tgl | M tygr, N tir] arrow. *tihóg [tyh:wk! | N tihi] small grey partridge. tir, v. tigr. Tir [tyl | M tyr, N ~] a god (confused with Tištar); astr. Mercury; cal. 4th month; 13th day. tis [MNDOM < А mnd‘m; ts | M, J tys] thing, affair. «iz [-c | M -yc] (with a negative) по... at all. tišn [tyšn!] thirst. tišnag [tyfnk! | M tyšng, N ~a] thirsty. ~th: thirst. Tištar [гуй | № ~] astr. Sirius. të [LK < A l-k | M tw, N tu] thou, thee. *tóf [twp | N to] layer. tóhmag [twhmk' | M twhmg, N tuxma] seed; stock, family. tom [t(w)m | M tm, N tam] darkness. -tom [-twm | (M. -dwm)] suffix forming superlative adjectives. tóm [twm | (M twhm, N tuxm)] seed, family. tórag [twlk' | N tora] jackal. tūšag [twšk! | N tófa] provisions. tóxtan, töz- [twhtn', twc- | M twz-, N ~] atone, expiate. ~išn: atonement, expiation. tóz [twe | N ~] bark, skin.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:1948:fire adur, ātaxš; form of ~ āsrēkerpa; sacred ~ ádarog, Burzénmihr, Farrobág, Gušnasp, ātaxš i Wah- ram.
PHD.txt:2038:free (v.) wišādan; ~ oneself from pardāxtan az.
PHD.txt:2512:judge (v.) handāxtan.
PHD.txt:2513:judgement ^ dadestàn, dadwarih; handāzišn, wizir. Jug xumb.
PHD.txt:2625:like (pr.) &iyon, handāzag i, hangēš- idag i, О... homānāg.
PHD.txt:3140:plan handāxtan.
PHD.txt:3343:reckon àmàr-, handāxtan, hangārdan, ó$murdan.
PHD.txt:4513:taxt taxtan, tāxtan taxtag tēx
PHD.txt:4688:frahixtan frahixtag frayádisnig fravādišn frāy frādahišnīh frahist farroxīh farrox lxwah-I xwastant frārāst frārūnīh frārēn frāmēš frūmēš- frāmuštan frahist parrag frch pardāxtan frehbūdīh frehbūd pardāz-
```


## [2026-09-14T03:11:48.516Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG tak\"; grep -n '\\*tak\\b\\|tak- .*run\\|^\\*tak' CHEUNG.txt | head -20; echo \"=== BRT tak\"; grep -n 'tačaiti\\|tacaiti\\|hqm\\.tac\\|vi-taxti\\|vitaxti\\|tačar\\|tacar' BRT.txt | head -20",
 "description": "Cheung and Bartholomae"
}
```


### [2026-09-14T03:11:48.597Z] TOOL RESULT

```
=== CHEUNG tak
=== BRT tak
4585:•  j,  +antar«.ar98am ''  Adv,  ('zwischen  den Seiten',  sva.)  1) 'innerhalb',  mit  Gen.:  °äjw zrayanhB  V.5.19;  —  ''(am  nmänahe  "V-ff. 33,  Yt./7.6o.  2)  'diesseits':  yas;/  iava masda  kirpnaot  tacar)  *nSit  *tacar>  *'Mm'^ upairi  Avanxsaiüm  "dass  dir  M.  eine Bahn  bereite,  nicht  eine  Bahn  diesseits, (sondern)  Über  dem  Sonnenball"  YL  5, 90.
11815:aiöJstkrOsca gaeyaoitiica  atacintls(^i^ . .  vaxiymte  (sd.)  ".  .  die  Quellen,  hin- äiessend  zu  den  . .  und  Fluren  ,  ."  Yt. Ä42;  —  ätacaiti  .  .  ar>dvX  Yt.^.102.
11881:•  p.  tacara-  'Palast,  königliche  Privat- wohnimg':  darayt^vt^u^  .  .  Aj"«*  imam •ram  akuiiaus  D,  /.
17019:•  j.  barszah-  n.  'Höhe,  Berg':  *upa *tnaitlm  (sd.)  'zargAam  V.J.  30;  —  mihnm .  .  yS  vlsp)m  aham  .  .  Sdt6aili  haratkyät (sd.)  paiti  'zatakat  Yt  jo.  5 1 ;  —  barniste paiti  'zaÄi  haraihyS  .  .  Y.  ^y.  19;  — AuiaitJm  (sd,)  °zS  Ytj.  96,  12.  24;  —  ya (näml.  arfdvt)  .  .fratacaiti  hukairyät  haca 'zaftkat  Y.  65.  3 ;  Yt  5.  2  5.
21217:—  y  his  spä  va  aiwi.vafnaiti  .  .  also druxl  yä  nasus  apa.dvqsaiti  FrW,;/;  Yt 6. 1  O,  7.  4;  —  yaozpnti  vXspe  karans  y his  aoi  fratacaiti  y  hll  aol  frazgaraiii andvl ..Y.6$.\;  —  Wirä  mthrahe fra- yanä  yase''^  tarn  dahyüm  äiaraiti  ya%a  . . Yt.  10.  i\2;  —  {ya%a  ralvastfmahe^l)  y usnqm    aiiti    va^ya  (sd.)    Y.  10,13;    —
21238:'modalen  Formen:  yaT  adaif  (sd.)  asa *drujim  vSngAaitT  Ay  ('so  dass')  '^qsasuia (sd.)  ya  ..Y.4S.\;  —  ka%a  iBt  gavBi ratul  hy  ('auf  dass')  AJm  data  xsayatttS (sd.)  %waxsB  Y.  25.  2;  —  a  *m3yastra.- barattä  (Sp.  1190  u.)  ,  ,  Ay  ('auf  dass') ^<iärJ(sd.)  mana  bava/Y.30.^; 32.i6(f); —  vax^a  vS . ,  Ay  ('damit')  d/ih^ng  (sd.) vicayaha  ad^qs^ä  Y,  46.  15;  —  asaonl rafonS  RySm  .  .  Ay  ('auf  dass')  *a  *basils (sd.)  .  .  dya  Y.43.S;  —  tat  ai  vairi- maidl  .  .  Ay  ('damit")  r  mainimadila  .  . ^■35- 3-  b)  im  jAw.;  i)  mit  Ind.:  tä Ai  taurvayatam  tba^a  .  .  y  ('so  dass') ^it  apB  takäis  stayat  Yt  y .  7  8 ;  —  x^anns .  .  yat  uparaAacat  AaoiyanApm  .  .  y  x/a- yata  .  .  dasvanqm  ma^anqmca  ".  .  so dass  er  herrschte  über  .  ."  Yt  ig.  26; 28f.3,  13,  79,  84,  Y.().4;  —  saya  ava%a staxrB  y  ha  druxl  oHti  tnfnzvT  .  .  FrW. 8.  2  (?).  a)  die  Antwort  auf  eine  Frage mit  ^anl'  einleitend  (s.  2  a,  3):  ^Ivata  (sd.) na  *mtima  vaca  gdha  sravayS  ratu/riil y  Ai  nasdiSiB  daAmH  aiwi.srunvai/i  ", .  so, dass  ihn . .  verstehen  kann"  N.  27.  a)  mit Konj.  (oder  Inj,):  y  ('damit')  yavB  (sd.) pouruS  bavät  oBa  mq%r3m  *tat  mairyai V._j.  32f.;  —  :farm3..yai  upawAaiat sao^antqm  Vfr^rajaram  .  .  y  hrmavai frasim  aAüm  ,  .  ". .  auf  dass  er  die Menschheit  neu  gestalte"  Yt/9.88f.;  11, 8.  I,  V.  ig.  23;  —  neben  ya%a'.  Jrsit  mB tat  nqma  /ramrUiti  .  .  ya%a  (Sp.  1 246 u.)  azsm  taurvayetti  . .  y  ('auf  dass')  mqtn nasHS  taurvayät  Yt.  i.  6;  —  th  mazdi zbayal  avanAe  .  .  y  ('damit')  spmtB mainyul  vfharayat  asmatum  y  ap)m y*  .  .  YLy.28;  —  mä  buyama  sSihrB,- iricö  ,  .  m^a  (sd.)  y  ('damit')  nS  uyra.- bäzaus  nivanai  (sd.)  Ytjo.  75;  —  kana 'hwqm  yasna  yazäne  .. yasp*^  ('auf  dass') tava  mazdi  kinnaot  tacara  .  .  yasi^^ ('damit')  äwa  nöit  aiwi.druiante  .  .  Yt 5. 90.  a)  wie  I  a:  h/at  aiwyätsAayanttl yat  aliqm  *3r)dvaya  (sd.)  . .  *v3r»^antqm ndit  avanrasayai  (sd.)  N.  85.  3)  mit Opt.;  wie  I  a:  cvantö  ata  Am  alle  kata  ..l ■  .  y°  Al  nsit  >r)dv5.hr3han3m  (sd.)  vayta- n»m  upa.janyatY .^.\\.  4)  dasVerbum i^aA')  ist  weggelassen:  spanim  nida%?m y  dim  mazaos  (sd.)  ksArpB  tarahe  V.  13. 39.  V)    einen   Inhaltssatz    einleitend
21344:•  j.  yaVant-  Adj.  (fem.  'vaiti-)  'quantus, wie  gross,  viel,  weit,  lang*,  mit  den  KorreL avant-,altai-ant-,ci-aitl-:  asHca  im  za  avaiti bqz5  'vaiti  frd^ascit  Y.ip.j;  —  ^at  .. upa.isat?  'val  hä'krfm  "auf  welche  Ent- fernung . .  soll  er  suchen?  So  gross  ein H.  (ist)"  N.  705.  A)N.-ASn.alsSubsL (mit  Gen.  part):  mit  aspinnd.masS  .  . 'vat  .  .  (aräitika  .  .  hanks  (sd.)  kancayäi V.5.60;  —  i(j'(sd.)  aSavat  ha%r7tn  'vat tacarsm  F.  27a;a;  —  'vat  anu  aipi  (sd.) .  .  garayö  visastan  visppm  avaj  aipi  . . Yt,  ig.  8;  —  'vaj  aArnai  yamanam . .  sairi- iiqm  (sd.)  a?tavat  atnjaokanqm  V.A'.Ss;
21947:6av3t  V.J.  19;  —  nairyh  v  pu%raAe  v haeyh  V  marfuyä  Y.ii.i; — yesi  a/sAaf upaOPm  V  aiwinaptlm  v°  . .  V  .  .  f  V. 7,  la;  —  pä^a  ayantim  v'  taBnhm  V V  ..V  V.6.26;  —  tiraos  v°  paiii  sBinma umm  V'  kaiat  V  paiti  siäaranqm  N.  loo; —  vännti  V  snaszinti  v°  bannti  v'  tima- nAqm  V  *aiwi^ais (sd.)  ayqn  v ..vantö. vire  (sd.)  jas»nti  V.  iV.  4;  —  yS  tat  draons ainät  t/'  tn/yät  v° apa  v yäsäiüY.ii.S',  — yS  gatwqm  ..janaiti  v  vayät'i  »*,.  v'  ,.V V-Zj.  5;*—  ferner:  Y.  (j2.  9,  Yt.4.4,  8.\\, JO.18,  J/.4,  75.50,  V.^.  44,  5.5, 12,27,45, 57,  6.46,  8.2,  12,  ß.  II,  y.37,  i4. 17. ^5-9.  14.  z»y-53.N.J5,  26',  J7,  P.i'/,  VyLJO, 2^\  —  s.  noch  Anhang  2;  —  im  Wechsel mW.  yai  vä  (Sp.  1261  f.):  hris  v  /ämaa yat  vä  xsvas  yat  vä  nava  V.5.  51;  — andus  v3  ayryS.siaonm  v*  bistaorfm  V yat  matauhsm  v a  3^ar?m  N, 45^^-  zu  Z ) ; b)  im  gAw.:  yä  nsitv'  aaiat(Sp.  271  u.) aKiAain  V  Y.31.  5.  c)  im  jAw.:  Aatci^ (Sp.  592  u.)  V  nsit  v°  \t.l4.2o; — yaf apirmäyüks  sraoüi^^  v'  anu.tacaiti  aoxtö (sd.)  V  hl  aoxte  . .  N.  7;  —  y!J  gä^anqm anttmaiti  (sd.)  V  * anumainyete  ainyehs  V srävayantö  paitistanti  (sd.)  anyS  V  hi dahmS  . .  "wemi  einer  . .  oder  wenn  er  . . oder  wenn  ihm  . ."  N.  25;  —  in  weiter Trennung^);  yat  .  .  spä  avaci  (sd.)  V aonityS.xratu^  . .  yai . .  spä  ahqm.baöh>mnS (sd.)  v°  bavat  ähäityS.xratus  "wenn .  ■  einer- seits , .,  wenn  . .  anderseits  . ."  V.  j_j,  29 und  35.  Anhang.  /)  Eine  Ellipse  liegt vor  in:  katärSm  ä  angrH  (Sp.  104  u.)  väi hvB  v  ar^rö  yS ..  ". .  der  Feind?  (Ist  er auf  dieser  Seite)  oder  ist  der  der  Feind, der  . ."  Y.  44. 1 2.  2)  Ausgefallen  ( ) ist  »a  an  folgenden  jAw.Stelienj  zu  IUI  1: daSvayasnäi  v°  tanupirikät  (w)  'Ü.16;  — näirikqm  V  *apßrmäyBi^m  (v)  N.  105; —  pas/a  v* paiti {v) ..'H.gs.  zullll  a: pure  v°  puäiräi  {v)  brähre  v°  Yt  14. 46;  —  mit  ungleich  gebauten  Gliedern: AvSiitö  v° ydiste  {v')  yi/it  V  ainim..cayqn N.  J.  zu  m  2 :  yai  arastr^m  (sd.)  pairi.- a^a  v°  *vaca  (»•)  *apayaiiti  (Sp.  190  o.) aratufrya  N,_52.
29826:mit  vaAmä  TgtU  beginnende  Stück"  Y.  bezeichnung,uzw.a)Wegmass'':  W/aSaz-a/ 5^.  10;  Y.  3Ä~^4,  4.J-57  Schluss,  N.46;|.3.WM  yavat  tacar>m  "ein  H.  zweimal —  ustavaityä  vä  sp^ntäMainySiif  va  hmis\  (genommen  ist)  soviel  als  ein  Tr  F.  27  a; '&.iO2\i02;  —  Hiranqm..haUUca{KS.)  _  tacat  paeirlm  '^r>m  V .  8.  loo;  'Ü.  8, afsmanala  vacasca  facasia/ffm(sd.)ca  ^r-' io();  —  antan  *'%nmcit  N./o^J);  — t3Z-  '.antarät    naemät  ''hroAe   ^.60,  104';    —
30664:•  j.  hvar«-xäaeta- "  n.  'der  leuchtende Sonnenball,  Sonne',  auch  als  Gottheit;  yas? tava  mazdä  k»r»naot  tacar»  ''nsit ..  *anlar».- ann»m{s<i.)  upairi  't»m  Ytj.go; — ya'^a avat  't»m..fraca  ätti  YtJO.  118;  —  °t»m *utyS.raili  Y.ig.iB; — uzayara  uslra  'ta aurvat.aspa  V.27.5;  —  yatcit  ahi..upa  ave stärd  .  .  upa  aom  maT»h»m  .  .  upa  'lfm aurzaj.rijp»m\t  12. 33—^4;  —  -/»m  am»i»m ralm  aurvat.asp»m  yasamaide  Yt 6.\\  6, jj.Si,  Y. /ö'.  4,  S.S.  11;  —  °tai  aurval- aspäi  Y.68.22;  —  'tahe  amtsahe  Yt,  6. o, Y.  22.  24;  Vd.20;  —  hvar»ca  xiaHahe'^ aurvaLaspahe  Y,  /.  1 1 .  a)  hvar»xsattaht (näml.  ayar»)  heisst  der  11.  Monatstag: 'tahe  amfsahe  ralvahe  aurvat.aspahe  S.  i. 11;  vgl.  2.  II,  Y.lö.  4.
```


## [2026-09-14T03:12:02.452Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PLA handasa\"; grep -n -i 'handasa\\|muhandis\\|handaza\\|handāza' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10; echo \"=== AFM هندسة\"; grep -n 'هندس' AFM.txt | head -10; echo \"=== TAD\"; grep -n 'هندس' TAD.txt | head -5; echo \"=== ARB\"; grep -n 'هندس' ARB_mo3rb.txt ARB_abdulraheem.txt | head -5",
 "description": "Arabic sources for handasa"
}
```


### [2026-09-14T03:12:02.556Z] TOOL RESULT

```
=== PLA handasa
18400:o*»#» - muhandis = muhandiz q. v. °. 
19574:handaza 
19577:oe,» - handaza: s. handäz.. 
19590:syr. handaza 3, 
=== AFM هندسة
1094:ام ندخشان ويقال ها 6 5 بالفارسمة قاسم ولاه ببن خوراسان وهندستان فيها 
6428:ونحوها ٠‏ 2 اللقدر حارى ܨ ܕ ܙܝ 7 0 1 وا هندس 
6429:وهندس كل ذلك 239 ܝ 4197 0 ® والتقدير والتخمين 
=== TAD
=== ARB
ARB_mo3rb.txt:2721:وم 00 « وأيدلوا الزاى سينا 6 فقالوأ 2 المهندس »اه 
ARB_mo3rb.txt:18931:وما بعد هذا الال عما عيب إليه ! ! وق اللسان :« قال ان تى” : ”*القنئن والقناقن*“ : المهندس 
ARB_mo3rb.txt:24594:5 أو سود مأ و ايمس شدقية هواس هن بر هندس
```


## [2026-09-14T03:12:03.731Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN toxic\"; grep -n -i 'toxicum\\|toxikon\\|toxon' KLN_1966.txt KLN_1971.txt SKT.txt | head -20",
 "description": "Klein and Skeat toxic"
}
```


### [2026-09-14T03:12:03.797Z] TOOL RESULT

```
=== KLN toxic
KLN_1971.txt:250758:fr. L. toxicum, ‘poison’, fr. Gk. to^ixov (scil. 
KLN_1971.txt:262219:Vincetoxicum, n., a genus of plants, the angle-pod 
KLN_1971.txt:262221:son’, fr. L. vincere, ‘to conquer’, and toxicum , 
KLN_1966.txt:39724:toxic,  adj.,  pertaining  to  poison.  —  ML.  toxicus, fr.  L.  toxicum,  ‘poison’,  fr.  Gk.  xoEixov  (scil. <pap|jtaxov),  ‘arrow  poison’,  neut.  of  the  adjec¬ tive  toEix6?,  ‘pertaining  to  a  bow  or  arrow’, fr.  x6 Eov,  ‘a  bow  or  arrow’,  fr.  Scythian *taxsha-,  whence  also  L.  taxus,  ‘yew’.  Cp.  taxus.
```


## [2026-09-14T03:12:10.583Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '19560,19600p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== 18390\"; sed -n '18390,18410p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt",
 "description": "Asbaghi handāz entry"
}
```


### [2026-09-14T03:12:10.655Z] TOOL RESULT

```
9. Addai Scher s. v. 

10. Nyberg Bd. II s. v. 

11. Wahrmund s, v., Addai Scher s. v. 
12. Mackenzie s. v. 

13. Brockelmann s. v., Macuch s. v. 


11 


handaza 


oe,» - handaza: s. handäz.. 


Vs - hindis: "Geometer, Architekt, Ingenieur" 


AL - hindisa: "Geometrie, Architektur, Ingenieurskunst" 
®, talm. Lw. hndz’, 


.o,lıı andäze MP. 9oor handädak v. handäxtan 


syr. handaza 3, 


- 


(3 se - hindaki: "Inder" pers. 


270 

=== 18390

er - mahsal: "alt" 1 ei pers. JWwa, mahsäl mp. mas + »sal am. 
mas + sarad / ®ard 2, 


PRESS mahmändär: "Gastgeber" 3 CT MP u sus mahmaneh am. ma&edana 4 
>>a$> - muhandiz: "Geometer, Feldmesser" _ andäza s. hindisa. 
5 


o*»#» - muhandis = muhandiz q. v. °. 


03)» - mawäbida: Pl. v. x. mubag q. v. 


E/> - mawäzif: Pl. v. > mauzaß q. v. 

Gt - a-mwag: Pl. v.&-müq q. v. 

>] - mawänig: PL. v. öl mänid qa. v.
```


## [2026-09-14T03:12:11.475Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6420,6435p' AFM.txt",
 "description": "Addi Shir handasa"
}
```


### [2026-09-14T03:12:11.547Z] TOOL RESULT

```
( ܐܝܟ ) ܐܨ 9 الضبع اظَنْهُ معر با 5 4 ايضاً 3( 
2346 وو بره وعفاؤه 

١‏ 99 الفصيل 5583 طن 53 3959 مأخرذًا من 7000 زهو 
)+£ 

( المنْدَاز) !ܐܚ والقياس .و ( !0:4 ) | سم ܗܘ الذى ܨܝ (3:02@ 

ونحوها ٠‏ 2 اللقدر حارى ܨ ܕ ܙܝ 7 0 1 وا هندس 
وهندس كل ذلك 239 ܝ 4197 0 ® والتقدير والتخمين 


اير © ܐ ܡܝ ܐܢ © ܦܩܢ 


( 9 9 تعريب اجن
```


## [2026-09-14T03:12:23.770Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG\"; grep -n 'TAK\\|tak: \\|√tak' CHEUNG.txt | head -20; echo \"=== HUB\"; grep -n -i 'andāxtan\\|handāz\\|gudāxtan\\|taxš\\|tāxtan' HUB.txt | head -20",
 "description": "Cheung and Hübschmann"
}
```


### [2026-09-14T03:12:23.837Z] TOOL RESULT

```
=== CHEUNG
=== HUB
```


## [2026-09-14T03:12:25.402Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v3 gudaxtan\"; grep -n 'گداختن' incoming/BQT/BQT_v3_pages.txt | head -6; echo \"=== BQT v4 handasa\"; grep -n 'هندسه' incoming/BQT/BQT_v4_pages.txt | head -6",
 "description": "BQT vol3/vol4 lookups"
}
```


### [2026-09-14T03:12:25.512Z] TOOL RESULT

```
=== BQT v3 gudaxtan
=== BQT v4 handasa
1905:۱-(عر ) اسم مفعول از تثلیث . - در اصطلاح هندسه سطحی است مخدود به اخط
16598:راکه حاب و هندسه و هیأت باشد او آورد » ۲ و بد مردم درول نگاهداشتن را نیز کویند.
18791:اصل‌الهندیا خواند . هندسه* « بکراوزوناك۹ وفتح-ین
```


## [2026-09-14T03:12:30.674Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [18791]:\n    print(ln,'leaf',('\\n'.join(lines[:ln])).count('\\f'))\nEOF\necho \"=== v3 gudaz\"; grep -n 'گداز\\|گداخ' incoming/BQT/BQT_v3_pages.txt | head -8",
 "description": "BQT v4 leaf and v3 godaz"
}
```


### [2026-09-14T03:12:31.768Z] TOOL RESULT

```
18791 leaf 461
=== v3 gudaz
5478:که چون مس را بگدازند و در کودی ریزند. تا
6652:طلا ر نقرژ گداخته باشد که در دارچة آحنین
33459:چون مس را بگدازد و در کوی ربزند تا بسته
41649:بگدازند ۵ ب وصبح صادق را لیز کوبند-وبمعشی
41677:‏برآن مثال که سیم گداخته درگاه.
42018:گداختی- بضماول وفتح پنجم = کدازیدن, اوستا- ‎Vitacina. lS )vitaxti‏
42126:گر از بطم اول بروز نگداز ‎oes‏
```


## [2026-09-14T03:12:31.775Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -c 800 CHEUNG.txt; echo; echo \"=== size\"; wc -l CHEUNG.txt HUB.txt",
 "description": "Check Cheung/HUB file format"
}
```


### [2026-09-14T03:12:31.866Z] TOOL RESULT

```
Etymological 
Dictionary 


of the Iranian Verb 


Johnny Cheung 


Etymological Dictionary of the Iranian Verb 


Leiden Indo-European 
Etymological Dictionary Series 


Edited by 
Alexander Lubotsky 


VOLUME 2 


Etymological Dictionary 
of the 


Iranian Verb 


By 


ohnny Cheun 
y g 


LEIDEN : BOSTON 
2007 


This publication has been made possible by the financial support of the 
Netherlands Organization for Scientific Research (NWO), and Leiden Unwersity. 


This book is printed on acid-free paper. 


Library of Congress Cataloging-in-Publication Data 


A СІР. record for this book is available from the Library of Congress. 


ISSN 1574-3586 
ISBN-13: 978 90 04 15496 4 
ISBN-10: 90 04 15496 5 


© Copyright 2007 by Koninklijke Brill NV, Leiden, The Netherlands 
Koninklijke Bri
=== size
  58427 CHEUNG.txt
  10982 HUB.txt
  69409 total
```


## [2026-09-14T03:12:37.316Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [42018]:\n    lf=('\\n'.join(lines[:ln])).count('\\f')\n    print(ln,'leaf/pdfpage',lf)\nprint(repr(lines[42010:42035]))\nEOF",
 "description": "BQT v3 gudaxtan footnote"
}
```


### [2026-09-14T03:12:38.407Z] TOOL RESULT

```
42018 leaf/pdfpage 573
['این\u200cیمین فریومدی «فرهنگه نظام»', 'در سروری یکس هردوکاف آمده «رشیدی» . \u200egadh(a)man . pA\u200f .', 'پهلوی 3۷9۲۲210 (خره » فره) > \u200e٩ We Gy\u200f - از: کدی (رك \u200eFCS aS\u200f ور', '(پسوند اتصاف)؛ ولی استعمال آن محتاج بشاهد است . ۶ رك \u200eaS:\u200f کدا :', '', '\u200fتست حاجت مرا بافانه _ کدیه\u200cخوش لیست .گنج \u200ewhey»\u200f نزاری\u200cقپستالی*فرهنگه بظام»-', 'بقیه \u200einte Liste jl\u200f ۱۷۷۹', 'گداختی- بضماول وفتح پنجم = کدازیدن, اوستا- \u200eVitacina. lS )vitaxti\u200f', '', '\u200fپپلوی \u200ege bvitaxtan\u200f 4۸۹۱ آب شدن وآب کردن فلز با روغن با جزآنها بوسیلحرارت-', 'آب شدن هر چیز سخت .', '', '\x0c[pdf page 575]', 'بیان هشتم', '', 'در کاف فارسی \u200eL\u200f ذال نق', '', 'گذ اد دن \u200epee\u200f اول بروزن اروت', 'بمعتی گذاشتن \u200eMast\u200f - وبمعتی ادا کردن ۴', 'وحبا(۱) لمودن عنی\u200cپیش کش کردن هم هست-', 'وبمعتی کثرالیدن هم آمده است بچاده\u200cعنی؟ ۰', 'گذادش؟ - \u200epe\u200f اول وک رایع', 'وسکون شین نقطه \u200eoon Soe\u200f وترلگدادن-', 'وادا تمودن', '\u200eUF\u200f اشتی = باتی\u200cوتای قرشت,بروزن']
```


## [2026-09-14T03:12:47.056Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint(repr(lines[18785:18800]))\nEOF",
 "description": "BQT v4 hendese entry"
}
```


### [2026-09-14T03:12:48.073Z] TOOL RESULT

```
['مفنها هل', 'هم بوده است۹ (۱) + زده » بمعنی هندیا باشد که\u200cکاسنی است۴ .', 'هندبا؟ « بکر اول و مکون نانی هندسان؟ باسین بی لقطه بر وزن', 'وثالت وبای ابجد بالف کشیده . گیاهی است تلخ | هندوان » مخفف هندستان و هندستان مخفف', 'که آنرا بفارسی\u200cکاستی میگویند وبیخ آ نراعربان هندوستان .9', 'اصل\u200cالهندیا خواند . هندسه* « بکراوزوناك۹ وفتح-ین', 'هندبید.- بکراول\u200cوسکون نانی\u200cونالث | بی\u200cنقطه . بمعتی اندازه وشکل باشد - وارقامی', 'وبای ابجد بتختانی مجهول کشیده وبدال بی\u200cنقطه | را نیز کوین د که در زیر حروف کلمات توسند', '() چش: ۳ هنام... اندام است (1). جای این اغت در صفحةٌ ۲۳۷۵ است .', '۹ - هند چگرخوارء زوجم ابو-فیان ومادر مماوبه. که چجگر حمزه عم پیفمبرس را که', 'درجنگه احد شهید شده بود جوید واورا عرب آكلة الاکباد خوانند . ۴ - ژاباکوید :', 'پهلوی «هندوپا» ازیونانی 601]0101 (کلمةٌ مسری) است. رل : 116 3۲ .26118007 ,8016', '1 ,۷11 .۸10۲8601 5عل ۳۵۵6 «ژابا س۲ 4۵ . لوفر گوبد : هندبا شکل «عرب از', 'سریانی 8841 وآن ماأخون ازیونانی 81(008] و نام انواع بسیار از18100۳80665» است', 'ودر عقار مراد 6841۷6 (فر) است س 6501۷012 ۳10807100 و سپس 4۱۷2۳1621080 6۰']
```


## [2026-09-14T03:12:48.821Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor ln in [9190,9211]:\n    lf=('\\n'.join(lines[:ln])).count('\\f')\n    print(ln,'leaf',lf)\nprint(repr(lines[9180:9225]))\nEOF",
 "description": "BQT v1 andakhtan area"
}
```


### [2026-09-14T03:12:49.912Z] TOOL RESULT

```
9190 leaf 280
9211 leaf 280
['که آهرمن بدکنش\u200cرا بکشت', 'دققی ۶ مزدسنا ۱۵۷: ۰۱۷۲ ۱۷۵ *.', 'ججیزی که سو کند بودی در اوی', 'کندی » ستی .آهسته کاری فونگف:', 'شه در صفحةٌ ۷۰\x0cودال ابجد ,کی را گویند که دروغ وید 6', 'هودم را فریپ دهد ۷ .', 'آ هی ؟ س بفتح اك و سکون نون »', 'ممروفست.- وشمشیر و تیغ را نیز آهن گویند .', 'بمعنی ب رکشیدن باشد مطلفا - و اهر بکشیدن\u200cهم', 'را یز گون که فاعل نوشیدن وکشیدن وانداختن', 'باشد ۴ - وبمعنی عزم واراده - ونضت وابدا-', 'و انداژهم آمده است .', 'از مرد سخت جان و سخلی کش نی محنت', 'کش باشد . ۱', '] هنجد ؟ - بنتح جیم و سکون دال', '۲ - آدرخش صاعقه » بدی 7', 'اه', 'ایجد , یشی یکشد - و ینداژد .', 'آهنچه - بتج جم ۰ پپناکش', 'جولاهگانرا گوبند , و آن چوبی است که طول', 'آن موافق عرش جامه ایست که می بافند و بر', 'هردو سرآن آهنی صب کرده اند » و آنرا هد', 'وقت بافند کی بردو کناوجامه بند کنند - وبعنی', 'گوند رسمانی باشد که جولاهگان در آخرکار', 'پندند و در سقف خانه بند کنند » و باجیم فارسی', 'هم کفته اند .', 'ا هی چخت - بض جیم و سکون 8', 'تای فرشت . آهنی باشد که زمین را بدان\u200cشیار', 'گت .', 'آ هنحیدن * - بر وزن واگردیدن,', 'بعمنی توشیدن- و کشیدن باشد. ویمعنی انداختن', 'هم آمده است ۷ .', 'آهمندآن دروشگو ظریب . « لت نامه » .', 'ایا 2515 < دهارله ۱۸۸ > و8268 « تیب که ٩-۱۳۵\u200f > اورامانی 25260 «2. اورامان ۱۲۰»', 'سمتانی 5110 ۰ منکری 21180 , سرخ 8987 , لاسگردی 888 , شهمیرزادی 8580', '٩۱۸۱-۷۲. 3\u200f * .کلکی 2010 م فریزندی ویرنی » ۵180 , نطنزی 2008 , دك .ص۷۸۵»:', 'ی دا و ار کف رت', 'خلقانی «لفت نامد».', '۴ - درلمات مرکب : آب\u200cآهنج » جان آهنج . دم\u200cآهنج , دودآخنج , گوشتآهنج »', 'معده آهنج بممنی آهنجنده یمنی بر آورنده , ب رکننده » یرون کنندم و پر کشنده است . رف :', 'دلت\u200cنامه ۰ ۴ رك : آهنجیدن. ۵ بهلوی ات2202 « منای ۹٩٩۵\u200f * , فذارسی', 'آهنگه , آهنگیدن » هنجیدن , آهیختن همربثه\u200cاند . از رسةٌ اوستائی 1308) بمعن ی کشیدن', '« بارنولمه ۷۸4 > « تب رکه ۷۰ ذیل ۲۵۳2908) >. ۱ - بر آهنجدن نژ بمحنی', 'بآوردن » جدا کردن : « پیدا شد که صورت معروف کنند؛ هیولی است ازمجهولی او » ومادت', 'مطلق اندر وهم آینده نیست مگ رکه نفس یاری عقل ازنخست مراورا بمیانجی سورت ثابت کند:']
```


## [2026-09-14T03:12:56.232Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 344 345 346 347 348 349 350; do echo \"--- leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -4; done",
 "description": "Scan BQT v1 leaves near p.128"
}
```


### [2026-09-14T03:12:57.480Z] TOOL RESULT

```
--- leaf 344
اعاء کلي اسطرلاب هفت‌عدد است : ۱ ام ۲۰ - عضاده , ۳ صفایح» نگ رن
۵ - فری » ٩‏ - فلس , ۷ - قطب .۰ ۶ التفهدم بیروئی مصحه جلال همایی ص و۲۸ - ۳۱۵ »
+ گاهنامه ۱۳۱۱ . سید جلال طهرانی ص ٩۷‏ - ۱۰۲ ۰
--- leaf 345
و
آلتی باش دکه بیشتر از برنج سازند و بدان‌ارفاع
افتاب و ستارکان کی ر ند . کویند سر آدرس
پیغمبر4 آنرا وضم کرده است » و بسنی گویند
--- leaf 346
که آنسخها از بدن اوجته برآن کس میخورد
وفرومیرود ؛ و گویندهرچنداورا بز ند فربه‌ترشود.
که خاریشت بر انداز باشد .
اسفا دور بفتح اول وسکون ئانی
--- leaf 347
۱۳
گذارندآ برامخود کشدوشراب‌رابگذارد,وباخا کتر
آن زخمی را که در ساعت زده باشند خشك بند
کنند » زود لیکو سازد . گرم و خهكت است
--- leaf 348
وفا ء قاضی ترسابانرا کویند وشخصی‌رانیز گویند
.از ابشان که بجهت رباشت خودرا بزنجیر :بندد.
گود اين لت عربی است
اسقلطسی ب سکن اوله وی کی
--- leaf 349
لک شود و اکر ساعتی توئف کند بفند
تشر
اسكث بکسر اول وسکون ثانی وکاف ؛
ای را کون که در راهها جهت قاصدان
--- leaf 350
اسکندروی
و دختثر از دارا حامله
بودوأنظهار نمیکردتابوی
دهن‌اورا با اسکندروی
```


## [2026-09-14T03:13:13.578Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- leaf 338\"; awk 'BEGIN{RS=\"\\f\"} NR==339' BQT_v1_pages.txt | head -25",
 "description": "BQT v1 leaf 338"
}
```


### [2026-09-14T03:13:14.619Z] TOOL RESULT

```
--- leaf 338
یعتی باز داشت و منم دفتن کرد .
استای بکر اول وسکون بای‌حملی,
امن استایی: است شش بایست :
استیر ب با بای ابجد بر وزن استخضر »
بمنی مطبر و کنده و غلیظ باشد ۴ .
۳
بزرکی هست بنابرآن بدین‌نام خوانند ؛ ومعرب
استالك س یکسر اول بر وزن مسوالك »
شاخی را کوبند که تازه از درخت ال روسده
باشد .
استام - . منم اول بروزن دشنام » سلخت
زین وبراق اسب 0 از طلا و نقره‌باشدب
سای اه لایر ای اس
استان ‏ بفتعح اول بروژن مستان » جای
خواب و آراکه ۱ 3
و
استا فیات ‏ بفتح اول بر وزن چسبانید »
۱ - استان صورت پوند مان ( در پپلوی یز 5020 «اووالا ۳۵۸ » ) در
کلسنان » بوستان » کوهستان ء بلوچنان » هندوستان وصررت بوند زمان درتابستان و زمستان
آمده (در این کلمات استان درلهجه های مر کزی صورت 65120 و در لپجه های شمالی ابران
صورت 250870 تلفظ میشود . بشکل بیشوند مکانی نیز در ۶ استان البهقباز الاسفل » و « اسان
البهفباذالاعلی » از کوره های جانب غربی سواد و « اسان سو » ناحیه‌ای درجبل و« استان‌المال »
کوره‌ای‌بمترب بغداد آمده (درهمةٌ این اسامی بکسر همزه). رک : ممجم البلدان؛ فرهنگستان»
استان را بهربك از ده ناحية ابران اطلاق کرده وآن لتاق از 69027 پهلوی است که بهربك از
ابالات عهد ساسالی اطلاق میشد « کرستنن . ساسان . ۱۳۹ .
```


## [2026-09-14T03:13:14.906Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'انداختن\\|انداز' BQT_v1_pages.txt | awk -F: '$1>9000 && $1<16000' | head -20",
 "description": "Find andaz in BQT v1"
}
```


### [2026-09-14T03:13:15.908Z] TOOL RESULT

```
9043:و لنگی و جامه و غیره بر زبرآن اندازند - و
9190:را یز گون که فاعل نوشیدن وکشیدن وانداختن
9211:بعمنی توشیدن- و کشیدن باشد. ویمعنی انداختن
9925:کون د که خارهای خودرا اند تیز اندازد وآنرا
10113:گوبند که آب دهن را جمم کردن و انداختن
10395:بمشی قدرو قیمت ومرتبه و حد واندازه‌باشد ۷
11460:عنیم اسب اندازد » منی بتازد .
11737:وانداختن هم آمده است - و بکتی اول بمعنی
11971:پی‌از 1: ن.که ک رکس‌ها ولاشه خوران گوشت جد وی را خوردند - او را ح رکودالی می‌اندازند ,
12097:که خاریشت بر انداز باشد .
12150:را ساحل اندازد » و
12356:وتختانی وزای‌هوزء برجتن‌وآلبزوجفته انداختن
12359:اسکیز است که برجمتن و آلیز انداختن ستور
12617:ثانی و رای بی نطه » خاریشت بزرک نیرانداز
12904:و تحرض کردن نادانان بجهت خصومت انداختن | سین بی‌قطه » یونانی صحرا! ویابالرا گوشد .
13207:۱ فعی فر بان کنابه از کمان‌تیراندازی
13230:ازیشوند 20-24 درساش‌کریت 6087 (کندن) « تب رک۱۳۵» ؛ انداختن» بدورانداختن »
13725:تعنانی و زای هوز . جفته و لکد انداختن اسب
13987:راکوند, که بعد از پوشش خانه بر بام اندازند
14148:است. واندازمومقیای‌ومقذار چیزی‌رانی زکویند ۱
```


## [2026-09-14T03:13:30.994Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:128 2>&1 | head -60",
 "description": "ref_page BQT:128"
}
```


### [2026-09-14T03:13:32.123Z] TOOL RESULT

```
no scan of BQT covers printed page 128 (see 'scans' in refs_online.json)
```


## [2026-09-14T03:13:37.032Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n '\\[pdf page' BQT_v1_pages.txt | sed -n '330,345p'; echo \"=== numerals near\"; for n in 336 337 339 340 341 342 343; do echo \"-- leaf $n:\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -2; done",
 "description": "Check pdf page tags and headers"
}
```


### [2026-09-14T03:13:38.349Z] TOOL RESULT

```
=== numerals near
-- leaf 336:
ابجد و ظهور های هوز ؛ مخفف اسباه است که
لشکر و سپاه باشد - و سگه را ليز کوشد که
-- leaf 337:
۱ ۷۲۳
ظروف می را سفید کند و اورا قلعی کر وسفید
-- leaf 339:
علم است بی حیوانات و نباتات » بر خلاف‌استه که اسقر » بروزن
متخصوص بانات لتعرتی کانه از مردم اصیل اف
-- leaf 340:
استرش -ایم اول و لت و قحرابم
و سکون‌شین قرشت ۰ آنی راکوبند کهزمین‌را
-- leaf 341:
وت ۱ تیم
استوی بش اول والث بر وزت بر
-- leaf 342:
استینه ۱
وورم وآمای کرده باشده وی سرعابی‌را گویشد
-- leaf 343:
راک ِ
۰
```


## [2026-09-14T03:13:48.837Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor w in ['اندام','انداختن','اندازه','انگور','انجیر','اندك']:\n    for m in re.finditer(w,t):\n        lf=t[:m.start()].count('\\f')\n        if lf>330:\n            print(w,'leaf',lf, repr(t[m.start()-60:m.start()+60].replace('\\n',' ')))\n            break\nEOF",
 "description": "Locate the ا+ن section in BQT v1"
}
```


### [2026-09-14T03:13:49.976Z] TOOL RESULT

```
اندام leaf 356 'ت و آن ای باشد که در آبگوشت ریزه کنند 9 - و بمعنی چین و شکن اندام نیز آمده است - و نام نوابی\u200cاست ازموسیقی . اشکو - بفتح '
انداختن leaf 337 ' هم آعده است ء واصح ابن است ۴ - و باول موم سرین و کفل حردم وانداختن هم آمده است - و بکتی اول بمعنی ستایش باشد - و امر با'
اندازه leaf 387 'اده ۷ » بروزن خمیازه ۰ یمانتهر چیز را گویند - و فیای کردن و اندازه گرفتن را نیز گفته\u200cاند , و تعرببش بهندسه کرده\u200cاند ۴ - '
انگور leaf 337 'ای باشد از ملك دکن ۹ استاقیل ۷۳ ۰ بر وزن اس\u200cافیل. بلفت رومی انگور را گوبند و بعریی عنب خوانند . ۴ رك : هستهواستخوان . ۸ '
انجیر leaf 385 'زن\u200cومعنی اجوخیدن است که برهم کشیده شدن پوست روواندام\u200cباشد . انجیره | نحو لد مس بر وزن مفلوك » نام دشتی و بیابانی\u200cاست نام'
اندك leaf 428 '\u200cایت در قرية هوا که\u200cیکی از فرای دامفان است گو مشد | کرانداد اندكك چیزی مردار درآن چشمه افتد باد و طوفان بمرتبه\u200cای شودکه '
```


## [2026-09-14T03:14:10.180Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== leaf 387\"; awk 'BEGIN{RS=\"\\f\"} NR==388' BQT_v1_pages.txt | head -50",
 "description": "BQT v1 leaf 387 andaze"
}
```


### [2026-09-14T03:14:11.411Z] TOOL RESULT

```
=== leaf 387
-۱۹۹ -
)اد « بروزن پرواژ ؛ ممنی شسد -
و میل نمودن - و حمله کردن باشد - و امر
باين معنی هم هست عنی فص دکن ومیل تمای -
است. واندازمومقیای‌ومقذار چیزی‌رانی زکویند ۱
و بممنی مصدرهم افخة ابت که انداختن ,اشد.
انداده ۷ » بروزن خمیازه ۰ یمانتهر
چیز را گویند - و فیای کردن و اندازه گرفتن
را نیز گفته‌اند , و تعرببش بهندسه کرده‌اند ۴ -
۰ بمعنی قدرت و فوت هم آمده است :
) ند ام ۴ « بروزن انجام , معروفت که
بدن رعنو آدمی باشد - و عر کاربر! نیز گویند
که آراسته و بنظام و با اصول بود - و بمعنی
زیبا ‏ و زیبایی هم آمده است - و ادب وآداب
و فاعده .ٍ روش را نیز کویند - و فنای خانه را
هم کنته اند .
ا او - بسکون واو . ترهتیزك باشد ,
/ آن سبزی است خوردنی د آنرا اهل مستان
نره میرم وعربان جرجیر خوانند , وبسضی کویند
جرجیر صحرایبی است که ابپقان باشد .
انداوه بفتح واو , مالهٌ استادان بثا
باشد , و آن افزارست که بدان کل و کچ بریام
ودیوار مالند - وشکوه وشکات - +غیبت رألیز
نند .
)ندایش بر وزن افزاش ؛ بسسنی
کاهگل کردن و گلابه و گچ‌مالیدن باشد .
| ند ایشگر ه بنتح تاف فارسی‌وسکون
رای فرشت. کاهگل و کلابه بربام ودیوار مالندمرا
گومثف .
آبدربایست
آثای4 « بروزن هسابه , بمعنی‌انداوه
. است که مالةٌ اسادان کل کار باشد - و شکوه
وشکایت - وغیبت را نیز گویند .
ودال بی‌نقطه مفترح بخای نفطه‌دار وسن بی‌لقَطةٌ
زده » حمات کننده ودشت ویتاه را گوشد ۰
اند خس و اده » اندخی‌سملوم. وواو
بالف کشنده و رای بی‌نقطة عفتوح ۰ قلعه وصاز-
وجایگاه ب ویناه رتکه گاه ماشد - و بناه دنله
ویشتیوانرا دز کنته‌انه 3
| فد جسیدن » بر وزن کم رضیدن ,
.حمایت سودن وپشتی کردن وپشاه دادن- و پناء
کرفتن باشد .
| فك ر؟ » بروزن بندر » بسعثی در باشد
وعریی فی کوبند حمجتانکه الدران و اندر خانه
هنی درون ودرخانه - و افاده ععنی شرت 0
میکند چون بامادر ویدر وخواهر وپرادر کیب
کنند همجو: مادراندر و پدر اندر و خواعر اندر
ار آب » بروزن منجلاب » شهری
است از ولات بدخشان مایین هندوستانوغزلن -
اندر بای » با بلی ایجد بروزن‌صتدل
```


## [2026-09-14T03:14:11.696Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 727 728 729 730 731; do echo \"=== leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -8; done",
 "description": "BQT v1 leaves near p.503"
}
```


### [2026-09-14T03:14:12.744Z] TOOL RESULT

```
=== leaf 727
کنابه از اشتیاق باشد .
تعه ۱ ع ما ثانی عشدد بر وزن بشه ۰
پيمانة روغن را گویشد .
ی « بفتح اول و کر انی و سکون
موز ریت کر کرین که خارهای خودرا
ات۴ - دتکراولمزیم! پرشیش را خوانند۲ .
نب هتح آول بروزن چمن » بمعنی
و لفزنده » آزعدس 2 داروهای چشم
=== leaf 728
کوبندا ‏ و بمعنی خوردلی وآذوقه ورأتب‌هم
آمده است - و بمعتی‌پیمانه هم هست - و نقاه
بر وزن شراره هم عیگویند .
ب‌- بنم هردو تای قرشت و سکون
هر دو غن نقطه دار . چیزی باه مالند کله
و قفیز که غله بدان پیمابند - و بعضی کویند
و بفتح ارل وثالث که تای فرشت باشد هم بمعنی
پيمانةٌ بزر که چهار خرواری باشد» و باین معنی
=== leaf 729
ات
هم‌آمدساست٩‏ - وکرم رفتن و کرم آمدن و کرم
کته رونت کته ۱ و بت خیم
وخرامان هم هست - و قهر و نب و گرم شدن
ازخشم وقهررا نیز کوبند؟ - و کیاهی‌است‌دوابی
که خوردن بیخ آن مانند تاتوله جنون آورد -
ونام موضعیاست ازمضافات یزد که از کمال صفای
هوا جامغع گرم سپر وسردسیر باشد.
=== leaf 730
قسیله - بر وزن غربیله . جنسی از
پارچة ابربشمی باشد کداز آن فبا وازار وچیزهای
دیگر نیز بدوزند.
فش - بسکون تانی بر وزن کفش ۰
سرزاش و طعنه را کوندا - و بکسر انی
حرارت و کرمی باشد؟ .
فشل - بر وزن مشعل» بمعنی اول نفش
است که طعنه وسرزش باشد .
=== leaf 731
اوح
ده » بفتح اول و سکون ثانی و دال
بی فقطهٌ مفتوح . بلفت بربرکشنیز را کوشد »
وآن دستنیی باشد که‌بشتردرآشهای بمار کنند,
و بعربی کژبیمخوانندا .
آقره ع بفتح اول و کسر ثانی و رای بی
قطةٌ مفتوح , بلفت بربر زبر؟ رومی را کویند »
ققر یر کردن ۰ کنابه از سخنی‌باشد
```


## [2026-09-14T03:14:29.119Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T03:14:29.169Z] TOOL RESULT

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


## [2026-09-14T03:14:34.558Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,40p' tools/fetch_source.py",
 "description": "Check fetch_source.py"
}
```


### [2026-09-14T03:14:34.600Z] TOOL RESULT

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
```


## [2026-09-14T03:14:42.031Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AE%D8%AA%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%A7%D8%AE%D8%AA%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D9%87%D9%86%D8%AF%D8%B3%D8%A9' \\\n 'https://en.wiktionary.org/wiki/%DA%AF%D8%AF%D8%A7%D8%AE%D8%AA%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%AF%D8%A7%D8%AE%D8%AA%D9%86' \\\n 'https://www.etymonline.com/word/toxic' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tek%CA%B7-' \\\n 'https://en.wiktionary.org/wiki/%CF%84%CF%8C%CE%BE%CE%BF%CE%BD' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 498, root Teku 1/Tekw' ; done",
 "description": "Archive web sources"
}
```


### [2026-09-14T03:14:50.925Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6b3e08ed266fcf95.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c9a323442b048666.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/34989f52fd107d89.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f483bbda47782c04.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a7a72e9265ab5861.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73f56310d941a7ec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/08830a9b6d599d52.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c4c1b9dee6e5cf31.txt
```


## [2026-09-14T03:14:53.787Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 6b3e08ed266fcf95 c9a323442b048666 a7a72e9265ab5861 f483bbda47782c04; do echo \"########## $f\"; grep -n -A12 -i 'Etymology' $f.txt | head -50; done",
 "description": "Read Wiktionary Persian etymologies"
}
```


### [2026-09-14T03:14:54.767Z] TOOL RESULT

```
########## 6b3e08ed266fcf95
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
72-
73- 1.4.1 
74- Conjugation 
75-
76- 1.4.2 
77- Derived terms 
--
159: Etymology
160- [ edit ] 
161-
162- From Middle Persian [Book Pahlavi needed] ( t'htn', t'c- /⁠tāxtan, tāz-⁠/ , “ to cause to run, to flow; to chase, to pour ” ) , [ 1 ] itself the causative form of Middle Persian [Book Pahlavi needed] ( thtn', tc- /⁠taxtan, taz-⁠/ , “ to run, to flow ” ) . Ultimately from Proto-Indo-European *tekʷ- . Cognate with Talysh تجه ( taja ) and Baluchi تاچگ ( tácag , “ to ride, drive; causative of تچگ ( tacag ) ” ) 
163-
164- Pronunciation
165- [ edit ] 
166-
167- ( Classical Persian ) IPA ( key ) : /taːx.ˈtan/ 
168-
169- ( Dari, formal ) IPA ( key ) : [t̪ʰɑːx.t̪ʰán] 
170-
171- ( Dari, formal ) IPA ( key ) : [t̪ʰɑːx.t̪ʰán] 
########## c9a323442b048666
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.3.2 
74- Derived terms 
--
148: Etymology
149- [ edit ] 
150-
151- From Middle Persian [Book Pahlavi needed] ( hndʾhtn' /⁠handāxtan⁠/ , “ to plan, allot, reckon, judge ” ) , from *ham- ( “ together, syn- ” ) +‎ *tač- ( “ to reach for, attain ” ) , the latter from Proto-Indo-European *tek- ( “ to stretch the hand, receive, reach ” ) and cognate with شاه ( šâh , “ king, shah ” ) , as well as Old English þiċġan ( “ to receive, accept ” ) and Lithuanian tèkti ( “ to be granted ” ) . See also اندازه ( andâze , “ size, scale ” ) .
152-
153- Pronunciation
154- [ edit ] 
155-
156- ( Classical Persian ) IPA ( key ) : /ʔan.daːx.ˈtan/ 
157-
158- ( Dari, formal ) IPA ( key ) : [ʔän̪.d̪ɑːx.t̪ʰán] 
159-
160- ( Dari, formal ) IPA ( key ) : [ʔän̪.d̪ɑːx.t̪ʰán] 
########## a7a72e9265ab5861
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.4 
74- References 
--
145: Etymology
146- [ edit ] 
147-
148- Inherited from Middle Persian [script needed] ( pldʾhtn' /⁠pardāxtan⁠/ ) , from Proto-Iranian *pari- ( “ peri-, around ” ) + *tač- ( “ to flow, run, walk ” ) . The former prefix is from Proto-Indo-Iranian *pári , from Proto-Indo-European *péri , while the latter component is from Proto-Indo-Iranian *ták- , from Proto-Indo-European *tekʷ- ( “ to hurry, rush, walk, flow ” ) . [ 1 ] 
149-
150- The "free" meaning comes from the same root, but with a different prefix (from the same origin), Proto-Iranian *para- ( “ farther, highest ” ) , from Proto-Indo-European *pér-o- ( “ distant, beyond ” ) .
151-
152- Pronunciation
153- [ edit ] 
154-
155- ( Classical Persian ) IPA ( key ) : /par.daːx.ˈtan/ 
156-
157- ( Dari, formal ) IPA ( key ) : [pʰäɾ.d̪ɑːx.t̪ʰän] 
########## f483bbda47782c04
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.4 
74- Further reading 
--
144: Etymology
145- [ edit ] 
146-
147- Inherited from Middle Persian [script needed] ( wtʾhtn' /⁠widāxtan⁠/ ) , from Proto-Iranian *wi- + *taHč- ( “ to melt ” ) , from Proto-Indo-European *teh₂-k- ( “ to melt ” ) , cognate with Northern Kurdish bihatin , bihoştin ( “ to melt ” ) . Compare Ancient Greek τήκω ( tḗkō , “ to melt ” ) .
148-
149- Pronunciation
150- [ edit ] 
151-
152- ( Classical Persian ) IPA ( key ) : /ɡu.daːx.ˈtan/ 
153-
154- ( Dari, formal ) IPA ( key ) : [ɡʊ.d̪ɑːx.t̪ʰán] 
155-
156- ( Dari, formal ) IPA ( key ) : [ɡʊ.d̪ɑːx.t̪ʰán]
```


## [2026-09-14T03:15:30.297Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '84963,85030p' POK_full.txt",
 "description": "Pokorny tek-1,2,3"
}
```


### [2026-09-14T03:15:30.355Z] TOOL RESULT

```
Root / lemma: tek-1 

Meaning: to produce; to bear 

Material: Old Indie takman-n. (Gramm.) " offspring, descendant, kid, child'; takant "ein 

Toil the weibl. Genitalien'; 

gr. tIktoo (*ti-tk-u)), etskov, ts^w, -0|jai, tetoko ' to give birth to children, zeugen', t£ko(; n. 
"kid, child; the young of an animal; Erzeugnis, scion, shoot', tekvov n. "kid, child' (: 
Germanic *t^egnaz), t6ko(; "das Gebaren, progeny, interest', tokI^cjo "leihe auf Zinsen', 
TOK£U(; "father, mother, PI. parents', Ionian eni-TO^, £ni-T£^ "the Niederkunft near '; 

Old Icelandic f^egnlree Untertan, free man'. Old English deg/7"Edelmann, warrior, 
hero, servant'. Old Saxon Old High German thegan ds., Modern High German Degen. 



References: WP. I 715, Mayrhofer 1 , 466. 
Page(s):1057 



Root / lemma: tek-2 

Meaning: to reach, stretch out the hand, get 

Material: The meaning "bid, beg, ask' only Germanic: Old Saxon thiggian^\v\yoke\ Old 

High German dicken, d/ggen stem V. "worum bid, beg, ask', Danish t/gge, Swedish t/gga 

"beg'. Old Swedish /=>/ggJa ds.; 



Old Icelandic /=>/ggJa' recede, annehmen', t^gegr{*t^egia-) "pleasant', Old Swedish 
P/'gg/a and Old Danish t/'gge a\so ' attain, achieve ', Old English d/cgan stem V. " attain, 
achieve, annehmen, consume'. Old Saxon th/gg/an 6s.; 

Old Irish techtaim^\ have', bret. tizaff^ receive ' (due to eines *fekfa^6as Empfangene, 
property'), cymr. /e^ 'beautiful, pretty' (compare to meaning Old Icelandic l=>3egi). Old Irish 
etig= cymr. annheg^\x<^\)i' {*n-teki-)\ ograde probably Old Irish /o/c/7"naturgemafl' 
(different under top-); 

Lithuanian tenku, /eM'sich erstrecken, reichen, ausreichen, sufficient have; zuteil 
become, zufallen'; kir. taknutylee\; touch on'. 

References: WP. I 715, Kuiper Indo Germanic Nasalpras. 186 f. 
Page(s): 1057-1058 

Root / lemma: tek-3 

Meaning: to weave, plait 

Material: Osset. taxun'to weave', an-dax^ filament ' (xfrom A); Armenian f ek em^ turn, 

twist, rotate, flechte, wickle', t'iur{*tek-ro-) " twiddled, twisted, rotated, revved, revolved '; 

Old High German taht'\N\ck, cord'. Modern High German Docht= Old Icelandic f^attr^cor6 

in a Sell', Swiss dsegel, dohe. Bavarian dahen, elsass. ddche'\N\ck' (proto Germanic *f^eh- 

, Peg-); also Old Icelandic f^segja ' press' actually "zusammendrehen'? about Old Church 

Slavic tbkat/'to weave' see above S. 1032. 

References: WP. I 716, WH. II 678 f.
```


## [2026-09-14T03:15:31.891Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'handāxtan\\|hand[aā]z\\|ham-tač\\|hqm.tac\\|TAK\\b\\|TAČ\\|tač' CHEUNG.txt | head -30",
 "description": "Cheung handāxtan"
}
```


### [2026-09-14T03:15:31.979Z] TOOL RESULT

```
4550:Pres. ja: IND. 3sg. YAv. daZaiti (Y 71.8), YAv. handazaiti (V 5.9), INJ. 3sg. YAv. daZat (F 548), YAv. 
24302:*tač! ‘to flow, run, walk’ 
24417:pld’c- /pardaz-/ ‘to accomplish’ || (+ *ham-) MMP hnd’c-, BMP hnd'c- / handaz-/ ‘to 
24423:BMP hnd’cyt /handazed/, 3р1. MMP hnd’cynd; Partic.: perf. pass. MMP hnd’xt, Pass.: pres. IND. 35р. 
24445:attain, receive’. As for MP /handaz-/ (NP andaz-), it is worth citing the example, 
24447:handazéd ‘and as I [standing on the ground] do not reach up to that haoma [placed at 
35210:hnd'c- /handaz-/, 374 
55518:*pad, *tač (s.v.), *ға(п)с
```


## [2026-09-14T03:15:34.872Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24300,24320p;24410,24470p' CHEUNG.txt",
 "description": "Cheung *tač entry"
}
```


### [2026-09-14T03:15:34.935Z] TOOL RESULT

```
*tač! ‘to flow, run, walk’ 

*AVESTAN: YAv. tac- ‘to flow; walk’ || (+ *apa-) ‘to flow away’ || (+ *abi-) ‘to flow 
towards’ || (+ *pari-) ‘to run around, encircle’ || (+ *fra-) ‘to flow to’. Ф On the Av. 
desid. formation tixsonti see Hoffmann (apud Mayrhofer, Fs Morgenstierne: 142f.). 
c» Liste: 24 

Pres. {1} them.: IND. 35р. YAv. fratacaiti (Y 65.3 f., Yt 5.3 f., Yt 5.15, etc.), 3pl. YAv. fratacinti (Y 65.3, 
Yt 5.3, Yt 5.15, etc.), INJ. 3sg. YAv. tacat (Y 16.8), YAv. apatacat (Y 9.11, Yt 19.56), Y Av. pairi.tacat 
(Yt 17.26), 3pl. YAv. apatacin (V 5.12), Y Av. fratacin (Yt 13.78), SUBJ. 1sg. YAv. atacani (Yt 5.38), 
3pl. YAv. tacanti (Yt 8.5), OPT. 3sg. YAv. tacöit (V 8.100 ff.), IMPV. 2sg. YAv. taca (F 18); Pres. {2} 
athem.: IND. 2sg. med. YAv. taxse (Y 10.17), SUBJ. 3pl. YAv. apa.tacin (V 5.12); Partic.: pres. {1} 
Y Av. tacint- (Yt 6.2, Yt 10.20, V 6.26, etc.), YAv. (Gpl.) aiBi tacaintam (ViD 4), Y Av. atacint- (Yt 8.42), 
perf. YAv. -fratat.kus- (Yt 13.53); Caus.: pres. IND. 3pl. YAv. tacaiieinti (Yt 14.54), INJ. 3sg. ҮАУ. 
*fratacaiiat (У 2.34), IMPV. 2sg. Y Av. "fratacaiia (V 2.26); Desid.: pres. IND. 3pl. YAv. "tixsonti (Y 
9.22) 


*taé 1 373 
208; Korn 2005: 313, 364 (passim) 


*ta(? “to reach for, attain, receive’ 

*MIDDLE PERSIAN: (+ *para-) MMP prdx- (pret. stem) ‘to be done with, freed of, deal 
with, be exhausted’, BMP pldc- /pardaz-/ ‘[+ ’c- /az-/] to be free from’, (caus.) BMP 
pld’c- /pardaz-/ ‘to accomplish’ || (+ *ham-) MMP hnd’c-, BMP hnd'c- / handaz-/ ‘to 
plan, allot, reckon, measure’, MMP hnd’c- ‘to throw (?)’ (Sundermann 1978: 488, n. 
25) = DMMPP: 278a, 180a 

(+ *para-) Pres.: IMPV. 2sg. BMP pldc /pardaz/; Partic.: perf. pass. MMP prdxt, caus. BMP pld'ht 
/pardaxt/; Inf.: BMP pldhtn /pardaxtan/, caus. BMP pld’htn /pardaxtan/ || (+ *ham-) Pres.: SUBJ. 3sg. 
BMP hnd’cyt /handazed/, 3р1. MMP hnd’cynd; Partic.: perf. pass. MMP hnd’xt, Pass.: pres. IND. 35р. 
MMP hnd’cyhyd 

*KHOTANESE: (+ *ара-) patajamata- ‘defeat, overthrow’ (Skjaerve, SVK III: 84 f.) 
*NWIR: (+ *para-, *pari-) NP pardaxtan/pardaz- ‘pay, settle, finish, accomplish’, Gz. 
pardaz-/pardaza, Khuns. pirdäz- ‘to get ready to do something’ || (+ *ham-) NP 
andäxtan/andäz- ‘to throw; to afflict, exhaust’, (?) Siv. nàs-/nàt ‘to throw’ 

*NEIR: Oss. D. taxun/taxt (old denomin.) ‘to equip, dress (up)’ || (+ *fra-) Oss. D. 
radaxsun/redaxst ‘to climb (a mountain)’ (< *to reach for the top’) || (+ *ham-) 


*taH 375 


Oss. І. andazyn/aendagd, D. ændæzun/ændağd ‘to stick, be stuck to’, I. 
endazyn/endagd, D. endazun/zndagd (old caus.) ‘to attach, stick to’ 

© The meanings of the forms above are often difficult to reconcile with that of *tac! 
‘to run, flow’ or *taHé ‘to melt’. They may point to another, homophonous root. The 
IE root *tek- ‘to stretch the hand, receive, reach’ is perhaps the best candidate. The 
meaning of NP pardaxtan/pardaz- ‘to pay, settle’ may derive caus. *to cause to 
attain, receive’. As for MP /handaz-/ (NP andaz-), it is worth citing the example, 
given by Nyberg II, l.c. (in revised transcription): u-m ... ¿Iyon ul 6 an hom në 
handazéd ‘and as I [standing on the ground] do not reach up to that haoma [placed at 
the top of the tree]’. If the formation with the prev. *ham- originally meant ‘to 
stretch, reach together’, we may easily arrive at the meaning of the Oss. reflexes: ‘to 
stick; [caus.] to attach’. 

«PIE *tek- ‘to stretch the hand, receive, reach’ = LIV: 618 f. | Pok.: 1057 f. 

*IE COGNATES: Lith. tekti ‘to reach (out), suffice, receive’, OE bicgan ‘to receive, 
take’, Ukr. tjaknuty ‘to touch’ 


*REFERENCES: Fraenkel II: 1077; Nyberg II: 94b; Abaev, Slovar’ II: 360 f.; DKS: 204a; WIM IV1: 83 f.; 
Abaev, Slovar’ III: 242 f. 


*taH ‘to flow, stream; to melt’ 

*AVESTAN: YAv. tat.ap- ‘with flowing waters’, ? YAv. tata- ‘falling, dripping, 
rising?’. © The interpretation of Y Av. tat ‘flowing’ (in the comp. YAv. tat.ap-) was 
given by Benveniste (ELO: 45). More recently, Panaino, Tist.: I, 135 f. revived the 
possibility that YAv. tatand YAv. täta- derived from the root *pat (cf. Bartholomae, 
AIW: 631, 646). This may be supported by the Homeric concept of бїїлєтїїс 
rotauög ‘river fed by rain (fallen from the sky)’. = Liste: 25f.
```


## [2026-09-14T03:15:48.029Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'taHč\\|taH¢\\|taHc\\|vitaxti\\|widāxtan\\|wid’x\\|gudāxtan\\|gudaxtan' CHEUNG.txt | head -20",
 "description": "Cheung *taHč melt"
}
```


### [2026-09-14T03:15:48.093Z] TOOL RESULT

```
24524:*NWIR: (+ *ш-) NP gudaxtan/gudaz- ‘to smelt, melt’, ? Kurd. (Kurm.) 
41043:gudaxtan/gudaz-, 376 
57203:*taH, *taHc
```


## [2026-09-14T03:15:50.259Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24495,24560p' CHEUNG.txt",
 "description": "Cheung *taHč entry"
}
```


### [2026-09-14T03:15:50.357Z] TOOL RESULT

```
*IE COGNATES: Arm. t‘anam ‘I dive’, OCS tajeti ‘to melt’, ? Welsh tawdd ‘melts’ 
*REFERENCES: КРЕТ. 142a; EVP: 79; KPF II: 189; Abaev, Slovar’ I: 180; MacKenzie 1966: 110; EVS: 
52a, 93b’ DKS: 2b; Abaev, Slovar’ III: 222 f.; Abaev, Slovar’ IV: 7 f.; Cabolov 1997: 74; NEVP: 84 


*taH ‘to melt’ 
*MIDDLE PERSIAN: (+ *ui-) MMP wdc- ‘to melt [intr.]’, BMP wt’c- /widaz-/ (caus.) 
‘to melt [tr.], BMP wt’cyn- /widazén-/ (sec. caus.) Чо cause to melt? = DMMPP: 


339b 
Pres.: IND. 3sg. MMP wadcyd; Partic.: perf. pass. BMP wt'htk /widaxtag/, BMP wt’ht /widaxt/; Caus.: 
pres. IND. 3sg. BMP wt'cyt /widazed/, BMP wt'cynyt /widazénéd/; Inf.: caus. BMP wt'htn /widaxtan/ 


*PARTHIAN: (+ *ui-) wdc- ‘to melt’, w(y)d'c- (caus.) ‘to dissolve" = Ghilain: 50, 47 
| DMMPP: 338b £. 

Pres.: IND. 3sg. wdcyd; Caus.: IND. 35р. wd’cyd, wyd’cyd; Partic.: perf. pass. "wdxtg; Inf.: "wdxtn 
*KHOTANESE: (+ *ui-) LKh. byaj- (byas-) ‘to dissolve’ = SGS: 104 

*SOGDIAN: (+ *ui-) BSogd. wyt’wxs ‘to disappear, melt away’, BSogd. wyt’yc ‘to 
melt’ 

(+ *ui-) Pres.: IND. 3sg. BSogd. wyt’wxsty, BSogd. wyt’wxst’y, CSogd. “wytwxsty; Partic.: perf. pass. 
BSogd. wytwytk ‘molten’; Caus.: pres. IND. 3sg. BSogd. wyt’yct 


*NWIR: (+ *ш-) NP gudaxtan/gudaz- ‘to smelt, melt’, ? Kurd. (Kurm.) 
bihöstin/bihös- ‘to melt’ (why -0- ?) 

9 The close match in meaning between the Ir. and Gr. forms suggests a common IE 
origin. Hence, the formally identical forms with the meaning ‘to run, walk, sim.’ 
should be excluded (*ta&!). *taHé appears to be an enlarged root of *taH. 

«PIE "enlarged" *teH5k- ‘to melt" = LIV: 617 | Pok.: 1053 


*IE COGNATES: Gr. 14c, (Dor.) тако ‘I melt [tr.]', (Hom.) ёт@кту ‘melted [intr.]’ 
*REFERENCES: Horn 1893: 199; Nyberg II: 217a; DKS: 307b; Gharib: 427b; Cabolov 2001: 175 


*tamH ‘to faint, be tired’ 


*PARTHIAN: t’m-, t^m- (intr.) ‘to choke’ > DMMPP: 321b 

Partic.: perf. pass. П t’m’dg, t’m’d 

*KHOTANESE: ttamd ‘fatigue’ || (+ *pati-) pätem- (pátaunda-, pyau-) ‘to confound’ || 
(+ *ui-) OKh. bitam- (bitan-) ‘to doubt, be perplexed’. 0 pátem- does not derive 
from a caus. form *pati-tamaja- (SGS: 83), but must derive from a ja-pres. stem: 
*pati-tam-ja-. The expected caus. form should be *tamaja-, cf. Skt. tamaya-, which 
clearly points to the presence of a laryngeal after m (i.e. Brugmann’s Law). = SGS: 
83, 95 

*SOGDIAN: MSogd. f^s'ó (ppp., inch.) ‘tired’, MSogd. tns ‘longing, regret’ (cf. GMS: 
8525) || (+ *aua-) CSogd. wts(-) ‘to complain’ || (+ *pati- MSogd. pt’’m 
‘unconscious’ 


*tané 377 


(+ *aua-) Pres.: IND. 3sg. CSogd. "wtst (cf. Sims-Williams 1985: 131); Impf.: IND. 3sg. w’ts
```


## [2026-09-14T03:16:21.521Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 498 -l 498 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg498 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg498.png",
 "description": "Render PDF page 498"
}
```


## [2026-09-14T03:16:23.023Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT taxra\"; grep -n 'taxra-\\|tacan-\\|hqm.tacina\\|hqm\\.tak' BRT.txt | head -10",
 "description": "Bartholomae taxra, tacan"
}
```


### [2026-09-14T03:16:23.279Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 86756 Sep 13 23:16 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg498.png
```


### [2026-09-14T03:16:23.338Z] TOOL RESULT

```
=== BRT taxra
11807:er  dann  laufen  .  .  er  soll  laufen,  bis den  ersten  (ihm  aufstossenden  Menschen)  j erreicht"  V.A'.ioo;  103;  —  yff  yrff/(sd.)  [ *tacS  {'SS.y  Aam^rvhaoa  .  .Vt.io.ji;  — ' nffij  ^usyaj  (sd.)  tacS  (NS.)  nsil  *msyqs Aog.60;  —  /acintä  (HP.)  ndit  apayänti ,  ,  barTntS  . .  vas)titö  YL  10. 20;  —  taca (aS.)  F./&  S.  noch  tacan-,  i)  ins-| besondere  von  Flüssigkeiten  'fliessen, strämen':  ka^a  xä  .  .  apqm  taisnti  nava "wann  werden  die  Wasserquellen  aufs  neue fliessen?"  Yt.  8.  5;  —  anham  raya  . .  gps Uieinti\t.i^.\\;  io,V.5.i9;  —  aptm  tacln- /a«(ASf.j»  Vt.6.i,V.ig.26.  a)  Kaus. 'fliessen  lassen':  yqt  . .  uo/iunim  . .  taca- ya'nii  Yt.i4.$^.
11869:•  j.  tacan-  Adj.  laufend':  *ayS  va  va (NS.)  vä  *hi^)mns  vä   anhunö  vä  N,  97,
26551:•  j,  staxra-  Adj.  'stark,  fest',  inbes.  vom Winterfrost  'streng':  TS  mrUrS  ty&  V, 2.  22;  F.  /2;  —  zaya  ava%a  °rS  yat  .  . "der  Winter  ist  darum  (so)  streng,  weil . ," FrW. 8.t;  —  'rahe  FrW.  8.  a.
```


## [2026-09-14T03:16:32.595Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg498.png"
}
```


### [2026-09-14T03:16:33.179Z] TOOL RESULT

```

```


## [2026-09-14T03:16:33.175Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:16:47.439Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('pg498.png')\nprint(im.size)\nw,h=im.size\nim.crop((int(0.17*w),int(0.55*h),int(0.62*w),int(0.72*h))).resize((int(0.45*w*2.2),int(0.17*h*2.2))).save('pg498-crop.png')\n\"; ls",
 "description": "Crop bottom-left arrows"
}
```


### [2026-09-14T03:16:48.739Z] TOOL RESULT

```
(1700, 2200)
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
404-top.png
411-top.png
412-zoom.png
414-bot.png
417hi.png
417-top.png
417-zoom.png
421-top.png
428hi.png
428-zoom2.png
428-zoom.png
429hi.png
429-zoom.png
431-top.png
432-bot.png
436-full.png
440-top.png
442hi.png
442-zoom.png
444hi.png
444-zoom.png
445-mid.png
446-full.png
450hi.png
450-zoom.png
454-top.png
457hi.png
457-zoom.png
460-top.png
462-full.png
466hi.png
466-mid.png
472-top.png
474hi.png
474-zoom.png
afm74-420.png
afm76-421.png
agents.txt
ahd430.txt
asha-468.txt
beekes410.txt
bly78-473.png
bqt1328-ftr-437.png
bqt1328-hdr-437.png
bqt1328-top-437.png
bqt1330-top-437.png
bqt1-440.txt
bqt2123-fn-435.png
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
bqt439-l254.jpg
bqt469-n486-bottom.png
bqt469-n486.jpg
bqt469-n486-top.png
bqt469-n547-bottom.png
bqt469-n547-fn2.png
bqt469-n547-hdr.png
bqt469-n547.jpg
bqt469-n547-mid.png
bqt469-n547-top.png
bqt-482-389-foot.png
bqt-482-389.jpg
bqt-482-390-foot2.png
bqt-482-390-foot.png
bqt-482-390.jpg
bqt508-495-bl2.png
bqt508-495-bl.png
bqt508-495.jpg
bqt509-495.jpg
bqt509-495-tr.png
build2-434.py
build2-471.py
build3-434.py
build-389.py
build-390.py
build-391.py
build393.py
build-394.py
build-395.py
build-396.py
build-398.py
build-400.py
build-401.py
build-405.py
build-406.py
build-407.py
build-412.py
build-414.py
build-415.py
build-417.py
build-418.py
build-419.py
build-422.py
build-425.py
build-426.py
build-428.py
build-429.py
build-430.py
build-431.py
build-434.py
build-435.py
build-438.py
build-439.py
build-440.py
build-444.py
build-445.py
build-446.py
build-447.py
build-448.py
build-450.py
build-452.py
build-453.py
build-454.py
build-455.py
build-458.py
build460.py
build-461.py
build-463.py
build-464.py
build-465.py
build-468.py
build-470.py
build-471.py
build-472.py
build-473.py
build-474.py
c404-empty.png
c404-greek.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
c412_cedar.png
c412_makrome.png
c412_makrome_zoom.png
c412_meqrameh.png
c412_meq_zoom.png
c412_sedr_zoom2.png
c412_sedr_zoom.png
c442-fa8b.png
c442-fa8c.png
c442-fa8.png
c442-samavar2.png
c442-samavar3.png
c442-samavar.png
c442-symp-zoom2.png
c442-symp-zoom.png
c497-arabic.png
c497-shakuk.png
crop14-394.png
crop18-394.png
crop411_a.png
crop411_b.png
crop411_c.png
crop419_a.png
crop419_b.png
crop419_c.png
crop419_d.png
crop419_grk.png
crop419_skt.png
crop428a.png
crop428b.png
crop428c.png
crop428d.png
crop-437.png
crop460-fa.png
crop460-latin.png
crop460-mithere.png
crop460-shamunhdr.png
crop460-shamun.png
crop468a.png
crop480_astro.png
crop480_chol2.png
crop480_chol.png
crop480_ster.png
crop491b.png
crop491c.png
crop491.png
crop496-a.png
drd496.wiki
e0-434.json
edit_about.py
edit_research.py
ffd492-055.png
ffd492-056.png
ffprof
gen-420.py
irn-425.pdf
irn-425.txt
kent2-448.txt
kent-448.txt
knt-440.txt
knt443.txt
meta-443-knt.json
mw1084-488.pdf
mw1084-488.txt
mw1085-488.pdf
mw1085-488.txt
mw1086-488.pdf
mw1086-488.txt
mw1087-488.pdf
mw1087-488.txt
oew459.txt
out488.bin
part1-471.json
pg390b.jpg
pg390b.png
pg390.png
pg391big.png
pg391crop.png
pg391.png
pg391root.png
pg391sog.png
pg392.png
pg393.png
pg394hi.png
pg394.png
pg397.png
pg398.png
pg399-crop1.png
pg399-greek.png
pg399.png
pg399-sog.png
pg400big.png
pg400_fa_heli.png
pg400_fr2.png
pg400_french.png
pg400_kasak2.png
pg400_kasak3.png
pg400_kasak.png
pg400.png
pg402.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
pg409.png
pg410hi.png
pg410-k2.png
pg410-kadm2.png
pg410-kadm.png
pg410-persian.png
pg410.png
pg410-q2.png
pg410-qedam.png
pg411_300.png
pg411.png
pg412_hi.png
pg412.png
pg412_uhi.png
pg413.png
pg414-greek.png
pg414.png
pg415-emptybox.png
pg415hi.png
pg415.png
pg416-v.png
pg417.png
pg418hi.png
pg418.png
pg418-raj2.png
pg418-raj3.png
pg418-rajidan.png
pg419_hi.png
pg419.png
pg420b.png
pg420.png
pg421.png
pg422.png
pg423.png
pg424.png
pg426.png
pg428hi.png
pg428.png
pg429-crop1.png
pg429-crop2.png
pg429-crop3.png
pg429hi.png
pg429.png
pg431.png
pg432.png
pg433.png
pg435-n1.png
pg435-n4.png
pg435.png
pg436.png
pg437-437.png
pg437hi-437.png
pg438.png
pg439.png
pg440.png
pg442hi-442.png
pg442-p442.png
pg442uhi-442.png
pg443.png
pg444.png
pg444-serom.png
pg444-sibum.png
pg445-crop.png
pg445.png
pg446.png
pg447-crop.png
pg447.png
pg449.png
pg450hi.png
pg450-pechkam.png
pg450.png
pg450-shangarf.png
pg451.png
pg452.png
pg453.png
pg454.png
pg456-germ.png
pg456hi.png
pg456.png
pg457_crop3b.png
pg457_crop3c.png
pg457_crop3.png
pg457hi.png
pg457.png
pg458.png
pg459.png
pg460hi.png
pg460.png
pg462-fa.png
pg462hi.png
pg462.png
pg462-sog2.png
pg462-sog.png
pg463-v.png
pg464.png
pg465.png
pg466-crop1.png
pg466-crop2.png
pg466-crop3.png
pg466hi.png
pg466-osqof.png
pg466.png
pg467.png
pg468hi.png
pg468.png
pg469.png
pg470.png
pg471.png
pg472-crop.png
pg472hi.png
pg472.png
pg473.png
pg474.png
pg474-sogd.png
pg475.png
pg476.png
pg477.png
pg479.png
pg480hi.png
pg480.png
pg482hi.png
pg482.png
pg482-tow2.png
pg482-tow3.png
pg482-tow.png
pg484.png
pg485.png
pg486.png
pg487.png
pg488.png
pg490.png
pg491big.png
pg491.png
pg493.png
pg494hi.png
pg494.png
pg494-root.png
pg494-tambour.png
pg495.png
pg496hi.png
pg496.png
pg497.png
pg498-crop.png
pg498.png
pla18-468-crop.png
pla18-468.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
write409.py
write410.py
write436.py
write469.py
write476.py
```


## [2026-09-14T03:16:51.827Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg498-crop.png"
}
```


### [2026-09-14T03:16:51.862Z] TOOL RESULT

```

```


## [2026-09-14T03:17:08.601Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; python3 - <<'EOF'\nimport json,glob\nfor f in glob.glob('page-*.json'):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            if 'blank' in (n.get('derivation') or '').lower() or 'empty box' in (n.get('derivation') or '').lower():\n                print(f, n.get('id'), n.get('verdict'), (n.get('derivation') or '')[:260]); print(' error_in:',n.get('error_in'),'| lang',n.get('lang'))\nEOF",
 "description": "Find precedent for blank boxes"
}
```


### [2026-09-14T03:17:10.244Z] TOOL RESULT

```
<persisted-output>
Output too large (42.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bi00lxe4g.txt

Preview (first 2KB):
page-400.json 24 unverified Blank, unlabelled box in the printed chart, arrowed from the Avestan box (fra-ptaražât, paiti-pasti); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after check
 error_in: extraction | lang None
page-400.json 25 unverified Blank, unlabelled box in the printed chart, arrowed from the Old Persian box (ud-pat, ud-a-pat-atâ); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checki
 error_in: extraction | lang None
page-203.json 2 unverified Empty pass-through box. On the printed page (pdf p. 203, book p. 173; see data/verification/sources/refs/ocr/BOOK/203.png) the large rectangle to the right of the Avestan/Old Persian box is drawn but left completely blank — no language, no reference, no word. 
 error_in: None | lang None
page-203.json 4 confirmed Empty pass-through box: the printed page shows a French box with no word in it, standing between the Greek box and the Persian one. The forms it stands for are French diabète (a learned borrowing of Late Latin diabētēs, Greek diabētēs, in medical French from t
 error_in: None | lang French
page-203.json 2 unverified Empty pass-through box: on the printed page (data/verification/sources/refs/ocr/BOOK/203.png) the rectangle to the right of the Avestan box in the Gwadh chart is drawn but left blank — no language, no reference, no word. The extraction is faithful and there is
 error_in: None | lang None
page-305.json 9 unverified Blank box in the printed chart (p.275), drawn to the right of the Avestan ragu/ravi box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extraction and was added by the owner.
 error_in: extraction | lang None
...
</persisted-output>
```


## [2026-09-14T03:17:30.193Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -B3 -A12 'Etymology' c4c1b9dee6e5cf31.txt | sed -n '1,60p'; echo \"#### PIE tekw\"; grep -n -A25 'Reconstruction' 08830a9b6d599d52.txt | head -60",
 "description": "Read toxon and PIE tekw wiktionary"
}
```


### [2026-09-14T03:17:30.266Z] TOOL RESULT

```
59- Toggle Ancient Greek subsection 
60-
61- 1.1 
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
--
158- Ancient Greek
159- [ edit ] 
160-
161: Etymology
162- [ edit ] 
163-
164- Possibly a cognate of Latin taxus or borrowed from Iranian : compare Persian تخش ( taxš , “ crossbow ” ) .
165-
166- Compare typologically English yew ( “ Taxus; a bow for archery, made of yew wood ” ) , which is cognate with Proto-Slavic *jьva , which is synonymous with *orkyta , which is possibly cognate with Latin arcus .
167-
168- Pronunciation
169- [ edit ] 
170-
171- IPA ( key ) : /tók.son/ → /ˈtok.son/ → /ˈtok.son/ 
172-
173- ( 5 th BCE Attic ) IPA ( key ) : /tók.son/ 
#### PIE tekw
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tek%CA%B7-
2-FETCHED: 2026-09-14T03:14:50Z
3-STATUS: 200
4:TITLE: Reconstruction:Proto-Indo-European/tekʷ- - Wiktionary, the free dictionary
5-
6:Reconstruction:Proto-Indo-European/tekʷ- - Wiktionary, the free dictionary 
7-
8- Jump to content 
9-
10- Main menu 
11-
12- Main menu
13-
14- move to sidebar 
15- hide 
16-
17- Navigation
18-
19- Main page 
20- Community portal 
21- Requested entries 
22- Recent changes 
23- Random entry 
24- Help 
25- Glossary 
26- Contact us 
27- Special pages 
28-
29- Search 
30-
31- Search 
--
65: Reconstruction 
66-
67- 1.3 
68- Root 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.4 
74- References 
75-
76- Toggle the table of contents 
77-
78: Reconstruction:Proto-Indo-European/ tekʷ- 
79-
80- Add languages 
81-
82: Reconstruction 
83-
84- Discussion 
85-
86- English 
87-
88- Read 
89-
90- Edit 
91-
92- View history
```


## [2026-09-14T03:17:34.138Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '95,175p' 08830a9b6d599d52.txt; echo \"##### etymonline toxic\"; grep -n -A10 -i 'toxic' 73f56310d941a7ec.txt | head -40",
 "description": "PIE tekw root page + etymonline"
}
```


### [2026-09-14T03:17:34.213Z] TOOL RESULT

```
 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Alternative reconstructions
 [ edit ] 

 *tek- 

 Reconstruction
 [ edit ] 

 The reconstruction of the root-final stop faces some contention with most older sources preferring the labiovelar *kʷ , [ 1 ] [ 2 ] while other sources question [ 3 ] [ 4 ] or outright reject the labiovelar [ 5 ] [ 6 ] in favor of the plain velar *k .

 The evidence in favor of the labiovelar consists primarily of the Hittite 𒉿𒀜𒆪𒍖𒍣 ( wa-at-ku-uz-zi /⁠watkuzi⁠/ , “ to jump (out of), to flee ” ) , which must come from an athematic stem ending in *kʷ and which may come from a univerbation of *wé-tkʷ-ti . Kloekhorst mentions, however, that this could also be a root *wetkʷ- comparable to stems such as *h₂edʰǵʰ- or *tetḱ- . [ 7 ] 

 Also, there is the proposal that Proto-Germanic *þewaz ( “ servant ” ) came from earlier *þehwaz from *tekʷós . While Kroonen prefers the Germanic-only root *tew- , [ 4 ] the EIEC ascribe this and other such forms as *-w- extensions of the root. [ 5 ] If the Sanskrit तकु ( táku , “ running along ” ) represents a *-u- stem adjective *tékʷ-u-s ~ *tkʷ-éw-s , this could explain the appearance of this extension.

 In favor of the plain velar is the Tocharian B cake ( “ river ” ) from Proto-Tocharian *cäke , which Adams derived from *ték-es- or *ték-ont- meaning “that which flows.” [ 6 ] 

 Ambiguously, the general absence of Proto-Brythonic *-b- in the descendants of Proto-Celtic *tek(ʷ)eti ( Middle Breton techet , Cornish têgh , Middle Welsh techu ) points to the velar being plain. Matasović, however, gives the explanation that the Brythonic *-x- was derived from the Celtic *-s- subjunctive: *tekʷs- > Brythonic *tex- , and that the labiovelar does surface in the form Old Welsh ny-de b it ( imperfect impersonal relative ) found in Aneirin . [ 8 ] 

 Root
 [ edit ] 

 *tekʷ- ( imperfective ) [ 1 ] [ 2 ] [ 9 ] [ 7 ] 

 to run , to flow 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *tekʷ- (25 c, 0 e) 

 *tékʷ-ti ~ *tkʷ-énti ( athematic root verb ) or *tékʷ-e-ti ( thematic root verb ) [ 8 ] [ 10 ] [ 11 ] [ 12 ] [ 3 ] 
 Proto-Albanian: *en-teka 
 Albanian: ndjek 

 ( perhaps ) Anatolian:
 Hittite: 𒉿𒀜𒆪𒍖𒍣 ( wa-at-ku-uz-zi /⁠watkuzi⁠/ ) (< *wé-tkʷ-ti )

 Proto-Balto-Slavic: *tektei 
 Latgalian: tecēt 
##### etymonline toxic
1:URL: https://www.etymonline.com/word/toxic
2-FETCHED: 2026-09-14T03:14:49Z
3-STATUS: 200
4:TITLE: Toxic - Etymology, Origin & Meaning
5-
6:Toxic - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
--
21: Origin and history of toxic 
22-
23: toxic (adj.) 
24-
25: 1660s, "of or pertaining to poisons, poisonous," from French toxique and directly from Late Latin toxicus "poisoned," from Latin toxicum "poison," from Greek toxikon (pharmakon) "(poison) for use on arrows," from toxikon , neuter of toxikos "pertaining to arrows or archery," and thus to a bow, from toxon "bow," which has been regarded as a loan-word from Scythian.
26-
27- Watkins suggests a possible source in Iranian  taxša-  "bow" (from PIE  *tekw-  "to run, flee"). Beekes, pointing to the early attestation of the Greek word, suggests a Pre-Greek origin.
28-
29: As a noun from 1890. Related: Toxical . Compare intoxicate . Toxic waste is by 1888 in medicine, "toxin;" by 1955 as "chemical or radioactive waste."
30- also from 1660s 
31-
32: Entries linking to toxic 
33-
34: intoxicate (v.) 
35-
36: mid-15c., "to poison, kill with poison" (obsolete), from Medieval Latin intoxicatus , past participle of intoxicare "to poison," from in- "in" (see in- (2)) + Latin toxicare "to poison," from toxicum "poison" (see toxic ). The meaning "make drunk" is recorded by 1570s (implied in intoxicated ). The figurative sense of "excite to a high pitch of feeling" is attested from 1590s. Related: Intoxicating .
37-
38: antitoxic (n.) 
39-
40: "substance which counteracts a poison," 1860; from anti- "against" + toxic . As an adjective, "counteracting a poison," from 1862.
41-
42: cytotoxic 
43: detoxicate
```


## [2026-09-14T03:17:46.504Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(720,742):\n    p=pages[i]\n    if 'تک' in p or 'تگ' in p:\n        # print first 3 non-empty lines\n        ls=[l for l in p.split('\\n') if l.strip()][:3]\n        print(i, ls)\nEOF",
 "description": "BQT v1 scan for tak/tag"
}
```


### [2026-09-14T03:17:47.619Z] TOOL RESULT

```
721 ['مهوت', 'حطی\u200cورای بی نقطه, نره\u200cای\u200cباشدشبیه تبرخون(۱)؛', 'لسکن بفایت تلغ\u200cاست .']
723 ['< 16 --', 'استکه آتش آن یار پماند , و بشم اول هم', 'بشظر آحده است .']
727 ['کنابه از اشتیاق باشد .', 'تعه ۱ ع ما ثانی عشدد بر وزن بشه ۰', 'پيمانة روغن را گویشد .']
729 ['ات', 'هم\u200cآمدساست٩\u200f - وکرم رفتن و کرم آمدن و کرم', 'کته رونت کته ۱ و بت خیم']
732 ['تکابوی', 'آبکند را گویند \u200f و وسط حثیقی دوکوه را نیز', 'گفته\u200cاند که دره باشد - و زمیئی را نیز گوبد']
733 ['وکاف " بمعنی تکس است که نخم و امتخوان', 'انگور باشد . و بکسر اول هم آهمده است ۰', 'تکسل « بنتح اول و ثانی و سکون\u200cتالث']
734 ['تکیز', 'اوواحت', 'کفده اند - وبکسراول لقمه و بارمای از هرچز']
735 ['یدای \u200c-', 'از ولات کنجه - و پرده ای ازموسيقی\u200cباشد .', 'تگتارا . غتح اول و ای قرشت']
737 ['9 کین', '0 هیرین نله » با نون بر وزن چرنده ۰ کچ', 'است٩\u200f - و ثلق وزر ورق را ليز گویند » و طلق زبالرا گوشد بعنی شخص ی که درست تکلم قوادد']
740 ['اي س', 'مر - و', 'قطه .آب مرواربد رااگوبند وآن علتین است که']
```


## [2026-09-14T03:17:54.174Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==733' BQT_v1_pages.txt | head -70",
 "description": "BQT v1 leaf 732 tak/takapu"
}
```


### [2026-09-14T03:17:55.274Z] TOOL RESULT

```
تکابوی
آبکند را گویند ‏ و وسط حثیقی دوکوه را نیز
گفته‌اند که دره باشد - و زمیئی را نیز گوبد
که‌ازدرموغیردره کمدر آن‌بسنی جاآب فرورود واز
جای دیگر برآبد و بضی جا خدك باشد و در
بسنی‌جا آب ایستاده و بعضی جا روان باشد وبسنی
جاهایآن سبز ومرغزار بود- ونام الکه وولابنی
هم عستث" .
تگالوی ۴ ه با بای فارسی بر وزن
جناجوی ؛ بمعتی آمف شد از روی تعحیل وشتاب
وجتجوی بیارباشد۴ ؛ و بعضی گویندکه‌تکاپوی
تردد بی فایده است .
تکاو ۴ « با واو . بر وزن و معنی
کاب است که زمین‌اب کند و در کوه و زمینی
که درآن بعضی جاها آب ایستاده و بسنی جاها
روان و بعضی جا ها خشات و بعضی جاها سبز
باشد 6
تکاور ۱ بر وزن سراسر » بمعنی
تك اررنده باشه بعنی حیوانات رونده و دونده
" عموما - و بمعتی اسب و شتر باشد که عربان
(۱) چك: ژند ویاژند.
بوی ( پوبدن ).
۴ - تکابوی مردم سود وزیان
۴ - از : وش (- آو (آب) -« تعاب.
وفت سح رکه چکاو » خوش بزند درنکاو
- ) تك ۳ آور ( آوردن‎ 0 9 ٩
وا
فری وجمل کویند خصوصاً .
تکاور ابلق کابه‌ازدناورو ز کار
است باعتبار شب وروز .
تلگ بنا» با بای‌ایجدبروزن‌فرزنده کمری را
کویند که از ابربشم و با یشم شتر و امثال ان
ببافند » و بريك سر‌آن تکمه با عهره و بر سر
دیگر آن انکله نصب سازند " و آن مهره با
تگر و لقن » بارا ونای قرشت بر
وزن پپلوشکن » بلغت زند و پازند( ۱ ) بمعنی
پیچیدن باشد .
کر - بفتح اول و انی و سکون زای
فارسی ؛ استخوان و تخم انگود باشد ؛ و حم
انی و کسر انی هم درست است۸ .
تکس - بر وزن مکس , بمعنی تک
است. که نخم ودانهةٌ انگور باشد وآنرا معر بی‌عجم
آسکساث بنتح اول و ثانی و سکون تالث
۴ از: نك ۳ ا(واسطه) +
بتاو و بدو هر سویی نازبان .
«لغت فری۵۲۵ متن‌وحاشیه».
۵ نیزتام اکن است 9 عگاب):
ساشکی کنج کاو » ساعشکی گنج باد.
+ منوچهری دامغانی ۱۸>.
۷ - مز .۰ ۱۵۲6۵0۵0 , 8۵0
« سنحیدن » است .
۸ - کر نیست کوبی در انگور او
همه شیره دیدیم یکس رژش .
( بر هان‌قاطع ۵؟)
```


## [2026-09-14T03:18:03.533Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==462' incoming/BQT/BQT_v4_pages.txt | tail -30",
 "description": "BQT v4 leaf 461 hendese footnotes"
}
```


### [2026-09-14T03:18:04.548Z] TOOL RESULT

```
هندبا؟ « بکر اول و مکون نانی هندسان؟ باسین بی لقطه بر وزن
وثالت وبای ابجد بالف کشیده . گیاهی است تلخ | هندوان » مخفف هندستان و هندستان مخفف
که آنرا بفارسی‌کاستی میگویند وبیخ آ نراعربان هندوستان .9
اصل‌الهندیا خواند . هندسه* « بکراوزوناك۹ وفتح-ین
هندبید.- بکراول‌وسکون نانی‌ونالث | بی‌نقطه . بمعتی اندازه وشکل باشد - وارقامی
وبای ابجد بتختانی مجهول کشیده وبدال بی‌نقطه | را نیز کوین د که در زیر حروف کلمات توسند
() چش: ۳ هنام... اندام است (1). جای این اغت در صفحةٌ ۲۳۷۵ است .
۹ - هند چگرخوارء زوجم ابو-فیان ومادر مماوبه. که چجگر حمزه عم پیفمبرس را که
درجنگه احد شهید شده بود جوید واورا عرب آكلة الاکباد خوانند . ۴ - ژاباکوید :
پهلوی «هندوپا» ازیونانی 601]0101 (کلمةٌ مسری) است. رل : 116 3۲ .26118007 ,8016
1 ,۷11 .۸10۲8601 5عل ۳۵۵6 «ژابا س۲ 4۵ . لوفر گوبد : هندبا شکل «عرب از
سریانی 8841 وآن ماأخون ازیونانی 81(008] و نام انواع بسیار از18100۳80665» است
ودر عقار مراد 6841۷6 (فر) است س 6501۷012 ۳10807100 و سپس 4۱۷2۳1621080 6۰
ودیگر 520۷286 66 07عزجا» (0۵]1116108[6 12۳352600) «عقار ۱۱4ف» «هندباء هی -
باليوتانية ااطویپا ... بقال له بالبربرية تبقاف و بمجمية الانداس شرالیه واسمه: بالعربية ید ,
وهوالشرقین > «عقار4 ۰*۱۱ ایتالیائی 1801۷18«تفی». کردیع 681000608 ۵ ژابا س۲ 10 .
۴ - ر4: هندیا. ۴ «هندوستان (ه.م.) - معرب « اندازه » «ژاباص
7 بیرون ی گوید : ««ندسه چیست؟ داستن اندازء ها وچندی يك از دیگر وخاسیت صورتها
وشکلها که اندر جسم موجود است ..» « التفهیم ۰۳ 8608261۳10 (ف) « ژابا اضاً» ور :
دزی ج۲ ص۷۹۹ ۹ - در عربی بفتح اول وثالت .
2 هندستان - بکر اول وضم سوم مخف «ندوستان (۸.م.) * هندسان (هم.)
بقیه ازحاشیةٌ صفحهٌ قبل
مسیحی. سیك, جین» بودایی, زرتشتی» بهودی وادبان مختلف دیگر. وسمت خالهند* ۱۳۹۹۹۲۹4
میل مربع بعنی برایر يك دوازدهم سطح زمین وبعبارت دیگر چ برایر قارة اروپا (بدون‌روسبه)
است. آب وهوای آن متنوع است. رودهای عمده عبارتند از: سند وکنگه. جمنا. براهم‌اپوترا.
کاوری, کتناء مگنا. سون کن, مهانادی. تاپتی معادن‌آهن. زغالسنگه. هنگنز, میکا.ی و کسیت.
کرومیت. مس. طلاء کرافیت, کچ. لیمینیت ومونازیت فراواست. دولت هند پصورت باحکومت
فدرال مر کب از۲۸ استان اداره میشود. پایتخت آن دهلی جدبد است هند دارای ۲۱ دانشگاءه
(حريك عامل چند داننکده) و۱۲ داننکهد: مستقل است .
```


## [2026-09-14T03:18:32.536Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in 'https://en.wiktionary.org/wiki/%D8%AA%D8%AE%D8%B4' 'https://abadis.ir/fatofa/%D8%AA%D8%AE%D8%B4/' ; do python3 tools/fetch_source.py \"$u\" --note 'page 498, node 15 taxs bow' ; done",
 "description": "Fetch taxš sources"
}
```


### [2026-09-14T03:18:35.901Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/02bd5861901d158e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/53e2e2f0368d0fca.txt
```


## [2026-09-14T03:18:38.777Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== wikt taxs\"; sed -n '130,200p' 02bd5861901d158e.txt; echo \"=== abadis\"; grep -n 'تخش' 53e2e2f0368d0fca.txt | head -30",
 "description": "Read taxš sources"
}
```


### [2026-09-14T03:18:38.875Z] TOOL RESULT

```
=== wikt taxs
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈtaxʃ/ 

 ( Dari, formal ) IPA ( key ) : [t̪ʰäxʃ] 

 ( Dari, formal ) IPA ( key ) : [t̪ʰäxʃ] 
 ( Kabuli ) IPA ( key ) : [t̪ʰäxʃ] 

 ( Hazaragi ) IPA ( key ) : [t̪ʰäxʃ] 

 ( Iran, formal ) IPA ( key ) : [t̪ʰæxʃ] 

 ( Tajik, formal ) IPA ( key ) : [t̪ʰäχʃ] 

 Rhymes: -axʃ 

 Readings

 Classical reading ? 

 taxš

 Dari reading ? 

 taxš

 Iranian reading ? 

 taxš

 Tajik reading ? 

 taxš

 Etymology 1
 [ edit ] 

 From تخشیدن ( taxšīdan  / taxšidan , “ to sit on the first place ” ) (see Etymology 2), or from Old Persian *taxšah ( “ arrow ” ) , [ 1 ] from Proto-Iranian *taxša ( “ bow ” ) , from Proto-Indo-European *tekʷ- ( “ to run ” ) .

 Noun
 [ edit ] 

 تخش • ( taxš ) ( Tajik spelling тахш ) ( Classical Persian ) 

 ( a kind of ) arrow 

 arrow laced with fire ; firework 
=== abadis
4:TITLE: تخش - معنی در دیکشنری آبادیس
6:تخش - معنی در دیکشنری آبادیس 
10: تخش
16: تخش. [ ت َ ]( اِ ) بالا و صدر مجلس. ( برهان ) ( انجمن آرا ) ( غیاث اللغات ) ( آنندراج ) ( ناظم الاطباء ). || نوعی ازتیر. ( برهان ) ( غیاث اللغات ) ( ناظم الاطباء ). ولف در فهرست شاهنامه از قول نلدکه و پاول هرن این کلمه را بمعنی تیر یاد کرده است. ( از حاشیه برهان چ معین ). || تیر آتشبازی را نیز گفته اند. ( برهان ) ( انجمن آرا ). تیر آتشبازی را گویند، چون تخشیدن بمعنی بالا نشستن است تیر آتشبازی را بهمین سبب تخش نامند که در هوا بسیار بلند میرود. ( غیاث اللغات ). تیر آتشبازی. ( ناظم الاطباء ). بعضی گویند تیر تخش به آن که درجنگ های هند سر دهند و آن آهنی باشد مجوف که از باروت پر کرده آتش در آن زنند جانب خصم به هوا اندازند، گویند. صاحب برهان قاطع نیز بر این است. مع ذلک اشعار استادان اشعاری بدان دارد. ( آنندراج ) : 
17:تو گوئی چو شد تیر تخشش بلند
20:چون تیر تخش ناوک آتش فشان شود. اشرف ( ایضاً ).
21: || بعضی گویند تخش نوعی از کمان است که تیر بسیار کوچکی دارد. ( برهان ). نوعی از کمان که تیر کوچک دارد. ( غیاث اللغات ). نوعی از کمان که تیر از آن به تعبیه اندازند. ( آنندراج ) ( فرهنگ رشیدی ) ( غیاث اللغات ). نوعی از کمان که تیر بسیار کوچکی دارد. ( ناظم الاطباء ). نوعی از کمان است. ( غیاث اللغات ) ( ناظم الاطباء ). کمان تیر ناوک. ( غیاث اللغات ). ولف در فهرست شاهنامه تخش را بمعنی کمان ، قوس نوشته و بدین بیت شاهنامه ارجاع کرده : 
23:جگرخسته تیغ و تخش منند.
25:کمان تخش از هر سوی میدان 
28:به تیری که از تخش ابرو دهد. ظهوری ( ایضاً ).
30:بدانسان که تیر از کمانهای تخش. وحید هاتفی ( ایضاً ).
35:مکن بر دل ما چنین روز تخش. فردوسی.
57: کمان تخش از هر سوی میدان
61: تخش: تخس
```


## [2026-09-14T03:18:55.697Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY latin\"; grep -n -i 'TEKW\\|TEQ\\|TEK ' incoming/ARY/ARY_latin_index_pages.txt | head -20; echo \"=== ARY fa\"; grep -n 'تاختن\\|انداختن\\|گداختن\\|هندسه' incoming/ARY/ARY_pages.txt | head -12",
 "description": "Aryanpur lookups"
}
```


### [2026-09-14T03:18:55.767Z] TOOL RESULT

```
=== ARY latin
6000:STEK (4L4)(DUTCH) sacle (PAHLAVI) (5 hy
12233:(RAMA: 137) set ply coor jl 33 KASH-CHI otek oh  KAS-CHIT pie! clasts
14109:TeQA-Ve4 god sbi oly MIGLA
=== ARY fa
360:۳ ؛سرزمين‌هاي «ایلام» 131.۸16 رسوخ کردند و آن زبان غیر هند و اروپایی را برانداختند. جهت حرکت
1090:پی آن بودند که با به خطر انداختن جان خود (حتی با از دست دادن آن) بتوانند برای همیشه با افتخار
1933:آلیز آلیزیدن» آلیختن(به چم *جفتک انداختن») / ۶۹
5468:۱ تاختن» تاخت, تاز, تازیدن / ۱۸۷
5561:۱ بازگشت به: تک و تاختن.
```


## [2026-09-14T03:18:58.393Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON\"; grep -n 'تاختن' MON_part1.txt MON_part2.txt | head -8; echo \"=== LKT toxic/handasa\"; grep -n -i 'handasa\\|toxon\\|taxsa' LKT.txt | head -10; echo \"=== SYN run\"; grep -n -i 'tek.-.*run\\|OPers. tak' SYN.txt | head -5",
 "description": "Moin, Lokotsch, Buck"
}
```


### [2026-09-14T03:18:58.667Z] TOOL RESULT

```
=== MON
MON_part1.txt:1119:آب‌تاختن: (مسصل.) بیشاب 
MON_part1.txt:36465:تاختن: 2-0 (تاخت» نازد» خواهد 
MON_part1.txt:36474:تاختن. 
MON_part1.txt:36739:تاز؛ 922 (امص.) تاختن» تاخت. (افا.) در 
MON_part1.txt:36744:تاختن» تازانیدن. 
MON_part1.txt:36754:تازش: ۱52-4 (امص.) تاختن» تک‌وبوی 
MON_part1.txt:36832:تاریدن: 22-0 [- تاختن] (تازبد» تازد» 
MON_part1.txt:36834:تازش) (مسصل.) تاختن» دویدن. حمله 
=== LKT toxic/handasa
=== SYN run
```


## [2026-09-14T03:19:01.603Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '36460,36480p' MON_part1.txt; echo \"=== ARY 5468 area\"; sed -n '5460,5480p' incoming/ARY/ARY_pages.txt",
 "description": "Moin tāxtan + Aryanpur tāxtan"
}
```


### [2026-09-14T03:19:01.696Z] TOOL RESULT

```
تاختگاه: ۱-0 (امر.) جایی که در آن 
یه وتا خرن 1 مهد موت خقطی 
که اسب‌های‌دونده در اسب‌دوانی در ۳ 
می‌دوند؛ بیست (فره.) 

تاختن: 2-0 (تاخت» نازد» خواهد 


تاحت» بتاز» تازنده» تاخته» تازش) (مص‌ل.) 
به سرعت رفتن» سخت دویدن. هجوم 
کردن؛ حمله بردن. (مص ع.) تازاندن» به 
تاخت بردن. (مسج.) غارت کردن» تاراج 
کردن: راندن» فراری ساختن» یرون کردن. 
به سرعت فرستادن (نامه و خبر)» آگهی 
تاختن. 

تاخیره: )۱21۲2 (.) سحت؛ طالع» 
سرنوشت. 

تار: ۱2 رشتة دراز سیار باریک از موی و 
ابریشم و پنبه و تنیده عنکبوت. فلر سار 
=== ARY 5468 area
اوستایی (۸(897/۷): 1 لاتین (147100):
پپلری (7ماتل۳۸): 727۸7۸ ,72810۸ 01 ,783170875 ,718240105
تخاری 4 (۸ ۸4ل70727۸7): ۳11 فرانسه (7[ع/(۳8): را ان ۷
تخاری 8 (8 4( 70827۸7): دا ابتالیایی (ف4ا7۸). 713/17۸
ارمنی (۸4814): 718 رومانی (24۸(2): 78/7۲۸
پونانی 082570): ندرا پرتغالی (0070010532): 71821708۸
[pdf page 186]
تج رو هموح سس ۱
۱ تاختن» تاخت, تاز, تازیدن / ۱۸۷
ایسلندی کهن (50۵(701۸1۸۸ 0ا0): پسگشت‌ها انشکتت تیتی ۲
0 1064 شا
انگلیسی (8۸/0/917): 78۸/۲۲ 3 (08۸۴۲ +8۸7
اسلاوی کهن (ع/۲بما5 4ل#ناتل طان): 81 بل 811
71۳1۸ 7 ناه
لیترانی (7274(/4۸/): 71317۸ ,71521۳71 برهان قاطع :(تسافتن) ۴۶۰ و (تساب) ۴۵۲ و
لترنی (لتی) (771۸۸با): 1۳۸5 (تابیدن) ۴۵۴
یادداشت:
۱ واژه‌ی انگلیسی ۸ از فرانسه کهن 7۸73127۸8-> ایتالیایی 1۸۳3127۸-> ترکی 1۸1۳3۸). از
واژه‌ی فارسی "نافته" آیده است.
۲- چم این واژه در تخاری ۸ : ثیرو.
چم این واژه در تخاری 8 : دانستن.
```


## [2026-09-14T03:19:09.665Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>5380 && NR<5470' incoming/ARY/ARY_pages.txt | grep -n 'pdf page\\|تاختن\\|هند و اروپایی\\|اوستایی' | head -20; echo \"--- context\"; sed -n '5400,5460p' incoming/ARY/ARY_pages.txt",
 "description": "Aryanpur tāxtan entry"
}
```


### [2026-09-14T03:19:10.980Z] TOOL RESULT

```
1:[pdf page 183]
6:دکتر محمد معین (به پیروی از نیبرگ) ریشه‌ی اوستایی این واژه را ۸0 ريشه‌يو پهلری آنرا
9:اوستایی (4887۸4): -8۸181 پروسی‌کهن (/(4ا55ن۲۸ ا0): ۳
31:[pdf page 184]
45:اوستایی (4857۸27): یترانی (40742نا4ل7ل): 2۸5
58:[pdf page 185]
61:اوستایی (۸۲887۸1): انگلیسی کهن (87ا8/0 ۰۰:۵2 ۳۸3۳ :تب
80:اوستایی (۸(897/۷): 1 لاتین (147100):
86:[pdf page 186]
88:۱ تاختن» تاخت, تاز, تازیدن / ۱۸۷
--- context

)8۲۸۷۸۲۲, ۸۲70178( 0 ۳25

لیترانی (۸۸/4(۷ ۰:7 ۳۳۸۰ ب8ظ۳
آوستایی (۸۲8974۷): ۰ ۳۸۹0 ,-۳۸۲71817 لاتین (0(ا7ها): ۰ ۲۸5۰ تف۲۳۸
پارسی باستان (288514(۷ ۰:)010 -۴۸71811 فرانسه (۳88۸/6/4): ۰ ,38
پهلری (14۲7لل۸): ۰ -۳۸7)1(83 +۴583 گریکد (0077712): -781
کردی (87(157): -81817 اپسلندی کهن ((5(/210/۸14 ۵ت۵): ۳۷۳۸
بلرچی (1لللانله8): 885917 آلمانی گهن (1(ف4ف052 04 صاه):
سانسکریت (54(/55/7): م2108 ,2۸ 7 ت۴۲78
پرنانی 0728/0): ۳۸1۹08 ,۶۸۸ +۴۸۸ انگلیسی کهن 8۸01/50 صا0):
[pdf page 184]
پیئو» پینوک (به چم / ۱۸۵
(از فرانسه‌ی‌کهن) ود پسگشت‌ها کی
انگلیسی (50لا8(/0): ۳ ان ۳
لیتوانی (7141۸2/40۷/رت): ادا 8 (۳82) :7
پروسی کهن (۳۴55314۸ 0ا0): الدد نا :ا(سا05
ایرلندی کهن (ا5ل#] 0(2: ۸ #ل۸ 1 (08 7 )
گالی ((8لالا0۸): -۸ 4 (87085) ,68 :۸۸215
آلبانی (0۷فاامقلم): 72۸ 3 (88۸8۰) :0۸105

0 (5) :57
برهان قاطع + ۳۴۰
بادداشت:
واژه‌ی انگلیسی 7 عم از همین ریشه است (۳0160۸۲۷:812).
اوستایی (4857۸27): یترانی (40742نا4ل7ل): 2۸5
۳۸۷۸۹۰ +ا۳۸3۸۸۵ تل۸ 2۸
سانسکریت (54۸/5777): پسگشت‌ها بدا درد
۳۷۸۸75 ,8180۷۸33 ,۳۸۸75 زر
ایسلندی کهن (140/ 90/0/0 صا0): 6 (81) +537
۱ 1۸ برهان قاطع : ۳۴۹
انگلیسی کهن (0ل8ل/80/0 2 7۸3/8 فرهنگ معین : ۹۶۹-۰
روژی (اممزه من دا لغت‌نامه دهخدا ۶۳
بادداشت:. ۹
۱- به احتمال زیاد واژه‌ی "پنیر" (پهلوی: ۱۳۸۷1 کردی: ۳338131) نیز از همین ريشه است.
۲- چم این واژه در سانسکریت: ورم کردن؛ یاد کردن,
چم این واژه در زبان‌های ژرمنی: خامه» سرشیر,
چم این واژه در زبان لیتوانی؛ شیر,
[pdf page 185]
اٍ ۶ پیه
| م‌انکلیسی سرواژهی نار رو 1385
اوستایی (۸۲887۸1): انگلیسی کهن (87ا8/0 ۰۰:۵2 ۳۸3۳ :تب
-۳۳۷۸ ,201773۷۷۸ ,نا۴17 انگلیسی (8(/01/877): ۳۸7
پارسی پاستان(2288407 صا۵): ۰۰ ۲1773۲ دانمارکی (0۸(/187): راد
پهلوی (ماقلهه): 1 سرئدی (5۲780/37): لاین ۱
اوستی (05587[76): 7 ,31۷ نروژی (۸/0۳780۵۸)+ 77
کردی (7ل0/5ل0): زر هلندی (007677): ۷7
بلوچی (31ل6لام): ۳6 لینرانی (۵(۷1۸0تا77ل): دا
سانسکریت (854867): ایرلدی کهن (نل5لجا 0ا :)0‏ " 11
۸ ل ۴17 ,۸5 ۷]ظ َ
یونانی (07280): 85 ,۶1۸ پسگشت‌ها اند ای دی دنا ۲
لاین ۰:07 2618 ,0710405 8 ۶00800
ابسلندی کهن (/0/0447/7۸9آل5 صاه): 1 (۳1۸7) تا اما
3 ود 9 (885تم#ه) بت ۱۸ وا
نورس کهن (۸0788 012): ۳7۸ 4 (1۸1) :۸۸52/5
سا کسونی کهن (/542:00 ل0): 77 47 (5۸1) :005
فریزی کهن (514(7ل۲۸ 2ا0): 7 9 (5۸7) +57
آلمانی کهن ((ف02794 07اب صاه): ۲812 برهان قاطم + ۳۵۰
آلمانی (/(0571۸): 7 ,7787
فارسی (//۳85۸54): تابیدن, تافتن, تاب (به چم اگرداندن" و "پیچیدن)
اوستایی (۸(897/۷): 1 لاتین (147100):
```


## [2026-09-14T03:19:16.303Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk '/\\[pdf page 186\\]/,/\\[pdf page 188\\]/' incoming/ARY/ARY_pages.txt | head -60",
 "description": "Aryanpur page 187 taxtan"
}
```


### [2026-09-14T03:19:17.327Z] TOOL RESULT

```
[pdf page 186]
تج رو هموح سس ۱
۱ تاختن» تاخت, تاز, تازیدن / ۱۸۷
ایسلندی کهن (50۵(701۸1۸۸ 0ا0): پسگشت‌ها انشکتت تیتی ۲
0 1064 شا
انگلیسی (8۸/0/917): 78۸/۲۲ 3 (08۸۴۲ +8۸7
اسلاوی کهن (ع/۲بما5 4ل#ناتل طان): 81 بل 811
71۳1۸ 7 ناه
لیترانی (7274(/4۸/): 71317۸ ,71521۳71 برهان قاطع :(تسافتن) ۴۶۰ و (تساب) ۴۵۲ و
لترنی (لتی) (771۸۸با): 1۳۸5 (تابیدن) ۴۵۴
یادداشت:
۱ واژه‌ی انگلیسی ۸ از فرانسه کهن 7۸73127۸8-> ایتالیایی 1۸۳3127۸-> ترکی 1۸1۳3۸). از
واژه‌ی فارسی "نافته" آیده است.
۲- چم این واژه در تخاری ۸ : ثیرو.
چم این واژه در تخاری 8 : دانستن.
چم اين واژه در لاتین و زبان‌های رومانس: گیجگاه» شقیقه.
چم اين واژه در زبان ایسلندی کهن؛ ورم کرده» تاب خورده,
اوستایی (4787۸27): یرنانی (07580): 7007
۸ ب7۸۵6 ,1۸2۳73۸171 لاتین (/710مل): 78
پهلو: ی (ماتلوه: ۰ اسلاوی کهن (۲/2شا5 207 صت0):
۲ 1 انیا
8 ی اس لینوانی (040۷هتا#م: ید
بلوچی (ابته‌سمه. کی لدرنی (لتی) (91ف471): 714
6 ,6فت7۸8 ,71۸6۸6 پروسی کهن (۳۸551404 0.ا۵): 71۸05135
افغانی (پشتر) (/4707۸7): ایرلندی کهن (۴757] 00):
78۸33 ,7۸8117 0 780319
تخاری 8 (8 له الان70): اد ۱ گالی (3لکلان0۸): لا ین ۱ اد با
سانسکریت (84(/57077): برتونی (/87670): تا ند ۱ : برد با با
۸ ,آتف7۸ ,7۸367 آلبانی (142لمقلم): و لزان |
[pdf page 187]
پسگشت‌ها اند گرد دنس 1 (8۲۸) ند تک ها
0 2 ۶۵808800 برهان قاطع : ۳۵۵
۱
28 م05 رو
و
یادداشت:
۱ چم این واژه در زبان‌های یونانی و لاتین: درخت سرخدار, :
چم اين واژه در زبان‌های ایرلندی کهن و برتونی وگالی: فرارکردن» قرار.. .
چم این واژه در زبان تخاری 8 رودخانه.
۲ پازگشت به: تکه» تخش.
اوستایی (۸۲887۸۷): ه171 آنرنی (لتی) (7714(4)م): 7۵
کردی (1/80157): 87 ,1۳ ,۳۸
افغانی (پشتر) (40۸(1). 712 ,108 پسگشت‌ها نشب دی
سانسکریت (84(/8/0/7): 7۸3۸ 3۸2۷۳۸ ان 0
۸2۰ بلل۸ 1۸۷۳ تا ۲۸۵7 1۸3۸ 9 (183) :33847
بونانی 068/0): 105 :3 (۸78) مس
لاتین (7120مل): 785 9 رصفتجین
لیترانی ((14ههلا 2 7): 711۳۲۸۵ برهان قاطم + ۳۶۵
یادداشت:
۱ به احتمال زیاد واژه‌ی "تور" نیز از همین واجریشه است.
۲ معنی این واژه در زبان‌های برنانی و لاتین: کشیده» کشیدگی.
۳ به عقیده‌ی 81۳8۸7 واژه‌ی انگلیسی 11118 (ر واژه‌های همریشه‌ی آن در زبان‌های ژرستی) هم از همین
واجریشه‌اند.
۴ بازگشت به: تنیدن و تار, ۰
[pdf page 188]
```


## [2026-09-14T03:19:49.393Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg498.png data/verification/sources/refs/ocr/BOOK/498.png && ls -la data/verification/sources/refs/ocr/BOOK/498.png",
 "description": "Save page PNG for audit"
}
```


### [2026-09-14T03:19:49.490Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 86756 Sep 13 23:19 data/verification/sources/refs/ocr/BOOK/498.png
```


## [2026-09-14T03:28:27.141Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-498.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nU = {\n \"taxtan\":  W+\"%D8%AA%D8%A7%D8%AE%D8%AA%D9%86\",\n \"andaxtan\":W+\"%D8%A7%D9%86%D8%AF%D8%A7%D8%AE%D8%AA%D9%86\",\n \"handasa\": W+\"%D9%87%D9%86%D8%AF%D8%B3%D8%A9\",\n \"godaxtan\":W+\"%DA%AF%D8%AF%D8%A7%D8%AE%D8%AA%D9%86\",\n \"pardaxtan\":W+\"%D9%BE%D8%B1%D8%AF%D8%A7%D8%AE%D8%AA%D9%86\",\n \"toxic\":   \"https://www.etymonline.com/word/toxic\",\n \"pie\":     W+\"Reconstruction:Proto-Indo-European/tek%CA%B7-\",\n \"toxon\":   W+\"%CF%84%CF%8C%CE%BE%CE%BF%CE%BD\",\n \"taxs\":    W+\"%D8%AA%D8%AE%D8%B4\",\n \"dehkhoda_taxs\": \"https://abadis.ir/fatofa/%D8%AA%D8%AE%D8%B4/\",\n}\n\nPOK_Q = (\"Pokorny IEW pp.1059-1060 s.v. tekʷ- 'to run; to flow' (local POK_full.txt, \"\n  \"'Root / lemma: tek\\\"-', Page(s): 1059-1060): \\\"Avestan tacaiti 'running, hurries; flows', \"\n  \"participle -taxta-, np. taxtan 'run', hantacina-; Avestan vi-taxti- f. 'das Zerfließen, Schmelzen'; \"\n  \"iran. (skyth.) *tahsa- (npers. taxs) 'arrow, bow', from which gr. toxon ds., Latin taxus 'yew'; \"\n  \"Avestan taka- m., np. tak 'run, flow'; Avestan tacar- n. 'run, flow, pathway', tacan- 'hurrying', \"\n  \"iran. *tahra- 'quick, fast'.\\\"\")\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(id=1, lang=\"Avestan\", words=\"tak, taka, tač; tačaiti\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Avestan has the primary verb tac- / tak- 'to run, to flow' (3sg. pres. tačaiti, Y 16.8 tačat, \"\n    \"Yt 8.5 tačanti) and the noun taka- m. 'course, running, flow'; these continue Proto-Iranian *tač- \"\n    \"< Proto-Indo-Iranian *tać- < PIE *tekʷ- exactly as drawn, the palatalisation of *kʷ before the \"\n    \"thematic *-e- giving Av. -c- [č] while the zero/other grades keep k (taka-, -taxta-). Sanskrit tákti \"\n    \"'rushes', Lithuanian tekù 'I run, flow', OCS tekǫ are the direct cognates. Nourai's three citation \"\n    \"forms tak / taka / tač are simply the root, the o-grade noun and the present stem; the gloss 'to run' \"\n    \"is Pokorny's and Bartholomae's.\"),\n  derivation_fa=(\n    \"در اوستایی فعل tac-/tak- «دویدن، روان شدن» با صیغهٔ سوم‌شخص tačaiti و اسم taka- «دو، جریان» به‌کار رفته است. \"\n    \"این‌ها بازماندهٔ ایرانی باستان *tač- و در نهایت هندواروپایی آغازین *tekʷ- اند؛ *kʷ پیش از واکهٔ e به č (ج/چ اوستایی) \"\n    \"بدل شده و در دیگر پایه‌ها به‌صورت k مانده است (taka-، -taxta-). هم‌ریشه‌های آن سنسکریت tákti و لیتوانیایی tekù است. \"\n    \"ادعای نورایی در این گره کاملاً درست است (پوکورنی ۱۰۵۹، بارتولومه، چونگ).\"),\n  sources=[U[\"pie\"], U[\"taxtan\"]],\n  ref_check=[\n    {\"ref\":\"POK:1059\",\"status\":\"supports\",\"note\":POK_Q},\n    {\"ref\":\"BQT:503\",\"status\":\"partial\",\"note\":(\n      \"Borhan-e Qate' (BQT_v1_pages.txt, form-feed leaf 732 = printed p. ~503/504, running head \"\n      \"تکابوی) carries the entries تکاپوی، تکاو، تکاور with Mo'in's footnote '۶ - از: تک + آور (آوردن)'. \"\n      \"The page documents the Persian tak-family Nourai puts in the daughter box, but it gives no Avestan tak-/tač- form, \"\n      \"so it supports the Persian side of the arrow only.\")}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"AiW col. ~626 s.v. tac- ; col. 1869 s.v. tacan-\",\"stance\":\"supports\",\n     \"note\":\"Bartholomae's Altiranisches Wörterbuch (local BRT.txt) lists Av. tac- with the senses 'laufen' and, \"\n            \"'insbesondere von Flüssigkeiten: fliessen, strömen' (e.g. 'kaθa xā .. apǎim tacinti nava', Yt 8.5), \"\n            \"plus the Kaus. 'fliessen lassen' — exactly the root and glosses Nourai gives.\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV p. 373 s.v. *tač¹\",\"stance\":\"supports\",\n     \"note\":\"Cheung 2007: \\\"*tač¹ 'to flow, run, walk' — AVESTAN: YAv. tac- 'to flow; walk'\\\", with the full \"\n            \"paradigm (IND. 3sg. fratacaiti, INJ. 3sg. tacat, SUBJ. tacanti …).\"},\n    {\"src\":\"IEC\",\"where\":\"Mann col. 1372 s.v. tek- (2)\",\"stance\":\"supports\",\n     \"note\":\"\\\"tek- (2) (teko, tekmi) 'run, flow'. WP I, 715 Skt. tákmi 'rush, hurtle'; Av. tak-, tac-, v. 'run, flow'…\\\"\"}])\n\nN(id=2, lang=\"Persian\", words=\"tâxtan; tâzîdan; takîdan; ham-tak\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"تاختن tāxtan 'to gallop, ride fast, charge' continues MP tāxtan / tāz- (MacKenzie: \\\"tāxtan, tāz- \"\n    \"[ʾhtʹ, ʾc-] cause to run, flow; chase; pour\\\"), the causative-lengthened counterpart of MP taxtan, taz- \"\n    \"'run, flow' < Av. tac-; the past stem in -xt is the regular Iranian *-č-ta- > -xt (*tāč-ta- > tāxt). \"\n    \"تازیدن tāzīdan is the New Persian secondary infinitive built on the present stem tāz-, whence also \"\n    \"تازان tāzān and تازیانه tāz(i)yāna 'whip' (MP tāzānag). تکیدن takīdan and the nouns تک tak 'a run', \"\n    \"تکاپو takāpu, تکاور takāvar 'swift-runner' go back to the unlengthened stem (MP tazīdan, Av. taka-). \"\n    \"هم‌تک / هم‌تگ ham-tak/ham-tag 'fellow-traveller' is ham- 'together' + tak/tag, and is registered as such by Mann.\"),\n  derivation_fa=(\n    \"«تاختن» از فارسی میانهٔ tāxtan/tāz- (سببیِ taxtan/taz- «دویدن، روان شدن») است که خود از اوستایی tac- می‌آید؛ \"\n    \"ستاک گذشته با تحول آواییِ ایرانیِ *-čt- > -xt ساخته شده است (*tāč-ta- > tāxt). «تازیدن» مصدر ثانوی نوساخته بر ستاک حالِ tāz- است \"\n    \"و «تازان» و «تازیانه» (پهلوی tāzānag) نیز از همین ستاک‌اند. «تکیدن»، «تک»، «تکاپو» و «تکاور» از ستاک کوتاه (پهلوی tazīdan، اوستایی taka-) گرفته شده‌اند. \"\n    \"«هم‌تک/هم‌تگ» یعنی «هم‌راه، هم‌دو» از ham- «با هم» + tak است. ادعای نورایی درست است (مکنزی، مان ستون ۱۳۷۲، ویکی‌واژه).\"),\n  sources=[U[\"taxtan\"]],\n  ref_check=[\n    {\"ref\":\"IEC:1372\",\"status\":\"supports\",\"note\":(\n      \"Mann, IECD col. 1372 (local IEC.txt, form-feed leaf 755, whose running head numeral is 1373) s.v. tek- (2) \"\n      \"'run, flow': \\\"Per. tàxtan, inf. 'gallop; attack' … Long-gde in Per. tāxtan beside tāzīdan 'gallop; attack' … \"\n      \"Cf. tokos … Per. ham-tag 'fellow-traveller'\\\" — it has tāxtan, tāzīdan and ham-tag, i.e. three of Nourai's four words.\"},\n    {\"ref\":\"BQT\",\"status\":\"supports\",\"note\":(\n      \"Cited without a page. The relevant Borhan page is p. ~503 (BQT_v1_pages.txt leaf 732), which has \"\n      \"تکاپوی، تکاو، تکاور with Mo'in's note 'از: تک + آور (آوردن)'.\"},\n    {\"ref\":\"MON:5176\",\"status\":\"not_checked\",\"note\":(\n      \"Mo'in's Farhang-e Farsi is online (vajehyab/abadis) only by headword, not by page, and the print volume for \"\n      \"p.5176 is not on disk, so the page could not be opened. The entry itself was checked in the OCR of the lexicon \"\n      \"volumes: MON_part1.txt line 36465 'تاختن: (تاخت، تازد، خواهد تاخت، بتاز، تازنده …) (مص‌ل.) به سرعت رفتن، سخت دویدن، هجوم کردن'.\")}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie 1971, p. 82 s.v. taxtan / tāxtan\",\"stance\":\"supports\",\n     \"note\":\"\\\"taxtan, taz- [thtnʹ, tc-] run, flow\\\" and \\\"tāxtan, tāz- [ʾhtʹnʹ, ʾc-] cause to run, flow; chase; pour\\\", \"\n            \"plus \\\"tāzānag [N tāz(y)āna] (whip)\\\" and \\\"tazīdan, taz- = taxtan\\\" — the whole Persian set of the node.\"},\n    {\"src\":\"ARY\",\"where\":\"Aryanpur, p. 187 s.v. تاختن، تاخت، تاز، تازیدن (ARY_pages.txt, pdf page 186-187)\",\n     \"stance\":\"supports\",\n     \"note\":\"Aryanpur's IE-root dictionary heads the entry تاختن، تاخت، تاز، تازیدن and lists Av. TAK-/TAČAITI, Pahlavi, \"\n            \"Sanskrit TAKTI, Greek, Latin TAXUS, OCS, Lith., with the cross-reference 'بازگشت به: تک، تخش' — the same \"\n            \"family, and the same link to taxs/toxon, that Nourai draws.\"},\n    {\"src\":\"HRN\",\"where\":\"Horn, Grundriss no. 297 (p.66) and the tāxtan family\",\"stance\":\"supports\",\n     \"note\":\"Horn treats tāxtan/tāzīdan as the regular NP continuants of the Avestan root tac- (cited for pardāxtan as 'aw. *para + √tac-').\"}])\n\nN(id=3, lang=\"Avestan\", words=\"pairi-tak\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"The compound is genuinely attested: Young Avestan pairi.tacaṭ 'ran around' (Yt 17.26), i.e. pairi 'around' \"\n    \"(PIE *peri) + tac- 'to run'. Cheung lists it under *tač¹: \\\"(+ *pari-) 'to run around, encircle'\\\". \"\n    \"Nourai's citation form 'pairi-tak' is the root-form spelling of the same compound; the gloss 'to run around' \"\n    \"is exactly right.\"),\n  derivation_fa=(\n    \"این ترکیب در اوستای نو به‌راستی گواهی شده است: pairi.tacaṭ «گرداگرد دوید» (یشت ۱۷ بند ۲۶)، یعنی pairi «پیرامون» (از *peri هندواروپایی) + tac- «دویدن». \"\n    \"چونگ نیز آن را ذیل *tač¹ با معنای «گرد چیزی دویدن، احاطه کردن» آورده است. صورت «pairi-tak» نزد نورایی همان ترکیب با پایهٔ tak- است و معنایی که داده درست است.\"),\n  sources=[U[\"pardaxtan\"]],\n  ref_check=[\n    {\"ref\":\"HRN:66\",\"status\":\"partial\",\"note\":(\n      \"Horn, Grundriss der neupersischen Etymologie p.66 no. 297 (local HRN.txt, form-feed leaf 87): \"\n      \"\\\"297. perdā́yten 'ausführen, ausleeren; streben, sich bemühen'; Praes. perdāzem. phlv. pardāčtan (AV.). \"\n      \"aw. *para + √tac-; Bedeutungswechsel wie bei endāčten (No. 117).\\\" Horn supports the root tac- but reconstructs \"\n      \"the prefix as *para-, not pairi-; Cheung and Wiktionary give *pari-, Nourai's form.\"},\n    {\"ref\":\"BQT:380\",\"status\":\"supports\",\"note\":(\n      \"Borhan-e Qate' p. ~380-382 (BQT_v1_pages.txt leaf 604, running head پردا) carries the entries پرداخت، پرداختن، \"\n      \"پرداز ('پرداختن … فارغ گشتن از علایق … و بمعنی آراستن …') with Mo'in's 'پهلوی' footnote — the right page for the daughter word.\"}],\n  consulted=[\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV p. 373 s.v. *tač¹\",\"stance\":\"supports\",\n     \"note\":\"\\\"YAv. tac- … || (+ *pari-) 'to run around, encircle'… INJ. 3sg. … YAv. pairi.tacaṭ (Yt 17.26)\\\" — the compound \"\n            \"Nourai cites is an attested Avestan form.\"},\n    {\"src\":\"BRT\",\"where\":\"AiW s.v. tac-, compounds\",\"stance\":\"supports\",\n     \"note\":\"Bartholomae records the same verb with preverbs (ā-tacaiti, fra-tacaiti, apa-tacaţ, pairi-), e.g. 'yaṣ (nāml. arədvī) .. fratacaiti hukairyāt haca' (Y 65.3).\"}])\n\nN(id=4, lang=\"Persian\", words=\"pardâxtan\",\n  verdict=\"plausible\",\n  derivation=(\n    \"پرداختن pardāxtan 'to empty, finish, settle, pay; to attend to' comes from MP pardāxtan, pardāz- \"\n    \"(MacKenzie: \\\"pardāxtan, pardāz- [pldʾhṭnʹ] accomplish\\\"; beside pardaxtan 'be done with, freed of'), i.e. \"\n    \"prefix par- < OIr. *pari-/*para- + the stem tač-, past stem *-tāč-ta- > -tāxt; the present stem پرداز pardāz \"\n    \"is the regular reflex of *-tāč-. Semantically 'to run (something) through/away' > 'to clear, empty' > 'to finish, \"\n    \"discharge a debt, pay' > 'to devote oneself to'. The reservation is the root: Cheung 2007 puts MP pardāxtan under \"\n    \"a SECOND, homophonous root *tač² 'to reach for, attain, receive' (PIE *tek-, LIV 618f., Pok. 1057f.), remarking \"\n    \"that \\\"the meaning of NP pardaxtan/pardaz- 'to pay, settle' may derive caus. 'to cause to attain, receive'\\\", \"\n    \"whereas Wiktionary (and Horn) keep it with *tač- < *tekʷ-. The formal derivation is uncontested; only the root is.\"),\n  derivation_fa=(\n    \"«پرداختن» از فارسی میانهٔ pardāxtan/pardāz- «به انجام رساندن، تهی کردن» است: پیشوند par- از ایرانی باستان *pari-/*para- به‌علاوهٔ ستاک tač-؛ \"\n    \"ستاک گذشته با همان تحول *-čt- > -xt ساخته شده و ستاک حال «پرداز» بازتاب *-tāč- است. تحول معنایی: «(چیزی را) دواندن، رها کردن» > «تهی کردن» > «به پایان بردن، ادای دِین کردن» > «به کاری پرداختن». \"\n    \"اما در ریشه اختلاف هست: چونگ (۲۰۰۷) این فعل را ذیل ریشهٔ هم‌آوای دیگری، *tač² «دست یازیدن، رسیدن، دریافتن» (هندواروپایی *tek-) می‌آورد، حال آنکه هرن و ویکی‌واژه آن را از همان *tekʷ- «دویدن» می‌دانند. \"\n    \"پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n  sources=[U[\"pardaxtan\"]],\n  ref_check=[{\"ref\":\"(none cited in the box)\",\"status\":\"not_checked\",\"note\":\n     \"The Persian box carries no refs of its own; its parent box cites BQT:380 and HRN:66, both checked on node #3 \"\n     \"(Horn no. 297 is in fact the entry for perdāyten = pardāxtan itself, and supports the formal derivation).\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie 1971, pp. 64-65 s.v. pardaxtan / pardāxtan\",\"stance\":\"supports\",\n     \"note\":\"\\\"pardaxtan, pardaz- [pldhtnʹ, pldc- | M prdxt, N ~], ~ az: be done with, freed of. ~ ō: set about, undertake. \"\n            \"… pardāxtan, pardāz- [pldʾhtnʹ, pldʾc- | N ~] accomplish.\\\"\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV p. 374 s.v. *tač² 'to reach for, attain, receive'\",\"stance\":\"partial\",\n     \"note\":\"\\\"(+ *para-) MMP prdx- 'to be done with, freed of' … BMP pldʾc- /pardaz-/ (caus.) 'to accomplish' … NP \"\n            \"pardaxtan/pardaz- 'pay, settle, finish, accomplish'\\\", with the comment \\\"The meanings of the forms above are \"\n            \"often difficult to reconcile with that of *tač¹ 'to run, flow' … The IE root *tek- 'to stretch the hand, \"\n            \"receive, reach' is perhaps the best candidate.\\\"\"},\n    {\"src\":\"HRN\",\"where\":\"Horn no. 297, p.66\",\"stance\":\"supports\",\n     \"note\":\"\\\"perdāyten 'ausführen, ausleeren' … phlv. pardāčtan (AV.). aw. *para + √tac-; … Die np. Bedeutung \"\n            \"'ausleeren' lässt sich aus 'weglaufen lassen' erklären.\\\"\"}])\n\nN(id=5, lang=\"Avestan\", words=\"ham-tač, ham-tak\",\n  verdict=\"plausible\",\n  derivation=(\n    \"No Avestan compound hǎm.tac- 'to throw' is actually attested; what Avestan has is hǎm.tacina- 'flowing together' \"\n    \"(Pokorny p.1059 'hantacina- = Lith. tekinas'), and the compound with *ham- turns up first in Middle Persian \"\n    \"(handāxtan/handāz-). Nourai's box is therefore a reconstruction projected back into Avestan, and its gloss 'to throw' \"\n    \"is the Middle/New Persian sense, not an Avestan one. On the root itself Horn and Pokorny are with Nourai \"\n    \"(*ham- + √tac- of *tekʷ- 'run'), but Cheung 2007 assigns the whole *ham-/*para- group to a homophonous *tač² \"\n    \"'to reach for, attain' < PIE *tek- (Pok. 1057f.), citing the Pahlavi passage \\\"u-m … ul ō ān hōm nē handāzēd\\\" \"\n    \"'I do not reach up to that haoma'; Wiktionary's انداختن entry follows Cheung. Compatible but not identical picture.\"),\n  derivation_fa=(\n    \"در اوستا ترکیبِ hǎm.tac- به معنای «افکندن» گواهی نشده است؛ آنچه هست hǎm.tacina- «به‌هم‌روان، هم‌جاری» است (پوکورنی ص ۱۰۵۹) و ترکیب با *ham- نخست در فارسی میانه (handāxtan/handāz-) دیده می‌شود. \"\n    \"پس این جعبه بازسازی‌ای است که نورایی به اوستایی نسبت داده و معنای «افکندن» نیز معنای فارسی میانه/نو است نه اوستایی. \"\n    \"دربارهٔ ریشه، هرن و پوکورنی با نورایی هم‌داستان‌اند (*ham- + √tac- از *tekʷ- «دویدن»)، ولی چونگ (۲۰۰۷) این گروه را به ریشهٔ هم‌آوای دیگری، *tač² «دست یازیدن، رسیدن» از *tek- هندواروپایی، می‌برد. \"\n    \"بنابراین با احتیاط پذیرفتنی است.\"),\n  sources=[U[\"andaxtan\"]],\n  ref_check=[\n    {\"ref\":\"HRN:27\",\"status\":\"supports\",\"note\":(\n      \"Horn p.27 no. 117 (local HRN.txt, form-feed leaf 49): \\\"117. endāčten 'werfen', Praes. endāz-em, endāz 'Plan, \"\n      \"Absicht', endāze 'Mass'. phlv. andāčtan 'werfen; sinnen' (Bund.), andāčak 'Mass', … arab. LW. muhandis \"\n      \"'Feldmesser', hindasat 'Geometrie' … aw. hǎm + √tac-; Bedeutungswechsel wie auch bei np. perdāčten (No. 297).\\\" \"\n      \"This is Nourai's arrow verbatim — Avestan hǎm + tac-, the Pahlavi noun, and the Arabic loans.\"},\n    {\"ref\":\"BQT:128\",\"status\":\"not_found\",\"note\":(\n      \"Borhan-e Qate' p.128 is, in the Mo'in edition used here (BQT_v1_pages.txt, leaf ~345-348, offset leaf−~218), \"\n      \"in the اسـ section (اسطرلاب، اسفاناخ، اسقف، اسقلطسی) and has nothing on انداختن/اندازه. The Borhan entry actually \"\n      \"wanted is اندازه at p. ~167 (leaf 387): 'اندازه … قیاس کردن و اندازه گرفتن را نیز گفته‌اند، و تعریبش به هندسه کرده‌اند'. \"\n      \"Either Nourai's page number is a slip or his printing differs; the claim itself is supported by that other page.\")}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"IEW p.1059 s.v. tekʷ-\",\"stance\":\"partial\",\n     \"note\":\"Pokorny lists under tekʷ- \\\"np. taxtan 'run', hantacina- 'zusammenfließend' (= Lithuanian tekinas 'running')\\\" — \"\n            \"the ham- compound is there, but with the sense 'flowing together', not 'to throw'.\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV pp. 374-375 s.v. *tač²\",\"stance\":\"contradicts\",\n     \"note\":\"\\\"(+ *ham-) MMP hndʾc-, BMP hndʾc- /handāz-/ 'to plan, allot, reckon, measure' … «PIE *tek- 'to stretch the hand, \"\n            \"receive, reach' = LIV: 618 f. | Pok.: 1057 f.\\\" — Cheung explicitly separates this from *tač¹ 'run, flow'.\"},\n    {\"src\":\"BRT\",\"where\":\"AiW s.v. hǎm.tacina-\",\"stance\":\"partial\",\n     \"note\":\"Bartholomae has the Avestan derivatives of tac- with hǎm only in the 'flow together' sense; no hǎm.tac- 'throw'.\"}])\n\nN(id=6, lang=\"Persian\", words=\"andâxtan; andâzeh\",\n  verdict=\"plausible\",\n  derivation=(\n    \"انداختن andāxtan 'to throw; to reckon, measure, think' is MP handāxtan, handāz- 'plan, allot, reckon, judge' \"\n    \"(MacKenzie), with the regular New Persian loss of initial h- (handāxtan > andāxtan, as hangam > hangām keeps it but \"\n    \"hanbān > anbān loses it) and the past stem in -xt < *-čt-. اندازه andāza 'size, measure' is MP handāzag \"\n    \"(MacKenzie: \\\"handāz-ag [hndʾckʹ | N andāza] measure, manner\\\"), the -ag/-ak noun of the same stem, i.e. Nourai's \"\n    \"Pahlavi handāčak. Horn (no. 117) gives exactly this set: endāčten 'werfen', endāz 'Plan, Absicht', endāze 'Mass'. \"\n    \"Verdict 'plausible' only because of the root question raised at #5 (Cheung's *tač² < PIE *tek-).\"),\n  derivation_fa=(\n    \"«انداختن» بازماندهٔ فارسی میانهٔ handāxtan/handāz- «برآورد کردن، سنجیدن، افکندن» است؛ هـ آغازین در فارسی نو افتاده (مانند hanbān > انبان) و ستاک گذشته با تحول *-čt- > -xt ساخته شده است. \"\n    \"«اندازه» نیز از handāzag پهلوی (همان handāčak نورایی) با پسوند -ag است. هرن (شمارهٔ ۱۱۷) همین مجموعه را می‌آورد: endāčten «افکندن»، endāz «قصد، نقشه»، endāze «اندازه». \"\n    \"حکم «با احتیاط پذیرفتنی» تنها به سبب اختلاف بر سر ریشهٔ هندواروپایی است که در گرهٔ بالاتر توضیح داده شد.\"),\n  sources=[U[\"andaxtan\"]],\n  ref_check=[{\"ref\":\"(none cited in the box)\",\"status\":\"not_checked\",\"note\":\n     \"No refs in this box; the parent box's HRN:27 (checked, supports) is the reference covering andāxtan/andāza.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie 1971, p. 42 s.v. handāxtan\",\"stance\":\"supports\",\n     \"note\":\"\\\"handāxtan, handāz- [hndʾhtnʹ, hndʾc- | M hndʾc-, N an~] plan, allot, reckon, judge. ~išn: judgement. … \"\n            \"handāz-ag [hndʾckʹ | N andāza] measure, manner\\\".\"},\n    {\"src\":\"HRN\",\"where\":\"Horn p.27 no.117\",\"stance\":\"supports\",\n     \"note\":\"\\\"endāčten 'werfen', Praes. endāz-em, endāz 'Plan, Absicht', endāze 'Mass'. phlv. andāčtan 'werfen; sinnen'…\\\"\"},\n    {\"src\":\"BQT\",\"where\":\"Borhan-e Qate' p. ~167 (BQT_v1_pages.txt leaf 387) s.v. اندازه\",\"stance\":\"supports\",\n     \"note\":\"\\\"اندازه ، بروزن خمیازه ، بمعنی انتهای هر چیز را گویند ‐ و قیاس کردن و اندازه گرفتن را نیز گفته‌اند، و تعریبش به هندسه کرده‌اند\\\" — \"\n            \"the same page also states the Arabicisation that node #9 depends on. The entry before it glosses انداز as 'مصدر … که انداختن باشد'.\"}])\n\nN(id=7, lang=\"Pahlavi\", words=\"handâčak\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Book Pahlavi hndʾckʹ, read handāzag by MacKenzie and handāčak in the older transcription (the letter is Aramaic \"\n    \"ṣade, transcribed č by Horn and Nyberg, z by MacKenzie), 'measure, manner': the -ak/-ag noun of handāxtan / \"\n    \"handāz-. Horn p.27 writes exactly 'andāčak \\\"Mass\\\"' beside andāčītan 'erwägen, ermessen' and andāč(i)šn \"\n    \"'Meinung'. Nourai's form is thus the book-Pahlavi spelling of what is New Persian اندازه and the source of \"\n    \"Arabic handasa; the gloss 'throw, measure' fuses the verbal and the nominal sense.\"),\n  derivation_fa=(\n    \"صورت پهلوی کتابی hndʾckʹ است که مکنزی آن را handāzag و هرن و نیبرگ به شیوهٔ قدیم‌تر handāčak می‌خوانند (حرف صاد آرامی که گاه č و گاه z آوانویسی می‌شود)، به معنای «اندازه، سنجه»؛ \"\n    \"اسمِ ساخته‌شده با پسوند -ak/-ag از ستاک handāz-. هرن در ص ۲۷ دقیقاً می‌نویسد: andāčak «Mass» در کنار andāčītan «سنجیدن» و andāč(i)šn «نظر». \"\n    \"همین واژه است که از سویی «اندازه»ی فارسی نو و از سوی دیگر «هندسه»ی عربی از آن برآمده است. ادعای نورایی درست است.\"),\n  sources=[U[\"handasa\"]],\n  ref_check=[{\"ref\":\"(none cited in the box)\",\"status\":\"not_checked\",\"note\":\n     \"No refs in this box; HRN:27 on the parent box gives the Pahlavi form andāčak 'Mass' explicitly (checked, supports).\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie 1971, p. 42\",\"stance\":\"supports\",\n     \"note\":\"\\\"handāz-ag [hndʾckʹ | N andāza] measure, manner; ~ ī: like\\\" — same word, MacKenzie's reading handāzag.\"},\n    {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II p. 94b (s.v. handāz-)\",\"stance\":\"supports\",\n     \"note\":\"Nyberg's glossary entry for handāz- is the one Cheung quotes (EDIV 375: \\\"it is worth citing the example, given by \"\n            \"Nyberg II, l.c. … u-m … ul ō ān hōm nē handāzēd\\\"), i.e. Nyberg has the stem and its noun.\"},\n    {\"src\":\"HRN\",\"where\":\"Horn p.27 no.117\",\"stance\":\"supports\",\n     \"note\":\"\\\"phlv. andāčtan 'werfen; sinnen' (Bund.), andāčak 'Mass', andāčītan 'erwägen, ermessen', andāč(i)šn 'Meinung'\\\".\"}])\n\nN(id=8, lang=\"Arabic\", words=\"(box printed with a language label but no word)\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"A pass-through box: the printed page (data/verification/sources/refs/ocr/BOOK/498.png) shows an 'Arabic' header \"\n    \"with an empty body. The forms it stands for are هندسة handasa 'geometry' and its denominative هندس handasa / \"\n    \"مهندس muhandis 'geometer, engineer' — Arabic borrowed the Middle Persian noun handāzag/handāčak, and Arabic \"\n    \"phonology, which has no /g/ and disfavours the sequence, rendered the final -z(-ag) as -s, giving a pseudo-triliteral \"\n    \"stem h-n-d-s on which the quadriliteral verb and the participle muhandis were built. Asbaghi notes the intermediate \"\n    \"Aramaic step (Talmudic hndzʾ, Syriac handazā).\"),\n  derivation_fa=(\n    \"این جعبه تنها «گذرگاه» است: در صفحهٔ چاپی سرِ جعبه «Arabic» آمده ولی بدنهٔ آن تهی است. واژه‌هایی که در نظر بوده «هندسة» و فعل و اسم فاعل برساختهٔ آن یعنی «هندس/مهندس» است. \"\n    \"عربی نامِ فارسی میانهٔ handāzag/handāčak را وام گرفت و چون در عربی z پایانیِ این ساخت جا نمی‌افتاد، به س بدل شد و از آن ریشهٔ چهارحرفیِ ساختگی «هـ ن د س» پدید آمد که فعل «هندسَ» و «مهندِس» بر آن ساخته شد. \"\n    \"اصبغی واسطهٔ آرامی/سریانی (handazā) را نیز یاد می‌کند. ادعای نورایی درست است.\"),\n  sources=[U[\"handasa\"]],\n  ref_check=[{\"ref\":\"(none cited in the box)\",\"status\":\"not_checked\",\"note\":\n     \"Empty box, no refs; the Arabic step is covered by HRN:27 on node #5 ('arab. LW. muhandis \\\"Feldmesser\\\", hindasat \\\"Geometrie\\\"').\"}],\n  consulted=[\n    {\"src\":\"PLA\",\"where\":\"Asbaghi, Persische Lehnwörter im Arabischen, p.270 s.v. handaza / hindisa\",\"stance\":\"supports\",\n     \"note\":\"\\\"هندسة - hindisa: 'Geometrie, Architektur, Ingenieurskunst' … اندازه andāze MP. handāčak/handādak v. handāxtan; \"\n            \"talm. Lw. hndzʾ, syr. handazā\\\" and \\\"مهندز muhandiz: 'Geometer, Feldmesser' ← andāza s. hindisa; مهندس muhandis = muhandiz\\\".\"},\n    {\"src\":\"AFM\",\"where\":\"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM.txt, l. 6428) s.v. الهنداز\",\"stance\":\"supports\",\n     \"note\":\"Addi Shir has الهنداز/المنداز 'والقیاس' beside هندس/المهندس and 'التقدیر والتخمین' — i.e. he lists the whole \"\n            \"h-n-d-s / h-n-d-z group among the Persian loans in Arabic (the OCR of this page is poor but the headwords are legible).\"},\n    {\"src\":\"KLN\",\"where\":\"Klein, s.v. (no entry)\",\"stance\":\"silent\",\n     \"note\":\"Klein's English etymological dictionary has no 'handasa'/'mohandes' entry (grep of KLN_1966/1971 for handas-, muhandis: no hits).\"}])\n\nN(id=9, lang=\"Persian\", words=\"hendeseh; mohandes\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"A textbook Persian→Arabic→Persian round trip. MP handāzag 'measure' was borrowed into Arabic as handasa \"\n    \"'measuring, geometry' with z > s and re-analysed as a quadriliteral root h-n-d-s; from it Arabic formed the \"\n    \"participle muhandis 'geometer, surveyor'. Both then came back into New Persian as the learned Arabic words \"\n    \"هندسه hendese 'geometry' and مهندس mohandes 'engineer' — so هندسه and native اندازه are doublets. \"\n    \"Mo'in states it flatly in his footnote to the Borhan entry هندسه: 'معرّب «اندازه»', quoting Bīrūnī's \"\n    \"at-Tafhīm 'هندسه چیست؟ دانستن اندازه‌ها و چندی یک از دیگر…'. Horn p.27 lists the same two Arabic loanwords under endāčten.\"),\n  derivation_fa=(\n    \"نمونهٔ کلاسیکِ رفت‌وبرگشتِ فارسی → عربی → فارسی. نامِ فارسی میانهٔ handāzag «اندازه» به عربی رفت و با بدل شدن z به س «هندسة» شد و در عربی ریشهٔ چهارحرفیِ «هـ ن د س» از آن انتزاع کردند و «مهندِس» ساختند؛ \"\n    \"سپس هر دو به فارسی نو بازگشتند. از این‌رو «هندسه» و «اندازه» دوگانه (doublet) اند. \"\n    \"معین در حاشیهٔ برهان قاطع ذیل «هندسه» صریح می‌نویسد «معرّب «اندازه»» و سخن بیرونی را گواه می‌آورد: «هندسه چیست؟ دانستن اندازه‌ها و چندیِ یک از دیگر…» (التفهیم). هرن نیز همین دو وام‌واژهٔ عربی را ذیل endāčten آورده است. \"\n    \"ادعای نورایی درست است.\"),\n  sources=[U[\"handasa\"], U[\"andaxtan\"]],\n  ref_check=[\n    {\"ref\":\"BQT:2379\",\"status\":\"supports\",\"note\":(\n      \"Borhan-e Qate' vol. 4 (BQT_v4_pages.txt, pdf leaf 461 → printed p. ~2378/2379) s.v. هندسه: \"\n      \"'هندسه ، بکسر اول و فتح سین بی‌نقطه ، بمعنی اندازه و شکل باشد', with Mo'in's footnote 'معرب «اندازه»' and \"\n      \"'بیرونی گوید: «هندسه چیست؟ دانستن اندازه‌ها و چندی یک از دیگر و خاصیت صورتها…» «التفهیم»' and a reference to Dozy II 799. \"\n      \"Exactly Nourai's claim, on the page he cites (±1).\"},\n    {\"ref\":\"HRN:27\",\"status\":\"supports\",\"note\":(\n      \"Horn p.27 no.117: \\\"arab. LW. muhandis 'Feldmesser', hindasat 'Geometrie' u. a. m. (de Lagarde, Arm. Stud., No. 116)\\\" \"\n      \"— Horn explicitly calls the Arabic words loans from the Iranian andāčak family.\")}],\n  consulted=[\n    {\"src\":\"PLA\",\"where\":\"Asbaghi p.270\",\"stance\":\"supports\",\n     \"note\":\"\\\"hindisa: 'Geometrie' … ← andāze MP. handāčak\\\"; \\\"muhandiz/muhandis: 'Geometer, Feldmesser' ← andāza\\\".\"},\n    {\"src\":\"BQT\",\"where\":\"Borhan-e Qate' p. ~167 s.v. اندازه\",\"stance\":\"supports\",\n     \"note\":\"'و تعریبش به هندسه کرده‌اند' — the Borhan says the same thing from the Persian end.\"},\n    {\"src\":\"ARB\",\"where\":\"al-Jawālīqī, al-Muʿarrab (ARB_mo3rb.txt l. 2721)\",\"stance\":\"partial\",\n     \"note\":\"The Muʿarrab's editorial notes discuss the s/z alternation in this word ('وأبدلوا الزای سینا فقالوا … المهندس'), \"\n            \"which is the sound substitution the loan requires.\"}])\n\nN(id=10, lang=\"Avestan\", words=\"vi-taxti\",\n  verdict=\"disputed\",\n  derivation=(\n    \"Avestan vi-taxti- f. is real and means 'melting, dissolving' (Bartholomae; Pokorny p.1059 prints \\\"Avestan \"\n    \"vi-taxti- f. 'das Zerfließen, Schmelzen'\\\" under tekʷ-), and Nourai's parenthetical 'run apart' is exactly \"\n    \"Pokorny's rationale. But modern Iranian etymology separates two homophonous roots here: Cheung 2007 sets up \"\n    \"*taHč 'to melt' (MP widāxtan, Parthian wdāc-, Sogd. wytʾyc, Khot. byāj-) from PIE *teH₂k- 'to melt' (LIV 617, \"\n    \"Pok. 1053, Gk. tḗkō), and says in as many words: \\\"the formally identical forms with the meaning 'to run, walk, \"\n    \"sim.' should be excluded (*tač¹)\\\". Wiktionary's گداختن entry follows the same line. So the WORD is right and \"\n    \"the meaning is right, but its attachment to this root is what current scholarship rejects.\"),\n  derivation_fa=(\n    \"واژهٔ اوستایی vi-taxti- واقعی است و «گداختن، آب شدن» معنی می‌دهد و پوکورنی (ص ۱۰۵۹) آن را ذیل *tekʷ- آورده و توجیه «از هم دویدن» نیز از اوست. \"\n    \"اما ریشه‌شناسی امروزی ایرانی دو ریشهٔ هم‌آوا را از هم جدا می‌کند: چونگ (۲۰۰۷) ریشهٔ *taHč «گداختن» را (پهلوی widāxtan، پارتی wdāc-، سغدی wytʾyc، ختنی byāj-) از هندواروپایی *teH₂k- «گداختن» می‌گیرد \"\n    \"(هم‌ریشه با tḗkō یونانی) و صریح می‌نویسد که صورت‌های هم‌شکل با معنای «دویدن» باید از آن جدا شوند. ویکی‌واژه نیز همین را می‌گوید. \"\n    \"پس پژوهش امروزی این پیوند را رد می‌کند: واژه و معنا درست است، ولی ریشه‌اش *tekʷ- نیست.\"),\n  sources=[U[\"godaxtan\"]],\n  ref_check=[{\"ref\":\"POK:1059\",\"status\":\"supports\",\"note\":(\n     \"Pokorny does put it here: \\\"Avestan vi-taxt'h [vi-taxti-] f. 'das Zerfließen, Schmelzen' (= Inf. Slavic *tekti)\\\", \"\n     \"POK_full.txt, Root/lemma tek\\\"-, Page(s) 1059-1060. Nourai reports his source faithfully; the source is what is now disputed.\")}],\n  consulted=[\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV pp. 375-376 s.v. *taHč 'to melt'\",\"stance\":\"contradicts\",\n     \"note\":\"\\\"«PIE \\\"enlarged\\\" *teH₂k- 'to melt' = LIV: 617 | Pok.: 1053… The close match in meaning between the Ir. and Gr. \"\n            \"forms suggests a common IE origin. Hence, the formally identical forms with the meaning 'to run, walk, sim.' \"\n            \"should be excluded (*tač¹).\\\"\"},\n    {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II p.217 s.v. vitāxtan\",\"stance\":\"supports\",\n     \"note\":\"\\\"vitāxtan vitāč- trans. to melt … Caus. of vi + Av. (624 sq.) tak-; MPrth wdxtn, wdc- … NP gudāxtan gudāz- \"\n            \"'to liquify'\\\" — Nyberg (1974) still derives it from Av. tak-, i.e. the older view Nourai follows.\"},\n    {\"src\":\"BRT\",\"where\":\"AiW cols. 624-626 s.v. tak- / vi-taxti-\",\"stance\":\"supports\",\n     \"note\":\"Bartholomae, to whom Nyberg's '(624 sq.)' refers, files vi-taxti- under the root tak-.\"}])\n\nN(id=11, lang=\"Persian\", words=\"godâxtan\",\n  verdict=\"plausible\",\n  derivation=(\n    \"گداختن gudāxtan 'to melt' is beyond doubt the continuation of MP widāxtan / widāz- (Manichaean wdāc-), \"\n    \"with the standard New Persian change of initial w- > g(u)- before a back vowel (MP widāxtan > NP gudāxtan, like \"\n    \"widaštan > guzaštan, wazurg > buzurg): so the step from the parent box (Av. vi-tax-) to this word is sound, and \"\n    \"Mo'in's own footnote in the Borhan says so. What is 'plausible' rather than 'confirmed' is only the inherited \"\n    \"root behind it: Cheung/LIV assign it to *taHč < PIE *teH₂k- 'melt', not to *tekʷ- 'run' (see #10). Nourai's \"\n    \"chart NOTE, 'compare with derivations from root Dhogh: to heat', is a red herring — Dhogh (*dhegwh- 'to burn') \"\n    \"has no part in gudāxtan.\"),\n  derivation_fa=(\n    \"«گداختن» بی‌گمان دنبالهٔ فارسی میانهٔ widāxtan/widāz- است؛ w آغازین در فارسی نو پیش از واکهٔ پسین به گ/گُ بدل شده است (widaštan > گذشتن، wazurg > بزرگ). \"\n    \"پس پیوندِ این جعبه با جعبهٔ مادر (اوستایی vi-tax-) درست است و حاشیهٔ معین در برهان قاطع نیز همین را می‌گوید: «گداختن … اوستا vitaxti، پهلوی vitāxtan». \"\n    \"تنها نکته، ریشهٔ هندواروپایی است: چونگ و LIV آن را از *teH₂k- «گداختن» می‌دانند نه از *tekʷ- «دویدن» (نگاه کنید به گرهٔ پیشین). \"\n    \"یادداشت نورایی دربارهٔ ریشهٔ «Dhogh: گرم کردن» نیز بی‌ربط است؛ «گداختن» هیچ پیوندی با *dʰegʷʰ- ندارد.\"),\n  sources=[U[\"godaxtan\"]],\n  ref_check=[\n    {\"ref\":\"NYB:217\",\"status\":\"supports\",\"note\":(\n      \"Nyberg, A Manual of Pahlavi II, p.217 (local NYB_vol2_glossary.txt, form-feed leaf 235 — the page footer of \"\n      \"leaf 236 reads '216 vitartan', confirming the offset): \\\"vitāxtan vitāč- trans. to melt: bē witāčēt 101¹⁷. — \"\n      \"Caus. of vi + Av. (624 sq.) tak-; MPrth wdxtn, wdc- and wdʾc- (MHC), Ghilain 50; MPrs. wdc- (S), Verbum 169; \"\n      \"Paz. vadāxtan vadāž- (SGV); NP gudāxtan gudāz- 'to liquify'.\\\" Exactly the chain of the box.\"},\n    {\"ref\":\"BQT:1777\",\"status\":\"supports\",\"note\":(\n      \"Borhan-e Qate' vol. 3 (BQT_v3_pages.txt, pdf leaf 573/574 → printed p. 1777; the page bottom carries the \"\n      \"continuation note 'بقیه … ۱۷۷۹') s.v. گداختن, with Mo'in's footnote: 'گداختن ‐ بضم اول و فتح پنجم = گدازیدن، \"\n      \"اوستا vitaxti / vitacina، پهلوی vitāxtan … آب شدن و آب کردن فلز با روغن یا جز آنها بوسیلهٔ حرارت'. The exact page Nourai cites.\")}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie 1971 s.v. widāxtan\",\"stance\":\"supports\",\n     \"note\":\"MacKenzie has the MP verb (wtʾhṭnʹ) 'melt' whose NP outcome is gudāxtan; the w- > g- development is the \"\n            \"standard one he records for wdaštan/guzaštan etc.\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV p.376 s.v. *taHč\",\"stance\":\"partial\",\n     \"note\":\"\\\"*NWIR: (+ *ui-) NP gudāxtan/gudāz- 'to smelt, melt'\\\" — same MP→NP chain, different IE root.\"},\n    {\"src\":\"HRN\",\"where\":\"Horn 1893 p.199 (cited by Cheung as the reference for this verb)\",\"stance\":\"supports\",\n     \"note\":\"Horn's entry for gudāxten is Cheung's first listed reference for *taHč, i.e. Horn already had the MP witāxtan > NP gudāxtan chain.\"}])\n\nN(id=12, lang=\"Avestan\", words=\"tačar; tačan; tahra\",\n  verdict=\"plausible\",\n  derivation=(\n    \"Two of the three are genuine Avestan and stand in Pokorny p.1059 in this very shape: tačar- n., an r/n-stem of \"\n    \"tac-, and tačan- adj. Bartholomae glosses tačan- 'laufend' (N 97) and uses tačar- as a unit of distance \"\n    \"('Wegmass', F 27a: 'yaθa asaṇat̄ haθram yāvat̄ tačarəm'), i.e. 'a course, a run' — so Nourai's glosses 'road' \"\n    \"and 'haste, hurry' are loose renderings of Pokorny's 'run, flow, pathway' and 'hurrying'. The third, 'tahra', is \"\n    \"NOT an Avestan word: Pokorny prints it as a reconstruction, \\\"iran. *tahra- 'quick, fast'\\\" (the Avestan adjective \"\n    \"actually attested is taxra-/staxra- 'firm, strong'). The box therefore mixes attested Avestan with a starred \"\n    \"Iranian form under one language label.\"),\n  derivation_fa=(\n    \"دو صورت از سه صورت این جعبه به‌راستی اوستایی‌اند و در همان صفحهٔ ۱۰۵۹ پوکورنی آمده‌اند: tačar- (اسم با ستاک r/n از tac-) و tačan- (صفت). \"\n    \"بارتولومه tačan- را «دونده» معنی می‌کند و tačar- را یکای سنجش راه می‌داند («yaθa asaṇat̄ haθram yāvat̄ tačarəm»)، پس «راه» و «شتاب» نزد نورایی برگردانی آزاد از «دو، جریان، گذرگاه» و «شتابان» است. \"\n    \"اما «tahra» واژهٔ اوستایی نیست؛ پوکورنی آن را با ستاره و با برچسب «ایرانی» آورده است: iran. *tahra- «تند، سریع» (صفت اوستاییِ گواهی‌شده taxra-/staxra- «استوار، سخت» است). \"\n    \"پس در این جعبه صورت‌های گواهی‌شدهٔ اوستایی با یک صورت بازسازی‌شدهٔ ایرانی زیر یک برچسب زبانی درآمیخته‌اند؛ ادعای نورایی با احتیاط پذیرفتنی است.\"),\n  sources=[U[\"pie\"]],\n  ref_check=[{\"ref\":\"POK:1059\",\"status\":\"partial\",\"note\":(\n     \"POK_full.txt, tek\\\"- p.1059: \\\"Avestan taka- m., np. tak 'run, flow'; Avestan tacar- n. 'run, flow, pathway', \"\n     \"tacan- 'hurrying'; tač-ap- 'running water (containing)', iran. *tahra- 'quick, fast'.\\\" All three of Nourai's \"\n     \"words are on the cited page, but Pokorny labels only the first two Avestan and marks *tahra- as a reconstructed \"\n     \"Iranian form, which Nourai's box does not.\")}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"Bartholomae, AiW s.v. tačan- and tačar-\",\"stance\":\"partial\",\n     \"note\":\"\\\"j. tacan- Adj. 'laufend'\\\" (N 97) and, under the measure terms, \\\"yaθa asaṇat̄ haθram yāvat̄ tačarəm 'ein H. \"\n            \"zweimal (genommen ist) soviel als ein Tr.' F. 27a\\\" — both attested, with 'running/course', not 'road, haste'. \"\n            \"No Avestan *tahra- (only staxra- 'stark, fest').\"},\n    {\"src\":\"IEC\",\"where\":\"Mann col. 1372 s.v. tokos, us (1)\",\"stance\":\"supports\",\n     \"note\":\"\\\"Av. takəm, n. 'run, flow'; takō, adj. 'running' … Per. tag, s. 'race'\\\" — Mann has the same Avestan noun family.\"}])\n\nN(id=13, lang=None, words=\"\",\n  verdict=\"unverified\",\n  derivation=(\n    \"Blank box. On the printed page (pdf p. 498, book p. 468; image saved at \"\n    \"data/verification/sources/refs/ocr/BOOK/498.png) the large rectangle to the right of the \"\n    \"tačar/tačan/tahra box is drawn but left completely empty — no language header, no reference, no word. \"\n    \"The extraction is faithful; there is nothing to verify. Presumably Nourai intended the Persian reflexes \"\n    \"(تک tak, تگ tag 'a run', تیز tīz 'swift') and never filled the box in.\"),\n  derivation_fa=(\n    \"جعبهٔ سفید. در صفحهٔ چاپی (تصویر ذخیره‌شده در data/verification/sources/refs/ocr/BOOK/498.png) مستطیل بزرگِ کنار جعبهٔ tačar/tačan/tahra کشیده شده ولی کاملاً تهی است: \"\n    \"نه برچسب زبان دارد، نه ارجاع، نه واژه. استخراج داده وفادار است و چیزی برای راستی‌آزمایی نیست؛ ظاهراً نویسنده می‌خواسته بازتاب‌های فارسی («تک»، «تگ»، «تیز») را در آن بیاورد و ناتمام مانده است.\"),\n  sources=[],\n  ref_check=[{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"Empty box in the printed chart; no reference is given and none applies.\"}],\n  consulted=[{\"src\":\"BOOK\",\"where\":\"printed page, pdf p.498 (data/verification/sources/refs/ocr/BOOK/498.png)\",\"stance\":\"silent\",\n              \"note\":\"The box is drawn but blank on the page itself — confirmed by rendering the page at 200 dpi.\"}])\n\nN(id=14, lang=\"Old Persian\", words=\"taxša\",\n  verdict=\"plausible\",\n  derivation=(\n    \"The word for the bow/arrow is an Iranian form, but it is not attested in Old Persian. Pokorny p.1059 writes \"\n    \"\\\"iran. (skyth.) *tahsa- (npers. taxs) 'arrow, bow'\\\", Watkins (AHD) \\\"suffixed o-grade form *tokʷ-so- in Iranian \"\n    \"*taxsa-, bow\\\", Klein \\\"Scythian *taxsha-\\\"; Kent's Old Persian lexicon has no such lexeme (the only OP form with \"\n    \"taxs- is the verb hamātaxsaiy 'I strove', a different root). The formation is *tokʷ-so- to *tekʷ- 'run', the bow \"\n    \"or arrow being 'the runner/that which flies'. So Nourai's form and its root are fine; the language label \"\n    \"'Old Persian' overstates the evidence — it should be Iranian/Scythian, and the form should carry an asterisk.\"),\n  derivation_fa=(\n    \"این واژه صورتی ایرانی است، ولی در پارسی باستان گواهی نشده. پوکورنی (ص ۱۰۵۹) می‌نویسد: iran. (skyth.) *tahsa- «تیر، کمان» (فارسی نو taxs)؛ واتکینز آن را Iranian *taxsa- و کلاین Scythian *taxsha- می‌نامد. \"\n    \"در واژه‌نامهٔ پارسی باستانِ کنت چنین واژه‌ای نیست (تنها صورتِ taxs- در آنجا فعل hamātaxsaiy «کوشیدم» است که از ریشهٔ دیگری است). \"\n    \"ساختِ آن *tokʷ-so- از *tekʷ- «دویدن» است؛ کمان یا تیر «رونده/پرنده» نامیده شده. \"\n    \"پس صورت و ریشه درست است، اما برچسب «پارسی باستان» بیش از گواهی‌هاست و باید «ایرانی/سکایی» و با ستاره نوشته می‌شد.\"),\n  sources=[U[\"taxs\"], U[\"toxic\"]],\n  ref_check=[{\"ref\":\"POK:1059\",\"status\":\"partial\",\"note\":(\n     \"POK_full.txt p.1059: \\\"here perhaps as 'dahinschießend': iran. (skyth.) *tahsa- (npers. taxs) 'arrow, bow', from \"\n     \"which gr. toxon ds., Latin taxus 'yew' (Benveniste Mél. Boisacq 1, 37 ff., Mayrhofer 1, 467 f.)\\\". The word and \"\n     \"the root are Pokorny's; the label 'Old Persian' and the missing asterisk are Nourai's.\")}],\n  consulted=[\n    {\"src\":\"KNT\",\"where\":\"Kent, Old Persian, Lexicon\",\"stance\":\"silent\",\n     \"note\":\"Grepping KNT_full.txt for taxsā/taxša returns only the verb forms hamātaxsaiy / hamataxsatā ('strive, be \"\n            \"active', OP taxs-) and the royal name Arta-xšaçā — no noun *taxša- 'bow'.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985, s.v. tekʷ-\",\"stance\":\"supports\",\n     \"note\":\"\\\"tekʷ-. To run, flee. Suffixed o-grade form *tokʷ-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, \"\n            \"bow, also (in the plural) bow and arrow (< 'that which flies'): TOXIC. [Pok. tekʷ- 1059.]\\\" — 'Iranian', not \"\n            \"'Old Persian'.\"},\n    {\"src\":\"KLN\",\"where\":\"Klein 1966, s.v. toxic\",\"stance\":\"supports\",\n     \"note\":\"\\\"… fr. τόξον, 'a bow or arrow', fr. Scythian *taxsha-, whence also L. taxus, 'yew'.\\\"\"}])\n\nN(id=15, lang=\"Persian\", words=\"taxš\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"تخش taxs is a real (now archaic, poetic) New Persian word for a kind of arrow or a small crossbow, the direct \"\n    \"continuant of the Iranian *taxsa- of the parent box; Pokorny cites it as 'npers. taxs' when reconstructing \"\n    \"*tahsa-. Dehkhoda, drawing on Borhan, Ghiyāṯ al-luġāt, Ānandrāj and Nāẓim al-aṭibbāʾ, gives 'نوعی از تیر' and \"\n    \"'نوعی از کمان که تیر بسیار کوچکی دارد', and notes that Wolff's Shahnameh glossary, following Nöldeke and Paul Horn, \"\n    \"renders it 'کمان، قوس' precisely at the Ferdowsi line Nourai quotes ('جگرخستهٔ تیغ و تخش منند'). The homonym \"\n    \"taxs 'chief seat; striving' belongs to تخشیدن and is a different word.\"),\n  derivation_fa=(\n    \"«تخش» واژه‌ای واقعی (امروز کهن و شاعرانه) در فارسی نو است به معنای گونه‌ای تیر یا کمانِ کوچک، و دنبالهٔ مستقیم همان *taxsa- ایرانیِ جعبهٔ مادر؛ پوکورنی هنگام بازسازی *tahsa- خودِ همین صورت را «npers. taxs» می‌آورد. \"\n    \"دهخدا به نقل از برهان، غیاث اللغات، آنندراج و ناظم الاطباء می‌نویسد «نوعی از تیر» و «نوعی از کمان که تیر بسیار کوچکی دارد» و می‌افزاید که ولف در فهرست شاهنامه به پیروی از نلدکه و پاول هرن آن را «کمان، قوس» دانسته و همان بیت فردوسیِ موردِ استناد نورایی («جگرخستهٔ تیغ و تخش منند») را گواه آورده است. \"\n    \"«تخش» دیگری که به معنی «صدر مجلس/کوشنده» است از «تخشیدن» می‌آید و واژهٔ جداگانه‌ای است. ادعای نورایی درست است.\"),\n  sources=[U[\"taxs\"], U[\"dehkhoda_taxs\"]],\n  ref_check=[{\"ref\":\"BQT:476\",\"status\":\"supports\",\"note\":(\n     \"Borhan-e Qate' p. ~474-476 (BQT_v1_pages.txt, form-feed leaf 702) is the تخش/تخشیدن/تخله page and it carries \"\n     \"the very Ferdowsi couplet Nourai prints: 'همه بنده در پیش رخش منند / جگرخستهٔ تیغ و تخش منند' with the source note \"\n     \"'شاهنامه چ ج۲ ص۹۹' and Mo'in's etymological footnotes. Dehkhoda's article on تخش attributes the 'bow/arrow' senses to \"\n     \"'(برهان)' and quotes 'از حاشیه برهان چ معین'.\")}],\n  consulted=[\n    {\"src\":\"MON\",\"where\":\"Dehkhoda/Mo'in article تخش (abadis.ir, quoting حاشیه برهان چ معین)\",\"stance\":\"supports\",\n     \"note\":\"'تخش … || نوعی از تیر. (برهان)(غیاث اللغات)(ناظم الاطباء). ولف در فهرست شاهنامه از قول نلدکه و پاول هرن این کلمه را بمعنی تیر یاد کرده است. \"\n            \"(از حاشیه برهان چ معین) … || بعضی گویند تخش نوعی از کمان است که تیر بسیار کوچکی دارد. (برهان)'.\"},\n    {\"src\":\"ARY\",\"where\":\"Aryanpur p.187, note 2 to the tāxtan entry\",\"stance\":\"supports\",\n     \"note\":\"'۲ بازگشت به: تک، تخش' — Aryanpur cross-refers تخش to the tāxtan root entry, as Nourai does.\"}])\n\nN(id=16, lang=\"Greek\", words=\"toxon\",\n  verdict=\"plausible\",\n  derivation=(\n    \"Greek τόξον tóxon 'bow' (pl. 'bow and arrows') is not an inherited Greek word but, on the standard view, an early \"\n    \"loan from Iranian: Pokorny \\\"iran. (skyth.) *tahsa- … from which gr. toxon\\\", Watkins \\\"Iranian *taxsa-, bow, \"\n    \"borrowed into Greek toxon\\\", Klein \\\"fr. Scythian *taxsha-\\\" — presumably through contact with the Scythians of the \"\n    \"North Pontic steppe, famous archers, well before the 5th c. BCE. The dissenting voice is Beekes, who, pointing to \"\n    \"the early (Homeric) attestation, prefers a Pre-Greek substrate origin; Wiktionary hedges 'possibly a cognate of \"\n    \"Latin taxus or borrowed from Iranian: compare Persian تخش'. Hence plausible, not confirmed. \"\n    \"NOTE ON THE CHART: on the printed page the arrow into this Greek box comes out of the bottom of the \"\n    \"Old Persian taxša box (#14), not from the root — i.e. the book does derive Greek from the Iranian word, exactly as \"\n    \"the modern authorities do. The extraction records parent 0, which is an extraction error, not an error of Nourai's.\"),\n  derivation_fa=(\n    \"واژهٔ یونانی τόξον «کمان» (در جمع «تیر و کمان») واژه‌ای موروثی در یونانی نیست، بلکه بنا بر دیدگاه رایج وام‌واژه‌ای کهن از ایرانی است: \"\n    \"پوکورنی می‌نویسد از iran. (skyth.) *tahsa- و واتکینز از Iranian *taxsa- و کلاین از Scythian *taxsha- — احتمالاً از راه تماس با سکاهای شمال دریای سیاه که کمانداران نامدار بودند، پیش از سدهٔ پنجم پیش از میلاد. \"\n    \"در برابر، بیکس با استناد به کهن بودن گواهی هومری، آن را واژه‌ای پیشایونانی می‌داند و ویکی‌واژه نیز محتاطانه هر دو امکان را می‌آورد. پس «با احتیاط پذیرفتنی». \"\n    \"نکتهٔ نموداری: در صفحهٔ چاپی پیکان این جعبه از پایینِ جعبهٔ «Old Persian taxša» بیرون می‌آید نه از ریشه؛ یعنی خودِ کتاب یونانی را از صورت ایرانی می‌گیرد، درست همان‌گونه که مرجع‌های امروزی می‌گویند. \"\n    \"در داده‌های استخراج‌شده پدرِ این گره به‌اشتباه ۰ ثبت شده است.\"),\n  sources=[U[\"toxon\"], U[\"toxic\"]],\n  ref_check=[{\"ref\":\"AHD:1545\",\"status\":\"supports\",\"note\":(\n     \"Nourai's AHD page numbers are for the 1976 New College appendix (pp.1505-1550), which is not open online; the same \"\n     \"root entry in the 1985 standalone Watkins (AHD_watkins1985.txt) reads: \\\"tekʷ-. To run, flee. Suffixed o-grade form \"\n     \"*tokʷ-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, bow, also (in the plural) bow and arrow (< 'that which \"\n     \"flies'): TOXIC. [Pok. tekʷ- 1059.]\\\" p.1545 is in the t- range of the 1976 appendix, so the citation is plausible \"\n     \"as well as substantively right.\")}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein 1966, s.v. toxic\",\"stance\":\"supports\",\n     \"note\":\"\\\"… neut. of the adjective τοξικός, 'pertaining to a bow or arrow', fr. τόξον, 'a bow or arrow', fr. Scythian \"\n            \"*taxsha-, whence also L. taxus, 'yew'. Cp. taxus.\\\"\"},\n    {\"src\":\"POK\",\"where\":\"IEW p.1059\",\"stance\":\"supports\",\n     \"note\":\"\\\"iran. (skyth.) *tahsa- (npers. taxs) 'arrow, bow', from which gr. toxon ds., Latin taxus 'yew' (Benveniste \"\n            \"Mél. Boisacq 1, 37 ff.)\\\".\"},\n    {\"src\":\"WEB\",\"where\":\"Etymonline s.v. toxic (summarising Watkins and Beekes)\",\"stance\":\"partial\",\n     \"note\":\"\\\"toxon 'bow,' which has been regarded as a loan-word from Scythian. Watkins suggests a possible source in \"\n            \"Iranian taxsa- 'bow' (from PIE *tekw- 'to run, flee'). Beekes, pointing to the early attestation of the Greek \"\n            \"word, suggests a Pre-Greek origin.\\\"\"}])\n\nN(id=17, lang=\"Latin\", words=\"toxicum\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Latin toxicum 'poison' is a straight borrowing of Greek τοξικón (φάρμακον) 'the (drug) for arrows', the neuter \"\n    \"of τοξικός 'of a bow or arrow' — the substance Scythian and Gaulish archers smeared on their arrowheads. \"\n    \"In Latin (Plautus, Ovid, Pliny) the adjective's reference to archery is lost and the word simply means 'poison'. \"\n    \"Nourai's gloss 'poison for arrows' is precisely the Greek phrase; drawing it from Greek toxon rather than from \"\n    \"toxikón is a one-step compression, not an error.\"),\n  derivation_fa=(\n    \"«toxicum» لاتین وام‌واژه‌ای مستقیم از یونانی τοξικón (φάρμακον) «داروی [زهرِ] تیر» است، یعنی صورت خنثای صفت τοξικός «وابسته به کمان و تیر» — همان زهری که کمانداران سکایی و گُلی به پیکان می‌آلودند. \"\n    \"در لاتین (پلاوتوس، اوویدیوس، پلینیوس) پیوند آن با تیراندازی از میان رفت و تنها معنای «زهر» ماند. معنایی که نورایی داده («زهر تیرها») دقیقاً همان عبارت یونانی است؛ کشیدن پیکان از toxon به‌جای toxikón فقط فشرده‌سازی یک پله است، نه خطا. \"\n    \"ادعای نورایی درست است.\"),\n  sources=[U[\"toxic\"]],\n  ref_check=[{\"ref\":\"AHD:1359\",\"status\":\"not_checked\",\"note\":(\n     \"AHD:1359 is a page of the main word-list of the 1976 New College Edition (s.v. toxic/toxin), which is not openly \"\n     \"readable (the Internet Archive copies are lending-only). The claim is however exactly what Klein and Etymonline \"\n     \"state, and Watkins's appendix entry (checked on node #16) ends '… TOXIC'.\")}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein 1966, s.v. toxic\",\"stance\":\"supports\",\n     \"note\":\"\\\"toxic, adj., pertaining to poison. — ML. toxicus, fr. L. toxicum, 'poison', fr. Gk. τοξικόν (scil. \"\n            \"φάρμακον), 'arrow poison', neut. of the adjective τοξικός …\\\"\"},\n    {\"src\":\"WEB\",\"where\":\"Etymonline s.v. toxic\",\"stance\":\"supports\",\n     \"note\":\"\\\"from Latin toxicum 'poison,' from Greek toxikon (pharmakon) '(poison) for use on arrows'…\\\"\"}])\n\nN(id=18, lang=\"English\", words=\"toxic\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"English toxic is first recorded in the 1660s in the sense 'of or pertaining to poisons, poisonous', taken from \"\n    \"French toxique and directly from Late Latin toxicus 'poisoned' / Medieval Latin toxicus, on Latin toxicum. \"\n    \"The modern extended uses (toxic waste 1955, toxic 'harmful' of people and behaviour) are twentieth-century. \"\n    \"The chain Latin → (French) → English as drawn is uncontroversial.\"),\n  derivation_fa=(\n    \"واژهٔ انگلیسی toxic نخستین بار در دههٔ ۱۶۶۰ به معنای «زهرآگین، وابسته به زهر» ثبت شده و از فرانسهٔ toxique و مستقیماً از لاتین متأخر toxicus «زهرآلود» (بر پایهٔ toxicum) گرفته شده است. \"\n    \"کاربردهای گستردهٔ امروزی (toxic waste از ۱۹۵۵ و toxic دربارهٔ رفتار و آدم‌ها) از سدهٔ بیستم‌اند. زنجیرهٔ لاتین ← (فرانسه) ← انگلیسی که در نمودار کشیده شده بی‌مناقشه است و ادعای نورایی درست است.\"),\n  sources=[U[\"toxic\"]],\n  ref_check=[{\"ref\":\"(none cited in the box)\",\"status\":\"not_checked\",\"note\":\n     \"The English box carries no reference; the parent box's AHD:1359 covers it (see #17).\"}],\n  consulted=[\n    {\"src\":\"WEB\",\"where\":\"Etymonline s.v. toxic (adj.)\",\"stance\":\"supports\",\n     \"note\":\"\\\"1660s, 'of or pertaining to poisons, poisonous,' from French toxique and directly from Late Latin toxicus \"\n            \"'poisoned,' from Latin toxicum 'poison'… As a noun from 1890.\\\"\"},\n    {\"src\":\"KLN\",\"where\":\"Klein 1966, s.v. toxic\",\"stance\":\"supports\",\n     \"note\":\"\\\"toxic, adj., pertaining to poison. — ML. toxicus, fr. L. toxicum, 'poison'…\\\"\"}])\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Teku 1, Tekw\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *tekʷ- 'to run, to flow' (Pokorny 1059-1060; Watkins/AHD tekʷ- 'to run, flee')\",\n  \"note\": (\n    \"Pokorny's IEW pp.1059-1060 heads the entry \\\"tekʷ-\\\" and glosses it 'to run; to flow' — Nourai's gloss word for \"\n    \"word. His two headwords are one root: 'Tekw' is his transcription of *tekʷ-, and 'Teku 1' the same root written \"\n    \"with -u for the labial glide (his own third entry on the page, 'Tekw', is a redirect to 'Teku 1'). The language \"\n    \"label 'Indo-European' is right. One modern caveat: the root-final stop is contested — older handbooks (Pokorny, \"\n    \"Watkins, Mann, LIV) write the labiovelar *kʷ on the strength of Hittite watkuzi, while Kroonen, Adams (Toch. B \"\n    \"cake) and EIEC argue for plain *k, so Wiktionary lists *tek- as an alternative reconstruction. That does not \"\n    \"affect any Iranian node on this page. The real problems on this chart are downstream: the melt-branch (#10, #11) \"\n    \"belongs to a different root by current scholarship, and the 'throw/measure' branch (#5-#9) is assigned by \"\n    \"Cheung to a homophonous *tač².\"),\n  \"note_fa\": (\n    \"پوکورنی در «فرهنگ ریشه‌شناختی هندواروپایی» صفحه‌های ۱۰۵۹–۱۰۶۰ سرواژهٔ *tekʷ- را با معنای «دویدن؛ روان شدن» می‌آورد — همان معنایی که نورایی داده است. \"\n    \"دو سرواژهٔ نورایی («Teku 1» و «Tekw») در حقیقت یک ریشه‌اند و خودِ او در همین صفحه «Tekw» را به «Teku 1» ارجاع داده است؛ برچسب «هندواروپایی» نیز درست است. \"\n    \"تنها نکتهٔ امروزی این است که همخوان پایانی ریشه مورد اختلاف است: فرهنگ‌های قدیمی‌تر (پوکورنی، واتکینز، مان، LIV) بر پایهٔ watkuzi هیتی *kʷ لبی‌کامی می‌نویسند، \"\n    \"ولی کرونن و آدامز (با استناد به cake تخاری ب) و EIEC *k سادّه را ترجیح می‌دهند و ویکی‌واژه *tek- را به‌عنوان بازسازی جایگزین آورده است؛ این اختلاف بر هیچ‌یک از گره‌های ایرانی این صفحه اثر ندارد. \"\n    \"اشکال‌های واقعی این نمودار در شاخه‌های پایین‌دست است: شاخهٔ «گداختن» (گره‌های ۱۰ و ۱۱) بنا بر پژوهش امروزی به ریشهٔ دیگری می‌رسد و شاخهٔ «انداختن/هندسه» (گره‌های ۵ تا ۹) را چونگ به ریشهٔ هم‌آوای *tač² می‌برد.\"),\n  \"sources\": [U[\"pie\"], U[\"toxic\"]],\n  \"ref_check\": [{\"ref\":\"POK:1059\",\"status\":\"supports\",\"note\":POK_Q}],\n  \"consulted\": [\n    {\"src\":\"POK\",\"where\":\"IEW pp.1059-1060, Root/lemma tekʷ-\",\"stance\":\"supports\",\n     \"note\":\"Headword and gloss match Nourai exactly ('to run; to flow'); references at the end of the entry: \"\n            \"\\\"WP. I 715 f., Trautmann 316 f., Vasmer 3, 89, 113 f., Mayrhofer 1, 466 f.\\\"\"},\n    {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 715 f. (the reference Pokorny himself gives)\",\"stance\":\"supports\",\n     \"note\":\"Pokorny's entry closes 'WP. I 715 f.'; WLD Bd. I p.715 f. is the earlier version of the same article \"\n            \"(the local WLD_Bd1 OCR shows the surrounding text of *tekʷ-/*tekʷu-s at that point: \"\n            \"'entw. moviertes Fem. zu *tekʷu-s, oder zu *tekʷu-s: ai. táku-ḥ').\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 (AHD_watkins1985.txt), s.v. tekʷ-\",\"stance\":\"supports\",\n     \"note\":\"\\\"tekʷ-. To run, flee. … [Pok. tekʷ- 1059.]\\\" — same root, same Pokorny page; Watkins glosses 'run, flee' \"\n            \"rather than 'run, flow'.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann, IECD col. 1372 s.v. tek- (2)\",\"stance\":\"supports\",\n     \"note\":\"\\\"tek- (2) (teko, tekmi) 'run, flow'. (Var: teks-). WP I, 715\\\" — Mann writes plain k and gives the same gloss.\"},\n    {\"src\":\"CHEUNG\",\"where\":\"EDIV pp. 373-376, the three roots *tač¹, *tač², *taHč\",\"stance\":\"partial\",\n     \"note\":\"Cheung splits what Pokorny (and Nourai) keep together: *tač¹ 'to flow, run, walk' (< *tekʷ-), *tač² \"\n            \"'to reach for, attain' (< *tek-) and *taHč 'to melt' (< *teH₂k-).\"}],\n  \"nodes\": nodes,\n}\n\nout = {\n  \"pdf_page\": 498,\n  \"book_page\": 468,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [entry],\n}\n\np = \"/home/sfmqrb/git/rishe/data/verification/page-498.json\"\nwith open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"wrote\", p, len(nodes), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-498.py",
 "description": "Build page-498.json"
}
```


### [2026-09-14T03:28:28.343Z] TOOL RESULT

```
Exit code 1
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-498.py", line 84
    "Cf. tokos … Per. ham-tag 'fellow-traveller'\" — it has tāxtan, tāzīdan and ham-tag, i.e. three of Nourai's four words."},
                                                                                                                            ^
SyntaxError: closing parenthesis '}' does not match opening parenthesis '(' on line 81
```


## [2026-09-14T03:28:44.614Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; python3 - <<'EOF'\np='build-498.py'\ns=open(p,encoding='utf-8').read()\nfixes=[\n ('four words.\"},','four words.\")},'),\n (\"'از: تک + آور (آوردن)'.\\\"},\",\"'از: تک + آور (آوردن)'.\\\")},\"),\n (\"not pairi-; Cheung and Wiktionary give *pari-, Nourai's form.\\\"},\",\"not pairi-; Cheung and Wiktionary give *pari-, Nourai's form.\\\")},\"),\n ('the right page for the daughter word.\"}]','the right page for the daughter word.\")}]'),\n ('the Pahlavi noun, and the Arabic loans.\"},','the Pahlavi noun, and the Arabic loans.\")},'),\n ('on the page he cites (±1).\"},','on the page he cites (±1).\")},'),\n ('Exactly the chain of the box.\"},','Exactly the chain of the box.\")},'),\n]\nfor a,b in fixes:\n    assert a in s, a\n    s=s.replace(a,b)\nopen(p,'w',encoding='utf-8').write(s)\nprint('ok')\nEOF\npython3 build-498.py",
 "description": "Fix parens and build"
}
```


### [2026-09-14T03:28:45.720Z] TOOL RESULT

```
ok
wrote /home/sfmqrb/git/rishe/data/verification/page-498.json 18 nodes
```


## [2026-09-14T03:28:47.920Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-498.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 498",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T03:28:48.947Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 9, 'plausible': 7, 'disputed': 1, 'unverified': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'partial': 4, 'not_checked': 8, 'not_found': 1}
books consulted: {'supports': 35, 'partial': 7, 'contradicts': 2, 'silent': 3} | by book: {'CHEUNG': 6, 'BRT': 5, 'PHD': 5, 'HRN': 5, 'KLN': 5, 'WEB': 3, 'IEC': 2, 'ARY': 2, 'POK': 2, 'BQT': 2, 'NYB': 2, 'PLA': 2, 'AFM': 1, 'ARB': 1, 'BOOK': 1, 'KNT': 1, 'AHD': 1, 'MON': 1}
```


## [2026-09-14T03:29:09.575Z] AGENT

Done. `data/verification/page-498.json` written; `verify_check.py 498` reports **0 PROBLEM lines** (18/18 nodes).

**Page 498 (book p. 468) — root "Teku 1, Tekw" = PIE \*tekʷ- "to run, flow" (Pokorny 1059-60): root confirmed.**

Node verdicts: 9 confirmed · 7 plausible · 1 disputed · 1 unverified.
Ref checks: 12 supports · 4 partial · 1 not_found · 8 not_checked (boxes with no refs / AHD:1359 & MON:5176 not openable).

Disputed / flagged:
- **#10 Av. vi-taxti "to melt"** — Pokorny p.1059 really does file it under \*tekʷ-, but Cheung (EDIV 375-6) sets up a separate \*taHč "to melt" < PIE \*teh₂k- (Gk. tḗkō) and says in as many words that the "run, walk" homophones "should be excluded"; Wiktionary/LIV agree. #11 گداختن kept at *plausible* (MP widāxtan > gudāxtan itself is certain; Mo'in's Borhan footnote at p.1777 confirms it).
- **#5/#6/#7 ham-tač → andâxtan/andâzeh** — *plausible*: Horn no.117 and Pokorny back Nourai (\*ham- + √tac-), but Cheung assigns the whole \*ham-/\*para- group to a homophonous \*tač² "to reach, attain" < PIE \*tek-. Also no Avestan hąm.tac- "to throw" is attested (Avestan has only hąm.tacina- "flowing together"); the gloss is the Middle Persian sense.
- **#4 pardâxtan**, **#12 tahra** (Pokorny marks it "iran. \*tahra-", not Avestan), **#14 "Old Persian" taxša** (Pokorny/Watkins/Klein: Iranian/Scythian \*taxša-, unattested in OP — Kent has no such lexeme), **#16 Greek toxon** (Beekes prefers Pre-Greek) — all *plausible* for the reasons noted in the file.
- **#13** — blank box, genuinely printed empty in the book; extraction faithful; *unverified*.

Extraction error the owner should fix:
- **Node #16 (Greek toxon) has `parent: 0` in `data/extracted/batch/page-498.json`, but the printed chart draws its arrow out of the bottom of the Old Persian `taxša` box (#14)** — see `data/verification/sources/refs/ocr/BOOK/498.png`. This matters: with the printed parent, Nourai agrees with Pokorny/Watkins/Klein (Greek borrowed the Iranian word), whereas the extracted tree makes Greek an independent IE descendant.

Best finds: BQT:2379 (Mo'in's footnote s.v. هندسه: «معرّب «اندازه»» + Bīrūnī's Tafhīm), HRN:27 (Nourai's andāxtan→handasa arrow verbatim), NYB:217 and BQT:1777 both exact. BQT:128 (node #5) is `not_found` — that page is in the اسـ section; the Borhan entry actually wanted (اندازه, "و تعریبش به هندسه کرده‌اند") is at p. ~167.
