# Verification process log — verify-page-497


## [2026-09-14T03:08:57.088Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 497 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-497.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-497.json. Write /home/sfmqrb/git/rishe/data/verification/page-497.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 497` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:58.152Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:59.005Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:59.020Z] TOOL RESULT

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


## [2026-09-14T03:08:59.495Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-497.txt"
}
```


### [2026-09-14T03:08:59.512Z] TOOL RESULT

```
1	=== PDF page 497 (book page 467) ===
2	--- entry 0 ---
3	ROOT [Turkish] Tata : Name of a Mongol tribe  (refs KLN:1574)
4	#1 (parent #0) [Persian] refs=MON:994 | tâtâr «تاتار ( تتار ، تتر )» : a Mongol Tribe
5	  #2 (parent #1) [English] refs=AHD; KLN:1574 | Tatar : a Mongol tribe
6	#3 (parent #0) [Sogdian] refs=SOD:392 | tt`r
7	--- entry 1 ---
8	ROOT Tâta -> redirect to Âtos
9	--- entry 2 ---
10	ROOT Tauro -> redirect to Tĕu 1
11	--- entry 3 ---
12	ROOT [Pahlavi] Taxl, Tâxlik : Taxl: bitter. Tâxlik: bitterness.  (refs MON:1131; BQT:508)
13	#1 (parent #0) [Persian] refs=MON:1131; BQT:508 | talx «تلخ ( تلخه ، تلخک ، تلخکام )» : bitter ; talx-šakŭk «تلخ شکوک ( تلخ جوک )» : a bitter herb (chicory) | NOTE: Note the change of the last two letters and compare with "mağz / mazğ"
14	  #2 (parent #1) [Arabic] refs=BQT:508; KLN:1573 | tarax-šaqŭq : chicory
15	    #3 (parent #2) [English] refs=KLN:1573; WEB:1865 | taraxacum : a kind of chicory
16	--- entry 4 ---
17	ROOT Tâxlik -> redirect to Taxl
18	--- entry 5 ---
19	ROOT Tebh -> redirect to Teub
20	--- entry 6 ---
21	ROOT Tebhos -> redirect to Teub
22	--- entry 7 ---
23	ROOT Teg -> redirect to Steg
24	--- entry 8 ---
25	ROOT Teig -> redirect to Steig
26	--- entry 9 ---
27	ROOT Teks -> redirect to Tex
28	
```


## [2026-09-14T03:09:02.317Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-497.json",
 "description": "Read source JSON for page 497"
}
```


### [2026-09-14T03:09:02.360Z] TOOL RESULT

```
{
  "pdf_page": 497,
  "book_page": 467,
  "entries": [
    {
      "root": {
        "name": "Tata",
        "lang": "Turkish",
        "refs": "KLN:1574",
        "gloss": "Name of a Mongol tribe"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:994",
          "words": [
            {"translit": "tâtâr", "gloss": "a Mongol Tribe", "script": "تاتار ( تتار ، تتر )"}
          ],
          "note": null,
          "quote": {
            "text": "در آن زمین که نسیمی وزد ز طُرّهٔ دوست - چه جای دم زدن نافه های تاتاریست",
            "poet": "Hâfez"
          }
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "English",
          "refs": "AHD; KLN:1574",
          "words": [
            {"translit": "Tatar", "gloss": "a Mongol tribe", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:392",
          "words": [
            {"translit": "tt`r", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Tâta",
        "redirect": "Âtos"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Tauro",
        "redirect": "Tĕu 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Taxl, Tâxlik",
        "lang": "Pahlavi",
        "refs": "MON:1131; BQT:508",
        "gloss": "Taxl: bitter. Tâxlik: bitterness."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:1131; BQT:508",
          "words": [
            {"translit": "talx", "gloss": "bitter", "script": "تلخ ( تلخه ، تلخک ، تلخکام )"},
            {"translit": "talx-šakŭk", "gloss": "a bitter herb (chicory)", "script": "تلخ شکوک ( تلخ جوک )"}
          ],
          "note": "Note the change of the last two letters and compare with \"mağz / mazğ\"",
          "quote": {
            "text": "زان حدیث تلخ میگویم تو را - تا ز تلخی ها فرو شویم تو را",
            "poet": "Molavî"
          }
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "BQT:508; KLN:1573",
          "words": [
            {"translit": "tarax-šaqŭq", "gloss": "chicory", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "KLN:1573; WEB:1865",
          "words": [
            {"translit": "taraxacum", "gloss": "a kind of chicory", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Tâxlik",
        "redirect": "Taxl"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Tebh",
        "redirect": "Teub"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Tebhos",
        "redirect": "Teub"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Teg",
        "redirect": "Steg"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Teig",
        "redirect": "Steig"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Teks",
        "redirect": "Tex"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T03:09:04.862Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','MON','SOD','BQT','AHD','WEB','POK','PHD','NYB','HRN','HUB','ARY','LKT','TTS','SKT','FSD','PLA','AFM','FVQ','HJB','IEC','SYN','WLD','CHEUNG','MK']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-14T03:09:06.179Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
```


## [2026-09-14T03:09:11.031Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','WEB','SOD','BQT','MON']:\n    print('=====',k)\n    print(json.dumps(d[k], ensure_ascii=False, indent=1))\n\""
}
```


### [2026-09-14T03:09:12.146Z] TOOL RESULT

```
===== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
===== WEB
{
 "title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)",
 "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w",
 "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt",
 "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.",
 "notes": "",
 "cites": "page number of Webster's New Twentieth Century Dictionary, 2nd ed."
}
===== SOD
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
===== BQT
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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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
===== MON
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
```


## [2026-09-14T03:09:15.539Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i '^tatar\\|^taraxacum\\|Tartar' KLN_1966.txt | head -40"
}
```


### [2026-09-14T03:09:15.625Z] TOOL RESULT

```
14501:fecula,  n.,  starch.  —  L.  faecula,  ‘burnt  tartar, salt  of  tartar’,  dimin.  formed  fr  .faex,  gen.  fae- cis,  ‘dregs’.  See  feces.  For  the  ending  see  suff. -ule.
16107:Derivatives:  ghoul-ish,  adj.,  ghoul-ish-ly,  adv. ghurry,  n.,  clepsydra,  clock,  watch,  space  of  time, hour  {India).  —  Hind,  ghari,  fr.  OI.  ghafika, ‘water  jar,  pot’  (serving  as  a  water  clock),  fr. ghafah,  of  s.m.,  which  is  of  uncertain  origin, ghyll,  n.,  a  ravine.  —  AN.  Engl,  dialectal  var. of  gill,  ‘ravine’;  introduced  into  English  by  the English  poet  William  Wordsworth  (1770-1850). giant,  n.  —  ME.  geant,  fr.  OF.  geant  (F.  geant), fr.  earlier  jaiant,  fr.  VL.  *gagantem,  acc.  of *gagas,  assimilated  vr.  L.  gigas,  ‘a  giant’,  fr. Gk.  ytya q,  ‘a  giant’,  fr.  I’tyat;,  'any  of  the  sons of  the  Earth  and  Tartarus’,  which  is  prob.  a pre-Hellenic  word.  Cp.  gigantic.
26088:compounded  of  oStov,  gen.  oSovto;,  ‘tooth’, and  -oeiStj?,  ‘like’,  fr.  s!8o?,  ‘form,  shape’.  See odont-  and  -oid  and  cp.  dentoid. odontolith,  n.,  dental  tartar.  —  Compounded  of odonto-  and  Gk.  Xtffo?,  ‘stone’.  See  -lith. odontology,  n.,  the  study  of  the  teeth  ahd  their diseases.  —  Compounded  of  odonto-  and  Gk. -Xoyia,  fr.  -Xoyo;,  ‘one  who  speaks  (in  a  cer¬ tain  manner;  one  who  deals  (with  a  certain topic)’.  See  -logy.
26155:ogre,  n.,  1)  a  man-eating  giant;  a  hideous  or cruel  man.  —  F.,  first  used  by  Perrault  in  his fairy  stories,  1697;  in  English  it  appears  first (spelled  hogre )  in  a  translation  of  a  French version  of  the  Arabian  Nights;  fr.  Byzantine Ogur,  ‘Hungarian’.  The  sense  development  is due  to  a  confusion  of  the  Hungarians  with  the Huns  and  the  Tartars.  See  Wiener  in  Anglia, XXIII,  107,  and  Meyer-Liibke,  Romanisches etymologisches  Worterbuch,  p.  446,  No.  6048. Cp.  Ugrian.
38134:tanga,  n.,  also  tanka,  name  of  various  coins  in India  and  Turkestan.  —  Hind,  tanga,  lit. ‘weight’,  fr.  OI.  tahkah,  ‘stamped  coin;  a weight’,  which  is  prob.  connected  with  Tartar. tanka,  ‘a  silver  coin’,  ModPers.  tanga.  Arm. t'anka,  ‘a  small  coin’.
38198:Taraxacum,  n.,  a  genus  of  plants  of  the  chicory family  (hot.)  —  ModL.,  fr.  Arab,  tarakhshaqun, tarakhshaquq,  fr.  Pers.  talkh  chakok,  lit.  ‘bitter herb’.
38244:Tartar,  n.  and  adj.  —  ML.  Tartarus,  fr.  Pers.  Ta¬ tar,  ult.  fr.  Tata,  name  of  the  Mongols,  who coming  from  the  Gobi  desert  invaded  Russia  in the  9th  cent.  The  first  r  in  Tartar  is  due  to  a  con¬ fusion  w'ith  L.  Tartarus,  ‘hell’ ;  see  Tartarus. tartar,  n.,  1)  potassium  bitartrate,  KHC4H4Os ( chem .);  2)  a  hard  deposit  on  the  teeth.  —  ME. tartre,  tartar,  fr.  OF.  tartre,  fr.  ML.  tartarum , fr.  Gk.  Tdpxapog  (see  Tartarus);  so  called  by Paracelsus  with  regard  to  the  burning  effect  of this  compound.
38245:Derivatives:  tartar-eous,  tartar-ic,  tartar-ish, adjs.,  tartar-ize,  tr.  v.,  tartar-iz-ation,  n.,  tortur¬ ous,  adj.
38246:Tartarean,  adj.,  pertaining  to  Tartarus.  —  Form¬ ed  fr.  Tartarus  with  suff.  -ean.
38247:Tartarus,  n.,  the  abyss  below  Hades;  place  of punishment;  Hades,  netherworld;  hell  (Greek mythol.)  —  L.,  fr.  Gk.  Taprapoc,  prob.  a  word of  imitative  origin,  suggestive  of  something frightful.  Cp.  tartar.
38248:tartlet,  n.,  a  small  tart.  —  Formed  fr.  tart,  n., with  dimin.  suff.  -let.  Cp.  F.  tartelette. tartrate,  n.,  salt  of  tartaric  acid  (chem.)  —  F., formed  with  chem.  suff.  -ate  fr.  tartre,  ‘tartar’.
38249:See  tartar.
38279:Tatar,  n.  —  See  Tartar.
39648:F.)  tortues ,  pi.  of  tortue ,  fr.  earlier  Proven?,  tor- tuga,  fr.  OProven?.  tartuga,  fr.  It.  tartaruga, which  derives  fr.  VL.  tartaruca,  lit.  ‘the  infernal animal’,  fr.  L.  Tartarus',  see  Tartarus.  The Proven?,  form  tortuga  is  due  to  the  influence  of L.  tortus,  ‘twisted’.  Folk  etymology  found  in  the name  of  the  animal  a  reference  to  its  twisted legs.  Cp.  turtle,  ‘tortoise’, tortricid,  adj.,  pertaining  to  the  Tortricidae.  —  See next  word.
```


## [2026-09-14T03:09:16.456Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==799||NR==800||NR==798' KLN_1966.txt | head -200"
}
```


### [2026-09-14T03:09:17.522Z] TOOL RESULT

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bt8vramxr.txt

Preview (first 2KB):
��,  and  houder,  ‘holder’;  in¬ fluenced  in  form  by  E.  holder  ( stadtholder  shows also  the  influence  of  G.  Stadt,  ‘town’).  See  stead, hold,  v.,  and  agential  suff.  -er.  Du.  stadhouder — like  MLG.  stedeholder,  Dan.  stadholder,  Swed. stathallare  and  G.  Statthalter,  of  s.m. — are prop,  loan  translations  of  L.  locum  tenens  (see locum  tenens).
stadholderate,  stadtholderate,  n.,  office  of  a  stad¬ holder.  —  A  hybrid  coined  fr.  prec.  word  and -ate,  a  subst.  suff.  of  Latin  origin, stadium,  n.,  1)  a  Greek  measure  of  length;  2)  a racecourse.  —  L.,  fr.  Gk.  oxocSiov,  ‘racecourse, stadium’,  which  is  a  blend  of  on diSiov,  ‘race¬ course’,  and  oxaSiov,  neut.  of  axaSioi;,  ‘fix, firm’.  ZtoxSiov  is  a  derivative  of  onas/,  ‘to  draw, tear’  (see  spasm).  ZxaSioc  derives  fr.  I.-E.  base *sta-,  ‘to  stand’;  see  state, staff,  n.  —  ME.  staf,  fr.  OE.  stsef,  ‘stick,  staff",  rel. to  OS.  staf,  ON.  stafr,  Dan.  star,  Swed.  staf, OFris.  stef,  MLG.,  MDu.,  Du.  staf,  OHG.  stab, MHG.  slap,  G.  Slab,  Goth.  *staf-s  (in  dat.  pi. stabim),  ‘element’,  and  cogn.  with  OLith.  stabas, ‘idol’,  Lith.  stebas,  ‘staff,  pillar’,  Lett,  stabs, OSlav.  stoborii,  ‘pillar’,  OPruss.  stabis,  ‘stone’, OI.  stabhrtati,  stabhndti,  ‘supports’.  All  these words  derive  fr.  I.-E.  base  *steb(h)-,  ‘to  cause  to stand,  place,  support;  to  step’.  See  step  and  cp. words  there  referred  to.  Cp.  also  stave  and  the second  element  in  distaff,  Gustavus,  palstave. Derivatives :  staff,  tr.  v.,  staff-ed,  adj. stallage,  n.,  accessories.  —  G.,  fr.  stuffier en,  ‘to dress  up,  trim,  garnish’,  fr.  MLG.  stofferen,  staf- feren,ft.  MDu.  stofferen,  fr.  OF.  estofer  (F.  itof- fer),  fr.  OHG.  stopfon  (MHG.,  G.  stopferi),  ‘to stuff,  fill’.  OF.  estofe  (F.  etoffe),  ‘stuff,  material’, is  prob.  a  back  formation  fr.  estofer  (F.  etoffer). Se
...
</persisted-output>
```


## [2026-09-14T03:09:22.475Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [38198,38244,38279,38134]:\n    pre='\\n'.join(lines[:target])\n    print(target, 'leaf', pre.count('\\f'))\n\""
}
```


### [2026-09-14T03:09:23.736Z] TOOL RESULT

```
38198 leaf 833
38244 leaf 834
38279 leaf 835
38134 leaf 832
```


## [2026-09-14T03:09:33.499Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\n# look for digits alone on lines in leaves 830-836\nfor i in range(830,838):\n    p=pages[i]\n    print('--- leaf',i, repr(p[:120]))\n\""
}
```


### [2026-09-14T03:09:34.898Z] TOOL RESULT

```
leaves 903
--- leaf 830 'e  rail  across  the  stern of  a  ship.  —  Du.  tafereel,  dimin.  of  tafel,  ‘table’, which,  together  with  OHG.  '
--- leaf 831 've,  adj.  —  A  hybrid  coined  fr.  talk  and -ative,  a  suff.  of  Latin  origin.\nDerivatives:  talkative-ly,  adv.,'
--- leaf 832 'hief, who  lived  in  the  second  half  of  the  1 7th  and  in the  first  half  of  the  18th  century.\nTammanyism,  '
--- leaf 833 'cp.  the  first  element  in tandem.  Cp.  also  taunt.  Cp.  also  the  first  ele¬ ment  in  tankard  and  the  second'
--- leaf 834 ' see  dram  and  cp.  target.  ML. targ(i)a,  OProvenq.  targa  (whence  It.  targa),  Sp. tarja,  ‘shield’,  are  also '
--- leaf 835 'p,  saucer’.  Cp.  OProveng.  tassa, It.  tazza,  Sp.  taza,  ‘cup’,  which  are  of  the  same origin.  Cp.  also  tazz'
--- leaf 836 '.  —  ME.  taxacioun,  fr.  MF.  (=  F.) taxation,  fr.  L.  laxationem,  acc.  of  taxatio,  ‘a rating,  valuing,  appr'
--- leaf 837 '.,  an  adherent  of  technocracy.  — Compounded  of  techno-  and  -crat.\nDerivative:  technocrat-ic,  adj. technology,'
```


## [2026-09-14T03:09:47.363Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(825,845):\n    nums=re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$', pages[i])\n    nums2=re.findall(r'\\b1[5-7][0-9]{2}\\b', pages[i])\n    print(i, nums, nums2[:8])\n\""
}
```


### [2026-09-14T03:09:48.530Z] TOOL RESULT

```
825 ['1556'] ['1541', '1614', '1556']
826 [] []
827 [] ['1530']
828 [] ['1789']
829 ['1565'] ['1565', '1791']
830 ['1566'] ['1566']
831 ['1568', '1569'] ['1568', '1569', '1763']
832 [] ['1583', '1561', '1613', '1767']
833 ['1572'] ['1572']
834 [] []
835 ['1577'] ['1577']
836 ['1578', '1579'] ['1707', '1578', '1579']
837 ['1580'] ['1580']
838 ['1583'] ['1762', '1792', '1583', '1679', '1754', '1728', '1757']
839 ['1584', '1003'] ['1743', '1798', '1584', '1564', '1642']
840 [] []
841 [] ['1693', '1761']
842 [] ['1797']
843 [] ['1779']
844 [] []
```


## [2026-09-14T03:10:13.094Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD taxl/talx\"; grep -n -i 'taxl\\|talx\\|tlhk' PHD.txt | head -20; echo \"=== NYB\"; grep -n -i 'taxl\\|talx\\|tlhk' NYB_vol2_glossary.txt | head -20; echo \"=== HRN\"; grep -n -i 'talh\\|talx\\|taxl' HRN.txt | head -20; echo \"=== HUB\"; grep -n -i 'talh\\|talx\\|taxl' HUB.txt | head -20"
}
```


### [2026-09-14T03:10:13.191Z] TOOL RESULT

```
=== PHD taxl/talx
593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
594:taxlih 83 102
1006:bitterness taxlih.
4525:-(i)t tah taxl taxlih
=== NYB
3697:tahl [t’hl] bitter 6119. — MPrth tal; MPrs thr (List 88); Paz. tahal (SGV); NP talx.
7471:talx: tahl
=== HRN
6287:Also aus aw. '*8ta/ma-^ vergl. staxlra- (zu dem
16622:pataxlnk 274'>".
=== HUB
1643:Hierher: np. talx *bitter, paz. tahal = phi. taxr
8981:xr und xtr wird im Np. auslautend zu tr in: talx
9433:Boxr vd. 1, 22, arm. Bahlf ap. BaxtriS ; np. talx 'bitter =
9534:b) Ap. xr — np. lx\ talx 'bitter', paz. tahal (= tahl) =
10751:talx 48, 251.
```


## [2026-09-14T03:10:14.163Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD tt'r\"; grep -n \"tt\\`r\\|tt'r\\|ttr\\b\\|Tatar\\|Turkish tribe\" SOD_pages.txt | head -30"
}
```


### [2026-09-14T03:10:15.398Z] TOOL RESULT

```
=== SOD tt'r
14633:3842 Pytr =» pr'yttr                                                 vision
18077:    5048 kws' B, M, S                                                   Sogdica. 64.13-, W-Lii; TPS 3.216, 8.177; kwttr,
18096:        kutre (kwttr'k, kwtr>k)                              5081 kwz(z) B                                     $J
18106:5067 kwttr'k ^ kwtr>y
19436:5482 mry^h          M => mrym                                              BBB; MSP bl0; Hen. Tales. 480.8; msfttr,
23888: pr}yttr
23890: 7031 pr'yttr B                                        jyy>     7042 prpVcy S                            j***/ <olj*>fj
24969:                                                                       fritam (frytm) ©<*friya-tama ^pr'yttr
29916:9066 swmtr M => swmdr                                         9080 swtr =» swttr
29917:9067 swndy(h) M                                    J^^        9081 swttr B                            vuf «JUjJ^>,
31730:     Tatar                                                  9708 twy1 B, M, S                                ^^txs
31733:9698 ttr'w B                                   Jj»v<j>-          TSP 3.9, 14, 6.33, 7.133, 8.151, 156; Frag. Len. 13
34252:          Frag. Len. 92.15; SCE 567; wyttr, VJ 828,                   428; Sund. MHC p27.6; AoFviii 1981, 22R4,
36546:11288 zywttr S
37117:      zuyt/ ydar (zwyt(t)r) -»zywttr                                 11489 zwrn'k B                                 dhj>«Jl*j
39606:Syriac 9075                                   Tatar     9697                          than 1912, 3147, 3208
```


## [2026-09-14T03:10:34.504Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31720,31745p' SOD_pages.txt; echo \"---- leaf of line 31730\"; python3 -c \"\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('leaf', '\\n'.join(lines[:31730]).count('\\f'))\n\""
}
```


### [2026-09-14T03:10:35.617Z] TOOL RESULT

```
       S W, IIJ 1976, 58                                         tu8e-y(twdy,
                                                                       A      twSyh)

9696 tsycq M                         oJL <J^- / ^*j^             heap, mass
                                                                 BSTBL, Dhy. 343; Benv. Notesii 236; Etii 329;
     tasice, tasicak ^t's-
     axe, spade                                                    BSTii 857.1 1:"C2, 17V4, 22V 13; Sogdica. 56.28,
     GMS 1012; Sund. Man. Lett. 305.18; 307 n 20
9697 tVr S                                            j&    9706 twdy C =» tw8>k
     tatar ©ob. -y                                          9707 tw8yh M =» tw6>k
     Tatar                                                  9708 twy1 B, M, S                                ^^txs
                                                                 tux ©Skt. takva =*twytr, twx
     S W-Ham. CII 1990 p86                                       fast
9698 ttr'w B                                   Jj»v<j>-          TSP 3.9, 14, 6.33, 7.133, 8.151, 156; Frag. Len. 13
     tatarw ©Pahl. tadarw
                                                                   Rl; GMS 254; Sogdica. 40.13; Tales. 481.44;
     pheasant                                                      MDii p2l3; S W, BSOAS 38, 133; twYw, TSP
     TSP 3239
                                                                   2.415
9699 9ty>q C                        J^j <c^Lj <&£-?         9709 twya S                               '^Oi
     Gatyak ? ©fOam\ Av. Oamnahvant "solicitous";                toy ©Khwar. twT\ Arm. tugam =>twz-, twyt-
       S0a "be strong"; Khot. thaka
     comfort, consolation                                        MDii p8923; Gersh. Advice. 90
                                                                 payment
 393

---- leaf of line 31730
leaf 459
```


## [2026-09-14T03:10:43.825Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (457,458,459,460):\n    ls=[l for l in pages[i].split('\\n') if l.strip()]\n    print('leaf',i,'FIRST:',ls[0][:80],'|| LAST:',ls[-1][:80])\n\""
}
```


### [2026-09-14T03:10:44.886Z] TOOL RESULT

```
leaf 457 FIRST:   tr*ypw                                                                         || LAST:                                                                                 
leaf 458 FIRST:  391 || LAST: 9674 trsVny ^ trs,k>n,k
leaf 459 FIRST:                                                                                  || LAST:                                                                  payment
leaf 460 FIRST:  393 || LAST:
```


## [2026-09-14T03:10:52.876Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if 'تلخ' in p:\n        print(i, p.count('تلخ'))\n\" | head -40"
}
```


### [2026-09-14T03:10:53.951Z] TOOL RESULT

```
leaves 777
2 1
42 1
116 1
142 1
235 1
236 1
257 1
272 1
310 1
312 1
317 1
365 1
368 1
372 1
377 1
396 1
406 1
454 1
531 1
548 1
659 1
692 1
693 1
703 1
714 1
736 6
753 1
762 1
```


## [2026-09-14T03:10:56.874Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[736])\n\""
}
```


### [2026-09-14T03:10:57.943Z] TOOL RESULT

```
تلاخان
قلاشان - با شین‌نفطه‌دار بروزن‌هراسان؛
نام مرغزارست بز ره در صفاهان٩‏ 3
کوند که درمیان فرح زنان است- وبمعنی یاچ
تنبان وشلوار عماهده است
قالالا ‏ بر وزن جلالا » نقش وصوت
و ۷ | گویند .
لا و 0 - بفتح اول ونون بروزن‌ادارج »
بانگگ ومشفله وشور 0 را گویند» وبکون
لون ِ است؟ .
تلیا ۴ با بای ابجد بر وژن حلوا ؛
عافت زند و بزند(۱) د.ه گوسفند و کار و امتال
آن باشد .#
تلج جکو ك س باخای قطه دار وجیم
وکاف و واو وکاف دیگر وحرکت حجهول . نام
کاسنی صحرابی‌است» ومعربآن طرخشقوق‌باشد,
و بعربی نید کویند .
تلخ جو لك » با جبم و اف بر وزن
گرم سود ؛ بمعنی تلخ جکوك است که کاسنی
صحرانی باشد ۰
(۱) چك: ژئذ ویاژند.
با هواس
تللخ عیشی ۰ کناه از کی است. که
آزاری ومکروهی ومصیبتی از حوادث رو زکار
یذو رسنده باشد .
تلخلت ح بر وزن زرواه . صتیر تلخ
باشد - و نام گیاهی است بغایت تلخ , و بسنی
گویند خربزة نلخ است که مربی حنظل
وقثاهء‌النمام خوانند. و بعضی کاسنی را گفته‌اند
و نام یکی از ظرفای سلطان محمود غزنوی
بوده -.
دناست .
تلحی بر وزن بل ی.کاسنیراگویند
وآنگیاهی است ممروف ٩‏ .
تلساگ* ه بکر ارل ونانی و سکون
که جزو خوشهٌ بزر که است,عنی‌برخوش‌بز رکه
تللكت ‌ بفتح اول 9 نانفی
کاف .کسی را کویند که صاتش بسیار کنده
وفر بباشده و فرجابی‌دیگر عسلت بر کنده‌نوشثه
بودند بفتح بای ابجد وکاف ام اعلم - و بفتح
۴ رکه :تلاح .
۴ ‌ فتاءالنعلی خرائه
دوران مقا چو باد صحرا بگذشت
۷ - د رکناملد فکهاع1.
. تلخی وخوشی وزشت وزببا بگذشت .
«کلستان ۲ه *.
مخن آخر بدهن میگنرد موذی را
سخنش تنم نخواهی دهنش شیری نکن .
«گلستان .4٩‏
۳ ۰ ب
شه درصفحه 6۰٩‏
```


## [2026-09-14T03:11:12.761Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('=== leaf 735 (p.507)')\nprint(pages[735][:3000])\n\""
}
```


### [2026-09-14T03:11:13.810Z] TOOL RESULT

```
=== leaf 735 (p.507)
یدای ‌-
از ولات کنجه - و پرده ای ازموسيقی‌باشد .
تگتارا . غتح اول و ای قرشت
بر وزن پرواز » ناختن و دویدن - و جتجو
کردن ماشه .
تگرگ؟ صبفتح اول و ثانی و سکون
رای فرشث وکاف فارسی ۰ معروف است که ژاله
وبخچه باشد - و بفتح دای فرشت بروزن‌نفزك.
تلای
یاه وی دبواررا گویند.
یگ - بفتح اول بر وزن حمل » قوچ
جاعه بثه کنند؟ .
تگمر م اول و فتح میم بس وزن
دختی » تیر تخمار است(۱) » وآن نبری‌باشد که
بجای پیکان کرعی از چوب دارد .
قل » بنتح اول وسکون ثانی , کوه‌یست
ويشتهة بلند راگویند؟ - و هرچیزی که برروی
هم ربخته خرمن کرده باشند - و کنابه از پس
امردمز لف‌ومضخم(۲) باشد» کوبندعربی‌است6 .
تلا توف بفتح اول وثانیبالف کشیده
وفوقانی بواو رسیده و بفا زده » شور و غوغا را
کویند - وکی را نیز کنته اند که خود را
وتفوها .
هر کجا ربدکی بود تگلم
چبر کین(۳) و بلید نگهدارد و از کثافت‌ونجاست
پرهیزنکند ومردم ازونفرت کنندلا .
اج بفتح اول بر وز نکلاح» بانگ
ومتغله وشور وغوغا وغلغله باشد » و باین ءعنی
لاس « بفتح اول بر وزن ممای ,
نام شهرست در تر کستان۸ .
(۳) خم۳:چ رکن.
۴ - پهلوی 28278) «بندهش ۱۳۷
هر کجا کاملی بود خیم .
«لفت فری ۱ ره : تل.
. ۹
٩‏ - زنی پلشت ونلاتوف و اهرمن کردار
۲ - رکه؛ تلانج: ثب‌یامد بردرم دربان باج
نگر نگردی از کرد اوکه کرم آمی .
شهبدبلخی. «لغت فری ۲۷.
در بجنبانید بابانگگ و تلاج .
طبان مرغزی. «لت‌فری ۵۶
لکنی خمش برادر» چو بری ازآب و آذر
ز سبو همان تلاید که درو کنند بائی .
```


## [2026-09-14T03:11:15.371Z] TOOL CALL #18: Bash

```json
{
 "command": "pdftoppm -f 497 -l 497 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg497 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-14T03:11:17.501Z] TOOL RESULT

```
total 30932
drwx------ 3 sfmqrb sfmqrb   12288 Sep 13 23:11 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   92443 Sep 13 21:13 391-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  129993 Sep 13 21:11 394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21316 Sep 13 21:11 394-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44712 Sep 13 21:14 400-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116049 Sep 13 21:14 400-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99858 Sep 13 21:16 404-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91913 Sep 13 21:18 411-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34177 Sep 13 21:23 412-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79667 Sep 13 21:24 414-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110116 Sep 13 21:31 417hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88133 Sep 13 21:31 417-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12361 Sep 13 21:31 417-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45082 Sep 13 21:33 421-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96996 Sep 13 21:38 428hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18073 Sep 13 21:38 428-zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21962 Sep 13 21:38 428-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  112884 Sep 13 21:41 429hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16099 Sep 13 21:41 429-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96248 Sep 13 21:43 431-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   94911 Sep 13 21:46 432-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115297 Sep 13 21:42 436-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125916 Sep 13 22:14 440-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  119070 Sep 13 22:18 442hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32445 Sep 13 22:18 442-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99953 Sep 13 22:12 444hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18325 Sep 13 22:12 444-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77093 Sep 13 22:10 445-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115375 Sep 13 22:12 446-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb  113997 Sep 13 22:18 450hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21276 Sep 13 22:18 450-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   85759 Sep 13 22:19 454-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  114246 Sep 13 22:16 457hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17873 Sep 13 22:16 457-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87326 Sep 13 22:43 460-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86207 Sep 13 22:38 462-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77713 Sep 13 22:56 466hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35076 Sep 13 22:56 466-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64929 Sep 13 22:42 472-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142254 Sep 13 22:57 474hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21097 Sep 13 22:57 474-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1227534 Sep 13 21:24 afm74-420.png
-rw-rw-r-- 1 sfmqrb sfmqrb  908713 Sep 13 21:23 afm76-421.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2998 Sep 13 23:09 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep 13 21:29 ahd430.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   37783 Sep 13 22:40 asha-468.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   46904 Sep 13 21:10 beekes410.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  207924 Sep 13 22:34 bly78-473.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1158 Sep 13 21:33 bqt1328-ftr-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1151 Sep 13 21:33 bqt1328-hdr-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1872 Sep 13 21:33 bqt1328-top-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3114 Sep 13 21:33 bqt1330-top-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb     146 Sep 13 22:00 bqt1-440.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  309946 Sep 13 21:35 bqt2123-fn-435.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95654 Sep 13 20:53 bqt390_436_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   34040 Sep 13 20:54 bqt390_436_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  124665 Sep 13 20:53 bqt390_662_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   93636 Sep 13 20:53 bqt390_662_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  537986 Sep 13 20:53 bqt390_n436.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527696 Sep 13 20:53 bqt390_n662.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  267233 Sep 13 22:02 bqt439-l254.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  171966 Sep 13 22:31 bqt469-n486-bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  620205 Sep 13 22:31 bqt469-n486.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   13019 Sep 13 22:31 bqt469-n486-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  254148 Sep 13 22:32 bqt469-n547-bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  123533 Sep 13 22:32 bqt469-n547-fn2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97094 Sep 13 22:32 bqt469-n547-hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb  583572 Sep 13 22:32 bqt469-n547.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  245067 Sep 13 22:32 bqt469-n547-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2642 Sep 13 22:32 bqt469-n547-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21513 Sep 13 21:39 build2-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   23107 Sep 13 22:49 build2-471.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19296 Sep 13 21:42 build3-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66340 Sep 13 21:06 build-389.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60725 Sep 13 21:08 build-390.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66850 Sep 13 21:11 build-391.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67328 Sep 13 21:13 build393.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65361 Sep 13 21:10 build-394.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53331 Sep 13 21:06 build-395.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49820 Sep 13 21:12 build-396.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61718 Sep 13 21:06 build-398.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55842 Sep 13 21:13 build-400.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56563 Sep 13 21:13 build-401.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45908 Sep 13 21:12 build-405.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52807 Sep 13 21:06 build-406.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63772 Sep 13 21:13 build-407.py
-rw-rw-r-- 1 sfmqrb sfmqrb   44609 Sep 13 21:22 build-412.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55188 Sep 13 21:23 build-414.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53220 Sep 13 21:24 build-415.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76184 Sep 13 21:30 build-417.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56437 Sep 13 21:35 build-418.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55739 Sep 13 21:45 build-419.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59029 Sep 13 21:41 build-422.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56950 Sep 13 21:42 build-425.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63145 Sep 13 21:40 build-426.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53942 Sep 13 21:37 build-428.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66449 Sep 13 21:40 build-429.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52975 Sep 13 21:39 build-430.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56759 Sep 13 21:42 build-431.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21413 Sep 13 21:37 build-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50426 Sep 13 21:45 build-435.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61435 Sep 13 21:55 build-438.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71845 Sep 13 22:16 build-439.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65194 Sep 13 22:13 build-440.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61144 Sep 13 22:11 build-444.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55607 Sep 13 22:10 build-445.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65723 Sep 13 22:11 build-446.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52352 Sep 13 22:17 build-447.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42400 Sep 13 22:13 build-448.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57147 Sep 13 22:17 build-450.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60619 Sep 13 22:15 build-452.py
-rw-rw-r-- 1 sfmqrb sfmqrb   86059 Sep 13 22:16 build-453.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76125 Sep 13 22:18 build-454.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80202 Sep 13 22:19 build-455.py
-rw-rw-r-- 1 sfmqrb sfmqrb   35780 Sep 13 22:11 build-458.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61561 Sep 13 22:42 build460.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53014 Sep 13 22:57 build-461.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49392 Sep 13 22:44 build-463.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59762 Sep 13 22:58 build-464.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30026 Sep 13 22:39 build-465.py
-rw-rw-r-- 1 sfmqrb sfmqrb   69908 Sep 13 22:54 build-468.py
-rw-rw-r-- 1 sfmqrb sfmqrb   85662 Sep 13 22:56 build-470.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43488 Sep 13 22:42 build-471.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49272 Sep 13 22:42 build-472.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58068 Sep 13 22:44 build-473.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66296 Sep 13 22:56 build-474.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2291 Sep 13 20:56 c404-empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77003 Sep 13 21:01 c404-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4255 Sep 13 20:56 c404-patil.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34837 Sep 13 20:57 c404-pest.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46825 Sep 13 20:57 c404-symp2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34820 Sep 13 20:56 c404-symp.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35928 Sep 13 21:11 c412_cedar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42397 Sep 13 21:11 c412_makrome.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81867 Sep 13 21:12 c412_makrome_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54838 Sep 13 21:11 c412_meqrameh.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62842 Sep 13 21:12 c412_meq_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4665 Sep 13 21:12 c412_sedr_zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35561 Sep 13 21:12 c412_sedr_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35749 Sep 13 22:05 c442-fa8b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   26067 Sep 13 22:05 c442-fa8c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5703 Sep 13 22:04 c442-fa8.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17003 Sep 13 22:05 c442-samavar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14614 Sep 13 22:05 c442-samavar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep 13 22:04 c442-samavar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   38593 Sep 13 22:06 c442-symp-zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67256 Sep 13 22:05 c442-symp-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3627 Sep 13 20:54 crop14-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4873 Sep 13 20:54 crop18-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11820 Sep 13 21:11 crop411_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8609 Sep 13 21:11 crop411_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4088 Sep 13 21:11 crop411_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5339 Sep 13 21:28 crop419_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5380 Sep 13 21:28 crop419_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1676 Sep 13 21:28 crop419_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4192 Sep 13 21:28 crop419_d.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3506 Sep 13 21:29 crop419_grk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4444 Sep 13 21:29 crop419_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25580 Sep 13 21:26 crop428a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6915 Sep 13 21:26 crop428b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54756 Sep 13 21:26 crop428c.png
-rw-rw-r-- 1 sfmqrb sfmqrb   48027 Sep 13 21:26 crop428d.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12740 Sep 13 21:36 crop-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36288 Sep 13 22:32 crop460-fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5500 Sep 13 22:30 crop460-latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18309 Sep 13 22:31 crop460-mithere.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep 13 22:31 crop460-shamunhdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3606 Sep 13 22:30 crop460-shamun.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78410 Sep 13 22:32 crop468a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44719 Sep 13 21:39 e0-434.json
-rw-rw-r-- 1 sfmqrb sfmqrb   20203 Sep 13 20:57 edit_about.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6853 Sep 13 21:12 edit_research.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep 13 21:14 ffprof
-rw-rw-r-- 1 sfmqrb sfmqrb   49815 Sep 13 21:44 gen-420.py
-rw-rw-r-- 1 sfmqrb sfmqrb 1434288 Sep 13 21:31 irn-425.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  200105 Sep 13 21:31 irn-425.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  929137 Sep 13 22:03 kent2-448.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     146 Sep 13 22:03 kent-448.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep 13 21:57 knt-440.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep 13 21:58 knt443.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   45281 Sep 13 21:58 meta-443-knt.json
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep 13 22:33 oew459.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   44198 Sep 13 22:46 part1-471.json
-rw-rw-r-- 1 sfmqrb sfmqrb  120893 Sep 13 20:58 pg390b.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   39607 Sep 13 20:58 pg390b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  113843 Sep 13 20:57 pg391big.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18836 Sep 13 20:57 pg391crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81140 Sep 13 20:57 pg391.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34659 Sep 13 20:58 pg391root.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21174 Sep 13 20:58 pg391sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75438 Sep 13 20:56 pg392.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101976 Sep 13 20:57 pg393.png
-rw-rw-r-- 1 sfmqrb sfmqrb  145431 Sep 13 20:54 pg394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96039 Sep 13 20:53 pg394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72433 Sep 13 20:54 pg397.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77067 Sep 13 20:55 pg398.png
-rw-rw-r-- 1 sfmqrb sfmqrb   85891 Sep 13 21:00 pg399-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45417 Sep 13 21:00 pg399-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64776 Sep 13 20:54 pg399.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43498 Sep 13 21:00 pg399-sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb  167174 Sep 13 20:58 pg400big.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24547 Sep 13 20:58 pg400_fa_heli.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23086 Sep 13 20:58 pg400_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14689 Sep 13 20:58 pg400_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32600 Sep 13 20:58 pg400_kasak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35662 Sep 13 20:58 pg400_kasak3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22852 Sep 13 20:58 pg400_kasak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79028 Sep 13 20:57 pg400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70671 Sep 13 21:01 pg402.png
-rw-rw-r-- 1 sfmqrb sfmqrb  136264 Sep 13 20:56 pg404hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71542 Sep 13 20:56 pg404.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63962 Sep 13 20:58 pg405.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63610 Sep 13 20:57 pg406.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79866 Sep 13 20:59 pg407.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21327 Sep 13 20:55 pg408-ampus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33681 Sep 13 20:55 pg408-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78365 Sep 13 20:54 pg408.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37449 Sep 13 21:14 pg409.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100242 Sep 13 21:09 pg410hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18557 Sep 13 21:09 pg410-k2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17676 Sep 13 21:09 pg410-kadm2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6217 Sep 13 21:09 pg410-kadm.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7410 Sep 13 21:09 pg410-persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65183 Sep 13 21:08 pg410.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23704 Sep 13 21:09 pg410-q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1736 Sep 13 21:09 pg410-qedam.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64940 Sep 13 21:11 pg411_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56566 Sep 13 21:10 pg411.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161139 Sep 13 21:11 pg412_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74221 Sep 13 21:11 pg412.png
-rw-rw-r-- 1 sfmqrb sfmqrb  481466 Sep 13 21:14 pg412_uhi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35423 Sep 13 21:09 pg413.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36532 Sep 13 21:12 pg414-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74486 Sep 13 21:12 pg414.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3823 Sep 13 21:16 pg415-emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78342 Sep 13 21:16 pg415hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73449 Sep 13 21:11 pg415.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39289 Sep 13 21:17 pg416-v.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55756 Sep 13 21:17 pg417.png
-rw-rw-r-- 1 sfmqrb sfmqrb  178105 Sep 13 21:15 pg418hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87213 Sep 13 21:15 pg418.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28628 Sep 13 21:15 pg418-raj2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13818 Sep 13 21:15 pg418-raj3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6734 Sep 13 21:15 pg418-rajidan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  114625 Sep 13 21:28 pg419_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79366 Sep 13 21:26 pg419.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72677 Sep 13 21:27 pg420b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66620 Sep 13 21:27 pg420.png
-rw-rw-r-- 1 sfmqrb sfmqrb   31408 Sep 13 21:27 pg421.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66285 Sep 13 21:29 pg422.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66328 Sep 13 21:27 pg423.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74989 Sep 13 21:24 pg424.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67629 Sep 13 21:26 pg426.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154381 Sep 13 21:26 pg428hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61436 Sep 13 21:23 pg428.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7200 Sep 13 21:23 pg429-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7703 Sep 13 21:23 pg429-crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4400 Sep 13 21:23 pg429-crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168822 Sep 13 21:23 pg429hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78202 Sep 13 21:23 pg429.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81124 Sep 13 21:24 pg431.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92551 Sep 13 21:33 pg432.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74286 Sep 13 21:24 pg433.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46452 Sep 13 21:28 pg435-n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42245 Sep 13 21:28 pg435-n4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89932 Sep 13 21:28 pg435.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66400 Sep 13 21:31 pg436.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60815 Sep 13 21:36 pg437-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153828 Sep 13 21:36 pg437hi-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100480 Sep 13 21:42 pg438.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82782 Sep 13 22:03 pg439.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75018 Sep 13 22:03 pg440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  174306 Sep 13 22:04 pg442hi-442.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84851 Sep 13 22:03 pg442-p442.png
-rw-rw-r-- 1 sfmqrb sfmqrb  496661 Sep 13 22:06 pg442uhi-442.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77924 Sep 13 21:59 pg443.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70076 Sep 13 21:57 pg444.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24437 Sep 13 22:00 pg444-serom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   19924 Sep 13 22:00 pg444-sibum.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11542 Sep 13 22:00 pg445-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74593 Sep 13 22:00 pg445.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47049 Sep 13 22:03 pg446.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43874 Sep 13 22:04 pg447-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69608 Sep 13 22:04 pg447.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75433 Sep 13 22:04 pg449.png
-rw-rw-r-- 1 sfmqrb sfmqrb  145450 Sep 13 22:01 pg450hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11427 Sep 13 22:01 pg450-pechkam.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79151 Sep 13 22:00 pg450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11602 Sep 13 22:01 pg450-shangarf.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82815 Sep 13 22:05 pg451.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63836 Sep 13 21:59 pg452.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78966 Sep 13 21:58 pg453.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74797 Sep 13 22:01 pg454.png
-rw-rw-r-- 1 sfmqrb sfmqrb  102312 Sep 13 22:00 pg456-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70887 Sep 13 22:00 pg456hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33661 Sep 13 21:58 pg456.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34197 Sep 13 22:05 pg457_crop3b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21717 Sep 13 22:05 pg457_crop3c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4990 Sep 13 22:04 pg457_crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  144439 Sep 13 22:04 pg457hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79186 Sep 13 22:04 pg457.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43086 Sep 13 21:58 pg458.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68729 Sep 13 22:30 pg459.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84070 Sep 13 22:30 pg460hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80591 Sep 13 22:30 pg460.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14451 Sep 13 22:29 pg462-fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb  146281 Sep 13 22:29 pg462hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60489 Sep 13 22:29 pg462.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29574 Sep 13 22:30 pg462-sog2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20304 Sep 13 22:29 pg462-sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62814 Sep 13 22:30 pg463-v.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77174 Sep 13 22:32 pg464.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50604 Sep 13 22:30 pg465.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18202 Sep 13 22:31 pg466-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18603 Sep 13 22:31 pg466-crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15010 Sep 13 22:31 pg466-crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77713 Sep 13 22:31 pg466hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16928 Sep 13 22:32 pg466-osqof.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53053 Sep 13 22:30 pg466.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73548 Sep 13 22:31 pg467.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115827 Sep 13 22:32 pg468hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81319 Sep 13 22:32 pg468.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36109 Sep 13 22:37 pg469.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75634 Sep 13 22:34 pg470.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73795 Sep 13 22:35 pg471.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10610 Sep 13 22:31 pg472-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96623 Sep 13 22:31 pg472hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60397 Sep 13 22:31 pg472.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72343 Sep 13 22:34 pg473.png
-rw-rw-r-- 1 sfmqrb sfmqrb  106745 Sep 13 22:48 pg474.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54581 Sep 13 22:48 pg474-sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67658 Sep 13 22:32 pg475.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61025 Sep 13 22:37 pg476.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84381 Sep 13 22:29 pg477.png
-rw-rw-r-- 1 sfmqrb sfmqrb   94168 Sep 13 23:10 pg479.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100595 Sep 13 23:09 pg484.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89081 Sep 13 23:09 pg486.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73288 Sep 13 23:10 pg490.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107265 Sep 13 23:11 pg494hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72008 Sep 13 23:10 pg494.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4527 Sep 13 23:11 pg494-root.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3272 Sep 13 23:11 pg494-tambour.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69092 Sep 13 23:11 pg497.png
-rw-rw-r-- 1 sfmqrb sfmqrb  160787 Sep 13 22:36 pla18-468-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  335113 Sep 13 22:36 pla18-468.png
-rw-rw-r-- 1 sfmqrb sfmqrb       0 Sep 13 23:08 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  387279 Sep 13 21:13 sem410.html
-rw-rw-r-- 1 sfmqrb sfmqrb   59726 Sep 13 21:14 u_mak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49161 Sep 13 21:14 u_meq.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34177 Sep 13 21:14 u_sedr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47858 Sep 13 21:06 write397.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59484 Sep 13 21:11 write-402.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43710 Sep 13 21:22 write409.py
-rw-rw-r-- 1 sfmqrb sfmqrb   28665 Sep 13 21:19 write410.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47575 Sep 13 21:42 write436.py
-rw-rw-r-- 1 sfmqrb sfmqrb   54336 Sep 13 22:52 write469.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51859 Sep 13 22:52 write476.py
```


## [2026-09-14T03:11:26.786Z] TOOL CALL #19: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg497.png"
}
```


### [2026-09-14T03:11:27.558Z] TOOL RESULT

```

```


## [2026-09-14T03:11:27.552Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T03:11:40.318Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg497.png')\nprint(im.size)\nim.crop((950,1350,1950,1440)).resize((3000,270)).save('c497-shakuk.png')\nim.crop((950,1580,2000,1680)).resize((3150,300)).save('c497-arabic.png')\n\""
}
```


### [2026-09-14T03:11:41.705Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-14T03:11:43.820Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c497-shakuk.png"
}
```


### [2026-09-14T03:11:43.941Z] TOOL RESULT

```

```


## [2026-09-14T03:11:43.939Z] INPUT

[Image: original 3000x270, displayed at 2000x180. Multiply coordinates by 1.50 to map to original image.]


## [2026-09-14T03:11:57.172Z] TOOL CALL #22: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T03:11:57.180Z] TOOL RESULT

```


```


## [2026-09-14T03:11:59.599Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/taraxacum",
 "prompt": "Give the full etymology of taraxacum (Latin/New Latin and English), including any Arabic and Persian intermediaries."
}
```


## [2026-09-14T03:12:01.179Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%84%D8%AE",
 "prompt": "Give the Persian entry for تلخ (talx): etymology, Middle Persian form, Proto-Iranian reconstruction, cognates, and any cited sources."
}
```


### [2026-09-14T03:12:03.309Z] TOOL RESULT

```
I cannot provide the full etymology you're requesting based on the content above. The Wiktionary page for "taraxacum" does not include an etymology section detailing the word's origins through Latin, New Latin, Arabic, or Persian intermediaries.

The page only defines taraxacum as either "the dried root of the dandelion once used as a tonic" or "a plant of the genus _Taraxacum_" (with dandelion listed as a synonym), but it contains no etymological information tracing the word's linguistic journey through different languages.

To obtain this etymological information, you would need to consult the entry for the capitalized "Taraxacum" (the genus name) or access a more comprehensive etymological dictionary.
```


### [2026-09-14T03:12:06.527Z] TOOL RESULT

```
# Persian Entry for تلخ (talx)

**Meaning:** Bitter

**Etymology:** The word derives from Middle Persian *t'hl'* (taxl), which comes from Proto-Indo-Iranian *\*tákram*. A cognate appears in Sanskrit *तक्र* (tákra), meaning "buttermilk mixed with water."

**Middle Persian Form:** t'hl' (taxl)

**Proto-Iranian Reconstruction:** *\*tákram*

**Related Languages:** Northern Luri *تݖل* (təəl) shares the same root, demonstrating the term's distribution across Iranian language families.

**Source:** The etymology is cited from Manfred Mayrhofer's *Etymologisches Wörterbuch des Altindoarischen* [Etymological Dictionary of Old Indo-Aryan] (1992), volume I, pages 611-612.
```


## [2026-09-14T03:12:12.527Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Taraxacum",
 "prompt": "Give the full etymology of the Translingual/New Latin genus name Taraxacum, including Arabic and Persian intermediaries and any alternative Greek etymology."
}
```


## [2026-09-14T03:12:13.210Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Tatar",
 "prompt": "Give the full etymology entry for Tatar / Tartar."
}
```


### [2026-09-14T03:12:16.272Z] TOOL RESULT

```
# Etymology of Taraxacum

Based on the Wiktionary entry provided, the etymology is traced as follows:

The genus name derives from **Medieval Latin** *taraxacum*, which in turn comes from **Arabic** *طَرَخْشَقُون* (ṭaraḵšaqūn).

Unfortunately, the source document does not provide information about Persian intermediaries or alternative Greek etymologies. The entry only documents the Medieval Latin and Arabic connection, noting that the Arabic term is the ultimate origin of the scientific name used in taxonomy today.
```


### [2026-09-14T03:12:19.174Z] TOOL RESULT

```
# Etymology of Tatar/Tartar

According to the Online Etymology Dictionary, the entry for **Tatar** simply directs readers to "see Tartar," noting related forms include "Tataric" and "Tatarian."

The **Tartar** entry provides more detail. The term originates in the "late 14c., from Old French *tartre* and directly from Medieval Latin *tartarum*." It derives from "late Greek *tartaron* 'tartar encrusting the sides of wine casks,'" though the source remains uncertain—possibly Semitic in origin, though "Arabic is unlikely because of the early date of the word in Latin."

Initially, tartar referred to a "bitartrate of potash, sediment of potassium tartarate" deposited during fermentation. By the 17th century, the term applied more broadly to encrustations from liquid contact. The specific dental meaning—referring to "encrustation on teeth (calcium phosphate)"—was documented by 1806.

The refined form is known as "cream of tartar." The entry notes that Paracelsus's explanation for the name "probably is fanciful."
```


## [2026-09-14T03:12:24.051Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Tatar",
 "prompt": "Give the English etymology of Tatar (the people), including Persian, Medieval Latin, Old Turkic and Mongolic forms and any mention of \"Tata\"."
}
```


## [2026-09-14T03:12:25.656Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AA%D8%A7%D8%B1",
 "prompt": "Give the Persian entry تاتار: meaning and etymology (Turkic/Mongolic origin)."
}
```


### [2026-09-14T03:12:30.846Z] TOOL RESULT

```
# تاتار (Tatar) - Persian Entry

Based on the Wiktionary content provided, the Persian entry for **تاتار** is not explicitly detailed in this document. However, the page indicates that تاتار exists in Persian Wiktionary alongside Ottoman Turkish and Uyghur entries.

## Etymology

According to the etymological information provided for related language entries, the word derives from **"the Turkic name of a Tatar tribe."** The source notes direct readers to additional etymology details via the Wikipedia article on Tatars.

## Meaning

While the full Persian definition isn't specified in this excerpt, the Ottoman Turkish and Uyghur sections clarify that تاتار refers to:
- A member of the Tatar ethnic group
- A person associated with Tatarstan

The term functions as both a noun (denoting a person of Tatar ethnicity) and an adjective (describing something relating to Tatar culture or origin).
```


### [2026-09-14T03:12:32.478Z] TOOL RESULT

```
# English Etymology of Tatar

According to the Wiktionary entry, the English term "Tatar" derives "From Old Turkic 𐱃𐱃𐰺 (t¹t¹r¹)." The entry notes it is a "Doublet of Tartar and tartare."

The page references a Wikipedia article on Tatars for additional etymological details but doesn't provide direct quotes about Persian, Medieval Latin, or Mongolic forms within the English section itself.

However, the Turkish etymology section reveals broader linguistic history: the term comes "From Ottoman Turkish تاتار, from a Mongolic or Turkic name of a Khorezmian Turkic (Old Tatar) tribe." This suggests the term may have Mongolic origins, though the exact Persian and Medieval Latin connections aren't explicitly detailed in the provided content.

The entry does not specifically mention "Tata" as a form in its etymology.
```


## [2026-09-14T03:12:58.011Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WEB taraxacum\"; grep -n -i 'taraxacum' WEB_vol1.txt | head -10; echo \"=== WEB Tatar/Tartar headword\"; grep -n -i '^Tatar\\|^Tartar' WEB_vol1.txt | head; echo \"=== ls AHD\"; ls | grep -i -E 'ahd|watkins'; echo \"=== LKT tatar/taraxacum\"; grep -n -i 'tatar\\|taraxac\\|tarachs' LKT.txt | head -20"
}
```


### [2026-09-14T03:12:58.112Z] TOOL RESULT

```
=== WEB taraxacum
49085:dan/dé‘li-6n, n. [Fr. dent de lion, lit. tooth of the lion; from L. dens (dentis), tooth, de, of, and /eo, lion.] in botany, a common plant, Taraxacum officinale, having a milky, peren- nial root, naked stalk, deeply notched leaves, and a single large, yellow flower.
92204:l horse’ciir, n. 1.a streetcar drawn by a horse or horses, formerly used in the United States. 2. a car used to transport horses. | horse cas/sia (kash/ia), an East Indian legu- minous plant, Cassia marginata, bearing long pods which contain a black cathartic pulp, used as a horse medicine. rahe horse chest’/nut, a large nut, the fruit of Æsculus hippocastanum; also, the tree itself. horse’cloth, 7. a blanketlike covering for a orse’s back and loins. horse cours/ér, one who keeps horses to race; also, a dealer in horses. {Obs.] horse crab, the horseshoe crab. Ea, horse cre-val-lé (kre-val-1’), a fish, the cavally: rg $0 named in South Carolina to distinguish it x from the crevallé, a kind of horse mackerel. horse dev’il, atumbleweed of the southeastern nited States, Baptisia lanceolata, one of the Leguminosx: so named because when dried it is blown about and sometimes frightens horses, horse drench, 1. a dose of horse medicine. 2. a device for giving medicine to a horse. a horse el/dér, elecampane. horse em’met, same as horse ant. horse’finch, n. the chaffinch. [Brit. Dial.] horse’fish, 7.; pl. horse’fish, horse’fish-es, a fish, as (a) the moonfish, Vomer setipinnts; (b) the sauger; (c) a sea horse. horse’flesh, ». 1. the flesh of a horse, espe- cially as food. 2. horses collectively; as, he has made money in horseflesh. í Beischel ore; bornite, an ore of copper and iron which has a red color when broken, horse’fly, n.; pl. horse/flies, 1. any of a number of related large flies the female of peice sucks the blood of horses, cattle, etc.; gadfly. 2. any of various other flies troublesome to horses, as the botfly. horse’foot, n. 1. in botany, coltsfoot. 2. in zoology, the horseshoe crab. Sa horse ġen’tiăn, any of a number of weedy plants of the honeysuckle family, with op- pote leaves, inconspicuous flowers, and eathery fruit; feverroot. horse gow’An, the oxeye daisy, Chrysanthe- mum leucanthemum; also, the dandelion, Taraxacum officinalis, and other plants. horse gram, a leguminous tropical plant, 7 olichos biflorus, the pod of which is used in < southern India as food for horses and cattle. : Horse Guards, 1. a guard consisting of a body of Wea h «in England, the cavalry brigade formin, the household guard of the Enelsh OAT 3. the building opposite Whitehall, London, housing this guard and certain departments of the War Office. [Colloq,] Ue n. 1, the hair of horses, especially ‘that of the mane and tail used for stuffing furniture, cushions, etc. _ 2. haircloth; the stiff fabric woven of such
=== WEB Tatar/Tartar headword
=== ls AHD
AHD_watkins1985.txt
=== LKT tatar/taraxacum
148:Vrtinbery  Frini  Kultur  —  Hermann  Vamliery,  Die  primitive  Cultur  des  Turko- Tatarisciien  Volkes  auf  Grund  sprachliclier  Fursc-hungen  erörtert.  Leipzig  1879.
149:Vambery  TktElWb  =  Hermann  Vambery,  Etymoloj^isches  Vi^örterhuch  der turkotatarischen  Sprachen.  Ein  Versuch  zur  Darstellung  des  Familienverhält- nisses des  turkütatarischen  Wortschatzes.    Leipzig  1878.
160:afrz.  =  altfranzösisch äg.  =  ägyptisch  (Sprache  der  Hiero- glyphen) ags.  =  angelsächsisch ahd.  =  althochdeutsch ait.  =  altitalienisch angloind.  =  angloindisch ai)g.  =  altportugiesisch ar.  =  arabisch arag.  =  aragonesiscli aram.  =  aramäisch asp.  =  altspanisch ass.  =  assyrisch äth.  =  äthiopisch berb.  =  berberisch bulg.  bult^arisch cag.  =  cagataisch  (osttk.) 6ech.  =  Cechisch  (böhmisch) chin.  =  chinesiscli dän.  =  dänisch dtsch.  =  deutsch engl.  —  englisch linn.  =  finnisch frz.  =  französisch gen.  =  genuesisch germ.  =  germanisch gr.  =  griechisch  (altgr.) hebr.  =  hebräisch hind.  =  hindustani ind.  =  indisch it.  =  italienisch jap.  =  japanisch jav.  =  javanisch jid.  =r  jiddisch jud.-dtsch.  =  .jüdisch-deutsch kas.  tat.  =  kazantatarisch
177:tat.  =  tk. -tatarisch  venez.  =  venezianisch.
339:[Kelekian  Kämas  32]  'Sattel-  od.  I'ack- pferd,  Wallach'.  Hieraus  russ.  losad' 'Pferd'  u.  viele  Ableitungen,  klruss.  losa 'Pferd',  losak  'Maulesel',  poln.  loszak 'Pferd,  kleines  Tataren pferd'.  [Gorjajew 192.    Bern  SlEtWb  734.
375:b)  Mit  pers.  zädäl  'geboren,  Sohn' [Horn  NpEt  S.  143,  Nr.  645]  entstand pers.  ämirzädä  od.  verkürzt  tnirzä,  wört- lich 'Fürstensohn'.  Nachgesetzt,  be- zeichnet das  Wort  einen  'Prinzen  von Geblüt',  z.  B.  ßäsid  tnirzä  'Prinz  R.'. Vorgesetzt,  ist  das  Wort  der  Titel  eines gebildeten,  besonders  eines  schreibkun- digen Mannes;  am  bekanntesten  ist Bodenstedts  JVIIRZA  SCHAFFT,  pers. mirzä  säfi'.  —  Russ.  mirza,  murza 'tatarischer  Großwürdenträger',  vielleicl  it auch  mit  gerade  gegenteiliger  Bedeutung
378:nmrza  'Schmutzfink,  Aschenbrödel'.  — Rum.  )H jr^;ac 'TatarenhäupUing'.  [Löbel EITAP  64.
510:[Vielleicht  vom  Stamme  al  'fremd,  wild' Vämbery  TktEtWb  S.  14,  Nr.  14]  'Pferd'. Hieraus  rum.  hat  'Pferd'  in  der  Volks- poesie; bulg.  serb.  at  'Pferd,  Hengst'. Mit  pers.  pähn  'groß,  weit,  breit'  [Horn NpEt  S.  76,  Nr.  344]  wird  tk.  pehn-at 'großes  Pferd',  woraus  rum.  bahntet 'edles  tatarisches  Roß'  in  den  Volks- liedern der  Moldau,  russ.  klruss.  poln. bachmat  'dass.',   Adj,  (dial.)  bachmatif
1091:'Tuch,  gefütterter  Rock' ;  hieraus  russ. cekmen  'Kasaken-  oder  Bauernrock', klruss.  6ehmen,  cehman  'tatarisches  Ober- kleid', poln.  czekman  'dass.'.  —  Aus  der ost-  und  nordtk.  Entsprechung  [cagat. sükmän,  cuwas.  stihman]  wurde  rum. sucman,  suman  'Bauernkittel',  russ.  suk- man  'Tuchrock,  Kaftan',  klruss.  poln. sukmana  'Bauernkittel  aus  Tuch'.  [Gor- jajew  409.    Bern  SlEtWb  139.
1958:Aus  liakän  [das  wohl  selbst  aus  dem Mongolischen  stammt],  ist  I.Name  der türkischen  und  mongolischen  Herrscher Miltfl.isiens,  etwa  'Kniser',  '■2.  eine  Art Adelsprädikat  im  heutigen  Persien  und Transkaukasien;  das  Wort  wird  in  dieser Bedeutung  nachgestellt,  z.  B.  Jahjä  Hän; hieraus  rum.  han  'Tatarenfürst';  bulg. serb.  hau,  cech.  chär},  poln.  klruss.  chan, russ.  hnn,  kagan,  kogan  'Herrscher  der Chasaren';  frz.  kan,  khan;  dtsch.  Chan. [Bern  SIEtWb  468.
3081:'Name  eines  Kosakenstammes' ;  hieraus rum.  lipcan  'Tatare,  Ritter'.
4031:'Eine  Antilope  Antilope  saiga  Wagn.  = Colus  tataricus  Forst.';  hieraus  russ. saiga  'Antilope',  saigak  'wilde  Steppen- ziege', bulg.  saiga,  poln.  saiga,  cech. sajha;  dtsch.  Saigaantilope;  frz.  saiga.
4558:'Wilde  Zichorie';  hieraus  la*.  taraxacum 'Löwenzahn,  Leontodon  laraxacum',  frz. taraxacon;  eng),  taraxacum.  [Devic  DEt 216/il7.    Lammens  Rem  235.
4595:[Tk.  Tatar.
4597:2045.  Tk.  Tatar:
4598:N.  pr.,  Name  einer  grolsen  Verzvveii^ung des  Türkenstammes;  hieraus  u.  a.  dtsch. Taterkorn  'Buchweizen',  Tatarennach- richt 'falsche,  voreilige  Nachricht,  Ente' (so  genannt,  weil  während  des  Krim- krieges ein  tatarischer  iVIeldereiter  vor- zeitig die  Nachricht  vom  Falle  Sewasto- pols nach  Konstantinopel  brachte] ;  cech. kh'üss.  tatarka  'Buchweizen,  Heidekorn'; rum.  tärtäcii^a  'dass.,  Walzenkürbis', tätar  'Tatare,  Tatarenpferd',  tätarcä 'Tatarenstute,  Pelzmantel';  frz.  tartare im  Schneiderargot  von  Paris  'Lehrling, zweiter  Geselle'.  [Roth  ViFr  43/44. MWiD  III.
4783:'Großer  Stamm,  Volk;  Lager'  [vom Stamme  al,  ol,  iil  'groß,  hoch',  Vämbery TktEtWb  S.  1],  Nr.  11];  hieraus  bulg. ulus,  klruss.  ulus,  russ.  ulus  'Nomaden- lager', poln.  wlus  'Tatar'.  [Gorjajew  387. Mikl  SlEtWb  372.
5015:Ä'äW*  1102 Kaschmir  1116 Kaspar  1059 Kathay  841 Kaurimuschel  1 1 33 Kimono  1177 King-te-chen  1 060 Ä'itet  841 iCoZJ  1198 A'onafc  120!2 Ä'omn  1250 Xo<«M  1214 Kretschmur  825 Kretschmer  825 AV«s  1163 Krumir  1220 Kuskus  1267 Landow  80 Lawsonia  inerniis  867 Lazarus  1310 Leonfo/idon  taraxacum
5882:Tatarennachricht  2045 Taterkorn  2045 tätowieren  2047 tatuieren  2047 Ta^ze  2044 tanschieren  2050 Teckholz  1756 7V^  415
6693:tandour  2019 I  taraxacon  2025
```


## [2026-09-14T03:13:00.821Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TTS vambery tatar\"; grep -n -i 'tatar' incoming/TTS/TTS_pages.txt | head -20; echo; echo \"=== AFM طرخشقوق\"; grep -n 'طرخشق\\|طرخش' AFM_pages.txt AFM.txt 2>/dev/null | head -10; echo \"=== PLA\"; grep -n -i 'tarax\\|tarhaš\\|Zichorie\\|Wegwarte' incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-14T03:13:00.914Z] TOOL RESULT

```
=== TTS vambery tatar
6:TUMO- TATARISCHEN SPRACHEN.
18:TURKO-TATARISCHEN SPRACHEN.
24:        TURKO -TATARISCHEN WORTSCHATZES.
71:     Eine etymologische Darstellung des türkisch - tatarischen
86:turko -tatarischer Sprachen am meisten erschwert, das ist der
99:wir im Turko -Tatarischen gänzlich.     Es fehlt uns ein dies-
251:Kcrecen *)   (christliclieii Tataren),      auf den der arabisch-persische
274:     1) Ob das sogenannte Stoffwort in den turko - tatarischen
292:tatarskago jazika (Kasan 1876).
388:lehre der turko -tatarischen Sprachen gesagt, wäre es schwer,
393:wechselung in den turko-tatarischen Sprachen befolgt, werden wir
430:ste Theil des consonantalenVorraths im Turko-Tatarischen, unter-
555:änderung in den turko-tatarischen Sprachen anbelangt, im Ver-
617:den turko-tatarischen Sprachen volle Bekräftigung. Der Reich-
638:Turko-Tatarischen ohnehin formell und materiell durchsichtigen
646:diente, welche den turko-tatarischen Völkerelementen in specieller
767:zumeist an L. Budagow's           „ Sravnitelnij   Slovar turetzko - tatars
769:der turko-tatarischen Sprachen) gehalten. Es ist dies ein Werk,
776:gisischen,                        auch des Sibirisch -Tatarischen
787:gleichstehenden     östlichen   Gliedes      der turko - tatarischen Spra-

=== AFM طرخشقوق
=== PLA
12240:(8 - gasni:                      "Zichorie"                 aus    pers.        „Lk käsni         9,
12551:Ge-          käsni:             "Cichorium                Intybus,           Zichorie,          Endivie"              pers.      (el       käsni?,
```


## [2026-09-14T03:13:10.888Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT 4550-4562\"; sed -n '4548,4562p' LKT.txt; echo; echo \"=== LKT 4590-4600\"; sed -n '4590,4602p' LKT.txt"
}
```


### [2026-09-14T03:13:10.949Z] TOOL RESULT

```
=== LKT 4550-4562
'Metallischer  Klang,  Gepränge',  ebenso tk.  tantana  'Pomp,  Parade';  hieraus rum.  dandana  'Gepolter,  Lärm,  schlechte Angelegenheit'.
2021.  Tk.  tapkur:
'Kleines  Lederkoppel,  das  die  Schabracke des  Pferdes  festhält'  [Kelekian  Kämüs 787  b:  iäiÄ;är];  hieraus  rum.  <«/'<wr 'dass.'.
2022.  Pers.  tär:
'Faden,  Gewebe'  [Horn  NpEt  S.  82, Nr.  369],  ebenso  tk.;  hieraus  rum.  tearä 'Zetteln'  (Weberausdruck).
2023.  Ar.  taraf:
'Seite,  Gegend',  ebenso  tk.;  hieraus  rum. taraf a  'Schar,  Bande'.
2024.  Ar.  taraha:
'Entfernen,  beseitigen',  dazu  subst.  Intin. tarh  'Abzug';  hieraus  it.  prov.  tara, frz.  tare,  sp.  pg.  <a>-a,  rum.  dar«;  dtsch. Tara,  engl,  tare;  russ.  tara  'Abzug  vom Bruttogewicht',  also  'Verpackungsge- wicht'. [Zur  Lautgestaltung  beachte man,  daß  das  ar.  tarh  fast  wie  farak gesprochen  wird;  Ableitung  von  fürah scheint  daher  zweifelhaft,  vgl.  RUSKÄ in  Isl  XII,  234-/235.]  Hierhin  gehört auch  it.  tarocco,  dtsch.  Tarock  'ein  Kar- tenspiel'. [DE  313.  Eguilaz  304.  ML 8568.    GrSVociSic  247.
2025.  Ar.  turahsakun:
'Wilde  Zichorie';  hieraus  la*.  taraxacum 'Löwenzahn,  Leontodon  laraxacum',  frz. taraxacon;  eng),  taraxacum.  [Devic  DEt 216/il7.    Lammens  Rem  235.
2Ui6.  Tk.  tarak: 'Kamm'  [vom  Stamme  tal,  tar  'groß, geräumig  >  erweitern,  ausstreuen',  c'ag. tarak  'Kamm',  eigentlich  'Zerstreuer', Vämbery  TktEtWb  S.  162,  Nr.  176  II]; hieraus  rum.  tarac,  arac  'Reben-  und Weinpfahr,  därac  'Wollkratze,  Krempel'.
2027.  Kas.-tat.  tarakau: 'Schabe';   hieraus  russ.  tarukan,  cech. tarakan  'dass.',    vielleicht  auch  poln. karuczan.     [Gorjajew  360.     Mikl  SiEt Wl)  347  a.
2028.  Ar,  taran^nbin:
'Flüssige  pers.  Manna'  [aus  pers.  türiin- gubin:  tär  'feucht,  irisch'  Hoin  NpEt S.  85,  Nr.  382  und  änguhin  'Honig'  eben- da 8.29,  Nr.  124];  hieraus  sp.  terenia- bin,  frz.  tireniabin  \teremabin  in  Roma- nia  XXXV,  409;  s.  Behrens  Beilr  264] 'dass.',  fiz.  tringibin.  [DE  350.  Devic DEt  219/220.  Eguilaz  505.  Lammens Rem  239.

=== LKT 4590-4600
2043.  Tk.  tasnia:
'Riemen';  hieraus  rnm. tasma  'Hutband'; russ.  tasma  'Riemen',  tesma  'Band',  tes- jomka  'schmales  Zwirnband',  öech.  tas- ma, poln.  tasma,  tasiemka  'dass.'.
2044.  Pers.  täst:
'Becken,  Untertasse'  [Horn  NpEt  S.  87, Nr.  389],  ins  Arabische  als  täs,  täsa 'Schälchen'  übergegangen;   hieraus  it.
161
[Tk.  Tatar.
tazza  'Trink schale',  sard.  taza,  prov. tassa,  frz.  fasse,  sp.  pg:.  taza,  rum.  tas; dtsch.  Tasse,  (dial.  Bayern)  Tatze;  russ. taz  'Becken',  serb.  tas,  poln.  tasa.  [DE 349.    Eguilaz  504.    ML  8594.
2045.  Tk.  Tatar:
N.  pr.,  Name  einer  grolsen  Verzvveii^ung des  Türkenstammes;  hieraus  u.  a.  dtsch. Taterkorn  'Buchweizen',  Tatarennach- richt 'falsche,  voreilige  Nachricht,  Ente' (so  genannt,  weil  während  des  Krim- krieges ein  tatarischer  iVIeldereiter  vor- zeitig die  Nachricht  vom  Falle  Sewasto- pols nach  Konstantinopel  brachte] ;  cech. kh'üss.  tatarka  'Buchweizen,  Heidekorn'; rum.  tärtäcii^a  'dass.,  Walzenkürbis', tätar  'Tatare,  Tatarenpferd',  tätarcä 'Tatarenstute,  Pelzmantel';  frz.  tartare im  Schneiderargot  von  Paris  'Lehrling, zweiter  Geselle'.  [Roth  ViFr  43/44. MWiD  III.
2046.  Ar.  tatbika:
jSubst.  Infin.  II  von  tabitka  'bedecken'] ; hieraus  sp.  pg.  iabica  'eine  Platte  aus Eisen  oder  Kupfer,  um  eine  Öffnung zuzudecken',  sp.  der  leere  Raum  selbst, also  'Hohlraum',  Vb.  tahicar  'zumauern'. [DE  344.
2047.  Tahitisch  tatn:
Auch  tatau  'Zeichen,  Schrift.  Malerei', Vb.  'zeichnen,  lesen,  rechnen';  hieraus engl,  tattow,  tattoo,  dlsch.  tatuieren,  täto- wieren; frz.  tatouer.  [Die  Sitte  des  Täto- wierens kam  zu  uns  von-den  Marquesas- Inseln.]
```


## [2026-09-14T03:13:12.450Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- WEB last headwords\"; tail -c 3000 WEB_vol1.txt; echo; echo \"=== AFM search\"; grep -n 'طرخش\\|طرخ\\|شقوق' AFM_pages.txt | head -10"
}
```


### [2026-09-14T03:13:12.540Z] TOOL RESULT

```
--- WEB last headwords
gation ° OTt Or record of a scholarly investi-
Sy T Scientific study; a monograph. that ep), we Teport or record of happenings tion ang ise on the writer’s personal observa- ~~ Knowledge or special information; as,
Memoir. autobia ct the French Revolution; (b) an
Ole eetaphy Or autobiographical record; Society. ord of the transactions of a learned Oir-is memoirs. n. the art or act of writing oir- : mems Uist, 2. a writer of memoirs.
MS-rà. 3
WL; neut bivia, n.pl.; sing. mem.o-rab/i-lé,
mentioned? : Of memorabilis, worthy to be or remembered.) things worth
üse, b ; n ull, brite, tarn, up; cry, myth; cat, machine, ace, church, chord; gem, añger, (Fr.) boñ, as; this, thin; az
remembering or recording;
kept of suche eines: g; also, the record mem"6-ra-bil/i-ty, n. the qualit iti
ot being memorable, q y or condition mem/’6-ra-ble, a. [L. memorabilis, worthy to
be noticed or remembered, from memorare,
to remind.} worthy to be remembered; note-
worthy; celebrated; distinguished.
Syn.—great, striking, remarkable, con- spicuous, prominent, noticeable, illustrious, extraordinary, famous, distinguished.
mem/6-ra-ble-ness, n, the quality of being memorable.
mem/6-ra-bly, adv. in a memorable manner.
mem-o-ran/dum, z.; pl. mem:6-ran/dums, mem.-6-ran/da, [L. memorandum, neut. of memorandus, to be remembered, gerundive of memorare, to call to remembrance, to remind.]
1. (a) a short note written to help one re- member something or remind one to do something; (b) a record of events or observa- tions, especially one for future use.
2. an informal written communication, as from one department to another in a business office.
3. in business, a statement, made by the consignor, of the goods and terms of a con- signment sent with the privilege of return.
4. in diplomacy, a summary or outline of a subject under discussion, reasons for or against some action, etc,
5. in law, a short written statement of the em of an agreement, contract, or transac- ion.
mem’ō-rāte, v.t. to commemorate. [Obs.]
mem/6-ra-tive, a. commemorating or tending to preserve the memory of anything. (Rare.]
mé-m0/’ri-a, n. [L. memory.]
1. a shrine or reliquary containing relics of amartyr.
2. a chapel or church erected in memory of a martyr or confessor.
mé-m0/ri-4l, a. [OFr. memorial; L. memorialis, of or pertaining to memory, from memoria, memory.]
1. serving to help people remember some person or event; commemorative.
2. of memory.
mé-m0/ri-Al, n. 1. anything meant to help people remember some person or event, as a statue, holiday, etc.
2. a note or hint to assist the memory; a memorandum. [Obs.]
3. a written statement of facts submitted to a person or persons in authority, as to Congress; a statement of facts accompanied with a petition. à
4. memory; remembrance; that which is or may be remembered. [Obs.]
5. in diplomacy, an informal state paper, used in negotiations, and containing such documents as circulars sent to foreign agents, answers to the communications of amba
=== AFM search
2849:( الطرخآن) اسم االن الغرفت تمريبة ترشآة ٠قال‏ في البرهان القاطع : ܨ
2853:الطرخانية الى من يردي خدمة جلية عظيمة للدولة ٠فنكان‏ يصبح بذلك معائى من
2856:( الطرخون ) نبات ُيَكْبّس في ܐܘ والملح واللبن واصل عروقه العاقر قرعا معرب
```


## [2026-09-14T03:13:24.972Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D8%A7%D8%AA%D8%A7%D8%B1/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for تاتار verbatim, including any origin tag in brackets, and also the Dehkhoda entry's statement of origin."
}
```


## [2026-09-14T03:13:26.210Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D9%84%D8%AE/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for تلخ verbatim, including any origin tag in brackets such as [په.], and any Pahlavi form given."
}
```


### [2026-09-14T03:13:31.156Z] TOOL RESULT

```
# فرهنگ معین Entry for تلخ

According to Mo'in's dictionary, the entry reads:

"(تَ) [په.] (ص.) ۱ - دارای مزة غیرمطبوع، بدمزه. ۲ - زننده، سخت، سخن تلخ. ۳ - تندخو، بدخلق."

The bracketed tag [په.] indicates a Pahlavi origin, with the entry defining the term as: (1) having an unpleasant taste or bad flavor; (2) harsh or severe (as in harsh speech); and (3) hot-tempered or ill-mannered.
```


### [2026-09-14T03:13:31.429Z] TOOL RESULT

```
# فرهنگ معین Entry

**Exact Quote (within 125 characters):**
"(اِ. ) نامی که در گذشته به مغول اطلاق می شد."

*Translation:* A designation historically applied to Mongols.

---

# Dehkhoda Dictionary Entry's Origin Statement

The Dehkhoda entry provides extensive historical context, stating that Tatar referred to a major tribal group from Turkestan whose origins traced to the descendants of Tatar Khan, brother of Mongol Khan. The entry notes various alternative spellings (Tatar, Tartar, Tartary) and explains how the term evolved from designating a specific people to becoming a general appellation for Mongol forces and later Turkic peoples more broadly during the 7th century AH/13th century CE Mongol conquests.
```


## [2026-09-14T03:13:42.155Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(733,741):\n    for ln in pages[i].split('\\n'):\n        if 'پهلوی' in ln or 'taxl' in ln or 'tahl' in ln:\n            print(i, ln.strip()[:200])\n\""
}
```


### [2026-09-14T03:13:43.212Z] TOOL RESULT

```
735 ۴ - پهلوی 28278) «بندهش ۱۳۷
```


## [2026-09-14T03:13:47.165Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AA%D9%84%D8%AE/' --note 'page 497, root Taxl, Mo\\'in entry تلخ shows [په.] Pahlavi origin tag' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AA%D8%A7%D8%AA%D8%A7%D8%B1/' --note 'page 497, root Tata, Mo\\'in/Dehkhoda entry تاتار = name applied to the Mongols' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AA%D9%84%D8%AE' --note 'page 497, Persian talx < MP taxl, Proto-Indo-Iranian *takra-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Tatar' --note 'page 497, English Tatar < Old Turkic tatar' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Taraxacum' --note 'page 497, Taraxacum < Medieval Latin < Arabic tarakhshaqun' 2>&1 | tail -3"
}
```


### [2026-09-14T03:13:48.288Z] TOOL RESULT

```
Exit code 1
(eval):1: unmatched '
```


## [2026-09-14T03:13:53.074Z] TOOL CALL #37: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%AA%D9%84%D8%AE/|page 497, root Taxl: Moin entry تلخ shows [pah.] Pahlavi origin tag\" \"https://abadis.ir/fatofa/%D8%AA%D8%A7%D8%AA%D8%A7%D8%B1/|page 497, root Tata: Moin/Dehkhoda entry تاتار = name applied to the Mongols\" \"https://en.wiktionary.org/wiki/%D8%AA%D9%84%D8%AE|page 497: Persian talx from MP taxl\" \"https://en.wiktionary.org/wiki/Tatar|page 497: English Tatar from Old Turkic tatar\" \"https://en.wiktionary.org/wiki/Taraxacum|page 497: Taraxacum from Medieval Latin from Arabic tarakhshaqun\"; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T03:13:58.302Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fc6c8d983905a266.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a2d379c9e96df22a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/98c477fca77769fd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/74c2ae4941baf3a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/04fe8dc0526b7bdc.txt
```


## [2026-09-14T03:14:02.891Z] TOOL CALL #38: WebSearch

```json
{
 "query": "Tatar ethnonym Old Turkic Orkhon inscriptions \"otuz tatar\" 732 etymology"
}
```


## [2026-09-14T03:14:03.787Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=Tatar",
 "prompt": "Give the American Heritage Dictionary entry for Tatar, especially its etymology line."
}
```


### [2026-09-14T03:14:07.104Z] TOOL RESULT

```
# Tatar - Dictionary Entry

**Definition:**
The entry defines Tatar as either "a member of a group of Turkic peoples primarily inhabiting Tatarstan" or "any of the Turkic languages of the Tatars," with an alternate historical sense referring to "Turkic and Mongolian peoples of central Asia."

**Etymology:**
According to the dictionary, the word traces back to "Persian _Tātār_, of Turkic origin."
```


### [2026-09-14T03:14:10.701Z] TOOL RESULT

```
Web search results for query: "Tatar ethnonym Old Turkic Orkhon inscriptions "otuz tatar" 732 etymology"

Links: [{"title":"Tatar confederation - Wikipedia","url":"https://en.wikipedia.org/wiki/Tatar_tribe"},{"title":"Tatar (term)","url":"https://en.wikipedia.org/wiki/Tatar_(term)"},{"title":"The Historical Meanings of the Term Tatar: a Critical and Comprehensive Examination - Lee - Golden Horde Review","url":"https://journals.rcsi.science/2308-152X/article/view/326386"},{"title":"Old Turkic","url":"https://en.wikipedia.org/wiki/Old_Turkic"},{"title":"Orkhon Turkic","url":"https://en.wikipedia.org/wiki/Orkhon_Turkic"},{"title":"(PDF) The Historical Meanings of the Term Tatar: a Critical and Comprehensive Examination","url":"https://www.researchgate.net/publication/393331183_The_Historical_Meanings_of_the_Term_Tatar_a_Critical_and_Comprehensive_Examination"},{"title":"Old Turkic script","url":"https://en.wikipedia.org/wiki/Old_Turkic_script"},{"title":"Orkhon inscriptions","url":"https://en.wikipedia.org/wiki/Orkhon_inscriptions"}]

Based on the web search results, here's what I found regarding the Tatar ethnonym in the Old Turkic Orkhon inscriptions:

The first precise transcription of the Tatar ethnonym was written in Turkic on the Orkhon inscriptions, specifically, the Kul Tigin (CE 732) and Bilge Khagan (CE 735) monuments as Otuz Tatar Bodun, 'Thirty Tatar clan' and Tuquz Tatar, 'Nine Tatar' referring to the Tatar confederation.

The Orkhon inscriptions, a group of 8th-century Old Turkic texts, include the first instances of the term (otuz tatar, toquz tatar), where it most probably referred to a group of Mongolian-speaking tribes. The Kül Tegin and Bilge Qaghan inscriptions list "the Otuz Tatar (Thirty Tatars)" as enemies of the Türks, along with the Qirghiz, the Khitan, and other Inner Asian peoples.

Regarding the etymology, the search results indicate the literal meanings: "Otuz" means "thirty" and "Tuquz" means "nine" in Turkic, so these terms refer to the numerical groupings of the Tatar confederation. However, the search results do not provide detailed information about the etymology of the word "Tatar" itself beyond these numerical designations in the inscriptions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:14:56.133Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN bitter\"; grep -n -i 'bitter' HRN.txt | head -20; echo \"=== HUB context 9534 / 8981\"; sed -n '8975,8990p' HUB.txt; echo '---'; sed -n '9528,9540p' HUB.txt; echo \"=== HUB 1640-1650\"; sed -n '1638,1650p' HUB.txt; echo \"=== ARY files\"; ls | grep -i ary; ls incoming/ARY 2>/dev/null | head"
}
```


### [2026-09-14T03:14:56.254Z] TOOL RESULT

```
=== HRN bitter
=== HUB context 9534 / 8981
vgl. zd. staxra-,
xr wird im Np. zu hr in : cahra 'Spinnrad' aus "^Saxrak,
vgl. carx *Rad'; Suhr-db, Suhr-asp H. 730 = surx 'roth*;
audi im Armenischen in Stahr (Agath., Laz. Pharp.
u. s. w.), syr. Istahr (ZDMG. 43, 407) = phi. Staxr (Stadt)
Gl. and Ind. 158.
xr und xtr wird im Np. auslautend zu tr in: talx
'bitter = phi. tOxr Dlnkart VI, Gloss, p. 2; Balx (Stadt)
= phi Baxr Vd. 1, 22, im Bdh. Balx, arm. Balx (Faustus
V. Byz.), syr. Balh (Inschr. 7. Jhd.), alter Baxfr- (oben
p. 194) = ap. Baxtris; auch mit hi: syr. ^r\2 N5ldeke,
Alexanderroman 14, 15, arm. Bahl Mos. Chor. 148 u. s.w.
c) xm = idg. km: daxm, daxma 'Dakhma' (Parsen-
wort!) = zd. daxma- H. 543; tuxm Same, Geschlecht' =
zd. taoxman-, pSz. tuxm, arm. tohm (aber ap. tauma-l);
haufiger wird xm schon zur Sassanidenzeit zu hm und mit Aus-
---
narx 'Preis', afgh. LW. nirx *Preis-
courant, Tarif , skr. ni + kri H. 1027.
In dem alten Namen Istaxr (Tab. p. 8
U.S.W.), Hauptstadt der Persis zur Sassa-
nidenzeit = phi. Staxr BB. 4,36, Gl. and
Ind. 158, arm. Stahr ist xr geblieben.
b) Ap. xr — np. lx\ talx 'bitter', paz. tahal (= tahl) =
phi. taxr Shk. 268, Dlnkart VI, Gl.
p. 2, afgh. trix^ fem. farxa; Balx,
arm. Balx, Balh (Faust us), Bald
(Mos. Chor. u. s. w.), phi. JSa/x- Bdh.,
Baxr vd. 1, 22, ap. Baxtri- (zd. baxdi-),
c) Ap. /r ~ np. rf: barf *Schnee* = phi. i;a/*r = zd. y«/n/- ;
=== HUB 1640-1650
389. Lies bal. tOs (statt tas).
391. Im Neupersischen wird tak und tag *Lauf (Fird.
I, 335, V. 302) genannt, vgl. afgh. LW. tak ^running
about', tag Vunning, gait, pace, walk'. tJber np. taj
'Krone = ap. Haga- s. oben Nr. 367.
Hierher: np. talx *bitter, paz. tahal = phi. taxr
Shk. 268, afgh. trl^, f. tarxa *bitter , pamir dial, trac,
trac (Geiger, Etym. und Lautl. des Afgh. Nr. 235).
Die persischen Fornien weisen auf iranisch *taxra-,
das vielleicht zu Nr. 394 geh5rt.
394. Ich stelle np. tanjtdan zusammenziehen' zu skr. tafiCf
faflj, pr. tanakti 'zusammenziehen*.
395. Dass tund *schnell, heftig, scharf, spitz' (Fird. Ill,
=== ARY files
NYB_vol2_glossary.txt
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
```


## [2026-09-14T03:14:57.545Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('leaf for line 593:', '\\n'.join(lines[:593]).count('\\f'))\nprint('leaf for line 1006:', '\\n'.join(lines[:1006]).count('\\f'))\n\""
}
```


### [2026-09-14T03:14:58.713Z] TOOL RESULT

```
leaf for line 593: 108
leaf for line 1006: 129
```


## [2026-09-14T03:15:15.364Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '593,600p' PHD.txt | cut -c1-1200; echo \"=== ARY تلخ\"; grep -n 'تلخ' ARY_pages.txt | head -10; echo \"=== ARY tatar\"; grep -n -i 'تاتار' ARY_pages.txt | head -5"
}
```


### [2026-09-14T03:15:15.453Z] TOOL RESULT

```
tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. ta
taxlih 83 102
~ih: bitterness. taxt [2А | N ~] throne. ~ag [-#! | N ~a] tablet, plank, (chess) board. taxtan, taz- [Phtn', tc- | M rem, tz-] run, flow. išnīh : flow. tāxtan, taz- [?Аїп!, Pc- | M Рс-, N ~] cause to run, flow; chase; pour. taxt-gàh [?hig’h | N <] couch. taz-, —išnih, v. taxtan. táz-, v. tāxtan, tazāģ [tc’k'] flowing, running. tāzānaģ [P enh | N tāz(y)āna] whip. tazënidan, tazën- [tcyn-ytn'] = tāxtan. tazidan, taz- [tc-ytn'] = taxtan. Itázig [Pcyk! | N tázi] swift, fast. "Táüzig [Pcyk! | N tāzi] Arab. tēmār [tym] | M tym’r, N ~] sorrow, grief, care. ltërag [tylk' | N tēra] dark, turbid. *térag [tylk'] (mountain) peak, summit. téx [tyh | N téy] sharp edge, ridge; ray. Mēz [tye | M tyz, N ~] quick. ~ih: speed. *téz [tye | (P tyj), N ~] sharp. ~ih: sharpness. *tidag [tytk' | (N dida)] pupil (of eye). tigr [HTY A < А Шу; tgl | M tygr, N tir] arrow. *tihóg [tyh:wk! | N tihi] small grey partridge. tir, v. tigr. Tir [tyl | M tyr, N ~] a god (confused with Tištar); astr. Mercury; cal. 4th month; 13th day. tis [MNDOM < А mnd‘m; ts | M, J tys] thing, affair. «iz [-c | M -yc] (with a negative) по... at all. tišn [tyšn!] thirst. tišna
tru(f)š 84 urwar
tru(f)Š [t/wu(p)$ | (P tryff), N turf] sour. truftag [t/wptk'] stolen; intercalary (days). tuhig [twhyk! | M twhyg, ЇЧ tuhi] empty, vain. ~ih : emptiness, void. tumbag [twmbk' | N ~a] drum. tund [twnd | N ~] sharp, violent. ~ih: violence, vehemence. Tür [twl | N ~] one of a people inimical to Eran, Turanian. ~ап [—n! | N ~] (land of) the Turanians. Turk [twlk' | N ~] Turk. tu&t [twst'] silent. tuwān [twb!n! | M twn, N ~] might, power. ~ (+infinitive): it is possible to, one can. ~ag [~k' | N —a] mighty, able. «gar [-kl | N ~] rich. ~garih: richness, wealth. ~ig [-yk'] able. ~igih: ability, power. --sāmān [-s’m’n'] the extent of one’s ability. tuxšáé [twhPk! | M рох р, N tuxsa] diligent. “Аһ: diligence, endeavour. tuxšīdan, tux&- [гол у! | (M. twxf‘yst), N ~] strive, endeavour. ~išn: endeavour, striving.
U
u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
urwāzistan 85 wādbān
=== ARY تلخ
ugrep: warning: ARY_pages.txt: No such file or directory
=== ARY tatar
ugrep: warning: ARY_pages.txt: No such file or directory
```


## [2026-09-14T03:15:28.203Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n 'تلخ' ARY_pages.txt | head -10; echo \"=== latin index\"; grep -n -i 'talx\\|taxl' ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T03:15:28.269Z] TOOL RESULT

```
3407:نورس کهن (۸0738 ۰:01 88077118 ایرلندی کهن (تلخنق! 012): 8727۸3
5657:فارسی (۳8۶/4۷). ۰ ترخینه, تلخینه, ترخنه (به چم "آب کشک)
6852:چم این واژه در زبان‌های رومانس (برگرفته از لاتین): تلخ :
6853:چم این واژه در زبان آلبانی: تلخی. ۰
=== latin index
```


## [2026-09-14T03:15:30.907Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D9%84%D8%AE-%DA%86%DA%A9%D9%88%DA%A9/",
 "prompt": "Is there an entry for تلخ چکوک (talx-chakuk)? Quote the Dehkhoda / Borhan definition and any mention of the Arabic طرخشقوق."
}
```


### [2026-09-14T03:15:31.922Z] TOOL RESULT

```
The server returned HTTP 410 Gone.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T03:15:36.204Z] TOOL CALL #45: WebSearch

```json
{
 "query": "\"تلخ چکوک\" طرخشقوق کاسنی دهخدا"
}
```


### [2026-09-14T03:15:43.034Z] TOOL RESULT

```
Web search results for query: ""تلخ چکوک" طرخشقوق کاسنی دهخدا"

Links: [{"title":"معنی تلخ | لغت‌نامه دهخدا","url":"http://www.vajehyab.com/dehkhoda/%D8%AA%D9%84%D8%AE"},{"title":"گنجور » خاقانی » دیوان اشعار » قصاید » شمارهٔ ۱۶۸ - هنگام عبور از مداین و دیدن طاق کسری","url":"https://ganjoor.net/khaghani/divankh/ghasidekh/sh168"},{"title":"طرشقون - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%B7%D8%B1%D8%B4%D9%82%D9%88%D9%86/"},{"title":"معنی کاسنی | واژه یاب","url":"https://vajehyab.com/?q=%DA%A9%D8%A7%D8%B3%D9%86%DB%8C&s=9&t=like"},{"title":"Culture Matters in Toxic Language Detection in Persian","url":"https://arxiv.org/pdf/2506.03458"},{"title":"آنا دیلی آموزش زبان ترکی آذری | دی ۱۳۹۱","url":"https://turkishdili.blogfa.com/1391/10?p=2"},{"title":"کپسول قاصدک (دندل هرب) - شرکت نیک داروی شفاساز امیران","url":"https://ndsaco.com/product/dandelherb/"}]

I've performed a web search for your query. The search results contain Persian dictionary entries and information related to the terms in your query.

Based on the search results, I found relevant information about these Persian terms:

**تلخ (Talakh):** Something that has an unpleasant and disagreeable taste, with various figurative meanings related to bitterness.

**طرخشقوق/طرشقون (Tarkhshaqooq/Tarshaqoon):** This is a plant also known as dandelion (Taraxacum officinale), and is referred to by names such as گل قاصد, قاصدک, هندباء بری, کاسنی بری, and دندان شیر.

**کاسنی (Kasni):** A self-seeding plant with crinkled leaves, a short stem, and blue flowers whose root, leaves, and seeds have medicinal uses.

All of these terms appear to be entries from **لغت‌نامه دهخدا (Dehkhoda Dictionary)**, one of the most comprehensive Persian dictionaries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:15:52.116Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \"https://www.ahdictionary.com/word/search.html?q=Tatar|page 497 node 2: AHD entry Tatar 'from Persian Tatar, of Turkic origin'\" \"https://en.wikipedia.org/wiki/Tatar_(term)|page 497 root Tata: history of the ethnonym Tatar, Orkhon inscriptions 732 CE\" \"https://abadis.ir/fatofa/%D8%B7%D8%B1%D8%B4%D9%82%D9%88%D9%86/|page 497 node Arabic tarax-shaquq: Dehkhoda tarkhashquq = dandelion/wild chicory\"; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T03:15:54.890Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/aafba3e30dcf8c9e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/07992fdf18aad4ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/869345dbf4a96f85.txt
```


## [2026-09-14T03:16:01.252Z] TOOL CALL #47: Bash

```json
{
 "command": "head -c 4000 /home/sfmqrb/git/rishe/data/verification/sources/web/07992fdf18aad4ee.txt; echo; echo ===; grep -n -i -m 20 'etymolog\\|Tata\\b\\|Da Da\\|Dada\\|Chinese' /home/sfmqrb/git/rishe/data/verification/sources/web/07992fdf18aad4ee.txt | head -30"
}
```


### [2026-09-14T03:16:01.321Z] TOOL RESULT

```
Exit code 1
URL: https://en.wikipedia.org/wiki/Tatar_(term)
FETCHED: 2026-09-14T03:15:53Z
STATUS: 200
TITLE: Tatar (term) - Wikipedia

Tatar (term) - Wikipedia 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Contents 
 Current events 
 Random article 
 About Wikipedia 
 Contact us 

 Contribute

 Help 
 Learn to edit 
 Community portal 
 Recent changes 
 Upload file 
 Special pages 

 Search 

 Search 

 Appearance 

 Donate 

 Create account 

 Log in 

 Personal tools 

 Donate 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 (Top)

 1 
 History 

 2 
 References 

 3 
 Bibliography 

 Toggle the table of contents 

 Tatar (term) 

 Add languages 

 Add links 

 Article 

 Talk 

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
 Switch to legacy parser 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Wikidata item 

 Appearance

 move to sidebar 
 hide 

 From Wikipedia, the free encyclopedia

 Term

 Tatar is a term whose meaning has varied throughout history. 

 History
 [ edit ] 

 The Orkhon inscriptions , a group of 8th-century Old Turkic texts, include the first instances of the term ( otuz tatar , toquz tatar ), where it most probably referred to a group of Mongolian -speaking tribes. Certain western groups of these tribes were later associated with Turkic tribes. Although the Tatar confederation was a longtime archenemy to Genghis Khan and his ancestors, later sources employed the term for most Mongol conquerors, the reason for which remains unclear. [ 1 ] 

 In the year 1236, according to a Russian annalist: "there came from the countries of the East into the Bulgar lands the godless Tatars and sacked the good city of Bolgar and killed everyone from the old to the young and the tiniest suckling". [ 2 ] It is likely the first time that the name Tatar was used in connection with the region. [ 3 ] In Russia and the rest of Europe , as well as India , Persia , and among the Arabs , the term continued to be used over the term Mongol . [ 4 ] 

 Within the Ottoman Empire , the term gained the new meaning of "court messenger", replacing ulak , coinciding with the undated establishment of the Tatar Corps ( Ottoman Turkish : Tatarān ocağı ), known to have undergone reorganization in 1775. [ 5 ] Several contemporary travelers and modern historians associated the rise of the term with the potential employment of Crimean Tatar refugees by the Ottoman government. [ 6 ] 

 References
 [ edit ] 

 ↑ Vàsàry 2005 , p.   9. 

 ↑ Bukharaev 2014 , pp.   118–119, "...but of the year 1236 the Russian annalist wrote with great sadness: 'In the autumn of 6744 (1236), there came from the countries of the East into the Bulgar lands the godless Tatars and sacked the good city of Bolgar and killed everyone from the old to the young and the tiniest suckling, and looted a lot of goods, and set the city on fire, and captured the whole of their land'". 

 ↑ Bukharaev 2014 , pp.   118–119. 

 ↑ Lane 2018 , p.   11. 

 ↑ Koh 2024 , p.   49. 

 ↑ Koh 2024 , pp.   49–50. 

 Bibliography
 [ edit ] 

 Bukharaev, Ravil (3 June 2014). Islam in Russia: The Four Seasons . Routledge. ISBN   978-1-136-80793-0 . 

 Koh, Choon Hwee (2024). The Sublime Post: How the Ottoman Imperial Post Became a Public Service . Yale University Press. ISBN   9780300270532 . 

 Lane, George (25 January 2018). A Short History of the Mongols . Bloomsbury Publishing. ISBN   978-1-78672-339-0 . 

 Vàsàry, Istvàn (24 March 2005). Cumans and Tatars: Oriental Military in the Pre-Ottoman Balkans, 1185–1365 . Cambridge University Press. ISBN   9781139444088 . OCLC   750757219 . 

 Retrieved from " https://en.wikipedia.org/w/index.php?title=Tatar_(term)&oldid=
(eval):1: == not found
```


## [2026-09-14T03:16:19.393Z] TOOL CALL #48: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:508 --image 2>&1 | tail -30"
}
```


### [2026-09-14T03:16:20.504Z] TOOL RESULT

```
no scan of BQT covers printed page 508 (see 'scans' in refs_online.json)
```


## [2026-09-14T03:16:34.297Z] TOOL CALL #49: WebSearch

```json
{
 "query": "\"تلخ شکوک\" OR \"تلخ چکوک\" کاسنی صحرایی برهان قاطع"
}
```


### [2026-09-14T03:16:40.441Z] TOOL RESULT

```
Web search results for query: ""تلخ شکوک" OR "تلخ چکوک" کاسنی صحرایی برهان قاطع"

Links: [{"title":"گنجور » محتشم کاشانی » دیوان اشعار » قصاید » قصیدهٔ شمارهٔ ۱۰ - در مدح میر محمدی خان فرماید","url":"https://ganjoor.net/mohtasham/divan-moh/ghaside-moh/sh10"},{"title":"خرفه - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%AE%D8%B1%D9%81%D9%87/"},{"title":"برهان قاطع - ویکی فقه","url":"https://fa.wikifeqh.ir/%D8%A8%D8%B1%D9%87%D8%A7%D9%86_%D9%82%D8%A7%D8%B7%D8%B9"},{"title":"گنجور » کسایی » دیوان اشعار » سوگنامه","url":"https://ganjoor.net/kesayee/divank/sh1"},{"title":"آشنایی با خواص کاسنی؛ گیاهی معجزه‌گر - همشهری آنلاین","url":"https://www.hamshahrionline.ir/news/214678/%D8%A2%D8%B4%D9%86%D8%A7%DB%8C%DB%8C-%D8%A8%D8%A7-%D8%AE%D9%88%D8%A7%D8%B5-%DA%A9%D8%A7%D8%B3%D9%86%DB%8C-%DA%AF%DB%8C%D8%A7%D9%87%DB%8C-%D9%85%D8%B9%D8%AC%D8%B2%D9%87-%DA%AF%D8%B1"},{"title":"\"کاسنی\" گیاهی معجزه‌گر","url":"https://www.asriran.com/fa/news/273833/%DA%A9%D8%A7%D8%B3%D9%86%DB%8C-%DA%AF%DB%8C%D8%A7%D9%87%DB%8C-%D9%85%D8%B9%D8%AC%D8%B2%D9%87%E2%80%8C%DA%AF%D8%B1"},{"title":"برهان قاطع، قصه - ویکیجو | دانشنامه آزاد پارسی","url":"https://wikijoo.ir/index.php/%D8%A8%D8%B1%D9%87%D8%A7%D9%86_%D9%82%D8%A7%D8%B7%D8%B9%D8%8C_%D9%82%D8%B5%D9%87"},{"title":"Khollan Vafa : اخوان صفا: مداخل مخزن الادویه عقیلی خراسانی (هفتم) 1","url":"https://mvahdatid5gmailcom.blogspot.com/2016/07/1_28.html"},{"title":"اسوه ,موسسه فرهنگی قرآن و عترت اسوه تهران - کاسنی","url":"https://www.osveh.org/fa/zndgy-khwb/pages-2/behdasht-va-taghzieh/kasny"}]

Based on the search results, I found relevant information about your query. The term "چکوک" (Chakuk) appears as an alternative name in dictionaries including Burhan Qati (برهان قاطع), which is a Persian lexicographical source.

The term "کاسنی تلخ" (bitter chicory) is listed among the alternative names for chicory plant (کاسنی), which is also known as wild chicory or desert chicory (کاسنی وحشی - کاسنی صحرایی).

The root extract of chicory has a bitter taste, which aligns with the "تلخ" (bitter) descriptor in the search terms.

The search results indicate that both "تلخ شکوک" and "تلخ چکوک" appear to be variant names for bitter chicory or similar wild herbaceous plants referenced in classical Persian dictionaries and herbal texts, with "برهان قاطع" (Burhan Qati) being one of the historical lexicographical sources where these terms are documented.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:16:47.605Z] TOOL CALL #50: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg497.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/497.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head; echo ---; sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T03:16:47.727Z] TOOL RESULT

```
total 23572
drwxrwxr-x  2 sfmqrb sfmqrb  12288 Sep 13 23:16 .
drwxrwxr-x 14 sfmqrb sfmqrb   4096 Sep 13 22:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
---
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


## [2026-09-14T03:17:10.884Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 تاتار\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'تاتار' in p: print(i, [l.strip()[:120] for l in p.split('\\n') if 'تاتار' in l][:2])\n\" | head -10\necho \"=== HRN tatar\"; grep -n -i 'tatar' HRN.txt | head -5\necho \"=== HUB tatar\"; grep -n -i 'tatar' HUB.txt | head -5\necho \"=== SKT Tartar/taraxacum\"; grep -n -i 'tartar\\|taraxac' SKT.txt | head -10\necho \"=== FSD vol4 taraxacum/Tatar\"; grep -n -i 'taraxacum, n\\|^Tatar\\|Tartar,' FSD_vol4.txt 2>/dev/null | head -10; ls | grep FSD"
}
```


### [2026-09-14T03:17:12.135Z] TOOL RESULT

```
=== BQT v1 تاتار
216 ['تاتار گریشت بان جزیره آمد(4) » دوز عمرش']
680 ['تاتار ۴ در ورن ناچار » ولاتی است', 'حای ترکی ارخون ۲500(). نام دوطایفه ازتاتار بنام « سی\u200cتانار » و «نه\u200cتاتار» باد شده. درآن عصر']
=== HRN tatar
22958:apr. tatarwis 379.
=== HUB tatar
=== SKT Tartar/taraxacum
19187:Taraxaciun.  the  dandelion.  (Arab.) From  Arab,  tarazacart,  explnined  as  a  kind of  succory.  Pen.  tarJthashifUn,  wild  endive ; latinised  as/artumrMs^inAviccnna.  (Devic; sunp.  to  Lillr^.)
19214:—  Span,  tiritar,  to  shi^Tr,  shake  with Doubtless  from  a  lost  Latin  verb,  all Gk.  rapTtxpil*iV,  to  shake  vrith  cold Tartar  (3).
19215:Tartar  (i),  an  add  sail  in  casfa^  1 cretion  on  the  teeth.  ( F.  —  Low.  L.  -^^ A  term  due  to  the  alchemists ;  called  jn tre,  or  tartre,  in  Chaucer.  —  F.  tartn,  *  ii Cot.;  Low  L.  tartarmm.  —  Arab,  durd, i sediment  tartar  of  wine:  duriiy.  1 Cf.  Arab,  darad,  a  shedding  of  teeth; Devic  connects  with  tartar  on  the  lee
19216:Tartar  (a),  a  native  of  Tartary.  (1 A  per^'trse  spcllmg  of  Tatar,  owins popular  etymology  which  regarded  1 as  let  loose  out  of  Tartaruj  or  bd below).  From  Tdtar,  a  Tatar,  or  ii tant  of  Tatary  (as  it  should  be  spelt).
19217:Tartar  (.0,  TartarD*,  hell  (U  - '  The  gates  of  Tartar ; '  Tw.  Nt  II  *
19218:—  L.  Tartarus.  -  Gk.  Ttiprapoi,  Tai the  infemnJ   regions;    conceived, place  of  extreme  cold ;  cC  Gk- 10  shiver  with  cold.
22841:tacfu,  tail,  tang,  tap,  taper,  tare,  tart, tartar,  tassel,  tattoo,  tear.  teem,  templ^ temporal,  tend,  lender,  tense,  tent,  terrier^ the,  thee,  t/tere  {there),  thole,  thrumg thrush,  tick,  till,  tilt.  tip.  lire,  to-,  toasts  totl^ toll,  tool,  top,  tow,  trace,  trad,  Ira trepan,  trice,  tricJt,  trill,  trinket, trump,  tuck,  tuft,  turtle,  twig.
23695:Fremh  from  I-OW  Latin  from  Arabic'. camlet,  tartar  (1).
=== FSD vol4 taraxacum/Tatar
1383:fiameassvLTOFLEMON —s.  of  tartar,  potassiumcarbonate  ...
3037:mammals  as  certain  jmt-catcrs  anff^ce  of  a   scale  from  the areoutgrowthsoftheepidermis  lateral  line  of  Labrtehthyt 2,  A   structure  rc  -   taUclanus  shonjog  o   raucif. SCmbling  or  suggestive  of  crous  duct  (a),  ramifying  into a   scale  in  thinness  or  flatness,  fi'J'cvwl  orifices  on  the  surface on  various  invertebrates,  as  on  the  wings  of  butterflies, the  body  of  most  thy  snnuratis,  aea-micc,  etc  3.  A scale-insect  4.  One  of  tho  hard  scabs  resulting  from certain  human  diseases  as  leprosy  5   Bot  (1)  A   rudi- mentary or  metamorphosed  leaf,  as  those  covering  the leaf-buds  of  trees,  the  bulb,  cones  of  coniferous  trees, etc  (2)  Any  epidermal  outgrowth  having  cell-dimen- aions  in  two  planes,  as  the  pale©  on  the  young  parts  of some  ferns  (3)  A   tnehome  whose  terminal  cell  be- comes a   flat,  dry  disk  Often  the  disk  becomes  stellate, as  m   Olcaccx  (4)  A   catnphy  Ilary  leaf  which,  tho  hav- ing no  assimulatmg  function,  is  important  protectively as  a   bud-scale,  as  in  the  horse-chestnut  (5)  Any  thin ecanoua  structure,  usually  a   degenerate  leaf  C.  Mech (1)  The  coating  of  oxid  that  forms  on  iron  and  some other  metals  when  heated,  and  comes  off  m   the  proc- esses of  forging  rolling,  etc  variously  called  rorge»scaIe, hainmcF'S  ,   iron><  »   mill  s   ,   roll  s   »   etc  (2)  An  incrus- tation that  forms  on  the  Inside  of  boilers  etc  ,   and  consists chiefly  of  the  stable  soluble  salts,  as  thoso  of  calcium  and magnesium  contained  la  water  (3)  The  ornamental  cov- ering outside  of  the  shell  of  a   pocket-’knlfe 7.  Tartar,  as  on  the  teeth  8   Any  hard,  thin,  scale- like  formation,  as  a   flake,  husk,  she)),  pod,  or  exfolia- tion 3.  Crude  paraffin  wax.  obtained  by  filtering  the cooled,  heavy  distillates  from  petroleum  or  shale Stavdabd  Oil  Company  Letler  to  Standard  Did  Oct 25,  ’ll  f<.AS  sceale.  scade]
30985:tar'tar*,  1   tor'tsr,  2   tar'tar,  n   1,  The  roughly  punfied cnist  of  argol  intermediate  between  crude  argol  and cream  of  tartar  See  cream  op  tartar,  under  cre  vm and  ABGOu  2.  A   yellowish  incrustation  that  forms  on the  teeth,  consisting  chiefly  of  calcium  phosphate  [< F   tartre  <   LI^  tartarun  <   Ar  dwd  dregs  j   —   tartar emetic,  a   white  crystalline  potassium  antlmonlous  tartrate (KSbOC^HiOO,  with  a   sweet  afterward  disagreeable  metal- lic taste  In  medicine,  chiefly  an  emetic  (poisonous  In  large doses)  and  In  calico-printing  and  *dj  elng  as  a   mordant  — ‘tar'tar-lsh,  a   [Rare  I   Same  as  tartarous*.  2 Tar'tar*,  a   &   n   Same  as  Tatar  the  usual  spellmg  in
30991:tar-ta're-ous*,  1   tor-te'n-us,  2   tar-ta're-tis,  a   1.  Hav-  Tasch  e-rcao,  1   ta^'e-rS  2   t^h'e-rO,  n   1.  ElzCar  Alex- ing  the  nature  of  tartar,  resembling  tartar  2.  Bot  (/i7lS-0-/ijl89S),  a   Canadian  cardliml,  a^blahop
31066:Any  mode  of  dress  not  suited  to  the  employ  ment,  the  age,  the  Tartar,  1   n
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
```


## [2026-09-14T03:17:23.794Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[680])\n\" | head -60"
}
```


### [2026-09-14T03:17:24.915Z] TOOL RESULT

```
تايه زر - یواح
ناتلی » بکسر ثالث بر ءزن غافلی »
سفره ودستار خوان‌را گویشد.
تاتوره بر وزن ماشوره ؛ چدار؟
و نجاوي باشد ازآهن ورسمان که بردست‌و پای
که مانند ماهی درمیان تایه 3 روغن برشته کرده
سیر وس رکه برآن زده ب‌اشند .
یابزر بفتح زای هوز وسکون رای
فرشت ۰ کنا.ه از | فتاب عالمتاب اسضت: ج
قالین ۱ - بر وزن‌خواییین » بمعنی | اسب وامتر گذارند؟ ۰
درخشیدن - وتاب و طافت- آوردن - و تافتن تا تول بروزن شاقول» شخصی‌را گویند
ویچیدن باشد . که دهان او کج شده باشد.
اقا سب تای قرشت‌بروزنکاا « گرفنگی افیا » با فوفانی بتحتانی رسیده و نون
ولکنت زبان را گویند . بالف کشیده . بلغت بربری باشه را گونند» وآن
تاتار ۴ در ورن ناچار » ولاتی است
که مك خوب از نجاآورند- و نرکان آنجا را
نیز گویند :
مرغیست شکاری از جنس زرد چشم وآلرا بعر یی
آبوعماره خواننف. ود شت‌ومرا بخته وخشك کرده
ایند و سه روز با آب سرد خورند » سرفه را
از: تاب (< .) + بدن ( علامت صدر )  .‏ اسم‌صوت. ۴ - وتر 12/۵۲
وتار؟۵]2) .نام فومی است.بقول نامسن10 11101086 درفرن هشتم مبلادی(دوم هجری) د رکنیبه.
حای ترکی ارخون ۲500(). نام دوطایفه ازتاتار بنام « سی‌تانار » و «نه‌تاتار» باد شده. درآن عصر
مراد ازنام مذ کور مفول بابخشی ازمفول بود نه قومی تركك و بقول تامسن این تاناران در جنوب
غرمی با یکال 221121 تاحدود ناحیهُ کرول ألا6۳* سکنی داشتند.
طرد ترکان از مقولستان کنونی و پیشرفت قبابل مفول مرتبط با تأسیس حکومت ۱
(قراخنائیان) است. محمودکاشغری(در نیمة‌دوم‌قرن پنجمه) که ازتاتار نم‌برده (۱۲۳۸1)] گاه‌بوده که
زبان تاتار جز زبان ترکی است ( آ. ۳۰ ) . بسض دمته های انار باقبایل‌فرك مثحد شدند و در
وی ری سای و گزبدند. در حدود المالم تاتاران متعلق به نغزغز دانسته شده‌اند . در
کتب مربوط بفتوحات مغول درفرن هفتم هجری همه جا (درچین وممالك اسلامی‌وروسیه واروپا)
آ نان بنام تا تارباد شده‌اند. این‌الاشر" (چاپ ترتب ,1611 ۱۷۸۰ ببعد» ٩۲۳بمد)‏ اسلاف چنگیز را
بدین نام میخواند . رشید الدین که کوباءاز مورد استعمال و وسمت مفهوم تاتار پیش از مفول ۰
آ گاهی نداشته. تاتار رافومی خاص‌بجزمفول میداند که حاکن بوبر نور ۲0۲[ ۲لا9 (در جنوب
ترفی کرولر ) بودند . ازعی فتوحات چنگیز » بسیاری از قبایل ثابع او بنام < مفول > خوانده
شد ند تاتاا ناناران بهمان اندازهٌ مفولان نیرومند بودند واز شجهت بسیاری از اقوام ان نم را
بخود بستند» از ابثرو است که امروز «در ختای » حندوسنان , چین, ماچن » قرفیزمتان » کلار
(لهستان) , باشفرد (هنگری) ۰ دشت قبجاق» ممالك شمالی اعراب بدوی» سوریه, مصر و معالك
مخرب‌تام تاناررا بهمهٌ اقوام ترك اطلاق کنند» . راك؛ دائرةالمعارف
اسلام : ناتار . بقلم بارتلد 2۲)/1010ظ .۰۷۷۰ در زیانهای ارویابی
6 کوند . ۴ رك. چدار .
۴ نیز نانوره 220012] کیاهی از تیرهٌ بادنجانیان
5 از کیاهان دولیهُ پبوسته کلب که . کیسولهای آن
دارای خار بسیار و بجدهار شاف ناژ مسشود . ماده سمی آن شام
6 ازمواه مخدر فوی است. « کل گلاب ۰ع۲».
```


## [2026-09-14T03:17:25.624Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -i \"Ta'tar[^|]\\{0,300\\}\" FSD_vol4.txt | head -5; echo \"---\"; grep -n -o -i \"Tatar[, ][^|]\\{0,250\\}\" FSD_vol4.txt | head -8; echo \"=== taraxacum FSD\"; grep -n -o -i \"taraxacum[^|]\\{0,300\\}\" FSD_vol4.txt | head -5"
}
```


### [2026-09-14T03:17:26.930Z] TOOL RESULT

```
31094:Ta'tar-j,  n   Same  as  Tartahy
31161:Ta'tar,  11  ta'tar,  2   ta'tar,  c   Of  or  pertaining  to  the  tat'ting*,  1   tat'iq,  2   tStlng,  n   1.  A   lace-hke  knotted as,  a   taste  for  mathematics,  a   taste  for  music  C.  Stylo  Tar'tar,  /Tatars  or  Tartars,  their  language  religion,  threadwork  or  tnmming  made  by  hand 
---
10360:Tatar  j   Same  as  ahu
12108:Tatar  and  Japanese  faces  show  the  stetr-eyelids  of  the MoDgolian  race  F   B   TrLonAnihropologj/p  C3  [a  1881] 2.  Math  (1)  Having  distorted  symmetry,  some  elements on  opposite  sides  being  reversed  (2)  Distorted,  awry  3. Laclung  
15600:Tatar  origin  resembling  the Samoyeda  and  Inhabiting  China  and  Siberia  near  the  source of  the  Yenisei  2   The  language  of  thc&e  peoples, so'ral,  1   sS'rel  2   sfl  ral  n   Chen  A   crj-stalllne  compound (AUCUHtOH  SOi)*)  obtained  b
29913:Tatar  djirasty  and  establish  a   native Chinese  dyna-ny  to  be  callrf  Te'-pfr"  (Great  Peace),  but was  crushed  by  the  *   e\  cr  victorious  army,’  o-ganiiedbythe American  general  F   T.  Ward  (died  1S62),  and  at  last  led by  Maior 
30380:Tatar  conqueror  of  India  and  Asia
30985:Tatar  the  usual  spellmg  in
31081:Tatar  or  Turldo
31082:Tatar djiiast3  (called  Manehu)  reigned  m   China Ethnoiofasta  well  know  that  the  name  of  the  so-called  ^Tartar* race  ns  propcrii  Tatar  and  they  are  now  endeavounn*:  to  restore this  i.a  correct  orthography  When  m   the  reian  of
=== taraxacum FSD
30811:taraxacum  ^
30812:Taraxacum  I
30821:taraxacum  Tar'en-tlne,  1   tarien-tln,  2   tfiriCn-lIn  la  Of  or  pertaln-
30822:Taraxacum]  ing  to  ancient  Tarentum  or  Its  inhabitants  II  n   An  In- Around  It  the  legends  of  the  Fenian  cycle  are  centered  _   ^4  ■«  habitant  of  Tarentum,  now  Taranto,  Italy
```


## [2026-09-14T03:17:39.671Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30805,30825p' FSD_vol4.txt | cut -c1-900"
}
```


### [2026-09-14T03:17:39.749Z] TOOL RESULT

```
CaupbeIbU  The  Launch  of  a   F\rtt*Haie  st  7 Tar*,  n   A   river  In  central  E   North  Carolina,  length,  180  m to  Pamlico  Sound
ta'ra*,  1   to'ra.  2   ta'ra  fl  Bot  Same  as  taro* ta'ra*,  n   Bot  Same  as  taliera ta'ra*,  n   Same  as  tara-fern ta'ra*,  n   [Maori }   The  sea-swallow  (Sterna  caspia)
A   town  In A   form  of A   small
evergreen  tree  (PUtosponm  eugenioides),  with  white  resinous bark,  handsome  Ilght-grecn  foliage,  and  many  fragrant pale-yellow  flowers  In  terminal  corymbs  Known  by  settlers as  maple,  turpcntloc,  and  white  mapau. tor"a-tan-tar'a,  1   tar  e-tan-tar'a,  2   tfir  a-ifin-t&ria,  a   ,n  ,& adv  [Rare  ]   The  sound,  or  like  the  sound,  of  a   trumpet ta-rauS  1   le-rou',  2   ta-rou%  n   A   Burmese  violin  having  3 silken  strings
tar"ax-ac'er-ln,  1   tar'aks-as'er-
In,  2   tfir  fiks-fic'er-ln.  n   The.  
resin  (CiHmO)  of  taraxacum  ^
(<  Taraxacum  I
ta*rax'a-cln,  l   ta-raks'e-sln,  2   larau
xiu,  25,  27,  etc  supposed  to  be  the  darnel  or  cockle, now  generally  used  figuratively,  as,  fores  of  haste,  the fores  among  the  good  2.  (1)  Any  one  of  vanous species  of  vetch,  especially  the  common  vetch  (Ficto eofiro),  also,  loosely,  any  one  of  several  plants  of other  genera  of  the  same  family  (2)  The  seed  of  a vetch  m   reference  to  its  size  ns  a   small  thing,  hence, n   whit,  jot,  tittle  [<  tare,  o   ,   <   AS  teran,  tear]
—   hairy  tare,  same  as  tare-vetch  — smooth  t,  the 4-seeded  vetch  (Vida  teirasperma)  —   sn'pcT-tate",  n   A special  allowance  in  excess  of  the  usual  amount  —   tare'* vetch",  n   A   creeping  weed  (Vida  fiirsxaa)  of  cultivated fields,  resembling  the  common  vetch,  but  with  Its  flower smaller  and  its  pods  oblong,  2-seeded,  and  hairy  naturalized in  the  eastern  United  States  from  Europe  t   «fitcht.
tare*,  n   1.  Com  An  allowance  made,  as  in  customi house  or  other  transactions,  by  deducting  from  the  gross weight  the  weight  of  the  receptacle,  as  the  box,  cask, sack,  or  wTapping  in  w   hich  goods  are  contained  Specif , the  weight  of  a   motor-vehicle  without  its  load,  fuel,  or necessary  equipment  2.  Chem  The  weight  of  a   ves- sel, as  a   flask,  in  which  a   substance  is  weighed  [F ,   < At  farho,  <   faroh,  throw  away  1
—   average  tare,  a   mean  allowance, arrived  atbywelghlng a   few  packages  and  adopting  their  average  as  the  standard for  all  —   customary  t ,   the  assumed  or  established  weight of  packlng-cascs  of  a   given  kind,  as  among  merchants  — real  t ,   the  actual  ascertained  weight  of  the  packing-case  In which  merchandise  is  packed  — t   and  tret.  1,  Same  as TARE*,  1,  and  teet  2   Arith  A   rule  or  process  for  calcu- lating the  above  and  similar  allowances
are*,  n   [E  Ind)  A   small  silver  coin,  now  disused  ta'rat* Ta're-a,  1   te'n-a  or  te-rFe,  2   tfi're-a  or  ta-rB'a,  n   Bib JChronvm,3S  [Heb,  flight)  [tarif.
tar'ee,  1   taril,  2   tfirie,  n   (E  ind)  Palm  wine,  toddy ta-ren'tc,  l   to-ren't6,  2   ta-r6n'tc,  n   [F]  A   gecko-Uzard (Platydactytus  mattriianicus)  of  the  Mediterranean  region, ta-ren'to-laf.  jANTELLA.etc
liviiiun  J   x   ue  bch-swuuuw  \otcr«u  ^   ,   —   j   ,   la-rvu'to-iai.  lAr4ix.iixjA,
Ta'raSn  A   villageln  Meath  county,  Ireland  near  the  Hill  of  ta-rfiks  a-cin,  n   Cnem  A   crystalline  compound  In  the  tar"en-tcl'la,  tar'ent-lsm,  ta-ren'tu-la  Same  as  tar- Tara  (507  ft  high),  ancient  seat  of  sovereignty  in  Ireland  dandelion-root,  from  wmch  the  drug  taraxacum  Tar'en-tlne,  1   tarien-tln,  2   tfiriCn-lIn  la  Of  or  pertaln-
from  a   remote  period  to  the  middle  of  the  Gth  century  ^   believed  to  derive  its  medicinal  value  (<  Taraxacum]  ing  to  ancient  Tarentum  or  Its  inhabitants  II  n   An  In- Around  It  the  legends  of  the  Fenian  cycle  are  centered  _   ^4  ■«  habitant  of  Tarentum,  now  Taranto,  Italy
There Malachy  defeated  the  Danes  In  979  Ta-rax  ^cura,  1   ^a-r&ks a-cQm,  n   fa-ren'to-Ia.  1   ta-ren'to-la  2 ta-r6n'to-la. n   1.  (ItlAEuro-
      Bot  A   genus  of  stemless  herbs  of  the  family  Clcftorloccar,  ^ean  Mcko  2.  ThP  eommon
having  a   rosette  of  usually  toothed  radical  leav  es  and  soil-  itzard.nqh  or  lArpr^  ®   /asdcuiarU) tary  yellow  heads  on  naked  hollow  scapes  T   offldnate  or  ta-  _ raxacum  Is  the  common  dandelion  2.  (t-J  (l)  Any  plani
```


## [2026-09-14T03:19:01.709Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nfor f,ln,off in [('NYB_vol2_glossary.txt',3697,8),('HUB.txt',9534,10),('HUB.txt',1643,10),('LKT.txt',4558,26),('LKT.txt',4597,26),('SKT.txt',19187,20),('SKT.txt',19216,20)]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    leaf='\\n'.join(lines[:ln]).count('\\f')\n    print(f, 'line',ln,'leaf',leaf,'printed≈',leaf-off)\n\""
}
```


### [2026-09-14T03:19:02.906Z] TOOL RESULT

```
NYB_vol2_glossary.txt line 3697 leaf 206 printed≈ 198
HUB.txt line 9534 leaf 276 printed≈ 266
HUB.txt line 1643 leaf 58 printed≈ 48
LKT.txt line 4558 leaf 188 printed≈ 162
LKT.txt line 4597 leaf 189 printed≈ 163
SKT.txt line 19187 leaf 517 printed≈ 497
SKT.txt line 19216 leaf 518 printed≈ 498
```


## [2026-09-14T03:25:09.062Z] TOOL CALL #56: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-497.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_TATAR = \"https://en.wiktionary.org/wiki/Tatar\"\nW_TALX  = \"https://en.wiktionary.org/wiki/%D8%AA%D9%84%D8%AE\"\nW_TARAX = \"https://en.wiktionary.org/wiki/Taraxacum\"\nA_TATAR = \"https://abadis.ir/fatofa/%D8%AA%D8%A7%D8%AA%D8%A7%D8%B1/\"\nA_TALX  = \"https://abadis.ir/fatofa/%D8%AA%D9%84%D8%AE/\"\nA_TARSH = \"https://abadis.ir/fatofa/%D8%B7%D8%B1%D8%B4%D9%82%D9%88%D9%86/\"\nAHD     = \"https://www.ahdictionary.com/word/search.html?q=Tatar\"\nWP_TAT  = \"https://en.wikipedia.org/wiki/Tatar_(term)\"\n\ndata = {\n \"pdf_page\": 497,\n \"book_page\": 467,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n\n  # ---------------- entry 0 : Tata ----------------\n  {\n   \"entry\": 0,\n   \"root\": \"Tata\",\n   \"verdict\": \"disputed\",\n   \"modern_form\": \"Old Turkic \\U00010C43\\U00010C43\\U00010C3A (tatar), ethnonym of a Mongolic-speaking tribal confederation; no shorter base *Tata is attested\",\n   \"note\": (\n     \"Nourai's box reproduces Klein p.1574 s.v. Tartar: 'ML. Tartarus, fr. Pers. Tatar, ult. fr. Tata, \"\n     \"name of the Mongols, who coming from the Gobi desert invaded Russia in the 9th cent.' The Persian->English \"\n     \"half of that is right, but the root box is not the modern view. (1) The form: the name is already tatar, \"\n     \"with -r, in its earliest attestation, the Old Turkic Orkhon inscriptions of Kul Tegin (732 CE) and Bilge \"\n     \"Qaghan (735 CE), otuz tatar 'Thirty Tatar' and toquz tatar 'Nine Tatar'; Sogdian tt'r is attested in the \"\n     \"9th-10th c. Turco-Sogdian documents of Dunhuang. None of the sources consulted (Wiktionary, AHD, Lokotsch \"\n     \"no. 2045, Mo'in's footnote in Borhan p.452) knows a base *Tata. (2) The date: the Mongols reached Russia in \"\n     \"1223-1240, not the 9th century; the Latin Tartarus spelling and the word's spread through Europe belong to \"\n     \"the 1240s. (3) The label: 'Turkish' is loose - the word is Old Turkic at best, and in the Orkhon texts it \"\n     \"names Mongolic-speaking tribes who were the Turks' enemies; AHD says only 'of Turkic origin'. Nourai's own \"\n     \"Persian authority contradicts him here: Mo'in's long footnote on تاتار in Borhan-e Qate' (p.452) cites Thomsen \"\n     \"and the Orkhon inscriptions for the 8th-c. forms سی‌تاتار / نه‌تاتار and Barthold's EI article. \"\n     \"Verdict: disputed as to the root form and gloss; the tree hanging from it is otherwise sound.\"\n   ),\n   \"note_fa\": (\n     \"نورایی ریشه را «Tata» و ترکی دانسته و عیناً از کلاین (صفحهٔ ۱۵۷۴) گرفته است؛ اما \"\n     \"پژوهش امروزی چنین ستاکی را نمی‌شناسد: کهن‌ترین گواهی این نام، در سنگ‌نوشته‌های ترکی ارخون \"\n     \"(کول‌تگین ۷۳۲ میلادی و بیلگه‌خاقان ۷۳۵)، همان tatar است با رای پایانی: otuz tatar «سی تاتار» و toquz tatar \"\n     \"«نه تاتار». جالب آنکه خود معین در حاشیهٔ برهان قاطع (ص ۴۵۲) به نقل از تامسن همین را می‌گوید. نیز یورش مغول \"\n     \"به روسیه در سدهٔ هفتم هجری/سیزدهم میلادی رخ داد، نه سدهٔ نهم. پس ادعای نورایی دربارهٔ ریشه رد می‌شود، \"\n     \"هرچند زنجیرهٔ ترکی ← فارسی ← انگلیسی درست است.\"\n   ),\n   \"sources\": [W_TATAR, WP_TAT, AHD],\n   \"ref_check\": [\n     {\"ref\": \"KLN:1574\", \"status\": \"supports\",\n      \"note\": \"Verified in KLN_1966.txt, leaf 834 (page numerals 1574/1575 printed on that leaf): 'Tartar, n. and adj. — ML. Tartarus, fr. Pers. Tatar, ult. fr. Tata, name of the Mongols, who coming from the Gobi desert invaded Russia in the 9th cent. The first r in Tartar is due to a confusion with L. Tartarus, „hell“.' Klein does say 'Tata' — so the citation is accurate; it is Klein who is out of date.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"LKT\", \"where\": \"no. 2045, p. 163\", \"stance\": \"partial\",\n      \"note\": \"'2045. Tk. Tatar: N. pr., Name einer großen Verzweigung des Türkenstammes' — Lokotsch treats Tatar as the primary Turkic form and gives no *Tata (grep 'Tatar' in LKT.txt, line 4597).\"},\n     {\"src\": \"TTS\", \"where\": \"Vámbéry 1878, whole text\", \"stance\": \"silent\",\n      \"note\": \"grep -i 'tatar' in incoming/TTS/TTS_pages.txt returns only the title and the phrase 'turko-tatarische Sprachen' in the preface; Vámbéry has no headword for the ethnonym.\"},\n     {\"src\": \"BQT\", \"where\": \"vol. 1, p. 452 (leaf 680), Mo'in's footnote 4 on تاتار\", \"stance\": \"contradicts\",\n      \"note\": \"'نام قومی است. بقول تامسن ... در قرن هشتم میلادی (دوم هجری) در کتیبه‌های ترکی ارخون نام دو طایفه از تاتار بنام «سی‌تاتار» و «نه‌تاتار» یاد شده ... مراد از نام مذکور مغول یا بخشی از مغول بود نه قومی ترک' (BQT_v1_pages.txt, leaf 680). Mo'in gives tatar as the oldest form and points to Mongolic, not to a base *Tata.\"},\n     {\"src\": \"AHD\", \"where\": \"online dictionary s.v. Tatar\", \"stance\": \"partial\",\n      \"note\": \"'Tatar ... from Persian Tātār, of Turkic origin.' Supports the Persian>English link but gives no *Tata.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"tâtâr\", \"verdict\": \"plausible\",\n     \"derivation\": (\n       \"Persian تاتار tātār is a borrowing of the Turkic/Mongolic ethnonym tatar. It entered Persian in the \"\n       \"7th/13th century with the Mongol campaigns — Ibn al-Athīr, Juwaynī and Rashīd al-Dīn all use it — and \"\n       \"at once became the general Islamic-world name for the Mongols (Mo'in: 'نامی که در گذشته به مغول \"\n       \"اطلاق می‌شد'), later extended to Turkic peoples generally. Hāfeẓ's line quoted in the box \"\n       \"(nāfe-hā-ye tātārī 'Tatar musk-pods') shows its literary use for Inner Asia, the source of musk. \"\n       \"The chart's variants تتار / تتر are the Arabic-script spellings without the long ā (tatār, tatar). \"\n       \"The borrowing itself is certain; what is not supported is the specific arrow drawn, i.e. that Persian \"\n       \"added an -r to a base *Tata: the -r is already there in Old Turkic tatar (732 CE) and in Sogdian tt'r \"\n       \"(9th-10th c.), both older than any Persian attestation. So: right word, right route (Turkic > Persian), \"\n       \"wrong starting form.\"\n     ),\n     \"derivation_fa\": (\n       \"«تاتار» وام‌واژه‌ای است از نام قومی ترکی‌مغولی tatar که در سدهٔ هفتم هجری با لشکرکشی مغولان \"\n       \"وارد فارسی شد (ابن‌الاثیر، جوینی، رشیدالدین) و زود بر همهٔ مغولان اطلاق گردید؛ معین آن را \"\n       \"«نامی که در گذشته به مغول اطلاق می‌شد» معنی کرده است. گونه‌های «تتار» و «تتر» همان نام بدون الف کشیده \"\n       \"است. وام‌گیری قطعی است، اما پیوند آن به ستاکی کوتاه‌تر به شکل *Tata پذیرفتنی نیست، زیرا رای پایانی \"\n       \"در ترکی باستان و سغدی (tt'r) از آغاز هست. با احتیاط پذیرفتنی است.\"\n     ),\n     \"sources\": [A_TATAR, W_TATAR],\n     \"ref_check\": [\n       {\"ref\": \"MON:994\", \"status\": \"partial\",\n        \"note\": \"Mo'in's entry تاتار read online (abadis.ir, فرهنگ معین section): '(اِ.) نامی که در گذشته به مغول اطلاق می شد.' The gloss 'a Mongol tribe' is supported; Mo'in gives no etymology there, and the 6-vol print pagination is not reproducible online, so p.994 itself could not be verified.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"vol. 1, p. 452 (leaf 680), s.v. تاتار + Mo'in's footnote\", \"stance\": \"partial\",\n        \"note\": \"headword 'تاتار بر وزن ناچار، ولایتی است که مشک خوب از آنجا آورند و ترکان آنجا را نیز گویند' — confirms the Persian word and the musk association behind Hāfeẓ's line; Mo'in's footnote derives it from Orkhon Turkic tatar, not from *Tata.\"},\n       {\"src\": \"HRN\", \"where\": \"Grundriss, whole text\", \"stance\": \"silent\",\n        \"note\": \"grep -i 'tatar' in HRN.txt gives only 'apr. tatarwis' (Old Prussian, unrelated); Horn has no entry for the ethnonym, as expected for a loanword of the Mongol period.\"},\n       {\"src\": \"HUB\", \"where\": \"Persische Studien, whole text\", \"stance\": \"silent\",\n        \"note\": \"grep -i 'tatar' in HUB.txt returns nothing.\"},\n       {\"src\": \"LKT\", \"where\": \"no. 2045, p. 163\", \"stance\": \"supports\",\n        \"note\": \"'Tk. Tatar: N. pr., Name einer großen Verzweigung des Türkenstammes' — the Turkic ethnonym is the source of all the European and Slavic forms; Persian is one of the transmitting languages.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"English\", \"words\": \"Tatar\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n       \"English Tartar/Tatar appears in the late 14th c. (Mandeville, Chaucer's Squire's Tale) from Old French \"\n       \"Tartre and Medieval Latin Tartarus/Tartari, which render Persian تاتار Tātār — the form in which the \"\n       \"Mongol invaders' name reached the Islamic world and, through it, Europe in the 1240s. The parasitic first \"\n       \"-r- of 'Tartar' is contamination with Latin Tartarus 'the underworld', the pun famously attributed to \"\n       \"Louis IX and recorded by Matthew Paris (1241): the invaders were demons loosed from Tartarus. English \"\n       \"restored the etymologically correct Tatar in the 19th c., which is why Klein's headword is Tartar and \"\n       \"'Tatar, n. — See Tartar' stands separately (p.1576). AHD s.v. Tatar: 'from Persian Tātār, of Turkic origin' \"\n       \"— precisely the arrow Nourai draws.\"\n     ),\n     \"derivation_fa\": (\n       \"واژهٔ انگلیسی Tatar/Tartar در اواخر سدهٔ چهاردهم میلادی از فرانسهٔ کهن Tartre و لاتین میانه Tartarus \"\n       \"وارد شد، و آن خود برگردان فارسی «تاتار» است که در دههٔ ۱۲۴۰ میلادی از جهان اسلام به اروپا رسید. رای \"\n       \"افزوده در Tartar از رهگذر ریشه‌شناسی عامیانه و همانندسازی با Tartarus (دوزخ لاتینی) پدید آمد. فرهنگ \"\n       \"میراث آمریکایی (AHD) نیز می‌نویسد: «from Persian Tātār, of Turkic origin». ادعای نورایی درست است.\"\n     ),\n     \"sources\": [AHD, W_TATAR, WP_TAT],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"ahdictionary.com s.v. Tatar: '...from Persian Tātār, of Turkic origin.' (fetched and archived)\"},\n       {\"ref\": \"KLN:1574\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt leaf 834 (= pp. 1574/75): 'Tartar, n. and adj. — ML. Tartarus, fr. Pers. Tatar...'; and leaf 835 (p. 1576): 'Tatar, n. — See Tartar.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SKT\", \"where\": \"Concise Etym. Dict., p. 498 s.v. Tartar (2)\", \"stance\": \"supports\",\n        \"note\": \"'Tartar (2), a native of Tartary. A perverse spelling of Tatar, owing to popular etymology which regarded [them] as let loose out of Tartarus... From Tātar, a Tatar' (SKT.txt line 19216).\"},\n       {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 4, s.v. Tartar / Tatar\", \"stance\": \"supports\",\n        \"note\": \"'Tar'tar², a & n. Same as Tatar, the usual spelling in...' and the note 'Ethnologists well know that the name of the so-called “Tartar” race is properly Tatar and they are now endeavouring to restore this correct orthography' (FSD_vol4.txt lines 30985, 31082).\"},\n       {\"src\": \"LKT\", \"where\": \"no. 2045, p. 163\", \"stance\": \"supports\",\n        \"note\": \"Lokotsch lists the European reflexes (Ger. Taterkorn, Tatarennachricht, Fr. tartare, Cz./Russ. tatarka) all from Tk. Tatar.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"tt`r\", \"verdict\": \"plausible\",\n     \"derivation\": (\n       \"Gharib's Sogdian Dictionary no. 9697, printed p. 392: 'tt'r S — tatar — Tatar', with the reference \"\n       \"'S W-Ham. CII 1990 p86' = Sims-Williams & Hamilton, Documents turco-sogdiens du IXe-Xe siècle de \"\n       \"Touen-houang (Corpus Inscriptionum Iranicarum, 1990), p. 86. The word thus occurs in secular \"\n       \"Sogdian-script documents from Dunhuang of the 9th-10th c., where Sogdian merchants and scribes wrote the \"\n       \"name of their Turkic/Mongol neighbours; Sogdian orthography <tt'r> represents /tatar/ (unwritten short a \"\n       \"in the first syllable, <'> for the second ā/a). It is a contemporaneous adoption of the same Inner \"\n       \"Asian ethnonym, not a Sogdian derivative of a shorter *Tata — on the contrary, together with Old Turkic \"\n       \"otuz tatar (732) it is one of the strongest arguments that the -r is original. The arrow is therefore \"\n       \"right about the family but wrong about the direction of formation.\"\n     ),\n     \"derivation_fa\": (\n       \"در فرهنگ سغدی بدرالزمان قریب (مدخل ۹۶۹۷، ص ۳۹۲) «tt'r» به صورت tatar آوانگاری شده و معنی‌اش \"\n       \"«تاتار» است؛ مأخذ آن اسناد ترکی‌سغدی تون‌هوانگ (سدهٔ نهم–دهم میلادی، نشر سیمز-ویلیامز و همیلتون، \"\n       \"CII ۱۹۹۰، ص ۸۶) است. در خط سغدی الف کوتاه نوشته نمی‌شود، پس <tt'r> همان /tatar/ است. این وام‌گیری مستقیم از \"\n       \"نام قومی ترکی است و خود گواهی است بر اینکه رای پایانی اصلی است، نه افزوده بر *Tata. واژه درست است، ولی \"\n       \"جهت پیکان در نمودار دقیق نیست.\"\n     ),\n     \"sources\": [W_TATAR, WP_TAT],\n     \"ref_check\": [\n       {\"ref\": \"SOD:392\", \"status\": \"supports\",\n        \"note\": \"Verified in SOD_pages.txt: entry '9697 tt'r S / tatar / Tatar / S W-Ham. CII 1990 p86' falls in the \\\\f-block whose running page numeral is 392 (leaf 459; leaf 458 heads '391', leaf 460 heads '393'). The English index of the same volume also lists 'Tatar 9697'. Nourai's page is exactly right.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"LKT\", \"where\": \"no. 2045, p. 163\", \"stance\": \"silent\",\n        \"note\": \"Lokotsch gives only the Turkic form and its European descendants; no Sogdian material (grep 'Sogd' near line 4597 finds nothing).\"},\n       {\"src\": \"BQT\", \"where\": \"vol. 1, p. 452, Mo'in's footnote on تاتار\", \"stance\": \"supports\",\n        \"note\": \"Mo'in independently dates the ethnonym to the 8th c. Orkhon inscriptions, which is consistent with a 9th-10th c. Sogdian attestation of the same -r form.\"}\n     ]\n    }\n   ]\n  },\n\n  # ---------------- entry 3 : Taxl, Taxlik ----------------\n  {\n   \"entry\": 3,\n   \"root\": \"Taxl, Tâxlik\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Middle Persian taxl <tlhk'> 'bitter' (Manichaean MP taxr <thr>), abstract taxlīh 'bitterness'; from Proto-Iranian *taxra-\",\n   \"note\": (\n     \"The root box is right in substance. MacKenzie, A Concise Pahlavi Dictionary p. 82: 'taxl [tlhk' | (M thr), \"\n     \"P txl, N talx] bitter', continued on p. 83 '~īh: bitterness'. Nyberg's glossary p. 198 reads the same word \"\n     \"tahl '[t'hl] bitter ... MPrth tal; MPrs thr; Paz. tahal (SGV); NP talx'. Hübschmann (Persische Studien \"\n     \"p. 48, no. 391) gives 'np. talx bitter, paz. tahal = phl. taxr' and reconstructs Iranian *taxra-; \"\n     \"Wiktionary derives NP تلخ from MP <t'hl'> taxl, from Proto-Indo-Iranian *takra- (Skt. takra- \"\n     \"'buttermilk'), citing Mayrhofer EWAia I 611-12. The only quibble is the second form: the abstract is \"\n     \"taxlīh (suffix -īh, Book Pahlavi <-yh>), and the long ā of Nourai's 'Tâxlik' is not supported by any of \"\n     \"them; it is an older-style reading of <tlhkyh> that Mo'in's print edition probably carries. Not enough to \"\n     \"downgrade the root.\"\n   ),\n   \"note_fa\": (\n     \"ریشهٔ پهلوی taxl «تلخ» درست است: مکنزی (ص ۸۲) آن را به صورت taxl [tlhk'] با گونهٔ مانوی taxr ضبط \"\n     \"کرده و مصدر آن را taxlīh «تلخی» خوانده است؛ نیبرگ (ص ۱۹۸) tahl و هوبشمان (ص ۴۸) taxr می‌خوانند و صورت \"\n     \"ایرانی باستان را *taxra- بازسازی می‌کنند. تنها ایراد آنکه صورت دوم، Tâxlik، باید taxlīh باشد (پسوند مصدری \"\n     \"-īh) و الف کشیدهٔ آن مستند نیست. در کلیات، ادعای نورایی درست است.\"\n   ),\n   \"sources\": [W_TALX, A_TALX],\n   \"ref_check\": [\n     {\"ref\": \"MON:1131\", \"status\": \"partial\",\n      \"note\": \"Mo'in's entry تلخ read online (abadis.ir, فرهنگ معین): '(تَ) [په.] (ص.) ۱ - دارای مزة غیرمطبوع، بدمزه...' — the tag [په.] is Mo'in's mark for Pahlavi origin, i.e. he does derive تلخ from Pahlavi, as Nourai says. The Latin-script Pahlavi form of the print edition is not reproduced online and the 6-vol pagination cannot be checked, so p. 1131 itself is unverified.\"},\n     {\"ref\": \"BQT:508\", \"status\": \"partial\",\n      \"note\": \"Borhan-e Qate' (Mo'in ed.) p. 508 located in BQT_v1_pages.txt at leaf 736 (offset leaf-228; leaf 740 = p.512). The page carries the تلخ- headwords (تلخ چکوک، تلخ چولک، تلخ عیشی، تلخک، تلخی), so the citation points at the right place; Mo'in's Latin-script Pahlavi footnote is not legible in the archive.org OCR of that leaf, so the specific form taxl could not be read off it.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie p. 82-83 s.v. taxl\", \"stance\": \"supports\",\n      \"note\": \"'taxl [tlhk' | (M thr), P txl, N talx] bitter.' followed on the next page by '~īh: bitterness.' (PHD.txt line 593-595; the running head of the following block is 'taxlih 83'). Exactly Nourai's pair, except that MacKenzie's abstract is taxlīh, not tāxlīk.\"},\n     {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, p. 198\", \"stance\": \"partial\",\n      \"note\": \"'tahl [t'hl] bitter 6119. — MPrth tal; MPrs thr (List 88); Paz. tahal (SGV); NP talx.' Same word, same New Persian outcome, but Nyberg transcribes tahl (and Manichaean thr), not taxl.\"},\n     {\"src\": \"HUB\", \"where\": \"Persische Studien p. 48 (no. 391)\", \"stance\": \"supports\",\n      \"note\": \"'Hierher: np. talx ‚bitter‘, paz. tahal = phl. taxr Shk. 268, afgh. trīx, f. tarxa ‚bitter‘ ... Die persischen Formen weisen auf iranisch *taxra-.'\"},\n     {\"src\": \"HRN\", \"where\": \"Grundriss, whole text\", \"stance\": \"silent\",\n      \"note\": \"grep -i 'talx|talh|taxl|bitter' in HRN.txt finds no entry for the word (Horn's numbering skips it; Hübschmann supplies it under his no. 391).\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"talx; talx-šakŭk\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"talx-šakŭk «تلخ شکوک ( تلخ جوک )»\",\n     \"correct_form\": \"talx-čakūk «تلخ چکوک» (Borhan's variant «تلخ چولک» talx-čūlak)\",\n     \"derivation\": (\n       \"(a) تلخ talx 'bitter' is the regular New Persian continuation of Middle Persian taxl <tlhk'> \"\n       \"(Manichaean taxr), from Old Iranian *taxra-. The sound change is the one Hübschmann states as a rule \"\n       \"(Pers. Studien p. 266): final Old-Persian/Pahlavi -xr yields New Persian -lx — r dissimilates to l and \"\n       \"the cluster metathesises — exactly as Pahlavi Baxr / OP Bāxtri- gives Balx. That is precisely what \"\n       \"Nourai's NOTE ('the change of the last two letters') describes, and his comparison with maġz / mazġ \"\n       \"'brain' is a genuine parallel metathesis. Pazand tahal and Pashto trīx / f. tarxa confirm the \"\n       \"pre-metathesis shape. Mo'in tags تلخ '[په.]', Pahlavi. The derivatives in the box — تلخه، تلخک \"\n       \"(diminutive -ak), تلخکام ('bitter-palated') — are all normal New Persian formations on talx. \"\n       \"This half is confirmed. \"\n       \"(b) The compound printed as talx-šakŭk «تلخ شکوک (تلخ جوک)» is not the form the sources know. \"\n       \"Borhan-e Qate' p. 508 — the very page Nourai cites — prints 'تلخ چکوک ... نام کاسنی صحرایی \"\n       \"است، و معرّب آن طرخشقوق باشد' and the variant 'تلخ چولک'; Klein p. 1573 writes 'Pers. talkh \"\n       \"chakok'. The book prints ش for چ and جوک for چولک — an author's misreading (very likely \"\n       \"back-formed from the Arabic طرخشقوق, which does have ش), not an extraction error: the printed page \"\n       \"(pdf 497 / book 467, image saved as data/verification/sources/refs/ocr/BOOK/497.png) plainly reads \"\n       \"'talx-šakŭk' and «تلخ شکوک ( تلخ جوک )», which the JSON reproduces faithfully. The plant is \"\n       \"wild chicory / dandelion, lit. 'bitter čakūk'.\"\n     ),\n     \"derivation_fa\": (\n       \"الف) «تلخ» دنبالهٔ قاعده‌مند فارسی میانهٔ taxl (مانوی taxr) از ایرانی باستان *taxra- است. \"\n       \"هوبشمان (ص ۲۶۶) قاعده را چنین می‌آورد: خوشهٔ پایانی -xr در فارسی نو به -lx بدل می‌شود؛ یعنی ر به ل \"\n       \"ابدال می‌گردد و دو واج قلب می‌شوند — درست همان‌گونه که پهلوی Baxr به «بلخ» رسید. پس یادداشت \"\n       \"نورایی دربارهٔ «تغییر دو حرف آخر» و قیاس آن با «مغز/مزغ» درست است. ب) اما ترکیبی که کتاب «تلخ شکوک \"\n       \"(تلخ جوک)» چاپ کرده، در منابع به این شکل نیست: برهان قاطع در همان صفحهٔ ۵۰۸ «تلخ چکوک ... نام کاسنی \"\n       \"صحرایی است، و معرّب آن طرخشقوق باشد» و گونهٔ «تلخ چولک» دارد، و کلاین هم talkh chakok می‌نویسد. \"\n       \"بنابراین شکوک/جوک خطای خود نورایی است (احتمالاً از روی صورت عربی طرخشقوق ساخته شده)، نه خطای خوانش \"\n       \"اسکن؛ تصویر صفحهٔ چاپی ۴۶۷ همین را نشان می‌دهد.\"\n     ),\n     \"sources\": [W_TALX, A_TALX],\n     \"ref_check\": [\n       {\"ref\": \"MON:1131\", \"status\": \"supports\",\n        \"note\": \"Mo'in s.v. تلخ: '(تَ) [په.] (ص.) ۱ - دارای مزة غیرمطبوع، بدمزه. ۲ - زننده، سخت... ۳ - تندخو، بدخلق.' The [په.] tag = Pahlavi origin, supporting the arrow Pahlavi taxl > NP talx and the gloss 'bitter'.\"},\n       {\"ref\": \"BQT:508\", \"status\": \"supports\",\n        \"note\": \"BQT_v1_pages.txt leaf 736 (= printed p. 508): 'تلخ چکوک — با خای نقطه‌دار و جیم و کاف و واو و کاف دیگر ... نام کاسنی صحرایی است، و معرّب آن طرخشقوق باشد، و بعربی نید گویند' plus 'تلخ چولک ... بمعنی تلخ چکوک است که کاسنی صحرانی باشد'. The page supports the Persian>Arabic arrow exactly; it also shows that the Persian word is چکوک, not شکوک.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HUB\", \"where\": \"Persische Studien p. 266 (§ ap. xr – np. lx) and p. 48 (no. 391)\", \"stance\": \"supports\",\n        \"note\": \"'b) Ap. xr — np. lx: talx ‚bitter‘, paz. tahal (= tahl) = phl. taxr Shk. 268, Dīnkart VI Gl. p.2, afgh. trīx, fem. tarxa; Balx ... ap. Baxtri-' — the metathesis rule Nourai's NOTE alludes to, stated explicitly.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p. 82 s.v. taxl\", \"stance\": \"supports\",\n        \"note\": \"'taxl [tlhk' | (M thr), P txl, N talx] bitter' — MacKenzie himself gives New Persian talx as the outcome.\"},\n       {\"src\": \"NYB\", \"where\": \"Nyberg II p. 198 s.v. tahl\", \"stance\": \"partial\",\n        \"note\": \"'tahl [t'hl] bitter ... NP talx' — same equation, different reading of the Pahlavi (tahl not taxl).\"},\n       {\"src\": \"KLN\", \"where\": \"Klein p. 1573 s.v. Taraxacum\", \"stance\": \"partial\",\n        \"note\": \"'fr. Pers. talkh chakok, lit. ‚bitter herb‘' — supports the compound but with č, not š; relevant to word (b) of this node.\"},\n       {\"src\": \"ARY\", \"where\": \"Aryanpur, Persian headword index\", \"stance\": \"silent\",\n        \"note\": \"grep 'تلخ' in incoming/ARY/ARY_pages.txt returns only incidental occurrences (ترخینه/تلخینه and glosses inside other entries); no headword تلخ.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Arabic\", \"words\": \"tarax-šaqŭq\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n       \"Arabic طَرَخْشَقُوق ṭaraxsaqūq (also طرخشقون ṭaraxsaqūn and the shortened طرشقون) 'wild chicory, dandelion' \"\n       \"is the muʿarrab of Persian تلخ چکوک talx-čakūk 'bitter čakūk (wild chicory)'. Persian t- was rendered \"\n       \"by the emphatic ط (the usual Arabization of Persian t in plant and drug names), the č of چکوک by ش, and \"\n       \"the ending was reshaped as -qūq / -qūn. Borhan-e Qate' p. 508 says it in so many words: 'معرّب آن \"\n       \"طرخشقوق باشد'. Klein p. 1573: 'Arab. tarakhshaqun, tarakhshaquq, fr. Pers. talkh chakok, lit. \"\n       \"‚bitter herb‘'; Skeat p. 497 and Lokotsch no. 2025 say the same. The word belongs to the Arabic-Persian \"\n       \"pharmacological tradition (it is the plant of Ibn Sīnā's Qānūn), and from there it passed into Latin \"\n       \"medicine. Nourai's transliteration drops the emphatic (ṭ) and writes the vowel as ŭ, otherwise the \"\n       \"node is right; note that the Arabic form was then re-borrowed into Persian as طرخشقوق/طرشقون, a \"\n       \"Persian>Arabic>Persian round trip that Dehkhoda records.\"\n     ),\n     \"derivation_fa\": (\n       \"عربی طرخشقوق (و طرخشقون، طرشقون) معرّب «تلخ چکوک» فارسی است؛ ت فارسی در عربی به ط بدل \"\n       \"شده (قاعده‌ای رایج در نام گیاهان و داروها)، چ به ش، و پایانهٔ واژه به قالب عربی -قوق/-قون درآمده است. \"\n       \"برهان قاطع (ص ۵۰۸) صریحاً می‌گوید «معرّب آن طرخشقوق باشد» و کلاین و اسکیت و لوکوچ هم همین را \"\n       \"می‌آورند. این واژه از راه طب اسلامی (قانون ابن‌سینا) به اروپا رسید و سپس خود به فارسی بازگشت (دور \"\n       \"فارسی ← عربی ← فارسی). ادعای نورایی درست است.\"\n     ),\n     \"sources\": [A_TARSH, W_TARAX],\n     \"ref_check\": [\n       {\"ref\": \"BQT:508\", \"status\": \"supports\",\n        \"note\": \"'تلخ چکوک ... نام کاسنی صحرایی است، و معرّب آن طرخشقوق باشد' (BQT_v1_pages.txt leaf 736 = p. 508). This is exactly the Persian>Arabic arrow.\"},\n       {\"ref\": \"KLN:1573\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt leaf 833 (page numeral 1573 printed on that leaf): 'Taraxacum, n., a genus of plants of the chicory family (bot.) — ModL., fr. Arab. tarakhshaqun, tarakhshaquq, fr. Pers. talkh chakok, lit. ‚bitter herb‘.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"LKT\", \"where\": \"no. 2025, p. 162\", \"stance\": \"supports\",\n        \"note\": \"'2025. Ar. tarahšakūn: ‚Wilde Zichorie‘; hieraus lat. taraxacum ‚Löwenzahn, Leontodon taraxacum‘, frz. taraxacon; engl. taraxacum. [Devic DEt 216/217. Lammens Rem 235.]' — Arabic confirmed as the source, though Lokotsch does not name the Persian original.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat p. 497 s.v. Taraxacum\", \"stance\": \"partial\",\n        \"note\": \"'From Arab. taraxacon, explained as a kind of succory. Pers. tarkhashqūn, wild endive; latinised as taraxacon in Avicenna. (Devic; supp. to Littré.)' — Skeat has the Persian form in its re-borrowed Arabic shape, not as talx-čakūk.\"},\n       {\"src\": \"AFM\", \"where\": \"Addi Shir, Alfaẓ al-Fārisiyya al-Muʿarraba\", \"stance\": \"silent\",\n        \"note\": \"grep 'طرخش' / 'شقوق' in AFM_pages.txt finds only الطرخان and الطرخون (tarragon); Addi Shir has no entry for طرخشقوق.\"},\n       {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n        \"note\": \"grep 'tarax|tarhaš|Zichorie|Wegwarte' in incoming/PLA/PLA_pages.txt returns only kāsnī ('Zichorie ... aus pers. کاسنی'); طرخشقوق is not among Asbaghi's lemmata.\"},\n       {\"src\": \"MON\", \"where\": \"Dehkhoda/abadis s.v. طرشقون\", \"stance\": \"supports\",\n        \"note\": \"the Persian dictionaries gloss طرخشقوق/طرشقون as the dandelion, Taraxacum officinale, = گل قاصد، قاصدک، هندباء بری، کاسنی بری — the same plant as Borhan's کاسنی صحرایی.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"taraxacum\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n       \"Medieval Latin taraxacum / taraxacon is a straight transliteration of Arabic ṭaraxsaqūq / ṭaraxsaqūn, \"\n       \"picked up by the 12th-13th c. Latin translators of Arabic medicine (Avicenna's Qānūn, Serapion); \"\n       \"Weber took it in 1780 as the genus name Taraxacum for the dandelions. English taraxacum is the \"\n       \"pharmacists' word for the dried root of Taraxacum officinale used as a bitter tonic — exactly the \"\n       \"gloss 'a kind of chicory' in the box, the dandelion being reckoned to the chicory family \"\n       \"(Cichoriaceae/Asteraceae). Klein p. 1573 and Lokotsch no. 2025 both give the Arabic source, Skeat \"\n       \"p. 497 adds 'latinised as taraxacon in Avicenna', and Wiktionary derives the genus from Medieval Latin \"\n       \"taraxacum from Arabic طرخشقون. The rival derivation from Greek τάραξις 'disturbance' + ἄκος \"\n       \"'remedy', still repeated in popular sources, is a learned folk etymology and is not accepted by any of \"\n       \"the dictionaries consulted here.\"\n     ),\n     \"derivation_fa\": (\n       \"لاتین میانه taraxacum/taraxacon آوانگاری مستقیم عربی طرخشقوق است که از راه ترجمهٔ لاتینی قانون \"\n       \"ابن‌سینا و کتاب‌های سراپیون در سدهٔ ۱۲–۱۳ میلادی وارد طب اروپایی شد، و وبر در ۱۷۸۰ آن را نام جنس \"\n       \"قاصدک قرار داد. در انگلیسی taraxacum نام دارویی ریشهٔ خشکیدهٔ قاصدک است. کلاین (ص ۱۵۷۳)، اسکیت \"\n       \"(ص ۴۹۷) و لوکوچ (شمارهٔ ۲۰۲۵) همگی مأخذ عربی را تأیید می‌کنند. ریشه‌شناسی یونانی (τάραξις + ἄκος) \"\n       \"ریشه‌شناسی عامیانه‌است و پذیرفته نیست. ادعای نورایی درست است.\"\n     ),\n     \"sources\": [W_TARAX],\n     \"ref_check\": [\n       {\"ref\": \"KLN:1573\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt leaf 833 (= p. 1573): 'Taraxacum, n., a genus of plants of the chicory family (bot.) — ModL., fr. Arab. tarakhshaqun, tarakhshaquq, fr. Pers. talkh chakok, lit. ‚bitter herb‘.' Covers the whole Persian>Arabic>Latin>English chain of this entry.\"},\n       {\"ref\": \"WEB:1865\", \"status\": \"not_checked\",\n        \"note\": \"Only volume 1 (A–Mem) of Webster's New Twentieth Century Dictionary 2nd ed. is available on disk / open on archive.org (WEB_vol1.txt ends in the 'mem-' range); 'taraxacum' occurs there only inside the entries dandelion and horse gowan. Page 1865 is in the unavailable second half.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"LKT\", \"where\": \"no. 2025, p. 162\", \"stance\": \"supports\",\n        \"note\": \"'hieraus lat. taraxacum ‚Löwenzahn, Leontodon taraxacum‘, frz. taraxacon; engl. taraxacum.'\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat p. 497 s.v. Taraxacum\", \"stance\": \"supports\",\n        \"note\": \"'Taraxacum, the dandelion. (Arab.) From Arab. taraxacon, explained as a kind of succory ... latinised as taraxacon in Avicenna.'\"},\n       {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 4 s.v. Taraxacum\", \"stance\": \"partial\",\n        \"note\": \"'Ta-rax'a-cum, n. Bot. A genus of stemless herbs of the family Cichoriaceae ... T. officinale or taraxacum is the common dandelion' — confirms the botanical sense and the chicory family, but the OCR of the entry shows no etymology bracket.\"},\n       {\"src\": \"WEB\", \"where\": \"Webster's 2nd ed. vol. 1, s.v. dandelion\", \"stance\": \"partial\",\n        \"note\": \"'dandelion ... in botany, a common plant, Taraxacum officinale, having a milky, perennial root...' — the only accessible Webster material; the taraxacum headword is in the missing second half.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-497.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-497.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-497.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 497"
}
```


### [2026-09-14T03:25:11.194Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 6/6
node verdicts: {'plausible': 2, 'confirmed': 3, 'transcription_suspect': 1}
root verdicts: {'disputed': 1, 'confirmed': 1}
ref checks: {'partial': 1, 'supports': 8, 'not_checked': 1}
books consulted: {'partial': 6, 'silent': 6, 'supports': 11} | by book: {'LKT': 5, 'SKT': 3, 'BQT': 2, 'HUB': 2, 'FSD': 2, 'HRN': 1, 'PHD': 1, 'NYB': 1, 'KLN': 1, 'ARY': 1, 'AFM': 1, 'PLA': 1, 'MON': 1, 'WEB': 1}
```


## [2026-09-14T03:25:17.733Z] TOOL CALL #57: Bash

```json
{
 "command": "head -c 200 data/verification/page-497.json | xxd | head -2; python3 -c \"\nimport json;d=json.load(open('data/verification/page-497.json'))\nprint(d['pdf_page'],d['book_page'],len(d['entries']))\nfor e in d['entries']:\n    print(e['entry'],e['root'],e['verdict'],[ (n['id'],n['verdict']) for n in e['nodes']], 'note_fa' in e)\n    for n in e['nodes']: assert n.get('derivation_fa') and n.get('ref_check') and n.get('consulted')\nprint('all fields ok')\""
}
```


### [2026-09-14T03:25:18.832Z] TOOL RESULT

```
00000000: 7b0a 2020 2270 6466 5f70 6167 6522 3a20  {.  "pdf_page": 
00000010: 3439 372c 0a20 2022 626f 6f6b 5f70 6167  497,.  "book_pag
497 467 2
0 Tata disputed [(1, 'plausible'), (2, 'confirmed'), (3, 'plausible')] True
3 Taxl, Tâxlik confirmed [(1, 'transcription_suspect'), (2, 'confirmed'), (3, 'confirmed')] True
all fields ok
```


## [2026-09-14T03:25:35.870Z] AGENT

Page 497 (book 467) verified. `verify_check.py 497`: 6/6 nodes, **0 PROBLEM lines**.

**Verdicts** — roots: 1 confirmed, 1 disputed. Nodes: 3 confirmed, 2 plausible, 1 transcription_suspect. Ref checks: 8 supports, 1 partial, 1 not_checked. 2 redirect-only entries skipped; 7 redirects on the page need no work.

**Flagged items**

- **disputed — ROOT "Tata" [Turkish] (entry 0).** Klein p.1574 does say "ult. fr. Tata, name of the Mongols" (citation accurate), but no source knows a base *Tata: the ethnonym is already *tatar* in the Orkhon inscriptions (Kül Tegin 732, Bilge Qaghan 735: *otuz tatar*, *toquz tatar*), in Sogdian tt'r (9th–10th c.), and AHD says only "of Turkic origin". Klein's "invaded Russia in the 9th cent." is also wrong (1223–1240). Mo'in's own footnote on تاتار in Borhan p.452 (citing Thomsen and the Orkhon texts) contradicts Nourai here.
- **plausible — #1 Persian tâtâr, #3 Sogdian tt'r (entry 0).** Both words are real and correctly placed in the family; only the arrow direction is wrong (the -r is original, not added in Persian).
- **transcription_suspect — #1 talx-šakŭk «تلخ شکوک ( تلخ جوک )» (entry 3).** `error_in: "book"`. Borhan p.508 — the page Nourai cites — prints **تلخ چکوک** (var. **تلخ چولک**), and Klein p.1573 writes "Pers. talkh chakok". The printed page 467 verified by image: it really reads *talx-šakŭk* / شکوک / جوک, so the extraction is faithful and the misreading is Nourai's (probably back-formed from Arabic طرخشقوق). `correct_form: talx-čakūk`. The other word in the node, تلخ *talx*, is fully confirmed (MacKenzie p.82 taxl; Hübschmann's rule ap. -xr → np. -lx, cf. Baxr → Balx — Nourai's "change of the last two letters" note is correct).

**No extraction errors found** — the JSON matches the printed page everywhere I checked.

**Page-number checks that came out right:** KLN:1573/1574 (verified against the page numerals on KLN_1966 leaves 833/834), SOD:392 (Gharib entry 9697 "tt'r … Tatar"), BQT:508 (leaf 736). Not checkable: MON page numbers (6-vol print not online; entry content confirmed via abadis), WEB:1865 (only vol. 1 A–Mem exists open).

Page image archived to `data/verification/sources/refs/ocr/BOOK/497.png`; 8 web sources archived via `fetch_source.py`.
