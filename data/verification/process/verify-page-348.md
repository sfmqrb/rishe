# Verification process log — verify-page-348


## [2026-09-07T17:36:26.610Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 348 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-348.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-348.json. Write /home/sfmqrb/git/rishe/data/verification/page-348.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 348` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:28.542Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T17:36:29.252Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:29.268Z] TOOL RESULT

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


## [2026-09-07T17:36:29.382Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-348.txt"
}
```


### [2026-09-07T17:36:29.420Z] TOOL RESULT

```
1	=== PDF page 348 (book page 318) ===
2	--- entry 0 ---
3	ROOT [Avestan] Naěza : sharp point  (refs BQT:2226)
4	#1 (parent #0) [Pahlavi] refs=MON:4884 | nězak : spear
5	  #2 (parent #1) [Persian] refs=BQT:2226; PLA:265; SDQ:73; FSF:336 | nayzeh «نیزه» : spear, also a flag post | extra: نیژه
6	--- entry 1 ---
7	ROOT [Old Persian] Nagan, Nağan : bread  (refs BQT:2107)
8	#1 (parent #0) [Pahlavi] refs=BQT:2107; SNS:223 | nân : bread
9	  #2 (parent #1) [Persian] refs=BQT:2107; HRN:229; HUB:101 | nân «نان» : bread, food, sustenance
10	--- entry 2 ---
11	ROOT Nağan -> redirect to Nagan
12	--- entry 3 ---
13	ROOT [Indo-European] Naks, Nask : twist, twine  (refs IEC:825)
14	#1 (parent #0) [Avestan] refs=IEC:825 | naska : thread
15	  #2 (parent #1) [Pahlavi] refs=MON:4683 | nax : thread
16	    #3 (parent #2) [Persian] refs=IEC:825; MON:4683 | nax «نخ» : thread, string
17	#4 (parent #0) [Latin] refs=IEC:825 | naxae : bonds
18	--- entry 4 ---
19	ROOT [Avestan / Sanskrit] Namra : soft  (refs HRN:230)
20	#1 (parent #0) [Pahlavi] refs=HRN:230 | namr, narm : soft ; namrak, narmak : soft thing, pillow
21	  #2 (parent #1) [Persian] refs=BQT:2130 | narm «نرم» : soft | extra: نرمه ، نرمک
22	  #3 (parent #1) [Arabic] refs=VDQ:403 | namraq : pillow ; namâreq : pillows
23	    #4 (parent #3) [Persian] refs=MON:4815 | namraq «نَمرَق» : pillow | extra: نمرقه ، نمارق
24	#5 (parent #0) [Avestan] refs=HRN:230 | namra-vâxš : soft sound (voice) ☞Wekw
25	
```


## [2026-09-07T17:36:32.773Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-348.json",
 "description": "Read source JSON for page 348"
}
```


### [2026-09-07T17:36:32.821Z] TOOL RESULT

```
{
  "pdf_page": 348,
  "book_page": 318,
  "entries": [
    {
      "root": {
        "name": "Naěza",
        "lang": "Avestan",
        "refs": "BQT:2226",
        "gloss": "sharp point"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:4884",
          "words": [
            {"translit": "nězak", "gloss": "spear", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2226; PLA:265; SDQ:73; FSF:336",
          "words": [
            {"translit": "nayzeh", "gloss": "spear, also a flag post", "script": "نیزه"}
          ],
          "script_extra": "نیژه",
          "note": null,
          "quote": {"text": "جهان از بدی ویژه او داشتی - برزم اندرون نیزه او داشتی", "poet": "Daqîqî"}
        }
      ]
    },
    {
      "root": {
        "name": "Nagan, Nağan",
        "lang": "Old Persian",
        "refs": "BQT:2107",
        "gloss": "bread"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:2107; SNS:223",
          "words": [
            {"translit": "nân", "gloss": "bread", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2107; HRN:229; HUB:101",
          "words": [
            {"translit": "nân", "gloss": "bread, food, sustenance", "script": "نان"}
          ],
          "note": null,
          "quote": {"text": "زگیتی دگر هرکه درویش بود - وگرنانش از کوشش خویش بود", "poet": "Ferdowsî"}
        }
      ]
    },
    {
      "root": {
        "name": "Nağan",
        "redirect": "Nagan"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Naks, Nask",
        "lang": "Indo-European",
        "refs": "IEC:825",
        "gloss": "twist, twine"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "IEC:825",
          "words": [
            {"translit": "naska", "gloss": "thread", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:4683",
          "words": [
            {"translit": "nax", "gloss": "thread", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "IEC:825; MON:4683",
          "words": [
            {"translit": "nax", "gloss": "thread, string", "script": "نخ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "IEC:825",
          "words": [
            {"translit": "naxae", "gloss": "bonds", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Namra",
        "lang": "Avestan / Sanskrit",
        "refs": "HRN:230",
        "gloss": "soft"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "HRN:230",
          "words": [
            {"translit": "namr, narm", "gloss": "soft", "script": null},
            {"translit": "namrak, narmak", "gloss": "soft thing, pillow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2130",
          "words": [
            {"translit": "narm", "gloss": "soft", "script": "نرم"}
          ],
          "script_extra": "نرمه ، نرمک",
          "note": null,
          "quote": {"text": "من از آتش عشق هم نرم گردم - اگرچه ز پولاد سخت است دلم", "poet": "Sanâî"}
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Arabic",
          "refs": "VDQ:403",
          "words": [
            {"translit": "namraq", "gloss": "pillow", "script": null},
            {"translit": "namâreq", "gloss": "pillows", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:4815",
          "words": [
            {"translit": "namraq", "gloss": "pillow", "script": "نَمرَق"}
          ],
          "script_extra": "نمرقه ، نمارق",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:230",
          "words": [
            {"translit": "namra-vâxš", "gloss": "soft sound (voice)", "script": null, "see": ["Wekw"]}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T17:36:34.761Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','PLA','SDQ','FSF','SNS','HRN','HUB','IEC','VDQ','POK','WLD','AHD','BRT','KNT','PHD','NYB','CHEUNG','ARY','KLN','FVQ','AFM','SYN']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T17:36:36.413Z] TOOL RESULT

```
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
SDQ {"title": "A. Siddiqi, Studien über die persischen Fremdwörter im klassischen Arabisch, Göttingen 1919", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/studienberdiep00sidd", "identifier": "studienberdiep00sidd", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SDQ.txt", "page_offset": "leaf = printed + 14..15 (e.g. leaf 16 = p.1/2). local 
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaSc
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
```


## [2026-09-07T17:36:56.077Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80"
}
```


## [2026-09-07T17:36:56.090Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,120p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T17:36:56.130Z] TOOL RESULT

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


### [2026-09-07T17:36:56.136Z] TOOL RESULT

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


## [2026-09-07T17:37:03.801Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT naeza ===\"; grep -n -i \"naeza\\|naēza\\|naiza\" BRT.txt | head -20\necho \"=== PHD nezag ===\"; grep -n -i \"nēzag\\|nezag\\|nēzak\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== HRN neze ===\"; grep -n -i \"nēze\\|neze\\|naiza\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"nēza\\|neza\\|naiza\" HUB.txt | head -20\necho \"=== NYB ===\"; grep -n -i \"nēzak\\|nezak\\|nēzag\" NYB_vol2_glossary.txt | head -20\n"
}
```


### [2026-09-07T17:37:03.895Z] TOOL RESULT

```
=== BRT naeza ===
18504:•  j.  'naeza-  n.  'Spitze',  spez.  der  Nadel: avavaieii  ya%a  sBkayä  (sd.)  'sim  Yt 14-  33-
18506:•  j.  'naeza-  m.  Name  einer  Krankheit: aüalfva  daxmalha  kamiavamU  axtiica gannusla  tafnusca  'zasca  sSrastisYaV.j.SJ ; —  paiHstätSe  gamiSusca  tafttaolca  'sahe^a sarastSisca  Yt/J.  131.
=== PHD nezag ===
PHD.txt:2557:lance nēzag.
PHD.txt:5201:wizih- wizihidan wizīhišnīh wizīhišn nēzūmānīh nēzūmānīg nēžūmān nēzag wēzišn
PHD_mackenzie.txt:3717:nezag [nyck I N neza] lance.
PHD_mackenzie.txt:4561:snezag [snyeh ] snow.
PHD_mackenzie.txt:6957:lance nezag.                              leper, leprous pes.
PHD_mackenzie.txt:7603:sister xwah(ar).                              StlOW snexr, snezag, wafr.
PHD_mackenzie.txt:10166:nezag                      \ ~,,\      nirmad
PHD_mackenzie.txt:10887:snezag                               andar!
=== HRN neze ===
8939:1031. uiS&iidy nezend niedergeschlagen (trop.); elend,
13118:nezend 1031.
=== HUB ===
=== NYB ===
995:bevar [bywl] ten thousand; 2 — späh an army of 20000 men 1811-16-17; 12 ~ späh 29233; won 15 ~, 14 ~, 13 ~ 2372.17, 248-11; 131 ~ ziön äyend 24115; 12 x 12 ~ 2427; 12 ~~ 251; 3 ~ nēzak (g. v.) balas 1041, — Av. (913) baévar-, baévan-; MPrth- Prs bywr ; Arm. lw. biur; Paz. baévar ; ear- rly NP bevar.
```


## [2026-09-07T17:37:06.272Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SDQ naizak ===\"; grep -n -i \"naizak\\|naizah\\|nēza\\|nezak\" SDQ.txt | head -20\necho \"=== FSF نیزه ===\"; grep -n \"نیزه\" FSF_pages.txt | head -20\necho \"=== AFM نيزك ===\"; grep -n \"نيزك\\|نيزه\" AFM_pages.txt | head -20\necho \"=== KLN nezak ===\"; grep -n -i \"naizak\\|nezak\" KLN_1966.txt | head\n"
}
```


### [2026-09-07T17:37:06.380Z] TOOL RESULT

```
=== SDQ naizak ===
926:nezä   mp.    nezag  <  nezak)  ,    /^iS  neben  /  a.j^.ä   (=  p.  **b ,
=== FSF نیزه ===
1627: ‫ابانیزه و آبداده سنان‬                             ‫تهر‬‫خب‬  ‫همه کس پنهان داشته است‪ .‬قی‬
1645:         ‫بر آویخت با دیو چون شیر نر‬                    ‫بگفت این وبگرفت نیزه به دست‬
2244: ‫سیاوش نکر د ایچ بکاس‌مکیس‬                                                   ‫کنایه از نیزه‪:‬‬
2256:       ‫نه استد کس آن پهلوان شاه را‬                            ‫بزد نیزهگشتاسپ بر جوشنش‬
2297:                                                       ‫چو تیر اسپری شد سوی نیزه گشت‬
2408:                                                      ‫که برنیزه‌ها گردد افسرده دست‬
2531: ‫همان گرز و نیزه زبان داردی‬                       ‫اگر چند رنج دراز آورم‬
3285: ‫چه حد جنوبست نیمروز گویند و میانه‬                       ‫بسزد نیزه بر بند درع و زره‬
3296:                 ‫(نفیسی بیت ‪:)۹۲۸-۰۲۸‬‬                       ‫سنان نیزهگفتی بابزن بود‬
3882:      ‫برآمدن‪ ,‬بالای کوه و تپه روی نهادن‪:‬‬                  ‫به بالای یک نیزه برف آیدت‬
4392: ‫براندر یکی نیزه بزد چنانک هفت بدست‬
4394:‫نیزه بهپیل اندر شد و برسید تا به دل‪ .‬از‬      ‫ازین ننک دارند جنگی یلان‬
7734:‫همه کار دیده همه نیزه‌دار‪...‬‬                          ‫است که برای ارایش به خود می‌افزاید‪:‬‬
7774: ‫(‪)۶-۵۳۲۰-۲۸۲‬‬                                          ‫به رنگی دگر نیزهر پای اوی‬
7831:                 ‫نوک آهنین و تیز نیزه و تیر‪:‬‬             ‫شاه ملوک جهان‪ .‬امیر خراسان‬
8031:‫بر آزادگان بر بگسترد مهر‬                            ‫بهگز نیزه قد خصم تو می پیمایند‬
8951:                            ‫اس‬‫ز‬                      ‫می‌پیچیدند‪ .‬از جوب خدنگ تیر و نیزه و‬
10312:‫مصراع اول این بيت را عباس اقبال‬           ‫سازند و‬     ‫که از ان تیر و نیزه و زین اسب‬
10465:‫در آن حلقه کرده‪ ,‬دست راتاب داده نیزه‬
10541:‫(‪)۲-۶۶-۳۶‬‬                                                         ‫به حفتانش بر نیزه بگذاشتم‬
=== AFM نيزك ===
=== KLN nezak ===
```


## [2026-09-07T17:37:14.306Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT context ===\"; sed -n '18495,18515p' BRT.txt\necho \"=== BRT col near ===\"; awk 'NR>=18400 && NR<=18510 && /^[0-9]{3,4}$|Sp\\.|^[0-9]+ *$/' BRT.txt | tail -5\necho \"=== SDQ ctx ===\"; sed -n '915,940p' SDQ.txt\n"
}
```


### [2026-09-07T17:37:15.743Z] TOOL RESULT

```
=== BRT context ===
dby  Google
1037
naemi.rä^-
iia9^
1038
ia'^a  saota  (sd.)  g!^ä  frasrSvayaitii  *°ta (LS.)'*   *Ma%9mya   vaca  zarahustri  man>
Tu. :  Htmak  1  vaclalt,  mit  der  Erl. :  hac  iun va/tjJt  "rom  Anfang  der  Stiophe  an".  - ')  ]Ids.  '/ai  und 'ti.  —  ')  Zur  Sache  vgl.  unte xraa{iij/aA- ;  ilci  zweite  Teil  der  Strophen  wird mit  lauterer  Stimme  voigetragen.
•  j.  naemi.räO«-"  m.  'halber  Pflichtteil"*; _f«»  sai/g  at?hat  '^a  pu%ra  da^aifi  'äa anyöJkaiia  nairi/ta  dalaiti  (soll  heissen) "wenn  Vermögen  da  ist,  gibt  man  einen Fäichtteil  zur  Hälile  dem  Kind,  zur  Hälfte der  ,  .  Frau"  Nik.j.
Pü. :  . .  iarr.  —  ■)  Wohl  statt  naemö:  —  ')  Das oder  irgend  einen  andern  bef>timmten  Anteit des  Venoagens  muss  rä%a-  bedeirten  (sollen), j.  «flö-c  (Öfters);  lies  naire;  s.  nar-,
•  j.  'naeza-  n.  'Spitze',  spez.  der  Nadel: avavaieii  ya%a  sBkayä  (sd.)  'sim  Yt 14-  33-
np.  vgl.  n^a  'Speer',  woiu  Hsu.KZ.^ff.  lös. —  Npü. ;  hmän  ki  südmand  garmä  asi.
•  j.  'naeza-  m.  Name  einer  Krankheit: aüalfva  daxmalha  kamiavamU  axtiica gannusla  tafnusca  'zasca  sSrastisYaV.j.SJ ; —  paiHstätSe  gamiSusca  tafttaolca  'sahe^a sarastSisca  Yt/J.  131.
woss.  n«,  ooss.  nä  'Krankheit'.  —  Pü.;  akn
•  j.  ^aeza-  m.  (etwa)  'Klumpen,  form- lose, breiige  Masse':  yaoBit  pu%raAe  Avä- zälahe  frä  °am  nasüm  palät  paiti  ä^re ü'hftn  barst  "als  ob  er  seines  eigenen Sohnes  Leichnam  zu  Brei  verkochte  (imd) das  Fett  dem  Feuer  darbrächte"  V./ö'.  17.
El.  und  Bcd.?').  —  Pü.:  Hffin  ka  pus  i  ^ei läiai  ftäi  /«  ak  n  Bau  n  ')  nasäk  piat  t  . .  .  — O  Unwahrscheinlich  Gdn.  KZ.  3$,  4t  1  (unter
3).    -    .)    Vgl.    zu    «B^Sfl..
•  j.  naotara-  patr.  Adj.  'von  Naotara stammend,  dessen  Nachkomme':  yat  mam (nämL  aHm)  tura  (sd.)  pazdayatUa  äsu.- aspa  'raca  Yt.l?,  55;  56';  —  t?m  (nämL iiaim)  yazaia  hutaosa  . .  vlsS  avi  'ranqm Yt.  IS-  35-
Ableit.  (durch  Verschiebung  des  Worlakients) oul  *nai!tara-i^  m.  EN.  eines  Sohns  des  Ma- mife^ra.  Vgl.  aaolairy'.  —  ')  Dessen  Deutung bei  J(7STI  NB.  326  nicht  lichtig  sein  kann.
•  j.  naotairya-  patr.  Adj.,  dnw.  naotara-: tarn  (nämL  arsdvJrti)  yasmta  hvBvänfa  tarn yazftiia  'ryätthö  jStim  jaihyanla  hvö.vS , asuMSplm    •«  (NP.)  motu  pascalla  hvs.vS ,
rftr«  baon  smsta  mosu  pasiagta  *re  (KP.) Ytj.gS.
AbleiL  aus  'naotara' ;  s.  zn  naviara-.  —  >)  Statt
=== BRT col near ===
1034
Srai^ä  frmavafaicä  (sd.)  y.56.3;  —  tat a?(Akk.)  «WM7  mfättt  Y.ßS.a;  —  jaSä «J  (Akk.)  data  ,  .  aäJ  «a  %räzdBm  (Sp. 1031  m.)  %rasdBm^  «;f3  (Akk.)  Y.5Ä  J. Vgl,  zu  vayam;  ferner  nS,  nS  ah  Part.
1036
1037
1038
=== SDQ ctx ===
2)  Das  c  wird  im  Norddialekt  des  Mittelpersischen  zu  s ;  vgl. Turf.  M.  10  und  II  D.  79 :  ^^DSTÖ  (=  (^i=^).  Diese  Stellen,  wie  vieles andere,  verdanke  ich  Herrn  Professor  Andreas.
3)  So  Abu  Ililäl:  SanKwS.  192-93;  G.  53  ohne  ^.     Vgl.  v^LäsI
vi>.A«..j .  Das  Wort  Li.j»-  ist  im  Persischen  nicht  belegt,  ist  aber wahrscheinlich.  In  Persien  gibt  es  (nach  der  Mitteilung  Herrn  Prof. Andreas)  eine  Art  Eidechse,  die  die  Sonne  liebt  und  die  bei  der leichtesten  Erregung  ihre  Farbe  ändert.
—     73     —
11.  Persisches  (j*  bleibt  meist  i^^  :  ^jJ.*» ,  J^*^  (= p.  J.i^'  +  t^iCLw),  die  Ortsnamen  ^j^^,  ^j-«jli  u.  s.  w.,  wir/i doch    in    vereinzelten    Fällen    durch    (jo    wiedergegeben :
^I^  „Zimbel"  (=  p.  ^ä*.),  x^^ö  „Wage"  (=  p.  ^A-^j^^u- „wiegen").  Daneben  kommt  das  letztere  Wort  im  Arabi- sehen  auch  mit  (j«  vor.  [Das  ijo  in  >i^  {=  p.  Oy«  „kalt") ist  auf  den  Einfluß  des  ^  zurückzuführen  wie  das  c  in ■i.\^  u.  s.  w.]  ;  für  ^J»  konmit  (wie  auch  in  echt  arabi- schen Wörtern)  in  /»O;,,  o,-.    neben  j>.*«  u.s.  w.  vor.
12.  Persisches    (jä    wird    durch    (j«    wiedergegeben :
^^*?'u*M ')  (Var.  j^*5>L.i;)  neben  ^^jl*«,  ^^*w,  u«^-^?  eV.*.*/).
In  manchen  Fällen  ist  (ji  überliefert:  »LiXÄ^Ä  (schon bei  A'sä).  Aus  der  Zahl  der  Beispiele  ergibt  es  sich, daß  ein  pers.  (j^  im  Arabischen  regelrecht  (j/,  bleibt,  wo- gegen ein  pers.  (ji  zu  ^_y.  wird.  Fälle,  in  welchen  ein pers.  Ji.  erhalten  bleibt  oder  neben  ^j»  erscheint,  sind meist  jung.  Schon  Abu  'Ubaid  zieht  in  solchen  Fällen das  y*  als  das  Äquivalent  des  pers.  (ji  vor  (M.  XI  133 =  oben  S.  30).  Möglich  ist  es,  daß  man  die  älteren  Ent- lehnungen später  nach  dem  persischen  Lautwert  verbessert hat  und  das  (j^  in  alten  Handschriften  erst  durch  (spätere) Redaktoren  punktiert  worden  ist.
13.  Persisches  ^  (k)  wird  meist  durch  »,  in  einigen Fällen  durch  »i) ,  wiedergegeben :  /^-^  (=  mp.  rözik),  (j*j.jIs (=  p.  ^J^»^i^),  /^J^^3-  (=  mp.  %antak  aus  Jcäiidän,  päz.  y^an-
dan  —  vgl.  Hörn.    S.  194) ;    ü^^xä*«    (=  np.    u.    mp.    snnih, arm.  LW.   smbak   —   vgl.  a.  a.  0.  161) ,    iiL^j    (=  np.  »1*3
nezä   mp.    nezag  <  nezak)  ,    /^iS  neben  /  a.j^.ä   (=  p.  **b ,
kjS,  ^kiirbak  =  armen,  krpak.  Hübschm.  Arm. Gr.  I  173),
/äIp-s   (=  p.  MrS^  <  kurtak ,    syr.   jL^^oo  —   vgl.  Fraenk.
1)  Die  Form  ist  bei  A'sa  belegt:  Snasr  381  Vers  5.
—     7.t    —
200).  Da  der  Perser  das  li  anaspiriert,  der  Araber  aber leiclit  aspiriert  spricbt,  ist  es  sehr  wahrscheinlich,  daß das  .*  für  pers.  h  das  Resultat  des  Versuches  ist,  ein unaspiriertes  /.;  wiederzugeben.  Eine  gute  Anzahl  persi- scher Wörter  ist  durch  die  Syrer  zu  den  Arabern  ge- kommen, wo  das  '^  aus  demselben  Grrund  schon  im  Syri- schen zu  p  geworden  war.  Der  Syrer  konnte  das  persi- sche k  schlecht  durch  3  wiedergeben,  besonders  im  Aus- laut, was  oft  bei  persischen  Lehnwörtern  (mit  der  En- dung -ak)  der  Fall  ist ,  weil  der  Syrer  das  D  nach  Vo- kalen wie  li  sprach.
14.     Persisches  ^  (g)  wird  in  der  Regel  durch  _,  in einigen  Fällen   durch  i^  oder    *,   wiedergegeben:    J3  (=
p.  "^täy  =  armen,  tag  =  JL^jl)^),  ^i^xj^öi  (=  p. ^^LJCjbjJiT  <  ätur  pätakäfi,  (pähl.)  =  armen,  atrpatakan,  wo- neben au^ch  atrpayakan,  welche  Form  wahrscheinlich  den griechischen,  syrischen  und  arabischen  Formen  zugrunde liegt)  %  «L^^L  (=  p.  «1^)1),  ^L% ')  {=  p.  ^Ui^j  <  ^^Üii^j =  "JSDns  Levy :  Chald.  WB.  S.  292),  (ji^'iJ»^«  neben  ^ßJ^^y^
und  ^^^-.A  (=  p.  (ji^Ü.ij./«  neben  (ji^i'  ^\ja).
1)  Lag.  83,  Fraenk.  62,  Hübschm.  PersSt.  46  (Nr.  367)  u.  Arm. Gr.  153,  Barthol.  WB.  626  und  unten  S.  84.
2)  Hübschm.    Arm.    Gr.    23  flg.   und    Andreas    (Pauly-Wissowa's Kealencycl.  unter  Adarbigana).
3)  Das  h  geht  auf  die  ältere   persische  Aussprache   des  Wortes zurück.
75
Auf  welchen  Wegen  wanderten  persische  Wörter zu  den  Arabern  vor  dem  Islam?
Persische  Wörter  machten  ihren  Weg  ins  Arabische größtenteils  durch  das  Aramäische;  die  meisten  der  von den  Syrern  gebrauchten  persischen  Wörter  drangen  auch in  das  Arabische  und  zwar  mit  derselben  Lautverschie- bung wie  die  echt  aramäischen.  So  gibt  es  im  Sjrrischen nur  wenige  persische  Fremdwörter,  die  nicht  auch  im Arabischen  vorhanden  sind ').
```


## [2026-09-07T17:37:15.975Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 1030/nan ===\"; grep -n \"1030\\.\" HRN.txt | head; echo \"---\"; sed -n '8920,8945p' HRN.txt\necho \"=== HUB nan ===\"; grep -n -i \"nān\\|nan '\\|Brot\" HUB.txt | head -30\n"
}
```


### [2026-09-07T17:37:16.051Z] TOOL RESULT

```
=== HRN 1030/nan ===
13163:Mtiät? 1030.
13164:nizade 1030.
16463:iiü^ufr 1030.
---
1028. nerm "weich, sanft', nerml,
ai. namrd' "sich biegend, unterwürfig, ehrfurchts-
voll ergeben; aw. namra.vä/ä (7jPQI,)?; phlv. narm
'weich, sanft*.
LW. kurd. nertn, zaza nemr "weich, sanft*; afy.
bei. (178) wa;^. narm.
1029. ne^^d "nahe', nezdik^ nezdiki,
aw. nazda- "nahe ; phlv. nazdik, nazdist; ai. nedl-
yas-, nedisfha-.
kurd. nizüky nezTk "nahe*; af/. nizde, nizde; bei.
nazlk, n. nazl/, nazi (256) ; sar. nizd.
*) Reimt auf niskerid, Öähn. I, 166 Vers 675.
2) Rücke rt hatte ZDMG. 8, 286 an ai. pidr (d. i. *pizd') ^drücken,
pressen' gedacht.
^) Die BelegstcUe vordanke ich Herrn Prof. Nöldeke.MI
— 231 -
WSO, niiad 'Geschlecht, Abstammung, Adel' *), nizade 'von
adeliger Abstammung 2).
aw. ^nizäti", vergl. skr. Jati-.
1031. uiS&iidy nezend niedergeschlagen (trop.); elend,
niedrig*.
ap. *ni -h l/yaw- niederschlagen*, also etwa ein ap.
*/ii/a«/M- 'niederschlagbar voraussetzend, vergl. indische
Bildungen auf -tti- bei B. Lind n er, Altindische Nomi-
nalbildung, 8 54, Ib (S. 80).
Unsicher.
=== HUB nan ===
774:-um wird, vgl. nu *Brot', num *Name'etc.), ka§. bun^ bdn,
1965:502. Dazu np. nctnx^ah 'Ammi' u. s. w. als *Brot-wurze',
2357:629. Np. rozl *das t^gliche Brot' ist direct = phi. rddTk
3233:rundes Brot' ^= arab. jardaqa im Armenischen als
3234:grtak *Laib Brot', das ein phi. *girtak voraussetzt.
4657:Vahram^ alter Varahran = zd. vere&rayna^ ; nOn *Brot* aus
4941:'Gerstenbrot' = arm. Raskin; GurgTn N. pr. = arm. GurgSn^)
5082:skr. krta-, vgl. § 7; girda 'rundes Brot' = arm. grtak
5083:'Laib Brot'; xirs 'Bar = zd. aresa-, skr. rkSa-; gdgird
5219:Brot* = np. girda; krpak 'Werkstatt, Laden' (Apg. 28, 15)
5525:vart geh5rt 0, zu der es sonst passt. Np. girda rundes Brot'
5526:lautet im Armenischen grtak 'Laib Brot* und setzt ein ap.
8054:rocik = np. rdz% *das tagliche Brot'; razan Tenster =
8490:kaskm Gerstenbrot* = arm. Ua^k^n (EliSe); laskar *Heer*
8925:d^rayna-; ndn *Brot* aus *wayna-?, vgl.
```


## [2026-09-07T17:37:30.834Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 8915-8935 ===\"; sed -n '8905,8940p' HUB.txt\necho \"=== HUB 4645-4665 ===\"; sed -n '4645,4670p' HUB.txt\n"
}
```


### [2026-09-07T17:37:30.882Z] TOOL RESULT

```
=== HUB 8915-8935 ===
Jahr 430 bezeugt, ZDMG. 48, 413.
§ 142. Fiir ap. g erscheint h in:
Bahistun {Y9Lq\x{), gr. to Bayiavavov iigog (Diodor II,
13, 1) in Medien, urspr. = *bayastana' 65tterort\ Das
Wort ist also medisch. Ueber nuhuftan siehe oben p. 103.
8 143. Geschwunden ist y = y in den Konsonanten-
verbindungen :
a) gm = ym (nach Vokalen): amadan *kommen*, phi.
matan, ptc. mat Gl. and Ind. 210, gd.
dgemat, zd. fraymat, ap. ha(n)gmat(l,
paragmata; scheinbar auch in np. Hama-
dan = arm. Ahmatan, bei Esra NHOnN,
* * •
bei Herod. 'Ay^drava, ap. Hagmatdna-
(= Haymatana-), Aber Hamadan ist erst
aus phi. Ahmatan =*Hahmatan (§ 107, b)
entstanden, hier also ap. gm ~ ym (im
Inlaut) zu hm geworden.^)
b) gn = yn (nach Vokalen): np. Bahram = phi.
Varahran = arm. Vahagn = zd. vere-
d^rayna-; ndn *Brot* aus *wayna-?, vgl.
bal. nay an etc. (oben p. 101). Dagegen
ist y geblieben in rOyan zerlassene
Butter = zd. raoyna-,
Ueber dlvar siehe oben p. 65; iiber padtrnftan ■= phi.
patgraftan oben p. 38; varzdv = varzgav H. 197. Ganz
unregelmassig ist die Entwicklung von g in dem Parther-
namen Vologeses = syr. ValgeS ^ phi. Valgas um 130
p. Chr. (Gardner, the Parthian coinage p. 56 — 57), Valaxs
') Anders Andreas in Pauly^s Realencyclop. s. v. Apobafana:
HtnnaSdn = Ahmatan = *Hmafatta {ftarnra bei laid or) — ap.
Haymatana-,= arm. Valars = np. BaM, syr. ^Dli^^D i. J. 430, ZDMG.
43, 409 ^ gr. BoXoysaltpopa Tab. 134, Hoffmann, Ausz. 67.
Kapitel 26: ap. x.
Ap. X {== arisch kh und vor Konsonanten = arisch k)
bleibt im Np. als x,
=== HUB 4645-4665 ===
c) Wechsel von a mit a durch Umspringen der Quan-
titat: x^'dhar *Sch wester' = phi. x^ahar aus *x^ah(lr (vgl.
bal. gvahar, aber nb. gvahar), ap. ace. *(h)uvaharam = skr.
svasaram (aber zd. x^atlharem nach pitarem u. s. w.); ftoASf
Triihling' = ap. vdhara- in ^ravflAora-?
d) Ap. a wird durch Ersatzdehnung zu np. a:
Np. paz. phi. Maraspand (Noldeke, Tab. 362, Shk.
258, Gl. and Ind. 209), arm. Maraspand (Mos. Kal. I, 258)
= zd. mq^rem spentem; np. tOr *Aufzug beim Gewebe* =
zd. *^(jdra-, skr. tantra- *Aufzug ; np. paz. phi. tar 'finster
= zd. tqSra-, skr. tamisra-- ^Dunkel'; hazar *tausend' =
ap. *hazahra-, zd. hazafira^, skr. sahasra^\ BaArflm = phi.
Vahram^ alter Varahran = zd. vere&rayna^ ; nOn *Brot* aus
*nayna' ? ? ; . Bistam aus Bistahm = Gustahm (N Q 1 d e k e ,
Tab. 96); np. §ar *Stadt' = sahr, saristan = Sahristan.
Fiir a&r = ahr ist schon in alter Zeit unregelmassig
ir eingetreten in ArdaSfr, arm. Artasir (sassanid.), phi.
Artaxslr^ alter arm. ArtaSSs, alter phi. ArtaxSa^r etc., siehe
§ 96, b.
§ 10. Ap. a ist nur scheinbar zu mp. np. a geworden,
in Wahrheit war a schon im Altpersischen vorhanden in:
a) den Kompositis mit pa-, pad-, phi. pat- = ap.
*pati', Nebenform zu pati- (wie zd. paiti- in paitivoJca-
*Gegenantwort' Nebenform zu paiti- ist): np. pazahr =
podzahr (bei Vullers und Polak, Persien II, 275) *Gegen-
gift*, paz. pad(a)zah(a)r Shk. 261 ; np. paz. pasux *Antwort*,
```


## [2026-09-07T17:37:33.026Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN nan ===\"; grep -n -i \"n[āa]n .Brot\\|nān\\b\" HRN.txt | head -20\necho \"=== HRN 1027 ===\"; grep -n \"1026\\.\\|1027\\.\\|1025\\.\" HRN.txt | head\necho \"=== PHD nan ===\"; grep -n -i \"^nan \\|nān\\b\\|bread\" PHD_mackenzie.txt | head -20\necho \"=== NYB nan ===\"; grep -n -i \"nān\\|nan \\[\" NYB_vol2_glossary.txt | head -20\n"
}
```


### [2026-09-07T17:37:33.130Z] TOOL RESULT

```
=== HRN nan ===
=== HRN 1027 ===
8899:1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
8909:1026. ner, nerr (AM.) "Mann; männlich', nere [nerre), nenne
8915:1027. nirx, nerx "Preis, Wert' (z. B. Schefer, Chresto-
11531:rtjcerrf 1025.
11533:ämefdgäh 1025.
12798:/^i*/(!n 4H2, 1027.
12956:nebfrd 1025.
12959:f/t6ri</e 1026.
13043:ner 1026.
13046:|n«-e 1026.
=== PHD nan ===
2070:2dron [d1wn I N darun] consecrated bread, ceremony in which c.b. is
2075:dron yaAtan: consecrate the sacrificial bread.
3665:nan [LIlMA < A l/:tm); n)n l 1 = M, N --] bread, food.
3982: --ay [~'d I N ",a] width, breadth.
4439:rozig [lwc)'k ' I N r()zi] daily bread, sustenance.
5314: ......ih: width, breadth.
6119:bread nan; daily - rozig.              burrow surl'ig.
6120:breadth pahnay, wehmih.                bUT1"owing sudgig.
6255:consecrated bread dron; ....., drink         coralline wassaden.
=== NYB nan ===
305:subst. the pious, righteous man 651%, 732.24; pl. cas. obl. ~-dn: ~-dn marian zanān 53%; ~-dn alone 634, 7322, 8835, 10121, — 3. blessed, of those in Paradise 8624; subst. pl. cas. obl. ~-dn the blessed 87%, — Borrowed from Av. (246 sqq.) ašāvan-, nom. ašavā; MPrthPrs (Zoro- astrian term) ’hlw, pl. ’hlw’n (A-H II); as to the correspondence -š-: -hl- v.s.v. Mahlāh; Paz. ašē, pl. ašēg. V. ahlav-dät, ahlài, ahlayéh. The genuine WIr form is OP artdvan ‘blessed’, whence MPrth ?rd^w ‘righteous, veracious’, also borrowed in MPrs (A-H II); v. further artäk.
740:Aškānān [’Sk’n’n'] patron. of the pre- ceding name 10815. 11415-26, — NP Aška- niyan; Arab. al-xaskäniya (read -x- in- stead of -h-) and al-asgäniya, Fihrist 32'730.31,
1256:én apčcak ~ i mäzdesn 244; veh ~ 4 apčcak 5914; (En) apécak veh ~ 4 maz- desnān 819. 844; ~ i Ohurmazd 60%; ~ stayitan, ~ yastan: v. these ws; — in particular: the authoritative canonical texts of this religion: én ~, cigon hamäk apastak u zand namely, the whole Avesta and commentary 1078; the quotations from these texts are introduced by the following formula: cigén ~ göbet followed by ku 3613-14, 421-13, 4520, 4615, 484-18, 491-16. 5224, 53%. 541-17; followed by hat (q. v.) 387-8. 4375-26, 4414-15, 503-5; without following particle 41196; (7) cigon et i ~ gobet ku 5323-24, 563. 581. 608. 617-8; cigon pat ~ 7718, pat hàn i ~ göbet kū 4345; andar ~ guft estet 8011; an-ic ~ gobet ku 3819; hac ~ (čičn) paitäk kü 341. 8612-115; cigón hac apécak veh- ~ i mäzdesnän paitäk 819-9; v. further paitäk and paitakéh; v. also s.v. dipivareh. — Av. (662 sqq.) daenä-; Arm. lw. den; MPrthPrs dyn religion, religious community, church; Paz. din. — Cf ak-dénéh, dén-burtàr, denik, dušden, huden.
1294:1ditan [dytn'; HZYTN-tn', inscr. and Ps. HZYTN-] vén-, 2nd p. sg. HZYTN-yd = vënë 7164. HZYTN-h = venah 31°; subju. lst p. sg. HZYTN-n = vēnān P2: 10: to see, to regard, to catch sight of, to contemplate, to discern, to experience: ayāftan u ~ u dänistan 88°; dänäkıhä ~ 51; pat venisn ~ 5013-1; pat (xves) cašm ~ 7479, 80%; — with ki that 115. 127 ete., with ka that 40%; — with a pt. as its complement: -m murtak dit han tahm spähpat I saw this valiant general slain 2719-11; 2 zan nisastak dit 6"; with an adj. P2:10. 2719. 5776 sq. (purr com- ` plement); — with an indir. interrog. clause: ~ kū . . . cigēn to see how 2518-19; ka-t dīt kū kas kē ... kart 137-9 a contam- ination between ka-t dit ku kas
2127:kart ēstēt, cigön Dahäk u Frāsyāp u Väman [thus Cod. DH; TD w’tn', Paz. vätan, perhaps for Väöarjä the father of Vaman, Tab. I, 530 init.] u apārīk hac én āivēnak marg-aržānān, pātifrās [+ Paz. vama, probably a misspelt Vaman] 10 ātvēnak-ic vitārēnd ‘those who have in- stituted their own *laws for mankind, as D. and F. and V. and other death deserving men of that kind, will undergo ten sorts of punishment’. For the whole passage cf Phl Vd ad 75? (p. 279).
2343:*kurtīk, pl. cas. obl. kurtīkān [kwltykn!'] villeins, slaves or bondmen employed in different occupations on, an estate: ~ šu- pānān slave shepherds 1°. — I follow the reading of Antiä, whose text reproduces the basic MS of Kn, that of Mihrapan (v. I, p. XII). S. has kurtān ‘Kurds’ (ef kurtān šāh KnS V, 1). Itis of course pos- sible that ~ is ultimately derived from the national name of the Kurds, who were notorius nomad  cattle-breeders (BQ notices kurd in the sense, inter alia, of cūpān(ān) and gēsjand-carān) but it cannot have an ethnie sense here. The narration presupposes that Sasan was a slave within easy reach of Papak, to be summoned. into his presence at any mo-
2909:followimg kü-sentence: cigén hac an giyāk ~ 4574-25; cigon hac apécak vēh-dēn 4 māzdesnān ~ 8189; — in a general sense, without reference to the canon: the
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3200:raftan [SGYTN-tn'; Iptn'] rav- [SGYTN-; lwb-, cf ravišn; lw-], imp. rav [SGYTN] 38° etc., ravé [SGYTN-yd] 44!; pres. 3d p. pl. SGYTN-nd = ravénd, e. g. 87°, but lwnd = ravand 20%: to go, to walk, to proceed, passim; with prep.: apak kurti- kānšu pānān raft he lived among the slave shepherds 19-10 (cf s.v. kurtīk); apak
3336:radišn [Iwdšn'] 1. (living thing) which is to grow: 1. pl. cas. obl. ~-dn: harvisten zāyišnān u —-än all (living things) which are to be born and to grow 88°. — 2. abstr. ~ u vaxsisn i urvarän growth and increase of the plants 899-1°. — Paz. rēšn.
3919:| Valaxš [wlhš] n. pr.: ~ 4 Aškānān V. of
4343:x"arrah [GDH] a divine essence, a special form of the Eternal Light, a splendour, a glory I. manifested in the gods: one swears by (pat) ~ % Ohurmazd bag u den imāzdēsnān 2117-22-28 (without bag). 2321-22 ; zor u ~ + visp-ākāh spēnāk meno datar Ohurmazd 1063-24, — 2. a cosmic essence 9215.19, — 3. Zartuxst’s divine essence 36-38. 43-45 passim; the elements con- stituting his individuality are his ~, fravahr and tan gohr 433-18; his rdi u ~ 51-52; v. also s: v. purr. — 4. the splen-
4457:yūnānāyik [ywn’n’yk] adj. Greek 11114. — OP yauna- ‘Tonian’.
```


## [2026-09-07T17:37:41.713Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB nagan/nayan ===\"; grep -n \"nayan\\|nagan\\|naySn\\|na^an\\|nayna\" HUB.txt | head -20\n"
}
```


### [2026-09-07T17:37:41.764Z] TOOL RESULT

```
=== HUB nagan/nayan ===
3551:nicht zu nan. Bal. nagan etc. setzt Iran, "^nagan^
3553:"^nayna- erklaren.
4658:*nayna' ? ? ; . Bistam aus Bistahm = Gustahm (N Q 1 d e k e ,
8653:dWnagan^) (aber np. danayan^) u. s. w. Sal. Shuk. Gr.
9718:p. 87, Nr. 842 — 845. Np. buzina (im pi. huzinagan) schon
```


## [2026-09-07T17:37:42.121Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC naks ===\"; grep -n -i \"naks\\|nask\\|naxae\\|nexus\" IEC.txt | head -40\n"
}
```


### [2026-09-07T17:37:42.174Z] TOOL RESULT

```
=== IEC naks ===
7542:koksó (1) ‘squeeze, constrain’. Skt. cf. káksyam ‘girdle’ beside (variant) kačā- mi 'bind'; Av. kaš- ‘bind’; Arm. koxem ‘squeeze, mangle, tread’; kox, koxan, s. ‘tread’; Ir. coscaim, coiscim ‘restrain’; cosc (restraint. Consonantism as in Ír. nasc *bond': Lat. nexus)
8573:Kas- (1), (Kasnos) “grey, white; grey or white creature or plant'. WP I, 357 Lat. canus ‘hoary, frosted, white-haired'; Osc. cf. casnar, m. old man'; Gk. cf. also kolo- kasía *hoar-wort'; OHG hasan, adj. ‘grey’ be- side haso, m. ‘hare’; OE hasu, heasu “grey, ashen’ beside hara, wm. ‘hare’; paroxytonic in E haze and in MHG heswe ‘pale’ (LW in Fr. háve, id.), but oxytonic in Scots har “low mist, suspended mist’; ON boss, acc. hosvan, adj. “grey, of wolf; G cf. Hasel, Hásel 'grayling'; Finn. LW harjus,id. Assimilated consonants in Skt. $a$áh “hare? owing to association w. Sasami “jump”; OPr. sasins ‘hare’. Cf. W cei- nach ‘hare’ if for *Kasinaks-
11509:(nàio ‘swim, float implied in Tokh. B nask- ‘bathe’ beside ambig. Lat. no, nare, pf. navi ‘swim’, but see snā- below; Alb. ambig. cf. not, m. (swimming, floating’ and notoj, v.: Lat. natàre, qua *nàt- or *snàt-)
11512:nāk- (naks-) (3) ‘come, arrive, reach, suf- fice’ Lat. cf. nanciscor, nactus, v. “find, get, reach’; OHG gi-nuogi, -nuog, adv. ‘enough’; OE nog, noh, id.; nogian, v. abound"; Big. cf. nax, prp. (towards < *nàks-); Li. nokstu, nokti, v. (‘mature’, lit. arrive); pra-noku & -nokiu, -ti ‘catch up’; Li. nāku, nākt ‘come, happen. (Un- related are Av. nãs- (2) ‘reach’ and OE nugan, 3s: neah ‘suffice’, cf. neks- ?nequ-)
11513:naks- (nask-) ‘twist, twine, torque, tress’. Cf. nekstos
11522:Av. naska-, id.; Per. nax ‘thread’; Gallo-Lat. naxae (‘bonds’, misspelt ‘noxae’) beside naxa, nassa “bownet'; Olr. & Ir. nasc, pl. naisc, m. (“collar, chain’, also in Ir. ‘ring, bracelet, tie, band, bale); Br. nachen, pl. -nneü, f. ‘tress, ribbon’ beside nask, pl. u, m. ‘tether’; OE næsc (mng. uncertain). The composition of OHG nestilo “fillet, snood, band”; OFris. nestla, wm. id.; MHG nestel, sf. id. is uncertain, but cf. the W simplex of type *nastis in nais, pl. neisiau, m. “band, tie
11538:nask- see naks-
11539:nast- variant of type nask-, naks- in W nais, pl. neisiau, m. ‘band, tie’; cf. OHG nestilo, wm. ‘fillet, snood, band’; OFris. nestla, wm. id.; MHG, G. Nestel, sf. id.
11576:negh- (negh-?) ‘bind’. Evidence ambig. Skt. nahyàmi, v. id.; Av. naz-, id.; Per. cf. naž ‘wards of a key” (?); Srb. cf. (?) negve ‘fetters’; ON cf. nist, n. brooch’, if fr. *neghst-, but WH and Kluge otherwise, see necto, Nestel); Lat. extn. in necto, pf. negt, sup. nexum ‘bind’ beside nexus, nexa ‘join’. O-gde prob. in OHG *nastila, actually nestila, f. & nestilo ‘bang’. (FK:EWDS: Nestel improb.)
11604:neksos, us (1) “bond, tie’. Cf. nekstos, naskos & neKsos. Variant: nesk- Tokh. (?) nasu ‘friend’; Lat. nexus, gs: -üs, m. ‘tie, band, bale’; Ir. neasc, m. id. (beside nasc ‘collar’: Br. nask); W nais, pl. neisiau, m. id. beside naith, pl. neithion, m. ((2) “betrothal, fr. *nekt- or *nekst-); G. cf. Nistel, f. 'band- age; buckle-beit; lace; shoestring’ (beside Nestel, id. fr. *nast- or *nakst-); ON nist, nisti, n. "brooch: pin” beside nezla, f. (“button- hole”, i. e. *netsla! perh. fr. *nakstila). (Fr. nasse *fish-basket! is a LW, perh. Gallo-Lat.). Cf. Av. nasko, m. ‘chapter, section’
11621:neKs- (neK-, neKst-) ‘approaching; near. (Variant: neks-). Cf. WP I, 59; I, 129 & II, 328. Cf. neksos, nekstos Per. cf. naxün (first. LW in Arm. nax first); nuxust, adj. “first, beginning’; Tokh. A nes, B naus, invar. adv. ‘earlier; Vedic cf. násami, Skt. nasSayami, v. “reach, approach’; Av. cf. nãs-, v. (2) ‘reach’; uncertainly to Tokh. A nasu "Trend: variant (*neks-) in Skt. naks-, Av. é-nak&-, v. ‘reach’; Lat. cf. nec-esse "to be necessary’; Osc. cf. nistrus, acc. pl. f. ‘nearer’; nessimas, fpl. (nearest, hence *near); Mir. nessa, mod. neas ‘nearer’; nessam, adj. “near- est; com-nessam, m. ‘neighbour’; W nes, Br. nés, néz, Cor. nes, adj. & adv. “near; nearer; W nesaf, adj. ‘next’. (The connexions of Go. néhw-, G nach, nah, OE neah are uncertain, but do not belong here)
11780:847 nnt-, (nntið also pí-naks, -nakos, m. “writing-tablef”; dó- naks, -nakos, m. ('two-thrust, hence “split quill, reed, arrow’); trí-naks, m. ‘trident’; cf. bo-nassos “wild bull’, fr. *guou-nnkios) and perhaps wá-naks, gs: -naktos 'ruler' and aga- naktéo (‘be incited’. Cf. ngnt- for px.); Pol. nekac, inf. ‘oppress’; Cz. v-nukat, v. ‘impress’, from *nonk-
12760:the night; MHG ver-nahten, v. id.; OCS pré- noStujo, -evati, v. id.; Li. per-nàkt, adv. “through the night’; cf. per-nakvoti, inf. ‘spend the night; Latv. cf. par-naktim, parnaktis ‘night after night’; pàrnakSot, inf. ‘spend the night
16531:snàió (3), snàmi “wash, bathe, swim, float. WP II, 692 Skt. snami, pp: snatab (1), and snàyami, v. id.; Oss. nain, pp: nad, v. ‘bath, bathe’; Tokh. B cf. nask, v. id. (fr. *nasK- rather than *snasK-); Gk. naío, náð, v. (ambig.) (“flow?. Cf. nàio); cf. also Gk. nékho, nekhomai, v. ‘swim’; Alb. not ‘swimming’; bie not, as v. ‘swim’; Lat. nó, nare, v. pf: navi, id.; MIr. snám, Ir. snámh, s. ‘swim, swimming, floating? beside Mir snáim, v. ‘swim’; Br. noei, noeni and noenvi, inf. id.; W nawf, m. pl. nofion ‘swim’; nofio, v. ‘swim, float, make swim’. (NB. Forms with- out initial s- are ambig. Cf. nàio; isophonic: Du. and EMDu. snoeien, v. 'trim")
```


## [2026-09-07T17:37:51.926Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC 11505-11530 ===\"; sed -n '11505,11530p' IEC.txt\necho \"=== nearby page markers ===\"; awk 'NR>=11400 && NR<=11560 && /^[0-9]{3,4}$/ {print NR\": \"$0}' IEC.txt\n"
}
```


## [2026-09-07T17:37:53.022Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT naska ===\"; grep -n \"naska\" BRT.txt | head -20\necho \"=== PHD nax ===\"; grep -n -i \"^nax \\|thread\" PHD_mackenzie.txt | head -20\n"
}
```


### [2026-09-07T17:37:53.184Z] TOOL RESULT

```
=== IEC 11505-11530 ===
825
na “well, so, now, behold, thew (a sentence particle) Ober. na; Arm. na; Gk. nà, né; Alb. na; Lat. cf. nam; Sard. na; G na; R no ‘but; Cz. no ‘why yes, indeed’; a-no “yes” (cf. a above); Li. nà, ná; Latv. na; W cf. (redup.) nan, id.
nad- (nod-?) ‘wet; water, water, Cf. not- Skt. nadih, f. ‘water’; Go. cf. natjan, v. ‘wet; OHG nas, OS nat ‘wet; G nass, id. beside netzen, v.; Sw. cf. nate, wm ‘duckweed’ and perh. Per. nai, nay ‘reed’
nai “indeed”. Cf. na and i Gk. nai, Tokh. A ne, B nai, id. Lat. (fr. Gk?) nae, id.
(nàio ‘swim, float implied in Tokh. B nask- ‘bathe’ beside ambig. Lat. no, nare, pf. navi ‘swim’, but see snā- below; Alb. ambig. cf. not, m. (swimming, floating’ and notoj, v.: Lat. natàre, qua *nàt- or *snàt-)
näk- (1) “press, cram, burst’. Cf. nnk (nonk-). Gk. ambig. Gk. násso, adj: naktós, id. (fr. *nak- or *nnk-); OCz. v-noCiti thrust; Li. niokiü, ti ‘burst, break up, squash, tousle’
năk- (2) “cover, hide” Skt. cf. nåkah, m. “vault of the sky'; Gk. ná- kos, náke, mf. “goatskin, fleece'; Br. naka, inf. ‘cover, hide, dissemble’
nāk- (naks-) (3) ‘come, arrive, reach, suf- fice’ Lat. cf. nanciscor, nactus, v. “find, get, reach’; OHG gi-nuogi, -nuog, adv. ‘enough’; OE nog, noh, id.; nogian, v. abound"; Big. cf. nax, prp. (towards < *nàks-); Li. nokstu, nokti, v. (‘mature’, lit. arrive); pra-noku & -nokiu, -ti ‘catch up’; Li. nāku, nākt ‘come, happen. (Un- related are Av. nãs- (2) ‘reach’ and OE nugan, 3s: neah ‘suffice’, cf. neks- ?nequ-)
naks- (nask-) ‘twist, twine, torque, tress’. Cf. nekstos
na — nark-
15
20
25
30
35
40
826
Av. naska-, id.; Per. nax ‘thread’; Gallo-Lat. naxae (‘bonds’, misspelt ‘noxae’) beside naxa, nassa “bownet'; Olr. & Ir. nasc, pl. naisc, m. (“collar, chain’, also in Ir. ‘ring, bracelet, tie, band, bale); Br. nachen, pl. -nneü, f. ‘tress, ribbon’ beside nask, pl. u, m. ‘tether’; OE næsc (mng. uncertain). The composition of OHG nestilo “fillet, snood, band”; OFris. nestla, wm. id.; MHG nestel, sf. id. is uncertain, but cf. the W simplex of type *nastis in nais, pl. neisiau, m. “band, tie
nām, sentence particle “but, or’. Cf. na Skt. nàma; Lat. nam; cf. quis-nam; OCS ng, cj. "but
namn- (nam-?) ‘curse, blame, guilt Av. nomo, obl. -åhb-, n. ‘guilt’; Alb. nàm, T nëm, v. ‘curse’; Br. namm, m. ‘blame, stain, vice’; Cor. nam, m. ‘flaw’; namma, v. ‘blight’; W nam, pl. au, m. (1) ‘blemish, fault’; Ir. cf. namha, gs namhad, ds & npl. namhaid (fr. *namnont-) (?) “bane, enemy’
(namð(n), nəm- ‘name’, a variant formula for Av. náma, n.; Go. OE namo, nama & com. Gmc. For Skt. etc. see onoómn-)
nanå “mother, nurse, foster-parent'. WP II, 317 Skt. nanà ‘mother’; Per. cf. nānā (“maternal grandfather' sic!); Oss. naná *mother, grand- mother; Gk. (expressive) nánne ‘maternal aunt; Alb. nán&, T nënë ‘mother’; W nain, pl. neiniau, neinoedd ‘grandma’; neina, f sg. id.
nardo, Indo-Iran. variant of type narnó, q.v. Cf. snar-
Skt. nardami ‘growl, roar’; Per. nalam, idan, v. ‘lament
narK- (?) ‘seizure, grip, torpor. Cf. WP II, 701 Gk. nárkë, f. ‘torpor’; Alb. cf. narth, v. “feel cold’; i nerthté, adj. ‘freezing cold’; Sw. cf.
827
=== nearby page markers ===
11410: 818
11422: 819
11442: 820
11454: 821
11473: 822
11480: 823
11495: 824
11505: 825
11521: 826
11530: 827
11548: 828
11552: 829
```


### [2026-09-07T17:37:53.239Z] TOOL RESULT

```
=== BRT naska ===
24661:ß  i^aiStih  /röl  hiSihFt  -  tiräk  aÜHÜk  J>a harvisp  vinaskarih.  —  0  iSchr.  s.  ^myaiirä.' iatana-  No.  a  und  Cld.  KZ.  33.  593.
=== PHD nax ===
4404:riital\ [1(y)ltk ' I N ""'0] rope, string, thread.
4876: tadan, tan- [ttn', tn- I N tan-] spin (thread).
7767:tend pahrextan.                           thread ristag.
```


## [2026-09-07T17:38:03.891Z] TOOL CALL #17: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T17:38:03.897Z] TOOL RESULT

```


```


## [2026-09-07T17:38:06.240Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT nask ===\"; grep -n \"Nask\\b\\|naaka-\\|nasfca\\|'naska\" BRT.txt | head -20\necho \"=== BRT namra ===\"; grep -n -i \"namra\" BRT.txt | head -20\necho \"=== BRT nam- bend ===\"; grep -n \"nam-.*biegen\\|namah\" BRT.txt | head -10\n"
}
```


### [2026-09-07T17:38:06.347Z] TOOL RESULT

```
=== BRT nask ===
1898:Aogsmadaeca;    HaäöxtNask;   Vistäsp  Yast;   NlrangiAtas;   Fragmente.  xxi
=== BRT namra ===
6388:•  j.  aäsmao^'a-  (Adj.  'der  das  heilige  ■  auch  Josti  NB.  ik.  —  o  Ein  wenig  sinnvolles. Recht  verwirrt',  als)  m. 'Verbreiter  ketze-!  ^^  "'"'"  und  j''  r'  nicht  lusammengehören. rischer  Lehre,  Irrlehrer">:  j'J^jföffi /«(Vi- ,  •  j-  aSam  vohu  (oder  «•  v  vahis'bm kanamra     s3>ram     kaoyam     kära/nam'a  \'"f^)-   wird  das  damit  beginnende  Gebet
9128:kaTucS  vlltaspö  Y.^j.a;  —  iava  vistiispö Ytj.  io8  usw.5>;  —  kavaitn  kaviltim  Yt IQ-Ti  usw.»;  —  iavöii  aipivai^A)us  \t. Ij.i3^  nsv/ß;  —  kai'aSm  usaöaium  Vt. 1(^-71  usw.**;  —  kti7-a  usa  VLJ.4S  usw.; —  iavdis  arsnö  Vt.  13.132  usw.** ;  —  iarms fisinaulß  Vt  JJ.  13z  usw.";  —  kavöis byarsiinS  Vt;_j.  132  usw. 5';  —  iavaim syävarsämm  Vt. /fj.?!  usw.*';  —  kavoU haosravaijhahe  Ny.  5.  5  usw. 5';  —  yat baun  Vispe  *d,iri'i.Aaire  kai'c  (NF.)  Vi.  /(?. 71*'.  2)  jAw,  Name  für  gewisse  Feinde des  Volks  und  Glaubens  der  Masdayasn^T: vTspamitn  tbihatqm  tbuuiii  diUvunam  mai- yänamra  y'f'ircum  pairikannmi'a  sä^rmii iaoyiim  {Gl'.)    'iara/nami'a 'Y.  (/■  tS;    Vt.
=== BRT nam- bend ===
18196:i)  'einen  Gott  befriedigen,  durch  Liebes, das  man  ihm  erweist,  gnädig  stimmen,  um seine  Gunst,  Gnade  werben  mittelst  — ' (Insti.);  a)  mit  Akk.:  iä  ns  (näml  fra- vasTs)  staväf . . yasäile . .  u/y3/ . .  */nnäi . . ptüti-zanäi  gaomata  sasta  Yt  13.  50;  — yä  vS  (näml.  apB)  .  .  atam  .  .  tUlmam* dttdui  tat!  vS  yasamaidf  .  .  *ßyanmahl' . .  mmahyamahl  .  .  ÜaidyamahT  V.3S.4 —  xbayamahi  Jrtnamahi  rasnüm  Yt  J2- S;  3.  b)   mit   Dal.    (auch  mit  s):  yS
18969:•  j.,  g.  'namah-  n.  'Verehrung,  Ehrerbie- 1 tung,  Huldigung,  Ehrfurcht{sbezeigung)':  | parinavö  .  .  m^vyaAe  .  .  patmrva  hl  °mö  '■ baraiti  paourva  sfartnä  "wer  eine  Feder  \ des  . .  Vogels  hat,  der  gewinnt  sich  zuert Huldigung  .  ."  Yt.  14.  36;  —  sonst  nur  in ' Beziehung  auf  Gottheiten  gebraucht:  haomö .  .  yakmäi  kvan  .  .  dural  'mS  l/ao6ayeiü  1 Yt.  jo.  90;  —  namistaAyä  {sd.)  °maaAä'^ fiii  .  .  paitJ.jamyä  Y.jß.s;  ~~  tat  vS  11}  \ hazaosanks(f.d.)  . .  daiäySi  savH  ahm  vohü\ manatihä  .  .  yaz:>mniN/iS {sA.)  °mai^h3''*\ Y.j/.  20;  —  at  töi  myazdtm  ..  'maahä^ .  .  däm3  (sd.)  y.^^.  3;  —  tsm  ttS  staotais 'maahS  ^a.vlvanlö  (sd.)  Y.  45-  8 ;  —  'maaka  ' aoara  data  ajasani  upara  data  Yt.JO.  118; 118;  —  mi%rim  . .  pairi.jasäi  vantaca 'maahaca  Yt/o.  6;  —  kn  nS  (näml.yVa- Tialls)  stavät  .  .  asa.näsa  "maaha  Yt.  /J. 50; —  'maAT  fySntä  *akura.mazdä  'mahi (LS.  als  Inf)  usSmahi  'mat»ki  (DS,  als Inf.)  vTsilmaidJ  "wir  haben  Freude  an  deiner Verehrung,  o  AAM.,  wir  wünschen  (dich) zu  verehren,  wir  sind  bereit  (dich)  zu  ver- ehren" ^.58.  3JI;  —  mit  Dat  des  Gottes, dem  die  Huldigung  gilt:  'matgkä  a/ni  . . avat  ituyl'^.  12.  3;  —  a/  3  %waAmai  äkre rtltqm  (sd.)  'manAS  .  .  Y.  4j.  9.  a)  bes. NS.  in  elliptischen  Sätzen«;  der  Name  der Gottheit  folgt  im  a)  Vok,:  °m^  urvaireV. ig.  18;  YLi.  21;  —  'num^l  kttvatm  y^arms Yt  /.  2 1 ;  18.  7.  b)  Dat  oder  Gen. :  'mB ahuräi  mazdai  °mS  anDsaHbyH  sp^ntaeibyS *mS^  .  .  'ms  gsul  'mS  gayehe  'mS  lara- "kusirahe ..frava^e  'mstn^'^  vJspayh  afaonS stBis  Y.  68.  22;  g.3,  16,  JO.  13, 17',  2o',Yt /.2iJ,7.iS,  JO.91, V./5.25';  — gave  am^m gave  'm?mi*  Vt/i^.  61,  c)  Vok.  hinter dem  enkl.  Dat-Gen.  des  Fron.  2.  Person: n;mas>  ti  aAura  mazda  .  .  'mB  vS  amf^ä spinta  Ny.  /.  1 ;  j.  4,  Y.58. 7,  V.  21. 1*;  — •mS  vS  gaha  alaonilY.  28.0,  43.  o,  47.0, ^i.o,  SS-o-  d)  Lok.:  'mir  airyene  vai- JaAi  Ytl.21.  OhneWert:  'ttU!  tistrim
18978:•  j.  namahi  In£  'zu  verehren':  s.  unter 'mmaA-  mit  No.  3.
18985:•  g.,j.n»niafiya-deD.Praes.3i  i)'Cemer Gottheit,  Akk.)  Ehrfurcht  bezeugen,  hul- (Ügen':  tamakySmahl  isäidyämahj  (sd.) 5a»a  mazda  ahurä  Y.jö^.5;  —  yä  vS (nämL  afB)  . .  ahträ  . .  *namam  dadat lait  vä  yatamaid!  .  .  *fryqnmahl  .  ,  nt- mahyämahf  ,  .  UBidyamaAi  Y.JÄ4;  3g. 4.  2)  'etwas  (Akk.)  durch  Gebet  er- streben, erflehen  fiir  -'  {avi  mit  Akk.): tat  vJsp?m  frfnamahi  . .  mmahyamahi  avi imqm  tanüm  V.  20. 5.
23827:•  j.  vouru.namah-  m.  £N.  eines  der  <  "ein  weisses  oder  schwarzes  Schaf"  Yt  S. sechs  Genossen  Aes  Saosyarrt  bei  der  58;F.^b.  2)  m.  Name  einer  Pflanze*), Auferstehung,  Ratav  des  KarhmrVtmru.-  6stKa  (weiches)  Holz  zum  Räuchern  und banhV^:  °manhS  asaonö  Yt.r_j.ia8.  zum  Unterhalten  des  heiligen  Feuers  diente :
```


## [2026-09-07T17:38:17.636Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT vaxs ===\"; grep -n \"va%s\\|vaxs\\|växs\\|vaLs\\|\\.vä\" BRT.txt | grep -i \"namr\\|nam\" | head -10\necho \"=== BRT nam- verb ===\"; grep -n \"•  j\\.\\|•  g\\.\" BRT.txt | sed -n '1,1p'\necho \"=== search nam1 ===\"; grep -n \"'nam-\\|\\bnam-\\b\" BRT.txt | head -20\n"
}
```


## [2026-09-07T17:38:17.668Z] TOOL CALL #20: WebSearch

```json
{
 "query": "Persian نخ nax \"thread\" etymology Middle Persian"
}
```


### [2026-09-07T17:38:17.742Z] TOOL RESULT

```
=== BRT vaxs ===
2780:mit  para  Kaus.  '(Wasser  od.  dgl.)  weg- ' yaia  °iS  amavü  %rqfiuö  fraxstüne  s^mil laufen  lassen,  verschütten';  vTspanqm  zt  paiti  Y.  ff. 20;  —  'silät  ^wa  imavantasiä *avajrasn-ntqmparaca  aisayamananam  ^(yarnJ  (sd.)  Y.4'-4;  —  hyatcä  tnöi  hy^i dasva  *raizaiie  (sd.)  N.  ÖÄ  \växs  'iö  "und  dass  meine  Rede  wirksam
2802:folgendem  Fall  brauchen  wir  den  unbe- stimmten Artikel  'ein':  yavat  °sa  carsitika *avi.mqm  har>k>  (sd.)  hancayät  V.5.60. Undeutlich:  °sS  gaeHanam  . .  rass?  (sd.) N.  2;  —  ainitis  -iÖ  *växs  P.  26.  Vgl.
4958:•  j-i  g-i  P-  'ava-  Pron.  dem.  (fem.  'rJ-)";  einem  erläuternden  oder  ergänzenden  Re- 'jener';  I)  in  starkdeiktischer  Verwendung :  lativ,  i)  adjektivisch:  aom  stänm  yiiii 'jener,  der  dort,  dann',  von  dem  gebraucht, ! //ÄrJ»»  YLÄ50;  —  -ve  sfärö  y5i  Aaptö.- was  dem  Sprecher  entfernter  liegt;  1)  im  iringa  Yt  J2,  28;  29—32,  S.  2.  13  (wo ausgesprochenen  Gegensatz  zu  'a-,  ima-'  aoe)^'*;  —  "ve  strsul  yq  Aaptöiringa  Yt, (usw.),  adjektivisch:  äfl:*Kra*mff2(/J  Ay^  .S.ix;  13.60,  S.  2.  13  (wo  aoe)i^;  — imflm  bümlm  adct''  AyJ'  'vam  asmänam  -vai  karsvan  yal  fradariaßu  vTdmafsu ad^  D.  6.  I,  X.  /.  I,  6.  I,  Ao.  /.  1 ;  —  V.  ig.  39;  39';  —  'i-at  zrayS  yat  vouru- imqmca  zqm  ..  aomca  asmänsm  Yt  y.  kahm  Yti^j.  59;  ^-  aom  gairjm  .  .  yim 'S3>  2; —  aif'fAasca  ztmS 'vaiAhda  ahtS  usLdqm  Yt. /.  28;  —  avqm  vanqm  yqm Y./.16;  —  imqmca  zqm  'vaca  raocä  H. ' saiftaAt  yt/2.27;  —  mazdäi  'rat*'*  xsa- J.16;  yt70.85,89;  —  upa  AvaHj aiMa  "^nm  hyat . .  vaxsat  (sd.)  .  .  Y.^j/.ö;  — wmö  .  .  upa  °V€  stSrS  .  .  upa  aom  man- 1  aoin^  spä<am^  .  .  yä  ml  pasküt  vasaiie lum  Yt  72,22— 28— 33;  —  imat  ««««jm   Yt/4-S8.  2)  substantivisch:  kä  tSm..
6598:yä  oder_>'J(?)  vll.  sva.  'es  geschieht,  kommt vor,  dass  ..':  asit'i^  yä  *ayar3Aa^a  sparr/a (sd.)  YL/0.  laöGl.;  —  asti'*''  yS gavasnaAe (sd.)  snäuya  jya  Yt  10. 1 28  Gl.  III)  als j  Praedilcatsverbnm  (Kopula).  Das  Praedikat ist  I)  ein  Substantiv,  das  mit  dem  Subjekt im  Numerus  und  Kasus,  oder  ein  Adjektiv, das  auch  im  Genus  kongruirt.  A)  I  im Ap.  (die  Kopula  folgt  dem  Praedikat): adam  bardiyä'  amiy  .  .  adam  xsäya'iiya* amiy  Bh.  b,  h;c-f*,  h-j^,  Bh.  7.5,  11,  16', -■3>  S'  55.  13-  4.2*,  D.(t.4;  —  adam xsaya%iy£^  amiy  asagartaiy  ""uvaxstraAyä laumäyä  Bh.2.  i4,4.2,Bh.g,;  —  adamsäm xsäya^iyt^  äham  Bh. /.  6;  —  ka"bujiy<^ ,  .paruvam  idä  xsäya'^iya"  ähJ^  Bh. /.  10; —  g  *duvitäiaranam  (sd.)  vayam  xsäya- üyä  amahy  Bh.  j.  4;  —  tyaiy  paruvam xsäya'iiyä  aha"  Bh.  7.  4;  —  kalä  pa- ruviyata'  hyä  amäxam  taumä  xsäya'iiyä (sd.)  äh(^  Bh.  j.  3 ;  —  adam  pärta''  amiy D.  77. 3 ;  —  martiyJ^  Ayo*  draujana'' ahatiy  Bh.^.5,  14;  14,  5;  —  Äj'u*  daustä <Ua*.  .  hyi^  arika''  äha*  Bh. /.  8;  2.4,  6, 3-  II,  5.4;  —  tyaisaiy  fratamä  martiyä anusiyä  äha"täi'>  Bh.  ;.  13;  J.  7,  8,  11,  13, /.  7;  —  negirt:  ya^ä  naiy  arika"  äham Bh..:^.  13;  13  ^  —  ty^  adam  naiy  bardiya'' amiy    Bh.  7.  13.  B  [)    im   jAwr.    (Die
8470:-*  'ranam  sBra  vaxfyente  (sd.)  vaxsa Yt.A4a;  —  'ranqm  (statt  Akk.  des  Ziels) urukmyanqm  ava.jasä/ii  V .  /q,  18;  Vyt.22; kö  p»rfi^we  (sd.)  aitihh  sjmS  *upa.- 'i:war>5li    'ranqm    (als   Obj.)    V.  p.  z;    —
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
8492:•  j.  urvä-"  f.  Name  eines  Lands,  (nach Pü.)  Muene  (Misän)  im  Euphratdelta'*: astJm^m  asaahqmca  .  .  /ra>w?r?i?m  .  . 'vqm  pourv.västrqm  V. /.  10.
8705:—  'saiihqm  para  frSritSii  FrW.  /0,4i ;  — ytzi  xsapsAva  mpr^ncaiie  (sd.)  'lakva bisazyat  V.  l'7.3J  —  uü'  (LS.).  A)  als weibliche  Gottheit  gedacht:  'sqm  (AS.) sriram  yazamaide  'säuAfm  . .  xsSi'inJm ravaLaspqm  .  ,  "säPikem  .  .  nvim  ranjat.- aspqm . .  avqm  'sqm . .  G.  5. 5.  a)  Name der  fünften  und  letzten  der  (priester- lichen) Tages  abteilungen*';  vupim  paiti "sauham  ä  kB  vaxsat  "immer  in  der Morgenfrühe  bis  Sonnenaufgang"  V.  /y. I.  3)  mit  süra-  Adj.  Name  des dritten  Abschnitts  der  Nacht**':  hö tiurr/ö  (j'S  parö.dars)  väHm  baraili  upa 'iaukim  yqm  särqm  V,  iS.  15;  —  'sqm särqm  V.2j\}.
10321:I  s; —  ime  vaca  framrva  ysi  kifiti  °ltahva bisämrüla  (sd,)  %risämrBla  (sd.)  cahrusä- \tnrata  (sd.)  V.  jo.  a;  2^,  3",  7',  11',  15, N.J,?;  —  cii  sflc/ar/ (sd.)  kairim  ,,? \{yai)  **äJjÄ)"  frasravayaiti  ,  .  jV.  72; I —  kaka  zaota  (sd.)  "^i  frasravayaiti? *naimS.va^astaita*mat»mya  vaca.-iJ.J^; — \yä  "äi  *aßmainivqrt  *srävayats  uva  '^ratu- \fris  valastaMvat  *srSvayat5  aUavat3 . . 1 N.  25;  — y^  '"^anam  Hy^m  väci/n  apayätti I  aSvqiH  va  vacastasUm  "wer  von  den  G. I  ein  Wort  ausVässt  oder  eine  Strophe" |N.^;  —  *öy?mäi..väiim  '^anqm  <umt?m \  (sd.)  . .  N.  103;  — yS  'ianqm  alvqm  ratu- \pritTm  (sd.)  ava.raotayeiti  N.  43',  —  vä^a hankiriia  .  .  "kanam  avaurusta  (sd.)  Y. 7/.  18;  —  ''ianqm  anapyBxitanqm  (sd.) anapisBtanqm  sravayamnartqm  W.ip.5;  — Ä'aj  (sd.)  «3  *nii3ma  vaca  "ha  sravayd ralufrisi  N,  37;  —  ^srao'ira  na  '^anqtu ratufris  paiiiMstila  (sd.)  yasnahe  .  .  N.22;
12424:oAurischta  Religion :  kahmät  paoiryS  mal-  \ yänqm  , ,  frada^ayS  'nqm  ,  .1  . .  yimäi .  .  fradaisalm  °nqm  .  .  äai  hi  mraom  . . vUanha  ml  minlff  b^ntala  (sd)  "nayäi (als  Gen.)  äat  . .  pailyaoxta  yimS  .  .  nSit dato  ahmt  . ,  tnirstl!  b3r?tala  'nayäi  V. 2.1  ff.;  Ytn.  14;  —  vXltäspaht.  .yS  batuUa upastaca  vTsata  .  .  •nayä  Yt  13.  99;  — ya%a  axsm  Asüyene .  .  zara%uänm  anu- matSe  'nayäi  anuxtie  'nay3i  anu.värltSe •nayäi  Yt.  j,  18;  Y.t?.  7;  —  hutaosqm  .  . yä  rrn  °nam . .  zraiia  (sd.)  dät  apica  aotaf Yt  ().26;'Vyt.  Jo(?);  —  ks  .  .  'nam  .  . vJbarat  aitaisva  vanfsva  ySyimö  ktnrtaoi^ .  .  vTs  iarsipia  V.  2. 42 ;  —  satö  .  .  zara- huiirS  .  .  ita  apam  vTjasaiH  .  .  °na  .  . vlspais  avi  karsvqn  Yt  jj.  94; —  mi^nm . .  yahmi  vyane  (sd.)  °nayäi  (als  Gen.) srirayai  p}r>^u.fräkaysi  . .  Yt  10.  64;  — sraoi^m  .  .  yB  damsJisS  *°nayä  Y. 57.23;
=== BRT nam- verb ===
2437:•  j.,  g.,  p.  'a%  °ä,  nur  KompA.  und  post- fifirt  an  Kasusfonnen:    'hia  zu  — ;   ' I)  Praen.;  —  3)  Praev.
=== search nam1 ===
```


### [2026-09-07T17:38:23.260Z] TOOL RESULT

```
Web search results for query: "Persian نخ nax "thread" etymology Middle Persian"

Links: [{"title":"نخ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%86%D8%AE"},{"title":"نخچیر - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%86%D8%AE%DA%86%DB%8C%D8%B1"},{"title":"Nāz. : languagehat.com","url":"https://languagehat.com/naz/"},{"title":"نخود - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%86%D8%AE%D9%88%D8%AF"},{"title":"Persian: سر نخ | WordReference Forums","url":"https://forum.wordreference.com/threads/persian-%D8%B3%D8%B1-%D9%86%D8%AE.2619183/"},{"title":"\"نخوت\" meaning in Persian","url":"https://kaikki.org/dictionary/Persian/meaning/%D9%86/%D9%86%D8%AE/%D9%86%D8%AE%D9%88%D8%AA.html"},{"title":"A concise review of the Iranian calendar","url":"https://arxiv.org/pdf/astro-ph/0409620"},{"title":"نخ (nax) | Meaning, Pronunciation, Grammar, Examples","url":"https://dictionary.farsi.school/definition/%D9%86%D8%AE"}]

Based on the search results, here's what I found regarding the etymology of Persian نخ (nax) meaning "thread":

The word is borrowed from Classical Persian نَخ (nax). However, the Wiktionary entry notes that the etymology is missing or incomplete, meaning that the ultimate origin of the word—including its Middle Persian ancestry—has not been documented in readily available etymological sources.

The search results confirm the word's use in Classical Persian, as evidenced by a poetic citation from around 1520, but they do not provide specific information about the Middle Persian form or the word's deeper etymological roots before Classical Persian.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T17:38:26.297Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%AE",
 "prompt": "What does the Persian entry نخ say — meaning, etymology, any Middle Persian or Proto-Iranian ancestor? Also list other language sections (Arabic etc.)."
}
```


## [2026-09-07T17:38:28.357Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%86",
 "prompt": "Persian نان: etymology in full — Middle Persian form, Proto-Iranian reconstruction, cognates (Parthian, Sogdian, Balochi), and any cited authors (Hasandust, MacKenzie). Quote the etymology text."
}
```


### [2026-09-07T17:38:32.560Z] TOOL RESULT

```
# Persian Entry for نخ

## Meaning
The Persian noun **نخ** (nax) has two primary definitions:
1. "Thread" or "string" — with examples like "colored thread" and "silk thread"
2. "A rug elegantly threaded"

## Etymology
The entry notes that the etymology is incomplete, stating: "This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium." No Middle Persian or Proto-Iranian ancestors are documented.

## Other Language Sections
The page contains entries for three languages:
- **Arabic**: Borrowed from Classical Persian; means a rough rug/mat or a silk garment with gold threading
- **Persian**: The main entry with thread/string meanings
- **Ushojo**: Borrowed from Classical Persian; means "mark/signal" or "target/goal"

The page also notes descendants in Arabic, Medieval Latin, Old French, Old Italian, Uyghur, and Turkmen.
```


### [2026-09-07T17:38:36.440Z] TOOL RESULT

```
# Persian نان Etymology

According to Wiktionary, the Persian word نان (nān) derives from **Middle Persian** (nān, "bread, food"), which came from **Old Persian**, ultimately tracing to **Proto-Iranian** *nagna- ("naked bread").

The entry explains: "naked bread (bread that was baked without ash)" contrasts with *nikāna- "buried bread (bread that was baked in ash)."

**Key cognates include:**
- Sogdian: nγn- /naγn/ ("bread")
- Manichaean Parthian: ngn (naγn)
- Khotanese: nāṃji
- Northern Kurdish: nan
- Baluchi: نگن (nagan)
- Sanskrit: नग्नहु (nagnahu)

The historical linguistic trail demonstrates how this word spread across Indo-Iranian languages, maintaining its core meaning of bread while undergoing predictable phonetic transformations across different language families over millennia.
```


## [2026-09-07T17:38:45.582Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%B2%D9%87",
 "prompt": "Persian نیزه: full etymology — Middle Persian nēzag, Avestan naēza-, Proto-Iranian; descendants including Arabic نيزك. Quote the etymology."
}
```


## [2026-09-07T17:38:46.480Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%82",
 "prompt": "Arabic نمرق / نمرقة: meaning, etymology (Persian loan?), plural نمارق, Quranic attestation. Quote the etymology text."
}
```


### [2026-09-07T17:38:50.992Z] TOOL RESULT

```
# Persian Word: نیزه (Neyze)

**Definition:** This Persian noun means "spear, lance, or javelin."

**Etymology Summary:**

The word traces back through several ancient language layers. It derives from Middle Persian *nēzag*, which came from Old Persian *naizakam*. The ultimate root lies in Proto-Iranian *náyjakam*, connected to Proto-Indo-Iranian *náyȷ́žʰam*.

**Key Quote:**
"From Middle Persian... from Old Persian... from Proto-Iranian..., derived from Proto-Iranian..., from Proto-Indo-Iranian" — this demonstrates the word's deep Indo-European heritage.

**Cognates:** The term appears in related languages including Avestan *naēza* ("tip, especially of a needle"), Classical Syriac, Old Armenian *nizak*, and Arabic *nayzak*. Modern descendants include Azerbaijani *nizə* and Kazakh *nayza*.
```


### [2026-09-07T17:38:52.650Z] TOOL RESULT

```
# نمرق (numruq)

Based on the Wiktionary entry provided, here's what I can tell you:

## Meaning
The word نمرق refers to "a cushion or bolster for sitting," functioning as an alternative form of نمرقة (numruqah).

## Grammatical Information
- **Part of speech:** Masculine noun
- **Plural:** نمارق (namāriq) - a broken plural form
- **Pronunciation variants:** numruq, nimriq, or namraq depending on vowel patterns

## Etymology & Language Status
The entry notes this is "an alternative form," but unfortunately, the Wiktionary page provided contains **no explicit etymology section** discussing Persian origins or other etymological details. The page lists the word across three language versions (Arabic, Persian, and Hungarian), suggesting its use across these languages, but specific etymological commentary is not included in this excerpt.

## Quranic Attestation
The provided content does not include information about Quranic usage or attestation.

To find etymological details and Quranic references, you would need to consult the full article or check specialized Arabic dictionaries like Lane's Lexicon or modern etymological resources.
```


## [2026-09-07T17:39:03.187Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ namariq ===\"; grep -n -i \"namariq\\|namāriq\\|namruq\\|numruq\\|nimriq\" FVQ_pages.txt FVQ.txt | head -20\necho \"=== AFM نمرق ===\"; grep -n \"نمرق\\|النمرق\\|نمارق\" AFM_pages.txt | head -20\necho \"=== KLN namariq ===\"; grep -n -i \"namariq\\|numruq\" KLN_1966.txt KLN_1971.txt | head\necho \"=== PLA files ===\"; ls incoming/PLA/ 2>/dev/null"
}
```


### [2026-09-07T17:39:03.272Z] TOOL RESULT

```
=== FVQ namariq ===
=== AFM نمرق ===
=== KLN namariq ===
=== PLA files ===
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-07T17:39:04.452Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%82%D8%A9",
 "prompt": "Arabic نمرقة numruqa: etymology — is it a borrowing from Middle Persian / Persian narm? Quote the etymology section and any mention of Quran 88:15 نمارق."
}
```


### [2026-09-07T17:39:09.938Z] TOOL RESULT

```
# Etymology of نمرقة (numruqa)

## Borrowing Origin

The word is borrowed from **Parthian**, not directly from Middle Persian or Persian, though related languages share the same root. According to the etymology section:

"From Parthian _nmr_ (namr, 'soft') + _-k_ (-ak, 'adjectival suffix'), 'thing having softness'; compare Zazaki _nemr_ ('soft'), Northern Kurdish _nerm_ ('soft') and Persian _نرم_ (narm, 'soft, gentle')."

The term refers to a cushion or bolster, with the semantic logic deriving from the softness quality.

## Quranic Citation

The word appears in **Quran 88:15** within a description of Paradise. The verse mentions **نمارق** (namāriq—the plural form), appearing in a list of furnishings: "cushions arranged in rows" alongside carpets and flowing springs, depicting the comforts of the afterlife.
```


## [2026-09-07T17:39:15.849Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA nayzak ===\"; grep -n -i \"nayzak\\|naizak\\|نيزك\\|nēzag\\|nezag\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== PLA namraq ===\"; grep -n -i \"namraq\\|numruq\\|نمرق\\|narm\" incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-07T17:39:15.903Z] TOOL RESULT

```
=== PLA nayzak ===
14833:u          - niyäzak:             Pl.       v. Ss           naizak           q.    v.
14849:Is     - naizag          = naizak                q.    v.
14851:Ds.: - naizak:               "kurze          Lanze" S_pers.                         , naize
14855:       naöza> ar.                  Lw.       naizak            , aram.                 or   (pers.       om).
=== PLA namraq ===
1026:              scheinlich                          aus           pers.           ar               narm        +   ähan       "weich        +     Eisen"           —m.Y2!
1027:              +       p-           narm           +    Asıen..
14465:Dot         - naäy narm:                 aus       pers.          st          nay-narm           10        ,,
14563:u          _    narmask:             "Duft,           Moschus         aus       Granatapfel"                =    narmask      q.    v.   a,
14566:nr     - narmaq:                "weich"              aus    pers.         uc narmak              5 m.                  narm    6,
14744:                 namra           9 >>mp.                I:    narm           10,         suff.            g /ak      11,
```


## [2026-09-07T17:39:18.013Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ contents grep n ===\"; grep -n -i \"narm\\|namrak\" FVQ_pages.txt | head -10\necho \"=== AFM narm/nayzak ===\"; grep -n \"نيزك\\|نيزه\" AFM_pages.txt AFM.txt | head -10\necho \"=== LKT ===\"; grep -n -i \"naizak\\|nayzak\\|namraq\" LKT.txt | head -10\necho \"=== AFA fraenkel ===\"; grep -n -i \"namraq\\|numruq\\|naizak\" AFA.txt | head -10"
}
```


### [2026-09-07T17:39:18.093Z] TOOL RESULT

```
=== FVQ contents grep n ===
12146:narm 281
=== AFM narm/nayzak ===
=== LKT ===
=== AFA fraenkel ===
```


## [2026-09-07T17:39:25.692Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA 14820-14860 ===\"; sed -n '14820,14860p' incoming/PLA/PLA_pages.txt\necho \"=== page tag before 14833 ===\"; awk 'NR<=14833 && /\\[pdf page/ {p=$0; n=NR} END{}' incoming/PLA/PLA_pages.txt; grep -n \"\\[pdf page\" incoming/PLA/PLA_pages.txt | awk -F: '$1<14860 && $1>14700' | tail -5\necho \"=== PLA 14730-14760 ===\"; sed -n '14730,14760p' incoming/PLA/PLA_pages.txt\necho \"=== PLA 14555-14575 ===\"; sed -n '14555,14575p' incoming/PLA/PLA_pages.txt"
}
```


### [2026-09-07T17:39:26.912Z] TOOL RESULT

```
=== PLA 14820-14860 ===
5.    al-MuCarrab                 s.       v.
6.    Yäqüt          n.     Nyberg          Bd.       II       s.    v.
7.    Wahrmund              s.    v.
8.    ebda.,          Addai           Scher          s.    v.
9.    Macuch          Ss.    V.
10.    Muhlt          s.     v.,       Addai          Scher          s.       v.
11.    Brockelmann                    s.    v.,       Macuch             s,       v.,     Lokotsch        s,    v.
nüfar                                                                        265                                             niı
Br - nüfar:=                 nilufar             q.    v.      .


J’%»- nu’l:          ägypt.            Ar.        "getrocknete                   Früchte" << pers. )» noql e,

u          - niyäzak:             Pl.       v. Ss           naizak           q.    v.


aneb - niyä$in:                    Pl. v.oWwnißän                           q. v.

DB - nairaz              - naurüz                q.    v.    3,


or      - niranf:             "Beschwörung"                   pers.              * mp.         >>ı nörang °, hebr.      [>
              9.
       aram. Ar

                                                              6
28         - nairüz          = naurüz              q. v.           .


Is     - naizag          = naizak                q.    v.

Ds.: - naizak:               "kurze          Lanze" S_pers.                         , naize
                                                                                   ie                7
                                                                                                     °Tmp.xc,    2
                                                                                                                n&zak   T aw.
       naöza> ar.                  Lw.       naizak            , aram.                 or   (pers.       om).

>21» - nisäbür                     = ni$äbür q. v. °.

u      -    nisab:       "gerader                Weg!"      pers.           10    ?.

=== page tag before 14833 ===
=== PLA 14730-14760 ===
       [73

 plo -                   nammäm:           '"Menthabathurm"                            6 2


a»l,» -                   nammäma           = nammäm                   q.    Vv.


 >           -       namad:           "Pferdedecke"                         aus        pers.        „     namad   I            Mp«      namadgs namat           am.
                                 7                  N         8
                 namta               ’, syr.        Ne            °.


 Se              -        amrag:           "Sattelkissen"                          ir.              nanr      "weich"                  air     *namra,    aw.
                 namra           9 >>mp.                I:    narm           10,         suff.            g /ak      11,

 v-
 —e          -       namat:           "Decke"            =    namad              q.     v.


Ge -                     amag:        "Buch,            Brief"              aus        pers.        «-L näme         s.        barnäma,        12,    aram.     Ads



 1.          Mackenzie                 s.    v.
 2.          Addai             Scher        s.      v.
 3.          ebda.
 4.          ebda,             Nyberg        Bd.         II       s.        v.
 5.          ebda.
 6.          Löw          s.    v.
 7.          Mackenzie                 s.    v.,         Nyberg              Bd.        II     s.       v.
=== PLA 14555-14575 ===


vb     ok;            - narsiyändärü                       = barsiyändäru                  q.    v.    2,


a-         narq:          "schön"           aus       pers.         7 narh, "glücklich"                     3,


u          _    narmask:             "Duft,           Moschus         aus       Granatapfel"                =    narmask      q.    v.   a,


nr     - narmaq:                "weich"              aus    pers.         uc narmak              5 m.                  narm    6,


Hp - nazaka:                     "Zartheit,                 Feinheit,            Eleganz"             v.    pers. .J;L näzuk             "m.
       oyı nAZ "Liebling" ®.

us     =       nastar       =    nastaran              q.     Vv.    9,


as         -    nastaran:             ''Heckenrose,                  wilde       Rose,          weiße       Rose!"     aus    pers.      ya
```


## [2026-09-07T17:39:35.883Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== running heads near 14735 ===\"; awk 'NR>=14680 && NR<=14760 {print NR\": \"$0}' incoming/PLA/PLA_pages.txt | grep -E \"26[0-9]|25[0-9]|pdf page\" | head\necho \"=== raw 14690-14735 ===\"; sed -n '14690,14735p' incoming/PLA/PLA_pages.txt"
}
```


## [2026-09-07T17:39:37.058Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ page 281 ===\"; grep -n \"namariq\\|Namariq\\|NAMARIQ\\|نمارق\\|narm\" FVQ.txt | head -20\necho \"=== FVQ_pages search ===\"; grep -n \"amariq\" FVQ_pages.txt | head"
}
```


### [2026-09-07T17:39:37.147Z] TOOL RESULT

```
=== running heads near 14735 ===
14711:  naqgs                                                                                       263                                                              nama
=== raw 14690-14735 ===


ee - nafif                 = nufga          a.    v.

      u.                                                                         7
=           _ nafir:          "pers.        Pfeife,                  Flöte"           ?.


ori.             naggäf;        nom.       agent.          n.         naqgd a. v.


el           _ naggäfi:              "Malerei"             s. nagg.


 1.        Mackenzie          s.     v.
 2.        Henning,        A List          of    Middle               Persian         and    Parthian        Words,     BSOS     9,    S.     85.
 3.        Brockelmann             s.     v.,    Macuch               s.   v.
 4.        Loktsch       s.     v.
 5.        Fremdwörterbuch                 s.    v.
 6. TaCälibl figh al-luga s. v.
 7. Wahrmund               s.      v.,     Muhit       s.            v.,   Addai       Scher       s.   v.
 naqgs                                                                                       263                                                              nama

 um!                                                                                                                      >,    £       “xy
o=# - nags:                          "Bild",            möglicherweise                        aus         pers.   cr                 negäätan        "zeichnen"
                 mp.                 Isı nigär "Bild"                              ı
  4
_t-                  nakir:           "klug,            schlau"              pers.           2, aus          pers,        ©,.& negärdan               nach -
                 denklich" ®
  /
ob - nakas:                           "umwenden"                            pers.        „LU, negünsar                          — MP.         n»pi nign&-sar
                                             4
                 << aw.               ni/ne    ".


CA                   nulk: "Mistelbaum" pers. ° ?.

U            - nilk = nulk q. v.

a                    -     namäriq:          Pl.         v.o                namrag           q.     Vv.
       [73

 plo -                   nammäm:           '"Menthabathurm"                            6 2


a»l,» -                   nammäma           = nammäm                   q.    Vv.
```


### [2026-09-07T17:39:37.196Z] TOOL RESULT

```
=== FVQ page 281 ===
21104:narm 281 
=== FVQ_pages search ===
```


## [2026-09-07T17:39:45.644Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" FVQ_pages.txt | head -3\necho \"---- find printed 281 ----\"\nawk '/\\[pdf page/{p=$0} /^ *281 *$|^281$/{print NR\": \"p\" || \"$0}' FVQ_pages.txt | head"
}
```


### [2026-09-07T17:39:46.865Z] TOOL RESULT

```
---- find printed 281 ----
11220:  || 281
11459:  || 281
12005:  || 281
```


## [2026-09-07T17:39:49.049Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11440,11530p' FVQ_pages.txt"
}
```


### [2026-09-07T17:39:49.095Z] TOOL RESULT

```
257
256 (loALO 258
) 61 U^U 276
289 )2oUbOJ 277
259.260 )i,J 278
179 ]iOIQJ 40
200 -MOJ 282
132.261 \*<U 282
273 teflOQJ 279
275
i 264
70, 263
149
149
278
279
22
oofiQJ 279
40
281
275
293
293
268
269
271
40, 268
]iiO 271
263
179
258
30
71, 182
[63
163
163
163
187
]T nrn^n 264,265 liouo is?
267 U' 000 182
D^lD 192 12lMlfi 159
190
O 261
283
262
265
258
V Q-^s
163
184
185
185
191304
INDICES
k S
^
i
192
192
192
194
202
50. 201
UiOr 201
198
197
i
199
246
97
)}QO 232
268
ID 243
242
179
246
234
1A00 238
244
244* 245
243
244
244
239
240
lioaO 246
O>;O 106, 107
236
234
236
240
```


## [2026-09-07T17:39:53.921Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"cushion\" FVQ_pages.txt | head -10\necho \"---\"\ngrep -n -i \"namruq\\|namäriq\\|namariq\\|namarik\\|nimriq\" FVQ_pages.txt | head"
}
```


### [2026-09-07T17:39:53.987Z] TOOL RESULT

```
10097:Cushions.
10101:frequently in the early poetry for the cushion on a camel's back, and
---
```


## [2026-09-07T17:39:56.779Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10085,10135p' FVQ_pages.txt"
}
```


### [2026-09-07T17:39:56.823Z] TOOL RESULT

```
also represents the Natra/ocucn of Epiphanius and Jerome, 1 who were
a Judseo-Christian sect related to the Elkesites, and the name may have
come to the Arabs from this source. 2
The most probable origin, however, is the Syr. U'V* which
represents the Nafopdtot of Acts xxiv, 5, and was a commonly
used designation of Christians who lived under Persian suzerainty. 3
As it was .from this area that the old Arm. Yiu/ui was borrowed, 4
the case is very strong for the Ar. (^jUx? having come from the
same source.
' 4
*j (Namdriq).
Ixxxviii, 15.
Cushions.
Only in an early Sura in a description of the delights of Paradise.
al-Kindl, Risala, 85, noted it as a loan-word from Persian, 5 though
it is not given as such by al-Jawallqi or as-Suyutl. It occurs not in-
frequently in the early poetry for the cushion on a camel's back, and
must have been an early borrowing.
Lagarde, Sytnmicta, i, CO, 6 pointed out that it is from the Iranian
namr meaning soft. In the old Iranian we find namrd, 7 which gives
Av. -u3g.u> natnra (Bartholomae, AI W, 1042, cf. Skt. WU),
and Phlv. v> varm (West, Glossary, 240 ; Salemann, Mamchaeiscke
Studien, i, 101), and from some Middle Persian form namr + the
suffix ) ak, it passed both into Aram. ^p"1133 and Ar.
for which a plu. 3jL was then formed.
1 Epiphanius, Panarion, xxix, and Jerome, Comment, on Matt. xii.
Bell, Origin. 149 ; Margoliouth, ERE, x, 540, thinks it was Heb.
Horovitz, KU, 145, 146. See also Mingana, Syriac Influence, 96; Fischer,
Glossar, 135.
Hiibschmann, ZDMG, xlvi, 245 ; Arm. Gramm., i, 312.
See also Sprenger, Leben, ii, 504, n.
Followed by Fraenkel, Vocab, 8.
This form occurs in nemr in the Zaza dialect to-day (Horn, Qrundriss, No. 1028).282 FOREIGN VOCABULARY OF THE
jT > (Nuh).
Occurs some fifty-three times, e.g. iii, 30 ; iv, 161 ; xi, 34.
Noah.
Some of the Muslim authorities would derive the name from
s>
r\J to wail, 1 though as al-Jawaliqi, Mu'arrab, 144, shows, it was com-
monly recognized as of non-Arabic origin. 2
The story of Noah was well known in pre-Islamic days, and was
often referred to by the poets, though as a personal name it apparently
was not used among the Arabs before Islam. 3
The form of the Ar. r~ y is in favour of its having come from the
Syr. *j*OJ rather than directly from the Heb. 113. 4 '
V >
jy (Nun).
xxi, 87.
Fish.
Only in the title J^lM }> given to Jonah, so that it is the equivalent
of d>>*i < *s>-U? in Ixviii, 48, whence came the theory
```


## [2026-09-07T17:40:08.572Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nn=$(grep -n \"^1042$\" BRT.txt | head -1 | cut -d: -f1); echo \"line $n\"; sed -n \"$((n-30)),$((n+40))p\" BRT.txt"
}
```


### [2026-09-07T17:40:09.775Z] TOOL RESULT

```
Exit code 1
line 
sed: invalid option -- '3'
Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]...

  -n, --quiet, --silent
                 suppress automatic printing of pattern space
      --debug
                 annotate program execution
  -e script, --expression=script
                 add the script to the commands to be executed
  -f script-file, --file=script-file
                 add the contents of script-file to the commands to be executed
  --follow-symlinks
                 follow symlinks when processing in place
  -i[SUFFIX], --in-place[=SUFFIX]
                 edit files in place (makes backup if SUFFIX supplied)
  -l N, --line-length=N
                 specify the desired line-wrap length for the `l' command
  --posix
                 disable all GNU extensions.
  -E, -r, --regexp-extended
                 use extended regular expressions in the script
                 (for portability use POSIX -E).
  -s, --separate
                 consider files as separate rather than as a single,
                 continuous long stream.
      --sandbox
                 operate in sandbox mode (disable e/r/w commands).
  -u, --unbuffered
                 load minimal amounts of data from the input files and flush
                 the output buffers more often
  -z, --null-data
                 separate lines by NUL characters
      --help     display this help and exit
      --version  output version information and exit

If no -e, --expression, -f, or --file option is given, then the first
non-option argument is taken as the sed script to interpret.  All
remaining arguments are names of input files; if no input files are
specified, then the standard input is read.

GNU sed home page: <https://www.gnu.org/software/sed/>.
General help using GNU software: <https://www.gnu.org/gethelp/>.
```


## [2026-09-07T17:40:12.296Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^1041$\\|^1042$\\|^1043$\\|^1044$\" BRT.txt | head"
}
```


### [2026-09-07T17:40:13.516Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T17:40:15.716Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1041\\|1042\\|1043\" BRT.txt | sed -n '1,20p'"
}
```


### [2026-09-07T17:40:15.775Z] TOOL RESULT

```
18591:nay-  1043
27362:1043  srava-  —
```


## [2026-09-07T17:40:18.481Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18520,18600p' BRT.txt"
}
```


### [2026-09-07T17:40:18.547Z] TOOL RESULT

```
yat,.aftra  kaAvart (sd.)  Jyä  navi^yan'> tifranhs  aüays  "wenn  .  .  die  Sehnen schwirren,  die  spitzen  Pfeile . ,"  Yt.  10. 1 1 3. Ganz  unsicher;  nur  die  Form  3FKA.  steht fest  —  ')  Oder  mit  (ausl.)  I.  —  >>  Ich  nehme nin/Ay'  {üx  mii^y'  und  verweise  auf  xlaviili
Jp  I    lU  V.   2.  32.
j.  naoma-  Adj.  (fem.  'mr-):   s.  unter aavama-.
•  j.  '^naomaya *>  Adv.  'neunmal':  tpätam
,  ^'yaüC'^  taha  asä  pa'^ä  vTi'^ayantu V.&18.
'naiianaia  (idg.  'netfn»'),  dafür  'na^ami^a mit  analogischem  m  (nach  dem  Zw.  für  7, 10} wie  im  Ordinale.  —  Pü.;  9  bar.  —  >)  So  Jp  1,
Mfa;  NA.  näumayäiU.
•  g.  nadant-  Adj.  'schmähend,  lästernd': ys  hwat  masäa  asrustlm  aktmiä  mans yasSi  (sd.)  apä  .  .  airyamanasSl  'dittis  .  .
'. .  und  von  dem  Sodalen  die  Lästerer  . ."
Y.^.4-
PP2A.  einer  ar.  Basis  *nW-;  Tgl.  ai.  ntndati, red,  Fraes.,  gr.  iMoff«/uvo( (?)  1),  —  Pü.:  nn aadnn  i/ii:&.f>i,  erl.;  ;^än  ndd  rjli  i/äri/n;  Sü.: nindäm  äätärak.  —  '>  VgL  iEL  BB.  1$.  354.
•  \.yai  hama  avi  nsit  aoiSTiaSö  saosuncayS V.7.72PiiZ.:-?-'
•  p.nadi^tabaira-m.EN.einesBabyloniers, der  ach  gegen  Darius  I.  empörte,  Nidin- tubel:   I  martiyt^  bäbiruviyt^  'r<^  näm^
irahya  pu^''a''  udapatatä  bäbirauv Bh./.i6;  19,  2.1,  42,  Bh.d;  —  'ram adam  bäbirauv  aväjanam  Bh.2.i;  i,  /.16, i;  —  käram  iyam  'rahyä'&\i.i.\^,  19;  18.
•  j.  nata-  m.  (Plur.)  Name  eines  Kleidungs- stücks: yS  vaaAaiti  °%ysca  sSoayanili'ca canmanca  *Aiiu  N.p5.
Pü. :  'k  n  da.
•  j,  naö-V.,  nur  mit  z/f 'schinden*.  Praes. 30  (Iter.)  nä'^aya'.
pqstS.fra'^arghm  (sd.)  kl  kapur^m  vi- nJk'ayfn  Y.^.io.p.^g. Et.  ?  —  Pü. :  iaiilan,  erl. ;  britan ;  vgL  Sp.  902  m.
ob,Google
I039
1040
•  ).,  g.,  p.  naplt-:ffa//-  m.,  j.  naptar-: nafsir-  m.",  j.  naptl-  f.  'Enkel;  Enkelin': '  adam  d3ray^v(^ui . .  vistäspahya  puh^e^ arSätnakyä  '/J(NS.)'*  Eh.  j.  i;  —  'pS (NS.)"  ..  ■■//("  (NSf.)  i/a  V./2.11;  10;  — nyaka  haca  'ptöisSs,  (^\%y^  nyske  haca  'pti (statt  AblSf.)  V.  J2. 1 1 ;  —  hyai  us  alä napiyaisii  na/i'uCLP.yVä ..uzp//  (Sp.4gSm.)  ' fryänakya  aojyaiiü  '^.46.12.  a)  mit GP.  apam''  'Enkel  derWasser',  Name  einer Gottheit**;  a  dim  (näml.  3^ar)nö)  Hahra kangturvayat  apum  'ph  (NS.)  aun'at.aspö Yt.  rp.  s  1 ;  5 '".  '.7-  95^';  —  «/>?'»  >'»  (NS.) t&  ups  ,  .  aiiuhe  .  .  vi.baxsaiti  Yt  8.  34; —  b^ntantfm  ahuntn  xsa^rlm  xSaltitn apqm  'pättm  aurvat.asp?m  .  .  yB  upäpB yazatS  Yt  ig.  51 ;  Y.  2,  5;  —  apqm  'ptär?m yasamaide  nairJm  sanh^m  Y.  7/.  23;  — b»->sat3  ahurake  'fiorS  aPqm  apasca  maida- la/aya  Y.  r.  5;  —  b^ryza  a/iura  xsa^rya apqm  V»?(VS.)Y.6'5.ia.  _  a)Nameeiner jener  Gottheit  geweihten  Örtlichkeit*'  (oder eines  Husses,  einer  Quelle,  eines  Berges): tarn  (näml.  andriin)  yaznäa  . .  sSyuidrSis pu%ra  upa  b3r?zant?m  ahur>m  xsairim xsaWm  apqm  'paism  Ylj.  73.  [na/jonm Y. ij.ii:  s.  x/alirB.napiar-.\
*)   Uiw.   einer  Wasiergolllieit   [k/J/b  ^.kö/ä),
wie  es  auch  der  indische  ^/li'm.Vu/'ii/  war;  vgl.
Grav   AfR.   s-  18.    Magoun   JAO.S.    sr.  374.
Oldenbekg  ReL  iiS,  Hillebkandt  Ved.  Mylh.
'-  .165,  3.  133.  3-  338-
KompE.;  Ableit.  —  «i.  nri/j/-,  näp!ar-{.  iiä;>tr-)
m.;    napli-  f.;    mp.  wo/,    rp.   nm-a,    navärla
(woin  Hbm.  PSt.  102).  —  Pü.  (zu  Y.  ^y.  nnf,
(so  V.  /2):  fehlt;   (lu  a):  äpän  nä/St;  {lu  Y.
j.  7):  ä/J«74;    SQ.!      ■"
erl.:
■  afäm  i
i.  Bthl.
tasmät  bljam  Jalasya  aruandasyc daiD  Sp,  Nerios.  10.  —  ')  il KZ.  ap.  572;  S  J97-  —  ')  Dl Dachgestelll  ist.  —  Sl  Wo  man  tia  afiim  (Sp. 3a  u.)  ap^m  napi  erwarten  sollte.  —  <)  Die alle  Beiwörter  der  Gottheit  erhält.  —  5)  So zu  lesen;  b.  Sü.  Statt  apan+napn  haben die  Hds,  apann+apn  (oder  daffir  auch  das Ideogramm  m  da),  Wihdiechmann  ZSt.  178 hat  Y.  46.  3  nicht  berücksichtigt.
•  j.  napta-  Adj.  'feucht':  altavat  huskatiam alsmanqm  aztavat  "ianqm  V,  7.  31;  29,  30, 33.  34;  —  kuskanqm  yavanqm  .  .  'tanan V.7.35.
Eig.  PPfP.  inm  V.  nah-,  sd.  —  PH.:  xavtL
•  j.  naptar- :  «qM'^  m.:  s,  unter  napäi-
•  j.  napti-  f.:  s.  unter  napnt-.
•  £■  (>  i)  'naptya-  m,  1)  'Abkömmling,
Nachkomme':  *yaisü  nafht^a  . .  frySnakyli Y.46.  13.         z)  'Generation' (nur Komp.).
KompE.  —  Vgl.  "tapiya-  EN.  —  Ableit.  ans napäl:  —  Pü.!  n3/.
•  j.  'naptya-  m.  EN.  eines  Gläubigen: °yehe  aiaonS  Yt.  13. 102.
Vgl.  ^»aftya-.
j.  nah-  V.  *befeuchten,  benetzen'.   PPfP. napta-^''  (sbes.);  Absol.  'napilm.
mit  aiwi  dnwS.:   s.  AbsoL  (Sp.  92  m.).
mp.  nambilan  'befeuchten',  np,  nam  'feucht',  ai. vgl.  nabkanu  f.  'Quelle''). —  i>  pl  nach  % Sj 11;  doch  s.  No.  z.  —  ")  Eine  andre  Etymo- logie (lu  ap.  wiira«  'Quelle',  lat  nrfilünui)  bei BcM,  Grdr."  I.  726  nach  Wil>ielm  BB.  12. 104.
g.  nabah-  n.,  Plur.  'Luftraum,  Himmel': iasmJ  d^rpla  zqmui  adf(sd.)  °iasalY.44.^. •ähko!-  n.  —  Pü.:  s,  unter  adf.
•  j.  nabä-nazdista-  Adj.  'der  verwandt- schaftlich nächststehend  e,  nächstverwandte'; ~i:ris  satifii  hana.ci^anqm  (sd.)  ttarqm 'lanqm  para.baraiti  V.  4.  5 ;  —  'tarn  fil . . *'asihrai/i  N.p;  —  kS  ht  .  .  ai^rapaiü-
,.  ästryeitiJ  *ts  N.  ij;  —  'lanqm  ioa asaonqm  aiaoninqmca  ahümid  datnqmca  . . Y.2(J.6; — vUpanqm  akmya  nmane  'tanqm paraÄristanam  .  .  fravasayS  "von  allen verstorbenen  Ifächstverwandten  dieses Hauses  .  ."  \.26.T,  j.  18.
Ar.  'iiahAä-naaiisIlia-  eig.  'der  der  Familie, Verwandtschaft  nächtt  stehende*.  Ar.  'nahhä. f.  'Nabel;  Familie';  ahd.  naba  'Nabe',  letl. naba  'Nabel';  vgl.  näfa-  m.;  Richter  1F.  p. 309.  —  ai.  näö/iSafdiitha-n  m.  EN.  (Ableit. ans  ar.  'naih').  —  Pü. ;  nabänaiiHsl  (Transskr.), SQ.:  ncaänvävanikaläh  'novem  familise  pro- pinqui'»).  —  ')  nahlf  (BB.  12.  105}  eiistirt nicht.  —  »)  Nach  V,  13.  i  ff.  wären  das: l)£hem,  2)Kinder,  3)  Geschwister.  4)  Gross- eitcm.  5)  Enkelkinder,  6)  Kinder  der  Ge- schwister, 7)  Geschwister  der  Eltern,  8  und 9)  deren  Kinder  und  Enkelkinder.  Vgl.  nava- naplya:
•  p.  nabukudra£ara-  m.  EN.  eines  baby- lonischen Fürsten  (Nebuhadnaar,  Sohn  des Nabonedos) :  1  martiya^  bäbiruviycr  nadt'ta- bairc^  .  .  avaUa  adurujiy<^:  adam  'ra* aptiy  hya*  nabunailahya  pu^''e^  Bh.  r.  ifij 18,  19,  4-  3,  Bh.  d;  —  iyam  arax^  aduru-
)iy<^  .  .:  adaWt  °r<^  am'iy  hy^  nabunai- Uihyä  puV(^  Bh.  i;  Bh.j.  13,  4.  3.
•  p.  nabunaita-  m.  EN.  eines  babylonischen Fürsten,  Nabemdoi:  adam  nabukudracar»^ amiy  hya''  -lahyä  pu%^<^  Bh, /,  16,  J.  13; —  'taAya  pü^'a*  Bh.  4. 3»,  Bh,  d,  i.
j.  m>/>ir- :  I.  unter  nafä/..
dby  Google
I04I  naohuämant-  -
g.  ttafhi-lä :  s,  anter  nafit-.
•  j.  naehui'mant-  m,  Name  eines  Bergs
oderGehiTgs:  aAmaj  Aa/a  ffaraysß-aäx^an .  .  säirivas^a  "masca  Y(.  ig.  4,
Eig.  Bed,?  ~    'TiaaAm-  (=—  ar.  *nasul-  oder
•  ].,  g.  Dana  Adv.  i)  'an  einem  besondem Ort,  abgesondert';  yJ  dät  ntanS  vahyS mazda  asyascä  .  .  %waAinl  xratä  apsmim °nä  aahat  "wer  sein  Denken  (jetzt)  besser macht  und  (jetzt)  schlechter  ,  .,  der  wird nach  deinem  Ratschluss  zuletzt  abgesondert sein"  Y,  48. 4''.  z)  'an  mehreren  ver- schiedenen Orten',  attrib.  sva,  'verschiedene, mehrere';  nabänazdists  aat  kavatqm  'na yahmi  "parftili  ". .,  aber  von  mehreren einander  gleichstehenden  der,  bei  dem  er den  Einwand  erhebt"  N.  79;  —  naba- nazdistfm  ,  .  äat  *havatqm  *°na''>  aihra- paittm  ", .,  aber  von  mehreren  einander gleichstehenden  den  Lehrer"  N.5J'.
KompA.  —  ai.  nänä  Adv.;  s.  daiu  BtHU IF.  10.  10,  12.  116.  —  Pa.  (in  N.)r  ^«/(?,  IF. 12.  1 1 7),  (m  V.) :  vtart  u  ian  «.  —  i)  Zuletzt  zSt. IF./2.  117.— ')  Hd».  aba,  s,  aber  Pü.  —  3)  IF. 12.  115.  —  *)  Weil  man  das  Wort  mit  Harim narlm  V.  JO.  Z  in  BeziehuDg  brachte.
•  j.  nana'rlstay-  m.  EN.  eines  Gläubigen: Uois  paisatat3h5  ai'aonS  Yt  13. 115,
Eig.  'da  und  dort  Sorge  tr^end';  "tastay-  f., .™  V.  rld-  (S  51  II),  ..  in  räl... j.  natalima  N,  86:  lies  tii  nUima.
•  j.,  g.namV,'sich(weg)beugen'.  Praes.3 tuma-,  3  °nma-,  4  näma-,  30  (Kaus.)  »3- maya-.  —  PPfP.  *'nala-;  Inf.  nsinSi.
parö  a^rlf  baoh^  dürSt  tumaiii  Vyt 5/(?).         S.  noch  Inf.
mit  apa  'entfliehen,  weichen  von  —  weg' (Abi.  mit  ha^ä):  paoirXm  i^annS  apani- mata  .  .  yimat  kaca  Yt  J^.  35.
mit^a  i)  'fliehen',  absolut:  /ränämailt . .  artrS  mainyul  Yt/p.gö.  a)  'fliehen vor  -'  (.pars  mit  Abi.,  Lok.):  hö  nöit taritS  *franämaite^^  .  ,  parS  dafvatibyö Y.57. 18;  — frä  akmat  parB  vlspe  daiva tarita  tumanle^.sy.i&,'^t.f).n{wQn3m/irite); — yä^a  assm  mit tarÜS  fra.nmäne .. pat daSvalibyS  Yt.5.4;  —  a?iu pars fränämaiU alsmö'VLit).')^.  3)  Kaus. 'niederbeugen, eindiiicken':  frS  *parst)m  nSmayänti  .  . ßättayänti  (sd.)  Yt.  14. 56.  Undeutlich ; yat  */ranata'^  bun  N.Ö5.
mit  VI  'sich  auseinander  tun,  -ziehen, -dehnen':  ärmaite  fraca  üia  vlla  mmataka
nay-  1043
harShre  pasvqmla  . .  "Arm.,  geh  vorwärts und  tu  dich  auseinander,  um  tragen  zu können  .  ."  V.  2. 10.  a)  Kaus.  'aus- einander treiben,  sprengen':  fravasayS  .  . yi  rasmanS  .  .  vf  ma&iyqmtn   namayeinti
Yty.39-
ai.  nämate,  nämaya'i;  naiah,  ni-näme;  mp. fra-nämilan  (usw.;  s.  Pü-V  -  Pö.  (lu  V.  57)- änäniT/an,  (la  V.  i):  awnämilanS.  ~  1)  Pt4; s.  daj  folg.  mmanle.  —  ')  So  T,  Ausg.  'Hl/a. Pä.:  fehlt  —  3)  Das  .i  darin  ist  Dach  /"J:.- Manier  mit  ^  dargestellt.
•  *iiainra-vak-"  Adj.  'ehrerbietige  Worte sprechend':  'växs  F.je,
Adj.;  np,  nanu  'sintl,  weich'.  —  Pü.:  ä/^i grwiln,  —  I)  Hds.  namnra'.
•  i->  K-.  P-  oay-  V.  'leiten'.  Praes.  2 naya-,  3  nya- '',  1 7  (FuL)  naSiya-;  j-Aor.  i
i)  'Jemanden  leiten,  führen':  darisa  nä pairyaQxtaca  . .  ^nyete  usianavaitli'  vTspä /rasutfiain/ (sd.)  P.jÄ  a)  ["hinführen, hinbringen  zu  —'  (abiy  mit  Akk.):  Äauv {ih''d'laxinam  agarbäye^  anayi^  abiy  mSm Bh.2. 14;  5.1;  —  fravartis  .  .  anayatä (in  pass,  Sbn)  abiy  mim  Bh.2.  13;  — hatev ,.  baitJ*  *anayaiä  (pass.)''  abiy  mäm Bh,  1. 17.  3)  'wegführen,  wegbringen':
*astB.vj%Stus  dim  bandayäti  vayö  dim batUm  nayeiti  V.  5. 8 ;  —  sp3n>m  *naisyuti FrB.(?).  a)  mit  Angabe  des  wohin? durch  Akk. :  tsm  *vä  ahum  dngvantB  syao- %anaU  c^äii  dama  nalsat  (Konj.)^'  "zu solchem  Leben  (aber)  wird  euch,  ihr  Drug- genossen,  ob  eurer  Taten  das  eigne  Ich führen"  Y.j/.  20.
mit  ava  i)  'Jemanden  herabfUhren, ■holen  von  —  her,  aus  — '  {haca  mitlnstr.): avanayeni  spmt>m  mainyBm  kaca  . .  *garö nmäna  Yt  75.44.  2)  absolut  'reissen', \omVi 3SStT :  rat)hqm  *avajtayHntTm''^"dit reissende  R."  P.J"^.
```


## [2026-09-07T17:40:41.143Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ned- ===\"; grep -n \"ned-\\|nascim\\|necto\\|nexus\" POK_full.txt | head -20\necho \"=== POK nem- bend ===\"; grep -n \"nem-\" POK_full.txt | head -20"
}
```


### [2026-09-07T17:40:41.205Z] TOOL RESULT

```
=== POK ned- ===
3246:Npers. a5(lengthened-grade form) "millstone, grindstone'; gr. OKn "point', lengthened- 
45483:1 . fltextension kened-, kena-d-: 
62018:Root / lemma: ned-1 : ned- {*he- noud-1) 
62026:Latin presumably nassa ( *nad-s-a) "basket for catching fish; a trap| snare '; necto, -ere, 
62035:nessa f, coru. nes. Middle Breton nes, nessaffds.; Old Irish nasc/m^b'\n6, verpflichte' {*ned- 
62077:Root / lemma: ned-2{*he- ned-2) 
62083:Root/ lemma: ned-2\ "to sound, roar, etc...' : Root/ lemma: neid-2: nid-\ "to flow, stream' 
62093:(Dalm.) from * ned-to-. 
62162:Root / lemma: ned-2\ "to sound, roar, etc...' : Root/ lemma: neid-2. nid-\ "to flow, stream' 
79233:related roots snep-, sneu-, sneu-, (s)ner-, also netr-a66er, viper'; s. also 1. ned-S. 758 f. 
=== POK nem- bend ===
26237:besides Indo Germanic em- formant the rhyme rooisjem- and nem-, probably originally 
26324:also (see below nem- "bend') Old Irish nem{n. es-stem), nir. neamh, cymr. corn, nef 
27016:course, as everybody knows', nem-ut6s.; ne' yea, in truth ', instrumental; 
62524:Root / lemma: nem-1 {*he- nem-f) 
62530:Root/ lemma: nem-1 {* he- nem-1)\ to take; to put in order, count, curse, bad name, 
62552:That \/t[ioq n. " meadowland ' here belongs, is not totally certain; see below nem-2, 
62575:Root / lemma: nem-2 {* he- nem-2)
```


## [2026-09-07T17:40:43.889Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ned-1 ===\"; sed -n '62010,62078p' POK_full.txt\necho \"=== POK nem-2 ===\"; sed -n '62575,62640p' POK_full.txt"
}
```


### [2026-09-07T17:40:43.969Z] TOOL RESULT

```
=== POK ned-1 ===


Root / lemma: ndo'^-2{*he- ndo^-2) 
See also: see above S. 315 f. {endo!^-). 
Page(s): 758 



Root / lemma: ned-1 : ned- {*he- noud-1) 

Meaning: to roll up; to attach, bind 

Material: 1 . Latin nddus^Vx\o\! (Indo Germanic *nddos)\ 

Maybe abbreviated alb. nuje, nyJe^Vx\o{' a Latin loanword. 

Latin presumably nassa ( *nad-s-a) "basket for catching fish; a trap| snare '; necto, -ere, 

nexT, nectum^ tie, bind, knot, bind' is neologism after yC>/ec/d"plait| twine '; with the meaning 

' near ' from 'narrowly joined': Oscan nessimas Horn. PI. f. ' proximae ', Umbrian nesimei 

"near| nearly; close by; almost '; 

Old Irish Kompar. nessa. Sup. nessam' propior, neighbor; nearest one ', cymr. nes, 
nessa f, coru. nes. Middle Breton nes, nessaffds.; Old Irish nasc/m^b'\n6, verpflichte' {*ned- 
sko), amenas'\ will bind' (etc.), na/dm^6as Binden, pact, covenant', for-na/dm^ band, 
strap', nasc^nng' (compare to -s/r-formation Old High German nusca, that also 
corresponds \v\ u= e, further Avestan /7as/r5- 'anthology (of texts), text collection ', 
probably actually 'bundle'); bret. naska 'band, join together '; 

Gothic nati. Old High German nezzi. Old Saxon net, netti. Old English Old Icelandic net 
'net', lengthened grade (as Latin nodus). Old Icelandic noti. 'big net'; 

with formant -s-k-, -s-t-: Old High German nuska. Middle High German nusche^ coat 
buckle ', Old Saxon n usk{i) a ^c\as'^, hairpin ' (see above); Old Icelandic nist, n/st/n. ' 
braces in the dress ', /7/5/a 'stitch together'; nesta' fasten with needle or thread, nail ', 
Middle High German nesten (neste/n) ' fasten, lace, tie ', Old High German nestilo, nestila 



'loop, strap, bandage'. Modern High German Nestel, Old Saxon /7es///a "bandage, 
hairband ', agutn. nasi, nestlr, reduced grade Old English nos(t)le^b3iU6, strap'; 

Maybe alb. nuske^ magic wrappings ' : alb. nuse^ bride'. 



there nec/-\s an extension from (s)ne-^ zusammenarBnen ', besides through the 
meaning also through the s-anlaut. forms Old Irish snaidm^Vx\o{' (compare above naidm) 
and Modern High German Hessian Schnatz^ das geflochtene und um die Haarnadel 
qevyickelte Haar der Frauen, Kopfputz der Braute ' ( *snatta-W\Vc\ Germanic -//-) probably. 

2. Here presumably the names of the nettle: 

Gr. dSiKPi ( *nd-ika)\ Old High German nazza. Old Icelandic ngtr. Old High German 
/7ezz//a (Germanic *natildn). Old English netele; besides with Indo Germanic -/- (also *n9-t- 
, no-t- as /-extension to the supposed root {s)ne-) Old Prussian noatis, Lithuanian notere, 
/yo/Ae "nettle', /7o//y/7e "dead-nettle', Latvian natre, natra^v\e\.\.\e\ Slavic *natb^ herbal 
leaves ' in slov. /75/(Gen. nat?}, poln. nacds. and at most (as redupl. proto Ce\Wc*ni-nati-l) 
Middle Irish nenaid, nir. /7e5/7/d^ "nettle', dissimil. bret. linadAs. 

References: WP. II 328 f., WH. II 144 f., 155 f., 172 f., Trautmann 194, H. Jacobsohn Arier 
under Ugrofinnen 90 f.; 
See also: see below (s)ne-. 
Page(s): 758-759 

Root / lemma: ned-2{*he- ned-2) 

=== POK nem-2 ===
Root / lemma: nem-2 {* he- nem-2) 

Meaning: to bend 

Material: Old Indie namas- v\. = Avestan nemah-n. ' bowing, bending = worship, 

veneration, grace'. Old Indie namat/' bows, leans, bends' (Kaus. namayati), Avestan namaiti^ 

bends ' {namaiti, Kaus. namayeiti), with apa-, /^5- 'escape, flee'; participle Old Indie nata-^ 

bent, curved '; 



gr. vt[ioq n. " meadowland ' = Latin nemus, -oris' grove ', etc.; gall. v£pr|Tov ' sacred 
grove ', PN Nemeto-briga, VN Nemetes, Old Irish nemed' shrine ', then "privilege, privileged 
person'; asachs. nimidas' sacra silvarum '; Lithuanian FIN Nemunas' Neman, Niemen, a river 
of western Belarus ' (= ' marshy stream'), nemuoge' blueberry '; gall. nanfo\a\\ey', tr/nanto' 
three valleys ', VN Nantuates, cymr. nant'vaWey, stream, brook' {*nm-tu-, compare 
participle Old Indie nata-irom nmto-); savoy. /7a 'stream, brook'; perhaps here Old Irish 
nem'sky, heaven'; different above S. 315. 

References: WP. II 331 f., WH. II 158 f., E. Frankel REIE. 1, 405 ff. 
Page(s): 764 

Root / lemma: nepot- {*he- nemot^ 
Meaning: uncle; nephew, *descendant 
Grammatical information: fem. nepff- 

Material: Old Indie /74o^/ (secondary naptr-) " grandson, descendant ', Avestan napat-, 
naptar-, ap. napat- (is.. Old Indie apam napat, Avestan apqm napa-u. name of a divinity (" 
primeval offspring of the waters '); hom. vsnoSsq (5r|or|) " young ones, children ' from a N. 
Sg. *V£TTU)T(;; perhaps here lemnisch-tyrsenisch vacpoG "offspring, descendant, son' 
(Kretschmer, Glotta 28, 266); alb. nip' grandson, nephew '; Latin nepos, -tis^ grandchild, 
grandson ', later also ' nephew '; Old Lithuanian nepotis, /7e/0^c//s "grandchild, grandson'; 
Old High German nevo' nephew, kinsman, relative'. Old English /7e/& 'grandchild, 
grandson, nephew ', Old Icelandic nefe' nephew, kinsman, relative' {*nepdts); Middle Irish 
n'i'ae. Gen. n'lath' sister's son ' (for the form in the end Pokorny ZfceltPh. 10, 405 f.), cymr. 
nei, nai6s., corn. /7c»/"grandchild, grandson'. Middle Breton /7/" nephew '. 

Fem. Old Indie /7a,c^- "granddaughter, female descendant ', Avestan naptT- 
"granddaughter'; 

Latin nept/s {ior -///Sy) after the Astem) 'granddaughter', later 'niece'; Old Irish necht, 
cymr. abret. n/th. Middle Breton n/z, corn. /70///7 'niece'; (common alb. Celtic -f-, -ph- > -ch-, 



Old High German n/ft'r\ept\s, privigna'. Modern High German (actually Low German) 
Nichte, Old Norse nipt' sister's daughter, niece'; Old Lithuanian /7e'yO/e 'granddaughter'; 
russ. -Church Slavic nestera 'n\ece' {*nept-tera). (common Slavic -pt- > -st-) 

further formations 'i^e/T/irb-/ Avestan naptya-' offspring, descendant '; alb. {^harness!) 
mbese 'n\ece' from *nepdtia; 



\\b. Geg mesa, Tosc mt>esa'n\ece (sister's daughter)' derived from Hittite Luwial 
a descendant); Luwian /7A7sa "grandson' : Hittite hamsa- hassa{a grandson) : Latvian 
nasas-me/ta^ niece (sister's daugliter)' = Latvian /77asa"sistei^^l^^7o£g^7o^^^sisten 
i me/ta 'daughter'; alb, has lost the AnatQiian old larygeaj 



gr. a-v£4Ji6(; " brother's or sister's son ' ( *sm-nept//os)] russ. -Church Slavic net/jb ' nephew 
'. (Greek Occidental Romance vowel prefix)
```


## [2026-09-07T17:41:00.953Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY نخ ===\"; grep -n \"^\\s*نخ\\s*$\\|نخ ,\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY نرم/نان/نیزه ===\"; grep -n \"نرم\\|نیزه\\|نان\" incoming/ARY/ARY_pages.txt | head -20"
}
```


## [2026-09-07T17:41:02.143Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON نخ ===\"; grep -c \"\" MON_part1.txt MON_part2.txt\ngrep -n \"نخ\" MON_part1.txt | head -5\necho \"=== MON ls ===\"; ls -la MON_part1.txt MON_part2.txt"
}
```


### [2026-09-07T17:41:02.221Z] TOOL RESULT

```
=== ARY نخ ===
=== ARY نرم/نان/نیزه ===
28:شترکك» واژه‌های همريشه در زبان‌های سانسکریت و ارمنی و یونانی ولاتین و آلمانی و انگلیسی و
76:دانشمندان اروپایی (به ویژه آلمانی زبانان) نام «هندوژرمنی) (1300-0880/۸11807 با
83:می‌بردند و وپژگی‌های بدنی و اجتماعی و فرهنگی آنان را مورد ستایش قرار می‌دادند. در دوران
127:(1-817811۸7) آنان شمال اروپا (به ویژه آلمان) بود. همانطو رکه در پالاگفته شد» نازی‌های آلمان
133:آلمان به خارج مهاجرت کردند ولی هر چه از آلمان دورتر شدند آمیزش آنان با اقوام محلی موجب
182:شدند. مردمان این نواحی (مثلا ساکنان آذربایجان و ترکیه) همه به زبانهای هند و اروپایی تکلم
183:می‌کردند ولی سلطه‌ی ترکك زبانان موجب شدکه طی چند قرن زبان آنها ترکی بشود ولی زبان ترکی
205:هندی» اسلاوی» بالتیکه) و زبانهای سنتم 4 (ژرمنی» لاتین» یونانی» سلنیک). در زبانهای
217:به‌جلگه‌ی تارم (باختر چین) کوج کردند و علت شباهت زبان آنها با یونانی و سلتی همین است؛ آیا به
291:همریشه‌اند می‌توان نتیجه گرفت که آنان در رام کردن اسب و استفاده از ترابرهای چرخدار پیشگام
381:آن به عرش برسد. خداوند از این گستاخی آنان به خشم آمد و ناگهان زبان آنها راکه عبری بود تبدیل
382:به زبانهای متفارت کرد به طوری که آنان دیگر حرف‌های همدیگر را درک نمی‌کردند و مجبور شدند
429:برخی از آنان که فرهیخته تر بودند با شگفتی دریافتند که شباهت عجیبی میان سانسکریت و زبانهای
432:ریژه اوستایی) پرداختند شگفتی آنان بیشتر شد چون ایرانی باستان نیز هم پا مانسکریت و هم با
462:ونان دادن 5 07۲ الفطاهمه ۴
465:دادن نان هام16 نس سنا
517:است: از یونانی کامل‌تر و از لاتین پرواژه‌تر و از هر دو به طور چشم‌گیری پالوده‌تر
544:باید به طور علمی و سامانمند بررسی و اثبات گردد. مثلاً آوای یونانی 2۳3 برابر است با آوای ژرمنی
545:8 چون واژه‌ی «بردن؛ در بونانی ۳۳180 و در انگلیسی 81۸14 است. واژه‌ی «برادر» در یونانی
547:نتیجه گرفت که طبق این اصل (یونانی 217 < ژرمنی 8). واژه‌ی یونانی ۳18005 (به معنی درخت
```


### [2026-09-07T17:41:02.347Z] TOOL RESULT

```
=== MON نخ ===
MON_part2.txt:94500
MON_part1.txt:99339
80:او نخست مادر و پس از پنج روز پدرش در عنفوان شباب درگذشتند. جد پدری 
109:۱ تشکیل و پایان‌نامةٌ او با قید ربسیار خوب؛ قبول گردید» و او نخستین 
181:سال ۱۳۳۳ کتاب جامع الحکمتین ناصر خسرو که نخستین بار به توسط هانری 
270:۸ -اضافه. بخش نخست. شمارة سوم از سلسله انتشارات (طرح دستور زبان 
841:جملات: آب از آب تکان نخوردن: (عم.) 
=== MON ls ===
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
```


## [2026-09-07T17:41:09.134Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== markers ===\"; grep -n \"\\[pdf page\\|^\\f\" MON_part1.txt | head -3\necho \"=== namraq ===\"; grep -n \"نمرق\" MON_part1.txt MON_part2.txt | head -10\necho \"=== nizak ===\"; grep -n \"نیزک\\|نیزه\" MON_part1.txt MON_part2.txt | head -10\necho \"=== nax thread ===\"; grep -n \"نخ ٬\\|نخ\\.\" MON_part2.txt | head -10"
}
```


### [2026-09-07T17:41:09.252Z] TOOL RESULT

```
=== markers ===
=== namraq ===
MON_part2.txt:79409:نمرقه: 00 16 ,0۱۲3۷-۵] ۱۱2 [ع. نمرقه ] (ا.) 
=== nizak ===
MON_part1.txt:4361:طلا. نامی از نام‌های زنان و کنیزکان ترکث. 
MON_part1.txt:7136:نیزه که در آن رخنه شود. (عر.) اثرم. 
MON_part1.txt:19759:دست دادن. نبزه باختن: نیزه زدن» نبرد و 
MON_part1.txt:27156:بیغال: 93,2۱ (.) نیزه» رمح. 
MON_part1.txt:30125:نیزه و علم آویزند یا به گردن اسبان بندند. 
MON_part1.txt:30726:مانعی بپرد. پرض بانیزه: (ور.) پریدن از 
MON_part1.txt:34167:ستعدد است و بس رگ‌هایش سرنیزه‌ای و 
MON_part1.txt:42780:سر چیزی مانند نوک سوزن» خنجر» نیزه» 
MON_part1.txt:52900:و نزاع مانند شمشیر» خنجره نیزه کوتاه» 
MON_part1.txt:55641:آن نیزه و تیر و زین اسب سازند. تیر 
=== nax thread ===
24650:چرخه پیچند. گلولة نخ. (کشتی) یکی از 
74658:رومی؛ زیلوی رومی» طنفسه» نخ. [- نسخء
```


## [2026-09-07T17:41:15.879Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '79400,79420p' MON_part2.txt\necho \"=== search nax headword ===\"\ngrep -n \"^نخ\\b\\|^نخ \\|نخ: \\|نخ .\" MON_part2.txt | head -10\necho \"=== search nan headword ===\"\ngrep -n \"^نان\\|نان: \\|نان،\" MON_part2.txt | head -10\necho \"=== search neze headword ===\"\ngrep -n \"^نیزه\\|نیزه: \" MON_part2.txt | head -10"
}
```


### [2026-09-07T17:41:15.987Z] TOOL RESULT

```
تمد کر : 

نمر: ۱ [ع.] (.) (جان.) پلنگ. (جا..) 
یوز پلنگ» ج. نمار» نمور. 

نمر ق؛ ۱68۵۲۵ ,16۳0۲6۵ ر۲2] 02202 [ع. ) (.) 


متکا. بالش؛ ج. نمارق. 
نمرقه: 00 16 ,0۱۲3۷-۵] ۱۱2 [ع. نمرقه ] (ا.) 
متگا» بالش؟ كی نمارق. 


نمرود. (دم)60۵۳4: [سعر .] (ا.) عنوان 
یادشاهان کلده؛ ج. نمارده. مخصوصا به 
پادشاه معاصر ابراهیم(ع) اطلاق شده. 
نمره: (0-)100172 [معر. عددء رقم] .( 
شماره؛» عدد. مجموع شماره‌هایی که از یک 
نشر به (روزنامه» مجله) در هر دفعه چاپ و 
منتشر می‌شود و دارای شمارة مسلسل است. 
عددی که معرف معلومات شاگرد و مدرسه 
=== search nax headword ===
624:که زیر زنخ مردم فربه پدید آید؛ ج. غباغب. 
4230:نخی که از آن جامه کنند؛ ج. (عم. غلط ) 
4630:نخودها دربارة شخص پیشگویی کنند. هم 
4886:نخ و ریسمان و مانند انها را تاب داده و فتیله 
10740:نخستین مرحلهٌ ایجاد قالی ریسندگی است و 
10741:آن مرحلةٌ تهیة نخ برای بوجود آوردن تار ها 
10744:نخ‌های رنگین» نقشه و قالیباف پا در میان 
10746:نخ‌های رنگین بدان آویزان می‌شود و 
12109:نخود معادل یک ریال کنونی. 
12450:نخست پیدا شود از شعاع آفتاب. رثیس 
=== search nan headword ===
4330:نان داضتم :وان : هنری. هنرور+ ج. 
6610:نان یز ند. 
7792:نان فطیر: نانی که خمیر آن درست ور نبامده 
9113:0 (۱۸)۵] [معر. فوته]| فوته نان: (ا.) 
10039:نانخورش, ادام. ترشیی که بر آش‌ها زنند؛ 
18721:نانوشته: کاغذی که چبزی روی آن ننوشته 
18956:نانی که از آرد خشکه با روغن و شیر پزند. 
21101:زنان: پرهای سیاه مرغابی را زنان بهم پیوند 
23635:نانی که از آرد باقلال و نخود و گندم و جو 
24240:کفک نان. کفک نان: (گیا.) کفک سفید. 
=== search neze headword ===
63681:مکانیزه: 6 (ص.) با وسایل ماشینی 
81916:نیزه‌به کف 
81925:نیزه‌به کف: (])]06-2-. اف. ع.] (ص مر .) 
81929:نیزه‌بندکن: ۱۰-02۱0 [- نیز ند کننده] 
81933:نیزه‌دار: ۱۰-۲ [< - نب ه‌دارنده] (ص‌فا ((
```


## [2026-09-07T17:41:23.949Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '81905,81930p' MON_part2.txt\necho \"=== نخ headword ===\"; grep -n \"نخ: \\|نخ ؛\\|نخ؛\\|^نخ\" MON_part2.txt | head\necho \"=== search 'ریسمان' نخ ===\"; grep -n \"نخ\" MON_part2.txt | sed -n '1,25p'"
}
```


### [2026-09-07T17:41:24.037Z] TOOL RESULT

```
نیر ه. (قد. -۱۱22۵)۱626()۵6 [- نیز ک] (.) 
چوب با نبی دراز که بر سر آن آهنی نوک 
تیز تعبیه کرده باشند و آن سلاحی بود که در 
جنگ بکار می‌بردند (و هنوز هم سورد 
استعمال بعض قبایل بدوی است)؛ رمح. 
چوب يا نیی که برای علم و رایت بکار رود. 
واحد مسافت»؛ بطور یک نيزة متو سط. یره 
آنشی (اتشین): ( کت.) شعاع آفتاب در وقت 
طلوع و غروب. نیز خطی: (منسوب به 


نیزه‌به کف 
خط ) نبزه‌ای که در خط (بحر ین) ساخته 
می‌شد. نیزة قلم: نی قلم» نی کلکث. نیزه بند 
کردن: ۳ .) چیزی را از کسی یا پررویی و 
وقاحت گرفتن؛ تیغ زدن (فرعا.جما.) نبزه را 
پیچ دادن: آن است که نیزه‌باران پیش از 
ارادةٌ جنگ نیزه‌بازی می‌کنند و دست و پا را 
گرم می‌ساز ند. 

نیزه‌به کف: (])]06-2-. اف. ع.] (ص مر .) 
کسی که نیزه در کف دست دارد. (کذ.) 
آفتاب» خورشید. 

نیزه‌بندکن: ۱۰-02۱0 [- نیز ند کننده] 
(ص‌فا.) (عم.) کسی که با پررویی از مردم 
=== نخ headword ===
4230:نخی که از آن جامه کنند؛ ج. (عم. غلط ) 
4630:نخودها دربارة شخص پیشگویی کنند. هم 
4886:نخ و ریسمان و مانند انها را تاب داده و فتیله 
10740:نخستین مرحلهٌ ایجاد قالی ریسندگی است و 
10744:نخ‌های رنگین» نقشه و قالیباف پا در میان 
10746:نخ‌های رنگین بدان آویزان می‌شود و 
12109:نخود معادل یک ریال کنونی. 
12450:نخست پیدا شود از شعاع آفتاب. رثیس 
15315:نخواهد» فعل صادر نشود؛ سق. عجز؛ ج. 
15492:نخستین به دو قسمت کرده‌اند: قوت و عقل 
=== search 'ریسمان' نخ ===
615:غبب: هه« [ع.] (!) گوشت زیر زنخ» 
624:که زیر زنخ مردم فربه پدید آید؛ ج. غباغب. 
755:گوشت که در میان گوشت باشد و نخورند و 
1402:(امص.) فریفتگی. تکبر» نخوت. پندار» 
1427:کند» آنجه کبر و نخوت آورد. 
1874:پوششی حول مراکز عصبی (دماغ» نخاع) را 
4230:نخی که از آن جامه کنند؛ ج. (عم. غلط ) 
4465:بخواهد فعلی را انجام دهد و اگر نخواهد 
4623:( کذ.) بیکار و پریشان بودن. فال نخود: فالی 
4628:بدیشان دهد و ایشان دانه‌های نخود را بر 
4630:نخودها دربارة شخص پیشگویی کنند. هم 
4683:استند و به سخن نخستین کسانی که از آنجا 
4886:نخ و ریسمان و مانند انها را تاب داده و فتیله 
5292:و جو)؛ نخاله. نخاله» زنک زده. کهنه و 
5456:فرابافن: 0.] (مسص‌ل.) دروغ نخ 
6833:ضمن انتفال به زمینة نخستین. ضح.- فرودها 
7199:و همچنین برخی ضایعات اعصاب نخاعی 
7799:روز نباید خمیر خورند. نخستین روز آن 
9122:تبره نخل‌ها که در مناطق کرم استا 
9156:اطماط» نخل هندی؛ پ وگافالاء اریکا. ضح.- 
9196:فوم: ۰ ۳ (ع.] (.) ( گی.) گندم و نخود و 
9207:که اصوات را نخست ضبط و سیس بازگو 
9360:بود. در مورد نخستین سکنهةٌ زمین تنها از حق 
10039:نانخورش, ادام. ترشیی که بر آش‌ها زنند؛ 
10740:نخستین مرحلهٌ ایجاد قالی ریسندگی است و
```


## [2026-09-07T17:41:33.977Z] TOOL CALL #47: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2226 --image 2>&1 | tail -40"
}
```


### [2026-09-07T17:41:40.051Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2226.png
REF: BQT:2226  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 309  OCR-lang: fas

بر <<
هت ازموسیقی ‎٩‏ . نقطه‌دار , ممروف است و بعربی‌سنان گوبند۹ -
یز ۴ - بکر اول وسکون نانی وزای | وعلم را هم کفته‌اند ۷ .
هوز » بمعنی دیگر است وبمربی ایآ گوبند۴ - نیز8] شین - کنایه از شماع آفتاب
و بمعتی بمدازاین اس بنظر آهده ات۴ ۰ است در وقت طلوع وغروب ۰
ف - با اول بنانی کشیده و پزای‌فارسی نیزه کف -« کنایه ازآفتاب عالمتاب
زده » کیاهی است که بر درخت پیجد و بعربی است .
مشقه کوند . نیز خطی * - نوعی از بیزه باشد.
نیزه * « با ثانی مجهول و فتح زای و بعضی کویندلیزه راست باشد مانند خط مستقیم.
۱ - نام غمبه‌ای از مقام اصفهان است - نیز نام آوازی است از دستگاه راست و پنج کاه
« فرهنگه نظام > . ۲ - ۰812 پهلوی 810 ۰ پازند 812 . هرن وجه اشتقاقی برای آن
آورده (راد: اسشق ساه5 6 وهو بشمان؟ نرا رد میکند و گوید فقط رشه 1۱ میتواند با
7 فارسی مرتبط باشد « هوبشمان ۱۶۹۵*. ۴ - « نیز باول مکسور وسکون ثانی وزای
معجمه , افاده معنی اشتراك ماسبق کند بكلمهٌ دیگر » و مرادف لفظ هم و واو عطف.است . >
« بهار عجم > . ۴ - « در اشمار قدما لفظ نیز بمعتی من بعد و دیگر بسیار: واقع شده .
دولتش برکسی که چشم افکند نیز در اروش له بینی چین .
مسعود سعد سلمان در تعریف رزم :...
یز جان جان را نت از هیبت تابنده تیغ نیز کس کس را ندید از ظطلمت تاری غبار...»
۰ بهار عجم له
باید داد ت که «ییز» درجملهٌ منفی معنی«دیگر» ود پی‌ا زآن» دهد : (شواهدفوق غامل جمله‌های
شتنگهی دید قیصر که یز نيامد ورا روم و ابران بچیز .
فردوسی طوسی « شاهنامةٌ بخ ج ۷ ۱۸۵۵
* - پهلوی 26286 ( بیزه ) , ممرب آن 321226 . ارمنی ع 81226 از اوستا
24 ( نو » نیغدار ) [ توك سوزن ] « بارتولمه ۱*۳۷ > ره : تیب رکه ص ۱۵۷ . و ار :
۰ 0 ,۳۳۵۳۵۲۵۲6۲ ,و514 .
‎٩‏ - بسن بر زکرد سیه ابر بت به لیزه دل سنگه خارا بخست .
فردوسی طوسی 3« شاهنامةٌ بش حج۱ ص ۵۸ ۰.۴
۷ بیزة علم : سی طوسی
چوآن پوست برلیزه بردید کی بنیکی بکی اختر افگند پی
بیاراست آنرا بدیبای روم ز کوهربرو پیکر وزرش بوم.
فردوسی طوسی در وصف درفش کاوه « شاهنامهة بخ ج۱ص1۸ نج
۸ - باقوت در معجم‌البلدان‌آرد : «الخط . بفتح اول‌آن وتشدید طاء. در کتاب‌المین» الط
زمینی‌است » منسوب بات رماح خطیه » وچون بت را اسم لازم فراردهی »کوبی خطیه‌ورماح
را ذ کرنکنی» وآن «خط» عمان است. ابومتصور کوید همه این‌ساحل را خط نامند ومراد ازقرای
خط,قطیف وعقیر وقطراست. من کویم : همه اینها درساحلپحربن وعمان است. وآن مواضمی‌است
که از هند نیزه‌ها بدانجا آرند وراست کنند و بعرب فروشند . » ( برهان قاطع ۲۸۱ )
```


## [2026-09-07T17:41:47.966Z] TOOL CALL #48: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2107 --image 2>&1 | tail -35"
}
```


### [2026-09-07T17:41:56.109Z] TOOL RESULT

```
۰ 3 ۰ ۰ ده
.اکویند - ویمعنی کناب هم هست همجوشاهنامه نان آتش روی + کنایه از آفتاب
وفرس نامه و پازنامه وامثال آن - و بمعنی‌سیلاب | عالمتاب است .

۱- « میندارید که آمدم تا ناموی وتوریت باطل کنم . نه نیامدم که منوکنم .. >
( قول عیسی4 ) «* انجیل فارسی ص*۹ *. ۴ - رك4 : اقرب الموارد . ۴ - رغیدی
کوبد ‎ :‏ هعنی ترکیبی آن منوب به « نام » » بعنی درآن‌کار نامدار و نامو رکشته » ظ . از :
نام ۳ وبه ( پسوند ) ۳ 06 که معرب آن « ویه » بفتح واو است [ قن : شیرویه » سیبویه .
مسکوبه ] رك: نلد که. تبعات ایرانی. وین ۱۸۸۸ یمد .

۴ - صولت او در آن صف ناورد زن ناموبه بر کند از هرد .

سنائی غزلوی «جهانگیری» « رشیدی *.
موْلف فرهنکه نظام نود : « ناموبه مر کب از با (نه) و موبه ( زاری ) است (1) و بمعتی زلی
که موبه نکرده (۱) یعنی شوهردار است و معنی شعر این است که ممدوح درجنکه زق شوهردلر
را بی شوهر میکند .> قس : نامزد . * - پعلوی 820281 (کتاب ) مأخون از « تام »
« نیب رکه ص ۱۵۶ > » کردی ع 88816 ( مرامله ) « ژابا ی 2۱۹ *.

۰ ‏در جهانگیری و بنقل از او در رشیدی آمده . ۷ - ر3 : جهانگیری‎ - ٩
۷ ‏رشیدی . ۸ از: نام +ی(دبت)» پهلوی 13201۷۴ بمعنی نامور ومشهور2 اسشق‎

‎٩‏ - مصحف با تلقظ عامیانهٌ ‎٩‏ نامه > (ه.م.) *۴- و نیز « نان آتشین » بهمین
هعنی « رشیدی ؟ .

‏2 لامیدی - از : نام ۳-یدن (پسوندمصدری) ؛ پپلوی 114132111870 ۶ اسشق ۱۰۲۲ 44
نام گذاشتن -کسی را بنام خواندن - احضار کردن .

‏نان - پپلوی 328 ۰ آرمنی 13628 (نان‌پخته درخا کتر): مأٌخوذ ازپهلوی 1627
«پارسی 0818۵8 ۰ بلوچی 338210 و نظابر آن » از ایرانی ( باستان ) 028888 ۰ منجعی
080 > رك : اسشق - هوبشمان ۱۳۲۳ . نیب ر که نیز کوید: نان (فارمی) ماخوداز 828138
است و ارجاع به هرن و هوبشمان کرده « نیب رکه ص ۱۵۶ *؛ کردی 888 ۰ 830 ۰ زثزا
11 ۰ 11 ۰ دوجبکی 30 « ژایا ص اه چا ؛گیلکی ۱1 ۰ فریژتندی + برلی‌واطتزی 108
7دک ۱ص ۲۹۰ سمتانی 31173 ۰ سنگسری وسرخه‌بی3118 ۰ لاسگردی ۰8070 شهمیرزادی
0 که .۲ ی ۱۹۶ ؛ قطعه‌ای از آرد خمین کرده وبرآتش پشته کهآ ترا خورند. -
```


## [2026-09-07T17:42:07.404Z] TOOL CALL #49: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2130 --image 2>&1 | tail -30"
}
```


## [2026-09-07T17:42:08.737Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS nan ===\"; grep -n \"nān\\|nan\\b\" SNS_pages.txt | head -10\necho \"=== SNS 223 ===\"; grep -n \"\\[pdf page\" SNS_pages.txt | head -3"
}
```


### [2026-09-07T17:42:13.589Z] TOOL RESULT

```
رم بر ۴ - بم بای ابجد. و سکون تنك و ملایم است کهآ درا بعیرازی لرمه کوبند.
رای قرشت , نام افزاری است درود کراثر! وآهن نرمسار ۷ بر وزن شرمار » بمعنی:
کرانرا - وکنایه از مردم چاپلوی و حیله‌ورهم | بردبار و صاحب حلم و حلیم باشد .
.هت نرم شاه » با شین «قطه داز و دون »
قرم‌لیز * « بکسر بای ابجد وسکون | کنایه‌ازکاهل - وکم قدرت - ومطیم باشد۸ .3
۹ - ر4: ار که. مرحوم بهار در سبك شناسی ( ج ۳ ص۹۹ ) در زمرة لغات مغولی که
ولرد فارسی شده نوشته‌اند : ‎٩‏ ار که. بمعنی شکار جر که ( درتازیخ سیستان بر که بیاه ) و فارمی
آن « شکار رژه است که درسپقی‌چاپی: ۸ شکارژه » بفلط چاپ شده است .» درتر کی‌جغتایی «با رکه»
بمعتی حلقه با دایره‌است که بدور چیزی ایجادکنند « جفتابی ص ۵*۸ *.
1 ۴ - ۶۸ نرم‌آهن » لفة بعنی‌آهن نرم » معرب آن لرماهن . وآن بنوعی از آه نکه درم"
است. لطلاق شود « دزی ج؟ ص ۹۵۵ ۰
۴ - تو درمن چه ارم آهنی دیده‌بی که پولاد او را پسندیدء ی ۰
۰ نظامی گنجوی«رشیدی» «بهارعجم» » قس: لرم‌شمشير.
۴ - از : درم بر ( برنده ). 8 - از: لرم ۳ پیز ( بیزنده ) » رك : بهار عجم.
۹ - در کدازم ز شرم مدعیان لرم چشمان چه سخت روبانند!
نلهوری « رشیدی ؟ .
۷ - از : نرم سار ( سر » پسوند) .
۸ کی که هرچه بگوبند همان قبول کند و هرچه تکلیفکنند تن در دهد . فقس :
ترم کردن : بقیه درحاشيهٌ صفحهٌ ۷۱۳۱
ارم - بفتح اول, هندی باستان .- 81748 2(مطیعءمنقاد).اوستا 5/107 ۰32772۳2۰۷226
پهلوی 3372 (نرم , لطف) » افغانی وبلوچی و وخی 327۲۷ «اسشق ۰۱۰۲۸ کردی 36۲770 »
2 » زازا 3627 ۸« ژابا ص ۶۱۸ - ۱۹ ؛ جمی که بهنگام لمس و تملی لطیف و ملایم
بماید . ضد سخت : « شبی که آتش مطبخ در انبار هیزمش افتاد ... و از بستر لرمش برخاکستر
گرم بشاند گلنتان ص 4۸ له
ارم دعثیر - بفتح اول و چهارم (درلهجهٌ مرکزی بکسرچهارم) » مجازاً هرد سست.
مبلرز زبون » قس : لرم‌آهن :
سختی پنجةٌ اسیه شیران کوفته مغز رم شمشیران .
نظامي کنجوی « نوروزنامه . تعلیقات ی ۱۳۶ ۰
( پرهای قاطم ۲۹۹ )
```


### [2026-09-07T17:42:13.645Z] TOOL RESULT

```
=== SNS nan ===
1798:         COVPff. 59)blra       :   L bhlma            :L bh&nan- bhay-:,*^-**                                U .jb^^*..^!^ Sbustanj Sbistan                                  j   abist
2112:•   U^a ^alA j      a* j3jj       .>*--   oU^j J0» Jj*' 'Ci^*- T:S sniain:                                           ^^j                    •&** o^'*-** 'o^^j>iT :3sarvanan/asr0nan:                       %?J^*»j»
3346:                                                                                                      \*i*j* jx» j'*£*iL-S:avizIdar                   dahisnan: v^^O i-i^Cf
5426:                                                                             patil + *mana   i^^y prati + /Tnan: *#%*.,                         fc,*
5684: Zoroastrian ProfcZems in The Ll'Centurij*                                                                                                                                               -j*l«jja-di^U>:frainan:             ^^ej
7026:                              .fa/l**         Uoj-o^j: zanan:                         <£                                                                 •   CjUj :zaia3n:           ^^3        1°
8206:                                                                           L nanan-      *fc-                                                                            I** • f>S   :sarm: ^-*U
8771:         **oM9^ho \&) .UjK.U^tkunisnan: ««M»3                                                  kusnati,              ^kOs  L kusaiti, /kaos-
9742:                                                                                      » Jj.jiji^. aS^LS ^bljjUT^ :margarzanan:
9822:                                                                                      . .   .   a t5j*J9 iym tS^LS                ^bljjUjt :margarzanan:                                      ttvu-o^
=== SNS 223 ===
```


## [2026-09-07T17:42:29.256Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN nan entry ===\"; grep -n \"1022\\.\\|1023\\.\\|1024\\.\\|1021\\.\" HRN.txt | head\nsed -n '8850,8900p' HRN.txt"
}
```


### [2026-09-07T17:42:29.310Z] TOOL RESULT

```
=== HRN nan entry ===
8879:1023. nän 'Brot'.
8886:1024. näv Wasserkanal; Schiffchen', nävdän.
13016:»dm 1022.
13028:: ua., 1023.
13090:1 Häo 1024.
13115:iiävdän 1024.
14238:näman- 1022.
14240:liäviyä' 1024.
14911:uaväza- 1024.
14921:nävaija- 1024.
232 Zeile 2, 3), nastab, nastat,
na + ai. V^aQ-, agndti *essen', Nöldeke, münd-
liche Mitteilung, doch vergl. unter np. äs (No. 29).
1020. nfe/ 'Nabel', nafe,
g. nafk.
aw. nafah' 'Geschlecht*, vergl. nOfya^ 'Verwandt-
schaft*; phlv. nafak, f?^/ 'Nabel', vergl. N[a]f^[far'nai
(Gemme, ZDMG. 18 No. 37 (IV)).
>) Vergl. S. 197 Anm. 1.
2) Vergl. Bartholomae, BB. XVII, 133.— 229 —
kurd. näw 'Nabel'; afy. nti^ nüm; oss. d. naffä;
bei. napag, nafag, n. nafay (259).
aw. naba[nazdista', ai. ndhhi- etc. gehen auf indog. bh
zurück, während die übrigen Formen auf ph weisen.
lOS^O'»'» nak Vermischt, nicht pur, verunreinigt*.
phlv. andk *böse', anokih^).
lC^t21. noffäh plötzlich, unerwartet*.
aw. *anäkasa' *improvisus* ; phlv. anakäslhd 'un-
vermutet', vergl. np. (igäh (No. 40).
näl 'Schilf* siehe nei (No. 1060).
1-022. näm 'Name' 2).
ap. nOtnan- 'Name* ; aw. nquian- ; phlv. mim, nCLmik
berühmt*, nämlnltan (PPGrl.); ai. wamaw- ; arm. anim
(H. No. 24).
LW. (?) kurd. näw 'Name' ; afy. nüm ; bei. nam
(181) ; oss. (echt) t. nom, d. non (198).
Rückert wollte ZDMG. 10, 219 auch neng 'Schimpf,
Schande', hierherziehen (als 'ein unregelmässig zu-
sammengezogenes Diminutiv von näm*).
1023. nän 'Brot'.
arm. nkan iyygvcplac *unter der Asche gebackenes
Brot'; vergl. chorasm. pekend (Vullers); hei. nagan,
n. nayan *Brot', nagan[pad *Bäcker* (249) ; minj. nayan;
phlv.-päz. nän (PPGl.).
Also zu l/^kan- + ^h ursprünglich '(unter die heisse
Asche) Vergrabenes* (zuerst de Lagarde)?
1024. näv Wasserkanal; Schiffchen', nävdän.
ap. näviyä' 'Flottille'; aw. navOza^ 'Schiffer* (Bar-
tholomae, ZDMG. 46, 294 Anm. 3), vergl. nävaya-
'fliessend'; phlv. nävfäk (aw. nävaya-), nävTcak (Bund.);
ai. näV' 'Schiff, Kahn, Nachen*, vergl. nävyä- *Strom*.
kurd. LW. nav; oss. LW. d. navä, t. nau- 'Schiff';
arm. nav 'Schiff*, navem 'schiffen* (H. No. 216).
naf 'Schilf*, vergl. tiäüej siehe unter nei (No. 1060).
*) Justi vergleicht ZDMG. 46, 282 arm. N. pr. Anak^ aber gegen
seine Lesung der betr. Gemme sprechen die voUständig deutlichen
Buchstaben auf dem Steine.
«j Vergl. Bartholomae, BB. XVII, 132.230 —
V
1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
Vers 586).
```


## [2026-09-07T17:42:37.943Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3530,3565p' HUB.txt"
}
```


### [2026-09-07T17:42:37.986Z] TOOL RESULT

```
wie so nicht und gehSrt wohl gar nicht hierher. Np.
mvno setzt Horn mit Recht = zd. mainyava-.
1012. Noldeke, Tabari 101 hat Km-mihan.
1014. Fiir na^ (in Comp.) und na nicht' steht im PSz.
durchweg wg = ap. waiy, vgl. Min. 61. 143 und Shk.
259. Daraus ist np. na, alter noch ne (vgl. nest 'ist
nicht' und nay-amad er kam nicht', Salem. Shuk.
Gram. p. 16 und 59) entstanden. Die nachdriickliche
Form nai reimt nach NSldeke auf kaL
1015. Dazu arm. LW. anapak ungemischt, rein (vom Wein).
1017. Dazu arm. LW. naz-i-m *thue stolz , briiste mich,
liebkose' (5. Jhd.). Im Phi. ist ndzuU zu lesen.
Afgh. nazuk (mit u) bei Raver ty; nazaka, nenzdka f.
heisst *Puppe*.
1019. Vgl. gr, v^OTig 'niichtern', das aber zur Wzl. ed essen'
gehSrt.
1020. Dazu kurd. noheh 'Nabel' (Socin , kurd. Samml. II, 339),
arm. napak 'Moschusbeutel' (bei Moses, Geogr. ed.
Soukry p. 44, 7 v. u.) = np. ndfa 'Nabel, Moschus-
beuteV (afgh. LW. nafa *a pod of musk*).- 101 —
1023. Arm. nkan ftihrt zu phi. nikan ^) = np. *nigan, aber
nicht zu nan. Bal. nagan etc. setzt Iran, "^nagan^
voraus. Zur Noth liesse sich fUln vielleicht aus
"^nayna- erklaren.
1024. Zd. navaza- (KZ. 27, 252) = arm. LW. navaz 'Schiflfer*
= skr. navajd- = lat. *navigu8 (in navigare) ZDMG.
35, 662. — Hierher auch np. naxudd *Schiflfscapita,n*
aus ''^nav'Xuda.
1026. Dazu np. naryan 'Hengst', von gleicher Bildung wie
mOdiydn 'Stute' (aus *nartkan, '^matlkan).
1032. Die Form nisaxtan auch bei Fird. I, 246, v. 57 als
Nebenform von niSastan, vgl. Horn Nr. 1033.
1033. Praes. niStnam aus "^nisldndmiy wie sikanam aus
*8kadnamiy? Vgl. Fr. Miiller, WZKM. 6, 190. —
Dazu afgh. -nastql sich setzen', pr. 3. sg. -nF, ptc.
.'nOst (mit der Praep. k^S- zusammengesetzt).
```


## [2026-09-07T17:42:52.106Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD narm ===\"; grep -n -i \"narm\\|^soft\" PHD_mackenzie.txt | head -10\necho \"=== NYB narm/nezak ===\"; grep -n -i \"narm\\|nēzak\\|nān\\b\" NYB_vol2_glossary.txt | head -10\necho \"=== AHD ned ===\"; grep -n -i \"^ned-\\|ned-\\b\" AHD_watkins1985.txt | head -10\necho \"=== AHD nem ===\"; grep -n -i \"nem-\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-07T17:42:52.187Z] TOOL RESULT

```
<persisted-output>
Output too large (29.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bzrdkuvjk.txt

Preview (first 2KB):
=== PHD narm ===
2958:hunaromand [hwnl'wmnd IN hunarmand] = hunarawand.
3671:narm [nlm I M nrm, N --] meek, humble, soft.
4564:sOftsta [swhpst) hi] sophist.
6810:hole may, siirdg, siirax.                      humble erman(ag), ertan, narm.
7041:  edonih.                                  meek narm; v. humble.
7610:-sized -masiiy.                               soft narm.
=== NYB narm/nezak ===
305:subst. the pious, righteous man 651%, 732.24; pl. cas. obl. ~-dn: ~-dn marian zanān 53%; ~-dn alone 634, 7322, 8835, 10121, — 3. blessed, of those in Paradise 8624; subst. pl. cas. obl. ~-dn the blessed 87%, — Borrowed from Av. (246 sqq.) ašāvan-, nom. ašavā; MPrthPrs (Zoro- astrian term) ’hlw, pl. ’hlw’n (A-H II); as to the correspondence -š-: -hl- v.s.v. Mahlāh; Paz. ašē, pl. ašēg. V. ahlav-dät, ahlài, ahlayéh. The genuine WIr form is OP artdvan ‘blessed’, whence MPrth ?rd^w ‘righteous, veracious’, also borrowed in MPrs (A-H II); v. further artäk.
427:as befits a man in his relations with his ruler or superior (cf 689-?. 70%). — Approx- imately ‘no gentleman’, with which the gl. a"ürtar ‘most contemptible, most wretched’ (v.s.v. 2a¥dr) best seems to tally. Av. (1042) namra.včaš FrO Ille with the gl. āzāt gobišn ‘whose speech is noble, is that of a nobleman’ (read "e*t! = āzāt, not ’pt' = dapat as Bthl and Reichelt have it), which seems to allude to the behaviour of a nobleman before his sovereign. Skr namrd- ‘bowing, humb- le, obedient’; MPrth nmr ‘humble, cle- ment’, abstr. nmryft (A-H IIT); SW with metathesis narm (g. v.), MPrs nrm ‘soft’ and ‘humble’ (A-H II). My former read- ing hwmltwm = *humartöm is, at all events, impossible.
740:Aškānān [’Sk’n’n'] patron. of the pre- ceding name 10815. 11415-26, — NP Aška- niyan; Arab. al-xaskäniya (read -x- in- stead of -h-) and al-asgäniya, Fihrist 32'730.31,
876:a-zén ['zyn'] unarmed, (war) conducted without arms 121%, — V. zen.
...
</persisted-output>
```


## [2026-09-07T17:42:53.153Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF page 336 ===\"; grep -n \"\\[pdf page\" FSF_pages.txt | head -3\nawk '/\\[pdf page/{p=$0} /نیزه/{print NR\": \"p}' FSF_pages.txt | head -20"
}
```


### [2026-09-07T17:42:54.413Z] TOOL RESULT

```
=== FSF page 336 ===
1627: 
1645: 
2244: 
2256: 
2297: 
2408: 
2531: 
3285: 
3296: 
3882: 
4392: 
4394: 
7734: 
7774: 
7831: 
8031: 
8951: 
10312: 
10465: 
10541:
```


## [2026-09-07T17:43:05.039Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD ned ===\"; grep -n \"ned-\" AHD_watkins1985.txt | head -8\necho \"=== AHD nem ===\"; grep -n \"^nem-\\|nem-\\. \" AHD_watkins1985.txt | head -8\necho \"=== SYN thread ===\"; grep -n -i \"thread\" SYN.txt | head -8"
}
```


### [2026-09-07T17:43:05.105Z] TOOL RESULT

```
=== AHD ned ===
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
218:lengthened-grade form. A form with lengthened vocalism.
219:ghers-. 2. Lengthened-grade form
293:aryo-. Lord, ruler; self-designation of the Indo-Iranians and perhaps of the Indo-Europeans. Lengthened-grade form *dryo- in Sanskrit drya-, noble, Aryan: ARYAN. [Pok. arjo- 67.]
454:ere-2. To separate. Variant *ré-, contracted from *reo-. 1. Suffixed variant form *rd-ro- in Latin rdrus, “having intervals between,” “full of empty spaces,” rare: RARE}, 2. Suffixed zero-grade form *ra-ti- in Latin ratis, raft (< “grating,” “latticework”): RATITE. 3. Suffixed length- ened-grade form *ré-ti- in Latin réte, r��tis, a net: RE- SEAU, RETE, RETIARY, RETICLE, RETICULE, RETINA; RETIFORM. 4. Suffixed form *eré-mo- in Greek erémos, empty, desolate, bereft: EREMITE, HERMIT; EREMURUS. [Pok. 5. er- 332.]
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
=== AHD nem ===
780:nem-. To assign, allot; also to take. 1. Germanic *nem- in: a. Old English niman, to take, seize: NIM, NUMB; (BENUMB); b. Old English n#mel, quick to seize, and numol, quick at learning, seizing: NIMBLE. 2. Greek nemein, to allot: NEMESIS. 3. O-grade form *nom- in: a. Greek nomos, portion, usage, custom, law, division, district: NOME, -NOMY; ANOMIE, ANTINOMIAN, AN- TINOMY, (ASTRONOMER), (ASTRONOMY), AUTONOMOUS, BINOMIAL, DEUTERONOMY, METRONOME, NOMOGRAM, NOMOGRAPH, NUMISMATICS; b. Greek nomé, pasturage, grazing, hence a spreading, a spreading ulcer: NOMA; c. Greek nomas, wandering in search of pasture: NOMAD; d. Greek nomimos, legal, probably borrowed in Latin nummus, coin: NUMMULAR, NUMMULATE. 4, Perhaps suffixed o-grade form *nom-eso- in Latin numerus, num- ber, division: NUMBER; ENUMERATE, SUPERNUMERARY. [Pok. 1. nem- 763.]
=== SYN thread ===
845:1.213 DUST Grk. — xévts Goth. mulda, stubjus Lith. dulkés (pl.) NG oxéyn ON dupt, dust Lett. pisli (pl.), putelklz (pl.) Lat. pulvis Dan. stg ChSl.  prachii It. polvere Sw. stoft SCr. oprah Fr. poussitre OE dist Boh. prach Sp. polvo ME dust Pol. proch Rum. opraf, pulbere NE dust Russ. pyl Ir. luaithred Du. stof Skt.  renu-, pansu-, dhiali- Nir. luaithreadh OHG _ stuppi, stoub (melm) Av. pasnu- W. Ulwch, pylor MHG stoup Br. poulir NHG _ staub
858:3. Tr. luaithred, NIr. luaithreadh (also -rean, etc.) ‘ashes’ and ‘dust’, fr. luaith ‘ashes’ (1.85).
1473:Boh. pramen ‘spring’, also ‘jet, stream, strand’ : ChSl. prament ‘thread’, SCr. pramen ‘tuft of hair’, Pol. promien ‘tay’, fr. *por-men-, deriv. of IE *per- ‘pass through’ (Grk. zepdw, etc.). Develop- ment in Bohemian through ‘thin stream’ to ‘spring’. Briickner 438.
9641:‘vinegar’ go back to expres- "ie Bee ar, acid’, sometimes : with words for ‘wine’. ts (> Rass, ko > Lith uksusas), Jate dim. Baio?) He a ae Grk, sts ‘sharp, pointed, acid’ (cf. elpos threadth’ : epis ‘broad’), Lat. acidus iid’, deer ‘sharp’, etc. Walde-P. 1,28 ff. : NG ydvxad fr. late Grk. yAvxadcor ‘vinegar’ (EM, Choerob.), this fr. -yAuxbs ‘sweet’. 2, Lat. acétum, orig. pass. pple. of acére ‘be sour’, beside acidus ‘sour, acid’ :dcer ‘sharp’, etc. Walde-P. 1.28 ff. Emout-M, 8. Walde-H. 1.6. Hence It. aceto, OF r. aisil, aisin (> Du, azijn); Ir. acét (also fin acét with fin wine); Goth. aket, OF eced, and, with transposition of consonants, LG edik,
9949:Lat. pannus (‘piece of cloth’, esp. ‘rag’), Goth. fana (reg. for péxos), OHG fano (NHG fahne like OE fana, ON fani specialized to ‘banner’) : Grk. rjvn ‘thread on the bobbin, woof’, pl. ‘web’,
10067:They are mostly based on words for ‘point, edge, tooth, peg, notch’, with ob- vious relation to the appearance of the fabric. A few are from words for ‘cord, thread’ or ‘bobbin’, or verbs for ‘fit’ or ‘turn around’.
10072:2. W. ysnoden ‘band, lace’ and ‘lace’ as fabric (like NE lace) : Ir. snath, Br. neud ‘thread’, W. nyddu ‘spin’ (6.31).
10171:Words for ‘spin’ are mostly based on the notions of either ‘turn’ or ‘stretch’, in one group derived from the noun for ‘thread’.
```


## [2026-09-07T17:43:05.195Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 600 FSF_pages.txt; echo; echo \"---\"; grep -n \"pdf page\\|^\\[\" FSF_pages.txt | head -5"
}
```


### [2026-09-07T17:43:05.244Z] TOOL RESULT

```
   ‫‪۵‬اژهنامکت‬
‫فرهوناکژته‌هایدشوارشاهنامه‬
  SAN    ۹ 75035 7-3
          ۱
  ‎‫ا‬
‫و‬۱6۱ 4                 |
‫‪9‬زژهنامت‬
‫‪ 9‬ازه‌نامک‬
‫نامه)‬
    ‫(فرهنگ واژه‌های دششاوهار‬




            ‫تألیف‬

      ‫عبدالحسین نوشین‬




          ‫انتشارات معین‬
                                             ‫نوشین» عبدالحسین؛ ‪۴۸۲۱-۰۵۳٩‬‏‬
 ‫واژه‌نامک (فرهنگ واژه‌ه
---
```


## [2026-09-07T17:43:15.495Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ned-\\. To bind\\|^ned-\\|ned-\\. \" AHD_watkins1985.txt | head\necho \"---\"; grep -o \"ned-\\.[^[]*\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -3\necho \"=== FSF entry in refs_online ===\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['FSF'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-07T17:43:16.831Z] TOOL RESULT

```
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
---
ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.]
=== FSF entry in refs_online ===
{
 "title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/20220809_20220809_1444",
 "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"
 ],
 "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking",
 "covers_etymology": false,
 "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."
}
```


## [2026-09-07T17:43:24.135Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7825,7840p' FSF_pages.txt; echo \"=== 2240 ===\"; sed -n '2238,2260p' FSF_pages.txt"
}
```


### [2026-09-07T17:43:24.193Z] TOOL RESULT

```
                    ‫(رودکی ‪ -‬نفیسی ‪:)۶۸۳‬‬           ‫(‪)۸۸۷-۰۱۲۴۲‬‬
                                                  ‫‪1۵۸‬‬                                           ‫پیخاره‬



                                          ‫پیکان‬                      ‫خسرو بترخت پیشگاه نشسته‬
                 ‫نوک آهنین و تیز نیزه و تیر‪:‬‬             ‫شاه ملوک جهان‪ .‬امیر خراسان‬

               ‫کمان کیانی گرفتن به چنگ‬                                          ‫(اسدی ‪:)۵۵۲-۵‬‬
 ‫بهپیکان پولاد و تیر خدنگ‬                                           ‫گزوهر یکی تخت در پیشگاه‬
‫(‪4٩۹۲۲-۱۹۶-۱‬‬                                            ‫بتی بروی از زر و پیکر چوماه‬
                                           ‫پیکر‬         ‫و در این بیت از دبیاچة داستان بیژن و‬
                                                                                                ‫‪۶‬‬
‫‪-۱‬نقش و نگاری کهبرای زینت و ارایش‬
                                                            ‫منیژه پیشگاه کنایهاز سپهرآوسمان است‪:‬‬
                                        ‫باشد‪:‬‬
=== 2240 ===
                                                           ‫هآننا‬
                                                               ‫وتوز‬
                                                                  ‫گخم‬
                                                                    ‫کهت‬
          ‫نشانی نهادند بر اسپریس‬                    ‫رتم‪۲۴۲۱‬‬
                                                                                        ‫آژدها‬
 ‫سیاوش نکر د ایچ بکاس‌مکیس‬                                                   ‫کنایه از نیزه‪:‬‬
 ‫(‪)۳-۹۸-۸۶۳۱‬‬
                ‫=یستادن‬
                      ‫استادن (بهکسر اول) ا‬
                                                   ‫یکی باره زیر اژدهایی به کف‬
               ‫ایستادگی و پایداریکردن‪:‬‬              ‫(‪)۶۲۵۸۱‬‬
 ‫در شاهنامه‬      ‫یتقی‬
                    ‫ق بی‬
                       ‫دار‬
                         ‫از هز‬
                                                              ‫و در چند بیت سپس‌تر گوید‪:‬‬
                ‫(‪۶۲۱۹-۱۷۳‬و ‪۳۰۱-۱۵۵6‬‬
       ‫نه استد کس آن پهلوان شاه را‬                            ‫بزد نیزهگشتاسپ بر جوشنش‬
                                                    ‫بخست آن زمان کارزاری تنش‬
‫ستوه آورد شاه خرگاه را‬
                                                                            ‫اول)‬    ‫ر‬
                                                                                    ‫سبه‬
```


## [2026-09-07T17:43:32.753Z] TOOL CALL #59: WebSearch

```json
{
 "query": "ریشه‌شناسی واژه «نخ» فارسی حسن‌دوست نخ ریسمان اتیمولوژی"
}
```


### [2026-09-07T17:43:43.533Z] TOOL RESULT

```
Web search results for query: "ریشه‌شناسی واژه «نخ» فارسی حسن‌دوست نخ ریسمان اتیمولوژی"

Links: [{"title":"نخ - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%86%D8%AE/"},{"title":"فرهنگ ریشه‌شناسی فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"معنی نخ | لغت‌نامه دهخدا","url":"https://www.vajehyab.com/dehkhoda/نخ"},{"title":"نخ به انگلیسی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatoen/%D9%86%D8%AE/"},{"title":"خرید کتاب فرهنگ ریشه شناختی زبان فارسی اثر محمد حسن دوست از نشر فرهنگستان زبان و ادب فارسی","url":"https://www.adinehbook.com/product/9647531281/%DA%A9%D8%AA%D8%A7%D8%A8-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%A7%D8%AB%D8%B1-%D8%A8%D9%87%D9%85%D9%86-%D8%B3%D8%B1%DA%A9%D8%A7%D8%B1%D8%A7%D8%AA%DB%8C-%D9%86%D8%B4%D8%B1-%D9%81%D8%B1%D9%87%D9%86%DA%AF%D8%B3%D8%AA%D8%A7%D9%86-%D8%B2%D8%A8%D8%A7%D9%86-%D9%88-%D8%A7%D8%AF%D8%A8-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"کتاب ریشه شناسی زبان فارسی - اتیمولوژی - etymology منابع زبانشناسی - عصر زبان","url":"https://asrezaban.com/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B1%DB%8C%D8%B4%D9%87-%D8%B4%D9%86%D8%A7%D8%B3%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C/"},{"title":"نخ - مانترَه","url":"https://mantrah.smsvtt.com/words/%D9%86%D8%AE"},{"title":"معنی نخ - لغت‌نامه دهخدا","url":"https://lamtakam.com/dictionaries/dehkhoda/468281/%D9%86%D8%AE"}]

بر اساس نتایج جستجو، اطلاعات مربوط به ریشه‌شناسی واژه «نخ» در فارسی موارد زیر را نشان می‌دهد:

## تعریف و معانی

«نخ» رشته‌ای از پنبه و ابریشم است که الفاظ دیگرش تار و ریسمان است.

## آثار حسن‌دوست

فرهنگ ریشه‌شناختی زبان فارسی به کوششِ محمد حسن‌دوست و سرپرستیِ دکتر بهمن سرکاراتی توسط فرهنگستانِ زبان و ادبِ فارسی در سال ۱۳۸۴ چاپ رسید، و سرانجام به نویسندگی محمد حسن‌دوست به‌صورت پنج دفتر از «آ» تا «ی» در بهار ۱۳۹۴ چاپ شد.

## ریشه‌شناسی واژه

در مورد منشأ واژه «نخ»، «ناره» (ریسمان کلفت) پارسی و «نائی» (نخ) گورانی و nus (نخ) آلبانیایی هم از یک ریشه برخاسته و حدس زده می‌شود که «نخ» نیز از همین ریشه مشتق شده باشد. این ریشه در زبان‌های اروپایی در واژگانی مانند naaien (دوختن) هلندی، nähen (دوختن) آلمانی و نیز در سانسکریت (सनायति: بافتن) نمونه دارد.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T17:43:56.615Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW nassa ===\"; grep -n \"nassa\\|naxae\" LEW_1910.txt | head -10\necho \"=== LAT nassa ===\"; grep -n \"nassa\\|naxae\" LAT.txt | head -10\necho \"=== KLN nassa ===\"; grep -n -i \"nassa\\b\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T17:43:56.797Z] TOOL RESULT

```
=== LEW nassa ===
=== LAT nassa ===
40464:tenant k la langue des p£cheurs oh iis ddsignent le "frai" et lenassa
40468:nassa, -ae f. (naxa): nasse; — est piscatorii uasi genus, quo cum
40479:quattuor "un vase a quatre bees". Toutefois un rapport avec nassa
40953:lisme que iri. nascim', cf. v.h. a. nusca "agrafe". Cf. lat. nassa ?
=== KLN nassa ===
5318:bonanza,  n.,  a  rich  vein  of  ore;  hence,  colloq.,  a source  of  wealth.  —  Sp.,  lit.  ‘fair  weather,  pros¬ perity’,  fr.  VL.  *bonacia  (whence  also  It.  bo- naccia,  OProveng.  bonassa,  F.  bonace,  ‘fair weather  at  sea’),  alteration  of  L.  malacia,  ‘calm at  sea’,  which  derives  fr.  Gk.  paXaxta,  ‘soft¬ ness’,  but  was  mistaken  for  a  derivative  of  L. malus,  ‘bad’,  and  accordingly  changed  into *bonacia,  fr.  L.  bonus,  ‘good’  (see  bonus), bonbon,  n.,  sweetmeat.  —  F.,  reduplication  of bon,  ‘good’,  fr.  L.  bonus,  ‘good’.  See  bonus  and cp.  bonny.
25302:Nestorian,  n.,  a  believer  in  Nestorianism;  a  mem¬ ber  of  the  Nestorian  Church.  —  See  prec.  word, net,  n.  —  ME.  net(t),  fr.  OE.  net(t),  rel.  to  OS. net(ti),  ON.,  Norw.,  Dan.  Du.  net,  Swed.  ndt, MLG.,  MDu.  net(te),  OHG.  nezzi,  MHG.  netze, G.  Netz,  Goth,  nali,  ‘net’,  fr.  Teut.  base  *natja, lit.  ‘something  knotted’,  and  cogn.  with  OI. nahyati ,  ‘binds,  ties’,  L.  nassa  (prob.  for  nad- sa),  ‘a  basket  for  catching  fish’,  nodus,  ‘knot’, Olr.  nascim,  ‘I  bind,  oblige’,  for-naidm,  ‘a  bind¬ ing'  ;  cogn.  also  with  L.  nectere,  ‘to  bind’  (which is  a  relatively  new  word,  formed  on  analogy  of pectere,  ‘to  comb').  All  the  above  words  derive fr.  l.-E.  base  *ned-,  ‘to  twist,  to  knot’,  an  en¬ larged  form  of  base  *(s)ne-,  w  hence  L.  neb,  nere , ‘to  bind’.  See  needle  and  cp.  nettle.  Cp.  also nexus,  annex,  connect,  node,  noose,  ouch. Derivatives:  net,  tr.  and  intr.  v.,  nett-ed,  adj., nett-er,  n.,  nett-ing,  n.
25518:node,  n.,  a  knot,  knob.  —  L.  nodus,  ‘knot’,  rel.  to L.  nassa  (prob.  for  *nad-sa),  ‘a  basket  for  catch¬ ing  fish’,  and  cogn.  with  ON.  not,  ‘a  large  net’, ON.,  OE.  net,  ‘net’.  See  net  and  cp.  nodus,  noose, denouement,  crunode,  intemode. nodical,  adj.,  pertaining  to  the  nodes  (astron)  — See  node  and  -ical.
```


## [2026-09-07T17:44:11.757Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%86%D8%AE\" \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%86\" \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%B2%D9%87\" \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%82%D8%A9\" \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%82\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 348 verification: Persian nax / nan / neyze / Arabic numruqa-namraq etymology\" 2>&1 | tail -2; done"
}
```


### [2026-09-07T17:44:15.444Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/dad4c080b9ba4e99.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/079ae929a568e9d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/055e1b79a6eda9ad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ce2b77097af3a1ab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f230f79f1a7eaba0.txt
```


## [2026-09-07T17:44:18.881Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== neyze ===\"; grep -n -A4 -i \"etymology\" 055e1b79a6eda9ad.txt | head -40"
}
```


### [2026-09-07T17:44:18.960Z] TOOL RESULT

```
=== neyze ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
154: Etymology
155- [ edit ] 
156-
157- From Middle Persian 𐭭𐭩𐭰𐭪𐭩 ( nycky ) / nyck' ( /⁠nēzag⁠/ ) , from Old Persian *naizakam , borrowed from Old Median *naizakam , from Proto-Iranian *náyjakam , derived from Proto-Iranian *náyjam , from Proto-Indo-Iranian *náyȷ́žʰam . Compare Avestan 𐬥𐬀𐬉𐬰𐬀 ( naēza , “ tip, especially of a needle ” ) and borrowings from Iranian: Classical Syriac ܢܝܙܟܐ ( nayzkāʾ ) , Old Armenian նիզակ ( nizak ) , and Arabic نَيْزَك ( nayzak ) .
158-
```


## [2026-09-07T17:44:24.539Z] TOOL CALL #63: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T17:44:24.577Z] TOOL RESULT

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


## [2026-09-07T17:44:27.132Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T17:44:27.169Z] TOOL RESULT

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


## [2026-09-07T17:47:43.012Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk348.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_NAX  = \"https://en.wiktionary.org/wiki/%D9%86%D8%AE\"\nW_NAN  = \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%86\"\nW_NEZ  = \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%B2%D9%87\"\nW_NMQA = \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%82%D8%A9\"\nW_NMQ  = \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%82\"\n\ndoc = {\n \"pdf_page\": 348,\n \"book_page\": 318,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": []\n}\n\n# ---------------- entry 0 : Naeza ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Naěza\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Avestan naēza- n. 'point, tip (esp. of a needle)' (Bartholomae, AiW col. 1037; Yt 14.33)\",\n \"note\": \"The root box is right in every particular. Bartholomae, Altiranisches Wörterbuch col. 1037 has '¹naēza- n. \\\"Spitze\\\", spez. der Nadel' with the single attestation Yt 14.33, and adds of his own accord 'np. vgl. nēza \\\"Speer\\\"'. Nourai's transliteration Naěza is his usual rendering of naēza-. The one refinement modern work adds: New Persian نیزه does not descend from the Avestan word itself but from its Old West-Iranian sister form *naiza-ka- (Wiktionary: MP nēzag < OP/Median *naizakam < Proto-Iranian *náyjakam), Avestan naēza- being the cognate that guarantees the base *naiza-.\",\n \"note_fa\": \"ریشهٔ اوستایی naēza- «نوک، سرِ تیز (به‌ویژه نوکِ سوزن)» واژه‌ای است واقعی که بارتولمه در «واژه‌نامهٔ ایرانی باستان» ستون ۱۰۳۷ با تنها شاهدِ یشت ۱۴٫۳۳ آورده و خود او نیز فارسی نو «نیزه» را با آن سنجیده است. برچسبِ زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ تکمیلی آنکه «نیزه» مستقیماً از صورت اوستایی نیامده، بلکه از صورت خواهرِ ایرانیِ باختری *naiza-ka- گرفته شده و naēza- اوستایی هم‌ریشهٔ آن است. ادعای نورایی درست است.\",\n \"sources\": [W_NEZ],\n \"ref_check\": [\n   {\"ref\": \"BQT:2226\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' p. 2226 (rendered with tools/ref_page.py BQT:2226 = BQT_v4 pdf p. 309), Mo'in's footnote 5 to نیزه: «پهلوی nēzak (نیزه)، معرب آن nayzak. ارمنی nizak، از اوستا naēza (نوک سوزن) «بارتولمه ۱۰۳۷»» — the root, the gloss and the Bartholomae column all as Nourai has them.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1037 s.v. ¹naēza-\", \"stance\": \"supports\",\n    \"note\": \"grep 'naeza' in BRT.txt line 18504: '• j. ¹naeza- n. \\\"Spitze\\\", spez. der Nadel: … Yt 14. 33' followed by 'np. vgl. nēza \\\"Speer\\\"'.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 59 s.v. nēzag\", \"stance\": \"supports\",\n    \"note\": \"MacKenzie: 'nezag [nyck | N neza] lance' (PHD_mackenzie.txt line 3717) — the Middle Persian continuant of the same base.\"},\n   {\"src\": \"HRN\", \"where\": \"nos. 1020-1031, pp. 229-231\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss has no entry for nēza/nēze between nāf (1020) and nezend (1031); the word is treated by Hübschmann (KZ) instead, as Bartholomae notes.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"nězak\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old Iranian *naiza-ka- (the -ka- diminutive/instrument suffix on *naiza- 'point' = Av. naēza-) gives Middle Persian nēzag, written Book-Pahlavi <nyck'>, 'lance, spear'; the Manichaean/Book-Pahlavi -g and the older -k of the Aramaeogram-based transcription are the same morpheme, so Nourai's 'nězak' and MacKenzie's 'nēzag' are one word. The Avestan diphthong ai/aē is monophthongised to Middle Persian ē (as in Av. daēza- > MP dēz), and the semantic step is 'sharp point (of a needle)' > 'the pointed weapon itself, lance'. The form was current enough in Sasanian times to be taken over as Syriac nayzkā, Armenian nizak and Arabic nayzak.\",\n \"derivation_fa\": \"فارسی میانه nēzag (به خط پهلوی nyck') «نیزه، رمح» از ایرانی باستانِ *naiza-ka-، یعنی ستاکِ *naiza- «نوک» (همان naēza- اوستایی) با پسوندِ -ka-. دوگانه‌واکِ ai/aē ایرانی باستان در فارسی میانه به ē کشیده بدل شده (مانند daēza- اوستایی > dēz پهلوی) و معنا از «نوکِ تیز» به «سلاحِ نوک‌تیز» تحول یافته است. صورتِ پهلوی چنان رایج بوده که به سریانی nayzkā، ارمنی nizak و عربی نَیزَک وام داده شده است. نگارشِ nězak نزد نورایی و nēzag نزد مکنزی یک واژه‌اند. ادعای نورایی درست است.\",\n \"sources\": [W_NEZ],\n \"ref_check\": [\n   {\"ref\": \"MON:4884\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi, s.v. نیزه (MON_part2.txt line 81905): «نیزه. (قد. nēzak) [= نیزک] (ا.) چوب یا نی‌ی دراز که بر سر آن آهنی نوک تیز تعبیه کرده باشند … رمح» — Mo'in explicitly gives the older (Pahlavi) form nēzak, which is Nourai's node. The page number itself could not be re-checked: the local MON OCR carries no page markers.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 59 s.v. nēzag\", \"stance\": \"supports\",\n    \"note\": \"'nezag [nyck | N neza] lance' (PHD_mackenzie.txt line 3717); the English-Pahlavi half has 'lance nēzag' (PHD.txt line 2557).\"},\n   {\"src\": \"SDQ\", \"where\": \"pp. 73-74, §13\", \"stance\": \"supports\",\n    \"note\": \"Siddiqi, Studien über die persischen Fremdwörter, in the section on Persian k rendered by Arabic k: 'نيزه nezā, mp. nezag (< nezak)' beside Arabic نيزك (SDQ.txt line 926, under the running head '— 73 —').\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary (Manual of Pahlavi II)\", \"stance\": \"silent\",\n    \"note\": \"grep 'nēzak/nezag' in NYB_vol2_glossary.txt returns nothing: the word does not occur in Nyberg's Kārnāmag/Mēnōg texts.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"nayzeh «نیزه»\", \"verdict\": \"confirmed\",\n \"derivation\": \"MP nēzag > New Persian نیزه nēza/nayza 'spear, lance', with the regular Middle-Persian final -ag > New Persian -a (> modern -e) that also gives bandag > banda, xānag > xāna; the classical reading is nēza, the modern Tehrani neyze. The extended sense 'flag-pole' is secondary and purely Persian — a banner (درفش، علم) was tied to a spear shaft, so Ferdowsi can speak of نیزهٔ علم; Borhan-e Qate' lists exactly this second meaning ('چوب یا نی‌ی که برای علم و رایت به کار رود'), as does Mo'in. The chart's variant script نیژه is the same word with the dialectal/orthographic ž for z familiar from نیزه/نیژه in the older lexica. Arabic borrowed the Middle Persian form, not this one: نَيْزَك nayzak 'short lance' (later also 'meteor'), a loan that Siddiqi and Asbaghi both list.\",\n \"derivation_fa\": \"«نیزه» از فارسی میانهٔ nēzag، با تحولِ قاعده‌مندِ پایانهٔ -ag فارسی میانه به -a/-e فارسی نو (همچون bandag > بنده، xānag > خانه). خوانشِ کهنِ آن nēza و تلفظِ امروزی neyze است. معنای دومِ «چوبِ درفش» تحولی درون‌فارسی است، زیرا علم و رایت را بر چوبِ نیزه می‌بستند؛ برهان قاطع همین معنا را جداگانه آورده است. صورتِ نگارشیِ «نیژه» همان واژه است با ابدالِ ز/ژ که در فرهنگ‌های کهن دیده می‌شود. عربی صورتِ فارسی میانه را وام گرفته است: «نَیزَک» که صدیقی و اصباغی هر دو آن را در فهرستِ وام‌واژه‌های فارسی آورده‌اند. ادعای نورایی درست است.\",\n \"sources\": [W_NEZ],\n \"ref_check\": [\n   {\"ref\": \"BQT:2226\", \"status\": \"supports\",\n    \"note\": \"The Borhan entry نیزه itself is on this page ('چوب یا نی‌ی دراز … و چوب یا نی‌ی که برای علم و رایت به کار رود'), with Mo'in's footnote 5 deriving it from پهلوی nēzak < اوستا naēza (page rendered with tools/ref_page.py BQT:2226).\"},\n   {\"ref\": \"PLA:265\", \"status\": \"supports\",\n    \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, p. 265 (running head 'nūfar 265' at PLA_pages.txt line 14831): 'naizak: \\\"kurze Lanze\\\" < pers. نيزه naize < mp. nēzak < aw. naēza; ar. Lw. naizak, aram. …' — the whole chain as Nourai draws it.\"},\n   {\"ref\": \"SDQ:73\", \"status\": \"supports\",\n    \"note\": \"Siddiqi p. 73/74 §13 lists 'نيزك = np. نيزه nezā, mp. nezag (< nezak)' among Persian words whose k is kept in Arabic (SDQ.txt line 926).\"},\n   {\"ref\": \"FSF:336\", \"status\": \"not_checked\",\n    \"note\": \"Noushin's Vāzhe-nāmak is on disk (FSF_pages.txt) and does discuss نیزه in several Shahnameh contexts, but the OCR carries no printed page numbers, so p. 336 of Nourai's printing could not be located; the book is a Shahnameh glossary and carries no etymology (refs_online: covers_etymology false).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. نیزه\", \"stance\": \"supports\",\n    \"note\": \"«نیزه. (قد. nēzak) … رمح. چوب یا نی‌ی که برای علم و رایت به کار رود» (MON_part2.txt line 81905) — both of Nourai's glosses, 'spear' and 'flag post'.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 1037\", \"stance\": \"supports\",\n    \"note\": \"Bartholomae himself appends 'np. vgl. nēza \\\"Speer\\\"' to Avestan naēza-.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\",\n    \"note\": \"grep 'nēza/neza/naiza' in HUB.txt returns nothing; Hübschmann treated the word in KZ (cited by Bartholomae), not in the Studien.\"}\n ]\n})\ndoc[\"entries\"].append(e0)\n\n# ---------------- entry 1 : Nagan ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Nagan, Nağan\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Old/Proto-Iranian *nagna- (also reconstructed *nagana-) 'bread'; not attested in Old Persian\",\n \"note\": \"The reconstruction is real and is exactly what Hübschmann proposed: Persische Studien p. 101, note to Horn no. 1023, says 'Bal. nagan etc. setzt iran. *nagan voraus. Zur Not liesse sich nān vielleicht aus *nagna- erklären' — i.e. Balochi nagan presupposes an Iranian *nagan and nān can be got from *nagna-. Mo'in repeats it in Borhan p. 2107. Wiktionary's current reconstruction is Proto-Iranian *nagna- ('naked bread', baked without ash, opposed to *nikāna- 'buried bread'), with Sogdian nγn-, Parthian ngn, Balochi nagan, Khotanese nāṃji. The one thing to correct is the LANGUAGE LABEL: no such word is attested in the Old Persian inscriptions (Kent's lexicon has nothing), so 'Old Persian Nagan' should read 'Old Iranian *nagan(a)-'. Note also that Nourai's second headword Nağan (with ğ = γ) is precisely the Parthian/Sogdian naγan, so the doublet in the root box is well founded. Horn himself preferred the rival etymology *ni-kan- '(that which is) buried in the hot ash' (after de Lagarde), which Hübschmann rejects for nān and keeps only for Armenian nkan.\",\n \"note_fa\": \"بازساختِ *nagan-/*nagna- «نان» درست است و همان است که هوبشمان در «مطالعات فارسی» ص ۱۰۱ آورده: «بلوچی nagan و مانندِ آن ایرانیِ *nagan را پیش‌فرض می‌گیرد و نان را در نهایت می‌توان از *nagna- توضیح داد». معین نیز در حاشیهٔ برهان قاطع ص ۲۱۰۷ همین را نقل کرده و افزون بر آن نظرِ نیبرگ را آورده است. ویکی‌واژه امروز *nagna- ایرانی آغازین («نانِ برهنه»، یعنی نانی که در خاکستر پخته نشده، در برابرِ *nikāna- «نانِ به‌خاک‌سپرده») را می‌آورد با هم‌ریشه‌هایی چون سغدی nγn، پارتی ngn، بلوچی nagan. تنها ایرادِ نمودارِ نورایی برچسبِ زبانی است: چنین واژه‌ای در پارسی باستانِ کتیبه‌ای گواهی نشده و باید «ایرانی باستان» خوانده شود؛ صورتِ دومِ او Nağan دقیقاً همان naγan پارتی/سغدی است. بنابراین با احتیاط پذیرفتنی است.\",\n \"sources\": [W_NAN],\n \"ref_check\": [\n   {\"ref\": \"BQT:2107\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' p. 2107 (tools/ref_page.py BQT:2107 = BQT_v4 pdf p. 190), Mo'in's footnote on نان: «نان – پهلوی nān، ارمنی nkanak (نان پخته در خاکستر) … بلوچی nagan و نظایر آن، از ایرانی (باستان) *nagana … رک: اشتقاق – هوبشمان؛ نیبرگ نیز گوید نان (فارسی) مأخوذ از nagna است و ارجاع به هرن و هوبشمان کرده (نیبرگ ص ۱۵۶)». Exactly Nourai's 'Nagan : bread', though Mo'in labels it Old IRANIAN, not Old Persian.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 101, ad Horn no. 1023\", \"stance\": \"supports\",\n    \"note\": \"'Arm. nkan führt zu phl. nikan = np. *nigan, aber nicht zu nān. Bal. nagan etc. setzt iran. *nagan voraus. Zur Noth liesse sich nān vielleicht aus *nagna- erklären.' (HUB.txt lines 3551-3553); repeated at §143b, 'nān \\\"Brot\\\" aus *nagna-?, vgl. bal. nagan etc. (oben p. 101)'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 1023, p. 229\", \"stance\": \"partial\",\n    \"note\": \"'1023. nān \\\"Brot\\\". arm. nkan … bal. nagan, n. nayan \\\"Brot\\\" … phlv.-pāz. nān (PPGl.). Also zu √kan- + ni- ursprünglich \\\"(unter die heisse Asche) Vergrabenes\\\" (zuerst de Lagarde)?' — Horn has the Balochi nagan but prefers the rival *ni-kan- etymology.\"},\n   {\"src\": \"KNT\", \"where\": \"Old Persian lexicon\", \"stance\": \"silent\",\n    \"note\": \"Kent's Old Persian lexicon has no word for 'bread'; the label 'Old Persian' on the root box is therefore not supportable from the inscriptions.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"nân\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old Iranian *nagna- (or *nagana-) loses the intervocalic γ before n and contracts: *naγna- > *naγān > Middle Persian nān 'bread, food' — the same loss Hübschmann sets out in Persische Studien §143b, where nān stands beside Bahrām < Varahrān < Av. vərəθraγna- as an example of Old Persian gn = γn giving Middle Persian n. The Parthian and Sogdian branches keep the γ (Parthian ngn /naγan/, Sogdian nγn-), and Balochi nagan keeps the whole *nagan. In Book Pahlavi the word is normally written with the Aramaeogram LḤMA, with the phonetic spelling n'n beside it.\",\n \"derivation_fa\": \"فارسی میانه nān «نان، خوراک» از ایرانی باستانِ *nagna-/*nagana-: غینِ میان‌واکه پیش از n می‌افتد و واکه‌ها کشیده و ادغام می‌شوند (*naγna- > *naγān > nān). هوبشمان همین تحول را در بندِ ۱۴۳ب «مطالعات فارسی» در کنارِ Bahrām < Varahrān < vərəθraγna- اوستایی نمونه آورده است. شاخه‌های شمالِ غربی و شرقی غین را نگاه داشته‌اند: پارتی ngn (naγan)، سغدی nγn-، و بلوچی nagan تمامِ *nagan را. در پهلویِ کتابی این واژه معمولاً با هزوارشِ LḤMA و گاه به‌صورتِ آوایی n'n نوشته می‌شود. ادعای نورایی درست است.\",\n \"sources\": [W_NAN],\n \"ref_check\": [\n   {\"ref\": \"BQT:2107\", \"status\": \"supports\",\n    \"note\": \"Mo'in's footnote on that page opens 'نان – پهلوی nān' before giving the Old Iranian reconstruction (page rendered with tools/ref_page.py BQT:2107).\"},\n   {\"ref\": \"SNS:223\", \"status\": \"not_found\",\n    \"note\": \"Tavoosi's Shāyast nē-Shāyast glossary is on disk (SNS_pages.txt) but its Persian/Pahlavi OCR is unusable — greps for 'nān' return only scrambled strings — and the file carries no page markers, so p. 223 could not be located.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 58 s.v. nān\", \"stance\": \"supports\",\n    \"note\": \"MacKenzie: 'nan [LḤMA (< A lḥm); n'n | | = M, N --] bread, food' (PHD_mackenzie.txt line 3665) — the gloss 'bread, food' is exactly the node's.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien §143b\", \"stance\": \"supports\",\n    \"note\": \"'b) gn = γn (nach Vokalen): np. Bahrām = phl. Varahrān = zd. vərəθraγna-; nān \\\"Brot\\\" aus *nagna-?, vgl. bal. nagan etc. (oben p. 101)' (HUB.txt line 8925) — the sound law that turns *nagna- into nān.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II\", \"stance\": \"partial\",\n    \"note\": \"Nyberg's grammar section is quoted by Mo'in (BQT 2107) as deriving Persian nān from *nagna- with reference to Horn and Hübschmann; the glossary itself has nān only in running text (e.g. 'pat 10 mart nān-ē ka xvarend sagr hend', NYB_vol2_glossary.txt line 3004).\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"nân «نان»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian nān passes unchanged into New Persian نان nān — a long-ā monosyllable has nothing to lose — and the word is attested from the earliest Dari poetry (the Ferdowsi line quoted on the chart, 'وگر نانش از کوشش خویش بود'). The widening from 'bread' to 'food, sustenance, livelihood' (نان درآوردن, نان کسی را بریدن) is an inner-Persian metonymy of the same kind as Latin panis > 'living'. All the modern Iranian dialects listed by Mo'in on Borhan p. 2107 (Kurdish nān, Zaza, Gilaki, Semnani, Sangesari, Lasgerdi, Shahmirzadi) continue the same form.\",\n \"derivation_fa\": \"«نان» فارسی نو بی هیچ دگرگونیِ آوایی از nān فارسی میانه آمده است؛ تک‌هجایی با آی کشیده چیزی برای از دست دادن ندارد. این واژه از کهن‌ترین شعرِ دری گواهی دارد (همان بیتِ فردوسی که در نمودار آمده). گسترشِ معنایی از «نان» به «خوراک و روزی» (نان درآوردن، نانِ کسی را بریدن) تحولی درون‌فارسی و از گونهٔ مجازِ جزء به کل است. گویش‌هایی که معین در حاشیهٔ برهان ص ۲۱۰۷ برشمرده — کردی، زازا، گیلکی، سمنانی، سنگسری، لاسگردی، شهمیرزادی — همه همین صورت را دارند. ادعای نورایی درست است.\",\n \"sources\": [W_NAN],\n \"ref_check\": [\n   {\"ref\": \"BQT:2107\", \"status\": \"supports\",\n    \"note\": \"The Borhan entry نان and Mo'in's footnote with the dialect list are on this page (tools/ref_page.py BQT:2107).\"},\n   {\"ref\": \"HRN:229\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss no. 1023 (printed p. 229, between the page marks '— 229 —' and '230 —' in HRN.txt): '1023. nān \\\"Brot\\\". arm. nkan … bal. nagan, n. nayan \\\"Brot\\\", nagan-pad \\\"Bäcker\\\" (249); minj. nayan; phlv.-pāz. nān (PPGl.).'\"},\n   {\"ref\": \"HUB:101\", \"status\": \"supports\",\n    \"note\": \"Hübschmann, Persische Studien p. 101 (the page mark '- 101 —' stands immediately before it, HUB.txt line 3551): 'Bal. nagan etc. setzt iran. *nagan voraus. Zur Noth liesse sich nān vielleicht aus *nagna- erklären.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 58 s.v. nān\", \"stance\": \"supports\",\n    \"note\": \"'nan … bread, food' with 'N --' meaning the New Persian form is identical.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. نان\", \"stance\": \"supports\",\n    \"note\": \"Mo'in's lexicon has نان and a long series of compounds (نان‌خورش, نان فطیر …) with the sense 'bread, food' (MON_part2.txt lines 7792, 10039).\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms, ch. 5 'bread'\", \"stance\": \"silent\",\n    \"note\": \"Buck's chapter lists no Persian form; grep in SYN.txt for 'nan/nān' returns only unrelated matches.\"}\n ]\n})\ndoc[\"entries\"].append(e1)\njson.dump(doc, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/part1.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(doc[\"entries\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk348.py"
}
```


### [2026-09-07T17:47:44.467Z] TOOL RESULT

```
ok 2
```


## [2026-09-07T17:51:52.495Z] TOOL CALL #66: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk348b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_NAX  = \"https://en.wiktionary.org/wiki/%D9%86%D8%AE\"\nW_NMQA = \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%82%D8%A9\"\nW_NMQ  = \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%82\"\n\nentries = []\n\n# ---------------- entry 3 : Naks, Nask ----------------\ne3 = {\n \"entry\": 3,\n \"root\": \"Naks, Nask\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *ned- 'to bind, tie' (Pokorny 758-759), with the -sk- extension *ned-sko- that gives OIr. nascim, Av. naska-; there is no independent root *naks-/*nask- in Pokorny, Walde-Pokorny or Watkins\",\n \"note\": \"The root box is a verbatim copy of Mann's lemma: IEC col. 825 has 'naks- (nask-) \\\"twist, twine, torque, tress\\\"', continued in col. 826 with 'Av. naska-, id.; Per. nax \\\"thread\\\"; Gallo-Lat. naxae (\\\"bonds\\\", misspelt \\\"noxae\\\") beside naxa, nassa \\\"bownet\\\"; OIr. nasc …'. So Nourai's reference is accurate. Mann's lemma, however, is his own: the standard handbooks put this material under *ned- 'to bind, tie' (Pokorny 758-759 ned-1, Watkins AHD ned-, Klein s.v. net), where OIr. nascim 'I bind', Latin nassa (< *nad-s-a) and OHG nusca are the -sk-/-st- derivatives, and where Pokorny explicitly adds 'Avestan naska- \\\"anthology (of texts), text collection\\\", probably actually \\\"bundle\\\"'. The connection Nourai draws is therefore not invented, but the root should be *ned- with an s-extension, and the gloss 'twist, twine' belongs to Mann alone.\",\n \"note_fa\": \"این ریشه عیناً از فرهنگ تطبیقی مان (IEC ستون ۸۲۵) گرفته شده است: «naks- (nask-) «تابیدن، رشتن، بافتن»». ارجاعِ نورایی درست است، اما خودِ این ریشه ساختهٔ مان است. فرهنگ‌های معیار — پوکورنی ص ۷۵۸ـ۷۵۹ ذیل *ned- «بستن، گره زدن»، واتکینز در پیوستِ AHD، و کلاین ذیل net — همین مواد را زیرِ ریشهٔ *ned- می‌آورند و صورت‌های nasc ایرلندی کهن، nassa لاتین (< *nad-s-a) و nusca آلمانی علیای کهن را گسترشِ -sk-/-st- آن می‌دانند. پوکورنی خود naska- اوستایی را نیز همان‌جا آورده و آن را «مجموعهٔ متون، و در اصل احتمالاً «بسته، دسته»» معنا کرده است. پس پیوند درست است اما نامِ ریشه و معنای «تابیدن» از آنِ مان است و نه دانشِ امروزی: با احتیاط پذیرفتنی است.\",\n \"sources\": [W_NAX],\n \"ref_check\": [\n   {\"ref\": \"IEC:825\", \"status\": \"supports\",\n    \"note\": \"Mann, An Indo-European Comparative Dictionary, col. 825 (the column number stands on IEC.txt line 11505, immediately above the lemma): 'naks- (nask-) \\\"twist, twine, torque, tress\\\". Cf. nekstos' — the root name and gloss Nourai prints.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"ned-1, pp. 758-759\", \"stance\": \"partial\",\n    \"note\": \"'Root/lemma: ned-1, Meaning: to roll up; to attach, bind … Old Irish nascim \\\"binde, verpflichte\\\" (*ned-sko), naidm … nasc \\\"ring\\\" (compare to -sk-formation Old High German nusca … further Avestan naska- \\\"anthology (of texts), text collection\\\", probably actually \\\"bundle\\\")' — same material, different root name and gloss; no lemma *naks-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ned-\", \"stance\": \"partial\",\n    \"note\": \"'ned-. To bind, tie. … 3. Re-formation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS … [Pok. 1. ned- 758.]' — Watkins likewise has no *naks-.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 328 f. (cited by Pokorny at ned-1)\", \"stance\": \"partial\",\n    \"note\": \"Pokorny's references line for ned-1 reads 'WP. II 328 f., WH. II 144 f., 155 f., 172 f.'; the material is filed there under ned-, not under any *naks-.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. net, node\", \"stance\": \"partial\",\n    \"note\": \"Klein: 'L. nassa (prob. for nad-sa) \\\"a basket for catching fish\\\", nodus \\\"knot\\\", OIr. nascim \\\"I bind\\\" … All the above words derive fr. I.-E. base *ned-, \\\"to twist, to knot\\\", an enlarged form of base *(s)ne-' (KLN_1966.txt line 25302).\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"naska\", \"verdict\": \"plausible\",\n \"derivation\": \"Avestan naska- m. is a real word and does belong here formally: it is *ned-sko- 'that which is bound together', i.e. a bundle — Pokorny (758) lists it under ned-1 next to Old Irish nascim (*ned-sko-) and OHG nusca 'clasp'. But its ATTESTED meaning is not 'thread': naska- is the technical term for a 'nask', one of the twenty-one books/sections into which the Sasanian Avesta was divided, which Pokorny renders 'anthology (of texts), text collection, probably actually \\\"bundle\\\"'. Mann's 'Av. naska-, id.' (i.e. 'twist, twine, tress'), which Nourai turns into 'thread', is a gloss no Avestan dictionary supports; Bartholomae has naska- only as the name of an Avestan text-division. So the arrow root→naska- is defensible, the gloss is not.\",\n \"derivation_fa\": \"واژهٔ اوستایی naska- واقعی است و از نظر ساخت به همین ریشه می‌خورد: *ned-sko- «آنچه به‌هم بسته شده»، یعنی «دسته، بسته». پوکورنی (ص ۷۵۸) آن را در کنارِ nascim ایرلندی کهن و nusca آلمانی کهن ذیلِ *ned- آورده است. اما معنای گواهی‌شدهٔ آن «نخ» نیست: «نَسک» نامِ هر یک از بیست‌ویک بخشِ اوستای ساسانی است و پوکورنی آن را «مجموعهٔ متون، در اصل احتمالاً بسته/دسته» ترجمه کرده است. بارتولمه نیز naska- را تنها به‌عنوانِ نامِ بخشی از اوستا می‌شناسد. بنابراین پیوندِ ریشه‌شناختی پذیرفتنی است، ولی معنایی که نورایی (به پیروی از مان) داده نادرست است: با احتیاط پذیرفتنی، با تصحیحِ معنا.\",\n \"sources\": [W_NAX],\n \"ref_check\": [\n   {\"ref\": \"IEC:825\", \"status\": \"supports\",\n    \"note\": \"The continuation of Mann's lemma in col. 826 (IEC.txt line 11522) opens 'Av. naska-, id.' — 'id.' referring to the col.-825 gloss 'twist, twine, torque, tress'. Mann says what Nourai says; the question is whether Mann is right.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"ned-1, p. 758\", \"stance\": \"partial\",\n    \"note\": \"'… further Avestan naska- \\\"anthology (of texts), text collection\\\", probably actually \\\"bundle\\\"' — same etymology, but the meaning is 'bundle/text collection', not 'thread'.\"},\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch\", \"stance\": \"contradicts\",\n    \"note\": \"Bartholomae knows naska- only as the Avestan book-division (cf. 'Haδōxt Nask' in the list of texts, BRT.txt line 1898); there is no Avestan word naska- 'thread' in the dictionary.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. ned-\", \"stance\": \"silent\",\n    \"note\": \"Watkins's ned- entry lists only the Germanic, Latin and Celtic reflexes; no Avestan form.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"nax\", \"verdict\": \"unverified\",\n \"derivation\": \"No Middle Persian nax 'thread' is attested in any Pahlavi source I can check: MacKenzie's Concise Pahlavi Dictionary has no such headword (its words for thread/rope are rēdag/rīsmān and tār), and Nyberg's glossary has nothing either. Phonologically the step is also not straightforward: Avestan -sk- does not simply reduce to Middle Persian -x-, so naska- would be expected to give MP *nask, not nax. The node therefore rests entirely on Mo'in's note (MON:4683), which I could not locate; treat 'Pahlavi nax' as an assumed intermediate, not an attested word.\",\n \"derivation_fa\": \"هیچ سندی برای صورتِ فارسی میانهٔ nax «نخ» نیافتم: فرهنگ پهلوی مکنزی چنین سرواژه‌ای ندارد (واژه‌های او برای «رشته» rēdag و tār است) و واژه‌نامهٔ نیبرگ نیز خاموش است. از نظر آوایی نیز گذر از -sk- اوستایی به -x- فارسی میانه قاعده‌مند نیست؛ از naska- انتظارِ *nask می‌رود نه nax. بنابراین این گره تنها بر یادداشتِ معین (که نتوانستم بیابم) استوار است و باید آن را صورتی فرضی دانست نه گواهی‌شده: تأیید نشد.\",\n \"sources\": [W_NAX],\n \"ref_check\": [\n   {\"ref\": \"MON:4683\", \"status\": \"not_found\",\n    \"note\": \"The local Mo'in OCR (MON_part1/part2.txt) has no page markers and repeated greps for a نخ headword returned only نخست/نخود/نخاله; the entry and hence the claim of a Pahlavi nax could not be verified.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, letter n\", \"stance\": \"silent\",\n    \"note\": \"grep of PHD_mackenzie.txt for a headword nax and for 'thread' gives only 'rēdag [l(y)ltk'] rope, string, thread' (line 4404) and 'thread rīstag' (line 7767) — no nax.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\",\n    \"note\": \"grep for 'nax' in NYB_vol2_glossary.txt returns nothing relevant.\"},\n   {\"src\": \"IEC\", \"where\": \"col. 826\", \"stance\": \"partial\",\n    \"note\": \"Mann jumps straight from Av. naska- to 'Per. nax \\\"thread\\\"' without any Middle Persian link, so even Nourai's own source does not attest the Pahlavi stage.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"nax «نخ»\", \"verdict\": \"plausible\",\n \"derivation\": \"New Persian نخ nax 'thread, string' is of course real and old (it is itself the source of Arabic نخ 'a coarse rug; silk stuff shot with gold thread', whence the Medieval Latin/Old French terms for that cloth). Its origin, however, is undetermined: Wiktionary's Persian entry marks the etymology as missing, and neither Horn nor Hübschmann has an entry for it. The only source that assigns it an etymology is Nourai's own reference, Mann IEC 826 ('Per. nax \\\"thread\\\"' under naks-/nask-), i.e. from PIE *ned-s-k- 'bind, twist' — attractive semantically ('twisted thing' > 'thread'), but with no attested Iranian intermediate and with the -sk- > -x- step unexplained. Accepted by one scholar, not established.\",\n \"derivation_fa\": \"«نخ» واژه‌ای است اصیل و کهن در فارسی؛ خودِ عربی «نخ» (نوعی زیلو و پارچهٔ ابریشمینِ زردوز) از فارسی وام گرفته شده است. اما ریشهٔ آن روشن نیست: ویکی‌واژه بخشِ ریشه‌شناسیِ آن را ناتمام گذاشته و نه هرن و نه هوبشمان مدخلی برای آن ندارند. تنها منبعی که برای آن ریشه‌ای قائل شده همان مأخذِ خودِ نورایی است، یعنی مان (IEC ستون ۸۲۶) که آن را ذیلِ *naks-/*nask- «تابیدن» می‌آورد؛ یعنی از *ned-s-k- هندواروپایی «بستن، تابیدن». از نظر معنایی («تابیده» > «نخ») پذیرفتنی است اما هیچ حلقهٔ میانیِ ایرانی ندارد و تبدیلِ -sk- به -x- توضیح داده نشده است: با احتیاط پذیرفتنی است.\",\n \"sources\": [W_NAX],\n \"ref_check\": [\n   {\"ref\": \"IEC:825\", \"status\": \"supports\",\n    \"note\": \"'Per. nax \\\"thread\\\"' stands in Mann's lemma naks- (nask-), col. 826, the continuation of the col.-825 headword (IEC.txt line 11522).\"},\n   {\"ref\": \"MON:4683\", \"status\": \"not_found\",\n    \"note\": \"Same problem as node #2: the local Mo'in OCR is unpaginated and the نخ headword could not be located.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss, letter n\", \"stance\": \"silent\",\n    \"note\": \"Horn has no entry for نخ; nos. 1020-1033 run nāf, nāk, nāgāh, nām, nān, nāv, neberd, ner, nirx, nezd …\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\",\n    \"note\": \"grep for 'nax' in HUB.txt yields only naxudā (< *nāv-xudā, p. 101 note to Horn 1024), not نخ 'thread'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi\", \"stance\": \"silent\",\n    \"note\": \"grep of ARY_pages.txt for a نخ headword returns nothing; Aryanpur does not treat the word.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"naxae\", \"verdict\": \"plausible\",\n \"derivation\": \"Copied from Mann, who writes 'Gallo-Lat. naxae (\\\"bonds\\\", misspelt \\\"noxae\\\") beside naxa, nassa \\\"bownet\\\"' — i.e. naxae is a form Mann restores in a Gallo-Latin glossary where the manuscripts have noxae. The well-attested Latin word is nassa (variant naxa) 'wicker fish-trap, weel', which Ernout-Meillet register as 'nassa, -ae f. (naxa): nasse … est piscatorii uasi genus', and which Pokorny and Klein derive from *nad-s-a, the s-formation of *ned- 'to bind' — so the connection to the root is sound. But 'naxae = bonds' is an emendation of Mann's own, not a standard Latin lemma, and Nourai reproduces it without the caveat.\",\n \"derivation_fa\": \"این گره نیز از مان گرفته شده است: «لاتینِ گالی naxae («بندها»، که به غلط noxae نوشته شده) در کنارِ naxa و nassa «تلهٔ ماهی»». یعنی naxae صورتی است که مان در واژه‌نامه‌ای گالی‌ـ‌لاتین بازسازی کرده، در حالی که دست‌نوشته‌ها noxae دارند. واژهٔ لاتینِ گواهی‌شده nassa (با گونهٔ naxa) «تلهٔ حصیریِ ماهی» است که ارنو و مه‌یه آن را چنین آورده‌اند و پوکورنی و کلاین آن را از *nad-s-a، ساختِ سینِ ریشهٔ *ned- «بستن»، می‌دانند. پس پیوند با ریشه درست است، اما «naxae به معنی بندها» تصحیحِ شخصیِ مان است و نه مدخلی معیار در لاتین: با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"IEC:825\", \"status\": \"supports\",\n    \"note\": \"IEC.txt line 11522 (col. 826): 'Gallo-Lat. naxae (\\\"bonds\\\", misspelt \\\"noxae\\\") beside naxa, nassa \\\"bownet\\\"' — Nourai's node verbatim, including the gloss 'bonds'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. nassa\", \"stance\": \"partial\",\n    \"note\": \"'nassa, -ae f. (naxa): nasse; — est piscatorii uasi genus, quo cum …' (LAT.txt line 40468) — the variant naxa is real, but the meaning is 'fish-trap', not 'bonds'; a few lines later Ernout-Meillet compare 'irl. nascim, cf. v.h.a. nusca. Cf. lat. nassa?'\"},\n   {\"src\": \"POK\", \"where\": \"ned-1, p. 758\", \"stance\": \"partial\",\n    \"note\": \"'Latin presumably nassa (*nad-s-a) \\\"basket for catching fish; a trap, snare\\\"' — the Latin word belongs to the root, under the name ned-.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. net\", \"stance\": \"partial\",\n    \"note\": \"'L. nassa (prob. for nad-sa), \\\"a basket for catching fish\\\" … All the above words derive fr. I.-E. base *ned-' (KLN_1966.txt line 25302).\"}\n ]\n})\nentries.append(e3)\n\n# ---------------- entry 4 : Namra ----------------\ne4 = {\n \"entry\": 4,\n \"root\": \"Namra\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Sanskrit namrá- 'bowing, bent, humble, yielding' (from √nam- 'to bend', PIE *nem- 'to bend', Pokorny 764); Avestan *naṃra- is reconstructed, attested only in the compound namra.vāxš\",\n \"note\": \"The Sanskrit half of the label is impeccable: namrá- is a normal -ra- adjective of √nam- 'to bend' (PIE *nem-, Pokorny 764 nem-2 'to bend', with Av. nam- 'bends', namah- 'bowing, veneration'). The Avestan half needs an asterisk: Bartholomae's dictionary has no simplex namra-, only '*naṃra-vak-' at col. 1042, and Horn — Nourai's own reference — writes 'aw. namra.vāxš (?)' with a question mark. The gloss 'soft' is likewise the Iranian development ('bending, yielding' > 'soft, gentle'); the Indic sense is 'bowing, humble'. So: right root, right family, but the Avestan simplex is a reconstruction and the gloss is the daughter-language meaning.\",\n \"note_fa\": \"بخشِ سنسکریتِ برچسب کاملاً درست است: namrá- صفتی است با پسوندِ -ra- از ریشهٔ √nam- «خم شدن»، همان *nem- هندواروپایی آغازین (پوکورنی ص ۷۶۴) که nam- و namah- اوستایی نیز از آن است. اما بخشِ اوستایی نیازمندِ ستاره است: بارتولمه صورتِ سادهٔ namra- را ندارد و تنها ترکیبِ *naṃra-vak- را در ستون ۱۰۴۲ آورده، و هرن — که خودِ مأخذِ نورایی است — «اوستایی namra.vāxš» را با علامتِ پرسش نوشته است. معنای «نرم» نیز تحولِ ایرانیِ معناست («خم‌شونده، رام» > «نرم، ملایم»)، حال آنکه معنای هندی «فروتن، خمیده» است. پس ریشه و خانواده درست است ولی صورتِ سادهٔ اوستایی بازسازی است: با احتیاط پذیرفتنی است.\",\n \"sources\": [W_NMQA],\n \"ref_check\": [\n   {\"ref\": \"HRN:230\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss no. 1028 (printed p. 230, between the marks '— 229 —' and '230 —'/'1025' in HRN.txt line 8850 ff.): '1028. nerm \\\"weich, sanft\\\", nermī, ai. namrá- \\\"sich biegend, unterwürfig, ehrfurchtsvoll ergeben\\\"; aw. namra.vāxš (?); phlv. narm \\\"weich, sanft\\\". LW. kurd. nerm, zaza nemr …' — the root, the two source languages and the gloss are Nourai's, with Horn's own question mark on the Avestan.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"nem-2, p. 764\", \"stance\": \"supports\",\n    \"note\": \"'Root/lemma: nem-2, Meaning: to bend. Material: Old Indic namas- = Avestan nemah- n. \\\"bowing, bending = worship\\\"; Old Indic namati \\\"bows, leans, bends\\\" (Kaus. namayati), Avestan namaiti \\\"bends\\\" … participle Old Indic nata- \\\"bent, curved\\\"' — the verbal root of namrá-.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 1042 s.v. *naṃra-vak-\", \"stance\": \"partial\",\n    \"note\": \"'• *naṃra-vak- Adj. \\\"ehrerbietige Worte sprechend\\\": namra-vāxš F.[3]6. Adj.; np. narm \\\"sanft, weich\\\". — Pü.: āzāt gōwišn' — Bartholomae has the compound only, and himself links New Persian narm to it.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nem-\", \"stance\": \"partial\",\n    \"note\": \"Watkins's nem- is 'to assign, allot; also to take' [Pok. 1. nem- 763]; the 'bend' root (Pok. 2. nem- 764) is not in his appendix, so AHD neither supports nor contradicts.\"},\n   {\"src\": \"BQT\", \"where\": \"p. 2130, Mo'in's footnote to نرم\", \"stance\": \"supports\",\n    \"note\": \"«نرم – بفتح اول، هندی باستان namrá- (مطیع، منقاد)، اوستا namra.vāxš، پهلوی narm (نرم، لطف)، افغانی و بلوچی و وخی narm «اشتقاق ۱۰۲۸»، کردی nerm، زازا nemr» (rendered with tools/ref_page.py BQT:2130) — Mo'in reproduces Horn no. 1028 exactly.\"}\n ],\n \"nodes\": []\n}\n\ne4[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"namr, narm; namrak, narmak\", \"verdict\": \"plausible\",\n \"derivation\": \"Both Middle Iranian shapes are genuine and Nourai is right to print them side by side: Parthian (north-western) keeps the inherited order, nmr /namr/ 'humble, clement' (abstract nmryft), while south-western Middle Persian metathesises the r, nrm /narm/ 'soft; meek, humble'. Nyberg states this explicitly — 'MPrth nmr \\\"humble, clement\\\" … SW with metathesis narm, MPrs nrm \\\"soft\\\" and \\\"humble\\\"' — and MacKenzie's dictionary has 'narm [nlm | M nrm] meek, humble, soft'. The -ak forms are a different matter: NP نرمک narmak 'softish' is well attested, but Pahlavi *namrak is not directly attested; it is inferred (so Jeffery, FVQ 281: 'from some Middle Persian form namr + the suffix -ak') from the Aramaic נמרקא and Arabic نمرق that were borrowed from it. Hence 'plausible' rather than 'confirmed': namr/narm confirmed, namrak reconstructed.\",\n \"derivation_fa\": \"هر دو صورتِ ایرانیِ میانه اصیل‌اند و نورایی به‌درستی آن‌ها را کنارِ هم نهاده است: پارتی (شمالِ غربی) ترتیبِ کهن را نگاه داشته، nmr /namr/ «فروتن، ملایم» (با مصدرِ اسمیِ nmryft)، حال آنکه فارسی میانهٔ جنوبِ غربی دچارِ قلب (metathesis) شده و nrm /narm/ «نرم، رام» داده است. نیبرگ همین را صریح می‌گوید و مکنزی نیز «narm [nlm | M nrm] فروتن، نرم» را آورده است. اما صورتِ -ak دار جداست: «نرمک» فارسی نو گواهی دارد، ولی *namrak پهلوی مستقیماً گواهی نشده و تنها از روی وام‌واژه‌های آرامی נמרקא و عربی «نمرق» بازسازی شده است (جفری، ص ۲۸۱: «از صورتی از فارسی میانه، namr + پسوندِ -ak»). پس namr/narm تأیید می‌شود و namrak بازسازی است: با احتیاط پذیرفتنی است.\",\n \"sources\": [W_NMQA],\n \"ref_check\": [\n   {\"ref\": \"HRN:230\", \"status\": \"partial\",\n    \"note\": \"Horn no. 1028 gives 'phlv. narm \\\"weich, sanft\\\"' — the narm form and the meaning, but neither namr nor the -ak derivatives.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 58 s.v. narm\", \"stance\": \"supports\",\n    \"note\": \"MacKenzie: 'narm [nlm | M nrm, N --] meek, humble, soft' (PHD_mackenzie.txt line 3671) — note the Manichaean spelling nrm.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.v. (a-)narm/anārm\", \"stance\": \"supports\",\n    \"note\": \"'Av. (1042) namra.vāxš FrO IIIe with the gl. āzāt gōbišn \\\"whose speech is noble\\\" … Skr namrá- \\\"bowing, humble, obedient\\\"; MPrth nmr \\\"humble, clement\\\", abstr. nmryft (A-H III); SW with metathesis narm (q.v.), MPrs nrm \\\"soft\\\" and \\\"humble\\\"' (NYB_vol2_glossary.txt line 427) — direct support for Nourai's double form namr / narm.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi pp. 263-264 s.v. namraq\", \"stance\": \"supports\",\n    \"note\": \"'namraq: \\\"Sattelkissen\\\" ir. namr \\\"weich\\\" < *namra, aw. namra > mp. narm, suff. -ak' (PLA_pages.txt line 14744) — Asbaghi posits exactly the namr + -ak formation.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"narm «نرم»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian narm passes unchanged to New Persian نرم narm 'soft, gentle, pliant'; the sense-history is 'bending, yielding' (Skt namrá-) > 'pliant' > 'soft', and the moral sense 'meek' survives in نرم‌خو, نرم‌دل. The chart's extra forms are ordinary Persian derivatives: نرمه narma 'the soft part (of the ear, nose)' with the nominal -a, and نرمک narmak 'softish, gently' with the diminutive/adverbial -ak (whence نرمک‌نرمک 'little by little'). Kurdish nerm, Zaza nemr, Balochi/Wakhi narm continue the same Middle Iranian word rather than being borrowed from Persian.\",\n \"derivation_fa\": \"«نرم» فارسی نو بی دگرگونی از narm فارسی میانه آمده است. تاریخِ معنایی چنین است: «خم‌شونده، رام» (همان namrá- سنسکریت) > «انعطاف‌پذیر» > «نرم»؛ و معنای اخلاقیِ «رام و فروتن» هنوز در «نرم‌خو» و «نرم‌دل» زنده است. صورت‌های افزودهٔ نمودار ساخت‌های عادیِ فارسی‌اند: «نرمه» با پسوندِ اسم‌سازِ -ه (نرمهٔ گوش، نرمهٔ بینی) و «نرمک» با پسوندِ تصغیر/قید‌سازِ -ک (نرمک‌نرمک). کردی nerm، زازا nemr و بلوچی و وخیِ narm نیز دنبالهٔ همان واژهٔ ایرانیِ میانه‌اند نه وام از فارسی. ادعای نورایی درست است.\",\n \"sources\": [W_NMQA],\n \"ref_check\": [\n   {\"ref\": \"BQT:2130\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' p. 2130 (tools/ref_page.py BQT:2130 = BQT_v4 pdf p. 213): the entry نرم with Mo'in's footnote «نرم – بفتح اول، هندی باستان namrá- (مطیع، منقاد)، اوستا namra.vāxš، پهلوی narm (نرم، لطف)، افغانی و بلوچی و وخی narm «اشتقاق ۱۰۲۸»، کردی nerm، زازا nemr «ژابا ص ۶۱۸-۶۱۹»؛ چیزی که به هنگام لمس لطیف و ملایم نماید، ضد سخت» — the whole node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 1028, p. 230\", \"stance\": \"supports\",\n    \"note\": \"'1028. nerm \\\"weich, sanft\\\", nermī … phlv. narm \\\"weich, sanft\\\". LW. kurd. nerm, zaza nemr \\\"weich, sanft\\\"; afγ., bel. (178), waɣ. narm.'\"},\n   {\"src\": \"PHD\", \"where\": \"p. 58 s.v. narm\", \"stance\": \"supports\",\n    \"note\": \"'narm … meek, humble, soft', with 'N --' marking the New Persian form as identical.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. نرم / نرمه / نرمک\", \"stance\": \"supports\",\n    \"note\": \"Mo'in has the headword and the derivatives نرمه and نرمک with the senses the chart gives.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Arabic\", \"words\": \"namraq; namâreq\", \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic نُمْرُق / نِمْرِق / نَمْرَق numruq (also نمرقة numruqa) 'cushion, bolster', broken plural نَمَارِق namāriq, is a Middle Iranian loan, and precisely from the namr + -ak form of the preceding node: 'thing having softness'. Jeffery, The Foreign Vocabulary of the Qur'ān p. 281, sets it out — Lagarde 'pointed out that it is from the Iranian namr meaning soft … Av. namra (Bartholomae, AiW 1042), and Phlv. narm … and from some Middle Persian form namr + the suffix -ak, it passed both into Aram. נמרקא and Ar. نمرق, for which a plu. نمارق was then formed' — so the route ran through Aramaic, before Islam (al-Kindī's Risāla p. 85 already lists it as Persian, and it is common in pre-Islamic poetry for the cushion on a camel's back). It is a Qur'ānic word, Sūra 88:15 وَنَمَارِقُ مَصْفُوفَةٌ, in the description of Paradise. Wiktionary's current entry names the donor precisely: 'From Parthian nmr (namr, \\\"soft\\\") + -k (-ak)'.\",\n \"derivation_fa\": \"عربیِ «نُمْرُق/نِمْرِق» (و «نمرقة») به معنی «متکا، بالش» با جمعِ مکسرِ «نمارق»، وام‌واژه‌ای ایرانیِ میانه است و دقیقاً از همان صورتِ namr + -ak گرهِ پیشین، یعنی «چیزِ دارای نرمی». جفری در «واژه‌های دخیل در قرآن مجید» ص ۲۸۱ می‌نویسد که لاگارد نشان داد این واژه از namr ایرانی به معنی «نرم» است و «از صورتی از فارسی میانه، namr + پسوندِ -ak، هم به آرامی נמרקא و هم به عربی نمرق راه یافت و سپس جمعِ نمارق برای آن ساخته شد». پس مسیرِ وام‌گیری از راهِ آرامی و پیش از اسلام بوده است؛ کِندی در رساله‌اش آن را فارسی خوانده و در شعرِ جاهلی برای بالشِ روی شترْ فراوان به کار رفته است. واژه‌ای قرآنی است: سورهٔ غاشیه، آیهٔ ۱۵ «ونمارقُ مصفوفة». ویکی‌واژه امروز مبدأ را «پارتی nmr «نرم» + -ak» می‌داند. ادعای نورایی درست است.\",\n \"sources\": [W_NMQA, W_NMQ],\n \"ref_check\": [\n   {\"ref\": \"VDQ:403\", \"status\": \"supports\",\n    \"note\": \"VDQ is Badre'i's Persian translation of Jeffery; the noorlib viewer could not be read, so I checked the corresponding entry in the English original, Jeffery FVQ p. 281 s.v. نمارق (FVQ_pages.txt lines 10097 ff.): 'Lagarde, Symmicta i, 60, pointed out that it is from the Iranian namr meaning soft. In the old Iranian we find namra, which gives Av. namra (Bartholomae, AiW 1042 …), and Phlv. narm (West, Glossary 240; Salemann, Manichaeische Studien i, 101), and from some Middle Persian form namr + the suffix ak, it passed both into Aram. נמרקא and Ar. نمرق, for which a plu. نمارق was then formed.' Nourai's arrow is Jeffery's sentence.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery p. 281 s.v. Namāriq\", \"stance\": \"supports\",\n    \"note\": \"Same passage; Jeffery adds 'Only in an early Sura in a description of the delights of Paradise. al-Kindī, Risāla, 85, noted it as a loan-word from Persian … It occurs not infrequently in the early poetry for the cushion on a camel's back, and must have been an early borrowing.'\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi pp. 263-264 s.vv. namāriq, namraq\", \"stance\": \"supports\",\n    \"note\": \"'namāriq: Pl. v. namraq q.v.' and 'namraq: \\\"Sattelkissen\\\" ir. namr \\\"weich\\\" < *namra, aw. namra > mp. narm, suff. -ak' (PLA_pages.txt lines 14730, 14744).\"},\n   {\"src\": \"KLN\", \"where\": \"Comprehensive Etymological Dictionary\", \"stance\": \"silent\",\n    \"note\": \"grep for 'namraq/numruq' in KLN_1966.txt and KLN_1971.txt returns nothing; the word left no English descendant, so Klein has no entry.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"namraq «نَمرَق»\", \"verdict\": \"confirmed\",\n \"derivation\": \"A round trip: the Middle Persian namr(ak) that Arabic borrowed as نمرق came back into New Persian as a learned Arabic word نَمرَق namraq 'cushion, bolster', with its Arabic plural نمارق namāreq and the Arabic feminine نمرقه namraqa alongside — forms that are pure Arabic morphology and could not have grown on Persian soil. Mo'in accordingly marks the entry [ع.] 'Arabic': «نمرق [ع.] (ا.) متکا، بالش؛ ج. نمارق» and «نمرقه [ع. نمرقة] (ا.) متکا، بالش؛ ج. نمارق». Its currency in Persian owes much to the Qur'ānic verse 88:15. So Persian today has the inherited نرم and the re-imported نمرق side by side — a doublet.\",\n \"derivation_fa\": \"این گره یک «رفت و برگشت» است: صورتِ فارسی میانهٔ namr(ak) که عربی آن را «نمرق» گرفت، دوباره همچون واژه‌ای عربی به فارسی بازگشت: «نَمرَق» به معنی متکا و بالش، همراه با جمعِ عربیِ «نمارق» و مؤنثِ عربیِ «نمرقه» — صورت‌هایی که ساختِ صرفیِ عربی دارند و بر زمینِ فارسی نمی‌روییدند. معین نیز مدخل را با نشانِ [ع.] آورده است: «نمرق [ع.] (ا.) متکا، بالش؛ ج. نمارق» و «نمرقه [ع. نمرقة] (ا.) متکا، بالش». رواجِ آن در فارسی تا حدِ زیادی مرهونِ آیهٔ ۱۵ سورهٔ غاشیه است. بدین‌سان فارسیِ امروز «نرم» موروثی و «نمرق» معرّبِ بازگشته را در کنارِ هم دارد، یعنی یک دوگانه (doublet). ادعای نورایی درست است.\",\n \"sources\": [W_NMQ, W_NMQA],\n \"ref_check\": [\n   {\"ref\": \"MON:4815\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi (MON_part2.txt line 79406 ff.): «نمرق [ع.] (ا.) متکا، بالش؛ ج. نمارق» immediately followed by «نمرقه [ع. نمرقة] (ا.) متکا، بالش؛ ج. نمارق» — the headword, the gloss and both of the chart's extra forms نمرقه/نمارق. The page number could not be re-checked (the local MON OCR carries no page markers).\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery p. 281\", \"stance\": \"supports\",\n    \"note\": \"Jeffery documents the Arabic side of the loan and its Qur'ānic status (88:15), which is what makes the word re-enter Persian as an Arabism.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi p. 264 s.v. namraq\", \"stance\": \"supports\",\n    \"note\": \"Asbaghi lists namraq among the Persian loanwords IN Arabic, confirming that the Persian نمرق of this node is the Arabic word coming back.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate'\", \"stance\": \"silent\",\n    \"note\": \"The Borhan is a dictionary of Persian words and has no entry for the Arabism نمرق; Mo'in's footnote on p. 2130 treats only نرم.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Avestan\", \"words\": \"namra-vâxš\", \"verdict\": \"plausible\",\n \"derivation\": \"The compound is real but its meaning is not quite what the chart says. Bartholomae, AiW col. 1042, lemmatises it as '*naṃra-vak- Adj. \\\"ehrerbietige Worte sprechend\\\"', nominative namra-vāxš, attested once in the Frahang ī ōīm; the Pahlavi gloss there is āzāt gōwišn 'of noble/free speech' (so Bartholomae; Nyberg reads the same gloss and renders 'whose speech is noble, is that of a nobleman'). It is a bahuvrīhi 'having soft/deferential words', first member *naṃra- (the root's own adjective), second member vāxš, the nominative of vāk- 'voice, word' — so the chart's cross-reference ☞Wekw is exactly right, PIE *wekʷ- 'to speak' (Skt. vāk, Lat. vōx). Nourai's gloss 'soft sound (voice)' is a literal rendering of the parts rather than the attested sense 'speaking deferentially, of gentle speech'; and note that this compound is the ONLY warrant for an Avestan namra-, which is why Horn writes it with a question mark.\",\n \"derivation_fa\": \"این ترکیب واقعی است اما معنایش دقیقاً آن نیست که نمودار می‌گوید. بارتولمه در ستون ۱۰۴۲ آن را چنین آورده: «*naṃra-vak- صفت، «سخنانِ احترام‌آمیز گوینده»»، با صورتِ فاعلیِ namra-vāxš که تنها یک بار در «فرهنگِ اویم» گواهی شده و برگردانِ پهلویِ آن āzāt gōwišn «آزاده‌گفتار» است (نیبرگ نیز همین را می‌خواند). ساختِ آن بهوریهی است: جزءِ نخست *naṃra- «نرم» و جزءِ دوم vāxš، صورتِ فاعلیِ vāk- «آوا، سخن»؛ پس ارجاعِ نمودار به ریشهٔ Wekw درست است، یعنی *wekʷ- هندواروپایی «سخن گفتن» (سنسکریت vāk، لاتین vōx). اما ترجمهٔ «آوای نرم» تحت‌اللفظی است و معنای گواهی‌شده «نرم‌گفتار، خوش‌سخن» است. افزون بر این، همین ترکیب تنها گواهِ وجودِ namra- در اوستاست و به همین سبب هرن آن را با علامتِ پرسش نوشته است: با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"HRN:230\", \"status\": \"supports\",\n    \"note\": \"Horn no. 1028 (p. 230) cites 'aw. namra.vāxš (?)' as the Avestan evidence for the root — precisely this node, question mark and all (HRN.txt line 8850 ff.).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1042 s.v. *naṃra-vak-\", \"stance\": \"partial\",\n    \"note\": \"'• *naṃra-vak- Adj. \\\"ehrerbietige Worte sprechend\\\": namra-vāxš F.[3]6. Adj.; np. narm \\\"sanft, weich\\\". — Pü.: āzāt gōwišn. — 1) Hds. namnra-.' The form is confirmed; the gloss is 'speaking deferential words', not 'soft sound'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary\", \"stance\": \"partial\",\n    \"note\": \"'Av. (1042) namra.vāxš FrO IIIe with the gl. āzāt gōbišn \\\"whose speech is noble, is that of a nobleman\\\" (read \\\"e*t\\\" = āzāt, not \\\"pt\\\" = dapat as Bthl and Reichelt have it) … Skr namrá- \\\"bowing, humble, obedient\\\"' (NYB_vol2_glossary.txt line 427).\"},\n   {\"src\": \"POK\", \"where\": \"nem-2 p. 764 / ue kʷ- \", \"stance\": \"silent\",\n    \"note\": \"Pokorny's nem-2 lists Avestan namaiti and nemah- but not the compound namra.vāxš; the second member belongs to his *ue kʷ- 'sprechen' (Nourai's Wekw).\"}\n ]\n})\nentries.append(e4)\n\ndoc = json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/part1.json'))\ndoc[\"entries\"].extend(entries)\nwith open('/home/sfmqrb/git/rishe/data/verification/page-348.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", [e[\"entry\"] for e in doc[\"entries\"]])\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk348b.py"
}
```


### [2026-09-07T17:51:53.905Z] TOOL RESULT

```
written [0, 1, 3, 4]
```


## [2026-09-07T17:51:57.464Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-348.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 348"
}
```


### [2026-09-07T17:51:58.846Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 7, 'plausible': 5, 'unverified': 1}
root verdicts: {'confirmed': 1, 'plausible': 3}
ref checks: {'supports': 15, 'not_checked': 1, 'not_found': 3, 'partial': 1}
books consulted: {'supports': 18, 'silent': 12, 'partial': 8, 'contradicts': 1} | by book: {'PHD': 6, 'NYB': 5, 'MON': 3, 'BRT': 3, 'HUB': 3, 'POK': 3, 'PLA': 3, 'HRN': 2, 'KLN': 2, 'FVQ': 2, 'SDQ': 1, 'SYN': 1, 'AHD': 1, 'IEC': 1, 'ARY': 1, 'LAT': 1, 'BQT': 1}
```


## [2026-09-07T17:52:16.681Z] AGENT

Done. Wrote `/home/sfmqrb/git/rishe/data/verification/page-348.json`; `verify_check.py 348` reports 13/13 nodes, 0 PROBLEM lines.

**Page 348 (book p. 318) — 4 entries (1 redirect skipped), 13 nodes**
- Node verdicts: confirmed 7, plausible 5, unverified 1
- Root verdicts: confirmed 1 (Naěza), plausible 3 (Nagan, Naks/Nask, Namra)
- Ref checks: supports 15, partial 1, not_found 3, not_checked 1 · 17 books consulted (18 supports, 8 partial, 12 silent, 1 contradicts)

No `disputed` and no `transcription_suspect` items; **no extraction errors** — the JSON matches the chart throughout. Flags worth the owner's attention:

- **Naks/Nask (root + #1 Av. naska + #4 Lat. naxae)** — the whole entry is copied verbatim from Mann IEC 825/826 (ref verified). Mann's root is idiosyncratic: Pokorny 758-9, Watkins and Klein file this material under *ned- 'to bind'. Bartholomae **contradicts** the gloss: Av. naska- is the Avesta text-division ('bundle'), never 'thread'. Latin "naxae 'bonds'" is Mann's own emendation of glossary *noxae*; the real word is nassa/naxa 'fish-trap'.
- **Naks #2 Pahlavi nax — `unverified`**: no MP nax anywhere (MacKenzie, Nyberg silent), and Av. -sk- would not give MP -x-. MON:4683 `not_found` (local Mo'in OCR is unpaginated).
- **Nagan root — `plausible` only on the label**: *nagan(a)-/*nagna- is exactly Hübschmann p. 101 and Mo'in BQT 2107, but it is Old *Iranian*, unattested in Old Persian (Kent silent).
- **Namra root/#5** — Avestan namra- exists only in the compound namra.vāxš (Bartholomae col. 1042 *naṃra-vak-), glossed "speaking deferential words", not "soft sound"; Horn himself prints it with "(?)".
- Best confirmations: BQT:2226 (Mo'in: pahl. nēzak < Av. naēza, "Bartholomae 1037" — exactly Nourai's chart), HUB:101, HRN:229/230, PLA:265, SDQ:73, and Jeffery FVQ 281 for Arabic namāriq (checked in the English original since VDQ:403 on noorlib is not fetchable).

Two references could not be reached: FSF:336 (Noushin OCR has no page numbers, and the book carries no etymology) and SNS:223 (unusable Persian OCR, no page markers). Five Wiktionary pages archived via `fetch_source.py`; BQT pages 2226/2107/2130 rendered and cached under `data/verification/sources/refs/ocr/BQT/`.
