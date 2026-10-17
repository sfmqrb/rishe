# Verification process log — verify-page-567


## [2026-10-17T00:30:14.405Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 567 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-567.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-567.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-567.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 567` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.473Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:21.575Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:21.595Z] TOOL RESULT

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


## [2026-10-17T00:30:22.074Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-567.txt"
}
```


### [2026-10-17T00:30:22.095Z] TOOL RESULT

```
1	=== PDF page 567 (book page 537) ===
2	--- entry 0 ---
3	ROOT [Semitic] Y.m.n : south, right hand (prosperous) side, prosperity  (refs KLN:164)
4	#1 (parent #0) [Arabic] refs=KLN:164 | yamîn : right hand, south side, fortunate and happy ; Yemen : the southern country ; maymŭn : blessed, fortunate, monkey | NOTE: Arabs used "maymŭn" euphemistically to denote the monkey whose sight is supposed to bring misfortune.
5	  #2 (parent #1) [Persian] refs=FVA:453 | yomn «یُمن» : good fortune ; Yaman «يَمَن» : Yemen ; meymŭn, maymŭn «میمون» : monkey, blessed | extra: میمنت ، تیمّن
6	  #3 (parent #1) [Turkish] refs=PRT:413; KLN:164,997 | maymŭn : monkey
7	    #4 (parent #3) [Italian] refs=KLN:997; PRT:413 | monna : monkey | NOTE: Several references, including AHD, derive "mona" from "Moneke", name of a monkey in a famous story in Europe.
8	      #5 (parent #4) [Middle German] refs=KLN:997 | meneke : ape
9	        #6 (parent #5) [English] refs=KLN:997; PRT:413 | monkey, mona
10	  #7 (parent #1) [English] refs=KLN:1762 | Yemen
11	#8 (parent #0) [Hebrew] refs=KLN:164 | yâmîn : right hand ; Ben-yâmin : son of the right (fortunate) side ☞B.n.v
12	  #9 (parent #8) [Persian] refs=MON5 | Benyâmîn «بنیامین» : Benjamin
13	  #10 (parent #8) [English] refs=KLN:164 | Benjamin
14	
```


## [2026-10-17T00:30:22.894Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-567.json"
}
```


### [2026-10-17T00:30:22.933Z] TOOL RESULT

```
1	{
2	  "pdf_page": 567,
3	  "book_page": 537,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Y.m.n",
8	        "lang": "Semitic",
9	        "refs": "KLN:164",
10	        "gloss": "south, right hand (prosperous) side, prosperity"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Arabic",
17	          "refs": "KLN:164",
18	          "words": [
19	            {"translit": "yamîn", "gloss": "right hand, south side, fortunate and happy", "script": null},
20	            {"translit": "Yemen", "gloss": "the southern country", "script": null},
21	            {"translit": "maymŭn", "gloss": "blessed, fortunate, monkey", "script": null}
22	          ],
23	          "note": "Arabs used \"maymŭn\" euphemistically to denote the monkey whose sight is supposed to bring misfortune.",
24	          "quote": null
25	        },
26	        {
27	          "id": 2,
28	          "parent": 1,
29	          "lang": "Persian",
30	          "refs": "FVA:453",
31	          "words": [
32	            {"translit": "yomn", "gloss": "good fortune", "script": "یُمن"},
33	            {"translit": "Yaman", "gloss": "Yemen", "script": "يَمَن"},
34	            {"translit": "meymŭn, maymŭn", "gloss": "monkey, blessed", "script": "میمون"}
35	          ],
36	          "script_extra": "میمنت ، تیمّن",
37	          "note": null,
38	          "quote": {"text": "شد از فروغ ریاحین چو آسمان روشن - زمین به اختر میمون و طالع مسعود", "poet": "Hâfez"}
39	        },
40	        {
41	          "id": 3,
42	          "parent": 1,
43	          "lang": "Turkish",
44	          "refs": "PRT:413; KLN:164,997",
45	          "words": [
46	            {"translit": "maymŭn", "gloss": "monkey", "script": null}
47	          ],
48	          "note": null,
49	          "quote": null
50	        },
51	        {
52	          "id": 4,
53	          "parent": 3,
54	          "lang": "Italian",
55	          "refs": "KLN:997; PRT:413",
56	          "words": [
57	            {"translit": "monna", "gloss": "monkey", "script": null}
58	          ],
59	          "note": "Several references, including AHD, derive \"mona\" from \"Moneke\", name of a monkey in a famous story in Europe.",
60	          "quote": null
61	        },
62	        {
63	          "id": 5,
64	          "parent": 4,
65	          "lang": "Middle German",
66	          "refs": "KLN:997",
67	          "words": [
68	            {"translit": "meneke", "gloss": "ape", "script": null}
69	          ],
70	          "note": null,
71	          "quote": null
72	        },
73	        {
74	          "id": 6,
75	          "parent": 5,
76	          "lang": "English",
77	          "refs": "KLN:997; PRT:413",
78	          "words": [
79	            {"translit": "monkey, mona", "gloss": null, "script": null}
80	          ],
81	          "note": null,
82	          "quote": null
83	        },
84	        {
85	          "id": 7,
86	          "parent": 1,
87	          "lang": "English",
88	          "refs": "KLN:1762",
89	          "words": [
90	            {"translit": "Yemen", "gloss": null, "script": null}
91	          ],
92	          "note": null,
93	          "quote": null
94	        },
95	        {
96	          "id": 8,
97	          "parent": 0,
98	          "lang": "Hebrew",
99	          "refs": "KLN:164",
100	          "words": [
101	            {"translit": "yâmîn", "gloss": "right hand", "script": null},
102	            {"translit": "Ben-yâmin", "gloss": "son of the right (fortunate) side", "script": null, "see": ["B.n.v"]}
103	          ],
104	          "note": null,
105	          "quote": null
106	        },
107	        {
108	          "id": 9,
109	          "parent": 8,
110	          "lang": "Persian",
111	          "refs": "MON5",
112	          "words": [
113	            {"translit": "Benyâmîn", "gloss": "Benjamin", "script": "بنیامین"}
114	          ],
115	          "note": null,
116	          "quote": {"text": "چون نه یعقوبی و نه بن یامین - زین دعا نشنوی مگر امین", "poet": "Hadîqat-ol-Haqîqat"}
117	        },
118	        {
119	          "id": 10,
120	          "parent": 8,
121	          "lang": "English",
122	          "refs": "KLN:164",
123	          "words": [
124	            {"translit": "Benjamin", "gloss": null, "script": null}
125	          ],
126	          "note": null,
127	          "quote": null
128	        }
129	      ]
130	    }
131	  ]
132	}
133	
```


## [2026-10-17T00:30:26.585Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['KLN','FVA','FVQ','PRT','MON','MON5','AHD','LKT','SKT','HJB','TTS','AFM','PLA','AFA']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\"; sed -n 1,200p sources/SOURCE_MATRIX.md | head -120"
}
```


### [2026-10-17T00:30:26.938Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe-private/data/
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
MON5 null
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered e
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f betwee
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 5
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djv
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sourc
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"],
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n
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
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/UNV.txt`
```


## [2026-10-17T00:30:29.909Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; sed -n 120,250p sources/SOURCE_MATRIX.md; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False))\"; command ls /home/sfmqrb/git/rishe-private/data/verification/ | head; cat /home/sfmqrb/git/rishe-private/tools/verify_check.py | head -80"
}
```


### [2026-10-17T00:30:30.435Z] TOOL RESULT

```
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/UNV.txt`
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
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

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HJB.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AID.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/GPL.txt`
- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/RCH.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt`
- **NAT** — C. Berlitz, Native Tongues, New York 1982
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NAT_2005.txt`
- **PEI** — M. Pei, The Families of Words, New York 1962
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PEI.txt`

## Turkic / Mongolian

- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/VIE/VIE_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf`

## Sanskrit / Hindustani

- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HJB.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/GPL.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AID.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt`{"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)", "local_files": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt"], "cites": "page number, continuous across the two volumes (1966–67)"}
agent
COORDINATOR.md
page-100.json
page-101.json
page-102.json
page-103.json
page-104.json
page-105.json
page-106.json
page-107.json
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


## [2026-10-17T00:30:36.397Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^(Benjamin|monkey|mona|Yemen|Yemenite)\\b' KLN_1966.txt | head; grep -n -i -E '^(Benjamin|monkey|mona|Yemen|Yemenite)\\b' KLN_1971.txt | head"
}
```


### [2026-10-17T00:30:37.004Z] TOOL RESULT

```
4759:Benjamin,  masc.  PN. ;  in  the  Bible,  Jacob’s  young¬ est  son.  —  Heb.  Binyamtn,  lit.  ‘son  of  the  right hand’,  fr.  ben  ‘son’,  and  yamtn,  ‘right  hand’; see  Gen.  35: 18.  For  the  first  element  see  ben, ‘son’.  Heb.  yamtn  means  also  ‘south’  (lit.  ‘the right  hand,  the  right  side’,  i.e.,  if  one  faces  east). It  is  rel.  to  Aram.-Syr.  yammin,  Ugar.  ymn, ‘right  hand’,  Arab,  ydman,  ‘right  hand,  right side,  south’,  ydmana,  ‘he  was  happy’,  lit.  ‘he turned  or  went  to  the  right’  (the  right  side  was regarded  as  auspicious),  Ethiop.  yaman,  Akkad. imnu,  ‘right  hand,  right  side’.  Cp.  Yemen,  mai- mon,  monkey.
4760:benjamin,  n.,  gum  benzoin.  — Corruption  of  ben- join,  an  earlier  form  of  benzoin  (q.v.) hennet,  n.,  a  herb.  —  ME,  herbe beneit,  ‘the  bless¬ ed  herb’,  fr.  F.  benoite ,  prop.  fern.  pp.  of  OF. beneir  (F.  benir),  ‘to  bless’,  fr.  L.  henedicere. See  benediction.
24225:Mona,  fern.  PN.  —  Ir.  Muadhnait,  prop,  dimin. of  muadh,  ‘noble’.
24226:mona,  n.,  a  small  African  monkey  (Cercopithecus mona).  —  Sp.  and  Port,  mona,  ‘female  monkey’, fem.  of  mono,  ‘monkey’.  See  monkey, monachal,  adj.,  pertaining  to  a  monk;  monastic. —  Eccles.  L.  monachalis,  ‘pertaining  to  a  monk’, fr.  Late  L.  monachus,  ‘monk’.  See  monk  and  adj. suff.  -al.
24264:monkey,  n.  —  MLG.  Moneke(n),  name  of  an  ape, prob.  fr.  MIt.  monnicchio,  fr.  Olt.  monna  (cp. Sp.  and  Port,  mono,  mono),  ‘ape,  monkey’, aphetically  formed  fr.  Turk,  maymiin,  of  s.m.,  fr. Arab,  maymun,  ‘auspicious’,  used  euphemis¬ tically  to  denote  the  ape  or  monkey,  whose  sight is  supposed  to  bring  misfortune.  See  Theodor Noldeke,  Worter  mit  Gegensinn,  in  his  Neue Beitrage  zur  semitischen  Sprachwissenschaft, Strassburg,  1910,  p.  89.  Arab,  maymun  is  pass, part,  of  yamana,  ‘he  was  happy,  he  was  for¬ tunate;  it  was  auspicious’,  fr.  yaman,  ‘right  side, south’,  yamfn,  Tight  hand’,  See  Benjamin  and cp.  maimon  and  raona,  ‘a  small  African  monkey’. —  Olt.  monna,  ‘ape,  monkey’,  has  been  influ¬ enced  in  form  by  monna,  ‘woman’,  contraction of  ma  donna,  ‘my  lady’.
26379:Benjamin Smith Barton of Philadelphia (died 
28329:Benjamin, masc. PN. ; in the Bible, Jacob’s young- 
28343:benjamin, n., gum benzoin. — Corruption of ben - 
75388:monkey. 
153741:Mona, fem. PN. — Ir. Muadhnait, prop, dimin. 
153744:mona, n., a small African monkey {Cercopithecus 
153771:mona], also monaul, n., a large pheasant of the 
154022:monkey, n. — MLG. Monekc(n), name of an ape, 
183425:monkey’, and &v$p<o7ro<;, ‘man’. For the first 
249965:monkey. — F., fr. Sp. toca , fr. Arab. taqiya h ,
```


## [2026-10-17T00:30:40.817Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(Yemen|maimon)' KLN_1966.txt | head; for l in 4759 24264; do awk -v L=$l 'BEGIN{p=0} {if(NR<=L){c+=gsub(/\\f/,\"&\")}} END{print L, \"leaf\", c}' KLN_1966.txt; done; grep -n -i 'yemen' KLN_1966.txt | head"
}
```


### [2026-10-17T00:30:41.171Z] TOOL RESULT

```
22594:maimon,  n.,  the  mandrill.  —  It.  maimone,  fr.  Pers. maymun,  ‘ape’,  fr.  Arab,  maymun,  ‘auspicious’. See  monkey.
4759 leaf 97
24264 leaf 535
4759:Benjamin,  masc.  PN. ;  in  the  Bible,  Jacob’s  young¬ est  son.  —  Heb.  Binyamtn,  lit.  ‘son  of  the  right hand’,  fr.  ben  ‘son’,  and  yamtn,  ‘right  hand’; see  Gen.  35: 18.  For  the  first  element  see  ben, ‘son’.  Heb.  yamtn  means  also  ‘south’  (lit.  ‘the right  hand,  the  right  side’,  i.e.,  if  one  faces  east). It  is  rel.  to  Aram.-Syr.  yammin,  Ugar.  ymn, ‘right  hand’,  Arab,  ydman,  ‘right  hand,  right side,  south’,  ydmana,  ‘he  was  happy’,  lit.  ‘he turned  or  went  to  the  right’  (the  right  side  was regarded  as  auspicious),  Ethiop.  yaman,  Akkad. imnu,  ‘right  hand,  right  side’.  Cp.  Yemen,  mai- mon,  monkey.
11180:tives  of  I.-E.  base  *dek-,  ’to  take,  receive, accept;  acceptable,  becoming,  good’,  whence also  L.  decere,  ‘to  be  fitting  or  seemly’.  See decent  and  cp.  words  there  referred  to.  Cp.  also ambidexter.  L,  dexter  and  Gk.  8e!;iTEp6p  were formed  fr.  base  *dek-  with  the  compar.  suff. -ter,  -terus,  resp.  -TEpoq,  and  orig.  meant  ‘that which  is  in  the  better  or  more  favorable  direct¬ ion’.  For  the  compar.  suff.  see  -ther  and  cp. words  there  referred  to.  For  the  sense  develop¬ ment  of  L.  dexter,  Gk.  Se^tTEpii;,  Seijioi;,  etc., cp.  Heb.  yamtn,  ‘right  hand,  south’,  Arab. yaman,  ‘right  hand,  south’,  yamana,  ‘he  was happy’  (see  Yemen).
16966:Habakkuk,  n.,  i)  the  eighth  in  the  order  of  the Twelve  Prophets;  2)  the  Book  of  Habakkuk (Bible).  —  Heb.  Habhaqqttq ,  prob.  from  the base  of  habhaq ,  ‘he  embraced’.  Cp.  Akkad,  harn- baququ ,  name  of  a  garden  plant,  Arab,  habaqiq, name  of  a  plant  in  Yemen  (‘the  basil’), habanera,  n.,  a  Cuban  dance  imported  from Africa.  —  Sp.  ( danza )  habanera,  ‘Havanan dance’,  fern,  of  habanero,  ‘Havanan’,  formed  fr. Habana ,  ‘Havana’,  with  suff.  -era  fr.  L.  - arias ; see  adj.  suff.  -ary.
```


## [2026-10-17T00:30:47.276Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^Yem' KLN_1971.txt KLN_1966.txt | head; tail -c 3000 KLN_1966.txt | head -30; grep -c $'\\f' KLN_1966.txt"
}
```


### [2026-10-17T00:30:47.615Z] TOOL RESULT

```
KLN_1971.txt:269722:Yemen, n., a region forming the southwestern 
��  Lit.  ‘neigh¬ borhood’,  fr.  ML.  vicinetum,  fr.  L.  vicinus, ‘neighboring,  near’,  fr.  views,  ‘district’;  see vicinage.  Venue  in  this  sense  was  influenced  in form  by  venue,  ‘arrival’.
venule,  n.,  a  small  vein.  —  L.  venttla,  formed  fr.
vena  with  dimin.  suff.  -i da.  See  vein  and  -ule. Venus,  n.  —  L.  Venus,  gen.  Veneris,  ‘the  goddess of  love’.,  fr.  venus,  ‘love,  sexual  desire,  loveliness, attractiveness,  beauty,  charm’,  whence  venerari, ‘to  reverence,  worship,  venerate’.  See  venerate, vera,  n.,  name  of  a  tree,  Bu/nesia  arborea.  —  Am. Sp.,  fr.  Sp.  vera,  ‘border’,  which  derives  fr.  L. ora,  ‘border’  (through  the  intermediate  form *uera\  cp.  Sp.  hueso,  ‘bone’  (fr.  L.  ossum).  L. ora  (for  *osa)  is  a  collective  noun  formed  fr.  os, gen.  -oris,  ‘mouth,  opening,  entrance’.  See  oral, veracious,  adj.,  truthful,  true.  —  Formed  with suff.  -ous  fr.  L.  verax,  gen.  veracis,  ‘truthful, speaking  truly",  fr.  verus.  See  very.
Derivatives:  veracious-ly,  adj.,  veracious-ness,  n. veracity,  n.,  truthfulness,  truth.  —  F.  veracite,  fr. ML.  veracitdtem,  acc.  of  veracitas,  ‘truthfulness’, fr.  L.  verax,  gen.  -acis.  See  prec.  word  and  -ity. veranda,  verandah,  n.  —  Port,  varanda,  ‘balcony’, introduced  into  English  from  India.  Port,  ra- randa  itself  is  of  uncertain  origin.  F.  veranda was  borrowed  from  English.
Derivative:  veranda(h)-ed,  adj. verano,  n.,  the  dry  season  in  tropical  America.  — Sp.,  fr.  L.  ver,  ‘spring’.  See  vernal.
Verbesina
verascope,  n.,  a  small  stereoscopic  camera.  —  A hybrid  coined  fr.  L.  verus,  ���true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) .
veratral,  n.,  the  radical  C9H10O4  (chem.)  —  Form¬ ed  with  adj.  suff.  -al  fr.  L.  verdtrum,  'hellebore’. See  veratrine.
veratric,  adj.,  pertaining  to  a  white  crystalline acid. —  Formed  with  adj.  suff.  -ic  fr.  L.  verdtrum, ‘hellebore’  (see  veratrine) ;  so  called  because  it  is easily  obtained  by  the  decomposition  of  vera¬ trine.  \
veratridine,  also  veratridin,  n.,  an  amorphous  al¬ kaloid  obtained  from  sabadilla  seeds, C36H61OnN  (chem.)  —  Coined  fr.  L.  verdtrum, ‘hellebore’  (see  next  word),  and  the  chem. suffixes  -ide  and  -ine  (resp.  -in), veratrine,  n.,  also  veratrin,  veratrina,  veratria,  a poisonous  mixture  of  alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because902
```


## [2026-10-17T00:30:51.302Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 269722,269735p KLN_1971.txt; grep -n -i -E 'monkey|maimon|meimun|maimun' SKT.txt | head; grep -n -i -E '^ *(monkey|mona)\\b' FSD_vol*.txt WEB_vol1.txt | head"
}
```


### [2026-10-17T00:30:51.666Z] TOOL RESULT

```
Yemen, n., a region forming the southwestern 
part of Arabia. — Vulgar pronunciation of 
Arab. Ydman, lit. ‘the country of the South; the 
happy country’ (cp. its Latin name Arabia Fe- 
lix, ‘Happy Arabia’), fr. ydman, ‘right hand, 
right side; south (i.e. the right side, if one faces 
east’), whence ydmana , ‘he was happy’, lit. ‘he 
turned or went to the right’ (the right side was 
regarded as auspicious), yammana, ‘he went to 
the right; he blessed; he went to Yemen’. See 
Benjamin and cp. words there referred to. 
Derivatives: Yemen-ic, adj., Yemen-ite, adj. and 
n. 

10879:mademoiaelle,  miss.  (F,  -  L )  F. ma,  my;  dtmoiselle,  riamitel  ;  see  Damsel, madonna.mylady.  U^bI*-!'-)  Ital.wa. my;  donna^  laHy.fiomL.  i/i?wma;  see  Dame. monkey,  an  ape.  (ItAl.~L.)  Corrapted from  O.  Ital.  nwHuchw,  'a  pugge.  a  mun- kie.  an  ape  ; '  Florio.  Dimin.  of  O.  Ilal. mono,  monna,  'an  ape,  a  munkte.  a  mun- kie-face;  also  a  nickname  for  women,  as we  say  gammer,  goodie ;  *  Florio.  Afonna is  a  familiar  corruption  of  madattna,  i.e. my  lady,  mistress  ;  Scott  introduces  ^/i7M/ia r.iuhi  in  the  Fortunes  of  NigeU  See  above.
11142:Marmoset,  a  small  Aitieric3n  monkey, (F.  — L.)  Much  older  than  the  discovery of  America ;  M.  E.  marmostttt,  a  kind  of ape  (Maundeville,  p.  aio).  —  O.  F.  mar- moset, F.  marmoHset, '  the  cock  of  a  cistern or  fountain,  any  flntick  image  from  who^e leats  water  trllleth,  any  puppet  or  andck;' Cot.  Thus  it  meant  a  grotesque  creature, '^fiS-  A  grotesque  ornament  on  a  fountain. Kormeci.  by  a  Parisian  change  of  r  to  /,  as in  chaise  for  ehaire,  (a  chnir).  from  Low  L. marmorelum,  a  thing  made  in  marble,  ap- plied to  fountains.  [Thus  the  rtu  dts  mar- mousfti  in  Paris  was  called  in  Low  Latin xticut  marmtrrtterttm ;  Littri.]  —  L.  marmor, marbie ;  sec  Marble.  %  This  seems  to  be quite  CDiitcL;  at  the  same  time,  the  trans- frrmce  in  sense  from  Mrinklng-fountain'  to 'afr  '  wta  oertMioiy  helped  on  by  confutiob
11144:with   F.  marmot,  *a  tnarmoset,  or  K monkey;*  which  ts,  a^in,  quite  a  diffeid word  from  E.  tnat  •  '-jw),
11832:Monkey:  secUadam.
17286:monkey-tike.    (L.)       From  L.
23443:lower,     mez2otinto,     miniature,    monkey,
WEB_vol1.txt:45936:mona,
WEB_vol1.txt:49964:monkey of South America.
FSD_vol3.txt:326:monkey of the genus Maaieua, of stout form, with Maivbcth', 1 mak-befli': 2
FSD_vol3.txt:40803:monkey-drift
FSD_vol3.txt:49261:Monkey*broAd
FSD_vol3.txt:49343:monkey
FSD_vol3.txt:96450:Mona (1912)
FSD_vol3.txt:151696:monkey, a sbort-taUed macaque (JAaeacut nemtUrinut) of
FSD_vol3.txt:178304:monkey, n I Slang ] l.Naut Ahoy
FSD_vol3.txt:189036:monkey.
```


## [2026-10-17T00:30:54.564Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 49335,49360p FSD_vol3.txt; grep -n -i -E 'maim[uû]n|meimun|maymun' LKT.txt TTS*.txt incoming/TTS/TTS_pages.txt | head; grep -n -i -E 'monkey' WEB_vol1.txt | head -5"
}
```


### [2026-10-17T00:30:54.924Z] TOOL RESULT

```
— sykes's m.. an African corcoplthecld {Cereopithecua tUbo-
guluris),— to have or get one's m. up [Blang], to be or
become angry.— to suck the m., same as to tap the ap-
uiKAi.. HecADMiiiAL. - whlte-eyellU m., the mangabey
mon'key-fy, 1 mun'ki-fal. 2 mdo'kv-fV, pi 1-kied. -pt'ino ]
(Rare ) I'n make like a monkey, dress in affeotod or out-
landish fashion
moil 'key-lsli* 1 mtiQ'ki-!^; 2 moo'ky-lsh, a Like a
monkey
Thn Bpociflo mnviug power to tho working-out of speech wm
not thn monkeyiah tuiuloiioy f4> iiiutattuu, but tho human ten*
rinttpy to ■ot'iality W l> Wtiirsar Oriental and Ltngutalic
atudiM fimi eariM. p 200 Is JH7.f ]
moil 'key-igm, 1 inuo'ki-izm: 2 mdo'kv-Tgm, n. Be-
havior chaructiTihtic of a monkey, mnnkcv-shmcN
Monk^-Ues'le-don, 1 muok'-hcz'l-dsn, 2 niOOk'-hOs'l-don,
n. A vllliigo In Durham county, England
Mon'fKhiiier", 1 indn'-kmor'; 2 niOn'-km^r”, n 1. A
brunch of the Indo-C'hluese family which Invaded Burma at
an early date according to the C^cnsiis Report, IfNll, It
constltuusi 1 iKT cent of the population 2. A division of
the ludu-Chlnese group of languages. Including the Tululng,
Wu. and raltiung. It was formerly simkeii from the Khasl
Hills of Assam lo the Paclllc ocean and from (.Central Asia to
the Malay Peninsula Bee under Inuo-C'hinkhl
Monk'liuuse, 1 muQk'hauH. 2 iiduk'hous, Tlllllam Cosmo
(eval):1: no matches found: TTS*.txt
6014:al-öu-atte’ (-at’), n. [Fr., from native name.] 3 the South American howling monkey.
8540:An-thro-poid/é-a, n.pl. [Mod. L., from Gr. anthropos, man, and eidos, resembling.] the suborder of proat manmel which includes man, apes, and monkeys.
8978:1. a chimpanzee, go- rilla, orangutan, or gib- bon; a large, tailless monkey that can stand and walk in an almost = erect position.
8979:2. any monkey.
10208:äräguä’tö (-gwa/to), n. [S. Am.] a species of monkey found in South America; the ursine howler, Mycetes ursinus: also called araba, etc.
```


## [2026-10-17T00:30:59.213Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'maim\\|mejmun\\|majmun' LKT.txt | head; grep -n -i 'maimun\\|maymun\\|majmun\\|meimun' incoming/TTS/TTS_pages.txt | head; grep -n -E \"^mon'?key|^mon.key, n\" WEB_vol1.txt | head"
}
```


### [2026-10-17T00:30:59.624Z] TOOL RESULT

```
1410:553.  Pers.  diirük-kär: 'Zimmermann'  [aus  durük  'dünnes  Holz' Horn  NpEt  S.  116,  Nr.  522  und  kär 'Täter'  ebenda  S.  185,  Nr.  832],  hieraus zunächst  mit  Dissimilation  von  r  zu  l tk.  dillger  'dass.'  und  dann  rum.  dulgher 'Zimmermaim',  dulgherie  'dessen  Hand- werk', bulg.  dulger,  dulgerin,  serb.  dun- der,  dunderin  'Zimmermann'.  [Bern SlEtWb  259.
3166:13fi5.  Ar.  luaimuu: 'Affe'  [eigentlich  'glücklich,  glückbrin- gend' genau  wie  das  andere  Wort  für Affe:  ar.  su'dän,  si'dän;  Euphemismus, da  der  Alle  als  Teufel  gilt.  Vgl.  Nöldeke, Neue  Beiträge  zur  semitischen  Sprach- wissenschaft. S.  89.  Zusammenhang mit  gl',  m^d»  ist  also  abzulehnen];  hier- aus it.  mammone  'Meerkatze',  maimone [Oriente  I,  195],  afrz.  prov.  maimon, kat.  maymon  'heuchlerisch,  faul',  sp.  pg. mono,  mona,  frz.  maimon,  mona,  Ablei- tung mimonet,  momine,  rum.  malmu^ä, momi^ä  [mit  Sulfixwechsel];  ferner  [mit Wechsel  von  m  zu  b]  it.  babuino;  engl. haboon  'Affe';  bulg.  majmima,  serb. majmun,  poln.  munia.  [ML  5242.  Devic DEt  155  (auf  pers.  m.  zurückgeführt). Mikl  SiElWb  ISO.
5452:maimün  1365
5655:modern  1341 magaza  1362 niagazin  1362 mahala  1350 mahmuren  1359 mahrama  1361 majasil  1368 majmuna  1365 matigal  1392 mastrapa  1439 medzit  1435 megdan  1364
6625:mahalep  135ti maharadja  1692 mahari  1"560 mahonfnje  144!) maimon  1365 malamoque  1384 malcuss  dial.  1379 mamlouk  1381 manimouth  1385 inandole  2016 mandore  2015 mangliev  1394 mangoustan  1395 mangue  1393 manguier  1393 «irtiime  1398 mardbout  141U marcassite  1374 Marion  1417 marionnette  1417 tnaroquin  1406 marotte  1417 mascarade  1436 masque  1436 massepain  1452 masser  1440 massicot  1735 »lai!  1443 matasse  476 matassin  1525 matelas  1446 mater  1443 materas  1446 maugrebin  674 milangine  161 melchites  1379 meranghie  161  • meschin(e)  afz.  1470 mesquin  1470 Messie  1437 migerat  afz.  1476 mimonet  1365 minaret  1463  a miqueht  1469 (grand)  Mogol  1494 moirS  1497 moirer  1497 »MoZoc/?  1379 momie  1510 momine  1365 >noMa  1365 morceau  d' Adam  19 mortaise  1713 mort-de-chien  1478 mosquee  1435 mosquete  afz.  1435 moucayarde  1497 moucre  1507 mousquet  1520 mousseline  1484 mousson  1451 mudzzin  1485
7107:magazzino  1362 :  maimone  1365 i  malase(nu)  siz.  1362 !  malco  dial.  1379
8549:maimon  1365
8719:mn!  64 macar  1456 macara  1371 mar-«!'  1370 madem  1341 magaza  1362 magazin  1362 mahal  806 mahala(giü)  1350 mahmicr(ie)  1359 waza  1367 maidan  1364 maimu^ä  1365 malotea  1380 mamelegiü  1487 mmneluc  1384 manä  1398 mandanea  1390 mangal  1392 marabut  1410 marafet  1418
49964:monkey of South America.
```


## [2026-10-17T00:31:07.790Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'میمون' MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head; grep -n 'بنیامین\\|بن یامین\\|بنيامين' MON_part*.txt incoming/MON/*djvu.txt BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null| head; grep -n -i 'yamin\\|yaman\\|yamtn\\|Binyam\\|Benjamin' FVQ_pages.txt AFA.txt | head"
}
```


### [2026-10-17T00:31:08.166Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v1_djvu.txt:2337:میمون» مبار ک. () بلندی در زمین» تل» 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:4721:آمد و نیامد» میمون و فرخنده ودن و نودن. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:21679:شده. ضح.. در قدیم شوم و نامیمون 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:26096:بوزنینه ] (.) (جاذ.) میمون. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:29828:اتاقه» اتاغه» قدما چون سابهٌ هما را میمون 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:33739:کپی» میمون. (به واسطهٌ آنکه رویش پهن 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:34208:پیچی ثیل: -0157 [تر.] (امر.) سال میمون» 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:34505:الب مسنصور فبروزه !سنج میمون» 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:55504:میمون» با سعادت. نیکك» خوب؛» خوش. (.) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:58239:آنچه که میمون و مبارک باشد» چیزی که 
FVQ_pages.txt:7280:which was put in Benjamin's sack.
```


## [2026-10-17T00:31:13.296Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -50; grep -n 'میمون\\|یمن' data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -20"
}
```


### [2026-10-17T00:31:13.653Z] TOOL RESULT

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
5963:خجسته. مبار ث. میمون. زیبا. جمیل. 
6005:میمون. مطرب؛ توازنده و سازنده. (کگیا.) 
6013:آنکه به طالع میمون متولد شده مبا رک زاد. 
6035:قس. شش منده | (ص.) مبارک» میمون 
12191:فرد: 2۵«(ع.] (4.) بوزینه» میمون نر) ج. 
12632:صاحیمنصبان روسی تربیت شده به لباس 
14728:گل میمون که یکساله است و برگک‌هایش 
17287:(اهریمن) انجام دهد. (کد.) کاری که 
19126:فرعونی» صبار» انجیر بربری» انجیر یمنی» 
20122:درآبند. روزها را کسک در محلی ایمن 
20526:کپی: 1-(0۴)0: [- کبی - گپی] )٩(‏ میمون 
28378:ضح.- (پز.) نشیمنگاه و در حقیقت ناحية 
28381:مقعد» نشیمنگاه» دبر. کون خر؛ نشستنگاه 
29954:میمون» قرد. 
33263:ساله از تیرهةٌ گل میمونیان که پوشیده از 
33768:گل میمونیان که اکثر گونه‌هایش بسصورت 
33793:است از تيرة کل میمونیان که دارای برخی 
33802:از گونه‌های گل میمون است که بنام‌های 
33856:(گیا.) گیاهی است از تيرهة گل میمونیان که 
33893:(قس. خار عقرب - بهرام). گل میمون:
```


## [2026-10-17T00:31:24.325Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in میمون یمن بنیامین; do python3 tools/fetch_source.py \"https://vajehyab.com/moein/$w\" --note \"page 567, root Y.m.n, Mo'in entry for $w\"; done; for u in \"https://en.wiktionary.org/wiki/%D9%85%D9%8A%D9%85%D9%88%D9%86\" \"https://en.wiktionary.org/wiki/monkey\" \"https://www.etymonline.com/word/monkey\" \"https://www.etymonline.com/word/Benjamin\" \"https://www.etymonline.com/word/Yemen\" \"https://en.wiktionary.org/wiki/%D9%8A_%D9%85_%D9%86\" \"https://en.wiktionary.org/wiki/%D7%91%D7%A0%D7%99%D7%9E%D7%99%D7%9F\" \"https://en.wiktionary.org/wiki/maymun\" \"https://en.wiktionary.org/wiki/monna\" \"https://en.wiktionary.org/wiki/mona\" \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D9%85%D9%88%D9%86\"; do python3 tools/fetch_source.py \"$u\" --note \"page 567, root Y.m.n\"; done"
}
```


### [2026-10-17T00:31:30.874Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/80b526dd32b093e7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a4b97ae6d6b0ecca.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/306bdac3d18a482d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7bdaf2fd61db5ed1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/11e5553655e4317d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d829a54a2d9c0ace.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c2270a4e21212b79.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3e3f5c5acf3ff81b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8b3ae74e1e5d2d55.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2ae1a136c2d652e5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b79a8e42576ea2ce.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4475c3ac63d36ab2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3c0655dc11837ef0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a0139a2332039239.txt
```


## [2026-10-17T00:31:35.203Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -14 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['url'][:70], d.get('status'), d.get('bytes'), d['file'])\"; for f in 80b526dd32b093e7 a4b97ae6d6b0ecca 306bdac3d18a482d; do echo \"== $f\"; grep -v '^\\s*$' $f.txt | grep -n -m8 -E 'میمون|یمن|بنیامین|\\[' | head -12; done"
}
```


### [2026-10-17T00:31:35.810Z] TOOL RESULT

```
https://vajehyab.com/moein/میمون 200 700 data/verification/sources/web/80b526dd32b093e7.txt
https://vajehyab.com/moein/یمن 200 477 data/verification/sources/web/a4b97ae6d6b0ecca.txt
https://vajehyab.com/moein/بنیامین -1 39 data/verification/sources/web/306bdac3d18a482d.txt
https://en.wiktionary.org/wiki/%D9%85%D9%8A%D9%85%D9%88%D9%86 200 9864 data/verification/sources/web/7bdaf2fd61db5ed1.txt
https://en.wiktionary.org/wiki/monkey 200 37852 data/verification/sources/web/11e5553655e4317d.txt
https://www.etymonline.com/word/monkey -1 39 data/verification/sources/web/d829a54a2d9c0ace.txt
https://www.etymonline.com/word/Benjamin -1 39 data/verification/sources/web/c2270a4e21212b79.txt
https://www.etymonline.com/word/Yemen -1 39 data/verification/sources/web/3e3f5c5acf3ff81b.txt
https://en.wiktionary.org/wiki/%D9%8A_%D9%85_%D9%86 -1 39 data/verification/sources/web/8b3ae74e1e5d2d55.txt
https://en.wiktionary.org/wiki/%D7%91%D7%A0%D7%99%D7%9E%D7%99%D7%9F 200 3778 data/verification/sources/web/2ae1a136c2d652e5.txt
https://en.wiktionary.org/wiki/maymun 200 9922 data/verification/sources/web/b79a8e42576ea2ce.txt
https://en.wiktionary.org/wiki/monna 200 5286 data/verification/sources/web/4475c3ac63d36ab2.txt
https://en.wiktionary.org/wiki/mona 200 33669 data/verification/sources/web/3c0655dc11837ef0.txt
https://en.wiktionary.org/wiki/%D9%85%DB%8C%D9%85%D9%88%D9%86 200 7058 data/verification/sources/web/a0139a2332039239.txt
== 80b526dd32b093e7
1:URL: https://vajehyab.com/moein/میمون
4:TITLE: معنی میمون | فرهنگ انتشارات معین | واژه یاب
5:معنی میمون | فرهنگ انتشارات معین | واژه یاب 
9: میمون
11: (مِ) [ ع . ] (اِمف .) فرخنده ، خجسته . ج . میامن .
12: میمون در فرهنگ‌های دیگر
13: معنی میمون در لغت‌نامه دهخدا 
14: معنی میمون در فرهنگ فارسی عمید / قربان‌زاده 
== a4b97ae6d6b0ecca
1:URL: https://vajehyab.com/moein/یمن
4:TITLE: معنی یمن | فرهنگ انتشارات معین | واژه یاب
5:معنی یمن | فرهنگ انتشارات معین | واژه یاب 
9: یمن
11: (یُ مْ) [ ع . ] (اِ.) خیر و برکت ، خجستگی .
12: یمن در فرهنگ‌های دیگر
13: معنی یمن در لغت‌نامه دهخدا 
14: معنی یمن در فرهنگ فارسی عمید / قربان‌زاده 
== 306bdac3d18a482d
1:URL: https://vajehyab.com/moein/بنیامین
```


## [2026-10-17T00:31:41.346Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 7bdaf2fd61db5ed1 a0139a2332039239 2ae1a136c2d652e5 4475c3ac63d36ab2 b79a8e42576ea2ce; do echo \"== $f\"; grep -i -A4 '^Etymology' $f.txt | head -24; done; grep -n -i -A8 '^Etymology' 11e5553655e4317d.txt | head -30; grep -n -i -B2 -A6 'Etymology' 3c0655dc11837ef0.txt | grep -i -A6 'monkey\\|mono' | head -30"
}
```


### [2026-10-17T00:31:41.788Z] TOOL RESULT

```
== 7bdaf2fd61db5ed1
== a0139a2332039239
== 2ae1a136c2d652e5
== 4475c3ac63d36ab2
== b79a8e42576ea2ce
659- a mona monkey, Cercopithecus mona 
660: Etymology
661- [ edit ] 
662-
663- From Spanish mona ( “ monkey ” ) .
664-
665- Pronunciation
666- [ edit ] 
--
692- [ edit ] 
693-
--
1078- From Spanish mono , of Arabic origin.
1079-
1080- Pronunciation
1081- [ edit ] 
--
1094- ( obsolete ) monkey 
1095-
1096: Etymology 2
1097- [ edit ] 
1098-
1099- Uncertain.
1100-
--
1747- feminine singular of mono 
1748-
1749: Etymology 2
1750- [ edit ] 
1751-
```


## [2026-10-17T00:31:45.574Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 7bdaf2fd61db5ed1 a0139a2332039239 2ae1a136c2d652e5 4475c3ac63d36ab2 b79a8e42576ea2ce 11e5553655e4317d; do echo \"== $f\"; grep -v '^\\s*$' $f.txt | grep -i -n -A3 'etymology\\|from \\|borrowed\\|inherited' | grep -v 'edit \\]' | head -20; done"
}
```


### [2026-10-17T00:31:46.240Z] TOOL RESULT

```
== 7bdaf2fd61db5ed1
39: Etymology 
40- 1.2 
41- Pronunciation 
42- 1.3 
--
99: From Wiktionary, the free dictionary
100- See also: میمون 
101- Arabic
103: Etymology
105: Derived from the passive participle verb form I of the root ي م ن ( y m n ) . See also يَمِين ( yamīn , “ right , right-hand ” ) .
106- Pronunciation
108- IPA ( key ) : /maj.muːn/ 
--
260: → English: monkey , monky ( obsolete ) , monkie ( archaic ) ( or from Middle Low German ) → Chukchi: маӈкы ( maṇky ) 
261- → Coeur d'Alene: moonki 
262- → Irish: moncaí 
263- → Mokilese: moangki 
--
271: → English: monkey ( or from Middle Dutch ) 
272- ⇒ Occitan: monin , monard 
== a0139a2332039239
39: Etymology 
40- 1.2 
41- Noun 
42- 1.3 
--
54: Etymology 
55- 2.2 
56- Pronunciation 
57- 2.3 
--
109: From Wiktionary, the free dictionary
110- See also: ميمون 
111- Ottoman Turkish
--
114: Etymology
116: Etymology tree
117- Arabic يَمَنَ ( yamana ) der. 
118- Arabic مَيْمُون ( maymūn ) bor. 
119- Ottoman Turkish میمون 
120: Borrowed from Arabic مَيْمُون ( maymūn , “ baboon, mandrill ” ) .
== 2ae1a136c2d652e5
39: Etymology 
40- 1.2 
41- Pronunciation 
42- 1.3 
--
52: Etymology 
53- 2.2 
54- Proper noun 
55- 2.2.1 
--
101: From Wiktionary, the free dictionary
102- Hebrew
104: Etymology
106- Roots 
107- ב־ן ( b-n ) 
--
111: From בן and ימין ; son of (the) right hand; Binjamin, youngest son of Jacob; also the tribe descended from him, and its territory.
112- Pronunciation
114- ( Tiberian ) IPA ( key ) : /bin.jɔːˈmiːn/ 
--
== 4475c3ac63d36ab2
62: Etymology 
63- 4.3 
64- Verb 
65- 4.3.1 
--
79: Etymology 1 
80- 5.2.1 
81- Noun 
82- 5.3 
83: Etymology 2 
84- 5.3.1 
85- Noun 
86- 5.3.1.1 
--
146: From Wiktionary, the free dictionary
147- See also: Monna 
148- Italian
--
184: Etymology
186: From Old Norse muna .
== b79a8e42576ea2ce
39: Etymology 
40- 1.2 
41- Pronunciation 
42- 1.3 
--
50: Etymology 
51- 2.2 
52- Pronunciation 
53- 2.3 
--
141: From Wiktionary, the free dictionary
142- Bukhari
144: Etymology
146: Etymology tree
147- Arabic يَمَنَ ( yamana ) der. 
148- Arabic مَيْمُون ( maymūn ) bor. 
149- Classical Persian مَیْمُون ( maymūn ) 
--
152: Inherited from Tajik маймун ( maymun ) .
153- Pronunciation
== 11e5553655e4317d
41: Etymology 
42- 1.3 
43- Pronunciation 
44- 1.4 
--
173: From Wiktionary, the free dictionary
174- See also: Monkey 
175- English
--
184: Etymology
186- Uncertain: 
187: May be derived from monk +‎ -ey ( diminutive suffix ) ,
188: or borrowed from Middle Low German Moneke , the name of the son of Martin the Ape in Reynard the Fox (which may represent an unattested colloquial Middle Low German *moneke , *moneken ), itself of uncertain origin:
189: Possibly derived from a Romance term represented by Late Middle French monne ( whence Modern French mone ( “ monkey ” ) ) or earlier Old French monnekin ( “ monkey ” ) , originally Monnekin , the name of a monkey in Li Dis d'Entendement . Compare also Old French and Middle French monin ( “ monkey ” ) .
190: The French terms may have been borrowed from Italian monna ( “ monkey ” ) , from Old Spanish mona ( “ female monkey ” ) , itself a shortening of mamona , variant of maimón , from Arabic مَيْمُون ( maymūn , “ baboon ” ) ).
191- However, Old French monnekin may alternatively be unrelated to the other terms, instead being a borrowing of Early Middle Dutch mannekin ( a diminutive of man , literally “ little human ” ) , and if so monkey is a doublet of mannequin ; see modern Dutch manneken .
192- Pronunciation
--
203: He had been visiting an area zoo when a monkey swung from its tree perch, swiped his glasses and hurled them into a hippo hole. 
204: 2007 September 20, Eric Wilson, “Blame It on Rio and Gisele”, in The New York Times ‎ [1] , archived from the original on 18 September 2020 : They thought of, I don’t know, monkeys and caipirinhas and samba.”
```


## [2026-10-17T00:31:50.459Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' a0139a2332039239.txt | sed -n 120,175p; grep -v '^\\s*$' 4475c3ac63d36ab2.txt | sed -n 146,182p"
}
```


### [2026-10-17T00:31:50.846Z] TOOL RESULT

```
 Borrowed from Arabic مَيْمُون ( maymūn , “ baboon, mandrill ” ) .
 Noun
 [ edit ] 
 میمون • ( meymûn or maymun ) ( definite accusative میمونی ( meymûnu, maymunu ) , plural میمونلر ( meymûnlar, maymunlar ) ) 
 monkey , ape , primate , any mammal in the order Primates except hominids 
 Synonyms: شادی ( şadi ) , قرد ( kird ) 
 ( figuratively ) buffoon , clown , fool , one who acts in a silly or ridiculous fashion
 Adjective
 [ edit ] 
 میمون • ( meymûn or maymun ) 
 lucky , fortunate , auspicious , favourable , propitious , of good omen , indicating future success 
 Synonyms: اوغورلو ( uğurlu ) , بختلی ( bahtlı ) , قوتلو ( kutlu ) 
 Derived terms
 [ edit ] 
 بزكلو میمون ( bezekli maymun , “ ridiculous appearance ” ) 
 ترس میمون ( ters maymun , “ variety of Damascus steel ” ) 
 حبش میمونی ( habeş maymunu , “ baboon ” ) 
 میمون اشتهالو ( maymun iştahlı , “ capriciously fanciful, temperamental ” ) 
 میمون اویونی ( maymun oyunu , “ hoax, con ” ) 
 میمون بالغی ( maymun balığı , “ angel shark ” ) 
 میمون كبی ( maymun gibi , “ ridiculous ” ) 
 میمون یوزلو ( maymun yüzlü , “ grimacing ” ) 
 میمونجق ( maymuncuk , “ picklock ” ) 
 میمونجی ( maymuncu , “ monkey man ” ) 
 میمونلق ( maymunluk , “ quality or nature of a monkey ” ) 
 هند میمونی ( hind maymunu , “ sapajou ” ) 
 Descendants
 [ edit ] 
 Turkish: maymun 
 → Albanian: majmun 
 → Armenian: մեյմուն ( meymun ) 
 → Bulgarian: майму́н ( majmún ) 
 → Georgian: მაიმუნი ( maimuni ) 
 → Greek: μαϊμού ( maïmoú ) 
 → Hungarian: majom → Romanian: moimă 
 → Ladino: maymona 
 → Macedonian: мајмун ( majmun ) 
 → Romanian: maimuță 
 → Serbo-Croatian: 
 Cyrillic script: ма̀јмун 
 Latin script: màjmun 
 Further reading
 [ edit ] 
 click to expand
 Barbier de Meynard, Charles ( 1886 ), “ میمون ”, in Dictionnaire turc-français , volume II, Paris: E. Leroux, page 807 
 Çağbayır, Yaşar ( 2007 ), “ maymun ”, in Ötüken Türkçe Sözlük (in Turkish), volume 3, Istanbul: Ötüken Neşriyat, page 3088 
 Hindoglu, Artin ( 1838 ), “ میمون ”, in Hazine-i lûgat ou dictionnaire abrégé turc-français ‎ [1] , Vienna: F. Beck, page 472b 
 Kélékian, Diran ( 1911 ), “ میمون ”, in Dictionnaire turc-français ‎ [2] (in French), Constantinople: Mihran, page 1257 
 Meninski, Franciszek à Mesgnien ( 1687 ), “Simia”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simul idem index verborum lexici turcico-arabico-persici, quod latinâ, germanicâ, aliarumque linguarum adjectâ nomenclatione nuper in lucem editum ‎ [3] , Vienna, column 1556 
 Meninski, Franciszek à Mesgnien ( 1680 ), “ میمون ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [4] , Vienna, column 5079 
 Nişanyan, Sevan ( 2002– ), “ maymun ”, in Nişanyan Sözlük 
 Redhouse, James W. ( 1890 ), “ میمون ”, in A Turkish and English Lexicon ‎ [5] , Constantinople: A. H. Boyajian, page 2056 
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: میمون 
 Wikipedia fa 
 From Wiktionary, the free dictionary
 See also: Monna 
 Italian
 [ edit ] 
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ˈmɔn.na/ 
 Rhymes: -ɔnna 
 Hyphenation: mòn‧na 
 Noun
 [ edit ] 
 monna   f ( plural monne ) 
 ( literary , archaic ) a courtesy title for a woman. abbreviation of madonna 
 Derived terms
 [ edit ] 
 Monna Lisa 
 Anagrams
 [ edit ] 
 Manno 
 Northern Sotho
 [ edit ] 
 Noun
 [ edit ] 
 monna 
 man ( human male ) 
 Norwegian Bokmål
 [ edit ] 
 Verb
 [ edit ] 
 monna 
 past tense of monne 
 supine of monne 
 Norwegian Nynorsk
 [ edit ] 
 Alternative forms
 [ edit ] 
 monne ( e-infinitive )
```


## [2026-10-17T00:31:56.401Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -v '^\\s*$' data/verification/sources/web/a0139a2332039239.txt | sed -n 175,200p; for u in \"https://en.wiktionary.org/wiki/Yemen\" \"https://en.wiktionary.org/wiki/Benjamin\" \"https://en.wiktionary.org/wiki/%D9%8A%D9%85%D9%8A%D9%86\" \"https://en.wiktionary.org/wiki/%D9%8A%D9%85%D9%86\" \"https://en.wiktionary.org/wiki/%D7%99%D7%9E%D7%99%D7%9F\" \"https://en.wiktionary.org/wiki/Moneke\" \"https://en.wiktionary.org/wiki/mono\"; do python3 tools/fetch_source.py \"$u\" --note \"page 567, root Y.m.n\"; done; tail -7 data/verification/sources/web/index.jsonl | cut -c1-200"
}
```


### [2026-10-17T00:32:05.219Z] TOOL RESULT

```
 Wikipedia fa 
 Etymology
 [ edit ] 
 Etymology tree
 Arabic يَمَنَ ( yamana ) der. 
 Arabic مَيْمُون ( maymūn ) bor. 
 Persian میمون 
 Borrowed from Arabic مَيْمُون ( maymūn ) , from يَمَنَ ( yamana ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /maj.ˈmuːn/ 
 ( Dari, formal ) IPA ( key ) : [mäj.muːn] 
 ( Dari, formal ) IPA ( key ) : [mäj.muːn] 
 ( Kabuli ) IPA ( key ) : [mäj.muːn] 
 ( Hazaragi ) IPA ( key ) : [mäj.mun] 
 ( Iran, formal ) IPA ( key ) : [mej.muːn] 
 ( Tajik, formal ) IPA ( key ) : [mäj.mun] 
 Rhymes: -uːn 
 Readings
 Classical reading ? 
 maymūn
 Dari reading ? 
 maymūn
 Iranian reading ? 
 meymun
 Tajik reading ? 
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2d3476a6a5cc00cc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e07c5cf70d002452.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1e5696617e25649a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a3754e8035e9c6dc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2b139ea483a16778.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b6e72e9f1e9ad09c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a88a4cece1ec944d.txt
{"url": "https://en.wiktionary.org/wiki/%D9%8A%D9%85%D9%86", "file": "data/verification/sources/web/a3754e8035e9c6dc.txt", "fetched": "2026-10-17T00:32:03Z", "status": 200, "bytes": 4339, "title": "يم
{"url": "https://en.wiktionary.org/wiki/جوشیدن", "file": "data/verification/sources/web/0f0ab8afe554d970.txt", "fetched": "2026-10-17T00:32:03Z", "status": 200, "bytes": 12992, "title": "جوشیدن - Wikt
{"url": "https://en.wiktionary.org/wiki/%D7%99%D7%9E%D7%99%D7%9F", "file": "data/verification/sources/web/2b139ea483a16778.txt", "fetched": "2026-10-17T00:32:04Z", "status": 200, "bytes": 5086, "title
{"url": "https://en.wiktionary.org/wiki/جوش", "file": "data/verification/sources/web/c3a97d203943c9ed.txt", "fetched": "2026-10-17T00:32:04Z", "status": 200, "bytes": 5485, "title": "جوش - Wiktionary,
{"url": "https://en.wiktionary.org/wiki/Moneke", "file": "data/verification/sources/web/b6e72e9f1e9ad09c.txt", "fetched": "2026-10-17T00:32:04Z", "status": -1, "bytes": 39, "title": "", "note": "page 
{"url": "https://en.wiktionary.org/wiki/یوز", "file": "data/verification/sources/web/d3cc5d47abcfbc4d.txt", "fetched": "2026-10-17T00:32:04Z", "status": 200, "bytes": 20779, "title": "یوز - Wiktionary
{"url": "https://en.wiktionary.org/wiki/mono", "file": "data/verification/sources/web/a88a4cece1ec944d.txt", "fetched": "2026-10-17T00:32:05Z", "status": 200, "bytes": 30863, "title": "mono - Wiktiona
```


## [2026-10-17T00:32:09.026Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -c . 2d3476a6a5cc00cc.txt e07c5cf70d002452.txt 1e5696617e25649a.txt; for f in 2d3476a6a5cc00cc e07c5cf70d002452 1e5696617e25649a a3754e8035e9c6dc 2b139ea483a16778; do echo \"== $f\"; grep -v '^\\s*$' $f.txt | grep -n -i -A2 '^ *\\(From\\|Borrowed\\|Derived\\|Etymology tree\\|Root\\)' | head -14; done; grep -v '^\\s*$' a88a4cece1ec944d.txt | grep -n -i -B1 -A3 'maim\\|maymūn\\|Arabic' | head -30"
}
```


### [2026-10-17T00:32:09.510Z] TOOL RESULT

```
1e5696617e25649a.txt:457
e07c5cf70d002452.txt:1139
2d3476a6a5cc00cc.txt:1120
== 2d3476a6a5cc00cc
49: Derived terms 
50- 1.4.3 
51- Translations 
--
105: Derived terms 
106- 8 
107- Norwegian 
--
128: Derived terms 
129- 10.2.3 
130- See also 
--
154: Derived terms 
155- 12.4 
== e07c5cf70d002452
45: Derived terms 
46- 1.3.2 
47- Translations 
--
228: From Wiktionary, the free dictionary
229- See also: benjamin , benjamín , Benjamín , Benjámin , and Benjamîn 
230- English
--
236: From Late Latin Benjamin , from Ancient Greek Βενιαμίν ( Beniamín ) , from Biblical Hebrew בִּנְיָמִין ( binyamīn , literally “ son of the right/south or son of days ” ) . Authorities differ on the meaning of the original Hebrew. Philo of Alexandria, the Samaritan Pentateuch The Testament of the Twelve Patriarchs and Midrash Leḳaḥ-Ṭob understand יָמִין to mean "days" (a meaning attested in Daniel 12:13 ) understanding the name to mean "son of days (i.e. old age)" (compare to the direct translations into Arabic بِنْ يَومِين ( bin yawmīn ) "son of the days" and Arabic بِنْ يَمِين ( bin yamīn ) "son of the right hand"), a formula paraphrased in Genesis 40:22 where Benjamin is described as a child of Jacob's old age. Rashi in his commentary on Genesis also gives this as a possible meaning but favors an understanding of יָמִין to mean "right" in the sense of "the south", noting that Benjamin was the only son of Jacob born in the south. Jerome understood the name to mean "son of the right hand" and Gesenius speculated that this expression might have meant "son of good fortune".
237- Pronunciation
238- [ edit ] 
--
259: Derived terms
260- [ edit ] 
== 1e5696617e25649a
47: Derived terms 
48- 1.1.2.3 
49- Descendants 
--
115: From Wiktionary, the free dictionary
116- See also: یمین 
117- Arabic
--
121: Etymology tree
122- Proto-Afroasiatic *yamin- 
123- Proto-Semitic *yamīn- 
--
243: Derived terms
244- [ edit ] 
== a3754e8035e9c6dc
103: From Wiktionary, the free dictionary
104- See also: یمن 
105- Arabic
== 2b139ea483a16778
47: Derived terms 
48- 1.4 
49- Proper noun 
--
98: From Wiktionary, the free dictionary
99- Hebrew
100- [ edit ] 
--
103: Root 
104- י־מ־ן ( y-m-n ) 
105- 8 terms 
106: From Proto-Semitic *yamīn- , from Proto-Afroasiatic *yamin- .
107- Pronunciation
108- [ edit ] 
1229- Etymology tree
1230: Arabic يَمَنَ ( yamana ) der. 
1231: Arabic مَيْمُون ( maymūn ) bor. 
1232: Spanish maimón 
1233: Spanish maimona clip. ? 
1234- Spanish mona bf. 
1235- Spanish mono bor. 
1236- Galician mono 
--
1321- Etymology tree
1322: Arabic يَمَنَ ( yamana ) der. 
1323: Arabic مَيْمُون ( maymūn ) bor. 
1324: Spanish maimón 
1325: Spanish maimona clip. ? 
1326- Spanish mona bf. 
1327- Spanish mono 
1328: Back-formation from mona , possibly clipping of maimona , female equivalent of maimón , borrowed from Arabic مَيْمُون ( maymūn , “ baboon, mandrill ” ) .
1329- Pronunciation
1330- [ edit ] 
1331- IPA ( key ) : /ˈmono/ [ˈmo.no] 
--
1338- monkey 
1339: Synonyms: chango , maimón , mico , simio , ( Louisiana ) macaco 
1340- ( informal ) any monkey -looking animal
1341- boiler suit , coveralls , overall , onesie ( a one-piece suit combining trousers and jacket, worn for heavy or hot manual labour ) 
1342- Synonyms: mono de trabajo , mameluco , braga , buzo , overol 
--
1480- Galician adjectives 
1481: Galician terms derived from Arabic 
1482- Galician terms derived from Spanish
```


## [2026-10-17T00:32:12.817Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' 2d3476a6a5cc00cc.txt | grep -n -i 'Arabic\\|from ' | head -8; grep -v '^\\s*$' a3754e8035e9c6dc.txt | sed -n 103,140p | head -30; grep -v '^\\s*$' 1e5696617e25649a.txt | sed -n 120,140p"
}
```


### [2026-10-17T00:32:13.152Z] TOOL RESULT

```
244: From Wiktionary, the free dictionary
254: Yaman ( directly from Arabic , rare ) 
258: Arabic اَلْيَمَن ( al-yaman ) bor. 
261: Borrowed from Ottoman Turkish یمن ( yemen ) , from Arabic اَلْيَمَن ( al-yaman ) , from Proto-Semitic *yamīn- ( “ right; right hand ” ) .
298: Arabic: الْيَمَن   (ar)   m or f ( al-yaman ) ( definite ) 
494: Borrowed from English Yemen , from Ottoman Turkish یمن ( yemen ) , from Arabic اَلْيَمَن ( al-yaman ) .
563: Arabic
704: Borrowed from Spanish Yemen ( “ Yemen ” ) .
 From Wiktionary, the free dictionary
 See also: یمن 
 Arabic
 [ edit ] 
 Etymology 1
 [ edit ] 
 Proper noun
 [ edit ] 
 يَمَن • ( yaman )  m 
 only used in اليَمَن ( al-yaman , “ Yemen ” ) 
 Etymology 2
 [ edit ] 
 See the etymology of the corresponding lemma form.
 Verb
 [ edit ] 
 يمن ( form I ) 
 يَمُنُّ ( yamunnu ) /ja.mun.nu/ : third-person masculine singular non-past active indicative of مَنَّ ( manna ) 
 يُمَنُّ ( yumannu ) /ju.man.nu/ : third-person masculine singular non-past passive indicative of مَنَّ ( manna ) 
 يَمُنَّ ( yamunna ) /ja.mun.na/ : third-person masculine singular non-past active subjunctive / jussive of مَنَّ ( manna ) 
 يُمَنَّ ( yumanna ) /ju.man.na/ : third-person masculine singular non-past passive subjunctive / jussive of مَنَّ ( manna ) 
 يَمُنِّ ( yamunni ) /ja.mun.ni/ : third-person masculine singular non-past active jussive of مَنَّ ( manna ) 
 يُمَنِّ ( yumanni ) /ju.man.ni/ : third-person masculine singular non-past passive jussive of مَنَّ ( manna ) 
 Etymology 3
 [ edit ] 
 See the etymology of the corresponding lemma form.
 Verb
 [ edit ] 
 يُمْنِ • ( yumni ) ( form IV ) /jum.ni/ 
 third-person masculine singular non-past active jussive of أَمْنَى ( ʔamnā ) 
 Etymology 4
 [ edit ] 
 Etymology tree
 Proto-Afroasiatic *yamin- 
 Proto-Semitic *yamīn- 
 Arabic يمين 
 Inherited from Proto-Semitic *yamīn- ( “ right ” ) , from Proto-Afroasiatic *yamin- ( “ right ” ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ja.miːn/ 
 Audio : ( file ) 
 Noun
 [ edit ] 
 يَمِين • ( yamīn )  m or f ( plural أَيْمُن ( ʔaymun ) or يَمَائِن ( yamāʔin ) or أَيْمَان ( ʔaymān ) ) 
 right , right side ( opposed to left ) 
 Antonyms: يَسَار ( yasār ) , شِمَال ( šimāl ) 
 ثُمَّ ٱنْعَطِفْ يَمِينًا . ― ṯumma nʕaṭif yamīnan . ― Then, turn right . 
 right hand 
 Antonym: شِمَال ( šimāl ) 
 609–632 CE , Qur'an , 20:17 : وَمَا تِلْكَ بِ يَمِينِ كَ يَا مُوسَى wa-mā tilka bi- yamīni ka yā mūsā And what is that in your right hand , O Moses? 
 oath 
 Power
```


## [2026-10-17T00:32:18.310Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/بنیامین/\" --note \"page 567, Y.m.n, Benyamin in Mo'in a'lam\"; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/میمون/\" --note \"page 567, Y.m.n, meymun\"; tail -2 data/verification/sources/web/index.jsonl | cut -c1-200; grep -n 'میمون' data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt | head -5"
}
```


### [2026-10-17T00:32:21.413Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e72fa1c975a59d1c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/67e7889179aba714.txt
{"url": "https://abadis.ir/fatofa/بنیامین/", "file": "data/verification/sources/web/e72fa1c975a59d1c.txt", "fetched": "2026-10-17T00:32:20Z", "status": 200, "bytes": 20153, "title": "بنیامین - معنی در
{"url": "https://abadis.ir/fatofa/میمون/", "file": "data/verification/sources/web/67e7889179aba714.txt", "fetched": "2026-10-17T00:32:21Z", "status": 200, "bytes": 12969, "title": "میمون - معنی در دیک
6111:راگون د که میمون باشد .۰ بز رکه است ‎٩‏ .
6610:آوتان ) ومیمولهای دم‌دار(میمونهای فارة‌قدیم ومیمونپای ۸ ی زنل وه 0
6613:المشهور عندالمامة آلمیمون. » « عقار ۳۱۳ . ار : نس
6615:طبری 838 مازندرانی کنونی 18 « واژه نامه شهمپانزه ( از اقام میمون )
15046:وقت زور - بکر بای فرعت , | وقلادة سگان (۱) ازطلاکنند و بوزینه ومیمون
```


## [2026-10-17T00:32:25.338Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n 'معین\\|عبری\\|یعقوب\\|بوزینه\\|\\[ع' e72fa1c975a59d1c.txt | head -12; grep -n 'معین\\|بوزینه\\|\\[ع\\|فرخنده' 67e7889179aba714.txt | head -12"
}
```


### [2026-10-17T00:32:25.703Z] TOOL RESULT

```
19: اسم: بنیامین (پسر) (عبری) (مذهبی و قرآنی) (تلفظ: benyāmin) (فارسی: بِنيامين) (انگلیسی: benyamin) 
20: معنی: پسر دست راست من، آخرین پسر حضرت یعقوب ( ع ) و برادر تنی حضرت یوسف ( ع )، یعنی پسر دست راستِ من، ( اَعلام ) آخرین پسر حضرت یعقوب ( ع ) و برادر تنی حضرت یوسف ( ع ) که پدرش ( حضرت یعقوب ) وی را بنیامین نامید، [درباره وجه تسمیه ی بنیامین آمده است که مادرش، راحیل همسر محبوب یعقوب، به هنگام تولد وی درد و رنج بسیار متحمل شد، از اینرو فرزندش را «بن اونی» نامید که در عبری «پسر رنج من» معنا می دهد ( البته معنای «پسر توانمندی من» نیز برای آن ذکر کرده اند )، گفته اند که راحیل، اندکی پس از ولادت فرزندش بر اثر سختی هایی که تحمل کرده بود، در گذشت، اما پدرش وی را «بن یامین» به معنای تحت اللفظیِ «پسر دستِ راست» نام نهاد، که بر پیروزی او در آینده نیز اِ شعار داشت، «بن یامین» را به معنای «پسر جنوب» نیز گفته اند، زیرا او تنها پسر یعقوب بود که در جنوب یعنی کنعان زاده شد، همچنین نام او را «بن یمیم» گفته اند، یعنی فرزند روزگاران، چون تولد او در سن پیری یعقوب بود، ( نقل مطالب از دانشنامه ی جهان اسلام ص ]، نام پسر حضرت یعقوب و برادر حضرت یوسف، پسر دست راست
21: برچسب ها: اسم ، اسم با ب ، اسم پسر ، اسم عبری ، اسم مذهبی و قرآنی 
25: بنیامین. [ ب ِ ] ( اِخ ) نام پسر یعقوب علیه السلام که برادر حقیقی یوسف علیه السلام بود و ابن یامین غلط است. ( آنندراج ) ( غیاث ). در عبری بمعنی پسر دست راست ، کوچکترین پسر یعقوب و راحیل جد یکی از قبایل دوازده گانه بنی اسرائیل. این قبیله در شمال فلسطین سکنی داشتند و مردمانش تیراندازان ماهری بودند. ( از دایرة المعارف فارسی ). و رجوع به قاموس کتاب مقدس شود. 
29: ۱ - آخرین پسر یعقوب ع و راشل . یعقوب به این فرزند که تولدش موجب مرگ مادرش شده بود - علاقه ای خاص داشت . توضیح در کتب لغت آمده که بنیامین بر وزن اسرافیل صحیح است نه ابن یامین ( قاموس ) ولی ابن یامین هم مستعمل است . ۲ - نام یکی از دوازده قبیله اسرائیل ( تورات ) .
30:نام پسر یعقوب علیه السلام که برادر حقیقی یوسف علیه السلام بود و ابن یامین غلط است ٠ در عبری بمعنی پسر دست راست کوچکترین پسر یعقوب و راحیل جد یکی از قبایل دوازده گان. بنی اسرائیل ٠ این قبیله در شمال فلسطین سکنی داشتند مردمانش تیراندازان ماهری بودند ٠ 
34: [ویکی فقه] بِنْیامین، کوچک ترین پسر یعقوب و تنها برادر تنی یوسف می باشد.
35:نام وی در قرآن نیامده، اما از زبان یوسف با عنوان برادرم (اخی) از دیگر برادران متمایز شده است. در داستانِ سفر برادران یوسف به مصر و بازشناختن یوسف که در نهایت سبب کوچ یعقوب و خانواده اش از کنعان به مصر شد چندین مرتبه، از بنیامین با همین تعبیر یاد شده است. 
39:درباره وجه تسمیه بنیامین آمده است که مادرش، راحیل همسر محبوب یعقوب، به هنگام تولد وی درد و رنج بسیار متحمل شد؛ ازین رو فرزندش را «بن اونی» نامید که در عبری «پسر رنج من» معنا می دهد (البته معنای «پسر توانمندی من» نیز برای آن ذکر کرده اند).گفته اند که راحیل، اندکی پس از ولادت فرزندش بر اثر سختی هایی که تحمل کرده بود، درگذشت. اما پدرش وی را «بن یامین»، به معنای تحت اللفظیِ «پسر دست راست» نام نهاد، که بر پیروزی او در آینده نیز اِشعار داشت.«بن یامین» را به معنای «پسر جنوب» نیز گفته اند، زیرا او تنها پسر یعقوب بود که در جنوب یعنی کنعان زاده شد.همچنین نام او را «بن یمیم» گفته اند، یعنی فرزند روزگاران؛ چون تولد او در سن پیری یعقوب بود؛ 
43: [ویکی شیعه] بِنْیامین، کوچکترین پسر یعقوب و تنها برادر تنی حضرت یوسف. نام بنیامین در قرآن نیامده، اما از زبان یوسف با عنوان برادرم (اخی)در سوره یوسف از دیگر برادران متمایز شده است. در عهد عتیق، در چندین باب، از بنیامین و سبط وی، به عنوان یکی از قبایل دوازده گانه بنی اسرائیل سخن گفته شده است.
45:درباره دلیل نامگذاری بنیامین آمده است که مادرش، راحیل همسر محبوب یعقوب، به هنگام تولد وی درد و رنج بسیاری کشید. ازینرو فرزندش را «بن اونی» نامید که در عبری «پسر رنج من» معنا می دهد. گفته شده که راحیل، اندکی پس از ولادت فرزندش بر اثر سختی هایی که تحمل کرده بود، درگذشت. اما پدرش وی را «بن یامین»، به معنای تحت اللفظی «پسر دست راست» نام نهاد که بر پیروزی او در آینده هم اِشعار داشت. «بن یامین» را به معنای «پسر جنوب» هم گفته اند، زیرا او تنها پسر یعقوب بود که در جنوب یعنی کنعان زاده شد. همچنین نام او را «بن یمیم» گفته اند، یعنی فرزند روزگاران؛ چون تولد او در سن پیری یعقوب بود.در آثار اسلامی، نام وی به صورت «ابن یامین» نوشته شده که احتمالاً نادرست است. امروزه نام بنیامین در بسیاری از زبان های اروپایی رواج دارد. wikishia: بنیامین 
48:بِنْیامین، کوچکترین پسر یعقوب و تنها برادر تنی یوسف. نام وی در قرآن نیامده اما از زبان یوسف با عنوان برادرم (اخی) از دیگر برادران متمایز شده است.(سوره یوسف: 90)
13: مترادف میمون : باشگون، خجسته، خجسته پی، خوش شگون، خوش قدم، سعد، فرخ، فرخنده، مبارک، مبارک پی، مسعود، نیک پی، همایون ، بوزینه، حمدونه، چز
22: میمون. [ م َ مو ] ( ع ص ) مبارک. ( منتهی الارب ) ( ناظم الاطباء ).ج ، میامین. دارای یمن و برکت. ( از اقرب الموارد ) ( آنندراج ) ( برهان ). بایمن. ( فرهنگ نظام ). خجسته. ( مهذب الاسماء ) ( دهار ) ( غیاث ). همایون. ( اوبهی ). فرخنده. خجسته. ( ناظم الاطباء ). خوش شگون. ( فرهنگ نظام ). مسعود. فرخ. بامیمنت. بایمن. خنشان. همایون. خرم. باشگون. مقابل مشؤوم : 
57: ( صفت ) خجسته فرخنده باشگون : سایه طایرکم حوصله کاری نکند طلب از سایه میمون همایی بکنیم . ( حافظ )
60: فرهنگ معین
62: (مِ ) [ ع . ] (اِمف . ) فرخنده ، خجسته . ج . میامن .
63: ( ~. ) (اِ. ) بوزینه . 
68:پستانداری پشمالو و شبیه انسان، با دست های بلند که معمولاً روی درختان زندگی می کند، بوزینه، بوزنه، بوزنینه، پوزینه، حمدونه، پهنانه، مهنانه، چز، کپی. 
77: [ویکی فقه] میمون (ابهام زدایی). واژه میمون ممکن است در معانی ذیل به کار رفته و یا اشاره به اشخاص و شخصیت های ذیل باشد: معانی• میمون، بوزینه، اسمی کلی برای میمون دارای چابکی فوق العاده و هوشمندی و زرنگی شگفت انگیز• چاه میمون، یکی از چاه های عربستان و دارای کاربرد فقهی در باب حج اعلام و اشخاص• میمون بن قیس، با تخلص ابوبصیر، از مشهورترین شاعران طبقه اول در جاهلیت و یکی از اصحاب معلقات نه گانه• میمون بن مهران، میمون بن مهران، رقی جزری، کنیه اش ابوایوب، از والیان بنی امیه و والی جزیره
82: میمون یا بوزینه و به فارسی افغانستان شادی، نامی عمومی برای اشاره به گونه ها یا گروه هایی از پستانداران راستهٔ نخستی سانان است. میمون مانندهای نخستی در آمریکای جنوبی در گذار نود میلیون سال به ردهٔ پَخ بینیان ( مارموست ها، میمون های عنکبوتی ) تکامل و فرگشت یافته اند. میمون های جهان قدیم مسیر متفاوت و پرثمرتری را پیموده اند که نخستین گام آن پیدایش ردهٔ راست بینیان از جمله ماکاک ها و بابون ها بود. 
112: بوزینه ,مبارک 
119: میمون، بوزینه
121: میمون، بوزینه
```


## [2026-10-17T00:32:38.103Z] TOOL CALL #24: Bash

```json
{
 "command": "command ls /home/sfmqrb/git/rishe-private/site/pages/567.jpg && echo ok"
}
```


### [2026-10-17T00:32:38.682Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/site/pages/567.jpg
ok
```


## [2026-10-17T00:32:41.261Z] TOOL CALL #25: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/567.jpg"
}
```


### [2026-10-17T00:32:41.291Z] TOOL RESULT

```

```


## [2026-10-17T00:32:56.942Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'maim[uü]n\\|meim[uü]n' HRN.txt HUB.txt | head -3; grep -n -B2 -A6 'Moneke\\|MLG\\. Moneke\\|Mon.ke' WEB_vol1.txt FSD_vol3.txt | head -30; grep -n -i 'Yemen\\|Benjamin' SKT.txt | head"
}
```


### [2026-10-17T00:32:57.323Z] TOOL RESULT

```
23808:gum  benjamin;*  Cotgrave  — Span.  ^m/W. I  The  Span,  /a  benjui  seems  tu  have   been
```


## [2026-10-17T00:33:04.098Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 49330,49336p FSD_vol3.txt; grep -n \"mon'key\\|mon'kl\\|mun'ki, n\" FSD_vol3.txt | head -5; grep -n -i \"Benjamin\\b\" FSD_vol1.txt | head -3; grep -n -i 'yamin\\|yaman\\|maym\\|maim' incoming/TTS/TTS_pages.txt AFM_pages.txt 2>/dev/null | head -5; grep -n 'ميمون\\|يمين' AFM_pages.txt PLA*.txt 2>/dev/null | head -3"
}
```


### [2026-10-17T00:33:04.641Z] TOOL RESULT

```
graspliig bolt, A
slight yard with ^ ^
which to exercise or train boys on shipboard — silky m.,
same os makikina - stump -tailed m., an Asiatic rer-
coplthccld, the short-tailed macaque {Macacua arctoideH).
— sykes's m.. an African corcoplthecld {Cereopithecua tUbo-
guluris),— to have or get one's m. up [Blang], to be or
49175:mon'key, 1 1 mun'ln. 2mdo'ky. e 1. ( fRare 1 To Imitate
49237:related spiTius - mon'key*lNNf*, n A small bag for cnii-
49271:mon'key •Howler, n A ny one of v artous flgworu of the genuA
49339:mon'key-fy, 1 mun'ki-fal. 2 mdo'kv-fV, pi 1-kied. -pt'ino ]
345:♦Marcus  Benjamin,  Ph.D.,  IX.D.,  F.C.S.,
2221:G.  B   G.  L.  Benjamin
3376:G.  B   G.  L.  Benjamin
(eval):1: no matches found: PLA*.txt
```


## [2026-10-17T00:33:08.625Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 49150,49176p FSD_vol3.txt | grep -n -i -B3 -A3 'mon.key\\|\\[' | head -30"
}
```


### [2026-10-17T00:33:08.977Z] TOOL RESULT

```
23-In Hampton Roads. March U. 1862, as presented in re-
24-lief on the pedestal of the monument to John Erics-
25-son. in New York city
26:mon'key, 1 1 mun'ln. 2mdo'ky. e 1. ( fRare 1 To Imitate
27-iiiun'ke) ) like a monkey, ape II. i {Colinq ] To act In n
```


## [2026-10-17T00:33:14.459Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK; pdftoppm -f 567 -l 567 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/567 && command ls -la data/verification/sources/refs/ocr/BOOK/567.png; python3 -c \"\nimport json;d=json.load(open('data/verification/page-558.json'));print(d['verified_by'], d['verified_on'])\""
}
```


### [2026-10-17T00:33:15.426Z] TOOL RESULT

```
-rw-r--r-- 1 sfmqrb sfmqrb 44792 Oct 16 20:33 data/verification/sources/refs/ocr/BOOK/567.png
claude-opus-5.5 2026-10-16
```


## [2026-10-17T00:33:24.234Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' b79a8e42576ea2ce.txt | grep -n -A4 '^ *Turkish *$' | head -12; grep -v '^\\s*$' 3c0655dc11837ef0.txt | grep -n -B3 -A3 'mamona\\|maimón\\|Spanish mona' | head -20"
}
```


## [2026-10-17T00:33:25.460Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' b79a8e42576ea2ce.txt | grep -n -i 'Ottoman\\|Turkish' | head -10; grep -v '^\\s*$' 3c0655dc11837ef0.txt | grep -n -i 'Spanish\\|Arabic' | head -10"
}
```


### [2026-10-17T00:33:25.800Z] TOOL RESULT

```
47: Turkish 
48- Toggle Turkish subsection 
49- 2.1 
50- Etymology 
51- 2.2 
--
163: Turkish
164- [ edit ] 
165- Turkish Wikipedia has an article on: maymun 
166- Wikipedia tr 
167- Etymology
435- a mona monkey, Cercopithecus mona 
436- Etymology
437- [ edit ] 
438: From Spanish mona ( “ monkey ” ) .
439- Pronunciation
440- [ edit ] 
441- IPA ( key ) : /ˈmoʊnə/ 
--
471- pudding boiled in a clay pot
472- Related terms
473- [ edit ] 
474: mamonana ( “ fat ” ) 
475- Catalan
476- [ edit ] 
477- Pronunciation
--
482- Audio ( Barcelona ) : ( file ) 
483- Etymology 1
484- [ edit ] 
485: From earlier mamona , maimona , from Arabic مَيْمُون ( maymūn , “ baboon, mandrill ” ) .
```


### [2026-10-17T00:33:25.925Z] TOOL RESULT

```
47: Turkish 
48: Toggle Turkish subsection 
163: Turkish
165: Turkish Wikipedia has an article on: maymun 
172: Ottoman Turkish میمون ( maymun ) 
173: Turkish maymun 
174: Inherited from Ottoman Turkish میمون ( maymun , “ monkey ” ) , borrowed from Arabic مَيْمُون ( maymūn , “ baboon, mandrill ” ) .
472: “ maymun ”, in Turkish dictionaries , Türk Dil Kurumu 
474: Çağbayır, Yaşar ( 2007 ), “ maymun ”, in Ötüken Türkçe Sözlük (in Turkish), volume 3, Istanbul: Ötüken Neşriyat, page 3088 
485: Turkish terms derived from Arabic 
296: Spanish 
297: Toggle Spanish subsection 
432: English Bembe •  Bunama •  Catalan •  Cornish •  Esperanto •  Hawaiian •  Irish •  Italian •  Kituba •  Kongo •  Lingala •  Luba-Kasai •  Middle English •  Murui Huitoto •  Ndonga •  Old English •  Old Frisian •  Pali •  Penrhyn •  Pileni •  Portuguese •  Sinaugoro •  Sotho •  Spanish •  Tahitian •  Tajio •  Volapük •  Yola Page categories 
438: From Spanish mona ( “ monkey ” ) .
485: From earlier mamona , maimona , from Arabic مَيْمُون ( maymūn , “ baboon, mandrill ” ) .
583: Old Spanish -a 
584: Spanish -a der. 
686: From Spanish mono , of Arabic origin.
803: Shirley Burtch ( 1983 ), Diccionario Huitoto Murui (Tomo I) (Linguistica Peruana No. 20)‎ [2] (in Spanish), Yarinacocha, Peru: Instituto Lingüístico de Verano, page 179 
974: Possibly borrowed from Spanish mona .
```


## [2026-10-17T00:35:02.632Z] TOOL CALL #32: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-567.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nAR_MYMWN=W+\"%D9%85%D9%8A%D9%85%D9%88%D9%86\"\nFA_MYMWN=W+\"%D9%85%DB%8C%D9%85%D9%88%D9%86\"\nMONKEY=W+\"monkey\"; MONA=W+\"mona\"; MONNA=W+\"monna\"; MONO=W+\"mono\"; MAYMUN=W+\"maymun\"\nYEMEN=W+\"Yemen\"; BENJ=W+\"Benjamin\"\nAR_YAMIN=W+\"%D9%8A%D9%85%D9%8A%D9%86\"; AR_YMN=W+\"%D9%8A%D9%85%D9%86\"\nHE_YAMIN=W+\"%D7%99%D7%9E%D7%99%D7%9F\"; HE_BINY=W+\"%D7%91%D7%A0%D7%99%D7%9E%D7%99%D7%9F\"\nVJ_MYMWN=\"https://vajehyab.com/moein/میمون\"; VJ_YMN=\"https://vajehyab.com/moein/یمن\"\nAB_BINY=\"https://abadis.ir/fatofa/بنیامین/\"; AB_MYMWN=\"https://abadis.ir/fatofa/میمون/\"\n\nKLN164={\"ref\":\"KLN:164\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 4759 (leaf 97), s.v. 'Benjamin': 'Heb. Binyamin, lit. son of the right hand, fr. ben son, and yamin right hand ... Heb. yamin means also south ... rel. to Aram.-Syr. yammin, Ugar. ymn, Arab. yaman, right hand, right side, south, yamana he was happy, lit. he turned or went to the right (the right side was regarded as auspicious), Ethiop. yaman, Akkad. imnu ... Cp. Yemen, maimon, monkey.'\"}\nKLN997={\"ref\":\"KLN:997\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 24264 (grep '^monkey,'), s.v. 'monkey': 'MLG. Moneke(n), name of an ape, prob. fr. MIt. monnicchio, fr. OIt. monna (cp. Sp. and Port. mono, mona), ape, monkey, aphetically formed fr. Turk. maymun, of s.m., fr. Arab. maymun, auspicious, used euphemistically to denote the ape or monkey, whose sight is supposed to bring misfortune (Nöldeke, Neue Beiträge 1910, p. 89).' This is exactly Nourai's chain.\"}\nLKT={\"src\":\"LKT\",\"where\":\"no. 1365 (LKT.txt line 3166)\",\"stance\":\"partial\",\"note\":\"'Ar. maimun: Affe [eigentlich glücklich, glückbringend ... Euphemismus, da der Affe als Teufel gilt. Vgl. Nöldeke ...]; hieraus it. mammone Meerkatze, maimone, afrz. prov. maimon ... sp. pg. mono, mona, frz. maimon, mona ... bulg. majmuna, serb. majmun' — confirms Arabic maymun > Romance mono/mona and Balkan majmun; does not list English monkey or a Turkish intermediary for Italian.\"}\nSKT={\"src\":\"SKT\",\"where\":\"SKT.txt line 10879, s.v. 'monkey' (under madonna)\",\"stance\":\"partial\",\"note\":\"'monkey, an ape. (Ital.-L.) Corrupted from O. Ital. monicchio, a pugge, a munkie, an ape (Florio). Dimin. of O. Ital. mona, monna, an ape ... Monna is a familiar corruption of madonna' — Skeat derives monna from madonna, not from Arabic, and has no MLG step.\"}\n\nnodes=[]\ndef N(**k): nodes.append(k)\n\nN(id=1,lang=\"Arabic\",words=\"yamîn; Yemen; maymŭn\",verdict=\"confirmed\",\n derivation=\"Arabic yamīn 'right hand, right side; oath' continues Proto-Semitic *yamīn- (cf. Heb. yāmīn, Aram. yammīn, Ugar. ymn, Akkad. imnu); since the Semites oriented themselves facing east, the right side = south, whence al-Yaman 'the southern land' (Yemen; the form 'Yemen' is the Turkish/vulgar pronunciation of Arabic Yaman, per Klein). The right side being auspicious, the verb yamana 'to be fortunate' and its passive participle maymūn (maf'ūl pattern m-y-m-ū-n from y-m-n) 'blessed, fortunate' arose. Maymūn 'monkey' is an antiphrastic euphemism (Nöldeke 1910): the ape, whose sight was ill-omened, was called 'the lucky one'. All three words and Nourai's NOTE are confirmed.\",\n derivation_fa=\"«یمین» عربی به معنای «دست راست، سوی راست» از سامی آغازین *yamīn- است (هم‌ریشه با عبری yāmīn و اکدی imnu). چون سامیان رو به خاور می‌ایستادند، سوی راست همان جنوب بود و از این رو «الیمن» یعنی «سرزمین جنوب»؛ «Yemen» تلفظ ترکی/عامیانهٔ Yaman است. از آن‌جا که راست را خجسته می‌دانستند، فعل «یَمَنَ» (خجسته بودن) و اسم مفعول آن «مَیْمون» (خجسته) ساخته شد؛ کاربرد «میمون» برای بوزینه به گفتهٔ نولدکه و کلاین از راه به‌گویی (euphemism) است، زیرا دیدن بوزینه را بدشگون می‌پنداشتند. ادعای نورایی درست است.\",\n sources=[AR_YAMIN,AR_YMN,AR_MYMWN,YEMEN],\n ref_check=[KLN164],\n consulted=[KLN997|{\"src\":\"KLN\",\"where\":\"p. 997 s.v. monkey\"} if False else {\"src\":\"KLN\",\"where\":\"p. 997 s.v. 'monkey' (KLN_1966.txt line 24264)\",\"stance\":\"supports\",\"note\":\"'Arab. maymun is pass. part. of yamana, he was happy, he was fortunate; it was auspicious, fr. yaman, right side, south, yamin, right hand' and the euphemism for the monkey.\"},\n  LKT,\n  {\"src\":\"FVQ\",\"where\":\"grep 'yamin|yaman' in FVQ_pages.txt\",\"stance\":\"silent\",\"note\":\"no entry: y-m-n is native Arabic, not a Qur'anic foreign word (only hit is 'Benjamin's sack', line 7280).\"}])\n\nN(id=2,lang=\"Persian\",words=\"yomn; Yaman; meymŭn, maymŭn\",verdict=\"confirmed\",\n derivation=\"All three are Arabic loanwords in New Persian: yomn 'good fortune, blessing' = Arabic yumn (verbal noun of yamana); Yaman = Arabic al-Yaman 'Yemen'; meymun/maymun = Arabic maymūn, used in Persian both as the adjective 'auspicious' (Hâfez: be axtar-e meymun 'under an auspicious star') and as the noun 'monkey' (Mo'in gives both senses). Classical Persian read maymūn; modern Iranian Persian has meymun with the regular ay > ey shift. The extra forms meymanat 'auspiciousness' (Ar. maymana) and tayammon 'taking a good omen' (Ar. tayammun, form V) belong to the same Arabic root.\",\n derivation_fa=\"«یُمن»، «یَمَن» و «میمون» هر سه وام‌واژهٔ عربی‌اند: «یُمن» (خیر و برکت) مصدر «یَمَنَ»، «یمن» نام سرزمین جنوب عربستان، و «میمون» اسم مفعول همان ریشه به معنای «خجسته» که در فارسی معنای «بوزینه» را نیز گرفته است. تلفظ کلاسیک maymūn در فارسی امروز ایران با دگرگونی ay > ey به meymun بدل شده است. «میمنت» و «تیمّن» نیز از همین ریشهٔ عربی ی-م-ن‌اند. معین هر دو را با نشان [ع.] آورده و ادعای نورایی درست است.\",\n sources=[VJ_MYMWN,VJ_YMN,AB_MYMWN,FA_MYMWN],\n ref_check=[{\"ref\":\"FVA:453\",\"status\":\"not_checked\",\"note\":\"Nahvi's Farhang-e vazheha-ye Arabi: no digital copy (refs_online.json).\"}],\n consulted=[{\"src\":\"MON\",\"where\":\"vajehyab.com/moein/میمون and /یمن\",\"stance\":\"supports\",\"note\":\"میمون: '(مِ) [ع.] (اِمف.) فرخنده، خجسته. ج. میامن' and (abadis copy of Mo'in) '(~.) (اِ.) بوزینه'; یمن: '(یُ مْ) [ع.] (اِ.) خیر و برکت، خجستگی'.\"},\n  {\"src\":\"BQT\",\"where\":\"Dehkhoda via abadis.ir/fatofa/میمون/\",\"stance\":\"supports\",\"note\":\"Dehkhoda s.v. میمون cites Borhan: 'مبارک ... دارای یمن و برکت ... (برهان)'; BQT_v4_pages.txt grep 'میمون' gives no clean headword line (OCR noisy).\"},\n  {\"src\":\"HRN\",\"where\":\"grep 'maimun|meimun' HRN.txt/HUB.txt\",\"stance\":\"silent\",\"note\":\"Arabic loan, not treated by Horn or Hübschmann.\"},\n  {\"src\":\"KLN\",\"where\":\"s.v. 'maimon' (KLN_1966.txt line 22594)\",\"stance\":\"supports\",\"note\":\"'maimon, n., the mandrill. — It. maimone, fr. Pers. maymun, ape, fr. Arab. maymun, auspicious.'\"}])\n\nN(id=3,lang=\"Turkish\",words=\"maymŭn\",verdict=\"confirmed\",\n derivation=\"Turkish maymun 'monkey' < Ottoman Turkish میمون meymûn/maymun 'monkey; lucky, auspicious', a borrowing of Arabic maymūn (probably via Persian usage, where the 'monkey' sense was current). Ottoman spread the word to the Balkans (Serbo-Croatian majmun, Bulgarian majmuna, Albanian majmun, Romanian maimuță). The word and its Arabic origin are certain; its role as source of Italian monna (next node) is a separate question.\",\n derivation_fa=\"«maymun» ترکی از ترکی عثمانی «میمون» (هم «بوزینه» و هم «خجسته») است که از عربی «مَیْمون» وام گرفته شده و احتمالاً معنای «بوزینه» را از کاربرد فارسی گرفته است. ترکی عثمانی این واژه را به زبان‌های بالکان (صربی majmun، بلغاری majmuna، رومانیایی maimuță) رساند. این بخش از ادعای نورایی درست است.\",\n sources=[FA_MYMWN,MAYMUN],\n ref_check=[{\"ref\":\"KLN:164\",\"status\":\"partial\",\"note\":\"Klein p.164 (Benjamin) cross-refers to 'maimon, monkey' but names no Turkish form; the Turkish form is on p.997.\"},\n  {\"ref\":\"KLN:997\",\"status\":\"supports\",\"note\":\"s.v. monkey: 'OIt. monna ... aphetically formed fr. Turk. maymun, of s.m., fr. Arab. maymun'.\"},\n  {\"ref\":\"PRT:413\",\"status\":\"not_checked\",\"note\":\"Partridge, Origins: lending-only copy on archive.org.\"}],\n consulted=[LKT,{\"src\":\"TTS\",\"where\":\"grep 'maimun|maymun|majmun' TTS_pages.txt\",\"stance\":\"silent\",\"note\":\"no entry found in Vámbéry (word is an Arabic loan, not Turkic).\"}])\n\nN(id=4,lang=\"Italian\",words=\"monna\",verdict=\"plausible\",\n derivation=\"Old Italian monna 'ape, monkey' (Florio 1598: 'mona, monna, an ape, a munkie'; dimin. monicchio) is real. Klein (Nourai's source) derives it aphetically from Turkish maymun; modern sources (Wiktionary, Lokotsch, Corominas) instead route the Romance word through Spain: Arabic maymūn > Old Spanish maimón, fem. maimona/mamona > clipped mona 'female monkey' (back-formed mono), with Italian monna borrowed from Spanish and contaminated by monna 'lady' (< madonna). Skeat thought monna simply = monna 'madam'. The Arabic ultimate origin is widely accepted, the Turkish intermediary is not; hence plausible. Nourai's NOTE (AHD et al. derive English monkey from Moneke) concerns the next step and is correct as a report.\",\n derivation_fa=\"«monna» در ایتالیایی کهن به معنای «بوزینه» به‌راستی وجود داشته است. کلاین (منبع نورایی) آن را با حذف هجای آغازین از ترکی maymun می‌داند، اما پژوهش امروزی (ویکی‌واژه، لوکوچ) راه را از اسپانیا می‌داند: عربی مَیْمون > اسپانیایی کهن maimón، مؤنث maimona/mamona > کوتاه‌شدهٔ mona، و ایتالیایی monna از اسپانیایی، با تأثیر monna «بانو» (کوتاه‌شدهٔ madonna). خاستگاه عربی پذیرفتنی است ولی میانجی ترکی پذیرفته نیست؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n sources=[MONKEY,MONO,MONA,MONNA],\n ref_check=[KLN997,{\"ref\":\"PRT:413\",\"status\":\"not_checked\",\"note\":\"Partridge, Origins: lending-only copy on archive.org.\"}],\n consulted=[LKT,SKT])\n\nN(id=5,lang=\"Middle German\",words=\"meneke\",verdict=\"transcription_suspect\",\n error_in=\"book\",book_prints=\"meneke\",correct_form=\"Moneke (Middle Low German)\",\n derivation=\"The book prints 'meneke' under 'Middle German'; the extraction is faithful. The attested form is Middle Low German Moneke (Moneken), the name of the son of Martin the Ape in the MLG Reynke de Vos (Lübeck 1498), which Klein (Nourai's own cited p. 997) gives as 'MLG. Moneke(n), name of an ape'. 'meneke' is Nourai's misprint, and the label should be Middle Low German. Its derivation from the Romance monkey word (It. monna / OF monne, monnekin) is a hypothesis, not certain (Wiktionary: 'itself of uncertain origin'), so even with the correct form the edge is only plausible.\",\n derivation_fa=\"کتاب «meneke» و برچسب «آلمانی میانه» را چاپ کرده و استخراج درست است؛ صورت درست «Moneke» در آلمانی سفلای میانه است، نام پسر «مارتین بوزینه» در داستان «رینکه روباه» (لوبک، ۱۴۹۸)، که خود کلاین در صفحهٔ ۹۹۷ آن را «MLG. Moneke(n)» آورده است. پس «meneke» خطای چاپی کتاب است. پیوند Moneke با واژهٔ رومیایی monna نیز فرضیه است و قطعی نیست.\",\n sources=[MONKEY],\n ref_check=[{\"ref\":\"KLN:997\",\"status\":\"partial\",\"note\":\"Klein s.v. monkey: 'MLG. Moneke(n), name of an ape, prob. fr. MIt. monnicchio, fr. OIt. monna' — supports the step, but the form is Moneke, not meneke, and the language is Middle Low German.\"}],\n consulted=[SKT|{\"stance\":\"silent\",\"note\":\"Skeat (SKT.txt line 10879) derives monkey directly from O. Ital. monicchio; no MLG Moneke step.\"},\n  {\"src\":\"FSD\",\"where\":\"FSD_vol3.txt around line 49175 (mon'key)\",\"stance\":\"silent\",\"note\":\"OCR of the monkey entry is unreadable for the etymology; no 'Moneke' found by grep.\"}])\n\nN(id=6,lang=\"English\",words=\"monkey, mona\",verdict=\"plausible\",\n derivation=\"English monkey (first recorded 1520s) is of uncertain origin: the leading view (AHD, Klein, Wiktionary) takes it from MLG Moneke, the ape's name in Reynard the Fox, itself perhaps from the Romance monna/monne family going back to Arabic maymūn; an alternative derives it from monk + -ey or from Early Middle Dutch mannekin (making it a doublet of mannequin). English mona (a West African monkey, Cercopithecus mona) does NOT come through MLG Moneke: Klein and Wiktionary derive it directly from Spanish/Portuguese mona 'female monkey' (< maimona < Arabic maymūn), so it belongs under a Romance node, not under 'meneke'. Ultimate Arabic origin of both is plausible; the route drawn is correct only for monkey.\",\n derivation_fa=\"«monkey» انگلیسی (نخستین کاربرد در دههٔ ۱۵۲۰) خاستگاه روشنی ندارد: دیدگاه رایج (کلاین، فرهنگ امریکن هریتیج، ویکی‌واژه) آن را از Moneke، نام بوزینه در «رینکه روباه» به آلمانی سفلای میانه، می‌داند که شاید خود از monna رومیایی و سرانجام از عربی مَیْمون باشد؛ دیدگاه‌های دیگر آن را از monk با پسوند -ey یا از هلندی mannekin می‌دانند. اما «mona» (گونه‌ای بوزینهٔ آفریقایی) مستقیم از اسپانیایی/پرتغالی mona «بوزینهٔ ماده» آمده، نه از Moneke. پس ادعای نورایی برای monkey با احتیاط پذیرفتنی است و برای mona راهِ کشیده‌شده نادرست است.\",\n sources=[MONKEY,MONA],\n ref_check=[KLN997|{\"note\":KLN997[\"note\"]+\" Klein s.v. 'mona' (line 24226) however: 'mona, n., a small African monkey. — Sp. and Port. mona, female monkey, fem. of mono' — i.e. mona is not from MLG.\"},\n  {\"ref\":\"PRT:413\",\"status\":\"not_checked\",\"note\":\"Partridge, Origins: lending-only copy on archive.org.\"}],\n consulted=[SKT,{\"src\":\"KLN\",\"where\":\"s.v. 'mona' (KLN_1966.txt line 24226)\",\"stance\":\"partial\",\"note\":\"'Sp. and Port. mona, female monkey, fem. of mono. See monkey' — mona comes from Spanish, not via MLG Moneke.\"},\n  {\"src\":\"WEB\",\"where\":\"grep 'Moneke' WEB_vol1.txt\",\"stance\":\"silent\",\"note\":\"monkey entry not found in the OCR of vol. 1.\"}])\n\nN(id=7,lang=\"English\",words=\"Yemen\",verdict=\"confirmed\",\n derivation=\"English Yemen, the country of SW Arabia, renders Arabic al-Yaman 'the south (land)', from yaman/yamīn 'right side' (= south when facing east); the -e- vowels reflect the Ottoman Turkish pronunciation Yemen, through which Europeans knew the name (Wiktionary: borrowed from Ottoman Turkish یمن yemen < Arabic al-yaman; Klein: 'vulgar pronunciation of Arab. Yaman'). The Latin Arabia Felix 'Happy Arabia' is a calque on the 'fortunate' sense of the root.\",\n derivation_fa=\"«Yemen» انگلیسی از عربی «الیمن» به معنای «سرزمین جنوب» است (از «یمن/یمین»، سوی راست که رو به خاور همان جنوب است). واکه‌های e از تلفظ ترکی عثمانی Yemen است که اروپاییان نام را از آن راه شناختند. نام لاتین Arabia Felix «عربستان خوشبخت» گرته‌برداری از معنای «خجسته» همین ریشه است. ادعای نورایی درست است.\",\n sources=[YEMEN],\n ref_check=[{\"ref\":\"KLN:1762\",\"status\":\"supports\",\"note\":\"Page 1762 is beyond the end of the KLN_1966 OCR (ends in V); found in KLN_1971.txt line 269722: 'Yemen ... Vulgar pronunciation of Arab. Yaman, lit. the country of the South; the happy country (cp. Arabia Felix), fr. yaman, right hand, right side; south ... See Benjamin.'\"}],\n consulted=[{\"src\":\"KLN\",\"where\":\"s.v. 'dexter' (KLN_1966.txt line 11180)\",\"stance\":\"supports\",\"note\":\"'cp. Heb. yamin, right hand, south, Arab. yaman, right hand, south, yamana, he was happy (see Yemen)'.\"},\n  {\"src\":\"SKT\",\"where\":\"grep 'Yemen' SKT.txt\",\"stance\":\"silent\",\"note\":\"no entry.\"}])\n\nN(id=8,lang=\"Hebrew\",words=\"yâmîn; Ben-yâmin\",verdict=\"confirmed\",\n derivation=\"Hebrew yāmīn 'right hand, right side; south' continues Proto-Semitic *yamīn- (cognate with Arabic yamīn). Binyāmīn (Benjamin), Jacob's youngest son (Gen. 35:18), is ben 'son' + yāmīn: 'son of the right hand' (Jerome; Gesenius 'son of good fortune') or 'son of the south' (Rashi: the only son born in Canaan, south of Paddan-aram); an ancient alternative reads 'son of days' (old age). Nourai's gloss 'son of the right (fortunate) side' matches the majority view.\",\n derivation_fa=\"«یامین» عبری به معنای «دست راست، جنوب» از سامی آغازین *yamīn- و هم‌ریشه با «یمین» عربی است. «بنیامین» (Binyāmīn)، کوچک‌ترین پسر یعقوب (پیدایش ۳۵:۱۸)، از ben «پسر» و yāmīn ساخته شده، یعنی «پسر دست راست» (یا «پسر خوش‌اقبالی»)؛ برخی آن را «پسر جنوب» یا «پسر روزگاران (پیری)» معنا کرده‌اند. ادعای نورایی درست است.\",\n sources=[HE_YAMIN,HE_BINY,BENJ],\n ref_check=[KLN164],\n consulted=[{\"src\":\"FVQ\",\"where\":\"grep 'Benjamin|yamin' FVQ_pages.txt\",\"stance\":\"silent\",\"note\":\"only 'which was put in Benjamin's sack' (line 7280), in another entry; Binyamin is not a Qur'anic word.\"},\n  {\"src\":\"AFA\",\"where\":\"grep 'yamin' AFA.txt\",\"stance\":\"silent\",\"note\":\"no entry.\"}])\n\nN(id=9,lang=\"Persian\",words=\"Benyâmîn\",verdict=\"confirmed\",\n derivation=\"Persian Benyâmin بنیامین is the Biblical name received through Arabic/Islamic tradition (Ar. Binyāmīn; Islamic texts also write Ibn Yāmīn, which Ghiyas and Dehkhoda call incorrect), ultimately from Hebrew Binyāmīn 'son of the right hand'. Attested in Sanā'i's Hadiqat ol-Haqiqa (quoted on the page as 'bon yâmin'). Mo'in's a'lam (vol. 5) lists it as the last son of Jacob and Rachel.\",\n derivation_fa=\"«بنیامین» نام کتاب مقدسی است که از راه سنت عربی و اسلامی به فارسی رسیده و سرانجام از عبری Binyāmīn «پسر دست راست» است؛ صورت «ابن یامین» نیز در متون اسلامی آمده که فرهنگ‌نویسان آن را نادرست شمرده‌اند. سنایی در حدیقة الحقیقه آن را به کار برده است. معین در بخش اعلام آن را «آخرین پسر یعقوب و راشل» آورده؛ ادعای نورایی درست است.\",\n sources=[AB_BINY],\n ref_check=[{\"ref\":\"MON5\",\"status\":\"supports\",\"note\":\"Mo'in a'lam as reproduced on abadis.ir/fatofa/بنیامین/: '۱ - آخرین پسر یعقوب ع و راشل ... بنیامین بر وزن اسرافیل صحیح است نه ابن یامین (قاموس) ولی ابن یامین هم مستعمل است. ۲ - نام یکی از دوازده قبیله اسرائیل (تورات)'. No etymology given.\"}],\n consulted=[{\"src\":\"BQT\",\"where\":\"grep 'بنیامین|بن یامین' BQT_v1_pages.txt\",\"stance\":\"silent\",\"note\":\"no headword found in Borhan vol. 1.\"},\n  {\"src\":\"KLN\",\"where\":\"p.164 s.v. Benjamin\",\"stance\":\"supports\",\"note\":\"'Heb. Binyamin, lit. son of the right hand' (the source of the Persian name).\"}])\n\nN(id=10,lang=\"English\",words=\"Benjamin\",verdict=\"confirmed\",\n derivation=\"English Benjamin < Late Latin Benjamin < Septuagint Greek Beniamín < Biblical Hebrew Binyāmīn 'son of the right hand', from ben 'son' + yāmīn 'right hand, south' (Gen. 35:18). The name entered English through the Latin Bible; the sense 'favourite youngest child' comes from Jacob's love for Benjamin.\",\n derivation_fa=\"«Benjamin» انگلیسی از لاتین متأخر Benjamin، از یونانی ترجمهٔ هفتادی Beniamín و از عبری Binyāmīn «پسر دست راست» (ben «پسر» + yāmīn «دست راست، جنوب») است و از راه کتاب مقدس لاتین به انگلیسی رسیده است. ادعای نورایی درست است.\",\n sources=[BENJ,HE_BINY],\n ref_check=[KLN164],\n consulted=[{\"src\":\"SKT\",\"where\":\"grep 'Benjamin' SKT.txt (line 23808)\",\"stance\":\"silent\",\"note\":\"only 'gum benjamin' (benzoin), unrelated; no personal-name entry.\"},\n  {\"src\":\"FSD\",\"where\":\"grep 'Benjamin' FSD_vol1.txt\",\"stance\":\"silent\",\"note\":\"hits are contributor names only.\"}])\n\nentry={\"entry\":0,\"root\":\"Y.m.n\",\"verdict\":\"confirmed\",\n \"modern_form\":\"Semitic root y-m-n, Proto-Semitic *yamīn- 'right hand, right side' (> south; auspiciousness)\",\n \"note\":\"The root y-m-n 'right hand' with derived senses 'south' (facing east) and 'good fortune' (right = auspicious) is standard (Klein p.164; Wiktionary Proto-Semitic *yamīn- < Proto-Afroasiatic *yamin-). All Semitic, Persian and Biblical-name nodes are confirmed. The monkey branch follows Klein exactly; modern sources keep the Arabic maymūn origin of the Romance mona/mono words but route it through Spanish (maimón > maimona > mona), not Turkish, and treat English monkey < MLG Moneke as uncertain. The book misprints MLG Moneke as 'meneke' (and labels it 'Middle German'); English mona comes from Spanish mona, not from Moneke.\",\n \"note_fa\":\"ریشهٔ سامی ی-م-ن «دست راست» با معناهای فرعی «جنوب» (برای کسی که رو به خاور است) و «خجستگی» (چون راست را مبارک می‌دانستند) در منابع امروزی پذیرفته است (کلاین ص ۱۶۴؛ ویکی‌واژه: سامی آغازین *yamīn-). شاخه‌های عربی، فارسی (یمن، یُمن، میمون) و نام بنیامین درست‌اند. در شاخهٔ «میمون/monkey» نورایی از کلاین پیروی کرده؛ پژوهش امروزی خاستگاه عربی mona/mono را می‌پذیرد ولی راه را از اسپانیا می‌داند نه ترکیه، و پیوند monkey با Moneke را نامطمئن می‌شمارد. «meneke» خطای چاپی کتاب به جای Moneke است.\",\n \"sources\":[AR_YAMIN,HE_YAMIN,HE_BINY],\n \"ref_check\":[KLN164],\n \"consulted\":[{\"src\":\"KLN\",\"where\":\"s.v. 'dexter' (KLN_1966.txt line 11180)\",\"stance\":\"supports\",\"note\":\"'For the sense development of L. dexter ... cp. Heb. yamin, right hand, south, Arab. yaman, right hand, south, yamana, he was happy'.\"},\n   {\"src\":\"LKT\",\"where\":\"no. 1365\",\"stance\":\"supports\",\"note\":\"'Ar. maimun: Affe [eigentlich glücklich, glückbringend ... Euphemismus]' — the y-m-n 'fortunate' sense.\"}],\n \"nodes\":nodes}\nout={\"pdf_page\":567,\"book_page\":537,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[entry]}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-567.json\",\"w\"),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-567.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-567.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 567"
}
```


### [2026-10-17T00:35:03.185Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'confirmed': 7, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'not_checked': 4, 'partial': 2}
books consulted: {'supports': 6, 'partial': 6, 'silent': 12} | by book: {'KLN': 5, 'SKT': 5, 'LKT': 3, 'FVQ': 2, 'BQT': 2, 'FSD': 2, 'MON': 1, 'HRN': 1, 'TTS': 1, 'WEB': 1, 'AFA': 1}
```


## [2026-10-17T00:35:13.531Z] TOOL CALL #33: SubagentHandback

```json
{
 "message": "Page 567 (book p. 537, root Y.m.n) is verified. I wrote /home/sfmqrb/git/rishe-private/data/verification/page-567.json, and `verify_check.py 567` reports 0 PROBLEM lines with 10 of 10 nodes covered.\n\n- **Root verdict:** confirmed. Y-m-n goes back to Proto-Semitic *yamīn- \"right hand\". \"South\" comes from facing east, and \"good fortune\" from the right side counting as lucky. Klein p.164 supports this.\n- **Node verdicts:** 7 confirmed, 2 plausible, 1 transcription_suspect, 0 disputed.\n  - Confirmed: the Arabic, Persian (یمن / میمون / بنیامین), Turkish maymun and Hebrew nodes, plus English Yemen and Benjamin.\n  - Plausible: #4 Italian monna and #6 English monkey, mona.\n- **Plausible, #4 monna:** the chain follows Klein p.997 exactly. Modern sources (Wiktionary, Lokotsch no. 1365) still trace it to Arabic maymūn, but through Spanish (maimón > maimona > mona), not Turkish.\n- **Plausible, #6 monkey, mona:** English monkey from Middle Low German Moneke is itself uncertain. English mona comes straight from Spanish/Portuguese mona (Klein s.v. mona), not through Moneke. So the chart attaches it to the wrong parent.\n- **transcription_suspect, #5 \"meneke\" [Middle German]:** this is a misprint in the book, and the extraction is faithful. The attested form is Middle Low German Moneke(n), the ape's name in Reynke de Vos, which is how Nourai's own source Klein p.997 gives it. The language label should be \"Middle Low German\". I saved the page image as data/verification/sources/refs/ocr/BOOK/567.png.\n- **Extraction errors:** none. The JSON matches the printed page.\n- **Not checked:** FVA:453 (Nahvi) and PRT:413 (Partridge) have no accessible copy, so those ref checks are marked not_checked.\n- **Klein page 1762 (Yemen):** this page is missing from the 1966 OCR text, so I checked the entry in KLN_1971.txt instead."
}
```


### [2026-10-17T00:35:13.944Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
