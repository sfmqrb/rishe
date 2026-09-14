# Verification process log — verify-page-420


## [2026-09-14T01:21:27.464Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 420 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-420.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-420.json. Write /home/sfmqrb/git/rishe/data/verification/page-420.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 420` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:28.509Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:29.245Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:29.258Z] TOOL RESULT

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


## [2026-09-14T01:21:29.746Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-420.txt"
}
```


### [2026-09-14T01:21:29.776Z] TOOL RESULT

```
1	=== PDF page 420 (book page 390) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Rek, Reg 2 : to tie  (refs POK:863; WLD2:362)
4	#1 (parent #0) [Sanskrit] refs=WLD2:362; POK:863 | račana, rašanâ : rope, strap, belt
5	  #2 (parent #1) [Pahlavi] refs=SNS:227 | rasan : rope
6	    #3 (parent #2) [Persian] refs=HRN:137; SNS:227 | rasan «رَسَن» : rope, string | extra: رَسَن زدن | NOTE: to measure with a rope (tape). MON:1654 & AFM:72 claim "rasan" is the Arabic pronunciation of Persian "rîsmân".  PLA:138 claims Arabic "rasan" is from Pahlavi "rasan".
7	--- entry 1 ---
8	ROOT Rekp -> redirect to Rei 2
9	--- entry 2 ---
10	ROOT Rěkto -> redirect to Reg 1
11	--- entry 3 ---
12	ROOT [Indo-European] Rem : to rest  (refs POK:864)
13	#1 (parent #0) [Avestan] refs=POK:864; KLN:1335; SYN:841; AEF:351 | râman : quiet ; airime : quietly ; hu-rama : well rested ☞Su 1 ; paiti-râman : well arranged, pleasant ☞Per 3
14	  #2 (parent #1) [Persian] refs=BQT:737,960; HRN:5; AEF:351; FAF:251; FFD:25 | râm «رام ( شهرام ، رامش ، رامین ، رمه )» : quiet ; ârâm «آرام ( آرامش ، آرمیدن ، رامیدن )» : quiet ; xorram «خرّم» : fresh, pleasant, cheerful ; pedrâm «پدرام» : "pleasant", a male name
15	#3 (parent #0) [Old Persian] refs=KNT:206 | ram : to be at peace
16	  #4 (parent #3) [None] refs=None |  | NOTE: box is printed entirely blank in the source (outlined box, no header text or content)
17	#5 (parent #0) [Old High German] refs=KLN:1335 | rasta : to rest
18	  #6 (parent #5) [English] refs=None | rest
19	
```


## [2026-09-14T01:21:31.252Z] AGENT

I'll start by looking at the source JSON and the reference infrastructure.


## [2026-09-14T01:21:32.960Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-420.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\n\"",
 "description": "Read source JSON for page 420"
}
```


## [2026-09-14T01:21:33.716Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:21:34.897Z] TOOL RESULT

```
{
 "pdf_page": 420,
 "book_page": 390,
 "entries": [
  {
   "root": {
    "name": "Rek, Reg 2",
    "lang": "Indo-European",
    "refs": "POK:863; WLD2:362",
    "gloss": "to tie"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Sanskrit",
     "refs": "WLD2:362; POK:863",
     "words": [
      {
       "translit": "račana, rašanâ",
       "gloss": "rope, strap, belt",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Pahlavi",
     "refs": "SNS:227",
     "words": [
      {
       "translit": "rasan",
       "gloss": "rope",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 2,
     "lang": "Persian",
     "refs": "HRN:137; SNS:227",
     "words": [
      {
       "translit": "rasan",
       "gloss": "rope, string",
       "script": "رَسَن"
      }
     ],
     "script_extra": "رَسَن زدن",
     "note": "to measure with a rope (tape). MON:1654 & AFM:72 claim \"rasan\" is the Arabic pronunciation of Persian \"rîsmân\".  PLA:138 claims Arabic \"rasan\" is from Pahlavi \"rasan\".",
     "quote": {
      "text": "برو کتف و یالش همانند من ـ تو گویی که داننده برزد رَسَن",
      "poet": "Ferdowsî"
     }
    }
   ]
  },
  {
   "root": {
    "name": "Rekp",
    "redirect": "Rei 2"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Rěkto",
    "redirect": "Reg 1"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Rem",
    "lang": "Indo-European",
    "refs": "POK:864",
    "gloss": "to rest"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:864; KLN:1335; SYN:841; AEF:351",
     "words": [
      {
       "translit": "râman",
       "gloss": "quiet",
       "script": null
      },
      {
       "translit": "airime",
       "gloss": "quietly",
       "script": null
      },
      {
       "translit": "hu-rama",
       "gloss": "well rested",
       "script": null,
       "see": [
        "Su 1"
       ]
      },
      {
       "translit": "paiti-râman",
       "gloss": "well arranged, pleasant",
       "script": null,
       "see": [
        "Per 3"
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
     "refs": "BQT:737,960; HRN:5; AEF:351; FAF:251; FFD:25",
     "words": [
      {
       "translit": "râm",
       "gloss": "quiet",
       "script": "رام ( شهرام ، رامش ، رامین ، رمه )"
      },
      {
       "translit": "ârâm",
       "gloss": "quiet",
       "script": "آرام ( آرامش ، آرمیدن ، رامیدن )"
      },
      {
       "translit": "xorram",
       "gloss": "fresh, pleasant, cheerful",
       "script": "خرّم"
      },
      {
       "translit": "pedrâm",
       "gloss": "\"pleasant\", a male name",
       "script": "پدرام"
      }
     ],
     "note": null,
     "quote": {
      "text": "اگر چه راه نا پدرام باشد - بپدرامد چو خوش فرجام باشد",
      "poet": "Vîs-o-Râmîn"
     }
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Old Persian",
     "refs": "KNT:206",
     "words": [
      {
       "translit": "ram",
       "gloss": "to be at peace",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": null,
     "refs": null,
     "words": [],
     "note": "box is printed entirely blank in the source (outlined box, no header text or content)",
     "quote": null
    },
    {
     "id": 5,
     "parent": 0,
     "lang": "Old High German",
     "refs": "KLN:1335",
     "words": [
      {
       "translit": "rasta",
       "gloss": "to rest",
       "script": null
      }
     ],
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
       "translit": "rest",
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


### [2026-09-14T01:21:34.933Z] TOOL RESULT

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


## [2026-09-14T01:21:40.590Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','WLD2','SNS','HRN','MON','AFM','PLA','KLN','SYN','AEF','BQT','FAF','FFD','KNT','BRT','PHD','NYB','IEC','AHD','ARY','CHEUNG','SKT']:\n    v=d.get(k)\n    print('==',k,'==')\n    print(json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Check refs_online metadata"
}
```


### [2026-09-14T01:21:41.655Z] TOOL RESULT

```
== POK ==
{"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== WLD ==
{"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== WLD2 ==
null
== SNS ==
{"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will 
== HRN ==
{"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== MON ==
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== AFM ==
{"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "covers_etymology": true, "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.", "
== PLA ==
{"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P
== KLN ==
{"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== SYN ==
{"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== AEF ==
{"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فر
== BQT ==
{"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== FAF ==
{"title": "A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
== FFD ==
{"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"], "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 =
== KNT ==
{"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec
== BRT ==
{"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== PHD ==
{"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
== NYB ==
{"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
== IEC ==
{"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== AHD ==
{"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== ARY ==
{"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== CHEUNG ==
null
== SKT ==
{"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
```


## [2026-09-14T01:21:47.730Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_02.txt POK_03.txt POK_full.txt; do echo \"=== $f\"; grep -n \"reĝ-\\|rek-\\|rem-\\|remə-\\|ram-\" $f | head -40; done",
 "description": "Grep Pokorny for rek/rem roots"
}
```


### [2026-09-14T01:21:48.817Z] TOOL RESULT

```
=== POK_02.txt
537:Wurzelerweiterung  grem-:
876:grem-  , feucht  (sein),  untertauchen,  untersinken'.
1430:2.  gher-  ,hart    worüber    streichen,    reiben';    vgl.    auch    die   Erweiterungen ghrei-,  ghreu-,  ghrem-,  ghren-,  sowie  oben  gröd-, Gr.  -/.eyxQog  , Hirse,  Korn',  Y.axQvq  , geröstete  Gerste'  (diss.  aus  *gher-ghro- und  *ghn-ghru-);   xegadog  n.  und   x^Q^Q'>  -d^og   f.    , Geröll,   Kies'    {*gherdd- oder  *ghernd-  ?) ;    x^Quaq^  -adog  f.  , Kiesel,  Schleuderstein' ;
1729:1.  ghrem-  ,scharf  worüber  reiben,  zerreiben,  abkratzen',  Erw.  von  gJier-  ds.
1731:lit.  gremziu,  gremzti  ,schaben',  grdmdau,  -yti  ,kratzen,  schaben',  lett. gremzu,  gremzt  , nagen,  beißen',  graffistU  , zusammenraffen'  (gegen  eine  andere Einreihung  der  halt.  Worte  s.  unter  ger-,  grem-  , fassen') ;  anders  Mühlen- bach-Endzelin  I  637,  649.  Vgl.  lit.  grendziu,  gresti  unten  unter  ghren-.
1733:2.  ghrem-  ,laut  und  dumpf  tönen,  donnern,  grollen,  zornig  sein* ;  ghromo-s^
1735:Av.  gram-  , ergrimmen,  Grimm  hegen'  (nur  im  Partiz.  Präs.  grdmdntam , derer,  die  uns  grimm  sind'  und  Partiz.  Perf.  Pass.  granta-  aus  *ghramita' , ergrimmt'),  npers.  yaram  , Grimm' ;
1748:lit.  grendu,  gresti  und  grendziu,  gresti  , tüchtig  reiben,  scheuern'  (dehnst. Präs.),  Iter.  grdnd-au,  -yti  (vgl.  gremzti  oben  unter  1.  glirem-)]  russ.  grjada.
3503:A.  Auf  -k-  (gebrochene  Reduplikation):  kerk-,  krek-,  krok-:
3577:dazu  als  ,Decoct'  auch  cremor  ,der  aus  aufgeweichten  Getreidekörnern oder  sonst  aus  Pflanzen  gewonnene  Saft,  Brei' ;  ferner  gall.  ytÖQixa,  xovgfii, air.  coirm  n.,  mcymr.  cwrwf,  acorn.  corefj  coruf  ,Bier',  wozu  vielleicht ai.  karam-h{h)d-  m.  , Grütze,  Brei',  kulmäsa-  m.  .saurer  Schleim  von Früchten,  saurer  Reisschleim';  vgl.  ferner  toch.  B  kark-,  kärk-  .braten, rösten'.
3708:(kerem-),  krem-  (:  krom-)  und  kerm-  (bes.  mit  s-Formans)  1.  ,Zwiebel- und  Knoblaucharten* ;  2.  , Eberesche  u.  dgl.' ;  Anlaut  k-,  vereinzelt  k-.
3717:russ.  ceremcha,  cerema,  ceremucha  , Faulbaum,  Ahlkirsche,  Prunus  padus', klr.  cerem-cha,  -uclia  ds.,  sloven.  örp7n-ha,  -sa  (und  mit  Palatal)  sr'^m-§a,  -sa ds.,  poln.  trzemcha,  öech.  tremcha,  heute  stremcha  ds.,
4380:I.  krek-  (-k-?)  ,schlagen',  auch  vom  Festschlagen  des  Gewebes,  des  Ein- schlages in  der  Weberei,  daher  auch  ,weben,  Gewebe'. Gr.  x^exw  ,schlage,  klopfe ;  schlage  das  Gewebe  fest',  Tcgöycrj  ,Einschlag- faden,  Gewebe',   xqö^   ds.,  y,Qoy,ovv   ,weben',   xqoy,vq,  -vdog   f.  , Wollflocke';
4386:2.  krek-j  krk-  ,Froschlaich,  Fischlaich,  schleimiges  Zeug  im  Wasser'.
4391:j.  krek-  ,Schallwort*  s.  oben  S.  567  ff.  unter  1.  ker-.
4392:4.  krek-  :  krok-,  mit  -u-  erweitert  ,ragen,  hervorragen'?  und  ,vorspringender Balken  oder  Pflock  u.  dgl.'.
4399:krem-  s.  oben  S.  580  f.  unter  kerem-.
=== POK_03.txt
541:C.  Kons.  Erweiterungen  von  per-  s.  noch  miier  perk',prek-  .gesprenkelt^^ pers-  ,sprühen,  spritzen,  gesprenkelt'.
574:aus  einem  dem  lat.  pri[s]mus  ähnlichem  '^prisjni-,  -ei:  air.  rem-  Präf. (lenierend)  ,vor,  voran'  {rlam  ,vor  ihm',  remi  .vor  ihr'),  remi-  als  Präverb, Präpos.  re  (nas.).
668:1.  perk-,  prek-  ,füllen,  auffüllen'?   Nur  indisch  und  irisch.
677:2.  perk-,    prek-    ,gesprenkelt,    bunt',    oft    zur  Bezeichnung  gesprenkelter,
691:4.  perk-,  prek-,  prk-  ,f ragen,  bitten';  prk-skä-  ,Frage'.
695:2.  Ai.  präS'  , (gerichtliche)  Befragung*,  av.  frasä  f.  ,Frage*,  ai.  prstha- (=  av.  parUa-)  ,Gerichtsf rage*,  prasnä-,  av.  frasna-  m.  ,Befragung,  Frage* (=  ahd. /ra^an  , Specht^  KZ  62,  31,  2),  arm.  harsn  ,Braut,  Neuvermählte, Schwiegertochter*  (vgl.  got.  fraihnan) ;  lat.  procus  ,Freier',  prex  f.  ,Bitte', precoTy  -äri  »bitten*,  umbr.  pepurkurent  3.  PL  Fut.  ,poposcerint* ;  got. fraihnan  ,f ragen*,  aisl.  fregna,  ags.  frignan  (und  to-Präs./ricnaw)  ds.,  as. Prät.  fragn]  ags.  friccea  ,Herold*;  germ.  *frehii-  in  aisl.  frUt  f.  Frage, Erforschung*,  ags.  frtht  f.  , Wahrsagung* ;  ahd.  fräga  ,Frage*  i^fräg-on^ -en,  frohen  ,fragen*),  aisl.  frägr,  ags.  gefrcege,  as.  gifrägi  ,berühmt*; ablaut.  ahd.  fergön  ,bitten* ;  aisl.  prositi,  bitten ;  lit.  Iterat.  praSaü^  -yti »fordern,  bitten*;  toch.  A  prak-j  B  prek-  , fragen*.
1164:2.  reg-,  rek-  (rek-  ?)  , feucht,  bewässern,  Regen^
1166:2.  rek-  {rek-  ?)  in :  got.  rign  n.  ,Regen'  (*rek-nö-)j  krimgot.  reghen,  aisl. regn  n.,  as.  regan,  regin  m.,  afries.  rein,  ags.  reg{e)nj  ren  m.,  ahd.  regan^ regin,  regen,  mhd.  regen  m. ;  aisl.  rigna  ,regnen',  ahd.  reganon  ds.  usw. ;  lit. (mit  westidg.  /j?)  rokia,  rökii  ,fein  regnen',  rÖke  , Staubregen'.
1212:5.  rei-  , stützen*  s.  unter  reid-^  reih  und  rem-,
1261:rek-  ,emporragen' ;  , Stange^  usw.,  wie  reik-,  s.  dort.
1265:2.  rek-  , anordnend
1270:rek-,  reg-  ,binden'?
1276:rem-,  rems-  ,ruhen,  sich  aufstützen;  stützen';   im   Germ.   ,Latte,  Leiste^? rom-ti  , Stütze';  Beziehung  zu  era-,  re-  ,ruhen'  (S.  338 f.)  ist  fraglich.
1280:ahd.  rama  , Stütze,  Gestell,  Webe-  oder  Stickrahmen',  mnd.  ramty (=  mnd.  mhd.  reme),  ramen  ds.;  got.  rimis  n.  ,Ruhe';  aisl.  rgnd  f.  ,Rand, Saum,  Schild',  ags.  rand  m.  , Schildrand,  Schild',  ahd.  rant  m.  ,Rand/^ Einfassung,  Schild',  norw.  rande  und  ablaut.  rinde  , Erdrücken,  Bank', krimgot.  rintsch  ,mons',  span.  (*got.)  randa  ,Leiste';  norw.  rand  f.  ,Quer- balken,  Sims',  nhd.  bair.  ranten  , Stange'  (:  lit.  ramtiSj  ramstis  ,Stütze,  Ge- länder'); ahd.  ramft  ,Rand,  Einfassung'  kann  *rom-ti-  sein,  aber  allenfalls auch  auf  der  Erw.  rem-hh-  beruhen,  vgl.  ai.  rambhd-  m.  ,Stab,  Stütze', norw.  rimhj  rimme  ,Erdrücken',  lit.  rambüs  , träge',  rembeti  ,träge  sein; nicht  recht  wachsen  wollen';
1283:toch.  AB  räm-,  B  ram-  , sich  neigen,  beugen'.
1751:acymr.  hepp,  mcymr.  heby(r),  cymr.  e5(e),  ehr  , sagte',  mcymr.  Jiebu jSprechen',  go-hebu  ,antworten',  cymr.  ,entsprechen',  mcymr.  gwrtheb  , Ant- wort', cymr.  , Einwand',  corn.  gordeby  , antworten' ;  mcymr.  diliaereb  , Sprich- wort' (*de-ad-pro-sky:o-),  air.  ärosc  ds.  {*ad-pro-sknO-)'j  mir.  rose  , dithyram- bische Dichtung'  (*pro-sk'!io-)  ]  air.  in-coissig  {^ind- com- sech-  aus  "^sek^-) , bezeichnet',  täsc  , Anzeige' (*<o-a(i-sÄ;"o-),  ecosc  , Erscheinung'  (^en-kom-sk'^o-)] mcymr.  atteb,  ncymr.  ateb  ,  Antwort'  (^ati-sek'^-)^  air.    aitliesc  n.   , Antwort'
2299:ker-k-,  daneben  kir-k-  (aus  redupl.  *ki-kro-)  und  {s)krek-:
2302:(s)krek-  in  nd.  schrege,  schräge,  mhd.  schrcBge  ^schräg',  mnd.  mhd.  schräge ,kreuzweise  stehende  Holzfüße';  klr.  körkiis  m.  ,Nacken',  korkosi  PI. , Achseln',  dech.  krk  ,Hals'  usw.  (vgl.  oben  ai.  k^ka-)-^  ksl.  sz-krzcüi  , zu- sammenziehen', russ.  körcu,  -ih  ds.,  , Gesichter  schneiden',  körca,  horc , Krampf,  okorca  ,gebogener  Teil  des  Schlittens',  öech.  dial.  krkoäka , Knorren  am  Holz',  krkva  ,Runzel,  Falte'  usw.;  auch  wruss.  korch  , Faust' usw.  aus  *k^rk-so-?  ]
2347:aisl.  skera  ,schneiden,  stechen,  abmachen',  ahd.  sceran  ,scheren,  ab- schneiden', ags.  scieran  ds.,  as.  sker-sahs  , Schermesser' ;  ahd.  scero  , Maul- wurf, nhd.  Schermaus,  norw.  vatn-skjer  u.  dgl.  ,Spitzmaus'  (vgl.  unten ags.  scierfe-müs  , Spitzmaus') ;  Kaus.-Iter.  ahd.  scerian,  as.  skerjan,  ags. scierian  ,zuteilen,  bestimmen';  aisl.  sk^r  f.  ,Haar;  Rand;  Ende',  ags.  sceörrit f.  ,das  Haarschneiden;  Anteil',  ahd.  scara  , Heeresabteilung,  Schar  usw.', mnd.  schare  f.  ds.  (daraus  aisl.  skqr  f.,  skari  m.  , Schar,  Menge^) ;  mit nicht  klarer  Bed. -Entw.  ahd.  liaram-skaraj  as.  harm-skara,  ags.  hearm- scearu  , Strafe,  Plage' ;
3239:aisl.  sparkr  , lebhaft,  rührig',  aisl.  spr^kr,  norw.  sprWk,  schwed.  dial. spräker  ,lebhaft',  auch  ,strahlend,  glänzend',  dän.  dial.  sprceg  ,hochmütig, prahlend'  {*spregi-) ;  engl,  sprinkle  ,sprengen,  besprengen,  sprühen',  schwed. dial.  spräkkel  , Fleck'  (,*Spritzer'),  spräckla  ,die  Masern',  norw.  und  nisl. sprekla,  mhd.  spreckel  ,(Haut)-fleck',  nasal,  mhd.  sprinkelj  sprenkel , Sprenkel , Fleck';  r-lose  Formen  sind  mnd.  spinkel  =  sprinkel,  mnl.  spekelen  ,be- sprengen',  nl.  spikkel  ,Fleck,  Sprenkel',  ags.  specca  ds.,  lit.  spüogas  ,Fleck, Punkt';  —  ohne  anl.  s,  und  gleichzeitig  als  Variante  neben  '^perk-^  "^prek- ,gesprenkelt'  (S.  820 f.):  dXsl.  freknöttr  ,sommersprossig',  norw.  und  nisl. frekna  , Sommersprosse',  engl,  freak  , gestreift  machen';
4511:über  gelangen'. Ai.  tirdh  Adv.  ,weg,  abseits',  Präp.  m.  Akk.  ,durch  —  hin,  über — weg* ter  auch  m.  Abi.  ,abseits  von')  =  av.  tard,  tarö  Adv.  , seitwärts,  un- merkt',  Präp.  m.  Akk.  ,durch  —  hin,  ��ber  —  hin,  über  —  hinweg,  hinaus; :esehen  von,  außer';  air.  tar  m.  Akk.  ,über- hinaus'  (^tares,  idg.  *Ures, |1-  tairse,  tairsiu  ,trans  eam,  trans  eos,  eas,  ea),  woneben  tairm-,  tarmi-  ds., •,  tremi-  ,durch'  (cymr.  trim-uceint  ,30',  ,Dekade  über  20  hinaus'),  um- Itet  nach  rem-:re  ,vor,  voran';  ai.  tirai-cä  Adv.  ,quer  durch'  =  av.
4536:^-,  trek-  {tork-j  trok-)  , drehen',  wohl  Erweiterung  von  3.  ter-  ,reiben, drehend  reiben'.
4726:11090),  dhregh-  (oben  S.  273).  dherägh-  (oben  S.  257).  dhreg-  (vgl.  auch 'klänge  unter  der-  , schinden' :  Wurzelf orm  dergh-j  dreg-  und  unter  dher- ^Iten':  Wurzelform  dheregh-,  dheregh-)  und  trek-  (S.  1092). ^.  I  752f.,  WH  II  697 ff.,  Trautmann  325.  H.  Lewis  BBCS.  9,  34f. 69
4774:ffot.  ^.rams^ei  ,Heuschrecke  (idg.  *trems;  wie  m  aksl.  tresg  Yerqmd .    von  trem-  und  ^m-) ;  as.  Mnmman  st.  V.  ,anschwellen'  oder  »^ekü« werden';  aisl.  pramma   ,trampeln,   schwer  gehen',  mnd.  drammen  ,WUW heftig  drängenS  dram  ,Lärm,  Bedrängnis,  Getümmel*  (:  lett.  ^r^m^), Intensivgemination?  ,•  ^j*—
4779:v^l.  1.  ter-  , zappeln',  woraus  ^trem-  und  *tres-  erweitert  sind.
4800:Wie  trem-  und  tres-  wohl  Erweiterung  von  1.  ter-  ,zappeln'.
5779:hitt.  ueriia-  ,rufen,  beauftragen',  Partikel  -uar-  eigentlich  ,sagte*; vielleicht  (trotz  Vasmer  2,  508  f.  und  oben  S.   860)   hierher  baltosUr. urek-,  urek-  in  lit.  rekiilj  rlktij  lett.  rekt  , schreien',  r^kuot  ,sich  unterhalten ; aksl.  rek^j  resti  , sagen',  ablaut.  aksl.  rok^  , Frist,  Termin',  rä6h  ,Ankla|y
5786:WP.  I  283  f.,  WH.  II  756  f.,  Trautmann  238,  360,  Vasmer  1,  234  f.,  2, 539,  Frisk  469 ff.;  hierher  wohl  urek-.
5791:D.  uerk-,  urek-:  gr.  ^«xog,  äol.  ßQaxog  {*fQ(xxog)  n.  ,Lumpen,  zerlumptes Kleid;  Runzel';  ßga^alov  qdnalov  Hes.;  ßgaycsrov  dqeTtavoVj  ytXaöevtrjQiov Hes.,  Q(x/.sTQOv  ds.;
5792:E.  uresk-  (aus  *urek-sk-),  u^sk-  ai.  vrscdti  ,haut  ab,  spaltet*,  vrdScana- ,abhauend',  n.  , das  Abhauen',  2?ra-wa5Ä:a- m.  , Schnitt*;  ava-vraSca-  , Splitter'; russ.-ksl.  vraska  usw.  ,Runzel'  (*uorska).
=== POK_full.txt
6529:airem{*ariomd). Gen. aireman' plowman ', also PN Airem-6n\ 
12391:Root / lemma: b^erem-1 
12402:b^rem-:b^rom-: 
12425:Root / lemma: b^erem-2 
12437:gr. cpoppiv^, -YYO<;f- "zither', because of suffixes loanword? Initial sound variant *brem- 
12459:As extensions *b^rem- perhaps here the onomatopoeic words: Old Indie bbr/jga-b ' g\ant 
13282:Note: An extension at most in *b^erem- "drone, grumble' and treated onomatopoeic words 
13313:Note: extensions of b'^er- "shine, appear, seem', b'^ereg-, b'^erek- 'shine'. 
18415:Root / lemma: {der-3), dra-, dreb- drem-, dreu- 
18453:drem-: 
18477:derived Root/ lemma: {der-3), dra-, drab- dram-, drau-\ "to run'. 
19120:derek-. 
24191:Latin prandium ' a late breakfast, luncheon ' {*pram-ediom'7), edulus " trencherman ' 
27404:Root / lemma: erek-1 {erfejgh^ 
27414:Root / lemma: erek-1 {eije]gh^\ louse, tick, derived from a suffixed Root/ lemma: er-2, eri- 
27423:under Indo Germanic *erek-. Furthermore it is to be compared Armenian o(r)Jirv\\\., louse' 
27444:Root / lemma: er(e)k-2, rek-, rok- 
27756:See also: compare rem-, this is put together like res- with (e)ra-. 
31179:root extension grem-: 
31186:maybe alb. {grem-) grem/ne' bottom, hole, abyss', grem/s'thro\N to the abyss, pile up' 
31197:maybe alb. Geg grumull grumbull {* grem-ul) "mass, pile' [common alb. /77>/77^ shift] : 
33057:Note: compare also the extensions ghrei-, ghreu-, ghrem-, ghren-, as well as above grod- 
33797:Root / lemma: ghrem-1 
33827:Root / lemma: ghrem-2 
33833:Material: Avestan gram- " become angry, feel rage ' (only in participle present gramantqm^ 
33940:present). Iter, grand-aunder -yti {compare gremzti above under ghrem-'f); russ. grjada. 
34492:Root / lemma: grem- 
45816:Root/ lemma: [kerem-), krem-{: krom-) and kerm- 
45822:Root/ lemma: [kerem-), krem-{. krom^ and kerrn-: 1) onion, garlic; 2) ash-tree, derived 
45847:Prunus padus', kir. cerem-cha, -ucha6s., sloven, crem-ha, -5a(and with palatal) srem-sa, 
45906:mcymr. cwrwf, acorn, coref, coruFbeef, wherefore perhaps Old Indie karam-b(h)a-'(r\. " 
46017:A. Auf -Ar- (broken reduplication): kerk-, krek-, krok-: 
46914:kubarem-b "headfirst, hastily', kubect "a humming spinning top, a spinning top that makes 
48312:Root / lemma: krek-1 {-k-7) 
48341:Root / lemma: krek-2, kfk- 
48372:Root / lemma: krek-3 
48382:Root / lemma: krem- 
48384:See also: see above S. 580 f. under kerem-. 
48713:Root / lemma: krek-4 : krok- 
66371:Root / lemma: perk-1, prek-
```


## [2026-09-14T01:21:48.898Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_03 leaf 101 (p863)\"; awk 'BEGIN{RS=\"\\f\"} NR==102' POK_03.txt | head -60",
 "description": "Print Pokorny page 863 area"
}
```


### [2026-09-14T01:21:49.920Z] TOOL RESULT

```
=== POK_03 leaf 101 (p863)
 Schaar',  gaeaf-rawd  .Winterszeit'  =  mir.  gem-rad  ds.,  mcymr.  bed- rawd,  cymr.  bedd-rod,  bret.  bez-ret  , Gräber'  (cymr.  bedd  .Grab'),  dazu  miri rä(i)the  .Jahreszeit.  Vierteljahr'  {^rötio-)]
air.  rethim  .laufe'  mit  Kompositis.   Kaus.  roithim  .treibe  an';  Verbaln. riutli  m.  .Lauf  (*/-<«-);  zu  air.  do-riuth  ,accurrö'  gehört  cymr.  tyred  (*to-rete)     . ,komm!';  air.  fo-riutkj  cymr.  ^2to-r6(ia/ ,succurrö',   acymr.  Perf.  gua-raut =  ir.  fo-rdith  (*upo-röt-e);
aisl.  rqdull  m.  ,Strahlenkranz,  Sonne'  und  as.  radur,  ags.  rador,  rodor  "" m.  ,Himmel';  got.  *raps  ,leicht',  (Kompar.  n.  rapizo)  ags.  rced  .schnell,  ^ behend',  ahd.  rado,  rato  adv.  ,schnell';  and.  rath,  afr.  reth,  ahd.  rad ,Rad',  radelöt  ,mit  Räderchen  versehen';  lit.  rätas  m.  ,Rad,  Kreis'  (Plur. rätai  ,Karren,  Wagen'),  lett.  rats  ,Rad'  (Plur.  rati  , Wagen'),  lit.  ratelis m.  ,Rädchen'  (vgl.  ahd.  radelöt  und  lat.  rotula  f.  ,Rädcheii'),  dvirätis (meist  PL  dviräöiai)  .zweirädriger  Wagen';
lit.  ritü,  risti  .rollen'  (*r^) ;  aber  gall.  petor-ritum  .vierrädriger  Wagen' kann  lat.  Entwicklung  von  *petor-roto-  sein;
WP.  II  368.  WH.  II  443  f..  Trautmann  238.
ret-,  rot-,  rgt-  .Stange.  Stamm,  Balken  gefüge'.
Ahd.  ruota,  aisl.  röda  ,Rute,  Stange',  as.   röda  .(Pfahl)  kreuz',   ags.  röd ds.    und   ksl.   rati§te,   ratoviste   , Lanzenschaft' ;   vielleicht   dazu   lat.   retae ,aus  dem  Ufer  des  Flusses  hervorragende  Bäume',  retäre  .den   Fluß  von  — solchen  reinigen'  und  o^ätis  .Floß'.  :
WP.  II  368.  WH.  II  420,  431.  ^
867
reti',  ^^""»  ^""  Schall  Wurzel  ^brüllen,  heisere  Laute  ausstoßen^;  , brummen,
murren';  roudo-  , Klage'.
\\,  räu-ti,  ruvdt'i,  ravati  ^brüllt,  lärmt,  dröhnt',  rdva-,  ravdtha-  m.  _,Ge-
briill*';   gl'-  (hotoLiat   ,heule,   brülle,   stoße   einen   Schrei  aus^,   (hq-Ddöv  Adv.
mit  GebrülP  (Präfix  idg.  ö);  lat.  rümor  ,Geräusch,  Ruf,   Gerücht^;   rävus
heiser^,  ravis  f.  , Heiserkeit',  raucus  ,heiser',  raviö  -ire',sich  heiser  reden';
ao-s.  reon  , Wehklagen',    mhd.  rienen  (*reunön)   ,klagen,  jammern';    aisl.
rymja  ,brüllen,  brummen',  ryjiir  m.  ,grobe  Stimme';
ksl.  revg,  rjuti  und  aksl.  rovo,  ruti  ,brüllen',  6ech.  f-üjö  (alt),  Hje  f. Geschrei  des  Hirsches,  Brunstzeit',  poln.  rnja  f.  ,Brunst(zeit)'  (daraus lit.  rujä,  lett.  ruoja  f.) ;  slar.  ^rovq  neben  *7'juti  aus  *reuö,  *reuti,  danach *rjoüg  >  "^rjevo]
mit  der  Bed.  des  dumpfen,  aber  heimlichen  Murmeins:  air.  rün  ,Ge- heimuis',  cymr.  rliln  ds. ;  got.  rüna  f,  ,Geheimnis',  as.  rüna,  mnd.  rüne ^heimliches  Flüstern,  h.  Beratschlagen,  Runenzei
```


## [2026-09-14T01:21:54.536Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1255,1300p' POK_03.txt",
 "description": "Print Pokorny rek/rem entries"
}
```


### [2026-09-14T01:21:54.589Z] TOOL RESULT

```
Ai.  leläydtij  Ullydti  ,schwankt,  schaukelt,  zittert',  leläyä  Instr.  ,schwan- kend,  in  unruhiger  Bewegung';
got.  reiran  (schw.  V.)  ,zittern,  beben',  reirö  , Zittern,  Erdbeben'. WP.  II  349.
r
863
^ito-,  i"^^^^"  ;^"&'  Schulter  von  Tieren'.
^4rm.  e^^  Gen.  ervoy  ,Bug,    Schulter  von  Tieren';   lit.   rietas  m.   ^Ober- schenkel,  Lende',  lett.  iHeta  f.  ,Bein';  ksl.  i^ih,  öech.  rit  ;podex^ Trautraann  242,  Liden  Mel.  Pedersen  88  f.
rek-  ,emporragen' ;  , Stange^  usw.,  wie  reik-,  s.  dort.
Aisl.  rä  f.  (*rahö)  , Stange  in  einem  Gerüst  zum  Trocknen,  Schiffsrahe', nind.  räj  mhd.  rahe  f.  ,Stange,  Rahe';  norw.  dial.  raaga  (*regön-)  , dünne Stange';  nd.  rack  , Gestell,  Wandregal',  mhd.  reck(e)  ^lange  dünne  Stange, bes.  zum  Überhängen  von  Kleidern';  mhd.  rachj  -lies  und  rac, -ges,  dehn- stufig rcehe  , steif;  mhd.  regen  st.  V.  ,sich  erheben,  starren,  emporragen', Faktitiv.  regen  schw.  V.,  ,aufrichten,  erregen,  bewegen,  wecken'  (*7^agjan), nhd.  regen ;  norw.  dial.  raga  , schwanken' ;  sehr  unsicher,  ob  als  reduk- tionsstufig hierher  mhd.  rogel  ,nicht  fest,  schwankend',  sich  rugelen  ,sich rühren',  nhd.  dial.  rogeln  ,wackeln',  aisl.  vugla  ,in  Unordnung  bringen, stören';  geminiert  rugga  , schaukeln,  bewegen*;  rykkia  ,rücken,  eilen',  ags. roccian  , schaukeln'  (engl,  rock)^  ahd.  rucken,  nhd.  ^rücken^,  aisl.  ryJckr, ahd.  ruc  m.  ,Ruck'  i^rukki-) ;
lit.  rekles  , Stangengerüst  zum  Trocknen,  Räuchern'.
WP.  II  361  f..  Wissmann  Nom.  postverb.  176.
2.  rek-  , anordnend
Ai.  racayati  ^verfertigt,  bildet',  racana-  n.  ,Ordnen,  Betreiben';  got. rahnjan  ,rechnen';  ragin  n.  ,Rat,  Beschluß',  aisl.  regin,  PL  rggn  ,die  rat- schlagenden Mächte,  Götter',  as.  ragino  giscapu  ,  Beschlüsse  der  göttlichen Mächte',  ahd.  regin-  in  Eigennamen;  aksl.  rokh  m.  , bestimmte  Zeit,  Ziel', rekq,  restij  , sagen',  raknqti,  raSiti  ,wollen'  usw. ;  toch.  A  rake,  B  reki^ PI.  rekauna  ,Wort';
mit  e:  got.  ga-rehsns  f.  , Bestimmung,  Ratschluß';  aksl.  riöh  f.  ,accusatio';
ganz  unsicher  Zusammengehörigkeit  mit  aisl.  rän  n.  ,Raub'  (*rahna-)j r'cena  , rauben'  (^rahnjan),  ahd.  bi-rahanen  ,erbeuten';  Grundbedeutung wäre  ,Raub- Anschlag' ?
WP.  II  362,  Trautmann  243.
rek-,  reg-  ,binden'?
Ai.  rasanä  f.  ,Strick,  Riemen,  Gürtel',  rasmi-  m.  , Strang,  Riemen,  Zügel' ; aschwed.  hurraka  {hurd-)  ,Heck-Band',  aisl.  rakki  m.  ,Stropp   zum   Fest- halten der  Rahe',  ags.  racca  m.  ds.,  aisl.  rekendi  n.,  rekendr  f.  PL  ,Kette, Fessel';  ags.  racente,  racete  f.,  ahd.  rahhinza  f.  d. WP.  II  362.
864
•
rekph-  ,schädigen^
Ai.  rdksas-  n.  ,Qua],  Quälgeist,  Unhold'^  av.  ra§ah-  ^Schädigung,  Schaden  , bes.  der  im  andern  Leben',  raSayeiti  ^schädigt' ;  gr.  igex^o)  ^zerre  und  beutle^ hin  und  her^  (der  Sturm  das  Schiff);  "Eqsx&svg  ;der  Erderschütte^er^ WP.  II  362;  dazu  fkpos  ,Bär'  als  ^Schädiger'.
rem-,  rems-  ,ruhen,  sich  aufstützen;  stützen';   im   Germ.   ,Latte,  Leiste^? rom-ti  , Stütze';  Beziehung  zu  era-,  re-  ,ruhen'  (S.  338 f.)  ist  fraglich.
Ai.  rdmate  ,steht  still,  ruht,  findet  Gefallen,  pflegt  der  Liebe',  rdmati^' ramnäti,  rämayati  ,bringt  zum  stille  stehen,  macht  fest,  ergötzt' ;  aY.  ramya^ ,er  soll  ruhen',  rämöidwdm  ,ihr  möget  stehen  bleiben',  rämayeiti  ,beruhigt'/' osset.  urömun,  urömyn  ,zurückhalten,  hemmen,  beruhigen';  ai.  räma-  nj, ,Lust,  Freude',  rämd-  ,erfreuend,  lieblich,  reizend',  av.  räman-  n.  ,Ruhe,^ Friede',  npers.  räm  ,Ruhe;  fröhlich,  heiter';  ai.  rdnti  f.  ,Erquickun^ Ergötzung',  ramsu  Adv.  ,erfreulich';  rata-  , stehen  geblieben,  sich  genügen lassend,  sich  ergötzend',  rata-  n.  ,Liebeslust',  rdti-  f.  ,Rast,  Ruhe,  Lust';
mit  unklarem  rj:  gr.  '^qe^iay  -ag  , ruhig,  sanft,  leise',  '^QSj.iccLog  »ruhig', flQeixearsQog  Kompar.  (vgl.  den  es-St.  got.  rimis)]
air.  fo-rim-  ,setzen,  legen'  (ursprüngl.  *,stützen' ;  ri-  =  f-) ;  vielleicht mir.  rinde  ,Gefäß';
ahd.  rama  , Stütze,  Gestell,  Webe-  oder  Stickrahmen',  mnd.  ramty (=  mnd.  mhd.  reme),  ramen  ds.;  got.  rimis  n.  ,Ruhe';  aisl.  rgnd  f.  ,Rand, Saum,  Schild',  ags.  rand  m.  , Schildrand,  Schild',  ahd.  rant  m.  ,Rand/^ Einfassung,  Schild',  norw.  rande  und  ablaut.  rinde  , Erdrücken,  Bank', krimgot.  rintsch  ,mons',  span.  (*got.)  randa  ,Leiste';  norw.  rand  f.  ,Quer- balken,  Sims',  nhd.  bair.  ranten  , Stange'  (:  lit.  ramtiSj  ramstis  ,Stütze,  Ge- länder'); ahd.  ramft  ,Rand,  Einfassung'  kann  *rom-ti-  sein,  aber  allenfalls auch  auf  der  Erw.  rem-hh-  beruhen,  vgl.  ai.  rambhd-  m.  ,Stab,  Stütze', norw.  rimhj  rimme  ,Erdrücken',  lit.  rambüs  , träge',  rembeti  ,träge  sein; nicht  recht  wachsen  wollen';
aisl.  rim  f.  ,langes,  dünnes  Brett',  engl.  dial.  rim  ,Leitersprosse',  ostfries. rim  ,Dachsparren';  ags.  rima  ,Rand,  Grenze,  Küste'  (engl,  rim),  aisl.  rimi m.  , Landrücken';  vielleicht  durch  Kreuzung  mit  einer  Wz.  rei-,  deren Erweiterungen  in  reid-  und  reik-  vorliegen  (Wissmann);
lit.  remiü,  reihti  , stützen',  Inchoativ  rimsti,  rimti  , ruhig  werden',  Kausat. raminti  und  rdmdau,  -yti  ,beruhigen',  ramtis  ,Stütze',  rämas  ,Ruhe',  ramüi ,ruhig',  römiis  ,ruhig,  sanftmütig',  lett.  räms  ,zahm,  still,  fromm';
toch.  AB  räm-,  B  ram-  , sich  neigen,  beugen'.
WP.  11  371  f.,  Trautmaun  243  f.
remb-,  romh-,  roznh-  ,hacken,  kerben,  Kanten  machen'.
Mhd.  rumph,  nhd.  Rumpf,   isl.  rumpr  ,Steiß',   md.  mnd.  rump  ,Rumpf'
865.
W   /#  ;ib gehacktes  Stück^);   ob   zu  lit.   ruiiihas  ,Narbe^,  rumbüoti  ^umsäumen' (*r  tnho-),  ablaut.  rembeti  ^Narben  bekommen',  lett.  riiohs  ,Kerbe'  (*rombo-), l^yr.  '^rgh^  m.  in   serb.  riib   ,Saum',   slov.  rgb  ^Kante,   Saum',  slov.   rgbiti hacken,  einsäumen',  Öech.  roubiti  ds.  usw.? '  \vP.  11  ^'73;  Trautmann  236,  Vasmer  2,  541  f.
fcndh'  ,(zer) reißen'.^
^i.  rdndhram  , Öffnung,  Spalt,  Höhle';  ags.  rendan  , zerreißen',  mnd. rende  , Zerbrochenes';  ahd.  rlnda,  rinta,  nhd.  Rinde,  ags.  rind{e)  f.  ,Rinde, Kruste*",  ablaut.  mnl.  hess.  runde  f.  , Wundschorf.
WF.  II  372,  374.
rent-  ,Sache'?
Unter  dieser  Wurzel  könnten  vereinigt  werden :
ai.  rdtnam  ,Habe,  Besitz,  Gut'  (*?:n<ttd-)  und  ir.  rit  ,Sache'  (*r7}tu-  oder *rentu-)]  auch  lett.  ruotigs  ,mit  allem  versehen'  (falls  aus  *ront-). WP.  II  374.
rep-  ,an  sich  reißen,  raffen'.
Ai.  vermutlich  rdpas-  n.  , Gebrechen,  körperlicher  Schaden,  Verletzung', raphitd-  , elend  (beschädigt)';  gr.  igsTiTO^ai,  , rupfe,  reiße  ab,  fresse',  äQTtvia (Asper  nach  dem  unverwandten  ligm],  ägridCa)^  worüber  s.  *ser-,  serp- , Sichel'),  dgsTtvia  ,Harpye',  hom.  ägrcvLai  dv-r^geipavzo  (Hs.  ävjjgsixpavTo) ', alb.  rjep  , ziehe  aus,  ab,  beraube';  lat.  rapiö,  -ere  ,raffen,  an  sich  reißen, hastig  ergreifen,  rauben'  (a  =  ^]  mir.  recht  ,Zorn,  Wut'  (*reptu-)j  s.  auch rabh-]  germ.  "^rafisjan  ursprüngl.  »körperlich '  strafen'  (Denominativ  eines -es-St.  wie  ai.  rdpas-)]  aisl.  refsa^  ahd.  refsen  ,züchtigen,  strafen',  as.  respian ds.,  ags.  refsanj  repsan,  respan  ,tadeln',  woneben  *rafjan  in  mhd.  reßen =  refsen,  vgl.  mit  Dehnstufe  ags.  gerö&f  n.  (?)  =  geresp  , Anklage,  Tadel';
aisl.  o^afr  ,Streifen  Heilbuttenfleisch',  rejill , Streifen,  Stück  eines  Gewebes' (,abgerissenes'),  ndl.  rafel  , Faser,  ausgezupfter  Faden',  rafelen  ,ausfasern';
lit.  ap-r^pti  , fassen,  ergreifen,  begreifen',  lit.  repUs  (apr.  raples)  f.  PL ,Zange'.
WP.  II  369  f.,  WH.  II  417,  Trautmann  244.
I.  rep-  (rep-?)  ,kriechen,  schleichen'.
```


## [2026-09-14T01:22:12.527Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN leaf 679 (p1335)\"; awk 'BEGIN{RS=\"\\f\"} NR==680' KLN_1966.txt | grep -n -i -A6 \"^rest\\|rest,\\|rasta\" | head -60\necho \"### KLN grep rest n.\"; grep -n \"OHG\\. rasta\\|rasta,\" KLN_1966.txt | head -20",
 "description": "Check Klein p.1335 rest"
}
```


### [2026-09-14T01:22:13.843Z] TOOL RESULT

```
### KLN leaf 679 (p1335)
23:Derivative:  purl-er,  n.,  a  throw,  spill, purlieu,  n.,  part  of  a  forest,  separated  from  it  after the  perambulation  of  its  boundaries  (Hist,  of Law).  —  ME.  purlewe,  fr.  AF.  puralee,  ‘peram¬ bulation’,  fr.  OF.  puraler,  ‘to  go  through,  per¬ ambulate’,  fr.  pur-  (see  pur-)  and  aler,  ‘to  go'. See  alley.  Purlieu  was  influenced  in  form  by  OF. (=  F.)  lieu,  ‘place’  (see  lieu). purlin,  n.,  a  timber  resting  on  the  principal  rafter and  supporting  the  common  rafters.  —  Of  un¬ certain  origin.
24-purloin,  tr.  v.,  to  filch.  —  ME.  purloinen,  fr.  AF. purloigner,  fr.  OF.  porloignier,  porloigner,  ‘to prolong;  to  retard,  delay’,  fr.  Late  L.  prolon- gare,  ‘to  lengthen,  prolong’.  See  prolong, purple,  n.  —  ME.  pur  pel,  pur  pul,  dissimilated  fr. purpre,  pur  per,  fr.  OE  .pur pure,  fr.  L.  purpura,  fr. Gk.  7top(pupoc,  ‘purple  fish,  purple  dye,  purple’, which  is  of  uncertain  origin.  Cp.  porphyry,  pur- pure.
25-Derivatives:  purple,  adj.  and  tr.  and  intr.  v., purpl-ish,  adj.  and  n.,  purpl-ish-ness,  n.,  purpl-y, adj.
26-purport,  n.,  bearing,  tenor,  meaning,  intention, import.  —  ME.,  fr.  AF.,  fr.  OF.  purport,  'con¬ tents,  tenor’,  back  formation  fr.  purporter,  ‘to contain’,  fr.  pur-  (see  pur-)  and  porter,  ‘to  carry’. See  port,  ‘to  carry’.
27-purport,  tr.  v.,  to  convey  the  meaning  or  intention of.  —  AF.  purporter,  fr.  OF.  See  purport,  n. purpose,  n.  —  ME.  porpos,  purpos,  fr.  OF.  porpos, purpos  (F.  propos),  fr.  porposer,  purposer,  'to propose’.  See  purpose,  v. purpose,  intr.  and  tr.  v.  —  ME.  purposen,  fr.  OF. porposer,  purposer,  ‘to  propose’,  collateral  forms of  proposer.  See  propose,  which  is  a  doublet  of purpose.
28-Derivatives:  purpos-ed,  adj.,  purpose-ful,  adj., purpose-ful-ly,  adv. ,  purpose-ful-ness,  n., purpose¬ less,  adj.,  purpose-less-ly,  adv.,  purpose-less- ness,  n.,  purpose-ly,  adv.,  purpos-ive,  adj.,  pur- pos-ive-ly,  adv.,  purpos-ive-ness,  n. purprcsture,  n.,  appropriation  of  another's  land (law).  —  ME.,  fr.  OF.  p(o)urpresture,  alteration of  p(o)urpresure,  p(o)urprisure,  fr.  p(o)urprise, prop.  fern.  pp.  of  p(o)urprendre,  'to  take  to  the detriment  of  another’,  fr.  p(o)ur-  (see  pur-)  and prendre,  fr.  L.  prendere,  ‘take’.  See  prehensile and  cp.  prize,  ‘the  act  of  seizing'.  For  the  ending see  suff.  -ure.
29-purpura,  n.,  a  disease  characterized  by  purple patches  on  the  skin  ( med .)  —  L.,  ‘purple  dye’.
### KLN grep rest n.
27833:—  Fr.  L.  pes,  gen.  pedis,  ‘foot’.  See  pedal,  adj. pederast,  paederast,  n.  —  L.  paederasta,  fr.  Gk.
32546:rest,  n.,  repose,  quiet.  —  ME.  reste,  fr.  OE.  rest, rsest,  ‘rest,  resting-place;  bed,  grave’,  rel.  to  OS. rasta,  ‘resting-place,  grave’,  ON.  rost,  ‘distance.
32547:journey,  mile’,  Goth,  rasta,  ‘mile-,  OHG.  rasta, MHG.  raste,  rust,  G.  Rust,  ‘rest,  peace’,  fr. Teut.  base  *ras-,  ‘to  rest,  remain,  dwell’,  whence also  Goth,  razn,  ON.  rann,  ‘house’,  OE.  rsesn, ‘plank;  ceiling’,  sern,  ‘house’;  fr.  I.-E.  base  *ere-, *re,  ‘to  rest’,  whence  also  OE.  row,  ON.  rd, MDu.  roe,  OHG.  ruowa  (MHG.  ruowe,  rowe, G.  Ruhe),  ‘rest’,  Avestic  airime,  ‘quietly’,  Gk. epo yr],  ‘rest’,  epcociv,  ‘to  draw  back  from,  rest from’,  W.  araf,  ‘quiet,  mild,  slow’.  Cp.  the  first element  in  ransack  and  the  second  element  in barn  and  in  saltern.
```


## [2026-09-14T01:22:14.150Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KNT leaf 221 (p206)\"; awk 'BEGIN{RS=\"\\f\"} NR==222' KNT.txt | head -50\necho \"### KNT grep ram\"; grep -n \"^ram\\b\\|ram-\\|rāma\\|ramnā\" KNT.txt | head -20",
 "description": "Check Kent p.206"
}
```


### [2026-09-14T01:22:15.377Z] TOOL RESULT

```
### KNT leaf 221 (p206)
r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II); see also hamapilar-. pita пет. ($86.П, $124.5, $186.1T) DB 1.4 bis, 5 bis, 6; 2.93; DBa 5, 6, 6f, 7, 8; DSf 12, 58; XPa 15; ХРе 12; XPf 16, 17, 19, 23, 31, 33, 42; XPg 7; X8a 2; XV 18; А!Ра 20f; D?Sb 4°. pica gsm. ($78, $124.5, $186.If) XPa 20; ХРе 14; XPf 35, 38, 47.
Pirdva- sb. ‘Nile’ (§75.V, $124.II, §166.V]): Pirdva пзш. DZc 9, in naming phrase, anacolu- thic for abl. after Ласа; either ‘Ivory River’, as deriv. adj. to piru- ‘ivory’, or possibly plural ‘The Tusks’ (JAOS 51.209).
miru- sb. ‘ivory’ (§75.V, 5153.1): Elam. pi- ru-§, Akk. pilu-, with cognates (or borrowings) in Eastern Asiatic languages (Przyluski, BSLP
197
27.3.220-2; Scheil, Rev. d’Assyr. 24.120; Bv. BSLP 30.1.62; König, Burgbau 66; Hz. AMI 3.67-8).  piruf пет. DSf 48.
pi-, vb., see paid-.
pisa- sb. ‘raft’: perhaps originally ‘cut mate- rial’, from root pazd- (8143.1II). різ ism. or isn., with collective meaning (§255), DB 5.24.
pisa- or paisa-, vb. stem, see paið-.
Putéya- adj. ‘man of Put, Libyan’ (§75.V, $/6.V, §144.HI); pl., ‘Libya’, a province of the Persian Empire (Cameron, JN ES 2.308-9) : Elam. pu-á-ti-ja-ap, Akk. pu-u-ta (Lg. 18.299, 15.165). Pulüya пет. A?P 27. Putāyā npm. DNa 29f; DSe 29°; XPh 28,
puça- sb. ‘son’: Av. puéra-, Ars. РЬ. рим, N Pers. pus, Skt. pulrá-, Ose. puclo-, рї *putlo- ($64, §75.1,§78,§148.1II). pucansm. AmH 3; AsH 4; CMb 2°; DB 1.8, 28, 39, 53, 74, 78, 79; 2.9; 3.25, 79, 81; 4.9, 14, 28, 30, 83, 84° bis, 85 bis, 86; DBa 3; DBb 6; DBd 6; DBh 7; DBi 8f; DPa 5; DPb; DPe 5; DPh 2; DNa 18, 14; DSa 2; DSb 10; DSe; DSd 2; DSe 12, 13; DSf 7; DSg 2°; DSi 2°; DS} 2°; DSk 3; DSm 2°; DSy 3; DZb 5f; DZec 6; DE 20; DH 2; XPa 10; XPb 20; XPe 9; XPd 14; XPe 4; XPf 14; XPh 11, 12; XPj; XPk; Х5е 2; XE 20; XV 15; A!Pa 15f; АЧ bis; D'Sb 2°; Аба 1, 2 bis, 3 bis; Ab; A?Sc 0° bis; А4 2; A?Ha 2°, 8, 3°, 4, 4°; А?Не 10, 11, 12, 13f, 15; A3Pa 18, 14, 15, 16, 18, 19, 20; Wa 7; Wb 8; We 9; Wd 9; Sa 8°, pucä npm. XPf 28; as nsm. А?НЬ (853; with -a after парӣ, acc. to Brd. WZKM 39.92).
farnah- sb., see Vidafarnah-.
fra- prefix ‘before, forth’ (as prep., not found in OP): Av. fra, Skt. pra, Gk. тро, Lt. prü-fessus, Gt. fra-, pIE *pro ($33, $01, $75.II, $106, $132.3). Found with verbs а1$-, jan-, nay-, var-, má-, sá-, haj-; in nouns framdtar-, framānä-, Fravarti-; in phrasal adv. fraharavam; with suffixes and exten- sions, in fratama-, fratara-, fratara-, fravata, fraxa-.
fratama- adj. ‘foremost’: fra- + superl. suf- fix -lama-, Av. fratama-, Skt. -tama- (4190.11). fratama npm. DB 1.57; 2.77; 3.48f, 51, 74, 90°, 91.
fratara- ad). ‘prior, further’: fra- + comp. suf- fix -tara-, Av. fratara-, Skt. adv. pratardm, Gk. mpotepos (§106, 5190.11). " fratara ism. DNb 38 (Sen 249 needlessly takes as error» for frataram).
198
frataram asn. XPg 11; adv. ‘previously’ DB 3.26, A!Pa 21.
fratarta DB 3.26, incorrect reading for fra- taram (Cameron).
fral- vb. ‘ask, examine, investigate, punish’: Av. fras-, Skt. pra-, Lt. precor, pIE *prek-, with inchoative present, *prk-ske-, OP parsa-, Av. poro- saiti, NPers. pursdd, Skt. precháti, Lt. poscit. Cf. also ufrasta- ufrasta-. parsdémiy 1st sg. (830, $97, $130, $212, 5226.1) ОМ 19. aparsam Ist sg. imf. ($122, 5182.3, $212. $226.П) DB 1.22; 4.67, parsü 2d sg. imv. (8212, 5237.1) DB 4.38, 69. . frabiyaiš opt. pass. ($220, $228.П, $228.11) DNb 21 (not desid. fut. pass., as taken by Hz. Арі 167). pati- + parsa- ‘examine, read’ (on meaning, Bv. DSLP 31.2.71-2): patiparsühy 2d sg. subj. (§222.- II, $227.I) DB 442.  patiparsátiy subj. ($222.11) DB 4.48.
frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl. -thama- in Skt. prathamd- ‘first’. Cf. also uradara
### KNT grep ram
58:In matters of etymology it has seemed desir- able to give a goodly representation to cognates outside the Indo-Iranian; not all those interested in Old Persian are primarily specialists in Aves- tan and Sanskrit. For greater clarity, stems of nouns and adjectives ending in -7- and -u- have been cited with -i- and -w-, rather than with the strong grade -ay- and -av- customary among Iranists; but verbs of OP and Avestan are cited in the strong grade, though Sanskrit verbal roots are cited in the form fixed by the Hindu gram- marians and customary among Sanskritists. The English translations of words and passages in the Grammar, especially in the Chapter on Syntax, frequently vary from the translations which accompany the texts in Part ЇЇ; this vari- ation is intentional, to bring out more clearly the point for which the word or passage is being cited.
722:ciydkarammeciy® DNb 51, 511, for -cmeüp, = ciyükaram-ca-mauy.
1379:enclitics: kamnam, jiyamnam, acc. nākam, adam- : q | kim, avakaram-ca-maiy, parwam-ciy. On [n*yà]- ; kama = |kam-ma, see $130. On pIE m, see $67; ^
1556:§125. Guna AND Увррні: The Hindu gram- marians recognized a variation of vowels within the same root or formative element. The vowels which they recognized in their system of roots were taken by them as the fundamental vowels; prefixation of d gave to each the guna-form (Skt. guna); lengthening of the guna-form gave the vriddhi-form (Skt. erddhz ‘growth’). But ‘dé was its own guna’; that is, й unchanged was also the guna of d. Thus they got the following cor- respondences; note that to the Hindu gram- marians the e and o were diphthongs ai and au (as they really were!).
1640:karam-ca-maiy DNb 27f; ciyakaram-ca-mary
1647:5135. Tux - BEFORE ENCLITIC normally re- verts to its true value, and the indication of length disappears: thus manā but mana-cà; avükaram-ca-maiy; avahya-
1672:I. Doubled consonants are written single: apis + Sim = dpisim DB 1.95f; taumaniš + Saiy = taumantSaiy DNb 25f; -kam + тату in {n*ya|kama A’Sa 4. In DNb 511 ciyakaram*m"cy is twice written for -m’c'my*, = ciyakaram-ca-maty.
2769:may be used as predicate to any subject:! DB 2.18f кага Parsa шй Майа hya ира mam аһа haw kamnam dha ‘the Persian and Median army which was with me—this was a small thing’; во also DB 1.47 uvaipa saam (referring to Parsam utà Madam ша aniyà dahyàva), DNa 39 ctyakaram aha ava dahyava, DNb 6f avakaram amiy, ОХЬ 27f avā- karam-ca-maiy usiy wa framand, DNb 50 ciyükaram amiy ciyükaram-ca-maiy tonaré. A neu- ter subject may have a masculine substantive as predicate: DNb 11f tya rdstam ava тат kama ‘what is right, that is my desire’.
3079:DNb 271 avükaram-ca-may; DNb 51, 51f ciyá- karam-ca-maty.
3550:$ Ariyãram- KT, both occurrences; not -rdm-, with RI. 1 [ота KT, cf. ота DBa 11 KT; not adaià with Andreas and Hüsing KZ 38.255. *VITI : manā : taumaya: ef, Hist. App. I. © duvilàparanam, sce Lex. “ On list of provinces, see Kent, JNES 2.302-6. 5 Yauna Bv. Gr. 6348; not ушпа] = Уат], with KT, cf. Ri.’s ашпа]. 1 [Sugluda. KT. © јот" RI., KT; instead of the expected fersherueme, ? agr"H--] KT, ef. Ri.’s аё; ортеу“ Cameron; see Lex. s.v. agriya-. ? tyanā : mand : dálà of RI. and KT is correct; not dittography for tyà : mand, cf. the idiom in XPh 49 and 51-2. 2 араттуйуа, from pari- + ay-; for wrong interpretations, see Lex. u-s Auramazda | miaiy :| ima KT. ** habnalddrayat{y] KT. ?hauvam KT. *avajata RL, KT; not to be emended to avdjate, with Gray, Bthl. # On Gaumata-Bardiya, sce Hist. App. П. * On the OP calendar, see Hist. App. IV.
4279:м tyä Konig, Burgbau 29; іта Hz. AMI 3.34; but the traces are very faint and indecisive, cf. Kent, JAOS 58.8. 2 Retranslation of Elam. version by Hinz, JNES 9.1-7, because of Elam. d-ga-ra-um-mi, transliteration of OP ucdramaiy = ucüram-maiy; the АКК. version is here, as often, quite different. # The Akk. does not war- rant ava with visam; in this phrase, ava always precedes, but the OP has no gap at that point. ? frásah[ya] (pas- rive) is probably better than my jfrüsaha[m| (active), JAOS 53.13. daruva Scheil 21.18, etc., is a better reading than sdruva, Hz. ApI 299; but normalize daruv, with Duchesne-Guilleman (d* certain, according to Duchesne- Guillemin, who inspected the original tablet at the Louvre in 1948) ; for meaning and normalization, see Lex. s.v. däruv. % [реча Bv. BSLP 30.1.62-3; [0:44 Hz.
5053:Ariydramna- sb. ‘Ariaramnes’, great-grand- father of Darius: Elam. har-ri-ia-ra-wm-na, АКК. ar-ja-ra-am-na-', Gk. 'Ариараштѕ. From ariya- + pass. pte. of d-ram- (8131; Av. Skt. ram- ‘to be at peace, to pacify’): ‘Having the Aryans at peace’ (8161.]1c). Hardly Ariyà pl. + ramna- (Foy, KZ 35.9), or Ariya- + aramna- pres. pte. mid. to ar- (Hz. Ар! 287). Anydramna nsm. AmH 1, 4, 9; DB 1.5; DBa 7; as gsm. AsH 3 ($313.1). Ariydramnahyé gsm. DB 1.5; DBa 7.
5095:avdkara- adj. ‘of such sort’: avd ‘thus’ + kara- ‘doer’ (§160.Ia; wrongly Hz. ApI 101-3, who takes -kara- in avükara- and ciyükara- not from kar- ‘do’, but as kara- ‘time’, as in hakaram, q.v.). avakaram nsn. (6259) DNb 6; avdkaram-ca-mary ($109, $133, $135) DNb 2f.
5162:‘good deed’: from u- + cãra-, to root kar- ‘do’ / (809, §122, §123.3), cf. LAv. dard- Hilfsmittel" NPers. батё (Ву. BSLP 30.1.65-6, Gr. $292; cf. Bthl. AiW 584); but Wb. AfOF 7.39-40, Hz. ApI 193-8, take from Ar. car- ‘move’ (Av. éaraitt, Skt. cárati; but Skt. has only sucürá as a woman's name!) ucüramnsn. DS} 4^; DSI 5. ucüram asn. DB 4.76; ucdramaiy DSf 20° (= ucéram-maty, $138.T).
5384:-ciy encl. particle, emphasizing or generaliz- ing, nsn. or asn. of с1-: Ау, -Git, Skt. eid, СК. т, Tat. quid, pIE *q*id (840, §84, $113, 5191.11, §201, 6998.11). In the following combinations: aciy (q.v.) ХРЇ 21. aniyaš-ciy nsn. DB 4.46; XPa 13; aniya&-c (452.1) XPh 41f; aniyai-ciy npm. XPf 29. avas-ccy nsn. DNb 55; asn. DNb 53f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. |
5395:ciyăkara- (§53) adj. ‘how great’; nt. аз sb., ‘how great a thing’: *ciya(n)t-, cf. Skt. kiyat nsn. ‘how much, how many’, + kara- to root kar- ‘make’ ($160.19; Bthl. AiW 597; hardly to kara- ‘time’, cf. hakaram, as taken by MB Gr $293, Hz. ApI 101-3). ciyakaram nsn. (§259) DNa 39; ciyükaram DNb 50; ciyakaram-ca-maiy (written — : -"m*m*eur; $41, $51, $132, $138.I; Lg. 15.178, — | against Hz. ApI 240) DNb 51, 51f. 1
5859:ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v.
```


## [2026-09-14T01:22:30.437Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef leafof(path, lineno):\n    txt=open(path,encoding='utf-8',errors='replace').read()\n    lines=txt.split('\\n')\n    pre='\\n'.join(lines[:lineno])\n    return pre.count('\\f')\nprint('KNT ram- leaf', leafof('KNT.txt',5859))\nprint('KLN rest leaf', leafof('KLN_1966.txt',32546))\nEOF",
 "description": "Compute leaf numbers"
}
```


### [2026-09-14T01:22:31.655Z] TOOL RESULT

```
KNT ram- leaf 230
KLN rest leaf 710
```


## [2026-09-14T01:22:32.229Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### HRN grep rasan/rismân\"; grep -n \"rasan\\|rismân\\|rīsmān\\|risman\" HRN.txt | head -20\necho \"### HRN leaf 158 (p137)\"; awk 'BEGIN{RS=\"\\f\"} NR==159' HRN.txt | head -40",
 "description": "Horn rasan"
}
```


### [2026-09-14T01:22:33.322Z] TOOL RESULT

```
### HRN grep rasan/rismân
4334:aw. ^hurasant-; phlv. /ursand 'zufrieden, fröhlich*
4554:Vers 693), Xurasan,
5491:apa\rasan zügellos*, erasan, erasanak 'Zügel' (Hübsch-
5493:arab. hebr. LW. rasan, bezw. JD^.
7128:818. ferseng 'Parasange', arab. LW. farsax»
7129:ap. 7Taf)f((r(iyy7j; phl. frasang bezw. farsany (Men.,
14322:l/'r««-, arasant 6 16.
22217:erasan 615.
22218:erasanak 615.
### HRN leaf 158 (p137)
- 137 —
Pärsenhandschrift 68, 10), röd(i)sn bezw. röy(i)sn; ai.
rödli' rodliati (KröA-, röltati).
bei. rtiday, n. ruday (319).
Zur i/^rödfi- vergl. Bartliolomae, ZDMG. 44, 553
No. 332.
615. resen 'Strick'.
ai. ragandr 'Strick, Riemen, Zügel, Gurt'; arm. LW.
apa\rasan zügellos*, erasan, erasanak 'Zügel' (Hübsch-
mann, No. 96).
arab. hebr. LW. rasan, bezw. JD^.
616. restden 'ankommen, erreichen', Praes. res-em^
resänTden,
g. rasadmün.
ap. i/^ras' 'kommen, gelangen', arusam^); phlv.
rasltan, ras(i)§n (AV.), rasmitan,
LW. afy. rasedal; bei. rasa(/ (313).
617. risten 'spinnen, Praes. res-efn, riste, resulen, resmän,
rismän, vergl. ebresum (No. 65).
g. risbün *Zwirn .
ai. i/^reg-, rigäte 'rupfen, abreissen.
bei. resag^ n. resay 'spinnen, flechten' (318), üresarj
'spinnen' (40) ; oss. alunjssin, d. alwiessun (bei Geiger).
resk s. eresk (No. 71).
618. risk 'Lauseei, Nisse' (AM. 141 Zeile 11, 191 Zeile 7).
ai. liksd' 'Ei einer Laus, Nisse' (Nöldeke bei
Hübschmann, Oss. Etym., S. 46).
kurd. LW. risk ; af/. riya ; bei. LW. rask, risk 'Läuse'
(217); oss. t. llsk, d. liskä 'Nisse' (170).
619. reften 'gehen, weggehen', Praes. rew-em, reftar, retvä
(arab. LW. rawäj), rewän, rewäne, retvis'^),
aw. y^rap' 'gehen' in rap<ö-.(?)3); phlv. raftafi, rapet^
rawad (3. Sing., geschr. ra/d)^ rawäk, räwäkth^
Aw. rasaintl' (y. 52, 1, 3) gehört nicht hierher nach liartho-
lomae, Indog. Forsch. II, 264.
*) BeilAufig bemerkt, ist die Aussprache rös in dem bei Vullers
aus Bh. 8. V. citirten öahnämeverse falscl^; derselbe steht I, 8 Vers 131.
') Yd. 13, 45. Aber ganz annoher.
```


## [2026-09-14T01:22:43.071Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### HRN leaf 26 (p5)\"; awk 'BEGIN{RS=\"\\f\"} NR==27' HRN.txt | head -45",
 "description": "Horn p.5 aram"
}
```


### [2026-09-14T01:22:44.119Z] TOOL RESULT

```
### HRN leaf 26 (p5)
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


## [2026-09-14T01:22:44.648Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SNS grep rasan\"; grep -n \"rasan\\|rsn\" SNS_pages.txt | head -30\necho \"### SYN leaf 865 (p841)\"; awk 'BEGIN{RS=\"\\f\"} NR==866' SYN.txt | head -40",
 "description": "SNS rasan and Buck p841"
}
```


### [2026-09-14T01:22:45.636Z] TOOL RESULT

```
### SNS grep rasan
1566:      aiwizav5yeiti:>j 9 (oj*) savayat- aivi+ /"sav-: t-                                                                    x v anira0           jo^Mtfj :vGuru-barsn                           '0**-j*»; jarasn
5556:                                          ,^j» <i&«> rfrasang:       3V->^0                                                                                   1       *A>>C>tV/?1 iS
5560:                                     U/T^ •(&&*) frasang :^                   |
5954:                                                  (AiWb.   894) pzrsna-            :     *-
9047:IH       137) ra ff ax*-    :   *•*** -oWo^rasan: VP&                                           .T»-u-, r^/A^-u^i.
13069:                                                                                                                 n«/Y^Ut^.l381) ursnay- ^jui. varsril-  :                                     :    £-
13175:                                                                                                                                                                              ^   «*^-j*:gursnag:                    ,\
14954:                                                     ursnay- 334/5                     gurav- 319/3
15142:                                                                   raoxsna- 231/12              varsnt- 334/5
15896:pSlapd&n 139/16            radtar 222/2                      rasan 227/3            rfizisn 233/12
16166:gursnag 336/8
16300:                                                         fraz 136/4-8                frasang 129/1
### SYN leaf 865 (p841)
ecom- a Prob. also Ir. -tal in Bes (11.78), taile gl. salari- be worth, reward’, t Lollere ig pane! (Stokes, 130 : 5 19, te. ; rejected by Walde-
T. paeq witha hor) Wildan ‘repay’) oe epds. fragildan, SN gjalda, OF gieldan,
Digitized by Arya Samaj Foundation Chennai and eGangotri
sgION, PROPERTY, COMMERCE 797
dgieldan, ME yelde, OHG geltan, MHG gelten, beside Goth. gild, gilstr ‘tribute, tax’, OHG gelt ‘payment, recompense, money’, NHG geld ‘money’, etc., out- side connections dub. Walde-P. 1.632. Feist 161. NED s.v. yteld vb.
MLG betalen (> Dan. betale, Sw. be- tala), Du. betalen, NHG (be)zahlen (MHG bezaln rarely ‘pay’, mostly = zaln ‘count, calculate, relate’, OHG zalon ‘count’), fr. the sbs. LG tal, OHG zala ‘number, series’, NHG zahl ‘num- ber’; hence ‘pay’ fr. ‘count out’. Falk- Torp 64, 1243. Paul, Deutsches Wtb. s.v. zahl.
ME paie, NE pay, fr. Fr. payer (above, 2).
5. Lith. mokéti ‘understand, know how’ (‘can’ in this sense, as ‘can read’) and ‘pay’ (ué- only in this sense) : mokti ‘learn’, Lett. maku, mdacét ‘under- stand, be able’, mdcit ‘teach’, OPruss. mukint ‘teach’. Miihl.-Endz. 2.575. Semantic development prob. ‘know how’ (to count), ‘count out’ > ‘pay’ (cf. NHG zahlen, above).
Lett. maksat, fr. maksa ‘payment’ (Esth. or Liv. maks id.). Mithl.-Endz. 2.555.
6. ChSI. vtizdati ‘give back’ (11.22), in Gospels reg. for drodiéwyxe also when it means ‘pay, repay’.
SCr. platiti, etc., general Slavic (but not in old ChSl.), deriv. of word for linen (ChSI. platti, platino, 6.23). Ac- cording to the chronicle of Helmold the Slavs used linen cloth as the standard of value in trade. Briickner 420. Schrader, Reallex. 1.325.
7. Skt. da- ‘give’ (11.21) also the usual word for ‘pay’.
Av. éi- ‘atone for’ and so ‘pay’ (e.g. Gikayat Vd. 13.10; cf. Barth. 108 s.v. afga- and 464) : Grk. zivw ‘atone for’, etc. (above, 1).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
798 SELECTED INDO-EUROPEAN SYNONYMS
11.66 ACCOUNT, RECKONING
Grk. Adyos, Aoyiopds Goth. rapjo Lith. Saskaila NG Noyaptacpés ON tal, tala, reikningr Lett. rek'ins, rtk'indSang Lat. ratio Dan. — regnskab, regning ChSl.  (slovo) It. conto Sw.  rdkning SCr. . ratun Fr. comple OE _ gerad, riht Boh.  uéet Sp. cuenta ME (a)count, re(c)k(t)n- Pol. rachunek Rum.  socoteald, cont ing Russ.  séet Tr. airem, comairem ' NE account, reckoning Skt. ganana- NIr.  comhaireamh, cunn- Du. rekening Ay.
tas OHG reda W. cyfrif MHG rech(e)nunge
Br. kont NHG  rechnung
Some of the words for ‘account’ are related to those for ‘number’ or ‘count’, while others are based on a more general notion of ‘reason, right’ or the like.
1. Grk. Adyos (
```


## [2026-09-14T01:22:57.036Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9040,9052p' SNS_pages.txt\necho \"---- pdf page tags near\"; grep -n \"\\[pdf page\" SNS_pages.txt | awk -F: '$1>8900 && $1<9100' | head",
 "description": "SNS rasan entry context"
}
```


## [2026-09-14T01:22:58.204Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"REST\\b\\|4\\.6[0-9] \\|QUIET\\|CALM\" SYN.txt | head -30",
 "description": "Find Buck REST section"
}
```


### [2026-09-14T01:22:58.267Z] TOOL RESULT

```
                                                             p- 168.
                                                                                                                    •rT/ia«5    ai^ :abar ravsnd:                  3<t>i          ^
                        .tA/Vt^     (Xofcual 5n5.                                                                                            *




IH       137) ra ff ax*-    :   *•*** -oWo^rasan: VP&                                           .T»-u-, r^/A^-u^i.
                                                                                                                                Umvt&v-tafa*. ra tu-.fa.

                                                                                          V
                                                                                                              .rr-.rr-.n-u/ir* •,***««•
                                                                                                                                                            .**'tr«diiii          ^
---- pdf page tags near
```


### [2026-09-14T01:22:58.321Z] TOOL RESULT

```
1487:141 WOODS, FOREST
6908:4.61 SLEEP (vb.; sb.)
6935:4.62 DREAM (sb.)
6955:4.63 WAKE (a, trans., b, intr.)
6995:4.64 BREAK WIND, FART (vb.)
7029:4.65 URINATE; URINE
7052:pARTS OF 4.66 VOID EXCREMENT; EXCREMENT, DUNG taae ee Goth. . ; maihstus, Lith.  Sikti; $udas, méSlas k KaKKaO, xe} Noe smarna Lett. dirst; stids, mésls
7135:4.67 HAVE SEXUAL INTERCOURSE
18728:11.66 AccouNnT, RECKONING 11.67 Security, SURETY 11.68 INTEREST
20338:11.68 INTEREST
21442:12.19 QUIET (adj.)
24305:14.53 14.61 14.62 14.63 14.64 14.65 14.66 14.67 14.68 14.71 14.72 14.78 14.74 14.75 14.76 14.77 14.78
25567:14.61 WEEK
25613:14.62 SUNDAY
25624:14.63 MONDAY
25628:14.64 TUESDAY
25630:14.65 WEDNESDAy
25641:TIME 1007 14.66 14.67 14.68 THURSDAY FRIDAY SATURDAY gapparov mopcanely oaBBarov Gr “co Acés tutpa "Agpodlrns jyutpa. Kpévov : wapacKkeun ‘ xo rT dies Veneris praia Iat. oe ‘nla feria a feria sabbatum easy venerdi 1 ele vendredi aan pr 4 viernes fi 1eves Lerne sdbado z ‘oui vinert simbdta HL quinta feira sexta Seira sabado Po dardain din diden satharn It dardaoin aoine satharn aM dydd iaw dydd gwener dydd sadwrn hr diziow digwener disadorn Goth “Se paraskaiwe, fruma sabbaté sabbato dags ON orsdagr Srjadagr laugardagr, pvattdagr Nicel. fimtudagur Séstudagur laugardagur Dan. forsdag fredag Igrdag Sy,  torsdag fredag lordag 0E  punresdeeg Srigedeg seter(n)dag ME thursday friday saterday NE thursday friday saturday Du.  dondersdag vrijdag zalerdag OHG donarestag Sriatag sambaztag, sunniinadband MHG donerstac, pfinztac vri(e)tac sameztac, sunnabent NHG donnerstag freitag samstag, sonnabend Lith. Ketvirtadienis (Getvergas) penktadienis (pétnycia) SeStadienis (subata) Lett. celurdiena piektdiena sestdiena a telurlttieis peliiki, pelinica sobota, sabota a ‘hey petak subota Pol, She Pe patek sobota Russ as e piqtek sobota : 9 pjatnica subbota
```


## [2026-09-14T01:23:05.052Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21430,21470p' SYN.txt",
 "description": "Buck 12.19 QUIET"
}
```


### [2026-09-14T01:23:05.201Z] TOOL RESULT

```
ON skilja eptir (and so reg. in NIcel.) with eptir ‘after, behind’ and skilja ‘di- vide, separate’ (12.23).
Sw. lémna (= Dan. levne ‘leave over’), with change to trans. sense : ON lifna, Goth. af-lifnan ‘be left’ (12.17). Hell- quist 607.
6. Lith. palikti, above, 1.
Lett. atstat, also intr. ‘separate from, give way, yield’ (cf. Lith. atstoti ‘step back, go away’), epd. of at- ‘back, again’ and stat ‘stand up’ (12.15).
7. ChSl., SCr. ostaviti, Russ. ostavit’, Boh. zéstaviti, Pol. zostawié, caus. for- mations to ChSl. ostati, etc. ‘remain, be left’? (12.16).
8. Skt. ¢is-, etym. dub. Uhlenbeck 310.
Skt. ric-, Av. (paiti-)rié-, above, 1.
Skt. ha- : Av. 2@- ‘release’, Grk. xijpos ‘bereft’, xjpa ‘widow’, x@pos ‘(empty) space, place’, etc. Walde-P. 1.543.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ee Digitized by Arya Samaj Foundation Chennai and eGangotri
i
840 SELECTED INDO-EUROPEAN SYNONYMS
12.19 QUIET (adj.)
Grk. —jovxos, Apenatos Goth. rimis (sb.) Lith. ramus
NG Hovxos ON ror Lett. kluss
Lat.  quiélus, tranguillus Dan. __rolig (stille) ChSl.  tichtt
It. tranquillo, quieto, Sw. stilla SCr.  miran, tih cheto OE row, stille Boh. _klidny, tichy, pokojns
Tr. tranquille ME quyet(e), stille Pol. spokojny, Gale, yin;
Sp. quieto, quedo, tran- NE quiet (still) Russ. spokojnyj, tichij quilo Du. rustig (stil) Skt. ¢@nta-
Rum.  linistit OHG ruowa, radwa (sbs.), Av. raman- (sb.)
I. sdim stilt
NIr.  suatmhneach, samh MHG ruowic, stille
W. lonydd, tawel NHG_ruhig (still)
Br. stoul
The words listed under ‘quiet’? may refer to the absence of rapid motion, exertion, noise, or any physical or mental disturbance. They differ somewhat in range and in dominant application. Thus in what is perhaps the most popu- lar use of NE quiet (e.g., be quiet! keep quiet!) reference to absence of noise is the dominant feeling, though not unmixed. But other uses are common enough, and the basic notion in the large group to which the word belongs, and in several of the others, is a ‘state of rest’. Occa- sional semantic sources are ‘even’ (through ‘calm’), ‘peaceful’, ‘silent’, ‘orderly’, ‘obedient’, ‘weary’.
For one or another of the applications other words may be used in much the same sense, as NE calm, still, peaceful, etc.
1. Grk. jovxos, yobxi0s, with sb. jouxla, etym. dub., perh. based on a *sé-lu- (> jov-), fr. the root *sé- in Goth. seipus, Lat. sérus ‘late’, Skt. sati- ‘conclusion, end’, etc. Walde-P. 2.461. Boisacq 330.
Grk. jpenatos, #peuos : Goth. rimis, etc. (below, 4).
2. Lat. quiétus (> It. quieto, cheto, Sp. quieto, quedo, OFr. quiete, ME, NE quiet), pple. of quiéscere, this fr, sb. quiés, -étis ‘quiet’ : OPers. Siyati-, Av. Saiti- ‘well being’, Av. Sydta-, 3ata- ‘hap- py’, ON hwvila ‘bed’, Goth. hweila, OF
hwil, etc. ‘time’ (NE while), ChS}. vb. po-citi, sb. po-koji ‘rest’, all based on a notion of ‘rest’. Here also Lat. tran- quillus (> It. tranquillo, etc.), epd. with trans, here in its intensive force (cf. the resulting Fr. trés, also NE thorough beside through, NHG durchaus), and lo- suffix. Walde-P. 1.510. Ernout-M. 840 f., 1052 (otherwise on the semantics of tranquillus).
Rum. linigtit, pple. of linisti ‘make quiet’, with sb. linise ‘quiet’, fr. lin ‘still, quiet’, this fr. Lat. lénis ‘mild’. Tiktin 914.
3. Ir. sdéim, NIr. sdémh, sdimhe, also NIr., Gael. samhach ‘quiet, calm, pleas- ant’, with sb. Ir. sém, NIr. samh ‘quiet, rest’, perh. through notion of ‘even- ness’ : Skt. sama-, Av. hama-, hdama- ‘equal, same’, OF som ‘agreement’, etc. Walde-P. 2.492. Stokes 290.
NIr. suaimhneach, with sb. suaimh- neas, etym.? Macbain 350.
W. Uonydd, through vb. lloni ‘glad- den’ fr. Ion ‘glad, cheerful’, with de- velopment of ‘quiet’ through ‘content- ed-’ (?).
W. tawel, fr. taw ‘silence’ (18.28).
Br. sioul, etym. dub. Henry 247. Ernault, Glossaire 381.
4. Goth. rimis (sb.; adj. not quot- able) : Lith. ramas ‘quiet’ (sb. obs.; now ramumas), adj. ramus ‘quiet , romus ‘gentle, mild’, rimti ‘be quiet.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
spaTI AL RELATIONS:
+ Skt. ram- ‘rest,
rans ids eh aie ‘rest, stay’ delight ae ere also (with pre- aman ee a ‘gently, quietly adj. ..) (rk. ia Br ccins ‘quiet, gentle’. P 2371 ff, Feist sae 76 sb 15 8D. 7 adj., Dan., 9W- *s
```


## [2026-09-14T01:23:20.683Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 grep خرم\"; grep -n \"خرم\" BQT_v2_pages.txt | head -10\necho \"=== BQT v2 grep رام\"; grep -n \"^رام\\|رام :\" BQT_v2_pages.txt | head -10\necho \"=== BQT v2 page tags\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3",
 "description": "Grep Borhan vol2"
}
```


### [2026-09-14T01:23:20.771Z] TOOL RESULT

```
=== BQT v2 grep خرم
416:‫پکاركده دخرمن رگوابند » و بعربی صبره‬              ‫ازآب‌نمابان شود‪ .‬طبیعت آن‌سرد وتراست وبعربی‬
1110:       ‫هزبر ژبان را پذیره شدند ‪ .‬فردوسی طوسی ‪.‬‬           ‫خرمودثان تا چپدره شدند‬
1160:    ‫اهل مغرب غور؟ خرما راکوبشد معتیخرمای‌سبز‬         ‫جم‌اول بروزز مباركء‬    ‫* جدار لك ۔‬
1193:                                                               ‫ایجد» مخز درخت خرماست وآلراپیه درخت‬
1195:                            ‫ج‬                                  ‫خرما کیوزبند ویعربی شحم‌النخله وقلب‌النخله‬
1651:‫خرم و شادان گردید و گفت ‪ « :‬این‌نورخداست‬
1963:       ‫و معرب کفری‌هم‌هست که پوست بهار خرمای‬
2290:‫خرما بافند و خرمادر آن کرده از جابی بجابی‬                                    ‫و بادام گوهی را نیز گفته اند ‪.‬‬
2293: ‫‪ -‬و ہمعنی درخت خرما هم بنظر آمده‌است ‪¥.‬‬
2326:  ‫«شرح قاموی»‪.‬‬        ‫بز رکه‌از نمروخرماست‪.‬‬          ‫کدوی‬    ‫‪۳‬‬        ‫جله ‪,‬ضم اول‬    ‫‪۹‬‬              ‫باشاهد)‪.‬‬   ‫‪(۰۶:۶‬‬
=== BQT v2 grep رام
=== BQT v2 page tags
```


## [2026-09-14T01:23:22.160Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA grep rasan\"; grep -n -i \"rasan\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== AFM grep رسن\"; grep -n \"رسن\" AFM_pages.txt | head -20",
 "description": "Asbaghi and Addi Shir rasan"
}
```


### [2026-09-14T01:23:22.234Z] TOOL RESULT

```
=== PLA grep rasan
687:>,>2\-                         ’abiward:                     eine         Stadt           im       Westen              v.    Marw;         in   der        Provinz           Khorasan
981:ul! _                          °’arsän:            Pl.               v.        rasan               a.     v.
984:Gyı-                       "arsan:             Pl.              v.           rasan             q,       v.
1410:a                  - ”isfaräyin:                   eine     Stadt       in Provinz       Chorasan         (iran.         Ostprovinz)-
2267:os           - badgais:                   Ein    Distrikt         in Khorasan                   2 aus     dem    pers.     e,L       bädhiz     3,
2582:cis-     baht:      "Kamel          aus     Khorasan"            6,
2618:du - bahti:                      nom.      un.     v. baht        "ein Kamel        aus Khorasan",
3892:       zabän-dari:                "Dialekt           v. Khorasan!.
4787: »L.s-         $aräbäd:                     ein Dorf          in der Nähe                        v. Marw        in Khurasan      7,
6160:        "Osten"                  ", mand.          kurasan             2,
6161:        Dtsch,           Khorasan:                 "der          in    der       Provinz           Khorasan            (Nordostiran)           geknüpfter
7747:rasan                                                                       136                                                          raff
7750:ow-      rasan:           "Strick"              aus    pers.      Gw rasan              'ı< mp.        ya       rasan    2, mand,.       risn,
8854:Au - subbar:                 "eine        Pflanze          in Khorasan"                 2,
10928:on        -    tabas:            eine        Stadt       in    Khorasan -
10931:Ol             - tabasän:                   Dual    v.     tabas,         zwei          Städte     in    Khorasan             4,
11006:ol&>         -      tarbän:           "Fürst          in    Khorasan!        v.    pers.        Ob,        darhän            oo   pers. , dar
11299:©%P-         tüs:                 eine           Stadt    in    Khorasan,           mand.          tüs 4,
11701:>       -           farsah:             "Parasange,;                   ein        persisches         Maß,     ungefähr         6232   mt        pers.
11702:            Li             farsang                > mp.                sd o frasang                    ap.        *frasanga       "a parasang"        6,
=== AFM grep رسن
298:0 ®+ ,|11 ,)7 5) العود 0 ) ܡܳܐ به . .قال الاصمعي ذهو فارسني
312:( !¥ ;ܨ ) 3091 فارسنتها آ نك وهو بالسريانّة ܐܢܟܐ و بالعبرانتة $
590:الشجري ٠ ٠‏ وهو ܘܝܬܝ للمصروع اذا عآه ق في علقه وللرجل ܫ بذاء: النفرسن اذا ربط
795:( البوصي ) ضرب من السفن فارسني معرب (اللسان)٠.وة:‏ سر $ >
1855:( الرسن) اليل 3 97 6 ايضاً ٠‏ وفرتكل يقول اله مأخوذ من
1857:ريسيدن ومعناء غزل ايضاً او من رسن اي المورصل
2170:فارسنة عراقة ون سلت إى كلت ومن كير اي ماسك
2441:( سدْجة ) ܐܬܡܐ ܩܐ ܨܘ فارسنة ܚ ܐܡܵܬ
2983:السرسن والما 80 والماطية ܐ ܝ 3 وه و كل ما صفح 5 ذهب 34 ܢ
3186:الدراء .< الاي تاليف جسلتيرسن): او من كم زا يدف الروك
3469:0 الكرستّه فارسيّتها كته ٠‏ واظن ان الكرسنة لغة فيها
3981:(النئبرشت) الذي شوئ لصف ܝܨ ا ܝ 2 اي نصف ومن رسن
4016:يخاف بزرًا دون 3 صلياً فارسنتة كلمون وبر كيتة مأر حو نه
4747:رسن ܕܡ
6681:به راصم رسن
```


## [2026-09-14T01:23:29.316Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA 7735-7775\"; sed -n '7735,7775p' incoming/PLA/PLA_pages.txt\necho \"=== PLA page markers near\"; grep -n \"\\[pdf page\" incoming/PLA/PLA_pages.txt | head -3",
 "description": "Read Asbaghi rasan entry"
}
```


### [2026-09-14T01:23:29.395Z] TOOL RESULT

```
=== PLA 7735-7775
1. Wahrmund                  s. v.,               Addai       Scher         s. v.,      Muhlt s. v.
2.       ebda,       Johnson              s.          v.
3.       Mackenzie             s.       v.
4. Muhit s. v.,                         al-MuCarrab                  s. v.,       Addai       Scher    s. v.
5.       Nyberg         Bd.        II     s.          v.
6.       Mackenzie             Ss.      v.
7.       Brockelmann                 s.          v.
8.       Macuch         s.     v.
9.       Chista         Bd.        10     S.          1190,    Johnson           s.    v.
10.       Macuch         Ss.       v.
11.       Ernst         S.     46.
12.       Macuch         s.        v.
rasan                                                                       136                                                          raff


ow-      rasan:           "Strick"              aus    pers.      Gw rasan              'ı< mp.        ya       rasan    2, mand,.       risn,
       syr.     w> 3,


Ai,      rast:        "eine           Speise"          pers.      4,


aiı,.-      riäta:         "eine           Art    Eintopf"            pers.        5, wahrscheinlich                eine       Abkürzung
       für     ad-e        reäte.

wu,         - ralidiyya                   = raft ga. v.           6,

of, - rasäs:               "Blei,           Zinn",        das Wort kann nach Ansicht                              von Siddigi kein
       arabisches               Wort        sein,        weil     zwischen              ihm    und    seiner       angeblichen           Wurzel
       0, rass            "festfügen"                 kein      Zusammenhang                 besteht,       So kann       es    seiner
       Meinung            nach        von       pers,                  arziz           — mp. oJ        ardid       7 abgeleitet           sein,
       Im    Armenischen                   existiert           immer        noch        die    Form     arcic,      mand.       rusas,     syr.
         1     8,


32, - rasad:              "Anteil"              aus     pers.    »,     rasad           °,


                                                                                  10
>e, - rasad?              "Rechnung;              eine       Melodie"                   aus    pers.       ı.    rasat    v.    Verb     Yu
       rasidan            "erreichen,                 ankommen"             T     mp.    aD     rasit       v.    Verb    rasitan        11,
=== PLA page markers near
```


## [2026-09-14T01:23:30.724Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM 1845,1865\"; sed -n '1845,1865p' AFM_pages.txt\necho \"=== page tags\"; grep -n \"\\[pdf page\" AFM_pages.txt | awk -F: '$1>1700 && $1<1960' | head",
 "description": "Read Addi Shir rasan entry"
}
```


### [2026-09-14T01:23:31.797Z] TOOL RESULT

```
=== AFM 1845,1865
+ رن ) فير بجر ضَلت تعد 22 4 ܐܢܟ معرب ارزن وهو ܡܨ
ܐܝܬ ܠܚܡ اللوز ܐ ܨ 11 05 ܐ الادوية وتتخذ من اغصانه
العمي ܢ 9 5 ܐ محان 30 هن سيراز دكثر فيه هذا
الجر
3 ن)) العسن ونات يفرش اوراقة على الارض دهي طويلة تبلغ الورقة منها
الى ط ول ذراع 2 :|© :10 في ܦܐ القاطع : 037 على وزن دامن يقال
9 اصله طيب الرائحة لونة بين الممرة وااضرة زهره مائل الى اردق
وبزده ܒܥܬ بيزر العصفر وهو عر يض قليلا وطعمة حاذ والْستّعمل ܐܩܝܐ ّ ويستى ܐܐ
بالعريية ܝ 5057( منشمس ورقة عريض:وطو يل
ويقال لبه حب الراسن ولاصله | الراسن »
( الرسن) اليل 3 97 6 ايضاً ٠‏ وفرتكل يقول اله مأخوذ من
80 المثتق هو 0 من 0.77 ܐ (ص: - › \ ) !ܙ ܬ مشتق من
ريسيدن ومعناء غزل ايضاً او من رسن اي المورصل
الرشحة 325:0 ) شرا عه وهو ܟܐܝܐ تعمل من العدس كلتق 3 قدت من ترقاك
العجين واصل ܘܫ رشته بالفارسيّة ܐܝܐ3 ܣ
* (الرشك» اكبيد اللحية معرب من ريشكاو: اي بليسة الثور 9 علل
الرجل الاحمى
(الشغك) فادسق ححض وقو العقرب
04:02 39
( § القام الاول ٠‏ هن الانفام تعريب رانست ومعناه المستقي الموافق
+ د 0 معرب عن 7 الذي ܝ
=== page tags
```


## [2026-09-14T01:23:43.969Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndef leafof(path, lineno):\n    lines=open(path,encoding='utf-8',errors='replace').read().split('\\n')\n    return '\\n'.join(lines[:lineno]).count('\\f')\nprint('PLA rasan leaf(0based)', leafof('incoming/PLA/PLA_pages.txt',7747))\nprint('AFM rasan leaf(0based)', leafof('AFM_pages.txt',1855))\nEOF",
 "description": "Compute leaves for PLA and AFM"
}
```


## [2026-09-14T01:23:44.798Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 tools/ref_page.py AFM:72 --image 2>&1 | tail -40",
 "description": "Fetch Addi Shir page 72"
}
```


### [2026-09-14T01:23:45.016Z] TOOL RESULT

```
PLA rasan leaf(0based) 150
AFM rasan leaf(0based) 73
```


### [2026-09-14T01:23:46.135Z] TOOL RESULT

```
no scan of AFM covers printed page 72 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:23:58.780Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la | grep -i afm; ls incoming/ 2>/dev/null | head -40; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\"",
 "description": "Check AFM local files"
}
```


### [2026-09-14T01:23:59.914Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb   383664 Sep  4 13:59 AFM_alt.txt
-rw-rw-r--  1 sfmqrb sfmqrb   342401 Sep  4 14:06 AFM_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb 14780832 Sep  4 14:01 AFM.pdf
-rw-rw-r--  1 sfmqrb sfmqrb   354548 Sep  4 14:06 AFM.txt
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
```


## [2026-09-14T01:24:06.099Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npdftoppm -f 74 -l 74 -r 200 -png -singlefile AFM.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm74-420\nls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm74-420.png",
 "description": "Render AFM leaf 74"
}
```


### [2026-09-14T01:24:15.454Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1227534 Sep 13 21:24 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm74-420.png
```


## [2026-09-14T01:24:17.690Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm74-420.png"
}
```


### [2026-09-14T01:24:18.651Z] TOOL RESULT

```

```


## [2026-09-14T01:24:18.648Z] INPUT

[Image: original 1942x3267, displayed at 1189x2000. Multiply coordinates by 1.63 to map to original image.]


## [2026-09-14T01:24:38.540Z] TOOL CALL #27: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM\ncat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/72.vision.txt <<'EOF'\n[Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, printed p. ٧٢ = 72 (= AFM.pdf leaf 74, offset leaf − 2). Read from page image, page 420 verification, root Rek/Reg 2.]\n\n( الرَسَن ) الحبل والمَقوَد وهو חבל بالعبرانيّة ايضاً . وفرنكل يقول انّه مأخوذ من\nالفارسيّ رِيس المشتقّ هو ايضاً من رِيشتَن اي غزل ( ص : ١٠٠ ) . او هو مشتقّ من\nرِيسيدن ومعناهُ غزل ايضاً او من رَسَان اي المُوصِّل\n\n(preceding entries on the same page: الرازقيّ / والرَازِقيَّة ، الرَوزَنة ، الأَرْزَن ، الرَاسَن ؛\nfollowing: الرِشْتة )\nEOF\necho saved",
 "description": "Save AFM p.72 vision text"
}
```


### [2026-09-14T01:24:38.620Z] TOOL RESULT

```
saved
```


## [2026-09-14T01:24:40.598Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON grep رسن\"; grep -n \"رسن\" MON_part1.txt MON_part2.txt 2>/dev/null | head -20\necho \"=== FFD grep آرمیدن/رمیدن\"; grep -n \"آرمیدن\\|رامیدن\\|آرام\" incoming/FFD/FFD_pages.txt | head -20",
 "description": "Mo'in rasan, FFD aramidan"
}
```


### [2026-09-14T01:24:40.690Z] TOOL RESULT

```
=== MON grep رسن
MON_part2.txt:287:غازی: [22:(ص.) رسن‌باز» ریسمان‌باز. 
MON_part2.txt:1655:(۱.) رشته» ریسمان» رسن. 
MON_part2.txt:4206:ترسنا کك. کسی که امور را از یکدیگر فرق 
MON_part2.txt:6242:فر سخ. ۲ (معر . فرسنک | ( ۰) واحد 
MON_part2.txt:7123:فریادرس: (۲25)۲65-.] [- فر بادرسنده ] 
MON_part2.txt:7482:فشل: ا25] [ع.] (.) مرد بد دل و ترسنده و 
MON_part2.txt:8236:سنگ اندازی که از رسن دو ی با 
MON_part2.txt:9596:را پرسند. وی در جواب چنین گویند. کار 
MON_part2.txt:10350:نهایت رسنده. دور؛ مق. دانی» نزدیک. 
MON_part2.txt:11091:رسند همجنان که اسب در دویدن است تبر 
MON_part2.txt:12122:(نظ. قد.) مکانی بلند قریب یکث فرسنگ 
MON_part2.txt:13412:الب با املاح آرسنیکث یا آنتی‌پیرین به عمل 
MON_part2.txt:13656:جناغ سینه نمی‌رسند بلکه هر کدام به 
MON_part2.txt:15002:خرسند بودن به قسمت خود» بسنده کردن به 
MON_part2.txt:15003:مقدار کم. (امص.) خرسندی. صرفه‌جویی. 
MON_part2.txt:16830:خواندن کتاب‌ها و قصص ترسناک و خیالی) 
MON_part2.txt:17752:کاررس: (۶ع۲۸5)۲-.۲ [- کاررسنده] (ص‌فا.) 
MON_part2.txt:17808:کارسنج: [:52-.۲ [- کارسنجنده] (ص‌فا.) 
MON_part2.txt:17952:پرسنل. 
MON_part2.txt:22602:رشیدی به معنی ثلث فرسنگ (که یک میل 
=== FFD grep آرمیدن/رمیدن
264:کتیبه‌های شاهان ساسانی به الفبایی که از آرامی گرفته شده و از راست به چپ نوشته
277:هزوارش واژه‌ای آرامی است که به فارسی میانه خوانده می‌شده. مثلاً می‌توشتند «مِنْ».
291:پهلوی اشکاتی به الفبایی» که از آرامی گرفته شده و در آن هزوارش به کار رفته» نوشته
682:آرامیدن. آرمیدن
683:«آرامید» مادةٌ ماضی جعلی است» از مادةٌ مضارع ساخته شده است.
684:آرام < ایرانی باستان 2 - 1308 - 3* برای 8 > آرای. 5 پیشوند فعلی است.
688:ريشهٌ 1318 «آرمیدن» و «رامیدن» هم آمده‌اند.
1377:خرامیدن
1498:رامیدن
1499:۰ آرامیدن
```


## [2026-09-14T01:24:48.647Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '675,700p' incoming/FFD/FFD_pages.txt\necho \"--- pdf page tag context\"; grep -n \"\\[pdf page\" incoming/FFD/FFD_pages.txt | awk -F: '$1>600 && $1<760'\necho \"=== rāmīdan 1490-1510\"; sed -n '1490,1512p' incoming/FFD/FFD_pages.txt",
 "description": "FFD aramidan entry"
}
```


### [2026-09-14T01:24:49.735Z] TOOL RESULT

```
است. 7 پیش از 1 به 8بدل شده است. 734 به معنی «منظم کردن» است. 18 پسوندی بوده
که از ریشهٌ لازم» صفت فاعلی گذشته, و از ريشهٌ متعدی» صفت مفعولی گذشته
می‌ساخته است.

آرای + فارسی میانه 273 < ایرانی باستان 2 - 734 - 3*. 2 برای ساختن ماده از ريشه
به کار می‌رفته است.

آرامیدن. آرمیدن
«آرامید» مادةٌ ماضی جعلی است» از مادةٌ مضارع ساخته شده است.
آرام < ایرانی باستان 2 - 1308 - 3* برای 8 > آرای. 5 پیشوند فعلی است.
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
--- pdf page tag context
636:[pdf page 27]
662:[pdf page 28]
666:[pdf page 29]
685:[pdf page 30]
709:[pdf page 31]
735:[pdf page 32]
=== rāmīdan 1490-1510
دیدن
دید <ج فارسی میانه 474 « ایرانی باستان ۵۲-1۵*. برای 48 > آراست. ريشة 7
به‌معنی «دیدن» است.
[pdf page 60]
ماده‌های ماضی و مضارع فارسی دری نا ۵۵
بین < فارسی میانه ۷۷68 + ایرانی باستان ۹/۵۱-3* 23 نشانه‌ای بوده که برای ساختن
مادهٌ مضارع از ريشه به کار می‌رفته است. ريشةٌ ۷۵ به معنی «دیدن» است.
«دیدن» و «بین» چون «آمدن) و «آی» دو ریشه‌ای است.
رامیدن
۰ آرامیدن
راندن
راندن مخفف «روانیدن» است و آن فعل واداری از «رفتن» است. در فارسی دری
فعل واداری از مادةٌ مضارع + «ان» و «(عن» ساخته می‌شود. «۵۶) در متون کهن آمده
مادهٌ ماضی فعل واداری هميشه جعلی است و به جای «انید» ممکن است («اند» به
کار رود.
ربودن
ربود + فارسی میانه 1010.
ربای + فارسی میانه 1003 +« ایرانی باستان ۵رقم۳*, 2رقم" از ۳803: اسم
به‌معنی «ربودن» و 8نشانه‌ای که برای ساختن مادةٌ جعلی از اسم به کار می‌رفته» ساخته
شده است.
مادهٌ ماضی باید «رّفت» < فارسی میانه ۳۵۶۲ < آیرانی باستان ۵۵ می آمد. به قیاس
با 573 و 5736 «ربود» آمده است.
3 از ریشةٌ 780 به معنی «ربودن» و پسوند 3 ساخته شده است.
```


## [2026-09-14T01:25:00.076Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:737 2>&1 | head -60",
 "description": "Fetch Borhan p.737"
}
```


### [2026-09-14T01:25:01.156Z] TOOL RESULT

```
no scan of BQT covers printed page 737 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:25:05.041Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1));print(d['BQT'].get('page_offset'))\"\nhead -5 BQT_v2_pages.txt; grep -c \"\\[pdf page\" BQT_v2_pages.txt",
 "description": "BQT scans metadata"
}
```


### [2026-09-14T01:25:06.142Z] TOOL RESULT

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
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
0
```


## [2026-09-14T01:25:12.701Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 194 195; do echo \"=== leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tr -s ' \\n' ' \\n' | head -25; done",
 "description": "Print BQT v2 leaves near p737"
}
```


### [2026-09-14T01:25:13.756Z] TOOL RESULT

```
=== leaf 194
 ‫‪۷۳۹‬‬
‫را‬ ‫مدور‬ ‫بز رگ‬ ‫زا کوب شوم ارا‬ ‫ومع‬ ‫کرمان بیز ند وبخورند وارد نیزسازند ونان هم‬
 ‫خت ‪۲‬‬ ‫يزنك ‪.‬‬
‫‪۰‬‬ ‫دوم‬ ‫بم خای‬ ‫=‬ ‫خر گاه خصر‬
 ‫خرك = بر وزن فلك » مخفف خارك‬
 ‫کنانه ازآسمان است‬ ‫است» وان نوعی ازخرهای خشك باشد » وبعضی‬
‫سیز سرخرگاه‌سزگاو پشت‬ ‫گراه‬
 ‫خ‬ ‫مور رما تت که خرمای نارسده باشد‬ ‫و‬
 ‫بمعنی خر گاه خضراست که آسمان باشد ‪.‬‬ ‫= ومصفر خر‬ ‫رخوانند‬
 ‫ببسان‬
 ‫وآترابعضی از عر‬
‫خگراه قمر ‪ -‬کنابه از هالهباشد‪.‬‬ ‫هم‌هت ‪ -‬وچوبکی باشد که برروی طنبوروعود‬
 ‫وآن دایرهء‌ایست که‌بعضی اوقات ازبخار بهم هرسف‬
 ‫و کمانسه(‪ )۱‬وامثال آن کذارند وتارها رایرهالای‬
 ‫زآندایره منگردد ‪.‬‬
 ‫چنانسه ماهمرک‬
 ‫آن کشند ‪ -‬و ام دهی استت از ولات فاری در‬
 ‫ییراز ‪ -‬و تخته‌ای ناشد که‬
 ‫ش‬ ‫خر‬
 ‫س ف‬
 ‫هشت‬
 ‫وناه کاران را برآن خوابانند و درهٌ‬
 ‫مجرمان گ‬
‫اول را‬ ‫و آسمان‬ ‫است که خرمن ماه باشفد —‬
 ‫و چوییرا نز گویند که استادان‬ ‫تادیب زتند ‪-‬‬
=== leaf 195
 ‫خرم‬ ‫‪ ۳‬اس‬
 ‫آمده ات ‪.‬‬ ‫کمان حلقه را بدان چکلنهند » وآن دوپارچه‬
 ‫چوب است که اندك خمی دارد‪-‬وتله‌ای‌باشدمانند‬
‫خر گوشك » مسفرخ کوش است ‪-‬‬
 ‫‌‬ ‫‪۰‬‬ ‫‪۰‬‬ ‫و‬ ‫‪5‬‬
‫و نامگیاهی همهست دوابی و (‪ )۳‬قابض ودفع‬ ‫کمان که بجهت گرفتن شفال و جانوران دیگر‬
‫اسهال کند وانرا بعربی آذان‌الارنت خوانند‪. ۷‬‬ ‫برسر راه ابشان درخاك ینهان کنند همین که بای‬
‫و آن نوعی ازلان‌السمل است » و بعضی گوبند‬ ‫در آن نهند تدری از آن بجهد و براشان خورد‬
 ‫کباهی است که اسفول تخمآنت ‪۰‬‬ ‫ونانه اکزار دشوار بی‌تفم حم‬
 ‫وهلاك ساژد ‪ - ۱‬ک‬
‫خر کو ‪ - 3‬بروزن موقوف » نوعی‬ ‫ورفتارشدن مردم را نگیوزبند درتعبی‬
 ‫هت ‪ -‬گ‬
 ‫وآزاری وتپلکه‌ای ‪۰‬‬
‫کهوف جغد را‬
 ‫رگ چ‬
 ‫اچزغد باشد بغایت بز‬
 ‫کوبند ‪.‬‬ ‫بر‬ ‫خر گو از ؟ = بفتح کاف فارسی‬
‫خر گه ‪ -‬بروزن در گه‪ ,‬مخفف‌خر گاه‬ ‫کاو را‬
 ‫سرفراز» چوبی بشد که خر و‬ ‫وزن‬
 ‫بدان رانند ‪. ۳‬وم کاف همآمده ات ‪٠‬‏‬
‫است کهجا و محل وسیم و خيمةٌ بزرکه مدور‬
 ‫راد ‪٩‬‏ ‪:‬‬ ‫‪۰‬‬ ‫سریوش‬ ‫‪ - ۴‬بر وزن‬ ‫خر گوش‬
 ‫‪۰‬ویند ماد او را (‪)۱‬‬
 ‫جانوری است معروف ‪ ۵‬گ‬
 ‫از آسمان‬ ‫خر که اررق ‪ -‬کنابه‬
```


## [2026-09-14T01:25:22.299Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 192 196; do echo \"=== leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tr -s ' \\n' ' \\n' | head -30; done",
 "description": "BQT leaves 192,196"
}
```


### [2026-09-14T01:25:23.112Z] TOOL RESULT

```
=== leaf 192
 ‫پات‬
‫ثالك وفتح فوقالی» بمعنی خرام وخرامیدن باشد‬ ‫ی‬ ‫رن رک‬ ‫کی‬
 ‫یعنی براه رفن از روی از وسر کشی ‪.‬‬ ‫بزرکه ناهموار ناراشده را گوند که در مدان‬
 ‫حشره‪ -‬بفتح اول وثالی وثالك » مخفف‬ ‫شد (‪ )۱‬مردم‬ ‫و مالع عمور و آمد‬ ‫راه افتاده‬
‫خرخشه است که شالتاق وبیجا و بیموقم جنگه‬ ‫ونابه از کسی است که‬
 ‫کردیده باشد ‪ - ۴‬ک‬
 ‫و خصومت و مجادله کردن باشد ‪٩‬‏ ب‪-‬موعنی‬ ‫و مطلوب مانع شود‬ ‫الوب‬
 ‫طاحب‬
 ‫مبان دو مص‬
 ‫خراشیده وخراشیده شده همهت ‪#.‬‬ ‫وبنشینف ‪.‬‬
‫خشرین «بروزن‌بروین؛ بمعنی‌خرامیدن‬ ‫بفتح اول و کرنالی وسکون‬ ‫«‬ ‫خرش‬
 ‫باشد‪ ۷‬ب ونام طایفه‌ایست از افغان که دعوی(‪)۳‬‬ ‫هزل‬ ‫که از روی‬ ‫> کسی را کوند‬ ‫فرشت‬ ‫عن‬
 ‫سادت میکنند‬ ‫وخر کی بروی خنده کنند ‪ -‬وضم اول والی‬
‫خطرال ‪ -‬بکر اول ا طای حطی‬ ‫باه‬
 ‫رب‬‫کغای‬
 ‫مخفف خروش باشد که شور و غو‬
 ‫بکار‬ ‫و‬ ‫وخار وخلاشه ‪-‬وسقطوافکندنی‬ ‫‪-‬‬ ‫ات‪۴‬‬
‫بر وزن اقبال ‪٠‬‏ يوست کاو با يوست کردن شمر‬
 ‫را یز گویند ‪.‬‬ ‫تامدیی‬
‫رگاویند کهآ نرا پر اشزوشة طلا با زرنقد کرده‬
‫باشند و بعربی فنطار خوانند ‪ - ۸‬و بفتح اول‬
‫تخمی است دوایی ‪٩‬‏ وآن در ميان گندم روبد ‪.‬‬ ‫بالف کشیده‪ .‬یکی از نامپای خورشید است ‪. ۸‬‬
 ‫وطبیعت آن معتدل است ‪.‬‬ ‫خر شاده = بضم اول‌برروژن شاد بمعنی‬
‫بر وزن‬ ‫خر غول" "‪ -‬باوأو مجپول‬ ‫خرشااست که کی ادزامهای آفتاب عالم تاب‬
 ‫مرغول » کیاهی است که آنرا بارتنگه خوانند‬ ‫ات (() ‪.‬‬
‫و در دواها خصوصاً در پاکیزه کردن جراحتیا‬ ‫سکون‬ ‫و‬ ‫الی‬ ‫و‬ ‫حر شته = بفتح اول‬
 ‫‪ 3‬چك ‪:‬دعوای ‪.‬‬ ‫چكش‪:.‬خورشد است ‪.‬‬
 ‫(‪ )۷‬چ‬ ‫(‪ )۱‬چك ‪ :‬آمدوشد ‪-‬‬
 ‫‪ - ۱‬از ‪( :‬خبرزرك) ‪ +‬سنك تاجیکی ‪(8125۲21‬سنك زرك ناهموار) « مجله سخن‬
 ‫‪ ۸ : ۲‬ص ‪ » > ۸۱۱‬دزفولی ‪. 80165121‬‬
=== leaf 196
 ‫و‪۳۷‬‬ ‫خرمای ابوجهل‬
 ‫خرم روز ‪ - ۴‬نام روزهشتم است‌از‬ ‫است که ماه دهم‌باشد ازسال شمی وبودن فت|اب‬
 ‫هرماه شمسی‪ .‬کوبند ملوك عجم درین روزلیکن‬ ‫در برح جدی ‪ - ۱‬ونام روز هشتم است ازهرماه‬
 ‫درماه د‬
 ‫کیه‌ان ماه دهم است از سالهای شمی‬ ‫شمسی » و بنا برقاعدهکلیه که نزد فارسان مقرر‬
 ‫جشن کردندی‌وجامپای سفید پوشیدندی وبرفرش‬ ‫است که (‪ )۱‬نام ماه وروز (‪ )۲‬موافق آبد عید‬
 ‫نشتندی ودربانر! ءنع کردندی وبار عام دادندی‬ ‫باید کرد دراین روز عید کنندوجشن سازند ‪٩‬‏ ‪-‬‬
 ‫ویامور رعیت مشفول شدندی وامرزعان ودهقانان‬ ‫نام مرغزاری‬ ‫رضم اول وسکون انی بی‌تشدید ‏‬
 ‫بمالوك بر سر يت خوان نشتندی وچیزی‬ ‫مطلبی که‬ ‫است» در آ نجاکوهی‌هم هست که هر‬
‫خوردندی وبمدازآن هر عرضی )‪(٩‬‏ ومدعایی که‬ ‫عرض کنند جواب آبد ‪ .‬کویند چون سکندر‬
 ‫دائتندی بوادطه دیگری بعرض رسانیدندی‬ ‫ذوالقرنین فوت شد رومیان وفارسیان برسرمدفن‬
 ‫وملوك برعایا کفتی‪ « : ۴‬من‌هم یکی از شمایم‬ ‫اوگفتگومیکردند ‪ .‬فارسیان میگفتند هرجاکه‬
 ‫ومدار عالم بزراعت وعمارتست وآن بیوجود شما‬ ‫فوت شده است دفن باد کرد ورومیان میگفتند‬
 ‫نمیثودوما را از شماکزبر(‪)۷‬تیت چنادکه شما‬ ‫جابی کهمولد اوست دفن‌ميکنيم ‪ .‬چون کفتگو‬
 ‫را از ما"ماوشما چون دو برادرموافق باشیم ‪» .‬‬ ‫هر زان کت ری ي‬
 ‫خر م فصا کنابه از آسمان است‪.‬‬ ‫رفت و سوال (ف‪۳‬ر)دبپرچه جوابآید عمل(‪)4‬‬
 ‫تمود وچنان کردند ‪ -‬وبمعنی بخارهم بنظرآعده‬
 ‫خ»رم‪-‬‬ ‫رلی‬
 ‫خهراث ب بماتشصدیفد ثا‬
 ‫است‪ -‬و بی‌تشدید وسکون ثانی‪.‬نام مهره‌ای باشد‬ ‫رم زومینهای تمنالك‬
 ‫است که از روی آب (گ‪)۵‬‬
 ‫یهد کب‬
‫وود کهآنرا بجهت دفع‬ ‫سشفسيا‬
 ‫اوزشی‬ ‫ىرھىخىزد ‪4.‬‬
 ‫چشم زخم‌بر گردن اطفال بندند؛ وباین معنی‌بفتح‬ ‫خرمای اجبوهل‪ -‬نوعی از خرما‬
 ‫و‬ ‫اول م مده ست‬ ‫باشد وازیوست آن رسن تابند‪# .‬‬
 ‫(‪ )۷‬خم ‪ + :‬که ‪.‬‬ ‫‪.‬‬ ‫چون‬ ‫‪+‬‬ ‫‪:‬‬ ‫چش‬ ‫چك‬ ‫(‪)۱‬‬
 ‫‪ -۳ :‬بابد ‪.‬‬ ‫چش‬ ‫(‪ )4‬چك ‪,‬‬ ‫(‪ )۳‬چك ‪ ,‬چش ‪ ۲ :‬بابد ‪.‬‬
 ‫(‪ )۷‬چش ‪ :‬کریز ‪.‬‬ ‫)‪ (٩‬چك » چش‪ :‬غرضی‪. ‎‬‬ ‫() چك‪ .‬چش‪ :‬آبهای ‪.‬‬
 ‫نام‌ماه دهم هرمال‌شمی رروزهشتم هرماه شم ی دی است » له «خرم؟ اما روزهشتم‬ ‫‪۱‬‬
```


## [2026-09-14T01:25:47.599Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== leaf 195 full\"; awk 'BEGIN{RS=\"\\f\"} NR==196' BQT_v2_pages.txt | tr -s ' \\n' ' \\n' | tail -30",
 "description": "BQT leaf 195 tail"
}
```


### [2026-09-14T01:25:48.661Z] TOOL RESULT

```
=== leaf 195 full
 ‫گفته اند ( ‪) ۲‬‬
 ‫خر گه مه ه مخفف خرگاه ماه است‬
 ‫لان الحمل است ‪.‬‬
 ‫که هاله و خرمن ماه باشد ‪.‬‬
 ‫وبارتنگه تخمی‬
 ‫بضم اول و فتح ثانی با قشدید ‪.‬‬ ‫حر"‬ ‫دوابی ‪٩‬‏ »وبایتمعنی‬
 ‫بمعنی شادمان وخوشوقت باشد ‪*٩-‬‏ ونام مامدی‬ ‫بساین بى نفطه هم‬
 ‫و‪.‬‬ ‫‪- :‬‬ ‫(‪ )۳‬چك‪ ,‬چش‬ ‫(‪ )۲‬چك‪ .‬چش ‪:‬گونن‪.‬‬ ‫(‪ )۱‬چش ‪ :‬آنرا ‪.‬‬
 ‫زی‪.‬‬
 ‫رتشات‬
 ‫دمخ‬
 ‫شتی چو کی‬
 ‫بپرو‬ ‫‪ - ۱‬تنی‌چون خکرمان ازگوژپشتی‬
‫‪۰‬‬ ‫أھ؟‪.‬‬ ‫نظامی گنجوی‪« .‬دکنجنه‬
 ‫از‪ :‬خر (الاغ) ک‪+‬واز (ہ‪.‬م‪[ ).‬‏ کواژ = جوازمعرب ]‬ ‫‪۴‬‬
 ‫هست‌باشمشیر تواقلام شیران‌خر کواز‪.‬‬ ‫‪ - ۴‬هت باخط‌توخطچینیان چون خط براب‬
 ‫«منوچهری دأمفانی ‪.۳4۹‬‬
 ‫‏* جالوری از بتانداران خانده ‪.‬‬ ‫‪ - ۴‬پهلوی ‪ « 1508721‬اونوالا ‪. ۵۸۲‬‬
 ‫معرب آن خرکوی = ‪( 120210‬فر)«لك ‪ ۲‬ص ‪4۲٩‬‏ «دزیج‬ ‫‪۱‬‬ ‫و وحشی ‪.‬‬ ‫زش‬
 ‫کاو‬
 ‫در‬
 ‫‪ = ۷‬کل ماھور ‪30٥830۲8۷‬‏ دککللاب ‪۶4۲‬؟‪.‬‬ ‫‪۱۱۹۳٩‬‏ ‪.‬‬ ‫ص‬
 ‫‪ _ ۵‬از ‪ :‬خر (بزرك) ‪ +‬کوف (ھ‪: ).۴.‬‬
 ‫عاشق که سمندر نه بودخر کوف‌است‬
 ‫شاه قاسم انوار‪.‬‬
 ‫که ‪ > ۲:۱‬شاید از‬ ‫* ‪ -‬بهلوی ‪( 712۲۳105‬شاد) «ریب‬ ‫‪ _ ٩‬رك ‪ :‬خرگاه‪. ‎‬‬
 ‫‪ - 2‬ا ‪( #‬نيك براعش) فس ‪:‬سان‌کریت ‪( 2907137115 -‬دوست داشتن) ?هوشمان ‪۹۷٤۰‬‏‬
 ‫ورك ‪ :‬اسشق ‪ 4۷1‬و اسفا ‪ ۲ : ۱‬ص ‪۳٩۱۰‬‏ کیلکی ‪( 1013۲103‬خوب)‪:‬‬
 ‫فرخ تبار توکه توبی سید تبار‪.‬‬ ‫خرم نژاد توکهتوبی‌مفخر نراد‬
 ‫«مفزی لثاموری ‪.*۷۰۳‬‬
```


## [2026-09-14T01:26:03.818Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 416 417 418; do echo \"=== leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tr -s ' \\n' ' \\n' | head -12; echo \"...tail...\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tr -s ' \\n' ' \\n' | tail -12; done",
 "description": "BQT leaves near p960"
}
```


### [2026-09-14T01:26:04.931Z] TOOL RESULT

```
=== leaf 416
 ‫بیان شانز دهم‬
 ‫ت‬
 ‫ات و‬
 ‫نه لغ‬ ‫دررای بی نقطه باقاف مشتمل بر چ‬
 ‫کهارد‬
 ‫اشرات کردنوازبهلوبیهلو غلطیدن باشد‪.‬‬ ‫رق س بکسراول وسکون ثالی » پوست‬
‫پااول مفتوح وسکون‌نالی وعین‬ ‫ر قعا‬ ‫لاك بشت دربایی باشد (‪ )۱‬و بعضی گوبند پوست‬
‫بینقطه بالف کشیده ‏ بممنی سرخس و کیلدارو‬ ‫لباكشت (‪ )۲‬وبسنی دیگر گفته‌اند نام لاك پنت‬
‫اشد ‪ ۰9 ۴‬آن چوبکی أست دوایی که دکرنار‬ ‫ی(‪٩ )۳‬‏ » وباین ممتی بفتح اول حم‬
 ‫اعسرتبدر‬
 ‫دربای خزر یایند ک‪.‬وبند عربی است ‪.‬‬ ‫آمده است ‪.‬‬
 ‫ر قعه ‪ -‬بفتح اول و ثالث " هکریاهی‬ ‫رقاراق ‪ - ۲‬بنتم اول و ثالی و رای‬
...tail...
 ‫عرك‬
 ‫ق‪.‬‬‫ر‪٩‬‏‬
 ‫‪۹۷:‬‬
 ‫ص‪۱‬‬
 ‫ورك ‪ :‬رقعا ‪.‬‬ ‫س‪.۰۸۱‬‬ ‫لك؟‬
 ‫‪0۵٩‬‏‬ ‫باهرصفعة‬
 ‫٭ رفوگر ‪ -‬نم‬
 ‫اول و دوم وفتح چهارم » از ‪:‬‬
 ‫أ‬ ‫شغل‬ ‫رفو ‪ +‬کر ( یوند‬
 ‫و مبالفه ) ‪ ۰‬آنکه رفو کند ‪۰ ۱ ۰‬‬
 ‫کیکه ‏ شخلش رفوکردن‬
 ‫الست ‪.‬‬
=== leaf 417
 ‫رك‬ ‫‪۷‬و ‪4‬‬
 ‫ومعی‬
 ‫پیام ابزد وییام نآیفوریدون مینوبسند‪ .‬ج‬ ‫رقعة بست نیلگون = کنابه از‬
 ‫اورانوح میدانند وعربان سلام عقلیى‌اولحمالمین‬ ‫زمین است > و بای سین بی‌اقطه شین نقطمدار‬
‫مینوسند » و بزعم اهل هند روز اينجم اسفتدار‬ ‫حم بنظر آهده است که رفعة پشت لیلگون‬
‫ماه‌باشد که‌درحة پنجم‌حوت‌است» ودرین روزرقمة‬ ‫باشف ‪.‬‬
‫کژد‌مینوسند بسیبآدکه میگوبند درجةً پنجم‬ ‫از‬ ‫به‬
 ‫نونا ‪-‬‬
 ‫کلگ‬
 ‫رعة بلند نی‬
 ‫ق‬
 ‫دازد ‪۰‬‬ ‫صورت حشرات‬ ‫حوت‬
...tail...
 ‫(‪ )4‬چك‪ :‬بازا ‪.‬‬
 ‫‪ «0‬فبشتن رقعه‌ها کژدم چیست ؟ این از رسم‌های پارسیان نیت » ولکن عامیان‬
 ‫نو آوردلد ویشب این روز برکاغذها تبیسند و بردرخانه‌ها بندند تا اندرو گزنده اندر بیاید ‪.‬ویتجم‬
 ‫روزاست از اسفندارمن ماه ‪ ,‬و پارسبان اورا مگریدران خوانند » زبراك زدان بربشوهران اقتراحها‬
 ‫کردندی و آرزوبها خواستندی ازمردان » «التفهدم ‪۰٩ - ۹۵۲‬‏ ‪ . ۰‬درآنار البافیه «چاپ زاخائو‬
 ‫ص‪ ۹۲۲‬آمده‪ :‬ازآغاز طلوع فجر نا طلوع آفتاب این رقعه را بر کاغذهای چهار کوش نوشته‪,‬‬
 ‫برسه‌سمت دیوارهای خاله بجسبانند ودیوار مقایل صترخاله را بازگذ‌ار د‪* :‬بسم‌انالر حمنالرحیم‪.‬‬
 ‫اسفندارمت ماه ‪ .‬اسفتدار مذروز» بستم دم ورفت زیروزبر ازهمه جز ستوران بنام یزدان وینم‌جم‬
 ‫اوفربدون ‪ .‬بم اله بآدم وحوا‪ .‬حسبی‌اله وحده وکفی › ‪ .‬التفپیم ص ‪ ۶۹۲‬ح‪ ۱‬و؛رك ‪ :‬خرده‬
 ‫«رژد» (ه‪.‬م‪ta ).‬‏ رك (ه‪.‬م‪۰ ).‬‬ ‫؟ _ مصحف‬ ‫دوارود ص ‪. ۶۱۲‬‬
 ‫اوستا ‪ .‬ي‬
 ‫رژه (ه‪.‬م‪. ).‬‬ ‫رجه =‬ ‫=‬ ‫رح‬ ‫=‬ ‫رک‬ ‫=‬ ‫‪۴‬‬
=== leaf 418
 ‫ه‬
 ‫ا ی‬ ‫کراب‬
 ‫آا‬
 ‫کویمتد‪ .‬وشمشیری که برپهلوی‌اسب‌بندند وار‬ ‫تبواشد ‪ ۰ ۱‬و بعربی ات‬ ‫ن)ی‬
 ‫مدع(‪۱‬‬
 ‫باژن‬
 ‫وپ‬
 ‫زمر رکابی هم خوانند ‪.‬‬
 ‫راسه ‪ - ۴‬پم اول بروزن خلاصه ‪.‬‬
 ‫ک‬ ‫ر کاب = بکراول بروزن‌قاب پىاله‌ای‬
 ‫يمعي‬ ‫‪E‬‏‬ ‫ماشف هشت‬
 ‫وآفرا (‪ )۲‬بعربی ابو مدلج گوبند‪.‬‬ ‫=‬ ‫است‬ ‫هم خفن‬ ‫سواری‬ ‫لب‬
...tail...
 ‫«حافط شرازی ‪٩۲۱‬‏ ‪.‬‬
 ‫چشممایست که راکلندرلُدبلمی ( متوفی بال‬ ‫ی»‬
 ‫نآب‬
 ‫کل =‬
 ‫ر او‬
 ‫رناباد ‪ -‬چم‬
 ‫‪ #‬ک‬
 ‫ازدننک‌انها کیره‬ ‫احداث کرده ‪,‬منبع آن بساقت مك فرسنگی تقرساه‌مدان دو کوه وممری‬ ‫‪۹۳۳‬‬
 ‫ی‬ ‫است ( آثار عجم ‪ .‬فرصت ات‬
 ‫ان‬ ‫لوحش‬ ‫رکنایاد ما صد‬ ‫رر‬
 ‫‪۲-۳۱۱‬‬ ‫«حافط «شیرازی ‏‪ ٩۱۸۹‬ورگ ‪:‬حافظ شبرىن‌مخن‪.‬ا‬
 ‫( إرهان فاطع (‪eT‬‏‬
```


## [2026-09-14T01:26:16.273Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'رامش' in l or 'رامین' in l:\n        print(i, l.count('رام'), [w for w in ['رامش','رامین','رامشگر'] if w in l])\nEOF",
 "description": "Find rām in Borhan vol2"
}
```


### [2026-09-14T01:26:17.338Z] TOOL RESULT

```
86 2 ['رامین']
107 1 ['رامش']
183 4 ['رامین']
302 1 ['رامش']
331 1 ['رامش']
384 1 ['رامش', 'رامشگر']
391 29 ['رامش']
392 27 ['رامش', 'رامین', 'رامشگر']
395 4 ['رامش', 'رامشگر']
399 1 ['رامش']
432 1 ['رامش']
551 1 ['رامش']
563 1 ['رامین']
589 3 ['رامش', 'رامین', 'رامشگر']
595 2 ['رامین']
608 1 ['رامش', 'رامشگر']
614 1 ['رامش']
650 1 ['رامش']
654 3 ['رامین']
672 2 ['رامش']
```


## [2026-09-14T01:26:29.255Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nimport re\nfor i in range(385,435):\n    l=leaves[i]\n    # try to extract digits in persian\n    nums=re.findall(r'[۰-۹]{3,4}', l[:400])\n    head=' '.join(l.split()[:6])\n    print(i, nums[:3], head[:70])\nEOF",
 "description": "Scan Borhan v2 leaves 385-435 headers"
}
```


### [2026-09-14T01:26:30.780Z] TOOL RESULT

```
385 [] ‫گفتار دهم‬ ‫اکزاب برهان قاطم د‬
386 [] ‫==‬ ‫راغ‬ ‫راد بوی » بابایابجد
387 [] ‫راست‬ ‫سوه‬ ‫رارقی ه بر وزن
388 [] ‫”‪~A‬‬ ‫رات‬ ‫تسا زع ‪‎‬هناش ‪.‬‬
389 [] ‫‪۲4‬‬ ‫خوانند ‪ ۰‬اکر درون وبرا
390 [] ‫س‪۳‬‬ ‫ه‪۳‬‬‫باه‬ ‫ران‬ ‫راك ‪ -‬بر
391 [] ‫رامعك‬ ‫‪-۳‬‬ ‫رامش د بکراك بروزن
392 [] ‫~‪“r‬‬ ‫رامشگر‬ ‫رامیتن ‏ د با
393 [] ‫رارز‬ ‫‪- ۳۳‬‬ ‫هم بنظرآمده است
394 [] ‫سوت‬ ‫راء‬ ‫شین ترگسایوالیرناد ‪۰ ۴‬‬
395 [] ‫راهوی‬ ‫و‪ ۳‬هس‬ ‫راه‌ کاهگشان ‪
396 [] ‫ومطلوب را گویند و مردم ماز
397 [] ‫بیان دوم‬ ‫دررای بی‌نقطه بابای |بحد
398 [] ‫—‪—Ara‬‬ ‫ربوسه‬ ‫برون؟ ‪ -‬بفتح اول
399 [] ‫‪ 4۳‬هت‬ ‫که کیاهی باشد که
400 [] ‫سس‬ ‫رجوعام‬ ‫ا او ماندند»‬ ‫تف
401 [] ‫رخش‬ ‫~‪t‬‬ ‫مرده را نز گفته‌اند‬
402 [] ‫‪4 ) ۰۷‬‬ ‫رخعا‬ ‫وئالث بالف
403 [] ‫ردای لیل‬ ‫م‪ ۳‬پهب‬ ‫واگر پراو
404 [] ‫‪—ttA‬‏‬ ‫رد کا‬ ‫رده ‪ -
405 [] ‫رزه‬ ‫‪‎-‬ی ) ‪“A‬‬ ‫مکان‌جنکه‬ ‫زرمگاه‪
406 [] ‫‪- 6‬‬ ‫رژیدن‬ ‫رر بدن "ت
407 [] ‫بیان دهم‬ ‫رای می نقطه باسین
408 [] ‫—‪AtA-‬‬ ‫رستاخیز‪‎‬‬ ‫رستگار است کهبمعنی خلاص
409 [] ‫با‬ ‫‪-‬‬ ‫وفتح فوقالی وها ومیم
410 [] ‫ها‬ ‫وی‬ ‫‪-‬‬ ‫رس‬ ‫مقرب وترديك
411 [] ‫رشتاك‬ ‫‪-‬ي‬ ‫‪ --‬ا‬ ‫‪.‬ویند عربی
412 [] ‫‪“Ao‬‬ ‫‪e‬‬ ‫رشته نگنده ‪ -‬بکر
413 [] ‫رسد گه ځا کی‬ ‫ت‬ ‫ا
414 [] ‫يبان سیز دهم‬ ‫در رای یاو‬
415 [] ‫بیان پانزدهم‬ ‫شش لغت‬ ‫بر‬ ‫رای
416 [] ‫بیان شانز دهم‬ ‫ت‬ ‫ات و‬
417 [] ‫رك‬ ‫‪۷‬و ‪4‬‬ ‫ومعی‬ ‫پیام ابزد
418 [] ‫ه‬ ‫ا ی‬ ‫کراب‬ ‫آا‬ ‫کویمتد‪
419 [] ‫رکو‬ ‫‪-‬‬ ‫‪-۹-‬‬ ‫بلفت زند وپازند
420 [] ‫=‬ ‫کرول‬ ‫وچادرىك‬ ‫‪-‬‬ ‫رکوه است
421 [] ‫رمکان‬ ‫هت‬ ‫‪-‬‬ ‫روش» بممنی‌تبدیل‌است که
422 [] ‫”‪IY‬‬ ‫رمه ‪ - ۳‬بنتح اول
423 [] ‫رند افریس‬ ‫وت‬ ‫خوشبو وخوشگوار حم
424 [] ‫سوه‬ ‫ردان خاك بیز‬ ‫و دام‬
425 [] ‫رنگه رییع‬ ‫‪-0‬‬ ‫‪‎‬ی ‪٩‬‬ ‫‪.‬‬
426 [] ‫نت‬ ‫رنگه رزگلگون‬ ‫نگ رر گلگون
427 [] ‫روادان‬ ‫=‪“۷‬‬ ‫ویآنشتر دآربهای‬ ‫پلای ‪
428 [] ‫سره‬ ‫روان آورد‬ ‫داشن را فيز
429 [] ‫رود بار‬ ‫‪4‬‬ ‫لخت پپلوی است
430 [] ‫سه‬ ‫رودزم‬ ‫مفرد روده همگفته‌اند ‪:‬‬
431 [] ‫روز خوش‬ ‫‪-4۷۱-‬‬ ‫لش مد و
432 [] ‫‪“AYY‬‬ ‫روز خون‬ ‫معروف‌است کهزمانة نایدارباشد؟
433 [] ‫روز مریم‬ ‫‪avr‬‬ ‫باشد ‪.#‬‬ ‫رور
434 [] ‫‪=4‬‬ ‫روزی افرای‬ ‫و« باشندة ده
```


## [2026-09-14T01:26:45.009Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== leaf 391 tail (footnotes)\"; awk 'BEGIN{RS=\"\\f\"} NR==392' BQT_v2_pages.txt | tr -s ' \\n' ' \\n' | tail -28\necho; echo \"=== leaf 422 head (رمه)\"; awk 'BEGIN{RS=\"\\f\"} NR==423' BQT_v2_pages.txt | tr -s ' \\n' ' \\n' | tail -20",
 "description": "Borhan ram and rama footnotes"
}
```


### [2026-09-14T01:26:46.280Z] TOOL RESULT

```
=== leaf 391 tail (footnotes)
‫راهشخو ار بخاای قطه دار و واو‬ ‫رمتان ‪ -‬بانای قرشتبروزن جانشین‪:‬‬
 ‫ا‬
‫معدوله ورای‌بی‌قطه بروزن فارغ بال » نام لوابی‬ ‫نام شخصی بوده چنك نواز‪ .‬گونند سازچنك رااو‬
 ‫است از موسیقی ‪.‬‬ ‫وضع کرده ات‬
‫وکاف » بامهم‌تیشكرامش‪-‬ت باکكسهترآ ترااكمشسوک ووآنرامریادبنع‬ ‫مادر * نام‬
 ‫ا‬
 ‫بفتح میم بر وزن‬ ‫=‬
 ‫‪¥‬‬
 ‫زرامر‬
 ‫شپریست کهابریق رامری‌منوب بدان شهرهست؛‬
 ‫وراه‌شگر باشد ‪.‬‬ ‫‪۰‬‬ ‫ویکرميم هما مده است‬
 ‫رام رای‬ ‫ا‬ ‫آرمیدن‪.‬‬ ‫ح‪٣‬‏ صفح قبل ورك‪ :‬آرام آرامیدن‪,‬‬ ‫‪ ۱‬رك‪:‬‬
 ‫که خود در لفظ ایشان خوش بود «رام»‪.‬‬ ‫‪ ۴‬شهی خوش زکنادلی بود و خوش نام‬
 ‫ویس ‪ 2‬ف‪.‬خر کگارلی ‪.‬‬
 ‫ات و اج‬
 ‫« اما بعضی (ازهندوان) نام « رام» برندکه او هم مظپر «به‬ ‫‪۴‬‬
 ‫‪E‬‬ ‫‪LSS‬‬ ‫‪o‬‬
 ‫دبتان المذاهی ص ‪.۹۵۱‬‬ ‫و افراط شهوت داشته اند ‪۰ .‬‬
 ‫‪۰‬‬ ‫شا کرده اردش رگوید‪ 1 :‬واما رام اردشیر فلااعرف موقمها‬ ‫درف کرشهرهای‬ ‫جمره‬ ‫ه‌‬
 ‫واما رام اردشیر (کذا) فالمسمی بلفة اهل‌الزمان ر(ی‌شهر) » «سنی ملوكالارض ب‪.‬رلین ص‪.*۳۳‬‬
 ‫درصورتیکه باقوت بنقل از حمزة اصفپانی گوید ‪ :‬رام اردشیر شهر (نوح) (بتشدید دوم) است که‬
 ‫‪. ۴‬‬ ‫معحجم البلدان‬ ‫بین اسفهان و خوزستان در جبال واقم است «‬
 ‫‪-۱۲‬‬ ‫ومزدسنا ‪6‬‬ ‫‪ 4‬برژین ‪۰‬‬ ‫مرزین‬ ‫‪۳‬‬‫‪ - ۱‬ظ‪.‬عمان «آذر بردین مهر“ است‪ .‬رك ‪:‬‬
 ‫بيك فرسنگی دای‬ ‫میم“ قربه‌ایست‬ ‫ح‬ ‫ت‬ ‫ف‬ ‫ب‬ ‫‪6‬‬ ‫درمعجم‌الیلدان ‪ 2‬ر امران‬ ‫‪۷‬‬ ‫‪۰‬‬ ‫و‪۷۲۳۲‬‬ ‫‪۹۷‬‬
 ‫شهر کی کم مردم‬ ‫حدود ‪nimãR( : ۳۱ ۲‬‏‬ ‫‪«۸‬رامن»(ر کے‪:‬مینورسکی‪.‬‬ ‫حدودالعالی‌ص‪۲‬‬ ‫ودر‬ ‫خراسان‬
 ‫‪ - ۸‬بهلوی‪ramishn ‎‬‬ ‫لیامده‪.‬‬ ‫ونار کت از نات حجدال بأد شده‪ .‬و«رامر» در هك‬
 ‫ش (اسممصدر) » برایشاهد » رك ‪ :‬رامشگی ‪.‬‬ ‫رام‬
 ‫»ا سفق ‪6۰٩‬‏» «اوبوالا ‪ ۰ »۸۳۸‬از‬

=== leaf 422 head (رمه)
 ‫بیان بیستم‬
 ‫در رایبی نقطه بانون مشتمل برسی و شش لغت و کنایت‬
‫رب است که موی زهار باشد ؛ و بفتح اول هم‬ ‫رفت ^ ‪ ۰‬بنم اول وسکون انیو بای‬
 ‫کفته اند (‪. )۳‬‬ ‫ایچد » موی زهار را گویشد ‪.‬‬
‫سکون ثالی وجیم»‬ ‫رنج ‌‪ -‬بقتح اول و‬ ‫ر نبه ‌ = ْم اول پروزن دلبه» بم‌عنی‬
 ‫(‪)۳‬خم‪۶ ۱‬‬ ‫‪.‬‬ ‫‪ +۲ :‬یز‬ ‫‪ ,‬چش‬ ‫چك‬ ‫(‪)۷‬‬ ‫‪ :‬رند ویاژند ‪.‬‬ ‫)‪ (۱‬جك‬
 ‫ویفتح‪ ...‬گفته‌اند ‪۰‬‬
 ‫را‬ ‫خاش مولف ‪kãma ۰‬‏‬ ‫و‬ ‫ما «بوتکر ‪۵‬‬ ‫بهلوی ‪1‬‬ ‫هر ‪namr„ ۰‬‏‬ ‫‪۱‬‬
 ‫‪ . °‬رك؛ رمه‪.‬‬ ‫‪ «9‬باروچا ‪۸‬‬ ‫ات‬ ‫‪10۷‬‬ ‫‏‪ hamãk‬خوانده بمعتی همه (ه م ( حزوارش همه‬
 ‫بایف دالت که فرائت‬
 ‫«سه رك‪ :‬زیون » اربون ‪ ۰‬ارمون ‪.‬‬ ‫‪۳‬‬ ‫باروچا ‪۹۱۲۰‬‬ ‫‪ ۷۰‬ورك‬ ‫بمعئی ما ‪2‬‬
 ‫تفس ‪٩.۰‬‏‬ ‫‪ :‬رم» رمكڭ؛ معرب آن رمق‬
 ‫سشق ‪ ۰۲1۰‬رك ‪:‬‬ ‫داد‬ ‫‪۰1‬‬ ‫‪ -‬بهلوی‪2۳13۲ 6‬‬
 ‫‪( -‬عر) رمه (حنم اول وتشدید دوم ‪ .‬بارء رسن بوسیده»‬ ‫رك ‪ :‬رفه‬ ‫‪۴‬‬
 ‫استخوان‌پو‪-‬یده» مورچۀ پردار» کرمك‌چوبشواره‬ ‫پیشالی؛ جمله وسائر؛ رمه (بکسراول ‪e‬‏‬
 ‫رك‪ :‬رمن ‪.‬‬ ‫‪- ۱‬‬ ‫خاك مناك » مغز استخوان » «منتهی الارب <‪.‬‬
 ‫رك‪ :‬رلب‪.‬‬ ‫‏‪- ٩‬‬ ‫رلبة» رمعان‪.‬‬ ‫رك‪ :‬روم » روههه‬ ‫‪۸‬‬ ‫‪ :‬رامیار ‪.‬‬ ‫رك‬ ‫‪۴‬‬
 ‫(پوند مصدری)؛ ترسان شدن‪ ,‬احتراز کردن‬ ‫دن‬
 ‫‪ #‬رمیدی ‪ -‬بفتح‌اول وسوم؛از‪ :‬ربم‪۳‬‬
 ‫از فرت وکراهت ‪ -‬پربدن از بیم‪ -‬آشفته ویربشان شدن ‪.‬‬
```


## [2026-09-14T01:27:31.054Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT rāman\"; grep -n \"rāman\\|räman\\|airime\\|hu-rama\\|huraman\\|paiti-rāman\\|paitiräman\" BRT.txt | head -25\necho; echo \"=== PHD rasan/ramisn\"; grep -n \"^rasan\\|^rāmišn\\|^rāmišn\\|^ram\\|^rāy\\|rasan \" PHD.txt PHD_mackenzie.txt | head -25",
 "description": "Bartholomae and MacKenzie lookups"
}
```


### [2026-09-14T01:27:31.133Z] TOOL RESULT

```
=== BRT rāman
4679:tsin  aiare^  utä  'niyä  bagäA^  lyaty  At^tiy Bh.  4-  ■  2  >  13;  —  "^'"i  vahistsm . .  'iiya^qm yat  anifsanqm  spmtanqtn  YL_j,3;  —  yetii zT  MS  maiysia  .  .  yazayanta  yak:a  'nye yazaiinhe  . .  yazinti  ". .  wie  dae  andern y.  verehrt  werden"  YtÄii;  —  ahe  nars asaofiB  ..  äai  'nyazsqm  asaonqm  Yti.30; i3-  ^Ti  —  airime  gstüm  kl  nUhka^a  .. *par^itar?m  kala  'uyalibyd  mazdayas- f>aiibysY.(}.^y, —  'nye  aaksus /rals.iar^ %ra  Aog.65(?)'';  —  \'.ulä  pärsJ' uls  msdt^ utä  "niyS  dahySve^  Bh. /.  13,  14;  11;  — psrsaiy . .  msdaiy  utä  'niy^uvä  dakyusuvä Bh.  J.  10;  —  ahmäi  nmsnäi  daaäiti  gBu^ca vq^iwa  . .  upa  'nya  (APn.)  sHndayäti  Yt /o,  2  8 ;  —  vätB  , ,  AubaoioitarS  . .  'nyalifyö vstaeihyö  H.2.7;  25,  V.j.ss,  ^,29,  Vyt. 45i  —  ""^  a%ra  frakavB  mä  apakavB  . . maia.cim  'nyqm  (GPn.)  daxstanqm  V,  2. 29;  —  ahtnavaila  (sd.)  gäkanqm  .  . uilavaitTm  hsitlmca  , .  av5  yS  °nya  (näml. gä'^h)  srSvaydii  N.  46.  a)  Plur.  mit folg.  äi  'auch  die  andern' :   tl  mqm  ava%a
5372:•  j.  airime  Adv.  'still,  ruhig':  'me  giilani h!  nisAioagta  "still  soll  er  (sie)  an  seinem (ihrem)  Ort  sitzen  bleiben"  V.5.33,  i6.&.'^
10298:•  j«  g-  gätav-,  p.  gää'av-'>  m.,  n. I)  'Ort,  PlaU,  Stätte,  Stelle':  bamUta!- sva'a  paiti  'tusva  V.6.^$;  Yt  75.53; apqm..yi  para  akmät  hist?nta  ..  hamaya 'h'ö  (LS.)  Yt  13.  53;  55,  57;  —  ap5  -tav, (LS.)  rJmSiow?m  yavata  ,  .  "o  Wasser, verweilet  an  dem  Ort,  so  lange  .  .' ü'5.9;  —  nalca  .  .  *häu  nl  akmat  haca •taot  isalla  .  .  apasUtoit  (sd.)  P.  23 ;  Yt. J.17,  i6.t;   —   airime  i^A.)  °iBm  kl  nis-
16326:yaha  rämanS  ifästralie  Az.  7;  —  'ra  (statt NSm.)  nqma  ahmt  (näml.  AhM.)  Yt.  j. 14.  1)  von  Bergen:  vXspägarayS  aia.-
17716:ai.  prämanas-  Adj.  (AV.  2.  l8.  1 ;  Bloomtibu): ■provident'), /rajBOHaj-  Adj,  tieiter  geBlimmt'.
20536:'^rütihayete  rahtus  paiti^ranhayde  sraosS afyö  . .  hqtn.väiti  .  .  Yt  /O-  41 ;  J?.  16;  — sraoiaiea  . .  ratttvalca  . ,  'räiäz  Vr.  11.  6;  Y, ^5.12, 70.3,  Yt//.6;  vgl.  Yt.;o.ioo,  2)  in Verbindung  mit  raman-  (sd.,  auch  fdSt) s^ästra-:  'rahe  vourugaoyaatBil rämanasca sPäsirahe  Yt/o.o;  usw.  3)  Du.  in  Ver- bindung mit  aAura-  Du.^';  tala  nS  jamyat avaiähe  'ra  aAura  b)r»zanta  Yt.  /0. 1 1 3 ; 145;  —  aAura  'ra  b)r»zania  aüiya/aivAa Y.3.1 1 ; — aAuraäbya  'raiibya  b^rvzanbya.. Y./.ii.  Aa)  'raAe  {ataA.  ma)  hetsst  der 7.  Monat  im  Jahr:  %risat^m  ays^rimahe (sd.)  -raAe  anayraaqm  A._J.  10.  b)  *raA^ (näiuL  ayar»)  heisst  der  lö.  Monatstag: 'raAe  *vourugaoyaoteis . .  yasatahe  S.  1. 16; vgl.  2.16,  Y.  16.5.
25358:rämanivant-
25379:•  j.,  g.  räman-  n.  'Ruhe,  Friede':  'ma :fSstrtm  (sd.)  aiiihh  daiiihsui  a/rfttämi \.68.iy,  —  gavöi  ..  'mala  västr^utcä dagdyäi{sd.)  Y.jj.4;  —  Plur.:  aö^(sd.).. xs'aiinm^  avat  . .  yä  Auüiti/  'mqmcä dst  ". .  durch  die  er  (ihnen)  gutes  Wohnen und  Frieden  schaffen  kann"  Y.  29, 10;  — mi  *dr^vS.dfbIs  xrUräis'mqm  dänti  "wer sind  sie,  die  Frieden  schaffen  werden  vor den  grausamen  Z>r«(5genossen?"  Y.  48. 1 1 ; —  Auxidiräis  jfrarqm  (sd.)  .  .  rämqinca ais  dadäiü  Y.JJ.  8.'  A)  mit  cfditra- Adj.  (Triede,  der  schöne  Weide  gewährt") Name  einer  Gottheit*':  mihr^m  vouru.- gaoyaeitim  .  ,  'ma  ^äifram  Vr.  2.  9,  Y. 2,  3,  G.  /.  7,  V.J.  I ;  Y.  16.  5,  25.  5,  S.  2.  7, II;  —  'manS  ('manash)  s^ästrahe  V.  i.3, 22.  33,  72,  10,  Vr. /.  7,  Yl/O.o,  146,  Az.7, S.  /.  7,  *Vd.  g.  a)  rämans  s^astrahe (n'ämL  ayan)  heisst  der  31.  Monatstag: S./.31;  vgl.  S.2.  31,  Y,i6'.  5.
25382:•  j.  räman'ivant-  Adj.  'Ruhe,  Frie- den habend,  bringend':  saiavalsB . .  trirB
25386:Ableit.  aus  räman-;   wegen  des  i  s.  afsmani-
25531:KompA.(?l.  —  EI.7  —  Aus  ar.  *{t)ninia-.  — PiL  (zu  V.):  myacd  dän,  (lu  Y.):  tttnärämand. —  0  Statt  -Bfo,  S  3ÖÄ  32. j.,  g.  urun'z  1,  unmn:
28628:j  N.  42;  —  spa  .  .  stamantm  kl  mai  nyä- saym  .  .  dasimm  hl  gaeiTtn  .  .  Aöyum  kl \gaosfm  upa^Wfrfsayitt  .  .  doTimtn  Al 'paßyqm  .  .  kaoyqm  hl  paiiyqm  upa.- ksr^ntay^n  .  .  dum^mcil  Al  (zu  a)  upa.- '^lionsaym  V.  13. 30  ff,;  8.  40,  5. 1 7  ff.  (oft), 49,  H.2.  18,  36;  —  Aavatianö  (sd.)  äaityS gatuÜ  .  .  Aaffyaj  *Al^^  *nalmat  Omatars R  7p;  *7P'^  Yl/o.  ioo',  126,  Ä  38,  V. 79.  2;  —  nairika  .  .  airime  (sd.)  gätüm ^?  (fem,;  zu  ß)  nisAihalta  V.i6.&;g.^^ (mask,);  —  ahmi  nairi . .  b^m/ayän/i  fsd.) /l . ,  mänh^m^a  hvarfca  aamca  Al{za  a) bfr^Jaim  V, 7.  52;  —  sünahe  .  .  asti  sl haHn  ya%a  a^aurune  V,  13.  44;  44'; —  yS  ga'hanqm  *anu.tnaiti  (sd.)  *afm.- mainyete . .  anyS  vä  hl  (zu  a)  daAmB  srvth ga%ä  dalaiti  N.  25;  —  azdibji. .  *usäan3m h  i (Plnr.)  alat  k^rmaot  Y.  6. 50; — *Aixsa»e . .  drvatqm  .  .  anyqm   i4?(PIur.)  avarptqta
28980:Sp.  928  o.)  ist  weggelassen:  danys.Hli (sd.)  ile  vTse  afrJnämi  yahmat  h°  imti zaoira  y.SS.i^;  \t.  S.  4'.  '  b)  bei NomiDa";  o)  bei  verbalen  Substantiven: raiis  i&i.;  'decessum')  rm  A^  ariha  ztmat vaähs  k^nnaoili  Vt.  17.  20;  —  spmtat  h" mainyaot  aisam  ahr^m  ('origo')  FrW. 70,40;  —  yä  h"  daSnayUt  .  ,  apastüilis ('abdicatio'j  ^.4J-  ß)  bei  Raumwörtera: dsräl  Cprocul')  A'  ahmiil  nmänät  .  .  ays i^yejä . .*yeyenH yeAhe ..  Y.57,  14;  14';  — nSii . .  *dräjyS  ('longius')  *'iyeillm  framraomi (sd.)  . .  ä/rllim  yUnat  -4'  .  .  P.  7j;  — nazdyS  ('propius')  ahmi  . .  yaia  änha  k' *gaosaHöya  P.  2  V;  28;  —  airime  gätüm hs nUhthaüta  . .  *psr3ntanm  (sd.;  'seorsum') h'  anyanbyS  mazdayasna^byS  V.g.  33;  29; —  aiai  dräjö  ('quantam  longitudinem')  h* i!^ral\.  3. 16;  16^;  — yS  hn%rS.masar»h3m iS/wamm  ('viam  miUe  passuum')  h'  vizibys paräiti  V.  JJ.  18;  —  äiat  ('quantum*)  h' mtiya^bya  Y.i).  10;  8f.';  —  avavat  ('tan- tum')  h'  paourt-aiibya  yäha  %rigilim  V. 1M39;  II,  76;  — yd  *yujyastxm  (sd.)  h' gat^abyS  parätti  'v.  7^.  17;  N.  8,  <??(?), V,_j.  17*,  J(5'.4*,  17. 4«,  b)  im  gÄw. a)  bei  Verben  (bei  solchen  der  Bewegung nicht  bezeugt):  frg  ma  sl/iJ  (Sp.  1575  o.) "iiwahmut  *vaoca^hl  *mainy}us  h'  'üwä Siaiihn  "..  pronuntiare  ex  tuo  , tuum  os"  Y.  28. 11;  —  ysi  gSus  h'  iyävtl (sd.)  "qui  a  bove  (habitant  sva.)  stant' Y.  J7.  a";  —  ka^ü  . .  zarjm  (sd.)  laränl h'  xsmap''  ",  .  impetrem  a  vobis  (sva. per  vos)"  Y.  44-17;  —  a^byS  mazdh  .  . xsäi^rät  A'  paifi.mraot  ". .  per  Regnum (deum)  respondit"  Y.ya.  2;  —  sonst mit  'asa-  A  (als  Gottheit)  im  Sinn  von 'peri^nim,  As'o  juvante  (u.  dgl.)':  aiät  h'
29072:Part.  Praes.  'sich  hinsetzen  etwas  zu  tun sva.  sich  daran  machen,  anheben  etwas  zu lun'*>:  aat  tum  niUilöt^  (PraeL)  gähasca srävayB  apasla  vanuhls  yassmnS  "da  hobst du   an,   die    G.   aufzusagen   und   die  . . Wasser  zu  verehren"  H.a.  13;  —  ya  tat yal    haomahe    draonS    nighttlwtti    *nishi' oaiti''>   "die  sich  dran  macht  den  Anteil desÄ  zu  verzehren"  Y.  10. 1 5.        3)  'sitzen, sitzenbleiben,  sich  aufhalten'*':  airimeisd.) gatüm    ht  niskihaita    V.p.  33,  16.  &;  — asne  vay^anät  nishihaiti  "in  der  Nähe  des Kopfes   hält   sie  sich  auf  H.  2. 1";   — yat  aAmi  nmäneyat  mäzdayasnBii!  näirika li%ravaUi  . .  niihSiäl  "wenn  sich  in  dem Hause  ..  befindet"  V. /6'.  i. mit  vT,  viy:  s.  unter  viltäspa-, *i.  iiditti,  sädäyaü,  sidih  \  np.  mlaslan,  niSinad, sbaL  nindag,    nUta   (%' g6.  l);    lit  ädmi.     - Pu.!  niiaslan,  (firs  Kaus.);  nüämtan;  %,  noch No.  7,  —   ■)  So  nach  dem  Herkommen,  *gl. aber    vonRozwadowski   BB.  31.  247,    Bau. Grdr.»  /.  486,  504,    ferner  No.  3.    —    »)  In iiisanhasH  für  'nilatti,    S  36S.  48.  —  .1)  jAw. Aiia-  iit   die   ICamposiiionifoim   zu  ai.  sTda-, IF,  7.  107;  das  np.  Verbum  enthält  altes  /.  — O  S  sS-   I.  -  s)  S  -^9.   ~   *'  Vgl  ifl*-  I.  — 7)  NA.  HilAai',    i.  Var.     Pü.:  3 yavisn  dänil. Sä, :    ihädanäya    tüvedayaü.      MlLU    Lesnng ZDMG.  J(5.  143  ist  mir  gani  Unverstand! ich.  — B)  Vgl.  die  Bedeutung  des  Verb*  im  Bai.  — 9)  An    der   Parallelilelle  H.  7.  20  steht  han-

=== PHD rasan/ramisn
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:852:rāyēnišn,
PHD.txt:3322:ram warān, warrag.
PHD.txt:3323:rampant zandag.
PHD.txt:4953:rasan
PHD_mackenzie.txt:4326:ram [l'm I M r)m, N -] peace; cal. 21st day.
PHD_mackenzie.txt:4327:ram(ag) [lm(h ) I P rm, N ram(a)] herd, flock.
PHD_mackenzie.txt:4328:ramenidan, ramen-       '            [l'myn-ytn l I M r)myn-] give peace, pleasure.
PHD_mackenzie.txt:4329:ramiAn [l'mln ' I M r)myln, N ramil] peace, ease, pleasure.
PHD_mackenzie.txt:4344:rasan [lsn' IN.....,] rope.
PHD_mackenzie.txt:5623:xwarasan [hwPs'n'  '      I M xwr)s)n, N .......] sunrise, east.
PHD_mackenzie.txt:9324:ram
PHD_mackenzie.txt:9329:ramag                          ,~      rozbanag
PHD_mackenzie.txt:9441:rasan                       ,~          rastih                 -'U~
PHD_mackenzie.txt:11993:xwarasan                 ,~"'"         uzdcsparist     \~~~
```


## [2026-09-14T01:27:33.863Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 420 -l 420 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg420\nls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg420.png",
 "description": "Render PDF page 420"
}
```


### [2026-09-14T01:27:35.569Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66620 Sep 13 21:27 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg420.png
```


## [2026-09-14T01:27:44.060Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 420 -l 420 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg420b\nls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg420b.png; ls site/pages/420.jpg 2>/dev/null",
 "description": "Render page 420 at 300dpi"
}
```


### [2026-09-14T01:27:46.549Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 72677 Sep 13 21:27 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg420b.png
site/pages/420.jpg
```


## [2026-09-14T01:27:48.132Z] TOOL CALL #42: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/420.jpg"
}
```


### [2026-09-14T01:27:48.158Z] TOOL RESULT

```

```


## [2026-09-14T01:28:14.027Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('leaves',len(leaves))\nimport re\n# find leaf containing rasana / rekendi\nfor i,l in enumerate(leaves):\n    if 'rekendi' in l or ('rasanā' in l) or ('raśanā' in l) or 'rahhinza' in l:\n        print('HIT leaf',i)\n        print(l[:1500])\n        break\nEOF",
 "description": "Walde-Pokorny Bd2 rek- binden"
}
```


### [2026-09-14T01:28:15.171Z] TOOL RESULT

```
leaves 725
```


## [2026-09-14T01:28:17.674Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\ndef leafof(line_hits, name):\n    pass\n# find leaves containing the raman- entry\nfor i,l in enumerate(leaves):\n    if \"räman-  n.  'Ruhe\" in l or \"räman- n. 'Ruhe\" in l:\n        print('raman leaf',i); print(re.findall(r'\\b1[0-9]{3}\\b', l)[:12])\n    if \"airime  Adv\" in l:\n        print('airime leaf',i); print(re.findall(r'\\b1?[0-9]{2,4}\\b', l)[:12])\nEOF",
 "description": "Bartholomae column numbers"
}
```


### [2026-09-14T01:28:18.838Z] TOOL RESULT

```
airime leaf 137
['44', '45', '11', '190', '143', '25', '146', '166', '27', '24', '583', '263']
raman leaf 833
[]
```


## [2026-09-14T01:28:26.892Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (136,137,138,832,833,834):\n    l=leaves[i]\n    print('--- leaf',i, repr(l[:200]))\nEOF",
 "description": "BRT leaf headers"
}
```


### [2026-09-14T01:28:27.990Z] TOOL RESULT

```
--- leaf 136 "':  äahms  zaota  dahmS  upa.sraolärü vispe  ratu/ryö  tanupirii^ö  zaota  tarnt- p>r3%5  upü.sraotltrS  vupe  '/ryüti.^i);  — yai  ig  däiti  dalätH  ^rafufrÜ . .  yesi  aal hSnDit  däiti  daoäiti  '"
--- leaf 137 "a-  Adj.  'keinen  Kampf  führend, nicht  kämpfend':  'na  F.  7.\nPü.:  apatkär.\n•  j.  ar«m,  g.  arvm  Adv.  'recht,  passend, wie  sichs  gehört':  y3cä  alä  arttau!  °r}m *vaiidyäiisd.)\\.44.S;—'K"
--- leaf 138 'ir  keinen  im  Stich lassen"  Y.Ö5.7;  7.\nZum  V.  ra/i!-;  vgl.  V/H.  Gr.»  %  irSS  <\'\'\'>■  — Pü.;  reiilär.  —  \'»  Die  S  4\'^  vorgeschlagene Fassung  ist  auch  möglich,  dann  zu  S  209.  5.'
--- leaf 832 '  S  Bi  i  Sktmazd.\n•  p.  *r^d-  f.  \'ratio,  causa\':  avahya-rädix {LS.)  sbes.\nZum  V.  räd:  —  Vgl.  np.  rSi  \'wegen\',  ksl. tadi  \'wegen,  x^^"\'-\n•  g.  räda-,  j.  rä8a-  m.  \'Fürsorger\':  yi'
--- leaf 833 '  wiilc-\ndby  Google\nI5»3\nrä9inan-\nrämanivant-\n1S»4\n•  j.  rädman-  Adj. mit  —  (Gen.),  Anhänger\':  yS yasnS  aojanS  aiahe  \'ma  (NS.)  jlslayamnd ya^wa  gai\'hä  asahe  tmrrjinte  "wer  .  . sich  '
--- leaf 834 'oHUfyäk kkädyasya  svädam  vindattii)  beruht  auf  »er- kehrter  Deutung  des  Beiworts.  Yt.  15  hat  mit Räman  nichts  zu  schaffen  (,  s.  die  Überschrift in  Fl),  nach  meiner  Meinung  auch'
```


## [2026-09-14T01:28:35.977Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nimport re\nfor i in range(130,142):\n    l=leaves[i]\n    m=re.findall(r'\\n\\s*(\\d{2,4})\\s*\\n', l[:400])\n    print(i, m, repr(l[:80].replace('\\n','|')))\nEOF",
 "description": "BRT airime column"
}
```


### [2026-09-14T01:28:37.109Z] TOOL RESULT

```
130 [] 'Pü.: aiapt  Sflisn.  —  D  iSt  und  Konttr.  s.  RV.  1. 17.  S,  /.  105.  3-|'
131 ['177', '178'] "^qm  hl  'Iqm  altahmifi  naire frabi!ray?n  V.5.39;  ig.id;  —  zur5.bir»ta ,'i"
132 [] 'he..  timänS.paite\'^xa Hilfe!  Hausherr"  V./Ä19;  31,22.  LS. avöaüs  Inf.  sbe'
133 [] " airyd.x^ii>a(  ka>a  garöit x^anvanhtn  'vt  gairjm  YLÄ6;  H.  2.  i6^ Yt.5.85"
134 [] 'm."_va-)  ^Mi>ra- feindlich\':  yat  a\'^ra  para./asaili  ..  ya%rii daiAMvü  \'ny'
135 [] "IF.  ts.  :o6.  —  >*)  Pü.:  undeut- lich, wohl  Transskr. •  j..  g.  'ar-  V."
136 [] "':  äahms  zaota  dahmS  upa.sraolärü vispe  ratu/ryö  tanupirii^ö  zaota  tarnt"
137 [] "a-  Adj.  'keinen  Kampf  führend, nicht  kämpfend':  'na  F.  7.|Pü.:  apatkär."
138 [] 'ir  keinen  im  Stich lassen"  Y.Ö5.7;  7.|Zum  V.  ra/i!-;  vgl.  V/H.  Gr.»  %'
139 [] "  wohl  eher  ar.  *aril-  :  'arl-  (im  Komp.),  s. BthL.  IP~./.  70.  VgVdar"
140 [] "(Anders  Justi  NB.  ii.)|•  j.  arvduä-  n.  'Verletzung,  Hieb',  im Strafgese"
141 [] "  Yt/2.8.  lYt.5. 90:  lies  antart.ari'jitn^|KompE.  (s.  nHflf^S/) ;  Ableit. "
```


## [2026-09-14T01:28:50.183Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nl=leaves[137]\ni=l.find('airime')\nprint(repr(l[max(0,i-300):i+600]))\nEOF\necho \"=== grep hurama / paitiraman\"\ngrep -n \"hu.rama\\|huräman\\|hurämsn\\|paiti.räman\\|paitiräman\\|paiti.raman\" BRT.txt | head -20",
 "description": "BRT airime entry and compounds"
}
```


### [2026-09-14T01:28:51.344Z] TOOL RESULT

```
'  dem  Weg  wie  die Hure"  V.y.4S.\nZum  V.  ray:  —  Vgl.  aviirila,  ai-wUrifim.  — Pü.;  pa  ras  riyai\');  dam  die  Bern.;  ai/  ki ilÖH  gdaiel  iu  andat  x\'tslhä  gäi  fl/j/  5  ma-f  «.- tiiiitüt.  —  »)  Statt  r  d  k  ist  wohl  r  d  d  lu lesen,  d.  i.  riyel  (=  np.  riyad).\n•  j.  airime  Adv.  \'still,  ruhig\':  \'me  giilani h!  nisAioagta  "still  soll  er  (sie)  an  seinem (ihrem)  Ort  sitzen  bleiben"  V.5.33,  i6.&.\'^\n•)  Pu.  hat  fa  an  i  armettän  gäk  "an  dem  Ort der  still  stehenden",  d.  L  derer,  die  sich  nicht bewegen,  sich  ruhig  verhallen  sollen,  damit  sie andre   nicht   verunreinigen ;    vgl.  artaarslä-  und\nauch  zu  Y.  62.  3.  Später  wurde  Tiir  sie  ein  be- sonderer Raum  als  Aufenthalt  bestimmt  und  die darin  untergebrachten  werden  selber  armeil  ge- nannt, vgl.  West  SBE.  24-  4ä.  Dst.  ZA.  2.  xii, XIV,  83;  ferne'
=== grep hurama / paitiraman
```


## [2026-09-14T01:29:05.397Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"huräm\\|hu.räm\\|hurām\\|hu.rama\\|pati.räm\\|padräm\\|pedräm\\|padrām\" BRT.txt HUB.txt HRN.txt NYB_vol2_glossary.txt 2>/dev/null | head -20\necho \"=== HUB xurram\"; grep -n -i \"hurram\\|xurram\\|chorram\\|churram\" HUB.txt | head -10\necho \"=== NYB ram\"; grep -n \"^rām\\|^rāmišn\\|^ramak\\|rāman\" NYB_vol2_glossary.txt | head -10",
 "description": "Search for hu-rama, paiti-raman, xurram"
}
```


### [2026-09-14T01:29:05.503Z] TOOL RESULT

```
HRN.txt:10645:in hu[ramak, hii/t, hu\tu/s, hu\xtm etc.
HUB.txt:1891:Fr. Muller (WZKM. 7, 373) auf iran. ^hu-rama-
NYB_vol2_glossary.txt:2072:hu-ramak [hwlmk'] having good herds of cattle 5076, with the gl. ku ramak 4 apdrik veh dānēt dästan ‘that is: it knows how to breed other cattle [than sheep, ete.] in the best way’. — V. ramak. Paz. hurama; translates Av. (1857) hvq0wa-.
NYB_vol2_glossary.txt:3228:ramak herd 50°. — Arm lw. eramak; NP ramah, ramak. V. hu-ramak.
=== HUB xurram
1887:sich xurram = x^aram JRAS. 1894, 459 allerdings
1890:entstanden wie narr aus nar, so kann xurram mit
7641:zd. ^hujasta-; xurram^) *fr5hlich*, s. oben p. 55.
9303:vielleicht auch in xurram *fr<5hlich* H. 479, oben p. 55. —
10806:xurram 55.
=== NYB ram
3228:ramak herd 50°. — Arm lw. eramak; NP ramah, ramak. V. hu-ramak.
3230:rāmēnītār [’mynyt’l]] one who brings joy, peace, satisfaction (etc.), pl. cas. obl. ~-dn of near relatives, “my dear ones”
3232:ramišn [l’msn] pleasure, joy, peace, sat- isfaction 47%, 632 ete. — Av. (1511) ram- ‘to repose’, caus. rāmaya- ‘to calm’, (1524) rāman- ‘peace’; MPrthPrs r’mysn ‘peace’.
3236:rām-šahr [Pmátr'] (ruler) whose realm is peace, who maintains peace in his realm, epithet of Vistasp 245.
5295:ram-, rāmaya-, rāman: rāmišn
5296:rāman-: hu-rām
```


## [2026-09-14T01:29:12.913Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1875,1900p' HUB.txt\necho \"=== HUB leaf/page\"; python3 -c \"\ntxt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nprint('leaf', '\\n'.join(txt.split('\\n')[:1891]).count('\\f'))\"",
 "description": "Hübschmann xurram"
}
```


### [2026-09-14T01:29:14.182Z] TOOL RESULT

```
aus xar 'Esel' und cang *Kralle' zusammengesetzt er-
scheint.
476. Lies arm. xrat (fur xart),
477. Dazu kurd. vird, Mrs, hire 'Bar ZDMG. 38, 93.
478. Auf Grund der Pazendlesungen des Min. und Shk
setze ich x^arsand als Pehleviform an und lehne
die so wie so unsichere Etymologie Darmesteters
(= hu-rasant' gut-kommend' ab.)
*) Arsao. phi. *x^ataS, sp&ter phi. x^atai, paz. x^adai.- 55 —
479. Np. xurr am 'ajigenehm, lieblich, frOhlich* kannselbst-
verstandlich nicht = skr. sugramor- sein, da iV im Pers.
zu svj nicht zu rr wird. Auf ein skr. "^svarnama- liesse
sich xurram = x^aram JRAS. 1894, 459 allerdings
zuruckfuhren, doch schwebt dies ganz in der Lnft. 1st
xtirram aus (dem von Vullers angefuhrten) xuram
entstanden wie narr aus nar, so kann xurram mit
Fr. Muller (WZKM. 7, 373) auf iran. ^hu-rama-
sich wohl freuend* zuruckgefiihrt werden^), vgl. skr.
suramya-y suramai^iya'^i suraman- erg5tzlich'.
480. Vgl. got. hrukyan *krahen', gr. ic^avyrj 'Geschrei* von
Wrzl. krug^ (Feist, Grundr. der got. Etym. Nr. 286).
481. Wo findet sich phi. xrust u. s. w.? Ich finde fiir zd.
xraoBy^iti vd. 15, 17 (Spiegel) im Phi. xr»iYat (falsch
fiir xr^smU) Phi. Vd. p. 175, Z. 16, fiir xraosentqm ys.
52, 8 (Spiegel): iphl. xrosisnu-Dmand, fUr xraosydtara-
vd. 13, 22 (Spiegel): phi. xrdsUar (lies xrd^taktar)
=== HUB leaf/page
leaf 65
```


## [2026-09-14T01:29:25.970Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -rn \"پدرام\" MON_part1.txt MON_part2.txt FSF_pages.txt FRS_pages.txt 2>/dev/null | head -10\necho \"=== BQT v1 pedram\"; grep -n \"پدرام\" BQT_v1_pages.txt | head -5\necho \"=== ARY ram\"; grep -n \"رام\\b\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== ARY latin index\"; grep -n -i \"^RAM\\|RASAN\\|^REM\\|^REK\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Search pedram and Aryanpur"
}
```


### [2026-09-14T01:29:26.094Z] TOOL RESULT

```
FRS_pages.txt:13916:‫تبول کرد دل از حداث ناپدرام‬
FRS_pages.txt:14304:‫کریستنش چه باید" که شد جهات پدرام |‬
FRS_pages.txt:14322: ‫‪ - ۱‬ن پ‪۰‬درام جایی بود خرم و دلگدای » چ ‪ :‬پدرام خرم باشد باعلسی یا خانة با‬
FRS_pages.txt:14324:                                   ‫جایی کهخرّم بود آنر! پدرام خوانند ؛س ب‬
FSF_pages.txt:6777:‫که‌گیتی تازه بود و روز پدرام‬                             ‫ازین زشت پتیاره چندین چه باک‬
FSF_pages.txt:6804:              ‫کهمن رفتنی‌ام به دیگر سرای‬                                             ‫پدرام‬
FSF_pages.txt:6815:‫پیام پسرش قباد شیرویه را می‌دهد‪ .‬به‬              ‫مرا دل درشتست و پدرام نیست‬
FSF_pages.txt:11569:         ‫سیاوش چو نزدیک ایوان رسید‬                 ‫مرا دل درشتست و پدرام نیست‬
MON_part1.txt:21597:پدرام: سعنهه< [- پدرام] (ص.) خوش؛ 
MON_part1.txt:29645:پدرام: (-(۳2)6 (ص‌ مر .) آراسته» نیکو. 
=== BQT v1 pedram
16249:۴ - جلد بشکول دان و خوش پدرام بادرم شد رعیتان را نام . « ازفرهنگستظوم *.
17947:۱ - باين معانی» رك: پدرام.
=== ARY ram
264:می‌شوند و زبانهای پیرامون بیشتر محافظه کارند و دارای واژه‌های کهن تراند. مثلاً زبان فرانسه‌ی رایج
266:در ایالت کبک در کانادا (یک زبان پیرامون) از زبان فرانسه‌ی رایج د رکشور فرانسه کمتر تغیی رکرده
268:حاشیه یا پیرامون حاوی واژه‌هابی هستند که قبل از خروج از گهواره جزو زبان هند و اروپایی
291:همریشه‌اند می‌توان نتیجه گرفت که آنان در رام کردن اسب و استفاده از ترابرهای چرخدار پیشگام
358:اروپایی تا حدود ۲۵۰۰ سال قبل از میلاد رواج داشته‌اند وی ورود اقرام هند و اروپایی از شمال
=== ARY latin index
1393:RAMAT: tT OHEN (SLOVAK) 51 yLah
1425:RAMTIS, RIMTI, :(LITHUANIAN) gl) ARAMITAN, PAHLAVD ($3,
1426:RAMDITI RAMISHN, RAM, RAMENITAN
1427:RAMS (LATVIAN) (33) gig RAM, RAM :(TOKHARIAN A) A 5,55
1539:RAMAT: 126 ye as
2359:RAMAT: 4 BARNHART: (EQUINE) 338,
2611:RAMAT: 45]: IMMORTALIS AAATINY yg 48
3437:RAMAT: 4 BEREN, BOREN
4833:RAMAT: a FEA, HOLD ENGLISH) of gJ&:
5250:RAMAT: 138 PEIROKSES X(GREEK) siy
```


## [2026-09-14T01:29:38.493Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-14T01:29:38.622Z] TOOL RESULT

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


## [2026-09-14T01:29:44.294Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D9%86\" \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%85\" \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%A7%D9%85\" \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D9%85\" \"https://en.wiktionary.org/wiki/rest\" \"https://www.etymonline.com/word/rest\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 420, roots Rek/Reg 2 and Rem: rasan, ram, aram, xorram, English rest\" ; done",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:29:48.714Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0c9919c3ce3d9a3a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b9457a2f281e5f6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e964839f7de29a89.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4d82e3a553ca26df.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/81e50066f3651b69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4d6454727cd9c5af.txt
```


## [2026-09-14T01:29:51.663Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 0c9919c3ce3d9a3a 3b9457a2f281e5f6 e964839f7de29a89 4d82e3a553ca26df; do echo \"######## $f\"; grep -n -A25 \"Etymology\" $f.txt | head -70; done",
 "description": "Read Wiktionary etymologies"
}
```


### [2026-09-14T01:29:52.675Z] TOOL RESULT

```
######## 0c9919c3ce3d9a3a
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Declension 
69-
70- 1.2.2 
71- Derived terms 
72-
73- 1.3 
74- Verb 
75-
76- 1.3.1 
77- Conjugation 
78-
79- 1.4 
80- Noun 
81-
82- 1.4.1 
83- Declension 
84-
85- 1.5 
86- References 
87-
--
105: Etymology 
106-
107- 3.2 
108- Pronunciation 
109-
110- 3.3 
111- Noun 
112-
113- 3.3.1 
114- Descendants 
115-
116- 3.3.2 
117- References 
118-
119- 4 
120- Urdu 
121-
122- Toggle Urdu subsection 
123-
124- 4.1 
125: Etymology 
126-
127- 4.2 
128- Pronunciation 
129-
130- 4.3 
131- Noun 
132-
133- 4.3.1 
134- Derived terms 
135-
136- 4.4 
137- References 
138-
139- Toggle the table of contents 
140-
141- رسن 
142-
143- 8 languages 
144-
145- বাংলা 
146- فارسی 
147- Magyar 
######## 3b9457a2f281e5f6
65: Etymology 1 
66-
67- 1.2.1 
68- Verb 
69-
70- 1.2.1.1 
71- Conjugation 
72-
73- 1.3 
74: Etymology 2 
75-
76- 1.3.1 
77- Verb 
78-
79- 1.3.1.1 
80- Conjugation 
81-
82- 1.4 
83: Etymology 3 
84-
85- 1.4.1 
86- Noun 
87-
88- 1.4.1.1 
89- Declension 
90-
91- 1.5 
92- References 
93-
94- 2 
95- Persian 
96-
97- Toggle Persian subsection 
98-
99- 2.1 
100- Pronunciation 
101-
102- 2.2 
103: Etymology 1 
104-
105- 2.2.1 
106- Adjective 
107-
108- 2.2.1.1 
109- Derived terms 
110-
111- 2.2.2 
112- Descendants 
113-
114- 2.3 
115: Etymology 2 
116-
117- 2.3.1 
118- Proper noun 
119-
120- 2.4 
121- References 
122-
123- 3 
124- Punjabi 
125-
126- Toggle Punjabi subsection 
127-
128- 3.1 
129: Etymology 
130-
131- 3.2 
132- Proper noun 
133-
134- 4 
######## e964839f7de29a89
87: Etymology 1 
88-
89- 3.1.1 
90- Noun 
91-
92- 3.1.1.1 
93- Descendants 
94-
95- 3.1.2 
96- Further reading 
97-
98- 3.2 
99: Etymology 2 
100-
101- 3.2.1 
102- Proper noun 
103-
104- 3.2.1.1 
105- Descendants 
106-
107- 3.2.2 
108- Further reading 
109-
110- 4 
111- Persian 
112-
113- Toggle Persian subsection 
114-
115- 4.1 
116- Pronunciation 
117-
118- 4.2 
119: Etymology 1 
120-
121- 4.2.1 
122- Adjective 
123-
124- 4.2.1.1 
125- Inflection 
126-
127- 4.2.2 
128- Noun 
129-
130- 4.2.3 
131- Proper noun 
132-
133- 4.2.4 
134- Derived terms 
135-
136- 4.2.5 
137- Related terms 
138-
139- 4.2.6 
140- Descendants 
141-
142- 4.2.7 
143- References 
144-
--
146: Etymology 2 
147-
148- 4.3.1 
149- Proper noun 
150-
151- 4.3.1.1 
152- Derived terms 
153-
154- 5 
155- Sindhi 
156-
######## 4d82e3a553ca26df
79: Etymology 1 
80-
81- 2.1.1 
82- Pronunciation 
83-
84- 2.1.2 
85- Verb 
86-
87- 2.1.2.1 
88- Conjugation 
89-
90- 2.2 
91: Etymology 2 
92-
93- 2.2.1 
94- Pronunciation 
95-
96- 2.2.2 
97- Verb 
98-
99- 2.2.2.1 
100- Conjugation 
101-
102- 2.3 
103: Etymology 3 
104-
105- 2.3.1 
106- Pronunciation 
107-
108- 2.3.2 
109- Noun 
110-
111- 3 
112- Ottoman Turkish 
113-
114- Toggle Ottoman Turkish subsection 
115-
116- 3.1 
117: Etymology 
118-
119- 3.2 
120- Pronunciation 
121-
122- 3.3 
123- Adjective 
124-
125- 3.3.1 
126- Descendants 
127-
128- 3.4 
129- Proper noun 
130-
131- 3.4.1 
132- Descendants 
133-
134- 4 
135- Persian 
136-
137- Toggle Persian subsection 
138-
139- 4.1 
140: Etymology 
141-
142- 4.2 
143- Pronunciation 
144-
145- 4.3 
146- Adjective 
147-
148- 4.3.1
```


## [2026-09-14T01:29:58.748Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 0c9919c3ce3d9a3a 3b9457a2f281e5f6 e964839f7de29a89 4d82e3a553ca26df; do echo \"######## $f\"; grep -n \"Proto-Iranian\\|Middle Persian\\|Proto-Indo-European\\|Sanskrit\\|Avestan\\|Old Persian\\|Hasandust\\|borrowed\" $f.txt | head -25; done",
 "description": "Grep Wiktionary etymology lines"
}
```


### [2026-09-14T01:30:01.264Z] TOOL RESULT

```
######## 0c9919c3ce3d9a3a
216: Borrowed from Middle Persian [script needed] ( lsn' /⁠rasan⁠/ , “ rope ” ) , see Classical Persian رسن ( rasan ) . Also found as Hebrew רֶסֶן ( resen ) and rarely as Jewish Literary Aramaic רִסְנָא ( risnā ) .
1000: Inherited from Middle Persian [script needed] ( lsn' /⁠rasan⁠/ , “ rope ” ) , from Parthian [script needed] ( rasan , “ rope ” ) , from Proto-Iranian *racanáH , from Proto-Indo-Iranian *raćanáH , from the root *rać- . Cognate with Sanskrit रशना ( raśanā́ ) and Old Armenian առասան ( aṙasan ) , an Iranian borrowing.
1071: Borrowed from Classical Persian رَسَن ( rasan , “ rope; string ” ) . Doublet of رَشْمِی ( raśmī ) and رَشْنا ( raśnā ) (borrowings from Sanskrit र॒श्मि ( raśmí ) and र॒श॒ना ( raśanā́ ) respectively).
1108: Categories : Arabic terms borrowed from Middle Persian 
1109: Arabic terms derived from Middle Persian 
1129: Persian terms inherited from Middle Persian 
1130: Persian terms derived from Middle Persian 
1132: Persian terms inherited from Proto-Iranian 
1133: Persian terms derived from Proto-Iranian 
1143: Urdu terms borrowed from Classical Persian 
1151: Hidden categories: Requests for native script for Middle Persian terms 
1158: Sanskrit terms with non-redundant manual transliterations 
1159: Sanskrit terms with redundant transliterations 
######## 3b9457a2f281e5f6
1621: Inherited from Middle Persian 𐫡𐫀𐫖 ( lʾm /⁠rām⁠/ ) , from Proto-Iranian *rām- , from Proto-Indo-European *h₁rem- ( “ to rest ” ) . Cognate with آرام ( ârâm ) .
1649: From Sanskrit राम ( rāma ) , most likely via Hindustani ( Hindi राम ( rām ) / Urdu رام ( rām ) ). Doublet of رامین ( râmin ) .
1658: a male given name , Ram and Rāma , from Sanskrit, of Hindu usage 
1673: Learned borrowing from Sanskrit राम ( rāma ) .
1685: a male given name , Ram and Rāma , from Sanskrit, of Hindu usage 
1698: From Sanskrit राम ( rāma ) . Cognate to Bengali রাম ( ram ) , Punjabi رام ( rām ) / ਰਾਮ ( rām ) , Marathi राम ( rām ) , Nepali राम ( rām ) .
1714: a male given name , Ram and Rāma , from Sanskrit, of Hindu usage 
1768: Persian terms inherited from Middle Persian 
1769: Persian terms derived from Middle Persian 
1770: Persian terms inherited from Proto-Iranian 
1771: Persian terms derived from Proto-Iranian 
1772: Persian terms inherited from Proto-Indo-European 
1773: Persian terms derived from Proto-Indo-European 
1776: Persian terms borrowed from Sanskrit 
1777: Persian terms derived from Sanskrit 
1778: Persian terms borrowed from Hindustani languages 
1780: Persian terms borrowed from Hindi 
1782: Persian terms borrowed from Urdu 
1790: Persian male given names from Sanskrit 
1791: Punjabi terms borrowed from Sanskrit 
1792: Punjabi learned borrowings from Sanskrit 
1793: Punjabi terms derived from Sanskrit 
1802: Punjabi male given names from Sanskrit 
1803: Urdu terms inherited from Sanskrit 
1804: Urdu terms derived from Sanskrit 
######## e964839f7de29a89
466: From Proto-Iranian *ā-rām(a)- , from *ā- ( “ ad- ” ) + *rām- ( “ calm ” ) , from Proto-Indo-European *h₂éd ( “ at ” ) + *h₁rem- ( “ to rest ” ) . [ 1 ] 
609: Proto-Indo-European *h₂éd 
611: Proto-Indo-European *h₁rem- 
675: Proto-Indo-European *h₂éd 
677: Proto-Indo-European *h₁rem- 
682: Borrowed from Classical Persian آرَام ( ārām ) , ultimately from Proto-Indo-European *h₁rem- .
751: Persian terms derived from the Proto-Indo-European root *h₁rem- 
753: Persian terms derived from Proto-Indo-European 
754: Persian terms derived from the Proto-Indo-European word *h₂éd 
755: Persian terms inherited from Proto-Iranian 
756: Persian terms derived from Proto-Iranian 
768: Sindhi terms derived from Proto-Indo-European 
769: Sindhi terms derived from the Proto-Indo-European word *h₂éd 
770: Sindhi terms derived from the Proto-Indo-European root *h₁rem- 
771: Sindhi terms borrowed from Classical Persian 
777: Urdu terms borrowed from Classical Persian 
778: Urdu terms derived from the Proto-Indo-European word *h₂éd 
780: Urdu terms derived from Proto-Indo-European 
781: Urdu terms derived from the Proto-Indo-European root *h₁rem- 
782: Urdu terms inherited from Proto-Indo-European 
787: Yidgha terms borrowed from Urdu 
######## 4d82e3a553ca26df
1051: From Persian خرم ( xorram ) , from Middle Persian [script needed] ( hwlm /⁠huram⁠/ ) .
1089: From Middle Persian [script needed] ( hwlm /⁠huram⁠/ ) .
1179: Ottoman Turkish terms borrowed from Persian 
1181: Ottoman Turkish terms derived from Middle Persian 
1189: Persian terms inherited from Middle Persian 
1190: Persian terms derived from Middle Persian 
1208: Requests for native script for Middle Persian terms
```


## [2026-09-14T01:30:20.034Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81rem-\" \"https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A4%B6%E0%A4%A8%E0%A4%BE\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%AF%D8%B1%D8%A7%D9%85\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/rastu\"; do python3 tools/fetch_source.py \"$u\" --note \"page 420 roots Rek/Reg 2, Rem: PIE h1rem-, Skt rasana, pedram, PWGmc rastu\"; done\necho \"=== etymonline rest\"; grep -n -i \"rest\" data/verification/sources/web/4d6454727cd9c5af.txt | head -20",
 "description": "Fetch more sources, read etymonline"
}
```


### [2026-09-14T01:30:24.487Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9eb07b4411765933.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0b7f5161ffc24357.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/95b308d9458ea2b0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d1b9006714c3c9a1.txt
=== etymonline rest
1:URL: https://www.etymonline.com/word/rest
4:TITLE: Rest - Etymology, Origin & Meaning
6:Rest - Etymology, Origin & Meaning 
21: Origin and history of rest 
23: rest (n.1) 
25: [sleep, repose, slumber] Old English ræste, reste "rest; a bed or couch; intermission of labor; mental peace, state of quiet or repose," from Proto-Germanic *rasto- (source also of Old Saxon resta "resting place, burial-place," Dutch rust , Old High German rasta , German Rast "rest, peace, repose"), a word of uncertain origin.
27: The original prehistoric signification of the Germanic noun was perhaps a measure of distance; compare Old High German rasta , which in addition to "rest" meant "league of miles," Old Norse rost "league, distance after which one rests," Gothic rasta "mile, stage of a journey." If so, perhaps a word from the nomadic period. But if the original sense was "repose," the sense was extended secondarily to "distance between two resting places."
29: Sense of "absence or cessation of motion" is from late 15c. The meaning "that on which anything leans for support, thing upon which something rests" is attested from 1580s, with specific senses developing later. In music, "an interval of silence," also the mark or sign denoting this, 1570s.
31: At rest "dead" is from mid-14c., on the notion of "last rest, the big sleep, the grave." The roadside rest stop for drivers on busy highways is by 1970. The colloquial expression give (something) a rest "stop talking about it" is by 1927, American English.
40: rest (n.2) 
42: "remainder, that which is left after a separation," early 15c., from French reste "remnant," from rester "to remain" (see rest (v.2)). Meaning "others, those not included in a proposition" is from 1530s.
45: rest (v.1) 
47: [to repose; to cease from action] Middle English resten , from Old English ræstan , restan "take repose by lying down; lie in death or in the grave; cease from motion, work, or performance; be still or motionless; be undisturbed, be free from what disquiets; stand or lie as upon a support or basis," from Proto-Germanic *rastejanan (source also of Old Saxon restian , Old Frisian resta , Middle Dutch rasten , Dutch rusten , Old High German reston , German rasten , Swedish rasta , Danish raste "to rest"), a word of doubtful etymology (compare rest (n.1)).
49: Transitive senses "give repose to; lay or place, as on a support or basis" are from early 13c. Meaning "cease from, have intermission" is late 14c., also "rely on for support." In law, "voluntarily end the presentation of evidence to allow presentation of counter-evidence by the opposing party," by 1905. Related: Rested ; resting .
51: To rest up "recover one's strength" is by 1895, American English. To rest in "remain confident or hopeful in" is by late 14c., biblical. Resting place "place safe from toil or danger" is from mid-14c.
53: Rest signifies primarily to cease from action or work, but naturally by extension to be refreshed by doing so, and further to be refreshed by sleeping. 
55: rest in a standing position. [Century Dictionary]
57: rest (v.2) 
59: [be left, remain] mid-15c., "remain, continue in existence," from Old French rester "to remain, stay" (12c.), from Latin restare "stand back, be left," from re- "back" (see re- ) + stare "to stand" (from PIE root *sta- "to stand, make or be firm").
61: It has been largely confused and partly merged with rest (v.1), which, however, is Germanic.
```


## [2026-09-14T01:30:35.993Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### PWGmc rastu\"; grep -n -i \"Proto-Germanic\\|Etymology\\|Proto-Indo-European\\|uncertain\" d1b9006714c3c9a1.txt | head -15\necho; echo \"### PIE h1rem-\"; grep -n -i \"Avestan\\|Sanskrit\\|Persian\\|Root\\|rest\\|Descendants\\|Ancient Greek\\|Gothic\\|Lithuanian\" 9eb07b4411765933.txt | head -40\necho; echo \"### Skt rasana\"; grep -n -i \"Etymology\\|Proto-Indo\\|rope\\|girdle\\|cord\" 0b7f5161ffc24357.txt | head -20\necho; echo \"### pedram\"; grep -n -i \"Etymology\\|Middle Persian\\|Proto-Iranian\\|pleasant\" 95b308d9458ea2b0.txt | head -20",
 "description": "Read fetched reconstruction pages"
}
```


### [2026-09-14T01:30:36.119Z] TOOL RESULT

```
### PWGmc rastu
62: Etymology 
140: Etymology
143: From Proto-Germanic *rastō .
256: Categories : Proto-West Germanic terms inherited from Proto-Germanic 
257: Proto-West Germanic terms derived from Proto-Germanic 

### PIE h1rem-
62: Root 
126: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
131: Root
136: to rest 
141: Terms derived from the Proto-Indo-European root *h₁rem- (38 c, 0 e) 
143: *h₁rém-e-ti ( thematic root present ) 
144: Proto-Indo-Iranian: *Hrámati ( see there for further descendants )
148: Lithuanian: ri̇̀mti (present ri̇̀mstu )
158: Sanskrit: रामयति ( rāmáyati ) 
161: Avestan: 𐬭𐬁𐬨𐬀𐬌𐬌𐬈𐬌𐬙𐬌 ( rāmaiie i ti ) 
164: Proto-Germanic: *remaz ( see there for further descendants )
170: Lithuanian: ramùs 
178: Persian: آرام ( ârâm , “ quiet, calm ” ) 
181: Ancient Greek: ἤρεμος ( ḗremos , “ gentle, quiet ” ) , ἠρέμα ( ēréma , “ calmly ” ) 
196: Proto-Indo-European roots 
197: Proto-Indo-European HReR-shaped roots 
203: Sanskrit terms with non-redundant manual transliterations 

### Skt rasana
65: Etymology 
180: Etymology
183: Inherited from Proto-Indo-Iranian *rać- ( “ to bind, tie ” ) , whence also Sanskrit रश्मन् ( raśmán ) , रश्मि ( raśmí ) . Cognate with Middle Persian lsn' ( rasan ) , Classical Persian رَسَن ( rasan ) (whence Hindustani रसन ( rasan ) / رَسَن ( rasan ) ). Compare also Old Armenian առասան ( aṙasan ) , an Iranian borrowing. See also रज्जु ( rájju ) .
197: rope , string , cord 
203: girth , girdle , zone (also figuratively applied to the fingers
291: Categories : Sanskrit terms inherited from Proto-Indo-Iranian 
292: Sanskrit terms derived from Proto-Indo-Iranian 

### pedram
62: Etymology 1 
80: Etymology 2 
155: Etymology 1
160: The first part is from Middle Persian 𐭯𐭥𐭭 ( pʿn ) / PWN ( pad , “ to, at, in, on ” ) , itself from Proto-Indo-European *per- , *próti , *préti . Compare Avestan 𐬞𐬀𐬌𐬙𐬌 ( pa i ti ) , Sanskrit प्रति ( prati , “ towards, to ” ) .
211: pleasant 
249: Etymology 2
272: Categories : Persian terms inherited from Middle Persian 
273: Persian terms derived from Middle Persian
```


## [2026-09-14T01:30:45.086Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '155,175p' 95b308d9458ea2b0.txt",
 "description": "Read pedram etymology"
}
```


### [2026-09-14T01:30:45.149Z] TOOL RESULT

```
 Etymology 1
 [ edit ] 

 An old compound. Akin to Sogdian 𐼾𐽂𐽀𐼰𐼺 ( ptrʾm /⁠patrām⁠/ , “ calm, peace ” ) .

 The first part is from Middle Persian 𐭯𐭥𐭭 ( pʿn ) / PWN ( pad , “ to, at, in, on ” ) , itself from Proto-Indo-European *per- , *próti , *préti . Compare Avestan 𐬞𐬀𐬌𐬙𐬌 ( pa i ti ) , Sanskrit प्रति ( prati , “ towards, to ” ) .

 The second part is from Proto-Indo-European *h₁rem- . Compare Avestan 𐬭𐬀𐬨𐬀𐬌𐬙𐬌 ( rama i ti ) , Sanskrit रमते ( ramate ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /pad.ˈraːm/ 

 ( Dari, formal ) IPA ( key ) : [pʰäd̪.ɾɑ́ːm] 

 ( Dari, formal ) IPA ( key ) : [pʰäd̪.ɾɑ́ːm] 
 ( Kabuli ) IPA ( key ) : [pʰäd̪.ɾɑ́ːm] 

 ( Hazaragi ) IPA ( key ) : [pʰäd̪.ɾɔ́ːm]
```


## [2026-09-14T01:30:54.128Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD rem/res\"; grep -n \"^rem-\\|^res-\\|^rek-\\|rem- To rest\\|res- To rest\" AHD_watkins1985.txt | head -10\necho \"=== AHD context\"; grep -n -B2 -A6 \"To rest\\.\" AHD_watkins1985.txt | head -40\necho \"=== IEC\"; grep -n \"^rem-\\|^rek-\\|^rekō\\|^remō\\|^ramos\" IEC.txt | head -10\necho \"=== SOD ptram\"; grep -n \"ptr'm\\|patrām\\|ptrʾm\\|patram\" SOD.txt SOD_pages.txt | head -10",
 "description": "Watkins, Mann, Gharib lookups"
}
```


### [2026-09-14T01:30:54.383Z] TOOL RESULT

```
=== AHD rem/res
=== AHD context
=== IEC
14488:rek- (1) ‘formulate, arrange, fix’. Cf. roKeið, rok- (1) W rheg, pl. -ion, f. ‘gift, donation’; Go. cf. ga-raíhsns, f. “arrangement, fixed term’; (o- gde in) Skt. racayami, v. “prepare, produce, form, adorn, set in motion’; Go. rahnjan, v. ‘reckon’; cpds: ‘estimate’; (isophone in Latv. recu, recēt, v. *coagulate")
14504:rem- ‘fit, join, strengthen’. Cf. rom-. WP II, 371 Skt. cf. ráme, mp. (1) ‘stop’; OW cf. co-ryf, s. (“stay, prop”? fr. *ko-rem, w. umlaut, as in er- byn fr. ar-ben); Go. rimis, -es-st. n. (‘rest, peace’, vocalism as for riqis); cf. (o-gde in) MHG ram, sm. ��prop, support’; OE remian, v. ‘mend’; OCS cf. remístvo, n. “art, craft; R remeslo, Cz. řemeslo, n. id.; Li. remm, “ti,
14507:rem- ‘raw; pain’ ON rámr, adj. ‘hoarse’; Sw. ráma, v. ‘bellow, bleat; Li. rémuo, -ens, m. ‘heartburn’; Late remenis, id.; cf. Li. remimas (2) ‘assertiveness’
14514:rem- — repið
=== SOD ptram
SOD.txt:60424:patram   (ptr'm-)  ©<*pati-rama 
SOD.txt:60442:7813  ptr'm   B  o^"{lj*<J^jl 
SOD.txt:60443:patram   ©MP  padram 
SOD.txt:60448:7814  ptr'm-   B,  M,  S  =»  ptr»m- 
SOD.txt:60451:patrams  ©med.  pass.  st. 
SOD.txt:60458:patramt   ©pt.  st.  =»ptr*m- 
SOD.txt:60465:7817  ptr'mty   B  ^jJ  i^lji 
SOD.txt:60466:patramte  ©pp;  ace.  -wt  f.  -} 
SOD_pages.txt:26208: 7801 ptpt'yn        B, M, S             crA-* *odl^ <*€ U>.    7813 ptr'm B                             o^"{lj*<J^jl
SOD_pages.txt:26209:       patpatin (ptptyn) =»ptyn\ pt>yn                               patram ©MP padram
```


## [2026-09-14T01:31:03.178Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC rek entries\"; sed -n '14485,14500p' IEC.txt\necho \"=== IEC ras/rasana\"; grep -n \"rasanā\\|raśanā\\|rasana\" IEC.txt | head\necho \"=== AHD rest/era\"; grep -n -i \"^era-\\|^rē-\\|rest\\b\" AHD_watkins1985.txt | head -20",
 "description": "Mann rek entries; Watkins"
}
```


### [2026-09-14T01:31:03.302Z] TOOL RESULT

```
<persisted-output>
Output too large (40.2KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bx929jxze.txt

Preview (first 2KB):
=== IEC rek entries
reið (2) ‘constrain’. Cf. WP I, 141 Av. rà-, v. ‘restrain’, OCS rájo, ati, v. (D ‘push, force’; sü-r&jo, ati, v. (thrust
rëið (3) 'roam, stray, wander, rampage, bluster’ ON cf. ræingi, m. ‘scamp’; Blg. rája se, v. ‘roam’; R réjat, inf. v. ‘blow, bluster’; Latv. cf. rees, m. ‘blusterer’; rëjigs, adj. ‘noisy, boisterous, savage’; cf. Li. riejuos, rietis, v. ‘quarrel’; Latv. reju, pf. rëm, inf: riet, v. ‘bark’. Cf. (?) Sw. rå ‘sprite, goblin’
reios; rēis ‘factual, apposite, substantive; fact, matter, substance’. WP II, 343 Skt. cf. á-råyah, adj. ʻil-liberal’; Vedic a-ráyah, m. ‘an evil spirit’; raih & ob, acc: ram, mf. ‘wealth’;? Av. rais, f. ('glitter', ambig. cf. rā- ios); Lat. rēs, gs: rēi, f. ‘thing, matter, fact, cause, state, property’; Olr. cf. ræt, m. (‘thing’, fr. *rēit-?); Ir. cf. (?) réad (2) ‘some, any’; W cf. (?) rhai ‘some’; Go. cf. -re in swa-re “with- out cause, in vain'. For the adj. cf. Lat. reus “guilty”
rek- (1) ‘formulate, arrange, fix’. Cf. roKeið, rok- (1) W rheg, pl. -ion, f. ‘gift, donation’; Go. cf. ga-raíhsns, f. “arrangement, fixed term’; (o- gde in) Skt. racayami, v. “prepare, produce, form, adorn, set in motion’; Go. rahnjan, v. ‘reckon’; cpds: ‘estimate’; (isophone in Latv. recu, recēt, v. *coagulate")
rék-, ið (2) ‘utter, pronounce’. Cf. rok- (2). (Variant: reks- in Irish) Olr. cf. reccaim, v. ‘recite’; Ir. reicim, reacaim, v. (recite; cry out; recommend’, fr. *reks-); OCS reko, resti, v. “say, speak? beside (long- gde) rěčí, f. ('speech', and com. S1.); Li. rékiuü, "ti, v. ‘shout’; Latv. recu, rēkt, v. ‘howl, bel- low?. Cf. WP I, 283 & II, 343. See next
rékis, os, à, us “utterance, noise; brawl; brawler’. Cf. WP I, 283 & II, 362, & cf rëk- above, and o-gde rok- Tokh. cf. (o-gde) A rake, B reki, s. ‘speech, word: OCS réd, f. (talk, speech’, and com. SL); Li. cf. reksmas, m. 'shout'; reka, mf. ‘brawler’; réküs, adj. ‘brawling’; (short-gde in)
rëið — rem-
13
20
25
30
35
40
45
1070
...
</persisted-output>
```


## [2026-09-14T01:31:09.046Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^rem-\\|^ ram\\|rem- To rest\\|res- To rest\\|^res-\" AHD_watkins1985.txt | head\ngrep -n \"ramus\\|Rast\\|rest, repose\\|To rest\" AHD_watkins1985.txt | head -10\necho \"--- search 'ramble'\"; grep -n \"ramble\" AHD_watkins1985.txt | head -5",
 "description": "Watkins rem-/res-"
}
```


### [2026-09-14T01:31:09.203Z] TOOL RESULT

```
650:kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
--- search 'ramble'
344:bly Latin fridre, to crumble: FRIABLE. 3. In the Celtic source of Vulgar Latin *brisdre, the source of Old French brisier and French briser, to break: BRISANCE; DEBRIS. [Pok. bhréi- 166.] bhrekv-. To cram together. 1. Probably Latin frequens, frequent, crowded: FREQUENT. 2. Suffixed zero-grade form *bhrk~-yo- in: a. Latin farcire, to cram, stuff: FARCE, FARCI, FARCY; INFARCT; b. Greek phrassein, to fence in, enclose, block up: DIAPHRAGM. [Pok. bhareky- 110.] bhrem-'. To growl. 1. Latin fremere, to growl, roar: FREMITUS. 2. Perhaps variant *brem- in Greek bronté, thunder: BRONTOSAUR. [Pok. 2. bherem- 142.] bhrem-2, To project; a point, spike; an edge. 1. Germanic *bréma-, name of prickly shrubs, in: a. Old English brém, broom: BRooM; b. Old English diminutive bremel, brém- bel, bramble: BRAMBLE. 2. Germanic *berm-, *brem-, in: a. Middle English brimme, edge: BRIM; b. Middle Dutch berme, barm, edge of a dike: BERM. [Pok. 1. bherem- 142.] bhres-. To burst. Germanic “brest- in Old English ber- stan, to burst: BURST. [Pok. bhres- 169.] bhreu-'. To cut, break up. Extension of bher-2. 1. Suf- fixed form *bhreu-d- in Germanic *breutan, to break up, in Middle English britel, brittle: BRITTLE. 2. Suffixed form *bhreu-t- in Germanic *breuthan, to be broken up, in Old English bréothan, to deteriorate: BROTHEL. [Pok. 1. bhreu- 169.] bhreu-?. To boil, bubble, effervesce, burn; with deriva- tives referring to cooking and brewing. I. 1. Germanic *breuwan, to brew, in Old English bréowan, to brew: BREW. 2. Germanic *braudam, (cooked) food, (leavened) bread, in Old English bréad, piece of food, bread: BREAD. 3. Germanic *brudam, broth, in: a. Old English broth, broth: BROTH; b. Old French breu, broth (diminutive brouet): BREWIS; IMBRUE. II. Variant form *bhré- in Germanic *brédan, to warm, with derivatives. 1. *bréd-6, “a warming,” hatching, rearing of young, in: a. Old English br��d, offspring, brood: BROOD; b. denominative *brodjan, to rear young, in Old English brédan, to beget or cherish offspring, breed: BREED. 2. Germanic *bré- d6n-, roast flesh, in: a. Old High German brat, brdto (> German Braten), roast meat: BRATWURST, SAUERBRA- TEN; b. Old French braon, meat: BRAWN. 3. Perhaps distantly related is the Germanic source of Old French brese, burning coal, ember (> French braise): BRAISE, BRAZE?, BRAZIER?, BREEZE2, III. Reduced form “bher-, especially in derivatives referring to fermentation. 1. Suf- fixed form *bher-men-, yeast, in: a. Germanic *bermén- in Old English beorma, yeast: BARM, (BARMY); b. further suffixed form *bhermen-to- in Latin fermentum, yeast: FERMENT. 2. Extended form *bherw- in Latin fervére, to be boiling or fermenting: FERVENT, FERVID, (FERVOR); DEFERVESCENCE, EFFERVESCE. IV. As a very archaic word for a spring. 1. Suffixed zero-grade form *bhru- n(e)n- in Germanic *brunnon- in Old English burn, burna, spring, stream: BOURN!, BURN?. 2. Suffixed form *bhréw-r in Greek phrear, spring: PHREATIC. [Pok. bh(e)reu- 143, 2. bher- 132.] bhreus-'. To swell. 1. Suffixed form *bhreus-t- in Ger- manic *breustam, “swelling,” breast, in Old English bréost, breast: BREAST. 2. Suffixed zero-grade form *bhrus-t- in Germanic *brust-, bud, shoot, in Old French broust, brost, shoot, twig: BROWSE. [Pok. 1. bhreu-s- 170.] bhreus-2, To break. 1. Germanic *briisjan, to crush, in Old English brysan, to crush, pound: BRUISE. 2. Suffixed zero-grade form *bhrus-to-, fragment, in Latin frustum, piece: FRUSTULE, FRUSTUM. [Pok. 2. bhreu-s- 171.] bhri-. Eyebrow. Contracted from *bhrua-. 1. Germanic *bris in Old English bri, eyebrow, eyelid, eyelash: BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugj6 (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE}, [Pok. 1. bhrii- 172, 2. bhrii- 173.] bhrig-. Agricultural produce; also to enjoy (results,
```


## [2026-09-14T01:31:15.899Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['rem- 864','ere-','era-','Pok. rem','rek-','rasta','Rast','REST','ramble']:\n    idxs=[m.start() for m in re.finditer(re.escape(pat), t)][:4]\n    print('##',pat, idxs)\n    for i in idxs[:2]:\n        print('   ...', t[max(0,i-300):i+300].replace('\\n',' ')[:600])\nEOF",
 "description": "Search Watkins for rem/rest roots"
}
```


### [2026-09-14T01:31:17.166Z] TOOL RESULT

```
## rem- 864 []
## ere- [45962, 48520, 55902, 163481]
   ...  mori- is attested dialectally (MERE), but it may well have referred to a lake or other smaller body of water. Trans- portation by or across water was, however, known to the Indo-Europeans, since most of the languages attest an old word for boat or ship, nau-?, probably propelled by oars or a pole (ere-', “to row”). The names for a number of different trees are widely enough attested to be viewed as Proto-Indo-European in date. The general term for tree and wood was deru. The origi- nal meaning of the root was doubtless “to be firm, solid,” and from it is derived not only the family of English
   ... m its color (kas-, “gray”), is also widespread. Do- mesticated animals are discussed below. A generic term for “fish” existed, dhghi- (also peisk- in Europe). The salmon (laks-) and the eel (ang”hi-) were known, the latter also in the meaning “snake.” Several birds were known, including the crane (gere-?), the eagle (or-), the THRUSH (trozdo-), the STAR- XX LING (storo-), and, at least in some dialects, the SPARROW (sper-’), FINCH (sping-), and woodpecker ((s)peik-). The generic term for “bird” was awi- (Latin avis), and from this was derived the well-represented word for egg, *dOwyo-. The nam
## era- [37783, 39865, 62902, 66846]
   ... here are two verbs expressing existence, es- and bheue-, found in English Is, Latin esse, and English BE, Latin fu-turus (FUTURE), respectively. There are verbs “to sit” (sed-'), “to lie” (legh-, kei-'), “to stand” (sta-). There are a number of verbs of motion, like g’a-, “to come,” ei-', “to go,” tera-?, “to cross over,” sek’-', “to follow,“ kei-3, “to set in motion,” and the variants of rolling or turning motion in wel-3, wer-%, k”el-'. Reconstructions are by no means confined to general, imprecise meanings such as these; we have also such specific semantic values as nes-', “to return safely
   ... , “race,” and the prototypes of Eng- lish KIN and KIND. A number of qualitative adjectives are at- tested that go back to the protolanguage. Some come in semantic pairs: sen-', “old,” and newo-, “new”; also sen-', “old,” and yeu-, “youthful vigor”; *tenu-, “thin” (under ten-), and tegu-, “thick”; g”era-?, “heavy,” and leg"h-, “light.” There are also the two prefixes su-, “good, well-,” and dus-, “bad, ill-,” in the Greek forms borrowed as EU- and pDys-. But normally adjectives of value judg- ments like good and bad are not widespread in the family and are subject to replacement; English good, 
## Pok. rem []
## rek- [27988, 28095, 28212, 98795]
   ...  ker-', “horn,” plus the noun suffix -wo-, plus the nominative singular ending -s. The root contained the basic semantic kernel, the underlying notion, which the suffix could modify in various ways. It was primarily the suffix that determined the part of speech of the word. Thus a single root like prek-, “to ask,” could, depending on the suffix, form a verb *“prk-sko-, “to ask” (Latin poscere), a noun *prek-, “prayer” (Latin precés), and an adjective *prok-o-, “asking’’ (underlying Latin procus, “suitor’). Note that *prek-, *prok-, and “prk- have, respectively, e-, o-, and zero grade. The root
   ... asic semantic kernel, the underlying notion, which the suffix could modify in various ways. It was primarily the suffix that determined the part of speech of the word. Thus a single root like prek-, “to ask,” could, depending on the suffix, form a verb *“prk-sko-, “to ask” (Latin poscere), a noun *prek-, “prayer” (Latin precés), and an adjective *prok-o-, “asking’’ (underlying Latin procus, “suitor’). Note that *prek-, *prok-, and “prk- have, respectively, e-, o-, and zero grade. The root could undergo certain modifica- tions, spoken of as extensions or enlarge- ments. These did not affect the
## rasta []
## Rast []
## REST [81213, 188010, 188021, 205817]
   ... Y; (DAISY), TODAY; b. Old English denominative dagian, to dawn: DAWN. [Pok. agher- 7.] agro-. Field. Derivative of ag-, “to drive” (< “place to which cattle are driven”). 1.Germanic *akraz in Old English zxcer, field, acre: ACRE. 2. Latin ager (genitive agri), district, property, field: AGRARIAN, AGRESTAL; AGRICULTURE, PEREGRINE, (PILGRIM). 3. Greek agros, field, and agrios, wild: AGRIA, AGRO-; AGRIOECOLOGY, AGRIOLOGY, AGROSTOLOGY, ONAGER, STAVESACRE. [In Pok. ag- 4.] agwesi. Ax. Germanic *akwesi, *akusj6- in Old English zx, ax: AX. [Pok. agu(e)si 9.] agwh-no-. Lamb. Germanic *aun- in verb *au
   ...  in Old English duru, door (feminine, originally plural), and dor, door (neuter): DooR. 2. Suffixed o-grade form dwo- *dhwor-dns (accusative plural) in Latin fords, (toward) out of doors, outside: FOREIGN. 3. Suffixed o-grade form *dhwor-ois (locative plural) in Latin foris, (being) out of doors: FOREST; (AFFOREST), FAUBOURG, FORECLOSE, FORFEIT. 4, Suffixed o-grade form *dhwor-o- in Latin forum, marketplace (originally the enclosed space around a home): FORENSIC, FORUM. 5. Zero-grade form *dhur- in Greek thura, door (> thureos, shield): THYROID. 6. Per- sian dar, door, gate: DURBAR. [Pok. dhyé
## ramble [142913]
   ... n fremere, to growl, roar: FREMITUS. 2. Perhaps variant *brem- in Greek bronté, thunder: BRONTOSAUR. [Pok. 2. bherem- 142.] bhrem-2, To project; a point, spike; an edge. 1. Germanic *bréma-, name of prickly shrubs, in: a. Old English brém, broom: BRooM; b. Old English diminutive bremel, brém- bel, bramble: BRAMBLE. 2. Germanic *berm-, *brem-, in: a. Middle English brimme, edge: BRIM; b. Middle Dutch berme, barm, edge of a dike: BERM. [Pok. 1. bherem- 142.] bhres-. To burst. Germanic “brest- in Old English ber- stan, to burst: BURST. [Pok. bhres- 169.] bhreu-'. To cut, break up. Extension of bh
```


## [2026-09-14T01:31:24.073Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'\\[(?:In )?Pok\\.[^\\]]*33[89][^\\]]*\\]', t):\n    print(repr(t[max(0,m.start()-450):m.end()].replace('\\n',' ')))\n    print('---')\nEOF",
 "description": "Find Watkins root at Pokorny 338"
}
```


### [2026-09-14T01:31:25.186Z] TOOL RESULT

```
'wer-yo-, to cover over (see wer-5). [Pok. epi 323.] er-1, To move, set in motion. 1. Probably Germanic *ar-, *or-, *art(a), to be, exist, in Old English eart and aron, second person singular and plural present of béon, to be: ARE!, ART?. 2, Perhaps in Germanic suffixed form “er- n-os-ti- in Old English eornoste, zealous, serious: EAR- NEsT!. 3. Suffixed form *or-yo- in Latin oriri, to arise, eu-! appear, be born: ORIENT, ORIGIN, ORIGINAL; ABORT. [Pok. 3. er- 326; ergh- 339.]'
---
"tic horned animals. Extended form *eri- in Latin ariés, ram: ARIES. [Pok. 2. er- 326.] era-'. To row. 1. Variant form *ré- (< *rea-) in: a. Ger- manic *ré- in Old English réwan, to row: ROW?; b. suf- fixed form *ré-thra- in Germanic *réthra, rudder, in Old English réther, steering oar: RUDDER; Cc. suffixed form *ré-smo- in Latin rémus, oar: BIREME, REMEX, TRIREME. 2. Oldest variant form *sres- becoming *eré- in Greek triérés, trireme: TRIERARCH. [Pok. 1. er9- 338.]"
---
'ces,” rare: RARE}, 2. Suffixed zero-grade form *ra-ti- in Latin ratis, raft (< “grating,” “latticework”): RATITE. 3. Suffixed length- ened-grade form *ré-ti- in Latin réte, r�\x0c�tis, a net: RE- SEAU, RETE, RETIARY, RETICLE, RETICULE, RETINA; RETIFORM. 4. Suffixed form *eré-mo- in Greek erémos, empty, desolate, bereft: EREMITE, HERMIT; EREMURUS. [Pok. 5. er- 332.] ered-. High. Suffixed zero-grade form red-wo- in Latin arduus, high, steep: ARDUOUS. [Pok. er(e)d- 339.]'
---
'et: RE- SEAU, RETE, RETIARY, RETICLE, RETICULE, RETINA; RETIFORM. 4. Suffixed form *eré-mo- in Greek erémos, empty, desolate, bereft: EREMITE, HERMIT; EREMURUS. [Pok. 5. er- 332.] ered-. High. Suffixed zero-grade form red-wo- in Latin arduus, high, steep: ARDUOUS. [Pok. er(e)d- 339.] ergh-. To mount. 1. Suffixed o-grade form *orgh-i- in Greek orkhus, testicle: ORCHID. 2. Suffixed o-grade form *orgh-eyo- in Greek orkheisthai, to dance: ORCHESTRA. [Pok. orghi- 782, ergh- 339.]'
---
```


## [2026-09-14T01:31:40.627Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (708,709,710,711):\n    l=leaves[i]\n    nums=re.findall(r'\\b1[23][0-9]{2}\\b', l)\n    print(i, nums[:6], repr(l[:120].replace('\\n','|')))\nEOF",
 "description": "Klein leaf page numbers"
}
```


### [2026-09-14T01:31:41.782Z] TOOL RESULT

```
708 ['1330'] 'l.|reprehensible,  adj.,  worthy  of  reprehension.  — ME.,  fr.  Late  L.  reprehensibilis,  fr.  L.  reprehen- sus,  p'
709 [] 'uisitus,  pp.  of  requirere.  See  require  and  -ion. Derivatives:  requisition,  tr.  v.,  requisition-ary, adj.,  re'
710 [] ' to. Derivatives :  resist,  n.,  resistance  (q.v.),  resistant (q.v.),  resist-er,  n.,  resist-fui,  adj.,  resistibl'
711 ['1336'] "F.  restaurant  is  pres.  part,  of  restau- rer,  ‘to  restore'.  See  restore  and  -ant.|restaurateur,  n.,  the  ke"
```


## [2026-09-14T01:32:03.675Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT rest\"; grep -n \"^REST\" SKT.txt | head -5\ngrep -n -A4 \"^REST, to repose\\|^REST (1)\\|^REST,\" SKT.txt | head -20\necho; echo \"=== FSD/WEB present?\"; ls | grep -i \"FSD\\|WEB\" | head",
 "description": "Skeat rest"
}
```


### [2026-09-14T01:32:03.762Z] TOOL RESULT

```
=== SKT rest

=== FSD/WEB present?
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
WEB_vol1.txt
```


## [2026-09-14T01:32:07.707Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"^Rest\\b\\|Rest, repose\\|Rest (1)\" SKT.txt | head -8\necho \"---\"; grep -n -i \"rasta.*mile\\|G\\. rast\\|A\\.S\\. rest\" SKT.txt | head -8\necho \"=== FSD rest\"; grep -n -i \"rest.*AS\\. rest\\|OHG\\. rasta\" FSD_vol3.txt FSD_vol4.txt 2>/dev/null | head -8",
 "description": "Skeat/F&W rest"
}
```


### [2026-09-14T01:32:07.838Z] TOOL RESULT

```
---
=== FSD rest
```


## [2026-09-14T01:32:10.852Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"rasta\" SKT.txt FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head -12",
 "description": "Search rasta in English etym books"
}
```


### [2026-09-14T01:32:10.932Z] TOOL RESULT

```
SKT.txt:15989:Best  (1),  repose.  (E.)  A.  S.  rest,  ntst, rest.  ^-  Du.  mst,  Don.  Swed.  «j/,  Icel rost  (the  distance  between  two  resting- places),  Goth,  rasta  <a  stage),  O.  H.  O. rcsta,  rest.  Allied  to  Ski.  ra-ti,  pleasure, Gk.  ipojij,  rest.  \^  RA.)
FSD_vol1.txt:23459:The  character  of  Jesus  Christ  is  instinctively  felttoofTerastain- Iess  and  archetypal  manhood,  which  forbids  our  accepting  any humbler  standard.  Getkie  Entering  on  Life  p.  33.  [j.  B.  A.  1887.] ari'chc-typ'Ic  or  -l-calt.—  archetypal  Idea,  the  Platonic Idea.  See  idea.—  a.  world,  an  immaterial  world  supposed by  some  Platonlsts  to  have  existed  prior  to  the  created  or ectypal  world  and  to  have  served  as  a   pattern  for  Jt  In  its construction.—  ar'che-ty"pal-ly,  ar"che-typ'I-cal-Iy,  cdr. ar'che-type,  1   ar'ki-taip;  2   ar'ce-typ,  n.  1-  A   primi- tive pattern  or  model  which  is  copied  or  imitated;  a prototype.
FSD_vol1.txt:23598:orthography orthostyle overmantel oxeyc pagoda palace panel parapet parastas
FSD_vol1.txt:46150:A   fccmSaif  clrcurastance  Horribly  Btuff'd  with  epithets  of  war.  Bo^mo-lodi'I-dcc,  1   bO'mo-Iek'x-dl;  2   b6'mo-I5c'l-de,  7».  pi.  Saint (122 1-V n 1274).  Giovannldi  FIdenz3,  an  Italian  thco- SiiAEESFEAEEOrAefio acti.sc.  1.  Crust.  A   family  of  parasitic  copepod3  having  the  cephalo-  loglan:  Franciscan  general  and  cardinal.
FSD_vol1.txt:53373:as  a   single  undertaking,  and  ordinarily  paid  for  as  such,  niis'tar  n   rastar
FSD_vol3.txt:93454:very destructive to rasta la Hawaii, suppoasd to have Unit
FSD_vol3.txt:120849:A Greek pllasuir. IL , < Gr parastas, < para, beside, 4
FSD_vol3.txt:228901:involvinx strong contrasta of llahl and shade Eein'-
FSD_vol2.txt:13077:eu'cra-slto,  1   ya'kro-salt:  2   yu'cni-slt,  «,  Mineral.  A   sili- cate of  thorium  and  other  rare  earth  allied  to  thorite,  i   -f Gt.eukrasta;  see  euckasy.)
FSD_vol2.txt:13440:[LL.,  <   Gr.  euphrasta,  delight,  <   eu,  well,  +   pArfre.  mind.]  eu"pyr-ehro'lte,  1   ya'par-kro'oit;  2   yu'p5r-cr5'-tt,  ... eu'phra-sy,  1   y^fra-si;  2   yu'fra-sy,  re.  I.  Bot.  Eyebright  Mineral.  A   concentric,  subfibrous,  ash-gray  and  bluish-  ^   white  bull.  2.  Astron.  (1) "Jupiter’s ''satelllt'e'
FSD_vol2.txt:16066:1.  The  outer  muscle  of  the  eye,  which  turns  the  eye- ball outward.  2.  The  pyramldalis  muscle  of  the  abdo- men.—ex"tra«red%  a.  Physics.  Same  as  infra-red.— cx"tra-re-gard'Ing,  a.  [Rare.]  Regarding  or  inspecting what  is  outside  or  beyond  ourselves:  looking  outw.ard. —   ex"tra-reg'u-lar,  a.  Unoonllnecl  or  unrestricted  by rule  or  regulation.— ex"tra-reg'u-lar-ly,  ado.— ex"tra- scrlp'tur-al,  a.  Aside  from,  or  derived  from  sources  other than,  the  Scriptures;  as,  an  cxtrascriptural  doctrine.—  ex"- tra-sen'sl-bl(ep,  ct.  &   n.  Being  beyond,  or  that  which  is beyond,  the  reach  of  the  senses.— ex^tra-specrtlon,  n.  A looking  outward:  observation  of  outward  things.—  ex"tra- 8ta-pe'dl-al.  I.  a.  Being  exterior  to  the  stapes:  s.aid  of a   part  of  the  columella  of  the  ear.  II.  n.  The  extrastape-
FSD_vol2.txt:57367:infrastapedlal  element.- !ft''fra-ster'nal,  a.  Situated  be-  or  dualities,  witlnnfo .   as.  t,e  rnfmed  zeal  ^nto
```


## [2026-09-14T01:32:25.269Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"604\\. \" HRN.txt | head -5\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\ni=t.find('604.  r')\nif i<0: i=t.find('604. r')\nprint(repr(t[i-200:i+700]))\nprint('leaf', t[:i].count('\\f'))\nEOF\necho \"=== SKT leaf\"; python3 -c \"\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); pre='\\n'.join(lines[:15989]); print('leaf',pre.count('\\f'))\"",
 "description": "Horn rām entry, Skeat leaf"
}
```


### [2026-09-14T01:32:26.353Z] TOOL RESULT

```
5405:604. räm *Ruhe; fröhlich, heiter, ramis, ramist (Lex.).
" rastl, rästln (Sahn. I,\n123 Vers 1070).\nap. rasta- recht, richtig'; aw. rasta--, phlv. rast,\nrastlh\\ ai. raddhd-,\noss. d. t. rast^ rasf (212).\nLW. kurd. af/. bei. (222) rast; wa./. rast, ssiv, rüst.\n604. räm *Ruhe; fröhlich, heiter, ramis, ramist (Lex.).\nap. vergl. Äriya]ramna', *Apia]^oi/nvt]g; aw. raman-\n^) Aw. rati- (yt. 10, 45) ist = ai. arati- (Bartholomae, Altiran.\nVerbum 194, BB. 17, 111 Anm., G;oldnor, KZ. 25,520 Note 61).\x0c— 135 —\n*Ruhe'; phlv. hu]ram, ram(i)sn, rämmltan; ai. rdmU'\n*Lust'.\noss. üromjn 'zurückhalten, hemmen, beruhigen' (263).\n605. ran 'Schenkel'.\naw. räna- 'Schenkel'; phlv. ran^ ränpün, arm. LW.\neran, meist pl. eranK (Hübschmann, No. 96).\nkurd. bei. (221) LW. ran; af/. vrün.\n606. ränden 'treiben, stossen*, ranis,\nContrahirt aus rawdmden^ Causativ von reßen\n(No. 619), vergl. Kä»än: Z(efre), beräw, heräivött^\nheräft s. v. ränden,\nPhlv. rayinTtan, räyma, räyln(i)sn,"
leaf 155
=== SKT leaf
leaf 424
```


## [2026-09-14T01:33:00.438Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\n# find offset: look for a leaf with page-like header 36x\nfor i in range(370,395):\n    l=leaves[i]\n    print(i, re.findall(r'\\b3[5-7][0-9]\\b', l[:300])[:4], repr(l[:90].replace('\\n','|')))\nEOF",
 "description": "Locate WLD Bd2 page 362"
}
```


### [2026-09-14T01:33:01.491Z] TOOL RESULT

```
370 ['366', '374'] '366                                          reg-|||  lat. rigare zu got. rign usw. unter '
371 ['367'] '                                           reg^os     ret-, red-                          '
372 ['368'] '368                                      ret-, rot-, rot-   — red-|ret-, rot-, rot- „Stang'
373 ['369'] '                                             red- ; rOd-   :   rad        rep-            '
374 ['370'] '                    ;                           ;                                         '
375 ['371'] '                                                     rebh-    — rem-                      '
376 ['372'] '372                                                    rem-|||ai. rama- m. „Lust, Freude‘^'
377 [] '                              ;|||||renib- „verzeiTen, verrenken^??|     Ir.           „Ve'
378 ['374'] '374                                           rent-   — nighio^|rent- „Saclie“?|  Unter di'
379 ['375'] '                                    rughio-                                  375||  asl. r'
380 [] '                                                     L.||1.   *la~ Schallwurzel,          '
381 ['377'] '                                                 la-,   lai-,   la[i]-dh-                 '
382 ['378'] "378                                                laiuo-||||„das Verge8sen“, dor. kd'&og "
383 ['379'] '                                             la 108        —   lau-                       '
384 [] '                                                        ,|||||380                         '
385 ['358'] '                                                                 ;   ^        ;|||||      '
386 [] '382                                                   lat-, slat-||||     aisL lepja (^lap'
387 [] '                              lap-: l9p-        — lab-, labh*(?), lap(h)-                 '
388 [] '                                                                                          '
389 [] '                                                                          :|||||          '
390 [] '386                                                        las-||||TrautmannApr. 461, Bed.'
391 [] '                                                        lazd-   —   lei-                  '
392 [] '                                                                          ;               '
393 [] '                                                         lei-                             '
394 [] '390                                                 lei-||||lit.    lynas^   lett.   Imis^'
```


## [2026-09-14T01:33:06.646Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (365,366):\n    print('=== leaf',i)\n    print(leaves[i][:2200])\nEOF",
 "description": "Print WLD Bd2 p.362"
}
```


### [2026-09-14T01:33:07.679Z] TOOL RESULT

```
=== leaf 365
                                               reumen        — req-                             361

sein miifite,        ist   unwahrscheinlich  den a die Herkunft aus der Lautgebarde
                                                    ;


           „rii]psen“      und „nigire“ ist sehr wahrscheinlich, und lit. raumxi kann
kann ^raudmu „das rote Muskelfleisch^‘ (^: raudas                            sein.


renmen „Haar‘'??
  ai. roman^ loman „Haar“ angeblich zu air. ruamnae gl, lodix: aber ir.
ron „Pferdehaar“ und niainne „einzelnes Haar‘‘ nach Pedersen        I 49                 KG
aus cymr. rliaivn ,Pferdehaar“ entlehnt, wozu bret, reun(enn) „einzelnes
                             5


starkes Haar, Schweineborste“, aus *rCin-.
  Kach Zupitza KZ. 35, 269 iage ein w-Stamm urspriinglich ^ra{d)xmd
^ra^umnes zugrunde. ir. ruamnae sei ^ra^mnon-, cymr. rhawn *ra(d)«emw-.
Pick II * 234. Aber einen kelt. Wandel mn'^nn gibt es nicht und auch
die Bedeutung von ruamnae ist nicht gesichert.  Kach Ausweis von nir.
r'daimneach „langes Haar, Angelschnur“ miifite eine Grundform "^reus-
men-jmon- angesetzt w^den (Pokorny brief lich).

reus- Blister?
     Ir.   riiaimm „betula alnus, alnus glutinosa*' (Pick II ^ 234);
     Zu ahd. rusbaum (Graff 3, 866), roust (ahd. Gl. 3, 41, 1), mhd. nhd. Rilsier'l

req- „Stange‘‘ usw. wie               reiq-,   s.       d.

     Aisl. ra   f.          einem Stangengeriist zum Trocknen, Schiffsraa“,
                      „Stange    in
mnd. ra „Schiffsraa“, mhd. rahe f. „Stange, Schiffsraa''; norw. mdartl. raaga
(^regdn-) „dunne Stange“, schwed. mdartl. raga „dunner langer Wurzel-
schoBling^^; nd. rach „GestelI, WandregaP’ {-kk- aus -qn-), mhd. reck{e)
„lange diinne Stange, bes. zum Gberhangen von Kleidern"'; mhd. rach,
-lies und rac, -ges, dehnstufig rceJie „steif; straff“; mhd. regen st. Y. „sich

erheben, starren, emporragen“, Faktitivum regen schw. Y., „aufrichten, er-
regen, bewegen, weekend (^rcigjan), nhd. regeyi: mhd. ragen „in die Hohe
stehen“ (auch wohl ags. oferhragian „uberragen“ mit unechtem h^ s. u, qreq-
jjVorspringender Balkeu“), norw. mdartl, raga „8chwanken“; reduktions-
stufig      mhd. rogel „nicht fest, schwank“ (auch nh
=== leaf 366
                                                                                    ;




362                                 req-, req   reg*


  Mhd. rcehe nicht als ^hrahi zu aksl. krehnqti (? s. Berneker 613) „steif
werden“, lit. Tcrenku^ TcreMi „germnen“ (als Alternative bei Zupitza aaO.).

req-, req- „anordnen“.
  Ai. racayati „verfertigt, bildet“, racana n. „Ordnen, Betreiben‘‘; got. ra-
hnjan „rechTieii“; ragin n. „Rat, Bescblu6“, altn. regin^ pi. rqgn „die rat-
schlagenden Machte, G6fter“, alts, ragino giscapti ^Beschliisse der gottlichen
Machte'^ ahd. regin- in Eigennamen;
  asl. roJcb m. „bestiTnmte Zeit, Ziel“, skr. rok ,jTermin“, ru. rok „Schick-
sal,    Jahr, Termin'^, ksl. rekq^ rcsti „sagen“, raknqti, raciti „wollen“.
     Mit e got. garehsns f. „Be8timmiing, Eatschlu6“, asl. rech f. „accusatio“.
     Ganz unsicher Zusammengehorigkeit mit altn. ran n. ^Raub^^, ahd. ran
n. (?)  „mtentio" "^rahna-^ altn. rcena „rauben“, ahd. (Hild.) hiraJianeM „er-
beuten‘‘ (?).   Gnindbedeutung ware „Raub-Anschlag“. Vgl. Pick III* 335
(reft, reg 2) u. Palk-Torp 876 (raw), Trautmann Bsl. Wb. 243.



rek-, reg- „bmden‘‘?
  Unsicher. Ai. ragana f, „Strick, Riemen, Gurtel“, ragmi m. „Strang.
Riemen, Zugel“, zu idg. reft?; aschw. hnrraka QiurS-) „Heck-Band“, an.
rakki m. „Stropp zum Pesthalten der Rahe“, ags. racca m. dass., an. re-
kendi n., rekendr f. pi. „Kette, Fessel"; ags. racente^ racete     f.,   ahd. rahhinm
f. dass. zu idg. re^? (Pick III* 332 f.).




rek|)h- „zerren, beuteln, einem zusetzen“.
     Ai. raksas- „Qual, Qualgeist,     Unhold“, av. rasali- „Schadigung, Schaden,
bes. der im andern Leben“, rasayeiti „schadigt“; gr. eQeyj&o} „zerre und
beutle hin und her“ (der Sturm das Schiff; 'EQey'&svg „der Erderschutterer‘‘)
„rei6en,       zerrei6en‘\   Bartholomae Ar. Forsch. II     57.   Airan. Wb. 1516.
Boisacq 277 (m. weiterer Lit.); Kretschmers KZ. 31, 432 f. Bedenken wegen
der gr. Bed. erle digen sich beim Ansatz der Gdbed. als „beuteln, zerren‘‘.

1.     reg- „grade, grade richten, lenken, reckon, strecken, aufrichten (auch
         unterstiitzend, helfend) ; Richtung, Linie (Spur, Geleise)'^ u. dgl.
     Ai. rjyat?\ rnjdtl „streckt sich, streckt sich
```


## [2026-09-14T01:33:24.347Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK\ncp /home/sfmqrb/git/rishe/site/pages/420.jpg /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/420.png 2>/dev/null || true\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg420b.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/420.png\nls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/420.png",
 "description": "Copy page 420 image for audit"
}
```


### [2026-09-14T01:33:24.448Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 72677 Sep 13 21:33 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/420.png
```


## [2026-09-14T01:33:26.686Z] TOOL CALL #71: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py",
 "description": "Inspect verify_check.py"
}
```


### [2026-09-14T01:33:26.739Z] TOOL RESULT

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


## [2026-09-14T01:33:29.274Z] TOOL CALL #72: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py",
 "description": "Rest of verify_check.py"
}
```


### [2026-09-14T01:33:29.324Z] TOOL RESULT

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


## [2026-09-14T01:33:36.553Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ntail -10 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['url'], '|', d.get('status'))\"",
 "description": "Check archived URL strings"
}
```


### [2026-09-14T01:33:37.706Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/%D9%84%D8%B4%DA%A9%D8%B1 | 200
https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%87%D8%A8 | 200
https://en.wiktionary.org/wiki/%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86 | 200
https://en.wiktionary.org/wiki/%D8%B9%D8%B3%D9%83%D8%B1 | 200
https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%A7%D8%A8%D9%87 | 200
https://www.etymonline.com/word/control | 200
https://abadis.ir/fatofa/%D8%B9%D8%B1%D8%A7%D8%AF%D9%87/ | 200
https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%A7%D8%AF%D9%87/ | 200
https://abadis.ir/fatofa/%DA%A9%D9%86%D8%AA%D8%B1%D9%84/ | 200
https://www.islamweb.net/ar/library/content/122/833/%D8%AA%D8%B1%D9%87 | 200
```


## [2026-09-14T01:33:40.885Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -c . index.jsonl; python3 - <<'EOF'\nimport json\nfor l in open('index.jsonl'):\n    d=json.loads(l)\n    if 'page 420' in (d.get('note') or ''):\n        print(d['url'],'|',d.get('status'))\nEOF",
 "description": "List page-420 archived URLs"
}
```


### [2026-09-14T01:33:42.157Z] TOOL RESULT

```
4793
https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D9%86 | 200
https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%85 | 200
https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%A7%D9%85 | 200
https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D9%85 | 200
https://en.wiktionary.org/wiki/rest | 200
https://www.etymonline.com/word/rest | 200
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81rem- | 200
https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A4%B6%E0%A4%A8%E0%A4%BE | 200
https://en.wiktionary.org/wiki/%D9%BE%D8%AF%D8%B1%D8%A7%D9%85 | 200
https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/rastu | 200
```


## [2026-09-14T01:39:35.194Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_RASAN = \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D9%86\"\nW_RAM   = \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%85\"\nW_ARAM  = \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%A7%D9%85\"\nW_XORR  = \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D9%85\"\nW_REST  = \"https://en.wiktionary.org/wiki/rest\"\nE_REST  = \"https://www.etymonline.com/word/rest\"\nW_H1REM = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81rem-\"\nW_RASANA= \"https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A4%B6%E0%A4%A8%E0%A4%BE\"\nW_PEDRAM= \"https://en.wiktionary.org/wiki/%D9%BE%D8%AF%D8%B1%D8%A7%D9%85\"\nW_RASTU = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/rastu\"\n\ndoc = {\n \"pdf_page\": 420,\n \"book_page\": 390,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Rek, Reg 2\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *reḱ- / *reǵ- 'to bind, tie' (Pokorny 863 'rek-, reg- ,binden'?'); in practice reconstructable only as Proto-Indo-Iranian *rać- 'to bind, tie'\",\n   \"note\": \"Nourai's root box reproduces Pokorny p.863 exactly: 'rek-, reg- ,binden'?' with the Sanskrit material raśanā / raśmi-. The language label (Indo-European) and the gloss ('to tie') are faithful. What Nourai drops is the question mark: Pokorny prints 'binden'?' and Walde-Pokorny II 362 opens the entry with 'Unsicher'. Both split the material in two — the Indo-Iranian words point to a palatal *reḱ-, the Germanic ones (ON rakki, rekendi, OE racente, OHG rahhinza) to *reǵ- — so there is no secure single IE root; modern handbooks (Wiktionary, after Mayrhofer EWAia) reconstruct only PII *rać- 'to bind, tie'. Hence 'plausible' rather than 'confirmed'. Note that the two neighbouring Pokorny entries on the same page — '2. rek- ,anordnen'' (Skt. racayati, racana-) and 'rek-, reg- ,binden'?' (Skt. raśanā) — are the source of the misprint in node #1.\",\n   \"note_fa\": \"ریشهٔ «Rek, Reg 2» با معنی «بستن» درست از پوکورنی (ص ۸۶۳) و والده‑پوکورنی (ج۲ ص۳۶۲) گرفته شده است؛ نام زبان (هندواروپایی آغازین) و معنی هم درست است. اما نورایی علامت پرسش پوکورنی را نیاورده: خودِ پوکورنی «binden?» می‌نویسد و والده‑پوکورنی مدخل را با واژهٔ «Unsicher» (نامطمئن) آغاز می‌کند، زیرا واژه‌های هندوایرانی (سنسکریت raśanā، raśmi-) به ریشهٔ کامی *reḱ- و واژه‌های ژرمنی به *reǵ- می‌رسند. ریشه‌شناسی امروزی تنها *rać- هندوایرانی آغازین را بازسازی می‌کند. بنابراین ادعای نورایی «با احتیاط پذیرفتنی» است.\",\n   \"sources\": [W_RASANA, W_RASAN],\n   \"ref_check\": [\n    {\"ref\": \"POK:863\", \"status\": \"supports\", \"note\": \"POK_03.txt (leaf 101-102, printed p.863, between the page marks '863' and '864'): \\\"rek-, reg- ,binden'? / Ai. rasanā f. ,Strick, Riemen, Gürtel', rasmi- m. ,Strang, Riemen, Zügel'; aschwed. hurraka (hurð-) ,Heck-Band', aisl. rakki m. ,Stropp zum Festhalten der Rahe', ags. racca m. ds., aisl. rekendi n. ... WP. II 362.\\\" Exactly Nourai's root, gloss and Sanskrit witness.\"},\n    {\"ref\": \"WLD2:362\", \"status\": \"supports\", \"note\": \"WLD_Bd2_pages.txt leaf 366 (header '362  reḱ-, reǵ'): \\\"rek-, reg- ,binden'? Unsicher. Ai. raśanā f. ,Strick, Riemen, Gürtel', raśmi m. ,Strang, Riemen, Zügel', zu idg. reḱ?; aschw. hurraka ... ahd. rahhinza f. dass. zu idg. reǵ? (Fick III⁴ 332 f.)\\\". Page number exactly right (offset: leaf = printed + 4, checked on leaves 370/366).\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.863 (POK_03.txt leaf 101)\", \"stance\": \"supports\", \"note\": \"\\\"rek-, reg- ,binden'? ... WP. II 362\\\" — with the question mark Nourai omits.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.362 (leaf 366)\", \"stance\": \"partial\", \"note\": \"\\\"Unsicher\\\" — Walde-Pokorny treat the root as doubtful and split the evidence between *reḱ? (Indo-Iranian) and *reǵ? (Germanic).\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. rek- (1) 'formulate, arrange, fix' (IEC.txt l.14488)\", \"stance\": \"silent\", \"note\": \"Mann has rek- (1) 'formulate, arrange, fix' (Skt. racayāmi) and rek- (2) 'utter, pronounce', but NO rek- 'bind'; grep for 'rasanā/raśanā' in IEC.txt returns nothing.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"No *rek-/*reg- 'bind' entry; the appendix lists only roots with English reflexes and this root has none.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"račana, rašanâ\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"račana, rašanâ\",\n     \"correct_form\": \"rašana, rašanâ (Skt. raśana n. / raśanā́ f.)\",\n     \"derivation\": \"The second form is right: Skt. raśanā́ f. (also raśana n.) 'cord, rope, string, thong; girdle, rein', from PII *raćanáH, built with the -ana- suffix on the root *rać- 'to bind, tie'; the same root gives Skt. raśmán-, raśmí- 'strap, rein'. The FIRST form is wrong. Nourai prints 'račana', i.e. Skt. racanā́ / racana-, which is a real Sanskrit word but means 'arranging, ordering, composing' (from rac- 'to arrange, produce') and belongs to the neighbouring Pokorny entry '2. rek- ,anordnen'' printed a few lines above on the very same page 863 (and on WP II 362, immediately above 'rek-, reg- ,binden'?'). Nourai evidently copied the headword of the adjacent root; the intended form was surely 'rašana' (raśana), the neuter by-form of raśanā, since in his font č and š differ only in the letter under the háček. The printed page 420 of the dictionary does read 'račana' (see data/verification/sources/refs/ocr/BOOK/420.png), so the extraction is faithful and the error is the book's.\",\n     \"derivation_fa\": \"صورت دوم درست است: سنسکریت raśanā́ (مؤنث) و raśana (خنثی) به معنی «ریسمان، بند، کمربند، افسار»، از هندوایرانی آغازین *raćanáH، ساخته‌شده از ریشهٔ *rać- «بستن» با پسوند -ana-؛ هم‌ریشه با raśmi- «تسمه، مهار». اما صورت نخست نادرست است: «račana» همان racanā́ سنسکریت است که معنی آن «آراستن، ترتیب دادن، سرودن» است و به ریشهٔ دیگری (rek- «نظم دادن») تعلق دارد که پوکورنی چند سطر بالاتر در همان صفحهٔ ۸۶۳ آورده است. ظاهراً نورایی مدخل مجاور را به‌اشتباه رونویسی کرده و مقصودش «rašana» بوده است (در حروف‌چینی او č و š تنها در حرف زیر هاچک تفاوت دارند). تصویر صفحهٔ ۴۲۰ نشان می‌دهد که خودِ کتاب «račana» چاپ کرده؛ پس خطا از کتاب است نه از خوانش اسکن.\",\n     \"sources\": [W_RASANA, W_RASAN],\n     \"ref_check\": [\n      {\"ref\": \"WLD2:362\", \"status\": \"partial\", \"note\": \"WLD Bd. II p.362 (leaf 366) gives under 'rek-, reg- ,binden'?': \\\"Ai. raśanā f. ,Strick, Riemen, Gürtel'\\\" — the second of Nourai's two forms only. The first form 'račana' is in fact the headword material of the entry printed immediately above on the same page: \\\"reḱ-, reǵ- ,anordnen'. Ai. racayati ,verfertigt, bildet', racana n. ,Ordnen, Betreiben'\\\" — a different root and a different meaning.\"},\n      {\"ref\": \"POK:863\", \"status\": \"partial\", \"note\": \"Same situation in Pokorny p.863: \\\"2. rek- ,anordnen': Ai. racayati ,verfertigt, bildet', racana- n. ,Ordnen, Betreiben'\\\" stands a few lines above \\\"rek-, reg- ,binden'?: Ai. rasanā f. ,Strick, Riemen, Gürtel'\\\". Pokorny supports 'rašanā = rope', not 'račana = rope'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.863\", \"stance\": \"partial\", \"note\": \"Supports raśanā 'Strick, Riemen, Gürtel'; assigns racana- to the separate root 'anordnen'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.362\", \"stance\": \"partial\", \"note\": \"\\\"Ai. raśanā f. ,Strick, Riemen, Gürtel', raśmi m. ... zu idg. reḱ?\\\" — but racana n. 'Ordnen, Betreiben' belongs to the preceding entry.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. rek- (1) (IEC.txt l.14488)\", \"stance\": \"contradicts\", \"note\": \"\\\"rek- (1) 'formulate, arrange, fix' ... Skt. racayami, v. 'prepare, produce, form, adorn, set in motion'\\\" — Mann too puts racana-material under 'arrange', not 'bind'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt), grep 'raśanā/rasanā'\", \"stance\": \"silent\", \"note\": \"Buck has no 'rope' section entry for the Indo-Iranian word.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"rasan\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The word itself is beyond doubt: MacKenzie's Concise Pahlavi Dictionary has \\\"rasan [lsn' | N ~] rope\\\", i.e. MP rasan written <lsn'> (Pahlavi <l> = /r/), continuing Old Iranian *racana- with regular Middle Persian loss of the final vowel and the Iranian development *ć > s (whereas Indo-Aryan gives ś). What is drawn wrongly is the ROUTE: the chart makes Pahlavi rasan a descendant of the Sanskrit word, but MP rasan is its sister, not its child — Wiktionary (with Parthian rasan) derives it from Proto-Iranian *racanáH beside Proto-Indo-Aryan *raśanáH, both from PII *raćanáH. The Armenian loan aṙasan (from an Iranian, not an Indian, source) shows the Iranian branch existed independently. This is Nourai's general chart convention (Sanskrit stands in for the Indo-Iranian parent), so the claim is acceptable with that caveat.\",\n     \"derivation_fa\": \"خودِ واژه قطعی است: مکنزی در فرهنگ کوچک پهلوی می‌آورد «rasan [lsn'] رسن، ریسمان». فارسی میانهٔ rasan از ایرانی باستان *racana- می‌آید؛ *ć هندوایرانی در شاخهٔ ایرانی به s و در شاخهٔ هندی به ś بدل شده است (از این‌روست که سنسکریت raśanā دارد و ایرانی rasan). اما مسیرِ رسم‌شده در نمودار درست نیست: پهلوی rasan فرزندِ واژهٔ سنسکریت نیست بلکه هم‌ریشه (خواهرِ) آن است؛ ویکی‌واژه آن را از ایرانی آغازین *racanáH (در کنار پارتی rasan) می‌گیرد. وام‌واژهٔ ارمنی aṙasan نیز از منبعی ایرانی گرفته شده نه هندی. چون نورایی معمولاً سنسکریت را به‌جای «نیایِ هندوایرانی» می‌گذارد، ادعا با این قید پذیرفتنی است.\",\n     \"sources\": [W_RASAN, W_RASANA],\n     \"ref_check\": [\n      {\"ref\": \"SNS:227\", \"status\": \"supports\", \"note\": \"Tavoosi, Vāže-nāme-ye Šāyast ne Šāyast: the word index (SNS_pages.txt l.15896) lists \\\"rasan 227/3\\\" — i.e. the Pahlavi text page 227 line 3 that the glossary entry cites; the glossary entry itself (SNS_pages.txt l.9047) carries the Latin transliteration 'rasan' with a Persian gloss (OCR of the Persian is unusable). So the citation points to a real Pahlavi attestation of rasan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.v. rasan (PHD.txt l.557; PHD_mackenzie.txt l.4344)\", \"stance\": \"supports\", \"note\": \"\\\"rasan [lsn' | N ~] rope\\\" — Pahlavi rasan 'rope', with New Persian identical.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"The glossary has rāmišn, ramak, hu-ramak etc. but no entry for rasan (grep '^rasan' returns nothing).\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 615, p.137\", \"stance\": \"partial\", \"note\": \"Horn gives NP \\\"resen 'Strick'\\\" straight from \\\"ai. raśanā 'Strick, Riemen, Zügel, Gurt'\\\" without citing a Pahlavi form — so he supports the word but not an explicit Pahlavi stage.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"rasan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP رَسَن rasan 'rope, cord' is the regular continuation of MP rasan (<lsn'>, MacKenzie 8), itself from Proto-Iranian *racanáH < PII *raćanáH, root *rać- 'to bind' — the Iranian cognate of Skt. raśanā́. Horn, Grundriss no. 615 (p.137) sets NP resen 'Strick' beside Skt. raśanā and notes the Armenian loan erasan / apa-rasan 'Zügel' and, expressly, \\\"arab. hebr. LW. rasan\\\", i.e. Arabic رَسَن and Hebrew רֶסֶן are loans FROM Iranian, not the other way round. The chart's own NOTE reports two contrary opinions and modern scholarship settles them in Nourai's favour: (a) MON:1654 / AFM:72 make rasan an Arabicised form of Persian rīsmān — this is wrong, since rīsmān belongs to the verb rēs- 'to spin' (Horn no. 617: 'risten „spinnen“, Praes. res-em, riste, resmān, rismān', root *raiś-), a different root, and an Arabic reshaping of rīsmān into rasan is phonetically impossible; (b) PLA:138 (Asbaghi) derives Arabic rasan from Pahlavi rasan — this is the accepted view, shared by Wiktionary ('Arabic رَسَن: borrowed from Middle Persian lsn' /rasan/ \\\"rope\\\"') and by Horn. The idiom رَسَن زدن 'to measure (land) with a rope' and the Ferdowsi line quoted are genuine classical usages of the noun.\",\n     \"derivation_fa\": \"«رَسَن» دنبالهٔ منظمِ فارسی میانهٔ rasan است که خود از ایرانی آغازین *racanáH و در نهایت از ریشهٔ هندوایرانی *rać- «بستن» می‌آید و هم‌ریشهٔ سنسکریت raśanā است. هرن (بند ۶۱۵، ص ۱۳۷) «رَسَن» فارسی را کنار raśanā سنسکریت می‌نهد و به‌صراحت می‌نویسد «رَسَن عربی و رِسِن عبری وام‌واژه‌اند»، یعنی جهتِ وام‌گیری از ایرانی به سامی است. یادداشتِ خودِ نمودار دو نظر متضاد را نقل می‌کند و پژوهش امروزی حق را به نورایی می‌دهد: ادعای معین و ادّی‌شیر که «رسن» تلفّظ عربیِ «ریسمان» باشد پذیرفتنی نیست، چون «ریسمان» از ستاک ریس‑/رشتن (ریشهٔ *raiś- «رشتن») است و ریشهٔ دیگری دارد (هرن بند ۶۱۷)؛ در برابر، اسبغی (وام‌واژه‌های فارسی در عربی، ص ۱۳۶) و ویکی‌واژه رَسَنِ عربی را معرَّبِ rasan پهلوی می‌دانند. ادعای نورایی درست است.\",\n     \"sources\": [W_RASAN, W_RASANA],\n     \"ref_check\": [\n      {\"ref\": \"HRN:137\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie, p.137 (HRN.txt leaf 158), no. 615: \\\"resen 'Strick'. ai. raśanā́ 'Strick, Riemen, Zügel, Gurt'; arm. LW. apa|rasan 'zügellos', erasan, erasanak 'Zügel' (Hübschmann, No. 96). arab. hebr. LW. rasan, bezw. רסן.\\\" Exactly the chart's derivation, and it also settles the note: Arabic and Hebrew have the word as a LOANWORD.\"},\n      {\"ref\": \"SNS:227\", \"status\": \"supports\", \"note\": \"See node #2: Tavoosi's index (SNS_pages.txt l.15896) lists 'rasan 227/3'.\"},\n      {\"ref\": \"MON:1654\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Fārsi is online only at vajehyab/abadis, where page numbers cannot be mapped, and the local files (MON_part1/part2, the 2-vol Adena abridgement) have different pagination and no رسن headword (grep 'رسن' in MON_part2.txt returns only compounds such as رسن‌باز). The substance of the claim is nevertheless refuted by Horn 137/617 and by Asbaghi 136.\"},\n      {\"ref\": \"AFM:72\", \"status\": \"partial\", \"note\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, printed p. ٧٢ = 72 (AFM.pdf leaf 74; read from the page image, saved to data/verification/sources/refs/ocr/AFM/72.vision.txt): \\\"(الرَسَن) الحبل والمَقوَد وهو חבל بالعبرانيّة ايضاً. وفرنكل يقول انّه مأخوذ من الفارسيّ رِيس المشتقّ هو ايضاً من رِيشتَن اي غزل (ص:١٠٠). او هو مشتقّ من رِيسيدن ومعناهُ غزل ايضاً او من رَسَان اي المُوصِّل.\\\" So Addi Shir does report (after Fraenkel) a derivation from Persian rīs / rīštan / rīsīdan 'to spin' — the family of rīsmān — which is roughly what Nourai paraphrases, but he does not say 'rasan is the Arabic pronunciation of rīsmān'; and he offers it as one of three alternatives. Page number is exactly right.\"},\n      {\"ref\": \"PLA:138\", \"status\": \"supports\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen 1988, s.v.: \\\"رسن rasan: 'Strick' aus pers. رسن rasan ← mp. rasan (Mackenzie s.v.), mand. risn, syr. ...\\\" — exactly Nourai's report. NB the entry stands on printed p.136, not 138 (PLA_pages.txt leaf 151, printed = leaf − 15; the running head of the leaf reads 'rasan 136 raff').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 615, p.137 and no. 617, p.137\", \"stance\": \"supports\", \"note\": \"no.615 'resen «Strick»' from Skt raśanā, with Arabic/Hebrew marked as loanwords; no.617 'risten «spinnen», Praes. res-em, riste, resūden, resmān, rismān' — proving rīsmān is a separate root, so rasan cannot be an Arabicisation of it.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. rasan\", \"stance\": \"supports\", \"note\": \"\\\"rasan [lsn' | N ~] rope\\\" — 'N ~' means the New Persian form is identical.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt)\", \"stance\": \"silent\", \"note\": \"No note on rasan; Hübschmann's no. 96 is cited by Horn for the Armenian loan only.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung, Etymological Dictionary of the Iranian Verb (CHEUNG.txt)\", \"stance\": \"silent\", \"note\": \"rasan is a noun, not a verbal stem; no entry.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Rem\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₁rem- 'to rest, be(come) calm; to prop, support'\",\n   \"note\": \"Pokorny p.864 heads the entry \\\"rem-, rems- ,ruhen, sich aufstützen; stützen'\\\" and lists, among other things, av. rāman- n. 'Ruhe, Friede', npers. rām 'Ruhe; fröhlich, heiter', Skt. rámate, Goth. rimis, Gk. ἠρέμα, Lith. rimti, Toch. AB räm-. Both the language label and the gloss of Nourai's root box are right; the modern laryngeal notation is *h₁rem- (Wiktionary, LIV *h₁remH-). One caveat that matters for node #5: Pokorny adds in the very first line that the connection of rem- with erǝ-/rē- 'ruhen' (his pp. 338 f., the root to which Germanic *rastō 'rest' is usually attached) \\\"ist fraglich\\\" — so the Germanic branch on this chart is not Pokorny's.\",\n   \"note_fa\": \"پوکورنی در ص ۸۶۴ مدخل «rem-, rems- «آرمیدن، تکیه دادن؛ نگاه داشتن»» را می‌آورد و از جمله اوستایی rāman- «آرامش، صلح»، فارسی نو rām «آرامش؛ شاد»، سنسکریت rámate، گوتی rimis، یونانی ἠρέμα و لیتوانیایی rimti را زیر آن فهرست می‌کند؛ پس نام زبان و معنیِ جعبهٔ ریشه در کتاب نورایی درست است. صورت امروزی این ریشه *h₁rem- است. تنها نکته آنکه خودِ پوکورنی در همان سطرِ نخست می‌گوید پیوندِ rem- با ریشهٔ erǝ-/rē- «آرمیدن» (ص ۳۳۸ به بعد) «مشکوک» است — و شاخهٔ ژرمنی این نمودار (rasta و rest) دقیقاً به آن ریشهٔ دوم تعلق دارد.\",\n   \"sources\": [W_H1REM, W_ARAM, W_RAM],\n   \"ref_check\": [\n    {\"ref\": \"POK:864\", \"status\": \"supports\", \"note\": \"POK_03.txt (printed p.864, between the page marks '864' and '865'): \\\"rem-, rems- ,ruhen, sich aufstützen; stützen'; im Germ. ,Latte, Leiste'? rom-ti ,Stütze'; Beziehung zu erǝ-, rē- ,ruhen' (S. 338 f.) ist fraglich. Ai. rámate ,steht still, ruht...'; av. ramya-, rāmōiδβǝm, rāmayeiti ,beruhigt'; ... av. rāman- n. ,Ruhe, Friede', npers. rām ,Ruhe; fröhlich, heiter' ... WP. II 371 f.\\\"\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.864\", \"stance\": \"supports\", \"note\": \"Root, gloss and the whole Iranian branch (Av. rāman-, NP rām) are Pokorny's own.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II pp.371-372 (WLD_Bd2_pages.txt leaves 375-376)\", \"stance\": \"supports\", \"note\": \"The leaf headers read 'rebh- — rem-' (371) and '372 rem-' with \\\"ai. rāma- m. ,Lust, Freude'\\\" — the source Pokorny cites as 'WP. II 371 f.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. rem- (IEC.txt l.14504)\", \"stance\": \"partial\", \"note\": \"\\\"rem- 'fit, join, strengthen'. Cf. rom-. WP II, 371. Skt. cf. ráme, mp. (1) 'stop'; ... Go. rimis, n. 'rest, peace'; MHG ram 'prop, support'; OE remian 'mend'; Li. remiu...\\\" — same root and same WP reference, but Mann foregrounds the 'prop, support' sense over 'rest'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 12.19 QUIET, pp.840-841 (SYN.txt l.21442 ff.)\", \"stance\": \"supports\", \"note\": \"Buck's table for 'quiet' lists \\\"Av. rāman- (sb.)\\\" and \\\"Goth. rimis (sb.)\\\", and the discussion (§4) adds \\\"Skt. ram- 'rest, stay', ... (with prefix) airime 'gently, quietly' ... Grk. ἠρέμα 'quiet, gentle'. Walde-P. 2.371 ff.\\\" — the same set Pokorny gives.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"No *rem- entry (the root has no English reflex in Watkins' list; 'rest' is not given a root either).\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"râman; airime; hu-rama; paiti-râman\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Two of the four forms are attested Avestan and exactly as glossed. (1) rāman- n. 'Ruhe, Friede' — Bartholomae, Altiranisches Wörterbuch col. 1523/24 (scan leaf 833, running head 'rāδinan- … rāmanivant-'): \\\"j., g. rāman- n. 'Ruhe, Friede'\\\", with the divine name Rāman xᵛāstra-; the verb rāmaiieiti 'calms' belongs with it. (2) airime Adv. 'quietly' — Bartholomae (scan leaf 137, col. ≈190): \\\"j. airime Adv. 'still, ruhig': airime gātūm hē nišhiδaiiata 'still soll er an seinem Ort sitzen bleiben' V.5.33, 16.6\\\", with the Pahlavi rendering armešt; the form is a prefixed *ǝ-rmi- (Greek ἠρέμα is the exact match), which is why Klein and Buck quote it. (3) and (4) are NOT attested Avestan words but Old Iranian reconstructions: *hu-rāma- 'well at ease' is inferred from Pahlavi hu-rām (Horn no.604, p.134-135, lists \\\"phlv. hu|rām, rām(i)šn, rāmēnītan\\\") and is the source of NP xorram, exactly as Hübschmann proposed (Persische Studien, note 479, p.55, after Fr. Müller WZKM 7, 373: \\\"so kann xurram mit Fr. Müller auf iran. *hu-rama- 'sich wohl freuend' zurückgeführt werden, vgl. skr. su-ramya-, su-ramaṇīya-\\\"); *pati-rāma- is inferred from Sogdian ptrʾm patrām 'calm, peace', which Gharib (Sogdian Dictionary no. 7813) explicitly analyses \\\"patrām (ptrʾm-) < *pati-rāma\\\", and from NP pedrām. So the box is right in substance but over-labels two reconstructions as Avestan.\",\n     \"derivation_fa\": \"از چهار صورتِ این جعبه دو تا اوستاییِ به‌گواهِ متن‌اند و معنیشان هم درست است: rāman- (خنثی) «آرامش، صلح» در فرهنگ ایرانی باستانِ بارتولومه ستون ۱۵۲۳–۱۵۲۴، و قید airime «آهسته، آرام» (بارتولومه، «airime gātūm hē nišhiδaiiata»؛ ترجمهٔ پهلوی آن armešt است) که خود *ǝ-rmi- پیشوندی است و درست با ἠρέμα یونانی می‌خواند. اما دو صورت دیگر اوستایی نیستند بلکه بازساختِ ایرانی باستان‌اند: *hu-rāma- از روی پهلوی hu-rām (هرن، بند ۶۰۴) و فارسی «خرّم» بازسازی شده (هوبشمان در «پژوهش‌های فارسی»، یادداشت ۴۷۹ ص ۵۵، به پیروی از فریدریش مولر)، و *pati-rāma- از روی سغدی ptrʾm (قریب، فرهنگ سغدی، شمارهٔ ۷۸۱۳: «patrām < *pati-rāma») و فارسی «پدرام». پس محتوای جعبه درست است ولی برچسبِ «اوستایی» برای دو صورتِ بازسازی‌شده گشاده‌دستانه است.\",\n     \"sources\": [W_H1REM, W_XORR, W_PEDRAM],\n     \"ref_check\": [\n      {\"ref\": \"POK:864\", \"status\": \"supports\", \"note\": \"Pokorny p.864 s.v. rem-: \\\"av. ramya- ,er soll ruhen', rāmōiδβǝm ,ihr möget stehen bleiben', rāmayeiti ,beruhigt' ... av. rāman- n. ,Ruhe, Friede'\\\" — rāman- is Pokorny's; airime is not in his list but is in WP II 371 and in Buck and Klein.\"},\n      {\"ref\": \"KLN:1335\", \"status\": \"supports\", \"note\": \"Klein, Comprehensive Etymological Dictionary, s.v. 'rest, n.' (KLN_1966.txt l.32546; scan leaf 710, printed pp. ~1334-1335, bracketed by '1330' on leaf 708 and '1336' on leaf 711): \\\"...fr. I.-E. base *erǝ-, *rē, 'to rest', whence also OE. rōw, ON. rā, MDu. roe, OHG. ruowa ..., 'rest', Avestic airime, 'quietly', Gk. ἐρωή, 'rest'...\\\" — Klein has airime, but under *erǝ-/*rē (Pok. 338), not under rem-.\"},\n      {\"ref\": \"SYN:841\", \"status\": \"supports\", \"note\": \"Buck 12.19 QUIET, pp.840-841: the word table gives \\\"Av. rāman- (sb.)\\\" for 'quiet', and §4 reads \\\"Goth. rimis ... : Skt. ram- 'rest, stay' ... also (with prefix) airime 'gently, quietly' ... Grk. ἠρέμα 'quiet, gentle'. Walde-P. 2.371 ff.\\\" Both of Nourai's attested forms, on exactly the cited page.\"},\n      {\"ref\": \"AEF:351\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asās-e Eštqāq-e Fārsi is the Persian translation of Horn (with Hübschmann's notes) and is not digitised anywhere (refs_online.json 'kind': 'catalog'). Checked against the German originals instead: Horn no. 604 (pp.134-135) and Hübschmann, Pers. Stud. note 479 (p.55) — see 'consulted'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1523-1524 (scan leaf 833) and col. ≈190 (leaf 137)\", \"stance\": \"supports\", \"note\": \"\\\"j., g. rāman- n. 'Ruhe, Friede'\\\" with the compound Rāman xᵛāstra-; and \\\"j. airime Adv. 'still, ruhig': airime gātūm hē nišhiδaiiata ... V.5.33, 16.6\\\". No entry for *hu-rāman- or *paiti-rāman- in Bartholomae (grep returns nothing).\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. rāmišn and hu-ramak (NYB_vol2_glossary.txt ll.2072, 3232)\", \"stance\": \"partial\", \"note\": \"\\\"rāmišn [l'mšn] pleasure, joy, peace ... — Av. (1511) ram- 'to repose', caus. rāmaya- 'to calm', (1524) rāman- 'peace'\\\" — confirms Bartholomae col. 1524 for rāman-. But Nyberg's \\\"hu-ramak [hwlmk'] having good herds of cattle ... Paz. hurama; translates Av. (1857) hvąθβa-\\\" is a different compound (from ramak 'herd'), a warning that Pahlavi hwlm- is ambiguous.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 604, pp.134-135\", \"stance\": \"supports\", \"note\": \"\\\"604. rām 'Ruhe; fröhlich, heiter', rāmiš, rāmišt. ap. vergl. Ariya|ramna-, Ἀριαράμνης; aw. rāman- 'Ruhe'; phlv. hu|rām, rām(i)šn, rāmēnītan; ai. rāmi- 'Lust'.\\\" — Horn has both Av. rāman- and Pahlavi hu-rām.\"},\n      {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 7812-7813 (SOD.txt ll.60424, 60442-60443)\", \"stance\": \"supports\", \"note\": \"\\\"patrām (ptrʾm-) © < *pati-rama\\\" and \\\"7813 ptrʾm B ... patrām © MP padrām\\\" — Gharib reconstructs exactly Nourai's *paiti-rāma(n).\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien note 479, p.55 (HUB.txt ll.1879-1892)\", \"stance\": \"supports\", \"note\": \"\\\"Ist xurram aus (dem von Vullers angeführten) xuram entstanden wie narr aus nar, so kann xurram mit Fr. Müller (WZKM 7, 373) auf iran. *hu-rama- 'sich wohl freuend' zurückgeführt werden, vgl. skr. su-ramya-, su-ramaṇīya-, su-raman- 'ergötzlich'.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"râm; ârâm; xorram; pedrâm\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four are regular Iranian continuations of *ram-. (1) رام rām 'calm, tame' < MP rām (MacKenzie: \\\"rām [l'm | M r'm] peace; cal. 21st day\\\") < PIr *rāma- < PIE *h₁rem-; the parenthesised derivatives are correct too — رامش rāmiš < MP rāmišn (Mo'in's footnote in Borhan-e Qāṭeʿ: \\\"پهلوی rāmišn\\\"), رامین Rāmīn (the Parthian romance name, MP Rāmīn), شهرام Šahrām 'king-of-peace', and رمه rama 'flock' < MP ramag (Mo'in's footnote: \\\"پهلوی ramak\\\"), semantically 'the resting/grazing herd'. (2) آرام ārām < MP ārām, ārāmīdan, from PIr *ā-rāma- = preverb ā- + rām-, so Wiktionary; Horn no.12 (p.5) gives \\\"ārām 'Ruhe', ārāmīdan, ārāmiš ... aw. āramayat 'er erfreute'; phlv. ārāmītan, ārām 'Ruhe'\\\", and Abolqāsemi FFD p.25 analyses \\\"آرام < ایرانی باستان *ā-ram-a-, ā پیشوند فعلی است ... ریشهٔ ram 'استراحت کردن' معنی می‌دهد. از ریشهٔ ram «آرمیدن» و «رامیدن» هم آمده‌اند\\\". (3) خرّم xorram < MP huram (Wiktionary: \\\"From Middle Persian hwlm /huram/\\\") < *hu-rāma- 'well at ease' (hu- 'good' + rām-); the gemination -rr- is a New Persian expressive doubling (Hübschmann compares narr from nar). (4) پدرام pedrām < *pati-rāma- (pad 'at, to' + rām), with the Sogdian cognate patrām; Wiktionary: \\\"An old compound. Akin to Sogdian ptrʾm /patrām/ 'calm, peace'. The first part is from Middle Persian pad ... The second part is from Proto-Indo-European *h₁rem-.\\\" The Vīs-o-Rāmīn couplet quoted uses both nā-padrām and the denominative bepadrāmad, a genuine 11th-century attestation.\",\n     \"derivation_fa\": \"هر چهار واژه دنبالهٔ منظمِ ستاک ram- ایرانی‌اند. «رام» از فارسی میانهٔ rām (مکنزی: «rām صلح، آرامش؛ روز بیست‌ویکم») از ایرانی باستان *rāma- و در نهایت *h₁rem- هندواروپایی؛ مشتق‌های داخل پرانتز هم درست‌اند: «رامش» < rāmišn پهلوی (حاشیهٔ معین بر برهان قاطع)، «رامین»، «شهرام»، و «رمه» < ramag پهلوی (باز هم حاشیهٔ معین) که از همان ریشه به معنی گلّهٔ آرام‌گرفته/چرنده است. «آرام» از *ā-rāma- ایرانی باستان با پیشوند فعلی ā-؛ هرن (بند ۱۲، ص ۵) «ārām، ārāmītan پهلوی» را می‌آورد و ابوالقاسمی در «فعل‌های فارسی دری» ص ۲۵ همین تحلیل را دارد. «خرّم» از huram فارسی میانه < *hu-rāma- «خوش‌آرام» (hu- «نیک» + rām)؛ مشدّد شدن ر در فارسی نو تأکیدی است (هوبشمان آن را با narr از nar می‌سنجد). «پدرام» از *pati-rāma- (pad + rām)، هم‌ریشه با ptrʾm سغدی. ادعای نورایی در هر چهار مورد درست است.\",\n     \"sources\": [W_RAM, W_ARAM, W_XORR, W_PEDRAM, W_H1REM],\n     \"ref_check\": [\n      {\"ref\": \"BQT:737,960\", \"status\": \"supports\", \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin, vol. 2. (a) p.≈737 = BQT_v2_pages.txt leaf 195 (the خُرّم cluster; the leaf carries the headword \\\"خرّم ـ بضم اول و فتح ثانی با تشدید. بمعنی شادمان و خوشوقت باشد\\\" and Moʿin's footnote \\\"پهلوی xurram (شاد) ... سانسکریت *su-ramya- (دوست داشتن) هوبشمان ۹۷۴\\\" — exactly the *hu-ram- etymology). (b) p.≈960: the leaf numbering (printed ≈ leaf + 540, fixed on leaves 431-433 = pp. 971-973) puts رام/رامش on leaves 391-392 and رمه on leaf 422, i.e. pp. ≈931-933 and ≈962 — so p.960 falls inside the رکـ/رمـ stretch rather than exactly on رام; the relevant footnotes are nevertheless there: leaf 391 \\\"پهلوی rāmišn (اسم مصدر)\\\" and \\\"رک: آرام، آرامیدن\\\", leaf 422 \\\"پهلوی ramak ... رک: رمه\\\". Substance supported; the page numeral may be off by a page or two (or Nourai's printing differs).\"},\n      {\"ref\": \"HRN:5\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.5 (HRN.txt leaf 26), no. 12: \\\"ārām 'Ruhe', ārāmīden, ārāmiš, ארם (jüd.-pers. Bibelübs.). aw. āramayat 'er erfreute'; phlv. ārāmītan, ārām 'Ruhe'. afγ. bel. LW. ārām. Vergl. rām (No. 604).\\\" Exactly Nourai's آرام.\"},\n      {\"ref\": \"AEF:351\", \"status\": \"not_checked\", \"note\": \"Not digitised (see entry-level note); its content is Horn + Hübschmann, both checked directly.\"},\n      {\"ref\": \"FAF:251\", \"status\": \"not_checked\", \"note\": \"Daneshgar, Farhang-e Aʿlām-e Fārsi: refs_online.json records 'kind': 'none' — nothing digitised on any platform. Presumably cited for the proper names Šahrām / Rāmin / Pedrām.\"},\n      {\"ref\": \"FFD:25\", \"status\": \"supports\", \"note\": \"Abolqāsemi, Feʿl-hā-ye Fārsi-ye Dari, printed p. ۲۵ = 25 (FFD_pages.txt, pdf page 30; printed = pdf − 5), s.v. آرامیدن. آرمیدن: \\\"«آرامید» مادهٔ ماضی جعلی است ... آرام < ایرانی باستان *ā-ram-a-, ā پیشوند فعلی است ... ram صورت بالانیدهٔ ریشهٔ ram است. ریشهٔ ram «استراحت کردن» معنی می‌دهد. از ریشهٔ ram «آرمیدن» و «رامیدن» هم آمده‌اند.\\\" Exactly the chart's ā-rām and rāmīdan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. rām, rām(ag), rāmēnīdan, rāmišn (PHD_mackenzie.txt ll.4326-4329)\", \"stance\": \"supports\", \"note\": \"\\\"rām [l'm | M r'm, N -] peace; cal. 21st day\\\"; \\\"rām(ag) [lm(h) | P rm, N rām(a)] herd, flock\\\"; \\\"rāmēnīdan ... give peace, pleasure\\\"; \\\"rāmišn [l'mšn' | M r'mšn, N rāmiš] peace, ease, pleasure\\\" — the Middle Persian stage of all of Nourai's Persian words except xorram/pedrām.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 12 (p.5) and no. 604 (pp.134-135)\", \"stance\": \"supports\", \"note\": \"no.12 ārām; no.604 \\\"rām 'Ruhe; fröhlich, heiter' ... aw. rāman- 'Ruhe'; phlv. hu|rām, rām(i)šn, rāmēnītan\\\" — Horn himself pairs rām with hu-rām, i.e. with xorram.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.55, note 479\", \"stance\": \"supports\", \"note\": \"Derives xurram from iran. *hu-rama- 'sich wohl freuend' (after Fr. Müller), rejecting the older equation with Skt. su-śarman-.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qāṭeʿ ed. Moʿin, vol.2 leaves 195, 391, 422\", \"stance\": \"supports\", \"note\": \"Moʿin's etymological footnotes: xurram < Pahlavi xurram; rāmiš < Pahlavi rāmišn; rama < Pahlavi ramak.\"},\n      {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi s.v. پدرام (MON_part1.txt ll.21597, 29645)\", \"stance\": \"supports\", \"note\": \"\\\"پدرام (ص.) خوش\\\" and \\\"پدرام (ص. مر.) آراسته، نیکو\\\" — Nourai's gloss 'pleasant / well arranged' is Moʿin's.\"},\n      {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors (FRS_pages.txt ll.14322-14324)\", \"stance\": \"supports\", \"note\": \"\\\"پدرام جایی بود خرّم و دلگشای ... جایی که خرّم بود آن را پدرام خوانند\\\" — the oldest Persian lexicographical gloss, and it explicitly equates pedrām with xorram.\"},\n      {\"src\": \"FFD\", \"where\": \"Abolqāsemi p.25 s.v. آرامیدن/آرمیدن\", \"stance\": \"supports\", \"note\": \"\\\"از ریشهٔ ram «آرمیدن» و «رامیدن» هم آمده‌اند\\\"; ā- analysed as a verbal preverb.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Riše-hā (ARY_latin_index_pages.txt ll.1425-1427)\", \"stance\": \"supports\", \"note\": \"The Latin index groups \\\"RAMTIS, RIMTI, RAMDITI (LITHUANIAN) | ARAMITAN, PAHLAVI | RAMISHN, RAM, RAMENITAN | RAMS (LATVIAN) | RAM (TOKHARIAN A)\\\" under one Persian headword — the same comparative set.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Old Persian\",\n     \"words\": \"ram\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Kent's Old Persian lexicon does list the root, but only as a bound element: \\\"ram- vb. 'be at peace', with prefix ā, in Ariyāramna-, q.v.\\\" (KNT.txt l.5859). The cross-referenced entry reads: \\\"Ariyāramna- sb. 'Ariaramnes', great-grandfather of Darius: Elam. har-ri-ia-ra-um-na, Akk. ar-ia-ra-am-na-', Gk. Ἀριαράμνης. From ariya- + pass. ptc. of ā-ram- (§131; Av. Skt. ram- 'to be at peace, to pacify'): 'Having the Aryans at peace'.\\\" So OP ram- is real, means exactly 'be at peace', and is an inherited *h₁rem- verb beside Av. ram-/rāmaiieiti and Skt. rámate; the only nuance is that it is attested solely inside the royal name Ariyāramna- (and in ā-ramna- 'having ... at peace'), never as a free verb form in the inscriptions. Horn no. 604 also cites the name (\\\"ap. vergl. Ariya|ramna-, Ἀριαράμνης\\\") as the Old Persian witness for NP rām.\",\n     \"derivation_fa\": \"کنت در واژه‌نامهٔ پارسی باستان ستاک را می‌آورد اما تنها به‌صورت جزء بسته: «ram- (فعل) «در آرامش بودن»، با پیشوند ā، در Ariyāramna-». ذیل همان نام می‌نویسد: «Ariyāramna- «آریارمنه»، جدّ داریوش؛ از ariya- + اسم مفعولِ ā-ram- (اوستایی و سنسکریت ram- «آرام بودن، آرام کردن»): «آن‌که آریاییان را در آرامش دارد»». پس ram- پارسی باستان واقعی است و معنیِ داده‌شده در نمودار درست است؛ تنها نکته آنکه این ستاک در کتیبه‌ها جز در همین نام شاهی گواهی نشده است. هرن نیز (بند ۶۰۴) همین نام را گواهِ پارسی‌باستانِ «رام» فارسی می‌گیرد.\",\n     \"sources\": [W_H1REM],\n     \"ref_check\": [\n      {\"ref\": \"KNT:206\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon (KNT.txt l.5859; scan leaf 230, lexicon offset leaf = printed + ~15 → printed p. ≈206-215, the 'r-' stretch of the lexicon which begins at p.164): \\\"ram- vb. 'be at peace', with prefix ā, in Ariyāramna-, q.v.\\\" and, at Ariyāramna- (l.5053): \\\"From ariya- + pass. ptc. of ā-ram- (§131; Av. Skt. ram- 'to be at peace, to pacify'): 'Having the Aryans at peace'.\\\" Nourai's gloss is Kent's, word for word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.vv. ram-, Ariyāramna-\", \"stance\": \"supports\", \"note\": \"As quoted; also notes that the alternative analyses (Foy 'Ariyā pl. + ramna-', Herzfeld 'Ariya- + aramna- to ar-') are rejected.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. rāman- (col. 1523-24) and the verb ram- (col. 1511, cited by Nyberg)\", \"stance\": \"supports\", \"note\": \"Bartholomae lemmatises Avestan ram- 'to repose' and rāman- 'peace' — the Avestan half of Kent's 'Av. Skt. ram-'.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no. 604, p.134\", \"stance\": \"supports\", \"note\": \"\\\"ap. vergl. Ariya|ramna-, Ἀριαράμνης\\\" — Horn uses the same Old Persian evidence.\"},\n      {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon (TLM.txt)\", \"stance\": \"silent\", \"note\": \"Tolman lemmatises the name Ariyāramna- but offers no separate root entry ram-.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": null,\n     \"words\": \"\",\n     \"verdict\": \"unverified\",\n     \"derivation\": \"There is nothing to verify: the box drawn to the right of the Old Persian 'ram' box is completely empty on the printed page — an outlined rectangle with no language header, no word, no gloss and no reference (confirmed on the page image, data/verification/sources/refs/ocr/BOOK/420.png). The extraction is faithful; this is a layout artefact of Nourai's chart (he draws a target box for the Old Persian branch and leaves it blank, as he does elsewhere on pages where a branch dies out). Most probably the intended descendant was the Middle/New Persian 'rām' already given in the Avestan branch, or a place/personal name he decided not to print. No claim is made, so no claim can be checked.\",\n     \"derivation_fa\": \"چیزی برای بررسی وجود ندارد: جعبه‌ای که در سمت راستِ جعبهٔ «ram» پارسی باستان کشیده شده در صفحهٔ چاپی کاملاً خالی است — کادری بی‌نام‌زبان، بی‌واژه، بی‌معنی و بی‌ارجاع (بر روی تصویر صفحه بررسی شد). پس خوانشِ اسکن درست عمل کرده و این نقصی در خودِ صفحه‌آرایی کتاب است؛ احتمالاً نورایی می‌خواسته دنبالهٔ فارسی میانه/نوِ شاخهٔ پارسی باستان را بیاورد و آن را ناتمام گذاشته است. چون ادعایی مطرح نشده، نه می‌توان آن را تأیید کرد نه رد.\",\n     \"sources\": [],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book.\"}],\n     \"consulted\": [{\"src\": \"BOOK\", \"where\": \"printed page 420 (pdf), image copied to data/verification/sources/refs/ocr/BOOK/420.png\", \"stance\": \"silent\", \"note\": \"The box is blank on the page itself — the JSON's note ('box is printed entirely blank in the source') is accurate.\"}]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Old High German\",\n     \"words\": \"rasta\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"OHG rasta is a real word, but the chart mis-states both its part of speech and its ancestry. (a) It is a feminine NOUN, not a verb: OHG rasta 'rest, repose', also 'a league of miles' (MHG raste, rast, NHG Rast), beside the verb OHG restēn 'to rest'; Klein, s.v. rest, groups it with Goth. rasta 'mile', ON rǫst 'league, distance after which one rests', OS resta 'resting place'. (b) The root: Germanic *rastō does NOT belong to *h₁rem-. Klein (p.1335, Nourai's own reference) derives the Teutonic base *ras- 'to rest, remain, dwell' \\\"fr. I.-E. base *erǝ-, *rē, 'to rest'\\\" — that is Pokorny p.338 f., a different entry from rem- (p.864); Pokorny himself writes at the head of rem- that the connection with erǝ-/rē- \\\"ist fraglich\\\". Wiktionary derives PWGmc *rastu from PGmc *rastō with no PIE etymon given, and Etymonline calls PGmc *rasto- \\\"a word of uncertain origin\\\", noting that the original sense may have been a measure of distance ('league') rather than 'repose'. Kroonen likewise keeps *rastō apart from the *rem- family. The only support for Nourai's grouping is older comparative work: Skeat (Concise Etym. Dict., s.v. Rest (1), p.≈404) allies AS. rest to \\\"Skt. ra-ti, pleasure, Gk. ἐρωή, rest (√RA)\\\" — and Skt. rāti-/rati- IS a rem- derivative in Pokorny p.864. So the chart follows a 19th-century view that modern scholarship does not accept.\",\n     \"derivation_fa\": \"rasta آلمانی علیای باستان واژه‌ای واقعی است، اما نمودار هم مقولهٔ دستوری و هم تبارِ آن را نادرست می‌دهد. نخست، rasta اسم مؤنث است («آسایش»، و نیز «فرسنگ/مرحلهٔ راه»)، نه فعل «آرمیدن»؛ فعل آن restēn است. دوم و مهم‌تر، *rastō ژرمنی به ریشهٔ *h₁rem- تعلق ندارد: کلاین در همان صفحه‌ای که نورایی ارجاع می‌دهد (۱۳۳۵) ستاک ژرمنی *ras- را از ریشهٔ هندواروپاییِ *erǝ-/*rē- «آرمیدن» می‌گیرد که مدخلی جداگانه در پوکورنی (ص ۳۳۸ به بعد) است؛ و خودِ پوکورنی در آغازِ مدخل rem- می‌نویسد پیوند این دو «مشکوک» است. ویکی‌واژه و اتیمآنلاین نیز ریشهٔ *rastō را «نامعلوم» می‌خوانند و احتمال می‌دهند معنیِ آغازینش «مسافت میان دو منزل» بوده باشد. تنها پشتوانهٔ نورایی دیدگاه کهنِ اسکیت است که rest را با rati- سنسکریت می‌سنجد. پژوهش امروزی این شاخه را از ریشهٔ Rem جدا می‌کند.\",\n     \"sources\": [E_REST, W_REST, W_RASTU],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1335\", \"status\": \"contradicts\", \"note\": \"Klein s.v. rest, n. (KLN_1966.txt l.32546-32547, leaf 710 ≈ printed p.1334-1335): \\\"ME. reste, fr. OE. rest, ræst, 'rest, resting-place; bed, grave', rel. to OS. rasta, 'resting-place, grave', ON. rǫst, 'distance, journey, mile', Goth. rasta, 'mile', OHG. rasta, MHG. raste, rast, G. Rast, 'rest, peace', fr. Teut. base *ras-, 'to rest, remain, dwell', ... fr. I.-E. base *erǝ-, *rē, 'to rest', whence also ... Avestic airime, 'quietly', Gk. ἐρωή, 'rest'.\\\" The reference Nourai cites does have OHG rasta, but assigns it to *erǝ-/*rē- (Pokorny 338), not to rem- (Pokorny 864) — so it contradicts the arrow as drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.864 (head of rem-) and pp.338 f. (erǝ-, rē-)\", \"stance\": \"contradicts\", \"note\": \"\\\"Beziehung zu erǝ-, rē- ,ruhen' (S. 338 f.) ist fraglich\\\" — Pokorny lists no Germanic *rast- under rem- at all; his Germanic material there is rama, rant, rimis, rim.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. rest, n., p.≈1335\", \"stance\": \"contradicts\", \"note\": \"As quoted: Teut. *ras- < I.-E. *erǝ-, *rē.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. 'Rest (1), repose' (SKT.txt l.15989; leaf 424, printed ≈ p.404)\", \"stance\": \"partial\", \"note\": \"\\\"Rest (1), repose. (E.) A.S. rest, ræst, rest. + Du. rust, Dan. Swed. rast, Icel. röst (the distance between two resting-places), Goth. rasta (a stage), O.H.G. resta, rest. Allied to Skt. ra-ti, pleasure, Gk. ἐρωή, rest. (√RA.)\\\" — Skeat's Skt. rati- is a rem- word in Pokorny, so the older literature did make Nourai's connection; but Skeat's √RA is really Pokorny's erǝ-/rē-.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II pp.371-372 (rem-)\", \"stance\": \"silent\", \"note\": \"The rem- entry has no Germanic *rast- material.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster (WEB_vol1.txt), grep 'rasta'\", \"stance\": \"silent\", \"note\": \"Nothing usable in the local OCR.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"rest\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"English rest (n.1 / v.1) is genuine and means what the chart implies, but it is not descended from Old High German rasta: it continues Old English ræst, rest 'rest; bed; intermission of labour; mental peace' (verb ræstan, restan), from Proto-West Germanic *rastu, Proto-Germanic *rastō — of which OHG rasta is the sister form, not the source (Etymonline: \\\"from Proto-Germanic *rasto- (source also of Old Saxon resta ..., Dutch rust, Old High German rasta, German Rast 'rest, peace, repose')\\\"). No borrowing from German into English is involved at any date; the chart's arrow is Nourai's usual 'oldest attested Germanic form stands for the branch' shorthand. ME reste > NE rest, with the noun and the originally distinct rest (n.2) 'remainder' (< OF reste < L. restāre) later confused with it. The ultimate root, as at node #5, is not *h₁rem-: PGmc *rastō is of disputed origin, usually put with PIE *h₁res-/*erǝ- 'to rest'.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی rest واقعی است، اما از rasta آلمانی علیای باستان نمی‌آید: دنبالهٔ انگلیسی باستانِ ræst/rest «آسایش؛ بستر؛ آرامش خاطر» (فعل ræstan/restan) است، از ژرمنی باستان *rastō، که rasta آلمانی هم‌ریشه (خواهرِ) آن است نه سرچشمه‌اش؛ اتیمآنلاین همین را می‌گوید. هیچ وام‌گیری‌ای از آلمانی به انگلیسی در کار نیست و پیکانِ نمودار همان شیوهٔ همیشگیِ نورایی است که کهن‌ترین صورتِ گواهی‌شدهٔ ژرمنی را نمایندهٔ کلِ شاخه می‌گیرد. ریشهٔ نهایی نیز — چنان‌که در گرهٔ ۵ گفته شد — *h₁rem- نیست؛ *rastō ژرمنی را معمولاً به *h₁res-/*erǝ- «آرمیدن» می‌بندند و منشأش را نامطمئن می‌دانند.\",\n     \"sources\": [E_REST, W_REST, W_RASTU],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The English box carries no reference in the book; the parent box cites KLN:1335, checked at node #5.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. rest, n., p.≈1335\", \"stance\": \"partial\", \"note\": \"\\\"ME. reste, fr. OE. rest, ræst ... rel. to OS. rasta ... OHG. rasta\\\" — 'rel. to', i.e. cognate, not 'fr.'; Klein's own wording excludes descent from OHG.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Rest (1), p.≈404\", \"stance\": \"partial\", \"note\": \"\\\"A.S. rest, ræst, rest. + Du. rust ... O.H.G. resta\\\" — the '+' sign is Skeat's cognate marker, again not descent.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls Standard Dictionary (FSD_vol1-4.txt), grep 'rasta'\", \"stance\": \"silent\", \"note\": \"The OCR of the Standard Dictionary yields no usable 'rest' etymology (hits are all noise such as 'contrasta', 'parastas').\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-420.json\"\nwith open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-420.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 420",
 "description": "Write and validate page-420.json"
}
```


### [2026-09-14T01:39:36.411Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<stdin>", line 190, in <module>
NameError: name 'null' is not defined
usage: python -m json.tool [-h] [--sort-keys] [--no-ensure-ascii]
                           [--json-lines]
                           [--indent INDENT | --tab | --no-indent | --compact]
                           [infile] [outfile]
python -m json.tool: error: argument infile: can't open '/home/sfmqrb/git/rishe/data/verification/page-420.json': [Errno 2] No such file or directory: '/home/sfmqrb/git/rishe/data/verification/page-420.json'
nodes verified: 0/9
node verdicts: {}
root verdicts: {}
ref checks: {}
books consulted: {} | by book: {}
pages without verification (1): 420
```


## [2026-09-14T01:44:28.130Z] TOOL CALL #76: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/gen-420.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nnull = None\n\nW_RASAN = \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D9%86\"\nW_RAM   = \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%85\"\nW_ARAM  = \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%A7%D9%85\"\nW_XORR  = \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D9%85\"\nW_REST  = \"https://en.wiktionary.org/wiki/rest\"\nE_REST  = \"https://www.etymonline.com/word/rest\"\nW_H1REM = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81rem-\"\nW_RASANA= \"https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A4%B6%E0%A4%A8%E0%A4%BE\"\nW_PEDRAM= \"https://en.wiktionary.org/wiki/%D9%BE%D8%AF%D8%B1%D8%A7%D9%85\"\nW_RASTU = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/rastu\"\n\ndoc = {\n \"pdf_page\": 420,\n \"book_page\": 390,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Rek, Reg 2\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *reḱ- / *reǵ- 'to bind, tie' (Pokorny 863 \\\"rek-, reg- ,binden'?\\\"); in practice reconstructable only as Proto-Indo-Iranian *rać- 'to bind, tie'\",\n   \"note\": \"Nourai's root box reproduces Pokorny p.863 exactly: \\\"rek-, reg- ,binden'?\\\" with the Sanskrit material raśanā / raśmi-. The language label (Indo-European) and the gloss ('to tie') are faithful. What Nourai drops is the question mark: Pokorny prints \\\"binden'?\\\" and Walde-Pokorny II 362 opens the entry with \\\"Unsicher\\\". Both split the material in two — the Indo-Iranian words point to a palatal *reḱ-, the Germanic ones (ON rakki, rekendi, OE racente, OHG rahhinza) to *reǵ- — so there is no secure single IE root; modern handbooks (Wiktionary, after Mayrhofer EWAia) reconstruct only PII *rać-. Hence 'plausible' rather than 'confirmed'. Note that the two neighbouring entries on the same page — \\\"2. rek- ,anordnen'\\\" (Skt. racayati, racana-) and \\\"rek-, reg- ,binden'?\\\" (Skt. raśanā) — are the source of the misprint in node #1.\",\n   \"note_fa\": \"ریشهٔ «Rek, Reg 2» با معنی «بستن» درست از پوکورنی (ص ۸۶۳) و والده‑پوکورنی (ج۲ ص۳۶۲) گرفته شده است؛ نام زبان (هندواروپایی آغازین) و معنی هم درست است. اما نورایی علامت پرسشِ پوکورنی را نیاورده: خودِ پوکورنی «binden?» می‌نویسد و والده‑پوکورنی مدخل را با واژهٔ «Unsicher» (نامطمئن) آغاز می‌کند، زیرا واژه‌های هندوایرانی (سنسکریت raśanā و raśmi-) به ریشهٔ کامی *reḱ- و واژه‌های ژرمنی به *reǵ- می‌رسند. ریشه‌شناسی امروزی تنها *rać- هندوایرانی آغازین را بازسازی می‌کند. بنابراین ادعای نورایی «با احتیاط پذیرفتنی» است.\",\n   \"sources\": [W_RASANA, W_RASAN],\n   \"ref_check\": [\n    {\"ref\": \"POK:863\", \"status\": \"supports\", \"note\": \"POK_03.txt (leaf 101-102, printed p.863, between the page marks '863' and '864'): \\\"rek-, reg- ,binden'? / Ai. rasanā f. ,Strick, Riemen, Gürtel', rasmi- m. ,Strang, Riemen, Zügel'; aschwed. hurraka (hurð-) ,Heck-Band', aisl. rakki m. ,Stropp zum Festhalten der Rahe', ags. racca m. ds., aisl. rekendi n. ... WP. II 362.\\\" Exactly Nourai's root, gloss and Sanskrit witness.\"},\n    {\"ref\": \"WLD2:362\", \"status\": \"supports\", \"note\": \"WLD_Bd2_pages.txt leaf 366 (header '362  reḱ-, reǵ'): \\\"rek-, reg- ,binden'? Unsicher. Ai. raśanā f. ,Strick, Riemen, Gürtel', raśmi m. ,Strang, Riemen, Zügel', zu idg. reḱ?; aschw. hurraka ... ahd. rahhinza f. dass. zu idg. reǵ? (Fick III⁴ 332 f.)\\\". Page number exactly right (offset: leaf = printed + 4, checked against leaves 370 = p.366 and 375 = p.371).\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.863 (POK_03.txt leaf 101)\", \"stance\": \"supports\", \"note\": \"\\\"rek-, reg- ,binden'? ... WP. II 362\\\" — with the question mark Nourai omits.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.362 (leaf 366)\", \"stance\": \"partial\", \"note\": \"\\\"Unsicher\\\" — Walde-Pokorny treat the root as doubtful and split the evidence between idg. reḱ? (Indo-Iranian) and idg. reǵ? (Germanic).\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. rek- (1) 'formulate, arrange, fix' (IEC.txt l.14488)\", \"stance\": \"silent\", \"note\": \"Mann has rek- (1) 'formulate, arrange, fix' (Skt. racayami) and rek- (2) 'utter, pronounce', but NO rek- 'bind'; grep for 'rasanā/raśanā' in IEC.txt returns nothing.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"No *rek-/*reg- 'bind' entry; the appendix lists only roots with English reflexes and this root has none.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"račana, rašanâ\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"račana, rašanâ\",\n     \"correct_form\": \"rašana, rašanâ (Skt. raśana n. / raśanā́ f.)\",\n     \"derivation\": \"The second form is right: Skt. raśanā́ f. (also raśana n.) 'cord, rope, string, thong; girdle, rein', from PII *raćanáH, built with the -ana- suffix on the root *rać- 'to bind, tie'; the same root gives Skt. raśmán-, raśmí- 'strap, rein'. The FIRST form is wrong. Nourai prints 'račana', i.e. Skt. racanā́ / racana-, which is a real Sanskrit word but means 'arranging, ordering, composing' (from rac- 'to arrange, produce') and belongs to the neighbouring Pokorny entry \\\"2. rek- ,anordnen'\\\" printed a few lines above on the very same page 863 (and on WP II 362, immediately above \\\"rek-, reg- ,binden'?\\\"). Nourai evidently copied the headword of the adjacent root; the intended form was surely 'rašana' (raśana), the neuter by-form of raśanā, since in his typeface č and š differ only in the letter under the háček. The printed page 420 of the dictionary does read 'račana' (image at data/verification/sources/refs/ocr/BOOK/420.png), so the extraction is faithful and the error is the book's.\",\n     \"derivation_fa\": \"صورت دوم درست است: سنسکریت raśanā́ (مؤنث) و raśana (خنثی) به معنی «ریسمان، بند، کمربند، افسار»، از هندوایرانی آغازین *raćanáH، ساخته‌شده از ریشهٔ *rać- «بستن» با پسوند -ana-؛ هم‌ریشه با raśmi- «تسمه، مهار». اما صورت نخست نادرست است: «račana» همان racanā́ سنسکریت است که معنی آن «آراستن، ترتیب دادن، سرودن» است و به ریشهٔ دیگری (rek- «نظم دادن») تعلق دارد که پوکورنی چند سطر بالاتر در همان صفحهٔ ۸۶۳ آورده است. ظاهراً نورایی مدخل مجاور را به‌اشتباه رونویسی کرده و مقصودش «rašana» بوده است (در حروف‌چینیِ او č و š تنها در حرف زیر هاچک تفاوت دارند). تصویر صفحهٔ ۴۲۰ نشان می‌دهد که خودِ کتاب «račana» چاپ کرده؛ پس خطای چاپی کتاب است، نه خطای خوانش اسکن.\",\n     \"sources\": [W_RASANA, W_RASAN],\n     \"ref_check\": [\n      {\"ref\": \"WLD2:362\", \"status\": \"partial\", \"note\": \"WLD Bd. II p.362 (leaf 366) gives under \\\"rek-, reg- ,binden'?\\\": \\\"Ai. raśanā f. ,Strick, Riemen, Gürtel'\\\" — the second of Nourai's two forms only. The first form 'račana' is in fact material of the entry printed immediately above on the same page: \\\"reḱ-, reǵ- ,anordnen'. Ai. racayati ,verfertigt, bildet', racana n. ,Ordnen, Betreiben'\\\" — a different root and a different meaning.\"},\n      {\"ref\": \"POK:863\", \"status\": \"partial\", \"note\": \"Same situation in Pokorny p.863: \\\"2. rek- ,anordnen': Ai. racayati ,verfertigt, bildet', racana- n. ,Ordnen, Betreiben'\\\" stands a few lines above \\\"rek-, reg- ,binden'?: Ai. rasanā f. ,Strick, Riemen, Gürtel'\\\". Pokorny supports 'rašanā = rope', not 'račana = rope'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.863\", \"stance\": \"partial\", \"note\": \"Supports raśanā 'Strick, Riemen, Gürtel'; assigns racana- to the separate root 'anordnen'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.362\", \"stance\": \"partial\", \"note\": \"\\\"Ai. raśanā f. ,Strick, Riemen, Gürtel', raśmi m. ... zu idg. reḱ?\\\" — but racana n. 'Ordnen, Betreiben' belongs to the preceding entry.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. rek- (1) (IEC.txt l.14488)\", \"stance\": \"contradicts\", \"note\": \"\\\"rek- (1) 'formulate, arrange, fix' ... Skt. racayami, v. 'prepare, produce, form, adorn, set in motion'\\\" — Mann too puts the racana-material under 'arrange', not 'bind'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt), grep 'raśanā/rasanā'\", \"stance\": \"silent\", \"note\": \"Buck's synonym sections have no entry for the Indo-Iranian word for 'rope'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"rasan\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The word itself is beyond doubt: MacKenzie's Concise Pahlavi Dictionary has \\\"rasan [lsn' | N ~] rope\\\", i.e. MP rasan written <lsn'> (Pahlavi <l> = /r/), continuing Old Iranian *racana- with regular Middle Persian loss of the final vowel and the Iranian development *ć > s (whereas Indo-Aryan gives ś). What is drawn wrongly is the ROUTE: the chart makes Pahlavi rasan a descendant of the Sanskrit word, but MP rasan is its sister, not its child — Wiktionary (citing Parthian rasan) derives it from Proto-Iranian *racanáH beside Proto-Indo-Aryan *raśanáH, both from PII *raćanáH. The Armenian loan aṙasan (from an Iranian, not an Indian, source) shows the Iranian branch existed independently. This is Nourai's general chart convention (Sanskrit stands in for the Indo-Iranian parent), so the claim is acceptable with that caveat.\",\n     \"derivation_fa\": \"خودِ واژه قطعی است: مکنزی در فرهنگ کوچک پهلوی می‌آورد «rasan [lsn'] رسن، ریسمان». فارسی میانهٔ rasan از ایرانی باستان *racana- می‌آید؛ *ć هندوایرانی در شاخهٔ ایرانی به s و در شاخهٔ هندی به ś بدل شده است (از این‌روست که سنسکریت raśanā دارد و ایرانی rasan). اما مسیرِ رسم‌شده در نمودار درست نیست: پهلوی rasan فرزندِ واژهٔ سنسکریت نیست بلکه هم‌ریشه (خواهرِ) آن است؛ ویکی‌واژه آن را از ایرانی آغازین *racanáH (در کنار پارتی rasan) می‌گیرد و وام‌واژهٔ ارمنی aṙasan نیز از منبعی ایرانی گرفته شده نه هندی. چون نورایی معمولاً سنسکریت را به‌جای «نیایِ هندوایرانی» می‌نشاند، ادعا با همین قید پذیرفتنی است.\",\n     \"sources\": [W_RASAN, W_RASANA],\n     \"ref_check\": [\n      {\"ref\": \"SNS:227\", \"status\": \"supports\", \"note\": \"Tavoosi, Vāže-nāme-ye Šāyast ne Šāyast: the word index (SNS_pages.txt l.15896) lists \\\"rasan 227/3\\\" — the text page/line the glossary entry cites; the glossary entry itself (SNS_pages.txt l.9047) carries the Latin transliteration 'rasan' beside a Persian gloss (the Persian OCR is unusable). So the citation points at a genuine Pahlavi attestation of rasan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.v. rasan (PHD.txt l.557; PHD_mackenzie.txt l.4344)\", \"stance\": \"supports\", \"note\": \"\\\"rasan [lsn' | N ~] rope\\\" — Pahlavi rasan 'rope', with the New Persian form identical.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"The glossary has rāmišn, ramak, hu-ramak etc. but no entry for rasan (grep '^rasan' returns nothing).\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 615, p.137\", \"stance\": \"partial\", \"note\": \"Horn takes NP \\\"resen 'Strick'\\\" straight from \\\"ai. raśanā 'Strick, Riemen, Zügel, Gurt'\\\" without citing a Pahlavi form — so he supports the word but not an explicit Pahlavi stage.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"rasan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP رَسَن rasan 'rope, cord' is the regular continuation of MP rasan (<lsn'>, MacKenzie p.70), itself from Proto-Iranian *racanáH < PII *raćanáH, root *rać- 'to bind' — the Iranian cognate of Skt. raśanā́. Horn, Grundriss no. 615 (p.137) sets NP resen 'Strick' beside Skt. raśanā, notes the Armenian loans erasan / apa-rasan 'Zügel', and states expressly \\\"arab. hebr. LW. rasan\\\", i.e. Arabic رَسَن and Hebrew רֶסֶן are loans FROM Iranian, not the reverse. The chart's own NOTE reports two contrary opinions, and modern scholarship settles them in Nourai's favour: (a) MON:1654 / AFM:72 make rasan an Arabicised form of Persian rīsmān — this is wrong, since rīsmān belongs to the verb rēs- 'to spin' (Horn no. 617: \\\"risten 'spinnen', Praes. res-em, riste, resmān, rismān\\\", root *raiś-), a different root, and an Arabic reshaping of rīsmān into rasan is phonetically impossible; (b) PLA:138 (Asbaghi) derives Arabic rasan from Pahlavi rasan — this is the accepted view, shared by Wiktionary ('Arabic رَسَن: borrowed from Middle Persian lsn' /rasan/ \\\"rope\\\"') and by Horn. The idiom رَسَن زدن 'to measure (land) with a rope' and the Ferdowsī line quoted are genuine classical usages of the noun.\",\n     \"derivation_fa\": \"«رَسَن» دنبالهٔ منظمِ فارسی میانهٔ rasan است که خود از ایرانی آغازین *racanáH و در نهایت از ریشهٔ هندوایرانی *rać- «بستن» می‌آید و هم‌ریشهٔ سنسکریت raśanā است. هرن (بند ۶۱۵، ص ۱۳۷) «رسن» فارسی را کنار raśanā سنسکریت می‌نهد و به‌صراحت می‌نویسد «رَسَنِ عربی و רסן عبری وام‌واژه‌اند»، یعنی جهتِ وام‌گیری از ایرانی به سامی است. یادداشتِ خودِ نمودار دو نظر متضاد را نقل می‌کند و پژوهش امروزی حق را به نورایی می‌دهد: ادعای معین و ادّی‌شیر که «رسن» تلفّظ عربیِ «ریسمان» باشد پذیرفتنی نیست، چون «ریسمان» از ستاک ریس‑/رشتن (ریشهٔ *raiś- «رشتن») است و ریشهٔ دیگری دارد (هرن، بند ۶۱۷)؛ در برابر، اسبغی («وام‌واژه‌های فارسی در عربی»، ص ۱۳۶) و ویکی‌واژه رَسَنِ عربی را معرَّبِ rasan پهلوی می‌دانند. ادعای نورایی درست است.\",\n     \"sources\": [W_RASAN, W_RASANA],\n     \"ref_check\": [\n      {\"ref\": \"HRN:137\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie, p.137 (HRN.txt leaf 158), no. 615: \\\"resen 'Strick'. ai. raśanā́ 'Strick, Riemen, Zügel, Gurt'; arm. LW. apa|rasan 'zügellos', erasan, erasanak 'Zügel' (Hübschmann, No. 96). arab. hebr. LW. rasan, bezw. רסן.\\\" Exactly the chart's derivation, and it settles the note: Arabic and Hebrew have the word as a LOANWORD.\"},\n      {\"ref\": \"SNS:227\", \"status\": \"supports\", \"note\": \"See node #2: Tavoosi's index (SNS_pages.txt l.15896) lists 'rasan 227/3'.\"},\n      {\"ref\": \"MON:1654\", \"status\": \"not_checked\", \"note\": \"Moʿin's Farhang-e Fārsi is online only at vajehyab/abadis, where page numbers cannot be mapped, and the local files (MON_part1/part2 = the 2-vol Adena abridgement) have different pagination and no رسن headword (grep 'رسن' in MON_part2.txt yields only compounds such as رسن‌باز). The substance of the claim is refuted independently by Horn 137/617 and Asbaghi 136.\"},\n      {\"ref\": \"AFM:72\", \"status\": \"partial\", \"note\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, printed p. ٧٢ = 72 (AFM.pdf leaf 74; read from the page image, transcript saved at data/verification/sources/refs/ocr/AFM/72.vision.txt): \\\"(الرَسَن) الحبل والمَقوَد وهو חבל بالعبرانيّة ايضاً. وفرنكل يقول انّه مأخوذ من الفارسيّ رِيس المشتقّ هو ايضاً من رِيشتَن اي غزل (ص:١٠٠). او هو مشتقّ من رِيسيدن ومعناهُ غزل ايضاً او من رَسَان اي المُوصِّل.\\\" Addi Shir does report (after Fraenkel) a derivation from Persian rīs / rīštan / rīsīdan 'to spin' — the family of rīsmān — which is roughly what Nourai paraphrases; but he does not say 'rasan is the Arabic pronunciation of rīsmān', and he offers it as one of three alternatives. Page number exactly right.\"},\n      {\"ref\": \"PLA:138\", \"status\": \"supports\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen (1988), s.v.: \\\"رسن rasan: 'Strick' aus pers. رسن rasan ← mp. rasan (Mackenzie s.v.), mand. risn, syr. ...\\\" — exactly Nourai's report. NB the entry stands on printed p.136, not 138 (PLA_pages.txt leaf 151; printed = leaf − 15; the leaf's running head reads 'rasan 136 raff').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 615, p.137 and no. 617, p.137\", \"stance\": \"supports\", \"note\": \"no.615 \\\"resen 'Strick'\\\" from Skt raśanā, with Arabic/Hebrew marked as loanwords; no.617 \\\"risten 'spinnen', Praes. res-em, riste, resūden, resmān, rismān\\\" — proving rīsmān is a separate root, so rasan cannot be an Arabicisation of it.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. rasan\", \"stance\": \"supports\", \"note\": \"\\\"rasan [lsn' | N ~] rope\\\" — 'N ~' means the New Persian form is identical.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt)\", \"stance\": \"silent\", \"note\": \"No note on rasan; his no. 96, cited by Horn, concerns the Armenian loan only.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung, Etymological Dictionary of the Iranian Verb (CHEUNG.txt)\", \"stance\": \"silent\", \"note\": \"rasan is a noun, not a verbal stem; no entry.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Rem\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₁rem- 'to rest, be(come) calm; to prop, support'\",\n   \"note\": \"Pokorny p.864 heads the entry \\\"rem-, rems- ,ruhen, sich aufstützen; stützen'\\\" and lists, among others, av. rāman- n. 'Ruhe, Friede', npers. rām 'Ruhe; fröhlich, heiter', Skt. rámate, Goth. rimis, Gk. ἠρέμα, Lith. rimti, Toch. AB räm-. Both the language label and the gloss of Nourai's root box are right; the modern notation is *h₁rem- (LIV *h₁remH-). One caveat matters for node #5: Pokorny adds in the very first line that the connection of rem- with erǝ-/rē- 'ruhen' (his pp. 338 f., the root to which Germanic *rastō 'rest' is usually attached) \\\"ist fraglich\\\" — so the Germanic branch of this chart is not Pokorny's.\",\n   \"note_fa\": \"پوکورنی در ص ۸۶۴ مدخل «rem-, rems-» به معنی «آرمیدن، تکیه دادن؛ نگاه داشتن» را می‌آورد و از جمله اوستایی rāman- «آرامش، صلح»، فارسی نو rām «آرامش؛ شاد»، سنسکریت rámate، گوتی rimis، یونانی ἠρέμα و لیتوانیایی rimti را زیر آن فهرست می‌کند؛ پس نام زبان و معنیِ جعبهٔ ریشه در کتاب نورایی درست است. صورت امروزی این ریشه *h₁rem- است. تنها نکته آنکه خودِ پوکورنی در همان سطرِ نخست می‌گوید پیوندِ rem- با ریشهٔ erǝ-/rē- «آرمیدن» (ص ۳۳۸ به بعد) «مشکوک» است — و شاخهٔ ژرمنیِ این نمودار (rasta و rest) دقیقاً به آن ریشهٔ دوم تعلق دارد.\",\n   \"sources\": [W_H1REM, W_ARAM, W_RAM],\n   \"ref_check\": [\n    {\"ref\": \"POK:864\", \"status\": \"supports\", \"note\": \"POK_03.txt (printed p.864, between the page marks '864' and '865'): \\\"rem-, rems- ,ruhen, sich aufstützen; stützen'; im Germ. ,Latte, Leiste'? rom-ti ,Stütze'; Beziehung zu erǝ-, rē- ,ruhen' (S. 338 f.) ist fraglich. Ai. rámate ,steht still, ruht ...'; av. ramya-, rāmōiδβǝm, rāmayeiti ,beruhigt'; ... av. rāman- n. ,Ruhe, Friede', npers. rām ,Ruhe; fröhlich, heiter' ... WP. II 371 f.\\\"\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.864\", \"stance\": \"supports\", \"note\": \"Root, gloss and the whole Iranian branch (Av. rāman-, NP rām) are Pokorny's own.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II pp.371-372 (WLD_Bd2_pages.txt leaves 375-376)\", \"stance\": \"supports\", \"note\": \"Leaf headers read 'rebh- — rem-' (p.371) and '372 rem-' with \\\"ai. rāma- m. ,Lust, Freude'\\\" — the source Pokorny cites as 'WP. II 371 f.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. rem- (IEC.txt l.14504)\", \"stance\": \"partial\", \"note\": \"\\\"rem- 'fit, join, strengthen'. Cf. rom-. WP II, 371. Skt. cf. ráme, mp. (1) 'stop'; ... Go. rimis, n. 'rest, peace'; MHG ram 'prop, support'; OE remian 'mend'; Li. remiu ...\\\" — same root and same WP reference, but Mann foregrounds 'prop, support' over 'rest'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 12.19 QUIET, pp.840-841 (SYN.txt l.21442 ff.)\", \"stance\": \"supports\", \"note\": \"Buck's table for 'quiet' lists \\\"Av. rāman- (sb.)\\\" and \\\"Goth. rimis (sb.)\\\"; the discussion (§4) adds \\\"Skt. ram- 'rest, stay' ... also (with prefix) airime 'gently, quietly' ... Grk. ἠρέμα 'quiet, gentle'. Walde-P. 2.371 ff.\\\"\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"No *rem- entry — the root has no English reflex in Watkins' list, and 'rest' is given no root either.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"râman; airime; hu-rama; paiti-râman\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Two of the four forms are attested Avestan and exactly as glossed. (1) rāman- n. 'Ruhe, Friede' — Bartholomae, Altiranisches Wörterbuch col. 1523/24 (scan leaf 833, running head 'rāδinan- … rāmanivant-'): \\\"j., g. rāman- n. 'Ruhe, Friede'\\\", with the divine name Rāman xᵛāstra-; the verb rāmaiieiti 'calms' belongs with it. (2) airime Adv. 'quietly' — Bartholomae (scan leaf 137, col. ≈190): \\\"j. airime Adv. 'still, ruhig': airime gātūm hē nišhiδaiiata 'still soll er an seinem Ort sitzen bleiben' V.5.33, 16.6\\\", with the Pahlavi rendering armešt; the form is a prefixed *ǝ-rmi- (Gk. ἠρέμα is the exact match), which is why Klein and Buck quote it. (3) and (4) are NOT attested Avestan words but Old Iranian reconstructions: *hu-rāma- 'well at ease' is inferred from Pahlavi hu-rām (Horn no.604, pp.134-135: \\\"phlv. hu|rām, rām(i)šn, rāmēnītan\\\") and is the source of NP xorram, exactly as Hübschmann proposed (Persische Studien, note 479, p.55, after Fr. Müller WZKM 7, 373: \\\"so kann xurram mit Fr. Müller auf iran. *hu-rama- 'sich wohl freuend' zurückgeführt werden, vgl. skr. su-ramya-, su-ramaṇīya-\\\"); *pati-rāma- is inferred from Sogdian ptrʾm patrām 'calm, peace', which Gharib (Sogdian Dictionary no. 7813) analyses \\\"patrām (ptrʾm-) < *pati-rama\\\", and from NP pedrām. So the box is right in substance but over-labels two reconstructions as Avestan.\",\n     \"derivation_fa\": \"از چهار صورتِ این جعبه دو تا اوستاییِ گواهی‌شده‌اند و معنیشان هم درست است: rāman- (خنثی) «آرامش، صلح» در فرهنگ ایرانی باستانِ بارتولومه ستون ۱۵۲۳–۱۵۲۴، و قید airime «آهسته، آرام» («airime gātūm hē nišhiδaiiata»، وندیداد ۵٫۳۳ و ۱۶٫۶؛ ترجمهٔ پهلوی آن armešt است) که خود *ǝ-rmi- پیشوندی است و درست با ἠρέμα یونانی می‌خواند. اما دو صورت دیگر اوستایی نیستند بلکه بازساختِ ایرانی باستان‌اند: *hu-rāma- از روی پهلوی hu-rām (هرن، بند ۶۰۴) و فارسی «خرّم» بازسازی شده — همان که هوبشمان در «پژوهش‌های فارسی» یادداشت ۴۷۹ ص ۵۵ به پیروی از فریدریش مولر پیشنهاد کرده — و *pati-rāma- از روی سغدی ptrʾm (قریب، فرهنگ سغدی، شمارهٔ ۷۸۱۳: «patrām < *pati-rama») و فارسی «پدرام». پس محتوای جعبه درست است ولی برچسبِ «اوستایی» برای دو صورتِ بازسازی‌شده گشاده‌دستانه است.\",\n     \"sources\": [W_H1REM, W_XORR, W_PEDRAM],\n     \"ref_check\": [\n      {\"ref\": \"POK:864\", \"status\": \"supports\", \"note\": \"Pokorny p.864 s.v. rem-: \\\"av. ramya- ,er soll ruhen', rāmōiδβǝm ,ihr möget stehen bleiben', rāmayeiti ,beruhigt' ... av. rāman- n. ,Ruhe, Friede'\\\" — rāman- is Pokorny's; airime is not in his list but is in WP II 371, in Buck and in Klein.\"},\n      {\"ref\": \"KLN:1335\", \"status\": \"supports\", \"note\": \"Klein, Comprehensive Etymological Dictionary, s.v. 'rest, n.' (KLN_1966.txt l.32546; scan leaf 710, printed pp. ~1334-1335, bracketed by '1330' on leaf 708 and '1336' on leaf 711): \\\"... fr. I.-E. base *erǝ-, *rē, 'to rest', whence also OE. rōw, ON. rā, MDu. roe, OHG. ruowa ..., 'rest', Avestic airime, 'quietly', Gk. ἐρωή, 'rest' ...\\\" — Klein does have airime, but under *erǝ-/*rē (Pokorny 338), not under rem-.\"},\n      {\"ref\": \"SYN:841\", \"status\": \"supports\", \"note\": \"Buck 12.19 QUIET, pp.840-841: the word table gives \\\"Av. rāman- (sb.)\\\" for 'quiet', and §4 reads \\\"Goth. rimis ... : Skt. ram- 'rest, stay' ... also (with prefix) airime 'gently, quietly' ... Grk. ἠρέμα 'quiet, gentle'. Walde-P. 2.371 ff.\\\" Both of Nourai's attested forms, on exactly the cited page.\"},\n      {\"ref\": \"AEF:351\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asās-e Eštqāq-e Fārsi is the Persian translation of Horn (with Hübschmann's notes) and is not digitised anywhere (refs_online.json 'kind': 'catalog'). Checked against the German originals instead: Horn no. 604 (pp.134-135) and Hübschmann, Pers. Stud. note 479 (p.55) — see 'consulted'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1523-1524 (scan leaf 833) and col. ≈190 (leaf 137)\", \"stance\": \"supports\", \"note\": \"\\\"j., g. rāman- n. 'Ruhe, Friede'\\\" with the compound Rāman xᵛāstra-; and \\\"j. airime Adv. 'still, ruhig': airime gātūm hē nišhiδaiiata ... V.5.33, 16.6\\\". No entry for *hu-rāman- or *paiti-rāman- (grep returns nothing).\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.vv. rāmišn, hu-ramak (NYB_vol2_glossary.txt ll.3232, 2072)\", \"stance\": \"partial\", \"note\": \"\\\"rāmišn [l'mšn] pleasure, joy, peace ... — Av. (1511) ram- 'to repose', caus. rāmaya- 'to calm', (1524) rāman- 'peace'\\\" — independently confirms Bartholomae col. 1524. But Nyberg's \\\"hu-ramak [hwlmk'] having good herds of cattle ... Paz. hurama; translates Av. (1857) hvąθβa-\\\" is a different compound (from ramak 'herd') — a warning that Pahlavi hwlm- is ambiguous.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 604, pp.134-135\", \"stance\": \"supports\", \"note\": \"\\\"604. rām 'Ruhe; fröhlich, heiter', rāmiš, rāmišt. ap. vergl. Ariya|ramna-, Ἀριαράμνης; aw. rāman- 'Ruhe'; phlv. hu|rām, rām(i)šn, rāmēnītan; ai. rāmi- 'Lust'.\\\" — Horn has both Av. rāman- and Pahlavi hu-rām.\"},\n      {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary nos. 7812-7813 (SOD.txt ll.60424, 60442-60443)\", \"stance\": \"supports\", \"note\": \"\\\"patrām (ptrʾm-) © < *pati-rama\\\" and \\\"7813 ptrʾm B ... patrām © MP padrām\\\" — Gharib reconstructs exactly Nourai's *paiti-rāma(n).\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien note 479, p.55 (HUB.txt ll.1879-1892)\", \"stance\": \"supports\", \"note\": \"\\\"Ist xurram aus (dem von Vullers angeführten) xuram entstanden wie narr aus nar, so kann xurram mit Fr. Müller (WZKM 7, 373) auf iran. *hu-rama- 'sich wohl freuend' zurückgeführt werden, vgl. skr. su-ramya-, su-ramaṇīya-, su-raman- 'ergötzlich'.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"râm; ârâm; xorram; pedrâm\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four are regular Iranian continuations of *ram-. (1) رام rām 'calm, tame' < MP rām (MacKenzie: \\\"rām [l'm | M r'm] peace; cal. 21st day\\\") < PIr *rāma- < PIE *h₁rem-; the parenthesised derivatives are correct too — رامش rāmiš < MP rāmišn (Moʿin's footnote in Borhān-e Qāṭeʿ: \\\"پهلوی rāmišn\\\"), رامین Rāmīn (the Parthian romance name), شهرام Šahrām 'king-of-peace', and رمه rama 'flock' < MP ramag (Moʿin's footnote: \\\"پهلوی ramak\\\"), semantically 'the resting/grazing herd'. (2) آرام ārām < MP ārām, ārāmītan, from PIr *ā-rāma- = preverb ā- + rām-; Horn no.12 (p.5): \\\"ārām 'Ruhe', ārāmīden, ārāmiš ... aw. āramayat 'er erfreute'; phlv. ārāmītan, ārām 'Ruhe'\\\", and Abolqāsemi FFD p.25: \\\"آرام < ایرانی باستان *ā-ram-a-, ā پیشوند فعلی است ... ریشهٔ ram «استراحت کردن» معنی می‌دهد. از ریشهٔ ram «آرمیدن» و «رامیدن» هم آمده‌اند\\\". (3) خرّم xorram < MP huram (Wiktionary: \\\"From Middle Persian hwlm /huram/\\\") < *hu-rāma- 'well at ease' (hu- 'good' + rām-); the geminate -rr- is a New Persian expressive doubling (Hübschmann compares narr from nar). (4) پدرام pedrām < *pati-rāma- (pad 'at, to' + rām), with the Sogdian cognate patrām; Wiktionary: \\\"An old compound. Akin to Sogdian ptrʾm /patrām/ 'calm, peace'. The first part is from Middle Persian pad ... The second part is from Proto-Indo-European *h₁rem-.\\\" The Vīs-o-Rāmīn couplet quoted uses both nā-padrām and the denominative bepadrāmad — a genuine 11th-century attestation.\",\n     \"derivation_fa\": \"هر چهار واژه دنبالهٔ منظمِ ستاک ram- ایرانی‌اند. «رام» از فارسی میانهٔ rām (مکنزی: «rām آرامش، صلح؛ روز بیست‌ویکم») از ایرانی باستان *rāma- و در نهایت *h₁rem- هندواروپایی است؛ مشتق‌های داخل پرانتز هم درست‌اند: «رامش» از rāmišn پهلوی (حاشیهٔ معین بر برهان قاطع)، «رامین»، «شهرام»، و «رمه» از ramag پهلوی (باز هم حاشیهٔ معین) که از همان ریشه به معنی گلّهٔ آرام‌گرفته/چرنده است. «آرام» از *ā-rāma- ایرانی باستان با پیشوند فعلی ā-؛ هرن (بند ۱۲، ص ۵) «ārām و ārāmītan پهلوی» را می‌آورد و ابوالقاسمی در «فعل‌های فارسی دری» ص ۲۵ همین تحلیل را دارد. «خرّم» از huram فارسی میانه و آن از *hu-rāma- «خوش‌آرام» (hu- «نیک» + rām)؛ مشدّد شدن «ر» در فارسی نو تأکیدی است (هوبشمان آن را با narr از nar می‌سنجد). «پدرام» از *pati-rāma- (pad + rām)، هم‌ریشه با ptrʾm سغدی. ادعای نورایی در هر چهار مورد درست است.\",\n     \"sources\": [W_RAM, W_ARAM, W_XORR, W_PEDRAM, W_H1REM],\n     \"ref_check\": [\n      {\"ref\": \"BQT:737,960\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, vol. 2. (a) p.≈737 = BQT_v2_pages.txt leaf 195, the خُرّم cluster: headword \\\"خرّم ـ بضم اول و فتح ثانی با تشدید. بمعنی شادمان و خوشوقت باشد\\\" with Moʿin's footnote \\\"پهلوی xurram (شاد) ... سانسکریت *su-ramya- (دوست داشتن) هوبشمان ۹۷۴\\\" — precisely the *hu-ram- etymology. (b) p.≈960: the vol-2 offset (printed ≈ leaf + 540, fixed on leaves 431-433 = pp. 971-973) puts رام/رامش on leaves 391-392 and رمه on leaf 422, i.e. pp. ≈931-933 and ≈962; p.960 therefore falls in the رکـ/رمـ stretch rather than exactly on رام, but the relevant footnotes are there: leaf 391 \\\"پهلوی rāmišn (اسم مصدر)\\\" with \\\"رک: آرام، آرامیدن\\\", leaf 422 \\\"پهلوی ramak ... رک: رمه\\\". Substance supported; the page numeral may be off by a page or two (or Nourai's printing differs slightly).\"},\n      {\"ref\": \"HRN:5\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.5 (HRN.txt leaf 26), no. 12: \\\"ārām 'Ruhe', ārāmīden, ārāmiš, ארם (jüd.-pers. Bibelübs.). aw. āramayat 'er erfreute'; phlv. ārāmītan, ārām 'Ruhe'. afγ. bel. LW. ārām. Vergl. rām (No. 604).\\\" Exactly Nourai's آرام.\"},\n      {\"ref\": \"AEF:351\", \"status\": \"not_checked\", \"note\": \"Not digitised (see the Avestan node); its content is Horn + Hübschmann, both checked directly.\"},\n      {\"ref\": \"FAF:251\", \"status\": \"not_checked\", \"note\": \"Daneshgar, Farhang-e Aʿlām-e Fārsi: refs_online.json records 'kind': 'none' — nothing digitised on any platform. Presumably cited for the proper names Šahrām / Rāmīn / Pedrām.\"},\n      {\"ref\": \"FFD:25\", \"status\": \"supports\", \"note\": \"Abolqāsemi, Feʿl-hā-ye Fārsi-ye Dari, printed p. ۲۵ = 25 (FFD_pages.txt, pdf page 30; printed = pdf − 5), s.v. آرامیدن. آرمیدن: \\\"«آرامید» مادهٔ ماضی جعلی است ... آرام < ایرانی باستان *ā-ram-a-, ā پیشوند فعلی است ... ram صورت بالانیدهٔ ریشهٔ ram است. ریشهٔ ram «استراحت کردن» معنی می‌دهد. از ریشهٔ ram «آرمیدن» و «رامیدن» هم آمده‌اند.\\\" Exactly the chart's ā-rām and rāmīdan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.vv. rām, rām(ag), rāmēnīdan, rāmišn (PHD_mackenzie.txt ll.4326-4329)\", \"stance\": \"supports\", \"note\": \"\\\"rām [l'm | M r'm, N -] peace; cal. 21st day\\\"; \\\"rām(ag) [lm(h) | P rm, N rām(a)] herd, flock\\\"; \\\"rāmēnīdan ... give peace, pleasure\\\"; \\\"rāmišn [l'mšn' | M r'mšn, N rāmiš] peace, ease, pleasure\\\" — the Middle Persian stage of all Nourai's Persian words except xorram/pedrām.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 12 (p.5) and no. 604 (pp.134-135)\", \"stance\": \"supports\", \"note\": \"no.12 ārām; no.604 \\\"rām 'Ruhe; fröhlich, heiter' ... aw. rāman- 'Ruhe'; phlv. hu|rām, rām(i)šn, rāmēnītan\\\" — Horn himself pairs rām with hu-rām, i.e. with xorram.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.55, note 479\", \"stance\": \"supports\", \"note\": \"Derives xurram from iran. *hu-rama- 'sich wohl freuend' (after Fr. Müller), rejecting the older equation with Skt. su-śarman-.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʿin, vol. 2, leaves 195, 391, 422\", \"stance\": \"supports\", \"note\": \"Moʿin's etymological footnotes: xurram < Pahlavi xurram; rāmiš < Pahlavi rāmišn; rama < Pahlavi ramak.\"},\n      {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi s.v. پدرام (MON_part1.txt ll.21597, 29645)\", \"stance\": \"supports\", \"note\": \"\\\"پدرام (ص.) خوش\\\" and \\\"پدرام (ص. مر.) آراسته، نیکو\\\" — Nourai's gloss 'pleasant / well arranged' is Moʿin's.\"},\n      {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors (FRS_pages.txt ll.14322-14324)\", \"stance\": \"supports\", \"note\": \"\\\"پدرام جایی بود خرم و دلگشای ... جایی که خرّم بود آن را پدرام خوانند\\\" — the oldest Persian lexicographical gloss, and it explicitly equates pedrām with xorram.\"},\n      {\"src\": \"FFD\", \"where\": \"Abolqāsemi p.25 s.v. آرامیدن/آرمیدن\", \"stance\": \"supports\", \"note\": \"\\\"از ریشهٔ ram «آرمیدن» و «رامیدن» هم آمده‌اند\\\"; ā- analysed as a verbal preverb.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Riše-hā (ARY_latin_index_pages.txt ll.1425-1427)\", \"stance\": \"supports\", \"note\": \"The Latin index groups \\\"RAMTIS, RIMTI, RAMDITI (LITHUANIAN) | ARAMITAN, PAHLAVI | RAMISHN, RAM, RAMENITAN | RAMS (LATVIAN) | RAM (TOKHARIAN A)\\\" under one Persian headword — the same comparative set.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Old Persian\",\n     \"words\": \"ram\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Kent's Old Persian lexicon does list the root, but only as a bound element: \\\"ram- vb. 'be at peace', with prefix ā, in Ariyāramna-, q.v.\\\" (KNT.txt l.5859). The cross-referenced entry reads: \\\"Ariyāramna- sb. 'Ariaramnes', great-grandfather of Darius: Elam. har-ri-ia-ra-um-na, Akk. ar-ia-ra-am-na-', Gk. Ἀριαράμνης. From ariya- + pass. ptc. of ā-ram- (§131; Av. Skt. ram- 'to be at peace, to pacify'): 'Having the Aryans at peace'.\\\" So OP ram- is real, means exactly 'be at peace', and is an inherited *h₁rem- verb beside Av. ram-/rāmaiieiti and Skt. rámate; the only nuance is that it is attested solely inside the royal name Ariyāramna- (and in the participle ā-ramna-), never as a free verb form in the inscriptions. Horn no. 604 also cites the name (\\\"ap. vergl. Ariya|ramna-, Ἀριαράμνης\\\") as the Old Persian witness for NP rām.\",\n     \"derivation_fa\": \"کنت در واژه‌نامهٔ پارسی باستان ستاک را می‌آورد اما تنها به‌صورت جزءِ بسته: «ram- (فعل) «در آرامش بودن»، با پیشوند ā، در Ariyāramna-». ذیل همان نام می‌نویسد: «Ariyāramna- «آریارمنه»، جدّ داریوش؛ از ariya- + اسم مفعولِ ā-ram- (اوستایی و سنسکریت ram- «آرام بودن، آرام کردن»): «آن‌که آریاییان را در آرامش دارد»». پس ram- پارسی باستان واقعی است و معنیِ داده‌شده در نمودار درست؛ تنها نکته آنکه این ستاک در کتیبه‌ها جز در همین نام شاهی گواهی نشده است. هرن نیز (بند ۶۰۴) همین نام را گواهِ پارسی‌باستانِ «رام» فارسی می‌گیرد.\",\n     \"sources\": [W_H1REM],\n     \"ref_check\": [\n      {\"ref\": \"KNT:206\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon (KNT.txt l.5859; scan leaf 230, lexicon offset leaf = printed + ~15, so printed p. ≈206-215 — the 'r-' stretch of the Lexicon, which begins at p.164): \\\"ram- vb. 'be at peace', with prefix ā, in Ariyāramna-, q.v.\\\"; and at Ariyāramna- (l.5053): \\\"From ariya- + pass. ptc. of ā-ram- (§131; Av. Skt. ram- 'to be at peace, to pacify'): 'Having the Aryans at peace'.\\\" Nourai's gloss is Kent's, word for word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.vv. ram-, Ariyāramna-\", \"stance\": \"supports\", \"note\": \"As quoted; Kent also rejects the alternative analyses (Foy 'Ariyā pl. + ramna-', Herzfeld 'Ariya- + aramna- to ar-').\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. rāman- (col. 1523-24) and the verb ram- (col. 1511, per Nyberg's citation)\", \"stance\": \"supports\", \"note\": \"Bartholomae lemmatises Avestan ram- 'to repose' and rāman- 'peace' — the Avestan half of Kent's \\\"Av. Skt. ram-\\\".\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no. 604, p.134\", \"stance\": \"supports\", \"note\": \"\\\"ap. vergl. Ariya|ramna-, Ἀριαράμνης\\\" — Horn uses the same Old Persian evidence.\"},\n      {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon (TLM.txt)\", \"stance\": \"silent\", \"note\": \"Tolman lemmatises the name Ariyāramna- but has no separate root entry ram-.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": null,\n     \"words\": \"\",\n     \"verdict\": \"unverified\",\n     \"derivation\": \"There is nothing to verify: the box drawn to the right of the Old Persian 'ram' box is completely empty on the printed page — an outlined rectangle with no language header, no word, no gloss and no reference (checked on the page image, copied to data/verification/sources/refs/ocr/BOOK/420.png). The extraction is faithful; this is a layout artefact of Nourai's chart (he draws a target box for the Old Persian branch and leaves it blank). Most probably the intended descendant was the Middle/New Persian rām already given in the Avestan branch, or the royal name Ariyāramna- he decided not to print. No claim is made, so no claim can be checked.\",\n     \"derivation_fa\": \"چیزی برای بررسی وجود ندارد: جعبه‌ای که در سمت راستِ جعبهٔ «ram» پارسی باستان کشیده شده در صفحهٔ چاپی کاملاً خالی است — کادری بی‌نامِ زبان، بی‌واژه، بی‌معنی و بی‌ارجاع (بر روی تصویر صفحه بررسی شد). پس خوانشِ اسکن درست عمل کرده و این نقصی در صفحه‌آراییِ خودِ کتاب است؛ احتمالاً نورایی می‌خواسته دنبالهٔ فارسی میانه/نوِ شاخهٔ پارسی باستان (یا نامِ آریارمنه) را بیاورد و آن را ناتمام گذاشته است. چون ادعایی مطرح نشده، نه می‌توان آن را تأیید کرد نه رد.\",\n     \"sources\": [],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book.\"}],\n     \"consulted\": [{\"src\": \"BOOK\", \"where\": \"printed pdf page 420, image copied to data/verification/sources/refs/ocr/BOOK/420.png\", \"stance\": \"silent\", \"note\": \"The box is blank on the page itself — the JSON's note ('box is printed entirely blank in the source') is accurate.\"}]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Old High German\",\n     \"words\": \"rasta\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"OHG rasta is a real word, but the chart mis-states both its part of speech and its ancestry. (a) It is a feminine NOUN, not a verb: OHG rasta 'rest, repose', also 'a league of miles' (MHG raste, rast, NHG Rast), beside the verb OHG restēn 'to rest'; Klein groups it with Goth. rasta 'mile', ON rǫst 'league, distance after which one rests', OS resta 'resting place'. (b) The root: Germanic *rastō does NOT belong to *h₁rem-. Klein (p.1335, Nourai's own reference) derives the Teutonic base *ras- 'to rest, remain, dwell' \\\"fr. I.-E. base *erǝ-, *rē, 'to rest'\\\" — Pokorny p.338 f., a different entry from rem- (p.864); and Pokorny himself writes at the head of rem- that the connection with erǝ-/rē- \\\"ist fraglich\\\". Wiktionary derives Proto-West Germanic *rastu from Proto-Germanic *rastō with no PIE etymon given, and Etymonline calls PGmc *rasto- \\\"a word of uncertain origin\\\", noting the original sense may have been a measure of distance ('league') rather than 'repose'. The only support for Nourai's grouping is older comparative work: Skeat (s.v. Rest (1)) allies AS. rest to \\\"Skt. ra-ti, pleasure, Gk. ἐρωή, rest (√RA)\\\", and Skt. rāti-/rati- IS a rem- derivative in Pokorny p.864. So the chart follows a 19th-century view that modern scholarship does not accept.\",\n     \"derivation_fa\": \"rasta آلمانیِ علیای باستان واژه‌ای واقعی است، اما نمودار هم مقولهٔ دستوری و هم تبارِ آن را نادرست می‌دهد. نخست، rasta اسم مؤنث است («آسایش» و نیز «فرسنگ/مرحلهٔ راه»)، نه فعل «آرمیدن»؛ فعل آن restēn است. دوم و مهم‌تر، *rastō ژرمنی به ریشهٔ *h₁rem- تعلق ندارد: کلاین در همان صفحه‌ای که نورایی ارجاع می‌دهد (۱۳۳۵) ستاکِ ژرمنیِ *ras- را از ریشهٔ هندواروپاییِ *erǝ-/*rē- «آرمیدن» می‌گیرد که مدخلی جداگانه در پوکورنی (ص ۳۳۸ به بعد) است؛ و خودِ پوکورنی در آغازِ مدخل rem- می‌نویسد پیوند این دو «مشکوک» است. ویکی‌واژه و اتیمآنلاین نیز خاستگاه *rastō را «نامعلوم» می‌خوانند و احتمال می‌دهند معنیِ آغازینش «مسافت میان دو منزل» بوده باشد. تنها پشتوانهٔ نورایی دیدگاه کهنِ اسکیت است که rest را با rati- سنسکریت می‌سنجد. پژوهش امروزی این شاخه را از ریشهٔ Rem جدا می‌کند.\",\n     \"sources\": [E_REST, W_REST, W_RASTU],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1335\", \"status\": \"contradicts\", \"note\": \"Klein s.v. rest, n. (KLN_1966.txt ll.32546-32547, leaf 710 ≈ printed pp.1334-1335): \\\"ME. reste, fr. OE. rest, ræst, 'rest, resting-place; bed, grave', rel. to OS. rasta, 'resting-place, grave', ON. rǫst, 'distance, journey, mile', Goth. rasta, 'mile', OHG. rasta, MHG. raste, rast, G. Rast, 'rest, peace', fr. Teut. base *ras-, 'to rest, remain, dwell', ... fr. I.-E. base *erǝ-, *rē, 'to rest', whence also ... Avestic airime, 'quietly', Gk. ἐρωή, 'rest'.\\\" The cited reference does have OHG rasta, but assigns it to *erǝ-/*rē (Pokorny 338), not to rem- (Pokorny 864) — so it contradicts the arrow as drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.864 (head of rem-) and pp.338 f. (erǝ-, rē-)\", \"stance\": \"contradicts\", \"note\": \"\\\"Beziehung zu erǝ-, rē- ,ruhen' (S. 338 f.) ist fraglich\\\" — and Pokorny lists no Germanic *rast- under rem- at all; his Germanic material there is rama, rant, rimis, rim.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. rest, n., p.≈1335\", \"stance\": \"contradicts\", \"note\": \"As quoted: Teut. *ras- < I.-E. *erǝ-, *rē.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. 'Rest (1), repose' (SKT.txt l.15989; leaf 424, printed ≈ p.404)\", \"stance\": \"partial\", \"note\": \"\\\"Rest (1), repose. (E.) A.S. rest, ræst, rest. + Du. rust, Dan. Swed. rast, Icel. röst (the distance between two resting-places), Goth. rasta (a stage), O.H.G. resta, rest. Allied to Skt. ra-ti, pleasure, Gk. ἐρωή, rest. (√RA.)\\\" — Skeat's Skt. rati- is a rem- word in Pokorny, so the older literature did make Nourai's connection; but Skeat's √RA is really Pokorny's erǝ-/rē-.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II pp.371-372 (rem-)\", \"stance\": \"silent\", \"note\": \"The rem- entry contains no Germanic *rast- material.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster (WEB_vol1.txt), grep 'rasta'\", \"stance\": \"silent\", \"note\": \"Nothing usable in the local OCR.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"rest\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"English rest (n.1 / v.1) is genuine and means what the chart implies, but it does not descend from Old High German rasta: it continues Old English ræst, rest 'rest; bed; intermission of labour; mental peace' (verb ræstan, restan), from Proto-West Germanic *rastu, Proto-Germanic *rastō — of which OHG rasta is the sister form, not the source (Etymonline: \\\"from Proto-Germanic *rasto- (source also of Old Saxon resta ..., Dutch rust, Old High German rasta, German Rast 'rest, peace, repose')\\\"). No borrowing from German into English is involved at any date; the arrow is Nourai's usual shorthand of letting the oldest attested Germanic form stand for the branch. ME reste > NE rest; the originally distinct rest (n.2) 'remainder' (< OF reste < L. restāre) was later confused with it. The ultimate root, as at node #5, is not *h₁rem-: PGmc *rastō is of disputed origin, usually attached to PIE *h₁res-/*erǝ- 'to rest'.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی rest واقعی است، اما از rasta آلمانیِ علیای باستان نمی‌آید: دنبالهٔ انگلیسی باستانِ ræst/rest «آسایش؛ بستر؛ آرامش خاطر» (فعل ræstan/restan) است، از ژرمنی باستان *rastō، که rasta آلمانی هم‌ریشه (خواهرِ) آن است نه سرچشمه‌اش؛ اتیمآنلاین همین را می‌گوید. هیچ وام‌گیری‌ای از آلمانی به انگلیسی در کار نیست و پیکانِ نمودار همان شیوهٔ همیشگیِ نورایی است که کهن‌ترین صورتِ گواهی‌شدهٔ ژرمنی را نمایندهٔ کلِ شاخه می‌گیرد. ریشهٔ نهایی نیز — چنان‌که در گرهٔ ۵ گفته شد — *h₁rem- نیست؛ *rastō ژرمنی را معمولاً به *h₁res-/*erǝ- «آرمیدن» می‌بندند و خاستگاهش را نامطمئن می‌دانند.\",\n     \"sources\": [E_REST, W_REST, W_RASTU],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The English box carries no reference in the book; its parent box cites KLN:1335, checked at node #5.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. rest, n., p.≈1335\", \"stance\": \"partial\", \"note\": \"\\\"ME. reste, fr. OE. rest, ræst ... rel. to OS. rasta ... OHG. rasta\\\" — 'rel. to', i.e. cognate, not 'fr.'; Klein's own wording excludes descent from OHG.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Rest (1), p.≈404\", \"stance\": \"partial\", \"note\": \"\\\"A.S. rest, ræst, rest. + Du. rust ... O.H.G. resta\\\" — the '+' is Skeat's cognate marker, again not descent.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls Standard Dictionary (FSD_vol1-4.txt), grep 'rasta'\", \"stance\": \"silent\", \"note\": \"The OCR of the Standard Dictionary yields no usable 'rest' etymology (hits are noise such as 'contrasta', 'parastas').\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-420.json\"\nwith open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/gen-420.py\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-420.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 420",
 "description": "Write and validate page-420.json"
}
```


### [2026-09-14T01:44:29.608Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-420.json
JSON OK
nodes verified: 9/9
node verdicts: {'transcription_suspect': 1, 'plausible': 3, 'confirmed': 3, 'unverified': 1, 'disputed': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'partial': 3, 'supports': 11, 'not_checked': 6, 'contradicts': 1}
books consulted: {'partial': 7, 'contradicts': 3, 'silent': 9, 'supports': 18} | by book: {'HRN': 5, 'PHD': 3, 'HUB': 3, 'POK': 2, 'WLD': 2, 'NYB': 2, 'BRT': 2, 'KLN': 2, 'SKT': 2, 'IEC': 1, 'SYN': 1, 'CHEUNG': 1, 'SOD': 1, 'BQT': 1, 'MON': 1, 'FRS': 1, 'FFD': 1, 'ARY': 1, 'KNT': 1, 'TLM': 1, 'BOOK': 1, 'WEB': 1, 'FSD': 1}
```


## [2026-09-14T01:44:45.759Z] AGENT

Done — `data/verification/page-420.json` written, valid JSON, `verify_check.py 420` reports 9/9 nodes and **0 PROBLEM lines**.

**Page 420 (book p. 390) — 2 non-redirect entries, 9 nodes**
- Root verdicts: plausible 1 (Rek/Reg 2), confirmed 1 (Rem)
- Node verdicts: confirmed 3, plausible 3, disputed 1, transcription_suspect 1, unverified 1
- Ref checks: supports 11, partial 3, contradicts 1, not_checked 6 (AEF ×2, FAF, MON, and the two boxes with no refs)

**transcription_suspect**
- Rek/Reg 2, node #1 Sanskrit `račana`: the book really prints *račana* (page image checked → `error_in: book`). Skt. *racanā* means 'arranging', from Pokorny's neighbouring root "2. rek- ,anordnen'" on the same p.863; the intended form is *rašana* (raśana n., by-form of raśanā́ 'rope'), c/š confusion under the háček.

**disputed**
- Rem, node #5 OHG `rasta`: Germanic *rastō does not belong to *h₁rem-. Klein p.1335 — Nourai's own citation — puts it under IE *erǝ-/*rē- (Pokorny 338), and Pokorny p.864 himself calls that link "fraglich"; Etymonline: "of uncertain origin". Also *rasta* is a noun, not the verb 'to rest'.

**Other notable findings (no owner action needed)**
- The chart's own NOTE is resolved in Nourai's favour: Horn 137 ("arab. hebr. LW. rasan") and Asbaghi make Arabic رسن a loan from MP *rasan*; MON/AFM's equation with ریسمان fails (Horn 617: rīsmān < *raiś- 'to spin').
- Page-number drift found, not extraction errors: Asbaghi's *rasan* is on p.136 (Nourai cites PLA:138); BQT:960 falls between the رام (≈p.931) and رمه (≈p.962) entries.
- `hu-rama` / `paiti-râman` are labelled Avestan but are Old Iranian reconstructions (Pahlavi *hu-rām* per Horn 604; Sogdian *ptrʾm* < \*pati-rāma per Gharib 7813) — hence "plausible".

**Extraction errors for the owner: none.** Node #4 really is a blank box on the printed page; the JSON note is accurate.

Saved for audit: `sources/refs/ocr/BOOK/420.png`, `sources/refs/ocr/AFM/72.vision.txt`; 10 web pages archived via `fetch_source.py`.
