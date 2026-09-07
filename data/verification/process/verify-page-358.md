# Verification process log — verify-page-358


## [2026-09-07T18:18:05.445Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 358 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-358.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-358.json. Write /home/sfmqrb/git/rishe/data/verification/page-358.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 358` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:18:07.597Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T18:18:08.072Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:18:08.085Z] TOOL RESULT

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


## [2026-09-07T18:18:08.951Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-358.txt"
}
```


### [2026-09-07T18:18:08.973Z] TOOL RESULT

```
1	=== PDF page 358 (book page 328) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Neku, Nokut, Nek 2, Nk, Enek, Enk : to reach, arrive, carry  (refs POK:316; KLN:524)
4	#1 (parent #0) [Avestan] refs=KLN:524; SYN:707; BRT:1067 | nas 2 : to attain, reach ; naš : to carry ; nasaiti : he reaches ; fra-nâš : to bring ☞Per 1 ; ašnaoti : he arrives at ; asa 2 : parcel, shipment
5	#2 (parent #0) [Old Persian] refs=TZF:62 | âs 2, âsa : to arrive, come | NOTE: It is not certain if these words belong to this family of words.
6	  #3 (parent #2) [Persian] refs=TZF:62 | âsîdan «آسیدن» : to arrive, come
7	#4 (parent #0) [Germanic] refs=AHD | ga-nôga : not little, sufficient
8	  #5 (parent #4) [English] refs=KLN:524 | enough
9	#6 (parent #0) [Germanic] refs=AHD | bher-nk : to arrive carrying (something), bring ☞Bher 1
10	  #7 (parent #6) [English] refs=None | bring
11	--- entry 1 ---
12	ROOT Nekw -> redirect to Noktis
13	--- entry 2 ---
14	ROOT Nekwt -> redirect to Noktis
15	
```


## [2026-09-07T18:18:11.830Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-358.json | head -200",
 "description": "Read source JSON for page 358"
}
```


## [2026-09-07T18:18:12.805Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-07T18:18:13.297Z] TOOL RESULT

```
{
    "pdf_page": 358,
    "book_page": 328,
    "entries": [
        {
            "root": {
                "name": "Neku, Nokut, Nek 2, Nk, Enek, Enk",
                "lang": "Indo-European",
                "refs": "POK:316; KLN:524",
                "gloss": "to reach, arrive, carry"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "KLN:524; SYN:707; BRT:1067",
                    "words": [
                        {
                            "translit": "nas 2",
                            "gloss": "to attain, reach",
                            "script": null
                        },
                        {
                            "translit": "na\u0161",
                            "gloss": "to carry",
                            "script": null
                        },
                        {
                            "translit": "nasaiti",
                            "gloss": "he reaches",
                            "script": null
                        },
                        {
                            "translit": "fra-n\u00e2\u0161",
                            "gloss": "to bring",
                            "script": null,
                            "see": [
                                "Per 1"
                            ]
                        },
                        {
                            "translit": "a\u0161naoti",
                            "gloss": "he arrives at",
                            "script": null
                        },
                        {
                            "translit": "asa 2",
                            "gloss": "parcel, shipment",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Old Persian",
                    "refs": "TZF:62",
                    "words": [
                        {
                            "translit": "\u00e2s 2, \u00e2sa",
                            "gloss": "to arrive, come",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": "It is not certain if these words belong to this family of words.",
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "TZF:62",
                    "words": [
                        {
                            "translit": "\u00e2s\u00eedan",
                            "gloss": "to arrive, come",
                            "script": "\u0622\u0633\u06cc\u062f\u0646"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u0632\u0628\u0627\u0646 \u067e\u0647\u0644\u0648\u06cc \u0647\u0631 \u06a9\u0647 \u0634\u0646\u0627\u0633\u062f - \u062e\u0631\u0627\u0633\u0627\u0646 \u0622\u0646 \u0628\u0648\u062f \u06a9\u0632\u0648\u06cc \u062e\u0648\u0631\u0622\u0633\u062f",
                        "poet": "Fakhr Gorg\u00e2n\u00ee"
                    }
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "ga-n\u00f4ga",
                            "gloss": "not little, sufficient",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "English",
                    "refs": "KLN:524",
                    "words": [
                        {
                            "translit": "enough",
                            "gloss": null,
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
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "bher-nk",
                            "gloss": "to arrive carrying (something), bring",
                            "script": null,
                            "see": [
                                "Bher 1"
                            ]
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
                            "translit": "bring",
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
                "name": "Nekw",
                "redirect": "Noktis"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Nekwt",
                "redirect": "Noktis"
            },
            "nodes": []
        }
    ]
}
```


### [2026-09-07T18:18:13.343Z] TOOL RESULT

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
page-134.json
page-135.json
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
page-148.json
page-149.json
---
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


## [2026-09-07T18:18:19.866Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"=== $f\"; grep -n -i \"enek\" $f | head -20; done",
 "description": "Grep Pokorny for enek-"
}
```


### [2026-09-07T18:18:21.104Z] TOOL RESULT

```
=== POK_01.txt
617:Obwohl  , Zwangt  aus  ,feiudlicher  Bedrängnis,  Verfolgung^  verständlich wäre,  macht  die  gr.-kelt.  Bed. -Übereinstimmung  es  doch  fraglich,  ob  das lautlich  übereinstimmende  ahd.  ähta  ,feindliche  Verfolgung^,  nhd.  Achty ags.  öht  (urgerm.  *anxto),  germ.  EN  Äctumerus  (d.  i.  AytuweraZy  1.  Jh. n.  Chr.;  Brugmann  Grdr.  P  382),  womit  ir.  echt  (*anktu-  oder  *nktu-, *e7iktu-)  ,Totschlag'^  zunächst  zu  verbinden  ist  (s.  Falk-Torp  17,  1430), wLirzelhaft  mit  anÄ:-  , Zwangt  (:, bedrängen,  töten^?)  ursprünglich  gleich ist,  oder  zu  *enek-  ,töten^  gehört,  wie  auch  hitt.  hi-in-kdn^  ht-en-kdn (henkan)  ,Tod^
2436:Angebl.  aus  den  Wz.  bher-  und  enek-  kontaminiert;  zuletzt  E.  Fraenke KZ.  58,  286^ f.;  63,  198.
4681:enek-,  nek-,   enk-,  nk-   , reichen,    erreichen,    erlangen'   und   (nur  Gr.  Bsl.)    . ,tragen';  onko-s  ,Tracht,  Anteil'.  ^
4685:gr.  (*enek-)  ÖL-rjvsytrjg  , durch  eine  Strecke  hindurchreichend  =  ununter-     j- brochen'  (dor.  und   att.  Sißveni^g  aus  *dia-Tjv£xrjg?,  anders  Boisacq   s.  v.),
4706:hitt.  *nenek-ti,  PL  ^nenk-enti,  daraus  ni-ik-zi  {nikzi)  , erhebt  sich',  3.  p| und  ni-in-kdn-zlj  ni-ni-ik-zi  (ninikzi)  ,hebt',  3.  PL  ni-ni'(in-)kdn-zi  (Pedersen Hitt.  147) ;
4794:WP.  I  132  f. ;  s.  auch  unter  enek-.
=== POK_02.txt
=== POK_03.txt
=== POK_full.txt
5274:press, kill '?) originally is same, or connected to *enek- " kill ', as well as Hittite hi-in-kan, 
15380:Angebl. contaminated from root b'^er- and enek-\ finally E. Fraenkel KZ. 58, 286'' f.; 63, 
26411:Root / lemma: eneR-, neR-, enR-, nR- {*henek-) 
26523:Root / lemma: e-neuen, neup, enup {* henek'i-)'. nine' was created as a compound of Root 
62182:Material: Old Indie nenekti^ washes, purifies, cleans', Aor. anaiksTt, Pass, nijyate, participle
```


## [2026-09-07T18:18:21.138Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['TZF','POK','KLN','SYN','BRT','AHD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900]); print()\n\"",
 "description": "Look up refs metadata"
}
```


### [2026-09-07T18:18:22.504Z] TOOL RESULT

```
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadable without login."}

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
```


## [2026-09-07T18:18:27.768Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4670,4720p' POK_01.txt && echo \"=== leaf number:\" && awk 'NR<=4681{n+=gsub(/\\f/,\"\")} END{print n}' POK_01.txt",
 "description": "Print Pokorny enek- entry"
}
```


## [2026-09-07T18:18:27.874Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26400,26480p' POK_full.txt",
 "description": "Print Pokorny full English entry"
}
```


### [2026-09-07T18:18:29.012Z] TOOL RESULT

```
Amboglanna   ,Ufer  des  Stromes',   sowie   arm.  amb    und   (mit   idg.  b)  amp  .^j
,AYolke'.  X
emb{h)-  :  omb{h)- :
ai.  ämbhas-  n.  ,Regenwasser';  ambu  n.  ,Wasser',  gr.  ^iißqoq  m.  ,Regen'
(zum  b  vgl.  oben  arm.  amp  und  Schwyzer  Gr.  Gr.  I  333) ;  hierher  auch  lak.  J;
di.iq^ä  , Geruch,  Hauch',  arkad.  si)Oi.i(pog  ,wohlriechend',  usw.  jj
nembh-:  ^^
pehl.  namb,  nam,  npers.  nem  , feucht,  Feuchtigkeit',  pehl.  nambltan  ,be-  W^
feuchten' ;  ■^^■_
lat.  nimbus  , Sturzregen,  Platzregen;  Sturmwolke,  Regenwolke'.  '5-
WP.  I  131,  WH.  I  681,    II  151  f.,   Specht  Dekl.  16f.  %
enek-,  nek-,   enk-,  nk-   , reichen,    erreichen,    erlangen'   und   (nur  Gr.  Bsl.)    . ,tragen';  onko-s  ,Tracht,  Anteil'.  ^
Ai.  aänötiy  av.  asnaoiti  (*nk-neu-)  ,gelangt  hin  zu  etwas,  erreicht',  Perf. ai.  andmsa  (idg.  *ön-onke  =  air.  ro-änaic) ;
ai.  ndäati,  av.  -nasaiti  (*nek-,  ursprüngl.  wohl  athematisch,  vgl.  2.  Sg. naksi  usw.),  ai.  ndksati  , erreicht,  erlangt',  Desid.  dnaksati  , sucht  zu  er- reichen, strebt  zu',  dmsah  m.  ,Anteil',  av.  qsa-  , Partei',  ai.  ndm§a-h  m. ,Erlangung',  -namiana-  (Kreuzung  von  ams-  und  nas-)]  -,-
arm.  liasi  ,bin  angekommen',  danach  hasanem  ,komme  zu  etwas,  komme     :.g. an';   nach  Pisani  Armen.  5  hierher  hunj-Jt,  linjo-c  , Ernte'  {^onkos)\  3:
gr.  (*enek-)  ÖL-rjvsytrjg  , durch  eine  Strecke  hindurchreichend  =  ununter-     j- brochen'  (dor.  und   att.  Sißveni^g  aus  *dia-Tjv£xrjg?,  anders  Boisacq   s.  v.),
317
^oö'TjVsy-rjg  ;bis  zu  den  Füßen  herabreichend^,  dovQ-r]vsyirjg  ,einen  Speerwurf ^yeit^  ==  ;S0  weit  man  mit  einem  geschleuderten  Speere  reicht'  oder  pass. vom  Speer  erreicht',  wie  y.evTQ-7]v8yirjg  ,vom  Stachel  (erreicht  =)  angetrieben'; Pass.  Aor.  '^vsx^rjv  ,wurde  getragen',  Perf.  xar-rjvoyia  Hes.,  h-rjvoxa  (iv- ist  darin  wohl  Reduplikation;  ebenso  im  Med.  iv-rjvsy(.iaL,  zu  dem  sich als   3.  Sg.  iv-rjveyycTai   statt  Hv-rjvs'/iTai  gesellte,   nach   dem  Aor.  iveyy,eTv)]
*e7ik-   im   red.   Aor.   iv-6yy.-eTv  (*enk-enlc-)  , tragen';  s.  unten  hitt.  ÄenÄ:zi;
*onJc-  in  iJyxog  , Tracht,  Last'  (=  ai.  dnisa-h,  bsl.  *nasa-) ;
^vsiv.a  dagegen  zur  Wz.  *seik-  ,langen',  s.  dort  und  Boisacq  251  f.  m. Lit.j  durch  Kreuzung  mit  ihm  wurde  'irjveyv.ov  zu  ^jvsyaa,  ijveLy-Aa]
lat.  nactus  (und  nanctus)  sum,  nancisci  (arch.  auch  nanciö,  -Ire)  , er- langen' (-a- =  ^,  so  daß  wac^ws  =  germ.  *nuh-ta-',  die  Nasalierung  des Präs.  ist  wohl  sekundär  (Kuiper  Nasalpräs.  163) ;
air.  ro-icc  , erreicht',  do-icc  ,kommt',  air-icc-  , finden',  con-icc-  ,können' usw.;  wohl  in  die  themat.  Konjugation  übergeführtes  dehnstufiges  *enk-ti, woraus  *lnk-,  *inc-,  icc--,  Verbalnomina  rlchtUj  tichtWj  s-Konj.  -i  aus  *enkst] Perf.  ro-änaic  (s.  oben);  s-Prät.  du-uicc  {^'onk-i-s-t)  ,hat  gebracht'  usw. s.  unten  S.  347 ;  Schwundstufe  nk-  in  cymr.  di-anc  ,entfliehen',  cyfranc (^kom-ro-anko-)  =  air.  comracc  »Zusammentreffen';  nach  Loth  RC  40,  353 ir.  oc^  cymr.  wnc,  long  ,bei'  aus  *onko-  ,Nachbarschaft'?;  dazu  mcymr. ech-wng  , Vertreibung';  nach  Vendryes  (MSL  13,  394)  hierher  auch  der gall.  VN  *Selva-nectes  (latinis.  Silvanectes)  ,qui  ont  obtenu  propriete',  zu air.  selb  , Besitz^;
got.  ganah  (Prät.-Präs.)  ,es  reicht  =  genügt',  Inf.  ganaühan  (über  germ. rmh-  s.  oben),  ahd.  ginah,  ags.  geneah  ds. ;  got.  *hinauhan  , erlaubt  sein', got.  ganaüha  m.,  ahd.  (usw.)  ginuht  f.  , Genüge';  ö-stufig:  got.  ganöhs ,genug,  viel',  ags.  genöh,  genüg,  anord.  {g)nögr,  ahd.  ginuog  ,genug'  usw.; e-stufig,  wie  es  scheint,  anord.  nä  ^nahekommen,  erreichen,  bekommen', ags.  (ge)ncegan  ,sich  jemandem  nähern,  anreden,  angreifen';
über  got.  neh  Adv.  ,nahe,  nahe  an',  neJva  ds.,  as.  näh,  ags.  neah  ,nah', Präp.  ,nahebei',  ahd.  näh  Adj.  ,nahe',  Adv.-Präp.  ,nahe',  nhd.  nach  s.  oben S.  40;  man  stellt  auch  alb.  nes,  nes-er  , Morgen'  (*nök-)  dazu,  ebenso  lett. näku,  näki  ,kommen',  lit.  pranökti  , überholen',  nökti  , reifen',  die  aber  idg. ä  voraussetzen ;  vgl.  Mühlenbach-Endzelin,  Lett.-D.  Wb.  II  698 ;
über  das  von  Jokl  SBWienAk.  168,  I  36  mit  pranökti  verglichene  alb. ke-nak  ,befriedigen,  vergnügen'  s.  denselben  lA.  35,  36;
bsl.  *nesö  ,trage'  (vgl.  ai.  naiati)  in:
Vit.  nesü,  nesiaü,  nesti]  IqU,  nesu,  ne§u,  nest]  dazu  Iterativum  lett.  «esa^, lit.  nesiai  =  lett.  nesi  m.  PL  ,Tracht  Wasser',  lit.  na§tä,  lett.  nasta  f. ,Last' ;
aksl.  nesg,  nesti,  Iterativum  nositi  usw.,
*
H
318
9
bsl.  *nasa-  m.  ,das   Tragen,    der  Träger'  (=  ai.  amsa-h,  gr.  ö^xog)  1,^.
lit.  ui-naSai  PL  , ausgeschenktes  Bier',  dehnstufig  sq-noSai  m.  PL  ,ano-e, schwemmtes  Geröll';
ksL  'po-nosz  jNeid',  russ.  za-nös  , Schneegestöber',  usw. ;
hitt.  *nenek-ti,  PL  ^nenk-enti,  daraus  ni-ik-zi  {nikzi)  , erhebt  sich',  3.  p| und  ni-in-kdn-zlj  ni-ni-ik-zi  (ninikzi)  ,hebt',  3.  PL  ni-ni'(in-)kdn-zi  (Pedersen Hitt.  147) ;
hi-in-ik-zi  (henkzi)  ,teilt  zu'  stellt  sich  zu  ijvsyyiov]  über  na-ak-ki-is  (nakis) ,schwer',  s.  Pedersen  Hitt.  147,  194;
über  toch.  A  emts-,  B  ehk-  ,nehmen,  fassen',  s.  Meillet  MSL  18,  28 Pedersen  Tochar.  236  und  Anm.  1;
Kuiper  Nasalpräs.  50  f.  zerlegt  en-ek-  ,tragen*,  das  er  als  Erweiteruno- von  en-  (s.  S.  321  unter  enos-)  ds.  auffaßt;  ebenda  weitere  Vermutungen  über en-ek-  , erreichen'.
WP.  1 128  f.,  Kuiper  Nasalpräs.  50  f.,  EM^  652,  Trautmann  198,  Schwyzer Gr.  Gr.  647,  744,  766.
eneu,  enu  ,ohne'.
Gr.  (Lokat.  ?)  ävsv^  Uvevd'B{v)  ,ohne';  dor.  Hvevv,  el.  Uvev(;,  meg.  Uviq (nach  x^^^'s  gebildet);
aus  *,neu-j  got.  imi  ,ohne' ;
mit  Dehnstufe :  ai.  änu-sdk,  av.  änu-Sak  ,der  Reihe  nach'  (zu  ai.  anu-sac- ,folgen',  Wz.  seku-) ;  altnord.  an,  ön,  afries.  öni,  as.  äno,  ahd.  änw,  äno^ äna,  mhd.  äne,  an,  nhd.  ohne  aus  *enu.
Nicht  ganz  sicher  ist  das  nur  von  Gramm,  belegte  ai.  anö  ,nicht'  (==  gr. ävev)  heranzuziehen,  auch  osset.  änä  ,ohne';  Verwandtschaft  mit  lat.  sine usw.  (Meillet  BSL.  30,  Nr.  89,  81)  mag  bestehen,  doch  keineswegs  sicher.
WP.  I  127  f.,    Feist  295,  WH.  I  677.
e-neuen,  neun,  enun  ,neun'.
Ai.  ndüa,  av.  nava  (neun)  ,9';
arm.  inn  (sprich  indn)  ,9'  ('^'enun),  PL  in(n)unk]
gr.  *eyfa-  in  hom.  elvä-ereg,  -yvx^Sy  böot.  iva-y,rj-SsyidTr]j  ion.  slva-'AÖaioi, att.  ha-'AOGLOL]  Ord.  elvarogy  att.  äol.  8vaTog]  *ivJ^a  auch  in  hom.  ivvrj(.iaQ (*ivß  ^^aQ)  ,9  Tage*;  daneben  *v€J^a  (*neun)  in  ivvs[ß]a  (mit  vorgesetztem ev,  Schwyzer  Gr.  Gr.  I  591);  danach  wurde  IvrfAOvia  ,90'  zu  ion.  att. ev8vrjY.ovTa ;
=== leaf number:
329
```


### [2026-09-07T18:18:29.056Z] TOOL RESULT

```
l\^ongolian protoform: *jevu-le- 
Tungus protoform: *hiabe- 
Korean protoform: *nub- 

Note: TMC 1, 352. It is tempting to compare also Evk. hewte, Evn. hewte 'spring, well' 
(*'washing or pouring place') and perhaps also OJ mjiwo 'water-way, seaway' (if mji- is to 
be analysed as 'water', the -wo part stays completely obscure). 

References: WP. I 131, WH. 1681, II 151 f., Specht Dekl. 16f. 
Page(s): 315-316 

Root / lemma: eneR-, neR-, enR-, nR- {*henek-) 

l\^eaning: to reach; to obtain 

l\1aterial: Old Indie asnoti, Avestan asnaoiti{ *nR-neu-) " if something is obtained, achieved 

', Perf. Old Indie anamsa {\v\6o Germanic *dn-onRe= Old Irish ro-anaic)\ 

Old Indie nasati, Avestan -nasaiti{*neR-, originally probably athematic, compare 2. Sg. 
naRs/etc), Old Indie naRsat/" achieved, attained ', Desid. anaRsati^ tries to reach, strives 
for ', amsa-h m. " allotment ', Avestan ^sa- " party ', Old Indie namsa-h m. " obtainment ', - 
narhsana- (hybridization from arhs- and nas-)\ common Old Indie gh- > Rs- 

Armenian hasrhave arrived ', thereafter hasanem^ come to close to something, arrive 
'; after Pisani Armen. 5 here hunJ-R', bnjo-c^ harvest' ( *onRos); 

Maybe alb. has, alb. (Calabria) {*Re-hasem) Reyasem' encounter' 

gr. {*heneR-) Si-nvEKnq " passing through distance = unbroken, perpetual ' (Doric and 
Attic SiavEKnq from *5ia-r|V£Kn(;?, different Boisacq s. v.), no5-r|V£Kn(; ' bis zu den Fijften 
herabreichend ', Soup-nvsKng " a far javelin-throwing ' = ' as far as one's spear can reach ' 



or pass. " obtain a javelin ', as K£VTp-r|V£Kn(; " tlie goad, prick (obtain =) set in motion, prick, 
drive on '; Pass. Aor. riv£x6r|v ' wurde getragen ', Perf. KOT-nvoKa Hes., £v-r|voxa (£v- is 
therein probably reduplication; also in Med. £v-nv£YMCii, joined as 3. Sg. £v-riv£YKTai instead 
of *£v-r|V£KTai, after Aor. £V£yk£Tv); 

*enR- in Redupl. Aor. £v-£yk-£Tv ( *enR-enR-) 'bear, carry'; see below Hittite henkzr, 

*onR-\n 6yko(; Tracht, load' (= Old Indie amsa-h, Balto Slavic *nasa-)\ 

riv£iKa against it to root *seik- ' suffice, reach ', see there and Boisacq 251 f. m. 
Lithuanian; through hybridization with it became nv£YKOv to nv£YKa, nv£iYKa; 

Latin nactus {and nanctus) sum, nanc/sc/ {arch, also nancio, -Tre) " to light upon, obtain, 
meet ' {-a- = e, so nactus = Germanic *nuh-ta-\ the nasalization of present is probably 
secondary (Kuiper Nasalpras. 163); 

Old Irish ro-icc' reaches ', do-icc^ comes ', a/r-zcc- "find', con-icc-^be able' etc.; 
probably in the themat. conjugation transferred lengthened gradees *enR-ti, from which 
*Tnk-, *mc-, icc-\ verbal nouns nchtu, tTchtu, s-Konj. -/"from *enRst, Perf. ro-anaic {see 
above); 5-preterit du-uicc{*onR-i-s-t} "has brought' etc. see below S. 347; zero grade nR-\r\ 
cymr. o'/-5/7c "escape, flee', cyfranc {*Rom-ro-anRo-) = Old Irish comracc^ encounter'; after 
Loth RC 40, 353 Irish oc, cymr. wnc, wng 'by' from *onRo- " neighborhood '?; in addition 
mcymr. ec/7-w77^ "expulsion'; after Vendryes (MSL 13, 394) here also the gall. VN *Selva- 
/7e'c/e5(latinis. Silvanectes) " property which is acquired ', to Old Irish selb' possession '; 

Gothic ganah (preterit-present) " it suffices = is enough, it meets the needs ', Inf. 
ganauhan {about Germanic *nuh- see above). Old High German ginah. Old English 
geneahds.; Gothic *binauhan' be permitted ', Got\r\\c ganauham., Old High German (etc.) 
ginuhti. " sufficiency '; o-grade: Gothic ganohs " sufficient, much, a lot of. Old English 
genoh, genog. Old Norse (g)ndgr. Old High German ginuog' sufficient ' etc.; e-grade, as it 
seems. Old Norse na' approach, reach, obtain ', Old English (ge)nsegan' approach to 
somebody, address, attack '; 

about Gothic ne/vAdv. " approach, come near to, close to, adjacent to, nearby, near ', 
nefva ds.. Old Saxon nah. Old English neah' nearby, close at hand, near, close in time ', 
preposition " nearby, next to, alongside ', Old High German nah Ad]. " adjacent ', Adv.- 
preposition "by'. Modern High German nachsee above S. 40; one places also alb. nes, 
nes-er, neser' tomorrow morning ' {*ndR-)\ in addition, also Latvian naRu, naR/'come', 



Lithuanian pranokt/" overtake', nokt/'npen', but tlie presupposed Indo Germanic a; 
compare Muhlenbach-Endzelin, Latvian-D. Wb. II 698; 

about that Jokl SB Wien Ak. 168, I 36 with Lithuanian pranokt/' overtake' compared alb. 
ke-nak^ satisfy, delight ' s. the same lA. 35, 36;
```


## [2026-09-07T18:19:07.886Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD nek\" && grep -n -i \"nek-2\\|nek-\\|enough\\|bhrenk\\|bhr-en-k\" AHD_watkins1985.txt | head -40",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-07T18:19:07.934Z] TOOL RESULT

```
=== AHD nek
135:The Indo-Europeans knew snow in their homeland; the word sneig”h- is nearly ubiq- uitous. Curiously enough the word for “rain,” however, varies among the different branches; we have words of differing distri- bution like seue-?, ombh-ro- and reg-?.
139:The names for a number of different trees are widely enough attested to be viewed as Proto-Indo-European in date. The general term for tree and wood was deru. The origi- nal meaning of the root was doubtless “to be
189:Most interesting are the cases where from two or more traditions (usually including Homer and the Rig-Veda) it is possible to reconstruct a poetic phrase or formula con- sisting of two members. Such are the expres- sions ‘“‘imperishable fame,” *klewos ndhg’hitom (kleu-', dhg“hei-); “holy (men- tal) force,” *isorom menos (eis-', men-'); and the “weaver (or crafter) of words,” the Indo- European poet himself, *wek”om teks-on (wek”, teks-). The immortality of the gods (*n-mrto-, from mer-?) is emphasized anew by the vivid verb phrase nek-' tera-?, “to overcome death,” appearing in the Greek word nektar, the drink of the gods. And at least one three-member formula (in the sense of the word in traditional oral poetry) can be reconstructed for the poetic language of prayer, on the combined evidence of four languages, Latin, Umbrian, Avestan, and Sanskrit: “Protect, keep safe, man and cat- tle!” (pa- wi-ro- peku).
333:bher-1. To carry; also to bear children. 1. a. Germanic *beran in (i) Old English beran, to carry: BEAR! (ii) Old English forberan, to bear, endure (for-, for-; see per’): FORBEAR; b. Germanic *bérd in Old English bér, ber, bier: BIER; c. Germanic *bér- in Old Norse bdra, wave, billow: BORE’. 2. a. Germanic *barnam in Old English bearn, child: BAIRN; b. Germanic *barwdn- in Old Eng- lish bearwe, basket, wheelbarrow: BARROW!, 3. a. Ger- manic *burthinja in Old English byrthen, burden: BURDEN}; b. Germanic *burthiz in Old Norse burdhr, birth, akin to the source of BIRTH; C. Germanic *burja- perhaps in Old Norse byrr, favorable wind: BIRR}. 4. Compound root *bhrenk-, to bring (< *bher- + *enk-, to reach; see nek-2), in Germanic *brengan in Old English bringan, to bring: BRING. 5. Latin ferre, to carry: -FER, FERTILE; AFFERENT, CONFER, DEFER!, DEFER®, DIFFER, EFFERENT, INFER, OFFER, PREFER, PROFFER, REFER, SUFFER, TRANSFER, VOCIFERATE. 6. Latin pro- brum, a reproach (< “pro-bhr-o-, “something brought before one”; pro-, before; see per'): OPPROBRIUM. 7. Lengthened o-grade form *bhor- probably in Latin far, thief: FERRET!, FURTIVE, FURUNCLE; (FURUNCULOSIS). 8. Greek pherein, to carry: -PHORE, -PHORESIS, -PHO- ROUS; AMPHORA, ANAPHORA, DIAPHORESIS, EUPHORIA, METAPHOR, PERIPHERY, PHEROMONE, TELPHER, TOCOPH- EROL. 9. Greek pherné, dowry (“something brought by a bride”): PARAPHERNALIA. [Pok. 1. bher- 128.]
642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
661:ladh-. To be hidden. 1. Greek léthé, forgetfulness: LETH- ARGY, LETHE. 2. Zero-grade form *ladh- (< *bdh-), with nasalized form *landh-, in Greek lanthanein (aorist lathein), to escape the notice of, with middle anthanes- thai, to forget: LANTHANUM; ALASTOR. 3. Suffixed (sta- tive) variant form */at-é- in Latin latére, to lie hidden: LATENT. [In Pok. 2. /a- 651.] laiwo-. Left. Latin Jaevus, left: LEVO-; (LEVOROTATION), (LEVOROTATORY). [Pok. laiuo- 652.] laks-. Salmon. Suffixed form */aks-o- in Germanic */ahs- az in Old High German Jahs, salmon: Lox}. [Pok. lak- 653.] laku-. Body of water, lake, sea. 1. Latin /acus, lake, pond, basin: LAKE!. 2. Greek lakkos, cistern: LACCOLITH. 3. O-grade form *loku- in Old Irish and Scottish Gaelic loch, lake: LocH, LouGH. [Pok. laku- 653.] lap-. To light, burn. Nasalized shortened form */a-m-p- in Greek lampein, to shine: LAMP, LANTERN; ECLAMPSIA. [Pok. la(i)p- 652.] las-. To be eager, wanton, or unruly. 1. Suffixed Ger- manic zero-grade form *lustuz in: a. Old English Just, lust: Lust; b. Old High German Just (> German Lust), desire: WANDERLUST; Cc. Germanic denominative verb *lustjan in Old English lystan, to please, satisfy a desire: LisT’, 2. Suffixed form */as-ko- in Latin lJascivus, wan- ton, lustful: Lascivious. [Pok. las- 654.] lat-. Wet, moist. Latin latex, liquid: LaTEx. [Pok. Jat- 654.] lau-. Gain, profit. 1. Suffixed form */au-no- in Germanic *Jaunam in Old High German J6n, reward: GUERDON. 2. Suffixed zero-grade form */u-tlo- in Latin lucrum, gain, profit: LUCRATIVE, LUCRE. 3. Suffixed variant form *low-ero- in Irish Gaelic ledr, sufficiency, enough: GA- LORE. [Pok. ldu- 655.] lé-1. To get. Contracted from “lea-. Suffixed zero-grade form *b-tr- in: a. Greek Jatreia, service (for pay), duties, worship: -LATRY; b. Greek Jatron, pay, akin to the Greek source of Latin latré, robber: LARCENY; c. Greek -/latrés, worshiper: IDOLATER. [Pok. 2. /é(i)- 665.] lé-2, To let go, slacken. Contracted from *les-. 1. Ex- tended form */éd- in: a. Germanic */étan in Old English létan, to allow, leave undone: LET!; b. Germanic deriva- tive *léthigaz, freed, in Medieval Latin /étus, litus, serf (< “free man”): LIEGE. 2. Extended zero-grade form */d- in: a. Germanic */ataz in Old English Zt, late, with its comparative lztra, latter, and its superlative Jatost, last: LATE, LATTER, LAST!; b. Germanic */atjan in Old English lettan, to hinder, impede (< “to make late”): LET?; c. suffixed form */od-to- in Latin lassus, tired, weary: LASSITUDE; ALAS. 3. Suffixed reduced form */é-ni- in Latin lénis, soft, gentle: LENIENT, LENIS, LENITIVE, LENITY. [Pok. 3. lé(i)- 666.] leb-'. Base of loosely related derivatives meaning “hang- ing loosely.” I. Variant form *lep- in Germanic */ap- in Old English lzppa, lappa, flap of a garment: Lap’. II. Nasalized form *lemb(h)-, with variant form *slemb(h)-. 1. Germanic *lemp- probably in obsolete English limphalt, lame (halt, lame; see kel-'): LIMP. 2. Germanic */ump- in: a. Dutch lomp, rag, akin to the Low German source of Middle English Jump, lump: LUMP!; b. possibly obsolete English Jump, lumpfish: LUMPFISH; Cc. German Lumpen, rags: LUMPEN. 3. Ger- manic *slimp- in Middle Dutch slim(p), slanting, bad: SLIM. 4, Middle High German slam, mud: SLUMGULLION. 5. Old Norse slambra, to strike at, akin to the Scandina- vian source of SLAM!. 6. Norwegian slumpa, to slump, akin to the Scandinavian source of sLuMpP. III. Variant *(s)lab- in Germanic *s/ab-. 1. Danish slab, mud, akin to the Scandinavian source of SLAB2. 2. Swedish slabb, slime, mud, akin to the Scandinavian source of Irish slab, mud: sLos. IV. Variants *slap-, *slep-. Germanic *slap- in: a. Low German s/app, slap: SLAP; b. Old Norse slafra, to slaver: SLAVER}. V. Variant */ab-. 1. Germanic *lab- in Old French label, ribbon, strip: LABEL. 2. Latin
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
900:a. Old English risan, to rise: RISE; b. Old English drisan, to arise (G-, up, out): ARISE. 2. Germanic causative *raizjan in: a. Old English réran, to rear, raise, lift up: REAR?; b. Old Norse reisa, to raise: RAISE.] rtko-. Bear. 1. Latin ursus, bear (< *orcsos): URSINE. 2. Greek arkios, bear: aRcTIC, ARcTURUS. 3. Celtic *arto- in Welsh arth, bear, in the name Arthur (> Medieval Latin Artorius, Arthur): ARTHUR. [Pok. tktho-s 875.] ruk-1, Fabric, spun yarn. Celtic and Germanic root. 1. Germanic *rukk6n- in: a. Italian rocca, distaff: ROCKET!; b. Old High German rocko, distaff: ROCAM- BOLE; C. Old French rocquet, head of a lance: RATCHET. 2. Germanic *rukka- in Old French rochet, rochet: ROCH- ET. [Pok. ruk(k)- 874.] ruk-2. Rough. Extension of reu-2. 1. Lengthened-grade form *rik- in Germanic *riéhwaz in Old English rih, rough, coarse: ROUGH. 2. Lengthened variant form *rig- in Latin riga, wrinkle: RUGA, RUGOSE; CORRUGATE. [In Pok. 2. reu- 868.] runo-. Mystery, secret. Germanic and Celtic technical term of magic. Germanic *riinaz in: a. Old English riinian, to whisper: ROUND?; b. Old Norse riin, secret writing (akin to the Germanic source of Finnish runo, song, poem): RUNE!, RUNE?. [In Pok. 1. reu- 867.] sa-. To satisfy. Contracted from *sas-. 1. Suffixed zero-grade form *s9-to- in: a. Germanic *sadaz, sated, in Old English sed, sated, weary: SAD; b. derivative Ger- manic verb *sadon, to satisfy, sate, in Old English sadian, to sate: SATE!. 2. Suffixed zero-grade form *s9-ti- in Latin satis, enough, sufficient: SATIATE, SATIETY; (ASSAI2), ASSET, SATISFY. 3. Suffixed zero-grade form *s9-tu-ro- in Latin satur, full (of food), sated: SATIRE, SATURATE. 4. Suffixed zero-grade form *so-d-ro- in Greek hadros, thick: HADRON. [Pok. sd- 876.] sab-. Juice, fluid. 1. Germanic *sapam, juice of a plant, in Old English sp, sap: SAP}. 2. Illyrian sabaium, beer, probably akin to the source of Italian zabaglione, zabaione, a frothy dessert: ZABAGLIONE. [In Pok. sap- 880.] sag-. To seek out. 1. Suffixed form *sdg-yo- in Germanic *sdkjan in Old English sécan, sécan, to seek: SEEK. 2. Suffixed form *sdg-ni- in Germanic *sdkniz in Old English sdcn, attack, inquiry, right of local jurisdiction: SOKE. 3. Zero-grade form *sog- in Germanic *sak- in: a. derivative noun *saké, “a seeking,” accusation, strife, in Old English sacu, lawsuit, case: SAKE}; b. Germanic *sakjan, to lay claim to (denominative of *sak6), in Old French seisir, to take possession of, seize: (SEISIN), SEIZE; c. Germanic *sakan, to seek, accuse, quarrel, in (i) Old English forsacan, to renounce, refuse (for-, prefix denot- ing exclusion or rejection; see per'): FORSAKE (ii) Old Norse saka, to seek: RANSACK. 4. Independent suffixed form “sdg-yo- in Latin sdgire, to perceive, “seek to know”: PRESAGE. 5. Zero-grade form “sog- in Latin sagdx, of keen perception: SAGACIOUS. 6. Suffixed form *sdg-eyo- in Greek hégeisthai, to lead (< “to track down”): EXEGESIS, HEGEMONY. [Pok. sdg- 876.] sai-. Suffering. 1. Germanic *sairaz, suffering, sick, ill, in Old English sdr, painful: sore. 2. Derivative Germanic adjective *sairigaz, painful, in Old English sarig, suffer- ing mentally, sad: SORRY. [Pok. sdi-, 877.] sak-. To sanctify. 1. Suffixed form *sak-ro- in: a. Latin sacer, holy, sacred, dedicated: SACRED; CONSECRATE, EXECRATE; b. compound *sakro-dhét-, “performer of sacred rites” (*-dhét-, doer; see dhé-'), in Latin sacerdés, priest: SACERDOTAL. 2. Nasalized form *sa-n-k- in Latin sancire (past participle sanctus), to make sacred, conse- crate: SAINT, SANCTUM; CORPOSANT, SACROSANCT, SANC- tiFy. [Pok. sak- 878.] sal-1, Salt. 1. Extended form ‘*sald- in: a. suffixed form *sald-o- in Germanic *saltam in Old English sealt, salt: SALT; b. Germanic zero-grade suffixed extended form *sult-j6 in (i) Old French sous, pickled meat: SOUSE (ii)
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
1461:ENNEAD newn ENNUI od-2 ENORMOUS gn6- ENOUGH kom, nek-2 ENSEMBLE sem-! ENSIFORM nsi- ENSTATITE sta- ENSUE sekw-1 ENSURE cira
1679:INNATE gene- INNER en INNOCENT nek=! INNOCUOUS_nek-1 INNOVATE newo- INNUENDO neu-2 INOCULATE okw- INORDINATE ar- INOSCULATE 6s- INOSITOL wei-1 INOTROPIC wei- INQUILINE kWel-1
1682:INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
1907:NEB _ nabja- NEBULA nebh- NEBULOUS nebh- NECESSARY ked- NECK ken-5 NECRO- nek-1 NECROMANCY negw-ro-, nek-1 NECROPOLIS pele-3 NECROSIS nek-1 NECTAR nek-! NECTARINE nek-1 NEE gene-
1929:NOBLE gno- NOCENT nek-! Nock ken-5 NOCTI- nekw-t- NOCTILUCA leuk- NOCTUID nekw-t- NOCTULE nekw-t- NOCTURN nekw-t- NOCTURNAL nekw-t- Nocuous_nek-! NOD ken-2
1939:NOXIOUS nek-1 NUANCE sneudh- NUB gen-
1944:NUDI- nogW- NUDNIK nau-! NUISANCE nek-1 NULL ne
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
1977:ONAGER agro-, asinus ONCE oi-no- ONCOGENESIS nek-2 ONCOLOGY nek-2 ONE oi-no- ONEIROMANCY oner- ONEROUS en-es- ONOMASTIC no-men- es ONOMATOPOEIA kWej-2, no-men- ONSLAUGHT ant, slak- -ONT es-
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
```


## [2026-09-07T18:19:10.011Z] TOOL CALL #10: Bash

```json
{
 "command": "pdftoppm -f 358 -l 358 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg358 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 358"
}
```


### [2026-09-07T18:19:11.635Z] TOOL RESULT

```
total 20232
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 14:19 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1011 Sep  7 14:18 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T18:19:23.840Z] TOOL CALL #11: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg358.png"
}
```


### [2026-09-07T18:19:24.185Z] TOOL RESULT

```

```


## [2026-09-07T18:19:24.171Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T18:19:52.329Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 358 -l 358 -r 500 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p358hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('p358hi.png'); print(im.size)\nw,h=im.size\n# quote area approx y 570-620 of 2200 at r200 -> fraction\nim.crop((int(0.44*w),int(0.235*h),int(0.78*w),int(0.285*h))).save('p358_quote.png')\n\"; ls -la p358_quote.png",
 "description": "Crop Persian quote at high resolution"
}
```


### [2026-09-07T18:19:55.595Z] TOOL RESULT

```
(4250, 5500)
-rw-rw-r-- 1 sfmqrb sfmqrb 4274 Sep  7 14:19 p358_quote.png
```


## [2026-09-07T18:20:00.237Z] TOOL CALL #13: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p358_quote.png"
}
```


### [2026-09-07T18:20:00.257Z] TOOL RESULT

```

```


## [2026-09-07T18:20:04.096Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p358hi.png'); w,h=im.size\nim.crop((int(0.44*w),int(0.255*h),int(0.79*w),int(0.29*h))).resize((int(0.35*w*1.4),int(0.035*h*1.4))).save('p358_q2.png')\n\"",
 "description": "Crop verse line"
}
```


### [2026-09-07T18:20:05.835Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T18:20:08.707Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p358_q2.png"
}
```


### [2026-09-07T18:20:08.792Z] TOOL RESULT

```

```


## [2026-09-07T18:20:08.788Z] INPUT

[Image: original 2082x269, displayed at 2000x258. Multiply coordinates by 1.04 to map to original image.]


## [2026-09-07T18:20:13.387Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p358hi.png'); w,h=im.size\nc=im.crop((int(0.44*w),int(0.283*h),int(0.79*w),int(0.302*h)))\nc=c.resize((c.width*2,c.height*2))\nc.save('p358_q3.png'); print(c.size)\n\"",
 "description": "Crop verse line again"
}
```


### [2026-09-07T18:20:15.190Z] TOOL RESULT

```
(2974, 210)
```


## [2026-09-07T18:20:17.990Z] TOOL CALL #17: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p358_q3.png"
}
```


### [2026-09-07T18:20:18.074Z] TOOL RESULT

```

```


## [2026-09-07T18:20:18.071Z] INPUT

[Image: original 2974x210, displayed at 2000x141. Multiply coordinates by 1.49 to map to original image.]


## [2026-09-07T18:20:29.827Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT 1067 leaf\" && grep -n \"^1067\\|1067\" BRT.txt | head -20",
 "description": "Find Bartholomae column 1067"
}
```


### [2026-09-07T18:20:29.882Z] TOOL RESULT

```
=== BRT 1067 leaf
21104:druxi  naiäite  (Sp.  1067  m.)  y  aiwiat jayma^  ". .,  von  wo  sie  herzugekommen war"  Vti^.  r2.
22272:pars  vay&ibyö^'*  YLjo.88; —  *ao^rab}'B ariuxialibyasca  vSyiibyB^^  vufitn  .  . yazatitn  yasamaide  Y,i6.  i;  Vi.  6.  i,  Ny, J.  1 6;  —  Avamxiaft?m .  .yaxamaide  vacaca ^ao^naca  sao^rabyasca  N.1.16.  5)  Sing. JcaT*  K.  oder  mit  arsuxZa-,  miuxZa-  sva. mq'^ra-  (Sp.  1178  o.),  'das  Wort,  das wahlgesprochene  Wort':  yä^a  lia  väHm Milma  (Sp.  1067  o.)  ya'^a  vä  saoiyatits Y.  70. 4;  —  zara%uitrahe  .  .  yS  paoiryS vacim  aoxta  vldsyum  akurS.tkaistnt  Yt. y.go;  90;  —  ^TKuxlam  vacim  yat  frä- dai^gat^gm  yasamaide  S.  2.  iS'"';  G.  2.  6; —  uita  tl  nsii  pairi.frasa  (sd.)  >rpzuxhm *p?rgsahi  VäHm  Y.g.as.  6)  "Einzel- wort,  (Plur.)  Wörter'  uzw.  der  GiJhäs"'>: tiiranam  haurva.paoiryanqm  (sd.)  häiliSla afsmanäca  vacasca  va^astaslim{sA.)ca  Vr. y.  3;  —  *ey3mcit  .  .  väcitn  gä^anqm asrvUm  (sd.)  N.  103;  — yS  gä^anqm  Byam vScim  afayäiti  alvqnt  v3  vacastaltXm  N. 4s\  42;  — ys  asnitgaoia  v3  ajravaoco  va nBii  Sim  Smm  väcim  *aiwyHs  (Sp.  378  0.)  \ .  .  yezi  äat  Syumpt  *väam  *aiwyas  1 anaiwilfi  (sd.)  astryeite  N.  i4-  Undeut- liche oder  wertlose  Stellen:  sar^yO  vaxs FrW.fj.i;  —'kaityavaca  FrW.5.2; — yS kaca  damayät . .*apastv6it  '^rilvayzibis^'^ ^haktni. .  N. 41 "';  —  xsvas  vayeibis^i N. 6j,  /OJ'J';  —  aAunavaitim  gshqm  .  .yasa- maide..  mal  vay£iby3^Va'*>  *pdübyasca V1.14.1;  YLz,  II,  13  (vacqm).  S.  noch vacim  bes.
```


## [2026-09-07T18:20:31.202Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN enough\" && grep -n \"enough\" KLN_1966.txt | head -20 && echo \"=== KLN1971\" && grep -n \"^enough\\|enough, adj\" KLN_1971.txt | head",
 "description": "Grep Klein for enough"
}
```


### [2026-09-07T18:20:31.276Z] TOOL RESULT

```
=== KLN enough
50:Most  etymological  dictionaries  do  not  pay  enough  attention  to  this  circumstance  and  there¬ fore  cite  equivalents  from  the  kindred  languages  quite  at  random,  often  enumerating  the  less important  ones  but  omitting  such  as  had  a  decisive  influence  upon  the  form  of  the  word  treated or  upon  the  development  of  its  meaning.  This  dictionary  tries  to  be  a  dependable  guide  to  the reader  in  this  respect  too,  by  giving  him  all  the  necessary  information  about  the  origin,  for¬ mation  and  sense  development  of  any  word  that  might  interest  him.
3673:Derivative:  assagai,  assegai,  tr.  v. assai,  adv.,  very  (musical  direction).  —  It.,  fr.  L. ad,  ‘to’,  and  satis,  ‘enough’.  See  assets, assai,  n.,  the  assai  palm.  —  Port,  assai,  fr.  Tupi assahy.
3696:Derivative:  assessor- ial ,  adj. assets,  n.  —  Orig.  a  singular  noun  fr.  OF.  asez (pronounced  asets)  (whence  F.  assez),  ‘enough’, fr.  VL.  *ad-satis,  ‘in  sufficiency’,  fr.  L.  ad,  ‘to’  (see ad-),  and  satis,  ‘enough’.  Cp.  O Proven?,  assatz, ‘enough’,  It.  assai,  ‘much’,  which  also  derive  fr. VL.  *ad-satis,  and  see  satis,  sad. asseverate,  tr.  v.,  to  affirm.  —  L.  asseveratus,  pp. of  asseverare,  ‘to  act  with  earnestness,  to  assert strongly’  (said  of  speech),  fr.  ad-  and  severus, ‘serious,  grave,  strict,  austere’.  See  severe  and cp.  persevere.
11053:bond’,  and  Syx oq,  ‘bend,  curve,  hook,  barb’. See  desmo-  and  onco-,  ‘barb,  hook’. Desmoscolex,  n„  a  genus  of  marine  worms  (hel¬ minthology).  —  ModL.,  compounded  of  Seapoi;, ‘band,  bond’,  and  axdtXTji;,  ‘worm’  (see  desmo- and  scolex);  so  called  from  the  globular  head, desolate,  adj.,  l)  lonely ;  2)  deserted ;  3)  laid  waste. —  L.  desolatus,  pp.  of  desolare.  See  desolate,  v. Derivatives:  desolate-ly,  adv.,  desolate-ness,  n. desolate,  tr.  v.,  1)  to  make  desolate;  2)  to  lay waste.  —  L.  desolatus,  pp.  of  desolare,  ‘to  leave alone,  forsake,  abandon,  make  solitary’,  fr. de-  and  solare,  ‘to  make  lonely’,  fr.  solus,  ‘alone, lonely’.  See  sole,  ‘alone’,  and  verbal  suff.  -ate. Derivatives:  desolat-ing,  adj.,  desolat-ing-ly, adv.,  desolation  (q.v.),  desolat-or,  n. desolation,  n.  —  F.  desolation,  fr.  Eccles.  L.  de- soldtidnem,  acc.  of  desolatio,  fr.  L.  desolatus,  pp. of  desolare.  See  desolate,  v.,  and  -ion. despair,  intr.  v.  —  ME.  despeiren,  desperen,  fr. OF.  despeir-,  pres.  sing,  stem  of  desperer,  ‘to despair’,  fr.  L.  desperare,  ‘to  lose  all  hope, despair’,  fr.  de-  and  sperdre,  ‘to  hope’,  fr.  spes, ‘hope’,  which  prob.  is  cogn.  with  OSlav.  spejq, speti,  ‘to  be  successful’,  spechii,  ‘endeavor,  as¬ piration’,  Lith.  speju,  speti,  ‘to  have  time;  to  be quick  enough’.  These  words  prob.  derive  fr. I.-E.  base  *spe(i)-,  *spi-,  ‘to  draw,  stretch, spread,  extend,  swell;  to  be  successful’.  See prosperous  and  cp.  desperado,  desperate,  Es¬ peranto.
13221:Derivatives :  enormous-ly,  adv, ,  enormous-ness ,  n. Enos,  masc.  PN. ;  in  the  Bible,  son  of  Seth.  — Gk.’Evco?,  fr.  Heb.  EnSsh ,  lit.  ‘man’,  rel.  to  Heb. nashtm,  ‘women’,  ish  (for  insh),  ‘man’,  Arab. ins  (coll.),  ‘men,  people’,  and  prob.  also  to Arab,  anisa,  ‘he  joined,  was  friendly’,  Akkad. eneshu,  to  unite,  join  (intr.) enough,  adj.  —  ME.  inogh,  enogh,  enouh,  fr.  OE. genoh,  rel.  to  OS.  ginog,  ON.  gnogr,  Swed.  nog, Dan.  nok,  OFris.  enoch,  Du.  genoeg,  OHG.  ginu- og(i ),  MHG.  genuoc,  G.  genug,  Goth,  ganohs, ‘enough’,  OE.  geneah,  OHG.  ginah,  Goth .ganah, ‘it  suffices’,  fr.  I.-E.  base  *enek-,  *nek-,  *nk-,  ‘to reach,  attain,  carry’,  whence  also  OI.  asndti, Avestic  ashnaoiti,  ‘reaches,  arrives  at’,  OI.  na- sati,  Avestic  nasaiti,  ‘reaches’,  OI.  drpsah, ‘portion,  part’,  Avestic  qsa-,  ‘party’,  Hitt,  nakish, ‘heavy’,  nikzi,  ‘rises’,  ninikzi,  ‘lifts,  raises’,  Gk. Jv-eyxeiv,  ‘to  bear,  carry’,  Srqvejo)?,  Att.  Siocve- y.ric,  ‘continuous,  unbroken’  (which  are  prob.  a contraction  of  *§ta-Tr)vexir)q  and  lit.  mean  ‘capa¬ ble  of  being  carried  through’,  fr.  8ia,  ‘through’, and  4veyxstv,  ‘to  carry’),  Syxo?,  ‘bulk,  size,  mass, body’,  L.  nancisci  (for  na-n-c-isci),  perf.  nactus sum,  ‘to  reach,  obtain’,  OSlav.  nesg,  nesti,  Lith. nesu,  nHsti,  Lett,  nesu,  nest,  ‘to  bear,  carry’, Lith.  nastd,  ‘burden’,  and  perh.  also  Toch.  A ents-,  B  enk-,  ‘to  seize,  take’.  Cp,  onco-,  ‘bulk, size’.
13222:Derivatives :  enough,  n.  and  adv. enounce,  tr.  v.,  i)  to  state  publicly;  2)  to  utter.  — F.  enoncer,  fr.  L.  enuntiare,  ‘to  divulge,  disclose, report,  say,  declare’,  fr.  e-  and  nuntiare,  ‘to  an¬ nounce,  declare’,  fr.  nuntius,  ‘messenger’.  See nuncio  and  cp.  enunciate.  Cp.  also  announce and  words  there  referred  to.
13223:Derivative:  enounce-ment,  n. enow,  adj.  n.  and  adv.,  enough.  —  ME.  inowe; an  archaic  var.  of  enough, en  passant,  by  the  way.  —  F.,  lit.  ‘in  passing’,  fr. en,  ‘in’  and  passant,  pres.  part,  of  passer,  ‘to pass’.  See  1st  en-,  pass  and  -ant. enquire,  enquiry.  —  See  inquire,  inquiry, enrage,  tr.  and  intr.  v.  —  OF.  (=  F.)  enrager, formed  fr.  1st  en-  and  rage,  ‘rage,  fury’.  See rage.
15731:Derivative :  galop,  intr.  v. galore,  adv.,  in  abundance.  —  Ir.  go  leor,  ‘to  suf¬ ficiency,  enough’.
16657:Murray  Cathcart  (1783-1859),  styled  Lord Greenock  (1807-43),  who  discovered  it.  For  the ending  see  subst.  suff.  -ite. greenovite,  n.,  manganese  titanite  (mineral.)  — Named  by  the  French  geologist  Ours-Pierre- Armand-Petit  Dufrenoy  (1792-1857)  in  1840 after  the  English  geologist  George  Bellas Greenough  (1778-1855).  For  the  ending  see subst.  suff.  -ite.
17007:rel.  to  aSivot;  (for  *sadinos );  ‘crowded',  lit. ‘thick’,  aS/jv  (for  *saden),  ‘to  one’s  fill,  to  sa¬ tiety’,  and  cogn.  with  L.  satis,  ‘enough’,  OE. szd,  ‘sated,  satisfied’.  See  sad  and  cp.  the  first element  in  Adephaga.
22478:macrocosm,  n.,  the  great  world,  the  universe.  — F.  macrocosme,  compounded  of  macro-  and  Gk. xoap.o<;,  ‘world’.  See  cosmos  and  cp.  microcosm, macron,  n.,  a  short  horizontal  line  placed  over  a vowel  to  indicate  its  length.  —  Gk.  paxpov, neut.  of  tj.ay.p6q,  ‘long’.  See  macro-, macroscopic,  also  macroscopical,  adj.,  large enough  to  be  seen  by  the  naked  eye.  —  Com¬ pounded  of  macro-  and  Gk.  axomriv,  ‘to  look at,  examine’  (see  -scope),  and  sulf.  -ic,  resp.  also -al.  Cp.  microscope.
26297:onco-,  combining  form  meaning  ‘barb’  or  ‘hook’. —  Gk.  oyxo-,  fr.  oyxop,  ‘barb  of  an  arrow, hook’,  which  stands  in  gradational  relationship to  Gk.  ayxop,  ‘a  bend,  hollow’,  ayxcov,  ‘elbow’, ityx’jpoc,  ‘an  anchor’.  See  angle,  ‘comer’,  and cp.  words  there  referred  to. onco-,  combining  form  meaning  ‘bulk,  mass,  tu¬ mor’.  —  Gk.  oyxo-,  fr.  oyxo?,  ‘bulk,  size,  mass, body’,  which  stands  in  gradational  relationship to  Gk.  ev-syxetv,  ‘to  bear,  carry’,  fr.  I.-E.  base *enek-,  *nek-,  ‘to  reach,  attain,  carry’.  See enough.
29153:pleonasm,  n.,  the  use  of  superfluous  words,  re¬ dundancy  ( rhet .)  — -  Late  L.  pleonasmus,  fr.  Gk. -Asrjvaau.oc,  fr.  TtXeova^Eiv,  ‘to  be  more  than enough,  abound,  be  superfluous’,  fr.  nXion, neut.  of  jtXeojv,  ‘more’.  See  pleio-. pleonaste,  n.,  ceylonite  (mineral.)  —  F.  pldonaste, fr.  Gk.  tiXsovaoToe,  ‘abundant’,  verbal  adj.  of nXEcvdc^eiv,  ‘to  be  more  than  enough,  abound’ (see  pleonasm);  so  called  by  the  French  mineral¬ ogist  Rene-Just  Hauy  (1743-1822)  in  1801  in allusion  to  the  number  of  faces, pleonastic,  adj.,  superfluous,  redundant.  —  Form¬ ed  with  adj.  suff.  -ic  fr.  Gk.  7tXeova<rroc;.  See prec.  word.
30632:prospector,  n.  —  L.,  fr.  prospectus,  pp.  of  prospi- cere.  See  prospect,  n.,  and  agential  suff.  -or. prospectus,  n.  —  L.  prospectus.  See  prospect,  n. prosper,  intr.  and  tr.  v.  —  ME .prosperen,  fr.  MF. (=  F.)  prosperer,  fr.  L.  prosperare,  ‘to  render happy’,  fr.  prosperus  or  prosper,  ‘favorable, fortunate,  happy'.  See  prosperous, prosperity,  n.  - — -  ME.  prosperite,  fr.  OF.  prospe- rite  (F.  prosperite),  fr.  L.  prosperitatem,  acc.  of prosperitas,  ‘desirable  condition,  prosperity’,  fr. prosperus  or  prosper.  See  next  word  and  -ity. prosperous,  adj.  —  ME.,  fr.  MF.  prospereux,  fr. L.  prosperus  or  prosper,  ‘agreeable  to  one’s wishes,  favorable,  fortunate, happy’,  prob.  form¬ ed  fr.  prospere,  for  OL.  pro  spere,  corresponding to  L.  pro  spe,  ‘according  to  expectation’,  fr.  pro, ‘for’  (see  1st  pro-),  and  abl.  of  spes,  ‘hope’,  which is  cogn.  with  OSlav.  spejq,  spSti,  ‘to  be  success¬ ful’,  spechu,  ‘endeavor,  aspiration’.  Lit.  speju, sped,  ‘to  have  time,  to  be  quick  enough’,  OE. spedan,  ‘to  be  successful,  make  successful’,  sped, ‘success,  prosperity',  spowan,  ‘to  prosper',  fr. l.-E.  base  *spe(i)-,  *sps-,  ‘to  draw,  stretch,  ex¬ tend,  swell;  to  be  successful’,  whence  also  L. spatium,  ‘space’.  See  space,  speed  and  cp.  des¬ pair,  desperate,  Esperanto.  For  the  ending  of prosperous  see  suff.  -ous.
33461:sacrum,  n.,  bone  at  the  lower  end  of  the  spine (anal.)  — —  ModL.,  fr.  os  sacrum,  ‘the  sacred bone’,  from  mistranslation  of  the  term  occur¬ ring  in  Galen:  Esoov  ootouv,  ‘the  strong  bone’, into  ‘the  sacred  bone’.  For  the  difference  be¬ tween  Gk.  iep6g,  ‘strong’,  and  Ecpo?,  ‘sacred’, see  Boisacq,  DELG.,  p.  368. sad,  adj.  —  ME.  sad,  ‘sated,  full,  satisfied,  tired’, fr.  OE.  sted,  ‘sated,  satisfied’,  rel.  to  OS.  sad, ON.  sadr,  MDu.  sat,  sad,  Du. zad, OHG.,  MHG. sat(t),  G.  sat t,  Goth,  saps,  ‘satiated’,  fr.  I.-E. base  *sa-,  *ss-,  ‘satisfied,  sated’,  whence  also  L. satis,  ‘enough,  sufficient’,  satur,  ‘satiated’, OSlav.  sytu,  Lith.  sotiis,  of  s.m.,  Lith.  sdtis,  ‘sa¬ tiation’,  Olr.  sdith,  ‘satiety’,  saithech,  ‘satiated’, Gk.  a$r,v  (for  *saden),  of  s.m.,  aero a  (for *saetai),  ‘satiates  himself’,  Sax-toq  (for  *n-s{'- tos),  ‘insatiable’,  01.  a-sin-van,  ‘insatiable’, Toch.  B.  soy-,  AB  si-,  ‘to  be  satiated’.  Cp.  as- sai,  assets,  hadro-,  sate,  satiate,  satis,  satisfy, saturate,  soil,  ‘to  feed’,  and  the  first  element  in Adephaga.
33783:Derivative:  satchel-ed,  adj. sate,  tr.  v.,  to  satisfy,  surfeit.  —  Prob.  a  blend  of obsol.  E.  sade,  fr.  OE.  sadian,  ‘to  satiate’,  and L.  sat,  satis,  ‘enough’.  See  sad  and  cp.  satiate, satis.
33792:satiate,  adj.,  satiated.  —  L.  satiatus,  pp.  of  satiare, ‘to  fill,  satisfy’,  fr.  satis ,  ‘enough’.  See  satis  and adj.  sutf.  -ate  and  cp.  sate,  ‘to  satisfy’, satiate,  tr.  v.  —  L.  satiatus,  pp.  of  satiare.  See prec.  word.
33793:Derivative:  satiat-ion,  n. satiety,  n.  —  MF.  (=  F.)  satiete,  fr.  L.  satietatem, acc.  of  satietas,  ‘sufficiency,  abundance’,  fr.  sa¬ tis,  ‘enough’.  See  satiate,  adj.,  and  -ity. satin,  n.  —  F.,  fr.  Arab,  atlas  zaytunt,  ‘tissue brought  from  Zaitun,  Arabic  name  of  the  Med¬ ieval  Chinese  shipping  port  Tzu-t'ing  (later  call¬ ed  Chuanchow,  now  Tsinkiang),  in  the  province Fukien.  F.  satin  was  prob.  influenced  in  form  by It.  setino,  a  word  of  identical  origin,  but  assim¬ ilated  to  seta,  ‘silk’.  Cp.  sateen.
33795:of  satin.  See  satin  and  -et,  -ette. satire,  n.  —  MF.  (=  F.),  fr.  L.  satura  (also  satira ), for  satura  lanx,  ‘a  dish  filled  with  various  kinds of  fruits;  mixture,  medley;  satire’  (first  applied in  this  last  sense  to  a  collection  of  various  poems by  Ennius);  not  related  to  satur,  ‘full  of  food’, satis,  ‘enough’.
33799:Derivative:  satiriz-able,  adj. satis,  adv.,  enough,  sufficient.  —  L.,  rel.  to  satur, ‘satiated’,  and  cogn.  with  Goth,  saps,  ‘satiated’, OE.  seed,  ‘satisfied’.  See  sad  and  cp.  words  there referred  to.
=== KLN1971
82672:enough, adj. — ME. inogh, enogh , enouh , fr. OE. 
142392:enough to be seen by the naked eye. — Com- 
167041:enough. 
184746:enough, abound, be superfluous’, fr. 7tX£ov, 
217649:enough’, parvus, ‘small, little’; see parvi-. Cp. 
236214:enough, suffice’, lit. ‘to make under’, fr. sub- and 
269270:enough.
```


## [2026-09-07T18:20:48.421Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /1067/ && /nas/ {print NR\": \"substr($0,1,200)}' BRT.txt | head -20",
 "description": "Find BRT leaf with column 1067"
}
```


### [2026-09-07T18:20:49.691Z] TOOL RESULT

```
686: .2^.        b)  die  Aussage  geht  auf  I  (Sp.  9  u.)  i'kä  vansaia  yi  data  ofahsus
druxi  naiäite  (Sp.  1067  m.)  y  aiwiat jayma^  ". .,  von  wo  sie  herzugekommen war"  Vti^.  r2.
Able
```


## [2026-09-07T18:20:50.173Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1nas-\\|2nas-\\|nas-\\b\" BRT.txt | head -30; echo \"=== naš\"; grep -n \"asnaoiti\\|aSnaoiti\\|asnaoiti\" BRT.txt | head",
 "description": "Grep BRT for nas- root"
}
```


### [2026-09-07T18:20:50.241Z] TOOL RESULT

```
18752:Pö.  {ru  SrB.l:  nasüaH-.Ua  V.  10,  32.  4,  5/,: Haseitäan,  erL  (lu  V.  /o-  1 5) :  a/aitai  iar.-jir, (10  Y.  J3.  4I:  la/üi  iar/an;  (lu  Y.  J?.  IS  : ♦m™*)  bülan,  Sü.;  amrli^aniyg  bhavati;  s. noch  N0.3-S,—  'j  S  -So.  *39-  7  c.—  »)Sutt 'nasya  gescbr.,  S  2**-  3*-  —  ■»  Part,  des i-Aor-  in  foloriscbem  Sinn  (vgL  la  a^imitS Vt.  /J.  66,  'a«-  No.  51;  ebenso  ist  nii^mnu Yu  /j.  5S,  Vyt.  2g  gebraacht  (10  'nas-';  s. nac\i  za  Jich.i-  No.  Z,  *tü}tay-  and  tisJjiaitt. —  Pu. :  ai  . ,  ia  iarfi  taiit  ö  Si  ahnn;  Sü.: ahau  .  .  iaievarom  vinäiayati  (LS.)  punyät- manai.  —  4)  Pü. :  fa  aft  iaiiiaiA  rat ;  i.  tu t<aili.vmttiiä-.  —  J)  Pü. :  nndeutlich;  MiLLS G.  387  itaX  arasi4ii;SiX.t\.:  m^ly-um  fräfn.ti.  — *)  Sol  Gescbr.  anbdnn.  —  7)  näUmim-  als Part,  des  Fulars  id  fassen  {^laAiaJav-  No.  1) hindert  mich  die  Länge  des  Wurzelvokals, die  vielmehr  auf  den  i-Aoiist  weist. j.,  g.*nas-V. 'hingelangen ZU— '.  Praes. 3  nasa-,  4  nOia-;  .r-Aor.  i  näs-;  PfPr, tsa-,  —  Int  °näs)m. i)  'erlangen,  «reichen':  Hat  K  nürqm aht/an3  urva&im  (sd.)  na- um  den  Wendepunkt  zu  er-
=== naš
7828:m\i paiti  '(mit  einer  Waffe)  treffen':  yat dim  aZnö.manatiha  paiti.asnaoiti  aetat  lis andus  (sd.)  V.  4. 1 7.
```


## [2026-09-07T18:20:55.638Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=18700 && NR<=18800' BRT.txt | tr '\\f' '\\n@FF@\\n' | head -80",
 "description": "Print BRT nas- area"
}
```


### [2026-09-07T18:20:57.093Z] TOOL RESULT

```
hanfa  .  .  afym  staoiti  "wenn  man  , ,"  H, J.  7 ;  —  hyat  n  a  /ryli  vasiamnö  isvä  (sd.) daidlt  Y.  43.  14;  — yat  nä  paurva  frahda (sd)  .  .  fi-amaaaiti  V.  18.  40J  34,  37,  46, 49i  54  (Sp-  Sao  u.);  —  ya%a  na  snaüi/ . .  nifmatfm  (Sp.  500  m.)  paiH.valnoit  P. 21;  YL13.JO,  71,  aa)  In  gleichem  Sinn erscheint  auch  NP.:  äai  mqm  narB  . . yazmte..  darrfB.yast»m(sd.)/a  .  .  H.2.  14; Vd.iS;  —  ^aj  ta  (Sp.  6ia)  nara  yaos- dayqn  aahm  .  .  ya  nasaum  avahistät "können  die  Männer  (sva.  kaim  man)  puxi- fizirt  werden  .  .,  wenn  man  . ."  V.  5*.  33; 35.  97.  7-"3.  "5-
Aus  dem  Zusammenhang  gerissene,  un- deudiche,  verderbte  oder  wertlose  Stellen mit  nar-.  «flr/(GS.)  ..  nara  (ND.)  .. «(jr?(NP.)  F.  2e;  —  «3  Fsd;  — nanm ..sar>t)m  V.^.  14  PüZ'J»;  N.52"';  — panca  narB  V.  75.  loPüZ.;  Vyt.  42,  Vd 13,15;  —  dva  nar^FiB.; — para  "iafah- mät(sd.)  n»r>t  (AblS.)  V.  j.  42  PÜZ.;  — aBsqmia  naram  V.  5.  gPUZ.;  —  ham.- tapiibyB  aiwys  caxrart  (sd)  n^r^byB  V. 4. 4  7 ;  I  o  PiiZ. ;  —  tl  ^narsS paitismarmitm Vy^  52;  —  nöil  dim  "nara  . .  avasyil  Yt /.  aS;  — ya'ia  na  ttäifyaY.  20.  2;  Yyt  28, 30.  narSm  nartm  als  Adv.  sbes.  [N. 301  streiche  «a.J
Komj>A.,  E. ;  AbleiL  —  ai.  nä,  nirah,  n/iliyah ;
dby  Google
"nara
nairyö.sanha-
1054
np.  nur.  —  Pü.:  mar/;  s.  noch  No.  10,  16-31.  — ■}  Die  einielnen  Bedeutungen  sind  nicht  immer streng  auseinanderzuhalten.  —  >)  Them.  Vgl. ai.  nara^  NS.,  usw.  —  3>  VgL  lu  nars  gAw. Bwj  und  Abis,  mnl;  Bthl.  IF.  5.  J63.  — 1)  Hds.  mrtgä  raydii.  —  S)  Vgl.  va  sava:  —
—  *>  S.  datu  nurobr.  nerf  'principes'.  — 7)  Pronominal  flcktirt?  —  8)  5  a6^_  54.  _ 9)  Vg).  Dbr.  VgJS.  /.  421.  —  ■")  Pü.!  lässt das  Wort  aus.  —  ")  Hds.  n<üri.  —  n)  Also GS.  an  Stelle  des  AR!  —  >J)  Hds.  nairi.  — M)  S  268.  41.  —  "s)  S.  daiu  Gdn.  BB.  14- 14.  —  16)  Pü.  hat  fiit  tasnä  nur  ki,  wie  Tür ii  allein;  ».  No.  ZO.  —  '7)  Pu.:  1  oniä^,  SU.: asmäiant.  —  18)  Hds.  Aaonä;  Pü.;  ön  mar/. — '9)  Die  beiden  Worte  fehlen  in  der  Ausg.; aber  T  hat  srao%rana  undPü. :  mart..gäiäri sräyiSn.  —  lo)  Pü.  nur  ii;  s.  No.  16.  —  "•)  Hds. vtt,  aber  Pü.  mart.  —  ")  Hds.  iä,  aber  Pü. marl.  —  'S)  Wohl  vetstümmeltes  Zitat;  s. P.  2J.
•  j.  ^vasia  /laoa  nara  /aca  mara  ^aSo näjanasus"  Yti2.8.
•  j.  "naratö  ifr^^m"  N.  46,  gj  (wo Jtarai^in),
Anscheinend  verderbtes  Zitat.
•  g.  naräm  nar^m  Adj.  'MannfiirMann, mlinniglich' :  sraota..n'  n°  i^ahyäi  lanuyi .  .  ahniäi  nS  sasdyäi  (sd.)  baodantd  paiij Y.30.3.
Ein  ämreißam;  AS.  aus  »flr-.  —  Pü.i  ki  marl
•  j.  narava-  patr.  Adj.  'von  Narav  stam- mend, dessen  Nachkomme' " :  ayraira^ahe °vahe  Yt  13.  131 ;  g.  18.
Ableit  aus  "tiarav-  m.  EN.  —  0  Anders  DsT. ZA.  3.  433.
•  j.  naircmanah-  Adj,  'mannhaften  Sinns' : °ni  ktnsäsps  Y.  g.  11,  Yt.  j.  37,  1$.  aj, ip-3^,  44*-
Slfttl  *nairya-m' 
 geschr.;  S  2ÖÄ  3*.  —  Vgl. ai.  H^mänas-  Adj.  —  Pü. :  mart  minisn,  erL : tus  dl!  pa  gas  däsl.
].  fiaili.naröiS  N.  Ö5:  lies  fnlli-barSis.
•  j.  *narö.vaeipya-  *'  Adj.  'päderasterisch': a'/a  anap?r3^a  fyaoiina  yS  °ya  V.  /.  1 1.
Ableit.  aus  *narv.i'ii^-  m.  'Päderastie';  zum V.  vacft-,  —  Pü.!  mart  vefili,   eri.:  tun  marz.
—  ')  So  Jp  I.     NA,  'vaifaya.
"  j.,  g.  narap-  V.  'abnehmen',  vom  Mond. Praes.  14  mrifia-.
is  yä  mä  ttxfyei/l  mnfsaitt  %'wal  (sd.) Y.44.%; —  k(ü  mh  mrifsmtii  . .  paiica.- dasa  tnä  n^n/saiti  Ytj.  2;  —  tunfsatä- (nur  Ableit.).
Pü. :  nir/sitan,  mit  der  np.  Glosse :  Um  hidan;
NpÜ.:  täsla«;  Sü.j  «imWiim,  (luVt.)i  kinyali
3S.  (statt  »liyatij.
•  g.  narapis-  n.  '(Verminderung  sva.) HcTabwürdigung,  Herabsetzung'  *\  mit  Akk. verb.:  iöi  'pis  (AS.)  *ar»jU  akasä  (sd.) (isjlt.anlä  Y.  53.  9.
Zum  V.  nartp:  —  Pü, :  :*/  m  i  15  dastawar nirfsenend  ('sie  vermindern')  vai  ..  .  —  •)  Vgl. lAusdr,  nnter  kasyah-  a.
•  j.  nairya-  Adj.  (fem.  'ryä-)  'virilis'; i)  'männlichen  Geschlechts';  a)  von  Men- schen; dva  nara  us.eayeirtie  mHwana (sd.)  strica  'ryasca  V.  2.  41 ;  —  yezi  °ryS afihat  ..yezi  strJ  atshat  V.S.  $S;  —  däya ml  .  .  'ryqm  3snqm  */razaintlm  \.6S.$;
—  'rySraiu!..  N.5(?).  b)von Tieren: m^rsya  .  .  mi^wana  strica  'ryasca  "V,  iS. *8;  iJ-Si  (von  Hunden).  2)  'mann- haft', von  hqm.vaniay-  f.  (sd.,  auch  fdSL): -re  (NSf.)  hqm.vanitis  \t.io.b()  usw.;  — 'ryqm  Aqm.vaniim  Yl  ig.  39  usw.;  — °ryayä  Aqtn.varytsis  S.1.32;  —  ha'hra °rya  (ISf.)  kqnt.vania  Yt  io.  71; — 'rya- yälparB  /tqm.v»rytoii  Yt  ig.  38.  S.  noch unter  nairyS-saaAa-  mit  No.  i.
KompA.  —  Ableit.  aus  nar-.  —  ai.  nörya- Adj.  —  Pü.:  nar,  (lu  Y.  68):  i  martä»,  (lu N.):  fehlt.
•  j.  nairyö.näman-Adj.  '(mit  männlichem
Namen  sva.)  männlichen  Geschlechts',  von Tieren;  hazanräis  jJ!nr/(sd.)  strl.nämanS ..  -manaitiP.)  V. 13.51,  l4-iG\.  Wert- los; ani>iaHbyS  .  ,  yS  asti  yazatanam  . . *'manh'^Yt4.Z. FB.  (lu  V.):  iiar  näm ;  s.  noch  No.  i.  —  >)  So F  1 ;  NA.  ray5.it',  vgl.  Npü. :  xälis  n.inii.
•  j.  nairy5,saoha-'>  m.  Name  einer  Gott- heit {Yazata),  die  des  Götterbotenamts waltet;  *'hs'^  ..  astö  mazdä  ahurahe  "J^., der  Bote  des  AhM^  V.  ;p.  34;  34;  — nairyS.sarjAs  (statt  Dat )  aocayata  yS  dmva ahurS  masdh:  nairya  sartha  '*  vyHxana  . . imal  saiihsil  airyamanai  V.  22.  7;  13;  — sraosasca  ,  .  °hasca  yd  mayu^{sA.)  Yt  10. 5a;  —  apqm  naptärsm  . .  nairim  sanfum  '> Y.  77.  23;  —  sraohm  ..  nairimca  saa/ifin'^ huraohm  Y.  57.  3,  Vyt^o;  Vr.  7.  i;  — sraolake  ,  .  nairyeheca  sat?haAe'^  Vr.  is. 16;  — yqmca  (räml.  Jrava/lm)  srao/aAe ..yqmca  nairyeAe  saaAaAe'^  Yty.Sj;  — Xfa%r»n.nafolrfm  "Atm  yazattm  Y.  77. 1 1 ;
—  xl<£ä:rd.naf^r5  'kaAe  yazatahe  üy.^.S. •)  Wie  der  indische  ^^nü.    In  der  Tat  steht
n'  in  y.  7/  unter  den  Namen  für  Feuer.  Vgl. ai.  HÖräJämia-  und  Gray  AfB.  j.  45,  OLDEM- RBKO  ZDMG.  S4-  49-  5.  noch  die  GrBd.-Stelle bei  DsT.  ZA.  S.  319-
dby  Google
I055     naiiyam-ham-värativant-
Eig.Bed.?i),
056
viaA  (alt  Hawunanie,  apa  dnixs  tuue  apa  . .  thära  apa  .  .  vi-
  „    _.  Tgl.  KÖräJämia-O  m.    Name   des  „-,«  ^-.CfA  1>)    QiR    t
Feneri   -    p1:  öaiuskr.    -    ■)  Oders  mit  ««''.("'*.)      falB  J.
TrennoDB  der  Glieder,   wobei   dis  erste  den  mit  3  ond/ßz-J  'der  Vcmichtung  anhcim
cDtipreiibnideii   Kamsansging   erhill:     i>fli<-  (allen':  fiaracä  mruf^-as  (sd.)  aurJcii  jrj'^rtl
laaAiiAe,     nairyekeia    i'    neben    nairyl.'  mainyui  dr.gvatS  aiiasat  parä  "wo  , .  der
^J"  Geist  des  ^/:i(f^enosseii  der  Vemichtung
.  aoheim  fallen  wird"  Y.5?.  7°,
S.  Qocb  za  f>i.. «afiar-,  ibailah-,  haela-  nnd  No.  4-  - getreoDtT   —    j»   Der  Vetf.  t
klärte  xich  das  W»rl  jedenfalls  als  'männlicbi Rede  fahrend'.  Die  DeDtnng  GIrPh.  3.  6^2 halle  ich  für  falsch.  5.  noch  No.  4.  —  *}  Zorn ai.  Wort  inleUt  Fav  JAOS.  j6.  clxxu  (mit Mbr  bedenklicher  Elymologie)  und  Oldek- BERC  ZDMG.5^51  (aus  'narämiamiah;  also Dissimilation  t).
'dem  Untergang  verfallen':  aiiüisu i.Hinasa  yJ  iarapJjSsi^'täl  ..  Y.J2, 15.
Pö.  {ru  SrB.l:  nasüaH-.Ua  V.  10,  32.  4,  5/,: Haseitäan,  erL  (lu  V.  /o-  1 5) :  a/aitai  iar.-jir, (10  Y.  J3.  4I:  la/üi  iar/an;  (lu  Y.  J?.  IS  : ♦m™
*)  bülan,  Sü.;  amrli^aniyg  bhavati;  s. noch  N0.3-S,—  'j  S  -So.  *39-  7  c.—  »)Sutt 'nasya  gescbr.,  S  2**-  3*-  —  ■»  Part,  des i-Aor-  in  foloriscbem  Sinn  (vgL  la  a^imitS Vt.  /J.  66,  'a«-  No.  51;  ebenso  ist  nii^mnu Yu  /j.  5S,  Vyt.  2g  gebraacht  (10  'nas-';  s. nac\i  za  Jich.i-  No.  Z,  *tü}tay-  and  tisJjiaitt. —  Pu. :  ai  . ,  ia  iarfi  taiit  ö  Si  ahnn;  Sü.: ahau  .  .  iaievarom  vinäiayati  (LS.)  punyät- manai.  —  4)  Pü. :  fa  aft  iaiiiaiA  rat ;  i.  tu t<aili.vmttiiä-.  —  J)  Pü. :  nndeutlich;  MiLLS G.  387  itaX  arasi4ii;SiX.t\.:  m^ly-um  fräfn.ti.  — *)  Sol  Gescbr.  anbdnn.  —  7)  näUmim-  als Part,  des  Fulars  id  fassen  {^laAiaJav-  No.  1) hindert  mich  die  Länge  des  Wurzelvokals, die  vielmehr  auf  den  i-Aoiist  weist. j.,  g.*nas-V. 'hingelangen ZU— '.  Praes. 3  nasa-,  4  nOia-;  .r-Aor.  i  näs-;  PfPr, tsa-,  —  Int  °näs)m. i)  'erlangen,  «reichen':  Hat  K  nürqm aht/an3  urva&im  (sd.)  na- um  den  Wendepunkt  zu  er-
•  j.  nairyf^niJii^.vänti'vant-  Adj.  'der ' mannhafte  Tapferkeit  besitzt*;  tir7zSJa-\ man^m  Tantum  taxtnpm  Yt.  ig.  42.
Vgl,  nairyifm  hnm.mirji/im  und  hqm.varilha'ö; anflitltge  Bildung;  ■.  Richtsr  IF.p.  204.
•  j.,  g.  'nas-  V.  'verschwinden'.  Praes. 26  nasya-,  Perf.  1  «Äiir-  :  nas-;  PfPr. nrsa-,  j-Aor.  i  nä/-.  —  PFfP.  nasta-, °n3xsta-''>.        Vgl.  noch  II  viyanattty<^,
i)    'verschwinden,    sich    fort    machen, weichen',  a)  absolut:  ffawCaSIA.)''  daivi druxs  Siß.  3;  J^;  —    natyät  drvxs' Ytj. 17;  —  vispa  druxs  ni^äiti  Yt  2. 1 1 ;  —  , maire  näsaite  Yt.^.  8;  —  *aia'jca  *maire   ■ näiätalca  mairyS  Vl  ig.  12.  b)  Von  -
weg,  aus'  ('totra  mit  Abi.) :  nasyäti  iaira fräktr^sla  ahmat  haca  nmänäl  ähitis  Y.  \/ravat?nti
lO.j,  2)  'abgehen,  abweichen  von  — '  /tmtia'^  ", .  —.  ^^^  ..^,.^.k>^»<-  —  — (Abi.):  ma/yä  . .  mandä  aAurahyä  xratSui  reichen"  Yt.  JJ.  58; —^j^Ja  aspa.. aparat nasyan/S  as'Ja/ä  "..^e  von  des  MAA.\^aca  urvauäl  fralar^m  unaism  *nä- Willen  abgehen  und  vom  heiligen  Recht"  ij-v^na')')  ",  .  Rosse  die  .  ,  den  vor- Y.^2.4;  —  urvä  ..  *"d<y  .d''W^'"»«"'ideren  Wendepunkt  erreichen  wollen"  Vyt Mtvasca  {sd.)  asahys  nqsvä  pa'hs  y.  si-\2g.  2)  'empfangen,  annehmen':  tarn 13;  —  dus^arma  näsle  ratisla  (sd.;  ..  vistäsps  ..  nasaj  . .  yam  cisim  {sd.)'.. liistr.  sutt  Abi.)  Vtjo.  105.  3)  'ver-  Y.j/.  16.  3) 'es  erreichen  zu  (werden)', loren  gehen,  abhanden  kommen';  vays.-  ^it  inf..  p^^rä  af/,3  snäxM  (^Sj-AofM, lundubyll  {sA.)  Atij^an^Sm  nasal  j^ä-  K\igni.y  yäis  srävaAyäii{sd.)  V.32.6. :itv>m  dr^^ff.d?6yS  Y.53.6;  —  s.  noch  „jt  aiwi  'erlangen,  bekommen':  y^ nasla:         4)    'zu   Grunde   gehen':   faiti  *pailismannle    yä    ^aiwinäsmie    vankai
. .   vadar»  (s '
fideli  . ."  V.(j.  30;  —  s.  noch  'anaxsla-. mit  apa  i)  dnwS.  la:    apa  druxl  nase
(iSIA.)*»..«/J^«(sd.)a/an«J)'Ä*^(2SKM.)
.,/      —    «.      g   .    j        j/aimniarvntc     ya       ai^ariimi^mie     i/av/iut
'pim  na/^mnäi^  alaone  kaoma  yasnasca  vahmasca  Y.23. 3;  —  aiwinasant- (sd.)  /ai<,i   ".  .  pro   perituros»  (Ableit).
Ü.  näiaii
,  näkfaii.  —
Vgl.  v.
_  pa.  (lu
aHäna  6älan,   (in  Y.
noch  lum  :
nf.    -    '
VgL  tn  'na
■^0-  3.  7
—    »>  Hds
nabmfa
-  ä  Zorn
».  S  i •  g.  %a8-  f.  "Not,  Unglück':  apas^a  vä  .
V
```


## [2026-09-07T18:21:07.410Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1065\\|1066\\|1067\\|1068\\|1069\" BRT.txt | head -30",
 "description": "Find BRT columns 1065-1069"
}
```


### [2026-09-07T18:21:07.472Z] TOOL RESULT

```
18909:Täx^na.y-  1066
20853:vaoiä  (sd.)  ys  Im  dät  "novi  (cum)  qiii .  ■" Y.45-4;  ö,  31.  19;  —  *malni/(sd.)  ys dngvaiU  xsä^rfm  Aun{iiil(sd.)  . .  yS  nöii jyUtam  (sd)  vlnastl  .  .  "poena  (eius)  qui . ,  eius  qui . ."  Y.JJ.  15;  —  rumanhä  (Sp. 1068  u.)  y!  . .  cista  yS  .  ,  dasdl  "respec- tuosus  (ei)  qui.."  Y-Jl-Sf.;  8; — yekya {zu  3)  iavS  isänii  . .  ySi  . .  *a»haricä dvaHti(ßd.yä  ". .  (ei)  qui  . ."  Y.  45. 7;  — yeAy3  . .  vahiibm  . .  valäs  maidä  . .  ySi äaharfcä  htnücä  "cuius  .  .  (eonim)  qui fuerunt  et  sunt"  Y.j/.  aa;  —  pirisä  ySi pi^yeitUI  (sd.)  "interrogo  (eps)  qui  . ."  Y. 44.  JO;  —  ä  vS  *gSus.ä  ÄsmyarUa  ySi  . . sännti  .  .  yassqm  ta  .  .  fradaxlts  akl ". .  (cum  üs)  qui  . .  quorum . ."  Y.5J.  3;
21104:druxi  naiäite  (Sp.  1067  m.)  y  aiwiat jayma^  ". .,  von  wo  sie  herzugekommen war"  Vti^.  r2.
22272:pars  vay&ibyö^'*  YLjo.88; —  *ao^rab}'B ariuxialibyasca  vSyiibyB^^  vufitn  .  . yazatitn  yasamaide  Y,i6.  i;  Vi.  6.  i,  Ny, J.  1 6;  —  Avamxiaft?m .  .yaxamaide  vacaca ^ao^naca  sao^rabyasca  N.1.16.  5)  Sing. JcaT*  K.  oder  mit  arsuxZa-,  miuxZa-  sva. mq'^ra-  (Sp.  1178  o.),  'das  Wort,  das wahlgesprochene  Wort':  yä^a  lia  väHm Milma  (Sp.  1067  o.)  ya'^a  vä  saoiyatits Y.  70. 4;  —  zara%uitrahe  .  .  yS  paoiryS vacim  aoxta  vldsyum  akurS.tkaistnt  Yt. y.go;  90;  —  ^TKuxlam  vacim  yat  frä- dai^gat^gm  yasamaide  S.  2.  iS'"';  G.  2.  6; —  uita  tl  nsii  pairi.frasa  (sd.)  >rpzuxhm *p?rgsahi  VäHm  Y.g.as.  6)  "Einzel- wort,  (Plur.)  Wörter'  uzw.  der  GiJhäs"'>: tiiranam  haurva.paoiryanqm  (sd.)  häiliSla afsmanäca  vacasca  va^astaslim{sA.)ca  Vr. y.  3;  —  *ey3mcit  .  .  väcitn  gä^anqm asrvUm  (sd.)  N.  103;  — yS  gä^anqm  Byam vScim  afayäiti  alvqnt  v3  vacastaltXm  N. 4s\  42;  — ys  asnitgaoia  v3  ajravaoco  va nBii  Sim  Smm  väcim  *aiwyHs  (Sp.  378  0.)  \ .  .  yezi  äat  Syumpt  *väam  *aiwyas  1 anaiwilfi  (sd.)  astryeite  N.  i4-  Undeut- liche oder  wertlose  Stellen:  sar^yO  vaxs FrW.fj.i;  —'kaityavaca  FrW.5.2; — yS kaca  damayät . .*apastv6it  '^rilvayzibis^'^ ^haktni. .  N. 41 "';  —  xsvas  vayeibis^i N. 6j,  /OJ'J';  —  aAunavaitim  gshqm  .  .yasa- maide..  mal  vay£iby3^Va'*>  *pdübyasca V1.14.1;  YLz,  II,  13  (vacqm).  S.  noch vacim  bes.
30170:•  j.,  g.  hu-xratav-  Adj.  'des  Einsicht  gut ist,  ems  ich  tsvoll':  haomö ..  •tus\.g,  23;  — fratanmät  lg  (näml.  haomahe)  havamm  . . 'tvSiyS.)  Y.10.2;  3; —  vastryö ^ao^anäii snsvS  hqs  'tul  ntmanhä  (Sp.  1068  u.)  Y.
```


## [2026-09-07T18:21:19.487Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=18880 && NR<=18960' BRT.txt | cut -c1-1200",
 "description": "Print BRT leaf around column 1066"
}
```


### [2026-09-07T18:21:20.657Z] TOOL RESULT

```
•  j.,  g.,  p.  näman-,  j.  n^tnan-"  n.  "Name":
äat  hi  'ma  fradai^yh  atr».dät)m  vä  . . Aqmät  va  ii/rf.dä/aAe  (sd.)   'ma  V. /Ä53;
dby  Google
1063  lumoan-  AI
Vd,/}";  —  ya^qmca  pars  mafyaia  ahoi- ta^a^a{&A.)..gaitinqm  'mqm{AS.)  däian Yt  IQ.  6;  —  yä  vs  vamtkU  (nämL  äp5) ahurS  mazdä  *°mqm'^  dadäi  .  .  täii  vi yazamaiäl  Y.  ^JÄ  4;  —  tq  yazsi  ifaii •w»ir/(IPO  pairicä  jasüi  (sd.)  vanta  Y. 57,22;  —  hyat  vä  töi  'manqtn  vözObm atan  . .  tä  äjoj  pairijasumaidi  Y.  j6'.  3;
—  anusS  ipfnti  vaakBi  sflräU  'mqn  (als IP.)  äiii^a  Y.  75.  1,  Vr.  tf.  i;  —  'tSm  .  . ahüirys  °«Är(als  IS.)  magda.vars  (sd.) . . yasamaiäf  Y.jj.^;  —  'mini  spu  yaza- maide  YtJ^,  79:79';  —  kaAe  nS  ila •ma  ayairydiiSp.  512  m.)  Yty.50;  — ahmä^m  'ma  . .  yat  amsSanqm  spintanqm tat  asH  mq^rake    spmiahe  amavästtmim
•  Yt7.3; — frsit  mg  tat  'ma  framrüm  Yt /.  S;  — yasia  me  .  .  tmi  •inlnli  (als  AP.) drfftJayS  . .  Yt/.  16;  11,  15;  —  ^vjsqs *taia  imi  'msnü  (als  NP.)  parltas^a  '.  . vismie  Yt /.  19;  —  l&sca  mg  °ma  (AP.) abaya^a  Yti5. 49,  50;  —  gSusca  'ma mazdaoätfm  Yt  Ä  2 ;  —  'mSni  amslanqtn sptnianqm  Ytrf-a;  7;  —  sPaitka  va  duyta va  'va'ni  V.  14. 15  (?) -ö.  a)  AS.  und  LS. (im  Sinn  des  IS.)^*  als  Adv.  'mit  Namen'; i)  im  jAw.  AS.  nqma,  hinter  dem  Nom. propr.ä':  iar^zahi ..yat  vaolii^A^ häkairJm °ffio  Yt/0.88;  12-7,  i^-SS';  — pairikayai .  .yS  duzyairya  yqm  mafyaka  . .  Auyäiryqm 'ma  ao/aiti!  (sd.)  YtÄ  51;  V. /j.  z,  6;  — tturf/S  .  .  yim  ma^aka  .  .  kahrkatas  'ma ac/ai/e  (sd.)  V.iS.i$;  17.31  —  vayui  bä 'ma  äkmi  Yt  75.  43 ;  43-48  (oft),  /.  7,  8, 12—15  (oft);  —  vairil yB  haosrava  'ma YtJp-sö;  59,62,  7.30,7^,129',  142,74. 59*,  V, /i".  15;  —  ar?dvi  'ma  apa  V.7.16;
—  ahm.ye^he.raocä  'ma  aiaonS  /ravalXm Yty.i2o;i2o'; — hinter  demNom.appelL: vJzari^  dagvs  'ma  N.ig.ii).  2)  Bim Ap.  LS-,  uzw.  a)  näma",  b)  namä";  ersteres folgt  dem  Namen  eines  mask.  oder  neutr., letzteres  dem  eines  fem.  Appellativs*'; a)  nämtf;  sowohl  der  Name  als  das Appellativum  stehen  unter  allen  Umständen im  Nominativ'';  al  das  Appellativum  geht voraus :  i  martiytr  magui  ähJ'  gaumntJ' •wo"  Bh.J.ii;  i6',  2.3,  5,  6,  i4,^-3.  S.  I3. 5,1'; — avahyS  k<^büjiyakya  bräta  bardiyt^ °m^  ak(^  "illius  Cambysis  firater  Bardiyas nomine  erat"  Bh.7. 10.  ast)  statt  des Appellativs  erscheint  i'*:  7  gaumäti^  'ma' äh<^  hauv  adurujiyj'  Bh.^  a ;  2*.       ß)  das
Appellativ    folgt:    *parg<^    'mii'    kauft^ avadä  , .  Bh,j,  7;  7. 11;  —  tOzäm^  'mii' vardanam  Bh,  7. 19;  2.3,  6,  12,  16,^.1,  5. 6,  8,  2.  7;   —  AaÜa  piravJ'  •««"  rauür D.77. 3".        7)  ohne  Appellativ;  wir  über- setzen dann  'einer  namens  , .'  oder  'ein  ge- wisser"*': kt^baßya*  °»w"  kärausptth^^ .. püruvam  ida  lüäya^iyi^  aAi/'  'Bh.i.io;  — taxmaspad^  'md'  mSd(^  manä  b(^dakt^ Bh.2.i4;io,j.3,6,q,  i4,^i8*,S.7.      Ohne Wert:     darayj'vcTus     vistaspakya     'mi^ /«ä'a*    Ao.  7.  2;   2.        b)    nätm/*;    das Appellativ  folgt:  hauv  udapatalä  habiraav dubali^  -ff/j"  äahyaus  haca  avadasa^  Bh. J-»3;3.  5.  »o.  ^-»S-i-ö,  10, 11, 13;— /«fra* -Ma"  dida  arminiyaiy  avadä  hamaranam akunav<i'  Bb.2,8;  9,   7.13, _j. 9,  11. KompA.  (n^iH'),  E.  —  tä.  tUiman-  n.,  np.  nän. —  P6,i  näm;  s.  nOch  No.  3.  —  >>  Nur  in  nfiu, aber  hier  stets.  —  >)  So  alle  Hds.,  mit  jinei Ausnahme,   J  3,   wonach  NA.  'oif  bietet  — 3)    Fü.:    nndeaüichi    a/ä^i  addpnark  ann (Jamaspji  Gloss.  569  u.)  paakann.  —   1)  S. No.  6.  —  5)  Von  dem  es  n
•  j.  "näyaäta  N.  4(5'',
Pa.i  fehlt  —  0  DsT.  liest  nä  yaHa.
j.  ava  niyn'ifiTm  P,  Jj:  lies  0x10.10/0/1/!!».
•  j.,  p.  nav-  f.  'Schiff"'.
KompA.  (s.  nmäta-);  Ableit  —  ai.  tiav-  f., np.  Mäti,  —  ')  S.  übrigens  näviyä-  No.  1.
•  3.  nävaya-  Adj.  (fem.  °ya-)  'schiffbar',  Be- zeichnung fli essenden  Wassers  von  grösserer Breite  und  Tiefe:  airysJayatam  ..yahmya apö  'y&  p^n%wi/  XiaoiartAa  %waxi?nU Yt  10. 14;  —  . .  'hraotS.siacS  apa  taänä 'yä  Yt/J.  ro;  — pxavS /raoirisyBti  tarasca apB  'ya  (APf.)  V.  14. 16;  7<y.  74;  —  tyaäa *nä  buyat . ,  hupirihwe  a/s*'ya''>  Yt.i6.y,
—  apqm  vä  'yanqm  paiti pfntBsYt.11.^;
—  dasanqm  apqm  'yanqm  aojS  ytÄ24; 74-39;  —  'yayai  .  .  ape  N.  ^7;  67;  — yai  nSit  spa  . ,  mag^e  va  cäiti  va  vaimi va  urüili  va  ape  va  'yä  (GSf.)  pai&yaiie
V.i?-37-
Ableit  ans  *näv:  —  Statt  «äviya-  getchr., S  S6S.  n  b;  vgl.  No.  I.  —  Pü.!  äfi  i  nis ISi'),  eri.  (in  V.  t4):  ktdd»  ;  äfiän  fia dan.    —    ')  So  J 10;    NA.   nach   Fl  nättya.
ob,Google
:o6s
naviya-
$36S.  13  a.—  >)  Statt  dessen  «uch  anap(t)>It. —  3)  S.  zu  parhiya:
•  p.  näviyä-  f.  'Schiffezeug,  Flotte,  Flottille' Uta  abis  'ya  ähJ'  "und  dabei  war  eine Flottille"  Bh.7. 18''.
Ableit,  aus  'näv.  —  ■)  Vgl.  Kbrn  ZDMG. 23.  237.  Anders  jeiit  FoY  ZBMG.  54.  371 (LS.  aus  Häti-\.
•  j.,  g.  näiri-  f.  'Frau',  bes.  die  verheiratete, als  Mitglied  der  Familie, 'Ehefrau',  im  Gegen- satz za^nar-  und/»&ra-:  huxsa%Tas{^A^tü «7  nä  vä  °rf  vü  xsailä  Y.  41.  2;  35. 6;  —  na  va  'ri  va  Yl  ii.  4;  —  narasca *'rlsca''>  (NP.)  Vytjo;  —  3  airySmä (sd.)  .  .  janta  mDhyascä  'ribyasca  zara- %ustrahl  Y.  54.  i;  FrW.  /.  i;  —  vTspa- nam  naram  'rinamca  taoxma  Y .2. 2"];  30, &12,  iz,^-SS.i2,yfä.2;  —  frinyä  'ryi usimtnanhö  "der  Fr.,  der  Frau  des  U'' Yt. /J.  140;  140*;  —  aat  niqm  tarn  fsaona- yeke  (sd.)  'rya  va  pu%Tahe  va  haoya  vä mariiiyi  (sd.)  Y.  //.  i ;  N.  54.  a)  mit asavan-  (Sp.  250  m.):  naram  'rinam  ., a/atmam  asaonitiqm  Y.  26.  7;  8,  10,  Vr. rö'.a,  Yt.y,i43— 145*;  —  asäunqm  fravasls narqmCä  'rinqmiä  '^.g-j.y,  $g.2,  [V. 5.37:  lies  hqm.ttairmqm?\
KompA.,  E.;  Ableit.  —  Ableit.  aus  nur-.  — ai.  närl-  L  —  Pü.:  n5irsf\  —  0  So  K4i Ausg.  'ryaica.  —  »)  S.  lU  näiriia-.
•  j.  nÜrikä-  f.  'Frau',  bes.  die  verheiratete,
'Hausfrau',  uzw.  der  a-4«rischenSchöpfung'': yat  ahtTti  nmane  yat  tnäzäayasnBts  °ka a^ravaiti  .  .  nisAihaj  V,  16.  i;  8;  —  yö 'kayä  ei^ravaihyä  .  .  x^an%>m  frabarät . .  hat  :far>%?m  frabaräli  dva  danar>  . . yesi  nSii  'ka  muruioyat  (sd.)  Y.16.5—7; a'i  13,  14,5.50;  —  yff  'kam  cdravaittm .  .  xhidrä  avi  franhartzaiti  V.  18.  67 ; y  ■  7 ;  —  anySJkaisa  (sd.)  -ka  pairi  xsudrh Jra»^artzaiti  tiik.  2;r;  — yaiAe . .  mazda- yasnanqm  °ka  avaya{%A^  xsudrä  *Aqm.- rai^wayeiti  .  .  ti.li;  —  y3  'kam  yqm apu%rqm  .  ,  xjudrä  avi  fratahrszaiti  V. i^.  8;  —yat  ahmt  nmäne  yal  mäzdayasnöis 'ka  upas.pükirlm  (sd.)  jasat . .  aSdla  alia °ka  la^a  apu%rJm  (sd.)  mjasai  uzuUana V.  5.  45;  59.  7-  70,  7I1  Vd.  igi;  —  yai fiairi.cinaivÄä  jasqn  upa  va  'kam  vä^ayaäa V.  4. 44;  —  'ka  (\AS.)  'kayä  (GD.)  'kanam (GP.)  F.2f.;  —  ratufris  -*'kaya'^  kihrpa N.  sg;  —  a^rS  .  .  av<^a  (sd.)  'kayäi  V. ■'5-4S;  —  naram..  °  rikqm  (GP.?)  Az.i, VytJ;  Vdy;   —   nar^m   va   *'iqm   va
Täx^na.y-  1066
pu%r?m  va  FrB. ;  —  Aai^a  na  paiHirütS haca    'ka  paiti.iriste  Y.  10.  $;  —  yat  ba
\paiti  nars  aSaorUS . .  °kala  apsnnsyäkasca varai^rm  (sd.)  pantqm  atBit  V.J.  11;  3; —  ,.  zaohrata  (sd.)  ratufris  'käscit  (GS.) apgrmäyükahecit  N.  .^0;  —  yS  anyahe'ka (IS.)  ..yS  anyehe  ^apirmSyüka  *anakaxt/T a'haurUTifm  *parar>kacaiti'ü.6i.;  6; — yHi.. 'kqm  vä  *ap}nnäyük>m  (vS)  a/t?m  dasli N.  105; —  'ka  kasujcra%wa  (sd.)  ^.40;  — ava%a  Ag  x"atg  (sd)  pu%rytn  ankat..aat yai  hvqtn  'ka^^  bavaiti(sd.)  ..yai dirftrqm \AfntiYd.2\  —  dahma  •^rf(NS.?)  ap^rma- yüke  kainike  Y.2^.3;  —  katärS  (sd.) '  a%aurumm  *parayat  'ka  va  nmänS.paiti^ va  N.5;5,  *5'>j — yai . .  nmanahe  nmOnB.- paitlm  'kam  .  .  daiöÄSui  daiiikupaitim 'kqm  bisazyätY.j.42;42',  is.$&.  a)mit asavan-  (Sp.  250  m.):  nanm  aiavanjm  . , 'kqm  a^aonlm  V.p.  33,  42,  75.12,  26,  rr.i, 2/7,  10  (statt  Ab!.),  Vr.j.4,  G.4.9;  — tat  asti  yUnO  . .  a^arihim  , .  tat  -kayai  . . ratuxsa^ray'ai  asaonyäi  H.  z.  1 8 ; — 'rikayh aiaonyä  Vd.  4-
Ableit.  aus  näiti-.  —  Pü. :  Ion,  näirU  (Transskr,). —  I)  Im  Gegensatz  za  jahikä-,  s.  H.  2.  18, 36.  Nik.  2  beweist  nichts;  s.  noch  No.  3.  — ^)  So  T,  —  3)  Pü.  erläutert  hier  (Vd.  2)  näirlk mit  pätixiäh  ian;  vgl.  d»iu  West  SBE,  J.  142 ('a  ruling'  or  •privileged  wife')  und  Houruu* Schindler  ZDMG.  36.  86  zu  ZDg.  Säkian.  — O  Ilds.  'käi.
•  j.  näiri'^'Wana-  n.  'Stand  der  (Ehe)&au, Ehestand':  o^anha  v3  duyoa  va  ..mrabyS a/avabys  *'%wanäi''>  upa.valayaaa  (sd.)  V.
14- 15-
Pü.!  »Si,mi.  —  ')  So  Jp  I  usw.;  NA-  •na.
•  j.  näiri.£mah-  Adj.  'eine  Frau,  Frauen
heischend"':  yai  'nankS  jasqn  upa  vä näirikqm  vähayagta  (sd.)  V.  ^44;  44.
Pü.:  tiäitik  iämaiih  rät.  —   •)  Vgl.  lu  laiß.-
Hnah-  No.  1.
•  j.  näiri'vant-  Adj.  'mit  einer  Frau  ver- sehen': nmämm  .  .  "vat  pu'^ravat  "ein mit  Frau  und  Kindeni  versehenes  Haus" V.  j.  2 ;  —  'vaite  .  .  aAmaj  pourum  fra- mraomi  . .  yaha  mayavö  (sd.)  fraväxlSi^ V.4.47-
Pü. :  n&irikSmand.
•  j.  närsnay-  Adj.  —  ?  — ,  bezeichnet  be- stimmte Handlungen:  avaisü  * dim pascalta 'ni  lyadhna  aiwi.daihlta  A.^.  13.
Et.?').  —  Pii.,  Sa.:  transskr.;  Pü.  erL:  kul lanäpuhr  Aaca}  ape  kartend.  —  ')  Greulich  DST. ZA.  2.  735.
dby  Google
io67  näs>m
•  j.  naspm  Inf.  'hinzugelangen  zu  -,  zu erlangen'.
KompE.  ~  Zum  V.  'nas-.  —  Pü.:  ariänik.
•  j-,  g.  näs-  V.  'tragen'.  Praes.  i  nä^-, 30  (Iter.)  näsaya-.  —  Inf.  °näsS.
'(tragen  sva.)  als  Träger,  Stütze  dienen für  — '  (Akk.):  ya^a  lia  väcim  näslma (iPOA.)  ya'ia  vä  saosyantd  dahyunam Y.70.4.
mit  ä:  s.  Inf.,  Sp.  331  u.
mit  fra  'herzutragen,  -bringen  zu  — ' (Akk.):  aesmanqmat  .  .  vasyäi/ (sd.)  .. ratSu^ nmätism /rSnSsayata{'i2.1)  K.3. 5;  5.
mit  tili  'wegbringen,  -schaffen':  ka^a drujtm  ms  ahmal  3  nis''>  naSämä  tsiig  a ava  ydi  . .  "ob  wir  wohl  die  (Anhänger der)  Driig  von  uns  wegschaffen  können hin  zu  denen,  die  .  ."  '^■44- 13;  —  «''■r-- na/ama  saosyantd  *ärußm;  ia%a  (sd.) nTs.naiamat  yaha  Mm  janama  Y.  6'/.  5''.
mit  nis  und  paüi  'wieder  wegbringen, fortschaffen':  *nis*tat  paiti  druxi  naSäite yaaat  (sd.)  aiwicit  jaymat  "die  Dr.  wird wieder  fortgebracht  werden  dahin,  woher.."
Yt.I(?.I2.
^"Eiweitening'  zu  lit.  ahiti,  kil.  nesli  'tragen' ; vgl.  ksl.  n&&,  j-Aor.;  S  338.  a.  —  Pü.  (lu  Y. 44,  61):  ntlaitl),  (lu  70):  nhiiiehilati,  (10  A): iurlan,  Sü,  (lu  A,):  samänetum.  —  •)  Nach dem  Metnim  zu  streichen.  —  ')  In  Anlehnung an  Y.  44.  13.  —  3)  Oder  kaillant  Vgl. West Sg.-Gloss.  353,  2Ö0.
•  j.  "nä^tanam  aajanka  Yt2. 12,  14,
j.  nähmea  Vyt.  25:  lies  tiäämna-,
•  j.  'ni§9nuia-  Ad}.,  Pj-AorM.:  s.  'nas-.
•  j.  'nääamna-  Adj.,  Pj-AorM.:  s.  'nas-.
g,  nä!ü  Y.  JA  5  1  E.  MOS-.
•  j.,  p.  nah-  m.  'Nase',  Sing,  und  Du.: Waäamsaiy  uta  nüham  utä  gausa  fraja- nam  Bh.  2. 14;  13;  —  yim  yava  vatim närahabya  hubaoüitim^m  ßgaurva  H. 2.8;  26;  —  t^m  vahm  ninhaya  (LS.)'> *uzgnmiiiysil.2.8;  a6;  —  «Jw^a  (ND.)'' F.jd; — yaha  *nänhai''  Aaca  *gaoSaäbya ydha  vä  gaosa  Aaca  *^raaAiiya  (sd.)  P.  28.
Vgl.  nSshan:  —  ai.  Has-:nas-  m.j  mp.  näk (?;  aus  *«äAail).  —  Pii.:  vinU.  —  ')  LS.  im Sinn  des  IS.;  oder  ist  die  Form  ein  zum  ND. neugehildeter  IS.?  S  22J.  3.  —  ')  Oder  IS., oder  allenfalls  auch  NS.  zu  niohan-.  —  3)  Hdi. ittha,  aber  Pu. :  vliük.
•  g.  n»  Part,:  s.  unter  ti3.
namaDhan-  i  oäS
j.  n>l}ma  N.  ^\  lies  nititna.
j.  tanf,  Verbalf.:  s.  unter  nam-.
•  j.  n«mata-"  m,  1)  'Reisig':  nasui  tga- 'kaite  .  ,  7flä(i  .  .  'tS  tarS  yan  "die  A''. verschwindet . .  wie  übers  Jahr  das  (dürre) Reisig"  V.p.  46'';  —  avi  Um  spayUt  . . vJspaca  avi  tiyra  *-ia  ".  .  und  auf  lauter spitzes  (dorniges)  Reisig"  V.J.35; — katgAus .  .  äraasca  *'taheca  ayanheca  "die  Nutz- niessung  von  Holz  und  Reisig  und  Eisen- gerät"  V.5.38.  2)  'Geflecht  aus  Reisig, Hürde'  (nur  Komp.),
KompA.,  E.;  vgl.  auch  *»^maÜj.  —  Zum  V. nam-  '(sich)  heraL beugen',  vgl.  nhd.  reit  und ags.  Aiissan  'liltem'.  S.  auch  JOHANSSON  IF. 3.  54.  —  np.  namad  'grober  Teppich;  Filz'  3).
—  Pü.:  namal;  (luV.j):  apdnnatdl,  un- klar. —  1)  NA.  schwankt  iwischen  niot'  und «im\  Vgl.  auch  das  ai.  LW.  namaJa-,  das ein  mp.  nam-  voraussetit.  —  =)  Die  dün  ge- wordenen  Reiser  der  Bäume  werden  von  den Frühjahrsstürraen  abgerissen  und  verwebt  — U  Vgl.  dazu  oben  Bed.  2.
•  j.  *namato.-aiwi.varana-'*  n.  'Unter- schlupf,   Hütte    aus  Reisiggeflecht"*:  yat
däuru.upa.darane  va  'ne  vä  spS  vs  nä  va
irihyat  V.S.i.
Eig.'ReisigCgeflechtjbedeckung',— Pü.:  nama' apar  nihumbih.  ~-  ')  NA.  tum".  —  s)  Im  Folgen- den als  nmäna-  bezeichnet.
•  j.  *nama8kä-"  f.  'Reisig'  als  Feuerungs- material'>:  yat  .,  mafyaAa  daluayasö  avi atnm  abarjnti  .  .  aft>m  alstmm  yS  vaoce 'ka  nqma  Yl/4-55-
Zu  tamaia-  wie  ai.  asialkä-  (BloouPIeld  SBE. 43-  278)  zu  avalä-  m.  —  0  Wegen  M  s.  S  36S. 50.  NA.  hat  lamAia,  was  ich  nicht  für awestisch  ansehen  kann.  Vgl.  Var.  —  >)  Das aber  zu  verwenden  verpönt  war.
■  j.,  g.  namaohan-  Adj.  1)  ehrfurchtig': *asaca  'tshana  (IS.)  ux^ne  (sd.)  xra'^we yaomm  (sd.)    aste  V.^,  45.  2)    'ehr-
furchtsvoll bittend,  betend' :  yi  mq%ra  (sd.) *vaam  .  .  baraitT  urvahu  aia  *nAa  (NS-) Y.50.  6;  —  vastryS  yyaoHanats  fnfys  Aas Auxratus  -»Aä  yS  . .  "der  Bauer,  der  in seinem  Tun  gerecht  ist,  der  einsichtsvolle, wenn  er  (zu  dem)  betet,  der  . ."  Y.  5/. 5  j  —  yH^i  'nAa  (NS.)  vaHm  baraili  yal gaosXsAyit  Yt  10.  85 ''.
Ableit.  aus  ^mmak:  —  ai.  vgl.  namaniB- Adj.
—  Pü.  (zu  Y.):  nySyünSmandlh,  (zu  Y.  57): ke  varzUar  fa  iuniSn  Kul  fa  Aiaaiän  Auxral Aä/  pa  nyäySn,  (zu  Y.  ySy.  aAräiih  nyäyisn giißär'),  erl.:  ö  iär  u  katpai  franämem.  — i>  Anscheinend  nach  Y.  jo.  ö  geformt.  — 3)  So  bei  Mills.
dby  Google
```


## [2026-09-07T18:21:42.011Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT asa Partei\" && grep -n \"'Partei'\" BRT.txt | head -10; echo \"=== BRT 2as- erreichen\" && grep -n \"as-  V\\.\\|\\bas-  V\" BRT.txt | head -10",
 "description": "Grep BRT for asa- Partei and as- verb"
}
```


### [2026-09-07T18:21:42.064Z] TOOL RESULT

```
=== BRT asa Partei
7838:•  g.  asa-  m.  'Partei',  nur  Du.  von  den beiden  Religio  nsparteien,  der  a^uHschen und  der  daiiA^hea'^ :  ai  vä  vTs^Sng  äyöt jiaiä  ratäm  (sd.)  ahurB  valdä  mazda  aya
=== BRT 2as- erreichen
9421:•  j.  kas-  V.,  nur  mit  ä  'gewahr  werden,  Eig.  'der  wenig  Nahrung  hat   (braucht  oder
9453:•  1.  'kas-  V.  lehren.  Praes.  i  oir-.  ^j   jj^„i  „„-irnK   diaytnl,   Jlins
15850:•  j.  pas-  V.  'fesseln'.  j-Aor.  1  pas-.  —  PPfP. *paxita-'^.
17415:ai.  bhyas-  V.  'sich  fürchlen'.  —  Vgl.  bay-.  —
17870:•  j-.  gl  P-  fras-  V.  'fragen'.  Praes.  i p»r3S-'-i,  J3*ß^r7sa»ya-%  1 4 (Inkoh.)/»'«^-, farsa-,  J-Aor.  1  /ras-,  firal-.  —  PPfP. parita-^^;  PFP.  *'ß-asata-;  Inf.  ßars/il^, 'parliöi^^;  AbsoL  'par^m.
18755:•  j.,  g.  'nas-  V.  'verschwinden'.  Praes. 26  nasya-,  Perf.  1  «Äiir-  :  nas-;  PfPr. nrsa-,  j-Aor.  i  nä/-.  —  PFfP.  nasta-, °n3xsta-''>.        Vgl.  noch  II  viyanattty<^,
20608:•  g.  myas-  V.  'mischen'.  Praes.  4  myäsa-,
23099:•  j.,  g.  vas-  V.  'wollen'.  Praes.  i  vas- US:  —  PPfP.  urta-.
26861:•  j.,  g.  'spas-  V.  'spähen'.  Praes.  s hispas-,  10  '^spasu-Q)'^,  11  spaln-,  26 sparya:   —    PPfP.    'spasta-.  [S.   noch
```


## [2026-09-07T18:21:43.426Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 731 (p707)\" && awk 'BEGIN{RS=\"\\f\"} NR==732 || NR==731 {print \"--- leaf \"NR-1; print substr($0,1,2500)}' SYN.txt",
 "description": "Print Buck page 707"
}
```


### [2026-09-07T18:21:44.740Z] TOOL RESULT

```
=== SYN leaf 731 (p707)
--- leaf 730
uti, Pol. (po)déwignaé, cpds. of or = ChSI. dvignati etc. ‘move’ (10.11). Berneker 240.
ChSl. viznesti, Boh. povznésti, Pol. podmiesé, cpds. of ChSl. nesti, etc. ‘carry’ (10.61).
Boh. zvednouti epd. of root ved- in vésit ‘lead, guide’ (10.64).
7. Skt. tul- : Lat. tollere, above, 2.
Skt. wt-thapaya- (mostly ‘raise’ = ‘make stand up’), caus. of ut-thd- ‘rise’ (10.21).
Av. us-grab-, cpd. of us- (cf. us-sta- ‘rise’) and grab- ‘seize’ (11.14). Barth. 527.
on; LOCOMOT
igitized by Arya Samaj Foundation Chennai and eGangotri
JON, TRANSPORTATION, NAVIGATION 671
10.23 FALL (vb.) Goth. driusan
Lith. pultt, kristi
_isT0 ON  falla Lett. Krist ork. ‘igo Dan. falde ChSl. pasti, padali NG caderé Sw. _ falla SCr.  pasti, padati Jat gdere OE __ feallan, dréosan Boh. padnouti Ie jgmber ME _falle, droppe Pol. pas¢é, padaé Fe oger NE fall, drop Russ. past’, padat' a cidea Du. _ vallen Skt.  pad-, pat- i do-tuit OHG  fallan Av. pat- Nir. {uilim thio MHG vallen y. cwympas SU NHG fallen Br koeza rds for ‘fall’ the central notion is | OFr. tumer ‘leap’, loanword fr. the Gme. : Whee rapid, downward motion, as | group seen in OHG éwmon ‘turn around’, Mot ai object falling by its own | NHG taumeln ‘stagger’, OE tumbian an But in many of them the ‘down- ‘tumble, dance’, NE tumble, etc., all yard’ element, though become domi- | prob. of imitative origin. REW 8975.
nant, is of secondary origin, & specializa- tion from some notion of rapid move- ment, This is especially obvious in the case of the root which serves for both fall’ and ‘fly’ in Indo-Iranian and also, though with differentiated forms of it, in Greek (below, 1). Some are probably of imitative origin, based on expressive syllables analogous to NE plump, thud, ete.
1, IE *pet-. Walde-P. 2.19.
Grk. rrr ‘fall’, NG pop. réptw (x7 > or regular; « from aor. éreca, cf. Hat- vidakis, Meo. 2.503), beside éropar fy’; Skt., Av. pat- ‘fall’ and ‘fly’, uenaias ‘made an uprising, re- psn ; Lat. petere ‘go after, seek’, etc.
he sense ‘fly’ is the most widespread notably in the derivs. for ‘wing, feather’, and was probably the prima a f ne noi, Cl.1038, “But the notron of rapid motion unites all e notion of rapid
all the uses.
eee cadere (> It. cadere, Sp. caer,
tal oh ‘ o OFr. cheoir) : Skt: cad- : aa oe casar ‘hail, lightning’,
» Walde-P, 1. ;
17 cos a 339. Ernout-M.
a 128.
18th ee Teplacing cheoi
--- leaf 731
r (above) in Mee sta 1 Lomber, tumber ‘1 Stagger, make tumble’, prob, with
Gamillscheg 847.
3. Ir. do-tuit (8sg.), NIr. tuitim, prob. through ‘hit the ground’ : Lat. tundere ‘beat, pound’, Skt. tud- ‘push, thrust, prick’, Goth. stautan ‘smite’, etc. Walde-P. 2.618. Pedersen 2.656 fi.
W. cwympo, cf. MW cwymp ‘a fall’, of imitative orig.?
W. syrthio, perh. (with reg. s fr. st, as in seren ‘star’, etc.) : OE styrte ‘jump, leap’ (NE start). Loth. RC 43.148 f.
Br. koeza (koueza), W. cwyddo (arch.), Corn. codhe, etym. dub., perh. : ON hitta ‘hit upon, meet’, etc. Walde-P. 1.364. Falk-Torp 407.
4. ON falla, OF feallan, OHG fallan, etc., the main Gmc. group : Lith. pultt, Lett. dial. pult ‘fall’, Arm. p‘lanim ‘fall in’. Walde-P. 2.103. Falk-Torp 202.
Goth. driusan, OE dréosan, ME drese (rare), OS driosan : OHG troren ‘drip, trickle’, Grk. @pabw ‘break up, shatter’, IE *dhreus-. Walde-P. 1.873. Feist 126.
ME droppe, NE drop, orig. like OE dropian ‘fall in drops’ (see 10.24), but extended, so that in its intr. use it is common in the sense of fall, without by any means displacing it, and in its trans. use is generally substituted for the
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
672 SELECTED INDO-EUROPEAN SYNONYMS
phrase let fall, NHG fallen lassen, Fr. laisser tomber, etc., e.g. drop a pencil, a
- handkerchief, etc.
5. Lith. pulti, above, 4.
Lith. kristi, Lett. krist; prob. : Lith. krésti, Lett. krest ‘shake, shake off’. Leskien, Ablaut 333. Mihl.-Endz. 2.281. Otherwise (: Lith. kirstz, Lett. cirst ‘hew, hack’) Walde-P. 2.579.
6. ChSI., SCr. pasti, Padati, ete general Slavic : Skt. pad- ‘fall, go’, hee pad-, paés- ‘move downward, plunge down’, prob. the same root as in Skt, pad-, Grk. wots, etc. ‘foot’. Walde-P, 2,28.
7. Skt. pad-, above, 6. Skt. pat-, Av. pat-, above, 1.
10.24 DROP (sb., of Liquid)
Grk.  craydv Goth.
NG orayéva ON dropi Lat.  guita Dan.  draabe It. goccia, gocciola Sw. droppe Fr. goutte OE dropa Sp. gota ME _— drope Rum. picdlurd, strop (gutd) NE drop Ir. banna, broen Du. drop Nir. braon OHG tropfo W. dafn, diferyn MHG tropfe Br. banne, bannec’h NHG _tropfen
The extension of ‘fall in drops’ to ‘fall’ in general, as seen in NE drop (10.23), leads us to consider here the nouns for a ‘drop’—despite the fact that in these the notion of motion, the ‘dropping’, is subordinate i
```


## [2026-09-07T18:21:58.784Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=765 && NR<=768 {print \"--- leaf \"NR-1; print substr($0,1,1800)}' SYN.txt",
 "description": "Print Buck leaves 764-767"
}
```


## [2026-09-07T18:21:59.437Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=7800 && NR<=7845' BRT.txt | cut -c1-600 | head -60",
 "description": "Context for BRT asa- Partei"
}
```


### [2026-09-07T18:22:00.004Z] TOOL RESULT

```
--- leaf 764
ti ‘arrive’, Lett. staigat ‘walk’ (10.45), Ir. tiagu ‘go’ (10.47), Grk. oveixw ‘stride, advance’, etc., IE *steigh-. Walde-P. 2.615.
Boh. prondsledovati (Pol. przeslado- waé ‘persecute’), Russ. presledovat’, cpds. of words for ‘follow’ (10.52).
7. Skt. anu-dhav-, lit. ‘run after’, cpd. of dhav- ‘run’ (10.46), similarly other epds. of words for ‘run’ or ‘go’.
Av. vayeiti, above, 5.
10.54. OVERTAKE
Grk, Karadop Bava, Pbdvw Goth. Lith. pavytt NG grav, xpodréve ON na Lett. panakt iat ad-, con- sequi Dan. indhente ChSl. postignati “ raggiungere Sw. _ upphinna SCr. (do) stec ? ae rallraper OE offaran Boh.  dohoniti, pristihnoult Tom alcanzar ME __ oftake, overtake Pol.  dogonic, doScignaé in ae , NE _ overtake Russ. dogonjat’ Ni. 5 grennim Du. _—_inhalen Skt.  ap- yo artm (suas) ar OHG  arfolgén(?) Ay. ap- pr, — seddiweddyd MHG erfolgen T — tizout fa ‘i NHG einholen
{ «
any of the words for ‘overtake’ are 1. Grk. caradap Bava ‘seize, lay hold of’ Merely compo 3 “aed an unds of those already con- | and ‘overtake’ (Hdt., ete.), epd. of Aan-
ie er ‘follow’ and ‘pursue’. | Baru ‘take, seize’ (11.18).
‘attive . Words for ‘seize, catch’, or Pounds a which, either in com- Grk. ¢04vw ‘be beforehand, get ahead for Pein. thout change, are also used | of, overtake, arrive’, NG ¢ravw ‘over- with, ©. Cf. NE catch or catch up | take, arrive’, and ‘be enough’, etym.?
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Boisacq 1025. Cpd. Grk. mpopfavw ‘an-
Digitized by Arya Samaj Foundation Chennai and eGangotri
702 SELECTED INDO-EUROPEAN SYNONYMS
ticipate’, NG mpodravw (or -alyw) ‘be in time for, overtake, arrive’.
2. Lat. ad-sequi, con-sequi, cpds. of sequi ‘follow’
--- leaf 765
near’, etc, Falk. Torp 751.
Dan. indhente, cpd. of hente ‘fetch? . ON heimta ‘fetch, demand’, Gme. *haim. aljan ‘bring home’ (deriy, of *haimaz > ON heimr, Dan. hjem, etc.). Falk. Torp 398. In the sense ‘overtake’ prob, modeled on NHG einholen (below),
Sw. upphinna, cpd. of hinna ‘reach’ (10.55).
OE offaran, cpd. of of- and Saran ‘go, journey’ (10.47). Rarely also OF offyl- gan with fylgan ‘follow’ (cf. OHG arfol- gén), below).
ME oftake (with of- as above), later overtake, cpds. of take. NED s.v, over- take.
Du. inhalen, NHG einholen (the for- mer perh. modeled on the latter), epds. of in-, ein-, and holen ‘fetch’; orig. perh. with the application ‘bring in’ the game pursued. Cf. Paul, Deutsches Wtb. s.v.
OHG arfolgén, MHG erfolgen, in OHG also merely ‘pursue’ (10.53), cpds. of
folgén ‘follow’.
5. Lith. pavyti, and Lett. panakt, epds. of vyti ‘pursue’, nakt ‘come’.
6. ChSl. postignqti, SCr. (do)stiti, Boh. pfistihnouti, Pol. doscignaé all epds. of ChSl. stignati, SCr. stiéi ‘ar- rive’, Boh. stthati, Pol. Scigaé ‘pursue’ (10.58).
Boh. dohoniti, Pol. dogonié, Russ. dogonjat’, etc., cpds. of Boh. honiti, etc. ‘pursue’ (10.53).
7. Skt. dp- ‘get, obtain’ (11.16) also ‘attain’ and ‘overtake’. So Av. ap-, esp. with avi- or a- (Barth. 71).
tArrive’ is most widely expressed by rhs for ‘come’ OF compounds of these. it several new terms have arisen, of diverse SOUrCES. , ans 1, Grk, agexvéopa (or simple tKVEO- jai), mostly ‘arrive at, reach at acc., but also intr. ‘arrive’ : ixw ‘come’ also ‘reach’, prob. : Lith. siekli ‘reach out with the hand, take oath’. Walde-P. 2465, Boisacq 372. Grk. ¢84yw in part ‘arrive’, NG ¢ravw usual for ‘arrive’ (cf. waiter’s érac
--- leaf 766
er po ryenire Dan. ankomme, naa ChSl. priti, prispéti qdvenite, Pe wal Sw.  framkoma, anlénda, SCr.  (na)do¢i, prispjelt grrivare, hinna, nd Boh.  prijitt, pristali arriver OE ancuman Pol. przybyé Ilegar ME aryve, reche Russ. pridti, pribyl’
_ ajunge 8 peapin NE arrive, reach Skt.  gam-, d-gam-, G-sad- roiccil 7 Du.  aankomen Av. jam-, aibi-Jam-, hant- sroichtm a OHG anaqueman, gilangon dyfod, eyrr@ MHG anekomen, gelangen don(e)t NHG ankommen, gelangen
Rum. sost, fr. Grk. ctw, aor. éowoa ‘save’, also ‘bring safe to’, Byz. and NG (new pres. omvw) also simply ‘arrive’. Cf., fr. same source, Alb. sos ‘finish, ar- rive’ and Bulg. sosaja ‘come’. Densusi- anu 358.
3. Ir. rotccim, riccim (‘reach’, trans.; cf. Laws, Gloss. 614f.), NIr. roichim, sroichim, fr. same root as do-iccim ‘come’ (10.48).
Ir. rosaigim, dorochim, epds. of saigim ‘seek’ (11.31). Pedersen 2.609 ff. From the same root also W. cyrraed, cyr- haed (cy-r-haed) ‘attain, reach, arrive at’, Br. direza ‘attain’. Pedersen 2.28. Loth, RC 30.260.
W. dyfod ‘come’ (10.48), also ‘arrive’.
Br. don(e)t ‘come’ (10.48), also ‘ar- rive’.
4, Goth. anagiman (but quotable only as ‘come upon, appear’, Lk. 2.9), ON koma at, Dan. ankomme (fr. LG or HG), Sw. framkoma, OE ancuman, Du. aankomen, OHG anaqueman, MHG anekomen, NHG ankommen, all epds. or phrases with words for ‘come’.
ON 7a, Dan. naa, Sw. nd: Goth. néhwjan ‘draw near’, advs. Goth. néhw, OE néah, etc., ‘near’ (12.43).
Sw. anlanda, orig. ‘come to land’, now in extended sense like Fr. arriver. Hell- quist 607.
Sw. hinna: Goth. fra-hinban ‘cap- ture’, OE hentan ‘pursue, follow’, hun-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
i 5 . . | Digitized by Arya Samaj Foundati
--- leaf 767
tati ‘stand’,
Pol. przybyé, Russ. pribyt’, epds. of verb for ‘be’.
7. Skt. gam-, Av. jam-, ‘£0, come’ (10.47), also used for ‘arrive’, or epds, with Skt. a-, abhi-, Ay. aibi-, OPers, abiy-d- (Barth. 496). OPers. also abiy upa-i- (abiy babirum yabé naiy wpdyam ‘when I had not yet reached Babylon’). Barth. 150.
Skt. d-sad- ‘arrive at, reach, approach, meet’, cpd. of sad- ‘sit’, with notion of motion developed in cpds. Cf. Grk. 656s ‘road’, ChSl. choditi ‘go’ (10.47). Walde-P. 2.486.
Av. hant- : OHG sinnan ‘travel’, sint ‘course, way’, etc. Walde-P. 2.496f. Barth. 1771.
10.56 APPROACH (vb.)
Grk. _ wAnotdtw, rASLW, Goth. néthwa wisan, néhwa Lith. artintis tyylitw qiman Lett. tuvoties b NG ss wAnordto, tvydvw, ON ganga ner, nakvema ChSl. pribliziti se : oho Dan. nerme sig SCr. _ priblizili se Lat. adpropinguare, ac- Sw. _ndrma sig Boh. pFiblizili se f cédere OE néahl@can Pol. zblizyé si¢ It. avvicinarsi ME aproche Russ. priblizat’sja Fr. approcher, s'approcher NE approach Skt. abhi-gam-, upa-stha- . Sp. acercar(se), allegar- Du. naderen Av. Pieieke
(se), aprozimar (se) OHG nahan, nahlihhon Rum. apropia MHG nahen Ir. ascnaim, tascnaim NHG  nahen, sich néhern
Nir. druidim, tarraingim W. dynesu Br. tostaat, (di)nesaat
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
orion:
‘ority the verbs for ap- qhe 14) pased 08 adverbs for “near ew are compounds of yes (2s or ‘go’, oF from various other
st Berice reratw fr. wrnatov,
j, Gil
ae og fr. eyyos ‘near’. But t
yG avy ‘ class. Grik. fuyéw ‘join’. join’, late refl. ‘ap- re ‘arrive’ (10.55). fr. oysd ‘near’.
(fr. xovrd ‘near’) is rarely ysed for ‘gpproach’ in the literal pense, but reg. i phrases like xovreber va. weBavn ‘comes
```


### [2026-09-07T18:22:01.218Z] TOOL RESULT

```
Zum   tti.   V.  antali;   s.  aiiku'.    —    Das   7   in
'afiia-  stellt  den  gulL  Nasal  dar,   vgl.  m^ri-
■!>'•"%  347  No.;  at.  *a»*ma-  (%  24)  wird  urir.
*aifma-  (%  24\  Aw,  "i^ama-  (S  296.  l).
dby  Google
359
f^xnanha-
sjs-  ra\l/r3
360
•  j.  f^naoha-  m.  EN.  eines  Gläubigen: vokustrahe  'nauhahe  aiaonö  "des  F.,  Sohns des  4 .."  Yl;j.i23.
AbleiL  aus  nxiiah-  oder  Kurtname  damit; etwa  'Zugclhaltei'.
•  j.  axna.h-  n, 'Zügel':  'nä  dralaite  välahe ".  .  hält  die  Züge!  des  Wagens"  Vt.  5. 1 1 .
Ableit.  —  Vgl.  anku'  und  Bthl.  Stud.  2.  101 ; S  24  aE. —  gr.  vel.äyii?.)! 'Schlinge,  Riemen'. Mit  PDw.  yixän  'Zügel',  das  Tomaschek SWienAW.jjö.  805  vergleicht,  weiss  ich  nichts anzufangen.
•  j.  ^mö.fränö.-masah-  Adj.  'des  Grösse den  gebogenen  Arm  fUlU',  d.  i,  'so  gross wie  man  es  unterm  Arm  trägt':  alsmanqm- ät  . .  °s}6t^  (näml.  stäir^  A.j.5.
'qxiiia-  m.  'Biegung  des  Arms';  vgl.  gr.  äiKÖ»; Bthl.  Stud.  2.  lo*.  —  I'ü.;  V  n  d /ranämihi maiäi,  Npa. :  /ri  iai  6älä,
•  }.  a^iSyä-  f.  'Pfosten':  mi^nm  .  .  yj .  . stawra  yä  kirtnaotti  Yt. /O.  a8.
ai.  vgl.  älä-  f. 'TüTumfassung' 1  s.  Zimmer  AiL. 154;  KZ.  32.  71,  IF.  5.  j68.  —  Falsch  Sp. VglGr.  209;  s.  Hbm.  AGr.  /.  141.
•  g.  a^nman-  n.  'Stetigkeit;  Unaufhörlich- keit': al  kahrplm  utayäitJs  äadät  armaiti^ 'mä  (AP.)'*  "und  Arm.  verlieh  den  Leibern Dauer  und  Stetigkeit"  Y.jo.;.  a)  LS. °m7nT  als  Adv.  'stets,  ewiglich;  unaufhör- lich"'; yi  'mSnl  mazdn  srävi  ahurd  "der ewiglich  MAk.  heisst"  Y.  45. 10;  —  yaii' gqm  karaps  usixscä  (sd.)  alhmUi  däii yücä    kavä   *'mJnI^^    urüdSyatä  (sd.)    Y.
El.?  Ir.  *aiiman-  (S  29J.  \i),  dessen  an  auf ar.  an  oder  an  mit  reduzirtem  denl.  Verschluss- taul  gehen  kann  (S  24.  S.  noch  No.  4-  — Pa,  (lu  Y.  30):  vai  elön  karp  luxsiin  dahel tpandaramat  /ü  astavih,  erl.  i  vi!  iavfl  slav  tie »avfUi;  (tnY-V^):  ifta  tayat  aiLrv  ii  ränoiik dälär,  erLi  Aac  rtr  i  apärön  slav  ne  taz'eH); (ittV.  45)-  kr  fa  an  i  nSmik  srül  estil  a^alä'i i  dättäk,  Sü.!  anyanämalayä.  —  ')  In  Ober- einstimmung  mit  dem  asynd.  danebenstehen- den  uiayiiitis.  —  a)  s.  dazu  Bgm.  Totaüiäl  
•  g.  anmäni  Adv.:  s.  unter  qnman-.
•  i-i  g.  a,8-  V.  'hingelangen  zu  — ',  Praes. I  as;  7{?)  ^qsa/u-'\  8  qs-,  10  asnav. asnv-;  j-Aor.  i  as-.  Inf.  astd,  iiSdyät (mit  a),  avasyiV^,  mit  ava).
i)    'hingelangen   zu    -'   (Akk.):   vuj>a
hmnaia  .  .  vahist^m  *anhüm  *asaiti^ (Konj.)  vTspa  dusmata  . .  aashm  *anhüm "'ahiti''!  FrW.j.a.  2)  'etwas  als  seinen Anteil  erlangen':  Ayat  ^qiaSufä  (3SPrM.)" ya  daibitänä  (sÄ)  fraoxla  am>r3täitl daeväilcä  masyäilca  "so  dass,  was , .,  den Dagva  und  Menschen  in  Ewigkeit  zugeteilt wird"  Y.4ÄiJ>.  3)   'wo  (Lok.)    an-,
unterkommen':  s.  asts  Inf.
mit  ava  'erreichen,  treffen':  ««V  dim arstöiS'  .  .  nSii  isaos  .  ,  ava.asnaeiii  san- mairyB  (sd.)  Yt  10.24;  —  nSiJ  dim  ..  ava- syät*^  nsit  akavö  nsit  .  .  Yt.  i.  18";  ij. 72.        S.  noch  Inf,  (Sp.  177).
mit  dtfi  und  ava  'treffen':  yezi  ma  hau n3  ava   ^snai^isa  (sd.)   aoi  ava  asnai-ät
P.  2!.
mit  ä:  s.  äzdyli  Inf. mit    US   'hinaufdringen   zu   — '   (Akk.): yniAe  vaxs  . .  us  ava  raocA  (sd.)  asnaaiti Vl  10.85;  ~  ■  ■  US  ava  raocä  asnaot  Yt /O.89.
m\i paiti  '(mit  einer  Waffe)  treffen':  yat dim  aZnö.manatiha  paiti.asnaoiti  aetat  lis andus  (sd.)  V.  4. 1 7.
mit  /r>l,  frB  i)  'erreichen,  treffen':  nsit gdüahe  .  .  tbalxB  frqstißna  (sd.)  fräsnu- y,lt  Yti/.  s;  —  cvat  antar?  *rurSus  aisa druxs  yä  nasu/  ax/i^a  .  .  fräsnaotti  V. J.27;  28;  —  ye%i  nsii  Aarv^rvm  baraiti aztaöa  hi  vfspä  hSirÜTl  fräsnaotti  ".  .  so trifft  er  damit  alle  Weiber"  (?)  V. />  19; —  nSit  ahyä  mä  ahris  (sd.)  syad^anäis frösyaii*    Y.46.8.  2)    'herzu-,    hinzu-
kommen zu  — '  (Akk.):  vlspü  anhus  ..  air- yatum  vaijS{sA^fräsnvät^.t.\.  a)  'in Berührung  kommen  mit  — ':  yezi  apin- I  näyüks  fräshaväi  "wenn  ein  (saugendes) Kind  (mit  der  menstniirenden  Frau)  in Berührung  kommt"  V. /6'.7*>.  3)  'teil- haftig werden,  sich  teilhaftig  machen',  mit |Gen.;  nSit  dva  nSit  irayS  .  ,  asake  ndil asaya  früsinti  (Konj.)  yß  rßit  .  .  "nicht '  werden  sich  zwei  .  .  des  Asa  noch  der 'Belohnung  teilhaftig  machen  .  ."  P. '  44''^.  4)  'zu  teil  werden':  hyat  nä  fryäi I . .  isvS  (sd.)  daidii  m
I  ai.  aiyal,  aHoiStnahai'il,  ainiti,  alial.  —  VgL '  »flflj-.  —  Fa.;  rasitOH,  hilan,  matan,  (zu  Yt. I  .  11,  P.):  pursUan;  s.  noch  No.  4-8.  —  ')  Die I  Fonn  i^aintä  ist  verderbt  Man  erwarttte *iisa!/ä  —  s.  aber  sfiahAä  —  oder  *qsiiimifä
ob,Google
36 I  ^sa-
(Praei.  7  +  10).     Unrichtig   KZ,   S3-    4^5- '}  Ausg.  aiaiia,  s.  Var.  —    3}  iSL  Gi>n.  KZ. JO.  514.  —  *)  Aus  ava  +  'ojyii/,  %  s6S.  3.  Pü, : nt . .  api  HosfmtSr,  erL :  aiär  tarlan  iie  titvän.
—  S)  Aus /w+*afcä/;  vgl.  Sjo^  II.  a8.  Pü. : ne  . .  /räi  rdntmlär,  eil. :  pälifris  bavttudak ape  iattan  ne  taväti.  —  *)  Pü.i  ka  afurriäyai fräc  raset,  erl.;  hac  kaitän  ajil  Sylt,  —  7)  zSL
Bthl.  IT-  7.  as8.  —  B)  Falsch  KZ.  jj.  465 ;
s.  noch  No.  g.  IMi.:  ie  S  15  iahrvtr  hac ahräilh  apiklk  framüt.  —  9)  Nicht  sicher; Bthl.  Stud.  i.  96.  frqitä  könnte  statt  Praes.  S auch  /-Aor.  sein.
•  g.  asa-  m.  'Partei',  nur  Du.  von  den beiden  Religio  nsparteien,  der  a^uHschen und  der  daiiA^hea'^ :  ai  vä  vTs^Sng  äyöt jiaiä  ratäm  (sd.)  ahurB  valdä  mazda  aya
°sayä  "so  wende  ich  mich  an  euch  alle als  der  Ratav  der  beiden  Parteien  hier, als  den  (mich)  ÄhM.  kennt"  Y.jJ.a.
>i.  ämia-  m.  —  Pü. :  hac  ö/än  an  raiiin.  — .)  VgL  'rJm...
•  j.  i^sav-  m.  'Schoss,  Zweig*  der  Haoma- pfianze:  ^ävaiitJ  alte  'sai'S  arihin  "wie gross  sollen  die  Zweige  sein?"  N.  to8;  — havamm  (sd.)  . .  yd  'sus  (AP.)  hangmr- vayäti  Y.jo.i.
KompE.  —  ai.  amiäv-  m.;  ■>.  dazu  Roth ZDMG.  jj.  684.  —  l'a-:  l^t.
ß,  '"ifsahitä  Y,  4S.  l:  s.  HS-  mit  No.  i.
•  ]-•  S-  S[sta-  m.  'Hass,  Feindschaft; Feindseligkeit':  %wahya  mazda  °tä  (IS.) urvataAyäisd.)  Y.34.&; — yü  gä^ä  asrü- vayd  *'ta  (IS.)"'  vH  tarff.waiti  v3  tanUm *piryetti  "wer  die  G.  nicht  aufsagt  aus Hass  oder  Trotz,  verwirkt  den  Leib"  N. 41;  —  kS  *tff'^  **J  *iarS.»iaitis' (sd.)  N. 41;  —  cim  aosaaAi  aoSaaukaiti  'Um Uaiti  tanva  Aog.  4S(?);  —  a  f/  dvafsSng (sd)  ..  anale  -tqsca  Y.  44-i4)  —  y^ maiiyä  yaoi  akmsi  .  .  vaAista  . .  SStiim  . . 'tftig  ahtnai  y7  nä  astät  (als  Inf)  daidüä ".  .  Feindschaft  (
Ans  ar.  *a«j-lha- ;  ygl,  (Et.  unter  aora- ').  — Pü.;  aiuufih,  (EU  N,  41)  erl,!  ka  gäwit  ku  den ntsi;  [iD  V.  44):  anasi  iat;  Sü.:  nSsäiatvam, anäitiiatvam  'Ungläubigkeit'.  —  >>  Hds.  ifslä.
```


## [2026-09-07T18:22:15.701Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=768 && NR<=772 {print \"=== leaf \"NR-1; print substr($0,1,2000)}' SYN.txt",
 "description": "Print Buck leaves 767-771"
}
```


### [2026-09-07T18:22:16.997Z] TOOL RESULT

```
=== leaf 767
tati ‘stand’,
Pol. przybyé, Russ. pribyt’, epds. of verb for ‘be’.
7. Skt. gam-, Av. jam-, ‘£0, come’ (10.47), also used for ‘arrive’, or epds, with Skt. a-, abhi-, Ay. aibi-, OPers, abiy-d- (Barth. 496). OPers. also abiy upa-i- (abiy babirum yabé naiy wpdyam ‘when I had not yet reached Babylon’). Barth. 150.
Skt. d-sad- ‘arrive at, reach, approach, meet’, cpd. of sad- ‘sit’, with notion of motion developed in cpds. Cf. Grk. 656s ‘road’, ChSl. choditi ‘go’ (10.47). Walde-P. 2.486.
Av. hant- : OHG sinnan ‘travel’, sint ‘course, way’, etc. Walde-P. 2.496f. Barth. 1771.
10.56 APPROACH (vb.)
Grk. _ wAnotdtw, rASLW, Goth. néthwa wisan, néhwa Lith. artintis tyylitw qiman Lett. tuvoties b NG ss wAnordto, tvydvw, ON ganga ner, nakvema ChSl. pribliziti se : oho Dan. nerme sig SCr. _ priblizili se Lat. adpropinguare, ac- Sw. _ndrma sig Boh. pFiblizili se f cédere OE néahl@can Pol. zblizyé si¢ It. avvicinarsi ME aproche Russ. priblizat’sja Fr. approcher, s'approcher NE approach Skt. abhi-gam-, upa-stha- . Sp. acercar(se), allegar- Du. naderen Av. Pieieke
(se), aprozimar (se) OHG nahan, nahlihhon Rum. apropia MHG nahen Ir. ascnaim, tascnaim NHG  nahen, sich néhern
Nir. druidim, tarraingim W. dynesu Br. tostaat, (di)nesaat
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
orion:
‘ority the verbs for ap- qhe 14) pased 08 adverbs for “near ew are compounds of yes (2s or ‘go’, oF from various other
st Berice reratw fr. wrnatov,
j, Gil
ae og fr. eyyos ‘near’. But t
yG avy ‘ class. Grik. fuyéw ‘join’. join’, late refl. ‘ap- re ‘arrive’ (10.55). fr. oysd ‘near’.
(fr. xovrd ‘near’) is rarely ysed for ‘gpproach’ in the literal pense, but reg. i phrases like xovreber va. weBavn ‘comes near dying’. :
9, Lat. adpropinquare, fr. adj. pro- pinguuus ‘near’, deriv. of adv. prope near’. Similarly, late adproximare (> Sp. aproximar), through proximus; late adpropiare (> OF r. apro
=== leaf 768
th. néhwa wisan (néhwa was = nrvyecev Lk. 19.41), néhva qiman (= mpoo- eyyicat Mk. 2.4), ON ganga ner, na- kvema, Dan. nerme sig, Sw. ndrma sig, OE néaahlé@can (léccan ‘seize’, 11.14), Du. naderen, OHG nahan (also nahlth- hon frequent in Tat., fr. adv. in -lih), MHG nahen, NHG nahen and sich nihern (ndhern ‘bring near’), all derivs., epds., or phrases with the Gme. words for ‘near’.
ME aproche, NE approach, fr. OFr. aprochier (above, 2).
5. Lith. artintis, refl. of artinti “bring near’, fr. arti ‘near’. Lett. twvoties, fr. tuvu ‘near’.
6. ChSl. pribliziti se, etc., general Slavic, fr. ChSI. blizt, etc. ‘near’.
7. Skt. abhi-gam- and other epds. of gam- ‘go’ or ‘come’.
Skt. upa-stha ‘stand by’ and ‘ap- proach’, epd. of stha- ‘stand’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
706 SELECTED INDO-EUROPEAN SYNONYMS
10.57 ENTER
Grk. — eloépxopar Goth. galeiban, inn-(at-) Lith.  jeiti NG ss uralvw gaggan Lett. zeiet, temit Lat. —_inirdre, introire, ON gagga inn ChSl.  viinit; ingredé Dan. inirade SCr.  udi, ulaziti, stupity It. entrare Sw. —inirdda Boh. — vstoupiti, vejiti u I. entrer OE ingan, infaran Pol. —- wejgé Sp. entrar ME entre Russ. voit, vstupit! Rum. inira NE enter Skt. vig- Ir. tnodliagu Du. binnen gaan (-komen, Ay. re NIr. —téighim isteach -treden) W. myned (or dyfod) 7 OHG ingangan mewn MHG ingan Br. mont ebarz NHG_hineingehen, eintreten
‘Enter’ is simply to ‘go or come in’ and is most commonly so expressed, but also in part by compounds of verbs for ‘tread, step’ or the like, or by a direct derivative of a word for ‘within’.
1, Cpds. or phrases with verbs for ‘go’ or ‘come’.
Grk. elcépxouat, Lat. introtre, Ir. in- od-tiagu (Pedersen 2.645), NIv. léighim isteach (isteach ‘into’, orig. ‘into the house’ : tech ‘house’; Pedersen 1.264), W. myned (or dyfod) i mewn (mewn ‘within’ : 
=== leaf 769
lésti in words for ‘ascend, descend’, Berneker 697, 715.
5. Skt. vig-, the usual word for ‘en- ter’, but this sense perh. extension fr. ‘enter the house or home’ (cf. Nir. tsteach ‘into’, above) in view of the wide- spread cognate nouns, like Skt. vi¢- ‘settlement, dwelling place, house’, Grk. ofxos ‘house’, Goth. weths ‘village’, etc. Walde-P. 1.231.
I. majority % : com eae to an inherited group
‘ting to an LE root of this meaning. Bert this group, like NE bear, have ceased to be the common generic words for ‘carry’ and are used only in more specialized applications. In certain other inherited groups the generic carry’ is much less widespread and ap- parently secondary to other notions, such as ‘reach’, ‘support, lift’, ‘carry by avehicle’. For the group in which this last is the dominant sense, though some- times extended to generic ‘carry’, name- ly Lat. vehere, OK wegan, Skt. vah-, etc., see under ‘ride’ (10.66). In the his- torical period there is development of ‘carry’ from ‘lift’, ‘carry in a vehicle’, ‘ead’, and ‘put, place’.
1. TE *bher-. Walde-P. 2.153 ff. Er- nout-M, 348 ff. Walde-H. 1.483 ff.
Grk, PEpw, NG also épvw; Lat ferre; I. iru, berim, NOx beirim; CG th. bai OE beran, ete, Bice : eee ‘carry’, now in. ae Bee Gme. for rn, NHG gebdren then Baten (Duvas bear in this sense alspice a an oe inmany phrases, as bear in mind, by and Onger paisiah’ te ee mind, but no Speech); Sict, igs ei in common Arm. berem; Alb bie oe OPers. bar-; : ring’; Toch. pdr-
448); but ChSl. bera,
brag ets (SSS ming together, collect? (12.21).
Digitized by Arya Samaj Foundation Chennai and eGangotri
LOCOMOTION, TRANSPORTATION, NAVIGATION 707
10.61 CARRY (BEAR) Agee Goth. batran Lith. negli i (tow averse): ON _bera Lett. nest Gtk gas es poor Dan. bere, Spre ChSIl. nest, nositi f in lps EP! Talus)» POT Sw. bara, fora SCr. nositi (nijeli, nestt) NG ferre (uli, d OE beran, fertan Boh. _ nésti, nos
=== leaf 770
ach’ hence ‘bring’.
3. Grk. fvexa or qika = fveyKa in most dialects except Attic, fr. a- and the root of tkw, ixvéouar ‘come, reach, arrive at’ (10.55). Walde-P. 2.465.
Grk. fut. otcw, also aor. in infin. dv- otca. etc., etym.? Walde-P. 1.103. Boisacq 694. Possibly : fue ‘go’, oluos ‘way’, through a caus. notion. Cf. Cret. tq-edevoe? ‘will bring’, aor. ér-jhevoar ‘brought’ : edeboopat ‘will come’.
Grk. éyw ‘lead’, orig. ‘drive’ (10.65), also used for ‘carry, bring’, but mostly of living creatures.
Grk. Baorétw ‘lift, raise’, also ‘carry’ (Aesch.+, freq. in NT), NG Baorafw pop. Baor ‘support, carry,’ and ‘bear’ = ‘endure’, etym.? Boisacq 116.
4. Lat. perf. tult, old tetult, pple. latus
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
. . . : ie Digitized by Arya Samaj Foundation Chennai and eGangotri
Sete peewee — LT
708 SELECTED INDO-EUROPEAN SYNONYMS
(*ildtos) : Lat. tollere ‘raise, lift’, etc. (10.22); the primary sense of the root *tel- being prob. ‘support’. Ernout-M. 1044,
Lat. portare (> It. portare, Fr. porter, Rum. purta) : Skt. pr- ‘lead across, rescue’, para- ‘beyond, far’, Grk. zelpw ‘pierce’, repdw ‘pass across’, Goth., OHG, OE faran ‘go, travel’ (10.47), OE ferian ‘carry’ (Dan. fre, Sw. fora ‘carry’ and ‘lead’, 10.64), IE *per-. Walde-P. 2.39. Ernout-M. 793 f.
Lat. vehere, sometimes generic ‘carry’ but mostly ‘carry’ on a horse, vehicle, ship, cf. pass. vehi ‘be carried, ride’ and cognates (10.66).
Lat. gerere, sometimes ‘carry’, but mostly ‘carry on one’s person, wear, conduct oneself, act’, etc., root *ges- (cf. gesst, gestus) but etym. dub., perh. as *9-es- : *ag-in agere ‘drive’, etc. Walde- P. 1.37. Ernout-M. 420f. Walde-H. 1.595 f.
Sp. Uevar = It. levare, Fr. lever ‘lift’, fr. late Lat. levdre ‘lift, lighten, alleviate’ (10.22).
Rum. duce, fr. Lat. dicere ‘lead? (10.64).
5. Ir. biru, NIz. beirim
=== leaf 771
g’), W. dwyn ‘bring’ (1sg. dygaf), Br. dougen ‘carry’, etym dub. Walde-P. 1.111. Pedersen 2.474, 475.
6. Goth. bairan, ON bera, ete., above, 1.
OE ferian, Dan. fore, Sw. fora, see under Lat. portdre (above, 4).
ME carie, NE carry, orig. ‘carry’ by a vehicle, fr. ONorthFr. carier (Fr. charrier ‘cart, haul’), fr. late Lat. carri- care derived fr. carrus ‘cart’ (Gallic ; ef. currere ‘run’, 10.46). NED s.y.
OHG tragan, MHG, NHG tragen, Du. dragen (Goth. dragan for ga-dragan ‘heap up’), prob. (but disputed) : ON draga, OF dragan ‘draw, drag’ (9.33). Walde-P. 1.862. Franck-v. W. 130. Feist 91. Falk-Torp 150 f. (separating OHG tragen, from ON draga, etc.).
7. Lith. nesti, Lett. nest, ChSl. nesti, nositt, above, 2.
8. Skt. bhr-, Av. bar-, above, 1. Ay. nai-, above, 2.
orton: a of ‘pring’ to ‘carry is at of ‘geome’ to ‘gO (cf. sa pile ‘carly ’ denotes the aetion iy -d to direction, ‘bring’ in-
s of a definite goal,
re :
‘ plication ae of the speaker, but Ey so, Generally this notion
‘-raeuished from ‘carry’, DE at ferre, etc., which 1 ond ‘bring’, or is ex- : ounds of the verbs for py relies meaning ‘to’ or the For these, as already discussed in 104", or obvious compounds of ee game, no further comment 1s needed.
It is only in Germanic that there is a distinctive independent group for tring’. But some other words of vari- ous primary meanings are also used for ‘bring’, and the most important of these are listed.
1. Sp. traer, fr. Lat. trahere ‘pull, draw’ (9.88).
2. Ir, to-wcc- (perfect. to do-biur), W. dwyn, Br. dizougen (= di + dou- gen), see under Ir. ro-ucc-, Br. dougen ‘carry’, 10.61.
W. cyrchu ‘approach’, but also (prob. through ‘go for, go get’) ‘bring’, fr. Lat. circdre ‘go around’ and ‘seek’, the latter meaning attested by It. cercare, Fr.
chercher ‘seek’, ete. (11 lat. 157 pe ere
pot ne?
Br, digas, epd ey) i , epd. of di- ‘t send, lead? (10.63). 2- ‘to’
```


## [2026-09-07T18:22:28.343Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"IE \\*nek\\|nek-. Walde\\|Av. nas-\\|Av. naš\" SYN.txt | head -20; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==770 {print}' SYN.txt | grep -n -i \"nek\\|nesti\\|reach\" | head",
 "description": "Find Buck group 2 IE *nek-"
}
```


### [2026-09-07T18:22:29.695Z] TOOL RESULT

```
7372:3, Lat. nex ‘violent death’ (vs. mors, above, 1), late sometimes also for natural ‘death’: Grk. vexpos, vexus Av. nasu- ‘corpse’ (4.77), Skt. nag-, Av. nas- ‘van- ish, perish’, Ir. éc, etc. (below, 4) ‘death’. Walde-P, 2.326. Ernout-M. 669 f.
7460:1. Grk. vexpés, véxus, Av. nasu- : Skt. nag-, Av. nas- ‘perish, vanish’, Lat. nex ‘violent death’, etc. Walde-P. 2.326.
17559:3. Ir. do-iccim, ticim, NIv. tigim, epd. of icc- (fr. *nk-?) : Skt. ag-, nag-, Av. nas- ‘attain’, Lat. nancirz, nancisci ‘at- tain, obtain’, Grk. jveyxa, Lith. negii, ChSl. nesti ‘carry, bring’. Walde-P. 1.128f. Ernout-M. 652. Pedersen 2.557 f. Thurneysen, Gram. 126, 130.
17819:Grk. aor. #v-eyxa (cf. Skt. perf. an- anca); Lith. ne&ti, Lett. nest, ChSl. nest, nositi, etc., general Slavic for ‘carry’; Skt. ac-, nag- ‘reach, attain’ (cf. Grk. mod-nvexns ‘reaching to the feet’), Av. nas- ‘reach, attain’, nd§- ‘carry’ (s-ex- tension, Barth. 1067); Lat. nancisct ‘ob- tain, receive’; Goth. ga-nohs ‘enough’, etc.; Ir. do-iccim ‘come’ (10.48). The meaning ‘reach, attain’ appears to be the primary one and ‘carry’ a secondary, in part already IB, prob. through ‘cause to reach’ hence ‘bring’.
18951:2. Lat. nancisci, inchoative of an obs. nancire, nanct (Gramm.) : Skt. nag¢-, Av. nas- ‘reach’, Grk. aor. jveyxa ‘carry’, etc. Walde-P. 1.128f. Ernout-M. 652.
19285:7. Skt. nagaya-, caus. of nag ‘be lost, perish’ : Av. nas- ‘disappear’, Lat. ne- care ‘kill’, etc., IE *nek-. Walde-P. 2.326. So also Toch. A ndks-, caus. of ndk- ‘disappear, perish’ (SSS 445).
---
1:lésti in words for ‘ascend, descend’, Berneker 697, 715.
4:‘ting to an LE root of this meaning. Bert this group, like NE bear, have ceased to be the common generic words for ‘carry’ and are used only in more specialized applications. In certain other inherited groups the generic carry’ is much less widespread and ap- parently secondary to other notions, such as ‘reach’, ‘support, lift’, ‘carry by avehicle’. For the group in which this last is the dominant sense, though some- times extended to generic ‘carry’, name- ly Lat. vehere, OK wegan, Skt. vah-, etc., see under ‘ride’ (10.66). In the his- torical period there is development of ‘carry’ from ‘lift’, ‘carry in a vehicle’, ‘ead’, and ‘put, place’.
11:10.61 CARRY (BEAR) Agee Goth. batran Lith. negli i (tow averse): ON _bera Lett. nest Gtk gas es poor Dan. bere, Spre ChSIl. nest, nositi f in lps EP! Talus)» POT Sw. bara, fora SCr. nositi (nijeli, nestt) NG ferre (uli, d OE beran, fertan Boh. _ nésti, nositi [st "are ME __sibere, carte Pol. __nie&é, nosié 7 porar® NE el (bear) sae nesti, nosit! * —— porler Du. ragen kt. bhr- Hs ane Bis OHG beran, tragan Ay. bar-, nas- aes a, a HG tragen jum. Pur. amchuirim M i es jomcharaim NHG tragen ue dudo, cario Br. dougen of the old words for 2. IE *enk-, *nek-, *nf-. Walde-P.
13:Grk. aor. #v-eyxa (cf. Skt. perf. an- anca); Lith. ne&ti, Lett. nest, ChSl. nest, nositi, etc., general Slavic for ‘carry’; Skt. ac-, nag- ‘reach, attain’ (cf. Grk. mod-nvexns ‘reaching to the feet’), Av. nas- ‘reach, attain’, nd§- ‘carry’ (s-ex- tension, Barth. 1067); Lat. nancisct ‘ob- tain, receive’; Goth. ga-nohs ‘enough’, etc.; Ir. do-iccim ‘come’ (10.48). The meaning ‘reach, attain’ appears to be the primary one and ‘carry’ a secondary, in part already IB, prob. through ‘cause to re
```


## [2026-09-07T18:22:41.446Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD asidan\" && grep -n \"آسید\\|آسیدن\\|خورآس\" incoming/FFD/FFD_pages.txt | head -20; echo \"=== BQT v1 asidan\" && grep -n \"آسیدن\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -20",
 "description": "Grep Persian sources for آسیدن"
}
```


### [2026-09-07T18:22:41.519Z] TOOL RESULT

```
=== FFD asidan
=== BQT v1 asidan
```


## [2026-09-07T18:22:43.538Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON asidan\" && grep -n \"آسیدن\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head; echo \"=== khorasan etym\" && grep -n \"خورآسان\\|خور آسان\\|خراسان\" MON_part1.txt 2>/dev/null | head -5",
 "description": "Grep Mo'in for آسیدن and خراسان"
}
```


### [2026-09-07T18:22:43.627Z] TOOL RESULT

```
=== MON asidan
=== khorasan etym
8635:کردن؛ اشتباه کردن. (مص‌م.) منسوب به خطا (اين کلمه بیشتر در خراسان بخصوص مشهد 
19644:بابل: ۵1 (.) مغرب؛ مق. خراسان به 
21369:سرخ‌رنگ که در خراسان و کرمان یافت 
22686:و انجیر و سب. (میوة اخیر در خراسان 
22781:گبلان خوزستان» فارس» خراسان»
```


## [2026-09-07T18:22:50.515Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FRS_pages.txt FSF_pages.txt BQT_v1_pages.txt BQT_v2_pages.txt MON_part1.txt; do echo \"=== $f\"; grep -n \"اسیدن\\|آسد\\b\\|خورآسد\\|خور آسد\" $f | head -5; done",
 "description": "Alternative spellings grep"
}
```


## [2026-09-07T18:22:50.524Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T18:22:51.870Z] TOOL RESULT

```
=== FRS_pages.txt
16446:                           ‫آسده را یر‬
17209: ‫ز هامون بر آسد خروش حکاو‬                   ‫کراو‬
=== FSF_pages.txt
794:‫(‪)۱-۷۵۱-۹۱۳‬‬                                   ‫(استم مسصدر از آراسیدن)‪ :‬اسایش‬
3309:‫خراسان‌ ان شوه کز وی خور آسد‬                    ‫چنین است‪ :‬خوراسان [خراسان] مشرق‬
3310:‫خورآسد پهلوی باشد‪ :‬خور آید‬                      ‫خوروران [خاوران» خاور] مغرب‪ .‬باختر‬
16166:        ‫هراسیدن‪ ,‬آشفته پوریشان شدن‪:‬‬
=== BQT_v1_pages.txt
18895:بر ماسیدن عبمعنی وین
24881:۴ ر: پرماسیدن ویرمای . ۵ رك: پرماسدن (حاشیه) . رك: برماه .
25122:رو اسیدن » بر وزن سر خاربدن .
=== BQT_v2_pages.txt
10568:               ‫خراسان آن بود کزوی خورآسد‬                              ‫زبان پپلوی هر کو شناسد‬
=== MON_part1.txt
9515:هراسیدن. 
17296:باد کردن؛ برآماسیدن» آماس کردن» ورم 
17299:کردن. آماسیدن. (.) آماس, ورم؛ ج. 
22583:بر که: (۵-) 3۵۲62 [ع.] .( آیگن آسدان؛ 
22724:برماسیدن: 0۸۲83-۲ [- بر ماسیدن]
```


### [2026-09-07T18:22:51.875Z] TOOL RESULT

```


```


## [2026-09-07T18:22:59.616Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF around 3300\" && sed -n '3290,3325p' FSF_pages.txt; echo; echo \"=== FSF pdf page tag\" && awk 'NR<=3309' FSF_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -2",
 "description": "Read FSF khorasan entry"
}
```


## [2026-09-07T18:23:00.545Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 around 10568\" && sed -n '10540,10600p' BQT_v2_pages.txt; echo \"=== page tag\"; awk 'NR<=10568' BQT_v2_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -2",
 "description": "Read Borhan khorasan entry"
}
```


### [2026-09-07T18:23:00.936Z] TOOL RESULT

```
=== FSF around 3300
 ‫سخنوران پیشین گاه باختر را به معنی‬            ‫‏)‪(VAT-114-1‬‬
  ‫ور رابه‌معنی مغرب آورده‌اند‪:‬‬ ‫او‬‫خرق‬
                                   ‫مش‬                  ‫از اسدی ( گرشاسب‌نامه ‪:)۷۱۲-۷۱‬‬
 ‫رودکی خراسان را به معنی مشرق‬                                 ‫بر آن آهنی نیزة یل فکنن‬
‫[چنانکه در زبان پهلوی نیز چنین است] و‬           ‫زد آگنور چون مرغ بر بابزن‬
     ‫خاور را بهمعنی مغرب بکار می‌برد‪.‬‬              ‫از فخر گرگانی (ویس و رامین ‪:)۴۶-۲۸‬‬
                 ‫(نفیسی بیت ‪:)۹۲۸-۰۲۸‬‬                       ‫سنان نیزهگفتی بابزن بود‬
      ‫مهر دیدم بامدادان چون بتافت‬              ‫بروبر مرغگرد تیغزن بود‬
 ‫اخزراسان سوی خاور می‌شتافت‬                                                         ‫بابک‬
      ‫نیم روزان بر سر ما برگذشت‬                ‫مرکب از باب [‪:‬پدر] ‪+‬ک [‪:‬نشانه تصغیر ]‪:‬‬
‫چون به حاور شد زمانادید گشت‬                                                      ‫پدرک‪:‬‬

 ‫تک ن رای نها خراسان‬                                          ‫بپرسید ازو راه فرزند خرد‬
         ‫معنیمی‌کند (ویس ‪:)۵ ۱۷۱-۱‬‬              ‫سوی بابکش راه بنمود گرد‬
 ‫خوشاجایاسرو بوم خراسان‬                         ‫(دقیقی ‪)۶-۱۱-۷۶۶‬‬
 ‫راهی‌خور آسان‬ ‫درو باش و جهام‬                                                  ‫اوور‬
                                                                                  ‫خختر‬
                                                                                     ‫با‬
 ‫زب ان پسهلوی هرکو شناسد‬                        ‫نام‌های جهات چهارگانه به زبان پهلوی‬
‫خراسان‌ ان شوه کز وی خور آسد‬                    ‫چنین است‪ :‬خوراسان [خراسان] مشرق‬
‫خورآسد پهلوی باشد‪ :‬خور آید‬                      ‫خوروران [خاوران» خاور] مغرب‪ .‬باختر‬
 ‫رس را خور زو برآید‬   ‫او‬ ‫پاق‬‫عر‬                                    ‫شمال و نیمروز جنوب‪.‬‬
    ‫ان‬    ‫ینی‬
            ‫آد مع‬
                ‫رابو‬
                   ‫وان ر‬
                       ‫ر اس‬
                          ‫خ‬ ‫خو‬                 ‫«خربران» پهلوی‪[ ۲۵۲۵۵۲۵۳ :‬مغرب ]؛‬

 ‫کجااز وی ور آید سوی ایسران‬                    ‫نیمروز‪ .‬پهلوی‪[ ۶۵:۳۵۷۱ :‬جنوب |‬
‫چه خوش نامست و چه خوش آب و خاکست‬                ‫خراسان پهلوی‪« .‬ةئةاه× [مشرق]‬

  ‫یر ات ره مدع ی‬                                                        ‫اپاختر‪ .‬پهلوی‪]:‬‬
‫ب(ایداد) افراه‬                                      ‫‪۷‬‬

                     ‫از فخر گرگانی (‪:)۸۷-۱۲‬‬             ‫و‬      ‫(‪۴-۸۶۱-۴۳۸‬‬         ‫شاهامه‬        ‫از‬

=== FSF pdf page tag
```


### [2026-09-07T18:23:02.366Z] TOOL RESULT

```
=== BQT v2 around 10568
‫تح اول بورزن لواش ‪.‬‬
                  ‫«‬                 ‫خر اش‬                     ‫امت که در مقابل مغرب با ‪ -‬و نام ولابتی‬
                                        ‫‪۲ ٩‬‬       ‫‪۰‬‏‬




 ‫‪-‬‬    ‫کردن‬      ‫وفبمعنی رخنه‬       ‫رحنه باشف‬           ‫نجعي‬    ‫آن ولات در مشرق‬         ‫وون‬
                                                                                         ‫مشهور چ‬    ‫هم هست‬
‫و تایکار‬    ‫و از کار افشاده وسقط شده‬      ‫‪-‬‬   ‫و خراشدن‬        ‫فاری و عراق واقم است بنا بران بدین نام‬
 ‫و دوستده‬      ‫زده‬   ‫خف‬   ‫و موه‬     ‫‪۴‬‬         ‫ا‬   ‫آهده‬
                                                                ‫ازموسیقی‪.‬‬    ‫خوانده‌اند ‪ -‬ونام نفمه‌ای هم هت‬

                                        ‫را نگیوزیند ‪.‬‬         ‫دروژن بداختر» موذیات‬
                                                                                 ‫حر استر ‪ /‬ب‬
‫= بر وزن ترآشیدن ›‬                ‫حر اشیدن‬                    ‫راکوبند مطلقاهم‌چو ماروعقرب وزنبور رموزچه‬
                                                                                                ‫وامثال آن ‪.‬‬
           ‫بمعنی ریش کردن ومجروح ساختن باشد ‪.‬‬
 ‫‪ ۰‬معرب‬        ‫طین‬
                 ‫ازن‬
                   ‫لو‬‫سبر‬
                       ‫حراطین =‬
                                                               ‫‪-‬نابه آاسزمان‬
                                                                           ‫خر اس خر اب ک‬
 ‫خراتین امت و آن کرمی باشد که در گل نرم‬
 ‫تکون پیدا کند و بعربی حمرالارض گوبند جم‬                       ‫به‌عنی خراس‬     ‫جر اس خسسان ‪-‬‬
                                         ‫‪ - ۱‬دریپلوی ‪(0252۲2۷۲‬مشرق) «میناه‪: › ۲: ۳۱‬‬
               ‫دروباش و جپان را میخور آسان‬                           ‫خوشا جابا بر و بوم خراسان‬
               ‫خراسان آن بود کزوی خورآسد‬                              ‫زبان پپلوی هر کو شناسد‬
               ‫کجا ازوی خورآبد سوی ابران ‪.‬‬                          ‫خورآسان رابودمعنی‪ :‬خورآبان‬
     ‫«وس ورامن ص ‪۱۷۱‬؟‪.‬‬
      ‫ورك ‪ :‬اسفا ‪ ۲ :۱‬ص ‪ « ۹۷۱.۰‬خراسان " تفسیره‌المشرق » « مفاتیج‌العلوم خوارزمیس‬
     ‫»رات ‪,‬‬ ‫ه‬     ‫بانا»ن‬   ‫طهست‬
                              ‫‪:‬براشهر (بشابور ‪۰‬ف‬    ‫‪ ۲‬؛ خراسان قدیم شامل چهاربخش‌بوده ا‬
      ‫پوشنگه » بادغیس » طوس) ‪ -‬مروشاهجان » سرخس » دا » ابیورد ‪ .‬مروالرون » طالقان آمل‬
     ‫‪,‬کگوانان » طخارستان علیا ‪ ,‬خت ‪ ,‬اندرآبه » بامیان » بفلان ‪ ۰‬والج » روستای بیل ‏‬  ‫فارباب ز‬
     ‫‪۰‬لم » سمدگان ‪ -‬ماوراءالنپر( بخارا ‪ ۰‬چاچ » طراز‬  ‫بدخشان ن‪۰‬رمن ‪ ۰‬چنانیان‪ .‬طخارستان سفلی خ‬
     ‫‪ ,‬اشروسنه ‪ ۰‬سیام » فرغانه و سمرفند ) « معجم‌البلدان »‬             ‫تان‬
                                                                         ‫فی»‬
                                                                           ‫نشد» صفد ‪ ۰‬هو کس ‪.‬رنو‬
     ‫خراسان کنونی ازشمال محدود است بماوراءاللهر ‪ ۰‬از مشرق بهربرود ودشت ناامید » از جنوب‬
     ‫بکرمان واز مغرب بعراق عجم و استراباد ‪ .‬طول آن ازشمال بجنوب بکرمان اوز مغرب بعراق‬
     ‫عجم و استراباد ‪ .‬طول آن ازشمال بجنوب ‪ ۰۰۸‬واز مشرق بمغرب *‪ ۸4‬کیلومتر و ماحت آن‬
      ‫کشف رود ورود‬‫گکارن و‬  ‫نزديك به ‪ ۰۰۰۰۲۳‬کیلومتر ھربح است ‪ .‬رودهای مهمی مانند اترك و‬
       ‫‪.‬معیت‌خراسان قرب ‪۰۰۰۰۰۳۴۱۰۱‬‬  ‫"یبشرم (قراسو ) درآن جاری است وبمصرف زراعت میرسد ج‬
     ‫است ‪ .‬کرسی‌آن مشهد وشهرهای‌آن ‪ :‬سرخس ‪ ,‬دره گز ‪ ۰‬فوچان » بجنورد ‪ ۰‬نیشابور ‪ ,‬جوین ‪۰‬‬
     ‫ولشن‬
        ‫سبزوار » اسفراین * جام » باخرز خوواف » تربت حیدری ‪ :‬ترشیز ‪ ۰‬فردوی ( تون ) گ‬
           ‫(طبس) » قاینات » شاهرود » سمنان وداعفان امت ‪.‬ک«یهان ‪ .‬جفرافیای سیاسی ‪.* ۹۷۱-۰۱۲‬‬
                     ‫‪ - ۴‬پپلوی ‪ , 7(8)05]۵۳5‬اوستا ‪ « 3615]8۳6-‬اسفا ‪ ۲ :۱‬ص ‪٩ ۰۸‬‏ ‪.‬‬
                                                       ‫‪ = ۴‬غراش ( ه‪ .‬م) «اسفا ‪ ۲ :۱‬ص ‪. ۰۷۰‬‬
         ‫ببر دو رخافت هست خراش ‪.‬‬                               ‫‪ ۴‬ت اکر چه لطف دارد تقش‬
      ‫رکوید‌سمرقندی‪ « .‬لغت فرس‪۵*۲‬؟‪.‬‬
                      ‫یدن ( یوند مصدری ) = غراشیدن («‪.‬م‪).‬‬                   ‫‪.‬م(‪) .‬‬
                                                                                 ‫«راش‬
                                                                                    ‫‪ -‬از خ‬
  ‫واح‬   ‫جع‬                                                                                               ‫خرافات‬

 ‫خوش راهم کنته‌انده ‪ -‬ویمعنی شادی وشادمالی‬                                                         ‫حنایقبطیه ‪٩‬‏‬
 ‫هم‌آمده است‪ -‬وبمعنی‌مهمالی وضیافت! ‪-‬ومرردة‬                ‫خر افات = بفتح اول و بافا(‪ )۱‬بر‬
                      ‫‪.‬‬    ‫بمهمالی طلبیدن همهت‬
=== page tag
```


## [2026-09-07T18:23:23.644Z] TOOL CALL #37: WebSearch

```json
{
 "query": "خراسان etymology xwarāsān \"āsān\" sunrise Middle Persian verb ās- \"to come\""
}
```


## [2026-09-07T18:23:25.783Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86",
 "prompt": "Give the full etymology section for خراسان (Persian): what is the Middle Persian form, how is it analysed (xwar + āsān), what verb/root is āsān from, and any cited sources."
}
```


### [2026-09-07T18:23:31.098Z] TOOL RESULT

```
Web search results for query: "خراسان etymology xwarāsān "āsān" sunrise Middle Persian verb ās- "to come""

Links: [{"title":"خراسان - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86"},{"title":"Eran-asan-kerd-Kawad","url":"https://en.wikipedia.org/wiki/Eran-asan-kerd-Kawad"},{"title":"Khorasan - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Khorasan"},{"title":"Chorasan - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Chorasan"},{"title":"Khorasani style (poetry)","url":"https://en.wikipedia.org/wiki/Khorasani_style_(poetry)"},{"title":"Khurasan — Grokipedia","url":"https://grokipedia.com/page/khurasb"},{"title":"Khorasan meaning thus the name Khorasan (or Khorāyān خورآيان) means sunrise, viz.","url":"https://karosseriebau-frenzen.de/evgd/9891"},{"title":"Khwarasan — Grokipedia","url":"https://grokipedia.com/page/khwarasan"},{"title":"Khorusan - Khorasan","url":"https://grokipedia.com/page/khorusan"},{"title":"What Does The Name Khorasan Mean?","url":"https://www.names.org/n/khorasan/about"}]

Based on the search results, here's what I found about the etymology of Khurasan:

The name Khurasan comes from earlier خوراسان (xwarāsān), from Middle Persian hwlʾsʾn' (xwarāsān), literally meaning "sunrise; east". It is equivalent to خور (xwar, "sun") + آسان (âsân, "coming").

More specifically, the term "Khwarasan" originates from Middle Persian Xwarāsān, a compound derived from khwar meaning "sun" and āsān (from the verb āyān, denoting "to come" or "rising"), collectively interpreted as "where the sun rises" or signifying the eastern frontier of the Sasanian Empire.

The element āsân is the Parthian conjugation of a verb meaning "to come, to rise". This confirms your query about the Middle Persian verb ās- "to come" being the source of the "āsān" component, which together with "xwar" (sun) creates the compound meaning related to sunrise and the eastern direction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-07T18:23:31.781Z] TOOL RESULT

```
# Etymology of خراسان (Persian)

**Middle Persian Form:** hwlʾsʾn' (xwarāsān)

**Analysis:** The word breaks down into two components:
- خور (xwar) = "sun"
- آسان (âsân) = "coming"

**Verb Root:** According to the text, "آسان (âsân) is the Parthian conjugation of a verb meaning 'to come, to rise.'"

**Related Forms:** The entry notes that for the first part, one should "compare خورشید (xoršid)" and for the second part, compare "Baluchi آسگ (ásag, 'to rise')."

**Etymology Summary:** The word literally means "sunrise; east" from Middle Persian, ultimately derived from the sun-related root plus the Parthian verbal element indicating "coming/rising."

**Cited Sources:** The etymological information is presented directly in the Wiktionary entry without specific academic source citations for the etymology section itself, though historical usage is demonstrated through the 11th-century quotation from Fakhruddin As'ad Gurgani's *Vis and Rāmin*.
```


## [2026-09-07T18:23:46.033Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG sad\" && grep -n \"sad-\\|\\*had\\b\\|Parth. ʾʾs\\|Khwar\" CHEUNG.txt | head -30",
 "description": "Grep Cheung for sad-"
}
```


### [2026-09-07T18:23:46.071Z] TOOL RESULT

```
=== CHEUNG sad
746:Choresmian = Khwarezmian 
3127:*ni-daja- < *ni- + *daH? and *ni- + *had respectively. 
3131:from a nasal pres. formation *Ci-naH-. Naturally, interference with the root *had ‘to 
5100:163 f. connects Skt. drsad- to Av. zarsuua- ‘stone’ (Yt 10.39, V). 
8914:*had 125 
8937:*had ‘to sit, be seated’ 
8948:*OLD PERSIAN: (+ *ni-) ni-sad- (caus.) ‘to establish’ = Kent: 212 
9701:1999: 335; Shahbakhsh: s.v. gusad- 
10726:*NWIR: (?) Qohr. ah-/aha(d)- ‘to be seated, remain’ (rather from *had ?) 
20058:morphologically impossible (*pa-zd- ‘absitzen’, from *had), on which see *pazd'. 
21794:*KHOTANESE: OKh. sad- (sai-, sei-, sas-) ‘to appear, seem’ || (+ *pati-) pasad- (pasai-, 
21802:*sad-), especially when the corresponding caus. formation *sandaja- is well attested 
24139:entertain, comfort oneself, Wa. psad-/p$ad-, pSat-/psat- ‘to touch; to be restless, 
24209:*NWIR: © NP nisém ‘nest’ is rather from the root *had, cf. Pth. nsdm ‘seat’. 
30330:*KHOTANESE: ysir- (ysad-) ‘to become old’ => SGS: 113 
31406:Henning — MacKenzie: Walter Bruno Henning, A fragment of a Khwarezmian dic- 
31774:MacKenzie 1975: David Neil MacKenzie, Khwarezmian imperfect stems, Fs 
31790:MacKenzie 1990: David Neil MacKenzie, The Khwarezmian element in the Qunyat 
31794:MacKenzie I, etc.: David Neil MacKenzie, The Khwarezmian Glossary-I, BSOAS 
31795:1970 (33/3): 540-559. The Khwarezmian Glossary-II, BSOAS 1971 (34/1): 74- 
31796:90. The Khwarezmian Glossary-III], BSOAS 1971 (34/2) 314-330. The 
31797:Khwarezmian Glossary-IV, BSOAS 1972 (34/3): 521-537. The Khwarezmian 
32107:Schwartz 1970: Martin Schwartz, On the vocabulary of the Khwarezmian 
37215:pasad-, 332 
37722:sad-, 332 
37801:ysir- (ysad-), 470 
49673:p3ad-/psad-, pšat-/pšat-, 
49692:rasad-, rosoó-/rosn-, 327 
55508:*had, *HaHh 
57834:*had, *HaHh
```


## [2026-09-07T18:23:48.089Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG nas\" && grep -n \"^\\*nas\\|\\*naH\\|nas- .to reach\\|NAS\" CHEUNG.txt | head -20; echo \"=== CHEUNG had/sad headwords\" && grep -n \"^\\*[a-zA-Z]*sad\\|^\\*had\" CHEUNG.txt | head",
 "description": "Grep Cheung for nas/had roots"
}
```


### [2026-09-07T18:23:48.205Z] TOOL RESULT

```
=== CHEUNG nas
12545:*nas, Insler, Gäthäs: 326) || (+ *fra-) ‘to attain, reach’ = Liste: 40f. 
18656:*nas ‘to disappear; to perish’ 
18675:*nas 283 
36989:*naspus- (naspus-), 303 
55362:*nas (s.v.), *uarc (s.v.) 
=== CHEUNG had/sad headwords
8914:*had 125 
8937:*had ‘to sit, be seated’ 
21802:*sad-), especially when the corresponding caus. formation *sandaja- is well attested 
22317:*sad 341 
55508:*had, *HaHh 
56795:*xsad 
56797:*xsad, *marzd 
57816:*sad 
57834:*had, *HaHh
```


## [2026-09-07T18:23:52.965Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8937,9010p' CHEUNG.txt",
 "description": "Print Cheung *had entry"
}
```


### [2026-09-07T18:23:53.005Z] TOOL RESULT

```
*had ‘to sit, be seated’ 

*AVESTAN: hiö- ‘to sit, be seated’ || (+ *abi-) ‘to be seated on (a horse)’ || (+ *ni-) ‘to 
sit down’ — Liste: 71 

Pres. them. red.: IND. 3sg. YAv. nishióaiti (Y 10.15), SUBJ. 3sg. Y Av. nishióat (V 16.1), OPT. 2sg. 
Y Av. nishiööis (Н 2.13, Vyt 59), 3sg. Y Av. nishióoit (V 9.29), med. 3sg. Y Av. nishióaeta (V 8.11, V 9.33 
ff., V 16.8 f£); Perf.: ОРТ. 3sg. YAv. ni hazdiiat (Yt 13.13); Inf.: ҮАУ. aiBi.Sasta; Caus.: IND. 35р. YAv. 
"nisaóaiieiti (FrA 24), INJ. 35р. YAv. nisaóaiiat (Y 9.24), OPT. 2sg. Y Av. nisaóaiiois (H 2.14); Desid.: 
INJ. 3sg. OAv. hisasat (Y 32.13) 

*OLD PERSIAN: (+ *ni-) ni-sad- (caus.) ‘to establish’ = Kent: 212 

Caus.: impf. IND. 1sg. niyasadayam <n-i-y-S-a-d-y-m> (DNa 36), niSadayam <n-i-8-a-d-y-m> (XPh 34) 
*MIDDLE PERSIAN: (+ *ni- MMP nsyy- ‘to sit down, settle oneself’, MMP ns’y-, 
BMP n3’n- (caus.) ‘to place, settle, ground, establish = DMMPP: 245b f. 

Pres.: IND. 3sg. MMP nsyyd, SUBJ. 3р1. MMP *nsyy’nd, IMPV. 2sg. nsyd; Partic.: perf. pass. MMP nšst, 
etc. 

*PARTHIAN: (+ *ni-) nšyd- ‘to sit (down), settle oneself’, also nšyl- (< Bact./Sogd. ?). 
= Ghilain: 50 | DMMPP: 245b f. 

Pres.: IND. 3sg. nsydyd, 3р1. nSylynd; Partic.: perf. pass. nšst; Inf.: "nsstn 

*KHOTANESE: (+ *ati-) tva’y- (ttuva’-) ‘to bring across’ || (+ *abi-) bvai(’)- ‘to 
mount; ride’ || (+ *ni-) nät- ‘to sit down’, näta’s- (na’s-) (inch.) ‘to end’ = SGS: 39, 
102, 53 f., 57 

*SOGDIAN: (+ *pati-) BSogd. ’pc’t ‘time, instant’ || (+ *pari-) SSogd. prsyö (old 
caus.) ‘to sit through, out’ || (+ *ni-) BSogd. пуб, CSogd. пуа, MSogd. пуб ‘to sit 
down’, BSogd. n(y)s’y6, BSogd. nysyö, CSogd. nsyd (caus.) ‘to plant; establish’ 

(+ *pari-) Impf.: IND. 2sg. SSogd. prysyöy || (+ *ni-) Well attested: Pres.: IND. 3sg. BSogd. nyöt, 3pl. 
BSogd. nyö’nt, SUBJ. 3sg. BSogd. nyö’t, etc. 

*CHORESMIAN: (+ *ni-) ny0- ‘to sit; to be, become’, m/nh’zy- (caus.) ‘to place’ 
c» Samadi: 127 


126 *hah 


*BACTRIAN: (+ *ni-) vipoApo, мролцо ‘seat (of the gods), throne, dwelling’. 0 Cf. 
Pth. nsdm, MMP nëm, BMP nsdm ‘seat’. = S-W, Bact.: 208b 

*NWIR: (+ *4-) Abz. avad/av-, Abyan. aya(y)-/ay-, Qohr. aha(d)-/ah-, Ard. axo/ax-, 
Tr. axa(y)-/ax-, Nn. āšis-/āš- ‘to become seated’ (influenced by *HaHh ‘to be seated, 
sit’ ?) || (+ *ni-) Widely attested: NP niSastan/nisin-, Bal. nist/nind-, Kurd. nistin, 
Zaz. ro-nistis/ro-sen-, Awrom. nistáy/-nis-, Tt. (Esh.) ansin/ansest, Gz. ni(y)-/nist, 
Gil. (Rsht.) nistaen/nisin-, Gur. (Kand.) nist-/-nisan-, Ham. he-nistän/ he-i-ni-, Semn. 
nia- ‘to sit’, Sang. -nést-/ neeroen-, Shamerz. -nist-am-/näsin-am-, Sorkh. -niäst-, 
(supplet. ?) nin-, Lasg. -nest-/nieroen-, Isfah. nišdän (supplet. ?) niy-, Sist. rsin-, Siv. 
rsin-/nist ‘to sit down’ (with dissim. n- > r-), Gz. nan-/nast (caus.) ‘to make to sit 
down’. 9 The intervocalic -r- attested in some modern dialects is perhaps the result 
of a "Parthian-like" development: *-d-> *-6-> -г- ?, cf. Sorkh. -sust-/Sur- ‘to wash’, 
s.v. *xSaud. 

*NEIR: (+ *8-) Sh. yä0 (m.), Bart. y00, Sariq. yo0, Yzgh. ya ‘nest’ || (+ *upa-) Oss. 
I. badyn/badt, D. badun/badt ‘to sit’ || (+ *ni-) Pash. näst ‘seated, sitting’, Sh. n10-/ 
nust, Rosh. ni0-/nost, Bart. ni0-/nóst, Yzgh. ni0-/noyüst, Sangl. nió-, Yi. nix-/niast-, 
M. nix-/nidst-, Yghn. nid-, Wa. nbizd-, nazd-/nayn- ‘to sit down’, (caus.) Sh. näö-/ 
näöd, Rosh. n&ó-/neód, Rosh. n&ö-/nüst, Bart. noó-/nóst, Sariq. nalaóon-/nalaóond, 
Yzgh. nidon-/nidont ‘to make to sit down’, Wa. nid(1)v-/nidovd-, niö(bI)v-/nidovd 
‘to place, give a seat’ 

*MISC: (+ *ni-) Orm. n-/nustuk, nastak ‘to sit down’ = ney-/nöstök, nóstok, nostok, 
Orm. naw- (orig. caus.) ‘to cause to sit down’ = naw-/nawok 

*SANSKRIT: sad ‘to sit’ (RV+) = EWAia П: 692 

9 The apparent loss of the expected ruki *š (after *ni-), cf. YAv. nishiöa-, Pth. nsyd-, 
Skt. ni-sida-, in several (esp. East) Iranian languages is strange: replaced by 
(simplex) *hida- ? Also the appearance of voiceless -0- in some languages needs an
```


## [2026-09-07T18:23:53.894Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12500,12600p' CHEUNG.txt",
 "description": "Print Cheung *nas 'to reach' entry"
}
```


### [2026-09-07T18:23:53.939Z] TOOL RESULT

```
does not exist, on which see further Skjaervo, SVK II: 62 f. 


*Hnas (Has) 183 


*NWIR: NP hunar ‘skill, art’ (with short -ü- !) || (+ *apa-, *abi- or *upa- ?) ? Gab. 
afnurdan, Yzd. pe-nart ‘to take’ || (+ *ui-) Bal. ginast/ginar- ‘to hold, take possession 
of, pull (a bridle)’ 

*NEIR: ? Oss. I. nersyn/nerst, D. nersun/nerst ‘to swell up; to become fat’, (ppp.) ? 
Oss. nard, narst ‘fat, well-fed’ || (+ *abi-) ? Oss. I. evnalyn/evneld, D. evnalun/ 
zvnald ‘to touch’. O The Pamir forms, Sh. winir ‘stall, pen, manger’, Yzgh. wanur 
‘long plank’, Wa. wandr ‘stable’, mentioned in EVS: 90b and compared to MMP 
wyn’r-, may rather be a compound with *uan(ä)- ‘tree’, YAv. vana-, BMP /wan/, 
Pth. wn, etc. 

*MISC: Par. nar-/nari ‘to be able’ 

*SANSKRIT: sundra- ‘powerful, potent’ (RV+) = EWAia П: 740 

© According to Mayrhofer, EWAia П: 20, the IE ‘man’ form *Нпег- (Skt. nár-, Av. 
nar-, Gr. àvip ‘man’, etc.) goes back to a verbal root *Honer- ‘to be strong, have 
vitality’. The problem is that the postulation of such a verbal root is unsubstantiated, 
as there is no (clear) evidence for the existence of this verbal root in IE. The modern 
Ir. forms, Par. nar-/nari et al. can easily be interpreted as denominative, which is the 
case with Lith. noréti, Olrish nertaim, etc. The IE reflexes that can be gleaned from 
Pokorny: l.c. rather suggest an originally adjectival/nominal root *Honer- from 
which we can derive the IE ‘man’ forms and the denominative verbs in Celtic, Baltic 
and Iranian. 

«PIE *Honer- ‘strong/strength, potent/potency' = LIV: — | Pok.: 765 

*IE COGNATES: Gr. nvopén ‘manliness’, Lat. neriösus ‘strong’, Olrish nertaim ‘I 


strengthen’, Lith. noréti ‘to want’ < nöras ‘wish, desire’ 
*REFERENCES: IIFL I: 276b; Abaev, Slovar’ I: 204 f.; Abaev, Slovar’ II: 170, 157 f.; Steblin-Kamenskij 
1999: 395; Shahbakhsh: s.v. ginar- 


*Hnas (Has) ‘to reach, attain, take’ 

*AVESTAN: näs- (a3-) ‘to reach, attain’ || (+ *abi-) ‘to attain’ || (+ *aua-) ‘id.’ || (+ *à-) 
‘id.’ || (+ *para-) ‘to fail to reach’ (Kellens — Pat III: 272, but ‘to disappear’ < 
*nas, Insler, Gäthäs: 326) || (+ *fra-) ‘to attain, reach’ = Liste: 40f. 

Pres. nu-: IND. 3sg. YAv. auua.asnaoiti (Yt 10.24), INJ. 3sg. ҮАУ. аппа asnaot (Yt 10.89), SUBJ. 35р. 
Y Av. (them.!) auua.asnauuät (P 20), OPT. 3sg. YAv. frasnuiiat (Yt 11.5); Aor. {1} athem.: INJ. med. 
3sg. OAv. frasta (Y 43.14), OPT. 35р. OAv. frösiiät (Y 46.8); Aor. {2} s-: SUBJ. med. 35р. ҮАУ. 
(them.!) nasaite (Yt 19.12), 1р1. OAv. nasama (Y 44.13), OPT. Ipl. ҮАУ. nasima (Y 70.4); Aor. {3} 
them. red.: impf. IND. 3sg. OAv. anasat para (Y 53.7), INJ. 3sg. OAv. nasat (Y 51.16, Y 53.6); Aor. {4} 
them.: IND. 3р1. ? YAv. aißinäsonti (Y 23.3, Y 67.3); Partic.: aor. {2} med. YAv. (them.!) nasomna- (Yt 
13.58, 9.30 f£), aor. {4} ? (superl.) YAv. aißinasastomam (Y 71.3); Inf: aor. {1} ? OAv. azdiiai (Y 
51.17), aor. {2} OAv. а naše (Y 44.14); Caus.: IMPV. 2р1. ? YAv. nasaiiata (A 3.5). 0 For an analysis of 
OAv. āždiiā see Humbach 1959 II: 92. 


184 *Hrab/fl 


MIDDLE PERSIAN: (+ *pati- MMP pn’h, ВМР pn’h /panäh/ ‘protector; refuge’ 
c DMMPP: 275b 

*KHOTANESE: nas- ‘to take’, nasa- ‘share’ = SGS: 52 f. 

*NWIR: (+ *pati-) NP panah ‘refuge, asylum’ 

*NEIR: Pash. nas-, nis-/niwul ‘to take, seize, catch’, Ishk., Sangl. nas-/nöö-, Yghn. 
nos-/nöta- ‘to take (away); to buy; to seize, catch’ 

*MISC: Огт. nas-/nök, nis-/nök ‘to seize, catch’ = nas-/nók 

*SANSKRIT: nas ‘to reach, attain ° (RV+) = EWAia II: 27 

«PIE *H>nek- ‘to reach, attain’ = LIV: 282 f. | Pok.: 316 ff. 

*IE COGNATES: Gr. noö-nverng ‘reaching down to the feet’, Gr. öinvexng, (Att.) 
diaveKrs ‘continuous’, Olrish -ánaic ‘reached’, Goth. ga-nah ‘is enough, suffices’, 
OE genög, Engl. enough, etc. 

*REFERENCES: EVP: 54; IFL I: 402b f., HFL II: 405a; Andreev — PeSéereva: 295b; DKS: 180b Ё; Werba 
1997: 390; NEVP: 58; Kiefer 2003: 202 


*Hrab/f ‘to go’ 

*MIDDLE PERSIAN: MMP rw-, BMP rwb-, Iwb- /raw-/ ‘to go, proceed’ || (+ *ni-) 
MMP nyrw- ‘to go down’ ?, MMP nyrwysn ‘movement downwards’ = DMMPP: 
296b f., 253b 

Pres.: IND. 15р. MMP rwym, 3sg. MMP rwyd, rwyyd, SUBJ. 3р1. MMP mind Partic.: pres. MMP 
“rw’n, perf. pass. MMP rpt, MMP "rft || (+ *ni-) Pres.: SUBJ. 3sg. MMP nyrw’d {uncert. reading} 
*KHOTANESE: (+ *4-) OKh. arüh- “о move, shake’ || (+ *ш-) OKh. bäräh- (brah-) ‘to 
soar up’ © SGS: 11, 98 

*NWIR: NP raftan/rav-, Bal. rapt (supplet. Sut) / ra(w)- ‘to go’, Kurd. (Kurm.) roy- ‘to 
go, walk’, (Sor.) ro- ‘to leave’ || (+ *ui-) Judeo-Ham. vorows- Ham.‘to get up, 
et _ I 
*NEIR: (+ *ш-) Sh. wirafc-/wirtivd, Rosh. wirafs-/wirüvd, Bart. wirafs-/wirtivd, 
Sariq. warofs-/warüvd, Yzgh. (w)urufs-/(w)uruvd ‘to rise, stand up’, (caus.) Sh.
```


## [2026-09-07T18:24:10.553Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\*.* ‘to come\" CHEUNG.txt | head -20; echo \"=== sad entry\"; sed -n '22317,22400p' CHEUNG.txt",
 "description": "Cheung roots meaning to come; *sad entry"
}
```


### [2026-09-07T18:24:10.640Z] TOOL RESULT

```
3346:*CarH ‘to come and go, wander’ 
3348:*AVESTAN: car- ‘to come and go’ || (+ *para-) ‘to pass over’ || (+ *ui-) ‘to go to and 
3762:*AVESTAN: S(ii)auu- (Sauu-, $0-) ‘to move, go’ || (+ *abi-) ‘to come to’ || (+ *fra-) ‘to 
7309:*AVESTAN: gam- ‘to come’ || (+ *apa-) ‘to go away, leave’ || (+ *abi-) ‘to come at’ || 
7365:*MIDDLE PERSIAN: MMP md, BMP mt- /mad-/ (pret. stem) ‘to come’, MMP z’m- ‘to 
10762:*OLD PERSIAN: ay- ‘to go’ || (+ *ati-) ‘to go along, beyond’ || (+ *a) ‘to come’ || (+ 
10805:*KHOTANESE: (+ *à-) OKh. his- ‘to come’ (with sec. h-) = SGS: 153 
11301:*AVESTAN: ar- ‘to start to move’ || (+ *a-) ‘to come, arrive’ || (+ *uz-) ‘to rise, go up’ 
11330:*MIDDLE PERSIAN: (old inch.) MMP rs-, BMP Is- (YHMTWN-) /ras-/ ‘to come, 
11386:*AVESTAN: ar- ‘to set in motion’ || (+ *uz-) ‘to rise, move up’ || (+ *fra-) ‘to come to’ 
14293:*ny’ms ‘to come to an end, be ended" 
14494:*NEIR: Sh. yad- ‘to come’, Rosh. yad- ‘to come’, ? Yghn. yat-/yätta ‘to find a place, 
19741:*AVESTAN: Y Av. pat- ‘to fly’ || (+ *aua-) ‘to fall down, off’ || + *4-) ‘to come, rush 
23471:*KHOTANESE: stä- (stä-) ‘to stand; be’, stas- (inch.) ‘to come to a standstill; to 
25542:*Өіај (*ti(n)j’) ‘to come to a halt, want to leave (from an awkward situation ?), 
25554:*CHORESMIAN: tynk- ‘to come to a standstill, stop’, (intr./inch.) tx- ‘to stammer, 
29023:*SOGDIAN: BSogd. xr’m ‘to come’ 
=== sad entry
*sad 341 


*MISC: Orm. say- ‘to rub’ = say-/sayok 

*SANSKRIT: 5а ‘to sharpen, whet > EWAia II: 627 

Ó The root *sauH' either reflects a rare ua-stem of *saH (similar to *fiHu, Kellens 
1984: 162) or, more likely, may have been the result of contamination with 


semantically similar roots: *dauH and *skauH. 
*REFERENCES: IIFL II: 245, 541b; EVS: 75b ff.; DKS: 429a f.; Paul 1998: 312b; Cabolov 1997: 72; Lecoq 
2002: 132; Kiefer 2003: 206 


*sauH ‘to bulge, swell up, increase’ 

*AVESTAN: su- (sáuu-) ‘to bulge, swell up, increase’ = Liste: 63 

Fut.: IND. 3sg. YAv. “saoSiiat® (A 4.6); Partic.: pres. pass. YAv. suiiamna- (Y 55.3, Y 70.4, V 4.2, intens. 
YAv. süsouuista- (Aog 19), fut. saosiiant-; Inf: OAv. süidiiai (Y 44.2, Y 49.3); Caus.: pres. INJ. 2sg. 
OAv. sauuaiiö (Y 51.9), SUBJ. 3sg. YAv. sauuaiiat (Yt 13.129) 

*MIDDLE PERSIAN: MMP swd, swwd, BMP swt /sud/ ‘profit, use, advantage’ 
=> DMMPP: 310a 

*KHOTANESE: (+ *fra-) LKh. hasv- ‘to swell’ 2 SGS: 151 

*BACTRIAN: 0000 ‘plenty’ {hapax} = S-W, Bact.: 224 

*NWIR: Bal. sit", si0/si- ‘to swell’, NP süd ‘ gain, profit’ 

*NEIR: Oss. І. sy-var, D. su-var ‘uterus’ || (+ *fra-) Oss. I. resyjyn/resyd, D. 
reesujun/resud ‘to swell’ 

*MISC: (+ *fra-) Orm. Susuk, sras-"ek ‘to swell’ 

*SANSKRIT: sav’ ‘to swell, to become strong, to increase, to prosper’ (RV+) 
= EWAia II: 623 

«PIE *KeuH;- ‘to bulge, swell up’ = LIV: 339 f. | Pok.: 592 ff. 

*IE COGNATES: Gr. коёо ‘I am pregnant’, Gr. к®но‹ (n.) ‘wave’, Lat. cavus ‘hollow’, 
in-ciéns ‘pregnant’, MWelsh cyw (m.) ‘young animal’, OE Aun (m.) ‘young one’. 
*REFERENCES: IIFL I: 409b; Abaev, Slovar’ II: 380 f.; Abaev, Slovar’ III: 213 f.; DKS: 476; Werba 1997: 
320; Shahbakhsh: s.v. si-; Korn 2005: 91, 314, 385 


*säd ‘to cover, protect, shield’ 

*AVESTAN: Y Av. saóaiianti- (f. ?) ‘long trousers ?’ (N 95) 

*MIDDLE PERSIAN: ВМР c'twl /čādur ‘sheet, veil’ (< late Skt.) || (+ *4-) BMP ’s’dk 
/asayag/ ‘shelter’ 

*SOGDIAN: (+ *а-) CSogd. ’s’dty ‘shielded, protected’ || (+ *pati-) SSogd. pts’6(°) 
‘shield’, CSogd. pts’6 ‘shield’ (Schwartz 1967: 141 f.) 

*NWIR: NP cadur ‘veil’ (< late Skt.) 

*NEIR: (+ *4-) Oss. I. asadyn/aseest, D. asadun/asast ‘to become clouded; to cover the 
seeds of the land before sowing; to plant (beans, peas)’ || (+ *upa-) ? Pash. psunai 
‘ambush’ || (+ *pati-) ? Pash. psöl (m.), psald (obl.) ‘ornament, gold or silver 
jewelry’ 


342 *séand (*skand) 


*SANSKRIT: chad ‘to cover, to conceal’ (RV+), chattra (n.) ‘parasol’ (Br.+) 
= EWAia I: 554 

© The root is exclusively Ir. with no certain IE cognates. The often cited 
comparison to the isolated form OE heteru ‘clothes’ can hardly be used for 
etymological purposes. 

*PIE — => LIV: 546 | Pok.: 919 

*REFERENCES: EVP: 60; Abaev, Slovar’ I: 76; Werba 1997: 185; Lubotsky 2001: 40; NEVP: 66 


*stand (*skand) ‘to break, cleave’
```


## [2026-09-07T18:24:19.688Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%DB%8C%D8%AF%D9%86",
 "prompt": "Does this page exist? If so give the Persian entry: meaning and etymology of آسیدن (āsīdan)."
}
```


## [2026-09-07T18:24:20.578Z] TOOL CALL #45: WebSearch

```json
{
 "query": "Parthian \"as-\" \"to come\" etymology Balochi \"āsag\" Sogdian \"ʾʾs-\" Proto-Iranian root"
}
```


### [2026-09-07T18:24:21.719Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:24:26.880Z] TOOL RESULT

```
Web search results for query: "Parthian "as-" "to come" etymology Balochi "āsag" Sogdian "ʾʾs-" Proto-Iranian root"

Links: [{"title":"Parthian - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/Parthian"},{"title":"Aspbed","url":"https://en.wikipedia.org/wiki/Aspbed"},{"title":"Parthian language","url":"https://en.wikipedia.org/wiki/Parthian_language"},{"title":"Parthian","url":"https://languagesgulper.com/eng/Parthian.html"},{"title":"Sogdia","url":"https://en.wikipedia.org/wiki/Sogdia"},{"title":"Drakht-i Asurig","url":"https://en.wikipedia.org/wiki/Drakht-i_Asurig"},{"title":"IRAN vi. IRANIAN LANGUAGES AND SCRIPTS - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/iran-vi-iranian-languages-and-scripts/"},{"title":"Iranian peoples - Wikipedia","url":"https://en.wikipedia.org/wiki/Iranian_peoples"},{"title":"Parthian language — Grokipedia","url":"https://grokipedia.com/page/Parthian_language"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/3402027/concepts"}]

The search results provide general information about Parthian, Sogdian, and Iranian languages, but do not contain specific etymological information about the Parthian "as-" root meaning "to come" or its connections to Balochi "āsag" and Sogdian "ʾʾs-" in relation to a Proto-Iranian root. 

The results confirm that these are Middle Iranian languages and that Parthian shares a common Proto-Iranian heritage, but they do not address the specific etymological comparison you're asking about. To find this specialized linguistic information, you may need to consult:

1. Academic linguistic resources focused on etymological studies of Middle Iranian languages
2. Specialized etymological dictionaries of Iranian languages
3. Scholarly articles on Proto-Iranian root reconstructions
4. Comparative studies of Northwestern vs. Eastern Iranian phonological developments

If you have access to academic databases like JSTOR or specialized journals in historical linguistics, those would be more likely sources for this detailed etymological analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T18:24:35.385Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD xwarasan\" && grep -n -i \"xwarasan\\|xwarāsān\\|hwlʾsʾn\" PHD.txt PHD_mackenzie.txt | head; echo \"=== NYB\" && grep -n -i \"xvarasan\\|khvarasan\\|hvarasan\" NYB_vol2_glossary.txt | head; echo \"=== KNT as-\" && grep -n -i \"^ā-sad\\|asa-\\|ās-\" KNT.txt | head -20",
 "description": "Grep Pahlavi and Kent"
}
```


### [2026-09-07T18:24:35.461Z] TOOL RESULT

```
=== PHD xwarasan
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
PHD.txt:1728:east OXastar, xwarāsān.
PHD.txt:3890:sunrise xwarāsān.
PHD_mackenzie.txt:5623:xwarasan [hwPs'n'  '      I M xwr)s)n, N .......] sunrise, east.
PHD_mackenzie.txt:11993:xwarasan                 ,~"'"         uzdcsparist     \~~~
=== NYB
=== KNT as-
373:s in asa- from Ё if it means ‘stone’. Sikayawati$, a Median fortress, with s- from
497:090: DB 1.65 and other forms of the same word; so always in DB, but við- in other inscriptions. У ištās-pa -pam -pahyd, always in DB, in some DS inscriptions, and in those of Artaxerxes II and
588:arasam impf. of pres. stem rasa- (-sa- from *-ske-),
1101:OP Casa-, from Elam. fu-ía-an, whence also Akk. Su-Sa-an.
1153:possibly in Asa-garta- (see Lex. s.v.). Cf. also aec. asmdnam ‘sky’, Av. asman- ‘sky, stone’,
1192:pIE *efuo- ‘horse’, OP asa- in aec. asam and in аѕађата-; OP aspa- (with Med. sp) in waspa-, Aspacanah-, Vistaspa-; Av. aspa-, Skt. бра, Lt. equos.
1304:pIE *qek-s-, probably in OP caSa-m ‘eye’, cf. Av. cašman- ‘eye’, Skt. cdksus- ‘eye’ (see Lex. s.v. casa-).
1330:cf. Av. paséa, Skt. pased. The evidence of Sasa- nian Pahlavi shows that this value alone is pho- netic in OP (Bv. Gr. §114), and that the -&- which is seen in some sandhi combinations, be- longs rather to Median: OP kaSevy ‘anyone’ from pIE *q*0s-q*id; manaš-clä] DNb 32 from *menos-
1524:*bher- ‘bear’ in bara*tiy ‘they bear’; *bhor- in aršti-bara ‘spear-bearer’; *bhr- in u-bar-tam ‘well uplifted’; *bhór- in asa-büra- ‘horse-borne’, uSa-büri- ‘camel-borne’.
1545:(д) long grade in substantives from the verbal root: asa-bdra-, u$a-büri-; u-céram, bajt-.
1566:wvüsabüra ‘good horseman’ (*hv-dsa-), to asa- ‘horse’; asabaéra with d is rendered probable by the unlengthened vowel in uSabart- ‘camel- borne’.
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
1758:-a- stems: frasa-, spaümaida-, Ainaira-, Auliydra-,
1776:І. Attached to a verbal root, the ablaut grade of the root varying: kara- in compounds, u-céra-, küma-, Катёа-, gausa-, raga-, adv. daríam, drauga-, baga-, bara- and bāra- in compounds, zana- in compounds; less certain formations in d-baha- in daha-vaja, casa-, U-t&na-, u-tava-, gara- in batu-gara-, Vi-vdna-, varga- in hauma-varga-.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1786:Passives: ha™-dugd- ‘im-pressed’ = ‘inscription’; pati-kara- ‘made thereto’ = ‘sculptured figure’; asa-bara- ‘horse-borne’.
1788:VI. The vocalism of the root varies in these for- mations, being either -a- (pIE -e- or -о- or -a-), as in baga-, bara-, daiva-; or à zero grade, as in karša-, u-zma-, darga- (see Lex. s.vv.); or a vriddhied or lengthened grade (§126), as in kdma-, asa-bāra-, Margava-.
1805:Expressing place: apa-dd-na-, daiva-di-na-, à- yada-na-, fem. us-tasa-nd-, d-vaha-na-, std-na-, varda-na-.
1877:Only compounds of stem + stem will be here discussed. Either stem may itself be a compound; either stem may already have one or more suffixes. The initial syllable of the first element, especially in adjectives, may show vriddhi or lengthening of the vowel, as in dáraniya-kara- ‘gold-worker’ to daranzya- ‘gold’; less often this appears in the sec- ond part, as in Baga-yadi- 'god-worshipping (month)’, where it is seen in both parts, and in asa-bàra- ‘horse-borne’, where it indicates passive meaning.
1881:Derivative adjectives to compounds may be made by the addition of suffixes; Haxamanis-iya- ‘Achaemenian’ to Hazámanis-, Asagart-iya- ‘Sa- gartian’ to Asa-garia-.
```


## [2026-09-07T18:24:44.872Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT come\" && grep -n \"‘come’\\|'come'\\|to come\" KNT.txt | head -15; echo; echo \"=== SOD as- come\" && grep -n \"آمدن\" SOD.txt | head -10",
 "description": "Kent verbs for come; Sogdian"
}
```


### [2026-09-07T18:24:44.931Z] TOOL RESULT

```
=== KNT come
346:I. Persian, the national language of Persia to this day, spoken in numerous varying dialects throughout the empire; some of the aberrant di- alects may go back to different dialects of an- tiquity, but the language as a whole seems to come from the general types of the Old Persian and the Avestan. The most highly esteemed literary Persian is the dialect of Shiraz.
407:aniyüha bagüha ‘the other gods’, with double endings (like Vedic Skt. devásas for devás) seems to come from the language of religion, for a normal OP aniyaiy bagd (pl. Бада happens not to occur).
962:*guin-tu- ‘place’, OP gàtu-, Skt. gätú- to the root *gvem- ‘come’.
1530:*g¥em- ‘come’ in -jamiy ‘may it come’, *g*m- in pardgmata ‘gone forth’ (see $244).
4890:hered to Phraortes, declared himself King in Sagartia, a distriet of northern Media; he claimed to be of the family of Cyaxares. Darius sent а force of Medes and Persians under Takhmaspada, a Median officer, who defeated and captured Cicantakhma, bringing him to Darius. Darius mu- tilated him and put him to death with torture, at Arbela ($33). Thus ended rebellion in Media (884) ; but there was still a strong rebel force in Armenia, against which Darius sent an Armenian officer named Dadarshi. Dadarshi, thrice attacked by the rebels, defeated them successively at Zuzaya on II 8 (§26), at Tigra on II 18 (§27), and at Uyama on III 9, whereafter he waited for Darius to come and make final governmental dispositions (828). This third battle by Dadarshi was only nine days after Vaumisa in а second engagement beat off the other force of Armenian rebels in the dis- trict of Autiyara, on IT 30; after which he also awaited Darius’s arrival (530). There was по fur- ther fighting in Armenia.
5029:à + ay- ‘come’: aya"là 3d pl. imf. mid. ($181, $208) DZe 11.
5354:(JNES 4.49-50): Av. gdtav- дабш-, NPers. gah, Skt. gütu-, to pAr. root gam-, pIE *g*em- ‘come’ ($68, $81, $158.11, §179.n2). давит asm. DNa 41f. дйбарй lsm. ($137, $182.IT) DB 1.62f, 66, 69; DNa 36; DNb 35 (INES 4.49-50); DSe 36f, 44, 44f; XPf 33 (as abl., $182.III, though without hacé: Lg. 941-6; Ву. BSLP 33.2.148-50; Wb. А 41.319-20; Sehaeder, SbPAW 1935.503; Hz. AMI 4.130-2, 8.45, ApI 177-80), 85; XPh 34.
5360:gam- vb. ‘come’: Av. gam-, Skt. gam-, Gk. Ваши, Lt. venió, Gt. qiman, pIE g*em- ($101, $244). See also gdéu-.
5361:à + gam- ‘come’: бјата opt. (Skt. gamyat; §67.1, §101, $122, $132.2, $218.11, $293.I, §228.IT) DPd 19.

=== SOD as- come
```


## [2026-09-07T18:24:47.979Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN asidan/khorasan\" && grep -n -i \"khorasan\\|churāsān\\|chorasan\\|hurāsān\" HRN.txt HUB.txt | head -10; echo \"=== NYB as\" && grep -n \"xvarāsān\\|khurāsān\\|hwrʾsʾn\\|xwrʾsʾn\" NYB_vol2_glossary.txt NYB_vol1.txt | head",
 "description": "Horn/Hübschmann/Nyberg for Khorasan"
}
```


### [2026-09-07T18:24:48.047Z] TOOL RESULT

```
=== HRN asidan/khorasan
HUB.txt:8874:und Margrot (als Distrikte von Chorasan) bei Sebeos p. 67
=== NYB as
```


## [2026-09-07T18:24:57.308Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اسیدن\\|آسـید\\|آسان\\b\" incoming/FFD/FFD_pages.txt | head -10; echo \"=== FFD file size\"; wc -l incoming/FFD/FFD_pages.txt; echo \"=== search آس\"; grep -n \"^\\s*آس\" incoming/FFD/FFD_pages.txt | head -20",
 "description": "Grep FFD for asidan"
}
```


### [2026-09-07T18:24:57.361Z] TOOL RESULT

```
1290:‏به 9 بدل و در 5 ادغام شده است. «هراسیدن» هم از 158 آمده است. -> هراسیدن.
2185:۱ هراسیدن
=== FFD file size
3193 incoming/FFD/FFD_pages.txt
=== search آس
706:آسودن
707:آسود + فارسی میانه 3800.
708:آسای + فارسی میانه 3837.
```


## [2026-09-07T18:24:59.485Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D8%B3%DB%8C%D8%AF%D9%86/",
 "prompt": "What does آسیدن mean in Persian dictionaries (Dehkhoda/Mo'in)? Quote the definition and any etymological note or example verse."
}
```


### [2026-09-07T18:25:02.254Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T18:25:07.707Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.vajehyab.com/?q=%D8%A2%D8%B3%DB%8C%D8%AF%D9%86",
 "prompt": "What do Persian dictionaries (Dehkhoda, Mo'in, Amid) say about آسیدن? Quote definitions and any example verse."
}
```


## [2026-09-07T18:25:08.588Z] TOOL CALL #52: WebSearch

```json
{
 "query": "\"آسیدن\" دهخدا معنی آمدن رسیدن خورآسد ویس و رامین"
}
```


### [2026-09-07T18:25:12.397Z] TOOL RESULT

```
Based on the webpage content provided, I cannot find direct definitions of آسیدن from the major Persian dictionaries you mentioned (Dehkhoda, Mo'in, Amid).

The page shows search results for آسیدن, but the actual dictionary entries from these sources are not displayed. The content includes related terms like:

- اسیدنیتریک (nitric acid) from Amid dictionary
- اِسّادَن from Bakhtiari dialect, meaning "گرفتن، ستدن" (to take, to hit)
- ترسیدن from the spectral dictionary, which includes "اسیدن، وحشت کردن" (fear, terror)

However, these are tangential results rather than direct definitions of آسیدن itself. No example verses are quoted on this search results page.

To find the actual definitions from Dehkhoda, Mo'in, and Amid dictionaries, you would need to access their complete entries directly.
```


### [2026-09-07T18:25:17.766Z] TOOL RESULT

```
Web search results for query: ""آسیدن" دهخدا معنی آمدن رسیدن خورآسد ویس و رامین"

Links: [{"title":"معنی رسیدن | لغت‌نامه دهخدا","url":"http://www.vajehyab.com/dehkhoda/رسیدن"},{"title":"معنی شدن | لغت‌نامه دهخدا","url":"https://vajehyab.com/dehkhoda/%D8%B4%D8%AF%D9%86-4"},{"title":"معنی رسیدن | لغت‌نامه دهخدا | واژه یاب","url":"https://vajehyab.com/dehkhoda/%D8%B1%D8%B3%DB%8C%D8%AF%D9%86-2"},{"title":"رسیدن | در فرهنگ لغات ها (دهخدا،معین و ... ) + سایر منابع اطلاعاتی | جدول یاب","url":"https://www.jadvalyab.ir/fa2fa/%D8%B1%D8%B3%DB%8C%D8%AF%D9%86"},{"title":"معنی راه آمدن - لغت‌نامه دهخدا","url":"https://lamtakam.com/dictionaries/dehkhoda/294696/%D8%B1%D8%A7%D9%87++%D8%A2%D9%85%D8%AF%D9%86"},{"title":"معنی رسیدن - لغت‌نامه دهخدا","url":"https://lamtakam.com/dictionaries/dehkhoda/298184/رسیدن+"},{"title":"معنی کار به جان رسیدن - لغت‌نامه دهخدا","url":"https://lamtakam.com/dictionaries/dehkhoda/394581/%DA%A9%D8%A7%D8%B1+%D8%A8%D9%87++%D8%AC%D8%A7%D9%86++%D8%B1%D8%B3%DB%8C%D8%AF%D9%86"},{"title":"معنی خدمت رسیدن - لغت‌نامه دهخدا","url":"https://lamtakam.com/dictionaries/dehkhoda/263673/%D8%AE%D8%AF%D9%85%D8%AA++%D8%B1%D8%B3%DB%8C%D8%AF%D9%86"},{"title":"معنی آمد و نیامد داشتن - لغت‌نامه دهخدا","url":"https://lamtakam.com/dictionaries/dehkhoda/3624/%D8%A2%D9%85%D8%AF+%D9%88+%D9%86%DB%8C%D8%A7%D9%85%D8%AF+%D8%AF%D8%A7%D8%B4%D8%AA%D9%86"}]

I searched for information about "آسیدن" and related terms from Dehkhoda Dictionary. However, the search results primarily returned information about "رسیدن" (residen) rather than "آسیدن" (asidenI couldn't find specific results for "آسیدن" in the Dehkhoda Dictionary from these search results. The results mainly showed definitions for related words like "رسیدن" (to arrive/reach) and "آمدن" (to come).

Let me search more specifically for "آسیدن" from the Dehkhoda Dictionary:

Links: [{"title":"درگاه:خراسان/مقدمه - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%AF%D8%B1%DA%AF%D8%A7%D9%87:%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86/%D9%85%D9%82%D8%AF%D9%85%D9%87"},{"title":"معنی آسودن","url":"https://dehkhoda.ut.ac.ir/fa/dictionary/1564/%D8%A2%D8%B3%D9%88%D8%AF%D9%86"},{"title":"درگاه:خراسان - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%AF%D8%B1%DA%AF%D8%A7%D9%87:%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86"},{"title":"اساییدن - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/اساییدن/"},{"title":"ساییدن - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%B3%D8%A7%DB%8C%DB%8C%D8%AF%D9%86/"},{"title":"معنی اشنیدن | لغت‌نامه دهخدا | واژه یاب","url":"https://vajehyab.com/dehkhoda/%D8%A7%D8%B4%D9%86%DB%8C%D8%AF%D9%86"},{"title":"معنی آسودن | لغت‌نامه دهخدا","url":"https://www.vajehyab.com/dehkhoda/%D8%A2%D8%B3%D9%88%D8%AF%D9%86"},{"title":"عصیان - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%B9%D8%B5%DB%8C%D8%A7%D9%86/"},{"title":"معنی گزیدن | لغت‌نامه دهخدا","url":"http://www.vajehyab.com/dehkhoda/گزیدن-2"},{"title":"آسودن | در فرهنگ لغات ها (دهخدا،معین و ... ) + سایر منابع اطلاعاتی | جدول یاب","url":"https://www.jadvalyab.ir/fa2fa/%D8%A2%D8%B3%D9%88%D8%AF%D9%86"}]

Perfect! I found the information about "آسیدن". Based on the search results:

According to Dehkhoda Dictionary, "آسیدن" (asiden) is an infinitive that means "آمدن، رسیدن" (to come, to arrive/reach). This is an old Persian verb that is historically documented in etymological references for compound words like "خراسان" (Khorasan), where it forms part of the meaning as "coming/arriving."

The word "آسیدن" is a classical Persian verb that's not commonly used in modern Persian, but it appears in historical and etymological contexts within Persian dictionaries and scholarly references.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T18:25:21.783Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://dehkhoda.ut.ac.ir/fa/dictionary/search?q=%D8%A2%D8%B3%DB%8C%D8%AF%D9%86",
 "prompt": "Find the Dehkhoda entry for آسیدن. Quote its definition and any cited verse."
}
```


## [2026-09-07T18:25:23.052Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/khorasan-i-geography",
 "prompt": "What does Encyclopaedia Iranica say about the etymology of the name Khorasan (Middle Persian xwarāsān)? Quote the analysis of the components."
}
```


### [2026-09-07T18:25:24.579Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:25:28.469Z] TOOL RESULT

```
# Response

I cannot find the Dehkhoda entry for "آسیدن" (āsīdan) in the provided web page content. 

The page shows a search results screen indicating "نتیجه‌ای یافت نشد" (no results found) for the term "search." The content provided is primarily the website's navigation menu, accessibility settings panel, and footer information from the Dehkhoda Dictionary website, rather than actual dictionary entry definitions.

To locate the entry for آسیدن, you would need to perform a new search directly on the Dehkhoda Dictionary's search interface at https://dehkhoda.ut.ac.ir/fa/dictionary.
```


## [2026-09-07T18:25:43.175Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C4%81sati",
 "prompt": "Does this page exist? What Proto-Iranian verb 'to come' is reconstructed and what are its descendants (Parthian, Sogdian, Balochi, Middle Persian)?"
}
```


## [2026-09-07T18:25:43.621Z] TOOL CALL #56: WebSearch

```json
{
 "query": "Sogdian \"ʾʾs-\" \"to come\" Parthian \"as-\" Proto-Iranian \"*ā-sad-\" PIE *sed- Khorasan āsān etymology Hasandust"
}
```


### [2026-09-07T18:25:44.499Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:25:54.111Z] TOOL RESULT

```
Web search results for query: "Sogdian "ʾʾs-" "to come" Parthian "as-" Proto-Iranian "*ā-sad-" PIE *sed- Khorasan āsān etymology Hasandust"

Links: [{"title":"(PDF) From Middle to New Persian: written materials from Northern Iran and Khorasan","url":"https://www.researchgate.net/publication/353096921_From_Middle_to_New_Persian_written_materials_from_Northern_Iran_and_Khorasan"},{"title":"KHORASAN xix. Linguistic Features of Khorasani Persian - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/khorasan-xix-linguistic-features-of-khorasani-persian/"},{"title":"SOGDIANA i. The Name - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sogdiana-name/"},{"title":"EASTERN IRANIAN LANGUAGES - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/eastern-iranian-languages/"},{"title":"The ethnic and linguistic identity of the Parthians: A review of the evidence from Central Asia 1","url":"https://www.researchgate.net/publication/233373982_The_ethnic_and_linguistic_identity_of_the_Parthians_A_review_of_the_evidence_from_Central_Asia_1"},{"title":"Sogdia","url":"https://en.wikipedia.org/wiki/Sogdia"},{"title":"Iranian peoples - Wikipedia","url":"https://en.wikipedia.org/wiki/Iranian_peoples"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/3402027/concepts"}]

The search results contain a reference to Hasandust's work on Iranian etymology in the context of Khorasan, but don't provide detailed information about the specific linguistic comparison you're asking about. Let me search more specifically for information about the etymology chain you mentioned.

Links: [{"title":"خراسان - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86"},{"title":"Khwarasan","url":"https://en.wikipedia.org/wiki/Khwarasan"},{"title":"KHORASAN xix. Linguistic Features of Khorasani Persian - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/khorasan-xix-linguistic-features-of-khorasani-persian/"},{"title":"Akhshunwar","url":"https://en.wikipedia.org/wiki/Akhshunwar"},{"title":"Okar Research: Word Origins…..-i-stan….-asan….-isan….-ezm...-i-ana....-asam","url":"http://balkhandshambhala.blogspot.com/2013/12/etymology-i-stanasanisanezm.html"},{"title":"Sogdia","url":"https://en.wikipedia.org/wiki/Sogdia"},{"title":"Okar Research: Great Khorasan Road & The Silk Route","url":"http://balkhandshambhala.blogspot.com/2012/10/asia-map.html"},{"title":"Okar Research: Ancient Khorasan: Land Where The Sun Rises (2000 BC)","url":"https://balkhandshambhala.blogspot.com/2012/11/balkh-khorasan.html"},{"title":"Khorasan (disambiguation)","url":"https://en.wikipedia.org/wiki/Khorasan_(disambiguation)"},{"title":"Okar Research: BACTRIA, Tagzig, Khorasan, Paktra, Zariaspa, Vahilka & Shambhala","url":"https://balkhandshambhala.blogspot.com/2012/10/ancient-bactria.html"}]

Based on the search results, I can provide you with information about the etymology of the Khorasan name component:

The name Khwarasan is a combination of khwar (meaning "sun") and āsān (from āyān, literally meaning "to come" or "coming" or "about to come"). This is equivalent to خور (xwar, "sun") + آسان (âsân, "coming"), where آسان (âsân) is the Parthian conjugation.

Regarding the etymological chain you asked about, the search results reference Hasandust (1393) regarding a possible Iranian etymology in the context of written materials from Northern Iran and Khorasan, but the specific details about the Sogdian "ʾʾs-," Proto-Iranian "*ā-sad-," and PIE *sed- connections that you mentioned are not directly available in these search results.

To get more detailed information about Hasandust's specific etymological analysis connecting these forms across Sogdian, Parthian, Proto-Iranian, and PIE levels, you would likely need to consult the primary scholarly work directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T18:26:16.659Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 enek\" && grep -n \"enek\\|ganahs\\|ganôhs\\|nancisci\" incoming/WLD/WLD_Bd1_pages.txt | head -15",
 "description": "Grep Walde-Pokorny Bd I for enek-"
}
```


### [2026-09-07T18:26:16.699Z] TOOL RESULT

```
=== WLD Bd1 enek
10112:zu ai. arndti „erreicht“ als *nk-. s. u. *enek- „reichen“); dagegen ai. cigati
11548:128                                eneuen, neun, enug            — enek-, nek-, enk-, nk-
11604:    enek-, nek-, enk-, nk- „reichen, erreichen, erlangen“ und „tragen“.
11619:         gr. voiles         *enek- noch in di-gvey.gg „durch eine Strecke hindurchreichend
11648:       nactus (und nanctus ) sum, nancisci (arch, auch nancio, -ire) „erlangen“
50208:„genekm sein" der                       u.   angefiihrten          si.   Worter, auch das Bedeutungsver-
72708:dun          bitter",       ursprgl.    .unangenekm   •
```


## [2026-09-07T18:26:18.036Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT bring/enough\" && grep -n \"^bring\\|^enough\\|Bring (1)\\|enough (1)\" SKT.txt | head; echo; grep -n -A6 \"enough,  adj\" SKT.txt | head -20",
 "description": "Grep Skeat for bring and enough"
}
```


### [2026-09-07T18:26:18.093Z] TOOL RESULT

```
=== SKT bring/enough
11592:bring  to  mind  again.    (L. mi  B«-  and  Mind, briongiug  to  me ;  see  ICe. to  excavate ;  set  Menaoe.
12517:bringcr  of  tiding*.      Prob.  for a  bnnger  of  news,  from  nouus^
```


## [2026-09-07T18:26:23.962Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11604,11680p' incoming/WLD/WLD_Bd1_pages.txt",
 "description": "Print Walde-Pokorny enek- entry"
}
```


### [2026-09-07T18:26:24.036Z] TOOL RESULT

```
    enek-, nek-, enk-, nk- „reichen, erreichen, erlangen“ und „tragen“.
      Ai. aepioti, av. asnaoiti „gelangt hin zu etwas, erreiclit“, Pf. ai anqqa
    (idg.      *on-onka,       -e,          = ai. t-anaic „er kam“), s. pi an-agnh (eine neben dem
    ?i<m-Praes. aqnoti stehende ««-Bildung *nk-na-ti sucht Uhlenbeck IF. 25,
    143 in ai. aqnati „iBt“ = *nimmt zu sich“; wegen der dann als urar. Ab-
    lautsneubildung zu fassenden ai. pratar-, sayam-aqa -, av. kahrk-dsa- wohl
    nicht mit Recht,                   s.   Wz. elc „essen“;
         ai.     nagati ,      ai. nalsati „erreicht, erlangt“, Desid. inaksati
                             av.        nasaiti,
    „sucht zu erreichen, strebt zu“ q ga   m. „Anteil“, av. asa- „Partei“, ai.
    nqga- m. „Erlangung“, -nqgana- (Kreuzung von qg- und nag-)-,
      arm. hasanem „komme zu etwas, komme an“ (s. Hiibschmann Arm. Gr. I
    464, Brugge IvZ. 32, 14; wegen der Bed. ganz fraglicli aber arm. anausr
    „rarus“, nach Pedersen KZ. 39, 411 aus *{n jnnku- „weit reichend“  „was                                            —
    weit reichen             soil,      daher diinn gesiit“j;
         gr. voiles         *enek- noch in di-gvey.gg „durch eine Strecke hindurchreichend
    = ununterbrochen“               (att. diavsy.rjg aus
                                                         * dia-gvey.ggl anders Prellwitz und

    und Boisacq s. v.                        nod-gvey.gg        „bis zu den FiiBen herabreichend*',                        Sovq-
yvexys „einen Speerwurf weit“                                =
                                   „soweit man mit einem geschleuderten
Speere   reicht“   oder  pass. „vom   Speer erreicht“,     wie y.evxQgvEy.gg
„vom Stachel ferreicht =) angetrieben“ (z. B. Boisacq 251, Bechtel
Lexil. 104), pass. aor. gveydgv „wurde getragen“, Pf. xax-yvoxa Hes        ev-                                                                 ,

                                                                             2
yvoya (ev- ist darin trotz xar-yvoxa kaum die Praep. ev, Brugmann II
3, 461, sondern wohl Reduplikation    ebenso im    Med.  iv-ijvey/uai, zu
                                                                        ;
                                                                          dem
sich  als 3. sg. ev-yveyaxai statt  *ev-rjvey.xai gesellte nach dem Aor.

eveyy.eTv);         *enk- im red. Aor. ev-eyy.-eiv „tragen“, *onk- in oyxog „Tracht.
Last“.
      tjveiy.a     dagegen Praep. ev + Wz. *seik- „langen“,                s. d. und Boisacq 251 f.

m. Lit,,          Brugmann II 2 3, 92             ;
                                                       durch Ivreuzung mit ihm wurde yveyxov zu
tfveyy.a,         rjveiyxa   ;




       nactus (und nanctus ) sum, nancisci (arch, auch nancio, -ire) „erlangen“
      lat.

(-a- = e s. Giintert Abl. 53, so dafi nactus = germ. nuJi-ta-; die Kasalierung
              ,




des Praes. hat trotz Brugmann IF. 12, 157 Anm. 1 keine Beziehung zur
Wzf, *enk -); air. ro-icc .,erreicht“, do-ice ,,kommt“, air-icc- „finden“, con -
icc- „konnen“ usw., Formenbestand bei Pedersen KG. II 552 ff.           zur Er-                                                       ;



klarung des Vokalismus s. Pokorny IF. 35, 339: in die themat. Konjugation
ubergefuhrtes dehnstufiges *euk-ti, woraus *lnk~, *Tnc-, icc- Yerbalnomina                                               ;



tlchtu, nchtu; s-Konj. -J aus *cnkst    Schwundstufe nk- in cymr. di-anc „ent-
                                                                    ;


fliehen“, cy franc ( *kom-pr\o]nko-) = air. comracc „Zusammentreffen“        fiir                                                              ;



anderes bei Fick II * 31 angereihte vgl. man Pedersen passim (ir. oc,
cymr. icnc, wng „bei“ aus *onko- „erreichend“?)                                                   :
                                                                                                      gall.      Selvanedes „qui ont
obtenu propriety? 11 (Yendryes Msl. 13, 394).
      Got. ganah             (Praet. - Praes.)               „es        reicht       = geniigt“, inf. yanauhan (iiber
```


## [2026-09-07T18:26:24.715Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/enough",
 "prompt": "Give the full etymology of \"enough\": Old English form, Proto-Germanic form, PIE root, and cognates."
}
```


### [2026-09-07T18:26:30.600Z] TOOL RESULT

```
# Etymology of "Enough"

**Old English Form:** _genog_, meaning "sufficient in quantity or number"

**Proto-Germanic Form:** _\*ganog_, "sufficient" (also found in Old Saxon _ginog_, Dutch _genoeg_, German _genug_, Old Norse _gnogr_)

**Structure:** The word comprises two elements:
- First: Old English _ge-_ prefix (equivalent to Latin _com-_ and Modern German _ge-_)
- Second: From PIE _\*nok-_, derived from root _\*nek-_ (2) meaning "to reach, attain"

**PIE Root:** _\*nek-_ (2) "to reach, attain," itself from _\*kom-_ "beside, near, by, with"

**Cognates:** Sanskrit _asnoti_ "to reach," Hittite _ninikzi_ "lifts, raises," Lithuanian _nešti_ "to bear, carry," and Latin _nancisci_ "to obtain"

The word's semantic evolution progressed from an adjective meaning sufficient, to an adverb meaning "sufficiently," eventually gaining the understated sense of "too much" by Old English times.
```


## [2026-09-07T18:26:43.420Z] TOOL CALL #61: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T18:26:43.458Z] TOOL RESULT

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


## [2026-09-07T18:26:44.098Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bring",
 "prompt": "Give the full etymology of \"bring\": Old English form, Proto-Germanic form, PIE root/compound analysis, and cognates."
}
```


### [2026-09-07T18:26:55.723Z] TOOL RESULT

```
# Etymology of "Bring"

**Old English:** *bringan* "to bear, convey, take along in coming; bring forth, produce, present, offer" (past tense *brohte*, past participle *broht*)

**Proto-Germanic:** *\*brangjanan*, which also produced Old Frisian *branga*, Middle Dutch *brenghen*, Old High German *bringan*, German *bringen*, and Gothic *briggan*

**PIE Root:** *\*bhrengk-*, traced to the root "*\*bher-* (1) 'to carry,' also 'to bear children.'" The connection shows that bringing involves the fundamental action of conveyance and generation.

**Cognates:** Welsh *he-brwng* "bring" represents a Celtic cognate, though etymologists note uncertainty about whether this reflects shared Indo-European ancestry or a "Germanic/Celtic substratum word."

The word's strong verb conjugation pattern (like *sing*, *drink*) became established early, with Old English showing rare strong forms like *brungen*, persisting in modern dialectal *brung*.
```


## [2026-09-07T18:27:12.190Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p358hi.png'); w,h=im.size\nc=im.crop((int(0.20*w),int(0.148*h),int(0.45*w),int(0.225*h)))\nc=c.resize((int(c.width*1.6),int(c.height*1.6)))\nc.save('p358_av.png'); print(c.size)\n\"",
 "description": "Crop Avestan box"
}
```


### [2026-09-07T18:27:13.779Z] TOOL RESULT

```
(1699, 676)
```


## [2026-09-07T18:27:13.966Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC nek\" && grep -n \"enek\\|^nek-\\|nekō\\|nek-, nk-\" IEC.txt | head -10; echo \"=== ARY latin index NEK\" && grep -n -i \"^NEK\\|NEK-\\|ENEK\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Mann and Aryanpur"
}
```


### [2026-09-07T18:27:14.026Z] TOOL RESULT

```
=== IEC nek
6203:Skt. cf. matrkah; Av. vorozika- (vorozo); Gk. statikós (stásis), kunikós (kuon); Lat. müricus (mūs), canticus (cantus); Osc. tüvtiks, toutico- (touto); Br. groenek (groen); W boneddig (bo-
10936:mnis, mniuo (1) Cf. monuos (minuos). WP II, 267 Skt. cf. minah (a fish); Gk. mainís, f. ‘sprat’; maíné, id.; OHG muniwa, f. ‘minnow’; OE myne, id.; E minnow, and dial. minny, id.; Fris. mûne, Du. meun, m. wd: WG Münne, f. ‘chub’; Cz. cf. meii, m. ‘chub’; Slovak men, s. ‘tadpole’; cf. Slovene dim. type menek, id.
11135:beside G mannig — in mannig-faltig *mani- fol)”, id.; Sw. mánge, många, mången, id.; OCS münogo, mnogo, prn., mnogü, adj. id.; Finn. LW moni, id. beside monikko, s. *plu- ral; menekki "a good sale, demand Cf. a variant of type *menighs-, meniks- in Ir. me- nicc ‘frequent’; W mynych, adv. ‘often’. Ver- bal type (monoghið) in Go. managjan “in- crease’: OCS množiti, id.
11603:nek- ‘negation, not-?. Lat. ambig., cf. neko, nekus Lat. (?) neco, are, pf. -ui (kil. Semantics of Li. naikinti «destroy'?, but see below: neK-); W neg, pl. ion, m. “barrier, frustration"; negio, inf. ‘frustrate’; Big. nekam, v. “say no; deny
11609:nek- — nëm-
=== ARY latin index NEK
14484:NEKROS, NEKUS — (GREEK) gly NASA (PAHLAVI) 5 ay
```


## [2026-09-07T18:27:16.837Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p358_av.png"
}
```


### [2026-09-07T18:27:16.859Z] TOOL RESULT

```

```


## [2026-09-07T18:27:26.156Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ne%E1%B8%B1-",
 "prompt": "Does a Wiktionary reconstruction page exist for the PIE root meaning 'to reach, attain' (h₂nek̑-)? Give the reconstructed form, meaning, and descendants (Avestan, Sanskrit, Gothic, Greek, Latin)."
}
```


## [2026-09-07T18:27:27.034Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gan%C3%B3hs",
 "prompt": "Give the Gothic entry ganōhs: meaning and etymology (Proto-Germanic form, PIE root)."
}
```


### [2026-09-07T18:27:29.213Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:27:31.762Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂neḱ-

Yes, a Wiktionary reconstruction page exists for this root.

**Reconstructed Form:** *h₂neḱ- (perfective)

**Meaning:** "to reach, to attain"

**Key Descendants:**

- **Sanskrit:** आनट् (ā́naṭ) and आष्ट (ā́ṣṭa); अश्नोति (aśnóti)
- **Avestan:** ašnaoiti; asnāt̰ (Old Avestan); asne (Younger Avestan)
- **Latin:** nancīscor ("to meet with")
- **Ancient Greek:** ἀνάγκη (anánkē)
- **Proto-Germanic:** *nēhwaz and *ganōgaz (with further Gothic and other Germanic descendants)
- **Celtic:** Old Irish éicen/écen; Welsh angen

The page notes this root was "conflated with *h₁neḱ-" in earlier scholarship, though they represent distinct etymological sources.
```


## [2026-09-07T18:27:40.707Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ne%E1%B8%B1-",
 "prompt": "Does a page exist for *h₁neḱ-? Give the reconstructed form, meaning ('to carry'?), descendants (Avestan nāš-, Greek, Balto-Slavic), and any note about conflation with *h₂neḱ-."
}
```


### [2026-09-07T18:27:46.749Z] TOOL RESULT

```
# Response: *h₁neḱ- Root Entry

Yes, a page exists for this reconstructed Proto-Indo-European root. Here are the key details:

**Reconstructed Form:** *h₁neḱ-

**Meaning:** The root means "to receive, take away" rather than 'to carry'. 

**Descendants:** The page documents several descendant forms across language families:
- Ancient Greek: ἐνεγκεῖν (enenkeîn) and related forms
- Balto-Slavic: Proto-Balto-Slavic *neśtei and Proto-Slavic *nosìti
- Proto-Germanic: *bringaną ("to bring")
- Hittite: 𒈾𒀝𒆠𒅖 (nakkis, "important, powerful")

**Note on Conflation:** The page explicitly states that this root was "Conflated with *h₂neḱ- ('to reach, attain') by Pokorny," distinguishing between the two roots' original meanings despite their historical merger in scholarly analysis.
```


## [2026-09-07T18:28:02.285Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂neḱ-' --note 'page 358, root Neku/Nek 2/Enek: PIE *h2nek- \"to reach, attain\", Av. asnaoiti, PGmc *ganogaz > enough' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁neḱ-' --note 'page 358: PIE *h1nek- \"to receive, take away\" (Gk enenkein, BSl nesti, PGmc *bringana); Wiktionary notes Pokorny conflated it with *h2nek-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86' --note 'page 358 node 3, asidan: Khorasan = xwar \"sun\" + asan \"coming\", Parthian verb, cf. Balochi asag' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/enough' --note 'page 358 node 5: OE genog < PGmc *ganog < PIE *nok- of *nek-(2) \"to reach\"' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/bring' --note 'page 358 node 7: OE bringan < PGmc *brangjanan < PIE *bhrengk- from *bher-(1)' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-07T18:28:05.303Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/16290256b4db4250.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fbb8a2ac7621e0eb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/334dc2fc4f3fc592.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cbdc9a20237289d1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a710d683c61cfe1c.txt
```


## [2026-09-07T18:28:09.656Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg358.png data/verification/sources/refs/ocr/BOOK/358.png && ls -la data/verification/sources/refs/ocr/BOOK/358.png",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-07T18:28:09.731Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 49496 Sep  7 14:28 data/verification/sources/refs/ocr/BOOK/358.png
```


## [2026-09-07T18:29:06.150Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK bring context\" && sed -n '2425,2445p' POK_01.txt; echo \"=== leaf\"; awk 'NR<=2436{n+=gsub(/\\f/,\"\")} END{print n}' POK_01.txt",
 "description": "Pokorny bher- + enek- contamination note"
}
```


## [2026-09-07T18:29:07.572Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bring,  tr\\.\" KLN_1966.txt | head -3; echo \"---\"; grep -n -o \"bring,  tr\\..\\{0,700\\}\" KLN_1966.txt | head -2",
 "description": "Klein s.v. bring"
}
```


### [2026-09-07T18:29:07.620Z] TOOL RESULT

```
=== POK bring context
lit.  brestu,  brendau,  bresti  , aufquellen,  reifen',  Partiz.  brendp  ,reif', h^stu,  brindau,  bristi  .quellen  (z.  B.  von  Erbsen)',  brandä  , Reife,  Erntesegen',
168  •
brandüs   ,körnig';   lett.    hriestu,    hrie£u,    briest    ,quellen,   schwellen,  reiferi^ brud^s    jdick,    stark';    apr.    pobrendints    ,beschwert',    sen    brendekermm »schwanger',  d.  i.  ,mit  Fruchtleib*;
slav.  *bred^  in  a^cech.  ja-bfadek,  sn^oln.  ja-brzqd  , Zweig  des  Weinstocl (daneben  ein  verschied,  slav.  *bred^  in  kaäub.  brod  , Obstbaum');
Beziehung  zu  bher-  (bliren-)  »hervorstehen'  ist  durchaus  annehmbar;
toch.  A  pratsakj  B  pratsäk-  .Brust'.
WP.  II  205,  Trautmann  35  f.,  Van  Windekens  Lexique  99.
bhrenk-,  hhronk-  ,bringen'.
Cymr,  he-bricng  »bringen,  gleiten,  führen'  (*8em-bronk-),  hebryngic , Führer',  acorn.  hebrenchiat  ,dux',  mcorn.  hem-bronk  ,wird  führen',  hm brynkys,  hom-bronkys  »geführt*,  mbret.  ham-brouCj  nbr.  am-brouk  , führen^
got.   briggan,    brähta^    ahd.   bringan,  brälita,   ebenso   as.  (wo  auch  bn gian),   ags.  bringan  und   breng{e)an  Prät.  brühte  (aus  *branhta)  »bringen^
toch.  B  prahk-,  AB  'pränk-  »entfernen'.
Angebl.  aus  den  Wz.  bher-  und  enek-  kontaminiert;  zuletzt  E.  Fraenke KZ.  58,  286^ f.;  63,  198.
WP.  II  204,  Lewis-Pedersen  40,  Feist  105,  Van  Windekens  Lexique  99]
bhre{n)k-  _,zu  Falle  kommen^?
Ai.  bhrdm§atej  bhrasyate  ,^dX\i,  stürzt^^  Partiz.  bhrastd-hj  bkrarhia-i jFall,  Verlust^^  aber  im  RV.  nur  von  nasalloser  Basis  bhräSdyan  (Kaus.), mä  bhrasat  (Aor.)^  dni-bhfsta-h  ^nicht  erliegend^;  also  bh'amSa-  mit  ursprgl. bloß  präsentischer^  dann  weiter  gewucherter  Nasalierung?  oder  alte Doppelformen?  Air.  brec  ;,Lüge'^  (Hhrenka)  ist  der  ßed.  halber  nicht  so sicher  mit  ai.  bhramSa-h  zu  vergleichen;,  daß  es  in  letzterem  Sinne  ent- schiede.
Kuiper  (Nasalpräs.  141  f.)  setzt  *bhrek-mi  neben  *bhre'n-kö  an;  seine^ etymologischen  Vergleiche  sind  jedoch  nicht   überzeugend.    Zu  1.  bhreg-7-
WP.  II  204.
hhren-to-s  ^Geweihträger,  Hirsche
Messap.  ßgsvöov  (aus  ^ßgevrov)  .sXacpov'  Hes.^  ßgevciov  .Hirsclikopf  Hes., brunda  ds.^»  Kurzform  (neben  Brenda)  zum  ON  Brundisium^  älter  BosYti- üiov  .Brindisi',  illyr.  VN  Bqsvtioi]  ven.  FIN  Brinta  ,Brenta';  noch  heute in  ital.  Berg-  und  Pflanzennamen  (Bertoldi  IF.  52,  206 f.);  vgl.  dazu  alb. brl,  brtni  ,Horn,  Geweih^  {Hhf-no-),  Plur.  ^eg.  bHena-^  raetorom.  brenta ;Tragkorb^;
nschwed.  dial.  bHnd{e),  norw.  (mit  g  aus  d)  bringe  .männliches  Elen- tier' i^bhrentös),  ablaut.  norw.  brund  .Männchen  vom  Renntier'  (Hhnitös)]
169
=== leaf
178
```


### [2026-09-07T18:29:08.815Z] TOOL RESULT

```
5661:Derivatives:  brine,  tr.  v.,  brin-er ,  n. bring,  tr.  v.  —  ME.  bringen,  fr.  OE.  bringan,  rel. to  OS.  brengjan,  OFris.  brenga,  MDu.  brenghen, Du.  brengen,  OHG.  bringan,  MHG.,  G.  bringen, Goth,  briggan,  fr.  Teut.  base  *bhrenk-.  Outside Teut.  cp.  W.  he-brnwg,  ‘to  send’,  MCo.  hem- bronk.  ‘we  lead’.
---
5661:bring,  tr.  v.  —  ME.  bringen,  fr.  OE.  bringan,  rel. to  OS.  brengjan,  OFris.  brenga,  MDu.  brenghen, Du.  brengen,  OHG.  bringan,  MHG.,  G.  bringen, Goth,  briggan,  fr.  Teut.  base  *bhrenk-.  Outside Teut.  cp.  W.  he-brnwg,  ‘to  send’,  MCo.  hem- bronk.  ‘we  lead’.
```


## [2026-09-07T18:29:32.187Z] AGENT

Now I'll write the verification file.


## [2026-09-07T18:34:32.095Z] TOOL CALL #73: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk358.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE2 = W + \"Reconstruction:Proto-Indo-European/h₂neḱ-\"\nPIE1 = W + \"Reconstruction:Proto-Indo-European/h₁neḱ-\"\nKHOR = W + \"%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86\"\nETY_EN = \"https://www.etymonline.com/word/enough\"\nETY_BR = \"https://www.etymonline.com/word/bring\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"Neku, Nokut, Nek 2, Nk, Enek, Enk\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *h₂neḱ- 'to reach, attain' (Pokorny's eneǩ-, neǩ-, enǩ-, n̥ǩ- 'reichen, erreichen, erlangen' und [nur Gr. Bsl.] 'tragen', IEW 316–319)\",\n \"verdict_detail\": \"root and gloss right; two of the six headword spellings are Nourai's own and the 'carry' sense now belongs to a separate root\",\n \"note\": (\"Pokorny IEW 316 heads the entry exactly 'eneǩ-, neǩ-, enǩ-, n̥ǩ- ‚reichen, erreichen, \"\n   \"erlangen‘ und (nur Gr. Bsl.) ‚tragen‘; onko-s ‚Tracht, Anteil‘', so Nourai's four forms Nek 2 / Nk / Enek / Enk \"\n   \"and his gloss 'to reach, arrive, carry' reproduce Pokorny (and Klein p.524 'I.-E. base *enek-, *nek-, *nk-, \"\n   \"‘to reach, attain, carry’') faithfully; the language label 'Indo-European' is right. Two problems. (1) 'Neku' and \"\n   \"'Nokut' are not reconstructions any standard work knows: they look like Nourai's own abstractions from the nu-present \"\n   \"*n̥ǩ-neu- (Skt. aśnóti, Av. ašnaoiti) and from Pokorny's remark that Lat. nactus = Gmc. *nuh-ta-. They are also \"\n   \"confusing, because *nekʷ- / *nekʷt- 'night' — which Nourai files on this very page as the two redirect boxes \"\n   \"'Nekw → Noktis' and 'Nekwt → Noktis' — is an entirely different root. (2) Current reconstruction (LIV 282f., \"\n   \"Wiktionary) splits what Pokorny lumped: *h₂neḱ- 'to reach, attain' (Skt. aśnóti, Av. ašnaoiti, Gmc. *ganōgaz > \"\n   \"enough, Lat. nanciscor) versus *h₁neḱ- 'to receive, take away' (Gk. ἐνεγκεῖν, Balto-Slavic *neśtei, Gmc. \"\n   \"*bringaną, Hitt. nakkiš). Nourai's single root box therefore covers two roots on the modern view; the arrows he \"\n   \"draws from it (enough on the one side, bring and Av. nāš- 'carry' on the other) fall on opposite sides of that split.\"),\n \"note_fa\": (\"ریشه در پوکورنی (صفحهٔ ۳۱۶ کتاب IEW) به صورت enek̑-, nek̑-, enk̑-, n̥k̑- با معنای «رسیدن، دست‌یافتن، \"\n   \"به‌دست‌آوردن» و (تنها در یونانی و بالتی‌اسلاوی) «بردن، حمل‌کردن» آمده است؛ کلاین (ص ۵۲۴) و واتکینز (AHD ذیل nek-2) نیز \"\n   \"همین را می‌گویند. پس چهار صورت «Nek 2»، «Nk»، «Enek» و «Enk» و نیز برچسب زبانی «هندواروپایی» و معنای ریشه درست است. \"\n   \"اما دو صورت «Neku» و «Nokut» در هیچ منبع معیاری نیست و پیداست که ساختهٔ خودِ نورایی است: نخستی از ستاک حاضرِ \"\n   \"*n̥k̑-neu- (سنسکریت aśnóti، اوستایی ašnaoiti) و دومی از یادداشت پوکورنی که لاتینی nactus برابر ژرمنی *nuh-ta- است. \"\n   \"این دو صورت گمراه‌کننده هم هستند، زیرا *nekʷ- و *nekʷt- «شب» ریشهٔ دیگری است و نورایی خود در همین صفحه آن دو را \"\n   \"با ارجاع به Noktis آورده است. افزون بر این، ریشه‌شناسی امروزی (LIV و ویکی‌واژه) آنچه پوکورنی یکی گرفته بود به دو ریشهٔ \"\n   \"همنام می‌شکند: *h₂neḱ- «رسیدن، دست‌یافتن» و *h₁neḱ- «گرفتن، بردن»؛ بنابراین «enough» به ریشهٔ نخست و «bring» و \"\n   \"اوستایی nāš- «بردن» به ریشهٔ دوم می‌رسند. نتیجه: ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [PIE2, PIE1],\n \"ref_check\": [\n   {\"ref\": \"POK:316\", \"status\": \"supports\",\n    \"note\": (\"POK_01.txt line 4681 (leaf ~329, printed p.316; the page markers 317 and 318 fall inside the entry and the \"\n      \"preceding entry closes with 'Page(s): 315-316'): 'enek-, nek-, enk-, nk- ‚reichen, erreichen, erlangen‘ und \"\n      \"(nur Gr. Bsl.) ‚tragen‘; onko-s ‚Tracht, Anteil‘.' — Nourai's four core forms and his whole gloss, on the page he cites.\")},\n   {\"ref\": \"KLN:524\", \"status\": \"supports\",\n    \"note\": (\"KLN_1966.txt line 13221 s.v. 'enough': '… fr. I.-E. base *enek-, *nek-, *nk-, ‘to reach, attain, carry’, \"\n      \"whence also OI. asnati, Avestic ashnaoiti, ‘reaches, arrives at’, OI. nasati, Avestic nasaiti, ‘reaches’, OI. \"\n      \"amsah, ‘portion, part’, Avestic qsa-, ‘party’ … Goth. ganohs, ‘enough’.' Klein's article is the direct model \"\n      \"for this whole chart.\")}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.128 (WLD_Bd1_pages.txt line 11604)\", \"stance\": \"supports\",\n    \"note\": \"'enek-, nek-, enk-, nk- ‚reichen, erreichen, erlangen‘ und ‚tragen‘.' — same four variants and same double gloss as Pokorny; Buck's and Klein's page reference (Walde-P. 1.128 f.) points here.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. 'nek-²' (AHD_watkins1985.txt line 776)\", \"stance\": \"supports\",\n    \"note\": \"'nek-². To reach, attain. I. O-grade form *nok- in Germanic *ga-nah- … forming *ganōga-, sufficient … ENOUGH. II. Variant form *enk-. 1. Reduplicated in Greek enenkein, to carry … 2. Compound root *bhrenk- (see bher-¹). [Pok. enek- 316.]' — exactly Nourai's two Germanic branches, and the same Pokorny page.\"},\n   {\"src\": \"IEC\", \"where\": \"IEC.txt (grep 'enek', 'nek-')\", \"stance\": \"silent\",\n    \"note\": \"Mann's only nek- headword (line 11603) is 'nek- ‚negation, not‘' (Lat. neco etc.); he has no entry for the 'reach, attain' root, so Mann is silent on this family.\"}],\n \"nodes\": []\n}\n\nn1 = {\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"nas 2; naš; nasaiti; fra-nâš; ašnaoti; asa 2\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": (\"Five of the six forms are exactly what Bartholomae and Buck have. (a) 'nas 2' = Bartholomae's ²nas- \"\n   \"'hingelangen zu —' (AiW col. 1055f.), deliberately numbered 2 because ¹nas- means 'verschwinden, to perish' — the \"\n   \"numbering is correct and important. (b) 'nasaiti' is its 3sg., Bartholomae's s-aorist/present material s.v. ²nas- \"\n   \"('erlangen, erreichen'), matching Skt. náśati. (c) 'naš' = Av. nāš- 'tragen, to carry', an s-extension of the same \"\n   \"base: BRT col. 1067 heads 'j., g. nāš- V. ‚tragen‘. Praes. 1 nāš-, 30 (Iter.) nāšaya-' and links it to Lith. nešti, \"\n   \"OCS nesti — i.e. Pokorny's '(nur Gr. Bsl.) tragen' wing. (d) 'fra-nâš' is the same verb with the preverb fra- \"\n   \"(PIE *pro-, hence Nourai's cross-reference to his root Per 1): BRT col. 1067 'mit fra ‚herzutragen, -bringen zu —‘ \"\n   \"… frānāšayata (Y 3.5)'. (e) 'ašnaoti' is the nu-present of the ablaut variant *n̥ǩ-neu-, but the form is wrong: \"\n   \"the Avestan word is ašnaoiti (Bartholomae col. 359f. s.v. aš- 'hingelangen zu', pres. 10 ašnav-/ašnv-, attested \"\n   \"paiti.ašnaoiti V 4.17, ava.ašnaoiti Yt 10.24, frāšnaoiti V 3.27; so too Klein p.524 'Avestic ashnaoiti' and \"\n   \"Wiktionary s.v. *h₂neḱ-). The printed page (pdf 358, book 328) really does read 'ašnaoti', so this is Nourai's \"\n   \"misprint, not an extraction error — the -i- of the thematic ending has dropped out. (f) 'asa 2' = Av. ǟsa-, and it \"\n   \"does belong to the root (Pokorny p.316 'av. ǟsa- ‚Partei‘', beside Skt. aṃśa- 'Anteil'), but Nourai's gloss \"\n   \"'parcel, shipment' is not what the sources say: Bartholomae col. 360f. gives 'g. ǟsa- m. ‚Partei‘, nur Du. von den \"\n   \"beiden Religionsparteien' and Klein 'Avestic qsa-, ‘party’'; the inherited sense is 'share, portion' (so the Skt. \"\n   \"cognate) developing to 'faction, party'. 'Shipment' is a mistranslation, probably of an older dictionary's 'parcel' \"\n   \"in the sense 'portion'.\"),\n \"derivation_fa\": (\"پنج صورت از شش صورت این جعبه درست است. «nas 2» همان ²nas- در فرهنگ بارتولومه (ستون ۱۰۵۵ به بعد) است \"\n   \"به معنای «رسیدن به، دست‌یافتن»؛ شمارهٔ ۲ بجا و لازم است، زیرا ¹nas- اوستایی معنای «ناپدیدشدن، نابودشدن» دارد. «nasaiti» \"\n   \"سوم‌شخص مفرد همان ستاک است (هم‌ریشه با سنسکریت náśati). «naš» همان nāš- اوستایی «بردن، حمل‌کردن» است، گسترشِ s-دار \"\n   \"همین ریشه؛ بارتولومه در ستون ۱۰۶۷ ــ همان ستونی که نورایی ارجاع داده ــ می‌نویسد: «nāš- V. tragen» و آن را با لیتوانیایی \"\n   \"nešti و اسلاوی کلیسایی nesti «بردن» می‌سنجد. «fra-nâš» همین فعل با پیشوند fra- (از *pro- هندواروپایی، و از همین‌رو \"\n   \"ارجاع نورایی به ریشهٔ Per 1) است: بارتولومه در همان ستون «mit fra: herzutragen, -bringen zu» و شکل frānāšayata را می‌آورد. \"\n   \"اما «ašnaoti» نادرست است: صورت درستِ اوستایی ašnaoiti است (بارتولومه ستون ۳۵۹ به بعد ذیل aš-، با نمونه‌های \"\n   \"paiti.ašnaoiti و ava.ašnaoiti و frāšnaoiti؛ همچنین کلاین ص ۵۲۴ و ویکی‌واژه). خودِ صفحهٔ چاپی کتاب (ص ۳۲۸) «ašnaoti» دارد، \"\n   \"پس این خطای چاپی کتاب است و نه خطای خوانش اسکن؛ «ی» پایانه از قلم افتاده. سرانجام «asa 2» همان ą̇sa- اوستایی است و \"\n   \"به‌درستی به این ریشه می‌رسد (پوکورنی ص ۳۱۶: «av. ą̇sa- Partei»، در برابر سنسکریت aṃśa- «بهره»)، ولی معنایی که نورایی \"\n   \"داده («بسته، مُرسوله») در منابع نیست: بارتولومه (ستون ۳۶۰ـ۳۶۱) آن را «حزب، گروه ــ تنها در مثنّی، دربارهٔ دو گروه دینی» و \"\n   \"کلاین «party» می‌آورد؛ معنای موروثی «بهره، سهم» است که به «گروه، دسته» تحول یافته. کوتاه: بدنهٔ گره درست است، یک صورت \"\n   \"خطای چاپی کتاب دارد و یک معنی نادرست ترجمه شده است.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"ašnaoti\",\n \"correct_form\": \"ašnaoiti\",\n \"sources\": [PIE2],\n \"ref_check\": [\n   {\"ref\": \"KLN:524\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt line 13221 s.v. 'enough': 'whence also OI. asnati, Avestic ashnaoiti, ‘reaches, arrives at’, OI. nasati, Avestic nasaiti, ‘reaches’ … Avestic qsa-, ‘party’' — has nasaiti, ashnaoiti and qsa-, but glosses qsa- 'party', not 'parcel, shipment'.\"},\n   {\"ref\": \"SYN:707\", \"status\": \"supports\",\n    \"note\": \"Buck 10.61 CARRY (BEAR), printed p.707 = SYN.txt leaf 769/770: '2. IE *enk-, *nek-, *n̥k-. Walde-P. 1.128 f. … Skt. aś-, naś- ‘reach, attain’ … Av. nas- ‘reach, attain’, nāš- ‘carry’ (s-extension, Barth. 1067); Lat. nancisci … Goth. ga-nohs ‘enough’ … The meaning ‘reach, attain’ appears to be the primary one and ‘carry’ a secondary'. Buck's own cross-reference 'Barth. 1067' is where Nourai's third citation comes from.\"},\n   {\"ref\": \"BRT:1067\", \"status\": \"supports\",\n    \"note\": \"BRT.txt (leaf headed 'io67 nāsǟm'): 'j. nasǟm Inf. ‚hinzugelangen zu -, zu erlangen‘ … j., g. nāš- V. ‚tragen‘. Praes. 1 nāš-, 30 (Iter.) nāšaya- … mit fra ‚herzutragen, -bringen zu —‘ … frānāšayata … ‚Erweiterung‘ zu lit. nešti, ksl. nesti ‚tragen‘.' Column 1067 carries precisely naš and fra-nâš.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 359–361 (aš- and ǟsa-) and col. 1055f. (²nas-)\", \"stance\": \"partial\",\n    \"note\": \"col. 359f. 'j., g. aš- V. ‚hingelangen zu —‘, Praes. … 10 ašnav-, ašnv-' with paiti.ašnaoiti (V 4.17) — form is ašnaoiti, not ašnaoti; col. 360f. 'g. ǟsa- m. ‚Partei‘, nur Du. von den beiden Religionsparteien' — contradicts the gloss 'parcel, shipment'; col. 1055f. '²nas- V. ‚hingelangen zu —‘. Praes. 3 nasa- … s-Aor. nās-' — supports 'nas 2' and 'nasaiti'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.183f. s.v. *Hnas (Has) 'to reach, attain, take'\", \"stance\": \"supports\",\n    \"note\": \"'*AVESTAN: nāš- (aš-) ‘to reach, attain’ || (+ *abi-) … || (+ *ā-) … || (+ *fra-) ‘to attain, reach’ … «PIE *H₂nek- ‘to reach, attain’ = LIV: 282 f. | Pok.: 316 ff.', with attested auua.ašnaoiti, frāsnuiiat, nasaite, nasama — confirms one root behind nas-, nāš-, aš- and the fra- compound, and spells the nu-present ašnaoiti.\"},\n   {\"src\": \"POK\", \"where\": \"p.316–317\", \"stance\": \"partial\",\n    \"note\": \"'Ai. aśnóti, av. ašnaoiti (*nk-neu-) ‚gelangt hin zu etwas, erreicht‘ … av. -nasaiti … ai. ǟmśah m. ‚Anteil‘, av. ǟsa- ‚Partei‘' — supports every form but again glosses ǟsa- 'Partei' and spells ašnaoiti.\"}]\n}\n\nn2 = {\n \"id\": 2, \"lang\": \"Old Persian\",\n \"words\": \"âs 2, âsa\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"No Old Persian verb ās- 'to arrive, come' exists in the Achaemenid corpus. Kent's Old Persian lexicon \"\n   \"(the standard, and one of the books this project is meant to check Iranian nodes against) has no such entry: for \"\n   \"'come' it gives only ā + ay- (3pl. impf. mid. āyaǹtā, DZc 11) and ā + gam- (opt. ājamiyā, DPd 19), plus the \"\n   \"inchoative rasa- 'arrive'; its asa- entries are 'horse' (asa-bāra-) and possibly 'stone' (Asagarta-). So 'Old \"\n   \"Persian' here is really 'some pre-classical Iranian', reconstructed backwards from the New Persian verb of node #3, \"\n   \"and Nourai's own NOTE ('It is not certain if these words belong to this family of words') concedes the doubt. On the \"\n   \"modern account the verb is not from *(H)neḱ- at all: the āsān of Middle Persian xwarāsān 'sunrise, east' (MacKenzie \"\n   \"p.96) is the present participle of a north-west Iranian / Parthian-type verb 'to come, rise' — Parthian as-, cf. \"\n   \"Balochi āsag 'to rise' (so Wiktionary s.v. خراسان) — which goes back to Proto-Iranian *ā-sad- (Skt. ā-sad- 'arrive \"\n   \"at, reach, approach', PIE *sed-), not to *h₂neḱ-. Cheung's article on *Hnas lists no Persian continuant of the \"\n   \"root except panāh < *pati-nas- 'refuge'. In fairness, Avestan does have ā-nas-/ā-aš- 'to attain' (Cheung, '+ *ā-'), \"\n   \"so a form *ās- is not phonetically unthinkable; but no source draws that line, and Nourai gives none beyond TZF:62.\"),\n \"derivation_fa\": (\"در متون فارسی باستان هخامنشی هیچ فعلی به صورت ās- «آمدن، رسیدن» نیست. واژه‌نامهٔ کِنت ــ مرجع معیارِ \"\n   \"فارسی باستان ــ برای «آمدن» تنها ā + ay- (āyaṃtā در DZc ۱۱) و ā + gam- (ājamiyā در DPd ۱۹) و ستاک rasa- «رسیدن» را \"\n   \"می‌آورد؛ asa- در فارسی باستان یا «اسب» است (asa-bāra-) یا شاید «سنگ» (Asagarta-). پس این جعبه در واقع بازسازیِ \"\n   \"واپس‌نگرانه‌ای از فعل فارسی نو (گرهٔ ۳) است، و خودِ نورایی هم در یادداشت جعبه پذیرفته است که «معلوم نیست این واژه‌ها به \"\n   \"این خانوادهٔ واژگانی تعلق داشته باشند». دیدگاه امروزی این است که این فعل هیچ پیوندی با ریشهٔ *(H)neḱ- ندارد: بخش دومِ \"\n   \"«خراسان» (فارسی میانه xwarāsān «خاستنگاه خورشید، مشرق»، مکنزی ص ۹۶) صفت فاعلیِ فعلی از گونهٔ شمال‌غربی/پارتی به \"\n   \"معنای «آمدن، برآمدن» است ــ پارتی as-، و مقایسه‌شدنی با بلوچی āsag «برآمدن» (ویکی‌واژه ذیل خراسان) ــ که به ایرانی \"\n   \"آغازین *ā-sad- (سنسکریت ā-sad- «رسیدن، نزدیک شدن»، از *sed- هندواروپایی) بازمی‌گردد. چونگ نیز در مقالهٔ *Hnas هیچ \"\n   \"بازماندهٔ فارسی برای این ریشه جز «پناه» (از *pati-nas-) نمی‌شناسد. البته در اوستایی ā-nas-/ā-aš- «دست‌یافتن» هست، پس \"\n   \"صورتی چون *ās- از نظر آوایی محال نیست؛ اما هیچ منبعی این پیوند را نکشیده است. نتیجه: پژوهش امروزی این حلقه را رد می‌کند.\"),\n \"sources\": [KHOR],\n \"ref_check\": [\n   {\"ref\": \"TZF:62\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi p.62. refs_online.json records no local copy and no free scan (the ketabnak PDF is behind a login and the book is not on archive.org), so the cited page could not be read. Its author's own verb dictionary FFD (Fe'l-ha-ye Farsi-ye Dari) is on disk and has no آسیدن entry at all (grep of FFD_pages.txt: only آسودن and هراسیدن).\"}],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.vv. ay-, gam-, asa- (KNT.txt lines 5029, 5360f., 1192)\", \"stance\": \"contradicts\",\n    \"note\": \"'ā + ay- ‘come’: āyaǹtā 3d pl. imf. mid. DZc 11'; 'gam- vb. ‘come’ … ā + gam- ‘come’: ājamiyā opt. … DPd 19'; 'pIE *eḱuo- ‘horse’, OP asa- in acc. asam and in asabāra-'. Kent has no verb ās-/āsa- at all, and no OP word of this shape means 'come'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.183f. s.v. *Hnas\", \"stance\": \"contradicts\",\n    \"note\": \"The only New Persian / west Iranian reflex Cheung admits for this root is '(+ *pati-) NP panāh ‘refuge, asylum’'; no ās-/āsīdan, and no Old Persian form.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.96 s.v. xwarāsān\", \"stance\": \"partial\",\n    \"note\": \"'xwarāsān [hwlʼsnʼ | M xwrʼsn, N ~] sunrise, east' — the noun is good Middle Persian, but MacKenzie lists no Pahlavi verb ās- from which to build it, so the verb is only inferred.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt (grep آسیدن)\", \"stance\": \"silent\",\n    \"note\": \"Mo'in's Farhang-e Farsi has no headword آسیدن in the digitised text; nothing for or against.\"}]\n}\n\nn3 = {\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"âsîdan «آسیدن»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The word itself is genuine: آسیدن āsīdan 'to come, arrive' is a rare classical verb (Dehkhoda glosses it \"\n   \"آمدن، رسیدن), and the couplet Nourai quotes from Fakhr al-Dīn As'ad Gorgānī's Vis o Rāmīn (mid-11th c.) is the \"\n   \"locus classicus for it — Borhan-e Qate' s.v. خراسان, with Mo'in's footnote 'in Pahlavi Xvarāsān (mashriq)', prints the \"\n   \"three couplets together: 'خوشا جایا بر و بوم خراسان / درو باش و جهان را می‌خور آسان ‖ زبان پهلوی هر کو شناسد / \"\n   \"خراسان آن بود کزوی خورآسد ‖ خورآسان را بود معنی خورآیان / کجا ازوی خورآید سوی ایران'. The poem is its own gloss: \"\n   \"خورآسد = خور آید 'the sun comes', خورآسان = خورآیان, and Noushin's Vazhe-namak says flatly 'خورآسد پهلوی \"\n   \"باشد: خور آید'. Morphologically ās-īdan is a secondary NP infinitive built on the present stem ās-, the same stem \"\n   \"in MP xwarāsān 'sunrise, east' (MacKenzie p.96). What is not supported is the ancestry drawn here: the stem is the \"\n   \"Parthian-type verb 'to come, rise' (Parthian as-, Balochi āsag), from Proto-Iranian *ā-sad- (PIE *sed-), so the \"\n   \"arrow from node #2 and hence from the root box carries the same problem as #2 — the word is right, the pedigree is \"\n   \"not. Extraction note: the JSON quote reads هر که شناسد where the printed page (and Borhan) read هر کو شناسد.\"),\n \"derivation_fa\": (\"خودِ واژه اصیل است: «آسیدن» فعلی کم‌کاربرد از فارسی کلاسیک است و دهخدا آن را «آمدن، رسیدن» معنی کرده؛ \"\n   \"بیتِ فخرالدین اسعد گرگانی در «ویس و رامین» (میانهٔ سدهٔ پنجم هجری) شاهدِ اصلی آن است. برهان قاطع ذیل «خراسان» ــ با \"\n   \"حاشیهٔ معین: «در پهلوی Xvarāsān (مشرق)» ــ هر سه بیت را پشت‌سرِهم آورده است و شعر خود شرحِ خویش است: «خورآسد» یعنی \"\n   \"«خور آید» و «خورآسان» یعنی «خورآیان». نوشین در «واژه‌نامک» نیز می‌نویسد: «خورآسد پهلوی باشد: خور آید». از نظر ساخت، \"\n   \"«آسیدن» مصدرِ ثانویِ فارسی نو بر پایهٔ ستاک حاضرِ «آس-» است؛ همان ستاکی که در xwarāsān فارسی میانه «مشرق» (مکنزی ص ۹۶) \"\n   \"دیده می‌شود. آنچه پذیرفتنی نیست تبارِ ترسیم‌شده است: این ستاک به فعلِ گونهٔ پارتی «آمدن، برآمدن» (پارتی as-، بلوچی āsag) و \"\n   \"از آن‌جا به ایرانی آغازینِ *ā-sad- (از *sed- هندواروپایی) می‌رسد، نه به *h₂neḱ-. پس واژه درست است ولی پیوندِ آن با این \"\n   \"ریشه پذیرفتنی نیست. یک نکتهٔ فنی: در فایل استخراج‌شده «هر که شناسد» آمده، در حالی که صفحهٔ چاپی کتاب و برهان قاطع «هر کو شناسد» دارند.\"),\n \"sources\": [KHOR],\n \"ref_check\": [\n   {\"ref\": \"TZF:62\", \"status\": \"not_checked\",\n    \"note\": \"Same as node #2: Abolghasemi's Tarikh-e Mokhtasar-e Zaban-e Farsi is not available online or locally (refs_online.json: 'PDF exists but not downloadable without login').\"}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' s.v. خراسان with Mo'in's footnote 1 (BQT_v2_pages.txt line 10568)\", \"stance\": \"supports\",\n    \"note\": \"'زبان پهلوی هر کو شناسد / خراسان آن بود کزوی خورآسد ‖ خورآسان را بود معنی خورآیان / کجا ازوی خورآید سوی ایران' («ویس و رامین ص ۱۷۱»), footnote 'در پهلوی Xvarāsān (مشرق)'. Attests both the verse and the ās- stem, and confirms هر کو against the JSON's هر که.\"},\n   {\"src\": \"FSF\", \"where\": \"Noushin, Vazhe-namak s.v. خاور/خراسان (FSF_pages.txt lines 3309–3310)\", \"stance\": \"supports\",\n    \"note\": \"'نام‌های جهات چهارگانه به زبان پهلوی چنین است: خوراسان [خراسان] مشرق …' and, after the same Gorgānī couplet, 'خورآسد پهلوی باشد: خور آید' — i.e. āsad = āyad 'comes', exactly Nourai's gloss for the verb.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.96 s.v. xwarāsān (PHD.txt line 663)\", \"stance\": \"supports\",\n    \"note\": \"'xwarāsān [hwlʼsnʼ | M xwrʼsn, N ~] sunrise, east' — the Middle Persian ancestor of the compound in the quoted verse; MacKenzie's index also has 'east xwāstar, xwarāsān' and 'sunrise xwarāsān'.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt / HUB.txt (grep Chorasan, hurāsān, āsīdan)\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss has no article on āsīdan or on Khorāsān; Hübschmann mentions 'Chorasan' only as a geographical name (HUB.txt line 8874, citing Sebeos p.67), with no etymology.\"}]\n}\n\nn4 = {\n \"id\": 4, \"lang\": \"Germanic\",\n \"words\": \"ga-nôga\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The form is right and comes straight from the reference Nourai cites. Watkins (AHD) s.v. nek-²: \"\n   \"'I. O-grade form *nok- in Germanic *ga-nah- (*ga-, intensive prefix; see kom), “satisfies,” forming *ganōga-, \"\n   \"sufficient, in Old English genōg, enough: ENOUGH.' Pokorny p.317f. gives the same set: 'got. ganah \"\n   \"(Prät.-Präs.) ‚es reicht = genügt‘ … ō-stufig: got. ganōhs ‚genug, viel‘, ags. genōh, genūg, anord. (g)nōgr, \"\n   \"ahd. ginuog', i.e. Gmc. *ga-nōga- is the o-grade *nok- of the root plus the Germanic prefix. What is wrong is the \"\n   \"gloss: 'not little' analyses ga- as a negative, which it is not — Germanic ga- is the collective/intensive prefix \"\n   \"from PIE *kom 'beside, near, with' (Watkins s.v. kom §1 lists ENOUGH under it), cognate with Latin com-. Watkins's \"\n   \"'not little' phrasing belongs elsewhere in his book, to Latin nimis < *ne-mi-s. So *ganōga- means simply 'sufficient, \"\n   \"amply reaching', not 'not little'.\"),\n \"derivation_fa\": (\"صورت درست است و مستقیم از همان مرجعی می‌آید که نورایی داده است. واتکینز در پیوستِ AHD ذیل nek-2 \"\n   \"می‌نویسد: «صورتِ o-دار *nok- در ژرمنی *ga-nah- (با ga-، پیشوندِ تأکیدی؛ نگاه کنید به kom) به معنای «بس است»، که \"\n   \"*ganōga- «کافی» را می‌سازد، در انگلیسی باستان genōg: ENOUGH». پوکورنی (ص ۳۱۷ـ۳۱۸) هم همین مجموعه را دارد: گوتیک \"\n   \"ganah «بس است»، گوتیک ganōhs «بس، فراوان»، انگلیسی باستان genōh/genūg، نورس باستان (g)nōgr، آلمانی علیای باستان \"\n   \"ginuog. آنچه نادرست است معنی است: «not little» (نه‌کم) پیشوندِ ga- را منفی‌ساز گرفته، در حالی که ga- ژرمنی پیشوندِ \"\n   \"جمعی/تأکیدی و بازماندهٔ *kom هندواروپایی «با، نزدِ» است (هم‌ریشه با com- لاتینی) و واتکینز نیز «enough» را زیر همان \"\n   \"kom آورده است. تعبیرِ «not little» در کتاب واتکینز جای دیگری دارد: برای nimis لاتینی از *ne-mi-s. پس معنای \"\n   \"*ganōga- تنها «کافی، بسنده» است. کوتاه: صورت درست، تجزیهٔ معنایی نادرست.\"),\n \"sources\": [PIE2, ETY_EN],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"AHD_watkins1985.txt line 776 s.v. nek-² gives *ganōga- 'sufficient' exactly, but derives ga- from *kom (intensive prefix), not from a negative; so the reference supports the form and contradicts the gloss 'not little'.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.317–318 (POK_01.txt, enek- entry)\", \"stance\": \"supports\",\n    \"note\": \"'got. ganah (Prät.-Präs.) ‚es reicht = genügt‘, Inf. ganaūhan … ō-stufig: got. ganōhs ‚genug, viel‘, ags. genōh, genūg, anord. (g)nōgr, ahd. ginuog ‚genug‘' — the Germanic branch of the root, as drawn.\"},\n   {\"src\": \"KLN\", \"where\": \"p.524 s.v. enough\", \"stance\": \"supports\",\n    \"note\": \"'… OE. genoh, rel. to OS. ginog, ON. gnogr, Swed. nog, Dan. nok, OFris. enoch, Du. genoeg, OHG. ginuog(i), MHG. genuoc, G. genug, Goth. ganohs, ‘enough’, OE. geneah, OHG. ginah, Goth. ganah, ‘it suffices’' — same Germanic set, glossed 'enough / it suffices', never 'not little'.\"},\n   {\"src\": \"WEB\", \"where\": \"Wiktionary, Reconstruction:Proto-Indo-European/h₂neḱ-\", \"stance\": \"supports\",\n    \"note\": \"lists Proto-Germanic *ganōgaz (and *nēhwaz) among the descendants of *h₂neḱ- 'to reach, attain'; archived copy in data/verification/sources/web/.\"}]\n}\n\nn5 = {\n \"id\": 5, \"lang\": \"English\",\n \"words\": \"enough\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Straight inheritance inside English. OE genōg / genōh 'sufficient in quantity or number' (the -g and -h \"\n   \"spellings are the same word, final /ɣ/ ~ /x/) > ME inogh, enogh, enouh > NE enough; the initial ge- was reduced to \"\n   \"e-/i- in early Middle English as in every other ge- prefix, and the final velar fricative was written -gh and then \"\n   \"lost in pronunciation, leaving the -ough spelling and modern /ɪnˈʌf/. Klein p.524, the page Nourai cites, gives just \"\n   \"this chain; Etymonline adds the semantic detail that the adjective yielded an adverb 'sufficiently' and, already in \"\n   \"Old English, the understated 'quite, rather'.\"),\n \"derivation_fa\": (\"این حلقه یکسر درون‌زبانی و بی‌گفتگو است. انگلیسی باستان genōg/genōh «کافی، به‌اندازه» (دو نویسهٔ g و h \"\n   \"یک واژه‌اند: سایشیِ پایانیِ /ɣ/~/x/) در انگلیسی میانه به inogh، enogh، enouh و سپس به enough امروزی رسیده است؛ \"\n   \"پیشوندِ ge- مانند همهٔ پیشوندهای ge- در آغازِ انگلیسی میانه به e-/i- کاهش یافته و سایشیِ کامیِ پایانی -gh نوشته شده و \"\n   \"سپس در تلفظ افتاده و نگارشِ -ough و تلفظِ /ɪnˈʌf/ از آن مانده است. کلاین در همان صفحهٔ ۵۲۴ که نورایی ارجاع داده همین \"\n   \"زنجیره را می‌آورد. ادعای نورایی درست است.\"),\n \"sources\": [ETY_EN, PIE2],\n \"ref_check\": [\n   {\"ref\": \"KLN:524\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt line 13221: 'enough, adj. — ME. inogh, enogh, enouh, fr. OE. genoh, rel. to OS. ginog … Goth. ganohs, ‘enough’ … fr. I.-E. base *enek-, *nek-, *nk-, ‘to reach, attain, carry’' — exactly the arrow Germanic → English drawn here.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nek-² and index ('ENOUGH kom, nek-2', line 1461)\", \"stance\": \"supports\",\n    \"note\": \"'… forming *ganōga-, sufficient, in Old English genōg, enough: ENOUGH' — and the word index files ENOUGH under both kom and nek-².\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. enough\", \"stance\": \"supports\",\n    \"note\": \"'Old English genog ‘sufficient in quantity or number’, from Proto-Germanic *ganog ‘sufficient’ … from PIE *nok-, from root *nek- (2) ‘to reach, attain’' — archived copy in data/verification/sources/web/.\"},\n   {\"src\": \"POK\", \"where\": \"p.318\", \"stance\": \"supports\",\n    \"note\": \"'ags. genōh, genūg' listed as the o-grade Germanic adjective of the root, the direct antecedent of the English word.\"}]\n}\n\nn6 = {\n \"id\": 6, \"lang\": \"Germanic\",\n \"words\": \"bher-nk\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The compound is exactly what the cited reference has, but it is a PIE form, not a Germanic one, and it is \"\n   \"not universally accepted. Watkins (AHD) s.v. bher-¹ §4: 'Compound root *bhrenk-, to bring (< *bher- + *enk-, to \"\n   \"reach; see nek-²), in Germanic *brengan in Old English bringan, to bring: BRING' — so *bhrenk- sits at the \"\n   \"Indo-European level and the Germanic stage is *brengan/*brangjan-; the box's 'Germanic' label and the hyphenated \"\n   \"spelling 'bher-nk' conflate the two, and the gloss 'to arrive carrying (something)' is Nourai's own paraphrase of \"\n   \"Watkins's 'to bring'. Pokorny is more reserved: he gives *bhrenk-, bhronk- 'bringen' its own entry (IEW 168f., with \"\n   \"Welsh he-brwng, Goth. briggan, OHG bringan, Toch. B prahk-) and reports the analysis only as hearsay — 'Angebl. \"\n   \"aus den Wzz. bher- und enek- kontaminiert; zuletzt E. Fraenkel KZ. 58, 286f.' Klein p.190 likewise stops at 'fr. \"\n   \"Teut. base *bhrenk-' without decomposing it, and Wiktionary now assigns Proto-Germanic *bringaną to the other root \"\n   \"*h₁neḱ- 'to receive, take away', not to the 'reach' root Nourai's box hangs it under. The arrow is a real \"\n   \"scholarly opinion (Watkins's), but not the consensus.\"),\n \"derivation_fa\": (\"این ترکیب درست همان چیزی است که مرجعِ ارجاع‌شده دارد، اما صورتی هندواروپایی است نه ژرمنی، و پذیرشِ \"\n   \"همگانی هم ندارد. واتکینز ذیل bher-1 بند ۴ می‌نویسد: «ریشهٔ مرکبِ *bhrenk- «آوردن» (از *bher- + *enk- «رسیدن»؛ نگاه \"\n   \"کنید به nek-2)، در ژرمنی *brengan، در انگلیسی باستان bringan». پس *bhrenk- در لایهٔ هندواروپایی می‌نشیند و مرحلهٔ \"\n   \"ژرمنی *brengan/*brangjan- است؛ برچسبِ «ژرمنی» و نگارشِ «bher-nk» این دو لایه را در هم می‌آمیزد، و معنیِ «رسیدن در \"\n   \"حالِ حمل چیزی» بازنویسیِ خودِ نورایی از «to bring» واتکینز است. پوکورنی محتاط‌تر است: او *bhrenk-, bhronk- «آوردن» \"\n   \"را ریشه‌ای مستقل می‌گیرد (ص ۱۶۸ـ۱۶۹، با ولزی he-brwng، گوتیک briggan، آلمانی علیای باستان bringan، تخاری B prahk-) و \"\n   \"تجزیهٔ آن را تنها نقلِ قول می‌آورد: «گویا از دو ریشهٔ bher- و enek- آمیخته شده است؛ اخیراً ا. فرنکل». کلاین نیز (ص ۱۹۰) \"\n   \"به «از ستاکِ ژرمنیِ *bhrenk-» بس می‌کند و آن را تجزیه نمی‌کند، و ویکی‌واژه امروز ژرمنیِ آغازینِ *bringaną را به ریشهٔ \"\n   \"دیگر، *h₁neḱ- «گرفتن، بردن»، می‌بندد و نه به ریشهٔ «رسیدن». نتیجه: ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [PIE1, ETY_BR],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 333 s.v. bher-¹ §4: 'Compound root *bhrenk-, to bring (< *bher- + *enk-, to reach; see nek-2), in Germanic *brengan in Old English bringan, to bring: BRING'; and s.v. nek-² 'II. Variant form *enk- … 2. Compound root *bhrenk- (see bher-¹)'. This is precisely Nourai's box, including the cross-reference to his root Bher 1.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.168–169 s.v. bhrenk-, bhronk- (POK_01.txt line 2436)\", \"stance\": \"partial\",\n    \"note\": \"'bhrenk-, bhronk- ‚bringen‘. Cymr. he-bricng … got. briggan, brāhta, ahd. bringan … Angebl. aus den Wzz. bher- und enek- kontaminiert; zuletzt E. Fraenkel KZ. 58, 286f.; 63, 198.' Pokorny keeps *bhrenk- as a separate root and calls the bher- + enek- analysis merely 'alleged'.\"},\n   {\"src\": \"KLN\", \"where\": \"p.190 s.v. bring (KLN_1966.txt line 5661)\", \"stance\": \"partial\",\n    \"note\": \"'bring, tr. v. — ME. bringen, fr. OE. bringan … Goth. briggan, fr. Teut. base *bhrenk-. Outside Teut. cp. W. he-brwng, ‘to send’' — Klein reconstructs *bhrenk- but does not analyse it as *bher- + *enk-.\"},\n   {\"src\": \"WEB\", \"where\": \"Wiktionary, Reconstruction:Proto-Indo-European/h₁neḱ-\", \"stance\": \"contradicts\",\n    \"note\": \"puts Proto-Germanic *bringaną under *h₁neḱ- 'to receive, take away' and states this root was 'conflated with *h₂neḱ- (to reach, attain) by Pokorny' — i.e. bring does not belong under the same root as enough on the current view.\"}]\n}\n\nn7 = {\n \"id\": 7, \"lang\": \"English\",\n \"words\": \"bring\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Undisputed Germanic inheritance. OE bringan (also breng(e)an; weak preterite brōhte < *branhta, past \"\n   \"participle brōht) > ME bringen > NE bring, beside Gothic briggan/brāhta, OHG bringan, OS brengian, Du. brengen, \"\n   \"G. bringen — all from Proto-Germanic *brengan / *brangjan- (Klein p.190; Pokorny p.168; Etymonline *brangjanan). \"\n   \"The odd preterite brought preserves the pre-Germanic velar before the *-t- of the dental preterite (*branh-ta > \"\n   \"OE brōhte with loss of n and lengthening). This node carries no reference in the book; the chain is covered by \"\n   \"Klein, Pokorny and Etymonline alike.\"),\n \"derivation_fa\": (\"این حلقه بی‌گفتگوست و درونِ ژرمنی می‌ماند. انگلیسی باستان bringan (و breng(e)an؛ گذشتهٔ ضعیفِ brōhte \"\n   \"از *branhta و اسم مفعولِ brōht) به انگلیسی میانه bringen و انگلیسی امروز bring رسیده است، در کنارِ گوتیک \"\n   \"briggan/brāhta، آلمانی علیای باستان bringan، ساکسون باستان brengian، هلندی brengen و آلمانی bringen ــ همه از \"\n   \"ژرمنیِ آغازینِ *brengan/*brangjan- (کلاین ص ۱۹۰، پوکورنی ص ۱۶۸، اتیمولاین *brangjanan). گذشتهٔ نامنظمِ brought همان \"\n   \"همخوانِ کامیِ کهن را پیش از -t- گذشته‌ساز نگه داشته است: *branh-ta با افتادنِ n و کشیدگیِ واکه به brōhte بدل شده. این \"\n   \"جعبه در کتاب هیچ ارجاعی ندارد، ولی زنجیره را کلاین و پوکورنی و اتیمولاین یکسان تأیید می‌کنند.\"),\n \"sources\": [ETY_BR, PIE1],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\",\n    \"note\": \"The box carries no reference in the printed book (refs=None); nothing of Nourai's to check. The chain was verified against Klein p.190, Pokorny p.168 and Etymonline instead — see 'consulted'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p.190 s.v. bring (KLN_1966.txt line 5661)\", \"stance\": \"supports\",\n    \"note\": \"'bring, tr. v. — ME. bringen, fr. OE. bringan, rel. to OS. brengjan, OFris. brenga, MDu. brenghen, Du. brengen, OHG. bringan, MHG., G. bringen, Goth. briggan, fr. Teut. base *bhrenk-.'\"},\n   {\"src\": \"POK\", \"where\": \"p.168\", \"stance\": \"supports\",\n    \"note\": \"'got. briggan, brāhta, ahd. bringan, brāhta, ebenso as. (wo auch brengian), ags. bringan und breng(e)an Prät. brōhte (aus *branhta) ‚bringen‘' — the Germanic paradigm including the OE preterite.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. bring\", \"stance\": \"supports\",\n    \"note\": \"'Old English bringan ‘to bear, convey …’ (past tense brohte, past participle broht), from Proto-Germanic *brangjanan … from PIE root *bhrengk-, from root *bher- (1) ‘to carry’' — archived copy in data/verification/sources/web/.\"}]\n}\n\nroot[\"nodes\"] = [n1, n2, n3, n4, n5, n6, n7]\n\nout = {\n  \"pdf_page\": 358,\n  \"book_page\": 328,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [root]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-358.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk358.py && python3 -m json.tool data/verification/page-358.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 358",
 "description": "Write and validate page-358.json"
}
```


### [2026-09-07T18:34:34.275Z] TOOL RESULT

```
written
JSON OK
nodes verified: 7/7
node verdicts: {'transcription_suspect': 1, 'disputed': 1, 'plausible': 3, 'confirmed': 2}
root verdicts: {'plausible': 1}
ref checks: {'supports': 5, 'not_checked': 3, 'partial': 1}
books consulted: {'partial': 5, 'supports': 13, 'contradicts': 3, 'silent': 2} | by book: {'POK': 5, 'WEB': 4, 'KLN': 3, 'CHEUNG': 2, 'PHD': 2, 'BRT': 1, 'KNT': 1, 'MON': 1, 'BQT': 1, 'FSF': 1, 'HRN': 1, 'AHD': 1}
```


## [2026-09-07T18:34:42.349Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 - <<'PY'\nimport json, io\np=\"data/verification/page-358.json\"\nd=json.load(open(p))\ne=d[\"entries\"][0]\ne.pop(\"verdict_detail\", None)\nfor n in e[\"nodes\"]:\n    for c in n.get(\"consulted\", []):\n        if c[\"src\"]==\"WEB\":\n            c[\"src\"] = \"Etymonline\" if \"Etymonline\" in c[\"where\"] else \"Wiktionary\"\nwith io.open(p,\"w\",encoding=\"utf-8\") as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write(\"\\n\")\nprint(\"fixed\")\nPY\npython3 -m json.tool data/verification/page-358.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 358",
 "description": "Clean up keys and source labels"
}
```


### [2026-09-07T18:34:43.802Z] TOOL RESULT

```
fixed
JSON OK
nodes verified: 7/7
node verdicts: {'transcription_suspect': 1, 'disputed': 1, 'plausible': 3, 'confirmed': 2}
root verdicts: {'plausible': 1}
ref checks: {'supports': 5, 'not_checked': 3, 'partial': 1}
books consulted: {'partial': 5, 'supports': 13, 'contradicts': 3, 'silent': 2} | by book: {'POK': 5, 'KLN': 3, 'CHEUNG': 2, 'PHD': 2, 'Wiktionary': 2, 'Etymonline': 2, 'BRT': 1, 'KNT': 1, 'MON': 1, 'BQT': 1, 'FSF': 1, 'HRN': 1, 'AHD': 1}
```


## [2026-09-07T18:35:07.788Z] AGENT

Page 358 done: `/home/sfmqrb/git/rishe/data/verification/page-358.json` — `verify_check.py 358` reports 7/7 nodes, 0 PROBLEM lines.

**Verdicts** (1 entry, 7 nodes; 2 redirect entries skipped)
- root: plausible · nodes: 2 confirmed, 3 plausible, 1 disputed, 1 transcription_suspect
- ref checks: 5 supports, 1 partial, 3 not_checked (all TZF / the un-referenced `bring` box)

**Flagged items**
- ROOT *Neku, Nokut, Nek 2, Nk, Enek, Enk* — plausible: POK:316 and KLN:524 give `enek-/nek-/enk-/n̥k-` "reach, attain, carry" verbatim, but "Neku" and "Nokut" are Nourai's own coinages (from the `*n̥ḱ-neu-` present and from Pokorny's `nactus = Gmc *nuh-ta-`), and they collide with `*nekʷ(t)-` "night" which he files on the same page as redirects to Noktis. Modern reconstruction also splits `*h₂neḱ-` "reach" (→ *enough*) from `*h₁neḱ-` "take away" (→ *bring*, Av. `nāš-`); Pokorny conflated them.
- #1 Avestan `ašnaoti` — transcription_suspect: real form is `ašnaoiti` (BRT col. 359f. `paiti.ašnaoiti`; Klein, Cheung, Wiktionary). **The book itself prints `ašnaoti`** (`error_in: book`; page PNG saved to `data/verification/sources/refs/ocr/BOOK/358.png`). Same node: `asa 2` glossed "parcel, shipment" is wrong — BRT col. 360f. and Klein give ą̇sa- "Partei/party" (inherited "share, portion", cf. Skt. aṃśa-). All of `nas 2`, `naš`, `nasaiti`, `fra-nâš` check out; BRT:1067 is literally the column with `nāš- 'tragen'` and `fra-nāš-`, and Buck 10.61 (p.707) is where Nourai got that citation.
- #2 Old Persian `âs 2, âsa` — disputed: no such verb in Old Persian; Kent has only `ā+ay-`, `ā+gam-`, `rasa-` for "come" (`asa-` = "horse"). The `āsān` of MP *xwarāsān* is a Parthian-type verb "to come/rise" (Parth. `as-`, Bal. `āsag`) from PIr. `*ā-sad-` (PIE `*sed-`), not `*h₂neḱ-`; Cheung's `*Hnas` admits no Persian reflex but `panāh`. Nourai's own NOTE concedes the doubt.
- #3 Persian `âsîdan` — plausible: word and verse genuine (Borhan-e Qate' s.v. خراسان with Mo'in's footnote; Noushin's Vazhe-namak "خورآسد پهلوی باشد: خور آید"), but its pedigree is `*ā-sad-`, not this root.
- #4 `ga-nôga` and #6 `bher-nk` — plausible: forms are Watkins's exactly, but #4's gloss "not little" mis-analyses Gmc `ga-` (< PIE `*kom`, not a negative), and #6's `*bhrenk-` is a PIE compound root (Gmc is `*brengan`), which Pokorny p.168 reports only as "angeblich" and Wiktionary assigns to `*h₁neḱ-`.

**Extraction error for the owner to fix**: node #3's quote in `data/extracted/batch/page-358.json` reads `زبان پهلوی هر که شناسد`; the printed page (and Borhan-e Qate') read `هر کو شناسد`. Everything else in the JSON, including the odd root headwords and `ašnaoti`, is faithful to the page.

Five web pages archived via `fetch_source.py` (two Wiktionary PIE reconstructions, Wiktionary خراسان, Etymonline *enough* and *bring*).
