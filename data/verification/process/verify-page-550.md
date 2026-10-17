# Verification process log — verify-page-550


## [2026-10-17T00:00:15.576Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 550 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-550.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-550.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-550.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 550` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.649Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.399Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.496Z] TOOL RESULT

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


## [2026-10-17T00:00:18.903Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-550.txt"
}
```


### [2026-10-17T00:00:19.006Z] TOOL RESULT

```
1	=== PDF page 550 (book page 520) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wes 1, Wesâ, Wâs, Wôs, Wôsos : wet, also male animal  (refs POK:1171,1172; IEC:1582)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:1172; DZA:59 | uš-tra, uštra : camel ; zara-uštra : (with) old camels ☞Ger 2
5	  #2 (parent #1) [Sogdian] refs=SOD:30,439 | `xwštr : camel
6	  #3 (parent #1) [Persian] refs=BQT:138 | oštor «اشتر ۱ (شتر)» : camel ; Zartošt «زرتشت» : "owner of old camels", Zoroaster
7	#4 (parent #0) [Avestan] refs=POK:1172 | vanhu, vohnua, vohuni : blood
8	  #5 (parent #4) [Sogdian] refs=SOD:176,437 | xwrn : blood
9	  #6 (parent #4) [Persian] refs=BRT:1434; HRN:113; SYN:206 | xŭn «خون» : blood
10	#7 (parent #0) [Persian] refs=IEC:1495,1525,1582; MON:470 | bâh «باه» : sperm, sexual drive | NOTE: MON:470 derives this word from Arabic
11	#8 (parent #0) [Sanskrit] refs=POK:1172; IEC:1582 | uštra : camel ; vasâ : liquid
12	#9 (parent #0) [Germanic] refs=AHD | wôs : juice
13	  #10 (parent #9) [English] refs=POK:1172 | ooze 1 : to leak out slowly
14	--- entry 1 ---
15	ROOT Wes 2 -> redirect to Aus 2
16	
```


## [2026-10-17T00:00:19.512Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-550.json"
}
```


### [2026-10-17T00:00:19.587Z] TOOL RESULT

```
1	{
2	  "pdf_page": 550,
3	  "book_page": 520,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wes 1, Wesâ, Wâs, Wôs, Wôsos",
8	        "lang": "Indo-European",
9	        "refs": "POK:1171,1172; IEC:1582",
10	        "gloss": "wet, also male animal"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan / Old Persian",
17	          "refs": "POK:1172; DZA:59",
18	          "words": [
19	            {"translit": "uš-tra, uštra", "gloss": "camel", "script": null},
20	            {"translit": "zara-uštra", "gloss": "(with) old camels", "script": null, "see": ["Ger 2"]}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Sogdian",
29	          "refs": "SOD:30,439",
30	          "words": [
31	            {"translit": "`xwštr", "gloss": "camel", "script": null}
32	          ],
33	          "note": null,
34	          "quote": null
35	        },
36	        {
37	          "id": 3,
38	          "parent": 1,
39	          "lang": "Persian",
40	          "refs": "BQT:138",
41	          "words": [
42	            {"translit": "oštor", "gloss": "camel", "script": "اشتر ۱ (شتر)"},
43	            {"translit": "Zartošt", "gloss": "\"owner of old camels\", Zoroaster", "script": "زرتشت"}
44	          ],
45	          "note": null,
46	          "quote": null
47	        },
48	        {
49	          "id": 4,
50	          "parent": 0,
51	          "lang": "Avestan",
52	          "refs": "POK:1172",
53	          "words": [
54	            {"translit": "vanhu, vohnua, vohuni", "gloss": "blood", "script": null}
55	          ],
56	          "note": null,
57	          "quote": null
58	        },
59	        {
60	          "id": 5,
61	          "parent": 4,
62	          "lang": "Sogdian",
63	          "refs": "SOD:176,437",
64	          "words": [
65	            {"translit": "xwrn", "gloss": "blood", "script": null}
66	          ],
67	          "note": null,
68	          "quote": null
69	        },
70	        {
71	          "id": 6,
72	          "parent": 4,
73	          "lang": "Persian",
74	          "refs": "BRT:1434; HRN:113; SYN:206",
75	          "words": [
76	            {"translit": "xŭn", "gloss": "blood", "script": "خون"}
77	          ],
78	          "note": null,
79	          "quote": {
80	            "text": "عشق آمد و شد چو خونم اندر رگ و پوست - تا کرد مرا تهی و پر کرد ز دوست",
81	            "poet": "Molavî"
82	          }
83	        },
84	        {
85	          "id": 7,
86	          "parent": 0,
87	          "lang": "Persian",
88	          "refs": "IEC:1495,1525,1582; MON:470",
89	          "words": [
90	            {"translit": "bâh", "gloss": "sperm, sexual drive", "script": "باه"}
91	          ],
92	          "note": "MON:470 derives this word from Arabic",
93	          "quote": null
94	        },
95	        {
96	          "id": 8,
97	          "parent": 0,
98	          "lang": "Sanskrit",
99	          "refs": "POK:1172; IEC:1582",
100	          "words": [
101	            {"translit": "uštra", "gloss": "camel", "script": null},
102	            {"translit": "vasâ", "gloss": "liquid", "script": null}
103	          ],
104	          "note": null,
105	          "quote": null
106	        },
107	        {
108	          "id": 9,
109	          "parent": 0,
110	          "lang": "Germanic",
111	          "refs": "AHD",
112	          "words": [
113	            {"translit": "wôs", "gloss": "juice", "script": null}
114	          ],
115	          "note": null,
116	          "quote": null
117	        },
118	        {
119	          "id": 10,
120	          "parent": 9,
121	          "lang": "English",
122	          "refs": "POK:1172",
123	          "words": [
124	            {"translit": "ooze 1", "gloss": "to leak out slowly", "script": null}
125	          ],
126	          "note": null,
127	          "quote": null
128	        }
129	      ]
130	    },
131	    {
132	      "root": {
133	        "name": "Wes 2",
134	        "redirect": "Aus 2"
135	      },
136	      "nodes": []
137	    }
138	  ]
139	}
140	
```


## [2026-10-17T00:00:25.759Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','DZA','SOD','BQT','BRT','HRN','SYN','MON','AHD','WLD','PHD','NYB','HUB','CHEUNG','ARY','KLN','SKT','WEB','FSD','KNT','FVQ','AFM','PLA','LKT']:\n  v=d.get(k);print(k, v and {x:v.get(x) for x in ['kind','local_file','page_offset','lookup_hint']})\n\"; command ls data/verification/sources/refs/ | head -100"
}
```


### [2026-10-17T00:00:26.131Z] TOOL RESULT

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
POK {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
IEC {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
DZA {'kind': 'purchase', 'local_file': None, 'page_offset': None, 'lookup_hint': 'Not found.'}
SOD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'], 'page_offset': 'printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)', 'lookup_hint': "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}"}
BQT {'kind': 'archive_djvu+local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
BRT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
HRN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
SYN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
MON {'kind': 'website+archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
AHD {'kind': 'archive_djvu+website+archive_restricted', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
WLD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
PHD {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
HUB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
CHEUNG None
ARY {'kind': 'local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
KLN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
SKT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
WEB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt', 'page_offset': 'not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.'}
FSD {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."}
KNT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt', 'page_offset': 'leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations."}
FVQ {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'], 'page_offset': 'printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)', 'lookup_hint': 'Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).'}
AFM {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt'], 'page_offset': "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", 'lookup_hint': "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير')."}
PLA {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'], 'page_offset': '301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).', 'lookup_hint': 'HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)'}
LKT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."}
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


## [2026-10-17T00:00:42.526Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Page(s): 117[0-3]' POK_full.txt | head; grep -n -i 'uṣṭra\\|ustra' POK_full.txt | head; command ls ../../page-54*.json | head -3"
}
```


### [2026-10-17T00:00:42.957Z] TOOL RESULT

```
92403:Page(s): 1170-1171 
92459:Page(s): 1171-1172 
92521:Page(s): 1172-1173 
92619:Page(s): 1173-1174 
4618:round, take round; esp. of the eyes, to turn all round; in religion, to lustrate, purify , by 
5131:III 12) ' Annoyance, loss, pity, affliction, frustration ', Old Frisian angost. Old High German 
8334:= Germanic *austra-) " souther, southerly wind ', australis^ southern '; 
8370:austrin/s (vejas) ' north-east wind ', Latvian austrai. ' daybreak', austrums rw. 'East'; in 
8373:Old Church Slavic za ustra 'to "rrpwr (about utro, jutro 'morning' from *aus{t)ro- compare 
14534:present f/uoirom), flustra Nom. PL " calm (at sea) ' ( *flugstrom)\ if here (with nasalization) 
19898:untouchable '; dambhayatr makes confused, frustrated' {dambha-h^6ece\t'), Desid. dipsati 
23076:(Plaut), Umbrian frosetom^ cheated, beguiled, defrauded, robbed ', Latin frustra {newer 
23077:frustra) " in deception, in error, in vain ', therefrom frustror, -ari^ deceive, cheat ' belong 
25196:English alor6s.; Indo Germanic eroot is guaranteed through Old \ce\an6'\c Jglstr {* elustra) 
../../page-54.json
```


## [2026-10-17T00:00:45.033Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92395,92625p POK_full.txt"
}
```


### [2026-10-17T00:00:46.174Z] TOOL RESULT

```
" dwells '; 

Hittite {*hueis-) huis-^ live, am Leben bleiben', {*hueisa-) /7^/sa-" mirror'. 



References: WP. I 306 f., WH. II 773, Frisk 25, 173 f., 576 f., VendryJs RC. 35, 89 f.. Loth 
RC. 38, 297, Ifor Williams BBCS. 2, 41 ff., R. A. Fowkes JC. stem 2, 1 f. 
Page(s): 1170-1171 



Root / lemma: ues-2 {* hauhes-2) 
Meaning: to feast 

Material: Old Indie anu vavase^has aufgezehrt', vastoh'vor dem ravenousness', Avestan 
vasfraTresse, muzzle', vastrsm loo6' , vas far- ^H\rte'; about Latin vescor^as meal eat, be 
nourished ' see above S. 73; Middle Irish fess, fe/sslood, eating' {*ues-ta). Old Irish fi'ach 
"raven' ( *uesakos), out of it borrowed cymr. gwyach "Steiftfuft' (ein bird); Old Irish ban- 
[f]ess^ wedding ' (Trauen-fesf), bret. /7a/7i/e5 'festival', cymr. ^n/es/ 'festival'; Gothic waila 
wisan 'to feast, delight ', frawisan 'consume', wizon 'indulge oneself, waila-wizns ' feast ', 
gawizneigs' s\c\\ mitfreuend'. Old English tvesa/? 'to feast' (only Beowulf 3115, Hs. 
weaxan); Old High German firwesan. Middle High German i/e/wese/7 'consume'; Old 
Icelandic vist. Old English Old High German wisti. 'dish, food'; in ablaut probably Old High 
German M/as/e/( French gateau) ' cake'; 

Hittite {*hauhes^ ^es/- 'pasture', uesua-^qraze, abweiden; lead, regieren'; {*hauhes- 
)i/es/a/'a- 'herdsman, shepherd'. 

Maybe alb. ushq/mlood', ushqejleed'. 

References: WP. I 307 f., Vendryes RC. 35, 89 f., WH. II 769 

See also: probably to uesu- 'good'. 

Page(s):1171 

Root / lemma: ues-3 {* hyes-3) 
Meaning: wet 

Material: Gr. sapov Aournpa, n Trpoxouv Hes., alt-theraisch hsapa (meaning 
unacquainted); Umbrian i/es/z/ra/^'libato' (formation as Latin lectTca); 
Maybe alb. vese^ dew ' 

Old High German wasa/^ra\n', Old High German waso'\a\Nn, clod of earth, pit, pothole'. 
Modern High German l/Vasen lawn' , Old Saxon waso, Middle Low German wase^damp 
Erdgrund, slime, mud; clod of earth, lawn'; Middle Low German wasemm. 'Wasserdampf, 
haze, mist'; Old English wosn. ' dampness, juice, sap'; engl. ooze' dampness, slime, 
mud', as verb 'durchsickern, spring up, bubble'. Middle Low German wos'scum, froth. 



foam, decoction, extract acquired by boiling, juice, sap'. Old Danish Norwegian os' plant 
juice '; 

presumably Avestan varjhu-tat-t "blood', varjhu&wa-u. "Blutvergieflen, bloody fight', 
vohuna- m. 'blood' and Old Indie vasa, Kas5 "bacon, fat, lard ' (also i/asa inscribed, as 
vasa-m "flijssiges fat'); 

here with the meaning "male animal' (compare Latin verresetc: uer-, t/eA-s-'feuchten'): 
Old Indie ustra- m. 'Buffel, Kamel', ^s/5/'-'Pflugstier', Avestan ustrom. 'Kamel' (also in 
Zaral=>-ustrd)\ Old Indie ^5/5'Pflugstier'. 

References: WP. I 308, Trautmann 343, Mayrhofer 1 , 113 f.. Frisk 433. 
Page(s): 1171-1172 

Root / lemma: ues-4 {*hues-4) 

Meaning: to stick, pierce 

Material: Old Indie nivasita- 'ums Leben gebracht', n/rvasana-m^ das Ermorden, Toten', 

y0a/7Vas5ya//"sehneidetrings ab, from' ; Old Irish ;fe/7/75/o'"schindet' {*ues-na-ti)\ (common 

Celtic -ns-, -nt- > -nn-), alb. usht^ ear '; 

Lithuanian i/s/7/s 'thistle, hawthorn', Latvian usna, i/5/7a "thistle'; 

about Church Slavic vtdSB "louse' etc., see above S. 692 and Vasmer 1, 232 f. 
Maybe alb. vesh, PI. veshe^ ear'. 

Old High German c»/'/"cusp, peak, point, edge etc.'. Modern High German 0/t"place' (and 
"Schusterahle'), Old English ord^cus^, peak, beginning ', Old Icelandic oddr^cus^, peak'. 
Old Germanic Osd-ulfus= Old Saxon Old English 0/-o'-i//f (different above S. 237); 
[common Latin Germanic -s- > -/"-]. 

References: WP. I 308 f. 
Page(s):1172 

Root / lemma: ues-5 {* haues-5) 

Meaning: to dress, put on 

Material: Old Indie i/a5/e"kleidet sich, zieht an', Avestan vasteds. (compare the unthemat. 

gr. EGoai, -soTai), varjhaiti 6s.\ Old Indie vasana-, Avestan varjhana- n. " garment '; Old 

Indie vasman- n. "cover' (= z\\\a)\ vastra-, Avestan vastra- n. " clothing ' (: gr. FEGipa, 

Middle High German westeil); 

Armenian z-genum^'^uW myself an' {*ues-nu- = zvvv[}\), z-gest^ clothing ' (-/i/-stem); 



gr. Evvupi, Ionian sTvupi, Aor. zo{o)a\ " apparel ', Med. "sich kleiden', athemat. Perf. £l|jai 
(*F£a-[jai) 3. Sg. Eni-Earai (Herod.); zoBoq n. ' clothing ' (-dhes-stem), zaBr\q, -nroc; ds. 
(*F£a[TO-]TaT-c; with dem 9 from eoQoq); savoc; "weibliches garment ' (Old Indie vasana-m); 
Ionian Attic sipa, Doric Fripa, Lesbian Fsppa 'dress' (: Old Indie vas-man-); Hes. yHMCi 
ipaTiov, £u-, KQKO, 5ua-£ifju)v "good, schlecht gekleidet', with Vorstufe of Itazismuslpariov 
'dress, mantle'; Doric Fsarpa (ysaTpa aroAri Hes.), z(pzoip'\qi. "warmeres Wintergewand, 
Soldatenmantel'; 

alb. vesh'\ kleide an', i//s/7e/77"kleide myself an'; 

Latin vest/'s ' clothing ', vest/'o, -Tre " apparel ' (compare Yscrria svSugk; Hes.); 

Gothic wasjan. Old High German werian. Old Icelandic veria^ apparel ', Old English 
werian^6s., dress bear, carry'; Gothic wastii. 'dress'; Middle High German wester {see 
above) Taufkleid' (but Old High German early wastibarn, previously by Notker westerwat); 
Old Icelandic veslu. "dress' {*wesala-), ver^ coating, layer' {*waza-); 

Hittite uas-, ues-, Luvian uas(s)-^beV\e\6ev\, lure, tempt '; Tocharian B wastsi, wastsi 
"dress' (neologism); A wsal6s.\ 

References: WP. I 309, WH. II 775 f.. Frisk 521 f. 
Page(s): 1172-1173 

Root / lemma: ues-no- {* haues-no-) 

Meaning: price 

Material: By den einzelnen Sprachen sways e-and ovocalism: Old Indie vasna- m. " 

purchase price', n. "earnings', i/5S/7ay5//"feilscht'; Armenian gin^ purchase price'; gr. hom. 

(I)vo(; " purchase price', Lesbian ovva {*uosnS), Ionian Attic cJbvri " purchase', cbv£0|jai " buy 

', gort. u)vr|v " sell '; Latin venus{ov\\)j in Akk. venum, Dat. veno, later venui) "sale' {vendo, - 

dere' sell ' is *venom+ do, i/e/7eo "verkauft become' = *venom+ eo); marr. eituam 

vena//nam ^pecun\a{r\ venaliciam' (?) muft ein loanword from Latin sein, da s/7marr. not n 

ergeben wurde; Old Russian i/e/70 "dowry'; Hittite ussan/ya-' sell ' (compare above uas- 

"buy'). 

References: WP. I 31 1 f., WH. II 753 f., Vasmer 1, 182 f. 

See also: ues-8 

Page(s):1173 

Root / lemma: ues-7 {* haues-7) 
Meaning: to turn, wind 



Material: Old Indie veda- m. " hassock, clump of grass ' ( *uozdos); usnfhai. " nape ', 
usnTsa- m. "head fascia' {*us-nT-' gyration '); Swedish, Norwegian uase'Laubbundel', vasa 
"verwickein, maunder, drivel ', Old Icelandic i/55as/r"sich verwickein'. Middle Low German 
Middle English n/ase "bundle'. 
References: WP. I 309 f., Mayrhofer 1, 114. 
Page(s):1173 

Root / lemma: yes-8 {* haues-) 

Meaning: to buy, sell 

Material: Hittite uas-, uasija- "buy, acquire', ussaniia-^ sell ', uessia-^ purchase price'; 

perhaps Latin vTlis{*ues-li-) " cheap '. 

References: WP. I 312, WH. II 753 f., Szemerenyi Arch. Lingunder 6, 36 

See also: ues-no- 

Page(s):1173 

Root / lemma: ues-9 {* hayes-) 

Meaning: " gleam, shine ' 

See also: see above S. 86 f. [ayes-). 

Page(s):1173 

Root / lemma: yesperos {yekeros) {* hayekk"'ero) 

Meaning: evening 

Material: Gr. ia-nz^oc, m. "evening, vespertine ', sanspa f. "evening', ZQ-nt^xoo,, eonspivoq " 

vespertine '; Latin vesper, -er/s and -©/"/"evening, eventide ', vespera^ eventide ' (out of it 

Old Irish fescor, mcymr. gosper, gosber); probably to Modern High German West {above 

S. 73); against it Baltic- Slavic *uekera- m. "evening': Lithuanian i/a/raAas "evening' (PI. 

Ka/ra/'arWesten', vakarQ i/^5s"Westwind'), Latvian i/a/ra/'s "evening'. Old Church Slavic 

vecerb ds., wherefore Adv. Old Church Slavic vbcera " yesterday ' etc., basic meaning 

perhaps " darkness', to Lithuanian i//ra/7as "cloudy', i>/7/r/7a "shadow', Latin umbra {^ unksra) 

"shadow'; 

Maybe zero grade alb. Geg {* umbra-) mbrame^ yesterday night', mbramje' evening, 

darkness' Latin loanword. 

cymr. i/c/7e/'"evening' not here, but from Indo Germanic 'Vo/i^se/'o- (Pokorny ZcP. 15, 
377); Armenian ^/se/'"night' from *uoiRero-, after Petersson Heteroklisie 231 ff. zur root 
t/e/]^- "humid, wet' (?) in Old Indie vesanfa-m. "pond, pool' (compare FIN Lithuanian 



Viesinta, V/esmuoetc), Old Icelandic ve/g' intoxicating drink', Latvian vieksts 
"Wasserstrudel'. 

References: WP. I 311, WH. II 770 f., 814 f., Trautmann 348, Vasmer 1, 196, Frisk 575; 
the variation uesperos : uekeros perhaps after Specht Indo Germanic Dekl. 1 1 9 taboo to 
define; compare also Havers Sprachtabu 125, 178. 
Page(s): 1173-1174 

Root / lemma: ues-f{*h2auhies^ 

Meaning: spring, prime of the year 

Note:
```


## [2026-10-17T00:00:49.837Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'u[sš][tṭ]ra\\|camel\\|w[eē]s[oō]s\\|^w[eoā]s' IEC.txt | head -40"
}
```


### [2026-10-17T00:00:50.533Z] TOOL RESULT

```
4964:ghrondhos, å (1) “base, floor, timber, beam’. WP I, 657. Cf. ghrendk- and ghrndh- Gallo-Latin grunda ‘roof; sug-grunda ‘eaves’; Ir. cf. gronn-lus, s. ‘groundsel’, lit. ‘ground- herb’; MHG grant, gs grandes (1) “base”; Slo- vene (?) grod “four-handled carrier, bier’; Li. grañdas ‘floorboard’; grandà ‘plate, sheet’; Latv. grodi, mpl. ‘well-top, balustrade; but- tress; foundation’. (For G Grand, R grùda, Cz. hrouda, see guhrondh-)
6232:distinguishes relationship from content, as in Cz. krevní ‘relating to blood": Li. kraujinis, id., cf. the Ligurian river-name Beverin (in the Engadine), and the Sequanian aidrini “bright in the Coligny weather-diary, cf. Gk. aithrinós “of early morning’. The passage from adj. to noun is illustrated in Arm. grean, gs greno Cliterature': gir ^writing"); cf. also Per. pūst- in (ffurcoat? :püst (fur); Gk. eruthrinos Ca red fish": eruthrós); Alb. dulli, gs dullini (ju- niper, lit. ‘fragrant bush’, cf. dhülos (1) above); Lat. scrinium (^writing-case' in rela- tion to scribo); sterquilinium (tdungheap'": stercus); Ir. goirm-ín (*woad, indigo’: gorm “blue”); Li. gandrynas (‘swarm of storks’: gañ- dras); akmenynas, akmenjne (‘pile of stones? :akmuoó). For the fem. suffix cf. Alb. kopshtin- je (market garden’ : kopsht *garden"). An ad- jectival extn. of an adj. occurs in Skt. navinah (new': navah), and cf. Arm. mi£in (‘mid- most': me£). A dim. extn. arises in Ir. goib-ín (small mouth": gob) and in Go. gait-ein Cd": gaits); W dern-yn (‘small piece’: darn); Li. merg-inà ("little girl: mergà)
8930:Klitos, à ‘sloping; slope’. Cf. Klitis. WP I, 490. Cf. Kleii, etc. Skt. $ritáh “attached” (isophonic, but possibly a different root); Gk. klítos, gs -eos, n., and klitüs, f. ‘slope’; OHG fita, G Leite, OE hlip, pl. hleobu, n. *mountain-slope, cliff; ON cf. i-st. hlið, hlíó, f. “side; slope’; Latv. slita “log- fence; balustrade'. (NB. The above forms co- incide in some instances with a type *klitis, kleitos, with velar initial).
11603:nek- ‘negation, not-?. Lat. ambig., cf. neko, nekus Lat. (?) neco, are, pf. -ui (kil. Semantics of Li. naikinti «destroy'?, but see below: neK-); W neg, pl. ion, m. “barrier, frustration"; negio, inf. ‘frustrate’; Big. nekam, v. “say no; deny
19015:tropos, ios (2) "inhibition, frustration’. Cf. trp- (2) and WP I, 756 Skt. trapa, f. ‘shame, shyness’; OE cf. prafian, v. (1) ‘restrain, reprove’ cf. E dial. to thraft, id.; Norw. cf. treven, adj. ‘sullen, dull’
```


## [2026-10-17T00:00:54.044Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -i '.\\{0,200\\}\\(kamel\\|camel\\|ustr\\|uṣṭr\\|ooze\\|bah\\b\\).\\{0,300\\}' IEC.txt | head -20"
}
```


### [2026-10-17T00:00:57.764Z] TOOL RESULT

```
ugrep: error: error at position 139
b)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,300}
          exceeds complexity limits___/
```


## [2026-10-17T00:01:01.119Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'camel',r'ustr',r'u[sš]tr',r'ooze',r'wōs',r'wes-',r'Per\\. bāh',r'bāh',r'xūn|khūn|ḫūn']:\n    for m in re.finditer(pat,t):\n        print(pat,'::',t[max(0,m.start()-250):m.end()+250].replace('\\n',' '));print('---')\nE"
}
```


### [2026-10-17T00:01:02.050Z] TOOL RESULT

```
<persisted-output>
Output too large (62.3KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/btdf8bmhn.txt

Preview (first 2KB):
ustr :: arədå — armn- (arimn-) 34 ‘unstable, corrupt’; ardà ‘quarrel; cf. OCS radina ‘care, sorrow’, radivú ‘hardworking’; raždọ, raditi ‘care’ (Li. and Sl. ambig.) arədā, see ardā arədhlom ‘plough, ploughshare’. WP I, 78. Cf. arātrom, aro, io (1) MHG arl; Austro-Ger. Arl; OCS oralo, ralo; Cz. rádlo *ploughshare'; Slovene orálo ‘plough’; ralo *ploughshare'; oral ‘acre’, ral 'arable field"; Li. arklas; Latv. arkls arotàios (artàios) ‘ploughman’. Cf. aró, io (1) Gk. cf. arótes, Locrian name Aratuos; OCS rataj
---
ustr ::  east’. WP I, 27. Cf. ausá Skt. usrà; Arm. awr (avur, avurb 'day'); Gk. cf. Hes. mirg-ábor, a dialectal form “twilight (other forms are ambig. Cf. auríon 'tomor- row’, aōri “in the morning”, Aeol. ados, Dor. aós, At. eós dawn); Li. au&rà; Latv. cf. austrs “east wind’ and austrumi, m. pl. ‘east’ and the Gmc. forms represented by ON austr “east”, etc. auster-, see aue-ster- austros, om ‘ladle, well-bucket'. Cf. ausó Lat. cf. haustrum (h- unexplained); ON austr ` aut (auti, autim, autom) (out-, etc.) "
---
ustr :: usá Skt. usrà; Arm. awr (avur, avurb 'day'); Gk. cf. Hes. mirg-ábor, a dialectal form “twilight (other forms are ambig. Cf. auríon 'tomor- row’, aōri “in the morning”, Aeol. ados, Dor. aós, At. eós dawn); Li. au&rà; Latv. cf. austrs “east wind’ and austrumi, m. pl. ‘east’ and the Gmc. forms represented by ON austr “east”, etc. auster-, see aue-ster- austros, om ‘ladle, well-bucket'. Cf. ausó Lat. cf. haustrum (h- unexplained); ON austr ` aut (auti, autim, autom) (out-, etc.) "but, yet, only'. Cf. au
---
...
</persisted-output>
```


## [2026-10-17T00:01:06.553Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor pat in [r'camel',r'ooze',r'Per\\. b[aā]h\\b',r'\\bb[aā]h[,;\\s]',r'vohun',r'vasā']:\n    for m in re.finditer(pat,t):\n        leaf=t[:m.start()].count('\\f')\n        print(pat,'leaf',leaf,'::',t[max(0,m.start()-300):m.end()+300].replace('\\n',' '));print('---')\nE"
}
```


### [2026-10-17T00:01:07.421Z] TOOL RESULT

```
ooze leaf 119 ::  tha- pan, acc. f. ‘fear’ (uncertainly to kró-taphos ‘temple of head’); Go. dumbs, OHG tumb; OE & Sw. dumb, etc.; Latv. cf. (ambig.) dimba ‘scrape, difficulty’.? *dhmb-. O-gde in Skt. dambhah “fraud”, lit. “bemusement. Cf. also Arm. damarim ‘get confused' (ambig. cf. dhmb-); EMDu. dommeren ‘doze, snooze’ dhmbh- (2) ‘tomb’. See dhnguh- Arm. damban, id.; Gk. (ambig.) táphos. A variant occurs in MHG tümpfel *water-hole? beside (W. Saxon type) tümpel *cunnus'; E dimple (fr. *dhmbilo- or *dhum-) dhmbhrio *be dazed'. See dhmb- and dhmbh- dhndhol- ‘idling, dallying; idler; to idle’. Cf. dhondhoal- and d
---
ooze leaf 128 :: ic is Latv. drūms ‘gloomy, dingy’) dhrumbó, ið lumber along’. (variant with *-b-. Cf. dhrombh-, dhrmbh-) MHG trumpfen, id.; Li. drumbiü, éti, id. dhrun- ‘rumble, roar’ Go. drunjus ‘din’: Icel. drunur, f. pl. id.; drynja, v. ‘rumble’; Cz. drním, čti, id.; Big. drán! ‘zoom! twang!; Li. druniù, éti ‘snooze’ dhrugh- — dhruuos, à 10 15 20 25 30 35 40 45 210 (Extended forms in) Big. dránkam ‘jangle’; Slovene drndati, id. dhrunuk-, see dhurunk- dhrup- ‘break up, crumble’. Cf. dhrubh-. Cf. WP I, 800 & 873 (G Trub, Trüb "bam" is ambig. cf. dhrubh-); Srb. drpam & drpim ‘têar, break up’; Latv. drüpu, drupt *
---
ooze leaf 374 :: -kotaty ‘tickle’ lasok-, see las- (1) and lasik- lasiguhos, å (?) ‘limp rag” (?) Gk. laiphos, n. ‘garment, rag, sail; OLat. là- ruua, Lat. larva (&mask', but OLat. 'ghost). (Isophonic: Go. lasiws ‘weak’; MHG er-les- wen ‘grow weak’; ON loskr, las- ‘weak’, but cf. Li. laskana 'rag") lasik- (lasok-) ‘ooze, gum, spittle; tree with oozing gum'. Cf. las- (1) Skt. lasika ‘spittle? beside lasakah (a tree); Lat. larix, gs -icis, f. ‘larch’, cf. laricina "ur. pentine'; LLat. cf. laragátum ‘resinous wine from larches'; laser, n. (gum, benzoin’, w. dissimilated consonants cf. miser); làsikos, à (lások-, lāsk
---
ooze leaf 375 :: ; Cz. láska ‘love’. The evidence of W. is ambig. cf. llochi, v. inf. ‘to fondle, cherish’, 3s. llawch (from a type *laks- or *plaks-). Isophonic: llawch, m. “protection” lasKo (form of laio, w. extn. in -sK-) “bark? Gk. lasko; Alb. leh, lef, id. lat- (1) (lator, latis, latio) ^wetness, liquor, mud, ooze’. Cf. latok-. WP II, 381. (For sen- ses ‘favour’ and ‘luck’, see lat- Ou Ir. laith, gs latha, f. ‘liquid’; beside lathairt, f. ‘liquor, lees’; W Haid, pl. lleidiau, m. “mire” beside Br. latar ‘wetness’; Icel. leója, f. ‘mud’ lat- (2) “favourable, lucky; favour, luck Hitt. laccis ‘fortunate, favoura
---
ooze leaf 375 :: from a type *slaktis, q. v.) lat- (2) “hero, man, boy’ (?) Ir. láth, láith, m. ‘champion’, cf. láthar, m. “vig- our’; láthas, m. ‘valour’; W llawd, m. (lad. As an adj. ‘pert, lewd’ cf. platos? Possible isophones occur in Pol. tacny ‘easy’ and Cz. láce *cheapness") i latək- ‘liquor, fluid; drainage, ooze, mire’. Cf. lat- (1). WP II, 381 Gk. cf. látax, gs latagos ‘dregs’; latagë ‘dash of liquor’; Lat. latex, gs. -icis, f. ‘liquor, fluid’; Ir. lathach, laitheach, f. ‘mud, mire’; W Russ. lotok (ditch, gutter. Bois); Li. latákas ‘stream, fluid, gush, puddle; ditch’ látoró, ið (later-, latur-) ‘shout, s
---
ooze leaf 519 :: sts a type *pigro-) (piiont-, piiont-, in Go. fijands, OHG fiant, OE feond ‘enemy’, see piio (2)) piio (1) ‘drink’. WP II, 71 Skt. piye, mp. id.; Gk. cf. pino, fut: piomai, aor: e-pion, id. beside pipisko, fut: piso, v. ‘water — animals’; Alb. pi, v. ‘drink’; LLat. *pio, are in Norm. Fr. pier, v. ‘booze’, OFr. pier, v. ‘drink’; NFr. pion, m. ‘boozer; OCS pijo, piti and com. S1. ‘drink’; Li. pyju & pynu, inf: pyti, v. ‘soak up: cf. py-dyti, inf. (make (a cow) yield milk"). A type *pilər is posited for OCS pirü, m. ‘carouse’; Slovene pir, m. ‘wedding’; Blg. pir, Ukr. pyr, m. ‘feas? piio-, pii- Skt. 
---
ooze leaf 519 :: fijands, OHG fiant, OE feond ‘enemy’, see piio (2)) piio (1) ‘drink’. WP II, 71 Skt. piye, mp. id.; Gk. cf. pino, fut: piomai, aor: e-pion, id. beside pipisko, fut: piso, v. ‘water — animals’; Alb. pi, v. ‘drink’; LLat. *pio, are in Norm. Fr. pier, v. ‘booze’, OFr. pier, v. ‘drink’; NFr. pion, m. ‘boozer; OCS pijo, piti and com. S1. ‘drink’; Li. pyju & pynu, inf: pyti, v. ‘soak up: cf. py-dyti, inf. (make (a cow) yield milk"). A type *pilər is posited for OCS pirü, m. ‘carouse’; Slovene pir, m. ‘wedding’; Blg. pir, Ukr. pyr, m. ‘feas? piio-, pii- Skt. cf. pry-üsam, n. ‘thick milk’; Gk. cf. dip- si
---
ooze leaf 589 :: eproof rár-, see rór-. Short vowel in Scots rair, rare, v. roar’, in phr: raring to go); Li. raruoti, inf. id. rásó, ið ‘roar, rush, shout’. WP II, 342. Cf. rés- Skt. rasàmi, rase, v. ‘roar’; rasanam, n. ‘roar, roaring’; Av. ráh-, ‘resound; praise’; Scots to raize, v. ‘to madden’ beside E dial. to rooze, v. ‘roar — of a fire’; Du. cf. roes, m. “tipsiness'; ON rasa, v. ‘rush’ beside ras, n. “race, dash’; Sw. rasa, v. (2) ‘rave, rage"; ras, n. ('din; exu- berance', but rosa, v. ‘praise’; Norw. rose, id. beside Sw. ros, pl. -er, f. ‘praise?’ are from a rap- (rop-?) — rëdh- 20 25 30 35 40 45 1064 type
---
ooze leaf 603 ::  rasā, f. ‘moisture’; rásah, m. ‘sap, es- sence’; Alb. re, f. ‘cloud’; Lat. ros, gs: roris, m. ‘dew, liquid’; OCS (and com. Sl.) rosa, R rosà, f. ‘dew’; Li. rasà, Latv. rasa, f. id. rós- (2) “stir, dash, violence’. Cf. rið Gk. (ambig.) eroé, f. “dash, force’; Du. roes, m. ‘drunkenness’; E dial. to rooze, v. ‘roar — as a fire’; ON cf. rósta, f. ‘tumult? (rosà ‘dew, moisture’, see rós- (1)) rosg- “twist, branch'. Cf. resg- Skt. (ambig. *-e- or *-o-) rájjuh, f. ‘rope’; OCS rozga, f. “branch, whip, shoot; R rózga, f. *birch-rod'; (e-gde in) Latv. režģi, mpl. (^wic- ker, matting'. See resg-); Li. cf. r
---
ooze leaf 610 :: th, adj. /sundered'; rhwtion, rhytion, mpl. *frag- ments’; Li. pa-rüptas ‘chapped — of hands” beside rüptas, adj. ‘erupted — of rash’; cf. OCS rüpünü, adj. (sudden or sim.) rüs- (1) ‘rush, roar’. Cf. reuos (1), ruuó & rüstis Skt. rüsah, adj. ‘tart, harsh; LG rüsen, v. ‘bluster’; E rouse, v. beside rooze, v. ‘roar — of a fire" (dial.); Sw. rus, n. “rush”; rusa, v id. beside rysa, v. ‘horrify’; ON (short vowel) rosi, m. ‘downpour’; Cz. cf. rych-ly, adj. ‘quick’; (R ryxlyj, adj. = ‘crumbly, spongy’); Latv. rūsa, f. (2) ‘summer lightning’; Li. cf. rüstüs, adj. ‘grim’ rüs- (2) “fall, fail, crumble, dec
---
ooze leaf 630 :: type: sik-, q.v. and cf. siqu-, siqusos. (The Germanic evidence im- plies consonantism of both types) Skt. sifcami, pp: siktáh, tr. “pour, sprinkle’; Av. hinca-, f. id. (and *wet); Gk. cf. (variant: *sik- in) ik-más, gs: -mádos, f. ‘moisture’; OE seon, pp: sigen & siwen, sv. 1. tr. ‘filter’; intr. ‘ooze, seep, trickle? beside seohhian, v. "filter, drain’; sife, n. ‘sieve’; sifepa, m E fpl. *siftings'; siftan, v. (‘sift’; if -f- is from *-qu- sil- — sis, si- 10 20 25 30 35 40 45 1140 as in wulf, seofon); OHG cf. (*seik-) sihan, sv. 1. “drain, sif? beside MLG and G sichten, v. ‘sift’; sichte, f. ‘si
---
ooze leaf 646 :: s. cf. sklent, adj. ‘slanting’; Li. sklandüs, adj. "sid. ing’; sklandá, f. (2) ‘slope’; Latv. (fr. Li?) sklan- da, f. (2) ‘slope’ sklug-, variant of type slug- with palatal- ism, q. v. Ir. sclogaim, v. ‘gulp, gasp’; sclog & sclug, m. ‘throat’; G Schluck m. ‘gulp; abyss, glen’; OHG cf. slucko, wm. ‘boozer sklütro, ið “jerk, jog’. Cf. (sludhro), slütor- Arm. xlrtem, v. ‘move, shake, stir; MHG slü- dern, v. “jerk, fling’; cf. for the consonantism R xlystàt, inf. ‘lash, spurt sklp-, see Supt: 5 skinb- ‘bent, twisted; bend, twist, hollow’ Gk. skambós, adj. 'bandy-legged'; cf. skan- in skán-dalon (&bent
---
ooze leaf 669 :: rawl’; Late, cf. šlau- gans, adj. ‘slack’; LW in Finn. liukas ‘sleek; slippery'. See next sleug- (variant of type sleug-, q.v.) Big. Srb. stuz, f., Pol. $luz, m., Cz. sliz, m. ‘mucus, slime’; (alleged) Li. sliaužti ‘creep’ and Latv. sļauža ‘sneak, creep’ (untraceable) sleuros ‘smooth, slimy; slime, ooze’. Cf. slür-, leur- Gk. leurós, adj. ‘smooth, level, expansive’; cf. *-ou-:*-ü- in kol-loúrion & kol-lürion, n. *eye-ointment; fine clay'; Lat. cf. (?) lora, f. (thin second wine from pressed grape-skins', if fr. *sleuor-); W llerw, adj. squeamish’, w. mmetath. cf. tarw, garw, fr. *tauros, *$auros);
---
ooze leaf 670 :: f. ‘soot’; cf. also a-lisgéo, v. ‘defile’; MIT. slige, Ir. slighe, f. ‘road, track’; OBr. Dou ‘stain’; MHG slich, sm. ‘glide, trail’ beside slëc, gs: -ckes, m. ‘tasting, sampling’; OE slic *oilstone': EME slickstone, id.; ON sliki- steinn, id.; OFris. slick, m. ‘sludge’; G Schlich, m. *metal-slick; ooze; byway’ beside Schlick, m. (*mudbank, fr. LG); cf. Schleck *titbit'; EME slick, adj. ‘corpulent; smooth; fatty’; mod. “trail of oil; sludge from metal"; LG cf. sick, pl. *byways'; Sw. slicka, v. ‘lick’; Li. sliZis, gs: -io, m. ‘slug, snail. Long-grade forms include: Lat. fü-ligo, -liginis, f. (soot
---
ooze leaf 683 :: ; OE snot, n. ‘snot; OFris. snotta, wm. id.; Du. snot, s. id.; Icel. cf. (long z-gde) snýta sjer, v. “blow the nose'; OE snytan, v. id.; Li. snuda, mf. (2) 'sniveller (snüið ‘turn’, see sneu-, neu-) (snumbh-, see snubh-) snüs- (snust-) ‘doze’ Gk. cf. nustázo, v. ‘nod, drowse'; E northern dial. to snooze (cf. N. Eng. to crooch = to crouch; to mooch = to mouch, etc.); Fris. cf. snüsterich, adj. *fusty, dusty’; Sw. Norw. snusa, snuse, v. ‘sniff snoitos, is (snoitt-, snoist-, snoits-) — so, sã, tod 15 20 25 30 35 40 45 1238 snusos, å, io, us ‘daughter-in-law’. WP II, 701 Skt. snusà, id.; Oss. nostä, i
---
ooze leaf 703 :: E; Norw. stripe ‘stripe, streak’; squhel- — sreuð, ið 20 25 30 35 40 45 1276 Sw. stripa, f. ‘gash’ srém- “Tun; running, flow? Skt. cf. sramse, mp. ‘fall’; pp: srastáh “fallen”; Per. ram, s. ‘flight’ beside ramam, -idan, v. ‘flee’; Alb. rremb, m. ‘current; artery’; Ir. Stream, mf. ‘fluid, viscosity, ooze’; MHG strám & stran, sm. ‘stream, current; Sw. cf. eld- strimma, f. “hail of bullets, volley’; R strémja, n. (2) “torrent, rapid’; stremnina, f. id. and ‘precipice’; cf. stremit'sa, v. ‘rush, gush’; stremglàv ‘headfirst’ sren- ‘loin, kidney’. Cf. rénos, is Lat. rén, gs: rénis, m. ‘kidney’; Li. dia
---
ooze leaf 752 :: oli, inf., tawl, 3sg. ‘divide, cut’; be- side tolli, inf. ‘take away’; Cz. cf. o-tálet, inf. ‘dally, delay; remove’; cf. also talácet, inf. ‘wander’; Li. toli, adv. ‘far’; tolüs, adj. ‘dis- tant”; Latv. tāli, tālu, adv. ‘far’; tals, adj. ‘dis- tant’. (NB. For Gk. tēle-, see quel- (quël-)) tāl- (3) ʻooze, flow; tāləuos ‘seepage, pus, matter’. Cf. taið (1) Ir. tálaim, v. “drip, pour, flow’; tál, pl: táil, m. (2) ‘flow, milk-yield'; OCS talü, adj. ‘liquid’; Slovene taliti, inf. “melt, dissolve’; Srb. cf. talog, m. ‘sediment. Extn. in Oss. táläw, s. ‘carbuncle’; Cz. talov, m. ‘pus’; R talyj, adj. ‘tha
---
ooze leaf 793 :: à, id. trust- (1) (trustis, os, for *trudst-) “poke; poker, stick'. Cf. trüd-, treud-. WP cf. I, 751 & II, 634 Ir. trost, m. “stick; thrust; headlong fal; EME thrust, as mod.; OCS trüstí, f. freed, cane, bristle’; OCz. trest, gs: trsti, f. ‘reed, cane; R trosti, f. ‘stick, cane’ trust- (2) ‘filth, ooze’ Ir. cf. trostar, m. ‘filth, dirt’; OE cf. brust- fell, s. leprosy’, lit. ‘foul skin’); Cz. Dest, gs: tresti, f. extract, juice’. (ISophone: W trws, pl. -oedd, m. ‘covering, dress’) trust- (3) (?) ‘staid, stolid’ W cf. trwstan, adj. faccident-prone'; LG (am- big.) druste, adj. ‘staid, solid’; R (?)
---
ooze leaf 821 :: mercenary?) uàr- (4) “water, liquid, fluid, flood’. Cf. uor- (5) Skt. var, vari, n. ‘water’; Av. vàro, m. ‘rain’; vairis, f. ‘lake’; Sogd. war, s. ‘rain’; Tokh. A wär, B war, s. ‘water’; Oss. cf. warin, warun, uāp- — uas- (uasilos, uaslos) 20 25 30 35 40 45 1494 s. and v. ‘rain’; OE wor, s. ‘water, ooze’ be- side (*-à-) waer, n. ‘ocean’; ON vari, n. ‘lymph’; cf. also OE wor-hana, wm. *moor-cock'; Du. woerhaan, m. ‘pheasant’ beside woerd, m. ‘duck’. (Cz. var, m., Pol. war, m. s. = ‘brew’; Cz. vařit, Pol. warzyé, inf. ‘brew, boil. Of uncertain origin but with an isophone in Latv. vàru, it, v. “boil'
---
ooze leaf 822 :: au, m. ‘defect, lack’; Cor. gwall, pl. -ow, m. ‘lapse, lack’; MHG cf. wesel, adj. (2) ‘limp’; Li. cf. vasnoti, inf. ‘flap, flutter’ 1495 uås- (uðs-?) ‘fluid’. Cf. uos-, ues- (5) and WP I, 308 Per. bah, s. ‘semen’; Hitt. wasi, n. (a ritual drink); OE wos, n. “Juice, liquor, sap’; wese, adj. ‘wet; OE ooze; Sw. (?) os, n. ‘vapour, steam’; cf. mat-os ‘smell of food’; kol-os *fire- damp’; short vowel in MHG wase, wm. ‘turf; E dial wazz, s. ‘urine’. (NB. Gk. haima *blood' is entirely ambiguous, fr. *uasimn-? Other possible cognates arise in Gk. eióeis, Doric -à- *squelchy, oozy’, of geese, of a har- bou
---
ooze leaf 823 :: efresh’; vēdis, gs: vëdZio, m. ‘oscillation’ uēd- (2) (uedios) ‘wet, damp’. (Arm. type *uedio-) Oss. wdain, Dig. wodajun, inf. ‘wet; Arm. gec, gs: giči, ab. s. -av, adj. ‘wet; OE w&t, adj. ‘damp, wet; waeta, wm. “moisture, fluid"; ON vátr, adj. *wet; mod. also væta, f. *wet- ness’; cf. wætla, inf. *ooze^; Sw. våt, adj. ‘wet’; vüta, f. *wetness' uedm-, uednom *bride-price, dowry’. WP I, 256 Gk. hédnon, n. “bridal gift'; Burgundian witte- mo(n) ‘dowry’; OFris. wetma, witma, wm. id.; OE wituma, weotuma, wm. id.; OCS (and com. SL.) véno, n. id. (Not related to OHG widamo, id., see Kl. DEW : Wittum and
---
ooze leaf 854 :: l, ferment, seethe’; OCS vlajo, vlajati, v. ‘surge, billow’; Cz. vlaju, vlát, v. (wave, intr); Late vilàju, at, v. ((1) “roll about, intr.); (variant extension in) Go. wu- lan, v. ‘seethe, rage’; OE wyllan, v. (“boil', intr. beside wylian & wylwan, v. ‘roll’. Cf. ulu- with extns. ulam- ‘mud, marsh, ooze, lowland’. WP II, 386 Oss. lámi, s. ‘mud’; Gk. léme, f. ‘rheum’; Alb. llom, m. ‘mud’; Lat. làma, f. ‘puddle’; G Lume, f. id.; cf. MLG wlom, adj. ‘muddy’; Blg. cf. làmo ‘shoddy, coarse wool? beside lám- ba, f. ‘mud’; Li. lómas, lomà, mf. ‘lowland’; Latv. làma, f. ‘puddle’ ulost- (ulott-), residual f
---
Per\. b[aā]h\b leaf 822 :: mping’. Lat. varius, adj. ‘changeable’; Gk. cf. (?) at, ouros (eat, lit. ‘wavytail’ (?)); W cf. gwall, pl. -au, m. ‘defect, lack’; Cor. gwall, pl. -ow, m. ‘lapse, lack’; MHG cf. wesel, adj. (2) ‘limp’; Li. cf. vasnoti, inf. ‘flap, flutter’ 1495 uås- (uðs-?) ‘fluid’. Cf. uos-, ues- (5) and WP I, 308 Per. bah, s. ‘semen’; Hitt. wasi, n. (a ritual drink); OE wos, n. “Juice, liquor, sap’; wese, adj. ‘wet; OE ooze; Sw. (?) os, n. ‘vapour, steam’; cf. mat-os ‘smell of food’; kol-os *fire- damp’; short vowel in MHG wase, wm. ‘turf; E dial wazz, s. ‘urine’. (NB. Gk. haima *blood' is entirely ambiguous, fr. *u
---
\bb[aā]h[,;\s] leaf 77 :: rst. Cf. WP IL, 206 and bhrstis above W brysio ‘hasten’, brys ‘haste’; Br. brésia ‘scamper’; OS brustian ‘break out; Slovene brstiti ‘sprout’; Icel. cf. byrstur, adj. ‘harsh, gruff; OE cf. byrst ‘loss’ bhrt- (bhrt-) (1) ‘strike, blow; striker; fate’. Cf. bherio & bhrio (1) Oss. bårdin ‘cudgel; Arm. bah ‘spade’; Per. bil, id.; Lat. fors; Ir. bráth ‘judgment; W brawd, id.; Br. breed ‘ple; MHG burt ‘pledge, duty’; OE byrd ‘fate’; Du. beurt ‘turn, lot; OFrankish, cf. staim-bort (a weapon: *stone-throwing catapult’) bhrt- (2) ‘bearing, load, product. WP II, 153. Cf. bhero, bhoros bhrsos, ios, à, is — 
---
\bb[aā]h[,;\s] leaf 822 :: ’. Lat. varius, adj. ‘changeable’; Gk. cf. (?) at, ouros (eat, lit. ‘wavytail’ (?)); W cf. gwall, pl. -au, m. ‘defect, lack’; Cor. gwall, pl. -ow, m. ‘lapse, lack’; MHG cf. wesel, adj. (2) ‘limp’; Li. cf. vasnoti, inf. ‘flap, flutter’ 1495 uås- (uðs-?) ‘fluid’. Cf. uos-, ues- (5) and WP I, 308 Per. bah, s. ‘semen’; Hitt. wasi, n. (a ritual drink); OE wos, n. “Juice, liquor, sap’; wese, adj. ‘wet; OE ooze; Sw. (?) os, n. ‘vapour, steam’; cf. mat-os ‘smell of food’; kol-os *fire- damp’; short vowel in MHG wase, wm. ‘turf; E dial wazz, s. ‘urine’. (NB. Gk. haima *blood' is entirely ambiguous, fr. *ua
---
```


## [2026-10-17T00:01:15.738Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(862,872):\n    p=pages[i]\n    for m in re.finditer(r'1582|1525|ues- \\(5\\)|u[oō]s-|Kamel|uṣṭr|ustr|uštr|Bušt|ušt',p):\n        print(i,m.group(),'::',p[max(0,m.start()-200):m.end()+600].replace('\\n',' '));print('---')\nE"
}
```


### [2026-10-17T00:01:16.358Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
IndexError: list index out of range
```


## [2026-10-17T00:01:22.314Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'\\b1582\\b',r'\\b1525\\b',r'ues- \\(5\\)',r'uesō',r'uesos']:\n    for m in re.finditer(pat,t):\n        print(pat,'leaf',t[:m.start()].count('\\f'),'::',t[max(0,m.start()-100):m.end()+900].replace('\\n',' '));print('---')\nE"
}
```


### [2026-10-17T00:01:23.228Z] TOOL RESULT

```
\b1525\b leaf 839 :: g; pur- pose’ . ues- (3) ‘wither, fade, rot, waste away” Hitt. (ambig.) cf. wesuriya(mi), v. ‘waste 1525 away’; Lat. cf. vescus, adj. (2) ‘puny, lean, if not fr. *guersK-, cf. vescor); Alb. cf. veshk, v. tr. (^wither', if fr. *ues-sKo); Ir. cf. feosach, adj. ‘withered’; ON cf. vás, n. ‘exhaustion, toil'; cpds. "bad. trying, cf. OHG wésaneén ‘wither, fade’ beside wérnon, wérnen, v. “suf- fer’; wérna, f. “suffering, hunger’; OE wisnian, weornian as OHG; cf. MHG wésel, adj. limp, weak; (but Go. fra-wisan, sv. 5 ‘expend, waste’: MHG ver-wésen ‘destroy; decay’ are probably referable to type *ues- (2) in the intr. sense *decay). Cf. also ON visna, v. ‘wither, fade? ues- (4) ‘put on (clothing); wear’. WP I, 309 Skt. váse, mp. ‘wear’; Av. vas(ē), mp. ‘dress’; Tokh. AB wäs-, B yás-, v. id.; Arm. cf. z- genum, v. ‘get dressed"; z-gest, u-st. ‘garment’; Hitt. wes(mi), wasami, wasiyami, wasemi, v. ‘put on — clothes’; Gk. Ion. heimai, 2s: héssai, 3s: héstai, v. ‘wear’ beside Gk. hénnüm,i, fut: héso, t
---
ues- \(5\) leaf 822 ::  wesel, adj. (2) ‘limp’; Li. cf. vasnoti, inf. ‘flap, flutter’ 1495 uås- (uðs-?) ‘fluid’. Cf. uos-, ues- (5) and WP I, 308 Per. bah, s. ‘semen’; Hitt. wasi, n. (a ritual drink); OE wos, n. “Juice, liquor, sap’; wese, adj. ‘wet; OE ooze; Sw. (?) os, n. ‘vapour, steam’; cf. mat-os ‘smell of food’; kol-os *fire- damp’; short vowel in MHG wase, wm. ‘turf; E dial wazz, s. ‘urine’. (NB. Gk. haima *blood' is entirely ambiguous, fr. *uasimn-? Other possible cognates arise in Gk. eióeis, Doric -à- *squelchy, oozy’, of geese, of a har- bour, if fr. a type *uasient-, cf. also Eiðn, s. queried *mudflat,, if fr. *uasion. W gwaed, m. “blood”, ambig., may derive from *uasito-) uástos, is 'empty; space’. Cf. WP I, 109 & 219 Lat. vàstus, adj. ‘waste, huge; insatiable’; Olr. fáss, adj. ‘empty’; Ir. fás, adj. ‘desolate, desert- ed'; OHG wuosti, OE weste, Dutch woest, adj. “desert, waste, desolate, empty”; OS cf. wostin, wostinnia, f. ‘desert’; (NB. The Eng. form waste is hybridized with Gmc. via OFr. Cf. guast, 
---
ues- \(5\) leaf 840 :: ; Br. gwiska, tr. id.; W gwisgo, id.; cf. Br. gwisk, pl. -u, m. ‘dress’; W gwisg, pl. -oedd, f. id. ues- (5) ‘soak; water’. Cf. uosolos, uðsos Skt. cf. vasin, m. ‘otter’; Tokh. A wes, B wents ‘urination’ beside B wesye, wensye, s. ‘mud’; Per. bàh ‘sperm’; Arm. cf. to-gorem, v. (soak, steep’: Gk. deüo, v. id.); cf. also Gk. di-éme- nos, pp. ‘watered, sprinkled', and eiíamenés, f. 4ey-meadow'; Lat. cf. (?) v&s-sica (bladder, anat. if fr. *ues-siqu- ^water-drip); MHG wise, f. ‘meadow’. (For Lat. urina, urinor, see uüsos) ues- (6) ‘shine’. Cf. uesel- . Skt. (radical only) vas- ‘shine’; cf. vasrah, m. *daytime'; vasar- in cpds.; Vedic also vàsá- yami, v. “make shine’; Av. váh-, v. ‘lighten, dawn’; Arm. cf. gey, o-st. (beauty, fr. *uesel- or *uesl-, cf. ueselos below) ueselos (uesal-, ueslo-, uésel-, uésol-) (1) “bright, cheerful, thriving'. Cf. ueKsl-. Sl. ues- — uesoar- 10 20 25 30 35 40 45 1526 and Latv. ambig. Skt. vasarab, adj. “bright; vasrah, m. 'day- time’; Arm. gey, o-st. ‘beauty’; Lat. cf.
---
ues- \(5\) leaf 840 :: sara, f. id.; vasáris, gs: -io, m. *February'; Latv. vasara, f. summer uesor- (2) “grass, hay’. Cf. ues- (5) and ueser- (1). WP I, 311 (Radical in) Hitt. wesis, s. ‘pasture; OHG wisa, G Wiese ‘meadow’; Tokh. wäert, s. ‘grass’; MIr. fér, Ir. féar, m. ‘grass, fresh pas- ture’; OBr. guer- ‘mowing-grass’; W gwair, pl. gweiriau, m. ‘hay’; OCor. guer beside Cor. gora, collective: guyr-af, cpd. ‘hay’. (Myce- , naean has wearejo-, epithet of tables and chairs: “of rushes’? Hes. uphéar, n. ‘mistletoe’ 1527 here?) ués- (1) (ueies) ‘we’ (‘you and P). Cf. ues- mens, WP I, 220, and mes Skt. vayám, id.; Av. vaem, id.; Tokh. A was, B wes, id.; Hitt. wes, id.; Gk. cf. hé-meis, acc. sg: hē-mãs ‘we; us’; Go. weis, OE wë; OHG wir; Du. wij, we; Fris. wy; ON vær, væri & veri, id.; OCS (dual) vé, id. cf. Li. ve-du, id. ues- (2) “breath, air, breeze, cool, fragrance’. WP I, 222. Extn. uésm- Skt. vàsah, m. ‘perfume’; vasáyami, v. tr. id.; vasin, adj. ‘fragrant’; Gk. cf. à-ema, n. (^wind', if fr. *sm-uésm-); Du. waas
---
ues- \(5\) leaf 841 ::  f. “garment usu. adj. 1 veshém ('clad', fr. *yuesim-) uesmn- (-men-, -mon-) (3) (?) ‘wetness’. Cf. ues- (5) Gk. cf. di-iemi, v. (2) ‘soak’; di-émenos 'soak- ed”; Ir. feamain, f. ‘seaweed’; W gwymon, m. 1529 id. (fr. Irish, w. preservation of -m-?; LW in Fr. goémon); (o-gde in) MHG wase, wm. ‘Jawn, turf uésmn- (uésmos, à) “breath, breeze, air, va- pour’. Cf. ues- (2). WP I, 222 Skt. vasanam, n. ‘fumigation, scenting'; Gk. cf. á-ëma, n. ‘wind’; Du. wasem, m. ‘vapour’; Latv. vēsma, f. ‘breeze’; Li. cf. vesumas, m. ‘coolness’; vesumáà, f. «cool place’ uesnà, is ‘springtime’. Variant of type uesor- (1) Gk. cf. enis, gs: -ios ‘yearling’; Lat. cf. ver- nalis, adj. “of spring’; OCS vesna (and com. SI.) ‘springtime’ uesnom (uosnom) ‘price’. Cf. ues- (1). WP I, 311 Skt. vasnám, n. id.; Oss. cf. wäi, s. ‘sale’; Hitt. cf. wesiya(s), s. ‘cost, price’; Arm. gin, gs: gno, s. id.; Lat. venum in — dare ‘sell’; venus, gs: -üs, m. ‘sale’; Umb. cf. (?) uestisia *JJibation'; OCS venjo, -iti, v. (1) "sell uesnt- 
---
uesos leaf 138 :: er scented plants, cf. sélinon) dhuésnom, à (dhués-, dhuésmà) ‘wraith; spirit abode’. Cf. dhueso, dhuesos, dhus-. Cf. WP I, 867 OLat. fésiae; Lat. feriae, festus; cf. Féronia (epithet of Juno); Osc. fiíísnu ‘temple’; Li. dvesnà ‘wretch? beside dvésena ‘domestic animal that has died’; Latv. cf. dvesma ‘breath’ dhuéso, ið “blow, breathe, expire, evaporate, turn to spirit. WP I, 845 Skt. dhvasye, dhvámsami, pp. dhvastáh “fall, fail, perish’; Alb. deh, dej ‘intoxicate’; MLG ver-dwasen, MHG -twasen ‘besot, destroy’; Du. -dwazen ‘infatuate’; dwaas ‘foolish; fool; OE dwæsian ‘become silly’; Li. dvesiù, dvēsti ‘expire’; dvesu, dvesti ‘choke’; Latv. dvešu, dvēst ‘breathe, gasp’. The Skt. form dhvam- sāmi and Li. dvẹsu represent a nasally infixed variant (*dhuenso) dhuésos, is, iom, ios, io “breath, vapour, spirit; inspired, mad’. WP I, 845 Skt. cf. dhvasirah ‘strewn, dusty’; dhvasrah ‘drooping’; Gk. cf. theion, theion ‘sulphur’; OLat. fesiae, Lat. feriae, festus beside ferus, adj.; cf. also feralis 
---
uesos leaf 138 :: cf. also Gk. borós & leía, léon. Oscan forms are ambig. *dhis-?) dhuesro- (dhuesoro-) see dhueso, dhuesos above, and cf. dhis- Skt. dhvasrah, dhvasirah; Lat. Februus (epi- thet of Pluto); februum, n. pl. februa 'puri- fier; atonements for the dead’ dbuidhurà (dhuidhrà) ‘shag, fringe’ Gk. sísura ‘shaggy coat; Lat. fibra ‘shag, fibre, fringe" beside (dialectal) februa ‘tufts on judge's cap’. (Ir. fabhra ‘fringe’ is LW) dhuimor- (?) ‘darkness, shade, phantom’. Cf. WP I, 842 Ir. diamhair ‘darkness, mystery; OE dwimor ‘phantom, illusion? dhuinó ‘wane’. Cf. WP I, 835. Cf. tuin- (Lat. fünus is preferably fr. tuin-, q.v.); OE dwinan ‘pine, waste’; Du. ver-dwijnen (fa fusion of *tui- and *dhui-. VW), id.; ON dvína ‘dwindle, subside’; Norw. dvine, id. dhuis- (radical) (turning-up of the nose, acrid stench, smell Gk. cf. various (aromatic) plants: síon, sí- nàpi, sí-sumbron, beside simà ‘with upturned nose’; simos ‘snub-nosed’; (perk. also) si-khós ‘disgusting’; Lat. cf. suf-fio ‘fumigate’; fimus ‘du
---
uesos leaf 571 :: i. keturi?) queso, gs. of type quis, q.v. WP I, 519 Homeric téo, Att. toü; OHG hwes; OCS česo, id. quesos, à “time, hour. WP I, 508 Alb. kohë, f. ‘time’; OCS (and com. Sl.) Casü, m. id. quét- (1) ‘reach, attain’ (?) Cor. pejya, pesya 'peZa', v. last, tolerate’; W cf. pedw, m. (1) ‘completion’; Li. ketas, m. “aim, intention’ beside kétü, éti, v. ‘intend’; késlas, m. “intention” quét- (2) lurk’. Cf. (1) Skt. cf. Cátat, pres. p. (hiding, fr. *quetnt-); čattáh, pp. ‘hidden’; Ukr. cf. čaty, pl. trecon- naissance’; čatuvaty, inf. ‘lurk’. (Isophone: Alb. sos, v. ‘exhaust; finish") (queteros (1), thus only in MHG wéder *which of two'. Cf. quoteros) queteros, à (2) (quetros, quetrà) *hind-quart- ers, withers' Cor. pedren, pl. pedrennow, id.; Li. keterà, f. (1), id. (NB.EME withers, id. displays no trace of initial *qu-. G Wider-rist, id. ambig.) quetosrio, fem. form of type quetuór-, que- quérsnos (qursno-) — quo 20 25 30 35 40 45 1030 tur-, q.v. Skt. Catasr, Catasrí, id., W pedair, Br. péder, Cor. 
---
```


## [2026-10-17T00:01:32.732Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f'); print(len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'\\b158[0-3]\\b',p): print('leaf',i, re.findall(r'\\b158[0-3]\\b',p))\nfor m in re.finditer(r'[uú][sšṣ][tṭ]r[aā]',t):\n    print('leaf',t[:m.start()].count('\\f'),'::',t[max(0,m.start()-300):m.end()+300].replace('\\n',' '));print('---')\nE"
}
```


### [2026-10-17T00:01:33.511Z] TOOL RESULT

```
858
leaf 200 ::  I, 657. Cf. ghrendk- and ghrndh- Gallo-Latin grunda ‘roof; sug-grunda ‘eaves’; Ir. cf. gronn-lus, s. ‘groundsel’, lit. ‘ground- herb’; MHG grant, gs grandes (1) “base”; Slo- vene (?) grod “four-handled carrier, bier’; Li. grañdas ‘floorboard’; grandà ‘plate, sheet’; Latv. grodi, mpl. ‘well-top, balustrade; but- tress; foundation’. (For G Grand, R grùda, Cz. hrouda, see guhrondh-) ghrondhos, à (2) ‘container, bosom, paunch’. Cf. WP I, 657 Arm. argand, a-st. womb'; MHG grant, gs grandes “holder, trough, cupboard’; G Grand (2) *wort-vat'; OCS grodí ‘breast’; Cz. hrug’, id.; cf. also Slovene grod *fou
---
leaf 249 :: 5   432 distinguishes relationship from content, as in Cz. krevní ‘relating to blood": Li. kraujinis, id., cf. the Ligurian river-name Beverin (in the Engadine), and the Sequanian aidrini “bright in the Coligny weather-diary, cf. Gk. aithrinós “of early morning’. The passage from adj. to noun is illustrated in Arm. grean, gs greno Cliterature': gir ^writing"); cf. also Per. pūst- in (ffurcoat? :püst (fur); Gk. eruthrinos Ca red fish": eruthrós); Alb. dulli, gs dullini (ju- niper, lit. ‘fragrant bush’, cf. dhülos (1) above); Lat. scrinium (^writing-case' in rela- tion to scribo); sterquilinium (tdun
---
leaf 354 :: lope’. Cf. Klitis. WP I, 490. Cf. Kleii, etc. Skt. $ritáh “attached” (isophonic, but possibly a different root); Gk. klítos, gs -eos, n., and klitüs, f. ‘slope’; OHG fita, G Leite, OE hlip, pl. hleobu, n. *mountain-slope, cliff; ON cf. i-st. hlið, hlíó, f. “side; slope’; Latv. slita “log- fence; balustrade'. (NB. The above forms co- incide in some instances with a type *klitis, kleitos, with velar initial). (Kliuos ‘slope, ridge’. See Kloiuos. Lat. ambig.). WP I, 490 Olr. cu ‘ridge’; Lat. (ambig.) clivus, -um ‘slope’; Li. (*-ei-) cf. Sleivas ‘awry’ Kloii- (Kloin-) ‘Iean, slope, tilt. Variant of typ
---
leaf 466 ::  W nyddu, Br. néza, id.; cf. W nedd, pl. nydd, f. ‘spinner; whirligig; OHG naen, MHG najen & næwen ‘sew’; Du. naaien, id. nek- ‘negation, not-?. Lat. ambig., cf. neko, nekus Lat. (?) neco, are, pf. -ui (kil. Semantics of Li. naikinti «destroy'?, but see below: neK-); W neg, pl. ion, m. “barrier, frustration"; negio, inf. ‘frustrate’; Big. nekam, v. “say no; deny neksos, us (1) “bond, tie’. Cf. nekstos, naskos & neKsos. Variant: nesk- Tokh. (?) nasu ‘friend’; Lat. nexus, gs: -üs, m. ‘tie, band, bale’; Ir. neasc, m. id. (beside nasc ‘collar’: Br. nask); W nais, pl. neisiau, m. id. beside naith, pl. 
---
leaf 466 :: . W nedd, pl. nydd, f. ‘spinner; whirligig; OHG naen, MHG najen & næwen ‘sew’; Du. naaien, id. nek- ‘negation, not-?. Lat. ambig., cf. neko, nekus Lat. (?) neco, are, pf. -ui (kil. Semantics of Li. naikinti «destroy'?, but see below: neK-); W neg, pl. ion, m. “barrier, frustration"; negio, inf. ‘frustrate’; Big. nekam, v. “say no; deny neksos, us (1) “bond, tie’. Cf. nekstos, naskos & neKsos. Variant: nesk- Tokh. (?) nasu ‘friend’; Lat. nexus, gs: -üs, m. ‘tie, band, bale’; Ir. neasc, m. id. (beside nasc ‘collar’: Br. nask); W nais, pl. neisiau, m. id. beside naith, pl. neithion, m. ((2) “betrotha
---
leaf 788 :: n, period, manner”; W tro, pl. -ion, m. “turn, time, lapse, period, walk"; Cor. tro, pl. -yow, s. “turn, time"; MHG (ambig.) drap, bes, sm. ‘trot’ (but cf. Du. draven, v. ‘trot; Fris. drave (!) and G traben, id.); Pol. trop, gs. -u, m. ‘track’; R tropà, f. *path, way' tropos, ios (2) "inhibition, frustration’. Cf. trp- (2) and WP I, 756 Skt. trapa, f. ‘shame, shyness’; OE cf. prafian, v. (1) ‘restrain, reprove’ cf. E dial. to thraft, id.; Norw. cf. treven, adj. ‘sullen, dull’ troqueio (1) ‘turn’. (Variant: torqu-) Myc. toroge-, id.; Homeric tropéo, Gk. tropáo, v. id.; Olr. cf. trochal, s. ‘sling’; 
---
```


## [2026-10-17T00:01:43.189Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(850,858): print(i, re.findall(r'\\b1[5-6]\\d\\d\\b',pages[i])[:5], pages[i][:150].replace('\\n',' '))\nE"
}
```


### [2026-10-17T00:01:43.997Z] TOOL RESULT

```
850 ['1543', '1544'] WP I, 259 & 577 Gk. mus, s: -ios, mf. ‘son, daughter’; Lat. cf. vin-dex, gs: -dicis, m. (lit. ‘speaker on behalf of a friend"); Ir. fine, f. ‘clan’; c
851 ['1545', '1546'] “man, husband, hero’. WP I, 314 Skt. viráh “man, hero’; Av. viro ‘man’; Tokh. A wir, id.; Gk. (Pelasgian ?) cf. Ka-beiroi (*metal-workers' if fr. *káu
852 ['1547', '1548'] rul-entus ‘poisonous’. Cf. OE wode-wistle ‘hemlock’. (Isophonic: Mir fial ‘modest; W gwyl, id.) uisolos (2) (uislos, us) 'abundant, produc- tive’. Cf.
853 ['1549', '1550'] - sure, acceptance'. Cf. uoit- (2) Skt. vitáh, adj. (2) id.; vitíb, f. ‘pleasure’; Lat. cf. Vitula ‘goddess of mirth’; in-vitus, adj. 'un-desirable'; 
854 ['1551'] Skt. vívakmi, v. ‘say, speak, tell beside vávak- mi, id.; (Hitt. wewakhi, v. see ufuék-); Gk. cf. en-ípto, v. ‘reprove’. WP I, 245 uluerá, is ‘squirre
855 ['1552', '1553'] Lat. liquor, gs: -óris, m. ‘fluid’; MIr. & Ir. fliuch *wet'; OBr. gulip & guilp, id.; W gwlyb, m., gwleb f. id.; Br. gléb, id. S-extn. in Lat. lixa, f
856 ['1554'] bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelated) (ulio (1) ‘wind, wrap’, see uluið; (2) ‘boil’, see ulāið) ulksuos, à (ul'suos, à) (?) 
857 [] (1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wylian 'seethe? beside wyllan, v. id. (fr. *ulnio) ulquátis, os *tearer,
```


## [2026-10-17T00:01:48.792Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'vohun\\|vohü\\|vohu-n\\|vohvn\\|vohünl\\|vohuna' BRT.txt | head; grep -n -i 'uštr\\|ustra-\\|uitra\\|ustr[aə]' BRT.txt | head -20"
}
```


### [2026-10-17T00:01:49.303Z] TOOL RESULT

```
2470:—  dgL:  al/s  giuS  urvä  raostä  .  .  yüzim aiibyO  (yiimX. gaobyd)'''*  ..  aogS  data  Y.sp. 10;  —  spintä  ma'myS  .  .  xia'irä  .  .  vohü mananha  .  .  aHbyö  (AbL)  .  .  Y.  4!j.  6 ;  — yastat  mtzäim  Aan>ntl  nöit  däitl  yS  it ahmüi  3r7zux'iä  (sd.)  nä  däiti  Y.44-J9', — -  'ia/aAyä  mahränO  . .  ahyä  . .  Y.^2.14; 43-9, 49-1,2,^6.3, 40.  s';  — -ahurSmazdt'
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
3619:•  g.  a-paourvim  Adv.  'in  noch  nicht  da- gewesener Weise,  wie  nie  zuvor":  yS  va aia  ufySnl  tnanaüa  vohü  ap'  mazdqmcä.. "der  ich  euch,  o  A.,  besingen  will  wie nie  zuvor,   und   den    VM.   und   . ,"    Y.
4142:frarmilY.  46.2;  —  ysi  im  ßrasSm  (sd.) *hrinaon  'Aom  Y.jo.^;  s4-i5,  55-6t Yt  ig.  II',  19,  89;  —  ai^e  "»Äius fral0.car7%rh  (sd.)  Aog.  6g;  —  zaota  asava °nhSus  Yt.  jo.  137  (?).  —  2)  vom  geistigen Leben*':  at  hii  mazda  'hüm  dadat  ahurö ahmäi  galiA  vohü  frsdat  mananhä  "es wird  ihm  MAh.  das  (andre)  Leben schenken,  ihm  wird  VM.  Haus  und Hof  fördern"  Y.46.13»;  —  .  .^ß;'>«(sd.) karapanS  akais  syad^anäis  'hüm  nunngn- dySi  maslm  Y.  46. 11»;  —  yS  'Aom  i/asas aibi  "wer  sich  um  das  (andre)  Leben  be- müht, (dem)  .  ."  Y.  j/.  19.  H)  mit näherer  Bestimmung  durch  Fron.,  Adj. oder  Gen.:  tim  *va  °häm  dngvanW iyao- ':ianaU  ^9is  dams  nadat  (sd.)  Y. 31.20; verwend.V.5.62(s.A3); — alyastä{sd.)'ABm yj  vaT3h3us  manauhs  Y.5_j,  5.  A)  ins- besondere I)  mit  a)  astvant- Ad].,  b)  paou- ruya-  Adj.,  c)  o-  Fron.,  d)  üyejakvatU- Adj.;  a)  'das  leibliche,  materielle  (irdische) Dasein,  Leben':  ka^a  apajasB  .  .  asir'atal haca  'tihaot  manahim  avi  ahUm  H.  2. 16;
5456:'gedeihen  lassen,  fördern':  däiä  ar?h3us andat  (Ko.)  vohü  manaahä  Aathyilvar/- tqm  (sd.)  Y.  50. 1 1 ;  —  >r»dat.'.
6065:31.  2;  —  vohü  xsdknm  , .  bägmt .  .  *vidl- bmnäi  (sd.) . .  'sä  (Instr.)  antarp.taraiti vahistsm  Y.  j/.  i ;  —  gültä  y}  'hm  mantd aham.bi/ (s±)  Y.3i.ig;  —  aj  .  .  's'ahyä ma  ..  manyäi  (sd.)  Y.43.1}; — yOinSit'üm mainyatita  (sd.)  aäbyS. .  Y.34,  8;  —  'hm manyä   (sd.)   vahehyä   Y.j^.  9;   —  yqm
6075:—  h3  dd'iS  'Aw  upaj-aooayeite  (sd.)  yd  xsa'^fjm/a  Y.  2<?,  1 1 ;  —  vohü  iwil drvaite  *daöiliti  P.  50;  —  vistäsps  'sähe  manauha  rcha  'iwä  'sä  patrT.jasSmaiäg hamayä  iaisfmnS  (sd.)  Yt /p.  93;  —  i-Jj- ■  Y.  j6'.  4;  —  at  ySng  'säatca  vöistä  vat*- taspahe  .  .  yS  .  .  'ssi  ravB  yaisa  (sd.)  Yt  hSu^lä  manauhs  pr^^iuSng  (sd.)  Y.  28. 10; '.?-99i99i — yd 'saht  cintnaiastsmS  atihat  \ —  'sä  (Instr.)  vS  anyd  ainim  (sd.) P.  4^;  —  frsaaiti  's'pm  P.  24;  Yt  6.  i,\vJfltighatü  Y.5J.  5;  —  ^?  -  -  dayat  .  . Vyt  ;5; —  'Sake  datsis  vahistahe  F.  4  c;  vahista    astm    (sd.)    "säi    vohs    xsä^r^m
6093:—  hvd  nJ  mazda  valtt  'saica  car3kir>%ra (sd.)  sravayetihl  Y.sp.S  {VM.  spricht);  — ta  v!  vohü  tnatuwha  'iaica  savai^*avlit (sd.)  Y.$s.  I S ;  ^  apanS  (sd.) . .  ä  xid^rtm rarihius  manatjhs  °/iJt  ä  ^^2S/(sd.)  päitö ^■33-  5 i  —  '"^"^  gatdr  maitan/hä  daidl  ^-sa (Instr.)  *dä  '*>  dangäyü  snrväii'  (sd.)  tu ti.voai/  mazda  Y.2Ä6.  c)  neben  Ahura- Mazdah  und  VohuManah  yöi  vi , .  särmig ahurö  *°jä'*'. .  ttX'-ais  vanhSu^  mananhö Y.J/.  3  (s.  1  aa);  —  anais  vä  nöij  aAura
6095:—  anyS  °iät  haiatcä  masda  ahura  asda (sd.) . .  fohi/täatca  mi7«aw^  Y.50.  i;4;  — tatcä  vohü  masdä  iraotü  manauha  sraetB (sd.)  'sa  (als  Subj.)"  güiahva  (sd.)  la ahurä  Y.4g.  7;  —  yesi  a^ä  sta  haiixm (sd.)  masda  'sa  (VoL)  vohß  manavhä  Y, 3-f-6;33-7,34- S.i". 7;  —yBiim . .  aAura., 'sa  . .  vohü  mananhä  Y.  2^.  10;  —  "sä,, vohü  manavAä  , .  mazda  ahurä  Y._j/.  5, 4g.i2\  —  vohü  maitanha  .  ,  'sä  mazdä V.  48. 1  a ;  —  voAü . .  manar^ha  , .  xsmakai (sd.)  °ja  vaAmäi  masdä  ahurä  Y.50. 10;
6096:—  vohü  , ,  manaaha  . .  masdä  '/a  Y.  33. 8;  —  °M  masda  . .  vohu  manauhä  Y.^. I ;  —  masdä  .  .  vohü  mananhä  'faia  Y. 34,  1 5.  d)  neben  VohuManah  und X/a'ira:  ahmäica  .xsa'hra  (sd.)  jasai  (sd.) manatfha  vohü  'säcil  (als  Subj.)^*  Y._J0. 7;
2899:•  j.,  g.  'ao}ah-  n.  '(physische)  Kraft,  Stärke': asistim  narl  alaotw  °Jö  Y.  60. 3;  —yakmi niyne  nars  'Jartha  Y.  /o.  a ;  —  ai-avaia '}arfka  yaia  yal  panca  narS  "mit  solcher Kraft,  als  wären  es  fünf  Männer"  V.  jj. loPaZ.;  Yt,2.i2,  14;  —  usla  U yd  ä"j 'jaiika  vasöjciairä  ahi  haoma  Y.9.25; —  kacaiti  dim  aspahe  "Jö  uitrahe  °Jö vlrahe  °j<>  Yt.  it).(i&;  8.2^^;  —  "jö  tanvö vispaya  Yt/.^.29;  —  -jö  vJspdMnüM  Y. 5.17;  —  drfahela  paiti  °)arakö  Yt,  i_j. 134;  ~-  y~'  itfsfro)  arinam  ..  matilüm 'jö  abaraiii  \t  14.12;  —  apa  .  .  buei'ä- °}5  , .  barahi  apa  pä',ayä  sävar»  Yt.  10. 23;  62;  —  haomö  asibil  yöi  ..  zävari "jssca  baxhili  Y.  9. 22; —  °Jasca  nn- S«)Wf'a..Y.  77.8,  yi.j.22,y.i,Y.  72.6;  — yS  nü  asSif  °janAil  vandayaÜJ  (sd.)  ., gae^am  Y.50,3.  a)  AS.  °jö  als  Adv,
3112:rim  stagr»m  (sd.)  arijö  V,  7. 41;  43'; —  uitraAe  k?hrpa  °yehe  P.^2;  —  aspahe paiti  arshö  °yehe  "um  einen  Rosshengst erster  Qualität"  V.9.37;  37';  —  dvada- satih£ir3m  (sd.)  asti  "rim  ayan  F.  27  b; '";  —  'krisatdkw)m  frasnütse  .  .  "yqtn paiti  usnaitJm  ".  .  (also)  mit  Abwaschung erster  Ordnung"  V,  Ä  98  (?) '' ;  —  mi>nm  . . taxm?m  mainyaam 'rJmYtw.i 40.  [P. 32:  lies  ayryö.mdaimasl°.'\
3116:•  j.  *aj'ry5.!na8imastflma-  '>  Adj.  'der  in der  Hochbninst  brünstigste',  vom  Kamel- hengst: ustrake  ktkrpa  ayryehe  °mahe P.J2.
3400:—  tara'^ustrahe  . .  paoiryäi  'rune  .  .  ra- >ais'tai  .  .  västryäi  ßuyänte  YLij.  88; iij.%  {'runalca),  V.J.  57,  58,  y.  44-  45. J4,8';  —  västrye/ie  JSuyantö  .  .  ra>aSstä ..  •rutUf  (GS.)  raiüm  Y.i^.3  f.;  Vytj,/ö", Az.$; — 'runqsca*^  ra>aistisca  vastryqsca ..ßuyaniö  Y.  13. 3 ;  Vr.j.  5 ;  —  'rufum  ya^a ra:iaestär>m  Yt2.i3(?);  12.
3817:•  j.  aiwi.ta£ina-  i)  Adj.  'heranlaufend, anspringend'  zur  Begattung,  vom  Kamel- hengst:  ustrake  vmairyaos  ,  .  °naAi  Yt 14.11.  i)  n.  'Herzulauf,  Anlauf  (nur Komp.).
4181:^ustraAit  .  .  °yaos  osaHnarthü  Y.  24-  St  ^^■
4678:maca  *frast3niite  .  .  ditSi  °iiye  (NPm.)  .  .  'nyeke  räkWB  V.  7.4.  I  i)  wiederholt *vaäsäz*/ramravainti..vTspa^qmia  aiwi.'  'Aex  eine  .  .  der  andere';  dsityB  *'inyS'^ srurwai/i  (sd.)  K.60;  —  aivB  pants  yB  havam  {^d^  *daityö  ^'inyB^  ya'ia  *va  . . a^ahe  vTspe  'nyalhm  apatitqm  {%A.)  \.y2.  li.107;  P.57;  —  yal  he  pukra  us^zaydi^e 11;  —  ^pasävi^  adam  käram  ..fraisayam  , .  .  tiaisB  'nys  .  .  aat  'iiyB  ,  .  Y.5. 10;  — hyt^  upa  mäm  äkJ* , .  hyJ^  °niyJ'  kärJ'  avi  *'iiy3^^  suruiiraiti  (statt  Du.)  nsil  'inyS ".  .  reliquus  exercitus  . ."  Bh.^.6;  —  eä  'S. 24;  — yay^  osH  'nyS  rasnus  razUtB asti  masyB  ..  an^rn  datpm  ..upairi'tiyai^'W.J^.^'PüZ.  (unvollst  Zitat);  — \,°myam sraväis  .  .  !  .  .  ya'^a  zrayB  vountJtahm '  (näml,  käram)  *ustrabilrim  akunavam upairi  °nyh  äpB  V. §.32{.;  —  vayaol . .  'myahyJ  aspilf^A^ paiiyariayatn^'Acnem^a taratatB  (Stverz.)  'tiysis  (als  APn.)  dämqtt  \  Teil  (des  Heers)  machte  ich  kamelberit- Y.22. 24;usw.; —  \' a^urcrmazdämaiy  upas-  ten  .  ."  Bh.7. 18'';  5. 4;  —  armaeflä  'iiyA
5554:mnbyascä  näiribyasca  xara>ustrahe  za-  »j.  aurva- Adj, 'schnell;tapfer">:  ^«rffli^^iT tshsus  raßoräi  manaahS  "het  komme  Ae^  aiWü  'vS  \X.4.q;  —  Iqm  yazjitta  'va liebe  X  zur  Unterstützung  zu  den  Männern  hunavSvalsakaya\\..$.t,T,i^;—iS>:riv!Ht und  Frauen  des  Z,  zur  Unterstützung  des  "'^"p«  Yt/0.109;  14;  —  'itwam  yazfmU guten  Sinns"  V.54,1.  "i-ätihs  ahuränhs  VL5.85;  —  yat  bäun
5638:5.120;  —  ustrane ..  yö -snam  ..  mattstem  i_  «,•„_;,_   ,,7,7-,   S  "  18    Vo  z";-    ■
5828:•  j,  astvat^rsta-  m.  EN.  des  dritten  der drei  Söhne  Zara^ustras,  die  aus  dessen; im  See  Kasaoya  aufbewahrten  Samen hervorgehen  sollen '' " :  uxsyatjtylahe  .  . uxsyai.mmanhs . .  'Iahe  aiaota  Yt  13. 1 28; HO,  117;  —  yttt  'lö /raxstäile  haca  apat kasaoyät  asts  mazdä  ahurahe  vjspa.taur- v'ayä  (sd.)  pu^rif  Yt.i5.92;  —  Aaxayif.. Hahe  vjrihrayne  Ytig.^s;  —  {'laAe)  ys atiAai  sao^as  (sd.)  vtrüraja  nama  'fasca iiqma  . .  ava'ha  'tS  ya%a  astva  kam  usfa- nava  (sd.)  astval  *aihyejahim  paitisät  Yt. JJ.129.
5830:•  j.,  g.  ast'vant-  Adj.  (fem.  'vaitt-)  'mit einem  stofflichen  Leib  versehen,  leiblich,  | stofflich,  materiell';  Ayat  'vant»m  dada uäatam  "als  du  Leben  mit  Leib  versahst" Y,_5/.  11;  —  tat  (näml.  mlidf/n)  er  mazdä vairlm  'vaits  ustänät  data  vatfhlus ^ttoiana  manar-ks ySi . .  "diesen  köstlichen (Lohn)  ja,  0  M.,  werdet  ihr  durch  das Wirken  des  VM.  dem  leiblichen  Leben (derer)  verschaffen,  die  . ,"  Y.54. 14;  — •vat  ahm  hyät  uslStiä  (sd.)  aojSrigAvat "^.43-  16;  —  ash-atjrmya%a  astva  *kqm ustanava  (sd.)  °vat  *ai^yeja/nm  paitisät Yt.  13. 1 29;  —  *vTjvähu  (sd.)  paiii  tanusti 'vh  gays  *däryeife  FTVf.4.2.  A)  sonst. nur  als  Beiwort  von  a)  stay-  (sd.) :  zara- , %ustrahe..yS paoiryö  stsis  'vadyä ..  Yt.ij.  1 Sgf«.  b)  gai^ä-  (sd.),  Sg.  und  Plur.J darfsca  (sd.)  da^at^amirixfyantim  vTspatn yam  "vaitlm  gae^qm  Yt  i<).  94;  Y.  g.  8, 37.23,  *Vd.£'>;  —  zarai:mtr5  ratus 'vai>ya  gaf^ayä  Yt.  73.  4r;  j.  89;  — kat»  %wqm  paoiryS  'vai^yäi  hunüta gai^yäi  Y.p.  3;  4;  —  m/l  m?m>cainTs gai>a  'vaitls  asake  SrB._j;  Yt/5.  41,  V. , ^^•SS;  —  "J  ^^  apqm  a'javö..  jasanli..' yavanqm  .  .  västranqm  ,  ,  gafianamüa 'vaitinqm  Yt  ^'.29;  —  V?'"  ■  ■  /rävavacä .  .  zara'iuströ  gae'iabyö  'vaiHbyS  Y.ö'j.g; P.  13;  —  ahura  mazda  mainyö  spinista däiar>  gad'^ariqm  'vaitinqm  asäum  ''" I.  7- 1.  9- 1,  lo- ".  "■  I.  '4-  I,  34,  K
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  —  sardiiustrahe  .  .  yd  paoiryö  .  . Staat  'Lm  naist  daivS  Yt.  13. 89;  —  yal  nä . .  %ris  "s^n  ufajtuyät  V.  18. 43 ;  —  "hmca *!0  pasca  hü  fräsmSJaitim  (näml  stuyät od.dgl.)  N.  6"^;  imd  so  Öfters.  a)  auch  mit a)  vanhav-'h  aiwi^r^lmahi  's>m  voAa  Vr. J7. 1.  ß)  vaAista-'^:  ahun^mca  vairitn  .  . °s?m(a  vahUtim . .yeAhl.tiätqmca\.6i.\\i3. 8,'Hyuf.S;—jainii  mqm  ahuna  vairya  ..lapa- yäti  mqm  'la  vakUta  Yt/7. 20;  —  6ayqm 'iahe  vahistake  yazatnatde  'sähe  vahÜtahe yasamaide  frasraeimmca  .  .  Y.  20.  5;  — zara^uitrS  ys  paoiryö  .  .  staota  °sfm  ya^
6189:Gen.  subj.  und  obj.:  alsm  *d>nidyäi{iA.) .  .  rayS  'st/  ". .  jrXoiiTOU  fioi'pai"  Y.  4J.  i ; —  abifra  (sd.) . .  ya  vaahsus  'sis  mananha Y._3i5.i3;  —  aiahya  yasa  {%A:)  'slm  y am iiyam  Y.  54.1;  —  °M/a  ^ae^ananqm viäu/(sd.)  ahurakya  mazdS  ".  .  des  AhM. Belohnungen  fiir  die  Taten  . ."  Y.2<V,4; — ■  nöit  kl  "M  *^ao^nanqm  vimysit  N. 16  ij);  —  zard>!ustrahe  .  .  asatinS  'itmia fravaiimca  yazamatde  Vr.  16. 2 ;  2,  Yt  13. 95;  —  tti  ahmt  nmane  Jamyarps  yh  asao- nqm  xshätas/a  'sayasca  . .  paitisatitayasla Y.  60. 2.  a)  mit  vanAav-  Adj.  und  aka^ Adj.  näher  bestimmt:  vatfkttyascä  °Ssi/ .. yS  ns  ara^ä  (sd.)  irmavaia^a  asanhäxs ^■5^-3't  —  syao^ana  mizdavqn  (sd.)  .. akfm  akai  vamthlm  'stm  vanhaavi  Y. 43. 5 ;  —  tSm  vatmklm  yasä  (sd.)  °sim  Y. 5;. ai;  —  maifyn  siaya  ahm  vaaAuya 'st  gaui  (sd)  Y.5/.  10«;  —  xmBth  afn- n>ntu  ahmya  nmsne  vawtklm  °/lm  i^a- parqm  Yt.  /J. i  S 7 ;  —  vaauAlsca  aöa  vaau- klsca  'sayS  Y.53.3;  —  yhca  tsi  gmh *aiura.mazda  ..  iSä  . .  vanukim  iihl/  'lim . .  ihm  .  .  *panndlm  yazamaidi  Y.^S. if  b)  Du.  'die  beiden,  beiderlei  Lose', d.  i.  (das)  gute  und  (das)  böse:  tmnanha (sd.) y5  dä%alibyd  priLratüm  xsayqs  'äfä*"^ üista  ". .,  der  über  beiderlei  Lose  gebietend den  Klugen  den  wahren  Ratav  versprochen hat"  Y.57.5.  A)  als  Gottheit,  die  die Lose,  insbesondere  die  guten  verteilt,  im jAw.  als  Göttin  des  durch  Frömmigkeit  ver- dienten Wohlstands*';  I)  im  gAw,:  Siraosö 'sfi  mqza.raya  (sd.)  Aacimnif  ya  vT  altl *ran3ibya  savlfi(sd.)  vldayäi  \ .  4j.  1 2 ; -^ sraosS  .  .  yU  *'li^  haiaiti  *mqxaraya  V. 27.6,  Vr. /2.1;  —  ya  vldayaf  'sts' (HS.) räshqm  (sd.)  Y.j^.  la;  —  ys  fta  'sSis aojaifha  var>dayaita  yqm  ,  .  gai^qm  .  . Y.  so.  3.  a)  Du,  in  Verbindung  mit armaiay-  Du.  ^A.  und  Arm.':  yads  ahm zivlm  (sd.)  .  ,  mazdasca  .  .  'sicil  armaitl Y.31.^.  II)  im  jAw.:  yö  'lim  yazäite ..k5  mihnm  yazaiieY\..i-j.2;  —  -/j  (VS.) srlre  'si  banumaili  .  .  °li  dä'ire  vehäm i^arifiilYt.sy.^;  6of.*;  —  hm  hacSl  'Hl pourvsj^ä'iira'Yt  /j?.54;  — /rä  mqm  aiwt.- urvalsayatfuha  marsdik?m  'al  (als  VS.) hnzaiti  Yl  77. 1 5 ;  —  'lim  . .  darr/S.- variiman3m..bartntltn  vispä  baSlazsY.S'i. 2;  —  sraohmla  'lim  nairXmca  sauh>m IVyt.40;   —  fravalays   .  .    'Isil  balsaza
6254:—  syao%ami  razistä  (sd.)  ängvataicä kyai<ä  *'iaotii  yehyäiä  ASmunylsaitl  (sd.) mi^aAyä  yucä  ksi  är»svä  Y.  _jj.  i ;  —  yS vü  xsayqs  adqs  drTtä  ayanhm  urvatsis (sd.)  Vit  huiSntul .  .  ra/nä  jvqs  yS  'savä dr3gvant)m  Y.  46.  5.  a)  Ko-i  it  von Zara^ustra  (s.  2  c  a  und  drTgvaiit- 1  2  a  a) : y!  äyal  •iavanam  divamnsm  (sd.)  hsi  . . *dusji^arä^Sm  (sd.)  . .  ISm  *vi  ahSm  dr>g- vants..dams  «a<tf«/(sd.)  Y.^7.20.  b)  im jAw.:  kat  *sava . .  vanai drvantami  'idva vanat  drußm  °sava  vanat  drvantpm  Yt. I.2S;  —  x^ayamnam  '/avanim  däyata *axsyamn^m  drvant^m  Y.  Ä  5  ;  —  vasB.- x/a'iirB  kyüi  'sava  avasS.xia'^rS  hyäf  drvä Y.S.6;  —  yqm  'lara  ..  asayqm  (sd.) va^  tarn  drva  ^ihva  Vr.  22.2;  —  mt^nm ms  janyh  mä  yim  drvatat  pimanke  mU yim  n^adafnat  'iaoiiat  uvayä  af  asti  (sd.) mskrB  drvataica  'saonai^a  Yt/o.  2;  — pdhqm  %rvB.däianqm  jasaiti  yasla  drvaile yas^a  '/aofieV.  lff.$o;  — yai  azäite^sd.) tsm  ahum  pai'iyaite  yim  "soonam  yesi  nHii azUiie  tun  aAam  pai^yäite  yim  drvatqm V.  /Ä76;  —  drvatqm  ..  urvänS ..'läunqm V.  ig.  30;  —  ga>il  nmätiam  ^mr^yS  asti '/SvaoyB  (DP.)  naSai  drvatqm  Yt,7.4;  — hiiia  para  'saonqm  pa^a  urva/ai/i  iu^a drvatqm  Yt4.4;  —  narqm  vä  'saonqm kanjamanäis  drvatqm  vä  . .  kandvaranäü YLi/,4; — yai  •i'ava  para.iriiyeiä  . . yal drvä  ava.*miryeie  H.2.1  — 19;  7,  8,  10, 15*,  16',  18  {'iaonyäi);  s.  unter  drvatif- 1 1.  2)  sonst,  a)  im  gAwr.  (ausser GHapt):  zara'^usträ  kastl  'lavä  urva^S mazsi  magäi  (sd.)  Y,  46. 14;  —  tSm  (näml. pounicistqm)  . ,  varänl  (sd.)  .  .  yä  försi vTdäl  paüyaFcä  västryaHbyo  (sd.) . .  *°iapnj 'iavabyS  Y.  5J.4;  —  hvs . .  yas^a  vadarS (sd.)  vBizdal  'iauni  Y.^a.io.        a)  spez.
6264:lich bezeichneten  Personen:  frasaoslrs ''Opa  Y.7/.1;  —  'sava  jämäspö  N.Ä9; —  "hraMaomm  "Az/a»?«  FrW.  2. 2 ;  i;  — gayehe  mary^nH  °s'aonSY.26.5,  Yt/J.87; 95-138'",  Y.7J.7,  2(7.5';  —  Vä«m tu'taspa  Vyt.  4s;  ~-  hvüvi  'laoni  Y\..i6. 'S; —  kt^yä  'saonyä  Yt./^.  139;  139— 141'*;  —  »nsvä  sräts.sps(,a  'saonä  {GD.} YL/^.  115;  115,124, 125,127'.  A)insbes. von  Zara'^ustra  (Spitama):  zatS  bl  yö '!ai-a  sara'inus'tre  V.  75.46;  3,  4,  10,  Yl. i.104,  7J.41,  74.28,  Vr.  77. 19,  Y.77.13, ^■43^'t  Vyt  70;  — yS  'sava  zara%u/trd Y.72.6; —  'iäva  yäia  zara%ustre  Yyl..  2, Az.4;  —  *savat>3m  i:ara%ui'inm  V.1O.2, 71.1,  2,  Yt,5.i8,  76.15,  ^5-79.  81  (statt I^om.),  V.5.21;  —  *saonö  zar^uHrahe Y.^23,  76".  2,  27.1,  24.5,2S.o,S7.S,08. «.  77.2,  P.5Ö,   Vr.76.2,  Yt«2,  y.62,
6268:'laona^a  (statt  Gen.)  sarahustrahe  Y.  Ä I ;  —  'säum  (VS.)  zara%ustra  V.  2, 2,  4. 2,
6395:1;.  m.-ia.  m.  'Irrewerden'.  —  Pü.:  a^ra«^. '  mit  Asjm  begmnende) -Spruch,  das  As^im- u.j«^  (Transskr.).  —  O  Hds.  asae^aAe;  s.^Qsbtt':  zara'huitraAe..yahmi paiti  i-lsji)m.- »ber  Pn,  ma^r>m  'vS  vTsruyata  ". .,  durch  den  das
6513:^'.^qzj-aiti  wie   ai.  iccAa-   zu  ahd.  eisi-öii.  —   Brunst*:    ustra»h5  .  .    sainiMaofa    'nanha
6796:g,  6,  2 1 ;  —  'ns  vairy3  fraoxts  H.  7. 4 ;  —  '  J-  'ahuimant-  Adj.  'der  emen  Aha  be- tam  paoiryd  zara>ustra 'npfn  vatrlm  fra-'^'^^'  stets  neben  ra/»;«^;,/.  (sd):  *"».a/'> irävayJvTb>r^>wa>,tfm{%^),lxtairJm{sA.)  ratumai  vaktnmi  vaocata  wzs  tin%n  Aha apar?tn  xraozdyehya  (sd.)  frasräiti  V.o.  "°°  ^"^"^  *""  '  "^^  "^°°'^t  das  beste" i4;V.in.2,YtiQ.8i;—panra  'na  vairya  P-'^'?)i  —  'mais  raiumatö  alaonö  asahe JrasravaySisW.n.z;    77.6,   7Ä43,  70.  zi;   '•■^^Sa-J  Vr.7.5J>;  —   'm^^m  rafummism
6828:Leben  heilende  Richter',  von  Zaraiustra:  ySi  rS  fyaoiaiiais  särmte {?,&.)  »rJ  (s.  aa)«
```


## [2026-10-17T00:01:56.980Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'^\\s*143[345]\\s*$',p,re.M) or re.search(r'\\b1434\\b',p[:300]): print('leaf',i,p[:200].replace('\\n',' '))\nfor m in re.finditer(r'Blut',t):\n    s=t[max(0,m.start()-200):m.end()+100]\n    if re.search(r'voh|v[oa]n',s): print('leaf',t[:m.start()].count('\\f'),s.replace('\\n',' '));print('--')\nE"
}
```


### [2026-10-17T00:01:57.714Z] TOOL RESULT

```
leaf 781 tm    vanaintTmia    upara- ,    Ableit  am  v>rAraina:  —  0  S  368.  32, dby  Google 1433 v^ntdraj^tara- i-b •  j.v9r«*raJns'tara-  Adj.  'der  siegreichere' : aha  fiä  yS  äim  (näml.  haom^m)  s
leaf 64 e  fiir  den  Armen  sorgen,  die  all- tränkenden"   ^.38.$. «L  äghnyä-  1.  "Kuh'  (auch  von  Wulken  and Flütseu);  Bthl  AF.  3.  39'  —  Vü.-.  agjnjiä (in  Av.-Buchst)  mit  der  Erl.:  xön  'Blut';  vgl. zn  ma^ioHt: •  j.  a)Ta-  1)  Adj.  (fem.  °rä-)  'der  erste, obierste',  nach  Zeit,  Ra
--
leaf 86 rn  als  das Los  des  guten  Sinnes"  Y,j_j.  13''. Pü.:  pa  patikik.  —  ij  Vgl.  iSt.  GoK.  BB.  /J. 2S1. •  j.  aiwijiaptim  Absol.,  mit  asti  ('er  be- feuchtet*, sva.)  'er  besudelt  mit  Blut*:  yesi atshal  .  .  aiwi.n°  va  . .  aiwi.vaniim  (sd.) va  V'7,  la. Zum  V.  fffl*-;  S  5i  I
--
leaf 87 Lvanyah- bespuckt',  sva.)  'er  besudelt  mit  Speichel' '' : yexi  atthai  upaä^m  v3  aiivi.naptlm  va aiwi.iritlm  va  aiwi.v  vä  "wenn  er  (der Leichnam)  sie  (die  Kleider)  mit  Sunen oder  Blut  oder  Kot  oder  Speichel  besudelt hat"  V.  7.12. Zum  V.  vairi:  —  PS. ;  hakar  ast  tus  . 
--
leaf 129 r  Art  von  Körper- verletzung*': °sahe  F.25a. Zum  V.  %warji-.  —  Pfl,:  api  biirrUii,  erl.: .  ir7n  i  an  ämär  *ia  xön  hafas  äyrt  "ein  Schnitt  I von  der  Art  (eig.  'Zahl'),  dass  Blut  danach fliesst".  —  •)  VII.  eine  spezielle  Art  von  c^'ara- ta{il.vähuBi-{^^;  vgl.  PüErL •
--
leaf 366 'des  (bei  dem,  durch den  die)  Wasser  fliessen':  xsvföa  ätoiti  . . °apa  (ND.)  ux^yatunara  Y.i6.8'\ Pü.;  laäh,  äp.  —  •■>  Vgl.  iSt.  unter  la/.jp-. •  j.  taCat-vohuni-  Adj.  'wobei  Blut  fliesst', mit  i^ara-  m.  (sd.)  Term.  techn.  für  die der  Schwere  nach  zweite  Art  der  Kö
--
leaf 742   usta  vaahö bvat  Vytjo;  —  räia  f  maidahäta  aiaoru \yl36. •  j.  "ätara  vaohit  vanat^  (Sp.  1352  o.) V.7.S2  PüZ. j.  ditö  vaahiti  V.  /p.  17:   lies  dätan  vaah- •  j.  vaohutät-  t  'Blut':  aslqmia  vansamia spämamla  mOhrqmca  -tätqmca  Y.6.J;  29. Auffällige  Bildung  ('languini/ai",
--
leaf 786 ist  voAu  hier  das  selbe  Wort  ('Blut') wie  in  TioAu.gaana'.  —  a)  West  SBE.  J.  61, 184  'the  good  diffuser'  oder  'oHereT'.  Dst. ZA.  /.  J50  'reitcellent  ami'. ■  j.  vohuna-  m.  'Blut'. KompA-i  Ableit  —  Vgl.  vokaiü-, •  j.  vohuna-nliag- :  'na-zg-  Adj.  mit ^span-  m.  'Bluthu
--
leaf 786   'the  good  diffuser'  oder  'oHereT'.  Dst. ZA.  /.  J50  'reitcellent  ami'. ■  j.  vohuna-  m.  'Blut'. KompA-i  Ableit  —  Vgl.  vokaiü-, •  j.  vohuna-nliag- :  'na-zg-  Adj.  mit ^span-  m.  'Bluthund,  Hund,  der  auf  den Mann  geht':  kva  asti  spä  'naegS^'>  däityB.- g3tusi..yS naecim  isa
--
leaf 786   CrBd.: Utk  i  ramii  'Hecrdenbund'.  —  ')  Them.,  S  390. —  »  Pü. ;  *ie  ni  rü  x'ähll  hac  hunarän  <i  ä lau  :^äAil  sräyiin. •  j.  vohuna'vant-'*  Adj.,  nur  fem.  'vaifi- 'die  ihre  Blutung  hat"';  nsirika  ci%ra-\ vaiti  äaxstavaiti  'vaiti  V.  16.  i ;  —  näiri- 1 Aqm  .  .  °vait
--
leaf 786   des   V.   .  ."   Yt y.iis- Eig.  'der  (den  Göttern)  gute  Ehrerbietung  er- uaoAav-.    —    >)   Oder '  3  aufgelührte  K  mit einem  der  beiden  ersten  identisch  ist •  j.  vohuni-  f.  'Blut';  ■«<  F.^  h;  —  yai  . . •nTm  va  täcayänti  /rasaiifm  vä  froH- canti  Yt  14.  54;  —  auch
--
leaf 786 yänti  /rasaiifm  vä  froH- canti  Yt  14.  54;  —  auch  Plur.:  astssla  .  . ^maslnynas^a  '«jY^a  (AP.)  YtJO.  72;  — yezi  nairika  'als  (AP.)  aiwi-vainäi  yai  .  . "wenn  die  Frau  (noch)  Blut  (von  der Menstruation)  sieht,  wenn  .  ."  V.iO'.S. KompE  —  Vgl.  itiaahav-,  zvAuna-.  —  Vg
--
leaf 809 .  'dem  Wasser'*  feind- lich', Bezeichnung  einer  Klasse  von  Dagva- priestem:  yat  nurim  *ra  dalva  malyäka dalvaySsö  vokunTm  vS  tacayeinti  . .  "wenn jetzt  die  damschea  Vy.  . .  das  Blut  fliessen lassen  oder  .  ."  Yt74-S4- Ableit.  aas  *vyäm6av.  Adj.*)  (Komp.:  M-j- * amiav- i1 
--
leaf 849 r-,  m  Ende  gehen, vcrslreichen;  vorübergegangen,  verstrichen sein',  mit  Dat  der  beteiligten  Person:  ym näiriia  vohunT^  aiwixamat  yat  kl  %rayS xSafna  salante  "wenn  die  Frau  noch  Blut- spuren  sieht,  nachdem  ihr  drei  Nächte (darüber)  vergangen  sind"  V.  16. 8 ;  8, 5, 33, ig-
--
```


## [2026-10-17T00:02:03.020Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(780,788): print(i, re.findall(r'\\b14[34]\\d\\b',pages[i]))\np=pages[786]; k=p.find('vohuni-  f.'); print(p[k-100:k+900])\np=pages[742]; k=p.find('vaohutät'); print(p[k-300:k+600])\nE"
}
```


### [2026-10-17T00:02:04.091Z] TOOL RESULT

```
780 []
781 ['1433']
782 []
783 []
784 ['1430']
785 ['1433']
786 ['1433']
787 ['1436']
Aav-.    —    >)   Oder '  3  aufgelührte  K  mit einem  der  beiden  ersten  identisch  ist
•  j.  vohuni-  f.  'Blut';  ■«<  F.^  h;  —  yai  . . •nTm  va  täcayänti  /rasaiifm  vä  froH- canti  Yt  14.  54;  —  auch  Plur.:  astssla  .  . ^maslnynas^a  '«jY^a  (AP.)  YtJO.  72;  — yezi  nairika  'als  (AP.)  aiwi-vainäi  yai  .  . "wenn  die  Frau  (noch)  Blut  (von  der Menstruation)  sieht,  wenn  .  ."  V.iO'.S.
KompE  —  Vgl.  itiaahav-,  zvAuna-.  —  VgL mp.  (Pü.)  jäB,  np.  xüa,  ZDs.  /tn  (GlrPh.  /  b. 387)').  —  1)  Die  ich  auf  ir.  *x^aAun'  zurück- (Ühre;  s.  dazu  np.  ^ähar  und  nbal.  gvähar, %  83.  2.     Anders  GIrPh.  i.  264.
•  j.  vohu'mant-  Adj,  'mit  Gutem  ver- sehen, reich  an  Schätzen' :  ahuräi  mazdai vatthavi  'matte  Y,  12. 1,  V.  ig.  11",
ai.  vdsumant-  Adj,  —  Pü.:  veA  paimän;  s.  IF. //.134.  —  Vgl.  "maUf.—  I)  Hier  trennt  die NA.   •Au.m'.
•  '].  vohu'raoöah-  m.  EN.  zweier  Glau- biger; i)  '^anhs  franyehe  a^aons  "d
ren  Mantel  gekleidet . ." Yt5. 126.
Zum  V.  iTiah-.  —  Vgl.  iF.  vavtuinim.
•  j.  "vaöhe  :  na^aia  V  paiti  usta  vaahö bvat  Vytjo;  —  räia  f  maidahäta  aiaoru \yl36.
•  j.  "ätara  vaohit  vanat^  (Sp.  1352  o.) V.7.S2  PüZ.
j.  ditö  vaahiti  V.  /p.  17:   lies  dätan  vaah-
•  j.  vaohutät-  t  'Blut':  aslqmia  vansamia spämamla  mOhrqmca  -tätqmca  Y.6.J;  29.
Auffällige  Bildung  ('languini/ai",).  —  Pü.:  xäa ta/U»ii.
•  j.  vanhu'däta-  m.  EN.  eines  Gläubigen: °taAe  i^aiätaAe  asaons  Ytij.  119.
Ableit.  ~~  Vgl.  voku.ääla',  vahyazdäla:  — Eig.  'von  den  guten  (Götlern,  s.  Y.  58-  S) gegeben'  oder  'gesc halfen'.  —  ai.  vgl.  vaiu- daita-  m.  EN.
•  j.  vanhuSätayana-  patr.  Adj.  'von Vavhiitäta  stammend,  dessen  Nachkomme*: utyeAe  fsd.)  -tayanake  Yt.  13.  1 19.
Ableit.  aus  va-ihulila..
•  j.,  g.  vaohu-däh-",  j.  °8äh-''  Adj.  'Gut,
```


## [2026-10-17T00:02:12.867Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\ndef leaf(f,i):\n    return open(f,encoding='utf-8',errors='replace').read().split('\\f')[i]\np=leaf('HRN.txt',134)\nfor k in ['xün','xun','Blut','Kamel','ustur','ultur','uStur']:\n    for m in re.finditer(k,p): print('HRN134',k,p[max(0,m.start()-300):m.end()+400].replace('\\n',' '));print('--')\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'Kamel',t): print('HRN leaf',t[:m.start()].count('\\f'),t[max(0,m.start()-300):m.end()+300].replace('\\n',' '));print('--')\nE"
}
```


### [2026-10-17T00:02:13.496Z] TOOL RESULT

```
HRN134 Blut (AV.). 510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388). aw. hü kehrpa in Ebergestalt'; phlv. /ük (Bund.), yßköak hezw, /übadak (Payprus, Ilorn ZDMG. 43, 51); skr. siikard- 'Eber, Schwein*. kurd. /ü (H.-Sch.); B>fy.xilg; oss. d. t. yiä (310); bei. hlk, n. hJy (157) ; wa;r. /äg, sar. y^ug, 511. //rn 'Blut', yümn. aw. vohuni' *Blut'; phlv. yün, yUnömaud, kurd. ;^("n (ll.-Sch.); af}'. vTne (f. pl.); bei. LW. hün, hon (162); wa/. vu/c^n, Uyn. vlyTn, sar. va/ln, sangl. vain, 512. xöl Helm', yöd. ap. yauda- *Helm*; aw. ayö],yaoda'. arab. LW. yu^at 'Helm'; Sify.yöl; oss. d. yodäy t. yüd (302) ; sar. ydtid *Hut, hohe Mütze aus Schaffell'. 513. yi^'ei 'Schweiss . aw. yya^öa- 'Schweiss' (ZPGl.), vergl. aw.
--
HRN134 Blut in, :i)5 (Qiss. Dan. S. 388). aw. hü kehrpa in Ebergestalt'; phlv. /ük (Bund.), yßköak hezw, /übadak (Payprus, Ilorn ZDMG. 43, 51); skr. siikard- 'Eber, Schwein*. kurd. /ü (H.-Sch.); B>fy.xilg; oss. d. t. yiä (310); bei. hlk, n. hJy (157) ; wa;r. /äg, sar. y^ug, 511. //rn 'Blut', yümn. aw. vohuni' *Blut'; phlv. yün, yUnömaud, kurd. ;^("n (ll.-Sch.); af}'. vTne (f. pl.); bei. LW. hün, hon (162); wa/. vu/c^n, Uyn. vlyTn, sar. va/ln, sangl. vain, 512. xöl Helm', yöd. ap. yauda- *Helm*; aw. ayö],yaoda'. arab. LW. yu^at 'Helm'; Sify.yöl; oss. d. yodäy t. yüd (302) ; sar. ydtid *Hut, hohe Mütze aus Schaffell'. 513. yi^'ei 'Schweiss . aw. yya^öa- 'Schweiss' (ZPGl.), vergl. aw. y'^'Tsctt, ynseu] phlv. y
--
```


## [2026-10-17T00:02:20.257Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nfor f in ['HRN.txt','HUB.txt','PHD.txt','NYB_vol2_glossary.txt','SYN.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for pat in [r'u[sšS][tṭ]r[aā]h?\\b',r'u[sšS]tur',r'u[sšS]tar\\b',r'\\bx[üūōö]n\\b',r'xwn\\b',r'\\bb[aā]h\\b',r'Zar[aə]?tu[sš]',r'Zartu[sš]t|zardu[sš]t|zartušt']:\n        for m in list(re.finditer(pat,t))[:4]:\n            print(f,pat,'leaf',t[:m.start()].count('\\f'),'::',t[max(0,m.start()-150):m.end()+250].replace('\\n',' '));print('--')\nE"
}
```


### [2026-10-17T00:02:21.619Z] TOOL RESULT

```
<persisted-output>
Output too large (32.4KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bt18e9vn4.txt

Preview (first 2KB):
HRN.txt u[sšS][tṭ]r[aā]h?\b leaf 42 :: ) u. ö. 86. ester ^Maulesel'. phlv. astar; ai. agvatard- 'Maulesel'. kurd. istir, histir; bei. istal, n. hastal (438). 87. iiStur *Kameer, sutur. aw. ustra- 'Kameel'; phlv. ustrlastän (vd. 15, 68); ai. üstra-, kurd. LW. (?) hustur^ sutur; bei. hustar etc. (161); wa/. ü^tür^ siyn. stur, sar. xtiir, LW.(?). 88. eSk *Thräne . g. sah, aw. *asraka (vergl. skr. dgra-), *arsaka (Hörn, Indog. Forsch., II, 136)
--
HRN.txt u[sšS][tṭ]r[aā]h?\b leaf 167 :: ze im Gegensatz zur ausser- persischen Währung'. Hörn, Grtindriss d. neup. Etymologie. 10.._ 146 — 655. {2).'^er 'Greis, Greisin'. aw. vergl. Zarad'lustra" ; ai. jdrant-; arm. cev 'Greis' (H. No. 135). Vergl. np. ^ol (No. 648). oss. t. zärond alt' (129). 656. zerd gelb', vergl. zerd[ab^ zerde 'Galle'. aw. zairita- 'gelb' ^) ; plilv. zart, zartth, syr. LW. plDI; ai. hdrita-. kurd. LW. zercl ; af/. ziya
--
HRN.txt u[sšS][tṭ]r[aā]h?\b leaf 346 ::  191. ubjyeitf 875 Anm. ubdafna- 168. uriinya' 209. itrüpayeiiitl 608 Anm. uroan- 625. urvarä' 201, 118' 644. uspa^atU' 1051 Anm. M»aÄ- ii7. w«y Uli. uStra- 87. m;a- 1085. Erexsa- 477. ^eyaw^- 72. erezaia' 68. ere/a- 609. ereStaa' 84. Är^/- 876. kainikä' 870, i;2ö. Äjomfii- 870. ka^nä' 881. kaofa- 875. l^kaoS'^ kuSaiti 855. teo- 844. katära' 848 Anm., lj<^5. Ärarfrt 878. iXÄran- 869. + «/li;/ 103. + *p
--
HRN.txt u[sšS]tur leaf 42 :: istir, histir; bei. istal, n. hastal (438). 87. iiStur *Kameer, sutur. aw. ustra- 'Kameel'; phlv. ustrlastän (vd. 15, 68); ai. üstra-, kurd. LW. (?) hustur^ sutur; bei. hustar etc. (161); wa/. ü^tür^ siyn. stur, sar. xtiir, LW.(?). 88. eSk *Thräne . g. sah, aw. *asraka (vergl. skr. dgra-), *arsaka (Hörn, Indog. Forsch., II, 136). afy. ö^a resp. ö/a; wsl/, ya^k, sar. yujck, Vergl. ers (No. 69). 89. iiSn
--
...
</persisted-output>
```


## [2026-10-17T00:02:25.633Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -v '^HRN' /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bt18e9vn4.txt | cut -c1-600 | head -60"
}
```


### [2026-10-17T00:02:26.260Z] TOOL RESULT

```
--
--
--
--
--
--
--
--
--
HUB.txt u[sšS][tṭ]r[aā]h?\b leaf 185 :: oren wird. *) Der Vorsohlag von a vor sx aus X8 (z, B. asx^ *roth' = zd. xsapta-'y asxarh 'Land' = ap. xsa^^'a-) ist; armenisoh.- 175 - ^tistr = zd. ustra- ; vielleicht auch in abr^um *Seide* = phi. *apr^utn (s. oben p. 12). Dieser Einschub fand also schon im Phi. statt. b) a eingeschoben in: rosan *heir (Vis u Ramin 103, 21) — zd. raoxsna- ; rdyan 'Butter, Oel' = zd. raoyna- ; dasan ^) *Geschenk* = d
--
HUB.txt u[sšS][tṭ]r[aā]h?\b leaf 214 :: st (Tab. 154), syr. Zara- dust (3. Jhd.), Cureton, Spicil. 25, nach NSldeke) Zardust, arm. Zradest, Zradast, phi. Zaratust {Zara- fuxst) => zd. ZaraO^ustra-. 3. Fur Or : fr in FrSdun, siehe p. 207. § 96. Ap. &^ wird im Np. zu s oder hr: a) zu 5 in: si, [liter se *drei' (s. oben p. 78) = zd. g. pi. x^rayqm, vgl. ap. ^Htiya- *der dritte*; si 'dreissig = ap. "^Old^at-, zd. drisat-] pus 'Sohn (daraus pnsar
--
HUB.txt u[sšS]tur leaf 148 :: n ^ir5 *Hals*, girebdn *Kragen*, skr. grTva- 'Nacken*. Kapitel 4: ap. u nnd u. § 21. Ap. u (= idg. u) bleibt im Np. als u, vgl. u (u) und* = ap. uta; ustur (sutur) 'Kameel* = zd. mtra-; xmk 'trocken = ap. uSka-, zd. huika-, skr. guska-; xusur *Schwiegervater = zd. x^asura- ; Xusrav = zd. husravah- (arm. Xosrov, gr. XoOpo^g). § 22. Anlaut. w vor einfachen Konsonanten in mittel- persisch zwei- oder mehrs
--
HUB.txt u[sšS]tur leaf 183 :: treten, die urspriinglich nicht mit Doppelkonsonanten (z. B. zd. spa^ia-^ stawra-) sondern mit Vokal + Doppel konsonant anlauteten. Dies geschah bei: ustur ^KsuneeY = sutur, zd. ttstra-; asvar *Reiter = .s?/- var, phi. asbar, ap. asabara-; afroxtan *anzunden, erleuchten, glanzen' = ftiroxtan, furoy 'Glanz', phi. afrOxtan, zd. aiwi + rwJ. Ebenso bei abresum = baresum *Seide', arm. apri- sum H. 65; fitad
--
HUB.txt u[sšS]tur leaf 184 ::  a) u eingeschoben in : phi. paz. barsum aus *barsm = zd. baresma (np. barsam ist Parsenwort); hezum 'Brennholz aus *ezm = ap. *aizma- = zd. a^sma- ; ustur 'Kameel' aus *) Schon bei Ptolem. liandSarcc^ das trotzdem zu zd. &p. spaSa- *Heer* gehoren wird. *) Der Vorsohlag von a vor sx aus X8 (z, B. asx^ *roth' = zd. xsapta-'y asxarh 'Land' = ap. xsa^^'a-) ist; armenisoh.- 175 - ^tistr = zd. ustra- ; vie
--
HUB.txt u[sšS]tur leaf 246 :: d kH = iran. ap. st = np. st und s^:' a) = s^ : mw6^^ Taust' = zd. rmdU-, arm. msrtfc 'Bundel* = phi. "^mustik; angust 'Finger, Zehe' = zd. angusta"; ustur 'KameeV = zd. uistra--, pust 'Rucken* = zd. parsfi-, skr. prstha-; mustan reiben, skr. mrsta-, Wrzl. m&t'g'^\ hihist 'Paradies' == zd. vahista-; xist 'ZiegeF, skr. istako-; ristan *spinnen, pr. resam, Wrzl. reik^; nivistan 'schreiben* = ap. nipistan
--
HUB.txt u[sšS]tar\b leaf 167 ::  gu- (statt nur zu gu-) : bidast, gidast *Spanne' = zd. vitasti- ; gustax *frech' = hustflx (unbelegt), arm. vstah, phi. v[i)staxv ; bistar 'Lager = gustar, g. vistara ZDMG. 36, 69, vgl. gustardan, von vi -\- Wzl. star, vgl. zd. stairis; hiskofa *Blute*, jiid. pers. ^) A us urspr. * varta- hatte np. *bard oder *var(f, aus *vrta', *ti'ii' np. *gurd werden sollen. Siehe oben p. 91. «) Siehe § 36.— 158 —
--
HUB.txt u[sšS]tar\b leaf 230 :: asta-^ skr. hasta-, arm. dast-ak, dasf-a-kert; 4) di? *Herz' = zd. zered'^ zaredaya- (vd. 1,3), skr. Ard-, hrdaya-] 5) d(Js^ Treund' — dostar = ap. daustar-, vgl. zd. zaosa-, skr. y^/s ; 6) dahan 'Mund* = zd. zafan-^ 7) d^, df^ gestern = skr. %as; darj/a *Meer' = ap. dray a- (oder drayah- ZDM6. 46, 298), zd. zrayah-, aber dial, zarah^); 9) ap. adam *ich' — zd. a^g;M, skr. aham; 10) ap. adm^ *er nahm' =
--
HUB.txt u[sšS]tar\b leaf 246 :: cht* = zd. asta, idg. okHOu ; biristan 'braten' mit st aus skt von Wrzl. iran. brj und bri^g = idg. bhrzg, oben p. 27. b) = st: dost Treund' == ap. daustar-; §ast 'sechzig' = zd. xsvasti- ; pist 'Mehl' = skr. pista- ; mahist (ZDM6. 46, 139) = ap. mad^ista- ; bargustuvan 'Pferdepanzer H. 205, oben p. 27. Durch spateren Vokalausfall entstand st aus sat in bTst 'zwanzig* = zd. visaiti und diivest zweihund
--
HUB.txt \bb[aā]h\b leaf 42 :: nn = ap.*e?aAa- gesetzt werden (vgl. np. bCLzU 'Arm', arm. LW. bazuk, also arsacid. phi. = *bdzuk == zd. bazU'y skr. bdhu- etc.). Ich stelle also np. bah-a, phi. vah-dk zu skr. vas-na-, Im Uebrigen hatte der Hinweis auf Solmsen, KZ. 29, 81 genugt. 243. Vgl. Nr. 501. 244. Np. bahdna Torwand' kann weder = skr. apidhdna- fBedeckung, Hiille, Decke* — Darmesteter) noch = skr. upadhdna- ^Deckel' etc. (vgl.
--
HUB.txt \bb[aā]h\b leaf 44 :: hte aber wegen der Laute auf np. pill ^Briicke' = gel. ptird^ kurd. pird, purd^ pel (Horn Nr. 325) verweisen. Ist berd die alteste Form, so darf arm. bah *Hacke, Karst* (= *bhrtrom nach Bartholomae) verglichen werden. 258. Np. him *Furcht' = skr. bhtma- 'furchtbar'. 259. Zu phi. vimdrimtan vgl. mein Zoroastrisches Lied p. 62. Np. bt/mdr = paz. vlmdr geht nicht auf ap. *v^mara'j das allerdings zu np. 
--
HUB.txt Zar[aə]?tu[sš] leaf 214 :: p. 96); 2. (T in np. Zardust, ZarOdvst (Tab. 154), syr. Zara- dust (3. Jhd.), Cureton, Spicil. 25, nach NSldeke) Zardust, arm. Zradest, Zradast, phi. Zaratust {Zara- fuxst) => zd. ZaraO^ustra-. 3. Fur Or : fr in FrSdun, siehe p. 207. § 96. Ap. &^ wird im Np. zu s oder hr: a) zu 5 in: si, [liter se *drei' (s. oben p. 78) = zd. g. pi. x^rayqm, vgl. ap. ^Htiya- *der dritte*; si 'dreissig = ap. "^Old^at-, zd
--
PHD.txt u[sšS][tṭ]r[aā]h?\b leaf 124 :: k! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < 
--
PHD.txt u[sšS][tṭ]r[aā]h?\b leaf 190 ::  yoke (n.) juy. yoke (v.) āyēxtan, (āyēzīdan). yolk zardag. you ašmā. young juwün, keh, kawādak, kodak. younger keh(tar). youth Juwan; juwānīh. Zaratustra, у. Zoroaster. Zend zand. zodiac dwazdahan; sign of the ~ axtar. Zoroaster Zardu(x)št. Zoroastrian, v. Mazdean. Ohrmazd Amahraspandan Wahman Ardwahišt (Urd-, Ašwahišt) Šahrewar Spandarmad Hordād Amurdād Ādur Anāhid Ahreman Akóman Arzür Astwihad I Fr
--
PHD.txt u[sšS]tur leaf 36 :: solate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] i
--
PHD.txt u[sšS]tur leaf 111 :: . ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. u
--
PHD.txt u[sšS]tar\b leaf 111 :: ! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~za
--
PHD.txt u[sšS]tar\b leaf 131 :: ar. calculate āmār-; v. reckon. calculated ēšmurdīg. calculation ēšmārag. calf gawdar. call xróstan, xwandan. calumny dušēwāzih. calyx kulāfak. camel uštar. camp bunag. camphor kapür. can Sayistan, tuwān, P Sah-; v. able. canapé bazmawurd. Cancer Karzang. cane graw, nay. cane-brake nayestan. cap kulaf(ak). capable adüg. capital šahrestān. Capricorn Wahig. captive dastgir, griftar, wardag; v. prisoner. 
--
PHD.txt u[sšS]tar\b leaf 142 :: uine wizurd. geometry zamig-paymanih. ghost (soul) gyān, uštān; give up the — gyan kandan. gift āyaft, dāšn, pārag, das?r. gigantic māzandar. giraffe uštar-gāw-palang. girdle kamar; sacred ~ ēbyānghan, kustig. girl kanig, maiden. give dadan. giving dahiin. glass abgénag, jam. glazed (pottery) dēsēn. gleam brāzidan. glorious bamig, xwarrahomand. glory abrang, bam, xwarrah. gnat paxSag. go franaftan, raf
--
PHD.txt u[sšS]tar\b leaf 247 :: .5t1€357 05 tee 1505 - (de es oru ко” 1510* sēr veo хоп! daménag zamigig zamig ^39 varā 1 45 set Viet zamigpaymünih AU росу gn? damidan mir-! murdant uštar! gow-t guftan™ gow-! guftant zamestān damišn. yask dastyār dastyārīh dastgraw . dastgir! dastwar dastwarih jastan dastag dast(a)gird мее ~litese Vpuréze хе ~ пме wt? ice gnftar griftàárómand griftan darz garz- darzig garzidan garzag garzišnīg garziá
--
PHD.txt \bx[üūōö]n\b leaf 104 :: . . -nights-long. ~estan [ipst?n! | N ~] gynaeceum, private apartments. Sabig [špyk! | N sabi] (Mazdean's ritual) under-shirt. Sabixón [špyhwn'! | N —xün] night raid. Sad [P?:! | M ға, N ~] happy, joyful. ~ih: happiness, joy. šādurwān [P?wlw’n! | N ~] dais, platform; basin, pond, fountain. šafšēr [!pfyl | M ут] = šamšēr. барг [fel | M šgr, N šēr] lion; astr. Leo. P šah- [šh- | = P] be able, can. šāh 
--
PHD.txt \bx[üūōö]n\b leaf 119 ::  [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption. wizārd-wars 93 xün wizürd-wars [wc'/t' wls] with parted hair. wizāstan, wizāy- [wyz'stn!, wyz'd- | M wy2’y-, N guzáy-] injure, impair, prejudice. ~išn: injury. ~išnīg: injurious. wizén [wcyn! | N guzin] choice. wizend [wz(y)nd | M wzynd, N guzand] hurt, harm, injury. 
--
PHD.txt xwn\b leaf 20 :: ~ druxtan : break faith. add mizīdan, miz- [myc-ytn' | N mazidan] suck. for *moy-mard ... read mowmard ... mēy ... add M mwy. read nüxun [n^hwn' | P nxwn, N nàxun] (finger) nail. delete nāyīzag ... (read wezag). nek, ~th ... add benefit. nibastan ... delete SKBHWN-tn' < A Vškb; nibastan ... read M nb’st, P nb’y-. nibeg ... add M nbyg. nibištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn
--
PHD.txt xwn\b leaf 23 :: n abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] re
--
PHD.txt xwn\b leaf 99 :: gh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy
--
PHD.txt Zar[aə]?tu[sš] leaf 190 :: anüz. yoke (n.) juy. yoke (v.) āyēxtan, (āyēzīdan). yolk zardag. you ašmā. young juwün, keh, kawādak, kodak. younger keh(tar). youth Juwan; juwānīh. Zaratustra, у. Zoroaster. Zend zand. zodiac dwazdahan; sign of the ~ axtar. Zoroaster Zardu(x)št. Zoroastrian, v. Mazdean. Ohrmazd Amahraspandan Wahman Ardwahišt (Urd-, Ašwahišt) Šahrewar Spandarmad Hordād Amurdād Ādur Anāhid Ahreman Akóman Arzür Astwihad I
```


## [2026-10-17T00:02:30.363Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==121' PHD.txt | grep -n -i -B1 -A1 'blood\\|xōn\\|xon'; grep -n -i '^xōn\\|^xon\\|^uštar\\|^ustar\\|^u[sš]tr' NYB_vol2_glossary.txt | head; grep -n -i 'blood' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:02:31.084Z] TOOL RESULT

```
2-хап 94 xurdruš
3:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; 
5401:uštra-: uštur
3582:šāhīkīk [šhykyk] royal, of royal blood 6617. — Derived from šāhīk ‘royal, kingly’: ke nāmīktar ? hàn + š��hīktar u aparvēžtar *who is the most famous? He who is the most kingly and the most triumphant’ PT 961.
4016:lyaspuhrakan used as pl. cas. obl. of vaspuhr: the heirs of body, in the royal family: the princes of the blood royal: apāk fradandàn u ~ 3793; spähpatän u vazurgān u üdzütakün u ~ 11%; apāk apurnäi zātakān ~ + Artaxšēr 16°"; apäk pusän brätarän u ~ u hāmharzān 188 (185 vispuhrakän inthe same series) ;bunak i Vistäsp u apārīk ~ 115%. — Paz. vāspu- hargq, vāspihiraga, Skr. v. vikhyātimant in pl. (Mx 1"). — As to the correlation sg. väspuhr: pl. cas. obl. väspuhrakän, cf apurnāi: apurnāyakān (but sg. also apur- näyik); äzät: azātakān (pl. also azatàn); Eran: Ērānakān (q.v.; also Mx 21%); Tür: Türakän (Mx ibd.; commonly Tū- ran); (Hrömäy-ik:) Hrömäyakän (Mx ibd.); Yahüd: Yahüdakän (v. these ws.); cf also vazurgakün and vispuhrakān".
4305:xurdruš [hwldlwš] carrying a bloody, cruel weapon 7212.15, 1037. — Borrowed from Av. (540) xrvidru-, nom. -druš, an epithet of Aēšma; Paz. xrui.draog, Skr. v. himsäsastra.
4399:x"ihl [hwyhl] curly 2677. xohal ‘crooked, bent’. xün [hwn'] blood 22°. 255, 5014, 606. 7814.
4402:xūn-rēcišnēh [-Iyešnyh] bloodshed, blood- bath 131, — V. rēxtan.
```


## [2026-10-17T00:02:37.320Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'camel' NYB_vol2_glossary.txt | head -5; grep -n -i 'camel' SOD_pages.txt | head; grep -n -i \"blood\" SOD_pages.txt | head"
}
```


### [2026-10-17T00:02:37.890Z] TOOL RESULT

```
97:GDH: GADDEH his Fortune, or Fate GMR”: GAM LA camel
3866:uštur [GMR?’] camel 9419, 9915, 1188. — Av. (420 sq.) ustra-; NP uštur, šutur.
4029:devan .. . hac hàn dar u vitarg vartend that they should keep the dévs back from this gateway 8714-4; asp apdc vast he turned his horse round 117; asp apar rahy vartét! harness the horse to the chariot! 5413-14, with the gl. ku andar bandet; — pas be 6 martom karpéh vast hend then they were metamorphosed into human shape 9526; apt-t frāc vast 6 hàn uštur karp and thou turnedst him into a camel's shape 9915, — Av. (1368) varat-; MPrthPrs wštn wrd-, MPrth also pres. wrt- (MHC); Paz. vaštan vard-, cf gaštan. V. also varténitan and the next w.
4101:Dhabhar vētvar, without etymology, in the sense of ‘contented, contentment, forbearance, patient, consoling oneself (‘consoling’ already West), resigned to the will of God’ (~ dätan ‘to console’); Hormazdyar with the same etymology as Bailey, but giving the same senses as Dhabhar (‘one who endures grief, en- during, patient, consoling, persevering’). Both lay stress on the close parallelism with a%ansand (x"arsand), of which it sometimes seems to be a mere synonym. However, the original idea underlying it must be looked for from another angle. I read it, with Dhabhar, vēt-var and derive it from OTr *vaiti-bara- ‘the willow- bringer [Av. (1314) vaéti-, NP bed, ’willow’] originally an epithet of Airyaman, the god of healing, and going back to the myth told in Vd. 22: Ahuramazdah, badly wounded and struck with 99999 maladies by Ahriman on his first on- slaught on the heavenly creation, pro- mised 1000 horses, 1000 camels, 1000 heads of cattle, 1000 sheep and “the beautiful Benediction of the Righteous" (dahma äfriti) to the god who could heal him. All declined except Airyama tišyē *Airyaman the desired(?)": he brought (barat) hair from 9 horse stallions, hair from 9 camel stallions, hair from 9 bulls, hair from 9 rams, and brought 9 willow twigs (nava vačtayo barat) and drew 9 furrows — the Phl v. adds: “and made a nirang (g. v.)”, a magic spell intended ‘to heal the wounds and stop the maladies. Apparently the willow twigs played the chief part in this nirang (of whose parti- culars we know of course nothing), thus it was quite natural to form out of it the epithet *vea$-bara- of Airyaman in his quality of the healing and relieving god. Later, Airyaman having faded away, the usage took a wider range and developed secondary nuances, but the original meaning ‘healing’ is still fairly transpar- ent in many passages, e.g. DD 36? (quoted both by Dhabhar and Hormazd-
4241:vitārēnītan [wt'lynytn'] to cause a p. to take a p. away from: Kat-Xēūsrēt ke hac vài i dérang-x"atà& vitārēnēi K. whom he (Saošyant) will take down from the Long- dominating Wind (who had been trans- formed into a camel on which K. is riding, v. 9911-1002) 1065.
5980:    (o)xusand (Ywsnt) =*xwsnd, 'Yws'nt, Yws'nt                       camel
9908:            impf. mxub                                                  camel
35043:      camel
37806:breadth 6812, 10950                           7087                                 camel      784, 2129, 10797
16329:                                                                            blood
17205:                                                                        instrument of bloodletting ?
34857:       BBB pl39, xwrbYw, ace. C2, 68V17, 69V13                        blood
34871:                                                                      blood-stained
34879:10751 xwrm M, C                               js*j<«^V               bloodthirsty(M<?0jly/ierf doer)
34884:                                                                     bloodletting «»xwrn-
35498:                                                                    blood
35861:                                                                       blood
35871:        yu-tac, ew-tac ©pi. ywtyst ^ywtfcfli)                         bloodshed
35939:          (to)keep aloof                                             blood
```


## [2026-10-17T00:02:43.022Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5970,5985p SOD_pages.txt; sed -n 9900,9912p SOD_pages.txt; sed -n 34850,34886p SOD_pages.txt; python3 -c \"\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nfor n in [5980,9908,34857]:\n  import itertools\n  pre='\\n'.join(t.split('\\n')[:n]); print(n,'leaf',pre.count('\\f'))\""
}
```


### [2026-10-17T00:02:43.802Z] TOOL RESULT

```
     GMS 86, 395 n 1
                                                                     GMS 160, 933; >Ywst\ Dhy. 77, 84, Ywstw, Dhy.
772 'ywrmzt rwc S                :^j^jjj   >yjt> «U Jji jjj            80, 79; pret. st. 'Ywst&r-, VJ 1077
                                                                 783 'ywst'r      B =» >Ywstr-
    (a)xurmazd roc          Oxwrmzt) =*Ywrmzt rwc
                                                                 784 'ywstr-      B                                       j&
    first day of the month
    MDiii; Hen. Orientalia. 8.94                                     (o)xust(o)r (}Ywst}r) ©*uxstra-, A v. ustra
                                                                       ©nom. -y; ace. -w; ob. -C)y> abl. -\ pi. -y(h)
773 'Yws'nt B, S                        ^Ij,ju^>                       =»xwstr-, }xwstr-
    (o)xusand (Ywsnt) =*xwsnd, 'Yws'nt, Yws'nt                       camel
                                                                                                                 'krt'nyk'rch
 31

        GMS 162, 257, 483, 497; VJ; TSP 3.183, 184,                       birth
                                                                          GMS 5; BBB f67
            -^nyWy-1                                               2128 *xwsp'ny S                                jlScjlj^
          0<?)break
          GMS 417; BBB p59, 11                                          oxuspane
                                                                        herdsman
2115 *'xwb(y)-          C                       oJ^J^ti'cf-*-
     axub ?                                                             MSP bl83
          (to)surgc forward                                        2129 »xwstr-   S                                       j±
          Mack. BSOAS 31124; S W, C2, 12V9 n p56,                       oxustr ©ace. -w     ^'ywstr-, xwstr-
            impf. mxub                                                  camel
                                                                        Anc. Lett. 1.11
2116 »xwd,wny' C                       j& <J^J i^~
     axudawanya ©f. n. -^wxd'wny*                                  2130 >xwyr C                                         j>T
     zeal, striving                                                     axwer =*»ywyr
       BBB p63, 521
                                                                      (related /o)Hormazd
 10745 xwr byw        C =» xwrPyyy                                    GMS 1278; Hen. Magi. 142.4
 10746 xwrpyyy        M                                         10758 xwrn- M, C                            oy>-
       xur-Payi ©ace. -w                                              xurn ©<Av. vohuni ©nom. ob. -y -»ywxn-,
       Sun-god
                                                                        yxwn-, ywrn-, yywn(w), wyrn-(h), yxwrn-
       BBB pl39, xwrbYw, ace. C2, 68V17, 69V13                        blood
10747 xwrc*q =* xwrcy*q                                               GMS 208, 492, 1168n 1; BBB 88.763; ace.
10748 xwrcy>q C                                  S\.                    xwrnw, GMS 350; STii 6.9; BSTi 318; Sund.
                                                                        AoFviii 1981, 23V10
      xurcyak ©f. n. ^ywrtcyk*
      food                                                     10759 xwrndy(y)     M                   6ju*L <^^„j i*jjjy~
       BSTii 836.3: C2, 108R3 n pl79.3                                xwarande, xurande     ~»ftr xwrndy(y)
                                                                      destructible
10749 xwrd'r-         C
                                                                      BBBbl5b95
      xur-5ar        ©trans, pret. =*xwr-
                                                      o>j^>-   10760 xwrnptxwrk       M                  ^To^-^liToy-
       0o)eat
       C2, 69R16; Sund. AoFviii 1981, 23V6                            xurn-patxure -»xwrn-
                                                                      blood-stained
10750 xwrjn(y)c M             (j^>- ^j^dS** f>> ^                    Sogdica. 21.19b, +6ndy, Gersh. Sogd. Cpds
      xur-zan(i)c =>ywryznych                                          143b, 148
       second month of the year
                                                               10761 xwrny psyncny C              j'y-u>- < jljoj*-
       Sogdica. 27.2a, xwrjncrrfx, Hen. Fasts. JRAS                  xurne-pasenc-nS ©voc. -n\ pres. part.
         1945, 149.3, 151.16; GMS 1275                                 «=»ywxn* }psyyk

10751 xwrm M, C                               js*j<«^V               bloodthirsty(M<?0jly/ierf doer)
      xurm ^xrwm, ywrm(h), ywrwm                                     STii 6.9; BSTi 318; GMS 893
       soil, earth
                                                               10762 xwrnyy ws- M                      (cr*j? uj*-)^b«*~
       GMS 415; BSTii 848.52: C2, 69V18                              xurn(e)-as
                                                                     bloodletting «»xwrn-
10752 xwrmny C                                        ^fiz-
                                                                     Sund. Man. Lett 305.21, 29
5980 leaf 95
9908 leaf 149
34857 leaf 504
```


## [2026-10-17T00:02:58.530Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(340,362):\n    p=pages[i]\n    if 'اشتر' in p or 'uštr' in p or 'ustr' in p:\n        for m in re.finditer(r'اشتر|u[sš]tr',p):\n            print('leaf',i,p[max(0,m.start()-150):m.end()+300].replace('\\n',' '));print('--')\nE"
}
```


### [2026-10-17T00:02:59.128Z] TOOL RESULT

```
leaf 353  » ی گونند بفتح واو بنایر قاعدم کلی . اشتم خار » نوعی از خار است کهشتر (۱) چك : ژند . ۱ مشفف اشتاب. آخت رکاو آنرا برغبت نمام میخورد وخارشتری‌همان است اشتر خو‌اد » با راو مسوله , سممتی ائتر خار است که خر شتری و از مار است که آنرا اشتر خوار 7 کوچك و خونض ار که بربدن شتر وکاو و خر و گوسفند بجبد و خون از بدن آنها بسکد . اشتردل- بکردال و سکون لام » بد دل وکینه دل را کویند - وکنایه‌از مردمی‌است که این صفت داشته باشند (۷) - وبسنی گوشد کنابه از مردم بیدل و ن
--
leaf 353  ژند . ۱ مشفف اشتاب. آخت رکاو آنرا برغبت نمام میخورد وخارشتری‌همان است اشتر خو‌اد » با راو مسوله , سممتی ائتر خار است که خر شتری و از مار است که آنرا اشتر خوار 7 کوچك و خونض ار که بربدن شتر وکاو و خر و گوسفند بجبد و خون از بدن آنها بسکد . اشتردل- بکردال و سکون لام » بد دل وکینه دل را کویند - وکنایه‌از مردمی‌است که این صفت داشته باشند (۷) - وبسنی گوشد کنابه از مردم بیدل و نامرد و ترسنده باشد . اشتر غاز - بافن نقطه دار بالف کشیده و بزای هوز زده » بیخ د
--
leaf 353 و مسوله , سممتی ائتر خار است که خر شتری و از مار است که آنرا اشتر خوار 7 کوچك و خونض ار که بربدن شتر وکاو و خر و گوسفند بجبد و خون از بدن آنها بسکد . اشتردل- بکردال و سکون لام » بد دل وکینه دل را کویند - وکنایه‌از مردمی‌است که این صفت داشته باشند (۷) - وبسنی گوشد کنابه از مردم بیدل و نامرد و ترسنده باشد . اشتر غاز - بافن نقطه دار بالف کشیده و بزای هوز زده » بیخ درخت انمدان است‌وصمغ انگوزه خوانند » و نی کویند کیاهی‌است یخ بخ آنراآ چار سازند ومعنی آن ش
--
leaf 353  بکردال و سکون لام » بد دل وکینه دل را کویند - وکنایه‌از مردمی‌است که این صفت داشته باشند (۷) - وبسنی گوشد کنابه از مردم بیدل و نامرد و ترسنده باشد . اشتر غاز - بافن نقطه دار بالف کشیده و بزای هوز زده » بیخ درخت انمدان است‌وصمغ انگوزه خوانند » و نی کویند کیاهی‌است یخ بخ آنراآ چار سازند ومعنی آن شوكا لجمال 7 و عربان زتجبیل المجم خوانند » تب ربع را مقید باشد . بمعنی موجه است خواه موجه دربا باشد و خواه تالاب و رودخانه و امثال ۹۹ اشتر ک) - بنتح اول و نال
--
leaf 353  سازند ومعنی آن شوكا لجمال 7 و عربان زتجبیل المجم خوانند » تب ربع را مقید باشد . بمعنی موجه است خواه موجه دربا باشد و خواه تالاب و رودخانه و امثال ۹۹ اشتر ک) - بنتح اول و نالك و کاف خوانند . اشتر گاو -زرانف را کوبند و آن جانوربت میان اشتر و کاو چنانکه استر حیان اسب و خر است . # ادتاد راهنمای مینوبان و جپانیان ۴ - مراد اختاد به ۵ رکه : آشتاب . یه درسفحةٌ ۱۳۸
--
leaf 353 یل المجم خوانند » تب ربع را مقید باشد . بمعنی موجه است خواه موجه دربا باشد و خواه تالاب و رودخانه و امثال ۹۹ اشتر ک) - بنتح اول و نالك و کاف خوانند . اشتر گاو -زرانف را کوبند و آن جانوربت میان اشتر و کاو چنانکه استر حیان اسب و خر است . # ادتاد راهنمای مینوبان و جپانیان ۴ - مراد اختاد به ۵ رکه : آشتاب . یه درسفحةٌ ۱۳۸
--
leaf 353 نی موجه است خواه موجه دربا باشد و خواه تالاب و رودخانه و امثال ۹۹ اشتر ک) - بنتح اول و نالك و کاف خوانند . اشتر گاو -زرانف را کوبند و آن جانوربت میان اشتر و کاو چنانکه استر حیان اسب و خر است . # ادتاد راهنمای مینوبان و جپانیان ۴ - مراد اختاد به ۵ رکه : آشتاب . یه درسفحةٌ ۱۳۸
--
leaf 354 اشتر گیا - بکر کاف فارسی و تحتانی بالف کشیده , بممتی اشتر خار است که خار شتری باشد ۰ و بسضنی کوبند کیاهی است‌دوابی که آنرا سلخه خوانند . اش شتر هرع - پرنده است که بای او شراست وسنکه و آش خورد و بایابپای خود سثگه بر هر چیز که خواهد زند و خطا نکند و عربان اورا نعامه کونند . اشتر مرغ اشثر هووو « کویند جانو
--
leaf 354 اشتر گیا - بکر کاف فارسی و تحتانی بالف کشیده , بممتی اشتر خار است که خار شتری باشد ۰ و بسضنی کوبند کیاهی است‌دوابی که آنرا سلخه خوانند . اش شتر هرع - پرنده است که بای او شراست وسنکه و آش خورد و بایابپای خود سثگه بر هر چیز که خواهد زند و خطا نکند و عربان اورا نعامه کونند . اشتر مرغ اشثر هووو « کویند جانورست مانند یا و یه ببزرکی بز کوهی میباشد و در جنگلهای 
--
leaf 354 سلخه خوانند . اش شتر هرع - پرنده است که بای او شراست وسنکه و آش خورد و بایابپای خود سثگه بر هر چیز که خواهد زند و خطا نکند و عربان اورا نعامه کونند . اشتر مرغ اشثر هووو « کویند جانورست مانند یا و یه ببزرکی بز کوهی میباشد و در جنگلهای حفرب بمیار است . اشتلث» بکر اول بر وزن خعتك , جامه‌ای را گویند که طفنلان و کودکان نو زایده را در آن یجند . اشتلا بو س امن ی و ال شبیه میای‌شثر از ولام بالف کشیده و بای ابجد بواو رسیده و بسین بی نقطه رده » بیونانی درختی ا
--
leaf 354 ه و کاه و اندر کا وروزهای کانها نامیده‌اند. باسم پنج فصل کانها « خرده اوستا ۲۱۱ > بهمین ملاحظه روز دوم مه مسترقه را نز نیز اشتود مس بشه ازسفحهٌ ۱۳۷ 4 اشتر - اوستا ۷05/52 ۰ سانسکریت ۱151۲2 « بارتولمه »4۲ - ۲۱ ۰ . بهلوی انا < اونوالا ۲۱۹ ۰ کلکی 500001 , فریزندی » بر نی, ونطنزی 051040۲ <کن . ۱ ص ۲۸۷ * ۰ سمنانی ۲لااتاکلا . منگری 251100۲ , سرخة 35040۲ . لاسگردی 265۳0007 , شهمیرزادی ٩0406‏ «که . ۷ صس ٩۱۸۳‏ , اشکاشمی 90:۲, زیاکی ۷0510001۲ . وخی ۷150۲ , سریک
--
leaf 354 ۸۳‏ , اشکاشمی 90:۲, زیاکی ۷0510001۲ . وخی ۷150۲ , سریکلی ۸480۲ . شخئی ۲ بودغا ٩1116010‏ « کربرسن ۷۳-۹5 چاربایی بار کش؛ حمل. از ۵ اشثر طاو بلنك - همان اشتر : شندهش . بوصنتی۹ . و است . ر
--
```


## [2026-10-17T00:03:06.702Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{0,10\\}باه[ \\.:(\\[].\\{0,200\\}' MON_part1.txt | head -8; grep -n 'شتر\\b\\|^خون\\| خون ' incoming/ARY/ARY_pages.txt | head -5; grep -n -i 'USHTOR\\|OSHTOR\\|SHOTOR\\|XUN\\b\\|KHUN\\b\\|BAH\\b' incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:03:08.299Z] TOOL RESULT

```
388:ارضه و اشتباه اطباء به حالت 
2333:ی میان در باه جز بره» 
3200:ر ۵ رنگ» سباه با قهوه‌یی» درخشان که در 
4513:اشتباه کر د. 
6361:ابلاع: باه [غ.] (مص‌م.) رسانیدن (نامه يا 
8459:.) سست و تباه 
8635:کردن؛ اشتباه کردن. (مص‌م.) منسوب به خطا (اين کلمه بیشتر در خراسان بخصوص مشهد 
9816:ههانه .2۳ باه -آ۳0ه 
28:شترکك» واژه‌های همريشه در زبان‌های سانسکریت و ارمنی و یونانی ولاتین و آلمانی و انگلیسی و
78:می‌شد ولی امروزه این نام بشتر برای اشاره به زبانهای بخش شمالی شبه قاره‌ی هند و به صورتث
89:برتری نژادی آنها کم شد. هر چه اين کوچگران از آلمان دورتر شدند؛ میزان آمیختگی خون آنها با
90:نژادهای «پست‌تر» بیشتر شد. بهمین دلیل در سرزمین‌های دور از آلمان درصد مردم چشم آبی و
105:نست. بیشتر مردم افریقای جنوبی به زبان انگلیسی (یعنی یک زبان هند و اروپایی) تکلم می‌کنند ولی
404:Bah 9 gall geet yo Seal 5 AS OL EL FI atin AS gE S ash >
672:Sty BOF 4 aly sa eT Og 19 (yesh y bah) slyl pli gall gos
828:bah lie od 5 9S (F obeay ClL; 9 4 09d (32 Cosel
7368:62, VEISA (NORWEGIAN) 5333 XON, XUN PAHLAVI 5 3h,
8910:LAPE, > (LITHUANIAN) gl) ROPAS, ROBAH =— (PAHLAVI) «5,4
14289:HOLD CHURCH SLAVIC) 4S 5 3%! NAXUN
14556:NUBES SUTALIAN) ol} NABAH- HAVESTAN) leu!
```


## [2026-10-17T00:03:12.153Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; python3 - <<'E'\nimport re\nt=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['XUN PAHLAVI','VOHUN','USTRA','UŠTRA','OOZE','VASA']:\n    for m in re.finditer(pat,t):\n        pre=t[:m.start()]; tags=re.findall(r'\\[pdf page (\\d+)\\]',pre)\n        print(pat,'pdf',tags[-1] if tags else None, t[max(0,m.start()-300):m.end()+200].replace('\\n',' | '));print('--')\nE"
}
```


### [2026-10-17T00:03:12.753Z] TOOL RESULT

```
XUN PAHLAVI pdf 255  55 | (SWIWE) 894, (SOW) 849 HOUCH, HOCH — (GRETON) yy | SKEAT: THI ALBANIAN) AST | (SWINE) 622, (SOW) 584 . | var i gbU oly | feetlaal | coh a9 er Waly cal a ayta cylin clang "eal eSB" 92 TF" Se tla 9 aly Ae | sdilead vaho com gh | 00ZE HENGLISH) gait VOHUNI-, VOHUNA (AVESTAN) ots! | 62, VEISA (NORWEGIAN) 5333 XON, XUN PAHLAVI 5 3h, | KEN, KWAN KURDISH) 535° | ‘REFERENCES enh HON, HUN (BALUCHI) gz 3 | POKORNY: ery) VINE, WINA — (AFGHANI) (+) sis! | BARNHART: (OOZE) 729 VASA, VASA. (SANSKRIT) cy Sie | ‘MACKENZIE: (BLOOD) 104 OLD SCAN
--
VOHUN pdf 255 AS) ple | BUCK: 160-164 su- GAULISH) J | ONIONS: HOCH, HWCH (WELSH) 55 | (SWIWE) 894, (SOW) 849 HOUCH, HOCH — (GRETON) yy | SKEAT: THI ALBANIAN) AST | (SWINE) 622, (SOW) 584 . | var i gbU oly | feetlaal | coh a9 er Waly cal a ayta cylin clang "eal eSB" 92 TF" Se tla 9 aly Ae | sdilead vaho com gh | 00ZE HENGLISH) gait VOHUNI-, VOHUNA (AVESTAN) ots! | 62, VEISA (NORWEGIAN) 5333 XON, XUN PAHLAVI 5 3h, | KEN, KWAN KURDISH) 535° | ‘REFERENCES enh HON, HUN (BALUCHI) gz 3 | POKORNY: ery) VINE, WINA — (AFGHANI) (+) sis! | BARNHART: (OOZ
--
VOHUN pdf 255 UCK: 160-164 su- GAULISH) J | ONIONS: HOCH, HWCH (WELSH) 55 | (SWIWE) 894, (SOW) 849 HOUCH, HOCH — (GRETON) yy | SKEAT: THI ALBANIAN) AST | (SWINE) 622, (SOW) 584 . | var i gbU oly | feetlaal | coh a9 er Waly cal a ayta cylin clang "eal eSB" 92 TF" Se tla 9 aly Ae | sdilead vaho com gh | 00ZE HENGLISH) gait VOHUNI-, VOHUNA (AVESTAN) ots! | 62, VEISA (NORWEGIAN) 5333 XON, XUN PAHLAVI 5 3h, | KEN, KWAN KURDISH) 535° | ‘REFERENCES enh HON, HUN (BALUCHI) gz 3 | POKORNY: ery) VINE, WINA — (AFGHANI) (+) sis! | BARNHART: (OOZE) 729 VA
--
USTRA pdf 374 (LATIN) 39 | PECORA AUTALIAN) gts! | : lentloal | 9 PEK phyla) “asin Sy "uy" ep g SHU ot oye ob ely 92 jN"0Lt" aS oH | Cody 2 CAFih POL oN sj! 9 ta) “Saal” pp 4 PANTY py | eh aly goes Sle “olay” soil 2h Jal got | SCAF pS GUT SCEAP i345 LS) SHEEP 16) y FSHU- glo! gh slat!) UT -¥ | fajlaayry SCHAF JST ~ | ewes °F | ih | USTRA SANSKRIT) 24 ibe USHRO, USHTRA {AVESTAN) pl) | VERRES, VERRIS (LATIN) yg PAHLAVI) (5 shay | VERRAT (FRENCH) sil 3 USHTAR, USHTR, USTR | [pdf page 375] | ee | REFERENCES eth VERRACO (SPANISH): gligel | POKORNY T
--
OOZE pdf 255 y cal a ayta cylin clang "eal eSB" 92 TF" Se tla 9 aly Ae | sdilead vaho com gh | 00ZE HENGLISH) gait VOHUNI-, VOHUNA (AVESTAN) ots! | 62, VEISA (NORWEGIAN) 5333 XON, XUN PAHLAVI 5 3h, | KEN, KWAN KURDISH) 535° | ‘REFERENCES enh HON, HUN (BALUCHI) gz 3 | POKORNY: ery) VINE, WINA — (AFGHANI) (+) sis! | BARNHART: (OOZE) 729 VASA, VASA. (SANSKRIT) cy Sie | ‘MACKENZIE: (BLOOD) 104 OLD SCANDINAVIAN) 34S 5-he\ | BUCK: (BLOOD) 206 VAS, VEISA | ONIONS: (OOZE) 628 WASE HOLD FRISIAN) oS S23 | SKEAT: (OOZE) 412 OLD HIGH GERMAN) «AS
--
OOZE pdf 255 2, VEISA (NORWEGIAN) 5333 XON, XUN PAHLAVI 5 3h, | KEN, KWAN KURDISH) 535° | ‘REFERENCES enh HON, HUN (BALUCHI) gz 3 | POKORNY: ery) VINE, WINA — (AFGHANI) (+) sis! | BARNHART: (OOZE) 729 VASA, VASA. (SANSKRIT) cy Sie | ‘MACKENZIE: (BLOOD) 104 OLD SCANDINAVIAN) 34S 5-he\ | BUCK: (BLOOD) 206 VAS, VEISA | ONIONS: (OOZE) 628 WASE HOLD FRISIAN) oS S23 | SKEAT: (OOZE) 412 OLD HIGH GERMAN) «AS gist | AMINDAROV: (BLOOD) 192 WASAL | vao sbi ohy WASEN (GERMAN) UST | Wer. types Bad WOS {OLD ENGLISH) oS gS: | bh . | [pdf page 256] | Yov
--
OOZE pdf 255  3h, | KEN, KWAN KURDISH) 535° | ‘REFERENCES enh HON, HUN (BALUCHI) gz 3 | POKORNY: ery) VINE, WINA — (AFGHANI) (+) sis! | BARNHART: (OOZE) 729 VASA, VASA. (SANSKRIT) cy Sie | ‘MACKENZIE: (BLOOD) 104 OLD SCANDINAVIAN) 34S 5-he\ | BUCK: (BLOOD) 206 VAS, VEISA | ONIONS: (OOZE) 628 WASE HOLD FRISIAN) oS S23 | SKEAT: (OOZE) 412 OLD HIGH GERMAN) «AS gist | AMINDAROV: (BLOOD) 192 WASAL | vao sbi ohy WASEN (GERMAN) UST | Wer. types Bad WOS {OLD ENGLISH) oS gS: | bh . | [pdf page 256] | Yov | "ou de" pee) 6 | seetlaak | Pe a Sole 35 205s
--
VASA pdf 137 ATIN) 53 | seatlooh | Pe CAE od | py ctSunr | GARUN, GARNAN (ARMENIAN) .g+,\ VANRI, VAHAR, —:(AVESTAN) (plus) | AR, EATH (GREEK) gy VAHRI, VASRI | VER, VERIS AALATIN) 3 -VAHARA — :(OLD RERSIAN) sku go | (OLD FRENCH) oS 415 WAHAR, VAHAR — (PAHLAVI) 6 ty, | PRIMEVOIRE BIHAR (KURDISH) $3, +s | PRIMAVERA SPANISH) pistol VASAR, VASAN, :(SANSKRIT) cu Site | PRIMAVERA AUTALIAN) glSte| YVASANTAS: | [pdf page 138] | wa | se | VASARA LITHUANIAN) <i} PRIMAVARA (RUMANIAN) gles) | VASARA, LATVIAN) (3) gi) VAR OLD NORSE) pS p35 | VAAR DANISH
--
VASA pdf 137 3 | seatlooh | Pe CAE od | py ctSunr | GARUN, GARNAN (ARMENIAN) .g+,\ VANRI, VAHAR, —:(AVESTAN) (plus) | AR, EATH (GREEK) gy VAHRI, VASRI | VER, VERIS AALATIN) 3 -VAHARA — :(OLD RERSIAN) sku go | (OLD FRENCH) oS 415 WAHAR, VAHAR — (PAHLAVI) 6 ty, | PRIMEVOIRE BIHAR (KURDISH) $3, +s | PRIMAVERA SPANISH) pistol VASAR, VASAN, :(SANSKRIT) cu Site | PRIMAVERA AUTALIAN) glSte| YVASANTAS: | [pdf page 138] | wa | se | VASARA LITHUANIAN) <i} PRIMAVARA (RUMANIAN) gles) | VASARA, LATVIAN) (3) gi) VAR OLD NORSE) pS p35 | VAAR DANISH) jal | ‘
--
VASA pdf 137  .g+,\ VANRI, VAHAR, —:(AVESTAN) (plus) | AR, EATH (GREEK) gy VAHRI, VASRI | VER, VERIS AALATIN) 3 -VAHARA — :(OLD RERSIAN) sku go | (OLD FRENCH) oS 415 WAHAR, VAHAR — (PAHLAVI) 6 ty, | PRIMEVOIRE BIHAR (KURDISH) $3, +s | PRIMAVERA SPANISH) pistol VASAR, VASAN, :(SANSKRIT) cu Site | PRIMAVERA AUTALIAN) glSte| YVASANTAS: | [pdf page 138] | wa | se | VASARA LITHUANIAN) <i} PRIMAVARA (RUMANIAN) gles) | VASARA, LATVIAN) (3) gi) VAR OLD NORSE) pS p35 | VAAR DANISH) jal | ‘REFERENCES beh VAR (SWEDISH) «53h p+ | POKORNY SS ~ 4 VAR
--
VASA pdf 138 plus) | AR, EATH (GREEK) gy VAHRI, VASRI | VER, VERIS AALATIN) 3 -VAHARA — :(OLD RERSIAN) sku go | (OLD FRENCH) oS 415 WAHAR, VAHAR — (PAHLAVI) 6 ty, | PRIMEVOIRE BIHAR (KURDISH) $3, +s | PRIMAVERA SPANISH) pistol VASAR, VASAN, :(SANSKRIT) cu Site | PRIMAVERA AUTALIAN) glSte| YVASANTAS: | [pdf page 138] | wa | se | VASARA LITHUANIAN) <i} PRIMAVARA (RUMANIAN) gles) | VASARA, LATVIAN) (3) gi) VAR OLD NORSE) pS p35 | VAAR DANISH) jal | ‘REFERENCES beh VAR (SWEDISH) «53h p+ | POKORNY SS ~ 4 VAR NORWEGIAN) 5333 | DELAMARRE: (PRINT
--
VASA pdf 138 AALATIN) 3 -VAHARA — :(OLD RERSIAN) sku go | (OLD FRENCH) oS 415 WAHAR, VAHAR — (PAHLAVI) 6 ty, | PRIMEVOIRE BIHAR (KURDISH) $3, +s | PRIMAVERA SPANISH) pistol VASAR, VASAN, :(SANSKRIT) cu Site | PRIMAVERA AUTALIAN) glSte| YVASANTAS: | [pdf page 138] | wa | se | VASARA LITHUANIAN) <i} PRIMAVARA (RUMANIAN) gles) | VASARA, LATVIAN) (3) gi) VAR OLD NORSE) pS p35 | VAAR DANISH) jal | ‘REFERENCES beh VAR (SWEDISH) «53h p+ | POKORNY SS ~ 4 VAR NORWEGIAN) 5333 | DELAMARRE: (PRINTEMPS) 196 (OLD CHURCH SLAVIC) 485391 | (MACKENZIE: (
--
VASA pdf 214 , YUVAN = (PAHLAVI) 5h, YUVAN, YONO = {AVESTAN) p=! | [pdf page 214] | os | | NNO | tse het ye | | UNG (SWEDISH) 5-8 y= JIWAN, JUVAN (KURDISH) 62,5 | UNG (NORWEGIAN) 8335 JAVAN X(BALUCHI) gz sh | JONG DUTCH) gala = ZWAN, JAVAN. (AFGHAND) (+4) gsi | :(OLD CHURCH SLAVIC) 34S 5.33! yuvas, (SANSKRIT) <4 Site | JUNT YUVASAS, YUVAN, YONAS, JUVACAS | JUNYJ (RUSSIAN) 53 ARMENIAN) gs, | (LITHUANIAN) gly YAVANAK, YOVANAK, | JAUNAS, JAUNIKIS JUVENCUS, JUVENIS (LATIN) 53 | JAUNS (LATVIAN) (3) 3 JEUNE FRENCH) «i | (OLD IRISH) gS 54) 3) 
--
VASA pdf 255 ta cylin clang "eal eSB" 92 TF" Se tla 9 aly Ae | sdilead vaho com gh | 00ZE HENGLISH) gait VOHUNI-, VOHUNA (AVESTAN) ots! | 62, VEISA (NORWEGIAN) 5333 XON, XUN PAHLAVI 5 3h, | KEN, KWAN KURDISH) 535° | ‘REFERENCES enh HON, HUN (BALUCHI) gz 3 | POKORNY: ery) VINE, WINA — (AFGHANI) (+) sis! | BARNHART: (OOZE) 729 VASA, VASA. (SANSKRIT) cy Sie | ‘MACKENZIE: (BLOOD) 104 OLD SCANDINAVIAN) 34S 5-he\ | BUCK: (BLOOD) 206 VAS, VEISA | ONIONS: (OOZE) 628 WASE HOLD FRISIAN) oS S23 | SKEAT: (OOZE) 412 OLD HIGH GERMAN) «AS gist | AMIN
--
VASA pdf 255 in clang "eal eSB" 92 TF" Se tla 9 aly Ae | sdilead vaho com gh | 00ZE HENGLISH) gait VOHUNI-, VOHUNA (AVESTAN) ots! | 62, VEISA (NORWEGIAN) 5333 XON, XUN PAHLAVI 5 3h, | KEN, KWAN KURDISH) 535° | ‘REFERENCES enh HON, HUN (BALUCHI) gz 3 | POKORNY: ery) VINE, WINA — (AFGHANI) (+) sis! | BARNHART: (OOZE) 729 VASA, VASA. (SANSKRIT) cy Sie | ‘MACKENZIE: (BLOOD) 104 OLD SCANDINAVIAN) 34S 5-he\ | BUCK: (BLOOD) 206 VAS, VEISA | ONIONS: (OOZE) 628 WASE HOLD FRISIAN) oS S23 | SKEAT: (OOZE) 412 OLD HIGH GERMAN) «AS gist | AMINDAROV:
--
VASA pdf 378 T SHUSH, SUSH PAHLAVI] 5 3h44 | KwAs (TOKHARIAN A) A 5,\55 PISHIK (KURDISH) 53,5 | [pdf page 378] | | YA | pts | HVASE (DUTCH) ihe CVAS, SHVASITI :(SANSKRIT) 24 Sil. | SHUSHINTI (LITHUANIAN) 53, SHUNCH ARMENIAN) + | QUEROR, QUERI S(LATIN) 3 | REFERENCES beth HOLD SCANDINAVIAN) 245 5-thes) | POKORNY, = ==S*S*~*«S HVASA | BARNHART: (WHEEZE) 1230 HOLD ENGLISH) pf gS: | MACKENZIE: (LUNG) 122 HWOSAN, HWAST | ‘MALLORY & ADAMS: KUESH WHEEZE ENGLISH) 5-83) | ev ebb ob, VASA SWEDISH) $2 y= | HVESE, KVESE (NORWEGIAN) 533, | sethsl | AAS 
--
VASA pdf 378 NSKRIT) 24 Sil. | SHUSHINTI (LITHUANIAN) 53, SHUNCH ARMENIAN) + | QUEROR, QUERI S(LATIN) 3 | REFERENCES beth HOLD SCANDINAVIAN) 245 5-thes) | POKORNY, = ==S*S*~*«S HVASA | BARNHART: (WHEEZE) 1230 HOLD ENGLISH) pf gS: | MACKENZIE: (LUNG) 122 HWOSAN, HWAST | ‘MALLORY & ADAMS: KUESH WHEEZE ENGLISH) 5-83) | ev ebb ob, VASA SWEDISH) $2 y= | HVESE, KVESE (NORWEGIAN) 533, | sethsl | AAS oh ee a La 625 ob rl Lale® lads 92 05a cal pe | op AOU 2 Ns atl ee | HS 52S 4393 todY O05 22 05 cal | | SEXTOTA, SEXTO XSHTVA HAVESTAN) plans! | SAIHST
--
VASA pdf 520 KEN (GERMAN) gal | deadloal | apts oe po Sina) “shoe 2 Sid ea olds 2 zl tN | Cad Sy CS get ge WERE 528 9 gi 9 uss 3 IF 252,545 22 139 al eV | — | [pdf page 520] | ONT C5 IS" 6 4) shas ding | VOL (4LE}(SERBIAN) 0 VARZA, WARZAG PAHLAVI) 5 Jha, | VOL (4L¢}(BOHEMIAN) gun y WERSA KURDISH) 53,5 | VERSHIS (LITHUANIAN) (gy VASA, VRSABHA (SANSKRIT) cy Sil. | VERSIS LATVIAN) (3) gs VACCA LATIN) 553 | VACHE FRENCH) Wit | REFERENCES bethany VACA SPANISH) glityal | POKORNY VACCA AUTALIAN) «gly! | BARNHART: (VACCINE) 1191 VACA (RUMANIAN) g
--
```


## [2026-10-17T00:03:18.542Z] TOOL CALL #27: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-17T00:03:18.551Z] TOOL RESULT

```

```


## [2026-10-17T00:03:21.102Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/خون",
 "prompt": "Give the Persian etymology section verbatim (Middle Persian, Proto-Iranian, PIE forms, cognates)."
}
```


## [2026-10-17T00:03:21.943Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/شتر",
 "prompt": "Give the Persian etymology section verbatim (Middle Persian, Avestan, Proto-Iranian, PIE forms)."
}
```


## [2026-10-17T00:03:22.742Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ooze",
 "prompt": "Give the etymology of ooze (noun and verb) verbatim, especially Old English wos and PIE root."
}
```


## [2026-10-17T00:03:23.805Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Zarathustra",
 "prompt": "Give the etymology of the name (Avestan Zaraθuštra), including all proposed interpretations of zarat- and uštra."
}
```


## [2026-10-17T00:03:24.761Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/باه",
 "prompt": "Give the Arabic and Persian etymology sections verbatim for باه (bāh), meaning sexual potency/coitus."
}
```


## [2026-10-17T00:03:25.581Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/उष्ट्र",
 "prompt": "Give the Sanskrit etymology section verbatim (Proto-Indo-Iranian, PIE root, meaning buffalo/camel)."
}
```


### [2026-10-17T00:03:26.313Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:03:29.091Z] TOOL RESULT

```
# Etymology of Zarathustra

Based on the Wiktionary content provided, I can only offer limited etymological information:

The page states that "Zarathustra" comes "From German _Zarathustra_, from Avestan _𐬰𐬀𐬭𐬀𐬚𐬎𐬱𐬙𐬭𐬀_ (zaraθuštra)."

However, **the document does not provide the proposed interpretations of the Avestan components** (zarat- and uštra) that you've requested. The Wiktionary entry only traces the etymological lineage back to Avestan without explaining the meanings or scholarly interpretations of these individual morphological elements.

To find detailed analyses of what "zarat-" and "uštra" signify in Avestan and how scholars have interpreted them, you would need to consult specialized etymological resources or academic works on Zoroastrianism and ancient Iranian languages.
```


### [2026-10-17T00:03:29.641Z] TOOL RESULT

```
# Persian Etymology Section

According to the Wiktionary entry, the Persian word شتر (šotor) derives from "Middle Persian [script needed] (GMRA, ʾwštl /⁠uštar⁠/, 'camel'), from Proto-Iranian *úštrah, from Proto-Indo-Iranian *úštras."

The etymological chain traces backward through:
- **Proto-Indo-Iranian**: *úštras
- **Proto-Iranian**: *úštrah
- **Middle Persian**: uštar

The entry notes that the Middle Persian form requires a script specification but provides the transliteration and phonetic value. No Avestan form is explicitly mentioned in this Persian etymology section.
```


### [2026-10-17T00:03:30.704Z] TOOL RESULT

```
# Etymology Information for باه (bāh)

Based on the Wiktionary content provided, there is **no Persian etymology section** for this entry. The page only contains etymology information for **Arabic** and **Sindhi**.

## Arabic Etymology

**Etymology 1.1:** The article states that بَاهَ (bāha) as a verb meaning "to have carnal knowledge of" compares to related Arabic terms including "بَهَأ (bahaʔ, 'to like the nearness of, to be familiar with')."

**Etymology 1.2:** This section provides a noun definition. The entry notes that "بَاه (bāh)" refers to "carnal knowledge, coitus" and "the faculty of carnal knowledge, venereal capacity, libido," with a historical quotation from a 1222 Islamic text.

## Note

The page header indicates this entry exists in multiple language versions (including Persian/فارسی on fa.wiktionary.org), but the English Wiktionary version shown does not include a separate Persian etymology section.
```


### [2026-10-17T00:03:31.366Z] TOOL RESULT

```
# Persian Etymology of خون (xūn)

## Middle Persian Origin
The word derives from Middle Persian **𐭣𐭬𐭩𐭠** (DMYA /⁠xōn⁠/) and alternative form **𐫑𐫇𐫗** (k̇wn /⁠xōn⁠/).

## Proto-Iranian Root
The ultimate source is Proto-Iranian **\*wahūnī**, meaning blood.

## Cognates Across Related Languages
The term shares ancestry with multiple Iranian and related language families:

- **Bakhtiari**: خین (xīn)
- **Northern Luri**: خی (xi)  
- **Kurdish dialects**: xwîn (Northern), خوێن (Central), xün (Southern)
- **Baluchi**: ہون (hōn)
- **Pashto**: وینه (wina)
- **Zazaki**: goni
- **Sogdian**: γwrn or wγrn
- **Yaghnobi**: вахм (vaxm)
- **Avestan**: 𐬬𐬊𐬵𐬎𐬥𐬀 (vohuna)

This widespread distribution across Indo-Iranian languages demonstrates the ancient pedigree of this blood-related vocabulary.
```


### [2026-10-17T00:03:32.076Z] TOOL RESULT

```
# Sanskrit Etymology of उष्ट्र

According to the Wiktionary entry, the etymology section states:

"Inherited from Proto-Indo-Iranian *úštras. See there for more. Cognate with Avestan 𐬎𐬱𐬙𐬭𐬀 (uštra), Old English ūr."

The word refers to a camel or buffalo. The entry indicates this Sanskrit term descends from a Proto-Indo-Iranian source, with related forms appearing in other ancient Indo-European languages like Avestan and Old English.
```


## [2026-10-17T00:03:35.203Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/úštras",
 "prompt": "Give the etymology section verbatim (proposed PIE origins, e.g. *wes- 'wet', *h2wes-, Old English ūr, any alternatives)."
}
```


## [2026-10-17T00:03:36.204Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wahūnī",
 "prompt": "Give the etymology section verbatim (PIE root, cognates like Sanskrit vasā) and descendants list."
}
```


## [2026-10-17T00:03:37.412Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ooze",
 "prompt": "Give etymologies verbatim for ooze (both noun senses and verb), Old English wōs, Proto-Germanic, PIE."
}
```


## [2026-10-17T00:03:38.437Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/zoroaster-i-the-name",
 "prompt": "Summarize the proposed interpretations of the name Zaraθuštra (uštra 'camel', zarat- 'old', 'yellow', 'angry', 'driving' etc.) and which scholars hold each; quote key phrases."
}
```


### [2026-10-17T00:03:39.084Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:03:42.055Z] TOOL RESULT

```
# Etymology of "Ooze"

## Noun (Etymology 1)
**Old English:** "wōs" (sap, froth)
**Proto-Germanic:** "*wōsą"
**Proto-Indo-European:** "*wóseh₂" (sap)

## Verb (Etymology 1)
**Old English:** "wōsan"
**Proto-Germanic & PIE:** Same lineage as the noun

## Noun (Etymology 2 - soft mud/marine sediment)
**Old English:** "wāse" (mud, mire)
**Proto-West Germanic:** "*waisā"
**Proto-Germanic:** "*waisǭ"
**Proto-Indo-European:** "*weys-" (to flow)

The first etymology traces to words meaning sap or secretion, while the second stems from roots meaning mud or flowing.
```


### [2026-10-17T00:03:43.462Z] TOOL RESULT

```
# Etymology Section of Proto-Indo-Iranian *úštras

The etymology remains uncertain, with three proposed origins:

1. **From PIE *úǵtr-o-s**: Derived from *uǵ-tḗr ~ *uǵ-trés plus *-os, ultimately from *weǵ- "to increase; to be strong" plus *-tḗr

2. **From PIE *ústr-o-s**: Derived from *us-tḗr ~ *us-trés "inseminator" plus *-os, from *wes- "wet, damp" plus *-tḗr

3. **Substrate borrowing**: Possibly borrowed from a substrate language, potentially related to PIE *ūsros "aurochs," comparable to Proto-Germanic *ūraz with the same meaning
```


### [2026-10-17T00:03:43.765Z] TOOL RESULT

```
# Etymology and Descendants of Proto-Iranian *wahuHniH

## Etymology Section

The page states: "The ultimate etymology is uncertain but is probably connected to Latin _vēna_ 'blood-vessel', via a reconstruction Proto-Italic _*uesnā-_."

The entry does not include a PIE root or Sanskrit cognates. The only comparative evidence provided links this term to the Latin word for blood-vessel through Proto-Italic reconstruction.

## Descendants List

The descendants branch across five major Iranian subgroups:

**Central Iranian**: Younger Avestan forms (vohuna, vohunī)

**Northeastern Iranian**: Khwarezmian, Sogdian (Buddhist/Christian/Manichaean variants), and Yaghnobi (vaxm)

**Southeastern Iranian**: Pashto (wína)

**Northwestern Iranian**: Baluchi, Kurdish dialects, Medo-Parthian languages including Middle Median, Parthian, and Zaza-Gorani branches

**Southwestern Iranian**: Middle Persian (xōn) with modern descendants in Persian, Dari, Tajik, and Lurish varieties
```


## [2026-10-17T00:03:47.298Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Zoroaster",
 "prompt": "Quote verbatim the Name/etymology section about Zaraθuštra: interpretations of uštra 'camel' and zarat- (old, yellow, angry, driving etc.), scholars named."
}
```


## [2026-10-17T00:03:48.167Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=باه&d=moein",
 "prompt": "Quote verbatim the Mo'in entry for باه, especially its origin tag ([ع.] Arabic etc.) and meanings."
}
```


### [2026-10-17T00:03:50.689Z] TOOL RESULT

```
# Mo'in Dictionary Entry for باه

According to the Mo'in Dictionary (فرهنگ انتشارات معین), the entry reads:

**Origin:** "[ ع . ]" (Arabic origin)

**Definition:** "غریزة جنسی ، نیروی شهوت" (sexual instinct, the force of desire)

The term refers to the sexual drive or the power of carnal appetite in Persian.
```


### [2026-10-17T00:03:55.158Z] TOOL RESULT

```
# Name and Etymology: Zaraθuštra Interpretations

## Camel Component
The second part of the name derives from the Indo-Iranian root for 'camel', making the full meaning "he who can manage camels."

## Zarat- Element Interpretations
Scholars have proposed several meanings for the *zarat-* component:

**"With old/aging camels"** - Related to Avestic *zarant-* (meaning 'old'), connecting to Pashto and Ossetian terms for aged animals.

**"With angry/furious camels"** - From Avestan *zarant-*, meaning 'angry, furious'.

**"Driving or fostering camels"** - Associated with Avestan *zarš-*, meaning 'to drag'.

**Desire-based interpretation** - Mayrhofer proposed "who is desiring camels" or "longing for camels," relating to Vedic Sanskrit *har-* ('to like').

**"With yellow camels"** - Parallel to Younger Avestan *zairi-*.

## Notable Scholars Mentioned
The text cites **Mayrhofer**, **Markwart**, and **Rüdiger Schmitt** among linguists analyzing these etymological possibilities.

[WebFetch note: this page's text is 190848 characters long and the answer above covers only characters 0 to 100000; the final 90848 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-17T00:04:23.888Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'ooze\\|OOZE' AHD_watkins1985.txt | head; grep -n -i '^OOZE\\|^ooze' SKT.txt KLN_1966.txt | head; grep -n -i 'u̯es\\|ues-' WLD_band3.txt | head -3; grep -n -i 'ustra\\|uštra\\|vohun\\|wōs\\b\\|wos ' WLD_band3.txt | head"
}
```


### [2026-10-17T00:04:24.691Z] TOOL RESULT

```
1000:stag-. To seep, drip. Possible root. 1. Latin stagnum, pond, swamp: STAGNANT. 2. Suffixed form *stag-yo- in Greek stazein, to ooze, drip: STACTE; EPIsTaxis. [Pok. stag- 1010.]
KLN_1966.txt:26303:ooze
KLN_1966.txt:26348:ooze,  n.,  1)  an  oozing;  2)  something  that  oozes; 3)  liquor  used  in  tanning  leather.  —  ME.  wose, wos,  fr.  OE.  wos,  ‘sap,  juice’,  rel.  to,  and  in-
KLN_1966.txt:26349:ooze
3105:200". modrig sein4, «l- 162. munket qotlo~ 455. Mase he tmer- 272* Molus weg ere J- « G37. niaasjy geri- 421 Pag". risa. Mast mucdo-e 235% Mohrriibo | mpk- 313* noy® 340%, mitt klem 498. | Molken Nadel dhelg- 808 mourc- 223", | Monat mbvica- 271°. (von Pitanzen)  (Ha-} 430", | Morgenriie = aues- 2th. fig oua* Mauer 7. yer- 230. morsch worden ger- G1), Nodelbiume 2. el(ew)- 162. dhaigh $33. | morschon 1b. merg- 281%, | oiben dhergh- 803, MmAGern dheigh- 833. | mucksen s00*, apa- SLs" Maul wf- 200°, Micke sno. aR aud- (fd" Mauleszet mn A = eA | > JTL". ) nhhres 2, al. f $11", iniide werden 4. Bema") 2, Fer- 408 Maus gdi- G30 -  pl- 72" més 312*. | Mahe haben mi 258 Niisse Letap. 706 Meakern . ona" mihen refl, 2. ye 225 - wmely. 207" Moar jot = o ben 308 Nagel - 180 aes oq ma- 201" wet guréugh- WOT, Moh} ve 519, | Méinduny dus 168. nk B60". Mohilj bret) 13. pal. 6 ith*. miirrisch  l, agend- 55d", | nagendes Gewirm |. mal- meinen a 302", | muhen mi. 200°. a ee, tmclken &, o Mi. pi La welled el lial 4 =" a noerien pen 25". Peon) LL to HEME ore. Motall + fer- S00. Cl, Mr Oe ame Milbe pela‘ Milch mdg- 224", lad- 381", inih- 305", L. ee 439". sty 2. ei B07". Thane SM),
535:= “ make, oo". anieoor 68°. sélua & néity 68". miso, Teds a miedo als, (541). oy 161" 162*. Harboe eH} méroin, adres (G61*). rin ; aérre 26%. preton, airog GO". aersvione - 143. eth za aéog BB". Figew thous. (40*), seman dor, 36, anoiay pamph, (44*), nop 6". anpoar &*. AETAT (Ga abe 56") aa* Tarye, 19", séntai 17*., tio 17T*. : eaciew att. 3)* age (Lod), Gna", nega 32 eal, oan = T . = : , Maoh BT". céotroc fid*, made 14* aoc B45 Ivete ayo?) 85" eet yo (B5*). rt nt, 74%, 2 a6. aetenic B10. aodiosdse| hy 400 mitioe OTF. 7a att, O16 snout 610, noimiiog 9. ois 72. pa | 600. aio; S20, sagamds 45%, (2T5"), togicn Bl". aépwos 45". noxa dor, 10, at ty? too: 16", 39", aijagos 54° hell, 50*. THT DOF mossti S15, 6), 21", aT (73%), 74*, cms 53*_ o*. mpadalg TO mA, attic 51".
```


## [2026-10-17T00:04:28.497Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 26348,26352p KLN_1966.txt; grep -n -i -A3 '^OOZE' SKT.txt | head; grep -n -i '^wes-\\|^\\*wes\\|^wes ' AHD_watkins1985.txt | head; grep -n -i 'wes-' AHD_watkins1985.txt | head; grep -n -i -A12 'BLOOD' SYN.txt | grep -i -n 'vohun\\|xun\\|xūn\\|vasa' | head"
}
```


### [2026-10-17T00:04:29.111Z] TOOL RESULT

```
ooze,  n.,  1)  an  oozing;  2)  something  that  oozes; 3)  liquor  used  in  tanning  leather.  —  ME.  wose, wos,  fr.  OE.  wos,  ‘sap,  juice’,  rel.  to,  and  in-
ooze
opiate
fluenced  by,  OE.  wdse,  ‘soft  mud,  mire' ;  rel,  also to  OS.  waso,  ‘wet  ground,  mire',  ON.  veisa,  ‘pond of  stagnant  water’,  and  prob.  cogn.  with  OI. vifdm,  ‘poison’,  Gk.  to 5  (for  *Fta6;),  L.  virus (for  *visos),  ‘poison’.  See  virus.
Derivative:  ooze ,  intr.  v.,  to  flow  slowly,  drip, exude,  percolate;  tr.  v.,  to  emit  by  oozing, ooze,  n.,  soft  mud,  mire.  —  ME.  wose,  fr.  OE. wdse,  ‘soft  mud,  mire’,  rel.  to  OE.  wos,  ‘sap, juice’.  See  prec.  word.
133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
1157:wes-!
1159:wes-1. To buy. 1. Suffixed form *wes-no- in Latin vénum, sale: VENAL, VEND. 2. Suffixed o-grade form *wos-nd- in Greek dneisthai, to buy: DUOPSONY. [Pok. 8. wes- 1173.]
1160:wes-?. Wet. Germanic *wdés- in Old English wés, juice: 00ZE}. [Pok. 3. wes- 1171.]
1161:wes-3. To stay, dwell, pass the night, with derivatives meaning “to be.” 1.O-grade form *wos- in Germanic *was- in Old English wes, was: was. 2. Length- ened-grade form *wés- in Germanic *wéz- in Old English wére (subjunctive), w#ron (plural), were: WERE. 3. Ger- manic *wesan in Old Norse vesa, vera, to be: WASSAIL. 4. Suffixed form *wes-td- perhaps in Latin Vesta, house- hold goddess: Vesta. 5. Suffixed variant form *was-tu- possibly in Greek astu, town (< “place where one dwells”), whence Latin astus, skill, craft (practiced in a town): ASTUTE. [Pok. 1. wes- 1170.]
1162:wes-‘. To clothe. Extension of eu-'. 1. Suffixed o-grade form *wos-eyo- in Germanic *wazjan in Old English werian, to wear, carry: WEAR}, 2. Suffixed form *wes-ti- in Latin vestis, garment: VEST; DEVEST, INVEST, REVEST, TRAVESTY. 3. Suffixed form *wes-nu- in Greek hennunai, to clothe: HIMATION. [Pok. 5. wes- 1172.]
1163:wes-pero-. Evening, night. I. Reduced form “wes-. 1. Suffixed form *wes-to- in Germanic *west- in: a. Old English west, west: WEST; b. Old English westerne, western: WESTERN; C. Old English westra, more west- erly: WESTERLY. 2. Possibly Germanic *wis- in Late Latin Visigothi, “West Goths” (Gothi, the Goths): Vist- GorTu. II. Basic form *wespero-. 1. Latin vesper, evening: VESPER, VESPERTILIONID. 2. Greek hesperos, evening: HESPERIAN. [Pok. wesperos 1173.]
133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
171:Indo-European had a verb “‘to cook” (pekv-, also having the notion “to ripen’’) and an adjective “raw” (om-). Another op- eration is denoted by peis-', “to crush.” Meat (méms-) was an established item of diet, and some sort of sauce or broth is indi- cated by the term yeue- (*yii-s-, JUICE, from Latin). Other household activities included spinning ((s)né-'), weaving, (webh-) and sewing (syd-). The verb wes-* (WEAR) is ancient and everywhere attested. The Indo- European garment was probably belted: y6és-, “to gird.”
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
468:in-, in, on; see en): ENDUE. 2. Latin exuere, to doff (ex-, off; see eghs): EXUVIAE. 3. Latin reduvia, fragment (red-, back, in reverse; see re-): REDUVIID. See extension wes-‘. [Pok. 2. eu- 346.]
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
1157:wes-!
114:5427:Goth. 5/6, Lith. kraujas ae ec ee) ON 3s Lett. asins Lat. sanguts, cruor Dan. blod ChSl.  kritvy It. sangue Sw. blod SCr.  krv Fr. sang OE blod Boh.  krev Sp. sangre ME _sblode Pol. krew Rum. singe NE blood (gore) Russ. krov’ Tr. fuil, crit Du. bloed Skt. asan- (Ved.), rakta-, Nir. futl, cro OHG _bluot rudhira-, ete, W. gwaed (crau) MHG bluot Av. vohuni- Br. gwad NHG  Dlut
133:5446:Av. vohuni- (NPers. xin ‘blood’), etym.? Barth. 1434.
```


## [2026-10-17T00:04:34.905Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/550.jpg 2>/dev/null; pdftoppm -f 550 -l 550 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg550 && echo ok"
}
```


### [2026-10-17T00:04:36.146Z] TOOL RESULT

```
site/pages/550.jpg
ok
```


## [2026-10-17T00:04:39.470Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg550.png"
}
```


### [2026-10-17T00:04:39.966Z] TOOL RESULT

```

```


## [2026-10-17T00:04:39.933Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:04:50.502Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg550.png data/verification/sources/refs/ocr/BOOK/550.png\nfor u in 'https://en.wiktionary.org/wiki/خون|page 550, Wes 1, Persian xun < MP xon < PIr *wahuni' 'https://en.wiktionary.org/wiki/شتر|page 550, Wes 1, Persian sotor/ostor < MP ustar < PIr *ustrah' 'https://en.wiktionary.org/wiki/Zarathustra|page 550, Wes 1, Zarathustra < Avestan zaraθustra' 'https://en.wiktionary.org/wiki/باه|page 550, Wes 1, Arabic bah coitus, libido' 'https://en.wiktionary.org/wiki/उष्ट्र|page 550, Wes 1, Skt ustra < PIIr *ustras' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/úštras|page 550, Wes 1, origin of *ustras (three hypotheses incl. *wes- wet inseminator)' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wahūnī|page 550, Wes 1, PIr *wahuHniH blood, etymology uncertain' 'https://en.wiktionary.org/wiki/ooze|page 550, Wes 1, ooze < OE wos < PGmc *wosa' 'https://en.wikipedia.org/wiki/Zoroaster|page 550, Wes 1, interpretations of the name Zaraθustra' 'https://vajehyab.com/?q=باه&d=moein|page 550, Wes 1, Moin: bah [ع.] Arabic'; do python3 tools/fetch_source.py \"${u%%|*}\" --note \"${u#*|}\" 2>&1 | tail -1; done"
}
```


### [2026-10-17T00:04:53.901Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f571e2cc1cd37d91.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/71c751188481983e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5736e12792dac7d1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/eeffb625980c0544.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/550108625dfebbe6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0b05c642a6b56c10.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/219fbcbeb6e0acb9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ac1a6b951184fd79.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f33419e7f57e0efc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b2580b0735eae1a1.txt
```


## [2026-10-17T00:05:09.594Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; python3 - <<'E'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'u[sṣš][tṭ]r[aā]',r'vohun',r'Kamel']:\n    for m in list(re.finditer(pat,t))[:3]:\n        print(pat,'leaf',t[:m.start()].count('\\f')+1,'::',t[max(0,m.start()-300):m.end()+200].replace('\\n',' '));print('--')\nE"
}
```


### [2026-10-17T00:05:10.306Z] TOOL RESULT

```
u[sṣš][tṭ]r[aā] leaf 36 ::                       *ausi „in der Morgenfriihe singend“)    lat. aurora „Morgenrote“ (fur *ausds - oris vgl. Flora flf<s )                                                             ,      a aster „Siid-                                                                         ,    :   ;   wind“, australis „8iidlieh“ (zur Bed. s. Vf. LEWb. 2 s. v.); vermutlich aucli durum, sabin. ausom „Gold“ als „*rotlich“ (s. Yf. LEWb. 2 s. v.)                         ;                                             
--
u[sṣš][tṭ]r[aā] leaf 150 :: nicht nach Meringer IF. 18,248 „ackernd“; von „freigebig‘                                                                                                                                                           !     aus vielleieht auch got. arwjo ,,unentgeltlich, umsonst", ahd. araivun „gratis, frustra'Grienberger Unt. 29 f., Fick III 4 17), ags. arod ,kraftvoll, flink‘\            -       Ags. reow „aufgeregt, sturmisch, wild, rauh“, umnana-riggics „wild, grau- sam“ (Holtbausen IF. 20, 328 s. auch
--
u[sṣš][tṭ]r[aā] leaf 160 ::                        *uliso ), ndl. els ds.; altn. elri n., elrir m., air, qlr (*ahiz)                                            :    elre           *nlizo ), else                ;                (                           ( ds.,       ags. alor  Das idg. e der \Vz. wird durch aisl. jqlstr (*t lustra)                                  ds. „Erle‘' und Ustre „ Weide, Salix pentandra“ (*elis-tr-jo -) mhd. dial. Mister                                                        ,  halster ds. mit sekund.  
--
Kamel leaf 258 :: es. zd  vazdra- „der vorwarts bringt", say-uzdri- EN. eig. „da6 weibliche Zugtierc scheckig sind" ( *uzdrl f. zu *uzdar        Bartholomae Airan. Wb. 1572; aber ai. iistur -, astdr- „Pflugstier", Bthl. 1392, ist nicht fiir *uzdar-, *ndhar-  eingetreten, sondern wohl ursprgl. mit uitra- m. „Biiffel, Kamel", av. ustra- „Kamel“ verwandt, woriiber eine Yermutung bei Uhlcnbeck Ai. Wb. 3 1 f.) ai. vaha- „fiihrend, tragend",      m. „Zugtier, Yehikel", av. vuza- „fahrend. fliegend", m. „Ziehen, Zug, Zugtier
--
Kamel leaf 258 ::  vorwarts bringt", say-uzdri- EN. eig. „da6 weibliche Zugtierc scheckig sind" ( *uzdrl f. zu *uzdar        Bartholomae Airan. Wb. 1572; aber ai. iistur -, astdr- „Pflugstier", Bthl. 1392, ist nicht fiir *uzdar-, *ndhar-  eingetreten, sondern wohl ursprgl. mit uitra- m. „Biiffel, Kamel", av. ustra- „Kamel“ verwandt, woriiber eine Yermutung bei Uhlcnbeck Ai. Wb. 3 1 f.) ai. vaha- „fiihrend, tragend",      m. „Zugtier, Yehikel", av. vuza- „fahrend. fliegend", m. „Ziehen, Zug, Zugtier" (: got. urgs), ai.
--
Kamel leaf 317 :: n, wie vdga-m ,,flussiges Fett“, Charpentier KZ. 46, 40 f.).    Hierher mit der Bed. „mannliches Tier“ (ygl. lat. verves usw. uer-, uer-s-                :     „feuchten“) nach Johansson IF. 2, 60 ff. ai. usrd-h „Stier“ (sekundar usrd  „Kuh“), ustra-h „Biiffel“, us tar- „Pflugstier“. av. ustra- m. „Kamel“ (sekun-  dar ustra, ustrl „Kamelstute“).    4.    ues- „stechen“?         nivasita-h „ums Leben gebracht“, nirvasana-m „das Ermorden,       Ai.  Toten “ parivOsayati „schneidet rings ab, aus“ u. dgl
--
```


## [2026-10-17T00:05:13.667Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==317' WLD_Bd1_pages.txt | tr -s ' ' | grep -n -i -B6 'flussiges Fett' | head -20"
}
```


### [2026-10-17T00:05:14.298Z] TOOL RESULT

```
50- gr. eager ‘
51- kovzfjoa, Tj zigoyovv Hes., alt-theraisch heaga (IG. XI 1/3 450,
52-Sommer Gr. Ltst. It 9), umbr. vestihatu „libato“ (Bildung wie lat. lectlca,
53-Sommer aaO.).
54- Yermutlich ay. vanhu-tat- f. „Blut“, vatohu&wa- n. ..BlutvergieBen, blutiger
55-Streit“, vohana- m. „Blut“ und ai. vasa, vasd „Speck, Fett, Sehmalz a (auch
56: vaga geschrieben, wie vdga-m ,,flussiges Fett“, Charpentier KZ. 46, 40 f.).
```


## [2026-10-17T00:07:03.062Z] TOOL CALL #47: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-550.json",
 "content": "{\n  \"pdf_page\": 550,\n  \"book_page\": 520,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Wes 1, Wesâ, Wâs, Wôs, Wôsos\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *wes- (Pokorny 3. u̯es-) 'wet, moist'; o-grade/lengthened *wōs-(o-) 'sap, juice'; Pokorny also tentatively files here words for 'male animal' (Skt. uṣṭra-, Av. uštra-)\",\n      \"note\": \"Pokorny pp. 1171-1172 (3. u̯es- 'feucht, naß') lists exactly this material: OE wōs 'juice, sap' > ooze; 'presumably' Av. vaŋhu-tāt- 'blood', vohuna- 'blood', Skt. vasā 'fat'; and 'here with the meaning male animal' Skt. uṣṭra- 'buffalo, camel', Av. uštra- 'camel' (also in Zaraθuštra). Watkins/AHD has wes-2 'wet' (only OE wōs > ooze). Root, label and the gloss 'wet, also male animal' faithfully reproduce Pokorny; the 'male animal' and 'blood' attachments are Pokorny's own hedged suggestions (from Johansson IF 2) and are not accepted as certain today (Wiktionary gives *wes- 'wet' only as one of three hypotheses for *úštras; PIr *wahuHnīH is called of uncertain etymology). The Persian bāh 'sexual drive' is Mann's addition (IEC 1495/1525) and is an Arabic word, not IE (node 7). The variant forms Wesâ, Wâs, Wôs, Wôsos follow Mann's uās-/uōs- notation.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *wes- «خیس، نمناک» (پوکورنی، ۱۱۷۱–۱۱۷۲؛ واتکینز wes-2) واقعی است و پوکورنی خود واژه‌های «شیره» (انگلیسی کهن wōs > ooze)، با احتیاط واژه‌های «خون» اوستایی (vohunī-, vohuna-) و نیز به معنای «جانور نر» واژهٔ uštra- «شتر» را زیر آن آورده است. پس سرواژه و معنای «خیس و نیز جانور نر» دقیقاً برگرفته از پوکورنی است و ادعای نورایی درست است، ولی پیوند «شتر» و «خون» با این ریشه امروز تنها یکی از فرضیه‌هاست. واژهٔ «باه» عربی است و به این ریشه ربطی ندارد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/úštras\",\n        \"https://en.wiktionary.org/wiki/ooze\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1171,1172\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root / lemma: ues-3 ... Meaning: wet ... Old English wōs ' dampness, juice, sap'; engl. ooze ... presumably Avestan vaŋhu-tāt- 'blood' ... vohuna- 'blood' and Old Indic vasā ... here with the meaning 'male animal' ... Old Indic uṣṭra- 'Büffel, Kamel' ... Avestan uštra- 'Kamel' (also in Zaraθuštra)' Page(s): 1171-1172.\"},\n        {\"ref\": \"IEC:1582\", \"status\": \"not_found\", \"note\": \"Local IEC.txt (858 leaves) ends at p. ~1555 (leaf 856 'ulksuos'); p. 1582 is not in the scan. Related Mann entries found: p.1495 'uās- (uōs-?) fluid. Cf. uos-, ues- (5) ... Per. bāh, s. semen; ... OE wōs ... ooze'; p.1525 'ues- (5) soak; water ... Per. bāh sperm'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. wes-2\", \"stance\": \"supports\", \"note\": \"'wes-2. Wet. Germanic *wōs- in Old English wōs, juice: OOZE1. [Pok. 3. wes- 1171.]' (no Iranian material, no 'male animal').\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 308 (WLD_Bd1_pages leaf 317)\", \"stance\": \"supports\", \"note\": \"'Vermutlich av. vaŋhu-tāt- f. „Blut“, vohuna- m. „Blut“ und ai. vasā „Speck, Fett“ ... Hierher mit der Bed. „männliches Tier“ ... nach Johansson IF. 2, 60 ff. ai. usrá-h „Stier“, uṣṭra-h „Büffel“ ... av. uštra- m. „Kamel“' — the source of Pokorny's entry; hedged ('vermutlich', 'nach Johansson').\"},\n        {\"src\": \"IEC\", \"where\": \"pp. 1495, 1525\", \"stance\": \"partial\", \"note\": \"Mann has uās- 'fluid' and ues- (5) 'soak; water' (with Per. bāh), not a single root including camel/blood in the accessible pages.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"uš-tra, uštra; zara-uštra\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. uštra- m. 'camel' (OP uša-bāri- 'camel-borne' in Bīsotūn) continues Proto-Iranian *úštrah < PIIr. *úštras, cognate with Skt. uṣṭra- 'buffalo, camel'. Its PIE source is uncertain: Pokorny/WP (after Johansson) put it under *wes- 'wet' with a sense 'male animal, inseminator' (*us-tro-), which Wiktionary lists as one of three hypotheses beside *uǵ-tro- (from *weǵ- 'strong') and a substrate word related to *ūsros 'aurochs'. Av. Zaraθuštra- certainly contains uštra- 'camel'; the first member zarat- is disputed: 'old' (zarant-, Bartholomae; hence 'with old camels'), 'angry/furious', 'yellow', 'driving' or (Mayrhofer) 'desiring camels' — Nourai's 'with old camels' is one accepted reading, not the consensus. The word is real; the root link is a minority/hedged hypothesis.\",\n          \"derivation_fa\": \"اوستایی uštra- «شتر» از ایرانی باستان *úštrah و هندوایرانی *úštras است و با سنسکریت uṣṭra- هم‌ریشه است؛ اما ریشهٔ هندواروپایی آن روشن نیست: پوکورنی و والده آن را از *wes- «خیس» به معنای «جانور نر، بارورکننده» می‌داند، ولی ویکی‌واژه دو فرضیهٔ دیگر (از *weǵ- «نیرومند» یا وام‌واژه‌ای از زبان زیرین) هم می‌آورد. در نام زرتشت (Zaraθuštra) جزء دوم بی‌گمان «شتر» است، اما معنای جزء نخست (پیر، خشمگین، زرد، رانندهٔ شتر، خواهان شتر) مورد اختلاف است؛ «دارندهٔ شتران پیر» فقط یکی از این تفسیرهاست. پس سخن نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/úštras\",\n            \"https://en.wikipedia.org/wiki/Zoroaster\",\n            \"https://en.wiktionary.org/wiki/Zarathustra\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1172\", \"status\": \"supports\", \"note\": \"POK_full.txt ues-3 (pp. 1171-1172): 'here with the meaning male animal ...: Old Indie uṣṭra- m. Büffel, Kamel ... Avestan uštra- m. Kamel (also in Zaraθuštra)'.\"},\n            {\"ref\": \"DZA:59\", \"status\": \"not_checked\", \"note\": \"refs_online.json: kind 'purchase', no copy found.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"cols. ~400-420 (e.g. leaf 3116 line 'vom Kamelhengst: uštrahe kəhrpa')\", \"stance\": \"supports\", \"note\": \"Bartholomae uses uštra- 'Kamel' throughout ('aiwi.tačina- ... vom Kamelhengst: uštrahe ...'); confirms the Avestan word.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 308 and p. 249 (leaves 317, 258)\", \"stance\": \"partial\", \"note\": \"p.308 'Hierher mit der Bed. männliches Tier ... nach Johansson ... av. uštra- m. Kamel'; p.249 relates ai. uṣṭra- 'Büffel, Kamel', av. uštra- 'Kamel' to ai. uṣṭar- 'Pflugstier' — hedged.\"},\n            {\"src\": \"KNT\", \"where\": \"not grepped in detail\", \"stance\": \"silent\", \"note\": \"OP has only the compound uša-bāri-; not needed for the claim.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`xwštr\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian ʾxwštr /(ə)xušt(ə)r/ 'camel' (also xwštr-) continues *uštra- with secondary x- before -št- (Gharib reconstructs *uxštra-); it is the regular Sogdian reflex of the same Iranian word as Av. uštra-.\",\n          \"derivation_fa\": \"سغدی ʾxwštr (خوانش əxuštər) «شتر» بازماندهٔ همان ایرانی باستان *uštra- است که در سغدی پیش از -št- یک x افزوده گرفته است؛ قریب آن را از *uxštra- و هم‌ریشه با اوستایی uštra می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:30\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 95 (≈ p.29-30), entry 784: ''ywstr- B (ə)xušt(ə)r ('xwštr) < *uxštra, Av. uštra ... camel'.\"},\n            {\"ref\": \"SOD:439\", \"status\": \"not_checked\", \"note\": \"Second citation probably the English-index/entry 2129 'xwstr- S oxustr ... camel' (leaf 149); page 439 itself not located.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"entry 2129 (leaf 149)\", \"stance\": \"supports\", \"note\": \"'2129 xwstr- S oxustr ... 'ywstr-, xwstr- camel. Anc. Lett. 1.11'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 87, p. 20\", \"stance\": \"supports\", \"note\": \"'87. uštur Kameel, šutur. aw. uštra- Kameel; phlv. uštr...; ai. uṣṭra-' — confirms the common Iranian word (Sogdian not listed).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"oštor; Zartošt\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP oštor/ ʼuštur, šotor 'camel' < MP uštar (ideogram GMRA, ʾwštl) < OIr. *uštra- = Av. uštra-; šotor arises by loss of the initial vowel and anaptyxis (Hübschmann: 'uštur (šutur) Kameel = zd. uštra-'). Zartošt/Zardošt < MP Zardu(x)št < Av. Zaraθuštra- (θ+u > MP d/t, final -a lost); the descent is certain, but the gloss 'owner of old camels' reflects only one of several interpretations of zarat- (see node 1).\",\n          \"derivation_fa\": \"«اشتر/شتر» از فارسی میانه uštar (با هزوارش GMRA) و آن از ایرانی باستان *uštra- (اوستایی uštra-) است؛ «شتر» با افتادن واکهٔ آغازین پدید آمده است (هوبشمان، هرن، برهان قاطع). «زرتشت/زردشت» از فارسی میانه Zardu(x)št و آن از اوستایی Zaraθuštra- است؛ تبار واژه قطعی است ولی معنای «دارندهٔ شتران پیر» فقط یکی از چند تفسیر است. پس اشتر درست و معنای زرتشت با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/شتر\",\n            \"https://en.wikipedia.org/wiki/Zoroaster\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:138\", \"status\": \"supports\", \"note\": \"BQT_v1_pages leaf 354 (p.138), Mo'in's footnote continued 'از صفحهٔ ۱۳۷': '۴ اشتر - اوستا uštra، سانسکریت uṣṭra «بارتولمه» ۴۰۲ ... پهلوی uštar ...' with dialect forms; headword اشتر 'camel' on p.137 (leaf 353).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 87, p. 20 (leaf 42)\", \"stance\": \"supports\", \"note\": \"'87. uštur Kameel, šutur. aw. uštra- Kameel; phlv. uštr...; ai. uṣṭra-'.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 138 (leaf 148) and p. 213 (leaf 214)\", \"stance\": \"supports\", \"note\": \"'uštur (šutur) Kameel = zd. uštra-'; 'np. Zardušt, Zarātušt ... phl. Zaratušt = zd. Zaraθuštra-'.\"},\n            {\"src\": \"PHD\", \"where\": \"pp. 85 and 98\", \"stance\": \"supports\", \"note\": \"'uštar [GMRA ... ʾwštl | N uštur] camel'; 'Zardu(x)št [zltw(h)št' | N Zardušt] Zaraθuštra, Zoroaster'.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. uštur\", \"stance\": \"supports\", \"note\": \"'uštur [GMRʾ] camel ... — Av. (420 sq.) uštra-; NP uštur, šutur'.\"},\n            {\"src\": \"ARY\", \"where\": \"pdf p. 374 (printed 375)\", \"stance\": \"supports\", \"note\": \"Latin index: 'UŠTRA (SANSKRIT) ... UŠHTRA (AVESTAN) ... VERRES (LATIN) ... UŠHTAR (PAHLAVI)' — Aryanpur files شتر with Lat. verres 'boar', i.e. Pokorny's 'male animal' grouping.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"vanhu, vohnua, vohuni\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The real Avestan words for 'blood' are vohunī- f., vohuna- m. and vaŋhu-tāt- f. (Bartholomae cols. 1355, 1434). The book prints 'vanhu, vohnua, vohuni': 'vohnua' is Nourai's misprint for vohuna-, and 'vanhu' is a truncation of vaŋhu-tāt- (bare vaŋhu- means 'good'). They continue PIr. *wahuHnīH 'blood'; Pokorny links them 'presumably' to *wes- 'wet' (with Skt. vasā 'fat'), but Wiktionary calls the etymology uncertain (perhaps related to Latin vēna 'vein'), so the root link is only plausible.\",\n          \"derivation_fa\": \"واژه‌های اوستایی برای «خون» vohunī-، vohuna- و vaŋhu-tāt- هستند (بارتولومه، ستون ۱۴۳۴). کتاب «vanhu, vohnua, vohuni» چاپ کرده که vohnua خطای چاپی کتاب به جای vohuna است و vanhu کوتاه‌شدهٔ vaŋhu-tāt- است (vaŋhu به تنهایی یعنی «نیک»). این واژه‌ها از ایرانی باستان *wahuHnīH اند؛ پوکورنی با واژهٔ «احتمالاً» آن‌ها را به *wes- «خیس» می‌پیوندد، ولی ویکی‌واژه ریشه را نامعلوم می‌داند. پس خطای چاپی کتاب است و پیوند با ریشه با احتیاط پذیرفتنی.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"vanhu, vohnua, vohuni\",\n          \"correct_form\": \"vaŋhu-tāt-, vohuna-, vohunī-\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wahūnī\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1172\", \"status\": \"supports\", \"note\": \"POK_full.txt ues-3: 'presumably Avestan vaŋhu-tāt- 'blood', vaŋhuθwa- 'Blutvergießen, bloody fight', vohuna- m. 'blood' and Old Indic vasā ... bacon, fat, lard' — hedged ('presumably').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1434 (leaf 786) and col. ~1355 (leaf 742)\", \"stance\": \"supports\", \"note\": \"'vohuna- m. Blut'; 'vohunī- f. Blut ... Vgl. mp. (Pü.) xōn, np. xūn ... die ich auf ir. *xvahun- zurückführe'; 'vaŋhutāt- f. Blut'. No vohnua/bare vaŋhu 'blood'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 308 (leaf 317)\", \"stance\": \"partial\", \"note\": \"'Vermutlich av. vaŋhu-tāt- f. „Blut“, vaŋhuθwa- n. „Blutvergießen“, vohuna- m. „Blut“ und ai. vasā' — hedged.\"},\n            {\"src\": \"SYN\", \"where\": \"4.15 BLOOD, p. 206\", \"stance\": \"partial\", \"note\": \"'Av. vohuni- (NPers. xūn 'blood'), etym.? Barth. 1434.' — Buck regards the etymology as unknown.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sogdian\",\n          \"words\": \"xwrn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian xwrn /xurn/ 'blood' (also γwrn, wγrn, γwn in Gharib) continues PIr. *wahuHnī- (Av. vohunī-) with metathesis/contraction of *wahun- > *wγun- > xu(r)n; Gharib explicitly derives it '< Av. vohuni'. Wiktionary lists Sogdian γwrn/wγrn among the descendants.\",\n          \"derivation_fa\": \"سغدی xwrn (خوانش xurn) «خون» با گونه‌های γwrn و wγrn بازماندهٔ ایرانی باستان *wahuHnī- (اوستایی vohunī-) است؛ قریب آن را صریحاً از اوستایی vohuni می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wahūnī\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:437\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 504 (≈ p.438), entry 10758: 'xwrn- M, C xurn < Av. vohuni ... ywxn-, γxwn-, γwrn-, γywn(w), wγrn-(h) ... blood'.\"},\n            {\"ref\": \"SOD:176\", \"status\": \"not_checked\", \"note\": \"Probably the cross-reference form γwrn-/ʾγwn; page not located.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"entries 10760-10762 (leaf 504)\", \"stance\": \"supports\", \"note\": \"'xurn-patxure ... blood-stained'; 'xurn(e)-as bloodletting → xwrn-' — compounds confirm xwrn 'blood'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 511, p. 113\", \"stance\": \"supports\", \"note\": \"Horn lists the Iranian cognates of xūn (aw. vohunī-, phlv. xūn, afγ. wīne ...) — the same etymon, Sogdian not cited.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"xŭn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP xūn 'blood' < MP xōn (ideogram DMYA, khwn) < PIr. *wahuHnī- (Av. vohunī-); the initial *wah- > *xvah- > xw- > x- and the contraction -ahu- > -ō- > NP -ū- (majhūl ō > ū). Cognates: Kurd. xwîn, Bal. hōn, Pashto wīna. The direct Avestan-to-Persian descent is standard (Horn, Bartholomae, MacKenzie); only the deeper PIE link is uncertain (node 4).\",\n          \"derivation_fa\": \"«خون» از فارسی میانهٔ xōn (با هزوارش DMYA) و آن از ایرانی باستان *wahuHnī- (اوستایی vohunī-) است؛ wah- آغازین به xw و سپس x بدل شده و -ahu- به ō (واو مجهول) و در فارسی نو به ū رسیده است. هم‌ریشه با کردی xwîn، بلوچی hōn و پشتو wīna. ادعای نورایی درست است؛ تنها پیوند دورتر با ریشهٔ هندواروپایی نامطمئن است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/خون\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wahūnī\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BRT:1434\", \"status\": \"supports\", \"note\": \"BRT.txt leaf 786 (cols. 1433-1434): 'vohunī- f. Blut ... Vgl. mp. (Pü.) xōn, np. xūn ... auf ir. *xvahun- zurückführe'.\"},\n            {\"ref\": \"HRN:113\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 134 (p.113): '511. xūn Blut ... aw. vohuni- Blut; phlv. xūn ... kurd. xūn; afγ. wīne; bel. hūn'.\"},\n            {\"ref\": \"SYN:206\", \"status\": \"partial\", \"note\": \"SYN.txt §4.15: 'Av. vohuni- (NPers. xūn 'blood'), etym.? Barth. 1434.' — confirms the Av.-NP link, leaves the etymology open.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 94\", \"stance\": \"supports\", \"note\": \"'xōn [DMYA < A dm'; hwn' | M xwn, N xūn] blood'.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. xūn\", \"stance\": \"supports\", \"note\": \"'xūn [hwn'] blood'; 'xūn-rēčišnīh bloodshed'.\"},\n            {\"src\": \"ARY\", \"where\": \"pdf p. 255 (printed 256)\", \"stance\": \"supports\", \"note\": \"Latin index under خون: 'VOHUNI-, VOHUNA (AVESTAN) ... XON, XUN (PAHLAVI) ... OOZE (ENGLISH) ... VASA (SANSKRIT) ... WOS (OLD ENGLISH)' — Aryanpur follows Pokorny's grouping.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"bâh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Persian bāh 'sexual potency, libido' is a loan from Arabic al-bāh 'coitus; venereal capacity' (Arabic root b-w-h / bāʾa, cf. al-bāʾa 'marriage, coitus' in the hadith), as Mo'in marks it '[ع.]'. The only support for an IE origin is Mann (IEC 1495, 1525), who lists 'Per. bāh semen' under uās-/ues- 'fluid, soak'; that entry is isolated, has no Old/Middle Iranian intermediate, and an IE *w- would give Persian g-/b- only via *wy- or *w- > b- in limited contexts. Modern sources (Wiktionary, Mo'in) treat it as Arabic; Nourai's own note records Mo'in's view, which is the correct one.\",\n          \"derivation_fa\": \"«باه» به معنای «نیروی جنسی، شهوت» وام‌واژه‌ای از عربی «الباه» (جماع، توان جنسی) است و معین نیز آن را با نشانهٔ [ع.] عربی دانسته است. تنها مان (ص ۱۴۹۵ و ۱۵۲۵) آن را به ریشهٔ هندواروپایی *wes-/*wās- «مایع» پیوند داده که هیچ صورت اوستایی یا پهلوی میانجی ندارد. پس پژوهش امروزی پیوند آن با این ریشه را رد می‌کند و یادداشت خود نورایی (عربی بودن به گفتهٔ معین) درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/باه\",\n            \"https://vajehyab.com/?q=باه&d=moein\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1495\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 822: 'uās- (uōs-?) fluid. Cf. uos-, ues- (5) and WP I, 308 Per. bāh, s. semen; Hitt. wasi ...; OE wōs ... ooze'.\"},\n            {\"ref\": \"IEC:1525\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 840: 'ues- (5) soak; water ... Per. bāh sperm'.\"},\n            {\"ref\": \"IEC:1582\", \"status\": \"not_found\", \"note\": \"Page beyond the end of the local scan (ends ~p.1555).\"},\n            {\"ref\": \"MON:470\", \"status\": \"contradicts\", \"note\": \"6-vol page not mappable online; Mo'in's entry via vajehyab: 'باه [ ع . ] غریزهٔ جنسی، نیروی شهوت' — Arabic, as Nourai's note says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 1171-1172\", \"stance\": \"silent\", \"note\": \"Pokorny's ues-3 has no Persian bāh.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 32 (leaf 42)\", \"stance\": \"silent\", \"note\": \"Only 'np. bah-ā, phl. vah-āk' (price) under skr. vasna-; no bāh 'libido'.\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab Mo'in\", \"stance\": \"contradicts\", \"note\": \"'[ع.]' Arabic.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"uštra; vasâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Skt. uṣṭra- m. 'buffalo; camel' (Vedic 'buffalo', later 'camel'; the book's uštra is a Persianising transliteration of uṣṭra) < PIIr. *úštras, cognate with Av. uštra-; its PIE origin is uncertain (see node 1). Skt. vasā f. 'fat, marrow, lard, (fluid) grease' is cited by Pokorny/WP 'presumably' under *wes- 'wet'; the chart's gloss 'liquid' is loose (Pokorny: 'Speck, Fett, Schmalz', also vasā 'flüssiges Fett').\",\n          \"derivation_fa\": \"سنسکریت uṣṭra- «گاومیش؛ شتر» از هندوایرانی *úštras و هم‌ریشه با اوستایی uštra- است، ولی ریشهٔ هندواروپایی آن نامطمئن است. سنسکریت vasā به معنای «چربی، پیه، مغز استخوان» است نه «مایع»؛ پوکورنی آن را با احتیاط زیر *wes- «خیس» آورده است. پس ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/उष्ट्र\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/úštras\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1172\", \"status\": \"supports\", \"note\": \"POK_full.txt ues-3: 'Old Indie vasā, vasā 'bacon, fat, lard' (also vaśā inscribed, as vaśā-m 'flüssiges fat') ... Old Indie uṣṭra- m. 'Büffel, Kamel''.\"},\n            {\"ref\": \"IEC:1582\", \"status\": \"not_found\", \"note\": \"Page beyond the end of the local scan.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 308 (leaf 317)\", \"stance\": \"partial\", \"note\": \"'ai. vasā, vasā „Speck, Fett, Schmalz“ ... ai. uṣṭra-h „Büffel“' — hedged ('vermutlich', 'nach Johansson').\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 wes-2\", \"stance\": \"silent\", \"note\": \"Only OE wōs > ooze listed.\"},\n            {\"src\": \"IEC\", \"where\": \"p. 1525\", \"stance\": \"silent\", \"note\": \"ues- (5) lists Skt. vasin 'otter', not vasā or uṣṭra.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Germanic\",\n          \"words\": \"wôs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *wōsą 'sap, juice' (o-grade *wōs- of PIE *wes- 'wet') > Old English wōs 'juice, sap, moisture', Middle Low German wōs 'scum, juice', Old Danish/Norwegian os 'plant juice'. Pokorny, Watkins and Wiktionary agree.\",\n          \"derivation_fa\": \"ژرمنی آغازین *wōsą «شیره، آب‌میوه» (درجهٔ o از ریشهٔ *wes- «خیس») در انگلیسی کهن wōs «شیره، رطوبت» و آلمانی پست میانه wōs دیده می‌شود. پوکورنی، واتکینز و ویکی‌واژه همه این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ooze\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt: 'wes-2. Wet. Germanic *wōs- in Old English wōs, juice: OOZE1. [Pok. 3. wes- 1171.]'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1171\", \"stance\": \"supports\", \"note\": \"'Old English wōs n. dampness, juice, sap ... Middle Low German wōs scum, froth ... juice, sap. Old Danish Norwegian os plant juice'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. ooze (n.)\", \"stance\": \"supports\", \"note\": \"'ME. wose, wos, fr. OE. wōs, sap, juice'.\"},\n            {\"src\": \"IEC\", \"where\": \"p. 1495\", \"stance\": \"supports\", \"note\": \"'uās- fluid ... OE wōs, n. juice, liquor, sap'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"ooze 1\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English ooze (n.) 'sap, exudation' < ME wose < OE wōs 'juice, sap'; the verb (ME wosen, c.1300 'to exude moisture') is derived from it, the w- being lost before the back rounded vowel (cf. who). Its homonym ooze 'soft mud' is from OE wāse 'mud, mire' (PIE *weys-), which influenced the meaning; Nourai's 'ooze 1' correctly takes the wōs one.\",\n          \"derivation_fa\": \"انگلیسی ooze «تراویدن، نشت کردن» از انگلیسی میانه wose و آن از انگلیسی کهن wōs «شیره» است و w آغازین پیش از واکهٔ پسین گرد افتاده است. واژهٔ هم‌آوای ooze «لجن» از wāse انگلیسی کهن و ریشهٔ دیگری است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ooze\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1172\", \"status\": \"supports\", \"note\": \"POK_full.txt ues-3: 'Old English wōs n. dampness, juice, sap; engl. ooze dampness, slime, mud, as verb durchsickern, spring up, bubble'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. ooze (n., v.)\", \"stance\": \"supports\", \"note\": \"'ooze, n. ... ME. wose, wos, fr. OE. wōs, sap, juice, rel. to, and influenced by, OE. wāse, soft mud'; 'Derivative: ooze, intr. v., to flow slowly'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 wes-2\", \"stance\": \"supports\", \"note\": \"'Old English wōs, juice: OOZE1'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. OOZE\", \"stance\": \"silent\", \"note\": \"grep '^OOZE' in SKT.txt found no headword line (OCR).\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-17T00:07:03.131Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-550.json (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:07:14.550Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 - <<'E'\np='page-550.json'; s=open(p,encoding='utf-8').read()\nreps=[('\"where\": \"no. 87, p. 20 (leaf 42)\"','\"where\": \"no. 87, p. 21 (leaf 42)\"'),\n('\"where\": \"no. 87, p. 20\"','\"where\": \"no. 87, p. 21 (leaf 42)\"'),\n('p. 138 (leaf 148) and p. 213 (leaf 214)','p. 138 (leaf 148) and p. 204 (leaf 214)'),\n('\"where\": \"pp. 85 and 98\"','\"where\": \"PHD.txt leaves 111 and 124\"'),\n('\"where\": \"p. 94\", \"stance\": \"supports\", \"note\": \"\\'xōn','\"where\": \"PHD.txt leaf 121 (x- section)\", \"stance\": \"supports\", \"note\": \"\\'xōn'),\n('col. 1434 (leaf 786) and col. ~1355 (leaf 742)','col. 1434 (leaf 786) and BRT.txt leaf 742'),\n('(Bartholomae cols. 1355, 1434)','(Bartholomae col. 1434 and the vaŋhutāt- entry, BRT.txt leaf 742)'),\n('\"where\": \"cols. ~400-420 (e.g. leaf 3116 line \\'vom Kamelhengst: uštrahe kəhrpa\\')\"','\"where\": \"BRT.txt lines 3116, 3817 (entries ayryō.naēmasəma-, aiwi.tačina-)\"'),\n(\" that entry is isolated, has no Old/Middle Iranian intermediate, and an IE *w- would give Persian g-/b- only via *wy- or *w- > b- in limited contexts.\",\" that entry is isolated and offers no Old or Middle Iranian intermediate form (no Avestan or Pahlavi *wāh-/*bāh 'semen' is attested), while the word is at home in Arabic with a native root.\"),\n]\nfor a,b in reps:\n    assert a in s,a; s=s.replace(a,b)\nopen(p,'w',encoding='utf-8').write(s)\nE\npython3 -m json.tool page-550.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 550"
}
```


### [2026-10-17T00:07:15.436Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'plausible': 3, 'confirmed': 5, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'not_checked': 3, 'partial': 1, 'not_found': 2, 'contradicts': 1}
books consulted: {'supports': 19, 'partial': 4, 'silent': 6, 'contradicts': 1} | by book: {'WLD': 3, 'HRN': 3, 'BRT': 2, 'SOD': 2, 'HUB': 2, 'PHD': 2, 'NYB': 2, 'ARY': 2, 'POK': 2, 'AHD': 2, 'IEC': 2, 'KLN': 2, 'KNT': 1, 'SYN': 1, 'MON': 1, 'SKT': 1}
```


## [2026-10-17T00:07:24.999Z] TOOL CALL #49: SubagentHandback

```json
{
 "message": "I wrote /home/sfmqrb/git/rishe-private/data/verification/page-550.json for page 550 (book page 520). It is valid JSON and `verify_check.py 550` shows 0 PROBLEM lines.\n\nPage 550 covers 1 entry. Wes 2 only points to Aus 2, so it is skipped.\n\n- **Root \"Wes 1\":** confirmed. Pokorny pp. 1171–1172 (3. u̯es- \"wet\") has all the material on the chart, including the \"male animal\" sense for uṣṭra/uštra and Avestan vohuna \"blood\". Those two attachments are Pokorny's own cautious guesses (\"presumably\", taken from Johansson), not settled scholarship.\n- **Nodes (10):** 5 confirmed, 3 plausible, 1 disputed, 1 transcription_suspect.\n  - Confirmed: Sogdian ʾxwštr, Sogdian xwrn, Persian xūn, Germanic wōs, English ooze.\n  - Plausible: Avestan uštra and Zaraθuštra (#1), Persian oštor and Zartošt (#3), Sanskrit uṣṭra and vasā (#8). The Proto-Indo-Iranian *úštras link to *wes- is one of three hypotheses on Wiktionary. \"With old camels\" is only one reading of zarat-; others are angry, yellow, driving or desiring. Sanskrit vasā means \"fat, marrow\", not \"liquid\".\n- **Disputed:** Wes 1 / bâh «باه» (#7). It is an Arabic loan (al-bāh, \"coitus, libido\"), which Mo'in marks [ع.] and Wiktionary also treats as Arabic. Only Mann (IEC 1495, 1525: \"Per. bāh semen\") puts it under the IE root. Nourai's own note (that Mo'in derives it from Arabic) is the correct view.\n- **Transcription_suspect:** Wes 1 / Avestan \"vanhu, vohnua, vohuni\" (#4). The real forms are vaŋhu-tāt-, vohuna- and vohunī- (Bartholomae col. 1434). \"vohnua\" is a misprint for vohuna, and \"vanhu\" is a cut-down vaŋhu-tāt- (bare vaŋhu- means \"good\"). The error is in the book: the printed page shows exactly these forms. The page image is saved at data/verification/sources/refs/ocr/BOOK/550.png.\n- **Extraction errors to fix:** none. The JSON matches the printed page.\n- **References I could not check:**\n  - IEC:1582 is past the end of the local scan, which stops around p. 1555.\n  - DZA has no copy.\n  - SOD:439 and SOD:176 were not located; SOD:30 and SOD:437 do support the chart.\n  - MON:470 cannot be mapped to a page, so I used Mo'in's entry on vajehyab instead (it says Arabic)."
}
```


### [2026-10-17T00:07:25.565Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
