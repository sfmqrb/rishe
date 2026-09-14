# Verification process log — verify-page-424


## [2026-09-14T01:21:38.605Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 424 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-424.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-424.json. Write /home/sfmqrb/git/rishe/data/verification/page-424.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 424` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:39.711Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-14T01:21:40.612Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:40.631Z] TOOL RESULT

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


## [2026-09-14T01:21:41.011Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-424.txt"
}
```


### [2026-09-14T01:21:41.033Z] TOOL RESULT

```
1	=== PDF page 424 (book page 394) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Reudh 1 : red  (refs POK:872)
4	#1 (parent #0) [Avestan] refs=POK:872 | raoidita : red
5	  #2 (parent #1) [Pahlavi] refs=MON:1695 | rôdîk, rôy : zinc
6	    #3 (parent #2) [Persian] refs=BQT:980,981; HRN:141; MON:1696 | rŭy 2 «روی ۲ ( رویگر ، رویین ، رویینه )» : zinc ; ronâs «روناس ( رویناس ، روینگ )» : a plant used for dying
7	#4 (parent #0) [Latin] refs=AHD | rôbeus : red
8	  #5 (parent #4) [French] refs=AHD | 
9	    #6 (parent #5) [Persian] refs=MON | rŭž «روژ» : red, lipstick
10	    #7 (parent #5) [English] refs=None | rouge, ruby
11	#8 (parent #0) [Germanic] refs=AHD | 
12	  #9 (parent #8) [English] refs=None | red, rust
13	--- entry 1 ---
14	ROOT Reudh 2 -> redirect to Reu 2
15	--- entry 2 ---
16	ROOT [Indo-European] Reug : to vomit, belch, produce smoke or vapor  (refs POK:871)
17	#1 (parent #0) [Persian] refs=POK:871; MON:44 | roğ «رُغ ( روغ )» : belch ; âroğ «آرغ ، آروغ ، آروق» : belch
18	#2 (parent #0) [Germanic] refs=AHD | riukan : to produce vapor, smell, stink
19	  #3 (parent #2) [English] refs=None | reek
20	--- entry 3 ---
21	ROOT [Indo-European] Reughmen : oil, cream  (refs POK:837)
22	#1 (parent #0) [Avestan] refs=POK:837; KLN:1307 | raoğna : oil
23	  #2 (parent #1) [Pahlavi] refs=BQT:978 | rôğn : oil ; rôvn : oil
24	    #3 (parent #2) [Persian] refs=BQT:978 | roğan «روغن» : oil
25	#4 (parent #0) [Sogdian] refs=SOD:345 | rwğn : fat, oil
26	#5 (parent #0) [Germanic] refs=KLN:1307; AHD | raugna : cream, oil
27	  #6 (parent #5) [English] refs=AHD; KLN:1307 | ream 1 : cream ; ramekin
28	--- entry 4 ---
29	ROOT Reup -> redirect to Reu 2
30	
```


## [2026-09-14T01:21:43.513Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-424.json && echo \"=====MATRIX=====\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-14T01:21:43.578Z] TOOL RESULT

```
{
  "pdf_page": 424,
  "book_page": 394,
  "entries": [
    {
      "root": {
        "name": "Reudh 1",
        "lang": "Indo-European",
        "refs": "POK:872",
        "gloss": "red"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:872",
          "words": [
            {"translit": "raoidita", "gloss": "red", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:1695",
          "words": [
            {"translit": "rôdîk, rôy", "gloss": "zinc", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:980,981; HRN:141; MON:1696",
          "words": [
            {"translit": "rŭy 2", "gloss": "zinc", "script": "روی ۲ ( رویگر ، رویین ، رویینه )"},
            {"translit": "ronâs", "gloss": "a plant used for dying", "script": "روناس ( رویناس ، روینگ )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "rôbeus", "gloss": "red", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "rŭž", "gloss": "red, lipstick", "script": "روژ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "rouge, ruby", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "red, rust", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Reudh 2",
        "redirect": "Reu 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Reug",
        "lang": "Indo-European",
        "refs": "POK:871",
        "gloss": "to vomit, belch, produce smoke or vapor"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:871; MON:44",
          "words": [
            {"translit": "roğ", "gloss": "belch", "script": "رُغ ( روغ )"},
            {"translit": "âroğ", "gloss": "belch", "script": "آرغ ، آروغ ، آروق"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "riukan", "gloss": "to produce vapor, smell, stink", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "reek", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Reughmen",
        "lang": "Indo-European",
        "refs": "POK:837",
        "gloss": "oil, cream"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:837; KLN:1307",
          "words": [
            {"translit": "raoğna", "gloss": "oil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:978",
          "words": [
            {"translit": "rôğn", "gloss": "oil", "script": null},
            {"translit": "rôvn", "gloss": "oil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:978",
          "words": [
            {"translit": "roğan", "gloss": "oil", "script": "روغن"}
          ],
          "note": null,
          "quote": {
            "text": "گر ببینم خانه ات را من دوام - روغن و شیرت بیارم صبح و شام",
            "poet": "Molavî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:345",
          "words": [
            {"translit": "rwğn", "gloss": "fat, oil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:1307; AHD",
          "words": [
            {"translit": "raugna", "gloss": "cream, oil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD; KLN:1307",
          "words": [
            {"translit": "ream 1", "gloss": "cream", "script": null},
            {"translit": "ramekin", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Reup",
        "redirect": "Reu 2"
      },
      "nodes": []
    }
  ]
}
=====MATRIX=====
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


## [2026-09-14T01:21:48.027Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','MON','BQT','HRN','SOD','WLD','HUB','PHD','NYB','BRT','IEC','SYN','SKT','LEW','LAT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-14T01:21:49.166Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
```


## [2026-09-14T01:21:53.967Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 837 871 872; do echo \"=== POK p.$p (leaf $((p-344))) ===\"; awk -v n=$((p-344)) 'BEGIN{RS=\"\\f\"} NR==n' POK_02.txt | head -80; done"
}
```


### [2026-09-14T01:21:55.004Z] TOOL RESULT

```
=== POK p.837 (leaf 493) ===
=== POK p.871 (leaf 527) ===
=== POK p.872 (leaf 528) ===
```


## [2026-09-14T01:21:57.684Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la POK_*.txt && for f in POK_01 POK_02 POK_03 POK_full; do echo \"$f: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f.txt) leaves\"; done"
}
```


### [2026-09-14T01:21:58.797Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
POK_01: 363 leaves
POK_02: 433 leaves
POK_03: 429 leaves
POK_full: 1 leaves
```


## [2026-09-14T01:22:01.832Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\""
}
```


### [2026-09-14T01:22:03.002Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
```


## [2026-09-14T01:22:05.349Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: reudh\\|lemma: reug\\|lemma: reug'-men\\|lemma: reu\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:22:05.408Z] TOOL RESULT

```
70434:Root / lemma: reu-b-ax\6 reu-g- 
70479:Root / lemma: reuA^-{*uereuA'^^ (zero grade of *hieleuRh-) 
70485:Root/ lemma: reu6!^-\ "red' derived from a zero grade of Root/ lemma: el-1, ol-, J-\ "red, 
70576:Root / lemma: reugh-m(e)n- 
70592:Root/ lemma: reu-1, reu- ru- 
70664:Root / lemma: reu-2, reus- : ru- 
70856:Root / lemma: reu-3, reu-s- 
70866:Root / lemma: reu-4 
70871:Root / lemma: reu-smen- 
70888:Root / lemma: reus- 
70898:Root / lemma: reuto-, routo- rut- 
70914:Root / lemma: reua- : ru-
```


## [2026-09-14T01:22:07.324Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '70430,70600p' POK_full.txt"
}
```


### [2026-09-14T01:22:07.391Z] TOOL RESULT

```
References: WP. II 368, WH. II 443 f., Trautmann 238. 
Page(s): 866 

Root / lemma: reu-b-ax\6 reu-g- 

Meaning: to vomit, retch 

Material: 1. /■ea&-;Old Icelandic rjupai. "Schneehuhn", Norwegian rjupa, /ype (compare 

Latvian /'i/i6'e/7/s'Birkhuhn'?); ablaut. Old Icelandic AO/Oa 'aufstoften', /yp/a'sich erbrechen', 

Old High German roffezzen^auisio^evi {*rupatjan). Middle High German rofzen. Modern 

High German reshaped to rulzen, rulpsen. 

2. reug-:H^ers. a-roy^dias Rulpsen'; Armenian o/ra/77'erbreche myself, burp' (from 
*orucam, o-\s suggestion vowel); gr. spsuYOMai 'speie from, erbreche myself, spuyyavcjo ' 
burp', spuyn "Aufstoften'; Latin erugo, -e/ie'ausrijlpsen', ructo, -a/ie "rulpsen, ausspeien'; 
Old English /"oce/Za/? "rulpsen', eo''/'c»c"das Wiederkauen', Old High German it-ruchen. 
Middle High German /fe/i/c/re/? "ruminate', iterochei. "gullet from ruminants', v\\s\. Jortru. 
"das Wiederkauen' (about ^urtrirom * id-ruhtr-)\ Old Icelandic yo/Y/'a"wiederkauen'; 

Lithuanian rjaugmi{riaugeju), raugiu, rugiu^ burp, have saures Aufstoften', Old Church 
Slavic rygajQ SQ^ burp', Lithuanian rugstu, rugti^ sour become, ferment, seethe', isrugos 
"wheys', /•Jgys"sauertopfischer person', rugztas ' sour' , A^i/^as "sourdough', Latvian 
atraugast PI. "Aufstoften', atraugt/es ^ auistoQ>en' , raudzet 'sauern', m/r/s "bitter, herb', Old 
Prussian ructan dadan "sour milk', raugus^reuuei'; 

as "re^-s/T?©/? "Wiederkauen; gullet ' (see 873) auf the Lautgebarde *reu-be\v\g based 
on; 

under a Mittelbed. " burst out, break out ', or "exhalare' reiht man (yet very doubtful) an: 
Old Icelandic //iy/ra "smoke, whisk, hurry'. Old English reocan^ smoke, steam, stink'. Middle 
Low German reken, /77/re/7 "smell'. Old High German rouhhan^ smoke, steam, smell'. Old 
High German rouh. Old Saxon rok. Old English rec. Old Icelandic reykrm. "smoke'. Middle 
High German ruch. Middle Low German rokevn. "smell, odor', isl. Norwegian roku. 
"Scatter, sprinkle, drive, impel, drift, propel, push, thrust, storm'; 

Maybe Rumanian ror cloud ' 



if alb. /"e "cloud' from */'c»^^/- originated is, as Modern High German Rauch, is ein 
previously proto Indo Germanic Ve^^- "cloud, smoke' voraussetzbar. 

References: WP. II 357, Wissmann Nom. Postverb. 128 f., Trautmann 244. 
Page(s): 871-872 

Root / lemma: reuA^-{*uereuA'^^ (zero grade of *hieleuRh-) 

Meaning: red 

Note: 

Root/ lemma: reu6!^-\ "red' derived from a zero grade of Root/ lemma: el-1, ol-, J-\ "red, 

brown (in names of trees and animals)' extended in formant Rh-\ 

Material: 

in e- grade: 

gr. £p£u9u) " to make red, stain red. Pass, to be or become red' (= Old Icelandic rjoda), 
epeuGoq n. " redness, flush; of dye' (compare Latin rubor); spuGpoq "red' (= Latin ruber. Old 
Church Slavic *rbdrb etc.); spuolpn " rust, in corn; title of Demeter in Lydia, mildew, 
metallic oxide, rust ' (ambiguous ending), zpuoi-TTzkaq "German measles. Rubella' 
(*£puaai-, *ru6^-s-); 

In zero grade: 

Old Indie r6hita- = Avestan raoi5ita-^re6, reddish', rohft- "rote mare, Weibchen a gazelle ', 
rohi- m., rohTi. " gazelle '; Old Indie /d/?^- "reddish', m. n. "reddish metal, copper, iron' 
(formal = Latin rOfus, Old Irish ruad, Gothic raut^s, Lithuanian raudas. Old Church Slavic 
rudii), rodhra-, lodhra-m. "symplocosracemosa, ein tree, from dessen Rinde ein rotes 
Pulver bereitet wird', /osta-n. " iron rust ' ( *reu6'^-s-fo-); ru6'^/ra-'re6, bloody', n. "blood' 
{*ru6'^-f-ro-, contaminated from *ru6'^-ro- and *ru6'^-/-); khotansak. rrusta-'red' {*reu6^-s-fo- 

); 

Maybe alb. (nde-rusk) ndryshk^ rust ' [Albanian prefix dz(a)-, de-, z-is of Macedonian 
Slavic origin (as in Mac. *dz-astra, dzastra " the day after tomorrow, tomorrow'), from 
Slavic za" behind; for, after, because of, during, at, in, on' see Root /lemma: gh6\ behind, 
towards]. 

Latin rubidus^ oxblood, indigo ' (with -o'o- further formations = Old Indie loha-); 

with dial. f. rufus^ light-red, rufous, reddish', Umbrian rofu^ red '; 

Maybe alb. rruva, rrufa^y\v\e without grapes' : rrufane, rrefane, /reT^/?^^/ (diminutive) 
"handle (*twig?)' Latin loaword. 



with dial, ofrom *ou Latin robus, robeus, rdb/us\ed', robrgo^Hosi; mildew, smut, blight ', 
also probably robus, robur' Hart\r\o\z, heartwood '; ruber, rubra, -um'red' (Umbrian rufru^ 
rubros '), Latin rubor' redness ', rubed, -ere'be red' (: Old High German roten, Old Church 
Slavic rbdeti), russus ' fleischrot ' ( *ru&^-so-)\ auf *ruA^ro-QO back to auson. loanword 
Ai/Z/Zi/s 'reddish', VN Rutuli {\n\Vc\ Dissim.); compare Ligurian fundus Roudelius, lllyrian 
CampT Raudii, apul. PN /?^o'/5e (Szemerenyi Arch. Ling. 4, 112 f.); about Latin raudussee 
below; 

Old Irish ruad, cymr. etc. rbudd're6', Old Irish ruccfaje' shame' {*rud-kja), nasal, fo- 
/'O//70'' blushes, turns red'; gall. PN Roudus, Ande-roudus, GN Rudiobos( red Schlager '?), 
Rudianos, Celtic roudo-'reA' and 'strong'; 

Old Icelandic rjddr. Old English reod'xeA', Old Icelandic rjoda' make bloody ', Old 
English reodan're6 paint ', Gothic (about ' shamefaced blush') ga-riut^s' respectable ', 
P'a-/7^ofe/"Schamhaftigkeit'; ablaut, raut^s. Old Icelandic raudr. Old English read. Old High 
German /io/'red'. Old Icelandic raudim. "rotes Eisenerz', rodrai. "blood', rodim. " redness 
', /ydn. and rydrvn. "Rosf, roda' be or become red ', Old High German /lo/e/? "blush'. 
Middle High German /'o/"red'. Old High German rotamo, rosamo {*ru&^-s-men-) " redness ' 
(moreover Old Icelandic /'c»s/77i/-^ip//"rotliche Berge'), Old English rudu' redness ', rudig 
"reddish'; a-ryderian' b\us\\'\ Old English rust. Old High German Old Saxon /'os/"Rost' 
[*ru6'^-s-to); 

Lithuanian raudas, raudonas'xQ^ , rauda'rote paint, color'; rudas' puce ' (Latvian ruds 
"reddish'), mo'^o "autumn', rudet/ 'rosten', rudisi. "Rosf, rudynas, rudyna, rudyne 's\Namp, 
marsh with rotlichem, eisenhaltigem water, morass, puddle, slop', rausvas {*rou6^-s-uo-) 
"reddish', Latvian rusa {*ru6^-s-a) "Rosf, Lithuanian rusvas' reddish brown ' {*ru&^-s-uo-), 
ms//s "Bratrosf, mse//" gleam, burn', Latvian rusla'V\v\6 of rotbrauner paint, color', 
Lithuanian rustas' brownish, purple, mauve' {*ru6^-s-to-), Latvian A^5/a"braune paint, 
color', rustet' red paint '; 

Old Church Slavic rudh 'red', ruda'ore, metal ', rusb{*roud'^-s-o-) "reddish, blond'; 
*rbdrb "red' in r. -Church Slavic rodrb; rbdeti s^' turn red ', rbzda' RosX , russ. rysyj 
"reddish blond' {*rij^^-s-o-, compare Latvian rusa); 

Tocharian A ratr-arkyant' xo\%\ara.e'(\d\ rtar, B ratre'xed' {*rutre-7). 

Old Indie rav/-m. "sun', Armenian arevds. kann only very doubtful as "the Rote' 
gedeutet become; Latin raudus, rodus, rudus'e\n formloses ErzstiJck as coin' is perhaps 



with Old Indie loha- "rotes metal, copper, iron' and Old Icelandic raudrroies Eisenerz', Old 
Church Slavic ruda'ore, metal ' to connect and gall, or lllyrian loanword; 

also Old High German aruzzi, erizzi, aruz. Old Saxon arut' ore, Erzstiick', Old Icelandic 
ortog ( *arutia-taugo) 'Drittel eines ore' are because of Schwankens the forms as borrowed 
to betrachten; hence besteht Hommels derivation from sum. urud^ copper' letztlich to right, 
different Kretschmer Gl. 32, 6 ff. 

References: WP. II 358 f., WH. II 420 f., 444 f., 455, 456, Trautmann 239. 
Page(s): 872-873 

Root / lemma: reugh-m(e)n- 

Meaning: cream 

Material: Avestan raoyna-^ butter'. Middle Persian npers. /'(9ya/7"(ausgelassene) butter'; 

Old Icelandic rjumirw. " skimmings', changing through ablaut Old English ream. Middle 

Low German rome. Old High German /"Oi//?? "cream', and Middle Low German rame {for 

*rdme), from which Modern High German Rahm, with J Swiss rum 6s. 

References: WP. II 357 f.; s. also above S. 868. 

Page(s): 873 

Root/ lemma: reu-1, reu- ru- 

Meaning: to roar, murmur, etc.. (expr.), onomatopoeic words 

Material: Old Indie rau-ti, ruvati, /'51/5// "bellow, roar, larmt, drohnt', rava-, ravatha- rr\. " 

bellowing, braying, roar '; gr. u)puo|jai "heule, bellow, stofte einen scream from', cbpuSov 

Adv. "with bellowing, braying, roar' (prefix Indo Germanic o); Latin /x7/77c»/'"noise, shout,
```


## [2026-09-14T01:22:16.866Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"reugh-m\\|reug-m\\|raoγna\\|raoyna\\|raoghna\" POK_03.txt | head -20; echo \"---leaf 107-112---\"; for n in 105 106 107 108 109 110 111 112; do echo \"## leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_03.txt | head -5; done"
}
```


### [2026-09-14T01:22:18.516Z] TOOL RESULT

```
1347:vermutlich  as.  ahd.  riomo  ,Riemen,  ledernes  Band,  Gürtel'  (*,abge- rissener  Hautstreifen'),  ags.  reoma,  reama  ds.,  auch  ,dünne  Haut'  (vgl. S.  873  *reugh-m(e)n-  ,Rahm');  mnd.  mndl.  rOw,  rüne,  schwäb.  raun  ,Wallach, Gaul',  wegen  ofries.  han-räne  , Hahnrei'  (eigentlich  »verschnittener  Hahn') ursprüngl.  ,equus  castratus',  mnl.  runen,  ruynen  'schneiden,  kastrieren*; (nhd.  runken);  entlehnt  lett.  rünlt  ,kastrieren',  ebenso  finn.  ruuna  , Wallach*, ruunata  , kastrieren*;
1403:Av.  raoyna-  ,Butter',  mpers.  npers.  röyan  , (ausgelassene)  Butter';  aisl. rjümi  m.  ,Rahm',  ablautend  ags.  7'eamj  mnd.  rövie,  ahd.  roum  , Sahne', und  mnd.  räme  (für  *röme)j  woraus  nhd.   Rahm^   mit  ü  Schweiz,   rüm    ds.
---leaf 107-112---
## leaf 105
n  und  Faulenlassen  des  Flachses vorbereitete  Ausziehen  der  Flachsfaser  weisen  aisl.  rotinn  ,faul,  verfault' (aber  ü-rotinn  noch  ,wer  die  Haare  nicht  verloren'),  rot  n.  ,Fäulnis; Ohnmacht^,  as.  rotön  ,von  Rost  verzehrt  werden',  ags.  rotian  ,faulen, welken';  mnd.  röten  ,Flachs  rösten',  ahd.  rözzen  , faulen',  mhd.  rözzen  und rcezen  , faulen  lassen',  nhd.  bair.  rossen  ,Flachs  faulen  lassen'  (umgebildet zu  rösten  nach  rösten  ,auf  dem  Rost  braten'),  mhd.  röz  ,müibe';
hierher  ai.  Rudrd-  GN  (*}'ud-lo-),  päli  ludda-  ,grausam'  nach  W.  Wüst Rudrd-.
c.  reudh-  ,reuten,  roden'.
Av.  raoidya-  , urbar  zu  machen';
aisl.  rjöda  ,reuten,  räumen*,  mhd.  rieten  st.  V.  ,ausrotten,  vernichten^; aisl.  rjödr  n.  , offene  Stelle  im  Walde',  ahd.  reod  ,gerodetes  Land',  nhd. dial.  Ried  ds.,  ahd.  riuti  ds.,  riuten  (*riutjan)  ,reuten',  ablaut.  aisl.  rud n.  ,gerodete  Stelle  im  Wald',  mnd.  rot  ,das  Roden',  aisl.  rydja  ,roden ; aufräumen,  ausrotten',  ags.  äryddan  (engl,  rid)  ,berauben,  plündern'; mhd.  roteri,  nhd.  rotten;  mnd.  roden,  daraus  nhd.  roden,  afries.  tö-rotha ,ausrotten'.
## leaf 106
  rüpes  ,steile  Felswand,  Klippe, Felskluft,   jäher  Abgrund'   (vgl.    unten   lit.    rupis  ,Fels',   wozu   illyr.  ON ^PvTtsg,  Achaia,  und  in  ähnlicher   Bed.   nhd.   Riepe  ,Schuttreuse'  und  die tirol.    Ortsnamen   roupd,   rouf?,   geschrieben   Roppen,   Rofen),  rüpex,  -icia  ■;Tr;. , ruppiger  klotziger  Mensch,  Rüpel'  (vgl.  lit.  rvpüs  ,rauh,  grob');
aisl.  riüfaj  ags.  reofan  ,brechen,  zerreißen'  (ahd.  ä-riuh  ,atrox,  dirus', eigentlich  ,ungebrochen') ;  aisl.  ravf  f.  ,Spalte,  Loch',  ags.  reaf  n.  ,Raub, Beute,  Kleid,  Rüstung'  (*roupa  =  slav.  *rupa  ,Loch'),  ahd.  roub  m.  ds.,  zu  ,; got.  hi-rauböiij  ahd.  rouhön,  as.  röbön  , rauben',  aisl.  raufet  ,durchbrechen,  ^ rauben'  und  reyfa  ,durchbohren,  zerreißen',  ags.  he-rlefan  ,berauben';  aisl. reyfi  ,gerupfte  Wolle,  rauhes  Fell',  mndl.  roof  , abgezogenes  Fell';  geminiert ostfries.  rubben  , kratzen,  reiben,  rupfen',  nd.  rubbelig,  rubberig  , uneben, rauh',  nhd.  ruppig  ,struppig',  engl,  rubble,  rubbish  ,Schutt,  Abfall';  aisl. rüfiim  ,borstig,  struppig,  rauhhaarig';  nhd.  rüffeln  , scheuern,  hart  zusetzen*;
lit.  rüpki  ,sich  kümmern',  rüpüs  ,besorgt'  (zu  russ.  rupd  ,Sorge_,  Gram'), raupyti  und  (idg.  Ablaut  ou :  öu)  ruopti  ,graben,  höhlen',  riipas  ,rauh, holperig',  rupüs  ,rauh,  grob',  rupis  ,Fels',  ostlit.  raupat  PI.  ,Masern, Pocken'  ('Rauhigkeit  in  der  Haut'),  raupsai  , Aussatz';  auch  lit.  rvpuil, raupeltl  , Kröte'  (von  der  Rauheit  der  Haut),  vgl.  auch  lett.  raupa  , Gänse- haut' (,Schauder');  serb.  rüpa  ,Loch,  Grube'  {*roupa),  poln.  rupic  sie  ,sich kümmern',  ablaut.  rypac  ,scindere,  friare'.
f.  reus-:  aisl.  reyrr  m.  , Steinhaufen',  rast  f.  ,Trümmer,  zerfallene  Mauer' (s.  oben  S.  686  über  ai.  lostd-  m.  n.);  ahd.  riostar  ,Pflugsterz',  ags.  reost ,ein  Teil  des  Pfluges',  nhd.  dial.  riester  ,Lappen  zum  Schuhflicken';  dän. ros   »Schnitzel,    Abfall*,    norw.    dial.   ros,    rys   ,Fischschuppe',    rus   , dünne
r
## leaf 107
 lett.  raust , schüren,  wühlen',  rausfU  ,zerreD,  reißen',  rwsa  , aufgehäufter  Schutt' ;  über aksl.  ruHti  ,umstürzen*,  "^i'uchh  , Bewegung*,  s.  oben  S.  332.
WP.  II  351  ff.,  WH.  II  445  f.,  447  f.,  451  ff.,  Trautraann  240,  241,  247, Wissmann  Nom.  Postverb.  10,  130,  176  f.
j.  reu-,  reu-s-  , eilen*,  s.  oben  S.  331  f.,  wozu  noch  mir.  rüaimm  , Ansturm', bret.  rianm  ,Schaar'  {*reu-smen).
4.  reu-  , nachforschen*,  s.  oben  S.  337.
reu-b  und  reu-g-  ,sich  erbrechen,   rülpsen,  hervorbrechen*,   auch  , Wolke, Rauch*?
## leaf 108
.  128  f.,  Trautmann  244.
reudh-  ,rot^;  roudho-,  rudh-rö-,  rudhio-,  rudh-so-  ds.
Ai.   röhita-  =  av.   raoiöita-  _,rot,   rötlich^;,  röMt-  ,rote   Stute,  Weibi einer   Gazelle',   röhi-   m.,  röJil  f.  , Gazelle';    ai.    löhd-  , rötlich^,   m.  n. liebes  Metall,  Kupfer,  Eisen'  (formell  ==  lat.  rüfusj  air.  rüad,  got.  rat lit.   raüdas,   aksl.   rud^),   rödhra-,    lödhra-    m.    ,sjmplocos    racemosa, Baum,  aus  dessen  Rinde  ein  rotes  Pulver  bereitet  wird',  losta-  n.  ,Ei rost'  (*reudh'S-to-) ;  rudhird-  ,rot,  blutig',  n.  ,Blut'  {*rudh-i-ro-,  kontaminie aus  *rudh-ro-  und  *rudh-i-) ;  khotansak.  rrusta-  ,rot^  (*reudh-s-to-)
gr.  igsvO^o)  ,ich  röte'  (=  aisl.  rjöda),  sgevd-og  n.  ,Röte'  (vgl.  lat.  rtil igvd^QÖg   ,rot'   (=  lat.  ruber,  aksl.  *r^dr^  usw.);    igvcißt]  ;,Mehltau,   robl (Ausgang  unklar),  igvai-nsXag  , Röteln'  {^igvoGL-,  *rudh-s-)]
lat.  rübidus  ,dunkelrot'  (mit  -c?o- Weiterbildung  =  ai.  löJid-)-
## leaf 109
da  ,blutig  machen',  ags.  reodan  ,r färben',  got.  (über  , schamhaft  erröten')  ga-riups  ,ehrbar',  ga-riudei  ,Schai haftigkeit';  ablaut.  rau'ps,  aisl.  rauär,  ags.  read,  ahd.  rot  ,rot',  aisl.  raudi ,rotes  Eisenerz',  rodra  f.  ,Blut',  rodi  m.  ,Röte',  ryd  n.  und  rydr  m.  ,Rost roda  ,rot  sein  oder  werden',  ahd.  roten  ,erröten',  mhd.  rot  ,rot',  ahd.  rotami rosamo  i^rudh-s-men-)  ,Röte'  (hierzu  aisl.  rosmu-fjgll  ,rötliche  Berge*), rudu  ,Röte',  rudig  ,rötlich';  ä-ryderian  ^erröten';  ags.  rüst,  ahd.  as.  f^ ,Rost'  {*'rMh-s-t6)\
m
873
lit.  raüdas,  raudönas  ,rot',  raudä  ,rote  Farbe';  rüdas  ^braunrot'  (lett. riids  , rötlich'),  ruduo  , Herbst',  rudUi  _,rosteii',  rüdis  f.  ,Rost',  rüdynas, rüdynäj  rädyne  , Sumpf  mit  rötlichem,  eisenhaltigem  Wasser,  Morast, Pfütze',  raüsvas  (*roudh-s-uo-)  , rötlich',  lett.  rwsa  (*rüdh-s-a)  ,Rost',  lit. yüsvas  ,rotbrauii'  {*rudh-s-uo-),  ruslis  , Bratrost',  ruseti  ,g'limmen,  brennen', lett.  rusla  ,Art 
## leaf 110
 rotbrauner  Farbe',  lit.  riXstas  ,bräunlich,  lila'  {*rudh-s-to-), lett.  rusta  ,braune  Farbe',  rüstet  ,rot  färben';
aksl.  rud^  ,rot',  ruda  ,Erz,  Metall',  rus^  (*roudh-s-o-)  ,rötlich,  blond'; *')'^dr^  ,rot'  in  r.-ksl.  rodr^-^  TbdHi  s^  ,sich  röten'^  Tbzda  ,Rost',  russ.  rysyj ^rötlich  blond'  (*rüdh-8-o-j  vgl.  lett.  ?'M5a);
toch.  A  rätr-ärkyant  , rotglänzend',  rtär,  B  rätre  ,rot'  {^rutre-'^).
ai.  ravi-  m.  , Sonne',  arm.  arev  ds.  kann  nur  sehr  unsicher  als  ,der Rote'  gedeutet  werden;  lat.  raudus,  rödus,  rüdus  ,ein  formloses  Erzstück als  Münze'  ist  vielleicht  mit  ai.  löhd-  ,rotes  Metall,  Kupfer,  Eisen'  und aisl.  raudi  ,rotes  Eisenerz',  aksl.  ruda  ,Erz,  Metall'  zu  verbinden  und gall.  oder  illjr.  Lw. ;
auch  ahd.  aruzzi,  erizzi,  aruz,  as.  arut  ,Erz,  Erzstück',  aisl.  ortog (*arut{a-taugo)  , Drittel  eines  0re'  sind  wegen  des  Schwankens  der  Formen als  entlehnt  zu  betrachten;  daher  besteht  Hommels  Herleitung  aus  sum. iirud  ,Kupfer'  letztlich  zu  Recht,  anders  Kretschmer  Gl.  32,  6  ff.
## leaf 111
o-ko-)  ]  jav.  uru&wardj  -wan-  n.  {*rut-uar-   .-nn   \
, Eingeweide,  Bauch';  '
ags.  reada  jTiernaagen*,  engl,  read  , Labmagen*  {*routo-)^  andl.  rooA , Blättermagen*;  schwed.  dial.  rudda   f.  , Labmagen'  {^ruddön-),
Liden  KZ.  61,  14  f.
reuo-'.rü-  ,öffnen';  reues-  ,Raum,  weit*.
## leaf 112
239  f.,  der den  Bären  als  , Zerstörer,  Schädiger^  deutet,  zu  ai.  rdksäs-,  n.  ,Zerstörung^, av.  ra§-  ,beschädigen^  (S.  864) ;  vgl.  auch  Frisk  Gr.  et.  Wb.  141  f.
s.
sä-,  SQ-  ,satt;  sättigea*;  sä-ti-s  ,Sattlieit^
Ai.  a-si-n-vd-j  dsinvan  , unersättlich^  (setzt  ein  Praes.  *sd-neu-mij  »^ voraus);
arm.  at-ok"^  ,voll,  ausgewachsen^;  hac,  hacoy  ,zufrieden^  (^sadio-)]
```


## [2026-09-14T01:22:24.225Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /raoyna/ {print \"LEAF\",NR; print}' POK_03.txt | head -40"
}
```


### [2026-09-14T01:22:25.560Z] TOOL RESULT

```
LEAF 110
 rotbrauner  Farbe',  lit.  riXstas  ,bräunlich,  lila'  {*rudh-s-to-), lett.  rusta  ,braune  Farbe',  rüstet  ,rot  färben';
aksl.  rud^  ,rot',  ruda  ,Erz,  Metall',  rus^  (*roudh-s-o-)  ,rötlich,  blond'; *')'^dr^  ,rot'  in  r.-ksl.  rodr^-^  TbdHi  s^  ,sich  röten'^  Tbzda  ,Rost',  russ.  rysyj ^rötlich  blond'  (*rüdh-8-o-j  vgl.  lett.  ?'M5a);
toch.  A  rätr-ärkyant  , rotglänzend',  rtär,  B  rätre  ,rot'  {^rutre-'^).
ai.  ravi-  m.  , Sonne',  arm.  arev  ds.  kann  nur  sehr  unsicher  als  ,der Rote'  gedeutet  werden;  lat.  raudus,  rödus,  rüdus  ,ein  formloses  Erzstück als  Münze'  ist  vielleicht  mit  ai.  löhd-  ,rotes  Metall,  Kupfer,  Eisen'  und aisl.  raudi  ,rotes  Eisenerz',  aksl.  ruda  ,Erz,  Metall'  zu  verbinden  und gall.  oder  illjr.  Lw. ;
auch  ahd.  aruzzi,  erizzi,  aruz,  as.  arut  ,Erz,  Erzstück',  aisl.  ortog (*arut{a-taugo)  , Drittel  eines  0re'  sind  wegen  des  Schwankens  der  Formen als  entlehnt  zu  betrachten;  daher  besteht  Hommels  Herleitung  aus  sum. iirud  ,Kupfer'  letztlich  zu  Recht,  anders  Kretschmer  Gl.  32,  6  ff.
WP.  II  358  f.,  WH.  II  420  f.,  444  f.,  455,  456,  Trautmann  239.
reugh-ni(e)n-  ,Rahm'?
Av.  raoyna-  ,Butter',  mpers.  npers.  röyan  , (ausgelassene)  Butter';  aisl. rjümi  m.  ,Rahm',  ablautend  ags.  7'eamj  mnd.  rövie,  ahd.  roum  , Sahne', und  mnd.  räme  (für  *röme)j  woraus  nhd.   Rahm^   mit  ü  Schweiz,   rüm    ds.
WP.  II  357  f. ;  s.  auch  oben  S.  868.
reuS'  Rüster?
Ir.  imaimm  ,betula  alnus,  alnus  glutinosa'  (^reiis-men) -, zu  ahd.  omsty  mhd.  nhd.  Rüster? WP.  II  361.
reu-smen-  »Wiederkäuen ;  Kehle,  Gurgel'.
Ai.  römantha-  m.  , Wiederkäuen';  wakhi  ramöt  (*raumq&a-)  ds.;  kati zemetr  (*romantra-)  ds.;
lat.  nimeriy  -inis  , Kehle,  Gurgel,  Schlund',  rüma,  rümisj  -is  ds.  (können •  m   aus   mn  haben,    wie;)    inimäre   neben   rüminäre    , wiederkäuen';    kymr. rhumen  ,  Wanst,  Euter' ;  vgl.  oben  S.  872.
WP.  II  360  f.,  Loth  RC.  43,  146;  Frisk  Suffixales-^Ä-  14  f.
reuto-    routo-,  ruf-  ,Tiermagen,  Eingeweide'.
874 da
Mpers.   rot   , Eingeweide   des   Rindes*,   npers.    rüda^    PI.  rüdag-ani    a
arme,  Eingeweide*  (*reut
```


## [2026-09-14T01:22:31.600Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 72 73 74 75 76; do echo \"## leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_03.txt | head -4; done"
}
```


### [2026-09-14T01:22:32.707Z] TOOL RESULT

```
## leaf 72
h-  und  Nierenfett*,  nhd.  Flom,  Flaum  m.  ds.,  aisl.^ey (=  nXotov,  *plouiom)  n.  ,Schiff';  aisl. /M  f.  ,blinde  Klippe'  (d.i.  ,über- flutete';  ü  :  ö[«]  :  eit);  ple-  in  mhd.  v^jen  ,spülen';  plö[u]-  in  aisl.  flöa, ags.  flöwan  ,überfließen',  got.  flödus  (:  nXcorög),  aisl.  flöcC  f.  n.,  ahd.  fluot ,FlutS  aisl. /öl  m.  ,Sumpf';
lit.  Kausat.  plduju,  plöviau,  plduti  ,waschen,  spülen',  Fut.  pldusiu  (^plöu- siö)]  plntis  , offene  Stelle  im  Eise';  plevesüoti  ,flattern';
837
iksl-  Jplovg,  pluti  ^fließe,    schiffe',  plujg,    schwimme',    Kaus.-Iter.  serb. l()viti , schwemmen,  schwimmen',  russ.  plov  ,Boot',  klr.  plov  ,natätiö',  dehn- go-  aksl.  plaviti , schwimmen  lassen',  -se  ,navigare',  j:^^a'i^«^i , schwimmen'; -erb.  p^^^^  ^-1  plüto  n.  ,Kork* ;  *plü'  im  Inf.   russ.  plyth,  serb.  pliti] toch.  A  B  "plu-  , fliegen,  schweben',  B  plewe  , Schiff'.
## leaf 73
 floccho  ,lanugo',  nhd.  Flocke,  mnd.  vlocke  ,Woll-,  Schnee- flocke', norw.  dial.  flugsa,  flygsa  , Schneeflocke';  Iit.  pldukas  ,ein  Haar', plaukai  , Haare',  lett.  plauki  , Schneeflocken ;  Abfall  beim  Weben  ;  Staub ; Mutterkorn',  plaükas  , Abfall  beim  Spinnen,  Flocken,  Fasern;  Hülsen'; lett.  plücu,  plükt  fi^üücken,  raufen,  zupfen,  schleißen',  Iit.  plüksna,  plünksna ,Feder'.
WP.  II  97.
pl(e)u-mon-y  pleu-tio-  , Lunge'.
Ai.  klöman-  m.  n.  ,die  rechte  Lunge'  (Dissim.  von  p — m  zu  k-^m)  = gr.  nXsv}A,a)v  , Lunge'  (durch  Anlehnung  an  Ttveco  auch  7tve'öy,(üv) ;  lat.  pulmo, meist  PL  , Lunge'  (aus  *pelmönes  oder  "^plumönes)]
## leaf 74
bach-Endzelin  III  325).  •
WP.  II  100,  WH.  II  319,  320;  Erweiterungen  der  Wurzel  peh-  ,flach, eben',  oben  S.  805.
plouto-,  pluto-  ,aus  Brettern  oder  Stangen  Gefertigtes'.
Lat.  pluteus,    -um   , Schirmdach,  Wandbrett,    Zwischenwand',   ablautend  :^£ mit  lit.  plautas  ,Steg  am  Bienenstock',  lett.  pläuts  ,Wandbrett',  plautaX    ^ ,die  Bänke  an  der  Wand  der  Badestube'  und  aisl.  fleydr  f.  ,Dachsparren', norw.  expressiv  flauta  f.  »Querbalken  an  einem  Schlitten'.
## leaf 75
  vöder  ds.;  ahd.  {fedar)fötar  ,canna', spätahd.  füoter  ,theca',  nhd.  Futter  (des  Kleides),  Futteral]
lit.  piemuö  ,Hirt',  Akk.  piemenj,  (^pöimen-).
WP.  II  72,  Trautmann  204,  207  f.
2.  pö{i)-  :  pi-  und  (von  po-  aus)  Po-  , trinken';   Aoristwurzel,  wozu  sekun-
## leaf 76
.  pojq,  pojiti  ,tränke';  baltoslav.  *pöta-  und *plta-  ,getrunken'  in  lit.  puotä  f.  , Trinkgelage'  und  aksl.  pitijh  , trinkbar'; baltoslav.  *pöti  und  *piti  L  ,das  Trinken'  in  apr.  Inf.  poüt  (*pöti')  und slov.  pit  f.  , Getränk'  (Infin.  *piti);  baltoslav.  *pötu-  m.  ,das  Trinken'  in apr.  Inf.  puton,  pouton  und  poutwei  ,trinken',  ablaut.  Supinum  russ.-ksl.  pit^.
WP.  II  71  f.,  WH.  I  103  f.,  Trautmann  228  f.
polo-:pölo-  , geschwollen,  dick,  groß'.
\jqX.  polleö,  -ere  ,bin  stark,  vermöge*,  Denomin.  eines  "Apollos  aus  *pol-no-; dazu  polleXy  -icis  m.  ,Daumen,  große  Zehe' ;  urslav.  pah  in  russ.  bez-pahij , fingerlos';  aruss.-ksl.  pahcz  , Daumen'  (*poliko-),  usw.;  vielleicht  dazu  als
```


## [2026-09-14T01:22:38.872Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD reudh ===\"; grep -n -A15 \"^reudh-\\|^ *reudh-\" AHD_watkins1985.txt | head -40; echo \"=== AHD reug ===\"; grep -n -B2 -A15 \"reug-\\|reugh-men\\|reug-men\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-14T01:22:39.043Z] TOOL RESULT

```
<persisted-output>
Output too large (33.4KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bhwxdq038.txt

Preview (first 2KB):
=== AHD reudh ===
=== AHD reug ===
404-d6-. To give. Contracted from *doo-. 1. Zero-grade form *do- in Latin dare, to give: DADO, DATE, DATIVE, DATUM, DIE?; ADD, BETRAY, EDITION, PERDITION, RENDER, (RENT!), (SURRENDER), TRADITION, (TRAITOR), (TREA- SON), VEND. 2. Suffixed form *dé-no- in Latin dénum, gift (> ddndre, to present, forgive): DONATION, DONA- TIVE, DONOR; CONDONE, PARDON. 3. Suffixed form *do-t/i)- in: a. Latin dds (genitive détis), dowry: DOT?, DOWAGER, DOWER, (DOWRY); ENDOW; b. Slavic *datja in Russian dacha, gift: DACHA; C. Russian dat’, to give, in izdat’, to publish: sAMIzDAT. 4. Reduplicated form *di-dé- in Greek didonai, to give: DOSE; ANECDOTE, ANTIDOTE, APODOSIS, EPIDOTE. [Pok. d6- 223.] [dorsum. The back. Latin noun of unknown origin. DORSAL, DORSO-, DORSUM, DOSS, (DOSSAL), DOSSER, DOS- SIER; ENDORSE, INTRADOS, REREDOS.]
405-drem-. To sleep. Suffixed zero-grade form “drm-yo- in Latin dormire, to sleep: DORMANT, DORMER, DORMITORY. [Pok. dré- 226.]
406:[dreug-. Dry. Germanic root. 1. Old English driigoth, drigath, dryness, drought: DROUGHT. 2. Suffixed form *drig-iz in Old English dryge, dry: DRY. 3. Suffixed variant form *draug-n- in Old English dréahnian, to strain, drain: DRAIN.]
407-[dub-. Also dup-. To drop, dip. Germanic imitative root. 1. Old English -doppa, a kind of bird (< “one that dips”): DIDAPPER. 2. Dutch doopen, to dip: DOPE. 3. Old English *dympel (diminutive with nasal infix), pool, dimple (> Middle English dimpel): DIMPLE. 4. Norwegian dumpa, to fall suddenly, akin to the Scandinavian source of Middle English dumpen, to dump: pump. [In Pok. dheu-b- 267.]]
408-[dud-. To shake, deceive. Germanic root. 1. Norwegian dudra, to quiver, akin to: a. Middle English daderen, to tremble: DODDER!; b. Middle English doder, vine (< “that which quivers in the wind”): DODDER2. 2. Middle English doten, to be foolish: DOTE. [In Pok. 4. dheu- 261.]]
...
</persisted-output>
```


## [2026-09-14T01:22:42.792Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"reudh\\|reug\\b\\|reugh-\\|RUBY\\|RAMEKIN\\|REEK\\|RUST\\b\" AHD_watkins1985.txt | grep -i \"reudh\\|reugh\\|^[0-9]*:reug\\|ramekin\" | head -20"
}
```


### [2026-09-14T01:22:42.870Z] TOOL RESULT

```
391:dhreugh-. To deceive. Germanic suffixed form *drau(g)ma- in Old English dréam, vision, illusion, dream (but attested only in the senses of “joy,” “music”): DREAM. [Pok. 2. dhreugh- 276.]
648:English hréowan, to distress, grieve: RUE!, RUTH. 2. Ex- tended o-grade form *krous- in Greek krouein, to strike: ANACRUSIS. [Pok. 3. kreu- 622.] kreup-. Scab; to become encrusted. 1. Germanic *hrub- in: a. Middle Low German ruffelen, to crumple, akin to the Germanic source of Middle English ruffelen, to ruffle, roughen: RUFFLE}; b. Germanic compound *ga-hrub- (*ga-, intensive prefix; see kom) in Middle Dutch grof, harsh: GRuFF. 2. Suffixed o-grade form *kroup-d in Serbo-Croatian krupa, groats (perhaps > German Graupe, barley): GRAUPEL. [Pok. kreup- 623.] kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in: a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN, CRUSTACEOUS, CRUS- TOSE; b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.] kreut-. Also kreudh-. Reed. Germanic *hreuda- in Old English hréod, reed: REED. [Pok. kreut- 623.] kropo-. Roof. Germanic *hréfam in Old English hrdf, roof: ROOF. [Pok. krdpo- 616.] krut-. Musical instrument. 1. Germanic *Arut- in Old French rote, a stringed instrument: ROTE3, 2. Geminated form *krutté in Welsh crwth, an ancient Celtic instru- ment: CROwD?. [Pok. krut- 624.] ksero-. Dry. 1. Lengthened-grade form *kséro- in Greek xéros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHAL- MIA. 2. Perhaps suffixed variant form “kseres-no- in Latin serénus, serene, bright, clear: SERENE. [Pok. ksero- 625.] ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: syN-. 2. Russian so-, s-, with, in sputnik, fellow traveler (see pent-): SPUTNIK. [In Pok. 2. sem- 902.] ku-. Hypothetical base of a variety of conceivably related Germanic words meaning “a hollow space or place, enclosing object, round object, lump,” and some other derivative denotations. 1. Germanic *kubdn-, hut, shed, room, in: a. Old English cofa, bedchamber, closet: COVE!; b. Middle Dutch cubbe, “pen, stall,” fish basket, akin to the probable source of CUBBY; C. Germanic compound *kubawald-, probably “house ruler,” household god (wald-, power; see wal-), in Middle High German kobolt, an underground goblin: COBALT, KOBOLD. 2. Germanic *kutam in Old English cot, cottage: COT?, (COTTAGE). 3. Germanic *kutdn- in Old English cote, shelter: CoTE!. 4. Germanic *k(e)ud- in: a. Old English codd, bag, husk: cop?; b. Old English cudele, cuttlefish (from its ink bag): CUTTLE. 5. Germanic k(e)ut- in Old English *cieter, intestines (probably > Middle English chiterling): cx1T- TERLINGS. 6. Germanic *kukk- in Middle English cok, haycock, pile of straw: cock?. 7. Germanic *kuk- in Old English cicen, chicken: CHICKEN. 8. Germanic *kugg- in Swedish kugge, cog, akin to the possible Scandinavian source of Middle English cogge, cog: coc}. 9. Germanic *kuggila in Old English cycgel, rod, cudgel: CUDGEL. 10. Germanic *keulaz in: a. Low German kielswin, keel- son: KEELSON; b. Middle Dutch iel, ship, keel of a ship: KEEL?, 11. Germanic *kijp- in Middle Dutch kipe, cask, tub, basket: COOPER. 12. Germanic *kunt- in Middle Low German kunte, vulva, akin to the Low German source of Middle English cunte, vulva: CUNT. 13. Germanic kird- in Icelandic kiird, to crouch, lie in wait, akin to the Scandinavian source of Middle English couren, to cower: COWER. 14. Possibly Old Norse kiiga, to oppress, akin to the probable source of cow?. [In Pok. géu- 393.] kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: Kiss. [Pok. ku-, kus- 626.] kwat-. To ferment, be sour. Possible root. Suffixed vari- ant form *kwét-so- in Common Slavic *kvasi in Russian kvas, kvass: Kvass. [Pok. kuat(h)- 627.] kwe, And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]
897:reu-2, Also reue-. To smash, knock down, tear out, dig up, uproot. 1. Suffixed o-grade form *rous-o- in Ger- manic *rawwa- in: a. Old Norse régg, réggr, woven tuft of wool: RAG}; b. Norwegian rugga, rogga, coarse cover- let, akin to the Scandinavian source of RUG. 2. Basic form *reu- in Latin ruere, to collapse, cause to collapse: RABBLE, RUIN. [Pok. 2. reu- 868.] reudh-', Red, ruddy. I. O-grade form *roudh-. 1. Ger- manic “raudaz in: a. Old English réad, red: RED; b. Old Norse rauthr, red (> reythr, rorqual): RORQUAL. 2. Ger- manic *raudnia- in Old Norse reynir, mountain ash, rowan (from its red berries), akin to the source of ROWAN. 3. Latin rijfus (of dialectal Italic origin), reddish: RUFES- CENT, RUFOUS. 4. Latin rdbus, red, in robigd, ribigo, rust: RUBIGINOUS. 5. Latin rdbur, rdbus, red oak, hard- ness, and rdbustus, strong: ROBLE, ROBORANT, ROBUST; CORROBORATE, RAMBUNCTIOUS. II. Zero-grade form *rudh-. 1. Form *rudh-d- in Germanic *rud6 in: a. Old English rudu, red color: RUDDLE, RUDDY; b. Old English rudduc, robin: RUDDOCK. 2. Suffixed form *rudh-sto- in Germanic *riist- in Old English rdst, rust: RusT. 3. Latin rubeus, red: ROUGE, RUBEOLA, RUBY; RUBEFACIENT 4. Latin rubicundus, red, ruddy: RUBICUND. 5. Latin rubidus, red: RUBIDIUM. 6. Suffixed (stative) form *rudh-é- in Latin rubére, to be red: RUBESCENT; ERUBES- CENCE. 7. Suffixed form *rudh-ro- in: a. Latin ruber, red: RUBELLA, RUBRIC; BILIRUBIN; b. Latin rutilus, reddish: RUTILANT; Cc. Greek eruthros, red (with pro- thetic vowel, from oldest root form *sreudh-): ERY- THEMA, ERYTHRO-; d. possibly remade Greek erusi-, red, reddening: ERYSIPELAS. 8. Suffixed form *rudh-to- in Latin russus, red: RISSOLE, ROUX, RUSSET. [Pok. reudh- 872.] reudh-2, To clear land. 1. Suffixed zero-grade form *rudh-yo- in Germanic *rudjan in Old Norse rydhja, to clear land: RID. 2. Possibly Germanic expressive variant *rudd- stick, club, in Old English rodd, stick: Rop. [In Pok. 2. reu- 868.] reue-. To open; space. 1. Suffixed variant form *ri-mo- (< *rua-mo-) in Germanic *riimaz in: a. Old English rim, space: ROOM; b. Old French run, ship’s hold, space: RUMMAGE. 2. Suffixed form *reu(g)-es- in Latin ris, “open land,” the country: RURAL, RUSTIC. [Pok. reuo-, ri- 874.] reug-. To vomit, belch, smoke, cloud. 1. Germanic *reu- kan in Old English réocan, to smoke, reek: REEK. 2. Suf- fixed zero-grade form *rug-to- in Latin ructdre, to belch: ERUCT. [Pok. 4. reu- 871.] reugh-men-. Cream. O-grade form *roughmen- in Ger- manic *rau(g)ma- in Middle Low German rém(e), cream: RAMEKIN. [Pok. reugh-m(e)n- 873.] reup-. Also reub-. To snatch. I. Basic form *reub- in Germanic *rupja in Flemish rippen, to rip: RIP!. II. O-grade form *roup-. 1. Germanic *raufjan in: a. Old English réafian, to plunder: REAVE!; b. Old English beréafian, to take away (be-, bi-, intensive prefix; see ambhi): BEREAVE. 2. Germanic *raubén, to rob, in: a. Middle Dutch and Middle Low German réven, to rob: ROVER; b. Old French rober, to rob: ROB; c. Italian rubare, to rob: RUBATO. 3. Germanic *raubd, booty, in Old French robe, robe (> “clothes taken as booty”): ROBE. 4. Suffixed form *roup-tro- in Sanskrit loptram, booty, from lumpati, he breaks, removes: LOOT. III. Zero-grade form *rup-. 1. Latin dsirpdre (< *isu- rup-; isus, use, usage, from iti, to use), originally “to interrupt the orderly aquisition of something by the act of using,” whence to take into use, usurp: USURP. 2. Na- salized form *ru-m-p- in Latin rumpere, to break (> riipés, rock): ROUT!, RUPTURE; ABRUPT, BANKRUPT, CORRUPT, DISRUPT, ERUPT, INTERRUPT, IRRUPT, RUPICO- Lous. [Pok. 2. reu- 868.] rezg-. To plait, weave, wind. Germanic *ruski- in Old English risc, rysc, rush: RUSH?. [Pok. rezg- 874.] [risan. To rise. Germanic word. 1. Germanic *risan in:
1299:BILBERRY bhel-2 BILINGUAL dnghi BILIRUBIN reudh-1 BILIVERDIN virére BILL! beu-1 BILL? bhei-2 BILLS = bhei-2 BILLET! beu-1 BILLET-DOUX = dik-u- BILLOW bhelgh- BILTONG bhel-2, dnghi BIMESTRIAL mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
1475:ERR ers-1 ERRANT ei-1 ERRATIC ers-1 ERRATUM ers-1 ERRONEOUS ers-1 ERROR ers-1 ERSATZ sed-1, ud- ERSE peie- ERST ayer- ERUBESCENCE reudh-1 ERUCT reug- ERUPT reup-
1476:ERYSIPELAS pel-4, reudh-1
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
2160:RABBET battuere RABBLE? reu-2 RABID rebh-1 RABIES rebh-1 RACE? ers-1 RACES wrad- RACHIS wragh- RACK! reg-1 RACK3 wreg- RACLETTE réd- RADDLE! reidh- RADICAL wrad- RADICLE wrad- RADIOSONDE swem- RADISH wrad- RADIX wrad- RADULA réd- RAFT! rép-2 RAFTER rép-2 RAG! reu-2 RAGA reg-3 RAGE rebh-1 RAGOUT geus- RAID reidh- RAIL! reg-1 RAIN reg-2 RAINBOW reg-2 RAISE risan RAJ reg-1 RAJAH_ reg-! RAKE! reg-1 RALLENTANDO lento- RALLY leig-1 RAMBUNCTIOUS reudh-1 RAMEKIN reugh-men- RAMIFY wrad- RAMOSE wrad- RAMP2  skerbh- RAMPART pere-1 RAMPION rap- RAMSON krem- RAMUS wrad- RANCH sker-3 RANGE sker-3 RANI reg-1 RANK!  sker-3 RANK? reg-1 RANKLE derk- RANSACK sag- RANSOM em- RAPACIOUS rep- RAPE! rep- RAPE? rap- RAPHE wer-3 RAPHIDE wer-3 RAPID rep- RAPPORT per-2 RAPPROCHEMENT per! RAPT rep- RARE! era-2
2175:RECTUM reg-1 RECUMBENT keu-2 RECUPERATE kap- RECUR kers-2 RED reudh-1 REDE ar- REDEEM em- REDEMPTION em- REDOLENT od-1 REDOUBT deuk- REDOUBTABLE dwo- REDOUND wed-! REDSTART ster-1 REDUCE deuk- REDUNDANT wed-1 REDUVIID eu-! REED kreut- REEF! = rebh-2 REEF? rebh-2 REEK reug- REEL! krek-1 REFECT dhé-1 REFECTORY dhé-1 REFER bher-! REFLUX bhieu- REFRACT bhreg- REFRAIN! ghrendh-
2185:RID reudh-2
2192:RIP! reup- RIPARIAN rei-1 RIPE rej-1 RIPPLE? rei-1 RISE isan RISORGIMENTO reg-1 RISSOLE reudh-1 RITE ar-
2197:ROBE reup- ROBLE reudh-1 ROBORANT reudh-1 ROBOT orbh- ROBUST reudh-1 ROCAMBOLE bhel-2, ruk-1 ROCHET ruk-1 ROCKET! = ruk-1 ROCKET? ghers- ROCKETSONDE swem- ROD reudh-2 RODENT réd- RODEO ret-
2199:ROOF kropo- ROOK! ker-2 ROOM reua- ROOST kred- ROOT! wrad- ROOT? wrdd- ROPE rej-1 RORQUAL = reudh-1, (s)kWal-o- ROSE! wrod- ROSEMARY ers-2 ROSTRUM_ réd- ROTA ret- ROTARY ret- ROTATE ret- ROTE? reu-! ROTE3 krut- ROTIFORM ret- ROTOGRAVURE ret- ROTUND ret- ROTUNDA ret- ROUGE reudh-1 ROUGH ruk-2 ROULETTE ret- ROUND! ret- ROUND? riino- ROUT! reup- ROUTS = reu-1 ROUX reudh-1 ROVER reup- Row! rej-1
2200:ROW? era-1 ROWAN reudh-! ROWEL ret- ROWEN wel-2 ROYAL reg-! -RRHAGIA wrég- -RRHEA sreu- RUBATO reup- RUBEFACIENT dhé-1, reudh-1
2201:RUBELLA reudh-1 RUBEOLA reudh-1 RUBESCENT reudh-1 RUBICUND reudh-1 RUBIDIUM reudh-1 RUBIGINOUS reudh-! RUBRIC reudh-1 RUBY reudh-1 RUCK? = sker-3 RUCKSACK sker-3 RUDDER ere-1 RUDDLE reudh-1 RUDDOCK reudh-1 RUDDY reudh-! RUE! kreue-2 RUFESCENT reudh-1 RUFFLE! kreup- RUFOUS reudh-1 RUG reu-2
2204:RUNE! riino- RUNE? riino- RUNNEL rei-3 RUPICOLOUS reup- RUPTURE reup- RURAL reue- RUSH? rezg- RUSSET reudh-! RUsT reudh-1 RUSTIC reue- RUT? reu-1 RUTABAGA wrad- RUTH kreue-2 RUTILANT reudh-1 Rx _ kap-
```


## [2026-09-14T01:23:00.638Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\""
}
```


### [2026-09-14T01:23:01.794Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-14T01:23:05.108Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ream\" KLN_1966.txt | head; echo \"---\"; grep -n \"^ramekin\\|^ramequin\" KLN_1966.txt | head; echo \"--- leaf 665 (p~1307) ---\"; awk 'BEGIN{RS=\"\\f\"} NR==666' KLN_1966.txt | grep -n \"ream\\|1307\\|1306\" | head -20"
}
```


### [2026-09-14T01:23:06.189Z] TOOL RESULT

```
31826:ream,  n.,  20  quires  of  paper.  —  ME.  reme,  fr.  OF. ray  me  (F.  rame),  fr.  Sp.  resma,  fr.  Arab.  rizmah, ‘bundle,  bundle  of  paper’.
31827:ream,  n.,  cream;  froth.  —  ME.  rem,  fr.  OE. ream,  ‘cream’,  rel.  to  MLG.  rom,  rome,  Du. room,  MHG.  roum,  G.Rahm,  Icel.  rjomi,  ‘cream’, fr.  Teut.  base  *rauma-,  which  corresponds  peril, to  I.-E.  *raugma-,  whence  Avestic  raoyna-,  ‘but¬ ter’.  Cp.  ramekin.
31829:ream,  tr.  v.,  to  enlarge  a  hole.  —  Lit.  ‘to  make room’,  fr.  ME.  remen,  rumen,  fr.  OE.  ryman,  ‘to make  room,  widen’,  fr.  rum,  ‘spacious,  wide’. Cp.  OS.  riimian,  ON.  ryma ,  OFris.  rema,  OHG. rumen,  ‘to  make  room,  widen’.  Cp.  also  E.  dial. rime,  ‘to  enlarge  a  hole’,  and  see  room, reamer,  n.,  a  tool  for  enlarging  a  hole.  —  Formed fr.  prec.  word  with  agential  suff.  -er. Derivatives:  reamer,  tr.  v.,  reamer-er,  n. reanimate,  tr.  v.,  to  bring  back  to  life.  —  Formed fr.  re-  and  animate,  v.
---
31610:ramekin,  also  ramequin,  n.,  a  preparation  of cheese  with  bread  crumbs,  eggs,  etc.,  baked  in  a small  dish.  —  F.  ramequin,  fr.  MLG.  ramken, dimin.  of  ram,  ‘cream’,  which  is  rel.  to  OE. ream,  of  s.m.  See  ream,  ‘cream’.  Fort  he  ending see  suff.  -kin.
--- leaf 665 (p~1307) ---
```


## [2026-09-14T01:23:10.229Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /^ream,  n\\.,  cream/ {print \"LEAF\",NR}' KLN_1966.txt; awk 'BEGIN{RS=\"\\f\"} /ramekin,  also  ramequin/ {print \"RAMEKIN LEAF\",NR}' KLN_1966.txt"
}
```


### [2026-09-14T01:23:11.310Z] TOOL RESULT

```
RAMEKIN LEAF 692
```


## [2026-09-14T01:23:13.721Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=695 && NR<=700 {print \"### LEAF\",NR; print substr($0,1,300)}' KLN_1966.txt"
}
```


### [2026-09-14T01:23:14.848Z] TOOL RESULT

```
### LEAF 695
rear,  reri,  ‘to  reckon,  believe, think’ ;  see  rate,  ‘amount’.  For  the  etymology  of L.  fiat  see  fiat.
ratal,  n.,  an  amount  at  which  property  is  assessed. —  Formed  with  adj.  suff.  -al  fr.  rate,  ‘amount’, on  analogy  of  rental. ratan,  n.  —  The  same  a
### LEAF 696
.  v.,  to  devour  greedily (rare).  —  MF.  raviner ,  ‘to  ravager’,  fr.  ravine, ‘rapine’.  See  ravin.
Derivatives:  raven-ing,  adj.,  raven-ing-ly,  adv., raven-ous,  adj.,  raven-ous-ly,  adv,,  raven-ous- ness,  n.
ravigote,  n.,  shallot  sauce.  —  F.,  back  formation fr.  r
### LEAF 697
nd  cp.  words  there  referred  to.
ream,  n.,  20  quires  of  paper.  —  ME.  reme,  fr.  OF. ray  me  (F.  rame),  fr.  Sp.  resma,  fr.  Arab.  rizmah, ‘bundle,  bundle  of  paper’.
ream,  n.,  cream;  froth.  —  ME.  rem,  fr.  OE. ream,  ‘cream’,  rel.  to  MLG.  rom,  rome,  Du. 
### LEAF 698
p., secondary  form  of  recabdo,  ‘caution,  care,  solic¬ itude,  attention’,  fr.  recabdar,  ‘to  gather,  keep in  custody,  assure’,  fr.  VL.  *recaptdre,  ‘to  seize’, fr.  re-  and  L.  captare,  ‘to  seek  to  catch’,  freq.  of capere  (pp.  captus ),  ‘to  catch’.  S
### LEAF 699
n,  ‘to  count,  reckon’,  OE.  recen,  ricen, ‘ready,  quick,  swift’,  fr.  I.-E.  base  *reg-,  ‘straight, right;  to  lead,  direct’,  whence  also  Gk.  opey^, ‘to  reach,  stretch  out’,  L.  regere,  ‘to  keep straight,  lead  straight,  guide,  lead,  rule’.  See regent, 
### LEAF 700
ler  (F.  reconcilier),  fr.  L.  reconciliare,  ‘to  bring together  again,  reconcile',  fr.  re-  and  conciliare, ‘to  bring  together’.  See  conciliate.
Derivatives:  reconcil-able,  adj.,  reconcil-abil-ity, n.,  reconcil-able-ness,  n.,  reconcil-abl-y,  adv., reconcil-ee,  n.,  reconc
```


## [2026-09-14T01:23:23.838Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=663 && NR<=668 {print \"### LEAF\",NR; print substr($0,1,250)}' KLN_1966.txt"
}
```


### [2026-09-14T01:23:25.127Z] TOOL RESULT

```
### LEAF 663
ential  suff.  -or. prevenance,  n,,  anticipation  of  the  needs  of  others. —  F.  prevenance,  fr.  prevenant,  pres.  part,  of prevenir,  ‘to  go  before,  anticipate’,  fr.  L.  prae- venire.  See  prevent  and  -ance. prevenient,  adj.
### LEAF 664
e, adj.,  and  -ive.
Derivatives:  primitive,  n.,  primitive-ly,  adv., primitive-ness,  n.,primitiv-ism,  n.,  primitiv-ist,  n., primitiv-ist-ic,  adj.
primo,  n.,  the  first  or  leading  part  ( mus .)  —  It.,  fr.
L.  primus,  ‘first’. 
### LEAF 665
alue,  price’.  Prize  is  the  doublet  of  price  (q.v.) The  spelling  prize  is  due  to  the  influence  of prize,  ‘act  of  seizing’.  Cp.  praise, prize,  tr.  v.,  to  estimate.  —  ME.  prisen,  fr.  OF. preisier,  prisier  (F.  pri
### LEAF 666
ns,  gen.  -entis,  pres.  part,  of  procidere, ‘to  fall  forward,  fall  down’,  fr.  1st  pro-  and cadere,  ‘to  fall’.  See  cadence.  For  the  change  of Latin  a  (in  cadere)  to  i  (in  prd-cidere)  see  abigeat and  cp.  words  t
### LEAF 667
l,  adj.  —  Formed  with  adj.  suff.  -al  fr. Late  L.  professorius,  ‘pertaining  to  a  public teacher’,  fr.  L.  professor.  See  prec.  word. Derivatives:  professorial-ism,  n .,  professorial-ly, adv.
proffer,  tr.  v.  —  ME.  pro
### LEAF 668
  a  suff.  frequently used  in  chemistry  and  biochemistry, prolapse,  n.,  the  falling  or  slipping  out  of  place of  an  internal  organ.  —  L.  prolapsus,  ‘a  gliding forward’,  fr.  prolapsus,  pp.  of  prolabi,  ‘to  glide forwa
```


## [2026-09-14T01:23:33.601Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=694 && NR<=699 {print \"### LEAF\",NR; n=split($0,a,\"\\n\"); for(i=1;i<=n;i++) if(a[i] ~ /^[^a-zA-Z]*1[0-9][0-9][0-9][^0-9]*$/) print \"   NUM:\",a[i]}' KLN_1966.txt; echo \"=== grep page nums generally ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=690 && NR<=700 {print NR\": \"; for(i=1;i<=3;i++){} }' KLN_1966.txt >/dev/null; awk 'BEGIN{RS=\"\\f\"} NR==697' KLN_1966.txt | grep -oE \"\\b1[23][0-9][0-9]\\b\" | head"
}
```


### [2026-09-14T01:23:35.193Z] TOOL RESULT

```
### LEAF 694
### LEAF 695
### LEAF 696
   NUM: 1307
### LEAF 697
   NUM: 1309
### LEAF 698
   NUM: 1310-
   NUM: 1311
### LEAF 699
=== grep page nums generally ===
1309
```


## [2026-09-14T01:24:09.232Z] TOOL CALL #21: Bash

```json
{
 "command": "pdftoppm -f 424 -l 424 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg424 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg424.png"
}
```


### [2026-09-14T01:24:11.493Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74989 Sep 13 21:24 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg424.png
```


## [2026-09-14T01:24:13.356Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg424.png"
}
```


### [2026-09-14T01:24:14.127Z] TOOL RESULT

```

```


## [2026-09-14T01:24:14.125Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T01:24:33.181Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD rōγn / rōy ===\"; grep -n \"rōγn\\|royn\\|roygn\\|rōy \\|lwgn\\|lwdy\\|rōd \\|rōy,\" PHD.txt | head -20; echo \"=== PHD_mackenzie ===\"; grep -n \"rōγn\\|rōy\\|rōd\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-14T01:24:33.315Z] TOOL RESULT

```
=== PHD rōγn / rōy ===
3913:sweetmeat royn-xwardig; afrōšag, gēzēnag, lawzénag, Šiftēnag, watrēnag.
4883:māzdēsn mahist, māst māzandar māš, maxš roynt
4927:ruzdīh royn-xwardig royn
=== PHD_mackenzie ===
```


## [2026-09-14T01:24:36.731Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"royn\\b\\|roy \\[\\|roy'\\|rod \\[\\|rodig\\|rōdīg\" PHD.txt | head -20; echo \"=== search 'brass' ===\"; grep -n -i \"brass\" PHD.txt | head -20; echo \"=== search 'butter' ===\"; grep -n -i \"butter\" PHD.txt | head -20"
}
```


### [2026-09-14T01:24:36.838Z] TOOL RESULT

```
148:tahm [thm | =M, N ~] strong, brave. tak [t^k' | N ~ 'vine'] branch. tohm(ag) [twhm(k') | M twhm, -g, N tuxm, -a] ... wanigar [wnykl) prodigal.
149:~Th : prodigality, waste. мапу |H(W)BDN < A hwbdn', bd |... wany(b)ūdīh |HWBDN'bwtyh, ... war-wézag [wl-w^yck'| andaxtan : cast lots. wāzīg ... read -wazig |-w cyk' | N -baz] -player. wezag |w yck'| lot. wiyaban, ~ig ... add confusing. Wizarš |wyzl3| a demon.
275:*brādarod [bPtlwt!'] relative, rival, counterpart. “АҺ: relationship, rivalry.
1780:entrails rodigàn.
2182:guts rodig(an).
3913:sweetmeat royn-xwardig; afrōšag, gēzēnag, lawzénag, Šiftēnag, watrēnag.
4919:lawzēnag rūzīg rozwürag rozan ranjwar rozward rozgar ranjag, rozag rozbinag roz-Saban rosnih rēšn rūšnag rūšngar rodbar rodigan rodig 12го rüdan abàg! rūstūg
4927:ruzdīh royn-xwardig royn
=== search 'brass' ===
256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
1070:brass brinj, rēy.
1071:brassard bāzābānag.
2138:Brass giya(h).
=== search 'butter' ===
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
1126:butter kär, rdyn.
1127:buttermilk, dried ~ kašk.
```


## [2026-09-14T01:24:57.853Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','SOD','HRN','CHEUNG']:\n  print(k, d[k].get('page_offset')); print('  hint:', str(d[k].get('lookup_hint'))[:400]); print()\""
}
```


### [2026-09-14T01:24:58.963Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
KeyError: 'CHEUNG'
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
  hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada

MON None
  hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab

SOD printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
  hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id

HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
```


## [2026-09-14T01:25:03.156Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 434 435 436 437 438 439; do echo \"##### LEAF $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -60; done 2>&1 | head -200"
}
```


### [2026-09-14T01:25:04.179Z] TOOL RESULT

```
##### LEAF 434
 ‫روز مریم‬                                                                           ‫‪avr‬‬
                                   ‫باشد ‪.#‬‬       ‫رور ننگ و نام ‪ - ۱‬بکراك‪‎.‬‬
                                                 ‫بمعنی روز کوشش است ککنهابه از ررز جنگ‬
‫وعم وسکون را وزا ودال ابجد‪ ,‬نام روزیتجشنیه‬     ‫وجدال وقتال و کینه خواستن باشد ‪ -‬و روز غنا‬
                                                   ‫ند‪.‬‬
                                                     ‫یام‬
                                                       ‫گهوون‬
                                                           ‫مزیشگ‬
                                                               ‫وساز وصحبت را یز رو‬
                                   ‫است ؟ ‪.‬‬
                                                  ‫نی‬
                                                   ‫نګ و فيرف»نش‬                    ‫رور‬
‫رود هریم ‪ -‬کنایه از خناموشی‬                              ‫وکوشش‬    ‫بر جنگ‬

‫وسکوت باشد؟ ‪ -‬کونابه از مرکهوموت حم‬             ‫رو ر نه ؟ د بفتح اول و تال و لون‬
                                   ‫‪4‬‬   ‫هت‬        ‫وسکون تانی ‪ ۰‬معروفت که مطلق‌سوراخ ومنقثة‬


  ‫‪۲‬شمار ‪۷‬‬
        ‫‪:‬وزن ‪»( ۳‬صمیر) «ارمغان سال ‪۱‬‬
                                   ‫از ر‬              ‫‪۴‬‬         ‫نك ولام ‪.‬‬
                                                                       ‫‪ -‬رك ‪:‬‬
  ‫معرب آن هم‌روزنة دنفس»‪ .‬اوسنا ‪« 301800231‬پورداود‪ .‬خرده‌اوستا ‪۲۱۲2۱‬‬           ‫عان ‪E‬‏‬
         ‫رك ‪:‬هرمز » هرمزد ‪-‬‬         ‫‪ - ۴‬دز اصطلاح ابرانیان باستان » روزاول هرماه شمسی‬
 ‫خطاب بمرم آمده ‪«:‬فقولی‬       ‫اشاره بروزة صمت مرربم‪" .‬درسورةٌ ‪٩۱‬‏ (مربم) ‪۷ 1‬‬       ‫‪۴‬‬

                                                ‫وتان من شر فیا کلام از‬
  ‫زی) از‪ :‬روز ‪( ۳-۰‬نیت)؛منسوب بروز‪:‬‬
                                  ‫کر‬‫ورسوم (در لهجةٌ م‬
                                                    ‫روزه ‪ -‬بضم‌اول ک‬
  ‫مکروزه » دو روزه ‪ -‬نخوردن و نیاشاه‌یدن ازسحر نا غروب (از اعمال دینی) ودرماه رمضان روزه‬
                                                     ‫داشتنمسلمانان را واجب است » صوم ‪.‬‬
  ‫‪ #‬روزی ‪ -‬بضم اول " از ‪ :‬روز ‪-۳‬ی (سبت) » پهلوی ‪)٥0۲‬‏ = ارمنی ع ‪61607‬‬
  ‫ر(زق یومیه) « هوبتمان ‪ > ۹۲۱‬دزفولی ‪ « 6120۲‬امام»؛ رزق » اصیب وقسمت و بهره و حط‪:‬‬
 ‫‪ ( ۳‬صیادی که ماهی دامرا ازدست او درربوده بوده دریاسخ معترض) گفت ‪ :‬ای برادر! چتوان کردن؟‬
  ‫لتان ‪ -۱۱۱‬خوراك هرروزه»غذا وطمام‪.‬‬
                                  ‫گ«‬‫مرا روزی نبود وماهی را همجنان روزی مانده بود »‬

                                                                            ‫بقیه از صفحة ‪۷۲٩‬‏‬
   ‫(که‬
     ‫ام‬‫نمه‬
         ‫روز نامه ‪ -‬بضم اول و کر ششم ( درلهجة مر کزی ) از ‪ :‬روز ‪ +‬نا‬                ‫‪#‬‬
  ‫پپلوی)» معرب آن روزنامج و روزنامجه‪ .‬بیرولی درالجماهر (صس*‪ )۹۲‬ازقول ناخدای کشتی‌آرد ‪:‬‬
  ‫‪+‬بوتهافی‌الروزنادج باسمه » (نام «صلةٌ سرب را باسم شیخی که بطلب حاجتی نزد ناخدا آمده‬
                                                                                    ‫کت‬
   ‫مه روزنامجه در قرنهای اواسلامی مستعه‌ل بوده امت‬         ‫بود وی‌در روزنامةٌ خود بادداشتکرد)‬
  ‫(اپ دمشق ج ‪۲‬ص *‪ )۱-۱۱‬کوید‪« :‬مااخرج‌م نکتاب الروزنامجةلاساحب‬     ‫تعالبی در بتیمةالدهر چ‬
   ‫(ابن‌عباد) الی ابن‌العمید ممایتملق بملح اخبارالمهلبی» ونیزدرجای دیگر شرحی اکزتاب روزنامجة‬
  ‫صاحب‌ین عباد ميآورد باين عنوان‪«.:‬فصل کمتناب‌الروزنامجة ایضا» وباقوت حموی درممجم‌الادیاو‬
  ‫(جاپ مکالریوث جه ‪4‬ص‪ ) ۰4‬دیز شرحی از ک«تاب الروزناءجة لابی القسم اسمعیل بن‌عبلد >‬
   ‫آورده است » وازهمةٌ ابنهاصر بحامعلوم میشود کهروزنامه درآن اوفات بمعنی کتاب شرح کزارش‬
    ‫هکنون بزبان فرانه‪ [20۳110‬میگوینده بوده ‪ .‬ایسنطلاح‬    ‫روژانه وبادداشتت وقایعهرروزه ک ا‬
  ‫ظاهرا بعدها درابران بهمین معثی باقی مالده ودر قردهای اخیربمعنی «راپورت» های وقابم‌نگاران‬
   ‫دولتی که ازولابات اخبار جاربه را بدولت می‌نوشتند وبمعتی مطبوعات بومیه وهفتگی اطلاق شد‬
  ‫‪ 2‬مجله‌کاوه‪ .‬دور دوم" شمارءٌ ‪٩:‬‏ روزنامه نگاری درایران بقلمآ قای تقی زاده» و رك ‪:‬ەى فواید‬
   ‫لغوی| لحماهر بقلم نگارنده » دربادنامة بیرولی »کته ‪4)٤ ۳۸۲‬‏ ‪ .‬ورك ‪ :‬دزیج ‪ ۱‬ص ‪.٠۹۹‬۔‏‬

##### LEAF 435
  ‫‪=4‬‬                                                                                                                   ‫روزی افرای‬

‫و« باشندة ده بعنی دهقان را هم‬                    ‫شهر است ‪۷‬‬          ‫روزی اقز ای ‪ -‬نام ماه چهارم باش‬
 ‫کفته‌اند که روستابی باشد ؛ ومعرب آن رستاق‬                                                     ‫اعهای ماکی بزدجردی ‪.‬‬
                                                                                                                  ‫امز‬
 ‫باشد (‪ -)۲‬وجمعیت‌ومجمم مردماترا نیز گوبند‬                          ‫روس = باالیمجپول بررزن‌بون(‪»)۱‬‬
                                                                    ‫نام ولابتی است در جالب شمال‪٩‬‏ ‪ -‬بمعنی رویاه‬
                                                ‫ومپمی دبگر ‪.‬‬        ‫هم‌آمده است ‪ - ۴‬وخرامیدن ‪ -‬وسبقت گرفتن ‪-‬‬
                                                                                                          ‫گوذشتن را گیز‬
                                                                                                  ‫فته اند ‪.‬‬
 ‫‪۸‬ے معروف‌است که رستم زال‬                       ‫رسوتم‬
                                                                    ‫روساختی کنابه از شرمنده شدن‬
                                                                                      ‫وخجالت کشیدن باشد ‪.‬‬
 ‫زده * معرب‬      ‫نقطه دار )‪ (£‬وفوفالی مفتوح بم‬                      ‫روس انگر ده ‪ ۴‬د پنکاف فارسی‪,‬‬
 ‫روسوختها سکته راسخت باشد وآن مس سوخته‬                              ‫روباه تربك است که سگ انکور باشد چه روی‬
 ‫است و بعربی فحاس محرق گوبند ‪ .‬بهترین آن‬                            ‫گویند و دعر ای‬        ‫دالهُ انگوررا‬          ‫دنکن‬        ‫نمعنی‌رویاه‬




                ‫مصری بود‪ .‬گرم است در دویم‪.‬‬                                                                      ‫عذب التملب خوانند ‪.‬‬
 ‫رو سی = بروزن‌طوسی» منوب بولایت‬                                    ‫رسومی؟ د بابای فارسی‌بر وزن‌دوستی؛‬
 ‫روس باشد ‪ -‬وئام پپلوانی است تورالی ‪ -‬ولوعی‬                                               ‫زن فاحشه وبدکاره رگاوند ® ‪.‬‬
 ‫ازپارچه هم‌هست منوب بروی ‪ -‬وال شرابرا‬                               ‫ووستای‪ ,‬باالی مجپول‬
                                                                                       ‫روستاا < ر‬
                                               ‫نز کوند ‪۶۱.۰‬‬         ‫مقابل‬    ‫در‬   ‫را گونن که‬           ‫ده‬   ‫‪۰‬‬   ‫بالف کشده‬       ‫وفوفانی‬




   ‫(‪ )۳‬چك‪ .‬چش ‪ :‬بجپت ‪.‬‬                              ‫(‪ )۲‬چك ‪« ,‬چش‪ :‬است‬                      ‫(‪ )۱‬چك‪,‬چش‪ :‬لوی‪.‬‬
                                                                                      ‫‪.‬‬   ‫خا‬    ‫‪ :‬وسکون‬           ‫(‪)4‬چك‬


   ‫اتی ع‪ ]82551۳7‬دك ‪.‬است ‪ ۷۳۱‬کیلکی ‪ :]50۲‬نام فوم‌ساکن روسیه ‪ .‬بخش‬
   ‫و خانواده‬    ‫وارویابی‬   ‫هند‬           ‫بز رکه تقسیم مشو لد ‪ :‬خانوادة‬        ‫از لحاظط نژاد يدو وة‬                ‫روسه‬    ‫اعظم مات‬


   ‫‪ _۴‬مخفف «رویای» بپلوی ‪ ۰‬رلك‪ :‬رویاه ‪.‬‬                        ‫اورال وآلتائی ‪ .)012۲11-0 607012‬رك‪ :‬روسیه‪.‬‬
   ‫پهلوی‬        ‫‪۴‬‬                   ‫‪.‬‬   ‫انگرده » روتاه تريك‬   ‫‪8‬‬    ‫رس‬   ‫رك‬    ‫انگرده ‪€‬‬         ‫رویای‬   ‫‪°‬‬        ‫مشفف‬     ‫‪۳‬‬


  ‫‪«-‬سه روسبی «چار کس از چار کس بجان‌بر نجند ‪ :‬حرامی از‬                            ‫‪۵‬‬              ‫«اونوالا ‪- ۵۱4۰‬‬               ‫‪61‬‬
    ‫پپ‪-‬لوی‬
         ‫‪۲‬‬                     ‫‪۰.‬‬       ‫«کلتان ‪۵‬‬        ‫سلطان و درد از باصبان وفاسعق از عماز وروسمی ازمحتب؟‪.‬‬

     ‫‪.‬‬   ‫ولز رزداق تفس‬                    ‫پورداود‪ .‬منا!‪4 ۲۲۱ :‬‬          ‫بونکر ه‪٩۰۱‬‏ و معرب آن رستاق‬                             ‫‪(1‬‬
   ‫اوشیروان عادل را درشکار گاه صیدی کداب کردند ولمك شود» غلامی بروستارفت‬                                           ‫‪2‬‬     ‫‪۷‬‬

  ‫(‪e.( .۵‬‏‬     ‫راسخت‬       ‫ت‬             ‫‪۹‬‬
                                              ‫‪۸‬‬          ‫تالمك حاصل کند» « گلتان ‪>٩ ۱4‬‏‪.‬‬
                                                   ‫‪ :‬رستم‪..‬‬   ‫رك‬

                                               ‫ی‬ ‫ز‬ ‫د‬
                                                ‫‪۲ :‬؟‪.‬‬‫«‬ ‫=‪« 6۲۷1۱ 610۳‬لك ‪ ۲‬س ‪۰ ۱۰‬‬
                                                        ‫‪۹‬‬
                                                        ‫‪۹6‬‬    ‫جص‬                      ‫‪0‬‬
   ‫*‪ -‬زیان روسی یکی از زبانهای هند و ارویامی و ازشعب زبانهای اسلاوی است وزبان‬
   ‫‪ ۱‬الفبای‬     ‫‪euqilliryc‬‏‬                  ‫رسمی ملل اتسعاد <ماهس شوروی میباشف _ خط روسی ‪ ۰,‬ازخط کزان‬

##### LEAF 436
                                                                                                                                                    ‫‪1‬‬
                                                                                                                                                ‫‪TEE‬‏‬    ‫سح‬       ‫‪۴‬‬        ‫‪۳‬‬   ‫‪۴‬‬    ‫‪5‬‬
                                                                                                       ‫‪۱‬‬
                                                     ‫‪SSE‬‬     ‫‪5‬‬       ‫=‬           ‫‪3‬‬   ‫‪5‬‬        ‫‪۳۳‬‬           ‫‪۳‬‬   ‫‪gG‬‬       ‫‪aa‬‬         ‫‪77‬‬   ‫‪۷‬‬
                   ‫‪5‬‬
                       ‫=‬        ‫کب‬   ‫ات‬   ‫ها‬   ‫>‬
                                                                                 ‫‪۱‬‬             ‫‪۰ ۰‬‬                                      ‫‪۰14‬نی‬   ‫‪5‬‬            ‫‪۰‬‬       ‫‪۹۳‬‬           ‫‪--‬‬
                  ‫صدای <ر وف |‬                 ‫ا‬     ‫‪E‬‏‬          ‫‪۷‬‬       ‫‪2‬‬               ‫‪3‬‬     ‫‪2‬‬                    ‫ل‬        ‫کب‬          ‫‪1‬‬      ‫ی‬        ‫‪9 ۰‬‬
‫برایر صفحة ‪4۷٩‬‏‬




                            ‫‪۱‬‬                      ‫هن سا جچ چ‬                                ‫مه ‪5‬‬                   ‫‪۲‬‬             ‫‪۶‬‬         ‫‪۶ 5‬‬              ‫‪3‬‬                             ‫‪2‬‬
                           ‫دا‬        ‫اده‬
                            ‫‪۱‬‬                  ‫‪5‬‏ ‪ ٩ $‬مب ق هی ‪٩5‬‏ ‪ 8‬تب ب م ه بر ‪ ۲‬و‬
                            ‫‪۱‬‬                                                ‫‪A‬‬                                           ‫‪ES‬‬                             ‫‪۳2‬‬
                                                                     ‫ما‬                                             ‫که کر رو چا ‪nN‬‏‬                                               ‫و‬            ‫‪FF‬‬   ‫‪2‬‏‬
                                               ‫‪u‬‬    ‫‪۱‬‬      ‫‪‎‬کت‬               ‫‪۰‬‬           ‫‪xX‬‬        ‫‪u‬‬            ‫‪3‬‬            ‫‪‎‬هه‬        ‫‪8‬‬               ‫‪31‬‬                    ‫&‬        ‫‪6‬‬
                                ‫‪EST‬‬
‫الفبای روسی‬                                    ‫مر‬                            ‫‪۱‬‬               ‫اد‬                                   ‫‪TTT‬‬                        ‫‏‪ITI‬‬
                                               ‫‪ ۲ 2 2 ۵ NS‬ک ‪ 5‬و گ ه > ‪ ۵ ۰۲‬هه‪» ‎‬‬                                                                                                                    ‫‪a‬‬

##### LEAF 437
            TL       LNLL
            EDIE 7777 SLL
                 ‎       ‫ر‬     IDL
                          IL۳ 7‫ک‬       E LDL
                                7 DID DLTI DD DSLL LS DD
                                                    LL BL, LL
                      SC        A    ATL                                              2
                           ‫ت‬‎   LS   MAE   ۸     1          >   ۳
            ۱   DLL
                                                                                          ‫رم‬   27 ‫رر‬
                                                                               2 ‫رم‬   ‫مد‬        , :        ۵   .
                                      ۱        ‫ له‬‎‫مق‬   1            ۱ ‫ط‬
                                                                    ‫رم‬     ۴              ES
                                                                                                       1           7
‫برابر ملس‬
‫‏‬۵۷٩

##### LEAF 438
‫روسه‬                                           ‫‪۱‬‬                                   ‫زا‬   ‫ی‬

                                                                        ‫بقبه از صفحٌ ‪4۷٩‬‏‬
‫وسیم نرارها اطلاق ميشد‪ .‬وآن در اروپا وآسیا از سواحل دربای بالتيك تاسواحل اقیالوی کبیر‬
 ‫ممتد بودوامروزه بجمهوری سوسیالیستی شوروی روس که قمت عمد اتحادبةٌ جماهیرسوسیالستی‬
 ‫شوروی‌را سکیل مبدهد()‪ ))/)/‬اطلاق‌شود وآن‌بمساحت ‪ ۰۰۸۷۹۰۷۹۱‬کیلومتر مرست و‪۳۱۱‬‬
‫و ‪100٥80‬‏ است وشهر های‌عمده‌عبار تنداز‪ :‬لنیتگر ا‪۳‬د‪ 48‬صن‪ 1‬عا‬ ‫آن‬‫متک‬ ‫ملیونسکنه‌داردوباشخ‬
‫رستف ‪ .۸ ۷050‬گر کی ‪ 161۲026۰‬اسوردلوسك ‪ .5۷0۱0۲6۷5‬ساراتف‪ ۷008۲3۹‬روسبه‌ارویا‬
‫هموار و دربعض مواضع دارای درباچه‌ها وباتلاق‌ها ودربرخی امکنه پوشیده از جنگلهاست و در‬
‫جتوب شرقی از استي‌حا مستور است ‪ .‬جبال عمده عبارتند از‪ :‬ففقاز و اورال [‪272‬ا()‪ .‬تیه های‬
‫والدائی ]‪ 20۱۵۷‬و ولگا ‪ . 281۵۷‬در میان شطها بابد یجورا ‪ 8102006۳‬دوینا ‪» 471۷‬‬
‫دونا ‪ » 2011121‬دون ‪ 01021‬و ولگا را نام برد ‪ .‬روسية آسیا ناحیه ایست که درمقرب پست» در‬
  ‫مشرق وجنوب کوهستانی وتوسط ابی ‪ .100‬بنیسه‌ئی ‪ ,]1655106‬لنا ‪ 2061‬وآعور ‪۲۷0۸‬‬
 ‫مشروب میشود ودارای درباچه‌های بزر که ‪ :‬ارال ‪ 12۲۸۰‬بالکای ‪ , 06261۵‬بایکال ‪lakiaB‬‏‬
 ‫است ‪ .‬روسیه اصللا کشوری است زراعتی ودارای منابم فراوان معدنی از قبیل‪ :‬لفت ‪,‬زغال سنك»‬
‫آهن ‪ .‬طلاء طلای سفید وجزآن‪ .‬ازاواخر قرن لوزدهم نېضت صنعتی قابل توجهی‌در روسیه ابجاد‬
                                               ‫ودرقسمت معادن وساجی پیشرفتی حاصل شف ‪.‬‬
‫بعنی گام هجوم وارکان ‪ -۷ 56118672‬ستولهابی از بژاد‬          ‫تاریخ روسبه درفرن اهم‬
 ‫اسکاندیناو که خوی جنگجوبی خود را باسلاوبان منتقل ساختند‪ .‬آغاز میشود‪ .‬روسیان مذهب‬
 ‫بتوسط مبلفان بیزاسی درزمان‌سلطنت ولادیمیر ‪۲۷۹-۵۱۰۱( ۲10۳11021۷‬م‪).‬‬        ‫را‬
                                                                           ‫ی‌بو‬
                                                                              ‫الینسیم‬
                                                                                    ‫تتو‬
                                                                                      ‫کا‬
‫پذیرفتند ‪ .‬بارسلاو ‪ ۷3150۲81‬برزکه (‪ )۵۱۰۱-4۵۰۱‬بمنزلهٌ شارلمان روسیه بشمارست » ولی‬
 ‫پس ازین پادشاه دور حرج ومرج آغاز جونگهای داخلی شروع کردید ‪ ۰‬وبراثرآ نهاروسیه نحت‬
 ‫تبعیت مفولان درآمد (فرن های ‪ ۲۱‬و ‪ ۳۱‬م‪ ).‬معهفا امرای مکو ومخصوماً ابوان (‪)02۷۲‬‬
 ‫رصرفات خودبیفزایند وسلطنتی مقتدر را در زمان رومانف ها‬‫مخوف موقق شدند که بتدریج بمت‬
 ‫‏‪ - Romanov‬که در ‪ ۳۱۱‬قدرت را دردست کرفتند ‪ -‬بی ریزی کنند‪ .‬مشپورترین تزار ها‬
 ‫بطر (‪ )۵۳۲63۳‬کسر )‪ )۰۵۲۷۱ - ۲۸1۱‬است که برشارل دوازدهم ‪5٥1131 ×11‬‏ غلبه کرد و‬
 ‫‪ ۲110005‬است‪ .‬درفرن‬    ‫‪0‬ر‪6‬ک‪۲‬ه‪8‬‬ ‫او مجدد تمدن مکوی بتقلید ارویابیان و بنیاد گذار ی‪۳‬طرز‬
                             ‫‪6‬بو‬
  ‫هیجدهم‌روسیه تقربباً لابنفطم درجنوب‌باترکان درمحاربه‌بوداما درزمان‌کاترین درم[ ‪601۲6‬طاه)‬
 ‫شتی تقیم لهنان (پی ازآن دوبار دیگر مقاسمه بعمل آمد) وفتحآزف‪ ۷02۸‬اجام گرفت‪.‬‬
 ‫رتد اما بمد نایلئون‬
                   ‫کک‬ ‫یل اول‪ ) ۹۹۷۲۱-۱۰۸۱( 112۳ 1‬روسیه در انحادیة ذد فرانه شر‬
  ‫بروسیه حمله برد »ولی سرعا داپلئون را ار روسه خارج کرد و الکاندراول ‪erdnaxelA 1‬‏‬
 ‫مورد توجه واحترام دول دیگ رکردیدو برباست اتحادبهٌ مقدس بگرزیده شد ‪ .‬ازآن یس تزاران‬
```


## [2026-09-14T01:25:13.195Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"روغن\" BQT_v2_pages.txt | head -20; echo \"=== leafs ===\"; awk 'BEGIN{RS=\"\\f\"} /روغن/ {print NR}' BQT_v2_pages.txt | head -20; echo \"=== ronas ===\"; awk 'BEGIN{RS=\"\\f\"} /روناس/ {print \"RONAS leaf\",NR}' BQT_v2_pages.txt | head"
}
```


### [2026-09-14T01:25:14.344Z] TOOL RESULT

```
782:         ‫وروغن ک‬                   ‫به ار سین و‬            ‫ازجان بشکرانه دادن و پیشکش نمودن باشد‪.‬‬
1699:‫روغن باشد ‪ -‬و بضم اول و فتح‌ثانی مشددآستین‬             ‫ارر‬  ‫نوزد]خ‬
2072:‫آن روغن ستور همچو روغن اسب و شتر و کاو‬                                 ‫واو را اخار بر وزن بخار کودند ‪.‬‬
2885:            ‫که در آن روغن از حبوبات ش‬                     ‫جو » نم اچولوبی باشد که بوقت‬
3132: ‫و روغن ستور دران آتش میریزند و چیز های‬
4808:                 ‫و روغن و امثال آن‬         ‫چربی‬                               ‫ومعنی چراغ است ‪.‬‬
4940:                                                   ‫وخ‬           ‫وچرب شدن چیزی ازروغن وامثال‬                 ‫نمودن ‪۹‬‬
4989:‫وطرح ونقش گذارند وبا قلم موی صورت و فقش‬                                ‫تنکی رانیز گوند که درمیان روغن بربان کرده‬
5024:                       ‫چربی و روغن ‪:‬‬        ‫و‬        ‫‪۴‬‬                           ‫‪.‬‬            ‫‪۶‬‬    ‫د تاریخ بیهقی مصحح ادیب ص‬
5031:                   ‫بروغن نرم کرد آهن ز پولا‬                                    ‫یشیرین چند چرییا فرستاد‬
5445:                        ‫باشد‪ . ۴‬٭‬                         ‫ویبه بربان کرد روغن گرفته کروایندا ‪.‬‬
6606: ‫باشد و کلافهرا نیز گونند خواه کلافةً رسمان‬                                ‫روغن بربان کرده باشند ‪.‬‬
7170:   ‫وروغن وشیرینی درهم مالیده شده‌باشد ‪ ۸‬و‬        ‫ازکاربازمانده باشد‪ -‬وم‌اول بمعنی‌سخن و گفتار‬
7183:                               ‫س‬                                          ‫که با روغن وشیرینی‬
7317:‫چوب دانه ‪ -‬با دال اب بر وزن‬                     ‫ویکاف زده » نالی‌باید کهآ نرابروغن بربان کنند‬
11758: ‫چپاز) خرة شاپور» پنجم خرة قباد ؛ وباین‌معنی‬        ‫کنفیتزه‌اند ‪ - ۴‬وتفل هرتخمی باشدکهروغن‬
12489:‫است کهپلاو بیروغن باشد ‪ -‬وآرد گندم نايشته‬
14208: ‫نکیفزته اند کوخیوناه (‪ )۱‬تخم مرغ بروغن‬                  ‫اراده گفته مشود چنالکه گویند « خواست خدا‬
15050:                               ‫یاه در ارنوزمی‬                               ‫و عسل باشد ‪.‬‬            ‫و روغن ‪-‬‬     ‫و ماست ‪-‬‬
15626:                                                                 ‫مغات‪.‬‬   ‫‪,‬‬   ‫کنند‬        ‫جزآن‬     ‫و‬   ‫شره‬   ‫‪۰‬‬   ‫روغن‬            ‫‪۰‬‬   ‫آن‬
=== leafs ===
18
33
39
53
57
85
87
88
95
114
124
126
201
213
241
257
265
296
343
360
=== ronas ===
RONAS leaf 154
RONAS leaf 443
```


## [2026-09-14T01:25:25.239Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 439 440 441 442 443 444; do echo \"##### LEAF $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tr -d '‫‬‏‎' | sed 's/  */ /g' | head -45; done"
}
```


### [2026-09-14T01:25:26.251Z] TOOL RESULT

```
##### LEAF 439
 ورف روش
ننی هم هست یمنی روشن کن �- ۴
 ممرعبدی
 وا � = ۱تح اول و کسر �انی روش
 و تندخوی و بدخلق را یز گفته اند�. وسکون شین قطه�دار » بممنی راه رفتن سوبقت
بوزن روشان ؟ � -با �انی م�هول کرفتن� -ود رکذ تن رخرامیدن باشد� -وطرز(�)۱
�وشان � .بمعنی�روشن است که ازروشنابی وفروع و ماد را یز کوند ت �-ل
 م�وئون
 وقامده وقا
 وخیابان وراه رو میان باغ را هم گفته�الد� -وم
 روشی � = ۴باشمول بروکزونکن�, اول و امن�یهول � .مخفف روشن باشد که از
بممنی روشنابی وفروغ باشد � -کونابه از ظاهر روشنابی است�چنانکه گویند �چشم شما روش»�- ۳

 (� )۱چك » چش � ۳:وعادت �.
 رك � :روشن �. �۴ � - ۱از � :رو (رفتن) اش (ینوند اسم مصدر )�..
 � - ۴بپلوی � » 85۵0۲اوستا �( 8110503۲ -صفت بمعنی�روشن) � بارتولمه �� ۸۸4۱
 وعم در اوستا�( 087-8011502۲ 11011156-اسم است�بمعنی روشنابی) �بارتولمه �۹۸8۱6 ۸۸4۱۰
 دیب رک � ۷۹۱۰۰افتانی م � . 18۵05۵۲ ۵22۵۲۰باوچي � 182۸815۵۲۰ . 12/5۵۳شغنی
 (نور روز)� .منکلی�ی �( 120150۲آنش) �اسنق � ۱۳1ورك � :هوبشمان اسا �. �58
 بقیه از صفحة و�٩۷
 ونی و لیتوانی و قسمتی از لهستان را ازدست داد � .بخشهای دیگراعیراطوری مزیور بتبع روسية
 شوروی تشکیل �مهوریهایی متحد باآن دادند�.
 و ژوزفت در گذشت �۶۲۹۱ لن در

 استالن �6811٩ � .5.٥�اشن اکوردید �.
 در � ۰ ۹۳۹۱شوروبان � ,بخش شرفی
 لهستان و در � ۰6۹۱قمتی از فتلادد ؛ رومالی
 و �مهوری های باتىك را بتصرف آوردلد �.
 مورد حملهةٌ �ماهیر شوروی در �۲۸ - ۱۸۹۱
 آلمانیان قرار کرفت و در �ه د�رنگه
 بین المللی دوم وارد گردید و عاقبت تواست
 کلیة سرزمین های خود راکه بدستآ لمالیان
 بود خارح کند و سپاهیان وی اشفال شده
 وارد برلن گردیدند و �نک خانمه پذیرفت
 (� .)۳۹۱-۵4در� ۵4۹۱وی�درغلبه وفتح�متفقین
 �: �۳یر�۳ص�۵
 برژاین شر کت کرد � ( .رك � :برا
 لنین(سمت چپ�تصوس) واستالین(سمت راست تصوسی) بیرقها )�.
 اناد �ماهیر شوروی شامل روسيةٌ شوروی � ۰اکورالی � ۰ببلوروسی �, 6155181-0161
 رنستان » ازبکستان » تا�بکستان� ,قراقتان »
 ئم
 �۰ر�تان (� ,)۹4۹۱ ۷ک ارمنستان� ],ذرباب�ان �
 وستولی
 قرقزستان است و از� ۰۸4۹۱بدین �مهوری�ها � ۰�مهوری�های ملداری » لیتوالی � ۰لتونی ا
 افزوده شده� .مساحت م�موع ممالك اتحاد �ماهیر شوروی � ۰۰۲4۷۲۱۲کیلومتر مربع�و �معیت
##### LEAF 440
 روعن کشت �۱۷


 ومعلوم وبين هم هت �.
وفتح �ال� ونون وکاف سا کن � ۰ام دخترداراست
 روشناس � .کنابه از شخصی مشهور
 وعروف و آشنای همه کس » و بعضی گوبند
 م
دارا او را بعقد ناح وصست سکندریمو�ب که


خود دآرورد � -و نام داروبی است مانتد کمای تر�مةٌ و�ه است �.
را روشنك و در دکن مشمل�ی شده �- خشك
 روشناسان ک�-نابه از ستارگان �- ۱
 میگوبند �. ومردمان مشهور ومعروف باشد �.
روضه باع ر فیع�-کنابهاز رباض روشنان فلك � .کنایه از ستار ها
 بپشت است �. باشد �.
روضه تر کیت � -کنابه از قالب است که در معروف �۴ روشنایی
 مردم است که �د آدمی باشد �۰
 مقابل تاریکی باشد � -و نام �وهربت که آبرا
روصه دورخ بار � -کنابه از مرقشیشا کوبند و بعربی <�رالنور خوانند و در
 شمش رآ بدار باشد �۹
 داروهای چشم بکار برند ک�.وبند اگر بگرردن
کنابه فیروده ر نگ ت روصه اطفال بندند از هیچ چیز نترسد �.
 ازآسمان است �. روشن چراع � -بکر�يم فارسی�,
روع = نم اول و سکون انی غوین نام لوابیست از موسیقی �. ۴
وآن بادی باشد است �۵ لقطه�دار � ۰مخفف آروغ
 رشوندان � -باالی م�هول � .منفذ
 ی
 بدر
 رول
 عح ا
 � -بفت
 و مکیلوابد
 که ابز رراه وسوراخی راگویند که در خانها ب�هت روشنابی
 حیلة ررباء�وحیله کردن کسی وینهان�بسوی چیزی مگذار اد � -و تایدان را لکىوزبند � -و معنی
رفتن � -ومیل کردن و گربختن راگونند ویینی روشتی دان هم هست که چراغدان باشد �.
 کوه رانیز گفته�اند �۰
 روشی قیاص د بکرناف� .کنابه از
روغن � -بقتح اول بر وزن کودن » مردم صاحب فراست باشد �.

 �رو�شنان» است و رء�شنان مطاق ستار گان وغالبا �وات را � - ۱بان معنی ظ » مصحف

 � ۹۳از � :روشنا (یهلری (�kãnhsêr �۳ رك� :روشنان فنك �. گورند دگاء شماری ص�۳۳۰

##### LEAF 441
 هی �۷۹۳
 روغنای
 کف واو
 معروف است � ۱و آنرا از دوغ گوسفند ک
روغی هفز � -کنابه ازعقل و تدییر اوم�ال آن م مبیگیرند » و نوعی دینگر همهت
 باشد �.
روغنی � - ۴بفتح اول وغین شطمدار�, و غن سنگه عصاری باشد �. شده غن است �۰


نالی باشد که خمیرآ لراباروغن سرشته باشند؟ �- روغناس = بر وزن و �عتی روی�ای
 وعسار وروغن گر را نگیوزیند �. است � ۰وآن�گیاهی باشدکه چیزها بدان رنگه
»بیان شله�دار ونون بر کنند �. ۴
 روغنینه * غ
 هیرآنرا
 کموزن هرشبینه » نرانایکوبند �٣ خ روغن بریگ ربختن � -کنابه
پهن کرده در روغن بفیدز(�)۱؛ بستی گوبند نان ازکار و مهم فرمودن بمردم بی ماحصل ر مهمل
کرمی است که بر آن روغن رز ند ودیگری را وضایم باشد �۰
بر بالای آن گذارندوهم�نین تاچندانکه باشد�.
 روغی خود د بکر نون ک�.نانه
سمرقند بافا » بزیان سغدی �- روف است از مذهب ودین خود �.
است تآخنمی
 و را
 ویند گ قرط(و�)۲
 نا بز روعن خوش » بکرلرن وض�خای
 معروف �۷# .
 �درا گوبند کهروغن شیرپخت
 نقطمدار� .رکونغن
فا کر
 � - ۲بسن اول و باشف � .سموم را نافع است �.
 روفس
 وسکون سین � ۰نحاکمیمی است بونالی �. کزسی است
 کتابه ا روغن رفته د
رگواه � -باکان�فارسی� ,کنابه ازدبباچة سدیولرتشده باشد�. .
 و ر
 کعهماز
کتاب است� -و دست بالای �امه را لز گویند
 روغی زان � -بسکون بون و قح
و پیشوای قوم(� )۳و پیشوای میت را گفته�اند �. دار > کنابه از نرم گرفتار و چایلوی رای فطه


 فتح اول و کاف بورزن رو کش وئیتالی وفرب دهنده باشد �.
مهوش» بمعتی دهر باشد که دیا وعالم است�- ۸ را بلان � -ررغن روعن مصری

 (� )۳خم� -:۱وپیشوای قوم �۰ (� )۲چش � :بنر �. � :بر لد �. (� )۱چك �٠ چش

##### LEAF 442
 �۷


 �شم امتت� .ء همچو باطنش رآن
 ایهکه
 ظر چ
 و نم اول ه
 رومی خوی کی ر�اوندکه لباشد �.

دورنگه ومتلون مزا،باشد وبهر کهرسد برنگه روم = نم اول وئالی م�هول بر وزن
 وخوی اوشود �. موم » موی زهار باشد � - ۱و با �انی معروف
رومی رن رعنا د کنابه ازآفتاب ملکی است مشهور بحدود شام� - ۴ومخفف رویم
 عالم تاب است �. هم هت یمنی روی هن � -وبفتح اول نام درختی
روهینا � -بروزن بوسیناه بمعنی زدوده نت » و بعضی گویند آکیرل م
 م مق
 �ت که
 اس
 همع آن درخت ا
 است که از ياك کردن وزدودن باش�د �.

 رومی ود نگی �کنابه از روزوشب روملوس � ۴با لامر�-ین بی�نقطه(�)۱
 بر وزن عود سوز � ۰نام شهریست از فرنگه بنام
 بانی آن که پر لمرود باشد * و او نمرود رادر
= بمعتی رومی رومی و هی زمان حکومت خود خادم ساخته بودوالت تناسل
و زنگی است ککنهایه از روز وشب ولیل ونهار
 او را فرمود بربدند ونمرود اگزوریخت و اوعد
 داش� �.
 از کربختن لمرود آن شهر را بناکرد �.
یه � 5حم اول بروزن بومیه(�»)۳ رمزو
 � -ضم اول و �انی م�هول روهنا �۴
نام شهر مت که انوشیروان )�(٤ بکرنار دربای
 وفتح�میم ونون بالف کشیده بلغت زند ویازهد(�)۲
روم بنمونهةًآ نطاکیهبنااکرده بود گ�.وبند ازآن
 انار را گوبند و بعربی رمان خوانند �.
 شهر تفاسطنطنه بك سال راه است�.

رون ه بفتح اول بروزن چمن� ,امتحان رومه * � -بم اول و فتحمیم � ۰موی
 گاوشد » وموی زهار را نگیفزته�اند �.
 اندام ر
و آزمایش رگوانند � -و بضم اول و�الی معروف
�۰نی سیب و باع� باشد چنانکه
 معبروزن دبون رومی بچگان � -کنایه از انك
 (� )۳چك �,چش� :بومیه�. (� )۷چك� :ژند ویاژند �.
 چش� :نوشروان�. )� (£چك

##### LEAF 443
 �AA رواس�

 فته اند که
 �مکوبند �رون�آن» بمنی سبب آن وباع� آن �١ | عسیب خوانند؟ ؛ و بکر اول ه
 بروزن شکن� و با �الی م�هول� .نام قصه�ایست درهندوستان که

 ر
تو�و � - ۴بفتح اول وضم�یمبر مولد ابوالفرح ب(ود�. )۱
وزن سمن بو » کرمی باشد چوب خوار و بعربی �۱ �. ر
 نواس؟
 ارضه گویتدش �. بضم اول وئالی م�هول


سیاره باشد که زحل و مشتری ومریخ و آفتاب رز ورسین بی لقطةٌ زده �.
 وزهره وعطارد وماه است �. د� �(�7 کیاهی�است�معروف که
 رو نما � -و روی�لها ک�.نابه از (�)۳ بدان �امه و ابریشم
 هد به وتحفه�است که در وقت دیدن روی عروی رولای وام�ال آن )� (+رگ

 وتك کل و �دباکرام» کنند و بعربی فوه
 دوه � -بروزن کوه � .نکام
 وهی است در عوروق�الحمر خوانند �.
 رو ن� = پفتح اول وانی وسکون نون |توابع کابل � -وبمعنی سیرت ليك و پارسایی (�)4
 �. است �۵ از این وروهبان م رکب » هم هت ا ا و


 بر وزن بفتح نالك روهنده د کوشت و برن� ومصالح یکررده باشند و بعربی

 �2 از چش�: (م) چك چس �-:وام�ال آن�. چك )�(۲ �:بوده�. دش )� (۱چك

 (� )4چش� :بارسای �.
 (رف� .�ہت» سمت) � .از � ,# 2۷۸2۲-از اوستا �( 12۷2۲-رود �.
 �-هلوی � ۳۵۲ط
 ب
 درون هر باشد� .عضصر ی( بلخی ) گفت �: رکه �۷ �êb
 حربان ِ قی� :برون �nêr _
 ب�س آندرم �نش ابزون<سون� .دهشدا اتت�». مچشم اندرم دیده( دید� .د�خدا) از رون تت

 فت فری �۲۹۳
 � = ۴روینای روغنای = روین � ۰وخی �, , 881۳۱سکرلی � ,2۳2 760از اوستات
 هانتلل�( 108۲سرخ رنکه) [رك� :روی ] �اسشق � 4۳۱سیوندی �( 65201۲روتنای) �هوبشمان
 � 4۶رونای�819لا� ]0از تیر روناسیان �e شه بشیر پ�یر» ولی بگرهای آن درشت�تر است
 واز رشة�آن ماد قرمز رنگی بنام � 60۳3182112بدست میااید که در رنگرزی پکاږ میرود وقبل
 ازتپی�رنگهای یلین اکبنیاه رابمقدار بسیاربرای استفاده رنکه�آن میکاشتند� � .کل کلاب �.»۹۵۲
 = ربون�ه (ه�.م� ).ورك� :زون� �. رور
 �= ۴ رك � :�کگرآکند �. �۴
##### LEAF 444
 رورشنه ��~A

 �و بنده� .کشت وزراعت پزرور و بالیده را
 روا � ۳وعزهبنر�بوبا(� .)4بمعني�روینده
 باشد بعنی هرچیز که آززمین بروبد (� - )0ودر
 �۳ دبدترا گویند �۸ عر هی خواب وکر �ال� ونون بتحتالی رسیده � ۰آهن وپولاد
بنك = یمعای رو بنداست کهآ نرا دوی

 روهینا = بائالی�م�هول بروزن موستنا»
 روی پوش � -بمعنی روپوش است بمعنی روهنی است که�آهن وفولاد �وهردار باشد


 کونایه اکزی چویزی که ظاهر وباطنش یکی روهینابی(� - )۷وشمشر �را قیمتی را نیز
 نباشد �. کفتماند� .وروهینیا بدو بای حطی هم بنظرآمده
 روی خاندان د یکرنات �,کنابه است�. .
 از بپترین و اشرف ودودمان و خالدان باشد �.
 رو هینی نز = عم اول وسکون انی
 روی دل نمودن� -کنابه ازمردمی م�هول و�ال� و خامی هر دو بتحتالی ر�-یدهه
 باشف �۰ کردن و گرمی واحسان
 بمعنی روهیناست (� )۳که آهن وفولاد �وهردار
 دوی دیدن �-کنایه از طرفگیری باشد � -و آلچه از آن ساز ند �.

 دوق = �م اول وسکون�نانی ونحتالی
 باشد �۰ و وحافب



 دو از » بفتح اول بروزن تمیز� .بمعنی بمعئی رو ورخساراست که بعربی و�ه گونند؟ �-
 طن |ی وامید� -وتفص وتصس ویمعنی رباوساختگی
 »راد آن باشدکه ظغناب�چنین است است م لمودن وپیدا کردن � - ۴وسبب وباع� هم آمده
 نقطه دار بقتح اول وشن بشند؟�� ۹ رو
 هیول � ۰یفکیلاززات �ان
 است © � -ومبا

 (� )۳چك » چس (� )۲چك� .چش � :روهنائی �. �:وهنی �.
 (�۱اچك� .چش ر
 (� )۵چك � ۰چش � :رود �. (� )۶چك» چش �:کودا �. روهناست

 رو
 �= ۴ � ۰روهیتا�. تی
 ه�:رورك
 �۴ � -رك� :روهیتا » روهیتی �.
 � .بهلوی�rêd (مخفف) � .اوستا �( 2002۲-بالش ولمو� .منظر� .صورت) ب�ارتولمه �» ۵۹۸۱
 �اسشق � ۰۳۱ورك� :مشتها � .۲پور داود ی��۹۳۱؛ کیلکی وفریز دی �� ۵۲ك� .اص � .»۸۸۲رك� :رو�.
```


## [2026-09-14T01:25:51.652Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==443' BQT_v2_pages.txt | grep -n \"اوستا\\|هلوی\\|هوبشمان\\|رون\" | cat -A | sed 's/\\$$//' | head -5 > /dev/null; awk 'BEGIN{RS=\"\\f\"} NR==443' BQT_v2_pages.txt | tail -12"
}
```


### [2026-09-14T01:25:52.824Z] TOOL RESULT

```
             ‫= ربونجه (ه‪.‬م‪ ).‬ورك‪ :‬زونج ‪.‬‬        ‫رور‬
                                                  ‫‪= ۴‬‬                  ‫رك ‪ :‬جکگرآکند ‪.‬‬           ‫‪۴‬‬
                                                                       ‫رك ‪ :‬راهب » ره(‪)۱‬‬        ‫‏‪e‬‬

                                                                                         ‫بقیه از صفحهٌ ‪۹۷٩‬‏‬
      ‫وعلمی‌رومیان‌است‪ ...‬رك‪:‬معجم البلدان‪.‬م لف‌حدود العالم (اندرناحیت‌روم وناحیتهاوشهرهای‌وی) آرد‪:‬‬
      ‫«رومیه‪.‬شهرست برکران این‌در‪:‬ا(دربای‌روم) نهاده‌ازافرنجه ومستقرملوگروم اندرفدیم اندرین‌رومبه‬
      ‫بودی» «حدود العالم ‪ . 5۰۱۰‬اما شهر رومیه‌ای کد درمتن بانوشروان نبت داده شده وباقوت نیز‬
      ‫بدان اشاره کرده همان شهر رومگان ‪( ۸8 1418400‬شهر رومان [بونانیان]) است که نام‌رسمی‬
      ‫آن ‪ ( ۵6۷ _ ۲0۱/0۸ - 8۳81162‬شهر خرو بهتر از الطا کبه ) بود واین‌شپر را خرو اول‬
       ‫افوشروان بنا کرده‌بود ومحتمللا یکیازشهرهای مداین‌بشمار میرفته‪ .‬ک«رستنن‪.‬سامان‪۹۸۳‬سعد»‪.‬‬
```


## [2026-09-14T01:25:59.841Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==443' BQT_v2_pages.txt | grep -n \"روین\\|سرخ\\|هوبشمان\\|رونای\" "
}
```


### [2026-09-14T01:26:00.876Z] TOOL RESULT

```
39:      ‫‪ = ۴‬روینای روغنای = روین ‪ ۰‬وخی ‪, , 881۳۱‬سکرلی ‪ ,2۳2 760‬از اوستات‬
40:      ‫هانتلل‪( 108۲‬سرخ رنکه) [رك‪ :‬روی ] «اسشق ‪ 4۳۱‬سیوندی ‪( 65201۲‬روتنای) «هوبشمان‬
41:      ‫‪ 4۶‬رونای‪819‬لا‪ ]0‬از تیر روناسیان ‪e‬‏ شه بشیر پثیر» ولی بگرهای آن درشت‌تر است‬
```


## [2026-09-14T01:26:14.879Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 444 445 446; do echo \"##### LEAF $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tail -22; done"
}
```


### [2026-09-14T01:26:15.936Z] TOOL RESULT

```
##### LEAF 444
  ‫‪ .‬بهلوی‪rêd ‎‬‬            ‫(مخفف) ‪ .‬اوستا ‪( 2002۲-‬بالش ولمو‪ .‬منظر‪ .‬صورت) ب«ارتولمه ‪» ۵۹۸۱‬‬
   ‫«اسشق ‪ ۰۳۱‬ورك‪ :‬مشتها ‪ .۲‬پور داود ی‌‪۹۳۱‬؛ کیلکی وفریز دی ‪« ۵۲‬ك‪ .‬اص ‪ .»۸۸۲‬رك‪ :‬رو‪.‬‬

  ‫وجه ‪.‬طریق‪« :‬چنانك کویم دروع زشتست وستم لبایدکردن با بر روی‪.‬‬                          ‫ملعیزنی‬
                                                                                             ‫ب‪-‬‬‫‪۴‬‬
                                                      ‫‪ 4‬و؟‪.‬‬                              ‫‏‪E‬‬
                                                               ‫سیستر باد کرده بده « دالشنامه‬

   ‫‪ - ۱‬از اوا ‪( 2411002۲ -‬سرخ رنکه) «بارتولمه ‪۵۹4۱‬‬                                  ‫‪ -‬رك‪ :‬رون ‪.‬‬



            ‫‪.‬‬    ‫‪e‬‏‬       ‫رك‪ :‬هوشمان‬       ‫) بر نج (‬     ‫ارمنی غ ‪rIora‬‏‬    ‫مس) ‪ ۰‬بلوچی ‪dêr‬‏ ی اسشق “<‪o‬‏‬


 ‫‪ - ۸‬رؤا بروزن بشری آن‬                               ‫(رو سدن) ‪( ۱ +‬صفت مشموه) ‪:‬‬       ‫‪:‬وی‬
                                                                                        ‫‪ -‬از ر‬
   ‫‪hsêav)a(1T‬‏‬
             ‫‏‪- ٩‬هز‪30. ,‬‬                         ‫چیزبست که دیده‌ای تواورا در خواب کردن» «شرح فاموس؟‪.‬‬

                ‫”سر“ آست ‪.‬‬         ‫ويسر“ درمتن تصحیف‬           ‫‪ ۰‬پپلری ‪ ۲25۰‬سر «یونکر ‪4۰۱‬‬       ‫‪2200121۵1‬‬

##### LEAF 445
                                                                 ‫‪ = ۱‬روشاس = روغنایں ر‬
                  ‫‪۰‬‬   ‫کردش قط از آب روین‬        ‫زده‬               ‫‪ -‬یکی یله است این‌منیر مجره‬           ‫‪۳‬‬


  ‫د منوچهری دامثانی ‪۷۵٩‬‏ ‪.‬‬
  ‫از ‪ :‬روی ‪ ۳‬ین ( نبت ) ‪ .‬بهلوی ‪ ( 9۵8۵۲‬از روی ساخته ) « اوئوالا ‪» 6۱۸‬‬                                  ‫‪۴‬‬
            ‫‪ - ۴‬مراد «روبین دژ» است رك‪ :‬رویین دز‪.‬‬                          ‫“‪eoF‬‏ رلك ‪ :‬روی‪.‬‬     ‫اق‬          ‫و ‪01۷5۳‬‬

 ‫اندر آعد» صدمتی که اکر کوه روین بودی‬                      ‫® ‪ -‬هپس (کشتی گبر ) چون پیل مت‬

  ‫رك ‪ :‬روینه‬           ‫‪۲‬‬          ‫‪ :‬رویینه تن ‪.‬‬       ‫رك‬    ‫‪۱‬‬              ‫ازجای بکرندی» «گلتان ‪. * ۰۵‬‬
  ‫دز بستل‪.. .‬‬    ‫و روسن‬    ‫اسفند بار رقت‬    ‫د‬         ‫‪۹‬‬          ‫روربكی‪:‬ته دژ‪.‬‬
                                                                             ‫‪۸‬‬                   ‫خرمی»نه خم‪.‬‬
                 ‫و غنیمتها بسیار آورد چنانکه قسهٌ آن معروف است‪ « » .‬فارسنامة ابن‌البلخی ‪۱۵٩‬‏ ‪.‬‬
                                                                              ‫رك ‪ :‬روبين ٿن ن‬        ‫‪°‬‬


                ‫* روید ن ‪ -‬بضم اول وفتح پنجم» ‪ ۳‬رستن (ه‪.‬م‪ ).‬؛ نمو کردن » بالیدن‪:‬‬
                ‫که دانه ‪Hl‬‏ یفشانی تر و دد ‪۱‬‬                           ‫بزر کی پایدت بخشند کی کن‬
  ‫«دکلتان ‪۱4٩‬‏ ‪.‬‬
  ‫(برهای قاطع‪)۸۴۱‬‬

##### LEAF 446
         ‫‪.‬‬     ‫‪:‬د‬
                ‫ار‬‫ب)بچش‬
                      ‫(‪۳‬‬                     ‫(‪ )۲‬جك " چش ‪ :‬صلمم ‪.‬‬                ‫‪.‬‬    ‫ئشی‪:‬نه‬
                                                                                           ‫وچ‬‫(ر‪)۱‬‬
                         ‫‪ ¬ ۴‬رك ‪ :‬روین دز ‪.‬‬                        ‫‏‪ - ٩‬رك ‪ :‬روبین خم ؛ رینه خم ‪۲‬‬
  ‫رحام‬       ‫درشاهنامه‬   ‫‪-‬‬     ‫‪۵‬‬             ‫‪ - ۴‬رك ‪ :‬راهب؛ ورهبان ‪.‬‬                     ‫رك ‪ :‬راه ‪.‬‬      ‫‪۴‬‬
                                                                                                ‫آعده ‪:‬‬   ‫پتشدید دوم‬


                 ‫که با بارمان او لبرد آزمود ‪.‬‬                            ‫به پنجم چو رهام کودرز بود‬
   ‫همیشه‌است‬       ‫اول‪ .‬باران‌ست‬         ‫یک‬     ‫ارهمه‬     ‫‪۹‬‬          ‫‪.‬‬    ‫رك ‪ :‬شاهنامه بخ ج ه ص ‪۷۳۲۱-۸۳‬‬
                         ‫وجمم‌ان رهم بر وزن عنب و رهام بروزن جبال میا بد ‪ * ۴‬شرح قاموس > ‪.‬‬
                                                                                 ‫‪۰‬‬   ‫رك ‪ ۰‬اه وود‬         ‫‪۷‬‬


  ‫چ ر ها ‪ -‬بفتح اول» از ‪ :‬ره (رهیدن) ‪( ۱ +۳‬صفت مشبهه) [رك ‪ :‬رهیدن ‪ .‬رستن ] ؛‬
   ‫آهنگه خدمتش‬           ‫‪« :‬‬       ‫‪,‬گذاشتن‬   ‫» بله کردن‬   ‫رها کردن » اجازه دادن‬      ‫‪-‬‬    ‫شده‬   ‫و خلاص‬       ‫آزاد شده‬


                                   ‫(کی از بزرکان ) کردم » درالم رهانکرد وجفاکرد ‪ ».‬ک«لستان ‪.> ۹۳‬‬
                                                                                               ‫ی‬
```


## [2026-09-14T01:26:31.758Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 440 441; do echo \"##### LEAF $n tail\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tail -20; done"
}
```


### [2026-09-14T01:26:33.206Z] TOOL RESULT

```
##### LEAF 440 tail

      ‫‪ ۹۳‬از ‪ :‬روشنا (یهلری (‪kãnhsêr‬‏‬      ‫‪۳‬‬          ‫رك‪ :‬روشنان فنك ‪.‬‬      ‫گورند دگاء شماری ص‪۳۳۰‬‬

  ‫‪ ۵ ۹۱‬؟‪.‬‬      ‫ح‪۱‬‬    ‫*روشنایا» دزی‬   ‫ممرب‌آن‬    ‫روشن)‬   ‫(رك‪:‬‬   ‫‪hînahsör‬‏‬   ‫بهلوی‬   ‫مصدر)‪:‬‬   ‫ی(حاصل‬   ‫‪+‬‬


           ‫نوبتی روشن چراغ ونوبتی کاویزنه ‪۰‬‬              ‫‪ - ۴‬نوبتی پالیز بان ولوبتی سروسهی‬
  ‫‪.‬‬     ‫دامفانی ‪۹‬‬    ‫*عمسوچجهری‬

  ‫‪ - ۴‬درفهرستتاه‌نامة ولف‌روشنك ‪ 8202115۵ ۰ 12025۵۸‬آمده و در بونانی‬
  ‫رکانه ‪ 0041۵31‬بوستی‌درتامنامةٌ ابرا آنرا ‪)kenahsuR( 2022۲5۵‬‏ آررده ‪.‬ازاوستا‬
 ‫‏_‪( Raoxshna‬رل‪ :‬روشن) بای دانت که دختردارا (داربوش سوم) که زن اسکندرشد استاتیر ا‬
  ‫(تاب ‪ ۷‬فصل ‪ ۷‬بند») تاماورا برسین ‪enisraB‬‏ لوشته واسکتدر‬
                                                        ‫‏‪ Statira‬نام داشت و آریان ک‬
  ‫بار دوم که بشوش آمد (‪ ۵۲۳‬ق ‪.‬م‪ ).‬با او ازدواح کرد «ابران باستان ج ‪ ۲‬ص‪۱٤٤۹‬‏ و‪۰ ۳۸۸۱‬‬
  ‫از لجیای مغد بود که اسکندر‬              ‫اما رکانه‪ .‬زن جنگ اسکندر ؛ دختر اکسیارتس ‪5‬‬
 ‫در سفر سغد » بیش از مافرت جنگی بهند بازدواح خود درآ ورد و همین نام است که درادبیات ما‬
      ‫به «روشنث» تبدبل شده واورا دختر دارا (داربوش سوم) بنداشته‌اند ‪ .‬رك ‪ :‬ابران باستان ج ‪۲‬ص‬
                                              ‫® _ رك ‪ :‬آروغ مرغ ‪.‬‬            ‫‪ ۹۳ -‬و ‪. ۳۸۸۱‬‬           ‫‪۹‬‬

##### LEAF 441 tail

  ‫(‪ )۳‬خم‪ -:۱‬وپیشوای قوم ‪۰‬‬                    ‫(‪ )۲‬چش ‪ :‬بنر ‪.‬‬            ‫‪ :‬بر لد ‪.‬‬    ‫(‪ )۱‬چك ‪٠‬‏ چش‬

      ‫‪ ۱‬پپلوی ‪« 2۷۵6۲‬تاوادیا ‪ . 0۵۵۲ 4۱:۷‬اوستا ‪« 2101802۲ -‬بارتولمه‪»۸۸4۱‬‬
      ‫‪۲‬ز‪. ۳3803‬کردی ‪ . 2۵۲‬بلوچی ‪ ۲28۵۲‬و ‪ ۲18۵۲‬و ‪020۵۵۲‬‬       ‫ورك ‪ :‬تریبکه ‪۷۹۱‬؛ با‬
  ‫‏‪,hi‬وخی ع ‪hr‘ 08۲‬‏ م‪۲‬نج‪0‬ی‪ .210۵‬سنگلیچیت‪ »8۵۲‬سربکلی ‪« 00141‬اسشق‬
                                                              ‫‪۵۲‬‬
  ‫[دان]‬
      ‫‪« -۴‬روین» روغنای بودکه ب‬        ‫‪ ۲‬؛ ماد چربی که از شیر با بعض تباتات گیرند‪.‬‬
              ‫رنك کنند بوستها وچرمهارا» «لت فرس ‪۶۹۳٩‬‏ ورك ‪ :‬روین » رونای » روینای ‪.‬‬
       ‫‪.‬‬   ‫‪€:‬‬         ‫(سبت) ‪ ۰‬بهلوی ‪kînhgor‬‏ ‪« ,kînvêr‬یاوادیا ‪۶‬‬              ‫از روغن ی‬           ‫‪۳‬‬
  ‫‪.‬‬    ‫روعنی‬    ‫رك‪:‬‬     ‫‪۹‬‬
                                    ‫© _ از‪ :‬روغن ‪ ۳‬بنه (نسبت)‪.‬‬                ‫‪ - ۴‬رك‪ :‬روغنینه ‪.‬‬
     ‫‪ 0۱1] - ۲‬ازمردم اف ‪ 50562۳۳‬عالم تشریح وپزشك بونانی که بارمُوی احتمال‬
      ‫درحدود اواخر قرن اول و اوابل قرن دوم میلادی میزسته و از زندکانی او اطلاعی در دست‬
      ‫یت ولی آثار متمدد ازاو موجود امت ‪ .‬در تاربخ الحکمای ققطی چاپ ليك ‪ ۰۲۳۱‬ص ‪۵۸۱‬‬
                            ‫از دساتیر« فرهنك دساتیر ‪.* ۸4۲‬‬        ‫‪۲‬‬          ‫شرحی درباب اوآمده است ‪۰‬‬
  ‫روسدن (هم‪).‬؛ جاروب کردن»‬                   ‫رفتن («‪.‬م‪).‬‬   ‫=‬    ‫‪ #‬روفتی ‪ -‬بضم اول وفتح چهارم‬
                                                                             ‫پاكکردن ‪ -‬سودن ومالیدن ‪.‬‬
```


## [2026-09-14T01:26:49.615Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT raoghna / raoidita ===\"; grep -n \"raoγna\\|raoyna\\|raoidita\\|raoiδita\\|raoi.ita\" BRT.txt | head -20"
}
```


### [2026-09-14T01:26:49.687Z] TOOL RESULT

```
=== BRT raoghna / raoidita ===
8330:•  j.  ratu/ris  canmanqmca  pasu.vastra- nqmca  "upajaeäaätnÜä '* "  fraoiritarst n'almät  N-i«?'*.
17512:•  j.  '"upa.raliastnäis  (sd.)  "fraoiritarät' naOnai  H.  58.
20187:•  j.  mazga'vant-  Adj.  (fem.  •vaitl-)  'mit Mark  versehen':  raoynavaiti  °vaili  (VSf.) frazaintivaiti  V,  21. 7.
24832:j  •  j,  raoyna'vant-  Adj.  (fem,  °vaitl)  'der I  Butter  hat':  xh-iptavaiti  •iaiti{\S(.)  mas- \gavaiti  V.  2/.  7.
```


## [2026-09-14T01:26:52.940Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"raoyna-\\|raoyna \\|Butter\" BRT.txt | head -20; echo \"=== raoidita ===\"; grep -n -i \"raoidita\\|raoiOita\\|raoi&ita\\|raoiSita\\|rot,  rötlich\\|rötlich\" BRT.txt | head -20"
}
```


### [2026-09-14T01:26:53.017Z] TOOL RESULT

```
19431:*)  Die  spätere  Theologie  sieht  in  maekainli- und  andern  Wörtern  von  Y.  38. 3  ond  5  siebzehn Namen  bestimmter  Flüssigkeiten ;  vgl.  Bd.  11.  1 : pa  din  haß  lo  sarlak  i  äp  ('17  Arten  Wasser'J giifi  und  deren  Aufzählung  nach  dem  GrBd.  bei DST.  ZA.  /.  265,267.  Bezeichnender  Weite  er- kennt sie  solche  Namen  auch  in  dem  GS.  ahu- rahyä  (Samenllüssigkeit)  und  in  ubcibyä  aiulryä cagimä  (ausgelassene  Butter).  Diese  Deutung ist  wohl  durch  Y.  38.  4;  üilJ  yä  vi  vamikii (näml.n/ö]  ahutS  maxdi*nämqm  (/«^veranlasst fiie  ist  wertlos.
22815:*}  Wie  da»  Bultetordal  angestellt  wurde,  ist nicht  bekannt.  Jedenfalls  mit  heisser  Butter, die  der  im  Gericht  stehende  sei  es  trinken,  sei es  Qber  sich  ausgiessen  lassen  musste.
24830:•  j.  rao^a-  n.  'Butter',  mit  *taramaya- Adj.  'Friihlingäbutter',  Bezeichnung  der Speise  der  Seligen:  i^ari%aiiqm  hi  barg- tqm  (sd.)  *zaramayeAe  "nahe  tal  atti  yünS ..  hudalnahe  ifarüim  pasca  para.iristjm H.  2.18".
24831:Ableit.  —  np.  rir,an  'ausgelassene  Butter'.  — Pü.  (lu  IL):  rSyn;  lu  Aog.  /Ö  wird  umschrie- ben: Sfe»,  malen,  ilrln,  aiif^apfnin.  —  ■)  Vgl. iSt.  Mx.  2.  152,  Dd.  j/.  13  f.,  Av.  10.  $  und IQ  am>r)talät-  No.  3.
24832:j  •  j,  raoyna'vant-  Adj.  (fem,  °vaitl)  'der I  Butter  hat':  xh-iptavaiti  •iaiti{\S(.)  mas- \gavaiti  V.  2/.  7.
24834:•  j.  raDj-nyä-  f.  'Butter':  avi  'yqm  vara- »hiiH  f  sd.)  Yt  /2. 3.
=== raoidita ===
24952:•  j.  raotJita-  Adj.  'rot,  rötlich"':  airyanim vaijö  .  .  äat  ake  paity3r)m  fräk^r^nlal atarS  mainyus  .  .  aiimca  yim  't)in  zyqmca dalv3.däl»m  V.  /.  2.  a)  m.  Name  eines Bergs  oder  Gebirgs'*:  ahmal  haia  garayS fraoxsyqn  .  ,  asthmo  'tS  Ytiff.2.
```


## [2026-09-14T01:26:59.256Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 162 (p.141) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==163' HRN.txt | head -60"
}
```


### [2026-09-14T01:27:00.107Z] TOOL RESULT

```
=== HRN leaf 162 (p.141) ===
— 141 —
634. rönäSj röyenäs, röyen *Krapp, Färberröte*.
wa;^. uruddn, sar. aradSn,
Wohl zu aw. raoidita- 'rötlich' (No. 635).
rönäs ist aus röyenäs (im FJ zweifach belegt)
contrahirt; andere von den Wörterbüchern überlieferte
Formen wie roden, rüdeng, röynäs sind unbelegt.
635. (i)röT, rö 'Kupfer, röyln.
aw. raoidita- 'rötlich* (vd. 1, 3); phlv. rödlk geschr.
rötik (vd. 1 (8)), rod bezw. röi (AV.), royin (AV.) ;
skr. lohä'^) 'rötlich, Roterz, Kupfer.
bei. rod 'Kupfer (325).
636. {i)röT, rö 'Gesicht'.
aw. raoSa- 'Wuchs, Ansehen'; phlv. röd"^), hu]rod(i)s7i
(AV.); got. ludja 'Antlitz'.
Allgemein entlehnt im iranischen Gebiet und über
dasselbe hinaus.
637. reht 'Diener, Sklave'.
phlv. rasik.
Wohl zu ap. \/^raS'j np. resTden (No. 016)?
638. reffen 'ausgiessen, verschütten, Praos. rez-em, rPzis,
ni^TI (Qiss. Dan.), reze, vergl. hirezen \Soiho, Durch-
schlag.
g. retmün, Praes. herlfe; Käs. V. retdti.
aw. l/'ra^d-, ra^cayat *Si\isg\essen ; phlv. re//^/w, ircPt
(päz. rezed), rec(i)sfi; lat. liquäre; ai. [/'rcc,-, rindkil
bedeutet nur überlassen, räumen' (vergl. np. gurc/ten,
No. 914); arm. vergl. IKanem 'verlassen' (H. No. 132).
kurd. 7'etin 'ausgiessen'; oss. d. lejtm, t. iJjjn
'laufen, fliehen' (167) ; bei. reöag, n. rTsay (316), vergl.
princag 'pressen, auspressen' (443); wa/. varic-am,
sar. variiz-am 'müde werden , Causat. Verweilen lassen'.
Hierher gehört auch syr. LW. pnjN, arab. LW.
ihrtq 'Wasserkanne' (de Lagarde, Ges. Abb. 7).
*J SpiegePs Erklärung, Ar. Periode 35, ist lautlich pfanz uu-
niüglich.
2j Fiilaoli oder vielmehr nur graphisch rö/, Bund.
```


## [2026-09-14T01:27:14.724Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rönäs\\|ronas\\|röyenäs\\|Krapp\\|röi \\|röy\\b\\|raoidita\" HUB.txt | head -20"
}
```


### [2026-09-14T01:27:14.778Z] TOOL RESULT

```
5929:Jiingere Kontraktionen sind rOnas *Krapp' aus royanas?
```


## [2026-09-14T01:27:17.373Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /Jiingere  Kontraktionen/ {print \"LEAF\",NR}' HUB.txt; sed -n '5920,5940p' HUB.txt"
}
```


### [2026-09-14T01:27:18.400Z] TOOL RESULT

```
niederen' PPGl. p. 9 Z. 4) aus *ayar (wie im Phi. auch ge-
lesen werden kann) -= zd. adairi, aiardt; bBva *Wittwe' (afgh.
*) daqsXoi und B^^lrjq (sohon bei Herodot) sind speeiell grie-
chische Umformungen der altpersischen Namen Darayava{K)u9 und
Xlayarsa,- 168 —
LW. beva)y phi. vBvak ZPGl. 5, Z. 3 = zd. viSava, Die Kon-
traktion fand schon im Mittelpersischen statt, da sonst aus
*ayar im Np. *yar geworden ware und da auch im Paz. er
(nicht ayar) erscheint.
Jiingere Kontraktionen sind rOnas *Krapp' aus royanas?
H. 634, cun 'wie aus *ciytln = digun H. 450 und ar Venn*
= agqLr.
§ 59. Kontraktion bei mittlerem v:
a) V fallt aus und
1) -at?a-wirdzu^: dlayad *beschmutzt' = '*alavayati (s.
oben p. 8, Nr. 42);
sardyad ^singt' = zd. sravay^iti;
sitayad preist' = skr. stavayati;
polad Stahr = phi. pOlafat (lies po-
lavat oder pdlavat, siehe oben
p. 43, Nr. 340);
```


## [2026-09-14T01:27:22.717Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rwyn\\|rwγn\\|rwgn\" SOD_pages.txt | head -20; echo \"=== by gloss ===\"; grep -n \"7345\\|^345 \\| 345 \" SOD_pages.txt | head -5"
}
```


### [2026-09-14T01:27:22.808Z] TOOL RESULT

```
12225:       frwyn- ©impf. fi}ywn =>Pywn-, P'ywn-                       Pi5ay ©<*badya- ©pass. st. =»Pynt-
15327:              4076 y}w rwyn B, M                           jf "j3J              tired(wif/i effort)
15328:                   yaw-royn =»rwyn
28423:8570 rwyn
28427:          Yaghn. ruYin ©ob. -y(y) =»Y>W rwyn                              (related to)fox
=== by gloss ===
4771:345 »y'pt- B                      j^^y^ol/
24870:7345 pry'n prytm =^ pry'nh prytmh
27704:                                                                      SCE 323; BSTBL, Dhy. 345                              >fb
29172:     KG 345 p35 n8                                              ocean
38382:OcOget lost 344, 345                  (to )go around     6145                  good looking       4862
```


## [2026-09-14T01:27:25.922Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28415,28435p' SOD_pages.txt; echo \"=== leaf of 8570 ===\"; awk 'BEGIN{RS=\"\\f\"} /8570 rwyn/ {print \"LEAF\",NR}' SOD_pages.txt; echo \"=== entry 345 area ===\"; awk 'BEGIN{RS=\"\\f\"} NR==411' SOD_pages.txt | head -5"
}
```


### [2026-09-14T01:27:27.035Z] TOOL RESULT

```
                                                                                     Oss. robds; Skt. lopasd; *raupasa ©f. n.;
 8569 rwSynch B
y     roSenc ©f. adj. ^rwSy^k
                                                       J5UJ                fox
       (o/)brass, brazen
                                                                           GMS 121; TSP 2.772, 13.18; Frag. Len. 68, 18, 19;
       SCE 229; GMS 1058
                                                                             SCE 149; Hen. Tales. 475.15
8570 rwyn
                                                if 11 'iJtJ?         8582 rwpsy'kh S
       royn   ©Av. raoYna*, Pahl. roYn\ Khwar. rYn%                                                       *bj(<f ^js) <u*bj
                                                                          rupasyak
          Yaghn. ruYin ©ob. -y(y) =»Y>W rwyn                              (related to)fox
       fat, oil
                                                                           MDii B-3, 13, 14-5 p71, 73nl2-3; MDiii p63
       TSP 2.897; BSTBL, Padm. 40, 54, Dhy. 279; STi
          36.1, 43.9; BSTii 827.50: C2, 94V20, 21; KG                8583 rwr* =* rwrh
         550, 552, 572, 580; MDii A-5, 13; CII 1990 p85;             8584 rwrh B, M                              <jLjJ**\f<jJ>
         Gersh. Sogd. Cpds. 1945, 147                                     yriira (rwr>) ©Av. urvard-      ©f. n.«, ob. -yh\ pi.
8571 rwysn B, S                                                             -t(t), -th =»>rwr(h)
                                         ^jj^jj
=== leaf of 8570 ===
LEAF 413
=== entry 345 area ===
343


8513 rst'wc'ry B                                      ^jUb
     rastucare (rst'wdryy)                                         jewel, noble
```


## [2026-09-14T01:27:34.956Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part*.txt incoming/MON/ 2>/dev/null; echo \"=== grep آروغ ===\"; grep -c \"آروغ\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null"
}
```


### [2026-09-14T01:27:35.046Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt

incoming/MON/:
total 48692
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4331421 Sep  4 14:06 MON_2vol_Adena_v2_djvu.txt
=== grep آروغ ===
MON_part2.txt:4
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4
incoming/MON/MON_2vol_Adena_v1_djvu.txt:4
MON_part1.txt:4
```


## [2026-09-14T01:27:37.677Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آروغ\" MON_part1.txt | head; echo \"=== روی brass ===\"; grep -n \"روناس\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-14T01:27:37.773Z] TOOL RESULT

```
2762:آروغ: [- آرغ - روغ - وروغ] (.) 
2766:اروق: سا [د آروغ] 1( آروغ» باد گلو. 
19811:از دهان خارج شو د. ۰ (آروغ» باد گلو) و اگر 
19817:دارد که آروغ نامند»ه زرافن» گوارش» 
=== روی brass ===
MON_part2.txt:16017:درختچه‌ای است از تیره روناسیان که 
MON_part2.txt:33914:روناسبان که دارای بوته‌های کوتاه است. 
MON_part2.txt:93232:روناسیان که خاص واحی حارة کر زمین 
MON_part2.txt:93281:درختچه‌ای از تيرة روناسیان که دارای 
MON_part1.txt:54695:ترة روناسیان که بابا است و ار تفاعش ۲۰ تا
```


## [2026-09-14T01:27:40.908Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2758,2772p' MON_part1.txt"
}
```


### [2026-09-14T01:27:40.966Z] TOOL RESULT

```
شکسته و از جای برآمده را بهم پیوندد) 
شکسته بند. 


آروغ: [- آرغ - روغ - وروغ] (.) 
باد کلو. 


اروق: سا [د آروغ] 1( آروغ» باد گلو. 
ارود: ۵( صفت نبکك» خوی خوش. 
ارویسن: 2۳۳1 [- اروین] (.) تجریبه 
امتحان» ازمایش. 

آری: 29 (ق. اثبات) کلمه‌ای است برای 
تصدیق امری» بلی» بله؛ مق. نه» نی.
```


## [2026-09-14T01:27:57.812Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T01:27:57.819Z] TOOL RESULT

```


```


## [2026-09-14T01:28:01.551Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%BA%D9%86",
 "prompt": "Give the Persian etymology section for روغن (roğan) verbatim: Middle Persian form, Avestan/Proto-Iranian reconstruction, cognates, and any cited sources (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-14T01:28:03.494Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C",
 "prompt": "Give the Persian etymology sections for روی: both روی \"face\" and روی \"brass/zinc/copper\". Quote Middle Persian forms, Proto-Iranian reconstructions, Avestan raoiδita-, and any cited sources."
}
```


### [2026-09-14T01:28:07.682Z] TOOL RESULT

```
# Persian Etymology of روغن (roğan)

Based on the Wiktionary entry provided:

**Middle Persian Form:**
The entry states: "From Middle Persian [Book Pahlavi needed] (lwkn' /⁠rōγn⁠/, "oil; butter")"

**Proto-Iranian Reconstruction:**
"from Proto-Iranian *ráwgnah, from Proto-Indo-Iranian *ráwgʰnas, perhaps from Proto-Indo-European *réwgʰ-no-s ("cream")"

**Etymology Chain:**
The word ultimately traces to PIE *rewgʰ- ("to tear, dig, churn") plus the suffix *-nos.

**Cognates Listed:**
Mazanderani رَاغون (rağun), Central Kurdish ڕۆن (ron), Shughni рӯған (rūɣan), Pashto روغن (roğán), and Zazaki ruwen.

**Sources Cited:**
The references section mentions "MacKenzie, D. N. (1971), 'rōγn', in A concise Pahlavi dictionary" and "Steingass, Francis Joseph (1892)" for Persian-English documentation, though no Hasandust or Cheung sources appear in this entry.
```


### [2026-09-14T01:28:09.626Z] TOOL RESULT

```
# Persian Etymology for روی

## روی "face" (Etymology 2)

**Middle Persian form:** 𐫡𐫇𐫏 (rwy /rōy/, "face")

**Proto-Iranian reconstruction:** *rauda- ("appearance"), derived from *Hraud- ("to grow")

**Proto-Indo-European:** *h₁lewdʰ- ("to grow")

The page notes a "semantic shift 'growth, development' > 'appearance'" tracing the meaning evolution through linguistic ancestry.

**Sources cited:** Edelʹman's *Etymological Dictionary of Iranian Languages* (2020), volume 6, page 402; and Cheung's *Etymological Dictionary of the Iranian Verb* (2007), page 193.

## روی "brass/zinc/copper" (Etymology 1)

**Middle Persian form:** 𐫡𐫇𐫏 (rwy /rōy/, "copper, brass")

**Proto-Indo-Iranian:** *Hrawdáh ("copper, brass"), from *Hrawdʰás

**Related forms:** Northern Luri ڕوویی (rruyi)

**Source cited:** Edelʹman's *Etymological Dictionary of Iranian Languages* (2020), volume 6, page 404.

Note: The page does not include Avestan forms in its etymology sections.
```


## [2026-09-14T01:28:17.400Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D9%86%D8%A7%D8%B3",
 "prompt": "Give the Persian etymology of روناس (ronās, madder): Middle Persian, Proto-Iranian, connection to روی, cited sources."
}
```


## [2026-09-14T01:28:19.341Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D9%88%D8%BA",
 "prompt": "Give the Persian etymology of آروغ (āroğ, belch): Middle Persian, Proto-Iranian/PIE reconstruction, cognates, and cited sources. Also note any variants رغ, روغ, آروق."
}
```


### [2026-09-14T01:28:23.083Z] TOOL RESULT

```
# Etymology of روناس (ronās)

Based on the Wiktionary entry, here's the etymological information:

**Primary Source:** The term was "borrowed from Ancient Greek _ῥόϊνος_ (rhóïnos, 'garnet, pomegranate-coloured')."

**Secondary Influences:** The word was "influenced by _روی_ (rōy, 'copper')" and may have also been "acquired via Aramaic attested in Classical Syriac."

**Missing Information:** The entry does not trace the word back to Middle Persian or Proto-Iranian stages. It focuses instead on the Ancient Greek origin and Aramaic transmission pathway. The connection to روی (copper) is noted as an influence on the Persian form, but no deeper proto-language etymology is provided in this source.

The documented path shows: Ancient Greek → Persian (with Aramaic influence and semantic interaction with the word for copper).
```


### [2026-09-14T01:28:24.591Z] TOOL RESULT

```
# Persian Etymology of آروغ (āroġ)

## Proto-Indo-European Origin

The word derives from **Proto-Indo-European *h₁rewg-** meaning "belch, roar." This reconstruction indicates the term's ancient roots in the language family.

## Cognates

A notable cognate appears in **Latin erugo**, which similarly means "belch," demonstrating the shared etymological heritage across Indo-European languages.

## Etymology Chain

The entry traces the word's lineage through Proto-Indo-European ancestry, establishing it as an inherited Persian term from this reconstructed ancestral language.

## Variants

The document lists several alternative forms including:
- آروق (âruq)
- آرق (âroq) – Iranian eye dialect
- وروغ (wurōġ/voruġ)
- روغ (rōġ/ruġ)
- رغ (ruġ/roġ)
- ارغ (arōġ/aruġ)

**Note:** The entry does not provide a specific Middle Persian or Proto-Iranian intermediate stage, only the PIE reconstruction as the deepest etymological source documented.
```


## [2026-09-14T01:28:31.336Z] TOOL CALL #48: Bash

```json
{
 "command": "curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B1%D9%88%D9%86%D8%A7%D8%B3&action=raw\" | head -60"
}
```


### [2026-09-14T01:28:32.815Z] TOOL RESULT

```
==Persian==

===Alternative forms===
* {{alt|fa|رویناس|tr=rōynās|روغناس|tr2=rōġnās}}
* {{alt|fa|رویان|tr=rōyān|رودینه|tr2=rōdīna|روذینه|tr3=rōḏīna||obsolete}}

===Etymology===
{{bor+|fa|grc|ῥόϊνος|t=garnet, pomegranate-coloured}}, influenced by {{m|fa|روی|tr=rōy|t=copper}}, plausibly also acquired via {{bor|fa|arc|-}} attested in {{cog|syc|ܪܘܙܢܘܣ}}.

===Pronunciation===
{{fa-IPA|rōˈnās|ir=ruˈnās}}

===Noun===
{{fa-regional|روناس|روناس|рӯнос}}
{{fa-noun|tr=ronâs}}

# [[madder]]

====Descendants====
* {{desc|ar|رُنّاس|bor=1|ll=rare}}

===References===
* {{R:fa:Dehkhoda}}
* {{R:fa:Dehkhoda|رودینه}}
* {{R:ar:Goeje|H|page=249 line 5b|lang=ar}} 
* {{R:arc:Löw-Pflanzen|page=363}}
* {{R:fa:Minorsky:1955|page=257a}}
* {{R:fa:Monchi-Zadeh:1990|page=149 Nr. 440}}
* {{R:fa:Vullers|L|II|page=80b}}

{{C|fa|Gentianales order plants|Pigments|Reds}}
```


## [2026-09-14T01:28:40.988Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rouge",
 "prompt": "Quote the etymology of \"rouge\" (French rouge from Latin rubeus) and any mention of ruby."
}
```


## [2026-09-14T01:28:41.933Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ruby",
 "prompt": "Quote the etymology of \"ruby\": Old French rubi, Medieval Latin rubinus, Latin rubeus/ruber, PIE root."
}
```


### [2026-09-14T01:28:44.450Z] TOOL RESULT

```
# Etymology of Rouge

**French Origin:**
The word "rouge" comes from French _rouge_ meaning "red coloring matter," which derives from Latin _rubeus_, itself related to _ruber_ "red" (from the PIE root *reudh- meaning "red, ruddy").

**Relevant Quote:**
"from French _rouge_ 'red coloring matter,' noun use of adjective meaning 'red' (12c.), from Latin _rubeus_"

**Connection to Ruby:**
The document mentions that the PIE root *reudh- "might form all or part of" various words including "rouge" and "ruby," indicating they share a common etymological ancestry rooted in the Proto-Indo-European word for the color red.
```


### [2026-09-14T01:28:46.644Z] TOOL RESULT

```
# Etymology of Ruby

Based on the Online Etymology Dictionary, the word "ruby" traces back through several linguistic layers:

**Old French Origin:** The term came from Old French *rubi* (12th century), which derives from Medieval Latin *rubinus lapis*, meaning "red stone."

**Latin Root:** Medieval Latin *rubinus* connects to Latin *rubeus* and *ruber*, both meaning "red."

**Proto-Indo-European Foundation:** These Latin terms ultimately stem from the PIE root *\*reudh-*, meaning "red, ruddy." As the source notes, this root is "the only color for which a definite common PIE root word has been found."

The word entered Middle English around 1300 as *rubi* or *rubie*, initially referring to "a clear, rich-red variety of corundum." By the 1570s, it began describing the color itself, and by the late 15th century, it functioned as an adjective meaning "made from or with rubies."
```


## [2026-09-14T01:28:57.416Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%DA%98",
 "prompt": "Persian رژ — etymology (from French rouge?), meaning lipstick/rouge. Quote it."
}
```


## [2026-09-14T01:28:58.722Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/reek",
 "prompt": "Quote the etymology of \"reek\": Old English recan/reocan, Proto-Germanic *reukanan, PIE root *reug-."
}
```


### [2026-09-14T01:29:00.704Z] TOOL RESULT

```
# Persian Word رژ (Rož)

**Etymology:** The word derives from French *rouge à lèvres* (lipstick), translated into Persian as "رژ لب" (rož-e lab).

**Definition:** According to Wiktionary, رژ functions as "short for رژ لب (rož-e lab)" in colloquial Persian usage, referring to lipstick or rouge as a cosmetic product.

**Historical note:** The entry also documents an archaic sense where the term meant "anger," though this usage is no longer current in modern Persian.
```


### [2026-09-14T01:29:03.836Z] TOOL RESULT

```
# Etymology of "Reek"

The word "reek" traces back through several language layers:

**Verb form:** "Middle English _reken_ 'to emit smoke,' from Old English _recan_ (Anglian), _reocan_ (West Saxon) 'emit smoke,' from Proto-Germanic _\*reukan_"

**Noun form:** "Middle English _reke_ 'smoke, fumes; steam, vapor,' from Old English _rec_ (Anglian), _riec_ (West Saxon), 'smoke from burning material,' probably from a Scandinavian source"

Both ultimately derive from **PIE _\*reug-_**, which meant "to vomit, belch; also smoke, cloud."

The sense shifted over time—the "stench" meaning developed by the 1650s through the notion of something that rises. The verb's sense of "emit a bad smell" appeared later, around 1710, evolving from an earlier sense meaning "be heated and perspiring" (early 15th century).
```


## [2026-09-14T01:29:11.368Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81rew d%CA%B0-",
 "prompt": "PIE root for \"red\" — give the reconstruction, gloss, and descendants (Indo-Iranian, Latin, Germanic)."
}
```


### [2026-09-14T01:29:12.702Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:29:12.794Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/rewg%CA%B0-",
 "prompt": "Give the reconstruction, gloss and descendants of PIE *rewgʰ- including any *rewgʰ-no-s \"cream\" derivative."
}
```


### [2026-09-14T01:29:14.152Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:29:17.565Z] TOOL CALL #55: Bash

```json
{
 "command": "for t in \"Reconstruction:Proto-Indo-European/h₁rewdʰ-\" \"Reconstruction:Proto-Indo-European/rewgʰ-\" \"Reconstruction:Proto-Iranian/ráwgnah\" \"Reconstruction:Proto-Indo-European/h₁rewg-\"; do echo \"=== $t ===\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$t\")&action=raw\" | head -50; done"
}
```


### [2026-09-14T01:29:19.537Z] TOOL RESULT

```
=== Reconstruction:Proto-Indo-European/h₁rewdʰ- ===
{{reconstructed}}
==Proto-Indo-European==
{{etymon|ine-pro|id=red|pos=root}}

===Root===
{{ine-root|adj}}

# [[red]]

====Derived terms====
{{rootsee}}

* {{l|ine-pro||*h₁réwdʰ-e-ti|pos=thematic present}}
** {{desc|gem-pro|*reudaną}} {{see desc}}
** {{desc|grk-pro|*eréutʰō}}
*** {{desc|grc|ἐρεύθω}}<ref>{{R:ine:LIV|page=508}}</ref><ref>{{R:grc:Beekes:2010|page=455}}</ref>
* {{l|ine-pro||*h₁réwdʰ-s ~ *h₁rudʰ-ós|pos=root noun}}
** {{desc|cel-pro|*ruts|t=madder}} {{see desc}}
* {{l|ine-pro|*h₁rudʰéh₁ti|*h₁rudʰ-éh₁-ti|pos=éh₁-stative}}
* {{l|ine-pro||*h₁réwdʰ-it-os}}
** {{desc|iir-pro|*Hráwdʰitas}} {{see desc}}
* {{l|ine-pro|*h₁rudʰrós|*h₁rudʰ-rós}}
* {{l|ine-pro||*h₁rudʰ-tós}}
** {{desc|itc-pro|*russos}}<ref>{{R:itc:EDL|page=527}}</ref>
*** {{desc|la|russus}} {{see desc}}
* {{l|ine-pro||*h₁rudʰ-yo-s}}
** {{desc|ine-bsl-pro|*rūˀdjas}} (post-PIE lengthened grade {{m|ine-pro||*h₁ruHdʰ-yo-s}})
*** {{desc|sla-pro|*ryďь}} {{see desc}}
* {{l|ine-pro||*h₁ru-né-dʰ-ti ~ *h₁ru-n-dʰ-énti|pos=nasal-infix present}}
** {{desc|cel-pro|*rundeti}} {{see desc}}
* {{l|ine-pro||*h₁rowdʰ-so-s}}
** {{desc|ine-bsl-pro|*raudsas}}
*** {{desc|sla-pro|*rusъ}} {{see desc}}
* {{l|ine-pro|*h₁rowdʰós|*h₁rowdʰ-ós}}
* {{l|ine-pro||*h₁rowdʰ-os ~ *h₁rowdʰ-es-os}}
** {{desc|itc-pro|*rouβos|alt=*rouβos ~ *rouβoses}}
*** {{desc|itc-ola|rōbos|alt=rōbos ~ rōbores}}
**** {{desc|la|rōbur}}
* {{l|ine-pro|*h₁rudʰ-i-[[pel-]]}}
** {{desc|grk-pro|}}
*** {{desc|grc|ἐρυσίπελας}}

; Unsorted formations:
* Balto-Slavic:
** {{desc|lt|raũmins}}
** {{desc|lt|raumuõ}}
** {{desc|sla-pro|*ruměnъ}} {{see desc}}
* {{desc|sla-pro|*rъďa}}, {{l|sla-pro|*rъďavъ}} {{see desc}}
* Albanian:
** {{desc|sqj-pro|*awa-ruđa|unc=1}}
=== Reconstruction:Proto-Indo-European/rewgʰ- ===
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1112 cp1112, Varnish XID 1073159845<br>Upstream caches: cp1112 int<br>Error: 404, Not Found at Mon, 14 Sep 2026 01:29:18 GMT<br><details><summary>Sensitive client information</summary>IP address: 128.100.1.22</details></code></p>
</div>
</html>
=== Reconstruction:Proto-Iranian/ráwgnah ===
{{reconstruction}}

==Proto-Iranian==

===Etymology===
From {{inh|ira-pro|iir-pro|*ráwgʰnas}}, perhaps from {{inh|ira-pro|ine-pro||*réwgʰ-no-s|cream}}, from {{af|ine-pro|*rewgʰ-|*-nos|nocat=1}}, from {{m|ine-pro|*rew-||to tear, dig, churn}}.<ref>{{R:ine:IEW|head=reugh-m(e)n-|page=873}}</ref> Possible cognate with {{cog|gem-pro|*raumaz}}.

===Noun===
{{head|ira-pro|noun|g=m}}<ref>{{R:ira:Novák:2013|page=183}}</ref>

# [[butter]], [[oil]]

====Inflection====
{{ira-decl-noun-auto}}

====Descendants====
{{top3}}
* Central Iranian:
** {{desc|ae-yng|𐬭𐬀𐬊𐬖𐬥𐬀|g=m}}
* Northeastern Iranian:
** {{desc|xsc-pro}}
*** {{desc|kho|tr=rrūṇa}}
*** {{desc|wbl|rūɣ̌n|rūɣ̌ən}}
** {{desc|ira-sbc}}
*** {{desc|xbc|𐫡𐫇𐫃𐫗|tr=rwgn}}
*** {{desc|xco|rɣyn}}
*** {{desc|ira-sgc-pro}}
**** {{desc|sog|𐽀𐼴γ𐼻|tr=rwγn|ts=rōɣᵊn}}
**** {{desc|yai|рӯғн|рӯған|рӯғна}}
* Southeastern Iranian:
** {{desc|ps|روغن|tr=roğán}}
** {{desc|ira-sgi-pro}}
*** {{desc|isk|tr=reɣn|3=|tr2=ɣun}}
*** {{desc|sgy|tr=rōɣ}}
** {{desctree|ira-sym-pro|*rūɣn}}
* Northwestern Iranian:
** Kurdish:
**: {{desc|ckb|ڕۆن}}
**: {{desc|kmr|rûn}}
**: {{desc|sdh|رۊن}}
** {{desc|ira-mpr}}
*** {{desc|mzn|راغون|tr=rağun}}
*** {{desc|xpr|𐫡𐫇𐫃𐫗|ts=rōɣn}}
**** {{desc|pal|tr=lwkn'|ts=rōɣn|sc=Phlv|bor=1}}
***** {{desctree|fa-cls|رَوْغَن}}
***** Luric:
****** {{desc|lrc|رغۏ|tr=reğö}}
****** Silakhori: {{l|lrc|رۋغۏ|tr=rüğö}}
****** {{desc|bqi|رۏغن|tr=röğen}}
****** {{desc|luz|رۏغن|tr=röğen}}
=== Reconstruction:Proto-Indo-European/h₁rewg- ===
{{reconstructed}}
==Proto-Indo-European==

===Etymology===
{{ety|ine-pro|pos=root}}
{{onom|ine-pro}}.

===Root===
{{ine-root}}<ref>{{R:grc:Beekes|vol=I|page=454}}</ref>

# to [[belch]]
# to [[roar]]

====Derived terms====
{{rootsee}}

* {{l|ine-pro||*h₁ru-né-g-ti ~ *h₁ru-n-g-énti|pos=nasal-infix present}}
** {{desc|grk-pro|}}
*** {{desc|grc|ἐρῠγγᾰ́νω|t=I belch}}
* {{l|ine-pro||*h₁réwg-(e)-ti|pos=root present}}
** {{desc|ine-bsl-pro|*ráuˀgtei}}<ref>{{R:bat:EDBIL|head=*raugti|page=378}}</ref>
*** {{desc|lv|raûgt|t=to pickle}}
*** {{desc|lt|ráugti|t=to leaven, pickle}}
** {{desc|gem-pro|*reukaną}} {{see desc}}
** {{desc|grk-pro|}}
*** {{desc|grc|ἐρεύγομαι|t=I belch}}
** {{desc|itc-pro|*rougō}}<ref name="De Vaan">{{R:itc:EDL|head=-rūgō, -ere|page=529}}</ref>
*** {{desc|la|ērūgō|alt=(ē)rūgō|der=1}}
* {{l|ine-pro||*h₁réwg-ye-ti}}
** {{desc|itc-pro|*rougiō}}
*** {{desc|la|rūgiō}} {{see desc}}
* {{l|ine-pro||*h₁rowg-o-s}}
** {{desc|ine-bsl-pro|*rauˀgas}}<ref>{{R:bat:EDBIL|head=*raugas|page=377}}</ref>
*** {{desc|lv|raûgs}}
*** {{desc|lt|ráugas}}
* {{l|ine-pro|*h₁réwg-(s-)[[-mn̥|mn̥]]}}
** {{desc|itc-pro||alt=*roug(s)mən ~ *rug(s)mən}}<ref name="De Vaan"/>
*** {{desc|la|rūmen}} {{see desc}}

; Unsorted formations:
* Armenian:
** {{desc|xcl|ործամ}}, {{l|xcl|ործկամ||vomit}}
** {{qual|perhaps}} Old Armenian: {{l|xcl|առիւծ|gloss=lion}}
* {{desc|ine-bsl-pro|*rūˀgā́ˀtei}}
** {{desc|sla-pro|*rygati|t=to belch}}, {{l|sla-pro|*rigati}} {{see desc}}
* {{desc|ine-bsl-pro|*rū́ˀgtei}}<ref>{{R:bat:EDBIL|head=*rūgti|page=385}}</ref>
** {{desc|lv|rûgt|t=to ferment}}
** {{desc|lt|rū́gti|t=to turn sour, to regurgitate acid}}
* {{desc|ine-bsl-pro|}}
** {{desc|lv|raûgâtiês|t=to belch}}
```


## [2026-09-14T01:29:36.084Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW robeus ===\"; grep -n \"robeus\\|rōbeus\\|robus,\" LEW_1910.txt | head -10; echo \"=== LAT robeus ===\"; grep -n \"robeus\\|robus\" LAT.txt | head -10; echo \"=== IEC reudh ===\"; grep -n \"reudhos\\|reudho\\|roudho\\|rudhros\" IEC.txt | head -10; echo \"=== IEC reugh ===\"; grep -n \"reughmen\\|reugh-men\\|reughm\" IEC.txt | head -10"
}
```


### [2026-09-14T01:29:36.187Z] TOOL RESULT

```
=== LEW robeus ===
=== LAT robeus ===
1385:comme le note Probus, GLK IV 150,9, il.y a des cas ou la distinction
3268:pelle osq. anafrlss = lat. imbri bus. Pour le b en face de 1 cf. robus
3799:robustus, augustus, uetus/uetustus? D'ou angustia, employe surtout au
3823:angustus peut-etre egalement tire de la, cf. le type robustus. L'elar-
5257:le Ps.Probus, GIK IV 47, note ueteres artem pro uirtute frequenter
6999:bassus, -us m.: substantif peut-etre imagin 4 par Probus Inst.Gramm.
8707:Le rapport roblgo/robus incline a penser que caligo derive d'un
11482:qui fait naitre les aoissons". Probus, Vg.G.1,7, Cerere* a creando
11558:ceueo,-es, ceui, ceuere (ceuo,-is attest6 par Probus, GLK IV 37,8;
17781:de duo, cf. du-(plex), comme probus est tird de pro-bho-s. A dubo se
=== IEC reudh ===
2476:droudhos, ā ‘forced, constrained; straint’. Cf. drudh- & WP I, 800 ON trauór ‘reluctant’; trauð ‘difficulty’; cf. trauóa (v. "Tat Latv. draudi, pl. ‘threats’; draudēt ‘to threaten’; Li. cf. draudimas "ban: warning; insurance’; draudZiü, draüsti “ban; warn; insure'
7880:kreudhos, om (?) ‘whip, reed'; (2) ‘shake’? OE hrëod, n. ‘reed’; OHG hriot, OS hriod, id.; Lusat. krjud, m. ‘whip’. (FK: EWDS 17 otherwise). (Isophonic: Skt. krodhah “anger? beside krudhyami *be angry': Av. xraodei(mi) “fear, tremble’)
14538:repl- (replio, replis) — reudhos
14551:reudhó ‘make red; redden’. Cf. roudhos, rudh- Gk. ereütho, v. tr. id.; OE reodan, sv. 2. tr. id.; ON rjóða, sv. tr. id.
14552:(reudhoó "root up, eradicate’, see Supt: R)
14553:reudhos “red; redness'. Form of roudhos,
14756:rot- — roudhros (rudhros)
14765:Cf. reudh-, rudh-, roudhos
14769:roudhos ‘red, russet’. Cf. reudh-, rudh-. WP II, 358 Skt. cf. rodhrah, m. late lodhrah ("lodh-tree', a dye-producer); Gk. rhóusios, adj. 'red- brown’; beside (e-gde) éreuthos, n. ‘red col- our’; Lat. cf. (dial.) rüfus, adj. ‘reddish’; Umb. rofu, mpl. acc. "red MIr. road Ir. ruadh, adj. id.; Gaul. roudo-, Br. rüz, MW rudd, W rhudd, Cor. roeth, id.; OHG rot, id.; G cf. also Acker- róte, f. madder": OE read & (e-gde) reod,adj. ‘ted’; ON rauór, id.; OCS ruda, f. ‘metal’; R rudà, f. ‘ore’; Cz. rudý, adj. ‘red, reddish’; rud, gs: -i, f. fred-colour; Li. raüdas, adj. “bay, roan, red-brown’; raudà, f. ‘redness; roach’; Latv. rauds, adj. ‘red-brown’; (LW in) Finn. rauta, s. “iron”; rautias, adj. “toan, red- brown’. (NB. According to H. Pedersen Sum- erian urudu “copper” is the prototype basis of Pahlevi rod, id. and of Lat. raudus “metal ingot for coining’ and ON rauði *bog-iron'. The Latin vocalism suggests borrowing)
14770:roudhros (rudhros), extn. of types roudhos, rudh-. WP II, 358 Skt. rodhrah, m. (lodh-tree', producing a red powder); Tokh. rtár, adj. ‘red, reddish’; Lat. rüber, f: rübra, adj. (red; Umb. acc. pl. m. rufru, id.
=== IEC reugh ===
```


## [2026-09-14T01:29:44.981Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC cream/raugmen ===\"; grep -n \"raugmen\\|rougmen\\|reughm\\|'cream'\\|‘cream’\" IEC.txt | head -10; echo \"=== SYN red ===\"; grep -n \"15\\.65\\|Red$\\|^15\\.65\" SYN.txt | head; echo \"=== SYN raoghna/butter ===\"; grep -n \"raoyna\\|rōγan\\|rogan\\|Av. raoyna\" SYN.txt | head"
}
```


### [2026-09-14T01:29:46.111Z] TOOL RESULT

```
=== IEC cream/raugmen ===
7038:kermn- ‘cut, cutting; piece, part; skin, flesh’. WP II, 573 Skt. Cárman, cpds. čarma- ‘skin, hide; Av. čaromam, id.; Per. Cárm; Oss. carm, id. (pl. cärmttä), id.; Gk. kérma (“slice, cutlet, small coin’, ambig. cf. Kerð); OCS črěmůù ‘tent’; Cz. Gemen, střemen ‘stirrup’; Latv. ker- menis ‘body’; OPr. kērmens, m. id. (Alb. cermë ‘cream’, if not a LW, suggests an alter- native type *querm-)
13015:platikós Gk. platikós, adj. “broad, general; LG fládig, fledig, flódig ‘flimsy, limp, weak’; Du. cf. vlade, f. ‘cream’
13115:pleudos, à, io (plud-, plüd-) “flow, float, swim; light, flowing, floating’. Cf. pleudó and ploud- Lat. cf. ap-pluda, aplüda, f. (“chaff, bran’. Se- mantics obscure); MHG vliez, sm. & n.; -e, sf. “stream, current’; OE flëot, m. ('estuary, tributary; raft, ship'. Z-gde in flot, n. deen water'; flota, wm. “ship, fleet); ON fljót, n. "floating; river, lake"; fljótr, adj. ‘swift, fleet’; Du. vliet, m. “little stream, rhine'; Norw. flöte ‘cream’; (ü in) Li. plüdé, f. “float, cork’; (u in) Late pludi, mpl. ‘floats’; plude, f. ‘float’; (ü in) plüdi, mpl. “flood?
13162:ploudeio, io ‘gush, be effusive, sweep along, . swill'. Cf. pleuo, etc. & ploud- Mir. luaidim, v. ‘move’; Go. flautjan, v. ‘boast’; cf. flauts, adj. ‘boastful’ (ambig. see ploud-); ON fleyta, v. launch, float’; flautir, fpl. ‘whipped cream’; Norw. flöte ‘cream’; OE fliete, f. ‘cream, curd; punt, raft’; MHG vlōz, sm. ‘stream, current’; OHG floz, n. ‘raft’; OFris. flat (sic), id.; Li. plaudžiu, plausti, v. ‘rinse, wash’; Latv. plaužu, plaust, v. tr. ‘pour forth; blab out beside plaudu, et, v. ‘dredge’. (Isophone: Latv. plaudis ‘bream’)
=== SYN red ===
25867:15.65 Buack
26646:2. Grk. uédas, xedauvds ‘black’ (15.65), also ‘dark’ in color,
26664:Br. du ‘black’ (15.65), also ‘dark’, as glas du ‘dark green’.
26675:6. Skt. krsna-, gyama ‘black’ (15.65), also ‘dark’ in color.
26708:15.65 BLACK
26773:OE hewen (gl. glaucus, caeruleus, hya- cinthinus, viridis, etc.), also h@we ‘blue, gray’ : Ir. ciar ‘dark, brown’, ON harr, OE har ‘hoary’; ChSI. sint, Russ. sini] ‘(dark)blue’, SCr. sinji ‘gray-blue, sea- green’, etc.; Lith. syvas, ChSI. sivit, Russ. sivyj ‘gray’, Skt. cyama- ‘black’ (15.65). Walde-P. 1.360f.
26774:5. Lith. mélynas : Lett. melns, Grk. nédas ‘black’ (15.65). Walde-P. 2.294,
27368:2. Lat. sordidus, with sordére ‘be dirty’, sordés ‘dirt, filth’ : Goth. swarts ‘black’, etc. (15.65). Walde-P. 2.585. Ernout-M. 958.
27413:7. Skt. malina-, malavant-, etc., sb. mala- ‘dirt, filth, impurity’ : Grk. pédas, Lett. melns ‘black’, etc. (15.65). Walde 2.293 f.
32497:Most of the words for ‘ink’ are de- rived from words for ‘color’ or.a color, especially ‘black’ (15.65). The Latin words were widely borrowed.
=== SYN raoghna/butter ===
7008:mundrus ‘lively, arrogant’, OHG mun- tar ‘zealous, lively’ (NHG munter), eto, Walde-P. 2.270 £.
9719:5.89 BUTTER Grk. — Bobripov (late) Goth. Lith.  sviestas NG — Bobrupov ON — smjor Lett.  sviests Lat. bityrum (late) Dan. smé¢r ChSl. a It. burro Sw. smér SCr. maslac Fr. beurre OE butere Boh.  mdslo Sp. manicca ME _butere Pol. —masto Rum. unt NE butler Russ. maslo Ir. amb Du. _boter Skt. ghrta-, navanita- NIr. im OHG = ancho, bulera Av. (raoyna-) W. ymenyn MHG buter, anke Br. amann NHG butter
9732:Av. raoyna-, raoynya- ‘butter’ (? So Barth. 1488) or ‘oil’ (Darmesteter) : NPers. rawyan ‘oil, grease’, outside con- nections unknown.
27501:Many parts of the body or bodily ac- tions are associated with emotions. Notably the heart, the words for which are universally used to denote the seat of emotion or ‘temperament, disposi- tion’, and in part (alone or in derivs. or cpds.) for special emotions such as ‘courage’, ‘fondness, love’, ‘sympathy, pity’, and (in Balto-Slavic) ‘anger’. Bristling of the hair may indicate ‘hor- ror’ (Lat. horror; cf. NE adj. hatr-razs- ing) or pleasurable excitement, ‘joy’ (Skt. harsa-, 16.22). To lower or wrinkle the eyebrows, ‘frown, scowl’, usually shows displeasure, but also arrogance (cf. numerous Grk. phrases with é¢pts, LS s.v.; NE. supercilious). Not only tears but also downcast eyes indicate ‘srief, sadness’ (NG xarn¢is ‘sad’, 16.36). Laughter may show pleasure or ridicule. Puffing out’ the chest suggests ‘pride’ (cf. NG kapapdvw etc., 16.48), as does also strutting or a stiff bearing. Words for ‘breath’ are the most common source of those for ‘soul, spirit’, and heavy breath- ing may indicate ‘hate’ (OE anda, 16.41) or ‘anger’ (Lett. dusmas, 16.42). The bile or gall is associated with bitter anger (Grk. xédos, 16.42; NE gall in U.S. slang ‘excessive assurance, impu- dence’; cf. also Grk. pedayxonia ‘black gall, melancholy’; the spleen with a variety of quite disparate emotions (NED s.v. spleen). A Greek word for the principal internal organs (orAayxva) was felt as the seat of various emotions (ef. LS s.v.), and later, through its use in the LXX and NT to translate a cer- tain Hebrew word and rendered in our
28752:3. Ir. format, NIr. formad, Br. gour- venn, arch. W. gorfyn, fr. a cpd. of Ir. for-, W. gor-, etc. ‘over’ and mento- (with influence of W. mynnu, etc. ‘wish’) fr. the root *men- ‘think’. Cf. Hom. brrep-pevewy ‘arrogant’. Pedersen 1.168.
28915:The nouns for ‘pride’ are derived from the adjs. for ‘proud’, or conversely. The adjs. are chosen here for discussion. Most of them are used for ‘proud’ in both the good and the bad sense. But a few of the words listed are used only in the latter sense, that is ‘proud’ = ‘haughty, arrogant’, and in many of the others this is the earlier, either in actual use or as indicated by the etymology.
28917:1. Grk. drepadarvos, epd. of izép ‘over’ and -favos ‘appearing’ : dalvouar ‘ap- pear’, with 7 (Dor. a) after the analogy of words with composition lengthening, esp. viep-yvwp ‘arrogant’. Brugmann, Ber. Sachs. Ges. 1901.104 derives the
28918:second member fr. -deavos, comparing dmepplados ‘arrogant, proud’ fr. -dfiades and Lat. swperbus ‘proud’. But there is no good reason to separate srephpavos from the large group of cpds. in -davos.
28924:mindru, orig. ‘wise’, fr. Slav. sat “rit ‘wise’ (17.21). Tiktin 986. For semantic relation, ef. Ir. diwmmusach (below, 3) and Pol. dumny (below, 6). 3 Jr. aallach, fr. sb. wall (*oup-sla-) : uasal, W. uchel ‘high’, Grk. tyndés ‘high’, ete, Walde-P. 1.193. Ir. diummusach, fr. sb. dtwmmus (*di-ud-mess) cpd. of midiur judge’. Pedersen 2.579. K. Meyer, Contrib. 665. Nir. mordhach, cf. médrdha id. also ‘great, grand, stately’, Ir. mérda ‘haugh- ty’, fr. mor ‘great, large’. NIr. waibhreach, fr. sb. uabhar, Ir. nee ‘arrogance, boasting’: W. ofer vain’, Br. ewer ‘vapid, spiritless’, perh. also Goth. abrs ‘strong, violent’, abraba very’. Walde-P. 1.177. Pedersen 1.49. NW: baleh, Br. bale’h : Ir. bale(c) id Stout, mighty’, prob. fr. the tae ae ppl ,in Gu. paddébs ‘penis’, oe a bag’, Ir. ball ‘limb’, ra ino oe pee enn Velde 2178, y fr. ‘swollen’. pds, - ee re: OE _héahheort,
28931:ON dramblatr, fr. dramba ‘be haughty, pompous’, dramb ‘arrogance’, also ‘roll of fat on back of neck’ (hnappa-dramb), NIcel. drambr ‘knot (in wood, etc.)’; de- velopment of ‘arrogance’ fr. ‘swelling’.
```


## [2026-09-14T01:29:54.867Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN RED ===\"; grep -n \"15\\.66 RED\\|15.66 Rep\\|15\\.66\" SYN.txt | head -5; echo; sed -n \"$(grep -n '15.66 RED' SYN.txt | head -1 | cut -d: -f1),+25p\" SYN.txt 2>/dev/null | head -30"
}
```


### [2026-09-14T01:29:55.919Z] TOOL RESULT

```
=== SYN RED ===
9429:3. Dan. rédlég, Sw. rédlok, epd. of words for ‘red’ (15.66) and ‘leek’ (ON laukr, OE léac, etc.).
15388:SCr., Boh. Russ. rudnik, fr. ruda, ‘ore’, orig. ‘red ore’ : ChSI. rtidrti (15.66).
25868:15.66 Rep
26619:Lett. krasa, esp. ‘beautiful complex- ion, beauty’, as ‘color’ also krass (Lith. krosa ‘color’, in Kurschat krosas, is no longer used, neither form in Lalis or NSB), fr. the Slavic, ChSl., Russ. krasa ‘beauty’, cf. Russ, kraska ‘paint’ (9.88), krasnyj ‘red’ (15.66). Miihl.-Endz. 2.267. Berneker 607 f.
26729:1056 SELECTED INDO-EUROPEAN SYNONYMS 15.66 RED Grk. — épvOpéds Goth. raups Lith. raudonas NG KOoxxtvos ON rauodr, rjodr Lett. sarkans Lat. ruber (rufus, russus) Dan. rd ChSl.  Giiminy, (Giveni, It. TOsso Sw. rod ritdrit) : Fr, rouge OE réad, réod SCr.  crven Sp. rojo ME reed Boh. — éerveny Rum. rosiu NE red Pol. —czerwony Ir, derg, ritiad Du. rood Russ. krasnyj NIr.  dearg, ruadh OHG rat Skt. rakta-, lohita- W. coch, rhudd MHG rat Av. raoisita- Br. ruz NHG rot

1056 SELECTED INDO-EUROPEAN SYNONYMS 15.66 RED Grk. — épvOpéds Goth. raups Lith. raudonas NG KOoxxtvos ON rauodr, rjodr Lett. sarkans Lat. ruber (rufus, russus) Dan. rd ChSl.  Giiminy, (Giveni, It. TOsso Sw. rod ritdrit) : Fr, rouge OE réad, réod SCr.  crven Sp. rojo ME reed Boh. — éerveny Rum. rosiu NE red Pol. —czerwony Ir, derg, ritiad Du. rood Russ. krasnyj NIr.  dearg, ruadh OHG rat Skt. rakta-, lohita- W. coch, rhudd MHG rat Av. raoisita- Br. ruz NHG rot
The majority of the words for ‘red’ be- long to an inherited group pointing to an TE word for ‘red’. Several of the others are derived from names of vegetable or animal sources of red dye; some from ‘rosy’ or ‘glowing’.
1. IE *reudh-. Walde-P. 2.358 f. Ernout-M.872. REW 7408, 7465, 7466. Falk-Torp 932.
Grk. épvépés; Lat. ruber, and (dial.) rufus mostly ‘light red’ (esp. of hair), Umbr. rufru ‘rubros’, also Lat. rubeus ‘reddish’ (> Fr. rouge, etc.), and (*rudh- tos) russus (>It. rosso; Fr. roux of hair), whence russeus ‘reddish’ (> Sp. rojo, Port. rozo); Ir. raad, NIr. ruadh, W. rhudd, Br. ruz; Goth. raups, ON raudr, OF réad, etc., general Gmc., also with different grade ON 7j00r, OF réod; Lith. raudas, now usually raudonas, also rudas ‘red-brown’, Lett. ruds ‘reddish’ ; late ChSI. ridri (ridrit, rodri), ryzdt, ruméni (SCr. rumen, Boh. rumény, Pol. rumiany, Russ. rumjanyj ‘flushed, red’ of complexion), etc, (cf. Trautmann, 238 f.); Skt. (Vedic) rohita-, later lohita-, Av. raotsita- (Skt. rudhira- ‘bloody’, exp. sb. ‘blood’).
2. NG xéxxwos, in class. Grk. ‘scar- let’, but now the pop. word for ‘red’, deriv. of Grk. xéxos ‘grain, seed’, and esp. ‘gall of the kermes oak’ yielding scarlet dye. Hence Lat. coccinus and
coccum (late coccus) used also for ‘scar- let (color)’ and ‘scarlet garments’,
3. Rum. rog(u), rogiu, fr. Lat. roseus ‘rose-colored’, deriv. of rosa ‘rose’. REW 7379. Puscariu 1475,
4. Ir. derg, NIr. dearg: OE deore ‘dark’, etc. (15.63). Walde-P. 1.855,
W. coch, fr. Lat. coccus (above, 2). Loth, Mots lat. 150.
5. Lett. sarkans, deriv. of  sarks ‘slightly red’, prob. fr. the same root as sdrts ‘red’ (in the face) : Lith. sartas ‘sorrel’, Lat. sorbum ‘service berry’, Skt. sdra- ‘heart-wood’ of a tree, saranga- ‘variegated’. Walde-P. 2.499. Miuhl.- Endz. 3.721, 807.
6. ChSI. ériimint (Russ. cermnyj ‘pur- ple-red’, fr. the ChSl., SCr. old érman), fr. *Sirmt ‘worm’ (Slov. érm ‘finger- worm, carbuncle’, etc.) : Skt. krmi- ‘worm’, etc. (3.84). Semantic develop- ment through the red dye obtained from various worms (ef. Fr. vermeil, fr. Lat. vermiculus ‘little worm’ and late = coc- cum). Berneker 169.
ChSI. ériivijent, sb. ‘red color’, Russ.- ChSl. riveni ‘red’, etc., general Slavic (Russ. éervonnyj ‘purple-red’, fr. Pol.); fr. ChSl. érivt, etc. ‘worm’. Walde-P. 1.523. Berneker 169, 172 f.
Russ. krasnyj : ChSl. krasini ‘beau- tiful’, ete. (general Slavic in this Bente but freq. also with special sense of a ing, ruddy’ and the like), deriv. °
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ty’, Russ. krasa ‘beau-
SENSE PERCEPTION
Digitized by Arya Samaj Foundation Chennai and eGangotri
/
1057
kurti ‘to heat’, etc. Berneker 607 f.
¢
prasad beau chs. ee ent, etc. (Pol. kras ‘color’, | Walde-P. 1.418 f. iy; ie color’ also ‘beauty’, ete.), prob. | 7. Skt. rakia-, lit, ‘colored’, pple. of P. ie 2 plendor’ (whence both ‘red’ | 7aj- ‘be colored’ (esp. red), be excited’, ey fhe utiful’) : Lith. karstas ‘hot’, | ete. : ranga-, rdga- ‘color’, etc. (15.61). aul
15.67 BLUE Goth. Lith. mélynas
Grk. cae Waxdtios, ON  blar Lett. zils NG nabs Dan. Oblaa ChSl.  sint
caeruleus Sw. bld SCr. modar Jat. blu, azzurro OE bl@wen, h@wen Boh. modry 4 blew ME blew Pol. —_niebieski 5 azul. NE blue Russ. sinij, goluboj i albasiru Du. blauw Skt. _nila- Ir. gorm, glass OHG blao Av. Nir.  gorm MHG Ola Eas NHG  blau Br gas
Many of the words for ‘blue’ are from roots that appear in the names of other colors, as ‘gray’, ‘black’, ‘yellow’, ‘green’, the primary application of which is un- certain. Some are derived from names of the sky, lapis lazuli, etc.
```


## [2026-09-14T01:30:02.845Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"raoyna\\|raogna\\|reugh-m\\|reudh-\\|rjümi\\|rjumi\" WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-14T01:30:02.916Z] TOOL RESULT

```
23313:mit wohl auch die unter "reugh-m(e)n- „Rahm" besprochenen germ. Worte
23426:   reudh- bes. „reuten, roden“.
23524:(s. o.   "^reudh-), nhd. mdartl. riester     „Lappen von Leder zum Schuhflicken“;
23595:                                        reng        reugh-m(e)n-                                      357
23627:„Lab‘^ (iiber     sly.   raoyna- „Butter“                           ^ahm“). Curtius 181f.,
23654:  Av. raoyna- „Butter'', mpers. npers. rdyayi „(ausgelassene; Butter"; anord.
23657:358                                        reudh-
23662:Einerseits wird fur ay. raoyna- Verwandtscliaft mit lit. \szrugos „Molken‘S
23674:reudh- „rot“.
23681:IP. 19, 124f., wo Gdf. ^reudh-s-to-‘, diese bestritten vonPersson Beitr. 325
23690:wie unten die auf ^reudh-s^ *rotidh-s, "^rudh-s- beruhenden Bildungen, iiber
23714:                                           reudh-                                       359
23744:    Aksl. rudz    „rot'^,   ruda „Erz, Metall“, rusz {^reudh-s-o- oder '^rondh-s-o-')
23801:*reudh- „rot'‘), lat. raudus, rodus, nidus und rudis mit abweichendem d
42340:*     streudh- oder strent-: ags. strudan „raubeTi, pliindern^, strydan ,,be-
```


## [2026-09-14T01:30:04.974Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '23650,23700p' WLD_Bd2_pages.txt"
}
```


### [2026-09-14T01:30:05.032Z] TOOL RESULT

```
rem^ fuyyium). Unsicher. Wenn alb. rtl „Wolke‘' aus "^rougi- entstanden ist,
wie dt. Rauch (G. Meyer Alb. Wb. 362), ist ein bereits uridg. * reug- „V^o\ke,
Rauch“ voraussetzbar.
reugh-ni(e)n- „Rahm“?
  Av. raoyna- „Butter'', mpers. npers. rdyayi „(ausgelassene; Butter"; anord.
rjomi m. „Rahm", ablautend ags. rearn^ mnd. rome, mhd. roiim „Sahne", und
   Walde, Etymologlsches Worterbuch. II.                                                     24
358                                        reudh-


mnd. mme (fur           woraus nhd. Bahm^ mit u els. schweiz.   ds. Ygl.       mm
Schwyzer IF. 21, 180 f.; 23, 307 f., Falk-Torp u. r^mme. Hochst unsicher.
Einerseits wird fur ay. raoyna- Verwandtscliaft mit lit. \szrugos „Molken‘S
rdugas „Sauerteig‘‘, apr. ructan dadan „Baure Milch“ usw. erwogen, freilich
mit zweifelhaftem Rechte, da diese zu *reitg- „sich erbrechen, sauer auf-
sto6en‘‘gehoren und die Annahme gleicher Bed.-Entw. im Av. beim Fehlen
vermittelnder av. Yerwandter bloBe Yermutung bleibt (die germ. Formen
waren mit diesem "^reug- iiberhaupt nur unter einer sonst ungestiitzten, da-
ber abzulehnenden Wzvariante reugh- oder reuJc- zu vermitteln). Aber fiir
die germ. Formen macht ags. reoma^ reama „dunne Haut“ (vermutlich als
„die abgerissene“ zu *reu- „aufrei6en‘‘) eine Gdbed. „Haut, Fettscbicht auf
der Milcb“ und eine Gdf. *reu-, roit~, m-m{en)- wahrscheinlicher (Fick
in* 348).

reudh- „rot“.
   Ai. Tohifa-   = av. raodita     „rot, rotlicb^,    roMt- „rote Stute, Weibcben einer
Gazelle",   rohi- m.,   roM   f.    „Gazelle“;      ai.   loM~ „r6tlich", m. n. „rotliclies
Metall, Kupfer, Eisen" (zu dieser Bed, s. u. ; formell = lat. rufuSj umbr.
rofu^ air. mad, got. usw. raups, lit. ratidas^ aksl. rudz)^ rodhra-^ lodhra- m.
„8ymplocos racemosa, ein Baum, aus dessen Rinde ein rotes Pulver be-
reitet wird", losta- n. „Eisenrost“ (unbelegt, aber gut verbiirgt, Johansson
IP. 19, 124f., wo Gdf. ^reudh-s-to-‘, diese bestritten vonPersson Beitr. 325
Anm., dessen Ankniipfung an arum- „rot“ nicht iiberzeugt) riidhird- „rot,  ;



blutig", n. „Blut" {^rndJi^ro-^ vgl. "^rudhro- in iQv'dqog usw,; wohl nicht
^rudJi-i-ro- mit demselben i wie To}i-i-t{ay^ slav. rzidq, rzditz^ Persson
Beitr. 885);
  gr. egevdco „r6te“ (= anord. rioda)^ egev'^og n. „Rote“ (vgl. lat. ruhor so-
wie unten die auf ^reudh-s^ *rotidh-s, "^rudh-s- beruhenden Bildungen, iiber
welche Persson BB. 19, 269 ff., J. Schmidt KZ. 32, 387 f., Brugmann IF. 6,
103, Johansson IP. 8, 162); egv^Qog „rot“ (==lat. ruber^ u. rufrti^ aksl. rzdrz^
ags. aryderian „erroten“); eovotfir] „Mehltau, robigo" (Ausgang unklar,
nicht nach Niedermann lA. 19, 34 mit dem -go von lat. robt-go zu ver-
gleichen, da dies nicht aus -gV:d -g\p\nes ausgeglichen.
                                           ;                   tJber das nach
Strabo XIII 613 rhodische igv'diprj s. Solmsen KZ. 38, 442; einen mit
^rudh-ro- im Austausch stehenden Zs.-Stamm ^rudh-i^ darin zu suchen, ist
wegen igval^Tj und weil der Ausgang nicht als 2. Zsglied feststeht, wohl
zu gewagt), Igvot-Tiekag „Roteln" {^igvooi-^ ^riidh-s-).
```


## [2026-09-14T01:30:15.644Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"robeus\\|robus, rob\\|rohus\\|robius\" WLD_Bd2_pages.txt | head -10; echo \"=== sed ===\"; sed -n '23725,23760p' WLD_Bd2_pages.txt"
}
```


### [2026-09-14T01:30:15.714Z] TOOL RESULT

```
2508:ahnliche Bed.-Entw. in lat. prohus „gut, tiichtig, braY“, u. profe „probe“ aus
23705:0 aus ^ou lat. robus^ robeus, robins „rot", robigo „Rost; Mehltau, Getreide-
=== sed ===
anord. raudr^ ags, read^ ahd. rot „rot“, anord. raudi „rotes Eisenerz“; anord.
rodra f. „Biut, bes. getoteter Tiere“, rodi m. „Rote“^ rgd n. und rgdr m,
„Rost“, roda „rot sein oder werden“, ahd. rotcn „err6ten‘‘, mhd. rot                  „rot‘^,

ahd. rotamo {^rudhmen-) „R6te“ (hierzu               altn.   rosmofjqil „rotiiche   Berge“?
doch vgl. Bugge Arkfnord. Fil. 1, 11),              ags. rudii   „Rote“, rudig „rotlich“;
ahd. Yosi^mo „Rost^^ (^nidh-s-men)^ ags. rUst^ ahd. as. ro5^„Rost” (^rUdh-S'to-),
—  tiber das von J ohansson IF. 19,124 angereihte ahd. rost            Schei ter-
haufen, Glut, Feuer'‘ s. eine andere Auffassung u.          Schallwurzel.
  Lit. raudas^ raiidonas „rot‘', rauda „rote Farbe*^; rudas „braunrot'‘ (lett.
ruds „r6tlich^^; = mhd. rof)^ rudu „Herbst“, rudeti „rosten^‘, rudis „Rost“,
rudynas, rudynd, rUdyne (Schulze SBprAk. 1910, 791) „Quebbe, Sumpf
mit rotlichem, eisenhaltigen Wasser, Morast, Pfutze, Lache^^; lit. 7'ausvas
(^reiidh-s-tp-  oder "^roudh-s-uo-) „r6tlich“, lett. rusa (^rUdh-s-a) „Rost^^,
lit.        „rotbraun" (pnidh-s-uo-) ^ ruslis „Bratrost“, ruseti ,,glimmen,
        riisvas
brennen^^, lett. rasla „Art rotbrauner Farbe“, lit. rustas „braunlich, lila“
(wohl rudh-s-to-y nicht "^riidh-to-), lett. msia „braune Farbe‘^, rustet „rot
farben“.
    Aksl. rudz    „rot'^,   ruda „Erz, Metall“, rusz {^reudh-s-o- oder '^rondh-s-o-')
„rotlich blond“; rzdrz „rot“, rzdHi sq „sich roten^',            rzMa „Rost“, russ. rysyj
„r6tlich blond“ {^rudh-s-o-^ vgl. lett. rasa),
       CurtiusS 252, Fick I^ 116, 298, 526, III* 351.
   Persson Wzerw. 48, 123 Anm. 2, 237 f. halt reudh fur Erweiterung eines
*(e)reu-, das aber durch die darauf bezogenen Worte nicht sichergestellt
wird;
   ai. ravi- ^Sonne^, arm. (Hubschmann Arm. St. I 21, Arm. Gr. I 424)

arev ,,Sonne‘‘ (ir. re „Raum, Zeit, Mond^^, Stokes KZ. 35, 596 hat damit
nichts zu tun) kann, muB aber nicht ais „die Rote'' gedeutet werden;
ai. arimd-, arum- „r6tlich“, av. annisa- „vreifi“ scheint eher von „geiblich,
orange" auszugehn und zu idg. *6^-, "^eluo- „gelblich" zu gehoren. Auch
die vermuteten Erweiterungen *reu-d- und ^reu-t- haben keine Gewahr;
fiir die Annahme,    daS lat. rudis „roh, unbehauen" eigentlich „biutig, roh
vom Fleische'* bedeutet babe, bietet seine Yerwendung keinen Anhalt (s.
Persson Beitr. 299); lat. raudus, rodiis, rudiis „ein formloses Erzstiick als
```


## [2026-09-14T01:30:31.208Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n \"rōγn\\|royn\\|rōy\\b\\|rōd \\|rōdīk\\|rodik\" NYB_vol2_glossary.txt | head -10; echo \"=== LKT ronas ===\"; grep -n -i \"ronas\\|runas\\|Krapp\\|alizarin\" LKT.txt | head -10; echo \"=== SKT reek/ream ===\"; grep -n \"^Reek\\|^Ream\\|^Red,\\|^Rust\\|^Ramekin\" SKT.txt | head -10"
}
```


### [2026-09-14T01:30:31.307Z] TOOL RESULT

```
=== NYB ===
=== LKT ronas ===
483:[Vom  Vb.  'asara  'pressen']  'der  Saft, der  durch  Pressen  aus  einer  Pflanze gewonnen  wird' ;  hieraus  sp.  frz.  alizari als  Handelsausdruck  für  garance  'Fär- berröte, Krapprot'  und  weiter  der  che-
486:mische  Ausdruck  Alizarin  zur  Bezeich- nung bestimmter  Farbstoffe;  frz.  alisa- rine.  Alizarintinte  wurde  i.  J.  1855 zuerst  in  Dresden  hergestellt.  [Devic DEt  23.    Lammens  Rem  15.
5708:.4?awrtc  St.  75 Albatros  1)88 Alchabor  St.  12 Alchimie  1157 Aldebaran  St.  451 Aleppin  792 Algebar  St.  629 Algebra  631 Algedi  St.  035 Algenib  St.  664 Algomeiza  St.  749 ^Z^^oZ  St.  741 Algorab  St.  754 Alhabor  St.  12 Alhajoth  St.  41 Alhidade  896 Alizarin  116 Alkakandschi  1016 ^ZA-«?i  1029 ^/fro/io?  1227 Alkoran  1250 Alkoven  1221 ^/^«/t  59 Alleluja  793 alligaßr  mhd.  2229 Abnagest  1348 Almanach  1389 Almemor  j.  1461  a Alphard  St.  587 Alpherath  St.  586 Alpheraz  St.  586 Alpheta  St.  574 ^/<«/r  St.  1575
=== SKT reek/ream ===
15774:Reek,  vapour.  (E.)  M.  E.  rtke.  \,  S. r/f,  vapour.  — A.  S.  rtdt,  pt.  t.  of  rttkatt (strong  veib),  to  reek,  smoke.  (Bai« kUK.)  +  Du.  n»Jb,  Icel.  reyJir.  Swcd. ri/k.  Dan.  rUg;  G.  raufh ;  cf.  Icel.  tjiiht, (pt.  t.  raui),  G.  rieehtn,  to  smoke,  reck. Orig.  •  dinmess ;'  cf.  Skt.  raja,  rujtu, dimness,  rajatti,  night,  rauj,  to  djrc.
16326:Rustic.  (F.-UI  F.  rttx/»^.-L, ttcus,  beloDging  to  the  counti)'. «- 1,  iai country.  Qf.  Knss.  raviifUL,  a  plain, « nxvan,  n  plain.
16329:Rustle  ;  see  Bouao  (1)*
```


## [2026-09-14T01:30:39.511Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT ===\"; grep -n -i \"^Red\\.\\|^Red,\\|^Rust\\.\\|^Rust,\\|^Ream\\|^Ruby\\|^Rouge\" SKT.txt | head -10; echo; grep -n -i \"Ruddy\\|Ruby,\" SKT.txt | head -5"
}
```


### [2026-09-14T01:30:39.601Z] TOOL RESULT

```
=== SKT ===
9475:red.  ptffa,  to  move  up  and
10388:red,  esp.  from  all
15759:rust.  ^E.)  A.  S.  rwi/,  rust ;  orig.  red* ness.  Allied  to  A.  S.  rudu,  ruddiness,  and redd^  red.^Du.  roest,  Dan.  nw/,  Swed.  G. rat.
16259:Ruby,  a  red  gem.  (F.— L.)  O.F.  nthi. rulfis ;  F.  rubii  (where  /  is  the  old  sign of  the  nom.  case).  Cf.  Span.  rubi.  rubin. Port,  rubim,  Itat.  rubino.  —  Low  L,  rvbiuMs, a  ruby ;  from  its  colour.  «•  L.  ruber,  red  ; rubtrt^  to  be  red.  Allied  to  L,  mfus,  red ; and  to  K  BodL
16261:rouge,  red  point.  (F.  -  L.)     F.  rou^,
16262:red.  —  L.  rubfus,  red ;  (whence  F,  rtmgt,

16259:Ruby,  a  red  gem.  (F.— L.)  O.F.  nthi. rulfis ;  F.  rubii  (where  /  is  the  old  sign of  the  nom.  case).  Cf.  Span.  rubi.  rubin. Port,  rubim,  Itat.  rubino.  —  Low  L,  rvbiuMs, a  ruby ;  from  its  colour.  «•  L.  ruber,  red  ; rubtrt^  to  be  red.  Allied  to  L,  mfus,  red ; and  to  K  BodL
16265:rubicund,  ruddy.  (F.-L,)  T.nthintndi.
16322:Ruflset.  (F.-L.)  M.  E.  russet.  -  F. rvMssr/,  'russet,  ruddy;*  Cot  Dimin.  of F.  ra$tjc  (iem.  mM//)»  reddish.  «L.  russvs.
```


## [2026-09-14T01:30:45.023Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"روغن\\|روناس\\|رویین\" ARY_pages.txt | head -10; echo \"=== latin index ===\"; grep -n -i \"REUDH\\|REUG\\|RAOGHNA\\|ROGHAN\\|RAOGNA\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T01:30:45.111Z] TOOL RESULT

```
9197:روغن / ۳۱۳
=== latin index ===
1499:EREUGOMAI GREEK) hy ORCAM, ORUCAM :(ARMENIAN) .g,!
1516:MALLORY & ADAMS: HREUG ROCETTAN
9014:ROUM y RAOGHNA, AVESTAN) glen 3) ‘
9016:REAM — (OLD ENGLISH) pS gsSsl ROGHAN, ROVN, — (PAHLAVI) «5 ly
9020:MACKENZIE: (OIL) 125 ROGHAN
```


## [2026-09-14T01:30:48.503Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '9005,9030p' ARY_latin_index_pages.txt; echo \"=== ARY page for روغن ===\"; awk 'BEGIN{RS=\"\\f\"} /روغن \\/ ۳۱۳/ {print \"LEAF\",NR}' ARY_pages.txt; echo \"=== ereug ===\"; sed -n '1490,1520p' ARY_latin_index_pages.txt"
}
```


### [2026-09-14T01:30:49.709Z] TOOL RESULT

```
AMINDAROV: (LIGHT) 249 (OLD HIGH GERMAN) pS gall
VPA sb oby LIOCH :
LICHT (GERMAN) giaST
=
[pdf page 312]
YY f gtsy
setloal
het aly oat Nis "oat" “okt” "ty SS eulh class
fe eam li |
ROUM y RAOGHNA, AVESTAN) glen 3) ‘
RAHM GERMAN) glaST RAOGAN 1
REAM — (OLD ENGLISH) pS gsSsl ROGHAN, ROVN, — (PAHLAVI) «5 ly
ROGHN
‘REFERENCES both, RUN (KURDISH) (53,5
POKORNY ~*~: ROGAN, ROGUN, — (BALUCHI) x 4h i
MACKENZIE: (OIL) 125 ROGHAN
AMINDAROY: (BUTTER) 195 OLD SCANDINAVIAN) 34Sis.isa
4VA [booby RIUM! t
1(OLD HIGH GERMAN) pS glST
i
. dentiloal
capt NE GIT 2 ajly gl m
|
LIA (4LEX(OLD IRISH) oy 5433p) RAEC., RAECAYATI.(AVESTAN) (plea)
LLIANT (4LX(WELSH) 55 APAHLAV) Sly, ow
LUM (4LEYALBANIAN) gl REXTAN, WEXTAN, REZ. REZISHN ©“ |
=== ARY page for روغن ===
LEAF 312
=== ereug ===
SKEAT: (ALVEOLAR) 17 ALVEOLUS (ENGLISH) (3 j)),5-aSt
rr eG oby (OLD CHURCH SLAVIC) 46 53%!
4 Haas aalicndl ULYJ
Jeetloak
Les aT Bly ga olan ae U oT alt 4) BLVARA tol gate BLS GF 32 ojly oy! JS“
98m gate gely gal eghysT” seal) 4 beth erly 5h pS gen y2 Seed dF 4 PHY (eet JST
eee oa a LBL laced ots gi onl (Ve GAdone) Manna Gaubca 59 gly Coed oath gla! |
eayla IB OT 52 alsin 5 eS oa i> diy oie oa 9 SU BIOL) vy ool eT
_ 3985 6A gle) O45 2 a alg
EREUGOMAI GREEK) hy ORCAM, ORUCAM :(ARMENIAN) .g,!
[pdf page 55]
. ea dhsfdt | oF
(OLD CHURCH SLAVIC) 4S 63%! RUCTUS, RUCTARE, = (LATIN) 3Y
RYGAJO . ERUCTARE- ERUGO
RYGATI . ARUSSIAN) y+ ROT, ERUCTER, (FRENCH) 4
oy @RIAUGM,” LITHUANIAN) ips ERUCTATION
RUGIU ERUCTO, (SPANISH) gl het
RUBENIS LATVIAN) (3) isd ERUCTARE
RUCTAN :(OLD PRUSSIAN) (AS 53.4 RUTTO, RUTTARE :(/TALIAN) plu!
ARROTO PORTUGUESE) Js 4
REFERENCES beth OLD SCANDINAVIAN) 5.5 hes\
poKomY: —~~OS~*~*~*~*~«SNST ROPA, RYPTA
DELAMARRE: (ROTER) 277 (OLD HIGH GERMAN) jy gilt
ONIONS: (ERUCTATE) 324 RUFEZZEN :
SKEAT: (ERUCTATE) 119] RULPSEN GERMAN) gist
TAUPMAN: (BELCH) 470 HOLD ENGLISH) pS gS
MALLORY & ADAMS: HREUG ROCETTAN
ERUCTATE ENGLISH) 55S
RYPE, RJUPTA — :(NORWEGIAN) 5353
leatlaay
OS ithe aol al gant
```


## [2026-09-14T01:31:00.979Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n -i \"RAOIDITA\\|ROY, \\|RODIK\\|RONAS\\|ROYNAS\" ARY_latin_index_pages.txt | head -10; echo \"=== persian ===\"; grep -n \"روی / \\|روناس / \\|آروغ / \" ARY_pages.txt | head -10"
}
```


### [2026-09-14T01:31:01.057Z] TOOL RESULT

```
10637:SAIR, SROY, SUR (ARMENIAN) <I
=== persian ===
```


## [2026-09-14T01:31:03.590Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"روی\\b\\|روناس\\|آروغ\" ARY_pages.txt | head -15; echo \"=== leaf 312/313 persian ===\"; awk 'BEGIN{RS=\"\\f\"} NR==313' ARY_pages.txt | head -30"
}
```


### [2026-09-14T01:31:04.634Z] TOOL RESULT

```
48:تفریباً همه‌ی زبانهای اروپا و فلات ایران و بخش شمالی شبیه قاروی هند می‌شود. کوچگری
240:۱ وجود دارد و این زبانها نیز (به ویژه پارسی کهن و اوستایی) شباهت زیادی با زبانهای شبیه قاروی.
313:بیشتر روی همریشگی تاکید دارد نه هم چمی.
325:در درون گور ساخته شده از سنگه‌های تراشیده شده قرار دارند و روی گور تپه‌ی کوچکی
414:چیز دیگری که دریافتند این بو که هر چه به عقب برویم شباهت زبانها بهم پیشتر می‌شود. مثلاً
514:انگلیسی سرویلیام جونز (1746-94 ,۷۷11۸۸120188 814) رسماً بیان شد. او در نطق معروفی
535:رو با زبانهاي یافثی اروپا خویشی دارند. این وضع ادامه داشت تا اینکه دیدمان فرگشت چارلز داروین
580:نداشته تعیین دقیق آوا و معنی واژه‌های هند و اروپایی بنیادین فقط از روی پیگیری پسگرایانه و
583:بودن واژه‌ی بازمازی شده را نشان دهند. (درکتاب حاضر نیز از این رسم پیروی شده است). . "
586:دیگر از زبانشناسان معتقدند که واژه‌های بازسازی شده با پیروی از اصول اثبات شده‌ی زبانشناختی و
615:کمتری یافت شده است. این مدارک وابسته به دوران برنز بوده و منحصرند به نوشتارهای روی سنگه
616:قبر و روی گنجانه‌های سفالین. وجود گورهای برجسته (1)1180۸) و آثار ویرانی ساختمان‌ها و
722:بخش‌های دیگر اوستا در سده‌های بعدی نگاشته شده‌اند. رویهم رفته اوستای اپرانیان و ودای ِ
887:بیاوروی ۳ب ایساندن
1089:ابدی بود. آنان با پیروی از آرمان‌های ی که در صدر آن جوانمردی و مروت و شجاعت قرار داشت در
=== leaf 312/313 persian ===
[pdf page 313]
۴ / ریسیدن» ریشتن» رشتن
بادداشت:.
۱ بازگشت به: گرپختن.
۲ چم این واژه در زبان ایرلندی کهن: سبل. 0
چم این واژه در زبان‌های ولزی و آلبانی: رود. رون
چم این واژه در زبان لاتین: آب شدن, ۲ :
۳ واژه‌ی "ریدن" نیز از همین واجریشه است.
پهلری (7ا#ل۳۸): 318711۸0 ,318177۸0
ارستی (05387/6): ,۸15511 پسگشت‌ها ۲۵۸۲2۳2/۵5
۸1 رن
کردی (70157ا6): ,8187 5 (573186) :۱/۸0/25
پلوچی (/007/: ۰ 338۸0 ,۸35۸617 9 (8187) :۸4200
سانسکریت (5480077): 115471 برهان قاطع : ۱۹۵۱۸
یرنانی (0620): زد اف دی ادا
بادداشت:
چم اين واژه در زبان پهلوی: ریسمان؛ رشته‌ی نخ.
چم این واژه در زبان یونانی؛ ریز ریز با پاره پاره کردن,
۱
اوستایی (4۲587۸400): 15 ۸ ۳
آلهتاکگفط ,۰1۸۹۷8۲۲ آلمانی مبانه (الفلن022 بزهاتز ها0طزیم:
پهلری (۲7ابلم): اند 7 ,815780 ا
کردی (073]7(): 15 آلمانی (/688214): 85 7725۸ ۱
بلوچی (31لعناءلم8): 1 اسلاوی کهن (ع۲7ما 7ل#6ناتل) صا0):
سانسکریت (5۸/5877): دی وان ۱
1 8157۸ ,835۸71 لتونی (لنی) (/2 7 ا): 23515 ۱
ایسلند یکهن (1010471۵2۷نمع5 صاه): یلا۱1 ۱
```


## [2026-09-14T01:31:08.974Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '9185,9215p' ARY_pages.txt"
}
```


### [2026-09-14T01:31:09.029Z] TOOL RESULT

```
ایتالپایی (۵۸لله7): 11 4 (7617) :مه
رومانی (۸/۸/1۸(1): 111۸ 7 ,185 :0245
گوتبک (00717/0): 1 ۱ :۸2لا
ایسلند یکهن (0/07۸12/(مع9 00): 1 010113 ,105 (831613) "
58 156۴ 5 ,991 ,60 ۸
ساکسونی کهن (5400/0 طا0): ۰ 1101۳ 7 101117 :002/5
فریزی کهن (/(94ل28 ضا0): ۰ 11۸0737 0 (3011) :57
آلمانی کهن (6880/۸0 71017( صا): 9 (136171) ۸4/۸
۱ 1100 برهان قاطع + ۹۷۶-۷
آلمانی (05704۸(0): 117
۳
[pdf page 312]
روغن / ۳۱۳
یادداشت
واژه‌های فارسی "آرخش " و "درخش" و "درخشیدن" و آرخشیدن" نیز از همین واجریشه‌اند.
:
| چم‌انگلیسی سرواز‌ی فارسا سا ۱0۷6
۱ اوستایی (4۷587/40): ,0011۸ 5 0
۱ ۸06۸7 آلمانی (/(657244): انا تا
پپلری (/4۲اط۸ :۰ ,80۷0 ,803613۸ انگلیسی کهن (34ا2/0 ۰:01 22۸36
8001
کردی (7015): ۸1 پسگشت‌ها 0/5
بلوچی (زبق‌ت۸ق: ۰ ,3301000 ,330۸81 5 ۸0/0000
لداا نی 5 (ا[0) :۸2/5
ابسلندی‌کهن ((0۸14/ مک (ل0): 5 (817788) ۸/0
۱ (ارایرد برهان فاطع + ۹1۸
آلمانی کهن (/(062۵14 03ج صمان):
ا
یادداشت: ۹
چم این واژه در آلمانی: خامه» سرشیر,
ِْ
```


## [2026-09-14T01:31:20.866Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/red",
 "prompt": "Quote the etymology of \"red\": Old English read, Proto-Germanic *rauthaz, PIE *reudh-."
}
```


## [2026-09-14T01:31:21.904Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rust",
 "prompt": "Quote the etymology of \"rust\": Old English rust, Proto-Germanic *rusta-, PIE *rudhso-/*reudh-."
}
```


### [2026-09-14T01:31:25.856Z] TOOL RESULT

```
# Etymology of "Red"

The word "red" traces back through several linguistic layers:

**Old English:** The term derives from Old English *rēad*, which described various shades including "purple, crimson, scarlet, pink" and also referred to "red clothes, dye, ink, wine, or paint."

**Proto-Germanic:** It comes from Proto-Germanic *rauthan*, found across Germanic languages like Old Norse *rauðr*, Danish *rød*, and German *rot*.

**Proto-Indo-European:** The ultimate source is reconstructed as PIE *reudh-, meaning "red, ruddy." As the entry notes, this represents "the only color for which a definite common PIE root word has been found."

**Related words:** This same root produces English derivatives including ruddy, rust, ruby, rubric, and russet—demonstrating how deeply this color term penetrated Western vocabulary.

The long vowel sound shortened during or after Middle English, which is why surnames like Reid and Read preserve the original Old English pronunciation, while the modern adjective uses the shorter vowel sound.
```


### [2026-09-14T01:31:27.353Z] TOOL RESULT

```
# Etymology of "Rust"

Based on the Online Etymology Dictionary, here's the etymological journey of "rust":

**Noun form (Old English origin):**
"Red oxide of iron, red coating which forms on the surface of iron exposed to the air," the word traces back to Old English *rust*, connected to *rudu* meaning "redness."

**Language lineage:**
The term descended through Proto-Germanic *\*rusta-* and ultimately derives from the Proto-Indo-European root *\*reudh-s-to-*, which literally means "red, ruddy." This same PIE root also produced related words like Lithuanian *rustas* and Latin *robigo*.

**Verb form:**
The verb usage emerged in the early 13th century (*rusten*) with the meaning "become rusty" for metals. The figurative sense—referring to deterioration from disuse—appeared by the early 14th century.

**Modern compounds:**
The slang term *rust-bucket* for old vehicles emerged by 1945, while the *Rust Belt* designation for declining industrial areas gained prominence through Walter Mondale's 1984 presidential campaign.

The word's color-related etymology connects it to a broader family including "red," "ruddy," and "ruby."
```


## [2026-09-14T01:31:29.024Z] AGENT

Now let me archive all the web sources.


## [2026-09-14T01:31:34.651Z] TOOL CALL #71: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/روغن\" \\\n \"https://en.wiktionary.org/wiki/روی\" \\\n \"https://en.wiktionary.org/wiki/روناس\" \\\n \"https://en.wiktionary.org/wiki/آروغ\" \\\n \"https://en.wiktionary.org/wiki/رژ\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁rewdʰ-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁rewg-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ráwgnah\" \\\n \"https://www.etymonline.com/word/rouge\" \\\n \"https://www.etymonline.com/word/ruby\" \\\n \"https://www.etymonline.com/word/reek\" \\\n \"https://www.etymonline.com/word/red\" \\\n \"https://www.etymonline.com/word/rust\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 424 (book 394): roots Reudh 1, Reug, Reughmen — verification of rūy/ronās/roğan/āroğ/rouge/ruby/red/rust/reek\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T01:31:41.894Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b148c364fad56117.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/135591967eac9e57.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cefe25bdac7c6273.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/04f34ce46ea8e7b8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb2f4b4ecc257411.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ccc1369772f48c60.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0f109c10edfa730.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4e7ab3eb85b9565b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d9b539e46a2ba8c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf15eca3ca17bf04.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/82f7186a2bc674a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a16c07da66c5fa88.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05832367079b553d.txt
```


## [2026-09-14T01:31:49.247Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg424.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/424.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/424.png\ncd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FRS روین ===\"; grep -n \"روین\\|روغنای\" FRS_pages.txt | head -5; echo \"=== MON abridged روغن ===\"; grep -n \"^روغن\" MON_part2.txt MON_part1.txt | head -5"
}
```


### [2026-09-14T01:31:50.293Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74989 Sep 13 21:31 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/424.png
=== FRS روین ===
6689:                                         ‫روینه الت و مس‬               ‫‪:‬ر‬
9787:      ‫بجای در پروین بنته در آبش‬           ‫بجای تنعل ماهی بسته برپای‬
11712:  ‫‪ - ۸‬لْ ‪ :‬استرنك نبانی بودیصورت مردم روید‬            ‫‪ - ۷‬چ ‪ ۰‬بر فلك بیدا شودیروین‬
15395:                                              ‫پروین بود [فرخی گوید‬
15418: ‫‪ :- ۲‬چون ریا ک[ذا]‬            ‫‪ ۵ - ۱‬برن ستارة پروین است » سایر ی‬
=== MON abridged روغن ===
MON_part2.txt:3003:روغن از کوبین بیرون آید. هاون چوبین با 
MON_part2.txt:8826:روغنی هم می‌گیرند که در عطرسازی بکار 
MON_part2.txt:13276:روغن داغ کرده و آنها را در روضن سرخ 
MON_part2.txt:16057:روغنی و فرار که به مقدار بسیار کم چند لیتر 
MON_part2.txt:16632:روغن سرخ کنند. سپس ۲۰۰ گرم له
```


## [2026-09-14T01:31:54.216Z] TOOL CALL #73: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:31:54.346Z] TOOL RESULT

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


## [2026-09-14T01:33:03.101Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN rogan ===\"; grep -n \"röyan\\|royan\\|rögan\" HRN.txt | head -5; echo \"=== ARY aroq ===\"; grep -n \"آروغ\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== MON rozh ===\"; grep -n \"^رژ\\|رژ لب\\|رژلب\" MON_part1.txt MON_part2.txt | head -5; echo \"=== FRS royin ctx ===\"; sed -n '6685,6692p' FRS_pages.txt"
}
```


### [2026-09-14T01:33:03.223Z] TOOL RESULT

```
=== HRN rogan ===
5612:aw. raoyna- 'Ol'; phlv. rökan (d. i. röyan^ päz.
5613:raoyftn), royan (PPGL).
5614:kurd. rrin\ bei. (LW. ?) rogan^ rögan, n. röya/i,
20726:rögan 632.
20727:. n. röyan 632.
=== ARY aroq ===
=== MON rozh ===
MON_part1.txt:67204:رژد: 72۵ (- رزد - رس] (ص.) 
MON_part1.txt:67207:رژه: (29)0[- رجه - رده طبر» دامغانی؛ 
MON_part1.txt:67220:رژیسم: ۳029 آطرز» قاعده» روش ] ).( 
=== FRS royin ctx ===
‫ود ‪ ۰‬لا‬    ‫و مس که آنرا بارزیر برلحام برهم زنند کفشیر‬              ‫‪ :‬کفشر روی‬     ‫س‬    ‫‪۳‬‬
 ‫بارزیز بندند و دوشانند[ ص ‏‬     ‫ودان‬
                                    ‫اهنن‬
                                       ‫مین‬
                                         ‫روینه الت و مس‬               ‫‪:‬ر‬
                                                                       ‫)ب‬‫فهش‬
                                                                           ‫کشی‬
                                                                             ‫( در حا‬
```


## [2026-09-14T01:33:05.703Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5605,5620p' HRN.txt; echo \"=== which leaf/page ===\"; awk 'BEGIN{RS=\"\\f\"} /aw.  raoyna-/ {print \"LEAF\",NR}' HRN.txt"
}
```


### [2026-09-14T01:33:06.795Z] TOOL RESULT

```
ap. vergl. hoidv/]^); aw. ruoysna' 'leuchtend'; phlv.
rosan^ rösanili, roSnäk, arm. LW. r. s/iakuH, rösnntitin,
LW. af/. rö/cifi, rö/näl; bei. rösani^ rösanal (324);
si;n. rosnagd 'Tageslicht*, sangl. rösnäi 'Feuer.
Vergl. No. 610.
632. röyen ^Butter, Öl*.
Käs. rüyän, rö.
aw. raoyna- 'Ol'; phlv. rökan (d. i. röyan^ päz.
raoyftn), royan (PPGL).
kurd. rrin\ bei. (LW. ?) rogan^ rögan, n. röya/i,
röyin (327); LW. wa;<. rilgfi, royim, minj. royün,
sangl. röy, sar. rdim,
633. vom, röme 'Schamhaare', nun, riimbe (geschr. rnnhe)').
ai. roman- 'Haar am Körper der Menschen und
Tiere' (in der Regel mit Ausschluss der langen Kopi-
und Barthaare).
=== which leaf/page ===
```


## [2026-09-14T01:41:27.579Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-424.json <<'JSONEOF'\n{\n  \"pdf_page\": 424,\n  \"book_page\": 394,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Reudh 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₁rewdʰ- 'red, ruddy' (Pokorny reudh- 872-873; Watkins reudh-1)\",\n      \"note\": \"Root, language label, gloss and page reference are all correct. Pokorny IEW 872-873 heads the entry 'reudh- ,rot'; roudho-, rudh-rō-, rudhio-, rudh-so- ds.' and lists exactly the Indo-Iranian, Italic and Germanic material Nourai draws. Buck (Selected Synonyms 15.66, p.1056) calls *reudh- the inherited IE word for 'red', and Etymonline notes it is 'the only color for which a definite common PIE root word has been found'. The laryngeal-notated modern shape is *h₁rewdʰ-. The one substantive problem on this chart is the Latin box (see node #4) and the origin of ronās (node #3).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₁rewdʰ- «سرخ، سرخ‌فام» (در نگارش قدیم‌تر *reudh-) درست است؛ پوکورنی در صفحهٔ ۸۷۲–۸۷۳ فرهنگ ریشه‌شناسی هندواروپایی همین ریشه را با همین معنی و با همان گواه‌های هندوایرانی، ایتالیک و ژرمنی آورده است، و باک نیز آن را تنها نام رنگی می‌داند که برای آن ریشه‌ای مشترک و مسلّم در هندواروپایی بازسازی شده است. برچسب زبانی «هندواروپایی»، معنای «سرخ» و ارجاع POK:872 هر سه درست‌اند. دو نکتهٔ کاستی در این نمودار، جعبهٔ لاتینی rôbeus (که سرچشمهٔ rouge و ruby نیست) و ریشهٔ «روناس» است که پژوهش امروزی آن را وام‌واژه‌ای یونانی می‌داند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁rewdʰ-\",\n        \"https://www.etymonline.com/word/red\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:872\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.872 (POK_03.txt leaf 108-110, running page numeral '873' visible on leaf 109): 'reudh- ,rot^; roudho-, rudh-rō-, rudhio-, rudh-so- ds. Ai. rōhita- = av. raoiδita- ,rot, rötlich^ ... lat. rubidus ... aisl. rauðr, ags. rēad, ahd. rōt ,rot^ ... ags. rūst, ahd. as. rost ,Rost^ (*rudh-s-tó)'. Entry runs 872-873, exactly Nourai's page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 358 f.\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt l.23674 'reudh- „rot“. Ai. rōhitá- = av. raoδita- „rot, rötlich“ ... gr. ἐρεύθω ... lat. ruber ... got. usw. rauþs' — the source Pokorny himself cites (WP. II 358 f.).\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reudh-1\", \"stance\": \"supports\", \"note\": \"'reudh-1. Red, ruddy. I. O-grade form *roudh-. 1. Germanic *raudaz in: a. Old English rēad, red: RED ... II. Zero-grade *rudh-. 2. Suffixed form *rudh-sto- in Germanic *rūst- in Old English rūst, rust: RUST. 3. Latin rubeus, red: ROUGE, RUBEOLA, RUBY. [Pok. reudh- 872.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 15.66 RED, p.1056\", \"stance\": \"supports\", \"note\": \"'1. IE *reudh-. Walde-P. 2.358 f. ... Lat. ruber, and (dial.) rufus ... also Lat. rubeus ‘reddish’ (> Fr. rouge, etc.) ... Skt. (Vedic) rohita-, later lohita-, Av. raoiδita-.'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.vv. reudhos / roudhos\", \"stance\": \"supports\", \"note\": \"IEC.txt ll.14551-14553, 14769: 'reudhō ‘make red; redden’', 'reudhos ‘red; redness’', 'roudhos ‘red, russet’. Cf. reudh-, rudh-. WP II, 358'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"raoidita\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan raoiδita- (Nourai's 'raoidita' = raoiδita-, δ transliterated d) is an adjective 'red, reddish', the exact formal match of Vedic róhita- 'red', both from PIE *h₁réwdʰ-it-os > Proto-Indo-Iranian *Hráwdʰitas: the full grade *rewdʰ- is kept, PIE *dʰ gives Indo-Iranian *dʰ, which in Avestan becomes the voiced fricative δ between vowels, and *-itos yields the deverbal/denominal -ita- suffix. The word is attested in Vidēvdād 1.2, where the evil spirit creates for Airyana Vaēǰah 'the red(-coloured) serpent and the daēva-made winter'; Bartholomae also lists raoiδita- as the name of a mountain. Nourai's gloss 'red' and the language label are correct.\",\n          \"derivation_fa\": \"صفت اوستایی raoiδita- «سرخ، سرخ‌فام» (نویسهٔ d در کتاب همان δ اوستایی است) دقیقاً برابر سنسکریت ودایی róhita- «سرخ» است و هر دو از هندواروپایی آغازین *h₁réwdʰ-it-os و هندوایرانی آغازین *Hráwdʰitas می‌آیند؛ dʰ هندوایرانی در اوستایی میان دو واکه به سایشی واک‌دار δ بدل می‌شود و پسوند -ita- صفت‌ساز است. این واژه در وندیداد ۱٫۲ («مار سرخ و زمستان دیوآفریده») آمده و بارتولمه آن را نام کوهی نیز ثبت کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁rewdʰ-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:872\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 108 (p.872): 'Ai. rōhita- = av. raoiδita- ,rot, rötlich^' — precisely the node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb., s.v. raoδita- (Mo'in's Borhan footnote cites col. 1495)\", \"stance\": \"supports\", \"note\": \"BRT.txt l.24952: '• j. raoδita- Adj. ,rot, rötlich‘: airyanǝm vaēǰō ... āat ahe paityārǝm frākǝrǝntat aŋrō mainyuš ... ažimca yim raoiδitǝm zyąmca daēvō.dātǝm V. 1.2. a) m. Name eines Bergs oder Gebirgs'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 15.66 RED, p.1056 table and §1\", \"stance\": \"supports\", \"note\": \"Buck's table lists 'Av. raoisita-' (OCR for raoiδita-) as the Avestan word for 'red' under IE *reudh-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 358\", \"stance\": \"supports\", \"note\": \"'Ai. rōhitá- = av. raoδita- „rot, rötlich“, rōhit- „rote Stute“ ...'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"rôdîk, rôy\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The forms are real and the descent from the 'red' root is the standard view, but the gloss is anachronistic. Old Iranian *rauda-/*raudi- 'the red (metal)' — the same colour-from-metal naming as Sanskrit lohá- 'reddish; red metal, copper, iron' — gives Middle Persian rōd, in Book Pahlavi written ⟨lwt(y)k'⟩ and read rōdīg/rōtīg, beside the later form rōy (⟨lwd⟩), with intervocalic -d- weakening to -y- before the New Persian period; the derived adjective rōyēn ⟨lwdyn'⟩ 'brazen, of copper' is well attested. Horn no.635 gives exactly 'phlv. rōdīk geschr. rōtīk (Vd. 1(8)), rōd bezw. rōi (AV.), rōyīn (AV.)', which is Nourai's pair. MacKenzie glosses *rōy 'copper, brass' and lists brinj and rōy as the two Pahlavi words for 'brass'; Wiktionary/Edelʹman derive MP rōy from Proto-Indo-Iranian *Hrawdáh 'copper, brass'. So the metal meant is copper/brass, not zinc: 'zinc' is the modern chemical sense that Persian روی acquired only in the 19th-20th c. Note also a minority dissent (Mann, after H. Pedersen) that Pahlavi rōd 'copper' is ultimately a culture-word from Sumerian urudu 'copper' rather than an inherited *reudh- derivative.\",\n          \"derivation_fa\": \"هر دو صورت واقعی‌اند و پیوندشان با ریشهٔ «سرخ» دیدگاه پذیرفته‌شده است، ولی معنای «روی/زینک» در نمودار نابه‌هنگام است. از ایرانی باستان *rauda-/*raudi- «فلز سرخ» ــ همان الگوی نام‌گذاری که در سنسکریت lohá- «سرخ‌فام؛ مس، آهن» دیده می‌شود ــ فارسی میانهٔ rōd پدید آمده که در پهلوی کتابی ⟨lwt(y)k'⟩ نوشته و rōdīg/rōtīg خوانده می‌شود، در کنار صورت متأخرترِ rōy ⟨lwd⟩؛ دالِ میان دو واکه پیش از دورهٔ فارسی نو به «ی» نرم شده است و صفت rōyēn «رویین، مسین» نیز گواه است. هرن (شمارهٔ ۶۳۵) دقیقاً همین جفت «rōdīk (نوشتهٔ rōtīk)، rōd/rōi» را می‌آورد و مکنزی *rōy را «مس، برنج» معنی می‌کند. پس فلزِ مورد نظر مس/برنج است نه روی؛ معنای شیمیاییِ «روی» تنها در سدهٔ اخیر به این واژه بار شده است. مان (به پیروی از پدرسن) احتمال داده است که rōd پهلوی سرانجام وام‌واژه‌ای از سومری urudu «مس» باشد؛ این نظر اقلیت است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/روی\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1695\", \"status\": \"not_checked\", \"note\": \"Mo'in's six-volume Farhang-e Farsi is not online with its print pagination (only a two-volume abridgement on archive.org, which has no page mapping and no روی 'brass' entry with the Latin-script forms). Mo'in's own etymological footnote in the same author's Borhan-e Qate' (vol. 2 p.981, BQT_v2_pages.txt leaf 444) does give this chain: 'از او[ستا] raoiδita- (سرخ رنگ) «بارتولمه ۱۴۹۵» ... بلوچی rōd ... ارمنی ... (برنج) رک: هوبشمان', i.e. the same derivation Nourai attributes to MON:1695.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.72 s.v. *rōy; p.26 'brass'\", \"stance\": \"partial\", \"note\": \"PHD.txt l.559: '*rōy [lwd | M rwy, N ~] copper, brass'; 'rōyēn [lwdyn' | M rʾwyn, N rōyin] (made of) copper, brazen'; English index l.1070 'brass brinj, rōy'. MacKenzie's rōdīg [lwtyk'] is a different word ('intestine, gut'), so 'rōdīk' as a metal-name rests on Horn's reading of Vd. 1(8), not on MacKenzie.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 635, p.141\", \"stance\": \"supports\", \"note\": \"'635. (i)rōy, rō ,Kupfer^, rōyīn. aw. raoiδita- ,rötlich^ (vd. 1, 3); phlv. rōdīk geschr. rōtīk (vd. 1 (8)), rōd bezw. rōi (AV.), rōyīn (AV.); skr. lohá- ,rötlich, Roterz, Kupfer^. bel. rōd ,Kupfer^ (325).' — Nourai's two Pahlavi forms verbatim; Horn's gloss is 'Kupfer', not zinc.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 2 p.981 (leaf 444), Mo'in's footnote to روی\", \"stance\": \"supports\", \"note\": \"'... از او[ستا] raoiδita- (سرخ رنگ) «بارتولمه ۱۴۹۵» ... بلوچی rēd/rōd ... ارمنی ... (برنج) رک: هوبشمان.'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. roudhos\", \"stance\": \"partial\", \"note\": \"IEC.txt l.14769: 'NB. According to H. Pedersen Sumerian urudu “copper” is the prototype basis of Pahlevi rōd, id. and of Lat. raudus “metal ingot for coining” and ON rauði “bog-iron”. The Latin vocalism suggests borrowing' — a dissenting, non-Indo-European account of exactly this Pahlavi word.\"},\n            {\"src\": \"FRS\", \"where\": \"Loghat-e Fors s.v. روین\", \"stance\": \"supports\", \"note\": \"FRS_pages.txt l.6689: 'روین: الت و مس' — the old lexicon glosses روین as (the metal of) brass and copper, not zinc.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"rŭy 2; ronâs\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two words, with different fates. (a) روی rūy 'copper/brass (mod. zinc)', with رویگر 'brazier', رویین/رویینه 'of brass' — confirmed: MP rōy < Old Iranian *rauda-/*raudi- < PIE *h₁rewdʰ-, the metal named from its colour exactly as Skt. lohá-; the New Persian form simply continues MP rōy, and رویین is MP rōyēn ⟨lwdyn'⟩ + the relational -īn. Again the classical gloss is 'copper, brass'; 'zinc' is the modern chemical use. (b) روناس ronās 'madder, Rubia tinctorum (the red dyestuff)', with the variants رویناس rōyenās and روینگ/رویان — disputed. Horn no.634 (Nourai's source) writes only 'Wohl zu aw. raoiδita- ,rötlich^ (No. 635); rōnās ist aus rōyenās ... contrahirt', a guess, and Hübschmann (Pers. Studien p.168) accepts only the contraction, not the etymology. Modern lexicography (Löw, Aramäische Pflanzennamen 363; Minorsky 1955; Monchi-Zadeh 1990 no.440, followed by Wiktionary) derives ronās instead from Ancient Greek ῥόϊνος 'garnet-, pomegranate-coloured', plausibly through Aramaic (Syriac ܪܘܙܢܘܣ), with the Persian shape secondarily reshaped under the influence of روی rōy 'copper'; Arabic رُنّاس is in turn borrowed from Persian. On that view the resemblance to رویناس is folk-etymological, not inherited. Because one of the node's two words is now given a different origin, the node takes the worse verdict.\",\n          \"derivation_fa\": \"این جعبه دو واژه دارد با سرنوشت جدا. الف) «روی» (با رویگر، رویین، رویینه) پذیرفتنی و درست است: از فارسی میانهٔ rōy، از ایرانی باستان *rauda-/*raudi- و در نهایت از ریشهٔ هندواروپایی «سرخ»؛ فلز را از رنگش نامیده‌اند، درست مانند سنسکریت lohá-. «رویین» نیز همان rōyēn پهلوی + پسوند نسبت است. ب) «روناس» (گیاه رنگرزی) محل اختلاف است: هرن تنها با احتیاط نوشته «احتمالاً به اوستایی raoiδita- مربوط است» و آن را مخفّفِ «رویناس» دانسته، و هوبشمان هم فقط همین ادغام آوایی را می‌پذیرد؛ اما پژوهش امروزی (لُو، مینورسکی، منشی‌زاده و به پیروی آنان ویکی‌واژه) آن را وام‌واژه‌ای از یونانی ῥόϊνος «به رنگ انار/گارنت» می‌داند که احتمالاً از راه آرامی (سریانی ܪܘܙܢܘܣ) به فارسی رسیده و سپس زیر تأثیر «روی» به صورت «رویناس» درآمده است ــ یعنی شباهت به «روی» ریشه‌شناسی عامیانه است. عربی «رُنّاس» نیز از فارسی وام گرفته شده. چون یکی از دو واژهٔ این جعبه امروز خاستگاه دیگری دارد، حکم کلی جعبه «مورد اختلاف» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/روی\",\n            \"https://en.wiktionary.org/wiki/روناس\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:980,981\", \"status\": \"supports\", \"note\": \"Verified in BQT_v2_pages.txt: leaf 443 = printed p.980 (روناس, Mo'in's footnote '... از اوستا ... (سرخ رنگ) [رک: روی]، هوبشمان ۴۶') and leaf 444 = p.981 (روی, footnote 'از او[ستا] raoiδita- (سرخ رنگ) «بارتولمه ۱۴۹۵»'). The leaf/page fit is fixed by the running note 'بقیه از صفحهٔ ۹۷۹' on the رومیه entry of leaf 442. So both of Nourai's cited pages carry exactly the claimed derivations — though what they carry for ronās is the older (Horn) view.\"},\n            {\"ref\": \"HRN:141\", \"status\": \"supports\", \"note\": \"Horn p.141 (HRN.txt leaf 163) nos. 634-635: '634. rōnās, rōyenās, rōyen ,Krapp, Färberröte^ ... Wohl zu aw. raoiδita- ,rötlich^ (No. 635). rōnās ist aus rōyenās (im FJ zweifach belegt) contrahirt; andere ... Formen wie rōden, rūdeng, rōynās sind unbelegt.' / '635. (i)rōy, rō ,Kupfer^ ...'. Nourai's whole Persian box, including the parenthesised variants رویناس/روینگ, comes from this page. NB Horn marks رویناس/روینگ-type forms as unattested ('unbelegt') and only 'wohl' (probably) connects rōnās with raoiδita-.\"},\n            {\"ref\": \"MON:1696\", \"status\": \"not_checked\", \"note\": \"The six-volume Mo'in is not accessible with its print pagination; the two-volume abridgement on disk (MON_part1/2.txt) has no روناس/روی headword with etymological tags. Mo'in's own footnotes in BQT (above) stand in for it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.168 (§58)\", \"stance\": \"partial\", \"note\": \"HUB.txt l.5929: 'Jüngere Kontraktionen sind rōnās „Krapp“ aus rōyanās? H. 634' — Hübschmann accepts the contraction rōyanās > rōnās (with a question mark) but takes no position on the *reudh- etymology.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.72\", \"stance\": \"partial\", \"note\": \"PHD.txt l.559: 'rōyan [lwd(y)n' | N ~] madder' — a Pahlavi word for madder does exist and is homographic with rōyēn 'brazen', which is what makes the رویناس/روی association so natural; but MacKenzie offers no etymology.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/روناس (Etymology; refs Löw, Aramäische Pflanzennamen 363; Minorsky 1955 p.257a; Monchi-Zadeh 1990 p.149 no.440)\", \"stance\": \"contradicts\", \"note\": \"'Borrowed from Ancient Greek ῥόϊνος (“garnet, pomegranate-coloured”), influenced by روی (rōy, “copper”), plausibly also acquired via Aramaic attested in Classical Syriac ܪܘܙܢܘܣ.' Descendant: Arabic رُنّاس (borrowed).\"},\n            {\"src\": \"FRS\", \"where\": \"Loghat-e Fors s.v. روین\", \"stance\": \"supports\", \"note\": \"'روین: الت و مس' — confirms روی/روین as the metal word in the 11th-c. lexicon, supporting word (a).\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"rôbeus\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin robeus (short o; Nourai's circumflex wrongly marks it long) is a genuine word, a dialectal Italic variant of ruber 'red' beside robus and robius, from the o-grade *h₁rowdʰ-os with the Sabellic/rural development of *ou to ō/o (Pokorny: 'mit dial. o aus *ou lat. robus, robeus, robius ,rot^'; cf. robīgō 'rust, mildew' and rōbur 'red oak, hardwood'). But it is NOT the etymon of the words hanging under it: French rouge and English ruby go back to Latin rubeus (zero grade *h₁rudʰ-yo-), as Nourai's own cited authority states — AHD/Watkins puts ROUGE, RUBEOLA, RUBY under 'Latin rubeus, red' and robus only under RUBIGINOUS. Buck likewise: 'Lat. rubeus “reddish” (> Fr. rouge, etc.)'. So the box is a real Latin word but the wrong link in the chain; robeus and rubeus are ablaut doublets of one root, which is presumably how the confusion arose.\",\n          \"derivation_fa\": \"لاتینی robeus (با «o» کوتاه؛ نشانهٔ کشیدگی در کتاب نادرست است) واژه‌ای واقعی است: گونهٔ گویشیِ ruber «سرخ» در کنار robus و robius، از درجهٔ o-ی ریشه یعنی *h₁rowdʰ-os، با تحول گویشیِ *ou به o (پوکورنی: «mit dial. o aus *ou lat. robus, robeus, robius ,rot‘»؛ سنجیده شود با robīgō «زنگار» و rōbur «بلوط سرخ»). اما نیای فرانسوی rouge و انگلیسی ruby این واژه نیست، بلکه rubeus لاتینی (درجهٔ صفرِ *h₁rudʰ-yo-) است؛ همان منبعی که نورایی خود ارجاع داده (AHD/واتکینز) ROUGE و RUBY را زیر «Latin rubeus» می‌آورد و robus را تنها زیر RUBIGINOUS. پس جعبه واژه‌ای حقیقی است ولی حلقهٔ درست زنجیره نیست؛ robeus و rubeus دوگانهٔ آواگردانیِ یک ریشه‌اند و همین سبب اشتباه شده است.\",\n          \"sources\": [\"https://www.etymonline.com/word/rouge\", \"https://www.etymonline.com/word/ruby\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. reudh-1: 'I.4. Latin rŏbus, red, in robigō, rūbigō, rust: RUBIGINOUS' — robus/robeus is there, but the very next section reads 'II.3. Latin rubeus, red: ROUGE, RUBEOLA, RUBY', so Watkins derives rouge and ruby from rubeus, not robeus.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II 358 f.\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt l.23705: 'o aus *ou lat. robus, robeus, robius „rot“, robigo „Rost; Mehltau“' — the form itself is well attested.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 15.66 RED §1, p.1056\", \"stance\": \"contradicts\", \"note\": \"'Lat. ruber, and (dial.) rufus ... also Lat. rubeus ‘reddish’ (> Fr. rouge, etc.), and (*rudh-tos) russus (> It. rosso ...)' — French rouge from rubeus.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. rouge, ruby\", \"stance\": \"contradicts\", \"note\": \"SKT.txt ll.16261-16262 'rouge, red paint. (F.-L.) F. rouge, red. — L. rubeus, red'; l.16259 'Ruby ... Low L. rubinus, a ruby; from its colour. — L. ruber, red.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box for French rouge (adj. 'red', 12th c., substantivised as 'red colouring matter, rouge'), which continues Latin rubeus 'reddish' with regular Gallo-Romance -bj- > -ʒ- and -u- > -ou- ; it is from this French word that both the English cosmetic term (node #7) and the modern Persian رژ (node #6) are taken. The immediate Latin parent is rubeus, not the robeus printed in node #4.\",\n          \"derivation_fa\": \"جعبه‌ای گذرا و بی‌واژه است که مقصود از آن فرانسوی rouge «سرخ» (سدهٔ دوازدهم میلادی) است که بعدها به معنی «مادهٔ رنگی سرخ، سرخاب» اسم شده؛ بازماندهٔ لاتینی rubeus است با تحول منظم گالو-رومانسِ -bj- به -ʒ- و -u- به -ou-. هم واژهٔ انگلیسی (جعبهٔ ۷) و هم «رژ» فارسی (جعبهٔ ۶) از همین واژهٔ فرانسوی گرفته شده‌اند. نیای بی‌واسطهٔ آن rubeus است نه robeus که در جعبهٔ لاتینی چاپ شده.\",\n          \"sources\": [\"https://www.etymonline.com/word/rouge\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. reudh-1 II.3: 'Latin rubeus, red: ROUGE, RUBEOLA, RUBY' — the French link is implicit in Watkins' listing of ROUGE.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. rouge\", \"stance\": \"supports\", \"note\": \"'rouge, red paint. (F.-L.) F. rouge, red. — L. rubeus, red; (whence F. rouge ...)'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 15.66, p.1056\", \"stance\": \"supports\", \"note\": \"'Lat. rubeus ‘reddish’ (> Fr. rouge, etc.)'; the table gives 'Fr. rouge' as the modern French word for 'red'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"rŭž\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Modern Persian رژ rož 'rouge, lipstick' is indeed a 20th-century loan from French rouge, taken in the compound رژ لب rož-e lab, calquing French rouge à lèvres, and then clipped to رژ; French [ʁuʒ] is rendered with Persian ژ /ʒ/ and short o. The derivation itself is uncontroversial. What is suspect is the spelling printed in the chart: standard Persian writes رژ (and رژ لب), without و; «روژ» with vāv is either a variant/older transcription of the French vowel or a confusion with Kurdish ڕۆژ rôž 'day, sun', which is unrelated. Nourai's transliteration rŭž matches the pronunciation rož. Because the form in the JSON is faithful to the printed page, this is the book's own spelling, not a scan error.\",\n          \"derivation_fa\": \"«رژ» فارسی امروز («رژ لب») وام‌واژه‌ای است از فرانسوی rouge که در سدهٔ چهاردهم خورشیدی از راه ترکیب rouge à lèvres («رژ لب») وارد شده و سپس کوتاه شده است؛ آوای فرانسوی [ʒ] با «ژ» و واکهٔ آن با o کوتاه نشان داده می‌شود. خودِ وام‌گیری تردیدبردار نیست؛ آنچه جای ایراد دارد املای نمودار است: املای معیار «رژ» است نه «روژ». «روژ» با واو یا نویسه‌گردانی کهنِ واکهٔ فرانسوی است یا آمیختگی با «ڕۆژ» کردی به معنی «روز، خورشید» که بی‌ارتباط است. چون داده‌های استخراج‌شده با صفحهٔ چاپی یکی است، این املا از خود کتاب است نه خطای خوانش اسکن.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/رژ\", \"https://www.etymonline.com/word/rouge\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"Nourai gives no page for MON here. Mo'in's French loanwords are in vol. 4 (foreign compounds), which is not online with its pagination; the two-volume abridgement on disk (MON_part1.txt) has no رژ headword (grep '^رژ' returns only رژد, رژه, رژیم).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/رژ\", \"stance\": \"supports\", \"note\": \"Persian رژ: 'short for رژ لب (rož-e lab)', from French rouge à lèvres — i.e. a French loan, spelt رژ, not روژ.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt (2-vol abridgement), headword list around ر-ژ\", \"stance\": \"silent\", \"note\": \"No entry رژ/روژ in the abridgement; it cannot confirm or deny Nourai's spelling.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"rouge, ruby\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are Romance loans that go back to Latin rubeus. ROUGE entered English in 1753 from French rouge 'red colouring matter', noun use of the 12th-c. adjective 'red' < Latin rubeus. RUBY came in c.1300 as Middle English rubi/rubie 'a clear rich-red corundum' from Old French rubi (12th c.), from Medieval Latin rubīnus (lapis) 'red stone', a derivative of Latin rubeus/ruber; the colour sense is from the 1570s. Both therefore belong to *h₁rewdʰ- through the Latin zero-grade *h₁rudʰ-yo-s.\",\n          \"derivation_fa\": \"هر دو وام‌واژهٔ رومانسی‌اند و به lat. rubeus بازمی‌گردند. rouge در ۱۷۵۳ میلادی از فرانسوی rouge «مادهٔ رنگی سرخ» به انگلیسی رفت، و ruby حدود ۱۳۰۰ میلادی از فرانسوی کهن rubi و آن از لاتینی میانه rubīnus (lapis) «سنگ سرخ»، مشتق rubeus/ruber؛ کاربرد آن به معنی خودِ رنگ از دههٔ ۱۵۷۰ است. بنابراین هر دو از راه درجهٔ صفرِ لاتینیِ *h₁rudʰ-yo-s به ریشهٔ *h₁rewdʰ- می‌رسند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/rouge\", \"https://www.etymonline.com/word/ruby\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai cites no reference on this node; it inherits AHD from its parent, which does list ROUGE and RUBY under reudh-1.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reudh-1 II.3 and the index\", \"stance\": \"supports\", \"note\": \"'Latin rubeus, red: ROUGE, RUBEOLA, RUBY'; index entries 'ROUGE reudh-1', 'RUBY reudh-1'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.vv. ruby, rouge\", \"stance\": \"supports\", \"note\": \"'Ruby, a red gem. (F.—L.) O.F. rubi ... Low L. rubinus, a ruby; from its colour. — L. ruber, red'; 'rouge, red paint. (F.-L.) F. rouge, red. — L. rubeus'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box for Proto-Germanic *raudaz 'red' (from the o-grade *h₁rowdʰ-ós, with Grimm's law *dʰ > *d), continued in Gothic rauþs, Old Norse rauðr, Old High German rōt, Old English rēad; beside it the zero-grade derivative *rūst- (*h₁rudʰ-s-tó-) 'rust'. These two supply the English words in node #9.\",\n          \"derivation_fa\": \"جعبه‌ای گذرا و بی‌واژه است که مقصود ژرمنی آغازین *raudaz «سرخ» است، از درجهٔ o-ی ریشه (*h₁rowdʰ-ós) با اجرای قانون گریم (*dʰ ← *d)؛ بازمانده‌های آن گوتیک rauþs، نورس کهن rauðr، آلمانی علیای کهن rōt و انگلیسی کهن rēad است. در کنار آن مشتقِ درجهٔ صفر *rūst- (*h₁rudʰ-s-tó-) «زنگار» قرار دارد. همین دو، واژه‌های جعبهٔ ۹ را می‌دهند.\",\n          \"sources\": [\"https://www.etymonline.com/word/red\", \"https://www.etymonline.com/word/rust\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. reudh-1: 'I.1. Germanic *raudaz in: a. Old English rēad, red: RED'; 'II.2. Suffixed form *rudh-sto- in Germanic *rūst- in Old English rūst, rust: RUST.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW pp.872-873 (POK_03.txt leaf 109)\", \"stance\": \"supports\", \"note\": \"'ablaut. rauþs, aisl. rauðr, ags. rēad, ahd. rōt ,rot^ ... ags. rūst, ahd. as. rost ,Rost^ (*rūdh-s-tó)'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 15.66, p.1056\", \"stance\": \"supports\", \"note\": \"'Goth. rauþs, ON rauðr, OE rēad, etc., general Gmc.'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"red, rust\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"RED is Old English rēad 'red, crimson, scarlet' (also 'red dye, ink, wine'), from Proto-Germanic *raudaz, the Middle English long vowel later shortening (whence the surnames Read/Reid keep the older value). RUST is Old English rūst, beside rudu 'redness', from Proto-Germanic *rūst- < *h₁rudʰ-s-tó- 'reddened (thing)' — the metal-oxide is literally 'the red stuff', the same naming principle that produced Persian روی for the red metal in node #3. Skeat states it plainly: 'A.S. rūst, rust; orig. redness. Allied to A.S. rudu, ruddiness, and rēad, red.'\",\n          \"derivation_fa\": \"red از انگلیسی کهن rēad «سرخ، ارغوانی» (نیز «رنگ سرخ، مرکب، شراب») و آن از ژرمنی آغازین *raudaz است؛ واکهٔ کشیدهٔ انگلیسی میانه بعدها کوتاه شده و نام‌های خانوادگی Read/Reid ارزش کهن‌تر را نگه داشته‌اند. rust از انگلیسی کهن rūst در کنار rudu «سرخی» است، از ژرمنی *rūst- و آن از *h₁rudʰ-s-tó- «چیز سرخ‌شده»؛ زنگار را از رنگش نامیده‌اند، درست همان الگویی که در فارسی «روی» را برای فلز سرخ ساخته است (جعبهٔ ۳). اسکیت به‌روشنی می‌گوید: «rūst انگلیسی کهن، در اصل سرخی؛ هم‌ریشه با rudu و rēad». ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/red\", \"https://www.etymonline.com/word/rust\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited on the node; the parent Germanic box carries AHD, which lists RED and RUST under reudh-1.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. rust\", \"stance\": \"supports\", \"note\": \"SKT.txt l.15759: 'rust. (E.) A.S. rūst, rust; orig. redness. Allied to A.S. rudu, ruddiness, and rēad, red. + Du. roest, Dan. rust, Swed., G. rost.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index\", \"stance\": \"supports\", \"note\": \"'RED reudh-1' and 'RUST reudh-1' in the English index.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Reug\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₁rewg- 'to belch, roar' (Pokorny reu-b- / reu-g- 871-872, filed under 4. reu-)\",\n      \"note\": \"Correct root, correct gloss, correct page. Pokorny IEW 871-872 heads it 'reu-b- und reu-g- ,sich erbrechen, rülpsen, hervorbrechen^, auch ,Wolke, Rauch^?' — Nourai's composite gloss 'to vomit, belch, produce smoke or vapor' renders that headword closely, including Pokorny's own doubt-marked 'smoke/cloud' extension (Old Norse rjúka, OE rēocan, OHG rouhhan), which is the part that carries English reek. Watkins files the same material as 'reug-. To vomit, belch, smoke, cloud. [Pok. 4. reu- 871.]' Wiktionary reconstructs *h₁rewg- and, with Beekes, treats the root as onomatopoeic.\",\n      \"note_fa\": \"ریشه، معنی و شمارهٔ صفحه هر سه درست است. پوکورنی در صفحهٔ ۸۷۱–۸۷۲ سرواژهٔ «reu-b- و reu-g- ,آروغ زدن، بالا آوردن، فوران کردن‘، و نیز (با تردید) ,ابر، دود‘؟» را آورده و معنای مرکبی که نورایی نوشته دقیقاً برگردان همان است؛ بخش «دود/بخار» همان است که واژهٔ انگلیسی reek را پشتیبانی می‌کند. واتکینز نیز همین مواد را زیر reug- «بالا آوردن، آروغ زدن، دود، ابر» آورده است. بازسازی امروزی *h₁rewg- است و بیکس آن را ریشه‌ای آوابنیاد (نام‌آوا) می‌داند.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁rewg-\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:871\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 107-108 and POK_full.txt: 'reu-b- und reu-g- ,sich erbrechen, rülpsen, hervorbrechen^, auch ,Wolke, Rauch^? ... 2. reug-: npers. ā-rōγ ,das Rülpsen^; arm. orcam ,erbreche mich^ ... gr. ἐρεύγομαι ... lat. ērūgō, ructō ... ags. rocettan ... Page(s): 871-872.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reug-\", \"stance\": \"supports\", \"note\": \"'reug-. To vomit, belch, smoke, cloud. 1. Germanic *reu-kan in Old English rēocan, to smoke, reek: REEK. 2. Suffixed zero-grade form *rug-to- in Latin ructāre, to belch: ERUCT. [Pok. 4. reu- 871.]'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 357 (WLD_Bd2_pages.txt l.23650-52)\", \"stance\": \"supports\", \"note\": \"'... Wenn alb. rê „Wolke“ aus *rougi- entstanden ist, wie dt. Rauch ..., ist ein bereits uridg. *reug- „Wolke, Rauch“ voraussetzbar' — the reference Pokorny cites (WP. II 357).\"},\n        {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index p.55 (ARY_latin_index_pages.txt ll.1490-1520)\", \"stance\": \"supports\", \"note\": \"Root page headed HREUG (Mallory & Adams) with Greek EREUGOMAI, Armenian ORCAM/ORUCAM, Latin RUCTUS/RUCTARE/ERUCTARE/ERUGO, OE ROCETTAN, OHG RUFEZZEN, German RÜLPSEN; references to Pokorny, Onions, Skeat.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"roğ; âroğ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pokorny cites the Persian word for this root by name: under reug- he writes 'npers. ā-rōγ ,das Rülpsen^'. آروغ āroγ 'belch' is the prefixed form, Old Iranian *ā- 'onto, up' + *raugah- (a neuter -as-stem from *h₁rewg-, cf. Greek ἐρυγή 'belch', Latin ē-rūgō), giving Middle/New Persian -rōγ with the regular Iranian *g > γ between vowels; the unprefixed رُغ/روغ roγ is the same *raugah- without ā-, and Mo'in lists the set together: 'آروغ [= آرغ = رُغ = وروغ] (اِ.) باد گلو', i.e. the variants آرغ, رُغ, وروغ (the last with a prothetic v-). آروق with qāf is a late orthographic variant (the -q spelling being the Turkic-influenced way of writing final -γ), listed as a variant by both Mo'in and Wiktionary. Cognates: Armenian որկամ, Greek ἐρεύγομαι, Latin ērūgō, Lithuanian rjáugmi, OCS rygati — an onomatopoeic root, so the Persian form is inherited rather than borrowed.\",\n          \"derivation_fa\": \"پوکورنی خودِ واژهٔ فارسی را نام می‌برد: زیر ریشهٔ reug- می‌نویسد «npers. ā-rōγ ,آروغ زدن‘». «آروغ» صورت پیشوندی است: ایرانی باستان *ā- «بر، بالا» + *raugah- (ستاک خنثای -as- از ریشهٔ *h₁rewg-؛ سنجیده شود با یونانی ἐρυγή و لاتینی ē-rūgō)؛ *g ایرانی میان دو واکه به غ سایشی بدل شده است. «رُغ/روغ» همان *raugah- بدون پیشوند است و معین هر سه را یک‌جا آورده: «آروغ [= آرغ = رُغ = وروغ] (اِ.) باد گلو» (صورت اخیر با «و» پیشین). «آروق» با قاف تنها گونهٔ املایی متأخر است (نوشتنِ غِ پایانی با ق به شیوهٔ ترکی). هم‌ریشه‌ها: ارمنی որկամ، یونانی ἐρεύγομαι، لاتینی ērūgō، لیتوانیایی rjáugmi، اسلاوی کهن rygati. چون ریشه آوابنیاد است، صورت فارسی ارثی است نه وام‌گرفته. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/آروغ\", \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁rewg-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:871\", \"status\": \"supports\", \"note\": \"POK_full.txt, entry 'reu-b- ... reu-g-', section '2. reug-': 'npers. a-royδ [= ā-rōγ] das Rülpsen; Armenian orcam ...' — Persian ā-rōγ is named on the very page Nourai cites (871-872).\"},\n            {\"ref\": \"MON:44\", \"status\": \"supports\", \"note\": \"Mo'in's entry verified in the two-volume abridgement (MON_part1.txt l.2762): 'آروغ: [= آرغ = رُغ = وروغ] (اِ.) باد کلو [باد گلو].' followed by 'آروق: [= آروغ] آروغ، باد گلو.' Page 44 of vol. 1 of the six-volume edition is consistent with an آ- headword this early in the alphabet, though the print pagination could not be checked directly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt l.2762-2766 (2-vol abridgement)\", \"stance\": \"supports\", \"note\": \"'آروغ: [= آرغ = رُغ = وروغ] (اِ.) باد گلو' / 'آروق: [= آروغ] آروغ، باد گلو' — all four of Nourai's Persian spellings (آرغ، آروغ، آروق، رُغ/روغ) are Mo'in's.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/آروغ\", \"stance\": \"supports\", \"note\": \"'From Proto-Indo-European *h₁rewg- (“belch, roar”); cognate with Latin ērūgō.' Alternative forms listed: آروق (âruq), آرق, وروغ (wurōγ), روغ (rōγ), رغ (roγ), ارغ — matching the chart's set exactly.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index p.55, root HREUG\", \"stance\": \"partial\", \"note\": \"Aryanpur's root page for this etymon lists the Greek, Armenian, Latin, Germanic and Balto-Slavic material but the Persian side of the entry was not legible in the OCR; it does not contradict the node.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Germanic\",\n          \"words\": \"riukan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The etymology is right, the citation form is slightly off. The Germanic strong verb is normally reconstructed as Proto-Germanic *reukaną 'to smoke, steam' (Watkins: 'Germanic *reu-kan'; Etymonline: 'from Proto-Germanic *reukan'), whence Old English rēocan (West Saxon) / recan (Anglian), Old High German riohhan, Middle Dutch rieken, Old Norse rjúka. Nourai's 'riukan' with -iu- reproduces the Old Norse/Old High German shape (rjúka, riohhan) rather than the Proto-Germanic one; Skeat similarly cites 'Icel. rjúka (pt. t. rauk), G. riechen' alongside A.S. rēocan. The sense given ('to produce vapor, smell, stink') is the Germanic branch of Pokorny's tentative 'Wolke, Rauch' extension of *reug-, and Pokorny marks that extension 'very doubtful' ('yet very doubtful') — so the link of the smoke-words to the belch-root is accepted but not certain.\",\n          \"derivation_fa\": \"ریشه‌شناسی درست است ولی صورت شاهد اندکی نادقیق. فعل قویِ ژرمنی را معمولاً ژرمنی آغازین *reukaną «دود کردن، بخار دادن» بازسازی می‌کنند (واتکینز: «Germanic *reu-kan»)، که انگلیسی کهن rēocan، آلمانی علیای کهن riohhan، هلندی میانه rieken و نورس کهن rjúka از آن است. صورت «riukan» با -iu- بیشتر شکل نورس/آلمانی علیای کهن را بازمی‌تاباند تا صورت ژرمنی آغازین را؛ اسکیت نیز در کنار rēocan انگلیسی کهن، rjúka ایسلندی و riechen آلمانی را می‌آورد. معنایی که داده شده («دود و بو و بوی بد دادن») همان شاخهٔ ژرمنیِ گسترشِ «ابر/دود» است که پوکورنی خود آن را «بسیار تردیدآمیز» می‌خواند؛ پس پیوند واژه‌های «دود» با ریشهٔ «آروغ» پذیرفته اما قطعی نیست.\",\n          \"sources\": [\"https://www.etymonline.com/word/reek\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. reug-: '1. Germanic *reu-kan in Old English rēocan, to smoke, reek: REEK.' The reconstruction is *reukan, not *riukan.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. reek (SKT.txt l.15774)\", \"stance\": \"supports\", \"note\": \"'Reek, vapour. (E.) M.E. reke. A.S. rec, vapour. — A.S. reac, pt. t. of reocan (strong verb), to reek, smoke. + Du. rook, Icel. reykr, Swed. rök, Dan. røg; G. rauch; cf. Icel. rjúka (pt. t. rauk), G. riechen, to smoke, reek.'\"},\n            {\"src\": \"POK\", \"where\": \"IEW 871-872\", \"stance\": \"partial\", \"note\": \"'under a Mittelbed. „hervorbrechen“, oder „exhalare“ reiht man (doch sehr zweifelhaft) an: aisl. rjúka „rauchen, stieben“, ags. rēocan „rauchen, dampfen, stinken“, ahd. rouhhan ... ahd. rouh, as. rōk, ags. rēc, aisl. reykr m. „Rauch“' — Pokorny attaches the smoke-words with explicit doubt.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"reek\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English reek continues both the Old English strong verb rēocan (West Saxon) / recan (Anglian) 'to emit smoke' > Middle English reken, and the noun Old English rēc / rīec 'smoke from burning material' (the modern noun form partly reinforced from Scandinavian rykr). The modern 'stench' sense is a specialisation attested from the 1650s, via 'that which rises'; 'to emit a bad smell' is from about 1710, developing out of an earlier 'be heated and perspiring' (early 15th c.). The whole family goes back to Proto-Germanic *reukaną and so to *h₁rewg-.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی reek هم دنبالهٔ فعل قویِ انگلیسی کهن rēocan «دود دادن» است (انگلیسی میانه reken) و هم اسمِ انگلیسی کهن rēc/rīec «دودِ چیزِ سوزان» (که صورت امروزینش تا اندازه‌ای زیر تأثیر اسکاندیناویایی rykr تقویت شده). معنی امروزی «بوی بد دادن» تخصیصی متأخر است: معنی «تعفن» از دههٔ ۱۶۵۰ و فعل «بوی ناخوش دادن» از حدود ۱۷۱۰ میلادی، از راه معنیِ کهن‌ترِ «گرم شدن و عرق کردن». همهٔ این خانواده به ژرمنی آغازین *reukaną و از آنجا به *h₁rewg- می‌رسد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/reek\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited on the node; the parent Germanic box carries AHD, which lists REEK under reug-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reug- and index 'REEK reug-'\", \"stance\": \"supports\", \"note\": \"'Germanic *reu-kan in Old English rēocan, to smoke, reek: REEK.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. reek\", \"stance\": \"supports\", \"note\": \"'Reek, vapour. (E.) M.E. reke. A.S. rec, vapour. — A.S. reac, pt. t. of reocan (strong verb), to reek, smoke.'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Reughmen\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *h₁rewgʰ-m(e)n- / *réwgʰ-no-s 'cream, butter' — Pokorny 'reugh-m(e)n- ,Rahm^?' IEW 873 (NOT 837)\",\n      \"note\": \"Two things to separate. (1) The root label and gloss are essentially right: Pokorny does have an entry 'reugh-m(e)n- ,Rahm^?' whose whole content is 'Av. raoγna- ,Butter^, mpers. npers. rōγan ,(ausgelassene) Butter^; aisl. rjúmi m. ,Rahm^, ablautend ags. rēam, mnd. rōme, ahd. roum ,Sahne^ ...'. But Pokorny writes it with a question mark, and his own source Walde-Pokorny II 357 f. calls the whole equation 'höchst unsicher' and prefers to take the Germanic 'cream' words from *reu- 'aufreißen' (*reu-, rou-, ru-m(en)- 'skin, layer of fat on milk', after Fick); Buck (§5.89 BUTTER) says of Av. raoγna- 'outside connections unknown'. Modern reconstruction keeps the Iranian side but derives it as *rewgʰ- + *-nos ('*réwgʰ-no-s'), i.e. an n-stem, not an -men- stem. So: Iranian branch certain, Germanic branch doubtful, hence 'plausible' rather than 'confirmed'. (2) The page reference POK:837 is wrong: p.837 of IEW is in the *pleu- 'to flow, swim' article (POK_03.txt leaf 72); the reugh-m(e)n- entry stands on p.873. Nourai's digits are transposed (873 → 837); the same wrong number is repeated on node #1. Aryanpur's parallel entry cites Pokorny too and Wiktionary cites 'IEW p. 873'.\",\n      \"note_fa\": \"دو نکته را باید از هم جدا کرد. یکم، نام و معنی ریشه در اساس درست است: پوکورنی سرواژهٔ «reugh-m(e)n- ,سرشیر‘؟» را دارد که همهٔ محتوایش این است: «اوستایی raoγna- ,کره‘، فارسی میانه و فارسی نو rōγan ,روغن (گداخته)‘؛ نورس کهن rjúmi ,سرشیر‘، انگلیسی کهن rēam، آلمانی علیای کهن roum ...». اما خودِ او نشانهٔ پرسش گذاشته و مأخذش والده-پوکورنی (ج۲ ص۳۵۷ بب.) این برابری را «بسیار نامطمئن» می‌خواند و ترجیح می‌دهد واژه‌های ژرمنیِ «سرشیر» را از ریشهٔ *reu- «دریدن» بگیرد؛ باک هم دربارهٔ raoγna- اوستایی می‌نویسد «پیوندهای بیرونی‌اش ناشناخته است». بازسازی امروزی شاخهٔ ایرانی را نگه می‌دارد اما آن را *rewgʰ- + پسوند *-nos می‌داند، یعنی ستاک n-دار نه men-دار. پس شاخهٔ ایرانی قطعی و شاخهٔ ژرمنی مشکوک است و حکم «با احتیاط پذیرفتنی» است. دوم، ارجاع POK:837 نادرست است: صفحهٔ ۸۳۷ پوکورنی در مقالهٔ *pleu- «روان شدن، شنا کردن» است و سرواژهٔ reugh-m(e)n- در صفحهٔ ۸۷۳ قرار دارد؛ رقم‌ها جابه‌جا شده‌اند (۸۷۳ ← ۸۳۷) و همین شمارهٔ نادرست در جعبهٔ اوستایی هم تکرار شده است.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ráwgnah\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:837\", \"status\": \"not_found\", \"note\": \"Checked both directions in POK_03.txt. Page 837 (leaf 72, page numeral '837' printed in the leaf) is inside 'pleu- ,fließen, schwimmen^': 'aksl. plovǫ, pluti ,fließe, schiffe^ ... toch. A B plu- ,fliegen, schweben^' — nothing about oil or cream. The entry Nourai wants is on leaf 110: 'reugh-m(e)n- ,Rahm^? Av. raoγna- ,Butter^, mpers. npers. rōγan ,(ausgelassene) Butter^; aisl. rjúmi m. ,Rahm^ ... WP. II 357 f.; s. auch oben S. 868. Page(s): 873'. So the correct citation is POK:873.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 357 f. (WLD_Bd2_pages.txt ll.23653-23665)\", \"stance\": \"partial\", \"note\": \"'reugh-m(e)n- „Rahm“? Av. raoγna- „Butter“, mpers. npers. rōγan „(ausgelassene) Butter“; anord. rjómi m. „Rahm“ ... Höchst unsicher. ... Aber für die germ. Formen macht ags. rēoma, rēama „dünne Haut“ ... eine Gdbed. „Haut, Fettschicht auf der Milch“ und eine Gdf. *reu-, rou-, ru-m(en)- wahrscheinlicher (Fick III⁴ 348).' — the standard reference explicitly doubts the Iranian-Germanic equation.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reugh-men-\", \"stance\": \"supports\", \"note\": \"'reugh-men-. Cream. O-grade form *roughmen- in Germanic *rau(g)ma- in Middle Low German rēm(e), cream: RAMEKIN. [Pok. reugh-m(e)n- 873.]' — note Watkins' own page number is 873.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck §5.89 BUTTER (SYN.txt l.9732)\", \"stance\": \"partial\", \"note\": \"'Av. raoγna-, raoγnya- ,butter^ (? So Barth. 1488) or ,oil^ (Darmesteter) : NPers. rawγan ,oil, grease^, outside connections unknown.' Buck accepts the Avestan-Persian pair but not the wider IE (Germanic) connection.\"},\n        {\"src\": \"KLN\", \"where\": \"Klein 1966 pp.1307-08 s.v. ream 'cream'\", \"stance\": \"supports\", \"note\": \"'ream, n., cream; froth. — ME. rem, fr. OE. rēam, ‘cream’, rel. to MLG. rōm, rōme, Du. room, MHG. roum, G. Rahm, Icel. rjómi, ‘cream’, fr. Teut. base *rauma-, which corresponds perh. to I.-E. *raugma-, whence Avestic raoγna-, ‘butter’. Cp. ramekin.' Note Klein's 'perh.' and his *raugma- (with m).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"raoğna\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan raoγna- (neuter) 'butter' is securely attested — Bartholomae quotes it from Hādōxt Nask 2.18, where zarǝmaya- raoγna- 'spring butter' is the food of the blessed, and gives the adjective raoγnavant- 'having butter' (Vd. 21.7) and the feminine raoγnyā- 'butter' (Yt. 12.3). It continues Proto-Iranian *ráwgnah, an -as-stem built on *rawgʰ-na- ; Bartholomae himself adds 'Ableit. — np. rōγan „ausgelassene Butter“. Pü.: rōγn'. Nourai's gloss 'oil' follows Darmesteter (Buck records both renderings, 'butter' per Bartholomae, 'oil' per Darmesteter); either is defensible, since the word covers clarified fat. The ONLY defect is the page number: POK:837 should be POK:873.\",\n          \"derivation_fa\": \"واژهٔ اوستایی raoγna- (خنثی) «کره» گواه استوار دارد: بارتولمه آن را از هادُخت نسک ۲٫۱۸ نقل می‌کند («کرهٔ بهاری» خوراک روان پرهیزگاران) و صفت raoγnavant- «دارای کره» (وندیداد ۲۱٫۷) و مؤنث raoγnyā- «کره» (یشت ۱۲٫۳) را نیز می‌آورد. این واژه دنبالهٔ ایرانی آغازین *ráwgnah است، ستاکی -as-دار بر پایهٔ *rawgʰ-na-؛ بارتولمه خود می‌افزاید: «مشتق: فارسی نو rōγan ,روغن گداخته‘؛ پهلوی: rōγn». معنایی که نورایی داده («روغن») از دارمستتر است؛ باک هر دو خوانش را ثبت کرده و هر دو پذیرفتنی است، چون واژه چربی گداخته را می‌رساند. تنها ایراد، شمارهٔ صفحه است: به‌جای POK:837 باید POK:873 باشد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ráwgnah\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:837\", \"status\": \"not_found\", \"note\": \"IEW p.837 is the *pleu- article; the Avestan word stands on p.873 (POK_03.txt leaf 110): 'Av. raoγna- ,Butter^, mpers. npers. rōγan ,(ausgelassene) Butter^'. A transposed page number.\"},\n            {\"ref\": \"KLN:1307\", \"status\": \"supports\", \"note\": \"Klein 1966 pp.1307-08 s.v. 'ream, n., cream': '... fr. Teut. base *rauma-, which corresponds perh. to I.-E. *raugma-, whence Avestic raoγna-, ‘butter’.' Page located in KLN_1966.txt leaves 696-697, which carry the OCR'd page numerals 1307 and 1309.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. col. 1488 (BRT.txt ll.24830-24834)\", \"stance\": \"supports\", \"note\": \"'• j. raoγna- n. ,Butter^, mit *zarǝmaya- Adj. ,Frühlingsbutter^, Bezeichnung der Speise der Seligen ... H. 2.18. Ableit. — np. rōγan ,ausgelassene Butter^. — Pü.: rōγn. • j. raoγna-vant- Adj. ,der Butter hat^ ... V. 21.7. • j. raoγnyā- f. ,Butter^: Yt 12.3.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §5.89 BUTTER, p.??? (SYN.txt l.9719, 9732)\", \"stance\": \"supports\", \"note\": \"Buck's table for 'butter' gives 'Av. (raoγna-)'; the note reads 'Av. raoγna-, raoγnya- ,butter^ (? So Barth. 1488) or ,oil^ (Darmesteter) : NPers. rawγan ,oil, grease^.'\"},\n            {\"src\": \"HRN\", \"where\": \"no. 632, p.140\", \"stance\": \"supports\", \"note\": \"HRN.txt l.5612: '632. rōγen ,Butter, Öl^. ... aw. raoγna- ,Öl^; phlv. rōkan (d. i. rōγan, päz. raoγǝn), rōγan (PPGl.).' Horn glosses the Avestan word 'Öl', exactly Nourai's gloss.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, روغن, printed p.313 (ARY_pages.txt leaf 312)\", \"stance\": \"supports\", \"note\": \"Avestan RAOGHNA, RAOGAN; Pahlavi ROGHAN, ROVN, ROGHN; Kurdish RUN; Baluchi ROGAN, ROGUN; ON RIUMI; OHG ROUM; German RAHM; OE REAM; with the cross-reference 'برهان قاطع ۹۷۸' — the same Borhan page Nourai cites.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"rôğn; rôvn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian rōγn ⟨lwkn'⟩ (ideographically M(H)ŠYA, from Aramaic mšḥ 'to anoint'), Manichaean Middle Persian and Parthian ⟨rwgn⟩, 'oil, butter' — MacKenzie's entry also gives the compound rōγn-xwardīg 'sweetmeats'. Formally it continues Proto-Iranian *ráwgnah with loss of the final syllable and the usual Middle Persian syncope of the unstressed vowel (*rawgna- > rōγn), the Old Iranian diphthong *au monophthongising to ō. Wiktionary/Edelʹman in fact mark Middle Persian rōγn as taken over from Parthian rōγn rather than inherited directly in the southwest — a refinement, not a contradiction of Nourai's arrow. The second form rôvn is not MacKenzie's but comes from the Persian tradition: Mo'in's footnote to Borhan-e Qate' p.978 gives both spellings (rōγn ~ rōvn, with the fricative γ written v in the Pāzand/late transmission, cf. Horn's Pāzand raoγǝn), and Aryanpur likewise prints 'ROGHAN, ROVN, ROGHN (PAHLAVI)'. So both forms are defensible.\",\n          \"derivation_fa\": \"فارسی میانهٔ rōγn (نوشتهٔ ⟨lwkn'⟩ با هُزوارش M(H)ŠYA از آرامی mšḥ «روغن مالیدن»)، در پارسی میانهٔ مانوی و پارتی ⟨rwgn⟩، به معنی «روغن، کره»؛ مکنزی ترکیب rōγn-xwardīg «شیرینی» را هم می‌آورد. از نظر صورت، دنبالهٔ ایرانی آغازین *ráwgnah است با افتادن هجای پایانی و افتادن واکهٔ بی‌تکیه (‏*rawgna- ← rōγn) و یک‌آوایی شدن دوگانه‌واکهٔ *au به ō. ویکی‌واژه (به پیروی ادلمان) rōγn فارسی میانه را وام‌گرفته از پارتی می‌داند، که پالایشی است نه ردّ نمودار نورایی. صورت دوم «rôvn» از مکنزی نیست بلکه از سنّت فارسی می‌آید: حاشیهٔ معین بر برهان قاطع ص۹۷۸ هر دو املا را دارد (غ در ضبط پازند/متأخر با «و» نوشته شده؛ سنجیده شود با raoγǝn پازندِ هرن) و آریان‌پور نیز «ROGHAN, ROVN, ROGHN» را به‌عنوان صورت‌های پهلوی چاپ کرده است. پس هر دو صورت پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ráwgnah\", \"https://en.wiktionary.org/wiki/روغن\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:978\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 441 = printed p.978 (fixed by the 'بقیه از صفحهٔ ۹۷۹' note on leaf 443 and the روغن…روم…روناس…روی sequence). Mo'in's footnote 1 to روغن reads: 'پهلوی rōγn «تاوادیا» ، اوستا raoγna- «بارتولمه ۱۴۸۸» ... کردی rōn، بلوچی rōγan ...', and footnote 3 to روغنی gives the pair 'پهلوی rōγnīk، rōvnīk' — both of Nourai's Pahlavi spellings and his Avestan parent, on the page he cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.72 (PHD.txt l.559)\", \"stance\": \"supports\", \"note\": \"'rōγn [M(H)ŠYA < Aram. mšḥ; lwkn' | P rwgn, (M rwyn), N rawγan] oil, butter. ~-xwardīg [-hwltyk'] sweetmeats.'\"},\n            {\"src\": \"HRN\", \"where\": \"no. 632, p.140\", \"stance\": \"partial\", \"note\": \"'phlv. rōkan (d. i. rōγan, päz. raoγǝn), rōγan (PPGl.)' — Horn's Pahlavi form is rōγan/rōγn; he does not print a -v- variant, which comes instead from the Pāzand spelling and from Mo'in/Aryanpur.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, روغن, printed p.313\", \"stance\": \"supports\", \"note\": \"'(PAHLAVI) ROGHAN, ROVN, ROGHN' — the -v- form is printed in the Persian etymological tradition as well.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep for rōγn / royn / rōy in NYB_vol2_glossary.txt returns nothing; the glossary of Nyberg's selected texts does not happen to contain the word.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"roğan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian روغن rōγan 'oil, clarified butter, fat' is the regular continuation of Middle Persian rōγn, with an anaptyctic vowel breaking the final cluster -γn (rōγn > rōγan), a normal New Persian resolution; the older orthoepy is رَوْغَن rawγan, which is the form Bartholomae, Horn and Buck all cite. The word is the common Iranian one: Kurdish ڕۆن rûn, Baluchi rōγan, Pashto روغن roğán, Mazanderani راغون rağun, Yaghnobi rūγan, all from Proto-Iranian *ráwgnah. The Molavī couplet quoted in the chart ('گر ببینم خانه‌ات را من دوام / روغن و شیرت بیارم صبح و شام') is a genuine attestation of the word in its ordinary sense.\",\n          \"derivation_fa\": \"«روغن» فارسی نو دنبالهٔ منظم rōγn فارسی میانه است: واکهٔ میانجی خوشهٔ پایانیِ -غن را می‌شکند (rōγn ← rōγan)، که در گذر به فارسی نو رفتاری عادی است؛ تلفظ کهن‌تر رَوْغَن (rawγan) است و همین صورت را بارتولمه، هرن و باک نقل کرده‌اند. واژه در سراسر زبان‌های ایرانی مشترک است: کردی ڕۆن، بلوچی rōγan، پشتو روغن، مازندرانی راغون، یغنابی rūγan ــ همه از ایرانی آغازین *ráwgnah. بیت مولوی که در نمودار آمده («گر ببینم خانه‌ات را من دوام / روغن و شیرت بیارم صبح و شام») گواهی درست برای کاربرد عادی واژه است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/روغن\", \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ráwgnah\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:978\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 2 p.978 (BQT_v2_pages.txt leaf 441) is the روغن article, with Mo'in's footnote 'پهلوی rōγn ... اوستا raoγna- «بارتولمه ۱۴۸۸» ... کردی rōn ، بلوچی rōγan ...' plus Wakhi, Munji, Sanglechi and Sarikoli cognates — exactly the derivation the chart draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 632, p.140\", \"stance\": \"supports\", \"note\": \"'632. rōγen ,Butter, Öl^. Kāš. rūγān, rō. aw. raoγna- ,Öl^; phlv. rōkan (d. i. rōγan ...) ... kurd. rrūn; bel. (LW.?) rōγan, rōγan, n. rōγan, rōγin (327); LW. waχ. rūγn, rōγīn, minǰ. rōγūn, sangl. rōγ, sar. rōīm.'\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.72\", \"stance\": \"supports\", \"note\": \"'rōγn ... | N rawγan] oil, butter' — MacKenzie's own New Persian equivalent for the Pahlavi word.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/روغن\", \"stance\": \"supports\", \"note\": \"'From Middle Persian (lwkn' /rōγn/, “oil; butter”), from Proto-Iranian *ráwgnah, from Proto-Indo-Iranian *ráwgʰnas, perhaps from Proto-Indo-European *réwgʰ-no-s (“cream”).'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"rwğn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian rwγn (Buddhist/Manichaean, read rōγn / rōγᵊn) 'fat, oil' is the northeastern Iranian cognate and, as the chart correctly draws it, a sister of the Avestan and Middle Persian forms rather than a descendant of either: all three continue Proto-Iranian *ráwgnah independently. Gharib's dictionary puts the comparison explicitly in the entry. Beside it stand Yaghnobi rūγan (the modern continuation of Sogdian), Khwarezmian rγyn, Bactrian ⟨rwgn⟩ and Khotanese rrūṇa.\",\n          \"derivation_fa\": \"سغدی rwγn (بودایی و مانوی، خوانده rōγn) «چربی، روغن» صورت هم‌ریشهٔ ایرانی شمال‌شرقی است و نمودار درست آن را همتای اوستایی و فارسی میانه کشیده، نه بازماندهٔ آن‌ها: هر سه جداگانه دنبالهٔ ایرانی آغازین *ráwgnah‌اند. غریب در فرهنگ سغدی همین سنجش را در خودِ مدخل آورده است. در کنار آن یغنابی rūγan (بازماندهٔ امروزی سغدی)، خوارزمی rγyn، بلخی ⟨rwgn⟩ و ختنی rrūṇa قرار دارند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ráwgnah\"],\n          \"ref_check\": [\n            {\"ref\": \"SOD:345\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 8570 on printed p.345 (SOD_pages.txt leaf 413; leaf 411 carries the numeral 343): '8570 rwγn — rōγn ©Av. raoγna-, Pahl. rōγn, Khwar. rγn, Yaghn. ruγin ... fat, oil. TSP 2.897; BSTBL, Padm. 40, 54, Dhy. 279; STi 36.1, 43.9; ... Gersh. Sogd. Cpds. 1945, 147'. Nourai's number is a page, and it is right.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib no. 8570, p.345\", \"stance\": \"supports\", \"note\": \"See the quotation above; Gharib himself sets Sogdian rwγn beside Avestan raoγna- and Pahlavi rōγn.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ráwgnah (Descendants)\", \"stance\": \"supports\", \"note\": \"Descendants list: Avestan 𐬭𐬀𐬊𐬖𐬥𐬀; Khotanese rrūṇa; Wakhi rūɣ̌n; Bactrian 𐫡𐫇𐫃𐫗 rwgn; Khwarezmian rɣyn; Sogdian 𐽀𐼴γ𐼻 (rwγn /rōɣᵊn/); Yaghnobi рӯғн; Pashto روغن; Kurdish ڕۆن/rûn; Parthian rōɣn; Middle Persian lwkn' rōγn > Classical Persian رَوْغَن.\"},\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. col. 1488\", \"stance\": \"silent\", \"note\": \"Bartholomae lists only the Avestan word and its Pahlavi/New Persian continuations; he says nothing about Sogdian (the Sogdian material was not yet available in 1904).\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"raugna\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The printed page shows 'raugna : cream, oil' under the label Germanic, and the extraction is faithful — but no source knows a Germanic *raugna-. Both authorities Nourai cites here write the form with m: Klein (p.1307-08 s.v. ream) has 'Teut. base *rauma-, which corresponds perh. to I.-E. *raugma-', and Watkins has 'O-grade form *roughmen- in Germanic *rau(g)ma-'. The attested Germanic words are Old Norse rjúmi, Old English rēam, Middle Low German rōm(e), Old High German roum, Middle Low German rāme > German Rahm, all pointing to *raum(j)az/*rauma-, with -m-. 'raugna' looks like a contamination of Klein's I.-E. *raugma- with the Avestan raoγna- of node #1 — an author's misprint (or slip), not a scanning error. On the substance, the node is also the weak joint of the whole chart: Walde-Pokorny call the Iranian-Germanic equation 'höchst unsicher' and would rather take the Germanic words from *reu- 'tear open' via 'skin, layer of fat on milk', and Buck says the Avestan word's outside connections are unknown.\",\n          \"derivation_fa\": \"در صفحهٔ چاپی زیر برچسب «ژرمنی» نوشته شده «raugna : cream, oil» و داده‌های استخراج‌شده با کتاب یکی است ــ اما هیچ منبعی صورت ژرمنیِ *raugna- را نمی‌شناسد. هر دو مرجعی که خودِ نورایی ارجاع داده، این صورت را با «م» می‌نویسند: کلاین «Teut. base *rauma-, که شاید با هندواروپایی *raugma- برابر باشد» و واتکینز «Germanic *rau(g)ma-». گواه‌های ژرمنی عبارت‌اند از نورس کهن rjúmi، انگلیسی کهن rēam، آلمانی سفلای میانه rōm(e)، آلمانی علیای کهن roum و rāme ← آلمانی Rahm، که همه به *rauma- با «م» می‌رسند. «raugna» ظاهراً آمیزهٔ *raugma-ی کلاین با raoγna-ی اوستایی (جعبهٔ ۱) است، یعنی خطای چاپی کتاب، نه خطای خوانش اسکن. از نظر محتوا نیز همین جعبه سست‌ترین بند نمودار است: والده-پوکورنی این برابری ایرانی‌ـ‌ژرمنی را «بسیار نامطمئن» می‌دانند و واژه‌های ژرمنی را ترجیحاً از ریشهٔ *reu- «دریدن» («پوسته، لایهٔ چربیِ روی شیر») می‌گیرند، و باک می‌نویسد پیوندهای بیرونی واژهٔ اوستایی ناشناخته است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"raugna\",\n          \"correct_form\": \"*raugma- (Proto-Germanic *rauma- / *raumaz)\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ráwgnah\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1307\", \"status\": \"partial\", \"note\": \"Klein 1966 pp.1307-08 s.v. 'ream, n., cream': 'fr. Teut. base *rauma-, which corresponds perh. to I.-E. *raugma-, whence Avestic raoγna-, “butter”.' Klein supports the connection (with 'perh.') but writes *rauma- / *raugma-, never *raugna-.\"},\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. reugh-men-: 'O-grade form *roughmen- in Germanic *rau(g)ma- in Middle Low German rēm(e), cream: RAMEKIN.' Again *rau(g)ma-, with m.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 873 (POK_03.txt leaf 110)\", \"stance\": \"partial\", \"note\": \"'aisl. rjúmi m. ,Rahm^, ablautend ags. rēam, mnd. rōme, ahd. roum ,Sahne^, und mnd. rāme (für *rōme), woraus nhd. Rahm, mit ū schweiz. rūm ds.' — all m-forms; and the whole headword carries Pokorny's question mark.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 357 f.\", \"stance\": \"contradicts\", \"note\": \"'Höchst unsicher. ... Aber für die germ. Formen macht ags. rēoma, rēama „dünne Haut“ (vermutlich als „die abgerissene“ zu *reu- „aufreißen“) eine Gdbed. „Haut, Fettschicht auf der Milch“ und eine Gdf. *reu-, rou-, ru-m(en)- wahrscheinlicher' — Walde-Pokorny prefer to separate the Germanic words from the Iranian ones altogether.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, روغن, printed p.313\", \"stance\": \"partial\", \"note\": \"Aryanpur's Germanic column gives Old Scandinavian RIUMI, Old High German ROUM, German RAHM, Old English REAM — m-forms only, no *raugna.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"ream 1; ramekin\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both English words are Klein's and belong together, though they reach English by different routes. REAM 'cream, froth' (the first of Klein's three homonyms, distinct from the paper 'ream' < Arabic rizmah and from 'to ream' < OE rȳman 'to widen') is inherited: Middle English rem < Old English rēam 'cream' < Germanic *rauma-. RAMEKIN (also ramequin) 'cheese preparation baked in a small dish', hence the dish itself, is a 17th-century loan from French ramequin, itself from Middle Low German rāmken, diminutive of rām 'cream' with the diminutive suffix -ken (English -kin); Watkins files RAMEKIN as the sole English descendant of reugh-men-. So the node is right as drawn; only the Germanic reconstruction in its parent box is misprinted, and the ultimate tie to Avestan raoγna- carries the doubt recorded on the root.\",\n          \"derivation_fa\": \"هر دو واژه از کلاین‌اند و به هم پیوسته‌اند، هرچند از دو راه به انگلیسی رسیده‌اند. ream ۱ «سرشیر، کف» (نخستین هم‌آوای کلاین، جدا از ream «بند کاغذ» که از عربی «رِزمه» است و از ream «گشاد کردن» که از rȳman انگلیسی کهن است) واژه‌ای ارثی است: انگلیسی میانه rem از انگلیسی کهن rēam «سرشیر» از ژرمنی *rauma-. ramekin وام‌واژه‌ای است از فرانسوی ramequin در سدهٔ هفدهم میلادی، و آن از آلمانی سفلای میانه rāmken، مصغّرِ rām «سرشیر» با پسوند تصغیر -ken (همان -kin انگلیسی)؛ واتکینز RAMEKIN را تنها بازماندهٔ انگلیسیِ reugh-men- می‌داند. پس این جعبه درست کشیده شده است؛ تنها صورت ژرمنیِ جعبهٔ بالادست غلط چاپی دارد و پیوند نهایی با raoγna-ی اوستایی همان تردیدی را دارد که در بخش ریشه یاد شد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ráwgnah\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. reugh-men- lists only RAMEKIN ('Germanic *rau(g)ma- in Middle Low German rēm(e), cream: RAMEKIN'; index 'RAMEKIN reugh-men-'); Watkins does not enter English 'ream (cream)', which is dialectal/obsolete in modern English. So AHD covers half the node.\"},\n            {\"ref\": \"KLN:1307\", \"status\": \"supports\", \"note\": \"Klein 1966 covers both, on the pages cited: p.1307-08 'ream, n., cream; froth. — ME. rem, fr. OE. rēam, “cream” ... Cp. ramekin.' and (a few pages earlier, leaf 692) 'ramekin, also ramequin, n., a preparation of cheese with bread crumbs, eggs, etc., baked in a small dish. — F. ramequin, fr. MLG. rāmken, dimin. of rām, “cream”, which is rel. to OE. rēam, of s.m. See ream, “cream”. For the ending see suff. -kin.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. ream (3 homonyms), ramekin\", \"stance\": \"supports\", \"note\": \"Klein distinguishes 'ream, n., 20 quires of paper. — ME. reme, fr. OF. rayme (F. rame), fr. Sp. resma, fr. Arab. rizmah', 'ream, n., cream; froth', and 'ream, tr. v., to enlarge a hole ... fr. OE. rȳman' — so Nourai's 'ream 1' correctly picks out the cream-word.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 873\", \"stance\": \"supports\", \"note\": \"'ags. rēam, mnd. rōme, ahd. roum ,Sahne^' — Old English rēam, the direct ancestor of ream 'cream', is listed in the entry.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 357 f.\", \"stance\": \"partial\", \"note\": \"Has the same Germanic words but would derive them from *reu- rather than from the Iranian etymon, so the English words stay related to each other but perhaps not to raoγna-.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-424.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-14T01:41:29.098Z] TOOL RESULT

```
JSON OK
```


## [2026-09-14T01:41:33.592Z] TOOL CALL #77: Bash

```json
{
 "command": "python3 tools/verify_check.py 424"
}
```


### [2026-09-14T01:41:34.680Z] TOOL RESULT

```
nodes verified: 18/18
node verdicts: {'confirmed': 12, 'plausible': 4, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 13, 'not_checked': 6, 'partial': 4, 'not_found': 1}
books consulted: {'supports': 35, 'partial': 10, 'contradicts': 4, 'silent': 3} | by book: {'SKT': 6, 'SYN': 5, 'Wiktionary': 5, 'WLD': 4, 'PHD': 4, 'HRN': 4, 'POK': 4, 'ARY': 4, 'BRT': 3, 'AHD': 3, 'FRS': 2, 'MON': 2, 'BQT': 1, 'IEC': 1, 'HUB': 1, 'NYB': 1, 'SOD': 1, 'KLN': 1}
```


## [2026-09-14T01:41:56.196Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-424.json` written; `verify_check.py 424` reports 18/18 nodes, 0 PROBLEM lines.

**Page 424 (book 394) — 3 non-redirect entries (Reudh 1, Reug, Reughmen), 18 nodes**

- Node verdicts: 12 confirmed, 4 plausible, 1 disputed, 1 transcription_suspect
- Root verdicts: 2 confirmed (Reudh 1, Reug), 1 plausible (Reughmen)
- Ref checks: 13 supports, 4 partial, 1 not_found, 6 not_checked (all MON — the 6-vol Mo'in has no page-mappable copy online)

Flagged items:
- **disputed** — Reudh 1 #3, Persian `ronâs` روناس "madder": Horn 141 (Nourai's source) only says "wohl zu aw. raoiδita-"; modern work (Löw *Aram. Pflanzennamen* 363, Minorsky 1955, Monchi-Zadeh 1990 no.440, Wiktionary) derives it from Ancient Greek ῥόϊνος "pomegranate-coloured", possibly via Aramaic/Syriac, with رویناس a secondary reshaping under روی. The other word in the node, روی *rūy*, is confirmed.
- **transcription_suspect** — Reughmen #5, Germanic `raugna`: no source knows Gmc *raugna-. Klein 1307 has Teut. *rauma- / IE *raugma-, Watkins Gmc *rau(g)ma-; all attested forms (ON rjúmi, OE rēam, OHG roum, G Rahm) have -m-. `error_in: "book"` — the printed page does read "raugna"; extraction is faithful. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/424.png`.

Other notable findings (not extraction errors):
- **POK:837 is wrong** on the Reughmen root *and* on node #1: IEW p.837 is the *pleu-* "flow" article; `reugh-m(e)n- ,Rahm‘?` stands on p.**873** (Watkins cites 873 too). Digit transposition by Nourai.
- Root Reughmen downgraded to *plausible*: the Iranian side is certain, but Pokorny question-marks the headword, Walde-Pokorny II 357f call the Iranian–Germanic equation "höchst unsicher", and Buck §5.89 says Av. raoγna- has "outside connections unknown".
- Latin `rôbeus` (Reudh 1 #4) is a real dialectal Latin word, but rouge/ruby descend from *rubeus* — as Nourai's own cited AHD says. Marked plausible.
- Pahlavi/Persian `rôy` is glossed "zinc"; Horn, MacKenzie and Wiktionary/Edelʹman all give "copper, brass" — "zinc" is the modern chemical sense. Marked plausible.
- `rŭž «روژ»` (Reudh 1 #6): the French loan is correct, but standard Persian spells it رژ; «روژ» is the book's own spelling (verified against the page).
- Confirmed exactly as drawn: HRN:141 nos. 634–635 (the whole Persian box), BQT:978/980/981 (Mo'in's footnotes located at vol. 2 leaves 441/443/444), SOD:345 (Gharib entry 8570), POK:871 (which names "npers. ā-rōγ" itself), KLN:1307–08 (ream/ramekin).

**No extraction errors found** — every form in `page-424.json` matches the printed page.
