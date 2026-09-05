# Verification process log — verify-page-159


## [2026-09-05T20:29:49.166Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 159 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-159.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-159.json. Write /home/sfmqrb/git/rishe/data/verification/page-159.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 159` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:29:50.381Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:29:51.140Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:29:51.154Z] TOOL RESULT

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


## [2026-09-05T20:29:51.689Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-159.txt"
}
```


### [2026-09-05T20:29:51.701Z] TOOL RESULT

```
1	=== PDF page 159 (book page 129) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Erek : flea, mite  (refs POK:335)
4	#1 (parent #0) [Sanskrit] refs=POK:335 | likša : louse, flea eggs
5	  #2 (parent #1) [Persian] refs=HRN:137; BQT:952 | rešk «ریشک» : flea eggs
6	#3 (parent #0) [Latin] refs=POK:335 | ricinus : flea
7	  #4 (parent #3) [English] refs=AHD:1116 | ricin : a poisonous protein
8	
```


## [2026-09-05T20:29:55.505Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-159.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-05T20:29:55.570Z] TOOL RESULT

```
{
  "pdf_page": 159,
  "book_page": 129,
  "entries": [
    {
      "root": {
        "name": "Erek",
        "lang": "Indo-European",
        "refs": "POK:335",
        "gloss": "flea, mite"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:335",
          "words": [
            {"translit": "likša", "gloss": "louse, flea eggs", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:137; BQT:952",
          "words": [
            {"translit": "rešk", "gloss": "flea eggs", "script": "ریشک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:335",
          "words": [
            {"translit": "ricinus", "gloss": "flea", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:1116",
          "words": [
            {"translit": "ricin", "gloss": "a poisonous protein", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== MATRIX ===
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


## [2026-09-05T20:30:11.032Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ricinus\" POK_full.txt | head -20; echo \"--- likša ---\"; grep -n -i \"liksa\\|likṣā\\|likša\\|likscha\" POK_full.txt | head -20; echo \"=== erek ===\"; grep -n \"erek\" POK_full.txt | head -30",
 "description": "Grep Pokorny for ricinus, likṣā, erek"
}
```


### [2026-09-05T20:30:11.127Z] TOOL RESULT

```
27435:Latin ricinus 1 . ' itself in the skin of sheep, dogs or cattle annoying vermin, tick ' 
27436:(doubtful is the affiliation from 2. ' a shrub kind, castor bean, ricinus ') could go back to 
--- likša ---
27432:Old Indie liksa 'nit, louse' common Old Indie gh- > ks- (probably from */a/rsa through 
=== erek ===
13313:Note: extensions of b'^er- "shine, appear, seem', b'^ereg-, b'^erek- 'shine'. 
16883:(Zr|v lengthened Zr|va, Zv\ybc„ Zr|vi; about Zat; by Pherekydes of Syros s. Schwyzer Gr. 
19120:derek-. 
27404:Root / lemma: erek-1 {erfejgh^ 
27414:Root / lemma: erek-1 {eije]gh^\ louse, tick, derived from a suffixed Root/ lemma: er-2, eri- 
27423:under Indo Germanic *erek-. Furthermore it is to be compared Armenian o(r)Jirv\\\., louse' 
46005:KopKOpuyn), Serb, krakoriti^ cackle ', kir. kerekorfty^ gobble, coo '. 
60064:mrakb^ darkness', russ. morok^ darkness, fog, clouds'; russ. merek^ imaginary 
69749:Armenian erek and erekoy 'even\ng'; also Adverb erek' yesterday '; 
87149:n., tisroi.; Armenian erek {treies); gr. Tp£T(;, gort. Tpee(;, m. f., alb. tre, f. //v' (originally 
91251:Material: A. root nouns uer- gr. Frip- in hom. (sni) npa cpspsiv "einen Gefallen tun', Pherek.
```


## [2026-09-05T20:30:12.967Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','HRN','BQT','AHD','MON','ARY','KLN','WLD','IEC','SYN','LEW','LAT','SKT','FSD','WEB','HUB']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600]); print()\n\"",
 "description": "Show refs_online entries"
}
```


### [2026-09-05T20:30:14.787Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
```


## [2026-09-05T20:30:17.660Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27395,27460p' POK_full.txt",
 "description": "Read Pokorny erek entry"
}
```


### [2026-09-05T20:30:17.735Z] TOOL RESULT

```
but Middle Irish o/'>t'5/>70' 'grains' stands for *arbainn, older arbanna {above S. 63). 

Probably borrowings from a common, probably east-mediterranean origin, from which 
derives also Old Indie aravindam ' lotus '. 

References: WP. I 145, WH. I 419 f., 863. 
Page(s): 335 

Root / lemma: erek-1 {erfejgh^ 



Meaning: louse, tick 

Note: often distorted taboo 

Note: 

Root / lemma: erek-1 {eije]gh^\ louse, tick, derived from a suffixed Root/ lemma: er-2, eri- 

: goat; sheep. 

Material: 

In e- grade: 

Lithuanian erke't\ck, sheep louse' {*erkia), Latvian erce^ cow's mite, wicked, evil person' 
under Indo Germanic *erek-. Furthermore it is to be compared Armenian o(r)Jirv\\\., louse' 
(here seems to be a root variant er(e)gh-, as also in the consecutive alb. form) and ork'iun 
"ringworm, itching, erysipelas' (from * orqndno- {1) with a-/70suffix as in Latin after 
Petersson KZ. 47, 263 f.), alb. e/yy/z 'small louse' (see G. Meyer Alb. Wb. 96; doubt by 
Hermann KZ. 41, 48; however, the irregular guttural in Armen. and Alban. could be based 
on taboo distortion). 

In zero- grade: 

Old Indie liksa 'nit, louse' common Old Indie gh- > ks- (probably from */a/rsa through 
influence of likhati' scarifies '); 

Latin ricinus 1 . ' itself in the skin of sheep, dogs or cattle annoying vermin, tick ' 
(doubtful is the affiliation from 2. ' a shrub kind, castor bean, ricinus ') could go back to 
older *recinos and be shared with Lithuanian erke^Wck, sheep louse'. 

References: WP. 11 45, II 344. 
Page(s): 335 



Root / lemma: er(e)k-2, rek-, rok- 

Meaning: to tear, cut, split 

Material: Old Indie //r/7a-/7' flayed, rubbed off bald ',//r5a-/7 'naked, bald, bleak', //rsaAa-/? 

'cusp, peak, thorn'; common Old Indie ^/7- >/r5- 

Lithuanian y-e^/ra, pra-j-erka 'slit'; (about Latvian efcis ' juniper ' etc. see above S. 67 f.); 
with other ablaut grade Lithuanian ranku, rakti^sWck in, poke', /"a/rsZ/'s 'splinter, thorn', etc. 

References: Persson Beitr. 839. 

See also: In addition belongs also: eres-/ 'prick'. 

Page(s): 335
```


## [2026-09-05T20:30:32.704Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN rishk/resk ===\"; grep -n -i \"rišk\\|risk \\|rešk\\|resk\\|Nisse\" HRN.txt | head -30",
 "description": "Grep Horn for rešk / Nisse"
}
```


### [2026-09-05T20:30:32.773Z] TOOL RESULT

```
=== HRN rishk/resk ===
390:verderbnisse oder ünechtheit der betreffenden Verse an ; er
824:Die Lautverhältnisse von äinaj und mätk passen
1078:71. er esk 'Neid, Eifer, resk.
1212:die Lautverhältnisse verkennt.
2440:Onomatopoetisch, sonst würden die Lautverhältnisse
3218:*) Die Verhältnisse liegen bei diesem Worte nicht klar. Darf
5506:resk s. eresk (No. 71).
5507:618. risk 'Lauseei, Nisse' (AM. 141 Zeile 11, 191 Zeile 7).
5508:ai. liksd' 'Ei einer Laus, Nisse' (Nöldeke bei
5510:kurd. LW. risk ; af/. riya ; bei. LW. rask, risk 'Läuse'
5511:(217); oss. t. llsk, d. liskä 'Nisse' (170).
5747:an wichtige, positive Ergebnisse.
6827:lebnissen in Persien' durchweg als einen genauen Kenner des Porsischen;
8071:neupersischen Kenntnissen des Verfassers darf man in solchen Fällen
8634:findet man bei F. Stolze und F. C. Andreas, Die Handelsverhältnisse
8753:sind die Lautverhältnisse von af/. woyai bezw. wökii
9176:Die Lautverhältnisse sind noch nicht richtig er-
9812:Um Missverständnisse unmöglich zu machen, mache
11629:eresk 71.
19556:I risk 618,
```


## [2026-09-05T20:30:35.077Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW ricinus ===\"; grep -n -i \"ricinus\" LEW_1910.txt | head; echo \"=== LAT ricinus ===\"; grep -n -i \"ricinus\" LAT.txt | head; echo \"=== WLD b1 ricinus ===\"; grep -n -i \"ricinus\\|erke\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20",
 "description": "Grep Latin dictionaries and Walde-Pokorny"
}
```


### [2026-09-05T20:30:35.150Z] TOOL RESULT

```
=== LEW ricinus ===
=== LAT ricinus ===
19170:Adj.: e ricinus (Aug., joint a leporinus). Lea gloses ont aussi un
33340:avec Xt| 9 ti (Varr. L.L.7,43); le verbe le 5 semble avoir ete extrait deleuaricinus
33343:leuaricinus: nom d'un poisson dans Polem.Silu. M.L.5001. Tardif,
39088:du type berbecinus, hircinus, porcinus, soricinus, uacclnus. On a dit7 37
53514:Derives: ricula (dim.); ricinus (re-): -a ttiro (Varr. ap.Mon.539,36);
53520:ricinus, -I m.: 1° tique, pou du mouton. Mot rural (Cat., Varr.,
59409:Derives: soricinus, cf. soricina naenia Pl.Ba.88y. Les 1 . romanes
=== WLD b1 ricinus ===
136:Pietat vorgegangen, um den einheitliehen Charakter des Werkes nicbt zu 
156:erhoht als herabgemindert. Der ganze Aufbau des Werkes ist im 
169:Bezuglich der keltischen Etymologien mochte ich noch bemerken, daB 
214:groBeren Teile des Werkes die moderne Orthographie durchzufiihren, an- 
819:Alb. idste „bitter“, idetiim , tosk. iderim „Bitterkeit, Zorn, Arger, Trauei'“ 
931:ahd. eihhan „zuerkennen“, s. Hoffmann rioas 39. 
1158:v dS, lat. de. — Ein aind. va- neben ava- ist wohl nicht anzuerkennen, siehe 
1290:Ai. avati mit ud- und pra- „aufmerken, beachten“, aksl. mm „Yerstand“ 
1418:audkendr „leicht zu erkennen“; Gdbed. sei „willig“, woraus ..leiclit zu 
1427:usvv.) mit der i-Basis *auri-, ohne aber zu verkennen, daB *uci- auch weiter 
1770:oder kelt. (Much IF. 21, 314) *upnos aus *uq“nos. — Verkehrt uber lat. 
2170:-eris „Umfriedigung, EinscliluB, Kerker, Schranken“, diss. cancer, cancel! t 
2316:und *ok-(oq-) „spitz“ der Anerkennung dieses Ablautes zu entziehen und 
2856:tennis „alljahrlich wiederkehrend oder gefeiert, feierlich; iiblich“ (Neben- 
2966:rucchen, ags. edrocinn „wiederkauen“, ags. cdcerr „Wiederkehr'‘, s. weitere 
3374:opaky , apace „zuruck, verkehrt", in welchen freilicb z. T. aucb zu *opi, gr. 
3378:ahd. abuh, abah „abgekehrt, verkehrt, bose“ (nhd. abig, abicht ), ags. *afoc 
3503:lautgerecht als *ap- wiederkehren : altn. npi m. „A£fe, Tor“, apa f. (auch 
5681:Tauscb, Yerkehr", aXlod-anog „von anderswoher, fremd, auslandisch" (For- 
6276:lage anzuerkennen. Fiir <■ ist c-briiis tetymologisch dunkel), kein sichererer
```


## [2026-09-05T20:30:44.606Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5495,5525p' HRN.txt; echo \"=== page of line 5507 ===\"; awk 'NR<=5507{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line 5507:\", n}' HRN.txt",
 "description": "Horn entry 618 context and leaf number"
}
```


### [2026-09-05T20:30:46.633Z] TOOL RESULT

```
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
') Yd. 13, 45. Aber ganz annoher.- 138 -
raw(i)sn; vergl. lat. repö, lit. replioti, lett. rayt
'kriechen*.
kurd. rewin ; bei. LW. röag, rowag, n. raway (o22) ;
\va/. vä-refsam, sar. va-rafsam.
Gehört hierher auch np. ram eilend, fliegend' (Pfeil)
=== page of line 5507 ===
formfeeds before line 5507: 158
```


## [2026-09-05T20:31:02.431Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== v2 pages tags around 952 ===\"; grep -n \"ریشک\" BQT_v2_pages.txt | head -20; echo \"--- reshk ---\"; grep -n \"رشک\" BQT_v2_pages.txt | head -20",
 "description": "Grep Borhan vol2 for ریشک / رشک"
}
```


### [2026-09-05T20:31:02.527Z] TOOL RESULT

```
=== v2 pages tags around 952 ===
--- reshk ---
2724: ‫وآنچه بدان صوف وشال وجامهای دیگرشکتجه‬                        ‫‪ ۰‬دوای اس ت که آرا سرج مرد‬         ‫ورای فرشت‬
5934:‫جراحتی راکوبند کهدهاش بسته شود لیکن در‬                 ‫لشکر یعنی جمعی که از پن سلرشکر براه‬
6686:                                                                    ‫برافشاندم خدوا لودچله درشکاف او‬
7836:         ‫فاض ‪۷۲۲‬؛ درآخر کلمات غیرتر کی نز آرند همجون درشکه‌چی ‪ .‬ارابه چی » تماشاچی ‪-‬‬
10828:                     ‫*‪« -۶‬خرچال» مرغیاست برشکل بطبزرکه‪ .‬زینبی کوبد ‪:‬‬                                 ‫چال («‪.‬م‪).‬‬
12139:       ‫خسر وروز درشکارگاه‬                             ‫‪(e.1‬‬        ‫(‏ ‪- ۰۵‬‬
16006:      ‫دارکوب‬                      ‫باکاف قارسی‬     ‫قرزهدی که درشکم مرده باشد بیفتد ‪ -‬و ستبل‬
17541:   ‫مأخون از آلمالی‬           ‫‪ ۵‬درشکه ‪ -‬بطم اول و دوم و کمر چهارم ‪ .‬از روسی ‪۴020۳‬‬
17542:   ‫‪6‬درشکه)؛ گردونۀ چهار چرخه که با اکسشبیده شود و اطافکی برای حمل مسافر‬                ‫(‬
19399: ‫خوار کر= پتشخوار کره‬       ‫پشودارشکر‬
19489:‫روزی رستم وطوی درشکار گاء] یبا دختری افتند‬           ‫بنیقطه بتحتانی زده ک»ثابه از عیب جوی وعیب‬
19741:  ‫خوانند ودر دواها بکاربرند خصوص‌درمرض‌استقا‪.‬‬                         ‫است مانند کره که درشکم بهم‬
21508:‫باشد وآن ازکان مس حاصل میشود » ورنگه‌آن‬                ‫وپرخوری رشکم‌خوار ‪ 2۳‬وبدزبانی وظلم وتعدی‬
23974:   ‫ابرشکور بلخی «لفت‌فری‪٩۸۹-۹‬‏ ‪.‬‬
24308:      ‫بازکوبم له که کس‌سیر خواهد بودن‪ «.‬کلستان‪.»۸۳۱‬‬          ‫رشکم آید که کسی سیرنگه درن وکند‬
24343:                                                     ‫رشکن ‪ = ۳‬بقتح‌اولو کرکاف وسکون‬
25699:   ‫اوشیروان عادل را درشکار گاه صیدی کداب کردند ولمك شود» غلامی بروستارفت‬                                           ‫‪2‬‬     ‫‪۷‬‬
26742:  ‫ین لبت ) تر کیب شده لظیر ‪ :‬رشکن » ربخن »‬                        ‫‪ 4‬ان ( =‬        ‫‪ 0‬میرساند کهکلمه از ‪ :‬ریم‬
27502:                 ‫پیکان تیرشکاری باکشدی‪-‬و‬
28230:                    ‫‪ ۷‬۔ زرشك ہا امبر باریس ‪ 51۲6۵۲6۳‬ازتیرۂ زرشکیان ‪٤٤‬‬
```


## [2026-09-05T20:31:05.251Z] TOOL CALL #11: Bash

```json
{
 "command": "pdftoppm -f 159 -l 159 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg159 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 159"
}
```


### [2026-09-05T20:31:07.293Z] TOOL RESULT

```
total 15384
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:31 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:31:13.194Z] TOOL CALL #12: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg159.png"
}
```


### [2026-09-05T20:31:13.591Z] TOOL RESULT

```

```


## [2026-09-05T20:31:13.588Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:31:13.927Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))['BQT']\nfor k,v in d.items(): print(k,':',str(v)[:900])\n\"",
 "description": "BQT ref details"
}
```


### [2026-09-05T20:31:15.771Z] TOOL RESULT

```
title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
kind : archive_djvu+local_scan_ocr
url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.
lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only t
local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verific
page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017,
covers_etymology : True
notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only
scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming
cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
```


## [2026-09-05T20:31:26.536Z] TOOL CALL #14: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 159 -l 159 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf $S/pg159_600 && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg159_600.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.55),int(h*0.13),int(w*0.80),int(h*0.185))).save('$S/pg159_word.png')\n\"",
 "description": "Crop Persian word from page 159"
}
```


## [2026-09-05T20:31:28.247Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==410||NR==409||NR==411 {print \"----- leafblock\", NR, \"-----\"; print substr($0,1,1500)}' BQT_v2_pages.txt | head -80",
 "description": "Print BQT vol2 leaves near 409"
}
```


### [2026-09-05T20:31:31.282Z] TOOL RESULT

```
(5100, 6600)
```


### [2026-09-05T20:31:32.977Z] TOOL RESULT

```
----- leafblock 409 -----
 ‫—‪AtA-‬‬                                                                                          ‫رستاخیز‪‎‬‬
 ‫رستگار است کهبمعنی خلاص و فجات باشد ‪-‬‬                    ‫بموط هم‬     ‫ضحک‬
                                                                        ‫می م‬‫وعت‬
                                                                              ‫روبید وبرآمد ‪ - ۱‬وی‬
 ‫و تزد محققین صاحب دولتی است که زخارف‬                      ‫آمده است ؟ ‪ -‬و نوعی از خاك سخت باشد ‪-‬‬
‫او‬   ‫دامنگیر حال‬   ‫وممنوی‬       ‫و تملقات موری‬    ‫دلوی‬
                                                           ‫ومطلق خاکه را نکیفزته اند‪ -‬و بمعنی شجاع‬
                                                ‫نباشد ‪.‬‬    ‫ودلیر ‪ -‬وچیره وغالب آمدن ومتولی شدن هم‬
                                                                                                  ‫‪۰‬‬   ‫صبت‬
‫‏‪ o‬بروزن افلااء ‪ ۰‬شاج ءازه ای‬        ‫رستاك‬

‫راکومند که ازبیخ درخت برآبد ؛ و پاین معنی‬                   ‫‪)۱‬‬
                                                             ‫رستا
----- leafblock 410 -----
  ‫با‬                                                                                             ‫‪-‬‬

‫وفتح فوقالی وها ومیم هردوسا کن » رستم زالرا‬         ‫رسته ‪ ۱‬ب«روزن دسته ‪ ۰‬بمعنی خلاص‬
                                     ‫ف‪2‬‬              ‫شده ولجات‌بافته باشد ومطلق صفرالگیوزبند‬
                                                     ‫اعم از انان وحیوان دیگر ‪ - ۴‬وراستة هرچیز‬
‫رسقی = بض‌اول بروزن ستی " راحت‬
                                                    ‫بازار‬    ‫و راستة‬    ‫دندان‬   ‫همجو راستةٌ‬     ‫هت‬   ‫هم‬
‫وفراغت باشد ‪ - 6‬وخر کی ودلیری و شجاعت‬
 ‫وغالب شدن و مستولی گردیدن را بیز گوبند ‪-‬‬           ‫وخالهابی که دريك صف واقع شوند ‪ -‬و بمعنی‬
 ‫وبمعنی‌رزق وروزی‪ -‬ونان حولواوماحضروخوردلی‬          ‫فاعده وقانون وطرز وروش باشد ‪ -‬ونزد محفقین‬
‫اندك هم هست ‪ -‬وبمه‌نی محکمی واستحکام نیز‬            ‫شخصی امت که درظاهروباطن گرفتاری ولآود کی‬
 ‫آمده است ‪ -‬و بفتح اول ععنی خلاص ولجات�
----- leafblock 411 -----
   ‫ها‬    ‫وی‬   ‫‪-‬‬
                                                                                                                           ‫رس‬




‫مقرب وترديك راگوبند همچو سفرچی و آبدار‬                                           ‫‪۴‬‬    ‫ساد معرباست‬           ‫رصد‬   ‫و‬     ‫هیر سد‬


 ‫وآنانکه سال سال وماه بماه ورور‬              ‫وشرابداروساقی‬         ‫‪ ۰‬خدمتکار‬   ‫يفنح اول بروزن‌خهم‬           ‫”‬   ‫ر سم‬

                                      ‫بروز راف گنف ‪۰‬‬               ‫نزديك باشد حمچوآ بدار وجامه‌دار وامثال آن ‪-‬‬
 ‫رسنواد؟ م بفتح اول و نون بر وزن‬                                   ‫ربمعنی‌داغ‌وشان هم‌هست‪ -‬وشیوه‌وعادت ومتعارف‬
 ‫کسمواد * بزبان زند و پازند (‪ )۱‬نبزۀ خطی‬                                                                ‫را یز گفته‌ایں ‪. ۱‬‬
                        ‫وبعربی رمح خوانند ‪*#.‬‬         ‫باشد‬
                                                                   ‫‪ -‬بروزن بدخو ؛ زور عل زا‬                     ‫رسهو‬

‫دسین ‪ = ۲‬بروزن‌بین‪ ,
```


## [2026-09-05T20:31:44.246Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=txt.split('\\f')\nprint(\"nleaves\",len(leaves))\nfor i,l in enumerate(leaves):\n    if 400<=i<=430:\n        for pat in ['رشک','رشك','ریشک','ریشك','شپش','تخم شپش']:\n            if pat in l:\n                for m in re.finditer(pat,l):\n                    print(i, pat, repr(l[max(0,m.start()-90):m.start()+90]))\nEOF",
 "description": "Search Borhan leaves 400-430 for rešk"
}
```


### [2026-09-05T20:31:45.843Z] TOOL RESULT

```
nleaves 684
406 رشک 'ز چشم است کوبد رژدی گلوی\u202a.\u202c\u202c                   \u202bز دبدار خیزد هزار آرزوی\u202c      \u202b\u202a۱\u202c\u202c\n   \u202bابرشکور بلخی «لفت\u200cفری\u202a٩۸۹-۹\u202c\u200f \u202a.\u202c\u202c\n   \u202bویایگانی ودامالی\u202c\n                  \u202b\u202a ۷\u202cط\u202a-\u202cبری \u202a( 2'
412 رشک 'لی \u202a« 0156۲\u202cامام»\u202a:\u202c\u202c\n      \u202bبازکوبم له که کس\u200cسیر خواهد بودن\u202a «.\u202cکلستان\u202a.»۸۳۱\u202c\u202c          \u202bرشکم آید که کسی سیرنگه درن وکند\u202c\n     \u202b\u202a «۷\u202cبباید داست که دربیان معنی رشك مصنف بچند وجه خط'
412 رشك '                                                                       \u202bب دار بندید \u202a.\u202c\u202c\n\u202bرشك = بفتح اول و سکون الیوکاف»\u202c\n                                                      \u202bمدت'
412 رشك 'ن\u202a.»۸۳۱\u202c\u202c          \u202bرشکم آید که کسی سیرنگه درن وکند\u202c\n     \u202b\u202a «۷\u202cبباید داست که دربیان معنی رشك مصنف بچند وجه خطا نموده \u202a :\u202cاول\u202c                   \u202bغی\u202a-\u202cرت\u202a.\u202c\u202c\n                      '
412 رشك '\u202c\n      \u202bآنکهرخك بالفتح بمعنی کرم گفته واین\u200cخلاف جمهور اهل\u200cلفت است\u202a .\u202cچه درفرهنگهای معتبرمرشك\u202c\n    \u202bبالکسر بمعنی تخم شیش که بهندی لیکهه کوبندآمده\u202a ,\u202cوآن غير کرم است \u202a .\u202cدوم آنکه کف'
412 رشك ' » زیراکه درعربی صوابه بوزن غرابه\u202c\n     \u202bبمعنی همان تخم شپش آمده لهبمعنی کرم \u202a ,\u202cسوم آنکه رشك بمعنی عجب ونکبرهم گفته و این\u202c\n      \u202bدر هکیتچاب ازکتب\u200cمتداولة لفت نیت \u202a ,\u202cازبنجاست که '
412 رشك 'ع \u202akhsir\u202c\u200f > افغانی \u202aaxir\u202c\u200f \u202a .\u202cبلوچی ع\u202c          \u202b\u200f\u202aA\u202c\u202c\n\n     \u202b(خم شیش )\u202c \u202bشمان گوید \u202a :\u202cرشك ت\u202c\u202bو\u200fب»\u202c\n                                   \u202bتق \u202a٩\u202cه\u202a۸۱\u202c\u202c   \u202b«ناا\u202a.\u202cسینا\u202c\u202bعاطف\u202ak , :2\u202c'
412 شپش ' عربان صوب کوبند » و ابن نیز خطاست » زیراکه درعربی صوابه بوزن غرابه\u202c\n     \u202bبمعنی همان تخم شپش آمده لهبمعنی کرم \u202a ,\u202cسوم آنکه رشك بمعنی عجب ونکبرهم گفته و این\u202c\n      \u202bدر هکیتچاب ازکت'
412 شپش "راض «چك» ورد معنی «کرم»» صوابه وصجب وتکیر وارد است \u202a.\u202c\u202c\n     \u202bهندی باستان \u202a( (24992۱1\u202cنشم شپش)' کردی ع \u202akhsir\u202c\u200f > افغانی \u202aaxir\u202c\u200f \u202a .\u202cبلوچی ع\u202c          \u202b\u200f\u202aA\u202c\u202c\n\n     \u202b(خم شیش )\u202c \u202bشما"
412 تخم شپش 'ر را عربان صوب کوبند » و ابن نیز خطاست » زیراکه درعربی صوابه بوزن غرابه\u202c\n     \u202bبمعنی همان تخم شپش آمده لهبمعنی کرم \u202a ,\u202cسوم آنکه رشك بمعنی عجب ونکبرهم گفته و این\u202c\n      \u202bدر هکیتچاب '
413 رشک '                 \u202bآمدہه است \u202a. ۱\u202c\u202c\n\n                                                     \u202bرشکن \u202a = ۳\u202cبقتح\u200cاولو کرکاف وسکون\u202c\n                                                     \u202bان'
```


## [2026-09-05T20:31:52.682Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=txt.split('\\f')\nl=leaves[412]\nimport re\ni=l.find('رشك = بفتح')\nprint(l[:200])\nprint('...')\nprint(l[-2200:])\nEOF",
 "description": "Print BQT leaf 412 head and footnotes"
}
```


### [2026-09-05T20:31:54.382Z] TOOL RESULT

```
    ‫‪“Ao‬‬
                                      ‫‪e‬‬
‫رشته نگنده ‪ -‬بکر نون وفتح‌کاف‪‎‬‬                        ‫رشته = بکراولوفتح فوقانی»تارابرشم‬
‫‪۰‬‬    ‫بی قطة مقتوح‪‎‬‬      ‫نون وال‬      ‫
...
           ‫گفه‌اید ‪.‬‬


     ‫‪ ۴‬آنرا در سواحل خلیح فاری لا گویند‬                ‫تن؟‪.‬‬ ‫اسم مقمول ارزش«‬        ‫‪8‬ے‬
     ‫‪-‬يزچيزی مانند تواررشته های باريك که از خمیرآرد کندم سازد وازآن‬ ‫‪ ۴‬ل‬                 ‫عو‪.‬‬   ‫ورك‪:‬‬


     ‫م‪).‬‬   ‫‪.‬‬   ‫(ه‬   ‫از ‪:‬رشت‬   ‫‪۴‬‬   ‫آش وجزآن ترتب دهند وبتازی «رشیدبه» کویند «ناظمالاطبا؟‪.‬‬
     ‫® = ارخك ( «‪.‬م‪ . ) .‬اوستا ‪ 265272‬پپلوی ‪khsar ۰ 10572‬‏ «‬                  ‫‪+‬ی (سبت)‪.‬‬
     ‫بلوچی‪« 97101‬اسشق شمارء ‪۱۷‬وص ‪ ۷۳۱‬ورك‪ :‬منای ‪ »)6105172( ۷۲:۲‬دزفولی ‪« 0156۲‬امام»‪:‬‬
      ‫بازکوبم له که کس‌سیر خواهد بودن‪ «.‬کلستان‪.»۸۳۱‬‬          ‫رشکم آید که کسی سیرنگه درن وکند‬
     ‫‪ «۷‬بباید داست که دربیان معنی رشك مصنف بچند وجه خطا نموده ‪ :‬اول‬                   ‫غی‪-‬رت‪.‬‬
                                                                                           ‫‪۷‬‬
      ‫آنکهرخك بالفتح بمعنی کرم گفته واین‌خلاف جمهور اهل‌لفت است‪ .‬چه درفرهنگهای معتبرمرشك‬
    ‫بالکسر بمعنی تخم شیش که بهندی لیکهه کوبندآمده‪ ,‬وآن غير کرم است ‪ .‬دوم آنکه کفنه که‬
     ‫کرم مکذور را عربان صوب کوبند » و ابن نیز خطاست » زیراکه درعربی صوابه بوزن غرابه‬
     ‫بمعنی همان تخم شپش آمده لهبمعنی کرم ‪ ,‬سوم آنکه رشك بمعنی عجب ونکبرهم گفته و این‬
      ‫در هکیتچاب ازکتب‌متداولة لفت نیت ‪ ,‬ازبنجاست که بعضی‌از متأخرین انکار این معنی‌نموده‌اند‬
      ‫گوفته کهاین‌معنی‪ -‬یعنی معنی عجب وتکبر ‪ -‬سند میخواهد ‪ .‬وافهاعلم بالسواب ‪ « » .‬چك ص‬
      ‫و خواداری‪( 60152۲‬بقتح راء)‬          ‫ولی‬
                                            ‫زیفو‬ ‫ح » ابمماعنی تخم شیش » دکریلکی و بل‬
                                               ‫دوچ‬                                              ‫‪۱‬‬
                          ‫است » اما اعتراض «چك» ورد معنی «کرم»» صوابه وصجب وتکیر وارد است ‪.‬‬
     ‫هندی باستان ‪( (24992۱1‬نشم شپش)' کردی ع ‪khsir‬‏ > افغانی ‪axir‬‏ ‪ .‬بلوچی ع‬          ‫‏‪A‬‬

     ‫(خم شیش )‬ ‫شمان گوید ‪ :‬رشك ت‬‫و‏ب»‬
                                   ‫تق ‪٩‬ه‪۸۱‬‬   ‫«ناا‪.‬سینا‬‫عاطف‪k , :2‬طوتا‏ ‪ .‬اتی ی‬
      ‫انی ‪( 201۲‬نخم‌شیش) = ابرانی ‪ 2601511 -‬برابرسا کریت ‪ « 8091‬حوبمان‬‫ظارسفیت=‬
     ‫«امام» ک»یلکی ط‪ 5۵۲‬و درتهرانی ‪ 98۴‬ب(کرراه )‬                 ‫دزفولی و خواداری که‬           ‫‪۸‬‬
```


## [2026-09-05T20:32:03.530Z] TOOL CALL #18: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg159_word.png"
}
```


### [2026-09-05T20:32:03.548Z] TOOL RESULT

```

```


## [2026-09-05T20:32:16.834Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LAT ricinus ==\"; sed -n '53505,53535p' LAT.txt; echo; echo \"== AHD watkins erek/ricin ==\"; grep -n -i \"erek\\|ricin\\|likṣ\\|liksa\" AHD_watkins1985.txt | head",
 "description": "Ernout-Meillet ricinus; Watkins"
}
```


### [2026-09-05T20:32:16.899Z] TOOL RESULT

```
== LAT ricinus ==
r(h) onchus: -y.roncus.rhythmus
- 10 13
rhythmus, -I m.: rythme, cadence. Emprunt siyant atteste de-
puia Varr. au gr. pi> 0 p, 6 s; rhythmicus (Cic.), passe par l'ecole en fr.
rime, M.L.7394b, et en iri. rithim.
rica, -ae f.: piece de drap, carree et bordee d'une frange, que
les femmes portaient en guise de coiffure et qui servait surtout
aux pretresses flamines, ou dans les ceremonies religieuses. Cf.
Varr., L.L.5,130; P.F.369,1; Fest.343,30.
Derives: ricula (dim.); ricinus (re-): -a ttiro (Varr. ap.Mon.539,36);
ricinium (re-): coiffure en forme de rica que les femmes portaient
en signe de deuil, cf.Rich, s.u.
Termes archaiques qui, apres Varron, ne figurent plus que dans
les gloses.
Sana etymologie connue.
ricinus, -I m.: 1° tique, pou du mouton. Mot rural (Cat., Varr.,
Coi., etc. ), M.I/.7300; 3 0 ricin, piante appelee egalement cici ou croton,
Plin.15,35; 3° mfire imparfaite: ricinos, Graeci uocant , Plin.33,137.
Seul le premier sens est ancien et usuel; il est possible que les
d-eux autres appartiennent a un homonyme de tout autre origine.
Sans etymologie connue.
ricto, -as, - 5 re: crier, rugir, en pariant du leopard. Se trouve
seulement dans Spartianus (ili® s. apros J.—C.); forme sans doute
sur rictus.
rictus, -us (rictum): v. ringor.
rided, -Ss, -si, -sum, ridSre: rire (sens absolu et transitif,
cf.ri dere aliquem et 1'emploi passif: tuum enim non sal, sed natura
ridetur, Cic. De Or.3,Cy,379). Par suite "sourire", "avoir un esprit
plaisant". En po^sie, peut s'appliquer aux choses, comme le gr.yeXav
(of. renideo) et p,si6iccu). Usit^ de tout temps. Panroman. les formes
romanes supposent *ndSre, M.L.7303, sans doute forme sur risi,

== AHD watkins erek/ricin ==
336:bhereg-. To shine; bright, white. Compare the by-form bherek-. 1. Germanic *berhtaz, bright, in Old English beorht, bright: BRIGHT. 2. “The white tree,” the birch (also the ash): a. Germanic *birkjon- in Old English birc(e), birch: BIRCH; b. suffixed zero-grade form *bhrag-s- probably in Latin fraxinus, ash tree: FRAXI- NELLA. [Pok. bherag- 139.]
337:bherek-
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.] bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan (*for, before; see per') in: a. Old English béodan, to proclaim: BID; b. Old English forbéodan, to forbid: FORBID; ¢. Old High German farbiotan, to forbid: VERBOTEN, @: Germanic *tudén- in Old English boda, messenger, hence bodian, to announce: BODE!. 3. Ger- manic *budilaz, herald, in Old English bydel, herald, messenger: BEADLE. 4, Germanic *budam in Old Norse bodh, command: OMBUDSMAN. 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE. [Pok. bheudh- 150.]
1087:teue-. Also teu-. To swell. 1. Extended form *teuk- in Germanic *theuham, “the swollen or fat part of the leg,” thigh, in Old English théoh, thigh: THIGH. 2. Extended form *tis- in Germanic compound *thiis-hundi-, “swollen hundred,” thousand (*hundi-, hundred; see dekm), in Old English thisend, thousand: THOUSAND. 3. Suffixed zero-grade form *tu-l- probably in Germanic *thul- in Old English thol(l), oar pin, oarlock (< “a swelling”): THOLE PIN. 4. Extended zero-grade form *tiim- in: a. Germanic *thimoén- in Old English thima, thumb (< “the thick finger”): THIMBLE, THUMB; b. suffixed (stative) form *tum-é- in Latin tumére, to swell, be swollen, be proud: TUMESCENT, TUMID, TUMOR; DETUMESCENCE, INTU- MESCE, TUMEFACIENT, TUMEFY; C. suffixed form *tum- olo- in Latin tumulus, raised heap of earth, mound: TUMULUS. 5. Extended lengthened zero-grade form *tibh- in Latin tiber, lump, swelling: TRUFFLE, TUBER; PROTUBERATE. 6. Suffixed zero-grade form *tu-r-yo- in Greek turos, cheese (< ‘“‘a swelling,” “coagulating”’): BUTTER, TYROSINE, TYROTHRICIN. 7. Suffixed variant form *tw6-ro- in Greek sdros, heap, pile: SORITES, SORUS. 8. Suffixed variant form *twd-mn, in Greek sdma, body (< “a swelling,” “stocky form”): SOMA, SOMATO-, -SOME?; PROSOMA. 9. Suffixed zero-grade form *twa-wo- in Greek saos, sds, safe, healthy (< “swollen,” “strong”), with derivative verb sdzein, to save, rescue: CREOSOTE, SOTE- RIOLOGY. 10. Perhaps nasalized extended form *tu-m-b(h)- (or extended zero-grade form *tum-) in Greek tumbos, barrow, tomb: TOMB. [Pok. téu- 1080.]
1090:[thrix. Hair. Greek word of unknown origin (stem form trikh-). TRICHINA, TRICHO-, TRICHOME, -TRICHOUS; PERI- TRICH, STREPTOTHRICIN, TYROTHRICIN, ULOTRICHOUS. [In Pok. dhrigh- 276.]]
1320:BRACE mregh-u- BRACERO mregh-u- BRACH bhrag- BRACHIUM mregh-u- BRACHY- mregh-u- BRACKEN bhreg- BRACKET brak- BRAD _bhar- BRADYLEXIA leg-1 BRAE bherek- BRAHMA! bhiagh-men- BRAHMAN bhiagh-men- BRAHMIN bhlagh-men- BRAID bherok- BRAIL  brak-
1323:BREEKS brak- BREEZE bhreu-2 BREGMA mregh-m(n)o- BREMSSTRAHLUNG | ster-2 BREW bhreu-2 BREWIS bhreu-2 BRIAR! wer-3 BRIDE? bherek- BRIDEGROOM dhghem- BRIDGE! bhri- BRIDLE bherek- BRIEF mregh-u- BRIGHT bherag- BRIM bhrem-2 BRIMSTONE gWher- BRINDLED gWher- BRING bher-!
2319:STOVE! staup- sTow sta- STRABISMUS streb(h)- STRABOTOMY streb(h)- STRAIN! | streig- STRAIN?  ster-2 STRAIT  streig- STRANGE eghs STRANGLE strenk- STRANGLEs  strenk- STRANGULATE _ strenk- STRANGURY strenk- STRATAGEM ag-, ster-2 STRATH ster-2 STRATOCRACY  ster-2 STRATUS  ster-2 STRAW ster-2 STREAK streig- STREAM sreu- STREET  ster-2 STRENGTH  strenk- STREPTO-  streb(h)- STREPTOMYCES meug-2 STREPTOMYCIN meug-2 STREPTOTHRICIN  thrix STREUSEL ster-2 STREW ster-2
2423:TYROTHRICIN teue-, thrix
2437:UNITY oi-no- UNIVERSE 0i-no-, wer-3 UNIVOCAL wekw- UNKEMPT gembh- UNTIL ant- UNWITTING weid- UP upo UPANISHAD sed-1, upo UPBRAID bherek- UPROAR kere-, upO UPSILON bhes-! URCHIN ghers- UREDO eus- URETER wers-2 URETHRA wers-2 URETIC wers-2 URGE wreg- -URGY werg- -URIA wers-2 URINE wér- URO-! wers-2 URO-2 ors- URONIC wers-2 -UROUS ors- URSINE rtko-
```


## [2026-09-05T20:32:18.638Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN ricin ==\"; grep -n -i \"ricinus\\|^ricin\\|ricin,\" KLN_1966.txt | head -20; echo \"== SKT ==\"; grep -n -i \"ricin\" SKT.txt | head; echo \"== FSD3 ==\"; grep -n -i \"ricinus\" FSD_vol3.txt | head; echo \"== FSD4 ==\"; grep -n -i \"ricinus\" FSD_vol4.txt | head",
 "description": "English dictionaries for ricin"
}
```


### [2026-09-05T20:32:18.745Z] TOOL RESULT

```
== KLN ricin ==
32862:Ricinus,  n.,  a  genus  of  plants  (family  Euphorbia- ceae).  —  L.,  ‘the  castor-oil  plant’,  which  is  of uncertain  origin.
35972:Sorex,  n.,  the  genus  of  shrews  ( zool .)  —  L.  sorex, ‘a  shrew',  which  stands  for  *swor-ak-s,  and  is cogn.  with  Gk.  (lpa£  (for  *surak-s),  of  s.m., prop,  ‘the  squeaking  animal’,  from  the  I.-E. imitative  base  *swer-,  *surr-,  ‘to  buzz,  murmur, pipe’,  whence  also  OI.  svarati,  ‘sounds’,  OSlav. svirati,  ‘to  pipe’,  L.  susurrus ,  ‘hum,  whisper’.  See susurration  and  cp.  soricine.  Cp.  also  hyrax. sorghum,  n.,  a  genus  of  grasses.  —  ModL.,  fr.  It. sorgo,  ‘Indian  millet’,  fr.  ML.  surgum,  surcum, suricum,  fr.  L.  Syricum  ( gramerif  (grass)  of  Syria’, neut.  of  Syricus,  fr.  Syria,  ‘Syria’.  See  Syrian, soricine,  adj.,  pertaining  to  the  genus  of  the shrews.  —  L.  soricinus,  ‘belonging  to  the  shrew’, fr.  sorex,  gen.  soricis.  See  Sorex  and  adj.  suff. -ine  (representing  L.  -inus). sorites,  n.,  a  series  of  syllogisms  in  which  the  pred¬ icate  of  each  becomes  the  subject  of  the  next (logic).  —  L. ,  fr.  Gk.  noipcLT^c; ,  (reopen;?,  short  for ( vSXkoyKsij.be,  acopu-nr)<;,  ‘a  heap  of  syllogisms, a  sorites’,  fr.  ncop6;,  ‘a  heap’.  See  sorus. soritical,  also  soritic,  adj.,  pertaining  to  a  sorites. —  Gk.  aeoperixoc,  fr.  atopei-r/]?,  (Topitrii;.  See prec.  word,  resp.  also  adj.  suff.  -a!, soroptimist,  n.,  member  of  a  club  of  business women  and  women  executives.  —  Contraction of  sorority  and  optimist.
== SKT ==
5731:Eland,  a  S.  Africin  antelope.  (Do.* Slavonic.)  Du.  eiarui,  an  elk.  Of  Slav, origin  :  d.  Russ.  oUru^  a  stag ;  tee  Blk.
16544:Saunter.  <  F.  t)     Oricin  unknown.
== FSD3 ==
239778:lumlnw and with 2-jolnted mandibles 1 < L ricinus, a
239782:E horhiaeex). Ricinus communis, the castor-oil plant*
239784:several varieties [ < L ricinus, castor-oil plant ]
== FSD4 ==
35063:tick*,  n   1,  One  of  v   arious  acandan  arachnids  d'wehing on  plants  and  attaching  themselv  es  to  the  skin  of  man and  other  ammals,  in  which  they  bury  the  head  and suck  the  blood  Especially  (1)  An  Lxodld  mite,  as  the American  cattle-lick  (Ixodes  or  BoophUus  horts),  or  the European  dog-tick  (/  ricinus)  (2)  A   harvest-lick  (3) One  of  various  other  tlcl,s  as,  AusfraUau  cattle  fRk (Boophitus  australis),  common  In  Australia  and  the  Philip- pine Islands  black*pltted  t.  (Rhipicephalus  simus),  blue t   (Rhipicephalus  decolorrtus).  boot'leg  t.  or  Senegal  t. (Hpedoma  xjyptlum).  Brown  f   (Rhipicephalus  appcndlo ufafuj),  ail  of  South  Africa  fever-f.  (Sfaroaropus  annu~ lotus  Say) ,   infectious  among  cattle  lone  star  t.  (Amblyomma americanum) f   occurring  all  over  the  American  continent monbata  t   (Ofnl(ho<foro8  sacx^atO.  occasionally  infesting houses  and  Iflftlctlng  dangerous  bites  red  t   (Rhipicephalus ecartsi)  of  South  Africa  spinosc  ear-t.  (OrnUhodarus  meg~ nini  Duses'),  infecting  cattle  and  human  beings
```


## [2026-09-05T20:32:37.240Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD Bd1 Nisse/erke ==\"; grep -n \"Nisse\\|erke ‚\\|liksa\\|liksa\\|Schaflaus\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20; echo \"== WLD Bd2 ==\"; grep -n \"Nisse\\|liksa\\|Schaflaus\\|ricinus\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20; echo \"== WLD band3 ==\"; grep -n \"ricinus\\|liksa\" WLD_band3.txt | head",
 "description": "Grep Walde-Pokorny"
}
```


### [2026-09-05T20:32:37.353Z] TOOL RESULT

```
== WLD Bd1 Nisse/erke ==
9415:auf alteres *rccinos zuriickgehen und mit lit. erfe „Zecke, Schaflaus {*erl i r >), 
9417:Weiterhin ist zu vergleichen arm. o(r)d:il „Nisse, Lausei“ (hier scheint 
9427:fiber die Benennung der „Nisse“ vgl. Wood IF. 18, 23 f. Zu idg. *ereik- 
29025:qonid-, qnid-, sqnid- „Laus; Lausei, Nisse". 
29050:lens , -dis „Nisse“ und lit. gtinda ds., die vielleicht als ghlnd- untereinander 
48993:engl. tike und tick „Holzbock, Schaflaus", mnd. secke m. f. „Holzbock“, 
== WLD Bd2 ==
22394:will ai. liksd ,,Nisse, Lausei“, lat. ricinus „eiri sicb in die Haut von Scbafen, 
22397:erke „Schaflaus, Holzbock“, lett. erze „Kubmilbe“ (vielleicht aucb lat. rici- 
22399:*er(e)gh- reibt sicb arm. o(r)jil „Nisse, Lausei^^, alb. ergis, -zi „kleine Laus‘* 
22401:41, 48, und Yf. LEWb.^ u. ricinus\ liksd -Aikhdti scheint klar, kann aber 
== WLD band3 ==
```


## [2026-09-05T20:32:38.705Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC ==\"; grep -n \"liksa\\|Nisse\\|erke\\b\\|ricinus\" IEC.txt | head -20; echo \"== SYN nit ==\"; grep -n -i \"nit\\b\" SYN.txt | head -20; echo \"== HUB ==\"; grep -n -i \"risk\\|liksa\\|Nisse\" HUB.txt | head -20",
 "description": "Grep Mann, Buck, Hübschmann"
}
```


### [2026-09-05T20:32:38.787Z] TOOL RESULT

```
== IEC ==
436:aliksa (Slavonic type-variant of al?sos, ios, q.v.)
706:ark- ‘container, holder, protector”. Cf. arkeio Tokh.B erke ‘cemetery’; Arm. cf. -ark (in glx- ark ‘hať, lit. &^head-covering'; h-ark ‘cover, roof, dwelling’, fr. *epi-ark-; arky ‘box’); Lat. arx; arca; cf. arcanus ‘secret; OCS raka (grave, ditch. Not a LW), cf. also rakno ‘garment’; Cz. rakev (‘coffin’, fr. *arküs via *raky). LWs in Gmc. Cf. also Fest. arcula *warning bird of augurs'
3668:erk- (1) “tick, mite' Ir. earc ‘stinging insect, gadfly’; Li. erke ‘tick’; Latv. érce, id.
== SYN nit ==
515:le. imperat. imperf. impers. ind. indef. infin. init. instr. intr. iter. lc.
875:Skt. parisu-, pansuka-, Av. pasnu-: ChSl. péstikt ‘sand’, prob. fr. a root *pés- ‘blow’ in ChSl. pachati ‘toss, fan’, Russ. pachnit’ ‘blow’, etc. Walde-P. 2.68. Barth. 903.
885:Lat. limus (esp. ‘river mud’) prob. : OHG leim, OE lam ‘clay’, and fr. the root seen in Grk. adtvw, Lat. linere ‘smear’; perh. also (with init. sl- beside L-) OE slim ‘soft mud, slime’, etc. Walde-P. 2.389f. Ernout-M. 552. Walde-H. 1.804 f,
935:1. Group of words belonging together, but of partly obscure phonetic relations, prob. (init. doublets ps-, s-) fr. the root seen in Grk. Waw ‘rub, crumble’, Widos ‘pebble’, etc. (Skt. bhas-, psa- ‘chew, devour’, fr. ‘crush’). Kretschmer, KZ 31.420. Ernout-M. 881.
1598:MLat., It. rocca ‘citadel, lofty for- tress’, It. roccia ‘rock’, OFr. roke, rocque ‘castle on a rock’ (> ME rocke ‘rocky clif?, NE rock, MDu. rotse, Du. rots) Fr. roche (whence also Toc), rocher Sp. roca, Rum. rocd, of unknown anit iad 7357. NED s.v. rock, sb,
1735:Nit. teintreach : adj. teintreach ‘fiery’, fr. teine ‘fire’ (1.81).
1885:ChSI. stént, Boh. stin, Pol. cie#t, Russ. ten’, history obscure. Perh. *#éni fr. *tem-ni- : ChSl. tima ‘darkness’, etc. (1.62), and sténi a blend of this and séni (above, 1). Vondrak, Verg. Gram. 1. 431. Otherwise (double development of init. sk) Briickner 62.
1920:Grk. védos, vebédn, NG vedi, obvvedo ‘cloud’, Skt. nabhas- ‘mist, vapor’ (also ‘sky’); Lat. nebula ‘mist’, OHG nebul, etc. ‘mist’ (1.74); Lith. debesis ‘cloud’, Lett. debess ‘cloud’ but mostly ‘sky’, padebesis ‘cloud’ (all with init. d for n under the influence of some other word), ChSl. nebo ‘sky’, etc. Further, fr. *embh-, *mbh-, etc., Skt. abhra-, Av. awra- ‘cloud’, Grk. duBpos, Lat. amber ‘show- er’, etc.
2168:It. bruciare (cf. abbrustiare ‘singe’), Fr. braler (OFr. brusler), of much dis- puted orig. Perh. fr. Lat. ustulare ‘singe’, with init. br by a blend with Gme. words like OHG brennan, brunst. REW 9097.
2345:now rejected), late also dpoevixes, Gppevixds (cf. Andukés, below, 2), NG apoevxds, Skt. vrsan- (cf. vrsabha-, and rsabha- ‘bull’), Av. argan- (also varasna-, ef. NPers. gugan ‘male’), parallel forms with and without init. w, the former : Skt. vrs- ‘to rain’, varsa- ‘rain’, Grk. goon ‘dew’, the latter : Skt. rs- ‘flow’. Whether or not these two roots belong together formally, the semantic develop- ment is the same, ‘male’ from the notion of emitting semen. Walde-P. 1.149 ff., 269.
2678:Grk. ahs (a); yanéouat Goth. ug (act. a; pass. — Lith. bea ornate (i8)- bo- ON kvangask (a); gip- Lett.  prectt; iet pie vira (b) a Beg Lick ie, fiak (b) ey Ch&l. (o)zeniti se (2); posa- ela Dan. gifte sig galt (b) ; Lat.  diicere uzorem (a), Sw. gifta sig SCr.  o%eniti se (a); udati nitbere (b) OE weddian; wifian (a) se (b) It. sposare; maritarst (b) ME wed, mary Boh. (o)zentti se (a); uvddti Fy. se marier, Epouser NE marry (wed) se (b) vr! Sp. casarse Du. trouwen, huwen Pol. (o)éenié ste (a); 78¢ za Rum. se cdsdlori; se tnsura OHG hiwan mq (b) ae (a); se mdrita (b) MHG_ hiwen, hirdten Russ. Zenit'sja (a); vyitt za Tr. dobiur séitcht (a); in- NHG _heiraten muz (b)
2742:} Goth. luga Lith. (apsi-)vedimas, 18tek- a Lie ON giptung, pple éjimas (b); vestu- N Hee Said ridkaup, brullaup vés | Lat. coniugium, conutnin Dan. giftermaal, egte; bryl- Lett.  precéSands, lauliba; | tie ie ChSl. 6; rie 1 ) | : oe Sw. iftermdl, dkta; brél- .  brakit (maliizentstvo | een zoned, es SCr.  brak, Zenidba (2), Fr. see a oats 0: bodas OE weddung, sinscipe; udaja (b); svadba Bienes. cecil gifta, brgdhlop Boh. manielstvt, stiatek, Rum. Fe ranas ME  weddyng, wedlok, Zenitba (a), vdavky It. eh nak mariage (b); svatba a priodas; neithior NE marriage (wedlock); Pol. -malzenstvo, Slub; we- Br dimezi; eured wedding : sele : ; f Du. huwelijk, echt; brut- Russ. brak, supruzestvo, ze- loft nit'ba (a), zamu- OHG  hirat, éwa; britlouft Zestvo (b); svad’ba MHG hirdat, é(we); britlouft, Skt. vivaha-, patitva-, etc. hohzit Av. nairiéwana-
2868:ChSl. synit dusti
3854:Grk.  &réuvw Goth, =... Lith. romylti NG povvouxita ON gelda Lett. riinit, rdmit Lat. castrare Dan. _kastrere, sh@re, gilde ChSl.  skopitt It. castrare Sw. kastrera, snépa, galla SCr. Skopiti, Strojiti Fy. chatrer OE belistnian, (a)fyran Boh. _ vyklestiti, vyrezati Sp. _castrar, capar ME _gelde Pol.  mniszyé, walaszyé, Sue castra, scopi, jugdni NE - castrate, geld, cut, alter irzebié ae ne: u. lubben, ontmannen Russ. skopit’, cholostit’ ae nllim OHG  arfirian Skt. vadh-, bhid-
3897:Lett. rinit, fr. or cognate with MLG rine ‘gelding’ (Du. ruin, NHG dial. raun ‘gelding’), prob. from the root of Skt. ru- ‘break in pieces’, Lith. rayzj ‘tear out’, etc. Walde-P. 1.352.
3947:Nit. beathaidhigh ‘animals’ (3.11) also used commonly for ‘domestic animals’.
3980:a rel ets ie ON beita (a), bita (b) Lett. ganit (a); ganities (b) NG = Booxw (a, b) Dan.  gresse (a, b ChSl. pastt (a); pasomi, Lat.  pascere (act. a, b; Sw. beta (a, b) (pple. b)
4011:5. Lith. ganyti (a), refl. ganytis (b), Lett. ganit (a), refl. ganities (b), deriv. of Lith. genu, ginti, Lett. dztt ‘drive’ : ChSI. Zena, giinati, gong, goniti ‘drive’, Skt. han-, Grk. Oetvw ‘strike’, etc., Ii *gvhen-. Walde-P. 1.679 ff. Develop- ment from ‘strike’ to ‘drive’, then ‘drive cattle’, ‘tend cattle’. Cf. VLat. minare ‘drive cattle’ fr. mindrz ‘threaten’, and the specialization in NE drover.
4177:Dan. faar vaedder Sw. far bagge, viédur, gumse OE sctap ramm, weder ME _ schepe ram, wether NE sheep ram Du. _—schaap ram OHG | scaf ram(mo), widar MHG schaf - wider, ram NHG ss schaf widder, schafbock Lith. avis tekis, avinas Lett. atta, avs auns, tekulis Chsl.  ovica ovinit SCr. ovca ovan Boh. _ ovce beran Pol. owca baran Russ. ovea baran Skt. avi- mesa-, urana-
4484:3. Ir. gabor, NIr. gabhar, W. gafr, Br. gaor, gavr, perh. with unexplained init. variation : Lat. caper, etc. So Thurney- sen, Gram. 189, Z. celt. Ph. 13.108 ff. Otherwise Walde-P. 1.533, 547. es Goth. gaits, ON geit, OE gat, etc., a general Gme. word: Lat. haedus kid ; perh. Lith. Zaidziu, Zaisti ‘play’ as =H Jump, gambol’. Walde-P. 1.527.
== HUB ==
1286:die Lautverhaltnisse von padlruftan unerklarbar. Denn
2337:618. Np. riSk *Nisse' = afgh. riSa fem. ^Nisse* ( = iran.
2338:*riska^ Geiger, Etym. p. 46 gegenilber skr. likSOr),
4772:risk *Nisse' = skr. liksd-; bidast *Spanne' = skr. vitasti-;
5715:sind die Verhaltnisse die gleichen wie im Buchpehlevi : gur-
6073:zd. sris 'haften*; sirisk 'Tropfen', paz. srisk, zd. srasc 'be-
7572:mischen*, skr. griS (siehe oben p. 75) ; sirisk *Tropfen = zd.
7689:hingam *Zeit* H. 1109. Ebenso liegen die Verhaltnisse im
7820:idg. ''^skepti') ; sikdr * Jagd', siehe oben p. 80 ; sirisk *Tropfen'
8294:xism 'Zorn H. 490; nisastan *sitzen' H. 1033; risk 'Nisse
8295:(= iran. ^riska-, oben p. 67) H. 618; Oskdra *klar = skr.
8486:*) Vgl afgh. rica (np. risk) = skr. likaa-.— 238 —
8488:askarak, skr. aviskdra-; xusk *trocken = ap. mka-; risk
8489:'Nisse', osset. lisk, skr. liksa-; sirisk *Tropfen' = zd. sraska-;
9251:Np. r = skr. 7: risk *Nisse' = skr. liksa^, afgh. rica,
10682:risk 67.
```


## [2026-09-05T20:32:57.771Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls | head -40; echo \"---\"; grep -l \"cognate\" page-1*.json | head",
 "description": "List verification files"
}
```


### [2026-09-05T20:32:57.842Z] TOOL RESULT

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
page-109.json
page-110.json
page-111.json
page-112.json
page-113.json
page-114.json
page-115.json
page-116.json
page-117.json
page-118.json
page-119.json
page-120.json
page-121.json
page-123.json
page-124.json
page-125.json
page-126.json
page-127.json
page-128.json
page-129.json
page-130.json
page-131.json
page-132.json
page-133.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
---
page-103.json
page-102.json
page-110.json
page-111.json
page-112.json
page-115.json
page-106.json
page-105.json
page-123.json
page-114.json
```


## [2026-09-05T20:32:58.122Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"louse\\|'nit'\" SYN.txt | head -20",
 "description": "Buck louse"
}
```


### [2026-09-05T20:32:58.214Z] TOOL RESULT

```
3772:‘small beast of prey’ (cf. REW 476 on the derivs. of Lat. animal), ‘horse’ (NG a&\oyo fr. ‘unreasoning’ through ‘animal’, 3.41), ‘deer’ (NE deer, 3.75), ‘louse’ (NI. miol, 3.11). ‘Cattle’ in the wide sense (‘livestock’) may be partly or wholly specialized to ‘cattle’ in the nar- row sense, the bovine species (many ex- amples in 3.15, 3.20), or to ‘sheep’ (Att. mpoBarov, It. pecora, 3.15, 3.25).
3816:Ir. mil (used mostly of small animals, or as second member of epds. in animal names; NIr. miol ‘louse’), W., Br. mil : Grk. yfhov mostly ‘sheep’ or ‘goat’ (3.15). Walde-P. 2.296. Pedersen 1.50.
4396:4. Fr. cochon ‘hog’, Sp. cochino ‘hog’, cochina ‘sow’, cochinillo ‘pig’, in OFr. ‘pig’, dial. forms ‘wood louse’, prob. con- nected with late Lat. cutiones ‘wood lice’, with the frequently observed rela- tion between the names of such animals and words for ‘pig’, ‘sow’, etc., as in Lat. porcellio ‘wood louse’, NE sow, sow bug, hog louse, but ultimate source dub. (fr. a calling cry?). Gamillscheg 233. REW 4745. Bloch 1.157.
19399:5. Lith. zeskoti : ChSl., SCr. iskati, Boh. (old) jiskati (Pol. iskaé old ‘seek’, now ‘hunt lice, louse’), Russ. iskat’, Skt. is- ‘seek, wish’ (esp. with anu- ‘seek after’), Av. 7&- ‘seek’, OHG eiscon ‘in- quire, ask, demand’, OF dscian ‘at- tempt, demand, ask’, etc. (18.31). Walde-P. 1.12. Berneker 432 f.
20604:Boh. zisk, Pol. zysk, fr. ziskatt, ayskaé ‘gain’, epds. of z- and Boh. (old) jtskatt, Pol. iskaé ‘seek’ (old, now ‘louse’), ChSl.
27383:Br. lows, same word as louz, MBr. louge ‘badger’, fr. (or conversely) Fr. dial. louse ‘badger’ and ‘trickery’, etc., hence orig. an opprobrious term. Er- nault, RC 14.287, Glossaire 377.
```


## [2026-09-05T20:33:04.672Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls | tail -30; echo \"=== sample ===\"; python3 -c \"\nimport json;d=json.load(open('page-158.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:1800]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2000])\n\" 2>&1 | head -60",
 "description": "Check page-158 sample"
}
```


### [2026-09-05T20:33:06.304Z] TOOL RESULT

```
page-72.json
page-73.json
page-74.json
page-75.json
page-76.json
page-77.json
page-78.json
page-79.json
page-80.json
page-81.json
page-82.json
page-83.json
page-84.json
page-85.json
page-86.json
page-87.json
page-88.json
page-89.json
page-90.json
page-91.json
page-92.json
page-93.json
page-94.json
page-95.json
page-96.json
page-97.json
page-98.json
page-99.json
process
sources
=== sample ===
Traceback (most recent call last):
  File "<string>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'page-158.json'
```


## [2026-09-05T20:33:10.593Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls page-1*.json | sort -t- -k2 -n | tail -12; echo \"=== sample from page-157 or 156 ===\"; f=$(ls page-15*.json 2>/dev/null | head -1); echo $f; python3 -c \"\nimport json,sys;d=json.load(open('page-127.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2000]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\"",
 "description": "Sample existing verification entry"
}
```


### [2026-09-05T20:33:12.392Z] TOOL RESULT

```
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
=== sample from page-157 or 156 ===
(eval):1: no matches found: page-15*.json

{
 "entry": 0,
 "root": "Dhem",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
 "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
 "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst',
{
 "id": 1,
 "lang": "Avestan",
 "words": "dam; da-dhmainya",
 "verdict": "plausible",
 "derivation": "The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, -blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit Inl.-Red.' and compares directly with 'ai. dhámati \"er bläst\", np. damīdan \"blasen\"'. Nourai's 'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam' is the root abstracted from that participle, i.e. Proto-Iranian *damH- 'to blow, breathe; to swell' (Cheung 2007 s.v. *damH³), which is real and is the ancestor of the Persian words in node 2; it is simply not an Avestan word-form. Hence plausible rather than confirmed: right root, misdescribed gloss, and one of the two 'words' is a root citation.",
 "derivation_fa": "در اوستا هیچ فعلِ صرف‌شدهٔ dam- «دمیدن» به‌جا نمانده است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۷۳۱ به بعد) تنها اسمِ فاعلِ جوان‌اوستاییِ daδmainiia- «باد کرده، خود را باد کننده» را می‌آورد که دربارهٔ قورباغه‌ها به کار رفته (وندیداد ۱۴٫۵ و ۱۸٫۷۳) و آن را ستاکِ حالِ پسوندِ -ainya- با تکرارِ درونی می‌داند و مستقیماً با «dhámati سنسکریت» و «دمیدنِ فارسی» می‌سنجد. صورتِ «da-dhmainya» در کتاب نورایی همان واژه است (او ذالِ اوستایی را dh می‌نویسد و هجای تکرارِ da- را با خط تیره جدا می‌کند)، پس خوانشِ کتاب درست است؛ اما معنایی که به آن داده («من می‌دمم») نادرست است، چون این صورت صفت/اسمِ فاعل است نه فعلِ اول‌شخص. «dam» هم واژهٔ اوستایی نیست بلکه ریشهٔ ایرانیِ باستانِ *damH- «دمیدن، باد کردن» است (چونگ، ذیل *damH³). بنابراین ریشه درست است ولی معنا و صورت‌بندیِ گره با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "IEW 247 (POK_01.txt line 3517): 'av. daδmainya- ,sich aufblasend, blähend, von Fröschen''  — the same Avestan form under the same root."
  }
 ],
 "consulted": [
  {
   "src": "BRT",
   "where": "Altiran. Wb. 731 f., s.v. daδmainya- (BRT.txt line 13362)",
   "stance": "partial",
   "note": "'j. däSmainya- Adj. \"sich aufblasend, -blähend\", von Fröschen … Eig. PPA. … — Vgl. ai. dhámati \"
```


## [2026-09-05T20:33:16.365Z] TOOL CALL #27: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:33:16.373Z] TOOL RESULT

```


```


## [2026-09-05T20:33:21.172Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B4%DA%A9",
 "prompt": "Give the full Persian etymology section(s) for رشک — especially the sense 'nit, louse egg' (Etymology 2 or similar): the reconstructed Proto-Iranian / Proto-Indo-Iranian form, Sanskrit cognate likṣā, Middle Persian form, and any cited references. Also the 'envy' sense etymology."
}
```


## [2026-09-05T20:33:21.444Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ricin",
 "prompt": "Give the etymology of 'ricin' and of 'ricinus'/castor oil plant verbatim."
}
```


### [2026-09-05T20:33:27.741Z] TOOL RESULT

```
# Persian Etymology for رشک (rašk/rišk)

## Sense 1: "Envy"

**Etymology 1** traces to Middle Persian (arešk/rešk, "envy"), ultimately from Proto-Indo-Iranian *Harš- ("envy"). The source notes this may derive from Avestan araska- ("envy"), with roots in Proto-Indo-European *h₁ers-. Cognates include Sanskrit īrṣyati ("to envy") and Old English irsian ("to be angry").

## Sense 2: "Nit" (Louse Egg)

**Etymology 2** connects to Sanskrit likṣā ("nit"). The Wiktionary entry explicitly states: "This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term."

The entry notes a problematic comparison with Latin ricinus (in the tick sense), but acknowledges further etymological connections require additional sourcing. No reconstructed Proto-Iranian or Proto-Indo-Iranian form is provided for this sense—the entry requests that the etymology be sourced.

The entry lacks detailed references for the "nit" sense beyond the Sanskrit cognate.
```


### [2026-09-05T20:33:28.110Z] TOOL RESULT

```
# Etymology of Ricin and Ricinus

**Ricin (noun):**
"poison obtained from the castor-oil bean, 1888, from *ricinus*, genus name of the castor-oil plant"

**Ricinus (castor-oil plant):**
The genus name *ricinus* dates to 1694 and comes "from Latin *ricinus* (Pliny), a word of uncertain origin, perhaps the same word as *ricinus* 'tick' (in sheep, dogs, etc.)." The source notes that "Latin *ricinum* was used in late Old English herbariums."

In summary: the English term *ricin* emerged in 1888 from the Latin genus name *ricinus*, whose origins remain unclear but may derive from the Latin word for "tick."
```


## [2026-09-05T20:33:36.316Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE",
 "prompt": "Give the Sanskrit entry लिक्षा (likṣā): meaning, etymology (including any note on likhati, Proto-Indo-European, Mayrhofer), and descendants/cognates listed."
}
```


## [2026-09-05T20:33:37.889Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ricinus",
 "prompt": "Give the Latin entry ricinus: meanings and etymology, any note on relation to Proto-Indo-European or to erek-, and whether the plant sense is treated as the same or a different word."
}
```


### [2026-09-05T20:33:43.228Z] TOOL RESULT

```
# Sanskrit Entry: लिक्षा (likṣā)

**Meaning:**
A "nit" (the egg of a louse), according to the Wiktionary entry.

**Etymology:**
The word is "Cognate with Persian رشک (rešk)." The entry notes that comparisons with Sanskrit रक्षस् (rákṣas, "harm") and other Indo-European words for "nit; mite, tick" are problematic. The etymology section indicates the entry requires expansion.

**Notable Etymology Reference:**
Mayrhofer's *Etymologisches Wörterbuch des Altindoarischen* (2001) addresses this term on page 443, though the entry does not elaborate on likhati or specific Proto-Indo-European roots.

**Descendants and Cognates:**
The word produced descendants across multiple Indo-Aryan languages:
- Bengali: निकी (niki)
- Hindi: लीख (līkh)
- Gujarati: લીખ (līkh)
- Marathi: लीख (līkh)
- Urdu: لِیکھ (līkh)
```


### [2026-09-05T20:33:45.153Z] TOOL RESULT

```
# Latin Entry: Ricinus

## Meanings
The Latin term *ricinus* has three distinct senses:
1. A tick (arachnid)
2. The castor oil plant (*Ricinus communis*) and its seeds
3. Mulberry seeds

## Etymology
The origin is uncertain. The entry states: "Unknown; possibly a substrate word." Scholars have compared it to words meaning "nit" or "tick" across various languages including Albanian, Lithuanian, Latvian, Sanskrit, and Persian, though these cannot be regularly derived from a common Proto-Indo-European source.

## Proto-Indo-European Connection
A hypothetical pre-form "*HreK-(e)r ~ *Hrek-en-*" is proposed for Latin, assuming post-PIE thematicization, but "the root would remain unidentified." No established connection to Proto-Indo-European is documented.

## Plant vs. Tick Senses
The Wiktionary entry treats these as separate definitions within a single lemma rather than distinct etymological words. The descendants section shows that Romance languages developed the plant sense (castor) separately from the tick sense, suggesting semantic divergence over time rather than two originally different words.
```


## [2026-09-05T20:34:00.550Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== POK_01 p335 (leaf 343) ==\"; awk 'BEGIN{RS=\"\\f\"} NR==344' POK_01.txt | grep -n -i \"erek\\|Laus\\|Milbe\\|ricinus\\|liks\" | head -20; echo; echo \"-- grep erek in POK_01 --\"; grep -n \"erek-\\|Milbe\" POK_01.txt | sed -n '1,25p'",
 "description": "Pokorny German original p.335"
}
```


### [2026-09-05T20:34:02.559Z] TOOL RESULT

```
== POK_01 p335 (leaf 343) ==

-- grep erek in POK_01 --
1925:^t  eil   B  verne,  A  |?arno  ^leuchtend^,   davon  B  perwe,   A  -paräm  ,Würde^ Erweiterungen   unseres   hher-  scheinen   hhereg-,   bherek-  .glänzend    Vgl. ferner  L  bhel-  mit  ähnlicher  Bedeutung.
1977:Ahd.   'brecht  kann;   wenn  diese  Vokalisierung  statt  'her(h)t   nicht   ei^ Neuerung   ist,   auch   auf   hherek-  bezogen  werden,   wie   an    sich  auch  gof lairJits,  cymr.  herth,  hitt.  parkuis.    Die  Gruppen  hhereg-,  hherek-  scheine Erweiterungen  zu  hher-  _,hell;  braun^  zu  sein.   Ähnliche  Erweiterung  hheU neben  hhel-  ^glänzen^
3010:derek- :
5005:j.  erek'  (er[e]g-i2-)  ,Laus,  Milbe^  oft  tabuierend  entstellt.
5007:lat.  ricinus  1.  ,ein  sich  in  die  Haut  von  Schafen,  Hunden  oder  Rind- vieh einbohrendes  Ungeziefer,  Zecke'  (unsicher  ist  die  Zugehörigkeit  von 2.  ,eine  Strauchart,  Ricinus  communis')  kann  auf  älteres  *recinos  zurück- gehen und  mit  lit.  erke  , Zecke,  Schaflaus'  (*erkia),  lett.  erce  , Kuhmilbe, böse  Person'  unter  idg.  *erek-  zusammengehören.  Weiterhin  ist  zu  ver- gleichen arm.  o{r)jil  ,Nisse,  Lausei'  (hier  scheint  eine  Wurzelvariante er{e)gh-  vorzuliegen,  wie  auch  in  der  folgenden  alb.  Form)  und  orJciun ,ringworm,  itching,  erysipelas'  (aus  *orqiiöno-  (?)  mit  einem  -rzo-Suffix  wie im  Lat.  nach  Petersson  KZ.  47,  263  f.),  alb.  ergjiz  ,kleine  Laus'  (s.  ü.  Meyer Alb.  Wb.  96;  Zweifel  bei  Hermann  KZ.  41,  48;  doch  kann  der  abweichende Guttural  im  Armen,   und  Alban.   auf   tabuierender   Entstellung    beruhen).
```


## [2026-09-05T20:34:02.792Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD risk ==\"; grep -n -i \"\\brisk\\b\\|rišk\\|nit\\b\" PHD_mackenzie.txt | head -15; echo \"== NYB ==\"; grep -n -i \"risk\" NYB_vol2_glossary.txt | head -10; echo \"== ARY latin index ==\"; grep -n -i \"RESK\\|RISK\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"== ARY fa ==\"; grep -n \"رشک\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "MacKenzie, Nyberg, Aryanpur"
}
```


### [2026-09-05T20:34:02.900Z] TOOL RESULT

```
== PHD risk ==
1105:angust pngwst l I (N angust)] finger, toe; unit of length (1 in.). \ , ~
1119: -- xwardan: risk death, fight to the death.
4886: ltag [t)k I N ta] item, unit; alone, single.
6327: cultivated abadan; ....., land warzbum.      deserving""" margarzan; risk "'.
7887:unit tiig.                               vanguard pesobiiy.
== NYB ==
1100:cāpūk [c'pwk'], comp. ~-tar, quick, brisk 8%; busy, active 178. — NP cābuk. cāpūkēh quickness of wit, nimble wit 223, 42, 141°. 1518,
3391:sapük [spwk'] light, brisk; unsteady, shallow, comp. ~-tar 90%, — < OP *capu-ka- < Olr *0rapu-ka-, from IE *trep-, Gr retro ‘to turn’, Lat trepidus
3430:hypothesis that we have to do with OP *oi- — NW (Av. 1645) sri- (Bthl srāy-) "beauty, splendour’ = Kkr sri- ‘splendour, majesty’, also personified as the goddess of beauty, of fortune, or of sovereign power; Milr *si(y) alternates freely with sih according to the common rule. This divine power is apparently miaterialized in some animal which is said to be very stout (71%), the most beautiful imaginable (718-18), very big and brisk (87%). In the Sn, where the episode is told at length (Book 21, v. 231 sqq., Tehr 4, p. 1697- 98 — Mohl V, p. 288), it is said to bea ram (yurm), but deseribed as a guite mythical, mysterious being: “I have not seen its equal painted in any palace”, one of the witnesses says, “with wings as Simurgh, with a tail as the peacock, like a flash of lightning, bold of head and ears and hoofs, purple-coloured, swift as the wind, in its way it does not remind of a ram at all". The conjecture varrak, adopted by Nöldeke and Antiä, robs the narration of the air of divine mystery essential to it. Sanjana’s remarks are worthless. — OP *ei- is also attested in NP séy ‘beautiful, elegant, excellent’ < MiPrs *sēk < OP *cayaka- for NW *srayaka- from Av. (1638 sg.) srayan- ‘beauty’ and ‘beautiful’; in a pejorative sense in NP sihah ‘harlot’ < MiPrs *sthak; possibly also in NP siyäb, whose meaning is, however, somewhat uncertain (v. Steingass and BQ). — It is not all too difficult to guess why the scribe chose such a strange way of writing this w.: by spelling it phonetically he would have got a very ambiguous and polyphonic graphic symbol. His spelling 30 guaran- teed safe reading. Certainly this is be- wildering for us who read with our eyes, but in antiquity all texts were intended to be perceived by ear. Cf also s. v. nist.
3510:srišk [slyšk'; slšk'] drop 211. 412°, 8920, — Av. (1645) sraska- 'tear'; MPrth srsk (List 87); NP sirisk.
5003:araska-: arisk
6698:korisk: kurusk
== ARY latin index ==
3357:BRESK (SLOVENIAN) gy hal (OLD SCANDINAVIAN) S,5the\
9086:RADIX LATIN) 3) RESK OLD PERSIAN) lool, gu
== ARY fa ==
2552:ا ۲ ۲ اشکه ارس» سرشک
10519:۵۶ ) سرشک (به چم "شک چشم » "قطره"
14176:چم این واژه درُزبان لوق وزوان‌های ژرمنی این فهرست: (گیاه) ترشکت؛ ریواس.
15166:۱ چم این واژه در زبان‌های ژرمنی: حمد» رشکه» جنگ و خصومت.
```


## [2026-09-05T20:34:13.133Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5000,5012p' POK_01.txt; echo \"== leaf of line 5005 ==\"; awk 'NR<=5005{n+=gsub(/\\f/,\"\")} END{print n}' POK_01.txt",
 "description": "Pokorny German erek entry full"
}
```


## [2026-09-05T20:34:14.792Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9080,9092p' incoming/ARY/ARY_latin_index_pages.txt; echo \"== which pdf page ==\"; awk 'NR<=9086 && /\\[pdf page/ {p=$0} END{print p}' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "ARY latin index RESK context"
}
```


### [2026-09-05T20:34:15.033Z] TOOL RESULT

```
lat.  ervum  n.  ,eine  Hülsenfrucht^  (aus  *eroiwm,  '^eregu(h)om  oder *erogi^{h)om)]
ahd.  araweiz,  ariciz,  nhd.  Erhse,  as.  er(iw)it,  rand.  erwete,  ndd.  erwten PL,  anord.  ertr  f.  PL  (Dat.  ertrum)  ds.  (-ait  wohl  bloßes  Suffix);
aber  mir.  orbaind  ,grains^  steht  für  ^ärbainn,  älter  arbanna  (oben  S.  63).
Wahrscheinlich  Entlehnungen  aus  einer  gemeinsamen,  wohl  ostmedi- terranen Quelle,  aus  der  auch  ai.  aravindam  , Lotosblume'  stammt.
WP.  I  145,  WH.  I  41 9 f.,. 863.
j.  erek'  (er[e]g-i2-)  ,Laus,  Milbe^  oft  tabuierend  entstellt.
Ai.  lik^ä  ,Nisse,  Lausei'  (wohl  aus  *laksd  durch  Einfluß  von  likhdti ,ritzt') ;
lat.  ricinus  1.  ,ein  sich  in  die  Haut  von  Schafen,  Hunden  oder  Rind- vieh einbohrendes  Ungeziefer,  Zecke'  (unsicher  ist  die  Zugehörigkeit  von 2.  ,eine  Strauchart,  Ricinus  communis')  kann  auf  älteres  *recinos  zurück- gehen und  mit  lit.  erke  , Zecke,  Schaflaus'  (*erkia),  lett.  erce  , Kuhmilbe, böse  Person'  unter  idg.  *erek-  zusammengehören.  Weiterhin  ist  zu  ver- gleichen arm.  o{r)jil  ,Nisse,  Lausei'  (hier  scheint  eine  Wurzelvariante er{e)gh-  vorzuliegen,  wie  auch  in  der  folgenden  alb.  Form)  und  orJciun ,ringworm,  itching,  erysipelas'  (aus  *orqiiöno-  (?)  mit  einem  -rzo-Suffix  wie im  Lat.  nach  Petersson  KZ.  47,  263  f.),  alb.  ergjiz  ,kleine  Laus'  (s.  ü.  Meyer Alb.  Wb.  96;  Zweifel  bei  Hermann  KZ.  41,  48;  doch  kann  der  abweichende Guttural  im  Armen,   und  Alban.   auf   tabuierender   Entstellung    beruhen).
WP.  I  145,  n  344.
2.  er(e)k',  rek-,  rok-  ,auf reißen,  spalten,  schinden'.
Ai.  rknd-h  ,geschunden,  kahlgerieben',  r^sdh  ,kahl',  rksara-h  ,Spitze, Dorn';
lit.  j-erkä,  pra-j-erkä  ,Schlitz';  (über  lett.  ercis  ,Wacholder'  usw.  s.  oben S.  67  f.) ;  mit  anderer  Ablautstufe  lit.  ranküj  räkti  ,aufstochern',  rakUis , Splitter,  Dorn',  usw.
Persson  Beitr.  839.   Dazu  .gehört  auch :
== leaf of line 5005 ==
348
```


### [2026-09-05T20:34:16.690Z] TOOL RESULT

```
Seetloot
soy efi
|
as
ae
RHIZA, GREEK) gt» VARESHAJI —({W)(AVESTAN) oleh
RADIX LATIN) 3) RESK OLD PERSIAN) lool, gu
RACINE (FRENCH) 403! 5 RESHAG, RESHAK (PAHLAVI) 6 shy
RaIs SPANISH) glia! RIXL, REXE HOSSETIC) in \
RADISE HUTALIAN) go RA, REH (KURDISH) 536
RADACINA -(RUMANIAN) lay RISHA AFGHAN) ( gu) gail
[pdf page 315]
. Oayh ahh / VF
== which pdf page ==
[pdf page 314]
```


## [2026-09-05T20:34:37.173Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSD3 ricin ==\"; sed -n '239770,239790p' FSD_vol3.txt; echo \"== ARY shepesh ==\"; grep -n \"شپش\\|لیکه\" incoming/ARY/ARY_pages.txt | head; echo \"== KLN ricin toxin ==\"; grep -n \"ricin\\b\" KLN_1966.txt | head",
 "description": "Funk&Wagnalls ricin, ARY, Klein"
}
```


### [2026-09-05T20:34:37.281Z] TOOL RESULT

```
== FSD3 ricin ==
In-o-le'lc* a Chim Of, pertaining to, or derived from the
eusior-oU plant rlc'7n-ol'lc;. — rlrlnolcic acid, a pale
yellow oily compound (CisIImOi) obtained by tho saponifica-
tion of either castor- or Jutropha-ell — rlr''ln-o'lc-ln, n.
Same os ricinklaidin rlr'ln-o'le-ine;.— rlc'ln-ol'lc* a,
Chem Same as ricinoleic
Rlr^l-nu'lc-l* 1 ris'i-nia'li-ol, 2 rlc'l-na'le>i, n pi. Aradi,
A suborder of oplllonlne arachnids without supramaxlllory
lumlnw and with 2-jolnted mandibles 1 < L ricinus, a
tick I— rlr''l-nu'lc-an, a A n
Rlr'l-nU8, 1 ris'i-nus, 2 riv'i-nfis, n Rot. A monotvpio
genus of tall annual plants of the spurge family (rJu-
E horhiaeex). Ricinus communis, the castor-oil plant*
as palmate leaves and muuaM'ious flowers There are
several varieties [ < L ricinus, castor-oil plant ]
rIrkU 1 nk, 2 rik, of. To heap up in neks, as hay.
rick** 0 Hame as wrick
rick'* n 1. A stack, espcciallv a stack of hay or of
sheaves of gram having the top rounded and thatched
tn protf'ct the interior from rain. 2. A small rounded
pile of hay made in the field so as to kf*ep dry and be
== ARY shepesh ==
300:گزمسیری می‌بود در حالیکه تفریباً همه‌ی واژه‌های گرمسیری و استوایی از ریشه‌ی هند و اروپایی
3717:لاتین (7100هل): 0۸ گالیکه (للتله0): 0
8235:0 ,۳۸1118۷۷۸ گالیکه (عللقهه): اد(
9033:شک (به چم "*تخم شپش!") / ۳۰۷
9703:گالیکه (0۸81]70): ند 3 (۸778) ۸400
13555:3 گالیکه (حللتظده): 3
14214:دانمارکی (0۸//510): ان گالیکه (0/اظ0۸): 3
== KLN ricin toxin ==
```


## [2026-09-05T20:34:43.946Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9015,9050p' incoming/ARY/ARY_pages.txt; echo \"== pdf page tag ==\"; awk 'NR<=9033 && /\\[pdf page/ {p=$0;n=NR} END{print p, n}' incoming/ARY/ARY_pages.txt",
 "description": "ARY context for rešk"
}
```


### [2026-09-05T20:34:45.844Z] TOOL RESULT

```
آرمنی (44501424): ادنید ۱ ۸
یادداشت:
ا چم این واژه در زبان لاتین؛ بلند شدن؛ بالا رتن. ۱
اوستایی (۸8874۷): بشاکشان۸ ساکسونی کهن (542:0۸0 00): 11
شکاهشال۸ ,188192 ,۸۸0877۸0۷1 آلمانی کهن (087420 04اب صام):
پهلوی (1/ انم ۴۸۹۲1 ,۸۸۳5136 انگلیسی کهن (لفلا200 صزم. ‏ هر
بلوچی (اتللانلم8): ت1قف بکاتاگته۸ لیتوانی (7ل۵ا/لولا 7 7): 58
تخاری ۸ (۸ ۸(4ل۸2تل707): ۸35۸ هتیت (7777178): ۸5۸3۷19۸ ,۸۹8۸۸*
نخاری 8(8 ۷فلمتل5م۲0. آم2فهمه
سانسکریت (5(75817): ,1۸۸7 پسگشت‌ها شک رد
7 185 ,1889۸71 1
آرمنی (71401ل۸(/5): 1 0 (8۸3015[) :۸۸02258
بونانی 076870): ,۸07 زر اه ۱۱ لاه
لاتین (۸71۸)«شاید) 18۸ برهان قاطع + ۲ و ۱۰۵
یادداشت, 1
چم این واژه در زبان‌های ژرمنی و زبان لاتین : خشمگین» خشم.
چم این واژه در زبان‌های تخاری: مار کِرم.
[pdf page 306]
شک (به چم "*تخم شپش!") / ۳۰۷
۱ ۱
چم‌اگایس سوای تارسن ا ک0
پارسی باستان (۳۶۶۵4 ۰:01 818136۸* لاتین (7100ل): 5
ارستی (055770). 156۸
کردی (7ل6/8/0/3): انیا پسگشت‌ها 5
بلوچی (زنت‌ناتفه: ۰ 8۸۹8۴ بکللاگاه 0
افغانی (پشتی) (/4/0/۸/۷): ۰ خا(اه ,816۸ برهان قاطع : ۱ از
سانسکریت (54۸/58/7): 13871۸ به1168
سانسکریت (54۸۷87/7): 5تالتهط بلفاری (/(۸ ال 8): 020۸
لاتین (7107مل): 75 لیترانی (420ا(ونا 382017:74 ,332077 ۱
فریزی کهن (/514ل87 00): ایا تونی (لني) (771424):
آلمانی میانه (020/401 04 ة04/00): : 7 ,88271018
5 ,3115615 :
آلمانی (0584۸0): انیا پسگشت‌ها نتب درد
انگلیسی کهن (2001/57 010): 0
8896 ,8886 6 (۸8) نمی ات تن
انگلیسی (تلدالاه/52): نان 778 :00/5
== pdf page tag ==
[pdf page 306] 9032
```


## [2026-09-05T20:35:00.396Z] TOOL CALL #38: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%D8%B4%DA%A9' --note 'page 159, root Erek, Persian رشک rešk: Wiktionary Etymology 2 (nit) cognate with Sanskrit likṣā; Etymology 1 (envy) separate' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE' --note 'page 159, root Erek, Sanskrit likṣā nit: cognate with Persian rešk; Mayrhofer EWAia 2001:443' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ricinus' --note 'page 159, root Erek, Latin ricinus tick/castor-oil plant: unknown, possibly substrate; *HreK-(e)r ~ *Hrek-en-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/ricin' --note 'page 159, root Erek, English ricin 1888 from genus Ricinus' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:35:03.530Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/92602be820b8706a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/40ed141fa55df120.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/72335a622d500c75.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ad801c210e0f882d.txt
```


## [2026-09-05T20:35:08.876Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"رشک\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; echo \"---\"; grep -n \"رشک\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -8",
 "description": "Grep Mo'in for rešk"
}
```


### [2026-09-05T20:35:08.955Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v2_djvu.txt:38
MON_part2.txt:38
incoming/MON/MON_2vol_Adena_v1_djvu.txt:66
MON_part1.txt:66
---
1161:سرشک. 
1720:محلی که در آن آب معدنی باشد. سرشکد؛ 
2130:۱ سین ۶۰۳ اسید کرشکک» 9۸۹۴ 
3668:پشه غال» پشه خار» سارخکدار» سارشکدار. 
7105:اثرار: هه [ع. بادیه ] ((.) (گیا.) زرشکک. 
8738:اخلال در امری: کارشکنی. 
10025:ارشک؛: (.) رشکد» عبرت. حسد» 
10028:ارشکین: 98070 [- رشکین] (ص‌نسب.)
```


## [2026-09-05T20:35:11.527Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"رشک\" MON_part2.txt | head -25",
 "description": "Mo'in part2 rešk hits"
}
```


### [2026-09-05T20:35:11.586Z] TOOL RESULT

```
618:زوال آن از او خواهد؛ بژهان بردن. رشکث 
1326:ورشکسته‌ای رابهنسبت طلب ین خود. 
2116:کینه گردیدن. رشکك بردن» حسد داشتن. 
2157:برنج و چاودار و جو ترشک و غیره. 
3815:رشک بسردن. (امص.) حسمیت. 
3816:ناموس پرستی. (.) رشک. (تسص.) حمیت 
3825:مایة رشکك. جنبیدن غیرت کسی: به غیرت 
3916:بارشکك». سبار غبرت دارنده. ( کذ.) (تص.) 
4797:اسب کشیده شود. درشکه. 
6306:فرشک: (۱.) سید ۳ "۳ 
12114:مستحفظ, پاسدار. میررشکاری که صید را از 
17815:کارشکن: ۲.307 [- کارشکننده ] (ص‌نا.) 
17817:کارشکنی کند. . سخن چین» ساعی» نمام. 
17853:کارشکن 
21678:(انیدرید کرشک) و در لجن مرداب‌ها 
21695:کرشک بو جود می آید: ۲۷۲ ۲+ و 
22586:کروک: ۲۳05 [رس.] (.) سقف درشکه و 
26419:کسمرشکن: «۲.30۷ [- ک مرشکننده] 
30103:سرشکک گذاره. 
32183:کربستن؛ مق. خنده. (ا.) اشکث» سرشکث؛ 
38424:دوشیزة بی‌عیب. (کد.) اشک. سرشک. 
39132:سر چوب تر بر آتش ریزد؛ سرشک اتش. 
49558:محسود: ۵۸5۳۵ (ع.] (امف.) رشک برده 
58064:(مانند درشکه‌چی و مهتر و داسیز شک و 
61502:غطه برند؛ رشک برده. (ص.) خوشخت»
```


## [2026-09-05T20:35:17.254Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"تخم شپش\\|تخم شپشل\\|شپش\" MON_part1.txt MON_part2.txt | head -15",
 "description": "Mo'in tokhm-e shepesh"
}
```


### [2026-09-05T20:35:17.316Z] TOOL RESULT

```
MON_part2.txt:14853:قمل: لسهر(ع.] (.) (جاد.) شپش 
MON_part2.txt:33723:کردن شپش بکار می‌برند؛ سنبل ختایی 
MON_part2.txt:47348:شپشکك گندم. 
MON_part1.txt:45663:به وسیلةً شپش سرایت کند و چون علایم 
MON_part1.txt:54858:مخصوصی که از گزیدن شپش يا کبک یا 
MON_part1.txt:84199:و تیفوس و غیره می‌باشد. شپش انکل انسان 
MON_part1.txt:84212:دگردیسی است. در انسان دو نوع شپش 
MON_part1.txt:84217:است و دیگری شپش 
MON_part1.txt:84219:لباس خارج می‌شود. تخم هر دو گونه شپش
```


## [2026-09-05T20:35:41.067Z] TOOL CALL #42: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null | head; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK 2>/dev/null | head",
 "description": "Check ocr/BOOK dir"
}
```


### [2026-09-05T20:35:41.118Z] TOOL RESULT

```
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
100.png
101.png
102.png
103.png
104.png
105.png
106.png
108.png
109.png
110.png
```


## [2026-09-05T20:35:45.582Z] TOOL CALL #43: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; cp $S/pg159.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/159.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/159.png; sed -n '1,60p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Copy page image and inspect checker"
}
```


### [2026-09-05T20:35:45.647Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 27814 Sep  5 16:35 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/159.png
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
```


## [2026-09-05T20:35:56.932Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nfor f,target in [('WLD_Bd1_pages.txt','recinos'),('WLD_Bd2_pages.txt','ricinus')]:\n    txt=open(f,encoding='utf-8',errors='replace').read()\n    pages=txt.split('\\f')\n    for i,p in enumerate(pages):\n        if target in p or 'liksd' in p and f.endswith('Bd2_pages.txt') and 'Nisse' in p:\n            tag=re.search(r'\\[pdf page (\\d+)\\]',p)\n            print(f,i,tag.group(0) if tag else None, p[:120].replace('\\n',' | ')[:120])\n            break\nEOF\necho \"--- Bd2 context ---\"; sed -n '22390,22405p' WLD_Bd2_1927_dli_106624_djvu.txt",
 "description": "Locate WLD pages"
}
```


### [2026-09-05T20:35:58.907Z] TOOL RESULT

```
WLD_Bd2_pages.txt 348 None 344                                                   rei- |  |  |  | schreiben"       Sommer Hdb.^ 231, Boisacq 274 Anm
--- Bd2 context ---
MuBarbeit). 

Vgl. Froebde KZ. 22,264, Pick I* 115, 525, Zupitza Gutt. 67f, (Lit.), 
Pick III* 343, Persson Wzerw. 12, 103, 161, 234, Beitr. 839 f. Letzterer 
will ai. liksd ,,Nisse, Lausei“, lat. ricinus „eiri sicb in die Haut von Scbafen, 
Hunden und Eindvieh einbobrendes Ungeziefer, Zecke ; ein Straucb“ (kann 
aber auch fiir *recinos stebn) ebenso zu unserem reik-- stellen, wie lit. 
erke „Schaflaus, Holzbock“, lett. erze „Kubmilbe“ (vielleicht aucb lat. rici- 
nus, 8. o.) znr nach ihm verwandten Wz. "^ere-k- (als dritte Yariante 
*er(e)gh- reibt sicb arm. o(r)jil „Nisse, Lausei^^, alb. ergis, -zi „kleine Laus‘* 
an); s. uber diese von Bugge vereinigten Worte die Zweifel Hermanns KZ. 
41, 48, und Yf. LEWb.^ u. ricinus\ liksd -Aikhdti scheint klar, kann aber 
auch Ergebnis nachtraglicher Angleichung etwa eines *rk-s-d an likkdti sein. 

Ahnlich "^reik- in ai. riqdt% ligdii „rupft, reiBt ab, weidet ab“ (npers. 
ristan „spmnen“, bal. resag, resay „spinnen, flechten“ Uhlenbeck Ai. Wb.
```


## [2026-09-05T20:36:10.487Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\ntxt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if 'ccinos' in p or ('Schaflaus' in p and 'erfe' in p):\n        print(\"block\",i, p[:200].replace('\\n',' | '))\n        j=p.find('ccinos'); print('...',p[max(0,j-600):j+900])\n        break\nEOF",
 "description": "WLD Bd1 page for erek"
}
```


### [2026-09-05T20:36:12.262Z] TOOL RESULT

```
block 153                                                                                   ;                                                           : |  |  |  |  |                                                     
... rer, Sattiger t*gara.zdjan-). Fick I 530, II 235, IIL 34»' }
341, Falk-Tovp u. ransage, vast.
  Ygl. *rem-.                   das wie res-                wohl auch yon Persson Wzerw. 70, 241                                            mit
(e)re- zusammengefaBt wird.


erek- „Laus, Milbe“ (er(e)gh-).
  Lat. ricinus „ein sick in die Haut von Schafen, Hunden oder Rindvieh
einbohrendes Ungeziefer, Zecke ; eine Strauehart (Ricinus communis) kann
                                                                                                                                       11




auf alteres *rccinos zuriickgehen und mit lit. erfe „Zecke, Schaflaus {*erl i r>),
lett. tree „Kuhmilbe“ unter idg. *ereJc- zusammengehoren (vgl. Vanicek 239).
Weiterhin ist zu vergleichen arm. o(r)d:il „Nisse, Lausei“ (hier scheint
eine Wzvariante er(e)gh- vorzuliegen, wie auch in der folgenden alb.
                                                                                                         11
Form) und orkiun „ringworm. itching, erysipelas (aus *rcqiidno- (?) mit
einem -«o-Suffix wie im Lat. nach Petersson KZ. 47, 263f.), alb. ergiz
‘.kleine Laus
                           11
                 (s. Bugge, Beitr. z. etym. Erlaut. d. arm. Spr. S. 17. G. Meyer
Alb. Wb. 96; doch Hermann KZ. 41, 48).
   Wegen ai. liksd „H7isse, Lausei (vgl. Fick 1 4 364, Vanicek 239, Bugge   11




aaO.) miiSte daneben ein idg. *ereik- angesetzt werden, welches evident
zu idg. *reilc(li)- „ritzen“ zu stellen is
```


## [2026-09-05T20:36:56.218Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:41:52.492Z] TOOL CALL #46: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-159.json <<'JSONEOF'\n{\n  \"pdf_page\": 159,\n  \"book_page\": 129,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Erek\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Pokorny IEW 335 '1. erek- (er(e)ĝ-) ‚Laus, Milbe‘' = 'louse, mite'; modern handbooks (de Vaan / Wiktionary on ricinus, Mayrhofer on likṣā) doubt that a regular PIE root can be set up for this group at all\",\n      \"note\": \"The root box is a faithful copy of a real Pokorny lemma. POK_01.txt (line 5005) prints, on p. 335, '1. erek- (er[e]g-ĵ-) ‚Laus, Milbe‘ oft tabuierend entstellt', i.e. 'louse, mite, often distorted by taboo', with exactly the two derivatives Nourai draws — 'Ai. likṣā́ ‚Nisse, Lausei‘' and 'lat. ricinus'. Two reservations. (1) The gloss: Pokorny's Laus is 'louse', not 'flea'; 'mite' (Milbe) is right. The louse/flea confusion runs through the whole chart (nodes 1, 2 and 3 all say 'flea' where the sources say louse/nit/tick), and it matters, because a nit (تخم شپش) is a louse egg, never a flea egg. (2) The reconstruction: Pokorny himself hedges every link (Latin ricinus 'kann ... zusammengehören', the Armenian and Albanian gutturals only work 'auf tabuierender Entstellung'), Walde-Pokorny I 145 says that Sanskrit likṣā́ would require a separate root *ereik- and WP II 344 files the same two words under *reik- 'ritzen' instead, and de Vaan (via Wiktionary's Latin ricinus) concludes 'Unknown; possibly a substrate word ... cannot be regularly derived from a common Proto-Indo-European source'. So the etymon is a real dictionary lemma and the words really do form a comparison set, but it is a taboo-distorted wander-/substrate word rather than a securely reconstructable root: plausible, not confirmed.\",\n      \"note_fa\": \"جعبهٔ ریشه برگردان درستی از مدخلی واقعی در پوکورنی است: در صفحهٔ ۳۳۵ فرهنگ او آمده «1. erek- (er[e]ǵ-) ‚Laus, Milbe‘ oft tabuierend entstellt» یعنی «شپش، کنه» که بسیار دستخوش تحریف تابویی شده است؛ همان دو مشتقی هم که نورایی رسم کرده (سنسکریت likṣā́ و لاتین ricinus) در همان جاست. دو ایراد هست: نخست آنکه Laus «شپش» است نه «کیک/پشه»، و این خطای معنایی (flea به جای louse) در همهٔ گره‌های این نمودار تکرار شده است؛ دوم آنکه خود پوکورنی در همهٔ پیوندها احتیاط می‌کند، والدهٔ‌پوکورنی (جلد ۱ ص ۱۴۵) برای صورت سنسکریت ریشهٔ جداگانهٔ *ereik- لازم می‌داند و در جلد ۲ ص ۳۴۴ همین واژه‌ها را زیر *reik- «خراشیدن» می‌آورد، و ریشه‌شناسی امروزی (دووان در فرهنگ ریشه‌شناختی لاتین) این دسته را واژهٔ زیرلایه‌ای/سرگردان می‌شمارد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/ricinus\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:335\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01.txt line 5005 (German original, IEW p.335): '1. erek' (er[e]g-ĵ-) ,Laus, Milbe‘ oft tabuierend entstellt.' followed by 'Ai. likṣā ,Nisse, Lausei‘ ... lat. ricinus ... kann auf älteres *recinos zurückgehen und mit lit. erke ,Zecke, Schaflaus‘ ... unter idg. *erek- zusammengehören'. Same text in the English rendering POK_full.txt line 27404 ff. Nourai's root name, language label and page are right; his gloss 'flea' renders Laus 'louse'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I 145 (incoming/WLD/WLD_Bd1_pages.txt block 153; djvu line 9415)\",\n          \"stance\": \"partial\",\n          \"note\": \"'erek- ‚Laus, Milbe‘ (er(e)gh-). Lat. ricinus ... kann auf älteres *recinos zurückgehen und mit lit. erke ‚Zecke, Schaflaus‘ ... unter idg. *erek- zusammengehören' — but then: 'Wegen ai. likṣā ‚Nisse, Lausei‘ ... müßte daneben ein idg. *ereik- angesetzt werden, welches evident zu idg. *reik(h)- ‚ritzen‘ zu stellen ist.' The root is there; the Sanskrit branch is explicitly said to need a different reconstruction.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II 344 (incoming/WLD/WLD_Bd2_pages.txt block 348; djvu lines 22394-22401)\",\n          \"stance\": \"contradicts\",\n          \"note\": \"Under *reik- 'rupfen, reißen': 'Letzterer [Persson] will ai. likṣā „Nisse, Lausei“, lat. ricinus ... ebenso zu unserem reik- stellen, wie lit. erke „Schaflaus“ ... s. über diese von Bugge vereinigten Worte die Zweifel Hermanns KZ. 41, 48'. Walde-Pokorny thus offers a rival root for the very words Nourai hangs on Erek.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"AHD_watkins1985.txt (grep -n -i 'erek|ricin|liksa' → only bherek- and unrelated hits)\",\n          \"stance\": \"silent\",\n          \"note\": \"Watkins' IE-roots appendix has no *erek- root and no English word tracing to it; its silence is not disagreement, only absence (no English reflex reaches it except the learned Latin borrowing Ricinus).\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, IEC.txt line 3668\",\n          \"stance\": \"partial\",\n          \"note\": \"'erk- (1) “tick, mite” Ir. earc ‘stinging insect, gadfly’; Li. erke ‘tick’; Latv. ērce, id.' — Mann keeps the root but lists only Celtic and Baltic; he does not admit Sanskrit likṣā or Latin ricinus to it.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck, SYN.txt (grep -i 'louse', 'nit')\",\n          \"stance\": \"silent\",\n          \"note\": \"Buck has no 'louse'/'nit' article (only passing mentions, e.g. NIr. miol 'louse' at 3.11), so no synonym-history discussion of this group.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"likša\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sanskrit लिक्षा likṣā́ is a real word, but it means 'nit, the egg of a louse' (Pokorny's 'Nisse, Lausei'), not 'louse, flea eggs': Nourai's gloss mixes up the insect with its egg and substitutes flea for louse. Its descent from *erek- is not straightforward. Pokorny p.335 puts it in the zero grade but immediately adds that it is 'wohl aus *lakṣā durch Einfluß von likháti ‚ritzt‘' — i.e. the initial l- (for an expected r-) has to be explained by contamination with likháti 'he scratches'. Walde-Pokorny I 145 says flatly that 'wegen ai. likṣā ... müßte daneben ein idg. *ereik- angesetzt werden', and WP II 344 puts the word under *reik- 'to pluck, tear' with Persson, noting that likṣā may simply be a secondary assimilation of *ṛk-s-ā to likháti. Mayrhofer (EWAia, cited by Wiktionary s.v. लिक्षा, 2001:443) leaves the etymology open and calls comparisons with rákṣas- and with the European 'nit/mite' words problematic. The word is securely Indo-Aryan (Hindi līkh, Gujarati/Marathi līkh, Urdu līkh all continue it) — what is uncertain is the arrow from the root, hence plausible.\",\n          \"derivation_fa\": \"واژهٔ سنسکریت likṣā́ واقعی است، اما معنای آن «رشک، تخم شپش» است نه «شپش، تخم کیک»؛ نورایی در معنا میان حشره و تخمِ آن و میان شپش و کیک خلط کرده است. پیوندِ این صورت با ریشهٔ *erek- هم بی‌دردسر نیست: خود پوکورنی می‌نویسد که این صورت «احتمالاً از *lakṣā به تأثیر likháti ‚خراش می‌دهد‘» پدید آمده، یعنی لامِ آغازین به جای رای موردِ انتظار نیاز به توجیه دارد؛ والدهٔ‌پوکورنی (ج ۱ ص ۱۴۵) می‌گوید برای این واژه باید ریشهٔ جداگانهٔ *ereik- گذاشت که به *reik- «خراشیدن» می‌پیوندد، و مایرهوفر ریشهٔ آن را ناروشن می‌داند. بنابراین خود واژه قطعی است (بازمانده‌اش در هندی līkh و در اردو لیکھ زنده است) ولی خطِ رسم‌شده از ریشه به آن با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:335\",\n              \"status\": \"supports\",\n              \"note\": \"POK_01.txt line 5006 (IEW 335): 'Ai. likṣā ,Nisse, Lausei‘ (wohl aus *lakṣā durch Einfluß von likháti ,ritzt‘)' — the word does stand under erek-, in the zero grade, exactly as Nourai draws it, though Pokorny's parenthesis concedes the initial l- is secondary. The gloss is 'nit, louse egg', not 'louse, flea eggs'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 145 (WLD_Bd1_pages.txt block 153)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Wegen ai. likṣā „Nisse, Lausei“ ... müßte daneben ein idg. *ereik- angesetzt werden, welches evident zu idg. *reik(h)- „ritzen“ zu stellen ist' — accepts the comparison but not the simple root Nourai prints.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II 344 (djvu line 22394 ff.)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'likṣā : likháti scheint klar, kann aber auch Ergebnis nachträglicher Angleichung etwa eines *ṛk-s-ā an likháti sein' — the Sanskrit word is filed under *reik- 'to tear, pluck' after Persson, not under erek-.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, IEC.txt line 3668 s.v. erk- (1) 'tick, mite'\",\n              \"stance\": \"silent\",\n              \"note\": \"Mann's erk- lists only Irish earc, Lithuanian erkė, Latvian ērce; likṣā is absent from the entry (grep 'liksa' in IEC.txt → no hit).\"\n            },\n            {\n              \"src\": \"HJB\",\n              \"where\": \"Hobson-Jobson, HJB.txt (grep -i 'liksa', 'likh')\",\n              \"stance\": \"silent\",\n              \"note\": \"No Anglo-Indian entry for the word; it produced no loan into English, only the modern Indo-Aryan 'līkh' forms.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"rešk\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"رِشک\",\n          \"correct_form\": \"رشک\",\n          \"derivation\": \"The word itself is right and well attested: New Persian رِشک rešk / rišk 'nit, the egg of a louse' (again not 'flea eggs'; Borhan-e Qāteʿ, s.v., defines it 'رشک بالکسر بمعنی تخم شپش که بهندی لیکهه گویند' — 'nit, which in Hindi is called līkh'). What the arrow gets wrong is the direction of descent: Persian rešk is not borrowed or descended from Sanskrit likṣā́, it is its Iranian sister. Hübschmann, Persische Studien no. 618 (p. 67), sets up 'Np. rišk ‚Nisse‘ = afgh. riša fem. ‚Nisse‘ (= iran. *riška-, Geiger, Etym. p. 46, gegenüber skr. likṣā-)', and on p. 251 uses this very pair as his textbook example of the sound correspondence 'Np. r = skr. l: rišk ‚Nisse‘ = skr. likṣā, afgh. riṣa'. The Iranian branch keeps the original r- and the cluster -šk- (‹ Proto-Iranian *riška-/*rikšā-), the Indo-Aryan branch shows l- and -kṣ-; neither can come from the other. The living cognates listed by Horn (no. 618, p. 137) and by Moʿin's footnote in Borhan and by Aryanpur are Kurdish rišk, Balochi rask/rišk, Pashto riṣa, Ossetic Iron lisk / Digor liskä — a straight Iranian family, with no Middle Persian form recorded (MacKenzie and Nyberg have none). Note also that this rešk is a homonym of the commoner رشک/ارشک 'rešk, envy' (Av. araska-, MP arišk, Horn no. 71), a different word entirely. SCRIPT ERROR: the printed page (pdf p.159, see sources/refs/ocr/BOOK/159.png) shows the three-letter spelling رِشک with a kasra under the rā; the extraction turned that kasra into a yāʾ and produced «ریشک», which is a different Persian word (rīšak 'awn, small beard'). The book is faithful; the JSON must be fixed to رشک.\",\n          \"derivation_fa\": \"خود واژه درست است: «رِشک» در فارسی نو یعنی «تخم شپش»؛ برهان قاطع نیز می‌گوید «رشک بالکسر بمعنی تخم شپش که بهندی لیکهه گویند»، پس معنای «تخم کیک» در کتاب دقیق نیست. اما جهتِ پیکان نادرست است: «رشک» وام‌گرفته یا بازماندهٔ likṣā́ی سنسکریت نیست بلکه هم‌ریشهٔ (cognate) ایرانیِ آن است: هوبشمان در «مطالعات فارسی» شمارهٔ ۶۱۸ (ص ۶۷) می‌نویسد «Np. rišk = afgh. riša (= iran. *riška-) در برابر skr. likṣā-» و در ص ۲۵۱ همین جفت را نمونهٔ قاعدهٔ «r فارسی = l سنسکریت» می‌آورد. یعنی شاخهٔ ایرانی رای آغازین و خوشهٔ -شک را نگاه داشته (ایرانی باستان *riška-) و شاخهٔ هندی لام و -کش را؛ هیچ‌یک از دیگری گرفته نشده است. هم‌خانواده‌های زنده (هرن شمارهٔ ۶۱۸، حاشیهٔ معین بر برهان، و آریان‌پور): کردی rišk، بلوچی rask/rišk، پشتو riṣa، آسی ایرونی lisk. این «رشک» را نباید با «رشک/ارشک» به معنی حسد (از اوستایی araska-) یکی گرفت. نکتهٔ خوانش: در صفحهٔ چاپی کتاب همان «رِشک» با کسره آمده؛ در استخراج JSON آن کسره به ی خوانده شده و صورت نادرستِ «ریشک» پدید آمده که واژهٔ دیگری است؛ پس خطای خوانش اسکن است، نه خطای کتاب.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B4%DA%A9\",\n            \"https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:137\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss no. 618 on p. 137 (HRN.txt line 5507, the page footer '- 138 -' follows a few lines later): '618. risk ‚Lauseei, Nisse‘ (AM. 141 Zeile 11, 191 Zeile 7). ai. likṣā ‚Ei einer Laus, Nisse‘ (Nöldeke bei Hübschmann, Oss. Etym., S. 46). kurd. LW. risk; afg. riša; bel. LW. rask, risk ‚Läuse‘; oss. t. lisk, d. liskä ‚Nisse‘.' Horn's page and word are exactly as cited — but he puts the Sanskrit beside the Persian as a comparandum, not above it as an ancestor.\"\n            },\n            {\n              \"ref\": \"BQT:952\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qāteʿ, s.v. رشک — BQT_v2_pages.txt leaf 412 (printed ≈ 952-955 by the vol-2 rule printed = leaf + 543 ±3; the running-head numeral is illegible in the OCR). Text: 'رشک بالکسر بمعنی تخم شپش که بهندی لیکهه گویند آمده، وآن غیر کرم است'; and Moʿin's etymological footnote on the same page: 'هندی باستان [likṣā] (تخم شپش)، کردی khsir > افغانی axir، بلوچی ...' and 'ایرانی *rišk- برابر سانسکریت likṣā، هوبشمان'. So Nourai's citation is sound, and Moʿin too writes 'Iranian *rišk- ≈ Sanskrit likṣā' (comparison, not descent).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien no. 618, p. 67 (HUB.txt line 2337) and p. 251 (line 9251)\",\n              \"stance\": \"partial\",\n              \"note\": \"p.67: 'Np. rišk ‚Nisse‘ = afgh. riša fem. ‚Nisse‘ (= iran. *riška-, Geiger, Etym. p. 46, gegenüber skr. likṣā-)'; p.251: 'Np. r = skr. l: rišk ‚Nisse‘ = skr. likṣā, afgh. riṣa'; also p.238 'rišk ‚Nisse‘, osset. lisk, skr. likṣā-'. Supports the word and the connection, contradicts the drawn direction (cognate via Proto-Iranian *riška-, not a descendant of Sanskrit).\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, printed p. 307 (incoming/ARY/ARY_pages.txt, [pdf page 306], line 9033)\",\n              \"stance\": \"partial\",\n              \"note\": \"Headword 'رشک (به چم „تخم شپش‘) / ۳۰۷' with the cognate list 'پارسی باستان *RISKA-, اوستی LISK, کردی ..., بلوچی RASK/RISK, افغانی (پشتو) RIŠA, سانسکریت LIKṢĀ, لاتین ..., لیترانی ERKĖ' and a reference to Borhan-e Qāteʿ. Independent modern Persian confirmation of the whole comparison set — and of an Old Iranian *riska- as the Persian word's own ancestor, i.e. cognate rather than descent.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, PHD_mackenzie.txt (grep -i 'risk', 'rišk')\",\n              \"stance\": \"silent\",\n              \"note\": \"No Pahlavi *rišk in MacKenzie's Concise Pahlavi Dictionary (the only 'risk' hits are English glosses). The Middle Persian stage of this word is simply not attested, so Nourai's jump straight to New Persian is not itself a fault.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, NYB_vol2_glossary.txt (grep 'risk' → 'araska-: arisk', line 5003)\",\n              \"stance\": \"silent\",\n              \"note\": \"Nyberg's glossary has only arišk 'envy' ‹ Av. araska- — the homonym — and nothing for 'nit'; useful as confirmation that the two رشک words are distinct.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, MON_part1/2.txt (grep 'رشک', 'تخم شپش')\",\n              \"stance\": \"silent\",\n              \"note\": \"The OCR of Moʿin's Farhang shows only رشک 'envy' entries (e.g. part2 lines 3815-3816 'رشک بردن ... حمیت'); the 'nit' headword could not be located in the scan, so Moʿin adds nothing here beyond his Borhan footnote.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"ricinus\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin ricinus is a real word of the rustic writers (Cato, Varro, Columella, Pliny), but it means 'tick, sheep-louse' — Pokorny's '‚ein sich in die Haut von Schafen, Hunden oder Rindvieh einbohrendes Ungeziefer, Zecke‘' — not 'flea'. Its attachment to *erek- is Pokorny's own conjecture and is stated as such: the form 'kann auf älteres *recinos zurückgehen und mit lit. erke ‚Zecke, Schaflaus‘ (*erkia), lett. erce ‚Kuhmilbe‘ unter idg. *erek- zusammengehören', i.e. it needs a metathesised/aphaeretic pre-form *recinos before the comparison works. Latin specialists do not follow him: Ernout-Meillet (Dict. étym. de la langue latine s.v.) end the article 'Sans étymologie connue', and de Vaan (reported at Wiktionary s.v. ricinus) has 'Unknown; possibly a substrate word', adding that the Albanian, Lithuanian, Latvian, Sanskrit and Persian look-alikes 'cannot be regularly derived from a common Proto-Indo-European source'. So the node is a genuine Latin word correctly placed in the traditional comparison, but with a wrong gloss and a derivation that modern Latin etymology declines: plausible.\",\n          \"derivation_fa\": \"واژهٔ لاتین ricinus واقعی است و در متون کشاورزی (کاتو، وارو، کولوملا، پلینیوس) به کار رفته، اما معنای آن «کنه، شپشِ گوسفند» است نه «کیک». پیوستن آن به ریشهٔ *erek- حدسی است که خود پوکورنی با قید «kann» (می‌تواند) آورده و برای درستی‌اش باید صورت کهن‌ترِ *recinos فرض شود. لاتین‌شناسان این را نپذیرفته‌اند: ارنو-مییه مقاله را با جملهٔ «Sans étymologie connue» (ریشهٔ شناخته‌ای ندارد) پایان می‌دهند و دووان آن را احتمالاً واژهٔ زیرلایه‌ای می‌داند. پس این گره با احتیاط پذیرفتنی است و معنای «flea» در کتاب نادرست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ricinus\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:335\",\n              \"status\": \"supports\",\n              \"note\": \"POK_01.txt line 5007 (IEW 335): 'lat. ricinus 1. ‚ein sich in die Haut von Schafen, Hunden oder Rindvieh einbohrendes Ungeziefer, Zecke‘ (unsicher ist die Zugehörigkeit von 2. ‚eine Strauchart, Ricinus communis‘) kann auf älteres *recinos zurückgehen und mit lit. erke ... unter idg. *erek- zusammengehören.' Pokorny does put it under the root, with two explicit hedges (kann; unsicher).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. ricinus (LAT.txt line 53520 ff.)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'ricinus, -ī m.: 1° tique, pou du mouton. Mot rural (Cat., Varr., Col., etc.); 2° ricin, plante appelée également cici ou croton, Plin.15,35; 3° mûre imparfaite ... Seul le premier sens est ancien et usuel; il est possible que les deux autres appartiennent à un homonyme de tout autre origine. Sans étymologie connue.' No IE root at all, and the plant sense may be a different word.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. Ricinus (KLN_1966.txt line 32862)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Ricinus, n., a genus of plants (family Euphorbiaceae). — L., ‚the castor-oil plant‘, which is of uncertain origin.' Klein knows the Latin word but offers no etymology.\"\n            },\n            {\n              \"src\": \"LEW\",\n              \"where\": \"Walde, Lat. etym. Wb. 2nd ed. 1910 (LEW_1910.txt, grep -i 'ricinus')\",\n              \"stance\": \"silent\",\n              \"note\": \"No hit in the OCR of the 1910 edition, although Walde-Pokorny II 344 refers to 'Vf. LEWb.² u. ricinus'; the entry is presumably present in print but lost to the scan, so nothing can be quoted from it.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 145 and Bd. II 344\",\n              \"stance\": \"partial\",\n              \"note\": \"Bd. I 145 gives the same tentative *erek- account ('kann auf älteres *recinos zurückgehen'); Bd. II 344 reports Persson's rival assignment of ricinus to *reik- '(kann aber auch für *recinos stehn)'. Two incompatible homes for one word.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"ricin\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English ricin is real and correctly glossed: the toxic protein of the castor bean, isolated and named by Peter Stillmark at Dorpat in 1888, formed on the Linnaean genus name Ricinus (communis), the castor-oil plant, with the chemical suffix -in (Etymonline: 'ricin — poison obtained from the castor-oil bean, 1888, from ricinus, genus name of the castor-oil plant'). The genus name is Latin ricinus, in use as a plant name since 1694 and already glossed in late Old English herbaria as ricinum; Linnaeus took it from Pliny, who applies ricinus to the plant because its mottled seed looks like an engorged sheep-tick. So the route Latin → New Latin genus → modern chemical term is solid. The weak joint is the one Nourai does not show: whether Pliny's plant-name ricinus is the same word as the rustic ricinus 'tick' at all. Pokorny himself brackets it off ('unsicher ist die Zugehörigkeit von 2. ‚eine Strauchart, Ricinus communis‘'), Ernout-Meillet think senses 2-3 may belong to 'un homonyme de tout autre origine', and Etymonline says only 'perhaps the same word as ricinus ‚tick“'. Hence plausible: the English word does come from Latin ricinus, but from the plant sense, whose identity with the 'tick' sense drawn in the chart is not established.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی ricin درست معنا شده است: پروتئین زهرآگینِ دانهٔ کرچک که پتر اشتیلمارک در سال ۱۸۸۸ جدا کرد و بر پایهٔ نامِ جنسِ گیاهی Ricinus communis (کرچک) با پسوند شیمیایی -in ساخته شد. این نامِ جنس را لینه از لاتینِ پلینیوس گرفته، که خود گیاه را به سبب شباهتِ دانه‌اش به کنهٔ پرخون ricinus نامیده است. پس زنجیرهٔ لاتین ← لاتینِ علمی ← انگلیسی درست است؛ نقطهٔ سست آن جاست که یکی بودنِ ricinusِ «گیاه» با ricinusِ «کنه» — که نمودار فرض گرفته — قطعی نیست؛ پوکورنی آن را «unsicher» خوانده و ارنو-مییه احتمال داده‌اند که دو واژهٔ هم‌آوا باشند. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/ricin\",\n            \"https://en.wiktionary.org/wiki/ricinus\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:1116\",\n              \"status\": \"not_checked\",\n              \"note\": \"AHD:1116 is a page of the main A-Z text of the American Heritage Dictionary, New College ed. (1975/76), which is not among the local files — only Watkins' IE-roots appendix (AHD_watkins1985.txt) is on disk, and it has neither an *erek- root nor RICIN in its English index (grep -i 'erek|ricin' → no relevant hit). Alphabetically p.1116 of that edition falls in the R's, so the citation is plausible for a dictionary definition of 'ricin', but it could not be inspected.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls, FSD_vol3.txt lines 239778-239784\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ricinulei ... A suborder of opilionine arachnids ... [< L ricinus, a tick]' and 'Ricinus ... A monotypic genus of tall annual plants of the spurge family. Ricinus communis, the castor-oil plant ... [< L ricinus, castor-oil plant]', with the ricinoleic/ricinoleate chemical family alongside — confirms the Latin → scientific-Latin → English route for both senses.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. Ricinus (KLN_1966.txt line 32862)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Ricinus, n., a genus of plants (family Euphorbiaceae). — L., ‚the castor-oil plant‘, which is of uncertain origin.' Klein gives the Latin source of the genus name (hence of ricin) but refuses the further etymology Nourai draws.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, SKT.txt (grep -i 'ricin')\",\n              \"stance\": \"silent\",\n              \"note\": \"Skeat's Concise Dictionary has no entry for ricin or Ricinus (the word is a late-19th-c. technical term, outside his scope).\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's New Twentieth Century, WEB_vol1.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"Only volume 1 (A-?) of Webster's 2nd ed. is on disk, so the R entries could not be consulted.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-159.json > /dev/null && echo \"JSON OK\"",
 "description": "Write page-159.json and validate"
}
```


### [2026-09-05T20:41:54.717Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T20:41:58.002Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 tools/verify_check.py 159",
 "description": "Run verify_check for page 159"
}
```


### [2026-09-05T20:41:59.978Z] TOOL RESULT

```
nodes verified: 4/4
node verdicts: {'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 4, 'not_checked': 1}
books consulted: {'partial': 6, 'contradicts': 2, 'silent': 8, 'supports': 1} | by book: {'WLD': 3, 'KLN': 2, 'IEC': 1, 'HJB': 1, 'HUB': 1, 'ARY': 1, 'PHD': 1, 'NYB': 1, 'MON': 1, 'LAT': 1, 'LEW': 1, 'FSD': 1, 'SKT': 1, 'WEB': 1}
```


## [2026-09-05T20:42:17.937Z] AGENT

Page 159 verified. `verify_check.py 159`: 4/4 nodes, 0 PROBLEM lines.

**Verdicts** — root: plausible ×1; nodes: plausible ×3, transcription_suspect ×1. Ref checks: supports ×4, not_checked ×1 (AHD:1116, main-dictionary page not on disk).

**Root Erek (POK:335)** — a real Pokorny lemma, quoted verbatim from POK_01.txt p.335: "1. erek- ‚Laus, Milbe' oft tabuierend entstellt", with likṣā and ricinus as its only two derivatives. Downgraded to plausible because (a) Nourai glosses Laus as "flea" throughout instead of "louse/nit", and (b) Walde-Pokorny I 145 says Sanskrit likṣā needs a separate *ereik-, WP II 344 files both words under *reik- instead, and de Vaan/Wiktionary call Latin ricinus "unknown, possibly a substrate word" — a taboo-distorted wander-word, not a securely reconstructable root.

**Flagged items**
- `transcription_suspect` — Persian node #2, rešk: **extraction error**. The printed page shows the three-letter «رِشک» (rā + kasra); the JSON reads the kasra as a yāʾ and gives «ریشک», which is a different word (rīšak "awn"). `error_in: extraction`; page image saved to `data/verification/sources/refs/ocr/BOOK/159.png`. **The owner should fix `data/extracted/batch/page-159.json` node 2 script to رشک.**
- Same node, substantive point: the arrow Sanskrit → Persian is the wrong direction of descent. Hübschmann PSt no. 618 (p.67, p.251) makes rešk the Iranian cognate (‹ Proto-Iranian *riška-, cf. Kurd. rišk, Bal. rask, Pashto riṣa, Oss. lisk), not a descendant of likṣā; Aryanpur p.307 and Moʿin's Borhan footnote (leaf 412 ≈ p.952-955) agree. Recorded in the derivation; verdict driven by the script error.
- Gloss errors (noted, not separately flagged): Lat. ricinus = "tick, sheep-louse", not "flea"; Skt. likṣā / Pers. rešk = "nit, louse egg", not "flea eggs".

Nourai's own refs POK:335, HRN:137 and BQT:952 all check out on the cited pages.
