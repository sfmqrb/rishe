# Verification process log — verify-page-123


## [2026-09-05T18:14:35.312Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 123 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-123.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-123.json. Write /home/sfmqrb/git/rishe/data/verification/page-123.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 123` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T18:14:36.723Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T18:14:37.433Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T18:14:37.453Z] TOOL RESULT

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


## [2026-09-05T18:14:37.689Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-123.txt"
}
```


### [2026-09-05T18:14:37.709Z] TOOL RESULT

```
1	=== PDF page 123 (book page 93) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dhars, Dhers : to dare  (refs POK:259)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:259; SYN:1149; KNT:190 | darš : dare, to be bold ; daršam : boldly
5	  #2 (parent #1) [Persian] refs=HRN:122; BQT:837 | dorošt «درشت» : large, rough | NOTE: POK:216 derives this from the Indo-European root "Deru 1:wood, firm".
6	#3 (parent #0) [Old High German] refs=AHD | tar : dare
7	  #4 (parent #3) [English] refs=None | dare
8	#5 (parent #0) [Latin] refs=AHD | infestare : to disturb
9	  #6 (parent #5) [English] refs=None | infest, manifest
10	--- entry 1 ---
11	ROOT [Indo-European] Dhě 1, Dhe-mnâ : to suckle milk, to produce; one who gives milk, nurse. Compare with the root "Dheugh: to milk".  (refs POK:241)
12	#1 (parent #0) [Avestan] refs=POK:241 | daenu : female
13	  #2 (parent #1) [Persian] refs=BQT:822; HRN:119 | dâyeh «دایه» : baby sitter, nurse ; dâyě «دایی» : mother's brother
14	#3 (parent #0) [Avestan / Old Persian] refs=POK:242 | dânô : grain ; danâxe : grain
15	  #4 (parent #3) [Persian] refs=BQT:820 | dâneh «دانه» : grain ; dâng «دانگ» : one sixth of the property
16	#5 (parent #0) [Sogdian] refs=SOD:134,136 | d`n : seed ; d`yh : female servant
17	#6 (parent #0) [Latin] refs=AHD | fěmina : female ; filius : son ; fě-tus : offspring
18	  #7 (parent #6) [English] refs=None | female ; affiliation ; fetus
19	
```


## [2026-09-05T18:14:41.672Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-123.json | head -200",
 "description": "Show source JSON for page 123"
}
```


## [2026-09-05T18:14:41.907Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T18:14:43.455Z] TOOL RESULT

```
{
    "pdf_page": 123,
    "book_page": 93,
    "entries": [
        {
            "root": {
                "name": "Dhars, Dhers",
                "lang": "Indo-European",
                "refs": "POK:259",
                "gloss": "to dare"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:259; SYN:1149; KNT:190",
                    "words": [
                        {
                            "translit": "dar\u0161",
                            "gloss": "dare, to be bold",
                            "script": null
                        },
                        {
                            "translit": "dar\u0161am",
                            "gloss": "boldly",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "HRN:122; BQT:837",
                    "words": [
                        {
                            "translit": "doro\u0161t",
                            "gloss": "large, rough",
                            "script": "\u062f\u0631\u0634\u062a"
                        }
                    ],
                    "script_extra": null,
                    "note": "POK:216 derives this from the Indo-European root \"Deru 1:wood, firm\".",
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Old High German",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "tar",
                            "gloss": "dare",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "dare",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "infestare",
                            "gloss": "to disturb",
                            "script": null
                        }
                    ],
                    "script_extra": null,
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
                            "translit": "infest, manifest",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Dh\u011b 1, Dhe-mn\u00e2",
                "lang": "Indo-European",
                "refs": "POK:241",
                "gloss": "to suckle milk, to produce; one who gives milk, nurse. Compare with the root \"Dheugh: to milk\"."
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:241",
                    "words": [
                        {
                            "translit": "daenu",
                            "gloss": "female",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "BQT:822; HRN:119",
                    "words": [
                        {
                            "translit": "d\u00e2yeh",
                            "gloss": "baby sitter, nurse",
                            "script": "\u062f\u0627\u06cc\u0647"
                        },
                        {
                            "translit": "d\u00e2y\u011b",
                            "gloss": "mother's brother",
                            "script": "\u062f\u0627\u06cc\u06cc"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:242",
                    "words": [
                        {
                            "translit": "d\u00e2n\u00f4",
                            "gloss": "grain",
                            "script": null
                        },
                        {
                            "translit": "dan\u00e2xe",
                            "gloss": "grain",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Persian",
                    "refs": "BQT:820",
                    "words": [
                        {
                            "translit": "d\u00e2neh",
                            "gloss": "grain",
                            "script": "\u062f\u0627\u0646\u0647"
                        },
                        {
                            "translit": "d\u00e2ng",
                            "gloss": "one sixth of the property",
                            "script": "\u062f\u0627\u0646\u06af"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
```


### [2026-09-05T18:14:43.492Z] TOOL RESULT

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


## [2026-09-05T18:15:14.930Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','SYN','HRN','BQT','SOD','AHD','MON','ARY','PHD','BRT','WLD','IEC','CHEUNG','HUB','KLN','SKT','LKT','TTS']:\n    v=d.get(k)\n    print('===',k, json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Print ref metadata for keys"
}
```


## [2026-09-05T18:15:15.757Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-123.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-05T18:15:16.681Z] TOOL RESULT

```
=== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
=== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec
=== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
=== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
=== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
=== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca
=== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
=== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
=== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
=== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
=== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
=== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
=== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
=== CHEUNG null
=== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
=== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
=== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
=== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}
=== TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books.", "notes": "Open full text (public domain). OCR rough (Fraktur +
```


### [2026-09-05T18:15:18.083Z] TOOL RESULT

```
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 0,
                    "lang": "Sogdian",
                    "refs": "SOD:134,136",
                    "words": [
                        {
                            "translit": "d`n",
                            "gloss": "seed",
                            "script": null
                        },
                        {
                            "translit": "d`yh",
                            "gloss": "female servant",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "f\u011bmina",
                            "gloss": "female",
                            "script": null
                        },
                        {
                            "translit": "filius",
                            "gloss": "son",
                            "script": null
                        },
                        {
                            "translit": "f\u011b-tus",
                            "gloss": "offspring",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "female",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "affiliation",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "fetus",
                            "gloss": null,
                            "script": null
                        }
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


## [2026-09-05T18:15:24.211Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 267 268; do echo \"=== POK_01 leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt | head -80; done",
 "description": "Print Pokorny p.259 area"
}
```


## [2026-09-05T18:15:25.096Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 249 250 251; do echo \"=== POK_01 leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt | head -90; done",
 "description": "Print Pokorny p.241-242 area"
}
```


### [2026-09-05T18:15:25.750Z] TOOL RESULT

```
=== POK_01 leaf 267 ===
 zu  got.  draühts)]  ags.  dora  m.  , Hummel' [*duran-)j  engl,  dorr  , Maikäfer';
redupl.  lett.  dunduris  ,große  Bremse,  Wespe',  denderis(?)  , weinender Knabe'  (Mühlenbach-Endzelin  I  455).
x4.uch  für  kelt.  und  balt.-slav.  Worte,  die  unter  cZe?*-  , murren'  genannt sind,  kommt  idg.  Anlaut  dh-  in  Frage.
dhren-:
ai.  dhrdnati  ,tÖnt'  (Dhätup.);
gr.  -d-QfjVog  m.  ,Totenklage,  Klagelied',  dgrjvew  ,wehklage',  ^qwva^-  xrjq)rjv (Drohne)  Hes.,  Tav-&Q7]V7]  ,Horniß',  dvS-Qrjvrj  {*dv-9-o-dQ'^v7])  , Waldbiene'; as.  dreno,  ahd,  ir^eno  , Drohne',  dehnstufig  as.  drän  ds.,  auch  ags.  drän drxn  f.  , Drohne';  schwachstufig  got.  drunjus  , Schall',  novw.  dryn  n.  , leises Brüllen',  drynja  ,leise  brüllen',  nd.  drönen  ,Lärm  machen,  langsam  und eintönig  reden'  (daraus  nhd.  dröhnen).
Eine  Anlautdublette  liegt  vielleicht  in  lit.  tränas,  aksl.  "^troH,  ^trqdi> , Drohne'  vor;  vgl.  Trautmann  326.
256
5-Erw.  in  mir.  dresacht  ^knarrendes  oder  quietschendes  Geräusch^,  g^U l3it.   drensö,    -äre   ^schreien   (vom   Schwan)'^,   ndd.    dt-unsen   ,leise    brülleßf ndl.  drenzeln  ,winseln',  hess.  drensen  ,äclizen',  nhd.  dial.  trensen  »lang-o-ezoo-g^  ■ brüllen^  (von  Kühen).
Eine  Gutt.-Erw.  wohl  in  arm.  drncim  ,Horn  blasen,  tuten^  (*dhrenk-)  xin^ air.  dreckt  ,Lied,  Geschichte^  (*dhrenkta)^  urslav.  *drokz  (*dhrnk-)  [^ sloven.  drok  , Stößel^  usw.;
vielleicht  toch.  A  tränk-,  B  treiik-  , sprechend
WP.  I  860  f.,  WH.  I  374,  Mladenov  Mel.  Pedersen  95ff.
4.  (dber-:)  dhor-  :  dber-  , springen,  bespringen'.
Ai.  dhärä  ,Strom,  Strahl,  Tropfen,  Same^;
gr.  (ion.)  S-ooögy  -^oqtj   , männlicher   Same',  d-oglaycsad-aL    , Samen  in  sich    ^ aufnehmen',  dichterisch  ^^(^cxw,  att.  ^gwaxu),  Fut.  d^oqov^aL,  Aor.  ed^o^oy     , , springen',   d^goanög  , Vorsprung,   Anhöhe'  {d-QCü-  aus   *dherd-j    das   wegen des  o  der  übrigen  Formen  zu  *dhore-j  dhoi^-^  dqu)-  entwickelt  ist);
von    einer    Basis    dhereu- :  d-ÖQwuai,    d^OQvvofxaL   , bespringen'    {oq    wohl  -^ äolisch  statt  ag  aus  x)  vgl.  d^aQvsvei'  dxevei.  OTtsiqsL.  q}v%evet  Hes.,  ■d'ccQw- ad-au'  dxsveiv  Hes.;  -d-ovgog  , stürmisch,  ungestüm'  wohl  aus*i^oß/os  (Bechtel Lexil.  167);
mir.  dar-  ,bespringen',  Impf,  no-dairedj  Prät.  ro-dart,  Verbalnom.  dair^ Gen.  dära,  myth.  PN  Däire  {*dhärio-s)j  der  ,Mädchen',  cjmr.  -der ig ,brünstig'.
WP.  I  861,  WH.  I  528,  Schwjzer  Gr.  Gr.  I  696,  708.
5.  dher-,  dhrei-d-  ,Unrat,  cacäre'  (ob  verwandt  m
=== POK_01 leaf 268 ===
it  1.  dher- , trüber  Boden-
satz' und  4.  dher-?).
Lat.  foria  PL  ^Durchfall'  (bei  Varro  von  Schweinen),  foinö,  -Ire  ,cacäre';
gr.  daQÖaiveL'  iiolvveu  (*dkr-d-)  Hes.,  nach  Fick  KZ.  44,  339  make- donisch, entweder  aus  d-aq-d--  mit  gebrochener  Red.  oder  aus  d-aq-d-  mit demselben  formantischen  -d-  wie  die  z-Erw.  dJir-ei-d-]  sehr  zweifelhaft;
lit.  der-k-iü  derkti  ,besudle  mit  Unflat,  leere  den  After'.
dbr-ei-d' :
anord.  drita  {dreit),  ags.  drltan,  mndl.  ndd.  drlteuj  ahd.  trizan  ,cacäre';    . o-stufig  anord.    dreita  ,facere    cacäre',    schwundstufig    mengl.    nengl.   dirt (aus  *drit),  aisl.  dHtj  fläm.  drits,  trets  , Dreck,  Kot',  westfäl.  dridt  , Schiß';
russ.  dial.  dristdth  ,Durchfall  haben',  bulg.  driskam^  dristh  ,habe  Durch- fall',  serb.   driskatij   dHckatij    cech.  dristati  ds.  (slav.  *drisk-,  *drist-  aus  J^ *dhreid-sk-j  -(s)t-j  Berneker  224).
WP.  I  861  f.,  WH.  I  527  f.
257
rSzb'  ;ziehen;  am  Boden  schleifen^,  gleiclibed.  mit  tmgh-  (s.  d.).
Anord.  draga,  got.  u.  ags.  dragan,  engl,  draio  ^ziehen",  anord.  drag  n. T/uterlage  eines  gezogenen  Gegenstandes^,  norw.  drag  , Luftzug^  Wellen- 'chl'*^;  Wasserlauf,  Zugseil^  dial.  drog  f.  (*dragö)  ^kurzer  Schlitten, ^Y'ecr(spur)  eines  Tieres^  Tal',  anord.  dregill  ,Band',  drög  f.  ^Streifen', ischwed.  dregh  , Schlitten',  ags.  drcege  f.  , Schleppnetz',  mnd.  dragge,  nnd. aucli  dregge  ,Bootsanker',  engl,  dredge  ds.;  ablautend  norw.  dorg  f.  \*durgöj jj,r.  *dhfghä)  , Angelschnur,  die  man  hinter  dem  Boot  herzieht';  mit  der Bed.  ,tragen'  (aus  ,schleppen',  s.  Berneker  212),  ahd.  tragan  ,tragen', iih  {gi)tragon  ,sich  betragen'.
Wohl  hierher  sl.  *därgä  in:  serb.-ksl.  draga  ;Tal',  russ.  doröga  ,Weg, j^eise',  dial.  , Angel',  serb.  dräga  ,Tal',  poln.  droga  ,Weg,  Straße,  Reise', russ.  dorözih  ,aushöhlen',  ßech.  drd^iti  ,einen  Falz  oder  eine  Furche machen,  aushöhlen';  vielleicht  auch  öech.  z-drdhati  se  ,sich  weigern',  poln. icz-dragac  sie  ,sich  sträuben,  nicht  daran  wollen'  (als  ,hinziehen')  und  aksl. podrag^  ,Saum,  Rand  eines  Kleides'  u.  dgl.  (anders  unter  dergli-  , fassen').
Lat.  trahö  .ziehe',  traha  , Schleife',  trägum  ,Schleppnetz',  trägula  ,ds., kleine  Schleife'  können  durch  Spirantendissimilation  {^*dragö  zu  *dragö) auf  dhragh-  zurückgehen,  aber  auch  idg.  t-  haben  (:  air.  traig  ,Fuß'  usw., 8.  trUgh-).
WP.  I  862,  Trautmann  45.
dbcrbh'
```


### [2026-09-05T18:15:27.650Z] TOOL RESULT

```
=== POK_01 leaf 249 ===
rüngl.  M^iGTog  ,*die  fest  und  unverbrüchlich  stehende' als  Göttinname,  dann  , Recht,  Gesetz,  Sitte',  d^e^is-d-Xa  PL  ,die  Grundlao-en eines  Gebäudes;  das  Tiefste,  Innerste',  d-ei.ieXioi  Xld-oi  ,die  Grundsteine' hom.  d^Bf-ieiXia  (ec  metr.  Dehnung)  , Grundlage,  Grund';
tief  stuf  ig:  ^a^a  ,*in  Haufen;  häufig,  oft',  d-apivog  , häufig,  gehäuft' hom.  d-a^-iieg^  femin.  d-afxeiaL  PI.  , gehäuft,  dicht  gedrängt'  (von  *0-ai.ivg\ d-äixvog  , Dickicht,  Gebüsch,  Strauch';  auf  ein  *dhd-mo-  jNiederlassuno- Wohnstätte'  (vgl.  '9-aLf,iög'  ohia,  artögog,  g)vT€ia  Hes.  [^dhdmio-l^  auch  ai. dhäman-  , Wohnstätte')  oder  , Haufe,  Schar  (der  Diener)'  bezieht  man  viel- leicht mit  Recht  auch  lat.  famulus  ,Diener', /ami'Zm  , Hausgenossenschaft', osk.  famel  , famulus',  famelo  ,familia',  umbr.  famerias  ,familia';
ö-stufig  gr.  d-wiiog  , Haufe,  Schober';  phryg.  dov^-iog  ,avvoSog,  ffvyxlr^Tog, aviißiu}OLg\  lat.  ah-dömen  , Unterleib*  als  ,pars  abdita',  vgl.  ahd.  intuoma ,exta'  (wäre  lat.  *indömen),  mnd.  ingedöme,  bayr.  ingetum  ds.,  got  döms m.  , Urteil,  Ruhm'  {dömjan  ,urteilen';  aus  dem  Germ.  russ.  düma  .Gedanke, Sorge;  Ratsversammlung'  usw.,  s.  Berneker  237),  ags.  dorn  »Meinung,  Sinn, Urteil,  Gericht',  ahd.  tuom  , Urteil,  Tat,  Sitte,  Zustand',  lit.  dornk,  domesya .Aufmerksamkeit,  Richten  des  Gedankens  und  Willens  auf  etwas',  auch lit.  deme  ,Mal,  Zustand;  ausgedachter  Grund'  usw.,  demetis  =  dometis jsich  merken,  die  Aufmerksamkeit  worauf  richten*.
Aisl.  dcell  jfacilis'  (*dhe-li-s):  vgl.  urnord.  dalidvn  ,sie  machten*  (Prät. von  germ.  *delian),  lit.  pa-delys  ,der  Henne  unterlegtes  Ei*,  priedelly priedelis  , Beilage',  abg.  d^lo  n.  ,Werk*,  wozu  (s.  Berneker  195 f.,  Traut- mann 48)  aksl.  delja,  däljhma  m.  Gen.  , wegen*,  lit.  del^  delj  deliaij  lett. deV  mit  Gen.  , wegen,  um  willen*.
An  vereinzelten  Bildungen  vgl.  noch  gr.  Ts-d-^iög  (Pind.),  d-e&(.iög  (lak. usw.),  &s(Ti,i6g  (att.)  , Satzung*  nach  Thurneysen  (KZ.  51,  57)  zu  air.  dedm, cymr.  deddf  (*dhe-dh-mä)  ds.  (anders  Schwyzer  Gr.  Gr.  I  492 ^^);  ^(orj, att.  ■d'0)d  , Strafe*.  Sehr  unsicher  wird  auf  eine  &'-Erw.  bezogen  aisl.  des {*dasjö)    , Heustock,    Heudieme'    (Lw.  aus    dem  Air.?),   air.   dais   {*dasti')
J-
239
Haufen,  Heudieme',   womit  E.  Lewy  (KZ.  52,  310)  vielmelir  osset.  dasun laufliaufen'  vergleicht.
'*  ^yp.  I  826  ff.,  WH.  I  266,  362  f.,  439ff.,  863,  Trautniann  47  ff.,  Schwyzer Qr.  Gr.  I  492,  686,  722,  725,  741,    Pedersen  Hitt.  141  ff.,  192.
dbe-,  dho-  ^hinschwinden^?
Lat.  fames  f.  , Hunger',  ad  fatim,  affatim  ,ad  lassitudinem,  zur  Genüge^, fatigö  ^hetze  ab,  ermüde^,  fatiscö,  -or  ,gehe  auseinander;  ermatte^;  air.  ded- (präs.  ru-dedüj  Fut.  Plur.  dedaitj  Prät.  con-ro-deda)  ,evanescere,  tabescere'; ao-s.  demm  , Schaden^  (*dhd-mi-s)]
mit  -s  anord.  dasi  ,träge'  (germ.  *d^s-),  mhd.  dcesic  ,still,  verschlossen, dumm^,  ablautend  norw.  dial.  dase  ,schlappe  Person^,  dän.  dase  ,faul  sein'; anord.  dcBsa(sk)  ^verschmachten,  verkommen',  c^asas^ , verkommen,  schlechter werden';  mengl.  dasen  , betäuben'  (engl,  daze),  dasewen  ,dunkel
=== POK_01 leaf 250 ===
  sein'.
In  allen  Gliedern  etwas  zweifelhafte  Verbindung.  Über  air.  de'd(a). vgl.  Pedersen  KG.  II  504  f.  (von  einem  Perf.  *dhe-doue  aus  zu  got.  diwans , sterblich'?  s.  dheu-  , hinschwinden',  wo  auch  über  air.  dlth,  arm.  di).  Die germ.  Sippe  endlich  erinnert  z.  T.  an  die  unter  "^dheues-  ,stieben'  bespro- chene von  ndd.  dösig  und  könnte  nicht  bloß  in  der  5-Erw.,  sondern  auch in  der  Bed.  sich  z.  T.  nach  dieser  gerichtet  haben;  immerhin  ist  mit  einer alten  Verwandtschaft  von  anord.  dcesask  usw.  und  ir.  -deda  zu  rechnen.
WP.  I  829,  WH.  I  451.
dheb-  ,dick,  fest,  gedrungen'.
Ahd.  tajpfar  , gravis,  gravidus;  schwer^  gewichtig',  mhd.  tapfer  ,fest, gedrungen,  voll,  gewichtig,  bedeutend',  spät  ,tapfer  (fest  im  Kampfe)', ahd.  tapfare  ,mole',  tapfarl  f.  ,moles',  mnd.  dapper  , schwer,  gewichtig, gewaltig',  ndl.  dapper  , tapfer;  viel',  norw.  daper  ,trächtig',  anord.  dapr ,schwer,  schwermütig,  düster,  traurig'.
Vielleicht  an.  damrarj  nhd.  Damm,  mhd.  tarn  ds.,  got.  faurdamwjan ,verdämmen,  hindern',  als  dhobmö-  hierher?
Aksl.  deheh  ,dick',  russ.  mdartl.  dehelyj  , wohlbeleibt,  stark,  fest',  abl. dohölyj  ,stark,  kräftig'  (usw.,  s.  Berneker  182);  apr.  deblkan  ,groß';  viel- leicht auch  lett.  dabVs  u.  dähls  , üppig',  dahVi  audzis  , üppig  gewachsen', dahVigs  ,üppig'  (Berneker  aaO.;  nach  Mühlenbach-Endzelin  I  428  sind jedoch  die  lett.  Wörter  wahrscheinlich  mit  aksl.  dohrh  zu  verbinden);
toch.  A  tsopats  ,groß',  täppo  ,Mut',  tpär  ,hoch',  B  tappre,  täpr-  ds., Pedersen  Toch.  243,  Toch.  Sprachg.  23,  27,  29,  Van  Windekens  Lex.  135, 148.    Zweifelhaft.
WP.  I  850,  WH.  I  437.
240
dhebh-,  dbebh-eu-  ^beschädigen;  verkürzen,  betrügen',  die  nasalierten  Fori (*dhembh-)  sind  als  proportionale  Neubildungen  nach  -^i-haltigen  Wurzel zu  verstehen.
x-Vi.  dahhnöti , beschädigt,  versehrt,  betrügt,  Pass.  nimmt  Schaden'  (*dhebl n-eu-ti),  Perf.  daddbha  und  (geneuert)  daddmhha,  Partiz.  Perf.  Pass.  dahdl und  (von  der  Wurzelform  auf  -u:)  d-dhlm-ta-  Adj.  ,wunderbar',  eigentli( ,*der    Täuschung    unzugänglich,     unantastbar';     damhhdyati    ,macht   aj schänden'    {damhhd-h    ,Betrug'),    Desid.    dipsati   (=  av.   dhv^-.    s.   unten] dabhrd-  ,wenig,  gering,  dürftig';
av.  dab'  ,betrügen,   um   etwas   bringen' :  davqi-d-yä  G.  Sg.  f.  ,der  betrl genden',  davayeinü  N.  Sg.  f.  ,die  betrügende',   ddbdnaotä  2.  PI.  Präs.  (a *dbha7icm-mi,  idg.  *dbh-en-eumi'),  Inf.  diwiaidyäi  (ohne   desiderative  B( mehr,   aber  =  ai.   dipsa-ti),  Partiz.  Perf.  Pass.  dapta-  (Neuerung);  d^l vayat  ,er   soll   betören'   (Wzf.  *dbheu-)j   a-ddbaoman-  n.  ,Betürung';  oss3 dawin  , stehlen';   hitt.  te-ip-nu-  , gering  achten',  Pedersen  Hitt.  144.
Dazu  sehr  wahrscheinlich  gr.  äzcfißco  ,beschädige,  beraube,  verküra (dvi.i6v)y  verwirre,  täusche',  Pass.  ,bin  beraubt',  mit  d-  wohl  aus  *ä-,  *
=== POK_01 leaf 251 ===
srri-xtm mit  demselben  Konsonantenverhältnis  wie  zwischen  nvvda^ :  ai.  budh-nd-\
WP.  I  850  f.,  Kuiper  Nasalpräs.  147,  Schwyzer  Gr.  Gr.  I  333.
dheg^h-  ^brennen';  Nominalbildungen  dti6g^ho-s,  dheg^h-ro-s.
Ai.  ddhati,  av.  dazaiti  , brennt'  (=  lit.  degü^  aksl.  zegg,  alb.  djek)^  Partiz. ai.  dagdhd-h  (=  lit.  degtas),  Kaus.  dähdyati]  däha-h  ,Brand,  Hitze',  nidagha-]^ , Hitze,  Sommer',  npers.  däy  , Brandmal'  (dazu  spätgr.  ödyalog,  -ig  ,rot- braunes  Pferd'?);  av.  daxsa-  m.  ,Brand';
gr.  d-emavog'  ä7tTÖ{,isvog  Hes.  (,angezündet';  =  lit.  degtinas  ,wer  oder was  zu  verbrennen  ist'),  tscpqä  , Asche'  (*dheguhra)]
alb.  djek  ,verbrenne,  brenne  an',  Kaus.  dhez,  n-dez  .zünde  an'  (Gdt *dhoguheiö  =  lat.  foveö)]
lat.  foveö,  -ere  ,wärraen,  hegen,  pflegen',  föculum  ,Feuerpfanne'  {^'foue- clom),  fömentum  ,ein  erwärmender  Umschlag'  {*fouementom)j  fömes,  -itis , Zunder'  (*fouemet-j  Bedeut.  wie  lett.  daglis),  favilla  , Asche,  bes.  noch glühende'  (wahrscheinlich  aus  *dhogi^h-lo-lä):  favöniiis  ,der  laue  Westwind' (aus  ^-fovönios)'^  febris  ,Fieber'  C^dheguhro-;  nach  Leumann  Gnom.  9,  226 ff. die  i-Flexion  nach  sitis).
Mir.  daig  (Gen.  dega)  ,Feuer,  Schmerz'  (aus  *degi-)]  über  mbret.  deuijf, nbret.  devi,  cjmr.  deißo  ,brennen'  s.  unter  *<^äw-, brennen';  cymr.  de ,brennend'; go-ddaith  ,Brand'  (aus  "^-dekto-)]  aber  air.  ded-öl  ,Morgengrauen'  nach Mai-strander  Dict.  Ir.  Lang.  I  213  eigentlich  .Abschiedstrunk,  letzter  Trunk'; nir.  dogha  ,Klette'  (:lit.  dagys  s.  unten);
über  got.  dags  ,Tag'  usw.  s.  unter  '^'ügher-  S.  7:
241
.  lit.  degu,  degt'i  .brennen'  (trans.  und  intrans.);  degtas  .gebrannt',  degtinas xras  25U  verbrennen  ist',  degüne  f.  .Branntwein',  ablautend  dagys,  dägis 'oistel'  (lett.  dadzis);  dägas  .das  Brennen;  Sonamerbitze;  Ernte',  dagä  .Ernte', ipr.  dagis  .Sommer';  lit.  däglas,  .brandfarben',  deglas^  .schwarzscbeckig-; lott.  daglas  f.  PI.  .Brandfleck',  daglis  .Zunder';  lit.  nuodegulis  .Feuer- brand'; degis  »Brandwunde';  ablaut.  atüo-dogiai(?)  m.  PI.  .Sommerweizen';
sloven.  djgniti  .brennen,  wärmen',  cech.  alt  dehna  .Teufel',  ablaut. Jahneti  .brennen';  russ.  degoth  .Teer'  (aus  .*harzreicbes  Holz'),  wie  lit. degtitas  .Birkenteer';  mit  Assimil.(?)  von  *degg  zu  "^gego:  aksl.  zegg,  zesti ^brennen',  ablaut.  >uss.  iz-gdga  .Sodbrennen'  (s.  Meillet  MSL.  14.  334  f., anders  Brugmann  II ^  3.  120).
Tocb.  B  teki  .Krankheit'  (=  ir.  daig)'^  A  tsäk-,  B  tsak-  .brennen',  das i8  nach  dem  ablaut.  tsäk-  {*dheguh-)  .glänzen,  glühen';  AB  cok  , Lampe' (aus  .Kienfackel')  :  bsl.  *degut-  .Teer'  (s.  oben).
WP  I  849  f.,  WH.  I  466  f..  469.  471  f..  864.  Trautmann  49.  Pedersen Tech.  Sprachg.  23.
äbS(i)'  (daneben  dh-ei-  ?)  .saugen,  säugen'  ( :  c?Äai-.  dJvt-  und  dhe-j  dhd-)  s
```


## [2026-09-05T18:15:34.092Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 252 253; do echo \"=== POK_01 leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt; done",
 "description": "Print Pokorny p.241-242"
}
```


## [2026-09-05T18:15:34.617Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 269 270; do echo \"=== POK_01 leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt; done",
 "description": "Print Pokorny p.259"
}
```


### [2026-09-05T18:15:35.790Z] TOOL RESULT

```
=== POK_01 leaf 252 ===
. bes.  Schulze  KZ.  27.  425  =  Kl.  Sehr.  363.  Nominalbildungen:  dhe-lä .Mutterbrust',  dhi-lo-  , Zitze',  dbe-lu-  .säugend'.  dbQi-l-  ds.,  dhei-nä .trächtig',  dhe-nä  .Fruchtertrag',  dhedhn-  .(saure)  Milch'. Ai.  dhäya-h  .ernährend,  pflegend',  dhäyas-  n.  .das  Saugen',  dhäyü-  .durstig'. dhätave    .zu    saugen',    Fut.  dhäsyati,    i^or.    ddhät   ,er    sog',    su-dhä    .Saft, Nektar',  dhätrl  .x4mme.  Mutter',  dhenü-  f.  .milchend'  =  av.  daenu-  .Weib- chen von  vierfüßigen  Tieren',  ai.  dJiBnä  .Milchkuh',  ablaut.  dhud-  .gesogen*^, Perf.  Plur.  1.  3.  da-dhi-md  (i  =  »),    da-dh-üh]   redupl.   Nomen    da-dh-an-j Nom.  dd-dh-ij  Gen.  dadhnds  .saure  Milch'  (:  apr.  dadaUj  alb.  djathej'j
vom  Stamme  dhoi-:  dhdyati  .saugt'  (*dh^ieti  :  Kaus.  *dhoi-4ie-ti  in slav.  dojiti,  got.  daddjan)  und  dhinöti  .nährt';
arm.  diem  .sauge'  (^  =  idg.  e  oder  eher  l,  so  daß  =  anord.  dia),  stn-di ,(Brust  saugend  ==)  Säugling',  dal  aus  dail  ,Biestmilcli'  (dhdi-li-)^  dayeak ,Amme'  (von  *dayi-  =  idg.  dhd-ti-)]
gr.  d-TjoaTo  .er  sog',  d^rja^at  .melken',  ^rjVLOv  ,Milch',  TL&rjvrj  ,Amme' (Kurzform  zlrd-rj  u.  dgl.,  worüber  anders  Falk-Torp  u.  taute),  yaXad-rjvög .Milch  saugend'.  n-d-aGÖg  ,zahm,  kultiviert';
alb.  djathe  .Käse'  ursprüngl.  ,aus  saurer  Milcb  gemachter  Quark'  (:ai. dddJii),  gr.-alb.  dithe  ,Käse';
lat.  femina  .Frau'  (,*die  säugende');  über  felix,  fecundus  s.  unten; air.  dinu   ,Lamm',    dlth   ,suxit'   {}  =  idg.  e   oder  i),    denaid   ,er   saugt' {*di-na-ti),  bret.  denaff  ,sauge',  cjmr.  dynu  .saugen';
16
242
got.  daddjan  =  8isc\iwed.  dceggja  ,säugen'  (urgerm.  *dajjan,  vgl.  ai.  dhdyat aksl.  dojo]  das  germ.  *dajj-  ist  regulär  aus  *dhoi-eie-  entstanden),  aschw« dla,   d'ä.n,  norw.  die  , saugen',   mhd.   dien,   tlen  ,säugen;    die  Brust   gebe^ (vgl.  0.  arm.  diem),  hochstufig  ahd.  täen,  Präs.  täju  (=  lett.  deju  ,sauge' Avestfäl.  däierrn  ,ein  Kalb  mit  Milch  auffüttern'  (Holthausen);
lett.  deju,  det  ,saugen',  at-diene,  at-diemte  ,eine  Kuh,  welche  im  zweite] Jahr  kalbt',  lit.  dieni  f.  ,trächtig'  (=  ai.  dhenü-),  dienä  ds.  (=  ai.  dhenä  ,Kuh*3 apr.  dadan  , Milch'  (=  ai.  dadJian-)]  aksl.  dojg  ,säuge'  (ai.  dhdyati),  doilicQ ,Amme',  mit  e  (=  idg.  e  oder  9i)  däth  f.  ,Kinder',  deva,  devica  ,Määchen Jungfrau'  (verschoben   aus   ,*Weib'  =  ,die  säugende',    s.  Berneker  197);
Mit  i-Formantien:   Ai.    dhärü-  ,saugend'  =  gr.  ^fjXvg  ,nährend  {isQSijJl säugend,    weiblich'    (fem.    d^r^leia    und    d-^lvg)^    ^^Xw,    -d^rjXa^tbv   ,Aminef d-r^laCo}  ,säuge,  sauge',  d^rilrj  ,Mutterbrust',  alb.  dele  , Schaf  {*dhdil-n-),  dek ds.,  dhalle  , saure   Milch',   illyr.  dalm-  , Schaf  in  ON  JdX^iov,  Jelixivio^ VN  Dalmatae,  Delmatae,  messap.  PN  Gen.  m.  dalmaihi,  fem.  PN  dalmad-oa' lat.  felö,  -äre   ,säugen',  fllius   ,Sohn'   (,*Säugling',   aus    *felios)  =  umbr^ fel
=== POK_01 leaf 253 ===
iuf,  filiu  ,lactantes';   mir.  del  , Zitze'  (*dhi-lo-),  delech  ,Milchkuh',  danT dcel  , Milchdrüsen  oder  Euter  bei  der  Sau',  schwed.  mdartl.  del  m.  jZitze*^ ahd.  tila  f.  ,weibliche  Brust',  ags.  delu  f.  ,Brustwarze,  Zitze',  anord.  dilkrl ,Lamm,   Junges';   lett.   dels   ,Sohn',  dele    ,Blutegel',    lit.  dele    ds.,  pirmdell '^ ,die  zum  ersten  Male  geboren  hat',  pirmdelys  ,was  gerade  geboren  worden ist';  lett.  dile  ,saugendes  Kalb',  dllit  ,säugen'.
Ob  gr.  d^tjad-ai  {^d^wisad-ai) , schmausen',  d^oivi]  ,Schmaus'  (aus  *d-(x}L-vG?) mit  Abtönung  hierher  gehöre,  ist  fraglich;  ob  d-Co^ai  und  (dor.)  d-a^ai ^lied-vaai^  als  ^d^oia'/.-(Jai  auf  eine  leichte  Wz.  *dhÖi-  (ebenso  dann  d^oirt]] auch  d'üJa-d'aL  kann  d-oia-od-ai  sein)  weisen?
Lat.  felix  , fruchtbar,  glücklich'  zu  feläre  geht  auf  ein  fem.  Subst. *fell-c-  ,die  säugende  =  fruchtbare'  zurück,,  nach  Specht  (KZ.  62,  237) aus  '^felui-k-s,  Femin.  zu  ai.  dhäru-,  gr.  d-fjXvg',  lat.  fecundus  ,fruchtbar^, fetus,  -üs  ,das  Zeugen,  Gebären',  feta  , schwanger,  trächtig',  auch  ,was geboren  hat',  effeta  , durch  vieles  Gebären  geschwächt',  fenus,  -oris  , Er- trag, Zinsen,  Wucher',  vielleicht  auch  fenum  ,Heu'  (als  , Ertrag')  erklären sich  aus   einer  Sonderanwendung  von   dhei-  , säugen'  für  , fruchtbar  sein';
dazu  aber  nicht  *dhönä-  , Getreide'  :  ai.  dhänäh  f.  PL  , Getreidekörner', dhänyd-  n.  , Getreide',  np.  däna  ,Korn',  av.  dänö-karsa-  ,eine  Ameisenart', d.  i.  , Körner  (=  Ameiseneier)  schleppend',  toch.  B  tano  ,Getreide'  und lit.  ddona,  lett.  duona  f.  ,Brot'  (ursprüngl.  , Getreide',  alit.  , Ausgedinge'); dor. -illyr.  (kret.)  ÖTjal  .  .  .  ai  KQid^ai  EM.,  örjTTcci'  al  inTLGf.i€vaL  xQi&ai (*c?Äe-Ä;-ia-)  Hes.;  anders  Jokl  bei  WH.  I  475;
s.  auch  oben  1.  dhe-,  dhe-dhe-.
WP.  I  829  ff.,  WH.  I  474  ff.,  864,  Trautmann  51.
245
.  rihiä-  :  dhi-  .sehen,  schauend -     *Ai.    ddldhet   ,Qr    schaute',    PL    dldUmah,    Med.   didhye,    ddldkUa,    Konj. thdhayat  (vielleicht  zum  Präs.  umgewandeltes  Perf.,  vgl.  Perf.  dldliaya)'^ jf^ya-th  dhyä-ya-ti  (lO-Präs.)  ^schaut  im  Geiste,  d.  i.  denkt,  sinnt',  Partiz. »j^yj.^rt-und  dhi-tä-,  dhyä  ,das  Denken,  Sinnen',  dhyä-tar- , Denker^,  dJiyä-na- „    ,das   Sinnen,   Nachdenken',   dhyäman-  n
```


### [2026-09-05T18:15:37.487Z] TOOL RESULT

```
=== POK_01 leaf 269 ===
  (dherobh-?)  ,arbeiten'.
Arm.  derbuk  ,rough,  stiff,  rüde';
ags.  deorfan  st.  V.  ,arbeiten;  umkommen',  gedeorf  n.  ,  Arbeit,  Mühsal', afries.  for-derva,  mnd.  vor-derven,  mhd.  verderben  ,umkommen',  auch  Kaus. ^verderben';
lit.  dirbu,  dirbti  , arbeiten',  ddrbas  , Arbeit',  darbüs  ,arbeitsam'.
WP.  I  863,  II  631,  Klügelt  101,  649,
dherebh'  , gerinnen,  gerinnen  machen,  ballen,  dickflüssig'.
Ai.  drapsd-h  m.  ,Tropfen'??;
gr.  TQeqisad-ai,  Tstqocpevai  ,gerinnen,  fest  sein',  XQecpu),  dor.  rgdcpco  , mache gerinnen  (ydXa]  tvqöv),  nähre  (*mache  dick,  feist),  erziehe'  (^QeipWy  ed-gstpa), tQocpög  ,nährend',  f.  ,Amme',  d-qe^if-ia  ,das  Genährte,  Pflegling,  Kind, Zuchtvieh',  TQOcpig  ,feist,  stark,  groß',  TQOcpallg^  -Idog  , frischer  Käse,  ge- ronnene Milch',  Taocpvg  , dicht',  rdgcpea  PI.  n.  , Dickicht',  TQacpeqr]  (yfj) ;festes  Land';
nasaliert  und  mit  idg.  b  (idg.  Artikulationsschwankung  in  nasaler  Um- gebung) d-QOi-ißoq  ,geronnene  Masse  (von  Milch,  Blut  usw.)',  ^go^ßdof-iai jgerinne',  d-QOfißeTov  ,Klümpchen';
17
268
as.  derli   (*dartia)  ^kräftig;   böse^^   afries.   mnd.   derve  ^derb,   gerades (verschieden  von  ahd.  derh  ^ungesäuert'  =  anord.  pjctrfr),  ablaut.  anor^ djarfr  , mutig,  kühn'  (die  ältere  Bed.  noch  in  norw.  dial.  dirna  aus  *c?iVa3I ^zunehmen;,  wieder  zu  Kräften  kommen');  anord.  dirfa  , ermutigen';
nasaliert  wohl  anord.  dramh  , Übermut'  (*dick  sein),  nisl.  dramhr  ,Knoteni im  Holz';  anord.  drumhr  , Klotz';  mnd.  drummel  ^gedrungene  Person'.
WP.  I  876.
dheregh-  mit  Formans  -(e)s-  und  -no-  in  Namen  beerentragender  strau- chiger Pflanzen,  bes.  auch  von  solchen  Dornsträuchern,  woraus  z.  t1 ,Dorn'?    Zweifelhafte  Gleichung.
Ai.  dräksä  ,Weintraube';
gallorom.  *dragenos  ,Dorn*,  air.  draigen  m.  , Schlehdorn*,  cymr.  drae^ m.,  nbret.  di^ean  , Dornstrauch'  (kelt.  "^drageno-  aus  *dhr^gli-)'^
vielleicht  auch  ahd.  tirn-pauma  ,cornea  silva*,  tyrn,  dirnhaum  ,cornus*^^ nhd.  dial.  di(e)rle,  dirnlein  ,Kornelkirsche',  Schweiz,  tierlij  falls  nicht! aus  dem  Slav.  in  sehr  alter  Zeit  entlehnt;
lit.  dngnes  PL,  lett.  drigenes  ,schwarzes  Bilsenkraut'  (vgl.  Mühlenbach-1 Endzelin  I  498),    falls  nicht  aus  dem  Slav.  entlehnt;
russ.  dereuj  deren  , Hartriegel,  Kornelkirsche',  skr.  drijen,  öech.  drin  ds. poln.  (alt)  drzon  jBerberitze',  kaschub.  drbn  , Dornen',  polab.  dren  ,Dorn'.
Germ.-sl.  Grundf.    kann   "^dherghno-   sein    und    stünde    dem   freilich   in seiner   Bed.    , Schößling,    Zweig',    PL  ,junges    Gebüsch'    erheblich    anders- gefärbten gr.  TQ€xyog  (Hes.,  anthoL),  tsqxvoq  (Maximus),  kypr.  t«  zsQxvija  ^  • sehr  nahe.
WP.  I  862  f.,  Pedersen  KG.  I  97,  M.-L.  2762.
dheregh-  {dhrgh-nä-)  , drehen,  winden,  wenden'  (auch  , spinnen,  nähen*).
Npers.  darz,  darza  ,Naht*,  darzmän,  darznän  , Faden*,  darzan  ,NadelV pehl.  darzik  , Schneider';
arm.  dafnam  (*darjnam),  Aor.  darjay  ,sich  wenden,  sich 
=== POK_01 leaf 270 ===
 drehen,  sich kehren;  zurückkehren*,  dafn  , bitter,  herbe*  (vgl.  oivog  zgerrsTac  u.  dgl.), darj  jWendung,  Umkehr,  Rückkehr*,  Kaus.  darjucanem  ,verto,  averto, converto,  reddo*;
alb.  dreth  (St.  *dredh-),  Aor.  drodha  ,umdrehen,  zusammendrehen, zwirnen,  spinnen*,  alb.-skutar.  nnrize  ,Windel*  (n-dred-ze)-  nach  Pedersen Hitt.  123,  125,  Toch.  Spracbg.  20  hierher  hitt.  tar-na-ah-hi  ,ich  stecke ein,  lasse  hinein*,  toch.  A  tärnä-,  tärk-,  Prät.  A  cärk,  B  carka  , lassen, entlassen'  (?).
WP.  I  863,  Liden  Arm.  St.  101  ff.,  Meillet  Esquisse^  111,  Kuiper  Nasal- präs. 151.  '^^
259
dbers'  , wagen,  kühn  sein',  älter  ,angreifen,  losgehen*  (auch  mit  -i-,  -u- erweitert).
Ai.  dhrs-nö-ti,  dhdrs-ati  ,ist  dreist,  mutig,  wagt',  ährsü-  (Gramm.),  dhrsat Jierzhaft'  (=  av.  dard^at),  dhrsnii-  ,kühn,  tapfer,  mutig,  dreist,  frech', dhfstd-  ,keck,  frech',  dhfsüa-  ,kühn,  mutig',  dädhrsi-  ,beherzt,  kühn',  mit Objekt  dharsayati  ,wagt  sich  an,  vergreift  sich,  bewältigt',  dharsana-  n. , Angriff,  Mißhandlung',  dharsaka-  ,angreifend,  über  etwas  herfallend';  av. darsam  Adv.  ,heftig,  sehr',  darsi-,  darsyu-,  darsita-  ,kühn',  apers.  adar^- nau§  ,er  wagte',  dädarsi-  EN;
gr.  lesb.  -d-sgaog  n.  ,Mut,  Kühnheit'  (hom.  QsgalTrjg  ,Frechling'),  mit aus  dem  Adj.  verschleppter  Tief  stufe  ion.  altatt.  d^ccQOog  (att.  ^agoog)  ds., att.  d-gdaog  n.  ,Mut,  Kühnheit;  Verwegenheit,  Frechheit',  d-aqüeu),  d^aggeo) ,bin  mutig',  S-agavg  (rhod.  QaQGvßiog,  ther.  Qhagvfxaqhog),  d-gaavg  ,kühn, mutig;  verwegen,  frech'  (=  ai.  dlifsu-),  lesb.  Adv.  -S^goaecjg,  Mgavvog mutig,  getrost,  vertrauend'  (*-9-ag(To-avvog)]
lat.  infestus  , feindlich*,  infestäre  , feindlich  behandeln,  angreifen'  und manifestus   , handgreiflich,   auf  der  Tat  ertappt;    offenkundig'   (*dhers-to-)]
got.  ga-dars  ( :  ai.  Ferf .  dadhdrsa  ,hat  sich  erkühnt'),  Inf.  gadaürsan,  ,ich wage',  as.  gidurran,  ags.  dear^  durran,  ahd.  {gi)tar,  (gi)turran  ,wagen',  ahd. giturst,  ags.  gedyrst  f.  , Kühnheit,  Verwegenheit'  (=  ai.  drsti-h  ,Kühnheit');
lit.  nasaliert  lit.  dresü  ,wage*  (*dhrensö),  dristü,  dristi  {dhrns-)  , wagen', drqsä  (*dkrons-)  , Dreistigkeit',  di-qsüs  =  lett.  drüoss  ,mutig'  (*dhrons-j alit.  noch  drisüs  und  draiisniaus)]  ohne  Nasalierung  apr.  dirstlan  , stattlich* und  dyrsos  ,tüchtig'  (*dirsu-);
hierher  vielleicht  toch.  A  ^sär  ,rauh',  tsrasi  , stark',  B  tsirauüe  , Stärke*.
WP.  I  864,  WH.  I  698  f.,  Trautmann  60,  Van  Windekens  Lexique  147.
dbes-,  dhos-  in  religiösen  Begriffen.
Arm.  di'Jt  , Götter*  (PI.  *dheses)',  lat./eWae  (alat. /esiae)  ,Tage,  an  denen kei
```


## [2026-09-05T18:16:04.416Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Getreidekörner\" POK_full.txt POK_0*.txt | head -20; echo ---; grep -n \"dhonā\\|dhōnā\\|dhǝnā\\|dhona-\" POK_full.txt | head -20",
 "description": "Grep Pokorny for grain root"
}
```


### [2026-09-05T18:16:04.484Z] TOOL RESULT

```
POK_01.txt:3434:dazu  aber  nicht  *dhönä-  , Getreide'  :  ai.  dhänäh  f.  PL  , Getreidekörner', dhänyd-  n.  , Getreide',  np.  däna  ,Korn',  av.  dänö-karsa-  ,eine  Ameisenart', d.  i.  , Körner  (=  Ameiseneier)  schleppend',  toch.  B  tano  ,Getreide'  und lit.  ddona,  lett.  duona  f.  ,Brot'  (ursprüngl.  , Getreide',  alit.  , Ausgedinge'); dor. -illyr.  (kret.)  ÖTjal  .  .  .  ai  KQid^ai  EM.,  örjTTcci'  al  inTLGf.i€vaL  xQi&ai (*c?Äe-Ä;-ia-)  Hes.;  anders  Jokl  bei  WH.  I  475;
POK_02.txt:3577:dazu  als  ,Decoct'  auch  cremor  ,der  aus  aufgeweichten  Getreidekörnern oder  sonst  aus  Pflanzen  gewonnene  Saft,  Brei' ;  ferner  gall.  ytÖQixa,  xovgfii, air.  coirm  n.,  mcymr.  cwrwf,  acorn.  corefj  coruf  ,Bier',  wozu  vielleicht ai.  karam-h{h)d-  m.  , Grütze,  Brei',  kulmäsa-  m.  .saurer  Schleim  von Früchten,  saurer  Reisschleim';  vgl.  ferner  toch.  B  kark-,  kärk-  .braten, rösten'.
---
```


## [2026-09-05T18:16:06.060Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN p.122 (leaf 143) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==144' HRN.txt | head -60; echo \"=== HRN p.119 (leaf 140) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==141' HRN.txt | head -60",
 "description": "Horn pages 119 and 122"
}
```


### [2026-09-05T18:16:07.797Z] TOOL RESULT

```
=== HRN p.122 (leaf 143) ===
— 122 —
Anm., Ar. Forsch. III, 22 Anm. 2) geben. Skr. djfdhä-
müsste also aw. *dereMa- entsprechen.
duriixs s. unter direfs (No. 553).
549. dei*:^, derze 'Naht', derzmän, demen, derzl (syr. LW.
pm), Käään Q.K. darzln 'Nadel' ').
g. dastmün, he-darze 'ich nähe*; Kjiö. hidastdn,
oadasten, vödastemän (S. 126).
aw. dereza- 'Fessel*, l/^rfar^-2f- 'festmachen'; ai. [y^darh-,
cte/fAöv/a-* befestigen', arm. (Zer/c/ifc 'Schneider (Schuster)*,
derjan 'Faden', handerj 'Kleid' (Hübschmann, No. 81).
oss. dares 'Kleid' (101).
Wahrscheinlich gehört np. enderz 'Rat, Ermahnung*
(phlv. andarj bezw. andarz) zu derselben Wurzel (mit
Praellx ham),
550. (lerd 'Schmerz'.
Wohl zu ai. 1 [/^dar- 'spalten, zerreissen, bersten
machen* (Hörn); vergl. got. tairan, ahd. zeraii, nhd.
zehren,
phlv. d(irt (vd. 20 (13)), dartak 'geplagt' (AV.); arm.
vergl. trtnm 'betrübt* (?) (Hübsch mann No. 278).
LW\ kurd. bei. (47) dard.
Nöldeke (mündliche Mitteilung) möchte derd zu
np. äzar (No. 20) stellen.
551. darust 'gesund, richtig, duriistl; vergl. tendumstX
aw. ^drva- + asti- gesunden Leibes* , oder wohl
besser drva- + sü- (vergl. aw. ayösti-), wie mir Bar-
tholomae vorschlägt; ap. diiruva- 'gesund'; phlv.
duritst^ durustih; ai. dhncvd- 'fest, bestimmt, bleibend'.
LW. kurd. durust 'wahr'; bei. driist 'voll, ganz,
vollständig' (86); wa/. drust, driist 'ganz, vollständig.
Anders Fr. Müller, WZKM. 5, 66; vergl. aber
unter np. dire/t (No. 548).
552. durust 'rauh, grob, stark, durustt,
ap. iXrfars- 'wagen', adarmans, darsma 'heftig, sehr';
aw. \/dar€S' 'wagen', darsi-; ai. \/dharS', dhfmoii
'J Unter sozen (Öcitc HDJ.
=== HRN p.119 (leaf 140) ===
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
diwcr (Men.) stimmt, wird durch den Reim bezüglich
ihres e beseitigt (debtr reimt auf plr, Vfs und Rcämln,
S. 23, V. 6, auf gir Sahn. III, 1452 Vers 142)2). Den
Zusammenhang mit dtwän, defter (phlv. daftar nur in
späten Kolophonen) hat bereits de Lagarde (Ges.
Abh. 216) erkannt.
54 L diiy^ter, du/t 'Tochter'.
aw. diiydar- 'Tochter'; phlv. dtt/t^ vergl. arm.
Tif/rana]du/t; ai. dtihitdr-; arm. ditstr (Jl. No. 87).
kurd. du/t, ditt; af/. lär; wa/. da yd, sangl. da/,
minj. loyda.
*) In Vis und Rämln findet sich am Versende auch däyeyän
*Aniuie* (z. B. S. 20 Vers 13, 21 Vers 2 v. u., 22 Vers 5 v. u.), mit
Suffix -gän^ wie in x^idälgät?, bäzärgän^ bendegän (E[»igraphia indica
II, 151 No. 38 u. ü.) u. a. m.
V
^) Die alte Londoner Handschrift des Sähnäme reimt III, 151G
Vers 336 allerdings deber auf Ardeser, wie Daqiqi im Gegensatz zu
Firdsdsi sprach (Nöldekc, Pcrs. Studien, II, 2, Anm.).
```


## [2026-09-05T18:16:20.946Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN p.123 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==145' HRN.txt | head -40",
 "description": "Horn page 123"
}
```


### [2026-09-05T18:16:22.554Z] TOOL RESULT

```
=== HRN p.123 ===
— 123 —
Als eine Bestätigung für diese Etymologie dient der
Umstand, dass Herr Prof. Nöldeke mir dieselbe
ebenfalls mitteilte; er war besonders von ai. (Ißtä- in
der Bedeutung *keck, frech' ausgegangen ^).
553. direfS Fahne, Banner'.
aw. drafsa- 'Banner -); phlv. draß^ arm. LW. draus;
ai. drapsd' 'Tropfen*.
oss. LW. (jrisa Tahne (von JStackelberg, Fünf
oss. Erz. 81).
Die ursprüngliche Bedeutung von ar. drapsd- ist
unsicher; Fick, Vorgl. Wörtbch. ^ I, 241, setzt
zweifelnd 'flutend, wallend' als solche an. Np. direfs
soll auch *Blitz, Glanz' bedeuten, vergl. direßän,
direfsiden, jüd.-pers. t^l^E»*!"! (Is. 41, 25) (phlv. draßntk
zitternd', AV. , drafset Bund.); in dieser Bedeutung
scheint ein Zusammenhang mit np. duru/s (so hiutet
die ursprüngliche Vokalisation), diiriiysün, duruyßlden
V
vorhanden zu sein, wie denn auch im 8<ähnäme oft
die Formen in den Varianten durcheinander gehen
(z. B. I, 107 Vers 839). Duriiyß etc. halte ich für
Composita, wohl mit Praep. ati, deren zweites Glied
ruys (No. 610) ist.
551. derniän *Arzenei', vergl. darß (No. 523), dermene'^)
^Absinth'.
i^dhar- 'halten', vergl. aw. drva- gesund'; phlv.
darwan 'Arzenei'.
LW. kurd. af/. bei. (48) darmän,
555. durüd, duröd (8ähn. I, 50 Vers 301, 170 Vers 751),
'Segenswunsch, Gebet'.
*j Vergl. auch SFgnirt^? *Frecliling*.
'-) *Banner', nicht Waife, wie Darmes t et ci-, Et. ir. II, 273 über-
Hetzt. Auch im Sähnäme heisst direfs niemals Lanze'. Mand. LW.
Nii^£»NT1 bedeutet *Kreuz* (Nöldeke, Mand. Gramm. 309 Nore i).
Greldner^s Übersetzung von aw. (jaos drafsö (y. 10, 14J durch
*ein Tropfen Milch* (Metrik, S. 153) ist schwerlich richtig (s. Ausgabe).
^) dramna (Bund), syr. LW. ^^O")*!-
```


## [2026-09-05T18:16:22.582Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','SOD','KNT','SYN']:\n  v=d[k]; print('===',k); print('offset:',v.get('page_offset')); print('hint:',v.get('lookup_hint')); print('local:',v.get('local_file'))\n\"",
 "description": "Offsets for BQT SOD KNT SYN"
}
```


### [2026-09-05T18:16:24.448Z] TOOL RESULT

```
=== BQT
offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
=== SOD
offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}
local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
=== KNT
offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
=== SYN
offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
```


## [2026-09-05T18:16:30.596Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT p.190 (leaf 205) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==206' KNT.txt | head -70; echo; echo \"=== grep dars in KNT ===\"; grep -n \"dar[sš]\" KNT.txt | grep -i \"wag\\|dare\\|bold\" | head -20",
 "description": "Kent p.190"
}
```


## [2026-09-05T18:16:31.521Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN p.1149 (leaf 1173) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1174' SYN.txt | head -70",
 "description": "Buck p.1149"
}
```


### [2026-09-05T18:16:32.233Z] TOOL RESULT

```
=== KNT p.190 (leaf 205) ===
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
OLD PERSIAN
*flu-); Sen 247, 251, has wrong meanings. Р}.
sani, Acme 1.319-20, gives another etymology, -
See also uzsnav-.
z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
gaifa- sb. ‘(living) personal property, cattle’: Av. gaébü- ‘individual living being, pl. world; household, property’, РЫ. géhdn ‘world’ (from gen, pl.), to root pIE *g*ei- seen in OP jiv- (869, $101, $151). For varying interpretations, see Tm. Lex, 85, with lit. — ga26àm-cà (S89) asf. DB 1.65.
gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
Gaubarwa- sb. ‘Gobryas’, ally of Darius against Gaumata: Flam. kam-bar-ma, Akk. gu-ba- ru-’, Gk. TwBpins; from gav- ‘cattle’ + *baruva-, cf. Skt. bharu- ‘lord’, to vb. bar- ($85.П, $101, $122, $142, $143.II, $150, $1581, $160.Ib): ‘Cattle- Possessor’ (Justi, IFA 17.111; otherwise Foy, ZDMG 54360). Gaubaruva nsm. DB 4.84; 5.7, 9, 11; DNe 1.
Gaumdta- sb. ‘Gaumata’, Median pretender who took the name Smerdis ($164.I): Elam. kam- ma-ad-da, АКК. gu-ma-a-lá; from gav- ‘cattle’ + pte. mdta- of unknown meaning ($242.II). Gau- mata nsm. DB 1.36, 44, 46, 64, 65, 70; 4.7; DBb 1f. Gaumdiam asm. DB 1.49f, 54, 57, 73; 4.81.
gausa- sb. ‘ear’: Av. gaosa-, NPers. gas, Skt. ghóga- ‘noise’; Iran. root *gaus- ‘hear’, pIE *gheus-
(670, 5101, $1431). диа adm. ($189) DB 274, — |
| КИ adven as n Le ЧЕР Г PERDE :
ок ALES
e
LESIN EI EOE PE EERE СООТУ
I aen i bag ih oea CAU Lin aE M iig Án
LEXICON
89. gaušāyā idm. (5189; with sg. ending, Lg. 19.225) DNb 53.
gafu- sb. ‘place, throne, place of battle’
(JNES 4.49-50): Av. gdtav- дабш-, NPers. gah, Skt. gütu-, to pAr. root gam-, pIE *g*em- ‘come’ ($68, $81, $158.11, §179.n2). давит asm. DNa 41f. дйбарй lsm. ($137, $182.IT) DB 1.62f, 66, 69; DNa 36; DNb 35 (INES 4.49-50); DSe 36f, 44, 44f; XPf 33 (as abl., $182.III, though without hacé: Lg. 941-6; Ву. BSLP 33.2.148-50; Wb. А 41.319-20; Sehaeder, SbPAW 1935.503; Hz. AMI 4.130-2, 8.45, ApI 177-80), 85; XPh 34.
gad- vb., see jad-.
Ga*dara- sb. ‘Gandara, Gandaritis’, a prov- ince of the Persian Empire: Elam. gan-da-ra, Akk. gan-da-ri. See also Gadáraya-. Сайдта nsm. DB 1.16; DPe 1.18; DNa 24f; DSe 24°; DSm 9°; XPh 25. Gadārā absm. DSf 34.
Ga"déraya- adj. ‘Gandarian’: adj. to preced- ing ($144.III, $167). Gadàraya пзш. APP 12.
Ga*dutava- sb. ‘Gandutava’, a district in Arachosia: Elam. gan-du-ma-+. Cf. Tm. Lex. 86. Gadutava пет. DB 3.66.
gan- vb., see jan-. gand- vb., see gasta-.
gam- vb. ‘come’: Av. gam-, Skt. gam-, Gk. Ваши, Lt. venió, Gt. qiman, pIE g*em- ($101, $244). See also gdéu-.
à + gam- ‘come’: бјата opt. (Skt. gamyat; §67.1, §101, $122, $132.2, $218.11, $293.I, §228.IT) DPd 19.
ava- + gam- ‘go dow

=== grep dars in KNT ===
1128:Final -d disappeared after 1, as in the enel. OP -cly, Skt. cid, pIE q*id; OP лаш ‘not’, Av. лб, from *ne + id. After и the final t seems to be retained as § in OP akunaus ‘he made’, adarsnaus ‘he dared’, Skt. ákrnot ddhysnot; but this § is better taken as an extension of the s of the aorist, after which -t would be lost. The prefix ud ‘up’, which appears unchanged before a vowel in ud- apatatā ‘he rose up (in rebellion)’, suffers com- plete assimilation of the d in uzma- ‘stake’ (from *ud-zma-), and became us- in us-taSand- ‘stair- case’ in the dental cluster (585).
2573:fer from the sigmatic aorist, where the termina- tions would be pIE -?s-m -is-s -is-t, pAr. -isam -iš -1&; the identity of second and third personal forms gives an analogy to the 2d sg. imperfect in -1-$# (no examples extant in OP), whence impf. 3d sg. in 4$. After u the phenomena are the same.? The OP examples are àt$ ‘went’, 0170-07 ‘went past’, aku- naus ‘паде’ (Skt. ékynot), adarsnaus ‘dared’ (Skt. ddhrgnot); and the thematic optatives active vi- ndlayars, passive kariyars fradiyars (cf. for ending Gk. $€po,, Skt. bhdret).
5513:Dàdar&- sb. 'Dadarsh?', (1) an Armenian, (2) а Persian, satrap in Bactria: Elam. da-tur-%-18, Akk. da-da-ar-5u. Репу. of darš- ‘dare’, with re- duplication; Skt. dadhyst- ‘bold’ ($30, §76.III, $152.1, §164.1V). Раат пет. DB 2.29, 31f, 48; 3.18, 15. Dédarsim asm. DB 2.33, 38, 44.
5533:darš- vb. ‘dare’: GAv. dora&- ‘deed of vio- lence’, Skt. dhrs-noti ‘dares’, NEng. dare (570.11, $117). See also Dädarši-, darfam. adaršnauš imf. $80, §84, §210.1, $228.11) DB 1.53.
```


### [2026-09-05T18:16:33.947Z] TOOL RESULT

```
=== SYN p.1149 (leaf 1173) ===
sti refl. shrases for ‘be troubled, care’, e.g. ne pecesi se = 0b pedrer cor, pecase = (Jagié, Entstehungsgesch. 370). Meillet, Etudes 416.
euehev
Brickner 406.
ing dominant.
Russ. zabota, prob. through ‘alarm’ :
Russ. botat’ ‘shake, beat, stamp with the feet’. Cf. Pol. ktopot ‘trouble, anxiety, care’ : ChSl. klopotié ‘noise’. 78. Otherwise Walde-P. 1.530.
Berneker
7. Skt. yatna- ‘effort, pains’ (: yat- ‘strive for’, etc.) is perh. also the best word for ‘care’ as intended here (cintd- is ‘thought’, and ‘care’ = ‘anxiety’).
16.15 WONDER, ASTONISHMENT
Gtk, 0a Bos, Pada, éxadAnkts Goth. sildaleik, afslaubnan Lith. mnusistebejimas, nuste- NG = &xwAnkis ON (undr) bimas Lat, admirdtio, stupor Dan. undren, forundring, Lett. brinums It. maravighia, stupore Sorbavselse ChSl. wzasi% Fr. — élonnement Sw. (for)undran, férvd- SCr.  éudenje, zaprepas- Sp. pasmo ning éenje, didlenje Rum. mirare OE wundrung Boh.  tidiv, vizas a machdad, ingantas ME wonder Pol. zadziwiente ue te NE wonder, astonishment Russ. udivlenie Br thyfeddod, syndod Du. verbazing Skt.  vismaya- poe cOuee, OHG (wuntar) MHG wunder NHG bewunderung (wun-
der),
ae of the words for ‘wonder’ de- =a Fee aly. the obj. ‘wonder’ (‘a ae = something wonderful’), and fr aera mostly through the race a their deriv. vbs. meaning ‘to a » the subj. feeling of ‘wonder’. ‘something based on such notions as Sight? — ae perceived’, (felt as ‘a ‘omething uni worth seeing’), or eto, own or of unusual form’, On th ® other hand, the more distine-
tive Wo tds for the feeling of ‘wonder,
(er)staunen
astonishment? are connected with words for ‘(be) struck, stunned, rigid, dis- placed’, etc., with extension from a phys- ical condition to a mental attitude. In some of these there is interchange be- tween ‘astonishment’ and ‘fear, terror’. ‘Wonder’ may turn to ‘admiration’.
1. Grk. @épBos, rados, beside vb. aor. éradov, perf. rénra ‘be astonished’, etym. dub. Walde-P. 1.824. Boisacq 333.
Grk. @adua (mostly obj. ‘wonder’, but also subj.) : 64 ‘sight, aspect’, fr. *#a-a,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1094 SELECTED INDO-EUROPEAN SYNONYMS
fr. a root *dhdu- beside *dhdi- (?), *dhi- in words for ‘see, look’ (15.51). Walde- P. 1.832. Boisacq 335. .
Grk. éxcraois ‘displacement, change’ (: élornut ‘displace’), hence mental ‘distraction’, in NT ‘amazement’.
Grk. é&mdnéts ‘consternation, terror’, in NG the usual word for ‘astonishment, surprise’, fr. ér\qoow (epd. of mdAqoow ‘strike’) ‘drive out’ and (‘drive out of one’s senses’) ‘astound, frighten’, in pass. ‘be astonished’.
2. Lat. admiratid (‘wonder, surprise’ and esp. ‘admiration’), fr. (ad-)mitrari ‘wonder at’, beside mirus ‘wonderful’, etc. : Skt. sm7- ‘smile’, etc. (16.25). Cf. esp. Skt. vi-smi- ‘be astonished’, vismita- ‘astonished’, vismaya- ‘astonishment’, smaya- ‘astonishment’ and ‘pride, arro- gance’. The development of ‘smile’ to ‘wonder at’ is not too difficult, and the connection is not to be doubted (as by Ernout-M
```


## [2026-09-05T18:16:41.970Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^1149\\|1149 SELECTED\\| 1149$\" SYN.txt | head; echo ---; grep -n \"16\\.4[0-9] \\|BOLD\\|DARE\" SYN.txt | head -20",
 "description": "Locate Buck p.1149"
}
```


### [2026-09-05T18:16:43.809Z] TOOL RESULT

```
---
27444:16.41 Hares (sb.)
27445:16.42 ANGER
27449:16.43 Races, Fory
27450:16.44 Envy, JEALousy
27451:16.45 SHame (sb.)
27452:16.46 Honor (sb.)
27453:16.47 Guiory
27454:16.48 Proup
28579:16.41 HATE (sb.)
28610:1134 SELECTED INDO-EUROPEAN SYNONYMS 16.42 ANGER
28679:see 16.42 under Grk. paves. r biés (> Fr, rage; It. rabbia, In Part, as also Lat. rabiés, tophobia,, rabies’), beside vb. e enraged’, prob. : Skt. rabhas-
28690:16.48 RAGE, FURY
28723:16.44 ENVY (sb.), JEALOUSY
28788:16.45 SHAME (sb.)
28839:N; T{EMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1143 16.46 HONOR (sb.) Goth. swéripa Lith. garbé F rit ON somi, semd, hetdr Lett. guods, ciens “a rib Dan. ere, heder ChSl. éistt, cé&na iat honor Sw. dra, heder SCr. ast " gnore OE Gr, weorpscipe Boh. est * ——_ honneur 2 ME (h)onor, worshipe Pol. czesé, honor ‘ pene hon NE honor Russ. est’, povet oar Ne aria Sa nak, miad, fiad aa A fe rs aa eg ir, ondir MHG @e AV anrhydedd NHG ehre enor ‘honor’ are based on such MIr., Nir. ondir, fr. Lat. honor
28862:16.47 GLORY Grk. __xAéos, 56Ea, Kidos Goth. wulpus Lith. Slove, garbé NG 56Ea ON dyr6, tirr Lett. slava, guodiba Lat. gloria Dan. are, herlighed ChSl.  slava It. gloria Sw. Gra, hdrlighet SCr.  slava Fr. gloire OE wuldor, tir, magen- Boh. _ sldva, chvala Sp. gloria prym Pol. _— slawa, chwala Rum.  slavé, mdrire, glorie ME glorie Russ. slava Ir. gloir : NE glory Skt. — ¢ravas-, yagas- Nir. _— gloir Du. roem, heerlijkheid Av. x¥aranah- W. gogoniant OHG  tiurida, guollichi Br. gloar, hano kaer MHG ruom
28910:16.48 PROUD
28960:16.51 DARE Grk. rodpdw, Bappico Goth. gadaursan Lith. dristi NG roy ON fora, dirfask Lett.  drikstét : Lat.  audére Dan. _vove, turde ChSl. _ siiméti, driizalt It. osare Sw. _ vdga, téras SCr.  smjeti, odvaziti se Fr. oser OE — durran Boh. odvdzilise Sp. osar ME _ durre, dore Pol.  (od)waayé sie, me Rum. indrdzni, cuteza NE dare Russ. smet', derzal’ Tr. ro-lamur Du. wagen Skt. dhrs- Nir. lamhaim, danuighim OHG  giturran OPers. dars- W. beiddio MHG _ turren Br. kredi NHG wagen
```


## [2026-09-05T18:16:47.316Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '28955,28985p' SYN.txt",
 "description": "Buck 16.51 DARE section"
}
```


### [2026-09-05T18:16:47.373Z] TOOL RESULT

```
Pol. dumny, with duma ‘conceit, pride’ : Russ. duma ‘thought, idea, coun- cil, assembly’, etc., Bulg. duma ‘word’, etc., fr. Gme., Goth. dims ‘judgment’, domjan ‘judge’, etc. Berneker 237.
Russ. nadmennyj, fr. ChSl. na-ditment ‘blown up’: ChSl. dima, dati ‘blow’. Berneker 244.
7. Skt. garvita-, with sb. garva- ‘pride, conceit’, perh. as ‘pomposity, weighty manners’: guru- ‘heavy’. Walde-P. 1.684.
Skt. drpta-, also ‘wild, arrogant’, fr. drp- ‘become mad, go crazy’, etym.? Uhlenbeck 129.
lepng, eatly,
16.51 DARE Grk. rodpdw, Bappico Goth. gadaursan Lith. dristi NG roy ON fora, dirfask Lett.  drikstét : Lat.  audére Dan. _vove, turde ChSl. _ siiméti, driizalt It. osare Sw. _ vdga, téras SCr.  smjeti, odvaziti se Fr. oser OE — durran Boh. odvdzilise Sp. osar ME _ durre, dore Pol.  (od)waayé sie, me Rum. indrdzni, cuteza NE dare Russ. smet', derzal’ Tr. ro-lamur Du. wagen Skt. dhrs- Nir. lamhaim, danuighim OHG  giturran OPers. dars- W. beiddio MHG _ turren Br. kredi NHG wagen
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
pmorl n inherited group, verbs ee peed on such varied no-
Ware’ are
fot De aire: undertake, be firm, be tions 8 he eagels have spirit, believe strOne) fidence), have need’. A few (have through risk’? from words for cor with dice’ or ‘wager’. ae +qhers-. Walde-P. 1.864. Feist 1
i fapoéw, Att. Gappew (‘be of good courage, have confidence’, not the com-
n vb. for ‘dare’, but cf. @apcos ‘cour- “I bpacts ‘bold, daring’); Goth. ga- daursan, OH durran, ME durre, dore, NE dare, OS gidurran, OHG giturran, MHG. lturren, nasalized Lith. dristi, lett. drikstét, dristet (on k, ef. Endz., Gramm. 172 ff.); Skt. dhrs-, OPers. dars-.
9, Grk. rohudw ‘endure, submit, un- dertake’ and esp. ‘dare’, beside rédya ‘courage, boldness’ : radkdooa, 7AHvat, etc, ‘bear, suffer, undergo’, Lat. follere lift’, Goth. bulan ‘bear, suffer’, etc. Walde-P. 1.738 f. Ernout-M. 1044.
3, Lat. audére (pple. ausus, whence VLat. *ausdre > It. osare, Fr. oser, Sp. tear), deriv. of avidus ‘eager’ : avére desire eagerly’. Earliest sense ‘desire’, Preserved in si audés, sddés ‘if you like, if you please’. Development of ‘dare’ Prob. first in neg. phrases like haud ausim dare, non ausit crédere (Plaut.) ‘wouldn’t
eto’ = ‘wouldn’t risk, dare’. Walde-
: 719. Ernout-M. 86, 87 £. Walde-H. 880, 1. REW 801.
dims marten’, fr. Slavic, of, ChS tin a. ulg. driznti (below, 7). Tik-
R
bly af ees fr. late Grk. korrifw the ee Ce (fr. kérros ‘die’), through (ike phorical Sense ‘risk, venture’ REW o9g7, muBebw ‘play dice, risk’).
4, i, r0-lq ‘ hang, undertane see lamaim ‘take in
» Nir, lamhaim ‘dare’
Digitized by Arya Samaj Foundation Chennai and eGangotri
ON; TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1149 ,
and ‘handle’, beside W. (old) Jlafasu ‘venture, attempt’, Corn. lawasos ‘dare, be permitted’, W. llawio ‘take in hand, undertake’, fr. Ir. lam, W. llaw ‘hand’. Pedersen 2.560 f. K. Meyer, Zur kelt. Wortkunde 179.
Nir. danuighim, danuim, fr. dana ‘bold’ (16.52).
W. beiddio, also ‘challenge, defy’ (cf. NE dare in this sense), perh. : Ir. bid- cais ‘sprang’ (pret.), bedc ‘start, leap’, NIr. btodhgaim ‘start, rouse, startle’, outside connections dub. Pedersen 1.88, 2.476.
Br. kredi ‘believe’ (17.15) is also ‘dare’, through ‘have confidence’.
5. Goth. gadaursan, OF durran, OHG giturran, etc., above, 1.
ON fora, Dan. turde (secondary form; ODan. thure, thore), Sw. (refl.) toras (also in Dan. and Sw. as auxiliary ‘may, will’), beside ON poran ‘daring, courage’, root connection dub. Walde-P. 1.710, 728. Falk-Torp 1299. Hellquist 1269 f.
ON dirfask (refl.) : djarfr ‘bold, brave’ (16.52).
NHG, Du. wagen, fr. MHG, MLG wagen ‘wager, put up as a stake, risk’ (MLG > Dan. vove, Sw. vdga, late ON vaga), this fr. wage, NHG wage ‘bal- ance, scales’ (MHG also ‘hazard, risk’), hence lit. ‘put in the balance, weigh’. Falk-Torp 1394. Paul, Deutsches Wtb. 623.
```


## [2026-09-05T18:16:54.977Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ *13[0-9] *d\\|d'n \\|d’n \\|d\\`n \" SOD.txt | head -20; echo \"=== search entries 134 136 ===\"; grep -n \"^134 \\|^136 \\|^ 134 \\|^ 136 \" SOD.txt | head",
 "description": "Search Gharib Sogdian dictionary"
}
```


### [2026-09-05T18:16:56.710Z] TOOL RESULT

```
33916:GMS  178,  317;  BBB  604;  C2  gloss.;  fsqrd'n  STi 
42417:MP  m^y'ri;  Parth.  mHgd'n 
45133:5591  myd'n   C  =■»  my8>n 
70261:sqrd'n  C2,  77R9;  AVS  76 
80432:10692  xw'nyzd'n   M  ( oLIjl>-  cJL+)ohj>.  u'>- 
83511:11123  yzd'n   M  jiij*. 
=== search entries 134 136 ===
8427:134  »k}c(h)   B  ^<U* 
8437:136  "k'rtk   B  ^jl^ 
16016:136 
25642:134 
29900:134 
30243:136 
47943:136
```


## [2026-09-05T18:17:01.727Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 200 202; do echo \"=== SOD leaf $L (printed ~$((L-66))) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' SOD_pages.txt | head -50; done",
 "description": "SOD pages 134,136"
}
```


### [2026-09-05T18:17:03.263Z] TOOL RESULT

```
=== SOD leaf 200 (printed ~134) ===
                                                                                                                                 w^«^^»—



 135


       with seed                                                        TSP 2.224, 538; BSTBL, Padm. 41; Frag. 2a.l9;
                                                                                                                           8>t
       TSP 2, 165, 1020; Hen. Texts. 717                                  GMS 978; -u>, TSP 3.296
3408 6'p't B                                        cJu^-uja
                                                                  3420 8'r'wkh =» 5>r>wk(>)
     5apat ©Skt. danapati                                         3421 *8Vyn,y B                        ^v^^w
     donor                                                             Sarene ©pi. SVynh
       SCE 186           ,                                             wooden

3409 d»p't C           /                            ? ^j-u              TSP 3, 181 n pl97; Hen. Texts. 728
     6apat                                                        3422 d'rny   C                                    *xjix&
     truely ?                                                          Same    ©pres. part.
       STi 18.5; BSTi 266; Hen. Sogdica. 7.1                            holder
                                                                        C2, 56R32
3410 S'p'tsyy      M     j£i *, ^G ^/    fO)olb «Jh> <Lj

       6apat- sey ? ©Parth. <fy&/; <Akk. dibat                    3423 d'rwq C ** 5>rwk())
                                                                  3424 8'rwk01 B, M, C                                   VJ>>-
       beautiful, fine, DapatO/ze ha/we o/ a godess)
                                                                       8aruk (d'rwq) ©Yaghn. dork         ©ob. -y, -u>
       Hen. Sogdica. 7.2; BSOAS 11, 737n 1                               =*&T}v/kly\ ptsng d>rwq
                                                                       wood
3411 8'p't- syrh M                             olb >c^
     5apat-sir ?                                                       SCE 133; TSP; BSTBL, Padm. 41; GMS 978; BBB
     Dapat-wishcr                                                        463; STii 1.49, 53; Syrwq% BBB 498; STii 1.15,
     Sogdica. 7.1                                                        80, 13.10

3412 8'r- B, M, S             (J>> ^<** jj)jzi.L^i <jiib          3425 S'rwkp'Sy B                               ^^      Jj£
     6ar (d'r1) ©OP ddraya- ©inf. -}y; trans, prct.                    5aruk-pa5c
       aux. =»5ryt-                                                    wooden shoes
     (/cOhavc, (/cOpossess, (ro)hold, 0o)kccp, (/o)wcar                SCE 152
       GMS 285, 877-880, 855
                                                                  3426 8'rwkync     M                          ^J^S ^^3^
3413 dV     C =» 8>r-                                                  5arukc(n)c   (5'rwqync) ©f. adj,
3414 dV     C                                          r t a— J
                                                                       (o/)pIant, herbal
       6ar ©<Av. dara; Skt. dhara                                      BBB 498; GMS 334, 1053, 1273; Sogdica. 64, 14
       blade
                                                                  3427 SVwqync =» 5,rwkync
       BSTii 843.36, 37; JA 1959, 127; S W, C2, 68V6
                                                                  3428 8'nvkynyy    M                                    ^[f
                                                                       5arukene
       pl49
=== SOD leaf 202 (printed ~136) ===
                                                                 i-■:&*. ;^-*i,W«i J J Vw^^tii>»irtt^i^vii^^:iA^4it^                     .A.-«i-:s&ift-.M*-*»-;:




 137
                                                                                                                                                         <0b i^ip i,


        BSTBL, Dhy. 89, 346; O2 32; Gersh. Minorsky                          3468 8p*nk S
          Mem. vol. 1971, 290 n47a; TSP 13.23; Benv.
                                                                                         (a)5Pane ^'SP'nk
          Sfi'z, n p228; S W, IIJ 1976, 55.23                                                                                                        4*sy
                                                                                         grain, seed
                                                                                         MDii pl99;MDiii  pll9
                                                                                                                                                                   i^
 3457 5p»r-     B -» 5p>r                                                                                                                                               6p't
 3458 8pwr Spr'yn'y B                           .ju^*^ «jui**                3469 5p}npn B, S => SP'mpnCw), Sp'mb'n
      8par- 8Parene «*8p,r                                                   3470 db'n(y) B
      giver of gifts                                                                                                                                               *j>j^
                                                                                         9/5Pan(e)
                                                                                         extension =»*8p>y-
      SCE 496; -Sprrik, SCE 46
                                                                                         STi 75.18; Sund. AoFiii 1975, 56
 3459 6p>Yst- B                      ( j&jji rJLJ-^j^-jJul
      Spaxst, Gfaxst (6Pj-) ©*0wax.?-; /"/wa^ ®pt.                          3471 5p>nz B, S
        st, =»9fyz-, 8p'yz-, 8pxsty(y), SPystc                                   SPanz ©<*debazah; Av. bazah
      GcOcollect, 0o)gain                                                        wide, coarse                     SPnstr
      GMS 293; Hen. LW 105; VJ 241, 243 pp., n p92;                              TSP 2.1018; Hen. Texts. 738; GMS 1310; MSP
        AVS 130                                                                              bl89; Frag. Len. 97a3
 3460 8p»m>n    B, S ~> db'mn                                               3472 6p}nzqVyy M                         Jz*^
                                                                                                                          Uw>
 3461 db,m)nqy> C                                   J£<JL*f                      5Panzkawc (8b)nzkwy)
                                                                                 thickness
      SPamankya ^SPm'nky*
      doubt                                                                      GMS 999; Hen. BSOAS 12.312, 91; BBB
      STii 3.21
                                                                            3473 5b*nzkwy                       B =» SP'nzq'wyy
3462 fip'mb'n M                           j^a ^ '^                          3474 8p»r B, M, S                            c^^-u
     Spamban    (5p>npn, S^mbn) ©<* demand- pad ni\                              8Par, 9far (8p»r-) ^Gb'r, 8p'r 8pr>yn>y
       Pahl. banbisn -^db'mn, SP}mpn(w)
     lady, wife                                                                         GMS 957, 1511; BBB 751 f34; VJ; TSP; BSTBL,
     GMS 14, 43, 466, abl. -\ 1224; Benv. Titers et                                         Vaj.; SCE; Frag. Len. 45.3; KG 414; Talcs. 481,
       Noms Proprcs. 29; Gersh. Sogd. Cpds. 137
                                                                                            48; 6fi*ry VJ 190, 58d, 988
3463 6p>mbn =» 5P,mb,n                                                     3475 6pV-gift B                                  (Jjzs ^r,f,,,, j->) q»lj<u-U *Jjb

3464 db>mn C, S                                                                         8Par, Gfar ©OP fra-bam Khwar. hfir-,
                                                    y,
     SPamman (SP'nVn) ^SP'mb'n, b}mn                                                     Yaghn. tifar ©inf. J>}y =>9br-, SPr-1
```


## [2026-09-05T18:17:10.663Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 199 201; do echo \"=== SOD leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' SOD_pages.txt | head -60; done",
 "description": "SOD leaves 199,201"
}
```


### [2026-09-05T18:17:12.402Z] TOOL RESULT

```
=== SOD leaf 199 ===
                                                                                                                                 134
          d-                                                                  BSTii 848, 60, 846.20; C2, 60R18, 69V 12, 26,
                                                                                120R3
                                                                        3397 5>m>k S                                              ^
                                                                             Samak ^tWkCh)
                                       d/5
       3384 d-      C                                          ji.4,          with me, about me
               8(a) ©prepos. in compd. ^Syw'yS, SymyS,                        MDii Nov. 4 RIO, 15-6; Frag. Len. 92.11
               to dywnt, Symnd, dyw1                                    3398 8'm'kh B                                   t^-a^^ry
                                                                             8amak ?
               Benv. JA 1955, 321, dyw                                       creature
       3385 6»m      M =» 6>m                                                O1 11: Frag. Len. 92.11
       3386 5Mwn =* 8>wn                                                3399 aWyyt B                              (J±jT jjh){
       3387 8» => L>     ,                                                    5amext ? ©*dame +>Ytw ©ob. -yh
       3388 d}- C              :                       i                      Mtihxai judge of the world)
                                                                              VJ 1205; Gersh. AHM p35, 40
            8a ©*/iada ©prepos. +/\ m> ^dT, d'nV, >8nn
            with                                                        3400 SWn'k
                                                                             worldly B
               Benv. JA 1955, 321                                            8amcane

       3389 8'pr- B, M                          (J>>>^>>)0^                 STii 7.28; GMS 1022
               8a(3ar ©impf. «*6pr-\ 9>br-                             3401 8>mcyk B
               Go)give                                                      worldly
               GMS 621                                                      Samcik
                                                                                                                                     jkr
       3390 d>cyqy> C                                     J^cJIop
                                                                             STii 9.17-, Frag. Len. 100 c5; GMS 1014
               dacikya ^d'tcyqy*
                                                                       3402 S'mSVk B                           jhh^i^.jfxjl
               justice                                                      8am-Sare                                      J^r
               C2, 50R20, !08V2pl08, 20
                                                                            creator
      3391 d>f> C                                              yu           TSP 8.61, 71, 75, 190, 8bis 5 etc.
fli        8afa =>tyw, t'P
           with you                                                    3403 5,m5n)k S             j^_ jl ^<c-a * o^r J* y
               BSTii 848.59, 885.5; C2, 51R5, 8, 69V25                      8am-8ane ©*daman-danaka
                                                                            center of the world
      3392 5>m B, M, S            (fl*)*yrj*<o^*ir±j't                       MDii pll2n 1
                                                                                                            ■■r




           8am (S»m, d'm1) ©<*daman ©f. n.; ob. -y(yA
                                                                       3404 8Jmh    B, M, S                      o^ <J±J
              -y/i =>8}mh
                                                                             8am (8*m) ©f. n.; ace. -wh, ob. -yh =>8}m
           creation, world, being                                            creation
           GMS 282, 940, 13; TSP; BSTBL, Vim, 135; Frag.                    GMS 282, 1219; BSTBL, Vim. 126, 129; TSP; VJ
             Len. 27.7, 93.33; Tales. 476; STii 4, 17; -y, TSP                 1007; STii 9.7, 9; KG 423; wA-, TSP 2.750,
             5.13; Tales. 481; -yy, BBB b83; Hen. JRAS                         6.190; Vim. 130; SCE 9; -y/z, TSP 2.836, 10.15;
              1944, 142; -d>mj\ C2, 60V3; Sund. AoFviii                        Dhy. 384; STii 7.22
              1981 p214, tf'm, BBB 499; S'myK STii 7.22                3405 5>mynyztk B
      3393 d'm' C => 8>m                                                    8ame-nizte
                                                                                                          O^r j' dj^i <WJ j' £->*>-
      3394 dW C ^ 8>m>                                                      out of the world
                                                           4s <r).
      3395 ^m* B, M                                                         STii 7.5
           8am(a) (d>m?) ©ob. <?Wy                                     3406 8>n M                                                   <ib
=== SOD leaf 201 ===
                                                                                                                            ;13



                                                                                                                          136
d't

3432 d>t C =* 8>t                                                  willy-nilly, at all costs
3433 S't'kdi)    B                              Jxjjtotjj®         Sund. MSP p44-5 bl53
     Satak
                                                             3445 5>tyk => S't'yk
      law                                                    3446 5'tymyc B
      SCE 58, 363; STii 7.2; TSP 2.55, -w; Hen. Texts.             0: 16
                                                                  Satemec
                                                                                                                      isy
        734                                                       lawful, legal

3434 8>t'yk B                                /&<J&ijj3
     Satik (8>tyk)
     just, lawful, legal                                     3447 8»w B ** 6»wt,(,)
                                                             3448 5Nv~ B                       Cpj^I * j=»jj < JJ^
     SCE 32; GMS 994; TSP 7, 18
                                                                  Saw (d>w-) ©Khwar. 5w-y Yaghn. dow, Oss.
3435 8'tpr B                                        ^oj^
     Satpar (d'tbr) ©*data-bara-          ©pi. -/                    ddw
                                                                   0o)r         ^'nS
                                                                        ub,en (ro)   'w-
                                                                                   smea r
      judge                                                        BSTBL, Dhy. 1, 68; TSP 3.88, 162, 196, 241, 280,
      Frag. Len. 91.8; STi 6.12; Sund. AoFviii 198,                     12.6-, trans, pret. d}wd}r-t Sund. AoFiii 1975,
        p214; STii 2.4, 4.7; BSTii 880.11, 16: C2, 77R5,                64, 6; STi 67
        16,24R13, 77V11
                                                             3449 dJw- C «* 5>w-
3436 d'tbr    C -> 5>tpr                                            {M(=B,
                                                             3450 6>wn  rm)M                (j>>>^ jj).!^^
3437 d'tcyq     M -+ 8>tcyk                                       8on (8wn) <§)<*hada-avana =*Sn, 8nn,
3438 5>tcyk B, C                                                  with
                                      c-^^^li
     Satcik (d'tcyq) -^d'tcyqy*
     legal, lawful, right                                          EGSii 122; GMS I6n 1, 1446; S*wn, Frag. Lcn.
                                                                     49.12
     TSP 16.25; GMS 994, 1017; Sogdica. 35.7; STi
        63.6, Sund. AoFiii 1975, 58.2; -y, STi 19.11         3451 d'wsy C                                            <oL-a
3439 d'tcyqy* C                           oLj 0>U jJ* «b          Sose ©pi. -t =>dwsy*
     Satcikya ^SHcyk, d'cyqy*                                     neighbour
     according to law, justice                                    BSTi 106
     STi 31.6; C2, 56R20, 108 V2                             3452 5>wt>(,) B                               ol^J^j^f
                                                                  duta (5>w) ©Skt. dhuta
3440 5>t(h) B, M, S                          OV:jL^)j'^
     Sat ©Skt. d/rar«; Vrfa ©pi. -//A                             morality, law
     wall                                                         BSTBL
      TSP 2, 527; BSTBL, Dhy. 325; KG 464
                                                             3453 d>y     C ** 5'yh
3441 6'tkn'k B                           (jOj*>)jja'j<^      3454 S'yh     B, M, S                    (oh)ojj&*^<^
     Sat-kane
                                                                  Say (d>y) ©<*dahi; Skt. dasi ©f. n.; pi. -/
     thief
                                                                  slave girl, female servant
      SCE 331; Gersh. Sogd. Cpds. 1945, 145, 3                    SCE 341, 373; VJ 162 etc.; BSTBL, Vim. 63; STii
                                                                    3.29; Tales. 486.11, 23; BSTi 134; MDii, Nov.
```


## [2026-09-05T18:17:22.427Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==200' SOD_pages.txt | sed -n '60,200p'",
 "description": "Rest of SOD leaf 199 (p.134)"
}
```


### [2026-09-05T18:17:24.152Z] TOOL RESULT

```
           8am(a) (d>m?) ©ob. <?Wy                                     3406 8>n M                                                   <ib

           net                                                              8an ©Av. ddno-kars
                                                                            seed
           GMS 973, 1265; Tales. 471.12; TSP 2, 273
      3396 dW C                                                             BBB 575
            8ama ^t'nV                                                 3407 5'n'ych B
                                                                            Sanic                                             <&*
                                                                                                                        jbojb i, j<ib
            with me
```


## [2026-09-05T18:17:32.668Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 277 279 294; do echo \"=== BQT_v2 leaf $L (printed ~$((L+543))) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -40; done",
 "description": "Borhan-e Qate vol2 pages 820,822,837"
}
```


### [2026-09-05T18:17:34.374Z] TOOL RESULT

```
=== BQT_v2 leaf 277 (printed ~820) ===
 ‫دامن بدندا نکرفتن‬                                                                           ‫‪ ۷۱‬رس‬

                                        ‫گفته‌اند ‪. ۴‬‬     ‫دام = بروزن رام» نقیض ددباشد که‌آن‬
                                                         ‫وحشی غیر درنده است عموماً و آهوو غزال و‬
                                                         ‫لیر را(‪)۱‬گویند خصوصا ‪ - ۱‬وحشرات‌الارش‬
                                                         ‫وپرنده را هم میگوبند ‪ -‬و هرچیز که جانوران‬
‫دامگاه ستول = بمعنی دامگاه دیو‬
                                                         ‫در آن بفریب گرفتار شوند ‪ - ۴‬و نزد محققین‬
                     ‫است که عالم سفلی است ‪.‬‬
 ‫‪e‬‏ تیدام اور‬         ‫گرگ‬            ‫دامگاه‬                                             ‫بمعنی زخارف‬

        ‫است کهجهان فانی وعالم سفلی باشد ‪.‬‬                                              ‫دلیوی و آنچه‬
‫دام آشتن > کابه از بازی دادن ودام‬                                                   ‫باعثبازماندکیاز‬
                                                            ‫مبداء باشد‪ . # .‬نوعی‌دام (تور) ماهیگیری‬
          ‫‪ -‬وخلاصی از دام باشد ‪9 .‬‬           ‫سردن‬

‫دامن باغی گرفتن‪ -‬کنابهازخلوت‬
                                                         ‫دامفول‪ -‬با غين نقطه‌دار وواوه‌جهول‬
                ‫زیدن گووشه نشینی باشد ‪.‬‬                  ‫بروزن زاغنول‪ ,‬دانهاو گرهها باشد مانند گردکان‬
‫دامن بد ندان گردن = کنایه از‬                             ‫که ازاعنا کولوی مردم برمیآید ودردنمبکند‬
‫نمودن باشد د و کنایه از‬        ‫فروتنی کردن و عجز‬         ‫نورآاسلعه میکوبند‪ -‬وغول‌بیابانی رائیز گفته‌اند‬
                  ‫گرشختن هما مدهاست (‪. )۲‬‬                                         ‫واونوعی ازجن است ‪.‬‬
‫دامن بنددان گر تز بمعنی‌دامن‬                             ‫داهلث » بفتحثالث بر وزن کالك '‬
‫بدندان کردن است کنهابه از عجز و فروتنی‬                   ‫جانوران وحتی کوچك راگویند همچوخ رگوش‬
                                    ‫وگربختن باشد ‪.‬‬      ‫ورویاه وامثالآن ‪ -‬و مقنمه وسرانداز زنانرا هم‬

                                ‫‪.‬‬    ‫(‪ )۲‬چك‪ .‬چش ‪ :‬هم هت‬               ‫(‪ )۱‬چك ‪ :‬نخحیر را ‪.‬‬

  ‫» رام شدن) » بونانی ‪( 5618002‬کاو نر) ‪.‬‬               ‫رمدن‬
                                                          ‫‪ - ۱‬حندی باستان ‪( 0۳31 -‬کرا‬
   ‫)؛ در پپلوی ‪0۳84‬‬           ‫رمدن‬
                                 ‫لانبنی ‪ ( 6720۳10‬کاو نر‪ .‬ورزاو ) فس ‪ :‬استی ‪( 000۳0‬کرا‬
                     ‫(مخلوق) (اوستا ‪« )020180-‬اسشق ‪ ۰۳۵‬و ص ‪۲۷۲٩‬‏ ورك ‪ :‬مناس ‪. ۰۷۲:۲‬‬
  ‫‪ - ۴‬هندی باستان‪( 02008 -‬بند‪ .‬ریمان ‪ ,‬زنجیر) » افقانی ‪ , 0101‬ارمنی ع (‪)8‬‬
  ‫‪( 602‬تور) «امذق‪ .۱۳۰‬پهلوی ‪« 018‬مناس ‪۱۷۲‬؛ نیز تورماهیگیری ‪« :‬ماهی از دام جدا‬
  ‫شد ‪,‬روباه پیشتررفت وماهی خوردن گرفت» «سندبادنامه‪ .‬ظهیری‪ .‬طبع احمدآش ص ‪ ۸4‬طبری‬
               ‫رك ‪ :‬دامنی ‪.‬‬          ‫‪ ۰‬مازندرانی کنونی ‪ « 20062‬واژه نامه ‪. ۲۱4۰‬‬
                                       ‫‪۴‬‬                                                         ‫‪8‬‬
   ‫‪ #‬داماد ‪ -‬پهلوی )‪ , 4072‬اوستا‪( 72]200282-‬داماد)‪ ,‬هندی‌باستان ‪,۲2420۳81-‬‬
   ‫کردی ‪ › 62۷22‬اففانی‪ 0۳2‬و ‪, 128۳02‬بلوچی ‪ 012002‬و ‪ «04۵۷021‬اسدق ‪۲۳۵۰۰‬‬
=== BQT_v2 leaf 279 (printed ~822) ===
 ‫داشور‬

‫دا نژه گ بازای فارسی» بروزن وهعتی‬                           ‫و واو وضم رای قرشت (‪ )۱‬و سکون جيم اول‬
                 ‫دالجه است که عدی اند ‪.#‬‬                    ‫وبای ابجد (‪ )۲‬وجیم آخرء حبی است که آنرا‬

‫داش ® ‪ -‬بروزن بال » بىمنىعلم‬                                ‫که از‬              ‫وبه‬
                                                                                 ‫بشیرازی انجکك خوانند وکازبکلوه‬
                                                                                           ‫ولات فاری است آورند ‪.‬‬
                 ‫وفطل ودااستن چزی باشد ‪.‬‬

‫د بکر بای فارسی‬         ‫دانش پژوه‬                            ‫بفتح‌ثالك وواو وبای‬                  ‫دانج و بر ‪1‬‬
‫وزای فارسی بواو کشیده و بها زده » بمعئی علم‬
                                                             ‫ابجد ‪ .‬دانۂ ویراست که حبالرای باشد ‪٠‬‏ وآن‬
 ‫وفضل جوینده وطالب علم‌باشد چه پژوه جوننده‬                  ‫تخمی است زردرنگه وطعم آن نلخ میباشد و از‬
                        ‫وتفحص کننده رکاوبند‪.‬‬                                    ‫وردستان مبآورند ‪.‬‬
                                                                                                ‫کوهتان فاری ک‬

‫دانشگر ‪- ۲‬باکان‌فارسی روزن‌داشور‪,‬‬                            ‫دا نحه ‪ = ۲‬بسکون ثالث و فتح جيم ‪,‬‬

 ‫داشمند و دانا و بیار دان و عالم و فاضل‬                                               ‫غله‌است که بعربی عدس کوند ‪.‬‬
                                             ‫باشد ‪. ¥‬‬        ‫انك ‪ » ۴‬بفتح‌ثاكك وسکون‌دال ابجد‪.‬‬
 ‫دانشور ‪ = 4‬با واو بورزن داشگر»‬                                   ‫‪۱‬‬                    ‫بمعنی تواند باشد ‪.‬‬
                                                   ‫وبا ‪۰‬‬   ‫)‪ (۱‬چك‪:‬‬                    ‫(‪ )۱‬چك ‪ :‬وضم را ‪.‬‬

 ‫دالره (ھ م‪ ۰ ( ۰‬دانجه دز فارسی‬      ‫‪-‬‬        ‫‪۴‬‬              ‫‪۰‬‬       ‫ودر‬   ‫‪:‬‬    ‫رك‬   ‫دالهٌوبر ‪.‬‬    ‫معرب‬         ‫‪۱‬‬


  ‫مضارع‬   ‫) مفردمغاب)‬   ‫شخص‬    ‫سوم‬   ‫‪- ۳‬‬                         ‫› ‪.‬‬       ‫بمعتی ‪( 61111061‬فر) است « لصك‪۹۷‬‬
  ‫‪ ۴‬ر=انجه (ه‪.‬م ) از ‪ :‬دان(دانه) ‪-۲‬ژه (یوند صفیر) رکه‪ :‬دانك ‪.‬‬                                 ‫آزمصدر دانتن(هم ) ‪.‬‬
                        ‫‪۹۱‬‬        ‫«منای‬           ‫اسم مصدر از دانتن ‪ ۰‬به‌لوی ‪nhsinãd‬‏‬                     ‫‪_ ۵‬‬


                              ‫اسم فاعل از پژوهیدن)‪.‬‬              ‫‪۰‬‬    ‫‪٣‬‏ یژوه (دژوهندء‬       ‫از‪ :‬داش‬      ‫‪ 1‬ت‬


  ‫‪ ۵4‬از‪ :‬داش ‪٣‬‏ ور (بواداتصاف)‪.‬‬


  ‫‪ #‬دانةن ‪ -‬بکر سوم و فتح پنجم (درلهجة مکرزی) ‪ .‬پپلری ‪« 82152021‬منای‬
  ‫»زربشة بارسی باستان‪. 8۳2-‬آریایی‬
=== BQT_v2 leaf 294 (printed ~837) ===
  ‫—‪~Art‬‬                                                                                                    ‫درخشان‬

‫ثالثو سکون‌واومعدو له‪,‬‬    ‫دق‬   ‫=‬    ‫خور‬       ‫در‬           ‫اوینا کرده است ‪ -‬ونام دهی استازولات قابن‬
  ‫بمعنی لایقو سزاوار ودر وسم‪-‬و در خورشید‪8‬‬                   ‫وقهستان‪ ,‬ودرا تساکلیم راخوب میبافند‪ -‬وبمعلی‬
                                ‫‪ -‬ودرطمام باشد ‪. ۷‬‬
 ‫با واو ممدوله بروزن شب‬                 ‫د‬
                                        ‫رخو‬
                                          ‫در‬               ‫یوفتح اول وضم‌نالث‪ ,‬به‌نی‌درخورولایق ومزاوار‬
‫کرد ؟ بمعتی درخوراست که لاق وسزاوار باشد‪.‬‬
                                                           ‫باشد؛وبمعنی ثالی که فروغ‌وروشنی باشد بضم‌اول‬
                                    ‫د‬                      ‫و بقتح اول وضم ثالث کهب‌عنی‬         ‫رفتح‌ثانی هم‌هست؛‬

 ‫‪ ۲‬د با واوممدوله بروزن‬            ‫در خوش‬
                                                            ‫درخور ولایق وسزاوار باشد بمعنی شوق واشتیاق‬
          ‫کرش‪ ,‬بمعنی شوق واشتیاق باشد ‪.‬‬  ‫س‬                                                          ‫هم گفته ند‪. ۱‬‬

‫حرون شدن ‪ -‬کنابه‌ازقسدد رکشتن‬      ‫د‬                           ‫صم اول بروزن سخن‬            ‫درخشان '‬
                   ‫واراده مخون کردن باشد ‪#.‬‬                        ‫باشد ‪۰‬‬   ‫دهده‬    ‫تابان وروشی‬       ‫بممعصنیی‬
                                                                                                             ‫دان ‪ ۰‬ب‬

 ‫در داب د بروژن زردآب » دستنیوبه‬
                                                               ‫ورتو‬
                                                                  ‫در حشیدن ‪ = ۴‬بمعنی تایدن پ‬
 ‫ای باشد كوچك و هدور‬           ‫را گونند ‪ ۰‬وآن هوه‬                                                   ‫افکندن باشد ‪.‬‬
                        ‫وخوشبوی شبیه بخريزه ‪.‬‬                  ‫هنابه ازت‌غیرشدن‬
                                                                              ‫در خط شدن ک‬
 ‫بر وزن سردار ‪ ۰‬نام درختی‬          ‫سم‬   ‫دردار‬              ‫آوزرده گردیدن باشد‪ -‬وبیپوش ویقرار کشتن را‬
‫است کهپشهبارمی آورد و بعربی شجرة البق‬
 ‫خوانند ‪ ۸‬و بعضی کوبند سفیددار همان است‪- :‬‬                 ‫بشم‌اول وئالث وسکون ثالی‬            ‫در حف‬
 ‫ومعنی نرکببیآن درخاله ‪٩‬‏ ‪ -‬وامردرد ببار*‪-۷‬‬                                       ‫و فا » زلبور سیاه را گویند ‪۱‬‬
                ‫وفاعل درد ورنده*‪ -۱‬ودریان؟‪.۱‬‬                   ‫خرواه ‪ ۴‬ت با واو معدوله بر وزن‬
                                                                                            ‫د‬
 ‫درد حوار = ینم اول با واوممدوله‬                            ‫در گاه ؛ بمعنتی الماس ودرخواست باشد ‪ ۳‬وامر‬

 ‫بروزن بردبار » هردم فقیر ودون وفرومابه باشل‬                ‫بایشممنی هم هست یمنی التمایکن ‪ 7‬و کدا‬
                                                                                  ‫و کدایی کنند‪ ۰‬رایز گونند ‪۰‬‬

                                                               ‫دخرود گر فتن » کنابه از کرد‬
                                ‫درصفاهان‬      ‫محله‌است‬                                 ‫باشف‪-‬‬    ‫آوری خود کردن‬
```


## [2026-09-05T18:17:47.928Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 270<=i<=300:\n        # find lines containing target words\n        for w in ['دانه','دایه','دایگ','درشت','دانگ','دانك']:\n            if w in p:\n                print(i,w,p.count(w))\nEOF",
 "description": "Locate BQT leaves with target headwords"
}
```


### [2026-09-05T18:17:49.505Z] TOOL RESULT

```
273 دانه 1
274 دانه 1
277 دانه 1
278 دانه 1
278 دانك 1
279 دانه 1
279 دانك 1
280 دانه 9
280 دانگ 2
280 دانك 1
281 دانه 5
281 دانگ 1
282 دانه 1
282 دایه 1
286 دانه 1
296 دانه 1
296 درشت 1
297 درشت 5
300 دانگ 2
```


## [2026-09-05T18:17:54.738Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 280 282 297; do echo \"=== BQT_v2 leaf $L (printed $((L+540))) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt; echo; done",
 "description": "BQT pages 820, 822, 837"
}
```


### [2026-09-05T18:17:56.236Z] TOOL RESULT

```
=== BQT_v2 leaf 280 (printed 820) ===
 ‫=‬    ‫=“‬
                                                                                               ‫داشومد‬

‫بف هد تا ازآن سرانجام خوردلی‬    ‫روفف هرىكڭزرى‬       ‫وخداو ند ودارندة داش باشد»چه ورىمەنى‬              ‫صاحب‬

‫ومایحتاج آن نر كنف ‪ -۳۴‬و فتح تااث اساب‬                                ‫ام‬     ‫و خداو ند ودارنده‬        ‫صاحب‬



                                                     ‫دا نشوهنك ‪ ۱‬ب‪-‬فتح‌ميم وسکون نون‬
                          ‫باد ©‬     ‫و متاع و کل‬


                                                     ‫و دال ایسد » بمعتی دانشمتد وحکیم وسباردان‬
                                                                                                  ‫‪۰‬‬   ‫باشف‬




                                                     ‫دانشی ‪ -‬بکرثالث ورایع وسکون‬
                                    ‫وامثال آن ‪.‬‬
                               ‫‏‪٩‬‬
                                                     ‫وانا‬
                                                        ‫تحتانی " بمعنی دانشگر امت که داشمند ر‬
‫د بفتح نالك وسکون‌ميم‪ .‬نمعدی‬        ‫دانم‬                                                          ‫باشد ‪.‬‬
                                    ‫توانم باشد ‪.‬‬
                                                    ‫دانك؟ = بفتح نالك و سکون كاف ‪٠‬‏‬
‫بروزنآغوش‪.‬نام‌شضصی است‬         ‫دناوش‬                 ‫گمنادزم و جو و ماش‬‫ناد اع‬  ‫به ر‬
                                                                                  ‫ودان‬
                                                                                     ‫گلق‬
                                                                                       ‫مط‬
‫ازبود معشوقة‬              ‫که عذرا را بفروخت‬         ‫ودص و غیره ‪ -‬وبضم الث آن باشد که بوقت‬
                                                                                        ‫ع‬
‫وامق ‪ ۰‬وفصهه ابغان مشپور است ؛ وآنرا دوانوش‬         ‫دندان نزآوزدن اطفال اقام دانها از جنس کندم‬
‫هم میگوبند که حرف انی واو باشد بر وزن‬               ‫وجو وماش وعدس وامثال آنها را باکله و پاچ‬
‫قدایوش ؛ ودلواش نیز گفته‌اند که حرف انی نون‬         ‫گوسفندپز دوبخانهای دوستانو خوبشانومصاحدان‬
‫باشد پروزن اوباش؛ و دیانوش نبینزظرآهده است‬          ‫فرستند ‪ -‬و در ملك دکن مهتر چاروا دار را‬
            ‫که حرف انی دای حطی باشد ‪* .‬‬                                                        ‫رنه ‪۵‬‬
‫داه جیدن‪ -‬بچمعینیدنبر‌دانه امت‬                       ‫دانگا ند = باکاف فارسی بروزن‌بازخانه‪.‬‬
‫اززمین‪ -‬کونابه‌ازسجده کردن‪ -‬و کدبه و کدایی‬           ‫وشت‬
                                                       ‫آن بائد که جمعی چون خواهند بسیر ک‬
 ‫ب‪-‬هلوی ‪ « 2016-0015080‬منای ‪» ۱۷۲۰‬از ‪:‬دای ‪ +‬اومند ( = مند‬
 ‫بهلوی ‪« 610151021‬منای‪ ۱۷۲‬از‪ :‬داش ‪ +‬ی(نسبت)‪« :‬چنن‬              ‫‪۴‬‬                     ‫‪۳‬‬    ‫اصاف)‬   ‫نمواد‬


 ‫گویدمحمدین عمرالرادوبانی که صثیف ها بسیار دیدم‌مرداشیان هرروز کاری را اندر شرح‌بلاغت»‬
  ‫«ترجمان البلاغه ‪ .‬رادوبانی چاپ احمد آتش ص‪( ۶۵۱‬بخش عکسی‪ » ).‬ولی در بخش چاپ سربی‬
 ‫‪ ۴‬پپلوی ‪ « 2020‬بندهش ‪٤٤۱‬‏ » « اسشق‬                              ‫ص‪ ۲‬بخطا «مرد انگابان » امده ‪.‬‬
 ‫‪. ۵00‬کنابادی ‪ « )8000‬پروین‬             ‫‪ ۳۳‬امروز دانگی (تهرانی‬   ‫‪۴‬‬              ‫‪۵‬‏ ‪٩‬ورك ‪ :‬دانه ‪.‬‬
‫‪ _ِ 1‬اول شخص مفرد (متکلم وحده) مضارع از‬                ‫© _ رك‪ :‬دانه کانه ‪.‬‬          ‫کگنابادی» گونند‬
                                                                                         ‫دانستن(«‪.‬م‪: ).‬‬
 ‫‪#‬دالگ ب‪-‬سکون‌سوموفتح آن‪ .‬بهلری‪ 802۰‬پارسی باستان (بنقل بونائی) ‪.44 8×41‬‬
  ‫«‪:‬نفس») اصلاهمر ش‌دانه (ھ ‪.‬م‪ ).‬اسست«اسشق‬     ‫(اپن‌درید»‬     ‫ارمنیع ‏‪ . dang‬عربی‌ع‌دانق ‪0‬‬
 ‫‏‪ ٩‬چهاريك درم ومثقال وجزآن ‪ -‬خش‌بك ملك وخانه ‪ -‬حصه و بهره «ناظم الاطبا » و رك‪:‬‬
                                                                       ‫‪ ۱‬دانق‬    ‫اسللام‬    ‫داثرةالممارف‬


  ‫د‪#‬اله ‪ € -‬سوم (درلھجۂ مر کزی)‪ .‬بهلوی ‪ . 8081‬اوستا ‪_ahsrakj‬‏ ‪6020‬‬
 ‫‪, 166021 ,‬بلوچی (ع(‬                ‫‪۰‬ردیع ‪6‬‬
                                          ‫هندی باستان ‪( 80800-‬دانهٌ کندم) ک‬
                                                                          ‫(دانه کشس) »‬
 ‫(نج دانه)‬
         ‫‪han‬‏ (دانه) ا‪:‬فنابیع ‪ . 6820‬سریکلی ‪ ]020[01‬پ‬
                                                    ‫مش ‪ 82020,‬و‬
 ‫«اسعق ‪ ۵۳۵۲‬گیلکی ‪ › 63081‬فربزندی وبرتی ‪ , 8800‬نطنزی ‪ .4< 8020‬اص ‪٩۸۲‬‏ ‪.‬‬
     ‫‪۱۲۸‬‬   ‫حرهٌ‬
              ‫فد‬‫صیه‬
                  ‫بق‬


=== BQT_v2 leaf 282 (printed 822) ===
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

                                                ‫نز ‪.‬‬     ‫(چ‪۲‬ش‪+:‬‬                      ‫‪.‬‬   ‫ونىز‬     ‫چش‪-:‬‬         ‫)‪۱‬‬


   ‫از‪ :‬داور ‪ +‬ی (مصدری) » پپلوی ‪ 017206020‬ر ‪ 01۲2۷6020‬٭ تب رکه )‪۵‬‬                                                  ‫‪۱‬‬
                                                                         ‫‪۰‬‬   ‫‪ :‬داو‬       ‫رك‬     ‫‪۳۴‬‬                   ‫‪.‬‬    ‫داور‬   ‫رك‪:‬‬


        ‫شکمش خاسته همحون دم رویاهان‪.‬‬                          ‫داهان‬    ‫‪ _- ۴‬تاك رز رادید (رزبان)آ ستن چون‬

  ‫‪۱۹۱٩‬‏ ‪.‬‬    ‫«منوچهری‌دامغانی‬
  ‫وداهیم ‪1‬‬   ‫‪ ۹۳ ۹‬از بونانی‪ .‬ره ‪ :‬دهم‬              ‫(«‪.‬م‪.).‬‬    ‫داهول‬     ‫—‪-‬‬    ‫‪۵‬‬                 ‫رلك‪ :‬ده‪.‬‬       ‫‪_ ۴‬‬

        ‫دیهیم ‪.‬‬     ‫«راهم» (ھ‪.‬م‪- (.‬‬      ‫مصحف‬    ‫ياين معنی ظ»‬     ‫‪_ 4‬‬                     ‫‪.‬‬   ‫رك‪ :‬داهل‬         ‫‪- ۷‬‬

                                           ‫رك ‪ :‬داو ‪۰‬‬    ‫٭_‬              ‫‪ :‬داهم ۾ دیپیم ‪.‬‬            ‫رك‬    ‫_‬    ‫‏‪٩‬‬


  ‫‪ #‬دایه ‪ -‬بفتح‌اول وکسرسوم (لهجةمر کزی)‪.‬فی‪ .‬اوتا ‪( 0062‬ماده[ ازجانوران])‪,‬‬
   ‫(شبردادن)‪ .‬ارمنی ‪kaeyad‬‏ (دانه؛مربی)‬                ‫بهلوی ‪( 1212‬دابه) ‪ ۰‬هندی باستان ريشة ‪20 -‬‬
    ‫‪eyûd‬‏ (ازفارسی) ‪ ۰‬افغانیع ‪33‬‬                ‫(مادره دابه)‬     ‫‪îd .‬‏ و ‪( 3۷10‬مادر) ‪niûd ۰‬‏‬                             ‫کردی ‪2‬‬
   ‫(مادر) » در‬      ‫اررامالی ‪2‬‬        ‫استی ‪( 01830 . 711/720‬شیر دادن) » بلوچی ع ‪iãd‬‏ «اسشق ‪۹۶‬‬
   ‫لپجه های دیگر کردی ‪.‬ةل ‪) .‬ةل ‪ 21 .‬وشرء «د‪ .‬اورامان ‪ » ۰۲۱2‬معرب‌آن دابة (ماماه‬
   ‫که از کورك‬        ‫زمائ‪-‬ی‬
                          ‫» شیرده » مرضعه ‏ قابله ‏ ما‬           ‫هنده‬
                                                                    ‫ر‏د؛‬
                                                                       ‫ی‪۰۲‬‬
                                                                         ‫ش‪٤:‬‬
                                                                           ‫قابله) ددری ج ‪ ۱‬ص ‪۲٤‬‬
                                                                             ‫پرستاری کند و اورا پرورش دهد ‪:‬‬
                    ‫کرد زیرپر چو دابه قرمیت ‪.‬‬                    ‫تخم بطی کر چه مرغ خانه ات‬
   ‫«مشنوی ‪۳‬ص‪٥۹۹1‬‏ بنقل نداب ‪ ۵ :۳‬ص‪5۹۰‬‬
  ‫هبارن فاطع‪)۸۰۱‬‬
               ‫(‬


=== BQT_v2 leaf 297 (printed 837) ===
                                                                                                                   ‫‪ ۴۱۳‬بت‬


                                                              ‫هآمده استِ ؛ وباین معنی باشین قرشت نیز‬
  ‫غدارل ‪ -‬بروژن پ هشن‬
                         ‫‪.‬‬    ‫آب ذلك‬          ‫که در یش‬

                                                                                                                   ‫گفته‌اند ‪.‬‬
                                          ‫باشد‬     ‫وه‬          ‫درس حوان د باواوممدوله بروزن‬
‫ب رکاله ‌ راهی را‬    ‫وزن‬     ‫بر‬     ‫درغا له‬                    ‫سخت جان ‪ .‬شا گردرا کوبند » وشخصیکه پیش‬
‫گوبند که ازمیان کوه‌بگذرد وآنرا بعربی شمب‬                                        ‫‪۱‬‬                  ‫بو اند ‪۱‬‬     ‫‪ 3-۳‬ری‬

 ‫وفرجة ميان دو کوه را نز کفته‌اند ‪۰‬‬              ‫خوانند ‪-‬‬      ‫درس ‪ ۱‬د بورزن عرصه » بمعنی درسته‬
                                                                                           ‫است که بش؛ددن وعفو باشد‪.‬‬
                                    ‫‪۰‬‬   ‫قند‬   ‫درحوالی‪-‬حر‬
                                                               ‫درش ‪ ۰‬بح اول و انی وسکون شین‬
 ‫» هرزه‬      ‫وزن یدمست‬       ‫در عست‪ -‬بر‬                        ‫قرشت ‪ ۰‬نام نوعی ازخبارست» وآن پاريك ودراز‬
                                  ‫وناه‌عقول را کویند ‪۰‬‬         ‫میشود ‪ - ۴‬وبسکون انی پایگاه وطوبلة اسبانرا‬
                                                                                                ‫گونند ‪۶ .‬‬
‫دعرلیکی د بالام وبای ابجد وکاف بر‬
‫دار‬     ‫تن ‪ ۰‬درهرا گونن که بره‬            ‫هر هفت‬     ‫ورن‬       ‫‌ کاءه ازمردم کشف‬                ‫در شت ند‬

 ‫باشد ؛ بمضی دري راگوبند که پیش آن پنجره‬                                                                         ‫طبع باشبد ‪.‬‬
 ‫داشته باشد ومردم از عقب پنجره نمابان باشند؛‬                  ‫در شته = بروزن ومعنی درسته است که‬

‫و معنی اول بهتر است چه غلیکن بمعنی پنجره‬                                         ‫وذشتن اکزناه باشد ‪#.‬‬
                                                                                                    ‫ردن گ‬
                                                                                                        ‫عکفو‬
‫‪ :‬وعم ثالث وفتح‪,‬ای فارسی هم نظر | مده‬                ‫است‬
                                                               ‫درشی مه بفتح اول و انی بر وزن‬
                                                 ‫است ‪. 3‬‬       ‫حبشی » بمعنی درش است که خیار باريك ودراز‬
‫م ثالث با زبادتی‌نحتالی‬      ‫‏‪e‬‬   ‫درغلیکس‬                                                                              ‫باشد ‪.‬‬
‫که در‬      ‫ماسن‌کاف و نون ‪ ۰‬به‌عتی درغاسکن ‪A‬‏‬                          ‫‌زشدن‬
                                                                           ‫لا‬‫جبه‬
                                                                               ‫در عرق شدن هخکنا‬
‫پنجره‌دار باشد؛ وبا بای فارسیتا کن‌هم‌درست است‪.‬‬                           ‫وخجلت کشبدن و شرمنده شدن باشد ‪.‬‬
                                                               ‫درغ ؟ = پروژن برق * بتدیراگویند‬

      ‫معرب‌آن بز «درش»*ابن درید» ‪ .‬رکه ‪:‬درشی‪.‬‬                  ‫‪۴‬‬             ‫‪.‬‬       ‫درسته» درشه‪‎‬‬     ‫ر؟‬       ‫‪١‬‬

   ‫‪(22‬آرودی است که‌بسحونریزد‬                  ‫غام ‪0۲‬‬        ‫‪ ۳‬در‬             ‫» (ھ‪ .‬م‪. ‎).‬‬     ‫ورغ‬    ‫«‬    ‫مصحف‬       ‫‪۴‬‬



                             ‫رك‪ :‬درغلبکین ‪.‬‬           ‫‪۵‬‬            ‫‪.‬‬     ‫‪۸‬‬       ‫‪.‬حدود‬    ‫میئورسکی‬        ‫«حجدود الءالم ‪۷۲‬؛‬




      ‫(رأت» سعی کردن ) ‪.‬هندی باستان ‪۲5۳20-‬‬
                                         ‫(جرأت ‪ .‬جارت‪ .‬کوشش) و اوستا ‪ 0156۳31‬ج‬
  ‫‪۰‬‬     ‫وهو‪.‬شمان از ريشةٌ ابرانی‪ 0 ۵6۳5۵۳-‬حدی مزند ‪ ۶‬هویشمان ‪۲۵۵۹‬‬                                        ‫میداند «اسدق ‪۲‬‬
      ‫افغانی ‪« 605۵۷۲0‬هوبشمان‌اضا» ‪ .‬کیلکی ‪405‬نا‪۲‬نا؛ ناهموار ‪ .‬ناصاف‪ -‬زمخت‪.‬سخت » خشن‪-‬‬
                                                                                             ‫غلظ‪ .‬کشف رك‪ :‬درشتی ‪۰‬‬

  ‫‪ ۵‬دشرتی ‪ -‬حم اول و دوم‪ « .‬از‪:‬درشت ‪ +‬ی (مصدری) ؛ درشت بودن » سختی و ستم‬
      ‫تندی‪(« :‬شاهدان) تا خوب و لطیفند درشتی کنند وچون درشت شوند تلطف‬                                  ‫با جور ‪ -‬ترش‌روبی ‏‬
                                                     ‫کنند و دوستی لمایند ‪« ».‬کلتان ‪. ۱۶۱2‬‬
   ‫مأخون از آلمالی‬           ‫‪ ۵‬درشکه ‪ -‬بطم اول و دوم و کمر چهارم ‪ .‬از روسی ‪۴020۳‬‬
   ‫‪6‬درشکه)؛ گردونۀ چهار چرخه که با اکسشبیده شود و اطافکی برای حمل مسافر‬                ‫(‬
                          ‫دارد که‌مقف آلرا میتوان بلند کرده برافراخت وبا تاکرده خواباند ‪.‬‬
```


## [2026-09-05T18:18:30.857Z] TOOL CALL #26: Bash

```json
{
 "command": "pdftoppm -f 123 -l 123 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg123 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 123"
}
```


### [2026-09-05T18:18:33.133Z] TOOL RESULT

```
total 35824
drwx------ 3 sfmqrb sfmqrb     4096 Sep  5 14:18 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb     5133 Sep  5 14:10 c_avestan120.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18289 Sep  5 13:48 c_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13620 Sep  5 13:48 c_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10949 Sep  5 13:48 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15141 Sep  5 13:51 c_hektaton.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb    18737 Sep  5 13:51 c_kent.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10687 Sep  5 13:48 c_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13469 Sep  5 14:10 c_latin120.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    63862 Sep  5 13:46 mk110.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48342 Sep  5 14:00 mk113.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61685 Sep  5 14:01 mk114.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60434 Sep  5 14:01 mk115.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76964 Sep  5 14:09 mk116.py
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
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  5 14:17 p117
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
-rw-rw-r-- 1 sfmqrb sfmqrb   117231 Sep  5 13:48 pg114_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1253 Sep  5 13:48 pg114_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11671 Sep  5 13:48 pg114_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83933 Sep  5 13:46 pg114.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163144 Sep  5 13:51 pg115_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70699 Sep  5 13:51 pg115.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64811 Sep  5 13:57 pg117.png
-rw-rw-r-- 1 sfmqrb sfmqrb    42354 Sep  5 14:05 pg118.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78691 Sep  5 14:11 pg119.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84971 Sep  5 14:10 pg120_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50224 Sep  5 14:06 pg120.png
-rw-rw-r-- 1 sfmqrb sfmqrb   330167 Sep  5 14:18 pg121_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82335 Sep  5 14:17 pg121.png
-rw-rw-r-- 1 sfmqrb sfmqrb   461010 Sep  5 14:18 pg121_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61026 Sep  5 14:18 pg123.png
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


## [2026-09-05T18:18:33.403Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT darsa / daenu ===\"; grep -n \"daenu\\|daēnu\\|dainu\" BRT.txt | head -10; echo \"--- darš adverb ---\"; grep -n \"darsam\\|daršam\\|darši-\\|darsi-\" BRT.txt | head -10; echo \"--- dānō-karša ---\"; grep -n \"dānō\\|dano-kar\\|dänö-kar\\|karsa\" BRT.txt | head -10",
 "description": "Bartholomae greps"
}
```


### [2026-09-05T18:18:33.494Z] TOOL RESULT

```
=== BRT darsa / daenu ===
8811:daenu  arpjs  "um  den  Preis  fiir  eine  Kamel- stute" V.7.42;  —  'ranqm  (GPf.)  dalnu- Mm  paiti.puiranqm  A.j.io.
10122:—  päitm  'Jus  arsn3  Yt ij. 55 ;i4-T,  V. 22. 2o;  —  Äazannm  'avqm  da!nunqm  (sd.)  A. _J.  8;  —  °ava  dainu  anjö  V.  7.42 ;  —  'itts paiti  atyS  (sd.)  .  .  'Std  paiti  fravaitya (sd.)  .  .  'Stil paiti  vasyä  (sd.)  V,  g.  37  f.;
13389:•  j.  'dänav-  f.  'Fluss,  Strom':  ■'nus  . .  *frä bunät  laHntis  "ein  aus  der  Tiefe  (der  Erde) her  strömender  Fluss"  Aog.  77.  IN.  52: lies  dainunam\
20870:zieht,  in  dea  Relativsatz  hereingenommen ist:  *sindä  (sd.)  .  .  yi  Ji  sSnghs  (sd)  .  . ämjö  dtmam  ääai  "perpetra  (sententiara) quae  sententia  .  .  imponat"  Y.  5/.  14;  — daidita  . .  *yri  (APf.)  da  .  .  mäyä  (sd.) "accipiat  (beneficia)  quae  dabis  . ,  bene- ficia"  Y.4IJ.  a;  —  yS  ■  •  vandayaitä  (sd.) yqm  nasdistqm  gai^qnt  drtgva  baxsaiil "qui  . .  auxerit  (dominium)  quod  domi- nium ..  habet"  Y.  50. 3;  —  advämm  .. yä  .  .  urvSxiat  (sd.)  hyat  *c)vUtä  ..  f/tfs- d>m  (sd.)  ". ,  (ad  praemium)  quod  desti- natum  est  praemium"  Y,^^.  13;  —  *»>?«- däidyäi  yä  (Sp.  1214  ra.)  töi  .  .  adisiis y3{NPn.)cä  vo/iB  uxts  frasT  mananhä yäcä  aSa  ".  .  et  (verba)  quae  verba  ,  . interrogavi"  Y.44-8;  —  «/  . .  vax^ä  .. siaoiacä  . .  yesnyäcä  . .  humazdrä  (sd.)  a^ä \yel^'S,l)^  yä  (NSt)  rtUmiS  dansatä urväzä  ". .  et  (voluptatem)  quae  una  cum Aso  quae  una  cum  luce  videatur  voluptas" Y._jo.  i;  —  kä^a  tnSi  yqm  yaoi  dalnqm *yaoidäm(sd.)  .  .  paitiss  sahyäl  .  .  asislls (sd.)  ".  .  (animae)  quam  animam  puri- ficem  .  ."  Y.  44. 9;  — ■  ist  daivSng  dqn yä  (NSf.)  dngvatS  dainu  ".  .  (animae) quae  (est)  faÜacis  anima"  Y.  49-  4 ', d3t?hs  (sd.)  tr^züs  pa%S  yqm  dalnqm ahurS  . .  dadat  ". .  vias  (religionis)  quam religionem  Ai.  . .  instituit?'  Y.  5_J.  2 ;  — hr3X%qm  . .  k^hrpsm  . .  dainayäi  vanhuyai ■[yqm  hdi  isyqm  (sd.)  däiü  .  .  aidyäi ". .  den  Leib  (der  lieben),  welcher  lieben . ." Y.  5/.  17.  ß)  adjektivisch:  yä  (NSf.) daliUI  . .  hanät  mTidfm  asahyä  yasä  ahm (wörtlich)  "welches  Ich  . .  verdient,  (dem) wünsche  ich  .  ."  Y.  54.  i ;  —  drBjS  hacä ra%>mi^  \y}m>  (ASm.)  "j/fl/KäJ(sd.)  fräi- dXm  [drBjs]  äyess  (sd.)  ".  .  quem  videtis successum  (cum) . ."  Y.  5^.  6.  Vgl.  noch Sp.  1216  t    unter    b.  b)    im    jAw.;
--- darš adverb ---
12998:Zum  V.  dari:  —  1)  NA,  liest  darsam  'sehr'; aber  Um  kann  nicht  von  hacä  abhängig  ge- macht werden.  Falsch  anch  FoV  KZ.  35.  31. Vgl.  iF.  Bthl.  Handb.  86;  S  403. ■  j.  daräyav-  Adj.  'kühn,  stark',  vom Wind:  vätahe  k?hrpa  *'syaoi''>  \t.i^.2.
28986:imam  daAylum  a'^ur^matdä  pätuv  Cser- vato')  A'  Aainaya  D.  4-  3;  3%  ö'.  5;  — Ä'  draug^  darsam  patifiaytritvit  ('cave') Bh.  4.  s;   in  eigentümlicher  Konstruk- tion (s.  rautaft-);  niyaltäyam  imäm  yuvi- yäm  fsd.)  ia'tanaiy  ('fodere')  A'  pirävcl' näma"  raut^  abiy  *draya*  .  .  D.  77. 3.  b)  bei  Nomina;  a)beiRaumwörtem: pärst^  martiyc^  *därayapiy  A°  pärs!^ Aamaram  (sd.)  patiyajatä  D.6'.4;  —  imS daAyäva^  tyit  . .  agarbäyam  apataram  '^sd.) /;•  pärti^  D.  6.  3.  ß)  sonst:  imn  daAya-
--- dānō-karša ---
4955:barqn  'va  ait>m  nmütam  V,5.4i;  —  Hai^  %iia  (sd.)  aoi  ava  asnavät  P.  2/;  —  "<■«/ ..  avaMmU  -m  «(//.iwffi  (sd.)  karsaya  as5  Vyt  25;  —  yat  he  'vat  pourum V.p.i2.  a)  in  Verbindung  mit  ä  dn.:  ubjyäite  (sd.)  V.7.S2PÜZ.  a)  auf  die ka%S  drußm  nJ/aAmai  3  fiT/.>t3säm3  (&d.}  a.Vevson  bezüglich  'iste':  sarJt  bß~dyrii.. fing  ä  'vä'>ydi..\.44-^2-  2)Praev.(mit  =1,«  ma^rs  >^..  "..gemäss  jenem  (deinem) '£an;gan-,gam-.'bar-,si,l-\ß«.}.  a)  bei ;  Spruch  .  ."  Y.  44.17;  —  cis'ca  '^wam Ellipse  des  Verbums:  t»m  janäi  .  .  k>n-  Jakarta  'va  masanaca  vatahanaca .  .  "Jeder s.lipJ  'va  '>  apaMm  (sd.)  gayeAe  Yt.  /().  44.  hat  dich  gern  gehabt  wegen  jener  (deiner) KompA.  i  Abldt.  ^  a^rS).  -  S._  auch  a-^ö  ~-  ^  q^q^^^  ^^^  .  .'■  H.  2. 11 ;  —  ai/at  tljas.lni ai.    ai'fl   Fraen.,   Praev.j    mp.  n  dm.    —    I  u.  .,  -  ,,  ,     ,
7012:—  7)  Hdi.  äijjf;  s,  Xo.  6.  —  s)  Die  Hds.  S4-  A)  zusammen  mit /a«a,/aji:aa'a  und mit  Pü.  und  entsprechend  die  NA.  teilen  /^/;  ,70  pasca  di'a,dasa  karsa  frakSraySH faIschIicbhiBterü«^-ab  rä:fl/o^«a-^4-ü«//  y^an;  —  ä'  pascaita  ..  V.5.3,  j.52; ,^ä«zk(No.aiV-wFiusff.;NA.ji/-.»™.-i—  «^  P^'"  «oa/  Aißaiti  ..  (tf/ryH  ..  3' '"')  NA.  ääqm;  s.  No.  6.  —  <')  Nur  gAw.  und  1  tat  dunmqn  hqtn.füstfnti  .  .  ä'  fai  dunmqtt
7024:ff(rai>/(Stverz.)  «^«röMasi/J  V.2, 1  f.,  usw.;'eines  koordiniiten  Satzes  an  das  Voraus- Y.p.z.s,  16,  7J.2,  V.j&ai,  H.  2.ii,Nik.  2, 1  gehende 'und';  die  zeitliche  Folge  tritt  min- yyt.8,22;  —  ä3tar3..kd  avalia..vl.l>arat..}'  dest  sehr  zurück;  a)  eines  Hauptsatzes:  tarn a°  aoxta  ahurö  mazdä  V.  2.42;  40,  Yt  5.  ^yatata  haofyauA^  .  ,  ä'  Alm  jaloyal  Yt. 9°>  95!  —  ahmäi  fradaisaSm  dainqm  .  .  ij.2^{.;  5.18,  5.17,  /j.40;  —  vagiipmnsm ä°  hl  mraont  .  .  visanha  mg  yima  .  .  ä'\  *apa  karsayjn  Jainis  .  .  ä°  tä  .  .  hazö ml  alm  paityaoxta  yimS  .  ,  ä"  h!  mraom  '  nivamay?n  (sd.)  Yt.  /5.80;  —  J  tat  han- .  .  ä'  mE  aem  paityaoxta  .  .  ä"  kl  saya  [jamarum  paiti.jasat .  .  ahurö  mazdä  .  .  ä° "       ■    "    "  ahurff  riazdfv.  2.21  f.;—  ,iat{s.  8}
9202:'einfurchen,  (Furchenstriche,  -streifen) '.  —  yaia  gaz'ishva  (sd.)  vasS.xsahrS ziehen":  karsaim  (sd.)  kirayeiti  Yt.4.4.     ,/racarane  Y.g.iT,  —  aat  hva  pasu  vTra
9204:mit /rJ  'durch  Einfurchen  herstellen':  (sSPrM.)  Vt.ij.  107;  —  aü?..  fr  acaraiti karsasiit  (sd.)  frakirayjis  tiyra  xi'a'ira  \*antan.ar/6}m  nm3nahe  Yt.  iS.  4;  3;  — *vairya  V.^,  10;  11',  F. 5;  —  nava  karsa.vasS.xsa^rS  (näml.  jran//')  *fracaraite  aoi frakJrayat  "neun  Furchstreifen  zog  er"  ^y^m  ..  gas%qm  ¥.57.34;  —ya'i:a..anJzarvtä \.22.ao; — yS  ZJinS  tisrS  kari^a/rak3ra-\.  .  yahm  (näml.  fravasayS)  fra^ara'imie yHH  N.;o/;  YL4.63.  (2PPM-)  ¥1/^.34.         2)  mit  Akk.  'hinzu
11373:—  daryyaäi"'>  bäzava  Yt  70,104;  — pourucil  ü^aAe  N.  6^;  —  *vanaite  akimat man3  Yt.  ig.  g6;  —  aspaat  ysi  mi%rö.- drujqm  .  .  Yl  10.  20;  Aog.  4^;  —  karsas- Ht  frakaraysis  Y.g.  10;  zit  *Y.y,  — autark  *kä%rwtHi  N.  /09;  —  tarS  p>rp- tümcit  Y.ig.6;  —  Aandarpzaat  /landar?- zaym  V.(?.  49;  —  urvähqmät  zbayant avi  . .  Yl  12.  3;  —  ianvasAf  :^ahya  uita- n?m  Y.  jj.  14;  verwendet  Y.  1/.18,  /j.4;
13961:.  j.   dva.dasa   indekl.   Zw.   'zwölf:    .,^1  V.Ä7o;7i,  V.p.16-24'»;  — «(Sp._6ai  o.) karsa  frakäraySis  V.  g.  n;   72.  8    14  14  ^^'"-'^  ^'^  ^^^  <^^^  "*"  druxs..upa.- KompA.;  Ableit.   -    ai.  vgL  dvAdaia  indekl.   '^^■''"'*'  "^-l-  ^4;    —    <irvxl  .  .  yä   haea Zw.  —  Pü.:  12.  \irista  upa  jvaiititn   upa.dvasaüi  V.  10.  i'K
19526:•  j.  'maj^-  m.,  mayä-  f.'>  'Loch  im  Erd- boden, Grube':  srvabya  (sd.)  'f»m  ava.- kanöis'V.iy.T,  5,  F.i7; —  baTvari  'yanqin (GPf)  irimaitinqm  aiühh  z?mö  aipt.kan- yät  V.  14. 6.  a)  insbes.  von  den  zu Zwecken  ritueller  Reinigung  gegrabenen Lochern":  mazdayasna  aiäAa  z?md  %rii (sd.)  'yjm  ava.kanay>n  dva  'fa  frasnä^aym malsmana  giul  *Bim  äp3  "die  Mazday. sollen  in  der  Erde  drei  Löcher  graben, zwei  Löcher  —  da  sollen  sie  mit  Rindsurin waschen  — ,  eins  —  mit  Wasser  — "  V.  76'.  1 2 ; Ä37; — paoirtm  upa  'fim  nt^w^>söis . . iitim  Ufa  . .  xltUm  upa  . .  "hrayS  anya  'ya ni^TVinssis  "ein  erstes  Loch  sollst  du  aus- stechen, ein  zweites  . .  ein  sechstes  . .  drei weitre  Löcher  sollst  du  ausstechen"  V. p.  6  ff.;  70. 18;  —  ^rJyS  yim  antari  vlta (sd.)  atitan  %räyS  {xh/as,  novo)  'ya  fra^ iärayBisY.g.  ii>;  11',  12,31; — arttanca (sd.)  .  .  'ya  (NP.)  V.p.  11;  —  karsascit frakäraySiS . .  ^ai  hala  'yaHbya  V.p.io; 29;  — paoirJfn  upa  *yim  frä.nasui  nanm (statt  NS.)  bavaiii  "am  ersten  Loch  . ." V.p.  28;  3iJ;  —  US  tansm  snayaSa  us vasirät  (statt  AP.)  gius  maSsmana  qpäca nava  (sd.)  upa  °ypm  "er  soll  seinen  Leib und  seine  Kleider  bei  den  neun  Löchern , .  waschen"  V.5.  54.
28959:irf.12;  —  pairi  dim  tanava  ('distinebo') ..  urvSmm  h°  vahiltat  attkaot  y.ig.T, 7/.  IS;  —  kö  .  .  a'^rB  ta/nus  darayat ('detinuit')  tanaot  h'  masyeht  V,  20.  i ;  — '  va^>mn>m  .  .  äalva  .  .  *apa  karsaym ('deripicbant')  jainii  h'  maiyakaäbyd  Yt 715.80;  —  ya'ia  vthrkB  .  .  barti^ryai  A' pu^r^m  niidaiydairyat  C^npiat')  V.JÄ38; —  vivaiti  ('fiigat')  Ai^  zrayaahai  A'  vouru- ka^SI  YtÄ4o;  —  Hyris  . .  yim  aaAal { jeci t')  »nxsd . .  airyöjcsu%  at  A'gardi^  s^an- vanttm  avi  gairlm  Yt. 8.6;  —  yS  ATm (näml.  daOtqm)  . .  utvasat  ('expedivit')  h° hinaiwyö  .  .  Yt,  13.  100;  —  upa  . .  naad rafS^wat  nänhanat  h'  ". .  intrabit  fa  naribus sva.)  per  nares"  V.J.  14;  —  s.  noch  unter bß(Sp.i749  0.)dieStcUenY57.i4,  V.33, y.3. 16, 13. 17.  ß)  bei  anderen  Verben; yS  naomyaSt  A'  daitihaol  . .  xrßm  (sd.) i»'zci>i7Ai(»'A' ('conspicit')  Yt/4.33;/6. 10;
```


## [2026-09-05T18:18:43.136Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -B3 -A6 \"daenu  arpjs\" BRT.txt | head -40; echo \"=== dana- korn ===\"; grep -n \"dänö\\|dano\\.kar\\|dänav\\|'dana-\\|dana-\" BRT.txt | head -20",
 "description": "Bartholomae daenu entry"
}
```


### [2026-09-05T18:18:43.196Z] TOOL RESULT

```
8808-'uStra-
8809-ka-I  I
8810-422
8811:daenu  arpjs  "um  den  Preis  fiir  eine  Kamel- stute" V.7.42;  —  'ranqm  (GPf.)  dalnu- Mm  paiti.puiranqm  A.j.io.
8812-'»  Das  weilv ollste  Tier  unter  den  ilaorii- ir.rossvieh)  nach  V,  7.  42.
8813--      ,,>A.,  E.  -  Vgl.  -   -        —
8814-."'-  f-.
8815--  Pii.i  .
8816-•  j.  'ustra-  111,  EN.  eines  Gläubigen:  'tnhe ta-janatshi^  aiaonS  "des  f.,  Sohns  des S.  ..'•  \t  13.115.
8817-Vgl    '«.;/,a-.    -    ai.   uil.a-    m.    EN.    (eines
=== dana- korn ===
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . ." V't.  jj-sif.;  Y..;j.6  (s.  2  2  aa);  —  auch bei  Beziehung  auf  das  Subjekt  des  Satzes: (ya^a)nar>m ..  asavamm*jas?nSfm  ahmya nmjne  .  .  paiti  taröpi^wim  dai'i^yät  "als ob  er  einen  Gläubigen,  der  in  sein  (zu ihm  ins)  Haus  kommt  .  ."  V.y.aa;  — naSca  ,  .  *hö  nl  ahmat  haca  gätaot  isaetci fraiütöip  nöit  apaiiitöit(%A.)'B.23.  b)  sub- stantivisch: adä  (sd.)  ta^a  guti  p>r9- sat  as>m  .  .  ahmäi  asä  (als  Subj.)  ,  ■  paitl.- mravat  Y.ag.ii.;  30.t,  46.8,  13;  —  uz- valoayat  zara^ustrS  annm  mainyUm  .  . paiti  ahmäi  adavata  .  .  aarS  mainyus  .  .
3533:•  p,  apa-dana-  n.  'Schloss,  Palast':  "imam
4006:—  Vgl.  gaodana-.  —  Pü.:  transski.  (als  EN.).
5718:FamÜie:  yat  bavama   atim.vanyä   dänavö  ^/ndäu'a'i     aMatca     zimäatca    Vr.  7.  4;
7354:•  p.  ä-yadana-  n,  'Stätte  der  Göttcrver-
9235:alavazdä..yatbavämaa,tut.vanyädänavs  ^^^^  ^^^^      -^  „^^^^_^^  ^...  ^„.,,„,^„^^
9399:•  j.  kasu.dänav-  Adj.  'mit  kleinen  (Samen-)
13389:•  j.  'dänav-  f.  'Fluss,  Strom':  ■'nus  . .  *frä bunät  laHntis  "ein  aus  der  Tiefe  (der  Erde) her  strömender  Fluss"  Aog.  77.  IN.  52: lies  dainunam\
13393:•  j.  'dänav-  Adj.,  bezeichnet  einen  den  Ira- niern  feindlichen  i'Srischen  Volksstamm: tala  yöi  taxma  xstüvayS  'nubyS  az)n  p?sana yüz»tn  (näml.  /ravasayj)  tdm  taurvayata v>r?^r?m  'nunqtn  türanqm..t6al^3  'nunam türanqm  .  .  xrBma  asSbis  frasinta  (sd.) "nunqm  baivari.pailinqm  Yt-/J.  37f.;  — yat  baväma  aiwi.vanya  °nav3  (als  AP.) tära  vyäxana  Yt.  J.  73.
13395:•  j.  ^dänav-  £  ' (Getreide) koro'.
14930:8^9  '*'paiti£a.gaodana-
14931:•  j.  *paitida.gaodana-''  Adj.  'verschiedene
15007:•  j.  paitinqm.  gaodana-  Adj.  'verschiedene Schüsseln,  Näpfe  benützend,  aus  ver- schiedenen Schüsseln  trinkend':  paitinam.- i^ariia  (sd.)  'na  (ND.)  N.  64.
17993:•  j.  frazdänav-  m.  Name  eines  Sees": tarn  {\^m\.ar3dvim)yazala..kava  vistäsps *'pasne  äp>m  'naom  Yt5. 108;  —  yazäi ap^m  'naom  ¥.4^.
17996:iura  V.  Ja-  (ar.  dAä-yi+dänav;   mit   HaploL
19014:•  j.  naramyazdana-  m.  EN.  eines  Gläu- bigen: 'nahe  äii<wyaoi  asaonH  Yt  13.  iio.
20982:I33I  *yaona-  —  '''yaoidana-  1333
22064:•  g.  vaedana-  Adj.,  PPfM.:  s.  'vaid-.
22282:•  j.  vaf'dana-  n.  1}  'Kopf  uzw.  ahurischtr ;  Wesen'';  a)  des  Menschen:  nar^ maomyehe I  'Uim  F^a;  ^b,  V.5. 11,  (5.  aa;  —  pasca
22904:•  p,  vardana-  n.:  s.  unter  vtniSna-,
```


## [2026-09-05T18:18:44.784Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD dān / dāyag / durušt ===\"; grep -n \"^dān\\|^dāyag\\|^dayag\\|^dan\\b\\|^durušt\\|^dury\\|^dāng\\|^dang\" PHD.txt PHD_mackenzie.txt | head -30",
 "description": "MacKenzie Pahlavi entries"
}
```


### [2026-09-05T18:18:44.834Z] TOOL RESULT

```
=== PHD dān / dāyag / durušt ===
PHD.txt:1487:danger sēj; free from ~ asēj.
PHD.txt:1488:dangerous sēļāmand.
PHD.txt:5560:dān, gyān baw-!
PHD_mackenzie.txt:1870:dan(all) [d'n(k) I I N ,...,a] seed, grain.
PHD_mackenzie.txt:10971:dan, gyan
PHD_mackenzie.txt:12011:dan-I                       -\\~        ....   anagr-rosn              ,~~ ~""
```


## [2026-09-05T18:18:54.725Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"dayag\\|d'yk\\|dāyag\" PHD_mackenzie.txt PHD.txt | head -10; echo \"=== durust/durušt ===\"; grep -n -i \"durušt\\|durust\\|drwšt\\|dlwst\" PHD_mackenzie.txt | head -10; echo \"=== dang ===\"; grep -n \"^dang\\|dang \\[\" PHD_mackenzie.txt | head -5; echo \"=== BRT daenu headword ===\"; grep -n \"• j\\.  'daenu\\|daenu-\\|dainu-\" BRT.txt | head",
 "description": "MacKenzie and Bartholomae entries"
}
```


### [2026-09-05T18:18:54.822Z] TOOL RESULT

```
PHD.txt:310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
PHD.txt:2948:nurse, (wet-) dayag.
PHD.txt:2949:nursing, nurture dayaganih.
PHD.txt:5577:Чадан! däs, "*gāh gāhwārag dār-! dārišn! даап! dāsār yāsaman gahbedīh gahbed dahigān Gayomart dahibed dāyagānīh dāyag
PHD_mackenzie.txt:1953:daya~ [d'yk l I M d'yg-, N --a] (wet-)nurse.
PHD_mackenzie.txt:7192:nurse, (wet·) dayag.                   oppressive stahmag, starnbag.
PHD_mackenzie.txt:7193:nursing, nurture dayaganih.            or ayab.
PHD_mackenzie.txt:10992:danistan                    , ,te..U t""U        dayaganih
PHD_mackenzie.txt:10996:                         -~~K'                   dayag
=== durust/durušt ===
2089:drust [drw(y)st l I (M dryst), N durust] right; well, healthy.
=== dang ===
5341:widang [wtng I P wdng] trouble, distress, constraint.
=== BRT daenu headword ===
```


## [2026-09-05T18:19:02.455Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD dhers ===\"; grep -n -A12 \"^dhers-\\|dhers-\\.\" AHD_watkins1985.txt | head -30; echo; echo \"=== AHD dhe(i) ===\"; grep -n -A20 \"dhē(i)-\\|^dhe(i)-\\|dhei-\" AHD_watkins1985.txt | head -40",
 "description": "Watkins AHD roots"
}
```


### [2026-09-05T18:19:02.529Z] TOOL RESULT

```
=== AHD dhers ===
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
380-14
381-dhg“hei-
382-blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
383-dhg“her-
384-dhgvher-. To run. Perhaps Greek phtheir, louse: (ICH), PHTHIRIASIS. [Pok. g¥hdher- 487.]
385-dhigv-. To stick, fix. 1. Germanic *dik- in: a. Old English dic, trench, moat: DIKE, DITCH; b. Old French digue, trench, perhaps akin to the source of Middle English diggen, to dig: DIG. 2. Latin figere, to fasten, fix: FIBULA, FICHU, FIX, (FIXATE), (FIXITY), (FIXTURE); AFFIX, ANTE- FIX, CRUCIFY, INFIX, MICROFICHE, PREFIX, SUFFIX, TRANSFIX. [Pok. dhéigy- 243.]
386-dhragh-. To draw, drag on the ground. Rhyming variant tragh-. 1. Germanic *dragan in: a. Old English dragan, to draw, pull: pRaw; b. Old Norse draga, to draw, pull (or Old English dragan): DRAG; c. Old English drexge, dragnet: DRAY; d. Old Norse *drahtr, drdttr, act of drawing, akin to the source of Middle English draught, a pull: DRAFT. 2. Russian drogi, a wagon: DROSHKY. See also variant form dhreg-. [Pok. dheragh- 257.]
387-dhreg-. To draw, glide. Variant form of dhragh-. 1. Na- salized Germanic form *drinkan, to draw into the mouth, drink, in Old English drincan, to drink: DRINK. 2. Nasal- ized Germanic form *drankjan, “to cause to drink,” in: a. Old English drencan, to soak: DRENCH; b. Scandina- vian *drunkna, drugna, to drown, akin to the Scandina- vian source of Middle English drounen, to drown: DROWN. [Pok. dhreg- 273.]
388-dhregh-. To run. 1. Greek trekhein (< *threkhein), to run (> trokhos, wheel): TROCHAL, TROCHANTER, TROCHE, TROCHEE; TROCHOPHORE. 2. O-grade form *dhrogh- in Greek trokhileia, trokhilia, system of pulleys, roller of a windlass: TROCHLEA, TRUCK!, (TRUCKLE). [Pok. 1. dhregh- 273.]
389-dhreibh-. To drive, push; snow. 1. Germanic *driban in Old English drifan, to drive, rush: DRIVE, DROVE?. 2. Germanic noun form “driftiz in Old Norse drift, snow- drift, and Middle Dutch drift, herd, both akin to Middle English drift, drove, herd: priFT. [Pok. dhreibh- 274.]
390-dhreu-. To fall, flow, drip, droop. 1. Extended form *dhreus- in Germanic “dreusan in Old English dréosan, to fall: DRIzzLE. 2. Extended o-grade form *dhrous- in: a. Germanic *drauzaz in Old English dréor, flowing blood: DREARY; b. Germanic *drasjan in Old English driisian, to be sluggish: DROWSE. 3. Extended zero-grade form *dhrub- in: a. Germanic *drupan in Old English dropa, drop: Drop; b. Germanic *driipjan, to let fall, in Old Norse driipa, to hang down: DROopP; c. Germanic *drupjan in Old English dryppan, to drip: DRIP. 4. Suf- fixed zero-grade form *dhrubh-yo- in Greek thruptein, to crumble: LiTHoTRITy. [Pok. dhreu- 274.]
391-dhreugh-. To deceive. Germanic suffixed form *drau(g)ma- in Old English dréam, vision, illusion, dream (but attested only in the senses of “joy,” “music”): DREAM. [Pok. 2. dhreugh- 276.]

=== AHD dhe(i) ===
```


## [2026-09-05T18:19:09.933Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"dhé(i)-\\. To suck[^]]*\\]\" AHD_watkins1985.txt | head -3; echo \"---\"; grep -n \"To suck\" AHD_watkins1985.txt | head -5",
 "description": "Find AHD suck root"
}
```


### [2026-09-05T18:19:10.019Z] TOOL RESULT

```
---
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
995:spit!. 2. Germanic *speiw- in Old English spiwan, spio- wan, to spew: SPEW. 3. Germanic *spait- in Old English spatl, spittle: sPITTLE. 4. Germanic *spiit- in: a. Middle English spouten, to spout forth: spout; b. Dutch sputte- ren, to sputter, akin to the probable Low German source of SPUTTER. 5. Zero-grade form *spu- in Latin spuere, to spit: SPUTUM; CUSPIDOR. 6. Zero-grade form *(s)pyu- in Greek ptuein, to spit: HEMOPTYSIS, PTYALIN. [Pok. (s)p(hjieu- 999.] srebh-. To suck, absorb. Zero-grade form *srbh- in: a. Germanic *surp- in altered form in Dutch slurpen, to slurp, lap: SLURP; b. suffixed form *srbh-é- in Latin sorbére, to suck: ABSORB, ADSORB, RESORB. [Pok. srebh- 1001.] srenk-. To snore. O-grade form *sronk- in: a. Greek rhonkos, rhonkhos, a snoring: RHONCHUS; b. Greek rhunkhos, snout, bill, beak: RHYNCHOCEPHALIAN. [Pok. srenk- 1002.] sreu-. To flow. 1. Suffixed o-grade form *srou-mo- in Germanic *straumaz, stream, in: a. Old English stréam, stream: STREAM; b. Dutch stroom, stream: MAELSTROM. 2. Basic form *sreu- in: a. Greek rhein, to flow: RHEO-, -RRHEA; CATARRH, DIARRHEA, HEMORRHOID, RHYOLITE; b. suffixed form *sreu-mn in Greek rheuma, stream, humor of the body: RHEUM. 3. Suffixed zero-grade form *sru-dhmo- in Greek rhuthmos, measure, recurring mo- tion, rhythm: RHYME, RHYTHM. [Pok. sreu- 1003.]
```


## [2026-09-05T18:19:23.614Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB durušt/dāya ===\"; grep -n \"durust\\|duru.t\\|dāja\\|daja\\|däje\\|daye\" HUB.txt | head -20; echo; echo \"=== CHEUNG dars ===\"; grep -n -i \"\\*dar\\?š\\|darš\\|H2dars\\|dars-\" CHEUNG.txt | head -20",
 "description": "Hübschmann and Cheung"
}
```


### [2026-09-05T18:19:23.682Z] TOOL RESULT

```
=== HUB durušt/dāya ===
2108:erwarten. Ich kann np. durust ganz, voUstandig,
2109:richtig, wahr, gesund*, paz. durust, drust ganz, voU-
2113:552. Np. duruSt rauh, grob, derb, hart (afgh. LW. durust
3631:und zu zd. nivaedayemi 'ich kiindige an* gehdren konnte,
6093:^= ^drusfa- (oben p. 61) ; durust 'rauh, grob' = "^drusta-
6144:ins Altpersische zuriick. Vgl. altpersisch: duruxtam, erlogen ,
6156:daratj Spandiat^ Spram, Stahr u. s. w.); pazend durust
6157:gesund' Shk. 242, Min. Gl. 66 = np. durust (s. oben p. 61).
7194:dayemi gehort, im lS^,*nuvai lauten sollte. Vgl. H. 1053, oben p. 103,— 208 —
10419:duruat 61.
10420:durust 61.

=== CHEUNG dars ===
5068:*OLD PERSIAN: dars- ‘to dare’ — Kent: 190b 
34038:dars-, 62 
56177:*darš , *Hmard, *ka(H)ud,
```


## [2026-09-05T18:19:25.551Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC dhers ===\"; grep -n \"^dhers\\|^dhers-\\|dhersō\\|dhrsus\" IEC.txt | head -10; echo \"=== IEC dhe/dhena ===\"; grep -n \"^dhēnā\\|^dhēnu\\|^dhōnā\\|^dhēi\\|^dhē-\" IEC.txt | head -20",
 "description": "Mann IEC"
}
```


### [2026-09-05T18:19:25.624Z] TOOL RESULT

```
=== IEC dhers ===
3023:dhorsios (variant of dhrsus, dhrsnus, q.v.) *daring, harsh, violent Av. dar&is “harsh, severe’; daros-, v. ‘dare’; Ober. darš-, v. id.; MHG ters ‘bold’
3192:dhrsnu- (dhrsun-) (variant of dhrsus, q.v.)
3195:dhrsus, os, is ‘bold’. Cf. dhrs-, dhrsnu-. WP I, 864 & 871 Skt. (variant) dhrsnuh; Av. cf. (o-gde) daro&- “dare”; darsis ‘violent’; Tokh. A tsrasi, B tsir ‘strong’; Arm. cf. darn ‘severe’; Gk. thrasüs, tharsüs “bold”; thársos, thárros ‘courage’; W dry ‘pert; LOIr. drenn trough! (ambig.); OHG turi, MHG türre, MLG dürre ‘bold’; Go. cf. ga-dauürsan ‘dare’; OCz. cf. drsati ‘to be bold, dare’; drstny, Cz. drsný “harsh?
3201:dhrsus, os, is — dhubhlos
=== IEC dhe/dhena ===
2756:dhēiô dhēmi (2) ‘put, lay’. Cf. dhídhemi, dhesnos, dhetis, dhētos, etc. WP I, 827-820 and cf. also dhedh-, dhesio Ober da-; Tokh. AB Gs, B tes- (= Skt. dhàsyàmi: Arm. edic: Gk. thésó: Li. désiu &
```


## [2026-09-05T18:19:32.404Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB 552 ===\"; sed -n '2105,2125p' HUB.txt; echo \"=== HUB p.61 ===\"; sed -n '6085,6100p' HUB.txt",
 "description": "Hübschmann durušt"
}
```


### [2026-09-05T18:19:32.458Z] TOOL RESULT

```
=== HUB 552 ===
dur6d (Nr. 555) aus *duiruvata;t'. FUr skr. drdhd- 'fest,
hart, stark, dauerhaft, ganz' (WZKM. 7, 374) = zd.
^dareida- oder *dareSta^ ware im Persischen *dis^ zu
erwarten. Ich kann np. durust ganz, voUstandig,
richtig, wahr, gesund*, paz. durust, drust ganz, voU-
standig Min. Gl. 66 (LW. bal. drust^ afgh. drast ganz,
vollstandig' u. s. w.) nur auf ein iran. "^drusta- = skr.
*drutta-- u. s. w. zuriickfiihren.
552. Np. duruSt rauh, grob, derb, hart (afgh. LW. durust
'rauh, hart streng, miirrisch) setzt ein iran. ^drusta^
voraus. Aus ^drsta^ (= skr. dhr^fd^ *keck, frech*) ware
np. *dist geworden.
553. Sicher ist hier nur die Gleichung: np. dirafS = phi.
drafs = arm. draus =■ zd. drafSa- Banner, Fahne.
Die Vermutung uber die Etym. von np. duruxs ist sehr
ungliicklich. Np. dirafStdan *to flash' JRAS. 1894,
p. 461.
554. Zu damidn *Heilmittel, Mittel* gehort auch arm.
LW. darman *Verpflegung, Pflege, Nahrungsmittel,
Proviant, Futter (ursp. Tnterhalt* von Wzi. dhar
*halten).
=== HUB p.61 ===
bliiheu', ii. s. w., ii. s. w.
e) Vorschlag von u in: uspus 'Laus' = zd. spis;
ustun - sutun 'Saule' ; ustor = sutor *Ross'; uspurz = supurz
'Milz'; usruh *Blei* = surh (aiis "^suruh), g. suroh^ afgh. bal.
surup, phi. sr(u)p, u. s. w.
f) Einschub von u in: durod Segenswunsch' (vgl.
padrud *Lebewohl') = ^druvatdt-^ arm. druatHc; durudan
ernten* (pr. diravam), Wrzl. dru ; diirust 'ganz, vollstandig*
^= ^drusfa- (oben p. 61) ; durust 'rauh, grob' = "^drusta-
(oben p. 61); durdy [daroy) Xiige' -= ap. drauga-; xuros
'Hahn*, xuros 'Larm', skr. kroc ; furod {firod) *hinunter', paz.
fro$, skr. pravdtd; ftiroxtan Verkaufen* aus fra-^-vaxs;
surod 'Gesang, Lied' = zd. sraota-; surudan (pr. sardyam)
singen', zd. srdvayeiti ; siiru {saru) 'Horn* = zd. srvd- ; surun
[surtfi] 'Hinterbacken*, bal. saren, zd.sraoni-; supurdan (pr.
siparam) 'iibergeben', Wrzl. spar; supdr 'Pflug', afgh. spdra
```


## [2026-09-05T18:19:33.155Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5040,5090p' CHEUNG.txt",
 "description": "Cheung *darš entry"
}
```


### [2026-09-05T18:19:33.199Z] TOOL RESULT

```
*KHOTANESE: dirsujsina- ‘wishing to see’ 

*NWIR: (+ *ham-) Tt. (Chal andas/andar-, (Tak.) andast/andar-, (Esh.) undard/ 
undard ‘to see’ 

*NEIR: M. lisk’-, Yi. lišč- ‘saw’ (pret. supplet. of win-) 


62 *darsl 


*MISC: Par. dhör, dhur ‘saw’ 
*SANSKRIT: dars ‘to look’ (RV+) = EWAia I: 706 
«PIE *derk- ‘to look at? = LIV: 122 | Pok.: 213 


*IE COGNATES: Gr. d€pKopc ‘I see, look’ 
*REFERENCES: IFL I: 249a; IIFL П: 262a; Yarshater 1969: 187 f. (passim); DKS: 159b; Werba 1997: 
197; ESIJa II: 352 f. 


* dar’! ‘to dare’ 

*AVESTAN: (+ *upa-) Y Av. upadaras- ‘to dare’ — Liste: 28 

Pres. nu-: IND. 3pl. YAv. upadarosnuuainti (Yt 8.44) 

*OLD PERSIAN: dars- ‘to dare’ — Kent: 190b 

Pres. nu-: impf. IND. 3sg. adarsnaus <a-d-r-8-n-u-8> (DB 1.53) 

*KHOTANESE: darv- ‘to dare’ = SGS: 44 

*NWIR: Bal. durrit/durr- ‘to take courage’ 

*SANSKRIT: dhars ‘to venture, be bold, audacious’ (RV+) = EWAia I: 780 

«PIE *d'ers- ‘to attack, venture, dare, be bold, audacious’ > LIV: 147 | Pok.: 259 

*IE COGNATES: Gr. Өросъс ‘bold’, Gr. Өбрсос (n.) ‘boldness, courage’, Lith. dristi 


‘to venture’, Goth. ga-daursan ‘to venture’, OE dear(r), Engl. to dare, etc. 
*REFERENCES: DKS: 153a f.; Werba 1997: 353; ESIJa II: 355 f.; Shahbakhsh: s.v. durr- 


*dar&? ? ‘to crush’ 

*NEIR: Wa. ÖBIX-/60Xt- ‘to grind’, dasn, dasnak ‘grindstone’, Sariq. dex-t ‘to crumble, 
be scattered’, Sariq. diXn, óüXn ‘stone mortar?
```


## [2026-09-05T18:19:53.690Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 224 225; do echo \"=== POK_01 leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt | grep -n \"npers\\|durus\\|np\\.\\|21[4-9]\" ; done; echo \"=== grep durust in POK ===\"; grep -n \"durust\\|durusi\\|durusl\" POK_01.txt | head",
 "description": "Pokorny p.216 deru- and durušt"
}
```


### [2026-09-05T18:19:55.218Z] TOOL RESULT

```
=== POK_01 leaf 224 ===
5:214  •
6:dera-,  doru-,  dr{e)u-,  drou-]  dreug  :  drü-  ,Baum',  wahrscheinlicli  urspr, und  eigentlich  , Eiche',  siehe  zur  genauem  BegTiffshestimmang  Osthoj Par.  I  169 f.,  Hoops  Waldb.  117 f.;  dazu  Worte  für  verschiedene  Hol gerate  sowie  für  , kernholzartig  hart,  fest,  treu';  Specht  (KZ.  65,  198j 66,    58  f.)    geht    jedoch    von    einem    substantivierten    Neutrum    einj Adjektivs    *döru    ,das  Harte'    aus,    woraus    erst    ,Baum'   und  ,Eicbe»^ dbru    n..    Gen.    dreu-s,    dru-nö-s]    Ableitungen:     deruo-,    dreu^ drU'Znö'S,  dru-nö-s,  druu-ö-s,  drü-tö-s. Ai.    däru   n.    ,Holz^    (Gen.    dröhj    drünah,    Instr.    drünä,    Lok.    därui^xi dravya-  ,vom  Baum'),   di-d-   n.  m.  ,Holz,   Holzgorät',   m.-^Baum,  Ast^  a? däuru  ^Baumstamm,  Holzstück,  Waffe  aus  Holz,  etwa  Keule'  (Gen.  draol ai.  därund-  ,hart,   rauh,  streng'  (eigentlich  ,hart  wie  Holz,   klotzig'),  drS in  Kompositis  wie  dru-päda-  ,klotzfüßig',  dvu-ghni  ,Holzaxt-  (-schlägerinf su-dini-h  ,gutes  Holz';  dhruvd-  ,fest,  bleibend'  (dh-  durch  volksetym.  Anschla|^ an   dhar-   ,halten,    stützen'  =  av.    dr{u)vö,    apers.    duruva    ,gesund,  heil* vgl.  aksl.  s^•d7^av^)]  av.  drvaena-  ,hölzern',  ai.  druvdya-h  ,hölzernes  Gefä(§ Holzkasten    der   Trommel',    drAna-m    ,Bogen,    Schwert'   (unbelegt;    mit npers.   durüna,   baluci   drin  ,Regenbogen'),   drunl  ,Wassereimer'^   drö-  a^ ,hölzerner  Trog,  Kufe';  drumd-h  ,Baum'  (vgl.  unten  dQV^Log)] ai.  ddrvv-hy  darvi  ,(bölzerner)  Löffel';
=== POK_01 leaf 225 ===
5:215
11:aus  dem  Lat.  vielleicht  durus  ,hart;  abgehärtet,  kräftig;  derb,  roh,  rauh, streng;  gefühllos'  (aber  über  düräre  ,ausdauern,  dauern'  s.  unten  S.  220), wenn  nach  Osthoff  Ulf.  als  ,baum3tark,  fest  wie  (Eichen) holz'  dissimiliert aus  *drü-ro-s  (*dreu-ro-s?)',
=== grep durust in POK ===
3096:triggws  (*tremiaz)  ,treu^,  ahd.  gi-trluwi  ,U'eu%  an.  tryggr  ,tve\i,  zuve, lässig,  sorglos',  got.  triggioa  ,Bund,  Bündnis',  ags.  treow  , Glaube,  Treu, Wahrheit',  ahd.  triuwa,  nhd.  Treue,  vgl.  mit  ders.  Bed.,  aber  ande] Ablautstufen  anord.  trü  f.  , religiöser  Glaube,  Versicherung',  ags.  irui m.,  mnd.  trüioe  f.  ds.,  ahd.  trüwa,  aisl.  trü  f.,  neben  trür  ,treu';  abgeleit| anord.  trüa  ,trauen,  für  wahr  halten'  =  got.  trauan,  und  ags.  trüiüia: as.  trüön,  ahd.  trü{w)en  ,trauen'  (vgl.  n.  apr.  druiuis)]  ähnlich  atiorj traustr  ^stark,  fest',  traust  n.  , Zuversicht,  Vertrauen,  worauf  man  sie! verlassen  kann',  ahd.  tröst  , Vertrauen,  Trost'  {*droust-)j  got.  trausti  ,Vec! trag,  Bündnis',  ablautend  engl,  triist  , Vertrauen'  (mengl.  trüst),  mla trustis  ,Treue'  in  den  afränk.  Gesetzen,  mhd.  getrilste  ,Schar'  (die  s^Bildu ist  alt  wegen  npers.  duruU  ,hart,  stark',  durust  ,gesund,  ganz';  nor\^ trysja  ,den  Boden  säubern',  ags.  ti^üs  , Reisig',  engl,  trouse,  aisl.  tn , Abfälle',  got.  ufar-trusnjan  , überstreuen'.
```


## [2026-09-05T18:20:03.273Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 3096\nidx=sum(len(l)+1 for l in lines[:3095])\nleaf=t[:idx].count('\\f')\nprint('leaf',leaf)\npg=t.split('\\f')[leaf]\nimport re\nprint([m for m in re.findall(r'^\\s*(\\d{3})\\s*$',pg,re.M)])\nprint(pg[:200])\nEOF",
 "description": "Find Pokorny page for durušt mention"
}
```


### [2026-09-05T18:20:05.150Z] TOOL RESULT

```
leaf 226
['216']
ngen);
deim-  in  germ.  Tervingl,  Matrib{us)  AlaterviSj  anord.  tjara  {^detiiön-), finn.  Lw.  terva,  ags.  teoru  n.,  tierwe  f.,  -a  m.  ,Teer,  Harz'  (*deruio-),  mnd. tere  ,Teer'  (nhd.
```


## [2026-09-05T18:20:15.157Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for w in ['درشت','دانه','دایه','دانگ']:\n        if w in p:\n            print(i,w)\nEOF",
 "description": "Find ARY pages for target words"
}
```


### [2026-09-05T18:20:16.680Z] TOOL RESULT

```
17 دانه
48 دانگ
233 دانه
263 دانه
264 دایه
271 درشت
346 درشت
509 دانگ
```


## [2026-09-05T18:20:19.785Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; for L in 263 264 271; do echo \"=== ARY leaf $L (printed $((L+1))) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' ARY_pages.txt | head -60; echo; done",
 "description": "Aryanpur pages for دانه دایه درشت"
}
```


### [2026-09-05T18:20:21.216Z] TOOL RESULT

```
=== ARY leaf 263 (printed 264) ===
[pdf page 264]
دانه / ۲۶۵
بادداشت:
۱- واژه‌ی "دانا" نیز از همین واجريشه است.
۲ بازگدت به: شناختن.
اوستایی (/4۲87۸): ۸ ,0۸۷0 لنونی (لتی) (771420ا): 0۸
پهلری (۷1الل۳۸):
6 020 ,020۸ پسگشت‌ها 5
کردی (9(0اطن0): ۰ 02080 ,0208 زر
بلوچی (/61/ال8۸): 6 وال0۸ 2 (8880) :4۸5/215
افغانی (پشتو) (017۸1/م: ۳ 515 ناط
سانسکریت (5۸۸/56277): 57 0107 :۸0۸5 بل ۸4۸07
,013201۸3 ,03۸۸۸8 برهان قاطع : ۸۳۰
لیترانی ((71۸هلالل7/): 00۸
ِْ
پارسی باستان (۳2781 010): ابسلندی کهن (/804۸01044 010)(شاید)
2 2006
تخاری ۸ (۸ (4ل10827۸): 720 ساکسرنی کهن ((542:0 012)(شاید) ‏ 0017
تخار ی 8 (8 15838:۳۵4۷ ,الق78 فریزی کهن (/۲57314۸ 010)(شاید) ‏ 3020
ی سانسکریت (54۸5577): 23 آلمانی کهن ((0870/۸ ۶707 010)(شاید)
1 ۳ ۰ 0۸038 ,033302۸8 ,211۸۷۸۷ 5 نآ70
برنانی 08220 (شأیم 71 آلمانی (02224400)(شاید) 7۸0
لاتین (/710ل): 8 8008 انگلیسی کهن (5۸/073[4 010)(شاید)
فرانسه (۳8۸۸۲۷): ۰ ۲0۱۲۳۸۹۸۲۳ ,808773 7۷ ,ت05
اسپانیایی (52۸((15[7): وید اد انگلیسی (5[7ا5۸/0)(شاید) درد
ابتالبابی (744/۷): ۴0۲۲۳۸۸۸ ,۲0۲۲75 دانمارکی (2۸4۸۷/54)(شاید) انا
رومانی (/(8۷-۸4۸2/4): انا ۱ سوئدی (57782154)(شاید) 26
پرتغالی (۳0717012858): 07 ملندی (/[0076): 24۸17


=== ARY leaf 264 (printed 265) ===
[pdf page 265]
۶ | دایه
پسگشت‌ها 55 (ق۸2۲2۲ +57
۲ 0 20 16 080 ,فد هن ۱
مک این 01 8( هنم
3 (08) ,404 (۲00۲۸1) آفت‌نامه دهغدا: ۱۴۴۱۳ رین
3 (089) :01005
یادداشت: :
چم این واژه در زبان لاتین و زبان‌های ناشی از آن (زبان‌های رومانس): فواره» چشمه,
چم این واژه در زبان‌های ژرمنی: ژاله» شینم.
هند و اروپایی (1۸/00-821078۸): + ,ترآ 013* ۴0۲180130۰ ,۴015۸۵ ,038+
اوستایی (4/88374/۷): -0۸3۸۷10 ,-0۸1380 20
پهلری (4۲7الا۳۸): 6 بل۸ 029 لیترانی (72۸(4/): 00
اوستی (0558716): ,09 لتونی (لتی) (7۷1407ل): 0837
کردی (6080158): 0256 ,225 ,1020 پروسی کهن (الفاک5ن۲7 ص۵): 02۸2۸
بلوچی (الللالهه): 02 ولزی (لاقا78): 20
افغانی (پشتو) (/۸7011۸۸). 3 بر ترنی (870670۸): 20
سانسکریت (7ل54۸/58): 0112781 013۸۰ آلبانی (المامقلم: نا ۱۱
آرمنی (/۸۷۵42(1۸): 0۸۸
پرنانی (07250): پسگشت‌ها 5
بقاگه ,035 زر ان 00 زر ۳
لاتین (7100): 8 ,۴810 ات امد هن
گوتبکه (007/6): 2067۸ 5 (۷888 87 ,5ا01(8)
نروژی (0717801421/): ار 3 (07180) 5
اسلاوی کهن (412ا5 6[7ن71ا» 01.0): برهان قاطم + ۸۳۲
بادداشت:
چم واجریشه‌ی هند و اروپایی این واژه: مکیدن» شیردادن,
چم این واژه در اوستایی: ماده» مادینه,
چم این واژه در زبان‌های لیترانی و پروس کهن و ولزی و برتونی و سانسکریت و لاتین و گوتیک و نروژی و
"۵


=== ARY leaf 271 (printed 272) ===
[pdf page 272]
نج ا
درشت / ۲۷۳
یادداشت:
۲- چم این واژه در زبان لیتوانی: قری
۳ چم این واژه در زبان‌های ژرمنی؛ باوفا؛ راستین؛ راست
پارسی باستان (1۵۸۵۷ق۳87 صا0):
۳۸ پسگشت‌ها درد دی
پهلری (4۲ائتاه): 0808777 ,0173105177 6 20090
ابسلندی کهن (070۸427(م5 صان): :۸2/5
708 1 117,010 (1۸81) ۱
انگلیسی کهن (8۸0157 ۰:00 7818 برهان قاطع : ۸۳۷
نروژی (077780۸/): 75۸
یادداشت,
پازگشت به: دار» درست
اوستایی (۰::):048574(0 ۰ ۸0۸360730 اسپانیایی (50۸/1577): 10
پهلری (47الل۸): ایتالیایی (4(۷ال77۸): 110
6 258۸016 ,018۸06 رومانی (/(۸44/]4ا): تزا ها
کردی (61805/7): دنداد درل پرتغالی (۳07101858): 1000
لاتین (7100): 6۸ ,10۳6۲85 گرتیکد (0077776): نی ۱۸
فرانسه (ت۳5(/6): 106
```


## [2026-09-05T18:20:46.602Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,40p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-05T18:20:46.648Z] TOOL RESULT

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


## [2026-09-05T18:20:51.319Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/درشت\" \"https://en.wiktionary.org/wiki/دایی\" \"https://en.wiktionary.org/wiki/دانه\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰers-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeh₁(y)-\"; do python3 tools/fetch_source.py \"$u\" --note \"page 123, roots Dhars/Dhe, verifying dorošt, dâyi, dâneh and the PIE roots\" ; done 2>&1 | tail -20",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-05T18:20:55.740Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ff54e6cc631f143d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e60ae291dfc9bc17.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bdb70704fef19e2e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06424ae6d9ed535b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3229797f135505e1.txt
```


## [2026-09-05T18:20:58.612Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"###### دُرشت\"; grep -n -A25 -i \"^Persian\" ff54e6cc631f143d.txt | head -60",
 "description": "Read Wiktionary درشت"
}
```


### [2026-09-05T18:20:58.671Z] TOOL RESULT

```
###### دُرشت
```


## [2026-09-05T18:21:01.724Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; wc -c ff54e6cc631f143d.txt e60ae291dfc9bc17.txt bdb70704fef19e2e.txt 06424ae6d9ed535b.txt 3229797f135505e1.txt; echo ---; head -40 ff54e6cc631f143d.txt",
 "description": "Check archived file contents"
}
```


### [2026-09-05T18:21:01.781Z] TOOL RESULT

```
 2437 ff54e6cc631f143d.txt
11064 e60ae291dfc9bc17.txt
 7672 bdb70704fef19e2e.txt
 5052 06424ae6d9ed535b.txt
10622 3229797f135505e1.txt
36847 total
---
URL: https://en.wiktionary.org/wiki/درشت
FETCHED: 2026-09-05T18:20:53Z
STATUS: 200
TITLE: درشت - Wiktionary, the free dictionary

درشت - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

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
```


## [2026-09-05T18:21:05.524Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== درشت tail ===\"; tail -20 ff54e6cc631f143d.txt; echo; echo \"=== دایی ===\"; sed -n '/Persian/,$p' e60ae291dfc9bc17.txt | head -60",
 "description": "Read درشت and دایی entries"
}
```


### [2026-09-05T18:21:07.054Z] TOOL RESULT

```
=== درشت tail ===

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 درشت 

 5 languages 

 Add topic
=== دایی ===
 Persian 

 Toggle Persian subsection 

 2.1 
 Alternative forms 

 2.2 
 Etymology 

 2.3 
 Pronunciation 

 2.4 
 Noun 

 2.4.1 
 Descendants 

 2.5 
 See also 

 2.6 
 References 

 2.7 
 Further reading 

 Toggle the table of contents 

 دایی 

 6 languages 

 فارسی 
 Français 
 Kurdî 
 Malagasy 
 Türkçe 
 中文 

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
```


## [2026-09-05T18:21:11.536Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i \"turk\\|etymolog\\|borrow\\|inherit\" e60ae291dfc9bc17.txt | head -20; echo \"=== tail ===\"; tail -30 e60ae291dfc9bc17.txt",
 "description": "Search دایی archive"
}
```


### [2026-09-05T18:21:11.598Z] TOOL RESULT

```
57: Ottoman Turkish 
59: Toggle Ottoman Turkish subsection 
65: Etymology 
91: Etymology 
176: Ottoman Turkish
184: Etymology
187: Inherited from Proto-Turkic *tāy , *dāj ( “ maternal uncle ” ) ; cognate with Old Turkic [script needed] ( tay, tagay ) , Azerbaijani dayı , Kyrgyz тай ( tay ) , Southern Altai таай ( taay ) , Turkmen daýy and Yakut таай ( taay ) . Akin to Persian دایی ( dâyi ) and تغایی ( taġāyī ) , both Turkic borrowings.
214: Turkish: dayı 
234: Çağbayır, Yaşar ( 2007 ), “ dayı3 ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 1119 
242: Meninski, Franciszek à Mesgnien ( 1680 ), “ دایی ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [5] , Vienna, column 2019 
246: Redhouse, James W. ( 1890 ), “ دایی ”, in A Turkish and English Lexicon ‎ [6] , Constantinople: A. H. Boyajian, page 887 
256: Etymology
259: A Turkic borrowing: compare Turkish dayı , Azerbaijani dayı . [ 1 ] [ 2 ] 
573: ^ Doerfer, Gerhard ( 1963 ), Türkische und mongolische Elemente im Neupersischen [ Turkic and Mongolian Elements in New Persian ] (Akademie der Wissenschaften und der Literatur: Veröffentlichungen der Orientalischen Kommission; 16 )‎ [1] (in German), volume I, Wiesbaden: Franz Steiner Verlag, § 1176 , page 196 
575: ^ Hassandoust, Mohammad ( 2004/2005 ), Bahman Sarkarati, editor, Farhang-e riše-šenâxti-ye zabân-e Farsi [ An Etymological Dictionary of the Persian Language ] (in Persian), volume II: P-D, Tehran: Academy of Persian Language and Literature, →ISBN , page 1264 
584: Categories : Ottoman Turkish terms inherited from Proto-Turkic 
585: Ottoman Turkish terms derived from Proto-Turkic 
586: Ottoman Turkish lemmas 
587: Ottoman Turkish nouns 
588: Ottoman Turkish terms with historical senses 
=== tail ===

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 دایی 

 6 languages 

 Add topic
```


## [2026-09-05T18:21:20.125Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== دانه ===\"; grep -n -i \"etymolog\\|inherit\\|Proto-Iranian\\|Middle Persian\\|Sanskrit\\|grain\" bdb70704fef19e2e.txt | head -20; echo; echo \"=== PIE dhers ===\"; grep -n -i \"descend\\|dare\\|Latin\\|Sanskrit\\|Avestan\\|root\\|Proto-Ger\" 06424ae6d9ed535b.txt | head -25",
 "description": "Read دانه and dʰers- archives"
}
```


### [2026-09-05T18:21:20.193Z] TOOL RESULT

```
=== دانه ===
62: Etymology 
79: Etymology 
93: Etymology 
187: Etymology
202: pip , seed , kernel , grain , berry of any fruit or grain 
204: seed , grain in bulk 
210: bait in a trap if remotely grain-formed
234: Etymology
251: grain 
256: Etymology
259: Inherited from Middle Persian 𐭣𐭠𐭭𐭪 ( dʾnk' /⁠dānag⁠/ ) , from Proto-Iranian *daHnáH , from Proto-Indo-Iranian *dʰaHnáH , from Proto-Indo-European *dʰoHnéh₂ . Cognate with Baluchi دانگ ( dànag , “ pimple ” ) . Doublet of دانگ .
312: grain ( seed of grass food crops ) 
314: grain ( grass food crops ) 
369: Vullers, Johann August ( 1855 ), “ دانه ”, in Lexicon Persico-Latinum etymologicum cum linguis maxime cognatis Sanscrita et Zendica et Pehlevica comparatum, e lexicis persice scriptis Borhâni Qâtiu, Haft Qulzum et Bahâri agam et persico-turcico Farhangi-Shuûrî confectum, adhibitis etiam Castelli, Meninski, Richardson et aliorum operibus et auctoritate scriptorum Persicorum adauctum ‎ [1] (in Latin), volume I, Gießen: J. Ricker, page 804a 
386: Persian terms inherited from Proto-Indo-European 
387: Persian terms inherited from Middle Persian 
388: Persian terms derived from Middle Persian 
389: Persian terms inherited from Proto-Iranian 
390: Persian terms derived from Proto-Iranian 
391: Persian terms inherited from Proto-Indo-Iranian 

=== PIE dhers ===
65: Root 
71: Descendants 
135: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
145: Root
150: to be bold , to dare 
155: Terms derived from the Proto-Indo-European root *dʰers- (15 c, 0 e) 
159: Proto-Slavic: *dьrznǫti ( see there for further descendants )
163: Sanskrit: धृष्णोति ( dhṛṣṇóti ) 
166: Younger Avestan: 𐬎𐬞𐬀𐬛𐬀𐬭𐬲𐬥𐬎𐬎𐬀𐬌𐬧𐬙𐬌 ( upadaržnuua i ṇti ) 
185: Sanskrit: धृष्ट ( dhṛṣṭá ) 
193: Descendants
198: Sanskrit: धृष् ( dhṛṣ , “ to dare, be bold ” ) 
203: ^ Kroonen, Guus ( 2013 ), Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN 
216: Categories : Proto-Indo-European terms belonging to the root *dʰer- 
218: Proto-Indo-European roots 
219: Proto-Indo-European CeRC-shaped roots 
225: Sanskrit terms with non-redundant manual transliterations
```


## [2026-09-05T18:21:30.659Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i \"femina\\|filius\\|fetus\\|fētus\\|daēnu\\|dhaynu\\|Avestan\\|suck\\|Root\\|Latin\" 3229797f135505e1.txt | head -30",
 "description": "Read dʰeh₁(y)- archive"
}
```


### [2026-09-05T18:21:30.719Z] TOOL RESULT

```
62: Root 
129: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
134: Root
139: to suckle , nurse 
144: Terms derived from the Proto-Indo-European root *dʰeh₁(y)- (76 c, 0 e) 
154: Proto-Germanic: *dijōną ( “ to suck, suckle ” ) 
161: Ossetian: ( “ to suck ” ) 
173: Latvian: dēt ( “ to suck ” ) 
182: Latin: fēmina ( “ woman ” ) ( see there for further descendants )
186: Latin: fētus ( “ pregnant ” ) 
189: Proto-Italic: *fētus 
190: Latin: fētus ( “ offspring ” ) ( see there for further descendants )
194: Latin: fēnum ( “ hay ” ) 
198: Latin: fēnus ( “ interest (on money) ” ) 
213: Sanskrit: धारु ( dhārú , “ sucking ” ) 
221: ⇒ Latin: fēlīx ( “ happy ” ) 
228: Latvian: dīle ( “ sucking calf ” ) 
238: Latin: fēlō , fellō ( “ to suck ” ) 
283: Proto-Germanic: *dajjaną ( “ to suck, suckle ” ) ( see there for further descendants )
304: ^ De Vaan, Michiel ( 2008 ), “ fēmina ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 210 
306: ^ De Vaan, Michiel ( 2008 ), “ fētus ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 217 
308: ^ De Vaan, Michiel ( 2008 ), “ fēnum / faenum [ n o ] ‘hay’ ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 211 
314: ^ De Vaan, Michiel ( 2008 ), “ fēlix, -icis ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 209 
331: Oshiro, Terumasa ( 1988 ), “ Some Luwian words of Indo-European origin ”, in Orient , volume 24 , page 49 : “ (5) suckling (241) ” 
336: Proto-Indo-European roots 
337: Proto-Indo-European CeHR-shaped roots
```


## [2026-09-05T18:21:39.464Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://www.etymonline.com/word/infest\" \"https://www.etymonline.com/word/manifest\" \"https://www.etymonline.com/word/dare\" \"https://www.etymonline.com/word/female\" \"https://en.wiktionary.org/wiki/filius\"; do python3 tools/fetch_source.py \"$u\" --note \"page 123, roots Dhars/Dhe: English/Latin branches (infest, manifest, dare, female, filius)\"; done 2>&1 | tail",
 "description": "Archive Etymonline and filius pages"
}
```


### [2026-09-05T18:21:42.576Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/92bea0597bcb14f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/355bbb9a9a3b2a74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7282a77e47f25e09.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ad5704c1b0e67a2c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aa75ceb706963080.txt
```


## [2026-09-05T18:21:47.243Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 92bea0597bcb14f1 355bbb9a9a3b2a74 7282a77e47f25e09 ad5704c1b0e67a2c; do echo \"###### $f\"; grep -n -i \"PIE root\\|from Latin\\|Old English\\|Proto-Germanic\\|dhers\" $f.txt | head -8; done; echo \"###### filius\"; grep -n -i \"etymology\\|Proto-Italic\\|dʰeh₁\\|bʰuH\\|De Vaan\" aa75ceb706963080.txt | head -12",
 "description": "Read etymonline and filius archives"
}
```


### [2026-09-05T18:21:49.406Z] TOOL RESULT

```
###### 92bea0597bcb14f1
25: late 15c., infesten , "to attack, assail, hurt, distress, annoy," from Old French infester (14c.), from Latin infestare "to attack, disturb, trouble," from infestus "unsafe, hostile, threatening, dangerous," originally "inexorable, not able to be handled," from in- "not, opposite of" (see in- (1)) + -festus , perhaps "(able to be) seized" (see manifest (adj.)). The sense of "swarm over in large numbers, attack parasitically" is recorded by c. 1600. Related: Infested ; infesting .
32: late 14c., "clearly revealed to the eye or the understanding, open to view or comprehension," from Old French manifest "evident, palpable," (12c.), or directly from Latin manifestus "plainly apprehensible, clear, apparent, evident;" of offenses, "proved by direct evidence;" of offenders, "caught in the act," probably from manus "hand" (from PIE root *man- (2) "hand") + -festus , which apparently is identical to the second element of infest .
48: word-forming element meaning "not, opposite of, without" (also im- , il- , ir- by assimilation of -n- with following consonant, a tendency which began in later Latin), from Latin in- "not," cognate with Greek an- , Old English un- , all from PIE root *ne- "not."
58: also over-run, Middle English overrennen, from Old English oferyrnan "to run across, pass over;" see over- + run (v.). Meaning "continue beyond a specified time" is from early 14c. Meaning "to ravage (a land), maraud, plunder" is by mid-14c. Of weeds, etc., "to grow over, cover a
62: mid-14c., occupien, "to take possession of and retain or keep," also "to take up space or room or time; employ (someone)," irregularly borrowed from Old French ocuper, occuper "occupy (a person or place), hold, seize" (13c.) or directly from Latin occupare "take over, seize, take
66: c. 1300, "one at dice," from Old French as "one at dice" (12c.), from Latin as "a unit, one, a whole, unity;" also the name of a small Roman coin (originally a rectangular bronze plaque weighing one pound, it eventually was reduced by depreciation to half an ounce; in imperial ti
70: Old English ærende "message, mission; answer, news, tidings," from Proto-Germanic *airundija- "message, errand" (source also of Old Saxon arundi, Old Norse erendi, Danish ærinde, Swedish ärende, Old Frisian erende, Old High German arunti "message"), which is of uncertain origin. 
74: 1690s, "sculpture of upper torso and head," from French buste (16c.), from Italian busto "upper body," from Latin bustum "funeral monument, tomb," originally "funeral pyre, place where corpses are burned," perhaps shortened from ambustum, neuter of ambustus "burned around," past 
###### 355bbb9a9a3b2a74
25: late 14c., "clearly revealed to the eye or the understanding, open to view or comprehension," from Old French manifest "evident, palpable," (12c.), or directly from Latin manifestus "plainly apprehensible, clear, apparent, evident;" of offenses, "proved by direct evidence;" of offenders, "caught in the act," probably from manus "hand" (from PIE root *man- (2) "hand") + -festus , which apparently is identical to the second element of infest .
39: late 14c., "to spread" (one's fame), "to show plainly," from manifest (adj.) or else from Latin manifestare "to discover, disclose, betray." Meaning "to display by actions" is from 1560s; reflexive sense, of diseases, etc., "to reveal as in operation" is from 1808. Related: Manifested ; manifesting .
52: late 15c., infesten , "to attack, assail, hurt, distress, annoy," from Old French infester (14c.), from Latin infestare "to attack, disturb, trouble," from infestus "unsafe, hostile, threatening, dangerous," originally "inexorable, not able to be handled," from in- "not, opposite of" (see in- (1)) + -festus , perhaps "(able to be) seized" (see manifest (adj.)). The sense of "swarm over in large numbers, attack parasitically" is recorded by c. 1600. Related: Infested ; infesting .
56: "public declaration explaining reasons or motives for a course of actions done or planned," 1640s, from Italian manifesto "public declaration explaining past actions and announcing the motive for forthcoming ones," originally "proof," from Latin manifestus "plainly apprehensible, clear, apparent, evident" (see manifest (adj.)), also used as a noun, "obvious facts, palpable things."
73: 1590s, "bear witness to, officially confirm; give proof or evidence of," from French attester (Old French atester, 13c.) "affirm, bear witness to," from Latin attestari "confirm, prove," literally "bear witness to," from assimilated form of ad "to" (see ad-) + testari "bear witne
77: mid-14c., "to declare the truth of," also "to vouch for or confirm" (an official record, etc.), from Old French certefiier "make certain, witness the truth of" (12c.), from Late Latin certificare "to certify, to make certain," from Latin certus "fixed, sure" (see certain) + root 
97: c. 1300, "flat, smooth," from Old French plain "flat, smooth, even" (12c.), from Latin planus "flat, even, level" (from PIE root *pele- (2) "flat; to spread"). Sense of "explicit, clear, evident" is from late 14c.; that of "free from obstruction" is mid-14c.; meaning "simple, sin
101: early 14c., condempnen "to blame, censure;" mid-14c., "pronounce judgment against," from Old French condamner, condemner "to condemn" (11c.) and directly from Latin condemnare, condempnare "to sentence, doom, blame, disapprove," from assimilated form of com-, here perhaps an inte
###### 7282a77e47f25e09
25: Middle English durren, daren , from first and third person singular of Old English durran "be bold enough, have courage" (to do something), also transitive "to venture, presume," from Proto-Germanic *ders- (source also of Old Norse dearr , Old High German giturran , Gothic gadaursan ), according to Watkins from PIE root *dhers- "bold" (source also of Sanskrit dadharsha "to be bold;" Old Persian darš- "to dare;" Greek thrasys "bold," tharsos "confidence, courage, audacity;" Old Church Slavonic druzate "to be bold, dare;" Lithuanian drįsti "to dare," drąsus "courageous").
27: An Old English irregular preterite-present verb: darr, dearst, dear were first, second and third person singular present indicative; mostly regularized 16c., though past tense dorste survived as durst , but is now dying, persisting mainly in northern English dialect.
65: Old English agan (past tense ahte) "to have, to own," from Proto-Germanic *aiganan "to possess" (source also of Old Frisian aga "have to, ought to," Old Norse eiga, Old High German eigan, Gothic aigan "to possess, have"), from PIE root *aik- "be master of, possess." The original 
93: late 14c., "a thing done," from Latin actus "a doing; a driving, impulse, a setting in motion; a part in a play," and actum "a thing done" (originally a legal term), both from agere "to set in motion, drive, drive forward," hence "to do, perform," figuratively "incite to action; 
97: Old English catt (c. 700) "domestic cat," from West Germanic (c. 400-450), from Proto-Germanic *kattuz (source also of Old Frisian katte, Old Norse köttr, Dutch kat, Old High German kazza, German Katze), from Late Latin cattus. The near-universal European word now, it appeared in
###### ad5704c1b0e67a2c
25: early 14c., female , femele , "woman, human being of the sex which brings forth young," from Old French femelle "woman, female" (12c.), from Medieval Latin femella "a female," from Latin femella "young female, girl," diminutive of femina "woman, a female" ("woman, female," literally "she who suckles," from PIE root *dhe(i)- "to suck").
46: late 14c., "male human being; male fish or land animal; one of the sex that begets young," from Old French masle (adj.) "masculine, male, adult," also used as a noun (12c., Modern French mâle ), from Latin masculus "masculine, male, worthy of a man" (source also of Provençal mascle , Spanish macho , Italian maschio ), diminutive of mas (genitive maris ) "male person or animal, male."
57: mid-14c., "belonging to the male grammatical gender;" late 14c., "of men, of male sex," from Old French masculin "of the male sex" (12c.), from Latin masculinus "male, of masculine gender," from masculus "male, masculine; worthy of a man," diminutive of mas (genitive maris ) "male person, male," a word of unknown origin. The diminutive form might be by pairing association with femininus (see feminine ). Meaning "having the appropriate qualities of the male sex, physically or mentally: Manly, virile, powerful" is attested by 1620s. As a noun, "masculine gender," from c. 1500.
72: mid-14c., "of the female sex," from Old French femenin (12c.) "feminine, female; with feminine qualities, effeminate," from Latin femininus "feminine" (in the grammatical sense at first), from femina "woman, female," literally "she who suckles" (from PIE root *dhe(i)- "to suck").
76: 1620s, "womanish" (of a man); 1650s, "having two sexes, being both male and female," from Latin androgynus, from Greek androgynos "hermaphrodite, male and female in one; womanish man;" as an adjective (of baths) "common to men and women," from andros, genitive of anēr "male" (fro
80: Old English distæf "long, cleft stick that holds flax for spinning," from dis- "bunch of flax" (cognates: Middle Low German dise, Low German diesse "a bunch of flax on a distaff;" compare bedizen) + stæf "stick, staff" (see staff (n.)). Figurative of "women's work" from late 14c.
88: "the female person referred to," third person nominative fem. pronoun, used as a substitute for the name of a female or anything...regarded as female, mid-12c., probably evolving from Old English seo, sio (accusative sie), fem. of the demonstrative pronoun...As a noun meaning "a female human being, a woman," she is attested from early 14c....Also used to signify "female" with the names of other creatures (late 14c.; she-wolf, etc.)....
96: 1650s, "demigoddess," from Latin heroine, heroina (plural heroinae) "a female hero, a demigoddess" (such as Medea), from...The sense of "principal female character in a drama, poem, etc." is from 1715....
###### filius
65: Etymology 
455: Etymology
458: Etymology tree
460: Proto-Indo-European *dʰeh₁(y)- 
465: Proto-Italic *θīlios 
466: Proto-Italic *fīlios 
469: Inherited from Proto-Italic *fīlios, *feilios (the Latin can reflect either one, but Faliscan 𐌅𐌉𐌋𐌄𐌏 ( fīleo, hīleo ) , if original and not modeled on Latin fīlius , would point to *fīl- ), from earlier *θeilios , from *dʰeh₁i-l-yo-s ( “ sucker ” ) , a derivation from the verbal root *dʰeh₁(y)- ( “ to suck ” ) .
662: Latin terms derived from the Proto-Indo-European root *dʰeh₁(y)- 
664: Latin terms derived from Proto-Italic 
665: Latin terms inherited from Proto-Italic 
680: Pages with etymology trees 
681: Latin entries with etymology trees
```


## [2026-09-05T18:21:57.789Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg123.png"
}
```


### [2026-09-05T18:21:58.293Z] TOOL RESULT

```

```


## [2026-09-05T18:21:58.290Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T18:22:24.865Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== Horn dāne ===\"; grep -n \"däne\\|dane 'Korn\\|Korn'\" HRN.txt | head -10; echo; echo \"=== Kent dana ===\"; grep -n \"^dāna\\|dana-\\|'grain'\\|grain\" KNT.txt | head -10",
 "description": "Horn/Kent grain words"
}
```


### [2026-09-05T18:22:24.937Z] TOOL RESULT

```
=== Horn dāne ===
4801:535. däne 'Korn , arab. dänaj (auch säli]dänaj, sah\danag,
4806:n. dän, danay 'Korn' (74); af/. LW. däne; sar. pinj]-
4808:536. dang, däneg 'eine Münze bezw. ein Maass*.
4813:Ursprünglich mit däne (No. 535) identisch.
5162:574. dendün 'Zahn*^), dendäne 'Mauerzinne'.
10082:ger bemihr-i tu myerdäned ztmüne ^) rayträi
10237:ci meS-l berri bedendänes dt be/te ve säk
19178:däneki 535.

=== Kent dana ===
1173:pIE *jono-, OP zana- ‘man’ with Med. г, Ау. zana-, Skt. jána-; m OP vispa-cana-, paru- canü-, and (restored month-name) Varka- 2010-; OP d is seen in *wsa-dana- *wispazana-', inferred from the Elamite mi-iš-ša-da-na.
1182:ardastina-, Ardumants, avahar|da], uradana-, dan-
1183:in adánd, vardana-; from plE gh in gaud-, Bar- diya; from pIE ĝ or gh in yaud-. For materials
4913:(1) Prefix with verbs ay-, zšnav-, gam-, grab-, jan-, bar-, mà-, yam-; in verbal nouns dyadana-, dvahana-, and in the second parts of compounds Adiyabaukna-, Ariyáramna-, Bagabigna-, also in Akaufaciya-.
5039:dyadana- sb. ‘sanctuary’: deriv. ($1471) of prefix à + vb. yad- ‘worship’. dyadand apn. DB 1.63f.
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5197:uradana- adj. ‘of good regulation’: u- ‘good’
5516:dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
5829:yad- vb. ‘reverence, worship’, usually middle: Av. yazaite, Skt. ydjati, Gk. aterat, pIE *raój- (888, §113). See also Agiyadiya-, dyadana-, Bagayadi-, zyadā. yadataiy mid. ($213, §235.1) XPh 53. ayadaty lst sg. imf. mid. ($288.Ш) DB 5.16, 32; DSf 18°; DSk 5; XPh 40f. ayadiya imf. pass. ($220) DB 5.16°, 32.  ayadiya^ 3d pl. imf. pass. (8220, $282.11) XPh 36, 40. yadàátaiy subj. mid. (6999 11, 8235.1) DB 5.19, 34f. yadaišä 2d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39.
5855:?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
```


## [2026-09-05T18:22:39.438Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"koro'\\|korn'\\|(Getreide)\" BRT.txt | head -20; echo \"=== Horn 535/536 ===\"; sed -n '4795,4820p' HRN.txt",
 "description": "Bartholomae grain entries; Horn 535-536"
}
```


### [2026-09-05T18:22:39.510Z] TOOL RESULT

```
9339:s.  femer  KZ.  36.  15.  aussaen,  (Getreide)  durch  Aussaat  gewin-
13395:•  j.  ^dänav-  £  ' (Getreide) koro'.
13402:•  j.  (0n5.kars-Adj.'(Getreide)kömer(ver)- schleppend',  Bezeichnung  einer  Ameisen- art*': maoirJm  °spm  Y.iö.ia; — maoirinam ■!„nqm  V.J4.S.  'i«  73-
=== Horn 535/536 ===
kurd. zänin 'wissen* ; af/. pezanam {ijuti-) ; oss.
d. zönum^ zönun, t. zönin^ zönin (134); bei. zdnag,
n. zänay (422); sar. pad-züti-am, va-zün-am, v/a/. paz-
dan-am,
Friedrich MüUer's Aufstellung, WZKM. IV, 309
scheint mir im Wesentlichen verfehlt.
535. däne 'Korn , arab. dänaj (auch säli]dänaj, sah\danag,
pers. säh]dane)^ dänöe 'Linse*.
aw. düiiiö.^karsa' 'körnerschleppend'; phlv. dänak;
ai. dhänd' 'Getreidekörner*.
kurd. däni (LW.), daneki; bei. (LVV. ?) dän, däniu/,
n. dän, danay 'Korn' (74); af/. LW. däne; sar. pinj]-
dand 'Fünfkorn* d. i. 'Hirse*.
536. dang, däneg 'eine Münze bezw. ein Maass*.
ap. öavay.r} (Herakleides im Etyni. magn.); phlv. dang
(PPGl.), arm. LW. dang, arab. LW. danaq , mand.
LW. Np3xn 'Obolus*, syr. talmüd. LW. pr\ (de
Lagarde, Ges. Abh. 32).
Ursprünglich mit däne (No. 535) identisch.
537. däwer 'Richter*, däwen,
aw. *dätö,bara'; phlv. dätwar, däthar (bezw. dätebar),
dawar, arm. LW. datavor, vergl. a7ia\^aöovd<i 'Heeres-
richter* (Chron. pasch, p. 709, 1, 2).
») Vcr^l Bartholomae, BB. X, 278.— 119 —
538. däh 'Sklave*, Diener (auch weiblich)'.
ai. dasä' 'Sklave, Knecht*.
```


## [2026-09-05T18:23:59.889Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T18:23:59.946Z] TOOL RESULT

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


## [2026-09-05T18:24:06.385Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd1 dhers (p.864) ===\"; grep -n \"dhers\\|dhers-\" incoming/WLD/WLD_Bd1_pages.txt | head -10; echo; echo \"=== WLD Bd1 dhē(i) saugen (p.829) ===\"; grep -n \"saugen, säugen\\|dhē(i)\\|dhei-\" incoming/WLD/WLD_Bd1_pages.txt | head -10",
 "description": "Walde-Pokorny Bd1"
}
```


### [2026-09-05T18:24:06.454Z] TOOL RESULT

```
=== WLD Bd1 dhers (p.864) ===
50260: s.                Worte unter *dhers- „wagen“ und Yf. LEWb. 2 385), lett.
80449:hierher gehoriges aksl. d/srz „kiihn“ s. dhers- „wagen“.
80794:dhers- „wagen, kiihn sein" (auch mit                       -a- Stammbildung,        s.    Persson
80838:*dhers-to- gegeniiber ai. dhrsta- voraussetzen wiirden, ist unsicher (s. Yf.
80842:nebenherlaufende Bed. „Hand anlegen, zugreifen" fur idg. dhers- zur Er-

=== WLD Bd1 dhē(i) saugen (p.829) ===
66505:ziz&tj s. aber u. dhei- „saugen“; ahnlich freilich arm. tit „weibliche Brust“,
77367:ax-ia> zu doiv      „Schmaus“ usw. (s. unter *dhei- „saugen‘‘), fur welche
77838:dhei- „saugen, saugen"                  (:   dim-, dM- und dhe-, dha-,         s.   bes. Schulze      KZ.
77856:830                                    dhei-
77938:von dhei- „saugen“ fiir „fruchtbar sein“ erklart (Froehde BB. 21, 193, Johans-
77939:son Beitr. 69\ doch wird ein dhei- dieser Bedeutungsfarbung nicht gestiitzt
```


## [2026-09-05T18:24:07.233Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LEW infestus ===\"; grep -n -i \"infestus\\|manifestus\" LEW_1910.txt LAT.txt | head -10; echo \"=== LEW femina ===\"; grep -n -i \"^femina\\|femina \" LAT.txt | head -5",
 "description": "Latin etymological dictionaries"
}
```


### [2026-09-05T18:24:07.323Z] TOOL RESULT

```
=== LEW infestus ===
LAT.txt:30073:Infestus
LAT.txt:30122:Infestus, -a, -um: 1° dirig 4 contre: infestis pilis procurrere,InficiO
LAT.txt:36251:manifestus: v. manufestus.
LAT.txt:36421:Masur. ap. Geli.11,18,11; manifestus mendacii, sceleris "pris en fla¬
LAT.txt:36429:classique de manifestus).
LAT.txt:39946:chat; cf. CSL V 6 ai ,6 nussio est cattus eo quod nuribus sit infestus,
=== LEW femina ===
9429:pqvoi (1 1 adjonction de 1'epithbte femina dans le capris feminis des
13121:cos usus quod intemouimus, appellatur mas columbus, femina columba.
20150:f 4 reaaent en bien ou en aal; P.F.,3,31, adfecta femina uel in bonam
21363:T.L.31,13,9 incertus infans... masculus an femina esset.Peut se joindre
21366:T.L.38,11,3, femina bds, musca fgmina, Pl.Tra.384, etc., par opposition
```


## [2026-09-05T18:24:10.853Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '80794,80850p' incoming/WLD/WLD_Bd1_pages.txt",
 "description": "Walde-Pokorny dhers entry"
}
```


### [2026-09-05T18:24:10.903Z] TOOL RESULT

```
dhers- „wagen, kiihn sein" (auch mit                       -a- Stammbildung,        s.    Persson
         Beitr. 830).
      Ai. dhrs-no-ti , dhdrs-ati „ist dreist, mutig, wagt", dhrsd- (Gramm.), dhrs-
nii-     „kiihn,     tapfer,   mutig, dreist, frech", dhrsta- „keck, frech", dhrsita-
,,   kiihn, mutig", dadhrsi- „beherzt, kiihn", mit Objekt dharsayati „wagt sich
an, vergreift sich, bewaltigt", dharsana- n. „Angriff,                 MiBhandlung", dhar-
saJ;a-    „angreifend, iiber etwas kerfallend"; av. darsam Adv. „heftig, sehr",
dcirsi darky a- „kiihn, stark" (vom Wind), darsita- „kiihn", apers. adarsnaus
„er wagte", dadarsi- Els'. Gr. lesb. fiegoos n. „Mut, Kiihnheit" (hom. Qso-
a’mjq ^Freckling"), mit aus dem Adj. verschleppter Tiefstufe jon. altatt.
dagoo;       (natt    -ddggos) ds.,   att.   dgdoog n. „Mut, Kiihnheit; Yerwegenheit,
Frechheit", dagoeco,  daggtco „bin mutig", dugaa/Jog. dagnal/og „kiihn“,
dagavg (rhod. Qagovfjiog, ther. Ohagv/iaqhog), dgaavg ,, kiihn, mutig; ver-
wegen, frech" (= ai. dlirkii-), lesb. Adv. dgoaecoq, dugavvo; „mutig, getrost,
vertrauend" (*t)agoo-ovvog). Got. gadars, Inf. gadaursan Ptc. gadaursts    ,


(= ai. dhrsta-)         „ieh   wage",   as. gidurran,     ags. dear,   durran,     ahd.    (
                                                                                               gi)tar

(gi)turran        „wagen“, ahd. giturst, ags. gedyrst f. „Kiihnheit, Yerwegenheit"
(= ai. drill-   ,
                  (Kiihnheit"). Lit. nasaliert lit. dresii „wage“ (* dhrens -), dr[stu,
dnsti   ( dhrvs -) „wagen",      dr ash '*dhrons -) „Dreistigkeit“, drqsiis = lett.
                                               (


driioss „mutig“; fern bleibt aksl. dnzz (kiihn, verwegen" (s. Berneker 257
                                                      ,


m. Lit., welcher irrig Tonendwerden des s unter den von Zupitza KZ. 37,
396 vermuteten Bedingungen annimmt doch miiBte wohl vorher s nach r
                                                     ;


zu ch geworden sein, dieses nach -hr- und vor der Tonsilbe                     —
                                                                         vgl. dgaovg,
dhrsu-      — ms    palatalisiert und erst dieses zu z erweicht sein; drazz trotz
der Bed. vielmekr zu av. darazra- „fest" usw., s. u. *dheregh- „fassen"
(S. 859) oder mit z durch Ivreuzung mit einem Worte dieser Sippe).
   Curtius 5 256, Fick I 4 75, 244, 464, III 4 203.           Zugehorigkeit von lat.
infestas „feindlich“, infest are „feindlich behandeln, angreifen" und mani-
festos „handgreiflich, auf der Tat ertappt; offenkundig", die ein hochstufiges
*dhers-to- gegeniiber ai. dhrsta- voraussetzen wiirden, ist unsicher (s. Yf.
LEWb. 2 385); im Yerein mit ai. dharsayati „bewaltigt, vergreift sich",
dharsana-, dharsaka- (die aber auch ind. Sonderentwicklung aus „kiihn,
dreist, verwegen sein" sein konnten), wiirden sie dann eine Gdbed. oder
nebenherlaufende Bed. „Hand anlegen, zugreifen" fur idg. dhers- zur Er-
wiigung stellen (Prellwitz 2 179); anders, aber kaum richtig iiber die lat.
 Worte Sommer Hdb. 2 242, s. u. *ghadh-.

 1.     dliel-,   dholo- ,.Wolbung“ und „HohIung“ (aus „Biegung“).
   Gr. ftoXog f. „Kuppel, Kuppeldach, rundes Gebiiude; rundgebautes Schwitz-
 bad", sizil. doXda Theokrit, lak. (Hes.) aaXld ( a-              =
                                                      d) „runder Sommerliut
 fiir Frauen", ttdX.af.iog m. „im Innern des Hauses gelegenes, von andern
```


## [2026-09-05T18:24:11.813Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '30073,30130p' LAT.txt | head -60; echo \"=== manufestus ===\"; sed -n '36415,36435p' LAT.txt",
 "description": "Ernout-Meillet infestus/manifestus"
}
```


### [2026-09-05T18:24:11.890Z] TOOL RESULT

```
Infestus
(Tert.); infanticida,-cldium (id.). Comme la periode dans laquelle
1'enfant est considere comme incapable de parier finit a 7 ans (cf.
Quint. 1,1,18), on con^oit que Infans ait pu designer 1'enfant dans
le sens ordinairement r^serve i puer. Columelle dit ab infante, Celse
ab infantibus dans le sens de a puero, a pueris. - Panroman, sauf
ronmain. M.L.4393,4393ab. - En arm^nien, c'est 1 '"animal" qui est
dosigne: anasun (litteralement "qui ne parle pas").
Les participes proprement dits n'entraient pas en composition
(v. Wackernagel, A Itind. Gramm., II 1, p.193 et suiv.); et ce n'est
qu 1 en vertu de d^veloppements secondaires que, meme avec n- negatif
ou le developpement s'est produit le plus, il a et<? fait quelques
composes de ce genre; en latin, les cas tels que infans-, insolens,
insfins sont demeures exceptionnels.
Infendere: eTUxetvai,, evxX-ruxaTLoai, (GI033. ). Peut-etre compose
de -fendo, comme offendo, ou tire secondairement de infensus.
Infenditor: CTuvSixoe, unius causae cun alio compar (Gloss.). De
infendo ?
Infensus: v. fendo.
Inferiae, -ferius: v. fero.
infertor: v.fero.
Inferus ( infer ap. Cat., Agr. 149,1, super inferque uicinus), -a, -um:
qui se tronve par dessous, par opposition a superus', de la substantive,
Inferi,-orum "les habitants du monde souterrain", Di Inferi, par
opposition a Dl Superi. Ancien (Enn.); usuel. N'est maintenu que dans
un seul dialecte du Tessin, M.L.4400; infera est demeure en corse,
M.L. 4394 a.
infra', en dessous (par oppos. k supra), plus bas. Adverbe et pre-
position (avec 1 'accusatif); sens physique et moral. Confondu avec
intra k bas se epoque, M.L.4410; Inferior,-oris (par oppos. a superior)'.
qui est plus bas; s'emploie de l'espace, et du temps (de la le sens
de "plus jeune, descendant"), du rang: Inferiores "les inf^rieurs";
Infimus (anc. infumus), -a,-um: qui se trouve tout au bas. Forme refaite
pour remplacer Imus qui avait perdu sa transparence etymologique.
Derives: infimat is (crAation de Plaute, St.493, qui 1 'oppose a sum¬
mates)', Infimitas (Amm.); Infimo (Apul.).A basse epoque, la forjne
ayant cesse d'etre comprise comme un superlatif, on rencontre le
comparatif infimior (iren.).
Inferus a un doublet infernus (cf. supernus, internus, etc.); d'ou
Inferna,-orum "les demeures des dieux Inferi "; Infernas,-atis (Vitr.).
La l.de 1 'figlise a employ 4 infernus m. dans le sens de "enfer" cf.
infernum, panroman, sauf roumain, M.L.4397, celt.: iri. iffern, britt.
uffern', germ.: ags. fern, et en a tire un adj. infernalis.
Lat. inferus, infimus repond evidemment a skr. ddharah (av. aSaro),
adhamdh "qui est au-dessous", a cote de adhdh "en bas"; le gotique
a undar "sons", et 1 'armenien dnd "sons" (entre autres sens). Mais
/ n 1 est pas conforne a la phonetique du latin de Rome; la forme du
mot est donc dialectale, ce qui s'expliquait par les emplois religieux
de ce groupe (inferi, etc. ). Pour le sens de Infra, cf .secus.
Infestus, -a, -um: 1° dirig 4 contre: infestis pilis procurrere,InficiO
S6 6 -
Ces.B.C.3,93, infestis signis ; "hostile k, acharne contre", gens
infestissima nomini Romano, Sali.C.5«; "expos£ au danger ou aux
attaques, perilleux, menaee, infeste": infestum iter, Cic., Phi. 1«, 10;
filii uita infesta, Cic.;Rose.Am.ii,30; omnia infesta serpentibus,
Sali.Iu.89; oppos^ a tutus, T.L.«,49, cf. Geli.9, as, 1. Souvent confondu
avec infSnsus, parfois meme avec infectus. Ancien (Pl. Cas.676); clas¬
sique. Rare k 1 1 ^poq. imper.; demeure en espagnol, M.L.440oa.
=== manufestus ===
nanicum, terme de la 1 . rustique, cf. CGL V 115,17.
Dirives: manubriatus', manubriolum, tous deux d'epoque imperiale.
V. manus . Formation obscure.
manufestus (mani-), -a, -um: explique par les Latins comme si-
gnifiant "pris a la main", par suite "pris sur le fait"; fur manufestus
(Lex XII Tab.); manifestum furtum est quod deprehenditur dum fit,
Masur. ap. Geli.11,18,11; manifestus mendacii, sceleris "pris en fla¬
grant delit de mensonge, de crime"; teneor manifesto miser, Pl. Tri.
yn; d'ou "que l'on peut saisir (sens moral); manifeste, evident".
- Ancien, usuel et classique. Adverbes: manifesto et manifeste (tar-
dif), manifestim (Cass. Fel., d' apres confestim).
Derivis: manifes 15 , -as (lat.imper.) et ses derives, conserve en60 y -
manus
v.esp. et portug., M.L.5304; manifestarius (synonyme ante- et post-
classique de manifestus).
Cf .in-festus? Si le premier element est bien le non de la "main",
la formation est etrange en face de manceps, ou de manumissus. L'abre-
gement de manu- en mani 1 -, du a 1'action de la loi des mots iambiques,
que suppose M.Leumann, Lat. Gr.$, p.342, est peu vraisemblable en cette
position.
manus, -ns f.(employe surtout au pluriel): main, partie du corps
```


## [2026-09-05T18:24:22.634Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN dare ===\"; grep -n \"gadaursan\\|OHG\\. (gi)tar\\|(gi)turran\" KLN_1966.txt | head -5; echo \"=== KLN infest ===\"; grep -n -o \"infest, tr\\. v[^|]\\{0,400\\}\" KLN_1966.txt | head -3; echo \"=== KLN manifest ===\"; grep -n -o \"manifest, adj[^|]\\{0,400\\}\" KLN_1966.txt | head -3; echo \"=== SKT DARE ===\"; grep -n -A3 \"^DARE\" SKT.txt | head -12",
 "description": "Klein and Skeat English entries"
}
```


### [2026-09-05T18:24:24.657Z] TOOL RESULT

```
=== KLN dare ===
=== KLN infest ===
=== KLN manifest ===
=== SKT DARE ===
4643:DARE.
4644-I
4645-fagffnt,  to  picTce— W.  (/dfr,  Irish  Jatfftar, a  dagger  ;  O.  Gael  tiaga^  a  dagger,  pistol ; Uret.  ./ti^,  iiaffer  (whence  F.  tfajpu).
4646-Daggle :  see  Dew.
--
4686:DARE.
4687-,  htr  Dart.
4688-E.    J>fX-.     A.  S.    Jiitrt, T>u,  dattitr^  Swctl.   F>nn. (£bUi%  duk.     Der.  dark- en the  dark.  (E"!    FonnctI idloag).  A.  S.  ^»c  iiti^,  b*ck-
4689-De&r.
```


## [2026-09-05T18:24:28.882Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \".\\{100\\}durran.\\{300\\}\" KLN_1966.txt | head -4; echo \"=== infestus in KLN ===\"; grep -n -o \".\\{80\\}infestus.\\{250\\}\" KLN_1966.txt | head -4; echo \"=== femina KLN ===\"; grep -n -o \".\\{60\\}she who suckles.\\{200\\}\" KLN_1966.txt | head -4",
 "description": "Klein greps"
}
```


### [2026-09-05T18:24:29.026Z] TOOL RESULT

```
=== infestus in KLN ===
19324:F.  infester,  fr.  L.  in¬ fest  are,  ‘to  trouble,  disturb,  molest’,  fr.  infestus, ‘disturbed,  molested,  infested,  unquiet,  hostile’, lit.  ‘seized’,  rel.  to  manifestus,  ‘evident’,  lit.  ‘that which  can  be  seized  by  the  hand’,  and  prob. cogn.  with  OI.  dharsati,  ‘dares’,  Gk.  ffdpoo?, ffpdcro?,  ‘courage,  a
=== femina KLN ===
```


## [2026-09-05T18:24:35.011Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"femella\" \"fetus,  n\" \"affiliate\" \"dear,  durran\" \"OE. durran\"; do echo \"### $w\"; grep -n -o \".\\{80\\}$w.\\{250\\}\" KLN_1966.txt | head -2; done; echo \"### dare v\"; grep -n -o \"dare,  intr[^|]\\{0,350\\}\" KLN_1966.txt | head -2",
 "description": "Klein female/fetus/dare"
}
```


### [2026-09-05T18:24:36.798Z] TOOL RESULT

```
### femella
### fetus,  n
### affiliate
14717:enaim,  ‘1  suck’,  Bret. denaff,  of  s.m.,  Mir.  del,  ‘teat,  nipple’.  Cp. affiliate,  dug,  ‘teat’,  effeminate,  effete,  epithelium, fecund,  felicity,  female,  feminine,  fennel,  fenu¬ greek,  fetus,  Fitz-,  thely-,  the  first  element  in hidalgo  and  the  second  element  in  sainfoin. Derivatives:  filial-ity,  h.,  fili
14717:s,  ‘son’, /i/fa,  ‘daughter’.  See filial  and  verbal  suff.  -ate  and  cp.  affiliate, filiation,  n.,  the  act  of  filiating;  affiliation.  —  F., fr.  ML.  filidtionem,  acc.  of  filiatio,  fr.  filiare. See  prec.  word  and  -ion. filibeg,  n.,  a  kilt.  —  Gael,  feileadh  beag,  fr. feileadh,  ‘kilt’,  and  beag,  ‘small’.
### dear,  durran
### OE. durran
### dare v
10340:dare,  intr.  and  tr.  v.  —  ME.  dar,  ‘I  dare’  (in  the past  tense  dorste,  durste),  fr.  OE.  ic  dearr,  ‘I dare’  (in  the  past  tense  dorste),  rel.  to  OHG.  tar , ‘I  dare’,  Goth,  ga-daursan,  ‘to  dare’,  preterite ga-dars,  ‘dared’,  fr.  I.-E.  base  *dhars-,  *dhers-, ‘to  dare,  be  courageous’,  whence  also  OI. dharsati,  ‘dares’,
```


## [2026-09-05T18:24:47.606Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/دایی/\" --note \"page 123, entry 1 node 2: Mo'in/Dehkhoda entry for دایی (maternal uncle), checking origin tag\" 2>&1 | tail -3",
 "description": "Fetch Mo'in entry for دایی"
}
```


### [2026-09-05T18:24:51.944Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8ed44a914710298b.txt
```


## [2026-09-05T18:24:54.492Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n \"معین\\|ترکی\\|دایی\" 8ed44a914710298b.txt | head -20",
 "description": "Read abadis دایی"
}
```


### [2026-09-05T18:24:54.539Z] TOOL RESULT

```
1:URL: https://abadis.ir/fatofa/دایی/
4:TITLE: دایی - معنی در دیکشنری آبادیس
6:دایی - معنی در دیکشنری آبادیس 
10: دایی
13: مترادف دایی : خال، خالو
21: دایی. ( اِ ) دائی. خال. برادر مادر. خالو. دای. مربرار : 
23:کو عمه و عم و خاله و دایی کو. تأثیر.
27: برادرمادر، خالو، دایی
30: فرهنگ معین
40: [ویکی فقه] دایی به برادر مادر گفته می شود.
43:احکام دایی
44:انسان می‏ تواند مالک دایی خود- که برده است- گردد، گرچه مکروه است 
45: دایی محرم انسان است؛ بنابر این، ازدواج با او جایز و صحیح نیست؛ هرچند با واسطه باشد، مانند دایی پدر یا مادر. در این حکم فرقی بین دایی نسبی و رضاعی نیست. 
47:← نفقه دایی
49:... wikifeqh: دایی 
53: دایی (عنوان). دایی[ ۱] ( به عربی: دای ) لقبی تُرکی[ ۲] [ ۳] و عنوان اشرافی بود که به حاکمان پادشاهی الجزایر عثمانی، طرابلس و تونس تحت سلطه امپراتوری عثمانی از سال ۱۶۷۱ به بعد داده می شد. [ ۴] از آغاز تا پیش از اشغال الجزایر توسط فرانسه در سال ۱۸۳۰، بیست و نه دایی منصوب شده بودند. این عنوان توسط رهبران غیرنظامی، نظامی و مذهبی محلی برای حکومت مادام العمر انتخاب می شد و با درجه بالایی از خودمختاری از سلطان عثمانی حکومت می کرد. منابع اصلی درآمد وی مالیات بر مردم کشاورزی، خراجهای مذهبی و پرداخت های حمایتی از طرف دزدان دریایی بربر بود که به حمل و نقل دریای مدیترانه حمله می کردند. در بخش اروپایی امپراتوری عثمانی، به ویژه در دوره انحطاط، رهبران غیرقانونی یا ماک که گاه غیرقانونی بودند، گاهی عنوان داهی را کسب می کردند که از عنوان دایی گرفته شده بود. قلمرو سلطنت الجزایر به سه استان ( کنستانتین، تیتری و ریمل ) تقسیم شد که هر یک از آنها توسط یک بیگ ( بای ) که او منصوب کرده بود اداره می شد. آخرین فرد دارای منصب «دایی» طرابلس، توسط احمد قارامانلی کشته شد، وی سلسله قارامانلی را در سال ۱۷۱۱ تأسیس کرد. [ ۵] 
54: wiki: دایی (عنوان) 
65: خریدار مال دزدی، عمو، دایی
74:واژه دایی از ریشه ی واژه ی دایه فارسی هست 
78:زبان های ترکی�در چند مرحله بر�زبان فارسی�تأثیر گذاشته است. نخستین تأثیر زبان ترکی بر پارسی، در زمان حضور سربازان تُرک در ارتش�سامانیان�روی داد. پس از آن، در زمان فرمان روایی�غزنویان، �سلجوقیان�و پس از�حملهٔ مغول، تعداد بیشتری�وام واژهٔ�ترکی به زبان فارسی راه یافت؛ اما بیشترین راه یابی واژه های ترکی به زبان فارسی در زمان فرمانروایی�صفویان، که ترکمانان�قزلباش�در تأسیس آن نقش اساسی داشتند، و�قاجاریان�بر ایران بود.
```


## [2026-09-05T18:25:01.046Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '18,42p' 8ed44a914710298b.txt",
 "description": "Read Mo'in section of abadis دایی"
}
```


### [2026-09-05T18:25:01.095Z] TOOL RESULT

```
 لغت نامه دهخدا

 دایی. ( اِ ) دائی. خال. برادر مادر. خالو. دای. مربرار : 
ام و اب و خواهر و برادر چه شدند
کو عمه و عم و خاله و دایی کو. تأثیر.

 فرهنگ فارسی

 برادرمادر، خالو، دایی
( اسم ) برادر مادر خال خالو 

 فرهنگ معین

 (اِ. ) برادر مادر، خال . 

 فرهنگ عمید

 برادر مادر، خالو، کاکو، کاکویه. 

 دانشنامه اسلامی

 [ویکی فقه] دایی به برادر مادر گفته می شود.
از آن در بابهای تجارت، نکاح، اطعمه و اشربه و ارث نام برده ‏اند.
```


## [2026-09-05T18:25:23.523Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (8811,12998,13395,13402,9399):\n    idx=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=t[:idx].count('\\f')\n    pg=t.split('\\f')[leaf]\n    cols=re.findall(r'\\b(1?\\d{3})\\b',pg[:400])\n    print('line',ln,'leaf',leaf,'head-nums',cols[:8])\nEOF",
 "description": "Compute Bartholomae leaves/columns"
}
```


### [2026-09-05T18:25:25.167Z] TOOL RESULT

```
line 8811 leaf 258 head-nums []
line 12998 leaf 403 head-nums ['437', '149', '321', '146']
line 13395 leaf 421 head-nums []
line 13402 leaf 422 head-nums ['133']
line 9399 leaf 278 head-nums ['131']
```


## [2026-09-05T18:26:18.446Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg123.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/123.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-05T18:26:18.534Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T18:26:20.856Z] TOOL CALL #67: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/123.png",
 "description": "Confirm PNG copied"
}
```


### [2026-09-05T18:26:20.898Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/123.png
```


## [2026-09-05T18:32:52.425Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 123,\n \"book_page\": 93,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Dhars, Dhers\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *dʰers- 'to venture, be bold, dare' (older 'to attack, go at'); Pokorny 259, LIV² 147\",\n   \"note\": \"Pokorny I 259 heads the entry exactly 'dhers- „wagen, kühn sein“, älter „angreifen, losgehen“ (auch mit -i-, -u- erweitert)'. Nourai's double citation form 'Dhars, Dhers' is Klein's, who writes 'fr. I.-E. base *dhars-, *dhers-, to dare, be courageous' s.v. dare — Dhars is simply the o/full-grade seen in Skt dharṣayati, Av. daršam. Language label ('Indo-European') and gloss ('to dare') are both right. All four branches Nourai draws (Iranian, Germanic, Latin, and the Persian word) are Pokorny's own on p.259, except the Persian dorošt, which Pokorny himself puts under a different root on p.216 — as the chart's own note admits.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *dʰers- «دلیر بودن، یارا کردن، جسارت ورزیدن» (معنای کهن‌تر: «تاختن، هجوم بردن») در پوکورنی ص ۲۵۹ و در LIV ص ۱۴۷ آمده است. صورت دوگانهٔ «Dhars, Dhers» که نورایی می‌آورد از کلاین گرفته شده است؛ Dhars همان درجهٔ آوایی o/کامل است که در سنسکریت dharṣayati و اوستایی daršam دیده می‌شود. برچسب زبانی و معنای ریشه هر دو درست است. تنها اشکالِ این نمودار در واژهٔ فارسی «درشت» است که خودِ پوکورنی آن را در ص ۲۱۶ زیر ریشهٔ دیگری آورده — نکته‌ای که نورایی نیز در حاشیهٔ نمودار به آن اعتراف کرده است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰers-\",\n    \"https://www.etymonline.com/word/dare\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:259\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 269/270 (running head 259): 'dhers- „wagen, kühn sein“, älter „angreifen, losgehen“' — with ai. dhṛṣṇóti, av. daršam Adv. „heftig, sehr“, apers. adaršnauš „er wagte“, lat. infestus/infestāre/manifestus (*dhers-to-), ahd. (gi)tar, (gi)turran „wagen“. Exactly Nourai's root, label and gloss.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 864 (= WP. I 864)\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt line 80794: 'dhers- „wagen, kühn sein“ (auch mit -a- Stammbildung)' with the same Indo-Iranian, Greek, Germanic and Baltic material.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dhers-\", \"stance\": \"supports\", \"note\": \"'dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhṛs- ... in Old English dearr and durst ... DARE ... [Pok. dhers- 259.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. dhr̥sus / dhorsios\", \"stance\": \"supports\", \"note\": \"'dhr̥sus, os, is ‘bold’ ... WP I, 864 & 871 Skt. dhr̥ṣṇuh; Av. daroš- ‘dare’; daršiš ‘violent’; Gk. thrasús ...; OHG turri, MHG türre ‘bold’; Go. ga-dauŕsan ‘dare’'.\"},\n    {\"src\": \"SYN\", \"where\": \"16.51 DARE, pp. 1148-1149\", \"stance\": \"supports\", \"note\": \"Buck's table for 'DARE' lists 'Skt. dhr̥ṣ-, OPers. darš-, Goth. gadaursan, OE durran, OHG giturran, NE dare' and the discussion opens 'an inherited group ... *dhers-. Walde-P. 1.864.'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *darš¹ 'to dare' (p. 62)\", \"stance\": \"supports\", \"note\": \"'*darš¹ ‘to dare’ ... «PIE *dʰers- ‘to attack, venture, dare, be bold, audacious’ = LIV: 147 | Pok.: 259'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"darš; daršam\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Old Persian darš- 'to dare' is attested in the sigmatic imperfect adaršnauš <a-d-r-š-n-u-š> 'he dared' (Bisitun I.53) and in the reduplicated personal name Dādarši- (Kent, Lexicon p. 190); Avestan has the adverb daršam 'vehemently, very' and the adjectives darši-, daršyu-, daršita- 'bold', with the Young Avestan compound verb upa-darəs- 'to dare' (Yt 8.44 upadarəšnuuainti). Both continue PIE *dʰers- with the regular Indo-Iranian developments *dʰ > d and *s > š after r (RUKI), matching Skt dhṛṣṇóti 'he dares', dhṛṣṭá- 'bold'. Nourai's gloss 'boldly' for daršam renders Bartholomae's/Pokorny's 'heftig, sehr' — the adverb is really an intensifier that shades into 'boldly'; the root gloss 'dare, to be bold' is exact.\",\n     \"derivation_fa\": \"پارسی باستان darš- «یارا کردن، دلیری کردن» در صورت ماضی سیگماتیک adaršnauš «یارا کرد» (بیستون، بند ۵۳ ستون یکم) و در نام خاصِ دوگان‌ساخته Dādarši- گواهی شده است؛ در اوستایی قید daršam «سخت، بسیار» و صفت‌های darši-, daršyu-, daršita- «دلیر» و فعل مرکبِ اوستایی نو upa-darəs- به کار رفته‌اند. هر دو از *dʰers- هندواروپایی‌اند با دو دگرگونی آواییِ قاعده‌مندِ هندوایرانی: *dʰ > d و *s > š پس از r (قاعدهٔ RUKI)؛ همتای سنسکریت آن dhṛṣṇóti «یارا می‌کند» است. برگردانِ نورایی از daršam به «boldly» کمی آزاد است (بارتولومه و پوکورنی «heftig, sehr» می‌دهند) ولی معنای ستاک درست است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰers-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:259\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 270: 'av. daršam Adv. „heftig, sehr“, darši-, daršyu-, daršita- „kühn“, apers. adaršnauš „er wagte“, dādarši- EN'.\"},\n      {\"ref\": \"SYN:1149\", \"status\": \"supports\", \"note\": \"Buck 16.51 DARE (the table on p.1148 continues to p.1149): 'Skt. dhr̥ṣ-, OPers. darš-'; the paragraph on p.1149 groups them with Goth. gadaursan, OE durran, NE dare under 'Walde-P. 1.864'.\"},\n      {\"ref\": \"KNT:190\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 205/206 (Lexicon p. 190): 'darš- vb. ‘dare’: GAv. dərəš- ‘deed of violence’, Skt. dhr̥ṣ-noti ‘dares’, NEng. dare ... adaršnauš imf.' and, on the same page, 'Dādarši- ... Perf. of darš- ‘dare’, with reduplication'. Nourai's page reference is precise.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"BRT.txt leaf 403, s.v. darš-\", \"stance\": \"supports\", \"note\": \"'Zum V. darš: — 1) NA. liest daršam „sehr“ ...' and 'j. darəšyav- Adj. „kühn, stark“, vom Wind: vātahe kəhrpa'.\"},\n      {\"src\": \"KNT\", \"where\": \"Lexicon p. 190 and §80/§84\", \"stance\": \"supports\", \"note\": \"Besides the lexicon entry, KNT.txt line 2573 lists 'adaršnauš „dared“ (Skt. ádhr̥ṣṇot)' among the OP -š imperfects, i.e. the form is morphologically as well as lexically secure.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *darš¹ (p. 62)\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: darš- ‘to dare’ — Kent: 190b. Pres. nu-: impf. IND. 3sg. adaršnauš (DB 1.53). *AVESTAN: (+ *upa-) Y Av. upadarəs- ‘to dare’'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"dorošt «درشت»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"NP دُرشت dorošt/dorušt 'coarse, rough, big'. Nourai follows Horn, Grundriss no. 552 (p. 122), who sets it beside 'ap. adarš- „wagen“, adaršnauš, daršam „heftig, sehr“; aw. √darəs- „wagen“, darši-; ai. √dharṣ-, dhṛṣṇoti' and reports on p. 123 that Nöldeke reached the same etymology independently, starting from Skt dhṛṣṭá- 'keck, frech'. Hübschmann rejected it two years later on phonological grounds (Persische Studien no. 552 and § on p. 61): 'Np. durušt „rauh, grob, derb, hart“ setzt ein iran. *družta- voraus. Aus *dṛšta- (= skr. dhṛṣṭá- „keck, frech“) wäre np. *dišt geworden' — Iranian *ṛ before the -šta- cluster gives NP i-, not the anaptyctic uru- of durušt/durust. Pokorny agreed: on p. 216, under 1. deru-, dreu- 'tree; firm, hard as wood', he cites 'npers. durušt „hart, stark“, durust „gesund, ganz“' as evidence for the age of the s-formation of the trust/true group — which is exactly what the chart's own note records. Aryanpur's modern IE-roots dictionary of Persian (p. 273, s.v. درشت, citing BQT:837) likewise cross-refers درشت back to دار and درست and lists Pahlavi drust, drustīh, ON traustr, OE trēowe. Mo'in's footnote in Borhan-e Qate' p. 837 reports both views side by side. Nourai's derivation is therefore the older, minority one; the prevailing view attaches dorošt to *drwa-/*dreu- 'firm, hard' and makes it a doublet of durust 'sound, whole'.\",\n     \"derivation_fa\": \"«درشت» در فارسی نو به معنی «زبر، ستبر، بزرگ». نورایی از هرن (بند ۵۵۲، ص ۱۲۲) پیروی می‌کند که آن را کنارِ پارسی باستان adarš- «یارا کردن»، daršam و اوستایی √darəs- و سنسکریت √dharṣ- می‌نشاند و در ص ۱۲۳ می‌افزاید که نُلدکه نیز جداگانه به همین ریشه‌شناسی رسیده بوده است. اما هوبشمان دو سال بعد در «پژوهش‌های ایرانی» (بند ۵۵۲ و ص ۶۱) آن را با دلیل آوایی رد کرد: «durušt فارسی نو ایرانیِ *družta- را پیش‌فرض می‌گیرد؛ از *dṛšta- (= dhṛṣṭá- سنسکریت) در فارسی نو باید *dišt می‌شد» — یعنی *ṛ ایرانی پیش از خوشهٔ -šta- در فارسی به «ای» بدل می‌شود، نه به «اُرُ». پوکورنی هم در ص ۲۱۶ زیر ریشهٔ deru-/dreu- «درخت؛ سخت و استوار چون چوب» می‌آورد: «npers. durušt „سخت، نیرومند“، durust „سالم، تمام“»، درست همان چیزی که خودِ حاشیهٔ نمودار نقل کرده است. آریان‌پور نیز (ص ۲۷۳، با ارجاع به برهان قاطع ۸۳۷) «درشت» را به «دار» و «درست» بازمی‌گرداند و پهلوی drust و drustīh را در کنار آن می‌نشاند. معین در حاشیهٔ برهان قاطع ص ۸۳۷ هر دو رأی را نقل کرده است. نتیجه: پژوهش امروزی رأی نورایی را نمی‌پذیرد و «درشت» را دوگانهٔ «درست» از ریشهٔ *drwa- «استوار» می‌داند.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"HRN:122\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 143 (p. 122), no. 552: 'durušt „rauh, grob, stark“, durušti. ap. adarš- „wagen“, adaršnauš, daršam „heftig, sehr“; aw. √darəs- „wagen“, darši-; ai. √dharṣ-, dhṛṣṇoti' — continued p. 123: 'Als eine Bestätigung für diese Etymologie dient der Umstand, dass Herr Prof. Nöldeke mir dieselbe ebenfalls mitteilte'. Exactly Nourai's claim.\"},\n      {\"ref\": \"BQT:837\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 297 (printed 837), Mo'in's footnote to درشت: '... (جرأت، جسارت، کوشش) و اوستا darši ... و هوبشمان از ریشهٔ ایرانی *družt- می‌داند'; i.e. Mo'in cites Skt dhṛṣṇu- next to Hübschmann's competing *družta-, so the page supports Nourai's family but records the rival derivation as well.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien no. 552; and p. 61 (f) 'Einschub von u'\", \"stance\": \"contradicts\", \"note\": \"'552. Np. durušt „rauh, grob, derb, hart“ ... setzt ein iran. *družta- voraus. Aus *dṛšta- (= skr. dhṛṣṭá- „keck, frech“) wäre np. *dišt geworden.' and p. 61 'durust „rauh, grob“ = *družta-'.\"},\n      {\"src\": \"POK\", \"where\": \"p. 216, s.v. 1. deru-, dreu-\", \"stance\": \"contradicts\", \"note\": \"POK_01.txt leaf 226 (running head 216): '... mhd. getrüste „Schar“ (die s-Bildung ist alt wegen npers. durušt „hart, stark“, durust „gesund, ganz“)'. Pokorny files the word under 'tree; firm', not under dhers- p.259.\"},\n      {\"src\": \"ARY\", \"where\": \"p. 273 s.v. درشت (ARY_pages.txt leaf 271, citing BQT 837)\", \"stance\": \"contradicts\", \"note\": \"The entry's note reads 'بازگشت به: دار، درست' and lists Pahlavi drustīh/drust, Old Icelandic traustr, OE trēowe, Norwegian tryst — the *deru-/'firm, true' family, not the 'dare' root.\"},\n      {\"src\": \"PHD\", \"where\": \"searched PHD.txt / PHD_mackenzie.txt\", \"stance\": \"silent\", \"note\": \"MacKenzie has only 'drust [drw(y)st | N durust] right; well, healthy'; no Pahlavi *društ 'rough' is recorded, so the Middle Persian stage cannot decide between the two etymologies.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *darš¹ (p. 62)\", \"stance\": \"silent\", \"note\": \"Cheung's entry for the verb *darš 'to dare' lists Av., OP, Khotanese darv-, Bal. durrit/durr- but no NP durušt — he does not treat the adjective as a continuant of this root.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Old High German\",\n     \"words\": \"tar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OHG (gi)tar 'I dare', infinitive (gi)turran, is the preterite-present that continues the PIE perfect *dʰe-dʰors-e (cf. Skt dádharṣa 'he has dared'), with Germanic *ders-/*durs- from the o-grade and zero-grade. Pokorny 259 prints 'ahd. (gi)tar, (gi)turran „wagen“' beside got. ga-dars, gadaursan and as. gidurran. Nourai's bare 'tar' (without the perfective gi-) is Klein's citation form: s.v. dare Klein writes 'rel. to OHG. tar, ‘I dare’, Goth. ga-daursan'. Gloss 'dare' correct.\",\n     \"derivation_fa\": \"صورت آلمانی علیای کهن (gi)tar «یارا می‌کنم»، مصدر (gi)turran، از فعل‌های «ماضی‌ـ‌حالی» ژرمنی است که بازماندهٔ ماضی نقلیِ هندواروپایی *dʰe-dʰors-e است (سنجیده شود با سنسکریت dádharṣa «یارا کرده است»)؛ ژرمنی *ders-/*durs- از درجه‌های آوایی o و صفر ساخته شده است. پوکورنی در ص ۲۵۹ همین صورت را می‌آورد. آوردنِ «tar» بدون پیشوند gi- شیوهٔ کلاین است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/dare\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. dhers-: 'O-grade form *dhors- and zero-grade form *dhṛs- respectively in Germanic *ders- and *durs- in Old English dearr and durst ... durran, to venture: DARE'. AHD cites the OE rather than the OHG form, but the branch is the same one Nourai draws.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p. 259\", \"stance\": \"supports\", \"note\": \"'got. ga-dars (: ai. Perf. dadhárṣa „hat sich erkühnt“), Inf. gadaúrsan „ich wage“, as. gidurran, ags. dear, durran, ahd. (gi)tar, (gi)turran „wagen“'.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. dare\", \"stance\": \"supports\", \"note\": \"'dare, intr. and tr. v. — ME. dar ... fr. OE. ic dearr „I dare“ ..., rel. to OHG. tar, ‘I dare’, Goth. ga-daursan, ‘to dare’ ... fr. I.-E. base *dhars-, *dhers-, ‘to dare, be courageous’'. Klein's citation form 'OHG. tar' is verbatim Nourai's node.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. dhr̥sus\", \"stance\": \"supports\", \"note\": \"'OHG turri, MHG türre, MLG dürre ‘bold’; Go. cf. ga-daúrsan ‘dare’'.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"dare\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English dare continues OE durran 'to be bold enough, have courage', a preterite-present verb whose 1/3sg present was dearr and past dorste (> durst); ME durren/daren, regularised as a weak verb in the 16th c. It is the direct English cognate, not a descendant, of the OHG form in the parent node: both go back to Germanic *ders-/*durs- < PIE *dʰers-. Nourai's arrow OHG > English is genealogically loose (English inherits it, it did not borrow it from German), but the root attribution is right.\",\n     \"derivation_fa\": \"فعل انگلیسی dare دنبالهٔ انگلیسی کهن durran «جرأت داشتن» است؛ صیغهٔ حالِ اول‌ و سوم‌شخصِ آن dearr و ماضی‌اش dorste (> durst) بود و در سدهٔ شانزدهم به فعل باقاعده بدل شد. این واژه هم‌ریشهٔ صورت آلمانی علیای کهن است، نه برگرفته از آن؛ هر دو از ژرمنی *ders-/*durs- و آن از *dʰers- هندواروپایی می‌آیند. پس پیکانِ «آلمانی علیای کهن ← انگلیسی» در نمودار از نظر خویشاوندی دقیق نیست (وام‌گیری در کار نبوده)، ولی انتسابِ ریشه درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/dare\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; it inherits AHD from the parent Old High German node, which does support the chain.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. dare\", \"stance\": \"supports\", \"note\": \"'ME. dar, ‘I dare’ (in the past tense dorste, durste), fr. OE. ic dearr ... fr. I.-E. base *dhars-, *dhers-'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dhers-\", \"stance\": \"supports\", \"note\": \"'... in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST).'\"},\n      {\"src\": \"SYN\", \"where\": \"16.51 DARE p. 1149\", \"stance\": \"supports\", \"note\": \"'5. Goth. gadaursan, OE durran, OHG giturran, etc., above, 1.' — Buck treats NE dare as the direct continuation of OE durran.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"infestare\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Latin infestāre 'to attack, disturb, molest' is a denominative of the adjective infestus 'hostile, dangerous, unsafe' (Plautus onwards), which is paired with manifestus 'caught in the act, palpable'. Both are analysed as containing a second element *-festus < *dʰers-to- 'attacked, seized' (so Pokorny 259, and Klein s.v. infest: 'fr. infestus ... lit. ‘seized’, rel. to manifestus ... and prob. cogn. with OI. dharṣati, ‘dares’, Gk. θάρσος, θράσος'). The connection is expressly flagged as uncertain by Walde-Pokorny ('Zugehörigkeit von lat. infestus ... und manifestus, die ein hochstufiges *dhers-to- gegenüber ai. dhṛṣṭá- voraussetzen würden, ist unsicher'), by Watkins ('2. Possibly Latin -festus'), and by Ernout-Meillet, who leave the element unexplained ('Cf. in-festus? ... la formation est étrange'). Note also that Nourai's node gives the derived verb, whereas the etymon proper is the adjective infestus.\",\n     \"derivation_fa\": \"لاتینی infestāre «تاختن، آزردن، آشفتن» فعلی است ساخته از صفت infestus «دشمن‌خو، خطرناک» که با manifestus «آشکار، مچ‌گرفته» جفت است. جزء دومِ هر دو را *-festus از *dʰers-to- «تاخته، گرفته‌شده» می‌دانند (پوکورنی ص ۲۵۹؛ کلاین ذیل infest). ولی این پیوند را والده‌ـ‌پوکورنی صریحاً «نامطمئن» خوانده است، واتکینز با قید «شاید» آورده و ارنو ـ می‌یه نیز جزء دوم را ناشناخته گذاشته‌اند. افزون بر این، ریشه‌واژه صفتِ infestus است نه فعلِ infestāre که نورایی در جعبه آورده. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://www.etymonline.com/word/infest\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. dhers-: '2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against” ...): INFEST; b. manifestus, palpable, evident ...: MANIFEST.' AHD gives the branch Nourai draws but marks it as merely possible.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p. 259\", \"stance\": \"supports\", \"note\": \"'lat. infestus „feindlich“, infestāre „feindlich behandeln, angreifen“ und manifestus „handgreiflich, auf der Tat ertappt; offenkundig“ (*dhers-to-)'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 864\", \"stance\": \"partial\", \"note\": \"'Zugehörigkeit von lat. infestus „feindlich“, infestare ... und manifestus ..., die ein hochstufiges *dhers-to- gegenüber ai. dhṛṣṭá- voraussetzen würden, ist unsicher (s. Wf. LEWb.² 385)'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. manufestus (and infestus)\", \"stance\": \"partial\", \"note\": \"'manufestus (mani-) ... Cf. in-festus? Si le premier élément est bien le nom de la „main“, la formation est étrange en face de manceps' — the -festus element is left unexplained, neither confirmed nor denied for *dhers-.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. infest\", \"stance\": \"supports\", \"note\": \"'F. infester, fr. L. infestare, ‘to trouble, disturb, molest’, fr. infestus ... lit. ‘seized’, rel. to manifestus, ‘evident’, ... and prob. cogn. with OI. dharṣati, ‘dares’.'\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"infest, manifest\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English infest (late 15c. infesten 'to attack, assail, distress') comes through Old French infester (14c.) from Latin infestāre; the modern sense 'swarm over parasitically' is only c. 1600. Manifest (adj., late 14c. 'clearly revealed') comes through Old French manifest (12c.) or directly from Latin manifestus; the verb manifest and the noun manifesto (from Italian, 1640s) follow. The Romance-to-English route is uncontroversial; the only uncertainty in this chain lies further back, in the Latin -festus element (see node #5).\",\n     \"derivation_fa\": \"انگلیسی infest (سدهٔ پانزدهم، infesten «تاختن، آزردن») از راه فرانسویِ کهن infester از لاتینی infestāre آمده و معنای امروزیِ «هجوم انگلی» تنها از حدود ۱۶۰۰ پیدا شده است. manifest (صفت، سدهٔ چهاردهم) از فرانسویِ کهن manifest یا مستقیماً از لاتینی manifestus گرفته شده و سپس فعلِ manifest و اسمِ manifesto (از ایتالیایی، دههٔ ۱۶۴۰) از آن ساخته شده‌اند. این حلقهٔ لاتینی ← فرانسوی ← انگلیسی هیچ مناقشه‌ای ندارد؛ تنها ابهام در جزء لاتینیِ -festus است (نگاه کنید به گرهٔ ۵). ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/infest\", \"https://www.etymonline.com/word/manifest\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference given by Nourai for this node; it inherits AHD from the Latin parent, where the two English words are indeed the head words (INFEST, MANIFEST).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. infest\", \"stance\": \"supports\", \"note\": \"'F. infester, fr. L. infestare ... fr. infestus ... rel. to manifestus, ‘evident’, lit. ‘that which can be seized by the hand’.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dhers-\", \"stance\": \"supports\", \"note\": \"The root entry ends its Latin section with the capitalised English head words 'INFEST' and 'MANIFEST'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Dhě 1, Dhe-mnâ\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *dʰeh₁(y)- 'to suckle, nurse' (Pokorny 241 dhē(i)-), with the derivative *dʰē-mnā- 'she who suckles'\",\n   \"note\": \"Pokorny I 241 has 'dhē(i)- (daneben dh-ei-?) „saugen, säugen“' with the nominal derivatives dhē-lā 'Mutterbrust', dhē-nā, dhē-nu-, and the note that the Latin fē-group (fēcundus, fētus, fēnus, fēlīx) 'erklären sich aus einer Sonderanwendung von dhē(i)- „säugen“ für „fruchtbar sein“' — which is Nourai's second gloss 'to produce'. His second head word 'Dhe-mnâ: one who gives milk, nurse' is Watkins's '*dhē-mnā- in Latin fēmina, woman (< “she who suckles”)'. Root, label and glosses are therefore all right. Two reservations that do not touch the root box itself: (a) Nourai's cross-reference 'Compare with the root Dheugh: to milk' is his own — Pokorny's dheugh- (p. 271) is 'to produce something of utility' and is not connected with dhē(i)-; (b) the grain branch (nodes #3, #4, and Sogdian d`n) is explicitly EXCLUDED from this root by the very page Nourai cites (POK 242: 'dazu aber nicht *dhōnā- „Getreide“'). See the node entries.\",\n   \"note_fa\": \"پوکورنی در ص ۲۴۱ ریشهٔ dhē(i)- «مکیدن، شیر دادن» را با مشتق‌های dhē-lā «پستان»، dhē-nā و dhē-nu- می‌آورد و می‌افزاید که خانوادهٔ لاتینیِ fēcundus, fētus, fēnus, fēlīx «از کاربردِ ویژهٔ این ریشه به معنی „بارور بودن“ پدید آمده‌اند» — و همین است معنای دومی که نورایی («to produce») داده است. سرواژهٔ دومِ او یعنی Dhe-mnâ همان *dʰē-mnā- «شیردهنده» است که واتکینز برای femina لاتینی بازسازی می‌کند. پس ریشه، برچسب زبانی و معناها درست‌اند. دو نکته اما بیرون از خودِ جعبهٔ ریشه: نخست اینکه ارجاع «سنجیده شود با ریشهٔ Dheugh» از خودِ نورایی است و پوکورنی این دو را به هم پیوند نداده؛ دوم اینکه شاخهٔ «دانه» (گره‌های ۳ و ۴ و سغدیِ d`n) را همان صفحه‌ای که نورایی به آن ارجاع می‌دهد (پوکورنی ۲۴۲) صریحاً از این ریشه بیرون می‌گذارد: «dazu aber nicht *dhōnā- „غلّه“».\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeh₁(y)-\",\n    \"https://www.etymonline.com/word/female\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:241\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 251-253 (running heads 241, 242): 'dhē(i)- (daneben dh-ei-?) „saugen, säugen“ ... Nominalbildungen: dhē-lā „Mutterbrust“, dhi-lo- „Zitze“, dhē-lu- „säugend“, dhei-nā „trächtig“, dhē-nā „Fruchtertrag“' — and 'lat. femina „Frau“ („*die säugende“)'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 829-831\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt line 77838: 'dhēi- „saugen, säugen“ (: dhī-, dhi- und dhē-, dhā-, s. bes. Schulze KZ. ...)' — the earlier form of the same article Pokorny reprints.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dhē(i)-\", \"stance\": \"supports\", \"note\": \"'dhē(i)-. To suck. Contracted from *dheə(i)-. 1. Suffixed reduced form *dhē-mnā- in Latin fēmina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE ... [Pok. dhē(i)- 241.]' — the source of Nourai's second head word 'Dhe-mnâ'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, searched for dhē-/dhēnā/dhōnā head words\", \"stance\": \"silent\", \"note\": \"IEC.txt has 'dhēiō dhēmi (2) ‘put, lay’' (the homonymous root *dʰeh₁-) but no separate head word for the 'suckle' root in the OCR I could locate; no evidence either way.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"daenu\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan daēnu- f. 'female (of quadrupeds), dam' (Vd. 7.42 daēnu 'she-camel' as the price of a service; A. 3.10 daēnunąm 'of the females') is the exact equivalent of Skt dhenú- f. 'milch-cow, milking', both from *dʰeh₁-nu- 'milk-giving', a -nu- derivative of *dʰeh₁(y)- 'to suckle'. Pokorny prints the equation verbatim on p. 242: 'dhenú- f. „milchend“ = av. daēnu- „Weibchen von vierfüssigen Tieren“'. Nourai's short gloss 'female' is a compression of that; strictly the word means 'female animal, dam', i.e. 'the one that gives milk'.\",\n     \"derivation_fa\": \"اوستایی daēnu- (مؤنث) «مادینهٔ چارپایان» (وندیداد ۷.۴۲ در معنیِ «مادّه‌شتر»، و آبان‌یشت/آفرینگان ۳.۱۰ daēnunąm) برابرِ دقیقِ سنسکریت dhenú- «گاو شیرده» است؛ هر دو از *dʰeh₁-nu- «شیردهنده»، مشتقی با پسوند -nu- از ریشهٔ *dʰeh₁(y)- «شیر دادن». پوکورنی در ص ۲۴۲ همین برابری را عیناً می‌آورد. برگردانِ کوتاهِ نورایی («female») فشردهٔ همین معناست؛ معنای دقیق‌تر «مادینهٔ جانور، شیرده» است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeh₁(y)-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:241\", \"status\": \"supports\", \"note\": \"The equation stands on the second page of the article (running head 242, POK_01.txt leaf 252): 'ai. dhenú- f. „milchend“ = av. daēnu- „Weibchen von vierfüssigen Tieren“, ai. dhēnā „Milchkuh“'. Nourai's POK:241 points at the head of the article, which is correct for the root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"BRT.txt leaf 258 (s.v. uštra-/daēnu-)\", \"stance\": \"supports\", \"note\": \"'daēnu ... „um den Preis für eine Kamelstute“ V.7.42; — (GPf.) daēnunąm paiti.puθranąm A.3.10' — Bartholomae's daēnu- is a female quadruped, as Pokorny says.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 539, p. 119\", \"stance\": \"supports\", \"note\": \"'aw. vergl. daēnu- „Weibchen (von Tieren)“' — Horn cites the same Avestan word (in connection with dāya, see node #2).\"},\n      {\"src\": \"ARY\", \"where\": \"p. 266 s.v. دایه (ARY_pages.txt leaf 264)\", \"stance\": \"supports\", \"note\": \"The entry's Avestan line reads '-daēnu-, -daēnav-' and the note says 'چم این واژه در اوستایی: ماده، مادینه' ('the sense of this word in Avestan: female').\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"dâyeh «دایه»; dâyě «دایی»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Two different words are put in one box. (1) دایه dāya 'wet-nurse, nanny' is genuine: Middle Persian dāyag [d'yk] '(wet-)nurse' (MacKenzie 55), NP dāya, ultimately from the verbal root *dʰeh₁(y)- 'to suckle' (Skt √dhā-, dhāyati 'sucks', dhātrī 'nurse'; Arm. dayeak 'nurse, tutor' is itself an Iranian loan); the Arabic دایة 'midwife' is borrowed from Persian. Horn no. 539 and Mo'in's footnote in Borhan-e Qate' p. 822 both place it exactly here, and both, like Nourai, put Av. daēnu- beside it — but with 'vergl.' ('compare'): dāya does not descend from the -nu- stem daēnu-, it is a parallel formation *dāya-ka- from the same root, so the arrow daēnu- > dāya is a cognate link rather than a line of descent. (2) دایی dāyi 'mother's brother' does NOT belong here at all: it is a Turkic loanword, from Proto-Turkic *tāy/*dāj 'maternal uncle' (Old Turkic tay, taγay; Turkish, Azerbaijani dayı), so Doerfer, Türkische und mongolische Elemente im Neupersischen I §1176 p. 196, and Hasandust, Farhang-e riše-šenāxti II p. 1264; Persian تغایی taġāyī is the same Turkic word in another shape. Nourai's own references do not support it: Horn 539 lists a variant dāī only as a by-form of dāya 'nurse/mother' (with Kurdish dā, dī, diyā 'mother'), and BQT 822 says nothing about 'mother's brother'. Verdict for the node: the worse of the two, disputed.\",\n     \"derivation_fa\": \"در یک جعبه دو واژهٔ جداگانه کنار هم نشسته‌اند. نخست «دایه» به معنی «شیرده، پرستارِ کودک» که ریشه‌شناسیِ آن درست است: فارسی میانه dāyag «دایه» (مکنزی ص ۵۵)، از ریشهٔ *dʰeh₁(y)- «شیر دادن» (سنسکریت √dhā-، dhāyati «می‌مکد»، dhātrī «دایه»؛ ارمنی dayeak خود وام‌واژه‌ای ایرانی است)؛ معرّبِ آن «دایة» به معنی قابله است. هرن (بند ۵۳۹) و حاشیهٔ معین بر برهان قاطع (ص ۸۲۲) هر دو همین را می‌گویند و مانند نورایی اوستایی daēnu- را در کنارش می‌آورند — اما با قید «vergl.» یعنی «بسنجید»: «دایه» فرزندِ ستاکِ daēnu- نیست، بلکه ساختی موازی (*dāya-ka-) از همان ریشه است؛ پس پیکانِ نمودار پیوندِ هم‌ریشگی است نه تبار. دوم «دایی» به معنی «برادر مادر» که اصلاً به این خانواده تعلق ندارد: وام‌واژه‌ای ترکی است از ترکیِ آغازین *tāy/*dāj (ترکی کهن tay، taγay؛ ترکی و آذربایجانی dayı)؛ چنین است رأی دورفر (عناصر ترکی و مغولی در فارسی نو، ج ۱، بند ۱۱۷۶، ص ۱۹۶) و حسن‌دوست (فرهنگ ریشه‌شناختی، ج ۲، ص ۱۲۶۴)؛ «تغایی» فارسی نیز همان واژهٔ ترکی است. مأخذهای خودِ نورایی هم پشتیبانِ او نیستند: هرن صورتِ dāī را تنها گونه‌ای از «دایه/مادر» می‌داند و برهان قاطع ص ۸۲۲ اصلاً از «برادر مادر» سخنی نمی‌گوید. پس: بخش نخست پذیرفتنی و بخش دوم را پژوهش امروزی رد می‌کند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/دایی\",\n      \"https://abadis.ir/fatofa/دایی/\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:822\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 282 (printed 822), Mo'in's footnote: 'دایه — ... اوستا daēnu (مادّه [از جانوران])، پهلوی dāyag (دایه)، هندی باستان ریشهٔ dhā- (شیر دادن)، ارمنی dayeak (دایه، مربّی)، کردی dāyik و dāyā (مادر) ... معرّب آن دایة (ماماه، قابله)'. Supports دایه fully; the page has no entry for دایی 'mother's brother'.\"},\n      {\"ref\": \"HRN:119\", \"status\": \"partial\", \"note\": \"HRN.txt leaf 140 (p. 119), no. 539: 'dāye „Amme“, dāī. aw. vergl. daēnu- „Weibchen (von Tieren)“; phlv. dāyak „Amme“; ai. √dhā-, dhāyati „saugen“; arm. dayeak „Amme, Erzieher“. kurd. dā, dī, diyā „Mutter“, dāīn „Mutter, Amme“'. Horn's dāī is a by-form meaning 'nurse/mother', not 'maternal uncle'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. dayag\", \"stance\": \"supports\", \"note\": \"'dayag [d’yk | M d’yg-, N -a] (wet-)nurse. -anih [-’nyh | (N dāyagī)] nursing, nurture.' — the Middle Persian stage of دایه.\"},\n      {\"src\": \"ARY\", \"where\": \"p. 266 s.v. دایه (leaf 264, citing BQT + AHD)\", \"stance\": \"supports\", \"note\": \"Lists PIE *dʰē(i)-, Avestan daēnu-/daēnav-, Pahlavi dāyag, Ossetic dæjyn, Kurdish dāyik/dāyā, Skt dhātrī, Latin fēlō/fēmina, Gothic daddjan; note 'چم واجریشهٔ هند و اروپایی این واژه: مکیدن، شیر دادن'. Nothing about a 'maternal uncle' sense.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. دایی (via abadis.ir)\", \"stance\": \"silent\", \"note\": \"Mo'in's entry is only '(اِ.) برادر مادر، خال.' — no origin tag at all, so Mo'in does not claim Iranian descent for it either.\"},\n      {\"src\": \"LKT\", \"where\": \"searched LKT.txt for dayı/tay\", \"stance\": \"silent\", \"note\": \"Lokotsch has no entry for the Turkic kinship term; the Turkic origin rests on Doerfer §1176 and Hasandust II 1264 as reported by Wiktionary.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"dânô; danâxe\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The forms are real, but the arrow from the 'suckle' root is contradicted by the very page Nourai cites. (1) dânô is the Avestan grain word: Bartholomae has 'j. dānav- f. „(Getreide)korn“' and the compound 'dānō.karš- „(Getreide)körner (ver)schleppend“, Bezeichnung einer Ameisenart' (Y. 16.12, V. 14.5) — the ant that drags grain; Nourai's 'dânô' is the compositional stem dānō-. (2) danâxe is not an Iranian form at all but δανάκη (danákē), the Greek transmission of an Old Persian coin/weight name, quoted from Herakleides in the Etymologicum Magnum; Horn no. 536 prints it as 'ap. δανάκη' and Mo'in's footnote to دانگ (BQT 820) as 'پارسی باستان (بنقل یونانی) δανάκη'. Nourai's 'danâxe' with x renders the Greek κ wrongly, and his gloss 'grain' is wrong too — δανάκη is a small coin, the sixth of a drachm (hence the child node dâng). (3) The derivation from the root: Pokorny p. 242 ends the dhē(i)- article by expressly excluding the grain word — 'dazu aber nicht *dhōnā- „Getreide“: ai. dhānāḥ f. Pl. „Getreidekörner“, dhānya- n., np. dāna „Korn“, av. dānō-karša-, toch. B tāno, lit. dúona' — i.e. the page Nourai cites (POK:242) says the opposite of his arrow. Current reconstruction agrees: Persian دانه goes back to PIE *dʰoHnéh₂, a separate etymon (of possible non-IE, BMAC origin), not to *dʰeh₁(y)-.\",\n     \"derivation_fa\": \"خودِ صورت‌ها واقعی‌اند، اما پیکانی که آن‌ها را از ریشهٔ «شیر دادن» می‌گیرد با همان صفحه‌ای که نورایی به آن ارجاع داده ناسازگار است. یکم، dânô همان واژهٔ اوستاییِ «دانه» است: بارتولومه «dānav- (مؤنث) „دانهٔ غلّه“» و ترکیبِ dānō.karš- «دانه‌کِش، نامی برای گونه‌ای مورچه» را ثبت کرده است؛ «dânô» شکلِ ترکیبیِ dānō- است. دوم، danâxe اصلاً صورتی ایرانی نیست، بلکه δανάκη (danákē) است: نامِ سکه/واحدِ وزنِ پارسی باستان که تنها از راهِ یونانی (نقلِ هراکلیدس در Etymologicum Magnum) به ما رسیده؛ هرن در بند ۵۳۶ آن را «ap. δανάκη» و معین در حاشیهٔ «دانگ» (برهان قاطع ۸۲۰) «پارسی باستان (بنقل یونانی) δανάκη» می‌نویسد. پس «danâxe» با x برگردانِ نادرستِ کافِ یونانی است و معنایی که نورایی داده («grain») نیز نادرست است: δανάκη سکه‌ای خرد و برابرِ یک‌ششمِ درهم بوده — و درست به همین سبب فرزندِ آن در نمودار «دانگ» است. سوم، دربارهٔ خودِ ریشه: پوکورنی در پایانِ مقالهٔ dhē(i)- در ص ۲۴۲ صریحاً می‌نویسد «dazu aber nicht *dhōnā- „غلّه“» یعنی واژهٔ «دانه» به این ریشه تعلق ندارد. بازسازیِ امروزی نیز همین است: «دانه» از *dʰoHnéh₂ می‌آید، ریشه‌ای جدا (و شاید غیرهندواروپایی). خطای چاپیِ کتاب در صورتِ danâxe و خطای انتساب در پیکانِ ریشه.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"danâxe : grain\",\n     \"correct_form\": \"danákē (Greek δανάκη), 'a small Persian coin, one sixth of a drachm' — not 'grain'\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/دانه\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:242\", \"status\": \"contradicts\", \"note\": \"POK_01.txt leaf 253 (running head 242), the closing paragraph of dhē(i)-: 'dazu aber nicht *dhōnā- „Getreide“: ai. dhānāḥ f. Pl. „Getreidekörner“, dhānyá- n. „Getreide“, np. dāna „Korn“, av. dānō-karša- „eine Ameisenart“, d. i. „Körner (= Ameiseneier) schleppend“, toch. B tāno „Getreide“ und lit. dúona, lett. duona f. „Brot“'. Pokorny lists exactly Nourai's words but to deny that they belong to this root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"BRT.txt leaves 421-422 (s.v. dānav-, dānō.karš-)\", \"stance\": \"supports\", \"note\": \"'j. dānav- f. „(Getreide)korn“' and 'j. dānō.karš- Adj. „(Getreide)körner (ver)schleppend“, Bezeichnung einer Ameisenart: maoirīm ... Y.16.12; — maoirinąm ... V.14.5'; cf. also 'j. kasu.dānav- Adj. „mit kleinen (Samen-)Körnern“' (leaf 278). The Avestan word is secure; Bartholomae offers no link to daēnu-.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 536, p. 118\", \"stance\": \"supports\", \"note\": \"'536. dang, dāneg „eine Münze bezw. ein Maass“. ap. δανάκη (Herakleides im Etym. magn.); phlv. dang (PPGl.), arm. LW. dang, arab. LW. dānaq ... Ursprünglich mit dāne (No. 535) identisch.' This is the source of Nourai's 'danâxe' and shows both its real shape and its real meaning.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian Lexicon\", \"stance\": \"silent\", \"note\": \"Kent has no Old Persian word for 'grain'; his dāna- (in apadāna-, daivadāna-) is a different formation, 'container, receptacle', from OP *dā- + -na- (KNT.txt line 5516). So the label 'Old Persian' on this node rests solely on the Greek-transmitted δανάκη.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dhē(i)-\", \"stance\": \"silent\", \"note\": \"Watkins's dhē(i)- article contains only the Latin fē-/Greek thēl- material; no grain word is attached to it, in line with Pokorny's exclusion.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"dâneh «دانه»; dâng «دانگ»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The internal Iranian chain drawn here is right, even though its ultimate attachment (node #3) is not. دانه dāna 'grain, seed' is inherited from Middle Persian dānag [d'n(k)] 'seed, grain' (MacKenzie), from Proto-Iranian *daHnáH, Proto-Indo-Iranian *dʰaHnáH, PIE *dʰoHnéh₂ (Skt dhānā- f.pl. 'grains', Av. dāna- in dānō-karša-, Baluchi dān/dānag, Tocharian B tāno, Lith. dúona 'bread'); MP -ag > NP -a is the regular loss of final -g. دانگ dāng 'a sixth (of a property, of a dirham)' is the same word with the diminutive/measure suffix: MP dāng, from the Old Persian coin name transmitted as Greek δανάκη, whence also Armenian dang and the Arabic loan دانق dānaq. Horn states the identity outright ('Ursprünglich mit dāne (No. 535) identisch'), Mo'in's footnote to دانگ says 'اصلاً همریشهٔ دانه است', and Wiktionary calls دانگ a doublet of دانه.\",\n     \"derivation_fa\": \"زنجیرهٔ ایرانیِ درونِ این جعبه درست است، هرچند انتسابِ نهاییِ آن (گرهٔ ۳) نادرست. «دانه» بازماندهٔ فارسی میانهٔ dānag «دانه، تخم» است، از ایرانی آغازین *daHnáH و هندوایرانیِ آغازین *dʰaHnáH و هندواروپاییِ *dʰoHnéh₂ (سنسکریت dhānā-، اوستایی dāna- در dānō-karša-، بلوچی dān/dānag، تخاری ب tāno، لیتوانیایی dúona «نان»)؛ افتادنِ -g پایانیِ فارسی میانه در فارسی نو قاعده‌مند است. «دانگ» به معنی «یک‌ششم (ملک یا درهم)» همان واژه است با پسوندِ کوچک‌ساز/واحدساز: فارسی میانه dāng، از نامِ سکهٔ پارسی باستان که یونانی δανάκη ضبط کرده، و از همان‌جا ارمنی dang و معرّبِ «دانق». هرن صریحاً می‌گوید «در اصل با دانه یکی است»، معین نیز در حاشیهٔ «دانگ» می‌نویسد «اصلاً هم‌ریشهٔ دانه است»، و ویکی‌واژه «دانگ» را دوگانهٔ «دانه» می‌خواند. ادعای نورایی در این حلقه درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/دانه\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:820\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 280 (printed 820), Mo'in's two footnotes: 'دانگ — ... پهلوی dāng، پارسی باستان (بنقل یونانی) δανάκη ... ارمنی dang، عربی معرّب دانق ... اصلاً همریشهٔ دانه (ه.م) است' and 'دانه — ... پهلوی dān(ag)، اوستا dānō-karša- (دانه‌کش)، هندی باستان dhānā- (دانهٔ گندم)، بلوچی dān(ag)، گیلکی dāna ...'. Exactly Nourai's two words, on exactly the page he cites.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. dān(ag)\", \"stance\": \"supports\", \"note\": \"'dān(ag) [d’n(k)] seed, grain.'\"},\n      {\"src\": \"HRN\", \"where\": \"nos. 535-536, p. 118\", \"stance\": \"supports\", \"note\": \"'535. dāne „Korn“ ... aw. dānō.karša- „körnerschleppend“; phlv. dānak; ai. dhānā- „Getreidekörner“' and '536. dang, dāneg ... Ursprünglich mit dāne (No. 535) identisch.'\"},\n      {\"src\": \"ARY\", \"where\": \"p. 265 s.v. دانه (leaf 263, citing BQT)\", \"stance\": \"supports\", \"note\": \"Lists Avestan dāna-, Pahlavi dān/dānag, Kurdish, Baluchi, Pashto, Sanskrit dhānā-/dhānya-, Lithuanian dúona, Tocharian A tāno.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Sogdian\",\n     \"words\": \"d`n; d`yh\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Both Sogdian forms are correctly quoted from Gharib, but only one of them can belong here, and the other is expressly given a different origin by Gharib himself. (1) δ'n (Gharib no. 3406, p. 134) 'seed', compared by Gharib with 'Av. dānō-karš' — the same grain word as node #3, hence subject to the same objection: Pokorny 242 excludes it from dhē(i)-. (2) δ'yh (Gharib no. 3454, p. 136) 'slave girl, female servant' is given the etymology '<*dāhi; Skt. dāsī', i.e. it belongs to Old Iranian *dāha- 'male/slave' (the ethnonym Dahae; cf. NP dāh 'slave', Horn no. 538, from Skt dāsá-), and has nothing to do with 'suckling'. So on Nourai's own cited page the second word contradicts his arrow; the first word supports his form but not his root.\",\n     \"derivation_fa\": \"هر دو صورتِ سغدی درست از فرهنگِ قریب نقل شده‌اند، اما تنها یکی از آن‌ها می‌تواند به این ریشه بستگی داشته باشد و دومی را خودِ قریب به ریشهٔ دیگری بازمی‌گرداند. یکم، δ'n (شمارهٔ ۳۴۰۶، ص ۱۳۴) «تخم، دانه» که قریب آن را با «اوستایی dānō-karš» می‌سنجد — یعنی همان واژهٔ «دانه» در گرهٔ ۳ و در نتیجه گرفتارِ همان ایراد: پوکورنی در ص ۲۴۲ آن را از ریشهٔ dhē(i)- بیرون گذاشته است. دوم، δ'yh (شمارهٔ ۳۴۵۴، ص ۱۳۶) «کنیز، خدمتکارِ زن» که قریب ریشه‌اش را «<*dāhi؛ سنسکریت dāsī» می‌دهد، یعنی از ایرانی باستان *dāha- «بنده» (همان نامِ قومِ داهه؛ سنجیده شود با «داه» فارسی در بند ۵۳۸ هرن) و هیچ پیوندی با «شیر دادن» ندارد. پس در همان صفحه‌ای که نورایی به آن ارجاع داده، واژهٔ دوم رأی او را رد می‌کند.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:134,136\", \"status\": \"contradicts\", \"note\": \"SOD_pages.txt leaf 199 (printed 134), no. 3406: 'δ’n M — δān ©Av. dānō-karš — seed. BBB 575'; and leaf 201 (printed 136), no. 3454: 'δ’yh B, M, S — δāy (d’y) ©<*dāhi; Skt. dāsī ©f. n.; pl. -t — slave girl, female servant. SCE 341, 373; VJ 162 etc.' The page numbers are right; the second entry gives an etymology incompatible with Nourai's root, and the first belongs to the excluded grain word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib nos. 3406 and 3454\", \"stance\": \"contradicts\", \"note\": \"As quoted above; Gharib's own etymological tags (©Av. dānō-karš / ©<*dāhi; Skt. dāsī) are the only ones he gives for these two words.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 538, p. 119\", \"stance\": \"contradicts\", \"note\": \"'538. dāh „Sklave, Diener (auch weiblich)“. ai. dāsá- „Sklave, Knecht“' — the Persian counterpart of Sogdian δ’yh, and Horn keeps it strictly apart from no. 539 dāye 'Amme'.\"},\n      {\"src\": \"BRT\", \"where\": \"BRT.txt leaves 421-422\", \"stance\": \"partial\", \"note\": \"Supplies the Avestan dānav-/dānō.karš- that Gharib compares for δ’n, but nothing that would join either Sogdian word to daēnu-.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Latin\",\n     \"words\": \"fěmina; filius; fě-tus\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All three Latin words are standard members of the *dʰeh₁(y)- family. fēmina 'woman' is *dʰeh₁-mn-eh₂ 'she who suckles' (Pokorny 241 'lat. femina „Frau“ („*die säugende“)'; Watkins *dhē-mnā-; De Vaan, EDL 210). fētus, -ūs 'bearing, offspring' with fēta 'pregnant', effētus, fēcundus, fēnus, fēlīx belongs, in Pokorny's words, to 'einer Sonderanwendung von dhē(i)- „säugen“ für „fruchtbar sein“' (De Vaan, EDL 217). fīlius 'son' is *dʰeh₁i-l-yo-s 'suckling' via Proto-Italic *fīlios (umbr. feliuf, filiu 'lactantes' shows the original sense 'sucklings'); Watkins hedges it ('Perhaps ... but these are equally possibly from the root bheuə-'), but De Vaan and Wiktionary keep it under *dʰeh₁(y)-. Nourai's hyphenated 'fě-tus' simply marks the root plus the -tu- suffix.\",\n     \"derivation_fa\": \"هر سه واژهٔ لاتینی از اعضای شناختهٔ خانوادهٔ *dʰeh₁(y)- اند. fēmina «زن» از *dʰeh₁-mn-eh₂ «شیردهنده» است (پوکورنی ص ۲۴۱: «femina لاتینی „زن“، در اصل „آن که شیر می‌دهد“»؛ واتکینز *dhē-mnā-؛ دِ وان، فرهنگ ریشه‌شناختی لاتین ص ۲۱۰). fētus «زایش، فرزند» همراه با fēta «آبستن»، fēcundus، fēnus و fēlīx به گفتهٔ پوکورنی از «کاربردِ ویژهٔ ریشهٔ dhē(i)- به معنی „بارور بودن“» برخاسته‌اند. fīlius «پسر» از *dʰeh₁i-l-yo-s «شیرخواره» است از راهِ ایتالیکِ آغازین *fīlios؛ صورتِ اومبریاییِ feliuf/filiu به معنی «شیرخوارگان» همین معنای نخستین را نشان می‌دهد. واتکینز دربارهٔ fīlius محتاط است و امکانِ ریشهٔ *bʰewH- را هم باز می‌گذارد، اما دِ وان و ویکی‌واژه آن را زیر همین ریشه نگه می‌دارند. خطِ تیره در «fě-tus» نزد نورایی تنها مرزِ ریشه و پسوندِ -tu- را نشان می‌دهد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/filius\",\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeh₁(y)-\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. dhē(i)-: '1. Suffixed reduced form *dhē-mnā- in Latin fēmina ... 2. Suffixed reduced form *dhē-to- in Latin fētus ... 5. Perhaps suffixed zero-grade form *dhī-lyo- in Latin fīlius, son, and fīlia, daughter (but these are equally possibly from the root bheuə-)'. All three of Nourai's words, with a caveat on fīlius.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"pp. 241-242\", \"stance\": \"supports\", \"note\": \"'lat. femina „Frau“ („*die säugende“) ... lat. fēlō, -āre „säugen“, fīlius „Sohn“ („*Säugling“, aus *fēlios) = umbr. feliuf, filiu „lactantes“ ... lat. fēcundus „fruchtbar“, fētus, -ūs „das Zeugen, Gebären“'.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. filial\", \"stance\": \"supports\", \"note\": \"The cross-reference list at that entry runs 'Cp. affiliate, dug „teat“, effeminate, effete, epithelium, fecund, felicity, female, feminine, fennel, fenugreek, fetus, Fitz-, thely-, hidalgo, sainfoin' — Klein groups fēmina, fētus and fīlius in one family, as Nourai does.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, searched s.v. femina/filius/fetus\", \"stance\": \"silent\", \"note\": \"The OCR of LAT.txt returns only running text mentions of femina (e.g. 'musca femina', 'masculus an femina esset'); the head-word articles could not be isolated in this scan, so Ernout-Meillet neither confirms nor denies here.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"female; affiliation; fetus\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"female: early 14c. femele, from Old French femelle (12c.), from Latin femella 'young female, girl', diminutive of femina 'she who suckles'; the spelling was refashioned after male in the 16th c. affiliation: from French affiliation, from Medieval Latin affiliātiō, from affiliāre 'to adopt as a son', ad- + fīlius. fetus: directly from Latin fētus 'offspring, bearing'. All three are the head words printed under Watkins's dhē(i)- article, and the Latin > (French >) English route is uncontroversial.\",\n     \"derivation_fa\": \"female: از سدهٔ چهاردهم به صورت femele، از فرانسویِ کهن femelle، از لاتینی femella «دخترک»، مصغّرِ femina «آن که شیر می‌دهد»؛ املای امروزی در سدهٔ شانزدهم به قیاسِ male بازساخته شد. affiliation: از فرانسوی، از لاتینیِ میانه affiliātiō و فعلِ affiliāre «به فرزندی گرفتن» از ad- + fīlius. fetus: مستقیماً از لاتینی fētus «فرزند، زایش». هر سه در فرهنگِ واتکینز ذیل همین ریشه سرواژه‌اند و راهِ لاتینی ← (فرانسوی ←) انگلیسی هیچ مناقشه‌ای ندارد. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/female\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference given; the node inherits AHD from the Latin parent, whose article ends with the head words FEMALE, FEMININE, EFFEMINATE, FETUS, FILIAL, AFFILIATE.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. filiation/filial\", \"stance\": \"supports\", \"note\": \"'filiation, n., the act of filiating; affiliation. — F., fr. ML. filiātiōnem, acc. of filiātiō, fr. filiāre' — and the same entry's cross-reference list contains female and fetus.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dhē(i)-\", \"stance\": \"supports\", \"note\": \"'FEMALE, FEMININE; EFFEMINATE ... FAWN, (FETAL), FETUS ... FILIAL, FILIATE; AFFILIATE, HIDALGO'.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('data/verification/page-123.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=1)\nprint(\"written\")\nPYEOF",
 "description": "Write page-123 verification JSON"
}
```


### [2026-09-05T18:32:55.169Z] TOOL RESULT

```
written
```


## [2026-09-05T18:33:00.024Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-123.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 123",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T18:33:01.830Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 8, 'disputed': 4, 'plausible': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'partial': 4, 'not_checked': 3, 'contradicts': 2}
books consulted: {'supports': 27, 'contradicts': 5, 'silent': 7, 'partial': 3} | by book: {'KLN': 6, 'BRT': 4, 'POK': 4, 'ARY': 4, 'AHD': 4, 'HRN': 4, 'PHD': 3, 'KNT': 2, 'CHEUNG': 2, 'LAT': 2, 'HUB': 1, 'IEC': 1, 'SYN': 1, 'WLD': 1, 'MON': 1, 'LKT': 1, 'SOD': 1}
```


## [2026-09-05T18:33:08.956Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT dayı/tay ===\"; grep -n -i \"dayı\\|dai (\\|taghai\\|tagay\\|Oheim\\|maternal uncle\" LKT.txt | head -8; echo \"(end)\"; echo \"=== LAT filius/fetus headwords ===\"; grep -n \"^filius\\|^fetus\\|^femina\\|^fetus,\" LAT.txt | head -8; echo \"(end)\"",
 "description": "Verify LKT and LAT greps"
}
```


### [2026-09-05T18:33:09.029Z] TOOL RESULT

```
=== LKT dayı/tay ===
968:[So  bei  A.  Hindoglu,  Diclionnaire  Turc- Franqais.  Vienne  1838.  S.  134  b;  aber bei  Kelekian  Kämüs  292  a:  bola,  altes Wort]  'Tante,  Frau  des  Oheims';  hieraus bulg.  bula  'Türkin'  und  mit  verschiedenen Übertragungen  'Mohn,  wilde  Schwalbe, Wiesel',  bulka  'Braut,  Schwiegertochter; Mohn',  serb.  hula  'Türkin',  bulka  'Feld- mohn'.   [Bern  SlEtWb  100.
1209:Part.  präs.  des  Vbs.  dcVa  'rufen,  zu- rufen'; ad-dä'l  war  der  Titel  des  Ge- sandten, der  die  Gläubigen  zum  heiUgen Kriege  [Gihäd]  aufzurufen  hatte;  ihn führten  auch  die  Beherrscher  Algeriens, aber  im  XVUI.  Jahrhundert  geriet  der eigentliche  Ursprung  des  Titels  so  sehr in  Vergessenheit,  daß  man  ihn  mit  dem tk.  dajy  'Oheim  mütterlicherseits'  ver- wechselte. Frz.  dey,  ndl.  deg,  dtsch. Dey.  [Dozy  Oost  33.  Devic  DEt  33. MWiD  71  (umgekehrt  dargestellt  wie hier!).
(end)
=== LAT filius/fetus headwords ===
5030:filius employait la forme a apophoniq rederguo (cf. contrecto et con-
20513:filius familias) a du designer 1 1 ensemble des esclavAs et des ser-
21376:femina peut s'eaployer anssi da genre des substantifs, coaae femi¬
21378:fetus ab eius umore. A anssi, coaae dans le fr .male, femelle, diversea
22359:filius, -I a.(voc./i It): fils; filia, -ae f. (dat. abl.pl. fllidbus
69017:feminal) et virginalia n."pudenda muliebria"; virginarius (Pl.);
(end)
```


## [2026-09-05T18:33:15.007Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '22359,22400p' LAT.txt",
 "description": "Ernout-Meillet filius article"
}
```


### [2026-09-05T18:33:15.061Z] TOOL RESULT

```
filius, -I a.(voc./i It): fils; filia, -ae f. (dat. abl.pl. fllidbus
ponr 4 viter 1 'aabigult^, cf. Charisins, GLK I 139,13, filiabus .in testa¬
mentis ob discrimen sexus ait Plinius dici consuesse-, 54,10, libertabus
filiabusque, quod iurisperiti instituerunt, ambiguitatis secernendae
gratia): fille. Attest^s Atoutes les ^poques. Ont pris dans la 1 . de
1'figi., et coaae frater, soror, nn sens affectif; filii, A basse £poqne
dans la 1. dn droit et dans la 1. coaanne d^signe d'une aanibre gi n£rale
"les descendants",cf. Thes. VI 757,63 et s., 758 , 75 » Panroaans. M.L.3395,
3303. p Ilius, filia sont apparentes A felSre-, cf. Pl. Ps.433 s.u./elo;
snr 1 'alternance, v.Meillet, Introd?, p.169. Tontefois le noa est
independant dn verbe, et rien n'y rappelle plns dans 1'usage le sens
de "nonrrisson qni tette". C'est le noa dn pbre, et non celni de la
abre, an g^nitif, qni accoapagne le patronyaiqne ponr le preciser.
Le noa de la abre n’est ajonte que dans les titnli etrnsqnes, e.g.
CIL I 3 3033, C. Proeni<us> Titiae nat(usy, dans les d^signations d'es-
claves qni n 1 ont pas de pbre l^gal, et dans les titnli gaulois. La
descendance par la abre n*existe pas l^galeaent; 1'indication des
denx parents dans les noas propres est Igaleaent fort rare, et filius,
quel qn'en soit le sens preaier, eat en rapport avec pater beancoup
plns qu 1 avec mater. La sociate roaaine est fond^e snr le regiae indo-
enropeen dn patriarcat, non dn aatriarcat. V. Funck, ALLG VII 73 et s.
D 4 riv 4 s: filiolus, - la, diainntifs tendres et faailiers, M.L.3303;
v.h.a. fi 1151 ) flliaster, -trl, syn. de prluignus "bean fils", M.L.
3397; flliastra-, et, dans lal.des pbres de 1'figlise, filialis, fllid-
litds, flliatid', cf. anssi M.L.3396 *fllianus.
L'italo-celtiqne a perdu les noas indo - europ£ens dn "fils" (got.
sunus, etc.) et de la "fille" (got . dauhtar, etc.). Ces noas ont iti
reaplac^s par des noas nonveaux, faailiers, on fabriqn^s. C'est ainsi
qne le noa celtique de la "fille" est *enigend "n 4 e dans [la faailie]",
iri. ingen, et le noa irlandais dn "fils" est la forae faailibre *maqqos
(iri. «ac, gim.maqi dans les inscriptione ogaaiqnes). Le lat./tlius
est de la faailie de fecundus, etc.(v. ce aot); il a pass 4 dn sens
de "enfant qn'on elbve" an sens de "fils" parce que le vieux noa avait
disparu par suite de qnelqne interdiction et qn'il fallait le reaplacer
(cf. le groupe slave de diva "jeune fille", ditf "enfant"). Le noa
ne coaporte pas de d 4 riv 4 s anciens. La foraation feminine de filia
est tonte secondaire.
filix, -i.cis f. (forae ancienne; le donblet felix est sans donte
dn A nne dissiailation des-denx i, favoris^e par 1 '^tyaologie popnlaire
qni rapprochait filix de felix, InfSlix, cf. Caper, GLK VII 106,3;
on lit anssi dans les ass. filex, cf. carex; et A basse ^poqne apparait
nne forae filica (refaite snr filicula?), cf. Thes. VI 759 ,35sqq.):
```


## [2026-09-05T18:33:27.274Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'PYEOF'\nimport json, io\np='data/verification/page-123.json'\nd=json.load(open(p,encoding='utf-8'))\ne1=d['entries'][1]\nfor n in e1['nodes']:\n    if n['id']==2:\n        for c in n['consulted']:\n            if c['src']=='LKT':\n                c['where']='LKT.txt entry s.v. dey (line 1209)'\n                c['stance']='partial'\n                c['note']=\"Lokotsch has no article for the kinship term itself, but s.v. dey he records the Turkish word: '... daß man ihn mit dem tk. dajy „Oheim mütterlicherseits“ verwechselte' — i.e. Turkish dayı 'maternal uncle' is a well-attested Turkic word; the loan direction into Persian rests on Doerfer §1176 and Hasandust II 1264.\"\n    if n['id']==6:\n        for c in n['consulted']:\n            if c['src']=='LAT':\n                c['where']='Ernout-Meillet s.v. filius (LAT.txt line 22359 ff.)'\n                c['stance']='supports'\n                c['note']=\"'filius, filia sont apparentés à felāre; cf. Pl. Ps.433 s.u. felo ... Le lat. filius est de la famille de fecundus, etc.' — Ernout-Meillet keep filius with the fē-/'suckle' family, against Watkins's hesitation; they add that 'rien n'y rappelle plus dans l'usage le sens de „nourrisson qui tette“'.\"\njson.dump(d,io.open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nprint('patched')\nPYEOF\npython3 -m json.tool data/verification/page-123.json > /dev/null && python3 tools/verify_check.py 123",
 "description": "Patch two consulted notes and re-check"
}
```


### [2026-09-05T18:33:29.156Z] TOOL RESULT

```
patched
nodes verified: 13/13
node verdicts: {'confirmed': 8, 'disputed': 4, 'plausible': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'partial': 4, 'not_checked': 3, 'contradicts': 2}
books consulted: {'supports': 28, 'contradicts': 5, 'silent': 5, 'partial': 4} | by book: {'KLN': 6, 'BRT': 4, 'POK': 4, 'ARY': 4, 'AHD': 4, 'HRN': 4, 'PHD': 3, 'KNT': 2, 'CHEUNG': 2, 'LAT': 2, 'HUB': 1, 'IEC': 1, 'SYN': 1, 'WLD': 1, 'MON': 1, 'LKT': 1, 'SOD': 1}
```


## [2026-09-05T18:33:45.653Z] AGENT

Page 123 (book p. 93) verified: 2 entries, 13 nodes. File written to `/home/sfmqrb/git/rishe/data/verification/page-123.json`; `verify_check.py 123` reports 13/13 nodes, 0 PROBLEM lines.

Verdicts: roots 2 confirmed · nodes 8 confirmed, 1 plausible, 4 disputed. Ref checks: 8 supports, 4 partial, 2 contradicts, 3 not_checked (nodes with `refs=None`).

Disputed / flagged:
- **Dhars → Persian `dorošt` «درشت»** — Horn 552 (+Nöldeke) backs Nourai, but Hübschmann PS 552/p.61 rejects it phonologically (`*dr̥šta-` would give NP *dišt; the word needs Iran. *družta-), and POK:216, ARY p.273 file it under *deru- 'firm' as a doublet of *durust* — the chart's own note is right.
- **Dhē → Persian `dâyi` «دایی» 'mother's brother'** — Turkic loan (Proto-Turkic *tāy/*dāj; Doerfer I §1176 p.196, Hasandust II p.1264). دایه is fine; دایی does not belong. Nourai's own HRN:119/BQT:822 do not support it.
- **Dhē → Av./OP `dânô; danâxe` 'grain'** — POK:242, the very page cited, *excludes* the grain word from this root ("dazu aber nicht *dhōnā- „Getreide“"); modern reconstruction PIE *dʰoHnéh₂. Also a transcription problem: `danâxe` is Greek δανάκη (danákē), an Old Persian coin = 1/6 drachm (Horn 536; BQT 820 "پارسی باستان (بنقل یونانی)"), **not** 'grain' — the printed page shows "danâxe : grain", so `error_in: "book"` (page PNG saved to `data/verification/sources/refs/ocr/BOOK/123.png`).
- **Dhē → Sogdian `d`n; d`yh`** — SOD:136 itself derives δ'yh 'slave girl' from *dāhi / Skt dāsī, not from the 'suckle' root; δ'n belongs to the excluded grain word.

Extraction errors: **none** — the JSON matches the printed page exactly (checked against the rendered image), including "danâxe", "dâyě «دایی»" and "fě-tus".
