# Verification process log — verify-page-560


## [2026-10-17T00:30:14.205Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 560 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-560.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-560.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-560.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 560` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.243Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:19.474Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:19.509Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
225	
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
231	command stuck. List files with `command ls` or `find` instead.
232	
233	```json
234	{
235	  "pdf_page": 126,
236	  "book_page": 96,
237	  "verified_by": "claude-opus-5",
238	  "verified_on": "2026-09-05",
239	  "entries": [
240	    {
241	      "entry": 0,
242	      "root": "Dheigh, Dhigha",
243	      "verdict": "confirmed",
244	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
245	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
246	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
247	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
248	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
249	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
250	      "nodes": [
251	        {
252	          "id": 6,
253	          "lang": "Avestan",
254	          "words": "pairi-daeza",
255	          "verdict": "confirmed",
256	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
257	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
258	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
259	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
260	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
261	        }
262	      ]
263	    }
264	  ]
265	}
266	```
267	
268	Rules:
269	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
270	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
271	- `words` = the transliterations of the node joined by "; " (copy from the chart).
272	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
273	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
274	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
275	- If a node lists several words, cover each word; if they differ in verdict, use the worst
276	  verdict for the node and explain per word in `derivation`.
277	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
278	  scholarship takes.
279	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
280	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
281	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
282	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
283	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
284	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
285	  any extraction errors (JSON differs from the printed page) the owner must fix.
286	  Do not paste the JSON back into your reply.
287	
```


## [2026-10-17T00:30:19.968Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-560.txt"
}
```


### [2026-10-17T00:30:19.999Z] TOOL RESULT

```
1	=== PDF page 560 (book page 530) ===
2	--- entry 0 ---
3	ROOT [Sogdian] `Xšnk : nice  (refs SOD:28)
4	#1 (parent #0) [Sogdian] refs=SOD:28 | gašnaka : nice
5	  #2 (parent #1) [Persian] refs=SOD:28; MON | qašang «قشنگ» : beautiful
6	--- entry 1 ---
7	ROOT [Avestan] Xvaini : cover, carpet  (refs SNS:59; HRN:110)
8	#1 (parent #0) [Pahlavi] refs=HRN:110; AEF:640 | xvân : table cloth, food table | NOTE: Hubshmân does not agree with this derivation.
9	  #2 (parent #1) [Persian] refs=BQT:783 | xân «خوان ۱ ( خوانچه )» : food table, table cloth
10	
```


## [2026-10-17T00:30:20.598Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-560.json"
}
```


### [2026-10-17T00:30:20.619Z] TOOL RESULT

```
1	{
2	  "pdf_page": 560,
3	  "book_page": 530,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "`Xšnk",
8	        "lang": "Sogdian",
9	        "refs": "SOD:28",
10	        "gloss": "nice"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Sogdian",
17	          "refs": "SOD:28",
18	          "words": [
19	            {"translit": "gašnaka", "gloss": "nice", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Persian",
28	          "refs": "SOD:28; MON",
29	          "words": [
30	            {"translit": "qašang", "gloss": "beautiful", "script": "قشنگ"}
31	          ],
32	          "note": null,
33	          "quote": {
34	            "text": "زی فرنگستان سه کرت شاه ایران راند خنگ - خواست تاایران شودهمچون فرنگستان قشنگ",
35	            "poet": "Bahâr"
36	          }
37	        }
38	      ]
39	    },
40	    {
41	      "root": {
42	        "name": "Xvaini",
43	        "lang": "Avestan",
44	        "refs": "SNS:59; HRN:110",
45	        "gloss": "cover, carpet"
46	      },
47	      "nodes": [
48	        {
49	          "id": 1,
50	          "parent": 0,
51	          "lang": "Pahlavi",
52	          "refs": "HRN:110; AEF:640",
53	          "words": [
54	            {"translit": "xvân", "gloss": "table cloth, food table", "script": null}
55	          ],
56	          "note": "Hubshmân does not agree with this derivation.",
57	          "quote": null
58	        },
59	        {
60	          "id": 2,
61	          "parent": 1,
62	          "lang": "Persian",
63	          "refs": "BQT:783",
64	          "words": [
65	            {"translit": "xân", "gloss": "food table, table cloth", "script": "خوان ۱ ( خوانچه )"}
66	          ],
67	          "note": null,
68	          "quote": {
69	            "text": "اَديم زمین ، سـفـرۀ عـام اوسـت - چهدشمن براین خوان یغما، چه دوست",
70	            "poet": "Sa`dî"
71	          }
72	        }
73	      ]
74	    }
75	  ]
76	}
77	
```


## [2026-10-17T00:30:24.387Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['SOD','MON','SNS','HRN','AEF','BQT','HUB','PHD','NYB','CHEUNG','ARY','BRT','KNT']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"; command ls sources/refs/ | head -100"
}
```


### [2026-10-17T00:30:24.882Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
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
KNT_full.txt
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
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
```


## [2026-10-17T00:30:26.505Z] AGENT

Let me look at a previous output file for format, then grep sources.


## [2026-10-17T00:30:28.436Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;d=json.load(open('page-558.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in d.items() if k!='entries'}));print(json.dumps(e,ensure_ascii=False)[:2500])\"; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['SOD','HRN','HUB','SNS','BQT','MON','PHD','NYB','ARY']:\n  print(k, d[k].get('page_offset'), d[k].get('lookup_hint','')[:600]);print()\n\""
}
```


### [2026-10-17T00:30:28.976Z] TOOL RESULT

```
{"pdf_page": 558, "book_page": 528, "verified_by": "claude-opus-5.5", "verified_on": "2026-10-16"}
{"entry": 0, "root": "Xac 1", "verdict": "plausible", "modern_form": "Skt. khac- 'shine through' (?) (Buck, after Uhlenbeck); modern view: Skt. kāca- probably a Nuristani loan, cognate with Skt. kāś- 'to shine'", "note": "The book files this chart under X because Nourai writes Skt. kh as X ('Xac' = Skt. khac-). The root and gloss come straight from Buck SYN 620, who gives it with a question mark: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' Wiktionary (after Mayrhofer) calls kāca- 'likely borrowed from a Nuristani language (*kāt's'a), cognate with Sanskrit kāś- to shine brightly'. Either way, a 'shining' root sits behind the glass word, so the chart is defensible, but the specific root khac- is uncertain. The extraction matches the printed page.", "note_fa": "نورایی ریشه را سنسکریت khac- «از درون درخشیدن» می‌گیرد (او kh سنسکریت را X می‌نویسد، از همین رو این مدخل زیر حرف X آمده). این ریشه را باک (SYN ص ۶۲۰) به پیروی از اولنبک، و خودش با علامت پرسش، آورده است. ویکی‌واژه به نقل از مایرهوفر سنسکریت kāca- «شیشه» را احتمالاً وام‌واژه‌ای از زبان‌های نورستانی (*kāt's'a) و هم‌ریشه با kāś- «درخشیدن» می‌داند. پس پیوند «شیشه» با ریشه‌ای به معنای درخشیدن پذیرفتنی است، اما خودِ ریشهٔ khac- قطعی نیست و ادعای نورایی را باید با احتیاط پذیرفت.", "sources": ["https://en.wiktionary.org/wiki/काच"], "ref_check": [{"ref": "SYN:620", "status": "supports", "note": "SYN.txt (printed p. 620, section 9.74 GLASS), para 7: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' This is exactly Nourai's root and gloss, including Buck's hesitation."}], "consulted": [{"src": "POK", "where": "POK_full.txt grep 'kāca|kāś-|kāçat'", "stance": "silent", "note": "no Pokorny entry for Skt. kāca- or kāś-."}, {"src": "WLD", "where": "WLD_Bd1/Bd2_pages.txt, WLD_band3.txt grep 'kāca'", "stance": "silent", "note": "no hit."}, {"src": "AHD", "where": "AHD_watkins1985.txt", "stance": "silent", "note": "no IE root for Skt. kāca- (an Indo-Aryan word with no European cognates)."}], "nodes": [{"id": 1, "lang": "Sanskrit", "words": "kâca", "verdict": "confirmed", "derivation": "Skt. kāca- m. 'glass, crystal, quartz' (classical, post-Vedic). Buck lists it as the Sanskrit word for GLASS and tentatively links it to khac- 'shine through'. Wiktionary instead suggests a Nuristani loan cognate with kāś- 'shine'. It continues in Pali kāca, Hindi kā̃c, Bengali kāc, Malay kaca. The gloss 'pearl' comes from Mo'in's BQT footnote, which cites Monier-Williams for 'شیشه، آبگینه، مروارید' (glass bead). The word and 
SOD printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/Sog

HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

SNS 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh

MON None Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a

PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

ARY printed page = pdf page + 1 Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image
```


## [2026-10-17T00:30:34.362Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"xšnk|xsnk|xšnk|gašnak|gasnak|qašang|qasang|beautiful|nice\" SOD_pages.txt | head -40"
}
```


### [2026-10-17T00:30:34.727Z] TOOL RESULT

```
5823:719 >YSVn)k S                                     A^<>^           (o)xsank/-g ©<*gasnak(k)a- ©ob, -y; pi. -*>
5824:    (o)xsawanc =»xsywny(y), }xswny                                  =^xsnk-, xsnq-
5825:    king, ruler                                                   beautiful, splendid
5831:                                                                  (o)xsankawe ^xsnkWk
5844:    kingly    ?                                                   more beautiful
9832: 2089 >xsnk- M                       Xii <.j£iL «L> j                king, ruler
9835:      ox(a)sang (xsnk) ©pi. -0 =»}Ysnk-
9836:      beautiful, splendid                                      2101 'xsy- =» }YS*y-, xsy-
9837:        GMS     157, 511, 981, 1204; f.adj. >xsnk\ KG; MSP     2102 >xsypt-    S => >xs>y|3t-
9838: 2090 'xsnkNv'k S                                J^ojfc        2103 »xsyc   M                   jjulT ^cjT ^qjulT ^<L^j < ^y*
9843: 2091 'xsnq'wyh       M ** ,xsnk)w,k                          2104 »xsy5 M                                  jiJL^l<^l<r,>U>
13495:       beautiful, fine, DapatO/ze ha/we o/ a godess)
16142:4348 ywpny      M                                                ox,>.         nice, pleasant
17557:             beautiful
17714:     beautiful                                                 4927 kstyy M =» kst>k
17719:     more beautiful                                                 Hen. Tales. 47526; STi 52.8; Sund. AoFviii 1981
30056:     finer, more beautiful                                           9132 syngtync M               (<_^La)JL^w*(<j Lfjj^*) i^jJOx^M
30915:        good, nice
30950:                                                                         nice n 2, 1210
34584:10656 xsnk =» }xsnk-, xsnq-                                           xsipd   ©<Av. xsvipta        =»}YSypt, 'xs'ypt-
34588:       xsang ©ob. -y =^xsnk-, >Ysnk-
34724:      xwasa6-tasa5                                                 nice, sweet, pleasant
35173:      niceness
37717:beautiful 731, 2089, 3410, 4858,      (to)bc disturbed     360, 1140, 5389    (to)be lead      9221
38927:more    beautiful   734, 4915, 9119     mourning     5221
38982:nice    4359, 9408, 9433, 10714         not drawn     5807                   (tofoblain     568, 2965, 3020, 3029
38983:niceness     10839                      not fated    5732                    obtained      2150, 3031, 3033
```


## [2026-10-17T00:30:37.720Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5815,5850p SOD_pages.txt; echo ----; sed -n 9825,9850p SOD_pages.txt; echo; awk 'BEGIN{RS=\"\\f\"} /2089 >xsnk/ {print NR-1}' SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} /719 >YSVn/ {print NR-1}' SOD_pages.txt"
}
```


### [2026-10-17T00:30:38.092Z] TOOL RESULT

```
717 'YsWnh -* 'Ys'w'n'h
                                                                  axsnam ©Av. xsnaoma- ^'xsn'm
718 ^sWnty    S                                 sz.M~<^\±         pardon, indulgence
    (o)xsawande                                                   GMS 157; VJ 1225, 1387, 1452; TSP 5.107, 7.47;
    rule
                                                                    SCE 194; BSTBL, -w, Dhy. 79
     Karab. Insc. 22.9; BBB b69
                                                              731 JYsnk- B, S          (i^j^ j<> Jj~*)oj&>1 t<JLji3
719 >YSVn)k S                                     A^<>^           (o)xsank/-g ©<*gasnak(k)a- ©ob, -y; pi. -*>
    (o)xsawanc =»xsywny(y), }xswny                                  =^xsnk-, xsnq-
    king, ruler                                                   beautiful, splendid
    Karab. Insc. 18.13, -w
                                                                  BSTBL, -y, Intox. 7; Frag. Len. 27.9, 44.3; GMS
720 ^sVnSV S                                     lj»eli             511; Sogdica. 20.1; S W, BSOAS 1983, 48
    (a)xsawan5ar, oxsonSar       Oxswnd'r)
    ruler                                                     732 'YsnkNv'k S                            ^Lti^^fc
                                                                  (o)xsankawe ^xsnkWk
    Karab, Insc. 15.4,7
                                                                  splendour, beauty
721 ,Ys)wn8,ry =* ^s'w'nS^y                                       Frag. Len. 44.14
722 'ys'wnyh =» 'y^w'n'h                                      733 JYsnkJwy(h)   S                               6J&

723 ^s'y- B                 d>/c-*£~ ^J'^.M...                    (o)xsankawe/-wya ? Oxsnq'wyh)
    (a)xsay Oxsy-) ©Av. xsa(y)- =*xsy-                            splendour, beauty
    (ro)rulc                                                      Frag. Len. 61, 10
    VJ 1094; GMS 1086
                                                              734 'Ysnkystr S                                jS~z5
724 >Ysy>5 S                                 jzU-wjsf             (o)xsankistar
    (o)xsaya5
    kingly    ?                                                   more beautiful

                                                                  Frag. Len. 27.6
    MDii 128n9, B-16, 9
                                                                                                                      'Yt'w
 29
                                                                   milk
----
        GMS 130, 157; BBB f 11; Sogdica. 33.12b
                                                                     BBB; GMS 414a, 571; Hen. Tales. 470.49
 2088 'xsn'w- M                        o^y^-
      oxsnaw (DAv. xsnavaya- =^xswndyy                         2100 'xswny M                                               j&
      Go)satisfy                                                     (o)xsawane, sxsone ? ©pi. -/ ^'xsWn,
      GMS 157,414a, 571; AVS 96

 2089 >xsnk- M                       Xii <.j£iL «L> j                king, ruler
                                                                       ^s'wn'k
                                                                     Hen.  AM 1952, 203.12
      ox(a)sang (xsnk) ©pi. -0 =»}Ysnk-
      beautiful, splendid                                      2101 'xsy- =» }YS*y-, xsy-
        GMS     157, 511, 981, 1204; f.adj. >xsnk\ KG; MSP     2102 >xsypt-    S => >xs>y|3t-
 2090 'xsnkNv'k S                                J^ojfc        2103 »xsyc   M                   jjulT ^cjT ^qjulT ^<L^j < ^y*
      oxsankawe Oxsnq'wyh) -^ysnkWk                                 axsic   ^'ksyc
      magnificence, splendour
                                                                    pulling instrument
      KG 421; Sogdica. 17.23; GMS 1082                              GMS 343, 1002; Sogdica. 30.11
 2091 'xsnq'wyh       M ** ,xsnk)w,k                          2104 »xsy5 M                                  jiJL^l<^l<r,>U>
 2092 >xsnyrk(,) M                         c-ou«Ai;                o/axse5
                                                                   ruler, king©<Av. xsaeta          ^'ysyS, xsyS, ys>y5
      oxsnirk -^ysnyrk^, xsnyrq
      sign, mark                                                    GMS 269, 1189; Hen. BSOAS           12, 302, 110
      BBB 758; GMS 976; Sund. KG pl80, 529, 621,              2105 'xsyspt pyy       M        jUjb- J ^JL fi)*^ ^sXjj^
        -*\ 616, 622, -jfcw, 526
                                                                                                   (ox j £ j j al^~i jl <<jy^

148
93
```


## [2026-10-17T00:30:46.582Z] TOOL CALL #8: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/قشنگ",
 "prompt": "Give the full Etymology section verbatim for the Persian entry, and any other languages' etymology."
}
```


## [2026-10-17T00:30:47.660Z] TOOL CALL #9: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/خوان",
 "prompt": "Give the full Etymology section verbatim for every Persian entry (especially the one meaning tablecloth/table of food), including cognates and cited sources."
}
```


### [2026-10-17T00:30:52.076Z] TOOL RESULT

```
# Etymology Sections

## Persian

"From Sogdian _ʾγšnk-_ ((ə)xšank, "beautiful"), Northern Luri _خشںݩ_ (xşəŋ), related to Proto-Iranian _\*gr̥šáti_ ("to rejoice, be happy")."

## Urdu

"From Classical Persian _قَشَنْگ_ (qašang, "beautiful, lovely"), ultimately from Sogdian _ʾγšnk-_ ((ə)xšank, "beautiful")."

The Khalaj entry contains no etymology section—it only notes this represents an "Arabic spelling" of the term meaning beautiful, pretty, or handsome.
```


### [2026-10-17T00:30:54.722Z] TOOL RESULT

```
# Persian Etymology for خوان (xwān/xân)

## Etymology 1 (Noun: Table/Tray/Tablecloth)

**Source text:** "Inherited from Middle Persian [Book Pahlavi needed] (hw'n' /⁠xwān⁠/, "tray, table")."

The entry traces this term back to Middle Persian, where it denoted dining surfaces. Cognate forms include Avestan _xᵛaini_ ("cover, carpet") and Old Armenian _խան_ (xan), which is identified as an Iranian borrowing.

**Descendants:** The word spread to Middle Armenian _խօն_ (xōn), Modern Armenian _խոն_ (xon), and Urdu _خوان_ (xān/xvān, "tray").

## Etymology 2 (Verb: Present stem of "to read")

This represents "present stem form of _خواندن_ (xwāndan/xândan, 'to read')."

## References Cited

The entry includes three scholarly sources:
- Steingass, Francis Joseph (1892) — *A Comprehensive Persian–English dictionary*
- MacKenzie, D. N. (1971) — *A concise Pahlavi dictionary*, page 95
- Nourai, Ali (2011) — *An Etymological Dictionary of Persian, English and other Indo-European Languages*, page 530
```


## [2026-10-17T00:31:00.420Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==132' HRN.txt | grep -n -i -B2 -A12 \"xvan\\|chvan\\|xwan\\|hvan\\|x'än\\|xvän\"; echo ===HUB; grep -n -i -E \"x[vw]än|xvan|x.än .tisch|Tisch\" HUB.txt | head -20"
}
```


### [2026-10-17T00:31:00.992Z] TOOL RESULT

```
Exit code 1
(eval):1: ==HUB not found
```


## [2026-10-17T00:31:03.648Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 130 131 132; do echo \"=== leaf $((n-1))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | grep -n -i -A10 \"tisch\\|tafel\" ; done | head -80"
}
```


### [2026-10-17T00:31:03.997Z] TOOL RESULT

```
=== leaf 129
=== leaf 130
=== leaf 131
23:498. x^äW/ 'Tischdecke; Tisch (gedeckter)'.
24-aw. /^'^aini' 'Teppich, Überzug, Decke',
25-kurd. LW. /an; af/. /^än; bei. n. vän 'Platte, Teller'
26-(289).
27-Geldner, Studien I, 17/8.
28-499. yiyänden Vufen, lesen etc.', /emden, /unlde, /unyä
29-'Musik, /unyäyer,
30-aw. l/";^^«;/- in /^anaf.ca/ra- ('klirrend'); phlv.
31-X'^äntan, /untt (GF.) ; ai. [/^svan-, sodnati 'tönen'.
32-kurd. y^ändin^ /ündin 'lesen; oss. d. /önim, i. xöJiin
33-'nennen , heissen , rufen , einladen' (305) ; bei. vänag,
```


## [2026-10-17T00:31:11.666Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *498[\\.,]|aini|Teppich\" HUB.txt | head; echo ===BRT; grep -n -i -E \"aini-|Teppich\" BRT.txt | head -20; echo ===PHD; grep -n -i -E \"^x[wv]?[aā]n |table|tray\" PHD.txt | head -20; echo ===NYB; grep -n -i -E \"x[wv]ān|table\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-10-17T00:31:12.103Z] TOOL RESULT

```
Exit code 1
303:klar, noch weniger kurd. nainih Afgh. dhina, ahTna^
970:LW. pastar 'Decke, Teppich*, das mit einer andern
1355:= ap. *paruviyaini' = np. parvm?
1958:498. Zd. x^aini" wird von der Phi. tTbersetzung durch
2677:(skr. *gumbhaini) hinweist. Sonst konnte auch iran.
2968:vermuthet *Teppich\
3305:Das Praesens giryam ist nicht aus ap. *giryainiy,
3913:'Kocher bedeutet. Zd. zaini-s wird durch phi. zin
4283:gaona- ; zanbar *Sanfte* = arm. zanuar = zd. "^jainibara- ;
6334:wohl Teppich* bedeutet und = phi. bop 61. and Ind. 82,
(eval):1: ==BRT not found
```


## [2026-10-17T00:31:15.735Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1955,1966p HUB.txt; echo \"-- BRT\"; grep -n -i -E \"aini-|Teppich|Überzug|Ueberzug\" BRT.txt | head -20; echo \"-- PHD\"; grep -n -i -E \"^x[wv]?[aā]n\\b|tray\" PHD.txt | head -20; echo \"-- NYB\"; grep -n -i -E \"x[wv]ān|xvān|\\btable\\b\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-10-17T00:31:16.221Z] TOOL RESULT

```
*) Im Skr. stiinde krmami fiir *krnatni wie hhrmami ffir ^bhrnami.
8. p. 28, Anm. 4 und skr. kraya- *Kauf neben krl wie zd. harOii^a'
neben hhrl.- 57 —
498. Zd. x^aini" wird von der Phi. tTbersetzung durch
xup *schon* wiedergegeben, das vollkomnien passt. Die
Zusammenstellung ist also falsch.
501. Np. x^ahar Schwester aus ^jf'ahar, vgl. skr. ace.
soctsaram, Ahnlich ware np. bahar 'Friihling' = phi.
vahar aus *vahar entstanden, wenn es zu ap. d^uravo-
hara- geh5rt.
502. Dazu np. nctnx^ah 'Ammi' u. s. w. als *Brot-wurze',
afgh. x^and 'Geschmack, Wohlgeschmack, Vergniigen
-- BRT
3413:•  j.  *a-ftTvayaDha-  n. 'NJchtgefahr,  Gefahr- \a%\^^\'C:*a'i:ra'"tih}m>''ya'i:raratui'i:wa- yar)k?m  ya^ra  apprmaynkö  3  *hg  "aini- iritim  starydti  ar,a  yat  v3  ya'^ra  '^waya- n/um  va  "»fum'^  t^S  "(ist)  daNichtgefahr, wo  der  R.,  Gefahr,  wo  der  Knabe  (sich befindet),  so  begeht  er  Sünde,  wenn  er ihn  (dem  Ratav)  nicht  anvertraut;  und (auch)  wenn  beide  (sich  an  einem  Ort befinden),  wo  sei  es  Gefahr  oder  Nicht- geiahr  (ist)"  N. /o'\
5703:Sagartien . ."  D.5.  2;  —  hauv  °lam  haini- '^''iyam  akunauS  Eh.  4-2;  —  adam xSayäHy<^  amty  -laiy  Bh.  2.  14,  4-  2,  Bh-g.
8378:•  j.  upa.^t9r9na-  n,  'Decke,  Teppich': zaranalne  patli  g3tv5  zaranasne  paiit/ia- spaiti  taranagiie  paiti  'ne  Yt  75.2.
13412:sppnie  mainyui  yasca  a»rd  ¥.57.17;  Yt.  xfaisa  Atn-anam  'mtrttamY.S  s;¥iVi.4.3; jy.  76,  /5.  3;  —  ■!'.»  °ma  (als  AD.)  .  .  —  avU  'man  asai-anö  yazamaide  yä  hmti jasca  dairal  sppntd  mainyui  yasca  daial  paoirySjiäta  paoiryS.fraiwarsta  amäatca .. at^rS  mainyu/ \t  t^.  43;  —  zara^uitra  Vr.7.4;  —  pauna  data  °man  aIaonls\. . ,  yS  . .  i'friirrojastfinö  abavat  mainiva  16.3;  \1.11.2,  VyL^j;  —  asa.paoiryjis^a •man  (GS.)  ¥.5.15;  \.ig.\z-,  —  fra-  'mSbls\.ig.\^\  Vr,;<?.2;  —  manas.paoir- rasayö  . .  h^titi  ySsktnsbmä  uvayä  *maini-  y(üibyB  °mabyS  Y.  Z^.  12;  Vi.  ig.  i ;  —  ^a/ vä  'man  VLy-76;  —  ^lyS  >wdr?!tira\'ma  (AS.)  asava  yaozdäir m  YL^.a;  — ya  vispa  'iwjrpsatS  'man  (AP.)  \. ^■j.2;\yaozdätimm  ankam  'manqm  vahisiqm  \'i. Yt./9.94;  —  aam  vTsfianqm  'manqm'  10.^2;  —  tisirlm  . ,  yS  ..  nafmiaiii  (sd.) nipäta  ahmt  Yt/O.54;  54;  — fravasaysX . .  vTspSst  13  'man  baZsasyatica  YtÄ43; vUpä  *'mqm  (AP.)  savavuhaitis  (sA)  V.  |  —  kihrpa  avavats  *sraya  (sd.)  ya'ia  'man '9-ZTi  —  tsm  ..yazat»m  ..'mdhu  iftistfm'.  sraäläis  H.  2.  9;  YLJO.141;  — '  anra mnr>m  yatäiSx.lo.6; — y5i  "i^wä  vamm  '  mainyS  janäni   'ma  dalvsJlUm  .  .  paili
14123:j2.io"; —  nsil  >r>s.vacä  sarSm{sA.)didqs\yi  'vaitls  V.  20.10  i  —  ailm  dahäA^m  . 'gvätä  hyal..aiä  yuxta{,&A.)  Y.4i?.9";  — 'vantim  Y.().  8;  Yt.5. 109;  —  'vä  saini- antarS  vXspTng  °gvatB  haxm}ng\..\  mruyl\gäui  Yt/p.93;  —  tat  'vatö  'vatam  .  . (Sp.  134111.)  Y.49.3;  —  mit  tnzfjysi.tat  'vats  -vatyäsca  .  .Yt.11.2;  Vyt^7(?); frajylitii  (sd.)  nBit  fiuymtl  'gfasü  pairl  —  tarn  ahüm  .  .  yim  'vatqm  V.5.62;  — Y.  2(). 5;  —  yS  "'guB-dbls  a^am^m  (sd.) .  in  gAw.  Form:  vi  zl  anä  (sd.)  sarsm vädäyBitY.2g.2;  —  ksi^'gvB.dibts  xraräÜ\mruyl ya^anä  'gvätä  (IS.)  *rqxfyania  Y. rämqm  (sd.)  dantl  Y.  ^ä*.  11;  ^  kyat  12. 4.  U)  von  den  Göttern  des  Drug- *ainatih£  'gvaiff  3:>äri/2  i^jtig  ar?hayälsd.)'\g\&abens;  i)  im  gAw.:  aya  *mainiva Y.^2. 16;  —  ka'hä  asäi  drujim  dyqm\varata  yS  'gvä  aastä  virizyB  ahm  main- zastayd  (sd)  .  .  imavaiilm  sinam  dirvBi^yus  spfriistü  ".  .der  zur  JJrug  habende.,  der (sd.)  'gvasB  V.4/.14;  —  ya>rä  ««(»ywj-';  heiligste  Geist"  Y.jo.j.  2}  im  jAw.,
17941:•  ').  *fra-spat-  ra.  (etwa)  Ttissen,  Pfuhl': taraname  paiti  gätvs  zaraaafae  paiti 'späiti  taraname  paiti  upastirme  "auf goldenem  Thronsesset . .  Kissen .  .Teppich"
17943:Et  ?  —  np./ar<jj/  (aus  \t.*friupäslH%)  'Teppich' ; GIrPh,  /  b.  IQI.
18948:KompA.,  E.;  vgl.  auch  *»^maÜj.  —  Zum  V. nam-  '(sich)  heraL beugen',  vgl.  nhd.  reit  und ags.  Aiissan  'liltem'.  S.  auch  JOHANSSON  IF. 3.  54.  —  np.  namad  'grober  Teppich;  Filz'  3).
25679:•  g.  urvätay-  f.  'Gelübde':  y7  va  xlayqi aäqs  drtta  ayantpm  'ISil  vä  huzSntus  mt- hrsiiys  vä  ramä  jvqs  yS  asavä  dngvan- tfm  "wenn  ein  wissender  einen  zu  halten vermag,  nachdem  er  ihn  dazu  gebracht hat,  von  seinem  Gelübde  und  seinen  Bin- dungen weg  (zu  ihm)  überzugehen,  einer der  nach  der  Satzung  lebt,  ein  .i^ntanhänger einen  Druggiuos&en"  Y.46".  5.
28704:.  j.  'haena-,  p.  haini-  f.  'Heer,  Heer-  ■  ■  ^'^  Z'^",  h«^_^rinHi  .  .  a3aih>a schar'  uzw.  rfa?^ischer  Wesen,  'Feindes-  'i^^lsva  . .  hau  astt  äafvö. .  avat  daa,a heer,  feindliche  Heerschar':  Wabiy  imäm  ^^'"'^'"■'»^  ' . .  (sva.)  dort  ist  der  Z>. . daÄyäum  mä  5>;/.,>J*  ma  'nä  D.4.3;  V-Z-SafO;  _  s.  noch  H.1.7  (Sp.173»  o.); ^  n^it  i^ra  atryA  dai^hävS  fräs  (%A..)  "  ™  Gegensatz  zu  ÄJ  (Sp.  1718  o.):  >Sff yiyj/  •;«»  YtÄs6;  F.l-^;  -  ^«laäa  «P^-m^r^tS  i%^.  1143  m.)  ,4 5 «  ,.j-;tjr^.- «(■rr-^-b'iT  rfa/Vi^«4>.S  ■««  (NP.)')  frapatänti  '""'^  iäW  ..V.4.AS;  -  zugleich  aul  ein Yt..y.6i:  —  ya'ba  yai  hazarirS.aspam  erläuterndes  Nomen  vorausweisend:  aoa 'nam  avazeit  mäzduya'sni!  avi  vis5  Y.  hau  apa^^arS bvatzraya»ks vouru.kaiahe i8'.i^;  -  Ümäm  daAyüufn  ^ura^mazdj  ^""^  yH  haosravA  nqma  Ytip.sS;  59, patup  haia'nmD.4.6;  —  'nayä^axra-  ^'-  ")  '"  schwachdciktischer  Vcr- vai^yä  z>yazJayä  (sd.)  Aog.  A;  Yt  5.  131,  Wendung  jener,  der';  I)  zurückweisend; 4.  3.  19-  93,  ^-  II  (wo  'nayiuay-'nyhla  ^  *"/  f  ?  ^^O'uen;  a)  auf  ein  Substantiv; .  .  davai^yi  pataihyä  Y.0.18;  —  fiairi  «>  adjektivisch:  II  War««*  näm^  pärsa* ^•nyhsia  pöiynäuyS  Y.  68. 13;  -  ivi  'nayi  1  ■  ■  ''/'"'  ^'^rnaf  hada  kärä  al,yav^  Bh. (AP.)'>  xrvi^ätl!  Yt  10.  8;  />  49,  /<?.  54;  1  ^-  K^^'  '■  »?'  ^-  ?-  5-  • !  —  'Jäw«  /Jwa« —  ;*a.n<i>7'a/4yff*-«ÄS;'?"  Y.i7.asi>.  ^fi-ätfayam  . .  ya-^a  hauv  karJ'  parä- Ableit.  —  Zum  V.  ^(>>.  —  ai.  sinä-  f.  '"öJir  . .  Bh.  5. 1 ;  ü  —  »flr?m  afavarum  .. 'Heer';  mp.  (Pü.)  Äe«.  —  ')  NPn.  aUtt  NPf.  j  *hau  *n3"  .  .  P.2^;  —  zugleich  auf  ein (wie    umgekehrt,  S   ¥"■    3  d).     Vgl.    dazu  1  Rglativum    vorausweisend:    Wkärt/'    hyi^
-- PHD
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
655:wistardan, wistar- [wstl-tn! | N gustardan] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bile. wišād [SLYTWNt', Р! | M wid, N gušād] open, wide, loose. wišādan, *wišāy- [SLYTWN-tn! < A У šrh; wPtn! | M шурап, (wys?h-), N gušādan, gušāy-) open, loose, free. wišād-dar [.SL Y TWNt! BBA] hospitable. wišād-dwārišnīh [zP??! dzb?lšnyh) going about ‘open’, i.e. without kustīg, or šabīg. | wišān- [w®n- | = P] shake down. *wišāy-, v. wišādan. wiškar [zo£hl | N bisgar(d)] hunting-ground, wilderness. wiškīdan, wiškin(n)- [wfkytn!, wškn-] divide, separate. ~išn: separation. wiskofag [wskwpk' | N biškēfa] blossom. wiškuftan, wiSk6f- [vvškup-tn! | J guškuftn, gwškwß-] blossom; hatch. wišūb-, —išn(-īģ), v. wišuftan. wišoūmand [w%wmnd] poisonous, venomous. wišūdag [wiwtk' | (M ghwdg)] abortion, daevic creature. wišūdan [wswtn'] bear daevic offspring. wišuftan, wišūb- (zfwp-tn! | M wiwb-, N *gusuftan] disturb, destroy. ~isn: destruction. ~1&п16 : destructible. *wixSay- [whsd-} forgive, forbear. ~iSn(ih): forbearance. ~išnīg : forbearing. lwiyaban [20(у) р?п! | Р шуп, N bīābān] desert. *wiyābān [wyd’p’n'] astray, wandering; deluded. ~ih: delusion, deception. wiyaban|garih [wyd"Pnklyh] deception. ~ig [-vk'] wandering, itinerant. wiyāftan, *wiyüb- [wd ptn! | M wy’b-] open (the mouth). wiyan [wyd?n! | M wy’n, N giyān] tent. wiyiz- [wydwe-] loosen, undo. *wiyufs- [wdwps-] make merry. ~išn: merry-making. ~iìšnīg : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-ytn'] tremble, quake. -išn: quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption.
663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
876:astray wiyābān; lead ~ wiyābānēn- īdan.
1472:бео аа (of stray animals) apédag-
2671:lost wany; (stray) apédag.
3837:stray apēdag; v. astray.
4054:tray xwan.
4994:xwan-!
-- NYB
3297:rāyēnišn [l?dynšn'] the act of arranging, of managing, or of caring for: xrat har-2- axvānīk ~ Wisdom means caring for both forms of existence (the spiritual and the material) 66!?; kē vinds pat ~ ddrét he who considers Sin worth his care 83°; kar u ~ (hendiadys) mission, task, function 872; — directions 132%,
4315:x"àndan [KLYTN-tn', KRYTN-tn'] to call (by a name) 1227. 184. 110°. 1144. 11579. 117; to summon 16! (fräc xvānd):*!; to read 1822. 1104. — MPrs Paz. NP; cf Av. (1864) X"anat.caxra- ‘with roaring wheels’.
```


## [2026-10-17T00:31:24.007Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \".{150}(x[^ ]{0,3}aini|\"aini|\\^aini|xüp|xup|xüb|xub).{250}\" BRT.txt | head -12"
}
```


### [2026-10-17T00:31:24.300Z] TOOL RESULT

```
Exit code 1
(eval):1: parse error near `)'
```


## [2026-10-17T00:31:30.952Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '.{150}(aini- ?(Adj|adj)|xüp|xup |xüb|np\\. *x.an\\b|x.än).{250}' BRT.txt | head -12"
}
```


### [2026-10-17T00:31:31.561Z] TOOL RESULT

```
10832:)  Part  'die Macht  dazu  habend,  dazu  im  Stand  seiend, es  vermögend'  (näml.  das,  was  das  Verb. fin.  aussagt):  ia/tmJt  ..islim  az3m  baxiäni "ayamnö  "wem  soll  ich  , .  zutcileii,  ich der  ichs  vermag?"  Yt/o.  108;  108,  iio, 23,  37,  J4-47;  — yüzsm  dasta  xsayamna raisca  ..Y.öS.zi;  —  tat  nS  dlyata  yüt^m yazata  .  .  xsayamna  isäna  Y.05,14;  — yakmai  ustä  (sd.)  ..
11081:apajasat  .  .  aß  paurva 7'aMaKyai(sd.)  ..  aidaca (sd.)  ila  ..  sadayät V.2.22— 24;  —  hö  vTsp>m  ahüm  ..va?nai .  .  darfsta  ddiat  * amir^x^äntim  vispqm ..galiqm  Yt /p.94;  —  (Vnam  ..  sqm' .  . yazamaUe  yä  ni  baraitl  yäslä  tsi  gmi  . . tä  yasamaide  Y.  38. 1 ;  —  kyatca  mSt  tnraos ..at..\. 43.12;—  prssa^a  na  ..  Y.  43- 10;  —  avavaitya  ..ya^a  im  sk  astica  im xä  a
14328:%wa  haxsöit  gjul vakwa  Y.63. 10;  10,  Vyty,  22,  45,  Any. 2^;  —  afii  %wä  3l>ayai  avairiAeYt.  lo.jy, 78;  — _/rJ  äwam  xadaraAa paiti  uzuxiäne Yt/9.  50;  48;- —  a/a  .  ,,  dansäma  haiS, pairi  %wa  Jamyama,  kamtm  hwä  haxma (sd.)  Y.  60.  la;  —  aoxtSJtamana  %wä yasna  ..yassi  Yt  /o.  31 ;  56,  Y.p.  27;  — aurvantsm  %tffS  ..iayS  tatasatY. 10.10;  10; —  yaskgm  %wqm  paiHs
28825: die  Obersten  antreiben  .  ,?"  Y, S.  j-j—yaka  atim  käcayene  ..  zara^ttitrtm anumatie  (_sA.)  dainayäi  YLj,  18;  105, g.  »6.  zu  ß);  *hixsäne  nanm..  *hixsäne nairikam  .  .  *hixsäru  drt'aiqm  .  .  sqm  .  . nrp3rayan/a  (sd.)  "soll  ich  ,  .  antrei- ben, dass  sie  . .  sich  aneignen''  V.  79. 26.  d)  'Jemandem  zu  teil,  zu  eigen werden,  eignen':  kacaiti  dim  aspahe  aoj
30341:mi  Y.68. 14.  a)  m\Xgä%qm  ..  'tarn  framar^mnqm  Vi.  14.1. Gen. desEmptingcTs: 'ntlsYa  u/ia.dmils"a  Zum  V. 'mar-.  —  Pa.  {ta'Vr.  74):  pa  xüp vanta.i^nscaya,aianqm}i.4^  .)'gute'  {r^fr:™ ™b^^! {"Ll^ ^J  '^\^'^.t: Pflege  :  IBm  13  datAkävd  ntpaht  ya  'r»/Im  ]  i„^t^  und  vgl.  Au/ram^uaya^/a.  Die  Wahl yatayäti  (sd.)   mi^rahe    Vt./0.78.  LS.       des  /^«-Ahsolutivs  war  hie
```


## [2026-10-17T00:31:40.173Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '.{200}aini.?s[aä]x.{300}' BRT.txt | head -5; grep -n -o -E '.{100}Teppich, *(Ü|U)ber.{200}' BRT.txt | head"
}
```


### [2026-10-17T00:31:40.901Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:31:45.323Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'x[wv]?ān|xwan|xvan|hw.n' SNS_pages.txt | head; echo \"-- BQT v2\"; grep -n -E 'خوان' BQT_v2_pages.txt | head -20; echo \"-- ARY\"; grep -n -E '^ *خوان|قشنگ' incoming/ARY/ARY_pages.txt | head; grep -n -i -E 'QASHANG|KHAN\\b|XVAN' incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:31:45.877Z] TOOL RESULT

```
912:Tavadia, j.c. : "Sur Saxvan or a dinner                                        tal Society 1953.
11973:                                                      yHWWN, tn                          Wf**M                                                                    :             v*«o
15684:xOrdad/xurdad 76/12      xvan 59/21                          xvaried niglrln 71/6-2 78/9yasfe 312/8-315/12
15685:xOsag 67/21              xvanfind 214/20                     xVarsSd yast 71/3          yastaran 316/1
-- BQT v2
33:‫خوانند گان فاضل درخواست کرد که اطلاعات خودرا درموضوعهای مختلف کتاب تراسا‬
63: ‫کرده‌اند‪ .‬تقدیم میکند وازخوانند کان درخواست دارد که اطلاعات خود را دربار؛ مطالب‬
145: ‫‪( ۹‬شامل مقاله‌ای حاوی لفاتی‌ازلهجه‌های گلپایگانی وخوانماری» گرد آوردء محمدعلی‬
417:                                     ‫خوانند ‪.‬‬                               ‫صلق‌الماء خوانند ‪۰‬‬
422: ‫جاغسو لك ‪ -‬بروزن و معنی جاخوك‬                   ‫و بعربی بباسه خوانند ‪ - ۴‬کویند پوبت‬
437:   ‫( ‪ 10012۷‬هم خوانده شده)‪ ,‬ارمنی دخیل ‪ « 61018‬اسشق ‪ * ۰۱4‬در بسیاری از مواضع اوستا‬
498:                             ‫عمیق بگنرند؟‪.۱‬‬        ‫فخ و ثباك خوانند ‪-‬‬           ‫وعربی‬
584:   ‫‪ .۷-۸۷۲‬جاماسب درادییاتابران و عرب‌بلقب « فرزانه » وه حکیم» خوانده شده‪ .‬پیشگوییهایی‬
898:                                   ‫مثلثه خوانند ‪.‬‬   ‫و قوت لایموت حم‬            ‫زی‬
1074:                 ‫هت که عرب لیلخوانند ‪۱‬‬                    ‫هنج است »‬
1086:‫ومهمی‪ ۱‬و درعربی‌چوبهابی‌باشد که براستخوان‬                ‫جدبةرویش ‪ ۰‬کنابه از ابر‬
1197:                                                               ‫خوانند‪ .‬کزند کی‌زتبور را ثافم‌است ودر عربی‬
1251:                               ‫خوانند ‪.‬‬            ‫ایلکلب‬
1334:                                  ‫ب‬                    ‫که عرب آنرا حباری خوانند وبه هوبره مشهور‬
1374:    ‫و‪ (۵۱۱‬جاررا )» مولف«سنگ» را «نك؛ خوانده ومعنی کرده است‪ .‬امامعنی دوم‌آن درست است‬
1418:‫گونند بمعنی چاردانگ هر چیز است عنی نه‬                ‫استخوان لرمی است که در سر شانة گوسفند‬
1420:                                                                                                          ‫خوانند ‪.‬‬
1522:                          ‫باستخوان سوراخ گردد ‪.‬‬
1532:       ‫و بعضی کوبند معرب خرو دارو است *‬                                                 ‫‪.‬‬   ‫خوانند‬   ‫اد‬
1744:   ‫اسر نياید و به پنجم روز است از اسفند ماه ‪ .‬پارسیان بشتن رقعها کژدم را مگریدران خوانند‬
-- ARY
1930:خواننده» جلر واژه‌های مشکوکك (شاید) آورده است.
7303:خوان (به چم آخوردنی" و سینی یا طبق "مواد خوراکی") / ۲۴۹
8214:خوانگایس موی اش سس ۱880
2459:KAULAS LITHUANIAN) | ¢\ 3 ASTUXAN, ASTAXVAN
7153:(QUY(OLD ENGLISH) oS 5-JS3t XVAN, XWAN PAHLAVI] 5 344
7158:REFERENCES eBay XVAN, KHWAND
7170:XWANDAN, XVANTAN XVAN., XVANAT: —:(AVESTAN) ls!
7174:(OLD IRISH) 5 5-4) 2! XVANDIN, XVENDIN :(KURDISH) 52,5
7192:SOROR LATIN) 553 XVAHAR, XVANHAR-(AVESTAN) (glo 31
8987:LUCHI ROKHAN HAFGHAND) (5-4) Ji}
10215:ENNEPE GREER) gli SAXWAN, SOXVAN (PAHLAVI) 34
11969:KHAN., KHANATI KAN- AVESTAN) gle 3)
```


## [2026-10-17T00:31:50.009Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n \"pdf page 248\\]\" ARY_pages.txt; awk '/\\[pdf page 248\\]/{f=1} /\\[pdf page 249\\]/{f=0} f' ARY_pages.txt | head -60; sed -n 7145,7160p ARY_latin_index_pages.txt"
}
```


### [2026-10-17T00:31:50.411Z] TOOL RESULT

```
7301:[pdf page 248]
[pdf page 248]
۹ ۲
خوان (به چم آخوردنی" و سینی یا طبق "مواد خوراکی") / ۲۴۹
بادداشت: ۱
۱ بازگشت به: سیاه.
۲ چم این واژه در زبان لاتین: کلیف و چرکین.
۳ چم این واژه در زبان‌های ژرمنی: سیاه,
اوستایی (۸887400): پرتغالی (۳087001288): ۳88(81۸018)
2۷۸۷08۸۰ ,2۸810 گرنبک (ع007[71): نان
پهلری (۲7ائله): 7 70۷2 انگلیسی کهن (للولا8۸۷0 010)(شاید)
کردی (80154/). 8 وال72 ل ان
بلوچی (/8۸/0[7): ۷۸ لیترانی (/12اهمتا7/): ادور ان
افغانی (پشتر) (/۸70/۸):
0 ال2 70۷ پسگشت‌ها 5
ساسکریت (64(/98/7): ,5۷70۸78 ری 0 سا
1 5۵ 5۷313 2 (۸81010ن81) ای انیت
پونانی (08627): لا ۱2۳۱۱۱ ۱ :2 ۸4
لاتین (47100): 51۸20580 ,81۸050 6 (8آق۸ ,95 (020)
فرانسه (لل2ق۳): لد نگ اند دی 1 (ه2) دی آاو ۱
اسپانیایی (7ل3]/مم52). 3 ارا ان دی برهان قاطع + ۷۸۳
ایتالیایی (فل7): ۰ 88طظ۳88(51۸0) فرهنگ معین : ۱۳۴۹
بادداشت. َ
شا ۱ چم این واژه در زبان لاتین و دیگر زبان‌های رومانس: وادار کردن» قبولاندن» متقاعد کردن.
۲ واژ‌ی آخوانجه" باه" نیز از همین ریشه است.
اوستایی (4188740): ۰ -7۷۸3/۸1 ,10۷۸8۰ ۸ ,2۷/۸۷0۸
پهلوی (۳۸/]۸4/1): اوستی (08587/6): ,20072
YE 1 Shh ale” Gb st 3 la pe) Ole
; Jeetlsab
ake tg efit
SPI BS AN 385 3! eV
ther sty) Gldk; 39 0519 cal eT
(PER)SUADIR (PORTUGUESE) JW 4 AAVESTAN) gl)
SUTIS GOTHIC) S36 XWASTO, XWANDRA-

(QUY(OLD ENGLISH) oS 5-JS3t XVAN, XWAN PAHLAVI] 5 344
SWATAN XAN, XUNCHE (KURDISH) 635°
SODYTI (LITHUANIAN) gi p3 VAN ABALUCHI) gr sh

AAFGHAND (34) gil
REFERENCES eBay XVAN, KHWAND
POKORNY, = ~SO*S~*~*~*~*«wOSOL OO SVADATE, (SANSKRIT) 2 Sse
BARNHART: (SUASION) 1082 SVATTA., SVADA-, SVADAYATI
```


## [2026-10-17T00:31:54.614Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 239 240 241; do echo \"-- leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n -E 'خوان|xvan|xwan|xvân|۷۸۳|۷۸۲|۷۸۴' | head -12; done"
}
```


### [2026-10-17T00:31:55.078Z] TOOL RESULT

```
-- leaf 239
6:‫وقانون است ‪ -‬و طعامی را نیز کوبند که مقوی‬                         ‫باشد "‪ ۳‬وبعربی | واز کاو را خوانند ‪۰‬‬                              ‫خوردنی‬
-- leaf 240
-- leaf 241
1:‫خوان پابه‬                                                                                                      ‫یز پا‬
9:‫کوچك راخوانجه گویند ‪ -‬وخاروخلاشه وگیاه‬                           ‫خو‌الی‪ -‬باانی ممدوله بروزن عالی»‬
11:‫برهسماند ‪ - ۷‬وبمعنی چیزی خواندن وطلیسن‬                           ‫خانهٌآب را همگفته‌اند ‪ -‬و بمعنی مطبخی نیز‬
14:                                 ‫بعنی بخوان وبطلب ‪. ۷‬‬                                                  ‫‪۰‬‬       ‫ات‬   ‫درست‬
18:‫خوان پایه ‪ -‬با انی معدوله و بای‬                                   ‫خوالیگر ‪ - ۴‬بنانی ممدوله بروزن‬
41:                         ‫هوشمان مردود مداند « هوبشمان ‪. ۸‬معرب آن خوان (ضم اول) «نفس»‬
44:                ‫و خار خوانا ‪۰‬‬       ‫مك‬    ‫خار‬       ‫مانندة‬         ‫سنداخت‬    ‫خوار‬   ‫از بمح نکند او ورا‬
48:  ‫الف خوانا دربن بيت » الف اطلاق است وخوان جمم خو (علف حرزه) (ه‪.‬م‪ ).‬است که‬
49: ‫‪.‬‬     ‫خواندن‬   ‫‪:‬‬   ‫رك‬   ‫‪-‬‬   ‫‪۷‬‬           ‫اسدی خود درص ‪ ۷۱۶‬متذ کر شده ) از افادات استاد دد«شدا) ‪.‬‬
```


## [2026-10-17T00:31:57.253Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==242' BQT_v2_pages.txt | sed -n 1,50p"
}
```


### [2026-10-17T00:31:57.598Z] TOOL RESULT

```
‫خوان پابه‬                                                                                                      ‫یز پا‬
                                                      ‫خوالگر ‪ - ۱ )۱‬باانی معدوله بر باشد ‪.‬‬
‫حوان ه با نانی ممدوله بر وزن نان »‬                               ‫وزن شالگر (‪ .)۷‬مطبخی و طباخ و طعام پز را‬
‫کنابه ازخوردنی وماده باشد ‪ ۵‬و‪-‬طبق بزرگی‬                          ‫گویند ‪ - ۴‬و بمعنی سفره چی هم بنظر آمده‬
                                                                                                                    ‫است‬
          ‫را یز گوبند که از چوب ساخته باش‬
     ‫طندبچه‬
     ‫ق‬
‫کوچك راخوانجه گویند ‪ -‬وخاروخلاشه وگیاه‬                           ‫خو‌الی‪ -‬باانی ممدوله بروزن عالی»‬
‫خودرو را نگیفزته اند که از ميان زراعت قوت‬                         ‫وزبند ‪ - ۴‬ورود‬‫زیبا ومهنا باشد ‪ -‬وطعام رگای‬
‫برهسماند ‪ - ۷‬وبمعنی چیزی خواندن وطلیسن‬                           ‫خانهٌآب را همگفته‌اند ‪ -‬و بمعنی مطبخی نیز‬
‫هم هت ‪ - ۷‬و امرباین دومعنی آیمزده است‬                            ‫؛بکراول بروزن نهالی هم‬
                                                                                      ‫بنظرآمده است ‪ ۴‬و‬
                                 ‫بعنی بخوان وبطلب ‪. ۷‬‬                                                  ‫‪۰‬‬       ‫ات‬   ‫درست‬



‫خوان پایه ‪ -‬با انی معدوله و بای‬                                   ‫خوالیگر ‪ - ۴‬بنانی ممدوله بروزن‬
‫فارسی بالف کشیده وفتح نحتانی‪ .‬دستار خوالرا‬                        ‫بازیگرطباخ‌ومطبخی‌وخوالالار وسفره چی‌باشد؛‬
                                                ‫‪.‬‬     ‫فمف‬
                                                                   ‫و بکر اول نیزگفته اندکه بر ونزانلیگر‬
                                                       ‫‪:‬الك‪.‬‬
                                                           ‫(‪ )۲‬خم ش‬                 ‫(‪ )۱‬خ‪٠‬‏ ‪ :‬خوالك ‪.‬‬

        ‫‪۰‬ص‪.‬‬
          ‫‪۲ :۹!۱‬‬
               ‫‪ - ۱‬از ‪ :‬خوال (= خوار) ‪ +‬کر ( یوند فاعلی وشفلی ) رکه‪ :‬اسفا‬
                                         ‫‪ -‬ابن آفروشه‌است‪ ,‬دوزاغ است خوالگرش‬
                ‫هر دو قرین بکدیگر وليك در خورند‪.‬‬
     ‫‪ ۶‬ناصرخسرر بلخی ‪.*۸۱۱‬‬
‫‪-‬اوزا‪:‬لی ‪ -۳‬کر( پوند فاعلی‬
                         ‫خ‬                                   ‫‪.‬ك‪ :‬اسفا!‪۲ :‬ص ‪. ۰۹۱‬‬
                                                                               ‫‪ = ۴‬خوال ر‬
                                                ‫‪0‬‬                                              ‫وشفل) = خوالگر‬
            ‫بدیبا وخوالیگران خواستند ‪.‬‬                                  ‫یکی خانه او را بباراستند‬
     ‫فردوسی طوسی‪ *.‬لغت فرس> ‪۳۱۰‬‬
     ‫» کردی ع ‪nãx‬‏ »افغانی ‪naVX‬‏‬                ‫‪ 9‬تاوادیا ‪۹۱۷‬‬       ‫س‬    ‫(طبق‬       ‫بهلوی ‪nãvx‬‏‬   ‫حه‬       ‫‪۵‬‬

     ‫اشتفافی که حهرن‌در موضع فوق برای کلمه آ ورده‪,‬‬           ‫وجه‬    ‫(سینی» بثقاب) «اسشق ‪A4‬‏‬            ‫بلوچی ‪02۷‬‬

                         ‫هوشمان مردود مداند « هوبشمان ‪. ۸‬معرب آن خوان (ضم اول) «نفس»‬
 ‫کرده ‪:‬‬              ‫کک‬                    ‫کاکک‬              ‫ا‬      ‫ا‬    ‫ی‬           ‫ا‬    ‫کا‬      ‫‪ ۹‬ا‬

                ‫و خار خوانا ‪۰‬‬       ‫مك‬    ‫خار‬       ‫مانندة‬         ‫سنداخت‬    ‫خوار‬   ‫از بمح نکند او ورا‬


     ‫«لفت فرس ‪.»۹۸۳‬‬
  ‫الف خوانا دربن بيت » الف اطلاق است وخوان جمم خو (علف حرزه) (ه‪.‬م‪ ).‬است که‬
 ‫‪.‬‬     ‫خواندن‬   ‫‪:‬‬   ‫رك‬   ‫‪-‬‬   ‫‪۷‬‬           ‫اسدی خود درص ‪ ۷۱۶‬متذ کر شده ) از افادات استاد دد«شدا) ‪.‬‬
```


## [2026-10-17T00:32:07.517Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for f in HRN.txt HUB.txt LKT.txt TTS.txt PHD.txt NYB_vol2_glossary.txt; do echo \"-- $f\"; grep -n -i -E 'ka[sš]ang|qa[sš]ang|ga[sš]ang|kaschang|qaschang' $f 2>/dev/null | head -5; done; command ls incoming/ | head -40; grep -n -E 'قشنگ' incoming/BQT/BQT_v3_pages.txt | head"
}
```


### [2026-10-17T00:32:07.903Z] TOOL RESULT

```
-- HRN.txt
-- HUB.txt
-- LKT.txt
-- TTS.txt
-- PHD.txt
-- NYB_vol2_glossary.txt
ARY
BLY
BQT
FFD
IRN
MFL
MON
PLA
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
```


## [2026-10-17T00:32:11.255Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; command ls incoming/TTS incoming/MON; grep -n -i -E 'ka[sš]ang|qa[sš]ang|ga[sš]ang|kaschang|qaschang|kašaŋ' incoming/TTS/* 2>/dev/null| head; grep -c '' incoming/BQT/BQT_v3_pages.txt; grep -n 'قشن' incoming/BQT/BQT_v3_pages.txt | head"
}
```


### [2026-10-17T00:32:11.580Z] TOOL RESULT

```
incoming/MON:
MON_2vol_Adena_v1_archive.pdf
MON_2vol_Adena_v1_djvu.txt
MON_2vol_Adena_v2_archive.pdf
MON_2vol_Adena_v2_djvu.txt

incoming/TTS:
TTS_pages.txt
TTS_vambery1878_uoft_djvu.txt
TTS_vambery1878_uoft.pdf
51425
3989:- ودر عربی‌بمعنی‌بلقشنه (۱) است. وآن‌ریسمالی
```


## [2026-10-17T00:32:14.622Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'قشنك|قشنگ|غشنگ' incoming/BQT/BQT_v3_pages.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt MON_part2.txt MON_part1.txt | head"
}
```


### [2026-10-17T00:32:15.107Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v2_djvu.txt:43101:والده. (ص.) (ف.) هر چیز خوب؛ قشنگك؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:43110:خوب و قشنگ و دوست داشتتی. . شسحص 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:43959:مستناس و قشنگی است و بسالة شنای 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:53608:که برای قشنگی و زیبایش آن را نگهداری 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:54351:قشنگ (به به مزاح و تمسحر.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:84470:نودن. زیباً بودن» قشنگ بودن. (اسص.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:93726:قشنگی برمی‌انگیزد» بخارهای ید بنفش 
MON_part2.txt:43101:والده. (ص.) (ف.) هر چیز خوب؛ قشنگك؛ 
MON_part2.txt:43110:خوب و قشنگ و دوست داشتتی. . شسحص 
MON_part2.txt:43959:مستناس و قشنگی است و بسالة شنای
```


## [2026-10-17T00:32:18.515Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/قشنگ",
 "prompt": "Quote verbatim the Mo'in (معین) entry for قشنگ including any origin tag in brackets like [تر.] or [سغ.], and the Dehkhoda entry etymology if present."
}
```


## [2026-10-17T00:32:19.556Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/خوان",
 "prompt": "Quote verbatim the Mo'in (معین) entries for خوان (xān/xvān, meaning tablecloth/food tray), including any origin tag in brackets like [په.]."
}
```


### [2026-10-17T00:32:22.008Z] TOOL RESULT

```
# Mo'in Dictionary Entry for قشنگ

According to the content provided, the Mo'in (معین) dictionary entry states:

"(قَ شَ) (ص .) ظریف ، خوشگل ، زیبا"

This entry defines the word as meaning refined, beautiful, or pretty, without including an origin tag in brackets. The page indicates that additional etymological information may be available through the Dehkhoda dictionary link, but that specific entry is not included in the provided content.
```


### [2026-10-17T00:32:22.912Z] TOOL RESULT

```
# Mo'in Dictionary Entry for خوان

Based on the webpage content provided, the Mo'in (معین) dictionary entry for **خوان** states:

"( ~.) (اِ.) 1 - خار و خلاشه . 2 - گیاه خودرو، علف هرزه"

This entry indicates two definitions: thorns/thistles, and a self-growing plant or weed. The notation "(~.)" and "(اِ.)" appear to be grammatical or origin markers used in the dictionary.
```


## [2026-10-17T00:32:25.641Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=خوان&d=moein",
 "prompt": "Quote verbatim every Mo'in (معین) entry for the headword خوان, especially the one meaning سفره / طبق / خوانچه, including any origin tag in brackets like [په.]."
}
```


### [2026-10-17T00:32:29.454Z] TOOL RESULT

```
# Mo'in Dictionary Entries for خوان

Based on the page content, here are the relevant Mo'in entries:

**Entry 1 (Botanical meaning):**
"خار و خلاشه . گیاه خودرو، علف هرزه"

**Entry 2 (Verbal root):**
"ریشة «خواندن ». در ترکیب به معنی «خواننده » آید"

**Entry 3 (Dining/household item):** [په.]
"سفره . طبق بزرگ چوبین . خوردنی"

The third entry is the most relevant to your interest, indicating that خوان refers to a tablecloth, a large wooden platter, or food items, with Persian etymology markers.
```


## [2026-10-17T00:32:31.145Z] AGENT

Now archive web sources and check the printed page.


## [2026-10-17T00:32:35.330Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/قشنگ' --note 'page 560, root `Xšnk, qašang etymology (from Sogdian ʾγšnk-)'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خوان' --note 'page 560, root Xvaini, xwān etymology (MP xwān, cognate Av. xvaini)'; python3 tools/fetch_source.py 'https://vajehyab.com/moein/قشنگ' --note 'page 560, Mo in entry qašang (no origin tag)'; python3 tools/fetch_source.py 'https://vajehyab.com/?q=خوان&d=moein' --note 'page 560, Mo in entry xvân [په.] sofre, tabaq'; pdftoppm -f 560 -l 560 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg560"
}
```


## [2026-10-17T00:32:35.925Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg560.png"
}
```


### [2026-10-17T00:32:37.691Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/51c25e5efb0012de.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/802bfae11dbfa661.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b02d073cc6759d72.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/83978f2167e33674.txt
```


### [2026-10-17T00:32:37.715Z] TOOL RESULT

```

```


## [2026-10-17T00:32:54.643Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '.{0,120}[x%][^ ]{0,2}aini.{0,200}' BRT.txt | grep -i -E 'sch[öo]n|xüp|xup|xvaini|decke' | head -5; grep -n -o -E '.{0,200}(sch[öo]n|Teppich).{0,60}x.?aini.{0,100}' BRT.txt | head -3"
}
```


### [2026-10-17T00:33:01.108Z] TOOL RESULT

```
ugrep: error: error at position 392
\xbf]){0,2}aini(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                       exceeds complexity limits___/


ugrep: error: error at position 178
i(?:[^\n\x80-\xbf][\x80-\xbf]*){0,100}
         exceeds complexity limits___/
```


## [2026-10-17T00:33:05.076Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='ignore').read()\nfor m in re.finditer(r'aini',t):\n    s=t[max(0,m.start()-150):m.end()+250]\n    if re.search(r'sch[öo]n|x[üu]p|Decke|Teppich',s): print(m.start(),repr(s));print()\nE"
}
```


### [2026-10-17T00:33:05.464Z] TOOL RESULT

```
2294026 'icht  verfallen  ist,  tockündig\':  ys mqm  .  .  därayehi  ya^a  tayam  -nm  nava (sd.)  akmi  \'rS  Y,  /;.  3;  —  väcö  ysi  p^simHt sär?m  "  bunjainii  ". .  die  selbst  den  noch retten,  des  Haupt  schon  dem  Gericht  ver- fallen isr  Yt./4.46.\nVgl.  tfa!ö.laHH\'.  —  Tä.:  fiirlak  sar.  —  \')  Mit Trennung  der  Glieder,   vgl.  lu  «aitySjaaia: \\.  ffhila  F.  /j;  \\\\ts /sula.\n•  j.  paäu.'

3311395 's)  \'etwas  (Akk.)  wahrnehmen\' : frS  mHi  fravBisdüm  (j-Aor.)  ar3%3  (sd.) ta  ya  ..  Y.33-  8;  —  arydvim  .  .ya  hiHaite Jravaih^mna  .  .  kaininö  kihrpa  srtrayä ".  .  die  immer  wahrzunehmen  ist  in  der Gestalt  eines  schönen  Mädchens"  Yt 5..i6.\nmit  «r  Kaus.  1 ) \'Jemandem  (wo  ?■  Ad  V.  statt Lok.)  etwas  zu  wissen  tun\' :  andvim .  .yakmya ahurS  .  .  nivaBiayat  Yt.5. 8'

4440329 '  —  Aux/a^rSJtmiti (sd.) . .  xsa\'irfm  . .  Mmahicä  *AvanmaAicä  \'* Y.  J5-  5-\nmit  apa  \'ablenken\':  yöi ..  tagiriptfmHi snahfm  apasa  apaj^anvainii  "dit.. seihst den  Schlag,  zu  dem  schon  ausgeholt  ist, rückwärts  ablenken"  Vt.  i4-  46-\nai.  suviü,  süläh,  —  Vgl.  a^ai-.  —  Pü. :  kartaii, (zu  Y.  3S  erl.):  liiriin  afe  tarlaiti  Sü.  (lu Y.  s&-  d^""«.  (lu  V.  35)1  karlum; '
```


## [2026-10-17T00:34:24.732Z] TOOL CALL #31: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg560.png /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/560.png; cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-560.py <<'EOF'\nimport json\nWK_Q=\"https://en.wiktionary.org/wiki/قشنگ\"\nWK_X=\"https://en.wiktionary.org/wiki/خوان\"\nVJ_Q=\"https://vajehyab.com/moein/قشنگ\"\nVJ_X=\"https://vajehyab.com/?q=خوان&d=moein\"\nSOD_REF={\"ref\":\"SOD:28\",\"status\":\"supports\",\"note\":\"SOD_pages.txt leaf 93 (printed p. 28/29), entry 731: \\\"'Xšnk- B, S (o)xšank/-g <*gašnak(k)a- ... beautiful, splendid\\\"; also entry 732 'xšnkWk 'splendour, beauty', 734 'xšnkystr 'more beautiful'. Gharib's Persian equivalent column (OCR garbled) is where Nourai's qašang link comes from. The Manichaean form is entry 2089 'xšnk- M ox(a)sang 'beautiful, splendid'.\"}\nHUB_C={\"src\":\"HUB\",\"where\":\"p. 57, no. 498 (HUB.txt line 1958)\",\"stance\":\"contradicts\",\"note\":\"'498. Zd. xᵛaini- wird von der Phl. Übersetzung durch xūp \\\"schön\\\" wiedergegeben, das vollkommen passt. Die Zusammenstellung ist also falsch.' Hübschmann rejects Horn's link of xᵛān with Av. xᵛaini- (this is the dissent recorded in Nourai's NOTE).\"}\nHRN_R={\"ref\":\"HRN:110\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 131 (= p. 110), no. 498: 'xᵛān \\\"Tischdecke; Tisch (gedeckter)\\\". aw. xᵛaini- \\\"Teppich, Überzug, Decke\\\", kurd. LW xan; afgh. xᵛān; bel. n. vān \\\"Platte, Teller\\\" (289). Geldner, Studien I, 17/8.' Exactly Nourai's chart (root gloss and Pahlavi/Persian word).\"}\nPHD_C={\"src\":\"PHD\",\"where\":\"p. 95 (PHD.txt line 663)\",\"stance\":\"partial\",\"note\":\"'xwān [hwʾn | M xwʾn, N ~] tray, table.' Confirms the Pahlavi word, Manichaean MP xwʾn and NP xwān; no etymology given.\"}\nNYB_C={\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt grep 'xvān|xʷān'\",\"stance\":\"silent\",\"note\":\"only xᵛāndan 'to call, read' (p. ~218) found; no entry for xvān 'table'.\"}\nBQT_R={\"ref\":\"BQT:783\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 241 (printed ≈ 783-784), headword 'خوان - با واو معدوله بر وزن نان، کنایه از خوردنی و مائده باشد و طبق بزرگی را نیز گویند که از چوب ساخته باشند و طبق کوچک را خوانچه گویند'; Mo'in's footnote: 'پهلوی xvān (طبق، سینی، بشقاب) «اسشق ۴۹۸»، کردی xān، افغانی xvān، بلوچی vān ... وجه اشتقاقی که هرن در موضع فوق برای کلمه آورده هوبشمان مردود می‌داند «هوبشمان ۵۸»'. Supports the Pahlavi→Persian step and itself reports Hübschmann's rejection of the Avestan link.\"}\nd={\"pdf_page\":560,\"book_page\":530,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n{\"entry\":0,\"root\":\"`Xšnk\",\"verdict\":\"confirmed\",\n\"modern_form\":\"Sogdian ʾxšnk / ʾγšnk- (əxšank) 'beautiful, splendid', < *gašnaka-, related to Proto-Iranian *gr̥š- 'rejoice'\",\n\"note\":\"The root box is the Sogdian word itself, not a reconstruction: Gharib (SOD entry 731, Buddhist and Sogdian-script; entry 2089, Manichaean) gives 'xšnk (o)xšank 'beautiful, splendid', which Nourai glosses 'nice'. Wiktionary writes it ʾγšnk- and derives Persian qašang from it, adding Northern Luri xşəŋ and a link to Proto-Iranian *gr̥š- 'rejoice'. The chart's direction is slightly odd: gašnaka, which is Gharib's reconstructed ancestor *gašnak(k)a-, is drawn as a child of ʾxšnk. The extraction matches the printed page.\",\n\"note_fa\":\"ریشهٔ این نمودار خودِ واژهٔ سغدی ʾxšnk (خوانده‌شده əxšank) به معنی «زیبا، باشکوه» است که قریب در فرهنگ سغدی (مدخل ۷۳۱ و ۲۰۸۹) آورده و نورایی آن را «nice» معنی کرده است. ویکی‌واژه هم «قشنگ» فارسی را از همین واژهٔ سغدی می‌داند و آن را با ریشهٔ ایرانی آغازین *gr̥š- «شاد شدن» مربوط می‌کند. پس ریشه و معنی آن درست است. تنها نکته این است که gašnaka، صورتِ بازسازی‌شدهٔ کهن‌تر نزد قریب، در نمودار فرزندِ ʾxšnk کشیده شده، در حالی که نیای آن است.\",\n\"sources\":[WK_Q],\n\"ref_check\":[SOD_REF],\n\"consulted\":[{\"src\":\"HRN\",\"where\":\"HRN.txt grep 'kašang|qašang|kaschang'\",\"stance\":\"silent\",\"note\":\"Horn has no entry for qašang.\"},{\"src\":\"HUB\",\"where\":\"HUB.txt grep 'kašang|qašang'\",\"stance\":\"silent\",\"note\":\"no hit.\"}],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Sogdian\",\"words\":\"gašnaka\",\"verdict\":\"plausible\",\n\"derivation\":\"gašnaka is not an attested Sogdian word. It is Gharib's reconstruction *gašnak(k)a-, which SOD gives in the etymology slot of entry 731 ('(o)xšank/-g <*gašnak(k)a-'). It is the presumed ancestor of attested ʾxšnk: initial *g- became the spirant γ/x, a prothetic ə-/o- was added before the cluster, and the final -aka- was reduced to -k. Wiktionary's link of ʾγšnk- to Proto-Iranian *gr̥š- 'rejoice' fits a stem *gr̥š-na-ka- > *gašnaka-. Labelling the form 'Sogdian' and drawing it as a child of ʾxšnk reverses the actual relation (it is pre-Sogdian), so the node is plausible rather than confirmed.\",\n\"derivation_fa\":\"gašnaka واژه‌ای گواهی‌شده در متون سغدی نیست. این صورتِ بازسازی‌شدهٔ *gašnak(k)a- است که قریب در بخش ریشه‌شناسی مدخل ۷۳۱ آورده و نیای سغدی ʾxšnk (əxšank) به شمار می‌آید. در این تحول g آغازین سایشی (γ/x) شده، پیش از خوشهٔ همخوان واکهٔ ə-/o- افزوده شده و پسوند -aka- به -k کوتاه شده است. ویکی‌واژه آن را با ریشهٔ ایرانی آغازین *gr̥š- «شادمان بودن» می‌سنجد که با *gašnaka- سازگار است. پس صورت پذیرفتنی است، ولی «سغدی» خواندن آن و نشاندنش در جای فرزندِ ʾxšnk دقیق نیست، چون این صورت پیشاسغدی و نیای آن است.\",\n\"sources\":[WK_Q],\n\"ref_check\":[SOD_REF],\n\"consulted\":[{\"src\":\"SOD\",\"where\":\"SOD_pages.txt entry 2089 (leaf 148)\",\"stance\":\"supports\",\"note\":\"\\\"2089 'xšnk- M ox(a)sang (xšnk) pl. -t =»'Ysnk- beautiful, splendid; GMS 157, 511, 981, 1204\\\": the attested Manichaean form, without the reconstruction.\"},{\"src\":\"ISS_alt_DKS\",\"where\":\"not searched in depth (Khotanese dictionary)\",\"stance\":\"silent\",\"note\":\"Bailey's Khotanese dictionary has no bearing on this Sogdian form; no hit for 'gašnak'.\"}]},\n{\"id\":2,\"lang\":\"Persian\",\"words\":\"qašang\",\"verdict\":\"confirmed\",\n\"derivation\":\"NP qašang قشنگ 'pretty, beautiful' is a loan from Sogdian ʾγšnk-/ʾxšnk (əxšank) 'beautiful'. The Sogdian voiced velar spirant γ was taken over as Persian γ, written ق/غ (the two merged as /ɣ~ɢ/ in Persian). The prothetic vowel was dropped, and an epenthetic -a- broke up the šn cluster (xšank → qašang), with final -k voiced to -g after the nasal (-nk > -ng). Wiktionary gives exactly this etymology and adds the Northern Luri cognate xşəŋ. Urdu qašang is borrowed from Persian. Mo'in (online) defines it as 'ظریف، خوشگل، زیبا' with no origin tag. Bahār's line quoted in the chart is modern (20th c.), which fits the word's late appearance in literary Persian.\",\n\"derivation_fa\":\"«قشنگ» به معنی زیبا و ظریف وام‌واژه‌ای از سغدی ʾγšnk / ʾxšnk (əxšank) «زیبا، باشکوه» است. همخوان سایشی γ سغدی در فارسی با «ق/غ» نوشته شده (این دو در تلفظ فارسی یکی شده‌اند). واکهٔ آغازین افتاده، میان ش و ن واکهٔ a افزوده شده و k پایانی پس از نون به g بدل شده است (-nk > -ng). ویکی‌واژه همین ریشه را می‌دهد و هم‌ریشهٔ لری شمالی xşəŋ را نیز می‌آورد. فرهنگ معین برچسب ریشه‌ای برای آن ندارد. ادعای نورایی درست است.\",\n\"sources\":[WK_Q,VJ_Q],\n\"ref_check\":[SOD_REF,{\"ref\":\"MON\",\"status\":\"partial\",\"note\":\"vajehyab Mo'in: 'قشنگ (قَ شَ) (ص.) ظریف، خوشگل، زیبا' confirms the word and meaning but gives no etymology (no page number in Nourai's citation).\"}],\n\"consulted\":[{\"src\":\"HRN\",\"where\":\"HRN.txt grep 'kašang|qašang|kaschang'\",\"stance\":\"silent\",\"note\":\"no entry.\"},{\"src\":\"HUB\",\"where\":\"HUB.txt grep 'kašang|qašang'\",\"stance\":\"silent\",\"note\":\"no entry.\"},{\"src\":\"BQT\",\"where\":\"BQT_v3_pages.txt grep 'قشنگ|قشنك'\",\"stance\":\"silent\",\"note\":\"headword not found in the OCR of vol. 3 (ق section), possibly an OCR gap; the word is not among Borhan's classical lemmata as far as the OCR shows.\"},{\"src\":\"MON\",\"where\":\"vajehyab Mo'in قشنگ\",\"stance\":\"partial\",\"note\":\"'ظریف، خوشگل، زیبا', no origin tag.\"},{\"src\":\"ARY\",\"where\":\"ARY_pages.txt / latin index grep 'قشنگ|QASHANG'\",\"stance\":\"silent\",\"note\":\"no entry (Aryanpur covers only IE-rooted words with European cognates).\"},{\"src\":\"LKT\",\"where\":\"LKT.txt grep 'kašang|qašang'\",\"stance\":\"silent\",\"note\":\"no Turkic-origin claim recorded.\"}]}]},\n{\"entry\":1,\"root\":\"Xvaini\",\"verdict\":\"plausible\",\n\"modern_form\":\"Av. xᵛaini- (meaning disputed: 'cover, carpet' per Geldner/Horn vs. 'beautiful' per the Pahlavi translation xūb, Hübschmann)\",\n\"note\":\"Nourai follows Horn no. 498 (p. 110), who follows Geldner: NP xᵛān 'covered table, tablecloth' < aw. xᵛaini- 'Teppich, Überzug, Decke'. Hübschmann (Pers. Stud. p. 57, no. 498) rejects the link because the Pahlavi translation renders xᵛaini- with xūp 'beautiful', which suits the context perfectly. Mo'in's BQT footnote repeats this rejection, and Nourai's own NOTE records it. MacKenzie gives Pahlavi xwān 'tray, table' (Manichaean xwʾn) with no etymology. Wiktionary lists Av. xᵛaini 'cover, carpet' as a cognate, but its only cited source for that is Nourai p. 530, so it is not independent support. Aryanpur (p. 249) instead puts خوان under PIE *swād- 'sweet'. The Avestan word exists, but both its gloss and the link are uncertain, so the root is only plausible. The extraction matches the printed page.\",\n\"note_fa\":\"نورایی به پیروی از هرن (شمارهٔ ۴۹۸، ص ۱۱۰) و گلدنر، «خوان» را با اوستایی xᵛaini- به معنی «فرش، روکش، پوشش» می‌سنجد. هوبشمان (پژوهش‌های فارسی، ص ۵۷) این پیوند را نادرست می‌داند، چون گزارش پهلوی اوستا این واژه را xūb «خوب، زیبا» ترجمه کرده است. معین هم در حاشیهٔ برهان قاطع همین ردّ هوبشمان را آورده، و یادداشت خودِ نورایی نیز به آن اشاره دارد. مکنزی xwān پهلوی را «سینی، میز» معنی کرده ولی ریشه‌ای برایش نیاورده است. ویکی‌واژه برای این هم‌ریشه تنها به خودِ نورایی استناد می‌کند، و آریان‌پور خوان را زیر ریشهٔ *swād- «شیرین» آورده است. پس واژهٔ اوستایی وجود دارد، اما معنای آن و پیوندش با «خوان» قطعی نیست و ادعای نورایی را باید با احتیاط پذیرفت.\",\n\"sources\":[WK_X],\n\"ref_check\":[{\"ref\":\"SNS:59\",\"status\":\"partial\",\"note\":\"SNS_pages.txt index line 15684: 'xvan 59/21': the Shayast ne Shayast glossary has Pahlavi xvān at p. 59, line 21. That attests the Pahlavi word, but no Avestan xᵛaini- link could be read in the OCR.\"},HRN_R],\n\"consulted\":[HUB_C,{\"src\":\"BRT\",\"where\":\"BRT.txt python scan for 'aini' near 'schön|xūp|Decke|Teppich'\",\"stance\":\"silent\",\"note\":\"the OCR of Bartholomae's xᵛ- section is too corrupt to locate the xᵛaini- article; no usable hit.\"},{\"src\":\"ARY\",\"where\":\"pdf page 248 (printed 249), headword 'خوان (به چم خوردنی و سینی یا طبق مواد خوراکی)'\",\"stance\":\"contradicts\",\"note\":\"Aryanpur files خوان under the *swād- 'sweet, persuade' group (Av. xᵛāsta-, Pahl. xvān, Kurd. xān, xunche, Afgh. xvān; Skt. svādate; Lat. suadere; refs BQT 783, Mo'in 1349): a different root from xᵛaini-.\"}],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"xvân\",\"verdict\":\"plausible\",\n\"derivation\":\"Pahlavi xwān [hwʾn] 'tray, table' (MacKenzie p. 95), Manichaean MP xwʾn, is well attested. It was borrowed early into Old Armenian as xan (later xōn, xon), and has dialect cognates Kurdish xān, Pashto xᵛān and Baluchi vān 'plate'. Horn derives it from Av. xᵛaini- 'carpet, cover', with a semantic path 'spread cloth' → 'tablecloth' → 'table laid with food'. Hübschmann rejected this because the Pahlavi translation glosses xᵛaini- as xūb 'beautiful'. The word is certain, but its descent from xᵛaini- is a minority, unverified view, as the chart's own NOTE says. Modern sources (MacKenzie, Wiktionary apart from its Nourai citation) leave the etymology open, so the edge is plausible.\",\n\"derivation_fa\":\"واژهٔ پهلوی xwān [hwʾn] به معنی «سینی، میز خوراک» (مکنزی، ص ۹۵) و مانوی xwʾn گواهی‌شده و بی‌گمان است. این واژه به ارمنی کهن (xan) وام داده شده و در کردی xān، پشتو xvān و بلوچی vān «بشقاب» نیز دیده می‌شود. هرن آن را از اوستایی xᵛaini- «فرش، روکش» می‌داند، با تحول معنایی «گستردنی» به «سفره» و سپس «میز گستردهٔ خوراک». هوبشمان این پیوند را رد می‌کند، چون گزارش پهلوی xᵛaini- را xūb «زیبا» معنی کرده است. پس واژه درست است، ولی ریشه‌اش قطعی نیست، همان‌گونه که یادداشت خودِ نورایی هم می‌گوید.\",\n\"sources\":[WK_X],\n\"ref_check\":[HRN_R,{\"ref\":\"AEF:640\",\"status\":\"not_checked\",\"note\":\"Khaleqi Motlaq's Persian translation of Horn+Hübschmann is not on disk or online (catalog entry only). It would reproduce Horn 498 together with Hübschmann's rejection.\"}],\n\"consulted\":[PHD_C,NYB_C,HUB_C]},\n{\"id\":2,\"lang\":\"Persian\",\"words\":\"xân\",\"verdict\":\"confirmed\",\n\"derivation\":\"NP xᵛān / xān خوان 'food tray, laid table, tablecloth' continues MP xwān directly. The spelling keeps the old xw-, whose w (the 'vāv-e maʿdūle') was later lost in pronunciation, so xwān > xān. Borhan defines it as 'کنایه از خوردنی و مائده ... و طبق بزرگی که از چوب ساخته باشند'. The diminutive xᵛānče 'small tray' (the chart's خوانچه) is formed with the suffix -če. Saʿdī's verse in the chart ('چه دشمن بر این خوان یغما، چه دوست') shows the classical sense 'spread of food'. Mo'in tags it [په.] (Pahlavi), and Arabic borrowed it as xiwān.\",\n\"derivation_fa\":\"«خوان» (با واو معدوله، خوانده‌شده xān) به معنی سفره، طبق بزرگ چوبین و خوراک گسترده، دنبالهٔ مستقیم واژهٔ فارسی میانهٔ xwān است. واو پس از خ در نوشتار مانده، ولی در تلفظ فارسی نو افتاده است. «خوانچه» نیز با پسوند کوچک‌ساز «-چه» از آن ساخته شده. برهان قاطع و معین (با برچسب [په.]) همین را تأیید می‌کنند، و عربی آن را به صورت «خِوان» وام گرفته است. این گام از پهلوی به فارسی بی‌گمان درست است.\",\n\"sources\":[WK_X,VJ_X],\n\"ref_check\":[BQT_R],\n\"consulted\":[{\"src\":\"MON\",\"where\":\"vajehyab Mo'in خوان (entry 3)\",\"stance\":\"supports\",\"note\":\"'[په.] سفره. طبق بزرگ چوبین. خوردنی' (Pahlavi origin tag).\"},{\"src\":\"HRN\",\"where\":\"p. 110 no. 498\",\"stance\":\"supports\",\"note\":\"'xᵛān \\\"Tischdecke; Tisch (gedeckter)\\\"', with Kurdish and Afghan cognates.\"},{\"src\":\"HUB\",\"where\":\"p. 57 no. 498\",\"stance\":\"partial\",\"note\":\"accepts the Persian word, rejects only the Avestan comparison.\"},{\"src\":\"ARY\",\"where\":\"printed p. 249\",\"stance\":\"partial\",\"note\":\"'خوان (به چم خوردنی و سینی یا طبق مواد خوراکی)'; Pahl. xvān, Kurd. xān, xunche; cites BQT 783 and Mo'in 1349. It agrees on the Pahlavi→Persian step but gives a different deeper root (*swād-).\"}]}]}]}\njson.dump(d,open('/home/sfmqrb/git/rishe-private/data/verification/page-560.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-560.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-560.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 560"
}
```


### [2026-10-17T00:34:25.280Z] TOOL RESULT

```
nodes verified: 4/4
node verdicts: {'plausible': 2, 'confirmed': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 4, 'partial': 1, 'not_checked': 1}
books consulted: {'supports': 3, 'silent': 7, 'partial': 4, 'contradicts': 1} | by book: {'HUB': 3, 'HRN': 2, 'MON': 2, 'ARY': 2, 'SOD': 1, 'ISS_alt_DKS': 1, 'BQT': 1, 'LKT': 1, 'PHD': 1, 'NYB': 1}
```


## [2026-10-17T00:34:30.806Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c -i -E 'ga[sš]nak|xšank|ka[sš]ang' ISS_alt_DKS.txt; grep -c -i -E 'QASHANG|GHASHANG|QAŠANG' incoming/ARY/ARY_latin_index_pages.txt; grep -c 'قشنگ' incoming/ARY/ARY_pages.txt; grep -c -i -E 'ka[sš]ang|qa[sš]ang' LKT.txt"
}
```


### [2026-10-17T00:34:31.386Z] TOOL RESULT

```
1
0
0
0
```


## [2026-10-17T00:34:35.168Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'ga[sš]nak|xšank|ka[sš]ang' ISS_alt_DKS.txt | cut -c1-300"
}
```


### [2026-10-17T00:34:35.491Z] TOOL RESULT

```
2393:the small and such a thing’; JS 24v2-3 ustairsfai amgam bedá jsinakye chale ‘you tore the fine skin on your limbs’. Five spellings in Z jseiņa-, jseina-, jsena-, jsdna-, jsei; Tumiuq Зака tsdnakar ‘small’ of insects (BSOAS 13, 1950,657). From *fasna- (as tceiman- ' eye! from casman-) with palat
```


## [2026-10-17T00:34:40.348Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'E'\nimport json\np='data/verification/page-560.json'\nd=json.load(open(p))\nfor c in d['entries'][0]['nodes'][0]['consulted']:\n    if c['src']=='ISS_alt_DKS':\n        c['where']=\"ISS_alt_DKS.txt grep -i 'gašnak|xšank|kašang'\"\n        c['note']=\"only one unrelated hit (line 2393, Khotanese jsinakye 'fine, small' < *fasna-); nothing on Sogdian ʾxšnk or *gašnaka-.\"\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nE\npython3 tools/verify_check.py 560 | grep -c PROBLEM"
}
```


### [2026-10-17T00:34:40.786Z] TOOL RESULT

```
0
```


## [2026-10-17T00:34:48.222Z] TOOL CALL #35: SubagentHandback

```json
{
 "message": "I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-560.json` for PDF page 560 (book page 530); `verify_check.py 560` shows 0 PROBLEM lines.\n\n- **Roots (2):** 1 confirmed, 1 plausible.\n- **Nodes (4):** 2 confirmed, 2 plausible. Nothing is disputed or transcription_suspect.\n- **Nourai's refs:** 4 support, 1 partial, 1 not_checked.\n\nThe plausible items:\n- **`Xšnk / gašnaka (node 1):** gašnaka is not an attested Sogdian word. It is Gharib's reconstructed ancestor *gašnak(k)a- (SOD entry 731), but the chart labels it Sogdian and draws it as a child of ʾxšnk, which reverses the real relation. The root ʾxšnk 'beautiful' and Persian qašang (from Sogdian, per Wiktionary) are confirmed.\n- **Xvaini (root) and Pahlavi xvân (node 1):** Horn no. 498 (p. 110) supports Nourai exactly. Hübschmann (Pers. Stud. p. 57) rejects the link, because the Pahlavi translation renders Av. xᵛaini- as xūp 'beautiful'.\n  - Mo'in's footnote at BQT:783 repeats that rejection.\n  - Wiktionary lists the Avestan cognate, but its only source for it is Nourai p. 530, so it is not independent.\n  - Aryanpur (p. 249) puts خوان under a different root, PIE *swād- 'sweet'.\n  - The word itself is confirmed: MacKenzie p. 95 has Pahlavi xwān 'tray, table', and Persian xân comes straight from it.\n\nAEF:640 could not be checked: it is not on disk or online.\n\nThere are no extraction errors to fix: the JSON matches the printed page. I saved the page image to `data/verification/sources/refs/ocr/BOOK/560.png`."
}
```


### [2026-10-17T00:34:48.485Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
