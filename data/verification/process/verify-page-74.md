# Verification process log — verify-page-74


## [2026-09-05T05:44:05.380Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 74 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-74.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-74.json. Write /home/sfmqrb/git/rishe/data/verification/page-74.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 74` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:44:06.934Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:44:07.725Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-05T05:44:07.735Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-74.txt"
}
```


### [2026-09-05T05:44:07.747Z] TOOL RESULT

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


### [2026-09-05T05:44:07.754Z] TOOL RESULT

```
1	=== PDF page 74 (book page 44) ===
2	--- entry 0 ---
3	ROOT Awes -> redirect to Aus 2
4	--- entry 1 ---
5	ROOT Awi -> redirect to Aw
6	--- entry 2 ---
7	ROOT [Indo-European] Ayer, Aier, Aien : day, morning, early in the day  (refs POK:12; AHD:1507; OEW:3)
8	#1 (parent #0) [Avestan] refs=POK:12; AEF:376 | ayare : day ; prô-ayare : yesterday ☞Per 1
9	  #2 (parent #1) [Pahlavi] refs=AEF:376 | parěr : yesterday
10	    #3 (parent #2) [Persian] refs=AEF:376 | parîr «پَریر ( پریروز )» : yesterday ; pîrâr «پیرار ( پیرارسال )» : two years ago
11	#4 (parent #0) [Germanic] refs=AHD:1507; OEW:3 | airiz : early
12	  #5 (parent #4) [English] refs=AHD; OEW | early, ere, erst
13	--- entry 3 ---
14	ROOT Ayo -> redirect to Aw
15	--- entry 4 ---
16	ROOT Ayos -> redirect to Aios
17	--- entry 5 ---
18	ROOT Âysan -> redirect to Zay
19	
```


## [2026-09-05T05:44:11.467Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-74.json",
 "description": "Read source JSON for page 74"
}
```


### [2026-09-05T05:44:11.510Z] TOOL RESULT

```
{
  "pdf_page": 74,
  "book_page": 44,
  "entries": [
    {
      "root": {
        "name": "Awes",
        "redirect": "Aus 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Awi",
        "redirect": "Aw"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ayer, Aier, Aien",
        "lang": "Indo-European",
        "refs": "POK:12; AHD:1507; OEW:3",
        "gloss": "day, morning, early in the day"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:12; AEF:376",
          "words": [
            {"translit": "ayare", "gloss": "day", "script": null},
            {"translit": "prô-ayare", "gloss": "yesterday", "script": null, "see": ["Per 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "AEF:376",
          "words": [
            {"translit": "parěr", "gloss": "yesterday", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "AEF:376",
          "words": [
            {"translit": "parîr", "gloss": "yesterday", "script": "پَریر ( پریروز )"},
            {"translit": "pîrâr", "gloss": "two years ago", "script": "پیرار ( پیرارسال )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "پریر قبلهٔ احرار زابلستان بود - چنانکه کعبه است امروز اهل ایمانرا",
            "poet": "Nâser-Khosrow"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1507; OEW:3",
          "words": [
            {"translit": "airiz", "gloss": "early", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD; OEW",
          "words": [
            {"translit": "early, ere, erst", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ayo",
        "redirect": "Aw"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ayos",
        "redirect": "Aios"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Âysan",
        "redirect": "Zay"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T05:44:11.934Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T05:44:12.000Z] TOOL RESULT

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


## [2026-09-05T05:44:22.305Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','OEW','AEF','BRT','PHD','HRN','HUB','MON','BQT','ARY','KLN','SKT','WLD','IEC','SYN','NYB']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-05T05:44:23.924Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
```


## [2026-09-05T05:44:32.594Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_01 leaf 20/21 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==21' POK_01.txt | head -80\necho \"=== grep ayer/aier in POK_full ===\"\ngrep -n -i \"ā̆ier\\|aier-\\|ayer-\\|Tag, Morgen\" POK_full.txt | head -20"
}
```


## [2026-09-05T05:44:33.332Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins ayer ===\"\ngrep -n -i -A12 \"^ayer\\b\\|ayer-\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-05T05:44:34.640Z] TOOL RESULT

```
=== POK_01 leaf 20/21 ===
rüh- stück' (unkontrahiertes  äigidiov  noch  herstellbar  Hom.  ^  124,  7t  2) -^  dehn- stufiges *äii)sQL  in  der  Ableitung  '^SQiog  , morgendlich',  kontrahiert  in  ^ol , morgens'.     Anders  Risch  105.
Got.  air,  aisl.  är,  Adv.  , frühe'  (ebenfalls  Lok.  *aierL),  dazu  Kompar. got.  airiza  ,früher',  Adv.  airis  =  ags.  cer,  ahd.  er,  nhd.  eher,  ehe;  Superl. ags.  '^rest,  ahd.  erist,  nhd.  erst.
WP.  I  3,  Feist  24  b.
Vielleicht  zu  4.  äi-.
13
aJg'  ,Zieg-e'.
Gf.  «1?,  -y(^9  ,Ziege^  arm.  aic  , Ziege';   tiefstufig  n,v.  izaena-  ,aus  Leder* (eio-entlich  ,aus  Ziegenleder'  wie  gr.  aXysiog^  vgl.  die  gleichen  Bedeutungs- rerhältnisse  bei  *ago-  ,Bock').     Vielleicht  orientalisches  Kulturwort. WP.  I  8,  Specht  KZ.  66,  13.
1.  aig-,  ii''^s.  ing'  ,verstimmt,  unwirsch,  krank'.
Alb.  ke-ek  ,b(3se'  (aus  ke  +  *aig{o-) ;  lat.  aegeo-^  aeg7'a,  -um,  aegrötus  ,ver- stinimt,  unwohl,  krank';  anord.  eikenn  ,wild,  wütend',  ags.  äcol  , erregt, bestürzt',  nnorw.  eikja,  eikla  ,unaufhörlich  mit  Angriffen,  Widersprüchen, Behauptungen  plagen',  eikjen  , zänkisch';  toch.  B  aik{a)re  (=  lat.  *aegro-), A  ekro  , krank';
nasaliert  *ing-:  lit.  mgis  , Faulenzer',  mgas  und  angüs  ,faul,  träge',  lett. igstu,  igt  , innerlichen  Schmerz  haben,  verdrießlich,  mürrisch  sein',  ignet , einen  Ekel  haben',  ignls  , mürrischer  Mensch'  (lit.  engti  , würgen,  quälen' bleibt  wohl  fern);  aksl.  jedza  , Krankheit',  nslov.  jeza  ,Zorn',  poln.  jedza , Furie,  Hexe'  (,unwirsch'),  cech.  jezlnka  , Waldfrau'  (usw.,  s.  Berneker 268 f.;  auf  *jega,  nicht  '^aigä,  ist  daher  auch  zurückzuführen:)  russ.  bdba jagd  ,B[exe'  (s.  Brückner  KZ.  45,  318);
aisl.  ekki  , Schmerz,  Kummer'  ==  ags.  inca  , Schmerz,  Verdacht,  Streit', afries.  tnc  (d.i.  jinc)  , erzürnt',  auch  nengl.  inkle  , ahnen',  inkling  »Gemun- kel, Ahnung,  Andeutung,  Wink'.
WP.  I  9,  WH.  I  16,  843,  Trautmann  70.
2.  aig-  , Eiche'.
Gr.  alyiXo)ip  ,eine  Eichenart'  (s.  u.),  vermutlich  auch  'AQar-aiyog,  xqar- cciyojv  ,eine  unbestimmte  Baumart'  (etwa  , Harteiche').
Der  Ausgang  von  aiylXtüXp  scheint  X(b\p'  yXaiivg  Hes.,  vgl.  Xcortiov,  Xd)7T7], Xortög  , Schale,  Rinde'  und  Plin.  n.  h.  16,  6,  13  aegilojps  fert  pannos  arentes  . .  . non  in  cortice  modo,  verum  et  e  ramis  de'pendentes,  Kretschmer  Gl.  3,  335.
Anord.  eik  (kons.  St.)  f.  , Eiche',  as.  ek,  ags.  äc  (engl,  oak),  ahd.  eih, mhd.  eicli,  eiche,  nhd.  Eiche]
Alle  weitern  Anreihungen  sind  zweifelhaft:  gr.  Ixiyigog  (richtiger  als aYysLQog,  s.  Fick  BB,  30,  273)  etwa  , Zitterpappel'  könnte^,  als  , Zitterbaum' auch  Ableitung  von  einem  wie  oUtlqo)  gebildeten  '^atylgo)  , schwi
=== grep ayer/aier in POK_full ===
8884:Root / lemma: aier-, aien- 
8892:Root/ lemma: aier-, aien-\ "day, morning' derived from a reduced Root/ lemma: agher-, 
9040:See also: S. under ai-^^-, aier-, ajos-, aisk-, ai-tro- 
91243:See also: see above ayer-S. 80 f.; in addition Var-'m many FIN {Uer-).
```


### [2026-09-05T05:44:34.686Z] TOOL RESULT

```
=== AHD watkins ayer ===
134:The most widespread of the words for “night” was nek’-t-. Words for “day” include amer- and agh-? and such dialectal creations as Latin diés; ayer- refers to the morning. The old word for “darkness,” reg”es-, shows up in Greek as a term for the underworld.
135-The Indo-Europeans knew snow in their homeland; the word sneig”h- is nearly ubiq- uitous. Curiously enough the word for “rain,” however, varies among the different branches; we have words of differing distri- bution like seue-?, ombh-ro- and reg-?.
136-Conceptions of the sky, heaven, were var- ied in the different dialects. As we have seen, the root deiw- occurs widely as the divinized bright sky. On the other hand, certain lan- guages viewed the heavens as basically cloudy; nebh- is “sky” in Balto-Slavic and Iranian, but “cloud” elsewhere. Another div- inized natural phenomenon is illustrated by the root (s)tene-, “thunder,” and the name of the Germanic god THOR.
137-A word for the earth can be reconstructed as dhghem- (*dheghom). Other terms of lesser distribution designated forest or uncul- tivated land, like kaito- and welt- (wILD). Swampy or boggy terrain was apparently also familiar, from the evidence of the roots sel-es-, pele-', and *mdno-. But since none of these runs through the whole family, it would not be justifiable to infer anything from them regarding the terrain of a hypo- thetical original homeland of the Indo- Europeans.
138-On the other hand, from the absence of a general word for “sea” we may deduce that the Indo-Europeans were originally an inland people. A root mori- is attested dialectally (MERE), but it may well have referred to a lake or other smaller body of water. Trans- portation by or across water was, however, known to the Indo-Europeans, since most of the languages attest an old word for boat or ship, nau-?, probably propelled by oars or a pole (ere-', “to row”).
139-The names for a number of different trees are widely enough attested to be viewed as Proto-Indo-European in date. The general term for tree and wood was deru. The origi- nal meaning of the root was doubtless “to be
140-firm, solid,” and from it is derived not only the family of English TREE but also that of English TRUE. Note that the semantic evolu- tion has here been from the general to the particular, from “solid” to “tree” (and even “oak” in some dialects), and not the other way around.
141-There are very widely represented words for the beech tree, bhadgo-, and the birch, bherag-. These formerly played a significant role in attempts to locate the original home- land of the Indo-Europeans, since their dis- tribution is geographically distinct. But their ranges may have changed over several mil- lennia, and, more important, the same word may have been applied to entirely different species of tree. Thus the Greek and Latin cognates of BEECH designate a kind of oak found in the Mediterranean lands.
142-Of fruit trees in the usual sense, only the apple (abel-) and the cherry (ker-®) were known. Wine was made in the Mediterranean basin before the arrival of the Indo- Europeans, and the pear and the olive, as well as the grape, were cultivated. As immi- grants into Greece and Italy the Indo- Europeans adopted the names along with the fruits, and both were later widely diffused.
143-Indo-European had a generic term for “wild animal,” ghwer- (FERAL). The wolf was known and evidently feared; its name is subject to taboo deformation (conscious al- teration of the form of a tabooed word, as in English gol-derned, dad-burned). The vari- ant forms wlk’o-, *lupo-, and wlp- (also “fox”), are all found. The name of the bear was likewise subject to a hunter’s taboo: the animal could not be mentioned by its real name on the hunt. The southern Indo- European languages have the original form, rtko- (Latin ursus, Greek arktos), but all the northern languages have a substitute term. In Slavic the bear is the “honey-eater,” in Germanic the “brown one” (BEAR, and note also BRUIN).
144-The BEAVER was evidently known (*bhi- bhru-, from bher-3), at least in Europe, and the MOUSE (mds-) then as now was ubiqui- tous. The HARE, probably named from its color (kas-, “gray”), is also widespread. Do- mesticated animals are discussed below.
145-A generic term for “fish” existed, dhghi- (also peisk- in Europe). The salmon (laks-) and the eel (ang”hi-) were known, the latter also in the meaning “snake.” Several birds were known, including the crane (gere-?), the eagle (or-), the THRUSH (trozdo-), the STAR-
146-XX
--
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
318-[bassus. Low. Late Latin adjective (> Medieval Latin bassus, Old French bas, and Middle English bas), possi- bly from Oscan: BASE?, BASS?, BASSET!, BASSO; ABASE, BAS-RELIEF, (DEBASE).]
319-[bat-. Yawning. Latin root of unknown origin; probably imitative. 1. Latin *batdre (> Old French ba(y)er), to
320-battuere
321-yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
322-bhares-
323-outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
324-bhasko-
325-English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
326-bhel-?
327-canoe” or “split planking”), in Old English baz, boat, and Old Norse bdtr, boat: BATEAU, BOAT; (BOATSWAIN). 5. Nasalized zero-grade form *bhi-n-d- in Latin findere (past participle fissus), to split: -FID, FISSI-, (FISSILE), FISSION, (FISSURE). [Pok. bheid- 116.]
328-bheidh-. To persuade, compel, confide. 1. Probably Ger- manic *bidan, to await (< “to await trustingly, expect, trust”), in Old English bidan, to wait, stay: BIDE; ABIDE, (ABODE). 2. Latin fidere, to trust, confide, and fidus, faithful: FIANCE, FIDUCIAL, (FIDUCIARY); AFFIANCE, (AFFIANT), (AFFIDAVIT), (CONFIDANT), CONFIDE, (CONFI- DENT), (DEFIANCE), DEFY, DIFFIDENT. 3. Suffixed o-grade form *bhoidh-es- in Latin foedus (stem foeder-), treaty, league: FEDERAL, FEDERATE; CONFEDERATE. 4. Zero-grade form *bhidh- in Latin fidés, faith, trust: FAITH, FEALTY, FIDELITY; INFIDEL, PERFIDY. [Pok. bheidh- 117.] bheig-. To shine. An uncertain but plausible root. Greek phoibos, shining: PHOEBE, PHOEBUS. [Pok. bheigz- 118.] bhel-'. To shine, flash, burn; shining white and various bright colors. I. 1. Russian byelii, white: BELUGA. 2. Greek phalaros, having a white spot (> phalaris, coot): PHALAROPE. II. 1. Suffixed variant form *bhié-wo- in Germanic *bléwaz, blue, in Old French bleu: BLUE. 2. Suffixed zero-grade form *bhb-wo- in Latin flavus, golden or reddish yellow: FLAVESCENT, FLAVO-; (FLAVIN), (FLAVONE), (FLAVOPROTEIN). III. Various ex- tended Germanic forms. 1. *blaikjan, to make white, in Old English blécan, to bleach: BLEACH. 2. *blaikaz, shining, white, in: a. Old Norse bleikr, shining, white: BLEAK}; b. Old English biéc, bright: BLEAK?. 3. Ger- manic *blikkatjan in Old High German blécchazzen, to flash, lighten (> German Blitz, lightning): BLITZKRIEG. 4. *blas-, shining, white, in: a. Old English blxse, torch, bright fire: BLAZE!; b. Middle Dutch bles, white spot: BLESBOK; C. Old French ble(s)mir, to make pale: BLEM- Ish. 5. *blend-, *bland-, to shine, dazzle, blind, confuse, in: a. Old English blind, blind: BLIND; (BLINDFOLD), (PURBLIND); b. Old High German blentan, to blind, deceive: BLENDE; Gc. Old English blandan, to mingle: BLEND; d. Old French blond; blond: BLOND. 6. *blenk-, *blank-, to shine, dazzle, blind, in: a. Old English blen- can, to deceive: BLENCH!; b. Old French blanc, white: BLANCH, BLANK, BLANKET; BLANCMANGE. 7. *blisk-, to shine, burn, in Old English blyscan, to glow red: BLUSH. IV. Extended form *bhleg-, to shine, flash, burn. 1. Ger- manic *blakaz, burned, in Old English blxc, black: BLACK. 2. Zero-grade form *bhig- in: a. Latin fulgére, to flash, shine: FULGENT, FULGURATE; EFFULGENT, FOU- DROYANT, REFULGENT; b. Latin fulmen (< “fulg-men), lightning, thunderbolt: FULMINATE. 3. a. Latin flagrdre, to blaze: FLAGRANT; CONFLAGRANT, CONFLAGRATION, DEFLAGRATE; b. Latin flamma (< *flag-ma), a flame: FLAMBE, FLAMBEAU, FLAMBOYANT, FLAME, FLAMINGO, FLAMMABLE; INFLAME. 4. Greek phiegein, to burn: PHLEGM, PHLEGMATIC, PHLEGETHON. 5. Greek phlox, a flame, also a wallflower: PHLOGISTON, PHLOX; PHLOGO- PITE. [Pok. 1. bhel- 118, bheleg- 124, bhleu-(k)- 159.] bhel-2. To blow, swell; with derivatives referring to various round objects and to the notion of tumescent masculinity. 1. Zero-grade form *bhl- in Germanic *bul- in: a. Old English bolla (> Middle English boll), pot, bowl: BOLL, BOWL!; b. Old Norse bolr, tree trunk: BOLE}; c. Old Norse bulki, cargo (< “rolled-up load”): BULK}; d. Old High German bolla, ball: ROCAMBOLE; e. Middle High German bole, beam, plank: (BOULEVARD), BUL- WARK; f. Middle Dutch bolle, round object: BOLL; g. Middle Dutch bille, buttock: BILTONG; h. Swedish *buller-, “round object,” in bullersten, “rounded stone,” boulder, akin to the Scandinavian source of English BOULDER; i. possibly obsolete Swedish bulde, a swelling (see wer-1). 2. Suffixed zero-grade form *bhl-n- in: a. Germanic *bulJ6n-, bull, in Old Norse boli, bull: BULL); b. Greek phallos, phallus: PHALLUS; ITHYPHALLIC.
329-bhel-*
--
1437:EACH [ik- EAGER! ak- EAR! ous- EAR2 ak- EARLY ayer- EARN! esen- EARNEST! er-! EARTH er-2 EARWIG wegh- EASE yé- EASEL asinus EAST aus-1
1438-89
1439-EASTER aus-' EASTERN aus-! EAT ed-
1440-EAVES upo EAVESDROP upo EBB apo-
1441-EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1442-EDIBLE ed- EpicT deik- EDIFICE aidh-, dhé-1 EDIFY aidh-, dhé-1 EDITION d6- EDUCATE deuk- EDUCE deuk- EFFACE dhé-1 EFFECT dhé-1 EFFEMINATE dhé(i)- EFFERENT bher-1 EFFERVESCE bhreu-2 EFFETE dh@(i)- EFFICACIOUS dhé-1 EFFICIENT dhé-1 EFFIGY dheigh- EFFLORESCE bhel-3 EFFLUENT bhleu- EFFLUVIUM bhieu- EFFLUX bhlieu- EFFORT bhergh-2 EFFULGENT bhel-1 EFFUSE gheu- EFTSOONS apo- EGEST gerere EGG! awi-
1443-EGG? ak- EGLANTINE ak- EGO eg
1444-EGOIST eg EGOTISM EGREGIOUS ger-! EGRESS ghredh- EIDER &ti- EIDERDOWN dheu-! EIDETIC weid- EIDOLON weid- EIGHT oktd(u) EINKORN gre-no-, oi-no- EISTEDDFOD bheue-, sed-' EITHER kWo- EJACULATE yé- EJECT yé-
1445-EKE! aug-!
1446-EKE? au-2 ELABORATE leb-1 ELAND el-2 ELAPID lep-1 ELAPSE leb-1 ELASMOBRANCH el-3 ELASTIC el-* ELATE tele- ELATER el-3 ELATERITE el-3 ELBOW el-1 ELDER! al-3
1447-ENERGY
1448-ELDER? el-2 ELDEST al-3 ELECAMPANE wel-3 ELECT leg-1 ELECTUARY leigh- ELEVATE leg*h- ELEVEN oi-no- ELF albho-
1449-ELIXIR ksero-
--
1472:ERE ayer- EREBUS regW-es- ERECT reg-! EREMITE ere-2 EREMURUS ere-2, ors- EREPSIN rep- ERG werg-
1473-ERGO reg-1 ERGOGRAPH werg- ERNE or-
1474-ERODE réd-
1475:ERR ers-1 ERRANT ei-1 ERRATIC ers-1 ERRATUM ers-1 ERRONEOUS ers-1 ERROR ers-1 ERSATZ sed-1, ud- ERSE peie- ERST ayer- ERUBESCENCE reudh-1 ERUCT reug- ERUPT reup-
1476-ERYSIPELAS pel-4, reudh-1
1477-ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1478-90
1479-EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1480-EVERT wer-3 EVERY aiw- EVICT weik-5 EVIDENT weid- EVIL wep-
1481-EVOKE wekw- EVOLVE wel-3 EVULSION wel-4 EVZONE yds- EWE owi-
1482-EWER akwg-
1483-Ex! eghs
1484-EX- eghs EXACERBATE ak-
1485-EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1486-EXxO- eghs EXOCRINE krei- EXODUS sed-2 EXOERGIC werg- EXONERATE en-es- EXOPHTHALMOS okw- EXORDIUM ar- EXOSTOSIS ost- EXOTERIC eghs EXOTIC eghs EXPAND pete- EXPATRIATE peter- EXPECT spek- EXPECTORATE peg- EXPEDITE ped-! EXPEL pel-6 EXPEND (s)pen- EXPERIENCE per-4 EXPERIMENT per-4 EXPERT per-4 EXPIATE pius EXPIRE spirare EXPLAIN pele-2 EXPLETIVE pela-1 EXPLICATE plek- EXPORT per-2
1487-EXPOSTULATE prek- EXPOUND apo- EXPRESS per-5 EXPUNGE peuk- EXPURGATE peue- EXQUISITE quaerere EXSCIND skei- EXSECT sek- EXSICCATE seikw- EXTANT sta- EXTEND ten- EXTENUATE ten- EXTERIOR eghs EXTERMINATE ter- EXTERNAL eghs EXTINGUISH  steig-
--
1992:OR2 ayer-
```


## [2026-09-05T05:44:43.045Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==20' POK_01.txt | tail -30\necho \"########### NR==21 head\"\nawk 'BEGIN{RS=\"\\f\"} NR==21' POK_01.txt | head -12"
}
```


## [2026-09-05T05:44:43.558Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8880,8905p' POK_full.txt"
}
```


### [2026-09-05T05:44:44.667Z] TOOL RESULT

```
ben  w-St.  *aidhu- im  gall.  VN  Aedui^  air.  ded  , Feuer',  auch  als  MN;  lat.  aedes  , Tempel',  ur- sprüngl.  ,der  häusliche  Herd',  auch  aedis  =  maked.  äöig'  soxccoa  Hes. Vom  Verbaladjektiv  auf  -to-  stammt  wohl  lat.  aestäs,  -ätü  , warme Jahreszeit,  Sommer'  (aus  *aisto-tät-,  idg.  *aidh-to-)]  aestiis,  -üs  (aus  *aidh- tu-)   , Hitze,   Glut,   Brandung',   aestuare    , kochen,   wallen,   brausen';   agerm.
12
MN  Aistomödius  (,mit  hitzigem  Mute'),  ags.  äst  f.  , Dörrofen',  engl,  oast ,  Darre'.
r-Formans:  gr.  aid^rjo  ,die  obere  Luft'  (maked.  ddfj),  ol&qcc  ,der  heitere Himmel'  (maked.  dÖQaid),  aXd-qiog  ,hell,  heiter  (vom  Wetter)',  wozu  ab- lautend id-aQÖg  ,heiter',  ai.  vldhrd-  (=  vi-idh-rd-)  ds.
i-Formans:  gr.  aid-dXrj,  ald-aloq  ,Ruß',  maked.  iidalog',  unter  Annahme einer  Entwicklung  von  ,glänzend,  scheinend'  zu  , anscheinend'  stellt  man etwas  gezwungen  hierher  ags.  idel , eitel,  unnütz,  nichtig',  ahd.  ital,  nhd.  eitel.
Auf  idg.  *aidh-lo-  beruht  germ.  ail-  in  ags.  '^lan  , brennen'  zu  al  n. , Flamme',  und  in  ags.  celed  m.,  aisl.  eldr  (Gen.  elds)  , Feuer,  Brand'.  Aus verschiedenen  Entwicklungsstufen  des  ags.  celed  sind  cymr.  aelwyd^  bret. oaled  , Feuer,  Herd'  entlehnt  (M.Förster  Themse  487 2).  Mir.  äel  ,Kalk' könnte  aus  *aidh-lo-  entstanden  sein.  Doch  könnten  die  germ.  und  kelt. Worte  auch  direkt  von  der  Wurzel  4.  äi-  mit  -Zo-Suffix  gebildet  sein.
s-Formans :  es-St.  gr.  cad^oq  n.  ,Glut,  Brand'  =  ai.  Bdhas-  n.  ,Brennholz^
Weiterbildungen:  aisl.  eisa  f.  [* aidh-s-ön-)  , Feuer',  norw.  , Feuerstätte', mnd.  ese  f.  ,Esse,  Feuerherd^  (aber  ahd.  essa  ,Esse'  s.  unter  äs-  , brennen'); av.  aesma-  m.  , Brennholz'  (*aidh-s-mo-,  vgl.  ohne  s  ai.  idhmd-li  m.  ds.); dazu  halt.  *ais7niä  in  lit.  iesme  , Brennholz';  lit.  aisträ  f.  , Leidenschaft'; acech.  niesteje  (fem.  PL)  ,Ofen',  später  nistej  (mit  7i-Vorsclilag  durch  falsche Zerlegung  der  Verbindungen  *v^n-esteje,  v^n'estejach^^  Berneker  275)  aus *aidh-s-to-]  dazu  schwundstufiges  *idh-s-to-  in  slov.  isteje,  steje  PL  ,Ofea- loch';  nach  Johansson  IF.  19,  J36  auch  ai.  isiakä  .gebrannter  Ziegel',  av. istya-  n.  , Ziegel,  Backstein'.
Auf  Hndh-  gehen  zurück:  alb.  gag.  idliuns,  tosk.  idhete  , bitter',  tosk. idherim  , Bitterkeit,  Arger',   hidhite  PL  , Brennessel'  (Jokl  Studien  29).
WP.  I  5,  WH.  15,  20,  843,"  Trautmann  3,  Schwyzer  Gr.  Gr.  I  347.
Wahrscheinlich  zu  4.  ai-.
Hierher  gehört  auch  aish-^  falls  aus  aidh-s-k-  entstanden.
äier-,  Mien-  n.  ,Tag,  Morgen'.
Av.  ayavdj  Gen.  aycin  n.   ,Tag'.
(j\\  Lok.  *<i(i)e^t-  in  aQiocov  (aus  '^aieri-d-tom,  zu  ed-  , essen')  , F
########### NR==21 head
rüh- stück' (unkontrahiertes  äigidiov  noch  herstellbar  Hom.  ^  124,  7t  2) -^  dehn- stufiges *äii)sQL  in  der  Ableitung  '^SQiog  , morgendlich',  kontrahiert  in  ^ol , morgens'.     Anders  Risch  105.
Got.  air,  aisl.  är,  Adv.  , frühe'  (ebenfalls  Lok.  *aierL),  dazu  Kompar. got.  airiza  ,früher',  Adv.  airis  =  ags.  cer,  ahd.  er,  nhd.  eher,  ehe;  Superl. ags.  '^rest,  ahd.  erist,  nhd.  erst.
WP.  I  3,  Feist  24  b.
Vielleicht  zu  4.  äi-.
13
aJg'  ,Zieg-e'.
Gf.  «1?,  -y(^9  ,Ziege^  arm.  aic  , Ziege';   tiefstufig  n,v.  izaena-  ,aus  Leder* (eio-entlich  ,aus  Ziegenleder'  wie  gr.  aXysiog^  vgl.  die  gleichen  Bedeutungs- rerhältnisse  bei  *ago-  ,Bock').     Vielleicht  orientalisches  Kulturwort. WP.  I  8,  Specht  KZ.  66,  13.
1.  aig-,  ii''^s.  ing'  ,verstimmt,  unwirsch,  krank'.
Alb.  ke-ek  ,b(3se'  (aus  ke  +  *aig{o-) ;  lat.  aegeo-^  aeg7'a,  -um,  aegrötus  ,ver- stinimt,  unwohl,  krank';  anord.  eikenn  ,wild,  wütend',  ags.  äcol  , erregt, bestürzt',  nnorw.  eikja,  eikla  ,unaufhörlich  mit  Angriffen,  Widersprüchen, Behauptungen  plagen',  eikjen  , zänkisch';  toch.  B  aik{a)re  (=  lat.  *aegro-), A  ekro  , krank';
nasaliert  *ing-:  lit.  mgis  , Faulenzer',  mgas  und  angüs  ,faul,  träge',  lett. igstu,  igt  , innerlichen  Schmerz  haben,  verdrießlich,  mürrisch  sein',  ignet , einen  Ekel  haben',  ignls  , mürrischer  Mensch'  (lit.  engti  , würgen,  quälen' bleibt  wohl  fern);  aksl.  jedza  , Krankheit',  nslov.  jeza  ,Zorn',  poln.  jedza , Furie,  Hexe'  (,unwirsch'),  cech.  jezlnka  , Waldfrau'  (usw.,  s.  Berneker 268 f.;  auf  *jega,  nicht  '^aigä,  ist  daher  auch  zurückzuführen:)  russ.  bdba jagd  ,B[exe'  (s.  Brückner  KZ.  45,  318);
aisl.  ekki  , Schmerz,  Kummer'  ==  ags.  inca  , Schmerz,  Verdacht,  Streit', afries.  tnc  (d.i.  jinc)  , erzürnt',  auch  nengl.  inkle  , ahnen',  inkling  »Gemun- kel, Ahnung,  Andeutung,  Wink'.
WP.  I  9,  WH.  I  16,  843,  Trautmann  70.
```


### [2026-09-05T05:44:44.716Z] TOOL RESULT

```
References: WP. I 38, Trautmann 22. compare also aig-. 
Page(s): 6-7 

Root / lemma: aier-, aien- 

Meaning: day, morning 

Grammatical information: n. 

Note: 

Root/ lemma: aier-, aien-\ "day, morning' derived from a reduced Root/ lemma: agher-, 

aghen-, aghes- (oder oghereic): day'. 

Material: Avestan ayara. Gen. ay^nu. "day'. 

Gr. Lok. *aO)£pi- in apiarov (from * ajeri-d-tom, to ed- "eaf ) " breakfast ' (uncontracted 
depiGTOv still produceable Hom. Q 124, tt2)\ lengthened grades *C(0)£pi in the derivative 
n£piO(; " early morning ', contracts in npi "in the morning '. Different Risch 105. 

Gothic air. Old Icelandic ar. Adv. " early ' (likewise Lok. *ajeri), in addition Kompar. 
Gothic airiza^ earlier'. Adv. airis= Old English ^r. Old High German er. Modern High 
German eher, ehe, Superl. Old English aerest. Old High German erist. Modern High 
German erst.
```


## [2026-09-05T05:45:16.325Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT ayar ===\"\ngrep -n \"ayar\\|ayara\\|ayąn\\|ayan-\" BRT.txt | head -30\necho \"=== BRT paro-ayara / parō ===\"\ngrep -n -i \"paro.ayar\\|par\\.ayar\\|parô.ayar\" BRT.txt | head"
}
```


### [2026-09-05T05:45:16.402Z] TOOL RESULT

```
=== BRT ayar ===
2513:Pü.—  '»)S.  Cld.  Pron.  46.—  ig)  ALe  guten  ' '"'^  ''''?)'"  saoirayn  frar»uharois  Yt.5.91; Hd».;  NA.  ^a&J/i.     Pü,:  Jn /a  nitirUn-,   vgl.    92,  93   (wo  'tayäsal);  —   "/d  »rtiü   maoa- No.  10.  — ") Ungeschickte  Nachahmung  von  jrtw/id    a^i   j/^^'a   sindayartha   (sd.)    Vr-Ä "  -^^^  '5"  i(?).       a)  auf  die  a.  Person  bezogen:  =/«
2663:dva   danart  .  .  'va    (statt   ASn.!)    danan  ayar»   äjasaiti  °va  vä  xsapa  Aog.  5/;  —
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
3149:•  g.  ■"'a-xsyaiit- ■>  Adj.  ('nicht  herrschend', sva.)  'nicht  selbständig,  hörig':  xsayan- tascii  'yantasiä  (AP.)  "die  herrschenden und  die  hörigen"  Y.J5.4.
3583:—  ma%rym  spmttm  . .  pmrumca  . .  'r^mca V.  4.45;  45;  —  ahun?m  vairJm  . .  Tim sraoidyehya  (^^  frasrüiti  Y.  5. 14;  — apanmta  tiais^mi&A.)  G.3.T, —  'raheca yamahe  haplanhatdis  Vr.2/.o;  0,4^;  — ranuhlsla  a'A  .  .  hupaurva  (sd.)  vahehiS Ti/"  räsaintü  ¥.52.3;  —  aiwiea  'rim patiia  'rym  apsca  paurvalibya  "und  (man soll)  einen  zweiten  (Rüden)  und  dann noch  einen  weiteren  (zulassen)  und  zwar (soll  man  ihn)  gesondert  von  den  beiden ersten  (halten)"  V.  i^.  48.  3)  '>  der  Zeit nach 'der  spätere,  kUnftige'rja^a  mä  'racil (NPm.)  saoiyanis  stavqn  V.9.  2;  — yastä datrSMg  °rö  .  .  tarS.mqstä  "wer  darum künftighin  (eig.  posterior)^  den  D.  ..  auf- sagen wird"  V.  4:5. 11;  —  huzantSus  paiti •raya  YL  13. 134.  a)  mit  ayan-  n.  'der spätere  Teil  des  Tags,  Nachmittag':  */ra- \aire  ayqn  bavaiiii^A.)  hubar,rS  ..  a',a  "re ayqrt  duWirjm  ". .  dann  am  Nachmittag (kommt)  das  Unglück"  Aog.jJ.  A)  ASn. 'r?m,  'ram  und  IS.  °ra  als  Adv.  'postea, später,  künftig' :  yezi  nairyS  aukat  pasca hl  pourum  (sd.)  paiti.hin£öi^  paitisa  "r^m V.ÄSS;  v,%;  —  \mätyi^hy(r'ramimam dipim  patiparsiltiy  .  ,  BL4.8;6,  15,  ^.y,
3982:•  j.  'aiwyästay-  f.  'Begehen,  ZurUck- legung  (eines  Wegs)':  ctniat  ,  .  äbststtm ayatum  .  ,yä  */rayarme  vä  uzayärine  V3 *ayqn  'tis  at^ka^  ". .  dass  seine  (des  Wegs) Zurücklegung  ..  stattfinden  kann"  N.p.
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
4777:ahmst  sISi  dqn  (sd.)  trvjh  utayüitl  Y.  4I5. 10;  57.7,  44.18,  47.1;  —  0,a  haurvaia "rstäta  ySi  slö  /nlzd»n  asaonqm  parSMsti jasmtqm  Yt.  1.25;  —  mazS  (sd.)  avaKyai .  .  daidl  Aaurväd  Titätä  (GD.)  V.  5Ä 7.  a)  als  Bezeichnung  fiir  die  Speise der  Seligen*;'*  at  löi  ubl  haurvassa 3^ar?%äi  3  'r^atasca  (NS.)**  "und  deine beiden  werden  zur  Nahrung  dienen,  der Wohlfahrtstrank  und  die  Unsterbltchkeits- speise"  Y.,?4.  n.  A)  als  Gottheit  {Amasa Spmtd),  der  die  Sorge  für  die  nützUchen Pflanzen  anvertraut  ist  (SüErL:  vanas- patipatiliySi  aya  damaya  fraonnta  akurd .  .  vohu  manu  .  .  a£>m  . .  xsa%rpm  .  . ärmaitil  frä  kaurvatas  fra  'r>tatils  Y.57. 24;  —  vanät  haurvasca  °rstas^a  (NS.)" •wa  sUMtttca  farsmmla  Yt  ig.  96 ;  96 ;  — armaitfm  ..  haurvaiat^m  ..  'rsiatatsm  yaza- maide  Y.16.%;  JI.12,  S,  2.6f.;  —  mazdii dadat  akurö  haurvatö  'riiatascä  .-.  sarS Y. 31.21;  —  data  vj  'rjtSscä (NS.  als VS.)i> utaySitT {%A.)  kaurvatas  draonsY.33.9,;  — iaurvatas^a  'r)tatasca\t.4.i(f)  a)bes. i  in  Dualverbindung  mit  Aaurvatät-:  aya I  damaya  fraornnta  ahurd  masdä  .  .  fra ,  sp^nta  *armaitis/ra  haurvaia  °rHäta  (ND.) Yt.  JO.92;  —  sarBi  bszdyai  (&d.)  haurräiä I  "niaia  (ND.) . .  j?.  .  Y.44.17;  —  upa.- ßm^ti  (sd.)  haurvatä  °r>talä  (AD.)  Y.  45, .  5;  —  sp)ntayai  ärmatSe  haurvalbya  -ntat- '  bya  Yt.  7. 2 ;  H.  i.  7 ;  —  yS  spsntaya  arma- töis  yä  haurvatä  'ntata  (GD.)  Y.  70. 3 ; .  —  kaurvatasca  nö  'ritats,'''^ gTusca  tasiiö.. I  Vr.  g.  5,  a)  amir>tät5  (näml.  ayar?) heisst  der  7.  Monatstag:  S.  7.7;  vgl, 2. 7, ,  V.  7tt.3,  A  1)  als  Bezeichnung  für  die
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
4884:•  jj  £■  ayar-  n.:  s.  unter  ayan-.
4885:•  j.  ayara-  m.  Plur.  Name  der  Gottheiten der  Tage :  ra'iwqm  'ranqmca  '*  asnya- nqmca  mlhyanamfa  yätryanqmca  Y.l.iy;
4887:Ableit.  aus  ayar-.  —  Pu. :  1  röi,  —  >)  S.  noch ayan-  No.  2.
4888:•  j.  ayarv.dräjah-  n.  Dauer  eines  Tages': *;irr  vä  äzaili  (sd.)  'jS  vä  vaslryll  (sd.) "(so)  soll  man  ihm  (als  Strafe)  drei  (mit der  Peitsche)  diktiren  oder  einen  Tag  lang Feldarbeit"  N.  42,  *43  '>,  6g,  83,  loff;  6g.
4891:•  j.  ayar^.bara-  m.  'Tagesritt':  kaiHtca aisqm  apa'jzäranqm  *(dhwansat3m  °bara- nqm  hvaspäi  naire  ^ar^wnj/" und  jeder  die- ser Abflüsse  ist  40  Tagesritte  lang  für  einen Reitersmann,  der  gut  zu  Ross  ist"  Y.  ('5.4.
4917:*)  Ursprünglich  des  Fesis  der  Heimkehr  von Hirt  und  Herden  aus  der  Senne  (s.  u.).   Später ist    es    dem   Andenken    an   die  SchaiTung   der Pflanzen  geweiht   Der  letite  (30,)  Tag  fällt  auf den  30.  des  7.  Monats,    d.  i.  in  alter  Zeit  auf den  3.  Okiober,  heutzutage  auf  Mitte  ApriL    S. im  übrigen  unter  yüirya-  und  miuiySisaiH: Ableit.  aas  'a-yä%ra.  n.  (iura  V.  yä-)  'Heim- kehr',  als   Adj.  ftlso  'was  mit  der  Heimkehr in  Beziehung  steht';  s.  Roth  ZDMG.  J4.  704. j.  ayiri.dräjS  N.  43:  lies  ayari.dr',
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
5267:ai.  Srta-.raiUa,  iyatti :  irle,  fcchati;  np.  rasaii 'er  kommt'.  —  Pü.;  verschieden,  s.  No.  4,  5, 8-11,  14.  —  ')  S  I03  I.  1  c,  ii6.  IF.  3.  69. Statt  'yiit°,  d.  i-  iyar-,  wird  auch  "ayar"  und •yS.r'  geschrieben,  S  afirf.  11,  57.  —  »)  Statt fr*.  S  sö'if.  1.  K  I,  L4  haben  anch  V.  21.  5 («ira.  — J>Them.— 4>Pü.!  S/tctid,  ?,\i.:  falatili.
5422:•  p.  arta'xäaB-'a-'*  m.  EN.  persischer Könige,  i)Ar/axerxa  I,  Sohns  des  Xerxes: dJraya''i'a'usakyä  ''ii'ahyä  xsäyaiiyahyä pui:'(^'^  Am.i;  1;  —  ''i'a/iyii  x^ayar^ahyä
5728:ayar?)  heisst  der  27.  Monatstag:  'sna binzats  sürahe%.i.2T,  vergl  2. 27,  Y.  7Ö'. 6-  [Yt.7j.96:  lies  asns.:^anrats">.'\ KompA. ;  Ableit.—  Vgl.  aimd^amani-ZÜ.  — tü.äiniaii'  m.  'Stein;  Himmel',  6ian-:aia-  m. 'Stein;  Himmel';  np,  äsmäit,  samän,  —  S. auch  lU  asi,i^-a..  —  Pü.:  10«^-,  (lu  V.  6): sanken;  äsmän.  S.  noch  Xo.  3,  5.  —  ')  Ober die  gegenseitigen  Beiiehungen  der  Stamm- formen (S  /SSaa  2  mit  No.)  s.  JScnumT Ktit.  88.  --  ')  Them.  —  3)  Pü. :  soHg  i  sani;;ii mil  der  Bemerk.:  ail  kc  mcnSk  yauihinhyök -5:i:iti,i;  s.  daiu  Y.  57.  12,  Vt.  7?,  20.  — 4)  Aus  dem  vorher^.  Verbum  ist  ein  solches von  ähnlicher  Bed.  lu  ergänzen.  —  5)  Pü. : cn  äsmän  1  fraliim  dCim.  Wegen  asma  als  AP. 5.  JScitsimTKriLSgundV.^as.  Ich  halte  die Stelle  für  geslött.  —  6)  S.  auch  V,  5. 25,  wo das  Wort  für  Himmel  ausgefallen  ist.  — 7)  Nach  der  n-Dekl.,  S^ojBem.  — «1  S.  auch Vr.  tl.  2  mit  No.  5.  —  9)  BtHL  IF.  /.  63 Ko.  _   .0,  S.  unter  a!mS.i.^amaHt:
5901:•  j.  asnya-  Adj.  'auf  den  Tag  bezüglich': °yehe  pascaSa  anyehe  ra'^ivü  "im  nächst- folgenden Tagesabschnitt"  V.  7.4,  A)  m. Name  der  Gottheiten  der  fünf  Tagesab- teilungen**  und  derentsprechendenGebete: •ya  asavana  asake  ratavS  Y.  2.3;  17;  — 'yaeibyS  aiahe  ratubyS  Y.  /.  3 ;  —  ra'iivqm ayaranqmca  'yanqmca  Y.  r.  17.
5971:mit  ä  dnwS,  4  a;  yezi  näil  paitiiaraiti *%rl  vs  äsäiti  ayar»jiräjö  (sd.)  vä  vastryä£ N.  69;  ^2,  43,  <V?,  log'''.
5973:mWpaiti  und  a  dnwS.  4a:  yezi  nsi^  *'irT 7>il  paiti  asaili  ayar).dr3jö  (sd.)  vä  västryät
5975:ai.  ä/a/i,  ajj/älf.  —  Pü.;  nnitehUan;  t.  noch ^■o.  2,  3,  5.  —  ')  S  2^-  3.  'gl.  Var.  L4  hat mia  atSü.  —  »)  Pü.:  i.  unter  ayarf-äräjah-, — J)  Pü.i  a/xir  apätfHtnd,  Sü.;  apasUiayanti.  — 4)  Pü. :  fa  an  i  öi  tanättuhtiikänlh  300  [st  a/itr ianisnik  apar  iaiiiin  asf  ailr.  —  S)  Stveri. unter  iipizaita-.
6106:slahe  a)  (nändich  ma)  heisst  der  2.  Monat im  Jahr:  pait^aca  cdiwansatimca  tnaiyji- xar7mayehe  (sd.)  'saht  vaAisiaAe  dd^tisS ^3-  7-  ß)  (nämlich  ayari)  heisst  der
6263:äfaiÄ  Y.  7<?.2o; —  vahilt?m  akßm  'Saonqm raocaahpm  (Stverz.)  Y.  (J.19USW.;  —  xshätä 'saotiatn  urvänS  pärayänti  .  ,  avt  garö nrnaium.  V,/(),33;  *Y.  2.4,  *42.4;  —  kaur- TtUa  am^nläta  ySi  sis  mlzd?m  'saonam parSMsH  jasMiqm  Yt.  J.  25;  —  vJspim 'iavansfH  vahiltjm  ä  oAüm  ä.baraUi'S.24; — iäbm  *dä^aifi  urvqtam  'saonS  *irfn'^3- naht  F.  24.;  *_J5;  —  vis/ipm  "iavafum  .  . kvavayarsÄ^m  jas>nt»m  paiti.baraAi  Y.55. 4;  —  t3  ahmt  nm3ne ]amy3r?? yä  'saenqtn xtnstatca  aSayasca  Y.  60. 2;  —  ya^raca xihaa  'sava  Yt7y.36;  25;  —  -savamm ti  'iaonat  äfyeihyai  (sd.)  mraomi'^.-ji.\y, —  visp»m  'iavarum  vlspäi  'saone  para.- cinasti  Y.20.2;  a';  —  vahistim  'iovamm vaiüitäi  °iaone  Y-2/.4;  —  tumas?  tS dä'^rö  baxt»tn  vahistäi  -saone  anazq^äi 'sttone  V.  2M;  —  tumd  aAurSt  mazdäi tvms  atnsiaiikyS  spmtalibyS  rrnnS  anyailqm (sd)  'saonqm  V./().2s;  33.  Yt7.3o;  '— yähaZa  zhayenU  °Iaone  ahm  anasti  Y.  20. 3;  YL/J.  24;  —  amamm  ..  yas»  %ws  .. ynaite  6arö.taohrS  'sava  "das  Haus  des Gläubigen,  der  zu  dir  betet .  ."  Yt  /0.30; 56;  —  •savaram  vahistsmea  avasöjcla- 'inmca  Y.  ig.^a;  —  nSit  'savarum  aint^tii (sd.)  ästarayei/i  P.  12;  ^N.JOj?";  —  aipi.- Pänrnnäi  ,  .  'saone  V.S.ioj;  —  näämnäi (i&.)'säone'V .g.^o;  —  'iavanum  makrka%äi Y.  79. 1 2 ;  —  kaaa  nS  '/aum  agats  .  .  V. '5-  3  ' ;  Y.  7/.  1 6 ;  —  "iavansm  manaspaoiryS V.  19. 19  {?);  —  sava  'SavabyS  yazatnaide Vr.i^j.i;    Y.77.6'.  a)    von    nament-
6598:yä  oder_>'J(?)  vll.  sva.  'es  geschieht,  kommt vor,  dass  ..':  asit'i^  yä  *ayar3Aa^a  sparr/a (sd.)  YL/0.  laöGl.;  —  asti'*''  yS gavasnaAe (sd.)  snäuya  jya  Yt  10. 1 28  Gl.  III)  als j  Praedilcatsverbnm  (Kopula).  Das  Praedikat ist  I)  ein  Substantiv,  das  mit  dem  Subjekt im  Numerus  und  Kasus,  oder  ein  Adjektiv, das  auch  im  Genus  kongruirt.  A)  I  im Ap.  (die  Kopula  folgt  dem  Praedikat): adam  bardiyä'  amiy  .  .  adam  xsäya'iiya* amiy  Bh.  b,  h;c-f*,  h-j^,  Bh.  7.5,  11,  16', -■3>  S'  55.  13-  4.2*,  D.(t.4;  —  adam xsaya%iy£^  amiy  asagartaiy  ""uvaxstraAyä laumäyä  Bh.2.  i4,4.2,Bh.g,;  —  adamsäm xsäya^iyt^  äham  Bh. /.  6;  —  ka"bujiy<^ ,  .paruvam  idä  xsäya'^iya"  ähJ^  Bh. /.  10; —  g  *duvitäiaranam  (sd.)  vayam  xsäya- üyä  amahy  Bh.  j.  4;  —  tyaiy  paruvam xsäya'iiyä  aha"  Bh.  7.  4;  —  kalä  pa- ruviyata'  hyä  amäxam  taumä  xsäya'iiyä (sd.)  äh(^  Bh.  j.  3 ;  —  adam  pärta''  amiy D.  77. 3 ;  —  martiyJ^  Ayo*  draujana'' ahatiy  Bh.^.5,  14;  14,  5;  —  Äj'u*  daustä <Ua*.  .  hyi^  arika''  äha*  Bh. /.  8;  2.4,  6, 3-  II,  5.4;  —  tyaisaiy  fratamä  martiyä anusiyä  äha"täi'>  Bh.  ;.  13;  J.  7,  8,  11,  13, /.  7;  —  negirt:  ya^ä  naiy  arika"  äham Bh..:^.  13;  13  ^  —  ty^  adam  naiy  bardiya'' amiy    Bh.  7.  13.  B  [)    im   jAwr.    (Die
6603:*aAu>fia,ra  *ratumaca  Vr.  2.  7 ;  —  iva  asti spa  pasus.haumS  (sd.)  dsityS.gälul  V.  ;j. 1 7  ;  —  a?vahe  , .  anasaen^  zänu.dräja  asti a/riiisisd.)  V.lS.ii;  —  andvlm  ..y^  asti avat'aiti  mass yd^a  . .  Y.  65. 3 ;  —  astila  "' im  S.I  ataiti  bqzS  yavaiii  .  .  Y.ig.-};  — dvadasaf»hä'ir9m  asti  ayrim  ayar?  F.  27  b
6871:Am?l'a  (^tvm.,va.ttx A. R-a.)  Sp^nta:  rumas» ts  'ra  mazda  ,  .  rumS  vS  amiiä  spsntä  . . allal  *jih<tt  'r)m  mazdqm  astat  am»si spjnts  Ny.  1. 1;  Y.  68.22;  usw.  b)  im Gegensatz  zu  A/jra(sd.)Mainyav:  xihae- ^ra  "rahe  mazdh  laröidtti  anrahe  main- ySus  Yt./.o;  —  sna>ai  attrahe  maittySuL. /rada%äi  'rahe  mazdiY.2-j.\(.  2  K)aAu- rahe  ma-id?!  (näml.  ayarg)  heisst  der  i. Monatstag:  'rahe  mazda  raivatS..  S,/,i, Y.j.  ii;vgL/6:i,S.2. 1.  3)inGHapt.; 'ra-  ist  einmal  Ci-3S-l)  von  mazdäh-  ge- trennt, sonst  steht  es  unmittelbar  davor oder  dahinter:  huxsa'irS.timüi  ..  xla'hnm .  .  *hvqnmahicii  kyat  mazdäi  'rat  Y.J5. S;  s.  A,_j.  6;  —  mazdil  'rä  . .  kätqm  hu- dsslfmä  \.4i.  2, 4;  —  'rä  mazda.. vaahuda YjA'.4;—  vohü  xsa'hr»m  tsi  mazdä  'rä apaSmä  Y.^/.  a;  —  sralstqm  at  tSi  k»hr- pSm  .  .  ävaSdayamahJ  masdä  'rä  . .  avat yät  hvar!  aväcl  V.j6.6;  — yäsctJ  tsi gmä  *'ra.mazdä^''>  Y.  j8.  i;  ^5.  3,  9;  — hyat  mizdjm  *mafai^im  (sd.)  Jradadfiä .  .  masdä  'rä  V.40.  i;  i,  4;  —  läa  äl yazamaide  'rtm  mazdqm  y}  gqmlä  ahmiä dat..  Y.3-J.  i;  —  BitJ  yä  v3  ..  '1^  mazdh *nämqm  dadät  ..  Y.  ^JÄ  4;  —  dätdl  a/.. mazdä  'rä  . .  västryJng .  .  akmaj-afonat>hs (sd.)  Y,  4a.  3;  —  ya^ä  tu  l  *'ra.mazdä^^ minghäcä  .  .yä  vohü  diä  tSi  dadunahi . . a^ä  iiSidyämahl  ^wä  mazdä  'rä  Y.yp.4; j6.  5,  I ;  —  'rakyä  :l  at  vi  mazda  yas- n»mcä  .  .  amSAmaidt  . .  Y.J5. 7;  —  ^wDi staotarascä  ..  ^''ra.mazdä"'^  aggitnadailä  .. Y. 41.%;  —  ätari  vSi (sd.)  mazdä  'rahyä ahi  Y.J6.3; — äiar^  mazdä  akurahyäY. 36.1,  3.  a)  in  Verbindung  mit  n)  Asa (sd,,  unter  A  1  a)  und  ß)  Asa  (sd.,  unter A  1  0,  VohuManah  ua.:  a)  *'ra.mazdä"'^ d/ä  srTrä  Y.  J^.  $;  — stets  garS  vahmSrtg 'rät  mazdäi  asäicä  vahiääi  dadtmahicä Y.  41.  I ;  _95.  s;  —  mazdä  'rä  .  .  iava/ä sar)iit  asaliyäcä  Y.  41. 5  f. ;  40.  i  f.  ß)  yaza- maide 'rillt  mazdqm  . .  ahm  ..  vahislmt  .. 7ighucä  inanö  . .  vohttcä  xiäi^rim  . .  Y.  ^-j. I— 5-  4)  im  gAw.  (ausser  GHapt,), Es  sind  hier  die  Strophen  herangezogen, die  ^ahura-  und  'mazdäh-  im  gleichen Kasus  enthalten;  s.  dagegen  I  z.  Die Stellung  der  Wörter  ist:  ah'..m',  m'..ah' (in  beiden  Fällen  ist  die  Trennung  oft erheblich);  m°  ah",  ah' m'  (im  letzten  Fall trifft  stets  die  Zäsur  dazwischen:  Y.  2^.  9,
7034:kniipfiiDg  eines  adversativen  Satzes  'aber; sondern;  vielmehr;  gleichwohl':  iha  main- yete  dus:^armä  .  .  ä'  az3M  manya  Yt.  10. losf.;  —  nöil  .  .  vispa  yasathahs  .  .  ä' .  .  aÄ'J  zara%uitro  Vt.  IJ.  ig;  5,  55  aSt^', N.55,  Y./0.8,  ig.  5;  —  iä  fi-avasays  .. aojistä  hinti  .  .  yä  .  ,  saosyaniqm  ä° anyalsqm  fravasayö  (sd.)  ,  ,  Yt.  jj.  17; N.  102;  —  nabänazdists  ä'  kavatqm  nana (sd.)  N.  Ig;  g,  67;  —  «/  zaotars  (sd) kairim  avAap. .  3'  AävanänS  (näral.  kairim a»Aat)  yat .  .  N.  72;  73-'j6,  66'';  —  apqm . .  yä  para  ahmäi  hist>nta  .  .  ä°  th  nüram p-aiacin/i  Yt.  13. 5:i(.;  56,  5S;  —  aat{^.  8) yahmäi  xsnBtS  bavaiti  mi^rS  ahmäi  jasaiti avaiäAe  ä'  yahmal  ibistd  bavaiti  . .  akmüi früiiinäayeiti  nmämmca  ..  Yt/o.S?; yaike  xsa'hriäa  nStt  aotfiri  ar?ka  . .  para akmat  yat  . .  ä°  yat  ..  ". .  bevor  . aber  als  . ."  Ytig.$$f.;  — yat  hf puhi iissaySi^e  .  .  ikaisö  anyö  .  .  ä°  anys Y.g.ia;  —  tarS.d»nanS  (sd.,  näml.  urv rayä  aahari)  .  .  ä°  up»ma  aisöJräjanAa N.po; —  navajcsaparfm  ..  aivii^äi kama  mazäräjaAlmW.^.^2;'^.46,47,5o; —  nöit  ahmt  nmäne  *sänaite  ä^rava  .  . ä'  .  .  sayänie  dahaksea  "nicht  werden  .  , geboren  .  .,  sondern  es  sollen  geboren werden  .."  Y.  //.6;  —  käu  .  .  yff  .  .  van- tasea  Aqm.räzayeili  .  .  aha  diin  upaJaosa^ yati  .  .  raZiayaca  (sd.)  .  .  ä'  yat  .  .  var>- saica  *hqm.räzayar>Aa  .  .  aat  (s.  7)  .  . pascana  apa.baröis  ". .  vielmehr  wenn  du dir  die  Haare  ordnest  .  .,  so  sollst  du dann  . ."  V.iy.2—4;  —  attm  vispanqm dämanqm  nipäta  ahmi  .  .  ä'  ('gleich- wohl') ma  nöit  masyäka  .  .  yazante  YL 10. 54.  a)  bes.  mit  a)  folgendem  _ya/  oder
=== BRT paro-ayara / parō ===
```


## [2026-09-05T05:45:17.211Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD parer ===\"\ngrep -n -i \"parēr\\|parer\\b\\|paryār\\|paryar\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"\ngrep -n -i \"parēr\\|parer\\b\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T05:45:17.282Z] TOOL RESULT

```
=== PHD parer ===
=== NYB ===
```


## [2026-09-05T05:45:25.307Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD 'day before yesterday' ===\"\ngrep -n -i \"before yesterday\\|par[eēě]r\\|pyl\\b\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD ayar/ēr ===\"\ngrep -n -i \"^ēr \\|ayār\\|'day'\" PHD.txt | head -20\necho \"=== NYB search ===\"\ngrep -n -i \"yesterday\\|parēr\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T05:45:25.418Z] TOOL RESULT

```
=== PHD 'day before yesterday' ===
PHD.txt:321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
PHD.txt:549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
PHD.txt:649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
PHD_mackenzie.txt:770:aber ['pyl] very, much.
PHD_mackenzie.txt:1312:aweran ['wyl'n l , )pyl'n l I N weran] desolate, ruined.
PHD_mackenzie.txt:4163: payrayag [pyl)dk' I M pyr)yg, N periiya] ornament, adornment.
PHD_mackenzie.txt:4235:pil [pyt I M pyl, N --] elephant; (chess) bishop.
PHD_mackenzie.txt:4242:pir [pyl IN ......] old, aged, ancient.
PHD_mackenzie.txt:5310:weh [SPYL < A spyr; wyh I M why, wyh, N bih] better, good.
=== PHD ayar/ēr ===
126:read ma... N та) not. delete mādayār ... mānīg ... add house-owner.
225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
412:J jad [y’t'] share, portion. Yadag [ytk! | M jdg] omen. tļadaģ [ytk'] form, property. jadag [y’tk' | M del share, portion; case, cause. jadag-g5(w) [y tkgwb'] advocate, intercessor. ~ЛЬ : intercession. jadag-wihīrih [ytkwhylyh] transformation, alteration. Jadarih [y2?lyh] maintenance. *fadisn [ytsn'] (accidental) quality, property. ~ig [-yk'] accidental, non-essential. jadiig [y?te&! | M j?dwg, N jadi] sorcerer, magician. — h: sorcery, magic. *jay [у?л | N ~] sissoo tree. jagar [yal | N jigar] liver. Jah-, v. jastan. jahišn [yhysn' | J jhysn-] chance, fortune, omen. Jahišn-ayār [yhyfn hdyb'l | N n. pr. jhiy?r] fortunate. ~ih: good fortune. jahüd [yhwt' | N juhiid] Jew. jām [y m | N ~] glass. јат [M ANE < A mn-h; ут | M Pm, N <] vessel, goblet. lfamag [y”mk! | N јата) = *jām. атар [y mk! | М ртр, N fama] clothing, garment. jang [yng | M jnng, N ~] struggle, battle, fight. Jar [ywl | M рт] time, occasion. jastan, jah- [ystn!, yh-] happen, occur, chance (to be). ~išn, v. jahišn. Jašn [yfn! | N —] celebration, festival. jaw [ŠZ < A £% | N ~] barley. Jāwēd [y wyt! | (P ywyd), N ~] eternal.
439:~ith: femininity. *madag [mtk' | (M myg, N māya)] essence, substance. ~ig [-yÀ!] essential. ~war [-w/] essential, especial, principal. madan [mtn! | M mdn] come. madār [т comer. mādar [AMYtl < А т-у; mtl | M mdr, N ~] mother. imādayān [m!tgd?n! | М m'dy'n] book. *mādayān [m tyd?n'] essence, basis, core; essential, chief. mādayār [m tgd’l] steward; (chess) rook, castle. mādišt [m’tyst'] *matter, protoplasm. mādīyān [m’tyg?n | N ~] mare. may [my | N ~] hole, pit. magas [mks | P mgs, N ~] fly. ~ i angubén: honey-bee. magind [mkn'd | M mgyn(d)] shield, protection.
695:able, be — ayārīdan, šāyistan, P šah-;
755:agitate ayārdēnīdan. agitated, be — ayārdīdan. agitation ayārdēnišn.
1215:chess Catrang; (pieces) K šah, Q frazén, B pil, Kt asp, R mādayār, P payādag.
1489:dare ayārīdan.
2018:fortunate farrox, hangad, jahišnayār, xwarrahómand.
2258:help (n.) ayārīh, dastyārīh, frayād, frayādīšn.
2259:help (v.) ayārīdan, frayādīdan.
2260:helper ayār, dastgīr, dastyār.
3566:seethe ayārdīdan.
3815:steward mādayār.
4885:mādayār mādišt mādagīh mādagīg 1*mādag mādagwar mādar Abt, mex ābgēnag! mēhan mēzd may, meh Sahrestan! ‘mahist men- moymard! menidan mënög
5578:jahišnayār
=== NYB search ===
```


## [2026-09-05T05:45:26.932Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN parir/pirar ===\"\ngrep -n -i \"parīr\\|parir\\|pirar\\|pīrār\\|pêrêr\\|vorgestern\\|vorvorig\" HRN.txt | head -30\necho \"=== HUB ===\"\ngrep -n -i \"parir\\|pirar\\|vorgestern\" HUB.txt | head -20"
}
```


### [2026-09-05T05:45:27.014Z] TOOL RESULT

```
=== HRN parir/pirar ===
2974:811. perer Vorgestern, perejröz, pere\seb.
2978:fal'iväre 'im vorvorigen Jahre' (274, 2); bei. parerl^
3318:351. pfrär, pirar[sal *das vor vergangene Jahr.
=== HUB ===
1327:303. Slvend. para Vorgestern' (Journ. asiat. 1893, 294)
5912:parBr Vorgestern - ap. paruva- friiher + ^ayar-^ zd.
```


## [2026-09-05T05:45:32.600Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 2970-2985 ===\"\nsed -n '2970,2985p' HRN.txt\necho \"=== HRN 3314,3325 ===\"\nsed -n '3312,3326p' HRN.txt\necho \"=== HUB 5905,5925 ===\"\nsed -n '5900,5925p' HUB.txt"
}
```


### [2026-09-05T05:45:32.674Z] TOOL RESULT

```
=== HRN 2970-2985 ===
aw. pairlkä' *Hure'; phlv. parlk, arm. LW. parik,
LW. af/. parT.
Nach Bartholomae, BB. 15, 9 ist die SiW. pairikä-
ursprünglich *die Fremde'.
811. perer Vorgestern, perejröz, pere\seb.
Kilo, perc; pere]sdl, pe7^i]söUf per]sew^ pörijsd.
aw. '^parö.ayare; phlv. parer.
kurd. picne (Houtum-Schindler), per; oss. vergl.
fal'iväre 'im vorvorigen Jahre' (274, 2); bei. parerl^
paireri^ n. paln (285).
812. piSmanj pemän^ ptizmän (8ähn. I, 359 Note 2, Calc.)
'bereuend', pesiman,
ap. patü r *wawc/- ; phlv. pasTmän (paz. pasemän) ;
ai. /)ra^^ -i- y/'yw^w- 'erwiedern, entgegenhalten'.
Die Entstehung der Form pesJmän ist ganz unklar ;
piz'' scheint aber sicher auf patis hinzuweisen. Der
=== HRN 3314,3325 ===
n. peöäy (205).
350. plr alt, Greis', pTre,
phlv. plr, pin^ pTrak altes Weib' (PPGL).
kurd. afy. LW. pTr; hei, ptrük, n. plrük 'Grossvater'
(300).
Vergl. aw. parö^ "^parya- 'früherer 2).
351. pfrär, pirar[sal *das vor vergangene Jahr.
aw. '^para,yär' (+ säl),
352. pmrästen schmücken, anordnen , Praes. peiray-em.
pati+ [/'räd- (s. ärästm No. 11); phlv. peray(i)sn;
arm. LW. patrast,
353. perähen 'Hemd*.
phlv. patrahan *ßock' (Yätkär-T Zarir. 64 Note 53),
perähen (PPGL).
kurd. LW. pirun, perlen 'Hemd'; wa/. parhän, sar.
=== HUB 5905,5925 ===
Darayava(h)us, arm. Dareh, gr. /lageto^*^) (Tab. p. 3 und 6).
Die Form sah datirt vor dem 3. Jhd. p. Chr., da sie schon
durch die Hajrsbad-Inschrift {s(a)hpuhr) bezeugt ist.
b) -aya- wird zu e: arm. LW. mazdezn^ mazdSzn^MsiZ'
dayasnier, mazdayasniscli*, phi. M-zd^isn d. i. Mazdayasn
(alter) oder MazdBsn (jiinger), gr. Maadaavov (gen.) (Haug,
Essay on Pahl. p. 4) ; arm. LW. sen *Dorf , bebaut, bewohn-
bar , zd. — sayana- 'Wohnnng, Sitz* ; arm. LW. patdSn * Ab-
schrift, Kopie', phi. pacen Gl. and Ind. 95, hebr. pa&seyen^
zd. "^paiticayana- ; e aya im pr. cans., z. B. phi. daret
'halt, haltet' ap. darayatiy^ darayata (belegt ist ddraya-
miy, adaraya), vgl. Darmesteter, Etud. iran. I, p. 190;
parBr Vorgestern - ap. paruva- friiher + ^ayar-^ zd.
paourva- 'friiher + ayare 'Tag'?.
Diese Kontraktion ist vor dem 5. Jhd. p. Chr., viel-
leicht lange vorher vollzogen, wie das Armenische zeigt.
AVenn y aus J entstanden ist, unterbleibt die Kon-
traktion (in paig H. 359 -- arm. payik, maig H. 1010, pi-
yada H. 347, miyan H. 1004) oder tritt ein in: zer *unter,
paz. er, phi. gr (in ertan Phi. Min. p. 5, Z. 2 ; erlkan *die
niederen' PPGl. p. 9 Z. 4) aus *ayar (wie im Phi. auch ge-
lesen werden kann) -= zd. adairi, aiardt; bBva *Wittwe' (afgh.
*) daqsXoi und B^^lrjq (sohon bei Herodot) sind speeiell grie-
chische Umformungen der altpersischen Namen Darayava{K)u9 und
Xlayarsa,- 168 —
LW. beva)y phi. vBvak ZPGl. 5, Z. 3 = zd. viSava, Die Kon-
```


## [2026-09-05T05:45:48.734Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndef leafof(path, lineno):\n    txt=open(path,encoding='utf-8',errors='replace').read().split('\\n')\n    upto='\\n'.join(txt[:lineno])\n    return upto.count('\\f')\nfor p,l in [('HRN.txt',2974),('HRN.txt',3318),('HUB.txt',5912),('BRT.txt',4869),('POK_01.txt',0)]:\n    print(p,l,'leaf(0-based)=',leafof(p,l))\nEOF"
}
```


### [2026-09-05T05:45:50.226Z] TOOL RESULT

```
HRN.txt 2974 leaf(0-based)= 90
HRN.txt 3318 leaf(0-based)= 99
HUB.txt 5912 leaf(0-based)= 177
BRT.txt 4869 leaf(0-based)= 120
POK_01.txt 0 leaf(0-based)= 0
```


## [2026-09-05T05:45:59.129Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- HRN leaf 90 (awk NR==91) first+last lines ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==91' HRN.txt | head -4\necho \"...\"\nawk 'BEGIN{RS=\"\\f\"} NR==91' HRN.txt | tail -4\necho \"=== HRN leaf 22 = p1? ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==23' HRN.txt | head -6"
}
```


### [2026-09-05T05:46:01.093Z] TOOL RESULT

```
--- HRN leaf 90 (awk NR==91) first+last lines ---
— 69 — '
810. perl 'Perl, guter Genius*.
aw. pairlkä' *Hure'; phlv. parlk, arm. LW. parik,
LW. af/. parT.
...
bekommen habe.
814. pizohlden 'erforschen, nachfragen*, pizöh, pizöhis^).
Reime z. B. Sahn I, 73 Vers 215, Sälin. I, 140 Vers 198. Die
Wörterbücher wissea nichts mehr voa einem Majhülvooal.
=== HRN leaf 22 = p1? ===
Ä.
1. ä. 1) Praefix, z. B. in ämeden^ ardi/is.
ap. aw. phlv. ä; ai. d,
2) Praeposition , z. B. in her ä her, gird ä gird,
aw. ai. ä,
/2^' ab, ätv *Wasser ; vergl. slm]ab (*Quecksilber, wortl.
```


## [2026-09-05T05:46:08.865Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==100' HRN.txt | head -3\necho \"...tail\"\nawk 'BEGIN{RS=\"\\f\"} NR==100' HRN.txt | tail -3\necho \"=== HUB leaf 177 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==178' HUB.txt | head -3\nawk 'BEGIN{RS=\"\\f\"} NR==178' HUB.txt | tail -2\necho \"=== BRT leaf 120 head ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==121' BRT.txt | head -3"
}
```


### [2026-09-05T05:46:11.374Z] TOOL RESULT

```
- 78 -
LW. kurd. peyamher; af;'. paiyämhar\ oss. t.
pa/umpar, d, pexompar; hei, paiyam^ paiyambar (207).
...tail
Etymologie während der Correctur einfügte, hatte ich vergessen, dass
ich selbst später die gleiche Erklärung brächte. Inzwischen ist der
vierte Bogen gedruckt worden.
=== HUB leaf 177 ===
— 167
Kapitel 10: Kontraktion.
Die Lautgruppen : Vokal -f y oder v + Vokal bleiben
chische Umformungen der altpersischen Namen Darayava{K)u9 und
Xlayarsa,
=== BRT leaf 120 head ===
nalibya  ktivanaiibya  Vf. "    ■    "  "'        -teht  abseits.  '  70.2,  *N./07');  —  'Hlis  kant3ii\.4.t,o;
nsis/mis'  V.4-51; — gaoaniim  -nc
"  j.  aya-  ra.  i)  'Gang',         3)  sva,  'Mal' (der  Wiederholung)'*. KoiiipE.  —   Zum  V.  ay-.   —  Vgl.  frayäi  Inf.
```


## [2026-09-05T05:46:30.464Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==121' BRT.txt | grep -n -E \"^\\s*[0-9]{2,4}\\s*$\" | head\necho \"---- context around ayan- ----\"\nsed -n '4865,4890p' BRT.txt"
}
```


### [2026-09-05T05:46:32.462Z] TOOL RESULT

```
22:157
---- context around ayan- ----
dby  Google
157
ayanho-zasta-
•  j.  ayanhö.zasta-  Adj.  'mit  nietallenen (eisernen)  Klauen';  varäzahe  ('eines Ebers'; ayüahs^äiahe  'saslahe  Yt.  ro.  70.
•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
KompA.,  E,;  Ableit.  —  np.  vgl. /«/■«•  'vor- ßeMern',  GIrPh.  /  b.  34.  —  tEt.  s.  Btkl. Stnd.  3.  37.  Hbu.  ACJr.  /.  426,  Osthoff Sup^leÜTut.  69  No.  89,  JSCHMIDT  Plur.  sl6.  — PiL;  r^f';  !,  noch  No.  1.  —  ')  Hds.  (ni(in; P£.:  ankd,  VS.n.  119.— =)  Das  Y. /.  17,  bei. 2.  17  vorkommende  Wort  in  falscher  Ver- «endang ;  »gl.  lu  niähya-.  —  J>  In  der  Hds. steht  a  i  und  das  Nasalieichen  Nu.  33  der .Schiifltsfel  in  CIrPh.  I.  161,  das  auch  sonst statt  q  Torkomml,  Tgl.  zB.  V.  41.  6  Na  6 Aa  NA.
•  j.  ayana-  n.  'Gang,  iter";  ^vat  *ana dbHsl»m  'fum  parankaSäiti  "quantum  p!u- rimum  iter  .  ,"  N.^;  —  yme  paittsi^A!) garS  nm3nim  Yl_J.  4,
KompE.  —  Zum  V.  ay:  —  Vgl.  ayatiä-,  — «L  äfona-  n.  —  Pu.:  ras.
•  )■•  %■  ayant-  Adj.,  PPA,:  s.  ^ay-.  — ayaniim  als  Absol.  sbes.
KompE.  —  Vgl.  yaiii:
•  j.  ayanä-  f.  'Gang,  Weg  zu  -'  (Gen.): TshUlake  atghSus  vakistqm  'nqm  yaza- maidt  Wi.y.i.
Zqid  V.  a^-.  —  Vgl-  tt/ana-.  —  Pü.;  Jn  i fitilmm  iyiia,  erl. :  kiiniäk  ras  ö  änök.
•i-  ayantwn  Ab3oL*>  'beim  Gehen':  yaj
-  ayasnya-  158
aiteySi  rtiaedayasna  piloa{sd.)  ay  v3  taHn- tim  vS  barpmnpm  vS  vaz?mn)m  vä  taci.- apaya  (sd.)  iiasHum  frajasqn  "wenn  die M.  schreitend  oder  laufend  oder  reitend oder  fahrend  .  ."  Y.6.26;  Ä73.
Zum  V.  ay-.  —  Pii.:  ia  , .  pa  päi  raa/ättä (3Plur.),  ia  .  .fa  fä%  rawän  .  ./räc  raiänd.  — 'J  Vgl.  BtHL.  IF.  12.  145-
j,  ayayTi  N.  15%  lies  asaya;  %.  asä-,
•  j.  ayav-  Adj.  'alt,  in  einem  gewissen Alter  stehend':  nars  kthrpa  pattca.dasar»}iS .  .  taia  yaos  yäia  paoirJm  vTrim  avi  ya bavaiti  ".  .  eines  fünfzehnjährigen  Manns .  .  eines  so  alten,  wie  wann  dem  Mann zum  ersten  Mal  der  Gürtel  angelegt  wird" Yt.Äi4;  14'.
Vgl.  äyav  n.  'Alter'  und  JSCHMIDT  Plur.  142; idg.  *ajii  n.  und  *ajii-s  Adj.  (mit  urldg.  >, S  6$.  2).
•  jj  £■  ayar-  n.:  s.  unter  ayan-.
•  j.  ayara-  m.  Plur.  Name  der  Gottheiten der  Tage :  ra'iwqm  'ranqmca  '*  asnya- nqmca  mlhyanamfa  yätryanqmca  Y.l.iy;
—  ra/avS  vtspe  mazista  .  ,  °ra'^  asnya Y.2.17.
Ableit.  aus  ayar-.  —  Pu. :  1  röi,  —  >)  S.  noch ayan-  No.  2.
•  j.  ayarv.dräjah-  n.  Dauer  eines  Tages': *;irr  vä  äzaili  (sd.)  'jS  vä  vaslryll  (sd.) "(so)  soll  man  ihm  (als  Strafe)  drei  (mit der  Peitsche)  diktiren  oder  einen  Tag  lang Feldarbeit"  N.  42,  *43  '>,  6g,  83,  loff;  6g.
Pii.!  ^ianisn  alävi))  röf  drahnji  i  väsiryöiih; dazu  die  Erl.:  dzbannwfOanpn  (d.i.'Slrafe', jAMASPjl  Gloss.  1076),  s.  No.  2.  —  I)  Ild.s. ayäri'.  —  >)  D.  i.  das  Ideogramm  \tm  yaeihi. Das  Wort  ist  aber  falsch  gelesen  worden. Man  erwartet:  'Strafe  für  Nachlässigkeit,  Ver- säumniss  (in  religiBsen  Dingen)',
p.  ayai/ä   Bh.  J.  1 :   lies   äyasalä,   s,  yam- No.  3.
```


## [2026-09-05T05:46:42.651Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD par- entries ===\"\ngrep -n -o \"par[a-zāēīōū]*r \\[[^]]*\\][^.]*\\.\" PHD.txt | head -20\necho \"--- raw grep 'yesterday' ---\"\ngrep -n -i \"yesterday\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt UNV.txt SNS.txt 2>/dev/null | head\necho \"=== PHD lines containing 'parwardan' region ===\"\ngrep -n \"parr\\|parag\\|par \\[\" PHD.txt | head -5"
}
```


### [2026-09-05T05:46:42.864Z] TOOL RESULT

```
=== PHD par- entries ===
542:paristar [plsť] | N parastár] maidservant.
542:parr [pl | M pr, N ~] feather, wing.
542:parrwar [plwl | M prwr] winged.
542:parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings.
--- raw grep 'yesterday' ---
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD_mackenzie.txt:533:add dig [YTMAL < A Ptm'll N d~ yesterday.
=== PHD lines containing 'parwardan' region ===
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
386:e--rób [-lwp | N jārē(b)] broom. geän [HY A < А hy’; yn! | M gy’n, N jan] soul, ghost. ~ kandan: give up the ghost; moment of death. ~-abespar [-^5sp?! | N jān-sipār] reckless, desperate; devoted. ~ig [-yk! | M -yg] spiritual; vital. | ~war [-wl | (P -br), N jánwar] animate; animal.
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
```


## [2026-09-05T05:46:45.513Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT پریر ===\"\ngrep -n \"پریر\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -20\necho \"=== BQT پیرار ===\"\ngrep -n \"پیرار\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -20\necho \"=== MON ===\"\ngrep -n \"پریر\\|پیرار\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20"
}
```


### [2026-09-05T05:46:45.648Z] TOOL RESULT

```
=== BQT پریر ===
incoming/BQT/BQT_v5_pages.txt:994:س۱ آرد : وق پسر شادران » برادد زنگه «ام‌پریره7 ؛ پسر کیکاوس
incoming/BQT/BQT_v5_pages.txt:2445:۵ هز ۰2۵7 پهلوی ۰0476 پریر (یونتکر س ‎)٩۳‏ ۰
incoming/BQT/BQT_v4_pages.txt:5554:وفوقانی بروزن پریروفکن, بلفت زند وپازند(۱) مویندی - با ثانی مجهول بر وزن
=== BQT پیرار ===
=== MON ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:29947:پریر: 06۲-۲ (اصت.) (تد. اطفال) صدای 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:29957:پریره. (۵-)06۲06۲2 [- فر فره] (.) من 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:31604:پسان پریروز: 29-20-0212 (ق‌مر.) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:34402:پیرار: 17« (ق.) سال پیش از پارسال؛ دو 
MON_part1.txt:29947:پریر: 06۲-۲ (اصت.) (تد. اطفال) صدای 
MON_part1.txt:29957:پریره. (۵-)06۲06۲2 [- فر فره] (.) من 
MON_part1.txt:31604:پسان پریروز: 29-20-0212 (ق‌مر.) 
MON_part1.txt:34402:پیرار: 17« (ق.) سال پیش از پارسال؛ دو
```


## [2026-09-05T05:46:57.428Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON پیرار ctx ===\"\nsed -n '34398,34410p' MON_part1.txt\necho \"=== MON search پرير / پرير adverb ===\"\ngrep -n \"پریروز\\|پريروز\" MON_part1.txt | head\necho \"=== ctx 31600 ===\"\nsed -n '31598,31612p' MON_part1.txt"
}
```


### [2026-09-05T05:46:57.568Z] TOOL RESULT

```
=== MON پیرار ctx ===
هافهافو» هفهفو: ببری که دندان‌های وی 
ريخته» سخت پیر. پیر هشت جلد: (اخ.) 
( کد.) رضوان» فرشته موکل بر بهشت. پیر 
هفت فلکك: (اح.) ( کد.) زحل» کبوان. 
پیرار: 17« (ق.) سال پیش از پارسال؛ دو 
سال پیش از سال حاضر» ببرارسال. 
پسیراستن: 1-0 [- پیراییدن « 
پیراهیدن؛ این مصدر فارسی جانشین دو 


بیرامون 


=== MON search پرير / پرير adverb ===
31604:پسان پریروز: 29-20-0212 (ق‌مر.) 
=== ctx 31600 ===
سان بر بر وز 


بزرگان به روزهای عید و جشن‌ها و دیگر 
مردمان روز دامادی یا بازگشتن از فتحی یا 
ظفری بر سر می‌زدند؛ اکلیل ریحان؛ عمار 
پسان پریروز: 29-20-0212 (ق‌مر.) 
سه روز پیش از دیروز. 

پس‌انداختن: 2.2020 (مص م.) ۳ 
کردن» به تعویق انداختن. قسطی از دین رابه 
موعد ندادن. به بان افتادن حسض در زن. 
تولید فرزند کردن (در مورد توهین بکار 
رود)» تولید مثل کردن.
```


## [2026-09-05T05:46:59.417Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v5 line 2440-2450 ===\"\nsed -n '2438,2452p' incoming/BQT/BQT_v5_pages.txt\necho \"=== nearest [pdf page] tag before 2445 ===\"\nawk 'NR<=2445 && /\\[pdf page/ {p=$0} END{}' incoming/BQT/BQT_v5_pages.txt\ngrep -n \"\\[pdf page\" incoming/BQT/BQT_v5_pages.txt | awk -F: '$1<2445' | tail -2"
}
```


### [2026-09-05T05:47:01.440Z] TOOL RESULT

```
=== BQT v5 line 2440-2450 ===

ستون۲ سطر۱۳.4 -- باین هعنی ظ . مصحف « اسوان » است . ر4 .
ممجم‌البلدان » لغت نامه .

سطر ۰۱۵ اسود سالخ - عربی است . رك . لفت نامه .

سطرم۲ , آسور -هز . 891۷۳1» پادسی «پری دوز» « بندهشن . یوستی
۵ هز ۰2۵7 پهلوی ۰0476 پریر (یونتکر س ‎)٩۳‏ ۰

صفحه ۱۳۷ , ستون ۱ ۰ سر ۱۵ . اشتالنگ آ شتالنگ (ه .م .)

طرآخر » اشقر خار_ رك4 . خارشتر . خاراشتر » شترخارد .
[pdf page 72]
۷ برهان قاطم

=== nearest [pdf page] tag before 2445 ===
2374:[pdf page 70]
2410:[pdf page 71]
```


## [2026-09-05T05:47:17.259Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON 'دو روز پیش' ===\"\ngrep -n \"دو روز پیش\\|پس‌ فردا\\|پرير\" MON_part1.txt | head\necho \"=== BQT v1 variants ===\"\ngrep -n \"پرير\\|پریر\\|پريروز\" BQT_v1_pages.txt BQT_alt_v1.txt BQT_v1.txt 2>/dev/null | head\necho \"=== ARY ===\"\ngrep -n \"پریر\\|پیرار\" incoming/ARY/ARY_pages.txt | head\necho \"=== ARY latin index AYER ===\"\ngrep -n -i \"AYER\\|AIER\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-09-05T05:47:17.377Z] TOOL RESULT

```
=== MON 'دو روز پیش' ===
=== BQT v1 variants ===
BQT_v1.txt:30846:۱ ع2011 کنصطا۸ ر 2002061۳ باتی است پریر که » کلش سفید 
=== ARY ===
=== ARY latin index AYER ===
946:“DUB ayer 285 aydley,-4
3877:eel esetey LIT cal jt al aat a a sladhj etl 2 le a 2 teed eT ayery ay dae glsT jl Lda 4
5547:DELAMARRE: (EFFRAYER) 289 ERER (4leS(ARMENIAN) gu}
8486:INDHE, IN-DE :(OLD IRISH) 4S 543 p! AYER SPANISH) giles!
13084:DELAMARRE: (BEGAYER) 266 LULLE (DANISH) Sails
```


## [2026-09-05T05:47:19.408Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN ere/erst/early ===\"\ngrep -n -o \"ere, adv[^|]\\{0,400\\}\" KLN_1966.txt | head -3\ngrep -n -o \"erst, adv[^|]\\{0,300\\}\" KLN_1966.txt | head -3\ngrep -n -o \"early, adj[^|]\\{0,400\\}\" KLN_1966.txt | head -3\necho \"=== SKT ===\"\ngrep -n -o \"ERE, before[^|]\\{0,300\\}\\|Ere, before[^|]\\{0,300\\}\" SKT.txt | head -3\ngrep -n -i \"^EARLY\\|ERST,\" SKT.txt | head -5"
}
```


### [2026-09-05T05:47:21.139Z] TOOL RESULT

```
=== KLN ere/erst/early ===
=== SKT ===
20783:Versify,  Version :  see  Ve Verst,  a  Rus^nn  measure (Kass.)  Ruts,  venta^  3500  Cofl Vert:  sec  Verdant Vertebra,  Vertex,  V«Pt Verse.
```


## [2026-09-05T05:47:25.565Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index ctx 940-955 ===\"\nsed -n '940,952p' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== ARY_pages: find pdf page for printed 285 ===\"\ngrep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | sed -n '280,295p'"
}
```


### [2026-09-05T05:47:25.637Z] TOOL RESULT

```
=== ARY latin index ctx 940-955 ===
: US GOVE) «2930 b cperia she os ji chip Gleey geal 99 (SG ue ome
J Mater Thay Bae pls (ARES) cysts esl oy co lie y oblast
| her saclagb (CASTE) S100 js j3.24e6993 9 ytloy3,¢ al(ATHENA)
VAISYA tlnyy 9 (3L,s& >) KASHATRIVA ih sLisy 9 (3 sly) BRAHMAN
G55 Gal ow 6 SUL WET celacel Ab Sucstls aye y (ILS la ye y abs 4 abst)
Bia ge Oybe hol caith ae 5 obeel alal ya Seal gysTab BY oth opie
“DUB ayer 285 aydley,-4
OHwd Slo jl y id ya Sty glass
{DIEWS: os.) Jota) MED Sly Ate ad Soop ayy SSS sande)
OLS (SHUISH:c 2s JUPETER) 205 ftslin 9 (y20 ges DYAU ty Sale
Jala oer pty OL LUT sual, Jy tats slizel Obls g WL y te Saas ge
CesT pace Oble ile y0 2.9 acl shel Ab y SLL tay 9 gto U etlal, ae
Soc FleD 8 Due Hy 33 (LIMES) Cl ym SEF Yea aay pn ca asl
=== ARY_pages: find pdf page for printed 285 ===
8239:[pdf page 280]
8269:[pdf page 281]
8301:[pdf page 282]
8331:[pdf page 283]
8360:[pdf page 284]
8393:[pdf page 285]
8419:[pdf page 286]
8449:[pdf page 287]
8478:[pdf page 288]
8505:[pdf page 289]
8535:[pdf page 290]
8564:[pdf page 291]
8593:[pdf page 292]
8626:[pdf page 293]
8655:[pdf page 294]
8685:[pdf page 295]
```


## [2026-09-05T05:47:27.856Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 'ere' ===\"\ngrep -n \"ME\\. er, ær\\|OE\\. ǣr\\|OE\\. aer\\|airiz\" KLN_1966.txt KLN_1971.txt | head -10\necho \"=== KLN erst ===\"\ngrep -n -i \"erst\" KLN_1966.txt | head -5\necho \"=== SKT early ===\"\ngrep -n -i \"Early\" SKT.txt | head -5"
}
```


### [2026-09-05T05:47:27.950Z] TOOL RESULT

```
=== KLN 'ere' ===
KLN_1971.txt:59768:cresse, fr. OE. aerse, cerse, cresse, rel. to MDu. 
=== KLN erst ===
48:One  example  may  suffice  to  prove  this.  Despite  the  fact  that  Tocharian  (this  language  extinct long  ago  but  newly  discovered  at  the  end  of  the  Nineteenth  Century)  occupies  a  very  important place  among  the  Indo-European  languages,  Tocharian  references  appear  only  quite  excep¬ tionally  in  the  etymological  dictionaries  of  the  English  language.  This  is  so  much  the  more  strik¬ ing,  because  Tocharian  may  help  us  understand  the  development  of  many  a  word  in  the  different Indo-European  languages,  inasmuch  as  the  words  of  the  Tocharian  language  often  represent the  transitory  form  —  ‘the  missing  link’  —  between  the  Old  Indian  and  the  other  Indo-European languages.  In  this  dictionary  Tocharian  words  are  regularly  referred  to  together  with  the  other Indo-European  equivalents.
49:English  belonging  to  the  great  family  of  the  Indo-European  languages,  it  is  quite  evident that  in  tracing  any  word  to  its  source,  an  etymological  dictionary  must  take  into  consideration all  the  important  cognates  of  this  word  in  the  other  Indo-European  languages.  If  we  want  to understand  the  history  of  an  English  word,  we  must  compare  this  word  with  as  many  corre¬ spondences  as  possible.
1009:Samuel Savoyard Scandinavian scilicet  (L.,  ‘understood, namely’)
1223:abreast,  adv.  —  Formed  fr.  a-,  ‘on’,  and  breast, abreovoir,  n.,  an  interstice  between  stones  ( ma¬ sonry ).  —  F.,  lit.  ‘a  watering  trough’,  fr.  abreu-
1332:Derivative:  accept-ant,  n. acceptation,  n.,  1)  acceptance  (archaic);  2)  the meaning  in  which  a  word  is  usually  understood. —  F.,  fr.  Late  L.  acceptationem,  acc.  of  accep- tatio,  ‘a  taking,  receiving’,  fr.  L.  acceptatus,  pp.  of acceptare.  See  accept  and  -ation. acceptation,  n.,  formal  remission  of  a  debt ( Roman  law);  remission  of  sins  (theol)  —  L. acceptildtio,  often  written  in  two  words :  accept f latio,  ‘formal  remission  of  a  debt’  (from  the formula  acceptum  fero  used  by  the  debtor).  The first  word  is  the  gen.  of  acceptum,  ‘receipt’,  prop, neut.  pp.  of  accipere,  ‘to  receive’,  used  as  a noun;  see  accept.  L.  latio  gen.  -onis  ‘entering of  money  paid’,  lit.  ‘a  bearing,  bringing’,  is  form-
=== SKT early ===
59:gwd  against  becoming  obscure.  In  my  opinion,  the  habit,  frequently adopted,  of  citing  supposed  cognate  words  (often  misspelt)  wifhcmt j^wy  wla/  t/uir  meanings  art,  is  a  very  bad  one,  and  leads  to  guess- il^  and  vagueness.  It  is,  accordingly,  to  be  understood  that,  when  I do  DOC  give  the  meaning  of  cognate  words,  it  is  because  their  sense a^Teeft  «ith  that  of  die  English  word  so  nearly  as  to  prevent  ambiguity. Tbos  tmder  bik,  which  is  derived  from  the  A.  S.  bitan^  to  bite,  I  cite ihr  ri..P....  Icelandic,  Swedish,  Danish,  and  German  forms  without ci  because  ihey  all  mean  precisely  the  same  thing;  but  the
98:§  i.   The  words  8eleot«dL      The  woH-Jist   contains   nearly the  wonts  of  most  frequent  occurrence,  with  a  few  others  that remarkably  prominent  in  literature,  such  as  uitaneUd.     Homonymi forms,  such  as  bay  (used  \wjivc  senses),  are  numbered.
556:alder-,  prefix,   of  all.    In  at^ir- (Sh.);    here  aider  is  for  alter,  A.  S. gen.  pi.  of  fd/j  all. almighty.  ».£.)     K.S.  eal-miMtig. almost.  <E.)    A. S.  ealmJtst,  i.e. qriM the  greatest  part,  nearly  all.
713:Annals.   {F.  —  I..)     F.  am -L. /I'-'"'""  -'  -'■' yearly yearly  -
755:Anlelopu.  vGk.)  In  Spenser,  F.  Q.  i. fi  J^.  iS.-iicI  to  be  corniptcd  from  latt  Gk. ilrfiaAi>»-,  or  d.vBnXon-,  the  stem  o^  uv&t\Ka/\tf or  lii^uAo^,  used  by  Eiifitathitu  of  Antiodi to  signify  *  bright*  eyed,'  i.  c.  a  gucUe Coined  from  Gk  dftfiif,  lu  iprout.  iNoaom, aUo  lo  shine;  nnd  w\f/  'gen.  iuir(^t\  the  eye. See  Auiher  and  Optica.  ^  Tlic  word Dorau,  tilt*  Gk.  and  Roman  name  of  the gazelle,  IS  from  SV^ico/icu,  1  see  clearly.
```


## [2026-09-05T05:47:37.275Z] TOOL CALL #27: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T05:47:37.282Z] TOOL RESULT

```


```


## [2026-09-05T05:47:38.444Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY pdf page 284-285 ===\"\nsed -n '8360,8420p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-05T05:47:38.496Z] TOOL RESULT

```
=== ARY pdf page 284-285 ===
[pdf page 284]
دو ۲ / ۲۸۵

| چماگلیس سوازی ان ی را 30
اوستایی (۷ل4۲2874): 0 2۷۸ بک20۸ آلمانی (/058014): ان ارم
پارسی‌باستان (۶88۶4۸ صا0): 017۷171۸ انگلیسی کهن (بلدلبا2070 صا0): 7
پهلری (۲7مالطمه): 2 انگلیسی (ل8ا8۸/01): 70
آوستی (0535716): 22 دانمارکی (4ل0۸73): 70
کردی (80157)): [آ0 ,0 سوئدی (8(75057): 72
بلوچی (اتلناملمه): 01 نروژی (۸/0837501۵۸): 70
افغانی (پشتو) (/۸70۸۸۷): 2۷۸ ملندی (0777617): 7

تخاری 4 (4 7( 707۸). اد رها اسلاوی کهن (ع]۷بما5 ۲771786/7 0ل0):
تخاری 8 (8ظ /(۵ل7۸7ل708): ۷ 6 217۷۸
سانسکریت (54۸/980/7): 2۷2 ,لا20۷۸ لهستانی (۳0/57): 0۷0۸ ,0۷۸
آرمنی (4/4ا۵/78۸): زد دا روسی (/185140): 8 ب0۷۸
یونانی 08880): 0 ,06 چکه (4ل280): 8 ب0۷۸ 1
لانین (/70مل): 0۸ ,010 اسلواکی (51.01424): -0۷81 م80۷۸
فرانسه (تل/۳22): اد لیتوانی (42هلا )+ 0,71
اسپانپایی (82۸(7/8[3): 205 ایرندی کهن لکلا ۰:02 00 ,تاْ2
ایتالیایی (4(۷ل7۸): 218 گالی (#اقلالامه): ۷ ,ت00
رومانی (0۱/۸24۷): 2 ,00 آلبانی ((۸ا/لمهله): 00 ,2 ,ل05
پرتغالی (۳0700010885): 2005 هبت (177/78): 20 ب7۸
گرنبکه (007/0): 7۷۷۸ ,7۷۷05 بل7۷/۸

ایسلندی کهن (2010۸/40نفه صاه): پسگشت‌ها 5
8 ق7781 8 ۸005200
ست ساکسونی کهن 5420000 صا0): 9 (7۷۵) +8
۰ ار ,1۷805 3 053 :ما05
فریزی کهن (۶7/53 ام 8 (1۷0) ات ام ند» ها
,71۷805 2 (0۷۵ :005
آلمانی کهن (/088(/۸ 1013 صا0): 6 (3۷۵) وا ند ام
0 ,2۷۷25 برهان قاطع : ۸۸۸
[pdf page 285]
۶ ود
پهلری (1مالله): 0۸07 00 روسی (7551۸7ا): ی ی
کردی (۸08/01577): 7 ,0 صربی (52881۷): 01
بلوچی (1للتاملم8): 207 برهمی (/80118/1142): 3
آفغانی (پشتر) (۸۳07۸(1): ات لیتوانی ((مالس‌تزرم: 01۸5
تخاری 8 (8 ۸لگه7ل707). ند با از ۷ ترنی (لتی) (7۲1۸ا): 01
سانسکریت (5(/987077): پروسی کهن (۶554(7 0ا0): 012118
1 ,107311 ایرلندی کهن (لاکلها صط0۲):
پونانی 07250): 705 5 017۸1۸673۸
لاتین (7/0۷ا): 2/15 هنیت (7177178): 71118131۸ ,7118
فرانسه (۳6۸/677): اند ان دا
اسپانیایی (5۳۸۸//374): 110 پسگشت‌ها 5
ایتالیایی (7۸(۸۸۷): 70 زن ۳
رومانی (#721۸(1(۷)+ اد 3 (۲۸8) تاک ان ان
پر تغالی (۳087001582): ۴۸۸۸ 2 (5ظا۲0) هام05
ساکسونی کهن (/(540 0۵ 03۸1۸0۲ 3 (5310165) 22 ( 21۸0
آلمانی کهن (05721۸ 2۷۲07 ا۳01:16:)0 73 8
انگلیسی (6۸/0//874)(از فرانسه) ‏ ۲1:۸8 34 تا
اسلاوی کهن (۲12ما5 #77نابل صا0): ۸0
11 م0۷26 41 (8578۸31) ,225 (۴0۵6)
لهستانی (374/.ا(۳0): 27 برهان قاطم + ۸۹۳
یادداشت:
چم این واژه در برخی از زبان‌های هند و اروپایی: بخار» روح.
اوستایی (/47887۸): پارسی باستان ((۳2781۸ صا0):
7 ,ق008۸ ,0185 218 بف018
[pdf page 286]
دوزخ ]۲۸۷
```


## [2026-09-05T05:47:44.204Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C%D8%B1",
 "prompt": "Give the full Persian entry for پریر: etymology (Middle Persian form, Avestan/Old Iranian reconstruction), meaning, and any cited sources."
}
```


## [2026-09-05T05:47:45.851Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%A9yer",
 "prompt": "Give the reconstruction, meaning, declension and the descendants listed (Avestan, Greek, Germanic) for this PIE root page."
}
```


### [2026-09-05T05:47:46.046Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T05:47:47.621Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T05:47:49.787Z] TOOL CALL #31: WebSearch

```json
{
 "query": "wiktionary Proto-Indo-European *h₂éyer \"day\" Avestan ayarə Gothic air reconstruction"
}
```


## [2026-09-05T05:47:50.340Z] TOOL CALL #32: WebSearch

```json
{
 "query": "wiktionary پریر Persian \"day before yesterday\" etymology Middle Persian parēr"
}
```


### [2026-09-05T05:47:57.210Z] TOOL RESULT

```
Web search results for query: "wiktionary Proto-Indo-European *h₂éyer "day" Avestan ayarə Gothic air reconstruction"

Links: [{"title":"Reconstruction:Proto-Indo-European/h₂ey- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey-"},{"title":"Reconstruction:Proto-Indo-European/yóh₁r̥ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/y%C3%B3h%E2%82%81r%CC%A5"},{"title":"Reconstruction:Proto-Indo-European/geH- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/geH-"},{"title":"Reconstruction:Proto-Indo-European/h₂eydʰ- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82eyd%CA%B0-"},{"title":"Reconstruction:Proto-Indo-European/éǵh₂ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%A9%C7%B5h%E2%82%82"},{"title":"Proto-Indo-European language - Wikipedia","url":"https://en.wikipedia.org/wiki/Proto-Indo-European_language"},{"title":"Reconstruction:Proto-Indo-Iranian/Áryas - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C3%81ryas"},{"title":"Proto-Indo-Iranian language - Wikipedia","url":"https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language"},{"title":"Avestan","url":"https://en.wikipedia.org/wiki/Avestan"},{"title":"Proto-Indo-Aryan language","url":"https://en.wikipedia.org/wiki/Proto-Indo-Aryan_language"}]

Based on the web search results, I found some relevant information about Proto-Indo-European reconstructions. While the search results don't contain a specific Wiktionary entry dedicated to the exact root *h₂éyer "day," they do reference related Proto-Indo-European roots and their reconstructions.

The Wiktionary reconstruction pages mention *h₂éyr̥ ("day, morning") as a related form. This appears to be a Proto-Indo-European root that is semantically related to "day."

The search results show that Wiktionary contains extensive comparative material from various Indo-European languages, including Avestan and Gothic, used to support PIE reconstructions. However, the specific entry you're looking for with the exact form *h₂éyer and its Avestan (ayarə) and Gothic (air) cognates was not directly found in these search results, though the page on *h₂ey- and related roots does discuss various reconstructions from these languages.

If you're looking for more detailed information about this specific etymological entry, you may want to visit the Wiktionary reconstruction pages directly, as they contain comprehensive comparative data from ancient languages including Avestan and Gothic forms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-05T05:47:59.562Z] TOOL RESULT

```
Web search results for query: "wiktionary پریر Persian "day before yesterday" etymology Middle Persian parēr"

Links: [{"title":"پری - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C"},{"title":"پریروز - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C%D8%B1%D9%88%D8%B2"},{"title":"پیر - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1"},{"title":"پیش - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B4"},{"title":"پر - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%BE%D8%B1"},{"title":"Parvardigar","url":"https://en.wikipedia.org/wiki/Parvardigar"},{"title":"How do you say \"”today” ”tomorrow” and ”yesterday”\" in Persian? | HiNative","url":"https://hinative.com/questions/6229119"},{"title":"day before yesterday - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/day_before_yesterday"},{"title":"Persian - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Persian"},{"title":"Par%C4%AB","url":"https://en.wikipedia.org/wiki/Par%C4%AB"}]

Based on the search results, here's the etymology information you were looking for:

The Persian word پریر (parir, parêr, "day before yesterday") comes from Middle Persian 𐬞𐬭𐬌𐬭 (prir /⁠parīr⁠/), which means "the day before yesterday" and derives from Proto-Iranian *parāyarah, composed of *para- +‎ *ayarah ("day").

The word ultimately traces back to Proto-Indo-European *h₂eyer- ("day, morning"), with a comparison to Avestan 𐬀𐬫𐬀𐬭𐬇 (ayarə̄, "day").

The word is cognate with various related forms across Iranian languages, including Mazanderani پره (pare), Bakhtiari پری (parey), Bashkardi پریر (parir), Kermanic پره (pare), Baluchi parērī and pairērī, Northern Kurdish pêr, and Central Kurdish پێرێ (pêrê).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T05:48:04.266Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C%D8%B1%D9%88%D8%B2",
 "prompt": "Full Persian entry for پریروز: etymology, the Middle Persian form parēr, Proto-Iranian reconstruction, meaning, and descendants/cognates listed."
}
```


## [2026-09-05T05:48:05.801Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey-",
 "prompt": "What does this page say about the root *h₂ey- and derived noun *h₂éyer / *h₂éyōr 'day'? List descendants (Avestan, Greek, Germanic)."
}
```


### [2026-09-05T05:48:09.531Z] TOOL RESULT

```
# Persian Word: پریروز (Pariruz)

**Meaning:** This Persian term functions as both an adverb and noun, referring to "the day before yesterday."

**Etymology:** The word combines two Persian elements: پری (pari/parê, meaning "day before yesterday") and روز (ruz, meaning "day"). Its roots trace back through Proto-Iranian and ultimately to Proto-Indo-European *léwk-os.

**Pronunciation:** In Iranian Persian, it's pronounced as [pʰæɾiːˈɾuːz].

**Word Class:** Categorized as a Persian compound term, it functions as both an adverb and noun related to temporal reference.
```


### [2026-09-05T05:48:12.669Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂ey-

## Root 3: "Day/Morning"

The page identifies **Root 3** as relating to "day" and "morning." The reconstruction is **\*h₂ey-**, with an alternative form **\*ay-**.

## Derived Forms and Descendants

The document lists **\*h₂óy-r̥ ~ \*h₂éy-ns** as a derived noun meaning "day," with the following attested descendants:

**Avestan:** "𐬀𐬌𐬌𐬀𐬭𐬆 (aiiarə, 'day')" — descended from Proto-Iranian **\*Háyr̥**

**Germanic:** The page references Proto-Germanic descendants through Kroonen's etymological dictionary but doesn't explicitly list Germanic forms for this root in the displayed sections.

**Greek:** The page mentions **\*h₂éy-eri** meaning "early, in the morning" as a derived term, though specific Greek descendants aren't detailed in Root 3's section.

Note: The page contains three distinct homonymic roots with the same spelling (*h₂ey-), covering life/vitality, giving, and day respectively.
```


## [2026-09-05T05:48:18.518Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ere",
 "prompt": "Full etymology of 'ere', and any related entries for 'early' and 'erst' shown on the page (Old English ær, Proto-Germanic *airiz, PIE root)."
}
```


## [2026-09-05T05:48:19.422Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/early",
 "prompt": "Full etymology of 'early' (Old English ærlice, ær, Proto-Germanic *airiz, PIE root)."
}
```


### [2026-09-05T05:48:23.935Z] TOOL RESULT

```
# Etymology of "Ere"

The word "ere" originated around 1200 from Old English *ær*, meaning "soon" or "before (in time)." 

**Linguistic Ancestry:**
The term traces back through Proto-Germanic *airiz* (a comparative form of *air*, meaning "early") to the Proto-Indo-European root *ayer-, which refers to "day" or "morning." This root also generated related words across Germanic languages, including Old Saxon, Old Frisian, and Old High German variants.

**Related Words:**
The page documents connections to several derivative terms:
- **Erstwhile**: Combines *erst* ("first, once, long ago") with "while," documented from the 1560s
- **Early**: Formed from *ær* plus the adverbial suffix *-lice*
- **Aristology**: Incorporates the Greek *ariston* ("breakfast"), itself derived from the same PIE morning-time root

The etymology demonstrates how this ancient temporal concept evolved across Indo-European languages while maintaining its fundamental association with daybreak and temporal precedence.
```


### [2026-09-05T05:48:24.324Z] TOOL RESULT

```
# Etymology of "Early"

The word "early" traces back to Old English *ærlice*, meaning "near the initial point of some reckoning in time." This combines *ær* (meaning "soon, ere") with the adverbial suffix *-lice*.

The root *ær* descends from Proto-Germanic *airiz*, a comparative form of *air* ("early"). This Germanic root ultimately derives from the Proto-Indo-European root *ayer-*, which means "day, morning" and also produced related words in Greek, Old Norse, and other ancient languages.

The phrase "early bird" dates to the 1670s, referencing the familiar proverb about catching something before others do.
```


## [2026-09-05T05:48:29.036Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1%D8%A7%D8%B1",
 "prompt": "Full Persian entry for پیرار: etymology (Proto-Iranian reconstruction, elements), meaning, cognates."
}
```


## [2026-09-05T05:48:29.578Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/erst",
 "prompt": "Full etymology of 'erst' (Old English ærest, superlative of ær, Proto-Germanic, PIE *ayer-)."
}
```


### [2026-09-05T05:48:30.842Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T05:48:36.733Z] TOOL RESULT

```
# Etymonline: Etymology Dictionary Resource

Based on the web page content provided, **Etymonline** is an online etymology dictionary offering "quick and reliable accounts of the origin and history of English words" that are described as "scholarly, yet simple."

## Key Features:

- **Alphabetical browsing** (A-Z word listings)
- **Search functionality** for word origins
- **Multiple access options**: website, Chrome extension, iOS app, and Android app
- **Premium membership** available
- **Community engagement**: forum, columns, and social media presence

## Example Etymology:

The page references the word "*erst*" (meaning "formerly"), tracing it back through Old English *ærest*, then to Proto-Germanic origins, and ultimately to Proto-Indo-European *ayer-*.

## Support & Information:

The site is maintained by Douglas Harper and Talia Felix (copyright 2001–2026) and provides documented sources for all etymologies. Users can support the project through Patreon donations, premium subscriptions, or merchandise purchases, keeping the core resource "free and open."
```


## [2026-09-05T05:48:45.318Z] TOOL CALL #39: Bash

```json
{
 "command": "ls site/pages/74.jpg 2>/dev/null; pdftoppm -f 74 -l 74 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg74 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T05:48:46.623Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/par%C4%81yarah",
 "prompt": "Proto-Iranian *parāyarah: reconstruction, meaning, components, and descendants (Middle Persian, Persian, Kurdish, Baluchi)."
}
```


### [2026-09-05T05:48:47.727Z] TOOL RESULT

```
site/pages/74.jpg
total 7104
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 01:48 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56073 Sep  5 01:48 pg74.png
```


### [2026-09-05T05:48:49.504Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T05:48:53.654Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg74.png"
}
```


### [2026-09-05T05:48:54.335Z] TOOL RESULT

```

```


## [2026-09-05T05:48:54.329Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T05:49:15.846Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 aier ===\"\ngrep -n -i \"äier\\|aier\\|ai̯er\\|ayer\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"=== WLD Bd3 register ===\"\ngrep -n -i \"aier\\|ayer\" WLD_band3.txt | head -10\necho \"=== IEC aier/aien ===\"\ngrep -n -i \"aier\\|aien\\b\" IEC.txt | head -10\necho \"=== SYN early/ day 14.41 ===\"\ngrep -n -i \"airiz\\|Goth. air\\b\" SYN.txt IEC.txt | head -10"
}
```


### [2026-09-05T05:49:15.967Z] TOOL RESULT

```
=== WLD Bd1 aier ===
447:     aier-, ctien- n.                    ..Tag, Morgenfriihe'':
466:   Mit aier- lautet nach Noreen Urg. Ltl. 59 vielleicht ab idg. *jcr-, *ijjr-
9405:Ltl.  89 ablautend mit *aier- „Tag“); russ.-ksl. jura „Frfihling“, russ. jan
19044:in    und von zvischenvok.                         t       zu    i    zu *iinaicr-, weiter zu *inaier-.           *naier-
27650:                    waurstw n. .AYerk“, (*waurh-stica-\ iihnlich av. varitva-
67828:(3. pi. Aor. pass, z payer )  zevSco, zevdigg s. u.
77182:kvlsl f. „gespaltener Zweig oder AYerkzeug, Arm eines Flusses" (dies mit
=== WLD Bd3 register ===
975:gelynin) ayer. 265°,
2997:Ecke goitie- 35). | einwickeln 7. ty 208, ‘ee 131", | Einwilbung 2. gew- 370, i. bher- 102", einzdunen 3, tyer- THO. oragvto702". | Eis 2. eis 108, Eien ihhewo- 165. jay 208, Ehre |. guni- 506. peiee- 620. Ehre erweisen dek’- 782. hoe AZ8*. ren l.gtei- G08. | aagenie) 1. oN 478. ehiffirehtiy ecln 2, aid- 13 Eiche 2. aig- 10, | erm 24 cilern 4. ayer- nao, dere ery Se ghers- G10. o emrplinden ort hl Kiehel = 3. vel 602.
3137:icp oad spa bu 113°. qaeip- Hil. echmmntzfarhi I, wa- SLE. I, gAes- 546; ptbin aaa*, omer aa 2 ayer A2a* eee ke ne) *To*. 2 gragi-n18. | a. | Kae fel 436, " Tags). 424°, | sckimuteiggran Soak 489°. gel " fey"). 421",  schmu t = a. qrex- 400, ‘aohlingen arc 380°, Schmutzstreifen ghrii- 646. grek- 453. Lage- G00",  schnalverad lecken Li). 383*, =. qrel- 484. L. awd 7TH", schosppen (nach Luft) L. grems- na, aohluoken Me 7 Gla. : cig. i = 2 gthem- O79. dewi(c))- 380" wchnarchen sremb- TOG. feleh- 748. | sch i. Meonraees. cckeaahent Niner ere ae a hea Se", | ae tirene bes . er a tui 747. seus 7108. titeu- 2198, a. dhen- S53 alewj- TIL". | achnoobend bAdr{o)}- 191"
3144:bhowdi- TRG". | 5 wil ., k= 7. aegh- a = Et 465. gqan- 351, . dhery pati 526, ruy- 374" gd Om 3 ok 270" FA 40, 3 ‘ete 517 steig- Dias aper- G09". * 716", Spite agro- 38. ee usse 1 wndbke B18 ie . Mra ab h- phd i misdid- 301". bend- 1Og* itre 2. agel- SDG*. bharea- 151° Schwnr 3. feugh- 415%, | Somm lato- 427°, . 6. bher: 162" gechs aka 522%, Ronis _ sduel- 446°. | npitzos stegh- 822° Saline gahei- B70, 3. del- BOD. J. ayer: B27" pula 604. bheid- 138%. | (foieelich)  eyegth- 110, wehnlich rerlangen méfudA- ne 403 *, TT". (lant) epel- aes seihen veik- 466°. Phe ite (te Baie) 125 ee x aeiye 407°. . apreizen e) (s) Seihvorrichtnng E'or- 462. (a)plei- 604°. elitr wlendo- 314° | Spanne der Hand I. der-7iM. Bprongcen , wer eves, sein ¥ e- 160. a PaArin lamp, 72], mh jor- G70". Relte ) 5°. 1. deny 724. at, Giz*. efos- 427° tengh- 726. splhiersd{h) senken rail. sek. 473° lena- 127. setzen 2. ghz. S26 l. api{i)- 655". | eprieBen  1..yeda- 240: sentzen -, Omg L. (#}pen- G60". 2 bhel- 17" J. sper- BAS*, 1. bhrew- 105% Byer 474. | Spaten lagh- 361*. 1. bhreus- 197* 601". | Specht iiyiae S8r apt h)er(e)-g- fais Th ange aighthar eobn - f* lL. aper- 805" apringen Bic ee epalen | fem 282 oe aes a ii. dher- sicben. vb, spt 87 Bpeiseberrii 4 lead rene: 1S" i meer Spel | ed my ih x malt Pa s aineh 408. Sperling 2 eper- 608" 2. (aer- 506° sieden wish een a apingo G82" (elke. pales , det d bal epcrren re j bs & ad nia, . = P slodoln pei 504. — itpielerts 1. rebh- aT0". (lobhaft) la 420°,
3215:sappelo 1. aplAjer- — eusamminsinken md Zo! Has? , ago-2, odo. | hi Leer Soo". ne y eat — 2, .er- ae sullen esa | 2. ter 728. qajo- $86, | zunehmen ayer, aur
=== IEC aier/aien ===
321:aier-, aier- “morning; early, WP I, 3 Gk. eri; Go. air; OE ær
974:brékio ‘cry’ Du. praaien, LG praien, id.; Latv. brēcu, brēkt, id.
3869:Li. gagü, eti. Cf. *gagaio in Blg. gagam; Latv. gagaju, id. gagos (gaglis) ‘knob, lump, berry’; as adj. *lumpish, boorish’ Alb. gogël “berry, oakapple'; gogé ‘boorish’; Sw. koka (&clod'. Ambig. cf. gogos); Li. gõgas ‘Jump, hump; withers’; Icel. kaekur, m. (' vice. Mod. -æ- for ON -ce-) gāið (1) ‘croak, caw'. WP I, 526. Cf. gauið, gouo Skt. gāyāmi ‘sing’; cf. G kaien ‘prattle’; keien “blub, weep’; OCS gajọ, ati ‘croak, caw’ gāið (2), see gígāmi gàios, à (1) “raucousness, cawing; jay, mag- pie, or other raucous bird’. WP I, 526. Cf. gaio (1) Skt. gayah ‘song’; Arm. čaj, Lat (jay, with induced palatalism); Lat. gaius, gaia “jay, mag- pie; G (short vowel) Kai ‘prattle’; Norw. Sw. Scots kaja, kaie, kae ‘jackdaw’; E caw; R gaj ‘caw’. Cf. Ukr. Zaj-voronok Clark fr. *gēi-); Pol. ga-wron, Cz. ha-vran ‘raven’ gaios, om (2) ‘pace, gait'. Cf. gígàmi, ghàio. WP I, 526 & 677 Skt. gayah, adj. ‘striding’; Av. gàyom ('pace', also 'yard-measure)); (ambig.) Cz. hej-no, OCz. hajno ‘flock’; (ambig.) cf. Li. góju, son ‘amble, wade’; Latv. (ambig.) gāju Cl went, but Arm. gaci, id. is fr. ghai-, q.v.); cf. also gājums ‘gait, track’; gājējs ‘pedestrian’ galdāið, galdeio ‘bawl, exuit, howl’. Skt. gardāmi, Av. garəd- (1); Alb. (denom.) galdoj ‘exult’; Lat. gallo, are (‘rave���, but poss. denom. of gallus, cf. gagol-); MHG kalzen, kelzen *bawl'; kelz “loud talk’; OFris. kaltia “talk”; Du. kouten chat": kout, s. id.; R. cf. galdét ('brawl', but the phonol. is irregular) galið *shout'. Cf. gald-, galu- Gk. cf. a-gállo ‘glorify’; MHG kallen ‘shout, chatter, sing, croak’; Du. G kallen ‘chatter’; LG kohlen, id.; Tirol. kallen ‘bellow, rut; OE ceallian: ON kalla (“calP', etc.). Cf. also Alb. galé ‘rook’; Br. gal-dü “black sea-bird"; OE -calla *-crier'. (Ambig. or variant in Skt. járe, Av. jar- ‘creak, rustle; call’, cf. &el-) galuó ‘call’. Cf. galið, gald-; galuos, s. Skt. cf. garvah ‘pride’; Br. galv ‘appeal’; W galw ‘call, vocation’; Ir. (?) gailbh ‘squall’;
4900:ghreiió (1) ‘grab’. Cf. ghreimn, ghres-, (ghrs-), ghreim- (1) Gk. cf. khráo, fut. khréso (1) ‘seize’, get: Du. graaien ‘filch, scrounge, scrabble’; Li. grieju, -ti (1) ‘grab’; cf. greitas ‘quick’
9621:leio (4) “stir, move” Oss. ráin, Dig. irajun ('seethe, surge; rejoice’ in phr: mà zàárdá rat ‘my heart rejoices’); Alb. luej, luaj, tr. ‘move’. Isophonic (but ambig.) Du. laaien, laien, v. ‘blaze, flame’
10506:meio (2) (moio) ‘mow’. WP II, 259. Cf. meto, ið Gk. cf. amáo, fut: améso, id. (fr. *sm-9); cf. ámetos, m. (“mowing, crop’: OE mb, n. id.); MHG mæjen, mawen, v. id.; OE mawan, sv. 7, id.; Du. maaien, id.; Sw. mäja, v. id.
11602:694. Cf. snë- Hitt. n&ya(mi), v. (2) ‘turn’; Gk. néo, fut: néso ‘spin’; Lat. neo, nere, id.; Cor. nedha, v. id.; W nyddu, Br. néza, id.; cf. W nedd, pl. nydd, f. ‘spinner; whirligig; OHG naen, MHG najen & næwen ‘sew’; Du. naaien, id.
15137:seið (sið) (pp: sətós) 'sow'; seio ‘sowing, seed-time-. WP II, 459. (Variant sëu-. Cf. se- dhlom, sətós) Lat. cf. Sēja, f. ‘goddess of seed-time’; sévi, pf. ‘I sowed’; W hau, inf. ‘sow’; Go. saian, sv. 7., id.; MHG sæjen, sæwen, id.; OE sawan, sv. 7., id. cf. OHG sājo, wm. 'sower'; Du. zaien (zaaien), v. id.; ON sá, v. id.; OCS (and com. Sl.) sějọ, sějati, v. id.; Li. sēju, seti, id.; Latv. seju, set, id.; cf. Li. sēja, f. (sowing": Lat. Sēja). (Denom. in Br. hada, inf. ‘sow’, see sotós)
16551:sneio ‘twist, spin’. Cf. néio, snaio. Gk. Lat. & W. Br. ambig. (Gk. cf. nén, inf.; Lat. neo, ere, W gwnio, inf. id.; Br. néza, id.); implicit in Olr. sníim, v. (2) 'interlace'; cf. sním, Ir. sniomh, m. *weav- ing’; Du. (?) snaaien, v. ‘pilfer’; ON cf. snælda, f. ‘spindle’
17042:Oss. cf. sixin, Dig. sexun, v. “sway'; W cf. chwi, pl. -on, m. ‘swerve’; LG schwaien, v. ‘sway at anchor’; Du. zwaaien, tr. ‘brandish’; intr. ‘sway’; Fris. swaeije, id.; Norw. svaie, v. ‘swing’; OCS (variant) xvéjo se, xvěti se, v. ‘shake, tremble’; Cz. chvét se, inf. id.; Pol. chwiać sig ‘totter
=== SYN early/ day 14.41 ===
SYN.txt:8990:1. Grk. dpicroy, orig. ‘breakfast’ as in Hom., later ‘lunch’ : jpx ‘early’, Goth. air ‘early’, NE ere, etc.; -oro- fr. -d-to-, pple. of *ed- ‘eat’. Walde-P. 1.3.
SYN.txt:23910:4, OE @rest (NE erst ‘in former time’), OHG G@risto, MHG ér(e)st, NHG erst; superl. of Goth. air ‘early’, OE @r (NE ere), OHG ér (NHG ehe) ‘early, former- ly’, hence orig. ‘first’ in time. Walde-P. 1.3. NED s.v. erst, Weigand-H. 1.405, 469.
SYN.txt:24479:Grk.  xput Goth. air Lith.  anksti
SYN.txt:24505:4. Goth. air, ON ar, epds. ON arla, Grlega, Sw. arla (poet.), OF dr-lice, ME erliche, erli, NIE early, beside comp. in OE @r, ME er(e) (often with positive force) : Goth. airis, OHG ér ‘before, earlier’, all perh. as ‘early in the morn- ing’: Grk. #épios ‘of the morning’, jpt ‘in the morning’, Av. ayara ‘day’, root connection dub. Walde-P. 1.3. Falk- Torp 8. Feist 24 f.
SYN.txt:25292:tainly those of the large inherited | léto ‘year, summer’ (14.73). Walde-P. ze denoted the -bright ‘day’ vs. | 2.427. Pedersen 1.133. Thurneysen, ie Kit and only secondarily (like ‘sum- | Gram..35, 180. Pokorny KZ 50.43 if ne ss ‘winters’ for ‘years’) the com- (taking lae as of different orig., but cf. wehensive 94-hour ‘day’ (for which | Vendryes, RC 42.234 f.). Dan., Sw. have distinctive forms). 4. Goth. dags, ON dagr, OE deg, 1. Derivs. of IE *dei- ‘shine’, rare in | OHG fag, etc. general Gmc. (also derivs. verbal forms (Skt. 3sg. imperf. adzdet, Goth. fidur-dogs ‘of four days’, OE dégor etc.), but widespread in words for ‘sky, | ‘day’, ON degr ‘12-hour period, day or heaven’ as Skt. nom. sg. dydus and the | night’, Dan. dégn, Sw. dygn (the last two personified Grk. Zebs, Lat. Iupiter, Iovis; denoting the 24-hour day), etym. dub., ‘god’ as Skt. deva-, Lat. deus, etc.; and | but perh. (despite phonetic difficulties ‘ay’. Walde-P. 1.772 ff. Ernout-M. | with the gutturals) : Lith. dagas ‘(sum- 268 ff. Walde-H. 1.350. Here as ‘day’. | mer-) heat’, OPruss. dagis ‘summer’, Skt. a) IE *dyeu-, *diw-, etc. nidagha- ‘heat, summer’, fr. the root Lat, digs (> It. di, OF r. di, Sp. dia, | *dheg*h- in Skt. dah-, Lith. degti, etc., Rum. zi); Ir, dia, die, W. dydd, Br. | ‘burn’, and also (with init. doublets, as deiz; Skt, diva- (in dive dive ‘day by day’, | Skt. agru-, Lith. asara : Grk. daxpu otherwise divasa-); Arm. tiw. Lat. deriv. | Goth. tagr ‘tear’, etc.), Skt. ahan-, Ay. adj. diurnus ‘of the day’, late sb. diur- | azan ‘day’. Walde-P. 1.849 f. Walde- mm > Fr. jour, Prov., Cat. jorn; It. | H. 1.467. Falk-Torp 183, 176. Feist ee vs. di perh. due to lit. influence | 113. ea or Fr. REW 2632, 2700.| 5- Skt. gat Caisse ae il ae 3.71f., 105f. Bonfante, | instr. sg. ahna, etc.), Av. se . Sg. “74 59.877 ff. (with refs.). asni, etc.), see above, 4, with reis. b) With nasal suffix. Av. ayan- (nom. sg. ayara, gen. 8g. aes Lett. diena; ChSl. dint, ete., | war ete., neut r/n stem. like Skt eral Slavies Skt. di in epds.): | 2a" above), prob. : Grk. fier ‘in the Me ed (eap. in epds.); ning’, Goth. air, ON ar, etc., ‘early’, » tre-denus ‘triduum’, Goth. sin- he eee z
```


## [2026-09-05T05:49:28.507Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '445,470p' incoming/WLD/WLD_Bd1_pages.txt\necho \"--- pdf page tag ---\"\ngrep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<450' | tail -2\necho \"=== IEC line 318-324 ===\"\nsed -n '318,324p' IEC.txt\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('IEC leaf', '\\n'.join(t[:321]).count('\\f'))\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor l in (8990,23910,24505):\n    print('SYN leaf for',l,'\\n'.join(t[:l]).count('\\f'))\nEOF"
}
```


### [2026-09-05T05:49:30.432Z] TOOL RESULT

```
dem Grin, stammenden)                                  esca ..Feuerschwamm, Zunder“ (wenn nicht als
idh-s-h zur Wzf. *aidh-).
     aier-, ctien- n.                    ..Tag, Morgenfriihe'':
     ay. ai/ard, gen.                         ayqn n. ..Tag";
     gr. lok. *a(i)£Qc- in dgtarov (-arov                                                = d-tom ptc. zu cd- ..essen") ..Friih-
                                                                                              -
                                                                                                      ,


stiick" (unkontrahiertes                               Q 124, n 2); vgl.
                                                         aegtorov nocli herstellbar Horn.
Brugmann IF. 10, 88 u. Fick KZ. 22, 95: dehnstufiges *d(j)egi in ’Heoifioia
und der Ableitung geotos                                         .   morgcndlich", kontraliiert in ygi „morgens“ aber
iiber lak.          ]gyv         .       Jiingling ', Ehrlich                 KZ. 39, 570, s. unter ar- ,,fugen ')
     got. air,          an.          dr,          adv.           ..friihe    '
                                                                                     (ebenfalls       loc. *ajeri)                 dazu komparativ
got. airisa ..f'ruher",                            adv   r
                                                             .       airis— ags. dr, ahd. er, nhd.                                 eher, elw,               Super-
lativ ags.         direst ,              ahd.       erist,            nhd.       erst.
     Ygl. Stokes KZ. 38, 459: iiber                                                  ir.     anair s. vielmehr *per- „bringen, hin-
iiberbringen".
   Mit aier- lautet nach Noreen Urg. Ltl. 59 vielleicht ab idg. *jcr-, *ijjr-
in:  slav. jan ..Friihling, Sommer     (davon Ableitungen fur heurige, ein-          "



--- pdf page tag ---
=== IEC line 318-324 ===
aiuisghos (ai-uidsKos?) “shame; shameful Gk. aischos; Go. aiwiski; -aiwisks, adj.; OE æwisc; G eisch ‘ugly’. Cf. Gk. aiskhrós; Ukr. jaskravyj ‘tawdry’
aiuit- ‘age’. Cf. aiuom Lat. cf. aetas; Osc. aitatum; MIr. áes “age, time’; áetid-iach, adj. “youthfuP; Br. oad, pl. oaZu; W oed, pl.-au beside oes, pl.-oedd
aiuom ‘age, lifetime’. WP I, 6 Cyp. cf. aiwéi ‘ever’; Gk. cf. aion; ae, aién; Lat. aevum; Go. aiws; OHG éwo, ẹwa; G dial. Ewe; Du. eeuw; Fris. ieu; cf. OE &fre, adv. (fr. *aiui-pro or sim. cpd. to Lat. sem-per); ON ævi; ei, ey, ae, adv.; Norw. æva, æve
aier-, aier- “morning; early, WP I, 3 Gk. eri; Go. air; OE ær
aiesnos "of bronze, of ore’. Cf. aios Skt. cf, àayasah; Av. ayáhaeno; Lat. aenus, aeneus; Umb. ahesn- (w. “false? h); OE &ren; OHG erin (G ehern, w. ‘false’ h)
aio, see åmi, aigio (2)
-àio (1) intensive continuant extn. of verb
IEC leaf 19
SYN leaf for 8990 398
SYN leaf for 23910 1012
SYN leaf for 24505 1036
```


## [2026-09-05T05:49:42.265Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('SYN leaf for 25292:', '\\n'.join(t[:25292]).count('\\f'))\nEOF\nfor n in 399 1013 1037; do echo \"--- leaf $((n-1)) ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | head -2; done"
}
```


### [2026-09-05T05:49:44.024Z] TOOL RESULT

```
SYN leaf for 25292: 1068
--- leaf 398 ---
acja obed uzin (bhojana-) (bhojana-) otis xsafnya-
fast’, or merely ‘coffee’ or ‘tea’. ‘Din- ner’, that is, the principal meal, may be & midday or evening meal. In the for- mer case the three regular meals are ‘breakfast’, ‘dinner’, and ‘supper’, while ‘lunch’ is a slight, casual meal. In the latter case the three regular meals are ‘breakfast’, ‘lunch’, and ‘dinner’, while
--- leaf 1012 ---
 fr. hep ‘without’ and ken ‘more’.
Dan. blot, Sw. blott, NHG bloss, fr. the corresponding adjs. meaning ‘naked, bare’ (4.99). Cf. NE barely.
--- leaf 1036 ---
NIE early, beside comp. in OE @r, ME er(e) (often with positive force) : Goth. airis, OHG ér ‘before, earlier’, all perh. as ‘early in the morn- ing’: Grk. #épios ‘of the morning’, jpt ‘in the morning’, Av. ayara ‘day’, root connection dub. Walde-P. 1.3. Falk- Torp 8. Feist 24 f.
ON snemma, snimma, in epds. snemm- etym. dub. Falk-Torp 1097, 1550. Walde-P. 2.696.
```


## [2026-09-05T05:49:52.427Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN Goth air ===\"\ngrep -n -o \".\\{0,200\\}Goth\\. air[,.  ].\\{0,250\\}\" KLN_1966.txt KLN_1971.txt | head -6\necho \"=== SKT ere ===\"\ngrep -n -o \".\\{0,120\\}A\\. S\\. [ae]r,.\\{0,200\\}\" SKT.txt | head -6\necho \"=== WEB early ===\"\ngrep -n -o \".\\{0,80\\}AS\\. [ae]rlice.\\{0,200\\}\\|.\\{0,80\\}aerlice.\\{0,200\\}\" WEB_vol1.txt FSD_vol2.txt 2>/dev/null | head -6"
}
```


### [2026-09-05T05:50:01.492Z] TOOL RESULT

```
=== KLN Goth air ===
ugrep: error: error at position 99
e](?:[^\n\x80-\xbf][\x80-\xbf]*){0,250}
          exceeds complexity limits___/


=== SKT ere ===
ugrep: error: error at position 92
\n\x80-\xbf][\x80-\xbf]*){0,200}
   exceeds complexity limits___/


=== WEB early ===
```


## [2026-09-05T05:50:05.129Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Goth. air\" KLN_1966.txt KLN_1971.txt | cut -c1-60 | head -8\necho \"---\"\ngrep -n \"erst, adv\\|Ere, prep\\|ere, prep\\|early, adj\" KLN_1966.txt KLN_1971.txt | cut -c1-80 | head -8\necho \"=== SKT: Ere ===\"\ngrep -n \"Ere,\" SKT.txt | cut -c1-200 | head -5\necho \"=== SKT Erst ===\"\ngrep -n \"Erst\" SKT.txt | cut -c1-200 | head -5"
}
```


### [2026-09-05T05:50:05.242Z] TOOL RESULT

```
KLN_1971.txt:78291:erda, MHG., G. erde, Goth, airpa, and cog
KLN_1971.txt:84692:lier’, ON. dr, ‘early’, Goth, air, 
KLN_1971.txt:85035:err, mistake’, which is cogn. with Goth
---
KLN_1971.txt:85083:erst, adv., formerly (archaic). — ME. erest, erste , 
KLN_1971.txt:269610:yearly, adj. — ME. yerely , yeerly , fr. OE. 
=== SKT: Ere ===
=== SKT Erst ===
```


## [2026-09-05T05:50:08.125Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '84686,84700p' KLN_1971.txt\necho \"===== erst =====\"\nsed -n '85083,85090p' KLN_1971.txt\necho \"===== early =====\"\ngrep -n \"^early\" KLN_1971.txt | head -3"
}
```


### [2026-09-05T05:50:08.239Z] TOOL RESULT

```
other element names ending in -ium. Cp. ter- 
bium, ytterbium, yttrium, 
ere, adv., prep, and conj. — ME. er, fr. OE. xr, 
‘soon, before (in time)’, adv., prep, and conj.; 
prop, an adv. in the compar.; rel. to OS., 
OFris., OHG., MHG. er, Du. eer , G. eher, ‘ear- 
lier’, ON. dr, ‘early’, Goth, air, ‘early’, compar. 
air is, ‘earlier’, and cogn. with Avestic ayar e , 
‘day’, Gk. ^pc [for *<$c(t)epi], ‘early, in the 
morning’, Homeric 7)lpto<;, ‘early, at daybreak’, 
Gk. (jcpiaxov, ‘breakfast’. Cp. early, erst, or, 
‘before’. Cp. also the first element in Erigenia, 
Erigeron, aristology. 

Erebus, n., a place of nether darkness leading 
===== erst =====
erst, adv., formerly (archaic). — ME. erest, erste , 
fr. OE. xrest, ‘soonest, earliest* (rel. to OS. 
and OHG. erist, MHG. erst, G. erst); superl. 
of xr, ‘soon, before (in time)’. See ere and cp. 
early. Compound: erst-while, adv. 
erubescence, n., process of becoming red. — L. 
erubescentia , ‘a blushing’, fr. erubescSns , gen. 
ends. See next word and -ce. 
===== early =====
36847:early borrowing, its doublet captive is a later 
78252:early, adv. — ME. erliche, erli, fr. OE. xrltce, 
79865:early G. elend, elen (= G. Elentier), fr. Lith.
```


## [2026-09-05T05:50:35.836Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg74.png data/verification/sources/refs/ocr/BOOK/74.png\nls -la data/verification/sources/refs/ocr/BOOK/74.png"
}
```


### [2026-09-05T05:50:35.903Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 56073 Sep  5 01:50 data/verification/sources/refs/ocr/BOOK/74.png
```


## [2026-09-05T05:50:41.865Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey-' --note 'page 74, root Ayer/Aier/Aien: modern PIE reconstruction *h2ey- (3) day/morning, heteroclitic *h2oy-r ~ *h2ey-ns, Avestan aiiare' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C%D8%B1%D9%88%D8%B2' --note 'page 74, Persian node: pariruz/parir etymology, MP parer, Proto-Iranian *para-ayarah' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/ere' --note 'page 74, English node: ere < OE aer < PGmc *airiz < PIE *ayer- day, morning' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/early' --note 'page 74, English node: early < OE aerlice (aer + -lice)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/erst' --note 'page 74, English node: erst < OE aerest superlative of aer' 2>&1 | tail -3"
}
```


### [2026-09-05T05:50:45.059Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c393974a7d06cc8a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3ee559bca0a3d68.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/acae966b3d7d4512.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6dcbdbd49f9c6057.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e3599021a56f04ea.txt
```


## [2026-09-05T05:50:52.022Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i \"parāyarah\\|parayarah\\|ayarah\\|parēr\\|h₂eyer\\|Middle Persian\" f3ee559bca0a3d68.txt | head -20"
}
```


### [2026-09-05T05:50:52.089Z] TOOL RESULT

```
158: Middle Persian 𐭩𐭥𐭬 ( yʿm )
```


## [2026-09-05T05:50:55.796Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C",
 "prompt": "Under the Persian entry for پری, is there an etymology section for the adverb meaning \"the day before yesterday\" (parê/parî)? Quote the etymology: Middle Persian form, Proto-Iranian reconstruction, PIE root, and cognates."
}
```


### [2026-09-05T05:51:02.184Z] TOOL RESULT

```
# Etymology of Persian پری (parê/parî) - "the day before yesterday"

Yes, there is an etymology section (Etymology 3) for this sense. Here are the key components:

**Middle Persian form:** "𐬞𐬭𐬌𐬭 (prir /⁠parīr⁠/)" and related variants

**Proto-Iranian reconstruction:** "[\*parāyarah](/w/index.php?title=Reconstruction:Proto-Iranian/par%C4%81yarah&action=edit&redlink=1)" composed of "[\*para-](/w/index.php?title=Reconstruction:Proto-Iranian/para-&action=edit&redlink=1)" plus "[\*ayarah](/w/index.php?title=Reconstruction:Proto-Iranian/ayarah&action=edit&redlink=1) ("day")"

**PIE root:** "[\*h₂eyer-](/w/index.php?title=Reconstruction:Proto-Indo-European/h%E2%82%82eyer-&action=edit&redlink=1) ("day, morning")"

**Cognates listed include:** Mazanderani, Bakhtiari, Bashkardi, Kermanic, Baluchi, Northern Kurdish, and Central Kurdish forms, plus Avestan comparisons.
```


## [2026-09-05T05:51:06.337Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C' --note 'page 74, Persian node: Etymology 3 of پری = پریر, from MP parir, Proto-Iranian *para-ayarah, PIE *h2eyer- day/morning' 2>&1 | tail -2\ngrep -n -i \"parāyarah\\|ayarah\\|parīr\\|h₂eyer\" data/verification/sources/web/*.txt | head -10"
}
```


### [2026-09-05T05:51:09.112Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3ab7c5d4990c9e20.txt
data/verification/sources/web/3ab7c5d4990c9e20.txt:470: From پریر ( parir, parêr , “ day before yesterday ” ) , from Middle Persian 𐬞𐬭𐬌𐬭 ( prir /⁠parīr⁠/ ) , [Book Pahlavi needed] ( plʾyyl ) , [Book Pahlavi needed] ( plʾyyʾl /⁠parīr, parēr⁠/ , “ the day before yesterday ” ) , from Proto-Iranian *parāyarah , [ 1 ] [ 2 ] from *para- +‎ *ayarah ( “ day ” ) (compare Avestan 𐬀𐬫𐬀𐬭𐬇 ( ayarə̄ , “ day ” ) ), from Proto-Indo-European *h₂eyer- ( “ day, morning ” ) . Cognate with Mazanderani پره ( pare ) , [ 3 ] Bakhtiari پری ( parey ) , Bashkardi پریر ( parir ) , Kermanic پره ( pare ) , Baluchi [script needed] ( parērī ) , [script needed] ( pairērī ) , Northern Kurdish pêr , Central Kurdish پێرێ ( pêrê ) . Also compare Shirazi پریگرو ( parigru ) , پریگروز ( parigruz ) , Southern Luri پریگ ( parig ) .
data/verification/sources/web/24cd7948c66bfb96.txt:5378: suffixed form *par-yo‑ . -para , parity 2 , -parous , parturient , postpartum , repertory , viper , from Latin parere , parīre , to get, beget, give birth;
data/verification/sources/web/3735d75498a331a4.txt:5378: suffixed form *par-yo‑ . -para , parity 2 , -parous , parturient , postpartum , repertory , viper , from Latin parere , parīre , to get, beget, give birth;
```


## [2026-09-05T05:51:14.498Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-05T05:51:14.557Z] TOOL RESULT

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


## [2026-09-05T05:57:30.434Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey-\"\nW_PARI = \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C\"\nW_PRZ  = \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C%D8%B1%D9%88%D8%B2\"\nE_ERE  = \"https://www.etymonline.com/word/ere\"\nE_EAR  = \"https://www.etymonline.com/word/early\"\nE_ERST = \"https://www.etymonline.com/word/erst\"\n\ndoc = {\n \"pdf_page\": 74,\n \"book_page\": 44,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 2,\n   \"root\": \"Ayer, Aier, Aien\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂ey- (3) 'day, morning', heteroclitic noun *h₂óy-r̥ ~ *h₂éy-n-s 'day' (= Pokorny ā̆ier-, ā̆ien-, IEW 12; Watkins ayer-)\",\n   \"note\": (\"Pokorny IEW p. 12 has the entry verbatim: \\\"ā̆ier-, ā̆ien- n. 'Tag, Morgen'. Av. ayarə, Gen. ayąn n. 'Tag'\\\", \"\n            \"and Watkins in the AHD appendix has \\\"ayer-. Day, morning. ... [Pok. ajer- 12.]\\\". Nourai's three headword variants are simply the AHD \"\n            \"spelling (ayer-) plus Pokorny's two stem forms (aier-/aien-); the r/n heteroclisis of the Avestan paradigm (nom. ayarə : gen. ayąn) \"\n            \"is exactly what produces the -r and -n variants. Language label 'Indo-European' and the gloss 'day, morning, early in the day' are both \"\n            \"correct (the third part of the gloss reflects the locative *h₂éy-eri 'in the morning' behind Gk. ἦρι and Goth. air). \"\n            \"Modern laryngealist notation is *h₂ey-/*h₂eyer-; Nourai's pre-laryngeal shape is the 1959 Pokorny shape and is not an error. \"\n            \"The Naser-Khosrow couplet printed in the Persian box (پریر قبلهٔ احرار زابلستان بود...) uses پریر in its ordinary adverbial sense \"\n            \"and is faithfully extracted. One substantive problem lies inside the chart, not at the root: see node #3 (پیرار).\"),\n   \"note_fa\": (\"ریشهٔ هندواروپایی آغازینی که نورایی آن را Ayer, Aier, Aien آورده، همان ā̆ier-/ā̆ien- پوکورنی (ص ۱۲) به معنای «روز، بامداد» است؛ \"\n               \"در ریشه‌شناسی امروزی آن را *h₂ey- و نامی دوگانه‌ستاک (heteroclitic) *h₂óy-r̥ ~ *h₂éy-n̥s بازسازی می‌کنند؛ همین گردش r/n در صرف اوستایی \"\n               \"(فاعلی ayarə، اضافی ayąn) دو صورت Aier و Aien را توضیح می‌دهد. برچسب زبانی «هندواروپایی» و معنای جعبهٔ ریشه درست است و هر دو \"\n               \"مأخذی که خود نورایی آورده (پوکورنی ۱۲؛ واتکینز در پیوست فرهنگ میراث آمریکایی، ص ۱۵۰۷) دقیقاً همین را می‌گویند. \"\n               \"ادعای نورایی دربارهٔ خود ریشه درست است؛ اشکال در یکی از شاخه‌هاست (نگاه کنید به گرهٔ ۳، «پیرار»).\"),\n   \"sources\": [W_PIE, W_PARI, W_PRZ],\n   \"ref_check\": [\n    {\"ref\": \"POK:12\", \"status\": \"supports\",\n     \"note\": \"Pokorny IEW p. 12 (POK_01.txt leaf 20, page marker '12' visible on the leaf): \\\"ā̆ier-, ā̆ien- n. ,Tag, Morgen'. Av. ayarə, Gen. ayąn n. ,Tag'.\\\" and on p. 13 \\\"Got. air, aisl. ár, Adv. ,frühe' ... Kompar. got. airiza ,früher' ... Superl. ags. ǣrest ... nhd. erst. WP. I 3\\\". Exactly the chart's root, gloss and both branches.\"},\n    {\"ref\": \"AHD:1507\", \"status\": \"supports\",\n     \"note\": \"Watkins, AHD IE-roots appendix (local AHD_watkins1985.txt line 317): \\\"ayer-. Day, morning. 1. Germanic *airiz in: a. Old English ǣr, before: EARLY, ERE; b. Old Norse ár, before: OR2. 2. Germanic (superlative) *airistaz in Old English ǣrest, earliest: ERST. [Pok. ajer- 12.]\\\" — the whole Germanic/English branch of the chart, verbatim; p. 1507 is the right page of the 1975 New College appendix (a-roots, pp. 1505-1508).\"},\n    {\"ref\": \"OEW:3\", \"status\": \"not_checked\",\n     \"note\": \"Shipley, The Origins of English Words (1984) is lending-only on archive.org (djvu.txt returns 403) and there is no local copy; refs_online.json marks OEW local_file: null.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 3 (WLD_Bd1_pages.txt line 447)\", \"stance\": \"supports\",\n     \"note\": \"\\\"aier-, aien- n. ,Tag, Morgenfrühe': ay. ayarə, gen. ayąn n. ,Tag'; gr. lok. *a(i)eri- in ἄριστον ... got. air, an. ár, adv. ,frühe' ... Superlativ ags. ǣrest, ahd. erist, nhd. erst.\\\" This is the WP. I 3 that Pokorny p. 12 cites, i.e. the primary source behind both.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, col./p. 8 (IEC.txt leaf 19)\", \"stance\": \"supports\",\n     \"note\": \"\\\"aier-, aier- 'morning; early'. WP I, 3. Gk. eri; Go. air; OE ǣr\\\" — Mann keeps the same root, with the 'morning/early' side foregrounded.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 14.41 'DAY' and 14.15 'EARLY'\", \"stance\": \"partial\",\n     \"note\": \"14.41: \\\"Av. ayan- (nom. sg. ayarə, gen. sg. ayąn ...), neut. r/n stem ..., prob. : Grk. ἦρι 'in the morning', Goth. air, ON ár, etc., 'early'\\\". 14.15: \\\"Goth. air, ON ár ... OE ǣr-līce, ME erliche, erli, NE early ... : Grk. ἠέριος ..., Av. ayarə 'day', root connection dub. Walde-P. 1.3.\\\" Buck accepts the equation but flags the Iranian-Germanic link as not certain — a caveat Nourai does not record.\"},\n    {\"src\": \"BRT\", \"where\": \"col. 157 s.v. ayan-, ayar-\", \"stance\": \"supports\",\n     \"note\": \"\\\"ayan-, j-, g. ayar- n. 'Tag'\\\" with the note \\\"np. vgl. parēr 'vorgestern', GIrPh. I b. 34\\\" — Bartholomae himself draws the Avestan 'day' word to New Persian parēr, i.e. the chart's Iranian branch.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"ayare; prô-ayare\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": (\"(a) Av. ayarə 'day' is real and correctly placed: it is the nom.-acc. sg. of the neuter r/n-heteroclite ayar-/ayan- \"\n                    \"(gen. ayąn), Bartholomae AiW col. 157, and it is the direct Iranian continuant of PIE *h₂óy-r̥. \"\n                    \"(b) 'prô-ayare' is not an attested Avestan word and, as printed, not a possible one — Avestan has no prō-. \"\n                    \"The source Nourai follows here (AEF:376 = Khaleqi Motlaq's Persian translation of Horn) renders Horn, Grundriss p. 69, \"\n                    \"which reconstructs, with an asterisk, \\\"aw. *parō.ayare; phlv. parēr\\\": parō 'before, in front of' (Av. parō, \"\n                    \"OP paruva- 'former') + ayarə 'day'. The printed page of Nourai (PDF p. 74, book p. 44) really does show 'prô-ayare' with \"\n                    \"the a of parō- dropped and Horn's asterisk lost, so the fault is the book's, not the extraction's. \"\n                    \"(c) The gloss is also wrong by one day: Horn glosses the compound 'Vorgestern' = the day before yesterday, \"\n                    \"and Nourai's own Persian parenthesis پریروز says the same.\"),\n     \"derivation_fa\": (\"الف) اوستایی ayarə «روز» واژه‌ای است گواهی‌شده و در جای درست نشسته است؛ صورت فاعلی–مفعولی مفرد ستاک دوگانهٔ r/n یعنی ayar-/ayan- \"\n                       \"(اضافی ayąn) است و بارتولومه در ستون ۱۵۷ فرهنگ ایرانی باستان همین معنا را می‌دهد و خود در حاشیه به «پریر» فارسی اشاره می‌کند. \"\n                       \"ب) اما صورت دوم، prô-ayare، واژهٔ اوستایی گواهی‌شده نیست و به همین شکل نمی‌تواند اوستایی باشد؛ مأخذی که نورایی پیروی کرده (ترجمهٔ \"\n                       \"فارسی گروندریس هرن به قلم خالقی مطلق، AEF:376) صورت بازسازیشدهٔ *parō.ayare را با ستاره می‌آورد: parō «پیش، جلو» + ayarə «روز». \"\n                       \"در صفحهٔ چاپی کتاب (ص ۴۴) هم دقیقاً prô-ayare چاپ شده؛ پس خطای چاپی کتاب است، نه خطای خوانش اسکن. \"\n                       \"ج) معنا نیز یک روز جابه‌جا شده است: هرن این ترکیب را Vorgestern یعنی «پریروز» معنا کرده، چنان‌که خود نورایی هم در کمانک فارسی «پریروز» آورده، نه «دیروز».\"),\n     \"error_in\": \"book\",\n     \"book_prints\": \"prô-ayare : yesterday\",\n     \"correct_form\": \"*parō.ayare 'the day before yesterday' (Horn's starred reconstruction)\",\n     \"sources\": [W_PARI, W_PIE],\n     \"ref_check\": [\n      {\"ref\": \"POK:12\", \"status\": \"supports\",\n       \"note\": \"Pokorny p. 12: \\\"Av. ayarə, Gen. ayąn n. ,Tag'\\\" — covers the first word of the node; Pokorny says nothing about any parō- compound.\"},\n      {\"ref\": \"AEF:376\", \"status\": \"not_checked\",\n       \"note\": \"Khaleqi Motlaq, Asās-e Eshteqāq-e Fārsi vol. I — refs_online.json: not online (kind 'catalog'), no local copy. It is however the Persian translation of Horn's Grundriss, and Horn's own entry (p. 69, 'perer Vorgestern ... aw. *parō.ayare; phlv. parēr') was checked directly instead: it supports the derivation but with a starred Avestan form and the gloss 'Vorgestern'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 157 s.v. ayan-, ayar-\", \"stance\": \"supports\",\n       \"note\": \"\\\"ayan-, j-, g. ayar- n. 'Tag'\\\"; the etymological note adds \\\"np. vgl. parēr 'vorgestern'\\\". No entry *parō.ayara- exists in the AiW, confirming that the compound is a reconstruction, not an attested Avestan word.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss p. 69, entry 'perer'\", \"stance\": \"partial\",\n       \"note\": \"\\\"perer Vorgestern, pere|rōz, pere|šeb. ... aw. *parō.ayare; phlv. parēr.\\\" Supports the compound but only as a starred reconstruction and glosses it 'the day before yesterday', not 'yesterday'; and the first element is parō-, not prō-.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 167 (ch. 10, Kontraktion)\", \"stance\": \"supports\",\n       \"note\": \"\\\"parēr Vorgestern - ap. paruva- 'früher' + *ayar-, zd. paourva- 'früher' + ayare 'Tag'?\\\" — Hübschmann gives the same two elements (with OP paruva-/Av. paourva- as the first member) and marks the analysis with a query.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 14.41 'DAY'\", \"stance\": \"supports\",\n       \"note\": \"\\\"Av. ayan- (nom. sg. ayarə, gen. sg. ayąn), neut. r/n stem\\\" — independent confirmation of the Avestan word and its paradigm.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"parěr\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Middle Persian parēr, Book Pahlavi plʾyyl / plʾyyʾl, 'the day before yesterday'. It continues Old Iranian \"\n                    \"*parā-ayarah (*para-/paruva- 'before' + *ayarah 'day'): the sequence -aya- contracted to -ē-, a change Hübschmann \"\n                    \"(Persische Studien p. 167) dates before the 5th c. CE and illustrates with this very word (alongside mazdēsn < mazdayasn, \"\n                    \"ēr 'below' < *ayar). Horn p. 69 likewise gives 'phlv. parēr'. Nourai's 'parěr' is his usual notation for the majhūl \"\n                    \"ē and is not a misreading. Two caveats: the gloss should be 'the day before yesterday' (MP 'yesterday' is dīg), and MacKenzie's \"\n                    \"Concise Pahlavi Dictionary happens not to carry the word at all, so the Pahlavi form rests on Horn/Hübschmann and the Book \"\n                    \"Pahlavi spellings cited on Wiktionary rather than on MacKenzie.\"),\n     \"derivation_fa\": (\"فارسی میانه parēr (در پهلوی کتابی plʾyyl / plʾyyʾl) به معنای «پریروز»، دنبالهٔ ایرانی باستان *parā-ayarah است: \"\n                       \"*para-/paruva- «پیش» + *ayarah «روز». در این واژه خوشهٔ -aya- به ـــē منقلب شده؛ هوبشمان در «مطالعات فارسی» (ص ۱۶۷) همین واژه را نمونهٔ \"\n                       \"این دگرگونی آورده و زمان آن را پیش از سدهٔ پنجم میلادی دانسته است؛ هرن نیز (ص ۶۹) «phlv. parēr» می‌نویسد. «parěr» در نوشتهٔ نورایی همان ـē مجهول \"\n                       \"است و خطای خوانش نیست. دو نکته: معنای درست «پریروز» است نه «دیروز» («دیروز» در فارسی میانه dīg است)؛ و مکنزی این واژه را در فرهنگ \"\n                       \"کوچک پهلوی نیاورده است. در مجموع، ادعای نورایی با اصلاح معنا پذیرفتنی است.\"),\n     \"sources\": [W_PARI],\n     \"ref_check\": [\n      {\"ref\": \"AEF:376\", \"status\": \"not_checked\",\n       \"note\": \"Not online and no local copy (refs_online.json, kind 'catalog'). Checked its German original instead: Horn, Grundriss p. 69 'phlv. parēr' — supports the Pahlavi form and its position under the Avestan compound, but glosses it 'Vorgestern'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 167\", \"stance\": \"supports\",\n       \"note\": \"\\\"parēr Vorgestern - ap. paruva- 'früher' + *ayar-, zd. paourva- 'früher' + ayare 'Tag'? Diese Kontraktion ist vor dem 5. Jhd. p. Chr. ... vollzogen\\\" — gives both the etymology and the sound change that produces ē.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss p. 69, entry 'perer'\", \"stance\": \"supports\",\n       \"note\": \"\\\"aw. *parō.ayare; phlv. parēr\\\", with the dialect comparanda \\\"kurd. pēr; bal. parērī, pairērī\\\" — the same Middle Persian form.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, p-section (PHD.txt leaf with parig ... parwardan)\", \"stance\": \"silent\",\n       \"note\": \"grep 'par[eēě]r' and 'before yesterday' over PHD.txt / PHD_mackenzie.txt returns nothing; the printed run goes paristag, paristar, paristīdan, parnīyān, parr, parrag ... with no parēr. MacKenzie simply omits the word.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n       \"note\": \"grep 'parēr' / 'yesterday' over NYB_vol2_glossary.txt returns nothing.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 5 (addenda), pdf p. 71, note on آسور\", \"stance\": \"partial\",\n       \"note\": \"Mo'in's addendum reads (rough OCR) \\\"... پارسی «پری روز» ... پهلوی ... پریر (یونکر ص ۹۳)\\\" — Mo'in cites Junker for a Pahlavi پریر beside Persian پریروز, which corroborates the Pahlavi form though the OCR is too damaged to quote the full sentence.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"parîr; pîrâr\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"Two words with two different verdicts. (a) پریر parīr is confirmed: NP parīr/parēr < MP parēr < Old Iranian \"\n                    \"*parā-ayarah (*para- + *ayarah 'day'), i.e. the chart's chain Av. day-word > Pahlavi > Persian is right; the New Persian \"\n                    \"extended forms پریروز parīrūz and پریشب parīšab simply add rūz 'day' / šab 'night' to the old adverb, and the cognates \"\n                    \"(N. Kurdish pêr, Baluchi parērī, Bakhtiari parey) confirm an inherited, not borrowed, word. Its meaning, however, is \"\n                    \"'the day before yesterday', not 'yesterday' — as Nourai's own parenthesis پریروز says. \"\n                    \"(b) پیرار pīrār 'the year before last' does NOT belong under this root. The reference Nourai cites for it (AEF:376 = the \"\n                    \"Persian Horn) has, at Horn's own entry, \\\"pīrār, pīrār|sāl 'das vorvergangene Jahr'. aw. *para.yār- (+ sāl)\\\" (p. 78): \"\n                    \"the shared element is only par-/pī- < *para- 'before'; the second member is *yār- 'year' (Av. yārə, PIE *yóh₁r̥, \"\n                    \"Pokorny 296 — the root of Germanic *jēram, English YEAR), not ayar- 'day'. pīrār is thus the exact 'year' counterpart of \"\n                    \"parīr, and modern scholarship places it under a different PIE root.\"),\n     \"derivation_fa\": (\"دو واژه با دو حکم جداگانه. الف) «پریر» درست است: فارسی نو parīr از فارسی میانهٔ parēr و آن از ایرانی باستان *parā-ayarah \"\n                       \"(*para- «پیش» + *ayarah «روز»)؛ صورت‌های گستردهٔ «پریروز» و «پریشب» فقط افزودن «روز» و «شب» به همین قید کهن‌اند، و هم‌ریشه‌های کردی (pêr)، \"\n                       \"بلوچی (parērī) و بختیاری (parey) نشان می‌دهد که واژه میراثی است نه وام‌واژه. تنها معنا باید «دو روز پیش» باشد نه «دیروز»، چنان‌که خود نورایی در \"\n                       \"کمانک «پریروز» آورده است. ب) اما «پیرار» به این ریشه ربطی ندارد. همان مأخذی که نورایی برای آن آورده (AEF، ترجمهٔ فارسی هرن) در اصل آلمانی \"\n                       \"خود (ص ۷۸) می‌نویسد: «pīrār, pīrārsāl ‘سال پیش از پارسال’؛ اوستایی *para.yār-»؛ یعنی جزء دوم yār- «سال» است (اوستایی yārə، \"\n                       \"هندواروپایی *yóh₁r̥، پوکورنی ۲۹۶، همان ریشهٔ year انگلیسی)، نه ayar- «روز»؛ تنها جزء مشترک، پیشوند *para- «پیش» است. معین نیز پیرار را \"\n                       \"«سال پیش از پارسال» معنا کرده است. پس پژوهش امروزی جای دادن «پیرار» را زیر ریشهٔ «روز» رد می‌کند و آن را به ریشهٔ «سال» می‌برد.\"),\n     \"sources\": [W_PARI, W_PRZ],\n     \"ref_check\": [\n      {\"ref\": \"AEF:376\", \"status\": \"partial\",\n       \"note\": \"Not accessible directly (no online copy); its German original was checked. Horn p. 69 supports پریر exactly as drawn, but Horn p. 78 no. 351 gives پیرار a DIFFERENT etymology (\\\"aw. *para.yār- (+ sāl)\\\"), so the same cited reference contradicts the second word of the node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Grundriss p. 69 ('perer') and p. 78 no. 351 ('pīrār')\", \"stance\": \"contradicts\",\n       \"note\": \"p. 69: \\\"perer Vorgestern, pere|rōz, pere|šeb ... aw. *parō.ayare; phlv. parēr\\\" (supports پریر). p. 78: \\\"351. pīrār, pīrār|sāl 'das vor vergangene Jahr'. aw. *para.yār- (+ sāl).\\\" — yār- 'year', not ayar- 'day'; this is the contradiction.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. پیرار (MON_part1.txt line 34402)\", \"stance\": \"partial\",\n       \"note\": \"\\\"پیرار: (ق.) سال پیش از پارسال؛ دو سال پیش از سال حاضر، پیرارسال.\\\" Mo'in confirms the gloss 'two years ago' but gives no etymological tag; his definition ('year before last') is itself the reason the word belongs with 'year', not 'day'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 167\", \"stance\": \"supports\",\n       \"note\": \"\\\"parēr Vorgestern - ap. paruva- 'früher' + *ayar-\\\" — supports the پریر half of the node; Hübschmann does not bring پیرار into this family.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' — grep of BQT_v1/v2/v3/v4 for پریر and پیرار\", \"stance\": \"silent\",\n       \"note\": \"No usable headword hit for either word in the OCR of vols 1-4 (only a stray پریر inside a v1 gloss line and the vol. 5 addendum noted on node #2); Mo'in's etymological footnote for these adverbs could not be located in the available scans.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'پریر' and 'پیرار' over ARY_pages.txt returns nothing; the Latin index hit 'ayer 285' leads to the entry for دو 'two', i.e. an OCR artefact.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Germanic\",\n     \"words\": \"airiz\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Proto-Germanic *airiz is the comparative adverb 'earlier' formed to *air 'early' (Gothic air 'early', comparative airis \"\n                    \"'earlier'; Old Norse ár). *air itself goes back to the PIE locative *h₂éy-eri 'in the morning' of the 'day' noun — the same \"\n                    \"case-form that gives Greek ἦρι 'at dawn', ἠέριος 'of the morning' and ἄριστον 'breakfast' (< *h₂yeri-h₁d-tom \"\n                    \"'early-eating'). Pokorny sets it out on p. 12-13 and Watkins repeats the reconstruction *airiz. The semantic move is \"\n                    \"'in the morning' > 'early' > (comparative) 'before, earlier'. The one loose point is the gloss: *airiz is strictly 'earlier'; \"\n                    \"'early' is the positive *air.\"),\n     \"derivation_fa\": (\"ژرمنی آغازین *airiz صورت تفضیلی قید *air «زود» است — گوتی air «زود» با تفضیلی airis «زودتر»، نورس باستان ár. خود *air از \"\n                       \"حالت دری (locative) نام «روز» یعنی *h₂éy-eri «بامدادان» می‌آید؛ همین صورت در یونانی ἦρι «سپیده‌دم» و ἠέριος و ἄριστον «چاشت» دیده می‌شود. \"\n                       \"پوکورنی (ص ۱۲–۱۳) و واتکینز (ص ۱۵۰۷) هر دو همین بازسازی *airiz را می‌آورند؛ تحول معنایی از «در بامداد» به «زود» و سپس «پیش‌تر» است. \"\n                       \"تنها نکتهٔ جزئی آن که *airiz به‌دقت «زودتر» است و معنای «زود» از آنِ صورت سادهٔ *air است. باک در فرهنگ مترادف‌ها (بند ۱۴٫۱۵) این پیوند را \"\n                       \"می‌پذیرد ولی می‌افزاید «پیوند ریشه‌ای مشکوک است». ادعای نورایی درست است.\"),\n     \"sources\": [E_ERE, W_PIE],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1507\", \"status\": \"supports\",\n       \"note\": \"Watkins: \\\"ayer-. Day, morning. 1. Germanic *airiz in: a. Old English ǣr, before ... 2. Germanic (superlative) *airistaz in Old English ǣrest, earliest\\\" — the reconstructed form *airiz is Watkins's own.\"},\n      {\"ref\": \"OEW:3\", \"status\": \"not_checked\",\n       \"note\": \"Shipley 1984 lending-only on archive.org; no local copy.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW pp. 12-13\", \"stance\": \"supports\",\n       \"note\": \"\\\"Got. air, aisl. ár, Adv. ,frühe' (ebenfalls Lok. *aieri), dazu Kompar. got. airiza ,früher', Adv. airis = ags. ǣr, ahd. ēr, nhd. eher, ehe; Superl. ags. ǣrest, ahd. ērist, nhd. erst.\\\" — identifies *air as the old locative and airiza/airis as its comparative.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. 'ere'\", \"stance\": \"supports\",\n       \"note\": \"\\\"ME. er, fr. OE. ǣr ... rel. to OS., OFris., OHG., MHG. ēr, Du. eer, G. eher, 'earlier', ON. ár, 'early', Goth. air, 'early', compar. airis, 'earlier', and cogn. with Avestic ayarə, 'day', Gk. ἦρι ... 'early, in the morning'\\\" — Klein makes the Avestan-Germanic equation explicitly.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 14.15 'EARLY'\", \"stance\": \"partial\",\n       \"note\": \"\\\"Goth. air, ON ár ... : Goth. airis, OHG ēr 'before, earlier', all perh. as 'early in the morning' : Grk. ἠέριος ..., Av. ayarə 'day', root connection dub.\\\" — same reconstruction, with an explicit note of doubt about the root connection.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p. 8\", \"stance\": \"supports\",\n       \"note\": \"\\\"aier- 'morning; early'. WP I, 3. Gk. eri; Go. air; OE ǣr\\\".\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"early, ere, erst\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"All three are the English reflexes of Proto-Germanic *airiz through Old English ǣr. ERE: OE ǣr 'soon, before (in time)' \"\n                    \"(adv./prep./conj., formally a comparative) > ME er > ere, first in that spelling c. 1200. EARLY: OE ǣrlīce = ǣr + the \"\n                    \"adverbial suffix -līce > ME erliche, erli > early, the adverb only later becoming an adjective. ERST: OE ǣrest 'soonest, \"\n                    \"earliest', the superlative of ǣr (cf. OHG ērist, G. erst) > ME erest, erste > erst, now archaic except in erstwhile \"\n                    \"(1560s). So the arrow Germanic *airiz > English is right for ere, while early and erst are formed on ǣr inside English \"\n                    \"itself — which is exactly how Watkins and Klein present them.\"),\n     \"derivation_fa\": (\"هر سه واژهٔ انگلیسی از همین خانواده‌اند و همه از راه انگلیسی باستان ǣr از ژرمنی آغازین *airiz می‌آیند: ere از ǣr \"\n                       \"«زود، پیش از» از راه انگلیسی میانهٔ er (حدود ۱۲۰۰ میلادی)؛ early از ǣrlīce، یعنی ǣr + پسوند قیدساز ‑līce، از راه erliche/erli؛ \"\n                       \"و erst از ǣrest، صورت عالی ǣr (مقایسه کنید با آلمانی باستان عالی ērist و آلمانی امروز erst). پس پیکان نمودار از *airiz به انگلیسی درست است، \"\n                       \"با این توضیح که early و erst در درون خود انگلیسی از ǣr ساخته شده‌اند. کلاین، اتیمآنلاین و واتکینز همین را می‌گویند؛ ادعای نورایی درست است.\"),\n     \"sources\": [E_ERE, E_EAR, E_ERST],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. ayer-: \\\"Germanic *airiz in: a. Old English ǣr, before: EARLY, ERE ... Germanic (superlative) *airistaz in Old English ǣrest, earliest: ERST\\\" — all three English words are listed under this root, exactly as in the chart. The AHD index (p. 89-90 of the 1985 ed.) also lists 'EARLY ayer-', 'ERE ayer-', 'ERST ayer-'.\"},\n      {\"ref\": \"OEW\", \"status\": \"not_checked\",\n       \"note\": \"Shipley 1984 not accessible (lending-only, no local copy).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1971 s.vv. 'ere', 'early', 'erst'\", \"stance\": \"supports\",\n       \"note\": \"ere: \\\"ME. er, fr. OE. ǣr ... prop. an adv. in the compar. ... Cp. early, erst, or 'before'.\\\" early: \\\"early, adv. — ME. erliche, erli, fr. OE. ǣrlīce\\\". erst: \\\"erst, adv., formerly (archaic). — ME. erest, erste, fr. OE. ǣrest, 'soonest, earliest' (rel. to OS. and OHG. erist, MHG. erst, G. erst); superl. of ǣr.\\\"\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 14.15 'EARLY' and 13.32 'FIRST'\", \"stance\": \"supports\",\n       \"note\": \"14.15: \\\"OE ǣr-līce, ME erliche, erli, NE early, beside comp. in OE ǣr, ME er(e)\\\". 13.32: \\\"OE ǣrest (NE erst 'in former time'), OHG ēristo, MHG ēr(e)st, NHG erst; superl. of Goth. air 'early' ... hence orig. 'first' in time.\\\"\"},\n      {\"src\": \"POK\", \"where\": \"IEW p. 13\", \"stance\": \"supports\",\n       \"note\": \"\\\"Adv. airis = ags. ǣr, ahd. ēr, nhd. eher, ehe; Superl. ags. ǣrest, ahd. ērist, nhd. erst\\\" — the Old English forms behind ere and erst.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\",\n       \"note\": \"The OCR of SKT.txt is too degraded in the E-section to retrieve the 'Ere'/'Erst' entries (greps for 'Ere,', 'Erst' return nothing usable); no statement could be extracted.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('data/verification/page-74.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 -m json.tool data/verification/page-74.json > /dev/null && echo \"valid JSON\"\npython3 tools/verify_check.py 74"
}
```


### [2026-09-05T05:57:32.446Z] TOOL RESULT

```
written
valid JSON
nodes verified: 5/5
node verdicts: {'transcription_suspect': 1, 'plausible': 1, 'disputed': 1, 'confirmed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 3, 'not_checked': 4, 'partial': 1}
books consulted: {'supports': 12, 'partial': 4, 'silent': 5, 'contradicts': 1} | by book: {'HRN': 3, 'HUB': 3, 'SYN': 3, 'BQT': 2, 'POK': 2, 'KLN': 2, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'MON': 1, 'ARY': 1, 'IEC': 1, 'SKT': 1}
```


## [2026-09-05T05:57:52.019Z] AGENT

Done — page 74 verified.

**Page 74 (book p. 44)** — 5 redirect entries skipped; 1 real chart (root **Ayer, Aier, Aien**, IE "day, morning"), 5 nodes.

- Root verdict: **confirmed** (Pokorny IEW p. 12 `ā̆ier-, ā̆ien- n. 'Tag, Morgen'`; Watkins/AHD p. 1507 `ayer-. Day, morning. [Pok. ajer- 12]` — both of Nourai's citations check out verbatim).
- Node verdicts: confirmed 2, plausible 1, disputed 1, transcription_suspect 1.
- Ref checks: supports 3, partial 1, not_checked 4 (AEF and OEW have no accessible copy; for AEF I checked Horn's German original instead, since AEF is its Persian translation).
- Books consulted: POK, WLD, AHD, IEC, SYN, BRT, HRN, HUB, PHD, NYB, MON, BQT, ARY, KLN, SKT.

Flagged items:

- **disputed — #3 Persian `pîrâr` «پیرار»**: does not belong under the "day" root. Nourai's own cited reference contradicts him: Horn, *Grundriss* p. 78 no. 351 gives `pīrār, pīrārsāl` < Av. `*para.yār-` — second element `yār-` "year" (PIE *yóh₁r̥, Pok. 296), not `ayar-` "day". Only the prefix *para- "before" is shared with `parīr`. (`parîr` itself is confirmed: MP parēr < *parā-ayarah.)
- **transcription_suspect — #1 Avestan `prô-ayare`**: not an attested (or possible) Avestan form. `error_in: "book"` — the printed page really does show `prô-ayare`; Horn p. 69 reconstructs, with an asterisk, `*parō.ayare` (parō "before" + ayarə "day"). Nourai dropped the *a* of parō- and the asterisk. Page PNG copied to `data/verification/sources/refs/ocr/BOOK/74.png`.

Gloss problems (book's, not the extraction's), noted in the derivations: `prô-ayare`, `parěr` and `parîr` are all glossed "yesterday" but mean **"the day before yesterday"** — Horn glosses *Vorgestern*, and Nourai's own Persian parenthesis «پریروز» says the same. Also #4 `airiz` is strictly the comparative "earlier"; "early" is the positive *air.

**No extraction errors** — the JSON matches the printed page exactly (forms, Persian script, Nāser-Khosrow couplet).

Files: `/home/sfmqrb/git/rishe/data/verification/page-74.json` (valid JSON, `verify_check.py 74` → 0 PROBLEM lines); 6 web sources archived via `fetch_source.py`.
