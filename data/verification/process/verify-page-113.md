# Verification process log — verify-page-113


## [2026-09-05T17:38:42.448Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 113 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-113.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-113.json. Write /home/sfmqrb/git/rishe/data/verification/page-113.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 113` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T17:38:44.223Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T17:38:44.934Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T17:38:44.949Z] TOOL RESULT

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


## [2026-09-05T17:38:45.065Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-113.txt"
}
```


### [2026-09-05T17:38:45.087Z] TOOL RESULT

```
1	=== PDF page 113 (book page 83) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dek : take, accept, understand  (refs POK:189)
4	#1 (parent #0) [Avestan] refs=POK:189; WLD1:784; SYN:1227 | daxš 1 : make things understandable, teach ; fra-daxš-tar : teacher ☞Per 1,Ter 3 ; daxšta : knowledge, tool
5	  #2 (parent #1) [Persian] refs=POK:189; BRT:667; BQT:827 | daxš 1 «دخش ۱» : trade, occupation
6	#3 (parent #0) [Latin] refs=AHD | docěre : to make things clear, teach (doctor, document) ; decěre : to be acceptable (decent) ; discere : to learn (disciple, discipline) ; decus : grace (decorate) ; dignus : worth taking (dignity)
7	  #4 (parent #3) [French] refs=None | 
8	    #5 (parent #4) [Persian] refs=MON | doktor «دکتر» : doctor ; dekor «دکور» : decoration
9	  #6 (parent #3) [English] refs=None | doctor, document, decent, disciple, discipline, decorate, dignity
10	#7 (parent #0) [Greek] refs=AHD | dokein : make things clear, think
11	  #8 (parent #7) [French] refs=MON:193 | orthodoxe
12	    #9 (parent #8) [Persian] refs=MON:193 | ortodox «ارتودوکس» : with correct thoughts
13	  #10 (parent #7) [English] refs=AHD | heterodox, orthodox, paradox
14	--- entry 1 ---
15	ROOT [Indo-European] Deks : right, on the right side  (refs POK:190; AHD:1511)
16	#1 (parent #0) [Avestan] refs=POK:190 | dašina : right
17	  #2 (parent #1) [Pahlavi] refs=SNS:316 | dašn : right
18	    #3 (parent #2) [Persian] refs=SNS:316; BQT:866 | dašn «دَشن» : right side, also the first (daily) sales ; dašt «دشت ۱» : the first sales of a business in a day
19	#4 (parent #0) [Latin] refs=POK:190; AHD | dexter : on the right
20	  #5 (parent #4) [English] refs=AHD | dexter, dextro-
21	
```


## [2026-09-05T17:38:48.036Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-113.json",
 "description": "Read source JSON page 113"
}
```


### [2026-09-05T17:38:48.069Z] TOOL RESULT

```
{
  "pdf_page": 113,
  "book_page": 83,
  "entries": [
    {
      "root": {
        "name": "Dek",
        "lang": "Indo-European",
        "refs": "POK:189",
        "gloss": "take, accept, understand"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:189; WLD1:784; SYN:1227",
          "words": [
            {"translit": "daxš 1", "gloss": "make things understandable, teach", "script": null},
            {"translit": "fra-daxš-tar", "gloss": "teacher", "script": null, "see": ["Per 1", "Ter 3"]},
            {"translit": "daxšta", "gloss": "knowledge, tool", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:189; BRT:667; BQT:827",
          "words": [
            {"translit": "daxš 1", "gloss": "trade, occupation", "script": "دخش ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "docěre", "gloss": "to make things clear, teach (doctor, document)", "script": null},
            {"translit": "decěre", "gloss": "to be acceptable (decent)", "script": null},
            {"translit": "discere", "gloss": "to learn (disciple, discipline)", "script": null},
            {"translit": "decus", "gloss": "grace (decorate)", "script": null},
            {"translit": "dignus", "gloss": "worth taking (dignity)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "doktor", "gloss": "doctor", "script": "دکتر"},
            {"translit": "dekor", "gloss": "decoration", "script": "دکور"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "doctor, document, decent, disciple, discipline, decorate, dignity", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "dokein", "gloss": "make things clear, think", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": "MON:193",
          "words": [
            {"translit": "orthodoxe", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:193",
          "words": [
            {"translit": "ortodox", "gloss": "with correct thoughts", "script": "ارتودوکس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "heterodox, orthodox, paradox", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Deks",
        "lang": "Indo-European",
        "refs": "POK:190; AHD:1511",
        "gloss": "right, on the right side"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:190",
          "words": [
            {"translit": "dašina", "gloss": "right", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:316",
          "words": [
            {"translit": "dašn", "gloss": "right", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SNS:316; BQT:866",
          "words": [
            {"translit": "dašn", "gloss": "right side, also the first (daily) sales", "script": "دَشن"},
            {"translit": "dašt", "gloss": "the first sales of a business in a day", "script": "دشت ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:190; AHD",
          "words": [
            {"translit": "dexter", "gloss": "on the right", "script": null}
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
            {"translit": "dexter, dextro-", "gloss": null, "script": null}
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


## [2026-09-05T17:38:48.405Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T17:38:48.437Z] TOOL RESULT

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


## [2026-09-05T17:38:57.890Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','SYN','BRT','BQT','MON','SNS','LEW','LAT','KLN','SKT','IEC','PHD','NYB','HRN','HUB','ARY','CHEUNG','FSD','WEB']:\n    v=d.get(k)\n    if v: print(k, json.dumps(v,ensure_ascii=False)[:600]); print()\n\""
}
```


## [2026-09-05T17:38:58.439Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && ls tools/"
}
```


### [2026-09-05T17:38:59.561Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
```


### [2026-09-05T17:38:59.594Z] TOOL RESULT

```
agent
page-100.json
page-101.json
page-102.json
page-103.json
page-104.json
page-105.json
page-106.json
page-107.json
page-108.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
---
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
```


## [2026-09-05T17:39:04.240Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py"
}
```


### [2026-09-05T17:39:04.281Z] TOOL RESULT

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


## [2026-09-05T17:39:04.454Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==197||NR==198||NR==199' POK_01.txt | head -200"
}
```


### [2026-09-05T17:39:06.118Z] TOOL RESULT

```
iff  ,Gott,  Göttliches^  ausge.1 gangen,  sondern  (wie  d-av^ia  von  d^edo/uai)  stellen^  sich  zu  klr.  dyvl'ii] dyvyty  sja  , schauen^,  cech.  divam  se  ,schaue,  betrachte^,  das  sich  zu  ai.i di-de-ti  ,leuchtet'  in  der  Bed.  verhält  wie  z.  B.  mhd.  blick  , Glanz,  Blitz*"* und  ,Blick  der  Augen^,  nhd.  glänzen :  slav.  gl^dati  ,schauen^
erz-St.  *deien'  (thematisch  deino-,  dino-)  nur  in  der  Bed.  ,Tag^: ursprüngl.  kons,  noch  in  aksl.  dhnh,  Gen.  dhne  ,Tag';  ai.  dina-m  (bes. in  Kompos.  ;Tag',  lat.  nundinae  ,der  an  jedem  neunten  Tag  gehaltene^ Markt',  air.  denus  ,spatium  temporis',  tredenus  ,triduum';  alb.  gdJiinj , mache  Tag'  aus  *-di-n-iö]  hochstufig  lit.  dienäj  lett.  diena,  apr.  Akk.  f.  deinan ,Tag',  (Mühlenbach-Endzelin  I  432 f.,  Büga  Kalba  ir.  S.  227 f.);  got.  sinteins^ ,täglich,  immerwährend';  vielleicht  hierher  ahd.  len(gi)zin  ,Lenz'  aus' *langat-tin  als  ,lange  Tage  habend'.
Kretschmer  führt  gr.  Ttv-dagiöat  , Zeussöhne',  etr.  Tin,  Tinia  ,Juppiter' auf  ein  vorgr.  Tin-  ,Diespiter',  bzw.  ital.  *Dinus  (idg.  *din-  ,Tag,  Himmel') zurück  (Gl.  13,  111;  14,  303 ff.,  19,  207;  s.  auch  Schwyzer  Gr.  Gr.  I  65); aber  die  ältere  Form  ist  Tvvöaoidai!
r-Er Weiterung  dei-ro-,  di-ro-  in:
germ.  *tera-  (*dei-ro-)  und  *tlra-  (*diro-)  in  ahd.  ze7'z,  ziari  ,kostbar, herrlich,  schön',  ziari  ,Schönheit,  Zier',  ziarön  ,zieren',  mnd.  ter  , Glanz, Ruhm,  Gedeihen,  gute  Beschaffenheit',  tei^e  und  tlre  ,Beschaffenheit,  Art und  Weise',  ags.  as.  tir  ,Ehre,  Ruhm',  anord.  tlrr  ds.;  norw.  dial.  ür , Ausguck,  Spähen,  Leuchten,  Glanz',  tlra  ,gucken,  funkeln';
dazu  lit.  dyretij  dyrofi  ,gaffen,  lauern',  dairytis,  lett.  dairities  , umher- gaffen', apr.  endyritioei  (u.  dgl.,  siehe  Büga  Kalba  ir.  s.  227  f.,  Mühlenbach- Endzelin  I  432  f.)  , ansehen'  (aber  bulg.  diH  , suche'  bleibt  fern,  s.  Ber- neker  201);
toch.  A  tiri  ,Art  und  Weise'.
Über  hitt.  siwat-  ,Tag',  Hivanni-  ,Gott'  (aus  *dieu-?),  hierogl.-hitt.  tina- ,Gott',  §ijäri  ,erscheint'  (*diä-?)  s.  Pedersen  Hitt.  57,  175  f.
Zu  ai.  divyati  ,spielt,  würfelt'  (angeblich  ,wirft  das  Auge')  vgl.  mit anderen  Ablautstufen  dyütdm  , Würfelspiel',  ferner  devanam  ,das  Spiel, Würfelspiel',  und  oben  dyötate  ,leuchtet',  dyutih  , Glanz',  dyumdnt-  ,hell, licht'.  Ob  hierher  auch  av.  ä-dlvyeinti  ,bemühen  sich  worum'  als  ,es  worauf abgesehen  "haben'?  Vgl.  Wackernagel,  Berl.  Sbb.  1918,  396 f.
;.<^fc
-4
187
niß  unsere  Wz.  als  ^vibrierendes  Liclit^  mit  deid-  ,eilen^  wirbeln'  ursprgl.
eins  g-ev^-esen  sei,  scheint  denkbar
^VP.  I   772  f.,  WH.  I   345 f.,   347,   349  f.,   355,   357  f.,    727,    732,    860, Sclnvyzer  Gr.  Gr.  I 
 576  f.
deiO'  (diS't  ^l^'f  ^^')  >sich  schwingen,  herum  wirbeln  (halt,  und  z.  T. o-riech.);  eilen,  nacheilen,  strebend
Ai.  diyati  , fliegt,  schwebt-;  gr.  dZvog  m.  ,Wirbel,  Strudel;  rundes  Ge- fäß runde  Tenne',  dhf]  (Hom.),  äol.  dlvra  (vgl.  Jivvof.i€vrjgj  Hoffmann  Gr. P.  II  484)  ,Wirbel,  Strudel',  divio),  ölrsvo),  äol.  dlvvrjfiL  , drehe  im  Wirbel oder  Kreise,  schwinge';  intr.  ,drehe  mich  beim  Tanz  im  Kreise'; pass.  , treibe  mich  herum,  taumle  umher,  rolle  (die  Augen),  wirble  (vom Fluß),  drehe  mich  tanzend  umher',  divw  äol.  öivvu)  , dresche',;  liom. <J/w  ,fliehe',  d'iouai  ,jage  weg'  (mit  auffälliger  Verteilung  der  intr. und  tr.  Bed.  auf  Aktiv  und  Medium),  hom.  öiswai  ,sie  eilen',  öieod^ai ,fliehen',  evöisoav  ,sie  hetzten',  disgög,  (Ttovg)  ,flüchtig'  (nach  hre,  i'srai  :  uvrai zum  thematischen  d/firat  analogisch  disvxai  statt  *SlovTaL  neugebildet?),  dicü-acü , verfolge'  (kontaminiert  aus  ficj-KO)  und  öieaai,  Meillet  MSL.  23,  50  f., Schwyzer  Gr.  Gr.  I  702);  hom.  di'Cr^t.iai  (Fut.  bom.  öi^rjaofiai)  , strebe  wo- nach, bemühe  micli  worum,  suche',  nachhom.  auch  ,forsche'  (*di,-diä-(.iai), woneben  auf  Grund  von  '*öiG-to-  att,  t^rjTeo)  , strebe  wonach,  lasse  mir angelegen  sein';  ob  hierher  mit  ursprgl.  *did- :  l&It]  ,Sturm,  heftige  Be- wegung, namentlich  des  Meeres',  t,&Xog  , Strudel,  heftige  Bewegung  des Wassers'?
Vgl.  über  die  ^  enthaltenden   gr.  Worte  Schwyzer  Gr.  Gr.  I  330^  833.
Air.  dlan  , schnell',  dene  ,Schnelligkeit' ;  lett.  deju,  diet  ,tanzen',  diedelet , müßig  gehen'.  Über  lit.  dainä  , Volkslied'  (zu  dejä  ,Wehklage?')  vgl. Mühlenbach-Endzelin  I  432  mit  Lit.
Ganz  fraglich  cymr.  dig  ,böse',  russ.  dikij  ,wild',  lit.  dykas  , übermütig, mutwillig,  unbeschäftigt,  müßig',  lett.  dtks  ,frei  von  Arbeit',  aksl.  divhjh ,wild'  (Berneker  203  f.,  Mühlenbach-Endzelin  I  478,  Trautmann  54).
Nicht  hierher  gr.  döva^  ,Rohr'  (Jüngeres  ion.  öovva^  und  vereinzeltes dor.  dajva^  metr.  Dehnung?  Schulze  Qu.  ep.  205,  Boisacq  196),  dovscj , schüttle',  äXidovog  ,im  Meer  herumgetrieben'  und  lett.  duonis,  duoni , Schilf,  Binsen'.
WP.  I  774  ff.
deigh-  , prickeln,  kitzeln'?  , zwickendes  Insekt'. Arm.  tiz  , Zecke';
mir.  dega,  Akk.  degaid  (*digät-)  ,Hirscbkäfer'; germ.  *tlkan-^    mit    Intensivschärfung    *tikkan-y    in    ags.    ticia   m.    (lies
'''  4  i
tiica  oder  ticca),  engl,  tike  und  tick  , Holzbock,  Schaflaus^,  mnd.  Zec^^  ] m.  f.  , Holzbock',  nhd.  Zecke]  daneben  eine  Vermittlungsform  ^tikan-yi^  ! mnd.  teke^  mhd.  Zeche,  engl,  teke  ds. ;  ;:2^
norw.  dial.  tikka,  ndd.  tickeri  gleicht  anstoßen',  mhd.  zlcken  ds.;  ahi zecÄön  ,pulsäre,  necken,  plänkeln';  engl,  tickle  ,kitzeln';  nasaliert  ags^ tinclian  ds.
Ein  Zusammenhang  mit  dheig-  ,stechen'  ist  nicht  nachweisbar.
WP.  I  777.
deik-  ,zeigen',  woraus  lat.  und  germ.  z.  T.  ,mit  Worten  auf  etwas
  hinweise] sagen',  mehrfach  auch  ,das  Recht  weisen,  auf  den  Täter  hinweisej beschuldigen'  entwickelt;  Partiz.  Pass.  dik-tö-s;  dikä  ,Richtunj dik'ti-  ,  An  Weisung',  deiko-s  ,Richtung'.
Ai.  didestij   disdti,   deiayati  , zeigt,   weist',   av.  daes-  Aor.  döU-  ;Zeig^ {daesayeiti,    disyeiti,    daedöiU)    ,zeigen ;    jemandem    etwas    zuweisen, sprechen',  Partiz.  ai.  distd-  (=  lat.  dictus) ;  dlsti-h  ,Weisung,  Vorschrift av.   ädiHi-§  , Anweisung,   Lehre'   (=  lat.  dicti-ö,  ags.  tiht  , Anklage',  ahc in-,  bi'Ziht  ds.,  nhd.  Verzicht),  ai.  dis-  f.  , Weisung,  Richtung',  diSä  .Richtum (=r  SUt]  ,Recht',  woraus  wohl  lat.  dicis  causa  ,nur  der  Form  wegen,  zuiä Schein'),  desd-h  ,(Richtung),  Gegend'  =  an.  teigr  s.  unten;
gr.  dsUvv[.iL,  sekundär  öeL-Kvvo)  ,zeige',  kret.  TtQO-öUvVTi  ,irtLÖsUwai^ öeT^ig  ,das  Zur-Schau-Stellen'  (mit  sekundärer  Hochstufe),  dUrj  s.  obei^ öUaLog,  ÖLTLccl^u),  SSrAog',  das  Perf.  Med.  öiösiyfxai,  und  dety^a  ,Beweis,  Bei^ spiel'  nicht  mit  idg.  g,  sondern   gr.  Neuerung;
lat.  dlcere  ,sagen',  dlcäre  ,feierlich  verkünden,  zusprechen,  weihen',  oskJ deikum  ,dicere',  umbr.  teitu,  deitu  ,dicito',  ablautend  osk.  dicust  ,dixerit'^ umbr.  dersicust  ds.,  osk.  da-dikatted  ,dedlcavit' ,  lat.  diciö  ,die  Macht  eines Herrn  über  andere,  Botmäßigkeit,  Gerichtsbarkeit',  indicäre  ,anzeigen', index  ,Anzeiger,  Angeber;  Zeigefinger'  (wie  auch  ai.  deHnl  ,Zeigefinger^), iudex  ,der  das  Recht  Weisende',  vindex  (yindicäre  =  vim  dicere),  causidicus] über  urir.  *Ekuo-decas,  Lugudec(c)as  (Gen.  Sg.)  s.  unter  1.  dek-.
got.  gateihan  ,anzeigen,  verkündigen',  anord.  tea,  jünger  tia  ,zeigen, darstellen,  ankündigen',  ags.  teon  ,anzeigen,  verkündigen',  ahd.  zlhan  ,an- schuldigen,  zeihen^,  wozu  anord.  tigenn  ,(*monstratus)  vornehm',  t'ign  f. ,Rang;  vornehmer  Mann';  ahd.  zeigön  ,zeigen',  wovon  zeiga  ,Weisung'; inziht  usw.  s.  oben;  ferner  anord.  teigr  m.  ,geradliniges  Wiesenstück' (,*Richtung'  =  ai.  desd-h  ,Gegend,  Platz,  Land'),  ablautend  ags.  tig,  tili , Anger,  Weide',  mnd.  tl{g)  m.  öffentlicher  Sammelplatz  eines  Dorfes', ahd.  zieh  , forum'.
,    Hierher  vermutlich  mit  der  Bed.  ,Finger'  (=  ,*Zeiger')  und  sekundär, aber  bereits  alt  ,Zehe',  ahd.  zeha,  ags.  tahe,  tä,  anord.  tä  ,Zehe'  {*döikuä),
189
nind.  teice,  nhd.  und  südd.  zewe  ds.  {*doik-ua),  und  das  wohl  aus  *dicitus Hurcli  Dissimilation  gegen  das  tonlose   t   entstandene   lat.  digitus  _,Finger,
Zebe^
flitt.  tek-kus-sa-nu-mi  ^maclie  erkennbar^  zeige^  hierher  nach  Sturtevant Lang.  6;  ^'^  ^^  227 ff.;  bezweifelt  der  Bildung  wegen  von  E.  Forrer  bei Feis°t  204.
Daneben  idg.  doig-  in  got.  taikns  f.  ^Zeichen,  Wunder^;  taikn  n.  ds., abd.  (usw.)  zeihhan  n.  _, Zeichen^,  ags.  txcan,  engl.  <eacÄ  ^lehren^^  anord. teikna  ^zeigen^  bedeuten^  bezeichnen'^,  ahd.  zeihh
```


## [2026-09-05T17:39:11.492Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dek-\\|deḱ\\|dek̂\\|1\\. dek\" POK_full.txt | head -40"
}
```


### [2026-09-05T17:39:11.536Z] TOOL RESULT

```
17250:{*dek-) djath-te 'nght' evolved from the common alb. -k- > -//7-like in alb. {mag-) math'b\g' 
17326:*dek-nor, PN Decius= Oscan Dekis, Gen. Dekkieis), Oscan deketasiuf, Nom. PI. 
18041:perhaps originally different from the root *dek- "tear', although *clenR- perhaps as 
19234:dek-; whereas is Old Indie abhi-dasati^ is hostile, attacked ' rather Denomin. of dasa-h 
63527:lemma: dek-1\ "to take, *offer a sacrifice, observe a custom' [common lllyrian-Baltic d- >
```


## [2026-09-05T17:39:12.430Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"deks-\\|deḱs\\|dexter\\|dašina\\|dasina\" POK_full.txt | head -40"
}
```


### [2026-09-05T17:39:12.478Z] TOOL RESULT

```
17233:5£^iT£p6(; = Latin dexter, -tra, -/m/r? (compounds dexterior, Superl. dextimus), Oscan 
17247:as Latin dexter, -tra, -trum is a suffixed form of old PIE Root / lemma: deR-1 : "to take'. The 
18053:dexterity, adroitness ' (in addition Old Indie darhsu- " powerful wonder ', dam- " very 
19701:skillfully ', contrast infabre, fabrica^ dexterity, workshop ' (Paelignian faber\s Latin 
44905:vehement, hasty, rash, practised, shrewd, experienced, adroit, dexterous *(from horses)' = 
60948:mcymr. medru^ ein Ziel treffen, to be able ', to medr^ dexterity ' (: gr. [jsipov?); gall.
```


## [2026-09-05T17:39:14.628Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17190,17270p' POK_full.txt"
}
```


### [2026-09-05T17:39:14.684Z] TOOL RESULT

```
alb. ndieh\o feel' {*deR-skd-?)\ ndeshl\n6, encounter' probably Slavic loanword? S. 
under des-, 

Latin decet, -ere 'it is proper, it is fitting (physically or morally)', decus, -oris n. 
"distinction, honor, glory, grace; moral dignity, virtue; of persons, pride, glory ', dignus^ 
worthy, deserving; esp. of persons, usually with abl. or genit. of things, worth having, 
deserved, suitable, fitting ' (from *dec-nos, actually ' adorned with'); Umbrian tigit decet 
(see in addition EM. 257); causative doceo, -e/ie' instruct' ('lets accept something '); disco, 
-ere, didTci^ to learn, get to know; 'discere fidibus', to learn to play on the lyre; in gen., to 



receive information, find out; to become acquainted witli, learn to recognize ' (from *di-elR- 
sko); 

Old Irish dech'the best ' (= Latin decus); also in PN Echuid {* eRvo-deR-s), Gen. 
Echdach, Luguid, Gen. L u/gdech {proto Irish Lugu-deccasW\\h cc= R), whether does not 
stand for efor older r, then to de/R-'po\nt', in the meaning "order'. 

Perhaps here Germanic *teh-udn\n Old English teohhian, t/ohh/an' mean, decide, 
define, ordain, determine', feohh, //b/?/? "troop, multitude, crowd, group of people ', feon 
{*tehdn) "decide, define, ordain, determine'. Old High German g/zehon' bring in order'. 
Middle High German zeche^ alignment, guild, brotherhood, colliery, association ', Modern 
High German Zeche, Middle High German zesem {* teksma-) "uninterrupted row', 
wherefore perhaps with lengthened grade ( *fej-ud) Gothic fewa "order', gatewjan 
"dispose'; s. above also under deua-^ move spatially forward '. 

Doubtful Old Church Slavic desg, des/t/"i\n6', Serbo-Croatian desTm des/t/"meet', refl. " 
meet somebody ', Czech po-des/t/an6 u-des/f/" catch up, catch'; changing through ablaut 
russ. -Church Slavic o'c»s///"find, meet'; s. also under des- 

Tocharian A faR- "adjudicate, decide, determine'; dubious A tasRmam {* taRsR-mam) 
"similar'. Van Windekens Lexique 137; Pisani Re. R. 1st. Lomb. 76, 2, 30. 

For e5-stem Old Indie dasas(yati), Latin decus\he words stand for "right' (Specht KZ. 
62,218). 

deRs- with variant suffixes: 

common Old Indie gh- > Rs- 

Old Indie daRsina-, daRsina- "on the right, to the south, skilful', Avestan o'as//7a- "right', 
Lithuanian des/nas6s., des/ne't\r\e right hand'. Old Church Slavic o'es/7b "right'; gr. 
5£^iT£p6(; = Latin dexter, -tra, -/m/r? (compounds dexterior, Superl. dextimus), Oscan 
o'es/rs/ (abbreviated from *destrust) "it is on the right ', Umbrian destrame' on the right 
side '; gr. 5£^i6(; "right, heralding luck, skilful, adroit' (from 5£^i- with formants -Fo-, 
compare gall. Dexsiva dea)\ (the suffix -i/o- probably aiter* /a f-uos, sRaZ-uos 'Wnks') Old 
Irish dess ^on the right, to the south', cymr. deheu {*deksovo-) ds., Gothic tafhswa. Old 
High German zeso "right', Gothic tafhswd-0\6 High German zes(a)wa^\he right hand'; alb. 
djathte ' ng\r\t' (that from G. Meyer identical with it Church Slavic destb is probably 
corruption for desnb, s. Berneker 187). 



Note: 

The etymology of G. Meyer seems erroneous because of the common alb. -R- > -//?- similar 
as Latin dexter, -tra, -trum is a suffixed form of old PIE Root / lemma: deR-1 : "to take'. The 
-ter,-tra s\x^\x has been attested in Avestan lllyrian alb. and Latin Hence before -tra, -ter 
suffix the -k- becomes usually -ks- in all the above mentioned languages. Hence alb. 
{*dek-) djath-te 'nght' evolved from the common alb. -k- > -//7-like in alb. {mag-) math'b\g' 
while -Zeis the common alb. suffix as in alb. maj-te'\eit' from Latin ma/e'ba6\Y, ill, wrongly, 
wickedly, unfortunately, extremely'. 

References: WP. I 782 f., WH. I 330 f., 346 f„ Trautmann 53, 54, Schwyzer Gr. Gr. I 648, 
678, 684, 697, Wistrand Instrumentalis 14 ff. 
Page(s): 189-191 

Root /lemma: deR-2{\ doR-, deR-) 

Meaning: to tear 

Material: Old Indie da'sa^ protruding sheet filaments at the end of fabric, fringes '; Irish dual 

"lock, curl of \\a\r\* doRlo); Gothic taglu. "single hair'. Old Norse taglu. "the hair in the 

horse's tail'. Old English tgegl{ev\Q\. tail) m. "tail'. Old High German zageridW, sting, prick, 

male member, rod'; 

Gothic tahjan^ rend, pull, tear, tug ', d/stahjan ^ scaiier' , isl. t^eja, taa^ teasels ',
```


## [2026-09-05T17:39:15.194Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '63520,63620p' POK_full.txt"
}
```


### [2026-09-05T17:39:15.240Z] TOOL RESULT

```
Note: besides ok-, see there 

Note: 

Root / lemma: ok"- : to see; eye derived from Root / lemma: deik- : to show' : Root / 

lemma: dek-1\ "to take, *offer a sacrifice, observe a custom' [common lllyrian-Baltic d- > 

zero]. The drop of initial d- in proto Aryan languages Irft the bare laryngeal /?-. 

One of the oldest cognates is Gr. 5ok£uu) ' to see, discern, perceive, observe; to think, 

suppose, imagine, expect ', then Marathi dola {*dokula) 'eye'. 

Material: Aryan out of the compounds only forms of stem *ok"t^- (whereupon partly the /■ 

and /7-stem is layered): 

Old Indie aksiu. 'eye' (this /-stem ved. only Nom. Akk. Sg. and in compounds, aksi-pat 
'a little, a bit', after ved. also in b^^-case and in Lok. PI.), Gen. Sg. aks-n-ahe\.c., Nom. Du. 
aksT= Avestan as/' (both) eyes ' 

Common Old Indie -g"h- > -ks- : Avestan -g"h- > -xs-, -s-. 

(compare *ok"'/'6s. in Lithuanian ak/, Old Bulgarian oc/ and as base from Armenian ac-k' 
and gr. oooz), formation of conservative stem *aks-, this stem aks- a\so in ved. an-ak 
'blind'; Avestan as/ior *axs/'aiter us/bears', compare Avestan aiwy-axsayeinti^ they 
supervise ', a/WyaA's/a/'- 'supervisor, custodian, keeper'; redupl. Old Indie Tksate^ sees ' 
(Indo Germanic '^"'-from *i-ok"-)\ aksa- m. 'dice, cube', i.e. ' provide with eyes '^ksana-m. 
n. 'instant, eye blink' (seems grown from a Lok. *[a]ksan)\ is not overgrown the A«-stem in 
the darkened compounds Old \v\6\c pratTka-^ turned, opposite ', n. 'face (with the eyes and 
mouth)' (: npoa-wnov), anJka-n. ' the turned, front ', Avestan aimka-m. 'face (with the 
eyes and mouth)' ( *proti, *eni+ ok"-\ compare Slavic nicb under *ni- 'low, mean'), ghrtacTt 
' greasy (looking); sacrificial spoon ', svitTcfi. 'gleaming'; 

Armenian (with expressive gemination) akn. Gen. akan^eye, aperture, hole' (/7-stem), 
Nom. PI. ac-^'pluralized from dem Nom. Du. *ok"r, 

gr. {*oks/) oooz Nom. Du. 'Augen' 

common Old Indie -g"'/!- > ks- : gr. -g"h- > -ss- 

( *ok"ie^o'c *ok'%, Attic *6TTe, whereof TpioTTi(; ' necklace with three glass eyes '; 6aao|jai 
'see, observe (spiritually), foresee, predict', Attic OTieuoijai 'foresee, predict, dread'; 

common Old Indie -g'^h- > ks- : gr. -g"h- > -ss-: -tt- 



onjopai " I will see ', common Old Indie -g^h- > ks- : gr. -g"'h- > -k"'h- > -phs- 

OTTOJTTa 'have seen'; onlTTEuu) " gawk at, look after ', napGsvoniTTri^ " overseer of girls ' with 
redupliz. root on (i + on >Tn-); 6|j|ja "eye' (*6n-[j/7), 



common 


Old Indie 


-g^h- 


> ks-: 


gr. 


-g'^h- 


> -k". > 


-p- 




6(p9-aA-fj6(; "eye' ( 


*ok'"t3h- with 


expressive Aspirata?); 




common 


Old Indie 


-g^h-
```


## [2026-09-05T17:39:20.474Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17120,17192p' POK_full.txt"
}
```


### [2026-09-05T17:39:20.525Z] TOOL RESULT

```
nachhom. also " investigate ' (*5i-5ja-[jai), next to which due to *5ia-T0- Attic ^r|T£w " strive 
for, let me be concerned with '; here with originally *dja-: ^aAr| "storm, violent movement, 
particularly of the sea', l^aKoo, "whirlpool, violent movement of water'? 

compare about gr. words containing the ^ Schwyzer Gr. Or. I 330, 833. 

Old Irish oVa/? "quick, fast', dene^ quickness '; Latvian deju, d/et^dance', d/ede/et^go 
idly'. About Lithuanian da/nalo\k song' (to deja' lamentation?') compare MiJhlenbach- 
Endzelin I 432 with Lithuanian 

Ouite doubtful cymr. d/g^mad, wicked, evil', russ. dfkij^\N\\d\ Lithuanian o'j7/ras"minxish, 
wanton, bratty, unengaged, leisured, unemployed, idle, lazy', Latvian dlkslree of work'. 
Old Church Slavic divbjb^WM (Berneker203 f., MiJhlenbach-Endzelin I 478, Trautmann 
54). 

Not here gr. 56va^ "reed' (new Ionian 5ouva^ and occasional Doric 5u)va^ metr. 
lengthening? Schuize Qunder ep. 205, Boisacq 196), 5ov£U) "shake', aAi5ovo(; " rove about 
in the sea' and Latvian duonis, duo/i/'reed, bulrushes '. 

References: WP. I 774 ff. 
Page(s): 1 87 

Root / lemma: de/c-l 

Meaning: to take, *offer a sacrifice, observe a custom 

Material: Old Indie dasasyat/" proves honour, venerates a god, is gracious' (Denomin. of 

*dasas- = Latin decus), dasai. "state, status, fate, destiny'; Avestan dasamn. "property, 

belongings piece '; Old Indie Desiderat. dJksate^\s consecrated', f/zTtsa "consecration' {*di- 

dR-s-\N\Vc\ secondary /), daksati^\s proficient, makes it right, is compliant', daksa-h 

"proficient, skilful' (but Avestan daxs- "instruct, teach, instruct', npers. daxs^ business, toil' 

stay away because of the Gutturals), lengthened grade Old Indie dasnoti, dasti, dasati 



'offer a sacrifice, give, proves lionour, grants', dasvas- 'hononng the Gods, godly, pious'; 
Avestan ^yas/a- 'receive, obtains, attains ' (participle); 

after Frisk Etyma Armen. 25 f. here Armenian a/7cay'gift' from *and-tisati- (proto- 
Armenian -//is- from *deR-)\ whether tesanem'\ behold '? (compare under 5ok£uu)); 
different Meillet Esquisse 135; 

gr. (Ionian Aeolic Cretan) SsKopai 'take in, accept', Attic 5£xo|jai, athemat. hom. 3. PI. 
5£xaTai (x after *5£x6u), Infin. 5£x6ai), Aor. 5£kto, participle 5£YM£voq, compare 
npoTi5£Y|jai npoa5£xofjai Hes. (yp instead of kjj); k is preserved in 5ok6(; '[absorption] 
beam ', 5oKav Ghkhv Hes. (out of it Latin doga 'a sort of vessel (perhaps a measure)'), 
5oKavai ai aTaAiK£c; Hes., 5£^a^u) ' to captivate, fascinate, be impressive ', 5u)po-56KO(; 
'the take of presents', 5£^a|j£vri (participle Aor.) 'water container, water carrier ', api- 
5£iK£T0(; ' distinguished ' (£i metr. lengthening); nasal present *5£iKvv|jai (: Old Indie 
dasnoti) in participle 5£iKvup£V0(; 'rendering homage, honoring, greeting ', to 5£iKav6(ji)VTO 
"to greet'; intensive 5£i5£xaTai ds., 5£i-5iaKO[jai 'greet' (for *5r|-5£(K)-aKO|jai after the 
present auf -ioKU)); 5£i- could be read 5r|- (Indo Germanic e), 5£ikv- also 5£kv-, and 5£iKa- 
could be metr. lengthening for 5£Ka- (Schwyzer Gr Gr. I 648, 697); causative 5ok£(jo (= 
Latin doceo'to teach, instruct (with ace. of person or thing); with clause, to inform that or 
how; 'docere fabulam', to teach a play to the actors, to bring out, exhibit', 5ok£T poi 'it 
seems to me' ('is suitable to me'); 56^a f. 'opinion, fame' (*5oK-aa), Soyija n. 'decision', 
56ki[jo(; ' respectable, approved '; 5ok£uu) ' to see, discern, perceive, observe; to think, 
suppose, imagine, expect ', Trpoa-SoKau) ' anticipate, expect'; about 5i5aaKU) see below 
cfens-1. 

Maybe alb. Geg o'o/re 'custom, ritual, tradition (observed)', {*deuk-) dukem ^appear, seem'. 

Alb. shows that from Root / lemma: cfeR-1 : 'to take' derived the nasalized Root / lemma: 
tong-1 ( *teng^ : 'to think, feel'. 

alb. ndieh\o feel' {*deR-skd-?)\ ndeshl\n6, encounter' probably Slavic loanword? S. 
under des-,
```


## [2026-09-05T17:39:33.937Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"daxs\\|daxš\\|dak.s\\|Guttural\" POK_01.txt | sed -n 1,40p"
}
```


### [2026-09-05T17:39:33.996Z] TOOL RESULT

```
590:^Zusammenschnüren  der  Kehle;  Unruhe^  Angst.  Kummer*/  amjus-tus  ,eng-^ faiis  '^■anghos-to-s)]  angiistiae  ^Enge,  Klemme^  Schwierigkeiten^;  über  kel- tisches s.  0.;  anord.  angr  m.  (vielleicht  ursprüngl.  neutraler  esSt.,  Fick* III  12)  ^Verdruß;  Schade^  Betrübnis^;  afries.  angost,  ahd.  angust,  nhd. 'bigst  (aus  *anghos-ti-  nach  *anghu-  umvokalisiert);  aksl.  qzosti)  ^Beengung^; lit.  afikstas  ,eng^  (A:-Einschub^  nicht  Gutturalwechsel)  kann  für  *anz[a]s-tas oder  '^' anz-tas  stehen.
1325:Mit  auslautenden  Gutturalen:  ai.  bük-kära-h  ,Gebrüll  des  Löwen^, bukkati  ,bellt^  (av.  bucahin-  ,der  das  Geheule,  Gefauche  an  sich  hat', buxti'  ,Heulen,  Fauchen'^?),  gr.  ßvKTVjQ  ,heulend^
1354:Gutturalerweiterungen:  |
1711:Mit  Gutturalerweiterung-en:
2516:Unklar  ist  der  Guttural  in  den  germ.  Formen:  *brugi-  aus  Hruui-, oder  k-  Suffix?  S.  Kluge^i  unter  ^Brücke'  und  Specht  Dekl.  2113  f^^  ^er Zusammenhang  mit  1.  bhrü-  annimmt.
2730:X.  dek-   ,nehmen,   aufnehmen',    daher  ,begrüßen,   Ehre   erweisend    Aus  der Bed.   ,annehmen,   gern   aufnehmen'   fließt  die  Bed.  ,gut  passend,  ge- eignet, sich  schicken,  ziemen,  es  jemandem  recht  machen;   als  unan- nehmbar darstellen,  etwas  einem  gut  scheinend  machen,  lehren,  lernen'; dekos-  n.  , Zierde,  Ehre'. Ai.  dasasydti  ,erweist  Ehre,  verehrt  einen  Gott,  ist  gnädig'  (Denomin. von   *dasas-   ==  lat.   decus),   dasä    f.    ,Zustand,   Schicksal';    av.   dasdm   n. ,Habe,  Vermögensstück';  ai.  Desiderat,  dlksate  ,weiht  sich',  dlksä  ,Weihe' (*di-dk-s-  mit   sekund.  i),   ddksati  ,ist  tüchtig,   macht  es  einem   recht,  ist gefällig',  ddksa-h  ,tüchtig,  geschickt'  (aber  av.  dax§-  ,lehren,  unterweisen', npers.  daxs    , Geschäft,   Mühe'    bleiben  wegen   des   Gutturals    fern),  dehn- stufig ai.  däsnötij  dästi,  däsati  ,bringt  Opfer  dar,  erweist  Ehre,  gewährt', däsvds-  ,die  Götter  ehrend,  fromm';  av.  däUa-    ,erhalten,  erlangt'  (Partiz.); nach  Frisk  Etyma  Armen.  25  f.  hierher  arm.  dncay  ,Gabe'  aus  *9nd-tiS' äti-  (urarm.  -tis-  aus  *dek-);  ob  auch  hierzu  tesanem  ,ich  sehe'?  (vgl.  unten doy.sva))',  anders  Meillet  Esquisse  135;
2971:terren  ^zanken^,  ndd.  terren,  tarren  ,reizen;  necken',  ahd.  zerren  ,zerreii'; £0t.  intrans.  dis-,  ga-taürnan  ^zerreißen'  ( :  ai.  drndti),  holl.  tornen  ,sicli auftrennen';  vgl.  nominal  ags.  as.  torn,  ahd.  zorn  ,Zorn,  Streit^  heftiger XjQwille'  und  in  ursprünglichster  Bed.  holl.  torn  ^Spaltung,  Scheidung-^ /_-  ai.  dlrnd-,  cjmr.  darn-j  auch  ai.  dlrnd-  heißt  außer  ^gespalten'  auch verwirrt;  in  Verzweiflung  befindlich');  woneben  hochstufig  anord.  tjgrn f,  (*derna),  tjarn  n.  (*dernom)  ^kleiner  See',  ursprgl.  wohl  ,Wasserloch' (y<r\.  ai.  dara-,  darl  ,Loch  in  der  Erde');  zu  ga-taürnan  trat  kausatives (iteratives)  gatarnjan  ^berauben'  (aber  ahd.  uozurnen  ^verachten'  ist penom.  von  *uo-zorn)'^  got.  gataüra  m.  _,Riß';  gataür^s  i.  ^Zerstörung' (=:  ai.  dfti-,  gr.  öciQGig)'^  anord.  tord-  in  Kompositis,  ags.  tord  n.  ,Kot' (*df-töm  ;Abscheidung',  vgl.  lett.  dirstu,  dlrst  ^cacare',  dirsa  ^der  Hintere', >Iühlenbach-Endzelin  I  470,  und  von  einer  Gutturalerweiterung  mhd. zurch,  zürch  m.  ,Tierexkremente') ;
3092:air.  derucc  (gg),  Gen.  dercon  ,glans',  cymr.  derwen  , Eiche'  (PI.  derw), bret.  deruenn  ds.,  gall.  Ortsname  Dervus  (, Eichenwald'),  abrit.  Derventiö, Ortsname,  VN  Derväci  u.  dgl.;  air.  derh  ,sicher';  reduktionsstufig  air. daur,  Gen.  daro  ,Eiche'  (devu-),  auch  dair,  Gen.  darach  ds.  {*d^ri-)j  air. daurde  und  dairde  , eichen';  abgeleitet  gall.  *d{a)rullia  , Eiche'  (Wart- burg ni  50);  maked.  ödgvXkog  f.  , Eiche';  schwundstufig  *dru-  im  Ver- stärkungswörtchen  (?  anders  Thurneysen  ZcPh.  16,  277:  ,Eichen-':  dru- ia  galat.  dgv-vaipLSTOv  ,heiliger  Eichenhain'),  z.  B.  gall.  Dru-talos  (,*mit großer  Stirn'),  Druides,  Druidae  PL,  air.  drüi  ,  Druide'  (,der  hoch  weise', *dru-uid-)j  air.  dron  ,fest'  (*drunos,  vgl.  ai.  di'u-na-nij  däru-nd-,  drö-na-m), mit  Gutturalerweiterung  (vgL  unten  nhd.  Trog)  mir.  drochta  ,(*hölzernes) Faß,  Tonne,  Kufe',  drochat  ,Brücke';  hierher  auch  gallorom.  drütos , kräftig,  üppig  (:  lit.  drütas)\  gr.  PN  JgvTCJV,  air.  drüth  ,närrisch'  (:  aisl. trädr  , Gaukler'?),  cymr.  drud  ,närrisch,  tapfer'  (das  cymr.  ?fc  stammt  aus den  roman.  Entsprechungen);
3297:Gr.  ölxcc  ^zweifach,  in  zwei  Teile  geteilt^  (nachhom.  dr/f],  di^ov),  woneben (durch  Kreuzung  mit  *öc-&d  zu  ai.  dvidhä)  hom.  di^^cc  ,dixa',  davon  ion. öi^ög  ,zweifach^  (*<^^X'^W  oder  *(5txö'og),  und  diOGÖg,  att.  öiTTog  ds.  {*dixil^t Schwyzer  Gr.  Gr.  I  598,  840);  über  hitt.  dak-sa-an  ,Halbteil^  s.  Pedersen Hitt.  141.
3364:fac'ilis  , (tunlich)  leicht',  umbr.  facefele  ds.;  facies  , Aussehen,  Erschei- nung,  Antlitz',  facinus,  pontifeXj  artifex  bene-ficus  u.  dgl.;  zur  Bed.  von interficiö  ,töte'  (,*lasse  verschwinden')  vgl.  ai.  antar-hita-h  ,versch wunden'. Dieselbe  /c-Erw.  außer  in  gr.  eO^rjxa  auch  in  &rj'Ar]  , Behältnis',  ai.  dha- kd-h  , Behälter'  und  phryg.  ad-öayisv  ,afficit',  Med.  aö-öaxsTOQ]  ven.  vha^s&o ,fecit'  (*fak-s-to,  das  /  wohl  aus  dem  Ital.);  hitt.  dak-ki-es-zi  (dakkeszi) , macht,  stellt  hin'  (:  lat.  facessö),  dak-su-ul  (daksul)  , freundlich'  (:  alat. facul)]  vielleicht  toch.  A  täkä  ,ich  wurde',  B  takäwä  ds.  (anders  Pedersen Toch.  194);
3410:Ai.  ddhati,  av.  dazaiti  , brennt'  (=  lit.  degü^  aksl.  zegg,  alb.  djek)^  Partiz. ai.  dagdhd-h  (=  lit.  degtas),  Kaus.  dähdyati]  däha-h  ,Brand,  Hitze',  nidagha-]^ , Hitze,  Sommer',  npers.  däy  , Brandmal'  (dazu  spätgr.  ödyalog,  -ig  ,rot- braunes  Pferd'?);  av.  daxsa-  m.  ,Brand';
3626:Gutturalerweiterungen:
3979:fitiüg{b)ster'  ,Tocliter';  Guttural  wie  bei  *eg{h)om  ,ich',  s.  dort.
4437:2.  Wasservögel:  el-,  ol-,  mit  Gutturalerweiterung  oder  r-  und  u-Stamm; Gr.  1.  iXiä  f.  ,ein  kleiner  Sumpfvogel'  (zu  eXog  n.  ,Sumpf  ?);  2.  sXujQiog
4452:Gutturalerweiterung  liegt  vor  in:
4539:E.  Gutturalerweiterungen:
5007:lat.  ricinus  1.  ,ein  sich  in  die  Haut  von  Schafen,  Hunden  oder  Rind- vieh einbohrendes  Ungeziefer,  Zecke'  (unsicher  ist  die  Zugehörigkeit  von 2.  ,eine  Strauchart,  Ricinus  communis')  kann  auf  älteres  *recinos  zurück- gehen und  mit  lit.  erke  , Zecke,  Schaflaus'  (*erkia),  lett.  erce  , Kuhmilbe, böse  Person'  unter  idg.  *erek-  zusammengehören.  Weiterhin  ist  zu  ver- gleichen arm.  o{r)jil  ,Nisse,  Lausei'  (hier  scheint  eine  Wurzelvariante er{e)gh-  vorzuliegen,  wie  auch  in  der  folgenden  alb.  Form)  und  orJciun ,ringworm,  itching,  erysipelas'  (aus  *orqiiöno-  (?)  mit  einem  -rzo-Suffix  wie im  Lat.  nach  Petersson  KZ.  47,  263  f.),  alb.  ergjiz  ,kleine  Laus'  (s.  ü.  Meyer Alb.  Wb.  96;  Zweifel  bei  Hermann  KZ.  41,  48;  doch  kann  der  abweichende Guttural  im  Armen,   und  Alban.   auf   tabuierender   Entstellung    beruhen).
```


## [2026-09-05T17:39:34.570Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"daxš\\|daxs\" BRT.txt | head -60"
}
```


### [2026-09-05T17:39:34.619Z] TOOL RESULT

```
<persisted-output>
Output too large (37.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bozig29me.txt

Preview (first 2KB):
3438:aisqm  kain!l{%A.)  jamaiil  aznaahqm  at.. taibyS  x!akr?m  .  .  "und  wenn . ,,  dann . ." Y,jO.8;50.9.  b)  hinter _>'ezr:  yezJ  a^ä st3  AaÜTm  (sd.)  .  ■  at  tat  m^i  daxslim data  . .  mai>!ä  (sd.)  .  .  "wenn  . .,  so  .  ," Y.J4.6;  48.\',  —  yezl  ais  nsil  .  .  adi4 aibijf^rps/ä{sd.)..at  vh ..  ay^i"öiiL  somit .., "  Y. j/.  2.  c)  hinter  Ayaf:  hyat  tJ
3689:•  j.  *aipi.9r«tö.-gitav- ')  Adj.  (auch  fem.) 'der  einen  fest  bestimmten,  fest  zugewie- senen Platz  hat  (,  den  er  nicht  verlassen darf)':  yat  ahmt  nmJne..  nilirika  daxsta- vaitj  anhat  yat  v.l  *sk^dS.aipi.jatS [pisirsY'>  'tus  (NSf)  "wenn  in  dem  Haus . .  eine  Frau  die  Regel  hat''  oder  wenn sie  wegen   eines   ihr   zugefügten  körper- 1
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g, 
...
</persisted-output>
```


## [2026-09-05T17:39:43.304Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"1.  dek-   ,nehmen\")>0) print \"leaf\",n}' POK_01.txt; awk 'BEGIN{RS=\"\\f\"} NR==197{print \"---LEAF197---\"} ' POK_01.txt >/dev/null; grep -n \"deks-\\|dek^s\\|dasina\\|dašina\" POK_01.txt | head"
}
```


## [2026-09-05T17:39:43.335Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lehren\" BRT.txt | head -30"
}
```


### [2026-09-05T17:39:45.139Z] TOOL RESULT

```
2741:deks-  mit  verschiedenen  Suffixen:
```


### [2026-09-05T17:39:45.177Z] TOOL RESULT

```
5739:•  j.  a-sä£ayant-  Adj.  'nicht  lehrend';  ys saite  haurvqm  iarasca  xsapanim  ayaztmnö ..  asixsJ  asJäzyS  . .  "..  nicht  lernend,  nicht lehrend  . ."  V.  iS.  5.
8902:•  j.,  g.  kaeJ--  V.  'lehren'.  Praes.  1  cai"^-, 8  cim'ii-.        PPfP.  äsia:
8903:'lehren,  belehren';  das  Sachobjekt  wird a)  durch  den  Inf.  gegeben;  nflit  iinto  ahm'i nöil  iistä  m^rjtö  b  nla^a  (sd.)  daimayili  "ich bin  nicht  .  .  gelehrt  zu  .  .  hegen"  V,  :■. 3.  b)  durch  einen  Satz  mit  yaüt:  k} hvi>  y»  mä  . .  ^vi'iat  (3SPrA.)"  ya>,l  'iTo.l ..  uüjmJ/u  (sd.)  V.4<i.g'K  a)  bes.  in religiösen  Dingen  "überzeugendideslSessernj belehren'  sva.  'bekehren'^':  yii/  Ars  Auma- yai^a  (sd.)  tiyiii'a  ana'^iimaide  (Konj,)  Vr. rj.  4.  a)  mit  Lok.:  a/yv  iik.'m  dr.'gi'\üti ' .  .  siisinibyl  (sd.)  r,>  vansaitl  vauh^iu  rä iW>i/(/t'(Konj.)  astim  ". .  oder  aber  seinen I  Anhänger  zum  Guten  bekehrt"  Y.  5J.  2«*.
8929:•  j.,  g.  ^kaes-  V.  'lehren'.   Praes.  i  .W/-;
8931:I)  'lehren',  mit  praed.  Akk.  sva,  'etwas lehrend  bezeichnen  als  ..';  humaya  upauha (sd.J  clsmaide  ahunahe  vairyehe  Y.  27.  7; Vr. /2. ».  i)    'lehren'    spei,    in  Bezug'
8939:mit  frA  'lehren',  mit  Akk.  der  Sache und  Person:  hyal  vi  .  .  syaohatDin  .  . fraanas  (sSPrA.)"'  ..  3:%^  (sd.)  Y..?2.5, Pü. ;  casUan,  5ü. ;  äsvädayilum  (ausser  Y.  31. 3,  wo  faii/iiäpitum);  s.  noch  No.  1, 4-7, 10.  — ■)  Falsch  beurleilt  BB.  21.  177;  s.  No,  2.  — ')  Mit  1  für  i,  S  2/p-  2;  s.  No.  I.  —  3)  Vßl. iBed.  Gdn.  'Stud.  /.  68,  134,  Bn.  Stad.  i. 305;  s.  auch  PüErl.  lu  Y.  44.  6,  ^.  18  in No.  4.  —  »  Pü.  crl.;  tahd  kakel;  ähnlich  zu  , Y,  44.  6.  —  S)  Pü. :  /raiänaÜA;  vgl.  tael- \ No.  5.  —  *)  Pü.  fugt  erl.  htniu;  ö  iasiiti.  —  1 J)  Pu.  erl.;  bitn  u  bar  hamäk  pa  3?eSh  i  öht-  1 tiKod  däiim.  Ähnlich  auch  m  Y.  13.  i.  —  ! B)  Die  Stellen  mit  i-iiiasti  und  pnra.linasti  sind  ' zT.  undeutlich;  vgl.  daiu  !UUG  SBayrAW.  ' iSys.  I.  124,  GON.  KZ.  2/.  J46,  BN.  Slud.  /. 304,  WEST  SBE.  i/.4S7,  461.  463-  —  «  Vyl. da2u    die    verschiedenen    Bedeutungen    von
9453:•  1.  'kas-  V.  lehren.  Praes.  i  oir-.  ^j   jj^„i  „„-irnK   diaytnl,   Jlins
9454:I)  lehren,  mit  Dat.  der  Pers.  und  Akk.  ,j^a//^,„  /ajtu/i  Vt. ;.?.  24.  a)  spez. der  Sache:  ^'it  'ttra^äli  (sd)  'mqinm  ,g„„  t,.„„„  i^^^^  wollen',  auch  mit ail,n  N.  17:  —  mrt  „laom  ..  arnua  i„f  ^^,  q^  .  ^,  j„„,j  ^j;,  ,„„r  i» Aii/«(sd.)  taianäicn"  .  .  xraftm  asa-  ^„„1^^;  „  ^aUlm  inl  (iS.)  a/imai ,m„S.S4-  2)  'Unterricht  erteilen,  „^^  „„„a»to  ya  ' nmyäJyäi  mantä imt  Dat  der  Pers.:  (*«/)  »I  dalvayatnlt  „„/^^j  "da  ich,  der  Priester,  durch  ^& !'J         •zl?5>:,j.   (sd.)   *ä.il./(l>  N.J7.  ^1,    „jh,„   (pfj^j    ,.„„„    I^„5„    „ill)
9455:eJ^re':Tr''."denXS'el^.,:'sS-3"'-  "»  i'"  »»»'l»  "«'l'  rahUtaMai.yav ai.  f<i.r/c  'er  sieht",  mp.  i//o/tf«r4  (s.  lu  z^K/qi,  kennen  lernen  will,  die  Landwirtschaft P0>,  äj/itt  'Obacht  geben'  (GIrPh.  /b.309),  in  jenem  Geist  zu  betätigen,  in  dem  es"' «p.  (Pü.)  ^äiiian  •lehren'.  -  0  Y.7  Sieht  äiic;  s. '  gedacht  ist"  Y.  !  J.  6 ". "^ri^Tl^^^^li^i^-""'"'^  niit  .A,  -?r;  ,pa  ^^,  k^.kän,aiäe .      ,    ,           .(Konj.?)  Vyt.22.
10234:•  g.  gaire  Inf.  'zu  wachen  über-'  (Akk.); yS  *urvqtiim  min  g°  . .  dadl  aslscä  vldus (sd.)  . .  yavat  isät  (sd.)  .  .  avai  xsäi  aesl asahyä  "der  ich  des  eingedenk  bin  über die  Seele'*  zu  wachen  .  .  und  .  .  sie  .  , lehren  will,  das  A.  zu  suchen"  Y.  2S.  4.
10691:•  j-,  g.  xsä-  V.  'lehren'.  Praes.  3  xsa-\ Perf.  I  caxs-.  —  PPfP.  xiSta-,  'xs/a-'\
12534:(sd.)  xiii'^fvm  Y.  51.  a;  —  6>rtx&am  mSi forasaeitrS  kvB.gvl!  däedöii't'i*  kihrpsm  .  . yam  . .  i^am  (sd.)  "den  geschätzten  Leib'' der  lieben  (Jui^;frau)  hat  mir  FrMv.  zuge- sprochen, welcher  . ."  Y.5J.  17;  —  <^^st (Pass.)*'  he a^Ae  avai  miiäfm{^) ..ya%a .. ^3-Tt  ^-5-44;  —  srTra  p^nsS  disyata yaha  mOvaya  ..Vyi.ß^i'i);  — jimama  tl dalsayama  U  .  .  Vyt_j2(?)  a)  '(Strafe) zuweisen  sva.  festsetzen':  avavantfm  asa- vaynyai  (sd.)  tqm  S^qm  daisayS  V.  5. 14.  3)  'Jemanden  (Dat-)  unterweisen in  — ,  belehren  über  — '  (Akk.):  ahmai  dal- nam  dalsayat  ahurd  Yt.  II.  14.  4)  'kund machen';  iä^a(ßd.)  ayärS ..firasayai dlsS (sSj-AorM.)  \.43-l.  5)  '(Jemandem) durch  —  (Instr.)  darauf  hinfuhren,  dazu verleiten,  dass  er—'  (KeUtivum):  «7a  dalna disyät  . .  yS  %riummaim  ratBm  aiwyän- kam  (sd.)  «Ji^  ahvyästi  V.  18.  9.
12599:•  j-,  g.  daxs-  V.  'lehren'.  Praes.  3  daxsa-, i4daxfaya-[,  35  •öaxJayaeta'>].  —  PPfP. •daxäa-.
12600:'lehren,  unterweisen',  mit  Akk.  der  Per- son: a^J  a^ä  cSii  (sd.)  aAurö  .  .  zara- 'hustnm  ataxsayaaa^^  (Augm.)*^  vJspa^ farasnt^la  Y.  iz.  5.  a)  mit  Inf.  als  Sach- objekt: kyat  mS  . .  daxsat  usyai  (sd.) *titsna.maiiis  vahistä  Y.  43.  r  5.
13613:•  g.  da^h-  V.  'lehren'.     Praes.  5  dldah-. Med.  in  pass.  Sinn  'von  Jemand  (Instr.)
14060:*draila-  Adj.,  PPfP.  lum  \.''iirang'.  —  PQ.; draxl  huaar,  mit  der  Erl. :  *iis  ämSUnd  *än kunil  "was  sie  ihn  lehren,  das  tut  er".  —  ')  Nach DST.  wäre  ipä  dr'  sva.  sfiä  taurunö  'Jagdhund'; s.  abei  laurana-.
25865:'lehren',  b)  Des.  'lernen':  yazamaide  .  . manmna  vtrfztmna  *jixsfmna^>  s3ca- yamna  Y.  55.  6;  —  paitihiamil>m  v>r>- sintim  *sixs>ni)m^''  säiayant>m  Vyt. 52;  —  mamitim  *r>r?zint»m  sixhnt?m sä^ayantim  P.  13.
25868:ai.  iaknili  'er  kann',  iikfoli  'er  lernt'.  —  Pü.: ämöxtan  ■lehren,  lernen';  StL:  üititum.  — '>  S.  No.  6,  7,  *iixsaya-  und  aiiiSant-.  —  ')  i (fit  fy,  S  po-  i  »■  S.  noch  No.  5-  —  ■J'  S  45- -4>  SjJ2— «  So  Pt4,  J2.  Ks.  —  6)NA. saxs' ;  s.  Var.  —  7)  Ausg.  saxi',  aber  gegen Hds. •  j.  'sak-  V.  '(zeitlich)  vorübergehen, -  sein'.    Praes.  i  ivi-»,  2  sa^a-.  —  PPfP.
26245:'heissen,  lehren',  mit  dopp.  Akk.:  data xratsul . .  razSng  voAb  säAli  mananAa "(es)  lehre  (mich)  der  Schöpfer  der  Geistes- kraft durch  VM.  (seine)  Satzungen"  Y. $0. 6;  —  y^  nä  )mBs  savatshs  pdhs  slisit "der  uns  die  rechten  Wege  des  Vorteils lehren  könnte"  Y.4J.3;  —  süa  nä  aia
26250:mit /rJ  i/rS)  'lehren,  ofiienbaren',  mit  5J-7-  4»  'Reden,  Spreeben  lüber  Je- dopp.  Akk.:  ahyä  xraiü  JrS  mi  s3stü  mandes)':  ^J  nar^m  aSaraiam  ain^.z^ifs- vahistä  "durch  seine  Weisheit  lehre  a  mich  «Jt  .  .  kavfanhs  Isd.)  'ahäi  da-iäiti ,  V. das  Beste"  Y.  45, 6; — '/rtuasta-.       a)mit   /J- a*'-  5f    Tled^    Woti":    *ambm9wf
```


## [2026-09-05T17:39:51.931Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"daxs-  V.  \\047lehren\\047\")>0) print \"LEAF\",n}' BRT.txt"
}
```


## [2026-09-05T17:39:53.043Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"fradaxsta\\|fra.daxsta\\|frädaxsta\\|daxsta-\\|daxstar\" BRT.txt | head -20"
}
```


### [2026-09-05T17:39:53.748Z] TOOL RESULT

```
LEAF 392
```


### [2026-09-05T17:39:53.795Z] TOOL RESULT

```
3689:•  j.  *aipi.9r«tö.-gitav- ')  Adj.  (auch  fem.) 'der  einen  fest  bestimmten,  fest  zugewie- senen Platz  hat  (,  den  er  nicht  verlassen darf)':  yat  ahmt  nmJne..  nilirika  daxsta- vaitj  anhat  yat  v.l  *sk^dS.aipi.jatS [pisirsY'>  'tus  (NSf)  "wenn  in  dem  Haus . .  eine  Frau  die  Regel  hat''  oder  wenn sie  wegen   eines   ihr   zugefügten  körper- 1
6650:aAl  \.32.T,  — yai^am  ta  ''paouruyl  .  .  kariamyi^^tä  man3^\\.4.i).  B)imAw.: fradaxsta   ahl  Y.5/.3;  4'-Z',  —  ^>"  ahl  aiwyiitkattfm  .  .  Bat  aiAhe  ahi  aiwylsts
6651:\.43.T,  —  idl  (2SIA.)i''>  «7  . .  vatihsu^  V.p.  26;  —  y:Ahe  mnänaya  .  .  ürq/n^ fradaxsta  manai^hs  ^.^l.xT,  —  a'^a  tu  asti paitiaanlö\.sj.j^;  —  usi-arsfpm  (sd.)
12601:mit  frä  i/rS)  dnwS.;  1)  absolut:  äat hwä  a^ra  spttita  fradaxsta  tturr/a  vi.- barm  ".  .  (darüber)  belehrte  Vögel  .  ," Y./aii.  2)  mit  a)  Akk.  der  Person und  Instr.  der  Sache:  /rB  spinta  ärmait! aia  damä  /radaxlayä^  "belehre,  o  heilige Arm.,  die  Daifiäs  über  das  A^d"  V.jj. 13.  b)  Dat  der  Person  und  Akk.  der Sache:  aet^m  md^rTtn  ma  fradaxlayS^ *ainyai  pihre  vä  pu%räi  vä  .  .  VL4.  9.
12623:•  j.  daxsta'vant-  Adj.  (fem.  'vaitf-)  'Merk- male, Zeichen  (körperlichen  Gebrechens) an  sich  tragend':  ava  daxsta  'vaniaCSP.) yä  tidil  pouru.jira  (sd.)  fradaxsta  Vt.  j. 93.  a)  nur  fem.  'mit  der  Regel  be- haftet, menstruirend''';  yai  ahmi  nmane .. tairika  •vaiH  anhat  V.  5. 59;  16.1;  — yB  nairikqm  cihravaillm  'Z'aitTm  voiuna- vaitlm  ,  .  xSudrh  avi  frattlutr^zaiti  V.  18. 67;  15.7;  —  näirikaya  ..  'vaityä  V.  16. 5.  «3.   »4-
20798:—  avat  *vy3x}mca  hanjamaiijmca  yat armSanqm  spinlanqm  G.  2.  8;  Vr.  20.  2,  Y, ig.i;  —  avat  x^ar?nS  . .  yim  (als  NSn.) vazaite  maitim  zrayaaiö  ..  Ytj.  4z;  — ave  aipi  ktsmarmts ysi  . .  miinym  druiinti Yt  /0. 45;  —  ava  ..xsa%rJi hupatSJsma  ya uitrS  paiti  ''vahairis  Yt  14. 12;  5.  93,  Y. 2j,r*;  —  ava  damqn,,yä  h^nti  paoiryö. data  Vr.  7.  4;  —  ava  daxsta  ..ya  (IS.)  nsil pouTv.Jira  fradaxsta  Ytf.ps;  —   die  Be-
```


## [2026-09-05T17:40:00.669Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==392' BRT.txt | head -120"
}
```


### [2026-09-05T17:40:02.398Z] TOOL RESULT

```
 Et,  KZ.  3S-  479  ist  sehr  iweifelbarr.  I
•  j.  daxma-  m.  'Leichenstätte,  Leichen- bestattungsort'*':  'ma  (NP.)  .  .  yaAmya nar/f  irista  niiayeinte  V._9.  9;  13;  —  sairi ..  triste  °me  nihätte  V.  7. 49;  —  avi  Ai irista  tanOm    upa    "ma  fraiaröis  \A.i2;
—  '^avai  Ai  'ma  nStt  upar»Aamäl  Vd,  l(); ig;  — *pairi  °ma  a/sayqn  vJ  'ma  caEsayqn (sd.)  V.  <?.  2;  —  'mazha  .  .  yöi  paiti  äya Zimä  bavainti  (sd.)  uzdatza  usdista  V.  7. 54;  —  nasOm  .  .  •in^m  .  .  Aixnm  V.  5. 16;  —  aeiaiTva  'ma^a  hqmJ>avainti axtisca  garmusea  .  .  V.  7.  57;  58,  55;  — *AixsaSsa  .  .  kimcit  .  .  altalsva  'tnaliva iT^un/Ä  V,  7.  50;  51;  —  nasunqmca  .. 'manqmca    aiwi.varslatiqm  (sd.)   V.5.  14;
—  °m5  F.  14.         a)    als    Aufenthalt    der
DaKia:  ..dafsa  aitaiiva  'ma^a gartApnti apoca  voipmü  ydha . .  V.  7. 55.  b)  vom Uterus  einer  Frau,  die  eine  Totgeburt  ge- habt hat:  yai  tiäiriAa  . .  apühnm  (sd.) mjasSt  usultana . .  alte  "ma  t^aaAantalta antarät    nalmäi    banhrisiia    uruiswSAva
LcE  Parsii  206,  der  auch  Abbildungen  gibt. El?    VII.   eig.  'Verbrennungsslälte',   mm  V. dag-,  %  33  h.   —    np.  daxm,  daxma.  —    Pä-: daxmai,  in  F.  mit  der  np.  Erl. :  gär  mäna  dar an  matdagän  rä  barajid.
•  j-,  g.  daxs-  V.  'lehren'.  Praes.  3  daxsa-, i4daxfaya-[,  35  •öaxJayaeta'>].  —  PPfP. •daxäa-.
'lehren,  unterweisen',  mit  Akk.  der  Per- son: a^J  a^ä  cSii  (sd.)  aAurö  .  .  zara- 'hustnm  ataxsayaaa^^  (Augm.)*^  vJspa^ farasnt^la  Y.  iz.  5.  a)  mit  Inf.  als  Sach- objekt: kyat  mS  . .  daxsat  usyai  (sd.) *titsna.maiiis  vahistä  Y.  43.  r  5.
mit  frä  i/rS)  dnwS.;  1)  absolut:  äat hwä  a^ra  spttita  fradaxsta  tturr/a  vi.- barm  ".  .  (darüber)  belehrte  Vögel  .  ," Y./aii.  2)  mit  a)  Akk.  der  Person und  Instr.  der  Sache:  /rB  spinta  ärmait! aia  damä  /radaxlayä^  "belehre,  o  heilige Arm.,  die  Daifiäs  über  das  A^d"  V.jj. 13.  b)  Dat  der  Person  und  Akk.  der Sache:  aet^m  md^rTtn  ma  fradaxlayS^ *ainyai  pihre  vä  pu%räi  vä  .  .  VL4.  9.
Vg\.'irradaxJtar-.  —  PO.  (d1ia.]:  faiAärl,  erL: bit  gufl,  Sü.:  fratyabhifala%  pa  daxsak,  Sü.: äkntna ;  frSl  daxiaiih,  Sü. :  praaknalayä  \  J'räc daxsakm,  Sü.:  /raciinaya.  —  ')  Korr.  der  NA. —  »)  Oder  Praev.  af  —  3)  Das  Praererb  ist doppelt  gesetiL  —  4)  S.  aber  Vt.  14.  46,  wo /radaiiayBis,
•  j.  dax^a-  m.  'Brand':    *dasat  ti  mqm
avavata  'sa  (IS.)  ya%a  .  .  F.  22.
Zum  V.  dag- ;  S  5S  ^'-  —  P". :  ^daiisit ;  in  der Hds.  stellt  ptin  statt  dptin;  s.  'daxita-tio.  5.
•  g.  daxSära-  m.  'Zeichen,  Kennzeichen': ka'^ä  (sd.)    ayär}  'rä   fgrasayäi   diiä    Y.
43-1-
lEt.  vgl.  'daxlta-.  —  Pü. :  daxiak,
•  j.,  g.  'daxäta-  n.  'Zeichen,  Kennzeichen, äusseres  Merkmal':  a/  tat  mdi  'tsm  data aAyä  atjAsus  vlspä  mai^ä  (sd.)  \-J4  6;
—  yqm  xsnütpm  räniiiyä  (sd.)  da  ..  aiAf aAvsAB  't»m  davBi{%A.)'^.$i.');  —  narym . .  aiavamm  *jas»nitm  aAmya  nmäne  mat avabyS    -inbyö'-'^  ydka    äiraz-a   V.  ij.  22;
—  dttxstanqm    (s.  a)  ySi    h>nti    aaraAe
dby  Google
677
'daxSta-
daJfvah-
678
mainyJtd  'ttm  mafyäi^ia  faiti  nSüÜ^m  V. z.  39.  a)  von  sichtbaren  körperlichen Mängeln  und  Leiden:  anäisca  kannis^a ..ava  -/«(IS.)  daxstavatUa  yä  rßit  peuru.- jira  (sd.)  fradaxita  Yt  5.  93;  —  ma  a%ra fi-akavö  mä  apakavS  .  .  tnüta,iSm  anyqm •tanqm  (Gen,  part  als  Subj.)  yBt  hmti anrahe  mainySus  daxStim  (s.  o.)  V.  2.  29;
—  paityanm  fräktnntat  a?»rs  mainyus ,.  arä^wyäca  'ia**  ari^wlmla  garimäum V.J.  18;  17.  b)  von  den  periodischen 'Merkmalen'  des  weiblichen  Geschlechts  J*; «)  bei  Menschen  "Regel,  MenstiuatioD': .  .  yat  .  .  näiriiayS  n^ravaityä  daxita- vaityä  vohunavaityS  't»m  uzvfnsyäi  "wenn (man)  . .  einer  . ,  Frau  die  Regel  ver- treibt" V.  /6. 1 3  <' ;  —  mä  ..  a£a  yä  Maine tarS  't?m  parayäl  (Sp.  1 52  u.)  V.  15.  9;  9;
—  yat  hi  cti^ra  fsd.)  'AM  bavatti  yat  hs •ta  aknm  bavaili  V, /ß.  I4(?);  —  Vii  F. 14.        ß)  bei  Tieren  (nur  Komp.).
Koi^E.;  Ableit.  —  np.  vgl.  daitän  'Frau,  die die  Regel  hat'.—  Vgl.  »fradaxUa-.  —  PB.  (lu Y.  J^  V.  2,  13,  l6):  daxsai,  Sü.;  ciknam;  (zu V.  /,  75):  daitän,  (lu  Y.  ßi):  daziln  «;  5.  noch No.  2,  4.  —  ■)  Die  fem.  sult  der  neutt. FormjS  412.  %A.  —  »)  Pfl.:  aparSnia  daitän,
```


## [2026-09-05T17:40:10.846Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"daxJtar\\|daxstar\\|daxitar\\|dax.tar\" BRT.txt | head -10; echo \"=== leaf 388-390 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=388 && NR<=389' BRT.txt | head -60"
}
```


### [2026-09-05T17:40:13.142Z] TOOL RESULT

```
12602:Vg\.'irradaxJtar-.  —  PO.  (d1ia.]:  faiAärl,  erL: bit  gufl,  Sü.:  fratyabhifala%  pa  daxsak,  Sü.: äkntna ;  frSl  daxiaiih,  Sü. :  praaknalayä  \  J'räc daxsakm,  Sü.:  /raciinaya.  —  ')  Korr.  der  NA. —  »)  Oder  Praev.  af  —  3)  Das  Praererb  ist doppelt  gesetiL  —  4)  S.  aber  Vt.  14.  46,  wo /radaiiayBis,
17613:•  ].,  g.  fra-daxStar-  m.  'Lehrer,  Unter- richter, Unterweisei*,  von  AHM.-,  zdl  ns mazdä  ahurä  vaahSuS  °tä  mananhö  "sei uns,  o  MAk.,  Lehrer  des  guten  Denkens" Y._^j.  17;  —  syadkanäis  lärpnß (sd.)  .. *Aizvä  ux^äit  vanfOui  manar>Ad  yatiqm tu  *paouruyS  mazdä  °tä  akJ  ",.  (sie)  für die  du,  o  M.,  der  erste  Lehrer  bist"  Y. ji.  3;  —  ^wqm  (lüroi.  mazdqm)  aiaisqm (nämL  vacarnkqm)  paifyastänmca  (sd.)  'fa- nmln  dadfmaidi  Y.J5. 9;  —  dazda  ma- nar^AS  para  im  ioa  (sd.)  mananhe  HnasH (sd.)  ^■iiSa  'fänrn  mananfu  V.  i^,  13.
=== leaf 388-390 ===
�r  die  Gottheiten der  vor  Zard^ustra  in  Iran  geltenden Religion:  cüma  .  .  Auxs'd^rä  (sd.)  °vä änkarS  .  .  aiibyS  kam  y.lis  gam  karapa usixt^ä  (sd.)  aehmtli  dstä  Y.  44-  *o;  — af  yaf  'vä  (VP.)  vtspitshö  akat  (sd.)  ma- nanha  sta  H^rsm  Y.^2. 3;  i;  —  aya (naml.  mainiva)  nSit  »ris  vSsyilta  °väcinä hyal  Jf  a-d^baoma  (sd.)  , .  upa.jasal  Y.  30. 6;  —  hya^  vi  .  -y^ns  °vSng  akaslä  main- yus  . .  syao%aiiim  ..fracinas  . .  x/ay^(sd.) Y.  J2.  5;  —  sas^ärS  (sd.)  .  .yä  zl  väv>rs- z5i  . .  °väUiä  masylisca  Y.  2p.  4;  —  hyat '"qsasutä  (sd.)  yii  daibitanä  (sd.)  fraoxti, 'iäilla  masySiicä  Y.  4^1;  —  par}  *v3 . . vacxsma  "väisca  xra/strais{sA.)  masyäiscä Y-^4.  5;  verwendet  Y.  75.  a;  —  yastä °ving  apars  masyqscä  tarS.mqsta  Y.  4^. II.  a)  GP.  mit  dam-  m.  sva.  drüjs dam-:  tsi  'VMg  (GP.)  dqn  \3  dngvais dama  (sd.)  Y.  4r).  4,  11)  'im  jAwr.* 'Dämon,  Unhold,  Teufel':  t&m  z^margüti
'äkirsnvS  vJspe  'va  zardhufira  yBt  para akmät  vtr5.rai^a  apataypn  paiii  äya  amS "du  hast  bewirkt,  dass  die  D.  sich  alle  in die  Erde  verkrochen,  die  sich  zuvor  in Männei^estalt  auf  der  Erde  herumtrieben" Y.p.  15;  FrW.4.3;  —  valtumnsm  akmat para  "va  patayjn  .  .  *apaJtarlay?n  (sd.) fainis  haca  maiyakaHbyS  aal  tä  .  .  hazB nivarKaym  (sd.)  'va  äat  tl  aivS  ahunS vaifyS  .  .  *zamangusa  avasai  vXipe  "va ayesnya  avahmya  Yt.  ig.  Za{.;  — ansürahe (sd.)  grlvaya  .  .  yat  ahmya  °va  handva- nnti  druj5  haca  girihSha  Y.^.j;  ig.44;  — alte  yei  "va  aBaisva  daxmalsva  gaafanü apaca  valpptttiY.j.$$; — Jha  'vanqm  han- dvarMS  kva  'vanqm  hantpatanS  kva  '-va hqmjivannti . .  /  . .  altaihßa  daxntaisva . .  V. 7.53 f.;  54^;  —  öAva  vyari%aAva{s,d.)  zpmS
va  Aqm^bavainH  ¥.77,3;  —  yat  yavB dayat  aaf   'va  a^U^  (sd.)  V._y.3a;  32J;
—  pas/a  para.iris/Tm  {täxa\.yaeida^ryeAe) 'va  .  .  iae^^m  ava%a  fratsrisinti  ya%a maesi  .  .  vthrkai  haüa  V.  /(j.  ^^ ;  —  va&n yji  -va  .  .  ova.mwamaAi  kisüotHa  pivasca (sd.)  V./Ä  55;  —  'va  ml .  .  aohm  (sd. hqmpmsmte  V. /p.  3;  —  ya'A  zT  hvan ndit  uzuxsydti  d',a  'va  vTspä  *m?nnHnta Yt  6, 3;  8.  44;  —  aat  Ae  pattyänm  (sd.) avaJ>ar>nti  'va  'vanqm  yasnäica  vahmaica V.  16. 11;  —  vlspanam  *zT  *ava.sras^ntam ..  'va  *ra^ai/e  (sd.)    V.68;  y.ig.2&(?);
—  'va  Aqm.rae'iui/iyati  (sd.)  Y.ig.20;  — 'va  drvantB  duldanhs  V.  ig.  3,  aS,  44— 47*;  —  'vanqm  da?u9.tim>m  Vtj.  14";  — kS  'vanqm  xawt5  (sd.)  ks  'vanam  xumbö ks  'vanqm  ia.nairls  iB  havqs{sA.)  'vS  in vispö  'vS  kö  para  m^ntö  'vS  k3  pasca m>r)tS  mainyava  'va  /raba7iainlH . .  aria:-a vjptö  ariaca  va^ayS  (sd.)  V.Äsif.;  32'; — ■  'vanqm  rapaks  V.  7.  56;  —  vi  'väiS ayais  *avat>hTs  anantail  aks.dabli  sarvm mruyl  hatqm  draojistais  . .  vT  'vais  vi daFvavatbls  Y.12.4;  6';  —  staoml  ahm ..  näismiisd.)  'vtriAP.")  W.  11.  ig— 12. 1; Yt.  7^.  89;  —  us»M^lala  masyäka  staeta ahm  . .  nTsta  (sd.)  'va  \.  18.16;  —  'va apa.dvaraia  Ytj.  7;  —  vil  apqm  ^a patmtu  vT  'väahs  vT  'vaysil  (NPf.)  Y. 70. 1 ;  —  paitistätSe  t>masciiiranqm  'z-anqm Ytö'.4;  y.  137;  —  duSmainyam  sisdyd 'vqn  apa  "asavqn(sd.)  Yt/p.84; — yaha azpm  uzbanini  hala  'vaHbyB  uyl  lüil'a saokaca..  Ytj.  26;  Jp.  23;  —  AS  (oämL
dby  Google
669
'daeva-  11
daevayasna-
670
sragis)  nlHt  tarsts  *JränSmaiU  .  .  parö •vaxibyS  frä  ahmät  pars  VJspe  'va . .  tarHa rumanie  tarUa  ttmanhs  ^dvannte  Y.  57. 1 8 ;
—  sraohm  ..yd..yBityeiti..Aata  'vaeibys Y-57-IT, — paiti-pirme  vannya  'z/fffAP."') V.  70. 14;  —  yat  baväni  aiwi.vanyä  vTspe •va  Ytp.  4,  /5.2g;  —  imi  alte  vaca  yoi fanti  vjspanam  'vanqm  snahim  V.io. 16;  16,  Y.27.1',  Y.ig.46';  —  snaihi/.. hvS.vafjim  kam^rihe  patti  "vanqm  Y.  57. 31;  31,  YtÖ-s,  jo.aß,  129,  V.79.15;  — pas^a  jainti  'vanqm  . .  fravaxaiU  mihrS Yt  70. 133;  3. 10,' 4-  2,  5-  2^.  V.J.  32;  — hasat^rayna  paiä./asaiit  aiars  .  .  'vanam mainyavanqm  ..  drvatam  Y.S.So;  Y.io. 6,  YL  13. 4S;  —  asfi»  ,  .  taurvayeintim vTspä  tbalsa  'vanqm  maSyänqmca  Y.52. if.;  5.18,  Yl/.i',  S,  6;  —yat  mqm nalcis  taurcayät  nsit  °vS  na^a  masyS  nöii yäiaz'B »a^a pairikä  YtJ.6;  J5.56,2.n(?); — paitiltätse  'vaheca  tbaiiatahs  ma^eheca Y.6S.S;  5S.3,  VLy.'"i42;  ~y8..ä>,r)m urvaaayata  °väatia  haotäti^A.)  mafyäatca Vt  13.  89;  —  'vanqm  parö  draomBku  Yt. ^3-57!  57-  S.  noch  Y.J5.  2  (Sp.  667 u.).  a)  klassifizi
rt:  mürym  . .  yahmal haca  frabr^SMii  vTspe  mainyava  (Stverz.) •va  yaica  varsnya  (Stverz.)  drvants  Yl /o.  97;  usw.;  —  paiti^tätJe  mäzanyanqm (Stverz.)  'vanam  varmyanqmca  Yt.  13,1  ^T, usw.  b)  namentlich  bezeichnet:  °vö  ao^O V. /j.  i;  —  akataam  dasum'^'^  V. 79.43  (statt  Nom.);  —  °vasca  yS  apaoSs \X.8.ii;  XI,  22,  28  (daiam^'i),  18.2,  6;  — inärS  °vS  V,  ig.  43;  —  kasvjS  'vS  V.  ig. 43;  —  daium  kund»n  V,  75.41;  —  daiwil 'vS  V.  79. 43;  —  driieis  °vS  V.  iq.  43 bßiti  'vS  Y.ig.  i,  2,  43;  —  paitisJ  °vS 'Z'onqm  da!v3JfmS  V,  7^,43;  — "^jm  dalum  V./0.9;  75.43; —  vätJm  'vö (statt  Akk.)  V.  70. 14;  —  vTzansd  °vS nama  .  .  urvän^m  bast>m  vataydti  V.  ig. 39;  —  saouru  'vS  V.  7_9. 43;  —  ar^rff mainyus   .  .  'vanqm  'vs  Y.ig.  1,  43;  44;
—  'vanqm  draoJUtB  .  .  anrS  mainyul  Yt. _5.  13.  An  verderbten  oder  verstüm- melten Stellen  steht:  'va  V.2.6  PüZ.,  FrG.;
—  •zian^m  Yt  5.95,  N._3_^.  [V.75.40: lies  daeum.jan^m.l
*)  Im  gAw.  gehört  der  BegritT  daeva-  in  die gleiche  Gnippe  wie  usif-,  'imiay- mhA  karafian- ; sd.  Die  Priester  und  Anhöiiger  des  alten  Glau- ben«, der  den  Goltesbegriff  mit  dania-  beieicii- nete,  setzten  begreiflicher  Weise  der  Einfühning
der  jjfiiiiwfrischen  Religion  hefilgen  Widerstand entgegen;  das  geht  aus  Stellen  wie  V.  jz-SfT, -  ".,  34.  8  f.,  4g.  1  ff.  uam.  mit  voller  Deutlich- ■  rochen,  der  neue  Glaube war,  ist  die  eigentliche irblasst,  am  den  'falschen sind  Dimonen,  Unholde S.  daiu  ZDMG.rfs.  157,
allgemein  angenommen
Bedeutung  von  daeva-  vi
Göttern',  den 'Götzen',
und  Teufel  geworden.
SBE.  J/.  253  No.  I. KompA.,  E.J  Ableit.  —  ai.  drvi-  m.  'Gott', dni-  f.  'Göttin' ;  mp.  (Pü.),  np.  dev.  —  1)  Nur in  daevayö,  s.  No.  3.  —  ■)  Unthem.  — 3)  %  36S.  13  «.  —  4)  S  ^SS.  22.
•  j.  'daeva-  Adj.  (fem.  'dapvj-)  'den Dapva  zugehörig,  von  ihnen  herrührend (usw.),  rfa?iisch':  kB  asti  'vö  ks  da^aySzB "wer  gehört  zu  den  Z>.,  wer  ist  ein  Z>.- Anbeter?"  V.Ä31;  32';  —  kva  asti  'vB kva  datvaydzB  Y.y.sz'y  54'.  yt77.6;  — yat  nürsm  vyämbura  (sd.)  'va  maSyäka da^vayäsB  vohuntm  vä  täc^änti  YL  7^.  54; — -  ga%Bittsca  'vJsüa  *handramana  (sd.) N.  5j;  Yt.  77, 6.  et)  sonst  von  drug-: aiXm  dahaktm  ..  'vTm  *dru/im  V.5. 8;  — Hat  ki  ha,  paiti.davata  ya.  'vi  druxl  V. 18.  $1;  —  nase  °vJ  druxs  SrB.j;  — sraosim  ..yd  janta  °vaya  drujB  Y.57. 15.
Ableit.  aus  >i/iimi-(mit  Verschiebung  des  Wort- akzenls).  —    ai,  vgl.  däiva-  Adj.,   fem.  ddivJ-
tnit    Verschiebung     des    Wortakzents    und 'rddüi^)').  —  Pü.!  dA,  (m  Yt.  //,  N.):   aus- gelassen. —  >)  Doch  s.  freilich  anch  ai.  dma-, fem.  dnri-  als  Adj. j.  danialböis  Yt.  13.  98;  lies  datvö.lb'. j.  dacuayal  F.   14:  lies  daesayai.
•  j.  daeva-yasna-  Adj.  'der  die  Dalva verehrt,  anbetet';  überhaupt  'ungläubig"*: ye^he  .  .  näirika  avayi  xfudrä  Aqm.- rafktoayeiti  mazdayasnanqm  'nanqmca N.  77'';  ~  kalärö  paurvB  ämayante  (sd.) maidayasna/ibyB  va  'nalibyB  vä  V.  7.  36; 37;  —  drvafäB  'naahdYt.  5.  94;  —  huma- yak»m  'n>m  drvanttmca  ..Y\..^.\\y,  109, 5.37;  —  drvatam  'nanqm  Y.ig.  26,41, Yt5.68,  ;;.  4,6;'  —  dusmainys .'. 'n^iAP.) A.  7,  11;  —  daffnqm  'nanam  Y,  72. 1 1 ;  —
'darSnikahe  'nahe  Y\.g.io;  —  v>krk»m ^yim  bizangrgm  'mm  V.7.S2PÜZ.;  —  yat I  mi  avavai  'nanqm  mjat?m  ya%a  . .  Yt 1 5.  7  7 ;  —  yä  haca  'natüyS  . .  apa.bara Usd.)'S.54;—yajpacnrrm  '»ff  (statt  AS.) \h»rmtat  V.7.37;  37'; —  •»?«  vä  tanu.- ^  ppr>%>m  (sd.)  vä  N.  705;  —  'nahe  vä \lanu.p>r^'^ahe  va  N.ii;  *F.iO^;  —  'näi vä  tanu.p>r3%äi  vä  N.  77;  *l8;  —  'nat I  va  tanup?ri%at  {va)  N.  lO;  —  vTspanqmcä
dby  Google
•  j.  daeva'vant*  Adj.  'vod  den  Dalva umgeben,  es  mit  ihnen  haltend,  DaOia- genösse':  vT  .  .  sanm  mruyl  .  .  äalvaU vT  .  .  'vafbll  vT  yatu/  vT  yätumaj&ii'  Y,
12.  4.
ai.  lüvävaHl-  Adj.    —   Pü.:  dev  ayäwär,   erl.:
•  j.  daevÖ.kaHita-  Adj.  'von  den  Dasva bewirkt,  veranlasst":  paitiMtSe  *take  i^ai- Saahö  YLy.137.
Vgl.  JahiiJratarSla-.
•  j.  'daevi-  f.:  s.  unter  ^dtuva-.
•  j.  daevö.;qiit-  Adj.  'die  Vaiva  schlagend' : vaca  arJuxia  vär»%rayms  'ynita  (AP.) yasamaiäe  Vr.  20.  i ;  G.  2.  ö''.
^^»-ü■  Adj.  {S  1S3),  zum  V.  gan-.  —  PQ.:"dÄ talär.  -  ')  Hier  i,  %  363.  i.
•  j.  daevÖ.£idTa-  Adj.  {fem.  'rä-)  'von den  i^oArn  abstammend':  nase  datvT drvxs nate  're  (VSf.)  SrB.j.
Pü. :  äevan  iäxmai.
•  j.  daevö.)ata-
```


## [2026-09-05T17:40:21.110Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -oh \"\\\"ref\\\": \\\"BRT:[0-9]*\\\", \\\"status\\\": \\\"[a-z_]*\\\"\" page-*.json | sort | uniq -c | head -30"
}
```


### [2026-09-05T17:40:21.162Z] TOOL RESULT

```
      1 "ref": "BRT:345", "status": "supports"
```


## [2026-09-05T17:40:22.580Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json,glob\nfor f in sorted(glob.glob('page-10*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            for rc in n.get('ref_check',[]):\n                if rc['ref'].startswith('BRT'):\n                    print(f, rc['ref'], rc['status'], rc['note'][:300]); print()\n\" | head -60"
}
```


### [2026-09-05T17:40:24.442Z] TOOL RESULT

```
page-106.json BRT:598 supports AiW col. 598 s.v. čirya- ends '— np. čīra. — Pü.: čīr, čērīh' — Bartholomae himself makes the New Persian word the descendant.
```


## [2026-09-05T17:40:35.269Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^667$\\|  667  \\|667$\" BRT.txt | head -10; echo ===; awk 'BEGIN{RS=\"\\f\"} NR>=386 && NR<=388' BRT.txt | grep -n \"66[0-9]\" | head"
}
```


### [2026-09-05T17:40:36.771Z] TOOL RESULT

```
Exit code 1
27731:i667
(eval):1: == not found
```


## [2026-09-05T17:40:40.551Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 386 387 388 389 390 391 392 393; do echo \"--- leaf $n ---\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | grep -oE \"^[0-9]{3}$|dby  Google\" | head -5; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | grep -E \"^[0-9]{3}\" | head -4; done"
}
```


### [2026-09-05T17:40:42.580Z] TOOL RESULT

```
--- leaf 386 ---
dby  Google
666
666
--- leaf 387 ---
dby  Google
668
668
--- leaf 388 ---
dby  Google
669
670
669
670
--- leaf 389 ---
dby  Google
--- leaf 390 ---
dby  Google
673
674
671  daevayaz-  —  daes-  3  (
673
674
--- leaf 391 ---
dby  Google
676
208).  —  mp,  (Pü.)  dösastar;  s.  No.  I.  —  •»  Das
676
--- leaf 392 ---
dby  Google
677
678
677
678
--- leaf 393 ---
dby  Google
679
679
```


## [2026-09-05T17:40:45.048Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==387' BRT.txt | head -30"
}
```


### [2026-09-05T17:40:46.788Z] TOOL RESULT

```
  (sd.)  äatü  . .  ahuri>
asahya  axäyai  (sd.)  ggnedim  Y.  37, 17;  — aiäunqm  . .  uruns  .  .  kudüJiatanqmAt  .  . yailqm  vahehl^  'na  vanainti  va  vSnghm va  vaonarS  va  H.  3g.  z;  —  karapanS kavayasca  .  .  ySng  ^S  urva  ::^a!^a  xrao- dat  (sd.)  'na  Y.46.11;  —  Ö  dngvats *tnandaHg  *9r?tael  (sd.)  haihim  yehya urvü  xraodaiti , .  Y.  ji,  13;  —  tsm  *vä ahsm  dtTgvantS  .  .  'na  nailal  (sd.)  Y.^y/. so;  zT.  verwendet  V.f.  fia;  s.  a;  —  ySi .  .  aiäm>m  vandtn  (sd.)  . .  töi  daoiStig dqn  yS  drsgvats  °na  ",.  die  —  in  AnDaiva Haus  fUr  das  Ich  des  ^rv^enossen!"  Y. 4^.  4*>.  a)  im  jAiv.:  alaonqm ..  ahümla 'nam/ai*  iaooasäi  urvänsmca  fravaiSmia yagamaide  Y.  a6.  4;  —  asni  iyazamaide\ manä  . .  °nä  [yazamaidi]  saoryantqm  yaaa- vtaide  Yt  13.  7^;  —  aisS  zT  växs . .  a  va^S ahunB  vaityS . .  uruna^a  'tiaca  (IS.)  span- vanti  (sd.)  H.  J.  4;  —  'nqm  .  .  yaoldai- är/a  dha  zl  aifihä  asH  yaosdaitis  kahmai- Ht  ..  havaya  tnsvS  'naya  yl  hvqm  'nqm yaozdaite  humataisla  ..  V.  10.  19*';  —  um vä  ahOm  drvaniö  *^a  *'na  msirtnttyJJ [a/isiäi  a/fuhe]  V.  5. 6a;  —  aiiihä  dim vütaya  fr-Jmita  (sd.)  salayeiti  ya  hava 'naT>  kaininS  k>hrpa  srlrayh  .  .  aat  Alm aoxta  ..yS  nars  asaonü  urva  alca  Karditis ahi  ..?  äat  hl paiH.aoxta  ya  hava  'na  .. az?m  ba  U  ahmt  .  .  yä  hava  'na  *:^ai- paihejanvö  {sd.Y'  H.2.9— 11; — arahvam 'nqm  V.^.ai  PüZ.s),  io.  19  PüZ.
*)  Ein  tlieologiscb-philosophitcher  BegrilT,  die Geiammtbeit  der  leeliscben  und  religiüsen Eigenschaften  eines  Menschen,  seine  seelische und  religiöse  Individaalitit  Sie  lebt  nach  seinem Tod  als  selbständiges  Wesen  fort  -  Tgl.  zu  yj-o- vasay--,  um  schliesslich  den  Wiedererstandenen ~  oder  seine  Seele  ~,  nachdem  sie  ihm  -  oder seiner  Seele  -,  gewissermassen  als  Spiegelbild seines  Innern  als  schönes  oder  hässliches  Mäd- chen erschienen  war,  lu  Faradies  oder  Hölle  zu geleiten.  S.  lu  obigen  .Stellen  noch  Av.^.gfT., //, äff.,  Mx.  3.  las  ff-  167 ff-  —  **J  D.  h.  die D,  des  Saafyant  (Zar.)  wird  seiner  (des  Gläubigen) D,  dereinst  (nach  dem  Tod  bei  der  Himmels- reise)  wie  ein  Freund  beistehen;  vgl.   daiu  V.
tj.    9   und   IQ   djiqi:
KompE.  —  Et.?  Ob  gleich  'daenä-  (sd.)?  S. No.  I.  —  Pü.:  den;  s.  noch  No.  3,  5.  — >)  Wo  ae  im  Metrum  für  iwei  Silben  rechnet wie  bei  ^daeaS:  —  »  Vgl.  (lu  V.5/.  19,  SS-  S) Y.J/.ai.  — 1)  Pü.;  fl  rfmWä«;  vgl.  PüErl.  zu den  inY.j7.  aj.—  4)DasVerbum,  etwa  atih>n, ist  zu  ergänzen,  yä  drjgvalö  daenä  statt  aKyäi daenayäi  yä  dr'.  Eine  ganz  ähnliche  Ellipse zeigt  V.  4q.  5  d;  5.  Sp.  614  m.  mit  No.  4.  — 5)  Pu.:  den,  erl.i  kiimin;    s.  dazu  No.  7f.  —
dby  Google
66?
daenävazab-
'daeva- n
668
6)  An  der  Parallelsl.  V.j.zi  sieht  beidemale aii/ivqm  statl  datnqm ;  I.  No.  9.  — ■  7)  Statt dessen  steht  Av.  4.  18,  77.  13:  an  i  ^cs  dm u  {an  i  x"!!)  haiisn,  aber  Mx.  1.  laj  blos; an  i  ^eskuniin;  s,  No.  5,  8,  —  8)  Statt  dessen Av.  4.  34:  tuniin  i  tö,  r^.  14:  an  i  IS  kuniin i  vat,  Mx.  3.  130:  tuniht  >  Htvmt  i  Id,  171 : duiiuniin  i  tS;  vgl,  No,  5,  7.  —  «  Die  Glosse dazu  erlilärl  beide  WSrter  für  gleichbedeu- tend; s.  aJiküä-  No.  3.
•  j.  daenä'vazah-  m.  EN.  eines  Gläubigen : 'zanhs  asaonS  Yt  13. 117.
Eig.  'die  Religion  fördernd'.
•  j.  daenö.dia-  Adj.  'der  die  Religion lehrt,  in  ihr  unterweist':  sraohm  . .  ys 'disS  (NS.)"  *dagnayä  ¥.57,23.
Pü.  r  fa  den  nimülärVi.  —   ')  Them.
•  j,  daenö.sak-  Adj.  'der  sich  auf  die Religion  versteht,  darin  unterrichtet  ist'; •säcain  ..  asaonam  a^aoninqm  Yt/J,  155; —  *ratui.mirita  'säca  (IS.)  Y, /p.  17.
Zorn  V.  sah-.  —  Pü.:  i  din  ämSxt,  eil.:  ya!/ tart  isla.
•  j.  daeman-n.  1) 'Auge,  Augapfel';  mi^rd .  .  a%ra  naram  mi^rSJrujqm  .  .  *pairi 'ma  (AP.)  värayeiti  Yt  10. 4*8;  —  yat  .  . uB  pairtjäarayeifttH^ä)  °ma  (als  AD.)  . . pairi.urvaBayänti  Yt  14. 56.  a)  "Blick': irtra  datäiti  •mäna  (AP.?)'>  darätsüka dsi'iräiya  Yt  10. 107  (?).
KompE.  —  Zum  V.  'ääiyy,  —  np.  äim  'Ge- sicht', ftfy.  Umff  'PupUle%  —  <)  Dann  them.
•  j-,  g,  'daeva-  m.,  j.  'daevi-''  f.  I)  im gAw.*'  Bezeichnung  f�
```


## [2026-09-05T17:40:58.518Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دخش\" BQT_v2_pages.txt | head -20; echo \"=== v1 ===\"; grep -n \"دخش\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-05T17:40:58.581Z] TOOL RESULT

```
7742:‫دختر بپمن مادردار اب ناشلت و نام دخشس افراساب‬                ‫چهار منقو طه کنابه ازفلك کرسی‬
10081: ‫است از بدخشان که اسب خوب از آنجا آورند‬                     ‫ختار بفتح‌اوز بروزن قطار‪ .‬پاك کردن‬
10576:     ‫‪۰‬لم » سمدگان ‪ -‬ماوراءالنپر( بخارا ‪ ۰‬چاچ » طراز‬  ‫بدخشان ن‪۰‬رمن ‪ ۰‬چنانیان‪ .‬طخارستان سفلی خ‬
13160: ‫قسبه است ازتوابع‌بلخ و درسرحد بدخشان واقع‬
13605:                                                                                                               ‫بدخشان ‪.۷‬‬
17962: ‫دارد‪ -‬ونام‌ولاتی‌هم‌هت ازملك بدخشان که مردم‬                   ‫درون باشد » و بیخی است دوایی شبیه بعقرب‬
18053:  ‫میباید ووضع آلرا سببی درکاراست ‪ -‬و منوب‬           ‫وبدخشان ومرو است ؛ و بعضی گوبند دری زبان‬
22644:                              ‫فش (‪۵‬‬  ‫دخشر »‬‫‪ = ۵9‬در‬           ‫(‪« . 61 ۱6126‬لت نامه» ‪.‬‬
23755:  ‫از جملهةٌ آنار شیخ اشراق سهروردی »‬        ‫‪۴‬‬        ‫مصحف « دخش » («م‪. ).‬‬           ‫‪۴‬‬
24410: ‫و ببشتر مردم بدخشان و بعضی از مردم کشمیر‬           ‫انی ‪۰,‬‬   ‫سکون‬      ‫اول و‬   ‫ین‬   ‫‪ ۲‬ه‬     ‫رع‬    ‫*‬
34870: ‫درموضم بامیان ازمضافات‌ابل در سرحدبدخشان‬            ‫نا‪-‬م‬
37908:                              ‫سنك ب‬                                                  ‫است از بدخشان ‪٩‬‏ ‪.‬‬
=== v1 ===
872:و بدخشان است ودرعصر تسلط عرب وزمان ساسانیان۴ین ایالت از ساحل
3385:چند شهر بوده است که‌آن بلخ وبخارا وبدخشان ومروانت؛ و بعضی گوبند دری زبان اهل بهشت
7087:خصمت بود بجنگگ خف وتیفت ت آذدخش
11179:ایست از بدخشان . و درآن قصبه زبارنگاهیست
11301:دار بر وزن سحر میگفت » نام دخشی پرویزاست
14192:است از ولات بدخشان مایین هندوستانوغزلن -
17308:فوشت وسکون سین‌بی فطه وبای ابجده نم دخش
17912:وشن حردو نقطهدار مخفف بدخشان اسمت ورجون
17913:لمل از آنجا آرند لعل را نیز بدخش گویند»
17914:و بدخشانی و بدخشی را هم بدخش کوباد ۷
```


## [2026-09-05T17:40:59.835Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dašn\\|dasn\\b\\|dašina\\|dasina\" SNS_pages.txt SNS.txt BRT.txt PHD.txt NYB_vol2_glossary.txt 2>/dev/null | head -30"
}
```


### [2026-09-05T17:40:59.890Z] TOOL RESULT

```
SNS.txt:1752:. f/U £ .c*-lj o'j haxt 1 dasn: c^«»W 
SNS.txt:4155:dasn + arm 
SNS.txt:4159:.»j ,5^1/: arm I dasn: 'Cj.^-ji^ 
SNS.txt:6819:,f/n ** .c»-lj ^ : cairn I dasn*-" *^^ 
SNS.txt:17246:.(c^-ljc^-.) c^ljidasn: Itroj 
SNS.txt:17247:Ctfir. Man. 11,51) dsn : >;fc (AiWb. 703)dasina- : fc. 
SNS.txt:29586:dasina 316/18 
SNS.txt:32677:haxt i dasn 2/12 
SNS.txt:33107:dasn 316/17 
SNS.txt:33336:casra I dasn 93/17 
SNS.txt:33678:irra I dasn 44/2 
PHD.txt:310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
PHD.txt:1478:dagger čēlān, dašnag.
PHD.txt:2194:hand dast, panjag; (daevic) gaw; right ~ dašn.
PHD.txt:3450:right-hand dašnag.
PHD.txt:5321:dašn, jain dašnag, gišnag
NYB_vol2_glossary.txt:616:ärak ['k'; Prth STR’] side: ‘L LBR’ STR? outwards HajA:9 = 0 beh ärak, MPrth ^w byh rg (A-H III s. v. byh); tar matist — in the line of his maternal grandmother 3610-11; cas. obl. ~-éh: 6 dašn ārakēh + . . from Av. (193) arada-; MPrthPrs ?rg, ?rg.
NYB_vol2_glossary.txt:727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
NYB_vol2_glossary.txt:841:ayinaftan [’dynptn'] to reach, to get at, to touch: 6 mar gav ayinaft as for the scoundrel, (his) hands touched 61", with the gl. kū-š ēvak pat dit frac zat he clapped his hands together; 6¢ mar han i dašn gav 6 rān apar ayinaft as for the secundrel, (his) right hand got at his hip = the scoundrel put his right hand on his hip 61%; [yērtāt bē ahi/ayi/-naftak 4 angust but the corn had reached the height of 4 fingers PR 29° (written *hdynptk', a
NYB_vol2_glossary.txt:1044:burtan [bwltn'; YBLWN-, YDLWN-tn'; forms v. I, 178] bar-, to carry, to bring, to bear, to wear, to procure; to take away, to remove (6 or pat ‘to’); arišk ~ to bear envy 691. 8419; !a&, bes, dast, dašn, gobišn, nam, namāc, nipart, paitäk, srav, stēžak, vāng, pat xrat ~: v. these ws.; bahr ~ v. barišneh; — to place on the top of (apar) 444; to lay a p. on (6) 4720-21; — andar 6 tan ~ to bring into corporeal existence 92t; — andarg ~, v. göbisn; — apar ~ to send out against 3711; to bring 6016; dmdcisn apar ~ to give instruction, to teach 80%; v. also apar-barisneh and apar-burtäreh ; — frac ~ to bring, to present 411; to bring forth, to light (a fire) 44°; — fröt ~ to bring down, to shed (water) 417°; v. also fröt- barišneh; — 6 ham ~ to collect, to amass 4815; pret. construed as an act. 187% Common Iranian; Av. OP (933 sqq.) also — (act. and middle) ‘to ride’, cf barak and asvār; cf also apar-barišneh from bar- ‘to move’.
NYB_vol2_glossary.txt:1215:dašn [dšn'], attributive before its subst. dašnē 22%, right, right hand 48? and often; — engagement (by giving one’s right hand): ~ i x¥é§ ruvān burtan to pledge one’s own soul (by an oath) 2116-17 — Av. (703) dašina-; MPrthPrs
NYB_vol2_glossary.txt:1216:din; Ps. dšny. Arm lw. dašn ‘treaty, alliance’ (I do not accept the explanation by Bailey, BSOS VI, 1931, 600).
NYB_vol2_glossary.txt:1218:dašnak [dšnk'] the right wing of an army 11919,
NYB_vol2_glossary.txt:3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
NYB_vol2_glossary.txt:3649:kālpad i gētāhīk 8925-25, 9028-27; pat han + dašn pad frac škast trampled on it with his right foot and crushed it 5311-12; škast was broken, burst 542°; v. also s. v. stur. — Av. (1586 sq.) skand-; MPrs ‘Skn- (Sogd. 31%, 33. 59); Paz. škastan, seldom  škandan, škan-; NP  šikastan šikan-.
NYB_vol2_glossary.txt:5608:dstygyrd: Dast-kart dšn: dašn
NYB_vol2_glossary.txt:5933:dán: dašn
SNS_pages.txt:1008:                                                                     pas, *HR          >»                         f/U £ .c*-lj o'j haxt 1 dasn: c^«»W
SNS_pages.txt:2520:                                                                                                                                                                                                ,5^1/: arm             I dasn:    'Cj.^-ji^
SNS_pages.txt:2521:                                                                                                                                dasn + arm                                                .»j
```


## [2026-09-05T17:41:09.476Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dasina\" BRT.txt | head -10"
}
```


### [2026-09-05T17:41:09.523Z] TOOL RESULT

```
5463:•  j.  ara^ah-  n.  'Seite';  dasina  paiti  'lanha N.ÖJ.
13684:•  j.  duma-  m,  'Schwanz':  dasinam  . .  hao- yqm  Ml  (näml,  !BnS)  patöyam    upa.kprm-
14885:—  paoiryS  gairiS  AqtnJtisiat  .  .  'ti  äya z^mä  YX.ig.i;  /O.  98,  /J.97,  Y.9.IS.  V, 7,  54;  —  nasunqm  yä  'ti  aya  zimä  irJri- ^ar»  V.5. 4;  — '11  karJ*  pärst^  hyJ'  vtha- (id.)patiy3'^  . .  Bh.  J.  4;  2.  5  (ergänzt);  — tiyri/  ,  ,  afanvaia  'ti  niral  (Sp.  184  o.) Yt^.  38;  —  dasina  'ti  ahoanha  "auf  der rechten  Seile"  N.  65.  4)  mit  Abi.,  nur räumlich;  a)  auf  die  Frage  woher?:  mihr>m .  .  yS  vlspfm  aAsm  . ,  ädiiäiti  haraihyat 'ti  bar3tanhai  Ytio.  51.  b)  auf  die Frage  wo?:  dunmqn  hqmJiiitinli  *iisMndvat °ti  garsit  YtS.32;  —  yim  yazata  ahurS mazda  raoxinat  'ti  gara  nmana£  Yt /0. 1 2  3 ; 5.25,45.  s)  mit  Gen.,  nur  raumlich; a)  auf  die  Frage  woher?:  naKa  dunmqn (sd.)  uzjasaiti  Aaraihyd  'ti  iamayä  Yt 10.  50.  b)  auf  die  Frage  wo?r  ^dasimm J  va  gaonavatö  (sd.)  ^banstrvS  va  'ti vayhanaAe  N.  65;  —  zqm  .  .  yetiAa  'ti  . . apa  taünti  Yt  jj.  9  f. ;  i  o ;  — y^iihe  nmämm ..vüätfm  banzi'te  paiti  bar^aAi (Sp.Ba^ u.)  AaraiiyS  'tt  banxayä  Y. 57.21;  19;  — ys .  .  Aaomq  utdasta  .  .  kara^yS  'ti  bar»- '  xayä  Ytio.  90.  c)  auf  die  Frage  wo- hin?: aurvantim  %wä  .  .  bcrjS  nida'iat .  . Aarai^yS  'ti  banzaya  Y.SO.  10.  6)  mit Dat(?)"'',  räumlich  auf  die  Frage  wo?: tarn  yazata  auf  .  .  daAakS  bawrsii  'ti daiiihaove  Yt.  5.  29.  3)  zum  Ausdruck des  Gleichkoromens,  Aufwiegens;  mit  Akk. 'gleichwertig  mit  — ',  bei  Ellipse  des  Verbums {'ah-):  ha  ml  baya  .  .  satam  'ti  anyaisqm ra^wqm  gä^anqm  "dieses  Stück  .  .  wiegt hundert  andre,,  auf  Y./^.S"';  15.  A)bes. zur  Angabe  dessen,  was  als  Preis  oder  Lohn geboten  oder  verlangt  wird,  'gegen,  um, für';  i)  mit  Akk.:  uzbasaui  'ti  ammxtttn (sd.) /rarazaite  miirS  Yt  10. 1 24.  a)  mit Lok.:  yehyS  .  .  vaAistptn  yesng  'ti  vaidä (sd.)   mazda  Y,  57.  2a;   27.15,  Vr.  16I3;
21751:—  y  ^wä  didvaMsay'  manatjka y  * . .  a  ti ai^he  fraca  sfuye  . .  y  tl  atAhe  avä.vrü- raeha  Y.  /.  a  i ;  —  yeähi'^  *nitriiim  frära (Sp.  185  m.)  J  hl  *anisritim  [staryäti)  y 3at  hl  nSii  nisritlm  frära  nöif  . .  ästryeiti N.  10;  —  fravasayd  .  .  yä  akurake  .  . dasinam  upa  yüiöyeinii  y  alm  davaiii *aiavaxsnui  y  i'l  bavainti  anäiarfiä  .  . Yty.63;Ä'.43,  iO.  137.        b)  Imp.,  aS.;
```


## [2026-09-05T17:41:10.132Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دشن\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-05T17:41:10.183Z] TOOL RESULT

```
863:                      ‫بزد بر بر و سنهٌ شهربار‬                   ‫مکی‌دشنه بگرفت‌جانوسیار‬
8425:                             ‫نارادشنمه‬ ‫‪ ROC‬آر‬
10747:             ‫مررد ‪.‬‬    ‫خر دشنه را ودرع‬   ‫جوشن‬             ‫بامش چون نسج عنکبوت کند روی‬         ‫‪- ۴‬‬
14146:     ‫وزن ماهی خوار » دشنام شنونده کروابند ‪.‬‬                                                                                         ‫ری ‪. ۴‬‬
14147: ‫خواری گردن ‏ کنابه از دشنام‬                                 ‫جو ار رم » نام‌شهر ست‌معروف ومشپور‬
14155: ‫بائالی ممدو له بروزن عازه »‬    ‫حور از و ‌‬                                       ‫‪۰‬‬    ‫گویند ‪۹‬‬   ‫را‬    ‫دهنده‬   ‫دشنام‬             ‫‪4‬‬    ‫چارباره‬
14160: ‫پندیرا دکیوزیند اعم اآزنکه بجهت آبین بندی‬                  ‫دشنام‬       ‫و‬    ‫‪-‬‬       ‫باشد ‪۷‬‬   ‫دشنام دهی‬       ‫‪ ۰‬نمعتی‬               ‫وارداری‬
15228:‫را‬     ‫خو له * = بورزن موبه " پاروب‬                  ‫گوبند» ویشتراین لفظ را درمحل قدح ودشنام‬
16517: ‫ودعوی‌کازبرانیز گفته‌اند؟ ‪ -‬وبمعنی‌فحش ودشنام‬              ‫درخت فرو برند تا سیر شود‬                ‫که درآن شاخہای‬
17554:       ‫لرزان باشد ‪ -‬ویمعنی تابان هم هت ‪. ۸‬‬                ‫‪.‬‬      ‫ب)اشدشند‬
18299: ‫دشنام ‪ ۰‬دشمن ) ودو ا گاه) آمده‬                  ‫ِ دزخیم ‪a‬‏‬           ‫مر کب بل‬            ‫‪ ۰‬در کلمات‬       ‫‪020 -‬‬       ‫‏_‪ ۰ dur‬آرئی ‪2‬‬
19250:‫‪ ۰‬ودشنام‬         ‫دل» چه من بمحنی دل همآمده ست‬
19270:       ‫بوده ‪.‬‬      ‫‪:‬‬   ‫)ل( جك‬            ‫‪ :‬دشنام ‪۰‬‬      ‫‏)‪ (e‬چك‬             ‫‪۲‬‬   ‫‪ ۳‬دشسل‬        ‫‪ ۰‬چش‬    ‫)‪ (4‬چك‬
19276:  ‫‪ - ۴‬در اراک (سلطانآباد) ‪« 8۷500‬مکی‌نژاد» وکره‪ :‬دشپیل ‪.‬‬                                              ‫دشخو ار ‪۳‬‬           ‫دشنام‪.‬‬
19329:‫دشن د بنتح‌ارل وسکون ثالی ونون »‬                                             ‫سین بی‌نقطه وفتح فوقالی» بمعنی محوی باشد‪.‬‬
19369:       ‫است » وآنرا عمود صبح هم میگوبند ‪.‬‬        ‫‪ -‬بر وزن بلنگه ‪ .‬نامشپری‬           ‫دشن‬
19383: ‫لطيفك ‪ .‬شب را گویند و بعربی لیل خوالند ‪.‬‬       ‫دشنة صبح ‪ -‬کنابه از روشتی صبح‬
19395:                      ‫بتیز دشنه آز‬       ‫ا‪-‬بوالمظفر شاه چنایان که برد‬
19414:      ‫‪٣‬‏ دام(لفة ‪ :‬اسمبد) پ‬           ‫٭ دشنام ‪ -‬منم اول ‪ .‬از ‪ :‬دش ( = دبژد»)‬
19416:                        ‫سرزاش» طعنه‬     ‫این مرد ملك را دشنام داد و دازا گفت‪« ».‬کلتان ‪-۷‬‬
```


## [2026-09-05T17:41:14.983Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19300,19400p' BQT_v2_pages.txt; echo \"=== page tags near ===\"; awk 'NR<=19400 && /\\[pdf page/ {p=$0; l=NR} END{}' BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1<19400' | tail -5"
}
```


### [2026-09-05T17:41:16.600Z] TOOL RESULT

```
‫تن‬       ‫سوزن کشند‬          ‫که هر‬      ‫را گوند‬            ‫تایده‬    ‫رشته‬
                                                                                             ‫وبضم اول بمعنی بد وزشت بود ‪٩‬‏ ‪.‬‬
‫کسر‬       ‫اول و‬   ‫وسم‬       ‫را همکفته‌اند ؛‬           ‫خام‬    ‫و ربمان‬
                                                                             ‫تانی‬     ‫سکون‬   ‫بقتح اول و‬             ‫‪ ۴‬ت‌‬   ‫دشتان‬

‫نزرامده‬      ‫فارسی‬      ‫باکاف‬      ‫و‬   ‫‪:‬‬     ‫است‬      ‫هم درست‬       ‫اول‬
                                                                             ‫وفوقالی‌بالف کشیده وبنون زده‪ .‬حالض‌رامی‌گوبند‬
                                                                   ‫ان‬
                                                                                               ‫یعنی زیکه خون حیضش آید ‪۰‬‬
‫‪ ۰‬رسمان‬           ‫خشکی‬       ‫‪ ۰ ۸‬بر وزن‬               ‫دشکی‬
                                                                             ‫بضم اول بروزن بدتی » زلورا‬                        ‫دشتی‬
‫خامی که زتانر سند و مردوك مانند تنضه بنخده‬                                   ‫جون‬      ‫رنگه ‪,‬‬   ‫آن کرمی باشد سیاه‬                     ‫و‬   ‫گونند‬

‫وفرموله خوانند‪.‬‬              ‫ی‬    ‫وان بفه مانندرا دب‬                ‫شود‬      ‫بر عمنوی از اعنای آدمی بح یانند خون ازان‬
                                                                                                                                            ‫ا‬
          ‫باشد شبیه بماش وبعربی درجم خوانند ‪۶#.‬‬
                                                                                      ‫بمعنی بدباد لمودن وغیبت کردن ‪ ۴‬باشد ‪.‬‬
                                                      ‫‪۰‬‬    ‫ار ان است‬         ‫وواو‬     ‫شف‬   ‫با خای‬            ‫ار )‪۱‬‬             ‫دشخو‬



‫دشمیر "اه بروزن نقصیر» بمعتی‌قیض‬                                             ‫بروزن و معنی دشوار است که مشکل‬                          ‫‪۰‬‬    ‫معدوله‬


‫وعناصر اردمه راهم کفته‌اند که خاك‬                         ‫باشد ك‬   ‫و مد‬
                                                                                                                                          ‫باشد ‪.‬‬



‫دشن د بنتح‌ارل وسکون ثالی ونون »‬                                             ‫سین بی‌نقطه وفتح فوقالی» بمعنی محوی باشد‪.‬‬
                                                                                                         ‫‪۰‬‬    ‫ودبشستها به‌عتی محوسات‬


                                                             ‫باشد ‪۴3.‬‬

                                                                                                ‫(‪ )۱‬چش ‪ :‬دشتخوار ‪.‬‬
         ‫‪ - ۴‬اوستا ‪_itiavathsxad‬‏ ‪ .‬پپلوی ‪82111520‬‬                                         ‫در (بد) ‪.‬‬          ‫=‬     ‫رش‬     ‫=‬     ‫‪۱‬‬
 ‫از‪ :‬دشت ( = رش = رژ بد) ‪ ۳‬بار‬
                             ‫‪۴‬‬                                                    ‫هد« اسشق ‪. › ۰۲۷۵‬‬                 ‫( ارمنی ع ‪0۶‬‬
 ‫از ‪ :‬دش ( ‪ ۳‬دز » بد)‬                             ‫‪۵‬‬               ‫رکک‪ :‬شتها ‪ . ۱‬یور داود ص ‪- ۱۷‬‬                      ‫‪۴‬‬           ‫‪۰‬‬       ‫(‪.۵‬م‪).‬‬


     ‫‪۰‬‬    ‫م‪ . ( .‬ر که ‪ :‬اسشق وهوشمان ‪٩۹۵‬‏‬                          ‫دشوار )‬    ‫=‬        ‫‪ +‬خوار (ھ‪.‬م ) بهلوی ‪0 -_2-/۳3‬‬
     ‫یبر که ‪۲٩‬‏ وە‌ناس‪۲۷۲:۲‬؛ در اراک (سلطانآباد) ‪( ۲2201500‬مشکل) «مکیراد» ‪« :‬ملكرا‬
     ‫‪ 1‬کے اؤ دساتبر‬                          ‫ایرد سخن ( سخن شاکرد کشتی گیر) دشخوار آمد ‪« ».‬کلتان ‪٩4۹‬‏ ‪-‬‬
 ‫‪ ۷‬دراراکے ( ملطان آباد ) نخ خیاطی (لخ قرقره ) را‬                 ‫« فرهنك دساتبر ‪. ۵۸۲‬‬
                        ‫‪۰‬‬    ‫دعك‬     ‫دسك » دمه ‪.‬‬
                                       ‫رك‪:‬‬    ‫_‬ ‫کویند « مکی‌نژاد» » رک ‪:‬‬
                                                  ‫‪۸‬‬                                 ‫‪۵‬‬
   ‫برساخته دساشر «فرهنك دساتیر ‪ « ۵6۲‬فاب‪.> ۷1 :۱‬‬         ‫‪۴‬‬                                          ‫‪۰.‬‬       ‫دسصر‬   ‫رك‪:‬‬    ‫‪= ۹‬‬


                                              ‫‪ -۷‬امروز دشت (بفتح‌ارل) کویند ‪.‬‬
          ‫‏‬‫‪٩‬یر‪۲‬کف‬
                ‫‪ ۶#‬دده‌ن ‪ -‬ضم اول وفتح سوم » پهلری ‪ « 07-15۱0‬متاس ‪۷۲:۲۲٩‬‏ ‪#‬تب‬
     ‫«**‪.‬اورامان‬                 ‫از ارستا ‪ ° 2082170-1511‬بارتولمه ‪”eve‬‏ «نببرکه ابضا* » اورامانی ‪0‬‬
     ‫معرب دشمان «دزیج‬                   ‫‪:۲‬‬    ‫«لد‪ .‬ص‪۹۸‬‬                            ‫» فریز ندی » بر نی ونطنزی‬                ‫‏‪ ‘(TY‬گرا ‪5‬‬

                                                                                  ‫‪:‬‬    ‫ددوست‬
                                                                                           ‫* ص‬           ‫‪ :‬خصم » مضالف‬           ‫ص‪٩۳‬‏‬

                  ‫اوست ‪۰‬‬         ‫که دل هرد در صرف‬                                      ‫از خدا دان خلاف دشمن و دوست‬
         ‫«گلتان‪.۷4‬‬
         ‫شه در صفحه ‪۷۸‬‬
  ‫دشيدك‬                                                                                  ‫مس‬   ‫ل‬




       ‫است » وآنرا عمود صبح هم میگوبند ‪.‬‬        ‫‪ -‬بر وزن بلنگه ‪ .‬نامشپری‬           ‫دشن‬
                            ‫دشوار ‪۴‬‬             ‫باشد ازملك ختای ‪٩‬‏ ‪ -‬و غلاف خوشة خرما‪-‬‬
‫= باواوبروزن هشیار‪ .‬بمعثی‬                                                 ‫‪8‬‬
          ‫‪¥. a‬‬                ‫‪‎‬راوخشد | ‪E‬‬        ‫وشاخیکه خوشه برآن است‪ -‬وبندیکه (‪)۱‬پیش‬
                    ‫‪۴‬‬                                                                ‫ا بندند ‪.‬‬
                                                                                             ‫ب‬
 ‫ار‬    ‫بفتح کاف‬         ‫گر‬     ‫دشوار‬             ‫= بفتح اول وثالیبروزن‌پلنگی»‬            ‫دش‬
‫بمعنی کوه‬                   ‫وسکون رای قرشت‬                 ‫دلیاوروز گار وعالم سفلی ر! گوبند ‪.‬‬
                             ‫و کوهستان باشد ‪.‬‬                  ‫‪۱‬‬                     ‫‪:‬‬
                                  ‫‪۱‬‬             ‫ذشنه = بفتح اول بر وزن تشنه ‪ .‬نوعی‬
‫بنتح شین دویم بر وزن‬        ‫دشیشاث ‏‬               ‫رمردم لار میدارند ‪.‬‬
                                                                     ‫‪۴‬تکه‬
                                                                        ‫خزنجراستبش‬
                                                                                 ‫ا‬
 ‫لطيفك ‪ .‬شب را گویند و بعربی لیل خوالند ‪.‬‬       ‫دشنة صبح ‪ -‬کنابه از روشتی صبح‬




                                                                   ‫)‪ (۱‬چك‪-( :‬در ‪۰‬‬


  ‫‪ - ۱‬درحدود العالم و ءمجم البلدان نيامده‪ .‬شابد ممحف دشتك « ترجمة تاربخ بخارا ‪.‬‬
             ‫نرشخی چاپ مدرسص ‪ «+ 120115221 ۳۳۳۰‬بارتوی‪ .‬تکرتان ‪ .‬ص‪ ۰۱۱‬باشد‪.‬‬
      ‫وی سوال ‪.‬‬   ‫لکی‬
                    ‫کاد‬
                      ‫بتیز دشنه آز‬       ‫ا‪-‬بوالمظفر شاه چنایان که برد‬
  ‫منجيك ترمذی‪« .‬سروری* ‪.‬‬
   ‫‪ .‬ارمنی ع ‪ ۳2۷124‬از ‪( * ۲2۷01200‬مشکل ‪.‬سخت‬              ‫‪ - ۴‬پهاوی ‪51 - ۳۵۷‬‬
  ‫تزديك به« دشخوار ‪٩‬‏ ‪ .‬ابرائی باستانی _ ‪ , * 2727۷-11200‬ضد ‪_arÃVXx‬‏ از ‪uh ۵۲۵۷‬‏ ‪#‬‬
 ‫خوار کر= پتشخوار کره‬       ‫پشودارشکر‬
                                    ‫یبر گك ‪ ۲۸۰‬ورك ‪ :‬خوار» دذخوار ‪.‬‏ ‪ - ۴‬مخفف پد‬
=== page tags near ===
```


## [2026-09-05T17:41:29.487Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\\[pdf page\" BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3; grep -n \"\\[pdf page\" BQT_v2_pages.txt | tail -3"
}
```


### [2026-09-05T17:41:29.550Z] TOOL RESULT

```
0
```


## [2026-09-05T17:41:29.745Z] TOOL CALL #33: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py"
}
```


### [2026-09-05T17:41:29.783Z] TOOL RESULT

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


## [2026-09-05T17:41:36.533Z] TOOL CALL #34: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('SNS'),ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-05T17:41:38.544Z] TOOL RESULT

```
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
 "scans": [
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
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
```


## [2026-09-05T17:41:48.596Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint(\"leaves\",len(pages))\n# map line number -> leaf\nlines_per=[p.count('\\n')+1 for p in pages]\nimport bisect\ncum=[]\ns=0\nfor n in lines_per:\n    s+=n; cum.append(s)\nfor ln in [19329,19369,22644,23755,17554]:\n    i=bisect.bisect_left(cum,ln)\n    print(ln,\"-> leaf\",i,\"printed ~\",i+543)\nEOF"
}
```


### [2026-09-05T17:41:50.325Z] TOOL RESULT

```
leaves 684
19329 -> leaf 321 printed ~ 864
19369 -> leaf 322 printed ~ 865
22644 -> leaf 376 printed ~ 919
23755 -> leaf 396 printed ~ 939
17554 -> leaf 293 printed ~ 836
```


## [2026-09-05T17:41:54.952Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (282,283,284,285,286):\n    print(f\"===== leaf {i} (printed ~{i+543}) =====\")\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-05T17:41:56.479Z] TOOL RESULT

```
===== leaf 282 (printed ~825) =====
    ‫ح‬
    ‫ر‪۷‬‬                                                                                                                     ‫دأوری‬


‫يدام لصب کنند تاجانوران‬         ‫صادان درصحراتزدىك‬         ‫داور ی‪ = ۱‬بر وزن لاغری » جنگه‬
                  ‫دام آ بند ‪5‬‬   ‫رم کرده بجالب‬   ‫ازآن‬           ‫یت‬
                                                                ‫اغصه‬
                                                                   ‫کو‬‫شظلم‬
                                                                        ‫ونی ت‬
                                                                            ‫وخصومت باشد ‪ -‬و به‌ع‬
‫داهم ‪ < ۱‬بروزن‌کاظطم تاج پادشاهانرا‬                       ‫پیش کسی بردن‪ -‬ومحا کمه نمودن ویک وکردن‬
                                                                        ‫ميان نك وید همآمده اسن‬
‫گوبند وآلرا دبهیم نزخوانند ‪ -‬و تخت شاهی‬
                      ‫وجتر بادشاهی راهم گفته‌اند ‪2‬‬        ‫داو ناف ‪ ۳‬کهنابه ازناشتن نقشی‬
‫بمعنی‌داهل‬   ‫بروزن افول ‏‬         ‫‪۰‬‬   ‫داهول‬                                                                     ‫بمراد باشد ‪.‬‬
‫ات ‪. ۷‬وان علامتی باشد کهدهقانان بجهت‌دفع‬                  ‫‪۳‬‬    ‫کنر ك ویرستارباشد‬              ‫بروزن‌ماه‪.‬‬       ‫‪-‬‬         ‫داه‬

‫جانورانز بانکردرمیان زراعت نصب کنند وصیادان‬               ‫رایز‬    ‫ده‬   ‫وعشد‬       ‫وناکس را همگفته‌اند ‪-‬‬                     ‫مددل‬   ‫و‬


‫کبنرار دام‌سازند ‪ -‬و بمعنی تاج ءرصم هم‌بنظ‬                                   ‫ند که بعربی عشره خوانند ‪. ۴‬‬
                                       ‫آهده است ‪. ۸‬‬
                                                          ‫داها ‪ .‬بروژن باها ء یمعنی دره و عار‬

                                                                                                                     ‫کوه باشد ‪.‬‬
‫وميم » بمعنی دیهیم است که تاج مرصع باشد ‪.‬‬
                                                             ‫داهل ‪ - °‬نم ثالك بر وزن ک کل ‪.‬‬
 ‫دای ‪ -‬بروزن‌لای‪.‬هرچینه‌ورده‌ومرتبه‌را‬
                       ‫‪3‬‬    ‫از دبوارکلی ‪۰‬‬       ‫کون‬
                                                             ‫آزن برمند‬
                                                                     ‫کت بجپت دفم‌جانورآن زبانکار» تا ا‬
‫دابه شوهر بسر ‪ -‬کنابه از کره‬                               ‫وداخل زراعت تشوند ؛ وباین معنی بكر ثالث‬
                                                          ‫هم مده است ونیز(‪ )۱‬علامتی را (گ‪۲‬و)نند که‬

                                   
===== leaf 283 (printed ~826) =====
                                                  ‫بیان دویم‬

          ‫ودو لغت و کنات‬                ‫در دال بی‌نقطه بابای ابجد مشتمل بریست‬


‫=روزن چناله ‪ ۰‬بمعنی دبال‬
                       ‫د باله ‪ ۷‬ب‬                        ‫بفتح اول و سکون الی ‪ ۰‬بمعنی "‬                  ‫دب‬

                                 ‫است که تراج باشد ‪۰‬‬          ‫اسب را‬    ‫نگاهداشتن باشد ‪ -‬و بهندی جهاایدن‬
                                                             ‫کویند ‪ -‬ویابای فارسی دایره را نامند و بعربی‬
‫» وعظمت را‬             ‫مهتاب »ا وازه وشان وش و کت و‬          ‫دف خوانند دوف‌معربآست ‪ ۱‬ونم اول ‪۲‬‬
                                                             ‫در عربی خرس را کوبند‪ .‬اکر قدری از خون‬
‫د بدبه* ب«ابای ابجد بروزن دغدغه‪,‬‬                              ‫کی را ا یت ر‬
                                                                                                         ‫شود ‪.۴‬‬
‫بمعنی بزرکی واظهارجاه وعظمت باشد ‪ -‬وآواز‬
‫مشوال آنرا فر‬
            ‫اره‬
              ‫ودای دهل و قا‬
                          ‫عظیم ص‬                             ‫‪ - ۵‬بفتح اول والی‌مشدد بالف کشیده‪.‬‬
                                            ‫گونند ‪*٩.‬‏‬       ‫روایند ‪ ۴‬وبعربی‌قرع‌خوانشد ؛ وضم اول‬
                                                                                                ‫کدو ک‬
‫« بکسر اول وسکون ثالی وسین‬                  ‫بس‬
                                             ‫د‬                        ‫وبی‌تشدید ثالی هم بنظرآمده است ‪.‬‬
‫ديشت‬    ‫بی‌قطه » دوشاب خرما را گون که آتش‬
                                                             ‫داب ‪ -‬منم اول بروزنکلاب » نوعی‬
                                                                                          ‫ب‬
                       ‫باشد ‪ .‬گووبند عربی است ‪٩۱.‬‏‬           ‫ازریعان است © وافرا سوستی رگوند ‪ .‬و آن‬
 ‫د بستان ‪٣‬ے‏ بقتح اول بروزن شستان»‬                           ‫کرم وخشك است درسیم ‪ .‬فواق را نافع است ؛‬
                   ‫‪.‬‬    ‫ومکتب‌خانه راگوبند‬    ‫دبرستان‬                                     ‫وبفتح اول همگفته‌اند ‪:‬‬

‫» طفل‬    ‫شبتانی‬         ‫بروزن‬   ‫د بستا نی ‪۴‬ے‬             ‫دبال ‪ -‬بروزن وبال » میوه‌ابت که‬
                                ‫مکتب خانه را گویند ‪.‬‬                                             ‫آرا تنج گوبند ‪.‬‬


  ‫‪citrouille‬‬            ‫‪۴‬‏ =‬     ‫‪ -‬و دوم مشدد ‪ ۴ .‬رك ‪ :‬خرس ‪.‬‬                 ‫‪۳‬‬       ‫رک‪:‬دف»دب‌تان‪.‬‬       ‫‪۱‬‬


  ‫‪ :‬دباله ‪۰‬‬   ‫رك‬       ‫بت‬   ‫‪۹‬‬    
===== leaf 284 (printed ~827) =====
 ‫‪۷‬‬      ‫>‬                                                                                                                 ‫دق‬


‫ورن‬     ‫سر‬    ‫اول‬       ‫قح‬        ‫‪-‬‬        ‫سك‬    ‫دبو‬
                                                                   ‫وقاف »‬                ‫وکون‬
                                                                                            ‫دلق » بکراول س‬
‫خبازی‬   ‫نان کلاغ زا کو شت وبعربی‬                ‫‪.‬گل‬    ‫عرومك‬                             ‫اندام زرخك‬   ‫و‬   ‫برنگه‬     ‫است‬   ‫حمی‬
                                                                    ‫نرا دو رج‬        ‫و‬

                                                      ‫خوانند ‪.‬‬     ‫لعابیسفید‬         ‫عگلوىبندیسببآنکه چون ‪3‬‬
                                                                    ‫وحل‌زمانند عل ازدرون‌آن برآبد ‪.‬گرم وخشك‬
‫دلو سه د بفتح اول بر وزن سبوچه »‬
                                                                    ‫است دردویم» وجمیع ورمها رانافم است ‪ .‬گویند‬
‫پس کشتی‬             ‫ختاکنهۂ‬
                          ‫بمه‌نی آخر دبوس اس‬
                                                      ‫باشد ‪3.‬‬                                               ‫عربی است ‪١‬‏‬
                                                                    ‫دبوداد ه بنم اول وانی بواورسیده‬
 ‫بنتح اول وثانی بواو رسیده‬                 ‫د بو کی‬
‫که‬    ‫است ‪۷‬‬   ‫‪«.۰‬معمی دبومك‬            ‫بتحتانی کے ده‬        ‫وکاف‬
                                                                    ‫ودال ابجه بالف کشده وبرای‌فرشت زده " لوعی‬
‫کنلاغ باشد که بمربی خبازی خوانند ؛‬
                                 ‫گل نا‬                             ‫از ابهل است آونرا ویر هندی یگزوبند ؛‬
                                                                    ‫و بای حوف الی بای حطی هم بنظر آمده‬
‫ان نیاتی‬      ‫‪.‬و‬    ‫وبعضی گوبند دبو کی ينبرك است‬
                                                                                                                      ‫است‪:.‬‬
‫که آ فتاب رود‬          ‫طرف‬   ‫ھر‬       ‫جه‬   ‫باشف آفتاب درست‬

                                                                   ‫= بفتح اول بر وزن مجوی »‬                 ‫بوس‬
                                                                                                              ‫د‬
 ‫به‬
  ‫آن‌یات روی بجانبآفتاب دارد وبعربی مکلو‬
                                                      ‫خوالند ‪.‬‬
                                                                 
===== leaf 285 (printed ~828) =====
 ‫دحر‬                                                                                                  ‫‪۲‬‬     ‫ی‬


                                                 ‫ك لیس بروزن طبیب » هرچیزبکهآ ترا‬
‫دلیر فلكت هکنابه از کرکب عطارد‬                                                             ‫ارم کوفته باشاد ‪.‬‬
                                   ‫‪9 .‬‬   ‫ات‬             ‫‪۰‬‬        ‫‪‌ ۰‬‬       ‫ب‬
                                                      ‫برورن وزیر» مسشی‌وتوستده‬
                                                                                  ‫‪°‬‬
                                                                                           ‫=‬
                                                                                               ‫‪۱‬‬




‫ذلیقی » بروزن حقیقی » لوعی ازقماش‬
                    ‫ناشن درلپایت لطات ‪. ۴‬‬
                                                  ‫د لسر ستان؟ ‪ -‬بمعنی دبتان است که‬
                                                  ‫مکب خاله باشد ‪ - ۴‬و بعضی گویند دفترخانه‬


                                         ‫بیان سوم‬

                   ‫بر دو لفت‬      ‫مشتمل‬        ‫در دال بی نقطه ‪ ۲‬جم‬


‫د جر = بفتح اول و کر الی و سکون‬                   ‫کج ‪ -‬بضماول وسکون الی» هرجیز که‬
‫رای قرشت ‪ ۰‬غله‌است که برا لوینا گویند ‪.۷‬‬          ‫وامثال آن مالیده شده‬           ‫وعل‬       ‫وشر‬     ‫دوشاب‬   ‫درآن‬


‫استوآ بی که وبرا درآن‌پشته‬   ‫وآن سر د وخنك‬            ‫باشد و بر دست وپا بجسبد ‪ -‬ویفتح اول درءربی‬
       ‫باشند حیض براند ‪ ۰‬کوبند عربی است ‪۰‬‬                                      ‫مرغ صحرایی راکوبند ‪. ۵‬‬




  ‫‪ - ۱‬قی‪:‬یارسی باستان‪,‬کلمامتمار)_ ‪( 11‬خط)؛ پرا کرت ‪( 1۳11-* 1014 -‬کتیبه‬
  ‫های آشوک) ؛ پهلوی ‪hîrîp(i) ۰ ۲1۳140 . ۲۵۷1۳00‬‏ ‪ d‬و ‪ ۲1۱4‬ر(کدتیبه ها) ارمنیع‬
 ‫ور‪ :‬هویشمان ‪ * 04۵‬لیر کت ‪ ۵‬و ‪.۵‬دائرة لمعارف اسلام ‪ .‬راجم برمشة‬                        ‫‏‪ dpir‬مشق ‪۰‬‬
                        ‫از‪ :‬دس (ه‪.‬م‪٣ ).‬‏ ستان (يوندمكان) ‪:‬‬             ‫‪۲‬‬               ‫‪۰‬‬    ‫دییی‪.‬را*‪ :‬دسان‬


  ‫‪ - ۴‬دیبرستان کنم در هیکل روم کنم آبین مطران را مطرا ‪«.‬خاقالی شروانی ‪۲۲٩‬‏ ‪.‬‬
 ‫‪ ۴‬اصل این نوع پارچه از دبیق ( با دبقا بقول حمزة‌بن حن و قل ياقوت از او)‬
   ‫آمده است وآن شپری‌بوده است درعصر‪:‬هپی صندوق‌ها کبشرادند وخلمت‌ها برآوردند ‪ :‬جامهای‬
  ‫دوخته و نا دوخته » ورسول برپای خاست» وهفت دواج بیرون گرفتند یکی از آن سياه و دمکر‬
 ‫© = باین محتی‬     ‫دیقی های بفدادی بفات تادر ملکانه ‪« ».‬تاریج هقی ص‪ ۷4‬متن وحاشیه» ‪.‬‬
 ‫درعربی بافته‌نشد ؛مصحف ”رج ن
===== leaf 286 (printed ~829) =====
                                            ‫بیان جهارم‬



                      ‫* دځ بدفتح‌اول وسکون ثانی‪ .‬بمعنی | کشهراب انگوری باشد ‪.‬‬
‫انیت‬    ‫ع‬    ‫و‬     ‫ام ق‬           ‫دحتر‬              ‫خوب ولیکوباشد ‪ -‬وفوج صف را بیزکوبند ۔‬
 ‫وسره وخلاصة هرچیزهم‌هست ‪ -‬وضم اول بمعنی | که‌کنایه از شراب لمل باشد ‪ - ۵9‬و بمعنی‬
 ‫انگور ودانه انگورهم آمفه است که بعربی علب‬         ‫گاهی را‬        ‫دختر باشد ‪۴‬‬        ‫است که مخقف‬         ‫دخت‬

                             ‫| خواشد ‪.‬‬       ‫ر‬  ‫یآن‬  ‫صاز‬   ‫حد و‬ ‫نیز گویند که درمیان اب روی‬
 ‫د ختر رور گار ‪ -‬کنابه از حوارت‬        ‫ه‬ ‫ز‬ ‫ب‬ ‫ر‬ ‫خ‬ ‫ن‬ ‫ا‬ ‫د‬ ‫ب‬ ‫و‬ ‫د‬ ‫ن‬ ‫ی‬ ‫بافند آونرا درخراسان اوخ کو‬
                                 ‫کزار است ‪.‬‬
                                          ‫| رو‬        ‫آرنگه کنند؟ ‪-‬وبه‌منی لیبو باهم! مده‌است ‪/‬‬
‫بارت‬    ‫بتکده ‪.‬‬    ‫» بر وزن‬
                                     ‫‪۱‬‬
                               ‫دختره ‏‬
                                                     ‫وتهیررآسمانی س زراا نسزر کدوونند که تءنرششپیاابین ‪,‬باشد ‪.‬‬
                                                             ‫کر‬          ‫‪۱‬‬                   ‫ج‬
                                                    ‫= هم اول وسکون ثالی ونای‬                 ‫د حت‬
‫ودخت رکی ودوشیز گی باشلب ومهر برا نیزکوبند‬
                         ‫که بر که لهند ‪. ۷‬‬                             ‫قرشت » مخقف دختر است ‪#*.‬‬

 ‫ینری ‪٬‬بمعنی‏‬ ‫دختری ^ گبر‬
            ‫لوز‬                                    ‫از شراب لملی‬           ‫ااببه‬
                                                                              ‫کنفت‬
                                                                                 ‫‪-‬تر‬
                                                                                   ‫دخ‬
         ‫دختره باشد که دوشیز کی وبکارت است‬                                                              ‫باشف‬


 ‫جمی = بروزن خفتن» مخفف دوختن‬                       ‫دحتر حم = بمعنی دخترافتاب است‬

   ‫متعافب همی رسد دخ دخ ‪ ۰‬تزاریةپستانی ‪«.‬جهانگیری»‪.‬‬              ‫‪ - 0‬همچو امواج بحر لشکر شاه‬
                              ‫مصحف «رخ» ‏ روخ ‪.‬‬       ‫‪۴‬‬            ‫رك‪ :‬دخت ؛دختر ‪.‬‬             ‫‪۴‬‬
                                          ‫‪ - ۴‬بپلوی ‪txud‬‏ نیم رگ ‪ ۰۶‬ورك‪ :‬دختر ‪.‬‬
        ‫که دم وحمت ماکرد ز بند آزادت ‪.‬‬              ‫® ‪ -‬برسان بندگی دختر رز کو بدرآی‬
  ‫«حافط شبرازی ‪۵۱٩‬‏ ‪.‬‬
  ‫‪ - ۷‬امروز دختره ( از‪:‬‬                  ‫‪- ۱‬
```


## [2026-09-05T17:42:03.272Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (287,288):\n    print(f\"===== leaf {i} (printed ~{i+543}) =====\")\n    print(t[i][:3000])\nEOF"
}
```


### [2026-09-05T17:42:04.866Z] TOOL RESULT

```
===== leaf 287 (printed ~830) =====
  ‫دخمه فروژه‬                                                                                         ‫‪۲۲۴‬‬


‫کتدااوروآغمازعامله بکیا‌باشد و‪-‬تبره وتازيك‬
                                         ‫اب‬                 ‫باشد ‪-‬وبمعنیاندوختن‌وجمم کردن‌هم‌هست ‪۴‬‬
                                        ‫را نیز گفته‌اند ‪۰‬‬                        ‫ودوشیدن‌را نکیوزبند ‪. ۱‬‬
‫دحم ‪ ۹‬بروزن زخم ‪ ۰‬سردابه‌ای که‬                              ‫دخقنكد ‪ ۴‬ه بروزن سوزنگر» دختر‬
                               ‫لهمل‪.‬‬         ‫مرده را دران‬   ‫ودختر زان آزشوهر‬      ‫شوهر باشد از زنی دیگر‬
                                                                                                       ‫وگ‬
 ‫د حمه = بروزن زخمه» بمعنی‌دخم‌است‬
‫که صردابة مر د گان‌باشد؛وصندوق‌موتی را گویند‬
                                                            ‫دخقه ‪ ۴‬ه بروزن کفته‪ .‬مخف دوخته‬

 ‫عموماً وکورخالاً کبرانرا خصوصاً ‪ -۷‬وآن‌چیز‬                 ‫است که خیاطت کرده‌شده باشد‪ -‬وبه‌عنی دوشنده‬
                                                                                                 ‫هما مده ار‬


            ‫میا ورد و آیرا بعر بی شعععه خوانند ‪۰‬‬            ‫دخدار » بفتح اول و دال بی‌نقطه بر‬
 ‫دخمه راندیان س کنابه آاسزمان‬                               ‫وزن دستار» چادرسیاه وسفیدبرا گویند که برروی‬
                        ‫‪۰‬‬      ‫‪.‬و‬   ‫ه‬    ‫‪۵‬‬     ‫‪۰‬‬



                                                     ‫ا‬
                                                            ‫تخت پوشند ؛ وبعضی گویند معرب تخت داراست‬
                                                                                ‫که جام خواب باشد ‪.‬‬
                            ‫ات که آسمان باشد ‪.‬‬              ‫‪ = °‬بقتح اول بروزن رخش ‪۰‬‬             ‫دحش‬




  ‫از‪ :‬وخت ‪+‬‬       ‫‪۴‬‬            ‫» دوختن‪.‬‬            ‫و‪:‬ختن‬
                                                       ‫دکه‬
                                                         ‫ال ر‬
                                                            ‫‪۴‬‬             ‫‪.‬‬    ‫دوخئن‬   ‫رکه‬   ‫=‬   ‫‪۱‬‬

                                                            ‫اندر ) فظدر يسرأندرء پدراندر و مادراندر ) ‪:‬‬


       ‫ن بدارا ‪.‬‬
               ‫تچو‬
                 ‫خهم‬
                   ‫درد‬
                     ‫با پسندر کینه دا‬                         ‫جز بمادندر نماند این جهان گړبه روی‬
  ‫رود کی‌سمرقندی( تصحیحعلامهدهشدا) ‪.‬‬
  ‫© ‪ -‬رکه‪ :‬اسشق وهوبشمان ‪.4۲۵‬بهلوی‬         ‫‪ - ۴‬اسم مفعول از «دختن» (هم‪. ).‬‬
 ‫‪( 11520‬شفل‪,‬تکلیف) قی‪:‬ارستا هتکن (آلت‪,‬ایزار) «بارتولمه‪»٩۷۷‬‏ وممکن است از‬
             ‫‪( 01:2‬شان ‪ ,‬علامت) «بارتولمه ‪۹۷٩‬‏ مشتق باشد « نریبکه ‪٩4۰‬‏ ‪.‬‬ ‫اوستا ‪2‬شا‬
  ‫‪۰07۳1۵0‬‬                   ‫‪ - ۷‬اوستا‪amxad -‬‏ ؛ پهلوی‬                     ‫‪ - ۱‬رکه‪ :‬دخمه ‪.‬‬
  ‫م دخمة اوستابی بمعنی دافگاه است سنی محل یکه مردگان را‌وزانند» چهرة‬                              ‫«اسشق ‪۳‬‬
  ‫این‌کلمه که ‪ 821‬باشد بمعنی سوزانبدن است وکلمة داغ فارسی از همین ماده است ‪ .‬ا
===== leaf 288 (printed ~831) =====
                                                       ‫يان بنحم‬

                    ‫بر دو لفت‬              ‫در دال بی‌نقطه بادال بی‌نقطه عفر‬



‫رانز گوند‪.‬‬      ‫وفلندر‬    ‫‪_۴‬‬       ‫جانوران‌درنده‌باشد‬   ‫که‬       ‫که جانور ان در نده باشدهمجو شبر و پلنگه‬         ‫گونند‬



‫وگ رکه ومانندآن ‪ - ۱‬ویبابان پرازشکار را نیز | ودرتر ککنیيزك را نیز کوبند که فرزندان کلان‬




   ‫در دال بی‌نقطه با رای بی‌نقطه مشتمل بریکصد ونود وپنج لفت و کنایت‬


 ‫مشمه ل بر صف‬      ‫هصست‬   ‫رردشت‬       ‫کتابی دراحکام ددن‬           ‫ثالی ‪ ۰‬در خانه‬   ‫»‪ -‬بفتح اول کون‬       ‫در‬



  ‫وسرای وامثال آن باشد وبعربی باب کویند ‪ ۴‬۔ | باب وآنرا «صد در نام‌نپاد‌اند ‪ -‬ونوع و جنس‬
 ‫ودره کوهرایز گفته‌الد‪ - 6‬وبمعتی کرت ومرتبه | را نیز گویند ‪ - ۷‬و بمعنی دربدن و پاره پاره‬
 ‫امر بر باره کردن هم‬           ‫و‬       ‫باشف‬    ‫کردن هم‬            ‫چنانکه‬    ‫‪ -‬وبایی که در کتابهامنوی ند‬          ‫همهت‬



    ‫‪ - ۱‬اوستا ‪( 2610124 -‬جانور وحشی)‪.‬پهلوی ‪.tad 64024 610۵1۰‬‏ «اسشقع‪4‬ه»‬
   ‫و گفت ‪ :‬مرا تشجیران و ددان بحکم اعتمادی‬                      ‫«رویاه بر حمدو له لام گفت ‪e‬‏‬        ‫«مناس ‪YT‬‏‬

   ‫ی‬    ‫‪5:۳‬‬   ‫ور‬    ‫ر کث‪ :‬دده‬        ‫رک‬            ‫‪۰‬‬    ‫‪۷:۰‬‬   ‫سند بادناه‬   ‫نزدىك تر فرستاده‌اند‪».‬‬   ‫وسفارت‬       ‫برمات‬



        ‫بی‬
         ‫اكك‬
           ‫نیز‬
             ‫غ کن‬
                ‫جشی‪.‬‬
                   ‫مرعکنیی‌جد پدری‌با مادری»خال (دائی) پبر» حبران وح‬
                                                                   ‫‪ - ۴‬دبرت‬
    ‫‪ - ۴‬پارسی باستان_ ‪( ۲3۷10‬در ‪.‬باب)‪ .‬اوستا‪ ۰ ۲2۷1 -‬پهلوی‬                                  ‫ور که ‪ :‬دادا ‪.‬‬         ‫‪۸‬‬
       ‫‪ ۳‬هندی باتان ‪ , 94۳1۷ ۰ ۲2۷‬ارمنی ‪( ۳۳1۱‬باب‪ .‬در) ‏ کردی ‪)red. ۲۵‬‏ „(‪îrad‬‬
       ‫افغانی ‪ ۰ ۲۵۷‬استی ‪. ۲2۷0‬وخی ‪۲20۰‬سر بکلی]‪ . 1۷11‬شفنی ‪ , ۲6۷۱. ۵۷14‬منجی ‪27021‬‬
   ‫سمنالی ولاسکردی ‪rab‬‏ «‬                  ‫‪ 3‬بارتولمه‪ ۷۰۲23۷0۰ ۹۹‬لیر گے بر‪ 3 » 6‬منای ‪۱‬‬                ‫»‪ 2‬اسشق ‪6 0‬‬
       ‫فنردییز‌ونطنزی ‪ ۳30‬برنی ‪٣‬ق‏‪0‬‬                     ‫‪.۲‬‬‫‪“3‬‏‬
                                                            ‫یص‪٩۹۸۱‬‬
                                                                 ‫ککے‪).‬‬
                                                                     ‫ل‪1‬ء‬
                                                                       ‫ک‌بی ‪3‬‬
                                                                            ‫شهمیرزادی ‪ . 81‬سرخه‬
                                                                                             ‫دک ‪۱ .‬ص‪٩ ۲٩۰۹‬‏ ‪:‬‬

                    ‫بی وسیلت گرد پیرامن ‪.‬‬                                  ‫درمیر و وزبر و سلطان را‬
       ‫هکلتان ‪. ۹۳۰‬‬
       ‫یز ‪ ۲۵34‬دربهلوی بهمتی باب و فصل کتاب آمده‌منای‬                      ‫‪٦‬‏‬          ‫رکه‪ :‬دره ‪۰‬‬     ‫‪- ۵‬‬

                     ‫‪ - ۷‬ه پنشتم و از هردری سخن در پیوستم ‪« ».‬کلتان*‪. 4‬‬                                      ‫‪.‬‬      ‫‪۱‬‬
```


## [2026-09-05T17:42:37.746Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef toen(s): return ''.join(str(fa.index(c)) if c in fa else c for c in s)\nfor i in range(283,295):\n    head=t[i][:300]\n    nums=re.findall(r'[۰-۹]{3,4}',head)\n    print(i, i+543, [toen(n) for n in nums])\nEOF"
}
```


### [2026-09-05T17:42:39.701Z] TOOL RESULT

```
283 826 []
284 827 []
285 828 []
286 829 []
287 830 ['224']
288 831 []
289 832 []
290 833 []
291 834 []
292 835 []
293 836 []
294 837 []
```


## [2026-09-05T17:42:49.115Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nprint(t[287])\n\" | sed -n '25,80p'"
}
```


## [2026-09-05T17:42:50.139Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"daxšak\\|daxsak\\|dax.ak\" NYB_vol2_glossary.txt | head; echo \"=== HUB 245 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==255' HUB.txt | head -60"
}
```


### [2026-09-05T17:42:50.981Z] TOOL RESULT

```
                                                            ‫تخت پوشند ؛ وبعضی گویند معرب تخت داراست‬
                                                                                ‫که جام خواب باشد ‪.‬‬
                            ‫ات که آسمان باشد ‪.‬‬              ‫‪ = °‬بقتح اول بروزن رخش ‪۰‬‬             ‫دحش‬




  ‫از‪ :‬وخت ‪+‬‬       ‫‪۴‬‬            ‫» دوختن‪.‬‬            ‫و‪:‬ختن‬
                                                       ‫دکه‬
                                                         ‫ال ر‬
                                                            ‫‪۴‬‬             ‫‪.‬‬    ‫دوخئن‬   ‫رکه‬   ‫=‬   ‫‪۱‬‬

                                                            ‫اندر ) فظدر يسرأندرء پدراندر و مادراندر ) ‪:‬‬


       ‫ن بدارا ‪.‬‬
               ‫تچو‬
                 ‫خهم‬
                   ‫درد‬
                     ‫با پسندر کینه دا‬                         ‫جز بمادندر نماند این جهان گړبه روی‬
  ‫رود کی‌سمرقندی( تصحیحعلامهدهشدا) ‪.‬‬
  ‫© ‪ -‬رکه‪ :‬اسشق وهوبشمان ‪.4۲۵‬بهلوی‬         ‫‪ - ۴‬اسم مفعول از «دختن» (هم‪. ).‬‬
 ‫‪( 11520‬شفل‪,‬تکلیف) قی‪:‬ارستا هتکن (آلت‪,‬ایزار) «بارتولمه‪»٩۷۷‬‏ وممکن است از‬
             ‫‪( 01:2‬شان ‪ ,‬علامت) «بارتولمه ‪۹۷٩‬‏ مشتق باشد « نریبکه ‪٩4۰‬‏ ‪.‬‬ ‫اوستا ‪2‬شا‬
  ‫‪۰07۳1۵0‬‬                   ‫‪ - ۷‬اوستا‪amxad -‬‏ ؛ پهلوی‬                     ‫‪ - ۱‬رکه‪ :‬دخمه ‪.‬‬
  ‫م دخمة اوستابی بمعنی دافگاه است سنی محل یکه مردگان را‌وزانند» چهرة‬                              ‫«اسشق ‪۳‬‬
  ‫این‌کلمه که ‪ 821‬باشد بمعنی سوزانبدن است وکلمة داغ فارسی از همین ماده است ‪ .‬ازخوداوستا‬
  ‫هم مفهوم میشود که در قدم ابراننان لاشة مرد گان را می‌سوزآنیده| ندودر رندیداد از جرم‌سوختن‬
                  ‫اص ‪ ۵۰۵‬راجم بدخمة پارسیان'ر که‪:‬‬                 ‫لاشه در آش سخن رانده شده ‪ .‬بشت‬

            ‫‪J.M. Unvala, Report on the Dakhmas‬‬                                  ‫‏‪of Tena, Bombay‬‬
  ‫‪1951; ibid, Preliminary Report‬‬                            ‫‪on an Old Dakhma of Yazd,‬‬
 ‫‪Reprinted.‬‬         ‫‪Sanj Vartaman‬‬                    ‫‪Pateti Annual‬‬       ‫‪1951.‬‬
```


### [2026-09-05T17:42:52.638Z] TOOL RESULT

```
1246:daxšak [dhšk'] sign, mark, token 488. 517-18; hac ~ bé histan to disregard 94. — Av. (676) daxsära-, daxšta, ci also (ibd.) daxša- ‘burning’; Sogd. 48.49. Paz. dasa (Mx), dašaa (SGV).
2006:2323; to omit, to neglect 33%. 66°, v. also s. v. daxšak; to dismiss 1094. — 2. to let loose: asp ~ to drive a horse to- wards (6) 11%, frāc along 262°. 278-34, 299.19; — to pour out on, in 95". 10121, 10273; to infuse 104? (andar). — 3. to allow to go off, to send forth 271%, to allow to enter (6) 3425. 351, 8414; to ad- mit 1818 (andar 6 peš). 1819 (6 peš); — to allow, to permit 1091? (kas virtual dat.); with an inf. 43-4; with a subordinate clause introduced by tāt 27%; — to hand over to (pat) 2972. — NB. In am be nē
2761:nīšān [nyš'n'] sign, omen, portent 487, gl. by daxšak + anak; pl. —-iha 11018. — MPrthPrs nys’n; NP nišan.
2860:-p, -pi [-py] (Prth) emphasizing part.: LHw-p = hē-p to him HajA:14; "MT- S-p = kaš-ip, v. "kaš; apar-p-im ravišn I must climb up 40%; (ZK-p =) an-ip tē armēšt daxšak-ip früc venend 5113-14 (v.s. v. an and tē); ZK-py 51: as -p(?) is purely Prth we have to assume the Prth. equivalent of ZK: et-- p? (Henning,
5117:daxšāra-, daxSta: daxšak
6530:d(a)rog: drog darma(n): darman daru: darok daruand, darvand: druvand daruandi: druvandéh daryäv: drayäp daryös: drigūš dasti: apastčh dastur: dastavar daša(a): daxšak dašt: daštan, dar-: dawar: davr davar: dätavar deh: déh
=== HUB 245 ===
— 244 —
62, pustikpanaklh 'Schutz' Phi. Min. p. 46, Z. 14, np. ptisH-
pan (Vullers Wb. I, p. 365); Anus er van =^ ^hl, ondsakruv^n,
i^eiz, Anosrua^i; Azarmiduxt (Sebeos) = phi. *^^(irw?A;f/Ma?^,
np. Azarmiduxt \ eritasard 'Jiingling = phi. *re^ai:sard (phi.
rmak a youth' PPGl. 197, 'foetus Bdh. Gl. 162, paz. np.
rEdak *Kind' +sard = zd. sareda- *Jahr), wo k auch im
Paz. und Np. (vgl. paz. madavar = phi. matakvar Shk. 257 ;
np. bandwan = phi. *bandtkpan, etc.) geschwunden war.
Der Schwund des k geht also hier in das 5. Jhd. oder in
altere Zeit zuriick.
Dagegen blieb k in neu gebildeten Kompositis: arm.
hamakden (EliSe 112) *die ganze Religion kennend' = phi.
*hamakden, vgl. unkomponirt: phi. hamdk den *the whole
religious ritual' West, PT. I, 383; xostakdar *Erbe* = phi,
x^astakdar (oben p. 56).
Die Syrer haben (wie die Mandaer, vgl. N old eke,
Mand. Gram. Einl. p. 13) in ihren pers. Lelmwortern -p und
*; fiir phi. -A:, jenes in alteren, dieses in jungeren Lehn-
wSrtern, die von ihnen meist entlehnenden Araber^) ent-
sprechend q und / (fiir g).
Wann ist ausl. ak im Persischen zu a geworden?
Ueber die Entwickelung der A-Suffixe im Ossetischen
{ag, ag, ug, ig, tg) siehe Verf. ZDMG. 41, 326 flg. , im
Afghanischen {k, g, ka^ ga etc.) Geiger, Etym. und Lautl.
p. 46; im BaludT {ag-^ ok, uk\ ig, deminut. i, ik, uk) Geiger,
Lautlehre p. 25.
§ 137. In den folgenden Fallen ist suffixales k im
Auslaut weder zu g geworden noch geschwunden, sondem
als k geblieben :
a) im deminutiven Suffix 2) ak, das wohl jungeren
Ursprungs als das allgemeine Pehlevisuffix ak = np. a ist :
mardak 'Mannlein* von mard *Mann', andak wenig' von and
'soviel* etc. (Vullers, Gram. p. 233). Dazu auch juftak
Inseparaber, eigentl. *Parchen , vgl. arm. juxtak ein Paar
*) Z. B. zibaq 'Queoksilber', arm. zibak (geschrieben zipah\ syr.
pD^T (Brockelraann p. 90), ;ii^7 (de Lagarde) = np. ziva — phi.
*zivak,
*) Vgl. bal. -/A;, uk (mit k) als Deminutivsuffix.
```


## [2026-09-05T17:43:06.214Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"daxs\\|dax§\\|daxš\" HUB.txt | head -20; echo \"=== HRN ===\"; grep -n \"daxs\\|dax§\" HRN.txt | head -20"
}
```


### [2026-09-05T17:43:06.272Z] TOOL RESULT

```
8327:daxstavaiti' ; xusnild zufrieden' = zd. "^huxsnuta- H. 509,
8334:raoxsna-- glanzend'; vaxsur 'Prophet' H. 1076; daxs 'Ge-
8394:dastan, zd. daxsta- ^Menstruation' ; hast Versohnt', np. asti
=== HRN ===
10313:da/sakömund; vergl. pes\(la/ßakih^ y^y^-daxsahlh (vd. 18
```


## [2026-09-05T17:43:07.146Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"daxs\\|daxš\" CHEUNG.txt | head -20; echo \"=== SYN 1227 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1251' SYN.txt | head -50"
}
```


### [2026-09-05T17:43:09.229Z] TOOL RESULT

```
4580:*NEIR: Sariq. óizd/óiz- ‘to be ill’, Yghn. (impers.) daxs(-)/daxsta ‘it hurts’ || (+ 
5567:*daxš ‘to show, teach, reveal, mark’ 
5569:*AVESTAN: daxs- ‘to instruct, show’, daxsta- (orig. ppp., n.) ‘sign, revelation [BMP 
5570:/daxsag/]; menstruation [= BMP /dastan/]’ (Y 34.6, Y 51.9, V, etc.), ? OAv. daxsära- 
5576:Pres. {1} them.: INJ. 3sg. OAv. daxsat (Y 43.15); Pres. {2} aia-: OPT. med. 3sg. YAv. aóaxsaiiaeta (Y 
5577:12.5), IMPV. 25р. OAv. «fra»daxsaiia (Y 33.13) 
5579:*MIDDLE PERSIAN: MMP dxsg, ВМР dhsk /daxsag/ ‘sign, mark, characteristic; 
5583:*NEIR: NP dastan ‘a menstruating woman’, ? NP daxs ‘start, commencement of 
5584:work; dark and gloomy’. Ф The meaning, “Geschäft, Mühe’ assigned to NP daxs by 
5587:Dehkhoda, s.v.): 1. "It is the commencement of work. One says, ће daxs is to you, it 
5592:work’ may be connected to MP /daxsag/, the meaning deriving from ‘start-sign’, 
5593:whereas daxs ‘dark and gloomy’ is perhaps related to *daj, from *'burnt, charred’ ? 
5595:pretation of the Avestan daxs- forms. Although there is general agreement on the 
5598:daxs- has secondarily developed from the past participle of the root daés- ‘to show’ 
5604:(dais'), with *dixsta- > daxsta-. However, Schlerath 1962: 514 points out that this 
5607:Gathas: daxsat. Humbach 1959 II: 52 (repeated Humbach 1990 II: 144) equates 
5608:OAv. daxsat with Skt. daks ‘to make right, be able [vel sim.]’: "macht es ... recht". 
5613:to Av. daxs- is disputed by Rieken 1999: 210 f., who rather relates Hitt. /tekkuss-/ to 
24432:radaxsun/redaxst ‘to climb (a mountain)’ (< *to reach for the top’) || (+ *ham-) 
24725:ill’ (contaminated with inch. *daxsa- < *daj ?), Yzgh. tifs-/tüvd ‘to be (over)heated’, 
=== SYN 1227 ===
 etym. much disputed, but OLG i. ‘refuge’ fr. ‘place one ine OE hoppian ‘spring, hop’. Nord. Tidsskrift 8 (1919), -H. 1.877f. Otherwise
perh. springs g JesperseDs 151 f. Weigand
365 f. ee aig MHG gedinge (both
6 ‘agreement’ ) with vbs. OHG (ge)- dingen, MUG (ge)dingen, not to be sepa- rated (as Walde-P. 1.705) fr. OHG din- an ‘negotiate, come to terms , etc. (NHG dingen ‘bargain’) : OE pingian ‘plead, make terms’, etc. (Walde-P. 1.725). Development through ‘agree- ment, promise’ (attested for OHG, MHG forms) to ‘expectation’ and ‘hope’.
5. Lith. viltis, beside vb. vilti-s : pa- yelli ‘wish, permit’, Lat. velle ‘will’, etc. (16.61). Walde-P. 1.294. Trautmann 348.
Lett. certba fr. cerét ‘guess, suppose,
Digitized by Arya Samaj Foundation Chennai and eGangotri
hope, think about, love’, prob. deriv. of ceras ‘devotion, reverence, ardor’, also coll. ‘hopes’, perh. : MHG, NHG harren ‘wait, award, tarry’. Walde-P. 1.411. Otherwise Mihl.-Endz. 1.374.
6. ChSl. uptivanize (with modern Slavic words for ‘expectation, hope, trust’, etc., as SCr. ufanje, Boh. “fant, doufdnt, Pol. ufnosé, ete., but not reg. for ‘hope’), fr. vb. wptivati ‘hope’, SCr. ufati se, etc., etym.? Miklosich 269. Briickner 403, 449. For this group vs. following in ChSl., cf. Jagié, Entste- hungsgesch. 410.
ChSl., Russ. nadezda, SCr. nada, Boh. nadéje, Pol. nadzieja, fr. ChSl. na-déjate se ‘rely, hope’, Russ. na-dejat'sja ‘hope’, etc., lit. ‘place oneself on’, cpd. of déja, déti ‘place, put’. Berneker 182, 193.
7. Skt. d¢d-, dcds-, fr. d-cds- ‘ask, sup- plicate, wish, hope for, expect’, cpd. of ¢ds- ‘correct, instruct, rule’. Uhlen- beck 22.
Av. vyaéra-, etym.? Barth. 1475 f.
16.64 THANKS
Grk. xapis Goth. awiliup, bank Lith. padeka NG dxaptord (vb.) ON pokk Lett. patetksana ie gratiae Dan. tak ChSl.  blagodétt, chvala a grazie Sw. tack SCr. hvala a Temerciments, graces OE panc Boh.  diky Rum gracias — ME _ thanke(s) Pol.  dzigkt
aie ibe NE thanks Russ. blagodarnost’ Nir uide Du. dank Skt.  krtajnata- Vv. buidheachas OHG danc B diolch MHG dance
"  trugarez NHG dank
_ vords that express the feeling of
ty see gratitude’ are either the those fet, mare often derived from, ine (e.g. through the adjs., ete, iaihich ¢ vness, NHG dank-bar-keit, ae therefore preferred in the tended = Scussion, This heading is in- eto, (sg, ie thanks in give thanks, Sther lan obs., and in several of the Buages the pl. obligatory or
usual in this sense); not as = thanks! and similar polite expressions, which, though of the same group, with some exceptions (e.g. Lith. adia, fr. the sound of asneeze = ‘good luck, God bless yow’; Russ. spasibo : spasat’ ‘save, spare’), are not always identical with the forms listed (e.g. Fr. merci).
The words are cognate with others for ‘joy, pleasure, praise, favor, recognition’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
eS ees
Digitized by Arya Samaj Foundation Chennai and eGangotri
1166 SELECTED INDO-E
```


## [2026-09-05T17:43:13.967Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5560,5620p' CHEUNG.txt"
}
```


### [2026-09-05T17:43:14.015Z] TOOL RESULT

```
0 This root is a so-formation of IE *d'eug"- ‘to prepare’. See *daud!. 
*REFERENCES: EVP: 41; IIFL II: 391b; WIM I: 68; Vahman — Asatrian 1991: 92 f.; Paul 1998: 296a; 
Cabolov 2001: 329; Lecoq 2002: 121, 123, 125 (passim) 


*daxš ‘to show, teach, reveal, mark’ 

*AVESTAN: daxs- ‘to instruct, show’, daxsta- (orig. ppp., n.) ‘sign, revelation [BMP 
/daxsag/]; menstruation [= BMP /dastan/]’ (Y 34.6, Y 51.9, V, etc.), ? OAv. daxsära- 
(m.) ‘mark, sign’ (Y 43.7) || (+ *fra-) ‘to instruct, teach’, also YAv. fradaxStar- 


‘teacher’ — Liste: 27 

Pres. {1} them.: INJ. 3sg. OAv. daxsat (Y 43.15); Pres. {2} aia-: OPT. med. 3sg. YAv. aóaxsaiiaeta (Y 
12.5), IMPV. 25р. OAv. «fra»daxsaiia (Y 33.13) 

*MIDDLE PERSIAN: MMP dxsg, ВМР dhsk /daxsag/ ‘sign, mark, characteristic; 
memory’ (Nyberg II: 61b), BMP dst’n /dastan/ ‘menstruation; menstruous’ (Cantera 
2004: 307) = DMMPP: 148a 

*NEIR: NP dastan ‘a menstruating woman’, ? NP daxs ‘start, commencement of 
work; dark and gloomy’. Ф The meaning, “Geschäft, Mühe’ assigned to NP daxs by 
Horn 1893: 120 (and subsequently adopted in e.g. EWAia I: 690 s.v. daks) does not 
exist. The two main meanings generally found in lexicographical works are (cit. 
Dehkhoda, s.v.): 1. "It is the commencement of work. One says, ће daxs is to you, it 
means the first business is with you (Dictionary of Asadi). It is the start and 
commencement (Jahangiri)..." and 2. "dark and gloomy (Jahangiri)...". (... (¿ Sot»). 
25) lol jel (sul Sa). aus b ¿Llasa ud el Cowl ыз Zén Ae, WEL US on £ Lael T. 
and ... (4 Solge). Aas 2,5 2.). Daxs with the meaning ‘start, commencement of 
work’ may be connected to MP /daxsag/, the meaning deriving from ‘start-sign’, 
whereas daxs ‘dark and gloomy’ is perhaps related to *daj, from *'burnt, charred’ ? 
© The evidence for and the meaning assigned to Ir. *dax$ largely rest on the inter- 
pretation of the Avestan daxs- forms. Although there is general agreement on the 
broad meaning, the Avestan forms have been interpreted in several ways with the 
etymology assigned accordingly. According to Insler 1962: 55 the Avestan root 
daxs- has secondarily developed from the past participle of the root daés- ‘to show’ 


*(d)banz1 71 


(dais'), with *dixsta- > daxsta-. However, Schlerath 1962: 514 points out that this 
development (which does not appear to be regular, cf. Y Av. frapixsta-) should have 
taken place very early, as this supposedly abstracted root is already found in the 
Gathas: daxsat. Humbach 1959 II: 52 (repeated Humbach 1990 II: 144) equates 
OAv. daxsat with Skt. daks ‘to make right, be able [vel sim.]’: "macht es ... recht". 
This equation can be doubted though, since the Pahlavi translation does mention 
/daxSag/, which does not agree semantically well with Skt. daks 

PIE *dek"s- ‘to show’. Ф The generally accepted comparison of Hitt. /tekkussij‘/,-/ 
to Av. daxs- is disputed by Rieken 1999: 210 f., who rather relates Hitt. /tekkuss-/ to 
/tekri-/ *defilement', Gr. тёкрор ‘sign’. As kindly pointed out by A. Kloekhorst 
(personal communication), this is unlikely and unnecessary. Hitt. /tekri-/ may rather 
mean ‘deposition’ and for the interpretation of Hitt. /tekkuss-/ as a secondary 
enlarged -u-s-formation from the root *tek- one has to postulate some arbitrary 
developments. If we do uphold the Av.-Hitt. comparison, the Hitt. forms provide 
proof that the velar of the IE root *dek"s- must have been labialized. > LIV: 112 | 
Pok.: 189
```


## [2026-09-05T17:43:50.715Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^dek-\\|dek-\\b\" AHD_watkins1985.txt | head -20; echo \"=== deks ===\"; grep -n \"deks-\\|dexter\" AHD_watkins1985.txt | head -20"
}
```


## [2026-09-05T17:43:50.736Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dek\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-05T17:43:50.797Z] TOOL RESULT

```
<persisted-output>
Output too large (43KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b9u4srncn.txt

Preview (first 2KB):
127:complete agreement on the numerals from two to ten: dwo- (*duw6), trei- (*treyes), kvetwer- (*k”etwores), penk”e, s(w)eks, septm, oktd(u), newn, dekm. For the nu- meral “one” the dialects vary. We have a root sem-' in some derivatives, while the western Indo-European languages Germanic, Celtic, and Latin share the form oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE
...
</persisted-output>
```


### [2026-09-05T17:43:50.804Z] TOOL RESULT

```
359:dek-'
361:dek-?
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1409:Dart dhabh- DAINTY dek-1 DAIRY dheigh- DAISY agh-2, okw- DALE dhel- DALLES dhel- DAMAGE dap- DAME deme-! DAMN dap- DAMNIFY dap- Dan? deme-! DANDELION dent- DANE dan- DANEGELD gheldh- DANELAW dan-, legh- DANGER deme-1 DaNIsH dan- DAPPER dheb- DARE dhers- DARK dher-! DASTARD dhé-2 DASYURE dens-2 DATE do- DATIVE do- DATUM do- DAUB _albho- DAUGHTER dhugheter- DAUNT deme-2 DAWN agh-2
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1426:DIET? deiw- DIFFER bher-! DIFFICULTY dhé-1 DIFFIDENT bheidh- DIFFRACTION bhreg- DIFFUSE gheu- DIG dhigw- DIGEST gerere DIGIT deik- DIGNIFY dek-1 DIGNITY dek-1 DIGRESS ghredh- DIKE dhig¥- DILATE stela- DILATORY tela- DILIGENT leg-1 DILUTE leu(@)- DIME dekm DIMENSION mé-2 DIMER (s)mer-2 DIMINISH mei-2 DIMITY mei-4
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1430:po! dhé-1 DOCENT dek-! DOCETISM dék-1 DOCILE dek-1 DOCK! deuk- Dock dheu-! DOCTOR dek-1 DOCTRINE dek-1 DOCUMENT dek-1 DODDER! dud- DODDER? dud- DODECAGON dekm, dwo-
1432:DOGE deuk- pocMa dek-1 pDoGMaTIC  dek-! DOIT twei- DOLABRIFORM del-3 DOLCE dik-u- DOLDRUMS_ dheu-t DOLE! dail- DOLE? del-3 DOLERITE del-2 DOLICHOCEPHALIC del-1 DOLICHOCRANIAL  del-1 DOLOR del-3 DOLPHIN gWelbh- Dott dheu-1 Dom deme-1, dhé-1 DOMAIN deme-! DOME deme-1 DOMESTIC deme-1 DOMICILE deme-! DOMINATE deme-1 DOMINICAL deme-1 DOMINIE deme-1 DOMINION deme-' DOMINO! deme-1 DOMINO2 deme-1 DONATION d6- DONATIVE d6- DONOR do- poom dhé-1 pooR dhwer- DOPE dub- DORMANT drem- DORMER drem- DORMITORY drem- DORSAL dorsum poRrsO- dorsum pory? aurum DOSE dé-
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
1997:ORGAN werg- ORGANOLEPTIC (s)lag¥- ORGANON werg- ORGASM wrdg- ORGEAT ghers- ORGY werg- ORIENT er-1 ORIFICE 6s- ORIFLAMME aurum ORIGIN er-1 ORIGINAL er-! ORINASAL 6S- ORIOLE aurum ORLOP klou-, uper OrMaAzD ansu-, men-1 ORMER mori-, ous- ORMOLU aurum, mele- ORNAMENT ar- ORNATE ar- ORNITHO- oF OROIDE aurum OROTUND 6s- ORPHAN orbh- ORPHREY aurum ORPIMENT aurum ORT ed-, ud- ORTHO- wrddh- ORTHODOX dek-1 ORTHOGONAL genu-1 ORTHOPEDICS pau- ORTHOSTICHOUS _steigh- ORTHOTICS wrddh- ORTOLAN gher-! os! Os-
2049:PANACEA yék- PANACHE pet- PANADA pa- PANATELA pa- PANCRATIUM pant- PANCREAS kreue-1, pant- PANDECT dek-1 PANDEMIC da- PANDORE pandoura PANE pan- PANEGYRIC ger-! PANEL pan-
2252:SEXTUPLE pel-3 SHABBY skep- SHADE skot- SHADOW skot- SHAFT! skep- SHAH tké- SHAKO dek-2 SHAKTI kak-1 SHALE skel-1 SHALL skel-2 SHAMBLES skabh- SHANK skeng- SHAPE skep- SHARD  sker-1 SHARE! | sker-1 SHARE? sker-1 SHARP sker-1 SHATTER sked- SHAVE skep- SHAWM kolem- SHE so- SHEAF skeup- SHEAR sker-1 SHEARS sker-! SHEATH skei- SHEAVE? skei- SHED! skei- SHEEN keu-1 SHEET! skeud- SHEET2 skeud- SHELDRAKE skel-1 SHELF skel-1 SHELL skel-1 SHIELD skel-1 SHIMMER skesi- SHIN! skei- SHINE skeei- SHINGLE! sked- SHINGLES kenk-! SHIP skipam SHIP skep- SHIRT sker-1 SHIT skei- Suiva_ kel-1 SHIVER? skei- SHOAL? skel-1 SHOOT skeud- SHORT sker-1 SHOT! skeud- SHOVE skeubh- SHOVEL skeubh- sHow keu-! SHOWER! kéwero-
2336:TaaL del-2 TABES ta- TACET tak-1 TACHE dek-? TACHISM deik- TACHYLYTE leu-! TACHYPNEA pneu- TACIT tak-1 Tack! dek-2 TACT tag- TACTICS tag- TACTORECEPTOR tag- TAEL tele- TAENIA ten- TAFFETA temp- TAG! dek-2 TAHSILDAR dher-2 TAIL! dek-2 TAINT teng- Tad (s)teg- TAKE tak-2 TALE del-2 TALENT tela- TALES to- TALION tele- TALISMAN kWel-1 TALK del-2 TALLOW del-4 TAME deme-2 TAMPON tap- TANDEM to- TANG! denk- TANGENT tag- TANGIBLE tag- TANGLE? tenk-2 TANGORECEPTOR tag- TANSY dhwene- TANTALIZE tele- TANTALUS tele- TANTAMOUNT to- TANTRA ten- Tap! tap-
=== deks ===
133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
781:nepot-. Grandson, nephew. Feminine *nepti-. Latin nepos, grandson, nephew, and neptis, granddaughter, niece: NEPHEW, NEPOTISM, NIECE. [Pok. nepdt- 764.] ner-1, Under, also on the left; hence, with an eastward orientation, north. Suffixed zero-grade form *nr-t(r)o- in Germanic *north-, north, in: a. Old English north, north: NORDIC, NORTH; NORMAN; b. Old English northerne, northern: NORTHERN; c. Middle Dutch nort, north: NorsE. Compare deks-. [Pok. 2. ner- 765.] ner-2, Also aner-. Man; basic sense ‘vigorous, vital, strong.” 1. Oldest root form *aner- (with prothetic vowel) in Greek anér (stem andr-, from zero-grade “anr-), man: ANDRO-, -ANDROUS, -ANDRY; PHILANDER. 2. Extended zero-grade form *(9)nrt- in Sanskrit nrtyati, he dances (“moves vigorously”): NAUTCH. 3. Referred by some to this root (as if “having human eyes”; dps, eye; see ok’-) but more likely of unknown origin is Greek anthropos, man (earliest Greek form anthrék”os): ANTHROPIC, AN- THROPO-; LYCANTHROPE, MISANTHROPE, PHILANTHROPY, THEANTHROPIC. [Pok. 1. ner-(t)- 765.]
1235:AMATIVE amma AMATORY amma AMAZON magh-2 AMBAGE ag- AMBASSADOR ag- AMBERGRIS gher-3 AMBI- ambhi AMBIDEXTROUS deks- AMBIENT ei-1 AMBIGUOUS ag- AMBITION ei-1
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
```


## [2026-09-05T17:44:04.499Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"17\\.2[0-9] *TEACH\\|TEACH$\\|TEACH \" SYN.txt | head -10; echo \"---\"; grep -n \"daxš\\|daxs-\\|frada\" SYN.txt | head -10"
}
```


### [2026-09-05T17:44:06.004Z] TOOL RESULT

```
30147:17.27 TEACHER il a nor, REASON 17.28 ScHooL 7.12 tax! (= Reflect, etc.) 17.31 REMEMBER 17.18 Tams? (= Be of the Opinion) 17.32 Forcet 114 BELIEVE 17.33 Mranine
30777:17.25 TEACH
30863:17.27 TEACHER
---
30811:Av. daxzs-, esp. cpd. fra-daxs-, etym. dub. Walde-P. 1.784. Barth. 676.
30870:f Ir. forcitlaid maister Skt.  adhyapaka-, upade- : Nir. = maighistir NE teacher caka-, cikgaka- Y W. athro Du. leeraar Av. addrapali-, fradazi- ; Br. mestr, skolaer OHG _ lérdri, meistar tar-, EaSan-
30903:Av. fradaxstar-, fr. fra-daxs- ‘teach’. Barth. 982.
34686:WARFARE 1387 20.23 SLING Grk. opevddyn Goth. . Lith.  vilksné NG odevddyn, opevtiva ON sléngva Lett. linga Lat. funda Dan. _ slynge ChSl. praita It. jionda Sw. slunga SCr. praca Tr. fronde OE lipere Boh. prak Sp. honda ME  slinge Pol. proca Rum. prastie NE sling Russ. pragéa Tr. tailm, taball Du. slinger Skt. Pare NIr. —crann tabhaill OHG - slinga, slengira Av. fradaxiana- W. fron dafl MHG sslinge, slenger Br. batalm, talm NHG §ssschleuder +
34714:Av. fradaxganda-, evidently fr. a fra- dazs-, but no apparent relation to the known dazés- ‘teach’. Barth. 981.
```


## [2026-09-05T17:44:14.930Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport bisect,re\nt=open('SYN.txt',encoding='utf-8').read().split('\\f')\ncum=[];s=0\nfor p in t:\n    s+=p.count('\\n')+1; cum.append(s)\nfor ln in [30777,30811,30863,30903]:\n    i=bisect.bisect_left(cum,ln)\n    nums=re.findall(r'\\b1[12][0-9][0-9]\\b', t[i][:400]+t[i][-400:])\n    print(ln,'leaf',i,'nums',nums[:6])\nprint(repr(t[bisect.bisect_left(cum,30811)][:300]))\nEOF"
}
```


### [2026-09-05T17:44:16.999Z] TOOL RESULT

```
30777 leaf 1257 nums []
30811 leaf 1260 nums []
30863 leaf 1261 nums []
30903 leaf 1262 nums []
'��make a sign, beckon’, etc. Walde-P. 2.218 f. Berneker 2.17 f.\n7. Skt. kapata-, perh. (*kmp-) : kamp- ‘tremble’ (if orig. ‘bend, stoop’), Grk. kéurrw ‘bend’, Lith. kumpti ‘bow’. Uhlenbeck 42. Walde-P. 1.350.\nSkt. chala-, hence chalaya- ‘deceive’, etym. dub., perh. : chada- ‘cover, cover- ing’, chad'
```


## [2026-09-05T17:44:23.722Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8').read().split('\\f')\nfor i in range(1255,1264):\n    txt=t[i]\n    nums=re.findall(r'\\b12[0-9][0-9]\\b', txt)\n    print(i, nums[:8], '|', txt[:90].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T17:44:26.177Z] TOOL RESULT

```
1255 [] | z (ChSl. iz) ‘out’? and -sto-: IE *sta- ‘stand’, like pro-stt ‘straight, simple’, etc. (Wa
1256 [] | 68 f. Lat. vb. mentiri ‘lie’ : méns, mentis ‘mind, intelligence, thought’ (17.11), with se
1257 [] |  th eit on 3 Gme. group the sense of ‘de- Sander, blame’ seems to be sec- ondary and ex me
1258 ['1215', '1243'] | -P. 2.223. K. Schneider, KZ 66.253. W. twyll, Br. touellerez, toellerez, beside vbs. W. tw
1259 [] | P. 1.874. Falk Hie, e 153. Weigand-H. 1.233, 2.1080. 5 Lith. apgaulé, apgavas, etc. : ap- 
1260 [] | ��make a sign, beckon’, etc. Walde-P. 2.218 f. Berneker 2.17 f. 7. Skt. kapata-, perh. (*k
1261 ['1260'] | tala, re- in Vulgate). Late Lat. perdéndre (> It. perdonare, Fr. pardonner, Sp. perdonar),
1262 [] | t Ant 4 aa 1s understood as the most ge- | adjs. (e.g. Lat. bene : bonus) or be quite fae 
1263 [] | ecor Meee Lith. labas (usual only in greetings a labas rytas, laba diena ‘good Mornin 3 go
```


## [2026-09-05T17:44:31.038Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | head -3; grep -n \"daxš\\|daxs\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-05T17:44:31.097Z] TOOL RESULT

```
49431:Aber av. daxs- „lehren", sowie np. daxs- „Geschaft, Miihe" bleiben fern 
53494:„Hitze, Sommer“ np. day „Brandmal ££ ; av. daxsa- m. „Brand ££ .
```


## [2026-09-05T17:44:34.895Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '49400,49460p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== pages file ===\"; grep -n \"bleiben fern\" WLD_Bd1_pages.txt | head"
}
```


### [2026-09-05T17:44:34.956Z] TOOL RESULT

```
Dehnstufe ( [*te^-u § ), got. tewa „Ordnung“, gatewjan „anordnen“ (s. uber die 
zu letzterem gehorigen grm. Worte Psilander KZ. 45, 281 f, und u. Wz. 
*deu{a)~ „sich riiumlich vorwarts bewegen'). 

Ai. duqnoti, ddsti, ddcati ;/ bringt Opfer dar, erweist Ehre, gewahrt, ver- 
leiht“, dagvams- ,,die Gotter ehrend, fromm“, dehnstufig wie hom. dt'jxvv/tiat 
(nur ptc. Sgxvv/uevog, von L. Meyer BB. 2, 260 If. fur <5 etxvv/uevog herge- 
stellt) „begruBe“ = ai .dagnoti; normalstufig hom. Seixavocovro „sie begriiB- 
ten“ ( ei nach L. Meyer aaO., Bechtel Lexil. 96 metr. Dehnung fur e wegen 
Sexavdzaf aozia^Ezai Hes., wahrend Wackernagel BB. 4, 268 f. Sgxavoiovro 
bevorzugt), Intensiv SgSr/jitai (3. pi. praes.), SgSexio, dijdeyaTo (3. sg. und 
pi. impf.) (fur iiberliefertes SeiS- einzusetzen) „begriiBen, bewillkommnen“ 
( 8 . dazu Wackernagel aaO., Boisacq 181; Brugmann GrGr. 3 291, 4 33S halt 



784 


dek- 


die Schreibung beiy.vv uevog, dety.avocovro fiir vielleieht richtig auf Grund 
eines Wzansatzes de[i]k- mit dek- als sekundarer Normalstufenbildung, was 
ohne auBergriech. Stiitze ist), dgSioxo/iai (iiberliefert Seid-) „begriiBe" (fiir 
*dt]de{>i)-ay.ojuai nach dem Praes. auf - 10 x 00 , s. Bechtel aaO.); ai. dagas- 
yati „erweist Ehre, verehrt einen Gott, ist gnadig" (Denominativ eines 
*dagas n. = lat. decus); Desiderativ dlksati „weiht“, diksa „Weihe“ (mit 
sekundarer Dehnung des i aus *di-dk-s s. Giintert IP. 30, 98 f.); daksati 
„ist tiichtig, macht es einem recht, ist gefallig", daksa- „tiichtig, geschickt". 

Aber av. daxs- „lehren", sowie np. daxs- „Geschaft, Miihe" bleiben fern 
(Gutt. ! s. TJhlenbeck Ai. Wb. 119), lat. deed, -ere „es ziemt sich, ziert, 
pafit gut", decus , -oris „Zierde“, umbr. tigit „decet“ (s. Vf. 2 u. deed m. Lit., 
auch fur o. deketasiui , degetasis , vielleicht „ordinarius“), lat . dignus 
„wiirdig, wert; wozu befiihigt" (*dec-nos ; die Konstruktion mit dem Abl. 
erklart Skutsch Gl. 2, 158 f. aus einer Gdbed. „womit geziert"; nicht 
nach Osthoff MU. 4, 206, Pay AJP. 31, 45 zu anord. tTgenn „vornehm" 
und Wz. *deik- „zeigen", s. Yf. LEWb. 2 s. v.); 

mir. deck „der beste, vorziiglichste" (= lat. decus-, Fickll 4 145); [aber 
cymr. deivr „Held“ ist ags. Lw., wegen des g bleibt auch fern ir. dag ,,gut“, 
cymr. da ds., gall. Dago-vassus ] ; gr. agideixeTog „ausgezeichnet" (metr. ge- 
dehnt fiir -dexerog, Schulze Qu. ep. 242) ; 

lat. doceo „lehre" (, mache etwas einem gut scheinend“, s. Yf. LEWb. 2 u. 
decet ), gr. doxeT yoi „(es ist mir annehmbar =) scheint mir", doxeco (dofeo, 
edoqe) „meine, scheme", dofa „Meinung; Ruhm“ (Suffix -oa, Solmsen Beitr. 
241 f.), doxifiog „ansehnlich, erprobt", doyfia „BeschluB“, doxevco „fasse ins 
Auge, beobachte", jigoodoxaco „auf etwas oder jeinanden warten, erwarten"; 
gr. diddaxco „lehre" (aus *did 0 k-sko, s. Giintert Abl. 45 ; friihere Erklarungs- 
versuche fiir das a s. bei Yf. LEWb. 2 223 u. decet, Boisacq s. y., Kretschmer 
Gl. 4, 349 m. Lit.) ; lat. disco, didici ,,lernen" ( *di-dk-sko allenfalls *di-d 0 k-skd; 
eine Gdf. *di-dak-sko, s. Boisacq 185, ist wegen doceo nicht zu yertreten). 

Zum es-St. ai. dagas(ydti), lat. decus stellen sich (nach Persson IP. 2, 244 
Anna. 2, Persson IP. 5, 48, KZ. 38, 410) auch die auf einem loc. *deksi 
„auf der tauglichen Seite" („auf der Seite der greifenden, fassenden Hand") 
oder unmittelbar auf dem St. *dek-s- beruhenden Worte fiir „rechts“: 

Ai. ddksina-, daksind- „rechts, siidlich, tiichtig, geschickt", ay. dasina- 
=== pages file ===
21871:witz          BB. 28, 310) bleiben fern.
35986:kandu- m. ..Pfanne. Rost“, Tchad ik a „gerostetes Korn“ bleiben fern);                                              aksl.
36099:KZ. 40, 257 Red.-Kote, 566) bleiben fern: russ. (usvv.) lcomohjj hornlos"
37732:„diirres Gestriipp" bleiben fern,                        s.       Uhlenbeck Ai. Wb. 38);
45075:bret. kraou „Stall" bleiben fern     trotz Pedersen KG. I 92]; aisl. hr of
51889:los“ und gael. gaol „Liebe“, mir. gael „Yerwandtschaft" bleiben fern; die
61457:   Gr. iiol. ygavco ,,ritze, verletze", usw. bleiben fern, s. u. ghreu- „reiben“.
74090:   Aber av. daxs- „lehren", sowie np. daxs- „Geschaft, Miihe" bleiben fern
```


## [2026-09-05T17:44:44.396Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '49460,49500p' WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T17:44:44.444Z] TOOL RESULT

```
Ai. ddksina-, daksind- „rechts, siidlich, tiichtig, geschickt", ay. dasina- 
„rechts“, lit. desine „die rechte Hand", aksl. desm ,,rechts“; gr. degi- 
t sgog = lat. dexter, -tra, -trum (komp. dexterior, Sup. dextimus ), osk. destrst 
(abgekiirzt fiir *destrust) „dextra est", umbr. destrame ;; in dextram"; [fern 
bleibt ir. Frauenname Decider — trotz Fick II 4 145, Brugmann II 2 1, 324]; 
gr. de£iog „rechts, gliickverkiindend, geschickt, gewandt" (yon deft- entw. 
mit Formans -o-, oder -yo-, vgl. dann gall. Dexsiva dea, Brugmann II 2 1, 
164); mit Suffix -no- (wohl nach *lai-uos, skai-uos „links“, Brug- 
mann aaO. und schon II 1 129), air. dess „rechts, siidlich", cymr. deheu 
ds., got. taihswa, ahd. zeso ,_rechts“, got. taihswl >, ahd. ses(a)wa „die rechte 
Hand"; alb. djadte „rechts“ (G. Meyer Wb. 69, s. zur Form Pedersen KZ. 
36,291; das von G. Meyer damit gleichgesetzte ksl. desl s ist wohl Y er- 
derbnis fiir desm, s. Berneker 187). 

Ygl. Fick I 4 65, 66, 234, 452, 453, II 4 145, III 4 153, 154. — Uber Brug- 
manns Wzansatz de{i)k- s. o.; auch Pedersens, KZ. 38, 410, Yereinigung 



dek-, dak-, dek dekm 

7 ’ o 


785 


von *dek- mit *deilc- „zeigen“ (ebenfalls mit ausgestreckter Hand) macht 
dieselben Yoraussetznngen. 

dek-, dek- oder (wegen des Aind.) dek- (: dole-, dek-) „reiBen, zerreiBen, 
zerfasern". 

Ai. daga „die am Ende eines Gewebes hervorragenden Zettelfaden, 
Fransen"; got. tagl n. „einzelnes Haar“, anord. tagl n. „die Haare im 
Pferdeschwanz" ags. tcegl (engl. tail ) „Schwanz“, ahd. sagal „Schwanz, 
Stachel, mannliches Glied, Rute“; got. tahjan „reiBen, zerren", distahjan 
„zerstreuen“, isl. tceja, tabi „karden“, norw. mdartl. tceja ( *tahjan ) und taa 
(*tahdn) „fasem, zerreiBen"; anord. tag , PI. tceger und tagar f. „Faser“, 
mhd. zdeh, zahe f. „Docht, Lunte"; in anderer Bed. („zerrend — ziehend, 
binausziehend") norw. mdartl. taag „langsam und andauernd", mnd. tege,
```


## [2026-09-05T17:44:45.914Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ارتودوکس\\|ارتدوکس\\|ارتودکس\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"=== دکتر ===\"; grep -n \"دکتر\" MON_part1.txt | head -5"
}
```


### [2026-09-05T17:44:46.010Z] TOOL RESULT

```
=== دکتر ===
105:کفالت اداره دانشسراها در وزارت فرهنگ» وارد دورة دکتری زبان و ادبیات 
107:گردید. پس از به بایان رسانیدن دورة دکتری» جلسة دفاع از پایان‌نامةٌ دکتری وی 
110:دکتر ادبیات فارسی در ايران شناخته شد. از آن پس به سمت ذانشیار و سپس به 
114:شورای ملی شروع شد؛ دکتر معین به همکاری وی برگزیده شد. در دی ماه 
116:مجلس شورای ملی منتقل شد و طبق وصیت‌نامه‌های سعظمله دکتر معین به
```


## [2026-09-05T17:44:53.428Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"--- $f\"; wc -l $f; head -c 300 $f; echo; done 2>/dev/null"
}
```


### [2026-09-05T17:44:55.092Z] TOOL RESULT

```
--- MON_part1.txt
99339 MON_part1.txt
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نا
--- MON_part2.txt
94500 MON_part2.txt
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاع�
--- incoming/MON/MON_2vol_Adena_v1_djvu.txt
99339 incoming/MON/MON_2vol_Adena_v1_djvu.txt
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نا
--- incoming/MON/MON_2vol_Adena_v2_djvu.txt
94500 incoming/MON/MON_2vol_Adena_v2_djvu.txt
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاع�
```


## [2026-09-05T17:45:00.030Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ودوکس\\|ودکس\\|تودو\\|orthodox\\|Orthodox\" MON_part1.txt MON_part2.txt | head -10; echo \"=== dekor/doktor ===\"; grep -nE \"décor|docteur|dekor|doktor\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-05T17:45:00.101Z] TOOL RESULT

```
MON_part2.txt:27840:کودکستان: «تات-0۵21: (امر.) مدرسه‌ای 
MON_part2.txt:27842:تحصبص دارد. ضح.. « کودکستان» پس از 
MON_part1.txt:9618:ار تودوکس: 0۳۱0۵0 (ص. ۱.) دارای ایمان 
MON_part1.txt:59717:کودکستان و بان تر از دبرستان است. 
=== dekor/doktor ===
```


## [2026-09-05T17:45:02.675Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9610,9630p' MON_part1.txt; echo \"=== دکتر / دکور ===\"; grep -n \"^دکتر\\|دکتر:\\|دکور\" MON_part1.txt | head -10"
}
```


### [2026-09-05T17:45:02.740Z] TOOL RESULT

```
خوردن, به یکك باره در آب فرو شدن. 
ارتماسی: وت [غ. ف.] (ص‌نسه.) 
منسوب به ارتماس. سل ارتماسی: (فق.) 
فرو رفتن در آب کر یا جاری به قصد غسل» 
نوعی از غسل که در آن تمام سر و تن را به 
نیت سل یکباره در آب فرو برند؛ مة 
ان در 

ار تودوکس: 0۳۱0۵0 (ص. ۱.) دارای ایمان 
و عقیدة صحیح. فرقه‌ای مخصوص از فرق 


مسنجیت. 
ارتهان: ات ۰](مصم ) گرو گرفتن» 
گروستاندن» گرو کردن به گروگان گرفتن. 
ارتیاب: ۳0 [غ.] (مسص‌ل.) شکت 
کردن؛ به شکك شدن» در شک افتادن» به 
شک افتادن» در تر دید افتادن» نز شک و 
تردید گردیدن کمان داد و 
تهمت کردن کسی را؛ کسی را متهم 

=== دکتر / دکور ===
110:دکتر ادبیات فارسی در ايران شناخته شد. از آن پس به سمت ذانشیار و سپس به 
143:دکتر محمدباقر (استاد پا کستانی) مورد تقدیر قرار گرفت. 
178:دکتر معین در سال‌های ۱۳۳۱-۳۳ عضو شورای عالی فرهنگ بود. در 
8912:اف وده‌اند. امروزه دانش مدکور را ادسیات 
24908:مسدکور بزند. (کد.) سخنان بزرگ» 
35001:کلمه «بره‌داته» در نند مدکور قسمك شده: 
40188:سالنکك. ( کا.) مبوة درخت مدکوره 
56582:مدکور سازند و در ولابات شمالی در 
62214:دکتر: ٩0:0۲‏ (.) آنکه بالاترین مراحل 
62219:دکترا: 3 (.) درجه دکتری» دکتری»
```


## [2026-09-05T17:45:08.789Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62210,62240p' MON_part1.txt; echo \"=== دکور ===\"; grep -n \"دکور\\|د کور\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-05T17:45:08.873Z] TOOL RESULT

```
تخته‌ای که روی آن نشینند» نیمکت. 
دک‌انداری: ۵-027 (ع. ف.] (حامص.) 
کاسبی در دکان. (مج.) چرب زانی. 

دکتر: ٩0:0۲‏ (.) آنکه بالاترین مراحل 
علمی را طی کرده در رشته‌ای به درجه 
اجتهاد ر سیده. (معمولاٌ) دکتر طب» پزشگی 
که دارای رتبه دکتری است (فر ه.) 

دکترا: 3 (.) درجه دکتری» دکتری» 
اجتهاد. 

دکترس: ۵ (.) خانم دک (یشتر در 
مورد پزشک زن استعمال می‌شود.) 
دکتری: آ-00007 [فر. ف.] (حامص.) دکتر 
بودن؛ اجتهاد؛ دکترا. 

دکترین: 0 (ا.) نظر به» اند بشه» فکر. 
دک زده: (0-)4.2212 (ص‌مف.) کسی که 
ریش و سبیل و مژه و ابرو را تراشیده باشد؛ 
چار ضرب زده. 

دکش: ۵ (ص.) (عم.) سست و بلند قد 
(شخص). 

دک شدن: 0 (سصل.) (عم.) 
آهسته از جایی بیرون رفتن بدون آنکه 
دیگران متوجه شوند» غایب شدن» جیم 
شدن. 

دکل: اماده [- دگل | ( تبر کشتی» دگل. 
=== دکور ===
MON_part2.txt:18245:استفادة گیاه مدکور برگک تازه و رشه 
MON_part2.txt:32553:مدکور در کنار جویبارها و رودخانه‌های 
MON_part2.txt:33429:به همین دلیل است که کل مدکور با اندوه و 
MON_part2.txt:42354:گیاهی درحت مد کور متوجه نقطة مزبور 
MON_part2.txt:43933:ای ی در در بای مد کور 
MON_part2.txt:46549:این است که در صیغه عقد مدت مدکور شود 
MON_part2.txt:50879:از هندسه را که از خواص منحنی‌های مد کور 
MON_part2.txt:53615:2 پرنده مد کور 
MON_part2.txt:57201:یعنی شیٌّ مد کور در جوار این عیر واقع شود 
MON_part2.txt:64727:تخم خارج می‌شود. ملخ مد کور بیشتر به
```


## [2026-09-05T17:45:17.649Z] TOOL CALL #57: Bash

```json
{
 "command": "pdftoppm -f 113 -l 113 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg113 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T17:45:18.838Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"orthodox\\|paradox\\|heterodox\" KLN_1966.txt | head -6; echo \"=== dexter ===\"; grep -n \"^dexter\\|dexter, adj\" KLN_1966.txt | head -6"
}
```


### [2026-09-05T17:45:19.588Z] TOOL RESULT

```
total 33696
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 13:45 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    24046 Sep  5 13:38 latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62837 Sep  5 13:37 mk108.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40927 Sep  5 13:43 mk109.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb     6518 Sep  5 13:38 pg110_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36325 Sep  5 13:32 pg110_yeth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46559 Sep  5 13:32 pg110_zbn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72718 Sep  5 13:38 pg111.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50381 Sep  5 13:37 pg112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65357 Sep  5 13:45 pg113.png
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


### [2026-09-05T17:45:19.646Z] TOOL RESULT

```
10197:Dada,  n.,  an  artistic  movement  characterized  by incoherence  and  the  love  of  paradoxes  ( art  and lit.)  —  F.  dada,  prop,  a  child’s  word  meaning ‘horse,  hobby  horse,  hobby’.  This  word  was chosen  in  1916  by  Tristan  Tzara,  a  Rumanian- born  poet  and  editor  in  Paris  (1896-1963),  to designate  this  artistic  movement.
10494:take,  accept,  receive,  receive  hospitably,  hold’, SoxeTv,  ‘to  seem  good,  to  seem,  think,  believe’, Soxeoeiv,  ‘to  watch  closely’,  86^a  (for  *S6x-<ra), ‘notion;  opinion;  honor,  glory’,  S6y|za,  ‘that which  one  thinks  true,  opinion,  doctrine,  decree’, 86xi[20?,  ‘tried ,  assayed,  genuine’,  86x0?,  a  wood¬ en  beam’  (lit.  ‘that  which  holds  the  roof’),  8e!;i6?, ‘on  the  right’,  SiSdoxetv,  ‘to  teach’,  Mir.  dech, the  best’.  Cp.  Adoxa,  choledoch,  condign,  Cymo- doce,  dainty,  Daksha,  decorate,  decorous,  deign, dexter,  diadoche,  Diadochi,  didactic,  dignify, dignity,  diksha,  Diplodocus,  disdain,  docent, Docetism,  docile,  docimasy,  docimology,  Doco- glossa,  doctor,  doctrine,  document,  dogma,  doxa- stic,  doxology,  heterodox,  orthodox,  pandect, paradox, synecdoche.
12181:doxastic,  adj.,  pertaining  to  opinion.  —  Gk. So^acmxoi;,  ‘forming  an  opinion,  conjecturing’, from  the  verbal  adj.  stem  of  8o!;at[etv,  ‘to  think, imagine,  to  form  an  opinion’,  fr.  So'a,  ‘notion; opinion;  honor,  glory’,  which  stands  for86x-0ot and  derives  fr.  Soxciv,  'to  seem  good,  to  seem, think,  believe’  (whence  also  Soypa,  ‘that  which one  thinks  true,  opinion,  doctrine,  decree’),  fr. I.-E.  base  *dek-,  *dok-,  ‘to  take,  receive,  accept; acceptable,  becoming,  good',  whence  also  L. decere,  ‘to  be  seemly  or  fitting’.  See  decent  and cp.  dogma,  the  first  element  in  doxology  and  the second  element  in  heterodox,  orthodox,  paradox, doxology,  n.,  a  hymn  of  praise.  —  Eccles.  L. doxologia,  fr.  Eccles.  Gk.  So^oXoyia,  ‘praise, laudation’,  which  is  compounded  of  Gk.  86i;ac, ‘glory’,  and  -Xoyta,  fr.  -Xoyot;,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  See  prec.  word  and  -logy.  Cp. also  next  word.
12182:doxy,  n.,  opinion,  doctrine  ( colloq .)  —  Back formation  from  words  ending  in  -doxy  (as heterodoxy,  orthodoxy,  etc..)  See  prec.  word, doxy,  n.,  a  wench ;  a  mistress  (slang).  —  Of  un¬ known  origin.
17632:heresiologist,  n.,  a  student  of  heresies.  —  Formed from  next  word  with  suff.  -ist. heresiology,  n.,  the  study  of  heresies.  —  Com¬ pounded  of  heresy  and  Gk.  -Xcyia,  fr.  -X6yoi ;, ‘one  who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  -logy, heresy,  n.,  unorthodox  belief  or  doctrine.  —  ME.
17696:heterodox,  adi.,  unorthodox.  —  Gk.  ExepoSo'ot;, ’holding  opinions  other  than  the  right’,  com¬ pounded  of  iixEpop,  'the  other’  (see  hetero-),  and 864a,  ‘opinion’,  fr.  Soxeiv,  ’to  think’.  See  decent and  dogma  and  cp.  doxastic  and  words  there referred  to.
=== dexter ===
11178:dexter,  adj.,  on  the  right-hand  side.  —  L.  dexter, ‘on  the  right  hand',  whence  arose  the  meanings ‘skillful,  favorable,  propitious,  fortunate’;  cogn. with  Gk.  Sc-  irepo;,  ‘on  the  right  hand’,  and  with OI.  daksinah,  daksinah,  ‘on  the  right  hand, southern,  skillful’,  Avestic  dashina-,  ‘on  the right  hand’,  Gk.  Se'io:,  ‘on  the  right  hand, fortunate,  clever’,  OSlav.  desnu,  Lith.  desinas, ‘on  the  right  hand’,  Lith.  desine,  ‘the  right hand',  Goth,  taihswa,  OHG.  zeso,  ‘on  the  right hand',  OIr.  dess,  on  the  right  hand,  southern’, W.  deheu,  Co.  dyghow,  ‘on  the  right  hand’,  Gaul. Dexsiva,  ‘goddess  of  fortune’.  Alb.  djab-te,  ‘on the  right  hand’.  All  these  words  are  prob.  deriva-
11182:dexterity,  n.,  1)  skill;  2)  cleverness.  —  F.  dexte- rite,  fr.  L.  dexteritatem,  acc.  of  dexteritas, ‘readiness,  skillfulness,  prosperity’,  fr.  dexter. See  dexter  and  -ity.
11183:dexterous,  dextrous,  adj.,  skillful,  adroit,  quick. — Formed  with  suff.  ous-  fr.  L.  dexter.  See  dexter. Derivatives:  dext(e)rous-Iy,  adv.,  dext(e)rous- ness,  n.
```


## [2026-09-05T17:45:24.051Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg113.png"
}
```


### [2026-09-05T17:45:24.379Z] TOOL RESULT

```

```


## [2026-09-05T17:45:24.377Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T17:45:38.846Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (319,320,321):\n    print('===== leaf',i,'printed ~',i+543,'=====')\n    print(t[i][:2600])\n\""
}
```


### [2026-09-05T17:45:40.743Z] TOOL RESULT

```
===== leaf 319 printed ~ 862 =====
                                                                                                    ‫<‬
                                                                                                    ‫‪.‬ی‬


                            ‫نکیوزبند ‪.‬‬             ‫ومند حکومتی رالیزکوبند کهبرسر‬                    ‫باشد ‪-‬‬

 ‫دستره ^ = بر وزن مسخره ‪ ۰‬بمعنی‬                    ‫ان قنل و کشتن واقع شود ؛ وبسکون ثالث بر‬
 ‫دسترباشد که دای کوچك دندانه دار است واصل‬                                          ‫وزن لمل کون هم هت ‪.‬‬
                      ‫آن دست اره بو‪:‬ه است ‪.‬‬        ‫دست دادن ‪ ۰‬کنابه‌ازحاصل‌شدن ‪۱‬۔‬
 ‫دست رن ‪ -‬با زای هوز (‪ )۱‬بر وزن‬                     ‫وبمل آمدن ‪ -‬وبیعت کردن ‪ -‬وآرام گردیدن‪.‬‬
 ‫کفش کن ‪.‬کنابه ازمردم ادم ویشیمان باشه =‬                                             ‫ومضبوط کشتن باشد ‪۰‬‬
‫و صاحب طرب و سرودگوی و خوشحال را لیز‬                ‫دست دآرستیی داشتی ‪ -‬کاه‬
 ‫کویند و کی رانز گفته‌اند کهدست مرچیزی‬                                         ‫از فارغ بودن ازکارهاست ‪.‬‬
                      ‫زد ومترسل بکی شود ‪.‬‬          ‫دست در آستین کردن = کنامه‬
  ‫دست سنگ‪ .‬باسین بی لقطه بورزن‬                                ‫‪.‬‬   ‫ازری‬
                                                                     ‫از باز داشتن ومنم کردن نود ا‬
‫هت رنگ ‪ .‬بمعنی دستاسنگك است که فلاخن‬
                                          ‫باشد ‪.‬‬
                                                   ‫دست دکرسه ردن د کنابه از‬
 ‫دست سو زه = بروزن هفت روزه »‬                       ‫جوان مردی کردن است یمنی بخشش و حانمی‬
 ‫دختری بزانی باشد که او را خواستگلری نموده‬                ‫‪۱‬‬                                           ‫ر‬
             ‫باشند اما هنوز نکاح نکرده باشند ‪.‬‬      ‫دست دست آوست» کابه ازتلط‬
‫= کنابه از رکف دادن‬       ‫شستی‬      ‫دست‬                                               ‫وغابه وزہادتی باشد ‪.‬‬
                        ‫ولا امید شدن باشد ‪.‬‬         ‫ار کوچکیرا‬      ‫بررزن کفتر ‪۰‬‬         ‫‪= ۴‬‬    ‫دس‬


 ‫دست شیکسته = ممروف است ‪٩‬‏ ‪-‬‬                        ‫کویند که پبکدمت‌کار فرمابند ‪ -‬و بمعنی دای‬
 ‫وکی را کیوزبند کهسبب تصیل مماش (‪)0‬‬                                 ‫‪۰‬‬       ‫دندانه دارهم آمده است‬    ‫کوچك‬



 ‫ازمابه وهنرو كمال وعلم وفضل وقدرت وشجاعت‬           ‫دست رادست ه معروف است ‪- ۴‬‬
 ‫وار و صنعت‬
          ‫کشدسوب ک‬
                 ‫وامثال اینپا نداشته با‬                             ‫ونابه از وزیر اعظم هم هت ‪.‬‬
                                                                                             ‫ک‬
                              ‫ویشه هم تداند‪. .‬‬
         
===== leaf 320 printed ~ 863 =====
      ‫کک‬
‫دست گز اد ہنم کاف فارسی و زای‬                                     ‫دستگار » باکاف بروزن‌دستبار‪ .‬همکار‪-‬‬
‫نقطه دار بالف کشده وبرای بی‌نقطة زده » کنابه‬                      ‫ند ‪ - ۱‬و بمعنی ساخته‬
                                                                                     ‫وهیرا‬
                                                                                         ‫گرند‬
                                                                                            ‫و دست کا‬
              ‫از مددکار وممد ومماون باشد ‪. ۳‬‬                            ‫ه‬
                                                                        ‫کهرک‬
                                                                           ‫سفه ب‬
                                                                               ‫پورداخته باشد مطلقاً ؟ ‪ .‬واضا‬
‫دستلث رن ‪ -‬بر وزن چشمك زن ‪.‬‬                                        ‫کنند و کونند « دستکار فلان ‪٩‬‏ بعنی ساخته‬
‫مطرب وسازنده گوسوریو‌دوخواننده‌باند‪ .‬ولادم‬                        ‫وپرداختة فلان ‪ -‬رشان وفرمان وتفش وکار نامه‬

                           ‫ویشیمالرا نگیوزبند ‪.‬‬                   ‫را یز گوبند که بردیوارها بچسانند و برستگها‬
      ‫دست گزیدن « بضم کاف فار‪-‬ی‬                                   ‫تکقنشند بجپت اعلام وتماشای مردم ‪ -‬وبمعنی‬
                                                                               ‫وچالاك وجلد هم مده است ‪.‬‬        ‫چت‬
‫است ‏ چه‬      ‫لدبیدن‬
                   ‫و سط‌ن‬          ‫لس‬
                                    ‫جصدر‬‫منی‬
                                          ‫بمم‬
‫دت بممتی صدرمجلس ومسند باشده ‪ -‬ویفتح‬
                                                                  ‫تخت‌گاه ‪ 4‬معمی‬   ‫بر وزن‬    ‫‪-‬‬   ‫دستگاه ‪۲‬‬
     ‫کاف فارسی بممنی دریغ وافوی خوردن ‪.‬‬                           ‫قدرت ‪ -‬وجمعیت و ‪-‬امان ۔ ودست ری ‪ -‬و مال‬
                                                                                 ‫وعلم وفصل ودانشمندی باشد ‪.‬‬
‫دست گزلن = بضمکاففارسی و زای‬
 ‫نقطه داربتحتانی رسیده وبنون زده» اسب جنبت‬                        ‫هنابه از قوای‬
                                                                              ‫وود ک‬
                                                                                  ‫دستگاه ج‬
‫را گونند که اس کتل است ‪ -‬وهرچیز که آترا‬                           ‫عشرم مشری‌است که سامعه وتاصره ولامه وذائقه‬

‫امتخاب کرده باشند ‪ -‬کونابه ازشخصی است که‬                           ‫حس‬    ‫ومتصر فه وحافظه و‬   ‫وخال‬     ‫وشامه و واهمه‬

‫پبوسته خواهد درمند وصدر مجلس بنشیند ‪.۷‬‬                  
===== leaf 321 printed ~ 864 =====
  ‫دست مرد‬                                                                                         ‫‪۱‬و‬
                                                                                                   ‫‪7‬‬


‫یر هم‬
    ‫ودنبده‌‪-‬عنی شنبهظو‬
                     ‫اسبان را بدان بن‬                      ‫دست کش ‪ « ۱‬جتح کاف و سکون‬
                                       ‫آمده اخت ِ‬          ‫شین قرشت » قاد نابینا راگوبند‪ .‬وآن شخصی‬
‫دست کندن سکنابه‌ازاق وی‌ویشمالی‬                            ‫باشد کهدست کوران راگرفته بهرجالب میبرد‪-‬‬
                                 ‫خوردن باشد ‪٦‬‏ ‪.‬‬           ‫وتانلو کدا زان کوشتت ومع اسو کرقا‬
                                                          ‫و نمی محکم‬            ‫وزبون وزبردست هم گفته‌اند‬
‫دستگه ه بفتم کاف فارسی ‪ ۰‬مخفف‬
                                                          ‫و مضوط باشد ‪ -‬وآنجه در دست گرفته بکشند‬
‫و علم‬   ‫سامان ‪-‬‬   ‫د‬   ‫وی‬      ‫که وت‬     ‫ات‬     ‫واه‬

                                              ‫باشد ‪.‬‬       ‫همچو کباده کومان زبرچاق وامثال آن ‏ وبمعنی‬
                                                          ‫مهرد دست ‪ -‬ومزدوری هم هت ‪ -‬و شخصی که‬
‫ت بروزن سردسیر ‪ ۰‬یمعنی‬           ‫دستگیر‬                    ‫چ‌روشاهین نگاه میداردوبتکار کردن میر سالد‬
‫واسیر کرده شده را یز گومتد‬            ‫مدد کار باشد "‬
                                                                                                   ‫ع‬
                                                           ‫وبچه که شکاری که مادر ویدر او را در حضور‬
‫‪-‬مفمول ‪٩‬‏ ‪ -‬وامرهم آمده‬
                      ‫و بممنی فاعل ‪ ۸‬و‬
                               ‫است‪۶۷ :‬‬
                                                           ‫امنکس‌جفت کرده باشند‪-‬و کر اسب این‌چنینی‬
                                                                                          ‫را نیز گونند ِ‪.‬‬

                                                           ‫دست گشادن ‪ -‬ممروف ات ‪- ۴‬‬

                  ‫‪۱‬‬   ‫دانند‬   ‫ومبارك‬   ‫وآیرا مندمن‬
                                                               ‫وکنابه ازجوانمردی وهمت وبخثش باشد ‪.‬‬
                                                           ‫دست کشی ‪ - ۴‬بءسنی دست مالیدن‬
                                                                      ‫و لامه‌کردن باشد ‪ -‬وکدبه ک‬
                                                           ‫ودابی را لیز‬
‫بدست بمالند ‪ -‬و پارچة مندیل ومندیل را لیز‬
                                                                                                     ‫‪9‬‬
‫کوبند ‪ -‬کونابه ازگرفتار واسیر وزبون باشد‪.‬‬
```


## [2026-09-05T17:45:49.039Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'دشن' in p or 'دشت' in p:\n        print(i, i+543, [w for w in ('دشن','دشت','دشتان','دشوار','دشمن') if w in p])\nEOF"
}
```


### [2026-09-05T17:45:50.561Z] TOOL RESULT

```
11 554 ['دشت']
16 559 ['دشت']
18 561 ['دشن', 'دشت']
27 570 ['دشت']
33 576 ['دشت']
47 590 ['دشت']
75 618 ['دشت']
101 644 ['دشت']
145 688 ['دشن']
170 713 ['دشت']
179 722 ['دشت']
181 724 ['دشت']
184 727 ['دشن']
219 762 ['دشت']
239 782 ['دشن']
248 791 ['دشت', 'دشمن']
251 794 ['دشت']
257 800 ['دشت']
258 801 ['دشت']
259 802 ['دشن']
281 824 ['دشن']
288 831 ['دشت']
298 841 ['دشن']
304 847 ['دشت']
311 854 ['دشن', 'دشمن']
321 864 ['دشت']
323 866 ['دشت']
325 868 ['دشن', 'دشت', 'دشوار', 'دشمن']
326 869 ['دشن', 'دشت', 'دشتان', 'دشوار', 'دشمن']
327 870 ['دشن', 'دشت', 'دشوار']
328 871 ['دشت']
329 872 ['دشت']
334 877 ['دشت']
355 898 ['دشت']
362 905 ['دشت']
369 912 ['دشت']
373 916 ['دشت']
390 933 ['دشت']
402 945 ['دشت']
411 954 ['دشت']
413 956 ['دشن']
420 963 ['دشت']
425 968 ['دشت']
447 990 ['دشن']
457 1000 ['دشت']
458 1001 ['دشت']
459 1002 ['دشت']
466 1009 ['دشن']
471 1014 ['دشت']
472 1015 ['دشت']
473 1016 ['دشت']
474 1017 ['دشت']
475 1018 ['دشت']
480 1023 ['دشت']
481 1024 ['دشت']
493 1036 ['دشت']
498 1041 ['دشت']
499 1042 ['دشت']
500 1043 ['دشت']
501 1044 ['دشن', 'دشت', 'دشمن']
505 1048 ['دشت']
506 1049 ['دشت']
512 1055 ['دشت']
524 1067 ['دشت']
529 1072 ['دشت']
530 1073 ['دشت']
537 1080 ['دشت']
552 1095 ['دشت']
556 1099 ['دشت']
587 1130 ['دشت']
593 1136 ['دشت', 'دشوار']
599 1142 ['دشت']
612 1155 ['دشت']
613 1156 ['دشت']
619 1162 ['دشت']
620 1163 ['دشت', 'دشمن']
621 1164 ['دشت']
631 1174 ['دشت']
663 1206 ['دشت']
665 1208 ['دشن']
678 1221 ['دشت']
```


## [2026-09-05T17:45:58.166Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (325,326):\n    print('===== leaf',i,'printed ~',i+543,'=====')\n    print(t[i][:3500])\n\""
}
```


### [2026-09-05T17:46:00.498Z] TOOL RESULT

```
===== leaf 325 printed ~ 868 =====
                                                        ‫بیان دهم‬
     ‫تست وذو لقت و کنات‬                       ‫نقطه دار مشتمل بو‬                     ‫در دال بی نةطه مأ شن‬

                                                                                                                      ‫ھ‬
 ‫‪.‬هت‬
   ‫بج‬‫وشد‬
       ‫بد وزشت وپیل (‪ )۳‬بمعنی کره با‬                              ‫دس » بفتح‌اول وسکون‌تانی» خودآرایی‬
‫تخفیف تارا الداخته‌الد دشپیل(‪)4‬شده‌است همجو‬                       ‫وخود راساختن وآراستن ‪ -‬وصورت خوش‪ -‬وشبه‬
‫دشمن که آن دشت من بوده معنی بد دل وزشت‬                                                        ‫رظیر ومانند ‪١‬‏ باشد ‪. ۴‬‬
‫‪ ۰‬ودشنام‬         ‫دل» چه من بمحنی دل همآمده ست‬
                                                                  ‫دشل ‪ -.)۱( ۳‬نم اول بروزن مقبل »‬
‫که بمعنی دشتنام (‪)e‬‏ بوده و دشوار که دشتوار‬
           ‫و دشخوا رکه دشتخوار و مافند آن ‪. ۷‬‬                     ‫کرحهامیرا گکوبندکه در مان گوشت و پوست‬

‫دشت بدتح اول پروزن طعت ‪ ۰‬محرا‬                                 ‫دیگرمیباشد ‪ ۰‬ومعربی غدد‬                ‫ادمی )‪ (۲‬وحوانات‬

                                                                                                                          ‫خوانند ‪.‬‬
‫و ببابان باشد ‪ - ۷‬و لام ولایتی است درخراسان‬
‫مشهوریدشت بیاض ‪ -‬وصحرایی است درتر کتان‬
‫وآن بدشت قیچاق اشتهاردارد ‪ -‬و نا) شهری‌هم‬                         ‫فارسی‌بتحتانی کشیده وبلام زده ‪ ۰‬بمعنی‌دشیل(‪)۱‬‬
‫و قربه است در‬               ‫)‪(٩‬‏ در آذرنایجان س‬        ‫هت‬         ‫مبان‬   ‫در‬     ‫کرهست‬     ‫آن‬    ‫و‬    ‫که غدد باشد »‬              ‫است‬



‫صفاهان ‪ -‬وموضمی است در فاری مشپور بدشت‬                        ‫» و معنی تسرکیبی آن دشت‬                       ‫وت‪.‬‬
                                                                                                              ‫پتوس‬
                                                                                                                 ‫ش‬
‫ارژن ؛ ومعرب آن دست باشد با سین بی‌تقطه ‪-‬‬                         ‫پیل (‪ )۳‬است بعنی کره بد » چه دشت بمعنی‬
  ‫(‪ )۳‬چك‪ .‬چش‪ :‬بیل‪.‬رك‪ :‬پیل‪.‬‬                            ‫(‪ )۷‬چك‪ :‬انان‪.‬‬                  ‫(‪ )۱‬چك‪ .‬چش‪:‬دشبل ‪.‬‬
       ‫بوده ‪.‬‬      ‫‪:‬‬   ‫)ل( جك‬            ‫‪ :‬دشنام ‪۰‬‬      ‫‏)‪ (e‬چك‬             ‫‪۲‬‬   ‫‪ ۳‬دشسل‬        ‫‪ ۰‬چش‬    ‫)‪ (4‬چك‬



  ‫دژ (بد ) چنانکه در‪ :‬دشمن‪,‬‬             ‫‪ - ۴‬وم اول =‬                     ‫(مخفف درس) ‪.‬‬           ‫‪ - ۷‬رلك‪ :‬دس‬

  ‫‪ - ۴‬در اراک (سلطانآباد) ‪« 8۷500‬مکی‌نژاد» وکره‪ :‬دشپیل ‪.‬‬                                              ‫دشخو ار ‪۳‬‬           ‫دشنام‪.‬‬


   ‫ت‌فوق‪.‬‬
        ‫کرلبكمااز‬
                ‫رکک‪ :‬ه‬                  ‫‪۱‬‬         ‫® _ ر که‪ :‬دشمن‪.‬‬                   ‫ر‪:‬دشپل» دژیبه ‪.‬‬
                                                                                                  ‫؟ ‏ ک‬
             ‫‪.‬‬   ‫‪ .‬رکك‪ :‬بر گے ‪°‬‬          ‫‪10520‬‬          ‫فدی‬   ‫»‬     ‫‪ - ۷‬بهلوی ‪thsad‬‏ «منای ‪۱۷‬‬

                                                                                                            ‫‪9‬‬     ‫‪.‬‬        ‫‪°١‬‬    ‫‪۰‬‏‬
                                                                                                     ‫‪۶۹۸‬‬        ‫شنه از صفحه‬

  ‫‪( ۰‬ح‪.‬م‪).‬‬       ‫دسك‬   ‫سس‬        ‫‪.‬رگ ‪:‬دسه‪.‬‬   ‫نورده»‬    ‫‪۳‬‬    ‫رست‬    ‫» مخفف‬       ‫ظ‬    ‫‪۵4‬‬   ‫‪۲‬‬    ‫» دشمر‬      ‫دسمه‬       ‫‪ ۵۳ ۵‬رك‪:‬‬

  ‫نام موا
===== leaf 326 printed ~ 869 =====
          ‫تا‬                                                                                                                             ‫دشتان‬

‫تن‬       ‫سوزن کشند‬          ‫که هر‬      ‫را گوند‬            ‫تایده‬    ‫رشته‬
                                                                                             ‫وبضم اول بمعنی بد وزشت بود ‪٩‬‏ ‪.‬‬
‫کسر‬       ‫اول و‬   ‫وسم‬       ‫را همکفته‌اند ؛‬           ‫خام‬    ‫و ربمان‬
                                                                             ‫تانی‬     ‫سکون‬   ‫بقتح اول و‬             ‫‪ ۴‬ت‌‬   ‫دشتان‬

‫نزرامده‬      ‫فارسی‬      ‫باکاف‬      ‫و‬   ‫‪:‬‬     ‫است‬      ‫هم درست‬       ‫اول‬
                                                                             ‫وفوقالی‌بالف کشیده وبنون زده‪ .‬حالض‌رامی‌گوبند‬
                                                                   ‫ان‬
                                                                                               ‫یعنی زیکه خون حیضش آید ‪۰‬‬
‫‪ ۰‬رسمان‬           ‫خشکی‬       ‫‪ ۰ ۸‬بر وزن‬               ‫دشکی‬
                                                                             ‫بضم اول بروزن بدتی » زلورا‬                        ‫دشتی‬
‫خامی که زتانر سند و مردوك مانند تنضه بنخده‬                                   ‫جون‬      ‫رنگه ‪,‬‬   ‫آن کرمی باشد سیاه‬                     ‫و‬   ‫گونند‬

‫وفرموله خوانند‪.‬‬              ‫ی‬    ‫وان بفه مانندرا دب‬                ‫شود‬      ‫بر عمنوی از اعنای آدمی بح یانند خون ازان‬
                                                                                                                                            ‫ا‬
          ‫باشد شبیه بماش وبعربی درجم خوانند ‪۶#.‬‬
                                                                                      ‫بمعنی بدباد لمودن وغیبت کردن ‪ ۴‬باشد ‪.‬‬
                                                      ‫‪۰‬‬    ‫ار ان است‬         ‫وواو‬     ‫شف‬   ‫با خای‬            ‫ار )‪۱‬‬             ‫دشخو‬



‫دشمیر "اه بروزن نقصیر» بمعتی‌قیض‬                                             ‫بروزن و معنی دشوار است که مشکل‬                          ‫‪۰‬‬    ‫معدوله‬


‫وعناصر اردمه راهم کفته‌اند که خاك‬                         ‫باشد ك‬   ‫و مد‬
                                                                                                                                          ‫باشد ‪.‬‬



‫دشن د بنتح‌ارل وسکون ثالی ونون »‬                                             ‫سین بی‌نقطه وفتح فوقالی» بمعنی محوی باشد‪.‬‬
                                                                                                         ‫‪۰‬‬    ‫ودبشستها به‌عتی محوسات‬


                                                             ‫باشد ‪۴3.‬‬

                                                                                                ‫(‪ )۱‬چش ‪ :‬دشتخوار ‪.‬‬
         ‫‪ - ۴‬اوستا ‪_itiavathsxad‬‏ ‪ .‬پپلوی ‪82111520‬‬                                         ‫در (بد) ‪.‬‬          ‫=‬     ‫رش‬     ‫=‬     ‫‪۱‬‬
 ‫از‪ :‬دشت ( = رش = رژ بد) ‪ ۳‬بار‬
                             ‫‪۴‬‬                                                    ‫هد« اسشق ‪. › ۰۲۷۵‬‬                 ‫( ارمنی ع ‪0۶‬‬
 ‫از ‪ :‬دش ( ‪ ۳‬دز » بد)‬                             ‫‪۵‬‬               ‫رکک‪ :‬شتها ‪ . ۱‬یور داود ص ‪- ۱۷‬‬                      ‫‪۴‬‬           ‫‪۰‬‬       ‫(‪.۵‬م‪).‬‬


     ‫‪۰‬‬    ‫م‪ . ( .‬ر که ‪ :‬اسشق وهوشمان ‪٩۹۵‬‏‬                          ‫دشوار )‬    ‫=‬        ‫‪ +‬خوار (ھ‪.‬م ) بهلوی ‪0 -_2-/۳3‬‬
     ‫یبر که ‪۲٩‬‏ وە‌نا
```


## [2026-09-05T17:46:20.571Z] TOOL CALL #63: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-09-05T17:46:20.625Z] TOOL RESULT

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


## [2026-09-05T17:46:24.398Z] TOOL CALL #64: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/de%C4%B1%CC%81-\" \\\n \"https://en.wiktionary.org/wiki/dexter\" \\\n \"https://www.etymonline.com/word/doctor\" \\\n \"https://www.etymonline.com/word/orthodox\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 113, roots Dek/Deks\" 2>&1 | tail -3; done"
}
```


### [2026-09-05T17:46:28.053Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/de%C4%B1%CC%81-
/home/sfmqrb/git/rishe/data/verification/sources/web/8379e855f01ca436.txt
### https://en.wiktionary.org/wiki/dexter
/home/sfmqrb/git/rishe/data/verification/sources/web/c8a88d2303de4fd4.txt
### https://www.etymonline.com/word/doctor
/home/sfmqrb/git/rishe/data/verification/sources/web/41609e3ed6a29a7d.txt
### https://www.etymonline.com/word/orthodox
/home/sfmqrb/git/rishe/data/verification/sources/web/a77f12fde6a91ab1.txt
```


## [2026-09-05T17:46:31.069Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -c 700 8379e855f01ca436.txt; echo; echo \"=== dexter ===\"; grep -n -m3 -A6 \"Latin dexter\\|deḱs\\|dek's\" c8a88d2303de4fd4.txt | head -30"
}
```


### [2026-09-05T17:46:31.141Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/de%C4%B1%CC%81-
FETCHED: 2026-09-05T17:46:26Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
=== dexter ===
231: Learned borrowing from Latin dexter ( “ right ” ) .
232-
233- Pronunciation
234- [ edit ] 
235-
236- ( UK ) IPA ( key ) : /ˈdɛks.tə/ 
237-
--
325: From Proto-Italic *deksteros , from Proto-Indo-European *deḱs-tero-s , from *deḱs- ( “ right ” ) . Cognate with Ancient Greek δεξιτερός ( dexiterós ) , and compare δεξιός ( dexiós ) , Old High German zesawa ( “ right hand, right hand side ” ) , Sanskrit दक्षिण ( dákṣiṇa ) , Old Church Slavonic деснъ ( desnŭ , “ right ” ) .
326-
327- Pronunciation
328- [ edit ] 
329-
330- ( Classical Latin ) IPA ( key ) : [ˈdɛk.stɛr] 
331-
--
550: Learned borrowing from Latin dexter .
551-
552- Adjective
553- [ edit ] 
554-
555- dexter   m or n ( feminine singular dexteră , masculine plural dexteri , feminine/neuter plural dextere ) 
556-
```


## [2026-09-05T17:46:38.056Z] TOOL CALL #66: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deḱ-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deḱs-\" \\\n \"https://en.wiktionary.org/wiki/دشن\" \\\n \"https://en.wiktionary.org/wiki/dašn\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 113, roots Dek/Deks\" 2>&1 | tail -2; done"
}
```


### [2026-09-05T17:46:42.047Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deḱ-
/home/sfmqrb/git/rishe/data/verification/sources/web/92cde14f1ed3396f.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deḱs-
/home/sfmqrb/git/rishe/data/verification/sources/web/5e075b8603702068.txt
### https://en.wiktionary.org/wiki/دشن
/home/sfmqrb/git/rishe/data/verification/sources/web/c28aafda30f87762.txt
### https://en.wiktionary.org/wiki/dašn
/home/sfmqrb/git/rishe/data/verification/sources/web/d0fbf3a484e10591.txt
```


## [2026-09-05T17:46:44.715Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 92cde14f1ed3396f 5e075b8603702068 c28aafda30f87762 d0fbf3a484e10591; do echo \"##### $f\"; head -5 $f.txt; done"
}
```


### [2026-09-05T17:46:46.767Z] TOOL RESULT

```
##### 92cde14f1ed3396f
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deḱ-
FETCHED: 2026-09-05T17:46:39Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/deḱ- - Wiktionary, the free dictionary

##### 5e075b8603702068
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deḱs-
FETCHED: 2026-09-05T17:46:41Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/déḱs - Wiktionary, the free dictionary

##### c28aafda30f87762
URL: https://en.wiktionary.org/wiki/دشن
FETCHED: 2026-09-05T17:46:41Z
STATUS: 200
TITLE: دشن - Wiktionary, the free dictionary

##### d0fbf3a484e10591
URL: https://en.wiktionary.org/wiki/dašn
FETCHED: 2026-09-05T17:46:42Z
STATUS: -1
TITLE:
```


## [2026-09-05T17:46:49.565Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,80p' 92cde14f1ed3396f.txt | tail -70"
}
```


### [2026-09-05T17:46:49.612Z] TOOL RESULT

```
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
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Descendants 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ deḱ- 

 Add languages 

 Reconstruction 

 Discussion 

 English
```


## [2026-09-05T17:46:49.968Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Persian\\|Middle Persian\\|right\\|gift\\|Etymology\" c28aafda30f87762.txt | head -30"
}
```


### [2026-09-05T17:46:50.018Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:46:52.696Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/^ Root/,/^ References/p' 92cde14f1ed3396f.txt | head -60; echo \"=== deks ===\"; sed -n '/Descendants/,/References/p' 5e075b8603702068.txt | head -40"
}
```


### [2026-09-05T17:46:54.638Z] TOOL RESULT

```
 Root 

 1.1.1 
 Descendants 

 1.2 
 References 
 Root
 [ edit ] 

 *deḱ- ( perfective ) [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ] [ 11 ] [ 12 ] [ 13 ] 

 to take 

 to perceive 

 Descendants
 [ edit ] 

 Terms derived from the Proto-Indo-European root *deḱ- (123 c, 0 e) 

 *déḱ-t ~ *dḱ-ént ( athematic root aorist ) [ 1 ] [ 2 ] [ 3 ] 
 Proto-Hellenic: 
 Ancient Greek: ἔδεκτο ( édekto ) 
 Homeric Greek: δέκτο ( dékto ) 
 Mycenaean Greek: 𐀆𐀒𐀵 ( de-ko-to /⁠dekto⁠/ ) 

 *dḗḱ-ti ~ *déḱ-n̥ti ( athematic Narten present ) [ 2 ] or *dé-deḱ-ti ~ *dé-dḱ-n̥ti ( reduplicated athematic present ) [ 3 ] [ 4 ] [ 5 ] 
 ⇒ *dēḱ-wéh₂ 
 Proto-Germanic: *tēwō ( “ order, array ” ) < *tēgwō ( see there for further descendants )

 ⇒ *dēḱ-w-éye-ti 
 Proto-Germanic: *tēwijaną ( “ to order, arrange ” ) 
 ⇒ ? Proto-Germanic: *tēwijaz ( “ ordered, ranked, classed ” ) ( see there for further descendants )

 Proto-Balto-Slavic: *deśitei 
 Proto-Slavic: *desiti ( “ find, encounter ” ) ( see there for further descendants )

 Proto-Hellenic: 
 Ancient Greek: δέχομαι ( dékhomai ) 
 Ionic, Aeolic, Cretan Greek: δέκομαι ( dékomai ) 

 Proto-Indo-Iranian: *dā́ćti ( “ to worship ” ) 
 Proto-Indo-Aryan: *dā́ṣṭi 
 Sanskrit: दाष्टि ( dā́ṣṭi ) , दाश्ति ( dā́śti ) 

 Proto-Iranian: *dā́šti ( “ to honor ” ) 
 Avestan: 𐬛𐬁𐬱𐬙𐬀- ( dāšta- , “ worshipped ” , verbal adjective ) 

 Khotanese: [script needed] ( dāś- , “ to receive with honor ” ) (or borrowed from Sanskrit)

 *dḱ-néw-ti ~ *dḱ-nw-énti ( new-present ) [ 2 ] 
 Proto-Indo-Iranian: *dāćnáwti 
 Proto-Indo-Iranian: *dāśnáwti 
 Sanskrit: दाश्नोति ( dāśnóti , “ attends, reveres ” ) 

 *de-dóḱ-e ~ *de-dḱ-ḗr ( reduplicated perfect ) [ 2 ] [ 3 ] [ 6 ] 
 Proto-Hellenic: 
 Ancient Greek: δέδεξο ( dédexo ) 

=== deks ===
```


## [2026-09-05T17:47:01.281Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"doceō\\|decet\\|dokéō\\|δοκέω\\|discō\\|decus\\|dignus\\|daxš\\|dax\" 92cde14f1ed3396f.txt | head -20; echo \"=== deks file ===\"; grep -n \"dašina\\|daxš\\|dexter\\|Avestan\\|right\" 5e075b8603702068.txt | head -20"
}
```


### [2026-09-05T17:47:01.349Z] TOOL RESULT

```
201: Latin: discō ( “ learn ” ) ( see there for further descendants )
204: The LIV assigns Hittite 𒁕𒀀𒀝𒆠 ( da-a-ak-ki /⁠dākki⁠/ ) , 𒋫𒀝𒆠 ( ta-ak-ki /⁠dakki⁠/ , “ resembles ” , 3rd person singular present active ) , 𒈭𒃷𒍣 ( ták-kán-zi /⁠takkanzi⁠/ , “ resemble ” , 3rd person plural present active ) and Ancient Greek δοκέω ( dokéō , “ think, suppose ” ) to this root. Kloekhorst rejects this in favor of *do k / ḱ h₁éy , *do k / ḱ h₁énti . [ 14 ] Beekes prefers to think of δοκέω ( dokéō ) as reflecting a deverbative derivation from δέχομαι ( dékhomai ) . [ 15 ] 
208: Proto-Italic: *dokeō Latin: doceō ( “ to inform, teach ” ) 
216: Latin: dignus 
267: ↑ 6.0 6.1 6.2 De Vaan, Michiel ( 2008 ), “ discō, -ere ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 172 
269: ↑ 7.0 7.1 7.2 7.3 De Vaan, Michiel ( 2008 ), “ decet ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 164 
271: ↑ 8.0 8.1 De Vaan, Michiel ( 2008 ), “ doceō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 176 
285: ^ Beekes, Robert S. P. ( 2010 ), “ δοκέω ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), volume I, with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , pages 344-345 
=== deks file ===
146: right ( side ) 
178: ↑ 2.0 2.1 De Vaan, Michiel ( 2008 ), “ dexter ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 168
```


## [2026-09-05T17:47:14.407Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c c28aafda30f87762.txt && sed -n '60,140p' c28aafda30f87762.txt"
}
```


### [2026-09-05T17:47:14.475Z] TOOL RESULT

```
8785 c28aafda30f87762.txt

 1.1 
 Pronunciation 

 1.2 
 Verb 

 1.2.1 
 Conjugation 

 1.3 
 References 

 Toggle the table of contents 

 دشن 

 2 languages 

 Magyar 
 Русский 

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

 د ش ن ( d š n )
```


## [2026-09-05T17:47:23.300Z] TOOL CALL #73: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/دشت/\" \"https://abadis.ir/fatofa/دشن/\" \"https://abadis.ir/fatofa/دکور/\" \"https://abadis.ir/fatofa/دخش/\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 113: Persian dašt/dašn/dekor/daxš, Mo'in + Dehkhoda entries\" 2>&1 | tail -2; done"
}
```


### [2026-09-05T17:47:32.025Z] TOOL RESULT

```
### https://abadis.ir/fatofa/دشت/
/home/sfmqrb/git/rishe/data/verification/sources/web/9f395963e411db5f.txt
### https://abadis.ir/fatofa/دشن/
/home/sfmqrb/git/rishe/data/verification/sources/web/886d2e818317b872.txt
### https://abadis.ir/fatofa/دکور/
/home/sfmqrb/git/rishe/data/verification/sources/web/386b3a8cbeb69241.txt
### https://abadis.ir/fatofa/دخش/
/home/sfmqrb/git/rishe/data/verification/sources/web/bffec1e9b70e9b1e.txt
```


## [2026-09-05T17:47:34.588Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9f395963e411db5f 886d2e818317b872 386b3a8cbeb69241 bffec1e9b70e9b1e; do echo \"##### $f\"; head -4 $f.txt; wc -c $f.txt; done"
}
```


### [2026-09-05T17:47:36.136Z] TOOL RESULT

```
##### 9f395963e411db5f
URL: https://abadis.ir/fatofa/دشت/
FETCHED: 2026-09-05T17:47:27Z
STATUS: 200
TITLE: دشت - معنی در دیکشنری آبادیس
25455 9f395963e411db5f.txt
##### 886d2e818317b872
URL: https://abadis.ir/fatofa/دشن/
FETCHED: 2026-09-05T17:47:28Z
STATUS: 200
TITLE: دشن - معنی در دیکشنری آبادیس
3857 886d2e818317b872.txt
##### 386b3a8cbeb69241
URL: https://abadis.ir/fatofa/دکور/
FETCHED: 2026-09-05T17:47:30Z
STATUS: 200
TITLE: دکور - معنی در دیکشنری آبادیس
5595 386b3a8cbeb69241.txt
##### bffec1e9b70e9b1e
URL: https://abadis.ir/fatofa/دخش/
FETCHED: 2026-09-05T17:47:31Z
STATUS: 200
TITLE: دخش - معنی در دیکشنری آبادیس
15083 bffec1e9b70e9b1e.txt
```


## [2026-09-05T17:47:38.383Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### دخش\"; grep -n \"دخش\" bffec1e9b70e9b1e.txt | head -25"
}
```


### [2026-09-05T17:47:38.443Z] TOOL RESULT

```
##### دخش
1:URL: https://abadis.ir/fatofa/دخش/
4:TITLE: دخش - معنی در دیکشنری آبادیس
6:دخش - معنی در دیکشنری آبادیس 
10: دخش
16: دخش. [ دَ ] ( اِ ) ابتدا کردن کار باشد. گویند دخش بتو است ؛ یعنی نخستین معامله با تست. ( فرهنگ اسدی ). آغاز و ابتدا بود. ( جهانگیری ) ( آنندراج ) ( از انجمن آرا ). آغاز کار. ( شرفنامه منیری ). ابتدا و آغاز کار و معامله با کسی باشد. ( برهان ). ابتدا کردن بود. ( اوبهی ) ( حاشیه فرهنگ اسدی نخجوانی ). سفته. دشت : دخش کردن ؛ دشت کردن. ( یادداشت مؤلف ). آغاز کار و معامله با کسی. ( فرهنگ فارسی ) : 
18:وین کار مرا با تو بود دخش. فرالاوی.
20:دخشم بتو است ارجو کم نیک بود فال . فرالاوی.
23:مکن روز با تاج و با تخت دخش. فردوسی ( از جهانگیری ).
25:مکن بر دل ما چنین روز دخش . فردوسی ( از جهانگیری ).
26: دخش. [ دَ خ َ ] ( ع مص ) آگنده گوشت شدن. ( از اقرب الموارد ). سطبر و درشت شدن. پرگوشت شدن. ( آنندراج ).
27: دخش. [ دُخ ْ خ َ ] ( ع اِ ) نوعی از ماهی بگفته ابن سیده ، یا همان «دخس » است. ( منتهی الارب ). 
44:تیره و تاریک: بکن آنچه خواهی و دیگر ببخش / مکن بر دل ما چنین روز دخش (فردوسی: لغت نامه: دخش ). 
67:3 - می توان به زیبایی برای فعلِ چندمعناییِ آلمانی "merken" از واژه یِ "دَخش، دَخشیدن" بهره گرفت؛ نیاز به یادآوری است که یکی از معناهایِ "merken"، "به یاد سپردن" است و از سوی دیگر ما گُزاره یِ "از دخشه هشتن" را در زبانِ پارسی میانه به معنای " از یاد بردن" داریم که در اینجا "دخشه" به معنای "یاد، یادواره" می باشد. همچنین واژه یِ "merken" با واژه یِ " مارک:Mark" به معنای " نشان" نیز همریشه می باشد. 
84: تنها با نگاه کردن به همین {دخش} پارسی می توانید به رَدی که پارسی بر زبان های دیگر جهان گذاشته است پی ببرید. بسیاری از زبان های اروپایی واژگانشان را از پارسی گرفته اند.
100:وین کار مرا با تو بوذ دخش
```


## [2026-09-05T17:47:56.170Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### دشن\"; sed -n '5,40p' 886d2e818317b872.txt; echo; echo \"##### دشت (first-sale sense)\"; grep -n \"نخستین\\|دشت کردن\\|معامله\\|دست راست\" 9f395963e411db5f.txt | head -20"
}
```


### [2026-09-05T17:47:56.253Z] TOOL RESULT

```
##### دشن

دشن - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 دشن

 دنبال کنید 

 لغت نامه دهخدا

 دشن. [ دَ ] ( اِ ) دستلاف ، که سودای اول اصناف باشد. ( برهان ) ( آنندراج ). معرب آن داشِن است. ( از منتهی الارب ).
 دشن. [ دَ ] ( ع مص ) بخشیدن چیزی را. ( از منتهی الارب ). اعطا کردن. ( از اقرب الموارد ). 

 فرهنگ فارسی

 ( اسم ) دستلاف فروش اول کاسب .
بخشیدن چیزی را . اعطا کردن . 

 گویش مازنی

 /deshen/ بریز بپاش

 پیشنهاد کاربران

 دَشن. راست. 
 ( ( # وندیداد - هَرَسُویتس وِرلَگ ) )

 در پارسی میانه 'دشن' به معنای سمت یا دست راست بکار می رفته و در واژه ی دشنه نیز دیده میشود؛ وارونه ی 'دشن'، 'هوی' است که معنای سمت یا دست چپ می داده است.

 منبع. عکس فرهنگ ریشه های هندواروپایی زبان فارسی

 دشن - دخش - یا اولین فروش یاسود و بخشیدن
دشن از بن ریشه هندواروپائی دک dek یا کرفتن ، در اوستا دخش سمت راست معنی هم میدهد که در انگلیسی واژه dexterity و ارتوداکس orthodox و در سانسکریت داکسیناس daksinas یا راست که در لاتین دوسره docere. یادشده. ( فرهنگ ریشه های هندواروپائی زبان فارسی، آریانپور )

 در متون پهلوی ساسانی به معنی" سمت راست" است.

##### دشت (first-sale sense)
50: ( ~. ) (اِ. ) ۱ - دستلاف . ۲ - پیش مزد. ۳ - (عا. ) فروش اول هر کاسب . ، ~ کردن نخستین بار پول گرفتن ، فروختن جنس اولین بار در هر روز. ، ~ کسی را کور کردن کنایه از: اولین بار فروش از او نسیه خریدن ، موجب کسادی کار او شدن .
56:نخستین پولی که کاسب و پیشه ور در آغاز کار روزانه از خریدار می گیرد، دخش، دستلاف. =دشتان 
144:زبان های ترکی�در چند مرحله بر�زبان فارسی�تأثیر گذاشته است. نخستین تأثیر زبان ترکی بر پارسی، در زمان حضور سربازان تُرک در ارتش�سامانیان�روی داد. پس از آن، در زمان فرمان روایی�غزنویان، �سلجوقیان�و پس از�حملهٔ مغول، تعداد بیشتری�وام واژهٔ�ترکی به زبان فارسی راه یافت؛ اما بیشترین راه یابی واژه های ترکی به زبان فارسی در زمان فرمانروایی�صفویان، که ترکمانان�قزلباش�در تأسیس آن نقش اساسی داشتند، و�قاجاریان�بر ایران بود. 
201: ریشه اصلی آن دست بوده، یعنی مانندکف دست صاف و هموار. اصطلاح دشت اول و دشت کردن که در بازار و بین کسبه، بسیار بکار می رود، از همین واژه گرفته شده و کنایه است از به دست آوردن اولین وجه نقد روزانه. همچنین است واژه مشت که به دست ( دشت ) بسته وگره کرده می گویند.
212:دست لاف. [ دَ ] ( اِ مرکب ) دشت. سفته. داشن. دشن. ( یادداشت مرحوم دهخدا ) . پولی که روز اول ماه یا روز اول سال به کسی دهند و آن را خجسته دانند و به فال نیک گیرند. || قلب �دست فال � است به معنی سوداو معامله ٔ اول. ( آنندراج ) . سودای اولی که استادان حرفت و اصناف کنند و آن را میمون و مبارک دارند. ( از برهان ) . سودای اول را گویند که از آن شگون گیرند و آن را سفته و دشن نیز گویند. ( جهانگیری ) : 
247: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد.
```


## [2026-09-05T17:48:15.890Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"دشن\\|دخش\" ARY_pages.txt | head -20; echo \"=== latin index ===\"; grep -n -i \"DEK\\b\\|DEKS\\|DEXTER\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-05T17:48:15.964Z] TOOL RESULT

```
189:می‌دهد که مردم ترکیه (و شاید مردم آذربایجان) از نظر زادشناختی (0138287109) فقط دارای سی.
3715:افغانی (پشنو) (/4024۸2): 2۸ ایرلندی کهن (/[3ل7] 0ا0): دشن
5879:سانسکریت (54(/5877): هعل7۸ ,1۸۲۷۸۹ پسگشت‌ها دشن اد
6217:پسگشت‌ها ندادن 331 دشن
6823:فرانسه (۴2(727): ندشن ۱ وا اد دی ی ۳
6907:لاتین (710م): دشن ای
7475:3 ,57816۸ ب80133 هلندی (/0076): ندشن ریما
7871:۸ | دخش, دشت (به چم *تکلیف". *شغل* *آغاز کار" "معامله‌ی اول*)
7872:فارسی (/(۳885]4): دخش, دشت (به چم تکلیف", شغل/ "آغاز کار", "معامله‌ی اول)
8248:برخی مستقدند که واژه‌ی "دشت" (یا آدشن") با واژه‌ی "دخش" به چم آغاز و "بتدا" و "تیره و تاریکه" (لغت‌نامه
8249:دهخدا: ۱۰۴۹۵) یکی است. حتی اگر "دشن" با راژه‌ی پهلوی 2۸8118 رابطه‌ای نداشته باشد رابطه‌ی واژه‌های
10925:ی , اسپاپابي (لاقاللم/ق): دشن ۷۱ لهستانی (/53(ا۳0): ان ده ۱
15951:اسپانیایی (5۳۸۸75): دشن لهستانی (52لا۳0): اسان در
=== latin index ===
8060:DESS (OLD IRISH) oS 5-4).2' DEXTER LATIN) 3
8067:ONIONS: (DEXTER) 263 ‘REFERENCES enthny
8068:SKEAT: (DEXTER) 167 “POKORNY, —SSO™S~*~S*~S~«S
8069:MALLORY: 140 BARNHART: (DEXTERITY) 274
```


## [2026-09-05T17:48:20.457Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '7840,7900p' ARY_pages.txt; echo \".....\"; sed -n '8220,8270p' ARY_pages.txt; echo \"=== page tags ===\"; awk 'NR<=8270 && /\\[pdf page/ {p=$0} END{print p}' ARY_pages.txt; awk 'NR<=7871 && /\\[pdf page/ {p=$0} END{print p}' ARY_pages.txt"
}
```


### [2026-09-05T17:48:22.338Z] TOOL RESULT

```
"۵
[pdf page 266]
دخت, دختر | ۲۶۷
اسلاری کهن: شیردادن.
چم این واژه در زبان آلبانی: شیرترش.
ٍ
ا
ارستایی (475374/4): دانمارکی (0۸2/1874): 3 دب ۱۱۸
01650۸ سرئدی (8178215): 2007
۱ پپلری (نماتله): ۰ 017 ,20177۸8 نروژی (/07775014/): 3 ی
ٍ کردی (80/5[7): 7 ,0177 هلندی (00762): ان ۷ درا
تخاری ۸ (۸ (4ل/7071۸): ۲۵۸ اسلاوی کهن (1شا5 674 #ناتل) 2ا0):
تخاری 8 (8 ۸4۸ل70727۸7): 7 ۰ ط8ط005117 ,018137
سانسکریت (54۸/50/7): 021 لهستانی (0/[54): ان ۱۸۵
اف 8ة 211117 روسی (/(7354): ۰ 20071881 ,200273
ارمنی ((40/80/1۸): 27 چکه (7ل28): 75 بش2۳
یونانی (072820): لیتوانی (۸۸]۵2تال7ل):
717۷0۸788۸ ,717۷02758 ۸ ش28۳5
گرتیکه (007[4/0): 0۸ لنونی (لتی) (0لفل ۰:7 01678
ایسلندی کهن 50/0/0۸14 صا0):
20۳ پسگشت‌ها . : ۸5
نورس کهن (۸0852 00): 230 7 ۸00520
ساکسونی کهن (//2400 ۰:01 00117۸ 52 (0۸16153787) مزر
فریزی کهن (۳۶4/0 صبا0):: 00073728 8( 052
آلمانی کهن ((5701۸ 470 012): 9 (0۸167771۳) :۸/۸۲25
تست 3 1106 80
آلمانی ۰.680۸0 تا 7 700878 5 (0۸68787) :0/05
انگلیسی کهن 80280 ص0): 5 (0۸611783) +57
200 برهان قاطع + ۸۶
انگلیسی (3ل5لا8۸0): ان ۷ ۱۱۳۹۹۵
[pdf page 267]
۸ | دخش, دشت (به چم *تکلیف". *شغل* *آغاز کار" "معامله‌ی اول*)
فارسی (/(۳885]4): دخش, دشت (به چم تکلیف", شغل/ "آغاز کار", "معامله‌ی اول)
7 0۸387
اس
ارستایی (۷ل42874):. . ,00680 ,0180588 ,018900
۸ ,228177۸ ,2۸3813 ,0۸8526 ایرلندی کهن (577ل#/-010): 21
پپلری (4۲7ا۳۸): آلبانی (14(0/(شلم: 701517,0855
6 0۸3577۸6
تخاری 4 (۸ 747 7077۸): 72 پسگشت‌ها گرد رن
خنی (27070/838): زرا 1 را ۳
سانسکریت (5۸(۷50777): : مر ها
17 328707 ,0۸82 ,3 133 هتقفتام ,1۵6 710قت2 ری
ارمنی (7ل072/82/14): 788۸881 ب۸ح327 برهان قاطع + ۸۳۷
یونائی (072520)+ 05070۸1 فرهنگ معین : ۱۳۹۸
لاتین (7700س): لفت‌نامه دهخدا: ۱.۳۹۵
بادداشت:
چم این و اجریشه در زبان سانسکریت : وضع» سرنوشت. َ
چم این و اجريشه در زبان لاتین : آموختن» آموزاندن,
چم این و اجریشه در زبان ایرلندی کهن : بهترین,
چم این و اجریشه در زبان آلبانی : برخورد کردن» ملاقات کردن.
چم این و اجریشه در زبان پرنانی : پذیرفت.
اوستایی (ل4287۸): 3 اد پهلری (1الم: ,0۸
پارسی باستان (۲8754۸1 صا0): 01۷۸ اوستی (0558716): 3
۹
[pdf page 268]
در دروازه / ۲۶۹
کردی (082130): 8۸۲ ,اج057 ب#(05 هلندی (0764): 3 راد
افغانی (پشت) (/4۳6[7۸/۷): اسلاوی کهن (ع۲7شا؟ تل#ناتتن طا0):
۸ بف0۸8 ,۷۸۹ اند
سانسکریت (5۸(877): 0۷98 لهستانی (۳07(3[7): رد
.....
کردی (1801374): 0 ۵ ((6(8) :28 مها
افقانی (پشتی) (0/1فت020): 0108821۸۸۲ 11346 ناه
سانسکریت (84(/8807): 2101۸0128 8 (8۸8۱6۷) ۸10
پونانی (08550): تلا برهان قاطع : ۸۶۸۶
رومانی (/742(فلان#): 01053۸7
بادداشت.
به احتمال زیاد علت وجود این واژه در زبان‌های آنجشت سانه‌ی يا لکان این است: واژه‌ی "دشمن" از فارسی په ‏
ترکی و از ترکی به این زبان‌های انطال یافته است. ۱
اوستایی (/478874): 0۸830۸ اسلاری کهن (70شا5 277076 0ا0): !
پهلری (4۲1ابز۳۸): 0۸811۸6 ,0۸5150۷ ۱ ,0882 ۱
سانسکریت (8۸4(/8077): روسی (/0فا155): نا نود ۱۱۱
سس لیترانی (200مناترم: ا
برنانی (0728): 087108 ,0870178805 8 ,05810۸8 ۱
لاتین (7107ما): ند ای هد ۱۱ ایرلندی کهن (ادلا صام): 25 ِ
گوتیکد (0077110): ولزی (57لع/): 0
0 ,۳۸1118۷۷۸ گالیکه (عللقهه): اد(
آلمانی کهن (05701۸2 ۲۲0 صا0): آلبانی (۸۸400قللم: 01
۸ ,2880 ان
: ۳
[pdf page 280]
ٍ دلیر / ۲۸۱
پبگشت‌ها ۸8۲2/5 63 (0878) :0/05
0 و۶00 7 (05783) 7
4 (02378773) و ی نا 140 40

۸/۸5/25 فرهنگ معین + ۶ و ۱۵۳۸
یادداشت:
چم این واژه در همه‌ی زبان‌های اپن فهرست (به جز فارسی امروزی): دست راست یا سمت راست» مهارت» ماهر.
برخی مستقدند که واژه‌ی "دشت" (یا آدشن") با واژه‌ی "دخش" به چم آغاز و "بتدا" و "تیره و تاریکه" (لغت‌نامه
دهخدا: ۱۰۴۹۵) یکی است. حتی اگر "دشن" با راژه‌ی پهلوی 2۸8118 رابطه‌ای نداشته باشد رابطه‌ی واژه‌های
اوستایی و پهلوی این فهرست با دیگر واژه‌های این فهرست مورد تایید همه‌ی پسگشت‌های در دسترس من است.
اوستایی (/4۷587۸: هلندی (ل007): 0 ۱
7 0۸387791 ات2۸88 اسلاری کهن (۲7۴ا5 #677نابت صا0):
پارسی باستان (/2ا2878 2ا0): 5 و2852
,0۸7157117۸ ,۸7811۸۸ ۸3۸33517-0 لهستانی ([0073): 12580
-0۸877 ,0۸0۸885 روسی (/(75314): دابا ان زرا
پهلری (۳۸]47): 3 دهاز لیترانی (۸0/1404لا777ا): دران ۱
کردی (0082015): 3 لتونی (لتی) (۵۸74/۷ل): هن ای (0
تخاری ۸ (۸ 7(للل707): پروسی کهن (//4ا99ن۶۶۷ 012): ۰ 02805
آقف158 بفالم718
سانسکریت (4۸577): پسگشت‌ها 5
سس سک زر رز
یونانی 0820 1 اند ۱:۷ 1 (0۸83) وی اب اد ۰
گوتبک (00777/2): ۸5 5 (۲8ه88) :۸1۲527215
آلمانی کهن ((6272(/۸ ۶۷/077 00): 313152 8
َ 017۸ 4 (5ه0۵۸) :0/0773
انگلیسی کهن (/8۸701/5 012): 5 (0۸35) 57
2۸ ,05۸3 4 (88۸۷8) ۸0
انگلیسی (80/01/80): اد ار
[pdf page 281]
۱/۸۲ دی دُمب
=== page tags ===
[pdf page 281]
[pdf page 267]
```


## [2026-09-05T17:48:46.621Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 141 (p.120) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==141' HRN.txt | grep -n -i \"daxs\\|dax\" ; awk 'BEGIN{RS=\"\\f\"} NR==141' HRN.txt | head -20"
}
```


### [2026-09-05T17:48:48.263Z] TOOL RESULT

```
=== HRN leaf 141 (p.120) ===
— 119 —
538. däh 'Sklave*, Diener (auch weiblich)'.
ai. dasä' 'Sklave, Knecht*.
539. däye *Amnie*, düiß^),
aw. vergl. daenu- 'Weibchen (von Tieren); phlv.
dayak 'Amme (vd. 15 (29) (Gl.); ai. [XrfA^-, dlidyaü
'saugen ; arm. dayeak 'Amme, Erzieher etc. (H. No. 78).
kurd. da^ dl, diyä 'Mutter*, drUn Mutter, Amme*,
däye (LW.); af/. LW. däyT; oss. d. däyim, t. däin
'saugen (103); bei. LW. dai (53).
540. dehlr, dibtr 'Schreiber', n^DI (Jer. 36, 10) aber nxn,
HNVn (Ezech. 9, 2, 11).
Nur in seiner Bildung vielleicht persisch; vergl.
aber Jensen, WZKM. VI (im Druck).
ap. vergl. LW. dipi- 'Schrift'; präkr. dipi-, lipi-
(Agöka-Inschriften) ; phlv. d(i)pioar (Hörn, ZDMG.
44, 670 No. 111), d(i)pTr, d(i)pTrih (PPGL), daneben
d(i)blr (Inschr.); arm. LW. dpir^ talm. ^''Dl, daßtiQ
(LXX).
Die Form np. diiwer der Wörterbücher, die zu päz.
```


## [2026-09-05T17:48:48.566Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC dek ===\"; grep -n \"deko\\|dek-\\|dekso\\|dekṡ\" IEC.txt | head -10; echo \"=== LEW doceo ===\"; grep -n \"doceo\\|decet\" LEW_1910.txt | head -5; echo \"=== LAT dexter ===\"; grep -n \"dexter\" LAT.txt | head -5; echo \"=== SKT dexter ===\"; grep -n \"dexterity\\|Dexterous\\|dexter\" SKT.txt | head -5"
}
```


### [2026-09-05T17:48:48.668Z] TOOL RESULT

```
=== IEC dek ===
2132:cency.. cf. deko cf. Lat. decus, óris “honour” beside decor, óris “handsome” (-r- not certainly original); Umb. cf. tekvias, npl. f. “due to receive gifts’; OHG ziari ‘beauty, ornament! beside ziari *adorned'; G Zier; OS tir “honour, fame; OE tir, id. (& *ornament); cf. denom. vb. in Lat. decoró, are: OHG ziarón
2135:deKo, io ‘find, get; deem, judge’. WP I, 783. Cf. deKs- Av. das- ‘possess’; dasan ‘possession’; Tokh. A täk- ‘decide, judge’; Myc. cf. dekasato (:Gk. edæxato); Gk. dékomai, beside dektós ‘agreeable’; Lat. decet; Umb. Get “is allowed’; Osc. cf. deketasis (title of a judge); cf. dek- manni(s) ‘paying member of a club’; MHG cf. ge-zéchen, OHG gi-zehon ‘arrange’; OE teohhian, v. *determine, judge' beside tióian (for tigóian *bestow"); OCS dešọ, desiti ‘get, find’. A possible long-gde occurs in Skt. dāśāmi, dāśmi & da$nómi ‘worship; bestow’. See next
2136:deKos, a ‘fit, fitting; fitness. Cf. deKo E deKsos. WP I, 784 Skt. da$a (2) “state, condition’; Lat. decus ‘grace, honour’; Mir dech "best: MHG cf. z&che “social status? G Zeche 'guild'; MHG ge-zëch “joined, arrange” (see deko above.
2148:deKsinos, dekKsiteros, deksitos, deKsiuos ‘right-hand’. WP I, 784 (1) Skt. dáksinab; Av. daSino; OCS desto, Srb. desni, R desnój; Li. deSinas (2) Gk. dexiterós; Lat. dexter, f dextra; Umb. destra-, f.; MIr. desreth, desred, s. (3) Alb. i djathét; OIr. dess; MIr. deas, adj. deissi, s.; (4) Myc. dekisiwo- *deksiwo-; Gk. dexiós; Umb. tesva-; Late Umb. dersua- (favourable! for *de$wa-); Sequanian cf. priou-dixivos (— Skt. pürva-daksinah 'south- east); Gaul. dexivo-; OBr. deh-; Br. déu, dé- hu, dihu; W deheu, deau ‘right-hand, south’; Go. taíswa; OHG zëso, gs zésawer; MHG zësewer, f zésewe, id. (‘the receiving hand. Cf. dek-)
2149:deKso (variant of deko, q.v.) “receive, get; meet, find’. WP I, 783 Skt. daksami 'satisfy; Myc. cf. dekasato *deksato', 3s mp; Gk. déxomai; Olr. cf. dess ‘ust’; W cf. dais, pl. deision ‘desire’; OE cf. tese ‘comely, suitable; OCS dešọ, desiti (find, eet Ambig. cf. deKó).
17788:süb- (3) “scale, skin” Umb. supa, f. ‘skin’; W hif, pl. -ion, m. “skin, surface'; Latv. süba, f. “scale, patina'; sübu, et, v. “form a scale’. (For Umb. supa for *suba, cf. tuplak, tekuries, for *du-, dek-); Lat. cf. süber, gs: -eris (for *sübus, gs: -eris, n. — as Lat. later for latus — 'cork?). (For Gk. süphar see tübhor-)
=== LEW doceo ===
=== LAT dexter ===
3179:sur le modele de ajxcpoSouC; ambidexter est une transcription tardive
4130:sunt postica dicuntur, et dexteram anticam, sinistram posticam dicimus.
16480:dexter, -tera, -teri* (-tra,-trum): 1 ' osco-oabrien ne connait que
16481:les foraes sans e, oabr. testru-ku destru~co, destram-e "ad dexterna,
16482:in dexteraa", osq. destr-st "dextra est". En latin, les foraes pleines
=== SKT dexter ===
8336:hA&dBomfi.  vE.)  M.  K.  AauJium,  one. tractable,  or  dexterous.  *  A.  S.  Man  J,  hana  ; 'SHm,  su(iFix.as  in  n'jivj'wm,  winsome.  •^Du. hoHfitaam.  tractable,  serviceable.
8337:handy  (i\  dexterous.  (E.)  M.  E. kendi  [never  Aandi).  A.  S.  heutiig,  skilful : forined  from  hand,  hand,  with  raflix  tg and  vowel-change.  +  t>ti>  handig,  Dan. handig,  bfhtFndig,  Swed.  hdndig,  dextcroos ; Goth,  handugs,  clever.
15808:adroit  (F.  -I*)  F.  adroit,  dexterous. -F.  <J  Jrvit,  rightfully. -F,  /)  {h.  ad),  to; Low  L.  dirttinm,  right,  joslice.  ocut.  of dirtctM\  see  diroot  (below).
17474:eleight,  dexterity.  (Scand.)  Put  for $teishth  ;  M.  E.  sUightht.  -  Icel.  slag^,  sly- ntsg,  cunning.  —  Icel,  slagr,  sly.  So  also Swed.  j/J*^,  dexterity,  from  slog  dexterous, aly.  cunning.  (Scuid.)  M.  £.  slU.  — Icel.  xAf^,  sly,  cunning ;  Swcd.  i/i^;  Dan. tiug,  tiu ;  G.  scklau.  We  also  hnd  Swed. iVog,  dexterous.  Icel.  slagr,  kicking  (as  a horse).  Allied  to  Slay ;  cf.  G.  vtrstklagtH. cunning,  crafty,  sly.  Oiig.  *  dexterous  with the  hammer.'    See  also  Slattern,  Sleel.
```


## [2026-09-05T17:48:56.250Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==142' HRN.txt | head -40"
}
```


### [2026-09-05T17:48:58.103Z] TOOL RESULT

```
- 120 —
542. de^S 'üeschäft, Mühe'.
ai. daksd' 'Tüchtigkeit, Tauglichkeit, Fähigkeit'
(Nöldeke, mündliche Mitteilung).
Die Bedeutung ^Geschäft, Mühe' passt für die
sämnitlichen bei V uliers s. v. mitgeteilten Beleg-
verse; 'finster' ist in den citirten Sähnämevers erst
künstlich hineininterpretirt.
543. deyinif de/me 'Dakhma (der Pärsen); Grab* (bei
Firdüsl auch immer nur zoroastrisch).
g. demd,
aw. da/tna-; phlv. da/mak, da^tn,
544. ded, dede 'Raubtier, wildes Tier.
aw. daitika- wildes Tier (Geldner, KZ. 28, 400;
aber sehr zweifelhaft, vergl. Baunack, Studien I,
385 folg.); phlv. dattk (ys. 39, 2 (4)), datak (AV.),
dal (Men.).
545. (\)der 'Tür*; :^n (Is. 3, 26); vergl. derbar^), derhan,
derwäze.
g. bar; Semn. bart; Käs. bar, ber; Vullers ber
wird auch dialektisch sein-).
ap. duvar- Tür*, duvarayä ; aw. dvar- ; phlv. dar,
dargas; ai. dvdr-^ duräs; arm. durn 'Tür (H. No. 86).
kurd. bar {der^ deri); af/. var; oss. dvar (114);
wa/. bär^ sar. divir, §iyn. dive, divSr, minj. labra,
546. {2)der Praeposition a) 'hinaus, draussen.
kurd. bar 'draussen ; bei. LW.(?) dar, dara 'draussen,
ausserhalb, hinaus' (72); lat. foras, foris.
Nominale von "^dvaram 'nach der Tür hin d. h.
'hinaus gebildete Praeposition. Vergl. berün (No. 252).
b) 'hinein, darin', derün.
phlv. dar, vereinzelt AV. (sonst immer pD).
An die allgemein angenommene Verkürzung aus
ender (No. 119) mag ich nicht gern glauben, ebenso
wie np. tä auch nicht aus päz. andak (s. No. 366)
Phlv. darhär? Vergl. Nöldeke, Kärnämak, 57 Note U
?) Arni. L^\ bar (Hübschmanp ZDMG. 35, 128),
```


## [2026-09-05T17:49:09.522Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^doctor\\|doctor (\" SKT.txt | head -3; grep -n \"orthodox\" SKT.txt | head -3; echo \"=== LAT decet/doceo ===\"; grep -n \"^doceo\\|doceo,\" LAT.txt | head -3; sed -n '16480,16495p' LAT.txt"
}
```


### [2026-09-05T17:49:09.660Z] TOOL RESULT

```
11915:Moslem,  a  Mussulman.  (Arab.)  Arab. moslim,  *a  mnsulmao,  a  true  believer  in the  Mohammedan  faith ; '  Richardson.  Cf. Arab.  mtualUm,  oat  who  aoqniesces.  A mussuiman  is  one  who  professes  ii/dm, i.  e.  submission  to  the  will  of  God  and  to the  orthodox  faith. —  Arab,  sa/ama,  to  sub- mit %  The  E.  words  mosUm,  mussuiman, islam,  and  talaam  are  all  from  the  &ame Arab,  root  satama,  to  submit.
11916:mussuiman,  a  true  believer  in  the Mohammedaa  laith.  (Fers.  — Arab.)  Pers. musuhndn,  an  orthodox  believer.  — Arab. mcsiim,  ptuiiim  (above).
=== LAT decet/doceo ===
17387:doceo, -es, -ul, doctum, -ere; causatif k vocalisme o (cf.moneo
17414:theses sur la fayon dont le sens a £volu£ dans doceo, d'une part, et
17417:doceo s 1 est trouv£ aupres d'un present athematique et confirme le
dexter, -tera, -teri* (-tra,-trum): 1 ' osco-oabrien ne connait que
les foraes sans e, oabr. testru-ku destru~co, destram-e "ad dexterna,
in dexteraa", osq. destr-st "dextra est". En latin, les foraes pleines
et les foraes sans e se rencontrent indiffereaaent k tontes les ^poqnes:
les secondes seablent pina frequentes, snrtont k l' 4 poque iap^riale;
d'ailleura chez les dactyliques, tontes les foraes pleines foraant
cr 4 tiqne, dn type dextSri, etaient exclnes. N 4 anaoins le coaparatif,
atteste k partir de Varron, est toujours dexterior, cf. Thes. V 9*0,
49sqq. Snperlatif archalque dextimus, trbs rare, et non attest 4 aprbs
Sallnste (correspond k sinistimus); dexterrimus dans Palladins. Sens:
i° droit, par opposition k sinister "ganche", ce qni expliqne la forae,
cf. gr. 8 eJ;i.TSp 6 c k cote de Senios; d'oi dext(e)rd "i droite" adverbe,
enploye quelquefois coaae pr^position (de aeae qne sinistra), snr le
aodfele de extra, etc., cf.Wackernagel Vorles. II 315; 3 ° qni rient dn
cote droit, en pariant des pr^sages, d'oi "favorable": P.F.65,6, dextera
auspicia, prospera (cf. tontefois nne trace de la croyance contraire
```


## [2026-09-05T17:49:27.253Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 404 405 406 407; do echo \"--- leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | grep -oE \"^70[0-9]$\" | head -3; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | grep -oE \"dasina[^ ]*|dasin\" | head -3; done"
}
```


### [2026-09-05T17:49:29.182Z] TOOL RESULT

```
--- leaf 404
700
--- leaf 405
703
704
--- leaf 406
--- leaf 407
706
```


## [2026-09-05T17:49:31.630Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==405' BRT.txt | grep -n -i \"rechts\\|dasin\\|dain\" | head -10"
}
```


### [2026-09-05T17:49:33.056Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:49:35.707Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==405' BRT.txt | head -40"
}
```


### [2026-09-05T17:49:37.195Z] TOOL RESULT

```
  1  andeutlich  »).  —  i)  Wegen der  BedetttDug  s.  k»L  diiiü  and  ai.  -uidas-  n. •Habe'  in  vüidiä.  —  ')  Dst.  ZA.  3,  196  liest xait,  aber  bei  Sp.  steht  dnddt;  vU.  stand  in der  Urschrift  n  ddt,  d.  i.  visi  ^  «i.  viiiä-  n.; die  Erseliang  von  n-  durch  dn-  ist  ja  häufig. '10'  (Ggr.  OK.  346)   will  sicher  auch  die  Pü.
•  j.  dasa.gäya-  n.  'Längenausdehnung von  zehn  Schritten,  zehn  Schrittlängen': äat  tum  .  .  apa.bar5i!  'gäim  haca  mnbyS asavabyS  V,  J7. 4,
Pü. :  10  gim.
•  j.  dasad^'vant-  Adj.  (fem.  °vaitl-)  'reich an  Besitz,  Hab  und  GiKC :  fravasayö  . .  yä . .  'vainf  Yt.  13.  ap.
Ableit.  aus  'diuaia-  n.;  mm  ksl.  V.  deii/i finden';  vgL  dasa-,  däsla-,
•  j.  dasa.mähya-  Adj.  'zehn  Monate dauernd':  yai. .  näirika  upas.pu'hfXm  jasat aivS.m3hTm  vä  .  .  °hXm  vä  "wenn  eine Frau  in  die  Schwangerschaft  kommt  auf die  Dauer  von  einem  Monat  .  ■  oder  von zehn"  V.5.45.
Ableil.  aus  *dasa.maA.  m, ;  s.  Wh.  Gr.'  %  iai2  c. —  ai.  daiamätya-  Adj.  'lehn  Monate  alt'  (vom reifen  Embryo).  —  PiL :  /O  ntähak.
•  j.  dasama-  Adj.-  'der  zehnte';  akmat haca  garayS  fraoxiyan  .  .  "mS  antan.-  \ tia1ihMtYt.1g.2-,  i.Z,'i4-^l,  Y.14.1);  —  : yexi  'm^mfASni.)  fi-äTitaoiti  näu?n>m paiti.- raihwayeiHV.S.iZ;  28;  —  •»«/«  (ASn.) asafghqmca  .  .  V.  /.  1  a ;  —  *'mahe  F.  i.
Ableit.  ans  daia  Im.  —  ai.  daiamä-  Adj.,  np.
Jaikum.  —  Pü.;  dakum.
j.  äaila,  dasli  (Verbatf.),  daiti:  5.  >i/J-. •  j.,  g.  daste  Inf.  i)  'zu  geben,  zu  ver- leihen': aiiqm  tut  ahurä  Shmä  pouruUmäis 'fe  "durch  deren  recht  viele  wollen  wir' dir,  o  Ah,,  (sie)  uns  zu  verleihen  Anlass ! geben"  Y.  34. 1  ">.  2)  'etwas  (Akk.)  zu ' machen  zu  — '  (Instr.  statt  Akk.) :    *'v?r3Z- 1
\yatqm  ("So  vohu  väsitya  (sd.)  uyamna  (sd.) anuyamnäii  'le  Vr.  i^.  i  *'.
Zum  Praes.  53)  des  V.  da-,  uiw.  laatgeseti- lich  zu  ar.  •oH-.  —  Pü.  (zu  V,):  ßiae  äiän  e 15  .  ,  atnäi  pfUar  dahim;  (zn  Vr.);  dät.  — ')Vgl.zStBTHL.  IF.5.  366.  — »>  Die  Fassung der  Stelle  bei  Gdn.  KZ.  30.  516,  Jn.  JAOS. 14.  cci  scheint  mir  aas  syntaktischen  Gründen unmSgltch.  —  3)  S,  aber  daidar-  No.  3.
•  j.  dasma-,  g.  das^ma-  m.  'Darbringung*: ysi  vf  yeih?m3(sd.)  'ml  stütam  Y.  2Ä9; verwendet  Y.  11.  9:  Sme  yH  vi  yai^- ma.  [F./:  lies  das)mahe.]
KompE.  —  ai.  Tgl.  ddiati,  daiasyäti;  Bthl. AF.  3.  1471).  —  Pü.:  dahtl,  aber  in  Y.  ir: dahtAnn,  s.  zu  *rH»ndäidyäi.  —  1}  Falsch JuSTl  NB.  491 ;  ar.  *dhadzhma-  wäre  gAw. "dauma.;  %  $3  I.  8. j.,  g.  dasT/ä:  E.  'du:
•  j.  dasvar-  o.  'Gesundheit',  nur  in  Ver- binduDg  mit  (folg.)  batsaza-  n.  'Heiltum': 'varfca  baisazfmca  V.5. 53;  —  ni  'van nl  baltazim  (näml.  mruyt)  Y.  p.  1 7 ;  71. 1 7, Vr.  20,  I,  Vyt_35; —  ci^nm  'van  baesa- stm  Y.  70. 7;  *FrW.9.  2";—  'varp  (statt AD.)')  baliaza  äfrfnämi  Y.6S.i$;  — *'varii*  (statt  des  Instr.)"  . .  ba^asa  Y. 55.3;  —  'van  (statt  des  Dat.)''  baisa- zäUa  Y.  6S.  2.
Et?  Vgl.  däsma-m-.  —  Bed,  nach  Pü.  —  Pü.: druslihi&i.:  surüpattiam,  saunäaryam. —  i)  Hds. 'var>in,  was  auch  als  Var.  zu  Y.  p.  17,  ro.  7, Vr.  lo.  I,  34.  I  vorkommt.  Vgl.  No.  1.  — ">  Man  hat  sich  begnügt,  die  syntaktische  Be- ziehung beim  zweiten  Wort  zum  Ausdruck  zu bringen;  vgl.  za  un/ä%ä-.  —  3)  NA.  "vara;  s. aber  No.  z  und  Var.
•  g,  dazdar-  m.  'der  etwas  hinsetzt,  -bringt zu  — '  (Dat.)'':  ya'^ä  ahü  (sd.)  .  .  varahsut
manaiahB  ^aohaiianqm  anhSus mazdai  xsa&nmcä  ahuräi  a  yim  ''dn- gubyö  (sd.)  , .  ". ,  der  des  guten  Sinnes Lebenswerke  dem  Masdäh  zubringt  und (so)  die  Obergewalt"'  dem  Ahura,  er, den  .  ."  Y.  27. 13"'.
*)  Das  AhunaVaityaG^ti  ist  zuletzt  von FrMOllbk  WZKM. //.  ii;  behandelt  worden-, der  auch  Litt  angibt;  dazu  noch  HBH.  KZ.  27. 102,  Bn.  Slud.  I.  30^  West  SBE.  ^.  S  -  und von  Ludwig  SBöhmGW.  /iJp/.  xxxi.  Ich  bleibe im  Wesentlichen  bei  meiner  AufTassnng  in  AF. 3.  47  stehen.  Dadurch,  dass  bei  der  schliest' liehen  Abrechnung  die  guten  Werke  überhaupt die  bösen  überwiegrn,  wird  der  Sieg  der  lyri- schen Welt  über  die  ^aÄische  gesichert,  ihr Übergewicht  beim  Einzelnen  sichert  diesem  den verheissencn  Lohn.  Zan&uilra  sorgt  als  'Ober- Herr'  {'ahi,-)  dafiir,  dass  von  des  Gläubigen  guten Werken  keins  verloren  gehe,  sondern  gebucht
ob,Google
703
dazdyli
'dahma-  A
704
Dnd  in  AkM^  'Hans'  Tcrwahrt  werde-  i.  dam-\ mit  No.  3,  'pä^y  mit  No.  4  -,  wUuend  er  «Is  1 Richter  {ralav-)  die  eDdeiltiKe  Ohnniacbt  der  | .ZVH«"Welt  fesutetlt  und  die  endeiltige  Hemcluft  i AkM^  I
Zum  Pnes.  5  3)  des  V.  da-,  diw.  lautgeseUlich m  M.  V*ä-,  —  Pü.:  äahihi;  s.  iPö.  dei  Ge- ' bei»  HAU
```


## [2026-09-05T17:49:47.435Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'rechts\\|„rechts\\|,rechts\" BRT.txt | head -10"
}
```


### [2026-09-05T17:49:47.485Z] TOOL RESULT

```
6302:•  j.  *asa'vaat-'*  Adj.  i)  'rechtschaffen' (nur  Ableit).  i)  'der  das  (höchste) Anrecht  a)  besitzt':  haurvafsavS  .  .  drvä Maurva  -vantö  (NP.)  Y.jÄiS.  b)  'ver- schafft':  hadiiasca  (sd.)   'vaiS  vOstravatS
```


## [2026-09-05T17:50:46.200Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m2 -A3 \"docere\\|doctor (n\" 41609e3ed6a29a7d.txt | head -20; echo \"=== orthodox ===\"; grep -n -m2 -A3 \"orthodoxos\\|orthodox (adj\" a77f12fde6a91ab1.txt | head -20; echo \"=== dekor ===\"; grep -n \"فر\\.\\|décor\\|فرانسه\" 386b3a8cbeb69241.txt | head -10"
}
```


### [2026-09-05T17:50:46.284Z] TOOL RESULT

```
23: doctor (n.) 
24-
25: c. 1300, doctour , "Church father," from Old French doctour and directly from Medieval Latin doctor "religious teacher, adviser, scholar," in classical Latin "teacher," agent noun from docere "to show, teach, cause to know," originally "make to appear right," causative of decere "be seemly, fitting" (reconstructed to be from PIE root *dek- "to take, accept").
26-
27- The meaning "holder of the highest degree in a university, one who has passed all the degrees of a faculty and is thereby empowered to teach the subjects included in it" is from late 14c. Hence "teacher, instructor, learned man; one skilled in a learned profession" (late 14c.).
28-
=== orthodox ===
23: orthodox (adj.) 
24-
25: mid-15c., in reference to theological opinions or faith, "what is regarded as true or correct," from Late Latin orthodoxus , from Greek orthodoxos "having the right opinion," from orthos "right, true, straight" (see ortho- ) + doxa "opinion, praise" (from dokein "to seem;" from PIE root *dek- "to take, accept").
26-
27- Of other subjects than religion or theology from 1640s. Meaning "of or pertaining to the Greek Church," by 1772. In reference to a branch of Judaism, recorded from 1853; as a noun meaning "an Orthodox Jew," by 1889.
28- also from mid-15c. 
=== dekor ===
29: (دِ کُ ) [ فر. ] (اِ. ) ۱ - مجموعة اشیاء و اثاثیه در صحنة نمایش و مانند آن . ۲ - مجموعة وسایل و اثاثیة خانه .
```


## [2026-09-05T17:50:49.914Z] AGENT

Now I'll write the verification file.


## [2026-09-05T18:00:10.519Z] TOOL CALL #88: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk113.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_DEK  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deḱ-\"\nW_DEKS = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deḱs-\"\nW_DEX  = \"https://en.wiktionary.org/wiki/dexter\"\nE_DOC  = \"https://www.etymonline.com/word/doctor\"\nE_ORT  = \"https://www.etymonline.com/word/orthodox\"\nA_DAST = \"https://abadis.ir/fatofa/دشت/\"\nA_DASN = \"https://abadis.ir/fatofa/دشن/\"\nA_DEKOR= \"https://abadis.ir/fatofa/دکور/\"\nA_DAXS = \"https://abadis.ir/fatofa/دخش/\"\n\ndoc = {\n \"pdf_page\": 113,\n \"book_page\": 83,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": []\n}\n\n# ------------------------------------------------------------------ entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Dek\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *deḱ- 'to take, accept, receive' (Pokorny 1. deḱ- 189-191; Watkins dek-1)\",\n \"note\": (\"The root box is right. Pokorny I 189-191 heads the lemma '1. dek- ‚nehmen, aufnehmen’, daher \"\n   \"‚begrüßen, Ehre erweisen’' and derives from 'annehmen, gern aufnehmen' the further senses \"\n   \"'gut passend, sich schicken, ziemen … lehren, lernen' — so Nourai's added gloss 'understand' is a fair \"\n   \"rendering of the causative branch (doceō, dokéō), not an invention. Watkins/AHD dek-1 'to take, accept' \"\n   \"[Pok. 1. dek- 189] and Wiktionary *deḱ- 'to take, to perceive' agree. The one real problem on this chart is the \"\n   \"Avestan/Persian branch (nodes #1-#2): Pokorny p.189 and Walde-Pokorny I 784 — the two pages Nourai cites for it \"\n   \"— expressly REMOVE Av. daxš- and NP daxš from this root because of the guttural.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *deḱ- «گرفتن، پذیرفتن» (پوکورنی صفحهٔ ۱۸۹–۱۹۱، وتکینز dek-1) درست است؛ \"\n  \"از معنای «پذیرفتن» معناهای «زیبنده بودن، آموختن، آموزاندن» پدید آمده است، پس افزودنِ «understand» از سوی نورایی بی‌پایه نیست. \"\n  \"امّا شاخهٔ ایرانی این نمودار (گره‌های ۱ و ۲) پذیرفتنی نیست: خودِ پوکورنی در همان صفحهٔ ۱۸۹ و والدهٔ–پوکورنی در جلد ۱ ص ۷۸۴ \"\n  \"«اوستایی daxš-» و «فارسی دخش» را به سبب واک پسین (گوتورال) از این ریشه بیرون می‌گذارند.\"),\n \"sources\": [W_DEK, E_DOC],\n \"ref_check\": [\n   {\"ref\": \"POK:189\", \"status\": \"supports\",\n    \"note\": (\"POK_01.txt line 2730 (printed p.189): '1. dek- ‚nehmen, aufnehmen’, daher ‚begrüßen, Ehre erweisen’ … \"\n             \"dekos- n. ‚Zierde, Ehre’'. The lemma runs pp. 189-191 and contains both the Latin/Greek material and the \"\n             \"deḱs- 'right' section, so the page number is exact.\")}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 782-784 (WLD_Bd1_1930_dli_70244_djvu.txt, printed marker '784' visible)\",\n    \"stance\": \"supports\",\n    \"note\": \"The lemma 'dek-' with ai. daćas(yati), lat. decet/decus/dignus, gr. dokéō, lat. doceō, discō — the same material Nourai charts.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dek-1 (AHD_watkins1985.txt line 362)\", \"stance\": \"supports\",\n    \"note\": \"'dek-1. To take, accept … [Pok. 1. dek- 189.]' with DOCTOR, DOCUMENT, DECENT, DISCIPLE, DISCIPLINE, DECORATE, DIGNITY, HETERODOX, ORTHODOX, PARADOX.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. deḲo, io (IEC.txt line 2135; WP I,783)\", \"stance\": \"supports\",\n    \"note\": \"'deḲo, io ‚find, get; deem, judge’ … Gk. dékomai … Lat. decet' — same root, no Avestan daxš- in the list.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 17.25 TEACH / 17.27 TEACHER (SYN.txt lines 30777-30903)\", \"stance\": \"partial\",\n    \"note\": \"Buck lists Av. daxš-/fra-daxš-tar under 'teach', but writes 'etym. dub. Walde-P. 1.784. Barth. 676.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. decent / doxastic (KLN_1966.txt lines 10494, 12181)\", \"stance\": \"supports\",\n    \"note\": \"'I.-E. base *dek-, *dok-, ‚to take, receive, accept; acceptable, becoming, good’, whence also L. decere' with the whole English family listed.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"daxš 1; fra-daxš-tar; daxšta\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The three Avestan forms themselves are real and correctly identified. Bartholomae AiW col. 675 has 'j., g. daxš- V. \"\n   \"‚lehren’ … ‚lehren, unterweisen’' (OAv. daxšaṯ Y 43.15; YAv. aðaxšayaeṯa Y 12.5), and with the preverb fra- \"\n   \"'fraðaxšayā' Y 33.13; the agent noun fra-daxštar- m. 'Lehrer, Unterrichter, Unterweiser' stands at AiW col. 982 \"\n   \"(Y 45.17, Y 51.3), which is Nourai's 'fra-daxš-tar : teacher'. But daxšta- is NOT 'knowledge, tool': AiW col. 677-678 \"\n   \"gives 'daxšta- n. ‚Zeichen, Kennzeichen, äusseres Merkmal’', specialised to the menstrual sign (daxšta-vaitī- \"\n   \"'menstruating'), whence MP daštān and NP دشتان; Cheung 2007 s.v. *daxš glosses it 'sign, revelation'. \"\n   \"The real problem is the arrow itself. Pokorny p.189, the page Nourai cites, explicitly excludes these words: \"\n   \"'aber av. daxš- ‚lehren, unterweisen’, npers. daxš ‚Geschäft, Mühe’ bleiben wegen des Gutturals fern' — the \"\n   \"-xš- of daxš- presupposes a plain (or labialised) velar, whereas *deḱ- has a palatal *ḱ which would give Avestan \"\n   \"-s- (cf. dasta-, dāšta-). Cheung 2007: 40-41 accordingly sets up Iranian *daxš 'to show, teach, reveal, mark' from \"\n   \"PIE *dekʷs- 'to show' (LIV 112), the labiovelar being guaranteed by Hittite tekkušš- 'to make known, show'. \"\n   \"So the Avestan box is a separate, homophonous-looking root, not a descendant of *deḱ- 'take'.\"),\n \"derivation_fa\": (\"سه صورتِ اوستایی درست‌اند: daxš- «آموختن، آموزاندن» (بارتولومه، ستون ۶۷۵)، با پیشوند fra- و پسوند کننده‌سازِ -tar: \"\n   \"fra-daxštar- «آموزگار» (ستون ۹۸۲، یسنا ۴۵؍۱۷ و ۵۱؍۳). امّا معنای daxšta- «دانش، ابزار» نیست؛ بارتولومه (ستون ۶۷۷) آن را \"\n   \"«نشان، علامت، نشانهٔ بیرونی» می‌آورد که در فارسی میانه daštān و در فارسی «دشتان» شده است. ایراد اصلی بر همان پیکانِ ریشه است: \"\n   \"پوکورنی در همان صفحهٔ ۱۸۹ می‌نویسد «ولی اوستایی daxš- و فارسی دخش به سبب واک پسین بیرون می‌مانند»؛ زیرا *ḱ کامی در اوستایی s \"\n   \"می‌دهد نه xš. چونگ (۲۰۰۷) نیز ریشهٔ ایرانی *daxš «نمودن، آموختن» را از *dekʷs- هندواروپایی (با گواهی هیتی tekkušš-) می‌گیرد، نه از *deḱ-. \"\n   \"پس پژوهش امروزی این پیوند را رد می‌کند.\"),\n \"sources\": [W_DEK],\n \"ref_check\": [\n   {\"ref\": \"POK:189\", \"status\": \"contradicts\",\n    \"note\": \"POK_01.txt line 2730 (p.189): '(aber av. daxš- ‚lehren, unterweisen’, npers. daxš ‚Geschäft, Mühe’ bleiben wegen des Gutturals fern)'. Nourai cites the very page that denies his arrow.\"},\n   {\"ref\": \"WLD1:784\", \"status\": \"contradicts\",\n    \"note\": \"WLD Bd. I p.784: 'Aber av. daxš- ‚lehren“, sowie np. daxš- ‚Geschäft, Mühe“ bleiben fern (Gutt.! s. Uhlenbeck Ai. Wb. 119)'.\"},\n   {\"ref\": \"SYN:1227\", \"status\": \"partial\",\n    \"note\": \"Buck §17.25 TEACH (SYN.txt line 30811): 'Av. daxš-, esp. cpd. fra-daxš-, etym. dub. Walde-P. 1.784. Barth. 676.' — the words are there, but Buck calls the etymology dubious and points to the same WP page that rejects it. §17.27 TEACHER: 'Av. fradaxštar-, fr. fra-daxš- ‚teach’. Barth. 982.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 675 (daxš-), col. 677-678 (daxšta-), col. 982 (fra-daxštar-)\", \"stance\": \"partial\",\n    \"note\": \"'j., g. daxš- V. ‚lehren’ … ‚lehren, unterweisen’'; 'daxšta- n. ‚Zeichen, Kennzeichen, äusseres Merkmal’'; 'fra-daxštar- m. ‚Lehrer, Unterrichter, Unterweiser’'. Forms confirmed, gloss of daxšta- differs from the chart.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *daxš (CHEUNG.txt lines 5567-5620)\", \"stance\": \"contradicts\",\n    \"note\": \"'*daxš ‚to show, teach, reveal, mark’ … Av. daxš- ‚to instruct, show’, daxšta- … ‚sign, revelation’ … also YAv. fradaxštar- ‚teacher’ … PIE *dekʷs- ‚to show’ … the velar of the IE root *dekʷs- must have been labialized. > LIV: 112 | Pok.: 189.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. daxšag (PHD.txt line 310)\", \"stance\": \"partial\",\n    \"note\": \"'daxšag [dhšk! | M dxsg] mark, sign, characteristic; memory' — the Middle Persian continuant means 'sign', not 'knowledge/tool'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. daxšak (NYB_vol2_glossary.txt line 1246)\", \"stance\": \"partial\",\n    \"note\": \"'daxšak [dhškʼ] sign, mark, token … — Av. (676) daxšāra-, daxšta, cf also (ibd.) daxša- ‚burning’; Sogd. 48.49.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dek-1\", \"stance\": \"silent\",\n    \"note\": \"Watkins lists no Iranian material at all under dek-1; the only Indo-Iranian item in the appendix's dek- family is Sanskrit.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"daxš 1 «دخش ۱»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"NP دَخش daxš exists, and its descent from the Av. daxš-/daxšta- family through MP daxšag is what modern \"\n   \"Iranists tentatively accept: Cheung 2007 s.v. *daxš, 'Daxš with the meaning ‚start, commencement of work’ may be \"\n   \"connected to MP /daxšag/, the meaning deriving from ‚start-sign’'. Mo'in's footnote in Borhan-e Qate' says the same \"\n   \"('پهلوی daxšak … قیاس کنید با اوستا daxšta … بارتولمه ۶۷۷ … نیبرگ'). What is wrong is the GLOSS. \"\n   \"'Trade, occupation' is Horn 1893 no. 542 (p.120): 'daxš ‚Geschäft, Mühe’', taken over by Pokorny; Cheung rejects it \"\n   \"outright: 'The meaning ‚Geschäft, Mühe’ assigned to NP daxš by Horn 1893: 120 … does not exist.' The lexica give \"\n   \"two senses: (1) 'ابتدا کردن کار باشد. گویند دخش بتو است؛ یعنی نخستین معامله با تست' (Loḡat-e Fors of Asadi, \"\n   \"then Jahangiri, Borhan; Dehkhoda notes 'دخش کردن = دشت کردن'), and (2) 'dark and gloomy'. And of course the node \"\n   \"inherits the root problem of #1: even Cheung's *daxš goes back to *dekʷs-, not to *deḱ-.\"),\n \"derivation_fa\": (\"واژهٔ «دَخش» در فارسی هست و پیوند آن با اوستایی daxš-/daxšta- از راهِ فارسی میانهٔ daxšag «نشان، علامت» پذیرفتنی است؛ \"\n   \"حاشیهٔ معین بر برهان قاطع (ذیلِ دخش) همین را می‌گوید و چونگ نیز می‌نویسد معنای «آغاز کار» از «نشانِ آغاز» پدید آمده است. \"\n   \"امّا معنایی که نورایی می‌آورد («داد و ستد، پیشه») از هرن (۱۸۹۳، شمارهٔ ۵۴۲، «Geschäft, Mühe») گرفته شده و چونگ آن را صریحاً رد می‌کند: \"\n   \"معنای درست به گواهی لغت فرس اسدی، جهانگیری، برهان و دهخدا «آغازِ کار و نخستین معامله» (و نیز «تیره و تاریک») است، نه «پیشه و تجارت». \"\n   \"پس ادعای نورایی در اصلِ پیوند با احتیاط پذیرفتنی است ولی معنای ذکرشده نادرست است.\"),\n \"sources\": [A_DAXS],\n \"ref_check\": [\n   {\"ref\": \"POK:189\", \"status\": \"contradicts\",\n    \"note\": \"Same sentence as for node #1: 'npers. daxš ‚Geschäft, Mühe’ bleiben wegen des Gutturals fern' — Nourai took Pokorny's gloss but reversed his verdict.\"},\n   {\"ref\": \"BRT:667\", \"status\": \"not_found\",\n    \"note\": \"AiW col. 667-668 is daēnā-vazah- / daenō.diš- / daeman- / daeva- (BRT.txt leaf 387, running head '667 daenāvazah- | 1daeva- 668'); nothing on daxš. The daxš- material is at cols. 675-678. Miscited column.\"},\n   {\"ref\": \"BQT:827\", \"status\": \"supports\",\n    \"note\": (\"Borhan-e Qate' vol. 2, BQT_v2_pages.txt leaf 287 (printed ≈830, i.e. within the ±3 uncertainty of the \"\n             \"leaf→page mapping): headword 'دخش = بفتح اول بروزن رخش' with Mo'in's footnote 'پهلوی daxšak (شغل، تکلیف) \"\n             \"قیاس: اوستا daxšta … «بارتولمه ۶۷۷» و ممکن است از اوستا daxša (نشان، علامت) «بارتولمه ۶۷۹» مشتق باشد «نیبرگ»'. \"\n             \"This is exactly the Avestan→Pahlavi→Persian chain Nourai draws (and the source of his 'occupation' gloss).\")}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *daxš, *NEIR section (CHEUNG.txt lines 5583-5593)\", \"stance\": \"partial\",\n    \"note\": \"'? NP daxš ‚start, commencement of work; dark and gloomy’. The meaning ‚Geschäft, Mühe’ assigned to NP daxš by Horn 1893: 120 … does not exist.' Connection to MP daxšag accepted, gloss rejected.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn 1893 no. 542, p.120 (HRN.txt leaf 142)\", \"stance\": \"supports\",\n    \"note\": \"'542. daxš ‚Geschäft, Mühe’. ai. daksá ‚Tüchtigkeit, Tauglichkeit, Fähigkeit’ (Nöldeke, mündliche Mitteilung).' — the ultimate source of Nourai's gloss and of the *dek- connection.\"},\n   {\"src\": \"MON\", \"where\": \"Dehkhoda/Mo'in s.v. دخش (abadis.ir/fatofa/دخش)\", \"stance\": \"contradicts\",\n    \"note\": \"'دخش. [دَ] (اِ) ابتدا کردن کار باشد. گویند دخش بتو است؛ یعنی نخستین معامله با تست. (فرهنگ اسدی) … سفته. دشت: دخش کردن؛ دشت کردن.' — 'first transaction', not 'trade, occupation'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p. 268 (ARY_pages.txt, [pdf page 267])\", \"stance\": \"supports\",\n    \"note\": \"Headword 'دخش، دشت (به چم تکلیف، شغل، آغاز کار، معاملهٔ اول)' listing Av. daxš-/daxšta-/daxšāra-, Pahl. daxšak, Gk. dokéō, Lat. docere — i.e. Aryanpur groups it exactly as Nourai does (both follow Horn).\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. daxšag\", \"stance\": \"partial\",\n    \"note\": \"'daxšag … mark, sign, characteristic; memory' — supplies the Middle Persian link but not the sense 'trade'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"docěre; decěre; discere; decus; dignus\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All five are the textbook Latin reflexes of *deḱ-. Watkins/AHD dek-1: '2. Suffixed (causative) o-grade form \"\n   \"*dok-eye- in a. Latin docēre, to teach (< “to cause to accept”) … 3. Suffixed form *dek-es- in a. Latin decus, grace, \"\n   \"ornament … 4. Suffixed form *dek-no- in Latin dignus (< *dec-nos) … 5. Reduplicated form *di-dk-ske- in Latin discere, \"\n   \"to learn'. Impersonal decet, -ēre 'it is fitting' is the primary stative; docēre is its causative (Ernout-Meillet: \"\n   \"'doceo … causatif à vocalisme o'). Walde-Pokorny I 784 has the same list. De Vaan 2008 (decet 164, doceō 176, \"\n   \"discō 172) keeps all of them under *deḱ-. The printed page spells the two verbs 'docěre' and 'decěre' with a \"\n   \"breve; the vowel is in fact long (docēre, decēre) — a typographic slip of the book, not an extraction error.\"),\n \"derivation_fa\": (\"هر پنج واژهٔ لاتین بازماندهٔ معیارِ *deḱ- اند: decēre/decet «زیبنده بودن» ستاک اصلی، docēre «آموزاندن» ساختِ سببی از *dok-eye-، \"\n   \"decus «زیور، آبرو» از *dek-es-، dignus «سزاوار» از *dek-no- (از راه *dec-nos) و discere «آموختن» از صورت دوگان‌شدهٔ *di-dk-ske-. \"\n   \"وتکینز، والده–پوکورنی ج۱ ص ۷۸۴، ارنو–مییه و دووان همه همین را می‌گویند. ادعای نورایی درست است؛ تنها علامت کوتاهی روی e در چاپ کتاب خطای حروف‌چینی است.\"),\n \"sources\": [W_DEK, E_DOC],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. dek-1 (AHD_watkins1985.txt line 362) lists docēre, decus, decor, dignus, discere in exactly this order of formations.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. doceo (LAT.txt line 17387), s.v. dexter (line 16480)\", \"stance\": \"supports\",\n    \"note\": \"'doceo, -es, -ui, doctum, -ere; causatif à vocalisme o (cf. moneo)'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 784\", \"stance\": \"supports\",\n    \"note\": \"'lat. decet, -ere … decus, -oris ‚Zierde’ … lat. dignus ‚würdig’ (*dec-nos) … lat. doceo ‚lehre’ … lat. disco, didici ‚lernen’ (*di-dk-sko)'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. decent, doxastic\", \"stance\": \"supports\",\n    \"note\": \"'I.-E. base *dek-, *dok- ‚to take, receive, accept’ … whence also L. decere'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Empty pass-through box: French is only the transmitting stage between the Latin words of #3 and the Persian \"\n   \"loans of #5. The relevant French forms are docteur (Old French doctour, 12th c., from Latin doctor 'teacher', agent noun \"\n   \"of docēre) and décor / décorer (from Latin decus, decorāre). Both are ordinary learned Latinisms of French, so the \"\n   \"box is correct as drawn even though the book leaves it blank.\"),\n \"derivation_fa\": (\"این جعبه تهی‌ست و تنها نقشِ واسطه دارد: فرانسهٔ docteur (از لاتین doctor، اسم فاعلِ docēre) و décor/décorer (از لاتین decus، decorāre) \"\n   \"دو وام‌واژهٔ کتابی از لاتین‌اند که سپس به فارسی راه یافته‌اند؛ پس پیکانِ لاتین ← فرانسه درست است.\"),\n \"sources\": [E_DOC],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book; nothing to check.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. doctor / decorate\", \"stance\": \"supports\",\n    \"note\": \"Klein routes English doctor through OF doctour < L. doctor, and decorate < L. decorāre < decus.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dek-1\", \"stance\": \"supports\",\n    \"note\": \"DECOR is bracketed as the French-mediated form of Latin decor under dek-1.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"doktor «دکتر»; dekor «دکور»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Two 19th-20th c. French loanwords in Persian, entering with the Dar al-Fonun generation and the Qajar-era \"\n   \"adoption of European medicine and theatre. Mo'in's Farhang-e Farsi has 'دکتر: docteur (ا.) آنکه بالاترین \"\n   \"مراحل علمی را طی کرده …' and 'دکتری: [فر. ف.] doctorat', and دکور is tagged '[فر.]' = French \"\n   \"(décor) with the sense 'مجموعهٔ اشیاء و اثاثیه در صحنهٔ نمایش'. French -eu- is rendered by Persian -o- \"\n   \"(docteur → doktor), and final French -r is kept. Chain: PIE *deḱ- > Lat. docēre > doctor / decus > décor > NP دکتر، دکور.\"),\n \"derivation_fa\": (\"«دکتر» و «دکور» دو وام‌واژهٔ فرانسوی اند که در دورهٔ قاجار و با دارالفنون وارد فارسی شدند. معین در فرهنگ فارسی \"\n   \"ذیلِ «دکتر» صورتِ فرانسوی docteur و ذیلِ «دکتری» نشانهٔ [فر.] را می‌آورد، و «دکور» نیز با نشانهٔ [فر.] از décor ثبت شده است. \"\n   \"در وام‌گیری، -eu- فرانسوی به -و- فارسی بدل شده است. زنجیره: *deḱ- > docēre > doctor > docteur > دکتر. ادعای نورایی درست است.\"),\n \"sources\": [A_DEKOR, E_DOC],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi (MON_part1.txt line 62214 ff.): 'دکتر: docteur (ا.) …'; 'دکتری: doctorat [فر. ف.] (حامص.)'. دکور is absent from this 2-vol. Adena reprint but stands in the full 6-vol. edition; abadis quotes it as '(دِ کُ) [فر.] (اِ.)'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in / Amid s.v. دکور (abadis.ir/fatofa/دکور)\", \"stance\": \"supports\",\n    \"note\": \"'(دِ کُ) [فر.] (اِ.) ۱ - مجموعة اشیاء و اثاثیه در صحنة نمایش' — explicitly French.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. doctor\", \"stance\": \"supports\",\n    \"note\": \"Latin doctor 'teacher', agent noun of docēre — the ultimate source of the French and hence the Persian word.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"doctor, document, decent, disciple, discipline, decorate, dignity\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Every item is in Watkins's own list under dek-1: DOCTOR, DOCTRINE, DOCUMENT (< Lat. documentum 'lesson, proof', \"\n   \"from docēre); DECENT (< Lat. decēns, ptcp. of decet); DISCIPLE, DISCIPLINE (< Lat. discipulus, disciplina, from discere \"\n   \"< *di-dk-ske-); DECORATE (< Lat. decorāre, from decus); DIGNITY (< Lat. dignitās, from dignus < *dek-no-). Most came in \"\n   \"through Old French in the 13th-14th c. (Etymonline: doctor 'c. 1300, doctour, “Church father”, from Old French doctour \"\n   \"and directly from Medieval Latin doctor'), disciple already in Old English from Latin discipulus. Klein s.v. decent \"\n   \"gives the same family.\"),\n \"derivation_fa\": (\"همهٔ این هفت واژهٔ انگلیسی در پیوستِ ریشه‌های وتکینز (dek-1) آمده‌اند: doctor و document از docēre، decent از decēns، \"\n   \"disciple و discipline از discipulus/disciplina (از discere)، decorate از decorāre (از decus)، و dignity از dignitās (از dignus). \"\n   \"بیشتر این‌ها در سدهٔ ۱۳ و ۱۴ میلادی از راه فرانسهٔ کهن وارد انگلیسی شده‌اند. ادعای نورایی درست است.\"),\n \"sources\": [E_DOC, W_DEK],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book; the parent Latin node's AHD citation covers it.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. decent / doxastic (KLN_1966.txt lines 10494, 12181)\", \"stance\": \"supports\",\n    \"note\": \"Klein's cross-reference list under the base *dek-, *dok- includes 'decorate, decorous, deign, dignify, dignity, docent, docile, doctor, doctrine, document …'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dek-1 and index\", \"stance\": \"supports\",\n    \"note\": \"Index entries 'DOCTOR dek-1', 'DOCUMENT dek-1', 'DECENT dek-1', 'DISCIPLE dek-1', 'DISCIPLINE dek-1', 'DECORATE dek-1', 'DIGNITY dek-1'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Greek\", \"words\": \"dokein\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Gk. δοκέω dokéō 'to seem good, to seem, think, believe' is the Greek counterpart of Latin doceō: Pokorny 189 \"\n   \"'causative δοκέω (= lat. doceo)', beside the primary verb δέχομαι / Ionic-Aeolic-Cretan δέκομαι 'to take in, accept'. \"\n   \"From it δόξα dóxa (< *dok-sa) 'opinion, glory' and δόγμα 'decree'. Nourai's gloss 'make things clear, think' is a \"\n   \"little strained — the sense is 'seem (good), be accepted, think' — but the root assignment is standard (Watkins dek-1, \"\n   \"Klein s.v. doxastic). One caveat worth recording: Beekes 2010 (I 344-345) prefers to derive δοκέω as a deverbative \"\n   \"of δέχομαι rather than as an inherited *dok-éye- causative; either way it is *deḱ-.\"),\n \"derivation_fa\": (\"یونانی δοκέω (dokéō) «پسندیده آمدن، به نظر رسیدن، پنداشتن» همتای لاتین doceō است و در کنار فعلِ اصلی δέχομαι (گویش ایونی δέκομαι) \"\n   \"«پذیرفتن» قرار دارد؛ از همین ریشه δόξα «رأی، آوازه» و δόγμα ساخته شده است. معنایی که نورایی می‌آورد کمی آزاد است، ولی تعیین ریشه معیار است. \"\n   \"یادآوری: بیکس (۲۰۱۰) بر آن است که δοκέω مشتق از δέχομαι است نه سببیِ کهن؛ در هر دو حالت باز از *deḱ- است.\"),\n \"sources\": [W_DEK, E_ORT],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 dek-1: '2b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA … HETERODOX, ORTHODOX, PARADOX.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK_01.txt line 2730 (p.189)\", \"stance\": \"supports\",\n    \"note\": \"'kausativ δοκέω (= lat. doceo) … δόξα f. ‚Meinung, Ruhm’ (*δοκ-σα), δόγμα n. ‚Beschluss’'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. doxastic (KLN_1966.txt line 12181)\", \"stance\": \"supports\",\n    \"note\": \"'δόξα … derives fr. δοκεῖν, ‚to seem good, to seem, think, believe’ … fr. I.-E. base *dek-, *dok-'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. deḲo (IEC.txt line 2135)\", \"stance\": \"supports\",\n    \"note\": \"'Gk. dékomai, beside dektós ‚agreeable’' under deḲo.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"French\", \"words\": \"orthodoxe\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"French orthodoxe (attested 1431 in the theological sense) is a learned borrowing of Late Latin orthodoxus, \"\n   \"itself from Greek ὀρθόδοξος 'having the right opinion' = ὀρθός 'straight, right' + δόξα 'opinion', and \"\n   \"δόξα is from δοκέω (node #7). Etymonline s.v. orthodox: 'from Late Latin orthodoxus, from Greek orthodoxos \"\n   \"“having the right opinion”, from orthos … + doxa “opinion, praise” (from dokein “to seem”; from PIE root *dek- “to \"\n   \"take, accept”)'. So the Greek → French step is exactly as drawn.\"),\n \"derivation_fa\": (\"فرانسهٔ orthodoxe وام‌واژه‌ای کتابی از لاتینی پسین orthodoxus است که خود از یونانی ὀρθόδοξος «دارندهٔ رأی درست» گرفته شده: \"\n   \"ὀρθός «راست، درست» + δόξα «رأی»، و δόξα از δοκέω (گره ۷) است. پس پیکان یونانی ← فرانسه درست است.\"),\n \"sources\": [E_ORT],\n \"ref_check\": [\n   {\"ref\": \"MON:193\", \"status\": \"supports\",\n    \"note\": \"Mo'in gives the French etymon in Latin letters at the head of the Persian entry: 'ارتودوکس: orthodoxe (ص. ا.) دارای ایمان و عقیدة صحیح' (MON_part1.txt line 9618). Vol./page 193 of the 6-vol. edition could not be paginated in the 2-vol. Adena reprint on disk, but the content is verbatim what Nourai cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. heterodox / doxastic\", \"stance\": \"supports\",\n    \"note\": \"'ἑτερόδοξος ‚holding opinions other than the right’ … δόξα ‚opinion’, fr. δοκεῖν ‚to think’' — the same compound type as orthodoxos.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, index 'ORTHODOX dek-1'\", \"stance\": \"supports\",\n    \"note\": \"Orthodox is filed under dek-1 via Greek dokein.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"ortodox «ارتودوکس»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"ارتودوکس is a modern Persian loan from French orthodoxe, borrowed in the Qajar/Pahlavi period chiefly in the \"\n   \"church sense. Mo'in's entry prints the French form as etymon: 'ارتودوکس: orthodoxe (ص. ا.) دارای ایمان و \"\n   \"عقیدة صحیح. فرقه‌ای مخصوص از فرق مسیحیت' — which is exactly Nourai's gloss 'with correct thoughts'. \"\n   \"French final -e is dropped, -th- of the spelling is realised as plain t, and the book's own script form on the printed \"\n   \"page is أرتودوکس with hamza (the JSON's ارتودوکس is the normal spelling; not an error worth flagging).\"),\n \"derivation_fa\": (\"«ارتودوکس» وام‌واژهٔ فرانسوی orthodoxe است که بیشتر در معنای کلیسایی به فارسی راه یافته است. معین در فرهنگ فارسی \"\n   \"می‌نویسد: «ارتودوکس: orthodoxe (ص. ا.) دارای ایمان و عقیدهٔ صحیح» که دقیقاً همان معنایی است که نورایی آورده است. \"\n   \"در وام‌گیری، -e پایانی فرانسوی افتاده و th به ت بدل شده است. ادعای نورایی درست است.\"),\n \"sources\": [E_ORT],\n \"ref_check\": [\n   {\"ref\": \"MON:193\", \"status\": \"supports\",\n    \"note\": \"MON_part1.txt line 9618: 'ارتودوکس: orthodoxe (ص. ا.) دارای ایمان و عقیدة صحیح. فرقه‌ای مخصوص از فرق مسیحیت.' The 2-vol. reprint has no page 193 of vol. 4, but the entry is the one cited.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in s.v. ارتودوکس (MON_part1.txt line 9618)\", \"stance\": \"supports\",\n    \"note\": \"French etymon printed in Latin script by Mo'in himself.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. heterodox\", \"stance\": \"supports\",\n    \"note\": \"Confirms the Greek compound and its sense 'having the right opinion' behind the European word Persian borrowed.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"heterodox, orthodox, paradox\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All three are Greek δόξα-compounds that reached English through Late Latin in the 15th-16th c.: heterodox \"\n   \"(ἑτερόδοξος 'holding another opinion'), orthodox (mid-15c., ὀρθόδοξος), paradox (1530s, παράδοξος \"\n   \"'contrary to expectation', para- 'beyond' + doxa). Watkins files all three under dek-1 through Greek dokein; Klein \"\n   \"s.v. doxastic lists 'the second element in heterodox, orthodox, paradox'.\"),\n \"derivation_fa\": (\"هر سه واژه ترکیب‌های یونانی با δόξα «رأی» اند که از راه لاتینی پسین در سدهٔ ۱۵ و ۱۶ وارد انگلیسی شده‌اند: \"\n   \"heterodox «دگراندیش»، orthodox «راست‌اندیش» و paradox «خلافِ انتظار». وتکینز و کلاین هر سه را ذیل dek-1 و δοκέω می‌آورند. ادعای نورایی درست است.\"),\n \"sources\": [E_ORT],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 dek-1, 2b: 'Greek dokein … DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. doxastic / heterodox (KLN_1966.txt lines 12181, 17696)\", \"stance\": \"supports\",\n    \"note\": \"'… the second element in heterodox, orthodox, paradox'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, s.vv. orthodox family\", \"stance\": \"silent\",\n    \"note\": \"Skeat's Concise has no separate orthodox/paradox entry (only incidental uses at 'moslem', 'mussulman'); no contradiction.\"}\n ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ------------------------------------------------------------------ entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Deks\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *deḱs- 'right (as opposed to left); southern' (an s-extension of *deḱ-; Pokorny 190, Watkins deks-)\",\n \"note\": (\"Correct in every part. Pokorny treats it inside the lemma 1. deḱ- (pp.189-191): 'deḱs- mit verschiedenen \"\n   \"Suffixen: ai. daḳṣiṇa-, av. dašina- ‚rechts’, lit. dešinas, aksl. desnŭ; gr. δεξιτερός = lat. dexter' — that \"\n   \"block begins on p.190, so POK:190 is exact. Watkins has a separate headword: 'deks-. Right (opposite left); hence, with \"\n   \"an eastward orientation, south … [In Pok. 1. dek- 189.]', which in the 1975 New College appendix falls in the range \"\n   \"Nourai cites (AHD:1511). Semantically the root is a derivative of *deḱ- 'take': the right hand is 'the taking / \"\n   \"fitting hand' — Persson's *deksi 'auf der Seite der greifenden Hand', quoted approvingly in Walde-Pokorny I 784.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی *deḱs- «راست، سمت راست» و برچسب و معنای آن هر سه درست است. پوکورنی آن را در همان مدخلِ deḱ- (ص ۱۸۹–۱۹۱) \"\n   \"می‌آورد و بخشِ deḱs- از صفحهٔ ۱۹۰ آغاز می‌شود، پس ارجاع نورایی دقیق است. این ریشه را مشتقّی از *deḱ- «گرفتن» می‌دانند: \"\n   \"دست راست همان «دستِ گیرنده» است (والده–پوکورنی ج۱ ص ۷۸۴). ادعای نورایی درست است.\"),\n \"sources\": [W_DEKS, W_DEX],\n \"ref_check\": [\n   {\"ref\": \"POK:190\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt line 2741 (printed p.190) heads the section 'deks- mit verschiedenen Suffixen:'; the material (ai. daḳṣiṇa-, av. dašina-, gr. δεξιτερός, lat. dexter) follows there. Page(s) of the whole lemma: 189-191.\"},\n   {\"ref\": \"AHD:1511\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. deks- (AHD_watkins1985.txt line 362 tail): 'deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter … DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. [In Pok. 1. dek- 189.]' The 1975 New College appendix runs pp.1505-1550 and d- roots fall around 1511, so the page is plausible; the standalone 1985 edition has different pagination and cannot confirm the number itself.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 784-785\", \"stance\": \"supports\",\n    \"note\": \"'auch die auf einem loc. *deksi ‚auf der tauglichen Seite’ … beruhenden Worte für ‚rechts’: Ai. dákṣiṇa- … av. dašina- ‚rechts’ … gr. δεξιτερός = lat. dexter'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. deḲsinos, deḲsiteros (IEC.txt line 2148; WP I,784)\", \"stance\": \"supports\",\n    \"note\": \"'deḲsinos, deḲsiteros … ‚right-hand’ … (1) Skt. dákṣiṇaḥ; Av. dašino; OCS desnŭ … (2) Gk. dexiterós; Lat. dexter'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. dexter (KLN_1966.txt line 11178)\", \"stance\": \"supports\",\n    \"note\": \"'L. dexter … cogn. with Gk. δεξιτερός … OI. dakṣiṇaḥ … Avestic dašina-, ‚on the right hand’ … All these words are prob. derivatives of the base *dek-.'\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"dašina\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Av. dašina- adj. 'right, on the right side' (AiW col. 703; e.g. N 65 'dašina paiti arǝdaŋha “on the right \"\n   \"side”', Yt 13.63 dašinam upa yūiðiieinti) continues PIE *deḱs-ino-, the -ino- suffix beside Skt. dákṣiṇa-; the PIE \"\n   \"cluster *-ḱs- gives Avestan -š- regularly (the same *ḱ that gives -s- elsewhere), so the form is phonologically \"\n   \"impeccable and is quoted in every handbook (Pokorny 190 'av. dašina- ‚rechts’'; Walde-Pokorny I 784; Mann; Klein).\"),\n \"derivation_fa\": (\"اوستایی dašina- «راست، سمت راست» (بارتولومه ستون ۷۰۳) ادامهٔ *deḱs-ino- هندواروپایی است، با همان پسوندِ -ino- که در \"\n   \"سنسکریت dákṣiṇa- دیده می‌شود. خوشهٔ *-ḱs- در اوستایی قاعدتاً به -š- بدل می‌شود، پس صورت از نظر آوایی بی‌عیب است. \"\n   \"پوکورنی، والده–پوکورنی، من و کلاین همگی همین را می‌گویند؛ ادعای نورایی درست است.\"),\n \"sources\": [W_DEKS],\n \"ref_check\": [\n   {\"ref\": \"POK:190\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt (p.190), section 'deks- mit verschiedenen Suffixen': 'ai. dákṣiṇa-, dakṣiṇá- ‚rechts, südlich, tüchtig, geschickt’, av. dašina- ‚rechts’, lit. dešinas …'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 703 (cited as such by Nyberg II 1215 and by SNS p.316)\", \"stance\": \"supports\",\n    \"note\": \"Both Nyberg ('Av. (703) dašina-') and Tavoosi's SNS glossary ('(AiWb. 703) dašina-') refer the Pahlavi word to Bartholomae's dašina- entry at col. 703; the OCR of that column in BRT.txt is defective, but the citation is unambiguous.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 784\", \"stance\": \"supports\",\n    \"note\": \"'Ai. dákṣiṇa-, dakṣiṇá- ‚rechts, südlich …’, av. dašina- ‚rechts’, lit. dešinė …'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. deḲsinos\", \"stance\": \"supports\",\n    \"note\": \"'Av. dašino' listed as the Iranian member of the *deksinos set.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"dašn\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"MP dašn [dšnʼ] 'right, right hand' is the regular continuant of Av. dašina-: the medial unstressed -i- of \"\n   \"*dašina- syncopates in Middle Persian (dašina- > dašn), the same reduction as in Av. hačima- type formations. \"\n   \"MacKenzie: 'dašn [dšn! | = M] right hand' (with dašnag '1. right hand; 2. dagger'), carefully distinguished from \"\n   \"dāšn [dʼSnʼ] 'gift'. Nyberg II 1215: 'dašn [dšnʼ], attributive before its subst. dašnē, right, right hand … \"\n   \"— Av. (703) dašina-'; it also developed the sense 'engagement (by giving one's right hand)'. Armenian borrowed it as \"\n   \"dašn 'treaty, alliance'.\"),\n \"derivation_fa\": (\"فارسی میانه dašn «راست، دست راست» دنبالهٔ قاعده‌مندِ اوستایی dašina- است؛ واکهٔ کوتاهِ میانی (-i-) در فارسی میانه افتاده \"\n   \"(dašina- > dašn). مکنزی می‌نویسد «dašn دست راست» و آن را به‌دقت از dāšn «هدیه» جدا می‌کند؛ نیبرگ نیز آن را به اوستایی dašina- \"\n   \"(بارتولومه ۷۰۳) بازمی‌گرداند و معنای ثانویِ «پیمان (دست دادن)» را نیز یاد می‌کند. ادعای نورایی درست است.\"),\n \"sources\": [W_DEKS],\n \"ref_check\": [\n   {\"ref\": \"SNS:316\", \"status\": \"supports\",\n    \"note\": (\"Tavoosi's glossary of Šāyast nē Šāyast: the word index gives 'dašn 316/17' and 'dašina 316/18' \"\n             \"(SNS.txt lines 33107, 29586), and the glossary line itself reads 'dašn: راست … (AiWb. 703) dašina-' \"\n             \"(SNS.txt lines 17246-17247). Page 316 is exactly right.\")}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.25 s.v. dašn (PHD.txt line 310)\", \"stance\": \"supports\",\n    \"note\": \"'dašn [dšn! | = M] right hand. dāšn [dʼSnʼ | M dʼs(y)n] gift. dašnag [dsnkʼ | N ~a] 1. right hand; 2. dagger.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II Glossary s.v. dašn (NYB_vol2_glossary.txt lines 1215-1218)\", \"stance\": \"supports\",\n    \"note\": \"'dašn [dšnʼ] … right, right hand … — Av. (703) dašina-; MPrthPrs dīn; Ps. dšny. Arm lw. dašn ‚treaty, alliance’.' Also 'dašnak [dšnkʼ] the right wing of an army'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"dašn «دَشن»; dašt «دشت ۱»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Both Persian words are real and Nourai's glosses are taken straight from Borhan-e Qate'. Dehkhoda s.v. دشن: \"\n   \"'دشن. [دَ] (اِ) دستلاف، که سودای اول اصناف باشد. (برهان)(آنندراج)'; s.v. دشت: \"\n   \"'۳ - (عا.) فروش اول هر کاسب؛ دشت کردن: نخستین بار پول گرفتن، فروختن جنس اولین بار در هر روز'. Two \"\n   \"reservations keep this from 'confirmed'. (1) The sense 'right side' is the Middle Persian one; the New Persian noun \"\n   \"دشن that the dictionaries record has only the commercial sense — the 'right hand' sense survives in Persian rather in \"\n   \"دشنه 'dagger' (< MP dašnag). (2) The step dašn → dašt (n > t) is not a Persian sound law, and Persian lexicography \"\n   \"itself puts the 'first sale' words with دخش instead: Dehkhoda s.v. دخش equates 'دخش کردن؛ دشت کردن', and \"\n   \"Aryanpur (p.281) notes 'برخی معتقدند که واژهٔ دشت (یا دشن) با واژهٔ دخش … یکی است. حتی اگر دشن با \"\n   \"واژهٔ پهلوی dašn رابطه‌ای نداشته باشد …'. If that is right, دشت/دشن 'first sale' belongs on the previous \"\n   \"chart (Av. daxš-, node 0/#1-#2), not under Deks. The auspicious-omen semantics ('سودای اولی که آن را میمون \"\n   \"و مبارک دارند', Borhan s.v. دستلاف) would fit 'right = lucky' nicely, so Nourai's route is defensible — just \"\n   \"not established.\"),\n \"derivation_fa\": (\"هر دو واژه در فارسی هستند و معنایی که نورایی آورده همان معنای برهان قاطع است: دهخدا ذیلِ «دشن» می‌نویسد \"\n   \"«دستلاف، که سودای اول اصناف باشد» و ذیلِ «دشت» «فروش اول هر کاسب». امّا دو اشکال هست: یکم آنکه معنای \"\n   \"«سمت راست» معنای فارسی میانه است و در فارسی نو بیشتر در «دشنه» (< پهلوی dašnag) باقی مانده؛ دوم آنکه تبدیل \"\n   \"ن به ت (dašn > dašt) دگرگونی آوایی قاعده‌مندی نیست. دهخدا خود «دخش کردن» را با «دشت کردن» یکی می‌گیرد و آریان‌پور \"\n   \"(ص ۲۸۱) می‌نویسد که برخی «دشت/دشن» را همان «دخش» می‌دانند. پس این پیوند با احتیاط پذیرفتنی است، هرچند پیوندِ \"\n   \"معنایی «راست = خجسته و مبارک» با «سودای اولی که آن را میمون دارند» به‌خوبی جور درمی‌آید.\"),\n \"sources\": [A_DASN, A_DAST],\n \"ref_check\": [\n   {\"ref\": \"SNS:316\", \"status\": \"partial\",\n    \"note\": \"SNS p.316 documents the Pahlavi word dašn 'right' (← Av. dašina-, AiWb. 703) but says nothing about the New Persian commercial sense; it supports the Pahlavi step only.\"},\n   {\"ref\": \"BQT:866\", \"status\": \"supports\",\n    \"note\": (\"Borhan-e Qate' vol. 2: the دشت / دشتان / دشن / دشوار block sits at BQT_v2_pages.txt leaves 325-327 \"\n             \"(printed ≈868-870, i.e. Nourai's 866 within the ±3 leaf→page uncertainty). Borhan's دشن is quoted by \"\n             \"Dehkhoda as 'دستلاف، که سودای اول اصناف باشد. (برهان)' — precisely Nourai's 'first (daily) sales'.\")}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Dehkhoda + Mo'in s.v. دشن and دشت (abadis.ir/fatofa/دشن , /دشت)\", \"stance\": \"partial\",\n    \"note\": \"دشن: 'دستلاف، که سودای اول اصناف باشد'; Mo'in '(اسم) دستلاف فروش اول کاسب'. دشت: 'فروش اول هر کاسب … دشت کردن'. Neither dictionary records a New Persian sense 'right side'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p. 281 (ARY_pages.txt, [pdf page 280])\", \"stance\": \"partial\",\n    \"note\": \"'چم این واژه در همهٔ زبان‌های این فهرست (به جز فارسی امروزی): دست راست … برخی معتقدند که واژهٔ دشت (یا دشن) با واژهٔ دخش … یکی است.' — flags exactly the doubt recorded here.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. dašnag, dašt\", \"stance\": \"partial\",\n    \"note\": \"'dašnag … 1. right hand; 2. dagger' (the ancestor of NP دشنه) and, separately, 'dašt [dst!] plain, open ground' — so MP has no dašt meaning 'first sale'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *daxš, *NEIR\", \"stance\": \"contradicts\",\n    \"note\": \"Cheung attaches the Persian 'commencement of work / first transaction' vocabulary to MP daxšag, i.e. to the daxš- root of entry 0, not to dašn 'right'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"dexter\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Lat. dexter, -tra, -trum 'on the right' < Proto-Italic *deksteros < PIE *deḱs-tero-s, a contrastive \"\n   \"*-tero- formation exactly matching Greek δεξιτερός; Oscan destrst 'dextra est', Umbrian destrame confirm the \"\n   \"Italic form (Ernout-Meillet s.v. dexter). Comparative dexterior, archaic superlative dextimus. Wiktionary/de Vaan \"\n   \"(2008: 168) give the same. The secondary sense 'favourable, propitious' follows from Roman augury, where the right \"\n   \"side was the lucky one — the semantic note Watkins makes for the root as a whole.\"),\n \"derivation_fa\": (\"لاتین dexter «راست، در سمت راست» از *deksteros ایتالیکی آغازین و آن از *deḱs-tero-s هندواروپایی است؛ \"\n   \"پسوندِ -tero- نشانهٔ تقابل است و دقیقاً با یونانی δεξιτερός برابر است. گواهی اسکی و اومبریایی (destrst، destrame) نیز هست. \"\n   \"معنای ثانویِ «خجسته، مساعد» از فال‌بینی رومی می‌آید. ادعای نورایی درست است.\"),\n \"sources\": [W_DEX, W_DEKS],\n \"ref_check\": [\n   {\"ref\": \"POK:190\", \"status\": \"supports\",\n    \"note\": \"POK (p.190): 'gr. δεξιτερός = lat. dexter, -tra, -trum (Kompos. dexterior, Superl. dextimus), osk. destrst … umbr. destrame'.\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins deks-: 'Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. dexter (LAT.txt lines 16480-16495)\", \"stance\": \"supports\",\n    \"note\": \"'dexter, -tera, -teri (-tra, -trum): l'osco-ombrien ne connaît que les formes sans e, ombr. destru-co, destram-e ‚ad dexteram’, osq. destr-st ‚dextra est’ … 1° droit, par opposition à sinister … cf. gr. δεξιτερός'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. dexter (KLN_1966.txt line 11178)\", \"stance\": \"supports\",\n    \"note\": \"'L. dexter, ‚on the right hand’, whence arose the meanings ‚skillful, favorable, propitious, fortunate’; cogn. with Gk. δεξιτερός … Avestic dašina-'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"dexter, dextro-\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English dexter (1560s, chiefly heraldic, 'on the right side of a shield') is a direct learned borrowing of \"\n   \"Latin dexter, and the combining form dextro- (in dextrose, dextrorotatory etc.) is built on the same stem; dexterity \"\n   \"came earlier through French dextérité < Lat. dexteritās. Watkins lists 'DESTRIER, DEXTER, DEXTERITY, DEXTRO-; \"\n   \"AMBIDEXTROUS' under deks-. Wiktionary s.v. dexter: 'Learned borrowing from Latin dexter (“right”)'.\"),\n \"derivation_fa\": (\"انگلیسی dexter (سدهٔ ۱۶، بیشتر در نشان‌شناسی) وام‌واژه‌ای کتابی از لاتین dexter است و پیشوندِ علمیِ -dextro \"\n   \"(در dextrose، dextrorotatory) بر همان ستاک ساخته شده است. وتکینز ذیلِ deks- همین فهرست را می‌آورد؛ ادعای نورایی درست است.\"),\n \"sources\": [W_DEX],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. deks-: '… DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS'; index lines 'DEXTER deks-', 'DEXTRO- deks-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. dexter, dexterity, dexterous (KLN_1966.txt lines 11178-11183)\", \"stance\": \"supports\",\n    \"note\": \"'dexterity … F. dextérité, fr. L. dexteritatem … fr. dexter'; 'dexterous … formed with suff. -ous fr. L. dexter'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, s.v. adroit (SKT.txt line 15808) and 'dexterous' glosses\", \"stance\": \"partial\",\n    \"note\": \"Skeat's Concise has no dexter headword but glosses several words as 'dexterous' from L. directus/dexter family; no contradiction.\"}\n ]\n})\n\ndoc[\"entries\"].append(e1)\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-113.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk113.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-113.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 113"
}
```


### [2026-09-05T18:00:12.799Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-113.json
JSON_OK
nodes verified: 15/15
node verdicts: {'disputed': 1, 'plausible': 2, 'confirmed': 12}
root verdicts: {'confirmed': 2}
ref checks: {'contradicts': 3, 'partial': 2, 'not_found': 1, 'supports': 13, 'not_checked': 2}
books consulted: {'partial': 9, 'contradicts': 3, 'silent': 2, 'supports': 27} | by book: {'KLN': 10, 'PHD': 4, 'AHD': 4, 'MON': 4, 'CHEUNG': 3, 'BRT': 2, 'NYB': 2, 'ARY': 2, 'LAT': 2, 'WLD': 2, 'IEC': 2, 'SKT': 2, 'HRN': 1, 'POK': 1}
```


## [2026-09-05T18:00:20.777Z] TOOL CALL #89: Bash

```json
{
 "command": "python3 tools/verify_check.py 113 | grep -c PROBLEM; python3 tools/verify_archive_sources.py 2>/dev/null | tail -5 || true"
}
```


### [2026-09-05T18:00:31.026Z] TOOL RESULT

```
0
FAILED https://www.academia.edu/35394163/_SWIran_didā_fortress_walled_residence_in_Iranian_Toponymy_by_Garnik_Asatrain
FAILED https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A5%8C%E0%A4%A8%E0%A4%95%E0%A5%BC
FAILED https://forum.wordreference.com/threads/persian-rustaki-and-latin-rusticus-rustic.3399756/
FAILED https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/
archived 18, failed 4
```


## [2026-09-05T18:00:51.725Z] AGENT

Page 113 (book p. 83) verified: `/home/sfmqrb/git/rishe/data/verification/page-113.json` — `verify_check.py 113` shows 15/15 nodes, 0 PROBLEM lines.

**Verdicts:** roots 2 confirmed; nodes 12 confirmed, 2 plausible, 1 disputed. Ref checks: 13 supports, 3 contradicts, 2 partial, 1 not_found, 2 not_checked. 14 books consulted.

**Disputed**
- *Dek* #1 Avestan `daxš / fra-daxš-tar / daxšta` — Pokorny p.189 (the page Nourai cites) and Walde-Pokorny I 784 (also cited by him) both **expressly exclude** these words: "aber av. daxš- 'lehren', npers. daxš 'Geschäft, Mühe' bleiben wegen des Gutturals fern". Cheung 2007 s.v. *daxš sets up PIE *dekʷs- 'to show' (LIV 112, labiovelar guaranteed by Hitt. tekkušš-), not *deḱ-. Buck (SYN 1227, the third ref) says "etym. dub." Also, `daxšta` is not "knowledge, tool" but 'sign, outward mark' (AiW 677-8; whence دشتان).

**Plausible (worth flagging)**
- *Dek* #2 Persian `دخش` "trade, occupation" — the gloss is Horn 1893 no. 542 ('Geschäft, Mühe'), which Cheung rejects outright ("does not exist"); Loḡat-e Fors/Borhan/Dehkhoda give 'آغاز کار، نخستین معامله' and 'dark, gloomy'. The Av.→MP daxšag→NP link itself is accepted, so the arrow stands.
- *Deks* #3 Persian `دشن / دشت` — glosses are Borhan's and correct, but NP دشن is recorded only in the 'first sale' sense ('right' survives in دشنه), and Dehkhoda equates دخش کردن = دشت کردن while Aryanpur (p. 281) notes some identify دشت/دشن with دخش — i.e. these may belong to the previous chart, not to Deks.

**Miscited reference (book error, not extraction)**
- `BRT:667` on *Dek* #2: AiW col. 667-8 is daēnā-vazah-/daēva-; the daxš- material is at cols. 675-678. Marked `not_found`.
- `BQT:827` and `BQT:866` both check out at Borhan vol. 2 leaves ≈ printed 830 and 868-870 — within the ±3 uncertainty of the leaf→page map, so recorded as `supports`.

**Extraction errors: none.** I rendered PDF p. 113 and compared: the JSON is faithful, including the book's own `docěre`/`decěre` (breve for a long ē — the book's typographic slip, noted in the derivation) and the printed script `أرتودوکس` vs JSON `ارتودوکس` (normal spelling, not worth a data fix).

9 web sources archived via `fetch_source.py` (Wiktionary *deḱ-, *deḱs-, dexter; Etymonline doctor, orthodox; abadis دخش/دشن/دشت/دکور).
