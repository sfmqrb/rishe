# Verification process log — verify-page-314


## [2026-09-07T01:37:01.355Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 314 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-314.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-314.json. Write /home/sfmqrb/git/rishe/data/verification/page-314.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 314` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T01:37:03.479Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T01:37:04.128Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T01:37:04.143Z] TOOL RESULT

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


## [2026-09-07T01:37:04.742Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-314.txt"
}
```


### [2026-09-07T01:37:04.757Z] TOOL RESULT

```
1	=== PDF page 314 (book page 284) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Lithra : a scale, balance  (refs AHD:1527)
4	#1 (parent #0) [Greek] refs=AHD:762; KLN:896 | litra : a unit of weight, also a unit of liquid measure
5	  #2 (parent #1) [Middle Latin] refs=AHD:762; KLN:896 | litra : a liquid measure
6	    #3 (parent #2) [French] refs=AHD:762 | litre
7	      #4 (parent #3) [Persian] refs=VOP:318 | lîtr «لیتر» : liter
8	      #5 (parent #3) [English] refs=AHD:762 | litre, liter
9	  #6 (parent #1) [Arabic] refs=VGH:65 | lîtr : liter ; ratl : a large liquid container | NOTE: "ratl" is a distorted form of "lîtr"
10	    #7 (parent #6) [Persian] refs=MON:1660; VGH:65 | lîtr «لیطر» : liter ; ratl «رطل» : a large cup of wine
11	#8 (parent #0) [Latin] refs=AHD:349 | Libra : balance, Roman pound ; Dě-lîberâre : to weight well, ponder
12	  #9 (parent #8) [English] refs=KLN:886; AHD:349 | Libra, deliberate, equilibrium
13	--- entry 1 ---
14	ROOT Ljakti -> redirect to Lakti
15	--- entry 2 ---
16	ROOT Lôi -> redirect to Lěi
17	--- entry 3 ---
18	ROOT Loik -> redirect to Uroiks
19	--- entry 4 ---
20	ROOT Long -> redirect to Longos
21	--- entry 5 ---
22	ROOT [Indo-European] Longos, Lenghô, Leng, Long : limp, lame, bent, also a low land, meadow  (refs IEC:678,709)
23	#1 (parent #0) [Persian] refs=IEC:678,709 | lang «لَنگ» : lame
24	#2 (parent #0) [Sanskrit] refs=IEC:709 | langah : lame
25	#3 (parent #0) [Greek] refs=IEC:709 | loggos : grove
26	
```


## [2026-09-07T01:37:07.027Z] AGENT

I'll read the source JSON and supporting infrastructure.


## [2026-09-07T01:37:08.451Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-314.json | head -200",
 "description": "Read page 314 source JSON"
}
```


### [2026-09-07T01:37:09.881Z] TOOL RESULT

```
{
    "pdf_page": 314,
    "book_page": 284,
    "entries": [
        {
            "root": {
                "name": "Lithra",
                "lang": "Indo-European",
                "refs": "AHD:1527",
                "gloss": "a scale, balance",
                "note": "This is most likely a Mediterranean word"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD:762; KLN:896",
                    "words": [
                        {
                            "translit": "litra",
                            "gloss": "a unit of weight, also a unit of liquid measure",
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
                    "lang": "Middle Latin",
                    "refs": "AHD:762; KLN:896",
                    "words": [
                        {
                            "translit": "litra",
                            "gloss": "a liquid measure",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "French",
                    "refs": "AHD:762",
                    "words": [
                        {
                            "translit": "litre",
                            "gloss": null,
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
                    "refs": "VOP:318",
                    "words": [
                        {
                            "translit": "l\u00eetr",
                            "gloss": "liter",
                            "script": "\u0644\u06cc\u062a\u0631"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 3,
                    "lang": "English",
                    "refs": "AHD:762",
                    "words": [
                        {
                            "translit": "litre, liter",
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
                    "parent": 1,
                    "lang": "Arabic",
                    "refs": "VGH:65",
                    "words": [
                        {
                            "translit": "l\u00eetr",
                            "gloss": "liter",
                            "script": null
                        },
                        {
                            "translit": "ratl",
                            "gloss": "a large liquid container",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": "\"ratl\" is a distorted form of \"l\u00eetr\"",
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "Persian",
                    "refs": "MON:1660; VGH:65",
                    "words": [
                        {
                            "translit": "l\u00eetr",
                            "gloss": "liter",
                            "script": "\u0644\u06cc\u0637\u0631"
                        },
                        {
                            "translit": "ratl",
                            "gloss": "a large cup of wine",
                            "script": "\u0631\u0637\u0644"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u062f\u0644 \u0645\u06cc\u062e\u0648\u0627\u0631\u0647 \u0631\u0627 \u0628\u0627\u0634\u062f \u0628\u0647 \u0645\u06cc \u0622\u0632 - \u0628\u0633\u06cc \u0631\u0637\u0644 \u0648 \u0628\u0633\u06cc \u0633\u0627\u063a\u0631 \u062e\u0648\u0631\u062f \u0628\u0627\u0632",
                        "poet": "V\u00ees-o-R\u00e2m\u00een"
                    }
                },
                {
                    "id": 8,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD:349",
                    "words": [
                        {
                            "translit": "Libra",
                            "gloss": "balance, Roman pound",
                            "script": null
                        },
                        {
                            "translit": "D\u011b-l\u00eeber\u00e2re",
                            "gloss": "to weight well, ponder",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "English",
                    "refs": "KLN:886; AHD:349",
                    "words": [
                        {
                            "translit": "Libra, deliberate, equilibrium",
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
                "name": "Ljakti",
                "redirect": "Lakti"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "L\u00f4i",
                "redirect": "L\u011bi"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Loik",
                "redirect": "Uroiks"
            },
            "nodes": []
        },
        {
            "root": {
```


## [2026-09-07T01:37:10.440Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','KLN','VOP','VGH','MON','IEC','POK','WLD','SYN','HRN','HUB','BQT','ARY','PHD','NYB','FVQ','AFM','PLA','SKT','FSD','WEB','LKT','TTS']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T01:37:11.663Z] TOOL RESULT

```
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
VGH {"title": "H. Khadiv Jam, Vazhe-name-ye Ghazalha-ye Hafez, Elmi 1371/1992", "kind": "website", "url": "https://ketabnak.com/book/121989 (145 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf",
```


## [2026-09-07T01:37:16.988Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-314.json'))\nprint(json.dumps(d['entries'][5], ensure_ascii=False, indent=1))\n\""
}
```


## [2026-09-07T01:37:17.772Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','KLN','IEC','MON','VGH','VOP']:\n    print('=====',k); print(json.dumps(d[k], ensure_ascii=False, indent=1))\n\""
}
```


### [2026-09-07T01:37:18.326Z] TOOL RESULT

```
{
 "root": {
  "name": "Longos, Lenghô, Leng, Long",
  "lang": "Indo-European",
  "refs": "IEC:678,709",
  "gloss": "limp, lame, bent, also a low land, meadow"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Persian",
   "refs": "IEC:678,709",
   "words": [
    {
     "translit": "lang",
     "gloss": "lame",
     "script": "لَنگ"
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": {
    "text": "پای ما لنگ است و منزل بس دراز - دست ما کوتاه و خرما بر نخیل",
    "poet": "Hâfez"
   }
  },
  {
   "id": 2,
   "parent": 0,
   "lang": "Sanskrit",
   "refs": "IEC:709",
   "words": [
    {
     "translit": "langah",
     "gloss": "lame",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 3,
   "parent": 0,
   "lang": "Greek",
   "refs": "IEC:709",
   "words": [
    {
     "translit": "loggos",
     "gloss": "grove",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  }
 ]
}
```


### [2026-09-07T01:37:19.650Z] TOOL RESULT

```
===== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
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
===== IEC
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
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
===== VGH
{
 "title": "H. Khadiv Jam, Vazhe-name-ye Ghazalha-ye Hafez, Elmi 1371/1992",
 "kind": "website",
 "url": "https://ketabnak.com/book/121989 (145 pp. PDF, login)",
 "lookup_hint": "Not on archive.org.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": false,
 "notes": "PDF page exists; not fetched."
}
===== VOP
{
 "title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992",
 "kind": "none",
 "url": null,
 "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."
}
```


## [2026-09-07T01:38:06.777Z] AGENT

Now let me check the local reference library.


## [2026-09-07T01:38:08.166Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60 && echo \"=== AHD lithra ===\" && grep -n -i 'lithra\\|līthr' AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T01:38:08.248Z] TOOL RESULT

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
=== AHD lithra ===
700:[lithra. A scale. Mediterranean word. 1. Probably Latin libra, a pound, balance: LEVEL, LIBRA, LIRA, LIVRE; DELIBERATE, EQUILIBRIUM. 2. Probably Greek /itra, unit of weight, pound: LITER.]
1752:LIPO- leip- LIQUATE wileik- LIQUEFY wleik- LIQUESCENT wleik- LIQUID wleik- LIQUOR wileik- LIRA lithra
1758:LIVRE lithra LIXIVIATE wleik- LLANO pele-2
```


## [2026-09-07T01:38:08.874Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN litra/liter ===\" && grep -n -i '^litra\\|^liter,\\|^litre\\|^Libra\\|^libra\\|^deliberate\\|^equilibrium\\|^rotl\\|^ratel' KLN_1966.txt | head -40"
}
```


### [2026-09-07T01:38:08.951Z] TOOL RESULT

```
=== KLN litra/liter ===
15:LIBRARY  OF  CONGRESS  CATALOG  CARD  NUMBER  65 -I  3229 COPYRIGHT  ©  1966  ELSEVIER  PUBLISHING  COMPANY,  AMSTERDAM ALL  RIGHTS  RESERVED
41:Library  for  the  facilities  extended  to  me  in  the  use  of  its  books.
10707:deliberate,  adj.  —  L.  deliberatus,  pp.  of  deliberare, ‘to  think  over,  take  counsel  about,  reflect,  de¬ termine’,  which  prob.  means  lit.  ‘to  weigh  in one’s  mind’,  and  derives  fr.  original  *de-librare, which  is  formed  fr.  de-  and  libra,  ‘scales;  that which  is  weighed;  a  pound’.  See  libra  and  adj. suff.  -ate  and  cp.  equilibrium.  L.  deliberare  was influenced  in  form  by  liberate,  ‘to  make  free’. Derivatives:  deliberate-ly,  adv.,  deliberate¬ ness,  n.
10708:deliberate,  intr.  and  tr.  v.  —  L.  deliberatus,  pp. of  deliberare.  See  deliberate,  adj.,  and  verbal suff.  -ate.
13472:equilibrium,  n.,  balance.  —  L.,  ‘even  balance’, compounded  of  aequus,  ‘equal’,  and  libra, ‘balance’.  See  equi-  and  libra, equimultiple,  n.,  one  of  the  products  obtained by  multiplying  two  or  more  numbers  by  the same  number.  —  Compounded  of  equi-  and multiple.
20920:LIBRARY  OF  CONGRESS  CATALOG  CARD  NUMBER  65- I  3  229 COPYRIGHT  C  1967  ELSEVIER  PUBLISHING  COMPANY,  AMSTERDAM ALL  RIGHTS  RESERVED
21641:libra,  n.,  a  pound.  —  L.  libra,  ‘balance;  Roman pound’,  fr.  earlier  *lipra,  whence  also  Gk.  Xixpa (Dor.  Xixpa  is  a  later  form),  of  s.m.  Cp.  librate, deliberate,  equilibrium.  Cp.  also  litra,  litre,  livre. Derivative:  libr-al ,  adj.
21642:library,  n.  —  ME.  librarie,  fr.  OF.  librairie,  ‘li¬ brary’  (F.  ‘bookshop’),  fr.  livraire,  since  the  13th cent,  libraire ,  ‘copyist’  (F.  ‘bookseller’),  fr.  L. librdrius,  ‘copyist,  bookseller’,  fr.  liber,  gen. libri,  ‘book’,  orig.  ‘the  inner  bark  of  a  tree’, whence  ‘the  text  written  on  this’,  ‘collection  of leaves  for  writing’,  and  finally  ‘book’.  L.  liber prob.  stands  for  *luber  and  is  a  derivative  of I.-E.  base  •leu-b(h)-,  *leu-p-,  ‘to  strip,  to  peel’. See  leaf  and  subst.  sufF.  -ary  and  cp.  leper,  lepi- do-.  Cp.  also  libel,  libretto,  ex-libris.
21644:librate,  n.,  land  worth  a  pound  a  year  (English hist.)  —  ML.  librata  (scil.  terra),  fr.  L.  libra.  See libra  and  adj.  suff.  -ate.
21645:librate,  intr.  v.,  to  be  balanced  or  poised  —  L. libratus,  pp.  of  librare,  ‘to  balance,  level,  make even’,  fr.  libra,  ‘balance;  pound’.  See  libra  and verbal  suff.  -ate.
21646:libration,  n.,  a  librating.  —  L.  librdtio,  gen.  -dnis, ‘a  balancing,  leveling',  fr.  libratus,  pp.  of  librare. See  librate,  v.,  and  suff.  -ion. librettist,  n.,  the  writer  of  the  libretto  of  an  opera. —  A  hybrid  coined  fr.  libretto,  and  -ist,  a  suff.  of Greek  origin.
21648:library.
21912:liter,  litre,  n.,  a  measure  of  capacity.  F.  litre, fr.  earlier  litron,  ‘an  old  measure  for  grain’,  fr. ML.  litra,  ‘a  liquid  measure’,  fr.  Gk.  XIxpa,  ‘a pound’.  See  litra.
21955:litre,  n.  —  See  liter.
31696:ratel
33174:rotl,  n.,  a  weight  used  in  North  Africa.  —  Arab. rati,  rel.  to  rdtala,  ‘he  poised’,  rattala,  ‘he weighed’.
```


## [2026-09-07T01:38:21.620Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# map line -> leaf (count formfeeds before)\ndef leaf_of(lineno):\n    return txt.split('\\n')[:lineno]  # placeholder\n# build cumulative\nleafidx=0\nres={}\nfor i,l in enumerate(lines,1):\n    res[i]=leafidx\n    leafidx+=l.count('\\f')\nfor ln in [10707,13472,21641,21912,21955,33174]:\n    print(ln, 'leaf', res[ln], '=> printed p ~', (res[ln]-12)*2)\nEOF\necho \"=== litra entry ===\"\ngrep -n 'litra,' KLN_1966.txt | head"
}
```


## [2026-09-07T01:38:22.536Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FVQ_pages.txt AFM_pages.txt AFA.txt LKT.txt DOZ.txt DEV.txt; do echo \"=== $f ===\"; grep -n -i 'ratl\\|rotl\\|رطل\\|litra' $f | head -12; done"
}
```


### [2026-09-07T01:38:22.974Z] TOOL RESULT

```
10707 leaf 230 => printed p ~ 436
13472 leaf 291 => printed p ~ 558
21641 leaf 476 => printed p ~ 928
21912 leaf 482 => printed p ~ 940
21955 leaf 483 => printed p ~ 942
33174 leaf 723 => printed p ~ 1422
=== litra entry ===
7932:clinical,  adj.  - —  Formed  with  adj.  suff.  -al  fr.  L. clinicus,  fr.  Gk.  xXmx6s,  ‘a  physician  who  at¬ tends  patients  in  their  beds’,  from  the  adjectiva xXIvixo?,  ‘pertaining  to  a  bed’,  fr.  xXfvtr),  ‘bed’, which  is  rel.  to  xXtueiv,  ‘to  cause  to  slope,  slant, incline’,  xXlptoc,  ‘inclination,  slope,  region’,  xXt- |xa£,  ‘ladder’,  xXtpaxTrip,  ‘rung  of  a  ladder’, xXTt6<;,  xXecru?,  ‘slope,  hillside’,  fr.  I.-E.  base *klei-,  ‘to  incline,  lean’,  whence  also  L.  -clinare (with  the  exception  of  the  pp.  clinatus,  occur¬ ring  only  in  compounds),  ‘to  bend,  turn’,  clivus, ‘slope,  hill’,  clitellae  (dimin.  of  *clitra,  for *kleitrd),  ‘a  packsaddle’,  Umbr.  kletram  (acc.), ‘litter,  bier’,  OI.  srayati,  ‘leans’,  sritah,  ‘leaning’, Lith.  slyti,  ‘to  slope’,  slieti,  ‘to  lean’,  slaitas, ‘declivity,’  sleivas,  ‘bandy-legged’,  Ofr.  cloin, ‘crooked,  wrong’,  Mir.  clithar,  ‘hedge’,  W. dedren,  ‘enclosure’,  Mir.  cle,  W.  cledd,  Co. cledh,  Bret,  kleiz,  ‘left’,  lit.  ‘slanting,  oblique’, Mir.  fo-chla ,  W.  go-gledd,  ‘north’,  lit.  ‘left’  (for sense  development  cp.  Heb.  semdl,  Arab. sham'dl,  shimdl,  ‘left;  north’),  Arm.  learn  (gen. leriri),  ‘mountain’,  Goth,  hlaiw,  ‘grave,  tomb’, OE.  hlxw,  hlaw,  ‘mound,  hill;  cave’,  OE.  hlinian, ‘to  lean’.  See  lean,  ‘to  incline’,  and  cp.  words there  referred  to.  Cp  also  acclivity,  aclinic,  anti¬ clinal,  clement,  client,  climacterium,  climate, climax,  clinamen,  clino-,  clitellum,  clition,  clivus, declension,  decline,  declivity,  diclinous,  enclitic, heteroclite,  incline,  isoclinic,  microcline,  mono- clinal,  pericline,  recline,  synclinal,  triclinium. I.-E.  base  *klei-  is  an  enlargement  of  base  *kel-, for  the  derivatives  of  which  see  heel,  ‘to  lean’ Derivative:  clinical-ly,  adv clink,  intr.  and  tr  v.  —  Prob.  fr.  MDu.  clinken (Du.  klinken),  ‘to  sound,  tinkle’,  which  is  rel.  to MLG.  klingen[  whence  ON.  klingia,  Dan .klinge, Swed.  klinga],  OHG.klingan,MHG.,G.klingen, ‘to  sound,  tinkle’;  of  imitative  origin.  Clink  is related  to  clank;  for  the  thinning  of  a  to  i  cp. click  and  clack.  Cp.  dough.
21641:libra,  n.,  a  pound.  —  L.  libra,  ‘balance;  Roman pound’,  fr.  earlier  *lipra,  whence  also  Gk.  Xixpa (Dor.  Xixpa  is  a  later  form),  of  s.m.  Cp.  librate, deliberate,  equilibrium.  Cp.  also  litra,  litre,  livre. Derivative:  libr-al ,  adj.
21912:liter,  litre,  n.,  a  measure  of  capacity.  F.  litre, fr.  earlier  litron,  ‘an  old  measure  for  grain’,  fr. ML.  litra,  ‘a  liquid  measure’,  fr.  Gk.  XIxpa,  ‘a pound’.  See  litra.
21954:—  Gk.  XFnj-n'ic,  ‘plainness,  simplicity’,  fr. Xtxoc,  ‘plain,  simple’,  fr.  I.-E.  base  *(s)le(i)-, ‘slimy,  sticky,  dauby,  slippery’,  whence  also  Gk Xetos  (for  *Xctfo? ),  ‘smooth’.  See  leio-. litra,  n.,  name  of  a  Greek  weight  and  coin.  —  Gk. Xfxpa  (Dor.  Xtxpa),  ‘pound’,  fr.  earlier  *lipra, whence  also.  L.  libra,  ‘Roman  pound’.  Cp.  libra, liter.
```


### [2026-09-07T01:38:24.241Z] TOOL RESULT

```
=== FVQ_pages.txt ===
12500:qf Parthasaratlii Misra by Ramanuja of the Prabhakara
=== AFM_pages.txt ===
1867:١الرطل‏ ) ® عشرة 5 اوقة ܘܐܒ ܡ وهو نصف المن النبريزى واللن التبديزي
=== AFA.txt ===
74:Eine Ton „het ProTlneiaal Utreehtseh GencotMliap tu Knnsten
2748:haben; derselbe Uebergang ist auch von /.Crpov zu litra vV^, et könnte aber
=== LKT.txt ===
2125:'Röte,  Rotlauf  [vom  Stamme  ahmar 'rot',  aus  dessen  fem.  hamra',  mit  ar. Art.  al-hamra'  'die  Rote'  der  Namen Alhambra  jenes  wunderbaren  maurischen Schlosses  auf  der  Höhe  von  Granada geworden  ist] ;  hieraus  sp.  alfombra, gewöhnlich  alfombrilla  'Masern'  [Dicc Gast  120  a].  —  Vom  gleichen  Stamme ist  sp.  alhamar  'rote  Decke'  [ebenda 123  b].
2767:Ein  Gewicht  von  100  Ratl  [s.  hier  Nr.  1 708 ; aus  lat.  centenarius,  ngr.  Kevxrivdpi  > mlat.  qiiintale];  hieraus  it.  cantaro,  siz. cantaiu  'Gewicht  von  100  rotuli',  qiiin- tale 'Zentner',  frz.  prov.  sp.  pg.  quintal 'dass.';  über  tk.  kantar,  das  die  Bedeu- tung 'Wage'  angenommen  hat,  wurde rum.  c'mtar  'Sehnellwage',  cintargiu 'Wiegemeister'.  [Mahn  EtUnt  126.  DE 327.    Eguilaz  425.
3601:'Natron'  [Prov.  25,20;  Jer  2.22;  wohl wie  aram.  niträ  aus  äg.  ntrj.],  hieraus gr.  vixpov,  lat.  nitrum  und  mit  lat.  sal zusammengesetzt:  it.  salnitro,  pg.  sp. salitre,  rum,  ^alitru;  dtsch.  Salniter, (dial.)  Saliter;  cech.  sahii/tr,  sanytr,  poln. saletra,  russ.  stlitra,  serb.  saliira  'Sal- peter'. Aus  ar.  natrün  ergab  sich  frz. engl.  7iatron,  dtsch.  Natron  und  mit  ar. Art.  sp.  anatron.
3896:1708.  Ar.  ratl:
3897:'Ein  Gewicht'  [aus  gr.  Xixpa;  ZDMG  LI, 298;  de  Lagarde,  Gesammelte  Abhand- lungen 33,  Anm.  Dieser  Entstehung entsprechend,  ist  die  Aussprache  riß nach  den  Arabern  selbst  die  richtigere, aber  unter  dem  Einflüsse  der  beiden ersten  Konsonanten  durch  die  andere ratl  aus  dem  Sprachgebrauche  verdrängt, FLEISCHER  in  BSGW  XXXII,  130]; hieraus  it.  (dial.)  rotolo  'Gewicht',  siz. ro<M?M 'Gewicht  von  12  Unzen',  sp.  (alt) arrate  'Gewicht  von  4  Pfund',  arrelde, arrel,  pg.  arretih  arratel,  frz.  arratel 'Gewicht  von  460g'.  [DE  201.  Devic DEt  35.    Eguilaz  286.    ML  7089.
9685:salitra,  1567
=== DOZ.txt ===
=== DEV.txt ===
722:'  y^y<ig<'^  <^(ins  l'archipel  dfis  Mohicqnes  (1768  à  1  778).  Tratl.  du  liollan- dais  par  Janson.  s*"  édit,  t.  II,  p.  .'.o.
```


## [2026-09-07T01:38:38.599Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA ctx ===\" && sed -n '2740,2760p' AFA.txt && echo \"=== AFM ctx ===\" && sed -n '1860,1875p' AFM_pages.txt"
}
```


### [2026-09-07T01:38:38.650Z] TOOL RESULT

```
=== AFA ctx ===
ist, nach Gauhari »Wasser, das mit Medicamenten ge-
kocht, in einen Krug gethan und von da tropfenweise
(XaJÜi ^LJLi) auf den Eopf des Kranken gegossen wird''
O m
1) Za derselben Warzel ^hört Termathlich aach ]]|J CMt. 637, wo das
^ sich dem vorhergehenden \ assimiliert hat. Derselbe Uebergang in ^y^
für mi^yi; and umgekehrt mJ^ für |<»-2j; {j»^^ für [j*^* ^-9-1 beden-
ket auch ein Gewicht, dies könnte sich aus dem Flüssigkeitsmaase entwickelt
haben; derselbe Uebergang ist auch von /.Crpov zu litra vV^, et könnte aber
auch einfach »Schwere** »Last** {pondci) sein.
2) In der zweiten bei Frcyta;r :in'.;cgebencn Bedeutung.67
ist gewiss erst aus syr. U^«?^ lAäLs^U Gast. 547 gebil-
det. Auch die Bedeutung » Wein pressen** filr Jdu (wober
JJbLuo) scheintauf »giessen** oder »tropfen** zurückzugehen.
Wie im Jüd. aram., ist auch ^N., J deuoniinat. » Wasser auf-
giessen** ZDilG. XXVII. 621, 8. Hierzu gehört JUaJut,
Dozy II. 685.
Es bliebe also schliesslich nur noch Jl^ju » Uuglilck*' ss
&Ai&ljJf übrig, das echt sein konnte. Aber auch dies ist
zweifelsohne nur eine poetische Übertragung von »Eimer",
vielleicht auch gar nur einer missverstilndlichen scholas-
=== AFM ctx ===
* (الرشك» اكبيد اللحية معرب من ريشكاو: اي بليسة الثور 9 علل
الرجل الاحمى
(الشغك) فادسق ححض وقو العقرب
04:02 39
( § القام الاول ٠‏ هن الانفام تعريب رانست ومعناه المستقي الموافق
+ د 0 معرب عن 7 الذي ܝ
ܟ ܨ ) ¥ 3 مغرت ܐܘܐ عن رت اي العريان ام عن رت أي الفقير
١الرطل‏ ) ® عشرة 5 اوقة ܘܐܒ ܡ وهو نصف المن النبريزى واللن التبديزي
1 109 ارخا ® على وعاء يوضع فيه الشراب :ونحوه فهر ܫܐ
باليونائّة ܚܝܫ 7 2 ® ٠‏ لست ادري هل اصله يوناني ام فاسي ܨ
(اأطل)» 12 0 ܟ واتكبير 0 0:30 تهون عن لاز
وهو ْيطلق على ما عتق من الاشياء وعلى الرجل الكهل والرذيل والسفيه
( ܬܵܢ قيل دواء يشبة الثوم فارسي ( يط امحيط) ول ܪ
6 من" 0 الكتسة مأخوذة من رأء اي الطيب !ܥ 4
8906 9 راموذ وهو الربان والفاسي مسأخوذ من
ܨ ` 3 ودعئاه م 0 البحر فاصله حبثي ` 4116[ ( ܝܢܝܐ ص
```


## [2026-09-07T01:38:40.151Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('total leaves', len(leaves))\nfor L in [354,355,369,370]:\n    print('#### leaf',L)\n    print(leaves[L][:1800])\nEOF"
}
```


### [2026-09-07T01:38:41.433Z] TOOL RESULT

```
total leaves 858
#### leaf 354
 “low set- tee’; MIr. clen ‘inclination, desire’; OHG lina, MHG lëne, line, lin, f. ‘back, support (MHG also: “balcony'); OFris. cf. hlen-bedd ‘sick- bed”; Li. cf. šlynù, inf. šlýti, intr. ‘lean, slope”. See next. Vowel obscure in Li. šlenúos, inf. šliñtis, id.
Klino, ið, aio ‘lean, slope; tilt; tend, go, in-
kleuinos (Klou-) — Kloinos, om, à, is, io
15
20
25
30
35
40
45
626
cline’. Cf. Kleio and Klit-. WP I, 490 Av. -sirinaomi, cpds. "gor: Gk. klinō, tr. intr. ‘lean, bend, tilf”; Lat. cfino, are, id.; MIr. den ‘inclination’; OHG hlinen ‘lean, lie down’; MHG linen, lénen, wd ` OS hlinon, tr. ‘lean, til; OE hlinian ‘lean, lie down’; Li. Slynü, Slýti ‘incline, lean". For Du. lenig, cf. Gk. klinikós .
Klitis ‘slope’. See next. WP I, 490, and cf. Kleiios, etc. Skt. $ritih approach": Gk. klísis "inclination, decline’; Lat. cf. (place-name) Clit-ellae 'val- leys, slopes’; MIr. clith- ‘sheltering’; W clyd, adj. ‘sheltered’; Ir. cf. cliteán ‘lean person’; Ger. Leite, f. ‘mountain-side’; ON hlið, f. i-st. ‘slope, mountain-side’; Li. Slitis, f. “pile, rick, row of sheaves, rump’; Slytis, f. ‘inclined plane’; Latv. cf. slita ‘banister; cattle-pen?
Klitos, à ‘sloping; slope’. Cf. Klitis. WP I, 490. Cf. Kleii, etc. Skt. $ritáh “attached” (isophonic, but possibly a different root); Gk. klítos, gs -eos, n., and klitüs, f. ‘slope’; OHG fita, G Leite, OE hlip, pl. hleobu, n. *mountain-slope, cliff; ON cf. i-st. hlið, hlíó, f. “side; slope’; Latv. slita “log- fence; balustrade'. (NB. The above forms co- incide in some instances with a type *klitis, kleitos, with velar initial).
(Kliuos ‘slope, ridge’. See Kloiuos. Lat. ambig.). WP I, 490 Olr. cu ‘ridge’; Lat. (ambig.) clivus, -um ‘slope’; Li. (*-ei-) cf. Sleivas ‘awry’
Kloii- (Kloin-) ‘Iean, slope, tilt. Variant of type Kleiio (Kleióo), 
#### leaf 355
lope’; Li. (long-gde) Sluonüs, adj. ‘sloping’. Cf. WP I, 442, I, 499 & II, 598
Klounis ‘buttock, thigh, haunch’. Cf. WP I, 411, 431 & 499 Skt. $rónih, f. id.; Av. sraonis, f. ‘hip’; Lat. clünis, m. f. ‘buttock’; W clun, pl. iau, f. ‘hip, haunch’; Br. klün; dual: di-glün, pl. klünioe, id.; Cor. clün, pl. -yow, f. id.; ON hlaun, f. n. id.; Li. šlaunis, f. ‘thigh, buttock’; Latv. cf. slauna, f. ‘hip’; Slaune ‘cow w. buttock-marks'. (The phonology of Gk. Kong f. ‘buttock’ has been influenced by type Klon-)
Klousos, ios “hearing; obedient; obedience’. WP I, 494. Cf. Klu-, etc.
 
Kloit- — Klus- (Kluso, io, eio; Klus-mi, KlüsKo, Klusn-)
20
25
30
35
40
45
 
628
Av sraoso, m. ‘obedience’; Arm. (ambig.) lsu, id.; cf. also lu i lu ‘publicly’; G. cf. lauschig ‘amenable’; OCS sluxü, m. “hearing”; sluxo, gs -ese ‘ear of pot’; Cz. cf. po-slušný obedient
(Kloustis, or Kleust-, Celtic form of type Klout- and Klustis by hybridism. Mir. doas Ir. cluas, f. ear pot-handle'; W clust, pl. -iau, f. id. Cf. Tokh. A klots, B klaut- so, id. See next)
Klout- (Kleut-) ‘hearing’. WP I, 494. Cf. Klu- stis, Kleus-, Klutos, etc. Skt. cf. $rótram, n. “ear, hearing, $rautab, adj. “of the ear’; Av. sraotom, n. ‘hearing’; Tokh. A klots, B klautso ‘ear’; cf. (variant): MIr. clüas, f., W clust, pl. -iau, f.; Go. cf. (e-gde) hliup ‘hearing’; Srb. slüta ‘diviner, forecaster’; slutim, v. “have prescience?
(Klouå, ios, io. “fame, rumour, glory”, etc. Cf. Kleu-, Klou-, etc. Skt. cf. $ravyah ‘audible’; OCS slava ‘glory’; Li. šlovē ‘fame’, for *šluovē ?)
Klu-, radical form of Kleu-, Kleu-, Klou-, Klou-, etc. q. v. WP I, 494
Klub-, cf. KIumb- (1) “hop, hobble’ MHG lupfen, lüpfen (2) jump’; Li. SJumbü, Slübti ‘limp’; Slübas, adj. ‘lame’
Klu$- OE cf. hloccetung ‘sighing’; Li. Sliuztu, inf. Sliüzti ‘wallow in misery’. 
#### leaf 369
tv. suns, gs suna, gp sunu. Variant: Skt. Sunih; Av. sünis; Li. šunis, mf ‘dog; bitch’; cf. Lat. cuni-culus ‘rabbit; cun-ila 'hore- hound’; cun-ilago 'fleabane'. Extn. in Go.
. hunds, and com. Gmc. Cf. Olr. pl. cointe
‘dogs’ beside con, id.
Kuodos (?), Kuad- (?). See Supt: K Arm. (?) šat, Let (plentiful'; adv. "vergi: OE hwaet ‘sharp, active’; ON hvatr, id.; hvati, m. “hurry”; hvot, f. impulse’
Kuoiio ‘weep, whine’. Cf. Kuoin-
Olr. cf. coi, f. ‘weeping’ beside ciim, v. ‘weep’; Ir. caoi, f., caoidhim, v. id.; OHG hwaijon, hweion ‘whinny, neigh’; MHG weien, weien, id.; Li. cf. $vajüs, adj. ‘twaddly’; $vóju, Svóti, v. ‘twaddle’; Late svajaju, v. id.
Kuoiios, -ón, -en ‘whey, serum’. WP I, 468-9
Oss. cài, Dig. c'àjá; Arm. Sic, and Sicuk, dim. type, gs Sicki, abl. -av, id.; Alb. cf. cikth, dim. type, id.; Br. küZen, m. id.; OE hwæg, n.; Fri- sian waei, n.; Du. (fr. Fris.) wei, f. beside Du. hui (doublet) id.; LG waddik, f., waddig, f. id.; Blg. cf. (dim. type) cvik, m. ‘cheese-whey’ Variant: Kuein- Olr. caínim, cáinim, cóinim, Ir. caoinim “la- ment’; Cor. kyny, id.; Br. cf. künüda, künüZa, id.; e-gde in W cwyn-, cpds. *wailing-, and in OE, ON hwinan, hvína ‘whizz, whirr, hum’; E whine; o-gde in p.t. hwan, ON hvein. (The ini- tial may be reflected in Cz. dial. caniti, inf. ‘whimper’. For G weinen, see uai-). Z-gde in ON hvinr, m. ^whirr, whizz’
Kuoit-, o-gde of type Kueit-, Kuit-, q. v. WP I, 470 Skt. $vetáh “white, bright"; sveta, f. ‘whiteness, brightness! cf. (vrddhi) a-$vait, aor. 3s. "he lighted’; Av. spaeto, adj. ‘bright’; OCS svétü, m. ‘light’ beside svésta, f. id. (fr. *Kuoitio); svésto, svétiti, v. “shine, illuminate’; Li. švie- tis, gs Oo, m. “lamp-o1l'; šviečiù, šviesti, v. "light, whiten’
w -
655 Kuoi
Kuoið (?)
Av. spaye(imi), v. ‘fell, remove’; Hes. soéð “drive, b
#### leaf 370
 consistency in the evolu- tion of what is here represented as Ku-, much of it onomatopoeic. See entries with initial qus-, su- and squ- for possible variants. Osse- tic and Slavonic reflexes are particularly diffi- cult to determine, except as variants. Greek and Latin also show some inconsistency.
Li. lábas, adj., labat, adv. wd Norw. cf. laps ‘dandy’ (?). (The existence of the parallel Li. form lobüs ‘wealthy’, lóbti, inf. ‘get rich’ sug- gests *láb-:làb-). Cf. labh-
labudios, io, iom, cf. labiom Gk. cf. lábuzos, f. (a spice-plant, so-named from shape of leaves?); Ger. Lefze, f. lip’; OCS lobüzü, m. *kiss'
(labh-, labhür-, see Imbh-)
labh- (labhos) “acceptable? (?). Cf. labhos. (All forms ambig. Cf. WP II, 385) Skt. lábhah (Cobtainable', but cf. Imbh-); Li. (?) lábas ‘good’; Latv. labs, id. (ambiguously *labh- or *lab-); Arm. lav, id. (ambig. as Li. and Latv.). See next
làbhos, ios, us (1) ‘gain; gainful, gained, pro- fitable'. Cf. labh-, Imbh- & WP II, 385 Skt. labhah “acquisition, profit'; Li. lobüs 'ac- quisitive, gainful; lóbis, gs. A0. m. “wealth?
lăbhos (2) (làbhis, ios) ‘limp, sloppy; siop’ Mir láib, f. ‘clay’; Ir. ‘mud’; OE lef "limp, weak’ beside Du. Fris. laf ‘sloppy, limp, stupid; muggy’; Li. lobas ‘riverbed, lowland’. Cf. also G Labbe “hanging lip’; ON lafa, v. ‘dangle’: mod. ‘garment’
` 651
labhros (labhər-) ‘limp, loose’. Cf. lubhros. (Expressive variant: labbhros) Oss. cf. labírín, Dig. laburun, v. “collapse, fall apart’; Du. labber, adj. “limp'; LG labber-ig, lawwer-ig, id.; beside labbern, lábbern ‘hang loose, flap, flop; slobber’; Lat. cf. labrum “lip”. Cf. slabhó, ið
(ládio? Dad? (1) The supporting evidence for these two formulae is entirely ambiguous. For lílád- as an intensive formula “strike, harm” cf. Lat. laedō, cpds: do. but with an ambiguous
```


## [2026-09-07T01:38:50.635Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^leng\\|^lengh\\|^longos\\|^long-\\|^longh\\|^lóng\\|^lengó\\|^lengh' IEC.txt | head -30; echo \"---- broader\"; grep -n 'longos\\|lengho\\|lenghos\\|langah\\|laṅga\\|langos' IEC.txt | head -30"
}
```


### [2026-09-07T01:38:50.697Z] TOOL RESULT

```
9660:lengho (1) “stretch, reach, advance, lunge, dart, project’. Cf. longhos and ingh-. WP I, 436 Skt. langhami “leap upon; waste’; langhe, mp. ‘cross’; ranghe "run cf. also ranghas, n. ‘speed’; Av. rag- (zero-gde?) ‘jump; lift; Gk. cf. (*-ñ-) lagkháno, pf. (*-o-) iélogkba; aor. (-n-) élakhon (*'cast', hence “acquire by luck"), cf. lógkhe (lit. ‘casting’, hence ot); MIr. & Ir (ambig. lingim (eap, dash’, but cf. *plenK-); OHG gi-lingan “proceed; succeed’; MHG cf. linge, f. ‘luck’; adj. ‘rapid’; R ljagát, ljagnùť ‘kick’; cf. dial. ljàga ‘thigb’; Z-gde in Latv. linga ‘sling’; o-gde in OHG lang (Clong', and com. Gmc.) and in Lat. longus
9661:lenghó (2) “reject, rebut, rebuff Gk. cf. elégkho “rebut, rebuff; Latv. liedzu, liegt “forbid, deny, refuse'; cf. o-gde langaju, at “call names, abuse”
9662:lengho (3) “trail, lie limp, pine’ (?) (Variant: leng-, long-. Si. Li. ambig.) (Per. langam, langidan, inf. “limp? is from a variant of type *leng- in view of Skt. langami, id.; langah lame); OCS 1ego, lẹšti “lie down’; Pol. cf. leg, m. ‘brood’; legnac, intr. ‘hatch out’; Li. cf. lengstu, lengti, v. ‘languish’. (For Lat. langueo, see slangueio. WH & EM un- tenable)
9663:lenguhos (variant of type elnguhos, elnghus, q.v.) lightweight Av. cf. renj-, v. ‘be lightweight; Gk. (from Phryg. or Thrac?) lémbos, m. ('skiff. The ex- pected Gk. form wd. be *lemph-); Li. lefigvas & lengvus "lightweight, easy’; Latv. liegs, id. (For MHG linge “rapid”, see lengho (1))
10042:longos “lame, bent, crooked; meadow, low- land”. (Semantics of Gk. kampé: Lat. campus, see kamp-, and of Li. lañkas “bend, bow? and lankà *watermeadow', see lonquos) Skt. langah ‘lame’; Per. lang, id.; Mod. Gk. lóggos, m. (*wood, grove’. A SI. LW for An- drioti); OCS logü, m., id.; Blg. lág ‘copse, meadow’; Cz. luh ‘meadow, heath’; Pol. lag, teg, m. “lowland, marsh’. (For G Lanke ‘waist, hip, haunch’; Ge-lenk, etc. see Supt: klong-, kleng-)
10043:longheio ‘make project; project, shoot; go forward’. See lengh- & next Skt. langháyami “leap over”; Ir. (?) cf. longui- ghim ‘haunt, frequent’; MHG langen ‘reach, stretch’; impers. ‘feel like, desire’
10044:longhos (1) ‘projecting; projection, reach; projector’. Cf. lengh-. WP I, 813 Skt. ranghas, n. ‘speed’; cf. e-gde ranghe, mp. ‘run’; Gk. lógkhe, f. (lot, portion’, lit. ‘what is cast); (2) ‘spearhead, lance’; Lat. longus ‘Jong’; Mir. long, f. “ship? beside longas, f. (banishment, fr. *longhosti); Br. long, pl. u, f. ‘ship’; W Ilong, f. id.; Go. laggs (long! and com. Gmc.); cf. also OE lang-scip *man-of- war’; z-gde in ON lung, n. id. beside langr, adj. ‘long’
10045:longhos, us (2) (?) “opening, gap’ Olr. long, f. “house, hall; lair; ON logg, f. *chimb of barrel; Li. lángas ‘window’; Latv. logs, id.
---- broader
9660:lengho (1) “stretch, reach, advance, lunge, dart, project’. Cf. longhos and ingh-. WP I, 436 Skt. langhami “leap upon; waste’; langhe, mp. ‘cross’; ranghe "run cf. also ranghas, n. ‘speed’; Av. rag- (zero-gde?) ‘jump; lift; Gk. cf. (*-ñ-) lagkháno, pf. (*-o-) iélogkba; aor. (-n-) élakhon (*'cast', hence “acquire by luck"), cf. lógkhe (lit. ‘casting’, hence ot); MIr. & Ir (ambig. lingim (eap, dash’, but cf. *plenK-); OHG gi-lingan “proceed; succeed’; MHG cf. linge, f. ‘luck’; adj. ‘rapid’; R ljagát, ljagnùť ‘kick’; cf. dial. ljàga ‘thigb’; Z-gde in Latv. linga ‘sling’; o-gde in OHG lang (Clong', and com. Gmc.) and in Lat. longus
9662:lengho (3) “trail, lie limp, pine’ (?) (Variant: leng-, long-. Si. Li. ambig.) (Per. langam, langidan, inf. “limp? is from a variant of type *leng- in view of Skt. langami, id.; langah lame); OCS 1ego, lẹšti “lie down’; Pol. cf. leg, m. ‘brood’; legnac, intr. ‘hatch out’; Li. cf. lengstu, lengti, v. ‘languish’. (For Lat. langueo, see slangueio. WH & EM un- tenable)
9663:lenguhos (variant of type elnguhos, elnghus, q.v.) lightweight Av. cf. renj-, v. ‘be lightweight; Gk. (from Phryg. or Thrac?) lémbos, m. ('skiff. The ex- pected Gk. form wd. be *lemph-); Li. lefigvas & lengvus "lightweight, easy’; Latv. liegs, id. (For MHG linge “rapid”, see lengho (1))
10042:longos “lame, bent, crooked; meadow, low- land”. (Semantics of Gk. kampé: Lat. campus, see kamp-, and of Li. lañkas “bend, bow? and lankà *watermeadow', see lonquos) Skt. langah ‘lame’; Per. lang, id.; Mod. Gk. lóggos, m. (*wood, grove’. A SI. LW for An- drioti); OCS logü, m., id.; Blg. lág ‘copse, meadow’; Cz. luh ‘meadow, heath’; Pol. lag, teg, m. “lowland, marsh’. (For G Lanke ‘waist, hip, haunch’; Ge-lenk, etc. see Supt: klong-, kleng-)
10046:lonquos, à “bent, crooked; bend, turn; mea- dow, field". (For semantics see longos above). WP II, 435. See lenquo Skt. raükah ‘stingy; slow; dull; poor’; m. *beg- gar”; Oss. länk ‘hollow, plain’; Tokh. B. lenke ‘slope’; OE cf. loh- in loh-sceaft and the phr.
14508:rembdhó (rombdh-) ‘run, chase’. (Skt. am- big. cf. lenghó) Skt. rámhami, v. ‘run’ (for ránghàmi, id. see lengho); Per. randan, inf. ‘drive; banish’; Oss. cf. ríndz, Dig. rindzå “path, track'; Alb. rénd, v. ‘run’ beside rrán, rrand, id. (prob. z-gde form of rénd); Tosk. Alb. cf. rëndë, f. ‘rennet’; (o-gde in) MIr. as-roinnim, v. ‘escape’; OHG cf. a-ranti, sn., OE &-rende, OFris. erende, ON erendi, órendi, n. ('errand', fr. *aue-rembdh-); LG cf. remsen, v. ‘rush, dash’. Cf. rembo (2)
14727:rong- ‘straight, forthright, ready, mature’. OE ranc, adj. ‘bold; noble; mature’; Li. rangà, f. ‘gear; equipment; élite; fulfilment of con- tract'; OLi. rangùs, adj. (2) ‘ready’; e-gde in rengiù, ^ti, v. ‘prepare’. (Isophone: Skt. langah ambig. phonology “lame)
```


## [2026-09-07T01:39:05.975Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nleaf=0; res={}\nfor i,l in enumerate(lines,1):\n    res[i]=leaf\n    leaf+=l.count('\\f')\nfor ln in [9660,9662,10042,10044]:\n    print(ln,'leaf',res[ln])\nleaves=txt.split('\\f')\nimport re\nfor L in [res[9660],res[10042]]:\n    nums=re.findall(r'\\b(6\\d\\d|7\\d\\d)\\b',leaves[L])\n    print('leaf',L,'page-like numbers:',nums)\nEOF"
}
```


### [2026-09-07T01:39:07.187Z] TOOL RESULT

```
9660 leaf 382
9662 leaf 382
10042 leaf 400
10044 leaf 400
leaf 382 page-like numbers: ['678']
leaf 400 page-like numbers: ['709', '710']
```


## [2026-09-07T01:39:07.683Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK leng ===\" && grep -n 'leng-\\|lengh-\\|longhos\\|lengu̯h' POK_full.txt 2>/dev/null | head -20; ls POK*; echo \"=== HRN lang ===\" && grep -n -i 'lang ' HRN.txt | head -20"
}
```


### [2026-09-07T01:39:07.748Z] TOOL RESULT

```
=== POK leng ===
29728:5. nasalized glengh- : Old High German k//ngan'r\ng, sound, clink' (without close 
47453:Root/ lemma: kleng-a'c\6 klenk- 
47479:See also: compare the rhyme roots /enk-'ben6', sleng-, slenk-^ coil, turn', skreng(h)-, 
55041:Unclear, whether to connect with lengh- "vilify, scold' (Osthoff MU. VI 7 ff.) 
78013:Root / lemma: slenk-, sleng- 
78241:Note: nasalized (s)leng-{= /e/7^- 'swing, waver'?) 
79821:Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- 
79943:fltextension sp(h)el-g-, nasalized (s)p(h)leng-: 
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
=== HRN lang ===
7331:27, 50 'der blaue Wolf, vergl. palang IJD kapötar
```


## [2026-09-07T01:39:12.085Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'Root / lemma: leng\\|Root/ lemma: leng\\|lemma: longho\\|lemma: lengh' POK_full.txt | head; echo \"=== ctx 55041 ===\"; sed -n '55010,55060p' POK_full.txt"
}
```


### [2026-09-07T01:39:12.149Z] TOOL RESULT

```
=== ctx 55041 ===


Root / lemma: lehizd-, lohizd-{*lehuzd-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: edge, fringe 

Material: Old High German ITsta^ bandformigerStreifen, Saum, Borte, Leiste ', Modern 

High German Leiste, Old English //5/' border, hemline, edge ' (from asachs. ITsta: Old 

Icelandic listai. " stripe, edge, strip '); alb. leth, ledh^ the raised edge of a property, 

margin, wall, riverside ' {*loizd-). 

References: WP. II 405. 

Page(s): 672-673 

Root/ lemma: {lehk-17) : lohk-{*lehuk-) 

Meaning: to scold, reprove 

Note: Only Celtic and Germanic 

Material: Old Irish lochtm. {*lok-tu-) "blame, fault, error'; 

Old High German Old Saxon lahan. Old English /ea/? "rebuke', nisi, /ads.. Old English 
leahtorm. " vice, crime, reprimand', mnl. lachter' shame, derision, ridicule'; Old Frisian 
laster. Old High German Old Saxon /5s/5/'"reprimand, insult, fault, error' {*lahstra-). Old 
Icelandic Igstrm. "fault, error, vice ' ( *lahstru-). 

Unclear, whether to connect with lengh- "vilify, scold' (Osthoff MU. VI 7 ff.) 

References: WP. II 436 f. 
Page(s): 673 

Root/ lemma: lehk-2{. lek-) and lehk-. Iahk-{*lehugh-) 
Meaning: joint, member; to bend, wind 



Material: Old \nd'\c rksa/a ' ankle of hoofed animals ' {*/k-s-e/a); common Old Indie gh- > 
ks- 

gr. Aa^, AaySriv "with dem Fufle ausschlagend', AaxMO<; (*AaKapoq) "das Ausschlagen 
with dem Fufte', AaKii^w "stofte with dem Fufte'; Aqktk;, -\oc, "Morserkeule'; ablaut. Ar|Kav 
TO np6(; d)5nv 6px£Ta6ai, Ar|Kr|aai nara^ai Hes . (: Latvian l$kat)\ AikeptI^eiv aKipTCiv HesJ 
{*leq-)- sA.Knn. S. 3nR under ^/--hend': 

whether Latin lacertus, mostly PI. " the muscular part of the arm from the shoulder to the 
elbow, upper arm ', lacerta "lizard' ("the flexible ')?? lacca " a swelling on the shinbone of
```


## [2026-09-07T01:39:14.501Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN lang/lang- ===\" && grep -n 'lang,\\|lang «\\|Aiä\\|hinkend\\|lahm' HRN.txt | head -20; echo \"=== HUB ===\"; grep -n 'lang\\b' HUB.txt | head -20; echo \"=== PHD ===\"; grep -n -i '^lang\\|lang ' PHD.txt 2>/dev/null | head; ls PHD* NYB* CHEUNG* ARY* 2>/dev/null"
}
```


### [2026-09-07T01:39:14.573Z] TOOL RESULT

```
Exit code 1
=== HRN lang/lang- ===
4898:547. diräz 'lang, diräza; vergl. direng.
7489:gr. y.vXXog zu skr. kuni- *lahm am Arm' (aus "^kulni-),
17958:6Aiä^- 183.
=== HUB ===
685:vareng) und bdlang. Die Bedeutung ist nicht nur
747:balu5i, vgl. drazad Lange' (neben drazt) von drag lang- 24 —
1998:es bei Firdusi lang erscheint, ist nicht xiJIs (Sal.
2221:ddc?) lautgesetzlich mit einander nicht in Einklang
5067:Mit Uebergang von w in a: palang 'Leopard oder
5068:Panther (aus *pulang) = afgh. prang *a tiger, a panther,
5613:Velum*; variing *Gurke, Citrone', np. badrang, balang, va-
6062:arm. pUnj; diraz ^) 'lang = zd. drajah-; diraxt *Baum'; dirafs
7635:Ton Belang.— 215 —
8216:diraz 'lang = zd. drajah-; sitez *Kampf', zd. stij- *Kampf' ;
8534:Wrzl. vik*^ (oben p. 10); palang 'Leopard', vgl. skr.prdaku-;
9029:lange Silben nicht (wie andere Konsonanten) uberlang macht,
9319:mrdtHka- *Weintraube'; palang 'Leopard*, afgh. pr(ing,[8kv,
10118:Umstellang von anl. Vocal + Doppelconsonant: p. 173.
=== PHD ===
430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
601:*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
2560:langour tandih.
2561:language uzwàn, (zuwān).
2562:languishing tand.
4681:frawahr - PO o parwāngāh 595 ep o parwanagih ^5 e» Ф parwanag 13 ? o frawār, parwāl M o frawār-, parwāl- ANN CH parwālišn e» O frawārdan wed > оу franàm- - PO v franāmišn Irv’ > vo parwāz о» ro franāftan мү оу \ o Farrobag Yo (read pin-) Farróbag | 23 » a) piring E N a palang 3 М оз рагпарап w as» QJ palangmusk VU re N) Q) parwand E R Фу parwand- - 9 i a parron Ў оу frogih- -45?o frogihistan Us 4» оу frog Po parrwar N М P
4996:kulang kirrdg sett kargās karkēhan kark karm, kirm karmīr karb, kirb karafs karbunag karzang kardār
(eval):1: no matches found: ARY*
```


## [2026-09-07T01:39:20.814Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'lang \\[' PHD.txt | head -5; echo \"=== NYB ===\"; grep -n 'lang\\b' NYB.txt | head -10; echo \"=== files ===\"; ls | grep -i -E 'ARY|BQT|MON|CHEUNG|HSN|SOD'; echo \"=== matrix ===\"; grep -n -i 'ARY\\|CHEUNG' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md | head -20"
}
```


### [2026-09-07T01:39:20.929Z] TOOL RESULT

```
430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
=== NYB ===
=== files ===
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
CHEUNG.txt
MON_part1.txt
MON_part2.txt
NYB_vol2_glossary.txt
SOD_pages.txt
SOD.txt
=== matrix ===
5:ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).
23:- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
25:- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
27:- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
29:- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
32:- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
38:- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
39:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
40:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
48:- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
51:- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
53:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt`
58:- **CHEUNG** — CHEUNG
59:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/CHEUNG.txt`
60:- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
63:- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
100:- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
101:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
102:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
118:- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
```


## [2026-09-07T01:39:27.771Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin lang ===\"; grep -n -i 'LANG\\b\\|LANG(' incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== ARY fa لنگ ===\"; grep -n 'لنگ' incoming/ARY/ARY_pages.txt | head -10; echo \"=== CHEUNG lang ===\"; grep -n 'lang' CHEUNG.txt | head -15"
}
```


### [2026-09-07T01:39:27.855Z] TOOL RESULT

```
=== ARY latin lang ===
4255:i, REFERENCES eth PALANG PAHLAV)) 5 34
7365:coh a9 er Waly cal a ayta cylin clang "eal eSB" 92 TF" Se tla 9 aly Ae
7874:REFERENCES , $s bcwtky |. LANG OLD SAXON) oS Go-S'e
7876:BARNHART: LANG, LENDZA
7878:‘MACKENZIE: (DURATION) 112 LANG, LENGAN
7879:BUCK: 882-883 LANG (GERMAN) glsT
7883:MALLOR & ADAMS: DLONGHOS LANG DANISH) si
7884:AY oad vb, LANG SWEDISH) 643 y+
7885:LANG NORWEGIAN) 5335
7886:LANG, LENGEN (DUTCH) (gute
=== ARY fa لنگ ===
1971:۱- معنی این واژه در هند و اروپایی و اکثر زبان‌های دیگر: کلنگ؛ پفکهه" 6
4349:۲ / پارس» پلنگ
13418:لنگ لنگیدن / ۴۵۳
13454:۱ رابطه‌ی آلنگه" با ان واجریشه‌ی هند و اروپایی و دیگر واژه‌های این فهرست در هیچ یک از مراجع من داده
=== CHEUNG lang ===
103:Abbreviations of languages nennen хуп 
208:For a very long time, a dictionary which incorporates all Iranian languages has been 
220:Middle and New Iranian languages barely known to many non-Iranists or even to 
222:for Iranian. A milestone in lexical-historical research of any Iranian language is the 
230:dictionaries for other languages have appeared since. Ivan Steblin-Kamenskij 
252:the prominence of Persian language and culture within the Iranian group. For the 
266:languages requires a separate present / past stem for the formation of the tenses: 
284:Finally, with regard to modern Iranian languages I had to limit myself to a 
285:representative selection of Eastern and Western languages, such as Ossetic, Shughni, 
288:important, recently published, contributions to the research of modern Ir. languages 
295:? This postulated ancestral language forms together with Indo-Aryan (and the little known group of lan- 
296:guages spoken in Nuristan, Afghanistan) the Indo-Iranian branch of the Indo-European language family. 
306:languages have been referred to as well”. The provenance of a root has been assessed 
316:As with other etymological dictionaries that contain vast amounts of languages 
323:etymological dictionary of the Iranian languages is still hampered by several
```


## [2026-09-07T01:39:28.943Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON رطل ===\"; grep -n 'رطل' MON_part1.txt MON_part2.txt | head -10; echo \"=== MON لیتر ===\"; grep -n 'لیتر\\|ليتر' MON_part1.txt MON_part2.txt | head -10; echo \"=== MON لنگ ===\"; grep -n '^لنگ\\|لنگ ' MON_part2.txt | head -10"
}
```


### [2026-09-07T01:39:29.031Z] TOOL RESULT

```
=== MON رطل ===
MON_part1.txt:17498:طسویل است؛ پریشاه‌رخ» سارطلایی؛ 
MON_part1.txt:18858:است برای وزن و آن را برابر با سل رطل» 
MON_part1.txt:28666:طرز تهیة آن (سبک قدیم): یک رطل شکر 
MON_part1.txt:28667:را با سه رطل بادام خوب می‌کوییدند بعد سه 
MON_part1.txt:28668:رطل شکر را با نصف اوقیه آب 
MON_part1.txt:67785:رطل: 12۱ [ع.] (.) واحدی است برای وزن 
MON_part1.txt:67787:است. پیالهٌ شراب؛ ج. ارطال. رطل گران: 
MON_part1.txt:88577:است معادل چهار مد و مساوی هشت رطل و 
MON_part2.txt:13745:الف - (قد.) واحد وزن معادل نود رطل 
MON_part2.txt:13771:در نبریز» قفیز جو و کشمش و ارزن ۳ رطل 
=== MON لیتر ===
MON_part1.txt:2359:پستانداران و عالیترین موجود زند؟ روی 
MON_part1.txt:10499:یک لیتر آن ۵ گرم وزن دارد در 
MON_part1.txt:13150:ارفع» عالیتر» بلندتر» اعلی. . روشنتر. 
MON_part1.txt:15857:هو ا. یک لیتر آن ۰۵ ۰ گرم جرم دارد. 
MON_part1.txt:34753:ساعت در حدود ۵ لیتر ادرار دفع می‌کند 
MON_part1.txt:34755:اضطراب افزاش می باید. در هر لیتر ادرار 
MON_part1.txt:46884:عالیترین استعدادها و قوی است و مانند 
MON_part1.txt:61791:دسی لیتر فررهنگ فارسی بموم ۰۸۹۳ 
MON_part1.txt:61794:دسی لیتر: 7-[062 (امر.) یک دهم ان 
MON_part1.txt:61795:عشر لیتر 
=== MON لنگ ===
1381:آن را کلنگ خوانند. . نرنیق» غرنیق» غرانق؛ 
9053:رومال. لنگ ( گر مابه). 
10018:ثاپ: : 5۲« [تر. - قاب] (ا.) استخوان شتالنگ 
16498:قیظه: (دبممدهرهر(.) (تص.) لنگ مانندی 
26630:لنگک سودن: از 0 کاری برنیامدن. 
26631:کمیتاش لنگ است: کم 
29773:درنده مانند پلنگ و ببر و شیر هم باکی 
30537:پلنگ و گرب وحشی نیز قرار دارند.) گربه‌ها 
30614:شیر و پلنگ و ببر و یوزپلنگ و گرب 
34758:لنگه| (ا.) هر چیز گرد و پیچیده؛ گروهه.
```


## [2026-09-07T01:39:36.302Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON ratl ctx ===\"; sed -n '67780,67795p' MON_part1.txt; echo \"=== MON لیطر ===\"; grep -n 'لیطر' MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-07T01:39:36.367Z] TOOL RESULT

```
=== MON ratl ctx ===
بی‌استخوان: رطبی است که نخلش نخلبندی 
نشده و مایةٌ نر به او نرسیده باشد. چنین 
رطبی هسته و استخوان صحیح ندارد و 
خشک و بی‌آب است. 

رطل: 12۱ [ع.] (.) واحدی است برای وزن 
و آن برابر دوازده اوقیه و مساوی ۸۴ مثقال 
است. پیالهٌ شراب؛ ج. ارطال. رطل گران: 
یال بزرگك» پیمانة بزرگك. 
رطویت: مت 4 . رطوبه ] (مص‌ل.) تر 
شدن» مرطوب گشتن. (اسص.) تری؛ 
نمناکی؛ مق. خشکی» یبوست. تازگی. نر می؛ 
ج. . رطویات. رطوبت هوا: مقدار بخار آب 
مسوجود در یکك سانتیمتر مکعب هوارا 
ی او وس 
(فز.) عبارت است از خارج قسمت رطوبت 
=== MON لیطر ===
```


## [2026-09-07T01:39:37.192Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY ctx 13418 ===\"; sed -n '13400,13460p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-07T01:39:37.249Z] TOOL RESULT

```
=== ARY ctx 13418 ===
فرانسه (۳8(/04): 8 ۰ [پسگشت‌ها کی
اسپانیایی (52۸(/182): 1310 20507
ایتالیایی (۷لام1): 10 0 (7۴) :ماقم
پرتغالی (۳071017835): 1310 2 (317) :50/25 2/۸
ساکسونی کهن ((54300 010): ۰ 1.6۳0 230 ناه
۱ فریزی کهن (0لفا9ل۲۸ صا0): ۰ 1188۸ 40 (39) 00/5
آلمانی کهن ((02791۸ 011 طلا0): 3 (1۶]) +7
8 1.8۲۴۷۲ 34 بان
۰ آلمانی (/4۸0ل088): تور رن ۱8۸۱ بره هان قاطع : ۱۸۸۵
انگلیسی کهن (لاقلا20/0 ۰:00 117۳۸
یادداشت,
۱- چم این واژه در سانسکریت: آوپزان» آویختن.
۲ واژه‌های لپ" فارسی و "10872" انگلیسی نیز از همین واجربشه‌ی هند و اروپایی آمده‌اند.
نخاری ۸ (۸ [(4ل70۸۶). هفکالشاه فرانسه (۳8۸1): ۱۵:۱
سانسکریت (54(/5577): هعشا ایتالیایی (7فقال7): ان ۱۳۵
یرنانی (078820)+ 60 ,180810 ایسلندی کهن (12/ 572/074 صا0):
لاتین (7107ما): 18 شاه
[pdf page 452]
لنگ لنگیدن / ۴۵۳
ساکسونی کهن ((54200 صا0): شاه
آلمانی کهن (/05704/0 ۷10 ا0): الشا5 پسگشت‌ها کرت تا
انگلیسی کهن (80لا8(0 ۰۰:02 هآ ومووو و ۰ ۲۵۵8
انگلیسی (8۸/015[7): و داهن ای یت ان
دانمارکی (0۸(۷[870): ۰ 8لکلگلشآ8 ,شا 4 (66ها5) ,582 تشم
سرئدی (8220157): شاه 3 (6هآ8) :002/5
نروژی (۷0870140: ها 8 (60هآ5) +5347
عرنی (لتي) (71421ل): 15 هنگ معین : ۳۸۴
اپرلندی کهن (57ل#] 00): ها فت‌نامه دهخدا:. :۱۹۳۸
ولزی (57): شآ
یادداشت:
۱ واژه‌های "لاش " و آلاشه" هم از همین واجریشه‌اند. :
۲+ جم این واژه در زبان تخاری: افسرده
چم این واژه در زبان‌های لاتین و سانسکریت: شَل» لگ
سانسکریت (54(55777): 1۸۸ 107
ابسلندی کهن ((0104۸/(م5 صا0): لهستانی (لاکلاه: 1.۸
آللشاآ روسی (/#55142): 109
ساکسونی کهن (547:0۸0 02): ۰ 1۸810 چکه (۲2830): 2:07
فریزی کهن (54۸ن۳8 صا0): ۰ 1016 لش[ بلفاری (/(4ل6۸): 1077
مر ار آلمانی کهن (62204۵/۷ ۲1۵ صا۵): شا اسلراکی (5101/420): لا زا
و آلمانی (0889/۸(0): .1 آینرانی (7140۷لا777/.): 117
انگلیسی کهن مسق ضام: هلتشا لترنی (لتي) ((7۲4ا): 117
انگلیسی ((6۸701/8): 1.8 پروسی کهن (4(۷ز۲۸۲:۹5 0۵): 1347۷۷1
دانمارکی (0۸7/54): ۱1 ایرلندی میانه (ل5لع1 047005 13
سرئدی (507:0[37): ها ولزی (]کا#): 1
نروژی (/(۸70۱78014): فا برتونی (88870/7): 12
هلندی (7ل007): 1 آلبانی ((7۵لمقلم): ها شلها
اسلاوی کهن (6:/اما5 67260 00):
[pdf page 453]
۴ )| نگ (مثلاً در ابنگ و پاچه»)
پسگشت‌ها اراد 3 (۸3/8) :00/5
زر 1 7 (318ه) +57
4 (۹15ش) پاک مت نا برهان قاطع : 0 و ۱۹:۷
19 (0۸۸8) 4اه فرهنگ معین : ۶۱
بادداشت. ۰
۱ رابطه‌ی آلنگه" با ان واجریشه‌ی هند و اروپایی و دیگر واژه‌های این فهرست در هیچ یک از مراجع من داده
نشده» بهمین دلیل برای احتباط در جلو واجریشه‌ی هند و اروپایی (شاید) آورده‌ام.
۲ چم این واژه در زبانهای اسلاوی و بالنیکه: شکستن
چم این واژه در زبانهای ولزی و ایرلندی میانه و برتونی: ناتران» از کار افتاده.
گس سرواژی تسش 86
کردی (68/0/5/7): 1136 بکلالشا ,1.1856 سوئدی (8[750157): عش
افغانی (پشتو) (/۸۳0۸۷): 110۸ نروژی (/0/07/20۵0: 106
```


## [2026-09-07T01:39:54.111Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'Page(s): 67[5-9]' POK_full.txt | head -20; echo \"--- root lemmas near\"; grep -n 'Root / lemma: leg\\|Root/ lemma: leg\\|lemma: leng\\|lemma: sleg\\|lemma: (s)leg' POK_full.txt | head -20"
}
```


### [2026-09-07T01:39:54.182Z] TOOL RESULT

```
55156:Page(s): 675 
55188:Page(s): 675 
55215:Page(s): 675 
55236:Page(s): 675 
55256:Page(s): 676 
55283:Page(s): 676 
55322:Page(s): 676-677 
55365:Page(s): 677 
55396:Page(s): 677-678 
55439:Page(s): 678 
55459:Page(s): 678 
55481:Page(s): 679 
55499:Page(s): 679 
56753:Page(s): 679 
--- root lemmas near
54109:Root / lemma: legh- {*lehugh- ) 
54214:Root / lemma: leg-1 {* lehug- ) 
54241:Root/ lemma: leg-2{* lehug-) 
54259:Root / lemma: leg- {* lehug- ) 
78238:Root / lemma: (s)leg-. (sj/ag- and (s)leg- 
78299:Root / lemma: sleg"-
```


## [2026-09-07T01:39:55.406Z] TOOL CALL #24: Bash

```json
{
 "command": "ls tools/ && timeout 60 python3 -c \"\nimport urllib.request\nr=urllib.request.urlopen('https://en.wiktionary.org/wiki/%D9%84%D9%86%DA%AF',timeout=30)\nprint(r.status)\n\" 2>&1 | tail -3"
}
```


### [2026-09-07T01:39:56.941Z] TOOL RESULT

```
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
  File "/usr/lib/python3.12/urllib/request.py", line 639, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden
```


## [2026-09-07T01:39:59.518Z] TOOL CALL #25: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-07T01:39:59.530Z] TOOL RESULT

```


```


## [2026-09-07T01:40:00.106Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '78238,78300p' POK_full.txt"
}
```


### [2026-09-07T01:40:00.161Z] TOOL RESULT

```
Root / lemma: (s)leg-. (sj/ag- and (s)leg- 
Meaning: weak, feeble 

Note: nasalized (s)leng-{= /e/7^- 'swing, waver'?) 

Material: Old Indie laiiga- "lame'; gr. Anyw 'lasse ab, hear auf (*ermatte); trans, "make 
withdraw' {*slegd}, aAAriKTOc; (*aA-) 'unaufhorlich', Aayaaaai acpsTvai Hes., Aayapoc; "slack, 
fragile, flimsy, thin', hom. Aaywoq, Ionian ka\/6q, Attic Aayclx;, -cb "hare' {*(s)lag-dusos^yN\Vc\ 
schlaffen ears'), Aaycbv, -ovoq usually PI. "the groin, DiJnnen' (formal = Old Icelandic laki 
"Faltmagen'), Aayavov "thin wide cake' (formal = Old Saxon /akan etc. "kerchief, cloth'), 
Awyaviov " dewlap ' (compare Swedish s/o/ra "schlaff herabhangen'), nasalized 
presumably here Aayya^u) " hesitate ', Aayycbv "Zaudern', Aayysuai cpsuyai Hes. (*"faint, 
languid sein, schlaff and unschliJssig sein'); with the meaning " lustful ': ka\/\/oq "horny, 
lustful', AayvEusiv " lustful sein', Aayvsia "lust, desire, sensuality, voluptuousness', Awyaq 
nopvri Hes. (besides with e-Vok. Asyai 5s YuvaiKzq = aKoAaaroi Archil., sAsyaivEiv 
"aasAyaivsiv' EM.; 



Latin /axus's\ack, wide, capacious ', nasaNzea langueo, -ere "faint, languid, slacl<, 
abgespannt sein'; 

Old Irish /ace (with expressive gg) "slack, weak'; mcymr. Ilacc, ncymr. //ac "slack' derives 
because of seines cc instead of c/7from engl. slack. 

Middle Low German /5/r"slack, loose ', Dutch lak. Modern High German Dialectal lack 
ds.. Middle Dutch laka\so " lustful ', Old Icelandic lakrav\6 (full grade) lakr^evW, bad, 
small'; with gradation d Swedish dial. /oAa "schlaff herabhangen'. Old Icelandic lokr^ 
blockhead, Faulpelz'; Germanic 7a/ra/7a-"baumelnder rag, corner, tail' in Old Saxon lakan 
"kerchief, cloth'. Old High German lahhanAs. (Modern High German Lakenirovn dem Low 
German, formal compare gr. Aayavov), Old Icelandic laklm. " tadpole, frog or toad larva '; 
the manyplies of the ruminant, Faltmagen' (= Aayoov), lack, fault, error'; 

with S-: Old Icelandic slakr^s\acV! (poet.), slakna^ languish, tire, slacken ', Old Saxon 
Middle Low German s/ac"slack, weak', participle Old Saxon ^/5/e/r//"stumpf gemacht'. 
Middle Low German 5/a/r-s/o'e'"Bauchseite' (as Aaycbv and Modern High German 
Welchen), Old English 5/^c "slack, idle, slow'. Old High German slah- "slack, idle'. Old 
English sleccan ( *slekjan) " exhaust, weaken '; 

with gradation 6: Old Icelandic slokr^a limp boy', Norwegian 5/o/re/7 "slack', Swedish 
s/o/ra "schlaffherabhangen lassen', dial, "trage sein', 5/0/rand (with e) s/a/r "leichtsinniges 
woman'. Old Swedish sloklfnP, -M/5"Kebsweib'; 

nasalized probably Swedish 5///7/ra"nicht fest ansitzen, shiver, limp ', Old High German 
sllnc, Dutch sllnk^ left ', Middle High German link. Modern High German link. Old High 
German lenka'6\e Linke', Swedish llnka and lanka ' somewhat limp ', /i//7/ra "slowly go', 
Danish slunken ^s\ack, schlotterig' (*"schlaff dahergehen'); perhaps Swedish dial, slank. 
South German schlank' scrap, shred, thin'; 

Latvian leg^ns ^ s\ack, soft'; 

doubtful russ. pere-slega lau\t, error in texture ' (*"Auslassen of Fadens'??), sloven. 
/7/'es/e^as/"fadenscheinig, naked, bald, bleak'; 

whether also Tocharian A slakkar'sa6'7 

References: WP. II 712 ff., WH. I 758 f. 
Page(s): 959-960 



Root / lemma: sleg"-
```


## [2026-09-07T01:40:10.804Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '55240,55330p' POK_full.txt | grep -n 'Root / lemma\\|Meaning\\|Page(s)'"
}
```


### [2026-09-07T01:40:10.910Z] TOOL RESULT

```
1:Root / lemma: lehngh- {*lehungh-) 
3:Meaning: to scold 
17:Page(s): 676 
19:Root / lemma: lehng- {*lehung-) 
20:Meaning: to bend oneself; to sway 
44:Page(s): 676 
48:Root / lemma: lehnk- {*lehunk-) 
49:Meaning: to bend 
83:Page(s): 676-677 
85:Root / lemma: lehnto- {*lehunto-) 
87:Meaning: flexible
```


## [2026-09-07T01:40:12.917Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D9%86%DA%AF",
 "prompt": "Give the full Persian etymology sections for لنگ (lang). Include all etymologies listed (lame; loincloth; etc.), the reconstructed Proto-Iranian/Proto-Indo-Iranian/PIE forms, Middle Persian forms, Sanskrit cognates, and any cited authorities (Cheung, Hasandust, MacKenzie). Quote verbatim."
}
```


### [2026-09-07T01:40:20.732Z] TOOL RESULT

```
# Persian Etymology for لنگ (lang)

Based on the Wiktionary content provided, here are the Persian etymologies:

## Etymology 1 (Lame/Leg)

The word derives from Proto-Iranian *langa-, which comes from Proto-Indo-Iranian *langa- ("lame"). According to Pokorny, it ultimately traces to Proto-Indo-European *(s)leh₁g- ("feeble, weak").

**Cognates include:**
- Central Kurdish لەنگ (leng)
- Pashto lang
- Sanskrit लङ्ग (laṅga, "lame")
- Armenian լանկ (lank) — a descendant form

The article cites Pokorny's 1959 *Indogermanisches etymologisches Wörterbuch* (Indo-European Etymological Dictionary) and Edelʹman's 2015 *Etymological Dictionary of Iranian Languages*.

## Etymology 2 (Towel/Loincloth)

This noun represents "a clipping of لنگوته (lungōta / longute)." It refers to "a traditional towel used after bathing."

**Related forms:**
- Tajik spelling: лунг (lung)
- Alternative form: لونگی (lōngī) in Tajik
- Descendants in Chagatai languages: Uyghur لۆڭگە (löngge), Uzbek lungi
```


## [2026-09-07T01:40:27.687Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BB%CE%AF%CF%84%CF%81%CE%B1",
 "prompt": "Give the full etymology of Ancient Greek λίτρα (lítra) verbatim: origin (Sicilian, relation to Latin libra, pre-Greek/Mediterranean substrate), meaning, and descendants (Latin, Aramaic, Arabic, French litre etc.). Also any note on Beekes."
}
```


## [2026-09-07T01:40:29.526Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B7%D9%84",
 "prompt": "Give the full Arabic etymology of رطل (raṭl / riṭl) verbatim: is it from Greek λίτρα via Aramaic/Syriac? which authorities are cited? meanings (unit of weight, vessel)? Also list Persian and other descendants."
}
```


### [2026-09-07T01:40:35.815Z] TOOL RESULT

```
# Arabic Etymology of رطل (raṭl/riṭl)

## Etymology Chain
The word traces back through Aramaic רִיטְלָא (rīṭlā) to Ancient Greek λίτρα (lítra). The entry notes an earlier Aramaic form לִיטְרָא (līṭrā) also deriving from the same Greek root.

## Authorities Cited
The references section lists:
- The Comprehensive Aramaic Lexicon Project (Hebrew Union College, Cincinnati, 1986–)
- Reinhart Pieter Anne Dozy's *Supplément aux dictionnaires arabes* (1881)
- Siegmund Fraenkel's *Die aramäischen Fremdwörter im Arabischen* (1886)

## Meanings
1. **Historical unit of dry weight**: "rottol, a historical Middle Eastern and North African unit of dry weight equal to 1–5 pounds (0.5–2.5 kg)"
2. **Modern meaning**: pound

## Selected Descendants
**English**: rottol, rotol, rotolo, rottolo, rattle (among others)
**Persian**: رطل (ratl, ritl)
**Italian**: rotolo
**Portuguese**: arrátel
**Spanish**: arrelde
**Swahili**: ratili
```


### [2026-09-07T01:40:36.023Z] TOOL RESULT

```
# Etymology of Ancient Greek λίτρα (lítra)

**Origin:**
The word was "borrowed from an Italic language," ultimately deriving from "Proto-Italic *līðrā ('ingot')." The immediate source may have been "Sicel *lītrā." This Italic term also survives in Latin *lībra*.

**Meaning:**
In Ancient Greek, λίτρα referred to two related concepts: a Sicilian silver coin, and a unit of weight (libra). A tertiary sense denoted a container for holding libras.

**Major Descendants:**
The term spawned extensive linguistic descendants across multiple language families:

- **Aramaic branches:** Classical Syriac *līṭrā*, Jewish Palestinian Aramaic *līṭrā*
- **Arabic:** *riṭl*, generating numerous European borrowings (English: rottol, rotol, rattle; Italian: rotolo; Portuguese: arrátel; Spanish: arrelde)
- **Romance languages:** Medieval Latin *litra* → French *litre* (with further descendants)
- **Other branches:** Old Armenian *litr*, Serbo-Croatian *litra/lȉtra*

**Beekes Reference:**
Robert S. P. Beekes' *Etymological Dictionary of Greek* (2010) confirms the Sicel borrowing hypothesis and provides comprehensive etymological documentation for this entry.
```


## [2026-09-07T01:40:54.187Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.vajehyab.com/?q=%D9%84%DB%8C%D8%B7%D8%B1",
 "prompt": "Does any Persian dictionary (Dehkhoda, Mo'in, Amid) have an entry for لیطر or لیطره? Quote whatever entries are shown verbatim, with the dictionary name."
}
```


## [2026-09-07T01:40:57.264Z] TOOL CALL #32: Bash

```json
{
 "command": "ls site/pages/314.jpg 2>/dev/null; pdftoppm -f 314 -l 314 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg314 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T01:40:57.800Z] TOOL RESULT

```
Based on the content provided, the Persian dictionaries shown have entries for **لیتر** (liter), not لیطر or لیطره:

**Dehkhoda Dictionary** includes:
"لیتر. (فرانسوی ، اِ) واحد حجم و اندازه گرفتن مایعات و آن معادل هزار گرم آب خالص چهار درجه حرارت است"

**Mo'in Dictionary** states:
"واحدی برای اندازه گیری آب برابر با یک کیلوگرم"

No entries for لیطر or لیطره are shown in this search results page.
```


### [2026-09-07T01:40:59.403Z] TOOL RESULT

```
site/pages/314.jpg
total 128
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 21:40 .
drwx------ 3 sfmqrb sfmqrb  4096 Sep  6 21:35 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   175 Sep  6 21:37 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     0 Sep  6 21:39 iec_pages.json
-rw-rw-r-- 1 sfmqrb sfmqrb 64584 Sep  6 21:40 pg314.png
-rw-rw-r-- 1 sfmqrb sfmqrb 49502 Sep  6 21:37 pg315.png
```


## [2026-09-07T01:41:01.711Z] TOOL CALL #33: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/314.jpg"
}
```


### [2026-09-07T01:41:01.735Z] TOOL RESULT

```

```


## [2026-09-07T01:41:21.240Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARB/AFM/DOZ ليطر ===\"; grep -n 'ليطر\\|لیطر\\|لیتر' ARB_mo3rb.txt ARB_abdulraheem.txt AFM_pages.txt PLA*.txt 2>/dev/null | head -10; ls | grep -i PLA; echo \"=== SYN lame ===\"; grep -n 'lame\\b' SYN.txt 2>/dev/null | head -8; ls | grep -i -E 'SYN|WLD'"
}
```


### [2026-09-07T01:41:21.319Z] TOOL RESULT

```
=== ARB/AFM/DOZ ليطر ===
(eval):1: no matches found: PLA*.txt
=== SYN lame ===
2087:Grk.. ¢aét Goth. - Lith. liepsna NG gorsya ON logi, leygr (poet.) Lett. lesma Lat. jlamma Dan. flamme, lue ChSl. plamy It. jiamma Sw. flamma, léga SCr. plamen Fr. flamme OE lieg Boh. plamen Sp. llama ME _leye, lowe, flamme Pol. plomicn Rum. flacdrd NE flame Russ. plamja Tr. lassar, breo Du. vlam Skt.  jvala-, cocis-, etc. Nir. air OHG loug Ay. *saocah- W. filam, ffagl MHG jflamme, lohe Br. mm NHG flamme (lohe)
2090:flamma, whence It. fiamma, Fr. flamme, Sp. llama, also, through Fr., ME flamme, NE flame, Br. flamm, or direct fr. Lat.(?) W. flam, Du. vlam, MHG, NHG flamme (> Dan. flamme, Sw. flamma).
2091:2. Rum. flacdré, fr. *flacula (It. fiaccola ‘torch’), this fr, Lat. facula ‘torch’ (dim. of fax id.) with / fr, flamma, flagrare. Cf. W. ffagl ‘blaze, flame, torch’ fr. Lat. facula. REW 3137.
2092:3. Ir. lassar, NIr. lasair (fr. *lap-s-) ; W. llachar ‘bright’, Grk. Adumw ‘shine’, OPruss. lopis ‘flame’. Lith. liepsna, Lett. liesma, fr. a parallel root *leip-. Walde-P. 2.383. Pedersen 1.75.
2099:Skt. ¢oczs-, coka-, Av.*saocah- (saoéah- in-, saocinavant- ‘flaming’) : Skt. cuc- ‘glow, flame’, etc. Walde-P. 1.378.
2163:Grk. ¢déyw, déyouar ‘blaze, burn’ b, gdéyw also ‘kindle’, or ‘burn’ a : dddé ‘flame’, Lat. flamma ‘flame’, flagrare ‘blaze’, etc. (1.82). Walde-P. 2.214.
2173:5. Ir. loscim, NIr. loiscim, W. Ulosgi, Br. leski, etym. dub. (fr. *lop-sk- : OPruss. lopis ‘flame’, Grk. Aduw ‘shine’,
2175:Ir. breoaim, deriv. of breo ‘flame’ (1.82).
SYN.txt
WLD_band3.txt
```


## [2026-09-07T01:41:22.265Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/liter",
 "prompt": "Quote the full etymology entries for liter/litre, and also whatever it says about libra, deliberate and equilibrium if shown. I mainly need liter/litre verbatim."
}
```


### [2026-09-07T01:41:27.343Z] TOOL RESULT

```
# Etymology of Liter

**Liter (noun):**
"Unit of capacity in the metric system, 1797, from French _litre_ (1793), from _litron_,

 name of an obsolete French measure of capacity for grain (16c.), from Medieval Latin _litra_, from Greek _litra_ "pound" (unit of weight), which apparently is from the same Sicilian Italic source as Latin _libra_"

**Libra (noun):**
The page describes it as a "zodiac constellation represented by a pair of scales" with roots in Latin _libra_ meaning "a balance, pair of scales," also "pound (unit of weight)," ultimately deriving from Proto-Italic _*leithra-_.

**Note:** The page content does not include entries for "deliberate" or "equilibrium," so those etymologies are not available to quote from this source.
```


## [2026-09-07T01:41:36.267Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN LAME ===\"; grep -n -i '^4\\.92\\|4\\.92 LAME\\|LAME$\\|LAME ' SYN.txt | head -10; echo \"=== SYN pound/libra ===\"; grep -n 'libra ‘\\|libra,' SYN.txt | head -5; echo \"=== WLD3 ===\"; grep -n 'laṅga\\|langa\\|sleg\\|(s)leg' WLD_band3.txt | head -10"
}
```


### [2026-09-07T01:41:38.590Z] TOOL RESULT

```
=== SYN LAME ===
696:Rain (sb.) Snow (sb.) Icz WEATHER Fire FLAME (sb.) SMoKE (sb.) ASHES Burn (vb.)
2086:oganj) : Ukr., Boh. dial. vatra, Pol. dial. | KZ 56.125. 1.82 FLAME (sb.)
2087:Grk.. ¢aét Goth. - Lith. liepsna NG gorsya ON logi, leygr (poet.) Lett. lesma Lat. jlamma Dan. flamme, lue ChSl. plamy It. jiamma Sw. flamma, léga SCr. plamen Fr. flamme OE lieg Boh. plamen Sp. llama ME _leye, lowe, flamme Pol. plomicn Rum. flacdrd NE flame Russ. plamja Tr. lassar, breo Du. vlam Skt.  jvala-, cocis-, etc. Nir. air OHG loug Ay. *saocah- W. filam, ffagl MHG jflamme, lohe Br. mm NHG flamme (lohe)
8131:4.94 LAME Grk. _ xwAds Goth. halts Lith. raiSas, Slubas NG xourcés ON halir (lami) Lett. _tizls, klibs, slums Lat.  claudus Dan. halt, lam ChSl. chromit It. zoppo, ranco Sw. halt, lam SCr. — hrom, Sepav Fy. botteur OE healt (lama) Boh. chromy, kulhavy yy Sp. cojo ME shalt, lame Pol. chromy, kulawy Rum.  schiop NE lame (halt) Russ. chromoj Ir. bacach, losc Du. kreupel, lam, mank Skt. grona-, srama-, pai- NIr. — bacach OHG _halz (lam) gu-, ete. W. cloff MHG lam, halz, hinlende Av. By hhe Br. kamm NHG  lahm, hinkend
8133:They are from diverse notions such as ‘break, bend, twist’, some from the name of a part affected (as ‘hip’), some prob- ably of imitative origin (from the clump- ing sound of a lame person), several quite obscure.
12096:i lal ea a Lett. krésls Ne lame Dan. _ stol ChSl.  sédali3te Ink. sella eels iS} tol SCr stolica ba gd a Ob sial Boh.  sedadlo, stolice Sp. silla ME stole, chatre Pol. krzesto Rum. scaun NE chair Russ. stul I, —_cathair Du. __ stoel Skt. —_ pitha- Nir, cathaoir OHG - stuol Av. (gatu-) W. — cadair MHG §stuol Br. kador NHG - stuhl
15534:ogy), deriv. of vaso ‘vase, pot’ (also vasel- lo, whence vasellame ‘pottery’), Lat. vasum.
17442:Grk. zepuraréw ‘walk about, walk up and down’, later simply ‘walk’ (cf. NT, Mt. 11.5 ‘the lame walk’), NG. pop. meprare, epd. of raréw ‘tread, trample’ : maros ‘path’, Skt. pantha-, ChSl. patt ‘way’, etc. Walde-P. 2.26.
29893:16.78 BLAME (sb.)
29894:Grk. — poudi, dvedos, Yoyos, Goth. fairina (vb. faian) Lith.  (pa)peikimas p&pos ON [ast Lett. pala — NG karnyopla (uoudn, Dan. dadel ChSl.  (zaztréti, vb.) ¥oyos) Sw. — tadel SCr. _prijekor Lat. —_reprehénsio, vilupera- OE tal, tal Boh. hana : to ME blame Pol. nagana li, It. biasimo NE blame, reproach Russ. chula, poricanie Fr. blame, reproche Du.  blaam Skt.  ninda-, garha-, Sp. censura, reproche OHG | lastar parivada- Run. blam MHG aster (tadel) Av. .. Ir. care NHG tadel, vorwurf NIr. —millean W. bat Br. tamall
=== SYN pound/libra ===
=== WLD3 ===
```


## [2026-09-07T01:41:38.742Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BB%CF%8C%CE%B3%CE%B3%CE%BF%CF%82",
 "prompt": "Give the etymology and meaning of Greek λόγγος (lóngos). Is it Modern Greek? Is it a borrowing from Slavic (*lǫgъ)? Quote verbatim."
}
```


### [2026-09-07T01:41:43.912Z] TOOL RESULT

```
# Etymology and Meaning of λόγγος (lóngos)

**Meaning:** The word means "dense and bushy forest, grove" in Greek.

**Etymology:** Yes, it is a borrowing from Slavic. According to the source: "Inherited from Byzantine Greek _λόγγος_ (lóngos), from Proto-Slavic _\*lǫ̑gъ_ ('[depression](/wiki/depression "depression"), [meadow](/wiki/meadow "meadow"), [valley](/wiki/valley "valley")')."

**Modern Greek Status:** The entry is categorized under Modern Greek, as indicated by the reference to "Dictionary of Standard Modern Greek" and the article's classification system.

The word traveled from Proto-Slavic into Byzantine Greek, eventually becoming part of the modern Greek lexicon with a meaning that evolved from the original Slavic concept of a depressed or low-lying area to specifically denote a wooded space.
```


## [2026-09-07T01:41:56.118Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor L in [476,482,723]:\n    s=leaves[L]\n    print('#### leaf',L,'len',len(s))\n    print(repr(s[:200]))\n    print('...tail:',repr(s[-200:]))\nEOF"
}
```


## [2026-09-07T01:41:57.132Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/deliberate",
 "prompt": "Quote the etymology of \"deliberate\" verbatim, including the Latin deliberare, de- + librare/libra \"scales, balance\" chain and any note about confusion with liber \"free\"."
}
```


### [2026-09-07T01:41:57.438Z] TOOL RESULT

```
#### leaf 476 len 11415
"colog-ic-al,  adjs., lexicolog-ist ,  n.\nlexicon,  n.,  a  dictionary.  —  Gk.  Xei;tx<5v  (scil. |3t|3Xlov),  ‘dictionary’,  lit.  ‘book  of  words, neut.  of  XeEiv.'k,  ‘pertaining  to  words’,  fr"
...tail: 'at’  (F.  lecher,  ‘to  lick’,  is  a  Teut.  loan  word), from  the  I.-E.  imitative  base  *leigh-,  whence  also OI.  ledht,  redid,  also  (a  later  form)  lihati,  ‘he licks’,  Avestic  raez-, '
#### leaf 482 len 11907
'viate,  prolix. Derivatives:  liquid,  n.,  liquidate  (q.v.),  liquid-ly, adv.,  liquid-ness,  n.\nLiquidambar,  n.,  a  genus  of  trees,  the  sweet  gum tree  (bot.)  —  A  ModL.  hybrid  coined  f'
...tail: 'it. ‘writing  on  stone’,  compounded  of  litho-  and Gk.  -ypaipta,  fr.  yp&petv,  ‘to  write’.  See -graphy.\nDerivatives:  lithograph-ic,  adj.,  lithograph-ic-al- ly,  adv.\nlithoid,  adj.,  stone'
#### leaf 723 len 11441
' rumpere,  ‘to  break’.  See  route  and  cp.  rut, ‘routine’.  For  sense  development  cp.  F.  routine, ‘practice,  routine’,  fr.  route,  ‘way’  (see  routine), rote,  n.,  a  medieval  stringed '
...tail: 'robbery  ( obsol .)  —  Back formation  fr.  rover,  ‘sea  robber’, rove,  1)  intr.  v.,  to  shoot  at  random;  2)  intr.  v., to  wander  about  aimlessly;  tr.  v.,  to  wander over.  —  ME.  rov'
```


### [2026-09-07T01:42:03.749Z] TOOL RESULT

```
# Etymology of "Deliberate"

**Adjective (early 15c.):**
"done with careful consideration," from Latin *deliberatus*, past participle of *deliberare* meaning "consider carefully, consult," literally "weigh well." The word breaks down as: *de-* (entirely) + *-liberare*, altered from *librare* "to balance, make level," which derives from *libra* "pair of scales, a balance."

**Verb (1540s):**
Similar origin: "weigh in the mind, consider carefully" from Latin *deliberare*, with the same etymological breakdown involving the scales/balance concept.

**Note on semantic evolution:**
The meaning "characterized by slowness in decision, consciously unhurried" appears by the 1590s, showing how the original sense of careful weighing evolved into describing deliberate slowness.

The webpage notes that *-liberare* was probably influenced by *liberare* "to free, liberate," though the primary root traces to the balance/weighing metaphor rather than the freedom concept.
```


## [2026-09-07T01:42:18.195Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor L in range(474,486):\n    s=leaves[L]\n    nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$', s)\n    nums2=re.findall(r'\\b(8[5-9]\\d|9[0-2]\\d)\\b', s)\n    print(L, 'standalone:',nums, 'inline:',nums2[:8], '| first words:', s[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T01:42:19.485Z] TOOL RESULT

```
474 standalone: ['882', '883'] inline: ['882', '883'] | first words: nless. Derivatives:  less,  adv.  and  n.,  lessen,  lesser 
475 standalone: [] inline: [] | first words: ��to  flow’.  See  -rrhea. Leucothoe,  n.,  the  daughter  o
476 standalone: [] inline: [] | first words: colog-ic-al,  adjs., lexicolog-ist ,  n. lexicon,  n.,  a  d
477 standalone: ['888'] inline: ['888'] | first words:  ‘to  lick’.  Arm.  lizum, lizem,  lizanem,  ‘I  lick’,  lak
478 standalone: ['889'] inline: ['889'] | first words: by lamplight’,  liicus,  ‘grove,  thicket’  (orig.  'an  ope
479 standalone: ['890', '891'] inline: ['890', '891'] | first words: —  L.  Umax,  gen.  -acis,  ‘slug,  snail’,  fr.  Gk.  Xsi- 
480 standalone: ['892', '893'] inline: ['892', '893'] | first words: usine,  n.,  a  large  automobile,  orig.  with  a closed  c
481 standalone: [] inline: [] | first words: � L.,  ‘a  little  tongue’,  dimin,  of  lingua,  ‘tongue’. 
482 standalone: ['897'] inline: ['897'] | first words: viate,  prolix. Derivatives:  liquid,  n.,  liquidate  (q.v.
483 standalone: ['898', '899'] inline: ['898', '899'] | first words: like.  —  Gk.  XtfloeiSrjp,  ‘like  a stone’,  compounded  o
484 standalone: ['900', '901'] inline: ['900', '901'] | first words:   cp.  delivery. Derivative:  liveri-ed,  adj. livery,  adj.
485 standalone: ['902', '903'] inline: ['902', '903'] | first words: ri,  ‘to wrestle,  struggle,  strive,  contend’,  lit.  ‘to
```


## [2026-09-07T01:42:40.719Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD sleg/lax/languid ===\"; grep -n -i '^sleg\\|^(s)leg\\|slēg\\|LANGUID\\|LAX\\b' AHD_watkins1985.txt | head -10; echo \"=== AHD lithra full ctx ===\"; sed -n '698,702p' AHD_watkins1985.txt; echo \"=== WLD3 leg ===\"; grep -n 'II 712\\|laṅga' WLD_band3.txt | head -5; echo \"=== HUB litra/ratl ===\"; grep -n 'ratl\\|litra' HUB.txt HRN.txt | head"
}
```


### [2026-09-07T01:42:40.810Z] TOOL RESULT

```
=== AHD sleg/lax/languid ===
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
594:keg-. Hook, tooth. 1. Germanic *hakan- in: a. Old Norse haki, hook, akin to Old English haca, hook: HAKE; b. Middle Low German hake, hook: HARQUEBUS. 2. Ger- manic lengthened form *Adka- in: a. Old English héc, hook: HOOK; b. Middle Dutch hok, hoec, hook: HOOKER}. 3. Germanic *hakila- in Middle Dutch hekel, hatchel, a flax comb with long metal hooklike teeth: HECKLE. 4. Germanic *hakkijan in Old English -haccian, to hack to pieces as with a hooked instrument: Hack!. [Pok. keg- 537.]
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
699:lino-. Flax. 1. Form */ino- in Greek linon, flax: LINOLEIC ACID. 2. Form */ino- in Latin linum, flax, linen: LINE}, LINE?, LINEN, LINGERIE, LININ, LINNET, LINT; CRINO- LINE, LINSEED. [Pok. /i-no- 691.]
851:[phulax. Watcher, guard. Greek noun of unknown origin, related to phulassein (Attic phulattein), to guard, pro- tect. PHYLACTERY, PHYLAXIS; PROPHYLACTIC. ]
858:plak-'. Also plak-. To be flat. Extension of pele-2. 1. Germanic *fléh6 in Old Norse fl6, layer, coating: FLOE. 2. Variant form *pldg- in: a. Germanic *flék- in Old English fléc, flatfish: FLUKE!; b. Germanic *flakaz in Norwegian flak, flat piece, flake, probably akin to the Scandinavian source of Middle English flake, flake: FLAKE}; c. Germanic *flak- in Old Norse flaki, fleki, hurdle: FLAKE?. 3. Extended form *plakd in Germanic *flag6 in Old Norse flaga, layer of stone: FLAG, FLAW}. 4. Possibly suffixed (stative) form *plak-é-, to be calm (as of the flat sea), in Latin placére, to please, be agreeable: PLACEBO, PLACID, PLEA, (PLEAD), PLEASANT, PLEASE; COMPLACENT. 5. Lengthened suffixed form *plak-G- in Latin placdre, to calm (causative of placére): PLACABLE, PLACATE. 6. Nasalized form *pla-n-k- in Latin plancus, flat, flat-footed, whence planca, board: PLANCHET, PLANK, PLANK-SHEER. 7. Variant form *plag- in: a. perhaps Latin plaga, net (? < “something ex- tended”): PLAGIARY; b. Greek plagos, side: PLAGAL, PLAGIO-, PLAYA. 8. Root form *plak- in Greek plax, flat, flat land, surface: PLACENTA, PLACOID. 9. Variant form *pelag- in Greek pelagos, sea: PELAGIC; ARCHIPELAGO. [Pok. 1. pla-k- 831.]
862:flad6, flat cake, pancake: FLAN. 4. Germanic nasalized suffixed form *flu-n-th-r-j6- in Old Swedish flundra, flatfish, flounder, probably akin to the Scandinavian source of Middle English flounder, flounder: FLOUNDER?. 5. Nasalized form *pla-n-t- in Latin planta, sole of the foot, and denominative plantdre, to drive in with the sole of the foot, plant, whence planta, a plant: CLAN, PLAN, PLANT, PLANTAIN!, PLANTAR; PLANTIGRADE, SUPPLANT. 6. Suffixed form “plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE‘, (PLANE TREE), PLATE, (PLATEAU), (PLATITUDE), (PLATY?), PLATY-, (PLAZA). [Pok. plat- 833.] [plegan. To pledge for, stake, risk, exercise oneself. West Germanic verb. 1. Old English plegian, to exercise one- self, play: PLAY. 2. Late Latin plevium (> Old French plevir, to pledge), pledge, guarantee: PLEDGE; REPLEVIN. 3. Germanic derivative noun *plehti- in Old English pliht, danger, peril: PLIGHT?.] plek-. To plait. Extension of pel-*. 1. Suffixed o-grade form *plok-so- in Germanic *flahsam, flax, in Old Eng- lish fleax, flax: FLAX. 2. Full-grade form *plek- in Latin -plex, -fold (in compounds such as duplex, twofold; and supplex, “with legs folded under one,” kneeling, entreat- ing; see dwo-, upo): MULTIPLEX, QUINTUPLE, SUPPLE. 3. Latin plicdre, to fold (also in compounds used as denominatives of words in -plex, genitive -plicis): PLAIT, PLIANT, PLICA, PLICATE, PLIGHT!, PLISSE, PLY!; APPLY, COMPLICATE, COMPLICE, DEPLOY, DISPLAY, EMPLOY, EXPLICATE, IMPLICATE, REPLICATE, SUPPLICATE. 4. Suf- fixed forms “plek-to- and *plek-t-to- in Latin plectere (past participle plexus), to weave, plait, entwine: PLEACH, PLEXUS; AMPLEXICAUL, COMPLECT, (COMPLEX), PERPLEX. 5. Greek plekein, to plait, twine, and plektos, twisted: PLECOPTERAN, PLECTOGNATH. [Pok. plek- 834.] plék-. Also pleik-. To tear. 1. Zero-grade form *pbk- becoming *plak- in Germanic *flahan in Old English fléan, to strip the skin from: FLAY. 2. Suffixed o-grade form “ploik-sk- perhaps in Germanic “flaiskjan, piece of flesh torn off, in Old English flésc, flesh: FLESH. 3. Zero-grade form *plik- in Germanic *flikkja in: a. Old English flicce, side of a hog: FLITCH; b. Germanic ablaut form *flekkja in Old Norse flekkr, piece of skin or flesh, spot, stain: FLECK. [Pok. plék- 835.] pleu-. To flow. I. Basic form “pleu-. 1. Latin pluere, to rain: (PLOVER), (PLUVIAL), PLUVIOUS. 2. Greek pleusis, sailing: PLEUSTON. 3. Suffixed zero-grade form *plu-elos dissimilated into Greek puelos, trough, basin: PYELITIS. 4. Suffixed form *pl/(e)u-mon-, ‘‘floater,” lung(s), in: a. Latin pulmé (< *plumonés), lung(s): PULMONARY; b. Greek pleumén, pneumon, lung: PNEUMONIA, PNEU- MONIC. 5. Suffixed o-grade form *plou-to- in Greek plou- tos, wealth, riches (< ‘‘overflowing’’): PLUTO; PLUTOCRACY. 6. Lengthened o-grade form *pl6(u)- in: a. Germanic *fléwan, to flow, in (i) Old English flowan, to flow: FLOW (ii) perhaps Middle Dutch vluwe, fishnet: FLUE?; b. suffixed form *pld-tu- in Germanic *fléduz, flowing water, deluge, in Old English fléd, flood: FLOOD. II. Extended form *pleuk-. 1. Germanic *fleugan, to fly, in Old English fléogan, to fly: FLY!. 2. Germanic *fleu- gon-, flying insect, fly, in Old English fléoge, a fly: FLY?. 3. Probably Germanic *fleuhan, to run away, in Old English fléon, to flee: FLEE. 4. Germanic causative *flauhjan in Old English flygan, flégan, to put to flight: FLEY. 5. Germanic suffixed form *fleug-ika in Old French fleche, arrow: FLECHE, FLETCHER. 6. Zero-grade form *pluk- in: a. Germanic *flugja-, feather, in Old English -flycge, with feathers (only in unfligge, featherless): FLEDGE; b. suffixed form *flug-ti- in Old English flyht, act of flying, and *flyht, act of fleeing, escape: FLIGHT, FLIGHT?; Cc. possibly (but unlikely) suffixed form *flug- laz, dissimilated into *fuglaz, bird, in Old English fugol, bird: FowL; d. Germanic suffixed form *flug-ila in Mid- dle High German viiigel (> Germanic Fliigel), wing: FLUGELHORN, FUGLEMAN. III. Extended form *pleud-.
914:sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
953:slég-. To be slack, be languid. Possibly related to sléb- through a hypothetical base *slé- (< *slea-). Zero-grade form *(sjlag-, becoming *(s)lag-. 1.Germanic *slak- in Old English sizc, “loose,” indolent, careless: SLACK}. 2. Suffixed form *lag-so- in Latin laxus, loose, slack: LAX; DELAY, RELAX, RELAY. 3. Suffixed nasalized form *la-n-g-u- in Latin languére, to be languid: LANGUISH. 4. Compound */ag-ous-, “with drooping ears” (*ous-, ear; see ous-), in Greek lagés, lagos, hare: LAGOMORPH.
1519:FLAW! piak-" FLAX plek- FLAY plék- FLEA plou- FLECHE pleu-
=== AHD lithra full ctx ===
[lik-. Body, form; like, same. Germanic root. 1. Old English lic, form, body: LICH GATE. 2. Old English -lic, having the form of: -LyY!}, -Ly?. 3. a. Germanic *galikaz in Old English gelic, similar: ALIKE, LIKE?; b. Germanic phrase *aiwo galikaz, “ever alike” (*aiwo, *aiwi, ever; see aiw-), in Old English #lc, each: EACH. 4. Germanic *is-lik in Old English ilca, the same (see i-). 5. Old Norse likr, like: LIKELY. 6. Middle Dutch -lijc, -ly: FROLIC. 7. Germanic *likjan in Old English lician, to please: LIKE!, 8. Germanic *hwa-lik-, which (see k’o-). [In Pok. 2. leig- 667.]]
lino-. Flax. 1. Form */ino- in Greek linon, flax: LINOLEIC ACID. 2. Form */ino- in Latin linum, flax, linen: LINE}, LINE?, LINEN, LINGERIE, LININ, LINNET, LINT; CRINO- LINE, LINSEED. [Pok. /i-no- 691.]
[lithra. A scale. Mediterranean word. 1. Probably Latin libra, a pound, balance: LEVEL, LIBRA, LIRA, LIVRE; DELIBERATE, EQUILIBRIUM. 2. Probably Greek /itra, unit of weight, pound: LITER.]
lds-. Louse. Germanic */is- in Old English Jas, louse: Louse. [Pok. liis- 692.]
ma-'. Good; with derivatives meaning “occurring at a good moment, timely, seasonable, early.” 1. Suffixed form *md-tu- in: a. further suffixed form *md-tu-ro- in Latin mdatirus, seasonable, ripe, mature: MADURO, MA-
=== WLD3 leg ===
=== HUB litra/ratl ===
HUB.txt:1177:auf = * wider den Strom'? Vgl. skr. pratlpdm gegen
HUB.txt:1178:den Strom*, pratlpd- Viderspanstig, Gegner, Wider-
HRN.txt:6846:des Erdteils, die Euphratländer, Persien, Palästina
```


## [2026-09-07T01:42:44.772Z] TOOL CALL #42: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CE%BB%CE%AF%CF%84%CF%81%CE%B1' --note 'page 314, root Lithra: Ancient Greek litra, Sicel/Proto-Italic *lithra, descendants Aramaic/Arabic ritl, ML litra, French litre' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%D8%B7%D9%84' --note 'page 314, node 6/7: Arabic ratl < Aramaic ritla < Greek litra; Persian ratl descendant' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/liter' --note 'page 314, nodes 2-5: liter < Fr litre < litron < ML litra < Gk litra, same Sicilian Italic source as Latin libra' 2>&1 | tail -3"
}
```


### [2026-09-07T01:42:47.248Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d9759aec9cc88b52.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b8d6c10e73343168.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f643c8e1332542b3.txt
```


## [2026-09-07T01:43:07.233Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%84%D9%86%DA%AF' --note 'page 314, entry Longos node 1: Persian lang < Proto-Iranian *langa- < PII *langa- < PIE *(s)leh1g-, Pokorny 1959, Edelman 2015' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CE%BB%CF%8C%CE%B3%CE%B3%CE%BF%CF%82' --note 'page 314, entry Longos node 3: Greek loggos is a Byzantine/Modern Greek borrowing from Proto-Slavic *longu, not an IE inheritance' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/deliberate' --note 'page 314 node 8/9: Latin deliberare < de- + librare < libra scales' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://www.vajehyab.com/?q=%D9%84%DB%8C%D8%B7%D8%B1' --note 'page 314 node 7: no Persian dictionary entry for لیطر; Dehkhoda/Moin have only لیتر marked فرانسوی' 2>&1 | tail -2"
}
```


## [2026-09-07T01:43:08.854Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%99%E0%A5%8D%E0%A4%97",
 "prompt": "Give the Sanskrit entry for लङ्ग (laṅga): meaning, etymology, whether it means \"lame\", and any cited authority (Monier-Williams, Pokorny, Turner). Quote verbatim."
}
```


### [2026-09-07T01:43:09.924Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b7bf95e8b8c38713.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/55b928e5a659f1c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d980c1bec79a87f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aaab596eec8a3e75.txt
```


### [2026-09-07T01:43:16.377Z] TOOL RESULT

```
# Sanskrit Entry: लङ्ग (laṅga)

**Meaning:** The word functions as both an adjective and noun. As an adjective, it means "limping, lame." As a noun (masculine), it denotes "limping, lameness."

**Etymology:** The entry states it derives from "Proto-Indo-European *(s)leh₁g- (weak, feeble)." Related cognates include Latin *langueo* and English *slack*.

**Authority Citations:**

The Monier-Williams Sanskrit-English Dictionary (1899) is cited as a reference source. Additionally, the page references Mayrhofer's *Etymologisches Wörterbuch des Altindoarischen* (2001) and Turner's *Comparative Dictionary of the Indo-Aryan Languages* (1969–1985).

**Direct Quote on Meaning:**
"limping, lame" (adjective definition) and "limping, lameness" (noun definition)
```


## [2026-09-07T01:43:20.960Z] TOOL CALL #45: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%99%E0%A5%8D%E0%A4%97' --note 'page 314 entry Longos node 2: Sanskrit langa \"limping, lame\" < PIE *(s)leh1g-, Monier-Williams/Mayrhofer/Turner' 2>&1 | tail -2; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T01:43:22.600Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/79139d84f31a704e.txt
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


## [2026-09-07T01:43:57.502Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK libra/lithra ===\"; grep -n 'lithra\\|libra ‘\\|Latin libra' POK_full.txt | head -5; echo \"=== SKT litre/libra ===\"; grep -n -i 'litre\\|^Libra\\|Libra,\\|equilibrium' SKT.txt | head -8; echo \"=== FSD liter ===\"; grep -n -i 'litra\\|Gr. litra' FSD_vol3.txt FSD_vol2.txt 2>/dev/null | head -5"
}
```


### [2026-09-07T01:43:57.844Z] TOOL RESULT

```
=== POK libra/lithra ===
=== SKT litre/libra ===
5933:equilibrium,  even  balancing.  (L.)  U o^uiN^Him.  —  L.  aquilibris^  evenly balanced.  —  L.  tttfui-^  lor  iryuHt,  even ;  /i- ico/v.  to  balanoe ;  sec  Llbrete.
5947:Equilibrium:  sec  Equal.
10239:LIBRARY, feeblement,  ignorance,  baseness,  U
10256:Library.  ^F.  -  L.)  F.  Htfmni-  • Hbran'a,  a  hook-shop :  firm,  tt  tih^ belonging  to  bocks.  — L./i^*-.  stem  <4l a    book,   ong.   the    t«ik    oi  a  tne
10257:LIBRATE.
10274:  wcitjh.  from  libra,  a  balance.
17770:•ou.  <F.  -  L.)    F.  torn.  O.  F.  mI,  t —  Low  L.  solidvs,  solid,  also  a  ecu /.  /.  d.,  L  e.  libra,  soiidi^  denarii. Soliloquy ;  see  LoQuaotoua. Soliped :  see  Solid. Solitary.  Solitude,   Solo ;  Me  H (.^). Solmisation  ;  aee  Solfa. Solstice;  see  Solar Soluble,  Solution  ;  sec  Batra. Solve.  iL  )     L.  solurwt,  lo  loosot.  rri ex.pUiD  :  pp.  Wu/mj— L.r^,  fo(  «-.t{fl imerty  to  looscu,  allie*!  to  t-ik.  Av-«ir.  tv free,  and  to  E.  Ijose.     Der.  t^StM.  b the  htein  of  (he  prcs.  pt.
=== FSD liter ===
FSD_vol3.txt:113607:Clraptulitra, ')
FSD_vol3.txt:214860:ancient strata r.«proof, a Proof against th«> I'litrariee
FSD_vol3.txt:214905:It^, a llu\ing no ralitrali
FSD_vol3.txt:221604:aaJ add dJ if alwvii O ' It ami il bnlnw aiilitrarl tJ
FSD_vol2.txt:74946:Tbench  On  the  Miracles  p.  17(5.  [a.  1853.1 3.  [Rare.]  A   leper»house.  3.  Figuratively,  any  defile- ment or  disease  in  the  moral  order;  as,  idleness  is  a   moral leprosy.  [<  OF.  leprosie,  <   Gr.  leprosis,  <   lepra;  see LEPER.]  —   anesthetic  iepro-sy*  a   common  kind  of  tropical leprosy,  caused  by  the  Invasion  of  the  nerves  by  the bacilli,  thus  causing  peripheral  neuritis,  and  subsequent loss  of  sensation  in  areas  of  the  skin  and  underlying  tissues. There  is  an  eruption  of  reddish  or  purplish  spots  preceded  by itching  and  numbness:  in  time  blisters  form  and  break,  the muscles  of  the  hand  become  atrophied,  and  the  bones  be- come necrotlts,  while  often  a   hand  or  foot  falls  oft.—  Italian 1.,  pellagra.— tubercular  or  nodular  1.,  leprosy  charac- terized by  red  areas  that  develop  into  nodules  composed  of tubercular  grauulatlon*tlssue  or  diffuse  inilitration  of  the ,   cuticle,  whence  mutilation  and  distortion  often  result.  The earliest  symptom  is  an  eruption  of  reddish  patches,  and  in time  an  eruption  occurs  on  the  face,  where  the  tumorous masses  and  horizontal  furrows  cause  an  appear.anoe  that  has been  likened  to  the  face  of  a   lion.  See  bsoNxiASis. lep'rous,  1   lep'rua;  2   ISp'rtis,  a.  Pathol.  1.  Relating  to, affected  with,  or  resembling  lepros.v;  unclean;  foul.  3. Scale«lilce;  covered  with  scales.  3t*  Causing  leprosy. [OB’.,  <   LL.  leprosus,  <   L.  lepra;  see  leper.]  —   Icp'rous-ly, adv.—  lep'rou.s-ncss,  n.
```


## [2026-09-07T01:43:59.363Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT ratl v2 ===\"; grep -n 'رطل' BQT_v2_pages.txt | head -5; echo \"=== SOD ===\"; grep -n 'lang' SOD.txt | head -3; echo \"=== HJB ratl/rottle ===\"; grep -n -i 'rottle\\|ratl' HJB.txt | head -5"
}
```


### [2026-09-07T01:43:59.445Z] TOOL RESULT

```
=== BQT ratl v2 ===
8962: ‫خارخار » خلحان وتعاق خاطر و اندشه که صمر آدمی برطلب و کنجکاوی دارد‬                                          ‫‪- ۷‬‬
11258:    ‫‏‪ ٩‬خرطال (بضم اوز) = خرطل (بضم اول وفتح سوم وچهارم مشدد) = کرطان‬
23932:                                ‫مثك ریز ک‬                     ‫خزبده اکنون برزهه» می‌بده اکنون برطل‬
24404:                        ‫رطل مت ‪-‬‬                     ‫*‪ #‬رطب وش دادن اه کنابه از‬
24428:           ‫که خانقاه ندارد ي‬      ‫شادی شحی‬                ‫‪ - ۱‬رطل گرانم ده ای مربد خرابات‬
=== SOD ===
894:12.  Bazin,  L.   Turks  et  SogdicnstM  Melanges  Linguistiques 
3595:spellings  of  each  term,  finding  cognates  in  sister  languages,  and  utilizing  information 
3791:or  languages  kin  to  Sogdian,  thv  respective  original 
=== HJB ratl/rottle ===
804:Soc.    Ed.  by  C.  Markham.    1878. Heber,    Bp.    Beginald.      NazratlTe   of   a
2084:1588.— "Neel,  the  churle  70  duckats,  and a  churle  is  27  rottles  and  a  half  of  Aleppo." —Mr  John  Newton,  in  Bail.  ii.  878.
4986:Moodeen  Sheriff  says  that  Jedfitr  is used  (in  Ind.  Materia  Medica)  for <  amber.'  Tdhasklr  (see  TABASHEEB), is,  according  to  the  same  writer,  called hdm-kdfur  *  bamboo  -  camphor ' ;  and ras-kafilr  (mercury-camphor)  ^  is  an impure  subchloride  of  mercury.  Ac- coming  to  the  same  authority,  the varieties  of  camphor  now  met  with in  the  bazars  of  S.  India  are— 1.  MfUr- i-iaifuriy  which  is  in  Tamil  called pach^iJi'ai  {i,e,  crude  kamppuram;  2. Mratl  kdfar;  3.  cklnl;  4.  haiai  (from the  BaJtta  country?).  The  first  of these  names  is  a  curious  instance  of  the perpetuation  of  a  blunder,  originating m  the  misreading  of  loose  Arabic writing.  The  name  is  unquestionably •anfMrl,  which  carelessness  as  to  points
6943:1510.— "The  Governor  (Alboquerque)  .  .  . in  Cananor  devoted  much  care  to  the  pre- paration of  cables  and  rigging  for  the  whole fieet,  for  what  they  had  was  all  rotten  from the  rains  in  Goa  River;  ordering  that  all should  be  made  of  ooir  (cniro),  of  which  there was  great  abundance  in  Cananor ;  because  a Moor  called  Mamalle,  a  chief  trader  there, held  the  whole  trade  of  the  Maldive  islands by  a  contract  vrith  the  kinss  of  the  isles  .  .  . so  that  this  Moor  came  to  be  called  the  Lord •of  the  Maldives,  and  that  all  the  coir  that  was used  throughout  India  had  to  be  bought  from the  hands  of  this  Moor.  .  .  .  The  G^ovemor, learning  this,  sent  for  the  said  Moor,  and ordered  him  to  abandon  this  island  trade and  to  recall  his  factors.  .  .  .  The  Moor, not  to  lose  such  a  profitable  business,  .  .  . finally  arranged  with  the  Qovemor  that  the Isles  should  not  be  taken  from  him,  and that  he  in  return  would  furnish  for  the  king 1000  haharg  {baria)  of  coarse  coir,  and  1000 more  of  fine  coir,  each  hahar  weighing  4) ^intals;  and  this  every  year,  and  laid  down at  his  own  charges  in  Cananor  and  Cochym, ffratlB  and  free  of  all  charge  to  the  King  (not being  able  to  endure  that  the  Portuguese should  frequent  the  Isles  at  their  pleasure)." —Correa,  ii.  129-80.
10755:[1809.— "  Seendhiya  was  seated  nearly  in the  centre,  on  a  large  square  cushion  covered with  TOld  brocade  ;  his  back  supported  by  a round  bolster,  and  his  arms  resting  upon two  flat  cushions  ;  all  covered  with  the  same costly  material,  and  forming  together  a  kind of  throne,  called  a  musnud,  or  guddee."— Brougktofiy  Letters  from  a  Mahratla  Camp. ed.  1892,  p.  28.]
```


## [2026-09-07T01:44:07.502Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24398,24435p' BQT_v2_pages.txt; echo \"--- page tag:\"; awk 'NR<=24435 && /\\[pdf page/ {p=$0} END{}' BQT_v2_pages.txt >/dev/null; grep -n '\\[pdf page' BQT_v2_pages.txt | awk -F: '$1<24435' | tail -2"
}
```


### [2026-09-07T01:44:08.745Z] TOOL RESULT

```
               ‫مکطزیمان حضرت شاهم ‪.‬‬                       ‫‪ - ۷‬من رئیس فلان رصد کاحم‬
   ‫کاتمیجوی« کنجینه ‪. ۳۷۰‬‬‫نظ‬
                                         ‫يبان سیز دهم‬
                                 ‫در رای یاو‬
‫کناءه‪ ۱‬زیباله ویمالٌ‬
                        ‫رطل مت ‪-‬‬                     ‫*‪ #‬رطب وش دادن اه کنابه از‬



                                        ‫يان چهار دهم‬

 ‫و ببشتر مردم بدخشان و بعضی از مردم کشمیر‬           ‫انی ‪۰,‬‬   ‫سکون‬      ‫اول و‬   ‫ین‬   ‫‪ ۲‬ه‬     ‫رع‬    ‫*‬

                                            ‫وا‬       ‫آروغ راگویند » وآن بادی است که با صدا از‬
 ‫رغوان ‪ -‬باواوبالف کشیده بنون زده‬                                                   ‫راه کلو مرها بد ‪۰‬‬


 ‫وحرکت اول عجهول » دکاموهی است درمغرب‬                  ‫رغث س بنتحاسولکوون ثالی و ا‬
                             ‫تزديك بافربقیه ‪. ۴‬‬      ‫اناری است‬       ‫و آن گل درخت‬     ‫‪۰‬‬    ‫مثلثه کلنار ات‬

‫سه‌ود آ ‪ ۰‬بلفت سربالی‬    ‫مروزن‬   ‫ر غیدا ‌‬            ‫که بغیر از کل ثمری دیگر ندارد ‪ .‬وبهترین‌آن‬
 ‫کنن ‪ ۴‬که آترا بشهرازی‬           ‫دانه است ان‬                                              ‫کلنار فارسی ناش‬

 ‫کف‬        ‫و‬            ‫هر گوبند بفتح ها کت‬           ‫رغزه = بر وزن سبزه " پتو گروایند‬
                                       ‫هربی است‬      ‫وآن لوعی ازلبای است که از بشم کو‪‌-‬فنه بافند‬




           ‫که خانقاه ندارد ي‬      ‫شادی شحی‬                ‫‪ - ۱‬رطل گرانم ده ای مربد خرابات‬
   ‫د حافط شرازی ‪۷۸٩‬‏ ‪.‬‬
  ‫> رغوان بقتح اول ودوم » اسم موضعی است درشعر‬         ‫‪۳‬‬          ‫‪.‬‬   ‫آروغ‬   ‫آرغ »‬   ‫رك ‪:‬‬      ‫‪۴‬‬


                        ‫‪( 613۲۷1 = ۴‬فر) «لك‪ ۲‬ص‪. ۸۷۱‬‬
                                        ‫‪ #‬رضوان گده ‪ -‬رك ‪ :‬لفات متفرقة پاهان کتاب ‪.‬‬
                                 ‫بایان کتاب ‪.‬‬     ‫رتفة‬
--- page tag:
```


## [2026-09-07T01:46:22.360Z] TOOL CALL #49: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg314.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/314.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-07T01:46:22.441Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T01:46:24.820Z] AGENT

Now writing the verification file.


## [2026-09-07T01:52:06.194Z] TOOL CALL #50: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build314.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n  \"pdf_page\": 314,\n  \"book_page\": 284,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Lithra\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"AHD/Watkins [lithra] 'a scale' — a Mediterranean (non-Indo-European) etymon; modern reconstruction Proto-Italic *līðrā 'ingot' / Sicel *lītrā (Beekes 2010 s.v. λίτρα; Etymonline 'Proto-Italic *leithra-')\",\n      \"note\": \"Nourai's root box is a faithful copy of AHD:1527. Watkins' appendix reads: '[lithra. A scale. Mediterranean word. 1. Probably Latin libra, a pound, balance: LEVEL, LIBRA, LIRA, LIVRE; DELIBERATE, EQUILIBRIUM. 2. Probably Greek litra, unit of weight, pound: LITER.]' — even the two branches of the chart (Greek litra / Latin libra) and the chart's own note 'This is most likely a Mediterranean word' come from there. But in AHD/Watkins the square brackets mean precisely 'not an Indo-European root', so the box's language label 'Indo-European' is Nourai's own and is wrong. The modern account is compatible in substance: Ancient Greek λίτρα was borrowed from an Italic language of Sicily (Sicel *lītrā), from Proto-Italic *līðrā 'ingot', which also yielded Latin lībra; the Proto-Italic word itself has no IE etymology and is taken as a substrate word of Sicily / southern Italy. Pokorny has no entry at all for lithra/libra/litra (grep of POK_full.txt for 'lithra' and 'Latin libra' returns nothing), which is exactly what one expects of a non-IE word. Gloss 'a scale, balance' is right. Verdict plausible: the etymon and the two branches are real, the language label is not.\",\n      \"note_fa\": \"ریشهٔ فرضی «Lithra» در واقع ریشهٔ هندواروپایی نیست. واتکینز در پیوستِ AHD این صورت را در قلاب گذاشته است — و در آن کتاب قلاب نشانهٔ «غیرهندواروپایی» است — و خودِ او آن را «واژه‌ای مدیترانه‌ای» می‌خواند؛ نورایی همین یادداشت را آورده ولی برچسبِ «هندواروپایی» را هم بر جعبه نشانده که نادرست است. بر پایهٔ بیکس (۲۰۱۰) و ریشه‌شناسی امروزی، λίτρα یونانی وام‌واژه‌ای است از زبانی ایتالیک در سیسیل (سیکِل *lītrā) که از ایتالیکِ آغازین *līðrā «شمشِ فلز» می‌آید و همان واژه در لاتین lībra شده است؛ خودِ این صورت ایتالیک ریشه‌شناسی هندواروپایی ندارد و آن را واژه‌ای بومی (زیرلایه‌ای) در سیسیل و جنوب ایتالیا می‌دانند. پوکورنی هیچ ریشه‌ای برای libra/litra ندارد که همین گواهِ غیرهندواروپایی بودنِ آن است. پس: معنی و دو شاخهٔ نمودار درست است، ولی برچسب زبانی نادرست.\",\n      \"sources\": [\n        W + \"%CE%BB%CE%AF%CF%84%CF%81%CE%B1\",\n        \"https://www.etymonline.com/word/liter\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"AHD:1527\", \"status\": \"supports\", \"note\": \"Local proxy AHD_watkins1985.txt line 700 (Watkins 1985 = the same root list as the 1975/76 appendix pp.1505-1550, in which 1527 is the L-neighbourhood): '[lithra. A scale. Mediterranean word. 1. Probably Latin libra, a pound, balance: LEVEL, LIBRA, LIRA, LIVRE; DELIBERATE, EQUILIBRIUM. 2. Probably Greek litra, unit of weight, pound: LITER.]' — word for word Nourai's root box, gloss and both branches. The New College Edition itself is lending-only on archive.org, so the printed page 1527 could not be seen.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 700, s.v. lithra\", \"stance\": \"supports\", \"note\": \"'[lithra. A scale. Mediterranean word...]' — but the brackets in Watkins mark non-IE forms, so it does not support the label 'Indo-European'.\"},\n        {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'lithra' / 'Latin libra' — no hits\", \"stance\": \"silent\", \"note\": \"Pokorny's IEW has no root for libra/litra anywhere; consistent with a non-IE Mediterranean word.\"},\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 476 = printed pp. 886-887, s.v. libra\", \"stance\": \"partial\", \"note\": \"'libra, n., a pound. — L. libra, ‘balance; Roman pound’, fr. earlier *lipra, whence also Gk. λίτρα (Dor. λίτρα is a later form), of s.m.' Klein posits a shared preform *lipra for both, i.e. the same common source Nourai draws, but does not call it Mediterranean/non-IE.\"},\n        {\"src\": \"WLD\", \"where\": \"only Band 3 (Register) on disk; grep of WLD_band3.txt — no hits\", \"stance\": \"silent\", \"note\": \"Walde-Pokorny Bd. I-II are not available locally, so the pre-Pokorny treatment could not be read.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"litra\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek λίτρα (lítra) is a western-Greek (Sicilian) word: a unit of weight equal to one third of a mina, the name of a Sicilian silver coin, and by extension a vessel holding one libra — exactly the chart's gloss 'a unit of weight, also a unit of liquid measure'. It is not inherited but borrowed, in the Greek colonies of Sicily, from the local Italic language: Sicel *lītrā < Proto-Italic *līðrā 'ingot' (Beekes, EDG 2010, followed by Wiktionary). Klein arrives at the same shared preform from the Latin side, '*lipra, whence also Gk. λίτρα', the Italic dental appearing in Greek as -τ-. So the arrow root→Greek is right in substance: Greek took the word from the Mediterranean/Italic source directly, not through Latin.\",\n          \"derivation_fa\": \"λίτρα در یونانی باستان واژه‌ای است ویژهٔ یونانیانِ باختر (سیسیل): یکایی برای وزن، برابرِ یک‌سومِ مینا، و نیز نامِ سکه‌ای سیمین در سیسیل و ظرفی به اندازهٔ یک libra — یعنی درست همان معنایی که نمودار می‌دهد. این واژه میراثِ هندواروپایی نیست بلکه وام‌گیری است: یونانیانِ مهاجرِ سیسیل آن را از زبانِ ایتالیکِ بومی (سیکِل *lītrā، از ایتالیکِ آغازین *līðrā «شمش») گرفتند (بیکس ۲۰۱۰). کلاین هم از سوی لاتین به همان صورتِ مشترک *lipra می‌رسد و می‌گوید λίτραی یونانی از همان است. پس پیکانِ ریشه→یونانی از نظرِ محتوا درست است: یونانی واژه را یکسر از سرچشمهٔ مدیترانه‌ای گرفته، نه از لاتین.\",\n          \"sources\": [W + \"%CE%BB%CE%AF%CF%84%CF%81%CE%B1\", \"https://www.etymonline.com/word/liter\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:762\", \"status\": \"not_checked\", \"note\": \"p.762 is main-text of the 1975/76 New College Edition (s.v. liter), which exists on archive.org only as lending copies (djvu.txt 401). The local Watkins proxy does carry the matching claim, 'Probably Greek litra, unit of weight, pound: LITER' (AHD_watkins1985.txt line 700).\"},\n            {\"ref\": \"KLN:896\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 482, whose OCR'd page numbers are 896-897: 'liter, litre, n., a measure of capacity. F. litre, fr. earlier litron, ‘an old measure for grain’, fr. ML. litra, ‘a liquid measure’, fr. Gk. λίτρα, ‘a pound’. See litra.' The λίτρα entry itself is on the next leaf (pp.898-899): 'litra, n., name of a Greek weight and coin. — Gk. λίτρα (Dor. λίτρα), ‘pound’, fr. earlier *lipra, whence also L. libra.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 483 = pp. 898-899, s.v. litra\", \"stance\": \"supports\", \"note\": \"'name of a Greek weight and coin ... fr. earlier *lipra, whence also L. libra, ‘Roman pound’.'\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 700\", \"stance\": \"supports\", \"note\": \"'2. Probably Greek litra, unit of weight, pound: LITER.'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'litra' / 'litre' — no hits\", \"stance\": \"silent\", \"note\": \"Skeat's concise dictionary has librate and equilibrium but no litra/litre entry.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"litra\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Medieval Latin litra 'a liquid measure' is the medieval Latinisation of Greek λίτρα, re-borrowed into the Latin of the Byzantine-and-Italian Mediterranean trade beside the inherited Latin lībra (which stayed the weight). Nourai's label 'Middle Latin' and his gloss 'a liquid measure' are Klein's own words: KLN pp.896-897 s.v. liter, 'fr. ML. litra, ‘a liquid measure’, fr. Gk. λίτρα, ‘a pound’'. Etymonline gives the same link ('from Medieval Latin litra, from Greek litra “pound”'). The semantic step weight → measure of capacity happens here, in mercantile usage where a litra of wine or oil was reckoned by the pound.\",\n          \"derivation_fa\": \"litraی لاتینِ میانه (قرون وسطایی) به معنی «پیمانهٔ مایعات» همان λίτραی یونانی است که در لاتینِ بازرگانیِ مدیترانه — در کنارِ lībraی موروثی که همچنان واحدِ وزن ماند — از نو وام گرفته شد. برچسب و معنیِ نمودار عیناً از کلاین است: «از ML. litra ‘پیمانهٔ مایع’، از یونانی λίτρα ‘پوند’». تحولِ معنایی از «وزن» به «حجم» همین‌جا رخ داده، زیرا در بازار، شراب و روغن را به پوند می‌سنجیدند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/liter\", W + \"%CE%BB%CE%AF%CF%84%CF%81%CE%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:762\", \"status\": \"not_checked\", \"note\": \"main-text page of the New College Edition, lending-only; not readable.\"},\n            {\"ref\": \"KLN:896\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 482 (OCR page numbers 896-897): 'fr. ML. litra, ‘a liquid measure’, fr. Gk. λίτρα, ‘a pound’' — Nourai's gloss verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 482 = pp. 896-897, s.v. liter, litre\", \"stance\": \"supports\", \"note\": \"as quoted: ML. litra 'a liquid measure' < Gk. λίτρα.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/liter\", \"stance\": \"supports\", \"note\": \"'from Medieval Latin litra, from Greek litra “pound” (unit of weight), which apparently is from the same Sicilian Italic source as Latin libra'.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 700\", \"stance\": \"silent\", \"note\": \"the appendix entry jumps straight from Greek litra to LITER without naming the Medieval Latin stage.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"French\",\n          \"words\": \"litre\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French litre is the metric unit named in 1793 by the commission of weights and measures and fixed by the loi du 18 germinal an III (1795) as the capacity of one cubic decimetre. It does not, however, come straight from Medieval Latin litra as the arrow draws: it was formed on litron, an obsolete French dry measure for grain (16th c.), and litron in turn goes back to ML litra. Klein pp.896-897: 'F. litre, fr. earlier litron, ‘an old measure for grain’, fr. ML. litra'; Etymonline: 'from French litre (1793), from litron, name of an obsolete French measure of capacity for grain (16c.), from Medieval Latin litra'. So the chain is right but one link (litron) is missing — hence plausible rather than confirmed.\",\n          \"derivation_fa\": \"litreی فرانسوی نامِ یکای متریِ حجم است که در ۱۷۹۳ کمیسیونِ اوزان و مقادیرِ فرانسه برگزید و در ۱۷۹۵ برابرِ یک دسی‌مترِ مکعب تعریف شد. اما — برخلافِ پیکانِ نمودار — یکسر از litraی لاتینِ میانه نیامده است: آن را بر پایهٔ litron ساخته‌اند، پیمانهٔ کهنِ فرانسوی برای غله (سدهٔ ۱۶م)، و litron خود از litraی لاتینِ میانه است (کلاین، اتیمانلاین). پس زنجیره درست است ولی یک حلقه (litron) از نمودار افتاده؛ به همین سبب «با احتیاط پذیرفتنی».\",\n          \"sources\": [\"https://www.etymonline.com/word/liter\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:762\", \"status\": \"not_checked\", \"note\": \"New College Edition main text, lending-only on archive.org; the local Watkins proxy has only the appendix entry, which does not spell out the French stage.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 482 = pp. 896-897\", \"stance\": \"partial\", \"note\": \"'F. litre, fr. earlier litron, ‘an old measure for grain’, fr. ML. litra' — inserts litron between ML litra and F litre.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/liter\", \"stance\": \"partial\", \"note\": \"same: litre (1793) < litron (16c.) < Medieval Latin litra.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'litre' — no hits\", \"stance\": \"silent\", \"note\": \"Skeat has no litre entry.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"lîtr «لیتر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian لیتر lītr is a modern loan from French litre, taken over with the metric system in the Qajar/Dār al-Fonūn era and through French-medium scientific teaching; French -tre is rendered -تر and the initial l- is kept unchanged. Dehkhoda marks the word plainly as French: 'لیتر. (فرانسوی، اِ) واحد حجم و اندازه گرفتن مایعات و آن معادل هزار گرم آب خالص چهار درجه حرارت است'; Mo'in glosses 'واحدی برای اندازه‌گیری آب برابر با یک کیلوگرم'. So the arrow French → Persian is right, and this is the box in which the Persian word for 'liter' belongs (see node #7, where Nourai puts a second, unattested Persian 'liter').\",\n          \"derivation_fa\": \"«لیتر» در فارسی نو وام‌واژه‌ای است نوین از litreی فرانسوی که همراه با نظام متری و آموزشِ علومِ فرانسوی‌زبان (روزگارِ قاجار و دارالفنون) به فارسی آمد؛ ‑tre فرانسوی به ‑تر بدل شده و l آغازی دست‌نخورده مانده است. دهخدا آشکارا آن را «(فرانسوی، اِ)» می‌داند و معین «واحدی برای اندازه‌گیری آب برابر با یک کیلوگرم» می‌آورد. پس پیکانِ فرانسوی→فارسی درست است و جای واژهٔ فارسیِ «لیتر» همین جعبه است (نگاه کنید به گرهِ ۷ که نورایی صورتِ ناموجودِ «لیطر» را هم آورده).\",\n          \"sources\": [\"https://www.vajehyab.com/?q=%D9%84%DB%8C%D8%B7%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"VOP:318\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e vāžehā-ye orupāyi dar fārsi (Alborz 1371) — exactly the right book for a French loan, but refs_online.json records that no digital copy exists (re-searched 2026-09: archive.org, ketabnak, noorlib, Google Books all negative).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab.com/?q=لیطر (Mo'in section, entry لیتر)\", \"stance\": \"supports\", \"note\": \"Mo'in has only لیتر: 'واحدی برای اندازه گیری آب برابر با یک کیلوگرم'; no لیطر.\"},\n            {\"src\": \"DKH\", \"where\": \"vajehyab.com/?q=لیطر (Dehkhoda section, entry لیتر)\", \"stance\": \"supports\", \"note\": \"'لیتر. (فرانسوی، اِ) واحد حجم و اندازه گرفتن مایعات...' — origin tag 'فرانسوی' confirms the French → Persian arrow.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1/v2_pages.txt — no hits\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' (1652) obviously cannot contain a metric term; grep confirms.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"litre, liter\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English liter/litre is attested from 1797, borrowed from French litre; the British spelling keeps the French -re, the American -er follows Webster's respelling of the -re words. Klein pp.896-897: 'liter, litre, n., a measure of capacity. F. litre...' Etymonline: 'unit of capacity in the metric system, 1797, from French litre (1793)'. The word came in with the metric system itself, so it is a learned/technical borrowing, not a popular one.\",\n          \"derivation_fa\": \"liter/litre انگلیسی از ۱۷۹۷م گواهی شده و وام‌واژه‌ای است از litreی فرانسوی؛ املای بریتانیایی ‑re فرانسوی را نگه داشته و املای امریکایی ‑er پیروِ اصلاحِ املاییِ وبستر است. کلاین: «liter, litre ... از F. litre»؛ اتیمانلاین: «۱۷۹۷، از فرانسویِ litre (۱۷۹۳)». این واژه همراه با خودِ نظامِ متری وارد شده است، یعنی وام‌گیری‌ای علمی و کتابی است نه عامیانه. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/liter\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:762\", \"status\": \"not_checked\", \"note\": \"main text of the New College Edition, lending-only; the appendix entry in the local Watkins proxy does list 'LITER' as the English derivative of Greek litra, which supports the endpoint.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 482 = pp. 896-897, s.v. liter, litre\", \"stance\": \"supports\", \"note\": \"'liter, litre, n., a measure of capacity. F. litre, fr. earlier litron...'\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/liter\", \"stance\": \"supports\", \"note\": \"'1797, from French litre (1793)'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'litre' — no hits\", \"stance\": \"silent\", \"note\": \"not in Skeat's concise dictionary.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Arabic\",\n          \"words\": \"lîtr; ratl\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The box packs two words of very different date. (a) رطل raṭl / riṭl 'a weight of twelve ounces; a large vessel for drink' really is Greek λίτρα, but it reached Arabic through Aramaic, not directly: Gk λίτρα → Jewish Palestinian Aramaic / Classical Syriac līṭrā → Aramaic rīṭlā (dissimilation of the first l to r before the second liquid, with metathesis of the vowel) → Arabic raṭl/riṭl; Greek τ is regularly rendered by the emphatic ط in Aramaic-mediated Greek loans. Lokotsch no. 1708 states it flatly: 'Ar. raṭl: „Ein Gewicht“ [aus gr. λίτρα; ZDMG LI, 298; de Lagarde, Gesammelte Abhandlungen 33]', adding Fleischer's point that the Arabs themselves felt riṭl to be the better pronunciation, ratl prevailing under the influence of the first two consonants. Nourai's NOTE, '„ratl“ is a distorted form of „lîtr“', is therefore substantially right, though the 'distortion' is a regular Aramaic development rather than a corruption inside Arabic; and the intermediate Aramaic stage is missing from the chart. (b) Arabic لتر/ليتر lītr 'liter' is not this word at all: it is a nineteenth-century loan from French litre taken with the metric system, so putting it under Ancient Greek λίτρα is wrong — it belongs with node #4 under the French box. Worst verdict therefore governs: plausible.\",\n          \"derivation_fa\": \"این جعبه دو واژه با دو تاریخِ بسیار متفاوت را یکجا آورده است. (الف) «رطل» عربی به معنی وزنِ دوازده اوقیه و نیز ظرفِ بزرگِ نوشیدنی، به‌راستی همان λίτραی یونانی است، اما نه یکسر: از راهِ آرامی آمده — یونانی λίτρα ← آرامیِ فلسطینی/سریانیِ کلاسیک līṭrā ← آرامی rīṭlā (ابدالِ l نخست به r پیشِ روانِ دوم، همراه با قلبِ واکه) ← عربی raṭl/riṭl؛ و τ یونانی در وام‌واژه‌های آرامی‌واسطه به‌طور قاعده‌مند «ط» می‌شود. لوکوچ (شمارهٔ ۱۷۰۸) همین را می‌گوید و می‌افزاید که خودِ عرب‌ها تلفظِ riṭl را درست‌تر می‌دانستند. پس یادداشتِ نورایی که «رطل صورتِ تحریف‌شدهٔ لیتر است» در اصل درست است، ولی این «تحریف» دگرگونیِ قاعده‌مندِ آرامی است نه فسادِ درون‌عربی، و حلقهٔ آرامی از نمودار افتاده است. (ب) «لتر/ليتر» عربی به معنی لیتر، اصلاً این واژه نیست: وام‌واژه‌ای است از litreی فرانسوی در سدهٔ نوزدهم همراه با نظامِ متری؛ پس آوردنِ آن زیرِ λίτραی یونانی خطاست و جایش زیرِ جعبهٔ فرانسوی (گرهِ ۴) است. بنابراین حکمِ گره «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [W + \"%D8%B1%D8%B7%D9%84\", W + \"%CE%BB%CE%AF%CF%84%CF%81%CE%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"VGH:65\", \"status\": \"not_checked\", \"note\": \"Khadiv Jam, Vāže-nāme-ye ghazalhā-ye Hāfez (Elmi 1371) — refs_online.json records only a login-walled ketabnak PDF (book/121989), not on archive.org; not readable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"LKT.txt lines 3896-3897, no. 1708 'Ar. ratl'\", \"stance\": \"supports\", \"note\": \"'„Ein Gewicht“ [aus gr. λίτρα; ZDMG LI, 298; de Lagarde, Gesammelte Abhandlungen 33, Anm. ... ist die Aussprache riṭl nach den Arabern selbst die richtigere]' — Greek origin, plus the Italian/Sicilian/Spanish/Portuguese offspring rotolo, arrátel, arrelde.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt line 1867, s.v. (الرطل)\", \"stance\": \"partial\", \"note\": \"Addi Shir defines it as ten (?) ounces, half the Tabriz man, and 'وعاء يوضع فيه الشراب ونحوه' (a vessel for drink), names a Greek form ('باليونانية'), then says 'لست أدري هل أصله يوناني أم فارسي' — he entertains the Greek origin but leaves it open between Greek and Persian.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 723 (pp. ~1422-1423), s.v. rotl\", \"stance\": \"contradicts\", \"note\": \"'rotl, n., a weight used in North Africa. — Arab. raṭl, rel. to raṭala, ‘he poised’, rattala, ‘he weighed’.' Klein gives an Arabic-internal derivation from a native root, against the Greek/Aramaic origin.\"},\n            {\"src\": \"AFA\", \"where\": \"AFA.txt line 2748 (Fraenkel, footnote)\", \"stance\": \"partial\", \"note\": \"Fraenkel discusses the same l~r interchange and explicitly cites the change 'von λίτρον zu litra' as a parallel; supports the phonetics of the Greek-to-Semitic route without giving raṭl a full entry.\"},\n            {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt, grep 'ratl'/'rotl' — no hits\", \"stance\": \"silent\", \"note\": \"raṭl is not a Qur'anic word, so Jeffery has no entry.\"},\n            {\"src\": \"HJB\", \"where\": \"HJB.txt line 2084\", \"stance\": \"supports\", \"note\": \"Hobson-Jobson quotes 1588: 'a churle is 27 rottles and a half of Aleppo' — the unit itself, in the Levant trade, as the chart's 'large liquid container' implies.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"lîtr «لیطر»; ratl «رطل»\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"لیطر\",\n          \"correct_form\": \"لیتر\",\n          \"derivation\": \"رطل is sound and well documented. Arabic raṭl was borrowed into Persian early and is common from the eleventh century on in exactly the sense the chart gives, 'a large cup/measure of wine': the chart's own Vis-o-Rāmin hemistich (Fakhr al-Din Asʿad Gorgāni, mid-11th c.), 'دل میخواره را باشد به می آز - بسی رطل و بسی ساغر خورد باز', is genuine, and Borhan-e Qateʿ quotes the same use with 'رطل گرانم ده ای مرید خرابات' (Hafez). Mo'in: 'رطل [ع.] (اِ) واحدی است برای وزن و آن برابر دوازده اوقیه و مساوی ۸۴ مثقال است. پیالهٔ شراب؛ ج. ارطال. رطل گران: پیمانهٔ بزرگ'. Since Arabic itself got raṭl from Greek λίτρα by way of Aramaic, رطل is in effect the Mediterranean weight-word returning to Persian through Aramaic and Arabic, which is what the chart draws — correct. — The other word in the box is not. «لیطر», with the emphatic ط, is unknown to Persian lexicography: Dehkhoda, Mo'in and Amid have only لیتر, tagged '(فرانسوی)'; no hit for لیطر or لیطره in either Mo'in text file or on vajehyab. The printed page 284 does show «لیطر» (see data/verification/sources/refs/ocr/BOOK/314.png), so the extraction is faithful and the error is Nourai's: he has re-spelt the modern French loan with the ط of رطل so that the two words in the box look like one word, and has thereby invented a form that is not Persian. The correct Persian spelling is لیتر, and it is already correctly placed under French at node #4.\",\n          \"derivation_fa\": \"«رطل» درست و مستند است: raṭl عربی زود به فارسی آمد و از سدهٔ پنجم هجری به همان معنایی که نمودار می‌دهد — «پیالهٔ بزرگِ شراب» — فراوان به کار رفته است؛ بیتِ ویس و رامین که خودِ نمودار آورده («بسی رطل و بسی ساغر خورد باز») اصیل است و برهان قاطع نیز بیتِ حافظ «رطل گرانم ده ای مرید خرابات» را گواه می‌آورد. معین: «رطل [ع.] (اِ) واحدی است برای وزن ... پیالهٔ شراب؛ ج. ارطال». چون خودِ عربی «رطل» را از راهِ آرامی از λίτραی یونانی گرفته است، «رطل» در واقع بازگشتِ همان واژهٔ مدیترانه‌ایِ وزن به فارسی از مسیرِ آرامی و عربی است — یعنی درست همان چیزی که نمودار می‌کشد. — اما واژهٔ دیگرِ این جعبه چنین نیست: «لیطر» با «ط» در فرهنگ‌های فارسی وجود ندارد؛ دهخدا و معین و عمید تنها «لیتر» را دارند با نشانِ «(فرانسوی)» و جست‌وجوی «لیطر/لیطره» در متنِ معین و در وجه‌یاب بی‌نتیجه است. صفحهٔ چاپیِ ۲۸۴ هم عیناً «لیطر» را نشان می‌دهد (تصویر: data/verification/sources/refs/ocr/BOOK/314.png)، پس خطای خوانشِ اسکن نیست بلکه خطای خودِ کتاب است: نورایی وام‌واژهٔ نوینِ فرانسوی را با «ط»ِ «رطل» نوشته تا دو واژهٔ جعبه یکی به نظر آیند و از این راه صورتی ساخته که فارسی نیست. املای درست «لیتر» است و در گرهِ ۴ (زیرِ فرانسوی) هم درست آمده است.\",\n          \"sources\": [W + \"%D8%B1%D8%B7%D9%84\", \"https://www.vajehyab.com/?q=%D9%84%DB%8C%D8%B7%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1660\", \"status\": \"partial\", \"note\": \"The 6-vol Amir Kabir edition Nourai cites is not digitised, so p.1660 cannot be checked; in the 2-vol Adena condensation (MON_part1.txt line 67785) the entry reads 'رطل: [ع.] (اِ) واحدی است برای وزن و آن برابر دوازده اوقیه و مساوی ۸۴ مثقال است. پیالهٔ شراب؛ ج. ارطال' — Mo'in supports the gloss and the Arabic origin of رطل, but has no لیطر at all.\"},\n            {\"ref\": \"VGH:65\", \"status\": \"not_checked\", \"note\": \"Khadiv Jam's Hafez glossary: only a login-walled scan (ketabnak 121989); not readable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt around line 24428 (ر section)\", \"stance\": \"supports\", \"note\": \"the Borhan material on رطل is illustrated with 'رطل گرانم ده ای مرید خرابات' (Hafez), attesting the 'large wine-cup' sense in Persian; the OCR of Mo'in's footnote apparatus on that page is too damaged to read the etymon he gives.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 67785, s.v. رطل\", \"stance\": \"supports\", \"note\": \"'[ع.]' + 'پیالهٔ شراب' — Arabic loan, exactly the chart's gloss.\"},\n            {\"src\": \"DKH\", \"where\": \"vajehyab.com/?q=لیطر\", \"stance\": \"contradicts\", \"note\": \"no entry for لیطر or لیطره in Dehkhoda/Mo'in/Amid; only لیتر '(فرانسوی، اِ)'.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt no. 1708\", \"stance\": \"supports\", \"note\": \"confirms that the Arabic word behind Persian رطل is Greek λίτρα, i.e. the round trip the chart draws.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"Libra; Dě-lîberâre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin lībra 'a balance, pair of scales' and 'the Roman pound' (12 unciae) goes back to Proto-Italic *līðrā (Etymonline: 'ultimately deriving from Proto-Italic *leithra-'), the same Mediterranean/Sicel etymon that Greek borrowed as λίτρα — so the chart's two parallel arrows out of the root, to Greek and to Latin, are correct and reproduce AHD:1527's two numbered branches. dēlīberāre 'to weigh well, consider carefully, consult' is denominal from lībra: de- (intensive, 'entirely') + *lībrāre, a by-form of librāre 'to balance, make level', hence literally 'to weigh thoroughly'; the -ī- and the medieval confusion with liber 'free' are secondary. Klein s.v. deliberate: 'derives fr. original *de-librare, which is formed fr. de- and libra, ‘scales; that which is weighed; a pound’ ... L. deliberare was influenced in form by liberare, ‘to make free’.' Etymonline says the same. Nourai's gloss 'to weight well, ponder' is Klein's/Etymonline's 'weigh well'.\",\n          \"derivation_fa\": \"lībraی لاتین به معنی «ترازو» و «پوندِ رومی» (دوازده اوقیه) به ایتالیکِ آغازینِ *līðrā می‌رسد (اتیمانلاین: *leithra-)، یعنی همان واژهٔ مدیترانه‌ای/سیکِلی که یونانی آن را λίτρα وام گرفت؛ پس دو پیکانِ موازیِ نمودار از ریشه به یونانی و به لاتین درست است و همان دو شاخهٔ شماره‌دارِ AHD:1527 را بازمی‌گوید. dēlīberāre «نیک سنجیدن، اندیشیدن» فعلی است ساخته از همین نام: پیشوندِ تأکیدیِ de- «به‌تمامی» + *lībrāre (گونه‌ای از librāre «سنجیدن، تراز کردن»)، یعنی تحتِ‌اللفظ «سنگ‌تمام سنجیدن». کلاین: «از *de-librare، ساخته از de- و libra ‘ترازو’ ... صورتِ deliberare زیرِ نفوذِ liberare ‘آزاد کردن’ دگرگون شده است». ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/deliberate\", \"https://www.etymonline.com/word/liter\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:349\", \"status\": \"not_checked\", \"note\": \"p.349 is the New College Edition main text (s.v. deliberate), lending-only on archive.org. The local Watkins proxy supports the substance: '[lithra ...] 1. Probably Latin libra, a pound, balance: LEVEL, LIBRA, LIRA, LIVRE; DELIBERATE, EQUILIBRIUM.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 230, s.v. deliberate, adj.\", \"stance\": \"supports\", \"note\": \"'L. deliberatus, pp. of deliberare, ‘to think over, take counsel about’, which prob. means lit. ‘to weigh in one’s mind’, and derives fr. original *de-librare, which is formed fr. de- and libra, ‘scales...’'\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/deliberate\", \"stance\": \"supports\", \"note\": \"'from Latin deliberatus ... de- (entirely) + -liberare, altered from librare “to balance, make level,” which derives from libra “pair of scales, a balance”'.\"},\n            {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'Latin libra' — no hits\", \"stance\": \"silent\", \"note\": \"Pokorny has no IE root for lībra, consistent with the non-IE origin of the Italic word.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 10274, s.v. Librate\", \"stance\": \"supports\", \"note\": \"'... weigh, from libra, a balance.'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"Libra, deliberate, equilibrium\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are learned Latinisms, borrowed in writing, not inherited. Libra is Latin lībra taken over unchanged as the name of the zodiacal Scales (in English astronomical use from Middle English on). deliberate is the Latin participle dēlīberātus, adjective from early 15c. ('done with careful consideration'), verb from the 1540s ('weigh in the mind'), with the sense 'consciously unhurried' from the 1590s. equilibrium is Latin aequilibrium 'even balance', aequus 'equal' + lībra. Klein's libra entry (p.886) cross-refers exactly this set — 'Cp. librate, deliberate, equilibrium' — and Skeat s.v. equilibrium: 'L. aequilibris, evenly balanced. — L. aequi- for aequus, even; libra, to balance; see Librate.' The same Latin word also underlies the abbreviations lb. and £, and It. lira and Fr. livre, which AHD lists under the same etymon.\",\n          \"derivation_fa\": \"هر سه واژه وام‌واژه‌هایی کتابی از لاتین‌اند، نه میراثِ ژرمنی. Libra همان lībraی لاتین است که بی‌تغییر نامِ برجِ «ترازو» شد. deliberate از اسمِ مفعولِ لاتینِ dēlīberātus است: صفت از آغازِ سدهٔ ۱۵م و فعل از دههٔ ۱۵۴۰م، و معنیِ «آهسته و سنجیده» از دههٔ ۱۵۹۰م. equilibrium از aequilibriumِ لاتین است، از aequus «برابر» + lībra «ترازو». کلاین در مدخلِ libra (ص ۸۸۶) درست همین سه را ارجاع می‌دهد («Cp. librate, deliberate, equilibrium») و اسکیت هم زیرِ equilibrium: «از L. aequilibris ... aequi- برای aequus ‘برابر’؛ libra ‘سنجیدن’». همین واژهٔ لاتین پشتِ نشانه‌های lb. و £ و نیز liraی ایتالیایی و livreی فرانسوی است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/deliberate\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:886\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 476, whose OCR'd page numbers are 886-887: 'libra, n., a pound. — L. libra, ‘balance; Roman pound’, fr. earlier *lipra, whence also Gk. λίτρα ... Cp. librate, deliberate, equilibrium. Cp. also litra, litre, livre.' Nourai's three English words are Klein's own cross-reference list on that very page.\"},\n            {\"ref\": \"AHD:349\", \"status\": \"not_checked\", \"note\": \"New College Edition main text (deliberate), lending-only; the local Watkins proxy lists 'LIBRA ... DELIBERATE, EQUILIBRIUM' under lithra, which supports the set.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 291 (equilibrium) and leaf 230 (deliberate)\", \"stance\": \"supports\", \"note\": \"'equilibrium, n., balance. — L., ‘even balance’, compounded of aequus, ‘equal’, and libra, ‘balance’.'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt lines 5933, 10274\", \"stance\": \"supports\", \"note\": \"'equilibrium ... L. aequilibris, evenly balanced. — L. aequi- for aequus, even; libra, to balance; see Librate' and 'Librate ... weigh, from libra, a balance.'\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/deliberate\", \"stance\": \"supports\", \"note\": \"adjective early 15c., verb 1540s; 'consciously unhurried' by 1590s.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 5,\n      \"root\": \"Longos, Lenghô, Leng, Long\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *(s)leh₁g- (Pokorny (s)leg-, (s)lag-, (s)lēg-, nasalized *(s)leng-) 'slack, weak, languid'; Indo-Iranian *langa- 'lame'\",\n      \"note\": \"The 'limp, lame, bent' half of the root box is real. Pokorny 959-960 sets up '(s)leg-, (s)lag- and (s)lēg-, Meaning: weak, feeble', with the express note 'nasalized (s)leng-' and, as his very first item of material, 'Old Indic laṅga- ‘lame’', beside Latin laxus 'slack', nasalized langueō, and Greek λήγω; Watkins' appendix has the same root as 'slēg-. To be slack, be languid ... Suffixed nasalized form *la-n-g-u- in Latin languēre'. Wiktionary's chain PIE *(s)leh₁g- > Proto-Indo-Iranian *langa- 'lame' > Skt laṅga- and Proto-Iranian *langa- > NP lang (citing Pokorny 1959 and Edelʹman, ESIJa 2015) is exactly the chart's Persian-Sanskrit pair. Nourai's four headword shapes are Mann's: lengho at IEC p.678 and longos at p.709, and the citation is exact — leaf 382 of the local IEC scan carries the printed page 678 ('lengho (3) ‘trail, lie limp, pine’ ... Per. langam, langidan, inf. ‘limp’ ... Skt. langami, id.; langah lame') and leaf 400 carries 709 ('longos “lame, bent, crooked; meadow, lowland” ... Skt. langah ‘lame’; Per. lang, id.; Mod. Gk. lóggos'). What is not established is the second half of the gloss, 'also a low land, meadow'. That comes from Mann's own decision to put the 'lame' words in one entry with Slavic *lǫgъ (OCS logŭ, Bulg. lǎg 'copse, meadow', Cz. luh, Pol. ług 'lowland, marsh') and Modern Greek lóggos. Modern handbooks keep the two apart: Slavic *lǫgъ 'meadow, marshy grove' has no accepted connection with *(s)leh₁g- 'slack', and Mann himself flags the Greek word as a Slavic loanword. Verdict plausible: correct root, over-wide gloss.\",\n      \"note_fa\": \"نیمهٔ نخستِ معنیِ جعبهٔ ریشه — «لنگیدن، لنگ، خمیده» — درست است. پوکورنی در صص ۹۵۹–۹۶۰ ریشهٔ «(s)leg-, (s)lag-, (s)lēg- به معنیِ سست و ناتوان» را با یادداشتِ «گونهٔ خیشومی‌شده (s)leng-» می‌آورد و نخستین گواهش «هندیِ باستان laṅga- ‘لنگ’» است، در کنارِ laxus و langueōی لاتین و λήγωی یونانی؛ واتکینز نیز همین ریشه را زیرِ slēg- «سست و بی‌رمق بودن» دارد. ویکی‌واژه زنجیرهٔ هندواروپاییِ آغازین *(s)leh₁g- ← هندوایرانیِ آغازین *langa- «لنگ» ← سنسکریت laṅga- و ایرانیِ آغازین *langa- ← فارسیِ نو «لنگ» را (به استنادِ پوکورنی ۱۹۵۹ و اِدِلمان ۲۰۱۵) می‌دهد که همان جفتِ فارسی–سنسکریتِ نمودار است. چهار صورتِ سرواژهٔ نورایی هم از مان (IEC) است و ارجاعش دقیق: برگِ ۳۸۲ نسخهٔ محلی صفحهٔ چاپیِ ۶۷۸ و برگِ ۴۰۰ صفحهٔ ۷۰۹ را دارد. اما نیمهٔ دومِ معنی، «و نیز زمینِ پست، چمنزار»، پذیرفتنی نیست: این از آنجاست که مان واژه‌های «لنگ» را با خانوادهٔ اسلاویِ *lǫgъ (چمنزار، بیشهٔ باتلاقی) و λόγγοςی یونانیِ نو در یک مدخل گذاشته است. ریشه‌شناسیِ امروزی این دو را جدا می‌داند و خودِ مان هم واژهٔ یونانی را وام‌واژهٔ اسلاوی می‌خواند. پس: ریشه درست، معنی گسترده‌تر از حق.\",\n      \"sources\": [\n        W + \"%D9%84%D9%86%DA%AF\",\n        W + \"%E0%A4%B2%E0%A4%99%E0%A5%8D%E0%A4%97\",\n        W + \"%CE%BB%CF%8C%CE%B3%CE%B3%CE%BF%CF%82\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"IEC:678\", \"status\": \"supports\", \"note\": \"IEC.txt line 9662, leaf 382 (the leaf carries the printed page number 678): 'lengho (3) “trail, lie limp, pine” (?) (Variant: leng-, long-...) (Per. langam, langidan, inf. “limp” is from a variant of type *leng- in view of Skt. langami, id.; langah lame)'. Nourai's headwords Lenghô/Leng/Long are Mann's.\"},\n        {\"ref\": \"IEC:709\", \"status\": \"supports\", \"note\": \"IEC.txt line 10042, leaf 400 (printed page 709): 'longos “lame, bent, crooked; meadow, lowland”. Skt. langah ‘lame’; Per. lang, id.; Mod. Gk. lóggos, m. (“wood, grove”. A Sl. LW for Andrioti); OCS logü, m., id.; Blg. lág ‘copse, meadow’...' — the source of Nourai's root name, of his double gloss, and of all three of his nodes.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_full.txt lines 78238ff., pp. 959-960\", \"stance\": \"supports\", \"note\": \"'Root / lemma: (s)leg-, (s)lag- and (s)lēg-; Meaning: weak, feeble; Note: nasalized (s)leng- ... Material: Old Indic laṅga- “lame”; ... Latin laxus “slack, wide”, nasalized langueo, -ere ... References: WP. II 712 ff., WH. I 758 f.'\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 953, s.v. slēg-\", \"stance\": \"supports\", \"note\": \"'slēg-. To be slack, be languid... Zero-grade form *(s)lag-... 2. Suffixed form *lag-so- in Latin laxus... 3. Suffixed nasalized form *la-n-g-u- in Latin languēre... 4. Compound *lag-ous- ... Greek lagōs, hare.' Same root, without the Indo-Iranian material.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt lines 9660-9662 (p.678) and 10042 (p.709)\", \"stance\": \"supports\", \"note\": \"Mann is the source of the chart, and his p.709 entry is verbatim Nourai's box.\"},\n        {\"src\": \"SYN\", \"where\": \"SYN.txt line 8131, §4.94 LAME\", \"stance\": \"partial\", \"note\": \"Buck's 'lame' list gives Grk. χωλός, Lat. claudus, Skt. śroṇa-, srāma-, paṅgu- and no Iranian form; he notes such words come 'from diverse notions such as ‘break, bend, twist’' — he does not use this root for 'lame'.\"},\n        {\"src\": \"WLD\", \"where\": \"only Band 3 (Register) on disk; no hits for laṅga / (s)leg-\", \"stance\": \"silent\", \"note\": \"Walde-Pokorny Bd. II 712 ff., which Pokorny cites for this root, is not available locally.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"lang «لَنگ»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian لنگ lang 'lame' continues Proto-Iranian *langa-, from Proto-Indo-Iranian *langa- 'lame' (= Sanskrit laṅga-), from PIE *(s)leh₁g- 'slack, weak' with the nasal infix (Wiktionary, citing Pokorny 1959 and Edelʹman, Etymological Dictionary of the Iranian Languages 2015). Phonetically nothing had to happen: Old Iranian *a stays a and the cluster -ng- is preserved through Middle Persian into New Persian, so lang is the direct continuant of the Middle Persian form; from the adjective are built langīdan 'to limp' and lang-lang, and Mann quotes precisely these forms at IEC p.678 ('Per. langam, langidan, inf. “limp”'). Cognates: Central Kurdish لەنگ leng, Pashto lang; Old Armenian լանկ lank is a borrowing from Iranian. The hemistich in the box, 'پای ما لنگ است و منزل بس دراز - دست ما کوتاه و خرما بر نخیل', is the familiar line traditionally attributed to Hafez and quoted proverbially. Note that Horn, Hübschmann and MacKenzie all happen to have no entry for this word, so Nourai's Mann citation is in fact the best available.\",\n          \"derivation_fa\": \"«لَنگ» در فارسی نو دنبالهٔ ایرانیِ آغازینِ *langa- است، از هندوایرانیِ آغازینِ *langa- «لنگ» (= laṅga- سنسکریت)، و آن از هندواروپاییِ آغازینِ *(s)leh₁g- «سست، ناتوان» با میان‌وندِ خیشومی (ویکی‌واژه، به استنادِ پوکورنی ۱۹۵۹ و اِدِلمان ۲۰۱۵). از نظرِ آوایی هیچ دگرگونیِ لازم نبوده است: aی ایرانیِ باستان a مانده و خوشهٔ ‑ng‑ از فارسیِ میانه تا فارسیِ نو پایدار بوده؛ پس «لنگ» بی‌واسطه دنبالهٔ صورتِ پهلوی است. از همین صفت «لنگیدن» و «لنگ‌لنگ» ساخته شده و مان هم در ص ۶۷۸ همین صورت‌ها را گواه می‌آورد. هم‌ریشه‌ها: «لەنگ» کردیِ سورانی و lang پشتو؛ լանկ (lank) ارمنیِ باستان وام‌واژه‌ای ایرانی است. بیتِ «پای ما لنگ است و منزل بس دراز...» بیتی است مشهور که به حافظ نسبت می‌دهند. نکته اینکه هرن و هوبشمان و مکنزی هیچ‌کدام مدخلی برای این واژه ندارند، پس ارجاعِ نورایی به مان در واقع بهترین گواهِ دردست است. ادعای نورایی درست است.\",\n          \"sources\": [W + \"%D9%84%D9%86%DA%AF\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:678\", \"status\": \"supports\", \"note\": \"IEC.txt line 9662 (leaf 382 = printed p.678): '(Per. langam, langidan, inf. “limp” is from a variant of type *leng- in view of Skt. langami, id.; langah lame)'.\"},\n            {\"ref\": \"IEC:709\", \"status\": \"supports\", \"note\": \"IEC.txt line 10042 (leaf 400 = printed p.709): 'longos “lame, bent, crooked...” Skt. langah ‘lame’; Per. lang, id.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'lang' — only 'diräz ‘lang’' (German for 'long') and palang\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for lang 'lame'.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt, grep 'lang' — only German 'lang', balang, palang, badrang\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien does not treat lang 'lame'.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD.txt, grep 'lang [' — no MP entry\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary as OCR'd here has palang, kulang, but no lang 'lame'; the MP form is inferred, not attested in his selection.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, printed p. 453 (running head «لنگ لنگیدن»)\", \"stance\": \"partial\", \"note\": \"Aryanpur does have an entry for لنگ/لنگیدن with Sanskrit and Latin cognates glossed 'شل، لنگ' and references to برهان قاطع and فرهنگ معین, but the OCR of that page is too damaged to read the PIE root he assigns.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt, grep 'lang' — only 'language(s)'\", \"stance\": \"silent\", \"note\": \"Cheung's Etymological Dictionary of the Iranian Verb has no *lang- root (it is denominal in Persian).\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/لنگ\", \"stance\": \"supports\", \"note\": \"'from Proto-Iranian *langa-, from Proto-Indo-Iranian *langa- (“lame”) ... ultimately from PIE *(s)leh₁g- (“feeble, weak”)', citing Pokorny 1959 and Edelʹman 2015.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"langah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Nourai's 'langah' is Mann's citation shape for Sanskrit लङ्ग laṅga-, nominative singular laṅgaḥ, adjective 'limping, lame', masculine noun 'limping, lameness' (Monier-Williams 1899 s.v.; Mayrhofer EWAia and Turner CDIAL are cited by Wiktionary for the Indo-Aryan continuations, e.g. Hindi laṅgṛā). Beside it stands the denominative laṅgati 'he limps'. It is the exact Indic match of Persian lang: both go back to Proto-Indo-Iranian *langa-, from PIE *(s)leh₁g- 'slack, weak' with a nasal infix, and Pokorny quotes it as his very first piece of material for that root ('Old Indic laṅga- ‘lame’', IEW 959). So the arrow root → Sanskrit is correct; only the transliteration is Mann's (nominative -aḥ written -ah, and no diacritic on the ṅ), not standard indological practice.\",\n          \"derivation_fa\": \"«langah»ِ نورایی همان صورتِ ارجاعیِ مان است برای लङ्ग (laṅga-) سنسکریت، فاعلیِ مفردِ laṅgaḥ، صفت به معنیِ «لنگ، لنگان» و اسمِ نریِ «لنگی» (مونیه‌ویلیامز ۱۸۹۹؛ ویکی‌واژه برای دنباله‌های هندوآریایی مانندِ laṅgṛāی هندی به مایرهوفر و ترنر ارجاع می‌دهد). در کنارِ آن فعلِ اسم‌بنیادِ laṅgati «می‌لنگد» هست. این واژه دقیقاً همتای هندیِ «لنگ» فارسی است: هر دو از هندوایرانیِ آغازینِ *langa-، از *(s)leh₁g- هندواروپایی با میان‌وندِ خیشومی؛ و پوکورنی نخستین گواهِ خود برای این ریشه را همین «laṅga- هندیِ باستان» می‌آورد (ص ۹۵۹). پس پیکانِ ریشه→سنسکریت درست است؛ تنها آوانگاریِ «langah» از مان است و شیوهٔ متعارفِ هندشناسی نیست.\",\n          \"sources\": [W + \"%E0%A4%B2%E0%A4%99%E0%A5%8D%E0%A4%97\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:709\", \"status\": \"supports\", \"note\": \"IEC.txt line 10042 (leaf 400 = printed p.709): 'Skt. langah ‘lame’' is the first item of Mann's longos entry — Nourai's node verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt line ~78243, IEW pp. 959-960\", \"stance\": \"supports\", \"note\": \"'Material: Old Indic laṅga- “lame”' — the first witness of Pokorny's (s)leg- root.\"},\n            {\"src\": \"Wiktionary/Monier-Williams\", \"where\": \"en.wiktionary.org/wiki/लङ्ग\", \"stance\": \"supports\", \"note\": \"'limping, lame' (adj.), 'limping, lameness' (n.), 'from Proto-Indo-European *(s)leh₁g- (weak, feeble)'; Monier-Williams 1899, Mayrhofer 2001, Turner 1969-85 cited.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 953, s.v. slēg-\", \"stance\": \"silent\", \"note\": \"Watkins lists only Germanic, Latin and Greek reflexes; no Sanskrit.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"loggos\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"There is no Ancient Greek *λόγγος. λόγγος 'dense and bushy wood, grove' is Byzantine and Modern Greek, and it is a Slavic loanword: Proto-Slavic *lǫ̑gъ 'depression, meadow, valley' → Byzantine Greek λόγγος → Modern Greek λόγγος (Wiktionary, following Andriotis' Etymological Dictionary of Standard Modern Greek and the Dictionary of Standard Modern Greek). Nourai's own cited reference says the same thing: Mann, IEC p.709, writes 'Mod. Gk. lóggos, m. (“wood, grove”. A Sl. LW for Andrioti)' — i.e. he labels it Modern Greek and a Slavic loanword, and lists it only because he wanted the Slavic 'meadow, lowland' family (OCS logŭ, Bulg. lǎg, Cz. luh, Pol. ług) in the same entry as 'lame'. The chart drops both qualifications, so there are two errors: the language label ('Greek' for a word first attested in Byzantine Greek), and the derivation (a Slavic borrowing, not a Greek inheritance — and the Slavic word itself has no accepted link to *(s)leh₁g- 'slack, lame'). This node is also the sole basis of the root box's extra gloss 'also a low land, meadow'.\",\n          \"derivation_fa\": \"در یونانیِ باستان *λόγγος وجود ندارد. λόγγος به معنیِ «بیشهٔ انبوه، جنگل» یونانیِ بیزانسی و نو است و وام‌واژه‌ای است اسلاوی: اسلاویِ آغازین *lǫ̑gъ «گودی، چمنزار، دره» ← یونانیِ بیزانسی λόγγος ← یونانیِ نو λόγγος (ویکی‌واژه، به پیرویِ آندریوتیس و «فرهنگِ یونانیِ نوِ معیار»). خودِ مرجعی که نورایی آورده همین را می‌گوید: مان در ص ۷۰۹ می‌نویسد «Mod. Gk. lóggos ... A Sl. LW for Andrioti» یعنی هم آن را یونانیِ نو می‌خواند و هم وام‌واژهٔ اسلاوی، و تنها از آن رو در این مدخل آورده است که می‌خواسته خانوادهٔ اسلاویِ «چمنزار/زمینِ پست» را با «لنگ» یکی کند. نمودار هر دو قید را انداخته است، پس دو خطا دارد: برچسبِ زبانی («یونانی» برای واژه‌ای که نخست در یونانیِ بیزانسی گواهی شده) و خودِ اشتقاق (وام‌گیری از اسلاوی، نه میراثِ یونانی؛ و آن واژهٔ اسلاوی هم پیوندِ پذیرفته‌شده‌ای با *(s)leh₁g- «سست، لنگ» ندارد). همین گره تنها تکیه‌گاهِ معنیِ افزودهٔ جعبهٔ ریشه («و نیز زمینِ پست، چمنزار») است. پژوهشِ امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [W + \"%CE%BB%CF%8C%CE%B3%CE%B3%CE%BF%CF%82\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:709\", \"status\": \"partial\", \"note\": \"IEC.txt line 10042 (leaf 400 = printed p.709) does contain the word, but with the caveat the chart omits: 'Mod. Gk. lóggos, m. (“wood, grove”. A Sl. LW for Andrioti)' — Modern Greek, and a Slavic loanword.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/λόγγος\", \"stance\": \"contradicts\", \"note\": \"'Inherited from Byzantine Greek λόγγος (lóngos), from Proto-Slavic *lǫ̑gъ (“depression, meadow, valley”)' — a Slavic loan, not an IE inheritance in Greek.\"},\n            {\"src\": \"POK\", \"where\": \"POK_full.txt pp. 959-960, s.v. (s)leg-\", \"stance\": \"silent\", \"note\": \"Pokorny's material for this root contains no Greek λόγγος and no Slavic 'meadow' words; his Greek reflexes are λήγω, λαγαρός, λαγώς.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 10042\", \"stance\": \"partial\", \"note\": \"Mann's own 'A Sl. LW' note undercuts the arrow he is cited for.\"},\n            {\"src\": \"SYN\", \"where\": \"SYN.txt, §§ on 'meadow'/'grove' — no λόγγος\", \"stance\": \"silent\", \"note\": \"Buck does not use the word.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-314.json', 'w', encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\n"
}
```


### [2026-09-07T01:52:06.230Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build314.py (file state is current in your context — no need to Read it back)
```


## [2026-09-07T01:52:09.786Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build314.py && python3 -m json.tool data/verification/page-314.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 314"
}
```


### [2026-09-07T01:52:11.271Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 12/12
node verdicts: {'confirmed': 8, 'plausible': 2, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'plausible': 2}
ref checks: {'not_checked': 9, 'supports': 6, 'partial': 2}
books consulted: {'supports': 22, 'silent': 14, 'partial': 6, 'contradicts': 3} | by book: {'KLN': 7, 'SKT': 5, 'Etymonline': 5, 'AHD': 3, 'POK': 3, 'MON': 2, 'DKH': 2, 'BQT': 2, 'LKT': 2, 'Wiktionary': 2, 'AFM': 1, 'AFA': 1, 'FVQ': 1, 'HJB': 1, 'HRN': 1, 'HUB': 1, 'PHD': 1, 'ARY': 1, 'CHEUNG': 1, 'Wiktionary/Monier-Williams': 1, 'IEC': 1, 'SYN': 1}
```


## [2026-09-07T01:52:29.864Z] AGENT

Done. `python3 tools/verify_check.py 314` → 12/12 nodes, **0 PROBLEM lines**.

**Page 314 (book p. 284) — 2 non-redirect entries, 12 nodes** (4 redirect entries skipped)

- Node verdicts: confirmed 8, plausible 2, disputed 1, transcription_suspect 1
- Root verdicts: plausible 2
- Ref checks: supports 6, partial 2, not_checked 9 (all AHD main-text pages 349/762, VOP:318 Moshiri and VGH:65 Khadiv Jam — no digital copies)

Flagged items:
- **disputed — Longos, #3 Greek "loggos" 'grove'**: there is no Ancient Greek *λόγγος; the word is Byzantine/Modern Greek and a loan from Proto-Slavic *lǫ̑gъ. Nourai's own reference says so — IEC p.709 reads "Mod. Gk. lóggos … A Sl. LW for Andrioti" — and this node is the only basis for the root box's extra gloss "also a low land, meadow."
- **transcription_suspect — Lithra, #7 Persian «لیطر»** (`error_in: "book"`): the printed page really does show لیطر with ط (image saved to `data/verification/sources/refs/ocr/BOOK/314.png`), so the extraction is faithful; the form is unknown to Dehkhoda/Mo'in/Amid, which have only لیتر tagged "(فرانسوی)". Nourai re-spelt the French loan with the ط of رطل. Correct form: لیتر (already correctly placed at node #4).

Other substantive findings (not flagged):
- Root **Lithra** is labelled "Indo-European" but Watkins' AHD:1527 entry — which the chart copies verbatim, brackets and all — uses square brackets precisely to mark *non*-IE forms and calls it "Mediterranean word." Modern view: Gk λίτρα borrowed from Sicel *lītrā / Proto-Italic *līðrā, same source as Lat. lībra; Pokorny has no such root. Hence root verdict plausible.
- #6 Arabic: رطل ← Greek λίτρα is confirmed, but via Aramaic līṭrā/rīṭlā (Lokotsch no. 1708), a link absent from the chart; and the modern Arabic لتر 'liter' in the same box is a 19th-c. French loan, not from Greek. Klein (s.v. rotl) contradicts the Greek origin outright.
- #3 French litre goes through litron, not straight from ML litra.
- Root **Longos**: the "lame" half checks out (POK 959-960 (s)leg-/nasal (s)leng-, Watkins slēg-, PIE *(s)leh₁g-), but "also a low land, meadow" is Mann's conflation with Slavic *lǫgъ, which modern work keeps separate.
- Nourai's IEC page numbers were verified exactly (IEC leaf 382 = printed p. 678, leaf 400 = p. 709), as were KLN:886 and KLN:896 (leaves 476 and 482 carry those OCR'd page numbers).

No extraction errors to fix — the JSON matches the printed page throughout.
