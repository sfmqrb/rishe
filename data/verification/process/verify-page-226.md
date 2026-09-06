# Verification process log — verify-page-226


## [2026-09-06T15:18:46.129Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 226 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-226.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-226.json. Write /home/sfmqrb/git/rishe/data/verification/page-226.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 226` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:18:47.622Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:18:48.331Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:18:48.344Z] TOOL RESULT

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


## [2026-09-06T15:18:48.749Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-226.txt"
}
```


### [2026-09-06T15:18:48.769Z] TOOL RESULT

```
1	=== PDF page 226 (book page 196) ===
2	--- entry 0 ---
3	ROOT lâtis -> redirect to lâtos
4	--- entry 1 ---
5	ROOT lâtom -> redirect to lâtos
6	--- entry 2 ---
7	ROOT [Indo-European] lâtos, lâtom, lâtis : going, movement, crowd, turn, period  (refs IEC:441)
8	#1 (parent #0) [Avestan] refs=IEC:441 | yâtem : road
9	  #2 (parent #1) [Persian] refs=IEC:441 | jâddeh «جادّه» : road | NOTE: MON:1202 claims "jâddeh" is an Arabic word while FVF:140 and AFM:39 indicate that Arabic has borrowed it from Persian
10	#3 (parent #0) [Sanskrit] refs=IEC:441 | yâtam : road
11	--- entry 3 ---
12	ROOT lě -> redirect to Ei
13	--- entry 4 ---
14	ROOT lěro -> redirect to Ei
15	--- entry 5 ---
16	ROOT leu -> redirect to Yeu 2
17	--- entry 6 ---
18	ROOT [Indo-European] leuo, Yewo : grain  (refs POK:512)
19	#1 (parent #0) [Avestan] refs=SYN:513; POK:512; KLN:1766 | yava : grain
20	  #2 (parent #1) [Pahlavi] refs=BQT:594 | jav : grain, barley
21	    #3 (parent #2) [Persian] refs=BQT:594 | jo «جو» : barley
22	  #4 (parent #1) [Sogdian] refs=SOD:448 | yw : barley
23	#5 (parent #0) [Greek] refs=AHD | zeiai : grain
24	  #6 (parent #5) [English] refs=KLN:1766 | zea : a genus of grasses
25	--- entry 7 ---
26	ROOT [Turkish] Ijlak, Yelek : sleeveless coat  (refs KLN:656)
27	#1 (parent #0) [Persian] refs=BQT:584 | jalîtqeh «جلیتقه ( جلیقه )» : waist coat without sleeves
28	#2 (parent #0) [Arabic] refs=KLN:656 | jaleco : coat of Christians
29	  #3 (parent #2) [Spanish] refs=None | 
30	    #4 (parent #3) [French] refs=None | 
31	      #5 (parent #4) [Persian] refs=VOP:206 | žîlet «ژیلت ( ژیله )» : gilet
32	      #6 (parent #4) [English] refs=KLN:656 | gilet
33	--- entry 8 ---
34	ROOT lo -> redirect to I2
35	
```


## [2026-09-06T15:18:54.782Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-226.json | head -300"
}
```


## [2026-09-06T15:18:55.490Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat tools/verify_check.py | head -60"
}
```


### [2026-09-06T15:18:56.507Z] TOOL RESULT

```
{
    "pdf_page": 226,
    "book_page": 196,
    "entries": [
        {
            "root": {
                "name": "l\u00e2tis",
                "redirect": "l\u00e2tos"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "l\u00e2tom",
                "redirect": "l\u00e2tos"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "l\u00e2tos, l\u00e2tom, l\u00e2tis",
                "lang": "Indo-European",
                "refs": "IEC:441",
                "gloss": "going, movement, crowd, turn, period"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "IEC:441",
                    "words": [
                        {
                            "translit": "y\u00e2tem",
                            "gloss": "road",
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
                    "refs": "IEC:441",
                    "words": [
                        {
                            "translit": "j\u00e2ddeh",
                            "gloss": "road",
                            "script": "\u062c\u0627\u062f\u0651\u0647"
                        }
                    ],
                    "script_extra": null,
                    "note": "MON:1202 claims \"j\u00e2ddeh\" is an Arabic word while FVF:140 and AFM:39 indicate that Arabic has borrowed it from Persian",
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "IEC:441",
                    "words": [
                        {
                            "translit": "y\u00e2tam",
                            "gloss": "road",
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
                "name": "l\u011b",
                "redirect": "Ei"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "l\u011bro",
                "redirect": "Ei"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "leu",
                "redirect": "Yeu 2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "leuo, Yewo",
                "lang": "Indo-European",
                "refs": "POK:512",
                "gloss": "grain"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "SYN:513; POK:512; KLN:1766",
                    "words": [
                        {
                            "translit": "yava",
                            "gloss": "grain",
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
                    "lang": "Pahlavi",
                    "refs": "BQT:594",
                    "words": [
                        {
                            "translit": "jav",
                            "gloss": "grain, barley",
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
                    "lang": "Persian",
                    "refs": "BQT:594",
                    "words": [
                        {
                            "translit": "jo",
                            "gloss": "barley",
                            "script": "\u062c\u0648"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u0645\u06af\u0648\u06cc \u0622\u0646\u0686\u0647 \u0637\u0627\u0642\u062a \u0646\u062f\u0627\u0631\u06cc \u0634\u0646\u0648\u062f - \u06a9\u0647 \u062c\u0648 \u06a9\u0634\u062a\u0647 \u06af\u0646\u062f\u0645 \u0646\u062e\u0648\u0627\u0647\u062f \u062f\u0650\u0631\u064f\u0648\u062f",
                        "poet": "Sa`d\u00ee"
                    }
                },
                {
                    "id": 4,
                    "parent": 1,
                    "lang": "Sogdian",
                    "refs": "SOD:448",
                    "words": [
                        {
                            "translit": "yw",
                            "gloss": "barley",
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
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "zeiai",
                            "gloss": "grain",
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
                    "refs": "KLN:1766",
                    "words": [
                        {
                            "translit": "zea",
                            "gloss": "a genus of grasses",
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
                "name": "Ijlak, Yelek",
                "lang": "Turkish",
                "refs": "KLN:656",
                "gloss": "sleeveless coat"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "BQT:584",
                    "words": [
                        {
                            "translit": "jal\u00eetqeh",
                            "gloss": "waist coat without sleeves",
                            "script": "\u062c\u0644\u06cc\u062a\u0642\u0647 ( \u062c\u0644\u06cc\u0642\u0647 )"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "KLN:656",
                    "words": [
                        {
                            "translit": "jaleco",
                            "gloss": "coat of Christians",
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
                    "lang": "Spanish",
                    "refs": null,
                    "words": [],
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
                    "refs": "VOP:206",
                    "words": [
                        {
                            "translit": "\u017e\u00eelet",
                            "gloss": "gilet",
                            "script": "\u0698\u06cc\u0644\u062a ( \u0698\u06cc\u0644\u0647 )"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 4,
                    "lang": "English",
                    "refs": "KLN:656",
                    "words": [
                        {
                            "translit": "gilet",
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
```


### [2026-09-06T15:18:56.568Z] TOOL RESULT

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
----
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


## [2026-09-06T15:19:19.285Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:19:19.329Z] TOOL RESULT

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
```


## [2026-09-06T15:19:21.846Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['IEC','POK','SYN','KLN','BQT','SOD','AHD','MON','AFM','FVQ','FVF','VOP','HRN','HUB','PHD','NYB','BRT','WLD','ARY','TTS','LKT','PLA','SKT','WEB','FSD','DEV','DOZ','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T15:19:23.618Z] TOOL RESULT

```
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git
CHEUNG MISSING
```


## [2026-09-06T15:19:53.029Z] TOOL CALL #7: Bash

```json
{
 "command": "pdftoppm -f 226 -l 226 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg226 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T15:19:54.017Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"i̯eu̯o\\|ieuo-\\|jeu̯o\" POK_full.txt | head -20; echo \"=== POK page 512 area\"; grep -n \"Getreide\" POK_full.txt | sed -n 1,5p"
}
```


### [2026-09-06T15:19:56.565Z] TOOL RESULT

```
total 3440
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:19 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    506 Sep  6 11:18 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb 431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb 111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb 118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74322 Sep  6 11:19 pg226.png
```


### [2026-09-06T15:19:56.624Z] TOOL RESULT

```
=== POK page 512 area
46959:Getreidehaufen, Hauste ' (: Lithuanian kupstas); *hufsto\s ablaut equally with Old High 
62211:Material: Gr. AiKpau) " handhabe die Getreidesehwinge ', AiKpr|Tiip "the das corn schwingt', 
62213:AiK|j6g, AIkvov "Getreidesehwinge', diss, from *viKp6(;, *viKVOv, compare vsTkAov, vIkAov, 
62227:Lithuanian niekoti, Latvian niekat 'Getreide durch Schwingen reinigen '; besides 
67620:"Getreidegarbe', Latvian peda^ bundle, armful, armload ', ablaut. Lithuanian puodas,
```


## [2026-09-06T15:20:00.944Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg226.png"
}
```


### [2026-09-06T15:20:01.566Z] TOOL RESULT

```

```


## [2026-09-06T15:20:01.563Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T15:20:09.330Z] TOOL CALL #10: Bash

```json
{
 "command": "pdftotext -f 226 -l 226 EtymologicalDictionary-persian-english.pdf - | cat -A | sed -n 1,60p | sed 's/\\$$//'"
}
```


### [2026-09-06T15:20:11.209Z] TOOL RESULT

```
^L
```


## [2026-09-06T15:20:26.562Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg226.png')\nprint(im.size)\n# header approx y=155*1.65, x=360*1.65\nim.crop((560,220,900,290)).resize((1360,280)).save('c_hdr.png')\nim.crop((560,300,1000,370)).resize((1760,280)).save('c_latis.png')\nim.crop((560,1250,1050,1330)).resize((1470,240)).save('c_ieuo.png')\nim.crop((560,1870,1200,1950)).resize((1920,240)).save('c_ijlak.png')\n\"; ls"
}
```


### [2026-09-06T15:20:28.488Z] TOOL RESULT

```
(2550, 3300)
agents.txt
bqt1854.png
bqt2023.png
bqt2420_fn.png
build213.py
c1.png
c2.png
c_gacele.png
c_harmathan.png
c_hdr.png
c_herman2.png
c_herman.png
c_ieuo.png
c_ijlak.png
c_latis.png
c_mag.png
crop1.png
crop2.png
crop3.png
crop_germ.png
crop_guthjo.png
crop_habl.png
crop_node12.png
crop_node1.png
crop_varathra.png
c_xzn.png
gen215.py
jscheck.js
mk201.py
mk207.py
mk208.py
mk214.py
pg201.png
pg204.png
pg206.png
pg207.png
pg208.png
pg209.png
pg211.png
pg212hi.png
pg212.png
pg213.png
pg214.png
pg215hi.png
pg215.png
pg216.png
pg217.png
pg218hi.png
pg218.png
pg219.png
pg220.png
pg221.png
pg222hi.png
pg222.png
pg223.png
pg224.png
pg226.png
```


## [2026-09-06T15:20:31.260Z] TOOL CALL #12: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_latis.png"
}
```


### [2026-09-06T15:20:31.279Z] TOOL RESULT

```

```


## [2026-09-06T15:20:31.536Z] TOOL CALL #13: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_ijlak.png"
}
```


### [2026-09-06T15:20:31.555Z] TOOL RESULT

```

```


## [2026-09-06T15:21:02.337Z] TOOL CALL #14: Bash

```json
{
 "command": "sed -n 60,200p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:21:02.381Z] TOOL RESULT

```
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


## [2026-09-06T15:21:03.749Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC yāt\"; grep -n -i \"y[āaâ]tos\\|i̯ā-tos\\|iātos\\|ia-tos\" IEC.txt | head -20; echo \"=== IEC page 441 tag?\"; grep -n \"441\" IEC.txt | head -5"
}
```


### [2026-09-06T15:21:03.824Z] TOOL RESULT

```
=== IEC yāt
6354:iātos, om, is ‘going, movement; gang, crowd, shoal; gait; turn, period, Cf. jà-, -mi, Gig Skt. yatàm; Av. yatom; Per. jade (&highway'. j = Ð; Ir. áth *ford'; W iawd ‘season, time; OCS jato (‘army on the march’, ambig. cf. oit-); Srb. jato ‘flock’; Slovene ‘gang, swarm’; Blg. “flock, shoal" (all ambig. cf. oit-); Li. jótas ‘mounted, on horseback’; jotis, ies ‘riding’
=== IEC page 441 tag?
6347:441
6678:kalos, is (1) “black, blackened, stained; stain’. WP I, 441. Cf. qual- (Slav & Skt. am- big.) Skt. (ambig.) kalah ‘black’; Romani kalo, id.; Lat. cf. calo, gs -onis 'camp-follower'; cal-1go ‘darkness’; càl-umnia ‘blackening of a charac- ter”; Ir. cf. caile (stain, fr. *kal-i-); Gk. kelís, id.; Cz. R kal, Pol. kat (ambig. ‘dung’. Cf. qual-); OE cf. hol *calumny'; cf. Li. kólioti, v. ‘abuse’; dim. extn. in Lat. caliculus *inkpot
9785:louó (1) Jong, ið ‘wash, bathe, soak, swill’. WP I, 441 Arm. luam ‘wash’; Hitt. lahuhi "pour" beside lahwahi, id., and lahhus, s. “basin”; Gk. loúo, louéo, loéo *wash, bathe'; Alb. laj, id.; Lat. luo, Gre “wash away’; -Iuo, cpds. “wash? beside lavo, are, pf. làvi, id., sup. lautum & lotum; Umb. cf. vutu! uetu! (Lat. luito!) *wash"; MHG 10, gs lowes, sn. “tan, tanbark'; G Lohe (2), id.; Du. looi, id.; loien, v., Fris. loaije, v. ‘tan, steep’; Gk. cf. lá-sana, npl. (^wash- stand”, fr. a type *lou-tuon-, cf. sanís ‘board’);
10071:loughos, io ‘wash, washing-pool, lye, buck’. WP II, 441. See lougho OHG louga; OE leah, f. “lye*; ON laug, pl. -ar, f. ‘bath’; lauga, wv. ‘bathe’; Arm. cf. loga- nam, v. id.; (prob. LWs in) Srb. lug, Cz. louh, m. "lye-ash, lye’ but cf. OCS luža, Cz. louže, f. ‘puddle’ beside (alleged) OCS lugü, m. ‘scented bath" and Cz. koZe-luh ‘tanner’. Du. loog, f., G Lauge, f. as OHG & OE. (A "LW for Holub-Kopeény; ‘not a LW?’ Mlad.)
10113:loutér-, loutro-, louotér-, louotro- ‘ablution, bath, bathtub’. WP II, 441 Myc. lewoter- ‘bathtub’; Gk. lóetron, loütron, loutrón ‘ablution’; Lat. lüter, gs lüteris, m. *"mixing-bowl' beside lavàcrum ‘washbasin’: Ir. lothar, m. “trough; cauldron’; Gaul. lautro
```


## [2026-09-06T15:21:15.380Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 6340,6360p IEC.txt"
}
```


### [2026-09-06T15:21:15.424Z] TOOL RESULT

```
iák- "brightness, beauty’. Cf. ioK-, ök- and WP I, 172 Skt. yásas, n. ‘beauty’; Cz. jas ‘lustre, gloss, joy’; W (ambiguously) iawg (Ckeenness', but see loK-) .
ialo ‘exult, revel. Cf. WP I, 775 Gk. cf. denom. zelóo *be zealous' beside Hes. ialía ‘voice’; OBr. iol- ‘pray’; W ioli “praise, worship’; MLG jolen ‘exult’; Du. joelen “re- vel, exult’. See next
iålos, à ‘revelry, ecstasy, fervour, exultation’. Cf. WP I, 775 & ialo Gk. zélos, (Dor. -a-) ‘religious fervour, zeal’; W iawl ‘worship’; OE geol ‘Yule’; ON jól, npl., id.; G (fr. LG) cf. Ge-johl ‘whoop’; Du. joel (also jool, fr. Fris.?) ‘exultation, merriment’; Finn. LW joulu ‘Yule’. Isophonic: Srb. Slo- vene: jal ‘envy’. (For Per. yara ‘boldness, power’, see iðr- (3))
iami, see iàio
iáqueio ‘go and seek’. Cf. iā- and quëið Skt. yácàmi (base: yáča-) “beg, ask’; Gk. zetéo, Aeol. zátémi “seek, ask for, study’; cf. -étiáo in khez-etiáo. (For the first element, cf. OCz. ja-dati ‘to search").
iaquos ‘brave, excellent’. (Correl. of a type tà-quos) Srb. Blg. jak, OCS jakü “such; strong, fit’; Cz. jaký “what sort of’; Li. joks ‘any’; cf. Srb. ja- Cam se ‘recover, revive": Li. jokejuos, -ētis, id. (For Gk. n-épios ‘childish’ and Cz. ne-japa ‘clumsy person’, see ap- and cf. -epelía “strength? in some cpds.). Short vowel in Gk. ássa, hássa, hátta “whatever”
iárim- (iarm-) “join, joint, yoke’. See next
441
and cf.ar-, arm- & WP I, 72 Tokh. A yärm-, B yarm-, v. ‘measure’; Myc. cf. a-ja(r)meno- queried: ‘not fitted’; Gk. har- mós “joint” beside árma ‘union’, ármena, npl. ‘rigging; outfit’: OCS jarímü (“yoke”, and com. Sl.)
iáro, ið (1) “fit, join". Cf. ar-, arm-, iarim- and WP I, 72 Arm. (ambig.) harem, id. (fr. *iar- or *en-ar-); Ir. oirim “suit, fit’; Pol. cf. ko-jarzyC “join, combine”
jaro, ið (2) ‘rave’. Variant of ioro, ið, q. v. Evidence ambig., but forms are based on ono- matopoeia; cf. LG joren "be peculiar’; Icel. mig órar, id.; ON óra ‘rave’ (loss of initial as in ostr ‘cheese’: Finn. LW juusto, (?) but equally to Lat. oro, orare pray"); OCS cf. jaru! ‘come on; Latv. jarëties ‘rave’. See next, and cf. R jarit'sa, refl. ‘rave’
iáros, is ‘uproar, violence’. Slav. forms am- big. Cf. jaro, ior-. WP I, 197 OCS jarð ‘violent’; R jàryj ‘irate’; cf. ant, v. ‘provoke’; Latv. jāris ‘din, uproar’
iās-, sigmatic variant of theme iā- ‘go’ Skt. cf. á-yāsişam, 3s: á-yāşīt, impf. "went: OCS jaxavü “having departed’; jaxati, v. ‘go, ride’; Latv cf. jāšus, adj. ‘riding’
iät- “power, force’ Skt. yàtüh ‘sorcery; demon’; Av. yātus “magi- cian’; yātu ‘demon’; Per. jådu ‘magic’ (j = £); Tokh. AB yāt- ‘tame, overpower; be able’; Gk. cf. zētrós ‘executioner
iātos, om, is ‘going, movement; gang, crowd, shoal; gait; turn, period, Cf. jà-, -mi, Gig Skt. yatàm; Av. yatom; Per. jade (&highway'. j = Ð; Ir. áth *ford'; W iawd ‘season, time; OCS jato (‘army on the march’, ambig. cf. oit-); Srb. jato ‘flock’; Slovene ‘gang, swarm’; Blg. “flock, shoal" (all ambig. cf. oit-); Li. jótas ‘mounted, on horseback’; jotis, ies ‘riding’
iaulo, ið ‘howl, yowl'. Onomat. (Variant: iaudhl-). Cf. iauuo Ir. uaillim, id. (fr. *iaudhlio); G jaulen (beside jauteln), id.; LGer. jolen (if -o- here; if -0- to ial-, q. v.); Du. cf. jool (if -oo- is secondary: ‘jollity’. Eng. yowl represents a variant of type *iül-)
laur- (quick, soon, early; speed Cf. aur-,
iáro, ið — iekso (ieks-)
20
25
30
```


## [2026-09-06T15:21:16.566Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT yāta\"; grep -n \"y[āa]ta-\\|yātǝm\\|yātem\" BRT.txt | head -30"
}
```


### [2026-09-06T15:21:16.627Z] TOOL RESULT

```
=== BRT yāta
3569:•  j.  apa'yata-  Adj.,  PPfP.:  s.  yam-.
4491:•  j.  an-upa'yata- ''  Adj.,  nur  fem.  °tä- 'die  noch  nicht  begattet,  noch  unberührt ist':  kanyqm  ashndqm  'tarn  V.i4.i$.
12935:•  j.,  g.  daradi^i  InC  i)  'in  seinen  Besitz zu  bringen,  sich  zu  erwerben':  kads  .  . uxfanS  (sd.)  asnqm  anhJuf  d'  frö  alahyä /rannt!  ".  .  auf  das  die  Welt  das  ^a sich  erwerbe"  Y.  46'.3.  3)  'au&ufassen, zu  vernehmen':  uH  ahurahe  masda  yata- maide  d'  mq%rahe  spmtahe  . .  xratüm  .  , marä^rai  .  .  Aitvqm  .  .  fravakai  "wir  ver- ehren die  Ohren  (das  Gehör)  des  AAM., dass  er  das  heilige  Wort  vernehme, . .  die Gedächtniskraft  . .,  dass  er  (es)  behalte, die  Zunge  ,  .,  dass  er  (es)  verkünde"  Yt
19790:Adj.:  °nff  voha  umnasÜa  alaonqm  yata- maidS  Y.^,4'*;  s.  Y.  49.  10,  Sp.1137 u.;  —  hau^a  *anayä  narä  voÄu  °nS Jägfv&uKarff  isd.)  anhai  V.  4.48*';  — am»ia  sp^nia  .  .  hsta  (Sp.  938  o.)  kaca vanhaot  'tianhai  Vr.  //.  1 2  *' ;  —  spmtaf haca  manyaoi . .  taSqm  Hhnm  voAiÜäaica 'nanhat  FrW.  10. 40  '■'.  a)  im  Gegen- satz zu  Spiechea  und  Handeln:  yai 'kwa  didüa^a  yezi  'nanha  .,  valatfha  .. ^«oS«a  Y.  7.  31;  Vr.  22.  2;  —  t»m  yazata . .  eara^uitrS  v^nhraynahe  patH  °nahi  . . vacahi  .  .  syaa^tte  YtJ^aS;  —  Jira  vS rähX .  .yasnsmüa  vahmsmla  f?ra  'nanhä . . vacatshä  .  .  fyaöhar^  Y.  //.  18; — patitmt ht  'nä  .  .  vacS  .  .  ryaohn^m  V.  7,  51;  51;
19901:140;  —  mi^mm  .  .  3^ar?na>?uhasbm»m 'yavanqm  yataianqmYt.  ig.  ZS'i  10.  13,  16, I4-J,  4-3,  y.  2^-3 ;  —  vXspimca  aidvamm 'yaom  yazatim  .  .  *ga^fm  yasatim  yaza- maide  Y.  16.  i  f.,  25.  8 ;  —  xshsvayati  vTspe •yavaäi  yaiata  ^gaa^ya/a  YL  6.  4;  Y. 16.  9,  7/.  5,  FrW.  1.3;  —  x^tümaine  yata- tanqm  afaenqm  'yavanqm  ga^yanqm  Y. J.4;  22,37,  V.ip.30,  Yt-^S,  ig.33;  — *Aist»nte  'yavir»kö  yazatiahs  .  .  Yt  (f .  i ; —  nava.ai  'yava  yasata .  .paiHstqm  vlimti yt5.3;  G.2.6;  —  yazataHbyS 'yaeUiyasca^ gaHä!yaäbyascäY.i.i^; — ha%ra  'yaoibyS^ yatataiibyS  V.2.ao.  zu  b):  m^r»m  .  . yahmai  haca  frat^nsittti  vTspe  'yava  daeoa yalca  vanttya  drvanis  Yt.  iO.  97;  V,  Ä  31, 32;  —  da^anqm  'yavanqm  V.  Ä  80;  — mq%rB  spmts  'y>vfm  drujam  niibairiltS Yt  II.  y,  —  tä  Al  snai^i/ca  .  .  vlstnie pairi  'yaoyät  drujat  ^vannyi^äatÜa  *drDS.- iiyaj  Yt.13.j1. Ableit.  aus  mainj'iiii-.  —  np.vgl.mriw  'Himmel'. —  Pü.;  menöt,    Sü.:  farahtacori,  /tiraiiiiyaJi,
21083:j.  yata-  Adj.,  PPfP.:  s.yam-. KompE.
21269:•  h  S>  P-  'y^'oa-  V.  'halten; fassen'.  Praes. I  yam-,  14  yasa-.  —  PPfP.  'yata-;  PFP. apayanta'  (Ableit);  Inf.  'yatie,  °yätT, 'ynne.        S.  noch  'yäta-,
21277:mit  upa:  s.  anupayata-.
21408:(Fürs  jAw.  unvollständig.)  Im  Praes.  3 fast  nur  Med.  I)  mit  persönlichem  Objekt '(eine  Gottheit)  verehren,  feiern,  ihr  hul- digen, ihr  zu  Ehren  Gebete  und  gottes- dienstliche Handlungen  verrichten' :  II  o*»ra*- mazänin  *yatiätaiy^'  Bh.5. 6;  —  »äJ  a/ yazamaidf  ahursm  masdqm  ..  asäunqm  fra- vahs  yazamaids  assm  at  vahiiigm  yata- maide . .  vohuiä  manu  yasamaiäe  Y.  57. 1,
21433:yasna  yatayanta  (Opt.)  yäha  anye  yata-
21536:ia83  'yata-
21699:mit  aiwi  i)  'etwas  sich  umtun,  anlegen, anziehen'  (den  Gürtel,  Kleidungsstücke): aiwyäahantm  va  aiwyanhayamnS  aiw- yäffhamm  vS  ia/ayamnä (sd.)  Yt  i.  i  ?;  — ya  hama  *aiwyär9Aana  (sd.)  aiwyanha- .yänti  N.g4;  —  aat  aiähe  (näml.  aiwyata- hanahe)  ahi  aiwyUstS  *banlnuS  paiH  . . Y.  p.  26;  —  aiwi  vastra  yäwAayanuha "zieh  deine  Kleider  an"  V.iS.iq;  — ,  vastra  .  .  aiwyänhayaäa  V.p.  32;  —  yS vastra  vastrim  *aiwyarfhaya7iti^'>  N.55(?);
22568:—  vattaintyssla  uparaläts  Vr.  /.  6 usw.  I  a)  insbes.  vom  Sieg  in  dem ! inneren  Kampf  zwischen  Gut  und  Böse  | (vgl.Y.49.4):  afiunqm  . .  yaiiqm  vahehir, damh  vanainit  vs  vsnghm  vä  vaonarS  va  1 "der  Gläubigen  . .,  deren  besseres  Ich  den Sieg  davonträgt  oder  davontragen  wird  I oder  davongetragen  hat"  Y.^5.  2'°';  zit.  r Ytzj.  154  (wo  V3f3km)\  —  vamntqmi vaahmtqm"^  *vaonuiqm'^  daiiil!.-\ säikm  .  ,  alaonqm  aiaoninqmca  .  .  YtJJ. 155;  —  mit  Dat  comm.:  asaonqm  ysi vaonar»^^  ".  .  die  zu  Gunsten  des  Aia den  Sieg  davongetragen  haben"  Y.  26. 4, 5.  b)  mit  Inhaltsakk.  aus  vanatay  {. 'Sieg':  sraosahe ..vanata vanaitls  vanaiti- vats  a^aonS  vanatö  (s.  i)  vanaitls . . yata-  janlt  \.g.a  _ maide  "des  Sr. . .,  des  Siege  gewinnenden,  l  mit  »/'gewinnen;  habhaft  werden':  juän sieghaften,    heiligen,   siegenden    Siege  .  .^ainn..masa  x/aira   nivsnäni  Yt5.i3o;
23749:Arbeit":  ya^  bü  paiti  .  .  ai^hi  i.fmS  naire asaone  °yat  asaya  äaiäiti  "wo  man . .  dem Gläubigen  für  seine  Arbeit  zahlt  wie  es rechtens  ist"  V.J. 34;  35.  2) 'Betätigung'; tnasilta  mqhra  .  .  °ya  (IS.)  .  .  urvüitya  .  . hai%yä.v3ntya  .  .  dalnaya  matdayasnsi! G.  2.  7,         S.  noch  v»r>zyata-  mit  No.  z.
29338:•  j.  han-k^rsS-a-  Adj.  'vollzogen,  voll- cndef ,  von  h!ak-  im  Gegens.  zu  aväurusta- (sd.)  'vollkommen  gesprochen':  väca  °%a ..gähanqm  avävrusta  (Sp.  1494  ui.)yata- maide  Y.  71. 18.
```


## [2026-09-06T15:21:25.811Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 21520,21560p BRT.txt"
}
```


### [2026-09-06T15:21:25.862Z] TOOL RESULT

```
mit  apa  i )  "weggehen  von  — '  (Abi,) :  apa aiat  frabirita  altäibyS  xaoi^rabyS  yäiti (Konj.)  yanhqm  .  .  N.  ?/(?).  2)    'ent-
gehen', mit  Abi.;  kaomsm  yim  nivUatH riivandäi  {sd.)  apayeiti  Yt.  1^,57,
mit  upa  'herzugehen,  -kommen':  3a/  tat dunmqn  fi-asäupayäü  (d.  '\.fi-ala  -(-  upay")  ■' marye^ara  "und  dann  kommen  die  wolken- bildenden Nebel  herangezogen"  YL1S33, Vgl. '<?>'-;  die  Formen  der  beiden  Basen  sind nicht  immer  sicher  lu  scheiden.    S.  auch  zn frayäi.  —    ai.  yäli  'er  geht".    —   Pii.  (lu  N.): ap^  ^tatoil.  —  ')  S  J04  IT-  31.  ^*-  33-
•  j.  *yä-  Adj.  (auch  fem.)  'gehend'. KorapE.  —  ai.  'ya-  Adj.  —  VgL  za  frayäi.
•  g.  *yäat''  Adv.  'seit  (dem  dass  — )';  es folgt  Perf.;  y  yusta  framXmaha  (sd.)  ya marya . ,  vaxs?nU  daevSsuUa  (sd.)  Y.  J2.  4.
AblSn.  (nominaler  Bildung)  aus  ya- ;  eig,  'ex qno'.  —  aL  yaf  Konjn.  'seit'.  —  PB.:  :*i"  haf an.  —  O  So  richtig  Mf  1  usw.;  s.  auch  Pt4. Vgl.  äal  No.  6.
•  g.  yäiä  Adv.  "wie';  i)  'so  wie,  sicut': yä  JSyä  sSnghaiti  y  sr3vT  :^amä  ayataks ". ,  sicut  auditur,  . ."  Y,_J2.  7.  a)  'in weicher  Weise,  wie',  hinter /aA-  'sehen': ysi  pisyeirat..y  gqm  karapü  usixi{sd.)cä aisfmai  data  ^J(Sp.  1197  u.)c^  kavä  .  . urüdöyati  (sd.)  Y,  44.  ao,  yaÜ  ä: sbes.
IPn,  aus  ya-.  —  Pü. :  ke.
•  gAw.  yiis  ä  adv.-artige  Verb,  'aufweiche Weise,  wie':  /rS  mä  si/a  (sd.) . .  *vao^adhi .  .  yais  ä  arghui  *paourt^  baoat  (sd,) Y.2&11.
IPn.  aus^o-;  vgL  Sp.302m.  —  Pü.:  ki  andar iu*flH  fralum  bül.
•  j.  yäkar-  n.  'Leber':  'kan  F.Jg.
Vgl.  ai.  yäirl;  mp,  (Pü.)  jakar,  np.  ßfort). Weiteres  bei  Hau.  AGr.  r.  452.  —  ')  j.  yä- kar) :  np.  jig-at  =  j.  sävar/  (sd.)  :  np.  sA" ;  vgl.
I      auch  Bthl.  BB,  //.  125.
I  •  j.  "gycS  yagara"  V.  5. 48  RiZ.
•  p.  yätä  Konjn.  i)  'währenddem  dass': y   adarn  parsaiy  .  .  akam  .  .  bäbiruvtyä
dby  Google
ia83  'yata-
Aami'i''iyä  abava'  Bh.  J.  13;  2.  3;  —  iyaiy paruvä  xiäya%iyli  y  "  äha'  avaOam . .  "die fiUheren  Käsige:  während  dem  dass  sie waren,  ist  von  ihnen . ,"  Bh.  4,  9,  a)  'als' mit  vorausgehendem  *'itäakiy  ('damals'); imaiy  martiyä  tyaiy  *adakly  (sd.)  avadä ah^ta  y  adam  gaumätam  .  .  avsjanam Bh.  4-  18.  3}  'bis  dass':  adam  hamata-
xlaiy  y  viharn  tysm  amäxam  ''gn'kavä avästayam  ". .  bis  dass  ich  unser  Haus wieder  an  seinen  PlaU  gestellt  hatte"  Bh, i.  14;  13;  —  va*umistr  Hlä  mäm  amll- nayt^  . ,  y  adam  arasam  Bh.  2. 1 1 ;  6,  9 ; —  a  urc^matdä  upastäm  abart^  y  im<^ xiah'^am  adlriy  Bh./.  9;  D.  6.  5.
Ads  ya-,  S  aj3.  4"),  —  Vgl,  Dbb.  Vg!S.  3. 334.  —  >)  Aas  a  ergänit  nach  Eü.  ^.  — •)  Salemanns  Aonabnie  GIrPh,  /.  318,  dus mp.  Oi,  np.  tä  anf  yjtä  zurückgehe,  balte  icti fiir  unmöglich.
•  j.  'yäta-  n.  'der  Jemandem  zugewiesene Anteil;  Besitz':  myazdavh  raiui  amyasda- vatam  raiunaim  *tfm  gal'hanqm  frapirf- naotti  ". .  verurteilt  den . .  Laien  zum  Ver- lust seines  Anteils  an  Hab  und  Gut"  A. ^.11;  —  bao6asca  urvStitmla  'Um  gaz'ia- natu  paiti.jaihydnti  dahm  astvainti  aahvB **, .  befragen  sie  nach  dem  Anteil  an  Hab und  Gut,  der  (dem  Verstorbenen)  . .  ver- lieben war"  V.jp.  29";  F.^f
Ableit.  —  Eig.  'was  (vom  Schicksal)  gewährt, lUgewieseQ  isl'  (s.  iai.'a-);  l'PfP.  lum  V.^am-, vgl.  IF. //.  141  undj'Jmi- mit  No.  1.  — wp.yäl, yälak  m  yälg^  (Päz.  jSdangS),  yälaigäw 'Yvt- Sprech,  Sachwalter'  ;s.  Hbm.  AGr.  l.  231,  IFAni. Ä43*'-  —  Pü-!  bahr{i  gehänX  »"äslak  {i gtili). —  >)  Um  danach  dessen  Wohltätigkeitsstnn zu  bemessen.  —  >)  Aber  die  eigentliche  Be- deutung des  mp.  Worts  ist  anders  als  dort lu  beslimmen.  Falsch  KZ.  j/.  553.  —  S. übrigens  auch  zu  vazö.v^'ieya-  No.  3.
•  j.  'yäta-  n.  Terni.  techn.  für  die  der Schwere  nach  dritte  Art  von  Körperver- letzung"; %rUäm  tarS  x^araya  (sd.)  .  . vUp)m  larS  *yär?Jräjahehim  °t)m  ästrydti N.42i  F.4f.i  —  'fa  raifqm  . .  N.77T{?).
Eig.  Bed.?  —  ?ü.:  ySl.  —  O  Sva.  asiö.iid- i^ara-;  Bthi.  1F.  It.  14z.
•  j.  *yäta'mant-  Adj,  'reich  an  Besitz, vermögend':  maiyänam..  •maiam  V.20. i.
Pü.:  hshremand,  erb:  ttwätilk  hgdn  päUsrav {'..  wie  /■.')!  ».  dazu  Dst.  ZA.  s.  177.  —  1 ')  Hds.  yälum';  s.  aber  Pü.  und  ^yäla-.  '
•  j.  yätav-  -.y-ihw-  ra.  i)  'Zauberei,  Be-I hexung*:  •'hwa  (IS.)^a?S-ä  aiahe  mtrr/tntt V.  8. 3.         3)  'Zauberer',  d.  i.  der  durch '
yätumant-
19S4
Zauber  den  Masdayasncm  Schaden  zufUgt:
vi  (nämL  sanm   mruyt)   'tui  (IP.)'*   vt
yatumalbli  Y.  12. 4;  —  nöii  ""«"(f  (sUtt  NS.)
nBit  yätumh  Yt  15.  56;  —  "'/«  (statt  AP.)
.  .  vanat  Yt.  2.  1 1 ;  —  frShnntal   atsrS
mainyul aya  °/ora(AP.)  V./.13.       3)sonst
in  Verbindung  mit  pairiks-  (sd.):  yim  n5i£
m?rrfgnle  (sd.)  nSit  'tavB  pairikäsca    noit
'tavS  malySnqm   Yt.Ä44;  r.6;  —  yä^a
attm  laurvayeni  vXspe  'tavö  (als  AP.)  pairi-
khsca  YL/.6;  /p.29,  V.20. 10;  — iboils  .  .
'^vqm  pairiianqmf^a  Y.p.18;  F.4i.,  Yt
```


## [2026-09-06T15:21:26.962Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls POK*; echo \"=== search ieuo\"; grep -n \"i̯eu̯o-\\|ieuo-\\|jeuo\\|i̯éu̯o\" POK_01.txt POK_02.txt POK_03.txt 2>/dev/null | head -20"
}
```


### [2026-09-06T15:21:27.030Z] TOOL RESULT

```
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
=== search ieuo
POK_02.txt:2546:ieuo-  , Getreide',  vor  allem  , Gerste'.
POK_02.txt:2548:hom.   att.  leial  f.  PL  , Spelt',   hom.    ^sldcuQog  ,Getreide   hervorbringend' (für   *^eJ^6Sü}Qog)^    q)vaL-^oog   (ala)   , Getreide   hervorbringend'   (:  ieuo-s s^-g)Q(i)v :  cpQifjv) ;
```


## [2026-09-06T15:21:52.026Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 2535,2570p POK_02.txt; echo \"=== page markers near\"; awk 'NR>=2400 && NR<=2560 && /^[0-9]{3}$|Seite|^\\s*51[0-9]\\s*$/' POK_02.txt | head"
}
```


## [2026-09-06T15:21:53.617Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK i̯ā- gehen\"; grep -n \"i̯ā-\\s*,gehen\\|i̯ā- ,gehen\\|i̯ā-  ,gehen\" POK_01.txt POK_02.txt | head -10; echo \"=== ei- gehen\"; grep -n \"^ei-\\|ei- ,gehen\" POK_01.txt | head -10"
}
```


### [2026-09-06T15:21:54.085Z] TOOL RESULT

```
WP.  I  203  f.,  WH.  I  724  f.,  Trautmann  109.
ieug-  ^aufregen,  unruhig^
Av.  yaozaiti  ,regt  sich  auf  (vom  Wasser,  ,  von  unruhigen  Ländern)', yaöHi-  ,Rührigkeit,  Regsamkeit';
arm.  yuzem  ,rege  auf'  ist  iran.  Lw. ;
got.  ßuka  ,Zorn,  Streit',  jiukan  ,kämpfen',  mhd.  jouchen,  jauchen  ^treiben, jagen'  und  ags.  geocor  ,full  of  hardship',  geocre  Adv.  ,streng';
toch.  A  yok-,  AB  yuk-  ,besiegen'.
WP.  I  203,  Feist  301  b.
ieu-ni-  oder  iou-ni-  etwa  ^angewiesene  Stätte,  richtiger  Weg'.
Ai.  yöni-  m.  ,Aufenthaltsort',  f.  ,Mutterleib',  av.  Akk.  Sg.  yaondm  »Weg*^ (wohl  aus  yaonim,  siehe  Wackernagel  KZ.  46,  266);  dazu  ai.  syond-  ,b( haglich'  aus  *su-yond-,  Wackernagel  KZ.  61,  203 f.;
air.  uain  f.  , Gelegenheit  (d.  i.  richtiger  Platz  =  richtige   Zeit),  Mußj Zeit'.
WP.  I  204;  wohl  zu  1.  ieu-  ,in  Bewegung  setzen'.
ieuo-  , Getreide',  vor  allem  , Gerste'.
Ai.  ydva-  m.  ,Getreide;  Gerste,  Hirse'  =  av.  yava-  m.  ,Getreide','^ npers.  jav  , Gerste'  (==  lii.javat)'^  ai.  yavya-  m.  ,Fruchtvorrat'  (:  lit.  ^a«;aj ,Scheune');  yavasd-  n.  ,Gras,  Futter',  av.  yavaidha-  n.  ,Weide';  av.  ydVlriA m.  , Getreidefeld' ;
hom.   att.  leial  f.  PL  , Spelt',   hom.    ^sldcuQog  ,Getreide   hervorbringend' (für   *^eJ^6Sü}Qog)^    q)vaL-^oog   (ala)   , Getreide   hervorbringend'   (:  ieuo-s s^-g)Q(i)v :  cpQifjv) ;
lit.  jävas  m.  , Getreideart',  java%  PL  , Getreide',  jduja  , Scheune'.
WP.  I  202  f.,  Trautmann  107.
ie^os-  etwa  ,Satzung,  Fug' ;  vielleicht  als  ,Verbindlichkeit'  zu  2.  *jet<-  ,ver- binden'.
Ai.  yöh  n.  ,Heil!'  (nur  in  Verbindung  mit  ^dm-^  zur  Form  s.  Bartholomae Airan.  Wb.  1234) ;  av.  yaoHa-däiti  ,macht  hell,  reinigt  rituell' ;
lat.  iüs  ,Satzung,  Verordnung,  Recht'  (alat.  ious  aus  *iouos,  vgl. :)  iüstm (alat.  iovestöd)  ,gerecht' ;  jürö,  -äre  ,schwören'  (alat.  wohl  in  iouesat  Duenos- Inschr.),  über  jürgö,  iniüria]  pe(r)ierarej  ejeräre^  deieräre  (tief stufiges iüsä-)  s.  WH.  I  732 ff.,  EM.2  506 ff.;  über  judex  ,Richter'  s.  oben  S.  188, WH.  1726;
air.  huisse  ,gerecht'  (*ius-t{o8).
WP.  I  203,  WH.  I  733  f.,  870.
513
io-  Relativstamm,  s.  oben  S.  283.
ioi-ni-  ,Binse^
Lat.  iuncus  ^Binse*^  (*ioini-ko-s)  gehört  zu  mir.  ain  ^Binse^  {*ioini-), Gen.  aine]  über  lat.  iüniperus  ^Wacholderstrauch'  s.  WH.  I  731,  870 und  Leumann  Gl.  27,  74;
aisl.  einiTj  schwed.  en  ,Wacholder^,  ndd.  en(e)ke  ds.  falls  aus  *jainia-, ■wodurch  der  Bedeutungs Wechsel  Binse :  Wacholder  (s.  oben)  als  alt  ge- sichert würde.  Doch  ist  dann  bei  mnd.  eynJiolz  und  nhd.  Einheerhaum (aus  aisl.  eini-ber  , Wacholderbeere')  Einfluß  von  ein  ,ein^  anzunehmen.
WP.  I  208  f.,    Kluge  11  126.
iofk-  _,Tier  aus  der  Gruppe  der  Rehe^
Gr.  ^OQ^j  ^OQy.ag,  mit  volksetym.  Anschluß  an  dsQxofxai  meist  ööq^,  öogy^ög-, dogycdg  f.,  dÖQy.og  m.  ,Reh,  Gazelle^;
gallo-rom.  *iorkos  ,Reh',  cjmr.  iwrch  ,caprea  mas',  corn.  yorch,  bret. iourc'h  ,Reh'  (vermutlich  aus  dem  Keltischen  stammen  die  späteren  ver- einzelten Formen  tb^xog,  io^xsg,  Yvoxeg  bei  Opp.  und  Hes.);  gall.  FN  Jurca.
WP.  I  209;  M.-L.  9678.
iou,  iu  .schon'^,  s.  oben  S.  285.
iö[u]s-  :  iüs-,  (vermutlich  zu  2.  ieu-)  , gürten^;  iös-to-s  ,gegürtet^,  iös-men- n.  ,Gurt'.
Av.  yäti^hayeiti  (meist  mit  aiwi-)  ,gürtet^,  Partiz.  yästa-  ,gegürtet^,  yäh n.  ;Gürtelschnur^;
gr.  tibwvixi  ,gürte',Xf^(TT6g  (=  av.  yästa-,  lit.  jüostas)  , gegürtet',  CcüOtt^q ,,GürteP,  ^ü)^a  ds.  (^toja-^a  vgl.  lit.  juosmud  ,Gurt'),  ^cowj  ds.  (%a)a-vä, vgl.  russ.-ksL poj asm  ds.);  ^ovad-o)'  Liawvad-u  Hes.  etwa  thessal.  =  ^cbaS-o)?
alb.  n-gjehs  ,ich  gürte';
=== page markers near
505
506
507
508
509
511
513
```


### [2026-09-06T15:21:54.187Z] TOOL RESULT

```
=== POK i̯ā- gehen
=== ei- gehen
4331:ei-el-  in  lit.  ielekstis  f.  ^Deichselstange^;  lett.  ieluksi,  ablaut.  ükss,  ükmU ds.;  lit.  alle  ^Stange^,  iem.  dilis  ^clava'^,  lett.  ailis  ^Stange^;
4332:ei-en-  in  lit.  iena  f.  ^Deichselstange';
```


## [2026-09-06T15:22:06.078Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN barley\"; grep -n -i \"BARLEY\" SYN.txt | head -10"
}
```


### [2026-09-06T15:22:06.132Z] TOOL RESULT

```
=== SYN barley
82:The two most general types are generalization or extension vs. specializa- tion or restriction. Generalization, as in barn etymologically ‘barley-plece’ whence storehouse for any grain or farm produce (now even carbarn), mill originally ‘machine for grinding’ (corn, etc.), and all words of such broad application as do, get, go, thing. Specialization, as in deer (see above), hound, originally any ‘dog’ (like NHG hund), sermon from Lat. sermé ‘dis- course’ specialized in church writings. The history of a given word may show successively a specialization and generalization from a new center, as starve from ‘die’ (as NHG sterben) to ‘die of hunger’ to ‘suffer from hunger’. But this classification is from one point of view only, that of scope. There are many other more specific types of shift within certain associated groups.
8399:ChSl. brasino (in Gospels = Bp&pua) : SCr. bragno ‘meal’, Russ. borosno ‘rye- meal’, Lat. far ‘spelt’, Goth. barizeins ‘made of barley’, etc. Walde-P. 2.134. Berneker 74. Cf. the use of Grk. otros ‘grain’ for ‘food’ (above, 3).
9083:3. Ir. bazrgen, W., Br. bara : OE bere ‘barley’, Lat. far ‘spelt’, etc. Walde-P. 2.134. Walde-H. 1.455. Pedersen 1.101.
9094:Lett. maize : miezis ‘barley’. Mihl.- Endz, 2.553.
9100:Grk. pata ‘barley-cake’, fr, pacow ‘knead’ (5.54).
9144:2. Lat. massa ‘lump, mass, dough’ (> Sp. masa also ‘dough’), fr. Grk. pata ‘barley-cake’ (5.52). Ernout-M. 594. REW 5396.
9187:3. Lat. farina (> Romance words), SCr. brasno (ChSI. brasino ‘food’, 5.12) : Lat. far ‘spelt, grain’, Goth. barizeins ‘made of barley’, OE bere ‘barley’, etc. Walde-P. 2.134. Ernout-M. 330. Walde-H. 1.455.
9790:6. Skt. yavasura-, epd. of yava- ‘grain, millet, barley’ and surd- itself perh. ‘beer’ (KZ 35.314) = Av. hura- ‘milk-wine’ (Barth. 1837), fr. the same root as Skt. soma-, Av. haoma- (5.92), or more directly : OE sar ‘sour’, etc. Walde-P. 2.513.
12350:Words for ‘barn’, as a storehouse for grain or other farm produce, are partly specializations of ‘storehouse’ and partly from words for ‘grain’ (or some particu- lar kind of grain, as ‘barley’ in the case of NE barn). But since the farmer’s barn may also be the place where the farm animals are kept, there is some- times confusion with the notion of ‘stable’. So a few of the words for ‘barn’ probably rest on this latter no- tion (Goth. bansts, Ir. saball). Con- versely in NE barn in U.S. usage the secondary association with the place where the cattle and horses are kept is so strong that in the country it is the common word covering ‘stable’, and it is by this analogy (rather than the no- tion of ‘storehouse’) that one uses car barn of the place where street cars stand when not on their run.
12369:ME berne, bern, NE of bere ‘barley in cpds. ‘place’ :
```


## [2026-09-06T15:22:07.002Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN zea\"; grep -n -i \"^zea\\|zea, n\\| zea \" KLN_1966.txt | head -10; echo \"=== KLN gilet\"; grep -n -i \"gilet\\|jaleco\\|jalikah\\|yelek\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-06T15:22:07.095Z] TOOL RESULT

```
=== KLN zea
=== KLN gilet
KLN_1971.txt:102608:gilet, n., a waistcoat. — F., fr. Sp. jileco, gileco 
KLN_1971.txt:102610:Arab. jaleco t ‘coat* of Christians in Moorish 
KLN_1971.txt:102611:captivity’, ult. fr. Turk, yelek. 
KLN_1966.txt:16144:L.  Aegidius,  fr.  aegis.  See  aegis, gilet,  n.,  a  waistcoat.  —  F.,  fr.  Sp.  jileco,  gileco (the  modern  Sp.  form  is  chaleco),  fr.  Algerian Arab,  jaleco,  ‘coat  of  Christians  in  Moorish captivity’,  ult.  fr.  Turk,  yelek.
```


## [2026-09-06T15:22:14.804Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- gilet page ctx\"; sed -n 16130,16150p KLN_1966.txt; echo \"=== nearest page markers\"; awk 'NR<16160 && /^\\s*6[0-9][0-9]\\s*$/ {print NR\": \"$0}' KLN_1966.txt | tail -5"
}
```


## [2026-09-06T15:22:15.664Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Zea\\|zea,\" KLN_1966.txt | tail -20; echo ===1971; grep -n \"Zea\\|zea,\" KLN_1971.txt | tail -10"
}
```


### [2026-09-06T15:22:17.427Z] TOOL RESULT

```
--- gilet page ctx
gigantean,  adj.,  gigantic.  —  Formed  with  suff. -an  fr.  L.  giganteus,  fr.  gigas,  gen.  gigarttis, ‘giant’.  See  giant.
gigantic,  adj.  — —  Formed  with  suff.  -ic,  fr.  L. gigas,  gen.  gigantis,  ‘giant’.  See  giant. Derivatives:  gigantic-al-ly,  adv.,  gigantic-ness,n. gigantism,  n.,  abnormal  tallness.  See  giant and  -ism  and  cp.  giantism, giganto-,  combining  form  meaning  ‘giant’.  Gk. YtyavTO-,  fr.  gen.  Y^TotVTOl?>  ‘Biant  •  See
giant.
gigantomachy,  gigantomachia,  n.,  the  war  be¬ tween  the  Olympian  gods  and  the  giants  ( Greek mythol.)  —  Gk.  ‘battle  of  the
giants’,  compounded  of  y'-Ys?>  8en-  YiyavTo?, ‘giant’,  and  (jF/y),  ‘battle’.  See  giant  and  -machy. Gigartina.n.,  a  genus  of  red  algae  (hot.) —  ModL., fr.  Gk.  yiy«PT0V>  ‘grapestone’,  prob.  fr.  Aram. gighartd,  ‘kernel,  stone’,  which  is  rel.  to  Aram. garger&,  ‘berry,  grain’.  See  gerah. giggle,  intr.  v.  and  n.  —  Of  imitative  origin, gigliato,  n.,  name  of  a  Neapolitan  silver  coin,  is¬ sued  by  Charles  II  of  Anjou.  —  It.,  fr.  giglio, ‘lily’,  a  word  formed  with  dissimilation  fr.  L. Iilium,  which,  for  its  part,  was  assimilated  fr. Gk.  Xdptov,  ‘lily’.  See  lily, gigolo,  n.,  a  paid  male  dancing  partner.  —  F., fr.  gigoter ,  ‘to  move  the  shanks,  to  hop  ,  fr. gigue,  ‘shank,  fiddle’,  which  is  of  Teut.  origin. See  gigue.  >
gigot,  n.,  leg  of  mutton.  —  F.,  ‘leg  of  mutton  , fr.  OF.  gigue,  whence  also  E.  gigue  (q.v.)  Cp. prec.  word.
gigue,  n.,  i)  a  stringed  instrument;  2)  a  kind of  dance.  —  F.,  reborrowed  fr.  E.  jig,  ‘a  quick dance’  (q.v.),  which  itself  was  borrowed  fr.  OF. giguer,  ‘to  move  the  shanks,  hop,  dance  ,  fr. gigue,  ‘shank;  fiddle’.  Cp.  the  two  prec.  words. Gila  monster,  a  kind  of  venomous  lizard.  —  From Gila,  name  of  a  river  in  Arizona.
Gilbert,  masc.  PN.  —  A  blend  of  OF.  Guillebert (whence  F.  Guilbert )  and  OF.  Gilebert  (whence F.  Gilbert).  Both  OF.  names  are  of  Teut.  origin. OF.  Guillebert  derives  fr.  OHG.  Williberht,  lit. ‘a  bright  will’,  fr.  willio,  willo,  ‘will’,  and  beraht, ‘bright’;  see  will  and  bright.  OF.  Gilebert  comes fr.  Gisilbert,  lit.  ‘a  bright  pledge’,  fr.  OHG.  gisil, pledge',  which  is  a  Celtic  loan  word  (cp.  OIr. giall,  W.  gwystl,  ‘pledge’),  and  fr.  OHG.  beraht, ‘bright’.
gilbert,  n.,  name  of  the  C.G.S.  unit  of  magneto¬ motive  force  ( electr .)  —  Named  after  the  Eng¬ lish  physician  and  physicist  William  Gilbert (1544-1603).
Gilbertian,  adj.,  resembling  the  style  of  the  Eng¬ lish  author  Sir  William  Schwenck  Gilbert  (1836-
1911).  For  the  ending  see  suff.  -ian.
Gilbertine,  n.,  a  member  of  the  religious  order founded  by  St.  Gilbert  in  the  12th  century.  For the  ending  see  suff.  -ine  (representing  L.  -inus). gilbertite,  n.,  a  variety  of  damourite  (mineral)  — Named  after  Davies  Gilbert  (1767-1839).  For the  ending  see  subst.  suff.  -ite. gild,  n.  —  See  guild.
gild,  tr.  v.  —  ME.  gilden,  fr.  OE.  gyldan,  fr.  OE. gold,  ‘gold’.  Cp.  ON.  gylla,  ‘to  gild’,  fr.  ON. gull,  goll,  ‘gold’,  and  see  gold.
Derivatives:  gild-ed,  adj.,  gild-er,  n.,  gild-ing,  n. Giles,  masc.  PN ;  often  used  to  denote  a  simple- minded  farmer.  —  OF.  Gil(l)es  (F.  Gilles),  fr.
L.  Aegidius,  fr.  aegis.  See  aegis, gilet,  n.,  a  waistcoat.  —  F.,  fr.  Sp.  jileco,  gileco (the  modern  Sp.  form  is  chaleco),  fr.  Algerian Arab,  jaleco,  ‘coat  of  Christians  in  Moorish captivity’,  ult.  fr.  Turk,  yelek.
Gilia,  n.,  a  genus  of  plants  (bot.)  —  ModL., named  in  1794  after  the  Spanish  botanist  Felipe Luis  Gil.
gill,  n.,  the  organ  of  respiration  in  fishes.  —  ME. gile,  gille,  from  Scandinavian;  cp.  ON.  giolnar (pi.),  ‘jaws’,  Swed.  gal,  ‘gill,  jaw’,  Dan.  gselle, ‘gill’,  which  are  cogn.  with  Gk.  ■/y.Tkoq,  ‘lip’, XeXi5 vy),  Tip,  jaw’.  Cp.  chilo-.
Derivative:  gill-ed,  adj.
gill,  n.,  a  small  measure.  —  ME.  gille,  gylle,  fr. OF.  gille,  gelle,  fr.  L.  gillo,  gello,  ‘cooling  vessel’, which  is  prob.  of  Sem.  origin.  Cp.  Heb.  gulldh, ‘oilcan’,  Arab.  gullaf,  ‘earthen  pitcher’, gill,  ghyll,  n.,  a  ravine  (Scot,  and  dial.  Engl.)  — ME.  gille,  gylle,  fr.  ON.  gil,  ‘a  narrow  valley, glen’,  which  is  rel.  to  MLG.  gil,  ‘throat’,  OHG. gil,  ‘hernia’,  OE.  gfelan  (for  *gailjan),  ‘to hinder,  impede’.  Cp.  goal.
Gill,  also  JiU,  1)  fern.  PN.;  2)  girl  sweetheart.  — Abbreviation  of  Gillian ,  resp.  Jillian ,  fr.  L. Juliana.  See  next  word  and  cp.  jilt.
Gillian,  fern.  PN.  —  Fr.  F.  Juliane,  fr.  L.  Juliana, fern,  of  Julianus,  lit.  ‘of  Julius’.  See  Julian, Juliana.
=== nearest page markers
15919: 646
15930: 647
15958: 648
16022: 650
16023: 651
```


### [2026-09-06T15:22:17.475Z] TOOL RESULT

```
Exit code 1
3032:Anzac,  n.,  a  member  of  the  Australian  and  New Zealand  Army  corps.  —  Acrostic  formed  from the  initials  of  the  words  Australian  (and)  Aew Zealand  Army  Corps.
4142:awaruite,  n.,  a  natural  alloy  of  iron  and  nickel (mineral.)  —  Named  after  Awarua  Bay  in  New Zealand.  For  the  ending  see  subst.  suff.  -ite.
11473:Dinomis,  n.,  a  genus  of  recently  extinct  birds  re¬ sembling  an  ostrich.  The  New  Zealand  Moa belonged  to  this  genus  (paleontol.) — ModL.,  lit. ‘a  frightful  bird’,  compounded  of  dino-  and Gk.  8pvi?,  ‘bird’.  See  omitho-. dinosaur,  n.  any  member  of  the  Dinosauria.  — See  next  word.
17357:herd,  MHG.  hert,  G.  Herd,  ‘hearth’,  fr.  Teut. base  *her-,  corresponding  to  I.-E.  base  *ker-, ‘to  singe,  bum,  glow’,  whence  also  Goth,  hauri, ‘coal’,  ON.  hyrr,  ‘fire’,  OI.  kudayati,  kulayati, ‘singes’,  OSIav.  kurjq,  kuriti  s^,  ‘to  smoke’, Lith.  kuriii,  kiirti,  Lett,  kuru,  kurt,  ‘to  heat’, Lith.  kdrStas,  ‘hot’,  katstis,  ‘heat’,  Lett,  karsts, ‘hot’,  kafst,  ‘to  grow  hot’,  and  prob.  also  L. carbo,  ‘coal,  charcoal’ ;  see  carbon.  Cp.  cremate, heat,  n.  —  ME.  hete,  Fr.  OE.  hxtu,  hxto,  rel.  to OS.  hittia,  ON.  hiti,  Dan.  hede,  Swed.  hetta, OFris.  hete,  Du.  hitte,  OHG.  hizzea,  hizza, heizi,  MHG.,  G.  hitze,  ‘heat’,  OE.  hxda,  ‘hot weather’,  Goth,  heito,  ‘fever’,  and  to  OE.  hat, etc.,  ‘hot’,  see  hot.  It.  izza,  ‘wrath,  anger’,  is  a Teut.  loan  word.
20525:OS.  kesur,  OFris.  keiser  (Goth,  kaisar  is  bor¬ rowed  fr.  Gk.  Katoap,  which  itself  is  a  loan word  fr.  L.  Caesar).  See  Caesar  and  cp.  czar, kaka,  n.,  any  of  certain  New  Zealand  parrots.  — Maori  kaka,  ‘parrot’,  imitative  of  its  cry. kakapo,  n.,  the  owl  parrot.  —  Maori.  Cp.  prec. word.
20551:Derivative:  katydid,  intr.  v. kauri,  n.,  a  tall  tree  of  New  Zealand  ( Agathis australis).  —  Maori.
20554:Kavi,  Kawi,  n.,  the  ancient  language  of  Java.  — Javanese  kavi,  ‘poetic  (scil.  language)’,  fr.  OI. kavih,  ‘wise,  sage;  seer,  poet’,  which  is  rel.  to kavarifi,  ‘stingy’,  a-kuvate,  ‘intends’,  and  cogn. with  Gk.  xoew  (for  *xoF£u),  ‘I  mark,  perceive, hear’,  fr.  I.-E.  base  *(s)qSu-,  ‘to  look  at,  observe, perceive’,  whence  also  OE.  sceawian,  ‘to  look, see'.  See  show  and  cp.  words  there  referred  to. kayak,  n.,  an  Eskimo  canoe  made  of  sealskin stretched  on  a  wooden  frame.  —  Eskimo, kea,  n.,  a  large  New  Zealand  parrot.  —  Maori, keck,  intr.  v„  to  retch.  —  Imitative.
20738:kiwi,  n.,  a  flightless  bird  of  New  Zealand;  ap¬ teryx.  —  Maori,  of  imitative  origin, klaprothite,  n.,  a  synonym  of  lazulite  (mineral.)  — Named  after  the  German  mineralogist  Martin Heinrich  Klaproth  (1743-1817).  For  the  ending see  subt.  suff.  -ite.
22855:Derivatives:  manufacture,  tr.  v.,  manufactur-er , n.,  manufactur-ing,  verbal  n.  and  adj. manuka,  n.,  the  New  Zealand  tea  tree.  —  Maori, manul,  n.,  a  small  wild  cat  of  Tibet,  Mongolia and  Siberia.  — -  Mongolian  name, manumission,  n.,  liberation.  —  ME.,  fr.  MF. (=  F.),  fr.  L.  manumissidnem,  acc.  of  manumis- sio,  ‘the  freeing  of  a  slave’,  fr.  manumissus,  pp. of  maniimittere.  See  next  word  and  -ion. manumit,  tr.  v.,  to  release.  —  ME.  manumitten, fr.  MF.  manumitter,  fr.  L.  maniimittere,  ‘to  re¬ lease,  set  at  liberty,  emancipate’,  lit.  ‘to  let  out of  one’s  hand’,  fr.  manu,  abl.  of  manus,  ‘hand’.
22869:Maori,  n.,  1)  a  member  of  the  native  of  New  Zea¬ land;  2)  the  language  spoken  by  them.  —  New Zealand  native  word.
24108:moa,  n.,  an  extinct  flightless  bird  of  New  Zealand. —  Native  (=  Maori)  name.
25661:Notodontidae,  n.  pi.,  a  family  of  moths  ( entomol .) —  Formed  with  suff.  -idae  fr.  not-  and  the  stem of  Gk.  68cov,  gen.  686vxo<;,  ‘tooth’.  See  odonto-. Notogaea,  n.,  a  zoogeographical  realm,  com¬ prising  the  Australian,  New  Zealand  and  Neo¬ tropical  regions.  —  Gk.,  compounded  of  v6 to;, ‘the  south  wind,  the  south’,  and  y aicc,  ‘earth’. The  first  element  prop,  means  ‘the  rainy  wind’, and  is  rel.  to  votio;,  voT£p6;,  ‘damp,  moist’, voxtc,  ‘moisture,  damp’,  voxtcc,  ‘moisture, rain’ ;  see  natation  and  cp.  Notus.  For  the  second element  in  Notogaea  see  geo-, notonectid,  adj.,  pertaining  to  the  Notonectidae-, n.,  one  of  the  family  Notonectidae.  —  See  next word.
25670:New  Zealand  ( ornithol .)  —  ModL.,  lit.  ‘bird  of the  south’,  compounded  of  not-  and  Gk.  opvi?, ‘bird’.  See  ornitho-.
30941:Derivatives:  puissant-ly,  adv.,  puissant-ness,  n. puja,  n.,  honorable  reception.  —  OI.  pujd,  ‘honor, esteem,  worship’,  prob.  of  Dravidian  origin, puka,  n.,  a  New  Zealand  tree, pukatea,  n.,  a  New  Zealand  forest  tree.  —  Maori, pukateine,  also  pukatein,  n.,  an  alkaloid  found  in the  bark  of  the  pukatea  ( chem .)  —  Formed  fr. pukatea  with  chem.  suff.  -ine,  resp.  -in. puke,  intr.  v.,  to  vomit.  —  Prob.  for  *spuke,  and rel.  to  G.  spucken,  ‘to  spit’,  which  is  a  freq.  of speien.  See  spew.
31722:rotta,  and  to  It.  ratto,  Sp.,  Port,  rata,  F.  rat, Gael,  radan.  The  etymology  of  these  words  is unknown.  There  is  no  connection  between them  and  L.  rodere,  ‘to  gnaw’.  Cp.  ratteen. Derivatives:  rat,  tr.  v.,  ratt-ish,  adj.,  ratt-y,  adj. rata,  n.,  a  New  Zealand  tree.  — -  Maori, ratable,  adj.  —  Formed  fr.  rate,  ‘to  estimate’, with  suff.  -able.
33928:Scandinavia,  n.  —  L.  Sca(n)dinavia,  name  of  an island  in  Northern  Europe  (prob.  Zealand  or Schonen),  in  ML.  ‘Scandinavia’,  from  a  Teut. form  of  ON.  Skaney,  name  of  a  district  in Southern  Sweden,  a  compound  word  whose second  element  is  identical  with  ON.  ey,  ‘island’. Cp.  OE.  eg,  ig,  ieg,  ‘island',  the  ending  -ey  in Jersey  and  in  other  names  of  islands,  OHG. auwia,  ouwa,  ‘island,  damp  meadow",  and  the first  element  in  G.  Ei-land,  ‘island',  and  see  is¬ land.  Cp.  Scandian,  scandium.
34039:Derivative:  schizophren-ic,  adj. scbnapper,  n.,  a  sea  fish  of  Australia  and  New Zealand.  —  Alteration  of  snapper  after  G. Schtiapper.
38189:Derivatives :  tar,  tr.  v.,  tarr-ed,  tarr-y,  adjs. tar,  n.,  sailor  ( colloq .)  — Abbreviation  of  tarpaulin, tara,  also  tara  fern,  n.,  a  kind  of  New  Zealand brake  with  edible  rootstock.  —  Maori  tara, 'spear'.
40375:Tsuga,  n.,  a  genus  of  plants,  the  hemlock  (bot.) —  ModL.,  fr.  Jap.  tsuga,  ‘larch’. Tsung-li-yamen,  n.,  Chinese  foreign  office.  — Chin.,  lit.  ‘general  management  office’,  fr.  tsung, ‘general’,  li,  ‘managing’,  and  yamen,  ‘office’,  lit. ‘gate  with  flags’.  See  yamen. tuatara,  n.,  a  New  Zealand  lizard.  —  Maori,  com¬ pounded  of  tua,  ‘on  the  back’,  and  tara,  ‘spine’, tub,  n.,  an  open  wooden  vessel.  —  ME.  tobbe, tubbe,  fr.  MFlem.  tobbe,  tubbe,  which  is  rel.  to OHG.  zubar,  zuibar,  ‘vessel  with  two  handles, wine  vessel',  MHG.,  G.  zuber,  ‘tub’;  prob.  not fr.  L.  tubus,  tube’,  but  rel.  to  E.  two,  hence  lit. meaning  ‘anything  that  has  two  handles’. Derivatives:  tub,  intr.  v.,  tubb-er,  n.,  tubb-ing, verbal  n.,  tubb-ish,  adj.,  tubb-y,  adj. tuba,  n.,  a  musical  instrument.  —  L.,  ‘trumpet’, of  uncertain  origin.
(eval):1: ==1971 not found
```


## [2026-09-06T15:22:24.644Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>16023 && NR<16400 && /^\\s*6[0-9][0-9]\\s*$/ {print NR\": \"$0}' KLN_1966.txt | head; echo \"=== tail KLN 1966\"; tail -c 3000 KLN_1966.txt; echo; echo \"=== 1971 zea\"; grep -n -i \"zea\\b\" KLN_1971.txt | tail -8"
}
```


### [2026-09-06T15:22:26.474Z] TOOL RESULT

```
16183: 658
16192: 659
16233: 660
16248: 661
16327: 664
16343: 665
16369: 666
16381: 667
=== tail KLN 1966
��  Lit.  ‘neigh¬ borhood’,  fr.  ML.  vicinetum,  fr.  L.  vicinus, ‘neighboring,  near’,  fr.  views,  ‘district’;  see vicinage.  Venue  in  this  sense  was  influenced  in form  by  venue,  ‘arrival’.
venule,  n.,  a  small  vein.  —  L.  venttla,  formed  fr.
vena  with  dimin.  suff.  -i da.  See  vein  and  -ule. Venus,  n.  —  L.  Venus,  gen.  Veneris,  ‘the  goddess of  love’.,  fr.  venus,  ‘love,  sexual  desire,  loveliness, attractiveness,  beauty,  charm’,  whence  venerari, ‘to  reverence,  worship,  venerate’.  See  venerate, vera,  n.,  name  of  a  tree,  Bu/nesia  arborea.  —  Am. Sp.,  fr.  Sp.  vera,  ‘border’,  which  derives  fr.  L. ora,  ‘border’  (through  the  intermediate  form *uera\  cp.  Sp.  hueso,  ‘bone’  (fr.  L.  ossum).  L. ora  (for  *osa)  is  a  collective  noun  formed  fr.  os, gen.  -oris,  ‘mouth,  opening,  entrance’.  See  oral, veracious,  adj.,  truthful,  true.  —  Formed  with suff.  -ous  fr.  L.  verax,  gen.  veracis,  ‘truthful, speaking  truly",  fr.  verus.  See  very.
Derivatives:  veracious-ly,  adj.,  veracious-ness,  n. veracity,  n.,  truthfulness,  truth.  —  F.  veracite,  fr. ML.  veracitdtem,  acc.  of  veracitas,  ‘truthfulness’, fr.  L.  verax,  gen.  -acis.  See  prec.  word  and  -ity. veranda,  verandah,  n.  —  Port,  varanda,  ‘balcony’, introduced  into  English  from  India.  Port,  ra- randa  itself  is  of  uncertain  origin.  F.  veranda was  borrowed  from  English.
Derivative:  veranda(h)-ed,  adj. verano,  n.,  the  dry  season  in  tropical  America.  — Sp.,  fr.  L.  ver,  ‘spring’.  See  vernal.
Verbesina
verascope,  n.,  a  small  stereoscopic  camera.  —  A hybrid  coined  fr.  L.  verus,  ���true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) .
veratral,  n.,  the  radical  C9H10O4  (chem.)  —  Form¬ ed  with  adj.  suff.  -al  fr.  L.  verdtrum,  'hellebore’. See  veratrine.
veratric,  adj.,  pertaining  to  a  white  crystalline acid. —  Formed  with  adj.  suff.  -ic  fr.  L.  verdtrum, ‘hellebore’  (see  veratrine) ;  so  called  because  it  is easily  obtained  by  the  decomposition  of  vera¬ trine.  \
veratridine,  also  veratridin,  n.,  an  amorphous  al¬ kaloid  obtained  from  sabadilla  seeds, C36H61OnN  (chem.)  —  Coined  fr.  L.  verdtrum, ‘hellebore’  (see  next  word),  and  the  chem. suffixes  -ide  and  -ine  (resp.  -in), veratrine,  n.,  also  veratrin,  veratrina,  veratria,  a poisonous  mixture  of  alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because
=== 1971 zea
95835:fruma, ‘advantage, profit’, MHG. vrum, ‘zea- 
110914:OFris. hete, Du. hitte, OHG. hizzea , hizza, 
144805:Maori, n., 1) a member of the native of New Zea- 
270323:Zea, n., a genus of grasses (bot.) — ModL., 
270325:naeus (1707-78) fr. L. zea, ‘a kind of grain’, fr. 
270386:chem.) — Formed fr. L. zea (see prec. word) with
```


## [2026-09-06T15:22:33.360Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 270318,270330p KLN_1971.txt; echo \"=== jaleco ctx 1971\"; sed -n 102600,102615p KLN_1971.txt"
}
```


### [2026-09-06T15:22:33.451Z] TOOL RESULT

```
is perh. rel. to Heb. *azen (in dzenekhd, Deut. 
23 : 14), ‘weapon’; so called in allusion to the 
ancient Hebrew form of this letter. Cp. zed, 
zeta. 

Zea, n., a genus of grasses (bot.) — ModL., 
adopted by the Swedish botanist Carolus Lin- 
naeus (1707-78) fr. L. zea, ‘a kind of grain’, fr. 
Gk. Zfiicti (later also in the sing, teia , Cei), 
‘one-seeded wheat’, which is cogn. with OI. 
yavah , Avestic yarn-, ‘corn, grain’, Lith. javaT 
(pi ), of s.m., Ir. eorna , ‘barley’, 
zeal, n. — ME. zele, fr. Late L. zelus [whence also 
=== jaleco ctx 1971
gild, tr. v. — ME. gilden , fr. OE. gyldan, fr. OE. 
gold, ‘gold’. Cp. ON. gylla, ‘to gild’, fr. ON. 
gull, goll t ‘gold’, and see gold. 

Derivatives: gi/d-ed, adj., gild-er, n., gild-ing, n. 
Giles, masc. PN; often used to denote a simple- 
minded farmer. - OF. Gil(l)es (F. Gilles ), fr. 
L. Aegidiusy fr. aegis. See aegis, 
gilet, n., a waistcoat. — F., fr. Sp. jileco, gileco 
(the modern Sp. form is chaleco) $ fr. Algerian 
Arab. jaleco t ‘coat* of Christians in Moorish 
captivity’, ult. fr. Turk, yelek. 

Cilia, n., a genus of plants (bot.) — ModL., 
named in 1794 after the Spanish botanist Felipe 
Luis Gil.
```


## [2026-09-06T15:22:33.768Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD yw barley\"; grep -n \"barley\" SOD.txt | head -20"
}
```


### [2026-09-06T15:22:33.826Z] TOOL RESULT

```
=== SOD yw barley
```


## [2026-09-06T15:22:40.734Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l SOD.txt SOD_pages.txt; head -40 SOD.txt; echo \"=== grep jaw/yw\"; grep -n \"^\\s*[0-9]\\{3,5\\}\\s*y[wʾ]\" SOD.txt | head -20"
}
```


### [2026-09-06T15:22:42.732Z] TOOL RESULT

```
 111423 SOD.txt
  45615 SOD_pages.txt
 157038 total
SOGDIAN 
DICTIONARY 

Sogdian  -  Persian  -  English 


B.Gharib 


FARHANGAN  PUBLICATIONS 


Sogdian  Dictionary  (Sogdian-Persian-English) 

by  B.  Gharib 

editorial  supervisor:  A.  Mansouri 

editor:  S.  Fotouhi 

©  1995,  Farhangan  Publications 

2/52.  Shahid-e  Said  Street,  Tehran  15916,  Iran. 

Tel:  6460069.    Fax:  670230 


ISBN:  964-5558-06-9 


4f*Jj*l{^  0"J-^8  'Jy^**-  ^J>*4^  tfW  :  j'  a>„J^  <f  jljX-U^  -LUi^-L  ^JjJ'j^  L»  e jlf  ijj- 
;l_^0  jL-u  jlS'  4$"  (.5*^-*^'  "^^  (H^-  fJ 


L?JJ  J' 


•  l^>  o-^  jl  ^^<o  (j  ^jb^b  j  uij^-  ^C*" 


=== grep jaw/yw
9872:363  ywz-'   B  o^/^pT 
9879:364  ywz-1   B 
9888:365  ywz-'  =*  ywz-1 
9890:366  ywz-2  =*>  ywz-2 
9892:367  ywzkr'k    B  J-'^*(^/vj 
35962:4290  yw1   B,  S  J<jl 
35969:4291  yw2   C  3€ 
35990:4293  yw"  =*  yw'w-,  yw- 
35999:4295  ywMkkr   B  (J'&^'d^j^ 
36006:4296  yw»n    B,  M  j^^f 
36013:4297  ywwnk    MD  ->  ywn>nk 
36015:4298  yw»t   B,  S  ^olj* 
36024:4299  ywwt-  =»  yw'w- 
36033:4301  yw'kr   S  =>  yw*kkr 
36035:4302  yw'kry   S  =»  yw'kkr 
36037:4303  yw'm   C  «&  JStf 
36043:4304  ywWk   S  v*>  <  jl*** 
36050:4305  yw'm  n'fc   C  (^/fv)^  v.><4;^ 
36070:4307  yw'ncy    B  J^^jy^S^ 
36077:4308  yw'ncyq    C  =^  yw'ncyk^
```


## [2026-09-06T15:22:47.671Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 35955,36000p SOD.txt; echo \"=== entry 448\"; grep -n \"^448 \\|^ 448 \" SOD.txt | head"
}
```


### [2026-09-06T15:22:47.773Z] TOOL RESULT

```
particle   =»xtw2 
so  ever,  however,  whoever,  the  very 
EGSii  119;  VJ;  TSP;  SCE;  BSTBL,  Dhy.  370,  393; 
GMS  1545,  1552;  Ywtw,  TSP  1512;  <  xwty 
"self"  KG  Apd.  198.5.2;  S  W,  SGI,  1986,  407 

4290  yw1   B,  S  J<jl 
xo   ©<hau   ©pron.  art.  nom.  sg.  m.  ^yw,  y-3, 

yh,  ywn'y,  xw,  ZK,  xww 
he,  that,  the 
GMS  1398,  1405-22;  S  W,  TPS  1994,  47-8 

4291  yw2   C  3€ 
ya/ow   =»y»w 

bull,  ox 

BSTii  887.8;  C2,  91R8,  105R3 

4292  y w-  o^  jtjj>>  *fX>  >*-^  *j£t>  f j^ 

yu/o,  yaw   (y>w-:)  ©<*£av;  Av.  gunaoitU 

Yaghn.  ^aw;  Khot.  hagav—,  Khwar.  T'yv-;  Oss. 

Yaun   =»ywtch,  yw>n,  ywtk 
0o)bc  necessary,  (ro)bc  wanting 
BBB  552;  GMS  576;  Bailey.  Asica.  14;  Mack. 

BSTBL  n  p56,  Dhy.  141,  Ywywty,  Dhu.  113,  124, 

Y'wty,  129;  Ywt  "it  must  be" 

4293  yw"  =*  yw'w-,  yw- 

4294  yW'p-    B  ^Uf  jUj  ^/T  <  j^O; 
xwaf   ©Yaghn.  xw/;  Parth.  wf- 

(to)spit 

SCE  323;  Gersh.  IF  1970,  305 

4295  ywMkkr   B  (J'&^'d^j^ 
xwakar   (yw'kr)   ©<*wahdkara   =*wh}kr,  xw}qr 
=== entry 448
10418:448  »zytk  =*  Vytk 
82631:448
```


## [2026-09-06T15:22:54.537Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 82600,82680p SOD.txt"
}
```


### [2026-09-06T15:22:54.587Z] TOOL RESULT

```
11000  yp'kpr'k   B  Cjt^s 
yipak-Pare  (yp'kPryCy))  ^yp'qbry* 

angry 

VJ  629;  Hen.  BSOAS  11,  65.4;  GMS  1132;  C2, 
22V2:  BSTii  857.2 

11001  yp'qbry*  C  JJ91 
y(i)pak-parya   =»yp}k,  yp}kpr>k 

anger 
BSTi  285 


11002  yp'kbrystr  C 

y(i)pak-Parestar 

angrier 

C2,  23R7:  BSTii  857.7 


J{jS^L^ 


yp}kpry(y) 


448 


t*S  'M 


(j*).U 


11003  yp»kpry(y)   M  =»  yp'kpr'k 

11004  yr>8y   C  =  y-  +r}9y  «»  r>8 

11005  yryt   B 

®<yYrt 
wide 
TSP  2.143  n  pl70 

11006  YRH>  S 
max   ©Idg.  ^m'x2,  ntfyCh)3 
month 

Anc.  Lett.  3.26 

1 1007  ys'm'nty   C  -»  'ys'mndy 

11008  ysmwtry*   C  =  y-  +smwtryJ  =»  smwtr 

11009  ysr'yl   C  JJf^ 
israil  (ysryl) 

Israil 

C2,  60R1,  94V24;  STii  1.32;  STi  32;  Sund.  AoFi 
241,  7 

11010  ysr'ylyq   C  JLfl^l 
israilik  ©pi.  -f;  ob.  pi.  -ty 

Israelite 
STi  8.9,  32.18 

11011  ysryl  -»  ysr}yl 

11012  yst*  «*  yst> 

11013  yst*  C 

(yst\  >ystO  ©2pl.  pres.  ind.  <^x-:
```


## [2026-09-06T15:23:09.996Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"barley\\|bariey\\|barlcy\" SOD_pages.txt | head -20; echo \"=== yava in SOD\"; grep -n \"yava\\|jav\\b\" SOD.txt | head -20"
}
```


### [2026-09-06T15:23:10.066Z] TOOL RESULT

```
=== yava in SOD
29837:ciwand   (cywnd,  cywnt)  ©<*haca-yavant  ? 
64509:rdjyavardhana  =*r>zprt 
69906:saw/u   ©Av.  syava;  Yaghn.  sow-,  Oss.  sdu  ©ob. 
70989:saw,  so  ©OP  syava—,  <*cyav  ©3sg,  pres.  swt 
82783:yaw   ©<Av.  yava
```


## [2026-09-06T15:23:14.107Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 82770,82800p SOD.txt; echo \"=== find page marker before\"; awk 'NR<82790 && /^\\s*4[0-9][0-9]\\s*$/ {n=NR; p=$0} END{}' SOD.txt; awk 'NR<82790 && NR>82000 && /^[0-9]{3}$/ {print NR\": \"$0}' SOD.txt | tail -3"
}
```


### [2026-09-06T15:23:16.455Z] TOOL RESULT

```
11029  yw2   C  (Oy>^J^jj)Ji 
yu,  ew  ©<aiva  =»*yw,  yw  pnc}s\  yw  wyst, 

ywnts,  ywp*t,  ywsmbd 

one 

GMS  1316,  1336  n  1;  STi  5.10  pl06;  Sund. 
AoFviii  1981  p220;  STii  4.39,  5.36  p60l;  C2 
gloss.;  ob.  ywy,  STi  45.8;  GMS  1319 

11030  yw-   M,  S  yr 

yaw   ©<Av.  yava 
barely 


449 


ywhnn 


GMS  519;  yw\  MDii  p215;  MDiii  p34.1;  loc. 
ywy\GUS  1183 

11031  yw»r    B  =»  yw>r 

11032  yw}nk   B  x^  J^a  < J-^a* 
iwang,  y(o)wang   ©<*wi-wanka->  Oss,  iwong 

=== find page marker before
```


## [2026-09-06T15:23:23.765Z] TOOL CALL #34: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T15:23:25.874Z] TOOL RESULT

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
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
```


## [2026-09-06T15:23:30.207Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 53 54 55; do echo \"===== leaf $L (printed ~$((L+540)))\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -60; done"
}
```


### [2026-09-06T15:23:32.113Z] TOOL RESULT

```
===== leaf 53 (printed ~593)
  ‫جوج‬                                                                                                     ‫ویس‬
                                                                                                            ‫‪--‬‬


                                           ‫‪۰‬‬   ‫هم هست‬
                                                            ‫جوا = باشومل‌بروزن زغال‪ ,‬معروف‬
‫» بکر اول بر وزن لپالی ؛‬              ‫جوالی‬                ‫اتفمته که چیز ها‬
                                                                          ‫ظآرنفی باشد ابزپ‬
                                                                                         ‫ات و‬

‫بانخواه_ و زنان )‪(٩‬‏ هم گویند ‪ -‬و بفتح اول‬                 ‫و پمعنی مکر و حیله همآمده است ‪ -‬و کنابه‬
           ‫‪.‬‬   ‫معروف است که لقض پیری باشد ‪۴‬‬                ‫ازیدن اسان هم هست ‪ -‬و کنابه ازچیزی گشاده‬
                                                                                                           ‫باشد ‪.‬‬
‫جو بال » بابایابجد بورژن رومال»‬
‫بلغت زند ویازند (‪ )۱‬جوال رگاونند وآنظرفی‬                    ‫جوالق ‪ .‬بورزن موافق » جنی بود‬
                 ‫باشد که از موی و یشم بافند © ‪.‬‬             ‫قلندران »‪ .‬و ابن جمع جولق است‬                 ‫از بوخش‬
‫جو بجو ‪ -‬بفتح اول و جيم ابجد ‪,‬‬                             ‫و جولق معرب جولخ » و جولخ بافته پشمی‌باشد‬
                ‫معتی بازه بازه ودره دره باشد ‪۰ ۹‬‬            ‫که ازآن خرجین مازند و مردم فقیر وقلندران‬
‫جو به ‪ -‬بم اول و انی مجهول وفتح‬                                                          ‫نیز پوشند ‪. ۴‬‬
‫بایابجد » جابی و مقامی را گویند درشهرکه‬                     ‫جوام ‏‪ ٣‬بم اول بروزن مدام‪ .‬بلفت‬
                                                            ‫زند و پازند (‪ )۱‬بمعنی روز است که بعربی يوم‬
      ‫از جهت فروختن آورند آلجا فروخته شود ‪.‬‬                                                             ‫گونند ‪۶ .‬‬

 ‫نوره = بفتح اول وتا ورای فرشت»‬
                              ‫ج‬
                                   ‫یمعئی مناره باشد ‪.‬‬


‫جوج = منم اول بورزن عوج » پارچة‬                                  ‫ی‬
                                                                 ‫خو‬‫سکرم‬
                                                                      ‫جآون‌هر ‪ ۵‬ک=نابه از‬
 ‫شت سرخی باشد که بر سر خروس است =‬                           ‫ونام بیرقصایان‬      ‫همت باشد ‪-‬‬      ‫و صاحب‬    ‫ششنده‬       ‫و‬



                            ‫(‪ )۲‬چش ‪ .‬زبنان (رك‪ :‬زیان ) ‪.‬‬                       ‫(‪ )۱‬چك‪ :‬ژند وپاژند ‪.‬‬

       ‫‪« lahg‬واژه‌نامه ‪۹‬‬           ‫‪ug‬‏ ‪lag .‬‬      ‫مازندرانی کنونی ‪12۷62‬‬           ‫طبری ‪1222‬‬          ‫‪۱‬‬

                                ‫جوهال (ھ ‪.e‬‏ ‪ ).‬وجهال وکاله(« م‪ ).‬گفته‌اند ‪ .‬رك‪ :‬جوبال ‪.‬‬            ‫ندیرزفارسی‬
  ‫‪۰‬‬   ‫‪۴‬‬   ‫«یونکر‪۹۷‬‬   ‫‪ ۰:‬روز ‪.‬‬     ‫‪9‬‬   ‫‪ ۹‬نظایر آن » بهلوی‬        ‫هر ‪ ۰‬ایا‬   ‫‪-‬‬         ‫‪.‬‬   ‫جولخ‬   ‫جولق‪.‬‬    ‫ركه‬      ‫‪۲‬‬


      ‫‪10۵۷۷ ۰ ۰‬‬         ‫‪۰‬‬        ‫د منای ‪۷۷‬‬      ‫‪۹۱۱‬‬         ‫) > بهلوی‬          ‫(دری‬
                                                                                  ‫مص‬‫‪ _ ۴‬از ‪ :‬حوان ‪ +‬ی‬
      ‫هنوز از باغ زندگانی برنخوردست‬             ‫‪.‬فت ‪ :‬ا(بندپزرد)‬
                                                               ‫‪ « :‬یکی از وزرا ‪ . .‬ک‬               ‫« اونوالا ‪۸‬‬
  ‫‪ ,‬جوال‪.‬‬       ‫© _ ‪ . [1206‬بپلوی ‪2:‬‬                        ‫‪.‬‬     ‫واز ربمان‌جوانی تمتم نافته‪« ›.‬ګلان))›‬
                                                                  ‫‪ - ۱‬رك ‪ :‬جوجو ‪.‬‬                ‫«بونکر ‪۸۷٩‬‏ ‪.‬‬
  ‫‪ #‬جوان ‪ -‬بفتح اول » اوستا ‪( 03۷(2)72-‬شاب » جوان) «بارتولمه ‪ ۵۰۳۱‬پهلوی‬
  ‫‪( 1802۷0 ,‬بجۂ چهاریا ) ‪,‬هندی باستان ‪-‬‬      ‫”لیر ‪ ۰۵۲۲‬ارمنی ع ‪۷‬‬                                               ‫‪12‬‬
  ‫‪.‬ردی ع ‪ . [72۷1‬افغانی وبلوچی ع ‪ ۰ [03۷3‬مازسرانی‪« [02۷3‬اسنق‪» ۹۲4‬‬
                                                                ‫‏‪ 0V2‬ک‬
      ‫کېلکی ‪ [04۷3‬فربز ندیو بر ئى ‪ [011۷5‬ن›طنز ی‪ 24.۱ [18۷3‬ص‪:٩۳۹۲‬‏ سمنالی ‪15۷5‬ل ‪.‬سنگری‬
      ‫و سرخه‌بی ‪ . [72۷0‬لاسکردی ‪ 70۷62‬؛ شهمیرزادی‪« [011۷2‬ك‪ .‬ص‪»4۹۱‬؛هرچیز‬                                        ‫‪0‬‬
                 ‫‪:‬یر ‪:‬‬
                     ‫‪.‬اب ‪ .‬ضد ه‬  ‫که از عمراو چندان نگذشته باشد خواه حبوان باشد خواه بات ش‬
               ‫«یبرچون پیل مت اندرآعد (یکشتی)‪ . . .‬استاد داست که جوان‌بقوت ازو برتوست ‪٩.‬‏‬
          ‫«کلتان ‪. ۰0۰‬‬

===== leaf 54 (printed ~594)
‫سم"‏‪ ٩,‬چ سس‬                                                                             ‫جو جادو‬
‫يك‌فرسخ وئلث فرسخی‌باشد که چپار گروه‌است‪.‬‬             ‫و علامتی را یز گونند که برسرطاقها وابوانها‬
                                                     ‫صب کنند تا خوشنما شود ‪ ,‬و بفتح اول هم‬
‫جو جو ه بفتح هر دو جيم و سکون‬
                                                                                           ‫گفته‌اند ‪.‬‬

‫اجا مك خوب وفوراعلی وجامهای ابریشمی‬                   ‫جحوبجاهدو‌ا=یت تیه بجولیکن‬
‫رزه‬   ‫و کنانه از باره باره و ررە‬      ‫مشود‬   ‫فس‬       ‫باربکتر و دراز ترمیباشد و طعم آن تلخ است »‬
                           ‫؟ ‪.‬‬    ‫ودره دره هم هت‬      ‫و طبیمت آن گرم و خشك است در اول وسیم‪.‬‬
‫هعنی حوزه‬     ‫و‬   ‫بر ورن‬    ‫‪-‬‬    ‫جوجه ‪°‬‬               ‫جو جر (‪ » )۱‬بم اول و ثالیمجهول‬
                                        ‫است که‬        ‫وکسرجیم و سکون رای قرشت ‪ ۰‬درم راگوبند‪.‬‬

                                                      ‫(‪ )۲‬است و «عربی درهم‬     ‫که چهل و هشت حه‬

                                                     ‫خوانند ‪ .‬و باین معنی بجای حرف آخرلون هم‬
                                                                                     ‫آمده ات ‪. ۱‬‬

                                                      ‫جو چم « نم اول و انی حجهول وفتح‬
                                                     ‫شاخی را کوبند ازدرخت که‬      ‫جیم وسکون هبم ؛‬


                                                                             ‫کل و میوه باراورد ‪.‬‬
   ‫مکایان وجوجه های وی‬           ‫ثالی وخای‬             ‫الث‬     ‫ر‬
                                                               ‫کو‬‫جوجن ‪ = ۴‬نم اول‬
‫نقطه دار » گرو» وفوح مردم وحیوانات راگویند‬             ‫و سکون نون » بلغت زند پوازند (‪ )۳‬بمعنی‬
 ‫و معرب‌آن جوقاست» وبعربی فوح خوانند ‪.‬‬                 ‫درم باشد که چهل و هشت حبه (‪ )۷‬است ‪-‬‬
‫جو دان ‪ -‬بفتح اول و دال ابجد بالف‬                     ‫و باتانی مجهول و قتح ثالث بلفت هندی ‪۴‬‬
      ‫(‪ )۳‬چك ‪ :‬ژد وپاژند ‪.‬‬              ‫(‪ )۲‬چك ‪ 4۸ :‬حبه ‪.‬‬           ‫‪.‬‬   ‫‪ :‬جوجره‬   ‫(‪ )۱‬چك‬


  ‫‪ - ۱‬صحیح «جوجن»است واین اختلاف‌ازقرائت کلم بهلوی برخاسته است‪ .‬رك‪ :‬جوجن‪.‬‬
       ‫‪ ۴‬هز » (‪0 . [02)[0‬ا[‪ , [0‬پهلوی‪ 712۲‬درهم ‪,‬درم‪< .‬یولکر ‪. ۴ ۸۷‬‬
 ‫‪ - ۴‬مانسکرت ‪ 30۸[0۷‬د فهرست تحقیق ماللهند طب‌زاخائو* ‪ , ۶۳۰‬هندی ‪: [8210‬‬
 ‫«فليعلم ان لهم ل(لپنود ) فی‌المافات مقداراً يمى جوژن و بشتمل على ثماية امیال فهو آذن‬
 ‫اثئنلانثوون‌الف ذراع » ‪ .‬رك ‪ :‬التفهیم س*‪۹۱‬متن وحاشيه ورك‪ :‬تحقیق ماللپند ص‪ ۴۷‬و ‪٩۸‬‏ ‪.‬‬
        ‫بيك جو برتو ای من‌جوجو انزو‪.‬‬               ‫کشم هرلحظه جوری لوئو ازتو‬      ‫‪ - ۴‬رك جویجو ‪:‬‬
       ‫لظامی« کنجینه ‪. ۲4۰‬‬
  ‫‪-‬یزیمعنی اندك اندك ‪ « :‬لابق قدر بزرکوار بادشه نباشد دست همت بمال چو مکندا‬
                           ‫«کگلتان ‪. ۷۰۱-۸۰۱‬‬         ‫آلوده کردن که حوحو مگدابی فراهم آورده‌ام ‪.‬‬
 ‫‪ _ 6‬کرماشاهی ز‪۵‬ز و ‪ » [860‬در کرمانجی مکری ‪۵‬ز و ‪1‬زاز دربوکان‬
 ‫(بین سقز و ساوجبلاغ) ها » در کرمانجی‌سنندج ‪10‬ز وھ‪1‬ه ز‪0‬ز ‪ ,‬در کرمانجی کردستان‬
 ‫رکه و عراق ‪ 6۳20‬و اهادنهنانه و ‪k‬عزثز‏ و ‪ , ۷2606‬درلری ا[ ‪ ,‬در لہج لکسی‬
                                     ‫» ورك ‪ :‬جوزه » ج وگك‬      ‫‏‪ » jijek‬پردد گان درکردی ‪۷-۸۵‬‬
  ‫“ وفوج و گروه «ردم د عاث‬          ‫‪ - ۷‬قرکی «چوخ» و «چوق» نمعئی سار « جغفتابی ‪YA‬‏‬

        ‫اللفات» وامروز درنظام جوقه و جوخه بمعنی دسته‌ای مرکب ازهشت تن صرباز رگاوند ‪.‬‬
          ‫‪» ۲ :۷5۱‬؛ خاریشت ‪ .‬ارمجی ‪.‬‬ ‫اد«یا‬  ‫ا‪2‬و‪62‬‬
                                                ‫ت‪00‬‬‫*وجه یفی ‪ -‬بهلوی ‪2‬‬    ‫ج‬

===== leaf 55 (printed ~595)
  ‫وره‬                                                                                                      ‫‪۷‬و‬

‫بممنی اول جودر است که غلةٌ خود روی ميان‬              ‫کشده بونون زدنهو»عی از کافور بود بغایت‬
‫زراعت باشد ‪٩‬‏ ‪ -‬ولام مبارزی هم بوده از لشکر‬          ‫خوشبوی بخرلاف کافور میت » وارآا خورند ‪-‬‬
                                          ‫روص ‪.‬‬      ‫عی ازچوب‬    ‫لدو‪-‬‬‫ووبن‬
                                                                        ‫وچینه دان مرغالرا بیز گ‬
                                                    ‫‪-‬ساهیی را‬
                                                            ‫‪ ۱‬و‬           ‫ويف باشد ‪ :‬که دستةٌ ببل كناد‬
  ‫جوڈر = باذال نقطه دار پروزن‌جوهر‬
‫بمعنی باره باره و ریزه ریزه و ذره ذره باشد ‪.۷‬‬       ‫دان اسب‬
                                                          ‫نان‬
                                                            ‫د مي‬
                                                               ‫يدانه جو در‬                        ‫شه‬         ‫کون‬
                                                    ‫آنها را از‬      ‫ی‬‫رو‬
                                                                      ‫بلی‬
                                                                        ‫آن که جوا‬                     ‫مرثوال‬
                                                                                                           ‫اخ‬‫و‬
   ‫کنیوون‬
        ‫سح ا‬
           ‫جور » بض اول و فت‬
                                                   ‫آن شناسنه و چون آن برطرف شود حکم بر‬
‫عتن"ی ببالااشدھ که تقیض پابین‬
                            ‫مرش‬
                              ‫بی ق‬
                                 ‫را‬
                                                    ‫سال اسب و خر توان کرد ‪ -‬و جنی از انارهم‬
‫و پىت است ‪ -‬و بفتح اول و سکون ثالی والك‬                   ‫هت که دانةٌ آن خشك و بی‌آب می‌باشد ‪۴‬‬
‫در عربی بمعنی ستم باشد ‪ -‬ونام یکی از خطوط‬
‫جام جم لیز هت که خط لب جام و ‪.‬پیاله باشد‬            ‫جو دا نه = بر وزن پروأنه » بمعنی‬
‫وياله جور بمعنی پیالة مالامال است چه هر گاه‬         ‫جودان امت که نوعی ازکافور ‪ -‬وجنسی از انار‪-‬‬
  ‫هت‬
   ‫حرف را دانته پیالة مالامال بدهند تا‬              ‫اوهی ميان دندان ستور‬
                                                                       ‫ی‪-‬‬‫و چینه دان مسرغ‬
 ‫شود و بیفتد و بی‌شمور گردد باو جور وستم کرده‬                                                             ‫باشد ‪. ۳‬‬
                               ‫خواهند بود ‪۶3 .‬‬       ‫ه بر وزن کوثر ‪ .‬گاهی است‬                     ‫جودد‬

‫جور پور )‪(۱‬‏ نم اول بوای ابجد‬                           ‫وو‬
                                                         ‫انعت کندم ح‬
                                                                   ‫ريا‬
                                                                     ‫دزرم‬                         ‫تر‬
                                                                                                   ‫شکه‬
                                                                                                     ‫خبودیرو‬
 ‫صحرایی شبیه‬      ‫بر وزن روز کور » پرنده ابت‬        ‫میروید ودانهةٌ آن کوچك و بلربك مباشد وآ را‬
           ‫بخرو ی که او را تذرو نگیوزیند ‪٩‬‏ ‪-‬‬       ‫بعربی طمج میگوبند ‪ - ۴‬وکاو را نیز گویند‬
                                                                                  ‫‪. ۵‬‬        ‫ند‬
                                                                                              ‫نقر‬
                                                                                                ‫ان م‬
                                                                                                   ‫وربا‬
                                                                                                      ‫خع‬‫که‬
‫جوده = بر وزن نوره ؛ همرنگه رهم‬
  ‫‪-‬مقابل کرد ‪ -‬وجفت چیزبرا گونند ‪.‬‬
                                 ‫وزن و‬                  ‫بارای بیلقطه مروزن‌حوصله‪.‬‬            ‫جو در ‪۵‬د‬



                                                                     ‫)‪ (۱‬چك‪ :‬جوربور )‪(1‬‬

  ‫رك‪:‬‬  ‫‪- ۳‬‬  ‫در در ةكرح جودانك کویند ‪ 71125 8000615082‬دنابتی‪.*۹۷۱‬‬                                      ‫‪۱‬‬
   ‫‪ = ۴‬جوزر « دزی ‪۱:۸۷۱٩‬‏ د لك ‪.*۱:۷۸۳‬‬        ‫رك ‪ :‬جودان ‪.‬‬    ‫‪۴‬‬                                           ‫جودانه ‪-‬‬
```


## [2026-09-06T15:23:46.494Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"yava\\|jav\\b\\|Jav\" BQT_v2_pages.txt | head -20; echo \"=== which leaf\"; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'yava' in p or 'Yava' in p:\n        print('leaf',i,'printed',i+540)\nEOF"
}
```


### [2026-09-06T15:23:48.306Z] TOOL RESULT

```
=== which leaf
```


## [2026-09-06T15:23:56.336Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 51 52; do echo \"===== leaf $L (printed ~$((L+540)))\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -70; done"
}
```


### [2026-09-06T15:23:59.271Z] TOOL RESULT

```
===== leaf 51 (printed ~591)
  ‫جنیور‬                                                                                     ‫وت‬   ‫‪۳‬‬


‫جنکو لت (‪ - )۳‬بروزن‌مفلوك ‪.‬کی‌را‬                       ‫بالامبروزن بزمگاهی»‬        ‫جنگالاهی ‏‬

 ‫کوبند که از بیماری برخاسته باشد ق۽وت‬                 ‫غلیواج را گویند » و باینمعنی بجای های هوز‬
                        ‫‪.‬‬        ‫رفتار نداشته باشد‬     ‫نون وبای حطی هم‌بنظرآمده استکه جنگلالی‬
‫جنییت کش ‪ «۰‬شخصی را کوبند که‬                           ‫گیفزته‌اند ‪.‬‬         ‫سمی‬
                                                                              ‫راجی‬
                                                                                 ‫»وب‬
                                                                                   ‫فدا‬
                                                                                     ‫جونگلابی باش‬
 ‫اکسوبتلرامیکشد‪ ,‬جنیبت» اسب کوتل‌است ‪۴‬‬                  ‫جنکلو ك (‪ -)۱‬باکاف پروزن عشکبوت‬
‫و مبرآخور را هم کفته‌اند که رش سفید طوبله‬              ‫رنجوریرا گویند که ابام قاهت او باشد و بوفت‬
                                            ‫باشف ‪.‬‬     ‫ااربرگیرد ‪٩‬‏ ‪-‬‬    ‫وی‬‫دزبانو‬‫برخامتن دست بر‬
 ‫جنیور ‪ - ۲‬بنتح اول توالی بتحتالی‬                      ‫و کسی را لز کوبندکه دست و پای او کجواج‬
‫رسیده وواومفتوح برای بیلقطة زده‪ .‬بل‌صراط را‬                     ‫باشد » و باجیم فارسی هم آمده است‬
‫گویند > و بتقدیم تحتالی بر حرف الی هم‬                  ‫جنگو ان (‪_ )0‬وبزرر ارغوان ‪. ۴‬‬
                            ‫‪.‬له اعلم ‪.‬‬
                                     ‫آمده است ا‬                              ‫‪.‬‬   ‫سرتان‬
                                                                                     ‫ود‬‫دست‬
                                                                                         ‫نهرب‬
                                                                                            ‫هم ش‬
                                                                                               ‫نا‬




  ‫(‪ )۳‬چك ‪ :‬جنگوك ‪.‬‬                  ‫(‪ )0‬خم ‪>» ۱‬چش ‪ :‬جنکوان ‪۰‬‬           ‫لوك ‪.‬‬
                                                                           ‫ج)نچگك ‪:‬‬
                                                                                  ‫(‪۱‬‬
    ‫‪ « 02۷8021 . 02۷28021-. 6‬انتنگای >‬                                  ‫‪.‬‬     ‫وك‬ ‫ج‪-‬نر كك‬
                                                                                ‫ك‪:‬‬     ‫‪۱‬‬
          ‫مم دستان ر داستان‪.‬‬
                           ‫رست‬    ‫حدیت‬   ‫کم شف‬                ‫یا فتح جنگوان را در داستان فزود‬

     ‫مسعود سعف لفت فرس‪.*۹۹۳‬‬
   ‫‪ -‬جنست درعر هی «صوف یشم شر شش ساله وناقه‌است‬                             ‫‪۳‬ك‪ :‬جنکلوك‪.‬‬
                                                                                      ‫ر‬
  ‫و بمعتی مذ کور در متن در عربی‬             ‫«منتپی‌الارب»‬   ‫دهند تا برآن غله آرد»‬   ‫بدراهم یکی‬   ‫که‬


  ‫فچنود» رك ‪ :‬ص‬        ‫‪ -‬ممحف‬     ‫نَ‬             ‫جنيب“ است «جنیب‪,‬کامیر اسب کتل» «منتهی‌الارب»‪.‬‬
                                                                      ‫مقدمه ورك ‪ :‬چینود ‪.‬‬   ‫چیل وشش‬

===== leaf 52 (printed ~592)
                                     ‫يان هجد هم(‪)۱‬‬
           ‫جیم ابجد باواو مشتمل برهفتاد و نهلفت و کنایت‬                                ‫در‬


‫ويره از انگور‬
            ‫که در آن روغن از حبوبات ش‬                     ‫جو » نم اچولوبی باشد که بوقت‬
                                                                         ‫زمین شدبار(‪ )۲‬کردن بر گردن‬
‫و بفتح اول در عربی بمعنی رخصت و اجازت ‪-‬‬                                  ‫کاو گذارند ‪ - ۱‬و مراب نود‬
‫وروالی وروابی‪-‬‬   ‫وخط ودستك راه ‪-‬‬     ‫‪-‬‬    ‫خلاص‬     ‫‪۱‬و‬                   ‫و ششم باشد از خلوص زر که‬
‫و روان شدن ‪ -‬و آب دادن ستور و کشت زار‬                                     ‫"را بعربی‌عیارخوانند ‪ -‬وجوی‬
                                         ‫! باشد ‪٩‬‏ ‪.‬‬                     ‫آبرا یز گوبند ‪ ۴‬وبفتح‌اول‬
‫جواران ‪ -‬بضم اول بروزن‌خراسان»‬                       ‫‪۱‬‬                   ‫غله است ‪ ۴‬معروف که پاسب‬
                                                                        ‫و استر و امثال‌آن دهند ‪ -‬و با‬
‫ورفی‬
   ‫‪ ۱‬بمعنی جواز است که هاون چوبین ‪ -‬ظ‬
                                                                ‫جو‬      ‫تشدید ثالی درعربی بمعنی هوا‬
                                                           ‫فا هم رون ‪ ۱۱‬و کر‬                  ‫وه‬
‫عربی بمعنی‌نجات یافتن‪ -‬ودستك راه ‪ -‬و روان‬
   ‫شدن_ و آب‌دادن تور کوشت زار بود ‪. ۷‬‬
‫بضم اول بر وزن خلاصه »‬     ‫جوار ه ‪-‬‬                        ‫جوار = ص اول بروزن گداز ‪ .‬هاون‬
                                                          ‫سنگین و چوبن راگویند که سیر در آن کوبند‬
                           ‫بچاوبن باشد ‪. ۸‬‬                                         ‫وبییع‌رمهرای‌خوانند‬

                 ‫چش ‪ :‬شیار ‪.‬‬   ‫(‪)۷‬‬            ‫‪.‬‬      ‫هم‬
                                                      ‫د‪:‬‬‫جچش‬
                                                          ‫ی؛‬‫هدهم‬
                                                               ‫)‪ (۱‬چك‪ .‬چب ‪ :۱‬هژ‬

 ‫‪ - ۳‬اوستا ‪( ۵۷2۷-‬گندم )‪.‬‬                   ‫جوی ‪.‬‬        ‫‪۴‬ك‪:‬‬
                                                           ‫ر‬         ‫جوغ («‪.‬م‪).‬‬   ‫‪ -‬مخقف‬

   ‫» حندی باستان ‪ ۰ ۵۷8۷-‬کردی ‪ . ۵۷ . [12 . [6‬استی لا‪ .2‬ةل‬                        ‫پپلوی ‪ [۷3‬با ‪۷27‬‬
 ‫‪ ۷81.‬شننی ز‪ ۰ 2۷4‬سربکلی [‪ ( 8۵۷[ ۰ 8۷2۷‬آرد )‬
                                            ‫‪ ( ۵۷‬ارزن ) ‪ .‬بلوچی ‪۰ [۵0‬‬
  ‫‪.‬ربزندی ‪ 2۰‬برلیو نطنزی ‪ ۱ .2« [2‬ص‬      ‫‪« . )# 2۵-‬استقم‪ .۲4۹‬کیلکی‪ [۷۳0‬ف‬    ‫‪۷‬ز‪۷‬‬ ‫(ا‬
   ‫‪ , ۹‬سمنالی ولاسگردی‪ »[2‬سنگری ‪ » [¥0‬سرخه‌بی ‪, 8‬شهمیرزادی لاز ك‪ .‬ص‪۲۸۱‬‬
  ‫رك ‪ :‬نوروزنامه ص ‪ . ۳۳ - ۰۳‬جو ‪ 011160۲01‬از رستة غلات‌استوسنبله‌آن ساده وشاخه‌های‬
                 ‫ککللاب ‪.4۹۲‬‬
                           ‫اتهای زبانك‌آن درازاست و دانه‌های آن بزبانجه چبیده است‪ .‬د‬
                                                         ‫‪ - ۴‬لفتی درکواز‪ .‬رلك‪:‬کواز وجوازه ‪:‬‬
       ‫چون کرنجی که فر وکوفته باشد بجواز ‪.‬‬                   ‫ای بکوپال کران کوفته پبلان رایشت ‏‬
        ‫فرخی لفت فرس ‪۷۱-۷۷‬‬
  ‫‪« - ۱‬جواز بروزن سحاب خط ولوشته‌ایست مافر راازبرای‬                       ‫® _ رك‪ :‬جوازان ‪.‬‬
  ‫است تمال ازچهاریادان»<شرح‬      ‫گذشت نکه راهداران حالع او شو نده وجوازآبی است که داده شده‬

‫‪ - ۲‬باید دانت کمجوازان با‬                 ‫قاموی» ومصدر امت بمعنی رفتن و گذشتن « شرح قاموس*‪.‬‬
           ‫‪ - ۸‬رك‪ :‬جواز » کواز ‪.‬‬                  ‫الف ونون بمعالی مذ کور در عربی نامده ‪ .‬رك‪ :‬جواز‪.‬‬
```


## [2026-09-06T15:24:14.647Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 43 44 45; do echo \"===== leaf $L (printed ~$((L+540)))\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -60; done 2>&1 | head -160"
}
```


### [2026-09-06T15:24:16.209Z] TOOL RESULT

```
===== leaf 43 (printed ~583)
  ‫جسجم‬                                                                                        ‫وس‬    ‫ی‬


‫و هت و مستی باشد ‪ -‬و بمعنی‌درشتی وعریه‬              ‫مره‬
                                                      ‫و‬           ‫‪۱‬‬   ‫عقل‌دوم(‪ )۱‬باشه از عقول عثره‬
‫هم آمده است ‪ -‬و آرایش کننده و فرببنده را‬
                                                    ‫و پاکیزمرا نگیوزبند ‪ - ۴‬وبمعنی‌ذات همهت‬
‫نیز گوبند ؛ و بعضی کویند این معنی عریی‬             ‫چنالکه! گر گونند «ولالی‌خوش‌جم است*؛ مرادآن‬
‫دومتان‌را‬   ‫وبائالی مشدد بروزن هاش‬    ‫است ‪- ۴‬‬
                                                                            ‫باشد کهخوش ذات است ‪.‬‬
‫باشد ‪ -‬و در عرمی نوعی از‬         ‫پنهانی دیدن‬       ‫بالف‬     ‫حمار = بفتح اول و الی مشدد‬
                                       ‫بادبود ‪.‬‬    ‫خرما‬     ‫‪ ۰.‬مفر درحت‬    ‫و تنوین رای فرشت‬        ‫کشده‬

‫نم اول بروزن گمان »گیل‬         ‫جمان ‪-‬‬
‫باشد سياه رنگه »‬            ‫کنی‬
                              ‫بو آ‬
                                 ‫وت »‬
                                    ‫چو اس‬
                                        ‫دار‬                ‫و عربان شحم‌النخله و قلب‌النخله خوانند ‪.‬‬
‫و چون بشکننددرون‌آن فستقی بودکرم‌مصده را‬
                                                   ‫جمار النهرت پیعتی جارالتپر است ‪.‬‬
                                                   ‫وان ارس باشد مانند لبلوفر ویسوسته در آب‬
‫جما نی = بروزن یمالی ‪ .‬ساقی را‬                                                                     ‫فتاه‬
                                                   ‫همزه ‪ .‬نام یکی‬        ‫۔ بک‬       ‫جم اسرم‬

 ‫جمنو‪ - 3‬باتای قرشت بروزن حسموده‬                   ‫از انواعرباحین‌است که شکوفة آن بیار كوچك‬
 ‫بمعنی ئیل‌است» وآن شاد شدن نقی باشدبامور‬         ‫جوار او‬      ‫که در‬    ‫هسباشد ‪ ۰‬و سات آن «درختانی‬

                  ‫‪.‬‬   ‫حسنه که ازو صادر شود ©‬      ‫بلواب در‬ ‫باشند تعلق گرد یمنی مانند عش‬
                                                         ‫لقه‬

‫جمجم » نم هر دو جيم و سکون‌هر‬                     ‫آنهاپیچد » و عرب آرنیرحاان‌اللیمان گویند‬
‫دو میم ‪ .‬وه را کوبند و آن پا افزاری‌است‬                     ‫چسهلجیممان است؟ و اسیرم ربحان ‪.‬‬
                                                                                       ‫‪0‬‬
 ‫لای آن ارزسمان‬
              ‫بهاو‬
                 ‫کزهیر آن از لت‬                    ‫فر‬     ‫ثالی مخفف‬     ‫‪ -‬بفتح اول و‬   ‫جماش‬

                       ‫باشد ‪٩‬‏ ‪# .‬‬                 ‫وزن لواش؛ بمه‌نی‌شوخ وشوخی ‪ -‬وفریبند گی‪-‬‬
                                                                           ‫‪ :‬دوم‪.‬‬   ‫)‪ (۱‬چك‬


  ‫چم‪« .‬چم» تمیزیود » خطیری کوید ‪:‬‬         ‫‪۳۴‬‬       ‫‪ - ٩‬از برساخته‌های فرقه‌آنرکوان‪. ‎‬‬
         ‫دردل کیست شرم و حمیت و چم ؟»‬                    ‫کس چه داند که روسبی زنکیست؟‬
   ‫«لفت فری ‪۲۵۳‬‬

  ‫‪ - ۴‬از عربی» جماش ‪ « :‬رجل‌جماش بروژن شداد » نی مردی‬        ‫‪ - ۳‬رك‪ :‬چم‪.‬‬
  ‫»وباکه طلب میکند زهار سترده اابزشان‪ « ».‬شرخ قلسوس» حرفارسی‬
                                                           ‫است پیش آینده بزنان ک‬
                                                                      ‫بمعالی هذ کور در متن آعده ‪0‬‬
         ‫کرد ‪.‬‬   ‫قرارت‬
                     ‫اظر ‏ بدرد کشان احز س‬              ‫فغان کهارکس جماش شیخ شهرامروز‬
  ‫شیرازی ‪. ۰۹۰‬‬        ‫قحا‬
                 ‫آثر کیوان ‪.‬‬     ‫ةیٌ‬
                                   ‫رتهقها‬
                                        ‫فساخ‬
                                           ‫ظ ‪.‬از بر‬           ‫ه‬             ‫چمراكل‪:‬ی‪.‬‬
                                                                                    ‫‪۴‬‬
                                   ‫) بنقل از‬       ‫‪۱‬‬
                                                   ‫‪( 4‬‬
===== leaf 44 (printed ~584)
 ‫‪“OAT‬‬                                                                              ‫جمد چیتی‬

‫ثانی آب و در الث فیاتات وعرب اخگرآ شرا‬             ‫جمد چیفی ‪ -‬بیمتی‌ثلم صینی است؛‬
                          ‫جمره خوانشد ‪.‬‬
                                                   ‫آون‌سنگی‌بادسفید که درداروهای‌چشم بکاربرند‪.‬‬
‫جمر ی » ْم اول بروزن قمری »بلغت‬                        ‫جمدر س با دال ابجد بروزن ‪1‬‬
‫ماوراء‌النهر مردم بازاری و کم اصل و جلف‬              ‫کار ‪٩‬‏‬   ‫سلاحی استت که آنرا در هندوستان‬
     ‫‪SG‬‬             ‫و کدا و ‪ES:‬‏‬                    ‫کونند بروزن قطار » واصل آن « جنب در »‬
                      ‫اول هم آمده است ‪# .‬‬               ‫ان‬ ‫دسنی‬‫ندی‬
                                                                 ‫د هن‬
                                                                    ‫لیو شکاف ‪ -‬و‬   ‫بتهن‬‫اس‬
 ‫واو بروزن‬
         ‫<مر اور = بزاای هوز و‬                                                      ‫عزرائیل ‪. ۴‬‬
‫که روی و شکم‬       ‫شة‬‫و را‬
                        ‫گسیی‬
                           ‫همدیگر » ا‬               ‫ثالی‬   ‫اول و سکن‬      ‫سنتح‬
                                                                             ‫*ب‬
                   ‫وهردوپای او سفیدباشد ‪. ۴‬‬          ‫و بخاری استکه‬    ‫شتت مفتوح ‪e‬‏‬
                                                                                 ‫ورای‌قرش‬
‫جمس » بروزن لمس *یمعتی بخ‌باشد‬                      ‫در آخر زمتان در شاط ماه دوهی به دفعه‌از‬
                         ‫که ات ممحجمد أ‬             ‫زیر زمین بر میخیزد ‪ :‬یکی‌در هفتم ماه مکذور‬
 ‫‏‪ = ٣‬بروزن الست »جوهری‬       ‫چمست‬                  ‫و زمین ببب آن کرم میشود و آنرا سقوط‬
 ‫باشد فرومابه و کم قیمت‌و رنکش بکبودیهابل‬           ‫جمرة اول میگوبند ‪ .‬و دبگری در چپاردهم‬
‫است وبسنی کویندکبودی است بسرخی‌مایل‪» 6‬‬              ‫وآن را سقوط جمرة دویم میگوبند وسبب آن‬
‫مومدن‌آن بمدیهُ طیبه ترديك است ‪ .‬گوویند‬               ‫‪۳‬‬        ‫با‬
‫از ظرفی که از آن سنکه سازند هی چندشراب‬              ‫وبکم که سقوط جمرء سیم باشد اشجار و نباتات‬
‫خورده شود مستی‌نیاورد‪ .‬و اکر پاره ای از آن‬          ‫کرم شود ؛ و نزد عرب مراد از سقوط جمره‬
 ‫سنگه درقدح شراب اندازند همین خاصیت دهده‬            ‫مقوط منازل قمراست‪ .‬چه در هفتم ماه مکذور‬
‫واک مزر بان آندازن کرای بکو‬                         ‫مقوط جبهه باشد و در چهاردهم سقوط زبره‬
                                                    ‫ودر بيست وبکم سقوط صرفه وتأثیرات ایذها نیز‬
                                                    ‫همچنان است که در اول زمین گرمشود و در‬

            ‫ت ‪ 620086۲2‬د« ‪ ۳‬اجار > رد ‪‎‬ودرا ‪. (kathãri) kathûrê‬‬                  ‫‪- ٩‬‬
  ‫هيتوسف‪‎‬‬    ‫ظ معنی این لفط که بهندی دندان عزرائل‬             ‫؟ ‏ در حاشهٌ چك آمده‬
  ‫است ودهار‬      ‫ایئیل‬
                     ‫رعن‬
                       ‫ز بم‬
                          ‫جمدهر مختصر جمدهار است وعجم‬             ‫علط است » زرا که بهندی‬

  ‫بدال مخلوط التلفظ بهابمعنی دم شمشیر و غیرآنت » وبضی در وجه تة ابن لفظ چنین‬
  ‫کفته‌اند که جم بمعتی‌جفت‌است ودهار بمعنی‌عذ کور» پس دربنصورت بمعنی دو دمه باشد واین‬
  ‫=دای مرك( ‪21200 +‬‬
                  ‫‪ ۰.‬درسان کربت ‪ [۳200012‬مرک از ‪4۳ :‬ھز ( جم خ‬                          ‫اقرب است‬
                                            ‫) |ست ‪ .‬د کتر راجا > ‪.‬‬  ‫(در اردو ‪ :‬دهار) (دم شمشیر‬
 ‫=مز = جمشت» وهرسه درعربی از‬
                           ‫‪ ۴‬ج‬                      ‫‪ ۳‬رك ‪ :‬تملفات نوروزنامه ‪. ۷۱۱‬‬
                                ‫‪.‬‬   ‫‪ :‬کست‬    ‫ورك‬     ‫‏‪ ٩۷‬متن و ح ‪۱‬‬     ‫ست‪.‬انخب‬‫فارسی مأخوذ |‬
       ‫کوهر سرخ چون دهم بجمت؟‬                         ‫دین‌من خسروی است حمچو میم‬           ‫‪۵‬‬
        ‫خسرویلت ری ‪۳۰‬‬
  ‫درمادة جمس آمنه ا‬                    ‫ت نبافتیما‬             ‫ا‬       ‫‪۳9‬‬                 ‫(قط را‬


                                                       ‫‪۹‬‬   ‫فرهنك مقط بيار دارر» خب ‪۸۹۱‬ح‬
                                              ‫‪ #‬جهو ‪ -‬بفتح اول ودوم » رك ‪ :‬جمست‪.‬‬

===== leaf 45 (printed ~585)
  ‫سقف‬
  ‫‪۳‬‬ ‫‪۰‬‬
                                                                                        ‫وس‬
                                                                                         ‫ز‪۷‬‬


‫است معروف که او را عربان متوشلخ کویند ‪.‬‬         ‫مائند لمل ‪ - ۱‬کونایه ازمردم بداسل و جاهل‬
‫واو در اول جم نام داشت یعنی ساطان‬                                                             ‫ج‬‫ج‬
‫ویادشاه‌بزر که ‪ ,‬و سبب‌جمشید کفتن آن شدکه‬       ‫»بیان قطه‌دار بروزن‬
                                                                  ‫جمشاسپ؟ ش‬
‫او سیر عالم میکرد چون باآنربایجان رسیدروزی‬    ‫‪:‬بایان عليهالسلام |ست اکر با خانم‬           ‫هلت‬
‫بود کهآ فتاب بنقطة اول‌حمل آمده بوده فرمود‬     ‫و حور و ری مذ کور شود » و جمشداستا کر‬
‫که تخت مرصمی را در جای بلندی کتاشتند‬           ‫بگویند ‪ ۴‬و نامیس جمشید‬           ‫بصاجراماوحی‬
‫چون‬      ‫وتاج مرصمی‌بر سرنهاده آبنر‌تخت شت‪.‬‬                                             ‫هم هت ‪.‬‬
‫آفتاب طلوع کرد شاع و پرتو آفتاب بر آن‬          ‫غمناك ‪ ,‬کفش‬       ‫رزن‬
                                                                   ‫= بو‬    ‫جمشثاك‬
                                                                   ‫وپای افزار راکوبند ‪¥. ۴‬‬
‫تاج و تخت افتاد‪ .‬شماعی در غابت روشنی یدید‬
‫آمد و چرن‌بزبان پهلوی شماع را شید میگویند‬       ‫» بروزن ادك » بمعلىجمشاك‬        ‫جمشك‬
‫اینلفظ را برهجم» افزودند و جمشید گفتند یعنی‬      ‫وای‬         ‫یی ادارا‬           ‫کے کک کی‬
‫یادشاه روشن »> و در آنروز جشنی عظیم کردند‬
           ‫و آن روز را نوروز نام نه‌ادند ‪۷‬‬     ‫‪ea‬‬
 ‫پ)‪٣.‬‏قیل یکرشاسي !‬
                  ‫س(ید‬
                     ‫اجمد‬
                        ‫‪ - ۴‬برساخته فرقهٌ آکذیروان؛ از‬              ‫‪:- ٩‬كر كل ‪‎‬ص‪. ۳۹۹ ۱‬‬
  ‫‪ . ۴‬رك‪ :‬جم‪« .‬چپارمین نظر از کتاب دستان (المذاهب) در تعرنف جمشاسپیان»» است که« اشارا‬

                ‫و ایشان تابع جمشاسپ بجنمشدبن تهپموری‌اد» «دبستان ‪.* ۶۹‬‬                   ‫جمشالی‬
                    ‫‪ _ ۵‬رك‪ :‬جمغاك » چمشاك »‬            ‫جمشك‪.‬‬     ‫رك ‪ :‬چمشاك »‬   ‫‪-‬‬   ‫‪۴‬‬

  ‫‪ - ۱‬از ‪ :‬جم ا(وستا ‪ , 20111۷‬ساسکریت (ودا) ‪ 21712۷۰‬پهلری‪ < 012۷‬بارتولمه‬
 ‫‪,‬پلوی ‪ 0۵115‬بمعنی درخثان و روشن )‬  ‫(وستا ‪ 2162151‬پ‬ ‫ديبرك ‪۸٤۲۰‬‏ ‪ +‬شید ا‬                       ‫‪۰‬‬
 ‫خا ‪,‬عنی جم درخشان ؛ جمدرکاتها بدون صفت دششه آمده « بنای ‪ » ۸ : ۲۳‬و جدها این‬
  ‫( رك ‪ :‬روزشماری ص ‪. ۰۳‬‬         ‫‪۰۳ 0‬‬     ‫‪5‬‬   ‫وت‬    ‫‪۵۲ :‬‬   ‫صفت بدان ضمیمه شده «آبان ‪,‬شت‬
      ‫در ودا یمه(جم) پسرخورشید ونضتین بشری است که مرکه‌براو چیره شده » بردوزخ حکومت‬
 ‫میکند ‪ ۰‬دارستانهای ملی ما نز آمده که مدت سبصدسالدرزمان جم بیماری وم که‌نبود يااو‬
  ‫کمراه شد وجهان بآرشفت و بیماری ومر که‌بازکشت‪« .‬شاهنامة فردوسی» بقول اوستا (وندیداد‪.‬‬
  ‫فصل ‪ )۲‬او تین کسی است که اهور مزدا دين خود را بدو سپرد ‪ .‬در روابات داستانی ابران‬
  ‫جم یکی از بکزتررین پادشاهان سلسلةٌپیشدادی است و در ادییات پارسی « جام جهان لما“ پدو‬
  ‫جم» یز گویند (رك‪ :‬جام جهان نمابقلم نگارنده در مجلةٌ داش ‪٦ : ۱‬ص‏‬        ‫ام‬
                                                                          ‫دتجکه‬
```


## [2026-09-06T15:24:23.466Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for w in ['جلیتقه','جليتقه','جلیقه','جليقه','جلتقه']:\n        if w in p:\n            print('leaf',i,'printed~',i+540,'word',w)\nEOF"
}
```


### [2026-09-06T15:24:25.745Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:24:32.998Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(34,45):\n    p=pages[i]\n    import re\n    heads=re.findall(r'([؀-ۿ]{2,12})\\s*[»\\-=]\\s*(?:بفتح|بضم|بکسر|بم |نم |بر وزن|بروزن)', p)\n    print(i, i+540, heads[:8])\nEOF"
}
```


### [2026-09-06T15:24:35.258Z] TOOL RESULT

```
34 574 ['جغر']
35 575 []
36 576 ['جفته']
37 577 []
38 578 []
39 579 ['جلبان']
40 580 []
41 581 ['جله', 'ند']
42 582 []
43 583 ['حمار', 'نی', 'جمجم']
44 584 ['جمس']
```


## [2026-09-06T15:24:38.448Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 41 42; do echo \"===== leaf $L (printed ~$((L+540)))\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt; done 2>&1 | head -120"
}
```


### [2026-09-06T15:24:40.662Z] TOOL RESULT

```
===== leaf 41 (printed ~581)
   ‫جر‬                     ‫‪۱‬‬                                                                             ‫‪~er -‬‬

‫با نون بر وزن عروسك »‬            ‫جلو نك‬                      ‫جلو ‪ -‬بفتح اول وضم انی ‪:‬روزن زلوه‬
‫امثالآن‬   ‫و‬   ‫و خار‬   ‫هندوانه‬   ‫بنهٌ خریزه و‬   ‫باره و‬                     ‫مردم شوخ ‪E‬‏‬
                                            ‫باشد © ‪.‬‬        ‫کبایرا همکفته اندچه اکر از چوب باءد جلو‬
                                                              ‫پوس ای مور‬                       ‫بای‬             ‫ام‬
 ‫‪۰‬معئی‬
     ‫ب‬        ‫یز‬
               ‫مزن‬
                 ‫هر و‬
                    ‫مب‬‫جلو یز ‪= ۱‬‬
 ‫ی‬            ‫و‬                 ‫ی‬


‫گزیده‬     ‫ویر‬     ‫‪۷‬‬     ‫مات‬              ‫مفد و عماز‬
                ‫و انتخاب کرده را نز گوند ‪.‬‬                    ‫سر‌شت‬               ‫اه‬


                                                                                               ‫وخوی‌ید را گوشد ‪.‬‬
‫جله » بضماول وح ثانی‌مشدد ک"روحة‬
‫وعرب آن جلاهق باشد ‪-‬‬   ‫ریمانرا کویند م‬
 ‫و گیاهی‌بود سربپن که احزاه ی‌نمباك ودءوارهای‬               ‫‪۳‬اول و ضم اور مم‬                         ‫چوبن باشد؛‬




                                                      ‫‪2‬‬
                                                                                                      ‫گفته اند ؟ ‪.‬‬
‫حمام و زبرهای خم آب و شراب و امثال آن‬
 ‫مائعات را فيز گویند‬   ‫ووف‬ ‫ظدر‪_۸‬‬  ‫روب‬                        ‫جلور؟ » با زای هوز بر وژن تموز »‬
‫همچوخم و خمچه ر کدوی شراب و امثالآن‪-‬‬                         ‫مفزدار و معروف‬         ‫چزست‬       ‫وآن‬     ‫فندق باشد ‪۴‬‬

‫کف‬      ‫کدرا از‬    ‫رف فو مادم‬                                 ‫لوز ات‬          ‫گوند‬        ‫؛ و یی‬         ‫که خورند‬

‫خرما بافند و خرمادر آن کرده از جابی بجابی‬                                    ‫و بادام گوهی را نیز گفته اند ‪.‬‬

  ‫برند ؛ و بعضی گویند باین معتی عریست ‪٩‬‏‬
 ‫‪ -‬و ہمعنی درخت خرما هم بنظر آمده‌است ‪¥.‬‬
                                                             ‫جل وزغ =‪ -‬بضم اول و کر ثانی »‬
                                                             ‫جام غوك است» وآن چیزی باشد سبزرنگ که‬
‫وزن مویز » بمعتی کمندیاشد‬          ‫جلیز سبر‬
                                                             ‫در رویهای آب‌استاده بهم هیرسد * وانرایعربی‬
‫و عملزژ‬   ‫و سعنی مد‬       ‫خوالند ‪-‬‬   ‫مقود‬      ‫سرنی‬   ‫و‬
                                                                      ‫طحلب و خرء الشفادع (‪ )۱‬نیز گویند ‪.‬‬




              ‫اویید‬
                                 ‫هم آمده است س‬
                                                              ‫مشفف‬        ‫عحوزه‬     ‫وزن‬   ‫بر‬    ‫‪-‬‬    ‫جلو زه‬
 ‫‪9‬پرده‬‫جلیل» سم اول بر وزن سهیل ء‬
‫و چادر و کجاوه پوش باشد ‪ ۴۷‬و جل اسب را‬
                                                               ‫چلنوزه است‪ ۰‬و آن منزی باشد بادريركاژو‪.‬‬
 ‫نیز گوبند ‪ -‬و نامشخصی بوده که کربهبیاری‬                     ‫جلو ند = بر وزن فرزند ' بمعنی چراغ‬
                                         ‫نگاهداشته ‪.‬‬                                                           ‫باشد ‪.‬‬


                                                            ‫(‪ )۱‬خم‪ ۱۰‬چب‪ .۱‬چش‪ :‬خر الضفادع‪.‬‬
     ‫‏‪ - ٩‬اکنون بممتی‌پیش ومقابل استممال‌شود» مأخون ازترکی«جیلاو» بمعنی‌لگام اسب» پیش»‬
  ‫معرب‌آن جلوز بکر اول‬               ‫‪۴‬‬           ‫‪ - ۴‬رك‪ :‬جلو» چلوچوب ‪.‬‬                    ‫برابر مجفتایی ‪۸۰۳٩‬‏ ‪.‬‬
                  ‫‪su 202۱۱۵۷۵‬ا‪yroC‬‏ دایتی ‪. › ۹۷۱‬‬                     ‫‪۴‬‬             ‫و تشدید دوم مفتوح«تفس؟‪.‬‬
                  ‫¶ ‪ -‬رك‪ :‬جلبيز» جلیز‪.‬‬                    ‫© درکیلکی ‪ .01‬رك‪ :‬جلنکه‪ .‬چلونگه ‪.‬‬

                                                 ‫‪:‬‬        ‫یلد‬
                                                            ‫گهروفض‬
                                                                 ‫‪« -‬جلویز » مفد است» طا‬
              ‫روانبود زندان و بند وست تنم (روا لبود بزندان و بنده بسته‌تنم ‪( .‬دهخدا))‬
  ‫‪٤ .‬‏ لغت فری ‪۳۷۱٩‬‏ این بیت برای معتی‪ .‬اول‬                            ‫اکر نه زلفك مشکین اوبدی‬
  ‫_ « جله چون سماروغ بود‪ ».‬رك ‪ :‬لفت فری‬                                                   ‫(کمند) السب است ‪.‬‬
  ‫«شرح قاموی»‪.‬‬        ‫بز رکه‌از نمروخرماست‪.‬‬          ‫کدوی‬    ‫‪۳‬‬        ‫جله ‪,‬ضم اول‬    ‫‪۹‬‬              ‫باشاهد)‪.‬‬   ‫‪(۰۶:۶‬‬


  ‫بقیه درصفحة ‪4۸‬‬

===== leaf 42 (printed ~582)
                                       ‫بیان شدانهزم‬

           ‫و هفت لغت و کنات‬             ‫در جيم آبجد با میم مشتمل رست‬

‫ابنیمع»نی | سلیمان است» ودرجابی کهباجامو پیالهسذکور‬              ‫وون‬
                                                                   ‫کول‬
                                                                     ‫سا‬‫جم ‪ = ۲‬بت‬
‫و آنجا که باآبینه وسد نام‌برده‬   ‫مشود جمشد»‬      ‫عله‌اللام‬   ‫و تلم سلیمان‬     ‫مادشله بزر که ماشد ‪-‬‬


‫وجمشید همهست ‪ . ۴‬لیکن درجایی که بانگین | میشود اسکندر ‪ -‬و بمعنی مردمك چشم هم‌بنظر‬
‫و وحش و طبر و دمو و بری گفته میشود مراد | آمده است بزبان اهل مرو شاه جان ‪ ۴‬و نام‬

  ‫‪ - ۴‬یں ازحہلۂ عرب و استقرار اعلام درایران» داستانپای‬             ‫‪.‬‬   ‫جمشد‬    ‫رك‪:‬‬     ‫‏‪٩‬‬

   ‫ملی ما با قصههای سامیان آمیخته شد‪ .‬یادشاهان ناموران ابران با بیامبران وشاهان بنی‌اسرائل‬
  ‫ص ‪ ۳۸‬ببعد‬     ‫‪:‬نا‬
                  ‫دكب‬
                    ‫(ر‬‫دز‬
                       ‫اورمیا وعزبر خلط شم‬             ‫زارتبشتراباهيم‬         ‫له‬
                                                                               ‫جدماز‬
                                                                                   ‫نتن‬
                                                                                     ‫رابطه یا‬
  ‫شیدرا باسلیمان مشتبه ساختند » زیرا این دو پادشاه دررمض احوال و اعمال‬
                                                                     ‫ج)مو‬
                                                                        ‫و‪۶ ۱۸۱‬‬
  ‫ماد استخدام دیوان وجنیان و طاعت جونانس ازابشان و سرفکردن درهوا (طبق‌داستانها) بهم‬
  ‫شبیه بود و ایرانان م رکز جمشید داستانی‌را کشور فاری‌مبداننته‌اند و آثاربافی ماندء داربوش‬
   ‫وخشیارشا ودیگر یادشاعان هخامنشی را بجم(جمتید) انتاب داده اند و نام «تخت جمشید» خود‬
   ‫حاکی ازانت » وبراثر اعجاب از ابنة‌مزبور ساختمان آلهارا بدیوان‌دبت داده اند دوراساطیر‬
  ‫سامی از لمان دیوان را درخدمت داشت و در بنای بت المقدي آنابرا یککامراشت ‪ .‬از اشرو‬
  ‫حرقرون اسلامی!ین دو تن یکی بشمار آمدند‪ ,‬فاری‌را دنختگاه سلیهان» وپادشاهان فاری را « قایم‬
   ‫مقلم سلیمان » و « وارث ملت ملیمان » خواندند وحتی آرامگاه کوروش بزرك موسی سلللة‬
                                             ‫هتامنشی را « متهد مادرسلمان » نامیدند ‪.‬‬
   ‫هجلم جم» رایز در ادبیات پارسی گاهسلیمان نبت داده‌اند و انگنتری مشهور سلیمان را بجم‪:‬‬
   ‫خزاتمی کهدکمی‌شودچه غم‌دارد؟ حافظ شیرازی‪.‬‬                  ‫رمد‬
                                                                ‫دلما ج‬
                                                                     ‫وج‬          ‫یت‬
                                                                                  ‫اغب‬
                                                                                    ‫می که‬
                                                                                        ‫دل‬
                    ‫رك ‪ :‬جام جهان‌نما بقلم نگارنده درمجلهةٌ داش ‪٩ : ۱‬‏ ص ‪۱۰۳-۳۰۳‬‬
   ‫‪ - ۴‬ملف ذیل «چم» کوبد ‪ « :‬مردم دارالمرز ومردم‌مروشاهجان چثم را چم‌میگویند‬
```


## [2026-09-06T15:24:57.718Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt incoming/BQT/BQT_v5_pages_faseng.txt; do echo \"-- $f\"; grep -c \"جلیقه\\|جليقه\\|جلیتقه\\|يلک\\|یلک\" $f 2>/dev/null; done; echo \"=== search v5 for jaleco/yelek latin\"; grep -n -i \"yelek\\|jaleco\\|gilet\\|jileco\" incoming/BQT/BQT_v5_pages_faseng.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head"
}
```


### [2026-09-06T15:24:59.620Z] TOOL RESULT

```
-- BQT_v1_pages.txt
88
-- BQT_v2_pages.txt
163
-- incoming/BQT/BQT_v3_pages.txt
68
-- incoming/BQT/BQT_v4_pages.txt
77
-- incoming/BQT/BQT_v5_pages.txt
7
-- incoming/BQT/BQT_v5_pages_faseng.txt
=== search v5 for jaleco/yelek latin
```


## [2026-09-06T15:25:04.759Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport glob\nfiles={'v1':'BQT_v1_pages.txt','v2':'BQT_v2_pages.txt','v3':'incoming/BQT/BQT_v3_pages.txt','v4':'incoming/BQT/BQT_v4_pages.txt','v5':'incoming/BQT/BQT_v5_pages.txt'}\nfor k,f in files.items():\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(k,e); continue\n    pages=t.split('\\f')\n    for i,p in enumerate(pages):\n        for w in ['جلیقه','جليقه','جلیتقه','جليتقه','جلتقه','جليقة']:\n            if w in p:\n                print(k,'leaf',i,w)\nEOF"
}
```


### [2026-09-06T15:25:06.913Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:25:11.880Z] TOOL CALL #44: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:584 --image 2>&1 | head -30"
}
```


### [2026-09-06T15:25:13.891Z] TOOL RESULT

```
no scan of BQT covers printed page 584 (see 'scans' in refs_online.json)
```


## [2026-09-06T15:25:20.672Z] TOOL CALL #45: Bash

```json
{
 "command": "curl -s \"https://archive.org/metadata/borhan-ghate-v2\" -o /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2meta.json && python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2meta.json'))\nprint(d.get('server'),d.get('dir'))\nprint([f['name'] for f in d['files'] if f['name'].endswith(('.pdf','djvu.txt','_djvu.xml','_chocr.html.gz','_djvu.txt'))][:10])\n\""
}
```


### [2026-09-06T15:25:26.538Z] TOOL RESULT

```
ia600609.us.archive.org /25/items/borhan-ghate-v2
['برهان قاطع، جلد دوم.pdf', 'برهان قاطع، جلد دوم_chocr.html.gz', 'برهان قاطع، جلد دوم_djvu.txt', 'برهان قاطع، جلد دوم_djvu.xml', 'برهان قاطع، جلد دوم_text.pdf']
```


## [2026-09-06T15:25:30.052Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for q in \"جلیقه\" \"جلیتقه\"; do echo \"== $q\"; curl -sG \"https://ia600609.us.archive.org/fulltext/inside.php\" --data-urlencode \"item_id=borhan-ghate-v2\" --data-urlencode \"doc=برهان قاطع، جلد دوم\" --data-urlencode \"path=/25/items/borhan-ghate-v2\" --data-urlencode \"q=$q\" | head -c 1500; echo; done"
}
```


### [2026-09-06T15:25:34.656Z] TOOL RESULT

```
== جلیقه
{"ia": "borhan-ghate-v2", "q": "\u062c\u0644\u06cc\u0642\u0647", "indexed": true, "matches": [{"text": "\u0647\u0647 \u0627\u0632 \u0635\u0641\u062d\u0647\u064c \u0665\u06f8\u06f4\u200f \u06f0- \u0631\u0643 : \u062c\u0644\u0628\u06cc\u0632 , \u062c\u0644\u0648\u06cc\u0632 . -\u0669\u0669\u200f \u0639\u0631\u06cc\u06cc \u0621\u0645\u0635\u0641\u0631 \u062c\u0644 (\u00ab.\u0645.) \u06f2\u06f4\u06f3- \u0628\u0631 \u06af\u0631\u062f\u0631\u062e\u0634(\u0633\u06cc\u0628)\u06cc\u0631, \u0642\u0637\u06cc\u200c\u0686\u0646\u062f \u0632\u062f \u0648 \u0627\u0646\u062f\u0631 \u062f\u0645 \u0627\u0648\u0633\u0628\u0632 \u062c\u0644\u06cc\u0644\u06cc \u0632 \u0632\u0645\u0631\u062f . \u00ab\u0645\u0646\u0648\u0686\u0647\u0631\u06cc \u062f\u0623\u0645\u0641\u0627\u0646\u06cc*\u06f2 \u06f0.\u0669\u06f1\u200f * \u062c\u0644\u0648 \u06af\u06cc\u0633\u0631 \u06cc- \u067e\u06a9\u0633 \u0627\u0648\u0644 \u0648\u0641\u062a\u062d \u062f\u0648\u0645 (\u062f\u0631 \u0644\u0647\u062c\u0629\u0645\u0631 \u06a9\u0632\u06cc) \u061b \u0645\u0646\u0639\u061f \u0645\u0645\u0627\u0644\u062a . \u0631\u0643:\u062c\u0644\u0648. # <IA_FTS_MATCH>\u062c\u0644\u06cc\u0642\u0647</IA_FTS_MATCH> = <IA_FTS_MATCH>\u062c\u0644\u06cc\u0642\u0647</IA_FTS_MATCH> \u0628\u06a9\u0631\u0627\u0648\u0644 \u0648\" \u0641\u062a\u062d \u067e\u0646\u062c\u0645 \u00bb \u0627\u0632 \u062a\u0631\u06a9\u06cc \u0627\u0632 \u0641\u0631\u0627\u0646\u0647 864 \u00ab \u0645\u062d\u0645\u062f \u0639\u0644\u06cc \u0642\u0631\u0648\u063a\u06cc 
== جلیتقه
{"ia": "borhan-ghate-v2", "q": "\u062c\u0644\u06cc\u062a\u0642\u0647", "indexed": true, "matches": []}
```


## [2026-09-06T15:25:46.072Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sG \"https://ia600609.us.archive.org/fulltext/inside.php\" --data-urlencode \"item_id=borhan-ghate-v2\" --data-urlencode \"doc=برهان قاطع، جلد دوم\" --data-urlencode \"path=/25/items/borhan-ghate-v2\" --data-urlencode \"q=جلیقه\" -o j.json && python3 -c \"\nimport json;d=json.load(open('j.json'))\nfor m in d['matches']:\n    print('PAR', json.dumps(m.get('par'),ensure_ascii=False)[:300])\n    print(m['text'])\n    print('---')\n\""
}
```


### [2026-09-06T15:25:49.329Z] TOOL RESULT

```
PAR [{"l": 1686, "t": 3250, "r": 2046, "b": 3309, "page": 42, "boxes": [{"l": 1866, "t": 3250, "r": 1980, "b": 3309, "page": 42}, {"l": 1686, "t": 3250, "r": 2046, "b": 3309, "page": 42}], "page_width": 2569, "page_height": 3970}]
هه از صفحهٌ ٥۸۴‏ ۰- رك : جلبیز , جلویز . -٩٩‏ عریی ءمصفر جل («.م.) ۲۴۳- بر گردرخش(سیب)یر, قطی‌چند زد و اندر دم اوسبز جلیلی ز زمرد . «منوچهری دأمفانی*۲ ۰.٩۱‏ * جلو گیسر ی- پکس اول وفتح دوم (در لهجةمر کزی) ؛ منع؟ ممالت . رك:جلو. # <IA_FTS_MATCH>جلیقه</IA_FTS_MATCH> = <IA_FTS_MATCH>جلیقه</IA_FTS_MATCH> بکراول و" فتح پنجم » از ترکی از فرانه 864 « محمد علی قروغی . فون زیانهای میگانه در زبان فارسی . آموزش ویرورش ۲۵ :٥ص‏ ۳۸» ؛ جامة کوتاه وبی آستین که روی پیراهن و زیر یم تنه پوشند .
---
```


## [2026-09-06T15:26:31.906Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 226 -l 226 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg226hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg226hi.png'); print(im.size)\nim.crop((1120,3740,2100,3890)).save('c_ijlak2.png')\n\""
}
```


### [2026-09-06T15:26:36.088Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-06T15:26:38.486Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_ijlak2.png"
}
```


### [2026-09-06T15:26:38.497Z] TOOL RESULT

```

```


## [2026-09-06T15:26:48.742Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT\"; grep -n -i \"jelek\\|jeläk\\|chaleco\\|jaleco\\|gilet\\|jilek\" LKT.txt | head -20; echo \"=== TTS\"; grep -n -i \"jelek\\|jäläk\\|yelek\" TTS.txt 2>/dev/null | head -10; ls incoming/TTS 2>/dev/null"
}
```


### [2026-09-06T15:26:48.817Z] TOOL RESULT

```
=== LKT
2279:Tk.  jelek.]
2281:<I5I.  Tk.  jelek: 'Weste'  [Dozy  Vetcin  431];  hieraus  ait. giulecco,  sp.  gileco,  joleco,  chaleco,  pg. jaleco,  prov.  gileco,  frz.  gilet,  it.  giU '\Vesle\  rum.  ilic  Manger  Bauernmanter; russ.  zilef,  bulg.  serb.  iilet,  bulg.  ziletka 'Weste'.  —  [Die  alte  von  MENAGE  her- rfihrenJe  Ableitung  führte  frz.  gilet  als demin.  auf  den  Eigennamen  Gilles  < Aegidius  zurück;  hiermit  sollte  eine komische  Figur  des  Jahrmarkttheaters bezeichnet  worden  sein,  in  deren  Kostüm die  Weste  eine  ähnhche  Rolle  spielte, wie  die  Hosen  beim  Pantalon,  vgl.  G.  PA- RIS in  Romania  X,  444.  ZfromPh  V, 100.  XIV,  180.  SBKAW  Wien  phil.- hist.  Kl.  CXXXYIII,  1,  S.  8.]  [DE  291. ML  9582.
8261:jaleco  951
=== TTS
TTS_pages.txt
TTS_vambery1878_uoft_djvu.txt
TTS_vambery1878_uoft.pdf
```


## [2026-09-06T15:26:59.118Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 2270,2290p LKT.txt; echo \"=== page marker\"; awk 'NR<2285 && /^\\s*[0-9]{2,3}\\s*$/ {print NR\": \"$0}' LKT.txt | tail -3"
}
```


### [2026-09-06T15:27:00.875Z] TOOL RESULT

```
'Sachte,  laugsam'  [Stamm  jaw  'eitel, nichtig,  schlecht'  Vämbery  TktEtWb S.  109,  Nr.  119];  hieraus  rum.  iavaf 'sachte ;  Gemächlichkeit'.
947.  Tk.  jawasa:
'Eisen-  oder  Holzkneife',  die  man  dem Pferde  an  die  Nüstern  steckt,  wenn  man es  beschlagen  will  [wohl  zu  jawas  'leise, sachte';  Kel6kian  Kämüs  1361];  hieraus rum.  iava^a,  iaba§a  'Bremse,  Kneife (für  widerspenstige  Pferde)'.
948.  Tk.  jedek:
'Handpferd,  Vorspann'  [nur  zufällig  an a.r.  jad,  jed  'Hand'  anklingend?];  hier- aus rum.  jedec,  edec  'Zubehör,  Gepäck, Zugseil',  daher  a  trage  la  edec  'ein Schiff  treideln'.
949.  Hebr.  JehiUa:
Vierter  Sohn  des  Patriarchen  JAKOB, danach  Stamm  und  Königreich  Juda ibenannt:  gr.  'loOba?,  'loOba  [bab.-ass. Ja'üdii  'der  gelobt  oder  berühmt  ist']; hieraus  lat.  judaeus,  afrz.  juien,  fem. juive  und  danach  ein  neues  masc.  frz. juif,  prov.  juzieu,  k3it.  juheu,  sp.judio, pg.judeu,  it.  (alt)  giiulio  [neu:  ehreo], engl,  jeiv,  dtsch.  Jude;  engl,  yiddisch, dtsch.  jiddisch  zur  Bezeichnung  der dtsch.  Sprache  im  Munde  der  Ostjuden; russ.  zid,  6ech.  zid,  poln.  zyd  [vgl.  hier Nr.  424].
950.  Tk.  jel:
'Wind,  Lähmung,Rheumatismus'  [Stamm jil,jel  'Wind,  windig'  Vämbery  TktEtWb S.  131,  Nr.  1421];  hieraus  rum.  tele,  ele 'Lähmung,  böse  Fee'.  [Löbel  EITAP 55.
Tk.  jelek.]
76
<I5I.  Tk.  jelek: 'Weste'  [Dozy  Vetcin  431];  hieraus  ait. giulecco,  sp.  gileco,  joleco,  chaleco,  pg. jaleco,  prov.  gileco,  frz.  gilet,  it.  giU '\Vesle\  rum.  ilic  Manger  Bauernmanter; russ.  zilef,  bulg.  serb.  iilet,  bulg.  ziletka 'Weste'.  —  [Die  alte  von  MENAGE  her- rfihrenJe  Ableitung  führte  frz.  gilet  als demin.  auf  den  Eigennamen  Gilles  < Aegidius  zurück;  hiermit  sollte  eine komische  Figur  des  Jahrmarkttheaters bezeichnet  worden  sein,  in  deren  Kostüm die  Weste  eine  ähnhche  Rolle  spielte, wie  die  Hosen  beim  Pantalon,  vgl.  G.  PA- RIS in  Romania  X,  444.  ZfromPh  V, 100.  XIV,  180.  SBKAW  Wien  phil.- hist.  Kl.  CXXXYIII,  1,  S.  8.]  [DE  291. ML  9582.
952.  Tk.  jelkowan :
'Ein  Vogel,  Halcyon  oder  Porcellaria yelcovan'  [aus  tk.  jel,  s.  hier  Nr.  950, und  tk.  kowan,  Part,  praes.  act.  des  Vbs. kowmak  'jagen'  vom  Stamme  kog^  kow 'jage»,  verfolgen'  Vämbery  TktEtWb S.  91,  Nr.  95;  Kelekian  KämOs  1355  b]; hieraus  rum.  elcovan  'Eisvogel,  See- schvvalbe'.
953.  Tk.  jenibahar: 'Spanischer  Pfeffer,  Capsicum  annuum' [aus  ik.jeni  'neu'  vom  Stamme  en,  en, jeü  'klein,  jung,  neu'  Vämbery  TktEtWb S.  32,  Nr.  35 II  und  ar.  lahär  'Gewürz']; hieraus  rum.  enibahar  'Paradieskörner, Piment  zum  Würzen  der  Wurst'.
954.  Tk.  jeniceri:
[Aus  tk.  jeni,  s.  hier  Nr.  953,  und  ceri 'Heer,  Truppe'  vom  Stamme  der,  ter 'eng  zusammenziehen,  vereinigen'  Väm- bery TktEtWb  S.  170,  Nr.  182  II],  Name des  stehenden  tk.  Heeres  von  1330  bis 1826,  in  welchem  Jahre  Sultan  MAH- MÜD  II.  die  Truppe  auflöste  [vgl.  Th. Menzel,  Das  Korps  der  Janitscharen.  In Beiträge  zur  Kenntnis  des  Orients.  I. (1902/03)  und  in  der  Beilage  zur  All- gem.  Zeitung  1903,  Nr.  284/286].  Hier- aus [und  aus  der  älteren  tk.  Form  ja- nycary]  bulg.  janil^arni,  serb.  janicar^ klruss.  janycar ,  jancar,  necar,  russ. janicar,  poln.  janiczar,  cech.  janicar ; dtsch.  Janitschar,  ndl.  jaiiitsaar,  engl. janizary;iLgiannizzero,  ivz.jannissaire, sp.  jemzaro,  pg.janizaro,  rum.  ianicer, ienicer.  [Devic  DEt  143.  ML  4583. Gorjajew  436.    Bern  SlEtWb  445.
9.55.  Chili,  jensheil : [Aus  jen  'Mensch'  und  shen  'die  Wurzel von  Panax  ginseng']  Name  für  die Wurzel  der  Panax  ginseng,  die  berühmte Universalmedizin  der  Chinesen;  die  Vor- setzung der  Bestimmung  jen  ist  wohl
erfolgt,  weil  die  gabelförmige  Wurzel eine  gewisse  Ähnlichkeit  mit  der  mensch- lichen Gestalt  zeigt.  Hieraus  dtsch. Ginseng,  engl,  ginseng  usw.  [Hirth ChinFW  209.
956.  Jap.  jinrikisha:
[Aus  jin  'Mensch',  s.  hier  Nr.  955,  riki 'Kraft',  sha  'Wagen',  also  'Menschen- kraftwagen'] 'ein  leichtes,  zweiräderiges Holzwägelchen,  das  von  einem  Manne gezogen  wird';  hieraus  engl,  rickshaw, aDgloinä.jennyrickshaw.  Dieses  Gefährt ist  übrigens  erst  seit  ungefähr  1870  in Gebrauch,  hat  sich  aber  in  kürzester Zeit  über  ganz  Japan,  die  Häfen  Chinas, die  malayischen  Inseln  und  Indien  ver- breitet; neuerdings  wird  die  Rickshaw stellenweise  durch  die  Strafsenbahn  ver- drängt. [Hobson-Jobson  459/460.  Ghamb AllJap  288/290.
=== page marker
2223: 74
2248: 75
2280: 76
```


## [2026-09-06T15:27:23.325Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM جاده\"; grep -n \"جاد\" AFM_pages.txt | head -20"
}
```


### [2026-09-06T15:27:23.376Z] TOOL RESULT

```
=== AFM جاده
266:الذهب لانة يلحمة ٠‏ وبال له 28 « جادر اوشاغى »
812:* (السجادق "7 حجر احمر اللون. فاذا خرج من معدنه اصابتة ظلمة .
1167:ܨ ܩܐ انسل 1 ܝܢܐ ܐܢ 3 تصتع من جاده فراء فاخرة 9
2203:0:1 ستجاده واستبدعة ٠‏ فانعم عليه ووصلة بصلات مينة ܒ عله اما اعتييسة :
2363:وقد اجاد الشاعر في وصفها حسث قال :
2409:جادها 5 ومن وبرها ثاب يلبسونبها في الايام المارة فلا يوثر يم 9705 1
4262:١2 جادار‎
4271:يجاده ܙ
```


## [2026-09-06T15:27:25.187Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TTS jelek\"; grep -n -i \"jelek\\|jeläk\\|jilek\\|jelak\" TTS_vambery1878_uoft_djvu.txt | head -10; echo \"=== HRN jo/jav\"; grep -n \"Gerste\" HRN.txt HUB.txt | head -10"
}
```


### [2026-09-06T15:27:25.265Z] TOOL RESULT

```
=== TTS jelek
ugrep: warning: TTS_vambery1878_uoft_djvu.txt: No such file or directory
=== HRN jo/jav
HUB.txt:4941:'Gerstenbrot' = arm. Raskin; GurgTn N. pr. = arm. GurgSn^)
HUB.txt:5831:Auslautendes av wird au {ou) gesproclien : jan 'Gerste* (afgh.
HUB.txt:8490:kaskm Gerstenbrot* = arm. Ua^k^n (EliSe); laskar *Heer*
```


## [2026-09-06T15:27:31.472Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 5825,5840p HUB.txt; echo \"=== HRN jau\"; grep -n \"jau\\b\\|ja[uv] 'Gerste'\\|Gerste\" HRN.txt | head -10"
}
```


### [2026-09-06T15:27:31.544Z] TOOL RESULT

```
zlvajjlva 'Quecksilber H. 683; suvaw 'ich gehe' H. 778 ; buvam
'bin H. 233; sunavam 'hore* H. 795; farvar \Sommerhaus
H. 823; gav 'Rind' H. 888; guvalidan waehson* H. 939; nav
'Eanal, R5hre' H. 1024; nuvazdah neunzehn H. 1048, navad
neunzig'^) H. 1049; navardldan *zusammenwickeln' H. 1050;
havan *M5rser* H. 1089; yavar 'Stossel* H. 1125 u. s. w.
Auslautendes av wird au {ou) gesproclien : jan 'Gerste* (afgh.
jau) H. 428: nau neu' H. 1045; sau *geh*, ipt. zu savam;
seltener o: td = tu *du\ zd. tava. Ueber v zwischen Vokalen
siehe ferner Kap. 10.
Ebenso im Armenischen : Artavazd - zd. asavazdah-^
gr. ^Agxaovoi^dric^ lat. Artavazdes; Xosrov = pers. Xusrav,
r
paz. xusraVj zd. husravah-; Savars = zd. sydvarsan-, np.
Siyacas, Siydvus, u. s. w.
Nach k^ = iran. s ist idg. v schon im Iranischen zu
=== HRN jau
3979:knrd, je, jau, yö (H.-Sch.); oss. yau, yäu, yeu *Hirse'
3980:(147); bei. /ö, jav, n. jau 'Gei-ste' (179); si/n. yavoj,
17671:Iii^jau-, Sdyate 646.
```


## [2026-09-06T15:27:32.049Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==48' AFM_pages.txt | head -40"
}
```


### [2026-09-06T15:27:33.765Z] TOOL RESULT

```
ري لد
3 ذات 9 × 90[ 5 1503
دار اي حافظ
( حدر ناندع 1" مر القلم على ما درس منة ܝܠܝܟ ْ ٠ماخوذ‏ من حندره ومعناها
ܝܬܐܕ الماش
(الجتاغ » فشر بضرب من ܓ قلت فارسيّتَهُ مجناغ ثوب مرضع
منقّش يِلتَى على السرج لازينة ١٠و‏ من المحتمل الَّهُ معرب عن 39
القدح والقصعة
( الجَنك) من آلات الطرب تعريب جنك
(الغنان) تعريب جنار وهو الدلل ٠‏ والصنار لغة فيه ٠‏ ومنة الكردى
رحنار
ܨ 0 1 نيدن لفظا ومعنى
+( 6 رد رحا قتا رمن الكل : نامك 1055 0 150
الخجل :3 ܚܨ
ولي 3 الناقد العارفه ميج احمذ 0:0 0 3
ا وى وحار تا ؛ الت في ܥܐ ويطكق على النساك وعلى الناقد والعارف
والدلّال
0:0000 1 معرب ܫܩ اي قطعة من الل وهو يطلق
بافارسية على حصان قوي عظي |
(الجَهبلة » المرأة القبيحة تمري ب ܐܢ اي الأحق الثقيل
( الجهاركاه ) اللحن الرابع من ܐܝܠܐ الموسيقى ܐܚܠܬ جهاركاه واصل معناه
الباب الرابع
( الجهارة ) . حسن |( والن تعر يب جهره ومعئاه ما الانسان وطاعتة ووجهة
وسحتة رومنة الحهزة بالار كة وانكرد ية ٠‏ واطن أن حير كد أ زمه ا `
ܢܟܐ
* ( الجهوّري» المرتفع العالي معرب عن جاهوار ومعناه ذو القدر وامازلة
(الجَوتمر) الأصل وكل 39 3 39 73 اغة فيه
```


## [2026-09-06T15:27:44.829Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\nfor i,p in enumerate(pages):\n    for w in ['الجادة','جادة','الجاده','جاده']:\n        if w in p:\n            print('leaf',i,'printed~',i-8,w)\nEOF\necho \"=== leaves 44-47 first lines\"; for L in 44 45 46; do echo \"-- leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' AFM_pages.txt | head -12; done"
}
```


### [2026-09-06T15:27:46.722Z] TOOL RESULT

```
npages 198
leaf 46 printed~ 38 جاده
leaf 87 printed~ 79 جاده
leaf 95 printed~ 87 جاده
leaf 165 printed~ 157 جاده
=== leaves 44-47 first lines
-- leaf 44
ܣ
× (الجلغل ) تعيب كل وه العرش ܐܒ 6 ܚܨܐ
“د (الجَلّخ ) 7930 بها السكين ܕܧܕܩܐ تعريب 5 آلة 123 ݂ܟ
حجر اأرحى
* ( الجْلندى والعْلندّد ) الفاجر معرب كلنده
+ ( 5 الأرض 038 تعريب 39 الى 0 03 6
( 5 القطعة من الارض الغليظة 007 5 ܐܟܐ 8( وابللون)
الغليظ الشديد
9 فير بالبندق 0 ابن سينا في القانون هو حب الصنوبر الجكار
مجع لان اموز معرب عن ܐܰܘ وهو حب الصنوبر الكبار
59 333 الغليل) و 1 اي ورد
ومن ستّان اي حل
-- leaf 45
اشر ا
الوجود في ܐܬܬܬ وجلدها ܐܢܐܟ منقّط والنقاشون يتاضون ܐܛܝܐ عن الثلم ( الإرهان
ܗ ظ
* (الجاهة ) الصخرة العظيمة المستديرة تعريب كله
+( الخن) 3060 تقولا كاماد اي شخصة تعريب تجو ܕܬܐ ܐܶܢ
( الجَيْجم ) معرب جمجم وهو ضرب من الأحذية يله فتراء بلاد فارس
( 3 الذي يمل :3 امام الملك حين يلس ثيابة مركب من جام اي
مرآة ومن دار اي حامل
* :5 5 ` معرب تجمّار أي شحم النخلة وهو مادّة بيضاء لسَة
لذيذة الطعم كالطليب التجتد تكون في رأس النخلة ويقال لها بالتركبة حزما
ني
امون ») معرث كارمدئ ومنة الا ران ليككة عد 4 ١‏ ` ܥ
-- leaf 46
ܝܚܘ 5 ܝܚ
( الَامَكيّة والجَوْمَك) رواتب خدام الدولة. 1 9 مودق مق
1 ` وهو آداة النسة
( )0 هنوات كالاؤاو من فضَّة وفي ܐܠܩܰܒ݂ܳܐ هو عن مم الفحة
6 على شكل ܐܕܕ مأخوذ ما عن الفارسي حجان ومعناهُ المرج والمخضرة
والحندنة ويطلق 50 على كن شي ٠‏ 17 ܚ ( راجع 08003
اوعء ن < 24 20
19ل ܓ ) 2 إن مسكر فقيل بيذ العنب 1
ل ل العترةا ܒ ا ܡ 3 0 29775
® وهو الشراب العثيق وهو 2 2 جم اي ظاهر ماه ومن : هور اي ضوء
7 × الياء ع فعمي للنسمة ٠‏ ܀ -- وعندي 5 :41 نفسة ععنى اللماعة ܨ الناس
ومعظم كل سيء ܕܨ ܠ[ 3 × ܐܐܟܘ اليم ومعناه اللياعة
```


## [2026-09-06T15:27:50.990Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==47' AFM_pages.txt | grep -n \"جاده\" ; echo \"--- full leaf 46\"; awk 'BEGIN{RS=\"\\f\"} NR==47' AFM_pages.txt | sed -n 10,40p"
}
```


### [2026-09-06T15:27:52.601Z] TOOL RESULT

```
26:ܨ ܩܐ انسل 1 ܝܢܐ ܐܢ 3 تصتع من جاده فراء فاخرة 9
--- full leaf 46
® وهو الشراب العثيق وهو 2 2 جم اي ظاهر ماه ومن : هور اي ضوء
7 × الياء ع فعمي للنسمة ٠‏ ܀ -- وعندي 5 :41 نفسة ععنى اللماعة ܨ الناس
ومعظم كل سيء ܕܨ ܠ[ 3 × ܐܐܟܘ اليم ومعناه اللياعة
* (الجمثورة 3 المجموع تعريب © الهري
الصنوع من التراب
1 ( ܐܚܝ 0 الضخم والطويل وااعالي تعريب 35 الذي ° ٠١‏ والجنادف
ܢ 3 ܙ :ܐ ܕ أب والتنفج ان وي وغيرها» كلها لغمات فيه
وكلها ܚܨܢ الضخم والسمسين سمين ܐܥܛܢ ٠‏ عن جنبه معرب ايضأ (الغنبقة ) اي 31
الستّئة الخاق ٠‏ والمنفس واللفنس لفتان فيها
ܝܘ كاه ومعناه الاثم وقالوا فيه جنحة اي 6 اليه اما ٠‏ <
ايضأ معربة ( التَاية) يعنى الذف وان 1 راق ما 92105 ع ܐܝܐ ܝ في
الاصل )11 3 من الشجر ثم قلت الى إحداث الشر ثم الى الشر ثم 30
حرم ( حيط الحيط )
5 ܝܐ والجند ܢܡܡ ) خصية حيوان البحر له قشر ܘ بادلى
مس وهو كلل النفخ ويطرد الرياح ٠وقيل‏ هو خصي حيوان بري يقال له كل الاء ٠‏
050 ܝ 096 :4 3 ܨ ܡ وهو كلب المساء
ܨ ܩܐ انسل 1 ܝܢܐ ܐܢ 3 تصتع من جاده فراء فاخرة 9
3:1
```


## [2026-09-06T15:28:00.494Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(38,50):\n    heads=re.findall(r'\\(\\s*(ال[؀-ۿ]{2,10})', pages[i])\n    print(i, heads[:12])\nEOF"
}
```


### [2026-09-06T15:28:02.455Z] TOOL RESULT

```
38 ['التَوْدَلةَ']
39 ['الخثر', 'المحنبار', 'الجل', 'الحم']
40 ['اللودّر', 'الثيء', 'الحرداب']
41 ['الرعبيل']
42 ['البرهان', 'الجيرون', 'الجراهية', 'الجَروهق', 'الجزير', 'اللاساء']
43 ['الخش', 'الكّسة', 'اليترى']
44 ['الجلغل', 'الجَلّخ', 'الجْلندى', 'الجلقّق', 'الخل', 'الجلاهق', 'الهم']
45 ['الإرهان', 'الجاهة', 'الخن', 'الجَيْجم', 'الجَمَسَفْرم', 'الجَبّشُ']
46 ['الَامَكيّة', 'الجمثورة', 'الغنبقة', 'التَاية']
47 ['الجتاغ', 'الجَنك', 'الغنان', 'الجَهبلة', 'الجهاركاه', 'الجهارة', 'الجهوّري', 'الجَوتمر']
48 ['الجهرمية', 'الججهاّة', 'الجهسار', 'الجُوحّة', 'الجوْحَان']
49 ['الجودياء', 'الجوار', 'الجَوَرَب', 'الأورس', 'الجوز', 'الجورّة', 'الجَوْذَ', 'التاج']
```


## [2026-09-06T15:28:08.775Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(33,40):\n    print('== leaf',i)\n    print(pages[i][:1200])\nEOF"
}
```


### [2026-09-06T15:28:10.577Z] TOOL RESULT

```
== leaf 33
- 7
» ( البيت ) القوت مشتق من ناد ومعناه المال والرزق
* (السجادق "7 حجر احمر اللون. فاذا خرج من معدنه اصابتة ظلمة .
فاذا قطعة الصانع خرج نوره وحسنة تعر يب ببحّاده وفيه اقوال: فقيل هو الكهرباء .
ܝܐ حجر دفيق ܪ أحمر اللون كالماقوت 4 ܫܐ ܪܝܬ كاتكهر باء ٠وقال‏ بعضهم هو المرحان
رد وقال غيدهم ضرب من الجواهر ( البيهان ܘ
* < السند ) الردي معرب إما عن :بد الذى عمناه او خن؟ تدا ويساة بلا قات ذه
وابلد معق
( السادة » من العسكر المشاة وعكسه 50( 05 اي الراجل 27
ܝ
راجلا
+ ( السدر) الموضع الدى ܐ شه داليم لقم 2 ܐܩܪܝ ومعناه
الرجل 3 5 .و تسل ان يكون معرباً عن السر £ ° خبط ܐܕܪܐ
(فرنكل ص:5١1١)‏
* (السَدَرِي) اللغة 5 المستوية تعريب به 7 £ معناه اليد
المسن ودَرِى هو القسم الأأفصيح من اللمة الفارسية قال في البرهان القاطع :دري
على وزن ܨܩ قسم من ` والماء 1 378 .وفي هذا !ܠ ܩܐ )ܪ̈ܝ
وهذه النسمة اقوال : )341 سم درى إيطلق على اللعة .ܬ ܝ اي على
اللغة غير الناقصة الوضع مثل « اشكم وبكو وبشنو» فان « شكم وكر وشدر» لا
3 " يطآق على لغة أهالي بلخ ܙ و بدخدان ومرو التي هي هي
من - العجم٠‏ ” ان اللغة 00 اهل 3 ٠فان‏ هؤلاء يتَكلّمون باللغة
العر بّة التى هي أفصح اللغات وباللغة الدرية ® هو مسطور ` ¥ قال
عبد القادر البغدادي :« لسان اهل 5 العر 3 والفارسيّة الدرية ».وقد رُوِي 5
انْ لسان الملاتكة 5 الرابعة هو الفارسى الدّري ٠‏ وقيل 6
== leaf 34
سس ܕܢ -
و( المَيرَقدَار) 0 من برق ومن دار اي حامل النيرق
+ (البيش) ܝ رطا ويايساً ورم نبت فيه سم قاتل لكل
حموان ܝ 9 00 21 اللغة الفارسيّة باصول نمات ` ܣ
وهو سم قائل 10 له ܗܗ يلدرجين 5 ( 5 ) 3( 033 ܒ
0 0 معناه فارة السسش وهو حيوان يشبه الفارة يسكن في اصل !+ ٠‏ وفي
المثل : اعجب من .فازة الميش تتخدّى السموم وتعش
( السيك) 5 الات المناء ذو 2-6 0 تدحت به ¬ ܨ ييك
® ( نيط المحيط ) . ! في لم !( هذه بار ذلعلها تصحيف اليونالي
676
ܝܚܘ مركب من بيار اي مر يض ومن ستان اي حل ويقال له بالتركة
خسثه خا نه
003 ضرب هن 13 ܀ تعر يب 8 ومعناها 0 والقدة واأسير
ܨ المذاء وتق رما اليونامة .07(
+ (الئّة) الحالة الشديدة  .‏ ( !ܪ ) النقص والخسار والهلاك .و١‏ تن ˆ
تنا ) هلك : ܨ أن «يكون كل” ذلك 07 من ثاب ومعناه الغضس والفساد
)1 اومن 15 ܠ الفاسد ادي
1 الطعام تعريب ܢܐ الذي عناه
0 النحاس 7 ما أساقط منة عند الطرق تعريب ܨܠ
16 3 0 ܚܝܨ | ܙܐܢ صغير معرب‎ 36 ١
( > والتبوذك ) الذي يدع ما في بطون الدجاج كالقاب والقانصة ܐܚܨ
( محبط الحيط ) ْ 0101 هذه اللفظة في كتى الاغة الفارسية . أفها تكون تصحيف
ܝ
== leaf 35
7 اي قائصة الطيور
( التآجة ) الصماحة .2 الفضّة واصلة تازه بالفارسة الدرهم المضروب حديثا
(التجات 6 ما 1 577 9 7 77 0 0
ܕܘܫܐܘ ماء الفضة
(الشَغِئّاف ) مغرب تَْتمَاه الي خارس 5037
( ܐܶܝ فارسي حض فاصل معناه 0 وهو نت £ ܐ
والكردنة ܪ 039(0 01 مرا تطح نزخ ضحت ومن روان ومعناه الذهاب ܙ !)ܨ ٠‏
والتتخت رهان ` 03 عن السّماء 37 نعش £ 3:5331 ܠ
وهو اش والاوح
݂+ )0( ܡܝ ܐܗ وهو عصارة السسم والعجين ܐܝܒܨ
( التخْرص : شقة الثثوب تعر دب < ٠‏ والتخرصة والتخر ܢܟܨ والتخر بصحة
والدخرص لغات فيه
( التدرج ܕܨ( طائر حسَن الصوزة “أرق نكرن بأرض كزاضات وسار
وغيرهه| 3 ܘ ¥ انه افضل 0 وقدل هو الحجل وقيل )ܠ ܥܨ
عن تدرو وهو 6 سوكاون
( النودّري) حب ورقه ܒܝ بورق الفراسيون مر بع المذر وجذره قدر نصف
ذراع معرب تودرى
05 00 ܠ 27 00 ܪܡ 000 ܐܝܐ ودقيقة 1
وهو من مننولات البلتم ويعرف بعشب الجبل .£
( لتر امان) نات يعرف بالغافت مركت من نره .ܬ اي عشب ومن ܠܘܝ ܐ !ܒܢ
سطوح ٠‏ زهره لازوردي الاون ورقة طويل ساقة واوراقة مرة ويقال له بالتركية قويون
9 ش
1 ܝ والا 17 ,879 ܕܐ ܐܒ ܢ‎ ١
ܙ ܐܛܪܘܓܐ ونه الاي ܝ‎
ا < 38 9 97 0570( 985
ܠܠ |
يها
== leaf 36
+ 0 ܨ 92 من ®( اي ܐܝܘܟ وهو ارضا ¦ ܨ0 ش بالتركة
والكردنة
( الترؤاس ) ضرب :ه ن الكمء فارسيتها 5 وبرادفة اللاا 3 011
ܐܐܐܝ والانتكايزي 11106 ܚܣ تع طن
الي 0 نات له جب هفرط ܨ عزز له نقّرة في الوسط مر ٠‏ الطععم
13 بعد المعالمة بالنقع في الماء 3" وترمش لغة فيه . لك الكلمة
:® 066 ويقال له ® 1:11111
+ لحان ) نات ساقه مسكايممة مر 00 4 مفرعة طو لها قدمان ا رن
673 وقال في البرهان القاطع 1 , 22 05 اللزيين بالعر 2 واوغل :1( ܝ
اولى بالتركة
(التزيفين ) ا" اكثر ما يسقط مجخراسان وما وراء الثهر ܓ وقوعه على الاح
ܕܫ كالن وأحوده الابيض : تعر يب 9 .قال ܒ البرهان ܕ ( (ترتكمين)
15 امن ابيط مثل الطلن على اسك وهو حاو ويقال له بالعربّة £ وبالتركّة
بال ܕ منة أيلغين بالى ٠‏ | معرب عنة ܨ م اسان
يطلقون | سم ܠ على 5 3 2 :4 أبيض ولسمسه العرب ܟܚ( وهو معرب
3 0 سقط على العاقول 1 .0( ܝܨ[ أ
3 3 .© ار مثل اللبن الابيض الصو ܟ ܨ( 4 :ننه درت إلى
ضرة واصله من ولاءة هرات في حراس ان بشع عة عل سجر الخلاف ٠‏ بدعونهة
0 ܥ وهو 30536 ونسميه العامة شيرخشت ٠‏ و يقول له
الأتراك > زلى وادغلان اشي 0 ٠‏ وطلتجبين $ في ܩ
19 ]0 ܨ المهزول 6 .< حداء ومن 0390 عسد.
والعامة ة تقول © وذلك ܢ
( ܬ ) الطريق | ألصغارة النشعية 7 خ لادج والباطل والتخليط يه ܝ
و( ره الرجل وقع في استرهات . ان )انا لماطل : كل ذلك 2 من راه اى
الطريق “قال الأصبعي ܐ« ܬܐܝ الطرق ا
== leaf 37
3 ا
الصحاصح وهي من )1104 )ܟܐ ¢
1 9 ) آذام وا استيخف ه مثتق :0 ومعناه الزن والاضطاراب
ܝܫܐ( والطنجير) الا جانة تعيب تغار ومن التري تغار
+ م معروف ܣ 5 الذى )ܘ وهر في لغة الفرس القدعة
+ ( 5 6 5 ܐܥ !ܙ والغضب وهو
ܪ هن 00 اي احترق وغضب وهو ܨ[ 000 ܒܚ ܕ 1@[(60 207
0 ( التفسيا ) صلغ السذاب 00 3 ܗ 3 بصمغ السداب
الحبلي الذى قال 4 بالتركة درياس وهو ܝܨ ܠܢ ܐܫܡ ܕܢܠ 35 3 ذو 25
0 فقيل هو .ܟ السذاب البرى ١‏ البرهان 59 `
0:0066
027 الى ء يي ܦ . ܕ ((() 4 ) في !ܠ ܩܚܝ̄ ان لا يكون لها ܟܝܢ ٠‏
و( انه ) كا ل ذلك مشتق من ܝ اناه ومعناة العاطل الردى ]0
(التلّسَة ) هنّة تسوى ٠‏ الوص وكدس اللساب ٠قيا‏ قيل فارسي الأصل فاعآة
0 تلوس وهر 338 او 50 لي اي حنظة 7 ® ٠واما‏ دل
( ܟ :¥ \ ) فيةول اله تعريب ܐܝܒܨ ا ܨ الأصح ل 13
1( 5 الذي 5 مشتق من 0 اي 5 ومنة الترى . تلسه
3 ܢ
( 5 تعريب تركش وهو <
* ܠ والتَّلونَ واللّونة ;3 3 0
+ ( || امون ) ضرب من البقطين ارد ديدتق في الشجر طعم ورقه
ار 0 من 1 ܘܐ 0
( الثنبور) القصير القامة ٠و١‏ التذّل $ والتذالة 6( والتأتل < |
05 القصير .و التذالة » القصر 6:7 اتكسلان بلغة العامة ١كل‏ ذلك
معرب عن ܢܠ وهو تصحيف تن بروّر ܙܚܐܘ الرلي ܥ .ܪ ويقال اتكيلان الايد
السمين الغير القادر ان يتحرك من مكانه
* (التتكار) ضرب من اللح 5 منة معدفي ومنة مصنوع ٠‏ فارستة
== leaf 38
3
ܢ ܟ | فى البيهان القاطع 3 ىبا 36 63 المورق وهو
يتكون مثل اليد في بعض الينابيع اكات 1:06 ملح الصناعة وهو مركب
من اللح والتلى »
: ور من ܗ ما يحرط بالخدم » 79 الموالقة من ١‏ فارم كه در
وفسّرت بضرب من 130 ن انواع الزرد.وهى في ± ܝܒܒ
اللتوع الواستة و كر م1 (0 مره وريم اى اللانس خلد | ܟܐ بأ
+ 03536 لة والتولة) الذاهية. المتكرة . و( التَوْدَلةَ والتوزلاء ) الداهة:
5 ذلك مأخوذ :3 1 ا التراع والثثال والفعل هو : ܕ ܥܝ 0 139
5
1.70 قريبان لفظأ ومعنى من 00
المسم والقدرة
»+ ( تري) الملل 00 10500 و :119 ܐܐܠ الضائع
( ܐ« ) فاسي 6 وهو 7 المعترضة بين الحا نطين
.ܘܣ ܣ التدل واطوالق وانكيتن
ܐܥܝ 08 الفلاة ܐ ܨܝ ܣ 7 : 0 او اليونالي »× 00
1
ܒ̄ ܒܗ ¢ ܘ 2م جم
00
60 ` 0 9 ` 5:5 9(
05 الغلرظ
ا 06 ܝܬܠ سحو من بان واصق شن
هنا وهناك ماء
== leaf 39
راع
+ ( )ܥ ) عريب ند وهو زهر الرمآن والورد < 0 ايضا على
| ® “ذفني 8 0 6 0 عب القية
0 1 0 فارسلتة جو ܢ( وهو مركت من جوى
اي سيل دمن بار دهي من الأدوات | 3 تدل على الكثرة
+ ( أ مجار) بات ܦܟ سديه بورق الرطبة عليه زغب لطيف كالغبار وله
أغصان دقيقة مائة الى الحيرة وزهر احمر واصل خشبي غائر في الارض تعر يب
انكر
* ( اد ) الغليظ والبخيل «اللثيم 89 الخليظ الشخين . وعة
مغرب ايضاً ١١ل‏ س2 بمنى ܝ ܒ > المافي انس واخفس اليس
غات فبه رك الس ܐ 07 99 عن اليونالي. 4 ومنه 5 ܣܨ
فالس @ 3 5 ا للعة الريامة !ܐܬܟ 9 ܨ والأسارسي
جسين ماخوذ من ܐܝܟ يالى .ܕܘܐ الخص فعرب عن :3 ¢ الاراعى
ܓܨܐ ܦܟ 100 ܘܒ فيه ܡܝ قصّص ܫܩܢ (طالع 1
ص : \-- ›  \‏ وهو 0 حص € ¬ 79
` الجل القصيد < ب كهتر وهو ܐ م 6 أي صخيد ومن ثر وي
أداة التفضيل ٠‏ وكثر الابدال والتصحيف في هذه الكلمة حق صار فيها لغات عديدة.
ܐܝ ذلك قوم شها 1 )ܨ : .ܙ ܕܠ ܨ وا للعظ_ار
ܙ ܐܝܐܝ واللعير والمعبرى || يخ (طالع الشرق * 7
(الخثر) ܢܬܐ والش.سية ܚܠܨܐ ܡ ومنها ܫܬܪ بالسريانّة
* ܣ الملاء ܡ ترب يديس مب ابعر | `
له ܘ قطاع الطريق
# ( حثا ححثو ) .ܗ حا ܩܡ 5( 0 وهو £ المونانة 01/0١‏
* (المحنبار 1 ܐܐ( الجل = والعظيم !+ ܙ العظي
ܐܝ ` ܢܝ 7 ܬ ܬ ܨ ل ويطلق 2 خصوصي على ܐܝܚ ܐ
واصان وهو 20 13 اي جمل ومن ܨ بكار اي جِنّة
* ( الحم » الضيّق الخلق 6 ال
```


## [2026-09-06T15:28:24.551Z] TOOL CALL #60: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:28:24.558Z] TOOL RESULT

```


```


## [2026-09-06T15:28:28.604Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A7%D8%AF%D9%87",
 "prompt": "Give the full Persian entry: etymology of جاده (road), and any Arabic section for جادة. Quote exactly."
}
```


## [2026-09-06T15:28:28.942Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A7%D8%AF%D8%A9",
 "prompt": "Give the Arabic entry for جادة: etymology, root, meaning. Quote exactly."
}
```


### [2026-09-06T15:28:32.793Z] TOOL RESULT

```
# Persian Entry: جاده

**Etymology:**
The word جاده is "Borrowed from Arabic جَادَّة (jādda)."

**Definition:**
In Persian, جاده means "road (between towns or areas); thoroughfare."

**Note on Arabic Section:**
The web page does not contain a separate Arabic section for جادة. It only references the Arabic etymon جَادَّة (jādda) within the Persian entry's etymology section.
```


### [2026-09-06T15:28:34.911Z] TOOL RESULT

```
# Arabic Entry: جادة

**Root:** ج د د (j d d)

**Meaning:** The word جَادَّة (jādda) is defined as "avenue, boulevard."

**Etymology:** The entry derives from the Semitic root ج د د, which contains 17 related Arabic terms according to the Wiktionary classification system.

**Key Details:**
- Part of speech: Feminine noun
- Pronunciation: /d͡ʒaːd.da/
- Plural forms: جَادَّات (jāddāt) or جَوَادّ (jawādd)
- Grammatical classification: Triptote singular in -a

The word also functions as a feminine singular adjective form related to جَادّ (jādd), and it has descended into Persian as جاده (jâdde).
```


## [2026-09-06T15:28:40.675Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%88#Persian",
 "prompt": "Persian entry جو (jow) 'barley': give the etymology chain (Middle Persian, Proto-Iranian, PIE) exactly as written."
}
```


## [2026-09-06T15:28:41.216Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewos",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Indo-Iranian, Greek, Baltic) exactly."
}
```


### [2026-09-06T15:28:44.142Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:28:45.436Z] TOOL RESULT

```
# Etymology Chain for Persian جو (jow) 'barley'

Based on the Wiktionary entry, the etymological progression is:

**Middle Persian** → **Old Persian** → **Proto-Iranian** → **Proto-Indo-Iranian** → **Proto-Indo-European**

Specifically, the entry states: "From Middle Persian [script needed] (jaw), from Old Persian *yáwaʰ, from Proto-Iranian *yáwah, from Proto-Indo-Iranian *yáwas, from Proto-Indo-European *yéwos ('barley, cereal')."

The chain traces the word through these successive language stages, with the original PIE root *yéwos meaning "barley, cereal."
```


## [2026-09-06T15:28:49.047Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/y%C3%A9wos",
 "prompt": "Give the reconstruction, meaning, and descendants (Indo-Iranian, Hellenic/Greek, Baltic, Celtic) exactly."
}
```


## [2026-09-06T15:28:49.689Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/yelek",
 "prompt": "Turkish entry yelek: meaning and etymology. Also any note about descendants (Arabic, Spanish, French)."
}
```


### [2026-09-06T15:28:54.780Z] TOOL RESULT

```
# Proto-Indo-European *yéwos

**Reconstruction:** *yéwos (n, non-ablauting)

**Meaning:** "cereal, grain" or more specifically "barley, spelt"

**Key Descendants:**

- **Indo-Iranian:** Proto-Indo-Iranian *yáwas
- **Hellenic/Greek:** Ancient Greek ζειά (zeiá, "spelt") via Proto-Hellenic *dzeyyā́
- **Baltic:** Lithuanian jãvas; Latvian java
- **Celtic:** Proto-Celtic *yewos ("barley, spelt"), leading to Middle Irish eórna, Irish eorna, Scottish Gaelic eòrna

The term derives from the root *yew- or *yewh₁- meaning "to ripen, mature."
```


### [2026-09-06T15:28:56.475Z] TOOL RESULT

```
# Yelek: Turkish Definition and Etymology

## Meaning
In Turkish, **yelek** refers to a "waistcoat" or "vest" — a sleeveless garment worn over other clothing.

## Etymology
The word traces back through Ottoman Turkish to Old Anatolian Turkish *yélek*, ultimately deriving from the Proto-Turkic root *yẹl* meaning "wind." The suffix *-ek* serves as a noun-forming element in Turkish.

## Descendants
This garment term spread across multiple languages through Italian intermediaries:

- **Spanish**: *chaleco* (and Galician variants)
- **French**: *gilet* (which further influenced Dutch and English)
- **Portuguese**: *jaleco*
- **Arabic**: Algerian Arabic adopted the term via Italian

The widespread adoption reflects the historical importance of this Ottoman-era clothing item in Mediterranean trade and cultural exchange.
```


## [2026-09-06T15:29:01.291Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gilet",
 "prompt": "French entry gilet and English entry gilet: give the etymology exactly (Spanish/Arabic/Turkish chain)."
}
```


## [2026-09-06T15:29:02.502Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%84%DB%8C%D9%82%D9%87",
 "prompt": "Persian entry جلیقه: meaning and etymology. Quote exactly. Also note any variant جلیتقه."
}
```


### [2026-09-06T15:29:07.501Z] TOOL RESULT

```
# Etymology of "Gilet"

## French Entry
The French word derives from regional Italian variants (Calabrian *gileccu*, Genoese *gilecco*, Neapolitan *gelecco*, Sicilian *ggileccu*), which come from Turkish *yelek* meaning "jelick; vest, waistcoat." The Turkish term ultimately traces to Proto-Turkic *yẹl* ("wind").

## English Entry
English borrowed the word directly from French *gilet*, which itself originated through the same pathway: regional Italian forms → Turkish *yelek* → Proto-Turkic *yẹl*.

## Complete Chain
**Proto-Turkic *yẹl* (wind) → Turkish *yelek* → Regional Italian dialects → French *gilet* → English *gilet***

Note: The Oxford English Dictionary does not support derivation from Arabic *jalīqa*, viewing any Arabic connection as recent borrowing from Italian into Algerian Arabic rather than the reverse.
```


### [2026-09-06T15:29:08.665Z] TOOL RESULT

```
# Persian Entry: جلیقه

**Meaning:** The word جلیقه (jeliqe) denotes "a sleeveless garment worn over other clothing," specifically what English speakers call a waistcoat or vest.

**Etymology:** This term was borrowed from Arabic جَلِيقَة (jalīqa), which itself derives from Turkish yelek ("waistcoat"). The Arabic form's structure was "modeled after" French loanwords like corset and mantelet. Cognates appear in Greek γιλέκο (giléko) and Spanish chaleco.

**Variant:** An archaic alternative form is جلیتقه (jelitqe), with dialectal variants جلیدقه (jelidqe) and جلزقه (jelezqe) also documented.
```


## [2026-09-06T15:29:26.807Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== DEV gilet\"; grep -n -i \"gilet\" DEV.txt PHN.txt LAM.txt 2>/dev/null | head -10; echo \"=== SKT/FSD/WEB zea\"; grep -n -i \"^Zea\\|Zea,\" SKT.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head -5; echo \"=== FSD/WEB gilet\"; grep -n -i \"gilet\" FSD_vol2.txt WEB_vol1.txt 2>/dev/null | head -5"
}
```


### [2026-09-06T15:29:26.909Z] TOOL RESULT

```
=== DEV gilet
PHN.txt:5324:GILET, s. m. (a.)
PHN.txt:5326:confectionner des vêtements. — Le gilet est une sorte de cami-
PHN.txt:10547:Gilet, s. m. (a.)
=== SKT/FSD/WEB zea
FSD_vol4.txt:5366:Zealand]  (1)  A   scorpaenold  fish  {Sehastaplstes  cottotde<!)  SCatcU  <lignt  ,   I   sur^i  -Imt  ,   2   serch  -Ut ,   n   1   A   power-
FSD_vol4.txt:18459:Zealand  — Splic"no-don'tl,  n   pl  The  lihynchoeepnalia
FSD_vol4.txt:26637:Zealand!  SamensPUKEKO  Sunda  group.  Malay  Archipelago.  6,3G2  sq  m   devastated
FSD_vol4.txt:45003:tm-res'pit»ed,o  1.  Not  delayed  or  postponed,  not  res-  rendered  mentally  subjective  un-spe  cial-izea,  a   Not  speciaU/ed,  especially,  in
FSD_vol4.txt:55783:Zealand  smelt  *   A   gobioid  (Lcpicopobius  icptdus)  the  letters  stand  out  In  the  color  of  the  paper,  whereas  the
=== FSD/WEB gilet
WEB_vol1.txt:81764:Ja gilet’ (zhē-lā’), n. [Fr., a aber naa a waist- coat or vest; especially, the front of a bodice
```


## [2026-09-06T15:29:27.967Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%98%DB%8C%D9%84%D9%87",
 "prompt": "Persian entry ژیله (and any mention of ژیلت): meaning and etymology."
}
```


### [2026-09-06T15:29:29.986Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T15:29:34.272Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 5316,5345p PHN.txt; echo \"=== page\"; awk 'NR<5330 && /^\\s*[0-9]{2,3}\\s*$/ {print NR\": \"$0}' PHN.txt | tail -2"
}
```


### [2026-09-06T15:29:36.003Z] TOOL RESULT

```
même nom et qui appartient aux Anglais depuis 170/i, époque
à laquelle ils se sont emparés de ses fortifications par surpriseGIR 181
et sont devenus, par le fait, seuls mattres du détroit. — On
prétend que Gibraltar doit son nom au général sarrasin Tarik
ben Ziad, qui prit possession de cette montagne, l'an 710 de
notre ère, sous le règne de Walid, fils d'Abd elmalek, sixième
khalife Omayyade, pendant que ftfousâ ben Nasir faisait la con-
quête de la Sardaigne.
GILET, s. m. (a.)
ùds^ [djild et djtlid] peau, cuir d'un animal, dont on se sert pour
confectionner des vêtements. — Le gilet est une sorte de cami-
sole de laine ou de coton que l'on porte habituellement soit
par-dessous, soit par-dessus la chemise. Dans certaines con-
trées, on en fait encore aujourd'hui avec des peaux de bétes;
et cet usage remonte sans doute aux premiers temps du monde,
car il est question, dans l'Écriture sainte, de peaux de bétes
dont Adam et Eve durent couvrir leur nudité, lorsque Dieu les
chassa du paradis terrestre. — L'analogie d'orthographe et
de signification que présente le mot français gikt avec son cor-
respondant arabe djilid me porte à croire qu'il vient do ce dei^
nier, et je n'ai trouvé dans les dictionnaires aucun renseigne-
ment qui puisse contredire cette hypothèse.
GIRAFE, s. f. (a.)
Ailjy [zcrr^t], dérivé de cjjj [zeref\ marcher avec rapidité. Les
Arabes ont sans doute appelé ainsi la girafe, à cause de sa lé-
gèreté et de la vitesse de sa marche. Semblable au chameau
sous plusieurs rapports, cet animal a la tête petite, surmontée
de cornes velues, et les jambes de devant plus hautes que celles182 GOD
de derrière; sa peau, tachetée de blanc sur un fondroussâtre,
lui a fait donner aussi le nom de caméléopard. On le croit ori-
=== page
661: 31
```


## [2026-09-06T15:29:46.071Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD yewo\"; grep -n -i \"yewo\\|zea\\b\\|zeia\" AHD_watkins1985.txt | head -10; echo \"=== AHD ya- root\"; grep -n -i \"^yā-\\|yā- To go\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-06T15:29:46.132Z] TOOL RESULT

```
=== AHD yewo
163:The Indo-Europeans practiced agriculture and the cultivation of cereals. We have sev- eral terms of Indo-European antiquity for grain: gre-no- (CORN), yewo-, and pdro-, which may have designated wheat or spelt. Others of more restricted distribution are wrughyo-, “rye,” and bhares-, “barley.” Two roots for grinding are attested, al-* and mele- (MEAL?, MILL). The latter is confined to the European branches of the family. Another European term is sé-', “to sow,” not found in Greek, Armenian, or Indo-Iranian. The verb “to plow” is are-, again a common European term, with the name of the plow, *ara-trom.
1200:yewo-. Grain. Suffixed form *yew-ya in Greek zeia, one-seeded wheat: ZEIN. [Pok. iewo- 512.]
=== AHD ya- root
```


## [2026-09-06T15:29:47.695Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA jadde\"; grep -n \"جاد\\|ǧādda\\|jādda\" incoming/PLA/PLA_pages.txt | head -10; echo \"=== IEC ia- go\"; grep -n \"^iā-\\|iā-, iāio\\|iaio\" IEC.txt | head -5"
}
```


### [2026-09-06T15:29:47.760Z] TOOL RESULT

```
=== PLA jadde
=== IEC ia- go
6041:ehiiaio (ghia-, £ha-, 2hi-) ‘gape, yawn’ (ono- matopoeic). WP I, 548 Per. fa-Zidan, cpd. id.; Gk. cf. kháos; Lat. hio, hiāre; OHG gen. beside MHG giegen ‘yawn; play the fool; OCS ziajọ, ziati beside z&ig, zéti; Cz. zen, záti; Li. Zióju, Zióti, id. beside žiojù, čti ‘snarl’
6044:Gk. khēlé “claw, notch, breakwater’; khelóo ‘split open’; MHG giel “open jaws’ beside Du. geul ‘gully, channel; Li. cf. Zioklë “open jaws, hob-hole, blowhole’ etc. Variant: ghiiom-, ghim- etc. Gk. khéme “yawn, gape'; MHG giem- in giem- olf ‘snarling wolf; G Giemen ‘chink’; Icel, gjamm ‘bark of dog’; Li. žiomuð, gs -eñs m. ‘jaws’. (Cf. also *&£hiien-, *&hin- in MHG ginen, gënen ‘yawn’; G gienen ‘burst open, gape’. See ghiiaio, etc. OE goma “open jaws’ is ambig. See gham-, as also for ON gómr ‘roof of mouth? < *gh-, or *gh- in view of Li. gomurjs, m. crater)
6318:iādh- (ià-) “go, ride". (Cf. iāt-, iaios, iðið). WP I, 104. See iāið for the simplex Swiss cf. jetten ("fling', fr. *iádh-?); Srb. cf. jadro ‘sail’; OCS jadü ‘going, riding"; jazü, jaza (canal, fr. *iádhio); Latv. -jāds (“sort', in tre-, tri-? ‘three kinds”, etc.); jadeleju “ride around’; Li. jódau, yti ‘ride — a horse’. (For Gk. &thos ‘custom’, see suëdh-)
6327:jaio, iami “go, ride’. Cf. iato-, iaios, iðið, ieks-. WP I, 104 Skt. yami; Av. yai(mi), id.; Hitt. iya- (queried to i-, see eimi?); Hes. záo 'futuere' beside záo, zémi, fut. zéso "live, flourish’, cf. also dí-zémi ‘seek out and déo “shall find" (synth. cpd.); cf. also op-ázo ‘follow’; op-aon (*follower', if fr. *soqu-^); Fris. joeije, v. “frisk; mate’; Li. jóju, jóti ‘ride a- horse"; Latv. om, jāt, id. (Hitt. iya- tari, impers. and depon. 'goes' is ambig. since initial i- gives Hitt. y- as in yukan ‘yoke’, cf. iugóm. Gk. eion, eg. impf. ‘I went? seems to belong here, though linked by suppletion with Gk. eimi. Gk. (Hom.) &ióeis, epithet of the Scamander river may belong here as also, more certainly, eia, ĉja journey food’ see next. For eios ‘bright’, epithet of Phoebus, see áu-, àu-mi) Skt. yáyub ‘horse’; Hom. eía, čja “provisions for a journey’; Lat. janua door, gate’; for -nua cf. neu- ‘turn’; Li. jojà ‘troop of horsemen, ride’; Latv. cf. jajejs ‘horseman’
6477:iðið (variant of iaio? q.v.) “live” Gk. zóð; Alb. (ambig.) ndér-zej, pp. -zyem ('breed', fr. Zenter"
```


## [2026-09-06T15:29:56.642Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la incoming/PLA/ && grep -c \"جاده\\|جادّ\" incoming/PLA/PLA_pages.txt; echo \"--- sample arabic presence\"; grep -c \"الجادة\\|جادة\" incoming/PLA/PLA_pages.txt; grep -n \"ǧ\" incoming/PLA/PLA_pages.txt | head -3"
}
```


### [2026-09-06T15:29:56.759Z] TOOL RESULT

```
total 6832
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  358695 Sep  4 14:06 PLA_asbaghi_1988_ia_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 5813714 Sep  4 14:06 PLA_asbaghi_1988_ia.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  807821 Sep  4 14:06 PLA_pages.txt
0
--- sample arabic presence
0
```


## [2026-09-06T15:29:59.615Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -60 incoming/PLA/PLA_pages.txt; echo \"...\"; grep -n \"gadda\\|ǧādda\\|jadda\\|Straße\" incoming/PLA/PLA_pages.txt | head -10"
}
```


### [2026-09-06T15:29:59.675Z] TOOL RESULT

```
             Asya Asbaghi


Persische Lehnwörter im Arabischen




    OTTO HARRASSOWITZ   - WIESBADEN
          Asya Asbaghi
Persische Lehnwörter im Arabischen
               Asya Asbaghi


Persische Lehnwörter ım Arabischen




                    1988


    OTTO   HARRASSOWITZ    - WIESBADEN
CIP-Titelaufnahme der Deutschen Bibliothek

Asbaghi, Asya:
Persische Lehnwörter im Arabischen / Asya Asbaghi. -
Wiesbaden : Harrassowitz, 1988
  ISBN 3-447-02757-6




Alle Rechte vorbehalten. © Otto Harrassowitz, Wiesbaden 1988. Photomechanische und photographi-
sche Wiedergabe nur mit ausdrücklicher Genehmigung des Verlages. Reproduktion, Druck und buchbin-
derische Verarbeitung: Hubert & Co., Göttingen. Printed in Germany.
Meinem   Lehrer,   Herrn   Prof.   Dr.   Macuch   zu   seinem   65.   Geburtstag.
Inhaltsverzeichnis


Verzeichnis   der   Abkürzungen     IX


Vorwort                           XIII


Einleitung


Wörterbuch


Literaturverzeichnis               275
Verzeichnis    der    Abkürzungen


a) Philologische       Abkürzungen


aaram.               altaramäisch          DB.               Darius    Bistun
...
137:’”insäb                  s. Mugaddasi Lv.            III   Brockelmann   Ss.   Lv.    II
270:       sarat "mar.                  sarät       "Straße"
10458:Io -            sirät:          "Straße"                  IP         po srät          7 s.        sirät,       hebr.   IVO%S-
15846:Mugaddasi,     abil-Fadl Muhammad ibn Tähir ibn “Ali: Kitäb al-’Insäb,
```


## [2026-09-06T15:30:08.858Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AC%D8%A7%D8%AF%D9%87/",
 "prompt": "Show the فرهنگ معین and لغت‌نامه دهخدا entries for جاده, including the origin tag (e.g. [ع.]) exactly as printed."
}
```


## [2026-09-06T15:30:10.568Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AF%E0%A4%BE%E0%A4%A4",
 "prompt": "Sanskrit यात (yāta): meanings and etymology (from यू/या 'to go'?). Quote exactly."
}
```


### [2026-09-06T15:30:12.870Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:30:16.596Z] TOOL RESULT

```
# فرهنگ معین Entry for جاده

**Origin tag:** [ع.] (اِ.)

**Definition:** "شاهراه ، راه بزرگ" (A highway or major road)

The entry also includes an idiomatic expression: "صاف کن" (clear/make smooth), which figuratively means facilitating others' progress or success.

---

# لغت‌نامه دهخدا Entry for جاده

**Origin tag:** [ع. اِ] (عربی - اِسلامی)

**Primary definitions:** "معظم طریق و وسط آن" (the middle/main part of a path), "راه راست" (a straight road), with plural form "جَوادّ"

Additional meanings include: "شاه راه" (major highway), "راه بزرگ" (large road), "گذر" (passage), and "معبر" (thoroughfare).

The entry notes that while the Arabic form uses doubled dāl (جادّة), Persian typically uses a single dāl, and includes classical poetry examples illustrating its usage.
```


## [2026-09-06T15:30:23.891Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://www.sanskritdictionary.com/?q=y%C4%81ta&iencoding=&lang=en",
 "prompt": "Give the Monier-Williams entry for yāta (यात): all meanings, especially any 'a going, motion, course, way, path'."
}
```


## [2026-09-06T15:30:24.648Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/y%C3%A1wah",
 "prompt": "Proto-Iranian *yáwah 'barley': give descendants (Avestan, Middle Persian, Persian, Sogdian, Khotanese) exactly."
}
```


### [2026-09-06T15:30:26.211Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:30:32.458Z] TOOL RESULT

```
# Proto-Iranian *yáwah Descendants

Based on the Wiktionary article, here are the documented descendants of Proto-Iranian *yáwah (meaning barley/grain):

**Avestan:** 𐬫𐬀𐬎𐬎𐬀 (yauua)

**Middle Persian:** Book Pahlavi script representation with the pronunciation /jaw/

**Persian:** جو (jow)

**Sogdian:** Represented in both Sogdian script (𐼷𐼴𐼷, ywy) and Manichaean script (𐫏𐫇𐫏, ywy), pronounced /yəwí/

**Khotanese:** The article does not include a documented Khotanese descendant, though it does list other Southeastern Iranian languages like Parachi (žō) and Shughni (ǰav).

The term traces back through Proto-Indo-Iranian *yáwas to Proto-Indo-European *yéwos, demonstrating its ancient etymological roots across multiple Iranian language branches.
```


## [2026-09-06T15:30:38.618Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD jaw\"; grep -n \"jaw \\|jaw'\\|ywd\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB jaw\"; grep -n \"jaw\\b\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-06T15:30:38.689Z] TOOL RESULT

```
=== PHD jaw
PHD.txt:314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
PHD.txt:412:J jad [y’t'] share, portion. Yadag [ytk! | M jdg] omen. tļadaģ [ytk'] form, property. jadag [y’tk' | M del share, portion; case, cause. jadag-g5(w) [y tkgwb'] advocate, intercessor. ~ЛЬ : intercession. jadag-wihīrih [ytkwhylyh] transformation, alteration. Jadarih [y2?lyh] maintenance. *fadisn [ytsn'] (accidental) quality, property. ~ig [-yk'] accidental, non-essential. jadiig [y?te&! | M j?dwg, N jadi] sorcerer, magician. — h: sorcery, magic. *jay [у?л | N ~] sissoo tree. jagar [yal | N jigar] liver. Jah-, v. jastan. jahišn [yhysn' | J jhysn-] chance, fortune, omen. Jahišn-ayār [yhyfn hdyb'l | N n. pr. jhiy?r] fortunate. ~ih: good fortune. jahüd [yhwt' | N juhiid] Jew. jām [y m | N ~] glass. јат [M ANE < A mn-h; ут | M Pm, N <] vessel, goblet. lfamag [y”mk! | N јата) = *jām. атар [y mk! | М ртр, N fama] clothing, garment. jang [yng | M jnng, N ~] struggle, battle, fight. Jar [ywl | M рт] time, occasion. jastan, jah- [ystn!, yh-] happen, occur, chance (to be). ~išn, v. jahišn. Jašn [yfn! | N —] celebration, festival. jaw [ŠZ < A £% | N ~] barley. Jāwēd [y wyt! | (P ywyd), N ~] eternal.
PHD.txt:414:jawédan [LOLMN < А l-Imn; ywyt?n' | (P y'wyd?n, M Pyn), N ~] eternally, always. ~ag [-k! | (P -g), N ~a] eternal, perpetual. jawén [S£yn! | № jawin] made of barley. jeh [yh, yyh = Av. jahi-] the Whore, female arch-demon. fiw [суш!, yyw! = Av. fiwya-] (consecrated) milk. *jomā [ywm’y] together with; both. jorda [ywilt’y, 2k | (P yw?rd?w), J *jwrd?r] corn, grain. jo(y) [ywd, ywb! | N ~] stream, channel. Jóy-, -išn, v. Jadan. jud [ywdt' | M jwd] separate, different; anti-. ~ az [N juz] except, apart from. judàg [ywd? h! | N juda] separate, different. ~ih: separation, difference. Jūdan, jóy- [ywtn!, ywd- | M jwwdn, (jw-), (N jawruan)] chew; devour (daevic). „išn: eating (daevic). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk!] schismatic, heretic. ~th: heresy. Juy [усе | N ~] yoke. Jumbāģīh [ywmb’kyh] motion. jumbénidan, jumbén- [ywmbyn-yin'] (cause to) move. jumbidan, jumb- [ywmb-yin' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- [ywmbyh-stn'] be moved. juttar [ywdtl | M jwtr] different, otherwise. --īh: opposite, reverse. Juwān [ywb?n! | (P ywn), N jawàn] young; a youth. ~th: youth. juxt [ywht! | (P ywxt), N juft!] pair, couple.
PHD.txt:428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
PHD.txt:649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
PHD.txt:2498:jaw ērwārag.
PHD_mackenzie.txt:1390:ayOxiust ['ywkhfwst l = Av. ayoxlusta- I M Uywdyst I] metal.
PHD_mackenzie.txt:2054:drayan-Joyisn [d1'd'n ywdfn ] one who speaks while eating.
PHD_mackenzie.txt:3080:jo(y) [ywd, ywb ' I N --] stream, channel.
PHD_mackenzie.txt:3082:Jud [ywdt ' I M jwd] separate, different; anti-.
=== NYB jaw
277:*adar-var [^dlw?l] *downwards: ~ tà 6 down to 21%, v. druvāsp. — I derive it from adar (g. v.) + var, cf ham-vàr. [It cannot have anything to do with adarvär BdJ 3511, 5710 = adarvārak BdA p. 103°. 120? ‘lower jaw’, also:the rendering of Av. (1767) hanuharana:].
1095:eak [ck'] the top of the skull; of a sheep: the extremity of the head = the nose and the chin 1028. — NP cak ‘the lower jaw and chin', but Bal. prep. cak*-à *upon'. cand [end] 1. interrogative: how much? how many? 2412-13, 629. 8313. ki... ~ in- direct interr. 213-4 — 2. relative: as much, as many as: ---šān tuvān dätan as much as they are able to bestow 79%; apärik ~ vazurg-kunisndn the other performers
2842:oškan [>wškn'] a verbal form used as pt. pass. and as pret. pass. 3d p. sg., to *throw: aš 6 pasēh gav apāc rānēnīt (g. v.) with the gl. kü apāc ~ ‘that is: it (his hand) was flung backward’ 485 -$; 62 gurg zat zanak (g. v.) with the gl. ki dahan évak apäk dit frot ~ ‘that is: his jaws were clasped together (the upper jaw was clasped down against the lower jaw)’ 5067; [(ka) dēn-ākāhēh ~ (when) reli- gious knowledge is overthrown DkM 33379; ātaxš mänäk aparociónik hesme m hàn i xét like a fire which has to be kindled but is thrown into wet fuel, ibid. 411°]. As it stands, this form can only be derived from *avis-kan- (the root *kan- ‘to throw’ found, e. g., in apakan- dan, q.v.), thus originally *avis-kanta- > *ēškand > oškann with assimilation of -nd > -nn, but the form is singular, as only old -nd, as far as we know, under- went this assimilation, not -nd- < -nt-. The inf. of this vb. shows the regular form expected: cé andar én mātagdān 6s- kandan [’wSkn'dn'] apāyišnīk dart druš- take [-k' +1, for -keh] vicārihēt ‘the (trouble-hardness =) troublesome diffi- culties which in this book inevitably
4488:izanak [znk'] jaw 50%. - MPrth zne (S); NP zanas.
4521:gor zat he shot an arrow at the onager 319-20; parr 6 pist zat its wing struck (the bowl with) the meal 925-26; 57 (= 6) fravahr + Zartuxst aš zafar frac zat threw open its mouth towards Z. 4012-13; 5; (= 6) gurg zat zanak the wolf's jaw was struck 506, with the gl. kū-š dahān ēvak apäk dit frot oškan (g. v.); Vidrafš pat dil zat stabbed V. in the heart 292; 25?! (cf s. v. rad 2 b)]; 383; — ēvak 6 dit ~ to knock to- gether 12019-20; ka šamšēr frac zanēt when the sword makes a stroke forward 254 (opp. apāc vēžēt, v. *véxtan); to drive (a peg) down into the soil 202%; tanbür ~ to play on the lute 476, — Av. (490) !gan-, pres. jan-; MPrth jdn jn-; MPrs zdn zn-; Paz. NP zadan zan-. V. also janišn, zanišn, zatak, zatar; cf apa-žand, ozatan.
```


## [2026-09-06T15:30:39.520Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://www.wisdomlib.org/definition/yata",
 "prompt": "Sanskrit yāta (यात): give the Monier-Williams definitions, especially 'a going, motion, course, way, path'."
}
```


### [2026-09-06T15:30:45.967Z] TOOL RESULT

```
# Yāta (यात) - Monier-Williams Definitions

According to the Monier-Williams Sanskrit-English Dictionary provided in this resource, **yāta** has several key meanings:

**Primary Definition:**
"Motion, progress, gait, course, drive" represents the core sense of this past participle form derived from the root √yā (to go).

**Additional Senses:**
The dictionary notes that yāta can also mean:
- "Gone, proceeded, marched" (as an adjective)
- "The place where a person has gone"
- "The past time" (contrasted with future events)
- "The guiding or driving of an elephant with a goad" (in technical contexts)

The entry emphasizes yāta's versatility across multiple semantic domains—from describing physical movement and transit to indicating temporal concepts and specialized equestrian terminology used in elephant management literature like the Mātaṅga Lila.
```


## [2026-09-06T15:31:13.417Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ei-  ,gehen\\|ei- , gehen\\|i̯ā-\\|ia-, i̯ā-\\|yāti\\|iā-ti\" POK_01.txt | head -20; echo \"=== search 'iä'\"; grep -n \"iä-\\|iã-\\|ia- (i̯ā-)\" POK_01.txt POK_02.txt | head -10"
}
```


### [2026-09-06T15:31:13.481Z] TOOL RESULT

```
4246:I.  ei-  ,gehen',  erweitert  ei-dh-,  ei-gh-,  i-tä-  und  i-ä-,  i-e-  :  iö-  :  19-]  Nominal- bildungen i'to-,  oi'UO-,  oi-tO'  und  i-ter,  Gen.  i-ten-os  ,Weg'. Ai.    imi,    kl,    imdh,   ydnti  ,gehen',  av.    aelti,   yeinti,   apers.  aitiy   ,geht', themat.  Med.  ai.  dya-te   usw.  (das  scheinbar   dehnstufige  ai.   äiti,   av.  äiti ,adit'  ist  *ä-a{ti,  mit  Präf.  ä);
=== search 'iä'
POK_01.txt:434:Dcazu  baltoslav.  *aldiiä-  in  ksl.  ladiji,  ahdiji  f.  ^Kahn^^  lit.  aldijä,  eldijä f.  ^Flußkahn^,  auch  lit.  eldijeU  ^Räucherpfanne^
POK_01.txt:1408:. Erweiterung'  bhö-s-:  Sii.bhäs-n.  (ved.  auch  zweisilbig),  Instr.  bhäsä 1  'cht  Schein,  Herrlichkeit,  Macht',  subhäs-  , schönen  Glanz  habend',  bJiä- *   //    o-länzt^  bhüsant-  ,glänzend',   bliäsah  n.   , Licht' ;
POK_01.txt:1626:lat.  fldöj  -ere,  flsus  sum  ,traue,  vertraue'  (flsus  ist  ^o-Partiz.),  fldus jsuverlässig';  foedus  (*bhoidhos)^  bei  Ennius  fldus  (*bheidhos)  n.  ,Bünd- nis',  fides  , Zutrauen,  Glaube',  Dius  Fidius  ,Schwurgott';  umbr.  combißatu (*bhidhiä-)  ,cön£iditö';  über  osk.  Fiisiais,  umbr.  Fise^  Fiso,  Fisovio-  s. WH.  I  494;
POK_01.txt:1645:I.  bhel',    balto-slav.    auch    bbelo-   ,glänzend,  weiß^     auch    von    weißlichen Tieren,  Pflanzen  und  Dingen,  wie  Schuppen,   Haut  usw.;  zu   1.  bJiä- im   selben  Verhältnis  stehend,  wie  stel-  zu  stä-  ,stehene  del-  ,spalten^ zu  *dä(iy  ,teilen^ Ai.  bhälam  n.  ,Glanz,  Stirn^  sam-bhälayaü  ^blickt^  (dehnstufig);  baläkä ,eine  Kranichart^  mit  b-  nach  bakd-h,  ,eine  Reiherart^ ; arm.  bal  ,Blässe,  Bleichheit^;
POK_01.txt:2094:alb.  hujj  hüj  (*bunjö)  ,wohne,  übernachte',  burr,  burre   (*buro-)   ,Manu^i; Ehemann',  baue  ,Wohnung,  Aufenthalt,  halb  verfallenes  Haus'  {*bhouona: a,i.  bhavanam),  banoj  , wohne';  bun{e)  , Sennhütte'  {Hhuna)]  vielleicht  auch böte  ,Erde,  Boden,  Welt,  Leute'  (*bhiiä-tä  oder  *bhue-tä).
POK_01.txt:2325:Bsl.  ursprgl.  Präsens  *bhdiö-y  Prät.-St.  *bhiiä-j  Inf.  *bhltei]  apr.  biät ,fürchten^,  kausat.  pobaiint  ,strafen^;  lit.  bijaus,  bijötis  (auch  nicht  reflexiv' ,sich  fürchten^,  lett.  bistuos,  bijuds,  bities  und  bijäjuos,  bijäties  ,sich  fürchten' lit.   baijils  ,furchtbar,  schrecklich,  abscheulich^;   baidaü,   -yti  ,scheuchen'^ lett.    baXdUj    baXdyt    und    biedet    ,schrecken^,    dazu    lit.    baisä    ,Sch recken' i^baid-s-ä),  baisüs  ,schrecklich,  greulich^,  baisiöti  ,beschmutzen,  beschmie- ren^ (und  aksl.  bäs^  , Teufel^,  *bH-s^)]   lit.  bdime  ,Furcht^;  bdiU  ds.  (bailus ,furchtsam^).
POK_01.txt:2654:I.  dei-,  deiQ'f  di-,  diä-  ,hell  glänzen,  schimmern,  scheinen'  (älter  ,*Strahlen
POK_01.txt:2694:Über  hitt.  siwat-  ,Tag',  Hivanni-  ,Gott'  (aus  *dieu-?),  hierogl.-hitt.  tina- ,Gott',  §ijäri  ,erscheint'  (*diä-?)  s.  Pedersen  Hitt.  57,  175  f.
POK_01.txt:2703:Ai.  diyati  , fliegt,  schwebt-;  gr.  dZvog  m.  ,Wirbel,  Strudel;  rundes  Ge- fäß runde  Tenne',  dhf]  (Hom.),  äol.  dlvra  (vgl.  Jivvof.i€vrjgj  Hoffmann  Gr. P.  II  484)  ,Wirbel,  Strudel',  divio),  ölrsvo),  äol.  dlvvrjfiL  , drehe  im  Wirbel oder  Kreise,  schwinge';  intr.  ,drehe  mich  beim  Tanz  im  Kreise'; pass.  , treibe  mich  herum,  taumle  umher,  rolle  (die  Augen),  wirble  (vom Fluß),  drehe  mich  tanzend  umher',  divw  äol.  öivvu)  , dresche',;  liom. <J/w  ,fliehe',  d'iouai  ,jage  weg'  (mit  auffälliger  Verteilung  der  intr. und  tr.  Bed.  auf  Aktiv  und  Medium),  hom.  öiswai  ,sie  eilen',  öieod^ai ,fliehen',  evöisoav  ,sie  hetzten',  disgög,  (Ttovg)  ,flüchtig'  (nach  hre,  i'srai  :  uvrai zum  thematischen  d/firat  analogisch  disvxai  statt  *SlovTaL  neugebildet?),  dicü-acü , verfolge'  (kontaminiert  aus  ficj-KO)  und  öieaai,  Meillet  MSL.  23,  50  f., Schwyzer  Gr.  Gr.  I  702);  hom.  di'Cr^t.iai  (Fut.  bom.  öi^rjaofiai)  , strebe  wo- nach, bemühe  micli  worum,  suche',  nachhom.  auch  ,forsche'  (*di,-diä-(.iai), woneben  auf  Grund  von  '*öiG-to-  att,  t^rjTeo)  , strebe  wonach,  lasse  mir angelegen  sein';  ob  hierher  mit  ursprgl.  *did- :  l&It]  ,Sturm,  heftige  Be- wegung, namentlich  des  Meeres',  t,&Xog  , Strudel,  heftige  Bewegung  des Wassers'?
POK_01.txt:3100:bsl.  *derua-  n.  ,Baum'  in  aksl.  drevo  (Gen.  dräva,  auch  dr^vese),  skr. dial.  drevo  (dnjevo),  sloven.  drevo,  aöech.  dfevo,  russ.  derevo,  klr.  derevo ,Baum';  dazu  als  ursprüngl.  Kollektiv  lit.  dervä  (Akk.  dervq)  f.  , Kienspan; Pech,  Teer,  harziges  Holz';  ablaut.  lott.  darva  ,Teer',  apr.  im  ON Derwayn]  dehnstuf.  *döru-iä-  in  lett.  düore  f.  , Holzgefäß,  Bienenstock  im Baum';  *su-dorua-  ,gesund'  in  aksl.  s^drav^,  öech.  zdrdv  {zdravy),  russ. zdoröv  (f.  zdoröva)  , gesund',  vgl.  av.  dr{u)vö,  apers.  duruva  ds.
```


## [2026-09-06T15:31:24.255Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<4250 && /^\\s*29[0-9]\\s*$/ {print NR\": \"$0}' POK_01.txt | tail -3; echo \"=== WLD Bd1 ieuo\"; grep -n \"ieuo\\|i̯eu̯o\\|jeuo\\|ydva\\|yáva\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-06T15:31:25.855Z] TOOL RESULT

```
4211: 292
4230: 293
4247: 294
=== WLD Bd1 ieuo
1904: (s.   ieuos „Satzung“).
18610: ieuo- „Getreide“ oder „eine Getreideart".
18622:                                                            ieuos     — ieudh-                                                       203
71124:wegen des x- von xagydvai nloxai. ovvdeoetg nebai Hes. nur auf xi be-
```


## [2026-09-06T15:31:30.897Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 18605,18625p incoming/WLD/WLD_Bd1_pages.txt; echo \"=== WLD iā- go p.104\"; grep -n \"iā-, iē-\\|ia- „gehen\\|iā- „gehen\\|yāti\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-06T15:31:30.966Z] TOOL RESULT

```
    Vielleieht mit i/u- verwandt sind auch die Sippen icu(v)i- „Satzung“
 als „Yerbindlichkeit, Bindung. Fug" (Uhlenbeck Ai. Wb. u. you. Meringer
 IF. 17, 144) und ids- „giirten“ als *jo[u]s- (Prellwitz u. Qtbvvvui. Brug-
 mann I 1 1020, Hirt Abl. 139, 144, Meringer aaO.).

 ieuo- „Getreide“ oder „eine Getreideart".
       Ai. yarn- m. „Getreide ; Gerste. Hirse"                    = av. yarn- m. , Gecreide". npers. /oy
                                                                                        ;


 „Gerste“ (= lit. jaral)               ;   ai.       yavya- m. „Fruchtvorrat" (: lit jduja ,,Scheune“);
                                                                                            .
                          i




                                                            ieuos     — ieudh-                                                       203

jjavasa- n. „Gras. Futter“. av. yavatoha- n. ,,Weide“; av. y.jvtu-                                                    is.    Bartho-
lomae Airan. Wb. 1292) m. „Getreidefeld“;
=== WLD iā- go p.104
```


## [2026-09-06T15:31:35.747Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *104 *$\\|  104  \" incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-09-06T15:31:38.158Z] TOOL RESULT

```
9309:104
```


## [2026-09-06T15:31:40.305Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 9280,9340p incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:31:40.354Z] TOOL RESULT

```
                        o-,

tiuf noch   deutlich  mit lat. itio sich deckend; noch klarzustellen bleibt, ob
das Praes. aus *o-itan in die Weise der Wzverba ubergefuhrt sei).
   nltor aber nicht *ni-itor „mit den FuBen (z. B. auf den Boden) nieder-
kommen", sondern urspriinglieh zu * knag'ih -, coniveo.        Ob oi’aco „werde             —
tragen", ark. La-oior] (von Prellwitz 2 s. v. als *otV-oco „werde fordern" ge-
deutet) als „an etwas herangehen" oder „mit etwas gehn“ wie utor auf
*o Jr *it- beruht?
   d7i-Bildungen: gr. idpa n. „Gang“, rioi&yi] „Eingang“ (bei der Frucht-
barkeit des Suff. gr. -ftyo- keine ganz verliiBlichen Zeugen fur bereits
                                                 r
idg. *i-dh-); zweifelhafter ladpog, att. inschr. Io&/n6g „schmaler Zugang,
Landzunge, Landenge; Hals“ (Gdf. *idh-dhm<>s ? wenigstens ware der Weg
des Eindringens von o in alteres *l'&p,og nicht klar; nicht fordernd Boi-
sacq     s.   v.)

  anord. eid „Landenge“                       (Bugge BB. 3, 101 f., Bezzenberger-Fick BB. 6,
235),    lit.   instr. eidine            „im PaBgang" (von Pferden), aksl. ida „gehe“ (s o.).
   Hochst fraglich lat. idus, -man „Monatsmitte“, osk. eiduis eidu’is d. abl.
pi. (wohl zunachst nach Meyer- Liibke ZfoG. 46, 617 f. mit air. eece „mensis
lunaris, mensis" aus *eid-skiom zu verbinden), worin Reichelt KZ. 46, 325
einen alien Dual „(Zeit, w o) Sonne und Mond (in ununterbrochener Fort-
                                                 7
                                        -     :      )                                                                      ,                     •




104

dauer des Lichtes sich ablosen)“ rermutet unter Yerweis auf die Bedeu-
tung von wax. iiimak „Mond“: soghd. zamanu „Zeit“ ai. gamana- „gehend,                                      :



kommend“.
     w-Bildung:            ai.   etna- m. „Gang“ (aber gr. oliiog, oluog „Gang“ zu seloazo,
                     u                Steige“ mit lit. -sm Suffix (eine alte
s.   '*uri-         lit. eismS „Gang,
              „n:itai ) ;
s-Erweiterung der Wz. wird weder durch ai. csati „schleicht, geht“                                                                              —
vielmehr zu is- „erregen“                           —
                                 noch durch ags. is-ban, nd. is-ben „Hfift-
                                                         ,


bein“ gestiitzt, Uhlenbeck Ai. Wb. 36 s. fiber letzteres Falk-Torp u. isben,
                                                                   ;


Weigand-Hirt u. Eisbein aus oder zu gr. toyjov „Htiftgelenk“?).
     w-Bildung:            ai.   cm- „eilend“, m. „Lauf, Gang, Gewohnheit, Sitte“; ahd.
ewa f. „Gesetz, Norm, Bfindnis, Ehe u                                      ,
                                                                                       as.   eu, eo m., ags. <sw,                   a    f.   „Ge-
setz, heiliger Brauch, Ehe“                         (Fick I 1 346, III 4 4, Zupitza Gutt. 74, Meringer
IF. 18,275; nicht zu aequus nach Noreen Ltl. 179, Kluge 8 u Elte; ffir                                                          .
```


## [2026-09-06T15:31:51.675Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"BARLEY\\|8\\.4[0-9]\" SYN.txt | grep -i \"barley\\|grain\" | head -10; echo \"---\"; grep -n \"Av. yava\\|yava-\\|yáva\" SYN.txt | head -10"
}
```


### [2026-09-06T15:31:51.751Z] TOOL RESULT

```
8364:. Xiros ‘grain’ (8.42) is also used for food’, and so especially otra or ciria (neut, pl.), also otrnots.
9093:5. Lith. duona (Lett. duona ‘bit of bread’) perh. : Skt. dhdnds (pl.), dhanya- ‘grain’ (8.42). Trautmann 58. Miihl.- Endz. 1.534. Otherwise (as orig. ‘sift of God’ : Lith. duoti ‘give’) Walde-P. 1.831.
9416:5. Lith. Zrnis, Lett. dzirnis : ChSl. zrtino, Goth. kaurn, Lat. grdnum ‘grain’, etc. (8.42). Walde-P. 1.599 f.
12309:Av. yavan-, yavin- ‘field of grain’, fr, yava- ‘grain’ : Skt. yava- id., ete. (8.42).
12353:place’. NG ctramoBijxn, epd. with cizos ‘grain’ (8.42).
12358:Lat. granarium (> It. granaio, Sp, granero, Fr. grenier), usually in pl. gra- naria, fr. granum ‘grain’ (8.42), whence also Fr. grange (> Br. granch) fr. VLat, granica, fem. of an adj. *granicus ‘per- taining to grain’. REW 3839, 3845, Gamillscheg 482.
12382:6. OhSI. Z2tinica, SCr., Russ. Zitnica, fr. ChSl. Zito ‘grain’ (8.42).
12385:Avy. yavan- fr. yava- ‘grain’ (8.42). Barth. 1.267.
12706:3. Fr. graine ‘seed’, fr. VLat. grana sg. coll., orig. pl. of Lat. granum ‘grain, kernel’ (8.42).
12733:Words for ‘mow’ or ‘reap’ (in the old specific sense, now uncommon, of NE reap) are mostly from ‘cut’, or in some eases ‘strike’, with partial or complete specialization to ‘cut grain’ (and besides the words listed here the common words for ‘cut’ may be freely used in equivalent expressions, as NE cut, NHG schneiden, etc.). In one group the specific ‘mow’ is common to Greek, Latin, Celtic, and Germanic. Owing to the natural asso- ciation, words for ‘mow, reap’ may be used for ‘gather the crop, harvest’, and this may become the dominant sense (as in NE reap). Conversely, words in which the latter sense is the more origi- nal may serve also for the specific ‘mow, reap’, and so are included here (but not those which are used only in the broad sense ‘reap’ = ‘harvest’, as OHG aron, NHG ernten, for which see under ‘har- vest’, 8.41).
---
2441:4. Goth. magus ‘boy’, ON mogr ‘boy, son, man’, OF magu ‘son, servant, young man’, with derivs. for ‘girl’, Goth. mawt (magaps ‘virgin’), ON m@r, OE megep, megden, ME, NE maiden, maid, Du. meisje (dim. of meid, dial. form of maagd, Franck-v. W. s.v. meid), OHG magad, MHG maget, NHG magt, mdd- chen : Ir. magu (Ogam), mug ‘servant’, Br. maouez ‘woman’, Av. maryava- ‘un-
9790:6. Skt. yavasura-, epd. of yava- ‘grain, millet, barley’ and surd- itself perh. ‘beer’ (KZ 35.314) = Av. hura- ‘milk-wine’ (Barth. 1837), fr. the same root as Skt. soma-, Av. haoma- (5.92), or more directly : OE sar ‘sour’, etc. Walde-P. 2.513.
12309:Av. yavan-, yavin- ‘field of grain’, fr, yava- ‘grain’ : Skt. yava- id., ete. (8.42).
12348:K troBohdy, &roFnK Goth. bansts Lith. — darziné, skuné Se La A hte ON hlada Lett. Sk'unis Lat. horreum, grandaria Dan, lade ChSI. Zittnica It. granaio Sw. ada SCr. —Stagelj, 2ilnica, ambqy ry. grenter, grange OE berern, beren Boh, stodola Sp. granero ME bern Pol. stodola Rum. surd, hambar NE barn Russ. Zitnica, ambar Tr. saball Du. schuur : Skt. kugila- Nir. _ sciobal OHG | sciura, scugin, stadal Av. yavan- W. ysgubor MHG schiur(e); schiune, Br. granch stadel
12385:Avy. yavan- fr. yava- ‘grain’ (8.42). Barth. 1.267.
12922:the generic name for the cereal prada: include a few that reflect an IH wor denoting ‘grain’, or more P pobaplneone particular kind of ‘grain’, the one best known in the IE period. Many more reflect an IE word denoting ‘a grain, emel’, which as esp. characteristic of the cereals, led to the generic ‘grain’. Similarly some other words orig. denoted ‘y grain’ or ‘seed’. Several come from such notions as ‘food, means of life, bread, fruit of the soil, good’, with spe- cialized application to the cereals from their prime importance as food products. ; The widespread literary words coming oe Lat. ceredlis ‘pertaining to Ceres’, 4%. céréales, NE cereals, etc., are omitted from the list. es ete words are often special- © denote a particular kind of grain the one that is the chief eiten tegion, as to « ie product of a ". froment, " part It i (aie TL Slone la edag Ol. éylo, NG 1,4 0 ‘rye’ (Boh. Zito, Gemany), to ‘hatleg qo eeny, Parts of ) © Darley’ (later Skt. yava-,
12928:AGRICULTURE, VEGETATION 513 8.42 GRAIN (Generic = British Corn) ; Lith. griidai, javai Goth. kaurn Kat, ros ON korn Lett. labiba amet) oirnpt Dan. korn ant Bie, frimentum to Sw. sdd, korn Hf es rand, frumen’o OE corn Boh. obilt biada ME corn, greyn : Pol.  zboze Hé, grain NE corn (Brit.), grain Russ. chleba grano Du.  graan, koren Skt.  yava-, dhanya-, sasya- OHG korn Av. yava- (dana-, hahya-) ith, arbar MHG korn ad NHG  gelreide y ed for ‘grain, corn’ (in the | food in Greek and Roman antiquity, and
12931:Skt. yava- ‘grain’ in RV, later ‘barley’; Av. yava- ‘grain’, NPers. jav ‘barley’; Lith. javai (pl.) ‘grain’; Grk. feat (pl.) ‘spelt’.
12972:(Ot AV. yava-,  dhanya-r Skt. A
13005:8.44 BARLEY Grk. «pid Goth. barizeins (adj.) Lith. mieSiat NG xpiOape ON bygg, barr Lett.  miezi Lat. hordeum Dan. byg ChSl.  jeetnénit, jetint (adj.) It. orzo Sw. bjugg, korn SCr.  jetam Fr, orge OE bere, berlic (béow) Boh. jeémen Sp. cebada ME bere, barli Pol. Jeczmien Rum. rz NE barley Russ. jaémen! Ir. eorna Du. __gerst Skt. —_ yava- Nir. corna OHG  gersta Av. Steiis W. haidd MHG §gerste Br. heiz NHG gerste
```


## [2026-09-06T15:31:59.544Z] TOOL CALL #88: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/yelek",
 "prompt": "Turkish yelek: etymology, first attestation, and any note on European borrowings (gilet, chaleco)."
}
```


## [2026-09-06T15:32:02.150Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARB\"; grep -n \"جادة\\|الجادة\" ARB_mo3rb.txt ARB_abdulraheem.txt TAD_pages.txt 2>/dev/null | head -10; echo \"=== HRN jadde\"; grep -n \"^[0-9]*\\. *jadda\\|jadde\" HRN.txt | head -5; echo \"=== HUB jadde\"; grep -n \"jadde\\|Strasse\" HUB.txt | head -5"
}
```


### [2026-09-06T15:32:02.255Z] TOOL RESULT

```
=== ARB
=== HRN jadde
=== HUB jadde
```


### [2026-09-06T15:32:05.758Z] TOOL RESULT

```
I appreciate your question, but the webpage content provided doesn't contain the etymological information you're requesting about the Turkish word "yelek" or its European borrowings like "gilet" and "chaleco."

The page appears to be only the header and footer of Nişanyan Sözlük (Nişanyan Dictionary), showing navigation elements and copyright information, but not the actual dictionary entry for "yelek." To find the etymology, first attestation, and information about European cognates, you would need to access the full dictionary entry on that website.
```


## [2026-09-06T15:32:11.539Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY jo/جو\"; grep -n \"^جو \\|جو (\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY jadde\"; grep -n \"جاده\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY yava\"; grep -n \"yava\" incoming/ARY/ARY_pages.txt incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-09-06T15:32:11.617Z] TOOL RESULT

```
=== ARY jo/جو
6275:ِ ۴ / جو (گونه‌ای غله)
=== ARY jadde
=== ARY yava
```


## [2026-09-06T15:32:14.423Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 6260,6295p incoming/ARY/ARY_pages.txt; echo \"=== pdf page tag\"; awk 'NR<6280 && /\\[pdf page/ {p=$0; n=NR} END{print n\": \"p}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T15:32:16.251Z] TOOL RESULT

```
آلمانی کهن (05824۸9 2۲۵/3 صا0): برهان قاطع + انصن
۸ ,80 ,10
پادداشت,
چم این واژه در سانسکریت: توانایی» بنیه.
| مانگلیس سروازی ارس 188
9 اوستای (/(4۲574): 1۸ برنانی 0788/0): ۰ 138۳۸7085 ,31۳3۳۸
پهلوی راام‌برمم: تْ. فلال ,۸0۸8 لانین (0امم: 75860878 ,1800
ْ اوستی (0555710): با162 فرانسه (4ل0/0ق۳8): 2018
اُ کردی (2/0/3(7). وان ره اسپانیایی (5۳۸۸۷]34): 10
بلوچی (8۸1-011): 3 ایتالیایی (/(۸لله7): ۳/0
افغائی (پشتر) (4۳0/1۵71). اسلاوی کهن ( ماک 0267 ام
16۸[ 1
سانسکریت (۷۸6۸5:)5۸۸7580/7 ,۷81687 روسی (/(85514): 1۸
[pdf page 213]
۹
ِ ۴ / جو (گونه‌ای غله)
لیتوانی (۸۸1۸04لا727ار): پسگشت‌ها 5
5 ,2۸305 ۳
لتونی (لتی) (07۲14/۷): ۸۸8 ,165 7 (1187۸710) 9 ای ما
پروسی کهن (/۶7۷934 ۰:00 1۸00 100 ال
ایرلندی کپن (9(0لق1 02م: 10071۸78 2 (37۴3) :2لاعن مار
25152 ۰ بلاط
7 (۲8۸710) :00/5
8 (78۳۸710) 7
(0 2 :۸0۵145 ۵ اتمه
برهان قاطع : 4۹
اوستایی (/4857۸۸): 0 ,۷۸۷۸ لیترانی (07770۸74): ۸۷۸8[ بل1۸۷۸
پهلری (,1۸1ن(۸): 1۸۷۷80 ,1۸3 ,۸ لترنی (لتی) (۸711/2ا): 1۸
اوستی (05587/2): ۰ ۷۸۲ ,ت۷2 ,1۸۷۷ هتبت (71771]78). ۸
کردی (70(13(7). 6 تاه[
بلوچی (761امل7۸۷:)8۸ رد پسگشت‌ها کیت تیا
. تخاری 8 (8 2008۵0۷ , ۷ 84 وم
سانسکریت (54۸5867): ۸۷۸8 ,۷۸۷۸ ۵ تفگش :5( 05
یونانی 072280): 78۸1 3 (29ت8۸8) :13 2(2 ۸4
لهستانی (827ا۳0): ع(2 516 کی
روسی (/۸ا95ل): 7 ,0۷8 305 :همم هه(
=== pdf page tag
6273: [pdf page 213]
```


## [2026-09-06T15:32:29.107Z] TOOL CALL #92: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%98%DB%8C%D9%84%D8%AA",
 "prompt": "Persian ژیلت: meaning and etymology (French gilet? Gillette?). Quote exactly."
}
```


### [2026-09-06T15:32:32.421Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T15:32:33.191Z] TOOL CALL #93: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%AC%D8%A7%D8%AF%D9%87\" \"https://en.wiktionary.org/wiki/%D8%AC%D8%A7%D8%AF%D8%A9\" \"https://en.wiktionary.org/wiki/%D8%AC%D9%88\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/y%C3%A9wos\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/y%C3%A1wah\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 226, roots Iatos / Ieuo: Persian jadde, Persian jo, PIE *yewos, Proto-Iranian *yawah\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:32:37.140Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0ffc47f8d3087719.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/97008256eb8478c2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/514c621597fcadca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d722cad8ea3d4f55.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3cb0dd7f7a54dc5f.txt
```


## [2026-09-06T15:32:41.975Z] TOOL CALL #94: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/yelek\" \"https://en.wiktionary.org/wiki/gilet\" \"https://en.wiktionary.org/wiki/%D8%AC%D9%84%DB%8C%D9%82%D9%87\" \"https://abadis.ir/fatofa/%D8%AC%D8%A7%D8%AF%D9%87/\" \"https://www.wisdomlib.org/definition/yata\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 226, roots Ijlak/Yelek and Iatos: Turkish yelek, gilet, Persian jaliqe, Mo'in/Dehkhoda jadde, Sanskrit yata\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:32:52.087Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6aa3da78e1f5b683.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e565432d46ccb2d4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b07103a8d403bf6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e6a2daab7fa93c99.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/842cd9a6a6fefac3.txt
```


## [2026-09-06T15:33:54.371Z] TOOL CALL #95: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%98%DB%8C%D9%84%D9%87/",
 "prompt": "Persian ژیله: give the Mo'in / Dehkhoda entries and the origin tag (e.g. [فر.]). Also anything on ژیلت."
}
```


## [2026-09-06T15:33:55.834Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT yava\"; grep -n \"yava-  m\\|'yava-\\|yava- \\+m\\.\" BRT.txt | head -10; echo \"=== AHD ei- go\"; grep -n -i \"^ei-1\\|ei-1\\. To go\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-06T15:33:55.895Z] TOOL RESULT

```
=== BRT yava
4664:•  j.  ainyava-  m.  EN.   eines   Gläubigen:
5570:•  j.  airyava-  m.  EN.  Name  eines  Gläu-  des  Viitäspa-.  pu>ri>m  yat  'fa/ie  taxm>m bigen:    manuS.airahe  (sd.)    'vahe   asaonS  kai-alm  züstJspfm  Vtj.  105.
19898:•  j.  mainyava-  Adj.  (fem.  'yava-''>;  •ywvJ-. 'yaoy-)  'geistig,  unslofflich  (und  daher imsichtbar)"^:  hianttm  dräjB  'yava  stis asaonS  data  ai  V.  2. 19  PüZ.;  —  vTspam a/aonS  stTm  . .  'ymimcä  gaihyqmcS  V- JJ.  i ;
21314:•  j.  yava-  m.  'Getreide':  yat  °vs  pouru^ bavät  ata  ma^nm  *tat  mairyät  "damit das  Getreide  reichlich  wachse,  drum  soll man  den  M.  aufsagen"  V.^;.  32f. '';  — yc^  'vO  dayst  aat  dadva  s^Um  (sÄ)  V.J.  3  2 ;
=== AHD ei- go
```


### [2026-09-06T15:33:59.651Z] TOOL RESULT

```
# ژیله Dictionary Entries

**Mo'in Dictionary (فرهنگ معین):**
Origin tag: [فر.] (French)
Definition: "نوعی لباس بدون آستین جلو بسته شبیه بلوز" — a sleeveless, front-closing garment resembling a blouse.

**Dehkhoda Dictionary (لغت نامه دهخدا):**
Two entries exist:
1. Claude Cazimier — a French botanist (1806-1896)
2. Louis — a French industrial historian and member of the French Academy, born in Paris in 1876

**Origin Tag:** [فر.] indicates French origin for the clothing term.

**Note on ژیلت:** The provided content does not include any information about ژیلت (alternate spelling/variant).
```


## [2026-09-06T15:34:19.132Z] TOOL CALL #97: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"https://abadis.ir/fatofa/%DA%98%DB%8C%D9%84%D9%87/\" --note \"pdf page 226, root Ijlak/Yelek: Mo'in tag [فر.] for Persian ژیله\" 2>&1 | tail -1; mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg226.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/226.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/226.png"
}
```


### [2026-09-06T15:34:22.207Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/82e9d8a6ea3a10d9.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 74322 Sep  6 11:34 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/226.png
```


## [2026-09-06T15:40:20.643Z] TOOL CALL #98: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk226.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 226,\n \"book_page\": 196,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n\n  # ------------------------------------------------------------------ entry 2\n  {\n   \"entry\": 2,\n   \"root\": \"lâtos, lâtom, lâtis\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"S. E. Mann's IE *i̯ā-tos, -tom, -tis 'going, movement; gang, crowd; gait; turn, period' — a *-to-/-ti- derivative of the PIE root *h₁ey- 'to go' in its long-vowel extension *i̯ā- (Pokorny 293 ff. '1. ei- \\\"gehen\\\", erweitert … i-tā- und i-ā-, i-ē- : i-ō- : i-ə-')\",\n   \"note\": \"The root box reproduces Mann, An Indo-European Comparative Dictionary col. 441 almost verbatim, including the odd multi-part gloss: 'iātos, om, is \\\"going, movement; gang, crowd, shoal; gait; turn, period\\\"'. Mann's reconstruction is his own: Pokorny and Watkins/AHD have no *i̯ātos entry, only the parent root ei- 'to go' (Pok. 293-297) with the extension i-ā- from which Skt. yā-ti, Av. yā- 'to go' come. So the root box is a faithful copy of an idiosyncratic source rather than of the consensus. EXTRACTION ERROR: the printed headwords are 'Iâtis / Iâtom / Iâtos' with a capital I (Nourai's letter for PIE *i̯-/y-); the OCR read the sans-serif capital I as a lower-case l. The same misreading affects the redirect stubs 'lě', 'lěro', 'leu' (= Iĕ, Iĕro, Ieu) and 'lo' (= Io) on this page, and 'leuo' in entry 6. That capital I is proved by Nourai's own cross-references on this very page: 'Iĕ / Iĕro → see root Ei' (Pokorny derives i̯ē-ro- 'year' from ei- 'to go'), 'Ieu → see root Yeu 2', 'Io → see root I 2', and by the alphabetical sequence Iâ- < Iĕ- < Ieu- < Ij- < Io-.\",\n   \"note_fa\": \"ریشهٔ این نمودار برساختهٔ استوارت مان (فرهنگ تطبیقی هندواروپایی، ستون ۴۴۱) است: *i̯ā-tos «رفتن، حرکت، گروه، نوبت، دوره»، که صورتی است با پسوند ‎*-to-‎ از ریشهٔ هندواروپایی آغازین ‎*h₁ey-‎ «رفتن» در گونهٔ کشیدهٔ ‎*i̯ā-‎؛ پوکورنی (ص ۲۹۳ به بعد) همین ریشه را با گسترش‌های i-tā- و i-ā- می‌آورد ولی ستاک *i̯ātos را جداگانه ثبت نکرده است. پس ادعای نورایی با احتیاط پذیرفتنی است: او مان را وفادارانه نقل کرده، اما مان در این مورد تنهاست. نکتهٔ فنی: در کتاب سرواژه‌ها با حرف بزرگ I چاپ شده‌اند (Iâtis، Iâtom، Iâtos)، و «l» در داده‌های استخراج‌شده خطای خوانش اسکن است.\",\n   \"error_in\": \"extraction\",\n   \"book_prints\": \"Iâtis / Iâtom / Iâtos (capital I)\",\n   \"correct_form\": \"Iâtos, Iâtom, Iâtis\",\n   \"sources\": [W + \"%D8%AC%D8%A7%D8%AF%D9%87\", W + \"%D8%AC%D8%A7%D8%AF%D8%A9\"],\n   \"ref_check\": [\n    {\"ref\": \"IEC:441\", \"status\": \"supports\",\n     \"note\": \"Mann, IEC.txt line 6354 (the page tag '441' stands at line 6347, immediately above): 'iātos, om, is ‘going, movement; gang, crowd, shoal; gait; turn, period’. Cf. iā-, -mi … Skt. yatàm; Av. yatom; Per. jade ‘highway’, j = ǰ; Ir. áth ‘ford’; W iawd ‘season, time’; OCS jato …' — the root box, its gloss and all three daughter nodes come straight from this column.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_01.txt line 4246, printed p. 293\", \"stance\": \"partial\",\n     \"note\": \"'1. ei- ,gehen‘, erweitert ei-dh-, ei-gh-, i-tä- und i-ä-, i-e- : iö- : i9-; Nominalbildungen i-to-, oi-uo-, oi-to- und i-ter, Gen. i-ten-os ,Weg‘' — Pokorny has the parent root and the i̯ā- extension but no *i̯ātos lemma.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I, pp. 100-105 (WLD_Bd1_pages.txt line 9309 = printed 104)\", \"stance\": \"partial\",\n     \"note\": \"The ei- 'gehen' article covers the -dh-, -m-, -u- and -s- formations of the root; no *i̯ā-to- noun 'road' is set up there either.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, appendix\", \"stance\": \"silent\",\n     \"note\": \"No entry *yato-/*ya- 'to go' in the Watkins appendix (grep 'yā-', 'yato' in AHD_watkins1985.txt: nothing); the appendix's only y-initial grain/motion root printed is yewo-.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"yâtem\", \"verdict\": \"plausible\",\n     \"derivation\": \"A verbal adjective/noun *yā-ta- from the Avestan root yā- 'to go' (Av. 3sg. yāiti, Bartholomae AiW col. 1281; cf. Skt. yā-ti) with the PIE participial suffix *-to-, would regularly give Av. yāta-, acc. yātǝm — which is the form Nourai writes 'yâtem'. The form exists, but not with the sense drawn here: Bartholomae's only Avestan yāta- entries (AiW 1283) are (a) n. 'der jemandem zugewiesene Anteil; Besitz' (the share allotted to someone), a PPfP of yam- 'to hold', and (b) a technical term for the third degree of bodily injury; a third yāta- is simply the past participle of yam-. The Avestan word for 'way' from a y-root is rather yaona- (acc. yaonǝm 'Weg', Pokorny 512 s.v. i̯eu-ni-). So the arrow IE *i̯ā-to- → Av. yāta- is phonologically impeccable, but the gloss 'road' rests on Mann alone.\",\n     \"derivation_fa\": \"صورت *yā-ta- از ریشهٔ اوستایی yā- «رفتن» (سوم‌شخص yāiti، بارتولمه ستون ۱۲۸۱) با پسوند اسم مفعولی هندواروپایی ‎*-to-‎ ساخته می‌شود و در حالت رایی yātǝm می‌گردد؛ همان چیزی که نورایی «yâtem» نوشته است. از نظر آوایی هیچ اشکالی ندارد، اما معنای «راه» در واژه‌نامهٔ بارتولمه تأیید نمی‌شود: yāta- در اوستا یا «بهره و دارایی واگذارشده» است (ستون ۱۲۸۳) یا اصطلاحی در بابِ آسیب بدنی. واژهٔ اوستاییِ «راه» از ریشهٔ y- در واقع yaona- است. پس ادعای نورایی (که برگرفته از مان است) با احتیاط پذیرفتنی است ولی معنای «راه» پشتوانهٔ مستقل ندارد.\",\n     \"sources\": [W + \"%D8%AC%D8%A7%D8%AF%D9%87\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:441\", \"status\": \"supports\",\n       \"note\": \"IEC.txt line 6354 lists 'Av. yatom' among the reflexes of iātos — exactly what the node claims, so Nourai's citation is accurate even if Mann's Avestan is not corroborated.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW col. 1283 (BRT.txt line ~21536 'ia83 ‘yata-')\", \"stance\": \"contradicts\",\n       \"note\": \"'j. ‘yāta- n. ‘der Jemandem zugewiesene Anteil; Besitz’ … Eig. ‘was (vom Schicksal) gewährt, zugewiesen ist’; PPfP zum V. yam-' and a second '‘yāta- n. Termin. techn. für die der Schwere nach dritte Art von Körperverletzung' — no sense 'road, way'.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon\", \"stance\": \"silent\",\n       \"note\": \"grep 'yata' in KNT.txt returns only the conjunction yātā 'until'; no Old Iranian noun 'road' of this shape.\"},\n      {\"src\": \"POK\", \"where\": \"POK_02.txt line 2544, printed p. 511-512 s.v. i̯eu-ni-\", \"stance\": \"partial\",\n       \"note\": \"'av. Akk. Sg. yaonǝm ‚Weg‘' — the attested Avestan y-word for 'way' belongs to a different root (*i̯eu-ni-), not to *i̯ā-to-.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"jâddeh «جادّه»\", \"verdict\": \"disputed\",\n     \"derivation\": \"Modern scholarship derives NP جاده jādde from Arabic جادّة jādda, the feminine active participle of جدَّ (root ج د د 'to cut, to be new'), literally 'the cutting one' > 'the beaten middle of the road, highway' (pl. جوادّ jawādd); Persian keeps the Arabic form but writes a single dāl. Wiktionary: 'Borrowed from Arabic جَادَّة (jādda)'; Mo'in tags the entry [ع.] and Dehkhoda [ع. اِ] with the Arabic plural جوادّ and the definition 'معظم الطریق و وسط آن'. The chart's own NOTE sets MON:1202 (Arabic) against FVF:140 and AFM:39 (Arabic borrowed it from Persian); the modern view is clearly with Mo'in. Corroborating negative evidence: Horn's Grundriss and Hübschmann's Persische Studien, which register genuinely Iranian vocabulary, have no jādde at all, and Asbaghi's Persische Lehnwörter im Arabischen — the standard modern inventory of Persian words in Arabic — has no ǧādda. There is no Iranian *yāta- 'road' from which the word could have been Arabicised, and the shape jādde with its Arabic feminine ending and broken plural is transparently Arabic morphology.\",\n     \"derivation_fa\": \"«جادّه» در پژوهش امروزی وام‌واژه‌ای عربی است: صورت مؤنث اسم فاعل از ریشهٔ ج‌د‌د («بریدن، تازه بودن»)، یعنی جادّة «راهِ کوبیده و میانهٔ راه»، با جمع مکسر «جوادّ»؛ در فارسی همان صورت با یک دال نوشته می‌شود. معین آن را [ع.] و دهخدا [ع. اِ] نشانه‌گذاری کرده‌اند و ویکی‌واژه نیز آن را وام از عربی جادّة می‌داند. هرن و هوبشمان که واژگان اصیل ایرانی را گرد آورده‌اند این واژه را نیاورده‌اند و اسبقی در «وام‌واژه‌های فارسی در عربی» هم آن را ثبت نکرده است. بنابراین یادداشت خود نمودار درست تشخیص داده که میان معین از یک سو و امام شوشتری و ادی شیر از سوی دیگر اختلاف هست، ولی پژوهش امروزی جانب معین را می‌گیرد و ادعای نورایی (فارسی‌بودن و برآمدن از *yāta- ایرانی) را رد می‌کند.\",\n     \"sources\": [W + \"%D8%AC%D8%A7%D8%AF%D9%87\", W + \"%D8%AC%D8%A7%D8%AF%D8%A9\", \"https://abadis.ir/fatofa/%D8%AC%D8%A7%D8%AF%D9%87/\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:441\", \"status\": \"supports\",\n       \"note\": \"Mann IEC col. 441 does say 'Per. jade ‘highway’, j = ǰ' under iātos, so Nourai's citation is faithful; the claim is Mann's and is not shared by Iranian/Arabic lexicography.\"},\n      {\"ref\": \"MON:1202\", \"status\": \"supports\",\n       \"note\": \"Mo'in's Farhang (via abadis.ir/fatofa/جاده, section فرهنگ معین) prints '[ع.] (اِ.) شاهراه، راه بزرگ' — the [ع.] tag is exactly the Arabic attribution the chart's note attributes to MON:1202 (page not verifiable: the 6-vol edition is not online).\"},\n      {\"ref\": \"AFM:39\", \"status\": \"not_found\",\n       \"note\": \"Addi Shir's ج chapter runs over leaves 39-50 of AFM_pages.txt (printed ≈ 31-42; leaf 47 ≈ p. 39 carries الجناغ، الجنك، الجنار، الجهبلة، الجهاركاه، الجهارة، الجهوري، الجوتمر). No headword الجادة/جاده occurs anywhere in the OCR of the book. Arabic OCR here is only fair, so this is inconclusive rather than proof of absence.\"},\n      {\"ref\": \"FVF:140\", \"status\": \"not_checked\",\n       \"note\": \"Emam Shushtari, Farhang-e vazheha-ye farsi dar zaban-e arabi — no scan online (refs_online.json: 'kind: website', noorlib viewer requires login).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie (HRN.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep 'jadde/jadda' returns nothing; Horn excludes Arabic loans, and jādde is absent from his numbered list of Persian etyma.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt)\", \"stance\": \"silent\",\n       \"note\": \"no entry for jādde; Hübschmann likewise records only inherited Iranian material and Aramaic/Armenian correspondences.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_pages.txt)\", \"stance\": \"contradicts\",\n       \"note\": \"The standard modern list of Persian loans in Arabic has no ǧādda/gādda lemma (grep 'jadda', 'ǧādda', 'Straße' → only sirāt 'Straße'), i.e. Arabic جادّة is not regarded as a Persian loan.\"},\n      {\"src\": \"MON\", \"where\": \"vajehyab/abadis, فرهنگ معین s.v. جاده\", \"stance\": \"contradicts\",\n       \"note\": \"'[ع.] (اِ.) شاهراه، راه بزرگ' — Mo'in marks it Arabic, against the chart's derivation from Avestan.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"yâtam\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Skt. yāta- is the regular *-ta- verbal noun/participle of √yā 'to go' (yā-ti, RV): PIE *i̯ā-to- > OInd. yāta-, neuter nom./acc. yātam. Monier-Williams glosses the neuter 'motion, progress, gait, course, drive', beside the participle 'gone, proceeded, marched' and 'the place where a person has gone'. That is the same formation as Latin itum, Greek -itos from the same root complex. The chart's one-word gloss 'road' is looser than the dictionaries' 'a going, course, way'; the derivation itself is standard and matches Mann's 'Skt. yatàm'.\",\n     \"derivation_fa\": \"«یاتَم» سانسکریت صورت خنثای اسم مفعول ‎yāta-‎ از ریشهٔ ‎√yā‎ «رفتن» (yāti در ریگ‌ودا) است، یعنی هندواروپایی آغازین ‎*i̯ā-to-‎ که با قاعده به ‎yāta-‎ بدل شده است. مونیه‌ویلیامز آن را «حرکت، پیشروی، روش رفتن، مسیر» معنی کرده و نیز «جایی که کسی بدان رفته است»؛ پس معنای «راه» در نمودار اندکی آزاد است ولی ساخت واژه و پیوند آن با ریشه درست است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\"https://www.wisdomlib.org/definition/yata\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:441\", \"status\": \"supports\",\n       \"note\": \"IEC.txt line 6354: 'Skt. yatàm' heads the list of reflexes of iātos — the node copies Mann exactly.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"IEC\", \"where\": \"Mann col. 441 s.v. iātos, and col. 441 s.v. iaio, iami 'go, ride' (line 6327)\", \"stance\": \"supports\",\n       \"note\": \"'Skt. yami; Av. yai(mi) …' establishes the parent verb from which yāta-/yātam is built.\"},\n      {\"src\": \"POK\", \"where\": \"POK_01.txt line 4246, printed p. 293\", \"stance\": \"supports\",\n       \"note\": \"'Ai. imi, ši, imáh, yánti ‘gehen‘, av. aeiti, yeinti, apers. aitiy ‘geht’' under ei- with the i-ā- extension — the Indic and Iranian y-forms of the verb are Pokorny's too.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 104\", \"stance\": \"partial\",\n       \"note\": \"The ei- article lists the -to-/-tā- nominal formations (ai. itá-, lat. itus) but does not cite yāta- 'road' as such.\"}\n     ]\n    }\n   ]\n  },\n\n  # ------------------------------------------------------------------ entry 6\n  {\n   \"entry\": 6,\n   \"root\": \"leuo, Yewo\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *i̯eu̯o- / *yéwos n. 'grain, cereal', especially 'barley' (Pokorny 512; Watkins yewo-)\",\n   \"note\": \"Pokorny p. 512 heads the article 'i̯eu̯o- ‚Getreide‘, vor allem ‚Gerste‘' and gives precisely the material of this chart: 'Ai. yáva- m. ‚Getreide; Gerste, Hirse‘ = av. yava- m. ‚Getreide‘, npers. jav ‚Gerste‘ (= lit. javai); … hom. att. ζειαί f. Pl. ‚Spelt‘ … WP. I 202 f.' Watkins/AHD: 'yewo-. Grain. Suffixed form *yew-yā in Greek zeia, one-seeded wheat: ZEIN. [Pok. iewo- 512.]' Nourai's two headword spellings are his own I-/Y- doublet for the same *i̯-. EXTRACTION ERROR: the book prints 'Ieuo, Yewo' with a capital I; the JSON has 'leuo'.\",\n   \"note_fa\": \"ریشه درست است: هندواروپایی آغازین ‎*i̯eu̯o-‎ «غله، به‌ویژه جو» (پوکورنی ص ۵۱۲؛ واتکینز yewo-). پوکورنی همان مواد این نمودار را می‌آورد: سنسکریت yáva-، اوستایی yava-، فارسی نو jav/جو، لیتوانی javai و یونانی ζειαί. دو صورت سرواژه (Ieuo و Yewo) هر دو از آنِ نورایی‌اند و یک آوا (*i̯-) را می‌نمایانند. نکته: در کتاب «Ieuo» با I بزرگ چاپ شده و «leuo» در داده‌ها خطای خوانش اسکن است. ادعای نورایی در این ریشه درست است.\",\n   \"error_in\": \"extraction\",\n   \"book_prints\": \"Ieuo, Yewo (capital I)\",\n   \"correct_form\": \"Ieuo, Yewo\",\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/y%C3%A9wos\", W + \"Reconstruction:Proto-Iranian/y%C3%A1wah\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:512\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt line 2546 (the printed page 513 marker follows 16 lines later, so this is p. 512): 'ieuo- ,Getreide‘, vor allem ,Gerste‘. Ai. ydva- m. ,Getreide; Gerste, Hirse‘ = av. yava- m. ,Getreide‘, npers. jav ,Gerste‘ (= lit. javai) … hom. att. ζειαί f. Pl. ,Spelt‘ … WP. I 202 f.'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, AHD_watkins1985.txt line 1200\", \"stance\": \"supports\",\n     \"note\": \"'yewo-. Grain. Suffixed form *yew-ya in Greek zeia, one-seeded wheat: ZEIN. [Pok. iewo- 512.]' — same root, same Pokorny page.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I pp. 202-203 (WLD_Bd1_pages.txt line 18610)\", \"stance\": \"supports\",\n     \"note\": \"'ieuo- ‚Getreide‘ oder ‚eine Getreideart“. Ai. yava- m. ‚Getreide; Gerste, Hirse“ = av. yava- m. ‚Getreide“, npers. jav ‚Gerste“ (= lit. javai)…'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 8.42 GRAIN, printed p. 513 (SYN.txt lines 12928-12931)\", \"stance\": \"supports\",\n     \"note\": \"'Skt. yava- ‘grain’ in RV, later ‘barley’; Av. yava- ‘grain’, NPers. jav ‘barley’; Lith. javai (pl.) ‘grain’; Grk. ζειαί (pl.) ‘spelt’.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"yava\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Av. yava- m. 'grain' is the direct continuation of PIE *i̯eu̯o- with no change: PIE *y- is kept as Avestan y-, the intervocalic *-w- as -v-, the thematic *-os as -ō/-a-. It is attested in the Vidēvdād (V. 3.32 'yat̰ yavō pouru bavāt̰ …' 'so that the grain may grow abundantly'), and its derivatives yavan-/yavin- 'grain field' and yavaŋha- 'pasture' are built on it. The exact equation Skt. yáva- = Av. yava- = Lith. javas is one of the oldest agricultural equations of Indo-European.\",\n     \"derivation_fa\": \"«yava-» اوستایی بازماندهٔ بی‌واسطهٔ ‎*i̯eu̯o-‎ هندواروپایی است و هیچ دگرگونی آوایی چشمگیری نیافته: y آغازین، v میان‌واکه‌ای و پایانهٔ ستاکی ‎-a-‎ همه بر جای مانده‌اند. در وندیداد (فرگرد ۳ بند ۳۲) آمده است و مشتقاتی چون yavan-/yavin- «کشتزار غله» از آن ساخته شده است. برابری سنسکریت yáva- = اوستایی yava- = لیتوانی javas از کهن‌ترین برابری‌های کشاورزی هندواروپایی است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"Reconstruction:Proto-Iranian/y%C3%A1wah\", W + \"Reconstruction:Proto-Indo-European/y%C3%A9wos\"],\n     \"ref_check\": [\n      {\"ref\": \"SYN:513\", \"status\": \"supports\",\n       \"note\": \"Buck p. 513 (SYN.txt 12928-12931): under 8.42 GRAIN, 'Av. yava-' is listed in the table and glossed 'Av. yava- ‘grain’' in the commentary — exactly the node's word and gloss.\"},\n      {\"ref\": \"POK:512\", \"status\": \"supports\",\n       \"note\": \"POK_02.txt 2546-2547: '= av. yava- m. ,Getreide‘'.\"},\n      {\"ref\": \"KLN:1766\", \"status\": \"supports\",\n       \"note\": \"Klein s.v. Zea (KLN_1971.txt line 270323): Greek ζειαί 'is cogn. with OI. yavah, Avestic yava-, ‘corn, grain’, Lith. javai, Ir. eorna ‘barley’' — the same Avestan form, and the page in the 2-vol edition is 1766 (final z-quire).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW col. 1265 (BRT.txt line 21314)\", \"stance\": \"supports\",\n       \"note\": \"'j. yava- m. ‘Getreide’: yat̰ °vō pouru bavāt̰ … ‚damit das Getreide reichlich wachse‘ V. 3.32'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 8.42, p. 513\", \"stance\": \"supports\",\n       \"note\": \"'Av. yava- (dāna-, hahya-)' in the word table for 'grain'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha, [pdf page 213] s.v. جو (گونه‌ای غله)\", \"stance\": \"supports\",\n       \"note\": \"The entry lists اوستایی YAVA, پهلوی JAV/JAW, سانسکریت YAVA, یونانی ZEIAI, لیتوانی JAVAI — an independent modern Persian handbook reproducing the whole chart.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"jav\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old Iranian *yava- > Middle Persian jaw 'barley': the Old Iranian initial *y- became the affricate ǰ- in Middle Persian (as in *yāma- > ǰām, *yuwan- > ǰuwān), and final *-a of the thematic stem was lost, while *-av- stayed as the diphthong -aw. MacKenzie writes it jaw and notes that it is usually spelled with the Aramaic ideogram ŠʿR (Aram. śeʿārā 'barley'), the Pahlavi letters ywd being used in the derived jawēn 'made of barley'. Mo'in's footnote in Borhan-e Qateʿ gives the same chain (Avestan yava- > Pahlavi jav > Persian جو).\",\n     \"derivation_fa\": \"ایرانی باستان ‎*yava-‎ در فارسی میانه به «jaw/jav» بدل شده است: ی آغازینِ ایرانی باستان در فارسی میانه به ج (واکِ سایشی‌ـ‌انسدادی) تبدیل می‌شود (مانند ‎*yāma-‎ > ǰām و ‎*yuwan-‎ > ǰuwān) و پایانهٔ ستاکی ‎-a‎ می‌افتد. مکنزی آن را jaw می‌نویسد و یادآور می‌شود که در پهلوی معمولاً با هُزوارش آرامی ŠʿR نوشته می‌شود. حاشیهٔ معین بر برهان قاطع نیز همین زنجیره را می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D8%AC%D9%88\", W + \"Reconstruction:Proto-Iranian/y%C3%A1wah\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:594\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ ed. Moʿin, vol. 2, the entry «جو» with Moʿin's footnote 3: 'اوستا yava- (گندم) … پهلوی jav … هندی باستان yava- … کردی … استی …'. In BQT_v2_pages.txt this is leaf 52; the vol.-2 offset is printed = leaf + 542 (verified by the catch-lines 'بقیه در صفحهٔ ۵۸۴' at the foot of leaf 41 and 'بقیه از صفحهٔ ۵۸۴' at the head of leaf 42), so leaf 52 = printed p. 594 — Nourai's citation is exact. (NB: refs_online.json currently records +540 for this stretch of vol. 2; it is +542 here.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. jaw (PHD.txt line 412)\", \"stance\": \"supports\",\n       \"note\": \"'jaw [ŠʿR < A šʿr | N ~] barley'; and line 414 'jawēn [ŠʿRyn’ | N jawin] made of barley'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep 'jaw' returns only English 'jaw' in translations of zanak etc.; the glossary of Nyberg's selected texts happens not to contain the word for barley.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur [pdf page 213] s.v. جو\", \"stance\": \"supports\",\n       \"note\": \"'پهلوی: JAV, JAW' listed beside Avestan YAVA.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"jo «جو»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"MP jaw > NP جو, pronounced jow/jō: the Middle Persian final -aw was written جو and is realised as the diphthong ow in standard New Persian (Hübschmann: 'Auslautendes av wird au (ou) gesprochen: jau ‘Gerste’'), whence the two transcriptions jav (Pokorny, Buck) and jo (Nourai). Cognate dialect forms confirm the chain: Kurdish je/jo, Ossetic jäw 'millet', Balochi jō/jav, Pashto ǰaw. The Saʿdi verse quoted in the chart ('که جو کشته گندم نخواهد دِرُود') is the standard proverb attesting the word in classical Persian.\",\n     \"derivation_fa\": \"«جو» فارسی نو دنبالهٔ jaw فارسی میانه است؛ ‎-aw‎ پایانی در فارسی نو به دوواکهٔ «ow» گفته می‌شود (هوبشمان: «av پایانی au/ou تلفظ می‌شود: jau ‘جو’») و از همین‌جاست دو گونهٔ آوانگاری jav (پوکورنی و باک) و jo (نورایی). صورت‌های گویشی نیز زنجیره را تأیید می‌کنند: کردی je/jo، آسی jäw «ارزن»، بلوچی jō/jav، پشتو ǰaw. بیت سعدی که در نمودار آمده گواه کاربرد کلاسیک واژه است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D8%AC%D9%88\", W + \"Reconstruction:Proto-Iranian/y%C3%A1wah\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:594\", \"status\": \"supports\",\n       \"note\": \"Same page as node 2: the Borhan headword is «جو … غله است معروف که به اسب و استر و امثال آن دهند», and Moʿin's footnote derives it from Avestan yava- through Pahlavi jav (BQT_v2_pages.txt leaf 52 = printed 594).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt line 5831)\", \"stance\": \"supports\",\n       \"note\": \"'Auslautendes av wird au (ou) gesprochen: jau ‘Gerste’ (afgh. jau) H. 428' — Hübschmann's phonological rule for exactly this word.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt lines 3979-3980)\", \"stance\": \"supports\",\n       \"note\": \"'kurd. je, jau, yō (H.-Sch.); oss. yau, yäu, yeu ‘Hirse’ (147); bal. jō, jav, n. jau ‘Gerste’ (179)' — Horn no. 428's dialect material.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur [pdf page 213], headword جو (گونه‌ای غله), citing برهان قاطع\", \"stance\": \"supports\",\n       \"note\": \"Independent modern Persian root-dictionary giving Avestan YAVA / Pahlavi JAV / Sanskrit YAVA / Greek ZEIAI for جو.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"yw\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian, unlike Persian, keeps Old Iranian initial *y- unchanged, so *yava- appears as yw /yaw/ 'barley' (Manichaean and Sogdian-script attestations; locative ywyʾ). The node's arrow from the Avestan word is really a sister relation — Sogdian yw and Av. yava- both continue Proto-Iranian *yáwah — but Gharib herself derives the Sogdian word 'from Av. yava', which is what Nourai has drawn.\",\n     \"derivation_fa\": \"سغدی برخلاف فارسی، «ی» آغازینِ ایرانی باستان را نگاه می‌دارد؛ از این رو ‎*yava-‎ در سغدی به‌صورت yw (yaw) «جو» درمی‌آید (در خط سغدی و مانوی، با صورت مکانی ywyʾ). به دقت، سغدی yw و اوستایی yava- هر دو دنبالهٔ ایرانی آغازین ‎*yáwah‎ هستند و رابطهٔ آنها هم‌ریشگی است نه اشتقاق؛ ولی قریب نیز در واژه‌نامهٔ خود آن را «از اوستایی yava» گرفته است و نورایی همان را رسم کرده است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"Reconstruction:Proto-Iranian/y%C3%A1wah\"],\n     \"ref_check\": [\n      {\"ref\": \"SOD:448\", \"status\": \"supports\",\n       \"note\": \"Gharib, Sogdian Dictionary entry 11030 (SOD.txt line 82783), which falls on printed p. 448 (the page numeral '448' stands at line 82631 and '449' immediately after the entry): 'yw- M, S — yaw ©<Av. yava — bar[l]ey — GMS 519; ywʾ, MDii p215; loc. ywyʾ GMS 1183'. So SOD:448 is a page number, not an entry number (entry 448 is ʾzytk).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib no. 11030, p. 448\", \"stance\": \"supports\",\n       \"note\": \"quoted above: 'yaw © < Av. yava … barley'.\"},\n      {\"src\": \"POK\", \"where\": \"POK_02.txt p. 512\", \"stance\": \"silent\",\n       \"note\": \"Pokorny's i̯eu̯o- article cites Indic, Avestan, New Persian and Lithuanian but no Sogdian.\"},\n      {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka\", \"stance\": \"silent\",\n       \"note\": \"grep 'yava'/'barley' finds no Khotanese reflex of *yava- to compare; Wiktionary's Proto-Iranian *yáwah page likewise lists Sogdian ywy but no Khotanese.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Greek\", \"words\": \"zeiai\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Greek ζειαί (pl.; later sg. ζειά, ζεά) 'one-seeded wheat, spelt' continues a suffixed *i̯ew-i̯ā: PIE initial *y- regularly becomes Greek ζ- (as in *yugom > ζυγόν, *yes- > ζέω), and the *-i̯ā suffix gives -ειᾰ. Homeric and Attic; the derivative ζείδωρος 'grain-giving' (< *ζεϝι-δωρος) shows the original digamma. It is a sister of, not a descendant of, the Indo-Iranian forms, which is how the chart draws it (straight from the root box).\",\n     \"derivation_fa\": \"یونانی ζειαί (جمع؛ بعدها مفرد ζειά/ζεά) «گندمِ تک‌دانه، اسپلت» دنبالهٔ ‎*i̯ew-i̯ā‎ است: ‎*y-‎ آغازینِ هندواروپایی در یونانی با قاعده به ζ بدل می‌شود (مانند ‎*yugom‎ > ζυγόν) و پسوند ‎*-i̯ā‎ به ‎-ειᾰ‎ می‌انجامد. صفت هومری ζείδωρος «غله‌بخش» (از ‎*ζεϝι-δωρος‎) نشان‌دهندهٔ واکِ w کهن است. این واژه هم‌ریشهٔ صورت‌های هندوایرانی است نه برآمده از آنها، و نمودار نیز درست آن را مستقیماً از ریشه رسم کرده است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/y%C3%A9wos\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 1200): 'yewo-. Grain. Suffixed form *yew-ya in Greek zeia, one-seeded wheat: ZEIN. [Pok. iewo- 512.]' — Nourai's un-paginated 'AHD' citation is verifiable and exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"POK_02.txt line 2548, printed p. 512\", \"stance\": \"supports\",\n       \"note\": \"'hom. att. ζειαί f. Pl. ,Spelt‘, hom. ζείδωρος ,Getreide hervorbringend‘ (für *ζεϝιδωρος)'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck p. 513 (8.42)\", \"stance\": \"supports\",\n       \"note\": \"'Grk. ζειαί (pl.) ‘spelt’' listed with Skt. yava-, Av. yava-, NPers. jav, Lith. javai.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. Zea (KLN_1971.txt 270323-270327)\", \"stance\": \"supports\",\n       \"note\": \"'Gk. ζειαί (later also in the sing. ζεια, ζεά), ‘one-seeded wheat’, which is cogn. with OI. yavah, Avestic yava-, ‘corn, grain’'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"zea\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English Zea, the Linnaean genus name of maize (Zea mays, 1753), is Modern Latin taken from Latin zea 'a kind of grain, spelt', itself a borrowing of Greek ζειά/ζειαί. The chart's arrow Greek → English is right but compresses one step (Gk. ζειά > L. zea > ModL. Zea); English also has the derived chemical term zein from the same base.\",\n     \"derivation_fa\": \"«Zea» انگلیسی نام جنسِ لینه‌ای ذرت (Zea mays، ۱۷۵۳) است و از لاتین نو گرفته شده که خود از لاتین zea «نوعی غله، اسپلت» و آن از یونانی ζειά/ζειαί است. پیکان نمودار (یونانی ← انگلیسی) درست است اما یک حلقه (لاتین) را نادیده می‌گیرد. واژهٔ شیمیایی zein نیز از همین بن ساخته شده است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/y%C3%A9wos\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1766\", \"status\": \"supports\",\n       \"note\": \"Klein, s.v. Zea (KLN_1971.txt line 270323, = p. 1766 of the 1966-67 two-volume edition, in the final z-quire): 'Zea, n., a genus of grasses (bot.) — ModL., adopted by the Swedish botanist Carolus Linnaeus (1707-78) fr. L. zea, ‘a kind of grain’, fr. Gk. ζειαί … cogn. with OI. yavah, Avestic yava-…'. The local OCR of the 1966 volume 2 breaks off at 'veratrine', so the entry was read in the 1971 one-volume reprint of the same text.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 line 1200\", \"stance\": \"supports\",\n       \"note\": \"cites ZEIN (from the same Greek word) as the English descendant of yewo-.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary vol. 4 (FSD_vol4.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep 'Zea' in the z-quire returns only 'New Zealand' compounds; the OCR of the genus entry is not recoverable.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\",\n       \"note\": \"no entry zea (Skeat omits Modern-Latin botanical genus names).\"}\n     ]\n    }\n   ]\n  },\n\n  # ------------------------------------------------------------------ entry 7\n  {\n   \"entry\": 7,\n   \"root\": \"Ijlak, Yelek\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Turkish yelek 'waistcoat, sleeveless jacket' (Ottoman یلك; Old Anatolian Turkish yélek, from Proto-Turkic *yẹl 'wind' + -ek)\",\n   \"note\": \"The etymon is right and well documented: Klein p. 656 s.v. gilet ends 'ult. fr. Turk. yelek', and Lokotsch no. 951 (p. 76) heads the whole European family 'Tk. jelek: ‘Weste‘ [Dozy Vêt. 431]'. Wiktionary derives Turkish yelek from Old Anatolian Turkish yélek, ultimately Proto-Turkic *yẹl 'wind'. The first of Nourai's two headword forms, 'Ijlak', is not found in any Turkic or European source consulted (Klein, Lokotsch, Vámbéry's list of stems as quoted by Lokotsch, Wiktionary): it appears to be Nourai's own variant transcription, and no reading of the printed page can rescue it — the page (see data/verification/sources/refs/ocr/BOOK/226.png) plainly shows 'Ijlak, Yelek'. Note that the initial letter here is the same capital I used in the other root headwords on the page, and that the OCR read it correctly in this one case.\",\n   \"note_fa\": \"بن این خانواده درست است: ترکی «یلک» (yelek) «جلیقه، جامهٔ بی‌آستین»؛ کلاین (ص ۶۵۶) در پایان مدخل gilet می‌نویسد «سرانجام از ترکی yelek» و لوکوچ (شمارهٔ ۹۵۱، ص ۷۶) کل خانوادهٔ اروپایی را زیر «tk. jelek ‘Weste’» می‌آورد؛ ویکی‌واژه آن را از ترکی آناتولیایی کهن yélek و در نهایت از ترکی آغازین ‎*yẹl‎ «باد» می‌داند. اما صورت نخستِ سرواژه، «Ijlak»، در هیچ‌یک از منابع ترکی و اروپاییِ بررسی‌شده یافت نشد و ظاهراً گونه‌نویسیِ خودِ نورایی است؛ تصویر صفحهٔ چاپی نیز همین «Ijlak» را نشان می‌دهد، پس خطای خوانش اسکن در کار نیست. ادعای نورایی دربارهٔ «Yelek» درست و دربارهٔ «Ijlak» تأییدنشدنی است.\",\n   \"sources\": [W + \"yelek\", W + \"gilet\"],\n   \"ref_check\": [\n    {\"ref\": \"KLN:656\", \"status\": \"supports\",\n     \"note\": \"Klein (KLN_1966.txt line 16144, between the OCR page marks 651 and 658, i.e. p. 656): 'gilet, n., a waistcoat. — F., fr. Sp. jileco, gileco (the modern Sp. form is chaleco), fr. Algerian Arab. jaleco, ‘coat of Christians in Moorish captivity’, ult. fr. Turk. yelek.' The whole of entry 7 — Turkish root, Arabic 'jaleco' with its gloss, Spanish, French, English — is copied from this one entry.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 951, printed p. 76 (LKT.txt line 2281)\", \"stance\": \"partial\",\n     \"note\": \"'Tk. jelek: ‘Weste‘ [Dozy Vetcin 431]; hieraus alt-it. giulecco, sp. gileco, joleco, chaleco, pg. jaleco, prov. gileco, frz. gilet, it. gilè ‘Weste‘, rum. ilic …' — same Turkish etymon, but Lokotsch treats jaleco as PORTUGUESE and inserts no Arabic stage.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein p. 656 s.v. gilet\", \"stance\": \"supports\",\n     \"note\": \"'ult. fr. Turk. yelek'.\"},\n    {\"src\": \"TTS\", \"where\": \"Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen\", \"stance\": \"silent\",\n     \"note\": \"only the PDF and a pages file are on disk (no usable djvu text); Lokotsch's citations of Vámbéry (stem jil, jel 'Wind', no. 1421) cover the same ground and give no form 'ijlak'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"jalîtqeh «جلیتقه ( جلیقه )»\", \"verdict\": \"plausible\",\n     \"derivation\": \"Persian جلیقه jaliqe 'sleeveless waistcoat' does go back to Turkish yelek, but through Arabic: Ottoman/Turkish yelek was taken into Arabic as جَلِيقة jalīqa (the Turkish y- being rendered by Arabic ǧ- and the word re-shaped on the pattern of the fem. nouns used for European garments), and Persian borrowed the Arabic form; the archaic variant جلیتقه jelitqe printed by Nourai — with an intrusive -t- — is recorded by Wiktionary beside the dialect forms جلیدقه and جلزقه. Nourai's arrow (Turkish → Persian, direct) therefore telescopes a real Arabic stage. Moʿin's footnote in Borhan-e Qateʿ, citing Foroughi, offers a third account ('از ترکی از فرانسه' — from Turkish, which he took from French gilet), i.e. a return loan.\",\n     \"derivation_fa\": \"«جلیقه» فارسی سرانجام به ترکی yelek بازمی‌گردد، اما نه بی‌واسطه: ترکی عثمانی yelek نخست در عربی به‌صورت «جَلِيقة» درآمد (یِ ترکی به ج بدل شد و واژه بر وزن نام‌های مؤنثِ جامه‌های فرنگی ریخته شد) و فارسی صورت عربی را وام گرفت؛ گونهٔ کهنِ «جلیتقه» با تِ میانجی که نورایی آورده در ویکی‌واژه در کنار «جلیدقه» و «جلزقه» ثبت شده است. بنابراین پیکانِ مستقیمِ ترکی ← فارسی یک حلقهٔ عربی را نادیده می‌گیرد. معین در حاشیهٔ برهان قاطع به نقل از فروغی روایت سومی می‌آورد: «از ترکی، از فرانسه [gilet]»، یعنی وام‌گیریِ بازگشتی. ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"%D8%AC%D9%84%DB%8C%D9%82%D9%87\", W + \"yelek\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:584\", \"status\": \"partial\",\n       \"note\": \"Borhan-e Qateʿ ed. Moʿin, vol. 2 p. 584 (archive.org borhan-ghate-v2 full-text search, page index 42 = BQT_v2_pages.txt leaf 42; the foot of leaf 41 carries 'بقیه در صفحهٔ ۵۸۴' and this footnote block opens 'بقیه از صفحهٔ ۵۸۴', which fixes the offset printed = leaf + 542): '* جلیقه = جلیقه بکسر اول و فتح پنجم، از ترکی از فران[سه] … «محمد علی فروغی، فرهنگ زبانهای بیگانه در زبان فارسی، آموزش و پرورش ۵: ص ۳۸»؛ جامهٔ کوتاه و بی‌آستین که روی پیراهن و زیر نیم‌تنه پوشند.' So the page really does carry the word and a Turkish source, but spells it جلیقه (not جلیتقه) and adds a French origin behind the Turkish.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 2 p. 584, Moʿin's footnote, quoting Foroughi\", \"stance\": \"partial\",\n       \"note\": \"'از ترکی از فرانسه' — Turkish, itself from French; the definition 'جامهٔ کوتاه و بی‌آستین' matches the chart's gloss 'waist coat without sleeves'.\"},\n      {\"src\": \"MON\", \"where\": \"Wiktionary's Persian entry جلیقه (which cites Persian lexicography)\", \"stance\": \"partial\",\n       \"note\": \"'Borrowed from Arabic جَلِيقة (jalīqa), from Turkish yelek … Archaic alternative form جلیتقه (jelitqe), dialectal جلیدقه, جلزقه' — confirms Nourai's variant spelling but inserts Arabic between Turkish and Persian.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 951\", \"stance\": \"silent\",\n       \"note\": \"Lokotsch traces the European reflexes of tk. jelek but does not treat the Persian word.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Arabic\", \"words\": \"jaleco\", \"verdict\": \"disputed\",\n     \"derivation\": \"The node copies Klein p. 656 exactly ('Algerian Arab. jaleco, ‘coat of Christians in Moorish captivity’'), and Klein in turn takes it from Dozy's Dictionnaire détaillé des noms des vêtements chez les Arabes p. 431. Two things are wrong with it as drawn. (a) The form: 'jaleco' is a Spanish/Portuguese spelling, not an Arabic one; the Maghrebi Arabic word is جليكة ǧalīka / ǧellīka. (b) The direction: modern scholarship reverses the arrow. The OED explicitly rejects derivation of gilet from Arabic and takes Algerian Arabic to have borrowed the word from Italian; Wiktionary's Turkish yelek entry likewise routes the European forms through southern Italian (Calabrian gileccu, Genoese gilecco, Neapolitan gelecco) with Algerian Arabic as a recipient; and Lokotsch no. 951 passes straight from Turkish jelek to Italian, Spanish and Portuguese with no Arabic link at all. Pihan's older guess (French gilet from Arabic جلد jild 'hide') is a third, now abandoned, proposal.\",\n     \"derivation_fa\": \"این گره واژه‌به‌واژه از کلاین (ص ۶۵۶) گرفته شده است: «عربی الجزایری jaleco «جامهٔ مسیحیانِ اسیر»»، و کلاین خود آن را از دوزی (فرهنگ نام‌های جامه نزد عرب، ص ۴۳۱) دارد. دو اشکال هست: نخست آنکه «jaleco» املای اسپانیایی/پرتغالی است نه عربی؛ صورت عربیِ مغربی «جلّیکة» است. دوم آنکه جهت وام‌گیری در پژوهش امروزی وارونه است: فرهنگ آکسفورد صراحتاً ریشهٔ عربی را برای gilet رد می‌کند و عربیِ الجزایر را وام‌گیرنده از ایتالیایی می‌داند؛ ویکی‌واژه نیز راه اروپایی را از گویش‌های ایتالیای جنوبی (gileccu، gilecco، gelecco) می‌گذراند و لوکوچ (شمارهٔ ۹۵۱) اصلاً حلقهٔ عربی ندارد. پس پژوهش امروزی این گره را رد می‌کند.\",\n     \"sources\": [W + \"gilet\", W + \"yelek\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:656\", \"status\": \"supports\",\n       \"note\": \"Klein p. 656: '… fr. Algerian Arab. jaleco, ‘coat of Christians in Moorish captivity’, ult. fr. Turk. yelek' — the chart's word and gloss are Klein's own, so Nourai cites accurately; the problem is with Klein, not with the citation.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 951, p. 76\", \"stance\": \"contradicts\",\n       \"note\": \"'Tk. jelek … hieraus alt-it. giulecco, sp. gileco, joleco, chaleco, pg. jaleco, prov. gileco, frz. gilet' — jaleco is Portuguese here and there is no Arabic intermediary.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein p. 656\", \"stance\": \"supports\",\n       \"note\": \"the source of the node, quoted above.\"},\n      {\"src\": \"PHN\", \"where\": \"Pihan, Dictionnaire étymologique … dérivés de l'arabe, s.v. GILET, p. 181 (PHN.txt line 5324)\", \"stance\": \"contradicts\",\n       \"note\": \"'GILET, s. m. (a.) [djild et djilid] peau, cuir d’un animal … L’analogie d’orthographe et de signification que présente le mot français gilet avec son correspondant arabe djilid me porte à croire qu’il vient de ce dernier' — a different (and now discarded) Arabic etymon, and no 'jaleco'.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale\", \"stance\": \"silent\",\n       \"note\": \"grep 'gilet' in DEV.txt returns nothing: Devic does not admit gilet among French words of Oriental origin.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Spanish\", \"words\": \"\", \"verdict\": \"plausible\",\n     \"derivation\": \"Pass-through node: the Spanish word is jileco/gileco, modern chaleco 'waistcoat' (Klein p. 656 supplies all three forms; Lokotsch adds joleco). Its existence and meaning are not in doubt; only its immediate source is — Klein and Dozy have it from Maghrebi Arabic, whereas OED and Wiktionary derive Spanish chaleco from Italian dialect gilecco/giulecco, itself from Turkish yelek. Either way the Turkish etymon at the head of the chart stands.\",\n     \"derivation_fa\": \"گرهٔ گذرا و بی‌واژه: صورت اسپانیایی jileco/gileco و امروزه chaleco «جلیقه» است (کلاین هر سه را می‌آورد و لوکوچ joleco را نیز می‌افزاید). وجود و معنای واژه محل تردید نیست؛ آنچه محل بحث است سرچشمهٔ بی‌واسطهٔ آن است: کلاین و دوزی آن را از عربی مغربی می‌گیرند، اما فرهنگ آکسفورد و ویکی‌واژه از گویش‌های ایتالیایی (gilecco/giulecco) و آن‌ها از ترکی yelek. در هر دو روایت، بنِ ترکیِ بالای نمودار بر جای می‌ماند. با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"gilet\", W + \"yelek\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference of its own; the parent's KLN:656 covers it ('fr. Sp. jileco, gileco (the modern Sp. form is chaleco)').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein p. 656 s.v. gilet\", \"stance\": \"supports\",\n       \"note\": \"'F., fr. Sp. jileco, gileco (the modern Sp. form is chaleco)'.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 951, p. 76\", \"stance\": \"partial\",\n       \"note\": \"'sp. gileco, joleco, chaleco' — the Spanish forms are there, but taken directly from Turkish via old Italian.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"plausible\",\n     \"derivation\": \"Pass-through node: French gilet 'waistcoat', in French since the 18th century. Klein derives it from Spanish jileco/gileco, which is the route drawn here; the OED and Wiktionary instead take it from southern Italian gilecco (Genoese) / giulecco, and Lokotsch lists it in the same series as the Italian and Iberian forms without ordering them. Ménage's old derivation from the personal name Gilles (a fairground character) is rejected by all of these.\",\n     \"derivation_fa\": \"گرهٔ گذرا و بی‌واژه: فرانسهٔ gilet «جلیقه» که از سدهٔ هجدهم در فرانسه به‌کار رفته است. کلاین آن را از اسپانیایی jileco/gileco می‌گیرد و نمودار همین راه را رسم کرده است؛ اما فرهنگ آکسفورد و ویکی‌واژه آن را از گویش ایتالیایی جنوبی gilecco/giulecco می‌دانند و لوکوچ صورت‌های ایتالیایی و ایبریایی و فرانسوی را در یک ردیف و بدون ترتیب می‌آورد. ریشه‌شناسی کهن مِناژ (از نام خاص Gilles) را همهٔ این منابع رد کرده‌اند. با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"gilet\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No reference on the node; the parent KLN:656 supplies the step 'F., fr. Sp. jileco, gileco'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein p. 656\", \"stance\": \"supports\",\n       \"note\": \"'gilet, n., a waistcoat. — F., fr. Sp. jileco, gileco …'\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 951, p. 76, with the note on Ménage\", \"stance\": \"partial\",\n       \"note\": \"'frz. gilet' in the series from tk. jelek; the bracketed note reports and dismisses Ménage's derivation of gilet from the name Gilles < Aegidius.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary vol. 1 (WEB_vol1.txt line 81764)\", \"stance\": \"partial\",\n       \"note\": \"'gilet (zhē-lā’), n. [Fr., …] a waistcoat or vest; especially, the front of a bodice' — records the French word and its English use but gives no oriental source.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\", \"words\": \"žîlet «ژیلت ( ژیله )»\", \"verdict\": \"plausible\",\n     \"derivation\": \"A 20th-century European loan: French gilet was taken into Persian as ژیله žile, which Moʿin tags [فر.] and defines 'نوعی لباس بدون آستین جلو بسته شبیه بلوز'. The chart's headword form ژیلت žilet, however, is in current Persian normally the safety razor, from the trade name Gillette, and only secondarily (and by confusion with ژیله) the garment; Nourai's parenthesis '( ژیله )' shows that he knew the garment form. The reference VOP:206 (Moshiri, Farhang-e vazheha-ye orupayi dar farsi) could not be checked — no copy of the book is available anywhere online.\",\n     \"derivation_fa\": \"وام‌واژه‌ای اروپایی از سدهٔ بیستم: فرانسهٔ gilet در فارسی «ژیله» شده است و معین آن را [فر.] نشانه‌گذاری کرده و «نوعی لباس بدون آستین جلو بسته شبیه بلوز» معنی کرده است. اما صورت سرواژهٔ نمودار، «ژیلت»، در فارسی امروز بیشتر به تیغِ صورت‌تراشی گفته می‌شود که از نام تجاری Gillette آمده است و تنها به سببِ آمیختگی با «ژیله» گاه به معنای جامه به کار می‌رود؛ پرانتزِ خودِ نورایی «( ژیله )» نشان می‌دهد که او از صورت درست آگاه بوده است. مأخذ VOP:206 (فرهنگ واژه‌های اروپایی در فارسی، مهشید مشیری) در دسترس نیست. با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%DA%98%DB%8C%D9%84%D9%87/\", W + \"gilet\"],\n     \"ref_check\": [\n      {\"ref\": \"VOP:206\", \"status\": \"not_checked\",\n       \"note\": \"Moshiri, Farhang-e vazheha-ye orupayi dar farsi (Alborz 1371) — refs_online.json records 'kind: none': not on archive.org, ketabnak, noorlib or the open web.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Moʿin s.v. ژیله (abadis.ir/fatofa/ژیله)\", \"stance\": \"supports\",\n       \"note\": \"'[فر.] نوعی لباس بدون آستین جلو بسته شبیه بلوز' — the French origin of the Persian garment word is Moʿin's.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein p. 656 s.v. gilet\", \"stance\": \"supports\",\n       \"note\": \"supplies the French source form that Persian borrowed.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"gilet\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English gilet 'a waistcoat; the front of a bodice' is a straight 19th-century borrowing of French gilet, still pronounced in the French way (Webster: 'gilet (zhē-lā), n. [Fr.]'). Klein's entry, the chart's own reference, is headed exactly 'gilet, n., a waistcoat. — F.'\",\n     \"derivation_fa\": \"انگلیسی gilet «جلیقه؛ پیش‌سینهٔ بالاتنه» وام مستقیمِ سدهٔ نوزدهم از فرانسهٔ gilet است و هنوز به شیوهٔ فرانسوی تلفظ می‌شود (وبستر: «gilet (zhē-lā)، [فرانسه]»). مدخل کلاین که خودِ مأخذ نمودار است دقیقاً چنین آغاز می‌شود: «gilet, n., a waistcoat. — F.». ادعای نورایی درست است.\",\n     \"sources\": [W + \"gilet\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:656\", \"status\": \"supports\",\n       \"note\": \"Klein p. 656: 'gilet, n., a waistcoat. — F., fr. Sp. jileco, gileco …' — English from French, exactly as drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary vol. 1 (WEB_vol1.txt line 81764)\", \"stance\": \"supports\",\n       \"note\": \"'gilet (zhē-lā’), n. [Fr., …] a waistcoat or vest; especially, the front of a bodice.'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein p. 656\", \"stance\": \"supports\",\n       \"note\": \"as quoted.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\",\n       \"note\": \"no entry gilet (Skeat omits recent unnaturalised French loans).\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-226.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\nprint(\"ok\")\n"
}
```


### [2026-09-06T15:40:20.676Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk226.py (file state is current in your context — no need to Read it back)
```


## [2026-09-06T15:40:25.828Z] TOOL CALL #99: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk226.py && python3 -m json.tool data/verification/page-226.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 226"
}
```


### [2026-09-06T15:40:31.714Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 15/15
node verdicts: {'plausible': 5, 'disputed': 2, 'confirmed': 8}
root verdicts: {'plausible': 2, 'confirmed': 1}
ref checks: {'supports': 14, 'not_found': 1, 'not_checked': 4, 'partial': 1}
books consulted: {'contradicts': 5, 'silent': 11, 'partial': 7, 'supports': 22} | by book: {'KLN': 6, 'POK': 4, 'LKT': 4, 'MON': 3, 'ARY': 3, 'BRT': 2, 'HRN': 2, 'HUB': 2, 'SYN': 2, 'SKT': 2, 'WEB': 2, 'KNT': 1, 'PLA': 1, 'IEC': 1, 'WLD': 1, 'PHD': 1, 'NYB': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'AHD': 1, 'FSD': 1, 'BQT': 1, 'PHN': 1, 'DEV': 1}
```


## [2026-09-06T15:40:51.687Z] AGENT

Done. `python3 tools/verify_check.py 226` reports **0 PROBLEM lines** (15/15 nodes).

**Page 226 (book p. 196) — 3 chart entries, 15 nodes** (5 redirect stubs skipped)
- Node verdicts: 8 confirmed, 5 plausible, 2 disputed. Root verdicts: 1 confirmed (*Ieuo/Yewo*), 2 plausible (*Iâtos*, *Ijlak/Yelek*).
- Ref checks: 14 supports, 1 partial, 1 not_found, 4 not_checked.

**disputed**
- *Iâtos* #2 — Persian **jâddeh جادّه**: modern view is Arabic جادّة (fem. act. part. of جدّ, root ج د د, pl. جوادّ); Moʿin and Dehkhoda both tag it [ع.], Wiktionary "borrowed from Arabic". Horn and Hübschmann have no such Iranian word; Asbaghi (*Persische Lehnwörter im Arabischen*) does not list it as a Persian loan. Mann IEC:441 ("Per. jade 'highway'") is the sole support.
- *Ijlak/Yelek* #2 — Arabic **jaleco**: copied verbatim from Klein 656 ("Algerian Arab. jaleco"), but "jaleco" is a Spanish/Portuguese spelling (Arabic is جليكة), and OED/Wiktionary reverse the arrow — Turkish yelek → southern Italian gileccu → Spanish/French, with Algerian Arabic as recipient. Lokotsch no. 951 (p. 76) has no Arabic stage at all.

**Extraction errors for the owner to fix** (checked against the page image, copied to `data/verification/sources/refs/ocr/BOOK/226.png`)
- Root headwords misread capital **I** as lower-case **l** throughout: `lâtis`, `lâtom`, `lâtos`, `lě`, `lěro`, `leu`, `leuo`, `lo` should be **Iâtis, Iâtom, Iâtos, Iĕ, Iĕro, Ieu, Ieuo, Io** (Nourai's I = PIE *i̯-/y-; proved by his own cross-refs "Iĕ/Iĕro → Ei", "Ieu → Yeu 2", "Io → I 2" and by the alphabetical run Iâ- < Iĕ- < Ieu- < Ij- < Io-). "Ijlak" was read correctly. No error in the node data.

**Reference-file note worth recording**: BQT vol. 2 offset in this stretch is **printed = leaf + 542**, not +540 (fixed by the catch-lines "بقیه در صفحهٔ ۵۸۴"/"بقیه از صفحهٔ ۵۸۴" at leaves 41/42). With that, both BQT:594 (جو, Moʿin's footnote "اوستا yava- … پهلوی jav") and BQT:584 (جلیقه, "از ترکی از فرانسه", citing Foroughi) check out exactly. Also: SOD:448 is a **page**, not an entry number (Gharib no. 11030 "yw- … <Av. yava, barley").
