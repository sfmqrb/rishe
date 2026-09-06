# Verification process log — verify-page-238


## [2026-09-06T15:41:52.742Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 238 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-238.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-238.json. Write /home/sfmqrb/git/rishe/data/verification/page-238.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 238` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:41:54.639Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:41:55.394Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:41:55.410Z] TOOL RESULT

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


## [2026-09-06T15:41:55.523Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-238.txt"
}
```


### [2026-09-06T15:41:55.546Z] TOOL RESULT

```
1	=== PDF page 238 (book page 208) ===
2	--- entry 0 ---
3	ROOT Kamer -> redirect to Kam 2
4	--- entry 1 ---
5	ROOT [Indo-European] Kamma, Quômn, Sqombh-no : little, small  (refs WLD:601; IEC:1044)
6	#1 (parent #0) [Avestan / Old Persian] refs=WLD:601; KNT:179; IEC:1044 | kamna, kamnô : little
7	  #2 (parent #1) [Persian] refs=BQT:1689 | kam «کم» : little ; kamîn «کمین» : least | extra: کمینه
8	--- entry 2 ---
9	ROOT Kamp -> redirect to Kam 2
10	
```


## [2026-09-06T15:41:58.151Z] AGENT

Small page: one real entry with 2 nodes. Let me look at the source JSON and reference infrastructure.


## [2026-09-06T15:41:59.556Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-238.json | head -120",
 "description": "Show source JSON for page 238"
}
```


### [2026-09-06T15:42:01.342Z] TOOL RESULT

```
{
    "pdf_page": 238,
    "book_page": 208,
    "entries": [
        {
            "root": {
                "name": "Kamer",
                "redirect": "Kam 2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Kamma, Qu\u00f4mn, Sqombh-no",
                "lang": "Indo-European",
                "refs": "WLD:601; IEC:1044",
                "gloss": "little, small"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "WLD:601; KNT:179; IEC:1044",
                    "words": [
                        {
                            "translit": "kamna, kamn\u00f4",
                            "gloss": "little",
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
                    "refs": "BQT:1689",
                    "words": [
                        {
                            "translit": "kam",
                            "gloss": "little",
                            "script": "\u06a9\u0645"
                        },
                        {
                            "translit": "kam\u00een",
                            "gloss": "least",
                            "script": "\u06a9\u0645\u06cc\u0646"
                        }
                    ],
                    "script_extra": "\u06a9\u0645\u06cc\u0646\u0647",
                    "note": null,
                    "quote": {
                        "text": "\u0628\u06af\u0630\u0627\u0631 \u06a9\u0647 \u0628\u0646\u062f\u0647\u0654 \u06a9\u0645\u06cc\u0646\u0645 - \u062a\u0627 \u062f\u0631 \u0635\u0641 \u0628\u0646\u062f\u06af\u0627\u0646 \u0646\u0634\u06cc\u0646\u0645",
                        "poet": "Sa`d\u00ee"
                    }
                }
            ]
        },
        {
            "root": {
                "name": "Kamp",
                "redirect": "Kam 2"
            },
            "nodes": []
        }
    ]
}
```


## [2026-09-06T15:42:01.480Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['WLD','IEC','KNT','BQT','POK','AHD','HRN','HUB','PHD','NYB','BRT','MON','ARY','SYN','CHEUNG']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-06T15:42:04.208Z] TOOL RESULT

```
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
CHEUNG null
```


## [2026-09-06T15:42:14.077Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60 && echo \"---\" && ls | wc -l",
 "description": "List local reference files"
}
```


### [2026-09-06T15:42:14.123Z] TOOL RESULT

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
---
95
```


## [2026-09-06T15:42:14.399Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,60p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix head"
}
```


### [2026-09-06T15:42:14.438Z] TOOL RESULT

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
```


## [2026-09-06T15:42:18.453Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'kamna' KNT.txt | head -20",
 "description": "Grep Kent for kamna"
}
```


### [2026-09-06T15:42:18.498Z] TOOL RESULT

```
1379:enclitics: kamnam, jiyamnam, acc. nākam, adam- : q | kim, avakaram-ca-maiy, parwam-ciy. On [n*yà]- ; kama = |kam-ma, see $130. On pIE m, see $67; ^
2044:Inst. Pl. asabára:b$, martiyaibiš, hamigtyaibis, bagaibi, vibaibiš, kamnarbis; Мааа, Sakai- b, Pardavaibis, Mārgavaibiš, Üvjiyaibis; nt. ünaraibiš,
2047:Nt. Nom. Sg. zsacam, dusiyaram, ardatam, darant- yam, aruvastam, dàtam, Sakatam, kartam, visam, kamnam; aec. xsagam, stánam, daraniyam, aru- vastam, kartam, visam, uvdipasiyam, uvaspam, probably casam.
2769:may be used as predicate to any subject:! DB 2.18f кага Parsa шй Майа hya ира mam аһа haw kamnam dha ‘the Persian and Median army which was with me—this was a small thing’; во also DB 1.47 uvaipa saam (referring to Parsam utà Madam ша aniyà dahyàva), DNa 39 ctyakaram aha ava dahyava, DNb 6f avakaram amiy, ОХЬ 27f avā- karam-ca-maiy usiy wa framand, DNb 50 ciyükaram amiy ciyükaram-ca-maiy tonaré. A neu- ter subject may have a masculine substantive as predicate: DNb 11f tya rdstam ava тат kama ‘what is right, that is my desire’.
2804:I. The definite article, properly speaking, is lacking in OP, despite the uses given in the pre- ceding section (ef. Lg. 20.6-8); for kya hyd tya as article function only to attach modifiers to another substantive, or to indicate generic value. Thus we find Ката Parsa utä Мада hya ира mam àha haw kamnam aha ‘the Persian and Median army which was with me, this was a small thing’ (DB 2.181); adam Déarayavaus xidyatiya vazraka ‘I (am) Darius the Great King’ (DB 1.1). It is noticeable
3499:56 máhyà : X : raucabis : 6akatà : dha : ауаба : adam : hada : kamnaibis : martiyaibi
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3614:71 šāyaðiya : pasàva : hauv : Fravarüs : hada : kamnaibi$ : asabāraibiš : amufa : Ra _
3722:40 tà : aha : avađðāšām : hamaranam : kartam 4 : Gdtiy : Dārayavauš : xsāyaði 41 ya : pasáva : hauv : Vahyazdáta : hada : kamnaibis : asabáraibis : a
3749:: fàtiy : Dárayavaus : xšāyaðiya : 70 pasáva : hauv : martzya : һуа : avahy& : kárahyà : mafia : dha : tyam : Va 71 hyazdata : fr&isaya : abiy : Vivánam : hauv : amufa : hada : kamnaib
4979:-ma gsm. for -maty ($198.11); apan*yáka-ma А?За 3; [n"yà |kama for n*yàkam-ma (5130) A’Sa 4. Not kamna-ma DB 2.19, as taken by Tolman.
5250:kamna- ad}. ‘small, few’: Av. kamna-, NPers. käm ($147.11). kamnam nsn. (as pred. sb. $259) DB 2.19. kamnatbis ipm. DB 1.56; 2.2, 71; 3.41, "Af.
```


## [2026-09-06T15:42:19.164Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'kamna\\|kamnō\\|kamno' BRT.txt | head -20",
 "description": "Grep Bartholomae for kamna"
}
```


### [2026-09-06T15:42:19.216Z] TOOL RESULT

```
4841:Beziehung  ist  aus  dem  Zusammenhang  zu  J*«^^'*''  ixivainit  yavaica  yavaäslaica erschliesscn:  yastat  mtzdim  kamna (%A.)\"^^^^  können  sie  nun  und  nunmennehr nsii  däitty}  U  aimii  »niuxiä  (sd.)  «T'pwfe'rt  werden"  V.^.14;  —  yezi  an>hat ditiay.44.iQ,—g3r?zfi  m  a  U  m-ams  »mamU . .  yavamüe  ya  (NSf.)  V.7.75. (sd.)  aAuräY.4'i.  2 i  — na  Tm  vTtpa  a>ri  V.««W>'"-PFP.iumV.^^M.._Pü.:  <y.^=i/i^. tl  mazdänAj.dBm  (sd.)  ^.45.1.  a)vor-l»j.  ay ata- Adj.  (fem.  "AI-)  -  ?  —■.gaatoam ausweisend,  auf  ein  Nomen:  tWii  ts  im  .."^rayam  *iaazdri  iary^ri/a puirä/a  (^.) x/nau/ val/ys (sd.)  ,.  zard^usir^m  Y.^t.'paemainiia  °läca  V.i^.4g. Ii;  — yasta  .  .  tarS.mqsta  yöi  Im  tari.A  P"-  '»■''/'';  ^og  "  "Iso  mm  V.  ay-  (a-ya/a-'.). mainyanta  ..  saofyants  Y.4^.11;  ^0.9  •  j,  a-yapta-  n.:  s.  unter  äyapta-. (ahüm),  45.3  (mahrim);  —  yS  I  (ADm.)  1     KorapA.
5890:•  p.  ""asbäray-  Adj.  'der  auf  einem  Ross reitet,  beritten':  /lauv  . .  iiadä  kamnaibis 'ribil  aiiyavt^  "..  mit  wenigen  Berittenen . ." BM-";  7. 2->,  13-
6657:—  cDimS  . .  huxsa'iira  (sd.)  dagvä  aahari  der  kongruenten  Form  des  Adjektivs  er- Y.  44,20;  —  negirt:  västry3t  vä  . .  yl  scheint  das  Neutr.  im  Sing.;  A)llimAp.: vä  nSii  aahat  väslryl  Y.3i.<).  PPA.:  kär<^  ..hyt^  up3  mäm  äha'' haur  kamnam dr.'gvä  ..  duiazöbä  hqs  ..  ahsmustd (^.)\ .  (sd.)  ähc^  Bh.2  6.  B)im  Aw.(?J:  kl.. 46.  j^;  —  vTa rS  (sd.)  hqs  tat/rS  ..  mruylt  lylxmanyata  ap?r;nlyu  ahmt  n''it  p3r^ Y.4i$.  5;  47-4>  J'-Si  —  ^pö  mä  isttm  nJyu yesi  baväni pjrftiäyu(sd).\t.ip.^zQ)'> apayantä  (sd.)  6jr>xoqm  häitlm  vaahsus  —  aojistanam  asti  aojist>m  tan'istanqm manaiihs  Y._j2.9;  —  a~i:S  hat  vohü  tat  asti  tanHst^m  (näml.  mi^rS)  Yt,  10. !?äda  (sd.)  tvr^zyjtS^ä  ..Y. 3^. 6.  a)  ins-  1411?).  a)  Bei  pluralischem  Subjekt bes.  ein  Partizip;  seine  Verbindung  mit  der  kongruirt  die  Kopula  damit  oder  mit  dem Kopula  dient  zur  Umschreibung,  a)  PPA.,  Praedikat;  B)  im  Aw.:  *imqm  vav..yii PPM.,  PPfA.  und  PFP;  B)  im  Aw.:  auhtn  vSrii:raynyXt?m»m:a'..Y.Q.2T,  — at  *'hudSnao^  isayqs(sd.)  girszdl  kyJm  Y.  mana  zaya  asti  vahist?nt  V.  ig.^.  1)  ein 50,9;  —  al  v^  usiilmli/ ahz'J  (iDPiA.)3'i  Adverb.  A)  !  im  Ap. :  ^aia  mäm  hJma* zastäis  frtmmnä  Y.29.5;  —  vasa'ia  ahi  (sd,)  änJ"  Ti.G.a,.  B)  im  Aw.:  y.i^a Xfayamna  ..*d3ilim  Yt  ly.  15;  —  narim  ..  ka'^aia  K  3s  zaosS  mana  yal  akuraheYt. yl  anhat  . ,  mq'^rfm  pgr^sS  Y.Cf.t;  Yyt.  '9.82;  —  vJdylti^d^  saosy u ya'i:a  hn  asis S0(});  —  h^.'d' ioa  y:i:i7i'7  (sd.)  *asta  Y.   awA«/ V.4Ä9;    —    franhapi^    hvS   nSit
11082:(yascd),  V,?.  70,  ij.4  (ymca);  —  iäsca imä  nämSnJs  "so  lauten  die  Namen" Vt  /.  15;  75.  49;  —  Hsca  caraitis  ahi yqm  ..  H.2.  io(?).  Anhang.  Ellipse ist  anzunehmen  für  gAw.:  vaidä  tat  ya ahmT  .  ,  anales  (sd)  tna  kamnafsva  (sd.) hyatlä  iamnänä  (sd.)  ahmT  "ich  weiss  das, weshalb  ich  , .  nichts  vermag;  nur  wenig Herden  sind  mein,  (deshalb  ist  es  so) und  weil  ich  nur  wenig  Leute  habe"  Y. 46. 2.  C)  In  der  Bedeutung  unsres 'auch';  ca  folgt  dem  angeknüpften  Satz- teil, bz.  dessen  erstem  Wort.  B)im  Aw.; 'auch'  hat  den  Sinn  von  i)  'ebenso,  eben- falls, nicht  minder' :  ^<«ji  mi^r>m..yazai vasram  .  .  yasäi  Aojoörpmi^a  yat  attt  . . Yt  6'.  5;  —  mai  vi  padäis{si.)  . .  paiti- fasai  .  ■  al  va  aridrahyala  n>manha  at vi  ..  AunarptatäY-SO.S;  —  tara^uänm ..hyathei  Im  caratasca{Sf.$(>$M.)aodiir?f^ä sSiS?na  vazä  V.jr.ia.  a)  Ellipse  liegt  vor in  gAw.:  vahiSta  tstii' {sA)  , .  tara%usttake .  .  yezT  hsi  dat  ayaptä  . .  ahurö . .  hvaivhf- vlm  (sd)  yaZcä  hsi  dabm  .  .  ". .  des  Z.: dass  ihm  nämlich  AA. ..  die  Herrlichkeiten verleihen  wird  . .  (So)  auch  denen,  die . ." Y,  $3.  I.  a)    'überdies,    ausserdem':
12388:<tffi2xii/n  Bh.f.  14*.  a)  dem  Substantiv geht  'ava-  voraus  (Sp.  105  o.):  avam  gau- mätam  'yam  magum  Bh.  1. 13';  —  avam karam  'yam  madam  Bh.2.6;  6— 11*,  14, ,?■  't  3;  — ■  ävam  käram  'yam  babiraurt Bh.j.  14;  —  avam  käram  'yam  vah- yazdatakyä  Bh.  J.  6,  7.  III)  als  zurück- weisendes Demonstrativum '' :  /ravartii hadä  kamnaibis  *asbäribis  .  .  asiyav^ fasavc^  adam  käram  fraiiayam  'yai{s^ Ait]ii.)paliy  ".  .  drauf  Üess  ich  ein  Heer gegen  sie  marschiren"  Bh.  2. 1 3 ;  —  hauv kadä  kamnaibii  *asbSribis  aiiyavi^  .  , pasäv<^  vivant^  hadä  kärä  nipadiy  (sd.) "yaiy  (als  Akk.)  aliyavt^  Bh.  ^.  1 1 .  a)  mit folg.  *Hy(^kara-  (sd.)  'wenig  zahlreich': *yadipatiy  *mamyähay  'yJ*  Hyt^karam *ava  dahyävJ'  . .  D.6. 4.  ASn.  tyO* als  Konjn.  sbes.         Vgl  zu.  kya-.
19428:•  g.  "ma-  Adj.  (fem.  mä-)  'mein,  memig"; a)  attrib.:  »»?  (KSm.)  urva  ^s7ä  azya (sd.)  Y.2g.t,;44.B;  —  kj  mS  nä  '^rätä vistS  Y.  50. 1 ;  —  makmai  hyätä  *avaAhl ^■50.  7;  —  tä  «tSj  *mainySul  maAys  .  . g3rm{sA.)  Y.^S.9;  —  AizvB  rai^lm  (sd.) stsi  makya  Y.50. 6;  —  vahistä  mahyh is'IBii  Y.46.1S;  50.9,  44-io;  —  mahmi manSi  (sd.)  Y.  J2.  i ;  —  inai^ä  (sd.)  mayä (ISf.)  Y.j^.9.  b)  pracdik.:  »«i(NPn.) kamnafhä  (sd.)  Y.  4Ö.  2.  [Y.  ^.  1 2 :  lies ali>mahyä^
21237:(sd.)  dngvanhm  avS  Y.32, 14;  —  täis  zl nä  /yao^anai/dyentf(sd.)..Ay  ('insofern') as  *aojS.  näidyankifn  (sd.)  Y.^J^.  8;  — vaidä  tal  ya  aAml . .  anaisö  tnä  kamna/svä hyatcä  (Sp.  574  o.)  kamnäna  aAmX  Y. 46.3;  —  parstim  zl  %wa  yohanä  tat )mavatqm{sA.)  Ay  {'■<Nt)[')%wä  x^ayqs{5i) alitm  dyat  imavantim  Y.43, 10.  b)  im jAw.:  atcit  bä  lumS  Aaomai  y'  ('weil') vupe  anye  tnatävAs  ailma  Aacinte  Yt  //.  5 ; Y,  /0. 1 3 ;  —  avat  vayul  ba  nqma  aAmi y  »va  dqma  vayemi  Yt  i^.  43;  43f-^;  — aojists . .  y  dim  upanAacat . .  Aqm.vanitts Yt/p.  38f.;  —  aom  ofarmB  AangSurva- yata  . .  ^raltaond .  .y  as . .  vftT^ravastTtnB Yt/5.36;  38;  —  bawraini  vasfrä  vajtAata ,,y  asti  bawris{sd.)  sraiita  Yt.5. 129;  — wn'^rayriB  ..  nBil ..  yanyB  (sd.)  vaAmyB .. y  nürjm  .  ,  dafvayäsS  voAunim  va  taca- yänti  . .  Yt  J^  54;  —  ^banhvB  va  patU vajaanaAe  .  .  y  alta%a  *Aanjastlnte  pouru gaonaAe  (sd.)  u%aheca  N.  65.  IV)  die Folge  oder  den  Zweck  angebend  'so  dass; auf  dass,  damit';  a)  im  gAw.;  1)  mit dem  Praeteritum;  Ayatis.!!!)  ji 3.dibaomä (sd.)  .  .  upa.jasat  Ay  ('so  dass')  vtrstmtä (sd.)    aciitim    manB   Y. 30.(1.  2)    mit
28520:—  adam  babirum  asiyavam  Bh. /.  19,  18, 2. 1 ;  1 3 ;  —  vahyazdäti^  hadä  kamnaibis *asb3raibis  amu^t/'  aHyavJ'  *pisiyä^uv3- däm  Bh.5. 7.  a)  Adv,  statt  Akk.:  fra- variis  . .  amuh<^  rag!  nämä"  dahyäul  .  . avadä  asiyavJ'  Bh.  2.  13.  b)  abiy und  Akk,,  uzw.  a)  'nach  .  .':  ^vfda*' famä  ..  asiyavc^  abiy  bsbirum  Bh.j.  14; 2. 1,  J.  4.  ß)  'gegen  — ',  in  feindlichem Sinn:  adam  bäbirum  (s.  a)  asiyavam  abiy avam  nadi"iabairam  Bh.  i.  !&.  2 )  "über- gehen zu  -,  Jemands  Partei  ergreifen',  mit abiy  und  Akk.:  iura*  .  .  iami'är''iyi^  (sd.) abara"  haca  ka'bajiyä''  abiy  avam  asiyavt^ Bh.7.11;  16,  2.5,  _j.  s,  13;  —  "uvajiyä hamih'^iya  abava"  abiy  avam  äh''inam aSiyava'  Bh.  /.  16. 1  3)  'an  etwas  (Akk.) herangehen,  (eine  Angelegenheit)  betreiben' : arfhä  (sd.)  ta  yä  voha  fyaväi  manaaßiä ^■33-  8.  4)  'verfahren  gegen  -'  (Akk.): ya  /«»<«■/? (3PPM.)W  adrSngisd.)  jriivänhB y.2g.  3.  5)  'handeln,  tun':  s.  Inf.  syao- ^anäi.  6)  'weggehen,  weichen  von  — ', mit  kaäi  und  Abi.:  i^armO  apammata.. /usal    ifarmB   yimal    haca    .  .    mtrrjake
28714:—  insbesondere  zur  Wiederaufnahme  des Subjekts,  das  sammt  Zubeliör  unmittel- bar vorausgeht^:  /  marliyt^  i^i^Vtaxma" näma"  asagartiyc^  hauvmaiy  hamii^iya'' abav^  Bh.  2.  14;  —  /  martiya''  araxa'' nama!'  arminiya''  haldüahya  pu^'a*  hauv udapatatä  Bh.,;.  13;  —  vistäspf^  tnatiä pita  hauv  paT^avaiy  ah<^  Bh,  2.  lö;  — dSrayJ'vt^us  xiäya%iya''  hyc^  manä  pitil hauv  .  .  vasiy  ty<^  naibam  akunaus  X. 7.  3;  D.  4-  ';  —  margui  näma"  dahyäus hauv(fem.)maiy  haHtiyä  abava^  Bh.j.3; 5, 1 ;  —  hya^  du7'aistam  nyäii/  axiatä  (sd.) Äau[fem.}ay  J'urä  nirasätiy  D.5.3J  — hauv  vahyazdätJ'  hyi^  bardiyJ'  agaubatä hauv  käram  fräisayi^  Bh.^.  9;  11;  — käri^  pänJ^  utä  mäda''  Afn*  upä  niilm äh<^  hauv  kamnam  äha^  Bh.  2.  6;l(  — ar^aia  vJptS  arsala  vaipayB  .  .  hau  asti daSi-B  hau*"  .  .  V,  <?.  33.  b)  auf  ein Relativum  als  dessen  Korrelat:  \hy(^ madaisuvä  mäkilt<^  äha*  hauv  *adakly naiy  adäraya''  Bh.  2.6;  —  hyä  J'ura''- mazdähc^  Jramiinä  hauv(ieai.)taiy  gas/ä mä  ^adaya^  D.  6. 6.  II  »)  auf  den  Inhalt eines  Satzes;  in  Kongruenz  mit  dem  (ge dachten)  Praedikat:  kä  hl  asti  n^a?  .  . panca  sota  upäxananam  upäisit  hau  (fem.) Jaiäus  hau  vTsäus  häu^ . .  hau  vispanqm . .  spaci^ranqm  anya  udra  upapa  ". .  das  (ist auch   die  Strafe  für  die  Verletzung)  des
```


## [2026-09-06T15:42:25.923Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"kamna- ad}\")\nif i<0: i=t.find(\"kamna- ad\")\nleaf=t.count('\\f',0,i)\nprint('leaf(0-based)',leaf,'=> printed approx',leaf-15, leaf-13)\nprint(repr(t[i-1500:i+700]))\nEOF",
 "description": "Locate Kent kamna page"
}
```


### [2026-09-06T15:42:27.575Z] TOOL RESULT

```
leaf(0-based) 201 => printed approx 186 188
'ddn ‘heap up’ from ava-kan- (Dv. Gr. $184; Morgenstierne, Acta Or. 1.249; Hz. ApI 225).\nava- + kan- ‘put down on, place on’: avakanam Ist sg. imf. (8213, 5226.1) DB 1.86.\nKa™pa"da- (8111) sb. ‘Kampanda’, a district in Media (cf. Kónig, RuID 71): Elam. qa-um-pan- taš, Akk. ha-am-ba-mu. Kapada пет. DB 2.27.\nkapautaka- adj. ‘blue’, in kdsaka hya kapau- |\ntaka ‘lapis lazuli’: deriv. ($146.11) of stem in РЫ. — | kapót, NPers. kabod ‘gray-blue’, Skt. kapóta- ‘pigeon, pigeon-color, gray’ (Scheil 21.29; Bv. BSLP 30.1.61; Konig, Burgbau 62; Bleichsteiner, WZKM 37.94-101; Wb. AfOF 7.42, cf. PW 10.1887 s.v. Караша; Hz. AMI 3.64-5). kapau- taka nsm. DSf 37.\nKäpišakāni- sb. ‘Kapishakani’, a fortress in Arachosia ($117, $126): Elam. qa-ap-pi-i3-fa-qa- nui, Каракат ns. DB 3.608.\nKa"büjiya- sb. ‘Cambyses’, (1) father of Cyrus the Great; (2) son of. Cyrus the Great, king of Persia before-Dartus: Elam. kan-bu-si-ia, АКК.\nLEXICON\nkam-bu-ai-ia, Gk. KayBvons (8111, $144.IV): ety- mology disputed (cf. Bthl. AiW 437; Charpentier, ZII 2.140-52). Kabūjiya nsm. DB 1.28, 30f, 31, 32, 33, 43. Kabijiyam asm. DB 1.45, 46. Kabüyyahyà gsm. CMb 1f; DB 1.29, 30, 39. Kabūjiyāä absm. DB 1.40.\nkam- vb. ‘like’, see amazamata, if for (h)- amaxmatd. See also kama-, and possibly canah-.\nkáma- sb. ‘wish, desire’: Av. Skt. kdma- (§126, $148.I, V, VI). See also kam-. For syntax of de- pendent acc., $249.T, JAOS 66.44-9. kama nsm. DB 4.35f; 5.17°, 29, 33°; DNa 38; DNb 8, 10, 12, 19, 20, 27; DSf 16; DZe 12°. ХРЇ 22, 30.\nkamna- ad}. ‘small, few’: Av. kamna-, NPers. käm ($147.11). kamnam nsn. (as pred. sb. $259) DB 2.19. kamnatbis ipm. DB 1.56; 2.2, 71; 3.41, "Af.\nkar- vb. ‘do, make, build’: Av. kar-, pres.\nkaronaoitt, Skt. kr-, pres. krndti karóti (809, $122, $132.2, 5182.3). See also akarta-, ucára-, kara-, dastakarta-, duskarta-, hakarta-.\nkunautiy (866.1, $70, $99, $2101) DNb 24f; DSs 2°, 3f, 4, 6°. |\nakunavam ($66.1) 184 sg. imf. DB 1.62, 63, 68, 12, 87; 2.20, 76, 83, 91; 3.31f, 52, 85; 4.3f, 6, 86°, 40, 41, 45, 59, 60, 65, 89; 5.2, 8f, 17, 29, 33; DNa 491, 51; DNb 48f; DSa 4, 5; 284 3°; DSe 32, 34, 45, 49; DSf 21, 22 bis; D8g 3^; DSi 4^; ре] 2°, 3, 3f°, 4; D8o 2°, 4; XPa 13, 14; XPb 27; XPd 17; ХРЇ 37f,'
```


## [2026-09-06T15:42:37.510Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (198,199,200,201,202,203):\n    p=t[n]\n    print('=== idx',n,'len',len(p))\n    print(p[:200].replace('\\n',' | '))\n    print('...TAIL:',p[-200:].replace('\\n',' | '))\nEOF",
 "description": "Inspect KNT leaves around kamna"
}
```


### [2026-09-06T15:42:39.232Z] TOOL RESULT

```
=== idx 198 len 3579
DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43, 45; XPf 19f; XPh BAL. | щй AsH 13; DB 1.34 bis, 34f, 41 ter, 46 bis, 47, 57, 67, 77, 85; 2.3, 4, 18, 74 ter, 77, 81f, 87, 88, 89, 92; 3.30, 
...TAIL: ymology un. | | certain, probably a popular etymologizing in OP of a local non-Iranian name, cf. Bthl. AiW 1830; Fick, ВВ 24.310; Justi, ТЕА 17.116; Tm. Lex. 77, Ufrätwā ism. DB 1.92 (not gen., as taken
=== idx 199 len 3923
 by Hz, ApI 71-2). | ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.
...TAIL: ! 216-9; W. Hinz, Altpers. Wortschatz 141. Not to be taken with W. Schulze, РАЖ 1912.685-703, 1918.331- 2, as ‘by a natural death’, citing semantic par- allels in other languages; who is followed by M
=== idx 200 len 3905
B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vriddhied), and by H. H. Schacder, Nachrich- ten d. Ak. d. Wiss. in Gottingen, phil.-hist. Kl. 19046-7.24-30. wdmarsiyus nsm. DB 143. | Uvárazmi-
...TAIL: .37; 3.44; DSf 31. | OLD PERSIAN | ka"ta- pte. as sb. (8276. TII) ‘excavation’: pAr, « 7 с *knta-, to 'kan-, with restored n ($242.11) agin с Samar-kand, wherein -kand has been transferred from the ditch 
=== idx 201 len 4054
to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54-5, Ар! 224). katam nsn. DSf 25. | Katpatuka- sb. ‘Cappadocia’, a province of the Persian Empire; also, as adj., ‘Cappadocian’: Elam. ga-at-ba
...TAIL: 10) DSf 50°, 51, 53. | акитӣ lst pl. aor. ($218.IT, $230.1T) DB 1.90, 94, 96; 2.68, 70; XPa 17; ХРЇ 43. | akunava"tà 3d pl. imf. mid. (§210.1, $236.IT) DB | 179 | 3.12; 5.6; DSf 48 (Hz. ApI 229-30 takes as fr
=== idx 202 len 3912
om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2). | акша aor. mid. ($66.1, §218.11, §235.11) CMb 4; DB 1.47. | akunavayalà imf. pass. (§220, $235.IT) DB 1.20, 24. | akariya imf. pass. (585.1, §99, $220) DSf 3
...TAIL: D; Lg. 19.227-9; not ndm.) Wal. karíayá lsm. (§251C; Lg. 19.227-9; not npm.) We 1; Wd 1. | kasaka- sb. ‘semi-precious stone’; Elam. ga- st-ga causes König and Wb. to write kás'ka, but this is not warran
=== idx 203 len 4207
ted by the OP writing. регу. of Iran. root *kas- (89.V, §87, $126, §146.II), = Skt. kaś- ‘be visible, appear, shine’ (so König, Burgbau 61; not to Skt. Ёйс@- ‘crystal, quartz’, despite Bv. BSLP 30.1.6
...TAIL:  CMb 1°; CMe^; DB 1.1 bis, 2 bis, 4, 6, 9, 11, 12, 13, 14, 18, 21, 24, 27, 277f, 29, 35, 44, 48 bis, 60, 61, 71f, 72, 78, 75, 76, 81f, 83, 90f; 2.1, 5f, 8, 11, 11°, 14, 17°, 18, 29, 37, 48, 49, 91, 64
```


## [2026-09-06T15:42:50.314Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC kamna/qomn/skombh ==\" && grep -n -i 'kamna\\|qomn\\|sqombh\\|skombh' IEC.txt | head -20",
 "description": "Grep Mann IEC"
}
```


### [2026-09-06T15:42:50.365Z] TOOL RESULT

```
== IEC kamna/qomn/skombh ==
14179:Av. kamno, adj. ‘puny, trivial, bad: Ober, kamna-, adj. ‘small, few’; Per. cf. kamin, ka- mine, adj. (mean, base’ cf. kam ‘few, less, lacking’; OE hwon (variant: “little, few’); (iso- phonic in Arm. omn “one, some?)
```


## [2026-09-06T15:42:51.894Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== POK ==\" && grep -n -i 'kamna' POK_full.txt POK_01.txt POK_02.txt POK_03.txt | head -20; echo \"== WLD ==\"; grep -n -i 'kamna' WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt 2>/dev/null | head -20",
 "description": "Grep Pokorny and Walde-Pokorny"
}
```


### [2026-09-06T15:42:51.984Z] TOOL RESULT

```
== POK ==
POK_full.txt:45691:Material: Old Indie kamna-^ young ', compounds Sup. kanlyas-, kanistha-, kanistha-, 
== WLD ==
incoming/WLD/WLD_Bd1_pages.txt:79716:Z. idg. Sprachgesch. 32 zu av. kambistsm „am vrenigsten", kamna- „wenig,
incoming/WLD/WLD_Bd2_pages.txt:39917:      Av. ap. kamna- „wenig, goring^ {^kamhhna-^          Super!, av. kambistdm
```


## [2026-09-06T15:42:58.502Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39890,39960p' incoming/WLD/WLD_Bd2_pages.txt && echo \"=== pdf page tag ===\" && awk 'NR<=39960 && /\\[pdf page/ {last=$0; n=NR} END{}' incoming/WLD/WLD_Bd2_pages.txt; grep -n '\\[pdf page' incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1<39960' | tail -3",
 "description": "Read WLD Bd2 kamna context and page tag"
}
```


### [2026-09-06T15:43:00.304Z] TOOL RESULT

```
    air.   (dehnstuhg) scdth „Schatten”, mcymr. cy-scaicd^ ncymr. cy-sgod^ acorn.
scod^ bret. squeut ds.
    got. skadus „Pinstemis, Dunkel”, ahd. scaiOj -awes „Schatten”, ags. sceadu
ds.,   norw. skodde „^Iebel”.
    Weitere Anknupfung ans^a[i]- „gedampft schimmern, Schatten”             ist gr.

o   im Wege {*ska-        :    sk-et-j -o^-??).

    Ygl. Curtius 168,          Fickl^ 566, 11^ 308, III^ 449.
    Alb. kot jjDunkelheit, Kacht” wiirde nicht blo6 eine       Form ohne anl. s-,
sondem auch mit                 fordem und bleibt besser fern (s. G. Meyer Wb.
                               idg. e
202).       Ebenso ai. cafati „ver8teckt u. dgl.” (Schulze KZ. 27, 426 beruft sich
auf oxoTo/utjviog    :   ai.
                                                    ;




                                               sqom-    — (s)qut-                                 601

    sqom- „seufzen, einen schwachen Laut von sich geben'^
         Gr. oxofi^Qioar yoyyvoai Hes.
         abg. skomljq^ skomati „gemere‘^, skomljati „gninnire“, cech. sk(yinliti^ poln.
    skomlic „winseln“         (u. dgl.,   s.   Miklosich EWb, 301).          Prellwitz^ 419.

    (s)qombh-no- {^sqaml)li-7io-l s. u.) „verkurzt, kurz, verstiimmelt, wemg‘‘.
      Av. ap. kamna- „wenig, goring^ {^kamhhna-^          Super!, av. kambistdm
•   „am wenigsten“; ahd. hammer „Yerstiiinmelt“ mit s- aisl, skammr „kurz“,
                                                                    ;


    ahd. scam(mer)^ skemmi „kurz“ {germ. Zubehor z. B. bei Falk-Torp u. skjemt^
    skjcemrne; ahd. scama „Scham‘' usw., Grienberger Unt. 187f., Falk-Torp
    u. skam zw., bleibt fern; unannehmbare Analyse von scamma- unter Verb,
    mit wgrm. skepa- „Schaf^‘ bei Schroder ZfdA. 42, 69),                         Ygl. Zup. G. 108,
    152,      BthLWb. 440.
      Nicht hierher gehoren (Fick 11^ 308) mir. seaman „Ievis“, cymr. ysgafn,
                                                           wozu mir. seaman^
    bret. skahv, corn, scajf ds., acymr. scamnhegint „Ievant^',
    cymr. ysgyfaint^ acorn, sceuens, bret. skevent „Lunge“; die kelt. Forraen
    setzen einfaches ni und nicht mi voraus; auch miifiten die brit. Lungen-
    namen (auch nir. sgamhdn, sgamhog „Lunge“) analogischen Suffixtausch er-
    fahren haben, s. Pedersen KG. I 76, 168. Die kelt. Worte wiesen auf idg.
    -am- als Vokalismus.         — Gegen Vergleich von              av. kambisbm    mit gr. diep^oy
    8.   u. dhebJi-   „beschadigen“.


    sqordho-, -a- „Pfanne, Scherbe“?
         Ahd.    scart-tsarn,    mhd.      scharf,      scharte   „eiserne   Pfanne“,'   ags.   sceard
    „Scherbe‘';       skrada „Tiegel, Pfanne, Herd“ (auch skvrada, skovrada^
                      aksl.
    poln. skowroda^ russ. skovorodd  v kann von slav. sheer- „schmelzen'‘, aksl.
                                                ;



    raskvhrq usw., s. Mikl. EWb. 305, iibernommen sein) lett. skeirds, skeirde;


    „Bl®ch, Wei6blech“ hat, wenn zugehorig, seine Bed. vielleicht aus „Scherbe
    (scharf und dunn)“ entwickelt,
         J.   Schmidt Yok. 11 136, Kluge s. v. (^385), Zup. G. 152.

    (8)qut- „rutteln“.
         Lit. kidh^                     kustu und kuntu^ hutau^ kusti „sich auf-
                       kiiteti „aufrutteln‘‘,

    riitteln, sich            kutrus „hurtig‘^, kuid „Quaste, Frans e“ (lett. kutet^
                       erholen“,
    kutinai „kitzeln“?? Leskien Abl, 317), nach Zupitza Gutt. 121 zu:
=== pdf page tag ===
```


## [2026-09-06T15:43:09.503Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14160,14200p' IEC.txt && echo \"=== leaf ===\" && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Av. kamno, adj')\nprint('leaf0',t.count('\\f',0,i))\nEOF",
 "description": "Read Mann IEC context"
}
```


### [2026-09-06T15:43:11.505Z] TOOL RESULT

```
quolos, -es- “turning, turn, wheel, axis, centre, community'. WP I, 515 and cf. I, 464. Cf. quol- extns. and queló Arm. cf. olor, Let, (twist, curl", fr. *quolesi-); Myc. -qoro-; Gk. pólos, m. 'axis, globe, dial, round chaplet’; cf. oneiro-pólos ‘interpreter of dreams; Alb. cf. kalla- in kalla-tumba *head- over-heels'; Thrac. cf. kól-abros ‘a dance’ be- side koléa, id. (if fr. *quoleso. Hes.); Lat. colus gs: -1, and -üs, f. 'spinning-wheeP" beside in-
1043
cola ('inhabitant'. Ambig. cf. kol-?); ON hváll, m. ‘hill, knoll’; Sw. hval ‘group of SOT: OCS (and com. Sl.) kolo, gs: -ese, n. ‘wheel’; Latv. cf. at-kal ‘again’. Long gde. in Skt. kaláh, m. ‘fixed point, time, period? and perhaps Gk. póle, f. ‘sale’ (value of Gk. p- uncertain) (Bois. & Hof. untenable)
quolpos (1) ‘hollow, bend, vault, arch’. Cf. quelp-, qulp-. WP I, 473 OE hwealf, adj. ‘hollow, arched’; s. ‘vault of sky; OHG cf. hwalbon, v. “arch, bend’; gi- hwelbi, n. “arch, vault'; Du. cf. welf-boog, id.; OS bi-hwelbian, v. as OHG; G (w. labial modi- fication) wólben, Ge-wólbe; MHG welben, tr. as OHG (but for welwen see uoluó, iô); EME to whelve, v. ‘to cover’; Finn. (LW fr. Gmc.) holvi ‘vault’; Li. kálpa, f. ‘thwart on sled, fet- lock; thong'; ON hválf, Sw. hvalf, n. as OE
(quolpos (2), see qulp-. Evidence ambig. Prob. an extn. of (1) in sense of ‘wrong, harm’. Uncertain references are Oss. káráf ‘greedy; greed’; MIr. col. n. ‘sin, blame’, but cf. W cwl, pl. -ion, m. (2) ‘fault’; Tokh. A karyap, B karep ‘harm’ not here since Tokh. preserves IE *1; Lat. culpa ‘blame’ is ambig. fr. *qulpa or fr. *quolpa)
quolt- (quelt-, quolət-) ‘turn, bend, curve’. See quel-, quol- and extns. Skt. katah, m. (2) “hip, waist, small of the back’; katih, f. “hip, buttock’; Gk. (e-gde) tél- son, n. *baulk, plough-turn of field’; Cz. cf. kolot, m. (‘rotation’, fr. *quolot-); Hätt se (2) “bend”; Ukr. kolotyty, v. ‘stir, mix’; (E-gde in) Li. kélta, f. (*ferry'. Initial ambig. cf. kel-)
(quoluolos, quoruolos (?) Skt. ambig. Cf. either quol- w. extns. or quor-, quor-quol-, quort-, etc. Thus only in Skt. kárvarah 'varie- gated'. See quoruol- as a possible variant of quorquel- (2)
quom, particle, adv. & cj. Cf. quam. (Indo- Iran., Alb. Slav. & Bait. ambig.) WP I, 519. Acc. sg. of type quos, q.v. in some instances. Dat. sg. in Baltic Vedic. Skt. kvà; kva *where; in which'; OPer. kan if; Oss. kàm, kámi, adv. ‘where’; Hiero- Hitt. (queried) kuwan Cu. and”, or sim.); Alb. cf. kë ‘whom’; ka- (in ka-dalé 'slowly?) beside EMAIb. kun *whom', mod. Alb. “anything?
quolpos — quo-né (-no, -n)
10
20
25
30
35
40
45
1044
(z-gde fr. *qum-); OLat. quom, Lat. quum, cum ‘when’; Osc. pún, cj. ‘when, as: (long- gde in) Cz. kam, Srb. kamo ‘whither’; (Go. hwan; OHG hwanne “when? ambig. cf. quam- and extns.); OLi. kám ‘why’; Li. kam “to whom, for whom’ beside kame ‘where’; Latv. kam *to whom; for what; whither'. Extensions in Lat. quum ... tum ...: Go. hwan ..., pan ... Type *quom-de, -dó, -d- (w. some ambiguity, see quam- and extns.) in Ossetic kand. . . nä ‘not only’; Alb. (z-ge) kund, kundi ‘wherever, somewhere, anywhere’ (cf. qum- dhe, etc.); Lat. cf. në-cunde (‘from some- where’, hence unde ‘where’ by “false? divi- sion); OHG hwanta, hwanda ‘why; hence, whence'; OE hwanne, hwonne, hwæne, rel. ‘when’; Fris. hwant, hwent, Du. want, cj. ‘for’; OCS koda, kody, kodu ‘whither’; Pol. kedy, Cz. kudy, R kudà, id. Cf. also Pol. do-kad, Cz. do-kud “as long as’. Type *quomi-quo(i) in Arm. h-umeke (fever'. P'austos, fr. en-^); Lat. cf. -cumque (--ever' in cpds.); Umb. -pumpe, id.; OCS cf. (o) komíko-li (loc. sg. “<... anyone); Cz. (o) komko-li, id. beside kam-ko-l1i “anywhere”
quómn- ‘small; little, few’. Cf. quón-
Av. kamno, adj. ‘puny, trivial, bad: Ober, kamna-, adj. ‘small, few’; Per. cf. kamin, ka- mine, adj. (mean, base’ cf. kam ‘few, less, lacking’; OE hwon (variant: “little, few’); (iso- phonic in Arm. omn “one, some?)
(quomst-, cf. qumstos, kmst-. O-gde only in Li. kamStas, m. ‘throng’; kamštis, gs: -SCio, m. ‘stopper, cork’; cf. kamšyti, v. ‘cram, block": kamsalas, m. ‘filling’; kamša ‘dam’, etc.)
(quondh-, o-gde to quendh- (2). Only in Balt. cf. Li. kándu, kásti ‘bite’; Latv. kožu, kost, id. beside kods ‘lean, thin’; koda ‘moth’. Iso- phonic in Skt. kandharah ‘neck’: Hes. tón- thōn ‘flesh of the back’)
quo-né (-nə, -n), adv. and cj. based on the pron. of type quo-, q.v. Cf. quan-, quam-, w. extns. Ambiguities of vowel in Indo-Iran., Gmc. & Slavo-Balt. Oss. känä or: Olr, con ‘till; that, so that; MIr. cun ‘unto’; W cf. po-na “if not, unless? beside po-ni, id. (fr. *quo-ne); OCS cf. ka -ky in ne-u-ka, ne-u-ky 4s it not that’; Lat. cf. quon-dam, quon-iam,
1045
advs.; Li. (cpds.) kàna- “some-?. Cf. (e-gde) Skt. -čana -soever
quón- (or quăn-. Evidence ambig.) “little’; quonið (or quanio?) ‘belittle’ Skt. cf. kanah ‘small’; Oss. cf. kanäg, kannäg, dim. type, id.; OE hwōn, adj. & adv. id. (Iso- phones: Ir. cáinim, v. ‘abuse’; Cz. kanit ‘daub, mess’)
quonos ‘effort, deed, achievement. Cf. queno (1) and konos (1). (Initial, IE *k- or *-qu-, ambig. in Indo-Iran., Ir. & Balto-Slav. Gk. probably here despite p- in pénomai “I toil"). Cf. WP II, 661 OPer. kan- ‘put, get, ava-^ ‘put down’; ni-? “destroy”; Av. kan-, v. (?) ‘beg’; Gk. pónos, m. ‘toil’; Olr. cf. fo-chonn, m. ('cause', fr. *upo- quon-or *-kon-); R kon, m. ‘turn, time, stake — in games'; po-kon, m. “custom; commence- ment’; OCS po-koni, f. ‘beginning’; OCz. po-kon, m. ‘end’. Cf. (? long-gde in) Srb. Cr. kanim se, v. faim to . . ?
quó-que (-quo), adv. & cj. formation based on prn. radical quo-. Cf. quaquos (2) Mir & Ir. cách ('each; every; everybody’. IE *.0- or *-a-); Lat. quoque, adv. "also: Go. cf. -hwah in pis-hwah *whatever'; OCS kakü ‘such’; kako “how, as’; R kak ‘how; as’; (short vowel in) li. kakiü, éti, v. “be capable’; (long vowel in) Latv. koc “though”
quoqulos «turning, bend, joint’. Cf. quequo- los, (ququlos) and quel-, quol- (O-gde type only in) Li. káklas "neck: Latv. kakls, id.
quór- (quor-, qur-) adverbial extn. of the pronominal type quo-, q.v. WP I, 521 Skt. cf. kár-hi (^when', fr. *quor-ghi); ON hvar- gi ‘everywhere’; cf. also Skt. karanam, n. (*cause, reason! in sense of Lat. qua-re); Arm. ur, adv. (z-gde) ‘where’; Alb. kur ‘when’; Li. kuf, Latv. kur *where'; cf. also Alb. kurr (never', fr. *qur-ne > *qur-n: OE hwar-ne ‘not at all); Lat. quor, qur, quur & cür ‘why’; Ir cár “where? beside MIr. cair (Chow, fr. *quori, *quori); Cor. cf. par ‘as, so’; Go. hwar, interr. ‘whence’; ON hvar “where; anywhere’, MHG war ‘whither’: hwær ‘where, whither; somewhere, everywhere, wherever’; Du. waar ‘where’; OS hwar ‘where, whither'; OFris.
quón- — quorquol- (quorquel-)
10
20
25
30
35
40
45
1046
hwer, Fris. wier, id.; OHG cf. hwar-ot, OS hwar-od ‘whence’
quorolis ‘mite, tick’. Cf. qurlis Arm. cf. akalar, akarar ‘mite? beside akal (‘bowstring hemp’, lit. ‘twist’ Bedevian. Pho- nol. obscure); Br. poral, pl. -ed, m. ‘tick’; Skt. cf. karirah, am. mn. ‘bamboo shoot? beside (z-gde) kurulah, m. ‘curl, lock’; Lat. cf. cur- culio, gs: -Onis, m. ((1) 'corn-weevil, lit. ‘twister’. Here, despite WH, and see below: quorquol-) (1)
=== leaf ===
leaf0 578
```


## [2026-09-06T15:43:29.171Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i bqt; echo \"---\"; ls incoming/ 2>/dev/null; echo \"--- ocr dirs ---\"; ls ocr/ 2>/dev/null",
 "description": "Check BQT files"
}
```


### [2026-09-06T15:43:29.223Z] TOOL RESULT

```
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
---
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
--- ocr dirs ---
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
```


## [2026-09-06T15:43:30.394Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'skambh\\|kambist\\|(s)kem-\\|skem-' POK_full.txt | head -30",
 "description": "Grep Pokorny for skembh"
}
```


### [2026-09-06T15:43:30.449Z] TOOL RESULT

```
74951:Material: Old Indie skabhnati, skabhnotr propped ', Perf. caskambha, skabhayatF 
74952:fastened, ligated, strengthened, reinforced, made fast; fortified '; skambha-rc\., 
74953:skambhana-m^ prop, pillar', Avestan i/y055/r5/77i6'a/77 'under fastening, strengthening ', 
74965:(compared with Old Indie skambhana-m) reshuffling through Aryan from skabh- after
```


## [2026-09-06T15:43:36.347Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'kamb\\|hornless\\|mutilated' POK_full.txt | head -40",
 "description": "Grep Pokorny for kamb/hornless"
}
```


### [2026-09-06T15:43:36.397Z] TOOL RESULT

```
10118:High German Bauch, in addition Latvian bugarains^ tubercular ', buga^ hornless cow ', 
17320:by PIE hunters, see Root/ lemma: Rem-2\ hornless, young deer. 
30710:horns-, also hen without tail ' because of poln. ^0/770/y" hornless', Czech homolyds.; 
30733:1. Germanic kamb-, kumb-'c\ot, chunk, clump, block, lump, cut-off piece of wood '. 
32042:(zero grade) kielbock^ hornless he-goat; billy goat ', compare alb. tsjap guF hornless he- 
35008:Old High German kamb. Old English cc»/77i7'comb' ('dentated'). Old Norse kambr^ Q,orr\\i , 
43419:Root / lemma: kamb- 
43421:See also: see below (s)kamb- 
43465:Gothic /7a/77/fe "mutilated'. Old English hof paralyzed hands ', asachs. haf, Old High 
43466:German /75/77r mutilated, lamed '; 
43479:similar root (s)kamb-ixoxx\ gr. aKap(36(;, gall. Cambio-dunum e\.c.)\ yet compare also the 
44757:'; compare OKaAic; 'hack, mattock, hoe' under s/re/- 'cut, clip';K6Aoq 'mutilated, unhorned ', 
44767:SKAaaa, auoKkdc,, Kkambc^, kAogk; ' breaking, fracture, bending of the knee joint, 
44859:klomb(h)o-\n. gr. KAa|jp6(; "mutilated'. Old English laempi-halt, lamp-healt^ lame ' 
45532:Runic Gen. Hnab(i)das {\v\6o Germanic */r/7abhe/ds 'mutilated'). Old Icelandic hnafa, 
50059:Meaning: hornless, young deer 
50060:Material: Old Indie sa/77a-/7 "hornless"; 
50066:Lithuanian zem. s/77i//a5 'hornless', smulism., smulei. ' ox, cow without horns ' {*Rm-u- 
50069:perhaps here russ. /rc»/77c»/>y "hornless'; compare also W. Schuize Kl. Schr. 619. 
57258:Material: 1. Old Irish maeF bald, dull, without horns ', acymr. mair maimed, mutilated ', 
57274:3. ^extension: Old Indie methati^ injures ' (expressives //?), gr. |jiTuAo(; "mutilated, 
60288:Latin /77i//ri/5 "mutilated' (out of it sizil. pupKoc; " dumb ') and murc/dus"\d\e, slack'; Middle 
61137:in Umbrian manfkVk. PI.; Latin /77a/7c^5 'mutilated' (originally 'in the hand'); here Latin 
61597:Material: Latin mutilus, /77i///o'i/s "mutilated', *muticus^ truncated, chopped down, cut down, 
67752:TTPipoq, Doric napoc; "mutilated, blind', a-nr|poc; "unverstummelf; Latin paene{pene) 
74951:Material: Old Indie skabhnati, skabhnotr propped ', Perf. caskambha, skabhayatF 
74952:fastened, ligated, strengthened, reinforced, made fast; fortified '; skambha-rc\., 
74953:skambhana-m^ prop, pillar', Avestan i/y055/r5/77i6'a/77 'under fastening, strengthening ', 
74954:fraskamba-, frascimbana- " girders, pillars '; npers. paskam " a covered walk between 
74955:columns, colonnade, piazza, arcade, gallery, porch, portico ', sogd. sk'np- {*skamb) " base 
74958:Maybe alb. Geg shkamb, Tosc sbkemb'seat, bench, rock, stone, *pillar' related to Latin 
74965:(compared with Old Indie skambhana-m) reshuffling through Aryan from skabh- after 
74973:Root /lemma: (sjkamb- and (s)kemb- 
74979:Root/ lemma: {sjkamb- and (s)kemb-\ "to curve, bend' derived from Root/ lemma: kam-p- 
75004:*(s)kamb- rexrnuAs an kam-, kamp- 'bend' (above S. 525); sein relationship to (s)kemb- 
75636:Material: Old Indie krdhu-' abbreviated, mutilated, small, mangelhaft' (comparative 
76056:"partis'; Umbrian /ra/t£/"distribuito'; Latin curtus^ abbreviated, mutilated' {*kr-t6-); 
76135:Church Slavic /r/^/7b "mutilated', c»/r/^/7///"amputieren', russ. dial. /rd/77>y"from kleinem 
77785:English hamola. Old High German /75/775/'mutilated' (Modern High German Hammel ' 
81409:High German stumpfm. " stub, stump '; Adj. 'stumpf mutilated, abbreviated ';
```


## [2026-09-06T15:43:44.718Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '43410,43485p' POK_full.txt; echo \"=== 77770-77800 ===\"; sed -n '77770,77800p' POK_full.txt",
 "description": "Read Pokorny kamb- and hamal contexts"
}
```


### [2026-09-06T15:43:44.788Z] TOOL RESULT

```
bulgar. k/an/k'room between stove, hearth and wall', serb. klanac. Gen. klanca^ defile, 
narrow passage between mountains ', sloven, klanec' defile, narrow passage between 
mountains, mountain path, rivlet of a brook, village lane ', Czech klanec^ saddle, pass, 
narrow road between mountains '. 

References: WP. I 356 f., WH. 1140 f. 
Page(s): 524 

Root / lemma: kamb- 
Meaning: ' bend, curve, crook ' 
See also: see below (s)kamb- 
Page(s): 525 

Root / lemma: kam-er- 

Meaning: to bend, curve, vaulted 

Material: Old Indie kmarati {ox\\y Dhatup.) 'is crooked'; 

Avestan kamarai. 'belt, girdle' (and '* dome '); 

gr. KpsAsGpov 'beam, ceiling, roof, house' (probably dissim. from *K[j£p£9pov), Kopiapa ' 
dome, four-poster bed; covered cart ' (to Solmsens BPhW. 1906, 852 f. assumption Carian 
origin, Kopapa AsysTai ra aacpaAr), s. Boisacq 402 Anm.; Latin loanword camera, camara^a 
vault, an arched roof, an arch'); at most KapTvoq 'oven' (certainly this could have derived 
from a culture word); 

Latin camur(us), -a, -^/t? 'arched, writhed, crooked, humped ' (dial.), genuine Latin 
camerus. 

References: WP. I 349 f., WH. I 146 f., 149 f., 306, Feist 6, 256; 
See also: s. also kam-p-. 
Page(s): 524-525 

Root / lemma: kam-p- 
Meaning: to bend 



Material: Old Indie kapana'\NO'cr(\, caterpillar, inchworm' {*kmpena), kampate '\.remb\es\ if 
originally ' writhes, curves ' (doubtful); ablaut, kumpa- (uncovered) " lahm an der Hand '; 

doubtful Old Indie kapata-u. "deceit, insidiousness' (would be *kmp-). 

gr. KaiJirn "bend", KaijnToo "curve, bend', KaiJTTuAo(;, Ka|ji|j6(; " writhed, crooked, humped 
'; Kapnri "caterpillar, inchworm'; Pannonian PN Campona; 

Maybe alb. Geg kama, Tosc kemba "leg, bent leg' : engl. Jamb n. A\so Jambe. me. [(0)Fr. 
jambe\eg, vertical support, f. Proto-Romance (whence late L gambahooi) f. gr. Kapinr).] 
The characteristic alb. m > /t?,^ shift. 

Latin campus ^i\e\(y (originally "bend, indentation, lowland, depression', as Lithuanian 
/anka\a\\ey, meadow' to /enkt/ 'bend'); 

Gothic /7a/77/fe "mutilated'. Old English hof paralyzed hands ', asachs. haf, Old High 
German /75/77r mutilated, lamed '; 

Lithuanian kampas 'po\nt, edge, angle ', Latvian kampis' Krummholz '; reduced grade 
(with Indo Germanic «= ein dark environment) Lithuanian kumptT crook oneself ', kumpas 
"crooked', Latvian kumpV become hunchbacked, crooked ', Old Prussian etkumpsMN. 
"against'; in addition probably Lithuanian kumste "fist' as *kump-ste " the fingers bending 
together '; 

perhaps poln. /rg/oa "river island covered with bush, shrubbery'. Old Church Slavic 
kqpina't\ thorn - bushes, thorns, rubus, bush, shrub', russ. /ri/yO//7a "shrubbery, bush, 
mound, knoll; bunch, fascicle, sheaf; 

Indo Germanic kamp- is possibly an extension from *kam- "bend, curve ' (see also the 
similar root (s)kamb-ixoxx\ gr. aKap(36(;, gall. Cambio-dunum e\.c.)\ yet compare also the 
nasalized equal meaning family of Old Indie capa-vn. n. "bow', capala-' resWess, 
fluctuating ', npers. cap "left', i.e. "*crooked'; Endzelin KZ. 44, 63 reminds of *capala-a\so 
in Latvian kaparuoties' wriggle ', k'eparaV wriggle, move with difficulty ', Lithuanian 
kapanotis " liegend sich aufzuhelfen suchen ' or " go laboringly '. 

References: WP. I 346, 350 f., WH. I 148 f., Trautmann 116. 
=== 77770-77800 ===
basic meaning " jumper, Laufbursche' and dissimilation from * skal-[s]kas-\ 

Lithuanian si/o/ys'Galopp', Latvian su6//s' footstep '. 

Maybe alb. (ske/-) *shke/'to step'. 

References: WP. II 600. 
Page(s): 929 

Root / lemma: (s)Rem- 

Meaning: disabled 

Material: Old Indie sama/a-n. 'fault, error, damage, pity'; Old Icelandic PN. Hamall, Old 

English hamola. Old High German /75/775/'mutilated' (Modern High German Hammel ' 

wether, castrated ram '); Old Icelandic hamla. Old High German hamalon e\.c. ' mutilate '; 

with expressive -mm-:0\6 Icelandic skammr. Old English Old High German sca/77/77 'short'; 

Old High German hamm, hammer^ rc\\}W\a\.e6\ 

Note: 

common lllyrian-alb. sk- > h-. 

References: WP. II 560, Holthausen Awn. Wb. 105; 

See also: in addition also kern- above S. 556.
```


## [2026-09-06T15:43:54.736Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '74940,75020p' POK_full.txt",
 "description": "Read Pokorny skamb-/skembh- entries"
}
```


### [2026-09-06T15:43:54.789Z] TOOL RESULT

```
pricker, awl'; further by Trautmann 261 f.; Hittite sum(m)anza(n)^ filament ', also (?) suel, 

su/7 ds. 

References: WP. II 515 f., WH. II 631 f., Carruthers Lg. 6, 161 f. 

Page(s): 915-916 

Root / lemma: sArab^- skarrt^- 
Meaning: to support 

Material: Old Indie skabhnati, skabhnotr propped ', Perf. caskambha, skabhayatF 
fastened, ligated, strengthened, reinforced, made fast; fortified '; skambha-rc\., 
skambhana-m^ prop, pillar', Avestan i/y055/r5/77i6'a/77 'under fastening, strengthening ', 
fraskamba-, frascimbana- " girders, pillars '; npers. paskam " a covered walk between 
columns, colonnade, piazza, arcade, gallery, porch, portico ', sogd. sk'np- {*skamb) " base 
of the universe '; 

Maybe alb. Geg shkamb, Tosc sbkemb'seat, bench, rock, stone, *pillar' related to Latin 
scamnum {*sksb'"nom). 

Latin scamnum {* skdb^nom) " bench, footstool ', Demin. scabillum, scabe/fum ' n\e6r\ges 
Bankchen, footstool '; 

die Aryan within nasalization, as well as the e-vocalism from Avestan frascimbana- 
(compared with Old Indie skambhana-m) reshuffling through Aryan from skabh- after 
*stent)^- (see steb-' jamb, upright section of a doorframe or window frame; stanchion, 
roof support ') in Old Indie stabhnat/" plinth, base, base of a pedestal t', stambha- ' posts, 
pillars, columns ' etc. 

References: WP. II 539, WH. II 487 f. 
Page(s):916 

Root /lemma: (sjkamb- and (s)kemb- 

Meaning: to curve, bend 

Note: 

Root/ lemma: {sjkamb- and (s)kemb-\ "to curve, bend' derived from Root/ lemma: kam-p- 

: "to bend'. 

Material: Gr. aKapp6(; "crooked, bowlegged'; Old Irish ca/77,6' "crooked', cymr. corn, cam, 
bret. kamm ds., gall, in Camb/o-dunum 'Kempten', bret. camhetan rot' rim of the wheel ' 
{*cambita); zero grades *kmb-'\.\}'cn = swap, vary, exchange ' and "zusammendrehen. 



fessein' in gall.-Latin cambiare^s\Na'Q, vary, exchange ' and Middle Irish cimb^ tribute, 
silver'. Old Irish c/'mb/d 'captwe', c/mbe' captivity, imprisonment, confinement'; 
Maybe alb. /re/r7/?ey 'exchange' a Latin loanword. 

With e-vocalism: gr. Koppoc; m. "band, strap, loop', K0|jp6u) " bind, knot '; Norwegian 
hempa 'Kleiderstrippe, loop, noose, snare, handle, part of an object designed to be 
gripped by the hand ' (also ' stuff of hemp ', in which meaning certainly influenced by hamp 
" hemp '); 

from a basic meaning " go crookedly ' from reiht man an: gr. *OK£|jpu) " limp ' 
erschlossen from dem names lK6iJpO(;, Swedish skumpa " limp ', skimpa " jump, dance ', 
Old High German scimpfan^ joke drive, push, play, deride ', Modern High German 
schimpfen, Schimpf, Modern High German (Low German) humpen, humpeln^ hobble, limp 
'(or to keub-? above S. 590 f.); 

*(s)kamb- rexrnuAs an kam-, kamp- 'bend' (above S. 525); sein relationship to (s)kemb- 
is still unclear; also das zur nasalized root for 'bend' (?) or 'haken' (compare Lithuanian 
kimbCi, kibti^ hang bleiben'): kabli, -eti^ hang ', kabinti^ hang ', kablysm. 'hook', kabei. ' 
Heftel, hook ' (but also e-forms as kebeklis 'hook'); Old Church Slavic skobai. ' fibula ', 
russ. skoba^ agrafe, hook, clasp ', wherefore Old Icelandic hopu. 'small bay'. Old English 
/7o/?'ring'; against it Old Icelandic hespa^ iron staples ' = Old English haepse, haesp. 
Middle High German haspe, hespe. Modern High German Haspe, Haspe, holl. hespe 
'Hijftgelenk', Middle Dutch also 'hack, mattock, hoe' to kap-, above S. 527 f. 

References: WP. 1346, 350 f., ll539f.,WH. I 148f., Trautmann 112, 116. 

Page(s):918 

Root / lemma: (s)kand- (s)kend- 

Meaning: shine
```


## [2026-09-06T15:44:11.332Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD kam ==\" && grep -n -E '^kam|kam ,|kam\\b' PHD.txt | head -30; echo \"== PHD kamen ==\"; grep -n -i 'kamēn\\|kamen\\|kamist' PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep MacKenzie for kam"
}
```


### [2026-09-06T15:44:11.392Z] TOOL RESULT

```
== PHD kam ==
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
421:kabk 48 kamālīģ
422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
828:archer kamāndār.
1061:bowman kamāndār.
1221:chief (a.) mādayān, (daevic) kamālīg.
1570:desire (n.) árzóg, kam(ag), waran, xwāhišn.
1938:éwéand, kam,
2230:head sar, waydān; (daevic) kamāl.
2376:ill-will duškam.
2645:little andak, kam, ēzārak, xwurd; à = čegām-iz-ē(w).
3296:purpose &im, kam(ag).
3698:small giínag, kam, keh, kédak, kūč(ak), Как, nihang, ēzārak, xwurd; ~ thing xwurdag.
4313:will axw, kam(ag). willing(ly) kāmagēmand. willow wed.
4987:kardagān 1%kardāg kam kamāndār kamān kamāl kamālīg kamistīh ‘kamist kamzor kamzorih kamar kamarband maygt arz! kastār kastärīh kchtar kaf
== PHD kamen ==
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:2588:least kahist, kamist, nidom; at — pad kamistih.
PHD.txt:4987:kardagān 1%kardāg kam kamāndār kamān kamāl kamālīg kamistīh ‘kamist kamzor kamzorih kamar kamarband maygt arz! kastār kastärīh kchtar kaf
PHD_mackenzie.txt:3158:kim-, v. kamistan.
PHD_mackenzie.txt:3177:kamist [kmyst'] least.
PHD_mackenzie.txt:3179:kamistan, kam- [YCBEN-stn' < A y~bJz, -V ~bh; k'm-(y)ltn'              M
PHD_mackenzie.txt:6942:lad redak.                                least kahist, kamist, nidom; at ""'" pad
PHD_mackenzie.txt:6943:ladder pillagiin.                            kamistih.
PHD_mackenzie.txt:7909:victuals pih.                            want (v.) abayistan, kamistan, xwas-
PHD_mackenzie.txt:9524:kamistih        ~~~                   kilN                  ~S
PHD_mackenzie.txt:9525:kamist               \~~              diz1                 ~~~
PHD_mackenzie.txt:9711:kcwan                            ,~t'~          kamistan                 \'~i
PHD_mackenzie.txt:10447:kamistanl             \\tU.' \ t6) V
```


## [2026-09-06T15:44:13.217Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN ==\"; grep -n -i 'kamna\\|kambist\\|kamîn\\|kamin' HRN.txt | head -20; echo \"== HUB ==\"; grep -n -i 'kamna\\|kambist' HUB.txt | head -20; echo \"== NYB ==\"; grep -n -i 'kam ' NYB_vol2_glossary.txt | head -10",
 "description": "Grep Horn, Hübschmann, Nyberg"
}
```


### [2026-09-06T15:44:13.302Z] TOOL RESULT

```
== HRN ==
7529:ap. kamna- Venig*; aw. katmia-; phlv. kaw^ kam(i).^f,
9743:- 1129. yöz *Jagdleopard' (Vis und Kamin, Seite 40 Vers 12'^).
== HUB ==
3107:kamna-, ^kanbiyah--, *kanbista- (= zd. kambiSta-), vgl.
3597:kamna- = *kabna'. Dazu afgh. numd, nUmd u. s. w.
9054:= ap. kamna- aus *kabna', idg. *A:i^6Awa-, vgl. zd. sup.
9055:kambistem; nam *feucht' = ap. *namna' = idg. *nabhna-y
9183:^namna- = arisch ^^nablina- (vgl. kam *wenig = ap. kamna
== NYB ==
335:akah [’k’s] aware, knowing 39%, 574. 108?; ~ kartan to inform 10%, 11%; kē hac dén ~ he who is enlightened by Religion 6716; subst. pl. cas. obl. kam ~-Gn the ignorant, the witless 11077. — MPrs .g?
737:aškamb ['škmb'], aškam ['škm], aškom [škwm], also [KLSH 1013-18, 1111, 6513], belly, stomach, womb 3? etc. — MPrs škmb (A-H II; Sogd. 3176); Paz. aškum (Mx), iškam (SGV); NP iškam, šikam. Aškān ['ik?n!] n. pr., the ancestor of the Aškanian, or Arsacid, dynasty; Zēndān
1750:h- (HWH- ; 3d p. sg. "YT', neg. L'YT', inser. and Ps. ^Y TY, L'YTY 2nd p. pl. enel. -ét in amahraspand-é 58"; forms v. I, 175] to be, only in the pres. ind., subju. and opt., other forms from bütan (q. v ): l. as an independent vb. in the 3d p.: exist(s), e.g. hast hàn ke ahlayeh the One who is Righteousness exists 57°; héc ke but hénd u hec ke bavénd u h&c ke hend all who have been, and all who will be, and all who exist (now) 6417-18, cf subst. hast and nesteh; im roc 7 mähakän hast tdi ... to-day it is seven months since 1011-12. kë hast ke ...? who is there who ...? 257-7; andar Ērān-šahr asvār-ē nest ke ... in Eran-shahr there is no horseman who ... 15; hast 4-8 ... u hast 1-§ ... u hast i .. . there is some (of it) that ... and there is some (of it) ... and there is some (of it) that... = part of it... part of it... ete. 9317-18.26; hast kč-š veš, hast ké-§ kam some have more, others less 96°; astömandän mar- tömän (gen. part.) hast i ... of earthly men there are some who 10519; hast <a> šāhān šāh, hast <i> kesar some belong to the King of Kings, others to the Emperor 11519-20; nē hast kū there is no place where, nowhere 611°; hast (i) ka there is a time when, sometimes, at times 7725-26, 8122, 12018-1?; — with prev.: šusr i Gayomart cis andar hast there is some part of the sperm of G. in it 9422-23; kū-š ataxš andar nést where there is no fire 3721, — 2. copula, with a noun, a pron., or a prep. -- subst. as its complement, pas- sim; the 3d p. sg. ‘is’ is very often not
2169:kam [km] little (adj. and adv.), few 6617. 9319.21 966.7, 11022; almost a modest ne- gation: explained by na FrP, Cod. S, XV, 7.— Av. (440) kamna-; Paz. NP kam. V. kem.
2170:kam [k?m] will, desire, wish 694. — Av. (463) kama-; MPrthPrs k'm; Paz. NP kam.
2190:10318-14; — personal construction: pdti- fras küménd kartan 10215. — Denom. of kam (q. v.); in the Ps. ‘to be well pleased in’; MPrs pres. k’m- personal; MPrth k’m’dn k’m- (A-H III); NP kamidan.
2281:. he whose virtue and sin are equal 7924-25; seldom % ke: cigon mart-ē ké-§ vēhēh veš u ēvak i ke vēhēh kam as a man whose goodness preponderates and an- other whose goodness is deficient 96°’ ; — it cannot be governed by a prep.; in such cases, a) the prep. is placed in the rel. clause and governs a dem. pron. referring to the antecedent: (dätär) ke hac & aštak veh (the Creator) from whom a good Messenger (has come) 5711; ke... hac ēišān ēvak ravēt (the three sons of Zartuxšt) of whom one ... shall appear 7115-16, 181; kē-š pat han urvar bē barēt [YDLWN-x-] by which he removes the plants 569-10; han kas ke yuvat hac či nē vicarét the man without whom you will not get on 416-1’; b) the prep., changed into an adv. and assuming its special form if there exists any, is placed in the rel. clause and may refer directly or through an encl. to kč: hàn ke én x"amn patiš dit the one about whom this dream was dreamt 21-9 (patiš for pat referring to ke); Hutös ke ... 30 haciš zàt H. of whom 30 children have been born 24? (haciš for hac); han gàv pem kē tan gohr à Zartuxst avis mat ēstāt the cow-milk into which the bodily element of Z. had entered 4225-26 (avi$ for 0); hamäk cis ke-š martömän rämisn ... haciš everything from which men derive pleasure 10020-21 (haciš for hac referring to ke through the intermedium of the encl. -š in ke-$); han keš pātiyāvandtar kē-š pätix$äych apāk bavēt that religion is most powerful to- gether with which there is royal power (which is joined with royal power) 8018-12 (apak here adv., referring to ké through the intermedium of the enel. in ké-8); béstan-é ke-š hamäk urvarihā u spramīhā andar a garden in which there are all sorts of plants and flowers 105! (ké-§ . . .
5202:ka-: cē kā- (kāta-): kātak kadā: kad kaēnā-: kēn kaēš-: nām-cišt kaēta-: kēt ka60: cihénitan kahrkäsa-: karkäs kahrpuna-: *karbök kainyä-, kaini: kanik kämä-: kam kamarä-: kamar kamoroča-: kamar kambištem: kčm
```


## [2026-09-06T15:44:26.260Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,off,pat in [('HRN.txt',21,\"ap. kamna- Venig\"),('HUB.txt',10,\"kamna- = *kabna\"),('HUB.txt',10,\"kamna-, ^kanbiyah\"),('HUB.txt',10,\"= ap. kamna- aus *kabna\"),('NYB_vol2_glossary.txt',8,\"kam [km] little\")]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    i=t.find(pat)\n    if i<0: print(f,pat,'NOT FOUND'); continue\n    leaf=t.count('\\f',0,i)\n    print(f, pat[:25], 'leaf0=',leaf, 'printed~', leaf-off, leaf+1-off)\n    print('   ...', t[max(0,i-400):i+400].replace('\\n',' ')[:900])\n    print()\nEOF",
 "description": "Locate Horn/Hübschmann/Nyberg pages"
}
```


### [2026-09-06T15:44:28.209Z] TOOL RESULT

```
HRN.txt ap. kamna- Venig leaf0= 214 printed~ 193 194
   ... rd. ktdäw, serkuläw, arm. LW. sarßiday 'cucullo dei dottori Armeni'). Calautica und Verwandtes (siehe de Lagarde, Mitteilungen II, 4 ffolg.) /gehören nicht hierher. 864. kulbe, kurbe *Bude', arab. LW. ktirbaj, kurhaq^ kidhat, N ö 1 d e k e (mündliche Mitteilung) vergleicht ^r. xaXvßrj *Hütte, Laube. Dies zu yiaXvnro) (6. Meyor, Griech. Grammatik-, § 197a). 865. kern 'wenig, gering, klein', kemJn, ap. kamna- Venig*; aw. katmia-; phlv. kaw^ kam(i).^f, LW. kurd. kirn; afy. bei. (125) kanij n. ßam. Die Grundform ist ^kanibhua- bezw. *kipbhna' (Hübschmann, ZDMG. 44, 559, Bartholomae, Studien H, 101). Kurd. kirn und phlv. kim^ welches bisweilen vorkommt (z. B. vd. 19 (9)), werden auf den Comparativ *kamni/ao zurückgehen («-Epenthese). 866. {\)kemer 'Gürtel', kemra^), aw. kamara- 'Gürtel*; phlv. 

HUB.txt kamna- = *kabna leaf0= 112 printed~ 102 103
   ... etc., im Paz. nigeriSn^ nigareSn etc. Phi. niklret = ap. *nikriyafiy? Vgl. oben Nr. 992 phi. m^nisn fiir paz. manisn. Hier fehlt np. nigun = phi. nikun *uingekehrt, umgestiirzt* = arm. nkun 'niedrig'? WZKM. 7, 380. Hierher nach Horn (KZ. 33, 434) np. nikuhtdan 'tadeln, schmahen' = skr. kutsay- schmahen, tadeln . Schon bei Vullers, Radices, s. v. 1039. Np. nam aus *namna- ~ *nabna- wie kam aus ap. kamna- = *kabna'. Dazu afgh. numd, nUmd u. s. w. (Geiger). 1040. Die iranischen Dialektformen sind schwerlich ent- lehnt, also iran. ^namad- anzusetzen. 1041. Zd. nimata- ist dunkel, vgl. Darmesteter, Zend- Avesta n, p. 45, Anm. — Dazu osset. nimdt, nmdt Tilz, Filzmantel', s. Verfasser, Etym. und Lautl. der osset. Sprache, p. 129, Miller-Stackelberg, Fiinf osset. Erzahlungen p. 62. Skr. namata- Ti

HUB.txt kamna-, ^kanbiyah leaf0= 98 printed~ 88 89
   ... cht vorliegt. Kurd, kiddw verhalt sich wohl zu np. kulah wie kurd. dew *Mund* zu ap. dahan, setzt also ein phi. *kulaf voraus, aus dem np. kulah entstand wie np. koh aus phi, kof 'Berg*. 864. Np. kulba = kurba *Bude' aus phi. "^kurpak = arm. krpak 'Werkstatt, Laden, Schenke', Apg. 28, 15 u. s. w., hat also mit gr. ytaXv^rj nichts zu thun. 865. Die drei Steigerungsstufen lauteten im Altpersischen: kamna-, ^kanbiyah--, *kanbista- (= zd. kambiSta-), vgl. zd. taxma--, tc^yah-, tandista^. Also Horn's *kamnyao eine wuste Bildung! Vgl. Fr. Muller, WZKM. 7, 368. 867. Das Verhaitniss von np. kamar 'altitude, collis, tumu- lus, saxum* = afgh. LW. kamar 'the middle of a moun- tain, precipice, cliff, the high bank of a river' zu zd. kamereda" 'Kopf der Devas u. s. w. = phi. kamdr^) ys. 56, 12, 4 (Sp.)

HUB.txt = ap. kamna- aus *kabna leaf0= 263 printed~ 253 254
   ...  Gabe* (= phi. dcihisn), rosan *heir = zd. raoxsna-, Ueber m aus g^, g^h + n siehe § 112, c; fiber s» aus 4'w siehe § 131. c) Idg. rfw, dAw — ap. np. n: sikanam zerbreche aus arisch *8kadnami, Wrzl. idg. slcend; vgl. zd. 6wna- JGrund, Boden ^) np. 6mw 'Fundament , Grund' = skr. budhna-. Dagegen bleibt nd, ndh, vgl. handa == ap. bandaka- *Diener. d) Idg. bhn = ap. mw = np. m im Auslaut : kam wenig = ap. kamna- aus *kabna', idg. *A:i^6Awa-, vgl. zd. sup. kambistem; nam *feucht' = ap. *namna' = idg. *nabhna-y vgl. zd. napta- 'feucht*. Siehe w6 = m § 153. e) Idg. pn = iran. fn = np. / oder m oder 6 ? im Auslaut: ^a/ *Hitze' = zd. tafnu-, tafnah-; sdm^) *Nacht- essen', phi. iflw, zd. xsdfnlm (ace, ys. 62, 7 der Neuaus- gabe), vgl. zd. xsafni; x^ab^) *Schlaf' = zd. x^afna- (oder = skr. svapa- *S

NYB_vol2_glossary.txt kam [km] little leaf0= 123 printed~ 115 116
   ... Vištāsp. Kai-X čsrči-šat [kdhwslwd š*t'] n. pr. of a town 1149. — “K.-X. is glad"; v.s. v. Xösröi. kālpa6 [k*lpt'], kalpu& [k’Ipwt'] shape, external bodily form 892%, 9026, 10127, — MPrs k’lbyd (List 84); Paz. kälbud, Skr. v. kaya sundara (Aog.); NP kalbad, kälbud ‘the body of a man or an animal’, ‘a model, a last for shoes" which is the original sense, the w. being borrowed from Gr xadronddtov.. kam [km] little (adj. and adv.), few 6617. 9319.21 966.7, 11022; almost a modest ne- gation: explained by na FrP, Cod. S, XV, 7.— Av. (440) kamna-; Paz. NP kam. V. kem. kam [k?m] will, desire, wish 694. — Av. (463) kama-; MPrthPrs k'm; Paz. NP kam. kamak 1. will, wish, desire (= kam): 6 ~ rasét (imp.) may you attain, (the ful- filment of) your Royal Pleasure! 107; brihenisn u spahr u ~ i yazdān th
```


## [2026-09-06T15:44:39.608Z] TOOL CALL #23: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1689 --image 2>&1 | tail -40",
 "description": "Fetch Borhan-e Qate page 1689"
}
```


### [2026-09-06T15:44:46.246Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1689.png
REF: BQT:1689  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 482  OCR-lang: fas

-۱۹۸۹- کما
کلیواژ ۱ ».با زای فارسی . بروزن *کلیون ؟ - بر وزن کلگون, جامه‌ای
ومعنی‌غلیواج است کهزغن‌باشدوآنرا مرغ کوشت | راکوبند که از هفت رنگه بافته باشند .
بیان نوزدهم
در کاف تازی با میم مشمّمل در هفنّاد وسه لغخت و کنات
گم - بفتح اول و اسکون ثانی » بمعنی کما - بفتح اول‌بروزن قبا »آستین رفیده
اسك باشد که در مقابل یار است ۴ - و بمعنی را گوبند و رفیده لته چندی است که مانند گرد
ترك ۴ - وضمان 9 - و نادرهم آمده است | بالشی دوزند و خمیر نانرا بربالای آن پهن‌سازند
و در عربی بمعنی چند ومقدار باشد ‎٩‏ - وم | و برتنور چبانند وآمتینی هم برآن اصب‌کنند
اول نام ولایتی است از عراق و معربآن قم‌است | تا بساعد و بازو ازآتش آسیبی نرسد ‎٩‏ - ویزباز
واکنون بتعریب اشتهار دارد ۷ - و نوعی‌از خار | را نیز کفته‌اند که عربان بسباسه خوانند. کوبنه
هم هست که کتیرا صمغ آنست و آنرا بعریی | پوست جوزبواست ؛ و باین معنی بضم اول و آدسر
شج‌ةالقدی و مواالمباد وموالذالسیح کوبند | اول عردو بنظر آمده است - و چم اول کیاهی
- و درعربی آستین قبا و پیراهن و امشال آن | باشد بغایت بدبو وکنده ومتعفن اوآ نراکمای‌نیز
باشد ۸ . کفته‌اند *۱.

۹ << کهواح * غلیواژ. ۲ - باکاف پارسی «گلیون» است مخفف‌انگلون(ه.م.).

۴ - پارسی باستان سعهصورت 2۲382 , - د[2ل(اط 0۷22 , 5012اط ۰5۳۵0 اوستا-
48 . پهلوی ۷8۲۵ » کردی ع ۴11۵ ۰ افضانی و بلوچی ۴:۲۷ « اسشق - هوبشمان
۹۵ نیب رکه اس ۱۱۸: ۳21ص ۴۵1۵:۱۲۷۸ سمنانی ۴3۲01 سرخه‌یی ۰۴250
لاسگردی وشهمیرزادی ۲8 «ک» . ۲ ص۱۹۷ > کیلکی ۴۵۲۵ .

۴ -کم‌اوکیر » پعنی ترك اوکیر «رشیدی». 8 - رك : رشیدی .

- بفتح اول و تشدید دوم . - رم بألشم شپهر معروف که معرب آن‌قم‌است
وکنب نیز گوبند .> «رشیدی». ۸ - (ع) «کم بالضم, آستین. اکمام و کمی هکعنبة جمم.»
« منتهی‌الارب >.

‎٩‏ - فرهنگه نظام کلمه را بم اول خوانده ومحرف کم بمعنی آستین عریی دالسته » و
محشی فرهنکه رشیدی نیزهمین حدی را زده است ۰ *۱ ۳ 16۷191100170 ۳6۲12 کیاهی
ازتیرة چتربان ( 010611118769 ) که درنقاط مرتفع بر کهای معطر آن برای خوراكحیوانات
بکارمیرود » وازجنسی(۶06108 298. ۳) صمغ بدپویی‌بنام انغوزه و از جنی616[ا4 ۰888 ۴
صمفی بنام اجدان حاصل میشو دکه مصرف داروئی دارد « کل کلاب رسفجتها

‏پوربهای جامی«فرهنکه نظام >.
```


## [2026-09-06T15:44:59.160Z] TOOL CALL #24: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1689.png"
}
```


### [2026-09-06T15:44:59.657Z] TOOL RESULT

```

```


## [2026-09-06T15:44:59.655Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T15:45:33.200Z] TOOL CALL #25: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1689.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed page ۱۶۸۹ = 1689 (BQT_v3_picofile.pdf p.482). Read from the page image by vision, 2026-09-06.]\n\nRunning head: کما  /  -۱۶۸۹-\n\nبیان نوزدهم\nدر کاف تازی با میم مشتمل بر هفتاد و سه لغت و کنایت\n\nکم - بفتح اول و سکون ثانی ، بمعنی اندک باشد که در مقابل بسیار است ۳ - و بمعنی\nترک ۴ - و نقصان ۵ - و نادر هم آمده است ۵ - و در عربی بمعنی چند و مقدار باشد ۶ - و بضم\nاول نام ولایتی است از عراق و معرب آن قم است و اکنون بتعریب اشتهار دارد ۷ - و نوعی از خار\nهم هست که کتیرا صمغ آنست و آنرا بعربی شجرةالقدس و مواکالعباد و مواکالمسیح گویند\n- و در عربی آستین قبا و پیراهن و امثال آن باشد ۸ .\n\nکما - بفتح اول بروزن قبا ، آستین رفیده را گویند ... (etc.)\n\n--- Mo'in's footnotes ---\n۳ - پارسی باستان kamna ، صورت *kanbiyah ، *kanbishta ، اوستا kamna ، پهلوی kam ،\nکردی kim ، افغانی و بلوچی kam - اشتق - هوبشمان ۸۶۵ ، نیبرگ ص ۱۱۸ : kam ،\nص ۱۲۸ : kēm ، سمنانی kāmi ، سرخه‌یی kam ، لاسگردی و شهمیرزادی kam «ک. ۲ ص ۱۹۷» ،\nگیلکی kam .\n\n۴ - «کم او گیر» ، یعنی ترک او گیر ، «رشیدی».\n۵ - رک : رشیدی.\n۶ - بفتح اول و تشدید دوم.\n۷ - «کُم بالضم» شهر معروف که معرب آن قم است و کنب نیز گویند ، «رشیدی».\n۸ - (ع) «کُم بالضم ، آستین. اکمام و کممة کعنبة جمع.» «منتهی‌الارب».\n۹ - فرهنگ نظام کلمه را بضم اول خوانده و محرف کم بمعنی آستین عربی دانسته ، و\nمحشی فرهنگ رشیدی نیز همین حدس را زده است.\n۱۰ - Ferula levisticum = گیاهی از تیرهٔ چتریان (Ombellifères) ...\nEOF\necho saved; ls -l /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1689.vision.txt",
 "description": "Save vision transcription of BQT 1689"
}
```


## [2026-09-06T15:45:34.625Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY latin index kam ==\" && grep -n -i 'kamna\\|KAM ' incoming/ARY/ARY_latin_index_pages.txt | head -20; echo \"== ARY pages کم ==\"; grep -n 'کمین\\|کم$\\|کم ' incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Aryanpur"
}
```


### [2026-09-06T15:45:35.499Z] TOOL RESULT

```
saved
-rw-rw-r-- 1 sfmqrb sfmqrb 2123 Sep  6 11:45 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1689.vision.txt
```


### [2026-09-06T15:45:37.331Z] TOOL RESULT

```
== ARY latin index kam ==
1944:VENIR ° (ld) :HTALIAN)' Ul! KAM, KAM :(TOKHARIAN A) A ¢ bs
1945:VENI (44) (RUMANIANY iho, KAM, KAM :(TOKHARIAN B) B 5 )\bs
2313:DELAMARRE: (LE LONG DE) 301 SACA, SAKAM (SANSKRIT) <y Suite |
11554:CARO AUTALIAN) gilt) KAM PAHLAVI) 5 shay
11839:(4slt)(OLD HIGH GERMAN) oS gllT KAMNA, KAMBISHTEM
11841:SCHARF (ULGERMAN) glT KAMNA, *KANBIYAH, KANBISHTA
11844:SHARP (4UMENGLISH) p81 KAM = NR ADOC
11845:SHARP (4UN(DANISH) Slats KAM “4APCHAND (uty) gh
11994:KDE, KAM CZECH) Sx, oG FRENCH) ii 5
11995:KDE, KAM BOHEMIAN) gos » DONDE SPANISH) glial
11996:KDE, KAM (SLOVAK) S\ gel DOVE ITALIAN) g\Jix
12319:KOMME s(NORWEGIAN) «5395 KAM A(TOKHARIAN A) A 5 j\65
12320:KOMEN (DUTCH) «sacha KAM (TOKHRIAN B) Bs ins
12323:GATRAM —(OLD IRISH) «Sg p! KAM > ARMENIAN) «g\
15792:JouG (FRENCH) 4.315 YOKAM s(TOKHARIAN A) A 15 )\o5
== ARY pages کم ==
34:ارائه شده است نیز کم نیست. مسئولیت درستی اینگونه واژه‌ها و به طورکلی همه مطالب این کتاب را
89:برتری نژادی آنها کم شد. هر چه اين کوچگران از آلمان دورتر شدند؛ میزان آمیختگی خون آنها با
114:سرزمین کم‌کم از یک سو به فلات ایران و شمال هندوستان و از سوی دیگر به آسیای صغیر و از آنجا
186:این نواحی نیز متقابلاً تحت تأثیر زبانهای محلی قرا رگرفت وکم کم به چندگویش تبدیل شد (ترکی
229:نبستند) این واژه کم کم نو آوری شده. امکان ثانی محتمل‌تر است چون ریشه‌ی واژه‌ی «مار» با ریشه‌ی
289:شده‌اند. این جامعه در آغاز شکارگر -گر دآور (11701181-0۸7778587) بوده ر کم کم شبانی و
350:کم شده است. در شمال و مرکز ایتالیا «اتروسکان‌هاء (177741780۸1758) تمدن درخشانی را به وجود
399:شماری از دانشمندان اروپایی متوجه شباهت‌هایی میان برخی از زبان‌ها شدند. آنچه که ک‌کم واضح
406:دیگری که کم کم مشهود شد اين بود که هر یکك از زبانهای معاصر پیامد زبانهای قدیمی‌تری هستند.
412:۸ کهن مادر,زبانهای |سپانیایی و ایتالیایی و پرتغالی و غیره هم هست. بدین روش کم کم بیشتر زبانهای
556:زبانهای هند و اروپایی نی ز کم کم سرعت بیشتری گرفت.
641:و ایرانی در زبان‌های مردم پین‌النهرین بسیار نادراند ولی پس از آن تاریخ شمار این واژه‌ها کم کم
759:اطراف آن) کم کم رواج بیشتری پیدا کرد و زبان امپراتوری روم ( که سر ناسر سواحل دریای مدیترانه
760:را تحت تصرف داشت) گردید. کم کم زبان لاتین در بخش‌های مختلف امپراتوری تبدیل به
771:مرکز آسیای صغیر پیش رفتند. در اثر ورود اقوام هند و اروپایی دیگر؛ کم کم گستره‌ی مردم سلت :
846:آمپراتوری روم فروریز شد و زبانهای رومانس کم کم از لاتین جدا شدند.
926:کم و بیش همین خصوصیات را دارا پودند.
1116:." امروزه شمار لبیدها بسیار کم شده است ولی باز هم در برخی نقاط به آنها برمی‌خوریم. در برخی از
1124:: هدوستان به یک زبان واحد تکلم می‌کردند ولی در اثرگذشت زمان کم کم دارای د وگویش و سپس
1253:شدکم نیست. پژوهشهای پیشاهنگانه معمولاً هم راهگشا هستند و هم محتمل به داشتن لغزش. امید من
```


## [2026-09-06T15:45:42.376Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11830,11850p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== tag ===\"; awk 'NR<=11850 && /\\[pdf page/ {t=$0; l=NR} END{print l\": \"t}' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Read ARY latin index around KAMNA"
}
```


### [2026-09-06T15:45:44.614Z] TOOL RESULT

```
POKORNY, = SSSsSt~CS~«aD KISHIN KURDISH) 52,5
MACKENZIE: KASHAG, KASHAGH :(BALUCHI) gx ss
(DRAM) 111, (PULL) 129 AAFGHANT) (su) lidh
BUCK: KXAL, KASHAWEL
(DRAW, PULL) 571-572 KARSH., KRSH- :(SANSKRIT) y Sle
170 ebb ub, KARSHEM ARMENIAN) gis)
sentloal
. CAPS 45h
SKARP, SKERP AAVESTAN) gee sl
(4slt)(OLD HIGH GERMAN) oS gllT KAMNA, KAMBISHTEM
SCARF HOLD PERSIAN) jel) pe,
SCHARF (ULGERMAN) glT KAMNA, *KANBIYAH, KANBISHTA
(QL(OLD ENGLISH) 4S godt KAM, KEM s(PAHLAVD) (5 34,
SCEARP KEM, KIM KURDISH) 525 at
SHARP (4UMENGLISH) p81 KAM = NR ADOC
SHARP (4UN(DANISH) Slats KAM “4APCHAND (uty) gh
SKARP (4U}(SHEDISH) 5.8 yo KHRAMBOS GREER) gli
SKARP (4Lt}(NORHEGIAN) 5335 (4L}(OLD SCANDINAVIAN) AS Gotha!
SCHERP (4LEx(DUTCH) gale SKARPR
SKARP()L4Y(OLD SAXON) oS pS
(4LM(OLD FRISIAN) oS 534.3
=== tag ===
11824: [pdf page 406]
```


## [2026-09-06T15:45:50.277Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'KAMNA\\|KANBISHTA\\|KAMBISHTEM' incoming/ARY/ARY_pages.txt | head",
 "description": "Grep ARY main pages for kamna"
}
```


### [2026-09-06T15:45:50.323Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:45:52.542Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer('kamna', t):\n    i=m.start()\n    s=t[max(0,i-200):i+300].replace('\\n',' ')\n    if 'Adj' in s or 'wenig' in s or 'kambi' in s:\n        print(t.count('\\f',0,i), '::', s[:500]); print()\nEOF",
 "description": "Find Bartholomae kamna entry"
}
```


### [2026-09-06T15:45:54.398Z] TOOL RESULT

```
153 ::  maoB  *°ya»Al>'^  N._J0. Pu. :  laiar  .  .  mal  an  äii/a  asp  ptm  •'.  .  Wei isPferdemilch".- :)  So  T. •  p.  ""asbäray-  Adj.  'der  auf  einem  Ross reitet,  beritten':  /lauv  . .  iiadä  kamnaibis 'ribil  aiiyavt^  "..  mit  wenigen  Berittenen . ." BM-";  7. 2->,  13- Durch  llaplol.  au*  'atp<7-h'iiay-i'';  S  /6  aE., 306,  Hbm.  ZDMG.  jö.  133.  AGr.  r.  109.  Füv KZ.  35.  19,  Bgm.  Crdr."  /.  858,  860.  (Falsch WZKM.  S.  182.)  —  mp.  ottBär,  np.  ni-.-ät.  — ')  Vgl.

182 ::   Form  des  Adjektivs  er- Y.  44,20;  —  negirt:  västry3t  vä  . .  yl  scheint  das  Neutr.  im  Sing.;  A)llimAp.: vä  nSii  aahat  väslryl  Y.3i.<).  PPA.:  kär<^  ..hyt^  up3  mäm  äha'' haur  kamnam dr.'gvä  ..  duiazöbä  hqs  ..  ahsmustd (^.)\ .  (sd.)  ähc^  Bh.2  6.  B)im  Aw.(?J:  kl.. 46.  j^;  —  vTa rS  (sd.)  hqs  tat/rS  ..  mruylt  lylxmanyata  ap?r;nlyu  ahmt  n''it  p3r^ Y.4i$.  5;  47-4>  J'-Si  —  ^pö  mä  isttm  nJyu yesi  baväni pjrftiäyu(sd).\t.ip.^zQ)'> apayantä  (sd.)

337 :: imä  nämSnJs  "so  lauten  die  Namen" Vt  /.  15;  75.  49;  —  Hsca  caraitis  ahi yqm  ..  H.2.  io(?).  Anhang.  Ellipse ist  anzunehmen  für  gAw.:  vaidä  tat  ya ahmT  .  ,  anales  (sd)  tna  kamnafsva  (sd.) hyatlä  iamnänä  (sd.)  ahmT  "ich  weiss  das, weshalb  ich  , .  nichts  vermag;  nur  wenig Herden  sind  mein,  (deshalb  ist  es  so) und  weil  ich  nur  wenig  Leute  habe"  Y. 46. 2.  C)  In  der  Bedeutung  unsres 'auch';  ca  folgt  dem  angeknüpften  Satz- teil, bz.  des

382 ::   /ravartii hadä  kamnaibis  *asbäribis  .  .  asiyav^ fasavc^  adam  käram  fraiiayam  'yai{s^ Ait]ii.)paliy  ".  .  drauf  Üess  ich  ein  Heer gegen  sie  marschiren"  Bh.  2. 1 3 ;  —  hauv kadä  kamnaibii  *asbSribis  aiiyavi^  .  , pasäv<^  vivant^  hadä  kärä  nipadiy  (sd.) "yaiy  (als  Akk.)  aliyavt^  Bh.  ^.  1 1 .  a)  mit folg.  *Hy(^kara-  (sd.)  'wenig  zahlreich': *yadipatiy  *mamyähay  'yJ*  Hyt^karam *ava  dahyävJ'  . .  D.6. 4.  ASn.  tyO* als  Konjn.  sbes.         Vgl  zu.  

614 ::   AizvB  rai^lm  (sd.) stsi  makya  Y.50. 6;  —  vahistä  mahyh is'IBii  Y.46.1S;  50.9,  44-io;  —  mahmi manSi  (sd.)  Y.  J2.  i ;  —  inai^ä  (sd.)  mayä (ISf.)  Y.j^.9.  b)  pracdik.:  »«i(NPn.) kamnafhä  (sd.)  Y.  4Ö.  2.  [Y.  ^.  1 2 :  lies ali>mahyä^ Ableit  aus  ■ma..  —  gr.  vgl.  iftii.  —  Fü-: (i^  man,  am,  (lu  Y.  _y ) :  pa  falmäit. •  g,  maekant-  Adj.  (fem.  'iainil-)  'hervor- ^ckemd,  quellend':  aps ..  "kainttscä  *ksba- vaintlscä  fravasaahs  "die  hervorquellen-
```


## [2026-09-06T15:46:01.910Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'kambi\\|kamna-  *Adj\\|kamnä' BRT.txt | head -10; echo \"=== leaves 225-245 headwords ===\"; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in range(224,236):\n    print(n, repr(t[n][:120]))\nEOF",
 "description": "Search Bartholomae for kambišta"
}
```


### [2026-09-06T15:46:03.708Z] TOOL RESULT

```
2714:klm  CASn.)'*  vä  bimlhlm  V3  "wenn  eine  I  so/ti  .  .  xsayamna  is.lna  (VPm.)  Y.  O5. Frau  in  die  Schwangerschaft  kommt  — 114.  4)  'haben  zu  — '  sva.  'verpflichtet einen  Monat  lang '>  oder  zwei  . ."  V.  5.45.  j  sein  zu -,  sollen',  mit  Inf.:  lii'a  dim  nara tm\A.s.>inieiJasa.mahya:-^rä.:ivotmä/iai.\i^gl-s^fi)  apa.skambim   (sd.)     vXcicaE^a
6646:gAw.  (die  Kopula  hat  keine  feste  Stelle;  uldäta  (s.  ß)  . .  uzdahyamna  .  .  aiwi.va^^a- besooders  häu5g  tritt  sie  als  letztes,  sei-  yamna  .  .  aiaii.vap;ayanta  (sd.)  , .  kunvana tener  als  vorletztes  Wort  des  Satzes  auO'":  (sd.)  ..  fiaesyania'Vi.g.^;  —  mtzdim  yat vaidä  tal  yä  ahml  ..  analJU  (sd.)  ..  zaota  hanayamttS  aftha'^ .  ^g.y^; — yiwii kyalca  kamnänä  (sd.)  ahmJ  Y.46.1;  — '  (sd.^  .  .  *gaii  asrävayi  kyal  (Opt.)^' at  vS  staota  aojäi  (sd.)  .  .  anhäcä  Y.jo.  aia  .  .  N.  ^;  42;  —  negirt:  mit  nä 11;  —  hai'iyBjval'ä  ,  .  dngväiti  .  .  at  pourS^  (sd.)  dr3gi-at5  hylf  cixlnus)  Y.  4$. aiauns  rafonJ  hySm    aojönghvat  Y.^j.  8;    15.  ß)  PPfP.;  A)  D  im  Ap.:    utsmaiy
15197:•  j-,  g.  pa9ä-  f.  'Pfad,  Weg':  ■■^?«  x'ä- sijt/lm  (sd.J  Ny.  /.  8;  —  '>ajS  s^äsmayj FrW.5. 1 ;  —  catanrü  ptr^rA  (sd.)  vi'iiira- ysis  avi  ''i:qm  katarasät  YL74;.44;  — äat  yasp  'iws  .  .  ''iqm  jasäiti  vq'kwafsö "wenn  zu  dir  an  den  Weg  herankommt (sva.  dir  in  den  Weg  tritt)  ein  Strauch- dieb" Yt  13.  2o;  —  hat  ta  '"ha  frayqn pasvqm  vä  . .  "sollen  diese  Wege  be- gehen .,?"  V.  A'.  14;  15,  ig,  23; —  iiiritim taaa  aitä  'ha  vlvä'iayaritu  .  .  spätem  V, iV.  16;  17,  18;  — yi  ■  ■  kambist}mca  atte ''i:a  frayqn  pasvasca  .  .  V.j.is; — hu^a ,  .  aiaonqm  "'ia  (NS.?)  .  .  ku%a  Jrjatqm Yt4.4.  '  a)  AS.  mit  V.  d,}-  und  Inf. '(Jemandem)  den  Weg  freigeben,  es  (ihm) freistellen  zu  — ">:  hyat  aßyäi  dada  -^qm Tiis/ryiil  vä  äi/i(sd.)  "als  du  es  ihm  (dem Rind)  freistelltest  .  .  zu  .  ."  Y.  31.  9.
15320:ttL  pptali,  pptiti  i  np.  anb^rad  'er  füllt  ein'.  — Pü.(iuV.3^:  ampa  diänpurr  kambärel kämak, (zu  P.):  ka  . .  kambärel,  erl.:  kuS  .  .  kart,  (lu V.  v)!  ke  pa  göit  unAwar  ö  kam  kambitit istel,  erl.!  jfr.  —  >)  la/raJ.äp-.  fra-  ist  Koinp- Form  zu  einem  al,  *purä-li.  —  »)  Them.;  ai, pfna.  —  i)  Hds.  p/rf.  —  4)  Them.
17494:'am  meisten'",  nach  Zahl,  Menge,  Um- fang usw.:  mq%raväkahe  .  .  yS  'Um  . . a/irmairyanqm  (Gen.  part  als  Obj.) . .  ava.- jaynat  Yt  1^.105;  —  yat  ba  paiti  'hm kärayeiti  .  .  yavanqnüa  västranqtnca  (sd,; Gen.  part  als  Obj.)  V.  3.  4;  ~  yat  bä paiti  't»m  viksnte  .  .  girihqm  (Gen.  part als  Obj.)  V.J.  22;  —  ya^  b3  paiti  'tim bavainü  .  .  g^rjiqm  (Gen.  Flur,  als  Subj.) V.J.  10;  —  yat  bä  paiti  't)m  malsmti pasvasca  , .  V._j.  6;  —  yat  bä  paiti  °t»m us.zlZ3nti  (sd.)  pasvasla  V,_j,  5;  — yat  bä paiti  'tim  daxma  usdaüa  (sd.)  kiryänte V.J.9;  13;  —  yat  bä  paiti  Uim  lairi nikantt  V.  j.  8;  —  yat  ba  paiti  "tsm uskfnti\.3.i2;  —  yS  't>m  apivataiU  dag- nayh  V.  g,  3.  a)  zur  Verstärkung  des Superlativs  '* :  yai  ahmi  nmäne  . .  'ttm yaozdätU.B3mö.t»n3mca  hu^ö.z3mS.t3m3mca kambistitnla  .  .  V,  5.  46^',
18688:38,  g.  2, 13.23,  75.  2,  Vr. 77. 3,  16.  I,  7&1, ig.i,  23.1,  \.i2.y,  ig.s,  V.23,  Yt^.3*, 6^  Vyt  75,  FrB.;  — kambist?mca  aäe  pa%ä frayqn  pasvasca  slaoraca  atnmca  . .  bargs- maca  .  .  nar^mca  (statt  Nora.)  yim  aia- vamm  V.3. 15;  — yal  ba  paiÜ  . .  naire asaone  v?r?zyat  asaya  da^äiti  V.J.  34;  5. ao,  iS.aS,  34' 37,  Yt 7^.153,  *N.S4"\ Y.ig.  17,  \t.iS.  i; — yüi  anhan  ninbyS osavabyB  ayapts.dät?masca  .  .  P.  45i  V.  ff. 43.  ^4.6,  IS,  YtÄii  («^rajö)**),  jo.  55 («««yj)''',  _J.  4  (ii»nysy''>;  —  yS  narS asaonö  urva  H.  2.  7,  8,  10,  ij*;  Y./5.8, 27.3,  60.  y,  —  ahe  nar^  alaons  frava- s'im  .  .  yS  asmSj^anvä  ttqma  Yt.  /.  30;  — narl  asaons  iririhusS  Y.3.40  PUZ.;  — dama  mazdayasnis  nars  aSaoTlB  framgrp- zaiti  vispim  duSmatsmca..  V.^J.  42;  7.  44;
19136:issihe .  .  upa-skambim  (sd.)  vlHcaehia  dim paiti  aiäka  z?m!l  nid'  V.8.  lo.
21237:(sd.)  dngvanhm  avS  Y.32, 14;  —  täis  zl nä  /yao^anai/dyentf(sd.)..Ay  ('insofern') as  *aojS.  näidyankifn  (sd.)  Y.^J^.  8;  — vaidä  tal  ya  aAml . .  anaisö  tnä  kamna/svä hyatcä  (Sp.  574  o.)  kamnäna  aAmX  Y. 46.3;  —  parstim  zl  %wa  yohanä  tat )mavatqm{sA.)  Ay  {'■<Nt)[')%wä  x^ayqs{5i) alitm  dyat  imavantim  Y.43, 10.  b)  im jAw.:  atcit  bä  lumS  Aaomai  y'  ('weil') vupe  anye  tnatävAs  ailma  Aacinte  Yt  //.  5 ; Y,  /0. 1 3 ;  —  avat  vayul  ba  nqma  aAmi y  »va  dqma  vayemi  Yt  i^.  43;  43f-^;  — aojists . .  y  dim  upanAacat . .  Aqm.vanitts Yt/p.  38f.;  —  aom  ofarmB  AangSurva- yata  . .  ^raltaond .  .y  as . .  vftT^ravastTtnB Yt/5.36;  38;  —  bawraini  vasfrä  vajtAata ,,y  asti  bawris{sd.)  sraiita  Yt.5. 129;  — wn'^rayriB  ..  nBil ..  yanyB  (sd.)  vaAmyB .. y  nürjm  .  ,  dafvayäsS  voAunim  va  taca- yänti  . .  Yt  J^  54;  —  ^banhvB  va  patU vajaanaAe  .  .  y  alta%a  *Aanjastlnte  pouru gaonaAe  (sd.)  u%aheca  N.  65.  IV)  die Folge  oder  den  Zweck  angebend  'so  dass; auf  dass,  damit';  a)  im  gAw.;  1)  mit dem  Praeteritum;  Ayatis.!!!)  ji 3.dibaomä (sd.)  .  .  upa.jasat  Ay  ('so  dass')  vtrstmtä (sd.)    aciitim    manB   Y. 30.(1.  2)    mit
24586:•  j.  vizvärant-  Adj.  'tüchtig,  geschickt' {?): dva  dim  nara  isSi'ie  vJzSislam  (sd.)  'rynlqm . .  ufajkambim  (sd.) . .  mdai^yan  V,  8.  1  o.
=== leaves 225-245 headwords ===
224 ".  arazvan-  Adj.  'gerade  gerichtet'  sva, 'die  Richtung  einhaltend,  nicht  abirrend, ohne  Fehl':  ta  ns  data  l"
225 'asivä (sd.)  (isla  Y.j/.s",\nPü.:  Tüsl  ml,  Sü.:  salyena  ladauruh.^  ■)  Vgl.\n•  j.  araz-UxÄa-  Adj.:  s.  unter  a'
226 "dj.  (fem.  '■faiiti-)  'Spangen\nan    den  Füssen    tragend':    al^m  kaitiinö\naijhfnte  'paiiii' (NFf.)  urvizö.mai'"
227 'erührung  kommt"  V. /6\'.7*>.  3)  \'teil- haftig werden,  sich  teilhaftig  machen\',  mit |Gen.;  nSit  dva  nSit  irayS'
228 ',  E.  —  Zum  V.  qz-.  —  ai.  dniAas-  a.\n—  PQ.:    langlA,  Sü.    (lU  Y.  8):    näslihyam.  —\nI)  zF.  s.  S  3S'
229 'vd  darrja  akarsta  saaa  ..  \'6a  i\'amiti  .. ila  sadayäj  ya^  "Sa  ..  pdo?m  vamaite\'^.yä  darrja  apu\'^ ra  *a?i('
230 "indekl.):  (/ranrase  ..  ayqm daoPirim  daomnS)  i°  i^a  ya^na  ahmäi Yt.i^.57;  —  i' i^a  ya^na  ahmäi  ai>ae%a i^a "
231 "s  'mam  sqm  äca  pairi^a bväva  Yt/j.  a;  153;  —  ava  raoffi  .. -mam  zqm  Yt  10.85,  89;  H./.  16;  —  'ms raoc"
232 ' maitä  kartam par\'iavaiy  "das  (wars),  was  ich  in  P.  tat" Bh,_y. 2;  4,  12,  2.15,  4-^;  —  in  Kon- gruenz mit'
233 "V.  SJ-  T.  B.  -.r'iyy  mit  vi.\n•  j.,  g.  ira-  n.  i)  'Anlauf;  Aa^cilCi /rava- says . .  ya  * afrö.urvisvat  (s"
234 '  (sd.)  andrSng  ". .  welche .  .  den  Wunsch  der  Frommen  bildend (sva.  von  den  Frommen  ersehnt)  . ."  Y. SO.'
235 'i.  191, Gdn.  KZ.  jo.  5 16,  Ludwig  ABoehmGW.  iSijn. 63,  Bthl.  Stud.  /.  133,  Leuuahn  EtWb.  36, Uhlenbeck  WA'
```


## [2026-09-06T15:46:16.365Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E '.{120}kamna.{160}' BRT.txt | grep -i -E \"wenig|Adj|Komp|Sup\" | head -10",
 "description": "Fuzzy search Bartholomae kamna headword"
}
```


### [2026-09-06T15:46:16.428Z] TOOL RESULT

```
11082: ahi yqm  ..  H.2.  io(?).  Anhang.  Ellipse ist  anzunehmen  für  gAw.:  vaidä  tat  ya ahmT  .  ,  anales  (sd)  tna  kamnafsva  (sd.) hyatlä  iamnänä  (sd.)  ahmT  "ich  weiss  das, weshalb  ich  , .  nichts  vermag;  nur  wenig Herden  sind  mein,  (deshalb  ist  es  so) und  weil
```


## [2026-09-06T15:46:24.266Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c '' BRT.txt; grep -n -E '^\\s*[•*]\\s*[jgp]\\.?,?\\s*(g\\.)?\\s*kam' BRT.txt | head -20; echo \"---alt---\"; grep -n -o -E '[•*]\\s*[jgp][.,]?\\s*(g[.,])?\\s*kam[a-zäöü]*-' BRT.txt | head -20",
 "description": "Search Bartholomae k- headwords"
}
```


### [2026-09-06T15:46:24.437Z] TOOL RESULT

```
30725
22338:•  j.  kameit  vä  vaxii§^m  N.57:  -?-. Als  Zitat  bezeichnet;  l'ü.:  fehlt.
24775:•  j.  kamcit  Vä  "rae^Twanam  Yt.  4.  5  ". O  Ofrenbär  verderbte  Anleihe  aus  Yt  //.  5, wo  ari&iwyannm.     Fehlt  in  Fl.
---alt---
```


## [2026-09-06T15:46:32.410Z] TOOL CALL #33: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%85\" \\\n \"https://en.wiktionary.org/wiki/kamna\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kamnah\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D9%86%D9%87\" ; do\n echo \"##### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 238, root Kamma/Quomn/Sqombh-no: Persian kam, kamin, kamina; OP/Av kamna-' 2>&1 | tail -5\ndone",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-06T15:46:37.183Z] TOOL RESULT

```
##### https://en.wiktionary.org/wiki/%DA%A9%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/506f01423cb675ee.txt
##### https://en.wiktionary.org/wiki/kamna
/home/sfmqrb/git/rishe/data/verification/sources/web/f596f0e278085729.txt
##### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kamnah
/home/sfmqrb/git/rishe/data/verification/sources/web/6e51da24856f83da.txt
##### https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D9%86%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/149988ecad0207ef.txt
```


## [2026-09-06T15:46:40.120Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 506f01423cb675ee f596f0e278085729 6e51da24856f83da 149988ecad0207ef; do echo \"===== $f\"; head -c 3000 $f.txt; echo; done",
 "description": "Inspect archived Wiktionary text"
}
```


### [2026-09-06T15:46:41.882Z] TOOL RESULT

```
===== 506f01423cb675ee
URL: https://en.wiktionary.org/wiki/%DA%A9%D9%85
FETCHED: 2026-09-06T15:46:35Z
STATUS: 200
TITLE: کم - Wiktionary, the free dictionary

کم - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Pahari-Potwari 

 Toggle Pahari-Potwari subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 1 

 2.1.1 
 Pronunciation 

 2.1.2 
 Adjective 

 2.1.2.1 
 Usage notes 

 2.1.2.2 
 Derived terms 

 2.1.2.3 
 Descendants 

 2.2 
 Etymology 2 

 2.2.1 
 Noun 

 2.2.1.1 
 Derived terms 

 2.3 
 Etymology 3 

 2.3.1 
 Pronoun 

 2.4 
 References 

 3 
 Punjabi 

 Toggle Punjabi subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 3.4 
 Further reading 

 4 
 Southwestern Fars 

 Toggle Southwestern Fars subsection 

 4.1 
 Noun 

 5 
 Urdu 

 Toggle Urdu subsection 

 5.1 
 Etymology 

 5.2 
 Pronunciation 

 5.3 
 Adjective 

 5.3.1 
 Derived terms 

 5.4 
 Adverb 

 5.5 
 Determiner 

 Toggle the table of contents 

 کم 

 11 languages 

 Deutsch 
 فارسی 
 Na Vosa Vakaviti 
 Magyar 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 
 پنجابی 
 سرائیکی 
 Тоҷикӣ 
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

 See also: كم and گم 

 Pahari-Potwari
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Prakrit 𑀓𑀫𑁆𑀫 ( kamma ) , from Sanskrit कर्म ( karma ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /kəmːᵊ/ 

 Noun
 [ edit ] 

 کَمّ ( kamm )  m 

 work , job , task 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 Etymology tree

 Proto-Indo-Iranian *kambʰ- 
 Proto-Iranian *kamb- 
 Proto-Iranian *kam(b)-na- 
 Middle Persian 𐭪𐭬 ( km /⁠kam⁠/ ) 
 Persian کم 

 Inherited from Middle Persian 𐭪𐭬 ( km /⁠kam⁠/ , “ little, small ” ) , [ 1 ] from Proto-Iranian *kam(b)-na- ( “ small ” ) , from *kamb- ( “ small ” ) , from Proto-Indo-Iranian *kambʰ- ( “ few, small, insignificant ” ) . Probably further related to Proto-Indo-European *ken- ( “ to arise, begin; new, fresh ” ) . [ 2 ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈkam/ 

 ( Dari, formal ) IPA ( key ) : [kʰäm] 

 ( Dari, formal
===== f596f0e278085729
URL: https://en.wiktionary.org/wiki/kamna
FETCHED: 2026-09-06T15:46:36Z
STATUS: 200
TITLE: kamna - Wiktionary, the free dictionary

kamna - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Czech 

 Toggle Czech subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Declension 

 1.3.2 
 Related terms 

 1.4 
 Further reading 

 2 
 Slovene 

 Toggle Slovene subsection 

 2.1 
 Noun 

 Toggle the table of contents 

 kamna 

 9 languages 

 Čeština 
 Dansk 
 Deutsch 
 Suomi 
 Français 
 Lëtzebuergesch 
 Malagasy 
 Polski 
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

 Czech
 [ edit ] 

 Czech Wikipedia has an article on: kamna 

 Wikipedia cs 

 Etymology
 [ edit ] 

 Borrowed from Italian camino .

 Pronunciation
 [ edit ] 

 IPA ( key ) : [ˈkamna] 

 Hyphenation: kam‧na 

 Noun
 [ edit ] 

 kamna   n   pl ( relational adjective kamnový , diminutive kamínka ) 

 stove , heater 

 Declension
 [ edit ] 

 Declension of kamna ( pl-only hard neuter reducible )

 plural

 nominative

 kamna 

 genitive

 kamen 

 dative

 kamnům 

 accusative

 kamna 

 vocative

 kamna 

 locative

 kamnech 

 instrumental

 kamny 

 Related terms
 [ edit ] 

 kamnář 

 Further reading
 [ edit ] 

 “ kamna ”, in Příruční slovník jazyka českého (in Czech), 1935–1957 

 “ kamna ”, in Slovník spisovného jazyka českého (in Czech), 1960–1971, 1989 

 “ kamna ”, in Internetová jazyková příručka (in Czech), 2008–2026 

 Slovene
 [ edit ] 

 Noun
 [ edit ] 

 kámna 

 inflection of kámən : 
 genitive singular 

 nominative / accusative dual 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=kamna&oldid=91097574 "

 Categories : Czech terms derived from Italian 
 Czech terms borrowed from Italian 
 Czech terms with IPA pronunciation 
 Czech lemmas 
 Czech nouns 
 Czech neuter nouns 
 Czech pluralia tantum 
 Czech hard neuter nouns 
 Czech nouns with reducible stem 
 cs:Home appliances 
 Slovene non-lemma forms 
 Slovene noun forms 

 Hidden categories: Czech entries referencing missing etymons 
 Pages with etymon 
 Czech entries with etymon 
 Czech entries with etymology texts 
 Pages using etymon with
===== 6e51da24856f83da
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kamnah
FETCHED: 2026-09-06T15:46:36Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
===== 149988ecad0207ef
URL: https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D9%86%D9%87
FETCHED: 2026-09-06T15:46:37Z
STATUS: 200
TITLE: کمینه - Wiktionary, the free dictionary

کمینه - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Persian 

 Toggle Persian subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Adjective 

 1.4 
 Noun 

 1.5 
 Pronoun 

 1.5.1 
 Usage notes 

 Toggle the table of contents 

 کمینه 

 3 languages 

 فارسی 
 Kurdî 
 Malagasy 

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

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: بیشینه و کمینه 

 Wikipedia fa 

 Etymology
 [ edit ] 

 From کم ( kam ) +‎ ـینه ( -ine ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ka.miː.ˈna/ 

 ( Dari, formal ) IPA ( key ) : [kʰä.miː.ná] 

 ( Dari, formal ) IPA ( key ) : [kʰä.miː.ná] 
 ( Kabuli ) IPA ( key ) : [kʰä.miː.ná] 

 ( Hazaragi ) IPA ( key ) : [kʰä.mi.ná] 

 ( Iran, formal ) IPA ( key ) : [kʰʲæ.miː.né] 

 ( Tajik, formal ) IPA ( key ) : [kʰä.mi.ná] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 kamīna

 Dari reading ? 

 kamīna

 Iranian reading ? 

 kamine

 Tajik reading ? 

 kamina

 Audio ( Iran ) : ( file ) 

 Adjective
 [ edit ] 

 کمینه • ( kamine ) 

 ( archaic ) superlative degree of کم ( kam , “ few ” ) : the least 
 Synonym: کمترین ( kam-tarin ) 
 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume I, verse 58: کای کمینه بخششت ملک جهان
من چه گویم چون تو می‌‌دانی نهان k-ay kamīna baxšiš-at mulk-i jahān
man či gūyam čōn tu mē-dānī nihān [Saying,] "O Thou whose least gift is the empire of the world, what shall I say, inasmuch as Thou knowest the hidden thing? 

 Noun
 [ edit ] 

 کمینه • ( kamine ) 

 ( mathematics ) minimum 
 Antonym: بیشینه ( bišine , “ maximum ” ) 

 Pronoun
 [ edit ] 

 کمینه • ( kamine ) 

 ( humble , archaic ) I , me ; this humble one 
 Synonyms: کمین ( kamin ) , بنده ( bande ) 

 Usage notes
 [ edit ] 

 Sometimes, women used کمینه ( kam
```


## [2026-09-06T15:46:52.375Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '45670,45700p' POK_full.txt; echo \"=== page ===\"; awk 'NR>45690 && /^Page\\(s\\)/ {print NR\": \"$0; exit}' POK_full.txt",
 "description": "Check Pokorny ken- entry"
}
```


### [2026-09-06T15:46:54.016Z] TOOL RESULT

```
With Indo Germanic tr. Gothic d/s-hn/upan ^ tear' , dishnupnan^ become torn ', Old 
Swedish n/upa 'n\p, pinch'. Old English a-hneopan' pick '; with intensive consonant- 
doubling Norwegian Dialectal n uppa ^ p\uck' , Old English hnopp/an ^p\uck', Danish Middle 
Low German noppe "flock, tuft of wool, Hechelhede '; 

with Indo Germanic b^: Old Icelandic hnyfiir short, blunted horn, lamb with such horns ', 
ndd. nobbe, nubbe^i\ock, tuft of wool'. Middle High German noppe, nop' Tuchflocke ' 
(rather loanword from Middle Low German noppe). 

5. 5-extension: Latvian /r/75Js/5 "small mosquito ' (as knisis, fen /s//s irom the /-basis). 

References: WP. I 392 ff., WH. I 217 f., 11166 f. 
Page(s): 559-563 



Root / lemma: ken-3 

Meaning: to appear, be born; to begin; young 

Material: Old Indie kamna-^ young ', compounds Sup. kanlyas-, kanistha-, kanistha-, 

kanya. Gen. PI. kanTnam {o\6er n-stem) "girl', Avestan ka/ne, kaim-, kainJn- ds.; 

gr. Kaiv6(; ' fresh, egregious '; 

Latin /'ece/75 "fresh, young, new', actually " lately arisen, not long in existence, fresh, 
young, recent '; 

Middle Irish cinim^ rise, puff up, originate ', c/n/ud^ gender, sex, stem, line '; Old Irish 
=== page ===
45720: Page(s): 563-564
```


## [2026-09-06T15:46:54.880Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -o 'Reconstruction:[A-Za-z-]*/[^ ]*' 506f01423cb675ee.txt | sort -u | head -20; echo \"--- refs section ---\"; sed -n '/2.4/,$p' 506f01423cb675ee.txt | grep -n -A3 -i 'MacKenzie\\|Hasandust\\|References' | head -40",
 "description": "Extract reconstruction links and refs from Wiktionary kam"
}
```


### [2026-09-06T15:46:56.662Z] TOOL RESULT

```
--- refs section ---
2: References 
3-
4- 3 
5- Punjabi 
--
314: References
315- [ edit ] 
316-
317- ^ Nourai, Ali ( 2011 ), “Kamma, Quômn, Sqombh-no”, in An Etymological Dictionary of Persian, English and other Indo-European Languages , page 208
```


## [2026-09-06T15:47:04.479Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '310,330p' <(sed -n '/2.4/,$p' 506f01423cb675ee.txt) ; echo \"=== grep etymology tree/desc ===\"; grep -n -B2 -A25 'Inherited from Middle Persian' 506f01423cb675ee.txt | head -60",
 "description": "Read Wiktionary references and descendants"
}
```


### [2026-09-06T15:47:06.370Z] TOOL RESULT

```
 کم • ( kam ) 

 ( dialectal , Khesht , Konartakhteh ) alternative form of کدام ( kodâm , “ which ” ) 

 References
 [ edit ] 

 ^ Nourai, Ali ( 2011 ), “Kamma, Quômn, Sqombh-no”, in An Etymological Dictionary of Persian, English and other Indo-European Languages , page 208 

 ^ Edelʹman, D. I. ( 2011 ), “*kamb- : kab-, *kambna- : kabna-”, in Etimologičeskij slovarʹ iranskix jazykov [ Etymological Dictionary of Iranian Languages ] (in Russian), volume 4, Moscow: Vostochnaya Literatura, page 193 

 Punjabi
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Prakrit 𑀓𑀫𑁆𑀫 ( kamma ) , from Sanskrit कर्म ( karma ) .

 Pronunciation
 [ edit ] 
=== grep etymology tree/desc ===
263- Persian کم 
264-
265: Inherited from Middle Persian 𐭪𐭬 ( km /⁠kam⁠/ , “ little, small ” ) , [ 1 ] from Proto-Iranian *kam(b)-na- ( “ small ” ) , from *kamb- ( “ small ” ) , from Proto-Indo-Iranian *kambʰ- ( “ few, small, insignificant ” ) . Probably further related to Proto-Indo-European *ken- ( “ to arise, begin; new, fresh ” ) . [ 2 ] 
266-
267- Pronunciation
268- [ edit ] 
269-
270- ( Classical Persian ) IPA ( key ) : /ˈkam/ 
271-
272- ( Dari, formal ) IPA ( key ) : [kʰäm] 
273-
274- ( Dari, formal ) IPA ( key ) : [kʰäm] 
275- ( Kabuli ) IPA ( key ) : [kʰäm] 
276-
277- ( Hazaragi ) IPA ( key ) : [kʰäm] 
278-
279- ( Iran, formal ) IPA ( key ) : [kʰʲæm] 
280-
281- ( Tajik, formal ) IPA ( key ) : [kʰäm] 
282-
283- Rhymes: -am 
284-
285- Readings
286-
287- Classical reading ? 
288-
289- kam
290-
```


## [2026-09-06T15:47:18.201Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC kamma ==\"; grep -n -E '^kamm|kamma[- ]' IEC.txt | head -10; echo \"== SYN ==\"; grep -n -i 'kamna\\|kambist' SYN.txt | head -10; echo \"== AHD watkins ==\"; grep -n -i 'kamna\\|skembh\\|skomb' AHD_watkins1985.txt | head -10; echo \"== KLN ==\"; grep -n -i 'kamna' KLN_1966.txt KLN_1971.txt | head -5; echo \"== CHEUNG ==\"; grep -n -i 'kamna\\|kamb-' CHEUNG.txt | head -10",
 "description": "Grep Mann, Buck, Watkins, Klein, Cheung"
}
```


### [2026-09-06T15:47:18.319Z] TOOL RESULT

```
== IEC kamma ==
== SYN ==
11983:ae ON arinn, Dan. arne : Lat. Gra, 7. Skt. agnikunda-, cpd. of agni- oe asi- ‘altar’ (orig. ‘fire- | ‘fire’ and kunda- ‘pot, vessel for coals’, : G ! ie BS. dry’, Grk. dtw ‘dry | is used of a receptacle for the sacred eect - 4290 ‘ashes’, etc., IE *ds-. | fire, but there is no word for a household Melt, KZ. 46.315. Falk-Torp 33. fireplace. Bt be, 7.32 STOVE ry TOs, Depud it wkorpa (lit 2) Goth, ..., Lith. kakalys, krosnis, pe- : mus, fornax hes HIQN (ofr) gus It inus 7 a- Dan. —_kakkeloun Lett. krasns y  ufa Sw. — ugn, kamin GhSLtes/2 . Potle (fourneau) OE (ofen) SCr.  peé Rim, 4/4, hornitlo ME (oven) Boh. kamna Te tobe NE stove Pol. _——piec Nin, {ornn) Du. kachel Russ. pet’ V, - OHG (ovan) Skt.  (aemanta-, culli-) Rad, MHG oven Av forniget NH G afer a mieten
11995:4. Lat. caminus ‘forge’, etc., also used for heating a room (7.31). Hence, be- sides words for ‘fireplace’ (7.31) or ‘chimney’ (7.33), also some for ‘stove’, as It. camino mostly ‘cookstove’, Sw, kamin ‘iron stove’, Boh. kamna ‘stove’.
22551:5. ON skam(m)r, OHG skammeér, be- side OHG hammér ‘mutilated, feeble’, perh. fr. *(s)kap-mé- : Grk. oxarrw ‘dig’, xor7w ‘strike, cut off’, ete. Walde-P. 2.560. Or fr. *skambh-no- : Av., OPers. kamna- ‘small’ in quantity or number? Walde-P. 2.601. Falk-Torp 1003.
23597:$Alyos (wadpos) Goth. leitil; fawat Lith. maz ddl yos ON litill; fair Lett. maz ,  parvus; parce Dan. __lidt (sb.); faa ChSl. malo poco Sw. litet (sb.); fd SCr. malo . peu de OE lytel; feawe Boh. mdlo poco ME litel; fewe Pol. mato Rum, pujin NE little; few Russ. malo .  becc, terc; uath, wa- Du. weinig Skt. —_alpa- thad, terc OHG  luzzil; luzzil, fohe Av., OPers. kamna- beagan, beag; beag, MHG lhiitzel, wénec learc NHG~ wenig ychydig nebeud
23618:Av., OPers. kamna- ‘little’ in amount (Av.) or number (OPers. of an army), OPers. pl. ‘few’ (hada kamnaibi¥ marti- yaibis ‘with few men’; cf. also Av. cpd. kamna-nar- ‘having few men’), NPers. kam ‘little, few’, fr. *kambna- (cf. Av. kambistam superl. adv. ‘least’), prob. : OHG hammer ‘mutilated’, ON skammr ‘short’, etc. Walde-P. 2.601.
== AHD watkins ==
== KLN ==
== CHEUNG ==
22527:put, build’ || (+ *pati-) Pash. pecumai ‘acclivity’ || (+ *ui-) Sh. wixkamb-/wixküvd, 
22528:Rosh. Xikamb-/Xikavd, Ishk. uskomb-/uskovd ‘to sort, tease wool with the hands’, 
48172:wixkamb-/wixküvd, 
48937:Xikamb-/Xikavd, 344
```


## [2026-09-06T15:47:20.649Z] TOOL CALL #39: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%F0%90%8E%A3%F0%90%8E%B6%F0%90%8E%B4\" ; do\n echo \"##### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 238, root Kamma/Quomn/Sqombh-no: Persian kamin; Old Persian kamna' 2>&1 | tail -3\ndone",
 "description": "Archive Wiktionary kamin and OP kamna"
}
```


### [2026-09-06T15:47:23.633Z] TOOL RESULT

```
##### https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/3c98def1f4ef6c97.txt
##### https://en.wiktionary.org/wiki/%F0%90%8E%A3%F0%90%8E%B6%F0%90%8E%B4
/home/sfmqrb/git/rishe/data/verification/sources/web/4d586cbbdf02dc82.txt
```


## [2026-09-06T15:47:33.649Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nfor pat in [\"Or fr. *skambh-no-\",\"Av., OPers. kamna- ‘little’ in amount\"]:\n    i=t.find(pat); leaf=t.count('\\f',0,i)\n    print(pat[:30],'leaf0',leaf,'printed~',leaf-24, leaf+1-24)\nEOF\necho \"=== Wikt kamin ===\"; grep -n -A12 'Persian$' /home/sfmqrb/git/rishe/data/verification/sources/web/3c98def1f4ef6c97.txt | grep -n -i -A8 'etymology' | head -40",
 "description": "Locate Buck pages and read Wiktionary kamin"
}
```


### [2026-09-06T15:47:36.507Z] TOOL RESULT

```
Or fr. *skambh-no- leaf0 955 printed~ 931 932
Av., OPers. kamna- ‘little’ in leaf0 999 printed~ 975 976
=== Wikt kamin ===
```


## [2026-09-06T15:47:39.894Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/From Wiktionary/,$p' 3c98def1f4ef6c97.txt | head -80; echo \"#### OP kamna\"; sed -n '/From Wiktionary/,$p' 4d586cbbdf02dc82.txt | head -60",
 "description": "Read Wiktionary kamin and OP kamna entries"
}
```


### [2026-09-06T15:47:41.525Z] TOOL RESULT

```
 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ka.ˈmiːn/ 

 ( Dari, formal ) IPA ( key ) : [kʰä.míːn] 

 ( Dari, formal ) IPA ( key ) : [kʰä.míːn] 
 ( Kabuli ) IPA ( key ) : [kʰä.míːn] 

 ( Hazaragi ) IPA ( key ) : [kʰä.mín] 

 ( Iran, formal ) IPA ( key ) : [kʰʲæ.míːn] 

 ( Tajik, formal ) IPA ( key ) : [kʰä.mín] 

 Rhymes: -iːn 

 Readings

 Classical reading ? 

 kamīn

 Dari reading ? 

 kamīn

 Iranian reading ? 

 kamin

 Tajik reading ? 

 kamin

 Etymology 1
 [ edit ] 

 Persian Wikipedia has an article on: کمین 

 Wikipedia fa 

 Borrowed from Arabic كَمِين ( kamīn ) .

 Noun
 [ edit ] 

 کمین • ( kamin ) 

 ambush 
 c. 1030 , Farrukhī Sīstānī , “Qaṣīda 153”, in دیوان فرخی سیستانی [ Dīvān of Farrukhī ]‎ [1] : از شبیخون و کمین ننگ آید او را روز جنگ
دوست دارد جنگ لیکن بی شبیخون و کمین az šabīxūn u kamīn nang āyad ō rā rōz-i jang
dōst dārad jang lēkin bē šabīxūn u kamīn He is ashamed of night attacks and ambushes on the day of war;
He loves war, but without night attacks and ambushes . (Classical Persian transliteration) 

 Etymology 2
 [ edit ] 

 Adjective
 [ edit ] 

 کمین • ( kamine ) 

 ( archaic ) superlative degree of کم ( kam , “ few ” ) : the least 
 Synonyms: کمینه ( kamine ) , کمترین ( kam-tarin ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=کمین&oldid=87758304 "

 Categories : Persian terms with IPA pronunciation 
 Rhymes:Persian/iːn 
 Rhymes:Persian/iːn/2 syllables 
 Persian terms borrowed from Arabic 
 Persian terms derived from Arabic 
 Persian lemmas 
#### OP kamna
```


## [2026-09-06T15:47:55.367Z] TOOL CALL #42: Bash

```json
{
 "command": "head -8 data/verification/sources/web/4d586cbbdf02dc82.txt; ls site/pages/238.jpg 2>/dev/null || echo \"no site jpg\"",
 "description": "Check OP wiktionary fetch and page image"
}
```


### [2026-09-06T15:47:55.407Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%F0%90%8E%A3%F0%90%8E%B6%F0%90%8E%B4
FETCHED: 2026-09-06T15:47:23Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Foundsite/pages/238.jpg
```


## [2026-09-06T15:47:57.018Z] TOOL CALL #43: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%A9%D9%85/' --note 'page 238: Mo`in/Dehkhoda entry for کم' 2>&1 | tail -3",
 "description": "Fetch abadis for کم"
}
```


### [2026-09-06T15:48:01.513Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2841ebcb65277e76.txt
```


## [2026-09-06T15:48:04.493Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -A6 'معین' 2841ebcb65277e76.txt | head -40",
 "description": "Check abadis Moin section"
}
```


### [2026-09-06T15:48:04.576Z] TOOL RESULT

```
21: کم. [ ک ِ ] ( موصول + ضمیر ) که مرا. که به من. ( فرهنگ فارسی معین ) مخفف که ام. که مرا. ( یادداشت به خط مرحوم دهخدا ) : 
22-بنگه از آن گزیده ام این کازه 
23-کم عیش نیک و دخل بی اندازه رودکی ( یادداشت به خط مرحوم دهخدا ).
24-معذورم داریت کم اندوه وَغیش است 
25-اندوه وغیش من از آن جعد و غیش است. رودکی ( یادداشت به خط مرحوم دهخدا ).
26-نو عاشقم و از همه خوبان زمانه 
27-دخشم به تو است ارچه نه کم خوب بود حال. فرالاوی ( یادداشت به خط مرحوم دهخدا ).
--
67: فرهنگ معین
68-
69- (کُ مّ ) [ ع . ] (اِ. ) آستین . ج . اَکمام .
70- (کَ ) [ په . ] ۱ - (ص . ) اندک ، قلیل . ۲ - (ص تف . ) کمتر، اقل . ۳ - الا، منهای . ۴ - کمیاب ، نادر. 
71-
72- فرهنگ عمید
73-
--
361:فرهنگ لغت معین
362-
363- کم ( کوچک، اندک ) 
364-ریشه هندواروپائی اسکرده - skerdh یا کم و کوچک در فارسی باستان کمن kamna ودر اوستا نیز کمنا ودر سانسکری کوترا kutra شبیه کوتاه در فارسی ودر انگلیسی کرت curt و cut و کارو carve هردو بمعنی بریدن و کوتاه کردن. 
365-کزیده از فرهنگ هند واروپائی زبان فارسی، منوچهر اریانپور.
366-
367- کوسه : به مجاز، کوچک. کم. اندک :
--
424: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
425-
426- لینک ها 
427-
428- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
429-
430- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-06T15:48:04.835Z] TOOL CALL #45: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/238.jpg"
}
```


### [2026-09-06T15:48:04.867Z] TOOL RESULT

```

```


## [2026-09-06T15:48:37.578Z] TOOL CALL #46: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check requirements"
}
```


### [2026-09-06T15:48:37.622Z] TOOL RESULT

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


## [2026-09-06T15:49:00.856Z] AGENT

Now I have everything. Writing the verification file.


## [2026-09-06T15:51:26.502Z] TOOL CALL #47: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-238.json",
 "content": "{\n  \"pdf_page\": 238,\n  \"book_page\": 208,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Kamma, Quômn, Sqombh-no\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Proto-Iranian *kamb-na- / *kab-na- 'small, few' (Edelman, ESIJa IV 193); older IE reconstructions *(s)kombh-no- (Walde-Pokorny II 601) and *kʷomn- (Mann, IEC 1044)\",\n      \"note\": \"The two last elements of Nourai's triple headword are genuine and correctly cited: WP II 601 heads an entry '(s)qombh-no- (*sqambh-no-?) \\\"verkürzt, kurz, verstümmelt, wenig\\\"' whose first witness is 'Av. ap. kamna- \\\"wenig, gering\\\" (*kambhna-)', and Mann IEC col./p. 1044 heads 'quómn- \\\"small; little, few\\\"' with 'Av. kamno', 'OPer. kamna-', 'Per. kam, kamin, kamine' and 'OE hwon'. But the two are RIVAL reconstructions that cannot both be right: WP's has a plain velar *k with s-mobile and a labial aspirate (*(s)kombh-no-, tying kamna- to ON skammr / OHG hamal 'mutilated, short'), while Mann's has a labiovelar *kʷ (*kʷomn-, tying it to OE hwon and Arm. omn). Nourai simply juxtaposes them. The first element, 'Kamma', is not a headword in either cited source and I could not find it in Pokorny, Walde-Pokorny, Mann, Buck or Watkins; it appears to be Nourai's own cover-form (his neighbouring headwords Kamer, Kamp, Kam 1/2 are formed the same way). Two further caveats: (a) Pokorny's IEW (1959), which superseded WP, DROPPED this entry — there is no *(s)kombh-no- there, and Pokorny's p. 929 '(s)kem- \\\"verstümmelt\\\"' (= WP II 560, not 601) keeps only the Germanic material; Watkins/AHD likewise has no such root; (b) modern Iranian etymology (Edelman, Etimologičeskij slovarʹ iranskix jazykov IV 193, s.v. '*kamb- : kab-, *kambna- : kabna-') reconstructs the word only to Proto-Iranian, with the further PIE affiliation left open. The language label 'Indo-European' is therefore over-confident and the gloss 'little, small' is right. Verdict: plausible.\",\n      \"note_fa\": \"سرواژهٔ نورایی سه صورت را کنار هم گذاشته است. دو صورت آخر واقعی‌اند و ارجاع‌ها درست: والده-پوکورنی (جلد ۲، ص ۶۰۱) مدخل «(s)qombh-no-» به معنی «کوتاه‌شده، اندک» دارد که نخستین شاهدش «اوستایی و پارسی باستان kamna- از *kambhna-» است، و مان (IEC ص ۱۰۴۴) مدخل «quómn- کوچک، اندک» دارد با شواهد اوستایی kamno، پارسی باستان kamna-، فارسی kam، kamin، kamine و انگلیسی کهن hwon. ولی این دو بازسازی با هم ناسازگارند: یکی کافِ ساده با s متحرک و «بهـ» می‌گیرد و واژه را با اسکاندیناویایی کهن skammr «کوتاه» می‌پیوندد، دیگری کافِ لبی‌شدهٔ *kʷ می‌گیرد و آن را با hwon انگلیسی کهن هم‌ریشه می‌داند؛ نورایی هر دو را پهلوی هم نشانده است. صورت نخست، «Kamma»، در هیچ‌یک از منابع یادشده و نیز در پوکورنی، باک و واتکینز یافت نشد و ظاهراً ساختهٔ خودِ مؤلف است. افزون بر این، پوکورنی در ویراست ۱۹۵۹ این مدخل را یکسره حذف کرده و ریشه‌شناسی ایرانی امروزی (ادلمان، فرهنگ ریشه‌شناختی زبان‌های ایرانی، ج ۴ ص ۱۹۳) تنها تا ایرانی آغازین *kamb-na-/*kab-na- پیش می‌رود و پیوند هندواروپایی را باز می‌گذارد. پس: ادعای نورایی با احتیاط پذیرفتنی است، ولی برچسب «هندواروپایی» و به‌ویژه صورت «Kamma» پشتوانهٔ منبعی ندارد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%DA%A9%D9%85\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"WLD:601\",\n          \"status\": \"supports\",\n          \"note\": \"Walde-Pokorny Bd. II, printed p. 601 (running head 'sqom- — (s)qut- 601'; local file incoming/WLD/WLD_Bd2_pages.txt line ~39917): '(s)qombh-no- (*sqambh-no-? s. u.) \\\"verkurzt, kurz, verstiimmelt, wenig\\\". Av. ap. kamna- \\\"wenig, gering\\\" (*kambhna-), Superl. av. kambistdm \\\"am wenigsten\\\"; ahd. hammer \\\"Verstiimmelt\\\", mit s- aisl. skammr \\\"kurz\\\"…' — Nourai's 'Sqombh-no' and its gloss come straight from here. Grep pattern: grep -n -i 'kamna' incoming/WLD/WLD_Bd2_pages.txt\"\n        },\n        {\n          \"ref\": \"IEC:1044\",\n          \"status\": \"supports\",\n          \"note\": \"Mann, IEC p. 1044 (local IEC.txt line 14179, leaf 578; the printed number 1044 stands immediately above the entry): 'quómn- \\\"small; little, few\\\". Cf. quón- | Av. kamno, adj. \\\"puny, trivial, bad\\\"; OPer. kamna-, adj. \\\"small, few\\\"; Per. cf. kamin, kamine, adj. \\\"mean, base\\\", cf. kam \\\"few, less, lacking\\\"; OE hwon (variant: \\\"little, few\\\")…' — this is the source of Nourai's 'Quômn' and of the whole chart (root, kamnô, kam, kamîn, kamîne).\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"IEW pp. 918, 929 (POK_full.txt lines 74973-75010, 77785-77800)\",\n          \"stance\": \"contradicts\",\n          \"note\": \"Pokorny 1959 has NO *(s)kombh-no- 'few'. His '(s)kamb- and (s)kemb- \\\"to curve, bend\\\"' (p. 918) and '(s)kem- \\\"disabled\\\"' (p. 929, 'References: WP. II 560') contain only the Greek/Celtic/Germanic material; Av./OP kamna- is not cited anywhere in the IEW (grep -n -i 'kamna' POK_full.txt returns only 'Old Indic kamna-[recte kanīna-] \\\"young\\\"' under ken-3, p. 563-564, an unrelated root). So Pokorny silently dropped the WP II 601 entry Nourai relies on.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, IE roots appendix\",\n          \"stance\": \"silent\",\n          \"note\": \"grep -n -i 'kamna|skembh|skomb' AHD_watkins1985.txt returns nothing; Watkins has no root of this shape, consistent with Pokorny's omission.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck, Dict. of Selected Synonyms, p. 976 (§12.56 'LITTLE, SMALL; FEW') and p. 932 (§12.59 'SHORT')\",\n          \"stance\": \"partial\",\n          \"note\": \"p. 976: 'Av., OPers. kamna- \\\"little\\\" in amount (Av.) or number (OPers. of an army)… NPers. kam \\\"little, few\\\", fr. *kambna- (cf. Av. kambistam superl. adv. \\\"least\\\"), prob. : OHG hammer \\\"mutilated\\\", ON skammr \\\"short\\\", etc. Walde-P. 2.601.' p. 932: 'ON skam(m)r, OHG skammer… perh. fr. *(s)kap-mo-… Walde-P. 2.560. Or fr. *skambh-no- : Av., OPers. kamna- \\\"small\\\"…? Walde-P. 2.601.' Buck confirms the WP II 601 reconstruction but marks it 'prob.'/'or…?', i.e. not certain — and he knows nothing of a labiovelar *kʷomn-.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"kamna, kamnô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both forms are real. Avestan kamna- 'little, few' (nom. sg. m. kamnō — which is exactly Nourai's second form, taken over from Mann's 'Av. kamno') is Gathic: Y. 46.2 kamnafšva- 'having few cattle' and kamnānā 'having few men' (Bartholomae, AiW col. 440, cited so by Nyberg); its superlative is kambištəm 'least' (Vd. 3.15). Old Persian kamna- 'small, few' is attested at Behistun: DB 2.19 kāra … hauv kamnam āha 'that army was a small thing', and instr. pl. kamnaibiš in DB 1.56, 2.2, 2.71, 3.41 (hadā kamnaibiš asabāraibiš 'with few horsemen'). The -mn- of kamna- goes back to *-bhn-: the Old Iranian stem was *kamb-na- / *kab-na- (Hübschmann's *kṃbhna-), the -b- still visible in the superlative Av. kambišta- and in the Manichaean Middle Persian spelling kmb (MacKenzie). Nourai's language label 'Avestan / Old Persian' is therefore right for both languages, and 'little' is the correct gloss.\",\n          \"derivation_fa\": \"هر دو صورت واقعی‌اند. اوستایی kamna- «اندک، کم» در گاهان به کار رفته است (یسنا ۴۶٫۲ در ترکیب‌های kamnafšva- «کم‌گله» و kamnānā «کم‌مرد») و صورت دوم نورایی، یعنی kamnô، همان صیغهٔ فاعلی مفرد مذکر kamnō است که از مان گرفته شده. برترین‌درجهٔ آن در اوستا kambištəm «کمترین» است (وندیداد ۳٫۱۵). پارسی باستان kamna- «کم، اندک» در بیستون آمده: DB 2.19 «hauv kamnam āha»، و صورت بایی جمع kamnaibiš در DB 1.56 و ۲٫۲ و ۲٫۷۱ («hadā kamnaibiš asabāraibiš» با سوارانِ اندک). خوشهٔ mn در این واژه از *bhn دگرگون شده است: ستاک ایرانی باستان *kamb-na-/*kab-na- بوده (بازسازی هوبشمان: *kṃbhna-) و بقایای «ب» را هم در صفت عالی اوستایی kambišta- و هم در املای مانوی فارسی میانه kmb (مکنزی) می‌بینیم. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%85\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:179\",\n              \"status\": \"supports\",\n              \"note\": \"Kent, Old Persian, Lexicon, printed p. 179 (KNT.txt form-feed leaf 201, whose tail carries the printed page number '179'): 'kamna- adj. \\\"small, few\\\": Av. kamna-, NPers. kām (§147.II). kamnam nsn. (as pred. sb. §259) DB 2.19. kamnaibiš ipm. DB 1.56; 2.2, 71; 3.41.' Exactly Nourai's arrow (Av./OP kamna- 'little', continued by NPers. kam).\"\n            },\n            {\n              \"ref\": \"WLD:601\",\n              \"status\": \"supports\",\n              \"note\": \"WP II 601: 'Av. ap. kamna- \\\"wenig, gering\\\" (*kambhna-), Superl. av. kambistdm \\\"am wenigsten\\\"' — the Iranian pair is the head witness of the entry, as the chart shows.\"\n            },\n            {\n              \"ref\": \"IEC:1044\",\n              \"status\": \"supports\",\n              \"note\": \"Mann p. 1044 s.v. quómn-: 'Av. kamno, adj. \\\"puny, trivial, bad\\\"; OPer. kamna-, adj. \\\"small, few\\\"' — the source of Nourai's doublet 'kamna, kamnô'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KNT\",\n              \"where\": \"p. 179 s.v. kamna-\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; Kent also gives the passages DB 2.19 and DB 1.56 etc., confirming the OP attestation.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW col. 440 (not recoverable in the local OCR)\",\n              \"stance\": \"not_found\",\n              \"note\": \"grep -n -i 'kamna' BRT.txt finds only the syntax/quotation sections (asbāray- col. ~211 'hauv … hadā kamnaibiš asbāraibiš aiiyava \\\"…mit wenigen Berittenen…\\\" Bh. 2.13'; and Y.46.2 'kamnafšva … kamnānā ahmī \\\"…nur wenig Herden sind mein… und weil ich nur wenig Leute habe\\\"'). The alphabetical headword kamna- itself is lost in this scan's OCR. Nyberg's glossary cites it as 'Av. (440) kamna-', i.e. AiW col. 440.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck p. 976 §12.56\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av., OPers. kamna- \\\"little\\\" in amount (Av.) or number (OPers. of an army), OPers. pl. \\\"few\\\" (hada kamnaibiš martiyaibiš \\\"with few men\\\"; cf. also Av. cpd. kamna-nar- \\\"having few men\\\"), NPers. kam \\\"little, few\\\", fr. *kambna- (cf. Av. kambistam superl. adv. \\\"least\\\").'\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien no. 865 (p. 88-89) and §153 d (p. 253)\",\n              \"stance\": \"supports\",\n              \"note\": \"no. 865: 'Die drei Steigerungsstufen lauteten im Altpersischen: kamna-, *kanbiyah-, *kanbista- (= zd. kambišta-), vgl. zd. taxma-, tąyah-, tančišta-.' §153 d: 'Idg. bhn = ap. mn = np. m im Auslaut: kam \\\"wenig\\\" = ap. kamna- aus *kabna-, idg. *kṃbhna-, vgl. zd. sup. kambištem.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"kam «کم»; kamîn «کمین» (extra script: کمینه)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP کم kam 'little, few' continues Middle Persian kam [km] 'little, small, few' (MacKenzie, CPD p. 48; Manichaean MP is written kmb, preserving the -b-), from Old Persian / Old Iranian kamna- < *kamb-na- / *kab-na-. The phonetic route is stated by Hübschmann §153 d: Indo-European *bhn > Old Persian mn > New Persian simple -m in final position (kam < ap. kamna-, exactly parallel to nam 'moist' < *namna- < *nabhna-); the cluster was simplified in Middle Persian, where the old superlative survives separately as kamist 'least' (pad kamistīh 'at least') beside the comparative kem 'less, fewer' (MacKenzie pp. 48, 50). Nourai's second word, کمین kamīn 'least', is genuine but is NOT the inherited superlative: the Old Iranian superlative was Av. kambišta- / OP *kanbišta- > MP kamist. NP kamīn / کمینه kamīna are New-Persian-internal superlatives in -īn / -īna, formed on kam exactly like mehīn, behīn, kehīn, bīšīna; they are common in classical verse ('kay kamīna baxšiš-at mulk-i jahān', Rūmī, Masnavī I 58) and, as the chart's Saʿdī line shows (بگذار که بندهٔ کمینم), also serve as a humble first-person 'this least one'. Mann lists precisely 'Per. cf. kamin, kamine' under the same root, so Nourai's arrow is his source's. One caution the chart does not mention: the homograph کمین kamīn 'ambush' is a wholly different word, an Arabic loan (كمين), and must not be confused with this one.\",\n          \"derivation_fa\": \"«کم» فارسی نو دنبالهٔ فارسی میانهٔ kam «اندک، کوچک» است (مکنزی، فرهنگ کوچک پهلوی ص ۴۸؛ در فارسی میانهٔ مانوی kmb نوشته می‌شود و «ب» هنوز پیداست)، و آن از پارسی باستان kamna- از ستاک *kamb-na-/*kab-na- می‌آید. راه آوایی را هوبشمان (بند ۱۵۳ د) چنین می‌گوید: «bhn» هندواروپایی در پارسی باستان به «mn» و در فارسی نو در پایان واژه به «م» ساده بدل شده است (kam از kamna، درست همانند nam «نمناک» از *namna-). در فارسی میانه خوشه ساده شده و صفت عالی کهن جداگانه به‌صورت kamist «کمترین» و صفت تفضیلی kēm «کمتر» مانده است. اما «کمین/کمینه» صفت عالیِ موروثی نیست: صفت عالی ایرانی باستان kambišta- (اوستایی) بود که در پهلوی kamist شد؛ «کمین» و «کمینه» ساخت درون‌فارسیِ نو با پسوند «ـین/ـینه» بر پایهٔ «کم»‌اند، درست مانند «مهین، بهین، کهین، بیشینه»، و در شعر کلاسیک فراوان‌اند («کای کمینه بخششت ملک جهان»، مثنوی ۱/۵۸) و همچون بیت سعدیِ همین چارت («بگذار که بندهٔ کمینم») در معنی «کهترین بنده» هم به کار می‌روند. مان نیز در همان مدخل «Per. kamin, kamine» را آورده است، پس مأخذ نورایی همین است. یک هشدار که چارت نمی‌دهد: «کمینِ» به معنی «کَمین‌گاه» واژهٔ دیگری است و از عربی «کمین» وام گرفته شده و نباید با این یکی اشتباه شود. در مجموع ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%85\",\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D9%86%D9%87\",\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D9%86\",\n            \"https://abadis.ir/fatofa/%DA%A9%D9%85/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1689\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qateʿ ed. Moʿin, printed p. ۱۶۸۹ (fetched with tools/ref_page.py BQT:1689 --image = BQT_v3_picofile.pdf p. 482; image and my vision transcription saved as data/verification/sources/refs/ocr/BQT/1689.png and 1689.vision.txt). Headword: «کم - بفتح اول و سکون ثانی، بمعنی اندک باشد که در مقابل بسیار است ۳». Moʿin's etymological footnote 3 reads: «پارسی باستان kamna، صورت *kanbiyah، *kanbishta، اوستا kamna، پهلوی kam، کردی kim، افغانی و بلوچی kam - اشتق - هوبشمان ۸۶۵، نیبرگ ص ۱۱۸: kam، ص ۱۲۸: kēm، سمنانی kāmi، سرخه‌یی kam، لاسگردی و شهمیرزادی kam، گیلکی kam.» That is exactly Nourai's arrow OP/Av. kamna- → NP kam. Caveat: p. 1689 covers only کم; کمین/کمینه are not on this page, so the citation does not document the other two words of the node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD pp. 48, 50\",\n              \"stance\": \"supports\",\n              \"note\": \"'kam [km | M kmb, N ~] little, small, few; v. kem.' — the Manichaean spelling kmb shows the original -mb-; also 'kamist [kmyst'] least. ~īh: pad ~īh, at least' and 'kem [kym] less, fewer; v. kam', i.e. MP had its own inherited superlative kamist, not *kamīn.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) p. 115-116 s.v. kam\",\n              \"stance\": \"supports\",\n              \"note\": \"'kam [km] little (adj. and adv.), few 66^17, 93^19.21, 96^6.7, 110^22; almost a modest negation… — Av. (440) kamna-; Paz. NP kam. v. kem.' The index of the same volume has 'kambištem: kēm'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 865 (p. 193-194)\",\n              \"stance\": \"supports\",\n              \"note\": \"'865. kem \\\"wenig, gering, klein\\\", kemīn, ap. kamna- \\\"wenig\\\"; aw. kamna-; phlv. kam, kam(i)… Die Grundform ist *kambhna- bezw. *kṃbhna- (Hübschmann, ZDMG 44, 559; Bartholomae, Studien II, 101). Kurd. kim und phlv. kim… werden auf den Comparativ *kamnyao zurückgehen.' Horn expressly lists the -īn form (kemīn) beside kem — direct support for Nourai's kamîn.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien no. 865 (pp. 88-89), §153 d (p. 253)\",\n              \"stance\": \"supports\",\n              \"note\": \"corrects Horn's *kamnyao ('eine wüste Bildung!') and sets up OP kamna-, *kanbiyah-, *kanbišta-; §153 d gives the sound law 'kam \\\"wenig\\\" = ap. kamna- aus *kabna-, idg. *kṃbhna-'. Moʿin's BQT footnote is taken verbatim from this passage ('هوبشمان ۸۶۵').\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann p. 1044 s.v. quómn-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Per. cf. kamin, kamine, adj. \\\"mean, base\\\", cf. kam \\\"few, less, lacking\\\"' — the only one of Nourai's books that actually lists all three Persian words together; note Mann glosses kamin/kamine 'mean, base' (the humble-self use), Nourai 'least' (the superlative use); both are current.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Moʿin s.v. کم (abadis.ir/fatofa/کم)\",\n              \"stance\": \"supports\",\n              \"note\": \"'(کَ) [په.] ۱ - (ص.) اندک، قلیل. ۲ - (ص تف.) کمتر، اقل…' — Moʿin tags the word [په.] = Pahlavi, i.e. inherited from Middle Persian, not a loan.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e rīše-hā-ye hend-o-orupāyī, s.v. کم (excerpt quoted on abadis.ir; Latin index p. ~406 'KAMNA, KAMBISHTEM (Avestan) / KAMNA, *KANBIYAH, KANBISHTA (Old Persian) / KAM, KEM (Pahlavi)')\",\n              \"stance\": \"partial\",\n              \"note\": \"Aryanpur keeps the same Iranian chain (Av. kamna, kambištem; OP kamna, *kanbiyah, kanbishta; Pahl. kam, kem) but attaches it to a different IE root: «ریشه هندواروپائی اسکرده - skerdh… در فارسی باستان کمن kamna و در اوستا نیز کمنا… و در انگلیسی کرت curt و cut», i.e. *(s)ker-dh- 'cut short' — neither Nourai's *(s)kombh-no- nor Mann's *kʷomn-. Another sign that the PIE level of this etymology is unsettled.\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"en.wiktionary.org s.v. کم, کمین, کمینه\",\n              \"stance\": \"partial\",\n              \"note\": \"'Inherited from Middle Persian 𐭪𐭬 (km /kam/, \\\"little, small\\\"), from Proto-Iranian *kam(b)-na- (\\\"small\\\"), from *kamb- (\\\"small\\\"), from Proto-Indo-Iranian *kambʰ- (\\\"few, small, insignificant\\\"). Probably further related to Proto-Indo-European *ken-…', citing Edelman, ESIJa IV 193 s.v. '*kamb- : kab-, *kambna- : kabna-'. کمینه: 'From کم (kam) +‎ ـینه (-ine)… (archaic) superlative degree of کم: the least'. کمین: two homonyms — Etymology 1 'Borrowed from Arabic كَمِين (kamīn)' = 'ambush'; Etymology 2 '(archaic) superlative degree of کم: the least'. CAUTION: this Wiktionary entry's reference [1] is Nourai 2011 p. 208 — this very chart — so its Middle-Persian link is not independent of the book being checked; only the Edelman citation [2] is.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T15:51:26.594Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-238.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T15:51:29.403Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-238.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 238",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-06T15:51:31.372Z] TOOL RESULT

```
JSON OK
nodes verified: 2/2
node verdicts: {'confirmed': 2}
root verdicts: {'plausible': 1}
ref checks: {'supports': 4}
books consulted: {'supports': 9, 'not_found': 1, 'partial': 2} | by book: {'HUB': 2, 'KNT': 1, 'BRT': 1, 'SYN': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'IEC': 1, 'MON': 1, 'ARY': 1, 'Wiktionary': 1}
```


## [2026-09-06T15:51:45.904Z] AGENT

Done — 0 PROBLEM lines.

**Page 238 (book p. 208)** — 3 entries, 2 are redirects (`Kamer` → Kam 2, `Kamp` → Kam 2, skipped). One real entry, 2 nodes.

- Node verdicts: **confirmed 2** · Root verdicts: **plausible 1**
- Ref checks: supports 4 (WLD:601, IEC:1044, KNT:179, BQT:1689 — all four of Nourai's citations verified verbatim on the exact printed pages)
- Consulted: 9 supports, 2 partial, 1 not_found across KNT, BRT, SYN, PHD, NYB, HRN, HUB, IEC, MON, ARY, Wiktionary (+POK/AHD/SYN at root level)

Nothing marked `disputed` or `transcription_suspect`; **no extraction errors** — the JSON matches `site/pages/238.jpg` exactly, including `کمین (کمینه)` split into script + script_extra.

Points worth the owner's attention (recorded in the root `note`, verdict `plausible`):
- The triple headword **conflates two incompatible reconstructions**: WP II 601 `*(s)qombh-no-` (plain *k, s-mobile, ties kamna- to ON *skammr*) vs. Mann 1044 `quómn-` (labiovelar *kʷ, ties it to OE *hwon*). Both citations are accurate; they just can't both be right.
- **"Kamma" has no source** — not a headword in Walde-Pokorny, Mann, Pokorny, Buck or Watkins; apparently Nourai's own cover-form.
- **Pokorny 1959 dropped this root entirely** (his p. 929 `(s)kem-` = WP II 560, Germanic only), and Watkins/AHD has nothing; modern Iranian etymology (Edelman, ESIJa IV 193) reconstructs only Proto-Iranian *kamb-na-/*kab-na-. Aryanpur puts کم under a third root, *(s)ker-dh-.
- Node #2 nuance: کمین/کمینه are New-Persian-internal superlatives in ‑īn/‑īna (the inherited superlative is Av. *kambišta-* > MP *kamist*); and کمین "ambush" is an unrelated Arabic loan.
- **Circularity warning**: the en.wiktionary entry for کم cites Nourai 2011 p. 208 — this very chart — as its reference [1]; only its Edelman citation is independent.

New artifacts: `data/verification/sources/refs/ocr/BQT/1689.png` + `1689.vision.txt` (Moʿin's etymological footnote transcribed by vision), 6 archived web pages under `data/verification/sources/web/`.
