# Verification process log — verify-page-411


## [2026-09-14T01:07:50.489Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 411 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-411.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-411.json. Write /home/sfmqrb/git/rishe/data/verification/page-411.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 411` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:07:51.471Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:07:52.187Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:07:52.199Z] TOOL RESULT

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


## [2026-09-14T01:07:52.760Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-411.txt"
}
```


### [2026-09-14T01:07:52.802Z] TOOL RESULT

```
1	=== PDF page 411 (book page 381) ===
2	--- entry 0 ---
3	ROOT Qeud -> redirect to Keued
4	--- entry 1 ---
5	ROOT Qhâd -> redirect to Khâd
6	--- entry 2 ---
7	ROOT Qhar -> redirect to Kar 1
8	--- entry 3 ---
9	ROOT [Arabic] Qirbah, Qirrâbah : a leathern bottle  (refs AHD:202)
10	#1 (parent #0) [Persian] refs=AHD:202; FVA:328; MON:2651 | Qarrâbeh «قرّابه ( قراب )» : a glass bottle (for wine)
11	#2 (parent #0) [English] refs=WEB:272; KLN:238; AHD:202 | carboy : large glass bottle
12	--- entry 4 ---
13	ROOT Qirrâbah -> redirect to Qirbah
14	--- entry 5 ---
15	ROOT [Arabic] Q.l.y : to cook or barbecue meat  (refs SAP:93)
16	#1 (parent #0) [Arabic] refs=None | Qely, Qela : alkaline material obtained from wood ash
17	#2 (parent #0) [Persian] refs=SAP:94; MON:2724 | qalya «قلیا» : alkaline ; qalyeh «قلیه» : a food made with meat
18	#3 (parent #0) [French] refs=KLN:50 | alcali : alkali
19	  #4 (parent #3) [English] refs=KLN:50 | alkali, alkaline
20	--- entry 6 ---
21	ROOT Qor -> redirect to Ker 3
22	--- entry 7 ---
23	ROOT Qr -> redirect to Ker 3
24	--- entry 8 ---
25	ROOT Qreu -> redirect to Kreu
26	--- entry 9 ---
27	ROOT Qreus -> redirect to Kreu
28	
```


## [2026-09-14T01:07:56.529Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-411.json | head -200",
 "description": "Read source JSON for page 411"
}
```


### [2026-09-14T01:07:57.691Z] TOOL RESULT

```
{
    "pdf_page": 411,
    "book_page": 381,
    "entries": [
        {
            "root": {
                "name": "Qeud",
                "redirect": "Keued"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Qh\u00e2d",
                "redirect": "Kh\u00e2d"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Qhar",
                "redirect": "Kar 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Qirbah, Qirr\u00e2bah",
                "lang": "Arabic",
                "refs": "AHD:202",
                "gloss": "a leathern bottle"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "AHD:202; FVA:328; MON:2651",
                    "words": [
                        {
                            "translit": "Qarr\u00e2beh",
                            "gloss": "a glass bottle (for wine)",
                            "script": "\u0642\u0631\u0651\u0627\u0628\u0647 ( \u0642\u0631\u0627\u0628 )"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u062f\u0631 \u0639\u0647\u062f \u067e\u0627\u062f\u0634\u0627\u0647 \u062e\u0637\u0627 \u0628\u062e\u0634 \u062c\u0631\u0645 \u067e\u0648\u0634 - \u062d\u0627\u0641\u0638 \u0642\u0631\u0627\u0628\u0647 \u06a9\u0634 \u0634\u062f \u0648 \u0645\u0641\u062a\u06cc \u067e\u06cc\u0627\u0644\u0647 \u0646\u0648\u0634",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "English",
                    "refs": "WEB:272; KLN:238; AHD:202",
                    "words": [
                        {
                            "translit": "carboy",
                            "gloss": "large glass bottle",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Qirr\u00e2bah",
                "redirect": "Qirbah"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Q.l.y",
                "lang": "Arabic",
                "refs": "SAP:93",
                "gloss": "to cook or barbecue meat"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": null,
                    "words": [
                        {
                            "translit": "Qely, Qela",
                            "gloss": "alkaline material obtained from wood ash",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "SAP:94; MON:2724",
                    "words": [
                        {
                            "translit": "qalya",
                            "gloss": "alkaline",
                            "script": "\u0642\u0644\u06cc\u0627"
                        },
                        {
                            "translit": "qalyeh",
                            "gloss": "a food made with meat",
                            "script": "\u0642\u0644\u06cc\u0647"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "French",
                    "refs": "KLN:50",
                    "words": [
                        {
                            "translit": "alcali",
                            "gloss": "alkali",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": "KLN:50",
                    "words": [
                        {
                            "translit": "alkali, alkaline",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Qor",
                "redirect": "Ker 3"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Qr",
                "redirect": "Ker 3"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Qreu",
                "redirect": "Kreu"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Qreus",
                "redirect": "Kreu"
            },
            "nodes": []
        }
    ]
}
```


## [2026-09-14T01:07:58.298Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','WEB','KLN','MON','FVA','SAP','POK','ARY','BQT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-14T01:07:59.409Z] TOOL RESULT

```
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "c

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
```


## [2026-09-14T01:08:08.061Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80"
}
```


### [2026-09-14T01:08:08.113Z] TOOL RESULT

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


## [2026-09-14T01:08:10.244Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','WEB','KLN','MON','SAP','FVQ','AFM','PLA','LKT','AFA','SKT','FSD','DOZ','DEV','PHN','LAM']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print(k, '|', v.get('local_file'), '|', v.get('page_offset'))\n\""
}
```


### [2026-09-14T01:08:11.445Z] TOOL RESULT

```
AHD | /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
WEB | /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KLN | /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
MON | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | None
SAP | None | None
FVQ | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
AFM | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
PLA | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
LKT | /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
AFA | /home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt | leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SKT | /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
FSD | /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
DOZ | /home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt | leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
DEV | /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt | leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
PHN | /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt | leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
LAM | /home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt | leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-14T01:08:15.812Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in KLN_1966.txt KLN_1971.txt WEB_vol1.txt SKT.txt FSD_vol1.txt LKT.txt DEV.txt DOZ.txt PHN.txt LAM.txt AFA.txt HJB.txt AID.txt; do\n  echo \"=== $f\"; grep -n -i -E 'carboy|carbo[iy]|qarraba|qirbah|karaba' $f | head -12\ndone"
}
```


### [2026-09-14T01:08:17.053Z] TOOL RESULT

```
=== KLN_1966.txt
6511:carboy,  n..  a  large  glass  bottle.  —  Pers.  qaraba.
6512:Cp.  Arab.  qirbah,  ‘a  large  leathern  bottle', carbuncle,  n.,  1)  formerly,  a  red  gem;  now  a  gar¬ net  with  a  convex  rounded  surface;  2)  a  painful inflammation  under  the  skin.  —  ME.,  fr.  ONF. carbuncle  (corresponding  to  OF.  charboncle , charbucle),  fr.  L.  carbuneulas,  ‘a  small  coal;  a bright,  reddish  kind  of  precious  stone;  a  kind of  tumor',  dimin.  of  carbo,  gen.  -onis,  ‘coal’. See  carbon  and  cp.  escarbuncle.
=== KLN_1971.txt
39538:carboy, n., a large glass bottle. — Pers. qaraba. 
=== WEB_vol1.txt
=== SKT.txt
23880:Carboy,  a  large  giasr  bottle,  protected by  wicker-work.  (Arab.?)  hers,  oardba. a  large  flagon ;  which  is  prob.  o\  Arab, origin.  Cf.  Pers.  and  Arab,  qirbah,  a water-skin,  water-boltle-
=== FSD_vol1.txt
18412:mlc);  strychnin  (tannic  acid,  cWoral);  sulfuric  acid  (al-  an^ti-gug'gler,  n.  An  air-tube  Inserted  m   the  mouth  of  a kalis,  lime-water,  soda):  tobacco,  see  nicotin;  turpen-  narrow-necked  vessel,  as  a   bottle,  carboy,  etc.,  to  prevent tine  (water,  demulcents);  zinc  (milk,  eggs,  carbonate  of  gurgling  and  splashing  when  the  contents  are  poured  out. potash).  [F.,  <   L.  antidolum,  <   Gr.  antidoton,  <   anti ,   an^tl-guriglerj.—  an"tl-ha-la  tlon^o.  ^Intended^to  coun-
=== LKT.txt
242:Ganzseide  [auch  ins  Semitische  über- gegangen :  syr.  abräsom,  ahr'isüm  BrLex- Syr  ob;  ar.  ibnsam,  ibrisum,  schon häufig  mit  der  Bedeutung  'Seidenfaden, Seidenzwirn',  vgl.  Joseph  Karabacek, Über  einige  Benennungen  mittelallei'- 1  icher  Gewebe  I.  Wien  1882.  S.  21 bis  2'2.].  Ins  Tk.  übergegangen  als  ibri- sim  [offenbar  mit  Anlehnung  an  die Wurzel  ip,  ib  'winden'  Vämbeiy  Tkt- EtWb  Nr.  37].  Aus  dem  Tk.  wurde  rum. ibri^im,  ibri^in  'Seidenfaden,  Zwirn'; Ableitung  ibri^inar.
517:'Glatt,  fein'.  Von  einem  Manne,  der nicht  viel  taugte,  sagte  man,  er  sei atlas;  ebenso  von  Seide,  sie  sei  atlas, d.  h.  minderwertig;  schheßlich  blieb das  Adjektiv  allein  zur  Bezeichnung  des Stofifes  [wie  z.  B.  im  Romanischen,  wo aus  lat.  ieciir  firatum  frz.  foie  'Leber', aus  lat.  caseum  fonnaticum  frz.  froinaffe 'Käse'  wurde],  und  zwar  des  sog.  Seiden- satins  [s.  hier  Nr.  2188].  Rum.  atlas, atlaz;  russ.  atlas,  bulg.  atlaz,  serb.  cech. atlas,  poln.  atlas  'Satin'.  Dtsch.  Atlas, ndl.  atlas.  [Joseph  Karabacek,  Über einige  Benennungen  mittelalterlicher Gewebe.  Wien  188±  S.  llfT.  Gorjajew 7.  Hobson-Jobson  39/40.  Kluge  '25. Dozy  Oost  22.
539:141.  Pers.  äzärg-Qii: Teuerfarben'  (aus  pers.  äzär  'Feuer' Horn  NpEt  S.  4,  Nr.  9  und  gün  'Farbe' ebenda  S.  211,  Nr.  946].  Hieraus  ar. zarkün  und  weiter  sp.  azarcön  'Mennig', pg.  zarcäo,  azarcäo;  volksetymologisch entstellt  auch  it.  panni  di  sirico  und ähnl.  [DE  225/226.  Dicc  Gast  296. Karabacek  (s.  hier  Nr.  131)  S.  8  unten.
2483:'Damast  oder  Brokat'  [aus  chin.  kmisa, kinsa,  d.h.  glatte  haarlose  Seidengewebe, oft  von  satinartiger  Textur,  also  'Brokat', häufig  mit  Gold  durchwirkt,  vgl.  chin. kin  'Gold',  Karabacek,  Über  einige  Be- nennungen mittelalterlicher  Gewebe. Wien  1882,  S.  11/12],  tk.  kemha;  hier- aus bulg.  kamuha,  serb.  kamka,  poln. kamcha  'dass.',  russ.  kamka  'Damast', kamcatka  'Damastleinwand,  Tischzeug'; sp.  camocän  [daneben  ungebräuchlich geworden:  camucdn  'orientahscher  Bro- kat' Dicc  Gast  440],  frz.  camocan  'kost- barer BrokatstofP,  canque  'chin.  Baum- wolleinen'; angloind.  kincob,  kingcob 'Goldbrokat'.  [Gorjajew  130.  Bern  SlEtWb 477.    Devic  80/81.    IB  246,  Anm.  1.
2549:'Große  lederne'  Milchflasche'  [offenbar mit  ar.  kirba  'Schlauch'  verwandt] ;  hier- aus engl,  carboy  'große  Glasflasche  zum Verschicken  von  Säuren  und  Explosiv- stoffen' [Hobson-Jobson  162/163].  — , Wenig  appetithch  ist  der  Anblick  der sauren  Milch,  die  in  einem  Zeugbeutel mitgeschleppt  wird,  der  an  dem  Hinter- schenkel des  Pferdes  herabhängt.  Die durchträufelnde  Flüssigkeit  gibt  dem Pferde  einen  sehr  widerlichen  Anbhck, der  vor  dem  Genüsse  der  so  transpor- tierten Milch  abschreckt.  Hat  die  Milch in  dieser  Weise  ein  gut  Stück  Weges hinter  sich,  so  ist  in  dem  Beutel  eine weiße  käseartige  Masse  zurückgeblieben, die  von  den  Persern  unter  dem  Namen Mas  zum  Brote  gegessen  wird."  Brugsch, Reise  der  k.  preußischen  Gesandtschaft nach  Persien  1860  u.  1861.  Leipzig 1862.  I,  156.
2988:'Meistens  aus*  iVilpferdhaut  hergestellte Peitsche,  Ochsenziemer';  hieraus  bulg. kot-baö  'Peitsche  aus  Leder(riemen)',  serb. korobac,  poln.  korbacz,  karbacz,  kara- bacz,  russ.  (dial.)  karbuc,  klruss.  karbac, öech.  karabaö;  dtscli.  Karbatsche  'Hetz- peitsche', dän.  krabask,  schwed.  karbas 'Rute',  ndl.  karbats,  karwats,  Vb.  kar- batsen;  runi.  girhaciü  'Peitsche,  Geißel', cärbäciü  'Stock  für  die  Bastonnade',  sp. corbacho,  frz.  cravache  'Reitpeitsche'. [ML  4691.  Kluge  228.  Bern  SlEtWb  568.
4790:gandin  'eine  Art  Mull ;  ein  glattes,  feines Baumwollengewebe  dichter  als  Musselin'. [Mfi  9082.  Karabacek,  Über  einige  Be- nennungen mittelalterlicher  Gewebe. I.  Wien  1882.  S.  21/22.
4892:N.  pr.,  Name,  mit  dem  im  MA  der  große chinesische  Ausfuhrhafen  Tseutung  oder Tswan-tschou-fu  in  Fokien  [MP  408/410; JB  246/247]  bezeichnet  wurde.  Hier- nach wurden  gewisse  Damaststoffe  ar. atlas  zaitüm  'zaitunischer  Satin'  ge- nannt; hieraus  sp.  aceituni,  setuni,  mfrz. zatony,  frz.  satin,  mit.  zetani,  it.  zetani- no,  setino  [mit  Anlehnung  an  seta];  engl. satin,  dtsch.  Satin.  Vgl.  ausführlich Karabacek,  Über  einige  Benennungen mittelalterlicher  Gewebe.  I.  Wien  1882. S.  12/13.  Hirth  ChinFW  204/205  weist darauf  hin,  daß  in  den  Seidenfabriken Kantons  noch  heutzutage  derselbe  Stoff, den  wir  gewöhnlich  als  Seidenatlas  be- zeichnen, unter  den  Namen  ssü-tuan, kantonesisch  szetün  'Seiden-Atlas'  ver- kauft wird.  Es  scheint,  daß  ar.  Käufer im  Laufe  der  Jahrhunderte  dieses  un- mittelbar eingeführte  Wort  mit  dem ähnlich  klingenden  Namen  ihrer  schon vor  Kanton  berühmt  gewordenen  Han- delskolonie Zaitiln  verwechselt  haben. [Hobson-Jobson  797.  DE  340.  Eguilaz 20/21.    ML  8962.
6028:i  cabale  9Ti j  caia,<t  993 1  cabaya  971 I  caftZe  766 I  carf«  984 j  m/f  er  997 i  co^re  997 !  ca^Zrt  996 '  ca/<o«  774 I  ca'ique  1014 i  cajeput  1142 j  cajuput  1142 I  caladium  1153 I  calam,in  1149 :  (■a^ff/'a  798 i  calender  1024 j  ca//ftßr  1030 I  cöiiöre  1030 I  CaZ/co  1031 caZtpfc  798 caliver  1030 camel  653 camphor  1100 campong  1045 capers  978 far«/fe  689 cara<  1182 Caravan  1075 caraway  1087 carboy  1074 carmine  1219 carnac  1251 caroi»  832 casÄ  1102 cashmere  1116 I  cassock  1143 cassowary  1119 casuarina  1119 cau^ee  984 cariar  851 coze?  984 cÄanfe  1831
7653:kabala  977 kaban  975 Ä;a6a^  971 kaczan  1192 Ä:a(ft  984 fcarfy  984 kafenauz  1005 kaftan  Iii. kaik  1014 kalauz  1276 Ä;a/efca  1040 kaleta  828 Ä;afÄ;aw  1034 kalkun(t)  1031 kamcha  1043 kamfora  1100 katnlot  653 kanczug  1042 kanczuk  1042 kanfora  1100 kaparki  978 kapary  978 kapinaz  1005 kapkan  1064 karabacz  1279 karaczan  2027 karafka  689 karawana  1075 karbacz  1279 karhona  1208 karbuz  824 karczma(rz)  825 karczoch  833 kardasz  1089 fcary  1070 Ä:a<MM  1272 ÄsttM^a  1005 kawak  1134 kawiar  851 kawon  1138 kazan  1144 kazna  855 kazmirek  1116
=== DEV.txt
=== DOZ.txt
=== PHN.txt
=== LAM.txt
=== AFA.txt
=== HJB.txt
5240:CARBOY.
5263:wine  tnde  at  Shiraz,  ^ves  an  exact etching  of  a  carboy.  Littr^  mentions that  the  late  M.  Mohl  referred  caraffe. to  the  same  original;  but  see  that word.  Kardba  is  no  doubt  connected with  Ar.  iirba^  '  a  large  leathern  milk> bottle.'
8562:DEMLTOHN,  s.  A  large  glass bottle  holding  20  or  30  quarts,  or  more. The  word  is  not  Anglo-Indian,  but  it is  introduced  here  because  it  has  been supposed  to  be  the  corruption  of  an Oriental  word,  and  suggested  to  have been  taken  from  the  name  of  Damaghdn in  Persia.  This  looks  plausible  (com- pare the  Persian  origin  of  carboy^ which  is  another  name  for  just  the same  th%iia\  but  no  historical  proof has  yet  oeen  adduced,  and  it  is doubted  by  Mr.  Marsh  in  his  NaUs  (m JVedgwood^s  Dictionary,  and  by  Dozy {Sup.  mix  Diet,  Araoes),  It  may  lie noticed,  as  worthy  of  further  enquiry, that  Sir  T.  Herbert  (192)  speaks  of  the abundance  and  cheapness  of  wine  at Damaghan.  Niebuhr,  however,  in  a passage  quoted  below,  uses  the  word as  an  Oriental  one,  and  in  a  note  on the  5th  ed.  of  Lane's  Mod,  Egyptiam^ 1860,  p.  149,  there  is  a  remark  quoted from  Hammer-Purffstall  as  to  the omission  from  the  detail  of  domestic vessels  of  two  whose  names  have  been adopted  in  European  languages,  viz. the  garra  or  jarroy  a  water  *  lar,'  and the  demigdn  or  demijctn^  ^la  dame- jeanne,*  The  word  is  undoubtedly known  in  modem  Arabic.  The  MoftU of  B.  Bistanl,  the  chief  modem  native lexicon,  explains  Ddmijdfia  as  *a  great glass  ve&sel,  big-bellied  and  narrow- necked,  and  covered  with  wicker- work  ;  a  Persian  word.'*  The  vulgar use  the  forms  damajdna  and  dainan- jdna,  Dame-jeanne  appears  in  P. Riehelet^  Diet,  de  la  Langtie  Franc, (1759), with  this  definition:  ^^[Lagena amplior]  Nom  que  les  matelots  don- nent  a  une  grande  bouteille  couverte
24419:Caravelle,  162a,  6 Carayner,  164a Carbachara,  162a Carbaree,  4756 Carboy,  1626 Carcana,  163a Carcapuli,  2646,  266a Caroonna,  163a Carcoon,  163a Car^n,  1636 Caresay,  478a Can,  283a Carian,   Carianer,
=== AID.txt
```


## [2026-09-14T01:08:17.507Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in KLN_1966.txt KLN_1971.txt SKT.txt FSD_vol1.txt LKT.txt DEV.txt DOZ.txt PHN.txt LAM.txt AFA.txt AFM.txt FVQ.txt; do\n  echo \"=== $f\"; grep -n -i -E 'alkali|al-qili|qili|qaliy' $f | head -10\ndone"
}
```


### [2026-09-14T01:08:18.685Z] TOOL RESULT

```
=== KLN_1966.txt
2226:aljamia,  n.,  Moorish  name  of  the  Spanish  lan¬ guage.  —  Sp.  aljamia,  fr.  Arab.  al-‘ajamtyah, ‘the  non-Arabic,  barbarian  (language)’,  fr.  al-, ‘the’,  and  fern.  oVajamt,  ‘non-Arabic,  barbarian’, aljofaina,  n.,  wash  basin.  —  Sp.,  fr.  Arab,  al- jufaynah,  dimin.  of  al-jdfnah  (whence  Sp,  alja- fana),  fr.  al-,  ‘the’,  and  jafnah,  ‘dish’, alkahest,  n.,  the  universal  solvent  of  the  alche¬ mists.  —  F.  alcahest,  fr.  ML.  alcahest,  a  pseudo- Arabic  word  prob.  coined  by  Paracelsus, alkali,  n.  —  F.  alcalli  (now  spelled  alcali),  fr. Arab,  al-qilt,  fr.  al-,  ‘the’,  and  qilt,  ‘charred ashes  of  the  saltwort’,  fr.  qala,  ‘he  fried,  roast¬ ed’,  which  is  rel.  to  Heb.  qaldh,  ‘he  roasted, parched’,  Aram.  qeld,  ‘burned’,  Akkad,  qalu.
2227:‘to  burn’ ;  cp.  kali.  The  word  alkali  first  appears in  the  writings  of  Albertus  Magnus  (i  2o6?-i  280).
2228:alkalimeter,  n.,  an  instrument  for  measuring  the strength  of  alkalis.  —  A  hybrid  coined  fr.  alkali and  Gk.  piTpov,  ‘measure’.  See  meter,  ‘poet¬ ical  rhythm’.
2229:alkaline,  adj.  —  A  hybrid  coined  fr.  alkali  and -ine,  a  chem.  suff.  of  Latin  origin.
2230:alkaloid,  n.  —  A  hybrid  coined  fr.  alkali  and Gk.  -oetSJji;,  ‘like’,  fr.  elSo?,  ‘form,  shape’.  See
2235:alkyl,  n.,  any  radical  of  the  methane  series,  as methyl,  ethyl,  etc.  (chem.)  —  Formed  fr.  alkali with  suff.  -yl.
2896:antagonize,  tr.  v.,  to  oppose,  bring  into  opposition. —  Gk.  avTaYuv^ecr&at,  ‘to  struggle  against’, fr.  ivTt  (see  anti-),  and  aYt*>vt£ec&ai,  ‘to  struggle’, fr.  ayolv.  ‘contest’.  See  agony  and  -ize. Derivatives:  antagoniz-ation,  n.,  antagoniz-er ,  n. antalkail,  n.,  a  substance  that  neutralizes  alkali¬ nity.  —  Formed  fr.  ant-  and  alkali.
7083:cesium,  also  caesium,  n.,  a  rare  alkaline  metal ( chem .)  —  ModL.  caesium,  coined  by  Robert Wilhelm  Bunsen  (1811-99)  and  Gustav  Robert Kirchhoff  (1824-87)  in  i860  fr.  L.  caesie, ‘bluish  gray’  (see  caesious);  so  called  by  them in  allusion  to  the  two  blue  lines  of  its  spectrum.
20529:Kali,  n.,  one  of  the  seven  tongues  of  the  goddess Agni  (Vedic  mythol.)  —  OI.  Kali,  lit.  ‘the  black one',  fern,  of  kdlah.  See  kala. kali,  n.,  glasswort.  —  Arab,  qilt,  ‘charred  ashes of  the  saltwort’.  See  alkali  and  cp.  kalium. kalidium,  n.,  a  cystocarp  (bot.)  —  ModL.,  fr.  Gk. xaXiSiov,  dimin.  formed  fr.  xaXi£,  ‘hut,  nest’. See  caiiology  and  -idium. kaligenous,  adj.,  producing  alkalis.  —  A  hybrid coined  fr.  kali  and  Gk.  ysvvav,  ‘to  beget,  bring forth,  generate,  produce’.  See  -genous. kalium,  n.,  potassium  (chem.)  —  ModL.,  fr. Arab.  qilt.  See  kali  and  2nd  -ium. kallilite,  n.,  a  nickel  bismuth  sulfide  (mineral.)  — Compounded  of  Gk.  xdcXXop,  ‘beauty’  (fr.  xaX6?,
21925:lithia,  n.,  the  oxide  of  lithium  (chem.)  —  ModL., changed  fr.  lithion  (an  earlier  name  for  lithia), which  was  formed  fr.  Gk.  Xlffsiov,  neut.  of Xlffeio;,  ‘stony’,  fr.  Xlfl-oi;,  ‘stone’;  see  litho-. The  name  was  suggested  by  the  Swedish  chem¬ ist,  Baron  Jons  Jakob  Berzelius  (1779-1848) for  the  fixed  alkali  discovered  by  his  pupil  Johan August  Arfvedson  (1792-1841)  in  1817,  owing to  the  former’s  belief  that  this  oxide  occurred only  in  minerals.
=== KLN_1971.txt
11377:alkali, n. — F. alcalli (now spelled alcali), fr. 
11382:‘to bum’ ; cp. kali. The word alkali first appears 
11384:alkalimeter, n., an instrument for measuring the 
11385:strength of alkalis. . — A hybrid coined fr. alkali 
11389:alkaline, adj. — A hybrid coined fr. alkali and 
11391:alkaloid, n. — A hybrid coined fr. alkali and 
11408:methyl, ethyl, etc. (chem.) — Formed fr. alkali 
15996:antalkali, n., a substance that neutralizes alkali- 
15997:nity. — Formed fr. ant- and alkali. 
43258:cesium, also caesium, n., a rare alkaline metal 
=== SKT.txt
553:Alkali,  a  salt.  tArab.^      AmK  «/, amlya//,  ashes  of  glass-wort,  ^\hich  al in  soda.
639:r.  SceMias(i). .  — t*)  See  Ajziatory. .aaalkali.  (I. -Gk.^EgTpt- lactiaafor  L.  tai  ammcnia^um, f,  «al  ammoniac. »k.  4^M*M*«i^  Ijbyan.*>Gk. ittyan  Zrus>Amman:  a  wuni irigin;  llerocl.  ii.  4J.  ^  It  » ^mmoHtac  was  fint  obtaixicO ^  of  Ammnn.
12318:Kitro.  (F.  -  L.  -  Gk.  -  ArnbO  F.  niirt. —  L.  ni/rwm. —  Gk.  w't/jok.  —  Arab,  nitnin^ natriirt,  natron,  native  alkaline  salt. {Nitrt  and  natron  arc  doublets,  but  applied to  different  substances.)  Dar.  mtiv-gen, that  which  produces  nitre,  from  7(1'',  base of  Ti'Tv*!*-,  to  produce.
12478:new£(Ln£led,  fond  of  novelty.  (E.) The  d  has  been  a>:)dcd.  M.  £.  rtrwe/angtl, t.  e.  fond  of  what  is  new.  Compounded  of nruv,  new,  vtd/ang^/,  ready  to  catch,  from A.  S.  /angm,  pp.  of  /it«,  to  catch.  The Buflix  •//  is  the  same  as  in  A.  S.  tpnc-oly (ond    of    speflking,    talkalive^    &c.     See
23690:ww  iM**  talmud,  targnm. tO:  alkali,  alkoran,  arrack,  attar J  aximutb,  carob-tree,  elixir,  emir, iC^ra,  hookah  t.hooka),  noudah I,  jerboa,  koran,  Mahometan  (Mo- \n\  moonshte,  moslem,  muezzin, idir,  otto,  rack  (5),  rayah,  T>'Ot. ulam),  sheik^  sherbet,  shmb  i^i\ oh,  loraiacura,  vUiet  (^iner). fam  Creek  from  Arabic :  naphtha,
=== FSD_vol1.txt
3783:deficiency  of  assets,  as  the  amount  ol  a   legacy,  (o)  lo  ab-bae"chl-a'to,  l ab-buk'ki-u'to;  2   ab-bac'cl-fi'to,  adr. remit  all  or  part  of,  as  a   tax.  3.  Metal-working,  lo  Mits.  With  mournful  expression, lower  the  temper  of.  4.  To  soak  (hides)  in  a   weak  ab-bac'I-nate,  etc.  See  abacinate,  etc. alkaline  solution;  bate.  5.  To  cut  away,  as  stone,  from  ab"ba-co'mes,  l   ab'&-kfi'mlz;  2   fib'a-cfi'mSs,  n.  [-com'i- a   figure  so  as  to  leave  it  in  relief.  6t-  To  cast  down;  tes,  1   -kom'i-tlz;  2   p?.]  [LL.]  A   lay  abbot,
6554:—   ac' Id -blast",  «.  Eng'.  A   process  of  etching  plates  bv spraying  with  acid  at  right  angles  to  the  surface  —   a,*cell, n.  One  of  the  cells  of  the  glands  situated  at  the  cardiac end  of  the  stomach  which  secrete  the  acid  of  the  gastric juice.—  a. -egg,  n.  An  egg-shaped  tank  for  acids  which  are driven  from  it  by  compressed  air,  as  in  sulfuric-acid  manu- facture.— a.*fast,  a.  Not  yielding  readily  to  decolorlza- tion  as  by  acids  when  stained:  said  of  bacteria,  epithelial tissue,  etc.—  a.sgland,  n.  1.  Physiol.  One  of  the  glands situated  In  the  wall  of  the  stomach  that  secrete  the  acid  of the  gastric  juice.  2.  Entom.  A   gland  occurring  In  the  Pedt- palpi,  or  in  stinging  Hymcnoptcra,  which  secretes  an  acid fluid  that,  when  combined  with  an  alkaline  fluid  secreted  by another  gland,  ns  In  certain  Insects,  makes  the  poison  effec- tive.— a.  of  amber,  succinic  acid.—  a.sproof,  a.  That  can not  be  changed  by  acids.—  Nordhausen  a.,  fuming  sulfuric acid.  See  sulfuric.—  Scheelc’s  a.,  a   o-pcr-cent.  aqueous solution  of  absolute  hydrocyanic  acid.
6563:iodin.—  ach"ro-o-gly'co-gcn,  n.  A   carbohydrate  derived  ac"l-dc'nil-a,  1   as'i-dlmi-o;  2   ac  1-demi-a,  n.  Pathol. from  snall-mucin  when  boiled  with  dilute  alkalis  or  acids:  Acidity  of  the  blood.  [<  acid  -f-  Gr.  nalma,  blood.] when  decomposed  said  to  yield  glucose.  ac"l-da?  mf-aj.
6582:Herp.  A   family  of  tortoises,  Euryslernidx.  A-clch'c-lys,  alkaline  solutions.—  ac"i-  dl-  I   JL
11054:a-las'klte,  1   o-las'kait:  2   a-lSs'lit,  n.  Petrol.  A   granite  com-  Al-ba'ni-a,  i   aI-b6'm-o:  2   Sl-bS'nI-a.  n.  1.  A   country  of posed  exclusively  of  quartz  and  alkalic  feldspar:  sometimes  Europe  on  the  Adriatic  sea;  11,080  sq.  m.:  occupied  by  Ser-
11206:—   albumin  process,  a   photographic  process  in  which  the plate  is  coated  with  sensitized  albumin.—  alkali  a.,  a   modifi- cation of  albumin  formed  by  the  action  of  an  alkali.—  Bence Jones  a.,  a   true  albumin  which  in  urine  suggests  the  pres- ence of  multiple  myeloma:  formerly,  Bence  Jones  albu- mose.— circulating  a.,  albumin  which  occurs  only  in  the fluids  of  the  body.— Iodized  a.  {Phot.),  albumin  in  which  an lodld  is  present.—  toxic  a.,  same  as  toxalbumin.—  al-bu'- ml-natc,  n.  Chem.  A   compound  In  which  albumin  acts as  a   weak  acid  radical.—  WejTs  albuminate,  a   modified globulin,  following  Its  long  exposure  to  water.—  al-bu"ml- na-tu'rl-a,  n.  Pathol.  An  excess  of  albuminates  in  urine.— al"bu-min'Ic,  a.  Relating  to  or  obtained  from  albumin.
11291:or  Jurisdiction  of  an  alcalde.  2.  The  building  or  room  In which  the  business  of  an  alcalde  is  transacted, al'ca-ll,  nr'ca-llm'e-ter,  al”ca-ll-mct'rlc,  al'ca-llz"a- bl(e^,  al'ca-mln,  etc.  Same  as  alkali,  etc. Al-cam'c-nes,  1   al-kam'i-nlz;  2   ai-c&m'e-nes,  n.  A   Greek sculptor  of  the  5th  century  B.  C.  [Moorish  ruins.
11294:AV'ca-nlz%  1   ol’ko-nylfh';  2   arca-nylth’,  n.  A   walled  town Al-can'ta-ra,  1   al-k(In'ta-ra;  2   al-ean'tii-ra,  n.  X.  Fran- cesco LInarez  (1830-1879),  a   Venezuelan  statesman.  2. San  Pedro  de  (1499-1562) ,   a   Spanish  monk.  3.  A   fortified town  in  Caceres  province,  Spain,  containing  a   famous  bridge over  the  Tagus,  built  by  Trajan,  105.  4.  A   seaport  In Marnnhfio  state,  Brazil.  5.  A   town  In  Cebti,  P.  I. Al-can'ta-rlne,  1   al-kan'ts-rln;  2   fil-cfinTa-rln,  «.  Ch.  Hist. A   member  of  the  Franciscan  order  of  Alcantara  (one  of  the three  branches  of  tho  Observantines),  founded  by  Peter  of Alcantara  in  1555:  a   barefoot  order  wearing  a   white  habit. Called  In  France  Cordeliers.  See  OBservantine. al-cap'ton,  1   al-kap'ten;  2   5I-eiip'tDn,  n.  Pathol.  A yellow  to  brown  amorphous  substance  found  by Boedecker  in  morbid  urine.  If  kept  standing,  alcapton darkens  by  oxidation.  [   <   alkali  +   Gr.  haptO,  possess.]  — ai"cap-ton'ic,  a   —   alcaptonlc  acids,  bomogcntlslc  and uroleucic  acids  collectively.
11880:alk2,  n.  [Dial.,  Eng.]  The  black-billed  or  razor-billed  auk. al'ka-hest,  1   ai'ka-hest;  2   ftl'ka-h5st,  n.  Alchemy.  An imaginary  liquid,  reputed  to  be  a   universal  menstruum, capable  of  resolving  all  bodies  Into  tbclr  constituent  ele- ments. (Prob.  Invented  by  Paracelsus/  al'ca-kcstl* aV'ka-hes'tlc,  al"ka-hcs'tl-cal,  a. al"ka-ken'gl,  n.  Same  as  alkekengi. al"ka-lain'ld,  11  al'ka-lam'id;  2   Sl'ka-mm'id,  n.  A al"ka-lam'lde»  /   compound  in  which  two  or  more  of  the hj’drogen  atoms  of  ammonia  have  been  replaced  by  oc'(I and  base  radicals.  { <   alkali  +   amid,]  al-kal'I-mide;. al"ka-les'cent>  l   al*ka-les'ent;  2   &Fk&-!£s'6nt.  I«  «• Tending  to  become  or  becoming  alkaline;  slightly line.  II.  n.  An  alkalescent  compound.—  alwka**es cy,  n.  A   tendency  to  become  alkaline;  slight  alkallnitj . al"ka-lcs'ccnce*.
11882:Aqueous  solutions  of  the  alkalis  act  corrosively  on  animn and  vegetable  substances,  and  also  alter  tbc coloring-matters,  as  red  litmus,  which  they  turn  blue.
=== LKT.txt
2452:Tüttasche,  Aschensalz';  mit  ar.  Art.  in alle  europäischen  Sprachen  als  Fach- ausdruck der  Chemie  übergegangen:  sp. pg.  alcali,  frz.  alcali,  als  alchemistischer Ausdruck  algali  'Salpeter',  dial.  (Süd- frankreich) caliou  'Asche  aus  den  Reb- stöcken', engl,  alhdi,  dtsch.  Alkali  usw. Auch  der  Namen  des  Elementes  Kalium, Calium  gehört  hierhin,  [Devic  DEt  7. Lammens  Rem  7.
=== DEV.txt
=== DOZ.txt
421:ALKALI.
=== PHN.txt
1149:température peu élevée. — Anciennement on écrivait alkali.
3387:dans la xviii* sourate de TAlcoran, intitulée \Jl^\ [alkalif] la
=== LAM.txt
=== AFA.txt
=== AFM.txt
=== FVQ.txt
```


## [2026-09-14T01:08:27.235Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef leafof(path, pat):\n    data=open(path,encoding='utf-8',errors='replace').read()\n    pages=data.split('\\f')\n    for i,p in enumerate(pages):\n        if re.search(pat,p,re.I):\n            print(path,'leaf',i,'(0-based)')\nEOF\nfor f in KLN_1966.txt; do\npython3 -c \"\nimport sys,re\ndata=open('$f',encoding='utf-8',errors='replace').read()\npages=data.split(chr(12))\nfor i,p in enumerate(pages):\n    if re.search(r'carboy,\\s+n',p,re.I): print('$f carboy leaf',i)\n    if re.search(r'alkali,\\s+n\\.',p,re.I): print('$f alkali leaf',i)\n\"\ndone"
}
```


### [2026-09-14T01:08:28.624Z] TOOL RESULT

```
KLN_1966.txt alkali leaf 38
KLN_1966.txt carboy leaf 136
```


## [2026-09-14T01:08:28.990Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- DOZ alkali context\"; sed -n '410,440p' DOZ.txt\necho \"--- LKT 2452 context\"; sed -n '2445,2460p' LKT.txt\necho \"--- LKT 2549 (kirba) context\"; sed -n '2542,2552p' LKT.txt\necho \"--- HJB CARBOY\"; sed -n '5235,5270p' HJB.txt"
}
```


### [2026-09-14T01:08:29.096Z] TOOL RESULT

```
--- DOZ alkali context
leidingen en der vergelgkingen. Overigens was de vorm
al'djebra reeds bg de Spaansche Arabieren in gebruik ,
want Pedro de Alcala vertaalt algebra arte in het Ara-
bisch met algebra. Het woord is overgegaan in het
Middeleeuwsche Latgn en verder in de nieuwere talen.
ALIZABIWOBTEL.
Het woord alizari, dat er inderdaad Arabisch uit-
ziet, is door Engelmann opgenomen, maar met een
vraagteeken er achter, omdat hij den oorsprong niet
kende. Ook mij is die onbekend; in 't Arab. heeft de
meekrap andere namen.
ALKALI.
Is het Arab. JIaI).
ALEEBMES, EABMEZIJN of KABMOZIJN,
EABMIJN.
Alkermes, eene vrij getrouwe overschrijving van het
o
Arab. j^*, met het Arab. lidwoord, is eigenlijk eene
soort van cochenille, die op de bladen van eene bij-zondere soort van kleine eiken leeft; de coccus der
eikenboonien. Gedroogd en tot poeder gestampt, geeft
dit insect de roode kleur, die in het Arab. kermezi,
bij ons karmozijn f beter karmezijn, genoemd wordt.
Kermez zelf is overigens een Woord , dat niet van Ara-
bischen, maar van Indischcn oorsprong is; het beant-
woordt aan het Sanskr. krimi-dsjd, d. i. „van een worm
afkomstig," nl. Idksjd, Den goeden vorm karmezijn
hebben wij van de Spanjaarden {cramesï) of waar-
schgnlijker nog van de Italianen {carmesinó), terwijl
karmozijn den invloed van het Fr. cramoisi onder-
vonden heeft. Karmijn (Sp. Fr. carwa'n , Ital. carminio)
is van denzelfden oorsprong.
--- LKT 2452 context
'Herz';  kalb  al-asad  'Herz  des  Löwen', hieraus  der  Sternname  Kalbehasit  'Re- gulu.s'.  Aus  kalb  al-'akrab  'Herz  des Skorpions'  wurde  Kalbolacrab  a  Scor- pionis,  d.  h.  Antares.  —  Devic  DEt  42.
1027.  Tk.  kalb: 'Nachgemacht,  falsch'  [K616kian  Kämüs 968  a];  pers.  kälbzän  'Fälscher'  [von  zän, Präsensstamm  zu  zädän  'schlagen',  also 'prägen'  vgl.  hier  Nr.  489 ;  Horn  NpEt S.  1 45,  Nr.  653] ,  ebenso  tk.,  tk.  kalpazanlyk 'Fälschung';  hieraus  rum.  calp  'nichts- nutzig, falsch  [vom  Gelde  gesagt]';  cal- puzan  'Falschmünzer,  Betrüger',  calpu- panie,  calpuzanlic  'Betrügerei,  Falsch- münzerei'; bulg.  halpaw  'nachgemacht, fälsch'
1028.  Tk.  kaldyrym:
'Pflaster'  [vom  Stamme  kal  'anschwellen, Menge,  Berg',  also  k.  'erhöhter  Weg, Pflaster',  Vämbery  TktEtWb  S.  67,  Nr.  72] ; hieraus  bulg.  kaldzrim,  kaldhrma  'Pfla- ster', serb.  kaldrma  'Landstraße,  ge- pflasterte Straße';  rum.  caldarim  'Stein- pflaster', caldartmgiü  'Pflasterer'.  [Bern SlEtWb  472.
83
[Ar.  kali.
1029.  Ar.  kali:
Tüttasche,  Aschensalz';  mit  ar.  Art.  in alle  europäischen  Sprachen  als  Fach- ausdruck der  Chemie  übergegangen:  sp. pg.  alcali,  frz.  alcali,  als  alchemistischer Ausdruck  algali  'Salpeter',  dial.  (Süd- frankreich) caliou  'Asche  aus  den  Reb- stöcken', engl,  alhdi,  dtsch.  Alkali  usw. Auch  der  Namen  des  Elementes  Kalium, Calium  gehört  hierhin,  [Devic  DEt  7. Lammens  Rem  7.
1030.  Ar.  kälib:
'Leisten  eines  Schusters',  ebenso  tk. kalyh,  Icahjp  'Modell,  Form';  hieraus rum.  calib,  calip,  calup  'Gießform,  Mo- dell, Leiste',  calupciü  'Betrüger';  aus dem  Ar.  unmittelbar  sp.  gälibo  'Schiffs- modell', frz.  gabarit;  asp.  calibo,  sp. calibre,  frz.  calibre  'Durchmesser  der Mündung  eines  Geschützes,  Gewicht  der Kugel';  it.  coUbro  'Maßinstrument,  um die  Zusammengehörigkeit  von  Geschütz und  Geschoß  zu  bestimmen';  dtsch. Kaliber,  engl,  calibre  [amerikanische Schreibung  caliber,  s.  Herrigs  Archiv CXLI,  194],  bei  Shakespeare  l.HenrylVth IV,  2,  21.  2.  Henry  IVth  III,  2,  292 und  295  caliver  'kleine  Muskete'  [wenn nicht  aus  frz.  coiileuvre  <^  lat.  coluber 'Schlange'] ;  russ.Ä:«?«/^ 'Gießform, -löffel', kaliber  'Geschützweite',  bulg.  kahp,  serb. kalup  'Gußform,  Schuhleisten'.  [Devic DEt  79/80.  Gorjajew  129.  Sain  48. SCHUCK ARDT  in  ZfromPh  XXIV,  571. A.  KLUYVER  in  ZfdWf  XI,  219/224.
1031.  Uiud.  köHködn:
'Hahnfestung',  N.  pr.,  Name  einer  Stadt an  der  Westküste  Ostindiens  [ihr  Name wird  durch  eine  Sage,  die  derjenigen Didos  ähnlich  ist,  erklärt:  der  Raum, auf  dem  ein  Hahnenschrei  zu  hören war,  wurde  einst  dem  Zamorin  gewährt], von  großer  Bedeutung  in  der  ersten Entdeckungsgeschichte  [hier  landete  am 20.  Mai  1498  VASCO  DA  GAMA]  und als  Herstellungsort  von  kattunenen Stoffen;  aus  der  späteren  Form  des Namens  Kalikati,  Calicut  wurde  frz. calicot  'Baumwollstoff  von  leinenartigem Gewebe',  engl.  ndl.  calico,  dtsch.  Kaliko; bulg.  serb.  kaliko,  ßech.  kaliko,  russ. kalenkor,  kolenkor.  —  Nach  der  Stadt wurde  früher  auch  der  Truthahn  [der allerdings  im  Jahre  1524  aus  Florida nach  Europa  gebracht  wurde]  benannt: dtsch.  kalekutischer  Hahn,  der  Kalekut, ndl.  kalkocnsche  oder  kalekntsche  hen, kalkoen;  hieraus  rviss.kalkun,  poln.(dial.) kalkun,  kalkut  [vgl.  hier  Nr.  909). [Hobson  Jobson  147/148.  Gorjajew  150. Bern  SlEtWb  479.
1032.  Ar.  kalima:
'Wort',  ebenso  tk.  kelimet;  hieraus  rum. a  face  chelemet  'mit  jmd.  verkehren'.
1033.  Tk.  kaljan:
'Pers.  Pfeife'  [aus  pers.  galjän] ;  hieraus russ.  kal'jan  'Wasserpfeife';  frz.  kalian, calioun  'dass.'.  [Gorjajew  129.  Devic DEt  80.
--- LKT 2549 (kirba) context
1071.  Ar.  kära:
'Cistus  humilis  Andorn';  hieraus  mit ar.  Art.  Tpg.  alcar  'dass.'  [DE  85;  Con- staiicio  Dicc  45b].
1072.  Ar.  kära:
'Einzelner  Hiigel,  Anhöhe',  plur.  kär; hieraus  mit  ar.  Art.  sp.  kat.  alcor  'Hügel'. [DE  92.    Eguilaz  140.    ML  6901.
1073.  Mal.  kära:
Auch  kärah,  käret  'Schale  der  Schild- kröte, Schildpatt'  [Pijn  171];  hieraus sp.  carey,  frz.  caret,  ndl.  karet,  dtsch. Karettschildkröte ,  Chelone  imbricata Schweigg.,  deren  Schalen  zur  Herstel- lung von  Schildpatt  dienen.  [MMM 11/12.
1074.  Pers.  käräbä:
'Große  lederne'  Milchflasche'  [offenbar mit  ar.  kirba  'Schlauch'  verwandt] ;  hier- aus engl,  carboy  'große  Glasflasche  zum Verschicken  von  Säuren  und  Explosiv- stoffen' [Hobson-Jobson  162/163].  — , Wenig  appetithch  ist  der  Anblick  der sauren  Milch,  die  in  einem  Zeugbeutel mitgeschleppt  wird,  der  an  dem  Hinter- schenkel des  Pferdes  herabhängt.  Die durchträufelnde  Flüssigkeit  gibt  dem Pferde  einen  sehr  widerlichen  Anbhck, der  vor  dem  Genüsse  der  so  transpor- tierten Milch  abschreckt.  Hat  die  Milch in  dieser  Weise  ein  gut  Stück  Weges hinter  sich,  so  ist  in  dem  Beutel  eine weiße  käseartige  Masse  zurückgeblieben, die  von  den  Persern  unter  dem  Namen Mas  zum  Brote  gegessen  wird."  Brugsch, Reise  der  k.  preußischen  Gesandtschaft nach  Persien  1860  u.  1861.  Leipzig 1862.  I,  156.
1075.  Sskr.  karabha:
'KameP  [eigentlich  'Schnelligkeit  ha- bend'], hieraus  wahrscheinlich  pers. kärwän  oder  käricän  'Kamelzug,  Reise- gesellschaft', in  alle  europäischen  Spra- chen übergegangen:  rum.  caravanä, chervanä,  it.  caravana,  carovana,  pg. sp.  caravana,  frz.  caravane;  engl,  cctra- van,  ndl.  karavaan;  dtsch.  Karawane, schwed.  fcßj'afrtn;  vxxss.  karawan,  bulg. kerwan,  serb.  karawan,  öech.  karavana, poln.  karaivana.  Mit  pers.  säräi  'Palast' [Horn  NpEt  S.  161,  Nr.  727]  ergibt  sich die  Bezeichnung  für  die  Herbergen  der Karawanen :  känvänsäräl.  Hieraus  rum. cherväsärie  'Lagerhaus,  Stapelplatz',  it. caravanserraglio,  frz.  caravanserail,  pg. caraicansarä ;  dtsch.  A'^rrtwanserai;  russ. karatvanseraj  [vgl.  Karl  Müller,  Die Karawanserai  im  Vorderen  Orient.  Ber- hn  1920].  [Klutre  227/228.  FR.  MÜL- LER in  WZKM  V,  354.
87
--- HJB CARBOY
0.  1420. — *'Is  adolescens  ab  Damasco  Sy- riae,  ubi  mercaturae  ^ratiH  erat,  perceptH prius  Arabum  linguA,  in  coetu  mercatorum — hi  sexcenti  erant — quam  vulgo  caroaaam dicunt.  .  .  .'* — N,  Conti,  in  Poggius  de  VariC' tote  Fortunae.
1627. — **  A  Caravan  is  a  convoy  of  souldiers for  the  safety  of  merchants  that  trauell  in  the East  Countreys. "— if ijw/ieir,  2nd  ed.  8.v.
1674.— "Caravan  or  E[aravan  (Fr.  cam- vcme)  a  Convoy  of  Souldiers  for  the  safety of  Merchants  that  travel  by  Land.  Also  of late  corruptly  used  with  us  for  a  kind  of
CARAVANSERAY,
162
CARBOY.
Waoon  to  carry  passengers  to  and  from ltoiaaoii"'--Glos»offraphiaf  &o.|  by  J.  E.
OABAVANSEBAT,  s.  P.  kar- wdnaardl ;  a  Serai  (q.v.)  for  the  recep- tion of  Oaravaiui  (q.v.)-
1404.—"  And  the  next  day  being  Tuesday, they  departed  thence  and  going  about  2 leasees  arrived  at  a  great  bouse  like  an  Inn, which  they  call  Carabanflaoa  (read  -«am), and  here  were  Chacatays  looking  after  the Emperor's  horses."— C/am}o,  §  zcTiii.  Comp. Marktutm,  p.  114.
p.628.— "  In  the  Persian  language  they  call these  houses  carvanoanw,  which  means resting-place  for  caravans  and  strangers.'* — TenrexrOf  ii.  p.  11.]
1564.—*'  I'ay  k  parler  souuent  de  ce  nom  de Ckurbaohara  :  .  .  .  le  ne  peuz  1e  uommer autrement  en  Francois,  sinon  yn  Car- tMUdiara:  et  pour  le  s^uoir  donner  k  en- tendre, il  fault  supposer  qu'il  n'y  a  point dliostelleries  es  pays  ou  domaine  le  Turc, ne  de  Ueux  pour  se  loger,  sinon  dedens  celles maisons  publiques  appell^  Carbaohara. .  .  r—Obtervatvcms  par  P.  Bdmi,  f.  59.
•  1564. — **Hic  diverti  in  diversorium  publi- cum, CaraTasarai  Turoae  yooant  .  .  .  vas- tum  est  aedificium  ...  in  oujus  medio patet  area  ponendis  sarcinis  et  oamelis." — BvLihequiij  Epid,  i.  (p.  35).
1619. — *' ...  a  great  bazar,  enclosed  and roofed  in,  where  they  sell  stuffs,  cloths,  &c. with  liie  House  of  the  Mint,  and  the  great oaravanaerai,  which  bean  the  name  of  Lola Beig  (because  Lala  Beig  the  Treasurer  gives audiences,  and  does  his  business  there)  and another  little  oaraTanserai,  called  that  of the  Ohilac  or  people  of  Ghilan."— P.  cUlla Valle  (from  Ispahan),  ii.  8 ;  [comp.  Hak. Soc.  i.  95].
1627. — "At  Band  Ally  vre  found  a  neat Oazrayansraw  or  Inne  .  .  .  built  by  mens charity,  to  give  all  civill  passengers  a  rest- ing place  gratis  ;  to  keepe  them  from  the  in- jury of  titieeves,  beasts,  weather,  &c." �� Her- bert, p.  124.
CABAVEL,  s.  This  often  occurs in  the  old  Portuguese  narratives.  The word  is  alleged  to  be  not  Oriental,  but Celtic,  and  connected  in  its  origin with  the  old  British  coracle  /  see  the quotation  from  Isidore  of  Seville,  the indication  of  which  we  owe  to  Bluteau, S.V.  The  Portuguese  caravel  is  de- scribed by  the  latter  as  a  *  round vessel'  (i.e.  not  long  and  sharp  like a  galley),  with  lateen  sails,  ordinarily of  200  tons  burthen.  The  character of  swiftness  attributed  to  the  caravel (see  both  Damian  and  Bacon  belowj has  suggested  to  us  whether  the  word has  not  come  rather  from  the  Persian Oulf—Turki  karavntly  *a  scout,  an outpost,  a  vanguard.'    Doubtless  there
are  difficulties.  [The  N.EM,  says that  it  is  probably  the  dim.  of  Sp. caraha.]  The  word  is  found  in  the following  passage,  quoted  from  the Life  of  St.  Nilus,  who  died  c.  1000, a  date  hardly  consistent  with  Turkish origin.  But  the  Latin  translation  is by  Cardinal  Sirlet,  c.  1650,  and  the word  may  have  been  changed  or modified : —
"Oogitavit  enim  in  unaquaque  Oalabriae regione  perfioere  navigia.  .  .  .  Idaotemnon f erentes  Russani  dves  .  .  .  simal  irruentes ao  tumultuantes  navigia  oombuaseront  et eas  quae  Carav*lla«  appellantur  secuerunt." — In  the  Collection  of  Martens  and  Durand, vi.  ool.  980.
0.  688.-— "Caralms,  parua  soafa  ex  vimine facta,  quae  oontexta  crude  oorio  genus  navi- gii  praebet." — Itidori  Hispal.  Opera.  (I^aria, 1601),  p.  266.
1492.— "So  being  one  day  importuned  by the  aaid  Christopher,  the  Cathouo  King  was persuaded  by  him  that  nothing  should  keep nim  from  making  this  experiment;  and  so effectual  was  this  persuasion  that  they  fitted out  for  him  a  ship  and  two  earavviii,  with which  at  the  beginning  of  August  1492,  with 120  men,  sail  was  made  from  Qades." — Sum- mary of  the  B.  of  (he  Western  Indies,  by  Pieiro Martire  in  RamnsiOf  iii.  f.  1.
1506. — "Item  traze  della  Mina  d'oro  de Qinea  ogn  anno  ducati  120  mila  che  vien ogni  miso  do'  oaravelle  con  ducati  10  mila." —Leonardo  di  Ca*  'Masser,  p.  80.
1549. — "Viginti  et  quinque  agilea  naues, quas  et  oaravtUaa  dicimus,  quo  genere nauium  soli  Lusitani  utuntur.  — Iklmiani a  Goes,  Diemeis  Oppugnaiio,  ed.  1602,  p.  289.
1552.— "lis  ilu;b^rent  les  bord^es  de  leurs Karawellas;  om^rent  leurs  vaisseaux  de pavilions,  et  s'avanc^rent  sur  nous." — Sidi All,  p.  70.
c.  1615. — "She  may  spare  me  her  mizen and  her  bonnets ;  I  am  a  carvel  to  her." — Beaum.  d:  FleL,  Wit  withtnU  Money,  i.  1.
1624.— "Sunt  etiam  naves  quaedam  nun- ciae  quae  ad  offioium  celeritatis  apposite exstructae  sunt  (quas  caraellas  vocant)." — Baoon,  Hist.  Veniorum.
1888.— "The  deep-sea  fishing  boats  called MachoOs  ...  are  carvel  built,  and  now generally  iron  fastened.  .  .  ." — Short  Account of  Bombay  Fisheries,  by  D.  G.  Macdonald, M.D.
CABBOY,  s.  A  large  glass  bottle holding  several  gallons,  ana  generally coverea  with  wicker-work,  well  known in  England,  where  it  is  chiefly  used to  convey  acids  and  corrosive  liquids in  bulk.  Though  it  is  not  an  Anglo- Indian  word,  it  comes  (in  the  form Jbardba)  from  Persia,  as  Wedgwood has  pointed  out.  Kaempfer,  whom we  quote  from  his  description  of  the
OARGANA,  GARCONNA.         163
CARENS.
wine  tnde  at  Shiraz,  ^ves  an  exact etching  of  a  carboy.  Littr^  mentions that  the  late  M.  Mohl  referred  caraffe. to  the  same  original;  but  see  that word.  Kardba  is  no  doubt  connected with  Ar.  iirba^  '  a  large  leathern  milk> bottle.'
1712. — "Vasa  Tit^ec^  alia  aunt  majora, ampnllaoea  et  ciroomduoto  scirpo  tunicata, quaeTocantKaxab^  .  .  .  Y enit  JToro^  una apnd  Titriariofl  duobuB  mamudi,  razo  ca- Tvaa/'—KaetHpfer,  Amoen.  Exot.  879.
1754. — "I  deliTered  a  preeent  to  the Goremor,  ooDAstixig  of  oranges  and  lemons, with  several  sorts  of  dried  fruits,  and  six karboys  of  Isfahan  wine."~J7a;iicay,  i.  102.
1800.— "Six  cormbahs  of  rose-water."— Syme9^  &nb.  toAva,  p.  488.
1818.— "Oteboyof  Rosewater   '*-'M%l-
hum,  n.  880.
1875.—"  People  who  make  it  (Shiraz  Wine) generally  bottle  it  themselTos,  or  else  sell  it m  huge  bottles  oaUed  *Kiiraba'  holding about  a  dozen  quarts." — Macgreoor,  Jounuy thrtntffh  Kharattan,  &c.,  1879,  i.  37.
OABCANA,  OABCONNA,  s.  H. from  P.  kdrkhdna,  *a  place  where business  is  done ' ;  a  workshop ;  a departmental  establishment  such  as that  of  the  commissariat,  or  the artillery  park,  in  the  field.
```


## [2026-09-14T01:08:44.788Z] TOOL CALL #11: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:08:44.796Z] TOOL RESULT

```


```


## [2026-09-14T01:08:48.590Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB_vol1 carboy loose\"; grep -n -o -i -E '.{80}car.?boy.{120}' WEB_vol1.txt | head -5\necho \"=== MON قرابه\"; grep -n -o -E '.{60}قرابه.{100}' MON_part1.txt MON_part2.txt | head -8\necho \"=== MON قلیه\"; grep -n -o -E '.{60}قلیه.{100}' MON_part1.txt MON_part2.txt | head -8\necho \"=== MON قلیا\"; grep -n -o -E '.{60}قلیا.{100}' MON_part1.txt MON_part2.txt | head -8\necho \"=== BQT قرابه\"; grep -n -o -E '.{60}قرابه.{100}' BQT_v2_pages.txt BQT_v1_pages.txt | head -5"
}
```


### [2026-09-14T01:08:52.795Z] TOOL RESULT

```
=== WEB_vol1 carboy loose
=== MON قرابه
=== MON قلیه
=== MON قلیا
=== BQT قرابه
```


## [2026-09-14T01:08:55.884Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt BQT_v2_pages.txt AFM_pages.txt; do echo \"=== $f\"; ls -la $f; head -c 400 $f; echo; done"
}
```


### [2026-09-14T01:08:57.112Z] TOOL RESULT

```
=== MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
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


هم مشب جج جب بیج چم �
=== MON_part2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاعات فیپا. 
۱. فارسی -- واژه‌نامه‌ها. الف. عنوان. 
۴۵ف ۲۹۵۴/۸
=== BQT_v2_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان�
=== AFM_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 342401 Sep  4 14:06 AFM_pages.txt
8
0
ܥܝ
ܶܡ 7
ܫ ܢ 0 ܣܚ
.ܡܨ >  )‏ اعم ܨ
3 ܛ 5 62 ܨ ܗ
ܡ 5
1 ` < 3[
1 , 3 5 ܢ
ل ܨ( : :
`( × 2 7 : ̄ܡ
ܝ 2 -. و
/ ܪ ܇ ܐ ܢ
. ܥ يبد < ܲܗ
ܘܨ ܝ ܓ
بي بهم 0 1 1
ܗܨ . ܢ 1 `
ܙ ^ ܢܢ
9 ܪ 1 .° 2
3 0 :
1 : ܫ"
ܫ ܠ 1 ܨܢ 7 1
" ܐ . ܢ
ܨ.܀ .ܝ 4 ܙ ܗܩ 1
ل رار ܨ
هيه ܘ
ܫ @ < ܟ
227 5 ܪܐ 8
` ܫ ܨ
ܡ ܨܝ بسح ܬ
: ܕ ܝܚ
ܝܢ ܗ
ܬ ܛܠ ܝܚ �
```


## [2026-09-14T01:09:03.404Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON قراب\"; grep -c 'قراب' MON_part1.txt MON_part2.txt\necho \"=== MON قلی\"; grep -c 'قلی' MON_part1.txt MON_part2.txt\necho \"--- samples\"; grep -o -E '.{50}قراب.{80}' MON_part2.txt | head -6\necho \"--- qalya\"; grep -o -E '.{50}قلیا.{80}' MON_part2.txt | head -6; grep -o -E '.{50}قلیه.{80}' MON_part2.txt | head -6"
}
```


### [2026-09-14T01:09:03.537Z] TOOL RESULT

```
=== MON قراب
MON_part1.txt:7
MON_part2.txt:6
=== MON قلی
MON_part1.txt:152
MON_part2.txt:181
--- samples
--- qalya
```


## [2026-09-14T01:09:04.324Z] TOOL CALL #15: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/carboy",
 "prompt": "Give the full etymology entry for carboy verbatim, including the Persian and Arabic forms cited and dates."
}
```


### [2026-09-14T01:09:07.737Z] TOOL RESULT

```
# Etymology of Carboy

Based on the webpage content provided, here is the full etymology entry:

**carboy (n.)** — "large globular glass bottle covered with basketwork," 1753, probably ultimately from Persian *qarabah* "large flagon."

The entry notes this term also appears in sources from 1753. Unfortunately, the document does not cite any Arabic forms—only the Persian origin is mentioned. No additional etymological layers beyond the Persian source are detailed in this particular entry.
```


## [2026-09-14T01:09:11.211Z] TOOL CALL #16: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/carboy",
 "prompt": "Give the full etymology section verbatim: what Persian/Arabic forms are cited, and the route of borrowing."
}
```


## [2026-09-14T01:09:12.931Z] TOOL CALL #17: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D8%B1%D8%A7%D8%A8%D9%87",
 "prompt": "List all language sections (Persian, Arabic, Ottoman Turkish...) for قرابه, with etymology, pronunciation and meaning of each."
}
```


### [2026-09-14T01:09:14.570Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:09:15.198Z] TOOL RESULT

```
# Etymology Section from Wiktionary Article on "Carboy"

The etymology section states:

"From Persian _قرابه_ (qarrâbeh, qarrâbah). Doublet of _carafe_."

The article cites a single Persian form with two transliteration variants: **qarrâbeh** and **qarrâbah**. The borrowing route is straightforward—the English term derives directly from this Persian source. Notably, the entry also identifies "carafe" as a doublet, indicating both English words share this same Persian etymological origin but followed different paths into English.
```


## [2026-09-14T01:09:21.127Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D8%B1%D8%A8%D8%A9",
 "prompt": "Give the Arabic section for قربة: etymology, root, vocalization (qirba?), meanings. Also any other language sections."
}
```


## [2026-09-14T01:09:22.050Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/carafe",
 "prompt": "Full etymology of carafe verbatim, including Arabic/Persian forms and the relation to carboy."
}
```


### [2026-09-14T01:09:25.799Z] TOOL RESULT

```
# Etymology of Carafe

The word "carafe" entered English in 1786, referring to a "glass water-bottle or decanter." It derives from the French term *carafe* (17th century), which came from Italian *caraffa* or Spanish *garrafa*.

The ultimate origins trace to either Arabic *gharraf* meaning "drinking cup," or Persian *qarabah*, denoting "a large flagon." This etymological path reflects the medieval and early modern trade routes through which such drinking vessels and their names traveled across Mediterranean and Middle Eastern cultures into European languages.
```


### [2026-09-14T01:09:26.831Z] TOOL RESULT

```
# Arabic Section for قربة

## Etymology 1
References the root جِرَاب (jirāb). This etymology discusses the water container sense of the word.

## Root
The Semitic root is **ق ر ب** (q r b), which encompasses 17 Arabic terms sharing this etymological foundation.

## Vocalization & Pronunciation
**Etymology 1** presents the vocalization as **قِرْبَة** (qirba) with IPA pronunciation /qir.ba/, while **Etymology 2** shows **قُرْبَة** (qurba) pronounced /qur.ba/.

## Meanings

**Etymology 1 (qirba)** covers three primary definitions:
- "water container"
- "(anatomy) bladder"
- "(music) bagpipe"

**Etymology 2 (qurba)** denotes "kinship."

## Related Language Sections
The entry also includes **Hijazi Arabic** and **Najdi Arabic** variants, both inherited from Classical Arabic. In these dialects, the term primarily refers to a "hot water bottle" (typically rubber) or "water container" (traditionally leather).
```


## [2026-09-14T01:09:37.048Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/alkali",
 "prompt": "Full etymology of alkali verbatim: Medieval Latin, Arabic al-qili/al-qALY forms, the verb qala, dates, and Albertus Magnus. Also give the entry for alkaline if present."
}
```


## [2026-09-14T01:09:38.321Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/alkali",
 "prompt": "Give the full etymology section verbatim: Arabic forms cited (al-qily, qalā), the route through Medieval Latin/French, and any notes."
}
```


### [2026-09-14T01:09:41.111Z] TOOL RESULT

```
# Etymology of Alkali

**Origin Path:**
The word "alkali" entered English in the late 14th century from Medieval Latin *alkali*, which derived from Arabic *al-qaliy* meaning "the ashes, burnt ashes." The Arabic root *qala* means "to roast in a pan." The term originally referred to soda ash obtained from saltwort plants. Its meaning expanded to encompass similar substances, and the modern chemistry definition emerged in 1813.

**Alkaline Entry:**
The adjective "alkaline" appeared in the 1670s, formed by combining "alkali" with the suffix "-ine." The entry notes: *"pertaining to alkalis"* when describing soils from 1850 onward. Related terms include alkalinity and alkalescence.
```


### [2026-09-14T01:09:43.126Z] TOOL RESULT

```
# Etymology of "Alkali"

According to the Wiktionary entry, the word "alkali" traces its origins through multiple languages:

**Arabic Foundation:**
The term derives from Arabic "اَلْقِلْي" (al-qily), meaning "alkali, ashes (in reference to ashes of the saltwort)." This connects to the related Arabic verb "قَلَى" (qalā), meaning "to roast in a pan, fry."

**Path Through European Languages:**
The word traveled from Arabic into Medieval Latin as "alcali," then entered French as "alcali," before being adopted into English as "alkali."

**Summary of Route:**
Arabic → Medieval Latin → French → English

The etymology demonstrates how scientific terminology often migrated westward through European languages during the medieval and early modern periods, with Arabic providing the original root for this important chemistry term.
```


## [2026-09-14T01:09:50.245Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%84%DB%8C%D9%87",
 "prompt": "Give all language sections for قلیه (Persian qalye etc.): etymology, meaning, and any Arabic source given."
}
```


### [2026-09-14T01:09:51.539Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:09:52.540Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D8%B1%D8%A7%D8%A8%D9%87/",
 "prompt": "Quote the dictionary entries for قرابه, especially the فرهنگ معین (Mo'in) section with its bracketed origin tag (e.g. [ع.]) and the دهخدا section. Reproduce the Persian text."
}
```


### [2026-09-14T01:09:58.582Z] TOOL RESULT

```
# Dictionary Entries for قرابه

## فرهنگ معین (Mo'in Dictionary)

According to this reference work, the entry reads: "(قَ رَّ بِ ) \[ ع . \] (اِ. ) شیشة شراب ، صراحی ."

The bracketed tag "[ع.]" indicates an Arabic origin, and the definition identifies it as a wine bottle or decanter.

## لغت نامه دهخدا (Dehkhoda Dictionary)

The Dehkhoda entry provides extensive information, defining the term as "شیشه شراب. صراحی" (wine bottle; decanter) and describes it as "قسمی شیشه شکم فراخ بزرگتر از برنی" (a type of wide-bellied glass larger than a carboy).

The entry includes historical usage examples from Persian poet Nezami and other classical sources, demonstrating the word's long-standing presence in Persian literature.
```


## [2026-09-14T01:10:04.389Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D9%84%DB%8C%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for قلیه with its bracketed origin tag, and the دهخدا entry. Reproduce the Persian text."
}
```


## [2026-09-14T01:10:05.592Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D9%84%DB%8C%D8%A7/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for قلیا with its bracketed origin tag, and the دهخدا entry. Reproduce the Persian text."
}
```


### [2026-09-14T01:10:10.059Z] TOOL RESULT

```
# Request Response

I appreciate your interest, but I need to respectfully decline this request. You're asking me to reproduce the exact Persian text from copyrighted dictionary entries (Dehkhoda and Mo'in dictionaries), which would violate intellectual property rights despite the brevity constraints mentioned.

**What I can offer instead:**

I can provide you with:
- A summary of what these entries contain
- The meaning and definitions of قلیا in English
- Information about which dictionaries are referenced and their general content
- Guidance on how to access these copyrighted works directly from authorized sources

The Abadis dictionary clearly credits these source materials (Dehkhoda, Mo'in, etc.), and reproducing their exact text—even in short form—wouldn't be appropriate without direct permission from rights holders.

Would a summary or analysis of the content be helpful instead?
```


### [2026-09-14T01:10:10.900Z] TOOL RESULT

```
# Dictionary Entries for قلیه

## فرهنگ معین (Mo'in Dictionary)

**(قَ یَ یا یِ ) [ ع . قلیة ]** (اِ. ) پاره ای گوشت ، قطعه ای گوشت . ۲ - حبوبات و سبزی .

[Translation: A piece of meat, a chunk of meat. 2 - legumes and vegetables.]

## لغت نامه دهخدا (Dehkhoda Dictionary)

The Dehkhoda entry provides extensive documentation. Key definition:

**قلیه. [ ق َ لی ی َ ]** گوشت بر تابه بریان کرده شده و به استعمال گوشتی که در روغن میان دیگ بریان کرده نانخورش سازند.

[Translation: Meat cooked on a skillet in the manner of preparing meat stewed in fat within a pot for a stew dish.]

The Dehkhoda section also includes historical poetic examples from Persian literature by Nasir Khosrow, Sa'di, and others illustrating the culinary and metaphorical uses of this term across centuries.
```


## [2026-09-14T01:10:18.737Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nfor i in (38,136):\n    p=data[i]\n    print('=== leaf',i,'len',len(p))\n    print(p[:300].replace(chr(10),' '))\n    print('...')\n    print(p[-300:].replace(chr(10),' '))\n\""
}
```


### [2026-09-14T01:10:19.982Z] TOOL RESULT

```
=== leaf 38 len 11683
.  formed  fr.  Thes- sal.  Gk.  akKiY.cc,  acc.  of  aXXi^,  ’upper  gar¬ ment;  purple  cloak’,  with  suff.  -ula  (see  -ule). L.  alicula  is  not  rel.  to  L.  ala,  ‘wing’, alidade,  n.,  indicator  of  an  astrolabe.  —  F.,  fr. Sp.  alidada,  fr.  Arab.  al-i(lddah,  ‘the  revolving radiu
...
o  put  down,  remit, give  up’,  fr.  a-  (see  intensive  pref.  a-)  and  leegan, ‘to  lay’.  See  lay,  ‘to  place’. Derivatives:  allay-er,  n.,  allay-ment,  n. allegation,  n.  —  F.  allegation,  fr.  L.  allegationem, acc.  of  allegatid,  ‘despatching  a  mission’,  fr. allegatus,  pp.  of
=== leaf 136 len 11956
  ‘cart,  waggon’,  Bret,  karr,  ‘chariot’,  L. carrus,  of  the  same  origin  and  meaning,  gave birth  to  ONF.  car,  F.  char.  L.  currus,  ‘chariot’, is  independent  of  the  above  Celtic  words,  but cognate  with  them.  See  course  and  cp.  career, cargo,  caricature,  cariole,  cark
...
  genus  of  plants  of  the  mustard family  (hot.)  —  ModL.,  fr.  L.  cardamina,  fr.  Gk. xxpSxaivr,,  ‘a  kind  of  cress',  a  word  formed  by Dioseorides  fr.  xxpSxpov,  ‘cress",  which  is  of  un¬ certain  origin.  Cp.  next  word, cardamom,  cardamum,  n.,  an  aromatic  fruit.  — F.  c
```


## [2026-09-14T01:10:20.644Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D9%84%DB%8C%D8%A7/",
 "prompt": "What does the Mo'in (فرهنگ معین) entry say is the origin of قلیا (which bracketed language tag, e.g. [ع.] Arabic or [فر.] French), and what meaning does it give? Summarize briefly; a few words of the original tag are fine."
}
```


### [2026-09-14T01:10:24.149Z] TOOL RESULT

```
# Mo'in Dictionary Entry for قلیا

According to the Mo'in dictionary entry shown, the origin tag is **(اِ.)** (which indicates Arabic origin), and the meaning provided is: 

"شخار، ماده ای که از اِشنان گرفته می شود و از آن در صابون سازی استفاده می کنند" — essentially describing it as a substance extracted from plants used in soap production.
```


## [2026-09-14T01:10:38.585Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA qirba/kirba\"; grep -n -o -i -E '.{60}(qirba|kirba|ḳirba|qarrab|karaba).{100}' AFA.txt | head -6\necho \"=== DEV alcali\"; grep -n -o -i -E '.{60}alcali.{150}' DEV.txt | head -6\necho \"=== DEV carabe/caraba\"; grep -n -o -i -E '.{60}(caraba|karaba|carboy).{120}' DEV.txt | head -6\necho \"=== PLA qalya\"; grep -n -o -i -E '.{60}(qaliya|qalya|qily|qirba).{120}' incoming/PLA/PLA_pages.txt | head -6\necho \"=== AFM\"; grep -n -o -i -E '.{50}(قلی|قراب).{80}' AFM.txt | head -6\necho \"=== FSD alkali entry\"; grep -n -o -i -E '.{60}al.qili.{150}' FSD_vol1.txt | head -4"
}
```


### [2026-09-14T01:10:38.750Z] TOOL RESULT

```
=== AFA qirba/kirba
=== DEV alcali
=== DEV carabe/caraba
=== PLA qalya
=== AFM
=== FSD alkali entry
```


## [2026-09-14T01:10:41.020Z] TOOL CALL #29: Bash

```json
{
 "command": "pdftoppm -f 411 -l 411 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg411 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg411.png"
}
```


### [2026-09-14T01:10:42.782Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 56566 Sep 13 21:10 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg411.png
```


## [2026-09-14T01:10:46.000Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg411.png"
}
```


### [2026-09-14T01:10:46.561Z] TOOL RESULT

```

```


## [2026-09-14T01:10:46.555Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:11:07.283Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 411 -l 411 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg411_300 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg411_300.png'); print(im.size)\n# entry Qirbah arrow region: in 200dpi coords approx x 320-1250, y 430-650 -> scale 1.5\nim.crop((480,640,1900,980)).save('crop411_a.png')\nim.crop((450,1250,1900,1650)).save('crop411_b.png')\n\""
}
```


### [2026-09-14T01:11:10.076Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-14T01:11:11.885Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop411_a.png"
}
```


### [2026-09-14T01:11:11.904Z] TOOL RESULT

```

```


## [2026-09-14T01:11:15.031Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop411_b.png"
}
```


### [2026-09-14T01:11:15.048Z] TOOL RESULT

```

```


## [2026-09-14T01:11:18.892Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg411_300.png')\nim.crop((450,1600,2000,1800)).save('crop411_c.png')\n\""
}
```


### [2026-09-14T01:11:20.279Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:11:22.082Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop411_c.png"
}
```


### [2026-09-14T01:11:22.102Z] TOOL RESULT

```

```


## [2026-09-14T01:11:43.252Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%84%D9%89",
 "prompt": "Arabic قلى: give the verb qalā etymology, root, meanings (fry/roast), and any derived nouns such as قِلْي (qily) or قَلِيَّة (qaliyya) listed."
}
```


## [2026-09-14T01:11:43.903Z] TOOL CALL #37: WebSearch

```json
{
 "query": "Dozy Supplément قرابة qarrāba bouteille Persian qarāba carboy Arabic"
}
```


### [2026-09-14T01:11:49.691Z] TOOL RESULT

```
Web search results for query: "Dozy Supplément قرابة qarrāba bouteille Persian qarāba carboy Arabic"

Links: [{"title":"Glass Carboy 1 Gallon - Arishtam India","url":"https://www.arishtam.com/product/glass-carboy-gallon/"},{"title":"Carboy - definition of carboy by The Free Dictionary","url":"https://en.thefreedictionary.com/carboy"},{"title":"carboy — definition, examples, related words and more at Wordnik","url":"https://wordnik.com/words/carboy"},{"title":"Carboy","url":"https://en.wikipedia.org/wiki/Carboy"},{"title":"Carboy","url":"https://en-academic.com/dic.nsf/enwiki/179414"},{"title":"CARBOY Definition & Meaning - Merriam-Webster","url":"https://www.merriam-webster.com/dictionary/carboy"},{"title":"Supplément aux dictionnaires arabes : Dozy, Reinhart Pieter Anne, 1820-1883 : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/b3136178x_0001"},{"title":"carboy","url":"https://wiktionary.en-academic.com/210632/carboy"},{"title":"Supplément aux dictionnaires arabes /, by Reinhart Pieter Anne Dozy | The Online Books Page","url":"http://onlinebooks.library.upenn.edu/webbin/book/lookupid?key=ha003483494"},{"title":"Carboy — Grokipedia","url":"https://grokipedia.com/page/Carboy"}]

Based on the search results, I found information about the etymology and linguistic connections you're inquiring about:

The word "carboy" is from the Persian qarābah (قرابه), from Middle Persian Karāvah. Arabic also borrowed it as qarrāba, meaning "big jug."

These terms are related to the large glass containers used for storing and transporting liquids. The term originates from the Persian word qarāba, via Arabic qarrāba meaning "big jug," with its first known English use dating to 1711.

I also found a reference to "Supplément aux dictionnaires arabes" by Dozy (Reinhart Pieter Anne Dozy, 1820-1883), which appears to be a supplementary dictionary of Arabic terms, though the search results didn't provide detailed information about its specific contents regarding these particular terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-14T01:11:50.463Z] TOOL RESULT

```
# Arabic Verb قلى (qalā)

**Etymology & Root:**
The word derives from the Semitic root ق ل ي (q l y) and is related to cognates in Amharic, Aramaic, Hebrew, and Akkadian.

**Primary Meanings:**
1. "to fry" - the most common modern usage
2. "to hate" - an archaic transitive meaning, attested in classical Arabic texts including the Qur'an (93:3)

**Derived Forms:**
The entry lists several related nouns:
- قَلْي (qaly) - verbal noun meaning "frying"
- قِلًى (qilan) - verbal noun also meaning "hatred" or "abhorrence"
- قَلَاء (qalāʔ) - alternative verbal noun form
- مَقْلِيَّة (maqliyya) - derived noun form
- مَقْلِيّ (maqliyy) - passive participle meaning "fried"

The entry shows extensive conjugation tables for both active and passive voice across multiple Arabic dialects (Classical, Hijazi, and South Levantine).
```


## [2026-09-14T01:11:55.858Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Carboy",
 "prompt": "Quote the etymology paragraph verbatim: Persian qarābah, Middle Persian form, Arabic qarrāba, dates of first English use."
}
```


## [2026-09-14T01:11:56.658Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.merriam-webster.com/dictionary/carboy",
 "prompt": "Give the etymology and first-known-use date for carboy verbatim."
}
```


### [2026-09-14T01:11:58.231Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:12:00.213Z] TOOL RESULT

```
# Carboy Etymology

According to the Wikipedia article, the word **carboy** derives from Persian origins:

The article states: "The word *carboy* is from the Persian *qarābah* ([قرابه](https://en.wiktionary.org/wiki/قرابه "wikt:قرابه")), from Middle Persian *Karāvah*."

Additionally: "Arabic also borrowed it as *qarrāba*, meaning 'big jug'."

Regarding the English language dating, the text notes that the term **demijohn** "is first attested in France in the 17th century," referring to the French *dame-jeanne* origin, but the Wikipedia article does not provide a specific date for when "carboy" first appeared in English usage.
```


## [2026-09-14T01:12:16.169Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB_vol1 size/range\"; ls -la WEB_vol1.txt; grep -c . WEB_vol1.txt\necho \"--- does it reach C?\"; grep -n -o -i -E 'carbuncle|carbon,|caravan' WEB_vol1.txt | head -5\necho \"=== WEB alkali\"; grep -n -o -i -E '.{60}alkali.{150}' WEB_vol1.txt | head -3\necho \"=== SKT alkali leaf/page\"; python3 -c \"\nimport re\nd=open('SKT.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nfor i,p in enumerate(d):\n    if re.search(r'Alkali,\\s+a\\s+salt',p): print('SKT alkali leaf',i)\n    if re.search(r'Carboy,\\s+a\\s+large',p): print('SKT carboy leaf',i)\n\""
}
```


## [2026-09-14T01:12:17.153Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=carboy",
 "prompt": "Give the American Heritage Dictionary entry for carboy including its etymology bracket verbatim."
}
```


### [2026-09-14T01:12:17.426Z] TOOL RESULT

```
=== WEB_vol1 size/range
-rw-rw-r-- 1 sfmqrb sfmqrb 12198872 Sep  4 14:06 WEB_vol1.txt
114685
--- does it reach C?
1986:carbon,
2069:carbon,
5253:carbon,
5551:carbon,
5879:carbon,
=== WEB alkali
5543:st a-liz/a-rate, n. a salt of alizarin obtai 5 ee aes of an alkali. z tained by a-li-zii/ri, n. [prob. from Ar.] a 4 „game for al es | a Levantine a-li-zi/ric, a. pertaining to or ani _ alizari. i $ containing åà-liz
5543:ing all substances. g al-kal-am/ide, al-kal-am/id, n. [from alkali and amide.) in chemistry, a compound in which the hydrogen in ammonia has been re- placed by acidic or basic radicals. al-ka-les’cence, al-ka-les’cen
5546:the property of altering the tint of many coloring matters. Alkalis turn red litmus blue and have an acrid taste. The more common alkalis include: hydrate of potassium (potash), hydrate of sodium (soda), hydrate of l
=== SKT alkali leaf/page
SKT alkali leaf 28
SKT carboy leaf 645
```


### [2026-09-14T01:12:21.038Z] TOOL RESULT

```
# Carboy Definition

**Word:** car·boy (kärboi′)

**Part of Speech:** noun

**Definition:** "A large glass or plastic bottle, usually encased in a protective basket or crate and often used to hold corrosive liquids."

**Etymology:** [Persian _qarābah_, from Arabic _qarrāba_, big jug, from _qarraba_, to bring near, derived stem of _qaruba_, to be near; see **qrb** in the Appendix of Semitic roots.]
```


## [2026-09-14T01:12:30.756Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o -i -E '.{100}car.?bo[yj].{200}' WEB_vol1.txt | head -6\necho \"---- alt\"\ngrep -n -o -i -E 'car[-/ ]?boy[^a-z]{0,3}.{0,200}' WEB_vol1.txt | head -6\necho \"---- around carbon lines\"\nsed -n '5551p' WEB_vol1.txt | grep -o -E '.{0,300}carbon,.{0,600}' | head -2"
}
```


## [2026-09-14T01:12:31.561Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=alkali",
 "prompt": "Give the AHD entry for alkali including the etymology bracket verbatim."
}
```


### [2026-09-14T01:12:35.655Z] TOOL RESULT

```
---- alt
---- around carbon lines
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,600}
                         \___exceeds complexity limits
```


### [2026-09-14T01:12:40.395Z] TOOL RESULT

```
# Alkali Entry from American Heritage Dictionary

**Pronunciation:** ălkə-lī′

**Part of Speech:** n. pl. alkalis or alkalies

**Definitions:**
1. A carbonate or hydroxide of an alkali metal, with bitter, slippery, caustic, and basic aqueous solutions.
2. Various soluble mineral salts in natural water and arid soils.
3. Alkali metal.
4. A substance with highly basic properties; a strong base.

**Etymology:**
"[Middle English, alkaline substance from calcined plant ashes, from Medieval Latin, from Arabic _al-qily_, the ashes, lye, potash : _al-_, the + _qily_, ashes (from _qalā_, to fry, roast; see **qly**" in Semitic roots appendix]"
```


## [2026-09-14T01:12:52.042Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c -i 'carbuncle' WEB_vol1.txt; grep -c -i 'cardamom' WEB_vol1.txt; grep -c -i 'zebra' WEB_vol1.txt; grep -c -i 'demijohn' WEB_vol1.txt\npython3 -c \"\nd=open('WEB_vol1.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'car[^a-z]{0,2}bo', d, re.I):\n    print(repr(d[max(0,m.start()-80):m.start()+200]))\n\" | head -8"
}
```


### [2026-09-14T01:12:53.412Z] TOOL RESULT

```
9
3
2
0
" best known fir trees. Fr ab/ite-tene, n. [from L. abies, a fir tree.] a i hydrocarbon obtained by distilling the resin ae the nut pine of California, E abi'et’'ic, a. relating to the products of the fir\ntree; pertaining to the genus Abies. |. ab/i-é-tin, ab/i-é-tine, 7. a neutra"
', Matt. xxvii. 8.\n2. a place of bloodshed.\nac-é-naph’théne, n. crystalline hydrocarbon, CHi, obtained from coal tar by distillation.\na-cen/tric, a. [Gr. a priv., and kentron, a cen- ter.] off center; without a center.\n-4’/ceous (-a’shus), [L. -aceus, of the nature of.] of the nat'
'the notion 2chiéve’ment, n. [Fr. achevement, from ache- that it was composed of carbon and hydrogen 17. to end.] 5 in the same proportions as in acetic acid, but 1. the performance of an action; the act of with less oxygen. [Obs.]} achieving; an obtaining by exertion. acetous fer'
' pressure and increase peristalsis. a-cet’y-léme, n. a colorless gaseous hydro- carbon, C:H2 prepared by the reaction of water with calcium carbide: it is used as the starting material in the synthesis of many organic compounds, for lighting, and, with oxygen in a blowtorch, for '
'the metal replacing the hydrogen of the acid; (e) the power of decomposing most carbonates, caus- ing effervescence: according to modern theory an acid is a compound which yields hydrogen ions (protons) to a base in a chemical reaction. Acids vary in their terminations according '
' ac/i-d6/sis, 7n. in medicine, a condition in which the alkali reserve (blood bicarbonates) , of the blood is lower than normal: loosely\ncalled acid intoxication, autointoxication.\nhigh percentage\nfate, far, fast, fall, finäl, care, at; mete, prey, hér, met; pine, marine, bird, p'
"\nå-cid'ū-lae, n.pl. [L.] an old name for medici?\n_ nal springs impregnated with carbonic acid.\nA-cid’/t-late, v.l.; acidulated, pt., pp.; acidu- lating, ppr. [L. acidulus, slightly sour, and\n_ -ate.] to make somewhat acid or sour, ;\na-cid’u-lent, a. having an acid quality; tart\na"
', and also for tinder and in dyeing.\nagaric mineral; a light, chalky deposit of carbonate of lime formed in caverns or fissures\n_ of limestone.\na-gasp’, adv. and a. in a gasping manner; out of breath.\na-gast’, a, obsolete spelling of aghast.\nA-gas’tri-a, n.pl. [Gr. a priv., and g'
Traceback (most recent call last):
  File "<string>", line 5, in <module>
BrokenPipeError: [Errno 32] Broken pipe
```


## [2026-09-14T01:13:05.145Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://www.etymonline.com/word/carboy\" \"https://en.wiktionary.org/wiki/carboy\" \"https://www.etymonline.com/word/carafe\" \"https://en.wiktionary.org/wiki/%D9%82%D8%B1%D8%A8%D8%A9\" \"https://www.etymonline.com/word/alkali\" \"https://en.wiktionary.org/wiki/alkali\" \"https://en.wiktionary.org/wiki/%D9%82%D9%84%D9%89\" \"https://abadis.ir/fatofa/%D9%82%D8%B1%D8%A7%D8%A8%D9%87/\" \"https://abadis.ir/fatofa/%D9%82%D9%84%DB%8C%D9%87/\" \"https://abadis.ir/fatofa/%D9%82%D9%84%DB%8C%D8%A7/\" \"https://www.ahdictionary.com/word/search.html?q=carboy\" \"https://www.ahdictionary.com/word/search.html?q=alkali\" \"https://en.wikipedia.org/wiki/Carboy\"; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 411 (book 381), roots Qirbah/Q.l.y: carboy, qarrabe, alkali, qalyeh\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T01:13:15.512Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5ba0447a043baaef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9ba8e52fd743dc29.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9e6b847831eb3d55.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f60ad02bef3ea358.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0070109655be6e11.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/690b1ed5ec3b175b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/be474731510f27d0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2ede512a38ba5fcd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4d2323cbfde16499.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f960be9dad613d69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5a17e42a9c2a4053.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/281430f0bd3ba66d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/641ab809c0736333.txt
```


## [2026-09-14T01:13:23.705Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o -i -E \"car'?.?boy[^a-z].{0,220}\" FSD_vol1.txt | head -4\necho \"--- alkali entry FSD\"\ngrep -n -o -i -E \"al'?ka-li,.{0,300}\" FSD_vol1.txt | head -3\ngrep -n -o -i -E \"\\[<\\s*Ar\\.[^]]{0,120}\\]\" FSD_vol1.txt | grep -i -E 'qili|kali|qali' | head -5"
}
```


### [2026-09-14T01:13:24.955Z] TOOL RESULT

```
18412:carboy,  etc.,  to  prevent tine  (water,  demulcents);  zinc  (milk,  eggs,  carbonate  of  gurgling  and  splashing  when  the  contents  are  poured  out. potash).  [F.,  <   L.  antidolum,  <   Gr.  antidoton,  <   anti ,  
--- alkali entry FSD
```


## [2026-09-14T01:13:29.219Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11881,11884p' FSD_vol1.txt | head -c 2500"
}
```


### [2026-09-14T01:13:29.302Z] TOOL RESULT

```
al'ka-ll,  1   al'ks-lai  or  -li;  2   Sl'kn-ll  or  -I!  (xin),  n.  f-u«  or -lies,  X   -laiz  or  -hz;  2   -lig  or  -lig,  pi.]  1.  Chem. pound  of  hydrogen  and  oxygen  with  any  one  of  the  ele- ments lithium,  sodium,  potassium,  rubidium,  and sium,  or  the  radical  ammonium,  characterized  by solubility  in  water  and  capability  of  neutralizing  n cm?, popularly  extended  to  anything  that  will  neutralise  an acid,  as  lime,  magnesia,  etc,  ,
Aqueous  solutions  of  the  alkalis  act  corrosively  on  animn and  vegetable  substances,  and  also  alter  tbc coloring-matters,  as  red  litmus,  which  they  turn  blue.
2.  A   saline  product  of  the  lixiviation  of  the  ashes  °{?e‘ plants  that  contain  sodium  and  potassium  m   combina- tion; soda-ash.  3.  Any  form  of  alkaline  substance  use in  the  arts,  as  either  the  hydroxid  or  cnrbonateoi  s   ' dium,  potassium,  or  ammonium.  4.  The  saltwort :   i*
sola  kali).  [   <   F.  alcali,  <   Ar.  abqally,  <   a^j,iLieii£ qally,  ashes  of  saltwort,  <   qalay,  fry,]  M   ca-m» al'ca-ly*.  ,   „   ln.
```


## [2026-09-14T01:14:14.691Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:14:14.739Z] TOOL RESULT

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


## [2026-09-14T01:14:16.088Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%84%DB%8C%D8%A7",
 "prompt": "Any language sections for قلیا (Persian/Arabic)? Give etymology and meaning."
}
```


### [2026-09-14T01:14:20.597Z] TOOL RESULT

```
# قلیا (qaliyâ) - Persian

**Meaning:** This Persian noun refers to an "alkali" in chemistry contexts.

**Etymology:** The page doesn't provide explicit etymological information about the word's origins or historical development.

**Key Details:**
- Pronunciation: qaliyâ (with audio available from Iranian Persian)
- Plural form: قلیاها (qaliyâhâ)
- **Synonym:** باز (bâz) - also means alkali
- **Antonym:** اسید (asid) - meaning acid
- **Derived term:** قلیایی (qaliyâyi)

The Wiktionary entry categorizes this as a chemistry term and notes it's a Persian lemma (base word form).
```


## [2026-09-14T01:14:29.392Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%82%D9%84%DB%8C%D8%A7\" --note \"page 411, Persian qaliyā 'alkali'\" 2>&1 | tail -1\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg411_300.png data/verification/sources/refs/ocr/BOOK/411.png && ls -la data/verification/sources/refs/ocr/BOOK/411.png"
}
```


### [2026-09-14T01:14:30.975Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7ccb3575ac09c697.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 64940 Sep 13 21:14 data/verification/sources/refs/ocr/BOOK/411.png
```


## [2026-09-14T01:18:14.383Z] TOOL CALL #51: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-411.json",
 "content": "{\n  \"pdf_page\": 411,\n  \"book_page\": 381,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 3,\n      \"root\": \"Qirbah, Qirrâbah\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic قِرْبَة qirba 'waterskin, leathern bottle' and قَرَّابَة qarrāba 'big jug', both under the Semitic root q-r-b\",\n      \"note\": \"The root box is right in substance. Arabic قِرْبَة qirba is the ordinary word for a leathern water-bottle/waterskin (Wiktionary places it under the triliteral root ق ر ب, alongside the anatomical 'bladder' and 'bagpipe' senses). The second form Nourai prints, 'Qirrâbah', is the vessel-word that AHD vocalises qarrāba 'big jug' and derives from the II-stem qarraba 'to bring near' (AHD s.v. carboy: 'see qrb in the Appendix of Semitic roots'); Persian lexicography (Dehkhoda, Mo'in) vocalises the borrowed form قَرّابه qarrābe, which points the same way. So Nourai's vowelling 'Qirrâbah' is a harmonisation with qirbah rather than the form the dictionaries print — a vowel choice on an unvocalised skeleton قرابة, not a wrong word, hence no transcription flag. The gloss 'a leathern bottle' fits qirba exactly and qarrāba loosely ('big jug'). Note also the structural point recorded at node #2: on the printed page the arrow to English carboy leaves the PERSIAN box, not the root box.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است. «قِرْبَة» در عربی مشک یا ظرف چرمیِ آب است و ویکی‌واژه آن را ذیل ریشهٔ سه‌حرفی ق‌-ر-ب می‌آورد. صورت دوم که نورایی «Qirrâbah» ضبط کرده همان واژه‌ای است که فرهنگ American Heritage آن را qarrāba «کوزهٔ بزرگ» می‌خواند و از باب تفعیلِ قَرَّبَ «نزدیک آوردن» می‌گیرد؛ دهخدا و معین نیز صورت فارسیِ وام‌گرفته را «قَرّابه» ضبط کرده‌اند. بنابراین مصوّت‌گذاریِ نورایی (قِرّابه) همسان‌سازی با «قربه» است، نه واژه‌ای نادرست، و چون رسم‌الخط عربیِ «قرابة» بی‌اعراب است، خطای چاپی به شمار نمی‌رود. معنیِ «بطری چرمی» برای قربه کاملاً و برای قرّابه تقریباً درست است.\",\n      \"sources\": [\n        \"https://www.ahdictionary.com/word/search.html?q=carboy\",\n        \"https://en.wiktionary.org/wiki/%D9%82%D8%B1%D8%A8%D8%A9\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"AHD:202\",\n          \"status\": \"supports\",\n          \"note\": \"The 1975/76 New College Edition p.202 (the alphabetical page carrying 'carboy') is not open online, but the AHD etymology is unchanged in the current online edition, ahdictionary.com/word/search.html?q=carboy: '[Persian qarābah, from Arabic qarrāba, big jug, from qarraba, to bring near, derived stem of qaruba, to be near; see qrb in the Appendix of Semitic roots.]' — i.e. exactly Nourai's Arabic root box, with qarrāba where he writes Qirrâbah.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"KLN\",\n          \"where\": \"KLN_1966.txt leaf 136 (~p.247-248), s.v. carboy\",\n          \"stance\": \"supports\",\n          \"note\": \"grep -n -i 'carboy' KLN_1966.txt → 'carboy, n., a large glass bottle. — Pers. qaraba. Cp. Arab. qirbah, \\\"a large leathern bottle\\\".' Klein's qirbah gloss is word-for-word Nourai's root gloss.\"\n        },\n        {\n          \"src\": \"HJB\",\n          \"where\": \"Hobson-Jobson pp. 162b-163a s.v. CARBOY (HJB.txt lines 5240-5263)\",\n          \"stance\": \"supports\",\n          \"note\": \"'Though it is not an Anglo-Indian word, it comes (in the form ḳarāba) from Persia … Ḳarāba is no doubt connected with Ar. ḳirba, \\\"a large leathern milk-bottle.\\\"' Yule cites Kaempfer, Amoen. Exot. 879 (1712) 'quae vocant Karabé' for the Shiraz wine trade.\"\n        },\n        {\n          \"src\": \"LKT\",\n          \"where\": \"Lokotsch no. 1074 (LKT.txt line 2549)\",\n          \"stance\": \"partial\",\n          \"note\": \"'1074. Pers. ḳārābā: \\\"Große lederne Milchflasche\\\" [offenbar mit ar. kirba \\\"Schlauch\\\" verwandt]; hieraus engl. carboy' — Lokotsch only says the Persian word is 'evidently related to' Ar. qirba, and does not commit to a direction of borrowing.\"\n        },\n        {\n          \"src\": \"SKT\",\n          \"where\": \"Skeat, SKT.txt leaf 645 s.v. Carboy\",\n          \"stance\": \"supports\",\n          \"note\": \"'Carboy, a large glass bottle, protected by wicker-work. (Arab.?) Pers. qarāba, a large flagon; which is prob. of Arab. origin. Cf. Pers. and Arab. qirbah, a water-skin, water-bottle.' Skeat's question mark marks the same residual doubt.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"Qarrâbeh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic قَرَّابَة qarrāba 'big jug' (II-stem noun of qarraba 'to bring near', root q-r-b, and in practice contaminated with قِرْبَة qirba 'leathern water-bottle') was taken into New Persian as قرّابه qarrābe, with the regular Persian treatment of Arabic feminine -a(t) as -e (tā' marbūṭa written ه). The sense narrowed from a generic large vessel to the wide-bellied glass flagon in which Shiraz wine was sold — Dehkhoda defines it 'شیشه شراب. صراحی … قسمی شیشه شکم فراخ بزرگتر از برنی' and Mo'in 'شیشهٔ شراب، صراحی', tagging the word [ع.] i.e. Arabic. The Hafez line Nourai quotes ('حافظ قرابه کش شد و مفتی پیاله نوش') shows the wine-bottle sense already in the 8th/14th century, and Kaempfer (Amoen. Exot. 879, 1712) describes the Shirazi 'Karabé' in exactly this shape. Nourai's Persian script قرّابه with shadda matches Mo'in's vocalisation (قَ رَّ بِ); the parenthetic قَراب he adds is the unsuffixed Arabic qirāb/qarāb. One dissenting voice: the Wikipedia article 'Carboy' asserts the reverse route, Persian qarābah < Middle Persian *karāvah, with Arabic qarrāba borrowed FROM Persian, but it offers no source and no Middle Persian attestation exists (MacKenzie has no such word), so AHD's Arabic > Persian direction stands.\",\n          \"derivation_fa\": \"«قرّابه» وام‌واژه‌ای است از عربیِ قَرَّابة «کوزهٔ بزرگ» (اسم از باب تفعیلِ قَرَّبَ، ریشهٔ ق‌-ر-ب، که در کاربرد با قِرْبَة «مشک چرمی» آمیخته شده است). تاء مربوطهٔ عربی در فارسی نو به‌طور قاعده‌مند «ـه» (ـه‌ی غیرملفوظ) شده و qarrāba به «قرّابه» بدل گشته است. تحول معنایی از «ظرف بزرگ» به «صراحی و شیشهٔ شکم‌فراخ شراب» است؛ دهخدا آن را «شیشهٔ شراب، صراحی… قسمی شیشهٔ شکم فراخ» و معین «شیشهٔ شراب، صراحی» با نشانِ [ع.] آورده‌اند. بیت حافظ («حافظ قرابه‌کش شد و مفتی پیاله نوش») گواه رواج این معنی در سدهٔ هشتم هجری است. ادعای نورایی درست است؛ تنها روایت مخالف (ویکی‌پدیای انگلیسی) که واژه را فارسیِ برگرفته از فارسی میانهٔ *karāvah می‌داند بی‌سند است و در فرهنگ مکنزی چنین صورتی نیست.\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/search.html?q=carboy\",\n            \"https://abadis.ir/fatofa/%D9%82%D8%B1%D8%A7%D8%A8%D9%87/\",\n            \"https://en.wiktionary.org/wiki/carboy\",\n            \"https://en.wikipedia.org/wiki/Carboy\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:202\",\n              \"status\": \"supports\",\n              \"note\": \"AHD s.v. carboy: '[Persian qarābah, from Arabic qarrāba, big jug…]' — the Arabic → Persian step Nourai draws. (Print p.202 of the 1975 New College Edition is not open online; the online edition carries the same bracket.)\"\n            },\n            {\n              \"ref\": \"MON:2651\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in's entry, read via abadis.ir/fatofa/قرابه (section فرهنگ معین): '(قَ رَّ بِ) [ع.] (اِ.) شیشة شراب، صراحی.' — Arabic origin tag [ع.] plus the gloss 'wine bottle, decanter' = Nourai's 'a glass bottle (for wine)'. The 6-vol. print pagination (p.2651) could not be checked directly; the 2-vol. Adena OCR on disk is unusable for Persian script.\"\n            },\n            {\n              \"ref\": \"FVA:328\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989): refs_online.json records no digital copy on any permitted platform (re-searched 2026-09); local_file is null.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir, section فرهنگ معین s.v. قرابه\",\n              \"stance\": \"supports\",\n              \"note\": \"'(قَ رَّ بِ) [ع.] (اِ.) شیشة شراب، صراحی.'\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Dehkhoda (Loghatnāme) s.v. قرابه, read via abadis.ir — Borhan-e Qate' vol. for ق is scan-only and not OCR'd locally\",\n              \"stance\": \"supports\",\n              \"note\": \"Dehkhoda: 'شیشه شراب. صراحی … قسمی شیشه شکم فراخ بزرگتر از برنی', with classical citations (Nezami and others). Borhan vols 3-5 have no local OCR text (only BQT_v1/v2 are on disk), so Mo'in's Borhan footnote could not be consulted.\"\n            },\n            {\n              \"src\": \"HJB\",\n              \"where\": \"Hobson-Jobson p.162b s.v. CARBOY\",\n              \"stance\": \"supports\",\n              \"note\": \"'it comes (in the form ḳarāba) from Persia, as Wedgwood has pointed out … Ḳarāba is no doubt connected with Ar. ḳirba'; Macgregor 1875 'huge bottles called Kāraba'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 136 s.v. carboy\",\n              \"stance\": \"supports\",\n              \"note\": \"'— Pers. qaraba. Cp. Arab. qirbah' — Klein has the Persian word as the immediate source of the English one.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"English\",\n          \"words\": \"carboy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English carboy 'large globular glass bottle in wicker-work' is first recorded in the early 18th century (Etymonline 1753; Hanway 1754 'six karboys of Isfahan wine'; Kaempfer's Latin Karabé 1712) and comes straight from Persian قرّابه qarrābe/qarāba, brought back by the Levant- and Persian-Gulf wine and acid trade rather than through any literary channel; English -oy renders Persian -ā(b)a as heard, as in the parallel 18th-c. spellings karboy / corrobah / caraboy recorded in Hobson-Jobson and Milburn. Klein, Skeat, Yule, Lokotsch, Etymonline and AHD all give the Persian word as the immediate etymon (AHD: 'Persian qarābah, from Arabic qarrāba'); carafe (< It. caraffa / Sp. garrafa) is a probable doublet that reached English by the Mediterranean route in 1786. STRUCTURAL NOTE: on the printed page (p.381) the arrow into the English box starts under the PERSIAN box, not at the root box — so Nourai draws Arabic → Persian → English, which is what every modern source says. The JSON gives this node parent 0 (the Arabic root); that is an extraction error and should be changed to parent 1.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی carboy «شیشهٔ بزرگ حصیرپوش» از اوایل سدهٔ هجدهم میلادی ثبت شده (اتیمانلاین: ۱۷۵۳؛ هنوی ۱۷۵۴: «شش karboy شراب اصفهان»؛ کمپفر ۱۷۱۲: Karabé) و مستقیماً وام‌گرفته از «قرّابه»ی فارسی است، از راه تجارت شراب و اسید در خلیج فارس و شام، نه از راه متون. پایانهٔ -oy برداشت شنیداری انگلیسیان از -ābe فارسی است؛ صورت‌های کهن‌تر karboy و corrobah نیز در Hobson-Jobson آمده است. کلاین، اسکیت، یول، لوکوچ و AHD همگی واژهٔ فارسی را خاستگاه بی‌واسطهٔ آن می‌دانند و carafe دوگانهٔ (doublet) آن از راه ایتالیایی است. نکتهٔ ساختاری: در صفحهٔ چاپی، پیکان به جعبهٔ انگلیسی از جعبهٔ فارسی می‌آید نه از ریشهٔ عربی؛ یعنی نمودار نورایی درست است و خطا در استخراج داده (parent=0 به جای parent=1) رخ داده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/carboy\",\n            \"https://en.wiktionary.org/wiki/carboy\",\n            \"https://www.ahdictionary.com/word/search.html?q=carboy\",\n            \"https://www.etymonline.com/word/carafe\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:238\",\n              \"status\": \"supports\",\n              \"note\": \"Klein s.v. carboy, found at KLN_1966.txt leaf 136 (the leaf runs 'car- … cardamom', i.e. printed pp. ~247-248 in this two-pages-per-leaf scan; Nourai's p.238 is within the same alphabetical stretch of vol. I): 'carboy, n., a large glass bottle. — Pers. qaraba. Cp. Arab. qirbah, \\\"a large leathern bottle\\\".' The same text stands in the 1971 one-volume edition (KLN_1971.txt line 39538).\"\n            },\n            {\n              \"ref\": \"AHD:202\",\n              \"status\": \"supports\",\n              \"note\": \"AHD s.v. carboy: '[Persian qarābah, from Arabic qarrāba, big jug, from qarraba, to bring near … see qrb in the Appendix of Semitic roots.]'\"\n            },\n            {\n              \"ref\": \"WEB:272\",\n              \"status\": \"not_found\",\n              \"note\": \"Webster's New Twentieth Century Dictionary, 2nd ed., vol. 1 OCR on disk (WEB_vol1.txt) covers the C range (carbon, carbuncle, cardamom all present) but no 'carboy' headword survives the OCR — regex searches for car.?bo[yj] and car[-/ ]?boy return nothing. Could not confirm the page number.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 136; KLN_1971.txt line 39538\",\n              \"stance\": \"supports\",\n              \"note\": \"'carboy, n., a large glass bottle. — Pers. qaraba.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, SKT.txt leaf 645 s.v. Carboy\",\n              \"stance\": \"supports\",\n              \"note\": \"'Carboy, a large glass bottle, protected by wicker-work. (Arab.?) Pers. qarāba, a large flagon; which is prob. of Arab. origin.'\"\n            },\n            {\n              \"src\": \"HJB\",\n              \"where\": \"Hobson-Jobson pp.162b-163a s.v. CARBOY\",\n              \"stance\": \"supports\",\n              \"note\": \"'A large glass bottle holding several gallons, and generally covered with wicker-work … it comes (in the form ḳarāba) from Persia'; quotations 1712 Kaempfer, 1754 Hanway 'six karboys of Isfahan wine', 1875 Macgregor.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 1074\",\n              \"stance\": \"supports\",\n              \"note\": \"'hieraus engl. carboy \\\"große Glasflasche zum Verschicken von Säuren und Explosivstoffen\\\" [Hobson-Jobson 162/163]' — from the Persian word.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"WEB_vol1.txt (Webster's 2nd ed., vol. 1)\",\n              \"stance\": \"silent\",\n              \"note\": \"No 'carboy' headword recoverable from this OCR, though the volume reaches the C range.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"FSD_vol1.txt line 18412\",\n              \"stance\": \"silent\",\n              \"note\": \"Funk & Wagnalls mentions 'carboy' only inside the entry anti-guggler ('the mouth of a narrow-necked vessel, as a bottle, carboy, etc.'); the headword entry did not survive the OCR.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 5,\n      \"root\": \"Q.l.y\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root ق ل ي q-l-y, verb قَلَى qalā 'to fry, roast (in a pan)'\",\n      \"note\": \"The root is real and correctly labelled. Arabic قَلَى qalā (imperf. yaqlī) 'to fry, roast in a pan' is a Common Semitic verb — Klein compares Heb. qālāh 'he roasted, parched', Aram. qelā 'burned', Akkad. qalū 'to burn'; Wiktionary lists cognates in Amharic, Aramaic, Hebrew and Akkadian. AHD s.v. alkali refers to the same root as 'qly' in its Appendix of Semitic Roots. Nourai's gloss 'to cook or barbecue meat' is a loose but fair rendering (the verb is specifically pan-frying/roasting, and it also has a homonymous sense 'to hate', Qur'an 93:3). Layout note: on the printed page the second line 'Qely, Qela : alkaline material obtained from wood ash' sits INSIDE the same Arabic root box as Q.l.y; the extraction has promoted it to a separate node #1 with refs=None. That is a rendering artifact, not a second derivation step.\",\n      \"note_fa\": \"ریشه واقعی و برچسب زبانیِ آن درست است: ق‌-ل‌-ی در عربی، فعل قَلَى (یَقلی) «سرخ کردن، بریان کردن در تابه». این فعل سامیِ مشترک است؛ کلاین آن را با عبری qālāh «بریان کرد»، آرامی qelā «سوزاند» و اکدی qalū «سوختن» می‌سنجد و فرهنگ AHD نیز ذیل alkali به همین ریشهٔ سامیِ qly ارجاع می‌دهد. معنایی که نورایی داده («پختن یا کباب کردن گوشت») کمی کلی است ولی نادرست نیست. نکتهٔ صفحه‌آرایی: در صفحهٔ چاپی سطر «Qely, Qela» درون همان جعبهٔ ریشه است، نه گرهی جداگانه؛ جدا شدن آن در داده‌های استخراج‌شده یک خطای خوانشِ نمودار است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%82%D9%84%D9%89\",\n        \"https://www.ahdictionary.com/word/search.html?q=alkali\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"SAP:93\",\n          \"status\": \"not_checked\",\n          \"note\": \"Sayyah's Farhang (the Persian translation of al-Munjid), 3 vols: refs_online.json lists it as purchase-only (fidibo.com), no local_file, no open scan. The Arabic side of the claim was instead checked against Wiktionary's قلى and AHD's Semitic-root note (see consulted).\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"KLN\",\n          \"where\": \"KLN_1966.txt leaf 38 (~p.52), s.v. alkali\",\n          \"stance\": \"supports\",\n          \"note\": \"'fr. qilī, \\\"charred ashes of the saltwort\\\", fr. qalā, \\\"he fried, roasted\\\", which is rel. to Heb. qālāh, \\\"he roasted, parched\\\", Aram. qelā, \\\"burned\\\", Akkad. qalū \\\"to burn\\\".'\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"ahdictionary.com s.v. alkali (Appendix of Semitic Roots, qly)\",\n          \"stance\": \"supports\",\n          \"note\": \"'qily, ashes (from qalā, to fry, roast; see qly in the Appendix of Semitic roots)'.\"\n        },\n        {\n          \"src\": \"LKT\",\n          \"where\": \"Lokotsch no. 1029 (LKT.txt line 2452)\",\n          \"stance\": \"partial\",\n          \"note\": \"'1029. Ar. ḳali: \\\"Pottasche, Aschensalz\\\"' — Lokotsch starts from the noun and does not mention the verb.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"Qely, Qela\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The deverbal noun قِلْي qily (also قَلَى/قِلًى in the manuscripts, hence Nourai's double citation 'Qely, Qela') is formed on the same root as قَلَى qalā 'to fry, roast': what is left in the pan after roasting, i.e. calcined ash. AHD glosses al-qily 'the ashes, lye, potash'; Klein 'charred ashes of the saltwort'. Technically it is the soda-ash got by burning saltwort/glasswort (Salsola kali, Persian اشنان ušnān), not wood ash in general, so Nourai's gloss 'alkaline material obtained from wood ash' is slightly too broad — but the substance and the derivation from the root are exactly right. On the printed page this line stands inside the root box, i.e. it is a second headword of the root rather than a separate derivational step; verdict is given for the word itself.\",\n          \"derivation_fa\": \"«قِلْی» اسم مصدرِ همان ریشهٔ ق‌-ل‌-ی است: آنچه پس از بریان کردن در تابه بر جای می‌ماند، یعنی خاکستر سوخته؛ ضبط دوگانهٔ نورایی (Qely, Qela) بازتاب صورت‌های قِلْی و قِلیٰ در متون است. AHD آن را «خاکستر، قلیاب، پتاس» و کلاین «خاکستر سوختهٔ اشنان» معنی کرده‌اند. به‌دقت، این مادّه از سوزاندن گیاه اشنان (Salsola kali) به دست می‌آید نه از خاکستر هر چوبی؛ پس تعریف نورایی اندکی کلی است، اما اشتقاق از ریشه درست است. در صفحهٔ چاپی این سطر درون جعبهٔ ریشه است و گرهی مستقل به شمار نمی‌رود.\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/search.html?q=alkali\",\n            \"https://en.wiktionary.org/wiki/alkali\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SAP:93\",\n              \"status\": \"not_checked\",\n              \"note\": \"Node carries refs=None in the chart; the root's SAP:93 is the governing citation and Sayyah is purchase-only (no local copy, no open scan).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 38, s.vv. alkali and kali\",\n              \"stance\": \"supports\",\n              \"note\": \"'kali, n., glasswort. — Arab. qilī, \\\"charred ashes of the saltwort\\\". See alkali and cp. kalium.' and 'kalium, n., potassium (chem.) — ModL., fr. Arab. qilī.'\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 1029\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ar. ḳali: \\\"Pottasche, Aschensalz\\\"; mit ar. Art. in alle europäischen Sprachen als Fachausdruck der Chemie übergegangen … Auch der Name des Elementes Kalium, Calium gehört hierhin.'\"\n            },\n            {\n              \"src\": \"DOZ\",\n              \"where\": \"Dozy, Oosterlingen, DOZ.txt line 421 s.v. ALKALI\",\n              \"stance\": \"supports\",\n              \"note\": \"'ALKALI. Is het Arab. القلي.' (Dutch: 'is the Arabic al-qilī').\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"qalya; qalyeh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two separate Arabic loans in Persian, both on q-l-y. (a) قلیه qalye is Arabic قَلِيَّة qaliyya 'fried/roasted meat' (the fa'īla form of qalā), taken in with the usual Persian -a(t) > -e; Mo'in's entry tags it '[ع. قلیة]' and glosses 'پاره‌ای گوشت، قطعه‌ای گوشت', while Dehkhoda defines it 'گوشت بر تابه بریان کرده شده … در روغن میان دیگ بریان کرده نانخورش سازند' with citations from Nāṣer-e Khosrow and Sa'di — i.e. Nourai's 'a food made with meat' is right, and the word is still the name of the herb-and-meat stew qalye-ye māhi/qalye. This part is confirmed. (b) قلیا qaliyā 'alkali' is the weaker link: it corresponds to Arabic قِلْي al-qily with an added -ā, and Dehkhoda equates it with اشخار/شخار, the saltwort ash, which supports an Arabic origin; but no Persian or Arabic dictionary consulted actually documents a form qilyā in Arabic, and the modern chemical sense of قلیا (opposite of اسید, adj. قلیایی) is plainly modelled on European alkali, so at least the technical use is a 19th-20th-c. re-borrowing of the Arabic word through French/English rather than a direct inheritance. Node verdict follows the weaker word.\",\n          \"derivation_fa\": \"دو وام‌واژهٔ جداگانهٔ عربی از ریشهٔ ق‌-ل‌-ی در فارسی: (الف) «قلیه» از عربیِ قَلِیَّة «گوشت بریان‌شده» (وزن فعیله از قلی)، با تبدیل قاعده‌مندِ تاء مربوطه به «ـه»؛ معین آن را با نشانِ «[ع. قلیة]» و معنیِ «پاره‌ای گوشت» و دهخدا «گوشت بر تابه بریان کرده شده… نانخورش سازند» با شواهدی از ناصرخسرو و سعدی آورده‌اند — پس ادعای نورایی دربارهٔ «قلیه» درست است و همان خورشِ «قلیهٔ ماهی» امروزی است. (ب) «قلیا» سست‌تر است: گرچه دهخدا آن را برابر «اشخار/شخار» (خاکستر اشنان) می‌داند و پیوندش با قِلْیِ عربی روشن است، صورت *قِلیا در فرهنگ‌های عربی مستند نشد و کاربرد شیمیاییِ امروزی «قلیا/قلیایی» در برابر «اسید» آشکارا بر الگوی alkali اروپایی ساخته شده، یعنی وام‌گیری دوباره از راه فرانسه/انگلیسی است. بنابراین گره در کل «با احتیاط پذیرفتنی» ارزیابی می‌شود.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%82%D9%84%DB%8C%D9%87/\",\n            \"https://abadis.ir/fatofa/%D9%82%D9%84%DB%8C%D8%A7/\",\n            \"https://en.wiktionary.org/wiki/%D9%82%D9%84%DB%8C%D8%A7\",\n            \"https://en.wiktionary.org/wiki/%D9%82%D9%84%D9%89\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:2724\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in read via abadis.ir/fatofa/قلیه (section فرهنگ معین): '(قَ یَ یا یِ) [ع. قلیة] (اِ.) پاره‌ای گوشت، قطعه‌ای گوشت. ۲- حبوبات و سبزی.' — the Arabic-origin tag and the meat sense are exactly Nourai's. Mo'in's قلیا entry gives 'شخار، ماده‌ای که از اشنان گرفته می‌شود و از آن در صابون‌سازی استفاده می‌کنند'. The 6-vol. print pagination (p.2724) could not be checked (no usable Persian-script OCR of Mo'in on disk).\"\n            },\n            {\n              \"ref\": \"SAP:94\",\n              \"status\": \"not_checked\",\n              \"note\": \"Sayyah's Farhang is purchase-only (fidibo), no local file and no open scan; refs_online.json records no accessible copy.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir, فرهنگ معین s.vv. قلیه and قلیا\",\n              \"stance\": \"supports\",\n              \"note\": \"قلیه: '[ع. قلیة] (اِ.) پاره‌ای گوشت'; قلیا: 'شخار، ماده‌ای که از اشنان گرفته می‌شود و از آن در صابون‌سازی استفاده می‌کنند'.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Dehkhoda (Loghatnāme) s.v. قلیه via abadis.ir; Borhan-e Qate' vol. for ق not available as local OCR\",\n              \"stance\": \"supports\",\n              \"note\": \"'قلیه. [قَ لی یَ] گوشت بر تابه بریان کرده شده و به استعمال گوشتی که در روغن میان دیگ بریان کرده نانخورش سازند', with verse citations from Nāṣer-e Khosrow and Sa'di. Only BQT_v1/v2 (آ–ج) are on disk as text, so Mo'in's Borhan footnote for ق could not be read.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi\",\n              \"stance\": \"silent\",\n              \"note\": \"Aryanpur covers Indo-European roots of Persian only; a Semitic loan such as قلیه/قلیا falls outside its scope and no local text/index entry exists.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 38, s.v. alkali\",\n              \"stance\": \"partial\",\n              \"note\": \"Klein documents Arab. qilī 'charred ashes of the saltwort' < qalā but says nothing about its Persian reflexes.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"French\",\n          \"words\": \"alcali\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French alcali (earlier alcalli, 16th c.; Pihan notes 'Anciennement on écrivait alkali') continues Arabic اَلْقِلْي al-qily, article al- included, as the alchemists' name for saltwort ash. The borrowing was not direct from Arabic into French, however: the word entered the Latin of the western alchemists first — Klein notes 'the word alkali first appears in the writings of Albertus Magnus (1206?-1280)' — and French took it from that Medieval Latin alkali/alcali, whence also Sp./Pg. alcali, It. alcali, Ger. Alkali. So Nourai's arrow Arabic → French is right in substance but skips the Medieval-Latin alchemical stage that every source records; hence 'plausible' rather than 'confirmed'.\",\n          \"derivation_fa\": \"واژهٔ فرانسویِ alcali (صورت کهن‌تر alcalli؛ پیان یادآور می‌شود که پیش‌تر alkali می‌نوشتند) بازماندهٔ عربیِ «اَلْقِلْی» است که حرف تعریف «ال» را نیز با خود برده است و در کیمیاگری نامِ خاکستر اشنان بوده است. اما این وام‌گیری مستقیم از عربی به فرانسه نبوده: واژه نخست به لاتینِ کیمیاگرانِ غرب راه یافت — کلاین می‌نویسد نخستین بار در نوشته‌های آلبرتوس ماگنوس (سدهٔ سیزدهم) دیده می‌شود — و از همان لاتینِ میانه به فرانسوی، اسپانیایی، ایتالیایی و آلمانی رفت. پس پیکان نورایی (عربی ← فرانسه) در اصل درست است ولی حلقهٔ لاتینِ میانه را نادیده گرفته؛ از این رو «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/alkali\",\n            \"https://www.etymonline.com/word/alkali\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:50\",\n              \"status\": \"supports\",\n              \"note\": \"Klein s.v. alkali, KLN_1966.txt leaf 38 (the leaf runs 'alicula … allegation', i.e. printed pp. ~51-52, adjacent to Nourai's p.50): 'alkali, n. — F. alcalli (now spelled alcali), fr. Arab. al-qilī, fr. al-, \\\"the\\\", and qilī, \\\"charred ashes of the saltwort\\\", fr. qalā, \\\"he fried, roasted\\\" …' — Klein does route the word through French, exactly as Nourai draws it.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 38 s.v. alkali\",\n              \"stance\": \"supports\",\n              \"note\": \"'— F. alcalli (now spelled alcali), fr. Arab. al-qilī … The word alkali first appears in the writings of Albertus Magnus (1206?-1280).'\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls, FSD_vol1.txt line 11881 s.v. al'ka-li\",\n              \"stance\": \"supports\",\n              \"note\": \"'[< F. alcali, < Ar. al-qally, < al, the + qally, ashes of saltwort, < qalay, fry.]'\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 1029\",\n              \"stance\": \"supports\",\n              \"note\": \"'mit ar. Art. in alle europäischen Sprachen … übergegangen: sp. pg. alcali, frz. alcali, als alchemistischer Ausdruck algali \\\"Salpeter\\\" … engl. alkali, dtsch. Alkali'.\"\n            },\n            {\n              \"src\": \"PHN\",\n              \"where\": \"Pihan, PHN.txt line 1149\",\n              \"stance\": \"partial\",\n              \"note\": \"'… température peu élevée. — Anciennement on écrivait alkali.' — confirms the older French spelling but gives no derivation there.\"\n            },\n            {\n              \"src\": \"DOZ\",\n              \"where\": \"Dozy, Oosterlingen s.v. ALKALI\",\n              \"stance\": \"supports\",\n              \"note\": \"'ALKALI. Is het Arab. القلي.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"alkali, alkaline\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Klein — the reference Nourai cites here — takes English alkali from French alcali, and Funk & Wagnalls the same ('< F. alcali'), so the arrow as drawn is defensible. But the fuller record is more complicated: alkali is attested in English from the late 14th century (Chaucer's Canon's Yeoman's Tale era) in the sense 'alkaline substance from calcined plant ashes', which AHD derives 'Middle English, from Medieval Latin, from Arabic al-qily' with no French stage at all; Etymonline and the OED agree, French becoming relevant only for the later chemical vocabulary. The second word in the box, alkaline, is certainly NOT from French: Klein calls it 'a hybrid coined fr. alkali and -ine, a chem. suff. of Latin origin', first attested in English in the 1670s. So the node is accepted with the qualification that Middle English took alkali from Latin and coined alkaline itself.\",\n          \"derivation_fa\": \"کلاین — همان مرجعی که نورایی آورده — واژهٔ انگلیسیِ alkali را از فرانسویِ alcali می‌گیرد و فانک و واگنالز نیز همین را می‌گویند؛ پس پیکان نمودار بی‌پایه نیست. اما سند کامل‌تر پیچیده‌تر است: alkali از اواخر سدهٔ چهاردهم میلادی در انگلیسی میانه به معنی «مادهٔ قلیایی از خاکستر گیاهان» گواهی شده و AHD و اتیمانلاین آن را یکسره از لاتینِ میانه (و آن از عربیِ اَلْقِلْی) می‌دانند، بی‌آنکه فرانسه در میان باشد. واژهٔ دوم جعبه، alkaline، به‌هیچ‌روی فرانسوی نیست: کلاین آن را «ترکیبی دورگه از alkali و پسوند -ine» می‌خواند که در دههٔ ۱۶۷۰ در خود انگلیسی ساخته شده است. از این رو گره با این قید پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alkali\",\n            \"https://en.wiktionary.org/wiki/alkali\",\n            \"https://www.ahdictionary.com/word/search.html?q=alkali\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:50\",\n              \"status\": \"supports\",\n              \"note\": \"Klein, KLN_1966.txt leaf 38: 'alkali, n. — F. alcalli (now spelled alcali) …' and on the same leaf 'alkaline, adj. — A hybrid coined fr. alkali and -ine, a chem. suff. of Latin origin.' — supports the French → English arrow for alkali, but shows alkaline to be an English coinage.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 38 s.vv. alkali, alkaline, alkalimeter, kali, kalium\",\n              \"stance\": \"supports\",\n              \"note\": \"'alkali, n. — F. alcalli … fr. Arab. al-qilī'; 'alkaline, adj. — A hybrid coined fr. alkali and -ine'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"ahdictionary.com s.v. alkali\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'[Middle English, alkaline substance from calcined plant ashes, from Medieval Latin, from Arabic al-qily, the ashes, lye, potash: al-, the + qily, ashes (from qalā, to fry, roast; see qly in the Appendix of Semitic roots).]' — no French link; the route is Arabic → Medieval Latin → Middle English.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls, FSD_vol1.txt line 11881\",\n              \"stance\": \"supports\",\n              \"note\": \"'[< F. alcali, < Ar. al-qally …]'.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"WEB_vol1.txt lines 5543-5546 s.v. alkali\",\n              \"stance\": \"partial\",\n              \"note\": \"The OCR preserves the definition ('Alkalis turn red litmus blue and have an acrid taste. The more common alkalis include: hydrate of potassium (potash) …') but the etymology bracket is illegible in the scan.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, SKT.txt leaf 28 s.v. Alkali\",\n              \"stance\": \"partial\",\n              \"note\": \"'Alkali, a salt. (Arab.) Arab. al, the, + qaly/qily, ashes of glass-wort, which abound in soda.' — Skeat marks the word simply '(Arab.)', naming no French intermediary; he lists alkali among words 'from Arabic' in his appendix.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:18:14.417Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-411.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:18:16.543Z] TOOL CALL #52: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-411.json > /dev/null && echo JSON_OK && python3 tools/verify_check.py 411"
}
```


### [2026-09-14T01:18:17.798Z] TOOL RESULT

```
JSON_OK
nodes verified: 6/6
node verdicts: {'confirmed': 3, 'plausible': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 7, 'not_checked': 3, 'not_found': 1}
books consulted: {'supports': 19, 'silent': 3, 'partial': 4, 'contradicts': 1} | by book: {'KLN': 6, 'LKT': 3, 'FSD': 3, 'MON': 2, 'BQT': 2, 'HJB': 2, 'SKT': 2, 'WEB': 2, 'DOZ': 2, 'ARY': 1, 'PHN': 1, 'AHD': 1}
```


## [2026-09-14T01:18:32.838Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-411.json`; `verify_check.py 411` reports 6/6 nodes, **0 PROBLEM lines**.

**Page 411 (book p. 381)** — 7 of 9 entries are redirects (Qeud, Qhâd, Qhar, Qirrâbah, Qor, Qr, Qreu, Qreus); 2 real charts.

- Root verdicts: confirmed 2 (Qirbah/Qirrâbah; Q.l.y)
- Node verdicts: confirmed 3, plausible 3, disputed 0, transcription_suspect 0
- Ref checks: supports 7, not_checked 3 (SAP ×2 purchase-only, FVA no digital copy), not_found 1 (WEB:272 — no `carboy` headword survives the Webster vol. 1 OCR)

Notable findings:
- `qarrâbeh` / `carboy`: AHD's own bracket ("Persian qarābah, from Arabic qarrāba, big jug, from qarraba… see qrb") backs Nourai exactly; Klein, Skeat, Yule (Hobson-Jobson 162b), Lokotsch 1074 agree. Wikipedia's uncited reverse claim (MP \*karāvah → Arabic) has no support in MacKenzie, so I left it as a minority note.
- `alcali` / `alkali, alkaline` marked **plausible**, not confirmed: Klein (Nourai's ref) and Funk & Wagnalls do route via French, but AHD/Etymonline/OED have Middle English alkali straight from Medieval Latin (Albertus Magnus), and Klein himself calls *alkaline* an English coinage (alkali + -ine, 1670s).
- Persian `qalya` marked down: قلیه < Ar. قَلِيَّة is solid (Mo'in "[ع. قلیة]", Dehkhoda), but قلیا's modern chemical sense is modelled on European *alkali*, so the node is plausible rather than confirmed.

**Extraction errors for the owner to fix in `data/extracted/batch/page-411.json`:**
1. Entry 3 (Qirbah), node **#2 `carboy` has `parent: 0`, but the printed page draws the arrow from the *Persian* box** — should be `parent: 1`. (Verified on the 300 dpi render, copied to `data/verification/sources/refs/ocr/BOOK/411.png`.) This matters: as printed, Nourai's chain is Arabic → Persian → English, which is what every modern source says.
2. Entry 5 (Q.l.y), node **#1 `Qely, Qela` is not a node** — on the page it is the second headword line *inside* the Arabic root box (hence `refs=None`). Cosmetic, but it inflates the node count.
