# Verification process log — verify-page-376


## [2026-09-07T20:16:24.100Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 376 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-376.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-376.json. Write /home/sfmqrb/git/rishe/data/verification/page-376.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 376` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:16:26.050Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-07T20:16:26.648Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:16:26.660Z] TOOL RESULT

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


## [2026-09-07T20:16:27.608Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-376.txt"
}
```


### [2026-09-07T20:16:27.684Z] TOOL RESULT

```
1	=== PDF page 376 (book page 346) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ost : bone  (refs POK:783)
4	#1 (parent #0) [Avestan] refs=SYN:207; POK:783; KLN:1099 | ast, ascu : bone ; asča : shin bone
5	  #2 (parent #1) [Pahlavi] refs=BQT:124; HRN:20 | astag, astak : bone ; astuxan : bone
6	    #3 (parent #2) [Persian] refs=MON | ast 2 «است ۲» : bone ; ostoxân «استخوان» : bone ; hasteh «هسته» : core ; xastu «خستو ۱» : core
7	#4 (parent #0) [Old Persian] refs=TZF:26 | ast : bone
8	#5 (parent #0) [Sogdian] refs=SOD:67 | `stk : bone
9	#6 (parent #0) [Latin] refs=AHD | os 1 : bone
10	  #7 (parent #6) [English] refs=None | os ; ossify
11	#8 (parent #0) [Greek] refs=AHD | osteon : bone ; ostreon : oyster
12	  #9 (parent #8) [English] refs=None | osteo- ; oyster
13	--- entry 1 ---
14	ROOT [Indo-European] Ôus 1, Au 1, Aus 1 : ear  (refs POK:78,785; KLN:126,494)  PART 1
15	#1 (parent #0) [Avestan] refs=POK:78; HRN:8; KLN:126 | aviš, avišiya : heard, known, clear
16	  #2 (parent #1) [Persian] refs=None | âškâr «آشکار» : clear, obvious
17	#3 (parent #0) [Avestan] refs=POK:785 | ŭši : two ears, intelligence, mortal life ; ŭši-dâta : intelligent ☞Dô 2
18	  #4 (parent #3) [Persian] refs=POK:785 | hŭš 1 «هوش ۱» : intelligence ; hŭšyâr «هوشیار» : intelligent
19	  #5 (parent #3) [Avestan] refs=BQT:178; FSF:51 | an-aoša : without a mortal life
20	    #6 (parent #5) [Pahlavi] refs=BQT:178 | anôšak : eternal life ; anôšak-ruvân : with eternal spirit
21	      #7 (parent #6) [Persian] refs=BQT:178; FSF:51 | anušeh «انوشه» : eternal, happiness, wine ; Anošîravân «انوشیروان» : "with eternal spirit"
22	      #8 (parent #6) [Persian] refs=ARM:206; HRN:30 | nŭš «نوش» : drink (for eternal life) ; nŭšîn «نوشین» : sweet drink ; nŭšîdan «نوشیدن» : to drink | extra: نوشدارو، نوشابه
23	
```


## [2026-09-07T20:16:31.696Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-376.json",
 "description": "Read source JSON for page 376"
}
```


### [2026-09-07T20:16:31.730Z] TOOL RESULT

```
{
  "pdf_page": 376,
  "book_page": 346,
  "entries": [
    {
      "root": {
        "name": "Ost",
        "lang": "Indo-European",
        "refs": "POK:783",
        "gloss": "bone",
        "note": "See the note under root \"Kost:rib bone\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SYN:207; POK:783; KLN:1099",
          "words": [
            {"translit": "ast, ascu", "gloss": "bone", "script": null},
            {"translit": "asča", "gloss": "shin bone", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:124; HRN:20",
          "words": [
            {"translit": "astag, astak", "gloss": "bone", "script": null},
            {"translit": "astuxan", "gloss": "bone", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "ast 2", "gloss": "bone", "script": "است ۲"},
            {"translit": "ostoxân", "gloss": "bone", "script": "استخوان"},
            {"translit": "hasteh", "gloss": "core", "script": "هسته"},
            {"translit": "xastu", "gloss": "core", "script": "خستو ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "TZF:26",
          "words": [
            {"translit": "ast", "gloss": "bone", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:67",
          "words": [
            {"translit": "`stk", "gloss": "bone", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "os 1", "gloss": "bone", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "os", "gloss": null, "script": null},
            {"translit": "ossify", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "osteon", "gloss": "bone", "script": null},
            {"translit": "ostreon", "gloss": "oyster", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "osteo-", "gloss": null, "script": null},
            {"translit": "oyster", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ôus 1, Au 1, Aus 1",
        "lang": "Indo-European",
        "refs": "POK:78,785; KLN:126,494",
        "gloss": "ear"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:78; HRN:8; KLN:126",
          "words": [
            {"translit": "aviš, avišiya", "gloss": "heard, known, clear", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "âškâr", "gloss": "clear, obvious", "script": "آشکار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:785",
          "words": [
            {"translit": "ŭši", "gloss": "two ears, intelligence, mortal life", "script": null},
            {"translit": "ŭši-dâta", "gloss": "intelligent", "script": null, "see": ["Dô 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "POK:785",
          "words": [
            {"translit": "hŭš 1", "gloss": "intelligence", "script": "هوش ۱"},
            {"translit": "hŭšyâr", "gloss": "intelligent", "script": "هوشیار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Avestan",
          "refs": "BQT:178; FSF:51",
          "words": [
            {"translit": "an-aoša", "gloss": "without a mortal life", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": "BQT:178",
          "words": [
            {"translit": "anôšak", "gloss": "eternal life", "script": null},
            {"translit": "anôšak-ruvân", "gloss": "with eternal spirit", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:178; FSF:51",
          "words": [
            {"translit": "anušeh", "gloss": "eternal, happiness, wine", "script": "انوشه"},
            {"translit": "Anošîravân", "gloss": "\"with eternal spirit\"", "script": "انوشیروان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بدو گفت پیران که ای شهریار - انوشـه بُدی تا بود روزگار",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "Persian",
          "refs": "ARM:206; HRN:30",
          "words": [
            {"translit": "nŭš", "gloss": "drink (for eternal life)", "script": "نوش"},
            {"translit": "nŭšîn", "gloss": "sweet drink", "script": "نوشین"},
            {"translit": "nŭšîdan", "gloss": "to drink", "script": "نوشیدن"}
          ],
          "script_extra": "نوشدارو، نوشابه",
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T20:16:32.191Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:16:32.233Z] TOOL RESULT

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


## [2026-09-07T20:17:12.091Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','SYN','KLN','BQT','HRN','MON','TZF','SOD','AHD','FSF','ARM','BRT','PHD','NYB','HUB','ARY','CHEUNG','WLD','IEC']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\"",
 "description": "Look up reference metadata"
}
```


### [2026-09-07T20:17:14.408Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadable without login."}
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page 
== ARM {"title": "A. Aryan, Farhang-e Vazheha-ye Hamanand: Armani–Avestai–Pahlavi–Farsi, vol. I (آ), Bonyad-e Neyshabur 1363/1984", "kind": "login_required", "url": "https://ketabnak.com/book/132355 (vol.1 آ) — free registration", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: digitised on ketabnak behind a free account. Not downloaded."}
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== CHEUNG MISSING
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
```


## [2026-09-07T20:17:17.944Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T20:17:17.990Z] TOOL RESULT

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


## [2026-09-07T20:17:24.512Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ost(h)\" POK_03.txt POK_full.txt | head -20; echo ---; grep -n \"ōus-\\|ous-, \\|Ohr\" POK_03.txt | head -30",
 "description": "Grep Pokorny for ost- and ous-"
}
```


### [2026-09-07T20:17:24.571Z] TOOL RESULT

```
POK_03.txt:197:.f(^h)-',  ost{h)i\  ost(h)r(g),  obl.  ost (^h) - (e) n-  , Knochen';  ost(b)eion ^Beinernes^ Ai.  dsthi  n.,  Gen.  asth-n-dh  ,Bein,  Knochen',  av.  ast-^  asti-  n.  ,Knochen', Q-en.  PI-  asfqm,  Instr.  PL  azdbls,  asti-aojah-  , Knochenkraft',  astdn-tät  ,Lebens- kraft';  päli  atthitaco  , Krebs'  {*asthi-tvacas  , knochenhäutig',  vgl.  zur  Bed. o-r.  <3ö'TCfxdg  , Meerkrebs');  gr.  dazsov  , Knochen'  (wohl  *oo-T6Vo>'  ,*Beinernes' =  lat.  osseum  ds.),  lat.  ossu,  ossua  wohl  als  Neuerung  nach  genu^  genua ; dötay-og  (heilenist.  zu  ä(jTay,6g  assimil.)  ,Meerkrebs'  aus  ^oax-xfavio-  , dessen Haut  Knochen  sind',  woneben  vom  r-St.  HoTga-nov  ,harte  Schale,  Scherbe', UffTQSOv  , Auster'  (wohl  auch  öafQvg,  daxqva^  öaTQvtq  ,Baum  mit  hartem, weißem  Holz'  durch  Dissimil.  aus  ^öaiQO-dQvg)^  dargayalog  , Knöchel'  (assimil. aus  ^dargayaloQ]  setzt  einen  Nom.  *ost{h)Yg  voraus);  wenat.  ostüakon ^ossuärium^;
POK_full.txt:7171:See also: s. ost(h)-. 
POK_full.txt:64241:Root /lemma: ost(h)-\ ost(h)i, ost(h)r(g), obi. ost(h)-(e)n- 
POK_full.txt:64383:See also: whether here Old Irish odb'kv\o\:, under S. 783 {ost(h)-)l 
---
80:Lok.  PL),  Gen.  Sg.  aks-n-dh  usw.,  Nom.  Du.  aksi  =  av.  ah  ,die  (beiden)  "^^ Augen'  (vgl.  *ofö-  ds.  in  lit.  aH,  abg.  o<fz  und  als  Grundlage  von  arm.  ac-i^  _ und  gi\  liaas),  Bildung  vom  kons.  St.  *aks-]  dieser  St.  ahs-  auch  in  ved.  an-"(ijb  r ,blind';   av.  rtsi   für  *axn  nach  wsi  ,Ohren',   vgl.  av.  aiwy-äxsayeinti  ,sie beaufsichtigen',  aiwyäxstar-  , Aufseher' ;  redupl.  ai.  iJcsate  ,sieht'  (idg.  *iiu, aus  *i-oÄ;^);  aksd-   m.  , Würfel',   d.  i.   ,mit  Augen  versehen';  ksana-  m.  n. , Augenblick'   (scheint  aus  einem   Lok.   *[a]ksdn  erwachsen);    nicht   über- gewuchert ist  der  /)-St.  in  die  verdunkelten  Komposita  ai.  prdtika-  ,zuge- wandt,   entgegengesetzt',  n.  , Antlitz'  (:  nQoa-tjnov),   dnlka-   n.  ,das  Zuge- kehrte, Vorderseite',  av.  ainlka-  m.  ,Antlitz'  (*proti,  '^eni  +  ^fc"- ;  vgl.  slav. nich  unter  *m-  ,nieder'),  ghrtäcl  f.  ,fettig  (aussehend) ;    Opferlöffel',  svitid f.  ,glänzend';
82:gr.  öWfi  Nom.  Du.  , Augen'  (*ok^ie  für  *ote),  att.  *5V2r£,  wovon  TQLOTzig^ jHalsschmuck  mit  drei  gläsernen  Augen';  HoGoi-iaL  ,sehe  (geistig),  ahne', att.  ÖTTsvofiaL  ,ahne,  fürchte';  oipo(j,aL  ,ich  werde  sehen',  hjtwna  ,habe gesehen' ;  ÖTtiJtsvo)  ,gaffe  nach',  TtaQd^svoniTtrjg  ,Mädchengaffer'  mit  redupliz. Wurzel  Ö7t  (i-^07t>  Irt-) ;  h^iixa  ,Auge'  {*ä7t-(.in)j  dg)-d-al-(j,ög  , Auge'  (*ok^ph' mit  expressiver  Aspirata?);  ohne  Aspirata  böot.  oyiTaXXog]  mit  (nach ÖTtög  usw.)  analogischem  ft:  lak.  önTiXog,  epidaur.  dfTTiAAog;  ähnlich  ver- hält sich  5xxov  d(pd^alfj.6v  zu  lesb.  OTtTtccra  ^^^ixiiaxa''  (wohl  mit  expressiver Geminata);  dni]  , Lücke,  Öffnung'  (ivöftai  f.  PL  , Ohrringe'  u.  dgl.,  noXv- ü)7t6g  ,Netze  mit  vielen  Öffnungen  oder  Maschen');  dehnstufig  ^?//  , Gesicht'; TtQÖaajnov  ,  Antlitz',  ^irwrcov  , Stirn',  KvyX-o}1jj,  ßo-wrtLg  u.  dgl. ;  fiv-wrp  ,kurz- sichtig' ;  daneben  ald-oxp  u.  dgl.  mit  Kürze  (vergleichbar  lat.  atr-öx,  fer-öx) ; vielleicht  gr.  hnig  ,ehrfürchtige  Scheu;  Strafe,  Vergeltung',  eig.  ,animad- versio'?;  iipao  ,du  hast  zurechtgewiesen,  bestraft',  iv-LTtrj  ,tadelnde,  rügende Anrede',  ividacj  (geneuert  ivtTttto),  Aor.  ijvtTtanov  und  ivennov  ,tadeln, rügen,  ahnden,  tätlich  zurechtweisen'  (idg.  *lk'^-  aus  redupl.  *i-ok]^j  vgl.  ai. iksate) ;
89:verkürztem  Präfix);  daneben  germ.  *awn- (*oÄ:"-en-);  durch  Ausgleich  und "Einfluß  von  *ausö  ,Ohr'  entstand  ein  St.  *au^an- :  krimgot.  PL  oeghene (gß  =  ö),  dann  got.  augöy  aisl.  auga^  ahd.  ouga,  ags.  eage  n.  ,Auge' ;  St. *auqj(^-  ir^  S^^'  and-augi  n.  , Antlitz*,  ags.  and-eages,  amd.  and-ouge  , ange- sichts', aisl.  -eygr,  ahd.  -ougi,  ags.  -eaged  ,-äugig* ;
228:2.  ous-  :  9US- :  us~  ,Ohr',  erweitert  mit  -i  (pusi-s),  -es  (qusos-  n.)  und  -en.
229:Av.  usi  Nom.  Du.  ,die  beiden  Ohren,  Verstand,  Sinn',  Instr.  Du.  usi-hya, npers.  hos  (iran.  *au§-)  ,Ohr';
230:arm.  unlcn  ,Ohr'  (*us-on-ko-m)  •  das  kn  nach  akn  ,Auge';
231:gr.  dor.  (bg  (*öus)  ,Ohr';  öu  auch  in  öjJ^ara  , Ohren'  Alkm.,  äficp-wsg Theokr.  ,mit  zwei  Henkeln',  dor.  i^-wßddia  , Ohrringe',  vTtsQ-cbirj  , Gaumen', att.  lay-cbg,  hom.  lay-coog  n.  ,Hase'  (*sbg-öusos)  ,mit  schlaffen  Ohren'; 3US-  in  gr.  lak.  a'ög  ,Ohr',  PI.  äavd-a  {^ava-avd-a)  Alkm.,  tarent.  äxa (*av(jara)]  ion.  rtaQ-rj'ioVj  att.  Ttcco-sla^  lesb.  Ttaq-ava  , Schläfe'  (:  air.  arae)-^ gr.  ous-  (Kreuzung  des  nominativischen  öus-  mit  dus-)  in  att.  oi)g  (*odaog) ,Ohr*,  hom.  Gen.  o^axog  {*ova'i}Tog),  (bytlösg  , Ohrringe'  Hes.  (*ous-n-ko-)'^ über  dy.ova)  s.  oben  S.  18,  587 ;  über  att.  dyLgcaad-ai  {*a'/.Q-ovg-)  s.  Schwyzer Gr.  Gr.  1,  348;
232:alb.  vesh  m.  ,Ohr'  (*öms-,  ös-);
233:lat.  auris  f.  ,Ohr'  (*ausi-s)'j  aus-cultö  ,horche'  s.  oben  S.  552;
234:air.  äw,  ö  n.  ,Ohr'  (^*dusos-)'^  air.  arae  m.  , Schläfe'  {*par-ausios)f  Plur. im  ON  Arai-,  gall.  ON  ilrawsiö  ,Orange'  (Thurneysen  KZ.  59,  12);  PN Su-ausiä  L  ,mit  schönen  Ohren';
235:got.  ausö  n.  ,Ohr'  (germ.  *ausan-) ;  mit  gramm.  Wechsel  (*auzan-) : aisl.  eyra,  ags.  eare,  afries.  are^  as.  ahd.  öra  n.  ,Ohr';  davon  ahd.  ö7'i, mhd.  CBre  ,ÖÄr' ;
236:lit.  ausis  f.  (älter  auch  m.),  Gen.  PI.  ausy,  (konson.  St.),  lett.  äuss  f. ; apr.  Akk.  PI.  aus  ins  ,die  Ohren',  daneben  ausins  Vok.  m. ;
1936:gr.  eiQo)  {*serio)  , reihe  aneinander'  (hom.  nur  Partiz.  Perf.  iegf^svog, 3.  Sg.  Plusqpf.  £€QTo)j  ivsiQü)  ,knüpfe  an,  reihe  an'  (:  lat.  in-serö  ,füge  ein'), sysQff ig  , das  Hineinfügen,  Hineinstecken'  (:  lat.  insertiö]  ti-St.  auch  in  prae- sertim  ,in  erster  Reihe,  vorzugsweise'),  €Qi,ia  n.  , Ohrgehänge',  Sgi-iog  m. ,Halskette*,  ÖQ^la  f.  , Angelschnur',  ögfia&ög  m.  , Reihe,  Kette',  vermutlich auch  eTgegov  ,in  Gefangenschaft';
2568:Ai.  skäu-ti,  skunäti,  skunöti  ,stört,  stöbert,  stochert^,  mit  ä-  ,zerkleinert durch  Stochern ;  macht  Einschnitte  (in  die  Ohren  von  Tieren)^,  ava-skaxt^. m.   ,ein   Wurm',   ni-skdvam    , zerfetzend',    cö-skü-yäts   ,scharrt    zusammen».
2655:[*slegö),  aXXrjy,Tog  (*gX-)  , unaufhörlich',  Xay&ooai'  dcpsTvat  Hes., 'chlaff,  schmächtig,  dünn^,  hom.  laycoög,  ion.  Xayög,  att.  Xaycog,  -d) 's)ldg-öusos  ,mit  schlaffen  Ohren*),  Xaywv,  -ovog  gewöhnlich  PI. Jien,  Dünnen'  (formell  =  aisl.  Uiki  , Faltmagen'),  Xdyavov  , dünner ichen*  (formell  =  as.  laJcan  usw.  ,Tuch'),  XfxjydvLOv  , Wamme'  (vgl. iöJca  , schlaff  herabhängen'),  nasaliert  vermutlich  hierher  Xayycc^co Xayychv  , Zaudern',  Xayysvai '  cpevyat  Hes.  (*,matt  sein,  schlaff  und ^  sein') ;   mit   der   Bedeutung  ,Tvollüstig' :  Xdyvog  ,geil',  Xayvsveiv
3124:1.  Anlaut  sp:  air.  sine  m.  , Zitze':  hö  tri-phne  =  hö  tri  sine  ,Kuh  mit drei  Zitzen',  mir.  sine  Seäin  ,uvula*;  aisl.  speni  m.  , Zitze,  Brustwarze* (aschwed.  spini  auch  , Zäpfchen  im  Halse'),  mnd.  spene  ds. ;  o-stufig  a«. Spane,  spanu  f.  ,Brustwarze*,  spanan  , entwöhnen';  mhd.  spen  f.  ,Bruat| Muttermilch*  (wohl  *spani'^  vgl.  nhd.  Span-ferJcel) ;  reduktionsstufig  mnd. spone  f.,  ahd.  spunni,  mhd.  spünne  und  spune  ,Brustwarze' ;  lit.  spen^t , Zitze,  Zäpfchen  im  Halse,  Ohrläppchen',  apr.  spenis  , Zitze*.
3857:Gr.  TQitwj  thqiya  ,zirpe,  schwirre,  knirsche',  Tqiyiidg  (neugebild oii6q)  m.  ,das  Zirpen,  Schwirren',  TQtylrj  , Seebarbe',  TgiyöXag  ,Knurrbll9- arglyS,  -yyög  f.,  auch  ct^i^,  (ttAi?;  atqlyXoq  Hes.  ,ein  Nachtvogel',: J*' strlx,  -gis  f.  , Ohreule',   strid{e)ö,  -ere,  strldl  ,zischen,  schwirren,  schrägt
4543:toch.  AB  tsärk-  ,quälen*,  A  tark-  , Ohrring',  B  tärk-  ,drehen'.
```


## [2026-09-07T20:17:25.690Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aoša\\|anaoša\\|an-aoša\" BRT.txt | head -40",
 "description": "Grep Bartholomae for aosa"
}
```


### [2026-09-07T20:17:25.736Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:17:36.615Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['POK_03.txt']:\n    txt=open(f,encoding='utf-8',errors='replace').read()\n    pages=txt.split('\\f')\n    for i,p in enumerate(pages):\n        if 'ost(h)-' in p and 'Knochen' in p:\n            print(f,'leaf',i,'ost(h)- page?',repr(p[:200]))\n        if '2.  ous-' in p or 'ous-  :' in p:\n            print(f,'leaf',i,'ous-',repr(p[:200]))\nEOF",
 "description": "Locate Pokorny leaves"
}
```


## [2026-09-07T20:17:37.520Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aos\" BRT.txt | head -50",
 "description": "Grep BRT for aos"
}
```


### [2026-09-07T20:17:37.946Z] TOOL RESULT

```
POK_03.txt leaf 18 ous- "Nachbildung  von  palam,  dam  aus  *co-öro- ,vor  dem  Angesicht  befindlich';  aureae  {öreae)  ,Gebiß  am  Zaum^  davon auriga  {öriga)  ,Wagenlenker'  {-igä  zu  agö)-  ösculum  ,Kuß'  ist  Demin."
```


### [2026-09-07T20:17:37.994Z] TOOL RESULT

```
190:Die  angeführten  Texte  bringen  ausserordentlich  zahlreiche  Wiederholungen. Und  zwar  sind  entweder  zwei  oder  mehr  Stellen  einander  völlig  gleich  oder  sie unterscheiden  sich  nur  in  untergeordneten  —  d.  h.  für  das  Wörterbuch  wenigstens untei^e ordneten  —  Stücken.  Als  Beispiel  für  die  erste  Art  von  Wiederholungen mögen  dienen:  Y.  65.  2-5  —  Yt.  3.  2-5;  Yt.  5.  10  =  12,  14,  16,  20  (usw.);  Yt. 5. 19  =  23,  27,  35,  39  (usw.);  Yt.  JO.  98  =  135;  Yt.  j^.  15  (von  hü  bis  taxmahe')  ^ Yt.  10.  70,  127;  Y.  57.  25  (von  akeca  an)  —  Yt.  10.  93  usw.  —  Die  Wiederholungen der  zweiten  Art  zerfallen  in  verschiedene  Gruppen:  Yt io.  103  wiederholt  sich  von yS  hantaia  an  wörtlich  in  Y.57.  isfl,  nur  dass  hier  das  ca  hinter  har>ta  fehlt; irgend  ein  Grund  für  die  Abweichung  ist  nicht  vorhanden.  Yt. /o.  94  (^=  114I und  Y.57. 26  stimmen  völlig  lusammen,  nur  dass  auf  die  Eingangsworte  aäa  nS tum  dort  der  Vokativ  mikira  vouru.gaoyaoite,  hier  aber  traosa  afya  huraöha  folgt; die  Gebetsformel  ist  die  selbe,  aber  die  Adresse  ist  verschieden.  Ähnlich  steht es  mit  den  vier  in  Yljo.  igof.  enthaltenen  Stücken,  die  von  vier  Waffenarten Mihras  durchaus  das  Gleiche  aussagen;  nur  eben  die  Namen  der  Waffe,  sowie deren  Beiwörter  machen  die  Verschiedenheit  der  Stücke  aus.  Besonders  zahlreich findet  sich  diese  Art  der  Wiederholung  im  Viälvdäi  {Vendidad);  z.B.  unterscheiden sich  in  dem  Kapitel  über  die  Verträge  (V.  4)  die  Abschnitte  6  bis  10  und  ander- seits II  bis  16  nur  durch  den  Namen  des  Vertrags  und  der  Zahl  in  der  Buss- bestimmung. Femer  haben  V.p,  53,  54,  55  und  S7  '^'on  üäca  an  den  gleichen Wortlaut,  nur  dass  das  dreimalige  para  von  53  in  54  durch  kaha,  in  55  durch nöü,  in  57  durch  pascalta  ersetzt  ist  In  den  liturgischen  Teilen  des  Yasna  wieder sind  grosse  Stücke  bis  auf  die  Eingangs-  oder  Schlussformel  gleichlautend.  So decken  sich  Y,  i.  3  ff.  und  5.  5  ff.,  4. 8  ff.,  7.  5  ff.  vollständig  bis  auf  die  Eingangs- worte, die  zu  Y.  1:  nivaiöayemi  hankärayemi,  zu  Y.^:  äyese yeSH,  zu  Y.  4:  Hat  dis äva^ayamahl,  zu  Y.  7:  alaya  daöami  lauten,  während  anderseits  Y.  2.  äff.  und 6.\S.  nur  darin  auseinandergehen,  dass  hier  (Y.  6)  jeder  Abschnitt  mit  yatamatde endet,  dort  (Y.  4)  jeder  mit  ahmya  zaohre  bar>smanaica  eingeleitet  und  mit  äyese yeiti  geschlossen  wird.
2080:logie.     Göttingen  I902. (PtroMBtADEB  Djaos:  Dyius  Asnra,  Ahnra  Mazda  und  die  Aiurai.     Halle  1885. BSächsGW.:  Berichte  der  phiL-hiiL  Klasse  der  K.  SächsUcben  Gesellschaft  der  Wissentchaften. BSLP.:  Bulletin  de  la  Socijlj  de  Ijnguiitique.     Paris. Bim.:  CrkBaktholomak. AF.!  Arische  Forschungen.     Halle  1S82  ff. AirV.:  Das  altiraniiche  Verbum.     München  1878.
2127:1896. KZ.:  Zeitschrift  für  vergleichende  Sprachforschung.     Heraosgeg.  von  AKuhn  n.  A.     Gütersloh. (P)dbLagaede  Beitr.:  Beiträge  zur  baktrischen  Lexikographie.    Leipzig  18öS.
2135:G.:  The   five  Zoroastrion  GSthSs  wilh  the  Zend,   Pahlavi,    Sanskrit   and   Perüan  Text«    and Traoslations.   1-eipzig  1895. USL:  Htmoires  de  la  Socittj  de  Lingniitique.    Paris. MS.:  MaiiräyariiiamAiiä,
2200:Ad}.:  Adjekttv(um).  aosk. :  altoskisch.
2290:Kaos. :  Kauiativ(um).
2440:—  3)  aus  ar.  *a  'in'  [idg.  *ii,  der  antelton! Nullfonn    la  'm  in   gr.  i-tapt^   und  vlL manuve,  aosk.  AiirtiH;    s.  WSCHULZE  KZ. 164,  (emer  KZ.  34. 384  und  vonPlanta  OUD. 3.  III,   161  s);  —  3)  aus  ar.  'ü  'in,  bei'  (idg. *■  iaViX. raSh-Jt,  rahkesf,  s. Bgm. Grdr.' 2.619)''.
2470:—  dgL:  al/s  giuS  urvä  raostä  .  .  yüzim aiibyO  (yiimX. gaobyd)'''*  ..  aogS  data  Y.sp. 10;  —  spintä  ma'myS  .  .  xia'irä  .  .  vohü mananha  .  .  aHbyö  (AbL)  .  .  Y.  4!j.  6 ;  — yastat  mtzäim  Aan>ntl  nöit  däitl  yS  it ahmüi  3r7zux'iä  (sd.)  nä  däiti  Y.44-J9', — -  'ia/aAyä  mahränO  . .  ahyä  . .  Y.^2.14; 43-9, 49-1,2,^6.3, 40.  s';  — -ahurSmazdt'
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2514:-  g.  'a-  Pron,  ident.  'ich,  du,  er  selbst',  humata  'ta'  ..  aat  mam  narö  paskat  ya- nur  NS. :  yi  maibya  yaos  (sd.)  akmai  astu  g3„ie . .  "um  dieses  (deines)  guten  Denkens vakUta  mahyä  isfois  voha  eöihm  mananM  willen  .  ."  H.2.14''.        2)  substantivisch: ".  .  dem  verspreche   auch  ich  selber  das  ,  ^tai  ti  .  .  avayam  *danmaM  Y.  öS.  i  '>;  — beste  meines  Besitzes  durch  VM."  y.4''-   am  yasna  .  .  ''ta  patti    ava.jasa  .  .  aoi \Z;    —    ai   -3    vaocal  ahurö  mazda    ''da  zam  ".  .    um    dessentwülen  (was  hier  ge- sprach er  selbst,  ^/iM."  Y.sp.ö.  [schiebt)    komm  . ."  Yt. 5.132  (s.  i);   — zBed._s.  Gdn.  GIrPh.   '  52      Ich   '^'^^<=^'^^'- -faimat puir.lt  (sUtt  AS.)  Kimar^xsaf^u/ia dass  f.  as'  aus  einerrart.  idg.  'n  'selber  er-    ,    ,  ,   ,.,       .,•.,..'        ,     .  ,        „ wachsen  ist,  die  in  aUi;  (aus  'a-u-r,  wie , (sd-)    damit  (was  ich  dir  gebe)  such  ..' eJroiaus*jn-H-/°)steckl.Dochs.B(;M,GrGr.3244-    V.  1^.  14;  —  in  Kongruenz  mit  dem  Prae-
2538:\ ■  /i.  1 3 ;  1 4;  -  'ta  parayaUi  (sd.)  ya>a  ,  ^j^  j.^^^^,^j  ^^„ ^^^^  ^^„^^  pas«s.Aaur- N.2.  aart,  «^1^^/  als  Adv.  sbes.  [N.   ,4„,,j  .f^i  ^raos,^  . .  Pairi.barämaAi  \l.
2550:äJffj  ti  'take  paiti  ..  V.22.2f.;  —  Da.'  aoAvo  (Stvetx.)  yal  as/tainti  Y.i^.6  \isw.; in  Verbindung  mit  anya-  Du.  (s.  i  b):  —  'tagsam  sünam  ..yimpasuiJiaurvamca.. asUm^mastrrfttqm  vispacayö*>nastr?inqm  i  V./^J.S;  —  'farahqm  urvaranqm  yat  ätri.- amqsta  fsd.)  ''i^arö.cikaya  *°le  anye  cika- ■  ciirranqm  V,4',75;  —  'ttm  ratümca  .. yatö  "wenn  einer  ,  .  und  wenn  einer  ,  .  \yim  maiaydhanmaim  A.j.3(?).  b)  sub- vcrletzt,  so  sollen  sie  dies  und  jenes  . ."  stasA\v\&c\\- 'ta(^T>.)äb3r3ta*sraosiivariza F,_jc  b)  adjektivisch:  j'iT/fl/ire'a/ara.-  vicarayaDm  "die  beiden,  der  .^.  und  der iri^yeiti  kva  "tarn  xsapan»m  . .  *vanAaiti  Sr.  .  ."  N.  jcf ;  —  cval  'te  (ADn.)  stai- "wenn  ein  Gläubiger  stirbt,  wo  weilt  asi\tiüa  bar>iis^a  ..  nasus  .,  fräsnaoiti dem  Tä^  (des  Todes)  . ."  H.  2.  i;  — yö  "..  die  beiden,  das  Bett  und  das  Polster .." . .  upairi  kunanm  (sdL)  manö  baräi  i-up^m  V.  7.9;  — ■  azim  °ta  (APn.)  zaota  zlsJi  (sd.) 'tfm  paiti  zmämm  aUariin  uri'a  kllayäi  ..  /rasrao^r?mca  /ragl>r>mca  . .  Vr._j.7; (sd.)  "wenn  einer  . .,  so  . .  während  der  —  't^m  nitamim  As'>rjm  '^rivacahim  (sd.) ganzen  Zelt  (seiner  Cberhebung)  .  ."P.  "id  minimum  Aj^/um:  triverbe"  F.  27b; J7.  a)  wo    wir   'solch'   brauchen:  yö  —  haomü  kutö  .  .  ava    'te  ahuta  .  .  "ge-
2782:{upa  mit  Akic.);  para  n  *gaosp}nta  ...will,  cupiti  potens,  glücklich':  am^rstäiti baodasla  urvän^mca  */rai^ämahi  nazdista  '■  *asaonö  urvä  °sö  "in  Ewigkeit  (wird)  die upa  >war}sta  raoca  V.34.  [Seele    des  -4Aanhängers    glücklich    sein"
2823:—  W.(inN.rf9):  afurr  fa  iiÄa  hir  u  djlastia,   fdSt):  sraos?m..'mah£  xn-Ldraos  hamai-
2931:'b^eifeo,  verstehen  lernen':  ydäia  . . kliayeni  hutaosqm  . ,  yä  me  daüiqm  . , trmtat  (sd.)  däi  apica  aotät  Yt^.26.
2946:VgL  lit.  aüü  'dieSchnhe  aoszUhen'.  —  Pü. ;  mök, j.  ao%rm/ana  V.  8.  23:  lies  ä%r'.
2961:Ableit.  —  aL  •öiai-.  —  \g\.  aosa-.  —  Fü. :  öS. •  j.  aoäah'vant-  Adj,  (fem.  "vaiii-)  'dem
2969:fromme,  der  es  zuerst  gelehrt  hat,  dass  •  j.  aosta- m. 'Oberlippe',  Du. 'die  beiden
2979:•  j.   aos-  V.    sagen.      Praes.   2   aosa-.       \      Kindern),    die    als   -/«rHsches  Zeichen  ange- Nur  Med.  'sagen,    sprechen';    es  folgt  i     sehen  wurde.    S.  noch  No.  2.  —  D  rt..%  ,/«•
2980:dir.  Rede:  am»la  Sp?nta  <lfrä«W(3P.)  Vyt !  und  %ri'  nehme  ich  als  Namen  dreier Kürper- 4a;    ~   yö    hS    aosante  (3P.)   . .   FrW.  ,V.  1      »«»==    ";="=    ■'.^.''   ^en  Lippen   und  .  .  unii  .
2982:i(?).         a)  'sagen  ZU -'(Dat):  aal  aosele^     pi^Eri.  1  3)  S.  freilich  w.n.  Aiür.  /.  167. (3S.)sp?ntayäiärmaßt\.ifi.sj.     WYV\*  \-  ^°^^^'  ™-  'Unterlippe',    Du.  'beide eben  mit  -'  (Instr.):  aal  aoSde  haxa  haSa  I  j^^       ,.  ,^^  ^^^.  p_  ^  l
2993:KompE.;    AMeit.  —  Vgl.  aosah-,  —   Eig.  (2)  j.  aui  bansen  N.  gS:  lies  or'ÄÄflr.urti.
3003:—  at  ..  dr?grai5  akäU  ^arihäii  (sd.)  •  j-  aka'tara-  Adj.  '(der  bösere,)  beson- paitiurvanöpaityeintl\.40-i\.  a)mitjders,  überaus  böse  (in  Wille  und  Tat) DaL  'Jmdm.  (gegenüber)  böse  (in  Wille  gegenüber-'  (Gen.)":  mtirim  ..  kam}- und  Tat)"':  tum  -kö  rahislasla  mi^ra  rs'.ö.jamm  daevanam  'nm  sraosyanqm ahi  masyJkaHbyS  "du  bist  (je  nachdem)  "■  ■  der  denen  überaus  böse  ist,  die  sich böse  und  (auch)  sehr  gut  gegenüber  den ,  strafbar  machen  .  ."  Yt.  10. 26. Menschen,  a  M»  Yt. /o.agijg;  — oiS«/«|  "  ^e'-  '"*"■  «■  F»Isch  KZ.  jo.  517. klil  {hd.)  aahat  ..  -kb  dngväitl  Y.47.  •  j-  aka'tas-  m.  Name  emes  Daiva: A)   in    religiös-moralischem    Sinn:  °tahm  daium  Y. 10.13,  '5  43-
3026:manaKiAa  Y.iff.^.  \naos  apazaäauhö  •wya  {GSf.y*  "..  in  der
3091:PPfP.  lum  V.  gaos:  —  Vi.:  a^ösT/är.  — •)  FbIscIi  S  5S-  '■
3148:PPfP.  einer  Basis  jJJJfl'j-,  s-  Erneilcrung (/-Aorist,  vgl.  xlnaosta,  xiiiaosiii)  des  \'.  ilnav-. —  VgL  axsaüla-.
3165:■übelste,  böseste"*:  dva  yaska..  -«(NDm.) I  V.  7. 70;  —  sHptibyasca  (sd.) . .  vispalibyasLa pairi  'taeibyö  \.  14.17;  —  °to«  rfuirfw- Aavö  'P.14;  —  nöil  hl . .  bvat  . .  zahistiJ anhuL.bi'ai  TTspariqm  *°/jm'^  *paosisl>mcix ya^  »riyat  daozaishum'^ . .  sondern  es  wird
3375:Satz:  aat  may^m  ava  kanöil  . .  paiti  dim abarBil  ''^a  ''imqm  vacS  framruyä  V.J7. S;  5.12,  27,  29;  — yö ..varasasca  *Aqm.- razayäte  . ,  '^5«  dim  *upa.taosayeiti  . .  raS- sayaca  (sd.)  V.  !■].  a.  5)  den  Nachsatz
3449:•  j.,  g.  at-ct,  j.  a«!-£a  '*  Pait.,  an  der  Spitze des  Satz(teil)es  und  Versgliedes,  'und  dann, und';  zur  Anknüpfung  i)  eines  Satzes:  atcä gSui  urvä  raostä  (sd.)  Y.  2rf.  9;  30. 9,  34. 2,  43.1,  4g.z,  S3-  2.  7;  —  y^  asim^m  . .
3493:•  j.  apaosB-m.  Name  eines  Z>ii^'a*\  beson- ders des  Gegners  des  Tisiry a  {sd.):  a  dim (näml.  tistrim)  paiti.yas  nizdvaraiti  dalvd yö  °sö  aspake  k)hrpa  sämake  Yt.  tV.  21; 22';  —  ä  dim  bavaiti  aiwi.vanya  tistryö . .  daFnm  yim  °S>m  Yt  <.V.  28;  —  tauna- yeiti  dalum  "sjm  Yt  /Ä  2;  6.
3508:•  j.  apa-j-zära-  m.  'Abfluss,  {Wasser)ab- zwejgung'  a)  des  VouruAasa:  srayä  vouru.- kasaya  .  .  yeäke  . .  Aazannm  -ranam  . . kasal  aSsqm  °ranqm  c(&war>.sat»m  ayan.- baranqm..*arihas(a  me  *afi:aAka  Spö 'rö *vt)asaiti  vispJis  aoi  karsvqn  Y.  65.  4  £; —  aija  käu  'rö  bvat  zrayanAs  vouru.- kaiahe  vairil  yH  Aaosravä  nqma  Yt  ig. 56;  —  zrayauhs  vouru.kasahe  ,  .  vTspJ rairi/  a^araiti  vlsp}sca..nimraoi!  vlspSsca srlr!  'äire (AP.)'> \i.8.i,f>;~ katiht kaüht •,lire(XS.)  Ytj.ioi.  b)  der  Ratfka:\ tipa  guoim  'r>m  ra»hayh  Yt/5. 27,  j
3510:•  j.  apajcraosaka-  Adj.  'schmähsUchtig' : nivayaka  mpalnaka  apa.skaraka  'ia(NP.) ima  paiti.vJsfTUe  Yt5.95.
3511:Ableit.  ins  ^apajrattsa-  m.,  zum  V.  xraos-.  — ■i.  vgL   aptirBSa-  m.  'Schmätiung'.
3622:•  j.  apa.skaraka-  Adj.  'hohnsüchtig,  höh- nisch': nivßyaka  nipasnaka  °^a{NP.)  apa.- xraosaka  imä  paifi.vlsmte  Yt.  5.95.
3817:•  j.  aiwi.ta£ina-  i)  Adj.  'heranlaufend, anspringend'  zur  Begattung,  vom  Kamel- hengst:  ustrake  vmairyaos  ,  .  °naAi  Yt 14.11.  i)  n.  'Herzulauf,  Anlauf  (nur Komp.).
3844:•  j.  aiwi.druxUm  Absol.  ">  'unter  Belügen, Betrügen  von  — '  (Gen.):  rasnaosÜd  paiti.- sat»h>m  mi'iraAeca  aiwtjiruxtim  "indem er  dem  R.  widerspricht  und  den  M.  be- trügt" V.^S4-
3906:Ableit.  aus  'atiourii^rima.  (mit  Verschiebung des  Ilanpttons ?).  —  Pü,;  traosskr.  —  ')  Hds. '%r>ni  ananifm;  s.  %  40g.
4085:•  j.  ^afsmaimv^  Adv.  'verszeilenweise' : iraosim  . .  yS  paoirys  ga^a  frasrävayat . . *a/s°'''  vacastastivat  ".  .  der  zuerst  die Gäha&  rezitirte  .  .  verszeilen-,  strophen- weise" Y.  57.8; — yä  gäiä  *a/s''^  sräva- yatö  uva  ratufris  (statt  ND.)  vacattaSHvat *srävayatS  aSavatö  katarascit ,.  N.  2J;  — ys  yasrum  *yasmti  *aft°  -ö  va  vacoitaitivai va  nva  ratufrya  N.  24;  —  yat  kakat *'amrutS  ^'vanca'''^  *valastastivaüa ..  N.24.
4127:|(ADf.)  äpa  urvaire  Y.5.4;  Yt  79.32. *kaasimna-,  PPM.  lu  *haosa;  Praes.  2.  —  Vgl aL  iüfyati  'er  vertrocknet',  np.  sSüdan  'ver- dorrt sein',  gr.  aIo(.  —  Vgl.  huska-.  —  Pü. : undeutl.,  dazu  die  Erl.:  an  i  ne  afiäyojl  Ausk ne  Ausi;  SQ. :  aSaft.  —  »  Zu  Yt.  1$.  16  fälsch- lich aai/iis',  s.  S  26S.  57.
4181:^ustraAit  .  .  °yaos  osaHnarthü  Y.  24-  St  ^^■
4209:I  wo  ? :  äat  aosete  haxa  hasa  "a  barnzis '\sayamnanqm  W.  iS.26.  2)    mit    Instr,
4221:—  ■vakisUm  %tt)ä  .  .  yasä  .  .  prasaostrsi maibyäcä  yaiibyascä  .  .  'nüis^^  vä  »Bit .  .
4277:•  j.  an-aiwi.^ratvö.gätav-  Adj.  'der keinen  bestimmt  angewiesenen,  festen  Platz hat':  "'tu'''  (NDm.)  aita  äb^rtta  ^sraosa- vanza**  vlcarayahin  "ohne  festen  Platz sind  die  beiden:  der  Ab.  und  der  Sr.;  sie gehen  auf  und  ab"  N.  717.
4300:•  j.  an-aiwi'ätay-,  an-aivi'ätay-"  f.  1) 'NichtStudium,  Unterlassen  des  Studiums'; yS  asrut^aosB  vä  a/ravaocS  vä  neit  lim afum  vääm  *aiwyas  tisit  *paslalta  'viM astryeili  yezi  dal  *öyum.pe  *v3am  *aiwyäs "wuti  ästryäti  "wenn  einer,  weil  er  taub ist  oder  stumm,  auch  nicht  ein  einziges Wort  lesen  kann,  dann  macht  er  sich durch  NichtStudium  nicht  sündig;  wenn er  aber  auch  nur  ein  einziges  Wort  lesen kann,  so  macht  er  sich  durch  NichtStudium sündig"  N.  i4;  — y5  .  .  nSii  aiwyästi  (sd.)
4376:•  j.  an-aSavan-  Adj.  'nicht  rechtgläubig, ungläubig,  glaubensfeindlich' :  vTsße  asraosö yS  'Sai'anö  (NP.)  vlspe  'iavanS  yS  tanu,- p>r?%B  \.  16.18;  —  zao/a  'sava  adahmd atanu.mO^rd  Yi.  yo.  138.  a)  sonst  von as^maaya-  (sd,  auch  fdSt.):  "sava,  -saonS (GS-),  'saonqm.        [N.  lOg:  lies  asavanim^
4570:—  vjfTirayru/m  ..yat  asti  °rf  ahutia  airya- mana  ". .  zwischen  dem  A/i.-  und  dem  Airy.- Gebet"  Vr.  24-i;  —  ''v  *am7sSsi!a  spmts saosyantasca  P.^f;^o,_ji(?);  —  'n  pitan i^A.)  puknmla  Yt.J0.117;  117,  116^;  — ' 'n  urvaitya  (sd.)  V.4-3— 4*;  —  ävis  iiä. "rs  hsiiiü . . rätttyl(%d.)  '^■33-T,  —  cvai  'rj *mr3us. .  "wie  viel  im  Kreis  der  Männer . ." V.5.27;  —  yim  'r»  vastnm  frajasäi  (sd.) 'V.i0.i6;i6;yd.ij.i4.  aa) unräumlich: ; \'it/iaiy()xsäydi^iyä  agarbäyam  "rimä  haina-  \ raim  "diese  9  Könige  nahm  ich  in  diesen Schlachten  gefangen"  Bh.  4. 3.  ß)  zeit-  j lieh:  *kva  altqm^aEsnmn  paiH.barat1  "r?, akuna  *airyamana  "wann  soll  man  das  1 Brennholz  herzubringen?  Zwischen  (der  | Rezitation)  des  Ah.-  und  des  .,4»>/, -Gebets"  |
4632:pataha  yat  'n  vä  aai  -w  v,l  .  ."  N. S3.  2)  Praen.  a)  mit  Akk.  'innerhalb, in,  unter,  zwischen';  a)  räumlich,  auf  die Frage  wo?  und  wohin?:  i  °r  tmä  äahyäve^ martiya''  kyi^  . .  "innerhalb  dieser  Län- der . ."  Bh.  /.  8 ;  —  I  avaiy  °r ''  didsm  frii- Aayam  {sd.)  Bh.  2, 13;  —  T;/  ja/W  (sd-) var?zäne  V.ij.iy;  —  'rt  daifiAu  pi}p?r?- tane  Yt  70.8,  J5.49;  49';  —  yS  vJräsaili 'r)  räiia  rJsmana  Yt.  7^47;  —  tiisiltm (sd.)  yim  'rp  mSurunua  büx'aimca  V.  /.  7 ; ■ —  yßi  'r)  v^rxika  *as  *mars}a  (sd.)  V. j8.  70  PüZ.;  —  'rj  sqm  asmanimca  "zwi- schen Himmel  und  'Erde"  Y.6Ä  15;  Yt. ÄS,  /O.95,  y,i3',  43,  44; — hax3or)mia , .  'n  mäti/Dtnla  Avan^a  Yt  ö.  5 ;  —  ..  */ra- hinein  (sd.)  *'r?i'>  airsatca  bammaca  H.öS; —  Vii^raymm ..yat  asH  "n  ahuna  atrya- mana  ". .  zwischen  dem  AA.-  und  dem  Airy.- Gebet"  Vr.  24.1, ;  —  -/-j  ''am?sSsca  spnitS saosyaiitas^a  P.3<i,30,ji{?);  —  'rv  pitan {zd.)  puhnmca  Yt. /0.117;  117,  116';  — °r>  urvaitya  (sd.)  ^",4.3—4*;  —  ävis  tui 'rs  Asnta . . rä/ayy(sd.)  Y._J3.7;  —  ä'at 'r.> *ii?rsus. .  "wie  viel  im  Kreis  der  Männer . ." V.5.27; — yim  'n  vastmii  fraJasäHsd.) V.j6'.i6ji6;Vd.y./4.  aa)  unräumlich: \'h/iaiyiixsilyahiyJ  agarbäyam  °r  ima  Aattia- rana  "diese  9  Könige  nahm  ich  in  diesen Schlachten  gefangen"  Bh.  4. 3,  ß)  zeit- hch:  *kva  aitqm  *agsm3m  paiti.barälf  °r) oAuna  ''airyamana  "wann  soll  man  das Brennholz  herzubringen?  Zwischen  (der Rezitation)  des  AA.-  und  des  ^;>f', -Gebets"  I
4656:—  ")  Pü. :  w  ^11  afar  an  l  hal  smäk  äiät em.  Der  Artikel  erscheint  hier  auflallig.  — ")  Pü.;  ÖB  7  nivän  i  apärlk  ias.  —  <J)  Wie ai.  anyä;  gr.  oKko^  und  lat.  alius.  Wir  müssen in  der  Obersetiiing  'anderseits;  ebenso'  ndgl. verwenden.  Vgl.  noch  No.  14  f.  —  14)  Der Za^lar  und  die  Ralav  singen  lusammen  die Liturgie  im  Wechselgesang.  —  'i>  Genau  wäre saosyantö  statt  haiayö.
4755:—  vTspe  vS  '/a  spmta  staota  zaota  .  .yüS- makim  yasnäica  . .  yat  'lanqm  spmianqm Vr.5.1;  2/,2,Y./2.i',  52.4,  Yt_).3,  4!.if.^ V-p:.i2,4ß,  *Vd.20,  V.  12,2;  —  äat  mraot ahurS  maeda:  ahmakim  tiqma  yat  'fanqm ipgntanqm  .  .  Yt  7.  3 ;  j.  i,  FrW.  /.  2 ;  — yB  nä  ..  kasiitam  . .  fräyatät  (sd.)  *ahma *yq  'i^  sp^tiO  Yt. /.24;  —  vaim  ySi  °s'ä sp»nta  Vyt.^js;  —  '^qsüa  sp^nta  saosyan- lascä  Y.  13.  3 ;  Vr.  3. 5  (wo  -J^sca),  P.  36 C'Si/a),  Vr.22.i,Vt//.i7;  —  sil  sp^nta dame  mäzdayasne..  tadhrasca  Y.  A3;  — kvanca  (sd.)  °sS  sp>nisYT,  ig.  2.  a)  bes. neben  AkM.  genannt:  a^m  ..  durfiianm ahurahe  mazää  x'aT^Aartm  'sanqm  spmta-
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['s'a  spunta  Yt.Ä 38  ist  Einschiebsel,  s.  an-  No.  3.]
```


## [2026-09-07T20:17:49.584Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aosa-\\|aoSa-\\|aosah\" BRT.txt | head -20",
 "description": "Grep BRT for aosa-"
}
```


### [2026-09-07T20:17:49.631Z] TOOL RESULT

```
2937:•  j.  aoSa-  m.  'Quelle"',  nur  in  upa  'liailu raahaya  (sd.)  "an  der  Quelle  der  R": yatäl  ahi  upa  'laf^u  ranhayh  . .  upa sanaie{sd.)  ratahaya  Yt  J2.  i8£  a)  als Name  eines  Landes*':  x^asJasam  asav- hqmHa  ..  frä^w^rmm  ..  upa  '%al^  raa- hayä  yö  asarB  (sd.)  atwyaxiayänti  " . .  schuf ich  (das  Land)   UAR. . ."  V./.19.
2961:Ableit.  —  aL  •öiai-.  —  \g\.  aosa-.  —  Fü. :  öS. •  j.  aoäah'vant-  Adj,  (fem.  "vaiii-)  'dem
2979:•  j.   aos-  V.    sagen.      Praes.   2   aosa-.       \      Kindern),    die    als   -/«rHsches  Zeichen  ange- Nur  Med.  'sagen,    sprechen';    es  folgt  i     sehen  wurde.    S.  noch  No.  2.  —  D  rt..%  ,/«•
2993:KompE.;    AMeit.  —  Vgl.  aosah-,  —   Eig.  (2)  j.  aui  bansen  N.  gS:  lies  or'ÄÄflr.urti.
4277:•  j.  an-aiwi.^ratvö.gätav-  Adj.  'der keinen  bestimmt  angewiesenen,  festen  Platz hat':  "'tu'''  (NDm.)  aita  äb^rtta  ^sraosa- vanza**  vlcarayahin  "ohne  festen  Platz sind  die  beiden:  der  Ab.  und  der  Sr.;  sie gehen  auf  und  ab"  N.  717.
5659:•  j.  *arStay-  f.,  anderer  Name  für  arftat- (sd.);  ufaratilUm  .  .  yqmca  sraosahe  ,  , yqmca  'tdif  yazata^e  y.^y.^^.
5857:•  j.  aspäyaoSa-  Adj.  'zu  Ross  (oder  um Rosse?)  kämpfend',  Beiname"  des  Zairi- varay:  °Ö3sairi.vairilYt. 5.112,11  J  (hier eingeschoben).
5937:•  j.  a-sraosa-  i)m. 'Ungehorsam' (nur  Ab- leit) 2)  Adj.  'ungehorsam' :  vUpe  adpriia.- Ikaiss  (sd.)  yJ  'iö"  vJspe  °A"  \ys\  anasa-  \ ranS  ". ,  aUe  die  (dem  Lehrer)  ungehorsam  1 siod,  sind  Glaubensfeinde"  V, /6. 18.
5955:asrutgaosa-
5976:j.  a-zaosa-  m.  'Nichtwille,  NichUbsicht'; yezi  zaela  yezi  -/a  (IS.)  "sei  es  absicht- lich, sei  es  unabsichtlich"  Y. ;.  21.
6421:•  j.  asi'vant-  Adj.  'der  die  Belohnungen besitzt,  verschafft*,  von  Srao/a:  s>raosS  O'ä astU  .  .  vanhui  'vä  Y.  56".  3;  —  sraosahe a/yeie  'vais  vpr^'^räjanS'^.i.T.  [Y.5<?. 6,  Vr.  g.  s :  lies  a^av^
7140:—  yat  titarat  (sd.)  attrö  tnaittyus  duhjm alahe  . .  antar)  pairi.avsilim  vohula  tnanö "tarsca  ta  hc  taurvayattm  tba!sa  Yt.  13. 7 7 f.*';  —  asim  vahütim  'tnmca  Y.2.4; 7.4,  A.  4.2,  S.  7. 7,  2.7;  —  xmümaine  ahu- rahe mazdä  am»sanqm  spintaiiqm  sraosahe afyehe  °^riJ  Y.  22. 4;  —  mana/a  yastum yat  ahurahe  mazdä  'hrascd  "S.^ff;  — haurvata  anitrstätä  ,  .  gjui  tarne  gfus itrwie  ..    "'hre  Y.JO.2;    7.2,  Vr.p-S;  —
8120:•  j,  ujra.zaosa-  Adj.  (fem.  '!•!-)  'starken sva.  unbeugsamen  Willens  gegenüber  — ' (Dat.) :  /ravasayö . .  °/.f  tbtsyanbyS  Vt  7J.  3 1  .■
8700:•  j,  u^as'tara-  Adj.  'gegen  Morgen  ge- legen, östlich':  °taire  kinävd  (sd.)  , .  daosa- taire  V.57.29;  —  haca  °lara  hindva  (sd.) avi  daosaslanm  hindum  V.J.  18  PüZ.;  — -taräl  haca.  nalmitt  °taraalyi>  haca  nai- maiibyS  V.  ig.  5,
8844:ayä  kahmäi^^  vananqm  (sd.)  dadh  Y. 4^15.  a)  mit  Gen.  part:  kö  hg  . . ae%rapaitinq7r^cä\  *afraoxti  (sd.)  astryäü N.  75 ;  —  kahmät  mazdayasnanqm  har»- 'hrtm  barät  V./j.  17;  N.  6'/,  G2;  —  kake vS  urva  /räye^ät  "^cuius  vestnim  anima . .  ?" Yt  13. 50;  —  iat  vast  (sd.)  iaj  vä  stBlö kat  Vä  yamahya.  "quid  vis?  quid  laudis  . ." Y.J4.12;  —  kat  tBi  as'ä  xbayetai  (sd.) avanhs  .  .  kat  .  .  "quid  . .  auxilii  .  ." Y.49. 12.  A)  Nom.  in  'Ist'sätzen  (s. 'a/i-  III):  ks  ahi  yS  mqm  zbayeln  \Liy. 17;  \.g.i;~  kö  asti  iraosahe  .  .  sraosil- var>zs  W.iS-n;  2.43,  7.78,  (y.31«,  Vt. 14.  i,  F.5;  —  if  airyama  ki  x^aetus" (sd.) datäisf  aukat  \.4g.T,  —  /«/(NSm.)  aAl ka/iyS  aht  (sd.)  Y.  4J.  7 ;  —  / 1*'/*'  hau  as .  .  yS  .  .  hö  aiiO  äs  . .  a/pmaayj  .  .  yO  .  . V.  y.5if.;  —  iai  tl  asti  ahunahe  vatryehe kai'^lm  P.  27;  —  kat  asti  mq^rahe  .  . amavast^tuMit  Vt./.i;  if.*,  /2.1*;  —  kal asti  damaya  .  .  uruiiwar»  V.j.30;  — '  cit  oval  vacö  äs  .  .  yat  .  .  Y.ig.i;  — /a/(NSn.)''  laoiar/ {sd.)  kainm  anhat N.72;--/«j(NSn.)"  aiüke  asti  uzvarsz^m V,  jrf.36;  —  hat  asti  ra'iswqm  /ram»r>itis Y.  7;.  I ;  I ;  —  kal  ait'ihe  asti  paititis  (sd.) V./A68;  68;  —  kat  sT  ('quidnam')  asti . .  tistTyehe..däity^i>inö  yasnasea  vahmasia \tS.$j;  —  las(SSa.}  aiMe  asti  bassass Yti4-34.  a)Kopulafehlt:  ks  ila&aSs'qm ar.mqm  paoiryö . .  hö  bä  aütaisqm  arsnqm paoiryü  yai  ..  Y.if/.^^t.;    —    k)   asavä
8956:•  j.  kaoia-  m.  EN.  eines  Gläubigen :  ^ac- raosahe  'iaAe  asaonS  "des  Fr.,  Sohns  des
9309:ä»  MazdayameT*h    vis/an^m  tbihatam   '  \  l^urvo^aosa-  Adj.  ^«'1  kahlen,  tin-
9888:•  p.  gauia-,  j.  gaoSa-,  g.  *g«uä.a-''  m. 'Ohr':'''''j&F._^g^';  — (ÄuvffjM  {^z.kSyum) 'fym  V.  (V,  44—46',  Q.  i6f.*;  —  sraotä *'gius.äiii'>  vakistd  "höret  mit  den  Ohren das  Beste"  Y._^.  z;  — _yaSa  *riär?Aa  haca *'saeibya'i>  ydha  vä  °/a  (ND.)  Aaca'*"Sira-
9893:KompE.  —  Komp.:  gaosa-+*d-iiara-  (zum  V. 'Äd-,  S  2**37)  m-  'wasiraOhtEetragen  wird'.
10579:•  j.p  g.  xraos-  V.  'schreien'.  Praes.  2 xraosa-,  26  xraosya-.  —  PPfP.  'xrusla-.
```


## [2026-09-07T20:17:51.223Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"an-aos\\|an.aos\\|anaos\" BRT.txt | head -20; echo \"=== usi ===\"; grep -n \"usi-  f\\|'die  beiden  Ohren'\\|beiden  Ohren\" BRT.txt | head -20",
 "description": "Grep BRT for an-aosa and usi"
}
```


### [2026-09-07T20:17:51.296Z] TOOL RESULT

```
11559:ai.  jänay-  t,  np.  iow.  —  VgU  Jqnay-.  —  mp. in«,  (in  A):JiA;  s.  noch  No.  i.  —  0  Pt4 usw. ;  NA.  janyaos  (woiu  Bthl.  AF.  3.  64). Das^  erklärt  sich  wie  in  al.  säkhyau.  Pu.: /fl  io»im,  — ')  S.  Vir.  NA./ancfl,  ohne  Epen- these 1
=== usi ===
```


## [2026-09-07T20:18:00.615Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"unsterblich\\|Unsterblich\" BRT.txt | head -20; echo === ; grep -n \"'Tod'\" BRT.txt | head -20",
 "description": "Grep BRT for unsterblich/Tod"
}
```


### [2026-09-07T20:18:00.666Z] TOOL RESULT

```
Exit code 1
3188:*J  Gemeint  ist  die  Zerstörung  des  Thebens  und alles  was  daiil  dient:  die  äaimichc  Gegen- achöpRing  [fiailyäta-)  in  dem  «Äunschen  gaya-. Vgl-  Bd.  I.  [ ;  iuadahiimk  i  ehrmazii  u  palyätak i  süräk  mrniii,  was  wesentlich  das  selbe  besagt wie  g'  ajy'.  Ohne  pa'ilyära-  wären  alle  aiiiri- sehen  Wesen  unsterblich.  S.  noch  Bd.  i.  6: kar  S  Hl  amiar  dahün  i  Shrmatd  tanärakömaH,!  u akanätakSmand  ei  en  an  i  andar  har  2än  meniik patmäii  ('Verlrag'}  däii/iid.  —  Pü.  beiiehl  die Stelle  auf  die  Schiffung  und  Tötung  des  Gaya Maritan.
4241:•  j.  an-aoäa-  Adj.  'dem  kein  Verderben droht,  unsterblich':  aurvantö .  .  mainyus.- ii^ar?^a  'shihs  Yt  70.125.
4242:np.  vgl.   iiBs   'Unsterblichkeitstiank' }   s.  dazu Hbm.  PSt.  19,  AGr.  /.  99.
4751:•  j.,  g.'>  a-maäa-  Adj.  'unsterblich':    'h
4764:•  j.  a-maräant-*'  Adj.  (fem.  °santT-)  nicht sterbend;  unsterblich':  yat  kirsnavqn  .  . ahüm  .  .  'hnhm  Yt  ig.  ii;  —  yaj  k)T}- naot .  .  *'/an/a  (AD.)  fasu  vlra  Y.p.4;  — bun  ga?SsA  *°sanlii  yä  a^ahe  Vt  /p.  1 2 ;  —
4775:•j.,g.am»rBta'^t-,  amarBtlt-'T.'Unsterb- lichkeit.  Ewigkeif;"'  tit  d^hnaotä  maslm hujyiH5is{sA)  "ntstascä  Y._j2. 5 ;  —  'rstSitl *a^aonö  urvä  also  (sd.)  utayütä , ,  Y.  43. 7 ; 48. 1 ;  —  yä  fyat/^an/t . .  -ntäbm  astmcä *taibyO  danhä  (sd.)  .  .  xs^nm^a  haurva- tätö  Y.34-^i  —  ahmäi  aahat  vahiihm yi  möi  vtdva  vaolat  hai~ilm  mq^r^m  yim haurvatatö  alahyä  'ritatasca  "dem  soll das  Beste  zu  Teil  werden,  der  mir,  ein: Wissender,  ktmd  tut  das  rechte  Wort  Aia^ von  der  Wohlfahrt  und  Unsterblichkeit" Y._3/.6.  a)  bes.  in  Dual  Verbindung  mit
6314:*)  A.,  Sohn  des  Pauruiäxslay-  gilt  Dk.  ji-  16, 17  als  einer  der  sieben  unsterblichen  Herrscher in  X^a>äta%a  und  Bd.  zp.  6  als  einer  der  Helfer des  SaosyanI  bei  der  Auferstehung.
12739:sOi  dqn*'  fytitÜ  utayBitI  ". .,  dass  uns  in seinem  Reiche  Wohlfahrt  und  Unsterblich- keit, in  seinem  Hause  Kraft  und  Bestand werden  sollen"  Y. 4:5.  10;  —  s^ahmi  dqm^'^ .  .  x'aAmi  xs'd^re  Vr.  14.1;  —  at'  &Si dümqm  HwaAmi  3  dam'^  ahurä  "seine Stätten   werden   in   deinem   Hause    sein,
13138:—  firaSaosträi  urväsistqm  (sd.)  asahyä da  sarSm  Y.  4p.  8;  —  spmiä  mainyü vahihäcä  manaähä  ..  kacä  asäi  (Sp.  231 m.)  .  .  ahmäi  dqn  (3PKA.)'>  haurvätä ammtätä  matdh  xiakrä  ärmaiti  ahurS ".  .  wird  uns  Wohlfahrt  und  Unsterblich- keit verleihen  MAh.  im  Verein  mit  Xs., mit  Arm."  Y.  47. 1 ;  5^.  1 ;  —  däidl  *a/<*  V.; (Sp.  7  40  u.)  dangayü . .  sara%ustrili  Y.  2S.  6 ;
13140:[verwendet  Ytp. 26;  —  sva.  'freigeben', den  Weg:  hyai  ahysi  dadä  pakqm  (sd.) västryät  vä  äitl  (sd.)  Y,^/.  9;  —  sva. 'preisgeben':  yuisgqm  karapa  taix/^ä {sd.) oS>m<j/ <ÄJ«(3PPrM.)*'«>Y.44-2o; — durch enkl.  Dat(-Gen.)  des  Pron.  pers.:  däidl mSi . .  am^ntätä  haurvälä  spsmstä  mainya mazdä  utayaitl  tpvli^l ..  sJnahlisd.)  "schenk mir  .  .  Unsterblichkeit  und  Wohlfahrt  fiir den   heiligsten  Geist,    o  J/.  . ."  Y.5J.  7;
13595:für  die  du,  o  M.,  die  Unsterblichkeit  und das  Asa  verleihen  wirst  , ."  Y.  34.  1 ;  — mlidjm..hyat  möi  mazdä  apivaiti  kaurvätä amfritätä ya^S  kl  *taibyS  'ha  "der  Lohn.., der  mir,  o  M.,  zugesagt  ward,  so  gut  wie deine  Verleihung  der  Wohlfahrt  und  Un- sterblichkeit" V.44.18.
16199:*)  Er  wird  Dk.  p.  16.  15  als  einer  der  sieben unsterblichenHerrscher  inA'"flHi™Sflbeieichneti s.  noch  Dk.  7.  4.  81  und  zu  kaiiha-.
17809:•  j.,  g.''  fravaäay-  f.  ^Fravasay*'>,  Be- zeichnung für  das  dem  Gläubigen  eigene Unsterbliche,  das  Element,  das  schon  vor setner  Geburt  vorhanden  war  und  ihn  über- dauert. So  lang  der  Gläubige  lebt,  wacht seine  Fr.  als  Schutzgeist  Über  ihn.  Die Gesammtheit  der  Fr.  der  Gläubigen  aber spielt  eine  ähnliche  Rolle  wie  die  indischen pitärah,  die  römischen  ««««■:  'sayö  hütti^ Aatqm..aigAu^qm..bUsyantqin{Sf.^^i  m.) a!'aanqmYt.i3.2\;—ä  hätqmca  anhusqfnca zätanqmca  azätanqinca  asaonqm  ilajasmiu °sayd  Y.  öj.  6;  —  aat  anyaisqm  'say!> jvanqm  narqm  aiaonqm  aojyehfi .  ,  ya^a iristanqm  "aber  im  übrigen  sind  die  Fr. der  lebenden  Gläubigen  stärker  als  die der  gestorbenen"  Yl;_j.  17;  —  vispäbyö asaonibyS  *nbyS  y3  irlrüu/qm  .  .  yasia jvantqm  .  .  yäsca  narqm  azätanqm  Y. 24-5;  —  vispanqmca  änhqm  alaonqm asaoninqmla  ila  yaxamatde  °stm  Yt,  ij. 148';  —  neben  'aAs-,  *da?nä-  usw.; alaonqm  aiaoninqmla  ahümla  dafaqtnca baoiasca  urvarumca  °slmca  Y.  26'.  4;  — gai^ssca  asdsbJlca  us'tänqsca  kahrpasca Uvlilsca  baohasia  urvämmca  'sTmca  Y. 55,  I ;  —  xardkuitrahe  . .  'Am  . .  sravä  . . dainqm  . .  varvtifmca  tkais»nca  Y.  16. 2 ; —  manä  . .  dalnä  . .  urunS . .  'say!)  (als  AP.)
25621:•  j.,  g.  urvan- :  urun-  m.  "Seele,  Geist'; I )  beim  Menschen  von  der  unsterblichen Kraft,  die  all  seine  Handlungen  bestimmt und  nach  dem  Tode  zu  verantworten hat;    i)  von  der  Seele  zu  Lebzeiten  des
29638:•  j-,  g.  haurvatat-,  baurvlt-'>  £  'Gani- heil, Vollkommenheit, Wohlfahrt"' :/5  Äaii- "^anä ..  armrftataiftn  astmcä  *taibyS  däahä (Sp.  744)  ..  xsahnmi^^.  544  \L)cä  •vatäts  Y. J4. 1 ;  — yf  msi . .  vaocät  katiim  ma^rpm yim  'vatäiö  asahyä  attantiliai(^A.)cä  Y. ^t.  6.  a)  bes.  in  Doalverbiodung  mit atmnttttat-:  diidl  mdi  .  .  ammtätä  'vä/ä s/Jms'ta  mainya  masdä  twih  utayüti  "gib mir . .  Unsterblichkeit  und  Wohlfidiit  durch den  heiligsten  Geist,  o  M.,  Kraft  und  Be- stand" Y.5/.7;  45.10,  44.18,  47.1;  — 10a  'Vota  amsrftata  yöi  sis  mistüm  aiao- nqm  parS.asü  Joimtam  Yt/.as;  —  matJ (sd.)  ^ra.fmS.hyäi  däidl  °vata  (OD.)  amsrf- mi  Y.5Ä7.  a)  als  Bezeichnung  fdr den  Trank  der  Seligen:  al  IBt  ubs  'vds- (HS.yica  ^anhäi  ä  am7r)talas{iA.)ia  Y. j4.11.  A}alsGottheit"(^M^/fl.^j«/<7), der  die  Sorge  für  die  Wasser  anvertraut  ist (SüEtL:  udaksdhipatih)*'>:  'vatättm  am?s?m spmtpm  Yt  4. 1  o" ;  —  aya  daStaya  fraormSa ahurS  mazdä  .  .frä  vohu  manS . .  as»m  . . x^a%r?m  . .  Srmaitii  frä  'vatät  frä  amirv- latäs  Y. 57.24;  —  vanät  •väs}a^'>  amiri- ihca  uva  h^imca  tarsmmca  Yt  ig.  96 ;  96 ; —  ärmaiUm  .  .  'vataUm  .  .  ammtatätim Y.16.3;  7/.  12,  S.2.6f.;  —  atf/n  da^atn •vatätö  narqm  ai'aonam  aväsca..  Yt.4-r  {f)', ■ — ■  mazdä  dadät  ahurS  "vatB  amfntslascä . .  sarff  (sd.)  Y.  _J/.  2 1 ;  —  dälä  vJ  amir?- tascä  utayäin  (sd.)  'vatäs  (NS.  als  VS.)^ draond  Y.  33.  &;  —  UätS  ra%wS  Yt. 4.0,  11;  2;  —  'vatasca  amir>tathsca yt.4-i(?)-  o)  bes.  in  Dualverbindung mit  amPTitatilt-.  {lya  dastaya  fraormla ahurB  mazdä .  .frä  'rata  (ND.)  amtr^täta Yt.  jo.  92;  —  saröi  buidyäi  (sd.)  'vätä am>r?tätä  Y.  44,  17;  —  upä.jimm  (sd.) •vatä  amtrmtä  (AD.)  Y.  45. 5;  —  yä spftitayä  ärmateii  yä  °vatä  (GD.)  amir}- tätä  Y.  70.  j;  —  'vatäsca**  nS  amintätä gsusca  talnS  .  .  Vr.  <?.  5 ;  —  sp?ntayäi ärwatse  °vatbya  arngntalbya  Y.  /.  2; I.  7.         a)  haurvatais  (näml.  ayari)  heisst
30201:•  (j))  g-  hu-JyStay-  f.  'gutes,  behagliches Lebea'  (nur  Komp.).  a)  insbes.  'das gute  Leben'  im  Jenseits'';  ta  dihinaotS maslm  'tSis  attuntatascä  hyai  .  .  fyao- %an>m  . .  "damit  bringt  ihr  den  Menschen um  das  gute  Leben  und  die  Unsterblich- keit", mit  dem  Tun,  welches  .  ."  Y. J2.  s ;  —  paityaogit  (sd.)  ta  .  .  yä  Xm 'tsil  payät  nöit  duzjyüisis  kactt  masda dvaihvM  "alle  (die  Taten)  die  feind- seligen, die  ihn  vom  guten  Leben  fern- halten werden,  nicht  vom  schlechten, o  M:'  Y.46.S.  [Yt.5.130,  V.J.3:  lies vispqm.hu/y.']
(eval):1: == not found
```


## [2026-09-07T20:18:23.091Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leaf(f,i):\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    return t[i]\nfor p in (8,20,30):\n    print('##### HRN printed page',p)\n    print(leaf('HRN.txt',p+21)[:3000])\nEOF",
 "description": "Print Horn pages 8, 20, 30"
}
```


### [2026-09-07T20:18:24.352Z] TOOL RESULT

```
##### HRN printed page 8
— 8
27. äsmän *Himmel', äsmä, semän,
g. asbän,
ap. asman- 'Himmel'; aw. asman-; phlv. äsmän; ai.
dgmafi-.
kiird. LW. asmärij äsimün, asmm; a{y, LW. äsmän;
bei. n. äzmän (22); sangl. minj. LW. asma, wa/. sar.
si/n. LW. äsmän,
28. äsüden ^beruhigen, ruhen', Praes. äsäy-em, -äsä,
äsäijis^ äsäyist (jüd.-per$.).
aw. *ä + sävayeitl (Bedeutung?); phlv. äsiitan^
äsäy(i)sn,
29. äs *Brühe, Speise .
skr. äga- in prataräga- Trühstück'. säyamäga- 'Abend-
essen ; vergl. aw. kahrkäsa- *Hühnerfresser.
kurd. LW. äspezyßne 'Küche'.
Zweifelhaft, denn np. s passt nicht zu skr. g, aw. s;
vergl. aber näsnä (No. 1019).
30. ÜHäm 'Trank', äsärmden,
aw. säman- 'Tropfen, vergl. fräsmi- (Geldner,
3 Yasht, 115); phlv. vergl. apisamak oder apismak
(vd. 5. 149, 7. 164).
31. äsH 'Friede*.
aw. äxsti' (ä/ßä), Bartholomae, Ar. Forsch. II,
100 (?); aw. ä/sti- 'Friede'; phlv. ästth, anästfh.
yayn. astiato forti 'se reconcilier (Tomaschek, 746).
32. äffuften, äSöften 'in Bewegung versetzen, Praes.
äsöb-em, äsöh, JTiNZIlÄ'N (Is. 9, 10), ]r;2^\t/^ (Is. 22, 5).
aw. ä-\-/sufsqn; phlv. äsöftan (vd. 9. 132, Gl.), äsöp
(d. i. äsöw)y äsöft'kärih (DK.); ai. [/^ksubh-, ksobhate
'in Bewegung geraten'.
33. äskär 'klar , äskärä, äskäre,
phlv. äskärak, äskäräk, arm. LW. askaray; aw.
*äviskära- {ävis 'offenbar, klar, y. 33, 7); vergl. skr.
äviskfta- (ai. ävis) und skr. äviskära- (spät) selbst.
af>^. xkära 'deutlich'.
34(i). äsna 'bekannt', äsnäyt,
ap. *ä(x)snäka- 'bekannt'; phlv. äsnäk.
##### HRN printed page 20
- 20 -
81. est ^Knochen, este 'Knochen, Kern' (vergl. künjeste,
AM. 80 Zeile 5, 163 Zeile 5 v. u., 170 Zeile 3, daneben
auch gün]estej AM. 126 Zeile 4 v. \x,), /estu,
g. äste,
aw. ast-^) *Knochen ; phlv. ast 'Knochen*, astak *Kern;
ai. asthdn-, dsthi-,
kurd. haste 'Knochen etc.; oss. stag, L stäg (228);
minj. asti, sangl. astak.
82. i8tä%, istaky sitak 'Zweig*.
de Lagard e vergleicht arm. cax, aber np. istäx könnte
im Armenischen nur als stax erscheinen. Die ältere
Form ist istak, sitäk, phlv. stak (Bund.). Zu l^sthä-.
83. iistäd, ustaö *Meister'.
aw. "^avastata- 'Vorsteher; phlv. östat, arm. LW. ostat,
LW. kurd. üstä; aiy. usfaä; bei. vastäd (286).
84. istäden stehen*, estäden, Praes. esf-em^)^ sitaden,
p^N^xriD^t* (Jer. 5, 26).
ap. V^stä' (ai. sthü-); päz. estädan.
Im Sähnäme reimt ist *stehe* auf nest, ist also est zu
sprechen {me est I, 136 Vers 125). Ich leite np. estaden,
später istäden, von ap. *adi + l^stä- ab, vergl. phlv.
evar (unter No. 16) und KZ. 32, 581 No. 7.
oss. t. sfln, d. isfün aufstehen* (144) ; sist 'stehe auf*
etc., mit Praefix s (ms).
phlv. ösfätan [ava + \/'stä-) ; bei. östag, vustag n. östay
(402) finden sich im Np. nur dialektisch in g. ustädmün,
vistädmün.
Das PehlevT besass auch die mittlere^) Wurzelform
stT' in stinik (vd. 5 (38), aw. ereöwa-) ^b^%stm 'aufrecht
stehend* (vd. 18 (98) GL), vergl. skr. sthTyat^ (Brähm.)*).
^) Bartholomae, Arische Forschungen II, 112.
*) Auch in Indien spricht man nur Waden,
') Zur mittleren Wurzelform aihä- vergl. Hübschmann, Das
indogermanische Vocalsystem 20, 63.
*J NatürUch könnte man die Pehleviforraen auch steulk, -sten
lesen und skr. sthimän- etc. vergleichen, dessen e (*ai) aus ai/i ent-
standen sein könnte (vergl. Bartholomae, zuletzt Indog. Forsch. I,
490). Die Lesung stenik, sten scheint Bartholomae nach brieflicher
Mitteilung vorzuziehen.
##### HRN printed page 30
— 80 -
125. enguM Tinger, Zehe'; vergl. etigustetl 'Ring'^
engusfioäne Tingerhut* *).
Kä§. ungüss^) (neben engüst, mgüs etc.); mäz. nngus.
aw. angusta- 'Zehe'; phlv. angust^)\ skr. angtistha-
*Daunien, grosse Zehe*.
kurd. LW. engust; oss. d. at'ndje^ ünguljä Tinger
(LW.), t. ängursf (26); af/. güta; wa/. yangl, minj.
augar, §iyn. angast, sar. ingä/t, sangl. ingit.
Dialektisch findet sich Kä§. engxdt, mäz. e)igel^
vergl. skr. atlgün-, angüli- Tinger, Zehe'.
126. efiffist 'Kohle'.
Vergl. skr. angärä- 'Kohle'.
127. engeiten antreiben', Praes. engez-em,
phlv. angfytan antreiben', angejet (AV.), vergl.
ham]vB/t (Geiger, Yätk. Zar., Anni. 52); skr. vgl.
samvignu' 'aufgeregt'.
vergl. oss. d. ve^^nn^ t. viyin erschüttern, bewegen'
(80), bei. gejag n. ge^cig 'schwingen, schleudern,
schlagen' (113).
128. enose 'glücklich, heil!', vergl. hös, nöse, nösin,^)
aw. anaosa- unsterblich'; phlv. anöäak unvergäng-
lich', arm. LW. antcsak, anois,
oss. ämisoriy änusi 'unvergänglich' (119); nicht bei.
anJmy 'Schicksal' (2) (Hübschmann, ZDMG. 44, 555).
129. ö er, jener, Plur. ösän (dialektisch, Lumsden, Per-
sische Grammatik, II, 76 Anm.; vergl. gel. üsüfi,
ühan),
ap. aw. ava- jener'; päz. ö.
Vergl, kurd. ätr, atve jener, er'.
130. o- (Praefix), u-,
aw. ava 'herab, von weg'; phlv. ö; ai. dva.
131. ewam, awam 'Schuld', loam,
phlv. äpäm (PPGL).
bei. LW. warn (288).
^) Aw. *angu8tapäna' (vergl. aw. ranapäna-)'^ oss. d. LW.
ängurstevän.
*) Der Wechsel von st und st ist häufig.
'') Vergl. Fr. Müller, WZKM. 5, 264.
```


## [2026-09-07T20:19:03.955Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ascu/Schienbein ===\"; grep -n \"ascu\\|Schienbein\" BRT.txt | head -10; echo \"=== BRT ast- Knochen ===\"; grep -n \"Knochen\" BRT.txt | head -15",
 "description": "Grep BRT for ascu, Knochen"
}
```


### [2026-09-07T20:19:04.022Z] TOOL RESULT

```
=== BRT ascu/Schienbein ===
7790:Ableit.  aus  iahairi-.  —  Pu, :  gihänl»  baviiniA ..k?  an  bavisnih  zäyiin  "vivorum  'futurit»s' . . cui  ilU  futuritas'  gignenda";  etl.:  Ü vusaak it  vuhühH  z^yisn  räh  itnt/ar  afäyil  *'masculuB enim  alque  'mascuUnitas'  gign«ndi  causa necessaria  est".  S.  noch  Dst,  ZA.  /,  445.  — 1)  Sc,  JusTi  -das  Zukiinflige  der  Welt',  DST. 'la  Production  des  etres',  MlLLS  'Ihe  Settle- ments of  the  futuie'. g.  äiiAS,  Si^liö:  s.  iSh-,
23081:•  j.  ^araäna-  Adj.  'mUnnlich,  masculus': cvai  . .  ?  yä^a  -nahe  hhrpahe  ä3ul  (sd.) N.  106.
=== BRT ast- Knochen ===
2551:spjmm  taropi^w)m{'&&.)  dastccvai  °tal-  kelterler Ä,.,  ..aber  (die.)  die  ungekelter- sqm  Syachnanqm  ästäraiti  "wenn  einer  ,.,  ten  . ,"  V.  Ij.  43;  — ■  yesi  nöit  sänö  . .  ^ta»- . .  solches  Thun?"  V.  jj,  ao;  —  yaica  vao-  hqtn  astqm  .  ,  barptit?m  frajasqn  "sonst cät  . .  aSaoa  (sd.)  ..  *havanli  (sd)  -tuhe  könnten  Hunde  .,  die  Knochen  verschlep- ryao'knaAe  .  .  V, /j, I3f.;  —  foa  iristaAe  psa"  V-6.46;  T,—yat ..Strim  natuplhm tatiüm  ovaMsta  . .  "tahe  ^aöinahe  , ,  V.  frajasqn  .  .  ava  °tim  nasupiknn  lanaeta 8. 100;  —  ä^ravamm  yaoida'i^ö  (sd.)  . .  . .  apa  'tarn  disiam  (sd.)  baray^n  apa  -t?m Hahmiii  natre  ".  .  einem  solchen  Mann  aa/jnjni  (iariy;'«  "wenn  (sie)  ..  auf  leichen- (der  purifizirtj"  V.p. 37— 39.  4)  auf  kochendes  Feuer  stossen  ..,  den  Leichen-
4932:'töis  pouruhäxstayanake  asaonsYt.13. 112. Eig.  'des  Knochen   von  Metall  (Eisen)  sind'.
5772:'<n'a.^/-p>/J/(sd.)V.^5o;  51.  a)  Sing. und  Plur.  'Knochenbau  des  Leibes':  "/J *hutal{lm  . .  lanvö  *huraomm  (sd.)  P.  4^;
5781:•  j.,  g.  ast-  n.  'Knochen',  von  Menschen und  Tieren:  _>'J  °/j«"  upanh}r?zaUi  siinS vä  .  .  masyehe  vä  V.  t/.io;  5.1Ö,  F._y  i;  — kva  narqm  iriitanqm  azdibls  (als  Obj.) baräma  kva  nidaiäma  V. 6.49;  — yö..
5792:•  j.  astaena-  Adj.  'aus  Knochen,  aus Bein  gemacht,  beinern':  nlif  °naeiiya {hszanaäbya)  .  .  ratufriS  N.  /07.
5797:•  j.  'astay-  n.  'Knochen'.
5799:•  j.  asta'va-  Adj.  'mit  einem  Knochen Teisehcn';  °v3  vä  taxmahe  mirr/ake pars- nai'SvS..  "wer  einen  Knochen  des  starken Vogels  oder  eine  Feder  (als  Amulet)  trägt .." YL/4.3(S.
5817:•  ].  asto.bid-  Adj.  'wobei  ein  Knochen gebrochen  oder  geschädigt  wird',  mit 3^ara-  ra.  (sd.)  Term.  lechn.  für  die  der Schwere  nach  dritte  Art  der  Körperver- letzung'': y5  nanm  'biiitm  i^arim  (sd.) jainti  V.4.37.  39-
5824:•  j.  *asti.aoJah-''  n.  'Kraft,  Stärke  der Knochen'  sva. 'Körperkraft':  Harqm..y5i hyqn  "Jaaha  aojtsta  ".  .  die  an  Körper- stärke die  stärksten  sind"  Yt.  Ä  55.
6936:einem  Hund  . .  nicht  zerkleinerte  Knochen
8650:Pü.:  u:^!tihisl,  (luV.  ö)eri.:  ni/m/J« 'Knochen-
9275:mit  paiti  und  ava  vll.  'hineinschneiden bis  auf  — '  (Akk.):  aya?ihalnsu  kantais azdibls  (für  AP.)  paiti  ava.k>r>i:ylt  "mit eisernen  Messern  soll  man  (ihm)  bis  auf die  Knochen  schneiden"  V.4. 50^'.
9277:und(far*w«/)**jr/H/fl,  PPA.  —  31  Es  handelt »ich  um  eine  Straftnarler,  Vll.  ist  azdibii  als Subj.,  k3rf%yäl  als  Pas5.  (mit  Aktivendung)  za nehmen ;  'die  Knochen  sollen  durch  Schneiden mit  ..  Messern  gelrofTen  werden'.  —  *)  Sü. ; prati-flam  kj-tah;  vg\.  frätirislay-.  —  S)  Mit a!l-=  Aw.  >nsi;  falsch  Ggr.  GlrPh.  /  b.  Sig. —  6)  Mit  irr  aus  r"'  a""-  r"'"i  Salemanns Fassung  GlrPh.  /.  303  verstehe  ich  nicht.
10276:•  j.  garaman-  m.,  Plur.  'Kehle,  Hals':  j  i'^'i  "ler  Klage  folgt  iti  dir.  Rede.  —  »  Mii y€zU'a  aZU  asti  düllhva  arante  'mS-\  '«'■rekter^Um^el^iune  i"s  jAw.;  s.  Btiil.  IF. kva   vToänie  "wenn   die    Knochen   (dem ,     ^'  '^  ^'  ""'•
15629:sollen  sich  nicht  dadurch,  dass  sie  Knochen oder  Haaie  .  .  hineinfallen  lassen,  am Wasser  versündigen"  V.  6.  29.
```


## [2026-09-07T20:19:05.840Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n \"ast\\b.*bone\\|astag\\|astūxān\\|astōxān\\|stūxān\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"astak\\|ast .*bone\\|anōšak\\|anōš\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-07T20:19:05.915Z] TOOL RESULT

```
=== PHD ===
PHD_mackenzie.txt:1065:anastag, ['n'stk ] = anast.
PHD_mackenzie.txt:1239:lIast(ag) ['st(k) I I M 'st(g), N hasta] bone; (fruit) stone.
PHD_mackenzie.txt:1283:astag ['Itk l ] messenger.
PHD_mackenzie.txt:1745: I~astag [c)ltk l ] doctrine.
PHD_mackenzie.txt:4169: paywastag [ptwstk I N ......a] continually.
PHD_mackenzie.txt:4352:rastag [lstk' I N rasta] series, row, progression; element.
PHD_mackenzie.txt:5245:was-xwastag [KBDhw)stk ] wealthy, rich.
PHD_mackenzie.txt:5250:wastag [wftk l ] sick, ill.
PHD_mackenzie.txt:5257:wastih [wftyh] = wastagih.
PHD_mackenzie.txt:5390:wlnastag [wnstk'] spoilt, corrupt.
PHD_mackenzie.txt:5931:   harwin, harwisp, hambastag.            apple seb.
PHD_mackenzie.txt:6109:brand drosidan.                        bunch, bundle dastag.
PHD_mackenzie.txt:6215:cock xros.                               composed hambastag; be- hambiidan.
PHD_mackenzie.txt:6223:collapsed hambastag.                     comrade hamahl, hamal.
PHD_mackenzie.txt:6267:constitution passazisn.                      corrupt gannag, winastagj v. ,·otten.
PHD_mackenzie.txt:6288:continually paywastag.                       fO'l'er (v.) nihuftan, (nihumhidan),
PHD_mackenzie.txt:6407:direct (v.) rayenidan.                  doctrine afrah, castag, poryotkesih.
PHD_mackenzie.txt:6492:element amezisn, rastag, dhag.               erect stey, stendag.
PHD_mackenzie.txt:6508:estate dastagird.                                  expense uzenag.
PHD_mackenzie.txt:6541:exaltation (astr.) biilist.                        fallen hambastag.
=== NYB ===
392:ämatan [Y"TWN-tn']dy-to go, to come, to arrive, to come on, to issue, to appear, passim; together with other vbs.: àyet u tapet 2219.13.16 (3d p. sg.); à? u den stāt 9926-27, apt-š Amat 2 zan nisastak dit hav- ing arrived there he saw ... 617; druyist šutan u āmatan to go and come in due
620:arastak ['Pstk'] fully armed, equipped 115. 310, 816 — From
706:ast ['st' the bones 50!. 10012; +ast- dahišnan corporeal creatures 5571. — Av. (211 sq.) ast-; MPrs ?st, stg. V. astómand.
1038:bun [bwn] bottom 102% ; foundations 1138; root 9375; beginning 81!; the primordial revelation 1118-9-21, 11219; — capital, stock of spiritual values acquired through meri- torious deeds: a ~ i... kartan to add (a value) to a p.'s spiritual stock 7912-14; 6 — bavet it affects a p.’s spiritual stock = detracts from it 652%. 8124, — Av. (968) būna-; MPrthPrs Paz. NP. — V. bundahišn and bunyastak.
1256:én apčcak ~ i mäzdesn 244; veh ~ 4 apčcak 5914; (En) apécak veh ~ 4 maz- desnān 819. 844; ~ i Ohurmazd 60%; ~ stayitan, ~ yastan: v. these ws; — in particular: the authoritative canonical texts of this religion: én ~, cigon hamäk apastak u zand namely, the whole Avesta and commentary 1078; the quotations from these texts are introduced by the following formula: cigén ~ göbet followed by ku 3613-14, 421-13, 4520, 4615, 484-18, 491-16. 5224, 53%. 541-17; followed by hat (q. v.) 387-8. 4375-26, 4414-15, 503-5; without following particle 41196; (7) cigon et i ~ gobet ku 5323-24, 563. 581. 608. 617-8; cigon pat ~ 7718, pat hàn i ~ göbet kū 4345; andar ~ guft estet 8011; an-ic ~ gobet ku 3819; hac ~ (čičn) paitäk kü 341. 8612-115; cigón hac apécak veh- ~ i mäzdesnän paitäk 819-9; v. further paitäk and paitakéh; v. also s.v. dipivareh. — Av. (662 sqq.) daenä-; Arm. lw. den; MPrthPrs dyn religion, religious community, church; Paz. din. — Cf ak-dénéh, dén-burtàr, denik, dušden, huden.
1294:1ditan [dytn'; HZYTN-tn', inscr. and Ps. HZYTN-] vén-, 2nd p. sg. HZYTN-yd = vënë 7164. HZYTN-h = venah 31°; subju. lst p. sg. HZYTN-n = vēnān P2: 10: to see, to regard, to catch sight of, to contemplate, to discern, to experience: ayāftan u ~ u dänistan 88°; dänäkıhä ~ 51; pat venisn ~ 5013-1; pat (xves) cašm ~ 7479, 80%; — with ki that 115. 127 ete., with ka that 40%; — with a pt. as its complement: -m murtak dit han tahm spähpat I saw this valiant general slain 2719-11; 2 zan nisastak dit 6"; with an adj. P2:10. 2719. 5776 sq. (purr com- ` plement); — with an indir. interrog. clause: ~ kū . . . cigēn to see how 2518-19; ka-t dīt kū kas kē ... kart 137-9 a contam- ination between ka-t dit ku kas
1827:hamév (inser. [hmyw], hamé [hmy, hm’y] always P 2:6. 2675. 6327. 10622-23; ~ ka always when 45°; ~ alone in this sense 1285; patvastak ~ pat Sap ka regularly every night when 5!-?; ~ tà ka, v. tdi; — often the original sense has faded, and — serves as a prev. denoting perduration or iteration, as (ha)mi in NP. — ham + ēv < *aiva-, Gr alel, det <
1883:handixtan [hnd*htn'] handdc- 1. apāc ~ to bring together again, to reunite, with apāk ‘with’: apāk apastak apāc handāxt reunited (them) with the Avesta 1091, 11119-20, — 2. to measure, to calculate (the horoscope) 7$. — 3. impers.: api-m
2744:nipast [npst'] place where a thing is deposited, depository, gl. of KLYT’ = gellāitā (v. Ideograms) 107%, — I reject the interpretation of the passage given by Bailey, ZP 152. There is no evidence what- ever of an ideogr. KLYT = QRYT’ being used for diz ‘fortress’. This Aram. w. always signifies ‘village’; in the FrP, ch. 2, it is hidden behind the somewaht be- wildering disguise MRDYN! (-DYN- common. error for -YT-) for MRYT" for QRYT* (cf MDM for QDM) = rētastak (g. v.) A form *ntptst for nipist is no- where attested, so the diz i nipist has to disappear from our context. KLYT? = Aram gellāitā (ultimately from lat. cella) refers obviously in KnS VI, 11 to the sanctuary of the Dragon of Kirman, most probably a cavern. — I deeply deplore the Ahrimanic slip of pen which made me write ntpāst, instead of nipast, as the equivalent of KLYT’ in the Index, I, 160a, 14. A benevolent critic will find the correct reading nipast in I, 157a, 30. - From nipastan; nipast is to nipastan what nisast is to nisastan.
3001:2pat[PWN; Prth. inser. pty] A. prep.; not governing encl. pronouns (in pat-šān dra- sanéh 10974 the enel. belongs to the follow- ing subst.). I. in a concrete sense: 1. local: in, on, upon, at; (to pass) over (a bridge), through (a passage); (to remain, dwell) with a p.; passim; 'pn LGLH PWN ZNH drky HNHTWN = api-n päd pat én darraky nihāt HajB: 6-7. (12-13), Prth NGRYN pty ZK wym HQ’YMW-t HajA: 6—7. (11-12); PWN ZK Psy ZY ... = pat hàn rah" 1... on the road to... P1:4. — 2. time: pat ham Sap 16°; pat- vastak hamë pat sap ka 5!; sap 1 sitikar pat usbam 1012-8 ; pat ul vaxšišneh inazdeh
3098:patvastak [ptwstk'] continually, regu- larly 51; subsequently 1111.
3262:rastak [lstk'] free 91?, from
4164:vinäsitan to destroy 5029, 7425; menisn i ~ to spoil a p.’s thoughts or intention: to seduce a p. 4817, to put a p. out of countenance 5222. — Av. (1055) Inas- ‘to disappear, to be lost’, (1056) vi-nas- ‘to be subject to destruction’ ; MPrth wnštg ‘destroyed? (MHC); MPrs wn'stn wn'h- ‘to damage, to injure’ (S); Verbum 191. V. also vinastakéh.
4168:vinastakéh [wnstkyh] decay 1128. — De- rived from the basic vb. vi-nas-, v. vind- sitan; SW form with -nast- for -nast-.
4219:višātan [wš'tn'; SLYTN-tn'] višay- or vi$-, to open, to let loose, to release: tô hàn i har 2 brätar i bastak viš(āy)ē [ŠLYTN- d, with final -d for -y as often occurs in the inscriptions after an ideogr.] thou wilt release thy two captive brothers 913; pt. visät loose, running without its rider, of horses 228; v. also the next w. — vi + Av. (1800) häy-; MPrth pt. wyš*d, pres. wyš*h-, pt. also gws’d, Ghilain 88; FrP 21 pres. in most MSS wšyt' wš(y)m, but Codd. U, U, wš*dt' wš*dm = visdyet, visayem ; Paz. kušādan kusäend (but subst. vašādai < visätakeh ‘open space’); NP gušādan gušāy-.
4360:to summon a p. to one’s side 2?-3-12, 56, 104 ete.; without 6 pes 625, 73. 315; Ohur- mazd ast hac damik ... x“ahét O. will call up the bones from the earth 100'2-13; vas a«vāhišn (q.v.) i rüpak-karihà xvāhēt he clamourously utters many implorations 7426-27, — 3. to ask, to demand: pat zan ~ to marry a wife 675; pat zanéh ~ to ask in marriage 1165-5; hac Papak past (g. v.) u zinhär xvāst 214; 3 rēc jamān x“äst he solicited a time of three days for consideration 11819; 121%; mizd dātihā ~ to demand reward righteously 8120-21; hac x"at karap margēh 4 Zartuxšt x"àst, apar cé āivēnak margēnītan he asked the karap himself about the manner of Z.'s death, how to put him to death 4812-13; sāi u baz ~ hac to exact tribute from 177. 58%; Pourušasp hàn hom hac Dugdāv apāc x"àst P. asked D. to give him back that Haoma 42?4-25,. 4, to seek,to search,to look for, to ponder, to strive to attain: api-ščin hàn hom x"àst they searched for that Haoma 409; pat ~ 4 hàn i či zuarrah in striving to attain his Glory 4614, more fully + an inf: api-š hàn xarrah bē aydftan x“dst 4618; — with an abstr. subst. as its obj.: v. cärak, ddrišn, dösäram, hucasmeh, ken, panäh, zivišn, ete.; cf also s. v. az"àyisneh. — Olr *hväz-, MPrth wx'št, pres. wz?z-; MPrs xw'stn, xwh-; Paz. NP z"üstan audah-; Verbum 187; Ghilain 69; Bailey, BSOS VI, 1930, 74. V. also x“dstar, -ēh, zuäyısn, -ēh.
4647:Barthélémy GA = Gujastak Abalish. Texte pehlvi publié pour la premiére fois, avec traduction, commentaire et lexique par A. Barthélémy. Paris 1887. Bibliothéque de l'École des hautes études, sciences philologiques et historiques, soixante-neuviéme fascicule.
6208:xw'stg: xuastak
6503:ec) : bunyastak
7366:röstä(i): rotastak
```


## [2026-09-07T20:19:26.217Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (230,231,232):\n    print('#### leaf',i)\n    print(t[i][:2500])\nEOF",
 "description": "Print Buck SYN page 207"
}
```


## [2026-09-07T20:19:27.503Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ost-\\b\\|ost(h)\\|osteon\\|ostreon\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for ost-"
}
```


### [2026-09-07T20:19:27.541Z] TOOL RESULT

```
1545
#### leaf 230
through the ‘gnawing’ woodworm. Ber- neker 403. Briickner 459.
3.85 SNAKE
Grk. — b¢us (és) Goth. waurms, nadrs Lith.  gyvaté (angis, Zaltys) NG Sdus, pl5e ON ormr, nadr, snakr Lett. _ éiska Lat. anguis, serpéns, Dan. _ slange, snog ChSl. zmija
colubra Sw. snok, orm SCr. zmija It. serpe OE wyrm, nedre, snaca Boh. had Fr. serpent ME  worme, snake, ser- Pol. waz (zmtja) Sp. culebra, serpiente pent, (n)addre Russ. zmeja (uz) Rum. garpe NE snake, serpent Skt. ahi-, sarpa-, uraga- Ir. nathir Du. slang Av. azi- Nir. nathair OHG nét(a)ra, wurm, slan- W. neidr, sarff go Br. der MHG slange, wurm
1. Grk. égis (NG gid fr. dim. ogl- doy), beside gus, exdva ‘viper’ (less generic than és cf. Aristot. HA 511914 ff.); Lat. anguis; Lith., OPruss. angis; ChSl. *qzt, Pol. waz, Russ. uz; Skt. ahi-, Av. adi-; fr. parallel forms with and without nasal, but phonetic rela- tions in part obscure. Walde-P. 1,63 ff, Emout-M. 52. Walde-H. 1.48,
2. Lat. serpéns, pple. of serpere ‘creep’, like Skt. sarpa- fr. srp- ‘creep’. Walde-P. 2.502. Ernout-M. 931.
Hence the Romance forms and ME, NE serpent fr. OFr., also W. sarff. REW 7855. Loth, Mots lat. 205.
Lat. colubra (> Sp. culebra) prob. : Grk. xvddés ‘crooked’, xuAvow ‘roll’, etc. Walde-P. 2.598. Walde-H. 1.248.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Ir. nathatr, W. pal . ger for *nqzr, Pe ersen ' wee nadrs (éxv5va) ON naor, 1.250) dre, ME (n)addre (NE adder p Ce of use), OHG nat(a)ra oes ter with restriction of use), here ee atrix ‘water snake’ (though et as derived fr. nare ‘swim’), t *(s)né- ‘turn, twist’ in ’ etc. (6.31). Walde-P.
Ir. nathi;
Ob wyrm, ; obs. for ‘snake’), rw (now rarely for ‘snake’ except in lind-
wurm ‘dragon’), all orig. ‘worm’. See 3.84. ON snakr, Dan. snog, Sw. snok, OF snaca, ME, NE snake (displacing ser- pent in pop. use) : OHG snahan ‘crawl’, OE snegl ‘snail’, etc. Walde-P. 1.697 ff. Falk-Torp 1098.
OHG slango, MHG, MLG slange (> Dan. slange), Du. slang, NHG schlange : OHG slingan ‘turn, wind’, refl. ‘crawl’, OE shingan ‘crawl’, Lith. slinktt ‘crawl’, etc. (10.41). Walde-P. 2.714.
5. Lith. gyvaté, deriv. of gyvas ‘liv-
Digitized by Arya Samaj Foundation Chennai and eGangotri
ANIMALS 195
ing’, with curious specialization, doubt- less through ‘animal’ (cf. gyvolis ‘animal’, 3.11). This is the generic word, while angis (above, 1) and Zaltys, fr. zalias ‘green’, are mostly ‘viper, adder’.
Lett. éuska, from a poor imitation of the hissing sound? Miihl.-Endz. 1.425.
6. ChSI., SCr. zmija, Pol. zmzj
#### leaf 231
�� ?
go’.
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri a
CHAPTER 4
PARTS OF THE BODY; BODILY FUNCTIONS
4.11 Bopy 4.12 Skin; Hipp 4.13 FLesH 4.14 Hair 4.142 Brarp 4.15 Butoop 4.16 Bone 4.162 Ris
4.17 Horn 4.18 Tam
419 Back 4.20 Hap 4.202 Sxuiu 4.203 Brain 4,204 Facr 4.205 ForEHEAD 4.206 EyEsrow 4.207 Jaw
4.29 Turoar 4.30 SHovutprer
4.32 Ersow 4.33 Hanp 4.34 Fincer 4.342 Taumes 4.35 Lxc 436 Kner 4.37 Foor 4.38 Tor 4.39 Nar 4.392 Wincg 4.393 FeaTaer
AND CONDITIONS
Breast (Front of Chest)
Breast (of Woman)
Upper (of Animals)
NAvEL
HEART
Liver
Betiy; Sromacu
Woms
Kae
TESTICLE
Prnis
Breatuy; BREATH
Yawn, Garp
Coues (vb.)
SNEEZE (vb.)
Swear (sb.)
Spit (vb.)
Vomir (vb.)
Bite (vb.)
Lick (vb.)
SLEEP (vb.; sb.)
Dream (sb.)
WaXxe (trans. and intr.)
Break Winn, Fart (vb.)
Urinats; Urine
Vor ExcremEnt; EXcREMENT, Dune
Have Sexvar Inrercoursn
Bzcer (of Father)
Bzar (of Mother)
PREGNANT
ConcEIvE
Live; Livine; Lirn
Dis; Drap; Dears
Kru,
Corrsz
Bury (the Dead)
GRAVE
Strong, Micuty, Powerrun
Weak
Wet; Hravra
Sick; SrcknEss
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ee
ar7s OF ae
WwW OUND (sb-)
gg Cone, HEAD 4 PuysiclAN MepIcIne, Drue Poison (sb.
joi ‘Tine, WARY 4.92 Laay
Words for parts of the ‘ch a rather large apnea
: form a distinctive is pac ea De Aid tacan a en of their extensive second- es uses. They have been exhaustively discussed for certain fields!, especially the Romance, where it has been noted that, with the inclusion of the dialects, there are some four hundred words an- swering to about eighty in Latin.
Many of the words belong to inherited groups reflecting definite IE terms for parts of the body both external and in- ternal. A considerable familiarity with the latter, gained through the dissection of animals for food or sacrifice, is com- mon among primitive peoples and is not surprising for the IE period.
In the case of such inherited words the Toot connection, and so the semantic source, is in large measure obscure. So far as. we can judge from the words whose etymology is clear, the underlying notion 'S more often relating to the position or Tae the part than to its function. riasaks erited words for ‘eye’, ‘ear’ Nose’, ‘mouth’, ‘foot? are not en d from any of ee erive
sual verbs for ‘see’,
1g Zann Reallex, S.v. Kérperteile. betisile Roe omanischen nlemien: der Kér- 0.
eyerLibiee see 14.3394
Pertej] z 7 eubenen 6
121-16" im Romanischen, Wact, Mis an
#### leaf 232

pinpolet, GRM 14.295 ff,
€n Anpelsa’p—.° Namen der Kg i i ng lsacksen, Diss Kiel Loy elle bei
Ge i ag Idson, Manic, Digs Chicas or the Body in Older
Digitized by Arya Samaj Foundation Chennai and eGangotri
5 BODY; BODILY FUNCTIONS AND CONDITIONS 197
4.93 Bap
4.94 Lamp
4.95 DEAF
4.96 Duns
4.97 BLIND
4.98 DRUNK
4.99 NaxKep, BARE
‘hear’, ‘smell’, ‘speak’ (or ‘eat’), ‘walk’, and so far as some cognates of the for- mer are applied to function this is prob- ably, and in most cases certainly, sec- ondary. On the other hand, the deriva- tion of the IE word for ‘tooth’ from the participle of the IE root for ‘eat’ seems too obvious on the formal side to be dis- carded, though even this situation may possibly be the result of a secondary as- sociation (see 4.27). The application of words for ‘tongue’ to ‘speech, language’ is almost universal, but the latter use is always secondary.
However, there are also examples enough of words for parts of the body derived from a function, as ‘hand’ from ‘grasp, gather’ (4.38), etc. and, regard- less of priority, a relation between organ and function is widely observed.
There is frequent shift of application between words for parts of the body that are adjacent, of similar relative position, associated in function, or through common figurative uses with reference to the emotions. So between ‘head’—‘horn’ (from ‘summit’); ‘head’— ‘skull’—‘brain’; ‘mouth’—‘jaw’, ‘throat’, ‘cheek’, ‘chin’, ‘lip’; ‘neck’—‘throat’; ‘shoulder’—‘shoulderblade’—back’—“‘arm’ ; ‘hand’—‘arm’; ‘foot’—‘leg’; ‘finger’—‘toe’ ; ‘belly’—‘womb’; ‘breast’ as front of the chest—‘woman’s breasts’; ‘heart’ from ‘soul’ (Rum. inimd, 4.44) or ‘bowels’ (W. calon, 4.44).
With such obvious exceptions as
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
198 SELECTED INDO-EUROPEAN SYNONYMS
‘hand’ or ‘horn, tail, claw’, the parts of the body correspond for man and beast and are generally expressed by the same word. But in some cases the etymology indicates that the original application was to one or the other. Words for ‘head’ that are based on the notion of ‘top, summit’ were most distinctly applicable to the head of man. Of the words for ‘back’, those connected with the notion of ‘rear, b
```


### [2026-09-07T20:19:27.583Z] TOOL RESULT

```
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
812:os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PALISADE, PEEL’, POLE?; IMPALE, TRA- VAIL, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English
```


## [2026-09-07T20:19:39.258Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if '4.16' in p and 'BONE' in p.upper() and 'ost' in p:\n        print('#### leaf',i)\n        print(p[:3500]); print('-----')\nEOF",
 "description": "Find Buck 4.16 BONE section"
}
```


### [2026-09-07T20:19:40.717Z] TOOL RESULT

```
#### leaf 242
et. éap, lap (jap Hesych.); OLat. aser, assyr (Paul. Fest., with as- saratum ‘drink of wine and blood mixed’); Lett. asins; Skt. asrk, gen. asnas; Arm. ariun; Hitt. eshar (with derivs., Sturtevant, Hitt. Gloss. 37); Toch. ysar (SSS, 6).
2. IE *krew-, *kri-, etc. Walde-P. 1.478. Ernout-M. 234f. Walde-H. 1.294 f.
Lat. cruor ‘blood from a wound, gore’ (as distinguished from generic sanguis; cf. also cruentus ‘bloody’); Ir. cri, NIr. cro, W. craw (obs.), Corn. crow, all used mostly like Lat. cruor; Lith. kraujas, OPruss. craujo, krawia, ChSI. kriivt, etc., the general Balto-Slavic (except Lett.) word for ‘blood’ : Grk. xpéas ‘meat’, Skt. kravis- ‘raw flesh’, Av. zra- ‘raw flesh’, Skt. krira- ‘raw, bloody’, Av. See ‘bloody, fierce’, OF hréaw Taw’, etc.
3. Grk. afua, etym.? Possibly con- nected with certain words meaning
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
‘drip’ or ‘juice’. Walde-P. 2.464 ¢. Boisacq 24.
4. Lat. sanguis (early neut. sanguen) ~inis (> the Romance words), etym.? Connection with Skt. asrk, asnas, ete, (above, 1) too complicated to be con- vincing. Cf. refs. in 1, above.
5. Ir. fuil (beside fuili ‘bloody wounds’) : W. gweli, Corn. goly, MBr. goult ‘wound’ (W. gweli formerly also ‘blood’, as still in rhed-weli ‘artery’, cpd. with rhed ‘course’), Lat. vulnus ‘wound’, ON valr, OE wel ‘the slain on the battle- field’, etc. Walde-P. 1.304 ff. Pedersen 1.139, 162. Loth, RC. 41.208.
W. gwaed, Corn. gut, goys, Br. gwad, perh. as ‘blood’ fr. ‘vein’ : W., Corn. gwyth ‘vein’, Ir. féith ‘fibre’, etc. (Walde- P. 1.224, without inclusion of the words for ‘blood’). Henry 146.
6. Goth. b16p, OE bléd, etc., general Gmc., prob. as ‘that which bursts out’ : Goth. bléma ‘flower’, etc. Walde-P. 1.177. Falk-Torp 83 f. Feist 101.
NE gore, used much like Lat. cruor, fr. OF, ME gor(r)e ‘dung, filth’. NED 8.V.
7. Lith. kraujas, ChSl. krivi, etc., above, 2.
Lett. asins, above, 1.
8. Skt. (Vedic) asan-, asrk, above, 1. .
Skt. rakta- neut., sb. use of rakta- ‘red’, pple. of raj- ‘be colored, be red’. Likewise for ‘blood’ neuter forms of other words for ‘red’, as rudhira-, lohita-, conita-. Cf. ON rodra ‘sacrificial blood’ beside rjodr ‘red’.
Av. vohuni- (NPers. xin ‘blood’), etym.? Barth. 1434.
Digitized by Arya Samaj Foundation Chennai and eGangotri
qm BODY; BODILY FUNCTIONS AND CONDITIONS 207
4.16 BONE Goth. Lith. kaulas k gaeor ON bein Lett. kauls Gr OKKaNO Dan. ben, knogle ChSl.  kostt NG 0s Sw. ben SCr.  kost oe 0ss0 OE ban Boh.  kost’ be 08 ME bone Pol. kosé g — fueso NE bone Russ. kost’ an os. Du. been, knok Skt. asthi- Ir. a OHG bein Av. ast- Tr, ond MHG bein v. Cae NHG  knochen (-bein) Br. ask + from the inherited group, words NHG knochen, fr. MHG knoch knoche, ne ‘knuckle, knot’, this with dim. MLG
for ‘bone’ come by e
-----
#### leaf 243
eualizetion. Sem or through terms denoting a particular hone, esp. ‘knuckle-bone’, or by exten- sion of ‘hollow stalk’, to the long bone of arm or leg, or by extension of the hard ‘kernel’ of fruits to the analogous parts of the body.
1, IE *ost-, etc. Ernout-M. 716.
Grk. dcréov; Lat. os, gen. ossis, also ossu, ossum (> It. osso, Sp. hueso, Fr., Rum, os); W. asgwrn, Br. askourn, Corn. ascorn; Skt. asthi-, gen. asthnas, Ay, ast-, asti-; Arm. oskr; Alb. asht. Here also ChS]. kosti, etc.? See below, 6.
2, NG xéxcado neut., fr. Grk. xéox- kahos ‘kernel of the pine cone’, deriv. of xoxxos ‘kernel, grain, seed’.
3. Ir, cnaim, NIr. cnaimh : Grk. nun ‘leg between knee and ankle’, ee a at the back of the 1.59, , ieee : ae a Pedersen Fenttelele? of ‘bone’ through
4, ; ee cae 8 ban, etc., general ‘ m for ‘bone’ now only
i cpds, as el , 7 \- ie 3 Scure, FalleTorp 60, ); origin ob-
Walde-P. 1.185 f.
knokel ‘bone, knuckle’ (> Dan. knokkel, knogle ‘bone’), ME knokel, NE knuckle, NHG knéchel ‘knuckle’: ON knjikr ‘round summit’, Lith. gniaudzti ‘close the fist’, etc. Walde-P. 1.582. Falk-Torp 69. The meaning ‘knuckle’ is the more general and earlier, whence ‘bone’ only by later extension (not ‘knuckle’ from ‘bone’, asin NED).
5. Lith. kaulas, Lett. kauls, OPruss. acc. kaulan : Grk. xavddés, Lat. caulis ‘stalk’, Ir. cuaille ‘post, stake’, also Skt. kulya- ‘canal, channel, ditch’ (hence neut. kulya- ‘receptacle for bones’, rarely ‘bone’, no direct connection with the Baltic use), with common notion ‘long, hollow shape’. Walde-P. 1.332. Doubt- less applied first to the long bone of arm or leg. Cf. Lat. caulis used by Pliny of the ‘bony part of an ox’s tail’; also the use of ON leggr (4.35).
6. ChSl. kostt, etc., general Slavie : Lat. costa ‘rib’. Further analysis of both as k-ost-, with relation to IE *ost- (above, 1) is attractive but dub. Walde-P. 1.186. Ernout-M. 225, 716. Berneker 582 f.
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
208 SELECTED INDO-EUROPEAN SYNONYMS 4.162 RIB tk.  wAeupdv Goth. .... Lith. Sonkaulis ne seat ON rif Lett. riba Lat. costa Dan. ribben’ ChSl.  rebro It. costa Sw. revben SCr. __rebro Fr. cole OE rib Boh. ebro Sp. costilla ME rib Pol. zebro Rum.  coastd NE rib Russ. ebro Tr. asna Du. rib Skt. parcu-, prsti- NIr.  ecasna OHG rippa Av. parasu- . asen MHG rippe Br. kostezen NHG rippe
The largest group of words for ‘rib’ is connected with words for ‘cover with a roof’, ‘a roof’ and were evidently applied to the plural ‘ribs’ as forming a sort of roof over the interior of the thorax. Some are connected with words for ‘bone’.
-----
#### leaf 244
 The secondary use as ‘side’, etc. is widespread.
1. Grk. wAevpéy, etym.? Boisacq 794.
2. Lat. costa (> It. costa, Fr. céte, Rum. coastd; Sp. cueste as ‘rib’ replaced by deriv. costilla) : ChSl. kostt ‘bone’ (4.16). Walde-P. 1.464. Ernout-M. 225. Walde-H. 1.281.
3. Ir. asna, NIr. easna, W., Corn. asen: Grk. écréov ‘bone’ etc. (4.16). Pedersen 1.85.
(source of Fr. cété ‘side’), deriv. of Lat, costa (above, 2). Henry 77.
4. ON rif, OE rib, OHG rippa, ete. general Gmc. (but Dan., Sw., rev ag ‘rib’ replaced by Dan. ribben, Sw. revben, epds. with ben ‘bone’) : ChSl. rebro ‘rib’, etc. general Slavic, fr. the root seen in Grk. épé¢w ‘roof over’, dpodos ‘roof’, ete. Walde-P. 2.371. Falk-Torp 896.
5. Lith. Sonkaulis, cpd. of Sonas ‘side’ and kaulas ‘bone’.
Lett. riba, fr. MLG ribbe. Endz. 3.521.
6. ChSl. rebro, etc., general Slavic: OE rib, etc., above, 4.
7. Skt. pargu-, prsti-, Av. parasu- : Ch8l. priisz (pl.) ‘breast’ (as region of the
Miunhl.-
Br. kostezen, fr. WLat. *costatum | ribs), root connection? Walde-P. 2.44. 417 HORN Grk. _ xépas Goth. haurn Lith. ragas NG xépato ON horn Lett. rags Lat. corn Dan. horn ChSl.  rogit It. corno Sw. horn SCr. og Fr. corne OE horn Boh. roh Sp. cuerno (asia) ME horn Pol. rég Rum. corn NE horn Russ. og Ir. adarc, benn Du. hoorn Skt. origa- Nir. adhare OHG horn Av. Sri-, srvd- W. corn MHG horn Br. korn NHG horn
Most of the words for ‘horn’ belong to a single group of cognates which in- cludes words for ‘horn, head, summit’, etc. with the common notion of ‘top’. Originally denoting an animal’s horn
and so considered here, most of them are also applied, like NE horn, to ‘horn’ as material and to objects of similar shape, esp. ‘drinking-horn’ or ‘horn’ for blow- ing. But such uses may also be distin-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ARTS or T d by different forms, as Fr. corne, guishe | gee _ jn a variety of formations ae c, summit, head, horn’.
1.403 ff. Ernout-M. 221 f. f >. Grk. xépas (cf. esp. ae si cen thead’), Att. gen. i Dit xépart, etc., whence NG toaT0; Lat. cornil (> It. corno, etc. gen- eT Romance; also Ir. corn ‘drinking- faa W. corn, Br. korn); Goth. haurn, OE aa etc., general Gme. 7 Bit. grniga-, Ay, sri, srva- (NPers. surt horn ); in other senses, Grk. Kapa, Bett giras- head’, etc. (4.21), Lat. cerebrum ‘brain’, Grk. xopvé? ‘summit’, etc.
Keparos,
4,18 Grk.  obpé Goth. NG �
-----
#### leaf 280
kaSa- ‘armpit’, OHG hahsa ‘bend of the knee’, with varied specializations fr. a common notion of ‘joint, articulation of the limbs’; Walde-P. 1.456f. Ernout-M. 226. Walde-H. 1.283. Pedersen 1.34, 78.
Br., Corn. gar = W. gar ‘thigh, ham’, Ir. gairri ‘calves’ of the leg (cf. Fr. jarret ‘hock’ fr. Gallic *garr-), etym. obscure. Henry 129. Connection with Lett. gurnt ‘groins, hips’ (as Bezzenberger in Stokes 107) apparently untenable (cf. Walde-P. 1.557, Miihl.-Endz. 1.684).
4. ON leggr ‘hollow bone of arms and legs’ but also ‘leg’ (> MB, NE leg), esp. in latter sense fotleggr (as handleggr ‘arm’, 4.31), Dan. leg, Sw. ldgg ‘calf (of the leg)’, no certain outside connection, but prob. fr. an IE “*lek- ‘bend’(?) in Skt. lakuta- ‘cudgel’, Lat. lacertus ‘muscle of the upper arm’, and numerous other words with partial application to parts of the body, etc. Walde-P. 2.421. Falk-Torp 631.
ON fotr ‘foot’ (4.37) used of the entire ‘leg’.
ON bein (but mostly ‘bone’), Dan.,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Sw. ben, Du. been, OHG, MHG bein ‘bone, leg’ (also coll. OHG gibeini, MHG gebeine in both senses), NHG bein ‘leg’ = OE ban, NE bone (4.16).
OE sceanca (but esp. the leg below the knee, ‘the shank’, gl. Lat. crus) = Dan. skank ‘shank’, Sw. skank ‘thigh- or shinbone’, MLG schenke ‘thigh’ (dim, MHG, NHG schenkel, etc. ‘thigh’), perh. fr. the notion of ‘crooked’ (cf. Grk, oxédos : axodtds, above, 1): OHG hin. kan, NHG hinken, Skt. khafij- ‘limp’, kanga- ‘lame’. Walde-P. 2.564. Falk. Torp 984 f.
OE scia, gl. Lat. crus, perh. only ‘shin’ : OF scinu, OHG scina, ete. ‘shin, shin- bone’, perh. fr. the root in Skt. chyati ‘cuts off’, Grk. oxaw ‘slit, rend’, as orig, ‘flat piece split off’, then applied to the ‘shinbone’. Walde-P. 2.542.
5. Lith. koja, Lett. kaja ‘leg, foot’, etym. obscure (Arm. k‘ayl ‘step, foot’??). Mihl.-Endz. 2.188.
6. ChSI. golént renders cxédos in Jn. 19, 31 ff., ‘breaking the (bones of the) legs’, the modern Slavic forms meaning ‘shinbone, shin’, etym. uncertain. Ber- neker 320 ff.
SCr. noga, etc. the common modern Slavic word for ‘leg’, but properly, and ChSI. noga in Gospels only, ‘foot’ (4.37).
7. Skt. javigha- (mostly ‘lower leg’; Av. zanga- ‘ankle’) : Lith. Zengli ‘step, stride’, Goth. gaggan, ON ganga, etc. ‘walk, go’, IE *fhengh-. Walde-P. 1.588.
Av. paitistana-, lit. ‘what one stands on, support’, fr. cpd. of sa- ‘stand’
-----
#### leaf 932
ROPEAN SYNONYMS
8. Skt. agri-, above, 1.
Skt. dhard-, Av. dard- (also Uzi-darg ‘with sharp edge’) : Skt. dhay- ‘ringe polish’? BR s.v. *dhara-. Uhlenbeck 136 f.
Skt. anta-, prdnta- ‘end’ (12.35), also ‘edge’.
Av. karana- ‘end’ (12.35), also ‘edge, shore’. Barth. 451.
12.36 SIDE Grk. — wAevpai Goth. féra Lith. Sonas, pusé NG se pepia ON sida Lett. sans, puse Lat. latus, costa Dan. side ChSl.  (rebra, strana) It. lato, canto Sw. sida SCr. strana, bok Fy. cété Or side Boh. strana, bok Sp. lado, costado ME side Pol. strona, bok Rum. parte NE side Russ.  storona, bok Ir. toib, sliss, leth Du. = zijde Skt. pargva-, paksa-, NIr. _—_taobh, slios, leath OHG - sit(t)a, fiara ardha- W. ystlys, tu MHG ssite Av. araéa- Br. kostez, tu NHG seite
Several of the words for ‘side’ were first used only for the ‘side’ of the body and are connected with words for ‘rib’.
‘ribbed’, Fr. c6té, Sp. costado (It. costato ‘region of the ribs’). REW 2280. It. canto ‘edge, corner’ (12.76), also
Others are from such notions as ‘half’ or freq. ‘side’ (cf. accanto ‘beside’).
‘part, region’; and, in general, words for ‘part’ (besides those included in the list here) are often used in the sense of ‘side’.
1. Grk. mAevpat, pl. of devpd ‘Tib’, used for ‘side’ of the body (Hom.-+), then for ‘side’ in general (wAevpé sg. for ‘side’ of the body in NT and N G); simi- larly w)evpé, pl. of rdeupdy ‘rib’, in nar- row sense (Hom.) and later generic, etym.? Boisacq 794.
Grk. pépos ‘part, portion’ (13.23), late ‘region’, NG Hépos, POP. pepid usual word for ‘side’.
2. Lat. latus (> It. lato, Sp. lado, OFr. lez, Rum. arch. laturi), prob. fr, another grade of the root in Lat. latus ‘wide’ (12.61). Walde-P. 2.497. Walde- H. 1.772. Otherwise Ernout-M. 598.
Lat. costa ‘rib’ (4.162), also ‘side’. Hence, through sb. form of Lat. costatus
Rum. parte (replaces older laturi, above), fr. Lat. pars, -tis ‘part’. Pus- cariu 1274.
3. Ir. toib, NIr. taobh, W., Br. tu, etym. dub., but perh. (as *toig”es) : Arm. t'ékn ‘shoulder’, ChSl. stigno ‘fe- mur’, Walde-P. 2.614. Otherwise Pe- dersen 1.116 (: Lat. tibia, Lith. staibiai ‘shin-bone’, etc.).
Ir. sliss, NIr. slios, W. ystlys, cf. Ir. sliosat ‘thigh’, etym. dub., perh. : Grk. mtxas ‘inside of the thighs’, rlocopat (‘cross the legs’ and so) ‘trot?? Walde-P. 2.684. Pedersen 1.84. Otherwise (fr. *stel- in ChSI. sttlati ‘spread out’, Lat. latus ‘wide’) Foy, IF. 6.319 (adversely Walde-H. 1.772).
Ir. leth, NIr. leath (both ‘side’, esp. 28 ‘direction’, and ‘half’, W. adv. led ‘0 part’), prob. : Ir. lethan, Grk. rAarts, ete.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
gpATI AL RE
-----
```


## [2026-09-07T20:19:53.233Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5770,5800p' BRT.txt",
 "description": "Print BRT around ast-"
}
```


### [2026-09-07T20:19:53.284Z] TOOL RESULT

```
'iSsüa  (AP.)'"'  vans^sia  *mastrr}nasca  .  . z^mäoa  hqm.raiiiwayaii  Yt  to.jx;  —  fisii 'tarn  nSit  varsqm  pairi.späili  \.6.2q;   7;
—  yai  nsit  sün}  .  .  a3atf/iqm  °tqm  .  . bannhm  (sA.) /rafasqn  V,  6.46;  —  'ti'a (AP.)  gaonaca  *dmi}'iaca  Ytij.  11;  —  yS süne  .  .  'tanqm'-''  (als  Obj.)  ahmarslanqm da',aiti  . .  yaica  alle  'ti  (NP.)  dälshva arSnte  V./3.3f.;  —  "tfin  .  .  *maslrr/nqm F,_y  c ;  —  ayanhaHiäis  kantlU  asdibls  paili
'<n'a.^/-p>/J/(sd.)V.^5o;  51.  a)  Sing. und  Plur.  'Knochenbau  des  Leibes':  "/J *hutal{lm  . .  lanvö  *huraomm  (sd.)  P.  4^;
—  vlsph  gaüäsca  tanvas.'a  atdiblsca  (als Obj.)  uitäiiqs^a  kihrpas^a  trvliJica  Y.  55, 1.  a)  überhaupt  'stofflicher  Leib'  im Gegensatz  zu  uUäna-  oder  baoriah-:  nöit "laca "  nBit  uStammca  tiöit  baooasca  *rl.- urvisyltt  V.ig.T,  —  vJ  mqm  urvaisayat 'laca'^  ustJnaca  V.si;  —  pasäi  "(as.'a baooan&asca  *vT.urvJstim  Y,  35.  s;  V.  i'.Si, H.  2.  r  7 ;  —  atars  haiidazaili  *ascai>  (AS.) u/tilMm^aV. ^.g;  —  «J;V  '/J  n$il  ustanaAl cinmam  Y.  /2. 3 ;  —  ffm  ahmäkäts  azdi- biscil  uitännUla yatamaidlX.3-].^.  [V,^. 49,  5.8:  lies  astd.vu°\
KompA.;  Ableit.  —  Vgl.  'aslay-,  asimtäl:  — iFlei.  s.  %39r.  —  ai.  äslhi,  ixilhnäk;  mp.,  np. an.  ~  Pü.:  ait,  (lU  V.  4.  $0,  51  und  zu  a): Mn.  —  'I  Thein.  —  ')  Mask.  Form!  Im  An- schluss  an  das  folg.  Wort.  —  J)  S  ^^4-  2  No.  2.
•  g.  a-süra-  Adj.  'unstark,  unvcnnögend': yj  anass»m  xsqnmJng  (sd.)  raditn  *vaHm n?ris  'rahya  V.2_9.<).
gr.  J*vii,-.  —  Vgl.  asis-iila-.  —  Pü.;  an apzar«!)  ™J,  Sü.;  aiäähaimlJyai. ^  i)  Vgl. nnler  iura-  No.  2.
•  j.  a-skvnda-  Adj.  (fem.  'da-)  'ohne körperlichen  Schaden,  ohne  Gebrechen': kanyqm  °dqm  anupayatqm  "ein  Mädchen ohne  Gebrechen,  das  noch  unberührt  ist" Y./^.iS.
Pü. :  aiiaiid,  erl. :  drusi  'gesund'.
•  j.  asCav-  m.  'Unterschenkel,  Wade'; dasitijm  (hSyum)  ks  °cüm'^  V.Ä63— 65*,
KompE.  —  Vgl.  gr.  4)^5;,  ann-  cj.fr.  —  ■) /  S  22  mit  No.  a,
•  j.,  g.  ast-  n.  'Knochen',  von  Menschen und  Tieren:  _>'J  °/j«"  upanh}r?zaUi  siinS vä  .  .  masyehe  vä  V.  t/.io;  5.1Ö,  F._y  i;  — kva  narqm  iriitanqm  azdibls  (als  Obj.) baräma  kva  nidaiäma  V. 6.49;  — yö..
NA.  a
\.  "asta':  yezi  asta  asa  xrdiwa  yezt asia  gas>^aby3  V./?.39.
KachPü,  zii'<i^.{3SPrM.?):  hatar  ast  aAr.U-iA hiS  xral  iieu'ai  haJtar  asl  kai  5  gchän  ofe päii  iu  pa  fräröiith  däict,
j.  'asta-  n.  'Heim,  Heimstätte':  *'tjm^'' ii^ra  fracarsnta pasvas^a  staoräca  masyäca "ein  Heim  schafften  sich  da  Kleinvieh  und Grossvieh  und  Menschen"  V.  2. 1 3.  a)  ins- bes,  von  der  Lagerstätte  der  Hunde:  duye nai^aiti  "tanqm  aiäityS.ai^Aarpi^ra/tqm  däi- tim  akmaiät  hanirsm  i:)r)nuyat"7.\<ie.\taa\ neuniig  nicht  gehörig  gepöegte  (Hunde) lagerstättcn  -  die  gehörige  Pflege  soll  er dafür  beschaffen"  V. /4.17.
Zum  ai.  V.  tiasali;  BtHU  KZ.  29.  483.  —  ai. isla-  n.,  mp.  pah-asl'i,  GOR,  OK.  346,  Bthl. BB.  13.  7a.  —  Vgl.  a»ha:  —  Pü.  {lu  V.  14): /nArtj/"),  (zu  V.  2) :  cigön  pis  ha:  an  büf  a/ar ö  clar  frii  ra/t  nid,  indem  sie  aslim  in  (_>-iilo para  ahmS/\  ai-\-l^m  (lira /ra!*)  zerreisstl); vgl.  No.  I,  3.  —  >>  NA.  as;  t>m  (mit  Inter- punktion dazwischen);  s.  zn  Pu.  Hds.  über- wiegend astjm;  s.  noch  No.  3.   —  ')  Vgl.  zu
dby  Google
*asti.aoJah-
314
faiiä.hasta-.  —  J)  Die  ZerreiEsung  findet  ihre Erklärung  durch  V.  g.  48,  wo  riehtig;  yi&a fata  ahmSj  as;  Aä, .  ,
•  j.  'asta-  Adj.  (fem.  'iä-),  PPfP.:  s.  'aA-. KompE.
•  j.  astaena-  Adj.  'aus  Knochen,  aus Bein  gemacht,  beinern':  nlif  °naeiiya {hszanaäbya)  .  .  ratufriS  N.  /07.
Ableit  aus  as!-.  —  mp.  (Pü.):  asien.
•  ].,  g.  'astay-  m.  'Geselle,  Genosse'' aarahe  mainySus  'ti^(ä\  P.j2'*;  —  y} atsm  drygvaile  .  .  varilaitJ  vaahäu  vä tSi>ain  (sd)  'nm*>  \-33.2;  —  drüjö (bmitni  Aaüya  auA^n  'tayd  "im  Haus  der Drug  werden  sie  sichere  Gesellen  sein" Y.  4t),  11;  —  ^y^t  aibJ.g)in>n  .  .  yavüi vispäi  dräjS  dimänäi  'tayj  ".  .;  sie,  die! Gesellen  im3>  Haus  der  Drvg  fUr  alle  Zeit" Y. 40. II.  a)  bes.  mit  vozista-:  hvs\ idi  masdä  ahurü  väzists  avAaUl  °ti/"dei\ wird  dir,  0  MAh.,  der  nützlichste  Geselle sein"  Y.JI.22;  —  Buyama  ahurahe  mazda  • frya  vaüHa  °tayS  Y,  70. 4;  —  fryefil, växistaAe  'tsis  ratum  ämruyS  airSm  Y.  1 13. 2.  I
li.  ve'-  ätilAay  m.  'Gast';  BtHL.  BB.  1$.   1°,
l^'^  /■  57'>.  —  I'Ö-!  '""<  (»uY.  46,49)%  «/"«; i.  noch  So.  1. —  ')  Pö. ;  ähitciiit;  unklar. — »I  Näml.  des  ärigvanl:  —  i)  Eig.  'fiic  das Haus'.  —  *)  Geselle,  eig.  Saalgenosse,  Hau^ eenosse;  das  ist  der  Gast  ebenfalls. —  Eine falsche  Et  bei  Gdn.  Cama  Mem.  Vol.  140; Tj;l.  tu  'aitaj!-.  Die  Et.  vonBradkes,  der ZDMG.  40.  349  got.  ansis  'Gunst'  vergleicht, halte  ich  mindeat  für  weniger  wabtscbcinlich.
•  j.  'astay-  n.  'Knochen'.
KompA.,  E.  —  Vgl.  ast-i  die  Oberfahrung in  die  i-Dekl.  gehl  vom  AS.  (ai.  islhi)  und AP.  (j.  oiii')  au»;  Bthl.  BB.  15.  38.
•  j.  asta'va-  Adj.  'mit  einem  Knochen Teisehcn';  °v3  vä  taxmahe  mirr/ake pars- nai'SvS..  "wer  einen  Knochen  des  starken Vogels  oder  eine  Feder  (als  Amulet)  trägt .." YL/4.3(S.
Abteil,  aas  asf-,  im  Anschluss  an  den  AS. aslim  gebildet;  paritunt :  aslim  ^^  pannavS  : titare.  —  Vgl.  asfä.Hd-.
```


## [2026-09-07T20:20:52.819Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK au- p78 ===\"; python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (85,86,87):\n    p=t[i]\n    if 'avis' in p or 'wahrnehmen' in p or 'offenbar' in p:\n        print('#### leaf',i); print(p[:2500])\nEOF",
 "description": "Print Pokorny page 78"
}
```


### [2026-09-07T20:20:54.027Z] TOOL RESULT

```
=== POK au- p78 ===
#### leaf 85
esang^  eher  zum  Hochzeits- ruf v^irjv:  andere  Deutungen  verz.  Walde  LEWb.^  u.  suö,  Boisacq  s.  v., wieder  anders  Risch  50).
Lit.  vadinü,  vadmti  ,rufen,  nennen^.
au-e-d'  in  d(J^)rjdd}v  ,NachtigalP  (äßr^ööva'  Scrjdöva  Hes.,  äol.  Scrjdcov  und drjdü),    die    Tiefstufe    ävd-    in    aidi]    ,Laut,    Stimme,    Sprache'    (äol.   ai'cJw
77
^  oho)  (xuödco  ^schreie;  spreche^;  addrjSLg,  dor.  avSasL^;  ^mit  menschlicher Stimme  sprechend'.
au-ei-d'  in  ä{J^)sLSa)  (att.  äöco)  ^sing-e*^  d(J^)oid-i^  (att.  (pörj)  ,Gesang-^, "oidög    Sänger^;  äoidii.iog  ^besungen^.    Anders  Wackernagel  KZ.  29^  151  f.
Toch.  B  loatk-,  AB  ivätk-,  B  ?/ai^/c-  ^befehlen^
WP.  I  251  f.;  Specht  KZ.  59^  119  f. ^  Van  Windekens  Lexique  155.
au-  aue-,  aj:?ei-  ;gern  haben'^;  daher  einerseits  ^verlangen^,  andrerseits be«'LinstigeU;  hilfreich  sein^;  auos  ^Hilfe^
Ai.  dvati  ^verlangt,  begünstigt_,  fördert^  =  av.  avaiti  ^sorg-t,  hilft^  =  air. con-öi  jbeschützt^;  messap.  aftva^xi  ^valere  iubeö?^;  ai.  dvas-  n.  Befriedigung, Gunst  Beistand^  =  av.  avah-  n.  .Hilfe'^  (dazu  wohl  ai.  avasd-  n.  ^Nahrung*^)^ ytrl.  o-r.  iv-Tj'rjg  ^wohlwollend''  ("^'ev-ßfTJg)]  ai.  öman-  ^günstig,  helfend^  =  av. aoman-j  helfend,  beistehend^,  ai.  ömdn-  m.  , Gunst,  Beistand,  Schutz^,  öma-h Genosse^;  ai.  avitdr-  m.  ,Gönner,  Förderer*^  (von  der  zweisilbigen  Wzf.  wie Fut.  avisyati,  Perf.  2.  Sg.  avitha,  sowie  Partiz.  ütd-  und:)  üti-li  ,För- derung,  Hilfe';
arm.  avmn  ,libido'  (Petersson  Et.  Misz.  8);
gr.  -afoveg  im  2.  Gliede  griechischer  Stammnamen  (7aov6e)?  Vgl. Kretschmer  Gl.  18,  232 f.,  anders  Schwyzer  Gr,  Gr.  I  487,  3;  521;  ätxäg (Theokrit)  ,Freund,  Geliebter';
lat.  aveö,  -ere  (Basis  auelj,]-  wie  im  vorhergehenden)  ,begierig  sein, heftiges  Verlangen  tragen',  avidus  , begierig,  worauf  Lust  habend'  (davon audeö,  -ere  , wofür  Lust  haben,  aufgelegt  sein,  es  übers  Herz  bringen, wagen'),  avärus  ,geldgierig,  habsüchtig';
air.  con  *  öi  ,beschützt',  cymr.  eioyllys  ,voluntas',  corn.  awell  ,Verlangen', abr.  a-iul  ,ultro',  mbret.  eoull,  youll  ,voluntas',  als  Namenbestandteil  in gall.  Ävi-cantus  (=  abret.  Eucant),  acymr.  Euilaun  u.  dgl.,  ebenso  in  ahd. Namen  wie  Awileih,  Äico]  vgl.  got.  awi-liu])  ^xägig,  svxaQiaTia^ ]  mcymr. ri-m-aiv  ,er  gewähre  mir',  cymr.  ad-aio  (mit  negat.  at-)  ,ve
#### leaf 86
,  ahd.  ödmuotij  as.  öthmödi  ,demütig',  ags.  eapmöd ,demütig',  anord.  audmjükr  ,leicht  zu  bewegen,  willig,  demütig',  audkendr ,leicht  zu  erkennen';  Gdbed.  sei  ,willig',  woraus  ,leicht  zu  machen'; formell  germ.  ^o-Partizip-Bildung  zu  aivi-  (Vorbild  germ.  aupia-  ,öde'?). Recht  unsicher.
Wenn  auch  altlit.  auUis  ,sich  erquicken',  atansimas  ,Erquickung',  lett. ataust  ,sich  erholen,  laben',  atauset  ,erquicken,  laben'  verwandt  sind,  liegt ihnen  die  Tiefstufe  *aus-  des  in  ai.  dvas-y  gr.  h-rjrjg  vorliegenden  es-St. zugrunde.  Oder  =  lit.  dusti  ,kalt  werden',  dusyti  ,kühlen'?
^8  m
Toch.  B  au-läre,  A  oZar  ^Genosse^;  als  zweifelhaft  B  omaute  ^Sehnsucht^^ w-är(ln)-  ,ersehnen'^  A  lo-aste  .Schutz^  mit  angebl.  Schwundstufe  der  Wz; Eher  hierher  wa-  ,geben^,  A  1.  Sg.  icsä  (Pedersen  Tochar.  186).
WP.  I  19,  WH.  I  81,  850,  Van  Windekens  Lexique  9,  79,  153,  157.
8.  au-,  auei-  , sinnlich  wahrnehmen,  auffassend
Ai.  -avati  mit  ud-  und  jpra-  ,auf merken,  beachten^,  aksl.  uim  ,Verstand' (Gdf.  ^au-mo-)]  hierzu  toch.  B  om-palokonne  ,meditation*^?  Anders  Pedersen, Tochar.  223  Anm.
Buis-:  dehnstufig  ai.  ävis  Adv.  ,offenbar,  bemerkbar^,  av.  ävis  Adv. ,offenbar,  vor  Augen^  (npers.  äsJcäi^  ,klar'^;  ai.  avistya-h,  av.  ävisya-  ,offen- kundig^;  aksl.  ave,  jave  Adv.  ,kund,  offenbar^  (im  Ausgang  nach  den Adjektivadverbien  auf  -e  umgebildet  aus  *avh,  wovon :)  aviti,  javiti  ,offen- baren,  kundmachen,  zeigen^  (lit.  ovytis  ,sich  im  Traume  sehen  lassen^ Lw.  aus  dem  Slav.).
Normalstufig:  gr.  aiad-dvouaty  Aor.  aiod-sad-ai  ,wahrnehmen^  (*aA(r-^-); lat.  audio  ,höre^  aus  *auiz-dh-iö,  vgl.  ohoedio  aus  *öb-avizdhiö  über  *oholdiö] gr.  3:t(x)  (Neubildg.  zum  Aor.  e7C-r]ia(a)a^  Kiov)  ,vernehme,  höre'^  (*«/t(J-), STtaioxog  ,gehört,  ruchbar,  bekannt^
Hierher  wohl  hett.  u-uh-hi  ,ich  sehe^,  a-us-zi  ,sieht^,  a-ü-ri-is  (aus  a-ü- wa-ri-is)  , Ausschau,  Warte^,  iterat.  usk-  ,wiederholt  sehend
WP.  I  17,  WH.  I  80,  Tr^utmann  21,  Pedersen  Hittitisch  172  f.
p.  au{e)-,  aued-,  auer-  ,benetzen,  befeuchten,  fließend
a)  au(e)-,  auent-:
Hisp.  FIN  Avo[f\  >  span.  Äve^  ON  A[v]o-hriga]  gall.  FIN  Äveda  >  prov. Äveze  (Gard),  Ävisio  portus  (Alpes-mar.);
ai.  avatd-h  m.  ,Brunnen^  (*awitos),  avatd-h  , Zisterne^  (mit  prakrit.  t  aus  t)^ ital.  FIN  Ävens  im  Sabinerland
```


## [2026-09-07T20:20:54.408Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"avii\\|äviS\\|avis  '\\|offenbar\" BRT.txt | head -20; echo \"=== usi Verstand ===\"; grep -n \"Verstand\" BRT.txt | head -20",
 "description": "Grep BRT for avis and Verstand"
}
```


### [2026-09-07T20:20:54.468Z] TOOL RESULT

```
2788:mrßiUisd.)  Y.^p.Ö;  —  ahutamca  vairim'     gmve  at  amä-.'anJih  bavii. fralsyilmaht    ..    hatnislayaica    ,  ,     Y.  61.   •  j.  ^aesa-  Pron.  dem.  (fem.  °s.i-);  nur  'sä I.  4)    'promittere,    versprechen':    tat  NSm.,f.  und  °Ü>  NSm. 'dieser'  I)  in  stark-
3162:•  j.  a-ciBra-  Adj.  "nicht  offenbar,  undeut- lich': '^nJ  F.  7.
4960:sprochenen)  Gegensatz,  1)  adjektivisch:  rfifa*  . .  aAt^  . .  pasäva'  ka''büjiy^  °vam *°variAe  ainö  .  .  apas^a  zimasca  Yt  75.28;  \bardiyam  avii/d'Bh.  T.io;  —  nadi'tabaira* 42,G.2.8; — para  "vaiüke  ahiS  d^r»höit..'' .  .  abty  bäbirum  asiyavi^  pasäva''  adatn para  'vairiAe  Aü  '^wantS  Y.  if}.&;  —  'vat'-'vam   nadflabairam    agarbäyam  pasära^
5196:i)  Nach  Gdk.  KZ.  28.   187   und  Dst.  ZA.  2. 671  wire  avö  Praev. j.  aviirisyäl:  S.  un-ti^s-.
5371:Zum  V.  ray:  —  Vgl.  aviirila,  ai-wUrifim.  — Pü.;  pa  ras  riyai');  dam  die  Bern.;  ai/  ki ilÖH  gdaiel  iu  andat  x'tslhä  gäi  fl/j/  5  ma-f  «.- tiiiitüt.  —  »)  Statt  r  d  k  ist  wohl  r  d  d  lu lesen,  d.  i.  riyel  (=  np.  riyad).
7395:•  j.  ävistayae-.'ir  Inf,;  s.  unter  wV/iyaJ-Ja. g,,  j.  ävis  Adv.  'offenbar,  vor  Augen': •°    IUI   antars   hlttta    .  .    rätayö  (sd.)  Y.
7790:Ableit.  aus  iahairi-.  —  Pu, :  gihänl»  baviiniA ..k?  an  bavisnih  zäyiin  "vivorum  'futurit»s' . . cui  ilU  futuritas'  gignenda";  etl.:  Ü vusaak it  vuhühH  z^yisn  räh  itnt/ar  afäyil  *'masculuB enim  alque  'mascuUnitas'  gign«ndi  causa necessaria  est".  S.  noch  Dst,  ZA.  /,  445.  — 1)  Sc,  JusTi  -das  Zukiinflige  der  Welt',  DST. 'la  Production  des  etres',  MlLLS  'Ihe  Settle- ments of  the  futuie'. g.  äiiAS,  Si^liö:  s.  iSh-,
8140:•  j.,  g.  ux$a-  I)  Adj.  '(von  den  Göttern) verkündet,  geoffenbart',  xmv  m\t  vahA- n.: im,l  at  °'i„j  vüM  . .  fravaocäma  Y.jj.9;
8143:—  tiiig  zbayS  (sd.)  varthiul  "däii  manatshö Y.  ^f7. 14;  —  'iiMH  trlrpmF.jf.;  —  ra^wya 'da  F.^f.;  —  pjnse  %ioqm  rasnya  '%ahe YL  72. i;  —  gave  n>ms..'}am ..  v^r^'^rpm W  10. 20.  a)  insbes.  'von  den  Göttern verkündeter,  geoffenbarter  Spruch,  ora- culum':  Ayat  xsmä  'oJis  didaitihs  (sd.) paounJm  Y.  43- 1 1 ;  —  y<icä  vohu  'i>ä /rast  (sd.)  mananhit  yjca  asä  anhSus  Y. 44. 8 ;  —  ditidi  *asä  da  *dar3gäyü  prMvdis (sd.)  lü  '(..lis  maüdä  Y.2S.6;  —  aAm 7'oiB  manauhii  °'6il  (IS.)  yilil^  ärmaitis  .  . mazdJr  rapunm  lag^dS  (sd.)  ".  .  der  Ver- kündigung gemäss  .."  Y. 57.20;  —  aitatca aeiqm  'hanqm  uxhs.btrum  {stL)  yiit's  yaz-a fraia  vaece  ,  .  Y.  79. 10;  —  sarai^ustrahe .  .  paoiryäi  hat/hanuse  gqmca  ahmca '<ijm/a  •tiaSyäca^^  sraosjm  xsa&fvmca  Yt 7^.88.  2)  'Rede,  Reden,  Worte*  im Gegensatz  zu  Denken  (Gedanke)  und  Tun (Werk):  nüit  ttä  manä  ..  naaiä  varanä (sd.)  nSil  'hä  naldä  /yaohamJ  nett  daenä .  .  Aacaintl  Y.  45.3;  —  aiüä  hsi  scanta manatihä  'oiiis  fyao^anilisciJ  xsuüm  (sd.) mazda  Y.  5^.  2 ;  — paurvatätsm  (sd.)  mana- i^hascä  vatfhSui  .  .  syao^anakya  .  .  yäcii ^oahyJcä  .  .^  y.^j.  14;  4>8;  —  vanhSui
9086:JrSiä-,^.  ÄS;I  ■""--  ^l!'-  """■-  Snbsl'Wohl,Heil,Grack':  iäl.  i,  rf«,.,,,,,, .  j.  ■ustaviiti-  f.  Name  eines  Flusses,  I !?  .f*""' .!'™  '"°"'  ?''f,  *'  <>»' '»"8« ZnHus!esdesA-«../«W,™,)-Sees:  zrvi,,"'i  '"  "'.',  S™"^.»  "?  H-£-'6-  , yat  kasaim  .  .    avi    tmi    avt.hanlaautt  ...         ,      ,      v  .      ,    _
11319:•  j.,  g.  'äöra-  i)  Adj,  (fem.  °ra-)  'mani- festus,  offenbar,  klar,  sichtbar,  augenfällig': ttü  Im  vTspa''>  °r7(NSm.)  zi''>  mazdanhs.- düm(sd.)  Y.43-i;  —  "nm  ahurim  mazdam Yt.j.  4;  —  ävil  nh  atUar?  hSntü  ..  °rS raiays  (■&&.)  Y.  JJ.  7 ;  —  -ri  (NPn.)  mi'irahe /rayans(sd.)Yt.  10.112;  —  'ra  vS  buyärss masänä  'ra  vö  zatan^.savS  (sd.)  'nm  bsit yäifmÜt  :^ar3n3  .  .  dayata  Ny.j.  n;  in ungeschickter  Verwendung  Vyt.  7f.;  —  "nl (NPn.)  J  kudiiahs  .  .  valdymnai  (sd.)  ■  . Y.J/.  32;  —  °/vm'>  dasvan  bassaz?m  Y. 10.  7.  2)  n.  'Gesicht';  a)  sva.  'Anblick': taica  .  .  awÄÄ/  vahistahe  're  paityanie "und  die  Werden  des  Anblicks  des  Para- dieses teilhaftig  werden"  P.  4g.  b)  sva. 'Anthtz':  yB  paoirys  'nm  urvaäayaia  (sd.) .  .  haolat  Yt.  13.  89;  —  mßinm  ..  *yahmi paiti  'rim  vlhatsm  vJspais  avi  karsvqn Yt  10. 64.  c)  sva.'  Vision,  Erscheinung' : 'ra  (IS.)  msi  dam  *ahUmMLratüm  (sd) ciidi  '^.44-i(>.'  d)  sva.  'äussere  Er- scheinung, Gesammtheit  der  äusseren  Merk- male', spez.  von  der  Menstruation:  ya} kl  'ra  daxst>m  havaiti  yat  kl  daxsta 'r?m  bavaiH  V.  16.  i4[?)^'I  —  s.  Ab- leit*' 3)  'Kundgebung';  vJ  daSväis  .  . sarpm  mruyi .  .  vi  manSbTs  vi  valsbxl  vT syao^anais  vi  'rai/  Y.  12,  4.  a)   sva
11647:Das  Unworl  ist  offenbar  in  Erinnerung  an die  Pü.  von  Jinarqm  V.  S3-  ^  entstanden.
12069:Pä.  (l.St.):  fakUluia,  (3.  St.):  j^aH;  offenbar Restart.  —   ■)  Zum  3  e.  tarAU-  No.  I.
13121:*)  Deren  jede  einem  xia%^apSvan-  unlerstellt war.  —  ••)  Uiw.  an  Grösse  und  Einwobnenahl obenanstehend.      In    SüErl.    zu   Y.  rj.  i    wird gfämah  als  paäiälaHiiaranäriyu^mai  beieichnet; .  unten  zu  Sii. KompA.,  E.  —  S.  auch  immiant-  daüiAtus  EH. —  mp.  i/ei  'Land',  arm.  LW.  äehprl  'Landes- heit',  np.  dih  'Dorr;  ai.  däsyrn^-  m.  hat  ganz abweichende  Bedeutung,  worüber  zuletzt  Gdn. VSt.  j.  96.     —    -Pi.:  lieh,    &h.:gräniah    {yitt offenbar  durch  die  Bedeutung  des  np.  dih  ver- anlasst  ist),   —   ')  Nur  gAw.;   s.  No.  2.    — >)  jAw.  und  gAw.;  s.  No.  1.  —  3)  NA.  daii- hui;  s.  aber  Jp  l,  Mf  2.
13403:*)  Die  Zoologen  des  Awesta  haben  offenbar die  Puppen,  die  die  Ameisen  in  die  Sonne  tragen, für  geraubte  Getreidekürner  angesehen.
13917:Oldenberö  ZDMG.  55.  314,  GnN.  VSt.  j.  i  1  V-  lO.  T,  -  J'aiiit  hl  dva  yaska  avt  aasts (,  dem  offenbar  die  neuere  Litt,  lu  den  vi,\äjasat  V.  7.  70;  —  dvaäna  pike  (sd.) Wörtern  unbekannt  ist).  ^  haämna  Yt.  10. 84;  —  dasa,  ava%ra  tnanhö
14985:•  j,  paitLpIyav-  Adj.  'sich  hütend  vor  -, behutsam,  vorsichtig':  a&avii . .  vttavü . . 'yu/  fiqma  ahmt  Yt.  7,  14.
15895:•  j.  pasfa  'post';  i)  Adv.;  a)  räumlich, a)  "hinten":  p' pavii pars pava  spasvXoaita Yt.  10,46;  F.  ?g;  —  /'  hi  vaylansm  .  . upa.dvqsaiH  "..hinten  auf  seinen  Kopf.." V.^.42;  9.16;  —  yezi  nairyB  anhat  p° fa püurum  (Sp.  872  o.)  paiti.hinMl  paiti^a aparim  V.  ÄgS;  58;  — yezi  aiwySnhana aipi.var)cainti  p°  vä  palri  (t'S)  bar»ttti ^■95-  b)  zeitlich  'hernach,  drauf,  später': pars  *'z?mi  .  .  p°  ■  ■  "vor  dem  Winter  .  ., darauf  .  ."  V.  2.  24;  5.  g.  Ä40,  ii)-  aS^,  N, 1^,  H.j.  s  Var.,  Yt.^8,  Vyt.5,  Vd.72;  — p'    vä  pttiri  (sd.)    va   *paiti.barö  N.  Joy;
16008:1)  Die  Stelle   ist   offenbar  nach  Yt.Ä3i   ge-
16819:mit  *ava"1  und  aw  'Jemandem  (Akk,) etwas  (Akk.)  zubringen,  verschaffen' ;  ^azia"' dim  aviJiarami  aojO  YtÄas;  —  *ava"'> mqm  aviiawryqm  .  .  aojS  .  .  "so  würde ich  mir  verschaffen  . .  die  Kraft  . ,"  Yt.
=== usi Verstand ===
3229:—  'na  (VS.)  miira  Yt. /0.31;  —  mand b(J  voiu  ..  *"«?»!'>''  *'riat'>  xrataot ", .  untrüglich  ob  untrüglichen  Verstands" P.  27».
3234:•  j.  adaoyöjiratav-  Adj.  'des  Verstand untrüglich  ist':  maoyö  aki  •tus  . .  vispö.- vinvh  Vt.  i2.i'K
3286:•  j.  a-8äityo.]fratav-  Adj.  'der  nicht  den gehörigen  Verstand  besitzt,  nicht  recht  bei Verstand  ist'  (vom  Hund):  yat..  sp3  avacä (sd.)  V1I  bavat  "/wx"  V.  y,  29;  31;  — yat .  .  spii    a/iqm.baoii>mn5  vä   bavat  "tu/  V.
5012:•  j.  a-va£ah-  Adj.  'stimmlos*  sva.  'der seine  Stimme  nicht  braucht'  (vom  Hund)": yat  .  .  J/J  'eä  vä  bavat  ohaityBjcratus "wenn . .  einerseits  ein  Hund  seine  Stimme nicht  braucht",  der  (weil  er)  nicht  recht bei  Verstand  ist"  V.  tj.  29;  —  yezi  nöil ipä  "ea..  dijäitySJcratus  pasüm  vä  narim rä  ragfyät  "damit  nicht  der  Hund,  der seine  Stimme  nicht  braucht'*,  weil  er  . ., ein  Schaf  oder  einen  Menschen  zu  Schaden bringe"  V,y.3i.
6752:•  ).  a-ham.baoS^mna-  Adj,  'nicht  wahr-  Oberherm  und  Richter  und  als  den nehmend'  sva,  'der  seine  Sinne  nicht  zu  ersten  Lehrer  der  Menschheit"  Yt. /_J.  1 5  a ; brauchen  weiss'  (vom  Hund):  yat  ..  sfä\ —  ya^a  fr3  loa  (sd.)  ämraot  yat  dim •n<s  Tä  haiat  aoäitySjxratus  "wenn . .  ander- '  ahümca  ratutn^a  ääadat  "'ya^a'  sagt  aus, seits  ein  Hund  seine  Sinne  nicht  zu '  dass  sie  ihn  (näml.  Zar^  als  A.  und  R. brauchen  weiss,  der  (weil  er)  nicht  recht  eingesetzt  haben"  Y.Jfj.u;  Yt  7^.92;  — bei  Verstand  ist"  V.  /_J,  35;  —  yesi  nnl<yailqm  ns  ahurS  maeäh  .  .  vatsks  valaa spS  'nS  mafye  v3  .  .pai'jyäite  aAmai(sA.)\{sA.)  atiqm  zaraiustr5  ankuca  (NS.)'' heüa  irisylt  "sonst  könnte  der  Hund,  der  ratu^ca  Vi.iö.i;  Yt./j.gi;  —  allai  dim seine  Sinne  nicht  recht  zu  brauchen  weiss,  lUsfanam  maziit?m  dazäyli  (sd.)  ahümca in  eine  Grube  ..  geraten"  V.  j_j.  37.  .^ratämca  yim    ahunm    mazdqm    Y.  27.  i;
8686:•  j.  u§-  n.  'Ohr'  uzw.  «^»rischer  Wesen'': k/(NS.)  F.9(?).  A)  sonst  nur  Du.;  a)  'die Ohren':  yezi  *kva£ibya  ''-sibya''^^  aiwi.- srunvaifi  . ,  yezi  äat  nöit  /ivagibya  "Hbya aiwi.surunvait(  N.  i'ö";  Uj;  —  *'sibya F.p'>*>;  —  drimts  .  .  asi  [-//Is)  karma gava  *dvari'^ra  zafan  Yt  jr.2;  —  pairi 'si  vSrayavw»m  kam  gava  nidanzaydmoMii Yt.  j.  27;  —  g?tirvaya  h?  päoave  züvar^ pairi  iS  'si  zvrpnäioi  sk)Hd?m  si  manS kirsnüioi  Y.9.28;  —  °//  ahuralu  mazda yazamaide  darp'^räi  (sd.)  maiirahe  .  . xratüm  .  .  mar>%räi  .  .  hisvqm  . .  fra^'äküi Yt. /.  28.  a)  von  Tieren;  °H  (näml. g>us)  pairi. dar ayänli  (sd.)  daSma  .  .  Vt. 14. 56.  b)  'Gehör*,  d.  i.  Fähigkeit  richtig zu  hören  und  zu  verstehen,  sva.  'Auf- fassungs-,  Verstandeskraft':  ava  pa'oS  ava zastS  ava  °/i  däraydiiwjm  .  .  däityanqm .  . syaoiinanqm  varpzäi  Vr.  75.  1;  —  d<lya ml . .  mastim  spilnö  xsviwrjm  (sd.)  hizi'qm uruiie  -si  xratBiH  .  .  Y.62.4.
8724:■  j.  uäLdaradra-  n.  'Aufthssen  mit  dem Verstand,  Begreifen',  mit  (>en.  oderAkk.: zarazdaitim  . .  'nm  daiuqm  nulzdayasnJm ..  vaivim  Y.  25,6; —  Tjot  daenaya  mlzda- yastiSis  Y.as.is.
10443:winnen,  (als  Ziel)  erreichen':  ^^f/nwriv.,! srirä  baninava  gsrnvnäiti  YtiO.  13;  — j gpr7wnap'>  F. 21.  6)  '("li'  den  Sinnen,] dem  Verstand)  auffassen,  wahrnehmen,! begreifen':  vätd ..yint yava  vJtitn  nSnhaya hubaoStitimim  jigaurva  (iS.)*'  H.2.8;  36; —  Aata.mq'^rfm  taini.parStim  *upairi.- gatubyS  (sd.)  girspDm  Extr.  2;  t—  ka<,a.- mq%räi  ('iraie,  '^ra)  ..g^Dptäi  {'tafie, 'ta)  Extr.  j  (,  y,  4);  —  s.  noch  Jnggnbus' PPtA.   (nur    Äbleit)  Unklar:     *ayi.-
10609:mönnäat  (sd.)  .  .  jyStSul  .  .  'tum  ('Plan')  |  itJ.107 Y-J2.9;  — ya  angrayä  karapanS  urspa- ydntJ  (sd.)  yäcä  'tä  (IS.,  'Absicht')  dus»- xid^ra  .  .  'S:.  48.  10;  —  vT6vä  avoi kava  Orca  ('Absicht')  paraiti  V.  75. 2.  a)  'Geisteskraft,  Einsicht,  Verstand  ; Gedächtnis  kraft,  Weisheit':  mana  'üwa^a ästica  (sd.)  Yt/.  26;  —  tat  müi  'tSui ('Verstand')  manankascä  vTä%?m  (sd.)  Y. .,^6'.  18;  —  hyat  .  .  ma-dj  .  .  gal^ascä tasü  damäsca  (sd.)  . .  -tus'cä  (AP. ;  'Geistes- kräfte').. Y.j/.i  i;  —  data  't^us  ('Geistes- kraft')  ..rdzA^f  vaha  sähtt  (sd.)  mananha Y,  50. 6 ;  —  hvd  -'iwa  ('Geisteskraft')  damis (sd.)  ahm  Y.  _?/.;;  —  vJdva  yai^l  güzrä (sd.)  singha»hg..vai3hsul  °'>:ina  ('Geistes- kraft') mananhö  Y.48.3;  —  aiJ  h^m firasvä  (sd.)  Jiw,?  '>wit  ('Verstand')  Y. 53-y<  —  *vfm4   aiat  hava   -^wa  Y.21
11672:•  j.  Jira-  Adj.  lebhaft,  rasch'  an  Verstand, 'intelligent,  schlau':  anzSJamamm  ..  finrn sbanmnim  ßyäurum  Yt  II).  42.
12440:KonpA.,    E.    —    Et?    Gon.S  Versuch,   der '*daiaä-  und  *dainä-  etjrmologiich  gleichselit -  inm  V.  Väty)-  -  überzeugt  mich  nicht,    S. noch  No.  I.   —   np,  din.  —   Pü.:   den,   Sü.: dätih{%    —    I)  Wo  a?  im  Metram   für  iwei Silben   rechnet;    s.    'dainä-.     Also   wohl   ae ans  ar.  d^i^,  %  St. •  j.,  g.  'daena-  £  Hniieres  Wesen,  geistiges Ich,  Individualität',  öfters  kaum  übertrag- bar"; i)im  gAw.'':^<i/«J  maadapaour- vTm  gai%äslä  la^  'näs^  %wä  manankä xratüica"^  du,  qM.,  zu  Anfang  Individuen schufst  und  Individualitäten  durch  deinen Geist,   und  Verstandeskräfte"  Y.  3t.  1 46.  6;    —    nSit  nä    manä    ,  .   s}ngA3 xraiavö  .  .  varanä  (sd.)  .  .  uxla  .  .  }yi "hanä  .  .  "na  .  .  urvaaB  hacainil  Y.  4$. —  vaauklmcä  °nqm  ..  fstratam .. ärmaitim "^•37-  5i  —  ^^  ^'^  ux^äis  fyao%an3  'tiä (IS.)   a&m  spnvat  (sd.)  Y.5/.  ar;  —  y7 *iat  manS  vahyS . .  aSyaslä  (sd.)  kvö  'nqm iyaoiianacS  valanhScä  V.4S.4;   —  yqm yao/  (sd.)  •nqm  .,  dämyam  *hudJnao^ .. y.44.^;  —  yS  'nqm  vohü  ^sänltä  (sd.) ftananhä  Y.  49-  5 1  —  '?«"  ^^^  dqstvam (sd.)  'nayai  frävao'a  Y. 46^.7;  — frö  .  . a-sä    'na  fradaxsaya  (sd.)  Y.  j^.  13;    — AvB  tat  .  ,  ahtnäi  dazäz  (sd.)  'nayä  (IS.) z-aldMtttö  Y.57. 19";  —  mSnÜl  T  mqtdas- düm  *valds.düm  'näbll  aiyasta  (sd.)  ahBm yJ  . .  Y-53-  s";  — yas/ä  .  .  tarJ.mqsia  ,  . sao^aiUS   Sng  (sd.)   patdU  spmiä    'nä urvahs  .  .  ".  .  des  Saelyant  .  .  Ich  wird ihm  Freund  sein  ,  ."  Y.  45. 1 1***;  —  tJm aAfSfum  . .  'nä  saoiyantqm  yä  . .  urväxiat (sd.)  hyat  .  .  mTedtm  .  .  Y._j4.  '3;  —  yä "nü     vairXm    hanät   mjedtm    asahya  yssa astftt  (sd.)  Y.  54. 1 ;  —  hyai  'na  vakUn yBjpn  (sd.)  mlzdlH.49-  9;  —  ^y<'i  mlSdjm ^trtavai^lm   (sd.)  fradadä^S    'näbyni^  Y. 40.  I  ;    —    harthus  (sd.)  .  .  dadät   aAurS 'fiayüi  va^huyai  Y.  5j.  4;  —  'nayäi  va»- ktiy^i  yqm  ksi  Uyam  (sd.)  äatü  . .  ahuri>
12856:mit  ava  'adhibere,  anwenden',  mit  Inf.: ava  pa})ö  ava  zast!  ava  usi  därayavuDm maxdayasna  .  .  dJttyanani  .  .  iysd^nartqm 7-ar»x3i  (sd.)  "wendet  die  FUsse,  wendet die  Hände,  wendet  den  Verstand  an,  um  .." Vr.  15. 1.
17878:ahmiii paoiryB  malyänqm  «/»««(Augm.)  — äha  hSmfirahia  Sws  ät-hStc^  "so  geh aum  yS  ahurS  .  .  anyS  ^wat  "mit  ihm  denn  mit  deinem  Verstand  zu  Rate"  Y. von  den  Menschen  habe  ich  mich  zuerst, 5^.  3.  3)   'sich  verabreden   Über  — '
22011:—  ya%a  ratsm  ahurs  vastä  (3SPfA,)  . .  |  seinem  Verstand  bewusst  ist:  'wenn  .  .'" ayi  asaya{'i&^  Y.J7.  2;  3^.6;  —  aam  _yj;P.  3/;  —  sp^m  viiu/avaitfm  .  .  äraagpm saota  . .  vlli'ä  alsqm  yasmmca  vahm?mca  (sd)  »iÄK/(NSm.)  apäihisi^A.)  V.-/.  55; ".  .  der  ich  mich  verstehe  auf  .  ."  Vr. ,  54.  a)  ohne  Objekt:  yS  näirikqtn II.  19;  19*.  a)  Kaus.  'erkennen  —,,ctiravaitim,,vl''ovä..vl'iuilm..xiuärä ms&ta  lassen' -.va^.ayatna  F.  S.  a)'etwas,\am  JraaAamaiti  V.iS.6j;  — yS  narvm.. Jemanden  (Akk.)  erkennen  als—'  {Akk.};'  iasyaahe  {sd.)  sarWiäi  daoaiti  vilvä  avat Perf.  auch 'etwas,  Jemanden  (Akk.)  kennen  '  ^«nia  xra%itia  paräiti  (Sp.  153  u.)  V", als-  (Akk.),  wissen  (von -),  dass  -  ist':  ,15.  2.  b)  insbes.  Part.  PerC  a)  Akt "t  yStg ■•  vdista  ..  »rpiailftg  {sd.)  Y.2Ä10;:  'kundig':  sraos>m  . .  yim  aurvants . .  spmta
23951:•  g.  vi-ciiha-  n.  i)  'Scheidung,  Sonderung': aisqmcJt  ä  ahm!  %wahml  mOMda  °^ffi  aipi "von  ihnen  werde  ich,  o  M.,  künftig  von  dir  [ geschieden  werden"  Y. 32.  8 ''.  2)  'Ent-  , Scheidung':  tal  msi  xraiSus  manar»hascä\ '%int  "das  ist  meines  Verstands  und  Sinnes  | Entscheidung"  Y.  46.  iS;  ^  mit  Gen.  obj.: sraotä  *g}us'.<lii'  (sd.)  vahistä  .  .  ävar>na •%aAy3  "das  Beste  . .  für  die  Entscheidung zwischen  den  beiden  Glaubensbekennt- nissen"   Y.  JO.  a'>.  [Vt  12. 1:  lies  vl-
24281:•  j.  'vira-  a.  'Verstand,  Einsicht'*. KompE.    —    np,  vir;    DsT.  6tlr.  3.  183.    — ')    iBed.   t.    SWienAW.    6/.    850.  231    vlrTA
28825:Jtä  litis  syaaianäi  (sd.)  matifil  yaHa  *v3 *haxtnV^  (n'ämL  syao'hanäi)  ".  .  wie  ich euch  dränge  (zu  tun)"  Y._j4.s**;  — *kixsalsa  .  .  kfmcit  ar»hSuS  .  .  affaiA-a daxmaliva  vTkantle  iiA.)  V.  7.  50;  F.  24 {hixial)^^; — Aaxsaya{i%0^.)azfmcit../ra- i>mq  . .  aitihä  damaya  anuniatayai(sd.ya "soll  ich  die  Obersten  antreiben  .  ,?"  Y, S.  j-j—yaka  atim  käcayene  ..  zara^ttitrtm anumatie  (_sA.)  dainayäi  YLj,  18;  105, g.  »6.  zu  ß);  *hixsäne  nanm..  *hixsäne nairikam  .  .  *hixsäru  drt'aiqm  .  .  sqm  .  . nrp3rayan/a  (sd.)  "soll  ich  ,  .  antrei- ben, dass  sie  . .  sich  aneignen''  V.  79. 26.  d)  'Jemandem  zu  teil,  zu  eigen werden,  eignen':  kacaiti  dim  aspahe  aojö Yt  ig.  68;  68I;  —  ttm  kacät  V)ri>r»m  . . aat  ana  vsrihra  hatmnS  (s.  2b)..  Yt J5- S4i — >^i  ttasTm  ..  sig(Sp.  1607  m.) , .  masyä  hacaite  . .  xratui yaira  mthr^mat . .  hacaite  . .  xratus  "es  gibt  keinen  Men- schen .  .,  dem  grösserer  Verstand  zu eigen  ist  als  .."Yt/o.io;.  e) 'in  Be-
```


## [2026-09-07T20:21:15.328Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8686,8740p' BRT.txt",
 "description": "Print BRT us- entries"
}
```


### [2026-09-07T20:21:15.374Z] TOOL RESULT

```
•  j.  u§-  n.  'Ohr'  uzw.  «^»rischer  Wesen'': k/(NS.)  F.9(?).  A)  sonst  nur  Du.;  a)  'die Ohren':  yezi  *kva£ibya  ''-sibya''^^  aiwi.- srunvaifi  . ,  yezi  äat  nöit  /ivagibya  "Hbya aiwi.surunvait(  N.  i'ö";  Uj;  —  *'sibya F.p'>*>;  —  drimts  .  .  asi  [-//Is)  karma gava  *dvari'^ra  zafan  Yt  jr.2;  —  pairi 'si  vSrayavw»m  kam  gava  nidanzaydmoMii Yt.  j.  27;  —  g?tirvaya  h?  päoave  züvar^ pairi  iS  'si  zvrpnäioi  sk)Hd?m  si  manS kirsnüioi  Y.9.28;  —  °//  ahuralu  mazda yazamaide  darp'^räi  (sd.)  maiirahe  .  . xratüm  .  .  mar>%räi  .  .  hisvqm  . .  fra^'äküi Yt. /.  28.  a)  von  Tieren;  °H  (näml. g>us)  pairi. dar ayänli  (sd.)  daSma  .  .  Vt. 14. 56.  b)  'Gehör*,  d.  i.  Fähigkeit  richtig zu  hören  und  zu  verstehen,  sva.  'Auf- fassungs-,  Verstandeskraft':  ava  pa'oS  ava zastS  ava  °/i  däraydiiwjm  .  .  däityanqm .  . syaoiinanqm  varpzäi  Vr.  75.  1;  —  d<lya ml . .  mastim  spilnö  xsviwrjm  (sd.)  hizi'qm uruiie  -si  xratBiH  .  .  Y.62.4.
KompA.  {Uli').  —  Vgl.  iBcd.  vonFieelinger KZ.  2/-  33S !  f«"!«'  ßß-  ■'*■  *S.  IFAni.  6.  47. IF.  7.  223,  WZKM.  9.  82,  IF,  //.  127,  Hbm. AGr.  /.  216.  —  mp.  (Pü.)  u!,  arm.  LW.  ui, np.  Affi;  s.  dazu  GliPh.  /  b.  36;  lat.  vgl. auri'S.  —  ')  Im  Gegensatz  zu  karma-.  — ')  zFlei.  s.  S  223{.  —  l)  Hds.  'iyi;  s.  No.4- —  4  )Hds.  ahifyii,  ahitiyö  (s.  No,  3);  aber  unter den  Wörtern  mit  anlaut.  u\  Pü.  fehlt.  — S)  In  den  Teit  geratene  Glosse   zum  folgcn-
■  j.  uäaoma-  m.  Name  eines  Bet^s  oder Gebirgs:  ahmat  haca  garayö  fraoxsyqit , . 'masc'a  Yt-ig.i Et.  und  eig.  Bed.?
dby  Google
415
uäaSa-
uävuru-
416
•  j.  u§aSä-  C  Bezeichnung  eines  Teils  des Rückens  (?)■>:  -iam  F._jg.
El.  und  Bcd.?    —   FB.:  piist  i  In  'der  spitze
Rücken'.  —   ■)  Vgl.  vaahä:
I.  uiahärii
Bb.  .
18;  lies  tthrab'.
•  j,  u^as'tara-  Adj.  'gegen  Morgen  ge- legen, östlich':  °taire  kinävd  (sd.)  , .  daosa- taire  V.57.29;  —  haca  °lara  hindva  (sd.) avi  daosaslanm  hindum  V.J.  18  PüZ.;  — -taräl  haca.  nalmitt  °taraalyi>  haca  nai- maiibyS  V.  ig.  5,
Ableit.  aus  HsaA-,   E.  Bthl.  Slud.  7.  58.  —
mp,  (Pö.)  iiiastar  (Pai.  Ms');    vgl,  »hd.  cslar, Bgs.  iaslerra.
•  j.,  g.  uSah-  :  uä-''  f.  1)  'Morgenröte, Morgen':  kS  yi  'Sa  (NS.)  arSm.ptiwä (sd.)  xiapsca  Y.44.$;  — ■  ayram  usailTm 'sirihtm  Yt/4-2o;  — /räymat  *s3nA?m süraya  *i'ft'i/f/«  (sd.)  Yt.  J.62;  62,  /5.S5;
—  tiärTm..y!f  avaf,at  frafasüiie  xssi>nyat "his  (lies  hacaf)  'säy.V  (AblS.)'>  Vti'.as'i
—  'saiihqm  para  frSritSii  FrW.  /0,4i ;  — ytzi  xsapsAva  mpr^ncaiie  (sd.)  'lakva bisazyat  V.  l'7.3J  —  uü'  (LS.).  A)  als weibliche  Gottheit  gedacht:  'sqm  (AS.) sriram  yazamaide  'säuAfm  . .  xsSi'inJm ravaLaspqm  .  ,  "säPikem  .  .  nvim  ranjat.- aspqm . .  avqm  'sqm . .  G.  5. 5.  a)  Name der  fünften  und  letzten  der  (priester- lichen) Tages  abteilungen*';  vupim  paiti "sauham  ä  kB  vaxsat  "immer  in  der Morgenfrühe  bis  Sonnenaufgang"  V.  /y. I.  3)  mit  süra-  Adj.  Name  des dritten  Abschnitts  der  Nacht**':  hö tiurr/ö  (j'S  parö.dars)  väHm  baraili  upa 'iaukim  yqm  särqm  V,  iS.  15;  —  'sqm särqm  V.2j\}.
*>  Die  von  Mittemacht  bis  Sonnenaufgang reicht  und  in  uSai-  (sd.  3)  sünU  und  rao/a/i/iiim fragalay-  (sd.)  lerlaÜt;  vgl.  'aiahna-,  F.  3/  b, N.  46  und  DsT.  ZA.  i.  zSl,  sowie  die  FüGI. lU  ul  und  u!  1  arinär  V.  rj.  1,  18.  IJ:  /a  n^m sap  iizäyil.  —  '*)  Der  von  Milleinachl  bis  lum Tagesgraucn  reicht  und  zusammen  mit  raolanhqm /iHi;alay-  (sd-)  die  fünfte  Tagesabteilung  uia/i- (sd.  2)  bildet;  s.  oben  *).
KompA.  (usi-\  E.  ^s.  ufaoSaDhia-);  Ableit.  —
ai.  Ufas-  t.  (AS.  Ufatam,  usaiii,  GS.  u}tiA);  mp.
(PiL)  ui3>  (Päi.  ei).   —    ')  Vgl.  WM.  AiCr.
II.   —    >>  Neubild,  zum  AS.  uS/im   nach  di
ä-Delil.  —   ä  Vgl.  kLbs.  Hbm.  IFAni.  6.  38,
HORM  GlrPh.  /  b.  36.
•  j.  'uäahina-  m.  Gottheit  der  fünften und  letzten  der  (priesterlichen)  Tages- abteilungen*':  'n.m  a/m-amtn  asahe  ratüm
Y.2.7,  0.5.5;  -  -näiy.i.j,  G.j.i;  —
'na  .  .  ratvB  Y.  i.ao.
*)  Genannt  iisak-,  sd.  a.   Vgl.  noch  Bd.  25.  9
{hai  rifm  iap  läi  slämi  afailäk  iavtl),  N.  .46  und
Ableit.  —  Abteil,  aus  uSaA:  —  Pü, :  Iransskr- ; Sa.  erL:  afaräidharälrasanidAjiali.
•  j.  'u^hina-  Adj.  {fem.  'nä-)  'den Usakina  betrefiend,  ihm  gebührend'; kahmat  haca  'hinanqm  gä^anqm  ratufrU fiajasaiti  li.46.
Ableit.    aus    lu'sahina-   mit  Verschiebung  des Hauptions  (?).  —  Fü.:  Iransskr. j.  uH  raoiai/i   V.  lg.  28 :   lies  iisi.raoc' ;  s. raak-  No.  I.
•  j.  uäi.dam-,  u§i-dain-  tn.  Name  eines Gcbirgs*':  ahmat  haca  garayS  fraoxiyan '0.1  (NS.)')  usi.äar?nd  {i±)  Yt/^.a;  — gairis  yU  °6<j  Yt/p-66;  —  aom  gairuii.. yim  °dam {fuS.y*  usi.darfmm (sd-)Mt.  1.2S.
*)  Dm  seine  Wasser  zum  /ßi/iin-See  schickt und  ösdicli  davon  gelegen  ist,  s.  SteIH  IA.  /£. ai,  DsT.  ZA.  3.  634.
Eig.  'der  sein  Haus  io,  bei  der  Morgenröte hat',  Komp.  mit  LS.  (zuiiSai-)  im  1. Glied.— Pü.:  IIS  diisljr,  erl.;  api  maziyTnll.  —  ')  Vyl. iUex.  S  402.
■  j.  uäLdaradra-  n.  'Aufthssen  mit  dem Verstand,  Begreifen',  mit  (>en.  oderAkk.: zarazdaitim  . .  'nm  daiuqm  nulzdayasnJm ..  vaivim  Y.  25,6; —  Tjot  daenaya  mlzda- yastiSis  Y.as.is.
Komp.  mit  ND.  (s.  »/-)  im   1.  Glied.  —  Pü.:
IIS  ,l,tilJtlA.
•  j.  u§i.dar3na-''ra.  Name  eines  Gebirgs"': ■lAmat  haca  garayS  fraoxsyqn  uHua  (sd.) -no  Yt.  i^.a;  —  aom  gairlm  .  .  yim  u/i.- dqm  'tum  Yt.  /,  28;  —  gairlm  'mm  maz- daoahm  ala:fa^r?m  yazatim  Y.2.14;  — garöiS  'nahe  Y.7.14,  22.26.
*)  Andrer  Name  für  iiJi.ii<iM-(sd.)i  die  Namen bedeuten    auch  wesentlich  das  Gleichen,   s.  u. In  Vi.  /.  2%  und  ig,  2   werden    beide    Namen verbunden,  um  das  Gebirg  zu  bezeichnen. Eig.  'der  seinen  Aufenthalt   bei  der  Morgen- röte hat,    nimmt',   Komp.  mil  LS.  (zu  iiiaA-) im  I.  Glied.    —    PQ.!    ui  däStär,    erl,:   Jtusf därcl;  SO.  erl.:  ta  girih  yai  cailanyam  tnaiius- yäiiäm  sthätie  dadhäli  takfatiat.  —    'j  In  NA. auch  ungetr.  —  ')  In  Pü.  gleich  gegeben.
•  g.  u^aurü-,    U^urü-  f.  —  ?— ":  kuirä
tßi  aridrä  (sd.)  .  .  ysi  vanhSus  vazd>na (sd.)  manauhö . .  aspSncit  sildrJcU  caxray3 (sd.)  'S3ura  (IS.)  \.34.T,  —  hamSm  tat vahiitäat  y!  's'urvye(DS.)  syasclt  (sd.)  dah- mahyä  Y.  J2.  r6.
zSchr.  s,  S  2ÖÄ  9,  wonach  ar.  *uhitü-  anzu-
dby  Google
4»  7
uä^
uStana-
418
setzen  wäre,  ein  höchst  fragwürdiges  Gebilde. —  Pä.!  fraif  uiih'),  erl.!  dättäi  usih;  Sü,; Pflhulacaitanyam,  vipiilacailaiiyam.  —  i)  Deu- lungsveisuche,  alle  verfehlt,  bei  Gdn.  KZ.  zS. 164  ('Bemühung,  Streben,  Eifei'),  Bn.  Stud.  r. 464  {'Veistand'),  Dsr.  ZA.  /.  342,  153  ('in- tetligence',1,  Mills  G.  486, 503  ('wide  enlighte- ment,  wide  apprehension',  danach  Kanqa Dict.  'Wide  mental  light').  —  '»  Weil  n us—\-um-  letiegte,  nach  Mills  'a  descriptive compositum  with  the  adjective  last',  was  ihm möglich  erscheint.
•  j.,  g.  u£ta  Adv.  'nach  Wunsch,  wie  es gewünscht wird':ri>AB  uxsy3(sd.)  manaukä ..  -ta  tanamW.jj.  10;— '/S  aAmaiyahmüi ui/,1  (sd.)  .  .  matää  dayät . .  tjvlslm  *gat.- tei  (sd.)  vasiml  Y.  43.  i ;  benüut  Vyt 5?>  —  rapBisla  tu  nS  äar?g?mla  °läcä \.4i.4;  —  vasas/a  tß  .  .  'läca  xsaisa V. Ä5;  —  darrfim  jva  Ua  jva  A.  J.  12; —  °la  ahurim  mazdqm  yazamaiäe'Vx.tS. 1;  i^;  —  °/a  astt  'la  afimsi  hyat  asäi vahistiii  as)m  (sd.)  Y.  2".  14;  —  'tä attusalibyB  sp>ntalibyS  yazamaide  Vr.  13. I  (?);  —  mit  Gen.  subj.:  ahä  nS  sazdyäi (sd.)  -ta  Y.  57. 16;  —  'ia  ta  sStS  aiirava .  .  iarai:uströ  Yty.94'\  a)  mit  astt 'er  befindet  sich  .  .,  es  geht  ihm  nach Wunsch';  ySng  usvakl  *°tä  stoi  (sd.)  Y. 46'.  1 6.  A)  als  Subst  'Wohl,  Heil,  Glück': iynt  aksya  (sd.)  dngväitl  °tä  yJ  as3m äädrl\.^i.%;  —  -ta  buyäl  ahmai  naire yas»  . .  Y.  62. 1;  F.g,  Vyt.  jo ;  —  mtatsüm nimravaite  tistryd  . .  °ta^  ml . .  °ta  ä.baväl "..  Heil  wird  mir  zu  teil"  YtÄ'.ag;  — mit  Ellipse  des  Verbs:  'ta  i^a  (i yö  .  .  "Wohl  dir,  o  Manit,  . ."  V,  7.  52; Y.9. 25,  Yt. /7.7,  Vyt. 5.?;  —  'ta  ahmäi naire  mainyäi  . .  yahmai  . .  säär>m  ahmäi naire  mainyai  .  .  yahmai  .  .  "Wohl  dem Manne,  so  denk  ich,  dem  .  .  Weh  dem Mann,  so  denk  ich,  dem  ,  ."  Yl  10. I37f.  a)  mit  asil  "es  ist,  wird  wohl, guf:  ai  aipT  läis  attkaitJ  °tä  "dann  wird es  künftig  woht  werden"  Y.jo.  11.
KompA.;  AbleiC.  —  LS.  ans  ustay.  —  Vgl. uift.  —  Pü. :  itP^eai,  nta/atiA,  fa  nctcaiiA.  — .)  Vgl.  «i,J^^,^..
•  j.  üita-  Adj.,  PPfP.:  s.  vas-. Korop.A-;  Ableit.
```


## [2026-09-07T20:21:47.117Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG auš ===\"; grep -n \"aoša\\|\\*auš\\|HauŠ\\|\\*Haus\\|to burn\" CHEUNG.txt | head -25",
 "description": "Grep Cheung for auš"
}
```


### [2026-09-07T20:21:47.167Z] TOOL RESULT

```
=== CHEUNG auš ===
492:*saucé ‘to burn, light", *rai9! / *frait/9 ‘to die, decompose’, *caud / *paud ‘to run’. 
2635:*CHORESMIAN: (+ *4-) m/’br’z- ‘to burn, light up’, (caus.) m/’br’zy- ‘to lit (fire)’; 
2640:*MISC: Огт. bras-/brastak ‘to burn [intr.]’ = brés-/bréSok, bróxtok 
2719:*PARTHIAN: brynz- ‘to roast, bake’, bry- ‘to burn [intr.]’ (< *brjia-, with disappear- 
4381:paóu/üs ‘fire-brand’. 0 Wa. pióis-/pióon- ‘to burn, flame up’, cited by Morgenstierne 
4544:*daj ‘to burn’ 
4546:*AVESTAN: YAv. daZ- ‘to burn’ (on daZ- < *daji- see Martinez 1999: 130) || (+ 
4547:*apa-) ‘to damage by burning’ || (+ *ham-) ‘to burn’. > Av. daZ-, with -Z-, derives 
4554:*MIDDLE PERSIAN: BMP dc- /daz-/ ‘to burn’ = DMMPP: 146 
4563:padas- (padajs-) ‘to burn [tr.]’, OKh. padis- (pandis-) ‘to catch fire’, dag- (das-) ‘to 
4585:*SANSKRIT: dah ‘to burn’ (RV+) = EWAia I: 712 
4587:«PIE Sieg. ‘to burn’ = LIV: 133 f. | Pok.: 240 f. 
4589:*IE COGNATES: OCS Zego, Lith. deen ‘I burn’, Toch. tsäk- ‘to burn’, Lat. foveo 
4760:The derivation from the root *daj ‘to burn’, mentioned by Shahbakhsh: s.v., is 
5422:*dauH! ‘to burn’ 
5424:*OLD PERSIAN: ? Oav- ‘to burn’ (Steve 1975: 8 ff.) 
5429:perfume; burn’ || (+ *pari- ?) OKh. pathai- (pathu-) ‘to burn up’ || (+ *ni-) nado ‘fire’ 
5440:or *pari-) CSogd. pr0w- ‘to burn, singe’ 
5444:*CHORESMIAN: Ow- (intr.) ‘to burn’, 0^wy- (tr./caus.) ‘to burn’ || (+ *upa-) bOw- ‘to 
5449:Өїа, dawon-d (caus.), Yzgh. tax”-t, tox" an- (caus.) ‘to burn’, Wa. 0aw-/0ət- ‘to burn 
5454:*MISC: Par. thi- ‘to burn’, (ppp.) Par. thói ‘burnt’, (caus.) Par. théw ‘to light, burn 
5457:*SANSKRIT: dav ‘to kindle, to burn’ (AV+) = EWAia I: 707 
5471:«PIE *deH;u- ‘to burn, be(come) on fire ?? = LIV: 104 | Pok.: 179 f. 
7723:*SANSKRIT: ghar- ‘to burn’ (Dha.) > EWAia I: 514 
7732:Lith. garéti ‘to burn’, Goth. brinnan, Engl. to burn, Alb. zien ‘cooks’, etc.
```


## [2026-09-07T20:21:48.539Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (29,30,31):\n    print('#### leaf',i); print(t[i][:2200])\nEOF",
 "description": "Print Hübschmann p.19"
}
```


### [2026-09-07T20:21:49.846Z] TOOL RESULT

```
300
#### leaf 29
— 19 —
124. Vgl. Horn p. 254—256. Danach steht ein neup. ang
*Biene*') fest, aber der etym. Verknilpfung mit lat.
apis, gr. ^/ttntg, ahd. imbi stehen erhebliche Schwierig-
keiten im Wege. — Afgh. gahUna *Honig' halt Geiger
jetzt fiir original 2), im Kurdischen lautet das Wort
auch gwln Socin, kurd. Samml. II, p. 332.
126. Lies skr. Angara^,
128. Ich kann die Begriffe ^unsterblich' und *suss' nicht ver-
einigen und trenne^) daher die W5rter: 1) np. ndS
*grati saporis, suavis, dulcis', n^n *HebIich, wohl-
riechend*, arm. LW. anoi§ wohlriechend, schmackhaft,
angenehm, lieblich'; 2) np. noS 'aqua vitae', nOS^ddru,
nos-giyd antidotum', paz. anos antidote' Shk. 230, phi.
anOs ^Unsterblichkeitstrank' Art. Vlr. 10, 5, and§ak
unsterblich, unverganglich' BE. 4, 45, zd. anaoSa-
unsterblich', arm. LW. anusak unverganglich, unsterb-
lich, ewig*. Np. a/noSa *heir! urspriinglich wohl =
*sei unsterblich*!
131. Darmesteter's Etymologie (avdm *Schuld' = a^a
+ ama, lat. abemptum) brauchte kaum erwahnt zu
werden. Denn einmal liegt die Wzl. am nehmen' im
Arischen nicht vor, ferner passt die Bedeutung: *An-
lehen, Schuld' nicht zur Etymologie, endlich steht die
iranische Grundform nicht fest, da sowohl *apama
(— np. vam, bal. LW. vdm) wie dpama (np. avam,
paz. avam *Anlehen' Min. Cap. 2, 63 = phi. ipam Phi.
Min. p. 8, Z. 1) angesetzt werden kann. Wo findet
sich iibrigens np. ai?flm? Die Form fam siehe J HAS
1894, p. 432.
132. Np. ^obdS" liederlicher Kerl, Gesindel' liegt als LW.
im Afgh. in der Form aubos vor und wurde so wohl
auch im Persischen gesprochen. Dann ist es arabisirt
Oder aus dem Arabischen entlehnt. Vgl. bei Freitag:
*) Vgl. auch jiid. tat. heng *Hummer (Miller p. 85).
•) Vgl. daneben das LW. angalnn bei R a v e r t y und vgl. das L W.
angu§t 'Finger', angustdna *Ring, Fingerbut* neben orig. giUa *Finger*.
') Oegen Fr. M filler, WZKM. 5, 264.
2*
#### leaf 30
— 20 --
vabaSf pi. aubas ^GesindeF. — Auch Noldeke halt
aubas fiir echt arabisch.
133. Np. . aurang (so , resp. jetzt durdng gesprochen,
Sal. Shuk. p. 7) 'Thron*, nach VuUers mit der
Nebenform afrang und zahlreichen Nebenbedeutungen
(Einsicht, Zierde, Freude, Leben, Betrug etc.) wird
durch ein ap. ^abiranga^ mit Hinweis auf skr. rafiga-
'Farbe, Theater, Schaubiihne nicht erklart.
135. Np. ostdm, ustam *fidus, securus' passt besser zu
skr. ava-sthcL (ptc. avasthita- standhaft, zuverlassig') als
das unter Nr. 83 ebenfalls dazu gestellte dstod^ ustad
'Lehrer, Meister . Aber das hier erwahnte phi. ostam
(Phi. Min. p. 59, Z. 4) scheint *Zuflucht' zu bedeuten
(West: ^support') und konnte verschrieben sein fiir
apastam (Phi. Min. p. 11, Z. 5; 37, 4 v. u.) = alterem
apastan (der Siegel), arm. apastan *Vertrauen, Zuflucht',
vieUeicht = skr. upasthdna- 'Aufwartung, Verehrung'
(Horn p. 266). Doch ist es wohl besser, an der iiber-
lieferten Lesart festzuhalten, das Wort durch *Stand-
ort' zu iibersetzen und mit Horn auf ^avastaman- (vgl.
skr. avasthana- *Verweilen, Verharren') zuriickzufiihren.
Hierher konnte auch paz. dstiyan *the faithful, stead-
fast', dstiydnl ^assurance' Shk. 261 = phi. ostlkdn,
Ganjeshayagan Gloss. 1 ; Dinkart I, Gloss, p. 13 ; V,
p. 20 gehoren, wenn man es von *dst = ap. *avastd
'Standhalten' (skr. avasihd- *Bestand') ableitet.
136. Wie man *ich' auf ap. gen. mand zuriickgeht, so sollte
oi, vai *er, jener' auf ap. gen. avahyd zuriickgefiihrt
werden. Doch fehlen lautliche Analogien, vgl. ap.
vahyah- 'besser — np. bih etc. Sonst ware np. ord^
vaird 'ihm, ihn' etymologisch = ap. avahyarddiy 'des-
halb*.
138. Np. ei ist verdruckt fur ei ~ ai o!' Solche Inter-
jectionen bleiben ebenso wie die onomatop. Worter
besser weg.
140. Die Gleichung ermdn *Gast' ^= zd. airyaman- (nach
Geldner: *Genossenschaft' , nach Darmesteter;
*Vasall, Dienerj — skr. aryamdn- Busenfreund, Ge-
#### leaf 31
- 21 -
fahrte, Kamerad*') scheint mir einwandfrei, ein zd.
*a^&raman' am Feuer sitzend' dagegen mehr als be-
denklich.
144. Vgl. WZKM. 5, 254. Fr. MuIIer bemerkt richtig,
dass upa in Neup. zu ab geworden ware. ^) Es bleibt
daher nichts tibrig, als np. ba = bad liber paz. pa =
pad nur auf ap. patiy zuriickzufUhren. 3) Als erstes
Glied von Compositen wurde pati- mp. zu pat- (neben
paJ- und pa-y vgl. Nr. 345), das im Neup. erhalten
blieb, wahrend das selbstandige pati mp. zu pad (vor
Vocalen) oder pa (vor Consonanten, zuerst wohl vor Den-
talen) wurde, um dann (allerdings gegen die Kegel : anl.
p = np. p) im Neup. in bad^ ba uberzugehen. Erhalten
blieb pa in jiingeren Zusammensetzungen [padrud,
padid^), pinhan, pinddstan) , in denen seine urspr.
Bedeutung verwischt war und nicht mehr gefiihlt wurde.
145. Np. bd, aba *mit' geht durch paz. awd [nicht awdkl]
mit* (Min. Gl. 25, Shk. 232), phi. *apak (in apakth
assistance, cooperation' Gl. and Ind. p. 9 = paz. awdgl
Shk. 232) auf ap. ^upaka- = skr. upaka- Verbunden*,
upake *in nachster Nahe, gegenwartig zuriick, wie
Fr. Muller WZKM. 7, 367 richtig erkannt hat.
Vgl. Nr. 165: jiid. pers. awdz mit' --^ *upaca' : skr.
updka- (Horn).
146. Die Form -vd z. B. in angistva *kohlen-gebacken* =
*auf Kohlenfeuer gebackenes Brod*, afgh. LW. ndnvde
'Backer.'
148. Lies Jtori^^iq und vgl. de Lagarde, G. A. p. 73,
Gesenius, hebr. Wb. s. v. :i3"n5-
^) Anders A. Ber^aigne, J^tudes sur le lexique du Big-Teda
p. 190.
^) Nur in Compositen, deren urspriingliche Bedeutung Tergessen
war, h&tte upa- zu ba- werden konnen. Daraus konnte sich aber koin
selbstSndiges ba entwickeln.
') Man beachte, dass im Paz. nur pa, pad, nicht aber ato (= upa)
als selbstandige Praeposition Torhanden ist.
*) Das Wb. fiihrt auoh badid auf, zu dem jiid. tat. wedi', wedif'
(Miller p. 59-60) stimmt.
```


## [2026-09-07T20:22:10.645Z] TOOL CALL #26: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py; echo ====; sed -n 1,30p tools/ref_page.py",
 "description": "Read fetch_source and ref_page tools"
}
```


### [2026-09-07T20:22:10.701Z] TOOL RESULT

```
Exit code 1
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
(eval):1: === not found
```


## [2026-09-07T20:22:18.145Z] TOOL CALL #27: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83est-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%AA%D8%AE%D9%88%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D8%B3%D8%AA%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B4%D9%83%D8%A7%D8%B1\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 376: entry 0 PIE ost- / Persian ostoxan, haste; entry 1 askar\" ; done 2>&1 | tail -20",
 "description": "Archive Wiktionary pages batch 1"
}
```


### [2026-09-07T20:22:23.135Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c19c1a0efd69f786.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a73393a8dd84dadf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0cd942cf7d6e3109.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d0d445802f4f2790.txt
```


## [2026-09-07T20:22:26.632Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in c19c1a0efd69f786 a73393a8dd84dadf 0cd942cf7d6e3109 d0d445802f4f2790; do echo \"########## $f\"; head -c 3000 $f.txt | sed -n '1,200p'; echo; done",
 "description": "Read archived Wiktionary pages"
}
```


### [2026-09-07T20:22:28.181Z] TOOL RESULT

```
########## c19c1a0efd69f786
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83est-
FETCHED: 2026-09-07T20:22:20Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
########## a73393a8dd84dadf
URL: https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%AA%D8%AE%D9%88%D8%A7%D9%86
FETCHED: 2026-09-07T20:22:21Z
STATUS: 200
TITLE: استخوان - Wiktionary, the free dictionary

استخوان - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Arabic 

 Toggle Arabic subsection 

 1.1 
 Noun 

 1.1.1 
 Declension 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 2.3.1 
 Alternative forms 

 2.3.2 
 Derived terms 

 2.3.3 
 Descendants 

 2.4 
 Further reading 

 3 
 Urdu 

 Toggle Urdu subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 3.4 
 References 

 Toggle the table of contents 

 استخوان 

 26 languages 

 Azərbaycanca 
 বাংলা 
 Deutsch 
 Euskara 
 فارسی 
 Français 
 Hrvatski 
 Magyar 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Limburgs 
 ລາວ 
 Lietuvių 
 Malagasy 
 Bahasa Melayu 
 Norsk bokmål 
 Polski 
 پښتو 
 Português 
 Русский 
 Sängö 
 Slovenščina 
 Тоҷикӣ 
 Türkçe 
 中文 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

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

 Arabic
 [ edit ] 

 Root 

 خ و ن ( ḵ w n ) 

########## 0cd942cf7d6e3109
URL: https://en.wiktionary.org/wiki/%D9%87%D8%B3%D8%AA%D9%87
FETCHED: 2026-09-07T20:22:22Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
########## d0d445802f4f2790
URL: https://en.wiktionary.org/wiki/%D8%A2%D8%B4%D9%83%D8%A7%D8%B1
FETCHED: 2026-09-07T20:22:23Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-07T20:22:35.179Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('a73393a8dd84dadf.txt',encoding='utf-8').read()\ni=t.find('Persian\\n [ edit ]')\nif i<0: i=t.find('Etymology')\nprint(t[i-200:i+2500])\nEOF",
 "description": "Extract Persian etymology of ostoxan"
}
```


### [2026-09-07T20:22:36.567Z] TOOL RESULT

```
 اِسْتِخْوَانًا 
 istiḵwānan 

 الِاسْتِخْوَانَ 
 al-istiḵwāna 

 اِسْتِخْوَانَ 
 istiḵwāna 

 genitive

 اِسْتِخْوَانٍ 
 istiḵwānin 

 الِاسْتِخْوَانِ 
 al-istiḵwāni 

 اِسْتِخْوَانِ 
 istiḵwāni 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *h₃ésth₁ 
 Proto-Indo-Iranian *HástʰH 
 Proto-Iranian *HástH 
 Proto-Iranian *HástHáhuānām 
 Middle Persian [script needed] ( ʾsthwʾn' ) 
 Persian استخوان 

 Inherited from Middle Persian [script needed] ( ʾsthwʾn' /⁠astuxwān⁠/ , “ bone ” ) , from Proto-Iranian *HástHáhuānām , a compound from *HástH ( “ bone ” ) , from Proto-Indo-European *h₃ésth₁ ( “ bone ” ) .

 Cognate with Mazanderani هسکا ( hassekā ) , Ancient Greek ὀστέον ( ostéon , “ bone ” ) , Latin os .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔus.tu.ˈxʷaːn/ 

 ( Dari, formal ) IPA ( key ) : [ʔʊs.t̪ʰʊ.xɑːn] 

 ( Dari, formal ) IPA ( key ) : [ʔʊs.t̪ʰʊ.xɑːn] 
 ( Kabuli ) IPA ( key ) : [ʔʊs.t̪ʰʊ.xɑːn] 

 ( Hazaragi ) IPA ( key ) : [ʔus.t̪ʰu.xɔːn] 

 ( Iran, formal ) IPA ( key ) : [ʔos.t̪ʰo.xɒːn] 

 ( Iran, formal ) IPA ( key ) : [ʔos.t̪ʰo.xɒːn] 
 ( Tehrani ) IPA ( key ) : [ʔos.so.xuːn] 

 ( Tajik, formal ) IPA ( key ) : [ʔus.t̪ʰu.χɔn] 

 Rhymes: -aːn 

 Readings

 Classical reading ? 

 ustuxwān

 Dari reading ? 

 ustuxān

 Iranian reading ? 

 ostoxân

 Tajik reading ? 

 ustuxon

 Noun
 [ edit ] 

 Dari

 استخوان 

 Iranian Persian

 Tajik

 устухон 

 استخوان • ( ustuxwān / ostoxân ) ( Tajik spelling устухон ) 

 bone (anatomy)
 Synonyms: ( medical ) عظم ( azm ) , ( rare ) است ( ast ) 

 stone (of fruits)

 Alternative forms
 [ edit ] 

 اُستُخون ( ostoxun ) ( colloquial Iranian ) 

 سُتْخوان ( sotxân ) , سُتَخوان ( sotaxân ) , اُستُخان ( ostoxân ) ( all obsolete ) 

 Derived terms
 [ edit ] 

 اُستُخْوَانی ( ostoxâni ) 

 Descendants
 [ edit ] 

 Judeo-Tat: osduqu , əsduqu 

 → Azerbaijani: üstüxan 

 → Chagatai: استخوان ( ʾstxwʾn ) 
 Uyghur: ئۇستىخان ( ustixan ) 

 Uzbek: ustuxon 

 → Ottoman Turkish: استخوان ( üstühan ) 

 → Urdu: اُسْتُخوان ( ustuxvān ) 

 Further reading
 [ edit ] 

 Hayyim, Sulayman ( 1934 ), “ استخوان ”, in New Persian–English dictionary , Teheran: Librairie-imprimerie Béroukhim 

 Urdu
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian استخوان ( ustuxʷān ) .

 Pronunciation
 [ edit ] 

 ( Standard Urdu ) IPA ( key ) : /ʊs.t̪ʊx.wɑːn/ 

 Noun
 [ edit ] 

 اُسْتُخْوان • ( ustuxwān )  m ( Hindi spelling उस्तुख़्वान ) 

 bone 

 skeleton 

 References
 [ edit ] 

 “ استخوان ”, in اُردُو لُغَت ( urdū luġat ) (in Urdu), Ministry of Education: Government of Pakistan, 2017 .

 “ استخوان ”, in ریخْتَہ لُغَت ( rexta luġat ) - Rekhta Dictionary [ Urdu dictionary
```


## [2026-09-07T20:22:38.048Z] TOOL CALL #30: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B4%DA%A9%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D9%88%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D9%88%D8%B4%D9%87\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 376: askar, hush, nush, anushe\" ; done 2>&1 | tail",
 "description": "Archive more Wiktionary pages"
}
```


### [2026-09-07T20:22:45.236Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f470e63a0d78e16d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5292f9b3d675ee2c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a661658ca29d9510.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3201130dc3d10214.txt
```


## [2026-09-07T20:22:52.016Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport re\nfor f,label in [('f470e63a0d78e16d','ashkar'),('5292f9b3d675ee2c','hush'),('a661658ca29d9510','nush'),('3201130dc3d10214','anushe')]:\n    t=open(f+'.txt',encoding='utf-8').read()\n    print('##########',label, t.split('\\n')[3][:80])\n    if 'FETCH FAILED' in t[:400]: print('FAILED'); continue\n    i=t.find('From Wiktionary, the free dictionary')\n    print(t[i:i+2600])\n    print()\nEOF",
 "description": "Read archived pages 2"
}
```


### [2026-09-07T20:22:53.374Z] TOOL RESULT

```
########## ashkar TITLE: آشکار - Wiktionary, the free dictionary
From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔaːʃ.ˈkaːr/ 

 ( Dari, formal ) IPA ( key ) : [ʔɑːʃ.kʰɑːɾ] 

 ( Dari, formal ) IPA ( key ) : [ʔɑːʃ.kʰɑːɾ] 
 ( Kabuli ) IPA ( key ) : [ʔɑːʃ.kʰɑːɾ] 

 ( Hazaragi ) IPA ( key ) : [ʔɔːʃ.kʰɔːɾ] 

 ( Iran, formal ) IPA ( key ) : [ʔɒːʃ.kʰɒːɹ] 

 ( Tajik, formal ) IPA ( key ) : [ʔɔʃ.kʰɔɾ] 

 Rhymes: -aːr 

 Readings

 Classical reading ? 

 āškār

 Dari reading ? 

 āškār

 Iranian reading ? 

 âškâr

 Tajik reading ? 

 oškor

 Adverb
 [ edit ] 

 آشکار • ( āškār  / âškâr ) ( Tajik spelling ошкор ) 

 alternative form of آشکارا 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=آشکار&oldid=91788894 "

 Categories : Persian terms with IPA pronunciation 
 Rhymes:Persian/aːr 
 Rhymes:Persian/aːr/2 syllables 
 Persian lemmas 
 Persian adverbs 

 Hidden categories: Persian terms in nonstandard scripts 
 Persian links with redundant wikilinks 
 Persian links with redundant alt parameters 
 Persian links with manual fragments 
 Pages with entries 
 Pages with 1 entry 

 This page was last edited on 3 August 2026, at 17:12.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 آشکار 

 7 languages 

 Add topic

########## hush TITLE: هوش - Wiktionary, the free dictionary
From Wiktionary, the free dictionary

 See also: هوس and هَوُسَ 

 Ottoman Turkish
 [ edit ] 

 هوش 
 Etymology 1
 [ edit ] 

 From Persian هوش ( huš ) , a variant of توسکا ( tuskâ , “ birch ” ) , which probably derives from a Mongolic source; compare modern Mongolian хус ( xus , “ birch ” ) .

 Noun
 [ edit ] 

 هوش • ( hoş or huş ) 

 birch , any of various trees in the genus Betula 
 Synonym: آق آغاج ( ak ağac ) 

 Descendants
 [ edit ] 

 Turkish: huş 

 Further reading
 [ edit ] 

 Çağbayır, Yaşar ( 2007 ), “ huş1 ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 2011 

 Kélékian, Diran ( 1911 ), “ هوش ”, in Dictionnaire turc-français ‎ [1] (in French), Constantinople: Mihran, page 1331 

 Nişanyan, Sevan ( 2002– ), “ huş ”, in Nişanyan Sözlük 

 Redhouse, James W. ( 1890 ), “ هوش ”, in A Turkish and English Lexicon ‎ [2] , Constantinople: A. H. Boyajian, page 2174 

 Etymology 2
 [ edit ] 

 Borrowed from Persian هوش ( huš , “ intellect ” ) .

 Noun
 [ edit ] 

 هوش • ( huş ) 

 reason , common sense , consciousness 
 Synonyms: ادراك ( idrak ) , اوص ( us ) , شعور ( şuûr ) , عقل ( akl ) 

 Derived terms
 [ edit ] 

 هوشمند ( huşmend , “ reasonable ” ) 
 هوشیار ( huşyar , “ reasonable ” ) 

 Descendants
 [ edit ] 

 Turkish: huş 

 Further reading
 [ edit ] 

 Çağbayır, Yaşar ( 2007 ), “ huş3 ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 2011 

 Kélékian, Diran ( 1911 ), “ هوش ”, in Dictionnaire turc-français ‎ [3] (in French), Constantinople: Mihran, page 1331 

 Meninski, Franciszek à Mesgnien ( 1687 ), “Intellectus”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simul idem index verborum lexici turcico-arabico-persici, quod latinâ, germanicâ, aliarumque linguarum adjectâ nomenclatione nuper in lucem editum ‎ [4] , Vienna, column 838 

 Meninski, Franciszek à Mesgnien ( 1680 ), “ هوش ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [5] , Vienna, column 5514 

 Redhouse, James W. ( 1890 ), “ هوش ”, in A Turkish and English Lexicon ‎ [6] , Constantinople: A. H. Boyajian, page 2174 

 Etymology 3
 [ edit ] 

 From Arabic هَوْش ( hawš ) .

 Noun
 [ edit ] 

 هوش • ( hevş ) 

 multitude , myriad , a great amount of something

 Further reading
 [ edit ] 

 Meninski, Franciszek à Mesgnien ( 1687 ), “Multitudo”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simu

########## nush TITLE: نوش - Wiktionary, the free dictionary
From Wiktionary, the free dictionary

 See also: نوس , نؤوش , and نۄش 

 Arabic
 [ edit ] 

 Root 

 ن و ش ( n w š ) 

 2 terms 

 Noun
 [ edit ] 

 نَوْش • ( nawš )  m 

 verbal noun of نَاشَ ( nāša , “ to grip, to take hold of something ” )   ( form I ) 

 Declension
 [ edit ] 

 Declension of noun نَوْش ( nawš )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 نَوْش 
 nawš 

 النَّوْش 
 an-nawš 

 نَوْش 
 nawš 

 nominative

 نَوْشٌ 
 nawšun 

 النَّوْشُ 
 an-nawšu 

 نَوْشُ 
 nawšu 

 accusative

 نَوْشًا 
 nawšan 

 النَّوْشَ 
 an-nawša 

 نَوْشَ 
 nawša 

 genitive

 نَوْشٍ 
 nawšin 

 النَّوْشِ 
 an-nawši 

 نَوْشِ 
 nawši 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( ʾnwš /⁠anōš⁠/ , “ elixir, antidote ” , literally “ immortal ” ) , from Proto-Iranian *an-auša- ( “ immortal ” ) , from *an- ( “ not, a- ” ) +‎ *auša- ( “ destruction ” ) , the latter from Proto-Iranian *Hawš ( “ to burn ” ) , from Proto-Indo-European *h₁ews- ( “ to burn ” ) . [ 1 ] [ 2 ] Related to Old Armenian անոյշ ( anoyš ) , an Iranian borrowing. Cognate with Parthian 𐫀𐫗𐫇𐫢 ( ʾnwš /⁠anōš⁠/ , “ immortal ” ) , Ossetian ӕнус ( ænus , “ eternity; century; age ” ) and Avestan 𐬀𐬥𐬀𐬊𐬱𐬀 ( anaoša , “ immortal ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈnoːʃ/ 

 ( Dari, formal ) IPA ( key ) : [noːʃ] 

 ( Dari, formal ) IPA ( key ) : [noːʃ] 
 ( Kabuli ) IPA ( key ) : [noːʃ] 

 ( Hazaragi ) IPA ( key ) : [nʊːʃ] 

 ( Iran, formal ) IPA ( key ) : [nuːʃ] 

 ( Tajik, formal ) IPA ( key ) : [nɵʃ] 

 Rhymes: -oːʃ 

 Readings

 Classical reading ? 

 nōš

 Dari reading ? 

 nōš

 Iranian reading ? 

 nuš

 Tajik reading ? 

 nüš

 Noun
 [ edit ] 

 نوش • ( nōš / nuš ) ( Tajik spelling нӯш ) 

 ambrosia , nectar 

 elixir 

 antidote 

 Derived terms
 [ edit ] 

 نوشابه ( nōšāba ) 

 نوش‌دارو ( nōš-dārū ) 

 Verb
 [ edit ] 

 نوش • ( nuš ) 

 present stem form of نوشیدن ( nušidan , “ to drink ” ) 

 References
 [ edit ] 

 Dehkhoda, Ali-Akbar ( 1931– ), “ نوش ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 

 MacKenzie, D. N. ( 1971 ), “anōš”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press 

 ^ Rastorgujeva, V. S. ; Edelʹman, D. I. ( 2000 ), Etimologičeskij slovarʹ iranskix jazykov [ Etymological Dictionary of Iranian Languages ] (in Russian), volume 1, Moscow: Vostochnaya Literatura, pages 266-7 

 ^ Cheung, Johnny ( 2007 ), Etymological Dictionary of the Iranian Verb (Leiden Indo-European 

########## anushe TITLE: انوشه - Wiktionary, the free dictionary
From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: انوشه 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 نوشه ( nōša  / nuše ) 

 Etymology
 [ edit ] 

 From Middle Persian 𐭠𐭭𐭥𐭱𐭪𐭩 ( ʾnʿšky /⁠anōšag⁠/ , “ immortal ” ) , from 𐭠𐭭𐭥𐭱 ( ʾnʿš /⁠anōš⁠/ ) + 𐭪𐭩 ( ky /⁠-ag⁠/ ) , from Old Persian [Term?] ( /⁠*anauša-⁠/ , “ immortal ” ) , from Proto-Iranian *an-awša- ( “ immortal ” ) . Cognate with Avestan 𐬀𐬥𐬀𐬊𐬱𐬀 ( anaoša , “ immortal ” ) , Ossetian ӕнус ( ænus ) , and the Old Armenian borrowing անուշակ ( anušak ) . Compare نوشین ( nōšīn  / nušin , “ sweet ” ) and نوشیدن ( nōšīdan  / nušidan , “ to drink ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔa.noː.ˈʃa/ 

 ( Dari, formal ) IPA ( key ) : [ʔä.noː.ʃá] 

 ( Dari, formal ) IPA ( key ) : [ʔä.noː.ʃá] 
 ( Kabuli ) IPA ( key ) : [ʔä.noː.ʃá] 

 ( Hazaragi ) IPA ( key ) : [ʔä.nʊː.ʃá] 

 ( Iran, formal ) IPA ( key ) : [ʔæ.nuː.ʃé] 

 ( Tajik, formal ) IPA ( key ) : [ʔä.nɵ.ʃá] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 anōša

 Dari reading ? 

 anōša

 Iranian reading ? 

 anuše

 Tajik reading ? 

 anüša

 Adjective
 [ edit ] 

 انوشه • ( anōša / anuše ) ( Tajik spelling анӯша ) 

 immortal 

 Derived terms
 [ edit ] 

 انوشگی ( anōšagī / anušegi ) 
 انوشیروان ( anōšērwān  / anuširvân ) 

 Proper noun
 [ edit ] 

 انوشه • ( anōša  / anuše ) ( Tajik spelling Анӯша ) 

 a male or female given name , Anousheh , Anosha , Anooshe , and Anoosheh , from Middle Persian 

 References
 [ edit ] 

 Durkin-Meisterernst, Desmond ( 2004 ), “ʾnwšg”, in A Dictionary of Manichaean Middle Persian and Parthian (Corpus Fontium Manichaeorum; 3.1 ), Turnhout: Brepols 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=انوشه&oldid=88003529 "

 Categories : Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
 Persian terms derived from Old Persian 
 Persian terms derived from Proto-Iranian 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/a 
 Rhymes:Persian/a/3 syllables 
 Persian lemmas 
 Persian adjectives 
 Persian proper nouns 
 Persian given names 
 Persian male given names 
 Persian male given names from Middle Persian 
 Persian female given names 
 Persian female given names from Middle Persian 

 Hidden categories: Old Persian term requests 
 Pages with entries 
 Pages with 1 entry 
 Persian terms in nonstandard scripts 
 Persian links with redundant wikilinks 
 Persian links with redundant alt parameters 
 Persian links with manual fragments 

 This page was last edited on 1 November 2025, at 04:25.
```


## [2026-09-07T20:23:08.362Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('5292f9b3d675ee2c.txt',encoding='utf-8').read()\ni=t.find('Persian\\n [ edit ]')\nwhile i>0:\n    seg=t[i:i+1500]\n    if 'Etymology' in seg and ('intellect' in seg or 'Middle Persian' in seg):\n        print(seg); break\n    i=t.find('Persian\\n [ edit ]', i+10)\nEOF",
 "description": "Find Persian section of hush page"
}
```


### [2026-09-07T20:23:09.748Z] TOOL RESULT

```
Persian
 [ edit ] 

 Persian Wikipedia has an article on: هوش 

 Wikipedia fa 

 Etymology 1
 [ edit ] 

 Etymology tree

 Proto-Indo-European *h₂ew- 

 Proto-Indo-European *-s 

 Proto-Indo-European *h₂ṓws der. 
 Proto-Indo-Iranian *HušíH 
 Proto-Iranian *HušíH 
 Old Persian [script needed] ( *ušiy ) 
 Middle Persian 𐭠𐭥𐭱 ( ʾʿš /⁠ōš⁠/ ) 
 Persian هوش 

 Inherited from Middle Persian 𐭠𐭥𐭱 ( ʾʿš /⁠ōš⁠/ ) , from Old Persian [script needed] ( *ušiy ) , from Proto-Iranian *HušíH . Compare Northern Kurdish hiş , Latin auris , English ear .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈhoːʃ/ 

 ( Dari, formal ) IPA ( key ) : [hóːʃ] 

 ( Dari, formal ) IPA ( key ) : [hóːʃ] 
 ( Kabuli ) IPA ( key ) : [ʔóːʃ] 

 ( Hazaragi ) IPA ( key ) : [ʔʊ́ːʃ] 

 ( Iran, formal ) IPA ( key ) : [húːʃ] 

 ( Tajik, formal ) IPA ( key ) : [hɵ́ʃ] 

 Rhymes: -oːʃ 

 Readings

 Classical reading ? 

 hōš

 Dari reading ? 

 hōš

 Iranian reading ? 

 huš

 Tajik reading ? 

 hüš

 Noun
 [ edit ] 

 هوش • ( hōš / huš ) ( Tajik spelling ҳӯш ) 

 intellect 

 intelligence 

 understanding 

 Derived terms
 [ edit ] 

 باهوش ( bâ-hôš ) 
 بهوش ( behôš ) 
 بی‌هوش ( bê-hôš ) 
 مدهوش ( madhôš ) 
 هوش مصنوعی ( hôš-e masnu'i ) 
 هوشمند ( hôšmand ) 
 هوشی ( hôši ) 
 هوشیار ( hôšyâr ) 

 Etymology 2
 [ edit ] 

 Noun
 [ edit ] 

 هوش • ( huš ) 

 alternative form of توسکا ( tuskâ ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=هوش&oldid=91080090 "

 Categories : Ottoman Turkish ter
```


## [2026-09-07T20:23:10.193Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG Hauš ===\"; grep -n -i \"hauš\\|haus\\b\\|\\*auš\" CHEUNG.txt | head -20; echo \"=== SOD stk bone ===\"; grep -n \"bone\" SOD.txt | head -20",
 "description": "Grep Cheung and Sogdian dict"
}
```


### [2026-09-07T20:23:10.263Z] TOOL RESULT

```
=== CHEUNG Hauš ===
10263:sleep’, Kurd. xeftin, (Sul.) xawtin, (Sina) xaftin, Zaz. witis, Anar. hauft-/haus-, 
11686:170 *Haus 
11705:*Hauš ‘to burn’ 
11873:*Hhaus 173 
27849:anger’ || (+ *para-a-) OKh. paroys- (parauys-, paraus-) ‘to drown’ || (+ *fra-) haus- 
29301:dein Haus verfallen !’) || (+ *a-) ? Bal. ašešt/ašeš- ‘to rot’ ("Et. unknown.", 
38046:haus- (hos-), 430 
44757:hauft-/haus-, 146 
55651:*Hhaus, *HuaH' (s.v.), 
55875:*Haus, *kaup’ (s.v.), *pax 
58407:*Hhaus 
=== SOD stk bone ===
17873:tomb,  grave  {place  of  bones) 
18839:bone 
18861:(o/)bone,  bony 
68592:(of Obone 
68625:bone 
75632:fingerbone 
87862:bone     1699,  1702,  8990,  8994 
89582:fingerbone     10013
```


## [2026-09-07T20:23:22.583Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18830,18870p' SOD.txt; echo \"==== search stk entries ====\"; grep -n \"^1699\\|^1702\\| 1699 \\|'stk\\|ʾstk\\|astk\" SOD.txt | head -20",
 "description": "Look at Sogdian bone entries"
}
```


### [2026-09-07T20:23:22.658Z] TOOL RESULT

```
cruel 
GMS  157 

1699  >stk-   B,  M,  S  ol>U 
ostak   ®<*astaka\  Khwar.  >stk\  Yaghn.  sitak\  MP 

astag   ©ace.  -w,  abl.  -Snon.  gen.  -y   =»stq-, 

st'yn'k 
bone 
GMS  981,  1185;  BBB  93  b37;  VJ  806,  TSP  2.117, 

361,  370,  3.273;  SCE  83,  271;  STSC;  -Wi,  VJ 

781,779 

1700  >stq)(n) 

ast-kan   ©3sg.  fut.   ->>styl 
GMS 

1701  'stkpys'y   B  f Ul  <^l>^J  y±*  ^'y^1 
ostak-pise  ? 

bony,  limb 

Gersh.  IF  1970,  303;  BSTBL,  Intox.  24;  SCE  368 

1702  'stkyn'y   B  J**^ 
ostakene 

(o/)bone,  bony 
SCE  169;  GMS  1053 

1703  >stny   B 
(o)stane   ^'st'ny 
place 
TSP  2.1017  n  p!82;GMS  1118 

1704  >str>   B  (. 
astara   ©<*ustara 
==== search stk entries ====
13603:anPaste,  ambastc   OnP'stk)  ©pp.  ^bsly,  'p'stk, 
15072:'nw'stk 
15205:anwaste   Onwsty,  'nw'stk)   ©pp. 
15413:anxaste   ©pp.   ^'ny'stk 
17578:'rw'stk 
17584:1516  Vw'stk  «»  WstHc 
18833:1699  >stk-   B,  M,  S  ol>U 
18851:1701  'stkpys'y   B  f Ul  <^l>^J  y±*  ^'y^1 
18858:1702  'stkyn'y   B  J**^ 
28568:3191  ck'stky*  M  jAj 
44432:mastkare  (mstk*ry(y)) 
46776:nast   ©pt.  st.  =*nys-\  n'stk,  nst- 
48235:6028  np'stk   B  <jji^ 
48243:6029  np>sty   M  =$  np'stk 
50041:^'np'stk,  np}y6- 
53272:6766  pS'stkyn   B  Uy*  0l£s.T 
55541:7110  pry'stk   B 
55676:parxaste  ©pp.  =*pryyz-,  pry'stk 
63858:pyaste   (py*sty)   ^py'stk,  pysty(y) 
75031:9920  wp'stk   B  =»  wpsty
```


## [2026-09-07T20:23:29.576Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1699\" SOD_pages.txt | head -5; echo ---; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('1699')\nprint(t[max(0,i-4000):i+200][-1200:])\nEOF",
 "description": "Find page tag for Gharib entry 1699"
}
```


### [2026-09-07T20:23:30.882Z] TOOL RESULT

```
8651:1687 'st'ryt M                                                           1699 >stk- B, M, S                             ol>U
37475:    11699 zy8 C                                           oytj             (to)return, 0#)detour
37767:(to)bc separated       10050             bitter      9648,9684,9687             bone     1699, 1702, 8990, 8994
---
          (a)stirc ©<*stri- =»}stryc
        ^'st'ryt                                                               female
                                                                               Benv. TSP 2.353 npl73
       star
       TSP 6.147; SCE 265; TSP 3.152                                      1698 »stptyy M                     c^ijt^ijSL*^
                                                                                 stpty(y)
 1686 'stYs B                                        Jjlf j^
                                                   jAljb
                                                                               (a)stapde ©Parth. MP 'stft ©pp. =»'stptyyh,
      (o)stars ©Wakh. stors
                                                                                cruel
       plough share                                                             GMS 157
       SCE 245; Gersh. IF 1970, 305
1687 'st'ryt M                                                           1699 >stk- B, M, S                             ol>U
                                                         olfjU-               ostak ®<*astaka\ Khwar. >stk\ Yaghn. sitak\ MP
     ostaret (st'r'k, *
```


## [2026-09-07T20:23:35.274Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=8500 && NR<=8660 && /pdf page/' SOD_pages.txt | tail -5",
 "description": "Find pdf page tag near entry 1699"
}
```


### [2026-09-07T20:23:36.623Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:23:39.987Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SOD_pages.txt | awk -F: '$1<8700' | tail -3",
 "description": "Locate page tag before line 8651"
}
```


### [2026-09-07T20:23:41.456Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:23:45.897Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 SOD_pages.txt; grep -c $'\\f' SOD_pages.txt; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if '1699' in p and 'stk' in p:\n        print('leaf',i, 'printed approx', i-66)\n        break\nEOF",
 "description": "Compute Gharib page for entry 1699"
}
```


### [2026-09-07T20:23:47.202Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English
642
leaf 132 printed approx 66
```


## [2026-09-07T20:23:55.757Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^osteo-\\|osteo- ,\\|oyster, n\\|^oyster\\|ostreon\" KLN_1971.txt | head; echo \"=== 1966 ===\"; grep -n \"osteon\\|ostreon\" KLN_1966.txt | head",
 "description": "Grep Klein for osteo/oyster"
}
```


### [2026-09-07T20:23:55.841Z] TOOL RESULT

```
169650:osteo-. The second element is prob. related to 
169744:osteo-, before a vowel oste-, ost-, combining form 
169775:osteo- and myelitis. 
169806:osteo- and Gk. -x^o?, ‘cutting’, from the stem 
169810:osteo- and -xojzta, ‘a cutting of’, fr. to|at), *a 
170754:oyster, n. — ME., fr. OF. oistre, uistre (F. huitre), 
=== 1966 ===
23764:metopic,  adj.,  pertaining  to  the  forehead  (anat.) —  Formed  with  adj.  sufT.  -ic  fr.  Gk.  aexomov, ‘forehead’.  See  metope,  ‘face  of  the  crab’, metopomancy,  n.,  divination  by  means  of  the  fore¬ head.  —  Compounded  of  Gk.  iaetmttov,  ‘fore¬ head’,  and  [AXVTeii,  ‘divination’.  See  metope, ‘face  of  the  crab’,  and  -mancy. metosteon,  n.,  ossification  of  the  posterior  lateral processes  of  the  sternum  ( ornithol .)  —  ModL., formed  fr.  Gk.  (aetoc-,  ‘behind’,  and  octxeov, ‘bone’.  See  meta-  and  osteo-. metralgia,  n.,  pain  in  the  uterus  (med.)  —  Medi¬ cal  L.,  compounded  of  Gk.  (A7)xpa,  ‘uterus, womb’,  and  aXyo?,  ‘pain’.  See  metro-,  uterine , and  -algia.
```


## [2026-09-07T20:23:59.050Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '169740,169760p;170750,170770p' KLN_1971.txt",
 "description": "Read Klein osteo- and oyster"
}
```


### [2026-09-07T20:23:59.123Z] TOOL RESULT

```
Derivatives: ostentatious-ly , adv., ostentatious- 
ness, n. 

osteo-, before a vowel oste-, ost-, combining form 
meaning a ‘bone’ or ‘bones’. — Gk. iaxso-, 
oCTTe-, 6 ot-, fr. £axiov, ‘bone’, which is cogn. 
with L. os, ‘bone’. See os, ‘bone’ and cp. words 
there referred to. Cp. also periosteum, 
osteoblast, n., a bone-forming cell. — Compound- 
ed of osteo- and Gk. (3Xacx6s, ‘bud, sprout, 
shoot’. See -blast. 

osteogenesis, n., formation of bone; ossification 
(physiol.) — Compounded of osteo- and Gk. 
Y^veais, ‘origin, source, birth, descent’. See 
genesis. 

osteoid, adj., like bone. — Compounded of osteo- 
and Gk. -oet57)?, ‘like’, fr. eI8os, ‘form, shape’. 
See -old. 
‘to hear’, fr. L. audidtis , 2nd pers. pi. of pres, 
subj. fr. audire, ‘to hear’. See audible and cp. 
oyer, 

oyster, n. — ME., fr. OF. oistre, uistre (F. huitre), 
fr. L. ostrea , ostreum , fr. Gk. Saxpeov, ‘oyster’, 
which is rel. to oct£ov, octxouv, ‘bone’; so 
called from its hard shell. See osteo- and cp. 
ostracize. 

ozo-, combining form meaning ‘smell’ (generally 
used in a bad sense. — Gk. &£o-, fr. ‘to 
smell’ . See odor and cp. ozone, osmium, 
ozocerite, n., a waxlike mineral. — G. Ozokerit , 
coined by the German mineralogist Ernst Frie- 
drich Glocker (1793-1858) in 1833 fr. ozo-, Gk. 
x?)p6<;, ‘wax’, and suff. -it, which goes back to 
Gk. -fxr^. See cere and subst. suff. -ite. 
ozone, n., an allotropic form of oxygen with a 
pungent odor (chem.) — Coined by the German 
chemist Christian Friedrich SchOnbein (1799-
```


## [2026-09-07T20:24:05.672Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^os, n\\|os, n\\., a bone\\|‘bone’, which is cogn\" KLN_1971.txt | head; echo ---; grep -n \"os, ‘bone’\" KLN_1971.txt | head -3",
 "description": "Find Klein os bone entry"
}
```


### [2026-09-07T20:24:05.756Z] TOOL RESULT

```
169373:os, n., a bone ( anat .) — L. os, gen. ossis,' ‘bone’, 
169385:os, n., a mouth (anat.).-— L. os, gen. oris , ‘mouth’. 
169746:oCTTe-, 6 ot-, fr. £axiov, ‘bone’, which is cogn. 
---
21591:cogn. with L. os, ‘bone’. See os. 
169663:stem of os, gen. ossis, ‘bone’. See os, ‘bone’. For 
169705:-fy. See os, ‘bone’.
```


## [2026-09-07T20:24:08.755Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '169373,169390p;169695,169712p' KLN_1971.txt",
 "description": "Read Klein os and ossify"
}
```


### [2026-09-07T20:24:08.824Z] TOOL RESULT

```
os, n., a bone ( anat .) — L. os, gen. ossis,' ‘bone’, 
cogn. with OI. asthi , Hitt, hashtdi -, Gk. ocjteov 
(A tt. ootouv, Dor. 6 cttiov, ‘bone’, ocrrpeov, 
‘oyster’, ocTpaxov, ‘oyster shell, potsherd’, 
dtoTpayaXo? (assimilated fr. *6oTpdcyaXo<;), 
‘one of the vertebrae of the neck, anklebone, 
molding’, Alb. asht, ashte , ‘bone’, Avestic ascu -, 
‘shinbone’, W. asgwrn, Co. ascorn , ‘bone’, and 
possibly also with Arm. oskr, ‘bone’. Cp. os- 
seous. Cp. also astragal, osphyo-, osteo-, os- 
tracize, oyster. 

os, n., a mouth (anat.).-— L. os, gen. oris , ‘mouth’. 
See oral. 

Osage orange, an ornamental American tree, 
Toxylon pomiferum ; its fruit. — Named after 
the Osage Indians. 

— L. ossifraga, ‘sea eagle’, fem. of ossifragus , 
‘bone-breaking’, fr. os , gen. ossis, ‘bone’, and 
frag-, stem of frangere, ‘to break’. See os, ‘bone*, 
and fraction and cp. osprey, which is a doublet 
of ossifrage. 

ossify, tr. and intr. v., to form or turn into bone. 

— Formed fr. L. os, gen. ossis, ‘bone’, and suff. 
-fy. See os, ‘bone’. 

Derivatives: ossifi-ed , adj., ossifi-er , n. 
ossuary, n., an urn for the bones of the dead. — 
Late L. ossudrium, ‘charnel house’, formed fr. 
L. os, gen. ossis , ‘bone’, on the analogy of mor- 
tuarium, ‘mortuary’. See os, ‘bone’, and 2nd 
subst. suff. -ary.
```


## [2026-09-07T20:24:24.766Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\ndef find(pat, lo=0, hi=99999):\n    for i,p in enumerate(t):\n        if re.search(pat,p):\n            print('leaf',i, '|', re.search(pat,p).group(0)[:80])\nfind(r'Avestic\\s+ascu')\nfind(r'audible,\\s*adj')\nfind(r'ear,\\s*n\\., the organ of hearing')\nEOF",
 "description": "Locate Klein 1966 leaves"
}
```


### [2026-09-07T20:24:26.203Z] TOOL RESULT

```
leaf 78 | audible,  adj
leaf 419 | audible,  adj
```


## [2026-09-07T20:24:29.790Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[78]\ni=p.find('audible')\nprint(p[max(0,i-1500):i+1500])\nEOF",
 "description": "Read Klein 1966 audible entry"
}
```


### [2026-09-07T20:24:31.218Z] TOOL RESULT

```
  L. aucupdtus,  pp.  of  aucupdre,  later  aucupari,  ‘to go  fowling’,  fr.  auceps,  ‘fowler;  spy,  eaves¬ dropper’,  for  *avi-cap-s,  fr.  avis,  ‘bird’,  and capere,  ‘to  catch,  seize,  take,  receive’.  See  auspice and  captive.
audacious,  adj.,  daring,  bold.  —  F.  audacieux (fern,  audacieuse),  fr.  L.  auddcia,  ‘daring,  bold¬ ness,  courage,  intrepidity’,  fr.  audax,  gen.  au- dacis,  ‘daring,  bold,  courageous,  intrepid’,  fr. audere,  ‘to  dare’,  which  stands  for  *avidire,  ‘to be  eager’,  fr.  avidus,  ‘eager’.  The  meaning  ‘to dare’  first  arose  from  the  negative  form:  non audere  orig.  meant  ‘to  wish  or  to  have  a  mind not  to  do  something’,  whence  it  came  to  denote ‘not  to  risk  or  dare  to  do  something’.  L.  avidus is  a  derivative  of  avere,  ‘to  wish,  desire,  long  for, crave’,  whence  also  avarus,  ‘greedy’.  See  avid and  cp.  avarice.
Derivatives:  audacious-ly,  adv.,  audacious¬ ness,  n.
audacity,  n.,  daring,  boldness.  —  Formed  with suff.  -ity  fr.  L.  audax,  gen.  -dm,  ’bold’,  fr.  au¬ dere,  ‘to  dare’.  See  prec.  word  and  -ity. audible,  adj.  —  ML.  audibilis,  fr.  L,  audio,  audire, ‘to  hear’,  which  prob.  stands  for  * awis-d-id ,  fr. I.-E.  base  *awei-,  *au-,  ‘to  perceive’,  whence  also OL  avifi,  Avestic  avish,  ‘openly,  evidently’,  Gk. alaffdvopai  (for  *4Fia-ff-<xvo[iai),  ‘I  perceive’, afo)  (for  ‘aft. to),  ‘I  hear’  (lit.  ‘I  perceive  by  the
ear’),  OSlav.  ave,  jave,  ‘open,  public’,  aviti, javiti,  ‘to  reveal’.  Cp.  obedient,  obeisance,  obey, oyer,  oyez.
Derivatives:  audibii-ity ,  n.,  audible-ness,  n., audibl-y,  adv.
audience,  n.  —  F.,  fr.  L.  audientia,  ‘a  hearing, audience’,  fr.  audiens,  gen.  -entis,  pres.  part,  o audire.  See  audible  and  -ence. audient,  n.,  a  hearer,  listener.  —  L.  audiens,  gen. -entis.  See  prec.  word  and  -ent. audile,  adj.,  auditory.  —  Formed  with  suff.  -ile fr.  L.  audire,  ‘to  hear’.  See  audible.
Derivative:  audile,  n.,  a  person  whose  imagery is  chiefly  auditory  ( psychol .) audiology,  n.,  the  science  of  curing  defective  hear¬ ing.  —  A  hybrid  coined  fr.  L.  audire,  ‘to  hear’, and  Gk.  -Xoyia,  fr.  -Xoyoi;,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  See  audible  and  -logy.
Derivative :  audiolog-ist,  n. audiometer,  n.,  an  instrument  for  measuring  the intensity  of  sounds.  —  A  hybrid  coined  fr.  L. audire,  ‘to  hear’,  and  Gk.  ptixpov,  ‘measure’.  See audible  and  meter,  ‘poetical  rhythm’.
Deriva
```


## [2026-09-07T20:24:40.223Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(d['KLN']['page_offset']);print(d['KLN'].get('lookup_hint'))\"",
 "description": "Klein page offset"
}
```


### [2026-09-07T20:24:41.500Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-07T20:24:50.804Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (75,559,560,561,258,259,260):\n    p=t[i]\n    # first headword-ish tokens\n    import re\n    hw=re.findall(r'(?m)^([a-zA-Z][a-zA-Z\\-]+),\\s', p)\n    print('leaf',i,'->', hw[:4], '...', hw[-3:] if hw else '')\nEOF",
 "description": "Check Klein leaf contents"
}
```


### [2026-09-07T20:24:52.099Z] TOOL RESULT

```
leaf 75 -> ['ataxic', 'ate', 'Ate', 'Athanasius'] ... ['Atlantic', 'Atlas', 'atlas']
leaf 559 -> ['neve', 'never', 'nevertheless', 'new'] ... ['nide', 'nidify', 'nidology']
leaf 560 -> ['nidorous', 'nidus', 'niece', 'Nietzschean'] ... ['Nike', 'nil', 'nilgai']
leaf 561 -> ['Nilotic', 'nim', 'nimble', 'Nimrod'] ... ['re', 'nit', 'nitric']
leaf 258 -> ['dodge', 'dodo', 'doe', 'doff'] ... ['dolent', 'dole', 'dolent']
leaf 259 -> ['dolerite', 'dolicho-', 'Dolichos', 'Doliidae'] ... ['dominator', 'Dominic', 'dominical']
leaf 260 -> ['Dominican', 'dominie', 'dominion', 'dominium'] ... ['dormant', 'dormer', 'dormy']
```


## [2026-09-07T20:25:04.575Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (74,75,78):\n    print('==== leaf',i)\n    print(t[i][:300].replace('\\n','|'))\n    print('...tail...', t[i][-200:].replace('\\n','|'))\nEOF",
 "description": "Inspect Klein leaves for page numbers"
}
```


### [2026-09-07T20:25:05.944Z] TOOL RESULT

```
903
==== leaf 74
  fr.  daxf]p,  ‘star’.  See|Aster.|astragal,  n.,  a  convex  molding  (archil.)  —  L.  as¬ tragalus,  fr.  Gk.  aaxpxyaXoc;,  ‘one  of  the  ver¬ tebrae  of  the  neck,  anklebone,  molding’,  assim¬ ilated  fr.  *6axpdyocXo<;,  which  is  rel.  to  oaxpoc- xov,  ‘oyster  shell,  potsherd’,  6ax£
...tail...   ‘grandfather’.  See  uncle  and cp.  avuncular.|atavistic,  adj.,  pertaining  to  atavism;  tending  to atavism.  —  Formed  with  suff.  -istic  fr.  L.  atavus. See  prec.  word.  See  atavism.|D
==== leaf 75
erivative:  atavistic-al-ly,  adv. ataxia,  n.,  irregularity  of  bodily  functions  ( med .)|—  Medical  L.,  fr.  Gk.  dxaljid,  ‘want  of  order’, fr.  d-  (see  priv.  pref.  a-)  and  xa^ip,  ‘arrange¬ ment,  disposition,  order’,  from  the  stem  of xdaaeiv,  ‘to  arrange,  put  in  order’. 
...tail...   word, atlas,  n.,  name  of  the  first  vertebra  ( anal .)  — From  Atlas  (q.v.);  so  called  because  it  bears  the|122|skull.  This  name  was  given  to  the  first  vertebra by  the  Belgia
==== leaf 78
  L. aucupdtus,  pp.  of  aucupdre,  later  aucupari,  ‘to go  fowling’,  fr.  auceps,  ‘fowler;  spy,  eaves¬ dropper’,  for  *avi-cap-s,  fr.  avis,  ‘bird’,  and capere,  ‘to  catch,  seize,  take,  receive’.  See  auspice and  captive.|audacious,  adj.,  daring,  bold.  —  F.  audacieux (fern,  
...tail... . Cp.  omlah.|aumildar,  n.,  a  revenue  collector  in  India.  — Hind.  ‘ amaldar ,  lit.  ‘one  holding  an  office’,  a hybrid  coined  fr.  Arab,  'dmal,  ‘work’  (see  au¬ mil),  and  the  Persi
```


## [2026-09-07T20:25:14.152Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'(?m)^ear,\\s*n', p):\n        print('leaf',i)\n        m=re.search(r'(?m)^ear,\\s*n.{0,1200}', p, re.S)\n        print(m.group(0)[:1200])\n        nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$', p)\n        print('page nums on leaf:', nums)\n        break\nEOF",
 "description": "Find Klein ear entry"
}
```


### [2026-09-07T20:25:15.669Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:25:18.644Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"the organ of hearing\" KLN_1966.txt KLN_1971.txt | head",
 "description": "Grep Klein for ear definition"
}
```


### [2026-09-07T20:25:18.696Z] TOOL RESULT

```
KLN_1971.txt:78205:ear, n., the organ of hearing. — ME. ere, fr. OE.
```


## [2026-09-07T20:25:21.529Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '78205,78230p' KLN_1971.txt",
 "description": "Read Klein ear entry (1971)"
}
```


### [2026-09-07T20:25:21.589Z] TOOL RESULT

```
ear, n., the organ of hearing. — ME. ere, fr. OE. 
eare, rel. to ON. eyra, Swed. ora, Dan. ore, 
OS., ODu., OHG. ora, OFris. are, Du. oor, 
MHG. ore, G. Ohr, Goth, ausd, and cogn. with 
Gk. ou?, gen. wto? (for ^oocto?, resp. ^ouoaxo?), 
L. auris (for *ausis), Avestic ushi, ‘both ears’, 
OSlav. ucho (gen. ulese, dual uii), Lith. ousts, 
Lett, auss, OPruss. ausins (acc. pi.), OIr. au, 6, 
‘ear’, Arm. unkn (for *uson-qo-m ), Alb. ves, 
‘ear’, All these words derive fr. I.-E, base *au 
‘ear’. Cp. aural, ‘pertaining to the ear’, auricle, 
auscultation, orillion, ormer, oto-, oyer, oyez. 
Cp. also acroama. 

Derivatives: ear-ed, adj., ear ing (q.v.) 
ear of corn, n. — ME. ere, ear, fr, OE. eare, rel. 
to Du. aar , OHG. ehir, ahir, MHG. eher, G. 
Ahre, ON. ax, Goth, ahs, ‘ear of corn’, fr. Teut. 
*ahiz, corresponding to I.-E. *akos-, whence L. 
acus, ‘chaff, husk’, Gk. axoorr), ‘barley’, lit. ‘the 
awny one’, fr. I.-E. base *ak-, ‘to be sharp or 
pointed’, whence also L. acer , ‘sharp, pointed’. 
See acrid and cp. words there referred to. 
Derivative: ear-ed, adj. 

ear, tr. v., to plow {archaic or obsol.) — ME.
```


## [2026-09-07T20:25:30.963Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD anos/os/askarag ===\"; grep -n -i \"anos\\|^os \\|osyar\\|askarag\\|'skl'k\" PHD_mackenzie.txt | head -20; echo \"=== NYB anos ===\"; grep -n -i \"anos\\|ōš\\b\" NYB_vol2_glossary.txt | head -10",
 "description": "Grep MacKenzie/Nyberg for anōš, ōš, āškārag"
}
```


### [2026-09-07T20:25:31.028Z] TOOL RESULT

```
=== PHD anos/os/askarag ===
1118:anos pnwf] lit. immortal, i.e. the next life; elixir, antidote.
1124:anOs-xwar [)nwshwl] mortal.
1267:askarAg ['/k)l(')k l I M )Iq)rg, N tUkara] obvious, evident.
1269:askaragenidan ['Ik)l'kyn-ytn l ] reveal, confess.
3877:osyar ['wsd'l I N h-] conscious.
5918:agreeable ham-dadestan.                   antidote anos, Jud-bes, piidzahr.
6281:content(ed) abemust, hunsand, hu-            countless amar(ag), anosmar, asag.
6328:cultivation abadanih.                         fight to ....., anos xwardan.
6333: cure besb(en)-.                           deceased anosagruwiin; v. blessed.
6520:evident askarAg, nigerisnig.                       extend, cause to ...... rawenidan.
6862:    deficiency.                           infirm anost; armest.
6864: immortal ahos, amarg, anos(ag).          inform agahenidan, azdenidan.
6865: immortality ahosih, amargih, anosa-      ingratitude anespasih.
6881:  innumerable amar, anosmar, asag.
6969:late (deceased) anosagruwan, hufra-       Libra Tariiziig.
7131:mortal anosxwar, gehanig, marg-                nature Cihr(ag), gohr(ag); ciyunih;
7845:                                         unreliable anost.
11873:osyar                   ~,.,               hanJam-                    -~~,..
11977:ogar                        ~.~~       anos                            ..-0,..-
11978:ogar-                      -~-',.-     anosxwar                  )~".,
=== NYB anos ===
463:Anēšē-zātān [/nw&yc?t?n'] patr. of Anošč- zat, the father (or ancestor) of Mihrak 1322, 1525. — From anos = anēšak + zat (q. v.) ‘Immortal-born’; as to the ending -ë in the composition cf s.v. mēnēt.
1004:rarudenc; patron. Prth 1. 28 = Prs 1. 24 bythškn, Gr. v. rırıdıyav; Paikuli = KZS. Arm. lw. bdeašx (Hübschmann, AG 119 sg.). Georg: Armazi bilinguis (Nyberg, Eranos 44, 1946, 228-243; 233 sqq.) bthš, Gr v. nırıadEng also on gems found there (l.c.; v. also Eränsahr 169), Armazi “Aram.” inscr. (Altheim & Stiel, FuF 35, 1961, 172-178) pyihš; native K art'veli patiaxsi, pitiaxši (Hübschmann, Tschen- keli). Syr. lw. ptahšā, ptakša (often faultily vocalized), aftakšā (Hoffmann, Auszüge p. 34 n. 275). Amm. Marc. XXIII, 6: 14 vitaxae (“id est magistri equitum"), Gr. Hesych. Btorač, read Birač. In dealing with its etymology the indigenous form bythš should; as a matter of course, be given preference before any deviating forms in foreign languages. In its oldest form it is, however, found in Arm bdea&r < *bdiaxs: -d- must be secondary (an original d would have given 7) and go back to a f, voiced because of its proximity to the preceding b, which consequently must be the original initial consonant, not p (pt- would have re- mained); this phonetic state is cogently conclusive in favour of an original form "bitiyaxši-. The first element is *bitīya- ‘the second’, NW form of "dvitiya; Av. (963 sg.) bitya-, MPrth. bdyg (Nyberg, l. e. 237 n. 2; Henning, Iranistik 62 n. 2); the second element has been explained by Pagliaro (RSO XII, 1929, 164 sqq.) as *axsi- ‘eye’ (in Av. derivatives, v. also apaxš); *bītīya-axši- ‘the second eye’ of the King, based on the idea, well attested by the classical authors. and well ana- lysed by P., of the King’s officials as his “eyes”. Thus any etymology starting from initial ptt- is peremptorily excluded; pit- for bit- must be due to a secondary development in the borrowing languages. Pagliaro, l.c. 160-168; Eilers IIJ V, 1962, 209 sq. (quotes Armazi pythé, but ignores bihš!); Benveniste, Titres 65; Rundgren, OrSu XII (1963), 1964, 89-98 (oh!); ete.
2020:+honéh [*hwnyh, for **nwš] "down there: ~ tdvarém [ŠTHn-ym = hwlym: z"a- rem, wrong reading of ’wlym] let us go down there, descend .(to the plain mentioned immediately after) 192%. — The text of the MSS: "nwš ŠTHn-ym = anos xYarém is void of sense here (anēš- z"ar ‘enjoying immortality’ Phl Vd.
3208:Rag [l'k']the name of a district and a town: né ka étar har 2 6 ham rasénd ~ u Notar not (even) when the two, Rag and Notar, come together here (i.e., never) 4316-17, 5017; fratom hac ax" 4 astomand andar ~ u Notar as the first of terrestrial beings between R. and N. (— far and wide, throughout the world) 5317-18, — A proverbial saying using op- posites to symbolize either absurdity or comprehensiveness. The saying is mean- ingless unless it refers to actual and well known geographical facts. Notar, other- wise unknown as a place-name, can only refer to the country of King Vištaspa, who derived his origin from Naotara the son of Manušcihr, thus symbolizing Eastern Iran (the Notars founded Tis, 1147-8). Rag must then be the OP Raga mentioned in the Behistun inseription (270, 32) as a district in Media ('Pdyat, called xčpoc by Arrianos III, 20, 2), thus representing Western Iran. That this dis- - trict had, already in Achaemenian time, a capital of the same name can scarcely be doubted, and is not contradicted by Strabo’s notice (C 525) that Alexander’s general Nikanor founded, besides other
4835:Eranos, Acta philologiea Suecana.
```


## [2026-09-07T20:25:41.148Z] TOOL CALL #52: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Read ref_page.py header"
}
```


### [2026-09-07T20:25:41.196Z] TOOL RESULT

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


## [2026-09-07T20:25:44.002Z] TOOL CALL #53: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:124 2>&1 | head -60",
 "description": "Fetch Borhan-e Qate page 124"
}
```


### [2026-09-07T20:25:45.314Z] TOOL RESULT

```
no scan of BQT covers printed page 124 (see 'scans' in refs_online.json)
```


## [2026-09-07T20:25:50.101Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v1_pages.txt | head -3; echo ...; grep -n \"استخوان\" BQT_v1_pages.txt | head -10",
 "description": "Search Borhan v1 for ostoxan"
}
```


### [2026-09-07T20:25:50.175Z] TOOL RESULT

```
...
1675:دساتبر برده مشت مشت از لفت های ناهنجار آن بر داشته مانند استخوان
6744:استخوان (۲) را نیز گفته‌اندکسه در زمر کردن
6763:۲ خر لك » بر وزن ناخنك » استخوانی
7484:«بناص 2۱۷۹ » خواناری 61۷272 < سالنامة گلپایگان 4۷ > هربك از دوقطمه استخوان که
7523:استخوان دار است و گوشت آن لذیذ است
10541:استخواندار , که در آب های ابران چندان ‌
11620:استخواندار که بچةٌ ماهیان پربهارا میخورد واز همین نظر ماهی
11732:و استخوان آدمی و ساير حیوانات ۴ - و تشم
11773:۴ رك : هستهواستخوان .
11810:۵ - فرات استخوان 25021۷20 پهلوی و ۳ پارسی با - 981 ِِ ره
```


## [2026-09-07T20:25:52.929Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11760,11830p' BQT_v1_pages.txt",
 "description": "Read Borhan v1 around ast/ostoxan entry"
}
```


### [2026-09-07T20:25:52.972Z] TOOL RESULT

```
استأث * - جنماولوسکون‌دال, آعوز کار
و آموزانده باشد - و داند صنمتی از امور
کلیه و جزلیه را دز استاد کودند . ۶
استاد باك » بکر اول.نم‌شهریانت
در طبرستان مشهور باسترآباد *۷.
استاده ه بکر اول ممروف است که
متاره و ک و کب باشد- و شامیانه و سایبان راهم
گفته اند - و مسطر فولادی و چوب جدول
کشانرا نیز گوبند - و بمعنی طنبور سه تار هم
هست - و نام بلوکی است از مضافات لاعیجان
0- و نام قلعهای باشد از ملك دکن ۹
استاقیل ۷۳ ۰ بر وزن اس‌افیل. بلفت
رومی انگور را گوبند و بعریی عنب خوانند .
۴ رك : هستهواستخوان .
۸ - ره : زند
پازند 01 « باروج ۹4
استان . 9۰ - رگ : استرآباد .
فرمنگی لامیجان برصر راه رشت
۶ اشت: ی«
و
- بونانی قآلاناها٩‏ ( دانهٌ انگور )
۵ استاده - رکه : اتاده .یعتی باز داشت و منم دفتن کرد .
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
ین ۴ طبری أا5ه ء مازنسرانی کنونی 25061 , اقدعه
« واژه نامه ۸۳۹ ۰ . گیلکی 65۱275 . ۴ - ور اوستا 5021662 « قوی , محکم؛ سخت *
4 . ۳۵۷ . 6۷675 . ۵ . 2۲1۵۲0 وشهر ی را بمناست انتحکامات ظاهرآبدین نام
خوانند نی مستحک . ( از افادات استاد پور داود .
۵ - فرات استخوان 25021۷20 پهلوی و ۳ پارسی با - 981 ِِ ره
سانسکریت بممنی عظم عربی فقط جزء اول کامه را آشکار میسازد . در مغرب ایران استصمال
کلمهٌ استخوان محدود است ولی لهجه‌های شرقی را حفظ کرده‌اند ازرة - 250213 *# :
سضدی 26اه , استی 58 ۰ منجی 05018 , اشکاشمی ۱۷25011 ۰ وخی 22506
منگلچی 8508 . بننویی علقنا؟ . لفت فارسی مزبور در پامیر نفوذی - جزمختصی - ندارد »
امادر لهجه‌های هم‌سرحدمفربابران بسیارزاد وباتعریفات متنوع‌استعمال میشود: سوندی50020,
نابینی ۱580 , کردی 300280 , کورانی ۹0*20 , سمنانی 2508067 , اورامانی
8 هم در پپلوی و پارسی 2502 باکة با 25270۷20 (64۲2۵0(ا) ردو وجود
دارند ۴ رد :
۴ ص1۱ معنه‌بانگ تفاحصهنم,عممل ومرصقب ماو ماوع: مادنوهبدر8۵ ۴8۰
۰ 33 ۳۵۷۳۷۲ ۲۰ ۰ ]0
۵ استافدار - حاکم‌استان» بمل وک طبرستان « استندار»مکفنند . درپهلوی1502027
بحا کم استان (درعهد ساسایان) اطلاق مشد. «کرستسن. ماسان ۰ ص ۱۳۹ > ۰علم است بی حیوانات و نباتات » بر خلاف‌استه که اسقر » بروزن
متخصوص بانات لتعرتی کانه از مردم اصیل اف
۰ | کنترء از دواب‌تهود
و بز رکه هم هست - ونام سلاحی باشد از ی ی اه
جنگ - و تام جانورست غین علوم - واءت | سس ِ
خرما را یز گوند . تصرف را فرعون کرده
استخو ان بز رگ کنابه‌ازشخصی است٩‏ -وآستر وبطالة
جامه وا نی زکونند.۲ 44
ات که او را اصالت و نجابت و لب عالی بوده 1
```


## [2026-09-07T20:26:04.518Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# find leaf containing the astuxvan footnote\nfor i,p in enumerate(pages):\n    if 'استخوان' in p and 'سغدی' in p:\n        print('leaf',i)\n    if 'انوش' in p and 'anos' in p.lower():\n        pass\nEOF",
 "description": "Find leaf of astuxvan footnote in BQT v1"
}
```


### [2026-09-07T20:26:05.751Z] TOOL RESULT

```
leaves 777
```


## [2026-09-07T20:26:09.564Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nlines=t.split('\\n')\n# locate line 11810 (1-based) offset\noff=sum(len(l)+1 for l in lines[:11809])\ncum=0\nfor i,p in enumerate(pages):\n    cum+=len(p)+1\n    if cum>off:\n        print('leaf index',i); break\nprint('total leaves',len(pages))\nEOF",
 "description": "Map line to leaf in BQT v1"
}
```


### [2026-09-07T20:26:10.856Z] TOOL RESULT

```
leaf index 338
total leaves 777
```


## [2026-09-07T20:26:21.157Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'انوش' in p and ('anos' in p.lower() or 'anaosa' in p.lower() or 'اوستا' in p):\n        print('leaf',i, [w for w in ['انوشه','انوشیروان','انوش','نوش'] if w in p])\nEOF",
 "description": "Find anushe leaf in BQT v1"
}
```


### [2026-09-07T20:26:22.477Z] TOOL RESULT

```
leaf 64 ['انوش', 'نوش']
leaf 139 ['انوش', 'نوش']
leaf 309 ['انوشیروان', 'انوش', 'نوش']
leaf 411 ['انوشیروان', 'انوش', 'نوش']
leaf 467 ['انوش', 'نوش']
leaf 493 ['انوشیروان', 'انوش', 'نوش']
```


## [2026-09-07T20:26:30.016Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(388,396):\n    p=pages[i]\n    print('==== leaf',i, '| has انوشه:', 'انوشه' in p, '| has انوش:', 'انوش' in p)\n    print(p[:300].replace('\\n',' | '))\nEOF",
 "description": "Inspect BQT leaves near 392"
}
```


### [2026-09-07T20:26:31.298Z] TOOL RESULT

```
==== leaf 388 | has انوشه: False | has انوش: False
اندر خور | ا ندز خو در - بنمخای نفطه‌داروسکون | واو ممدو له و رای می‌نقعله 4 ممحنی اج وسزاوار | وزیبا باشد . | بمشی اندرخور است که لابق و مزاوار و زیبا | باشد . | آثدر خو دك هه بنکون داز ابید . | بمعنی اندرخور است که لابق و سزاوار و زیبا | باخد - و بختح رای دوبم بسمنی یبد است بعنی | می‌زید . | | نذر حور ند - بسکون نون 
==== leaf 389 | has انوشه: False | has انوش: False
اف | او رفتی . بکشب بای شد و آتش را بکشت | راندروی درمیان دربا کم کردید .. | سین می‌نقطه , نام یکی از حکمای بونان است | گوند درطبابت اعجاز مکاربردی ۴ | نلم مکی از مبلوزان تورانیی است ۳ | دوازده د بردست گر کین ملاد کشنه شد" شلد , | | ند ۴ بسکون کاف , تسضر اند | است , واند عددی باشد مجهول میان سه و نه | و انرا بعربی بض
==== leaf 390 | has انوشه: False | has انوش: False
انسجان | که کرفتگی دل ودلگیری باشد . | اندهان بروزن مردمان ؛ جمم انده | باشد چنانکه جانور را جانوران ومردمرا عردمان | کویند . واین جمم بخلاف‌قیای است چه‌بنیراز | جاتور را بالف ونون جمع وان کرد . | نده‌قو و » بت دوقاف و سکون دو | واو ؛ دوایی‌است که آنرا حندقوفی‌خوانشد * کلف | را نافع است , | انفی ‏ بر وزن لندی » بمعنی
==== leaf 391 | has انوشه: False | has انوش: False
رن | ار ه- باازای فارسی بر وزن غمزه ؛ | مرجماث باشد و آثرا ببربی عد ی گویند . | انسته - بفتم اول و کسرثانی و سکون | سین بی‌قطه و فتح فوفالی 4 مقصورآ دته است» | وان بیخ کیاهی باشد خوشبوی که بعربی سعد | " گو بکف . | ۰ ۰ | انشانا - بفتم اول و سکون الی وشن | فرشت ونئای مثلته هردو مالف کشیفه » بسربالی | دوابی‌است که آنرا بغ
==== leaf 392 | has انوشه: False | has انوش: False
اگارده است که افسانه و سر گذشت باشد . | انگاده ۱ ه بروزن عموارء ."هر چیز | "که افانه وس گذشت داشد - وباد گذشتها کردن | رانیز کوبند - و ازسر گرفتن سر گذشت وافانه | را عم گفته اند بطریق کنابه چنانکه ا گر کسی | بسیارومکرراز گذشته بگوید گویشدهانگاره‌میکند» | یعنی باز از سر هیگیرد - و پس پی خزنده از | شرم و حیا را نیز
==== leaf 393 | has انوشه: False | has انوش: False
مردم فررنگ «م هست ٩‏ ۰ | الث و زای قطه‌دار ساکن » سلی باشد که بآن | زمن را هموار ساز ند ۹ | انگز ح بفت اول و خم نالث: و کت | تابی و زای فارسی» آهنی باشد سر کج که فیلرا | بدان بهرطرف که خواهند بي‌ند . | انگژ د ۴ ختح اول دضم ثالث‌وسکون | انی و فتح زای فارسی ودال ابجد -اکن مطلق | صعفها را گویندعموعاً و صمفی باشد بغایت
==== leaf 394 | has انوشه: False | has انوش: False
انگشت ب حرف‌نهادن - کنابه | ازعیب کر فتن ودکته گیری کردن باشد . | ) نگشت بر دهان گد اشتن- کنابه | از<سرت واضوی - وتعجب وتحیرباشد - واشاره | کردن بخاموشی هم هست . | بضم بای ابجد وفتح رای فرشت و سکون کاف ؛ | جانورست که آنرا حوش کورمیگویند و پیوسته | درزیی زمین‌میباشد وسخ درخت ونباتات‌میخورد. | گونشد ساز و کدنا را بسب
==== leaf 395 | has انوشه: False | has انوش: False
یاف | چنکالی ومالیده 3۳ وان یش کی | با روغن وشیرینی بهم‌بمالند . | انگشتو) ۰ بکس الك و داد بالف | کشیده . نی باشد که آنرا برروی آعل زغال | وغیره بز ند. | انگشته - بنم الث بر وزن خریشته ؛ | ۳ باشد ازچوب مانشد ینجه دست ودسته یز | دارد که پرزیگران خرمن کوفته شده را بدان | بباد دهند - و بفثح ثالث برزیگربر! کوبند که | ساحب
```


## [2026-09-07T20:26:44.356Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(396,404):\n    p=pages[i]\n    print('==== leaf',i)\n    print(p[:600].replace('\\n',' | '))\nEOF",
 "description": "Inspect BQT leaves 396-403"
}
```


### [2026-09-07T20:26:45.640Z] TOOL RESULT

```
==== leaf 396
انگوز زیتونی . . | وبعربی اصابع‌المذاری گوبند . | ) نگوژه؟ - با زای فارسی بر وزن | سنبوصه ؛ صمغ درخت انکدان باشد و به_بی | حلثیت و صمن‌المحروث خوانند . و تخم آنرا | بذرالانجره وقریض کویند . | که کوی کربان وتکمة کلامرا اژآن‌بگذرانند - | است . | نف 4 - بررزن زنگوله, بمعنی‌انگول | که تکمه را ازآن میگنرانند . | انگیان؟ - نم ثالث و نحتانی بالف | کشیه وسنون زده » بررزن ومعتی انگدان است | که درخت حلمیت باشد ,و حلتیت صمغ آن | درحت است . | ) نگیتن " ح بمنی جنباایدن از جای | و برشورانبدن - و بلند ساختن وب کشیدن‌باشد ‏ | و بمعنی دور کردن - و پیدا کردن - وساخئن- | افگیر ۴ ه بر وزن زنجیر » انگور ر | کوند و بعربی عنب خوانند . | الگیژ ۴ ۰ بروزن 
==== leaf 397
نوهیان - بکرم بروزن‌مجوسیان. | لاله باشد » و درصحاحالادوبه بهمین ححنی‌باسقاط | نون آخر آورده‌استو گفنهاست که‌این لفت‌روهی | است واه اعلم .. | ) و لیفن(۱) » بروزن‌بولیدن » بسعنی | ناله و زاری و نوحه کردن باشد . | انهو با س با های هوز وبای‌ابجد پروزن | محمودا , بلغت زند و پازند (۲) ستار؛ حشتری | راگوند ۲ ی | انیب - با بای ابجدیروزن چلییا .بلفت | زند و پازند (۲) درخت مورد را کونند ؟ . | و ب رک آنرا در دواها یکار برند » و بجای بای | ابجد تای فرشت هم بنظر آمده است | آثیر پروزن امپر » خوی‌زشث وطبیصت | بد را گویند ۰ ۱ | افیر ان * -بروزن‌امیران. نم فرعته‌است | )۱ چش : الوگیدن . | ست از جر | ماه شمسی » وماین حعثی با زای نقطه‌دار بروزن | عز
==== leaf 398
کوبند که بدشواری از انا شود و حل | 9 | | ثیشه - بر‌رزن‌همینه .جاسوی‌وچاپلوی | هر چیز بسته و منجمد بأشدچه درفارسی‌سینوشن | تب ۱۵۰ , | 0 زمین ۰ ء ظرفی باشد ازسنال | مانند مو وخمچأیزگی که دوغ وا جر آ ‌کنند | او * نم اول : و سکونِ نافی » ۳ | ۳ 0 ه‌ ۰ | او اه بروزن هوا » بمعنی آوازباشد ٩‏ | -وبمعنی ابا هم هت که شوربا و آش باشد . | دفتر و حساب دبوائی باشد ۷ - و بضم‌اول کرما | و هوای کرم را یز گویشد . | آواده - بفتح اول بروزن شرآره. دفش | حمایی باشدکه حسابهای پراگندث دیوانی را در | آن نوبند و در این زمان آن دفتر را اوارجه | کویند ۸ - و بمعتی دبوان خانه بمنی‌دارالاماره | هم آهده اس تکه بار کاء ملوك وسلاطین بلشد - | و ریز آحنی را نیز گوب
==== leaf 399
رل اس | یفکن - و بشم اول ناله و زاربراگویند . * | او باریدن ۱ - بنتح اول بروزن سر | خاریدن ؛ ناجاویده فرو بردن را گویشد و بعری | پلع خوانند ‏ و بمعنی افگندن هم هست-ویضم | اول بممتی ناله و زاری کردن باشد . | 5 ۱ ۳۹ | او باش ‏ بر وزن افراش » مردم عامی | هیچ نافهمید: )۱( بی‌سرویا و جلف و بر خود | و هتعصصت را گوند ۴ ۰ | شش رهپس | پر کردن و افگندن باشد . | او برث ۱ - ینم ناك بر وزن افترد . | بحئی ناجاویده فروبرد و پلع کرد . | او ببس - نم اول وکر الك بر وزن | مونن ؛ خوش و پیوند و قرابت را گونند . | او به شم اول و سکرن انی مجپول | کر ثالث و ظهورها » دام قربه است از فرای | هرات , | اوج - بفتح اول بر وزن موج » معرب | او گه است که مقابل حضیض 
==== leaf 400
واجب و بفستا وا گیبتد و جر هی اهنت » | و آن‌قدارست ازسرانگشت ,کوچك ۷ مرانگشت | بزر که دست آدمی ۰ | اوذست » بروژن بدست » بمعنی‌آودی | اس ت که وجب و بدست وشبر باشد . | و مدشه‌ایست . | ذاز شلمدار وسکون رای بی‌شطه ؛ بات بونانی ۷ | آب را گویشد و مربی ماء خوائند . | آور » پم اول‌بروزن مور . بمعنی‌مشت | باشد عمواً و عشتی را گویند که بر دهن شخصی | زنند خصوساً - و بادام و پسته وکردکان وامثال | آ ها را یز گونندکه مغزشان نایم و یز شده | باشد . ۱ | آودا - بختح اود و سکون تالی و ثالث | مالف کشده , حصار و قلمه راکوشد . | فراز وبالا و بلندی باشد ۴ . | آوداشتی - بر وزن و ععنی برداشتن | و بلند ساختن و افراختن باشد ۴ . | اوداهي » بن اول و فتم میب
==== leaf 401
ای ۸ اه | نیز خواشد ره ۳ | اورمز ۱ نم اول و میم و سکون | وین ثالث و زای قطمدار . دام متارة | ی باشد - و فام روز اول است از هر صله | نيك است در این روز نو پوشیدن‌وسفر | کردن" و مهر بر کاغذ نهادن » و بد است قرض | و وام دادن - و نام فرشته ایست که تدییر لمور | اسفندیار هم هستِ که بسر بهمن باشد . | اودهز ۵ ۱ » پروزن روز دزد » بمعنی | اورمز است که نام روز اول از حرمله شمسی - | و نم ستار؟ مشتری -.و لام فرشته ای که موکل | ات تلم بسرزاده اسفندبار | اورمك « پروزن اوزيك , کلاموطاقی | پهمین‌را گویند,وسنی‌این‌لفت ران رکی‌میدانند ۴ . | آود نج - تال وثالك و سکون‌نالی | و نون و جیم » سکه الگور را کویشد و آرا | و جم ال و سکون انی مجهول » چوب خ
==== leaf 402
آوروختن | آود و ختن ه بروزن و معنی افروخئن | است. که روشن کردن: آنشس و چراغ باشد ۷ .: | آوده » بفتح اول و ثاكك وسکون‌انی » | بمعنی ابره است که روی فبا و کلاه و امثال ان | باشد, چه درفارسی با و واو بهم نبد بل‌می با بند ‌- | اور یا ۴ ه بر وزن بوربا» نام شخصی | است که داود علیه‌السلام او را بجنك فرستاد واو | ۳ جنک کته شد و داود زن او را خواست | سلیتان عله‌الملام از ان زن بهم دسید ؛ ویسنی | گوند جد مادری سلیمان است و جمعی گویند | برادز داود عله‌السلام بود . | ۱ اور لت هن اول و خفای نانی و کسر | الث و سکون تحتانی و بای ابجد» آنست که در | عربی محرف و بت رکی قیقاح گویند . * | "او رف هت یک ثات و سکون واو ؛ | بروزن و معنی اوربباست که
==== leaf 403
ی و ای | ع ‏ به ۷ ج جم حممي یه ۶" چا + ف ( ۲[ ج هو مه | ۳ 2 | ۳ | ۱۲ | ۳ 5 | ۴ اه | ۵اه | کدی نع | 1 پدیم‌ر(ید._ | هرز | ع۴غطع | اصونل خدا ۳ | ۲ تس( ]ار ۱ 3 | ری رکراه) رسد ایدا 2۶ | اعا ۹ | ری و 4 پلاس ۳ -72] ]| جزه, فره ۹ | او ص دویسم ای اوسعَة ید | اشم.خم ب | او رگشبه) وود اه | جرف ۳ 1 | | زد رس طکه 6 یر فا ول دس ت نمسندا سین .حانه 9 اد | ! دگرنای )ان (رش 8۱۳24 راست ,دست له 0۶ ) 5 | یه 66 ند جرد جر نت اصعبعوق | رانا رورشد (ممدا) ع | ز وراه ورتم دملد او ارو 29۳۵ تعارز 0 | ز (اراه ویر ات 4 | آ و رکشده) [ید<6 ره وت و (وساة | او نهد (س تراد مهم | دم »بر _ | ان ترسیری مس () نتم وحصگ» اند + صأنه | ] (دیچن) ری زد خن ۱ ی 6 | ۹ 5 مند 6 مب کاعٌه ه
```


## [2026-09-07T20:27:09.773Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[396][600:]); print('#########397'); print(pages[397][600:1800])\nEOF",
 "description": "Print rest of BQT leaves 396-397"
}
```


### [2026-09-07T20:27:11.149Z] TOOL RESULT

```
مهمیز » بمعنی بر
انگخته - و بلند ساخته و بر خیژانیده باشد.
انگیز و 6
٩‏ رك : انگد .
۵ انگیز+-ه(آا كت وسبب).
« بروزن کفلیزه » بمه‌نی سبب
وبا چیزها باشد . ۶
انگسی « با کاف تازی بروزن ادرمی .
0 ی از اشکال رمل - و در عریی‌یمعنی
گفته وب رکشتن باشد .
انگیل - با کاف فارسی بروزن زئبیل .
حلقه‌ای را گوشد که کوی گریبان و کم کلاء
را از آن مگذرانند 9 تکمه و گوی گریبان را
انگیله - بروزن غربیله ۰ بمعنی انگیل
است که وی کربان- وحلقة گوی کریبان باشد.
اثویا - بفتح.اول رضم انی وسکون
واو و بای فارسی بالف کشده کار زبان تلخ را
گوند , و آن گیاهی است که در دوا ها بکار
برند - وکاسنی را تیز گفته اندکه بعرمی هندبا
خوانشد ۱.
)ور سها - با را و سین بی‌نقطه ومیم
بر وزن ابودردا ؛ بلفت بونانی ۷ سیلان خورا
آفو شا با ناك مجپول و شین قطمدار
بالف کشیده » مذهب وکیش کبراترا گوبند -
وییعنئی شادی و خرمی وعدالت هم آمده‌است .#
او شه - بنتح اول و رابع بمعنی خوش
و خوشاو خرم و خوشحال باشد - و شراب
انگوری را نیز گفته‌اند - و نام عمة شاپور حم
هست - و پادشاء نوجوانرا نیز گویند - و بستی
آفرین و باركافه هم آمده است که بر بی‌طوبی
و مرحبا خوانند ؛ و منم اول نی زکنته‌اند ۸ .۵
۴ رث : انگور.
۷۲ - مونانی 4060۲15۳12 دائتینگاس»
انوهیروان ی رد . الوشروان -
6۷۹ ظ
#########397
یزان هم آمده است ۵ ۱
افیرٌ ‏ با زای‌فارسی پروزن کنیزه کیاهی
بزد .
عریی عین کویند - و اثارت بسحیوب و مطلوب
هم هست ۰
بیهوده . و خلاف و کذب ودروغ ومخالت باشد .
] یسون - بروزن‌شبیخون. بلفت بوهانی
نم حای بی‌هطه , نشنگی را فرو نشالد و شکم
را پیشدد . و بضی کوبند انیسون عربی است نه
بودانی ۱ - و بمنی اسان هم آعده اس تکه
بیهوده و خلاف و کذب و دروغ باشد .
افیسه ‏ پروزن هرسه ۰ هرچیز بستهرا
۱ - بیودالی 80600008 «اشتینکاس*. ۴ _ فرالت غلطکلمة بپلوی۵11۳۳۳0224 که آنرا
ئً ازمنة آخیر 299۱3۵09۵ میشو اند ند و مولف برهان بجای میم باه آورده آ[ رد 0 بوثکر ۹۰
اوهرمز د,خداست و چون اورمزد در فارسی بمشتری اطلاق شده . بفعتی آخیر در من آمده ات .
هن , 20102 هاری 0007 یمعنی مورد « بوتکر ۰۹۰ ؛ پي ائیبا .
حصوحف ۶ انتا تا » است
۴ در رس 2 200881178, درپهلوی ویارسی آنیران . جزواول‌خود مر کتاست
از 20 علامت نفی و غرم بمعنی پابان و حد و حصر ؛ و جزو دوم بمعنی روشن است . جمعایعنی
روشنی بی‌پابان . انفره رئوچه بار گاه جلال اهورمزدا با عرش اعظم محسوب شده - علاوه بر آن
نلم ایزدی است که نگهبانی روزسیام بدو سپرده شده . ابورسحان در فهرست روز های ایزانی‌این
روز را «البران» و درسفدی «نفر» و در خوارزمی وزع ورده و زرتشتبان امروز «انارام» گوبند
«روزشماری 4۹۱۸-۹٩‏ تفرگ انیران از اوستابی 28۲72 - 80 مرک از 21 علامت لفی وجزو
دوم بمعنی آرب
```


## [2026-09-07T20:27:35.882Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (339,340,341,342):\n    print('==== leaf',i)\n    print(pages[i][:1400].replace('\\n',' | '))\nEOF",
 "description": "Inspect BQT leaves 339-342"
}
```


### [2026-09-07T20:27:37.125Z] TOOL RESULT

```
==== leaf 339
علم است بی حیوانات و نباتات » بر خلاف‌استه که اسقر » بروزن | متخصوص بانات لتعرتی کانه از مردم اصیل اف | ۰ | کنترء از دواب‌تهود | و بز رکه هم هست - ونام سلاحی باشد از ی ی اه | جنگ - و تام جانورست غین علوم - واءت | سس ِ | خرما را یز گوند . تصرف را فرعون کرده | استخو ان بز رگ کنابه‌ازشخصی است٩‏ -وآستر وبطالة | جامه وا نی زکونند.۲ 44 | ات که او را اصالت و نجابت و لب عالی بوده 1 | باشد ۳ استر اد ب بکر اول د‌ فتح الث‌بروزن | بیمدار » نام غله‌ایست که آنرا مرجمك خواشد» | و بعربی عدس کویند . ۱ | استر خا - بکر اوز. و اك و خای | نقطه دار » لغتی بونالی بمعتی زرنیخ سرخ است | و آن نوعی از زرتیخ باشد که ارباب عمل داخل | ا کی ی کنند وزریخ‌احمرهمان‌است . اکرباصارة | ب رکه درخت بزرالینج برشیب بق ل که موی آنرا | کنده باشند طلاکنند دیگر برنباید ۰ و بفتح | وضم اول لیز گنته اند » و بجای حرف ثاكث بای | ابید هم بنظی آعده است » و بامقاط تالف ۳ | باین معنی لوشئه آند که‌اسرخا بادوان اعلم؟ . | استر دن - بتم شم اول و الث و فتح دال | ابجد بر وزن درسفتن ؛ بمعنی تراشیدن و باه | ساختن و محو کردن باشد . | ادتخوان در گلو گرفتن - | کنابه از رنج و محنت کشیدن باشد . | استحوان ریا صم رای قرشت | و بای ابجد بالف کشیده , پرنده ابست که آلرا | بعربی همای گویند , وذای او استخوان‌جانوران | باشل . | استخو ان ر ند فتحم رای فرشت | وسکون نون‌ودال ابجد. بممنی استخوان رباست | استخوان خورد . | استخوان د نگه - باکاف فارسی . | بر وزن و معنی استخوان رند است کد همای | باشد . *# | 62۲00 . 0.۶ سانسکرت ۸۲۵ 95۷2 : جزهء اول آن 25۷2 بمعنی اسب است‎ - ۱٩ | 2508۲ ان .1۳20 و راك : کوتینا . در پهلوی‎ . 1 . 2۳0 . 2 ۸۵
==== leaf 340
استرش -ایم اول و لت و قحرابم | و سکون‌شین قرشت ۰ آنی راکوبند کهزمین‌را | بدان شیار کنند . | وسکون‌ثانی ونون وکاف فارسی» مردم کیاه باشد, | وآن گیاهبت مانند مردم و نگونار بود ورسشة | آن بجای موی‌سر باشد . نر وماده بهم‌در آميخته | و دستها در: گردن بکدیگر کرده و پابها در حم | محکم نموده . گویند هرکس آن گیاء را بکند | حلاك مشود پس بدین واسطه اک رکسی خواهد | آنرا بکند او حوالی واطراف آنرا خالیمیکند | وسگی کرسنه را رسمانی ب رکمر می بندد وس | دیگر رسمانرا بر ربثه آن و قدری کوشت در | بش آن‌سک بدور می ادازد ابقوت آن سکه | کیاء از بیخ کنده میشود و سگه بعداز چندروز | میمیرد و آترا سکه | کن‌باین اعتبارمیگوبنده | و بتازی ببروح ( ۱) | است‌خوانند. و گوشد | اکر کسی بنام شخصی | بك عضو از اعضای او | را جدا کند در حمان | روز با روزدبگر همان | عو آن شخصرا تجدا اترنگه:ا. گل؛ ب؛هیوه | کنند . و بکسر اول نیز گفتهافد - | استر ون » بفتح اول و واو بر وزن | چشمك زن » زنی را کوبند که حرکز زابد | واورا جربی عیمه خوانند . و معتی ت رکیبی آن | استرمانند است چه ون بمعنی مانند هم آمده | است ۰ | (۱) چك . چش : ببروح ! | تس . | استر و تین بر وزن ادرون تن » بذ | لت زند ویلزند(۲) بممنی‌بستن باش که 9 | کشودن است . | ی نم 4 و ات در ره | ۳ یکسرلام ۰ کنابه از | دلیری وجانبازی کردن باشد . | استطلس- بکسر اول وفتح تاث وضم | لام و سکون ثانی و طا وسین می نفطه » یلفت | بوئانی نوعی از حومیابی باشد و آن مانند زفت | است و بوی قیی از آن می‌آید و در شکستکی | و کوفتگیاعضا عمل‌مومیابیمیکندرآنرا مومیابی | تتانی رسیده ولام یال 9 ار بوده | نورانی درلشگر افراسیاب .*3 | استل « بکر اول وفتح ناك‌وسکون. | ثانی و لام ؛ تالاب و آبگی
==== leaf 341
وت ۱ تیم | استوی بش اول والث بر وزت بر | کوی » مهر پشت را کویند . | استه * ه ختح اول بروزن خسته , دالةٌ. | خرما و شفتالو و زردآ لو ء امثال آبرا کوبند - | واستضوانآ دمی‌وحبوانات. دبگررایز گفتهان - | وضم اول کفل وسرین را کوبند -و بکر اول | وضم تاكث وظهورهای هوز مضفف امتوه است که | ملول وتشکهآمده ومانده شده‌باشد - وبکنراول | وثالث وظهوها بمعنی ستیزه ولجاجت. باشد . | استهیتن- بکر اول وثاكث : بمعنی | لجاجت کزدن ونتیزه نمودن باشد . | استیا - بابای حطی‌بروزن اقترا . نم | کوهیست از کوحپای مىاین هرات وغزنه . | ان پروز نکفگیر: مقداری باشد | ممین وآن ششی درم و نیم اسث . | استیژه - بکس اول » بعنی متیزه | و لجاجت و جنکه و خمومت - و خشم و کین | استیم » بنتع اول بروزن تسلیم. آستین | جلمه را گویند - وبیعتی دهان ظروف و ارانی | هست - و بکسر اول جراحتی را کویند که | ک رکه (۱ ) شده باشد بعنی سرما خورده باشد | ویع‌بی کابوی‌خوانند - ویسمتی دیوهمآمدماست | که درمقابل برست: - ومودم دلیر وصاحب قوت | وقوی‌بازو را نیز کفتهانم.: | استو ار ۱ بم اول بروزن خشکوار | بمعنی محکم و عضبوط باشد - و آمین و متمد | وامادی‌را نیز کوبند - وبمعنی باورهم حست‌چه | استوار داشتن بمعنی باورداشتن است . | استوان ۲ - بن اولو تالث بروزن | پلبلان » بسعنی استوار است که محکم و مضبوط | واهمین ومعتمد باشد. | استو‌ذان؟ - بن اول و ثاك و دا | بالف کشیده و بتون زده » دخمه ومقبرة کبران‌ر! | گوند . | استود ذ بنم اول واكث و سکون‌تالی | و رایع و رای قرشت شت ۰ هر چهار یاه را گوینه | عموماً و اسپ واستر را خصوصاً . | استون - بر وزج کلکون . بسنی | ستون باشد؟ | استوه - بکرلول ونم ثالث وسکون | نانی و راب و ها » بمنی مانده شده و 
==== leaf 342
استینه ۱ | وورم وآمای کرده باشده وی سرعابی‌را گویشد | که برجراحت زند ویاماساند . کوبند اکر آن | سرما در شبهای ماحثاب بر جراحت بهام خورد | الينه او را بکشد » و بمض دیگی جراحتی را | و ریم باشد وبدون شترزدن برییاید - و بمعنی | استبنه بروزن دستینه » تخم مرغ را | گویند . | اسجاده - با حای بی نقطه بن وزن | گهواوه 4 بلخت رومی دوابیاستکه را تودری | وکلگون . وبهترین آن زرد باشد » سرطان را | اسر فج « بکر اول و رای فرشت | وسکون انی و نون وجیم » طبقی باشد بی کناره | که از روی سازند وبریشت آن قبه کنند وبندی | بر آن بگذارند و روزهای جشن ونماشا دو تای | آنرا بردست گرفته برهم زنند تا از آن صدابی | بر‌آید و آنرا سنج نیز گوبند - و سرنج را لیز | گفته‌اند ءوآن رنگی باشد همروف که تفاشان | و مصوران بکار بررند و سوخشگی‌ها را یز نافع | است . | اسر وش ۴ « بنم اول.وثاك وسکون | تانی و واو و شین قرشت » بممنی آواز خوش | زا | باشد- وفرشته را نیز گوندمطلقا و‌فرشتهامست | که تدیر امور بئدکان بدست اوست - وفلم روز | حفدهم از حرماه شمسی هم هست . | اسر و شنه - بکسر اولو فتح ثالث وشین | ولون بر وزن می حوصله » للم شهرست ازولات | ماوراء النهر ء و جم اول و ثالث اصح است . | اسر شم * بکراو » سریشم را کوند | و آن دو توع است: یکی آنکه از پوست کاو | میش وکاو سازند و چیزها بدان چبانند و آنرا | بمریی غرامالجلود خوانند » و دمگری عانند پیه | بود وآفر | ازشکم ماهی برمیآورند وآناسریشم | ماهی میگویند» وحربی غراء السمك حخوانند . | اسطخر ه بللای حطی» نروزن و معنی | درآن قلمه تالاب بزرکی بوده است بنابر آن‌باین | آند و بسن یگویند معرب استضر است؟ . | اسطر « بنم اول و اك و سکون انی | و رای فرشت » بیونانی‌ترازورا
```


## [2026-09-07T20:27:52.776Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF anushe ===\"; grep -n \"انوشه\\|انوش\" FSF_pages.txt | head -10; echo \"=== KNT ast ===\"; grep -n \"bone\" KNT.txt TLM.txt | head -10",
 "description": "Grep FSF and Kent"
}
```


### [2026-09-07T20:27:52.859Z] TOOL RESULT

```
=== FSF anushe ===
2851:‫انوشه‬                                      ‫ال"‬
2854: ‫فردوسی گاه نیز به جای انوشه و نوشه‬                             ‫چرا نزد باب تو خواهشگران‬
2867:‫واه انوشه و نوشه در فرهنگ‌ها از صحاح‬              ‫(ارجاسب به سپاهیان خود گوید‪ :‬هر کس‬
2874:          ‫نیامده است‪ .‬لخت فرس این وا‬             ‫پهلوی انوشک ‪ 61205602‬مرکب از الف و‬
2877: ‫جهانگیری» رشیدی‪ ,‬برهان» عجم ووللرس‬              ‫«گوید ریدک کهانوشه هفت کشور خدای‬
2885:‫مصحح برهان» دکتر محمد معین نیز در‬                ‫انوشه بدی تابود روزگار‬
2891:                                           ‫ره‬                                         ‫انوشه‬
2924:                                  ‫گوید‪:‬‬                         ‫بدو گفت شاها انوشه بدی‬
2956: ‫انوشه‬                                    ‫‪۳‬‬
3045:                ‫آورمرد» ارمزد‪ ,‬ارمز» هرمزد» هرمز‬       ‫انوشه کسی کو بمیرد به زهر‬
=== KNT ast ===
```


## [2026-09-07T20:27:54.192Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON xastu ===\"; grep -n \"خستو\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10; echo \"=== ARY ostoxan ===\"; grep -n \"استخوان\\|هسته\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Mo'in and Aryanpur"
}
```


### [2026-09-07T20:27:54.322Z] TOOL RESULT

```
=== MON xastu ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:9175:اقرار کردن» خستو شدن. قبول کردن؛ 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:14290:کردن» خستو شدن.» مقر شدن. (امسص.) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:15468:اقرار: ۰ ۲ [ع. ۰] (مص‌ل.) خستو شدن» مقر 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:15471:خستویی» اعتراف؛ ج‌. اقرارات. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:29735:مطیع ؛ مقر» معتر ف» خستو. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:42540:قرار دادن. خستو کردن» مقر کردن» به اقرار 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:56448:حستو: اد [- خستون] (ص.) مقر » 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:56449:معترف؛ ج. خستوان؛ مق. ناخستو. 
MON_part2.txt:63041:معتر ف؛ خستو. 
MON_part2.txt:71424:ناخستو: 210 [- ناخستون] (ص.) 
=== ARY ostoxan ===
327:دارد. استخوان اسب موجود درکنار برخی جسدها نشان می‌دهد که اسب بزرگان را با جسد آنها دفن .|
330:نرع جمجمه‌ها (رأس و پیشانی بلند و استخوان‌های گونه‌ی برجسته) و شاخص سر آنها ا
701:و تپه‌های کوچکی بر فراز آنها قرار دارد. در درون آنها استخوان انسان و اسب و گهگاه اجاقی و اسلحه
1524:۴ معلی اين واژه در برخی زبان‌های رومانس: زند زبرین؛ استخوان آرنج.
2527:واژه‌ی فارسی آهست" (پهلوی ۸87 ,۸87۸0 به چم "استخوان" و "هسته‌ی میوه" نیز از همین واجربشه است ۱
7545:چم این واژه در زبان انگلیسی امروز: آهسته جاری شدن» (خون) آمدن؛ گل و لای» خون نیمه لخته.
11015:شانه (به چم "استخوان کلف" و "کثیف) / ۳۷۳
11050:۴ در پیشتر زبان‌های هند و اروپایی این واجریشه به چم "استخوان کف" بکار می‌رفنه و شکل و کاربرد این
11051:استخوان برای کندن و ضربه زدن منجر به پیدایش واژه‌ها و چم‌های دیگر شده املی ار
13105:چم این واژه در زبان یونانی؛ بند استخوان» فوزکك.
```


## [2026-09-07T20:28:03.643Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2840,2900p' FSF_pages.txt",
 "description": "Read FSF anushe entry"
}
```


### [2026-09-07T20:28:03.682Z] TOOL RESULT

```
 ‫بر پاداشتن» از جای جنباندن و جهانیدن‪.‬‬           ‫ازینسان که هستی بپنداشتم‬
                            ‫به هیجان آوردن‪:‬‬      ‫(‪)۵-۲۱۱-۰۸۴‬‬
       ‫چه چاره است جز خون او ریختن‬                       ‫انزاصر خسرو (دیوان ‪)۷۳۴-۰۲‬‬

 ‫(‪)۲-۵۲-۲۲۲‬‬
                                                         ‫جز علم نیست بهر تو زین عالم‬
                                                 ‫زنهار تاکهخوارش ننگاری‬
           ‫برانگیخت آن رخش رویینه سم‬
‫برآمد خحروشیدن گاو دم‬
                                                ‫بیشتر معنی باور کردن‪ ,‬پذیرفتن برمیاید‬
‫(‪)۳۸۶۲-۲‬‬
‫انوشه‬                                      ‫ال"‬


 ‫فردوسی گاه نیز به جای انوشه و نوشه‬                             ‫چرا نزد باب تو خواهشگران‬
    ‫واه جاودان یاجاوید را بهکارمی‌برد‪:‬‬           ‫نینگیزی از هر سوی مهتران‬
           ‫هميشه تو را جاودان باد روز‬             ‫(‪)۵-۶۶-۶۸۵‬‬
‫به شادی و بدخواه را پشت کوز‬                                            ‫انگیزند (بهفتحزاو نون)‬
 ‫)‪(۳-۲1-400‬‬                                                                 ‫مخفف انگیزاند‪:‬‬

            ‫فرودی تو ای شهریار جوان‬               ‫از هزار بیت دیقی در شاهنامه‬

 ‫که جاوید بادی به روشن‌روان‬                                                   ‫(‪)۶-۴۰۱-۲۶۵‬‬
‫‏)‪(OVA-FF-F‬‬                                               ‫هر آن کز میان باره انگیزند‬
        ‫که‌ای شاه پیروز جاوید زی‬                  ‫بگرداندش پشت و بگریزند‬
 ‫که خود جاودان زندگی را سزی‬                              ‫من او را دهم دختر خویش را‬
 ‫(‪۵-۰۱-۱‬ع)‬                                       ‫سپارم بدو لشکر خویش را‬
‫واه انوشه و نوشه در فرهنگ‌ها از صحاح‬              ‫(ارجاسب به سپاهیان خود گوید‪ :‬هر کس‬
‫گرفته تا جهانگیری‪ ,‬رشیدی پرهان» غیاث؛‬             ‫اسب برانگیزاند و زریر رااز میدان بگریزاند‪)..‬‬
‫بهار عجم‪ .‬ووللرس‪ ,‬لغت شهنامة عبدالقادر‬                                 ‫ه)‬   ‫شخفف‬ ‫وه (م‬‫ننوش‬‫اشه =‬
                                                                                              ‫انو‬
 ‫واوید‬ ‫میرگ ج‬    ‫‌معن‬‫بفیبه‬
                         ‫وهرست ول‬   ‫ف‬                                    ‫‪-۱‬بی‌مرگ‪ .‬جاوید‪:‬‬
 ‫تالا‬ ‫ضر‬‫ازه‬
          ‫نیامده است‪ .‬لخت فرس این وا‬             ‫پهلوی انوشک ‪ 61205602‬مرکب از الف و‬
                                  ‫ندارد‪.‬‬         ‫نون (نشانة نفی) ‪ +‬نوش = هوش بهمعنی‬
 ‫از این گذشته در فرهنگ‌های‬                       ‫مرگ نیستی‪ .‬روی هم‌رفته ب=ی‌مرگ‪:‬‬
 ‫جهانگیری» رشیدی‪ ,‬برهان» عجم ووللرس‬              ‫«گوید ریدک کهانوشه هفت کشور خدای‬
 ‫برای وا نوشه به معنی خوش و خوشی‬                                ‫خوش انجام فرماید بودن»‬
‫و خوشحال و خرم این بیت شاهنامه‌را‬                        ‫خسرو خوش انجام فرماید بودن»‬
 ‫وه خطا شاهد‬
           ‫نادرست خوانده‌اند ب‬                   ‫(خسرو و ریدک» ص ‪ ۷۱‬بند ‪)۰۲‬‬
                              ‫آورده‌اند‪.‬‬          ‫و نیز اهش (الف نسفی ‪+‬هش =مرگ)‬
          ‫نماند برین خاک خونخوار کس‬                             ‫‪( 156‬یوستی بندهش ‪)۰۸‬‬
‫تورا نوشه از راستی باد و بس‬                                     ‫بگدفوت پیرانکهایشهریار‬
‫مصحح برهان» دکتر محمد معین نیز در‬                ‫انوشه بدی تابود روزگار‬
‫حاشيهة برهان همین بیت را بههمین شکل‬               ‫(‪)۳۰۲۷۰۶۱۱۱‬‬

‫برای واژ؛ «نوشه» به معنای «خوش و خوشاو‬                      ‫که نوشه زی ای شاه تا جاودان‬
‫خوشی و حوشحال و رم از فرهنگ‬                      ‫ز جان تو کوته بد بدگمان‬
    ‫رشیدی نقل کرده و شاهد اورده است‪.‬‬              ‫(‪)۱-۵۹۱-۵۰‬‬
                                           ‫ره‬                                         ‫انوشه‬

              ‫کنون هرچ دانید ککرزدگار‬           ‫در صورتی که این واژه در این بیت‬
 ‫بود رستگاری به روز شمار‬                           ‫نوشه [با نون]نیست تووشه ]تباا]است‪.‬‬
           ‫بجویید و آن توشهة رکهنید‬             ‫یک معنی توشه خورد و خحوراکی است که‬
‫کوته کنید‬    ‫بکوشید تارنج‬                             ‫رفع گرسنگی کند‪ .‬فردوسی فرماید‪:‬‬
 ‫)‪(1-۷4-4۳‬‬                                                ‫بسنده کنمزین جهان گوشه‌ای‬
   ‫(امه‬
      ‫‌ین‬
        ‫بسد‬
```


## [2026-09-07T20:28:04.400Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2500,2535p' incoming/ARY/ARY_pages.txt",
 "description": "Read Aryanpur context"
}
```


### [2026-09-07T20:28:04.436Z] TOOL RESULT

```
۱ یادداشت:
چم این واژه در اوستایی: ستحکم» محکم» یرومند.
چم اين واژه در سانسکریت: پایداری» مقاومت(می‌کند).
چم اين واژه در زبان‌های ژرمنی: پولاد.
اوستایی (/۸874): ۰ ۸81 بوهمی (/80/4814140): 107
پهلوی (۲1مالظه‌ه): :6 ,آک۸8 اسلراکی 5101۸0): ان
0 ,الق2ن1 ۸87 یتوانی (4۷اللالا 2 7لر): قماتاه هط
اوستی (0597/0): تا ایر دی کهن (50ل#/ صاه): ۸
کردی (0070/880): 11381۲ ,810201 برتونی (/88270): لد اراک نکن
سانسکریت (84۸/5877): تقا ۸1 آلبانی (الفاهشتم: متکاکه ,۸57
۸5 هیت (01771778: 1۸7۸
ارمنی (۸45۸7121): 05
یونانی 088/0): 00 پسگشت‌ها 5
لاتین (700مم: 0588016 ,055 ,05 8 70808000
| فرانسه (850/24): 95 9 (0838018) همه
اسپانیایی (5۸۸۷73[4): 10 6 (089) :هام05
ایتالیایی (7همامقه17): 030 1 +25( 2
رومانی (۷ل۸۸7]۸(): 05 207 8 لاه
پرتغالی (۳0۲7001882): 050 35 (0898015) :0105
لهستانی (۳0(757): ادن 6 (0882801۲15) +3
روسی (/5540): 17 7 ۸/700
چکه ((280): 07 برهان قاطع : ۱۳۴
صربی (88781۸۸۷): ان
۱
[pdf page 88]
مود
بادداشت: ۳
واژه‌ی فارسی آهست" (پهلوی ۸87 ,۸87۸0 به چم "استخوان" و "هسته‌ی میوه" نیز از همین واجربشه است ۱
58 (۸۹)۸6. 12 (برهان قاطع : ۲۳۳۷).
اوستایی (4ل412874): وال51 ب87۸۷02 آلمانی (088۸44(0): 51811801 ,8781715
اما ان انگلیسی کهن (#لعنا20 صا۵): ,87808
پهلوی (1اتلهه): 3 دا ان
اوستی (0898716): ۸۸ انگلیسی (5ل8(701): داد ان
سانسکریت (54(/852/7): ,8777۸10۸8 دانمارکی (0۸۸7/977): دای وان
5732۷۸۳ سوئدی (5177:0187): ه77
آرمنی (/4/04827/4): 3 اون نروژی (/01050/۵/: ال وان
```


## [2026-09-07T20:28:41.647Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT ast ===\"; grep -n \"^ast\\|\\bast-\\b\\|asti-\" KNT.txt | head -10; echo \"=== TLM ===\"; grep -n \"bone\\|^ast\" TLM.txt | head -10; echo \"=== POK_03 ost leaf ===\"; python3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'ost(h)-' in p and 'Knochen' in p:\n        print('ost leaf',i,'-> printed approx',i+762,'to',i+766)\n    if '2.  ous-' in p:\n        print('ous leaf',i,'-> printed approx',i+762,'to',i+766)\nEOF",
 "description": "Check Kent, Tolman, Pokorny leaves"
}
```


### [2026-09-07T20:28:42.975Z] TOOL RESULT

```
=== KNT ast ===
1138:There are the following examples in OP: pasti- foot-soldier’, from *patsti- from *ped-t-. ustaxand- ‘staircase’, from *uést- from *ud-te-. aruvastam ‘activity’, in form an abstract “arval-
1635:(2-3) pAr. split of pIE s into s š A, and plr. split of pAr. s into s and A (8115): stanam avas- layam niyašiāyam ачоіа; hadiš niy-asddayam; afaham 6asianaty; nom. ending in baga-" pasti- ріти-&.
5644:pad- sb. ‘foot’: Av. Skt. pad-, Gk. roô-, Lt. ped- ($142); in mipadiy, cf. also pada-, páda-, pasti-.
5681:pasti- sb. ‘foot-soldier’: Skt. pailt-, from pIE *ped- ‘foot’ (OP pad-) + suffix -t&- ($85, 5152.11; Wb. Grab 40, Hz. ApI 94-8). — pasti$ nsm. DNb 48, 45.
=== TLM ===
365:astam  abara  vasna  Auramaz-7)daha  Yistaspa  avam  karam  tyarn hami0riyam  ajan  vasiy  Ga-8)rmapadakya  mahya  I   rauca  tfakatam1 aha  avaflasam  hamaranam  ka-9)rtam.
=== POK_03 ost leaf ===
ous leaf 18 -> printed approx 780 to 784
```


## [2026-09-07T20:28:51.568Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'Auster' in p and 'Knochen' in p:\n        print('leaf',i,'-> printed',i+762,'..',i+766)\n        print(p[:400].replace('\\n',' '))\nEOF",
 "description": "Find Pokorny ost leaf"
}
```


### [2026-09-07T20:28:52.803Z] TOOL RESULT

```
leaf 16 -> printed 778 .. 782
*ösi-s',  dazu  illyr.-pannon.  VN  Osi,  ON  Osones);  slav.  *jasenh  {*jasem)  m.  in serb.  jäseUj  russ.  jdsenh] mit  ic-Erweiterung:  arm.  haci  ,Esche*,  alb.  ah  ,Buche*  {*oskä)-  gr. d^vT]  ,Buche,  Speerschaft*  (*aax[e](T-?);  ligur.  ON  'Oax^a  ,Eschenwald*(?); aisl.  askr  m.  ,Esche,  Speer,  Schiff*,  ags.  xsc  (germ.  *askiz\  ahd.  asc  ,Esche*;  ' vgl.  tscherem.  o^ko  ,Es
```


## [2026-09-07T20:28:57.732Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11700,11760p' CHEUNG.txt",
 "description": "Read Cheung *Hauš entry"
}
```


### [2026-09-07T20:28:57.779Z] TOOL RESULT

```
‘to vow solemnly’, Umb. vufru ‘consecrated, vowed’ 
*REFERENCES: EVS: 107b; DKS: 237; Werba 1997: 164 f.; ESIJa I: 260 f. 


*Hauš ‘to burn’ 

*KHOTANESE: (+ *ш-) OKh. byuv’- ‘to burn’ (or with prev. *abi- ?) = SGS: 105 
*NWIR: Zaz. vesäyis/vesen- (intr.), vesnayis/vesnen- (tr.), Tt. (Xia.) vast/vast ‘to 
burn’ 

*NEIR: Oss. I. usong, D. osongz ‘hut, tent, shack’ 

*MISC: Arm. (LW) atrusan ‘fire-temple’ (< WIr. *atar- ‘fire’ + *ausäna- ‘fire-place’), 
Brah. (LW) husing ‘to burn’ (< Bal.) 

*SANSKRIT: os ‘to burn’ (RV+) = EWAia I: 281 

«PIE *H;eus- ‘to burn, scorch’ = LIV: 245 | Pok.: 347 f. 

*IE COGNATES: Gr. £00 ‘I scorch’, Lat. urd ‘I burn, scorch’, (ppp.) Lat. ustus ‘burnt’, 


etc. 
*REFERENCES: Yarshater 1969: 182; DKS: 310a; Abaev, Slovar’ IV: 21 f.; Werba 1997: 338; Paul 1998: 
317a; ESIJa I: 266; Cheung 2002: 234 


*Haxs! ‘to aim, shoot; mark? 

*OLD PERSIAN: ? uvaxstra- PN (lit. ‘with Good Arrow/Target’ ?) <u-v-x-8-t-r-> (DB 
4.19, DB 4.22, DB e.7), <u-v-x-8-t-r-> (DB g.9) 

*NWIR: (+ *apa-) Bal. buxt'a/busk- ‘to let go, go off (shoot)’. © The etymology of 
Geiger 1891: 436, accepted by Korn 2005: 1.с., viz. from *buxs-, *bauj” ‘to release, 
free, open’ needs to be explained further, as there is actually no evidence for an 
enlarged root *buxs- of *bauj” in Iranian. Citing from Shahbakhsh, we apparently 
have two semantically and also formally similar verbs in Balochi: butk/busk- ‘to be 
released (from jail), be fired (a gun), be emptied’ and buskt’, bux6/busk- ‘to 
discharge a gun, be let go, go off (of a gun)’. This seems to point to two different 
origins. The former clearly derives from an inchoative formation *buxsa- of *bauj’, 
whereas the latter may go back to (zero grade) *apa-Hxsa-. Obviously, the two verbs 
show signs of convergence. 


*Haz 171 


*NEIR: Oss. І. æxsyn/æxst, D. &xsun/zxst ‘to aim, shoot at’ || (+ *a-) ? Oss. I. 
axsyn/axst, D. axzessun/axesst ‘to catch; to conquer, occupy; to arrest’ || (+ *fra-) ? 
Oss. I. raxsyn ‘to throw out; to shoot at’ 

*SANSKRIT: aks ‘to mark, to make earmarks, [+ nis] to castrate’ = EWAia I: 41 

© This Пг. root has no certain IE correspondences. = LIV: – | Pok.: 21 


*REFERENCES: Abaev, Slovar’ I: 221 f., 92 f.; Werba 1997: 449; Shahbakhsh: s.v. busk-; Korn 2005: 177, 
312, 356!
```


## [2026-09-07T20:29:10.014Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npages=t.split('\\f')\ndef leaf_of(lineno):\n    off=sum(len(l)+1 for l in lines[:lineno-1]); c=0\n    for i,p in enumerate(pages):\n        c+=len(p)+1\n        if c>off: return i\nfor ln in (4241,5781,5772,8686,7395,8724):\n    i=leaf_of(ln)\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', pages[i])\n    print('line',ln,'leaf',i,'cols on leaf:',nums[:8], '|', lines[ln-1][:60])\nEOF",
 "description": "Find Bartholomae column numbers"
}
```


### [2026-09-07T20:29:12.227Z] TOOL RESULT

```
line 4241 leaf 98 cols on leaf: [] | •  j.  an-aoäa-  Adj.  'dem  kein  Verderben droht,  unsterb
line 5781 leaf 149 cols on leaf: ['314'] | •  j.,  g.  ast-  n.  'Knochen',  von  Menschen und  Tieren:
line 5772 leaf 149 cols on leaf: ['314'] | '<n'a.^/-p>/J/(sd.)V.^5o;  51.  a)  Sing. und  Plur.  'Knoch
line 8686 leaf 254 cols on leaf: [] | •  j.  u§-  n.  'Ohr'  uzw.  «^»rischer  Wesen'': k/(NS.)  F
line 7395 leaf 213 cols on leaf: ['335', '336'] | •  j.  ävistayae-.'ir  Inf,;  s.  unter  wV/iyaJ-Ja. g,,  j.
line 8724 leaf 255 cols on leaf: ['415', '416'] | ■  j.  uäLdaradra-  n.  'Aufthssen  mit  dem Verstand,  Begr
```


## [2026-09-07T20:29:28.726Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT xastu ===\"; grep -n \"خستو\" BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -10; echo \"=== BQT haste ===\"; grep -n \"^هسته\\|هسته -\\|هسته ه\" incoming/BQT/BQT_v5_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -5",
 "description": "Grep Borhan for xastu and haste"
}
```


### [2026-09-07T20:29:28.803Z] TOOL RESULT

```
=== BQT xastu ===
BQT_v1_pages.txt:27680:بهستیش بابد که خستو شوی ز گفتار پیکار _مکسوشوی. فردوسی طوسی.
=== BQT haste ===
incoming/BQT/BQT_v4_pages.txt:3689:۸ - رك: مت . هسته - ‎٩‏ -مفت بکراول » جوی آب :
```


## [2026-09-07T20:29:38.343Z] TOOL CALL #72: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%AE%D8%B3%D8%AA%D9%88/\" \"https://abadis.ir/fatofa/%D9%87%D8%B3%D8%AA%D9%87/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 376: Persian xastu / haste, Mo'in+Dehkhoda entries for node 3\" ; done 2>&1 | tail -4",
 "description": "Fetch abadis entries for xastu and haste"
}
```


### [2026-09-07T20:29:42.653Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fc18b850584bd743.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8cd1f53414fe73d8.txt
```


## [2026-09-07T20:29:47.369Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in fc18b850584bd743 8cd1f53414fe73d8; do echo \"###### $f\"; grep -o \"فرهنگ فارسی معین.\\{0,400\\}\" $f.txt | head -2; echo \"--- dehkhoda:\"; grep -o \"لغت‌نامه دهخدا.\\{0,500\\}\" $f.txt | head -1; done",
 "description": "Extract Mo'in/Dehkhoda entries"
}
```


### [2026-09-07T20:29:48.624Z] TOOL RESULT

```
###### fc18b850584bd743
--- dehkhoda:
###### 8cd1f53414fe73d8
فرهنگ فارسی معین ). اولین بار در سال 1831 م. براون گیاه شناس انگلیسی در یاخته های پوست سطحی گیاهان ، هسته را تشخیص داد و اظهار داشت که تمام یاخته ها باید هسته داشته باشند. هسته معمولاً جسمی است کروی ، ولی اگر یاخته دراز و باریک باشد و یا مواد خارجی در آن پدید آمده باشد، به دیواره یاخته رانده شده به واسطه فشردگی به صورت عدس درمی آید. حجم آن کم و طول و عرضش از یک تا ده و گاه به پنجاه میکرن میرسد. در داخل هسته ، هست
فرهنگ فارسی معین
--- dehkhoda:
```


## [2026-09-07T20:29:54.360Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nfor f in ['fc18b850584bd743','8cd1f53414fe73d8']:\n    t=open(f+'.txt',encoding='utf-8').read()\n    print('######',f, len(t))\n    import re\n    i=t.find('معین')\n    print(t[:300])\n    print('...')\n    # print around first occurrence of the headword definitions\n    for key in ['هسته','خستو']:\n        j=t.find(key, 2000)\n        if j>0:\n            print('KEY',key, t[j-200:j+900].replace('\\n',' '))\n            break\nEOF",
 "description": "Inspect abadis pages"
}
```


### [2026-09-07T20:29:55.694Z] TOOL RESULT

```
###### fc18b850584bd743 5849
URL: https://abadis.ir/fatofa/%D8%AE%D8%B3%D8%AA%D9%88/
FETCHED: 2026-09-07T20:29:40Z
STATUS: 200
TITLE: خستو - معنی در دیکشنری آبادیس

خستو - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 خستو

 مترادف خستو : اعتراف کننده، اقرارکننده، معترف، مقر ، هسته
 متضاد خستو : ناخستو
 معنی انگلیسی : confess
...
KEY هسته نقل دهخدا از تحفةالملوک و بقول او شاید از آفرین نامه ابوشکور باشد. ) در این زمانه بتی نیست از تو نیکو تر نه بر تو بر، شمنی از رهیت خستو تر. ابوسلیک گرگانی.  بیشتر بخوانید ...    فرهنگ فارسی   ( اسم ) هسته ( میوه ) . نام یکی از اکابر چین    فرهنگ معین   (خَ ) (ص . ) مقر، معترف . ج . خستوان .    فرهنگ عمید   کسی که به امری اقرار و اعتراف می کند، مقر، معترف، اقرارکننده.    مترادف ها   kernel (اسم)   هسته، دانه، شالوده، مغز، تخم، هسته اصلی، مغزهسته، خستو  self-confessed (صفت)   خستو   فارسی به عربی   لب    پیشنهاد کاربران   واژه " خستو" معانی مختلف دارد از جمله هسته میوه هایی مانند هلو و خرما. با این معنی خستو از ریشه نیا هند و اروپایی ost بمعنی استخوان مشتق شده است. همانطور که در نمودار زیر نشان داده شده این واژه از مسیر زبان اوستایی و پارسی میانه به فارسی رسیده است.  هسته واستخوان نیز از این ریشه هستند.   کورش جان خسته که امروز بجای مانده میگویند برابر با زخمی شدن است از خستن و پیوندی با ماندگی ندارد و هیچ پیوندی با خستو ندارد خستوه از ستوه شده است و خودستوه شدن را خستوه گویند -   - دوستی که گفتند بسیار به کار نرفته باید بیشتر جستجو کنند برای نمونه در کوشنامه ایرانشان چندین بار امده در
###### 8cd1f53414fe73d8 21591
URL: https://abadis.ir/fatofa/%D9%87%D8%B3%D8%AA%D9%87/
FETCHED: 2026-09-07T20:29:42Z
STATUS: 200
TITLE: هسته - معنی در دیکشنری آبادیس

هسته - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 هسته
 /haste/

 مترادف هسته : بذر، تخم، خستو، دانه، مغز
 معنی انگلیسی : nucleo- , nucleus , pit , (fruit-) st
...
KEY هسته و اجسام بزرگتری به اسم کروموزوم به وجود می آورند که عده آنها در هر گونه ای ثابت است... ( از جانورشناسی عمومی تألیف مصطفی فاطمی ص 14 و 15 ). || وجود و هستی. ( ناظم الاطباء ). رجوع به هست و هستی شود.  هسته. [ هََ ت َ / ت ِ ] ( ص ، ق ) مخفف آهسته :  تو نرم شو چو گشت زمانه درشت  هسته برو ، که سود ندارد سته. ناصرخسرو.   فرهنگ فارسی   دانه میان میوه مثل دانه زرد آلو، خسته، مرکزاتم، درفیزیولوژی هسته جسم کروی شکل است که درون سیتو، پلاسم قراردارد (اسم ) ۱- مجموع. دانه ودرون برخی گیاهان که درداخل میوه قراردارد. باین معنی که دان. علاوه برپوشش خود دانه ازخارج بوسیل. درون برچوبی شد. میوه فراگرفته شده است بعبارت دیگر هسته نیز عبارت ازدانهایاست که بوسیل. درون برچوبی شده پوشیدهشدهاست هسته معمولا درداخل میوه های شفت قراردارد مانند هست. گوجه و آلبالو وهلو جز آن .۲- جسم شفاف وهموژنی ک درداخل سیتوپلاسم سلولهای زنده قراردارد وقابلیت انکسارنور در آن از سیتوپلاسم بیشتراست ودرداخل آن یک یاچند دان. کوچک باسم هستکمشاهدهمیشود دردوره زندگی سلول هسته ممکنست بدوصورت مختلف مشاهده شودیادرحال آرامش باشد ویامختلف تقسیم باشد مخفف آهسته    فرهنگ معین   (هَ تِ ) (اِ. ) ۱ - دانة سفتِ داخل میوه ها. ۲ - نقطه ، گروه یا تود
```


## [2026-09-07T20:30:12.479Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"anosag\\|anosagruwan\\|ruwan\\b\" PHD_mackenzie.txt | head -8; echo \"=== SKT ===\"; grep -n \"^oyster\\|oyster,\\|ossify\\|osseous\" SKT.txt | head -8",
 "description": "Grep PHD anosag and Skeat"
}
```


### [2026-09-07T20:30:12.546Z] TOOL RESULT

```
1023:  e.g. an i ahlawiin ruwan = ruwiin i ahlawan, the souls of the
1122: ---ruwan [-lwb)n l ] the late, deceased.
6333: cure besb(en)-.                           deceased anosagruwiin; v. blessed.
6969:late (deceased) anosagruwan, hufra-       Libra Tariiziig.
7639:     ruwan, uStan.                      spring, v. source.
9394:amaI                            tG~       ruwan
11979:ogardan                  ,,~.s~        anosagih                   ~   joIO,,,,,
11981:xog,xug                     \ -' \""   anosag, hunusak              \¥U\"",
=== SKT ===
12977:ostraoiso,  to  banish  hy  a  vote  written on  a  potsherd.  (Gk.)  Gk.  barptuu^tiv,  to ostracise,  —  Gk.  S^rpaKor,  a  potaherd,  tile, voting- tablet,  orig.  0  ahell.wGk.  JaTpMr, an  oyster,  orig.  a  shelL
```


## [2026-09-07T20:30:24.065Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ossis\" LAT.txt LEW_1910.txt | head -8",
 "description": "Grep Latin dictionaries for os ossis"
}
```


### [2026-09-07T20:30:24.125Z] TOOL RESULT

```
LAT.txt:4072:et os, ossis, asser,
LAT.txt:4795:fossis, montibus, arboribus ante missis, aquarum diuergiis, et si qua
LAT.txt:14185:P.F.36,11. La glose de Festus r6unit un substaatif cossus,-i (cossis
LAT.txt:37424:facere id possis, nostram nunc accipe nentem), par suite "1’intention".
LAT.txt:40960:tu possis. Ce n'est pas une negation "subordonnante"; mais comme le
LAT.txt:44178:os ( oss , puis Bs), ossis n. (doublet dssum, cf.Charis., GLK I 139,3,
LAT.txt:44188:oortoXoyiov; exBs (6 Lucr. 3,73:1.), -ossis (cf. ops), d'oh exossB,-Bs;
LAT.txt:44198:~ 5 s~ de rst- dans 1 at. os (oss), ossis ne se ret.rouverait nulle part
```


## [2026-09-07T20:30:28.157Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '44178,44210p' LAT.txt",
 "description": "Read Ernout-Meillet os entry"
}
```


### [2026-09-07T20:30:28.204Z] TOOL RESULT

```
os ( oss , puis Bs), ossis n. (doublet dssum, cf.Charis., GLK I 139,3,
conservd dans les 1 . ronanes, cf.M.L.6114; et ossu, usitd surtout au
pl» ossua, cf»Charis, ibid. 139,4) : os. — Attestd de tout tenps; pan—
ronan.
D 4 riv 4 s et conposds: i° de *ossosseus-, ossiculum dininutif, tech-
nique ou populaire avec valeur affective, et ses d 4 riv 4 s ossiculStim
(Caec.), ossiculBris (V 4 g.); ossGsus-, ossifragus dont ddrive le non
de "l f orfraie", H.L.6113 (avec un a?); QssipBgina "ddesse qui raf~
fernit les os dea enfants" (Ara.3,30); ossilSgo "tunepr dure (sen-
blable A tm os) ", ossilegus, ossilegium traductione de OCTroXoyoc,
oortoXoyiov; exBs (6 Lucr. 3,73:1.), -ossis (cf. ops), d'oh exossB,-Bs;
3 de ossu —: ossuSrius {—a Sila) et le n» ossuBrium "ossuaire"; os—
suBsus-, os suculum autre forne de ossiculum (cf. geni- et genuculum).
• L'iranien offre la forne du non de l'"os", sans aucun 4largisseaeat:
av. astpm (g 4 n. pl. )j azdiblS, azdebis (c.-A-d. azdb fi instr.pl.), «t
le sanskrit la n$me forne avec un 4 largissenent i/n: dsthi (non.acc.
sg.), asthndh (g 4 n. abi. sg.). Le grec a un d 4 riv 4 th 4 natique odreov;
hitt. ha$t—ai. Le not affecte en-partie des formes populaires ain~
si qu*il ressort du t,h de skr. dsthi et du k— pr 4 fixe dans v.sl. kosti
(pass 4 au f 4 ninin -sous i'influence du non.plur. kosti). TJn traitenent
~ 5 s~ de rst- dans 1 at. os (oss), ossis ne se ret.rouverait nulle part
ailleuTs; il ne reste donc d'autre hypothbse que de partir d’un ancien
oss— et d'adnettre que —t— ou —th— ne sont pas des 4 l 4 nents essentiels
du non de 1 '"os", v. MSL 33, p. 3 S 9 , ot Benveniste, formation des noms
en u-e .,6 et 77. Si arn. oskr "os" repose, conne il senble, sur *ostwer,
l'i* de 1 at. ossua pourrait ^tre anci en. La gutturale de gall. asgwrn
"os" ne se concilie pas avec le h de l'arn 4 nien» Plusieurs langues
ont des nons iaol 4 s, ainsi le gernanique: v.isl. bein, etc., et le
balti^ue: lit. kdulas, v.pr. kaulan (neutre), etc.
oscen, -lnls n.: t. de la langue augurale, s^appliquant aux oi-
seaux dont le chant est proph 4 tique. De *obs-cen "qui chaate en avant",
cf. pour le prenier terne os-tendB , et pour le second tubi-cen, etc.
L’explication de Festus: oscines aues auspicium ore facientes, P.F.
```


## [2026-09-07T20:30:56.215Z] TOOL CALL #78: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83%C3%A9sth%E2%82%81\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B4%DA%A9%D8%A7%D8%B1%D8%A7\" \\\n \"https://www.etymonline.com/word/oyster\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%E1%B9%93ws\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 376: PIE bone root, askara etymology, oyster, PIE ear root\" ; done 2>&1 | tail -5",
 "description": "Fetch more sources"
}
```


### [2026-09-07T20:30:59.005Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/070748714fb927f2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dd95e240ed4a6ec8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0ce78063f8f2671.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/728aa27d27c33db0.txt
```


## [2026-09-07T20:31:04.858Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nfor f,l in [('070748714fb927f2','PIE h3esth1'),('dd95e240ed4a6ec8','ashkara'),('e0ce78063f8f2671','oyster'),('728aa27d27c33db0','PIE h2ows')]:\n    t=open(f+'.txt',encoding='utf-8').read()\n    print('##########',l,'|', t.split('\\n')[2][:40])\n    if 'FETCH FAILED' in t[:400]: print('FAILED'); continue\n    i=t.find('From Wiktionary, the free dictionary')\n    if i<0: i=0\n    print(t[i:i+1800])\n    print()\nEOF",
 "description": "Read new sources"
}
```


### [2026-09-07T20:31:06.196Z] TOOL RESULT

```
########## PIE h3esth1 | STATUS: 200
From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Alternative reconstructions
 [ edit ] 

 *h₂óst [ 1 ] [ 2 ] 

 Reconstruction
 [ edit ] 

 The original form was a neuter root noun, as can be seen from Latin os and Avestan 𐬀𐬯𐬙- ( ast- ) . In the rest of the daughters, the noun has been transferred to various vocalic stems.

 Medial -th- in Sanskrit अस्थि ( ásthi ) requires root of the form *HestH (the initial laryngeal is there to account for the canonical shape of Proto-Indo-European root). The Latin reflex requires the initial laryngeal to be *h₃- , and Ancient Greek ὀστέον ( ostéon ) points to *h₁ as the root-final laryngeal.

 Celtic forms require initial laryngeal to be *h₂- , so this noun is sometimes [ 3 ] reconstructed to have the paradigm *h₂óst(h₁) ~ *h₂ést(h₁)s .

 Noun
 [ edit ] 

 *h₃ésth₁   n 

 bone 

 Declension
 [ edit ] 

 Acrostatic ablauting paradigm.

 Athematic, acrostatic

 singular

 nominative

 *h₃ésth₁ 

 genitive

 *h₃ésth₁s 

 singular

 dual

 plural

 nominative

 *h₃ésth₁ 

 *h₃ésth₁ih₁ 

 *h₃ésth₁h₂ 

 vocative

 *h₃ésth₁ 

 *h₃ésth₁ih₁ 

 *h₃ésth₁h₂ 

 accusative

 *h₃ésth₁ 

 *h₃ésth₁ih₁ 

 *h₃ésth₁h₂ 

 genitive

 *h₃ésth₁s 

 *? 

 *h₃ésth₁oHom 

 ablative

 *h₃ésth₁s 

 *? 

 *h₃ésth₁mos , *h₃ésth₁bʰos 

 dative

 *h₃ésth₁ey 

 *? 

 *h₃ésth₁mos , *h₃ésth₁bʰos 

 locative

 *h₃ésth₁ , *h₃ésth₁i 

 *? 

 *h₃ésth₁su 

 instrumental

 *h₃ésth₁h₁ 

 *? 

 *h₃ésth₁mis , *h₃ésth₁bʰis 

 Derived terms
 [ edit ] 

 *h₃ósth₁-i 
 *h₃ósth₁-ey-om 
 Proto-Hellenic: *ósteyon ( alternatively, *óstewon like the Armenian u-de

########## ashkara | STATUS: 200
From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 آشکار ( āškār  / âškâr, āšikār  / âšekâr ) , آشکاره ( āškāra  / âškâre, āšikāra  / âšekâre ) 

 Etymology
 [ edit ] 

 Inherited from Middle Persian [script needed] ( ʾškʾl(ʾ)k' /⁠āškārāg⁠/ , “ obvious, evident ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔaːʃ.kaː.ˈraː/ , /ʔaː.ʃi.kaː.ˈraː/ 

 ( Dari, formal ) IPA ( key ) : [ʔɑːʃ.kʰɑː.ɾɑ́ː] , [ʔɑː.ʃɪ.kʰɑː.ɾɑ́ː] 

 ( Dari, formal ) IPA ( key ) : [ʔɑːʃ.kʰɑː.ɾɑ́ː] , [ʔɑː.ʃɪ.kʰɑː.ɾɑ́ː] 
 ( Kabuli ) IPA ( key ) : [ʔɑːʃ.kʰɑː.ɾɑ́ː] , [ʔɑː.ʃɪ.kʰɑː.ɾɑ́ː] 

 ( Hazaragi ) IPA ( key ) : [ʔɔːʃ.kʰɔː.ɾɔ́ː] , [ʔɔː.ʃi.kʰɔː.ɾɔ́ː] 

 ( Iran, formal ) IPA ( key ) : [ʔɒːʃ.kʰɒː.ɹɒ́ː] , [ʔɒː.ʃe.kʰɒː.ɹɒ́ː] 

 ( Tajik, formal ) IPA ( key ) : [ʔɔʃ.kʰɔ.ɾɔ́] , [ʔɔ.ʃi.kʰɔ.ɾɔ́] 

 Rhymes: -aː 

 Readings

 Classical reading ? 

 āškārā, āšikārā

 Dari reading ? 

 āškārā, āšikārā

 Iranian reading ? 

 âškârâ, âšekârâ

 Tajik reading ? 

 oškoro, ošikoro

 Adjective
 [ edit ] 

 آشکارا • ( āškārā, āšikārā / âškârâ, âšekârâ ) ( Tajik spelling ошкоро , or ошикоро ) 

 evident , obvious , manifest 

 open , public 

 frank 

 Adverb
 [ edit ] 

 آشکارا • ( āškārā  / âškârâ or āšikārā  / âšekârâ ) ( Tajik spelling ошкоро or ошикоро ) 

 openly , frankly 

 Derived terms
 [ edit ] 

 آشکاری ( āškārī  / âškâri ) 

 آشکار کردن ( āškār kardan  / âškâr kardan ) 

 Descendants
 [ edit ] 

 → Azerbaijani: aşkar , aşkara 

 → Chagatai: آشکار ( ʾʾškʾr /⁠āškār⁠/ ) , آشکارا ( ʾʾškʾrʾ /⁠āškārā⁠/ ) , آشکاره ( ʾʾškʾrh /⁠āškārä⁠/ ) 
 Uyghur: ئاشكارە ( ashkare ) , ئاشكارا ( ashkara ) 

 Uzbek: oshkor , oshkora 

 → Gawar-Bati: اخکارہ 

 → Georgian: აშკარა ( ašḳara ) 

 → Gulf Arabic: اشكرة ( aškara ) 

 → Hebrew: אשכרה 

 → Old Armenian: աշկարայ ( aškara

########## oyster | STATUS: 200
URL: https://www.etymonline.com/word/oyster
FETCHED: 2026-09-07T20:30:58Z
STATUS: 200
TITLE: Oyster - Etymology, Origin & Meaning

Oyster - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of oyster 

 oyster (n.) 

 "edible bivalve mollusk of the family Ostreidæ ," late 13c., oistre , from Old French oistre , uistre (Modern French huître ) and directly from Latin ostrea , plural or fem. of ostreum "oyster," from Greek ostreon , from PIE root *ost- "bone." It is thus related to Greek ostrakon "a hard shell" and to osteon "a bone." The h- in the modern French word is a regular development; compare huile "oil" (Latin oleum ), huit "eight" (Latin octo ).

 Why then the world's mine Oyster, which I, with sword will open. [Shakespeare, "The Merry Wives of Windsor," II.ii.2]

 Oyster-bed "place where oysters breed or are bred" is from c. 1600; oyster-knife , used for opening oysters, is recorded from 1690s. Oysterman "man engaged in rearing, taking, or selling oysters" is attested from 1550s. The common statement that edible oysters are in season only in months that end in -r is recorded by 1765.
 also from late 13c. 

 Entries linking to oyster 

 prairie-oyster (n.) 

 "salted and peppered raw egg, drunk in booze or vinegar," by 1878, American English, from prairie + oyster (in reference to the taste or the method of consuming it). Also called prairie-cocktail (1889). Prairie-oyster as "fried calf testicle," considered a delicacy, is by 1941.

 PRAIRIE OYSTER. This simple but very nutritious drink may be taken by any person of the most delicate digestion, and has become one of the most popu

########## PIE h2ows | STATUS: 200
From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 From *h₂ew- ( “ to see ” ) +‎ *-s ( root nominal suffix ) , with a semantic shift to "to hear" after the split of the Anatolian branch.

 Reconstruction
 [ edit ] 

 The initial laryngeal must be *h₂ to account for Latin forms auris , aus-cultō , which must reflect e-grade *h₂ews-.

 Noun
 [ edit ] 

 *h₂ṓws ( oblique stem *h₂éws- ) 

 ear 

 Inflection
 [ edit ] 

 Athematic, acrostatic

 singular

 collective

 nominative

 *h₂ṓws 

 *h₂éwsōs 

 genitive

 *h₂éwsos 

 *h₂usés 

 singular

 dual

 plural

 collective

 nominative

 *h₂ṓws 

 *h₂ṓwsih₁ 

 —

 *h₂éwsōs 

 vocative

 *h₂ṓws 

 *h₂ṓwsih₁ 

 —

 *h₂éwsōs 

 accusative

 *h₂ṓws 

 *h₂ṓwsih₁ 

 —

 *h₂éwsōs 

 genitive

 *h₂éwsos 

 *? 

 —

 *h₂usés 

 ablative

 *h₂éwsos 

 *? 

 —

 *h₂usés 

 dative

 *h₂éwsey 

 *? 

 —

 *h₂uséy 

 locative

 *h₂éws , *h₂éwsi 

 *? 

 —

 *h₂éws , *h₂éwsi 

 instrumental

 *h₂éwsh₁ 

 *? 

 —

 *h₂uséh₁ 

 Notes 

 Acrostatic singular, amphikinetic plural

 Nominative: *h₂óws-s > *h₂ṓws

 Genitive: *h₂éws-s > *h₂ḗws, or *h₂usós

 Dual: *h₂(e)usih₁

 Collective plural: *h₂éw(s)ōs, genitive *h₂u(s)-s-és

 Derived terms
 [ edit ] 

 *h₂ḱh₂owsyéti 

 Unsorted formations 

 Sanskrit: उषस् ( uṣás , “ the outer passage of the ear ” ) 

 Proto-Indo-Iranian: *Húšma 
 Proto-Nuristani: 
 Northern Nuristani:
 Prasuni: yǘmu 

 Descendants
 [ edit ] 

 Proto-Albanian: *ōusi 
 Albanian: vesh 

 Proto-Armenian: 
 Old Armenian: ունկն ( unkn ) ( singulative ) , ականջք ( akanǰkʻ ) ( plural ) (
```


## [2026-09-07T20:31:24.403Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ost(h)\\|ost(b)\\|osteon\\|dazeov\" incoming/WLD/WLD_Bd1_pages.txt | head -6; echo \"=== Bd2/3 ===\"; grep -n \"ost(h)\" WLD_band3.txt incoming/WLD/WLD_Bd2_pages.txt | head -6; echo \"=== IEC ost ===\"; grep -n \"^ost\\|osti-\\|ostei\" IEC.txt | head -6",
 "description": "Grep Walde-Pokorny and Mann for ost-"
}
```


### [2026-09-07T20:31:24.483Z] TOOL RESULT

```
16943:                              ozgho-   — ost(h)-; ost(h)i, ost(h)r(g), ost(h)-(e)n-                     185
17012:ost(h)-        ;
17051:(ass.                      Schmidt aaO.; setzt einen nom. *ost(h)rg voraus).
17107:von ost(h)- zu lat. costa „Rippe“, abg. kosh „Knochen“ (Meringer aaO. 42,
43990:LEWb. 2 s. v., Berneker 582               f.,   und gegen Yerknupfung mit *ost(h)- „Knochen“
=== Bd2/3 ===
=== IEC ost ===
3840:ost-, see osth-
3841:oster- (osteren-, ster-) ‘star’. WP II, 635. (A Semitic LW according to E. Schrader. Cf. Akkad. istar, Can. Syr. Astarte, AStoroth, a goddess of fertility. Cf. also Basque izar ‘star and Kabyle ithri, id.) Skt. cf. str-bhih ‘by the stars; Romani Cheren ‘star’; Av. stare, acc. stárom beside axtaro, id., Per. sitare, axtar; Tokh. eren, B on, sCirin, beside cCirye; Hitt. asteras, sittar; Gk. astér, gs. asté- ros beside ástron; (LW in Lat. astrum); Lat.
3845:ostrk- (ostrk-, osthrk-) ‘potsherd’. Cf. osth-, (ost^-, o?st-) Skt. istaka ‘brick’; Av. istya ‘brick, tile’; Oss.
9539:leghn-, leghen- ‘lie, repository’. Cf. légh- and following entries Lat. cf. anti-lena, posti-lena *front- and rear- pieces on horse's equipment; W lleyn, pl. -oedd, m. *lowlying strip of land’; MHG lége, f. ‘settlement’; R léZení, f. “sleeper, wallplate' beside Cz. (*-&-) líheň, f. ‘lair; focus; cradle’
10162:luk- “light, shine’. Cf. luk- and cpds., leuk-, louk- (louk-), etc. Skt. luč & lúčih, f. id.; Arm. cf. h-ykem, v. (‘polish’, fr. *en-luk-); Gk. cf. lukó-phos; W llwg, pl. liygon, m. ‘gleam, blotch’; adj. ‘livid’ beside llygas, f. (‘splendour’, fr. *lukosti-); go-Iwg, m. ('sight, view’, fr. *upo-Iuk-); MHG lo, lohe, wm & f ‘flame, glare’. (Oxytonic pro- totypes in OFris. loga, wm “flame? and ON loga, f. *candle^). WP II, 408
11804:noid- ‘hate’. Cf. ne-, n-, uoid- (?). WP II, 322 Skt. cf. à-nedyah ‘blameless’; Go. ga-naitjan, v. ‘denigrate’; MHG neis, s. ‘torture’; neisen, v. id.; OE nætan, v. “hurt, harm'; ON neita, v. “deny, refuse'; Latv. naids, m. “hate, hosti- lty’; cf. (z-gde) nidu, inf. nist, v. ‘hate’. (For Gk. ón-eidos, n. “shame, blame”, cf. uon- “lack? and ueidos 'face")
```


## [2026-09-07T20:31:29.302Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17008,17030p;17100,17112p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== IEC osth- ===\"; grep -n \"osth-\" IEC.txt | head -4",
 "description": "Read Walde-Pokorny ost- entry"
}
```


### [2026-09-07T20:31:29.367Z] TOOL RESULT

```
„Knoten“, cymr. oddf „Anwuchs, Ivnoten“ idoch s. u. i>d(e)go- „Stengel“)
gehoren sollen. bestreitet Seheftelowitz (Lit.) mit Iiecht.


ost(h)-        ;
                                  Kasus obi. ost/h)-(e)n- „Knochen“.
                   ost(h;i, ostt.h;r(g),
   Ai.    asflii   gen. asth-n-ah „Bein, Knochen", av. ast-, asti- n. „Knochen‘\
                        n.,

pali ntth 'dnco „Krebs“ (* asthi-lvnms ,knochenhiiutig“, Schulze KZ. 43. 380. vgl.
zur Bed. gr. bmay.bg ,.Meerkrebs“) gr. bar tor ,.Knochen“ (w ohl *ooreyov ..^bei-
                                                        ;
                                                                                r



nernes = lat. ossevm. Bgm. II 2
          :i
                                     157; fur Sommers Hdb - 405 *boTf f-ov kann
                                                1   .


 was aber *ooy.vg oder *6oyyg ergeben hatte; ebenso unmoglich Johansson
BB. IS, 23 f.), besteht auch seitens der Bed. nicht der mindeste AnlaB;
s.    u.        od(e)go- „Stengel“.
     Ygl. Curtius 209, und                    zur Stammbildung und Flexion   Saussure   Mem.
226, Mahlow AEO. 80, Bartholomae Ar. Fo. II 122,   BB. 15, 38, J. Schmidt
PI. 109, 266, Pedersen KZ. 32, 355, Johansson Beitr. Sff., BB. 18, 23, IF.
2, 17, Meringer SB Ak Wien 125, II 10. Osthoff BB. 24. 157f.    Beziehung        —
von ost(h)- zu lat. costa „Rippe“, abg. kosh „Knochen“ (Meringer aaO. 42,
Persson Beitr. 526 unter der unbewiesenen Annahme eines ^-Praefixes,
s. auch Berneker 583:     Hirt Abl. 137 unter (o)qosth - oq(o)sth-') iiberzeugt
                                                                         :


=== IEC osth- ===
3840:ost-, see osth-
3845:ostrk- (ostrk-, osthrk-) ‘potsherd’. Cf. osth-, (ost^-, o?st-) Skt. istaka ‘brick’; Av. istya ‘brick, tile’; Oss.
12367:osku, iu (?) Variant of type osth-, osthrk-, q. V.
12375:osth- (osthn-, o'st-) ‘bone’. WP I, 185. Cf. ostrk-, osku Skt. ásthi, asthán, n., Av. astis, pl. asta, m. id. beside ascus, m. ‘shin’; Oss. (dim. type) ástág, stág, id.; Hitt. hastai (for "hast id.; Gk. ostéon, n. “bone, kernel, rib”; ostón, n. “shell, jar; Alb. asht, pl: eshtna, m. ‘bone’; Lat. os (f for *osts), gs: ossis, n. id.; Venetic, cf. (alleged) ostiiakon *ossuary'; MIr. cf. (Gast asna, Ir. asna & easna, f. ‘rib’; Gael. aisean, id.; W asen, pl. ais, id.; R cf. óstov, m. (1) ‘skeleton’; Li. cf. kab-ákStai, mpl. id. (kabus ‘loosely held"). Extns. in Skt. asthila ‘pebble; anvil and in Alb. eshtnoj, v. ‘ossify
```


## [2026-09-07T20:32:31.701Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"au-[0-9]*\\. To perceive[^[]*\\[[^]]*\\]\" AHD_watkins1985.txt | head -3; echo ---; grep -o \"aw-\\?is[^ ]*\\|awis-[^ ]*\" AHD_watkins1985.txt | head -5",
 "description": "Grep AHD for au- perceive"
}
```


### [2026-09-07T20:32:31.761Z] TOOL RESULT

```
---
awis-dh-,
awisdh-yo-
```


## [2026-09-07T20:32:35.548Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \".\\{700\\}awis-dh-.\\{300\\}\" AHD_watkins1985.txt | head -1",
 "description": "Read AHD au- perceive context"
}
```


### [2026-09-07T20:32:38.054Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:32:41.493Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('awis-dh-')\nprint(t[i-900:i+500])\nEOF",
 "description": "Read AHD context around awis-dh-"
}
```


### [2026-09-07T20:32:42.815Z] TOOL RESULT

```
ein, to foster. 1. Germanic *athal- in Old English ztheling, prince: ATHELING. 2, Variant Germanic *6thel- in Old High German edili, noble: EDELWEIss. [In Pok. atos 71.]]
atto-. Father (nursery word). Possibly Latin atta, father: ATAVISM. [In Pok. atos 71.]
au-', To stay the night, dwell. Suffixed form *au-/d- in Greek aulé, court, dwelling: autic. [Pok. 2. au- 72.]
au-?. Pronominal base appearing in particles and adverbs. Suffixed form *au-ge in Germanic ‘*auke in Old English éac, éc, also: EKE?. [Pok. 4. au- 73.]
au-3, Off, away. 1. Old Russian u-, away, in Russian ukazat’, to order: UKASE. 2. Sanskrit ava, off, down: AvaTAR. [Pok. 3. au- 72.]
au-‘4, To weave. Extended form *wedh- (< *awedh-). 1. Germanic *wédiz in Old English wed, wéde, garment, cloth: WEED?, 2. Germanic *wadlaz in Old English watel, watul, wattle: WATTLE. [Pok. 5. au- 75.]
au-5, To perceive. Compound forms *aw-dh-, *awis-dh-, “to place perception” (see dhé-'). 1. Suffixed form *awisdh-yo- or *awdh-yo- in Latin audire, to hear: AUDIBLE, AUDIENCE, AUDIENT, AUDILE, AUDING, AUDIO-, AUDIT, AUDITOR, AUDITORIUM, AUDITORY, OYEZ; OBEY, SUBAUDITION. 2. Greek aisthanesthai, to feel: AES- THETIC; ANESTHESIA. [Pok. 8. au- 78.]
aug-'. To increase. Variant *(a)weg- (< *aweg-). 1. Ger- manic *aukan in: a. Old English éacan, écan, to increase: EKE!; b. Old English éaca, an addition: NICKNAME. 2. Variant extended forms *wogs
```


## [2026-09-07T20:32:47.889Z] AGENT

Now I have enough material. Let me write the verification file.


## [2026-09-07T20:45:15.811Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-376.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = {\n 'ostoxan':'https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%AA%D8%AE%D9%88%D8%A7%D9%86',\n 'pie_bone':'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83%C3%A9sth%E2%82%81',\n 'pie_ear':'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%E1%B9%93ws',\n 'askara':'https://en.wiktionary.org/wiki/%D8%A2%D8%B4%DA%A9%D8%A7%D8%B1%D8%A7',\n 'askar':'https://en.wiktionary.org/wiki/%D8%A2%D8%B4%DA%A9%D8%A7%D8%B1',\n 'hush':'https://en.wiktionary.org/wiki/%D9%87%D9%88%D8%B4',\n 'nush':'https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B4',\n 'anushe':'https://en.wiktionary.org/wiki/%D8%A7%D9%86%D9%88%D8%B4%D9%87',\n 'xastu':'https://abadis.ir/fatofa/%D8%AE%D8%B3%D8%AA%D9%88/',\n 'haste':'https://abadis.ir/fatofa/%D9%87%D8%B3%D8%AA%D9%87/',\n 'oyster':'https://www.etymonline.com/word/oyster',\n}\n\ne0_nodes = [\n dict(id=1, lang=\"Avestan\", words=\"ast, ascu; asča\",\n  verdict=\"plausible\",\n  derivation=(\"Av. ast- n. 'bone' is the unextended root noun of PIE *h₃ésth₁ (Bartholomae, AiW col. 313 'ast- n. ‘Knochen’, von Menschen und Tieren', gen. pl. astam, instr. pl. azdbīš; beside it the i-stem asti- and the n. 'astay-). Buck 4.16 and Pokorny 783 both list exactly 'av. ast-, asti- n. ‘Knochen’', so root→Avestan is uncontroversial. The other two forms are one and the same word doubled: Bartholomae has j. asčav- m. 'Untersch\"\n   \"enkel, Wade' (nom. asču, V. 8.63-65), i.e. 'shin, calf' — Klein (s.v. os 'bone', Nourai's KLN:1099) cites it as 'Avestic ascu-, ‘shinbone’' and Mann (IEC s.v. osth-) as 'ascus m. ‘shin’', both under the same *ost- noun. So Nourai's 'ascu' and 'asča' are the same lexeme (asču / stem asčav-); his gloss split ('ascu: bone' vs 'asča: shin bone') is inexact, and the shape 'asča' is not an attested Avestan nominative. Bartholomae himself compares Gk. ἰσχίον rather than ast-, so the membership of asču- in this root is accepted by Klein/Mann but not universal.\"),\n  derivation_fa=(\"اوستایی ast- (خنثی) «استخوان» همان نام‌ریشهٔ هندواروپایی آغازین *h₃ésth₁ است که در ایرانی باستان بی‌هیچ گسترشی مانده است؛ \"\n   \"بارتولومه (فرهنگ ایرانی باستان، ستون ۳۱۳) همین را «ast- خنثی، استخوان آدمیان و جانوران» می‌آورد و پوکورنی در ص ۷۸۳ و باک در بند ۴.۱۶ نیز. \"\n   \"اما دو صورت دیگر در واقع یک واژه‌اند: اوستایی asčav- (نام فاعلی asču) «ساق، ماهیچهٔ ساق»؛ کلاین و من آن را زیر همین ریشه می‌آورند، ولی بارتولومه آن را با یونانی iskhíon مقایسه می‌کند. \"\n   \"پس ادعای نورایی دربارهٔ ast درست است، ولی جداکردن ascu و asča به دو واژه و جابه‌جایی معنای آن‌ها با احتیاط پذیرفتنی است.\"),\n  sources=[W['pie_bone']],\n  ref_check=[\n    dict(ref=\"SYN:207\", status=\"supports\", note=\"Buck, Selected Synonyms 4.16 BONE, printed p.207 (SYN.txt leaf 242-243): '1. IE *ost-, etc. ... Skt. asthi-, gen. asthnas, Av. ast-, asti-' — the root and the Avestan form, but no ascu/asča.\"),\n    dict(ref=\"POK:783\", status=\"supports\", note=\"POK_03.txt leaf 16-17 (= printed 782-783): 'ost(h)-, ost(h)i, ost(h)r(g), obl. ost(h)-(e)n- ‘Knochen’ ... av. ast-, asti- n. ‘Knochen’, Gen. Pl. astam, Instr. Pl. azdbis'.\"),\n    dict(ref=\"KLN:1099\", status=\"supports\", note=\"Klein s.v. 'os, n., a bone': 'L. os, gen. ossis, ‘bone’, cogn. with OI. asthi, Hitt. hashtai-, Gk. osteon ... Avestic ascu-, ‘shinbone’' — this is where Nourai's 'ascu' comes from (KLN_1971.txt line 169373; 1966 ed. p.1099).\")],\n  consulted=[\n    dict(src=\"BRT\", where=\"col. 313 s.v. ast-; col. ~299 s.v. asčav-\", stance=\"partial\", note=\"'j., g. ast- n. ‘Knochen’, von Menschen und Tieren'; and separately 'j. asčav- m. ‘Unterschenkel, Wade’ ... Vgl. gr. ἰσχ...' — Bartholomae does not put asčav- under ast-.\"),\n    dict(src=\"IEC\", where=\"s.v. osth- (IEC.txt line 12375)\", stance=\"supports\", note=\"Mann: 'osth- (osthn-, o’st-) ‘bone’. WP I, 185 ... Av. astiš, pl. asta, m. id. beside ascus, m. ‘shin’' — asču- is put under the bone root, as in Nourai.\"),\n    dict(src=\"WLD\", where=\"Bd. I 185\", stance=\"supports\", note=\"Walde-Pokorny I 185 s.v. ost(h)-: 'Ai. asthi ... av. ast-, asti- n. ‘Knochen’' (WLD_Bd1_pages.txt line 17012).\"),\n    dict(src=\"LAT\", where=\"Ernout-Meillet s.v. os, ossis\", stance=\"supports\", note=\"'L'iranien offre la forme du nom de l’“os”, sans aucun élargissement: av. astǝm (gén. pl.), azdibis' (LAT.txt line 44178 ff.).\")],\n ),\n dict(id=2, lang=\"Pahlavi\", words=\"astag, astak; astuxan\",\n  verdict=\"confirmed\",\n  derivation=(\"Av. ast- → MP ast (Book Pahlavi 'st', Nyberg: 'ast ‘the bones’ ... Av. ast-'), with the common MP -ag/-ak diminutive/singulative suffix astag '(single) bone; fruit stone' (MacKenzie reads the word with prothetic h-: 'hast(ag) [’st(k)] bone; (fruit) stone', Manichaean 'st(g)). Beside it stands the compound astuxwan (Book Pahlavi ’sthw’n'), from Proto-Iranian *HástH-áhuanām, i.e. ast- plus the -uxwan/-āhuan element; Mo'in's footnote to Borhan s.v. استخوان states that 'both ast and astuxvān exist in Pahlavi and Persian' and lists the Iranian dialect forms. Nourai's 'astuxan' is the ordinary transliteration of ’sthw’n minus the labial glide.\"),\n  derivation_fa=(\"در فارسی میانه (پهلوی) ast «استخوان» دنبالهٔ مستقیم ast- اوستایی است و با پسوند -ag/-ak به astag/astak «یک استخوان؛ هستهٔ میوه» بدل شده است. \"\n   \"مکنزی همین را با هٔ افزوده hast(ag) می‌خواند و معنای «استخوان؛ هستهٔ میوه» می‌دهد و نیبرگ نیز ast را ثبت کرده است. \"\n   \"صورت مرکب astuxwān (در خط پهلوی ’sthw’n) از ایرانی باستان *HástH-áhuanām می‌آید؛ معین در حاشیهٔ برهان قاطع می‌نویسد که «در پهلوی و پارسی ast با astuxvān هر دو وجود دارند». ادعای نورایی درست است.\"),\n  sources=[W['ostoxan']],\n  ref_check=[\n    dict(ref=\"BQT:124\", status=\"supports\", note=\"Borhan-e Qate' (Mo'in ed.), the استه/استخوان pages (BQT_v1_pages.txt leaves 338-341 ≈ printed 120-124): s.v. استه 'دانهٔ خرما و شفتالو و زردآلو ... و استخوان آدمی و حیوانات دیگر را نیز گفته‌اند', with Mo'in's footnote at استخوان: 'استخوان astuxvān پهلوی ... سغدی ... هم در پهلوی و پارسی ast با astuxvān هردو وجود دارند'.\"),\n    dict(ref=\"HRN:20\", status=\"supports\", note=\"Horn, Grundriss p.20 no.81: 'est ‘Knochen’, este ‘Knochen, Kern’ ... xestu ... aw. ast- ‘Knochen’; phlv. ast ‘Knochen’, astak ‘Kern’; ai. asthán-, ásthi-' — exactly Nourai's astag/astak.\")],\n  consulted=[\n    dict(src=\"PHD\", where=\"MacKenzie p.42 s.v. hast(ag)\", stance=\"supports\", note=\"'hast(ag) [’st(k)] | M ’st(g), N hasta] bone; (fruit) stone' (PHD_mackenzie.txt line 1239) — same word, read with h-.\"),\n    dict(src=\"NYB\", where=\"Nyberg II s.v. ast\", stance=\"supports\", note=\"'ast [’st’] the bones ... +ast-dahišnan corporeal creatures. — Av. ast-; MPrs ’st, stg' (NYB_vol2_glossary.txt line 706).\"),\n    dict(src=\"ARY\", where=\"Aryanpur, root *ost- (ARY_pages.txt, pdf p.88)\", stance=\"supports\", note=\"'واژهٔ فارسی هسته (پهلوی AST, ASTAG به چم استخوان و هستهٔ میوه) نیز از همین واج‌ریشه است' (برهان قاطع cited).\"),\n    dict(src=\"WIKT\", where=\"en.wiktionary استخوان\", stance=\"supports\", note=\"'Inherited from Middle Persian ’sthw’n’ /astuxwān/ “bone”, from Proto-Iranian *HástHáhuānām, a compound from *HástH “bone”, from PIE *h₃ésth₁'.\")],\n ),\n dict(id=3, lang=\"Persian\", words=\"ast 2 «است ۲»; ostoxân «استخوان»; hasteh «هسته»; xastu «خستو ۱»\",\n  verdict=\"confirmed\",\n  derivation=(\"All four New Persian words continue the MP forms of node #2. (a) است ast 'bone' is the bare MP ast, now archaic/medical (Wiktionary marks است as a rare synonym of استخوان). (b) استخوان ostoxân < MP astuxwān, classical ustuxwān, with the regular loss of the labial glide in Iranian Persian (ostoxun colloquially); obsolete variants sotxān/ostoxān are recorded. (c) هسته haste 'stone of a fruit, kernel, nucleus' < MP (h)astag, the same word as astag with the prothetic h- that MacKenzie already reads in Pahlavi (cf. Horn's 'este ‘Knochen, Kern’'); the 'bone → hard kernel' shift is the one Buck notes for this root ('by extension of the hard kernel of fruits to the analogous parts of the body') and Mann glosses Gk. ostéon itself 'bone, kernel'. (d) خستو xastu 'fruit stone' is a further NP by-form of the same word (Horn no.81 lists 'xestu' with este/kūnjeste); Mo'in's Farhang gives خستو '(اسم) هستهٔ میوه' as sense 1, separate from the homograph خستو '(ص.) مقر، معترف' — which is why Nourai's chart writes «خستو ۱».\"),\n  derivation_fa=(\"چهار واژهٔ فارسی نو همه ادامهٔ همین ستاک پهلوی‌اند: «است» همان ast فارسی میانه است که امروز کمکاربرد شده؛ \"\n   \"«استخوان» از astuxwān است که در خوانش کلاسیک ustuxwān بوده و واک میانجی w در فارسی ایران افتاده است (گفتاری: استخون)؛ \"\n   \"«هسته» همان astag است با هٔ افزایشی (مکنزی در پهلوی هم hastag می‌خواند) و تحول معنایی «استخوان ← مغز سخت میوه» در همین ریشه در یونانی ostéon نیز دیده می‌شود؛ \"\n   \"و «خستو» گونهٔ دیگری از همین واژه است (هرن در شمارهٔ ۸۱ xestu را کنار este می‌آورد) و در فرهنگ معین در معنای «هستهٔ میوه» آمده است، جدا از هم‌نویسهٔ «خستو = مقر، معترف». ادعای نورایی درست است.\"),\n  sources=[W['ostoxan'], W['haste'], W['xastu']],\n  ref_check=[\n    dict(ref=\"MON\", status=\"supports\", note=\"Mo'in, Farhang-e Farsi s.v. هسته: '(هَ تِ) (اِ.) ۱- دانة سفتِ داخل میوه‌ها' and s.v. خستو (Farhang-e Farsi) '(اسم) هسته (میوه). نام یکی از اکابر چین', beside Farhang-e Mo'in's second homograph 'خستو (خَ) (ص.) مقر، معترف' — read via abadis.ir (archived).\")],\n  consulted=[\n    dict(src=\"HRN\", where=\"no. 81, p.20\", stance=\"supports\", note=\"Horn lists the whole NP family together: 'est ‘Knochen’, este ‘Knochen, Kern’ (vergl. kūnjeste ...), xestu, g. āste'.\"),\n    dict(src=\"ARY\", where=\"ARY_pages.txt pdf p.88\", stance=\"supports\", note=\"Aryanpur puts هسته (پهلوی AST, ASTAG) under the same IE root as استخوان, Gk. OSTEON, Lat. OS/OSSIS.\"),\n    dict(src=\"MON\", where=\"abadis.ir هسته / خستو (Dehkhoda + Farhang-e Mo'in)\", stance=\"supports\", note=\"Dehkhoda's خستو article gives 'مترادف خستو: ... هسته' and هسته 'مترادف: بذر، تخم، خستو، دانه، مغز'.\"),\n    dict(src=\"SYN\", where=\"Buck 4.16, p.207 (intro)\", stance=\"supports\", note=\"Buck notes that words for 'bone' arise 'by extension of the hard ‘kernel’ of fruits to the analogous parts of the body' — the haste/ast relation.\")],\n ),\n dict(id=4, lang=\"Old Persian\", words=\"ast\",\n  verdict=\"plausible\",\n  derivation=(\"Old Iranian *ast- 'bone' is securely reconstructed (it underlies MP ast/astuxwān and is guaranteed by Av. ast- and Skt. ásthi), but the word is NOT attested in the Old Persian corpus: Kent's lexicon (Old Persian, 1953) and Tolman's Ancient Persian Lexicon have no 'bone', and Wiktionary's tree for استخوان stops at Proto-Iranian *HástH with no Old Persian entry. So the box should read *ast- (reconstructed) rather than an attested Achaemenid form. Nourai's authority here is Abolghasemi's Tarīx-e Moxtasar-e Zabān-e Fārsi p.26, which is a historical-grammar handbook and habitually cites such reconstructed Old Persian forms without asterisks.\"),\n  derivation_fa=(\"صورت ایرانی باستان *ast- «استخوان» بازسازی استواری دارد، اما در سنگ‌نوشته‌های پارسی باستان گواهی ندارد؛ \"\n   \"نه کنت (۱۹۵۳) و نه تولمن در واژه‌نامهٔ پارسی باستان چنین واژه‌ای ندارند و ویکی‌واژه هم زنجیره را از ایرانی باستان *HástH به فارسی میانه می‌رساند بی واسطهٔ پارسی باستان. \"\n   \"پس این خانه باید با ستاره (*ast-) نوشته می‌شد؛ ادعا با احتیاط پذیرفتنی است. ماخذ نورایی، تاریخ مختصر زبان فارسی ابوالقاسمی ص ۲۶، در دسترس نبود.\"),\n  sources=[W['ostoxan'], W['pie_bone']],\n  ref_check=[dict(ref=\"TZF:26\", status=\"not_checked\", note=\"Abolghasemi, Tarīx-e Moxtasar-e Zabān-e Fārsi — refs_online.json records no downloadable copy (ketabnak login only), so p.26 could not be read.\")],\n  consulted=[\n    dict(src=\"KNT\", where=\"Kent, Old Persian, Lexicon\", stance=\"silent\", note=\"grep of KNT.txt for 'bone' and for ast-/asti- returns only pasti- 'foot-soldier' and ustaxand- 'staircase'; no OP word for 'bone' is recorded.\"),\n    dict(src=\"TLM\", where=\"Tolman, Ancient Persian Lexicon\", stance=\"silent\", note=\"no 'bone' entry (the only 'ast'-string hits are the verb form astam 'was' in DB).\"),\n    dict(src=\"WIKT\", where=\"en.wiktionary استخوان / Reconstruction:PIE h₃ésth₁\", stance=\"partial\", note=\"The etymology tree runs PIE *h₃ésth₁ > PIIr *HástʰH > PIr *HástH > MP ’sthw’n with no Old Persian link.\")],\n ),\n dict(id=5, lang=\"Sogdian\", words=\"`stk\",\n  verdict=\"confirmed\",\n  derivation=(\"Sogdian ’stk (Buddhist, Manichaean and Christian Sogdian), vocalised ōstak, 'bone' < *astaka- — i.e. the same *ast- + -aka- suffixation as MP astag, with the regular Sogdian prothetic ’- before the initial cluster. Gharib no.1699 (printed p.66-67 of the Sogdian Dictionary, Nourai's SOD:67) gives '’stk- B, M, S / ōstak <*astaka; Khwar. ’stk; Yaghn. sitak; MP astag ... bone', with the derivatives ’stkyn’y 'bony' (no.1702) and ’stkpys’y. Mo'in's footnote to Borhan s.v. استخوان lists the same Sogdian form among the Eastern Iranian cognates.\"),\n  derivation_fa=(\"سغدی ’stk (در هر سه دبیرهٔ بودایی، مانوی و مسیحی)، بازخوانی‌شده به شکل ōstak «استخوان»، از *astaka- است؛ همان ساخت که در پهلوی astag دیده می‌شود، با الف افزایشی پیش از خوشهٔ آغازین. \"\n   \"قریب (فرهنگ سغدی، مدخل ۱۶۹۹، ص ۶۶–۶۷) همین را با هم‌ریشه‌های خوارزمی و یغنابی sitak و پهلوی astag می‌آورد؛ معین نیز در حاشیهٔ برهان قاطع همین صورت سغدی را ذکر کرده است. ادعای نورایی درست است.\"),\n  sources=[W['ostoxan']],\n  ref_check=[dict(ref=\"SOD:67\", status=\"supports\", note=\"Gharib, Sogdian Dictionary no.1699 (SOD_pages.txt leaf 132 ≈ printed p.66-67): '1699 ’stk- B, M, S / ōstak <*astaka; Khwar. ’stk; Yaghn. sitak; MP astag ... bone' — Nourai's page number is right.\")],\n  consulted=[\n    dict(src=\"SOD\", where=\"nos. 1699, 1701, 1702\", stance=\"supports\", note=\"derivatives ’stkyn’y '(of) bone, bony' (SCE 169) and ’stkpys’y 'bony, limb' confirm the stem.\"),\n    dict(src=\"BQT\", where=\"Mo'in's footnote s.v. استخوان\", stance=\"supports\", note=\"the footnote's Eastern-Iranian list opens 'سغدی ...' beside استی، منجی، اشکاشمی، وخی forms.\"),\n    dict(src=\"IEC\", where=\"s.v. osth-\", stance=\"supports\", note=\"Mann cites 'Oss. (dim. type) ástág, stág' — the same *ast-aka- diminutive as Sogdian ’stk.\")],\n ),\n dict(id=6, lang=\"Latin\", words=\"os 1\",\n  verdict=\"confirmed\",\n  derivation=(\"Latin os, gen. ossis, n. 'bone' is the direct reflex of the PIE root noun, with the geminate -ss- of the oblique stem (*ost-s > oss-) generalised; the doublets ossu/ossua and ossum are late remodellings after genu/genua. Ernout-Meillet s.v. os note that the Iranian branch keeps the unextended form (av. astǝm, azdibīš) while Sanskrit has the i/n-extension ásthi/asthnáh, and that the Latin outcome requires an old oss- rather than *ost-. Watkins (AHD, Nourai's ref) lists it under 'ost-. Bone. 1. Latin os (stem oss-), bone: OS², OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY'.\"),\n  derivation_fa=(\"لاتین os (حالت اضافی ossis) «استخوان» بازماندهٔ مستقیم همین نام‌ریشهٔ هندواروپایی است؛ دوگانهٔ -ss- از ستاک غیرفاعلی (*ost-s > oss-) به همهٔ صرف گسترده شده است. \"\n   \"ارنو-مییه می‌نویسند که زبان‌های ایرانی صورت بی‌گسترش را نگه داشته‌اند (اوستایی astǝm، azdibīš) و وتکینز در پیوست ریشه‌های AHD همین را ذیل *ost- می‌آورد. ادعای نورایی درست است.\"),\n  sources=[W['pie_bone']],\n  ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins 1985 s.v. ost-: 'Bone. 1. Latin os (stem oss-), bone: OS², OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. ... [Pok. ost(h)- 783.]'\")],\n  consulted=[\n    dict(src=\"LAT\", where=\"Ernout-Meillet s.v. os, ossis\", stance=\"supports\", note=\"'os (oss, puis ōs), ossis n. ... : os. — Attesté de tout temps; panroman' with the Iranian/Sanskrit comparison (LAT.txt line 44178 ff.).\"),\n    dict(src=\"SYN\", where=\"Buck 4.16, p.207\", stance=\"supports\", note=\"'Lat. os, gen. ossis, also ossu, ossum (> It. osso, Sp. hueso, Fr., Rum. os)' under 'IE *ost-'.\"),\n    dict(src=\"WLD\", where=\"Bd. I 185\", stance=\"supports\", note=\"'gr. ostéon ‘Knochen’ (wohl *osteyon ‘Beinernes’ = lat. osseum)'.\")],\n ),\n dict(id=7, lang=\"English\", words=\"os; ossify\",\n  verdict=\"confirmed\",\n  derivation=(\"Learned Latinisms, not inherited words: anatomical 'os' (pl. ossa) is Latin os 'bone' taken over unchanged in 17th-c. anatomy, and 'ossify' (1713) is a modern formation on the oblique stem oss- plus -fy (Latin -ficare), on the model of L. ossifragus/ossuarium. Klein: 'ossify, tr. and intr. v., to form or turn into bone. — Formed fr. L. os, gen. ossis, ‘bone’, and suff. -fy'; Watkins lists both OS² and OSSIFY under ost-. Nourai's empty refs= is fine: the Latin-to-English step is uncontroversial.\"),\n  derivation_fa=(\"این دو واژهٔ انگلیسی وام‌واژهٔ عالمانه‌اند و میراثی نیستند: os در کالبدشناسی همان os لاتین است که در سدهٔ ۱۷م عیناً وام گرفته شده، \"\n   \"و ossify ساختهٔ تازه‌ای است از ستاک غیرفاعلی oss- به افزودن پسوند -fy (از -ficare لاتینی). کلاین و وتکینز هر دو همین را می‌گویند؛ ادعای نورایی درست است.\"),\n  sources=[],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"the node carries no reference in the book; the Latin > English step is checked against Klein and Watkins under 'consulted'.\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"s.v. os 'a bone', ossify, ossuary\", stance=\"supports\", note=\"'os, n., a bone (anat.) — L. os, gen. ossis, ‘bone’'; 'ossify ... Formed fr. L. os, gen. ossis, ‘bone’, and suff. -fy' (KLN_1971.txt lines 169373, 169705).\"),\n    dict(src=\"AHD\", where=\"Watkins s.v. ost-\", stance=\"supports\", note=\"'Latin os (stem oss-), bone: OS², OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY.'\")],\n ),\n dict(id=8, lang=\"Greek\", words=\"osteon; ostreon\",\n  verdict=\"confirmed\",\n  derivation=(\"Greek ὀστέον (Att. ὀστοῦν, Dor. ὀστίον) 'bone' is a thematic derivative *ost-ey-om of the root noun (Pokorny: 'gr. ostéon ‘Knochen’ (wohl *osteyon ‘*Beinernes’ = lat. osseum)'); ὀστρεον 'oyster' belongs to the r-stem variant *ost-r- of the same root (Watkins: 'Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd; b. Greek ostreon, oyster'), the animal being named from its hard, bone-like shell — cf. ὀστρακον 'potsherd, shell' and ἀστράγαλος (assimilated from *ostrágalos) 'knucklebone'. Nourai's glosses ('bone', 'oyster') are exact.\"),\n  derivation_fa=(\"یونانی ostéon «استخوان» مشتقی موضوعی *ost-ey-om از همان نام‌ریشه است (پوکورنی آن را برابر osseum لاتین می‌گیرد)؛ \"\n   \"و ostreon «صدف/اویستر» از گونهٔ rدار همین ریشه (*ost-r-) است، زیرا این جانور را به سبب پوستهٔ سخت و استخوان‌ماننددارش چنین نامیده‌اند؛ هم‌ریشه با ostrakon «سفال‌پاره، پوسته» و astrágalos «قاپ، مفصل قوزک». ادعای نورایی درست است.\"),\n  sources=[W['pie_bone'], W['oyster']],\n  ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins s.v. ost-: '2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEUM, SYNOSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon ... b. Greek ostreon, oyster: OYSTER'.\")],\n  consulted=[\n    dict(src=\"POK\", where=\"p.783 (POK_03 leaf 16-17)\", stance=\"supports\", note=\"'gr. ostéon ‘Knochen’ ... vom r-St. ostrakon ‘harte Schale, Scherbe’, ostreon ‘Auster’ ... astragalos ‘Knöchel’ (assimil. aus *ostragalos)'.\"),\n    dict(src=\"KLN\", where=\"s.v. oyster / osteo-\", stance=\"supports\", note=\"'oyster ... fr. L. ostrea, ostreum, fr. Gk. ostreon, ‘oyster’, which is rel. to osteon, ostoun, ‘bone’; so called from its hard shell.'\"),\n    dict(src=\"IEC\", where=\"s.v. osth-\", stance=\"supports\", note=\"Mann glosses 'Gk. ostéon, n. ‘bone, kernel, rib’; ostón, n. ‘shell, jar’' and cross-refers ostrk- 'potsherd'.\")],\n ),\n dict(id=9, lang=\"English\", words=\"osteo-; oyster\",\n  verdict=\"confirmed\",\n  derivation=(\"Two different routes out of Greek. 'osteo-' (before a vowel oste-, ost-) is a modern scientific combining form taken straight from Gk. ὀστέον (osteoblast, osteogenesis, osteoid, osteopathy). 'Oyster' is the popular route: Gk. ὀστρεον > Latin ostrea/ostreum > Old French oistre, uistre (Mod.Fr. huître, with the regular prothetic h- as in huile, huit) > Middle English oistre (late 13th c.) > oyster. Klein and Etymonline give exactly this chain.\"),\n  derivation_fa=(\"دو راه جداگانه: osteo- پیشوندی علمی و نوساخته است که مستقیم از ostéon یونانی گرفته شده (osteopathy، osteoblast)؛ \"\n   \"اما oyster راهی مردمی پیموده است: یونانی ostreon > لاتین ostrea > فرانسهٔ قدیم oistre/uistre (فرانسهٔ امروز huître با هٔ افزایشی مانند huile و huit) > انگلیسی میانه oistre (پایان سدهٔ ۱۳م) > oyster. ادعای نورایی درست است.\"),\n  sources=[W['oyster']],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference given in the book for this node; verified against Klein, Watkins and Etymonline below.\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"s.v. osteo-, oyster\", stance=\"supports\", note=\"'osteo-, before a vowel oste-, ost-, combining form meaning a ‘bone’ ... Gk. osteo-, oste-, ost-, fr. osteon'; 'oyster, n. — ME., fr. OF. oistre, uistre (F. huître), fr. L. ostrea, ostreum, fr. Gk. ostreon'.\"),\n    dict(src=\"ETYMONLINE\", where=\"etymonline.com/word/oyster (archived)\", stance=\"supports\", note=\"'late 13c., oistre, from Old French oistre, uistre ... and directly from Latin ostrea ... from Greek ostreon, from PIE root *ost- “bone” ... The h- in the modern French word is a regular development.'\"),\n    dict(src=\"SKT\", where=\"Skeat s.v. ostracise\", stance=\"supports\", note=\"'Gk. ostrakon, a potsherd, tile, voting-tablet, orig. a shell = Gk. ostreon, an oyster, orig. a shell' (SKT.txt line 12977).\")],\n ),\n]\n\ne1_nodes = [\n dict(id=1, lang=\"Avestan\", words=\"aviš, avišiya\",\n  verdict=\"confirmed\",\n  derivation=(\"Av. āviš is an adverb 'openly, before the eyes, manifestly' (Bartholomae col. 335: 'āviš Adv. ‘offenbar, vor Augen’', Y. 33.7), with the adjective āvišya- 'manifest, notorious'; the exact match of Skt. āvíĥ / avișṭya-. Formally it is the lengthened-grade *aw-is of the root *h₂ew- 'to perceive' (Pokorny's 8. au-, au̥ei-, p.78; Watkins au-⁵ 'To perceive', compound *awis-dh- whence L. audīre) — i.e. 'having (it) in perception'. So the semantic step 'perceive' > 'perceptible, in plain view' is internal to the root, and the derivation root→āviš is standard. Nourai's spelling 'avišiya' for āvišya- is a lax transliteration; the gloss 'heard, known, clear' is a shade loose ('manifest, evident' is closer).\"),\n  derivation_fa=(\"اوستایی āviš قید است به معنای «آشکارا، پیش چشم» (بارتولومه، ستون ۳۳۵، یسنا ۳۳،۷) و صفت هم‌ریشهٔ آن āvišya- «آشکار، هویدا»؛ \"\n   \"برابر دقیق سنسکریت āvíḥ. این صورت گسترشی *aw-is از ریشهٔ هندواروپایی *h₂ew- «دریافتن، دیدن/شنیدن» است (پوکورنی ص ۷۸، همان ریشه‌ای که audīre لاتین از آن است)؛ \"\n   \"پس تحول معنایی «دریافتن ← دریافتنی، آشکار» درون‌ریشه‌ای است. ادعای نورایی درست است، تنها معنای «شنیده‌شده» کمی سهل‌انگارانه است.\"),\n  sources=[W['pie_ear']],\n  ref_check=[\n    dict(ref=\"POK:78\", status=\"supports\", note=\"POK_01.txt leaf 86 = printed p.78: '8. au-, au̥ei- ‘sinnlich wahrnehmen, auffassen’ ... au̥is-: dehnstufig ai. āvis Adv. ‘offenbar, bemerkbar’, av. āvis Adv. ‘offenbar, vor Augen’ (npers. āskār ‘klar’); ai. avistya-, av. āvisya- ‘offenkundig’'.\"),\n    dict(ref=\"HRN:8\", status=\"supports\", note=\"Horn, Grundriss p.8 no.33 (āskār): 'aw. *āviskara- (āvis ‘offenbar, klar’, y. 33, 7)'.\"),\n    dict(ref=\"KLN:126\", status=\"supports\", note=\"Klein s.v. audible (1966 ed. p.126, KLN_1966 leaf 78): 'fr. I.-E. base *awei-, *au-, ‘to perceive’, whence also OI. āvíĥ, Avestic avish, ‘openly, evidently’'.\")],\n  consulted=[\n    dict(src=\"BRT\", where=\"col. 335-336 s.v. āviš\", stance=\"supports\", note=\"'j. āviš Adv. ‘offenbar, vor Augen’' with Y.33.7 (BRT.txt line 7395).\"),\n    dict(src=\"AHD\", where=\"Watkins s.v. au-⁵\", stance=\"supports\", note=\"'au-⁵, To perceive. Compound forms *aw-dh-, *awis-dh-, “to place perception” ... [Pok. 8. au- 78.]' — confirms both the *awis- element and Nourai's page 78.\")],\n ),\n dict(id=2, lang=\"Persian\", words=\"âškâr «آشکار»\",\n  verdict=\"confirmed\",\n  derivation=(\"NP آشکار āškār (also آشکارا āškārā, آشکاره) < MP āškārag [’šk’l(’)k'] 'obvious, evident' (MacKenzie p.14), from Old Iranian *ā-viš-kāra- '(a) making manifest' — āviš (node #1) + the verbal noun kāra- of kar- 'to do', exactly as Skt. āviṣ-kṛ- 'to make manifest', āviṣkāra-. Phonetically *āviškāra- > MP āškārag by loss of the intervocalic -v- before the š cluster (Horn no.33 sets up precisely 'aw. *āviskara-'), and the Armenian loan aškaray shows the Middle Persian form. Pokorny p.78 himself cites 'npers. āskār ‘klar’' under this root, so the chain āviš > āškār is textbook.\"),\n  derivation_fa=(\"«آشکار» از فارسی میانهٔ āškārag است (مکنزی: ’šk’l’k «پیدا، هویدا»)، و آن از ایرانی باستان *ā-viš-kāra- «آشکارکردن» می‌آید، مرکب از قید āviš و ستاک kāra- از ریشهٔ kar- «کردن»؛ \"\n   \"همانند سنسکریت āviṣ-kṛ- و āviṣkāra-. در دگرگونی آوایی، v میانی پیش از خوشهٔ ش افتاده است (هرن در شمارهٔ ۳۳ دقیقاً *āviskara- را بازسازی می‌کند) و وام‌واژهٔ ارمنی aškaray گواه صورت فارسی میانه است. \"\n   \"پوکورنی خود در ص ۷۸ «npers. āskār» را ذیل این ریشه می‌آورد؛ ادعای نورایی درست است.\"),\n  sources=[W['askara'], W['askar']],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"the node carries no reference in the book; the step is checked against Horn no.33, MacKenzie, Pokorny p.78 and Wiktionary below.\")],\n  consulted=[\n    dict(src=\"HRN\", where=\"no. 33, p.8\", stance=\"supports\", note=\"'āskār ‘klar’, āskārā, āskāre. phlv. āskārak, āskārāk, arm. LW. askaray; aw. *āviskara- ... vergl. skr. āviskrta- (ai. āvis) und skr. āviskāra- (spät) selbst.'\"),\n    dict(src=\"PHD\", where=\"MacKenzie p.14 s.v. āškārag\", stance=\"supports\", note=\"'āškārag [’šk’l(’)k' | M ’šq’rg, N āškara] obvious, evident' and āškāragēnīdan 'reveal, confess' (PHD_mackenzie.txt lines 1267-1269).\"),\n    dict(src=\"WIKT\", where=\"en.wiktionary آشکارا\", stance=\"supports\", note=\"'Inherited from Middle Persian ’šk’l(’)k' /āškārāg/ “obvious, evident”'; آشکار is listed as its alternative form.\")],\n ),\n dict(id=3, lang=\"Avestan\", words=\"ŭši; ŭši-dâta\",\n  verdict=\"plausible\",\n  derivation=(\"Av. uš- n. 'ear' occurs almost only in the dual uši 'the two ears', and from that concretely 'hearing', i.e. 'the faculty of grasping, understanding' — Bartholomae col. 413 glosses the dual 'die beiden Ohren; Verstand, Sinn' and its sense (b) '‘Gehör’, d.i. Fähigkeit richtig zu hören und zu verstehen, sva. ‘Auffassungs-, Verstandeskraft’' (Y.62.4 uruṭe uši xratəuš). Pokorny p.785 prints exactly 'Av. uši Nom. Du. ‘die beiden Ohren, Verstand, Sinn’, Instr. Du. uši-bya, npers. hōš'. So 'two ears, intelligence' is right. The other two elements are not: (i) the gloss 'mortal life' does not belong to uši at all — it is imported from the homonymous NP/MP ōš 'death' < Av. aoša- (see node #5); (ii) an Avestan compound 'uši-dāta' is not attested — Bartholomae has uši.darəθra- n. 'Auffassen mit dem Verstand, Begreifen' and the mountain names Uši.dam-/Uši.darəna-, which he derives from ušah- 'dawn' ('der sein Haus bei der Morgenröte hat'), although the Pahlavi version glosses them uš dāštār 'holder of intellect' — which is presumably where Nourai's 'given intelligence' (cross-referred to his root Dô 2 = dā- 'to give') comes from.\"),\n  derivation_fa=(\"اوستایی uš- «گوش» تقریباً همیشه در شمار دوگانه uši «دو گوش» به‌کار رفته و از همان جا معنای «شنوایی، قوّهٔ دریافت، خرد» گرفته است؛ \"\n   \"بارتولومه (ستون ۴۱۳) همین را «دو گوش؛ خرد و هوش» و پوکورنی در ص ۷۸۵ عیناً «uši ... npers. hōš» می‌آورد. پس تا این‌جا درست است. \"\n   \"اما دو نکته نادرست است: یکی معنای «زندگی فانی» که از هم‌نویسهٔ فارسی «هوش = مرگ» (بازماندهٔ aoša- اوستایی) به این‌جا راه یافته؛ \"\n   \"دیگر آنکه مرکب uši-dāta در اوستا گواهی ندارد؛ آنچه هست uši.darəθra- «دریافتن به خرد» و نام کوه Uši.darəna-/Uši.dam- است که بارتولومه آن را به ušah- «بامداد» برمی‌گرداند، هرچند ترجمهٔ پهلوی آن uš dāštār «دارندهٔ هوش» است — و همین پشتوانهٔ نورایی بوده است. پس با احتیاط پذیرفتنی است.\"),\n  sources=[W['pie_ear'], W['hush']],\n  ref_check=[dict(ref=\"POK:785\", status=\"partial\", note=\"POK_03.txt leaf 18 (= printed ≈785): '2. ous- : əus- : us- ‘Ohr’ ... Av. uši Nom. Du. ‘die beiden Ohren, Verstand, Sinn’, Instr. Du. uši-bya, npers. hōš (iran. *auš-) ‘Ohr’' — supports uši, but Pokorny says nothing about 'mortal life' or about a compound uši-dāta.\")],\n  consulted=[\n    dict(src=\"BRT\", where=\"col. 413 s.v. uš-; col. 415-416 s.v. uši.darəθra-, Uši.dam-, Uši.darəna-\", stance=\"partial\", note=\"'j. uš- n. ‘Ohr’ ... b) ‘Gehör’, d.i. Fähigkeit richtig zu hören und zu verstehen, sva. ‘Auffassungs-, Verstandeskraft’'; but for the mountain: 'Eig. ‘der seinen Aufenthalt bei der Morgenröte hat’, Komp. mit LS. (zu ušah-) ... Pü.: uš dāštār' — no uši-dāta.\"),\n    dict(src=\"KLN\", where=\"s.v. ear (1966 ed. p.494)\", stance=\"supports\", note=\"'cogn. with Gk. ous ... L. auris (for *ausis), Avestic ushi, ‘both ears’' — only the 'ear/understanding' sense.\"),\n    dict(src=\"WIKT\", where=\"en.wiktionary هوش, Reconstruction:PIE *h₂ṓws\", stance=\"supports\", note=\"the tree PIE *h₂ṓws > PIIr *HušíH > PIr *HušíH > OP *ušiy > MP ōš > NP هوش carries only 'ear/intellect'.\")],\n ),\n dict(id=4, lang=\"Persian\", words=\"hŭš 1 «هوش ۱»; hŭšyâr «هوشیار»\",\n  verdict=\"confirmed\",\n  derivation=(\"NP هوش hōš (Iranian hūš) 'intelligence, wits' < MP ōš [’ʿš] < Old Iranian *uši- (the Avestan dual uši of node #3), i.e. 'the two ears' > 'hearing' > 'wits'. Pokorny p.785 states the equation outright: 'npers. hōš (iran. *auš-)'. The initial h- is the familiar Persian prothetic h- before an old initial u/ō (cf. MP ōšyār beside NP هوشیار: MacKenzie explicitly notes 'ōšyār [’wšd’l] conscious', flagging the New Persian form as 'N h-'). هوشیار hōšyār is the MP compound ōš-yār, with -yār < *-̄yāra- 'holding, keeping' (cf. hušyār 'wide awake, sober'). Both words are thus regular.\"),\n  derivation_fa=(\"«هوش» از فارسی میانهٔ ōš است و آن از ایرانی باستان *uši- ، همان شمار دوگانهٔ اوستایی uši «دو گوش»؛ تحول معنایی «گوش ← شنوایی ← خرد». \"\n   \"هٔ آغازین «هوش» هٔ افزایشی است که در فارسی نو پیش از واکهٔ آغازین u/ō افزوده می‌شود؛ مکنزی نیز پهلوی ōšyār «هشیار» را می‌آورد و می‌نویسد در فارسی نو با h- است. \"\n   \"پوکورنی در ص ۷۸۵ صریحاً «npers. hōš (iran. *auš-)» می‌نویسد؛ ادعای نورایی درست است.\"),\n  sources=[W['hush'], W['pie_ear']],\n  ref_check=[dict(ref=\"POK:785\", status=\"supports\", note=\"POK_03.txt leaf 18: 'Av. uši Nom. Du. ‘die beiden Ohren, Verstand, Sinn’ ... npers. hōš (iran. *auš-) ‘Ohr’' — exactly Nourai's arrow.\")],\n  consulted=[\n    dict(src=\"PHD\", where=\"MacKenzie p.62 s.v. ōšyār\", stance=\"supports\", note=\"'ōšyār [’wšd’l | N h-] conscious' (PHD_mackenzie.txt line 3877) — the MP antecedent of هوشیار, with the note that New Persian adds h-.\"),\n    dict(src=\"WIKT\", where=\"en.wiktionary هوش\", stance=\"supports\", note=\"'Inherited from Middle Persian ’ʿš /ōš/, from Old Persian *ušiy, from Proto-Iranian *HušíH. Compare Northern Kurdish hiş, Latin auris, English ear.'\"),\n    dict(src=\"BRT\", where=\"col. 413 s.v. uš-, Nachtrag\", stance=\"supports\", note=\"Bartholomae's note to uš-: 'mp. (Pü.) uš, arm. LW. uš, np. hōš ... lat. vgl. auris'.\")],\n ),\n dict(id=5, lang=\"Avestan\", words=\"an-aoša\",\n  verdict=\"disputed\",\n  derivation=(\"The word is real: Bartholomae has 'j. an-aoša- Adj. ‘dem kein Verderben droht, unsterblich’' (Yt 10.125, of Mithra's horses), and adds 'np. vgl. nōš ‘Unsterblichkeitstrank’; s. dazu Hbm. PSt. 19'. What is wrong is the arrow: an-aoša- is a- (privative, an- before a vowel) + aoša- 'destruction, death', and aoša- does not belong to *h₂ows- 'ear' but to the verbal root *Hawš 'to burn, consume' (Cheung, EDIV s.v. *Hauš, from PIE *h₁eus- 'to burn, scorch', Pokorny 347 f.; Skt. oṣ- 'to burn', Lat. ūrō), whence 'consumption > destruction > death'. Wiktionary (following ESIJa I 266-7 and Cheung 2007) derives نوش from Proto-Iranian *an-auša- 'immortal', '*an- + *auša- “destruction”, the latter from Proto-Iranian *Hawš “to burn”, from PIE *h₁ews-'. Nourai's link is not his own invention: it follows the Persian lexicographical tradition, and his own reference is explicit — Noushin (FSF, s.v. انوشه) writes 'anos̱ak ... مرکب از الف و نون (نشانهٔ نفی) + نوش = هوش به‌معنی مرگ، نیستی', i.e. he too equates nōš/hōš 'death' with the hōš of node #4. Modern Iranian etymology keeps the two هوش apart: hōš 'wits' < *uši- (ear) vs the classical hōš/ōš 'death' < aoša- (burning). Hence this edge should hang from a root 'to burn', not from 'ear'.\"),\n  derivation_fa=(\"خود واژه درست است: بارتولومه an-aoša- را «بی‌مرگ، نامیرا» می‌آورد (یشت ۱۰،۱۲۵) و خود به «نوش» فارسی و به پژوهش‌های فارسی هوبشمان (ص ۱۹) ارجاع می‌دهد. \"\n   \"اما جای این واژه در نمودار نادرست است: an-aoša- مرکب است از پیشوند نفی an- و aoša- «نابودی، مرگ»، و aoša- از ریشهٔ فعلی ایرانی *Hawš «سوختن» است \"\n   \"(چونگ، فرهنگ ریشه‌شناختی فعل ایرانی، ذیل *Hauš؛ هندواروپایی *h₁eus- «سوزاندن»، پوکورنی ۳۴۷؛ سنسکریت oṣ-، لاتین ūrō) و ربطی با *h₂ows- «گوش» ندارد. \"\n   \"نورایی این پیوند را از سنت فرهنگ‌نویسی فارسی گرفته است؛ نوشین در واژه‌نامک می‌نویسد «انوشک مرکب از الف و نون (نشانهٔ نفی) + نوش = هوش به‌معنی مرگ، نیستی». \"\n   \"پژوهش امروزی دو «هوش» را جدا می‌داند: هوش «خرد» از *uši- و هوش/اوش «مرگ» از aoša-. پس این پیوند رد می‌شود.\"),\n  sources=[W['nush'], W['anushe']],\n  ref_check=[\n    dict(ref=\"BQT:178\", status=\"partial\", note=\"Borhan (Mo'in ed.) p.178 s.v. انوشه (BQT_v1_pages.txt leaf 396) documents the Persian word ('بمعنی خوش و خرم و خوشحال ... و شراب انگوری را نیز گفته‌اند'), but says nothing that would attach an-aoša- to the 'ear' root.\"),\n    dict(ref=\"FSF:51\", status=\"supports\", note=\"Noushin, Vazhe-namak s.v. انوشه: '۱- بی‌مرگ، جاوید: پهلوی انوشک anōšak مرکب از الف و نون (نشانة نفی) + نوش = هوش بهمعنی مرگ، نیستی' — this IS Nourai's source for equating the second element with hōš, and it is the analysis modern Iranian etymology rejects.\")],\n  consulted=[\n    dict(src=\"BRT\", where=\"s.v. an-aoša- (BRT.txt line 4241, leaf 98)\", stance=\"supports\", note=\"'j. an-aoša- Adj. ‘dem kein Verderben droht, unsterblich’: aurvantō .. mainyuš.hāra- ‘šəihīš Yt 10.125' + 'np. vgl. nōš ‘Unsterblichkeitstrank’; s. dazu Hbm. PSt. 19, AGr. I. 99' — the word, but no link to uši.\"),\n    dict(src=\"CHEUNG\", where=\"EDIV s.v. *Hauš 'to burn'\", stance=\"contradicts\", note=\"'*Hauš ‘to burn’ ... «PIE *H₁eus- ‘to burn, scorch’ = LIV: 245 | Pok.: 347 f. ... Skt. oṣ ‘to burn’ ... REFERENCES: ... ESIJa I: 266' — this, not *h₂ows- 'ear', is the root of aoša-.\"),\n    dict(src=\"WIKT\", where=\"en.wiktionary نوش\", stance=\"contradicts\", note=\"'from Proto-Iranian *an-auša- (“immortal”), from *an- (“not”) + *auša- (“destruction”), the latter from Proto-Iranian *Hawš (“to burn”), from Proto-Indo-European *h₁ews- (“to burn”)' [ESIJa I:266-7; Cheung 2007].\"),\n    dict(src=\"POK\", where=\"p.785 (2. ous- 'Ohr')\", stance=\"silent\", note=\"Pokorny's ear entry lists no aoša-/anaoša-; the 'burn' root is his separate eus- at p.347 f.\")],\n ),\n dict(id=6, lang=\"Pahlavi\", words=\"anôšak; anôšak-ruvân\",\n  verdict=\"confirmed\",\n  derivation=(\"Av. an-aoša- > MP anōš [’nʿš] with the regular Middle Persian monophthongisation au > ō and loss of the thematic ending, extended by the adjectival suffix -ag to anōšag [’nʿšky] 'immortal, undying'. MacKenzie: 'anōš [’nwš] lit. immortal, i.e. the next life; elixir, antidote', with the abstract anōšagīh 'immortality' and the antonym anōš-xwar 'mortal'. The bahuvrīhi anōšag-ruwān 'whose soul is immortal' (ruwān 'soul') is the standard Sasanian honorific of the dead, glossed by MacKenzie 'the late, deceased'; Nyberg cites the patronymic Anōšē-zātān 'Immortal-born' from anōš = anōšak. The edge #5→#6 is exactly right; only its ancestry (node #5) is misplaced.\"),\n  derivation_fa=(\"اوستایی an-aoša- در فارسی میانه به anōš بدل شده است؛ دوواکهٔ au ایرانی باستان در پهلوی به ō ساده شده و پایانهٔ موضوعی افتاده، و با پسوند صفتی -ag به anōšag «نامیرا» رسیده است. \"\n   \"مکنزی: ºnōš در اصل نامیرا، یعنی زندگی پسین؛ اکسیر، پادزهر»، با anōšagīh «بی‌مرگی» و متقابل anōš-xwar «میرا». \"\n   \"ترکیب anōšag-ruwān «روانش بی‌مرگ» لقب رسمی مردگان در دورهٔ ساسانی است؛ نیبرگ نیز نام Anōšē-zātān «زادهٔ نامیرا» را از همین می‌داند. این پیوند درست است؛ تنها جایگاه پدرش در نمودار نادرست است.\"),\n  sources=[W['anushe'], W['nush']],\n  ref_check=[dict(ref=\"BQT:178\", status=\"supports\", note=\"the انوشه page of Borhan (Mo'in ed.) is the entry Nourai draws on; Mo'in's own footnote apparatus there and at انوشیروان ('انوشیروان → رک: انوشروان') give the Pahlavi anōšak background; leaf 396 of BQT_v1_pages.txt.\")],\n  consulted=[\n    dict(src=\"PHD\", where=\"MacKenzie p.10 s.v. anōš, anōšag(-ruwān)\", stance=\"supports\", note=\"'anōš [’nwš] lit. immortal, i.e. the next life; elixir, antidote'; 'anōš-xwar mortal'; English-Pahlavi index: 'immortal ahōš, amarg, anōš(ag)', 'late (deceased) anōšagruwān'.\"),\n    dict(src=\"NYB\", where=\"Nyberg II s.v. Anōšē-zātān\", stance=\"supports\", note=\"'From anōš = anōšak + zāt ‘Immortal-born’' (NYB_vol2_glossary.txt line 463).\"),\n    dict(src=\"WIKT\", where=\"en.wiktionary انوشه\", stance=\"supports\", note=\"'From Middle Persian ’nʿšky /anōšag/ “immortal”, from ’nʿš /anōš/ + -ag ... Cognate with Parthian ’nwš /anōš/ “immortal”, Ossetian ænus, Avestan anaoša.'\")],\n ),\n dict(id=7, lang=\"Persian\", words=\"anušeh «انوشه»; Anošîravan «انوشیروان»\",\n  verdict=\"confirmed\",\n  derivation=(\"انوشه anōša < MP anōšag, with the ordinary NP loss of final -g/-k after a vowel (anōšag > anōša, cf. Borhan's by-form نوشه nōša with aphaeresis). In classical usage it is (i) 'immortal, undying' — hence a salutation 'may you be immortal!' (Hubschmann, PSt. 19: 'Np. anōša ‘heil!’ ursprünglich wohl = ‘sei unsterblich’!'), which is the sense of the Ferdowsi line quoted in the chart (بدو گفت پیران که ای شهریار / انوشه بُدی تا بود روزگار), and (ii) by the lexicographers 'happy, glad; grape wine' — both glosses stand in Borhan s.v. انوشه, which is why Nourai's gloss reads 'eternal, happiness, wine'. انوشیروان Anōšīrwān (also Nōšīrwān) is the same MP compound anōšag-ruwān 'of immortal soul', contracted in New Persian, the standing epithet of Khosrow I. Nourai's own translation, '\\\"with eternal spirit\\\"', is right.\"),\n  derivation_fa=(\"«انوشه» از anōšag پهلوی است با افتادن معمول -g پایانی در فارسی نو (در برهان قاطع گونهٔ «نوشه» با افتادن الف آغازین نیز ثبت است). \"\n   \"در کاربرد کلاسیک دو معنا دارد: یکی «بی‌مرگ، جاوید» که در دعای «انوشه بُدی» دیده می‌شود (هوبشمان، پژوهش‌های فارسی ص ۱۹: «انوشه! در اصل یعنی بی‌مرگ باش!»)، \"\n   \"و دیگری «خوش، خرم، خوشحال؛ شراب انگوری» که همان معانی برهان قاطع است و توضیح معنای مرکب نورایی («جاوید، شادی، شراب») را می‌دهد. \"\n   \"«انوشیروان» همان anōšag-ruwān پهلوی «دارای روان بی‌مرگ» است که در فارسی نو فشرده شده و لقب خسرو اول است. ادعای نورایی درست است.\"),\n  sources=[W['anushe']],\n  ref_check=[\n    dict(ref=\"BQT:178\", status=\"supports\", note=\"Borhan (Mo'in ed.) s.v. انوشه (BQT_v1_pages.txt leaf 396 ≈ printed 178): 'بمعنی خوش و خوشا و خرم و خوشحال باشد - و شراب انگوری را نیز گفته‌اند - و نام عمة شاپور هم هست ... و بمعنی آفرین و بارک‌الله هم آمده است', immediately followed by 'انوشیروان → رک: انوشروان' — both of Nourai's words and all three of his glosses.\"),\n    dict(ref=\"FSF:51\", status=\"supports\", note=\"Noushin s.v. انوشه: '۱- بی‌مرگ، جاوید: پهلوی انوشک ...' and quotes the very verse printed in the chart, 'بگفت پیران که ای شهریار / انوشه بدی تا بود روزگار' (FSF_pages.txt lines 2874-2885).\")],\n  consulted=[\n    dict(src=\"HRN\", where=\"no. 128, p.30\", stance=\"supports\", note=\"'enōše ‘glücklich, heil!’, vergl. hōš, nōše, nōšīn. aw. anaoša- ‘unsterblich’; phlv. anōšak ‘unvergänglich’; arm. LW. anušak, anoiš.'\"),\n    dict(src=\"HUB\", where=\"Persische Studien p.19 (ad Horn 128)\", stance=\"partial\", note=\"Hübschmann accepts 'np. anōša ‘heil!’ ursprünglich wohl = ‘sei unsterblich’!' but insists on splitting off the 'sweet' words: 'Ich kann die Begriffe ‘unsterblich’ und ‘süss’ nicht vereinigen und trenne daher die Wörter'.\"),\n    dict(src=\"FSF\", where=\"Vazhe-namak s.v. انوشه/نوشه\", stance=\"partial\", note=\"Noushin argues that the Shahnameh line adduced by the dictionaries (and by Mo'in in his notes to Borhan) for نوشه 'happy' actually reads توشه, i.e. he doubts the 'happiness' sense on that evidence.\")],\n ),\n dict(id=8, lang=\"Persian\", words=\"nŭš «نوش»; nŭšîn «نوشین»; nŭšîdan «نوشیدن» (extra نوشدارو، نوشابه)\",\n  verdict=\"plausible\",\n  derivation=(\"نوش nōš 'ambrosia, elixir, antidote' is MP anōš 'elixir, antidote (lit. immortal)' with aphaeresis of the unstressed initial a-, exactly as انوشه ~ نوشه; the compounds نوشدارو nōš-dārū and نوشابه nōšāba are built on it, and Bartholomae's note to an-aoša- names 'np. nōš ‘Unsterblichkeitstrank’' as the reflex. نوشیدن nōšīdan 'to drink' is then a denominative of that noun ('to take the elixir' > 'to drink'), nūš being its present stem. The one point where sources part company is نوشین 'sweet' (and نوش 'sweet'): Hübschmann (PSt. 19, precisely on Horn's no.128 which Nourai cites) refuses to unite 'immortal' and 'sweet' and sets up two words — (1) nōš 'grati saporis, suavis, dulcis', nōšīn, Arm. loan anoš 'fragrant, tasty'; (2) nōš 'aqua vitae', nōš-dārū, Pahl. anōš 'Unsterblichkeitstrank'. Wiktionary and the Persian tradition (Dehkhoda, Mo'in) keep them together, comparing نوشین and نوشیدن under انوشه. Hence: nūš and nūšīdan confirmed, nūšīn only plausible — and the whole group inherits the wrong grandparent from node #5.\"),\n  derivation_fa=(\"«نوش» همان anōš پهلوی «اکسیر، پادزهر؛ در اصل نامیرا» است که الف آغازین بی‌تأکیدش افتاده است، همان‌گونه که «انوشه ~ نوشه»؛ \"\n   \"ترکیب‌های «نوشدارو» و «نوشابه» بر همین ساخته شده‌اند و بارتولومه خود «np. nōš میٔ بی‌مرگی» را بازماندهٔ an-aoša- می‌داند. \"\n   \"«نوشیدن» فعلی است ساخته‌شده از همین اسم («نوش خوردن» ← «آشامیدن») و nūš ستاک حال آن است. \"\n   \"تنها اختلاف بر سر «نوشین = شیرین» است: هوبشمان (ص ۱۹، در نقد همان شمارهٔ ۱۲۸ هرن که نورایی ارجاع می‌دهد) «بی‌مرگی» و «شیرینی» را یکی نمی‌داند و دو واژهٔ جدا می‌نشاند، \"\n   \"ولی ویکی‌واژه و سنت فارسی (دهخدا، معین) همه را یکجا می‌آورند. پس این خانه با احتیاط پذیرفتنی است.\"),\n  sources=[W['nush'], W['anushe']],\n  ref_check=[\n    dict(ref=\"ARM:206\", status=\"not_checked\", note=\"A. Aryan, Farhang-e Vazheha-ye Hamanand (Armenian-Avestan-Pahlavi-Persian) vol. I — refs_online.json records it as available only behind a ketabnak login; not downloaded.\"),\n    dict(ref=\"HRN:30\", status=\"supports\", note=\"Horn, Grundriss p.30 no.128: 'enōše ‘glücklich, heil!’, vergl. hōš, nōše, nōšīn. aw. anaoša- ‘unsterblich’; phlv. anōšak' — Horn does group nōš/nōšīn here, exactly as Nourai.\")],\n  consulted=[\n    dict(src=\"HUB\", where=\"Persische Studien p.19, ad no. 128\", stance=\"contradicts\", note=\"'Ich kann die Begriffe ‘unsterblich’ und ‘süss’ nicht vereinigen und trenne daher die Wörter: 1) np. nōš ‘grati saporis, suavis, dulcis’, nōšīn ...; 2) np. nōš ‘aqua vitae’, nōš-dāru, nōš-giyā ‘antidotum’, ... phl. anōš ‘Unsterblichkeitstrank’' — i.e. nōšīn 'sweet' does not belong here.\"),\n    dict(src=\"WIKT\", where=\"en.wiktionary نوش / انوشه\", stance=\"supports\", note=\"نوش: 'From Middle Persian ’nwš /anōš/ “elixir, antidote”, literally “immortal” ... Derived terms نوشابه, نوش‌دارو ... Verb: نوش present stem form of نوشیدن “to drink”'; انوشه: 'Compare نوشین “sweet” and نوشیدن “to drink”'.\"),\n    dict(src=\"PHD\", where=\"MacKenzie s.v. anōš\", stance=\"supports\", note=\"'anōš ... elixir, antidote' — the Middle Persian noun from which NP نوش and its compounds come; the English index gives 'antidote anōš, šud-bēš, pādzahr'.\"),\n    dict(src=\"BRT\", where=\"note to an-aoša-\", stance=\"supports\", note=\"'np. vgl. nōš ‘Unsterblichkeitstrank’; s. dazu Hbm. PSt. 19, AGr. I. 99'.\")],\n ),\n]\n\ndata = {\n \"pdf_page\": 376,\n \"book_page\": 346,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  dict(entry=0, root=\"Ost\", verdict=\"confirmed\",\n   modern_form=\"PIE *h₃ésth₁ (alt. *h₂óst) 'bone' — Pokorny's ost(h)-, Watkins' ost-\",\n   note=(\"The root, its language label and its gloss are all right. Pokorny 783 lemmatises 'ost(h)-; ost(h)i, ost(h)r(g), obl. ost(h)-(e)n- ‘Knochen’' and Watkins prints 'ost-. Bone.' with '[Pok. ost(h)- 783]', so Nourai's spelling 'Ost' is AHD's. Modern reconstruction is a neuter root noun *h₃ésth₁ (Wiktionary; alternative *h₂óst, since Celtic asgwrn/askourn wants *h₂-, Latin os wants *h₃-, and Greek ostéon wants root-final *h₁); the shape *HestH is required by the -th- of Skt. ásthi. \"\n    \"Nourai's cross-reference 'See the note under root Kost: rib bone' points at the old idea that Lat. costa / OCS kostĭ are the same noun with a k-prefix; Watkins registers it cautiously ('kost-. Bone. Probably related to ost-'), Buck 4.162 calls it 'attractive but dub.', and Walde-Pokorny I 185 says the connection 'überzeugt nicht'. So that note deserves the hedge it gets. \"\n    \"One drafting slip in the Avestan box (node #1): 'ascu' and 'asča' are the same word (asču, stem asčav- 'shin, calf'), with the glosses split between them.\"),\n   note_fa=(\"ریشه، برچسب زبانی و معنای آن هر سه درست است. پوکورنی در ص ۷۸۳ مدخل ost(h)- «استخوان» دارد و وتکینز در پیوست AHD همان را *ost- می‌نویسد؛ \"\n    \"پس شکل «Ost» در کتاب برگرفته از AHD است. بازسازی امروزی یک نام‌ریشهٔ خنثی *h₃ésth₁ است (یا *h₂óst)؛ ث در سنسکریت ásthi نشان می‌دهد که ساخت ریشه *HestH بوده است. \"\n    \"یادداشت نورایی دربارهٔ ریشهٔ Kost (دنده) به این اندیشهٔ قدیم اشاره دارد که costa لاتین و kostĭ اسلاوی همان واژه با پیشوند k- باشد؛ \"\n    \"وتکینز این را با احتیاط می‌پذیرد، باک آن را «dub.» می‌خواند و والده-پوکورنی می‌نویسد «قانع‌کننده نیست». تنها لغزش نمودار در خانهٔ اوستایی است: ascu و asča یک واژه‌اند (asču «ساق») که معناهایشان جابه‌جا شده است.\"),\n   sources=[W['pie_bone'], W['ostoxan'], W['oyster']],\n   ref_check=[dict(ref=\"POK:783\", status=\"supports\", note=\"POK_03.txt leaf 16-17 (printed 782-783) carries the lemma 'ost(h)-; ost(h)i, ost(h)r(g), obl. ost(h)-(e)n- ‘Knochen’ ... Ai. asthi n., Gen. asth-n-áh, av. ast-, asti- n. ‘Knochen’ ... gr. ostéon ... lat. ossu, ossua'; Watkins independently cites '[Pok. ost(h)- 783]', confirming the page.\")],\n   consulted=[\n     dict(src=\"AHD\", where=\"Watkins 1985 s.v. ost- (and kost-)\", stance=\"supports\", note=\"'ost-. Bone. 1. Latin os (stem oss-) ... 2. Greek osteon ... 3. Suffixed form *ost-r- ... [Pok. ost(h)- 783.]'; 'kost-. Bone. Probably related to ost-.'\"),\n     dict(src=\"SYN\", where=\"Buck 4.16 BONE, p.207\", stance=\"supports\", note=\"'1. IE *ost-, etc. ... Grk. ostéon; Lat. os, gen. ossis ...; Skt. asthi-; Av. ast-, asti-; Arm. oskr; Alb. asht. Here also ChSl. kosti? See below, 6' — and §6: 'Further analysis of both as k-ost- ... is attractive but dub.'\"),\n     dict(src=\"WLD\", where=\"Walde-Pokorny Bd. I 185\", stance=\"supports\", note=\"the same lemma, with the explicit verdict on the k- theory: 'Beziehung von ost(h)- zu lat. costa ‘Rippe’, abg. kostĭ ‘Knochen’ ... überzeugt nicht' (WLD_Bd1_pages.txt line 17107).\"),\n     dict(src=\"IEC\", where=\"Mann s.v. osth-\", stance=\"supports\", note=\"'osth- (osthn-, o’st-) ‘bone’. WP I, 185 ... Hitt. hastai (for *hast) ... Lat. os (f. for *osts), gs. ossis'.\"),\n     dict(src=\"WIKT\", where=\"Reconstruction:Proto-Indo-European/h₃ésth₁\", stance=\"supports\", note=\"'*h₃ésth₁ n — bone. The original form was a neuter root noun, as can be seen from Latin os and Avestan ast-. ... Medial -th- in Sanskrit ásthi requires root of the form *HestH.'\")],\n   nodes=e0_nodes),\n  dict(entry=1, root=\"Ôus 1, Au 1, Aus 1\", verdict=\"plausible\",\n   modern_form=\"PIE *h₂ṓws (oblique *h₂éws-) 'ear', itself *h₂ew- 'to perceive' + *-s\",\n   note=(\"Two things are being asserted at once. (a) That the 'ear' noun and the 'perceive' root are one: Nourai's box unites Pokorny's 8. au-, au̥ei- 'sinnlich wahrnehmen' (p.78) with his 2. ous- : əus- : us- 'Ohr' (p.785) and glosses the whole 'ear'. Pokorny himself keeps them as separate lemmas and so does Watkins (au-⁵ 'To perceive' [Pok. 8. au- 78] vs ous-/aus- 'Ear' [Pok. ous- 785]); but Klein, whom Nourai also cites, gives the base of 'ear' as '*au ‘ear’' (p.494) and of 'audible' as '*awei-, *au- ‘to perceive’' (p.126), and today's standard reconstruction does exactly what Nourai does — Wiktionary derives *h₂ṓws 'ear' from *h₂ew- ('to see' > 'to hear' after Anatolian splits off) + the root-nominal *-s. So the union is defensible, though the gloss should be 'perceive; ear' rather than plain 'ear'. \"\n    \"(b) That Av. an-aoša- 'immortal' and its whole Persian progeny (anōšag, anuše, Anōšīrwān, nūš, nūšīdan) hang from this root through a sense 'mortal life' of Av. uši. That is wrong (node #5): aoša- 'destruction, death' belongs to *h₁ews- 'to burn' (Pokorny 347 f., Cheung s.v. *Hauš), and only the accident that classical Persian has two homographs هوش — 'wits' < *uši- and 'death' < aoša- — made the Persian lexicographers (Noushin, whom Nourai cites at FSF:51, and Borhan's commentators) identify them. Everything on the uši/hūš/āškār side of the chart is sound; the anōš-branch is correctly drawn internally but attached to the wrong root.\"),\n   note_fa=(\"در این خانهٔ ریشه دو ادعا با هم آمده است. یکی اینکه نام «گوش» و ریشهٔ «دریافتن» یکی‌اند: نورایی مدخل ۷۸ پوکورنی (au-، au̥ei- «حس کردن») را با مدخل ۷۸۵ (ous- «گوش») یکی می‌گیرد. \"\n    \"خود پوکورنی و وتکینز این دو را جدا می‌آورند، اما کلاین (ص ۴۹۴) ریشهٔ «گوش» را *au می‌گذارد و بازسازی امروزی نیز همین را می‌کند: *h₂ṓws «گوش» از *h₂ew- به‌علاوهٔ پسوند اسمی *-s. پس این یکی‌گرفتن پذیرفتنی است، هرچند معنای ریشه باید «دریافتن؛ گوش» می‌بود. \"\n    \"دوم اینکه an-aoša- اوستایی و همهٔ فرزندان فارسی‌اش (انوشه، انوشیروان، نوش، نوشیدن) از این ریشه و از معنای «زندگی فانی» برای uši باشد؛ این نادرست است. \"\n    \"aoša- «نابودی، مرگ» از ریشهٔ *h₁ews- «سوختن» (پوکورنی ۳۴۷؛ چونگ ذیل *Hauš) است و تنها هم‌نویسگی دو «هوش» در فارسی کلاسیک فرهنگ‌نویسان (نوشین در واژه‌نامک و حواشی برهان) را به این یکی‌گرفتن کشانده است. \"\n    \"بازوی uši/هوش/آشکار درست است، اما بازوی انوش به ریشهٔ نادرست بسته شده است.\"),\n   sources=[W['pie_ear'], W['hush'], W['nush']],\n   ref_check=[\n     dict(ref=\"POK:78\", status=\"supports\", note=\"POK_01.txt leaf 86 = printed p.78: '8. au-, au̥ei- ‘sinnlich wahrnehmen, auffassen’ ... au̥is-: ... av. āvis ‘offenbar, vor Augen’ (npers. āskār ‘klar’) ... lat. audio ‘höre’ aus *auiz-dh-iō'. The page number is right, but Pokorny's gloss is 'perceive', not 'ear'.\"),\n     dict(ref=\"POK:785\", status=\"supports\", note=\"POK_03.txt leaf 18: '2. ous- : əus- : us- ‘Ohr’, erweitert mit -i (ousi-s), -es (ousos- n.) und -en. Av. uši Nom. Du. ... npers. hōš (iran. *auš-) ‘Ohr’; gr. dor. ὦs; lat. auris; got. ausō'. Pokorny lists this as a lemma of its own, not as an extension of 78.\"),\n     dict(ref=\"KLN:126\", status=\"supports\", note=\"Klein s.v. audible (1966 p.126): 'L. audio, audire ... prob. stands for *awis-d-iō, fr. I.-E. base *awei-, *au-, ‘to perceive’, whence also OI. āvíĥ, Avestic avish, ‘openly, evidently’'.\"),\n     dict(ref=\"KLN:494\", status=\"supports\", note=\"Klein s.v. ear (1966 p.494): 'cogn. with Gk. ous ... L. auris (for *ausis), Avestic ushi, ‘both ears’ ... All these words derive fr. I.-E. base *au ‘ear’' — Klein's single base *au- is exactly Nourai's merged root box.\")],\n   consulted=[\n     dict(src=\"AHD\", where=\"Watkins s.v. au-⁵ and ous-\", stance=\"partial\", note=\"Watkins keeps them apart: 'au-⁵, To perceive ... [Pok. 8. au- 78.]' and 'ous-. Also aus-. Ear ... [Pok. ous- 785.]' — no derivational link is drawn between the two.\"),\n     dict(src=\"WIKT\", where=\"Reconstruction:Proto-Indo-European/*h₂ṓws\", stance=\"supports\", note=\"'Etymology: From *h₂ew- (“to see”) + *-s (root nominal suffix), with a semantic shift to “to hear” after the split of the Anatolian branch' — i.e. today's standard view unites the two, as Nourai does.\"),\n     dict(src=\"CHEUNG\", where=\"EDIV s.v. *Hauš 'to burn'\", stance=\"contradicts\", note=\"the 'mortal life / immortality' branch of this chart belongs to '*Hauš ‘to burn’ ... «PIE *H₁eus- ... Pok.: 347 f.', not to the 'ear' root.\"),\n     dict(src=\"BRT\", where=\"col. 413 s.v. uš- ; col. 335 s.v. āviš\", stance=\"supports\", note=\"Bartholomae's own notes tie both Iranian branches to the same family: uš- 'Ohr' ('mp. uš, arm. LW. uš, np. hōš ... lat. vgl. auris') and āviš 'offenbar, vor Augen'.\")],\n   nodes=e1_nodes),\n ],\n}\n\nout='/home/sfmqrb/git/rishe/data/verification/page-376.json'\nwith io.open(out,'w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('written', out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-376.py",
 "description": "Build the page-376 verification JSON"
}
```


### [2026-09-07T20:45:17.250Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-376.json
```


## [2026-09-07T20:45:26.652Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-376.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 376",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-07T20:45:28.198Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 4, 'confirmed': 12, 'disputed': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 18, 'not_checked': 5, 'partial': 2}
books consulted: {'partial': 5, 'supports': 43, 'silent': 3, 'contradicts': 3} | by book: {'WIKT': 8, 'BRT': 6, 'PHD': 5, 'KLN': 4, 'IEC': 3, 'HRN': 3, 'WLD': 2, 'LAT': 2, 'NYB': 2, 'ARY': 2, 'SYN': 2, 'AHD': 2, 'POK': 2, 'HUB': 2, 'MON': 1, 'KNT': 1, 'TLM': 1, 'SOD': 1, 'BQT': 1, 'ETYMONLINE': 1, 'SKT': 1, 'CHEUNG': 1, 'FSF': 1}
```


## [2026-09-07T20:45:35.329Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-376.json'))\nn=d['entries'][0]['nodes'][0]\nprint(n['derivation'][:900])\n\" ; git status --short",
 "description": "Sanity check node 1 text and git status"
}
```


### [2026-09-07T20:45:41.110Z] TOOL RESULT

```
Av. ast- n. 'bone' is the unextended root noun of PIE *h₃ésth₁ (Bartholomae, AiW col. 313 'ast- n. ‘Knochen’, von Menschen und Tieren', gen. pl. astam, instr. pl. azdbīš; beside it the i-stem asti- and the n. 'astay-). Buck 4.16 and Pokorny 783 both list exactly 'av. ast-, asti- n. ‘Knochen’', so root→Avestan is uncontroversial. The other two forms are one and the same word doubled: Bartholomae has j. asčav- m. 'Unterschenkel, Wade' (nom. asču, V. 8.63-65), i.e. 'shin, calf' — Klein (s.v. os 'bone', Nourai's KLN:1099) cites it as 'Avestic ascu-, ‘shinbone’' and Mann (IEC s.v. osth-) as 'ascus m. ‘shin’', both under the same *ost- noun. So Nourai's 'ascu' and 'asča' are the same lexeme (asču / stem asčav-); his gloss split ('ascu: bone' vs 'asča: shin bone') is inexact, and the shape 'asča' is not an attested Avestan nominative. Bartholomae himself compares Gk. ἰσχίον rather than ast-, so
 M data/verification/sources/web/index.jsonl
?? data/verification/page-376.json
?? data/verification/sources/web/011b62dde870a80d.txt
?? data/verification/sources/web/10a472dfd05a9fb2.txt
?? data/verification/sources/web/46de964006f4ef2a.txt
?? data/verification/sources/web/93eaf6e5d0758898.txt
?? data/verification/sources/web/a6743c07dae52e0c.txt
?? data/verification/sources/web/ab62cce6ec083b54.txt
?? data/verification/sources/web/b6b751e1585aaf67.txt
?? data/verification/sources/web/de0a53b891e147ce.txt
?? data/verification/sources/web/ff7e9b1baa06d2b4.txt
```


## [2026-09-07T20:45:47.850Z] TOOL CALL #88: Bash

```json
{
 "command": "ls -la data/verification/sources/web/a73393a8dd84dadf.txt data/verification/sources/web/e0ce78063f8f2671.txt 2>&1 | head; git log --oneline -1; git status --short | wc -l",
 "description": "Check archived files present"
}
```


### [2026-09-07T20:45:47.931Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 7568 Sep  7 16:22 data/verification/sources/web/a73393a8dd84dadf.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 6926 Sep  7 16:30 data/verification/sources/web/e0ce78063f8f2671.txt
7868596 Verify page 373 (Ôku/âhu, kašak, ocean, accipiter; Okw/nešân, eye, ocular)
11
```


## [2026-09-07T20:46:17.972Z] AGENT

Done. `verify_check.py 376` reports **0 PROBLEM lines**, 17/17 nodes verified.

**Page 376 (book p. 346) — 2 entries, 17 nodes**

Verdicts: nodes 12 confirmed · 4 plausible · 1 disputed; roots 1 confirmed (Ost) · 1 plausible (Ôus 1/Au 1/Aus 1).
Ref checks: 18 supports · 2 partial · 5 not_checked (TZF:26, ARM:206 — no accessible copies; 3 nodes carry no refs in the book).

**disputed**
- *Ôus 1* #5 Avestan `an-aoša` — the word is genuine (Bartholomae: "an-aoša- 'dem kein Verderben droht, unsterblich'", Yt 10.125), but it does not descend from *uši* 'ears/intellect': `aoša-` 'destruction, death' belongs to *h₁ews- 'to burn' (Pokorny 347 f.; Cheung EDIV s.v. *Hauš; Wiktionary/ESIJa I 266-7). Nourai follows Noushin (his own FSF:51), who equates the second element with هوش 'death'; modern Iranian etymology keeps the two homographic هوش apart. Everything below the node (anōšag → anuše/Anōšīravān/nūš) is internally correct but hangs from the wrong root.

**plausible (flagged in the notes, not in the FLAG list)**
- *Ost* #1: "ascu" and "asča" are one word (Av. asču, stem asčav- 'shin, calf'); the glosses are split/swapped. Klein p.1099 and Mann do put it under *ost-, Bartholomae compares Gk. ἰσχίον instead.
- *Ost* #4 Old Persian `ast`: not attested in the OP corpus (Kent and Tolman silent; Wiktionary's tree goes PIr *HástH → MP directly) — should be starred.
- *Ôus* #3: Av. `uši-dāta` is unattested (Bartholomae has uši.darəθra- and the mountain Uši.darəna-, from ušah- 'dawn', Pahlavi gloss uš dāštār); the gloss "mortal life" is imported from the other هوش.
- *Ôus* #8: `nūšīn` 'sweet' is separated from the anōš group by Hübschmann (PSt. 19, on the very Horn no. 128 Nourai cites); Wiktionary/Dehkhoda keep them together.

**Root notes**: Ost = PIE *h₃ésth₁ (alt. *h₂óst), Pok. 783, Watkins ost- — confirmed; the "Kost" cross-note is duly hedged (Watkins "probably related", Buck "dub.", Walde-Pokorny "überzeugt nicht"). The ear root merges Pokorny's separate 78 (au- 'perceive') and 785 (ous- 'ear'); Pokorny and Watkins keep them apart, but Klein p.494 and Wiktionary (*h₂ṓws < *h₂ew- + *-s) do exactly what Nourai does — hence plausible, with the gloss better read 'perceive; ear'.

**No extraction errors** — the JSON matches the chart in every node; nothing needed the printed page.

Sources archived via `fetch_source.py` (Wiktionary استخوان/هوش/نوش/انوشه/آشکارا + PIE *h₃ésth₁/*h₂ṓws, abadis هسته/خستو, Etymonline oyster); local books quoted with file/leaf/column: POK_01 leaf 86 (=p.78), POK_03 leaves 16-18, BRT cols 313/335/413 + an-aoša-, HRN nos. 33/81/128, HUB p.19, PHD, NYB, SOD no. 1699 (p. 66-67 = SOD:67 ✓), BQT_v1 leaves 338-341/396 (استه، استخوان with Mo'in's footnote; انوشه), FSF s.v. انوشه (has the exact Ferdowsi verse printed in the chart), SYN p.207, AHD, KLN 1966 pp. 126/494/1099, IEC, WLD I 185, LAT, ARY p.88, CHEUNG s.v. *Hauš.
