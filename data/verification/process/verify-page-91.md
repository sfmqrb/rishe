# Verification process log — verify-page-91


## [2026-09-05T13:45:24.120Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 91 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-91.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-91.json. Write /home/sfmqrb/git/rishe/data/verification/page-91.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 91` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T13:45:25.555Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T13:45:26.274Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T13:45:26.288Z] TOOL RESULT

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


## [2026-09-05T13:45:26.462Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-91.txt"
}
```


### [2026-09-05T13:45:26.475Z] TOOL RESULT

```
1	=== PDF page 91 (book page 61) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bher 5, Bheru, Bhereu, Bhreu, Bhru 2 : to boil, bubble  (refs AHD:1510; POK:132,143; IEC:116)
4	#1 (parent #0) [Persian] refs=IEC:116, MON:575 | balvâ «بلوا» : tumult | NOTE: MON:575 claims this is from an Arabic root
5	#2 (parent #0) [Germanic] refs=AHD | breuwan : to brew ; braudam : cooked food, bread ; brudam : broth ; brôd : hatching
6	  #3 (parent #2) [English] refs=AHD | brew ; bread ; broth ; breed
7	#4 (parent #0) [Germanic] refs=AHD | brěthaz : warm air, breath ; bres : burning ; brenw : to burn ; brandaz : a flaming torch
8	  #5 (parent #4) [English] refs=AHD | breath ; braise, breeze ; burn ; brand, Brandy
9	#6 (parent #0) [Latin] refs=AHD | fer-mentum : yeast ; fervere : to be boiling
10	  #7 (parent #6) [English] refs=AHD | ferment ; fervent
11	--- entry 1 ---
12	ROOT bherd -> redirect to Bher 3
13	--- entry 2 ---
14	ROOT [Indo-European] Bhereg, Bhreg : to shine, bright  (refs POK:139)
15	#1 (parent #0) [Avestan] refs=POK:139; BQT:137 | brâz : to shine
16	  #2 (parent #1) [Persian] refs=BQT:247; MON:493 | barâzîdan «برازیدن» : to look nice ; barâzandeh «برازنده» : well suited, fit
17	#3 (parent #0) [Sogdian] refs=SOD:106 | br`z`nt : shining
18	#4 (parent #0) [Germanic] refs=AHD | berhtaz : bright ; berkjôn : white tree, birch ; adel-beraht : bright in nobility (Albert) ☞Âtos
19	  #5 (parent #4) [English] refs=None | bright, Albert, Robert ; birch
20	--- entry 3 ---
21	ROOT Bhereu -> redirect to Bher 5
22	
```


## [2026-09-05T13:45:30.081Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-91.json | head -200",
 "description": "Read page 91 source JSON"
}
```


## [2026-09-05T13:45:30.265Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T13:45:31.883Z] TOOL RESULT

```
{
    "pdf_page": 91,
    "book_page": 61,
    "entries": [
        {
            "root": {
                "name": "Bher 5, Bheru, Bhereu, Bhreu, Bhru 2",
                "lang": "Indo-European",
                "refs": "AHD:1510; POK:132,143; IEC:116",
                "gloss": "to boil, bubble"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "IEC:116, MON:575",
                    "words": [
                        {
                            "translit": "balv\u00e2",
                            "gloss": "tumult",
                            "script": "\u0628\u0644\u0648\u0627"
                        }
                    ],
                    "script_extra": null,
                    "note": "MON:575 claims this is from an Arabic root",
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "breuwan",
                            "gloss": "to brew",
                            "script": null
                        },
                        {
                            "translit": "braudam",
                            "gloss": "cooked food, bread",
                            "script": null
                        },
                        {
                            "translit": "brudam",
                            "gloss": "broth",
                            "script": null
                        },
                        {
                            "translit": "br\u00f4d",
                            "gloss": "hatching",
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
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "brew",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "bread",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "broth",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "breed",
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
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "br\u011bthaz",
                            "gloss": "warm air, breath",
                            "script": null
                        },
                        {
                            "translit": "bres",
                            "gloss": "burning",
                            "script": null
                        },
                        {
                            "translit": "brenw",
                            "gloss": "to burn",
                            "script": null
                        },
                        {
                            "translit": "brandaz",
                            "gloss": "a flaming torch",
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
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "breath",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "braise, breeze",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "burn",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "brand, Brandy",
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
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "fer-mentum",
                            "gloss": "yeast",
                            "script": null
                        },
                        {
                            "translit": "fervere",
                            "gloss": "to be boiling",
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
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "ferment",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "fervent",
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
                "name": "bherd",
                "redirect": "Bher 3"
```


### [2026-09-05T13:45:31.917Z] TOOL RESULT

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


## [2026-09-05T13:45:36.670Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-91.json'))\nprint(json.dumps(d['entries'][2],ensure_ascii=False,indent=1))\nprint(json.dumps(d['entries'][1],ensure_ascii=False,indent=1))\n\"",
 "description": "Print entries 1 and 2"
}
```


### [2026-09-05T13:45:38.423Z] TOOL RESULT

```
{
 "root": {
  "name": "Bhereg, Bhreg",
  "lang": "Indo-European",
  "refs": "POK:139",
  "gloss": "to shine, bright"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Avestan",
   "refs": "POK:139; BQT:137",
   "words": [
    {
     "translit": "brâz",
     "gloss": "to shine",
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
   "refs": "BQT:247; MON:493",
   "words": [
    {
     "translit": "barâzîdan",
     "gloss": "to look nice",
     "script": "برازیدن"
    },
    {
     "translit": "barâzandeh",
     "gloss": "well suited, fit",
     "script": "برازنده"
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 3,
   "parent": 0,
   "lang": "Sogdian",
   "refs": "SOD:106",
   "words": [
    {
     "translit": "br`z`nt",
     "gloss": "shining",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 4,
   "parent": 0,
   "lang": "Germanic",
   "refs": "AHD",
   "words": [
    {
     "translit": "berhtaz",
     "gloss": "bright",
     "script": null
    },
    {
     "translit": "berkjôn",
     "gloss": "white tree, birch",
     "script": null
    },
    {
     "translit": "adel-beraht",
     "gloss": "bright in nobility (Albert)",
     "script": null,
     "see": [
      "Âtos"
     ]
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
   "refs": null,
   "words": [
    {
     "translit": "bright, Albert, Robert",
     "gloss": null,
     "script": null
    },
    {
     "translit": "birch",
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
{
 "root": {
  "name": "bherd",
  "redirect": "Bher 3"
 },
 "nodes": []
}
```


## [2026-09-05T13:45:38.897Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','POK','IEC','MON','BQT','SOD','WLD','KLN','HRN','HUB','SYN','CHEUNG','ARY','PLA','AFM']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600]); print()\n\"",
 "description": "Print ref metadata"
}
```


### [2026-09-05T13:45:40.852Z] TOOL RESULT

```
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

CHEUNG null

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
```


## [2026-09-05T13:45:51.551Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\n# POK_01: leaf = p + 8\nfor p,f in [(132,'POK_01.txt'),(133,'POK_01.txt'),(143,'POK_01.txt'),(144,'POK_01.txt'),(139,'POK_01.txt'),(140,'POK_01.txt')]:\n    pages=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    leaf=p+8\n    print('='*20,'POK p.',p,'leaf',leaf)\n    print(pages[leaf][:3000])\nEOF",
 "description": "Print Pokorny pages 132,139,143"
}
```


### [2026-09-05T13:45:53.400Z] TOOL RESULT

```
==================== POK p. 132 leaf 140
 i.)  glück- brin^-endes  Zauberwesen';  aisl.  PL  harar,  harir,  hqrur  , Bahre',  ags.  hearwe, on^'l.  harroiv,  ostfries.  harwe,  ndl.  herrie  ,Bahre';
debnstufig  ahd.  -häri,  nhd.  -har  (z.  B.  fruchtbar  =  Frucht  bringend, tragend),  ags.  hvbre  (wcestmhcbre  , fruchtbar'),  aisl.  höerr  ,fähig  zum  Tragen, tra<^bar';  abd.  as.  hära,  ags.  hier  f.  , Bahre'  (auch  aisl.  hära,  mengl.  mnd. bare  ,Woge'?  vielleicht  hierher  als  ,die  sich  hebende^,  vgl.  unten  die  Gruppe von  abd.  hurian  ,sicb  erheben');
schwachstufig  got.  haur  ,der  Geborene',  aisl.  hurr,  ags.  hyre  ,Sohn'; got.  gahaur  n.  , Kollekte,  (pöqog,  Steuer',  gahaür  m.  , Festgelage,  Schmaus* (zu  gahairan  ,zusammentragen'),  vakidi.  urhor,  urhar  f.  n.  ,Zins  von  einem Grundstück',  m.  , Zinspflichtiger';  abd.  hör  f.  , oberer  Raum,  Höhe',  ahd. m  hor{e)  ,in  der  Höhe,  in  die  Höhe',  mhd.  enhor[e),  nhd.  empor,  ahd. hurian,  mhd.  6wrn, erheben';  hierher  obd.  Jörnen  , hervorstehen'  =  ags. horettan  , schwingen'  (germ.  *-at{an),  dazu  nhd.  Bürzel  u.  purzeln^  ahd. gihurian,  mhd.  gehilrn  ,sich  ereignen,  geschehen,  rechtlich  zufallen,  gehiihren\ as.  gihurian,  ags.  gehyrian,.  aisl.  hyrja  ,sicb  gehören,  ziemen,  zukommen'^ aisl.  hyrja  auch  , anfangen',  eig.  *,anheben',  ags.  hyre,  gebyre  m.  ,günstige Gelegenheit,  Gelegenheit',  got.  gahaürjaha  adv.  ,gern',  gahaürjöpus  , Wollust'; aus  dem  Begriff  des  »hochgehobenen,  hohen'  entsprang  der  verstärkende Sinn  von  ahd.  hora-,  z.  B.  in  hora-lang  ,sehr  lang',  woneben  o-stufig  as. bar-  in  harwirdig  ,sehr  würdig';  vermutlich  auch  aisl.  hyrr  m.,  ags.  hyre ,günstiger  Wind',  mnd.  hore-los  ,obne  Wind'  als  ,(das  Schiff)  tragend'.
Got.  gahaurps  f.  , Geburt,  Abstammung,  Geschlecht*,  aisl.  hurdr  m.  , Tragen, Gebären,  Geburt',  hyrd  f.  , Geburt',  ags.  gehyrd  f.,  ahd.  gihurt,  as.  gihurd , Geburt',  auch  , Schicksal'  (=  ai.  hhfti-h,  lat.  fors)-  got.  haurpei  ,Bürde, Last',  ahd.  hurdl  f.  ,Bürde',  *hhi'tiön'  :  -tlu]  aisl.  hyrdr,  ags.  hyrpen,  hyrden  ds. Aksl.  herg,  hhrati  (h^rati)  , sammeln,  nehmen',  skr.  herem  hräti  ds.,  russ. berü  hrath  ds.  usw.  (slav.  *h^rat^  trat  an  Stelle  von  älterem  *h^rti  nach dem  Präteritalstamm  bsl.  *hirä-),  aksl.  hr^m^  ,Last,  Bürde',  skr.  hreme, russ.  mdartl.  heremja,  aö.  hfiemä  (*hheo^-men-),  aksl.  ST>-hor7>  , Versamm- lung'; ksl.  hr^£da  , trächtig,  schwanger',  russ.  herezaja  ,trächtig  (von  der btute)*,  skr.  hreda  ds.  von  Kühen  (*hhei^-dia),  im  Formans  ähnlich  lat. forda]  aksl.  hrahno  , Speise,  Nahrung'  s.  unter  hhares-  , Gerste*.
Lit.  hernas  , Jüngling;  Knecht*,  alit.  ,Kind*,  lett.  h^rns  ,Kind*;  wahr- scheinlich lett.  hars  , Haufe,  Menge*.
9*
132
Hierher  mit  Spezialisierung  auf  das  Austragen  des  Samenkorns:  transiti^ lit.  heriüj  heriau,  berti  , streuen'  (vom  
==================== POK p. 133 leaf 141
sche  usw.),  lett.  beru,  bert  ds.,  im  Ablaut  intransitiv  lit.  hyi^ü^  biraii birti  , streuen,  ausfallen*,  lett.   bifstUy   biruj   bift  , ausfallen,  abfallen',   usv^
Toch.  AB  pär-  , tragen,  bringen,  holen',  vielleicht  auch  in  A  kos-prej^ ,wieviel?'  ku-pre  ,wenn',  täprem  ,wenn*,  täpär{k)  ,jetzt',  falls  zu  gr.  li-cpQa  . . ; r6-(pQ(x  , solange  als'  (S.  129).  Über  hitt.  bar-ah-zi  ,jagt'  s.  Pedersen  Hitt.  185;
Specht  will  auch  (Dekl.  148),  mit  i-  und  it-Formans,  ags.  bri-d,  birci ,junger  Vogel',  germ.  brü-tis  ,Frau,  Braut',  ai.  bhimnd-  , Embryo',  lett. braüna,  Öech.  brnka  {*bhru-nka)  ,Nachgeburt'  hierherstellen.  S.  aber  unter bh(e)reu-  , quellen'.
WP.  II  153  f.,  WH.  I  483  f.,  527,  569,  865,  866,  Trautmann  31,  E.  Her- mann Stud.  Balt.  3,  65  f.
2.  bher'  etwa  , auf  wallen',  von  quellendem  oder  siedendem  Wasser  (auch  vom Aufbrausen  beim  Gähren,  Kochen,  sowie  vom  Feuer)  »sich  heftig  be- ,     wegen';    oft  mit  in-Formans;    auch  als  schwere  Basis  bbers-  :  bhr-^ bb{e)rei-,  bb(e)rf-.    Vgl.  6.  bher-.
Ai.  bhurdti  (Hhf-e-ti)  , bewegt  sich,  zuckt,  zappelt.  Intens. ^*ar-&Äwn^i  ds.; auch:  ,züngelt,  vom  Feuer';  bhuranydti  ,zuckt,  ist  unruhig;  setzt  in  heftige Bewegung,  rührt  um,  rührt  auf;  mit  m-Formans  ai.  bhramati,  bhrämyati jirrt  umher,  dreht  sich  herum',  bhramd-h  , wirbelnde  Flamme,  Strudel', bhfmi-h  ,beweglich;  Wirbelwind'  (s.  unten  aisl.  brimi  usw.);  bh'ärni-]^ ,heftig,  zornig,  wild,  eifrig',  dürfte  als  *bhfni-  ebenfalls  auf  der  schweren' Basis  beruhen;
hierher  wohl  av.  avabaraiti  , strömt  herab',  uzbardnte  ,sie  strömen  hervor(?)',l bardnti  ayqn  ,an  einem  Tag,  wo  es  stürmt'.
Aus  dem  Gr.  7tOQq)iQ(x)  (^rcoqcpvQ lo))  , walle  auf,  woge  auf,  bin  in  unru- higer Bewegung'  (:  si.  jdrbhurlti)'^  vermutlich  auch  (pi)qo)  »vermenge,  bringe durcheinander'  (wenn  ursprgl.  vom  Durcheinanderrühren  beim  Kochen; Gdf.  Hhoviö  mit  durch  den  Labial  bedingter  w-Färbung  des  Reduktionsvo- .  kales),  wozu  q)VQd7]p  »durcheinander*,  cpvQ(.iög  »Verwirrung',  q)VQdü)  .mische, rühre  durcheinander,  knete,  verwirre'.  '
Über  lig.  und  ven.  Namen  s.  unten.
Alb.  burme  .vollreif'  (*gargekocht)  aus  *bhormo-.
Aus  dem  Lat.  wahrscheinlich /re^t^m  undfretus,  -üs  ,Wallung  des  Meeres, bes.  Meerenge;  Brausen,  Wallen,  Hitze',  fretäle  ,Bratpfanne';
fermentiim,  Gärungsstoff,  Sauerteig'  (:  ags.  beorma,  engl,  barm,  nd.  barme, woraus  nhd.  Bärme  »Bierhefe');  auch /er-uere  S.  144;
Air.  topur,  nir.  tobar  »Quelle'  (Ho-uks-boro-),  mir.  commar  =  cymr.  cymmer »Zusammenfluß'  {*kom-bero-))  lig.  FIN  Comberanea-,  mir. /o6ar  »Quelle,  unter-
#' %
133
•rdisclier  Bach*  =  cymr.  gofer  ,BacliS  bret.  gouver  ds.  {*u[p]o'bero-), cvmr.  ^6'*^  
==================== POK p. 143 leaf 151
rscher,  Fürst^,  aisl.  bragr  ,bester,  trefflichster,  vornehmster,  princeps^, mhd.  brogen,  sich  erheben,  in  die  Höhe  richten,  übermütig  großtun*^.
Tech.  AB  park-  ,sich  erheben',  A  pärkänt,  B  pirko  ,das  Aufstehen', A  pärkäry  B  parkre,  pärkre  ,lang^;  vielleicht  A  präkär,  B  präkre  ,fest^ (vgl.  lat.  fortis)'j  hitt.  pdr-ku-us  (parkiis)  ,hoch^  (:  arm.  barjr).
WP.  II  173  f.,  WH.  I  124,  535  f.,  853,  Feist  75  f.,  85  f.,  Trautmann  30  f.. Van  Windekens  Lexique  90,  Couvreur  H  178.
bhergk',   bhrek-    , glänzen*^,    gleichwertig  mit  bherdg-,    bhreg-  ds.   (s.   dort, auch  wegen  doppeldeutiger  Worte). Ai.  bhräsate  ,flammt,  leuchtet^  (unbelegt); gr.  cpoQ'/.6v'  levKÖVj  Ttohöv,  gvaöv  Hes.,  vgl.  aber  S.  134; vielleicht  hierher  air.  brecc  ,gefleckt^,  cymr.  brych  ds.,  gall.  PN  Briccius (aus   *bhrk-,  mit  expressiver  Konsonantendehnung);
unsichere  Vermutungen  über  die  Herkunft  von  cymr.  breuddivyd ;Traum^,  mir.  bruatar  ds.  bei  Pedersen  Litteris  7,  18,  Pokorny  IF.  An- zeiger 39,  12  f.;  ob  aus  *bhroguhdh-eiti-,  -ro-?
142  #
mhd.  hrehen  ,plÖtzlich   und  stark   aufleuchten',   aisl.  hrjä,  brä  (*bre ^aufleuchten',    braga,  bragda  , funkeln,   flammen',    bragd  , Augenblick', ursprgl.    bloß    präs.  -dh-   auch    aisl.    bregda,    Prät.    brä   ,schnell    bewege' schwingen,    vorwerfen',    ags.    bregdan,    bredan    st.  V.    ,schnell     bewege^^ schwingen',  engl,  braid  ,flechten',  wpbraid  ,vorwerfen',  ahd.  brettan,  mhdj breiten  ,ziehen,  zucken,  weben'  (dazu  ahd.  brldel,  ags.  bridel,  älter  brigde]^' ,Zaura,  Zügel');
mit  Formans  -uo-  got.  brafv  in  in  braJva  augins  ^iv  Qiit^  dq)&aXfiov,  im Augenblick'  (vgl.  aisl.  augnabragd  n.  , Augenblick,  Zwinkern  mit  den Augen')  und  dehnstufiges  *brihwa,  *bre^wä  in  aisl.  brä  f.  , Wimper',  agg^ bräewj  breaw,  breg  m.  , Augenlid',  as.  bräha  , Augenbraue',  slegi-bräwa , Augenlid',  ahd.  bräwa  f.  ,Braue',  loint-präwa  ,Wimper'  (die  Bed.  , Braue' von  *bra-  , Braue',  idg.  *bhra-,  bezogen);  daß  trotz  Schwyzer  Gr.  Gr.  I. 350,  463^  und  Specht  Dekl.  83,  162  ahd.  bräwa  nicht  auf  Hhreuä  zurück- gehen kann,  wird  durch  den  grammat.  Wechsel  im  Ags.  bewiesen,  der eine  Form  mit  -ku-  voraussetzt  (Sievers-Brunner  200).
Hierher  wohl  der  Fischname  ahd.  brahs{i)aj  brahsina,  as.  bressemo , Brassen',  norw.  brasma,  brasme  ds.,  ablaut.  aisl.  brosma  ,eine  Art  Dorsch'.
Hitt.  pdr-kn-is  {jparkuis)  ,rein',  pdr-ku-nu-uz-zi  (jparkunuzi)  , reinigt'.  \
WP.  II  169,  Feist  76  f.,  103  f.,  Couvreur  9  327.
1.  bherem-  ,hervorstehen,  eine  Spitze   oder    Kante    bilden;  Kante,  Spitze'|
bhorm- :
Aisl.    barmr    ,Rand,    Saum',    ey-barmr    ,ora   insulae',   norw.    dial.    bai ,Kante,  Bräme'  (z.  B.  am  Segel),  ndd.  barm,  berme  ,die  sanfte  Abdachunj des  Deichfußes,  Wallr
==================== POK p. 144 leaf 152
  f.  ,Laub'  (*bhrom-di',  wie  gläns  aus  *glan-di-)\
an.  brum  n.  ,Blattknospen',  ahd.  brom,  irum  ds.,  Schweiz.  6rom  , Blüten- knospe, junger  Zweig',  ablaut.  bräme  ds.
Auf  eine  Grundbed.  ,borstig,  Dorn'  gehen  zurück:  ags.  bröm  m.  ,Ginstei (*bhremo-)j  mnd.   bräm  ^Brombeerstrauch,   Ginster',  ahd.  brämo  m._,  brama] L  ,Dornstrauch,  Brombeerstrauch',  brämberi,  nhd.   Brombeere,  ags.  bremel) engl,  bramble  (urgerm.  *bramil),  ablaut.  mnl.  bremme,  ahd.  brimma  ,Ginster'| und  mnd.  breme,  brumme  ds.
Mit  der  Bed.  ,Kante,  Rand':  mhd.  br'&m  n.  ,Einfassung,  Rand',  nhd. verbrämen,  ablautend  mengl.  brimme,  engl,  binm  ,Rand'.
WP.  II  102.
2.  bherem-  ,brummen,  summen,  surren'.
Ai.  bhramard-h  ,Biene'
143
o-r.  q)ÖQ^iyS,  -yyog  t  ,Zither',  wegen  des  Suffixes  Lehnwort?  Anlauts- viriante  ^bretn-  wohl  in  ßqsiiw  ;,brausen,  rauschen^  tosen',  ßQ(^ttog  m. Geräusch,  Getön',  ßoovTrj  f.  ,Donner'  {^ßgofi-ro)]
lat.  fremö,  -ere  ,brummen,  brüllen,  tosen,  lärmen';  frontesia  ,Donner- und  Blitzzeichen'  ist  Lw.  aus  gr.  ßgovri^aiog  (zu  ßQOVTrj)-
cymr.  hrefu  ,blöken,  brüllen';
ahd.    hreman    ,brummen,    brüllen',  ags.    hremman    ,brüllen',    brymm   m.
Flut,  ]\Ieer',  mhd.  brimmen  ds.,  ablaut.  brummen  , brummen'  (dazu  brunft
Brunft');  mnd.  brummen  und  brammen  ds.,  ahd.  as.  bremo  ,Bremse',  mhd.
Ireme,  as.  bremmia,  ahd.  brimisse,  nhd.  Breme  und  (aus  dem  Ndd.)  Bremse]
poln.  brzmiec  ,tönen,  summen'  {*bi^m-),  bulg.  bii>mch  ,summe,  brumme', bHmkam  ds.,  brimb-al^  -ar,  -zr  ,Hummel,  Käfer'.
Als  Erweiterungen  unseres  *bhrem-  vielleicht  hierher  die  lautmalenden Worte:  ai.  bkridga-h  ,große  schwarze  Biene';  poln.  brzek  ,Klang,  Geklirr; Bremse',  russ.  67^aÄ:a<6, klirren,  klappern',  6ech.  brouk  ,Käfer';  lit.  br{nktereti ,klirrend  fallen'  usw.;
lit.  brenzguj  brengsti  ,klirren,  klopffen',  ablaut.  branzgu,  brangsti  ,tönen'; slav.  brezgz  in  russ.  brjdzgi  PI.  ,leeres  Geschwätz';  russ.-ksl.  brjazdati ,t()nen'.
WP.  II  202  f.,  WH.  I  544  f.,  Trautmann  37.
bberes-  ,schnell'.
Lat.  festlnö,  -äre  ,beeile  mich,  beschleunige',  Denom.  von  *festiö{n)-y An-  ,Eile',  Erweit,  zu  *festi-  (aus  *fersti-)  in  cönfestim  ,sofort'  (aus  *com festl  ,mit  Eile');
mir.  bras  ,schnell,  stürmisch'  {*bhr^sto-)^  cymr.  brys  ds.  (*bhrsto-),  mbret. bresicy  brezec  ,eilig';
lit.  bruz-g-üs  ,schnell',  bruz-d-hs  ,be weglich',  daneben  burz-d-üUs  ds.,. burz-deti  ,hin  und  her  laufen';
slav.  *b^rz^  in  aksl.  brbzo  Adv.  ,schnell',  skr.  brz  ,schnell',  russ.  borzöj ,schnell,  feurig',  daneben  *b^rzd^  in  wruss.  börzdo  Adv. 
==================== POK p. 139 leaf 147
avov ,dürres  Holz',  q)QiysTQOv  ,Gefäß  zum  Rösten  von  Gerste'.
Merkwürdig  ist,  daß  in  den  Schallsippen  von  gr.  q)QvyiXog  ,ein  Vogel', iRt.frigö  ,quietsche',  poln.  bargiel  ,Bergmeise',  russ.  berglezz  ,Stieglitz'  die Verteilung  der  Formen  mit  u,  mit  i,  und  ohne  beides,  dieselbe  wie  in den  Worten  für  kochen  ist.
WP.  II  165 f.,  WH.  I  486  f.,  548 L
7-  bher-  ,flechten,  weben'?  bb^u-  , Gewebe'.
Hom.  (pagog  =  att.  cpäqog  n.  {^cpaqfog)  ,Tuch,  Leinwand,  Hülle,  Decke'; (potQai  Q)' vq)aivuvyTc'ki'AELvllQs.'^  yo^^uog  , Tragkorb,  Matte';
lit.  burva  ,eine  Art  Kleidungsstück',  lett.  burves  PI.  ,kleine  Segel'  {-u-
138
Suffix  wie  in  gr.  *cpaQJ^og),  lett.  buras  ds.,  lit.  büre  ,Segel^  S.  zum  Vpka^ lisinus  Walde  Streitberg-Festschrift  176. WP.  II  164,  Specht  Dekl.  182.
bberedh-  ^schneiden',  bhrdho-  ,Brett^
Ai.  bardhaka-h  ^abschneidend,  scherend',  m.  ^Zimmermann',  sata-bradl^ na-h  ,100  Metallspitzen  habend';  vielleicht  gr.  tceq&u)  ^zerstöre',  noq^eii ^zerstöre,  verwüste';
bhredbos-  in   as.   ags.   bred  ,Brett',  ahd.  bret   n.,    davon   ahd.    britissc nhd.  Pritsche]
bhrdho-  in   got.  fötu-baürd  n.   ,Fußbrett',   aisl.   bord  n.  , Brett/ Tisch* ags.  bord  n.  ds.,   ahd.  bort  ds.  =  umbr.  forfo-   ds.  in  furfant  ,sie  legeo] auf  das  Brett';  wohl  damit  identisch  aisl.  bord  ,Rand,  Kante,  Schiffsrand' ahd.   mhd,    bort   ds.   (nhd.   Bord  aus   dem   Ndd.),  ags.   bord  ,Bord,  Rand; Schild';  ags.  boi-da  m.  ,Rand,  Verzierung',  ahd.  bortOj  nhd.  Borte-,
bhordhO'  in  aisl.  bard  ,Rand,  Kante',  norw.  dial.  bard  ds.
Aus  germ.  *burd-  stammen  skr.  brdo,  russ.  berdo  usw.  ,Weberkamiii^ und  lett.  birde  f.  , Webergestell'.
WP.  II 163, 174,  Devoto  Mel.  Pedersen  227  f.,  Meillet  Slave  commun«  75j
bhereg'  in   Schallworten  ,brummen,  bellen,  lärmen  u.  dgl.',  vgl.  bher-  ds sowie  die  bei  bhreg-  ,brechen'  und  ,krachen'  begegnende  Schallbedeutung
Ags.  beorcan  St.-V.,  bearkian  (*barkön),  engl,  bark  ,bellen',  aisl.  berkja ,bellen,  poltern,  toben';
lit.  (zem.)  burgeti  ,brummen,  zanken,  unfreundlich  sein',  burgesus ,Brummbart';  vermutlich  auch  skr.  brgljati  , murmeln,  schwatzen',  brgalica ,Turteltaube'.
Daneben  ähnliches  bhereq- :  lett.  brecu,  br^kt  , schreien',  russ.  breiü, brechdth  ,kläffen,  schreien,  zanken,  lügen',  brechnjd  , leeres  Geschwätz', skr.  bresem,,  brehati  , keuchen,  laut  husten'  (^bhreq^-s-),  brekcem^  brektati ,schnauben'.
Etwas  verschieden  wegen  der  helleren  Schallvorstellung  sind  folgende W^orte,  die  in  ihrem  teil  weisen  i-  und  n -Vokalismus  an  die  bei  bher(e)g- ,rösten'  A'orliegenden  Vokalverschiedenheiten  erinnern,  die  aus  verschie- dener Schallnachahmung  erklärt  werden:
gr.  q}QvyiXog  ,ein  kleinerer  Vogel'  (Umstellung  aus  *g)QiyvXoQ:  lat./ri^-?);
lat.  frigö,  -ere  ,quietschen  (von  klei
==================== POK p. 140 leaf 148
reien (von  der  Dohle)',  fring{u)illa  ,Fink,  Sperling';
russ.  berglez  ,Stieglitz',   skr.   brglijez  ,Sitta    syriaca',   cech.  brhel  ,Pirol/   ^ Goldamsel',  mähr.  ,Specht',  poln.  bargiel  ,Bergmeise'.  ^
i
139
Vi  «liehe    aber  gewiß  jüngere  Schallvvorte  sind  lat.  mendus  frindit,  lit. Ijrr-gUi  .blöken,  meckern,  brummend ^yp.  II171f,  WH.  1548.
-  bbreg-  ^glänzen,  weiß^,  wozu  auch  der  Birkenname  N.  Sg.  *bherQg'S, Q^  So".  *bherdgös.  Gleichwertig  mit  hlierik-,  s.  d.
ni  hhräjate  .glänzt,  strahlt^;  apers.  hräzaiti  ds.  (*hhreyö),  npers.  barä- zidan  ^ghänzen',  haräz  .Schmuck';
hsl  *hresk-  aus  bhreg-sk-  in  lit.  hreksta,  hrUko,  hreksti  .anbrechen  (vom rr^a-eY  ctpybre§kis  .Zeit  um  Tagesanbruch';  slov.  hr'^sk,  öech.  bresk,  poln. hrzask  Morgendämmerung',  poln.  obrzasknqc  .hell  werden',  brzeszczy  si^ OS  o-raut  der  Tag',  mit  Assimil.  des  Auslauts  -sk-  an  den  tönenden  Wortan- laut aksl.  pobrSzg^  .Dämmerung.  Tagesanbruch',  russ.  brezg,  poln.  brzazg  ds.
Mit  Abtönung  bh(e)rög-  wahrscheinlich  schwed.  brokig  .bunt',  norw. indartl.  h^ök  .Sälmling'.  auch  wie  bröka  f.  .großgeflecktes  Tier'.
Mit  Hochstufe  der  1.  Silbe:  got.  bairhts  .hell,  glänzend,  deutlich',  ahd. heraht,  mhd.  berht  .glänzend'  (auch  in  Namen  ahd.  Bert-,  -bert,  -brecht), a«-s.  beorlit  .glänzend,  strahlend'  (engl,  bright),  aisl.  biartr  .licht,  hell'; cymr.  berth  .glänzend,  schön'.  PN  bret.  Berth-walart,  ir.  Flaith-bertacJi; lit.  javcn  berst  .das  Getreide  wird  weiß';  wohl  auch  norw.  mdartl.  bjerk .sehr  hell'  .(vgl.  noch  berk  .blanke  Forelle',  schwed.  björkna  .Abramis blicca').
Reduktionsstufig  alb.  barth  (bardh-i)  .weiß'  {*bht,rdgo-).
Im  Namen  der  Birke  (slav.  z.  T.  Ulme.  lat.  Esche):
Ai.  bhürjd-h  m.  .eine  Art  Birke';  osset.  6ärz  .Birke';  dak.  ON  Bersovia; lat.  farnus  .Esche'  {*fdr\_a]g-s-no-s,  ursprgl.  Stoffadj.  .eschen',  wie  auch:) fräxinus  ds.  (wohl  mit  a  anzusetzen,  ^bh^rdg-s-enös)-^  die  zwiefache  Ent- wicklung von  -erd-  in  farnus  und  fräxinus  wird  wie  bei  palma  =  gv. *ftdXa(.iG,  naXdj.irj  gegenüber  latus  =  rlr]r6g  durch  alte  Akzentverschieden- heit bedingt  sein;
ahd.  birihha  (*bher9g-iä),  ags.  beorc,  birce,  aisl.  hjqrk  {*bher9gä)  .Birke';
\it.  ber^as  m..  PL  6^riäi  .Birke',  ablaut.  birztva  f.  .Birkenwald';  bifzliai .Birkenzweige',  lett.  b(}fzs  m..  apr.  berse  .Birke';  russ.  bereza,  skr.  breza, aöech.  brieza  .Birke'  (die  alte  Farbbedeutung  noch  in  bulg.  brSz  .blässig' =  norw.  bjerk  s.  o..  slov.  breza  .Name  einer  weißgestreiften  Kuh  oder Ziege');  mit  Formans  -to-  (=  got.  bairhts)  und  Intonations Wechsel  slav. *berst^  in  russ.  berest  m.  .Ulme.  Rüster',  skr.  brijest,  öech.  brest  ds..  aber mit  der  Bed.  .Birke'  wiederum  russ.  beresta  f..  beresto  n.  .Birkenrinde',  öech. bfesta  .obere
```


## [2026-09-05T13:46:08.138Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('POK_01.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor p in (145,146):\n    print('='*20,'POK p.',p)\n    print(pages[p+8][:2500])\nEOF",
 "description": "Pokorny 145-146"
}
```


## [2026-09-05T13:46:09.446Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"bhreu-\\|bhreu\" AHD_watkins1985.txt | head -40; echo ---; grep -n -i \"bherag\\|bherəg\\|bhereg\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-05T13:46:14.586Z] TOOL RESULT

```
==================== POK p. 145
 ,schnell',  skr» brzdica  f.  ,Schnelle  im  Bach'.
Vielleicht  hierher  ligur.  FIN  Bersula^  Schweiz.  FIN  Birsig  (Krähe  ZONF. 9,  45).
WP.  II  175,  WH.  I  259,  488  f.,  Trautmann  40,  Specht  Dekl.  192.
bh{e)reu-  :  bh(e)rU-,  Erw.  von  2.  bher-  ,sich  heftig  bewegen,  wallen,  bes.  vom Aufbrausen  beim  Gären,  Brauen,  Kochen  usw.' A.  Ablautstufen  bheru-  (bheru-),  bhr^-:
Ai.  bhurvdni-h  ,unruhig,  wild',  bhurvdn-  ,unruhige  Bewegung  des- Wassers'.
144
Arm.  bark  ,scbarf,  sauer,  grausam^  (barkanam  ,ich  werde  zornig^),  ^ sehr  vieldeutig  ist,  wird  von  Dumezil  BSL.  40,  52  als  *bhr-u-  hierher, gestellt,  desgleichen  berkrim  ,ich  freue  mich^  als  *bher-u-]  sehr  unsicher!
Gr.  (pagv^ög-  roX^ifjQog,  d^gaaiug  Hes.  (Hh.ru-)  und  cpOQvxög  ,Gemisc}j^ Kehricht,  Spreu,  Mist',  (poqtvo),  cpoqvaau)  ,knete  durcheinander,  vermiscKe^ beflecke,  besudle',  wahrscheinlich  auch  cpQV-daao^aL  ,gebärde  mich  ung^. duldig  (bes.  von  feurigen  Pferden);  bin  übermütig'.
Thrak.  ßgvrog  (s.  u.).
Alb.  brum  m.,  brume  f.  ,Sauerteig',  mbruj,  mbrünj  ,knete'.
Lat.  ferveöj  -ere,  fervö,  -Sre  ,sieden,  wallen'  (über  fermentum  s.  2.  bher-f^ defi-ntum  ,eingekochter  Most,  Mostsaft'  (:  thrak.  ßgvrog,  ßgvrov,  ßgovro^ ,eine  Art  Gerstenbier';  aus  thrak.  *brütiä  (gr.  ßgvTia\  stammt  illyr.  hrUc^ ,Weintrester',  urverw.  alb.  bersi  ds.,  woraus  serb.  bersa,  birsa,  hh-ZQ Schimmel  auf  dem  Wein;  lat.  brlsa  aus  dem  Venet.  oder  Messap.).
Mir,  berbaim  ,koche,  siede',  cymr.  benvij  bret.  bhwi  ,sieden,  wallen^, beroj  berv  ,gekocht',  galL  GN  Borvö  (bei  Heilquellen),  vgl.  mit  anderem Suffix  Bormö  oben  S.  133;  vielleicht  auch  frz.  bourbe  ,Schlamm'  aus  galL *borvä  ,Sprudel';  air.  bruth  ,Glut,  Wut',  mir.  bruith  ,kochen',  enbruith ,Fleischbrühe'  (zu  en-  ,Wasser',  s.  unter  peno-),  acymr.  brut  ,animus',  ncymr. brwd  ,heiß'  (cymmrwd  ,Mörtel'  aus  *kom-bru-to-,  vgl.  mir.  com&rta^/i  , sieden^), brydio  ,fervere',  acorn.  bredion  ,coctio'  (Umlaut),  abret.  brot  ,zelotypiae^, nbret.  broud  ,heiß,  gärend'.
Über  germ.  67'it-Formen  s.  unter  B.
B.  Ablautstufen  bhreu-  und  (teilweise  wieder)  bbrü-:
Zunächst  in  Worten  für  ,Quelle'  ==  ,Hervorsprudelndes'  (r/n-St.,  etwa .bhreurj  bhreun-,  bhrun-):  arm.  aibiur,  aibeur  (Gen.  aiber)  ,Quelle'  (aus *blireio{a)r  =)  gr.  (fgsag,  -äzog  ,Brunnen'  (^cpgfjJ^ag,  -atog,  ho
==================== POK p. 146
  ags.  brunna^  burna  , Brunnen' (aisl.  brunn)y  mit  Metathese  nhd.  (ndd.)  Born.
Mit  ähnlicher  Bed.  russ.  brujd  ,Strömung',  bruith  ,stark  reißend  strömen, ■dahinfließen',  wruss.  brüjic  ,harnen'  (diese  Bed.  auch  in  mhd.  brunnen  und in  nhd.  dial.  brunzen,  bair.  brunnlen  ,harnen'  von  Brunnen),  formal  näch- stens zu  lit.  br{i)dujs,  br{i)dutis  ,sich  mit  roher  Gewalt  vordrängen'  (*bhreu-), lett.  brauligs  ,geil';  auch  apr.  breicingi  , forderlich'?
bhre-n-U'  (Präsens  mit  Nasalinfix,  vgl.  nhd.  brennen)  mit  Beziehung -auf  züngelnde  Flammen  liegt  vor  in  got.  ahd.  as.  bi-innan,  ais.  brinna, .ags.    beornan,    birnan   ,brennen',    Kaus.   got.    brannjan,   aisl.   brenna,  ahd.
145
Iretinan,  ags.  haernan  ^brennen^,  wozu  u.  a.  ahd.  hrant  ,Brand^,  brunst Brennen^  Brand^,  aisl.  hruni,  ags.  hryne  ^Brand'^  ahd.  hronadoj  ags.  hrunapa Jucken;  Hitze  am  Körper^,  schwed.  bränad  ^Brunst'^;
hhreu-  :  bhruu-  in:  ahd.  hriuwan,  ags.  breowan  ,brauen^,  aschwed. bryggja  (aus  *bryggwa)  ds.;  germ.  *bruda-  in:  aisl.  ags.  brod^  ahd.  prod BrUhe^  {:  defrütum,  air.  bruthy  thrak.  ßQvrog:  mhd.  brodelen,  nhd.  brodeln)-, trerm.  *brauda-  in:  aisl.  braud,  ags.  bread,  ahd.  6rö^  ,Brot^  (von  dem Gärstoff);  über  ahd.  tüm^es  pril^  ^Windsbraut^  s.  Kluge ^^  692.
WP.  II  167  f.,  WH.  I  333  f.,  487.  •        .
bhergh'  ^bergen^  verwahrend
Got.  bairgan  ^bergen,  verwahren^;  aisl.  bjarga^  ags.  beorgan,  ahd.  bergan j as.  gi-bergan  ^bergen*^;  ablautend  ags.  byrgan  ^begraben^,  byrgen  i^burgizno), byrgels,  as.  burgisli  ^Begräbnis^  und  ahd.  bor(a)gen  ^sich  wovor  hüten,  sich wovor  in  Sicherheit  bringen,  acht  worauf  haben,  schonen,  anvertrauen, borgen^,  ags.  borgian  ,behüten,  borgend  Slav.  *bergg  in  aksl.  bregq,  brästi '  ^sorgen^  in  nebrästi  ,vernachlässigen^,  russ.  beregü,  berech  ,hüten,  bewahren, •  schonen,  sparen^,  skr.  älter  brzem,  brijeci  , bewachen,  bewahren,  sorgen; feiern^;  ablautend  klr.  oborih,  gen.  oboröha  ,Heuschober^,  öech.  brah  ,Heu- schober,  Haufen'^,  poln.  brög  ,Scheune,  Schober^  (daraus  lit.  brägas  ds.); schwundstufig  öech.  brh  ,Höhle,  Hütte,  Zelt^;  ostlit.  birginti  ,sparen^
Vielleicht    hierher    gallo-rom.    (rhät.-ill.)    bargä    ,gedeckte    Strohhütte^, falls  aus  Horgä]  Tagliavini  ZrP.  46,  48 f.,  Bonfante  BSL.  36,  141  f. WP.  II  172,  Tr
```


### [2026-09-05T13:46:14.633Z] TOOL RESULT

```
334:bher-2. To cut, pierce, bore. 1. Germanic *bordn in Old English borian, to bore: BORE}. 2. Germanic *baru-ga-, castrated pig, in Old English bearg, barg, castrated pig: BARROW’. 3. Germanic *bor-, perhaps in French burin, burin: BURIN. 4. O-grade form *bhor-d- in Latin fordre, to pierce, bore: FORAMEN; BIFORATE, PERFORATE. 5. Per- haps Greek pharunx, throat (< “a cutting, cleft, pas- sage”): PHARYNX. 6. Slavic *bor- in Russian borot’, to overcome: DUKHOBOR. See extension bhreu-'. [Pok. 3. bher- 133.]
344:bly Latin fridre, to crumble: FRIABLE. 3. In the Celtic source of Vulgar Latin *brisdre, the source of Old French brisier and French briser, to break: BRISANCE; DEBRIS. [Pok. bhréi- 166.] bhrekv-. To cram together. 1. Probably Latin frequens, frequent, crowded: FREQUENT. 2. Suffixed zero-grade form *bhrk~-yo- in: a. Latin farcire, to cram, stuff: FARCE, FARCI, FARCY; INFARCT; b. Greek phrassein, to fence in, enclose, block up: DIAPHRAGM. [Pok. bhareky- 110.] bhrem-'. To growl. 1. Latin fremere, to growl, roar: FREMITUS. 2. Perhaps variant *brem- in Greek bronté, thunder: BRONTOSAUR. [Pok. 2. bherem- 142.] bhrem-2, To project; a point, spike; an edge. 1. Germanic *bréma-, name of prickly shrubs, in: a. Old English brém, broom: BRooM; b. Old English diminutive bremel, brém- bel, bramble: BRAMBLE. 2. Germanic *berm-, *brem-, in: a. Middle English brimme, edge: BRIM; b. Middle Dutch berme, barm, edge of a dike: BERM. [Pok. 1. bherem- 142.] bhres-. To burst. Germanic “brest- in Old English ber- stan, to burst: BURST. [Pok. bhres- 169.] bhreu-'. To cut, break up. Extension of bher-2. 1. Suf- fixed form *bhreu-d- in Germanic *breutan, to break up, in Middle English britel, brittle: BRITTLE. 2. Suffixed form *bhreu-t- in Germanic *breuthan, to be broken up, in Old English bréothan, to deteriorate: BROTHEL. [Pok. 1. bhreu- 169.] bhreu-?. To boil, bubble, effervesce, burn; with deriva- tives referring to cooking and brewing. I. 1. Germanic *breuwan, to brew, in Old English bréowan, to brew: BREW. 2. Germanic *braudam, (cooked) food, (leavened) bread, in Old English bréad, piece of food, bread: BREAD. 3. Germanic *brudam, broth, in: a. Old English broth, broth: BROTH; b. Old French breu, broth (diminutive brouet): BREWIS; IMBRUE. II. Variant form *bhré- in Germanic *brédan, to warm, with derivatives. 1. *bréd-6, “a warming,” hatching, rearing of young, in: a. Old English br��d, offspring, brood: BROOD; b. denominative *brodjan, to rear young, in Old English brédan, to beget or cherish offspring, breed: BREED. 2. Germanic *bré- d6n-, roast flesh, in: a. Old High German brat, brdto (> German Braten), roast meat: BRATWURST, SAUERBRA- TEN; b. Old French braon, meat: BRAWN. 3. Perhaps distantly related is the Germanic source of Old French brese, burning coal, ember (> French braise): BRAISE, BRAZE?, BRAZIER?, BREEZE2, III. Reduced form “bher-, especially in derivatives referring to fermentation. 1. Suf- fixed form *bher-men-, yeast, in: a. Germanic *bermén- in Old English beorma, yeast: BARM, (BARMY); b. further suffixed form *bhermen-to- in Latin fermentum, yeast: FERMENT. 2. Extended form *bherw- in Latin fervére, to be boiling or fermenting: FERVENT, FERVID, (FERVOR); DEFERVESCENCE, EFFERVESCE. IV. As a very archaic word for a spring. 1. Suffixed zero-grade form *bhru- n(e)n- in Germanic *brunnon- in Old English burn, burna, spring, stream: BOURN!, BURN?. 2. Suffixed form *bhréw-r in Greek phrear, spring: PHREATIC. [Pok. bh(e)reu- 143, 2. bher- 132.] bhreus-'. To swell. 1. Suffixed form *bhreus-t- in Ger- manic *breustam, “swelling,” breast, in Old English bréost, breast: BREAST. 2. Suffixed zero-grade form *bhrus-t- in Germanic *brust-, bud, shoot, in Old French broust, brost, shoot, twig: BROWSE. [Pok. 1. bhreu-s- 170.] bhreus-2, To break. 1. Germanic *briisjan, to crush, in Old English brysan, to crush, pound: BRUISE. 2. Suffixed zero-grade form *bhrus-to-, fragment, in Latin frustum, piece: FRUSTULE, FRUSTUM. [Pok. 2. bhreu-s- 171.] bhri-. Eyebrow. Contracted from *bhrua-. 1. Germanic *bris in Old English bri, eyebrow, eyelid, eyelash: BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugj6 (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE}, [Pok. 1. bhrii- 172, 2. bhrii- 173.] bhrig-. Agricultural produce; also to enjoy (results,
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
1316:BOUND! bamb- BOUND‘ bheue- BOUNTY deu-2 BOUQUET busk- BoURG bhergh BOURGEOIS bhergh-2 BOURN bhreu-2 BOURSE bursa
1321:BRAIN mregh-m(n)o- BRAISE bhreu-2 BRAKES bhreg- BRAKE‘ bhreg- BRAMBLE bhrem-2 BRAND gWher- BRANDISH gWher- BRANDY gWher- BRASS ferrum BRASSARD mregh-u- BRASSIERE mregh-u- BRATWURST bhreu-2 BRAWN bhreu-2 BRAY? bhreg- BRAZE? bhreu-2 BRAZEN ferrum BRAZIER! ferrum BRAZIER? bhreu-2 BREACH bhreg- BREAD bhreu-2 BREAK bhreg- BREAKFAST past- BREAM! bherak- BREAST bhreus-1 BREATH gWhré- BREATHE gWhré- BRECCIA bhreg- BREECH brak- BREED bhreu-2
1323:BREEKS brak- BREEZE bhreu-2 BREGMA mregh-m(n)o- BREMSSTRAHLUNG | ster-2 BREW bhreu-2 BREWIS bhreu-2 BRIAR! wer-3 BRIDE? bherek- BRIDEGROOM dhghem- BRIDGE! bhri- BRIDLE bherek- BRIEF mregh-u- BRIGHT bherag- BRIM bhrem-2 BRIMSTONE gWher- BRINDLED gWher- BRING bher-!
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1442:EDIBLE ed- EpicT deik- EDIFICE aidh-, dhé-1 EDIFY aidh-, dhé-1 EDITION d6- EDUCATE deuk- EDUCE deuk- EFFACE dhé-1 EFFECT dhé-1 EFFEMINATE dhé(i)- EFFERENT bher-1 EFFERVESCE bhreu-2 EFFETE dh@(i)- EFFICACIOUS dhé-1 EFFICIENT dhé-1 EFFIGY dheigh- EFFLORESCE bhel-3 EFFLUENT bhleu- EFFLUVIUM bhieu- EFFLUX bhlieu- EFFORT bhergh-2 EFFULGENT bhel-1 EFFUSE gheu- EFTSOONS apo- EGEST gerere EGG! awi-
1507:FERIA dhés- FERMATA dher-2 FERMENT bhreu-? FERN per-2 FEROCIOUS ghwer- FERRET! bher-1 FERRET? bhel-3 FERRI- ferrum FERRO- ferrum FERROUS ferrum FERRUGINOUS ferrum FERRULE wei-1 FERRY per-2 FERTILE bher-1 FERVENT bhreu-2 FERVID bhreu-2 FERVOR bhreu-2 FEss bhasko- -FEsT dhés- FESTAL dhés- FESTINATE bhers- FESTIVAL dhés- FESTIVE dhés- FESTOON dhés- FETAL dhé(i)- FETCH! ped-1 FETE dhés- FETICIDE dhé(i)- FETISH dhé-1 FETLOCK ped-! FETTER ped-1 FETTLE ped-2 FETUS dh@(i)- FEUD! peig-2 FEUD? peku- FEUILLETON bhel-3 FEVERFEW bheug-! FEW pau-
1544:FROLIC fik-, preu- FROM per? FRONTISPIECE spek- FROST preus- FROTTAGE bhréi- FROWARD per! FRUCTIFY bhrig- FRUGAL bhriig- FRUGIVOROUS bhrig- FRUIT bhriig- FRUITION bhriig- FRUMENTACEOUS _ bhrig- FRUMENTY bhriig- FRUSTULE bhreus-2 FRUSTUM bhreus-2 FRY! bher-4 FUGACIOUS bheug-1 -FUGE bheug-! FUGITIVE bheug-1 FUGLEMAN man-1, pleu- FUGUE bheug-! FUHRER per-2 FULCRUM bhelg- FULGENT bhel-1 FULGURATE bhel-1 FULIGINOUS dheu-1 FULL! pele-1 FULMAR pu-2 FULMINATE bhel-1 FUMARIC ACID dheu-1 FUMAROLE dheu-1 FUMATORIUM dheu-! FUMATORY dheu-1 FUME dheu-! FUMIGATE ag-, dheu-! FUMITORY dheu-1, ters- FUNAMBULIST al-2 FUNCTION bheug-2 FUND bhudh- FUNDAMENT bhudh- FUNDUS_ bhudh- FUNGIBLE bheug-2 FUNNEL gheu-
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
2085:PHOTO- bha-1 PHOTOTROPH threph- PHRASE gWhren- PHRATRY bhrater- PHREATIC bhreu-2 -PHRENIA gW¥hren- PHRENITIS gWhren- PHRENO- gWhren- PHTHIRIASIS dhgWher- PHTHISIS dhgWhei-
2215:SATISFY sa- SATRAP pase, tké- SATURATE sa- SATYAGRAHA es-, ghrebh-1 SAUCE sal-1 SAUERBRATEN bhreu-2, stiro- SAUERKRAUT siro- SAUTE sel-4 SAVANT sep-1 SAVE!  sol-
---
141:There are very widely represented words for the beech tree, bhadgo-, and the birch, bherag-. These formerly played a significant role in attempts to locate the original home- land of the Indo-Europeans, since their dis- tribution is geographically distinct. But their ranges may have changed over several mil- lennia, and, more important, the same word may have been applied to entirely different species of tree. Thus the Greek and Latin cognates of BEECH designate a kind of oak found in the Mediterranean lands.
331:bherag-
336:bhereg-. To shine; bright, white. Compare the by-form bherek-. 1. Germanic *berhtaz, bright, in Old English beorht, bright: BRIGHT. 2. “The white tree,” the birch (also the ash): a. Germanic *birkjon- in Old English birc(e), birch: BIRCH; b. suffixed zero-grade form *bhrag-s- probably in Latin fraxinus, ash tree: FRAXI- NELLA. [Pok. bherag- 139.]
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.] bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan (*for, before; see per') in: a. Old English béodan, to proclaim: BID; b. Old English forbéodan, to forbid: FORBID; ¢. Old High German farbiotan, to forbid: VERBOTEN, @: Germanic *tudén- in Old English boda, messenger, hence bodian, to announce: BODE!. 3. Ger- manic *budilaz, herald, in Old English bydel, herald, messenger: BEADLE. 4, Germanic *budam in Old Norse bodh, command: OMBUDSMAN. 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE. [Pok. bheudh- 150.]
1301:BIOTA g¥ei- BIOTIC gWei- BIPARTITE pere-2 BIRCH bhereg- BIREME ere-!
1323:BREEKS brak- BREEZE bhreu-2 BREGMA mregh-m(n)o- BREMSSTRAHLUNG | ster-2 BREW bhreu-2 BREWIS bhreu-2 BRIAR! wer-3 BRIDE? bherek- BRIDEGROOM dhghem- BRIDGE! bhri- BRIDLE bherek- BRIEF mregh-u- BRIGHT bherag- BRIM bhrem-2 BRIMSTONE gWher- BRINDLED gWher- BRING bher-!
1537:Fra _bhrater- FRACTED bhreg- FRACTION bhreg- FRACTIOUS bhreg- FRACTURE bhreg- FRAGILE bhreg- FRAGMENT bhreg- FRAGRANT bhrag- FRAIL! bhreg- FRANGIBLE bhreg- FRANK! Frankon- FRANK Frankon- FRANTIC gWhren- FRATERNAL bhrater- FRATRICIDE bhrater- Frau pert FRAUGHT @ik- FRAULEIN pert FRAXINELLA bhereg- FRAY? bhréi- FRECKLE (S)preg- FREE pri-
```


## [2026-09-05T13:46:51.782Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD gwher / gwhre ===\"\ngrep -n \"gWher-\\. \\|gWhré-\\. \\|gWhre-\\. \" AHD_watkins1985.txt | head\nsed -n '331p' AHD_watkins1985.txt | head -c 300\necho; echo \"=== search burn entries ===\"\ngrep -no \"gWher-[^.]\\{0,40\\}\" AHD_watkins1985.txt | head -5\ngrep -n \"To heat, warm\" AHD_watkins1985.txt | head -3\ngrep -n \"To smell, breathe\\|gWhré-\" AHD_watkins1985.txt | head -5",
 "description": "Locate AHD gwher entries"
}
```


### [2026-09-05T13:46:53.352Z] TOOL RESULT

```
=== AHD gwher / gwhre ===
bherag-

=== search burn entries ===
1321:gWher- BRANDISH gWher- BRANDY gWher- BRASS fer
1323:gWher- BRINDLED gWher- BRING bher-!
1324:gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bhe
1530:gWher- FORCIPATE gWher- FORD per-2
1533:gWher- FORNICATE gWher- FORSAKE sag- ForT bher
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
551:ghré-. To smell, breathe. Contracted from *gvhreo-. Germanic suffixed form *bré-thaz in Old English bréth, odor, exhalation: BREATH, (BREATHE).
1321:BRAIN mregh-m(n)o- BRAISE bhreu-2 BRAKES bhreg- BRAKE‘ bhreg- BRAMBLE bhrem-2 BRAND gWher- BRANDISH gWher- BRANDY gWher- BRASS ferrum BRASSARD mregh-u- BRASSIERE mregh-u- BRATWURST bhreu-2 BRAWN bhreu-2 BRAY? bhreg- BRAZE? bhreu-2 BRAZEN ferrum BRAZIER! ferrum BRAZIER? bhreu-2 BREACH bhreg- BREAD bhreu-2 BREAK bhreg- BREAKFAST past- BREAM! bherak- BREAST bhreus-1 BREATH gWhré- BREATHE gWhré- BRECCIA bhreg- BREECH brak- BREED bhreu-2
```


## [2026-09-05T13:46:53.620Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor leaf in (72,73,74):\n    print('='*15,'leaf',leaf)\n    print(t[leaf][:2500])\nEOF",
 "description": "Mann IEC near p.116"
}
```


### [2026-09-05T13:46:55.530Z] TOOL RESULT

```
858
=============== leaf 72
üs 'fordable'; Latv. bradus (adj. *wading)
bhromolos ‘buzz, hum, roar’ Skt. bhramarah ‘bee’; ON and Icel. braml ‘roar’
bhrondh- ‘burn, destroy’ Olr. bronnaim ‘destroy’; Du. branden “burn”
bhrondhos, å, is ‘swell, growth, surge’ Ir. bronn ‘swell, bruinne ‘breast’; Br. bronn, W bron ‘breast’; Br. cf. also brons (‘tree-bud, shoot’, fr. *bhront-); Ger. branden, v. ‘surge’; Li. brandùs ‘full, abundant’, brandà ‘crop’; brandis ‘full pod’
bhronghos, à, us (1) ‘bearing, suffering;
loose,
105
loaded, heavy”. Cf. bhrengh-. WP II, 204. Cf. brongh- Å NAIb brångë (1) “sorrow beside Alb. brengë ‘suffering’; ON (hapax) branga *quar- re; Li. brangüs ‘dear’. (Alb. & Li. ambig.)
bhronghes, à (2) ‘swollen; swelling’. Cf. bronsghos NAIb brángé, Alb. brengë (2) ‘tumour, esp. in cattle; ulcer; MHG branc, gs. -ges *boast- ing; brenge ‘ostentation’; cf. brangen, V., (Upper) Ger. prangen “boast'; Icel. braggast ‘thrive’; Latv. cf. brangs ‘luxuriant, fat. (A variant *bhrong- occurs in Scots branks ‘mumps’). See next. (Alb. brángé, brengë are ambiguous, cf. brongh-)
bhronka ‘swelling’. (Variant of bhronghos (2), q.v.). Cf. bronk- (Alb. brángé, brengé is ambig.); Srb. bruka ‘calumny? (here); Li. brankà “swelling” (ambig. cf. bronk-)
bhrontos, à (?) : W brwnt, f. bront 'dirty'; Li. brantai, mpl. *syphilis'
bhrosk- ‘tumultuous; turmoil'. Cf. bhra$s- & WP II, 196 (206) & II, 193 Mir. broscur ‘clamour; mob’; brosc ('thun- der; adj. (big); Icel. braska ‘bustle’; Dan. braske ‘boast’; Sw. braska ‘rustle; live in luxury; Li. cf. brasküs 'crackly beside brafkü, éti ‘creak’. (Lith., & Scots brash ‘sudden illness, bout; E brash ‘showy’ are ambiguous. See bhra$s-. For It. brusco and Fr. brusque cf. bhrisk-)
bhroud- (?) (Gk. phroüdos ‘transient, vain” is usu. refd. to pro  hodós); ON braut, f. i-st. road: adv. "away beside breyta "change: NNorw. braute ‘boast; rampage’; RNorw. brøyte “break; turn; dear": Cor. brows 'crumbs', cf. Br. brüzün ‘crumb’; Pol. Ukr. Slovak. Cz. brud “dirt?
bhroukið ‘turn, go’ MHG bröuwen ‘bend, turn’; Pol. cf. bruk ‘road-paving’; Li. braukiù, braükti ‘plod’; Latv. braucu, braukt ‘travel
bhrouK- *edge, side; side-piece' . „ Ir. bruach “edge, side’; Cz. Pol. brus, R (dim.) brusók ‘whetstone’ beside Cz. brusle ‘skate’;
bhronghos, à — bhrughno-
10
15
20
25
30
35
40
45
106
Srb. brüs ‘whetstone’; R brus ‘beam, girder
bhroulios, iə ‘seething, brew, surge’ Br. brülľ’, pl. brüP u ‘wave, billow; brew, soup’; brül'a v. ‘vomit’; OCS brulja ‘fountain’. (For a possible verbal prototyp
=============== leaf 73
ce, adj. ‘useful; (*-u-) in broc "use, benefit’; Go. brüks *useful
bhrüg- (2) ‘tremble’ Illyr. in Lat. briza *quaking-grass'; OE broc- cian ‘tremble’; Pol. bryze *yellowrattle'
bhrugilos, see bhrigil-
bhrugh- 'swell, increase” Lat. fruor, fructus; Ir. broghaim “increase, advance, press', beside broghdha *exceeding; big, MHG brogen “raise, anger; rise; swag- ger
bhrughis, os, io (?) ‘construction’ Ir brugh ‘mansion; fort; MHG  brucke, brücke “bridge, stage’; OE brycg; Du. brug; cf. also OE brycgian, v. ‘pave paralleled in Russian most ‘bridge’; mosti? ‘to pave’; ON bryggja ‘gangway, pier; Latv. brugis ‘paved road?
bhrughno- (2) ‘shrubbery, rushes’. WP II, 208
107
Br. broenn; W brwyn; Cor. bron “rushes, reeds’; OE brogne ‘bush’
bhrug- (1), ‘fragment. Cf. bhrügo Gk. cf. phrüganon ‘chip, faggot’; OS brokko, OE broc, bryce, MHG brocke ‘fragment’ beside bruch ‘breakage’; Du. brok
bhrug- (2) “breast of animal, brisket, sweet- bread’ Arm. erbuc, gs erbco ‘breast of animal’; cf. Lat. frümen (‘glottiş’ if for *bhrugmn-); (Ir. brú, gs bronn “breast? is ambig. Cf. bhrondh-); OCz. brzicé “breast, dewlap’; Slovak brzica, id.; Cz. cf. brz-lík, m. 'sweetbread'. Cf. bhreuks-, bhreus-
bhrügo, io (?). Cf. bhru2- (1) Mir brüghaim, brüighim “bruise, crush, mash’; Li. brüzyti ‘scour’; cf. Latv. bruzaju ian (?) óbrüzos, adj. ‘refined, pure’ are un- certain as also Srb. briznem, -nuti "well up'.
bhruk- ‘hurt’ Olr. broc ((3) 'grie); Blg. brükam “prod, stir; Li. brukü, brükti “force, thrust, scutch'; Latv. brukt ‘collapse’. (Sw. bry ‘vex derives from LG brüden, id.) (EH)
bhruktos It. (Gallo-Lat?) brutto ‘ugly, fou; W brwth, m., broth, f. ‘turmoil; MHG bruht, wider- bruht ‘defiant; defiance’, cf. Ger. brohsein ‘riot, fuss’; Li. brükti ‘thrust; scutch'; Latv. brukt ‘crumble, collapse’; Cz. brkati, brknouti ‘jerk; shriek; flap; trip’. For Ir. bruth, broth, see bhrütos (2); cf. Srb. brka ‘muddie’.
bhrumbhalos, bhrumbhəros ‘buzzing insect’. See next Alb. brúmbull ‘bumble-bee’; Blg. brúmbar ‘cockchafer’ or sim.
bhrumbho, bhrumo, ið “hum, buzz, rumble’? MHG brummen; Du. brommen; Dan. brumme, and com. Gmc.; Pol. brzmieć; cf. Blg. brüméca ‘hum’
bhrumn- ‘welling-up, bhreumn-. WP IT, 208 Alb. (ambig.) brumë ‘dough, paste, plasma’; OHG. OS brunno ‘well, spring’; G cf. Brunst; Du. bronst “heat in animals? beside bron, as G Brunnen
(bhruniə 'trappings, harness, equipment.
ferment. See
bhrug- — bhrüs
10
15
20
25
30
35
40
45
108
A Celt. LW in Gmc.Sl. and Balt.) (Cf. bhrondh- for background of Ir. 
=============== leaf 74
��dun, brownish; brown or dun- coloured creature’. WP II, 166 | Gk. phrünos, phrüne ‘toad’; MHG brün, ON brünn; OE brün; Du. bruin (LW in Fr. & It.); beside ON brünn “raven horse”, brún (i-st. ʻa material); (*-ü- in) Cz. Slovak brna ‘brown cow’; OCS brünije, n. ‘mud’; Latv. (LW fr. Gmc.) brūns “brown?
bhrüs (1) (oqu-bhrüs, -bhrüues) ‘brow’. Cf. bhrün-. WP IT, 206 Skt. bhrüs, bhruva; Av. brvat, du.; Per. abrü; Kurd. biro; Oss. árfíg; Tokh. pårwan, párwane, du.; Maced. abroütes (err. for *abroüwes?) (AM); Alb. (?) bri, def. brija (edge, side"; G Braue, id.: MIr. brú, d: Gk. ophrüs be- side ophrúë (also = ‘dike, vallum’: ON brú ‘bridge’ (?); MIr. brú (2) ‘bank, border’); MIr. brói, dual: dabrúad; Ir. cpd. fo-bhar, fa-bhar, fa-bhra (phon. obscure); Br. abrant; OE brū,
109
pl. brüwa; phon. obscure in OHG wint-bråwa, Du. wenk-brauw; OCS brúvi, obrüvi; Slovak brva, obrva; OCz. brv, gs brve; Li. bruvis, io & bruvē.
bhrus- (2) “break, crumble; fragment, crumb'. Cf. bhrusd-. WP II, 198 Lat. cf. frustum beside frustáre, v. ‘shatter’; Olr. brus “fragment; gravel, grit; refuse; MHG cf. brosem ‘crumb’; OE brosnian ‘crumble, decay’; OCS brüsng, noti (1) ‘corrode’, v. be- side brüseli, f. ‘chip’. Long ü is represented in Alb. brishtë, i — (ambig.) “rugged (if not fr. bhrst-, q. vr: MIr. brüim “pound, shatter’; OE brysan, brysian, id.
bhrüs- (3) ‘gush, teem’. Cf. WP II, 199. Gk. cf. phruássomai ‘bluster; MHG brüsen; G brausen; Du. bruisen; Norw. fr. LG bruse; Blg. brisna, brisvam; Li. cf. brüsa, brüsva “plenty”. (O-gde is represented in Slovene bruhati ‘erupt’; Blg. bruxam ‘chatter’: Cz. brouchati se *mess about, paddle', though the semantic link is obscure)
bhrusdhó (bhrusd-) (1) ‘crumble, break’. Cf. bhrus- (2) Arm. brdem ‘crumble’ beside brdon (i-st. *erumb); Umb. cf. e-furfatu (queried) “let him scatter”; (Alb. z-brydh “make friable, mel- low'. Ambig. cf. bhrgo, ið); Norw. brudd “breach, rupture’. (Variant *bhrusd in Ir. brod *d or *dh *trifle); OE, ON brot ‘fragment’; Norw. brott, id.; cf. OE bryttan, brytsen *break up'
bhrusdho, io (2) ‘goad, tease’ MIT. bruitim ‘stab’; brot ‘goad’: MHG brutten ‘scare’; (w. nach) demand": OE bryrden; LG brüden ‘tease’; OE bryddan ‘scare’? beside bryrdan ‘incite’; LW fr. LG in Sw. bry; ON brydda ‘stab, incite’. (The isophonic Li. bruzdü, éti ‘scurry; revolt? appears to be un- related). See next
bhrusdhos ‘spike, peg, barb, goad, sting. WP II, 133. Cf. bhrusdh- (2) OFr. cf. brosder ‘embroider’; OBr. cf. broth- rac, cpd. ‘embroidery’; M
```


## [2026-09-05T13:47:14.612Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '545p' AHD_watkins1985.txt | grep -o \"g’her-\\. To heat.\\{0,1800\\}\"\necho \"=== gwhre ===\"\nsed -n '551p' AHD_watkins1985.txt | head -c 400",
 "description": "AHD gwher- full entry"
}
```


## [2026-09-05T13:47:15.496Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (77,78):\n    print('='*15,'leaf',leaf)\n    print(t[leaf][:2600])\nEOF",
 "description": "Mann IEC leaves 77-78"
}
```


### [2026-09-05T13:47:16.193Z] TOOL RESULT

```
g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
=== gwhre ===
ghré-. To smell, breathe. Contracted from *gvhreo-. Germanic suffixed form *bré-thaz in Old English bréth, odor, exhalation: BREATH, (BREATHE).
```


### [2026-09-05T13:47:17.810Z] TOOL RESULT

```
=============== leaf 77
beside birüs ‘apt to fall.
bhrio (2) see bhráið & bhur- (2)
bhrio (3) ‘raise’. Variant of bhrgh- (?) OW (ambig.) cf. bry (above'. See bhrghus);
` OHG burian ‘raise’ beside bor “height, upper
room’; MHG bor ‘up’; OE bor-lice “very”
bhrios (bhro(n)) (1) ‘bearer, holder’. See bheró, bhor- Skt. cf. bhrpámi ‘bear’; OHG OS -boro; OE bora, -bora; ON cf. ó-byr-ja ‘sterile woman’; Gk. pharía 'vessel
bhrios (2) ‘son, young man. (Semantically related to (1)) Kurd. cf. bire “a stalwart’; Per. barnà, burnā ‘young man’; OE bora ‘son’ and byre, id.; Alb. bir, pl. bij, id.; Go. baür, cons. st. id., cpds. -born; ON burr, pl. rir, id.
bhrios, bhrà (3) “bore, hole’. Cf. bhraio Alb. birë “hole; OHG bora 'gimlet; OE, MLG bor, id.
bhrkos, à, o(n) (1) ‘spike, splinter ` Lat. (ambig.) furca 'fork, prop, gibbet" beside forco *ploughpoint'; Ir. cf. (either) briogún ‘skewer (or) bráca ‘harrow’, brácaim, v. “har- row’ (*-T-); Srb. Slovene bøk ‘moustache’; Cz. brk ‘quill’; Pol. barki, pl. ‘shoulders’; Lusat. cf. bórkać (‘root up ground": Ir. brá- caim); Li. birka ‘tally-stick’; Latv. birka ‘chip, point
bhrkos, om, à (2) (?) "boat Gallo-Lat. barca; Br. bark ‘boat’; Slovak brko. ‘keel
(bhrm- ‘bore, hole’. Cf. bhrios (3). Alb. brimë ‘hole’)
bhrnio ‘tingle, burn” Gk. cf. os-phrainomai ‘smell, sniff? (initial to osmé. EB otherwise); OFris. burna; Fris. baerna; OE byrnan beside biernan (vocalism obscure); OCz. Cz. brnéti ‘tingle’
bhro (bhur-), see bhràio
bhrs- “break; fragment. Cf. bhris-, bhrus-, bhrst- Hitt. pars-mi, -imi, -ihi “break, divide’; cf.
115
parsür “crumbs'; Gk. phársos, n. (1) “frag- ment’; OCS (ambig.) brúseli (“potsherd”, but for OCS brúsno, -noti ‘destroy’, cf. bhris-. Ir. brisim ‘break’ seems to represent a form bhrst-, q.v., while OE brysan represents a form containing -ü-, cf. bhrus- (2)
bhrsos, ios, à, is ‘shag, tuft, bristles, fur. Cf. bhrstis Av. cf. boro$o ‘backbone’; Arm. bars (i-st. ‘horsehair, mane"); Gk. phársos (2) ‘cluster’; Phryg.? (LW in Gk.?) bürsa ‘rawhide, skin bag’; Lat. (LW or Gallo-Lat?) burra ‘shaggy garment’; re-burrus, adj. ‘bristly’, cf. also LLat. borr-àágo (“borage”, lit. *bristly plant"); variant (*bhors-) in Olr. barr *tree-foliage, spray’; Cor. bar (1) “bunch, tufted branch? beside Oir. barrán “head of hair; ME burre ‘burr’; Norw. Sw. borre, id. (Sw. also 'thistle- head, sea-urchin’); Cf. OCS brí$-ljanü *spindle- Dee beside Cz. brs-len, id.; cf. also Cz. brs- ina ‘grassy slope’. See bhors-
bhrstis, os (bhurst-, bhrust-) ‘spike, shoot, twig, bristle’. WP II, 131 Sk. bhrstíb; Oss. barc ‘mane’; Hitt. parsdus ‘sprout; Lat. (ambig. füstis ((stick'
=============== leaf 78
; OE byrd ‘fate’; Du. beurt ‘turn, lot; OFrankish, cf. staim-bort (a weapon: *stone-throwing catapult’)
bhrt- (2) ‘bearing, load, product. WP II, 153. Cf. bhero, bhoros
bhrsos, ios, à, is — bhübh-
15
20
25
30
35
40
45
116
Sk. bhrtíh; Av. borotis; Olr. brith; Go. ga- baürps, baürpei; MHG burt; bürde; OE byrd; ON byrð, f. beside byrór “birth; load"
bhrt- (3) “boring, bore, hole, hollow’. Cf. bhraio ON byrða “bin, trough”; Pol. barc, Cz. brt, R bort ‘hollow in tree, hive of wild bees’
bhrtós, á “borne, carried'. Cf. bherð Sk. bhrtáh; Av. boroto; Per. bilà ‘alms’; ON burór (*bearing?, etc.)
bhrug- (bhorug-, bhor-) ‘neck, windpipe’. Cf. bhrug- Oss. bárzài ‘neck’; Gk. phárux (& phárugx); ON barki
(bhru-, see bheru-. Z-gde radical in Per. balwà ‘tumult; OE brymm, m. ‘surf, sea”, prob. also in MHG brunne ‘spring’; ON brunnr, id.)
bhruos, à “arch, span, beam, bridge’. (prob. variant of bhruu- q. v.) Gaul. brivo-, brio-, briva (‘bridge’, in place- names); ON brú; Sw. bro, id.; Blg. brúvi, Srb. brv “sleeper; footbridge’; OCz. břev, pl. břvi, f. ‘beam, rafter’; cf. OCS brüvno ‘beam’; Cz. břevno, Ukr. berveno; Slovene bruno
bhū- (bhüu-) (1) theme of verb ‘to be’. Cf. bhüio & bhui-. WP II, 141 Skt. á-bhut, pf., bhütáh, pp.; Av. büta, npl.; Per. budan, inf; Gk. phüs, m. ‘son’ beside Hes. pháos ‘plant’; phué ‘growth’, éphün, aor., etc: Ir. budh (was, 3sg);; W OBr. bu, wd: Lat. Dm. id. beside OLat. fuam ‘may be’ and OBr. bi “will be’; OS bū, OE bü ‘dwelling’; Norw. bu ‘booth’; ON búi ‘dweller’; bua “dwell, be’; beside byggva ((populate', fr. *bhuu-); OHG bü, gs buwes ‘farming’; OCS byxü, etc. ‘was’; Li. būvis, 10, m. ‘creature’ beside buvau “I was’; Latv. büveju ‘I build”
bhū- (2) ‘howl, gale, blast. Cf. bhübh- Arm. bu (o-st. 'owl) beside buk, pl. form “gale, storm’; Per. cf. bü timàr ‘heron’; Phryg. or Mac. büza ‘owl’; Du. bui ‘squall’; cf. Lat. butio and MIr. bufa (‘bittern’, fr. *bhuuo-). Sw. rágn-by (LW < Du.)
bhübh- “a hooting animal’. WP II, 112 Arm. bbun (/noise', fr. *bhübhon); Lat. bübon (owl, w. assimilated consonants) beside bū- bulo, are (onomat. *büb-); MIr. cf. búbaire,
117
m. ‘bittern’; Li. bübe ‘heifer’ beside bübauti ‘bellow’
bhubbh- (expressive variant of above) ‘mut- ter, burble’ OE à-byffan; Latv. bubinaju, id. See next
WP II, 114. See bubul- Lat. bullio (assimilated consonants); MLG bubbeln; Du. bobbelen; OCS bübljo, čti & -ati; Alb. bubullon (3sg *thunder); Cz. be- blati, Pol. bebłać ‘stammer; slobber’
bhubhlos, see bhubhulos
bhubhos, à (bhubbh-) (1) ‘creature, monster’ Hitt. pupus (queried) ‘paramour, concubine’ Alb. bubë ‘grub’; LW in Srb. buba, B
```


## [2026-09-05T13:47:30.367Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['MON','BQT','SOD','BRT','ARY']:\n    v=d[k]\n    print('###',k)\n    for f in ['local_file','page_offset','lookup_hint','scans']:\n        print(' ',f,':',json.dumps(v.get(f),ensure_ascii=False)[:700])\n\"",
 "description": "Ref offsets for MON BQT SOD BRT ARY"
}
```


### [2026-09-05T13:47:32.173Z] TOOL RESULT

```
### MON
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"]
  page_offset : null
  lookup_hint : "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."
  scans : null
### BQT
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "/home/sfmqrb/git
  page_offset : "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; th
  lookup_hint : "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ
  scans : [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920
### SOD
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"]
  page_offset : "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)"
  lookup_hint : "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}"
  scans : null
### BRT
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt"
  page_offset : "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."
  scans : null
### ARY
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"]
  page_offset : "printed page = pdf page + 1"
  lookup_hint : "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"
  scans : [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf", "first_printed": 1, "last_printed": 546, "pdf_offset": -1, "lang": "fas+eng", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"}]
```


## [2026-09-05T13:47:39.560Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part1 بلوا ===\"; grep -n -o \".\\{80\\}بلوا.\\{160\\}\" MON_part1.txt | head -8\necho \"=== MON part1 برازیدن/برازنده ===\"; grep -n -o \".\\{60\\}برازید.\\{200\\}\" MON_part1.txt | head -6\ngrep -n -o \".\\{60\\}برازنده.\\{160\\}\" MON_part1.txt | head -6",
 "description": "Grep Mo'in for balva and barazidan"
}
```


### [2026-09-05T13:47:39.648Z] TOOL RESULT

```
=== MON part1 بلوا ===
=== MON part1 برازیدن/برازنده ===
```


## [2026-09-05T13:47:40.285Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 براز ===\"; grep -n \"برازیدن\\|برازنده\\|براز \" BQT_v1_pages.txt | head -20",
 "description": "Grep Borhan v1"
}
```


### [2026-09-05T13:47:40.337Z] TOOL RESULT

```
=== BQT v1 براز ===
1688:ممجزه لفت براز نده‌ای پنداشنه ودرمدح بیغمبر گفته:
8174:خربطه که براز بشه باشد وآنرا بشه خاته گویند
10509:تأیید میکند و هنینگه قول دستذ دوم را - جزه اول اردا بمعنی مقدس است - وبراز بمعثیکراز
18118:۸ رك : برازیدن .
18149:براز بان‌است‌و انآ هن بارة دنباله کاردوشمشر وخنجر
23779:زمتی را گونند براز 3 و لای که سب نردد
```


## [2026-09-05T13:47:46.059Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\n# find leaf containing line 18118 text\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'برازیدن' in l or 'برازند' in l:\n        print('=== leaf',i,' printed ~',i-215)\n        print(l[:1800])\n        print('---')\nEOF",
 "description": "Find Borhan leaves with barazidan"
}
```


## [2026-09-05T13:47:46.887Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -c MON_part1.txt MON_part2.txt; head -c 600 MON_part1.txt; echo; echo ===; grep -c \"برا\" MON_part1.txt",
 "description": "Check MON file content"
}
```


### [2026-09-05T13:47:48.254Z] TOOL RESULT

```
=== leaf 466  printed ~ 251
و مردمی را نز گویند که در عروسی همرامداهان
بخانة عروی روند .
بر اذا ند - مختف برادراندر اس تکه
پس پدر باشد از زن دیگر » با پر مادرازشوهی
دیگر #
پر اد ۲ ه بروزن تماز » بمعنی‌برازند گین
و زسایی و تیدویی و آوانتتگ باشد ‏ و اهر
باینممنی هیهمت سعتی آراعته کنو نیکو ییاور _"
و چوبکی رانب ز گوبند که کنش گران مان کفش
و قالب گذارند و درود گران مبان شاف چوب
نهند بوقت شکافتن - و پینه را نیز گویند که‌بر
جامه و غیر آن دوزند - و درعربی بمعنی‌پیرون
آمدن باشد - و فنله و غابط را پیز گویشد -
و بمعنی وصل کردن و چبانبدن‌هم لسع
بر او بان ح بکس اولبروزن نگاهبان,
آهن بار درازی را گوند که بر دنبالهٌ تیفهٌ کارد
و ششیر و خنجر و امثال آن باشد که بدرون
دسته و قنه فرو کنند :
و زن جوان - و آغوش و کنار و بغل را نیز
کوبند ٩‏ - وبهنای هرچیز ۴ - وطرف‌وجانب-
و باد وحافظه حفظ و نگاهداشتن بخاطر- ونفع
و قابده را هکفتهاند. و بننتی در سرا و خانف
و مین خك بی آب و علف و پیابان بود ۴ -
و مخطف ب رکه درخت باشد - و نام درختی است
درهند ۴ - وپرنده‌ای رائیز گوند - و آمریبردن
هم هست یعنی ببر 6 .
بر ]ب ]هدن - کنابه از ظاهرتدن
و فاش گردیدن باشد .
رابر ان س بر وزن تتاکران .کیاهی
است دوابی که آنرا یونانی سطاربون خواننده
بر گزندگی عقرب ضماد کنند ناقم باشد .
پر آب گفتی- بسنی فی السال ر زود
گفتن و زودجواب‌دادن باشد . *
بر ات بر شاخ ]هو » کنابه از
دروغ گفتن و وعده دروغ کردن باشد . . .
بر اقی ‏ بروزن‌باتی, جامة کهنهوانتال
اج اتف که توق بالق موالت من یناف بر ادك « بروزن ترازد بعنی زبد .
0 توت ۶ ۲. .۰ ۰ ۲ طبری و مازندرانی کنونی (۷2۲ (یهدا)
*واژه‌نامه ٩۷۲۹۱‏ . ۴ - باین حعثی بفتح ارل و دید دوم عرمی است .
۴ - بر (بفتح‌اول ویض‌اول) درهند (بزبان‌اردو) نام درخت لور 06082160515 عداهز۳
است «ثابتی ۱۱6 ۵ _ راجم بحرف «بر» » رك : ص » لد از دیباچة مولف .
1 -رك:سنطاربون. ‏ ۷ - اوستا 2۲27207222 (زینت. آراش) «اسفا!:۲ص۳۹».
۸ رك : برازیدن .
+ ارات _ درعرف بازر گانان بمحثی نوشثه‌ای که بواسطهٌ آن دولت برخزانه بابرحکام با
تاجری بر ناجر دبگر حوالةٌ وجه
---
```


### [2026-09-05T13:47:48.295Z] TOOL RESULT

```
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
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
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی 
(eval):2: == not found
```


## [2026-09-05T13:48:03.777Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nleaves=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(\"### leaf 466 tail\")\nprint(leaves[466][1800:3500])\nprint(\"### leaf 467\")\nprint(leaves[467][:1500])\nEOF",
 "description": "Borhan leaf 466-467"
}
```


### [2026-09-05T13:48:05.493Z] TOOL RESULT

```
### leaf 466 tail
ی دهد و آنرا پپروات جمع بشدند » و آن عربی است ودراصل
(برامة) بوده است به‌عنی بری‌الذمه گردیدن از دین, و صواب درجمم آن برامات با براوات است
«قزویتی . تعلبقات چهار مقالا ی *۱۷* . ه برادر - بفتح آول وچهارم» پهلوی 2۲26
و 08۳۵12۴ هوست ۷۸»"اوستا ۲22 «حرن. اسفاا:ص ۰۱۰۲ طبری 932726 «واژه‌نامه۱۰۵»
کلکی 02408۵۲ . نطتری 926۲2 «۵. ۲۸4۱ , سمتانی [08۳26 ؛ منگری 96۲36۲
سرخه ولاسگردی ۰۳6۲ شهمبرزادي 8۲2۲ «4. ۷ ص۱۸۸ » اورامانی ۵8۲2 .«. اورامان
۰ ».۰ اشکاشمی ۷۲۵۵ , زیاکی ۷۵۲۵۵4 ۰ وخی ۷۲۱ . سریکلی ۷۲۵ منگلچی۷۷۳4
منجی ۷6۲21 ۰ بودفا ۷۳۵1 « گربرسن ۰۷۱۰۱ ؛ اخ » پسر که با شخص از مك پدر و مادو
ما ازمکی از آغدو ماشد ‏
### leaf 467
۷ ۱ : ۱ برانه
پر اغلیدن - بروزن‌جفا کنیدن» مخخف
برآغالیدن است که بمنیتحرض (۱) کردن وبر
انگیختن باشد و بعربی اغرا هگویند .
بر ااق‌جم « کنابه ازبادی اس تکه‌تخت
سلیمان علیه‌السلام را میبرد .
بر ! کوه (۷)- بتح اول و ضم کات
و سکون واو و ها » نام کوهی است که ما بین
«شرق و جئوب فصبٌ اوش واقم است از ولات
فرغانه تزديك باندجان .
بر ) هلان « بر وزن در آمدن » بمعنی
بر انداف - بش اول و سکون نون
و دال بی نفطه بالف کشیده و بفا زده . رودهای
اسان و حبوانات دیگر را گویند .۷
پر اثه - بفت اول و نون » نلم شهری
و مدبنه‌ایست .
ح ۱
برازش - بقتح ارل بی وژن نوازش »
بمعنی زیبند گی باشد - وبمعنی وصل کردن‌ینه
و پاره هم حست برقبا و خرقه و امثال آن .
بر ادوان - با واو » بر وزن و ععنی
براز بان‌است‌و انآ هن بارة دنباله کاردوشمشر وخنجر
و امثال آن باشد که در دسته و قضه‌فرو کنشد.
بر اد یشان ۱ < بروزن‌تراودن » بمعنی
خوب و زبا نمودن- و وصل کردن باشد چیز برا
جچعیر ی ۰
‌
بر آنش» بغتح‌اول.بروزن‌ومعنی‌خراش‌وزخم
لست- وبمعنی‌باشدن- وفرو نشاندن هم آمده‌است.
براغ با تشدید ثانی بروزن دباغ.فصاد
و صد کننده راگوشد
بر آ غالیدن ۲ » بالامبروزن‌سراپلدیدن ,
بمعئی بر انگیختن و تحریض ( ۱ )کردن باشد
شخصی را برچیزی و کاری .
۱ - از مسدراوستابی ۳22 (یرتوافکندن): ساسکرت 0۳4[206ن «بارتولمه۹۷۲ .
۴ - م رکب از : بر( آغایدن [رك آغالیدن] .
ه برانوش ‏ با #رالوش.مهندس رومی در زمان شابور اول ساسان يکه بپنگلم اسارت
امپراطور روم بامی شایور پل شوشتر را بساخت :
همی برد هرسو برآنوتی را بدو داشتی در سخن کوش را
مکی رود بد پهن در شوشتر که ماهی نکردی بروبر گنر
برانوش را کفت اکر هندسی بلی سازی‌این راچنان چو دسی
که ماباز کردیم این‌پل بجای بماند بدانایی رهن
```


## [2026-09-05T13:48:05.496Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nleaves=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (346,347,348,349,350,351,352,353,354,355,356,357):\n    txt=leaves[i]\n    print('=== leaf',i, repr(txt[:120]))\nEOF",
 "description": "Borhan leaves around p137"
}
```


### [2026-09-05T13:48:07.121Z] TOOL RESULT

```
=== leaf 346 'که آنسخها از بدن اوجته برآن کس میخورد\nوفرومیرود ؛ و گویندهرچنداورا بز ند فربه\u200cترشود.\nکه خاریشت بر انداز باشد .\nاسفا دور '
=== leaf 347 '۱۳\nگذارندآ برامخود کشدوشراب\u200cرابگذارد,وباخا کتر\nآن زخمی را که در ساعت زده باشند خشك بند\nکنند » زود لیکو سازد . گرم و خهكت'
=== leaf 348 'وفا ء قاضی ترسابانرا کویند وشخصی\u200cرانیز گویند\n.از ابشان که بجهت رباشت خودرا بزنجیر :بندد.\nگود اين لت عربی است\nاسقلطسی ب س'
=== leaf 349 'لک شود و اکر ساعتی توئف کند بفند\nتشر\nاسكث بکسر اول وسکون ثانی وکاف ؛\nای را کون که در راهها جهت قاصدان\nبسیارند وقاصد رانی'
=== leaf 350 'اسکندروی\nو دختثر از دارا حامله\nبودوأنظهار نمیکردتابوی\nدهن\u200cاورا با اسکندروی\nکه آنرا بفارسی سیر\nکوشد علاح کردند و\nمدازآن ف'
=== leaf 351 '- و۱۳\nاسمنك بفتح اول وثالث وسکون نانی\nاسمند\u200cر » بنتح او » پمعشی سمئدر\nباشد و آن چانوریت که در آتش حتکون\nمیشود ۷ .\nاسموسا'
=== leaf 352 'باشد ٩\u200f - و بلفت زند و پازند (۱) بمعنی مینه\nاست که جربی صدر خوانند ۴ .\nاسیر لگ - بارای فرشت بروز نکنيزك .\nیار خریزه را ک'
=== leaf 353 'وا\nاول هم آمده است ٩\u200f .\nاشتاب ۴ - جن\u200cاول وسکون بایابید.\nبمعنی ثتاب و تعجیل باشد » و بکر اول حم\nآمده است » و بجای حرف آخر'
=== leaf 354 'اشتر گیا - بکر کاف فارسی و تحتانی\nبالف کشیده , بممتی اشتر خار است که خار\nشتری باشد ۰ و بسضنی کوبند کیاهی است\u200cدوابی\nکه آن'
=== leaf 355 'و سکن الی و دال ابجد , نام روزدوم است از\nخمسا مترفةٌ فدیم- وبودن آفتاب دربرجعفرب\nودرین روز عفان بمنی آتش پرستان جش نکنند'
=== leaf 356 'اخك تلح ه جفتح فوقالی » کنایه از\nشراب الکوری باشد - و اثك چشم را نیز\nکواند .\nباشد . ۷\nاشگر ف « بنتح اول وکاف فارسی بر\nوز'
=== leaf 357 '_ٍِِ\nاشکو خیدن . مصدر اشکوخ است\nکه لفزیدن دبسردرآمدن وافتادن\u200cباشد , چها کر\nکی را پایش از یش بدد رود و یفئد گویند\nاشکوخیه'
```


## [2026-09-05T13:48:29.096Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nleaves=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(leaves[347])\nEOF",
 "description": "Print Borhan leaf 347 (p.137)"
}
```


### [2026-09-05T13:48:30.837Z] TOOL RESULT

```
۱۳
گذارندآ برامخود کشدوشراب‌رابگذارد,وباخا کتر
آن زخمی را که در ساعت زده باشند خشك بند
کنند » زود لیکو سازد . گرم و خهكت است
در اول و دوم (۱) .
آسفنح است که آمر مرده باشد
اسقنك ۱ - بکر اول وفتح اك‌وسکون
افی و رأبع و دال اسجد ۲ تام ماه دوآزدهم باشد
از سا شسی ۲ و نام الکه‌است درنیشابور -
1 نام داروبی است که ترا حزاراسفتد نیز گویده
و آن نوعی از سداب کوهی باشد و بعربی‌حرمل
" اسقئدار هف ت بر وزن و معت
اسیندارمذ است که‌نام‌امدوازدهم باشدازسال‌شسی.
و للم روژ پنجم آزهر ماه شمسی ۰ و فارسیان این
که مان ابشان متعارفست که چون نام روز با نام
ماه موافق باشد آنروز را عید باید کرد و مبارك
دانت - و نام فرشته است موکل بر ییشپا و
درعتای بو امیر و صاله ماد ایتدان کی میتی
دارد - و بمعثي زمین هم آمده ! ست که سر بی
ارش خوانند ۴ .
اسفند اسشید یک اول وفای دوم»
خردل سفید است ۳
حب‌الرشاد خوانند .
اسفند مد - نم میم ۴
نقطه دار » نام روژسوم (۷) است
و بوسیرن: ۳
اسفندیاره بر وزن و معنی آ-نددار
است که نم پس کشتاسب باشد و او را روبین تن
میکفتند - و بمعنی قدرت حق و لطف یزدان‌هم
هت ورب ماه امفندار و رب روز اسفندار
اسقیك - بر وزن و معنی اسیهید است
کممطلق سیهسالار باشد۷ - ونامی است مخصوس
ملوك فارسیان ۸ .
اسفهبد خوده. بر وزن و معنی
اسیپبد خوره است که باعتقاد اشرافیان فاری شی
ناطقه باشد که آن قوت متکلمة اسانی‌است ٩‏
اسفیجاب - باجيم بروزن استیعاب .نم
3
و۲
اسفیداج باجیم. عمرب اسفیداب است
که زنان برروی مالند و نقاشان و مصوران هم‌کار
قرمایند» وخوردن آ نکشنده نود تا سفیداب
تر
استبی‌ار ‏ مخفف اسفیددار (۳) است
که درخت یده‌باشد وبعربی غرب خوانند ۰ وبصنی
کویند توعی از یده است ٩*‏
اسفیف دشت « اسفید معلوم » و دا
ایجد عفتوح‌وشین ونای فرشت فت‌سا کن» نام‌قر به‌ایست
از توایع صفاحان .
اسفیوش ع بر وزن و معنیاسپیوش‌است
که بزر قطونا باشد . و عربان بقلةٌ با رکه
هه
)۱( چش : دوم . )۱( چش : سیم . )۳( چش: اسفیدیار .
۸ ملوکک طبرستان . صحیح است
خوره - ۱۰ رکه : اسیمدار .
ب وله : اسیندبار.
اسیپیث .
هی کته ۵ تاو 9 انس
```


## [2026-09-05T13:48:30.955Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT brāz ===\"; grep -n -i \"brāz\\|brāzaiti\\|brāzah\\|bräz\" BRT.txt | head -20\necho \"=== SOD βr'z ===\"; grep -n \"βr'z\\|br'z\\|βrʼz\" SOD_pages.txt | head -20",
 "description": "Grep Bartholomae and Gharib"
}
```


### [2026-09-05T13:48:31.023Z] TOOL RESULT

```
=== BRT brāz ===
4462:•  j.  ajnika-  m.  i)  'Antlitz' 1  tanüm  .  . yeühe  'ks  bräzaiti  yaia  ..  Yt. /o.  143; F.jd,  2)  'Stirn-,  Vorderseite":  aspahe ..  yim  ttpairi  'tum  sanat  amS  Yt.  14. 9.  a)  bes.  des  Heeres,  'Front'  (nur Komp.).
5117:sükaya  (sd.)  bräZ3m  Yt  14.  33;  33;  — jainü  mqm  ahuna  vairya  "vata  snai>isa ya%a  asma  . .  YtZ/.ao;  P.22;  —  kthrpa 'vatS  (GS.)  *sraya  (sd.)  ya%a  dämqii sralstail'^.2.^;  —  ifkrpa  "vatqm  sraya ydka  di'iayatqm  zaosS  (sd.)  Yt  17. 1 1 ;  — st»r)naoili  aria  *°vat  starim  .  .  ya'ia  .  . P.25(?).  a)  substantivisch  'Wntum',  mit Gen.  part:  yat  mS  'va(  daüvayasnanqm ni/atitn  ydka  .  .  Yt  J.77;  —  upa  .  .  'vat siWi/  (sd.)  urva  *isaiti  yd^a  .  .  H.  2. 2.  b)  mit  Akk.  der  Beziehung:  andern .  .  y3  asti  'vaiti  masö  yd^a  vJspa  ima äpS  Y.  65. 3 ;  — yash  . .  "vant^m  (als  ASn.) mass  vikilnayät  ya'ia  hi  tanus  atphat  V. 7.51.  a)  mit  ya'i:a  yat  'wie  wenn,  als ob':  °vaia  aejanha  yd^a  yat  panca  narS "mit  solcher  Kraft,  als  ob  es  fiinf  Männer wären"  V.  75. 10  PiiZ.  2)  'dass':  asti  sl
17408:bräza-
17452:•  J,  bräz- V. 'strahlen'.   Praes.  2'>  ^äz«-. 'strahlen,     glänzen':     tanüm    ,  .  yeAkä
17453:ainiks  brasaiti  ya'i^a  tistrydMärahe  YL  10. 143.  a)  mit  Akk,  des  Inhalts'^  und des  Ziels:  car?ma  (sd.)  vamanto  bräzmta frSiia  trizatam  saranim  Yt.  5.  129.
17456:•  j.  btäza-  i)  Adj,  (fem.  -za-)  tlinkend, schimmernd':  ya'iia  sükayä  (sd.)  'sayh bräztm  Yt.  i4~  33-  *)  n.  'Schein,  Schim- mer': avavalai  ya^a  sükayh  (sd.)  bräzayä ',3m  Yt  14.  33.
21119:—  yaihä  ainikö  bräzaiti  y*  HBrySMärahe  ?r>ti-S  V.  ö^  43 ;  —  yö  astim  upanh^rvtaiH Yl  JO,  142;  —  ahe  ti  na  *travanh3*afra-  ,.  *avai  atpi  y  kasistahe  ^rTtfS  fratanam mar7rUi{sA)astrjdley' gaianqm(itM.22;  tbifti   W.6.  10;     11,    14,    iz;    —   yas:a
26364:•  j.  sükä-  f  'Nadel';  avaviüctl ya%a  °kaya bräzayä  bräs»m  avavatcit  ya'ha  'kayü na/am  "auch  was  nur  so  gross  ist  wie der  Schein  einer  blinkenden  Nadel, . .  wie das  Öhr  einer  Nadel"  Yt  74.33.
27847:bräziHta  .  .  }r3zai>m  'nim  Yt  5,  129;  17.
=== SOD βr'z ===
5157:481 'br'z— C                o-^j'^ < j-^^V*^ 'J^s^s.                 plant, growth
5163:482 'br'zc C                                JU-aP i'Ui-j^Sl y       desire
5173:484 'br'ztr C
5174:                                                                    (o)prez ©3pl. -ynt -^br'z-
11450:        -^br'z-, Pr'zndtyy                                         2692 pr'k^ncyk B               ^jIjuU o'jIjuL «(^w9
11593: 2727 br'z- ** >br>z-
```


## [2026-09-05T13:48:45.376Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== grep r'z'nt ===\"; grep -n \"z'nt\\|z-nt\\|βr’z\" SOD_pages.txt | head -20\necho \"=== leaf 172 (p.106) ===\"\npython3 - <<'EOF'\nleaves=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(leaves))\nprint(leaves[172][:1500])\nEOF",
 "description": "Gharib Sogdian lookups"
}
```


### [2026-09-05T13:48:47.976Z] TOOL RESULT

```
=== grep r'z'nt ===
22002:6362 nyz'nt B, S                                                        BBB p66, 537, 586, 705, 615; BSTii: C2, 40V19
22007:6363 nyz'ntyh B
22013:6364 nyz'pdy* ? C                                                     nizandya (nyzntyO =»nyz'ntyh, nzndy*h
32893:       TSP 3.204; Hen. Texts. 729, wz'ntk "blowing"
34302:10563 wyzp S                                   c                       waz ^wz'nt'k
=== leaf 172 (p.106) ===
645
                                                                                                               Pr'ywy
 107

 2701 pr>s kyr>n B                                     ^^          KG 353, 384
      fras kiran ^fr'skyr'n                                   2713 prVmVn S                                       ^3J
      south                                                        fromayan ^prwnVyk
        BSTBL, Vaj. 20; Benv. Notesi 65                            Roman, Byzantine
                                                                   KG 394; GMS 1049, 1244
 2702 pr'st- S                         o>J &lj <j=-*jL~
      frast ©pt. St.; perf. fi^stwS'r- ^fr'y?-, Pr>z-,       2714 prNvscyCh)     B                              J*^J
                                                                   frawisci    ^Pr'wcy, pr'wscy, fr*wyscy, frwycy
         frst-
       OeOconclude, (resettle                                      forgetfulness
       MDii; Gersh. Advice. 89; S W, C2 n pl32.22                  TSP 2.171, 7.168, 20.11; BSTBL, Dhu. 279

 2703 prJs(y)- S(M)                          o^J             2715 Pr'xs-      M              O-iU^ tjjA^lf <jj£ Ju>
      frasay ©<*fra-ais ©impf. ^Pr'ys-, pr'ys-1,                   Praxs ©<*brixsa-
                                                                   (rc)be roasted
          pr}yst-
       (to)scnd                    v                               GMS 825; Sogdica. 40.12; AVS 73
       Hen. Tales. 478.25
```


## [2026-09-05T13:48:58.390Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if \"br'z\" in l or \"Pr'z\" in l or \"pr'z\" in l:\n        # find page marker\n        m=re.findall(r'\\n\\s*(\\d{2,3})\\s*\\n',l[:400])\n        print('=== leaf',i,'approx p.',i-66,'markers',m[:3])\n        for ln in l.split('\\n'):\n            if \"br'z\" in ln or \"Pr'z\" in ln or \"pr'z\" in ln or 'shin' in ln.lower() or 'brilliant' in ln.lower():\n                print('   ',ln.strip()[:160])\nEOF",
 "description": "Find Sogdian br'z entries in Gharib"
}
```


### [2026-09-05T13:49:04.124Z] TOOL RESULT

```
=== leaf 84 approx p. 18 markers []
    481 'br'z— C                o-^j'^ < j-^^V*^ 'J^s^s.                 plant, growth
    (o)Praz (br>z-) ^Pr'z'nl
    482 'br'zc C                                JU-aP i'Ui-j^Sl y       desire
    484 'br'ztr C
    (o)prez ©3pl. -ynt -^br'z-
=== leaf 171 approx p. 105 markers []
    -^br'z-, Pr'zndtyy                                         2692 pr'k^ncyk B               ^jIjuU o'jIjuL «(^w9
    shining                                                           frakencik ©adj. ^PrV, fr'kcynyy
    Praz(a)nde, Prazonde =»Pr'zndtyy                             2693 br'qcny C                              ^jIjU, «t&w>
=== leaf 173 approx p. 107 markers []
    2726 pr'z— S               e.uU* < j^~> i^J'x^ tj^jjL^
    2727 br'z- ** >br>z-
    Pr'zyntk
    shining                                                2742 pry'w B, S                         J*<gf<^jJ
    2729 pr'zntyy -> Pr'zndtyy                                         possession, richess
```


## [2026-09-05T13:49:09.406Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nleaves=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(leaves[171][:2200])\nprint('#### leaf173 head')\nprint(leaves[173][:1200])\nEOF",
 "description": "Print Gharib leaf 171 and 173"
}
```


### [2026-09-05T13:49:11.693Z] TOOL RESULT

```
        TSP 6.158 n p206                                                   Frag. Len. 38.9, 12, 21; prw, 84 a 9, 86.7
 2678 pr^n     B =* |3r>n                                          2690 -prJk . B            (J3 :<jCU; -u^-^ljb t*jjj* u>xj>
 2679 prMs B                                           jS                Pare ©<*-baraka ©suff.
                                                                         bearing, porter
       fras =*pr's                                                       TSP 3.50 n pl94; GMS 1132
       punishment
       SCE 476; TSP 2.365, 1169; VJ 827                            2691 pr'k'yS B                             J^jjj*^«jj
 2680 prwt =» prH                                                        fra-ke5 ©adv. ^Pr'k1
                                                                         early, the next day
 2681 prVnt B                        uU^p<0'jj>
                                                                         GMS 1109, TSP 2.582-, Hen. Texts. 734
      Prazand ©MR bryz-, Khwar. Wz-% A v. brdz-
        -^br'z-, Pr'zndtyy                                         2692 pr'k^ncyk B               ^jIjuU o'jIjuL «(^w9
      shining                                                           frakencik ©adj. ^PrV, fr'kcynyy
                                                                        morning, of morning
       BSTBL, Dhy. 212
                                                                        TSP 2.1162 n pi 84
 2682 prMzyntk B            *                      J*=i,«jujj>
      Praz(a)nde, Prazonde =»Pr'zndtyy                             2693 br'qcny C                              ^jIjU, «t&w>
                                                                        morning
                                                                        frakcanc ? ^fr'kcynyy
      burning, ablaze
      BSTBL, Intox. 3; GMS 1068                                          Sund. KG pl8l
 2683 pr>pry     M =» p>rp)rk                                      2694 pr'nity* B                            ^j&'JJJ
 2684 pr>cp- S                                           ? o^           Pramtya -»Pr»mt(wh)
      fracap ? ©impf.         
#### leaf173 head
                                                                                                                    108



  pr'yz-
 2724 pr'yz-      B        j/ j^o jjj, <J& Jj* *lf)y_J i^J          KG 333; GMS 293

       frez/z ?                                               2738 pry»r B => Pry>r
                                                              2739 pryWk S                           *k>^ «£,
       {name of a)plant
                                                                   frayame ? ©*/^- gamaka\ Munj. fraYomiy
       TSP 19.20 n p232                                            male kid
 2725 prJyzk(h) B                                £****£>-           "year-old" KG 503, S W, Apd. 3.2.3
      frezk/e ? ©ob. -yh                                      2740 prYnk    S                              ^^J^^J
      thorn
      VJ 902,781, 1104                                              faryane ©-w
                                                                    (<?/)Farghane
                                                                    MDii p84
 2726 pr'z— S               e.uU* < j^~> i^J'x^ tj^jjL^
      fraz ©<*fra-raza =»J3r*st-
      GeOconclude a pact,
```


## [2026-09-05T13:49:24.904Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD brāz ===\"; grep -n -i \"brāz\\|brʾc\\|brazidan\\|brāc\" PHD.txt PHD_mackenzie.txt | head -15\necho \"=== HRN barāz ===\"; grep -n -i \"barāz\\|baräz\\|barazīdan\\|bräz\" HRN.txt | head -15\necho \"=== HUB ===\"; grep -n -i \"barāz\\|bräz\\|brāz\" HUB.txt | head -15\necho \"=== CHEUNG brāz ===\"; grep -n -i \"brāz\\|bra(u)z\\|\\*brāz\" CHEUNG.txt | head -15",
 "description": "Grep Iranian refs for braz"
}
```


### [2026-09-05T13:49:25.001Z] TOOL RESULT

```
=== PHD brāz ===
PHD.txt:281:brāzīdan, brāz- [bPc-ytn! | M br?z-, N barázidan] shine, gleam. ~išn: radiance, brightness.
PHD.txt:1094:brightness, brilliance Һат, brāzišn, frog, payrég, spig.
PHD.txt:2108:gleam brāzidan.
PHD.txt:3315:radiance brāzīšn; v. brilliance.
PHD.txt:3316:radiant brāzišnīg.
PHD.txt:3630:shine brāzīdan, drafšīdan, frēgīh- istan, tāftan, (tābīdan).
PHD.txt:3631:shining brāzišnīg; v. bright.
PHD_mackenzie.txt:1618:brazidan, braz- [bt>c~ytn' I M br)z-, N bariizidan] shine, gleam.
PHD_mackenzie.txt:11108:brazidan                           bob, buf                        ~
=== HRN barāz ===
2099:aw. bräza-f brOzaiü 'er strahlt'; phlv. braz(i)sah
15079:bräza- 193.
15080:bräzaiti 193.
15735:bräzOßak 10, 193.
15736:I bräzfißoHh 10, 193.
19133:bräztin 201.
=== HUB ===
=== CHEUNG brāz ===
```


## [2026-09-05T13:49:31.175Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2085,2110p' HRN.txt\necho \"=== which leaf ===\"\npython3 - <<'EOF'\ndata=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\nidx=sum(len(l)+1 for l in lines[:2098])\nprint('leaf', data[:idx].count('\\f'), 'printed p.', data[:idx].count('\\f')-21)\nEOF\necho \"=== CHEUNG braz ===\"; grep -n -i \"braz\" CHEUNG.txt | head -10",
 "description": "Horn entry 193 context"
}
```


### [2026-09-05T13:49:32.902Z] TOOL RESULT

```
(283), resp. gvar (136); wa/. sar. war,
Geiger, Etymol. des Balü^i s. v. gvar (136), macht
darauf aufmerksam, dass in np. her eine von her
*Brust' gebildete nominale Praeposition und upari zu-
sammengeflossen sind. Np. her- kommt auch als Prae-
fix vor.
ü:^. hiräder *Bruder .
a ap. hrätar^ *Bruder' ; aw. bratar^; phlv. brätar, brät ^);
p/;^ ai. bhrdtar-; arm. ekbair (H. No. 91).
' kurd. barä; afy. wrör; oss. d. arwäde, erwOde
*Bruder, t. arwäd 'Verwandter* (30); bei. brät n.
bräs etc. (38); wa/. wrüt, si/n. w'rod, sar. wrödy
sangl. tt'wrd.
193. herä» *Schmuck, Schönheit*, berüzlden, berOzis^),
aw. bräza-f brOzaiü 'er strahlt'; phlv. braz(i)sah
geschmückt*, braz(i)saklh (AV.) ; ai. bhrajd-, bhrajate
glüht, strahlt, funkelt*. Also zu gr. (fkeyro, (pXnlE.
194. heräl 'wegen*, ez berai^ -ra.
ap. rädiy 'wegen'; phlv. rät,
kurd. araz 'für.
195. berd 'packe dich*^).
i^vart-; s. gerdiden (No. 886).
196y bürden 'tragen', Praes. ber-em^ berde^).
"^^ ' g. bartmün; Käs. bertän^ bardin, bardemün, bebSrt;
mäz. bavarden^ gel. barden.
*) Np. 6erä<? in den Patet's.
=== which leaf ===
leaf 66 printed p. 45
=== CHEUNG braz ===
2606:*AVESTAN: YAv. braz- ‘to shine’ — Liste: 40 
2608:Pres. them.: IND. 3sg. YAv. brazaiti (Yt 10.143), INJ. med. 3pl. YAv. brazonta (Yt 5.129) 
32122:Schwartz 1990: Martin Schwartz, Hospitalities and formalities (Vwaz, Vbraz), Fs 
33318:braz-, 21
```


## [2026-09-05T13:49:42.997Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2590,2640p' CHEUNG.txt",
 "description": "Cheung braz entry"
}
```


### [2026-09-05T13:49:43.044Z] TOOL RESULT

```
*SANSKRIT: bhisáj- (m.) ‘healer, physician’ (RV+) = EWAia II: 264 

© The denominative form bisaz derive from a noun *bis, which is continued in YAv. 
bis- (6151$ framätö ‘skilled in medicine’, F 576), Y Av. paiti.bisi- ‘medicinal, healing’ 
(Y 10.18), cf. Klingenschmitt 1968: 171 ff. This root has no IE etymology and may 
reflect an ancient cultural borrowing, on which see Lubotsky, Early Contacts: 310. 
The forms with a long vowel in the first syllable reflect an ablauting (denominative) 
variant: *baisaz. 


“PIE LIV: — | Pok.: 
*REFERENCES: Werba 1997: 432; Cabolov 2001: 196 


*braHz ‘to shine, set on fire, alight’ 

*AVESTAN: YAv. braz- ‘to shine’ — Liste: 40 

Pres. them.: IND. 3sg. YAv. brazaiti (Yt 10.143), INJ. med. 3pl. YAv. brazonta (Yt 5.129) 

*MIDDLE PERSIAN: MMP br’z- ‘to shine’ (LW), ВМР БГА /bräh/ ‘splendour, beauty’ 
(genuinely Pers.) > DMMPP: 110a 

Pres.: IND. 3sg. MMP br’zyd, 3pl. MMP br’zynd, SUBJ. 3sg. MMP br’z’d; Partic.: perf. pass. MMP 
br’zyst- 

*PARTHIAN: br’z- ‘to shine, gleam’ || (+ *ui-) wybr’z- ‘to shine, be lit up’ = Ghilain: 
59 | DMMPP: 110a 


22 *braiH 


Pres.: IND. br’zyd; Partic.: pres. br’z’g ‘shining’ || (+ *ui-) Pres.: IND. 3sg. (?) “wybr’zyd; Partic.: perf. 
pass. II wybr’z’d 

*SOGDIAN: BSogd. fr’’z’’nt ‘shining’, BSogd. Br’’zyntk, MSogd. Br’zn(d)tyy 
‘ablaze’ || (+ *a-) CSogd. *br’z ‘to be lit up, become angry’, ? CSogd. ’bryZ (caus.) 
‘to light, set on fire’, BSogd. "D'rxs'k, BSogd. ’’Brxs’kw ‘wish, desire, lust’, 
MSogd. ”’Brxsyy ‘desire, lust’, SSogd. ’’Brxs’kmync ‘lascivious’ (cf. Sims-Williams 
1976: 49 f.) 

(+ *4-) Impf.: IND. 3sg. CSogd. ’br’z; Partic.: perf. pass. CSogd. ’br’zc (f.) ‘lit up, angry’, CSogd. ’br’ztr 
(compar.) ‘angrier’; Caus.: pres. OPT. 3pl. CSogd. ’br<yZy>nt 

*CHORESMIAN: (+ *4-) m/’br’z- ‘to burn, light up’, (caus.) m/’br’zy- ‘to lit (fire)’; 
’br’z ‘flame’ (450.1) = Samadi: 1 

*NWIR: NP barazidan/baraz- ‘to shine, beam’ 

*MISC: Огт. bras-/brastak ‘to burn [intr.]’ = brés-/bréSok, bróxtok
```


## [2026-09-05T13:49:52.705Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2640,2665p' CHEUNG.txt",
 "description": "Cheung braz continued"
}
```


### [2026-09-05T13:49:52.746Z] TOOL RESULT

```
*MISC: Огт. bras-/brastak ‘to burn [intr.]’ = brés-/bréSok, bróxtok 

*SANSKRIT: bhräj ‘to shine, beam’ (RV+) = EWAia II: 279 

«PIE *b'reH;é- ‘to shine’ = LIV: 92 | Pok.: 139 f. 

*IE COGNATES: Lith. bréksti ‘to break [of day], dawn’, Pol. o-brzasknaé ‘to become 
light’ 

*REFERENCES: IIFL I: 389b f.; Werba 1997: 467; Kiefer 2003: 193; ESIJa II: 184 ff. 


*braiH ‘to shave, shear, cut’ 


*AVESTAN: (+ *pari-) Y Av. pairi.bri- ‘to shave, shear’ = Liste: 40 
MED.; Pres. them. nà-: IND. 3р1. YAv. pairi.brinonte (V 17.2), INJ. 25р. Y Av. pairi.brinagha (V 17.4) 


*MIDDLE PERSIAN: MMP bryn-, BMP blyn- (PSKWN-) /brin-/ ‘to cut off, MMP 
bwr-, BMP bwr- /bur-/ ‘to cut off, sever’ (secondary formation, cf. Hübschmann 


1895: 28) = DMMPP: 111a, 117b 
Pres.: IND. 3sg. MMP brynyd || Pres.: IND. 3pl. MMP bwrynd, IMPV. 2sg. MMP bwr, Partic.: perf. pass. 
BMP blyt, BMP bwlytk /bridag/ (or /bur(r)idag/ ?), MMP bryd, Inf.: BMP /bridan/
```


## [2026-09-05T13:49:54.193Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"brew,\" \"bread,\" \"broth,\" \"breed,\" \"ferment,\" \"fervent,\" \"brand,\" \"breath,\" \"burn,\" \"braise,\" \"breeze,\" \"birch,\" \"bright,\"; do\n echo \"--- $w\"; grep -n -m2 \"^$w\\|^ *$w\" KLN_1966.txt | head -3\ndone",
 "description": "Grep Klein headwords"
}
```


### [2026-09-05T13:49:56.127Z] TOOL RESULT

```
--- brew,
5615:brew,  tr.  and  intr.  v.  —  ME.  brewen,  fr.  OE.  bre- owan,  rel.  to  OS.  breuwan,  ON.  brugga,  Dan. brygge,  Swed.  brygga,  Norw.  brugga,  bryggja, OFris.  briiiwa,  MDu.  brouwen,  bruwen,  Du. brouwen,  OHG.  briuwan,  MHG.  bruwen,  brou¬ wen,  G.  brauen,  ‘to  brew’,  MLG.  broien,  MDu. broeyen,  MHG.  briiejen,  brtien,  G.  briihen,  ‘to scald’,  fr.  I.-E.  base  *bheru-,  *bhreu-,  *bhrd-,  ‘to boil,  ferment’,  whence  also  OI.  bhurv-anih,  ‘wild, turbulent’,  bharnih,  ‘violent,  passionate’.  Arm. albeur  (gen.  aiber),  ‘source’,  Gk.  <pop6veiv, tpopuoaew,  ‘to  knead  together,  soil,  bespatter’, <pp(ap  (gen.  <ppeaxo<;),  ‘well,  spring’  Thracian Gk.  PpOxoc  (fjpouxoi;  in  Hesychius),  ppuxov.
--- bread,
5581:bread,  n.  —  ME.  breed,  brede,  fr.  OE.  bread, ‘morsel,  crumb,  bread’,  rel.  to  OS.  brod,  ON. brand,  Dan.  brod,  Swed.  brod,  OFris.  brad,  MDu. brot,  broot,  Du.  brood,  OHG.,  MHG.  hot,  G. Brot,  fr.  Teut.  *brauda,  lit.  ‘bread  leavened  with barm’ ;  cogn .  with  Thracian  Gk.  ppuroi;  (Ppouxo; in  Hesychius),  flputov,  ‘fermented  liquor  made from  barley’,  L.  de-frutum,  ‘must  boiled  down’. These  words  are  formed  with  the  l.-E.  pp.  suff. -to  fr.  base  *bhreu-,  *bhru-,  ‘to  boil,  ferment’, whence  also  OE.  breowan,  ON.  brugga,  ‘to brew’.  See  brew  and  cp.  words  there  referred  to. Derivative:  bread,  tr.  v.
--- broth,
--- breed,
5594:breed,  tr.  and  intr.  v.  —  ME.  breden,  fr.  OE.  bre-
--- ferment,
14582:ferment,  n.  —  F.,  fr.  L.  fermentum,  ‘substance causing  fermentation’,  fr.  I.-E.  base  *bher-, ‘to  boil  up,  seethe'.  See  barm  and  cp.  fervent. Cp.  also  fry,  ‘to  cook  in  fat’.  For  the  ending see  suff.  -ment.
14583:ferment,  tr.  and  intr.  v.  —  F.  fermenter,  fr.  V.  fer¬ ment  are,  ‘to  ferment’,  fr.  fermentum.  See  fer¬ ment,  n.
--- fervent,
14611:fervent,  adj.,  i)hot;  2)  deeply  earnest;  ardent.  — L.  fervens,  gen.  -entis,  pres.  part,  of  fervere,  ‘to boil,  glow,  foam’,  fr.  I.-E.  base  *bheru-,  en¬ larged  form  of  *bher-,  ‘to  boil,  seethe’,  whence also  L.  defrutum ,  ‘must’.  See  barm  and  -ent  and cp.  ferment.
--- brand,
5538:brand,  n.  —  ME.  brand,  brond,  fr.  OE.  brand, brond,  ‘firebrand,  fire,  torch,  sword’  (the  mean¬ ing  ‘sword’  is  derived  from  the  flashing  of  the blade),  rel.  to  ON.  brandr,  ‘firebrand,  blade  of sword’,  OHG.,  MHG.  brant,  OFris.  brond,  of s.m.,  Dan.,  Swed.,  Du.,  G.  brand,  ‘firebrand, fire’;  formed  from  the  base  of  OE.  beornan,  etc., ‘to  burn’  (see  burn,  v.),  with  suff.  -pa(  -  l.-E.  -to). Cp.  OF.  brant,  ‘blade  of  a  sword,  sword’.  It.  bran- do  (poet.),  ‘sword’,  F.  brandon,  ‘firebrand,  torch’, which  are  Teut.  loan  words.  Cp.  also  brandish, brandy,  brindled,  the  first  element  in  brandreth and  the  second  element  in  Hildebrand, brandish,  tr.  v.  —  ME.  brattndisen,  fr.  OF.  bran- diss-,  pres.  part,  stem  of  brandir,  fr.  brant, ‘blade  of  a  sword,  sword'.  See  brand  and  verbal suff.  -ish.
--- breath,
--- burn,
5919:burn,  n.,  a  brook,  water  (Scot,  and  dial.  Engl.)  — ME.  burne,  fr.  OE.  brunna,  burna.  See  bourn, ‘stream’.
5920:burn,  tr.  and  intr.  v.  —  ME.  birnen,  bernen, bremten,  fr.  OE.  beornan,  biernan,  brinnan  (intr.), b»rnan( tr.),  rel.  to  ON.  brenna,  brinna  (intr.), brenna  (tr.),  MDu.  bernen,  Du.  branden,  OS., OHG.  brinnan ,  MHG.  brinnen  (intr.),  OHG. brennan,  MHG.  brennen  (tr.),  G.  brennen,  Goth. brinnan  (intr.),  brannjan  (tr.),  ‘to  burn’ ;  fr.  I.-E. base  *bhreu-,  ‘to  boil’.  See  brew  and  words  there referred  to  and  cp.  esp.  bourn,  burn,  ‘brook’, brand,  brindled.
--- braise,
--- breeze,
5599:breeze,  n.,  a  light  wind.  —  F.  brise,  prob.  fr.  Sp. brisa,  ‘north-east  wind’;  not  related  to  F.  bi.se, ‘dry  and  cold  north  wind’  (see  bise). Derivatives:  breeze ,  intr.  v.,  breez-y,  adj.,  breez- i-lv ,  adv.,  breez-i-ness,  n. breeze,  n.,  refuse  from  charcoal  or  coke.  —  F. braise,  ‘cinders,  live  coal’.  See  braise, bregma,  n.,  front  part  of  the  head  ( craniometry ). Gk.  Ppsypa,  ‘front  part  of  the  head’,  rel.  to $peyu.6q,  of  s.m.,  and  cogn.  with  OE.  brsegen, ‘brain’;  see  brain.  The  name  bregma  was  intro¬ duced  into  craniometry  by  the  French  surgeon and  anthropologist  Paul  Broca  (1824-80). Derivatives:  bregm-ate,  bregm-alie,  adjs. brehon,  n.,  one  of  a  class  of  judges  in  ancient  Ire¬ land.  —  Ir.  breitheamh,  fr.  OIr.  brilhem,  gen. brithemon ,  ‘judge’,  fr.  breth,  ‘a  bearing;  judg¬ ment'.  which  is  rel.  to  biru,  ‘I  bear’,  and  cogn. with  L.  ferre,  ‘to  bear,  carry’.  See  bear,  ‘to carry’.
--- birch,
--- bright,
5650:bright,  adj.  —  ME.  briht,  fr.  OE.  beorht,  bryht, rel.  to  OS.  berht ,  ON.  bjartr,  Norw.  bjerk,  OHG. beraht,  MHG.  birlit,  Goth,  bairhts,  ‘bright’,  fr. I.-E.  base  *bhereg-,  ‘to  shine,  be  white’,  whence also  OI.  bhrdjate,  ‘shines,  glitters',  Lith.  breksta, breksti,  ‘to  dawn’.  W.  berth,  'bright,  beautiful’. Cp.  birch.  Cp.  also  Bertha,  the  first  element  in Bardolph,  Bertram,  and  the  second  element  in Albert,  Cuthbert,  Egbert,  Ethelbert,  filbert,  gil¬ bert,  Herbert,  Hubert,  Lambert,  Robert,  I.-E ,  base *bhereg-  is  rel.  to  base  *bherek-,  ‘to  shine,  be white’ ;  see  braid  and  cp.  words  there  referred  to. Bright’s  disease,  chronic  nephritis.  —  So  called after  the  English  physician  Richard  Bright  ( 1789-
```


## [2026-09-05T13:50:06.137Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in breath broth breed birch braise Albert brandy barm brood; do\n echo \"--- $w\"; grep -n -o \"  $w,  [a-z. ]\\{0,20\\}—.\\{0,700\\}\" KLN_1966.txt | head -2\ndone",
 "description": "Klein more headwords"
}
```


### [2026-09-05T13:50:07.945Z] TOOL RESULT

```
--- breath
17085:  breath,  exhalation.  —  L.  halitus, ‘breath’,  rel.  to  halare,  ‘to  breathe’.  See  exhale, hall,  n.  —  ME.  halle,  hal,  fr.  OE.  heall,  hall,  rel. to  OS.,  OHG.  halla,  MHG.,  G.  halle,  Du.  hal, ON.  holl,  ‘hall’,  and  to  OE.  hell,  Goth,  halja, ‘hell’,  fr.  I.-E.  base  *kel-,  ‘to  hide,  conceal’, whence  also  OE.,  OS.,  OHG.  helan ,  OFris.  hela, MDu.  helen,  Du.  (ver)helen,  MHG.  heln,  G. hehlen,  ‘to  conceal’,  OI.  sdla,  ‘hut,  house,  hall, stable’,  salah,  ‘hedge,  enclosure,  wall’,  Gk.  xaXii, ‘hut,  nest’,  xaXuPr;,  ‘hut,  cabin’,  xaXuKTetv,  ‘to cover,  hide,  conceal’,  OIr.  cuile,  ‘cellar,  magazine’, L.  cella,  ‘store  room,  granary;  cell’,  celdre,  ‘to h
--- broth
--- breed
--- birch
--- braise
--- Albert
13718:  Albert,  which derives  —  through  the  medium  of  French  —  fr. OHG.  Adalbert,  the  exact  equivalent  of  OE. /Edclbryht,  and  cp.  words  there  referred  to. Etheldred,  fern.  PN.  —  OE.  Mdeldryd,  lit.  ‘of noble  strength’,  compounded  of  xdele,  ‘noble’, and  dryd,  ‘strength’.  For  the  first  element  see atheling.  The  second  element  is  rel.  to  ON. prudr,  ‘strength’,  ON.  pro-ask,  ‘to  thrive’, proskr,  ‘strong’,  OHG.  triuwen,  ‘to  blossom, flourish’,  trouwen,  ‘to  grow’,  MHG.  druo,  ‘fruit’. Ethelinda,  fern.  PN.  —  Formed  fr.  OE.  xdele, ‘noble’,  and  lindi,  ‘a  serpent’.  For  the  first element  see  atheling  and  cp.  the  two  prec.  words. The  second  element  is 
--- brandy
--- barm
--- brood
```


## [2026-09-05T13:50:13.310Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in breath broth breed birch braise brandy barm brood; do\n echo \"--- $w\"; grep -n -o \"$w, *n\\?[a-z]*\\.\\{0,3\\} *[a-z. ]\\{0,15\\}— *.\\{0,600\\}\" KLN_1966.txt | head -1\ndone",
 "description": "Klein headwords retry"
}
```


### [2026-09-05T13:50:26.445Z] TOOL RESULT

```
--- breath
ugrep: error: error at position 91
n\x80-\xbf][\x80-\xbf]*){0,600}
  exceeds complexity limits___/


--- broth
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,600}
 exceeds complexity limits___/


--- breed
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,600}
 exceeds complexity limits___/


--- birch
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,600}
 exceeds complexity limits___/


--- braise
ugrep: error: error at position 91
n\x80-\xbf][\x80-\xbf]*){0,600}
  exceeds complexity limits___/


--- brandy
ugrep: error: error at position 91
n\x80-\xbf][\x80-\xbf]*){0,600}
  exceeds complexity limits___/


--- barm
ugrep: error: error at position 89
x80-\xbf][\x80-\xbf]*){0,600}
exceeds complexity limits___/


--- brood
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,600}
 exceeds complexity limits___/
```


## [2026-09-05T13:50:30.483Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor w in ['breath','broth','breed','birch','braise','brandy','barm','brood','Bertha']:\n    m=re.search(re.escape(w)+r',\\s+[a-z.,\\s]{0,25}—',t)\n    if m:\n        print('---',w)\n        print(t[m.start():m.start()+700].replace('\\n',' '))\n    else:\n        print('---',w,'NOT FOUND')\nEOF",
 "description": "Klein entries via python regex"
}
```


### [2026-09-05T13:50:32.190Z] TOOL RESULT

```
--- breath
breath,  n.  —  ME.  breeth,  breth,  fr.  OE.  brxp,brep, ‘odor,  scent,  breath’,  rel.  to  OHG.,  brddam, MHG.  bradem,  G.  Brodem,  ‘breath,  steam’,  fr. I.-E.  base  bher-,  ‘to  boil’.  See  brew  and  cp. words  there  referred  to. Derivatives:  breath-less,  adj.,  breath-less-ly, adv.,  breath-less-ness,  n.,  breath-y,  adj. breathe,  intr.  and  tr.  v.  -  ME.  brethen,  fr.  breth. See  prec.  word. Derivatives:  breath-ed,  adj.,  breath-er,  n., breath-ing,  verbal  n.  and  pres.  part, breba,  n.,  fig  of  the  first  crop.  —  Sp.  breva,  meta¬ thesis  of  bevra,  of  s.m.,  fr.  L.  bifera,  fern,  of bifer,  ‘bearing  fruit  twice  a  year’,  which  is  com¬ pounded
--- broth
broth,  n.  —  ME.,  fr.  OE.  brod,  rel.  to  OHG.  brod, fr.  Teut.  base  *brauda-,  lit.  ‘anything  leavened’, cogn.  with  Thracian  Gk.  [JpO-rop  (fipou-ro;  in Hesychius),  ppurov,  ‘fermented  liquor  made from  barley,  beer’,  L.  defrutum,  ‘must  boiled down’,  Mir.  embruthe,  ‘broth’,  bruith,  ‘to  boil’, ModW.  brwd,  ‘hot’,  ModBret.  broud,  of  s.m.; fr.  I.-E.  base  *bhreu-,  *bhru-,  ‘to  swell’,  which is  enlarged  fr.  base  *bher-,  ‘to  boil’.  See  brew and  cp.  bread,  brood. brothel,  n.  —  ME.  brothel,  ‘worthless  person, prostitute’,  derived  fr.  OE.  broden,  pp.  of breodan,  ‘to  destroy’ ;  confused  in  meaning  with OF.  bordel,  ‘hovel’  (for  
--- breed
breed,  tr.  and  intr.  v.  —  ME.  breden,  fr.  OE.  bre- breeze brief 198 den,' to  cherish,  keep  warm,  nourish’,  rel.  to  Du, broeden,  OHG.  bruoten,  MHG.  briieten,  G.  brii- ten,  ‘to  brood,  hatch’,  fr.  I.-E.  base  *bher-,  ‘to boil'.  See  brew  and  cp.  words  there  referred  to. Derivatives:  breed,  n.,  breed-er,  n.,  breed-ing,  n., hreed-y,  adj. breeze,  n.,  a  light  wind.  —  F.  brise,  prob.  fr.  Sp. brisa,  ‘north-east  wind’;  not  related  to  F.  bi.se, ‘dry  and  cold  north  wind’  (see  bise). Derivatives:  breeze ,  intr.  v.,  breez-y,  adj.,  breez- i-lv ,  adv.,  breez-i-ness,  n. breeze,  n.,  refuse  from  charcoal  or  coke.  —  F. braise,  
--- birch
birch,  n.  —  ME.  birche,  fr.  OE.  bierce,  beorc,  rel. to  OS.  birka,  berka,  ON.  bork,  Dan.  birk ,  Swed. bjork,  Norw.  bjerk,  MDu.  berke,  Du.  berk,  OHG. birihha,  birka,  MHG.  birche,  birke,  G.  Birke, ‘birch’,  and  cogn.  with  Osset,  barz,  OSlav.  breza, Lith.  berzas,  Lett,  befza,  OPruss.  berse,  Russ. bereza,  OCzech  brieza,  OI.  bhurjdh,  ‘birch’,  L. farnus,fraxinus,  ‘mountain  ash’.  All  these  words lit.  mean  ‘the  white  (or  bright)  tree’  and  derive fr.  I.-E.  base  *bhereg-,  ‘to  shine,  be  white’.  See bright  and  cp.  Fraxinus,  fraxinella. Derivatives:  birch,  adj.  and  tr.  v.,  birch-en,  adj., birch-ing,  n. bird,  n.  —  ME.  brid
--- braise NOT FOUND
--- brandy
brandy,  n.  —  Shortened  fr.  earlier  brandwine, brandewine,  fr.  Du.  brandewijn,  lit.  ‘distilled wine’,  fr.  branden,  ‘to  burn’,  whence  ‘to  distil’, and  wjn,  ‘wine’.  For  the  first  element  see  burn, v.,  and  cp.  brand,  for  the  second  see  wine.  Cp. G.  Branntwein ,  ‘brandy’.  Cp.  also  Czech pdlenka, ‘brandy’,  and  its  equivalents  in  the  other  Slavic languages,  fr.  pdliti,  etc.,  ‘to  burn’. Derivative:  brandi-ed,  adj. brandypawnee,  n.,  brandy  and  water  ( Anglo - Ind.)  —  A  hybrid  coined  fr.  E.  brandy  and  Hind. pani,  ‘water’. brangle,  intr.  v.,  to  wrangle  (archaic).  —  Prob. a  var.  of  wrangle.  Cp.  embrangle. Derivative :  bran
--- barm
barm,  n.,  yeast.  —  ME.  berme,  fr.  OE.  beorma, rel.  to  Du.  berm,  MLG.  berm,  barm,  LG.  barme (whence  G.  Barme),  and  cogn.  with  L.  fermen- tum,  ��substance  causing  fermentation’,  fr.  I.-E. base  *bher-,  ‘to  boil,  seethe’,  whence  also  OI. bhurati,  ‘moves  convulsively,  quivers’,  Mir. berbaim,  ‘I  boil,  seethe’.  Cp.  brand,  bread,  brew, broil  (in  both  senses),  broth.  Cp.  also  ferment. bar  mitzvah,  a  male  person  who  has  completed his  thirteenth  year,  when  he  reaches  the  age  of religious  responsibility  ( Jewish  religion).  — Heb.  bar  mitzvdh,  lit.  ‘son  of  command’,  fr.  bar, ’son’,  which  is  rel.  to  Heb.  ben,  and  mitz
--- brood
brood,  n.  —  ME.  brod,  fr.  OE.  brod,  lit.  ‘that which  is  hatched  out  by  warmth’,  rel.  to  Du. broed,  MHG.  bruot,  G.  Brut,  ‘brood’,  and  to MLG.  brdien,  MDu.  broeyen,  MHG.  briieyen , briien,  G.  briihen,  ‘to  scald’.  See  brew  and  cp. words  there  referred  to. Derivatives:  brood,  v.  and  adj.,  brood-er,  n., brood-ing,  adj.,  brood-ing-ly ,  adv.,  brood-y,  adj. and  n. brook,  n.,  a  small  stream  of  water.  —  ME.  broc, fr.  OE.  broc,  rel.  to  LG.  brok,  Du.  broek, OHG.  bruoh,  MHG.  bruoch,  G.  Bruch,  ‘marshy ground’,  and  to  E.  break.  Brook  orig.  denoted ‘that  which  breaks  out  of  the  earth’. Derivative:  brook-y,  adj. brook, 
--- Bertha NOT FOUND
```


## [2026-09-05T13:50:51.609Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 بلوا ===\"; grep -n \"بلوا\\|بلوی\\|بلوٰی\" BQT_v1_pages.txt | head -10\necho \"=== ARY بلوا ===\"; grep -n \"بلوا\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== HRN belva ===\"; grep -n -i \"belwä\\|belva\\|balwa\" HRN.txt HUB.txt | head -5\necho \"=== SKT braise/brew ===\"; python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor w in ['BRAISE','BREW','BREAD','FERVENT','BURN','BREATH','BRIGHT','BIRCH']:\n    m=re.search(r'\\b'+w+r'\\b',t)\n    print('---',w, (t[m.start():m.start()+400].replace('\\n',' ') if m else 'NOT FOUND'))\nEOF",
 "description": "Grep for balva and Skeat entries"
}
```


### [2026-09-05T13:50:53.752Z] TOOL RESULT

```
=== BQT v1 بلوا ===
1124:۷- خسرو قبلوان وربدك وی» ترجمهٌ نکارنده. مجلهٌ آموزش وپرررش سالع۱ ۰.۷۵۲
20777:بلواله - با
20780:آن پرنده است که بعربی بلوابه
26280:بلواس « باوار بروزن المای » پنعنی
=== ARY بلوا ===
2158:انگلیسی (بلواه/(6): 0 9 (0788) رادم
2701:پهلری (۵(1ا3ل۳۸): ۸۸00 انگلیسی ربلواا6۸0): ۱۱ انا
6403:انگلیسی کهن (بلوابا80 صا0): 2 و9 :0515
9605:لهستانی (بلوارا۳۵): ه۸ 7 پسگشت‌ها ک 3 ۱
11543:آلمانی کهن (0270440 بلواتز صان): َ :28 اهر
=== HRN belva ===
=== SKT braise/brew ===
--- BRAISE NOT FOUND
--- BREW BREW. braoketh  a  corbel,  ftc  (F.<«C.)  F» merly  spelt  bmgget,  as  in  Mioshin,  el 1627.  So  named  from  the  rescmbUnoeto the  front  part  of  a  pair  of  bivecha,  is formerly  made.— F.^/U!fitf//««  'a  cod[Nec^* Cot  (the  front  part  of  a  pair  of  brenhes); the  allied  Span,  bingueta  also  meant  1 projecting  mould  in  architectoce,  a  btadut or  corbel  Dimin.  of  O.  F
--- BREAD NOT FOUND
--- FERVENT NOT FOUND
--- BURN BURN. na.  G«eL  ivrr-^U/t  swncgering, Src  BiUT. (i>.verb.  (EL)    M.  E.  ^cmm;  also A.  S.  Aefiman,  byman.  i>nmnaM, verb,  pit  L  i^^m,  tran,  pp  bcmin, n;   alio  /rnnam.  Atfrwan.  bunnan, Kvb>.  ^  led.  AnrwM.  Can.  ^ntnJi, ^wtow;    G.  ^ranjvrw;  Gotb.  ^Wm* ^     IVihApt  allied  to   LaL  feruitt,  to BUSS. 57 i;  piece  of  wood»  scar  of (  M.  E.  ^rond^  A.  S. }d,  a  Im
--- BREATH NOT FOUND
--- BRIGHT NOT FOUND
--- BIRCH NOT FOUND
```


## [2026-09-05T13:51:08.315Z] TOOL CALL #35: Bash

```json
{
 "command": "head -40 tools/fetch_source.py && echo ... && python3 tools/fetch_source.py --help 2>&1 | head -20",
 "description": "Inspect fetch_source.py"
}
```


## [2026-09-05T13:51:08.425Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T13:51:10.154Z] TOOL RESULT

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
...
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


### [2026-09-05T13:51:10.158Z] TOOL RESULT

```


```


## [2026-09-05T13:51:20.017Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0rewh%E2%82%81-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0re%CA%B0%C7%B5-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/brinnan%C4%85\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/brandaz\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/br%C4%93%C3%BEaz\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%A7%D8%B2%DB%8C%D8%AF%D9%86\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 91 verification (Bher5/bhreu-, Bhereg)\" 2>&1 | tail -2\ndone",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-05T13:51:24.980Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2ac1a027f1c99e23.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/64e79609d0be30fd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/deede849e74fdd1e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4891fdcac285dbcc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c22d16559c0f9cc5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c8937881f8ca82b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/745e236e6d16c36d.txt
```


## [2026-09-05T13:51:28.279Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 2ac1a027f1c99e23 64e79609d0be30fd; do echo \"########## $f\"; head -c 300 $f.txt; echo; grep -n -A20 \"Proto-Indo-European\\[edit\\]\\|Root\\[edit\\]\\|Etymology\\[edit\\]\" $f.txt | head -60; done",
 "description": "Read PIE wiktionary pages"
}
```


### [2026-09-05T13:51:30.165Z] TOOL RESULT

```
########## 2ac1a027f1c99e23
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0rewh%E2%82%81-
FETCHED: 2026-09-05T13:51:21Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/bʰrewh₁- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/bʰrewh₁- - Wiktionary, the free dictio
########## 64e79609d0be30fd
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0re%CA%B0%C7%B5-
FETCHED: 2026-09-05T13:51:22Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T13:51:34.876Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0reh%E2%82%81%C7%B5-\" --note \"page 91, root Bhereg 'to shine'\" 2>&1|tail -1\nsed -n '1,140p' data/verification/sources/web/2ac1a027f1c99e23.txt | sed -n '5,140p'",
 "description": "Fetch bhreh1g- and read bhrewh1-"
}
```


### [2026-09-05T13:51:37.053Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/96ce948a8f51f3ef.txt

Reconstruction:Proto-Indo-European/bʰrewh₁- - Wiktionary, the free dictionary 

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
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Etymology 

 1.2 
 Root 

 1.2.1 
 Alternative reconstructions 

 1.2.2 
 Derived terms 

 1.3 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ bʰrewh₁- 

 Add languages 

 Reconstruction 

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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 A user suggests that this Proto-Indo-European reconstruction entry be moved, merged or split.

 Please see the discussion on Requests for moves, mergers and splits ( + ) or the talk page for more information and remove this template after the request has been fulfilled.
```


## [2026-09-05T13:51:39.633Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk 'NR>140 && NR<260' 2ac1a027f1c99e23.txt | tr -s '\\n' '\\n' | head -80",
 "description": "Read bhrewh1 body"
}
```


### [2026-09-05T13:51:41.051Z] TOOL RESULT

```
 Etymology
 [ edit ] 
 Extension of *bʰer- ( “ to boil ” ) . [ 1 ] 
 Root
 [ edit ] 
 *bʰrewh₁- [ 2 ] [ 3 ] [ 4 ] 
 to boil 
 to brew 
 Alternative reconstructions
 [ edit ] 
 *bʰrew- [ 2 ] 
 *bʰerw- [ 5 ] ( this root structure is probably not possible [ 6 ] ) 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *bʰrewh₁- (62 c, 0 e) 
 *bʰrewh₁-e- ( thematic present ) 
 Proto-Germanic: *brewwaną ( “ to brew ” ) ( see there for further descendants )
 *bʰrowh₁- ( o-grade ) 
 Proto-Albanian: *brāu 
 Albanian: mbruaj 
 *bʰrenw- ( nasal infix present ) 
 > ? Proto-Germanic: *brinnaną ( see there for further descendants )
 *bʰréh₁wr̥ 
 *bʰrowh₁-tó- 
 > ? Proto-Germanic: *braudą ( “ bread ” ) ( see there for further descendants )
 *bʰru(h₁)-to- 
 Thracian: *brutas ( in the masculine ) 
 → Ancient Greek: βρῦτος ( brûtos ) 
 Proto-Celtic: *brutom ( in the neuter ) 
 Welsh: brwd 
 Cornish: bros 
 Proto-Germanic: *bruþą ( “ broth ” , in the neuter ) ( see there for further descendants )
 Proto-Italic: *frutom ( in the neuter ) 
 Latin: dēfrutum , dēfritum 
 *bʰréwmn̥- [ 7 ] 
 Proto-Albanian: *bruma 
 Albanian: brumë 
 *bʰru-tis 
 Proto-Celtic: *brutis 
 Old Irish: bruith ( see there for further descendants )
 *bʰru-tus 
 Proto-Celtic: *brutus 
 Old Irish: bruth Irish: bruth 
 *bʰerw-ós 
 Proto-Celtic: *berwos ( see there for further descendants )
 *bʰorw-ós 
 Proto-Celtic: *borwos 
 Gaulish: Boruo 
 Unsorted formations 
 > ? Proto-Albanian: *britśiā 
 Albanian: bërsi 
 Ancient Greek: πορφῡ́ρω ( porphū́rō , “ to heave, boil, surge up ” ) 
 References
 [ edit ] 
 ^ Pokorny, Julius ( 1959 ), “ 2. bher- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 1, Bern, München: Francke Verlag, pages 132-133 
 ↑ 2.0 2.1 De Vaan, Michiel ( 2008 ), Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN 
 ^ Kroonen, Guus ( 2013 ), “*brewwan-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 76 
 ^ Philippa, Marlies; Debrabandere, Frans ; Quak, Arend; Schoonheim, Tanneke; van der Sijs, Nicoline ( 2003–2009 ), “ brouwen ”, in Etymologisch woordenboek van het Nederlands ‎ [2] (in Dutch), Amsterdam: Amsterdam University Press 
 ^ Rix, Helmut , editor ( 2001 ), “*bʰeru̯-”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 81 
 ^ Adiego, Iganasi-Xavier, et al. (2022) A little-known law on the root and syllable structure of Proto-Indo-European. Zurück zur Wurzel—Struktur, Funktion und Semantik der Wurzel im Indogermanischen. Akten der 15. Fachtagung der Indogermanischen Gesellschaft, vom 13. bis 16. September 2016 in Wien : page 3 of 1-14. 
 ^ Orel, Vladimir ( 1998 ), “ brumë ”, in Albanian Etymological Dictionary , Leiden; Boston; Cologne: Brill, →ISBN , page 38 : “ IE ” 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/bʰrewh₁-&oldid=92151206 "
 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European CReRH-shaped roots 
 ine-pro:Cooking 
 Hidden categories: Requests for moves, mergers and splits 
 Requests for attention concerning Proto-Indo-European 
 Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages with entries 
 Pages with 1 entry 
 Thracian terms with redundant script codes 
 This page was last edited on 23 August 2026, at 21:53.
 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
 Privacy policy 
 About Wiktionary
```


## [2026-09-05T13:51:49.742Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in deede849e74fdd1e 4891fdcac285dbcc c22d16559c0f9cc5; do echo \"########## $f\"; grep -n \"TITLE\" $f.txt; awk '/Etymology/{found=1} found' $f.txt | head -30; echo; done",
 "description": "Read Germanic wiktionary pages"
}
```


### [2026-09-05T13:51:51.258Z] TOOL RESULT

```
########## deede849e74fdd1e
4:TITLE: Reconstruction:Proto-Germanic/brinnaną - Wiktionary, the free dictionary
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Verb 

 1.3.1 
 Inflection 

 1.3.2 
 Derived terms 

 1.3.3 
 Related terms 

 1.3.4 
 Descendants 

 1.4 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Germanic/ brinnaną 

 1 language 

 Русский 

########## 4891fdcac285dbcc
4:TITLE: Reconstruction:Proto-Germanic/brandaz - Wiktionary, the free dictionary
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Inflection 

 1.3.2 
 Derived terms 

 1.3.3 
 Related terms 

 1.3.4 
 Descendants 

 1.4 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Germanic/ brandaz 

 Add languages 

 Reconstruction 

########## c22d16559c0f9cc5
4:TITLE: Reconstruction:Proto-Germanic/brēþaz - Wiktionary, the free dictionary
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Adjective 

 1.3.1 
 Declension 

 1.3.2 
 Alternative reconstructions 

 1.3.3 
 Related terms 

 1.3.4 
 Descendants 

 1.4 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Germanic/ brēþaz 

 Add languages 

 Reconstruction
```


## [2026-09-05T13:51:54.506Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in deede849e74fdd1e 4891fdcac285dbcc c22d16559c0f9cc5; do echo \"########## $f\"; awk '/^ Etymology$/{c++} c==2' $f.txt | head -25; echo; done",
 "description": "Read etymology sections"
}
```


### [2026-09-05T13:51:56.205Z] TOOL RESULT

```
########## deede849e74fdd1e

########## 4891fdcac285dbcc

########## c22d16559c0f9cc5
```


## [2026-09-05T13:51:59.019Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in deede849e74fdd1e 4891fdcac285dbcc c22d16559c0f9cc5; do echo \"########## $f\"; grep -n \"From \\|Proto-Indo-European\\|Derived from\\|Related to\" $f.txt | head -12; echo; done",
 "description": "Grep etymology lines"
}
```


### [2026-09-05T13:52:02.311Z] TOOL RESULT

```
########## deede849e74fdd1e
141: From Wiktionary, the free dictionary
151: Kroonen reconstructs Pre-Germanic *bʰrénuh₁e- , from Proto-Indo-European *bʰrewh₁- ( “ to boil, brew ” ) . [ 1 ] 
377: Categories : Proto-Germanic terms derived from Proto-Indo-European 
378: Proto-Germanic terms inherited from Proto-Indo-European 
379: Proto-Germanic terms derived from the Proto-Indo-European root *bʰrewh₁- 

########## 4891fdcac285dbcc
139: From Wiktionary, the free dictionary
149: From *brinnaną ( “ to burn ” ) +‎ *-az ( “ -er ” , agent noun suffix ) . [ 1 ] 
277: Categories : Proto-Germanic terms derived from the Proto-Indo-European root *bʰrewh₁- 

########## c22d16559c0f9cc5
139: From Wiktionary, the free dictionary
149: Related to Sanskrit भुरति ( bhurati , “ to stir, palpitate ” ) , both from Proto-Indo-European *bʰer- ( “ to boil, seethe ” ) . [ 1 ] By synchronic analysis, an adjectival formation from *brējaną ( “ to roast, waft ” ) . [ 2 ] 
385: Categories : Proto-Germanic terms derived from Proto-Indo-European
```


## [2026-09-05T13:52:14.242Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"###### بلوا\"; grep -n \"Persian\\|Arabic\\|From \\|بلوا\\|Etymology\" 4c8937881f8ca82b.txt | sed -n '1,40p'\necho; echo \"###### برازیدن\"; grep -n \"From \\|Middle Persian\\|Etymology\\|Avestan\\|Proto-Iranian\" 745e236e6d16c36d.txt | head -20",
 "description": "Read balva and barazidan pages"
}
```


### [2026-09-05T13:52:14.298Z] TOOL RESULT

```
###### بلوا
4:TITLE: بلوا - Wiktionary, the free dictionary
6:بلوا - Wiktionary, the free dictionary 
57: Arabic 
59: Toggle Arabic subsection 
66: بلوا 
126: From Wiktionary, the free dictionary
130: Arabic
136: بلوا ( form I ) 
145: Retrieved from " https://en.wiktionary.org/w/index.php?title=بلوا&oldid=81545026 "
147: Categories : Arabic non-lemma forms 
148: Arabic verb forms 
181: بلوا 

###### برازیدن
62: Etymology 
133: From Wiktionary, the free dictionary
138: Etymology
141: From Middle Persian brʾcytn' ( brāzidan , “ to shine, gleam ” ) , from Proto-Indo-European *bʰreh₁ǵ- ( “ to gleam, shine ” ) . 
209: Categories : Persian terms inherited from Middle Persian 
210: Persian terms derived from Middle Persian
```


## [2026-09-05T13:52:23.654Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%A7/\" --note \"page 91, Persian balvâ: Dehkhoda/Mo'in entry\" 2>&1|tail -1\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D9%89\" --note \"page 91, Arabic balwā root b-l-w\" 2>&1|tail -1\necho \"###### bhreh1g-\"\ngrep -n \"Root\\|to shine\\|Derived\\|Proto-Iranian\\|Proto-Indo-Iranian\\|Pokorny\" data/verification/sources/web/96ce948a8f51f3ef.txt | sed -n '1,30p'",
 "description": "Fetch balva sources; read bhreh1g"
}
```


### [2026-09-05T13:52:27.118Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c6d1088929ab0d82.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1ddec17b8b6fd73d.txt
###### bhreh1g-
```


## [2026-09-05T13:52:29.609Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nhead -8 96ce948a8f51f3ef.txt\necho \"=== body ===\"; awk 'NR>130' 96ce948a8f51f3ef.txt | head -60",
 "description": "Read bhreh1g page"
}
```


### [2026-09-05T13:52:31.139Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0reh%E2%82%81%C7%B5-
FETCHED: 2026-09-05T13:51:37Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found=== body ===
```


## [2026-09-05T13:52:40.223Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/berhtaz\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/berk%C5%8D\" \\\n \"https://en.wiktionary.org/wiki/breath\" \\\n \"https://www.etymonline.com/word/braise\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 91 verification\" 2>&1|tail -1\ndone",
 "description": "Fetch berhtaz, berkō, breath, braise"
}
```


### [2026-09-05T13:52:43.404Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f4fb50ae56f822b3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf2f2d63e69f205b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/315c6a04e6e5b73b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/565608dd3c098f06.txt
```


## [2026-09-05T13:52:46.587Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in f4fb50ae56f822b3 cf2f2d63e69f205b 315c6a04e6e5b73b 565608dd3c098f06; do echo \"###### $f\"; sed -n '4p' $f.txt; grep -n \"From \\|from Proto\\|Related to\" $f.txt | head -6; echo; done",
 "description": "Read fetched pages"
}
```


### [2026-09-05T13:52:48.205Z] TOOL RESULT

```
###### f4fb50ae56f822b3
TITLE: Reconstruction:Proto-Germanic/berhtaz - Wiktionary, the free dictionary
141: From Wiktionary, the free dictionary
151: From Proto-Indo-European *bʰer(H)ǵ-tó-s , from *bʰerHǵ- ( “ to shine ” ) +‎ *-tós . Cognate with Proto-Celtic *berxtos , Proto-Albanian *bardza ( “ white ” ) . [ 1 ] 
404: Categories : Proto-Germanic terms derived from Proto-Indo-European 
405: Proto-Germanic terms inherited from Proto-Indo-European 

###### cf2f2d63e69f205b
TITLE: Reconstruction:Proto-Germanic/berkō - Wiktionary, the free dictionary
139: From Wiktionary, the free dictionary
149: From Proto-Indo-European *bʰerHǵós . Cognate with Sanskrit भूर्ज ( bhūrjá , “ a species of birch ” ) , Proto-Slavic *berza ( “ birch ” ) . [ 1 ] 
252: Categories : Proto-Germanic terms derived from Proto-Indo-European 
253: Proto-Germanic terms inherited from Proto-Indo-European 

###### 315c6a04e6e5b73b
TITLE: breath - Wiktionary, the free dictionary
231: From Wiktionary, the free dictionary
248: From Middle English breeth , breth , from Old English brǣþ ( “ odor, scent, stink, exhalation, vapor ” ) , from Proto-West Germanic *brāþi ( “ vapour, waft, exhalation, breath ” ) (compare German Brodem ( “ haze, vapor; breath ” ) , of a different but related formation). [ 1 ] 
1012: Categories : English terms derived from Proto-Indo-European 
1014: English terms derived from Proto-Germanic 
1019: English terms inherited from Proto-West Germanic 
1020: English terms derived from Proto-West Germanic 

###### 565608dd3c098f06
TITLE: Braise - Etymology, Origin & Meaning
25: "to stew in a closed pan with heat from above and below," 1797, braze , from French braiser "to stew, cook over live coals" (17c.), from braise "live coals," from Old French brese "embers" (12c.), ultimately (along with Italian bragia , Spanish brasa ) from Proto-Germanic *brasa , from PIE root *bhreu- "to boil, bubble, effervesce, burn." Related: Braised ; braising .
60: "a part or portion," Middle English del, from from Old English dæl "a part of a whole, a share;" with qualification (great, etc.), "an extent, degree, quantity, amount," from Proto-Germanic *dailaz (source also of Old Norse deild, Old Frisian del "part; juridical district," Dutch
68: late Old English wyrre, werre "large-scale military conflict," from Old North French werre "war" (Old French guerre "difficulty, dispute; hostility; fight, combat, war;" Modern French guerre), from Frankish *werra, from Proto-Germanic *werz-a- (source also of Old Saxon werran, Ol
72: 1680s, "signal calling soldiers or sailors to quarters at night," earlier tap-to (1640s), from Dutch taptoe, from tap "faucet of a cask" (see tap (n.1)) + toe "shut, to" (from Proto-Germanic *to; see to (prep.)). "So called because police formerly visited taverns in the evening t
```


## [2026-09-05T13:52:59.519Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"###### abadis بلوا\"; sed -n '1,6p' c6d1088929ab0d82.txt; grep -n \"بلوا\" c6d1088929ab0d82.txt | head -30",
 "description": "Read abadis balva"
}
```


### [2026-09-05T13:52:59.583Z] TOOL RESULT

```
###### abadis بلوا
URL: https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%A7/
FETCHED: 2026-09-05T13:52:26Z
STATUS: 200
TITLE: بلوا - معنی در دیکشنری آبادیس

بلوا - معنی در دیکشنری آبادیس 
4:TITLE: بلوا - معنی در دیکشنری آبادیس
6:بلوا - معنی در دیکشنری آبادیس 
10: بلوا
13: مترادف بلوا : آشوب، ازدحام، اغتشاش، غوغا، ناامنی، فتنه، هرج ومرج، هنگامه، سختی، مشقت، گرفتاری، آزمایش، آزمودن
14: متضاد بلوا : آرامش، امنیت
22: بلوا. [ ب َل ْ ] ( از ع ، اِ ) بلوی. زحمت. ( غیاث اللغات ). مشقت : 
24:لیک حلوا بر خسان بلوا بود. مولوی.
26: بلوا. [ ب ُل ْ ] ( اِ ) در لهجه خراسانیان امروز، بالوایه قدما است یعنی پرستو. ( یادداشت مرحوم دهخدا ). 
55:مرکز اداری ولایت لوآر ـ اِ ـ شِر در مرکز فرانسه، کنار رود لوآر، به فاصلۀ ۵۵کیلومتری جنوب غربی اورلئان. جمعیت آن ۵۱,۵۰۰ نفر است (۱۹۹۰). اسقف نشین و دارای قلعه ا ی تاریخی است. صنایع آن عبارت اند از تولید ظروف چینی، جواهرات، کفش، و شکلات. در این ولایت تجارت شراب، الوار، و غله رواج بسیار دارد و مرکز مهم جهانگردی در درّۀ لوآر است. بلوآ در قرن ۶م بنا شد؛ تا قرون وسطا کنت های بلوآ از قدرت مندترین اشراف فئودال فرانسه بودند. در قرن ۱۴م، بلوآ مقرّ لوئی، دوک اورلئان، پدربزرگ لوئی دوازدهم، شد. در ۱۴۹۸م به فرانسه واگذار شد و در قرن ۱۶، بسیاری آن را پایتخت دوم فرانسه می دانستند. قلعۀ اولیه شهر در قرن ۱۳م ساخته شد، اما در قرن ۱۶ فرانسوای اول آن را به شیوۀ رنسانس بازسازی کرد. بعدها، بناهایی به سبک گوتیک و باروک به آن افزوده و به یکی از بزرگ ترین بناهای فرانسه تبدیل شد. از قرن ۱۵ تا ۱۷ اقامتگاه سلطنتی، محل تولد دوک شارل بلوا، و لوئی دوازدهم (۱۴۶۲م)، همچنین محل قتل دوک سوم گیز (۱۵۸۸) بود؛ کاترین دو مدیسی (مدیچی)، ملکۀ فرانسه، نیز در ۱۵۸۹ در این شهر درگذشت؛ شهر مزبور محل حبس ماری دو مدیسیتوسط پسرش، لوئی سیزدهم بود که پس از دو سال سرانجام از آن جا گریخت. گرچه بسیاری از بناهای قدیمی شهر در جنگ جهانی دوم نابود شدند، برخی از ساختمان های گوتیک و رنسانس باقی مانده اند. کلیسای سن نیکلا، که در گذشته صومعه بوده، نمونۀ بارزی از معماریِ قرن ۱۲م است. wikijoo: بلوآ 
60: غوغا، داد و بیداد، همهمه، غریو، بلوا، شورش، هنگامه
62: غوغا، اشوب، داد و بیداد، یاغیگری، فتنه، بلوا، طغیان، شورش
64: زد و خورد، قیل و قال، بلوا
66: خیز، بلوا، برخاستگی، طغیان، شورش، قیام، بر خیزش
77:بلوا : آشوب ؛ فتنه ؛ جنجال ؛ هنگامه ؛ هیاهو ؛ غوغا. . .
```


## [2026-09-05T13:53:08.924Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -B2 -A6 \"فرهنگ معین\\|معین\" c6d1088929ab0d82.txt | head -40\necho \"###### arabic بلوى\"; sed -n '4p' 1ddec17b8b6fd73d.txt; grep -n \"From \\|root\\|Etymology\\|بلو\" 1ddec17b8b6fd73d.txt | head -20",
 "description": "Mo'in section and Arabic balwa"
}
```


### [2026-09-05T13:53:08.987Z] TOOL RESULT

```
32-در لهج. خراسانیان امروز بالوای. قدماست یعنی پرستو . 
33-
34: فرهنگ معین
35-
36- (بَ ) [ ع . بلوی ] ( اِ. ) ۱ - شورش ، آشوب . ۲ - سرکشی . 
37-
38- فرهنگ عمید
39-
40- ۱. = بلیه
--
87- دیکشنری آبادیس
88-
89: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
90-
91- لینک ها 
92-
93- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
94-
95- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
###### arabic بلوى
TITLE:
```


## [2026-09-05T13:53:18.192Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '1,8p' 1ddec17b8b6fd73d.txt",
 "description": "Check arabic page status"
}
```


### [2026-09-05T13:53:18.235Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D9%89
FETCHED: 2026-09-05T13:52:27Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T13:53:26.214Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D8%A7%D8%A1\" --note \"page 91, Arabic balāʾ / root b-l-w for Persian balvâ\" 2>&1|tail -1",
 "description": "Fetch Arabic bala'"
}
```


### [2026-09-05T13:53:32.750Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/91f945e80930eb56.txt
```


## [2026-09-05T13:53:35.400Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '4p' 91f945e80930eb56.txt; grep -n \"From \\|root\\|ب ل و\" 91f945e80930eb56.txt | head -12",
 "description": "Read Arabic bala page"
}
```


### [2026-09-05T13:53:35.453Z] TOOL RESULT

```
TITLE: بلاء - Wiktionary, the free dictionary
139: From Wiktionary, the free dictionary
146: ب ل و ( b l w ) 
338: Categories : Arabic terms belonging to the root ب ل و
```


## [2026-09-05T13:53:57.165Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor n in (17408,17452):\n    seg=lines[max(0,n-60):n+8]\n    nums=[l.strip() for l in seg if re.fullmatch(r'\\s*\\d{3,4}\\s*',l)]\n    print('line',n,'nearby column numbers:',nums[-6:])\n    print('\\n'.join(l for l in lines[n-3:n+8]))\n    print('---')\nEOF",
 "description": "Find Bartholomae column for braz"
}
```


## [2026-09-05T13:53:58.097Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls incoming/WLD/ 2>/dev/null; grep -n \"bhereu\\|bh(e)reu\\|bheru-\\|bhreu-\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "Grep Walde-Pokorny Bd2"
}
```


### [2026-09-05T13:53:59.075Z] TOOL RESULT

```
line 17408 nearby column numbers: ['969', '970', '971']
971
byah-
bräza-
97z
•  j.  byah-  V.  'Schreck  erregen'.  Pcrf.  1 1 biwynh-.  \
'Schreck  erregen,  furchtbar  sein':   aca  |
äfars  zasia  paiti  apa.^urvayat  yaha  azis'
biwivinka^''  "da  zog^  die  Hände  zurück, ,
weil  der  Drache  furchtbar  war"  Yt. /().  48.
ai.  bhyas-  V.  'sich  fürchlen'.  —  Vgl.  bay-.  —
>)  Stall  *bivyii}ha  (»=  biwy',  S  268.  37)  geschr.,
---
line 17452 nearby column numbers: ['971']
ai.  bhritiitili  'sie  versehren',  vgl.  np.  burrldait I  'schneiden'  (wozu  S  '33  aE.,  Hbm.  AGr.  /. I  427  mit  Litt,  das,,  Bthl.  IF.  9.  253),  ZDg. j  bride  'geschnitten'  (GIrPh.  /  b.  394).  —  VgL I  tiii.itira-S.  —  Pü.:  brilan.  —  i)  So  Mfl, j  Jp  1  u.  a.  Them.  —  ')  Man  erwartet  i,  3Sing, I  3.  Med.,  also  *brinleoAti('ÜiKm.)'brinailc. — i      ])  Man  halte  dazn  n.  gräbhä- ta.  onA  gf-bkäy-
I         j.  bräsal:  s.  bram-.
•  J,  bräz- V. 'strahlen'.   Praes.  2'>  ^äz«-. 'strahlen,     glänzen':     tanüm    ,  .  yeAkä
ainiks  brasaiti  ya'i^a  tistrydMärahe  YL  10. 143.  a)  mit  Akk,  des  Inhalts'^  und des  Ziels:  car?ma  (sd.)  vamanto  bräzmta frSiia  trizatam  saranim  Yt.  5.  129.
ai.  bhräjaU;  np.  baräzidan.  —  ')  S.  aberS /2J,
—  »  Vgl.  Dbk.  AiS.  169.
•  j.  btäza-  i)  Adj,  (fem.  -za-)  tlinkend, schimmernd':  ya'iia  sükayä  (sd.)  'sayh bräztm  Yt.  i4~  33-  *)  n.  'Schein,  Schim- mer': avavalai  ya^a  sükayh  (sd.)  bräzayä ',3m  Yt  14.  33.
Zum  V.  bräs-,  —  ai.  ihrajd-  Adj.;   np.  barät
dby  Google
■Schmuck'.  —  Npü.  (fiir  *r*  *r')j  toaify  ;»(.;,  j.   fyuäta-   m.   EN.   eines   Gläubigen: *"'^''  %riiö   atvSjar?lö  (s4)    'toAe    asaotiS    Yt
j,  brtnjayäiU  N.  g4:  lies  d>r>tay'.  j_  jj-
---
```


### [2026-09-05T13:53:59.118Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
10279:      reuer“ (vgl. denselben Bed.-Umfang bei der Erw. bhereu-). Der etwas
10557:bhreu-           bJireii-q-f   -t-,     bhreus    „zerbrecben“,    bherdh    ..scbneiden”',           bhe‘>^i{g-
10804:s. aucb u. bhereu „sich heftig be^vegen^).     Da6 die bait. Worte nach Traut-
10851:166                                       bhero-s, bheru-s
10888:bhiro-S, bheru-s „hell, braun“, vielfach von braunen Tieren; redupl. "^bhe-
10898:u wie das u von ai. bJiallSka'h aus dem St. ^bheru- stammen mag)                             = ags.
10916:                                             bhereu- bheru- bbreu- bbru-
10950:bhereu- : bheru- : bhreu- : bhru- Erw. von bher- .,sich heftig bewegen,
10952:   A. Ablautstufen '^bheru- "^(bh^m-), "^bhrtt:
10980:168                              bhereu- bberu-
```


## [2026-09-05T13:54:08.330Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10945,10985p' incoming/WLD/WLD_Bd2_pages.txt\necho \"=== bhereg ===\"; grep -n \"bhereg-\\|bhereĝ\\|bherag\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "WLD bhereu and bhereg"
}
```


### [2026-09-05T13:54:08.391Z] TOOL RESULT

```
blier     scheinen bhereg, bhcrek- „glanzen'*, Persson Beitr, 6S9a                              1.




bhereu- : bheru- : bhreu- : bhru- Erw. von bher- .,sich heftig bewegen,
    wallen, bes. vom Aufbrausen beim Gahren, Brauen, Kochen usw.‘'
   A. Ablautstufen '^bheru- "^(bh^m-), "^bhrtt:
   ai.                       ,,unruhig, wild'', blinridn- ..unruhige Bewegung des Wassers'*
(iiber blmryii-h            s.   u. bher-').
   Gr. (sehr fragwiirdig) (pagviuog' roAur]o6g,           Hes. (Persson Beitr.
179, 335, 785) und (pogviog „Gemisch von allerlei wertlosen Dingen, Ge-
mengsel, Kehricht, Auswurf, Spreu, Mist*', cpogvvco, (pogvoooj „knete durch-
einander, vermische, befiecke, besudle" (von Persson lleitr. 785 A 3 wohl
rich tig zunachst mit (pvgo)    s. u. biter    —
                                               verkniipft, letzteres daher aus
                       DaB dazu skr. brljati „verwiiTen, beschmutzen",
                                                                  r.-ksl. bhrJogz
„latibulum'\ russ. berloga „Barenhohle’' u. dgl. gehore, wie Berneker 120 zw.
als Alternative zur Verb, der slav.                         V
                                         orte mit lit. berti „streuen“ erwagt,
wurde dann auch formell weniger glaubhaft): etwas wahrscheinlicher gr.
(pgvdoooyai ..gebarde mich ungeduldig (bes. von feurigen Pferden); bin
ubermiitig" /;Persson Beitr. 179, 785, 964,                          s.   auch u. bhreiis- „brausen'‘).      —
Thrak. fgmog               (s. u.) :    alb.   brum m., brume f. ,.Sauerteig*' (G. Meyer Alb.
Wb. 49).
  Lat. ferreo, -ere, ..alt und dicht‘\ fervo, ere ..sieden, wallen" (uber fermeyi’-

Uim s. bher -) drfruhim „eingekoehter Most. Mostsaft" (: thrak. fgvrog, fgv-
                       ;


rov, fgovrog, .,eine Art Gerstenbier"; Curtius 531, Vf. LEWb.^ s. v. und u.
brisa; vgl. auch ahd. prod ,,Bruhe’*. air. bruth „Glut".         Kicht annehmbar
iiber fgvrog Schrader KZ. 30. 470 f.).
168                              bhereu- bberu-
                                           :           :   bhreu- ; bbru-


     Mir. berbaim ^^koche, siede. schmelze^, cymr. berwi^ bret. birvi (Ptc. bervet)
„sieden, wallen“          bero, berv „gekocht“          (z.      B. Pick II ^ 172,      Pedersen KG. I
=== bhereg ===
11055:bherek- „glanzen‘‘, gleichwertig mit bhereg- ds.                    (s. d.,   auch wegen doppel-
11057:   ai.   bhrdcafe „flammt, leuchtet^^ (unbelegt:            s.   u. bhereg-);    ob dazu bhr<^a-h
11114:bhereg- „glanzen,                         wozu auch der Birkenname.                      Gleichwertig           rait
11134:se.^'Basis %her9g- eben auf *bhereg- weist, sich als zshangend erweisen.
11187:  Forraen, die fur die Wz. *bhereg- eine leichte Nebenform bliertg- sichern
```


## [2026-09-05T13:54:11.625Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11114,11140p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD bhereg entry"
}
```


### [2026-09-05T13:54:11.669Z] TOOL RESULT

```
bhereg- „glanzen,                         wozu auch der Birkenname.                      Gleichwertig           rait

       hJierek-^ s.d.
  ai.    bhrdjate „glanzt, strahlt", bhrajd-h „glanzend, funkelnd“; ap. brasaiti
„strahlt,    glanzt^^, braza- „bliiikend. schimmernd^' n. „Schein, Schimmer'*,
up.    barcmdan „glanzeii“, baraz „Schmuck'^                           (die ar.   Worte      nicht    zu bhleg
„glanzen“,   s. Walde KZ, 34, 51 4 f.);

  lit.    brekszta^ breszfco^ brekszti „aiibrechen                    (vom Tage)“, apybreszkis „Zeit
um     Tagesanbruch“            ;
                                    slov. br'^sk^ cech. bfesk^         poln. brzask „Morgendainme-
rung“, poln. obrzasknqc „hell werden“, brzeszczy si^ „es grant der Tag“,
mit Ass. des Auslauts ^bk- an den tonenden Wortanlaut aksL pobrezgz
„Damniemng, Tagesanbruch“, rnss. brezg^ poln. brzazg ds. Ygl. Berneker
85 m.          Lit.   (gegen anl, *w r-    2     s.    auch      u.    7ner-   ^flimmem'^),       Trautmann
Bsl. Wb. 37 f.; es besteht kein AnlaS, wegen ai. bhrdcate „fiammt, leuchtet^
(Gr.     und Lexikogr.) die bsl. Gruppe auf                           "^bhrek-so zuruckzufiihren,              denn
das      ai.   Wort      gehort,       wenn    zuverlassig,       mit nach bhrdjate              eingefuhrter
Dehnstufe zur leichten Wzf. ^bherek-^ wahrend bsl. brtsk- und ar. "^bhrak-
durch ihre iibereinstimmende Lange, die mit den flgdn. Worten von der
se.^'Basis %her9g- eben auf *bhereg- weist, sich als zshangend erweisen.
   Mit Abtonung bh{e)rog- wahrscheinlich schwed. brokig „bunt'\ norw. mdartl.
brok „Salmling“, auch wie broka f. „grofigeflecktes Tier'‘ (s. u, mrr-, mer{p)q
„flimmern“ m. Lit.)
   Mit Hochstufe der 1. Silbe: got. bairhts „hell, glanzend, deutlich“, ahd.
beraht^        mhd. btrht „glanzend'' (auch                in    Namen ahd. Bert-^ -bert^ '-brecht)^
ags. beorht „glanzend,                 strahlend^*     (engl. bright)^         aisl.   biartr   ,,licht,   hell“;
```


## [2026-09-05T13:54:26.658Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\n# page markers like [pdf page N] ?\nfor i in range(11100,11135):\n    if re.search(r'\\[pdf page',lines[i]): print(i,lines[i])\n# find nearest page numbers printed\nfor i in range(11090,11150):\n    if re.fullmatch(r'\\s*1[6-8]\\d\\s*.{0,60}',lines[i]): print('PGMARK',i,lines[i][:80])\nEOF\necho \"=== ARY برازیدن ===\"; grep -n \"برازیدن\\|برازنده\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "WLD page marker and ARY grep"
}
```


### [2026-09-05T13:54:28.100Z] TOOL RESULT

```
PGMARK 11109 170                                                   bliereg-
=== ARY برازیدن ===
3394:۸ / برازیدن» برازء برازندگی
15167:چم این واژه در زبان‌های لاتین: چشمگیر؛ درخشان» برازنده.
15605:چم این واژه در زبان‌های انگلیسی نرین: برازیدن» نمودن.
```


## [2026-09-05T13:54:31.859Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('\\n'.join(lines[3370:3420]))\nEOF",
 "description": "Aryanpur barazidan entry"
}
```


### [2026-09-05T13:54:33.500Z] TOOL RESULT

```
پهلوی (1هالله۳۸): با8۸ انگلیسی کهن (0ا5لا5۸0 2: ,8187135
کردی (80/5[7با): اد[ 3
تخاری 4 (۸ 7( ۸ل70): 2۸ انگلیسی (]5لا60): 7
تخاری 8 (8 4۸ل1۸2ل70): ۳7 اسلاری کهن (12اما5 7لع#ناتت) صا0):
سانسکریت (84(/57/7): با 1 آن اند زا
0 ۸ ,21387
برنانی (02): ۰ ۳130108 ,۳1188۸۵ پسگشت‌ها اند نم رای اد دی
لاتین (710ل): 3 2000
گوتیک (0077716): بای ۱10 5 (۲8۷11 ,17 دراد ها
ایسلند یکهن (/010504(/0/0740): 8۸3 نات ۱۱:۱ بکلطمصم غ نم نتهلد
نررس کهن (۸0882 0ل0): قا نی زان برهان قاطع + ۳۵
فریزی کهن (/(۲۴/۹4 2ا0): ۰ 658820 فرهنگ معین : ۴۸۹
یادداشت: .
۱ این واژه با واژه‌ی "پار"(به چم "وزن سنگین" همریشه است.
معنی این واژه در زبان‌های ژرمنی: زایش» زادآوری (البته در فارسی نیز این معنی وجود دارد» مثلاً ّزن پاردار")
۳ ریشه‌ی واژه‌ی انگلیسی 38۸3017 نیز از همین واجریشه است.
اوستایی (4۲587۸4): 3۵۸ افغانی (پشتو) (/۸701۸۷): ۷0
پارسی باستان (//8۵ق8 0ا0). ۰ 8821۸ تخاری ۸ (۸ 4۷ل70577۸): 3
پپلری (4۲7ات۳۸): ,8820۸ ,8820 تخاری 8 (8 40لا 7۸ل705): 3 اد هه ۱
1 ۱ سانسکریت (54(/8877): ب۸ 2
کردی (6(80/5[7): 3117۸ 323
1
[pdf page 117]
۸ / برازیدن» برازء برازندگی

یونانی 025680): یلا۷ درا لهستانی (81ا.۳0): 2۸7
لاتین (110ها): 3 لد اش | روسی (75514(۷)): 3۸7
فرانسه (۳7(/0): ادن دا صربی (/81۸ظ5:) لا

ایتالیایی (۸(۷لله5): ۲۸۸۲2۵ برهمی (000هر0 ۵" و

رومانی (/(۸۱۸/۸/۸): ۳/۸ لیتوانی (7(فااههنتم: ,۰۵07۳85۲8 +

گرتبکد (007710): 3 را ۱۱ 1 8085
ایسلند ی‌کهن (4(/070/۸71۸(۷ی)5 )+ لنونی (لتی) (/۸47۳1۸ا): 8828
3( ۵ پروسی کهن (۲۸۷۹۹۸/۷ 2ا0): 88۸۲1
نورس کهن (۸0738 ۰:01 88077118 ایرلندی کهن (تلخنق! 012): 8727۸3
ساکسونی کهن (54200۸۷ 0ا0): 130773۸4 ولزی (7ک )+ راید ۱۱
فریزی کهن (//۲۶/54 ۰:02 80717868 برتونی (876702): 3 راد 3 زا
آلمانی کهن (62704۸/0 بلاط صا): گالبکه (70اق۸ه): 8۸71
3
آلمانی (/0270/۸2): راز نا پسگشت‌ها ات دا
انگلیسی کهن (/8۸/05 88711078,:)00 8 ونم
انگلیسی (6۸/01/5[7): 3 دا ری ۱۱ 0 (8۸0777833) زره
دانمارکی (0۸(7137): 3 لن ۱[ ۱۵ 8 (85) م02
سوئدی (8(۳8015): ند راز ۱ 5 (807883) درد سا
نروژی (/۷0501۸2: 3 10108 اه
هلندی (0076/7): 810130 ,131201057 1 (8077183) :0/1015
اسلاوی کهن (۷16امآ5 بط تال صان): 4 (8807753) ۸0
1 ,3۸78 برهان قاطع ‏ ۳۶
```


## [2026-09-05T13:54:46.963Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A8%D8%B1%D8%A7%D8%B2%DB%8C%D8%AF%D9%86/\" --note \"page 91, Persian barâzîdan: Dehkhoda/Mo'in\" 2>&1|tail -1\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A8%D8%B1%D8%A7%D8%B2%D9%86%D8%AF%D9%87/\" --note \"page 91, Persian barâzandeh: Dehkhoda/Mo'in\" 2>&1|tail -1",
 "description": "Fetch abadis barazidan/barazandeh"
}
```


### [2026-09-05T13:54:50.605Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/753cc90f1d74d699.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f636178791d9f4fe.txt
```


## [2026-09-05T13:54:53.754Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 753cc90f1d74d699 f636178791d9f4fe; do echo \"##### $f\"; grep -n -A4 \"فرهنگ معین\" $f.txt | head -12; grep -n \"لغت نامه دهخدا\" -A6 $f.txt | head -10; done",
 "description": "Read Mo'in entries"
}
```


### [2026-09-05T13:54:57.039Z] TOOL RESULT

```
##### 753cc90f1d74d699
38: فرهنگ معین
39-
40- (بَ دَ ) (مص ل . ) سزاوار بودن ، شایسته بودن . 
41-
42- فرهنگ عمید
--
124: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
125-
126- لینک ها 
127-
128- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
17: لغت نامه دهخدا
18-
19- برازیدن. [ ب َ دَ ] ( مص ) زیبا نمودن.( شرفنامه منیری ). خوب و زیبا نمودن. ( برهان ) ( آنندراج ). زیبیدن. ( صحاح الفرس ). نیکو کردن. ( فرهنگ اسدی ). طرازیدن. ( فرهنگ اسدی ). ( برازیدن یک مصدر بیش ندارد ). ( یادداشت مؤلف ). || سزیدن. شایسته بودن. سزاوار بودن. لایق بودن. در خور بودن. لیاقت داشتن. ( یادداشت مؤلف ) : و پس ترا از من می آید آنکه از من قدیم تر است و زورمندتر است. آنکه نمی برازم که بند کفش او از پای او بگشایم. ( دیاتسارون ).
20-گر سیستان بنازد بر شهرها برازد
21-زیرا که سیستان را زیبد بخواجه مفخر. فرخی.
22-مرا هم گوشه بی توشه سازد
23-خراش چنگ ناخن را برازد. نظامی.
##### f636178791d9f4fe
39: فرهنگ معین
40-
41- (بَ زَ دَ ) (ص فا. ) شایسته ، زیبنده . 
42-
43- فرهنگ عمید
--
128: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
129-
130- لینک ها 
131-
132- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
26: لغت نامه دهخدا
27-
28- برازنده. [ ب َ زَ دَ / دِ ] ( نف ) زیبنده : 
29-خالق خلق و نگارنده ایوان رفیعی 
30-فالق صبح و برازنده خورشید منیری. سعدی.
31- || سزاوار. درخور. برازا. لایق : 
32-پیش بالای تو میرم چه بصلح و چه بجنگ
```


## [2026-09-05T13:55:13.329Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nls site/pages/91.jpg 2>/dev/null; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 91 -l 91 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg91 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 91"
}
```


### [2026-09-05T13:55:16.419Z] TOOL RESULT

```
site/pages/91.jpg
total 30156
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 09:55 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
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
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
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
```


## [2026-09-05T13:55:19.425Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg91.png"
}
```


### [2026-09-05T13:55:19.771Z] TOOL RESULT

```

```


## [2026-09-05T13:55:19.770Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T13:55:57.845Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T13:55:57.884Z] TOOL RESULT

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


## [2026-09-05T13:56:16.200Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg91.png data/verification/sources/refs/ocr/BOOK/91.png\nls -la data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Archive page image"
}
```


### [2026-09-05T13:56:17.542Z] TOOL RESULT

```
total 2136
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 09:56 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
```


## [2026-09-05T13:58:11.606Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ('LEW_1910.txt','LAT.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for w in ['fermentum','ferveo','fervere']:\n        m=re.search(w,t)\n        print('###',f,w, (t[max(0,m.start()-80):m.start()+400].replace('\\n',' ') if m else 'NOT FOUND'))\n        print()\nEOF",
 "description": "Latin etymological dicts on fermentum"
}
```


### [2026-09-05T13:58:13.325Z] TOOL RESULT

```
### LEW_1910.txt fermentum NOT FOUND

### LEW_1910.txt ferveo NOT FOUND

### LEW_1910.txt fervere NOT FOUND

### LAT.txt fermentum npe dn perfectnm; cf. le cas de fer 5 , Idtus. Cf.forO, ferula ? ferae: v.fere. fermentum, -I n.: ferment, levain = Ancien (Pl. ), classi¬ que. M.L.3354. De IA: fermento,-as et aes d 4 riv 4 s, fermentSscS,-is (Plin.); fermentacius. Lea correspondants lea pina proches sont v.angl. beorma "levain" et ganl. Bormo qni ddaigne nne sonrce bonillonnante. Fermentum doit a' analyser *bher-nentom, le thbme 4 tant fourni par nne forme non dlargie de la racine de ferueo (v. ce mot). fer

### LAT.txt ferveo NOT FOUND

### LAT.txt fervere NOT FOUND
```


## [2026-09-05T13:58:18.128Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('LAT.txt',encoding='utf-8',errors='replace').read()\nm=re.search(r'ferueo',t)\nprint(t[max(0,m.start()-60):m.start()+700].replace('\\n',' ') if m else 'NOT FOUND')\nEOF",
 "description": "Ernout-Meillet ferueo"
}
```


### [2026-09-05T13:58:19.937Z] TOOL RESULT

```
nne boisson feraentee, gr. owiecppucrev • ane^eaev, Hes. V .ferueo. degener: v. genus. deguno: v. gustus. delero: y. iuro s .ius. deinceps: v.le salvant. deinde, deln adv.: k la suite, ensnite. - Usiti de toat teaps. Conserve dans quelques 1 . roaanes, M.L.afiaS. Deinde est la forae la plus ancienne; dein en est nne forae abrigie: Cic., Or.154, ain pro aine... dein etiam saepe et exin pro deinde et pro exinde dicimus. - Deinde seal est attesti epigraphiqueaent; dein (comae proin, etc.) se rencontre seolement devant consonne. La coaparaison de dehinc snffit k pronver que deinde est antirieur a dein. De ce dernier a eti tiri: deinceps : successiveaent, a la suite. Correspond a gr. e^r[c ecpe^T)S: souvent joint k inde, postea, deinde, cf. gr. erotTU. et
```


## [2026-09-05T14:03:49.562Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk91.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PIE_BREW = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0rewh%E2%82%81-\"\nW_BRINNAN  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/brinnan%C4%85\"\nW_BRANDAZ  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/brandaz\"\nW_BRETHAZ  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/br%C4%93%C3%BEaz\"\nW_BREATH   = \"https://en.wiktionary.org/wiki/breath\"\nW_BERHTAZ  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/berhtaz\"\nW_BERKO    = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/berk%C5%8D\"\nW_BARAZ    = \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%A7%D8%B2%DB%8C%D8%AF%D9%86\"\nW_BALWA    = \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D8%A7\"\nW_BALA     = \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D8%A7%D8%A1\"\nA_BALVA    = \"https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%A7/\"\nA_BARAZIDAN= \"https://abadis.ir/fatofa/%D8%A8%D8%B1%D8%A7%D8%B2%DB%8C%D8%AF%D9%86/\"\nA_BARAZANDE= \"https://abadis.ir/fatofa/%D8%A8%D8%B1%D8%A7%D8%B2%D9%86%D8%AF%D9%87/\"\nE_BRAISE   = \"https://www.etymonline.com/word/braise\"\n\ndoc = {\n \"pdf_page\": 91,\n \"book_page\": 61,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Bher 5, Bheru, Bhereu, Bhreu, Bhru 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *bʰer- 'to boil, seethe, well up' with its u-extension *bʰrewh₁- / *bʰer(e)u- 'to boil, brew'\",\n   \"note\": \"Nourai's five variant names correspond exactly to the two Pokorny lemmata he cites: IEW 132-133 '2. bher- etwa \\\"aufwallen\\\", von quellendem oder siedendem Wasser (auch vom Aufbrausen beim Gähren, Kochen, sowie vom Feuer) \\\"sich heftig bewegen\\\"; oft mit u-Formans', and IEW 143-145 'bh(e)reu- : bh(e)rū-, Erw. von 2. bher-, \\\"sich heftig bewegen, wallen, bes. vom Aufbrausen beim Gären, Brauen, Kochen usw.\\\"' — so 'Bher 5' = Pokorny's bher-2, 'Bheru/Bhereu/Bhreu/Bhru 2' = his bh(e)reu- : bh(e)rū-. Watkins (AHD) fuses them into one entry, bhreu-2 'To boil, bubble, effervesce, burn; with derivatives referring to cooking and brewing. [Pok. bh(e)reu- 143, 2. bher- 132]'. Wiktionary reconstructs *bʰrewh₁- 'to boil, to brew', explicitly 'Extension of *bʰer- (to boil)'. Language label (Indo-European) and gloss ('to boil, bubble') are both right; only the numbering is Nourai's own.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰer- «جوشیدن، فوران کردن» و گسترش «واوی» آن *bʰrewh₁- (نوشتار کهن‌تر: bh(e)reu-) «جوشیدن، آبجو پختن». آنچه نورایی زیر پنج نامِ Bher 5، Bheru، Bhereu، Bhreu و Bhru 2 آورده، همان دو مدخل پوکورنی است: bher-2 در صفحهٔ ۱۳۲–۱۳۳ و bh(e)reu- : bh(e)rū- در صفحهٔ ۱۴۳–۱۴۵؛ واتکینز در پیوست فرهنگ American Heritage این دو را در یک مدخل bhreu-2 «جوشیدن، حباب زدن، سوختن» یکی کرده است. برچسب زبانی و معنای ریشه هر دو درست است و ادعای نورایی در این حد پذیرفتنی است.\",\n   \"sources\": [W_PIE_BREW],\n   \"ref_check\": [\n    {\"ref\": \"AHD:1510\", \"status\": \"supports\", \"note\": \"Content verified in the local Watkins text (AHD_watkins1985.txt) s.v. bhreu-2: 'To boil, bubble, effervesce, burn; with derivatives referring to cooking and brewing … [Pok. bh(e)reu- 143, 2. bher- 132.]' — the same appendix Nourai cites. p.1510 falls inside the 1975 New College appendix range (pp.1505-1550, bh- section); the local copy is the 1985 standalone reprint, so the exact page number itself could not be re-checked.\"},\n    {\"ref\": \"POK:132\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 140 (= printed p.132-133): '2. bher- etwa \\\"auf wallen\\\", von quellendem oder siedendem Wasser … oft mit u-Formans; auch als schwere Basis bhers-'. Exactly Nourai's gloss.\"},\n    {\"ref\": \"POK:143\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 151-152 (= printed p.143-145): 'bh(e)reu- : bh(e)rū-, Erw. von 2. bher- \\\"sich heftig bewegen, wallen, bes. vom Aufbrausen beim Gären, Brauen, Kochen usw.\\\"'\"},\n    {\"ref\": \"IEC:116\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 78 (= printed p.116) carries the cross-reference lemma '(bhru-, see bheru-. Z-gde radical in Per. balwà \\\"tumult\\\"; OE brymm, m. \\\"surf, sea\\\", prob. also in MHG brunne \\\"spring\\\"; ON brunnr, id.)'. Mann's bheru- is Nourai's 'Bheru'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 132-133 and 143-145\", \"stance\": \"supports\", \"note\": \"Both lemmata present, with fermentum, ferveo, brinnan, brauen, Brot, defrutum all gathered under them.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.167-168\", \"stance\": \"supports\", \"note\": \"'bhereu- : bheru- : bhreu- : bhru- Erw. von bher- \\\"sich heftig bewegen, wallen, bes. vom Aufbrausen beim Gahren, Brauen, Kochen usw.\\\"' — the direct forerunner of Pokorny's article.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins, s.v. bhreu-2\", \"stance\": \"supports\", \"note\": \"'bhreu-2. To boil, bubble, effervesce, burn' with sections I (brew/bread/broth), II (*bhrē- brood/breed), III (fermentum/fervēre), IV (spring words).\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. brew, barm\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *bheru-, *bhreu-, *bhrū-, \\\"to boil, ferment\\\"' (brew); 'fr. I.-E. base *bher-, \\\"to boil, seethe\\\" … Cp. brand, bread, brew, broil, broth. Cp. also ferment' (barm).\"},\n    {\"src\": \"IEC\", \"where\": \"p.116, lemma bhru-/bheru-\", \"stance\": \"supports\", \"note\": \"Mann keeps the same root but attaches Persian balwā to it (see node #1).\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"balvâ\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Persian بلوا balvā 'riot, tumult, uproar' is treated by every Persian lexicon as an Arabic loan. Dehkhoda: 'بلوا. [بَلْ] (از ع، اِ) بلوی. زحمت (غیاث اللغات). مشقت' ('from Arabic; = balwā; trouble, hardship'); Mo'in — the very reference Nourai cites — 'بلوا (بَ) [ع. بلوی] (اِ.) ۱- شورش، آشوب. ۲- سرکشی'. The Arabic source is بَلْوَى balwā, a maṣdar of the root ب ل و b-l-w 'to test, try, afflict' (same root as بلاء balāʾ 'trial, affliction'), the sense shifting in Persian from 'ordeal, calamity' to 'disturbance, riot'. Nourai's Indo-European derivation rests solely on Mann, IEC 116, whose parenthetical lemma reads '(bhru-, see bheru-. Z-gde radical in Per. balwà \\\"tumult\\\" …)'; Mann is alone in this, and no Iranian etymological dictionary (Horn, Hübschmann, Cheung, Hasandust) knows a Persian verb *balv-/*burv- 'to boil'. Phonetically an inherited zero-grade *bʰru- would not yield NP balv- (cf. the genuine reflexes MP/NP burr-, borr- of *bru-). The chart's own NOTE records the conflict; modern scholarship sides with Mo'in.\",\n     \"derivation_fa\": \"«بلوا» در فارسی وام‌واژه‌ای عربی است، نه واژه‌ای ایرانی. دهخدا آن را «(از ع، اِ) بلوی. زحمت. مشقت» می‌داند و معین — همان مأخذی که نورایی به آن ارجاع می‌دهد — می‌نویسد: «(بَ) [ع. بلوی] (اِ.) ۱- شورش، آشوب. ۲- سرکشی». اصل آن بَلْوَی عربی از ریشهٔ «ب ل و» به معنی «آزمودن، گرفتار کردن» است (هم‌ریشه با «بلاء»)، و تحول معنایی «گرفتاری، آزمون» ← «آشوب» در فارسی رخ داده است. تنها پشتوانهٔ نورایی مدخل مان (IEC ۱۱۶) است که این واژه را درجهٔ صفر ریشهٔ *bʰreu- «جوشیدن» گرفته؛ این رأی در ریشه‌شناسی ایرانی هواداری ندارد و از نظر آوایی نیز *bʰru- در فارسی «بلو-» نمی‌دهد. پس پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n     \"sources\": [A_BALVA, W_BALA, W_BALWA],\n     \"ref_check\": [\n      {\"ref\": \"IEC:116\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 78 (printed p.116): '(bhru-, see bheru-. Z-gde radical in Per. balwà \\\"tumult\\\"; OE brymm, m. \\\"surf, sea\\\" …)' — Mann does say precisely what the arrow says; the reference is accurate, the claim is what is doubtful.\"},\n      {\"ref\": \"MON:575\", \"status\": \"contradicts\", \"note\": \"Mo'in's entry (read at abadis.ir, section فرهنگ معین): '(بَ) [ع. بلوی] (اِ.) ۱- شورش، آشوب. ۲- سرکشی' — the tag [ع.] marks it Arabic. The 6-volume pagination is not available online, so p.575 itself could not be checked, but the entry text is unambiguous, and Nourai's own NOTE reports the same.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. بلوا (via abadis.ir)\", \"stance\": \"contradicts\", \"note\": \"'[ع. بلوی]' — Arabic.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 1 (آ–ت), searched BQT_v1_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'بلوا' returns only بلواله (a bird name) at leaf 466 and بلواس at leaf 26280; Borhān has no headword بلوا, as expected for an Arabic word.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss, searched HRN.txt for balwa/belva\", \"stance\": \"silent\", \"note\": \"Horn has no entry for balvā; his b-section (nos. 190-200) covers berāz, berāi, berd, burden — nothing of the shape balv-.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"No headword بلوا in Aryanpur's Indo-European roots dictionary (grep hits are only Latin-script transliteration noise).\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Germanic\",\n     \"words\": \"breuwan; braudam; brudam; brôd\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four are Watkins' Germanic citation forms under bhreu-2: 'Germanic *breuwan, to brew, in Old English brēowan: BREW. 2. Germanic *braudam, (cooked) food, (leavened) bread, in Old English brēad: BREAD. 3. Germanic *brudam, broth, in a. Old English broth: BROTH … II. Variant form *bhrē- in Germanic *brēdan, to warm … 1. *brēd-ō, \\\"a warming\\\", hatching, rearing of young, in Old English brōd, offspring, brood.' Nourai's 'brôd : hatching' is that last item (PGmc *brōdō 'brood'), so the node mixes the *bhreu- and the *bhrē- ablaut variants, exactly as AHD does. Klein agrees: brew 'fr. I.-E. base *bheru-, *bhreu-, *bhrū-, to boil, ferment'; bread 'fr. Teut. *brauda, lit. bread leavened with barm … formed with the I.-E. pp. suff. -to fr. base *bhreu-, *bhru-'; broth 'fr. Teut. base *brauda- [read *bruþa-] … cogn. with Thracian βρῦτος, L. dēfrutum'. Wiktionary reconstructs *brewwaną, *braudą, *bruþą, all under *bʰrewh₁-. The -am of braudam/brudam is simply the neuter nom.-acc. ending of Watkins' notation, not a misprint.\",\n     \"derivation_fa\": \"این چهار صورت، همان صورت‌های ژرمنی آغازین‌اند که واتکینز زیر ریشهٔ bhreu-2 آورده است: *breuwan «آبجو پختن» (انگلیسی کهن brēowan)، *braudam «خوراک پخته، نان» (انگلیسی کهن brēad)، *brudam «آبگوشت» (انگلیسی کهن brōþ) و *brōd- «جوجه‌آوری» (از گونهٔ *bhrē- «گرم کردن»). کلاین نیز همین را می‌گوید و «نان» را در اصل «خمیرمایه‌زده» می‌داند. پایانهٔ ‑am در braudam و brudam تنها نشانهٔ خنثای صرفی در شیوهٔ نگارش واتکینز است و خطای چاپی نیست. ادعای نورایی در این گره درست است.\",\n     \"sources\": [W_PIE_BREW],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. bhreu-2, sections I.1-3 and II.1: '*breuwan … BREW', '*braudam … BREAD', '*brudam, broth … BROTH', '*brēd-ō, \\\"a warming,\\\" hatching, rearing of young … BROOD'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins s.v. bhreu-2 I-II\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. brew, bread, broth, brood\", \"stance\": \"supports\", \"note\": \"'brew … fr. I.-E. base *bheru-, *bhreu-, *bhrū-, to boil, ferment'; 'brood … lit. that which is hatched out by warmth … See brew'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 145-146\", \"stance\": \"supports\", \"note\": \"'bhreu- : bhrū̆u- in: ahd. briuwan, ags. breowan \\\"brauen\\\" … germ. *bruda- in aisl. ags. brod, ahd. prod \\\"Brühe\\\" (: defrutum, air. bruth, thrak. βρῦτος) … germ. *brauda- in aisl. braud, ags. bread, ahd. brōt \\\"Brot\\\" (von dem Gärstoff)'.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"English\",\n     \"words\": \"brew; bread; broth; breed\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The regular English continuations of node #2: OE brēowan > ME brewen > brew; OE brēad 'morsel, bread' > ME breed/brede > bread; OE broþ > ME broth; OE brēdan 'to cherish, keep warm, hatch' > ME breden > breed (Klein s.v. breed: 'fr. OE. brēdan, to cherish, keep warm, nourish … fr. I.-E. base *bher-, to boil. See brew'). Semantically: 'to boil/ferment' → 'brew'; 'the leavened (barm-raised) loaf' → 'bread', which displaced OE hlāf in the sense 'loaf' only in late Old English; 'the boiled liquid' → 'broth'; and through the *bhrē- 'to warm' variant, 'to keep warm, hatch' → 'to breed'. Only the last one reaches 'boil' by way of 'heat' rather than 'bubble'.\",\n     \"derivation_fa\": \"این چهار واژهٔ انگلیسی دنبالهٔ منظم صورت‌های ژرمنی گرهٔ پیشین‌اند: انگلیسی کهن brēowan ← brew؛ brēad ← bread؛ brōþ ← broth؛ brēdan «گرم نگاه داشتن، پروردن» ← breed. تحول معنایی روشن است: «جوشاندن/تخمیر» ← «آبجوسازی»؛ «نانِ ورآمده با خمیرمایه» ← «نان»؛ «مایع جوشیده» ← «آبگوشت»؛ و در مورد breed پیوند با «جوش» از راه معنای «گرما» است نه «حباب». کلاین و واتکینز هر دو همین زنجیره را می‌دهند؛ ادعای نورایی درست است.\",\n     \"sources\": [W_PIE_BREW],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins bhreu-2 names BREW, BREAD, BROTH, BROOD/BREED as the English outcomes; the reverse index confirms 'BREAD bhreu-2', 'BREW bhreu-2', 'BROTH bhreu-2', 'BREED bhreu-2'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. brew, bread, broth, breed\", \"stance\": \"supports\", \"note\": \"'breed … fr. OE. brēdan, \\\"to cherish, keep warm, nourish\\\" … fr. I.-E. base *bher-, \\\"to boil\\\". See brew'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins index\", \"stance\": \"supports\", \"note\": \"'BREAD bhreu-2 … BREED bhreu-2 … BREW bhreu-2 … BROTH bhreu-2'.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Germanic\",\n     \"words\": \"brěthaz; bres; brenw; brandaz\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Three of the four are contested, and Nourai's own authority (AHD) is on the other side. (a) *brēþaz: Klein s.v. breath derives OE brǣþ 'odor, scent, breath' (rel. OHG brādam, G Brodem 'breath, steam') 'fr. I.-E. base bher-, to boil. See brew'; Wiktionary takes OE brǣþ < PWGmc *brāþi, a derivative of the *brē-/*brēdaną 'to warm, roast' group, ultimately *bʰer- 'to boil, seethe' (with Skt. bhurati). Watkins instead files BREATH under gʷhrē- 'To smell, breathe. Contracted from *gʷhreə-. Germanic suffixed form *brē-thaz in Old English brēth'. (b) 'bres : burning' is the book's own abbreviated citation of the Germanic word behind Old French brese 'live coals'; the reconstructed form is *brasa- (Etymonline: braise 'from Old French brese \\\"embers\\\", ultimately … from Proto-Germanic *brasa, from PIE root *bhreu-'), and AHD bhreu-2 III.3 has 'Perhaps distantly related is the Germanic source of Old French brese, burning coal, ember (> French braise)'. The printed page really reads 'bres', so this is Nourai's loose citation form, not a scanning error. (c) *brenw- 'to burn': Pokorny IEW 145-146 puts the nasal-infix present here — 'bhre-n-u- (Präsens mit Nasalinfix, vgl. nhd. brennen) … got. ahd. as. brinnan, aisl. brinna, ags. beornan, birnan \\\"brennen\\\", Kaus. got. brannjan … ahd. brant \\\"Brand\\\"' — and Kroonen reconstructs Pre-Germanic *bʰrénuh₁e- from *bʰrewh₁-; Klein s.v. burn: 'fr. I.-E. base *bhreu-, to boil. See brew'. Watkins alone derives *brenw-/*brennan from gʷher- 'to heat, warm' with 'analogical vocalism'. (d) *brandaz is derived from *brinnaną + *-az (Wiktionary), so it stands or falls with (c); Watkins puts it under gʷher- as well. Verdict: the arrows are supported by Pokorny, Klein and Kroonen — the majority view — but not by the AHD that Nourai cites for them.\",\n     \"derivation_fa\": \"این گره از دو سو محل اختلاف است. پوکورنی (صفحهٔ ۱۴۵–۱۴۶) ستاک با میان‌وند نونی bhre-n-u- را — که گوتی brinnan، آلمانی brennen و انگلیسی کهن beornan/birnan «سوختن» و نیز ahd. brant «آتش‌پاره» از آن است — زیر همین ریشهٔ bh(e)reu- می‌آورد؛ کلاین هم burn را «از ریشهٔ هندواروپایی *bhreu- «جوشیدن»» می‌داند و کرونن صورت پیش‌ژرمنی *bʰrénuh₁e- را از *bʰrewh₁- بازسازی می‌کند. برعکس، واتکینز در پیوست AHD — یعنی همان مأخذی که نورایی برای این گره آورده — واژه‌های burn، brand و breath را زیر ریشه‌های دیگر (*gʷher- «گرم کردن» و *gʷhreh₁- «بوییدن، دمیدن») می‌گذارد. صورت «bres» نیز در خودِ کتاب چاپ شده (خطای خوانش اسکن نیست) و صورت کوتاه‌شدهٔ ژرمنی *brasa- است که فرانسوی کهن brese «اخگر» از آن آمده. بنابراین ادعای نورایی «با احتیاط پذیرفتنی است»: رأی اکثریت با اوست، اما مأخذ خودش با او همداستان نیست.\",\n     \"sources\": [W_PIE_BREW, W_BRINNAN, W_BRANDAZ, W_BRETHAZ, E_BRAISE],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Only 'bres' belongs to bhreu-2 in Watkins ('the Germanic source of Old French brese … BRAISE, BRAZE, BRAZIER, BREEZE2'). For the other three Watkins says the opposite: 'gʷher-. To heat, warm. 1. Zero-grade *gʷhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan … BURN; … 2. Germanic *brandaz, a burning …' and 'gʷhrē-. To smell, breathe … Germanic suffixed form *brē-thaz in Old English brēth: BREATH'. The reverse index likewise reads 'BRAND gʷher- … BREATH gʷhré-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 145-146\", \"stance\": \"supports\", \"note\": \"'bhre-n-u- (Präsens mit Nasalinfix, vgl. nhd. brennen) mit Beziehung auf züngelnde Flammen liegt vor in got. ahd. as. brinnan … wozu u. a. ahd. brant \\\"Brand\\\", brunst'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. burn (v.), brand, breath, brandy\", \"stance\": \"supports\", \"note\": \"'burn … fr. I.-E. base *bhreu-, \\\"to boil\\\". See brew'; 'brand … formed from the base of OE. beornan'; 'breath … fr. I.-E. base bher-, \\\"to boil\\\". See brew'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷher-, gʷhrē-\", \"stance\": \"contradicts\", \"note\": \"assigns *brenw-, *brandaz and *brē-thaz to other roots (quoted in ref_check).\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. BURN\", \"stance\": \"partial\", \"note\": \"Skeat's OCR is poor but legibly reads '… Goth. brinnan … Perhaps allied to Lat. feruēre, to boil' — i.e. the same connection Pokorny and Klein draw.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"breath; braise, breeze; burn; brand, Brandy\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The English chains themselves are secure; what they inherit from node #4 is the disputed PIE attachment. breath: OE brǣþ 'odour, exhalation' > ME breeth > breath (the sense 'air drawn into the lungs' is Middle English). braise: French braiser (17th c.) from braise 'live coals' < Old French brese (12th c.), a Germanic loan into Gallo-Romance, the same word as Italian bragia, Spanish brasa; English braise is 1797. breeze here must be breeze² — Klein: 'breeze, n., refuse from charcoal or coke. — F. braise. See braise' — and NOT breeze 'light wind', which Klein derives from French brise, probably Spanish brisa 'north-east wind', and which is unrelated; the chart's undifferentiated 'breeze' is therefore only half right. burn: OE beornan/biernan (intr.), bærnan (tr.), ON brenna. brand: OE brand, brond 'firebrand, fire, torch, sword' (the 'sword' sense from the flashing of the blade), formed from the base of beornan with suffix -þa-. Brandy: shortened from 17th-c. brandwine, brandewine < Dutch brandewijn 'burnt (i.e. distilled) wine', from branden 'to burn' + wijn.\",\n     \"derivation_fa\": \"زنجیره‌های انگلیسی این گره درست‌اند و تنها ریشهٔ نهایی‌شان (گرهٔ پیشین) محل بحث است. breath از انگلیسی کهن brǣþ «بو، دمِ برآمده»؛ burn از beornan/biernan؛ brand از brand «مشعل، آتش‌پاره» (و از درخشش تیغه، «شمشیر»)؛ Brandy کوتاه‌شدهٔ brandwine از هلندی brandewijn «شرابِ سوخته/تقطیرشده». braise از فرانسوی braise «اخگر» (فرانسوی کهن brese) که خود وام‌واژه‌ای ژرمنی در گالو-رومی است. اما باید توجه داشت که breeze در این جا breeze² یعنی «تفالهٔ زغال» است (کلاین: از فرانسوی braise) و نه breeze «نسیم» که از brise فرانسوی/brisa اسپانیایی آمده و بی‌ارتباط است؛ نمودار کتاب این دو را از هم جدا نکرده است.\",\n     \"sources\": [W_BREATH, E_BRAISE],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins lists BRAISE and BREEZE2 under bhreu-2, but BREATH under gʷhré- and BURN1/BRAND/BRANDY under gʷher- (reverse index: 'BRAND gʷher- BRANDISH gʷher- BRANDY gʷher- … BREATH gʷhré- … BURN? bhreu-2' — where BURN2 is the noun 'brook').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. breath, breeze (both), brandy, brand\", \"stance\": \"partial\", \"note\": \"supports the derivations but separates 'breeze, n., a light wind. — F. brise, prob. fr. Sp. brisa' from 'breeze, n., refuse from charcoal or coke. — F. braise'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins bhreu-2 III.3 and index\", \"stance\": \"partial\", \"note\": \"BRAISE/BREEZE2 yes, BREATH/BURN/BRAND no.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Latin\",\n     \"words\": \"fer-mentum; fervere\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin fermentum 'leaven, yeast' continues *bʰer-men-to- (AHD bhreu-2 III.1: 'Suffixed form *bher-men-, yeast, in a. Germanic *bermōn- in Old English beorma, yeast: BARM; b. further suffixed form *bhermen-to- in Latin fermentum'); PIE initial *bʰ- gives Latin f-, so *bʰer- > fer-. Its closest cognate is precisely OE beorma 'barm', as Ernout-Meillet note: 'Les correspondants les plus proches sont v.angl. beorma \\\"levain\\\" et gaul. Bormo qui désigne une source bouillonnante. Fermentum doit s'analyser *bher-mentom, le thème étant fourni par une forme non élargie de la racine de ferueo.' fervēre (also 3rd-conj. fervere) 'to boil, seethe, glow' is the w-extension *bʰer-w-, Pokorny's bh(e)reu- (IEW 144: 'Lat. ferveō, -ēre, fervō, -ere \\\"sieden, wallen\\\" (über fermentum s. 2. bher-)'), with Celtic mir. berbaim 'I boil' and Thracian βρῦτος beside it. Nourai's hyphen in 'fer-mentum' just marks the suffix boundary; it is not a variant form.\",\n     \"derivation_fa\": \"لاتینی fermentum «مایهٔ خمیر، خمیرمایه» بازماندهٔ *bʰer-men-to- است؛ *bʰ آغازی هندواروپایی در لاتینی به f بدل می‌شود، پس *bʰer- ← fer-. نزدیک‌ترین هم‌ریشهٔ آن انگلیسی کهن beorma «خمیرمایه» است، چنان‌که ارنو–می‌یه می‌نویسند fermentum را باید *bher-mentom تحلیل کرد. فعل fervēre «جوشیدن، تفتیدن» گسترش «واوی» همان ریشه (*bʰer-w-) است و پوکورنی در صفحهٔ ۱۴۴ آن را زیر bh(e)reu- آورده. خط تیرهٔ «fer-mentum» در نمودار تنها مرز پسوند را نشان می‌دهد. ادعای نورایی درست است.\",\n     \"sources\": [W_PIE_BREW],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins bhreu-2 III: '1. Suffixed form *bher-men-, yeast … b. further suffixed form *bhermen-to- in Latin fermentum, yeast: FERMENT. 2. Extended form *bherw- in Latin fervēre, to be boiling or fermenting: FERVENT, FERVID, (FERVOR)'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 133 and 144\", \"stance\": \"supports\", \"note\": \"'fermentum \\\"Gärungsstoff, Sauerteig\\\" (: ags. beorma, engl. barm …); auch fer-uere S. 144' and 'Lat. ferveō, -ere, fervō, -ere \\\"sieden, wallen\\\"'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. fermentum\", \"stance\": \"supports\", \"note\": \"'Fermentum doit s'analyser *bher-mentom, le thème étant fourni par une forme non élargie de la racine de ferueo.'\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. ferment, fervent, barm\", \"stance\": \"supports\", \"note\": \"'ferment … fr. L. fermentum … fr. I.-E. base *bher-, \\\"to boil up, seethe\\\". See barm and cp. fervent.'\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"ferment; fervent\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both are learned Romance borrowings, not inherited words. ferment (n., late 14th c. in the sense 'leaven') came through French ferment from Latin fermentum; the verb from French fermenter < Latin fermentāre (Klein: 'ferment, n. — F., fr. L. fermentum … ferment, tr. and intr. v. — F. fermenter, fr. L. fermentare'). fervent (14th c., Chaucer) is Old French fervent from Latin fervēns, gen. -entis, the present participle of fervēre (Klein: 'fervent, adj. … L. fervens, gen. -entis, pres. part. of fervere, \\\"to boil, glow, foam\\\", fr. I.-E. base *bheru-, enlarged form of *bher-'); the figurative sense 'ardent, zealous' is already Latin. Both therefore rejoin the root only through node #6.\",\n     \"derivation_fa\": \"این دو واژه وام‌گیری‌های عالمانه از لاتینی‌اند و میراث مستقیم انگلیسی نیستند: ferment از راه فرانسوی از لاتینی fermentum (و فعل آن از fermenter/fermentāre) در سدهٔ چهاردهم میلادی وارد انگلیسی شد، و fervent از فرانسوی کهن fervent از fervēns، اسم فاعلِ fervēre «جوشیدن». معنای مجازی «پرشور» پیش‌تر در خود لاتینی پدید آمده بود. پیوند این دو با ریشه تنها از راه گرهٔ لاتینی است. ادعای نورایی درست است.\",\n     \"sources\": [W_PIE_BREW],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins bhreu-2 III.1.b and III.2 name FERMENT and FERVENT/FERVID/FERVOR as the English outcomes; index: 'FERMENT bhreu-2 … FERVENT bhreu-2'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. ferment, fervent\", \"stance\": \"supports\", \"note\": \"quoted in the derivation.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins index\", \"stance\": \"supports\", \"note\": \"'FERMENT bhreu-? [bhreu-2] … FERVENT bhreu-2 FERVID bhreu-2 FERVOR bhreu-2'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Bhereg, Bhreg\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *bʰerHǵ- (older notation *bherəg- : *bhrēǵ-) 'to shine, be white'; for the Iranian branch *bʰreh₁ǵ- (LIV 92)\",\n   \"note\": \"Pokorny IEW 139-140: 'bherəg- : bhrēg- \\\"glänzen, weiß\\\", wozu auch der Birkenname N. Sg. *bherəg-s … Gleichwertig mit bherek-'; Walde-Pokorny II 170 has the same lemma. Watkins: 'bhereg-. To shine; bright, white. Compare the by-form bherek- … [Pok. bherəg- 139.]'. Nourai's two variant names 'Bhereg, Bhreg' are exactly Pokorny's full-grade and reduced-grade forms of the one root, the language label is right and the gloss 'to shine, bright' is Pokorny's own. Modern laryngeal notation is *bʰerHǵ- (so Wiktionary s.v. *berhtaz, *berkō) and, for the verb continued in Iranian and Indic, *bʰreh₁ǵ- (LIV 92, cited by Cheung).\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰerHǵ- (در نگارش کهن‌تر bherəg- : bhrēg-) «درخشیدن، سپید بودن»؛ همین ریشه نام «توس» (birch) را نیز ساخته است، چون درختی سپیدپوست است. پوکورنی در صفحهٔ ۱۳۹–۱۴۰ و والده–پوکورنی در جلد دوم صفحهٔ ۱۷۰ همین دو گونهٔ آوایی را می‌آورند که نورایی زیر نام Bhereg و Bhreg آورده است؛ برای شاخهٔ ایرانی و هندی صورت *bʰreh₁ǵ- بازسازی می‌شود (LIV ۹۲). برچسب زبانی و معنا هر دو درست است.\",\n   \"sources\": [W_BERHTAZ, W_BERKO],\n   \"ref_check\": [\n    {\"ref\": \"POK:139\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 147-148 (= printed p.139-140): '-bhreg- [bherəg-] \\\"glänzen, weiß\\\", wozu auch der Birkenname N. Sg. *bherəg-s … Gleichwertig mit bherek-. ai. bhrājate \\\"glänzt, strahlt\\\"; apers. brāzaiti ds. (*bhrēĝō), npers. barāzidan \\\"glänzen\\\", barāz \\\"Schmuck\\\" … Mit Hochstufe der 1. Silbe: got. bairhts … ags. beorht (engl. bright) … Im Namen der Birke: ai. bhūrjá-, osset. bärz, ahd. birihha, ags. beorc'. The page carries the whole entry, root box and all four nodes.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 139-140\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.170\", \"stance\": \"supports\", \"note\": \"'bhereg- \\\"glanzen\\\", wozu auch der Birkenname … ai. bhrājate … ap. brāzaiti \\\"strahlt, glänzt\\\", brāza- \\\"blinkend, schimmernd\\\" … np. barāzīdan \\\"glänzen\\\", baraz \\\"Schmuck\\\" (die ar. Worte nicht zu bhleg \\\"glänzen\\\", s. Walde KZ 34, 514f.)' — note the explicit refusal to connect the Indo-Iranian words with *bhleg-, which is what Horn had suggested.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins s.v. bhereg-\", \"stance\": \"supports\", \"note\": \"'bhereg-. To shine; bright, white … 1. Germanic *berhtaz, bright … 2. \\\"The white tree\\\", the birch … [Pok. bherəg- 139.]'\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. bright, birch\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *bhereg-, \\\"to shine, be white\\\", whence also OI. bhrājate, \\\"shines, glitters\\\", Lith. brėkšta, W. berth, \\\"bright, beautiful\\\"'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"brâz\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Young Avestan brāz- 'to shine' is well attested: Bartholomae, Altiranisches Wörterbuch col. 971-972, 'j. brāz- V. \\\"strahlen\\\". Praes. brāza-: \\\"strahlen, glänzen\\\": tanūm … yeŋhe ainikō brāzaiti yaθa tištryehe Yt. 10.143 … mit Akk.: caročma vanᵊnto brāzəṇta … Yt. 5.129. — ai. bhrājati; np. barāzīdan', with the derived brāza- adj. 'blinkend, schimmernd', n. 'Schein, Schimmer' (Yt. 14.33). Cheung, Etymological Dictionary of the Iranian Verb, pp. 21-22, lemma *braHz 'to shine, set on fire, alight': 'YAv. brāz- \\\"to shine\\\" … PIE *bʰreH₁ǵ- \\\"to shine\\\" = LIV: 92 | Pok.: 139 f.' The Avestan verb is the exact cognate of Sanskrit bhrāj- 'to shine' (RV+). Note that Pokorny p.139 labels the form 'apers.' (Old Persian); that is a slip or a loose label, since brāzaiti occurs only in the Young Avesta — Nourai's 'Avestan' is the correct label, and Bartholomae, Cheung and Wiktionary all agree.\",\n     \"derivation_fa\": \"اوستایی نو brāz- «درخشیدن» صورتی است کاملاً مستند: بارتولمه در ستون ۹۷۱–۹۷۲ فرهنگ ایرانی باستان می‌آورد «brāz- «تابیدن، درخشیدن»: yeŋhe ainikō brāzaiti یشت ۱۰:۱۴۳»، و نیز صفت/اسم brāza- «درخشان؛ درخشش» (یشت ۱۴:۳۳)؛ هم‌ریشهٔ سنسکریت آن bhrāj- «درخشیدن» است. چونگ نیز در فرهنگ ریشه‌شناختی فعل ایرانی (ص ۲۱–۲۲) ستاک *braHz «درخشیدن، برافروختن» را از *bʰreh₁ǵ- هندواروپایی می‌گیرد. تنها نکته این‌که پوکورنی در صفحهٔ ۱۳۹ این صورت را «پارسی باستان» برچسب زده که دقیق نیست؛ برچسب «اوستایی» نورایی درست است.\",\n     \"sources\": [W_BARAZ],\n     \"ref_check\": [\n      {\"ref\": \"POK:139\", \"status\": \"supports\", \"note\": \"IEW 139: 'apers. brāzaiti ds. (*bhrēĝō), npers. barāzidan \\\"glänzen\\\", barāz \\\"Schmuck\\\"' — the derivation is there, though Pokorny mislabels the language as Old Persian (so does Walde-Pokorny II 170); the form is Young Avestan (Bartholomae col. 971).\"},\n      {\"ref\": \"BQT:137\", \"status\": \"not_found\", \"note\": \"BQT_v1_pages.txt leaf 347 = printed p.137 of the Amir Kabir/Ibn Sina reprint carries the entries اسفنج / اسفند / اسفهبد / اسفیداج — nothing on براز or Avestan brāz. Mo'in's etymological footnote on Av. brāz stands on p.247 (leaf 467, footnote 1: 'از مصدر اوستایی brāz (پرتوافکندن): سانسکریت bhrāj- «بارتولمه ۹۷۲»'), i.e. the page Nourai cites for the next node — BQT:137 looks like a misprint for BQT:247.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 971-972 (BRT.txt line 17452)\", \"stance\": \"supports\", \"note\": \"'j. brāz- V. \\\"strahlen\\\" … ainikō brāzaiti … Yt. 10.143 … ai. bhrājati; np. barāzīdan'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"pp. 21-22 s.v. *braHz\", \"stance\": \"supports\", \"note\": \"'*braHz \\\"to shine, set on fire, alight\\\". AVESTAN: YAv. brāz- \\\"to shine\\\" … PIE *bʰreH₁ǵ- = LIV: 92 | Pok.: 139 f.'\"},\n      {\"src\": \"ARY\", \"where\": \"p. 118 (pdf page 117) s.v. برازیدن، براز، برازندگی\", \"stance\": \"supports\", \"note\": \"Aryanpur's entry lists Avestan BRĀZ with Sanskrit BHRĀJ, Gothic BAIRHTS, Old English BEORHT and English BRIGHT as cognates — the same tree Nourai draws.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"barâzîdan; barâzandeh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Av. brāz- continues in Middle Persian brāzīdan, present stem brāz- — MacKenzie, Concise Pahlavi Dictionary p.19: 'brāzīdan, brāz- [bʾc-ytn' | M brʾz-, N barāzīdan] shine, gleam; ~išn: radiance, brightness'; the Manichaean MP and Parthian forms are brʾz- (Cheung 21-22). New Persian برازیدن barāzīdan arises by the regular resolution of the Middle Persian initial cluster br- with an anaptyctic vowel (MP brāz- > NP barāz-, exactly as MP brādar > NP برادر barādar, MP brēh > NP بره). برازنده barāzande is the ordinary NP present participle, present stem barāz- + -ande. The semantic shift is 'to shine' → 'to look fine' → 'to be becoming, to befit': Dehkhoda glosses برازیدن 'زیبا نمودن. خوب و زیبا نمودن (برهان)' and then '|| سزیدن. شایسته بودن. سزاوار بودن'; Mo'in has '(مص ل.) سزاوار بودن، شایسته بودن' and برازنده '(ص فا.) شایسته، زیبنده' — so Nourai's glosses 'to look nice' and 'well suited, fit' are both accurate. Mo'in's own footnote in Borhān-e Qāṭeʿ p.247 n.1 states the etymology: 'از مصدر اوستایی brāz (پرتوافکندن): سانسکریت bhrāj- «بارتولمه ۹۷۲»'. Horn, Grundriss no. 193 (p.45): 'berāz \\\"Schmuck, Schönheit\\\", berāzīden, berāziš — aw. brāza-, brāzaiti \\\"er strahlt\\\"; phlv. brāz(i)šn … ai. bhrājate'.\",\n     \"derivation_fa\": \"«برازیدن» و «برازنده» بازماندهٔ فارسی میانهٔ brāzīdan / ستاک حال brāz- «درخشیدن» است (مکنزی، فرهنگ کوچک پهلوی، ص ۱۹: brāzīdan, brāz- ⟨bʾcytn'⟩، پهلوی مانوی و پارتی brʾz-)، و آن خود از اوستایی brāz- می‌آید. خوشهٔ آغازین br- فارسی میانه در فارسی نو با واکهٔ میانجی گشوده شده است: brāz- ← barāz-، درست مانند brādar ← «برادر». «برازنده» صفت فاعلی معمول فارسی است: ستاک حال barāz- + پسوند ‑نده. تحول معنایی «درخشیدن» ← «زیبا نمودن» ← «شایسته بودن» را دهخدا («زیبا نمودن؛ || سزیدن، شایسته بودن») و معین («سزاوار بودن، شایسته بودن») نشان می‌دهند، و حاشیهٔ معین بر برهان قاطع (ص ۲۴۷، پانوشت ۱) خود می‌نویسد: «از مصدر اوستایی brāz (پرتوافکندن): سانسکریت bhrāj- «بارتولمه ۹۷۲»». ادعای نورایی درست است.\",\n     \"sources\": [W_BARAZ, A_BARAZIDAN, A_BARAZANDE],\n     \"ref_check\": [\n      {\"ref\": \"BQT:247\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 467 (= printed p.247): the headword 'برازیدن، بر وزن تراویدن، بمعنی خوب و زیبا نمودن' carries footnote 1: 'از مصدر اوستایی brāz (پرتوافکندن): سانسکریت bhrāj- «بارتولمه ۹۷۲»'. Leaf 466 (p.246) has برازنده 'بمعنی برازندگی و زیبایی' with a footnote giving the Avestan form for 'زینت، آرایش'. Exactly Nourai's arrow.\"},\n      {\"ref\": \"MON:493\", \"status\": \"partial\", \"note\": \"Mo'in's entries were read online (abadis.ir, section فرهنگ معین): برازیدن '(بَ دَ) (مص ل.) سزاوار بودن، شایسته بودن'; برازنده '(بَ زَ دَ) (ص فا.) شایسته، زیبنده'. They confirm the words and glosses but give no etymology, and the 6-volume pagination is not reproducible online, so p.493 itself could not be verified.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.19 s.v. brāzīdan (PHD.txt line 281)\", \"stance\": \"supports\", \"note\": \"'brāzīdan, brāz- [bʾc-ytn' | M brʾz-, N barāzīdan] shine, gleam. ~išn: radiance, brightness.'\"},\n      {\"src\": \"HRN\", \"where\": \"no. 193, p. 45\", \"stance\": \"supports\", \"note\": \"'berāz \\\"Schmuck, Schönheit\\\", berāzīden, berāziš — aw. brāza-, brāzaiti \\\"er strahlt\\\"; phlv. brāz(i)šn \\\"geschmückt\\\" … ai. bhrājate'. Horn adds 'Also zu gr. φλέγω, φλόξ', i.e. he also links it with *bhleg- — a connection Walde-Pokorny II 170 explicitly rejects.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 22 s.v. *braHz, NWIR section\", \"stance\": \"supports\", \"note\": \"'NWIR: NP barazidan/baraz- \\\"to shine, beam\\\"'.\"},\n      {\"src\": \"MON\", \"where\": \"s.v. برازیدن / برازنده (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"'سزاوار بودن، شایسته بودن' / 'شایسته، زیبنده'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien, searched HUB.txt for brāz/barāz\", \"stance\": \"silent\", \"note\": \"Hübschmann has no entry for this verb.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Sogdian\",\n     \"words\": \"br`z`nt\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Gharib, Sogdian Dictionary, entry 2681 on printed p.106 (SOD_pages.txt leaf 171): 'βrʼznt B — βrāzand ⓔ MP brʾz-, Khwar. βrz-, Av. brāz- → βrʼz-, βrʼzndtyy — shining — BSTBL, Dhy. 212', with the neighbouring 2682 βrʼzyntk 'βrāz(a)nde, βrāzənde — burning, ablaze'. The word is the present participle of the same verb: Sogdian βrāz- < Old Iranian *brāz- with the regular Sogdian spirantization of initial b- to β-, plus the inherited participial suffix -ant- (Av. -aṇt-, Skt. -ant-). Cheung p.22 cites the fuller spelling 'BSogd. βrʼʼzʼʼnt \\\"shining\\\"' — with the two ʼalephs, i.e. exactly Nourai's transliteration br`z`nt (his backtick = ʼaleph). Page reference and gloss are both right.\",\n     \"derivation_fa\": \"صورت سغدی βrʼzʼnt (خوانش βrāzand) «درخشان» اسم فاعل (صفت فاعلی) همان فعل است: ستاک βrāz- از ایرانی باستان *brāz- — با تبدیل قاعده‌مند b آغازی به β در سغدی — به‌علاوهٔ پسوند اسم فاعلی ‑ant که در اوستایی ‑aṇt‑ و در سنسکریت ‑ant‑ است. قریب در فرهنگ سغدی (مدخل ۲۶۸۱، ص ۱۰۶) می‌آورد: «βrʼznt، خوانش βrāzand، مقایسه شود با فارسی میانه brʾz-، خوارزمی βrz-، اوستایی brāz-؛ معنی: درخشان»، و مدخل بعدی βrʼzyntk «سوزان، شعله‌ور». چونگ نیز صورت βrʼʼzʼʼnt را می‌آورد که دقیقاً با نگارش نورایی می‌خواند. ارجاع SOD:106 درست است و ادعای نورایی پذیرفته می‌شود.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:106\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 171 (printed page ≈ leaf − 66, and the following leaf 172 carries the running number 107, so leaf 171 = p.106): entry '2681 βrʼznt B — βrāzand … Av. brāz- … shining'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"entry 2681, p.106\", \"stance\": \"supports\", \"note\": \"quoted above; Gharib himself refers the form to Av. brāz-.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.22 s.v. *braHz, Sogdian section\", \"stance\": \"supports\", \"note\": \"'BSogd. βrʼʼzʼʼnt \\\"shining\\\", BSogd. βrʼʼzyntk, MSogd. βrʼzn(d)tyy \\\"ablaze\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Germanic\",\n     \"words\": \"berhtaz; berkjôn; adel-beraht\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Watkins s.v. bhereg-: '1. Germanic *berhtaz, bright, in Old English beorht, bright: BRIGHT. 2. \\\"The white tree\\\", the birch (also the ash): a. Germanic *birkjōn- in Old English birc(e), birch: BIRCH; b. suffixed zero-grade form *bhrəg-s- probably in Latin fraxinus, ash tree'. Wiktionary derives *berhtaz from *bʰer(H)ǵ-tó-s, i.e. the *-tó- verbal adjective 'having shone' > 'bright' (cf. Proto-Celtic *berxtos, Welsh berth 'bright, beautiful'), and *berkō/*birkjōn from *bʰerHǵós, cognate with Sanskrit bhūrjá-, Ossetic bærz, OCS brěza — 'the white tree'. Nourai's 'berkjôn' is Watkins' *birkjōn- with e for i (the ablaut variant *berkō is equally reconstructed, so the form is not an error). 'adel-beraht' is Old High German Adal-beraht 'noble-bright', the source of Albert; Pokorny explicitly notes the name element: 'ahd. beraht, mhd. berht \\\"glänzend\\\" (auch in Namen ahd. Bert-, -bert, -brecht)'.\",\n     \"derivation_fa\": \"این سه صورت ژرمنی آغازین همان‌اند که واتکینز زیر ریشهٔ bhereg- می‌آورد: *berhtaz «درخشان» (انگلیسی کهن beorht) که از صفت مفعولی/فاعلی *bʰer(H)ǵ-tó-s ساخته شده؛ *birkjōn- «درخت سپید، توس» (انگلیسی کهن birce) از *bʰerHǵós، هم‌ریشه با سنسکریت bhūrjá-، اوستی bærz و اسلاوی کهن brěza؛ و adal-beraht آلمانی علیای کهن «درخشان در نجابت» که نام Albert از آن است. نگارش «berkjôn» نورایی همان *birkjōn- است با e به‌جای i، و خطای چاپی به‌شمار نمی‌آید زیرا گونهٔ *berkō نیز بازسازی می‌شود. پوکورنی خود می‌نویسد که این ستاک در نام‌های آلمانی به صورت Bert-، -bert و -brecht دیده می‌شود. ادعای نورایی درست است.\",\n     \"sources\": [W_BERHTAZ, W_BERKO],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. bhereg-, quoted in full in the derivation; the reverse index reads 'BIRCH bhereg-' and 'BRIGHT bherəg-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins s.v. bhereg-\", \"stance\": \"supports\", \"note\": \"'*berhtaz … BRIGHT … *birkjōn- in Old English birc(e), birch: BIRCH'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 139-140\", \"stance\": \"supports\", \"note\": \"'got. bairhts \\\"hell, glänzend, deutlich\\\", ahd. beraht, mhd. berht \\\"glänzend\\\" (auch in Namen ahd. Bert-, -bert, -brecht), ags. beorht (engl. bright) … ahd. birihha (*bherəg-iā), ags. beorc, birce, aisl. bjǫrk \\\"Birke\\\"'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.170\", \"stance\": \"supports\", \"note\": \"'Mit Hochstufe der 1. Silbe: got. bairhts \\\"hell, glanzend, deutlich\\\", ahd. beraht, mhd. berht \\\"glanzend\\\" (auch in Namen ahd. Bert-, -bert, -brecht), ags. beorht \\\"glanzend, strahlend\\\" (engl. bright)'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. bright, birch\", \"stance\": \"supports\", \"note\": \"'bright … fr. I.-E. base *bhereg- … Cp. birch'; 'birch … All these words lit. mean \\\"the white (or bright) tree\\\" and derive fr. I.-E. base *bhereg-'.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"bright, Albert, Robert; birch\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"bright: OE beorht (with the usual West Germanic metathesis from *breht-) > ME briht, bryht > bright. birch: OE bierce, beorc > ME birche > birch. Albert reached English from the continental Germanic name OHG Adal-beraht 'noble-bright' through French (Klein s.v. Etheldred/Albert: 'Albert, which derives — through the medium of French — fr. OHG. Adalbert, the exact equivalent of OE. Æðelbryht'); it was re-popularised in England by Queen Victoria's consort. Robert is OHG Hrōd-beraht 'fame-bright' (OFr Robert), brought over by the Normans; only its second element belongs to this root, the first being Germanic *hrōþiz 'fame'. Klein s.v. bright gathers exactly this family: 'Cp. Bertha, the first element in Bardolph, Bertram, and the second element in Albert, Cuthbert, Egbert, Ethelbert, filbert, Gilbert, Herbert, Hubert, Lambert, Robert'.\",\n     \"derivation_fa\": \"bright از انگلیسی کهن beorht (با قلبِ آوایی *breht- ← beorht) و birch از انگلیسی کهن bierce/beorc می‌آید. نام Albert از آلمانی علیای کهن Adal-beraht «نجیب‌درخشان» است که از راه فرانسه به انگلیسی رسید و در سدهٔ نوزدهم با نام همسر ملکه ویکتوریا رواج تازه یافت؛ Robert نیز از Hrōd-beraht «نام‌آورِ درخشان» است که نورمن‌ها به انگلستان بردند — یعنی تنها جزء دوم این نام به ریشهٔ مورد بحث می‌رسد و جزء نخست *hrōþiz «آوازه» است. کلاین همین خانواده را زیر مدخل bright گرد آورده است. ادعای نورایی درست است، با این توضیح که در Robert تنها نیمهٔ دوم نام از این ریشه است.\",\n     \"sources\": [W_BERHTAZ, W_BERKO],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The English box in this entry carries no reference icon on the printed page (checked on the page image, data/verification/sources/refs/ocr/BOOK/91.png), and the JSON accordingly has refs=None. Verified independently against Klein and Watkins.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. bright, birch, Albert (s.v. Etheldred)\", \"stance\": \"supports\", \"note\": \"'bright … Cp. also Bertha … and the second element in Albert, … Robert'; 'Albert … derives — through the medium of French — fr. OHG. Adalbert'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins index\", \"stance\": \"supports\", \"note\": \"'BIRCH bhereg-', 'BRIGHT bherəg-'.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open(\"data/verification/page-91.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk91.py",
 "description": "Write page-91.json"
}
```


### [2026-09-05T14:03:52.625Z] TOOL RESULT

```
written
```


## [2026-09-05T14:04:00.417Z] TOOL CALL #69: Bash

```json
{
 "command": "ls -la data/verification/page-91.json && python3 -m json.tool data/verification/page-91.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 91",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T14:04:02.287Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 51089 Sep  5 10:03 data/verification/page-91.json
JSON OK
nodes verified: 12/12
node verdicts: {'disputed': 1, 'confirmed': 9, 'plausible': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'contradicts': 1, 'partial': 3, 'not_found': 1, 'not_checked': 1}
books consulted: {'contradicts': 2, 'silent': 4, 'supports': 27, 'partial': 3} | by book: {'KLN': 8, 'AHD': 7, 'POK': 4, 'CHEUNG': 3, 'MON': 2, 'HRN': 2, 'ARY': 2, 'BQT': 1, 'SKT': 1, 'LAT': 1, 'BRT': 1, 'PHD': 1, 'HUB': 1, 'SOD': 1, 'WLD': 1}
```


## [2026-09-05T14:04:26.142Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-91.json` written; `verify_check.py 91` reports 12/12 nodes, 0 PROBLEM lines.

**Page 91 (book p.61) — verdict counts**
- Roots: 2 confirmed (Bher 5/Bheru/Bhereu/Bhreu/Bhru 2 = Pokorny's bher-2 + bh(e)reu-; Bhereg/Bhreg = Pokorny 139 bherəg-/bhrēg-)
- Nodes: 9 confirmed, 2 plausible, 1 disputed
- Ref checks: 9 supports, 3 partial, 1 contradicts, 1 not_found, 1 not_checked; 15 books consulted (KLN, AHD, POK, WLD, LAT, SKT, BRT, PHD, HRN, HUB, CHEUNG, SOD, BQT, MON, ARY) plus Wiktionary/Etymonline/Dehkhoda-Mo'in (all archived via fetch_source.py).

**Disputed**
- Bher 5 #1 Persian `balvâ` بلوا "tumult": Dehkhoda ("از ع، اِ") and Mo'in ("[ع. بلوی]" — the MON:575 Nourai himself flags) make it the Arabic loan بَلْوَى from root ب ل و; the IE derivation rests solely on Mann IEC 116 ("Z-gde radical in Per. balwà 'tumult'"), which no Iranian etymological dictionary follows, and *bʰru- would not give NP balv-.

**Plausible (documented splits, no transcription flags)**
- Bher 5 #4/#5 Germanic `brěthaz, bres, brenw, brandaz` → `breath, braise/breeze, burn, brand/Brandy`: Pokorny (145-146), Klein and Kroonen put *brenw-/*brandaz/*brēþaz here, but Nourai's own cited AHD assigns BURN/BRAND/BRANDY to gʷher- and BREATH to gʷhrē- (only braise/breeze² are under bhreu-2). Also: the chart's bare "breeze" is breeze² "charcoal refuse" (< F. braise); breeze "light wind" (< F. brise) is unrelated. "bres" is the book's loose citation of Gmc *brasa-.

**Reference errors found in the book (not extraction errors)**
- Bhereg #1 `BQT:137` → not_found: p.137 of Borhān vol.1 is the اسفند/اسفهبد range. Mo'in's footnote on Av. brāz ("از مصدر اوستایی brāz … «بارتولمه ۹۷۲»") is on p.247 — apparently a misprint for BQT:247.
- POK:139 and WLD II 170 both label brāzaiti "apers."; the form is Young Avestan (Bartholomae col. 971-972) — Nourai's "Avestan" label is the correct one.

**Extraction errors: none.** I rendered PDF p.91 and compared every box: all transliterations, glosses, Persian script (بلوا، برازیدن، برازنده), refs and the missing-refs English box in entry 2 match the print exactly. Page image archived at `data/verification/sources/refs/ocr/BOOK/91.png`.
