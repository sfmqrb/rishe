# Verification process log — verify-page-395


## [2026-09-14T00:49:43.900Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 395 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-395.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-395.json. Write /home/sfmqrb/git/rishe/data/verification/page-395.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 395` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:44.875Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:49:45.640Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:45.657Z] TOOL RESULT

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


## [2026-09-14T00:49:46.142Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-395.txt"
}
```


### [2026-09-14T00:49:46.169Z] TOOL RESULT

```
1	=== PDF page 395 (book page 365) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Per 2 : to lead or fly across. Related to the Indo-European root "Per 1".  (refs POK:817)
4	#1 (parent #0) [Avestan] refs=POK:817; KLN:1220 | peretu : bridge
5	  #2 (parent #1) [Pahlavi] refs=SNS:137 | puhl : bridge
6	    #3 (parent #2) [Persian] refs=BQT:414 | pol «پُل» : bridge
7	  #4 (parent #1) [Avestan] refs=POK:817; AHD:452 | hu-parathwa : good to cross over ☞Su 1 | NOTE: Euphrates river in Iraq.
8	    #5 (parent #4) [Persian] refs=None | forât «فُرات» : Euphrates river
9	    #6 (parent #4) [Greek] refs=AHD:452 | Euphrates
10	      #7 (parent #6) [Latin] refs=None | 
11	        #8 (parent #7) [English] refs=None | Euphrates
12	#9 (parent #0) [Avestan] refs=POK:816 | par 2 : there, over there ; pâra 2 : end, shore
13	  #10 (parent #9) [Pahlavi] refs=AEF:209 | bâr 2 : shore, edge
14	    #11 (parent #10) [Persian] refs=AEF:209 | bâr 3 «-بار ۳» : a suffix meaning shore | extra: رودبار ، جویبار ، زنگبار ، دریابار
15	#12 (parent #0) [Avestan] refs=POK:817,850 | parena : feather, wing
16	  #13 (parent #12) [Persian] refs=BQT:397; DRM:286 | par «پَر» : feather, wing | extra: پریدن ، پروانه
17	#14 (parent #0) [Latin] refs=AHD | porta : gate ; portâre : to carry
18	  #15 (parent #14) [French] refs=AHD | 
19	    #16 (parent #15) [Persian] refs=MON |  | extra: پاسپورت ، ترانسپورت ، اسپرت
20	    #17 (parent #15) [English] refs=AHD | port, passport, transport, report, support, sport
21	
```


## [2026-09-14T00:49:49.091Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-395.json | head -200",
 "description": "Show source JSON for page 395"
}
```


## [2026-09-14T00:49:49.860Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:49:50.238Z] TOOL RESULT

```
{
    "pdf_page": 395,
    "book_page": 365,
    "entries": [
        {
            "root": {
                "name": "Per 2",
                "lang": "Indo-European",
                "refs": "POK:817",
                "gloss": "to lead or fly across. Related to the Indo-European root \"Per 1\"."
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:817; KLN:1220",
                    "words": [
                        {
                            "translit": "peretu",
                            "gloss": "bridge",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Pahlavi",
                    "refs": "SNS:137",
                    "words": [
                        {
                            "translit": "puhl",
                            "gloss": "bridge",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "BQT:414",
                    "words": [
                        {
                            "translit": "pol",
                            "gloss": "bridge",
                            "script": "\u067e\u064f\u0644"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u062f\u0633\u062a \u0637\u0645\u0639 \u0628\u0647 \u067e\u06cc\u0634 \u062e\u0633\u0627\u0646 \u0645\u06cc\u06a9\u0646\u06cc \u062f\u0631\u0627\u0632 - \u067e\u0644 \u0628\u0633\u062a\u0647 \u0627\u06cc \u06a9\u0647 \u0628\u06af\u0630\u0631\u06cc \u0627\u0632 \u0622\u0628\u0631\u0648\u06cc \u062e\u0648\u06cc\u0634",
                        "poet": "S\u00e2eb"
                    }
                },
                {
                    "id": 4,
                    "parent": 1,
                    "lang": "Avestan",
                    "refs": "POK:817; AHD:452",
                    "words": [
                        {
                            "translit": "hu-parathwa",
                            "gloss": "good to cross over",
                            "script": null,
                            "see": [
                                "Su 1"
                            ]
                        }
                    ],
                    "note": "Euphrates river in Iraq.",
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": null,
                    "words": [
                        {
                            "translit": "for\u00e2t",
                            "gloss": "Euphrates river",
                            "script": "\u0641\u064f\u0631\u0627\u062a"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 4,
                    "lang": "Greek",
                    "refs": "AHD:452",
                    "words": [
                        {
                            "translit": "Euphrates",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "Latin",
                    "refs": null,
                    "words": [],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 7,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "Euphrates",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:816",
                    "words": [
                        {
                            "translit": "par 2",
                            "gloss": "there, over there",
                            "script": null
                        },
                        {
                            "translit": "p\u00e2ra 2",
                            "gloss": "end, shore",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "Pahlavi",
                    "refs": "AEF:209",
                    "words": [
                        {
                            "translit": "b\u00e2r 2",
                            "gloss": "shore, edge",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "Persian",
                    "refs": "AEF:209",
                    "words": [
                        {
                            "translit": "b\u00e2r 3",
                            "gloss": "a suffix meaning shore",
                            "script": "-\u0628\u0627\u0631 \u06f3"
                        }
                    ],
                    "script_extra": "\u0631\u0648\u062f\u0628\u0627\u0631 \u060c \u062c\u0648\u06cc\u0628\u0627\u0631 \u060c \u0632\u0646\u06af\u0628\u0627\u0631 \u060c \u062f\u0631\u06cc\u0627\u0628\u0627\u0631",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:817,850",
                    "words": [
                        {
                            "translit": "parena",
                            "gloss": "feather, wing",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
```


### [2026-09-14T00:49:50.394Z] TOOL RESULT

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


## [2026-09-14T00:49:55.040Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-395.json'))\nprint(json.dumps(d['entries'][0]['nodes'][12:],ensure_ascii=False,indent=1))\nprint('ENTRIES:',len(d['entries']))\n\"",
 "description": "Show remaining nodes"
}
```


### [2026-09-14T00:49:56.148Z] TOOL RESULT

```
[
 {
  "id": 13,
  "parent": 12,
  "lang": "Persian",
  "refs": "BQT:397; DRM:286",
  "words": [
   {
    "translit": "par",
    "gloss": "feather, wing",
    "script": "پَر"
   }
  ],
  "script_extra": "پریدن ، پروانه",
  "note": null,
  "quote": null
 },
 {
  "id": 14,
  "parent": 0,
  "lang": "Latin",
  "refs": "AHD",
  "words": [
   {
    "translit": "porta",
    "gloss": "gate",
    "script": null
   },
   {
    "translit": "portâre",
    "gloss": "to carry",
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 15,
  "parent": 14,
  "lang": "French",
  "refs": "AHD",
  "words": [],
  "note": null,
  "quote": null
 },
 {
  "id": 16,
  "parent": 15,
  "lang": "Persian",
  "refs": "MON",
  "words": [],
  "script_extra": "پاسپورت ، ترانسپورت ، اسپرت",
  "note": null,
  "quote": null
 },
 {
  "id": 17,
  "parent": 15,
  "lang": "English",
  "refs": "AHD",
  "words": [
   {
    "translit": "port, passport, transport, report, support, sport",
    "gloss": null,
    "script": null
   }
  ],
  "note": null,
  "quote": null
 }
]
ENTRIES: 1
```


## [2026-09-14T00:49:56.519Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SNS','BQT','AHD','AEF','DRM','MON']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Show ref metadata"
}
```


### [2026-09-14T00:49:57.548Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

DRM {"title": "J. Darmesteter, Études iraniennes, 2 vols., Paris 1883", "edition_found": "1883 both tomes in one scan", "kind": "archive_djvu", "url": "https://archive.org/details/etudesiraniennes00darm", "identifier": "etudesiraniennes00darm (t.1 alone: tudesiranienne01darmuoft; t.2 alone: darmesteter-etudes-sur-la-langue-la-litterature-les-croyances-de-la-perse-ancienne)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DRM.txt", "page_offset": "Tome I: leaf = p + 22 (e.g. leaf 26 = p.4); Tome II (starts ~leaf 364): leaf = p + 364 (e.g. leaf 368 = p.4). Nourai does not say w

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
```


## [2026-09-14T00:50:26.146Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','AHD','KLN','DRM','BQT']:\n    print(k,'OFFSET:',d[k].get('page_offset'))\n    print(k,'HINT:',d[k].get('lookup_hint'))\n    print(k,'LOCAL:',d[k].get('local_file'))\n    print()\n\"",
 "description": "Page offsets"
}
```


### [2026-09-14T00:50:27.475Z] TOOL RESULT

```
POK OFFSET: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
POK HINT: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
POK LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt

AHD OFFSET: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
AHD HINT: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
AHD LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt

KLN OFFSET: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KLN HINT: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
KLN LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt

DRM OFFSET: Tome I: leaf = p + 22 (e.g. leaf 26 = p.4); Tome II (starts ~leaf 364): leaf = p + 364 (e.g. leaf 368 = p.4). Nourai does not say which tome - try both. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
DRM HINT: Tome I is the historical grammar of Persian (numbered §§); Tome II contains the 'Études sur la langue...' incl. etymological notes on Persian words. grep the Persian word in transliteration.
DRM LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/DRM.txt

BQT OFFSET: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
BQT HINT: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
BQT LOCAL: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
```


## [2026-09-14T00:50:31.263Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: per\" POK_full.txt | head -40",
 "description": "grep Pokorny full dump for per roots"
}
```


### [2026-09-14T00:50:31.337Z] TOOL RESULT

```
16935:deesse : Portuguese deusa ' goddess '. [see Root / lemma: per-2\ to go over; over]. 
66301:Root / lemma: perd- 
66318:Root / lemma: perg-1 
66324:Root/ lemma: perg-1 \ "pole; trunk' derived from lllyrian : Baltic : Slavic prefix pre- + ga 
66353:Root / lemma: perg-2 
66371:Root / lemma: perk-1, prek- 
66379:Root/ lemma: perk-1, prek-\ to fill, derived from Root/ lemma: *(s)p(h)ereg-, (s)p(h)erag-, 
66418:Root / lemma: pertt-1 
66436:Root / lemma: perti-2, preR- 
66468:Root / lemma: perR-3, pfR- 
66490:Root / lemma: perti-4, preR-, pfR- 
66530:Root / lemma: pericu-s 
66537:the oldest IE cognate, hence Root/ lemma: pertcu-s'. oak derived from an earlier Root 
66569:Root / lemma: per-1, pera- : pre-, preu- 
66577:Root / lemma: per-1, pere- : pre-, preu- : to drizzle, sprinkle, jet, derived from Root / 
66631:Root / lemma: per-2 
66947:Root / lemma: per-2. B. per-, pera- 
67039:Root / lemma: per-2: C. per-, pera- 
67071:Root / lemma: per-2. D. per- 
67102:Root / lemma: per-2. E. per- 
67128:Root / lemma: per-3, per-g- 
67172:Root / lemma: persna, -snT-, -sno- 
67190:Root / lemma: pers- 
67196:Root/ lemma: pers-\ to drizzle, sprinkle; dust, ashes, derived from Root/ lemma: per-1, 
67220:Root / lemma: perth- {*pe-horghi-a) 
67228:Root / lemma: perth-{*pe-horghi-a)\ pole; sprout, derived from a prefixed pe- of Root/
```


## [2026-09-14T00:50:32.618Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=472 && NR<=474 {print \"=== leaf\",NR-1,\"===\\n\" $0}' POK_02.txt | head -150",
 "description": "Print Pokorny leaves around p.817"
}
```


### [2026-09-14T00:50:33.676Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:50:35.905Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '66631,66720p' POK_full.txt",
 "description": "Print Pokorny per-2 entry start"
}
```


### [2026-09-14T00:50:35.956Z] TOOL RESULT

```
Root / lemma: per-2 

Meaning: to go over; over, through, very, exceedingly 

Material: 

A. Dient as preposition, proverb and Adverb: a. per, pe/7(locative of root noun) 
"vorwarts, in Hinausgehen, HiniJbergehen about, in Durchdringen, in Ubermaft', from 
which "about - out, through - toward '; 



Old \nd'\c pan, Avestan pa/n, Old pers. par/y, gr. TTspi, irsp, alb. per {partiy also = Indo 
Germanic *pro), pej, pe, besides per {*per/) with wiederhergestelltem r, Latin per{*peror 
*per/y, Oscan-Umbrian per- and pert {*per-tl)\ gall, eri-. Old Irish ir-, e/"- (analogical *ero-)\ 
cymr. corn. bret. er, Gothic fafr-. Old English fyr-. Old High German fir- 'ver-', Old High 
German Old Saxon firi- ds.; Old Prussian per, Lithuanian per, per-; Slavic per-\v\ Old 
Church Slavic pre- etc.; from "vorwarts' entwickelte sich already Indo Germanic die 
meaning "very' (Old Indie pari-prT-'very dear', gr. nspi-KaAAnq "very beautiful', Latin per- 
magnus "very groft'; Lithuanian per-didis "to big, large'. Old Church Slavic pre-blagt "very 
good'), then die the Uberlegenheit (Old \u6\c pari- as-, pari- biiu-^ excel, surpass ', gr. 
nspi-sTvai ds.), of Ubermaftes or hohen Grades (Old \v\d\c pari-vid-, gr. n£pi-oi5a, Latin 
per-videre "genau know, have knowledge of '); esp. Old Indie and gr. is die meaning 
"ringsum, umherum' (Old Indie /Oa/7/-"umhergehen', gr. nspi-isvai; gr. nspi-^cbwufji = 
Lithuanian yOe/'-yc'i/s//"umgurten'); 

derivatives are: 

Gothic fairra NdN. "afar', as preposition "fern from'. Old Icelandic fjar{ri) Adv. "afar' 
(therefrom Kompar. firr, Superl. first). Old English feor(r), engl. far. Old Saxon ferr. Old 
High German ferrofKdv. "afar, very', Kompar. ferror {*fer-ro- iroru *fer-ero-); Old Church 
Slavic pred-b "before; voran; das Vordere' (as na-di^, prezh "about - toward '; -/roAdj.: 
prel^t "quer', Czech pi'fc(l<a)^ transom ' = Umbrian pe/ra/77 "virgam', Oscan perl<[ais] 
"perticis'; 

in zeitlicher Verwendung: Old \v\d\c par-ut, gr. nspuai etc. (see below uet-'year') and die 
derivatives Lithuanian pernai"\n vorigen years', Latvian perns Ad], "the previous year, firn'. 
Middle High German verne'the previous year', vern^\n vorigen years', Gothic only in af 
fairninjera'oiWor]a\r\re', Old Saxon fernun gere, fernun iara^\n Vorjahre', therefrom with 
„/b-forms Gothic fafrneis^-naKa\6(^ , Old Icelandic fyrndt "age'. Old High German firni^o\d; 
wise'. Modern High German F//77"old snow'; also to zero grade Gothic faur: Old Icelandic 
forn'o\d', besides the /-stem Old Saxon an furndagun. Old English fyrn, firn ^o\d'; compare 
Old Indie purana- "vormalig' to pura, ap. paranam " previously, in the past ' to para, Latin 
perendie^ the day after tomorrow ' from *peren-diel 

Maybe in -e- grade Latin Greek Albanian: Latin perendie {* peren-dies) " on the day after 
tomorrow ' : Albanian {* peren-diem) perendim m. " sunset, end of the day ', perendimi' 
west ', {* peren-destia) perendestia^ upper goddess ' {*peren-dea) perendia^ divinity '. 
Albanian {-dea, -desha^ goddess ' : Latin dea: Italian dea: Spanish diosa: French 
deesse : Portuguese deusa " goddess '. 



auf per- \n other Verwendung point at *per-u-r/n-\n horn. irsTpap (Pind. n£Tpa(;), 
n£ipaTO(;, Attic n£pa(;, -aTO(; 'ending, end', horn, direipajv ' eternal, infinite ' = (Attic) 
dnspova nspac; fjr| exovtq Hes., horn, nsipaivu), Attic TTspaivu) ' vollende '; - besides in Old 
Indie eine gleichlautende family the meaning 'knot': Old Indie pan/a- Nom. Akk. PI. n. 
"knot, joint ' (instead of *pan/j), paru-m. 'knot, joint, limb, member (ocean, sky, heaven)', 
parus-n. 'knot, joint, limb, member'; gr. nsTpap 'knot' is doubtful (G. Bjorck Mel. Boisacq 1, 
143 ff.). 

b. Adj. pero-s lurther': Old Indie p^^a-/? 'further, jenseitig, fiend; prior; later', Superl. 
parama-h lernster, last, best', Avestan ap. para- 'ulterior, the other, spatere, kijnftige', 
para-tara-l\en6'; Old Indie pa/'a/? (Nom. Sg. m. with adv. End stress) preposition m. Akk. 
'about - out', with Abl. 'fern from', with Instr. 'beyond from', seldom adverbal = Avestan 
paAd preposition m. Akk. 'besides - apart from'; Old \n6\c para, Avestan para {\nstr. Sg.) 
adverbal 'fort, weg, zurSeite'; Old \n6\c pare {Lok. Sg.) 'darauf, fernerhin'; Old Indie yoa/'a/r? 
(Nom. Akk. Sg. n. = Osean perum) 'out about, beyond, after', preposition with Abl.; 

Armenian /7e/7"remote, distant, afar'; 

gr. n£pc((v), Ionian nspnv (Akk. Sg. f.) 'daruber out, beyond'. Adv., preposition m. Abl. 
(Gen.); Latin per-peram^ inverted ', per-perus^ ineorreet ', from which gr. TT£pTT£po(; 
'Geek'; gr. TTspd 'daruber out, beyond' (Instr. Sg. f. of stem *pero-= Old Indie yoara' away, 
in another plaee, fort') ; therefrom n£paTo(; 'jenseitig' (TTspaiTspoq), nspaGsv 'from beyond 
her', Tfi nsparn (yfi) 'gegen Westen'; 

from a sehwundstufigen additional form from nspa through -/ro- extended is delph. 
npaKO(; 'with e. Geldstrafe covered', Ionian npnaaw Attic npaTToo 'durchfahre, vollstrecke, 
vollfiJhre, verriehte, do'; 

Osean perum (= Old Indie param) 'sine'; 

Old Irish l^e 'further, langer' {*perio-, das /"after s/?'long'); 

Hittite para{= gr. nspd) 'vorwarts, further, further', postposition 'from - heraus'; periia(n) 
'daruber out', postposition 'about - out', parranda 6s. (*= gr. nspav + 5£). 

e. prai, per5/(Riehtungsdativ of stem pei), also prei, pri, peri.
```


## [2026-09-14T00:50:40.341Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '66947,67130p' POK_full.txt",
 "description": "Print Pokorny per-2 B/C/D/E"
}
```


### [2026-09-14T00:50:40.392Z] TOOL RESULT

```
Root / lemma: per-2. B. per-, pera- 

Meaning: to carry over, bring; to go over, travel 

Note: not certainly from per 2: C. to separate 

Material: Old Indie /0/p5/"//"fuhrt hinijber, geleitet, furthers, ijbertrifft', causative parayati^ 

places about' (= y05/aya//"schutzt'), Avestan par-{\N\Vc\ Prafixen) "hindurch-, hiniJbergehen', 

Kaus. -parayeite. Old Indie yoara-'hinuberbringend, iJbersetzend', m. n. "jenseitiges bank, 

border, shore, purpose, aufterste limit, boundary' (in addition parya- 'wirksam'), Avestan 

para-vn. 'bank, border, shore; limit, boundary, end'; 

Armenian /7c»/(0'"begangen, betreten', hordan^ leave, depart ', hordantam^ allow to 
leave, depart ', and /7e'/7^/7'Pfrieme'; thrak. n6po(;, -napa in place names = gr. n6po(; 
■ford'; 

gr. nspau) 'dringe through ', nsipw (TTsnappsvoc;) "durchdringe, durchbohre' (= Church 
Slavic na-perjg), 5iaiJ-n£pr|(; 'durchbohrend', nspovr) 'cusp, peak, sting, prick, clasp, 
hairpin '; TT6po(; ' passage, Zugang, junction, ford; Ausweg; PI. incomings ', hom. nopeTv ' 
obtain ', Aor. snopov; nsnpwTai 'is, war of Schicksal bestimmt' ( *pf-), nopsuoj 'lead, guide, 
obtain ', Med. ' travel, journey', nopi^w 'grant, bestow passage; obtain ', TTopGpoc; 
'Uberfahrt, Meerenge'; 

alb. pruva, prura 'brachte, fijhrte', 5/7-yOo/ioy 'durchbohre, durchsteche' {d/s-+ *pera-id), 
sh-poj, tsh-poj, sh-puay^6s., durchbreche eine wall, breche ein' {dis-+ *pereid), sh-pie 
'lead, guide hin' {*sem-+ *perd)\ pirr(e)i. 'thorn' {*per-na) etc.; 

Maybe nasalized {*pera-idnd) alb. perend/m ^ sunsei, west', perendi, perendia ' goddess' 
[common alb. n- > nd-] : Middle Persian: xwarofran, (Man.) xwrwpr'n^s\}v\se\., west' : 
Avestan: paratu-{vc\] 'crossing, bridge'; OAv. (fra)fra{\sq.sub].aox.3iCt] 'to cross' ( Y 



46.10); LAv. fra-para/7a/jhe [2sg.caus.sub\.ac\..] "to bring over' ( Yt 71.16); ni-paraiieinti 
[3pl.caus.act.] "to lead to' 

Latin porta, -are'bear, carry, guide, lead, drive, bringen, offer', Umbrian portatu 
"portato', yOO/:^i/5/"portaverit' ( *poritd, to an iterative *poreJd)\ 

Gothic faran, for^ wander, pull, drag', farjan^6uye, schiffen', stem V. Old High German 
Old English faran. Old Icelandic /^as "drive', schw. V. Old Saxon ferian. Old High German 
ferien, ferren. Old Icelandic /fe/ya "drive, schiffen'(/&/75/7 = *poreid)\ Old Icelandic fQr\. 
'journey, Fahrt', Old English faru\. "Fahrt, journey, pull'. Middle High German var\. 'Fahrt, 
way, kind of, way' (fem. to gr. n6po(;); Old Icelandic farmr. Old English fearmm. "shipload', 
Old High German farm " bark, type of sailboat' (= russ. porom); lengthened grade Kaus. 
Old Saxon forian. Old High German fuoren. Modern High German fuhren. Old Icelandic 
f0ra6s.. Old English (as Iter.) feran^qehu, pull, drag' (= Avestan parayati. Old Church 
S\av\c par/f/); Old High German fuoraTuhre, Fahrt etc.'. Old English fori. "Fahrt, cart '; 
Old Icelandic f0rr lahrbar, suitable ', Old High German gi-fuori^ fitting, comfortable, useful 
'; Verbalabstr. Old Icelandic ferd. Old English fierd. Old High German Middle High German 
fartTabr^ {*por-ti-); 

russ. -Church Slavic na-perjg{= Treipw), -yOeA/Z/'durchbohren'; perg, p-brati^i\y'\ Iter, pariti 
"fly, schweben' (= Old Indie parayati, Germanic Jorjan); pero^ feather '; russ. porom, 
Serbo-Croatian pram^ ferry ' (= Old Icelandic farmr); presumably here also Old Church 
S\ay\c porjg, yO/a//" carve, slit'; about Modern High German Farne\.c. s. addendum S. 850. 

per-tu-, por-tu-, Gen. pf-teus^ passage, ford': Avestan porotu-sxxx. f. (Proto Aryan *prtu- 
s) and pasu-src\. (Proto Aryan *prtu-s) " passage, ford, bridge' {hu-para^wa-' good to 
overstep ' = "Euphrat'); Latin portus, -Js"Hausture' (XII tab.); " harbor', angi-portus 
"narrow Passage, Nebengaftchen'; besides a-stem porta ^Siadiior, gate' = Oscan [pjurtam; 
lllyrian PN Nau-portus, gall, ritu- "ford' in Ritumagus, Augustoritum, acymr. n't, ncymr. rhyd, 
corn. A/rford'; Old High German furt. Old English ford^iord' (zero grade Old Icelandic fjgrdr 
"narrow gulf, bay' from *per-tu-s); besides f. /-stem in Modern High German PN Furth 
{*furti-). 

Maybe alb. porte'door' derived from Latin porta'gate', port 'harbor' derived from Latin 
yOC»/:^^s 'harbor'. 

addendum toS. 817: 



To Church Slavic pero " feather ' belong *por-no- " feather ' in Old Indie parna-v\. " 
feather, leaf, Avestan parana-v\. " feather, wing'. Old Saxon Old High German farn 
"Farnkrauf (*Federkraut), Old English fearnm. 6s., Lithuanian sparnas, Latvian sparnsm. 
"wing' (das s-from the root spher-); 

*prati-s\n gall, ratis. Middle Irish raithi. 'Farnkrauf, bret. /'ao'-e/?/? collective ds.; 

*po-port-io-\y\ Lithuanian papartis, papartys Tamkraui', Latvian paparde, paparske (is.; 
with lengthened grade Slavic *paparti-\. in russ. paporotb e\.c. ds. 

WP. II 21, Trautmann 206, Vasmer2, 313. 

References: WP. II 39 f., WH. II 344, Trautmann 206, 215 f. 
Page(s): 816-817 

Root / lemma: per-2: C. per-, pera- 
Meaning: to sell 

Material: a. Gr. nspvriMi (present and Impf.), nEpaw, -u) (formal = nspaw "dringe through '), 
£n£paa(o)a, and nirrpaaKU), nspaou) (Attic nspoj), Enspaoa, nsnpaKa 'verkaufe', (gr. 
stem *pera-), nopvp 'meretrix'; Old Irish ren{a)/d ^s/erkauit' {*pr-n9-: gr. nspva-), Konj. 3. 
Sg. -/7a-(*/7a-after Indik. *[p]ri-na-ior "/b/e/'a-eingetreten), Perf. 3. Sg. -rir {*ri-r-e); verbal 
noun reicc{Da\..) 'Verkaufen' (in final sound after /cc "healing, payment ' directed); 
compare with an old guttural-extension Lithuanian perku pFrkti' buy '. 

p. Avestan pairyante^sxe become compared', a/p/'-par-' {se'\r\e blame) begleichen, 
penance, atonement make', a-psrst/'-s' atonement ', pdrs^a-n. " equalization of (blame), 
atonement, punishment ', para- m. "blame' (in addition probably also par- "verurteilen'); 
Latin p5/'(lengthened grade), yC>a/7s"gleichkommend, alike, pair', therefrom paro, -are 
"gleichschatzen', comparare^ Q,oxr\^ax€ (Umbrian pa/'ses/'paresf has das sfrom mers 
est). 

y. Old Indie purta-u., purtf- f. "earnings' = Latin pars, -tis "parf ( *pereti-), port/o^part, 
allotment ' (Post Classical; Classical only pro port/one, assim. from * pro part/one); Old Irish 
rann, cymr. rhan, mcorn. ran, abret. PI. rannou^parV ( *per9-sna); (common Celtic -ns-, -nt- 
> -nn-). Old Irish ern(a)id^ grav\{s\ Konj. r-a-aera^ex moge esgewahren', preterit ro-fr^ev 
has gewahrf ( *per-e), Fut. *ebraid{ *pi-pra-s-e-tf); ro-rath^\s gewahrt worden' ( *pra-to-l\, 
Hittite Paz's- "break, rupture, grind, split up, cut up, divide'. 

References: WP. II 40 f., WH. II 250 f., 256 f., 257 ff. 



Page(s):817 



Root / lemma: per-2. D. per- 

Meaning: to bear (child) 

Note: (as fera 'gebare' in einstiger reiationsliip to per-2: C "allot') 

Material: a. Latin pario, -ere, peperT, partum, pariturus " to give birth to children ', reperio, - 

Tre, repperJ, repertum'\N\edefi\nden, find, learn', partus, -us' to give birth to children, birth; 

foetus', Parca {*par/ca) originally 'Geburtsgottin', Propert/us actuaWy "the FriJhgeborene' = 

Umbrian Propart/e 'ProperiW, pare, -are'bere'\\.e, acquire, buy', comparo' buy' ("sich 

etwas besorgen, obtain '); //77/?e/'5/'e 'anschaffen = order'; 

Lithuanian per/u, peret/ "brute', peraTHom. PI. "Bienenlarven'. 

(3. Old Indie prthuka-m. 'rother, cattle, calf, the young of an animal ', Armenian ort', -u 
"calf of Rindes or Hirsches' (with formants -thu-)\ gr. nopiq, nopra^, nopiK; "calf, young 
cow'; cymr. e/'//7j//"abortus'; Old High German far, farro. Modern High German Farre, Old 
English fearr. Old Icelandic farri {*farz-) "bull', with gramm. variation Middle High German 
verse. Modern High German Farse "young cow' (Germanic *farsT, Gen. *farsjds), to Old 
English heah-fore, engl. heifer, originally from jungen animals, compare engl. farrow^uoi 
pregnant'. West Frisian fear^qeW!; lengthened grade Old English for. Middle Low German 
KO/'"Schweinchen'; Old Church Slavic za-/0/^/b/rb "wind-Ei', Czech s-pratek Iruh 
geborenes calf, kir. Kj/-pc»/:^c»/r"Fruhgeburt'. 

References: WP. II 41 f., WH. II 255 f., Trautmann 215. 
Page(s):818 

Root / lemma: per-2. E. per- 
Meaning: to try, dare, risk; danger 
Note: (= /Oe/'-"hinuberfuhren, durchdringen') 

Material: Armenian yC>"c»/7"Versuch' (express, p"-); gr. nsTpa f. "Erfahrung, Versuch', Aeolic 
nsppa (*n£pja), nsipau), -a^u) "versuche', £|jTT£ipo(; " skillful, smart, adroit'; Latin experior, - 
/?/""versuche, prijfe', expeffmentum "Versuch, examination ', comperid, -/?e"erfahre genau', 
opperior, -Iff, -Itus {and -tus) s^/r? "warte, expect ', perJtus" skillful ', perTculum^M ersuch. 
Probe; danger; Prozeft; accusation '; das /"from perT-tus, -culum derives from den 
compounds with -perior. Old Irish a(/)/'e"Wachen, attention', nir. faire, because of gallo-brit. 
areanTP\. "Kundschafter' from * psreja, Germanic '7^/7/73- "das Auftergewohnliche' in Gothic 
fairina\. "blame'. Old High German firina" crime ' etc.; Germanic Yera- "danger' in Old 
Icelandic farn. "danger, misfortune'. Old English /^/"m.. Old High German far(a)" 



pestering, temptation; snare, danger', to GotJiic ferjaxr\. "Aufpasser', Old Higli German 

/^/'e/7"auflauern' etc.; perhaps in addition with Abtonunggr. TaAai-nwpoq " afflicted ' as 

"Gefahren erduldend'. 

References: WP. II 28 f., WH. II 288 f. 

Page(s):818 

Root / lemma: per-3, per-g- 

Meaning: to hit
```


## [2026-09-14T00:51:03.097Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT peretu ===\" && grep -n -i \"p\\(ə\\|e\\|a\\)r\\(ə\\|e\\)tu\" BRT.txt | head -20; echo \"=== BRT huparethwa ===\"; grep -n -i \"hupar\\|hu-par\" BRT.txt | head -20; echo \"=== BRT parena ===\"; grep -n -i \"^par\\(ə\\|e\\)na\\|parana-\" BRT.txt | head -20",
 "description": "grep Bartholomae"
}
```


### [2026-09-14T00:51:03.200Z] TOOL RESULT

```
=== BRT peretu ===
=== BRT huparethwa ===
17773:mit  ava  und  >tl  Kaus,  'Jemanden  weg und  nach  Haus  fliegen  lassen,  im  Flug heimkehren  lassen':  fä  (näml.  fravasays) dim  ava  nifrävayenle  mqnaym  ake  yäha ttä  trur^ys  huparfnS  (sd.)  Yt.  13.  ^o.
21129:/ravayente  mqnaytn  ahe  y  nä  mfrr/ö\ huparms  (sd.)  Yt  13.  70;  —  täpayeiti mqm  asa  vahi^ta  ntqnaysn  ahe  y' ayaoxsusUm  ". ,  ab  wäre  es  geschmolzenes Eisen"  Yt.  77.  ao;  ao.  2)  sie  geht  auf
30304:Pü. :  mkirU. •  j.  hu-parana-  Adj,  'wohlbeflügelt':  th dim  ava  nifrävaymte  mqnaym  ahe  ydha nH  jmrr/S  'nS  ". .,  gerade  als  ob  man (es)  ein  wohlgeflügelter  Vogel  wäre"  Yt 13. 70.
=== BRT parena ===
5859:•  j.  asparana-  m.  Name  einer  Münze*>: °nS  F.  7;  —  duye  AazaaraAe  'nam  nidmat Vd.  6.
7721:•  j.  «rszifyö.parana-  Adj.  'mit  Adler- fedem  besetzt":  isavasca  'na  V.  77.9;  Yt. /0.39,   lOI.
9251:srayä  voumkaiaya  Y,  65. 4;  —  ys  haaiay-j  S/-'^v^'^'jU^'ond''zD"'"w',/irLter ...va  uruassayat  '«o»  Yt,5.  131;  —  ^-i  HriÄ^-^  No^T).  -  mp,  fl'ü.  Tu  V.'s  49" rasmanS  hqm.ststse  (sd.)  ^5  ^'na  ">  J'  karkäi,  vgl.  np.  (Npa,)  kargas. iHndayänti  Yt,  jj.  39;  —  yaoz)nH  »aA'«j.*kahrkäs5.parana-"  Adj. 'mit  Federn •«ff  (NP.)'>  rasmans  Ytio.36.  2)  zeitlich  ^  des  (Vogels)  Kakrklsa  versehen':  isunqm (nur  Komp.).  ^-paranum'^  Yt/o.isg.
15412:ASn.  aus  'parana-  Adj.  'vormalig';  s.  'para, parö.  —  ai.  vgl.  puräriä-  Adj.
15704:•  j.  parana-  n.  1)  'Feder":  mirrjahe  .  . vHrmßnaAe  (sd)    'tarn   ayasaisa   .  .  ana
16082:•parana-
16127:rä.:pur  atäs  i  kar  i  däiasiän.  l  •  j.  'parana-  m.,  n.  i)  'Feder':  cataurS
16201:•  '].  pflSö-parana-  Adj.  'des  Federn  weit
17913:frasparana-  1 00a
17931:•  j.  fra-8parana-  Adj.  'mit  den  Füssen ausschlagend':  usirahe..  'noAe  \tl4-ii.
30304:Pü. :  mkirU. •  j.  hu-parana-  Adj,  'wohlbeflügelt':  th dim  ava  nifrävaymte  mqnaym  ahe  ydha nH  jmrr/S  'nS  ". .,  gerade  als  ob  man (es)  ein  wohlgeflügelter  Vogel  wäre"  Yt 13. 70.
```


## [2026-09-14T00:51:04.626Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD puhl ===\" && grep -n -i \"puhl\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD bar shore ===\"; grep -n -i \"^bar\\b\\|bār\" PHD_mackenzie.txt | head -30",
 "description": "grep MacKenzie"
}
```


### [2026-09-14T00:51:04.689Z] TOOL RESULT

```
=== PHD puhl ===
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:586:Sóymand 81 tanüpuhl
PHD.txt:590:tà [OD < A “d | (M d’), N ~] until; so that. tab [tp | N ~] fever. tab-, —išn, v. taftan. tüb- , ~išn, v. tāftan. хабар [r5k! | N taba] frying-pan. tabāh [tp?% | N ~] ruined, spoilt, destroyed. 7h : ruin, destruction. tabāhīhistan, tabāhīh- [tp’hyh-sin' | J th’hh-] be ruined. tabangóg [ipngwk! | N tabangó] box, chest. tabarzad [tpizt' | N ~] manna. tābestān [P stn! | N ~] summer. tábidan [P 5ytn! | N ~] = tāftan. tadan, tan- [itn!, tn- | N tan-] spin (thread). tadar(w) [ttl | (N tačarw)] pheasant. taftan, tab- [tp-tn'] grow hot; shine. —išn: heat, fever. táftan, tāb- [2°p-tn' | P РЬ-, N ~] heat, burn; shine. ~išn: burning. taftīg [tptyk' | (P tft)] burning, ardent, fervent. tag [tk' | N ~] running, attack. — kardan abar, ó: attack. мар (Pk! | N ta] item, unit; alone, single. ңар [Ok | N tā] branch. tagarg [tklg | M erg, N ~] hail. tagig [tkyk!] swift, strong. ~ih: speed, strength. tah [th | N ~] bottom. tak6k [tkwk! | N ~] drinking vessel. talag [t/k' | N tala] snare, trap. ~-€in [-cyn'] fowler. tambiir [tm-, tnbwl | N ~] cither, lute. ~ag [-k'] tambour (?). tan [tn' | = M, N ~] body, person. tan-, v. tadan. *tanāpuhl [tr?pwhl = Av. tanu.parada- | (N tanáfür)] a degree of sin.
PHD.txt:882:atone toxtan; cause to ~ puhlēnīdan.
PHD.txt:883:atonement puhl, tēzišn.
PHD.txt:1088:bridge puhl.
PHD.txt:1847:expiation puhl, tēzišn.
PHD.txt:3287:punishment drēš, pādifrāh, puhl.
PHD.txt:3662:sin abārēnih, āstār, bazag(ih), mān- dag, wināh; degrees of — āgrift, anābuhlag, arduš, bāzāzanišnih, framān, ēyrišt, tanápuhl, xwar, yüt; cause to — āstārēnīdan.
PHD.txt:4496:tuhig tohmag tanapuhl tuxš- tuxšagih tuxšag i tuxšīdan tuxšišn tēxtan tuwānāg tuwānīgīh tuwānīg tuwāngar tuwāngarīh tuwān tuwānsāmān tambūr tambūrag did!, tand, tang tandih, tangih tanigardig tanigard tan
PHD.txt:4718:[154] 1-2pešag 1 V. pēšpārag S eoo petyāragīh AS dax sa) petyārag ҳу 10 paydāgīh ^0 з» 10303 paydāgīh- = 95747 №0 paydagihistan 1152294 3” е 0 paydāgēn- = 527310500 paydāgēnīdan ММ 8” 5 05 paydag 15? ye» о) paygām -È ve os paygāmbar Sye Yeso petitigih A3 4) M 4290) petītīg 14) 95 1050) petit 12d уез 0› **pid we es panāh ^U? 103 panāhīh AY 10) "oul PITT puhlén- = "yes 10) puhlénidan ure rne 19у frāz erie pēhišn IMO” tay poxtan ure 125 nem! 519
PHD_mackenzie.txt:1766:~eh-widarag [cyhwtlg] = ~inwad puhl.
PHD_mackenzie.txt:1794:~inwad [cynw(p)t l ], - puhl: the 'divider bridge' which separates the
PHD_mackenzie.txt:4270:Ipuhl [pwhl I N pull bridge.
PHD_mackenzie.txt:4271:2puhl [pwhl] expiation, atonement; punishment.
PHD_mackenzie.txt:4272:puhlenidan [pwhlynytn'] cause to atone.
PHD_mackenzie.txt:4902:  • tanapuhl [tn)pwhl = Av. tanu.pmJ8a- I (N tanafur)] a degree of sin.
PHD_mackenzie.txt:6004:atone toxtan; cause to - puhlenidan.     bark post, toz.
PHD_mackenzie.txt:6005:atonement puhl; tozisn.                  barley Jaw; Jawen.
=== PHD bar shore ===
1492:bar [bll N ,,-,] fruit, produce, profit.
1493:bar-, ,,-,iin. v. burdan.
8981:bar-I
11091:bar~
```


## [2026-09-14T00:51:13.475Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT Brücke ===\" && grep -n \"Brücke\\|Bnicke\\|Briicke\\|Brucke\" BRT.txt | head -20; echo \"=== BRT Euphrat ===\"; grep -n -i \"Euphrat\" BRT.txt | head; echo \"=== BRT Ufer ===\"; grep -n \"'Ufer\\|Ufer,\" BRT.txt | head -20",
 "description": "grep Bartholomae German glosses"
}
```


### [2026-09-14T00:51:13.546Z] TOOL RESULT

```
=== BRT Brücke ===
11367:—  nava.naptyae{&d)iit  ht  urvätum  para.- tmrntiaiU  V,  JJ.  3 ;  —  yasüa  ml . .  bayqm ahunahe  vairyehe  .  .  yazäite  %rTiüi  tarö p?r>lümati^'^.y)ixa^  h! urvätam  vahistim ahUm  frapärayetii  "wer  . ,,  des  Seele  will ich  sogar  dreimal "'  über  die  Brücke  . . führen"  Y.  z^.  6;    —  yat  na  kasvikamlii
11424:•  j.,  g.  finvant-  Adj.  'scheidend',  nur  GS. °valä  mit  p>r»tav-   oder  p?sav-^  'Brücke
11579:Zum  V.  'ga)!:  — ■  Pü. :  fia  rasiSn  S  t/ilarai  u nyäyiia  i  imät  räi  'beim  Kommen  lur  Brücke und  wegen  eures  Preises',  erl.;  läi  ka  5  änik räsäni  am  nyäytim  5  smäi  titvän  bavSt  karlan. —  I)  Dh.  sobald  der  Preis  der  Götter  inge- stimiut  wird,  schirrt  sich  ihr  Wagen  zur  Her- fahrt.
13825:•  j,  duzäpya-  n.  'Schwer-,  Unbeikömm- lichkeit',  mit  Akk.  (des  Obj.):  yaesam anhat  'fim  änval.psntum  "für  welche  die (^-Brücke  schwer  (beikömmlich,  sva.)  _un- überschreitbar  sein  wird"  V.  y,  3.
15348:hmuber   gehen';    i)   'über  -'  (Akk.):  /re'     ^i  ^^ni)'fjrj','};  (.0  nj:   -a".  "ch  V' /j/'/  vJsfäis  cimatO /ra/ra  (iSK.)  p^rptüm       (\'.  ♦  5\  ;^'j>  ^-  S'-  ^S-  JiJ-  *)■  —  '>  Pü,: "mit  all  denen  werde  ich  voran,  htnüberj     fehlt;  s.  No.  2.  —  »  So  Y.  jj-,  7;  s.  No.  i. Über   die  Brücke   des   Scheiders   gehen" ;     ^s'"  ^'~'  -'"'■  \  "  ^'  ^i^'-  '^"'■ Y.  4Ö'.  10.  2)  'zu  -'  (Akk.  mit  ä):  usta  •  j.,  g,,  p.  "para  I)  Adv.  'luvor";  i)  lUum-
16069:•j.,g.p»r9tav-ra.,f.'*i) 'Durchgang,  Gang*: "tui  F.  JO;  —  frabm?m  daiähsus  nava '%ioS  (AP.)  k»r?nai'a  "in  der  grössten  Ab- teilung des  Bezirks  mach  neun  Gänge ((L  i.  Abteile)"  V.  2. 30";  —  fraUtmm °^wd  (AP,)  Aazavnm  narqm  näirinanua taoxma  upa.bara  "in  die  Gänge  der  grSssten Abteilung  bring.. "■V.2.3o'>,  2)'^gang, Pforte',  mit  z^mS  'Pforte  des  Winters',  Name einer  Örtlichkeit:  ndt^  tä  im  xsnäus  vaipyS (sd.).,V?(LS.)  t?mB\.5i.  1 2.  3)  'Durch- gang durch  — ,  Übergang  über  das  Wasser, Furt,  Brücke':  afqmca  -/«/(AP.)  Y.42.1; —  apqm  .  .  nOvayanqm  patti  °tül  Yt. II.  4.  a)    mit    GS.    Smiatö  (sd.)    'die
16070:Brücke  des  Scheiders'  (beim  letzten  Ge- richt): Ayat  aüT^gpirun  yd^rä  ^vatJ  °tui "wenn  sie  dahin  kommen,  wo  die  Brücke des  Scheiders  ist"  Y.4Ö".  11;  —  frS  toii vispsis  cinvats  frafra  (Sp,  851  m.)  'tum \.46. 10;  —  tarS  änvats  °tSm  Y.  71. 16, V.  7p.  30;  Vr.  7.  i;  — yeiya  urvä  xraodaUl änvatJ  'tä(l£,.) aia(s��)Y.5i.i3.  a)dn. auch  ohne  cinvatB  'die  Brücke'  Kar'  i^,: hrlicit  (Sp.  591  m.)  tarS  'tümcit  la  urväram vahistfm  aÄsm  frapärayem  Y.  ig.  6.
16177:•  j,  p«äav-  m.  i)  'Durchgang,  Furt': husk?m  °ium  ralcayat  tarS . .  vltatiuhaitim Yt.  5.  78;  77.  2)  'Übergang,  Brücke, Brückensteg':  W/  hapta  'savS  (als  AP.) fraoirisySil    tarasia    äps    nävayä    V.  14,
16207:•  j.  paäu.päna-  Adj.  'die  Brücke  (/car"  i£.) behütend,  bewachend',  von  den  beiden Hunden,  die  ab  Wächter  an  der  Cinvani- Brücke  stehen;  naita  späna  'päna  (ND.) paiti  irista  i^2flift'"noch  werden  die  Hunde,
16208:I  die   beiden  Briickenwächter  bei   (seinem)
16447:—  '^nm  a?m  narff  varsta  "d^r  Mann  hier ist  der  Erzeuger  des  Kindes"  V.  75. 13; Yt  77.  58;  —  gaohan>m  ..yat  asti  "'iirahe %rimö  W.21.T,  —  aäaüa  aSfä  yä  kaine aitahmai  '"^rä^  (statt  AS.)^*  mimarsxiaite (sd.)  V.  75. 14;  14;  —  fravasayö  .  .  ya ban'hrisva  "ä«  (als  AP.)  *>  vföaraym  paitt- V3r3te  Y.  23.1;  —  käirisls  '^ri  (AP.) vprmvamii  Yt/^.  15;  11,28;  —  ya'ia Vihrks .  .  barii^ryäl  haca  "'iirim  nizdar».- dairyäi  Y.iS.^Z;  —  äat  hl  'hrqm cahwarS  tnähyanamca  upa  dasa  ayaranqm nSie  iavai/i  {s.  Sp.g32  o.)Yd.ip;  —  ahmät "'iirqs^^  daläiti  Vyt 34, 4(';  —  "pa  hs ''hnm  fradalat.  .yahmat  haca  °irif  haom urvämm  Snvatp3r>tüm  *i-toarayal  "so soll  man  ihm  (dem  Sterbenden)  einen  Sohn geben  (adoptiren),  damit  der  (adoptirte) Sohn  dessen  Seele  über  die  Brücke  des Scheiders  hinüberbringe"  Vd.2*>;  ij;  — ava^a  .fe  .*^a/?(sd.)  "ärwi  ar^hat  Vd,  2; V.72.  8  Gl,;  —  yat  ^aÜS  anhat  naimi.- raha  (sd.)  -Sr«  (statt  DS.)  daoäiti  Nik. 3,  a)  auch  von  Tierjungen:  iis  hapta
22693:*)  Die  S.  /.  21  mit  Ramait  in  Beziehung  ge- setzt wird»).  V. /p.  13  steht  der  Name  hinter &Jiij!a  und  Zrvan  und,  durch  eine  Anrufungs- Tormel  getrennt,  vor  Väla.  Der  Gottheil  ist das  junge  Machwerk  Yt  1$  gewidmet,  dai  irr- tümlich räm  yail  genannt  wird.  —  Die  mp. Schriften  kennen  einen  guten  und  einen  bSsen Väy  fväy  i  veA,  v3y  i  vailcir),  von  denen  gesagt wird,  dass  aie  bei  der  D'm'iir>/-Briicke  um  die Seelen  kämpfen  (Me.  3.  w^).  Es  scheint  mir aber  nicht  notwendig,  darum  'vaytOf  und  'vayav- gleichiutetien  und  in  den  beiden  'the  personi- ficaiions  of  ihe  Upper  and  Iower  air'  (Wbst SBE.  37.  224)  »u  sehen.  Im  Awesta  ist  *on jener  Tätigkeit  des  aA«Hschen  Vayav  nirgends die  Rede.
25030:KompA.,  E;  Ableit.  —  Vgl.  h-alav.  ~  Et.? Wohl  lu  *atla-,  iBild.  vgl.  xralav-.—  Gdn.s Versuch,  iwitchen  '?■■  'Zeit'  und  =r"  'Richter' eine  Brücke  zu  schlagen,  KZ.  jo.  325,  halte ich  für  verfehlt.  —  Pü.:  ral,  raßh,  erl.  (oft): datlmaar;  Sü.!  gu'i'fy,  gurutä,  gututvam\  s. noch  No.  2-7,  9,  13  f.  —  't  So  luletit  Gdk. KZ.  $0.  325;  aber  BB.  1$.  252  übersetit  er wieder  'Meister';  i.  ferner  Haug  Essays' 327 Cjadge'),  JN.  A  hymn  23,  DsT.  ZA. /.  7,  123. Vgl.  ^ähü-  mit  No.  1.  —  ')  Pü.:  ii  tö  sösfand\
25564:bringen': hävana  fraoirisimna  fralä- vayamna  Vr. /2.  5;  —  bi!  hapta  pi^avS fraoiriiysil  taraiia  äpo  navayä  "zweimal sieben  Briickenstege  soll  er  hinzubringen (sva.  anbringen,  legen)  über  . ."  V.  14. 3)  'sich  ab-,  wegwenden  von  — ' (pairi  mit  Abi.):  yat  fraoiriiaiti  pairi dusmataliöyas^a  . .  H.  /.  1 7.  4)  'heraus-
28677:•  j.  haetav-  m,  'Damm';  ha  aSaunam urvänö  . .  tarö  cinvatS  p^niSm  vT%arayaii 'tu  (LS.)  mainyavanqm  yasatanam  ". .  bringt die  Seelen  der  Gerechten  .  .,  über  die Brücke  des  Scheiders  hinüber  zum  Ufer- damm der  himmlischen  K"  V.  ig.  30.
28678:Ableit.  —  ai.  lilav-  m.  'Damm,  Brücke, Schranke';  ooss.  jtu'.'woss.  jrnf -Brücke',  PDs. ytid,  yn.  ilk  'Steg',  —  Pü.:  *■//.
29083:urvsnS taras^a  haram  b)nzaitim*iisnaoiti tarS  cinvats  p>r>tum  vilärayeiii  haits  (sd.) "sie  bringt  die  Seelen  . .  —  über  die  hohe H.  kommt  sie  heran  —  über  die  Brücke  . ," V.  75.30.  a ) 'erreichen,  ersteigen' :f(i»W- nqm  (als  Obj.)  asai^shranqm  *3snaoiti'^ mi^r»m  (statt  NS.)  V. /p.  28.
=== BRT Euphrat ===
8492:•  j.  urvä-"  f.  Name  eines  Lands,  (nach Pü.)  Muene  (Misän)  im  Euphratdelta'*: astJm^m  asaahqmca  .  .  /ra>w?r?i?m  .  . 'vqm  pourv.västrqm  V. /.  10.
=== BRT Ufer ===
13715:•  j.  dürae-pära-  Adj.  (fem,  °rä-)  'des Ufer,  Grenzen  in  der  Feme  liegen':  ai^A^ z?mS  yat  pahanaya  (sd.)  skannaya  'ray'i YL  JO-95;  //.  19,  5-38;  —  ranhaya  'raya Yt.  14. 19;  —  raahqm  'rqm  "  Az.4,  *Vyt2.
16022:•  j'j  P-  ^pära-  in.  1)  'Ufer*.  a)  'Grenze, &u)e'.
16027:Eig.  {lii  Komp.  mit  AS.  im  i.  Glied)*)  'das Ufer,  dl«  Grenie  f*J/üro-)  Bberschreitend (*tara-)'.  —  Pü. :  paräniar.  —  i)  So  N.  li.  — »  K  1,  L4i  NA.  V<jw.  —  J)  Jf  I,  Mf2;  NA. '/ar).  —  *)  Vgl.  ai.  driihaiiitai-ä^.
24014:Zum  V.  lar:  —  ai.  vgl.  tärä-  m.  'Ufer';  mp. vitär,  np.  ^uiär  'Durchgang'  (s.  dain  Hbm. AGr.  7.  249>  —  Pü.;  vilast^).  —  O  So  nach DsT.  ZA.  3.  218;  anders  Rückert  u.a,  b. HORN  NpEt.  199.
```


## [2026-09-14T00:51:28.029Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16015,16035p' BRT.txt; echo \"-----PARA-----\"; sed -n '15340,15360p' BRT.txt",
 "description": "BRT pāra and para entries"
}
```


### [2026-09-14T00:51:28.090Z] TOOL RESULT

```
welch  beide  alle  Wesen  schufen"  Y.57. 3; —  *yaäi''>  %wsnltarä  Y.4S.2.
KompE.  —  Zum  V.  M^>.  —  »i.  fiäyäv-  m.  — Pü.i  fänak.  —  ')  Pü.  eil.:  mihr  oder  viiht yazal. VIL  sind  Mi%ra  und  Ahura  gemeint,  s.  Yt, 10,  113.  Anders  Gdn.  BB.  14.  17;  s,  unter %w5riiUr:  —  >)  Hds.  'yülcä  (so  NA.),  'yusia,
•  j.  'pira-  m.  'Schuld':  äa^a  masäayasnis ..spayeiti  anäpfrsh^m  syao'hn»m..d)mänB. p^rihtm  'rTtn  "die  m.  Religion  . .  nimmt auch  eine  Schuld  weg,  die  schwere  Sühne erheischt"  V,_j.  41;  F.  jo,  26;  - mudisbm  .  .  ^-ra ''  .  .  ^raSÜakcca  . .  *äst3- raiti  (sd.)  N.  g.
Zum  V,  yar-  —  aif.  fSr.  —  Pü. :  äpäm,  Npü. iart-   —  ')  nAi,f^a;  Fü. :  fehlt
•  j.  ^ära-  Adj.  'der  äusserste,  femste'{?); anuss  'r?m    marmm  (sd.)    avaMstät  V.
4-53-
VgL  *fara-1  —  Vä,: /rSitum.
•  j'j  P-  ^pära-  in.  1)  'Ufer*.  a)  'Grenze, &u)e'.
KompA^  E.  —  Zum  V.  ^far-.  —  ai.  pärä-  m. ;
y. pärayäl, pärayemli  usw.;  s.  ^ay-  (Sp.  15 1  f.) und   *par:     V.  /i).  aj;   lies  patrytle;    s.
■  j.  pärantara-,  pärantara-  ■>  Adj. i)  'abseits,  gesondert  gelegen':  "^räys antanca  (sd.)  *ava.anlara  *'ra  '>  (alsAPm.) mtTfa  fi-akuraydii  V.g.  11;  —  airtme gätBm  hl  »i/AiäaSa  ..*'rpm^  haca  anyait- bys  maedayasnaeibyö  V-S-SS;  —  pas/aSa ..msAiol'it,,*anlarvm(s,d.)  ar>%>m  mayahe *'ffm  3*  Aaca  anyasibyS  mayaiibyü  V.  g. 29.  a)  ASn.  als  Adv.  'abseits  von  — '
(Akk.):  stntazS  (sd.)  gairif  'r?m  arioO manusake  W.ig.T..  2)  'anderwärts  be- findlich': *yaa  tai  *apwataiti  (sd.)  'rim issii  ". .  soll  er  sich  anderwärts  an  einen (Lehrer)  wenden"  N.  12.
Eig.  {lii  Komp.  mit  AS.  im  i.  Glied)*)  'das Ufer,  dl«  Grenie  f*J/üro-)  Bberschreitend (*tara-)'.  —  Pü. :  paräniar.  —  i)  So  N.  li.  — »  K  1,  L4i  NA.  V<jw.  —  J)  Jf  I,  Mf2;  NA. '/ar).  —  *)  Vgl.  ai.  driihaiiitai-ä^.
•  j.  pär^ntartm  Adv.:  %. pSntUara-,
•  j.,  g.  pärvnday-  f.  'strotzende  Fülle, Üppigkeit:  3  äit  frat^Aärayat  .  .  sIryS mayä  •lA/w/iK'aa*"..  Weiber,  Beischlaf  und FüUe  herzubringend"  A,y.4{?)".  a)  als Gottheit";  aslm  .  .  ihm  .  .  äzüitlm  .  . frasastlm  varmhjm  *'dlm "  yazamaiäi  Y.
38.  2;  *y.  1";  —  rrvlm  *'älm''>  yazamaide Vr.  7.  a.  a)  sonst  mit  raf^raäJ-:  mihnm . ,  yim  halaite  aiil .  .  'di(SS.)ea  raora%a YtiO.66;  Ä38,  *Vyt<?;  —  •älm  raorahqm S.2.as;~  •dyA{GS.)  raorakaya  S./.äs. *}  Ober  deren  Bedeutung  Sicheres  nicht  zu ermitteln  ist;  vgl.  die  GrB.-Slelle  bei  Dst.  ZA. 2,  3:1,     Meist  erscheint  sie  in  Verbind ung  mit
Komp.  mit  AS.  im  i.  Glied;  %  165,  304  11. 10.  Zum  Schlussglied  und  iFlex.  s.  S  203, 313.  2.  Aus  ar.  '^pärandh';  dagegen  weist ai.  pürandhay  f.  auf  ar.  'ff''aiufk'.  Die  Be- deutung ist  unsicher;  vgl.  Bthl.  IF.  i.  184, RiCHTCR.  IF.  g.  247;  weitre  litt.  ebd.  —  ai, ygl.  purandAay' t;  s.o.  —  Fi.:  pärani/,  SüErJ.; nUAätarakiaiä ;  s.  noch  No.  1.  —  >)  PiLi  ie iSn  andar  an  mälaiän  tnäyaiän  änia  i  färari- tum  vatsä  estft.  —  a)  NA.  far';  t.  Var.
•  j.  päiri  i)  Adv.   'ringsherum':  F.  jg,
N.<y5(?).  3)  Praev.  (mit  siiy-,  haBi-).
Sva.  pairi,  vermutlich  durch  sekundäre  Ab- lösung aus  vfdääinen  Ableitungen  wie  fäiri- väia-  entstanden.  Vgl  ^fäiiUmuxfa-.  —  Po.: pirätnitt,
i.fiäiri  g-ir^ßayäj  N,^/:  lies  /aitig^irtpf.
-----PARA-----
•  j.,  g. 'par- V. 'hindurch-,  hinübergehen*,  53-1-         a)}Aw.  in  der  Verbindung  «<-i((Sp.
mirmilPraev.;Praes.i4b/rar<7-,2i  '/rä-,   $000.) faraca'\nn\aiAYxt':  >nxsaparfm
30  (Kaus.)  päraya-.  ha>rSk)m  xh-as  xsafiw  a^a  'raca  li.4'^;
mit   a   'durchdringend   hinzu   kommen  Vt.ÄS4,  i-t-47-         O)  Praev-  (mit  aJ^■,
za -•  (Dm.):  ^ä'ja  IM  3/rasa>K'i  da^Äu6y,f  '*'^-.    ^''-f-,   gam-,    'iar-,     'nas-,    rae^-,
V._j.27  (die  Erde  spricht).  -'Aa^i-osw.).
mit/ni    (/re)    'voran,    vorwärts    und       ^"'"f''-    7  y^h/iZ'l."- ^^''.fT^^
u-    ..L  .        .         i    i...  ,    ,.,,  ,      .       "»P--    np.   /ar'    ,GIiFli.  r.  310,    /  b.   159).  —
hmuber   gehen';    i)   'über  -'  (Akk.):  /re'     ^i  ^^ni)'fjrj','};  (.0  nj:   -a".  "ch  V' /j/'/  vJsfäis  cimatO /ra/ra  (iSK.)  p^rptüm       (\'.  ♦  5\  ;^'j>  ^-  S'-  ^S-  JiJ-  *)■  —  '>  Pü,: "mit  all  denen  werde  ich  voran,  htnüberj     fehlt;  s.  No.  2.  —  »  So  Y.  jj-,  7;  s.  No.  i. Über   die  Brücke   des   Scheiders   gehen" ;     ^s'"  ^'~'  -'"'■  \  "  ^'  ^i^'-  '^"'■ Y.  4Ö'.  10.  2)  'zu  -'  (Akk.  mit  ä):  usta  •  j.,  g,,  p.  "para  I)  Adv.  'luvor";  i)  lUum-
.  .  U  nan  yS  iiryejaakatat  haca  aukaot  lieh  "voran*:  ya!  mi  stärS  .  .  ia'attto isd.) ai>ye/aaÄjm    ahant    ä    frafrä    (2SPrA.)   -ra^a  ma  Vt&i.  2)  zeitlich 'vordem,
"..der  du  vom  vergänglichen  Leben  zum  ehedem*:  /rarasayS  .  .  yl  araca  'ra unvergänglichen  Leben  herüberkamst"  \.  /raoirisisiä  fsA.)  ya^ra  ..  VtJj.2S;  — 7.  52.  A)  Kaus.  'vorwärts  und  hinüber-   ij  nJtriJkqm  yam  apu^ram  .  .  anasaxtqm
nihreD|;  a)  'über  -'  iUrd  mit  Akk.):  /ra-  (sd.)  'ra  xsudrä  aii  fratihfri-aiti  V.  i^'.Z; parayaiihi  urvarum  tard  anvats  p^ntäm  —  drum  . .  hamaia  iSt^-erz.)  ya>a  'raät Y.  -ji.  16;  /p.  6  (s.  b)-  bl    'hin  -zu'  \X.  •,.  65;    usw.         a)    gAw.    mit    folg.
(Akk.):  ^ris'aj  tarS  pintümal hs unUmm  fiyal  'antequam,  bevor"";  es  folgt  Konj.: vahisttm  aküm  frapäraymi  S.ig.^.  *uurpidyji  isd.)    °rä    hyat    mSi    ä.jtmat
mitfl^Kaus.  i)  Tiemieder-,  herabfuhren,  s?raoi5\.4^.\i\  —  vaccä  möi..'r3  hyat -bringen':  tat  }^ar?n3  Aamblrayeinti  ..  ../j/v>.i  (sd,)7/w/a//i  Y.  J.V.2.  II)Praen. niparaydnti  .  .  baxsmti  sqm  paiti  a/iura-  'vor';  i)  räumlich,  mit  Akk.:  t  ava^para häiqm  Yt.6.  I.         2)  'Jemandem  (Dat)  sbes.  2)    zeidich;    a)    mit    Ab!.:    Tä
etwas(Akk.)  herzufuhren.-bringen':  ärvhqm  iiasS  yanhö  ahmäi  rü  sazdysi  (sd.)  ,  .  V. saB>ranqm  yä  (APn.  statt  f.)  mlzk-a  70. 2'>;  —  'ra  aiwühe  asnö  d^i>h?it  Y. mpärayänti  Yt  /J.  S4-  a)  Med.  'sich   ig.  S;   8*;    —    pasca    hü    */räsm,\däitim
etwas  (Akk.)  zuführen  sva.  aneignen':  -ra  hü  vaxull  "iü.^B;  46,  50;  —  sara- *hix/Jiie  nanm  asaian^m  .  .  nsirikqm ;  'i^uitrsm  .  ,  taimmrr.'m  (sA)  ahmat  'ra asaonim  .  ,  dn-atqm  .  .  zqm  .  .  nipurayaiita  daeia  pataytt  Ytip.j^f.;  —  yc/ihe  xsa- äpam  .  ,  anyqm  hl  azarHqm  nipärayania  \  "irä-ja  nsif  aottm  auha  ..  'ra  anädruxtöil "soll  ich  .  ,  (sie)  antreiben,  dass  sie  der  (sd)  para  ahmilt  yat  .  .  Yt  ig.  33;  — Ungläubigen  .  ,  Land  sich  aneignen,  ihr  ;  die  adv.-artige  Verbindung  para  ahmät Wasser  .  .,  ihr  übriges  Besitztum  sich  an- '  sbes.  b)  mit  Lok.:  'ra  m>r}tö  fasca eignen?"  V,/p.26.  'ffwrj/j  V.  6'.3i,  32;    —    *ra    avatähe  Aü
gl.  »«>«,  EOt. /arnn.  —  Pü.  (ru  Y.46,  X.^V,  ^tcarStö (sd.)  kfhrpya  <i/f(sd-)  am^sanqm /ran-ßa»,  (zaV.fp,  ^/'-.ji/jr/an,  (ta  Yt.6.:  >_   ^jil„    Y.  iO.  8.  C>     mit    Akk.:    «/
oval  vace  äs  ..yat  ml  fr-nao/rS  'ra  asm^m 'ra  appm  .  .  'ra  dalvaista  xrafiträis .masyäUi'a  'ra  vfsp?m  ahüm  ..Y.iff.ii;  3*-
rämlan    -
Sfi.:  praralayilu
m
```


## [2026-09-14T00:51:29.143Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hu\\.p\\|hu-p\\|huparp\\|hupar\" BRT.txt | head -30",
 "description": "grep BRT hu- compounds"
}
```


### [2026-09-14T00:51:29.190Z] TOOL RESULT

```
6888:"  j-i  g-  'ahura-  m.  i)  jAw.  'Herr,  Macht- haber, Fürst":  'rO  *sästr)nqin  äaiiihupai/is VliJ.  37;  —  ^wqm  yazante  aurvanhB -ränhs  äai^hu.patayS  ¥1.5.85;  —  yim fnäml.  z'jrf^raytam)  vasiinte  'rät^hö  .  . ähuiryarffa  .  .  haosravatahanS  Yt  i4-  39;
12701:•  j.  daÜhu-patay-')  m-  'Herr,  Gebieter einer  Provioz,  eines  Landes,  Landesherr'; i)  im  eig.  Sinn:  a!%rapatay3  .  .  *°tayS Aog.59;  —  va%ayanö  'paitts  V.  ig.  6 Yt.  15.  31;  —  yim  yazmte  "tayö  arjzahe ttva.jaspras  Yl  JO.  8;  —  ahurö  ^sästrfnqm •paiHl  Yt.  J^  37;  —  akuranhS  'tayS pu%ränhs  'paitinqm  Yt,  5. 8  5 ;  —  ä/rlitami tava  nara  ••paiti(VS.)Az.i;  A.i.8.  a)  mit Gen.  aus  ^Xyav,  daiAAav-.  nmanaAe  va KMätuspaitil  .  .  daijihfui  va  "paitis  Yt 10.18;  83,  l6.\%  VyL46';  —  dai^hsus yatffiM  Vr.J.  3,  V.  7.41,5.37;  —  daiMiuf •mVV.iO.S,  Y.y.  I,  Vyl-iö;  —  liairihSus 'tSe  Yt  /o.  17;  —  da/ryunam  'pattil (AP.)  Yt  /O.  18;  —  äaiAhyui  'painm*> nSirikqm  "die  Frau  ebes  Landesherrn" V.  7,  4a.  2)    von   Göttern;    a)    von
16445:—  'hfvm  ..  duyoarpm  Y,i2.s;  i,  3;  — näirya  va  '%raAe  vä  Y.  //.  i ;  —  nar»m vä  *näirikqm  vä  °&/vw  va  FrB.;  —  °^raAe '^rrtrt  Frb.7;  —  II  vistäspahyä  •ä'a* ariämahyä  napa  Bh.  i.\-,  —  küraui '%* J" Bh.  /.  10,  II,  13,  j,  5,  4.  i»,  b,  h;  J.  16^, 2.3,.?i3'.  4.i\  18*,  d,  i,  D./,  2,  5.1, 6'.  \',  72,  jy,  76',  ig,  X.  I.  2,  5,  Am.  /*,  2, Ao.  1.  2^;  l  —  pouruSaspahe  ''irS  V.  ig.  6, Yt.5. 18;  7z,  105,5.18,  30,  Y.5.  5;  —  ala- vazdasca  ^ritasca  säyuidrsi?  °'^ra  (ND.) Yt5.72;  —  /f^a"'ärfl(NP.)  "iiranaonahe F.  4  f.;  —  ycti  aslüal?r»tö  (sd.)  /raxUäiU äste  ..  vJspa.taurvaya  '^rS  Ytjp.  92;  — '"iratihs  daiähu.paitinqm  Yt.  5.  85;  /4. 59,  V.rp.43;  —  ''kra  (oder  °%r!>)  kava vJliäspa  (oder  'psi-,  Stverz.)  Vytj'  usw.; '■'i  31'  52.  54i  55;  —  i'ftff  "Sr?  ä^wya- >iSisYt5.32,  /7.3s;  y.7.43;  —  airpm (Stvetz.) aAuraAe  masdi  '^n>nY.2.J2U3y/.;
17773:mit  ava  und  >tl  Kaus,  'Jemanden  weg und  nach  Haus  fliegen  lassen,  im  Flug heimkehren  lassen':  fä  (näml.  fravasays) dim  ava  nifrävayenle  mqnaym  ake  yäha ttä  trur^ys  huparfnS  (sd.)  Yt.  13.  ^o.
21129:/ravayente  mqnaytn  ahe  y  nä  mfrr/ö\ huparms  (sd.)  Yt  13.  70;  —  täpayeiti mqm  asa  vahi^ta  ntqnaysn  ahe  y' ayaoxsusUm  ". ,  ab  wäre  es  geschmolzenes Eisen"  Yt.  77.  ao;  ao.  2)  sie  geht  auf
23853:Vgl.  urüct-  fem.  Adj.  ^  •  j.  vohu.p^T^sa-  m.  EN'.  eines  Gläubigen :
30265:•  j.  hu-paitiStäna-  n.  'gutes  Bein':  ustrS
30287:n  gaospmta..*gaohula''^  (:y%.)Y.2i.i;Y.  .  j.  hu-pairi'tan- Adj. '(sich)  wohl  hcrum-
30293:'da  Y.  12.  7:  —  gJu/  'iaukö  urvamm  Y.  j  •  j.  hu-pairi'spl-  Adj.  "ringsum  wohl  ge- JÖ'.  4,  20".  4,  S.  2. 14;  FrW.  Ö.  1;  —  gsusca  deihend'(?);  Aupatritä  nama  ahmi  'sph •däiilsS  gay€hyäiä  mardinS  Y. /j.  7.  nama  ahmt  (närol.  vayus)  Yt/5. 46.
30300:•  j,  hu-pairt§ta-  Adj.  'wohl,  gut  ausge- !  Abstammung':   ywii  Aubayi  '/nrif'^  Vr.
30304:Pü. :  mkirU. •  j.  hu-parana-  Adj,  'wohlbeflügelt':  th dim  ava  nifrävaymte  mqnaym  ahe  ydha nH  jmrr/S  'nS  ". .,  gerade  als  ob  man (es)  ein  wohlgeflügelter  Vogel  wäre"  Yt 13. 70.
30306:•  j.  hu-paurva-    Adj.    (fem.  -va-)    'der,  •'^'"««(APn.)  Yt.5.130;— fJto„=^ai.j?r« reichlich    frühere'    oder    'voranstehende': '(ASm.  statt  n.)  Vt5. 102.
30313:•  j.  hu-plta-  Adj.  'gu^ehütet':  pilüm yim  cinvats  .  .  yim  't>m  Vyt  4^.
30335:•  j.    hu-puftra-    Adj.    (fem.  -ri-)    Adj.  I     ^^^-  ""  ^-  "*"-  "  »'■  **'"-'^^-  ^'^i- 'treffliche   Söhne,    Kinder  habend':   nüi/-»  j- hu-barana-  Adj.  'gut  zu  reiten":  aipa tarn  .  .  *daste    'rm    "nicht   macht  er  sie  r"«  ■  ■  ^"^'^  hvazSna  Vyt  4S.
30338:•  j.  hu-ptar-  Adj.  (fem.  'fshrl-')  'der  einen  \yd^a  . .  atmia  spmta  .  .paitisqn  ^'nitlmca guten  Vater,  gute  Eltern  hat,    von  ^Xct\*uHa.b)r)itlm^a  *van/a.b>r3itlmfa  Y.60.6;
```


## [2026-09-14T00:51:42.522Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"euphrat\" AHD_watkins1985.txt KLN_1966.txt KNT.txt | head -20",
 "description": "grep Euphrates in AHD, Klein, Kent"
}
```


### [2026-09-14T00:51:42.577Z] TOOL RESULT

```
KNT.txt:1042:V. OP p bf are in some instances not traceable to pIE forebears or are definitely borrowings from outside sources; such are piru- ‘ivory’, si"kabru- ‘carnelian’, naiba- ‘good’ (only in Iranian), and many place and personal names, such as Pirdva ‘Nile’, Putdya- ‘Libyan’, Babirus ‘Babylon’, Arabdéya ‘Arabia’, Arbatrü- ‘Arbela’, Ufrütu- ‘Euphrates’, Nadifaba?ra ‘Nidintu-Bel’, Nabukudracara ‘Nebuchadrezzar’.
KNT.txt:1344:"Euphrates", Armina ‘Armenia’, Karka ‘Carians’,
KNT.txt:1970:regularly given; but it is given with names of provinces only when there is a list of all or several, and is omitted with some larger districts (Kar- тала, Varkàna), with cities (Pársa, if = ‘Persepo- пе’; Passiyduvdda ‘Pasargadae’; Hagmatana 'Ecba- tana’; Arbatra ‘Arbela’; Babirus ‘Babylon’), and with well-known rivers (Ufrätuš ‘Euphrates’;
KNT.txt:2716:Е. With or without prepositions, to denote place where or within which: DB 1.92 vardanam amu» Ufrātwã ‘a town beside the Euphrates’; DB 3.26 kära Parsa hya vapatüj ‘the Persian army which (was) in the palace’; XPa 13f vasiy aniyaSciy naibam kartam ana Parsé ‘much other good (construction) was built within this (city) Persepolis’.
KNT.txt:3118:Euphrates"), and then a resumptive adverb. The . E
KNT.txt:3584:519. 1.90-6. Saith Darius the King: After that I went off to Babylon. When I had not arrived at Babylon, à town by name Zazana, beside the Euphrates—there this Nidintu-Bel who called himself Nebuchadrezzar came with an army against me, to deliver battle. Thereupon we joined battle; Ahuramazda bore me aid; by the favor of Ahuramazda I smote that army of Nidintu-Bel exceedingly. The rest was thrown into the water, (and) the water carried it away. Of the month Anamaka II days were past, then we fought the battle.
KNT.txt:4879:Darius came upon Nidintu-Bel and his army at the Tigris, forced the crossing, and defeated him in IX 26 ($18), and though Nidintu-Bel rallied his forces and took the offensive, again defeated him at Zazana on the Euphrates, X 2 ($19); he pursued him and his few remaining horsemen to Babylon, took that city and Nidintu-Bel with it, and put the rebel to death ($20).
KNT.txt:5184:Ufrütu- sb. ‘Euphrates’, river of Babylonia:
KLN_1966.txt:14605:Fertile  Crescent,  a  semicircle  of  fertile  land  ex¬ tending  from  Palestine  and  Phoenicia  around the  Euphrates-Tigris  valley  to  the  Persian  Gulf {Ancient  hist.)  —  Coined  by  the  American  ar¬ chaeologist  and  historian  James  H.  Breasted (1865-1935).
KLN_1966.txt:20883:suff.  -fc  fr.  Kufa  (fr.  Arab.  al-K&fa"),  name  of  a town  on  the  Euphrates.
KLN_1966.txt:23636:mesoblast,  n.,  the  mesoderm.  —  Compounded  of  between  the  Euphrates  and  Tigris  rivers.  —  Gk.
```


## [2026-09-14T00:51:43.645Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^per-2\\|^per-\\|^2\\. per-\\|per-2\" AHD_watkins1985.txt | head -20",
 "description": "grep AHD per roots"
}
```


### [2026-09-14T00:51:43.694Z] TOOL RESULT

```
838:per-?
839:parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
840:per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
841:per-‘. To try, risk (< “to lead over,” “press forward”). A verbal root belonging to the group of per’. 1. Lengthened grade *pér- in Germanic *féraz, danger, in Old English
981:ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
1387:COMMODITY med- COMMON mei-! COMMOTION meue- COMMUNE mei-1 COMMUNICATE mei-1 COMMUNISM mei-1 COMMUTE mei-1 COMPACT! pag- COMPANION pa- COMPANY pa- COMPARE pera-2 COMPART pere-2 COMPASSION pé(i)- COMPEL pel-6 COMPELLATION pel-6 COMPENDIUM (s)pen- COMPENSATE (s)pen- COMPETE pet- COMPLACENT plak-! COMPLAIN plak-2 COMPLECT plek- COMPLETE pele-1 COMPLEX plek- COMPLICATE plek- COMPLICE plek- COMPLIMENT pele-1 COMPLY pele-1 COMPONENT apo- COMPORT per-2 COMPOSE apo-, paus-, COMPOSITE apo- COMPOSITION apo- COMPOUND apo- COMPRADOR pere-1 COMPREHEND ghend- COMPRESS per-5 COMPRISE ghend- COMPROMISE (s)meit(9)- COMPUNCTION peuk- COMPURGATION peue- COMPUTE peu- COMRADE kamer- con! kom
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1454:ELUANT leu(@)- ELUCIDATE leuk- ELUDE leid- ELUTE leu(a)- ELUVIUM leu(a)- ELYTRON wel-3 EMACIATE mak- EMANATE ma-3 EMANCIPATE man-2 EMASCULATE mas EMBASSAGE ag- EMBASSY ag- EMBELLISH deu-2 EMBER eUS- EMBER DAY ambhi, rei-3 EMBLEM gWele-1 EMBLEMENTS bhel-3 EMBOUCHURE beu-! EMBRACE mregh-u- EMBROCATE mergh- EMEND mend- EMERGE mezg-! EMERITUS (s)mer-2 EMESIS weme- EMETIC weme- EMIGRATE mei-! EMINENT men-2 EMIT (s)meit(9)- EMMET mai-1 EMOLLIENT mel-1 EMOTION meue- EMPEROR pere-! EMPHASIS bha-' EMPHYSEMA pu-! EMPIRIC per-4 EMPLOY plek- EMPORIUM per-2 EMPRISE ghend- EMPTY med- EMPYEMA pu-2 EMPYREAL pil- EMULSION melg- EMUNCTORY meug-2 EN-! en
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1486:EXxO- eghs EXOCRINE krei- EXODUS sed-2 EXOERGIC werg- EXONERATE en-es- EXOPHTHALMOS okw- EXORDIUM ar- EXOSTOSIS ost- EXOTERIC eghs EXOTIC eghs EXPAND pete- EXPATRIATE peter- EXPECT spek- EXPECTORATE peg- EXPEDITE ped-! EXPEL pel-6 EXPEND (s)pen- EXPERIENCE per-4 EXPERIMENT per-4 EXPERT per-4 EXPIATE pius EXPIRE spirare EXPLAIN pele-2 EXPLETIVE pela-1 EXPLICATE plek- EXPORT per-2
1498:FARCE bhrekw- FARCI bhrekw. FARCY bhrekw- FARE per-2 FARINA bhares- FARINACEOUS _bhares- FARM dher-2 FARRAGINOUS_ bhares- FARRAGO bhares- FARRIER ferrum FARROW! porko- FART perd- FARTHING kWetwer- FARTHINGALE virére FASCES bhasko- FASCIA bhasko- FASCICLE bhasko- FASCINATE bhasko- FASCINE bhasko- FASCISM bhasko- FASHION dhé-1 FAST! past-
1506:FENCE gWhen-! FENNEL dhé@(i)- FENUGREEK dhé(i)- -FER bher-1 FERAL ghwer- FER-DE-LANCE ferrum FERE per-2
1507:FERIA dhés- FERMATA dher-2 FERMENT bhreu-? FERN per-2 FEROCIOUS ghwer- FERRET! bher-1 FERRET? bhel-3 FERRI- ferrum FERRO- ferrum FERROUS ferrum FERRUGINOUS ferrum FERRULE wei-1 FERRY per-2 FERTILE bher-1 FERVENT bhreu-2 FERVID bhreu-2 FERVOR bhreu-2 FEss bhasko- -FEsT dhés- FESTAL dhés- FESTINATE bhers- FESTIVAL dhés- FESTIVE dhés- FESTOON dhés- FETAL dhé(i)- FETCH! ped-1 FETE dhés- FETICIDE dhé(i)- FETISH dhé-1 FETLOCK ped-! FETTER ped-1 FETTLE ped-2 FETUS dh@(i)- FEUD! peig-2 FEUD? peku- FEUILLETON bhel-3 FEVERFEW bheug-! FEW pau-
1514:FIRTH per-2
1516:FIx dhigw- FIXATE dhig¥- FIXITY dhigw- FIXTURE dhigw- FIZGIG peis-2 FIZZLE pezd- FJELD pelis- FJORD per-2 FLABELLUM bhié-2 FLAG! = plak-1 FLAGELLATE bhiag- FLAGELLUM _bhiag- FLAGITIOUS bhlag- FLAGRANT bhel-1 FLAIL  bhlag- FLAIR bhrag- FLAKE! plak-1 FLAKE? plak-1 FLAMBE bhel-1 FLAMBEAU bhel-1 FLAMBOYANT bhel-1 FLAME bhel-1 FLAMEN bhilad- FLAMINGO bhel-1 FLAMMABLE bhel-1 FLAN plat- FLANEUR pele-2 FLANK kleng- FLANNEL wele-1 FLAP plab-
1530:FORCEPS gWher- FORCIPATE gWher- FORD per-2
1544:FROLIC fik-, preu- FROM per? FRONTISPIECE spek- FROST preus- FROTTAGE bhréi- FROWARD per! FRUCTIFY bhrig- FRUGAL bhriig- FRUGIVOROUS bhrig- FRUIT bhriig- FRUITION bhriig- FRUMENTACEOUS _ bhrig- FRUMENTY bhriig- FRUSTULE bhreus-2 FRUSTUM bhreus-2 FRY! bher-4 FUGACIOUS bheug-1 -FUGE bheug-! FUGITIVE bheug-1 FUGLEMAN man-1, pleu- FUGUE bheug-! FUHRER per-2 FULCRUM bhelg- FULGENT bhel-1 FULGURATE bhel-1 FULIGINOUS dheu-1 FULL! pele-1 FULMAR pu-2 FULMINATE bhel-1 FUMARIC ACID dheu-1 FUMAROLE dheu-1 FUMATORIUM dheu-! FUMATORY dheu-1 FUME dheu-! FUMIGATE ag-, dheu-! FUMITORY dheu-1, ters- FUNAMBULIST al-2 FUNCTION bheug-2 FUND bhudh- FUNDAMENT bhudh- FUNDUS_ bhudh- FUNGIBLE bheug-2 FUNNEL gheu-
1550:GABERDINE per-2, wel-3 GABFEST dhés- GABION keue-2 GABLE ghebh-el- GABRO gladh- GaD2 ghasto- GAEA gé
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1988:OPINION op-* OPISTHOBRANCH epi OPISTHOGNATHOUS epi OPIUM s(w)ok"o- OPPORTUNE per-2 OPPOSE apo- OPPRESS per-5 OPPROBRIUM bher-1 OPPUGN peuk- OPSIN OkW-
```


## [2026-09-14T00:51:59.600Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"p\\(e\\|ə\\|a\\)r\\(e\\|ə\\)tu\\|peretush\\|p9r9tu\" KLN_1966.txt | head -20; echo \"=== ford/port ===\"; grep -n \"^port, n\\.\\|^port,\\|^ford,\\|^porter,\\|^portal,\" KLN_1966.txt | head",
 "description": "grep Klein for Avestan peretu"
}
```


### [2026-09-14T00:51:59.673Z] TOOL RESULT

```
29679:cogn.  with  Avestic  peretush,  ‘passage,  ford, bridge’,  OW.  rit,  W.  rhyd ,  ‘ford’,  OE.  ford,  of s.m.,  fr.  I.-E.  base  *per-,  ‘to  lead  across,  drive across,  traverse,  pierce'.  See  port,  ‘to  carry’,  and cp.  port,  ‘gate’,  portico,  portolano,  opportune, importunate,  and  the  second  element  in  passport. Cp.  also  ford.
=== ford/port ===
15140:ford,  n.  —  ME.,  fr.  OE.  ford,  rel.  to  OS.  ford, OFris.  forda,  OHG.  furt,  MHG.  vurt,  G.  Flirt, ‘ford’,  and  cogn.  with  L.  portus,  ‘harbor'  (orig. ‘entrance,  passage’),  OW„  Co.  rit,  W.  rhyd, ‘ford’  (cp.  the  Gallo-L.  place  name  Augusto- ritum,  lit.  ‘Ford  of  Augustus),  and  to  OE.  faran, ‘to  go’.  See  fare,  ‘to  prosper’,  and  cp.  fiord, firth,  frith.  Cp.  also  port,  ‘harbor’.
15144:ford,  former,  forth,  further.  Cp.  also  arpent,  ex¬ perience,  experiment,  expert,  finnan,  paradise, pardao,  parallel,  Perean,  peregrine,  peril,  per¬ oneal,  pilgrim,  poligar,  pore,  ‘opening",  porrect, port,  ‘harbor’,  port,  ‘gate’,  port,  ‘to  carry’,  post, ‘stake’,  Prajapati,  Prakrit,  prakriti,  Pralaya, pram,  ‘a  kind  of  boat’,  prana,  priest,  primary, prime,  prior,  proceres,  procerity,  prodigal,  prone, prose,  proso-,  protero-,  proto-,  province,  prow, ‘fore  part  of  a  ship’,  prowess,  Purana,  and  the second  element  in  reciprocal.
29680:port,  n.,  gate;  opening  in  the  side  of  a  ship  for loading  cargo.  —  OF.  (=  F.)  porte,  fr.  L.  porta , ‘gate,  door’,  which  is  rel.  to  portus,  ‘harbor’.  See port,  ‘harbor’,  and  cp.  portal,  Porte,  Portulaca, purslane,  and  the  first  element  in  porthole, port,  n.,  a  kind  of  strong  red  wine.  —  Lit.  ‘wine of  Oporto',  a  town  in  Portugal.  Oporto  (i.e.  o porro )  lit.  means  'the  port’.  See  port,  ‘harbor’, port,  tr.v.,  to  carry  (a  rifle  or  sword).  —  The word  orig.  meant  ‘to  bear,  carry  in  general’.  It derives  fr.  MF.  (—  F.)  porter,  ‘to  bear,  carry’, fr.  OF.,  fr.  L.  portare,  for  *poritare,  freq.  of  a supposed  primitive  verb  *porere,  which  is  cogn. with  OI.  piparti,  ‘brings  over’,  parayati,  ‘carries over’,  Gk.  neipeiv  (for  *~£pic.v ),  ‘to  penetrate’, fr.  I.-E.  base  *per-,  ‘to  lead  across,  drive  across, traverse,  pierce',  whence  also  Goth,  faran,  ‘to go’,  OE.  ferian,  ‘to  go;  to  carry’.  See  fare,  v., and  cp.  port,  ‘gate’,  port,  ‘harbor’,  apport,  com¬ port,  deport,  disport,  export,  import,  portly,  pur¬ port,  rapport,  report,  sport,  support,  transport, and  the  first  element  in  portmanteau, port,  n.,  manner  in  which  a  person  bears  himself. —  OF.,  fr.  porter,  ‘to  bear,  carry’,  fr.  L.  portare, of  s.m.  See  port,  v.
29681:port,  n.,  the  left  side  of  a  ship  looking  forward from  stern  to  bow;  larboard,  —  Either  fr.  port, ‘gate;  opening  in  the  ship  for  unloading  cargo’, or  fr.  port,  ‘harbor’.
29696:porter,  n.,  a  doorkeeper.  —  ME.,  fr.  OF.  (  =  F.) portier,  fr.  Late  L.  portarius,  ‘a  doorkeeper’,  fr. L.  porta,  ‘door’.  See  port,  ‘gate’,  and  agential sufT.  -er.
29697:porter,  n.,  a  carrier.  —  ME.  portour,  fr..MF.  por- teour  (F.  porteur),  fr.  L.  portdtorem,  acc.  of  por- tator,  ‘bearer,  carrier’,  fr.  portdtus,  pp.  of  por- tare,  ‘to  carry’.  See  port,  ‘to  carry’,  and  agential suff.  -er.
29699:porter,  n.,  an  inferior  kind  of  ale.  —  Short  for ‘porter’s  beer’;  so  called  because  preferably drunk  by  porters.  See  porter,  ‘carrier’.
```


## [2026-09-14T00:52:01.012Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5180,5190p' KNT.txt; echo \"=== KNT para ===\"; grep -n \"^para\\b\\|para- \" KNT.txt | head -10",
 "description": "Kent Ufratu entry"
}
```


### [2026-09-14T00:52:01.072Z] TOOL RESULT

```
(2) Prefix, ‘under’, in Upadarma-; ‘toward’, with verb ay-; ‘beside’, in upasia-.
Upadarma- sb. ‘Upadarma’, father of Agina: Elam. uk-ba-[lar|-ra-an-ma. From ира + darma- (root dar-), Skt. dhérma- ‘right conduct’ (§163.V): “Не who is under (= behaves himself according to) right conduct’ (so Bthi. AiW 390, with lit.; hardly Upadara"ma-, after the Elam.; hardly as taken b Hz. ApI 190). Upadarmahyá gsm. DB 1.74.
upariy adv., prep., prefix, ‘above’: Av. upairi, Skt. upd, Gk. тёр, Lt. s-uper, Gt. ufar, pIE *uperi (5191.1). (1) Adv. ‘above’, XPh 31. (2) Prep. with ace., ‘over, over and above, upon, according to’: DB 4.64; DNb 4, 32, 46, 49; DSf 27. (3) Prefix, ‘over’, with verb ay-.
upasté- sb. ‘help, aid’: upa- + verbal root slà- (6140.1, $142), ef. Gm. Bei-stand for meaning. upastém asf. AmH 10; DB 1.25, 55, 87, 94; 2.24f, 34, 40, 45, 54, 60, 68, 86, 97°; 3.6, 17, 37, 45, 62, 67, 87; 4.60f, 62; DPd 13; DNa 50; DSf 19°; DSk 5; XPh 32, 45.
Ufrütu- sb. ‘Euphrates’, river of Babylonia:
OLD PERSIAN
Elam. t-ip-ra-tu-i8, Akk. purattu, Gk. Еўфрат
(§75.V, §76.V, §166, $166.II). Etymology un. |
certain, probably a popular etymologizing in OP of a local non-Iranian name, cf. Bthl. AiW 1830; Fick, ВВ 24.310; Justi, ТЕА 17.116; Tm. Lex. 77, Ufrätwā ism. DB 1.92 (not gen., as taken by Hz, ApI 71-2).
ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + prep. айту, as taken by ВШ. IF 12.110, A1W 60-1, Mt. Gr. $818).
uba- adj. ‘both’: GAv. uba-, Skt. dual ubhá(u), pIE *ubhó(u), cf. Gk. &p-dw, Lt. ат-00 ($143.11). ubà ndm. ($189) DSf 14; XPf 21.
=== KNT para ===
1811:П. Secondary -па-, forming adjectives: para- na-, perhaps here kam-na; as mase. sb., drauja- па-, as nt. abstract pariy-ana-; forming hypo- coristic personal name, Aci-na-; perhaps Mardu- na- in Mardun-tya-; forming place names, with lengthening of preceding vowel, Varkàna- to varka-, Ha"-gmalàna- to ha?-gmala-; with -na- of uncertain origin, h*zdna- (see Lex. s.v.).
2845:para ‘beyond’, of place where.
2846:para ‘along’, of motion; enclitic postposition.
5003:apara- adj. "later, after’: Av. Skt. apara-, from apa- + comp. -ra- ($32, 419.11). арата пет, XPh 47. aparam asn. as adv. DB 4.37, 42, 48, 68, 70, 87; DSt 10° (not apara-ma, nsm. with enel. abl., DB 4.37, 68, 87—and DSt 10°—as Bthl. AiW 77 suggests, following АКК. $a be-la-a ar-kt-a ‘who shall rule after me’).
5419:tauman- sb. ‘power, strength’: deriv. of root tav- ‘be strong’, with suffix -man- as in Skt. nama ‘name’, Lt. nomen (§122, $155.11). For separa- tion from taumd- ‘family’, see Tm. Lex. 91, and Kent, JAOS 35.329-31. See also tawiyah-. taumā nsn. ($187) DB 4.74, 78; 5.19°, 35. tau- тату (= taumanis-Saiy; §41, §130, $138, $187) ipn. DNb 25f (Lg. 15.171-2, 176; not gen. sg. with Hz. Api 327; hardly loc. sg. with Sen 247; possibly aee. du., ‘two powers lof mind and of body|’, with Pisani, Riv. Stud. Or. 19.88-9).
5580:Skt. jrdyas- ‘expanse’, pIE *órejos- (§88, $113, $128, $156.II). Decl, §185.1. See also para- draya. draya asn. DB 5.23; DPe 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
5648:ipara- adj. ‘later’, possibly in hyáparam (q.v.) : Av. para- ‘farther’, Skt. pára- ‘distant’, Gk. qépav ‘beyond’.
5649:nara prep. with acc. ‘beyond’ (§32, $63.1): Av. pard ‘before’, Skt. purds ‘before’, Gk. таро ‘before’; DPe 15; DPh 5; DH 4, See also para- dayadàm, paradraya.
5733:para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
```


## [2026-09-14T00:52:17.098Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f in ['KLN_1966.txt']:\n    txt=open(f,encoding='utf-8',errors='replace').read()\n    for target in ['cogn.  with  Avestic  peretush','port,  n.,  gate;  opening']:\n        i=txt.find(target)\n        print(f,target[:30],'leaf',txt.count('\\f',0,i))\nEOF\necho \"=== AHD PASSPORT/SPORT index ===\"; grep -n \"PASSPORT\" AHD_watkins1985.txt | head -3",
 "description": "Find Klein leaf for port entry"
}
```


## [2026-09-14T00:52:18.030Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS puhl ===\"; grep -n -i \"puhl\\|pwhl\" SNS_pages.txt | head -20",
 "description": "grep SNS for puhl"
}
```


### [2026-09-14T00:52:18.407Z] TOOL RESULT

```
KLN_1966.txt cogn.  with  Avestic  peretush leaf 650
KLN_1966.txt port,  n.,  gate;  opening leaf 650
=== AHD PASSPORT/SPORT index ===
```


### [2026-09-14T00:52:18.451Z] TOOL RESULT

```
=== SNS puhl ===
15906:puhl 137/6                   328/5                           ravagtar 228/19        rOsnlg 231/18
15907:puhl    I   ravan 137/10   rast grav 222/17                  rav3n 229/1            rOsnth 231/14
```


## [2026-09-14T00:52:29.186Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==623' KLN_1966.txt | head -c 1500",
 "description": "Klein leaf 622 content"
}
```


### [2026-09-14T00:52:30.263Z] TOOL RESULT

```
 adj.  —  MF.  (=  F.)  persuasif  (fem. persuasive ),  fr.  ML.  persuasivus,  fr.  L.  persuasus, pp.  of  persuadere.  See  persuade  and  -ive.
Derivatives:  persuasive,  n.,  persuasive-ly,  adv., persuasive-ness,  n.
persulfate,  persulphate,  n.  ( chem .)  —  Formed  fr. per-  and  sulfate.
persulfide,  persulfid,  persulphide,  persulphid,  n.
(chem.)  —  Formed  fr.  per-  and  sulfid(e). persulfuric,  persulphuric,  adj.  —  Formed  fr.  per- and  sulfuric.  See  sulfur  and  adj.  suff.  -ic. pert,  adj.,  impudent.  —  ME.,  aphetic  for  OF. apert,  ‘open’,  fr.  L.  apertus,  pp.  of  aperire,  ‘to open’.  See  apert.  In  some  senses  pert  represents OF.  (es)pert,  fr.  L.  expertus,  ‘experienced’.  See expert.
Derivatives :  pert-en,  tr.  and  intr.  v.,  pert-ly,  adv., pert-ness,  n.
pertain,  intr.  v.,  —  ME.  partenen,  pertenen,  fr. MF.  partenir,  ‘to  belong',  fr.  L.  pertinere,  ‘to belong,  concern,  have  reference  to’.  See  per¬ tinent  and  cp.  abstain  and  words  there  referred to.  For  the  substitution  of  the  L.  pref.  per-  to OF.  par-  cp.  peradventure  and  words  there referred  to.
Derivative:  pertain-ing,  adj. pertinacious,  adj.,  persistent,  obstinate.  —  L.  per- tinax,  gen.  -acis,  ‘steadfast,  persevering,  very tenacious’,  fr.  per-  and  tendx,  ‘tenacious’.  See tenacious.  For  the  change  of  Latin  e  (in  tendx) to  i  (in  per-tinax)  see  abstinent  and
```


## [2026-09-14T00:52:47.695Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 640 645 650 655; do echo \"--- leaf $n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | grep -oE \"^[0-9]{3,4}$|[0-9]{4}\" | head -5; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -c 120; echo; done",
 "description": "Look for page numbers in Klein leaves"
}
```


### [2026-09-14T00:52:48.856Z] TOOL RESULT

```
--- leaf 640 ---
1200
1201
1743
1822
1801

Derivative:  plecol-ine,  adj. plecto-,  combining  form  meaning  ‘twisted’,  as  in Plectognathi.  —  Fr.  Gk. 
--- leaf 645 ---
1209
7768
1210
 n.,  a  native  of  Poland.  —  G.  Pole,  sing,  of Polen,  fr.  MHG.  Polan,  pi.  Polane,  fr.  Pol.  Pol¬ jane, 
--- leaf 650 ---
1220
1221
,  fr.  L.  porca  (for  *prkd),  ‘ridge between  furrows’,  which  is  cogn.  with  OE.furh, OHG.  juruh,  ‘furro
--- leaf 655 ---
1228
1793
  pulsate,  ‘to  beat,  strike’)  and  cafe, ‘coffee".  See  push  and  cafe  and  cp.  next  word, poussette,  n.
```


## [2026-09-14T00:52:53.165Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==651' KLN_1966.txt | grep -n \"peretush\" -B4 -A2",
 "description": "Klein port harbor entry"
}
```


### [2026-09-14T00:52:54.185Z] TOOL RESULT

```
24-Derivative:  porridg-y,  adj. porriginous,  adj.,  pertaining  to  porrigo.  —  Form¬ ed  with  suff.  -ous  fr.  L.  porrigo,  gen.  -inis.  See next  word.
25-porrigo,  n.,  eruption  on  the  scalp  ( med .)  —  L. porrigo,  ‘dandruff’,  rel.  to  porrum,  ‘leek’.  See porraceous.  For  sense  development  cp.  F.  poi- reau,  porreau,  ‘leek;  wart’, porringer,  n.,  a  bowl  for  porridge.  —  A  blend  of earlier  pottanger  (fr.  F.  potager ,  a  derivative  of potage),  and  porridge  (q.v.)  —  For  the  intrusive n  cp.  harbinger,  messenger,  passenger,  scavenger. port,  n.,  harbor,  haven.  —  ME.,  partly  fr.  OE. port,  partly  fr.  OF.  (=  F.)  port,  which  both derive  fr.  L.  portus,  ‘harbor’,  orig.  ‘entrance, passage’,  which  is  rel.  to  porta,  ‘gate,  door’,  and
26-port
27-roseidon
28:cogn.  with  Avestic  peretush,  ‘passage,  ford, bridge’,  OW.  rit,  W.  rhyd ,  ‘ford’,  OE.  ford,  of s.m.,  fr.  I.-E.  base  *per-,  ‘to  lead  across,  drive across,  traverse,  pierce'.  See  port,  ‘to  carry’,  and cp.  port,  ‘gate’,  portico,  portolano,  opportune, importunate,  and  the  second  element  in  passport. Cp.  also  ford.
29-port,  n.,  gate;  opening  in  the  side  of  a  ship  for loading  cargo.  —  OF.  (=  F.)  porte,  fr.  L.  porta , ‘gate,  door’,  which  is  rel.  to  portus,  ‘harbor’.  See port,  ‘harbor’,  and  cp.  portal,  Porte,  Portulaca, purslane,  and  the  first  element  in  porthole, port,  n.,  a  kind  of  strong  red  wine.  —  Lit.  ‘wine of  Oporto',  a  town  in  Portugal.  Oporto  (i.e.  o porro )  lit.  means  'the  port’.  See  port,  ‘harbor’, port,  tr.v.,  to  carry  (a  rifle  or  sword).  —  The word  orig.  meant  ‘to  bear,  carry  in  general’.  It derives  fr.  MF.  (—  F.)  porter,  ‘to  bear,  carry’, fr.  OF.,  fr.  L.  portare,  for  *poritare,  freq.  of  a supposed  primitive  verb  *porere,  which  is  cogn. with  OI.  piparti,  ‘brings  over’,  parayati,  ‘carries over’,  Gk.  neipeiv  (for  *~£pic.v ),  ‘to  penetrate’, fr.  I.-E.  base  *per-,  ‘to  lead  across,  drive  across, traverse,  pierce',  whence  also  Goth,  faran,  ‘to go’,  OE.  ferian,  ‘to  go;  to  carry’.  See  fare,  v., and  cp.  port,  ‘gate’,  port,  ‘harbor’,  apport,  com¬ port,  deport,  disport,  export,  import,  portly,  pur¬ port,  rapport,  report,  sport,  support,  transport, and  the  first  element  in  portmanteau, port,  n.,  manner  in  which  a  person  bears  himself. —  OF.,  fr.  porter,  ‘to  bear,  carry’,  fr.  L.  portare, of  s.m.  See  port,  v.
30-port,  n.,  the  left  side  of  a  ship  looking  forward from  stern  to  bow;  larboard,  —  Either  fr.  port, ‘gate;  opening  in  the  ship  for  unloading  cargo’, or  fr.  port,  ‘harbor’.
```


## [2026-09-14T00:53:02.373Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN pul ===\"; grep -n \"pul\\b\\|pul  \\|Brücke\" HRN.txt | head -20; echo \"=== HRN par Feder ===\"; grep -n \"Feder\" HRN.txt | head -20",
 "description": "grep Horn for pul, par"
}
```


### [2026-09-14T00:53:02.442Z] TOOL RESULT

```
=== HRN pul ===
3096:325. pul^) 'Brücke.
3098:aw. peretU' 'Brücke', pesu- 'Furt' (d. i. peretü-, peäu-^
3100:puhrj puhl ^Brücke, Furt'.
3102:pul.
3116:2j Nie pul gesprochen oder geschrieben (Vullers), das nur
3210:340. puläd 'Stahl'.
3215:bolaf; bei. puläJ , pülat (209) ; arab. fülad, syr. "TPC.
=== HRN par Feder ===
273:schreiben, wie mir die Zeichen gerade in die Feder fliessen,
2852:aw. parena- 'Feder, Flügel'; phlv. par bezw. parr^
2854:143); ai. parnd- 'Feder, Flügel*; lit. spafnas 'Flügel*.
```


## [2026-09-14T00:53:04.878Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3090,3120p' HRN.txt; echo \"=========== par ===========\"; sed -n '2845,2862p' HRN.txt",
 "description": "Horn entries 325 pul and par"
}
```


### [2026-09-14T00:53:04.962Z] TOOL RESULT

```
das im Commentar immer für aw. yhaec- (auch für
visrascayen vd. 7 (77)) steht.
Zusammenhang mit l/"Aa^c-, hincaiti, ai. l/'sec-,
sincdti ist unklar, aber doch wohl vorhanden.
324. pegäh *Frühlicht, früher Morgen .
aw. upa ~r (Jäh (s. No. 889).
325. pul^) 'Brücke.
gel. purd.
aw. peretU' 'Brücke', pesu- 'Furt' (d. i. peretü-, peäu-^
Bartholomae, Ar. Forsch. II, 35 folgg.); phlv.
puhrj puhl ^Brücke, Furt'.
kurd. per^ pir, pird, purd, pel (H.-Sch.); af/. LW.
pul.
326. peleng 'Leopard'^).
skr. p^däku' *Tiger, Panther' (ai. pfdaku-^ pfdäkü-
nur *Natter, Schlange').
kurd. LW. pilink; afy. prang,
327. penUh 'Zuflucht, Schutz', penahlden 'Schutz suchen'.
phlv. panäh,, panähih^ vergl. Mitr]panähak (AV.).
Doch wohl zu l/^pä- schützen'?
Bartholomae stützt diese Erklärung brieflich
*) Das Wort ist nicht allzu gut beglaubigt. Die anderen Wörter-
bücher belegen es gar nicht, nur der FR hat folgenden Vers Leblbl's
(Metr. Muteqärib) mit der Aussprache bis^ :
be^enjer heme tens^ enjlde end
ber an /äk^ /üues bisetijlde end
2j Nie pul gesprochen oder geschrieben (Vullers), das nur
•Geld' bedeutet.
^) Felis pardus L. (Blanford, S. 34).7:^
durch den Hinweis auf ai. dhäna- zu dhä-^ aw. frena-
zu prä'^ aw. frä/snenem (KZ. 30, 330) zu (ai.) jüa-,
=========== par ===========
Vor, weg* ; phlv. par-, ai. pdrä- 'weg, fort*.
In dieser Bedeutung auch in der' Form pera- vor-
kommend.
2) ap. pariy 'um , herum' ; aw. pairi ; phlv. par- ;
ai. pari.
293. perr Teder, Flügel*; pemden^ penden^ perend 'Vogel'^),
perre.
aw. parena- 'Feder, Flügel'; phlv. par bezw. parr^
par(r)Uan (Bund.), par(r)is (Nöldeke, ZDMG. 46,
143); ai. parnd- 'Feder, Flügel*; lit. spafnas 'Flügel*.
kurd. per^ zaza pel 'F]ügel\ firin 'fliegen*; wa/. parr.
^) Auch vd. 5 (28) steht patlrak^ nicht patir, gegen Spiegel,
Trad. Lit. 412.
2J Suffix 'a?it, Partie. Praea.
Ilorn, QrundrisH d. neiip. Fitymolü^i<\ 5— m —
np. per7' soll auch *Blatt' bedeuten, wie ai. parnd- ;
vgl. ebenso g. par^ kurd. per, af;'. pur, bei. pan (442),
wa;^. paU^ sar. porÄ-, si/n. />arjr (aus "^parnaka-).
```


## [2026-09-14T00:53:17.038Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN Ufer ===\"; grep -n \"Ufer\" HRN.txt | head -20; echo \"=== HUB Ufer/bar ===\"; grep -n \"Ufer\" HUB.txt | head -20",
 "description": "grep Horn/Hübschmann for Ufer (shore)"
}
```


### [2026-09-14T00:53:17.125Z] TOOL RESULT

```
=== HRN Ufer ===
1765:o. t aw. para- 'Ufer, Rand'; phlv. -bär, z. B. röt[bar
7377:). keräu Ufer, Seite, Ende', keräne, meist kenür^ keyiüre.
=== HUB Ufer/bar ===
5262:sard 'kait', sarin *Schani'; karr *taub*, karan 'Ufer, kardan
9576:(Fird. I, 247, 71; 251, 132) 'Ufer, Ende = zd. karana-,
```


## [2026-09-14T00:53:19.526Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1752,1775p' HRN.txt",
 "description": "Horn -bar entry"
}
```


### [2026-09-14T00:53:19.577Z] TOOL RESULT

```
155. hädye *Weingefäss', vergl. bade 'Wein .
ap. ßandarj' üsgaiiitj (ptdXrj Athen. XI, 27 (de
Lagarde, Ges. Abh. 211), unsicher; phl. batak (PPGl.).
156. (\)här Xast'; vergl. ;^er]M;ar.
ai. bhärd' 'Bürde, Tracht, Last*; phlv. bar; arm.
bern Last'.
kurd. af;^. bei. (33) bär.
np. bar, ber Trucht' gehört ebenfalls hierher;
berömend, jüd.-pers. aber 1D01D (Is. 45, 8).
157. {2)bär 'Mal'.
skr. vära- 'Mal'; phlv. bär.
158. {s)bär in Comp. Jöi[bäry derya\bär, röd[bar, Zeng[bar,
Hindü[bär,
o. t aw. para- 'Ufer, Rand'; phlv. -bär, z. B. röt[bar
(Bund.); ai. pard- *üfer.
159. bärän *Regen', bartden regnen', baris, bärgln,
g. he-väre 'es regnet'; mäz. väris; Käs. vörün etc.
aw. vara- 'Regen', varenti Venu es regnet' (Barth o-
lomae, Indog. Forsch. I, 178); phlv. varan, värUan,
varimtan (PV.), väranUan (Bund.); ai. vdr- 'Wasser.
kurd. baritty bari^ barän (LW.), baris (LW. ?) varin
(H. -Seh.); af/. varyaj 'Wolke*, varyaz, var-edal
Vegnen'; oss. d. warun^ t. vdrin (73); bei. gväris^
gvaray (147) ; wa;^. vür ; sar. variij^ varisa,
```


## [2026-09-14T00:53:36.123Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 632 633 634 635 636; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -c 700; echo; done",
 "description": "BQT v1 leaves around p.414"
}
```


### [2026-09-14T00:53:37.127Z] TOOL RESULT

```
=== leaf 632 ===
پشت پاخارمدن
شدن و خوش آمدن و خوشحال کردبدن
جاشد ۱ ۰
فست با ردن کنابه از ترك دادن
واعراض نمودن - ومنهزم شدن باشد.
پشت پای - حیز ومختث را خواننده
و گاهی حنوان دشنام هم این
کومف .
فشت دست - کلیمی با شالی باش دکه
برزمگران 3 باغبانان چبر ی درآن نهند و بریشت
بتدند .
پشت چمی ۰ کتابه از سحن چمن
پشت دادن «کنایه از روی کردایدن
ورو ردان شدن و گریختن باشد .
پشت دار - پروزن‌بردیار » پشتیبانرا
گوبند - و هر چی
=== leaf 633 ===
مِِ ۳
ار ها کلیس
#5
بت ۸ دول
۰
چن 2 ًُ ۰ وم رای و
گر مرف تاره از ۳
ای فرب

=== leaf 634 ===


=== leaf 635 ===
4 سس
ارل و واو عمروف مرطبان سقالین باشد, ومعرب
آن فنتدل لست.:
بشتواره بر وزن خدك باره ۰
مقداری از هر چیز باشد که آئرا برهشت نوان
برداشت
سس ۰ ۹2 ۰ ۰
پشتوآن - بر وزن و معنی‌پشنیبان‌باشد»
آنرا بدیوار و سر دیگرآنرا برزمین ص بکنند.
وچوب یشت در را نیز گویند وبمعنی پشت‌ویناه
وجانب دار وممد ومماون هم‌آمده است .*
ی « نم اول و سکون ثانی و کس
الث وسکون تستانی . جامةٌ کوناهی را گونند
که تا کم گاه باشد و آ
=== leaf 636 ===
اشکل , عمروفست که سرکن گوسفند و آخو
باشد ۰ 3
بشکله ‌‌ بفتح لام بمعنی شکل است
ی ماد و کسك
کلیدانرا لیز گوبند .
پشکلید » بکر اول و لام بروزن دل
کشد * یعنی بناخن وانکشت رخن ه کرد
پشکم ه بکر اول بر وزت اشکم »
اموان وبا ر گاه وا گز نش ۰ رضتح اول نیز همسن
معنی آهده اس ۷ :
بشل -
ی
هد چز را کو ند که مکدنگز زشیفا مدا کند:
و بفتح ال و ثانی هم بنظر آمده است ؛ ویسنی
که مد دو چیز است که با مکدیگر بگیرند
وبکوبند»
```


## [2026-09-14T00:53:47.137Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if 'جسر' in p or re.search(r'پل\\s*[-‌ـ]',p):\n        print('leaf',i, [l for l in p.split('\\n') if 'جسر' in l or 'پل' in l][:4])\nEOF",
 "description": "Find pol entry in BQT v1"
}
```


### [2026-09-14T00:53:48.434Z] TOOL RESULT

```
leaf 54 ['و بپلوی 118۳68۲ ۱ .', 'کلم پپلویچینوت)۸390۷8) (پل\u200cصراط) درفارسی چینود شده»ولی']
leaf 55 ['چپل وهفت عدم توجه ایرانیان . لفت\u200cنویسان فیرایرانی', 'اگر خود بیشتی و گر دوزخی گذارش سوی چینود پل\u200cبود ۱ .']
leaf 374 ['سین سعفص ونای فرشت : ستار؛ سپل\u200cرا گوشد .', '۴ - پپلوی 2861611. کناه ککه سلاح خود دا برای ضربت کسی بلند کند . اونایمی']
leaf 640 ['پل - بنم اول وسکون ثانی, طافی باشد | خوانند 8 ومتفف پول هم\u200cهست که عرب فلوی', '۴۳ - شاد صرفی در۳2(62, پپلوی65124: استاد. رگ بونکر ص۲۷ ۱۲. ۴ رك :', '6 - اوستا !۳6۳6/۷ (یل) » 865۵ ( کدار بایاب) ؛ پهلوي 00۲ , اطنا0 (پل, کدار).']
```


## [2026-09-14T00:53:54.791Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==641' BQT_v1_pages.txt | grep -n \"پل\\|اوستا\" | head -20",
 "description": "BQT leaf 640 pol entry detail"
}
```


### [2026-09-14T00:53:55.925Z] TOOL RESULT

```
14:پل - بنم اول وسکون ثانی, طافی باشد | خوانند 8 ومتفف پول هم‌هست که عرب فلوی
22:۱ اوستا 820 + ۷0۵ (به هاگام) « اسشق ۷۲ [ رك : گاه ] , اجکی ۳۵8281
24:۴۳ - شاد صرفی در۳2(62, پپلوی65124: استاد. رگ بونکر ص۲۷ ۱۲. ۴ رك :
26:6 - اوستا !۳6۳6/۷ (یل) » 865۵ ( کدار بایاب) ؛ پهلوي 00۲ , اطنا0 (پل, کدار).
```


## [2026-09-14T00:53:56.646Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in range(612,630):\n    p=pages[i]\n    hits=[l for l in p.split('\\n') if 'parena' in l or 'اوستا' in l and 'پر' in l or 'بال' in l]\n    if hits: print('leaf',i,hits[:5])\nEOF",
 "description": "Find par entry in BQT v1"
}
```


### [2026-09-14T00:53:57.535Z] TOOL RESULT

```
leaf 613 ['بالف کشیده ویکاف زده ءآدم جوان و اول مرا', '؟الث و دال بی نقطه بالف کشیده و بضای\u200cشطه\u200cدار']
leaf 614 ['بالف کشیده . بمعنی طافت و آرام و صبرباشد -']
leaf 615 ['داشته باشد - و خانه\u200cای را نیز گوبند که\u200cبربالای', 'است که خانةٌ تابتانی - و بالاخانه  -\u200f وکنجیته.', 'بجهت پوشیدن خانه بر بالای چویهای بزر که', 'بردارند و با از دنبال بیاورند - و درعنه را یز']
leaf 616 ['" پرو بال داشتن « کنابه اززوروفوت']
leaf 619 [' *\u200f پهلوی۳۵۸۲۳2 (حاشیه - لبه \u200f کناره) «ناوادیا ۱۹۶ نیز بمعنی بال\u200cویر « اونوالا']
leaf 620 ['پومیده و رکوی سوخنه باشد که بربالای\u200cسنکه', 'خدزمین وآب وگیاه وستوران و آنش درکارند . همانها بشکل ستار کان دباله دار بانشثر فرعتة.']
leaf 624 ['پژُمرده کردن ۰ اذبال :']
leaf 627 ['بالف کشیده و سکون سین سعقص ونای قرشت »', 'پسالتن ۴ ه بنتم اول و انی بالف']
leaf 628 ['ببال همت پرواز عروج بمدارح کمالات حفانی', 'بالف کشیده. برسرکاری رفت نکه قبل\u200cازین شروع']
```


## [2026-09-14T00:54:03.314Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==617' BQT_v1_pages.txt | head -60",
 "description": "BQT leaf 616 par entry"
}
```


### [2026-09-14T00:54:04.354Z] TOOL RESULT

```
 یلووپ‎
پرواص » بر وزن المای,بنمنیلاسه
بائد که دست سودن بر چیزی است - ویممنی
دانسئن هم هست - و دراز کردنر! نیز گوبند -
و بمعئی خلاص و نجات - و فراغ و پرداختن
هم‌آمده است - و تری و بی‌را دز کفه‌ایدا ه
پر و اسیك - بمنیدست سودولاسه کرد
بجهت میز درشتی ونرحی ۰
رو اسیدن » بر وزن سر خاربدن .
بمعثی دست مالیدن ولامسه کردن - و ترس‌دن
و واهمه‌نمودن باشد .
پر و اسیكه » بروزن ترسانیده » ,یعنی
دست مالیده و لامسه کرده بجپت نمیز درشتی
ولرعی ۰
بروان بر وزن‌مروان» نام‌ثهرست
ترديك بفزلین؟ - و چرخ ابرشم تاییرا پیز
کوند بمنی چرخی که ابربشم را بدان از پبله
بر‌آورند وآن چرخ را بای میگرداشد .
پروافلث؟ - بر وزن ابوانك » دام
جالورست که "
فربلد کنان بیش
پیش شیرمیرود
علجاتوران دیگر
آوازاورا شنیده
بداند که ثير
می‌آید وخودرا
بکناری کشند .
کویند پی‌ماندشیر دا میخورد و کنابه ازییش
(۱) خم ۳: باانان .
رولشگرهم‌هست» رحمرب‌آن فروائق است؟ 7
رو اه ه بروزن فرزانه » ممروف‌است
وآن جالور کی باشد که شبها خودرا بشملهشمع
۳ چراغ زند ات
وجانوربر! نیز گفتمانه
که پیش پیش ‌شیرفرباد
کنان رود و جانوران پروانه
دیگرراا ز] مدن‌شی رخبردارسازد * -وحکم‌وفرمان
سلاطین را نیز گویند۷ .
" پرو بال داشتن « کنابه اززوروفوت
وقدرث داشتن باشد .
پروهای - با بای فارسی بر وزن سر
وپای, بمعئی تاب وطاقت رفدرت وتوانایی‌باشد .
یرود - بفتح اول وضم ثانی و سکون
ثالث و رای قرشت بروزن ضرور » بمعنی پبوند
بود مطلفاً واه پوند اسان باسان (۱) و خواهء
درخث با درخت باشد» و بفتح اول وسکون انی
هم آمده است که بر وزن زر گن باشد. و فراویز
و سنحافی جامه را نیز گویند ۸
پر ورد گاد؟ ت مرون است جل
شاه - و کنادد از بادشاه لمز هت و او را
پرورد کار گونه و پرورنده هم : کویند و بعربی
رب النوع خوانتد*۷.
لیر وردن"- بروزن سر کردن»ممروف
است - و بمعنی پرستش و پرستیدن هم آمده
ِ_ِ
است. » « حدودالمالم ص۹4 .
۴ - وآن سیاه کوش
قبه درجضة ۳۸۳
(بر های قاطع 0۴)
```


## [2026-09-14T00:54:14.910Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in range(596,618):\n    p=pages[i]\n    lines=[l.strip() for l in p.split('\\n') if l.strip()]\n    print(i,'|', ' / '.join(lines[:2])[:110], '||FOOT:', ' / '.join(lines[-2:])[:90])\nEOF",
 "description": "Scan BQT v1 leaves 596-617 headwords"
}
```


### [2026-09-14T00:54:16.056Z] TOOL RESULT

```
596 | بحطیجه / بتطیح - با لامبروزن زنگیجه:بمعنی ||FOOT: است. یاب. والد » اب. بایا. ۱ / ۲۳ ۲ ۶
597 | مت ۳۱۲ / فد ۱۵ - بروزن‌فرسود؛ بمععنی‌سلامت ||FOOT: » بدید -بفتح اول. بهلوی 4 0۵ د«یرند که .کرنامه 44۰ ؛ فر اوستانااه 00۳02 / «اسشق ۲۷۸۹ , نبر
598 | پر قتتکاد ۱ سباعان بالفکنیدوبرای / قرشت زده ؛ بستی فبول کننده و فرماببردار ||FOOT: ۳ بب رکه ۱۸۰و رك: اسشق ٩۲۹۱‏ . / ٩‏ - « چون خفل بزرکه علی بابات آعد
599 | در بای فارسی / بر - فتح اول و سکون ثانی» هحروف ||FOOT: ۲ « 4 . ۲ ص 6۱۹۲ ؛ هملولبالب لبریز. ۴ - ۵۱۷۵ قاانا۸۵ «لت‌ناه » . / ۵ - معرب‌آن فرزوق «مجمم
600 | فر ) گنف ه باکاف قارسی بروزندهاوند, / ماضی پرا کندن است بعنی‌متفرق ساخت ویر بشان ||FOOT: ۸ رك: ایرهام . ٩‏ - وك : هم دمتا / (برهان فاطع ۲ )
601 | پر با له - بروزن هرساله. بمعنی پربال / ایت که خان ابتانی باد. ۱ ||FOOT: «لفت نامه ۴ . / بقه درصفحةً ۳۷۸
602 | هر تو اس 35 / لیزه وعلم بندند - و قطاي ۴ را نیز کنتداند " ||FOOT: -لوعی‌از حر کبات 20681041117 0107998" ازتیر2 سداییان 18000120625 « ک نکلاب ۲۱۵ ۰۰ / ۷ م با
603 | پر یی ۱ ۰ بر وژن پروین ؛ حساری / باشد که از خاروخللاشه وشاخ درختان بر دورباغ ||FOOT: بیکی دست‌می خالص ایمان نوشتد بیکی دست د کر پرچم کافر کیرند. / مولوی بلخی رومي -
604 | پردا / پرد بمنی يك لای و دو لای با يك ته و دوثه - ||FOOT: ۵ رل : ی رکار . / «لنت نامه > .
605 | پرنح / پردختن- بر وزن برجن ۰ مخفف ||FOOT: ۴ - قعربان / چنین کفت باپرده داران اوی
606 | پرده دار فلك / پرده داد قلاك - کنابه ازماء است ||FOOT: بر دخسش بر » اثر سبلت. سقلابی / یه درصفحة ۳۸۳
607 | -_۳۸۳ / و ثالكث بتحنالی رسیده و واو مفتوح بنون ودال ||FOOT: از پی داغ آتشی افروخته خورشید واو. " / فرخی سیستانی. «لفت نامه» ۰
608 | ستو! بکر اول و #الی وسکون / الك و ضم فوقانی و واو ساکن . بمعنی پرستكث ||FOOT: برسنیدن بادشه خوار کرد . فردوسی طوسی. / ( برهان قاطع ۲ه)
609 | ویو - / پر سیاوش" « بفتح‌اول وسکون‌نانی ||FOOT: درطول باعرض با ارتفاع بدون وسیله با بانکاء / بو ای دراز ) نیزه) ۰
610 | پر گال4 - بر وزن‌هرساله " بمعنی‌حصه / و پاره ولخت باشد -- و پینه ووصله رائیز گویند ||FOOT: پرکست ۳8۴8950 اندر یزدان مینیوان (مپنوبان) ۱ (ر) کیثیان (کیتیان)» ا(و) مردمان. ا(و) / شبه 
611 | - پر۳ - ۳۳ کی / هر کم -_بفتح‌کاف تازی بروزن پرچم؛ پر و لك - باعاف فارسی بروزن‌مفاوك, ||FOOT: رود کی استاد شاعران جهان بود سديك ازوی توب یکسایی ؛ پر گست ! / 1 کایی مروزی .
612 | پرخر / و فرزندیر! نیز گفته‌اند که عاق رعاصی پدر ومادر ||FOOT: چون سسنگه دیگیابه هقعه برجوزا کنار چون شرار دمگیایه یش‌او خیل‌پرن . / «منوچهری دامفالی۸».
613 | - و۳ - / منازل قمرحم هت۱ سویمعتی دیروز عم گفته‌اند ||FOOT: سد دستی. ركك : برن (حاشیه) . ۴ رك : پراداخ و برنداق . ۴- از : بر ند / ( جر شمشیر ).۲+ آور 
614 | پرعدوار / و ثل وار ۱ نتمولنانی‌وسکون ||FOOT: و در شم رکله بتشدید آید: / خمانف قد سیاز واندك سای ر‌ بر نله وهردم چاریای. فردوسی طوسی. «ل
615 | و قری وییم وباگك٩‏ -و سروب رکه را نی زکوین / و بمعنی داشتن (۱) و فرات - و پرداخت - ||FOOT: است. دهمن». " ۵ - بدین معلی مصحف «یدواز» است. (< مم) . / ۳ ره : بروار.
616 | یلووپ‎ / پرواص » بر وزن المای,بنمنیلاسه ||FOOT: قبه درجضة ۳۸۳ / (بر های قاطع 0۴)
617 | رو دش" « بر وزن سرزش » بمعنی / پروردن - و پرسنش و پرسنیدن باشد - و کتابه ||FOOT: ۳۵۲۷25 «یب رکه ۰۱۷۱ ؛ تربیت کردن ۰ پرورش دادن , آموختن؛ و ترییت شدن: / برآن پرورد کش همی‌پ
```


## [2026-09-14T00:54:27.656Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in range(590,650):\n    p=pages[i]\n    m=re.findall(r'برهان\\s*\\S*\\s*قاطع[^\\n]{0,12}|قاطع\\s*[۰-۹0-9]{2,4}',p)\n    print(i, m[:2])\nEOF",
 "description": "Extract Borhan page footers"
}
```


### [2026-09-14T00:54:28.796Z] TOOL RESULT

```
590 []
591 []
592 []
593 []
594 []
595 []
596 []
597 []
598 []
599 []
600 []
601 []
602 []
603 []
604 []
605 []
606 []
607 []
608 ['برهان قاطع ۲ه)']
609 []
610 []
611 []
612 []
613 []
614 []
615 []
616 ['قاطع 0۴']
617 []
618 []
619 []
620 []
621 []
622 []
623 []
624 ['برهان قاطع\u200cهه)']
625 []
626 []
627 []
628 []
629 []
630 []
631 []
632 []
633 []
634 []
635 []
636 []
637 []
638 []
639 []
640 []
641 []
642 ['قاطع9۷']
643 []
644 []
645 []
646 []
647 []
648 []
649 []
```


## [2026-09-14T00:54:42.474Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in range(596,626):\n    for l in pages[i].split('\\n'):\n        if 'اوستا' in l or 'پهلوی' in l or 'پپلوی' in l:\n            print(i,'|',l.strip()[:160])\nEOF",
 "description": "Mo'in footnotes in par region"
}
```


### [2026-09-14T00:54:43.635Z] TOOL RESULT

```
596 | * - ازاوستا 0۵۱۸1.۲2۳020 ۵ (فی: رام) «اسشق ٩۲۸۷‏ :
597 | ۱ - پهلوی 04ت +08 «نولدکه . کارنامه »٩۵‏ (قس : درود) «اسشق ۲۸۸ : «( علی
597 | » بدید -بفتح اول. بهلوی 4 0۵ د«یرند که .کرنامه 44۰ ؛ فر اوستانااه 00۳02
597 | «اسشق ۲۷۸۹ , نبرک پهلوی آنرا 16 084 نوشنه. «یب رکه 0۷»؛ آشکار. سامان,
598 | - پپلوی
599 | - پرجنم اول, پهلوی کلام داستق ۹۵4», 1۲۲ا۳] دنیب رکه ۱۸۷ اوستا 0676103 (ممتلی)
603 | ۱ - مرکب از : پر - اوستا :025 ( پیرامون ) + چن (از : چیدن ) جمعاً یرامون
604 | ۴ پپلوی
610 | ت» پر لست - در فصل ۵۳ بند ۷ رسالةٌ پهلوی مینوخرد چئن امد : «۱(و) اگر
614 | ۲ پهلوی 08۲0130 تاوادبا
615 | ۴ - هرن *بروار» فارسی رابمعنی اصطبل آورده و گوید: دراوستا 02171۷2۲202 ۵ قی :
615 | 2 . 21۴1 (باروء طوبله)؛ پهلوی ۳3۲۷27 ودرحاشبه امن‌یت خاقانی شروانی راکه برولررا
619 | ر گرامی باشد - ویزبان پهلوی ماهی را گوشد.
619 | *‏ پهلوی۳۵۸۲۳2 (حاشیه - لبه ‏ کناره) «ناوادیا ۱۹۶ نیز بمعنی بال‌ویر « اونوالا
620 | ۵ پپلوی 0۸۲۳۵6
620 | استاد پورداود ورك: بشنها ۱ص ۳۰-۲۹) . درپهلوی ۳2116 ارمنی ۳2۲3» اففانی [۳8۲«اسشق
624 | ۴ - پارسی باستان_ 00202 ۵ + تافقا2 ؛ پپلوی 25۳15020 ( بازند 0ناعدم) ,
624 | * پزمر دن و پزمریدن - بکسر اول و ضم سوم و فتح پنجم » پارسی باستان أکقا08 ( اوستا
```


## [2026-09-14T00:54:54.279Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==621' BQT_v1_pages.txt | head -40; echo \"#### leaf599 ####\"; awk 'BEGIN{RS=\"\\f\"} NR==600' BQT_v1_pages.txt | head -25",
 "description": "BQT leaves 620 and 599"
}
```


### [2026-09-14T00:54:55.749Z] TOOL RESULT

```
پرهازه .
و پر؛ آسیا (۱) و دولاب و امثال آن باشد -
وبسمنی‌پهلو نیز بنظر آمدم‌است که‌بعربی جنب
خوانند .
پر هازه - بر وزن دروازه . چوب
پومیده و رکوی سوخنه باشد که بربالای‌سنکه
چشاق گذاشته چشماق (۲) بدان زنند نا آتشل
درآن افتد .
پرهام - بر وزن فرجام » نامی است
پارسی باستانی و معرب آن براهیم است٩‏ .
پر هتن - بفتح الك و سکون خای
غطه دار بر وزن برجستن » بمعنی ادب کردن
عاشف 6 فبکن تالث هم‌آمده است؟ ۲
سهوده را گوبند - و جامه ای که از تاش
۱ - ركگ : ایرهام .
و حرارت آتش رنگه کردانیده شوختن ترديك
رسمه باشد ۰
. فر هون - بروزن مجنون. دایرم وهر
چیز میان‌خالی را گوبشد مانندچنبر وطوقوحالة
ماه و امتاز آن۴ ۰
ثر هیلقن - بر وزن‌انگیختن» بمعنی
ادب کردن باشد.
پر هیز * ه بر وزن پرویز » آست
که بعریی حذر و احتراز میکویند؟ - و ترد
محققیناجتناب از ماسویاه تمودن باشدوبمعنی
تری و بیم و نگاهداشت‌خود ازمضرت. و بمعنی
تفاوت هم بنظر آمده ات
ری ۲ بننع اول وکر ثانی وسکون
نحتانی , همروف است که قیض دیو باشد -
جهل کشبده بگردجان تو پرهون.
تاصرخسرو بلخی. «لفت نامه».
۱ - چهل روز با لشکر اویز بود
۵ پپلوی 0۸۲۳۵6
کهی رزم ر که روی برهیز بود .
فردوسی‌طوسی. «لفت‌نامه».
باهمال خود انسائرا می‌فر سمف. دراومتا بری جنس موّث «حادو» مصوب شده که ازطرف اهریمن
گماشته شده تاییروان مزدیسنا رااز داه راست مثحرف سازد. همجن پربان درزمرة میاه اهردمن
خدزمین وآب وگیاه وستوران و آنش درکارند . همانها بشکل ستار کان دباله دار بانشثر فرعتة.
باران در ستیزماند ناوی راز بارس گی بازدارند وزمین رااز خشکی وبران سازه. ( از بادداتهای
استاد پورداود ورك: بشنها ۱ص ۳۰-۲۹) . درپهلوی ۳2116 ارمنی ۳2۲3» اففانی [۳8۲«اسشق
#### leaf599 ####
در بای فارسی
بر - فتح اول و سکون ثانی» هحروف
است که بال و پر باشد و عربان رش‌خوانند ۷
واز سر کتف نا سرانگشتانرانیز گوشد - وروشنی
وشماع و پرتو را هم کنته‌اند؟ - و دامن و کناره
حرچیز باشد همچو پ رکلاءو کنار؛ کلاه»ویرببابان
و پربینی هم بنظر آمده است که دامن بپابان
وکناره بینی باشد و ترك کلاهرا تین کفته‌اند -
و بر که درخت را هم هیگوبند - وبمعنی پر
آسیا وچرخ دولاب و امثال آ هم همست؟ .
پر اذدان - بح اول رذال له دار
بر وزن برادران ؛ برنده ایست شکاری از جنی
سره چشم مانند چرغ و بحرک » لیکن بضایت
پاکیزه منظر و نيك اعضاه باشد » رآنجه‌ازآن
سرخ رنگگ باشد بهتر است وآنرا پسندیده آند
وآنچه در کوء تولك کند بعنی پر بریزد بکاری
نیابد و آنجه درخانه تولك کند بسیار خوب‌میشود
و آنرا بجربی زمج خوانند؟ .
پرادلن - یکس اود و رای فرشت
: ژند ویاژند.
بر وزن رباحين » بلغت زند و پازند (۱) بمعنی
خوب ولیکو باشد ۰ و بفتح اول هم درست‌است
پر ازده؟ » بنتم اول و ثانی بالف
کشیده و بزای‌شطه دار زده ودال بی تطهٌمفتوح»
پاره‌ای از خمیر باشد که بجهت بك نه نان گرد
```


## [2026-09-14T00:55:07.880Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==624' BQT_v1_pages.txt | head -30",
 "description": "BQT leaf 623"
}
```


### [2026-09-14T00:55:08.972Z] TOOL RESULT

```
۵ بفتح اول وسکون‌ثانی ودالابجد,
بمعنی خون باشد که بعرچی دم گویند , و بعضی
بمملی جان کفته‌اند که بعربی روح خوانند .
پز ۱2۵ بفتح اود و دال ابجد بروزن
نفزكك » کرمکی باشد که کندمرا خورد و خراب
سرشك ؛ طب و جراح را گوبند ۴ - و بفتح
اول و ثانی بممنی جغد باخد, و آن پرنده ایست
حمروف و حنسوی . #۶
۱ فز عیّك » نم اولوغین قطمدار وسکون
ثانی ونون ودال بی‌نقطه. بممنی بزغنج است‌وان
پته مانندی باشد بی مفز که بدان پوست را
دبای کنند 3
وی - ختح اور و سکون ثانی و واو
بتحثانی کشیده ۰ فرومابه تربن مردمان را گومند
و بعربی ارذل خوانند ۰ بفنح اول و شانی «م
آمده است . #
لِر - بفتح اول وسکون ثانی» زمین پست
و بلند و کوه و کتل را گویند» و ؛عربی عضه
خوانند ۴ - وبسسنی کهنه و مندری هم هست -
و کل کهثه و نرم را نیز گویند - و بمعنی چرل
وریم هم آمده است ۴ - و جنم اور برف ریزها
که از شدت هوای سرد مانند ز,ك از آسمان
بریزد - و چوبی باشد زهد که بدان مداوا کنند
و آن‌را بعربی وج خوانند .
| گن» باعاف فارسی بروزن مساکن .
زشت ویلید وچ رکن را کوند ۵
او ند ‌ بروزن دهاو ند ۰ چودی باشد
کهدریس درانداز ند نادر کشوده نگروو؟ وجوب
کازران را نیز گویند ۰
له نم هردو بای فارسی و سکون
```


## [2026-09-14T00:55:24.719Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==623' BQT_v1_pages.txt | head -20",
 "description": "BQT leaf 622"
}
```


### [2026-09-14T00:55:25.794Z] TOOL RESULT

```
ح‌ِ ۰ 4 بت .
سازد ٩‏ ,
فر لصو ع اب وزن کئبدن مشتف
برمشان باشد ۴ - و بمعی افشاندن و برشان
کردن هم‌آمده است .
۱ پر یشیك ه مانی پربشیدن است یعنی
پرشان کرد و براکنده ساخت ٩‏ .
بر شین « بر وزن پری دسن .
سمنی بدحاوپریشان کردایدن و بیخود گشتن
بائد ؟ .
پریشیده ۴
ممعنی بر شان شده و برباد داده و عتفرق ساخته
بر وزن پری دنله ۰
باشد .
فری گر فت - کسی راگونن که جن
باو ار شده باشد و او از مفیبات خبر دهد و از
ماضی و مستقبل گوید » و دزد برده بیدا کند»
و هر چیز که در خاطر " بگنرانی و ازو بیرسی
بگوبد. واکی خوابی دیده باشی وآنرا فراموش
کرده باشی ازو بپرسی جواب کوبد و تعبیر
```


## [2026-09-14T00:55:42.400Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== DRM parna/plume ===\"; grep -n \"parna\\|parəna\\|plume\" DRM.txt | head -20; echo \"=== DRM pul ===\"; grep -n \"pont\\|puhl\" DRM.txt | head -10",
 "description": "grep Darmesteter"
}
```


### [2026-09-14T00:55:42.494Z] TOOL RESULT

```
=== DRM parna/plume ===
7854:Le  dialogue  pouvait  durer  longtemps  :   il  dure  encore.  Les deux  écoles,  celle  de  la  tradition  et  celle  de  l’étymologie,  ne  se sont  guère  accordées  que  sur  un  point  :   c’est  que  les  deux  mé- thodes sont  incompatibles  et  portent  ceux  qui  les  suivent  aux deux  antipodes,  et,  comme  l’a  observé  M.  Spiegel,  il  est  telle partie  de  l’Avesta  qui  prend  un  aspect  si  différent,  sous  la  plume de  deux  traducteurs  d’école  différente,  qu’un  profane  serait  in- capable de  soupçonner  que  c’est  le  même  morceau  qu'il  vient de  lire  deux  fois.  Cependant,  depuis  quelques  années,  il  sem- ble que  les  deux  écoles  tendent  a   se  rapprocher  :   d’une  part, M.  Spiegel  n’a  jamais  contesté  à   la  méthode  comparative  le droit  de  contrôler  au  moins  les  données  de  la  tradition  ;   et  d’autre part,  deux  des  représentants  les  plus  distingués  de  l’école  com- parative, M.  Jollv  et  M.  Hübsehmann,  ne  repoussent  point  a priori,  ni  en  toute  occasion,  les  données  de  la  tradition.  Il  nous
=== DRM pul ===
697:fravashi,  ange  gardien  ; kasha,  gouffre  ; pesliu,  pont; peslui,  payé; asha,  saint; ashavan , id.  ; peshana,  bataille; bâshar,  cavalier; hvâshar,  mangeur;
1533:Il  se  change  en  l 2   dans  : vâraghna,  corbeau Hara- herezait !   ("nom  de  montagne) peretu,  pont
1554:3.  Peut-être  puhl.  Cet  exemple  rentre  d’ailleurs  plutôt  dans  les  groupes.
2050:*   Partliaviya,  parthicus peretu,  pont  (*perethu)  pûlml
6331:§   237.  van ,   vân,  vâna.  —   Ce  suftixe  joue  a   l’��gard  des mots  faits  h   peu  près  le  même  rôle  que  a   s   : de  pul,  pont,  pulvânpulvan  chemin  en  rebord
8634:Les  trois  mots  que  nous  avons  laissés  sans  traduction  peu- vent être  entendus  de  deux  façons  différentes,  selon  (pie  l’on reconnaît  dans  cinvat  le  pont  mythique  de  ce  nom  qui  conduit les  âmes  de  la  terre  au  ciel,  ou  qu’on  en  fait  un  participe  pré- sent gouvernant  ushtànem.  Ushtâuêm  signifie  la  rie  (pehlvi  jtin et  khayâ );  jayâi  est  le  datif  d c   jaya,  ir.Yz  A£-;s;j.evov,  de  sens  in- certain.
8635:Haug,  dans  une  première  traduction  ’,  faisait  de  cinvat  le  pont de  ce  nom,  et  de  cinvat-ushtânem ,   une  «me  (de  pont)  Cinvat,  c’est- à-dire  «capable  de  passer  le  pont».  —   A   la  même  série,  appar- tiennent la  traduction  d’Auquetil  :   «qui  veut  rendre  purs  et dignes  de  passer  le  pont  ceux  qui  mènent  une  vie  criminelle», et  celle  d’Aspendiârjî  :   tathâ  nêk  cinvat jmlno  mârnâr  «   et  destruc- teur du  bon  pont  Cinvat»  ou  :   «et  destructeur  du  bien  du  pont Cinvat»2.
8645:Quant  à   la  forme,  cinvat-ushtânem  est  un  de  ces  composés  si fréquents  dans  les  Védas  et  en  zend,  où  le  déterminé  est  un participe  présent  et,  contrairement  a   la  règle  générale,  est  placé en  tête  du  composé.  Quand  le  premier  terme  de  pareils  com- posés offre  difficulté,  la  première  chose  a   faire  est  de  chercher si  l’on  ne  retrouve  pas  le  même  composé  sous  forme  ordinaire, le  participe  étant  remplacé  par  une  forme  nominale.  Il  suffit d’ouvrir  l’excellent  lexique  de  M.  Justi  au  mot  ushtânem  pour trouver  immédiatement  le  composé  ushtânô-cina.  Le  mot  se trouve  Yt.  XIX,  48  :   at  âtarsh  zayta  paiti  apa  géurvayaf  frakh- shni  ushtânô-cinahya  yatha  azhish  biwivâo  âonha  :   «alors  Atar retira  les  deux  mains,  sous  l’empire  de  l’amour  de  la  vie,  tant Azliis  était  effrayant».  —   D’une  part,  la  valeur  donnée  par  la traduction  pehlvie  à   cinvat  et  transportée  ici  à   cina  donne  un sens  concordant  avec  le  contexte  :   d’autre  part,  ushtânô-cina, étant  la  contre-épreuve  de  cinvat-ushtânem,  condamne  défini- tivement toute  tentative  de  jeter  sur  ce  dernier  le  pont  Cinvat.
8654:2.  Le  zend  a   l’équivalent  de  cette  expression,  Yt.  X,  32  :   ham  hîsh  zao- thrdo  cinmainê  baraiiuha  :   reçois  ces  libations  à   plaisir  (agrée  les).  —   Il n’est  point  jusqu’à  ce  mot  cinman  que  n’ait  poursuivi  le  pont  Cinvat;  Win- dischmann  (dans  son  Mithra )   traduit  :   trage  sie  hin  zum  Sammelorte  (Cin- vat) :   porte  les  au  lieu  de  la  réunion,  le  Cinvat.
8770:qui  renvoie  k   un  primitif  perse  *yâta-gauba.  Or  gâta  paraît  plu- sieurs fois  dans  l’Avesta;  dans  le  Vendidad  XIX,  20  (97)  il  est traduit  bahr  «   part  »   ;   dans  Y   Afrigan  I,  1 1,  il  est  traduit  dânakala «part  de  dons»;  dans  le  Vendidad  XX,  1   (4)  paraît  un  adjectif yâtamant  qui  est  traduit  bahrômand  et  glosé  tuvânîk  «riche». Dans  le  premier  passage  du  Vendidad ,   il  est  dit  que  l’âme  du mort  au  pont  Cinvat  va  réclamer  (paiti  jaidhyêinti)  son  ydtem gaêthanâm,  c.-k-d.,  dit  la  traduction  «la  part  de  biens  terrestres (bah ri  gêhân)  qu’elle  a   donnée  ici  bas  (dâtera  açtvaiti  aiihvô)  ». Il  est  clair  que  nous  avons  ici  une  allusion  au  jâdangô.  Le jâdangô,  le  jâtak-gôb  est  donc  littéralement  «celui  qui  dit  la part»,  soit  que  cela  ait  signifié  d’abord  «celui  qui  fixe  la  part contributive»  ou  mieux  «celui  qui  dit,  qui  pêche  de  donner part».  Le  sens  d’intercesseur  se  développa  de  lk  plus  tard  quand le  sens  premier  fut  obscurci.
```


## [2026-09-14T00:55:43.704Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB parena/par ===\"; grep -n \"parena\\|Flügel\" HUB.txt | head -20",
 "description": "grep Hübschmann for par"
}
```


### [2026-09-14T00:55:43.757Z] TOOL RESULT

```
=== HUB parena/par ===
9272:dan *fiiegen {parran *fiiegend' Fird. I, 440, 126), zd. parena-;
```


## [2026-09-14T00:55:52.819Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('DRM.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint('total leaves',len(pages))\nfor n in (308,650):\n    print('=== leaf',n,'===')\n    print(pages[n][:900])\nEOF",
 "description": "DRM leaves 308 and 650"
}
```


### [2026-09-14T00:55:53.953Z] TOOL RESULT

```
total leaves 756
=== leaf 308 ===
miques  et  les  noms  de  pays  concourent  il  produire la  même  erreur,  en  multipliant  les  noms  en  akân  : phi.  Pâpak-ân,  fils  de  Pâpak,  rjevej
Shâhpûhrak-ân,  ville  de  Shapur,
Âtarpâtak-ân,  Adarbaijân
de  shah,  roi
De  là  un  suffixe  gân,  marquant  relation,  similitude,  origine  : shâhigân  royal.
khudâigân  divin.
J   dehgân  campagnard,
|   transformé  en  deliqân.
râhgân  abandonné  sur  la  route.
»   khudâ,  dieu »   deh,  village »   râh,  chemin
§   218.  Suffixe  âna .   pehlvi  ânak.  —   Le  suffixe  an (pri mitif  perse  âna),  étant  remplacé  par  sa  forme  vocalique  dérivée âna  (ph.  ânak),  produit  de  même  un  suffixe  abusif  gâna, ph.  kânak  jry  II  sert  à   former  des  distributifs,  ayant  pour  point de  départ  le  mot  evak,  un  (p.  151)  :
;rw  évak-ânak,  d’où  ib  yagâna,  et  par  analogie  du-
gâna,  etc.
Ce  suffixe  ânak, 
=== leaf 650 ===
em  priores  contemplentur,  adimere  ad  præ- sens»  (VIII,  34).  De  même  saint  Ambroise  dans  l’Hexamerou (VI,  4)  :   «   Lupus  si  primo  hominem  viderit,  vocem  ei  eripit  et eum  tauquam  victor  vocis  ablatae  despicit»  '.  De  même  Isidore de  Séville  :   «lupus  de  quo  rustici  aiunt  vocem  hominem  per- dere,  si  eum  prior  lupus  viderit  »   (Etymol.'X. II,  2,24;  cf.  I,  37,  28). Virgile  ( Ecl .   IX,  55),  Théocrite  ( ld .   XIV,  22)  et  Platon  ( Rep .   X) font  h   cette  croyance  des  allusions  très  claires.  11  paraît,  par les  termes  de  Laisnel  de  la  Salle,  comme  par  ceux  de  ces  divers auteurs,  qu’il  s’agit  bien  aujourd’hui  et  qu’il  s’agissait  autrefois d’une  croyance  existant  parmi  le  peuple;  elle  se  traduit  même par  certains  préceptes  pratiques  pour  détruire  l’effet  du  malé- fice, et  l’emploi  de
```


## [2026-09-14T00:56:00.705Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"par,  aile\\|aile\\b\" DRM.txt | head -15; echo \"---\"; grep -n \"parvâna\\|parvana\\|parîdan\\|paridan\" DRM.txt | head -10",
 "description": "grep DRM for aile/par"
}
```


### [2026-09-14T00:56:00.782Z] TOOL RESULT

```
1001:1.  Le  valàk  est  cité  parmi  les  oiseaux  ( Bund .   31.  Il;  47.  8.  13); la  tradition  le  traduit  kâgado,  corbeau,  comme  elle  traduit  vâraghna  :   k dans  valûk  n’est  qu’une  représentation  imparfaite  de  <jh  ^comme  dans pour  laglia  (cf.  p.  25);  la  seule  altération  est  un  déplacement  de  quantité. Vâraghna  semble  formé  de  vâra-ghna,  «qui  frappe  de  la  queue»,  peut-être «qui  frappe  de  l’aile»;  il  serait  identique  au  vârenjana  ( Yt .   XIV,  31).  Mais le  sens  primitif  a   dû,  en  ce  cas,  être  rapidement  oublié  ;   autrement,  le  mot ne  se  serait  pas  corrompu  comme  il  l’a  fait,  et  il  commencerait  par  bâl,  J4-
1940:2°  parena,  aile
5606:par  aile  pare-na.
6334:de  par,  aile,  parvâna  à papillon.
---
3538:parvâna  khvêshtan  bekushad
6334:de  par,  aile,  parvâna  à papillon.
6335:Le  suffixe  pehlvi  est  vânak  y")  : parvânak  papillon.
```


## [2026-09-14T00:56:06.081Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('DRM.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nimport itertools\nfor target in [1940,5606,6334,2050,1533]:\n    pos=sum(len(l)+1 for l in lines[:target-1])\n    print(target,'leaf',txt.count('\\f',0,pos))\nEOF",
 "description": "DRM leaf numbers for par lines"
}
```


### [2026-09-14T00:56:07.220Z] TOOL RESULT

```
1940 leaf 122
5606 leaf 299
6334 leaf 325
2050 leaf 125
1533 leaf 105
```


## [2026-09-14T00:56:14.051Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('DRM.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in range(296,332):\n    head=pages[i].strip().split('\\n')[0][:60]\n    nums=re.findall(r'\\b(2[0-9]{2}|3[0-9]{2})\\b',pages[i][:200]+pages[i][-200:])\n    print(i,nums[:4],'|',head)\nEOF",
 "description": "DRM page numbers"
}
```


### [2026-09-14T00:56:15.250Z] TOOL RESULT

```
296 [] | orte,
297 [] | les  formations  du  suffixe  ma  se  sont  réduites  à   m,
298 [] | cette  formation  :
299 ['225'] | ême  absolument  dans  :
300 [] | dans  une  période  antérieure  à   celles  que  nous  con- 
301 ['214', '218'] | ne  pronominale.
302 [] | r-$  zîvandak, de  *zîvant-,  participe  de  zîv,  sscr .   
303 [] | wei-“,  Qpitdmân,  le  fils  de  Çpitama.
304 [] | ��un  com- posé à   sens  adjectival  :   khôb  bînâ  bbo  v
305 [] | a,  sans  perdre  pour  cela  la  forme  plus simple  h   te
306 [] | la  forme  dérivée  : ph.  dôshak  yoy,  désir;  z.  zaosha.
307 [] | de  cinq
308 [] | miques  et  les  noms  de  pays  concourent  il  produire la
309 ['219'] | riel  de  zinda,  «   vivant  »,  et  qui  est  en  réa- lit
310 ['270', '224'] | ce  sens  dans  quelques  dérivés; mardum-a,  dukhtar-a  (p.
311 ['222'] | fixe  î   (ê).  Le  suffixe  î(ê)  1   ^   a   des  valeurs 
312 [] | perse  hya . . ava  renversée  :   martiya  hya  draujana  a
313 ['264'] | ;   le  groupe  y   a   se  contracte  en  î,  comme  il  le
314 [] | OVT,  impureté
315 [] | créer,  on  forme  le  mot  dahishn  iv*e-,o. qui  signifie 
316 [] | iishishn ,   vêtement. bakshislin,  largesse. dânishn,  scie
317 ['272', '227'] | i
318 ['359'] | k,  persan  îna,  comme  ân  avait  donné ânak  âna.
319 [] | de  «mal»  aux  dérivés  :   frârûn  suppose  un  dérivé *fr
320 [] | formation  prépositionnelle  comme  andarûn  auquel  il  s’o
321 [] | mploie  encore  comme  substantif,  car  il  est  sus- cepti
322 ['235'] | zend  ni  en  sanscrit.  Exemples  :
323 [] | hired-mand  :   sur  ce  type  sont
324 ['230', '237'] | tan-ômand  fort  (avec  le  vâvi  majhûl) ;
325 [] | �gard  des mots  faits  h   peu  près  le  même  rôle  que  
326 ['275'] | nâk  timide;
327 ['288', '253'] | qu’a  côté  de  kanya,  existait
328 ['289'] | il
329 [] | i-bâr  pays  de  rivières 3.
330 ['292'] | ’",  place  des  os,  cimetière. âtash-dân  place  du  feu, 
331 [] | gar  musicien1.
```


## [2026-09-14T00:56:26.294Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('DRM.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor n in (325,329):\n    print('=== leaf',n,'===')\n    print(pages[n][:1200])\n    print()\nEOF",
 "description": "DRM leaves 325, 329"
}
```


### [2026-09-14T00:56:27.556Z] TOOL RESULT

```
=== leaf 325 ===
�gard  des mots  faits  h   peu  près  le  même  rôle  que  a   s   : de  pul,  pont,  pulvânpulvan  chemin  en  rebord
de  angisht,  charbon,  angishtvâna  foyer
de  daçt,  main,  daçtvâna  bracelet
de  par,  aile,  parvâna  à papillon.
Le  suffixe  pehlvi  est  vânak  y")  : parvânak  papillon.
§   238.  Suffixe  nà.  —   Le  suffixe  nâ  nui,  U   ^U,  forme  des abstraits  :
tavg-nâi  ^Uibo,  angustiae,  de  tang,  étroit;  a   côté  de  tangî. firâkli-nâi  largeur,  d efirâkh,  large,  a   côté  de  firâkhî.
dirâz-nâ  Uj'y,  longueur,  de  dirâz,  long;  à   côté  de  dirâzî.
Le  point  de  départ  de  cette  formation  est  le  mot  pahnâ  LLfj, phi.  pahnâi  ou  pahnâk  -“Tel,  largeur,  de  palmn  (z. pathana), étendu,  qui  a   formé  un  abstrait  en  a   (âk)  et  a   créé  l’analogie  en faveur  d’un  suffixe  en  nâ.  Le  fait  que  ce  suffixe  est  bien  une création  de  l’analogie  paraît  par  la  formation  pehlvie  dirahnâ longueur,  (pii  ne  peut  s’expliquer  organiquement,  soit  que l’on  parte  de  daregha  ou  de  dranga  ou  de  drâj-ah.
1)  Peshotun.
2.  Lecture  de  Peshotun  :   la  transcription  parsie  est  vîmanql  (Minoklii- red)  que  M.  West  

=== leaf 329 ===
i-bâr  pays  de  rivières 3.
1.  Voir  p.  92,  n.  2.
2.  De  là  aussi  le  nom  de  la  côte  de  Malabar  ,bx_Lo  (la  côte  du  Malaya  : Malaya-pâ  ra) .
3.  Cf.  à<sr  ;   zinja  et  zinjîr ,   chaînes;  mais  l’étymologie  de  ces
19
290
Il  s’agit  toujours,  on  le  voit,  de  pays  où  l’on  aborde  par  les côtes;  de  la  l’emploi  dépara.
Il  ne  faut  pas  confondre  ce  suffixe  bar  —   para  avec  le  suffixe bar  marquant  itération  et  qui  est  le  sanscrit  vâra,  fois.  Bar ,   fois, est  un  mot  encore  indépendant  (p.  154)  : bârî  une  fois
bârliâ  l*>^b,  des  fois.
§   245.  bân.  —   Le  suffixe  bân,  ph.  pan  re),  forme  les  noms de  gardien  ;   il  vient  du  mot  pana  (zend  et  sscr.),  ce  qui  garde  : (   zend  râno-pâna,  ce  qui  garde  les  jambes,  caleçon  : i   ph.  rân-pân  rüA
ph.  pdç-pdn  rei*uei,  gardien.  p.  ^U^ob
marz-pdn  gardien  des  frontières.  cMjj*
çtôr-pân  rAs0-”,  gardien  des  bêtes  de  somme  (*çtaora-pâna). zînddn-pân  püwA,  gardien  de  la  prison.
gnv-pân  reiA,  armure  protégeant  le  cou(*  grîva-pâna)^\^jS.
Il  semble  avoir  pris  une  existence  indépendante  en  se  dé- tachant des  composés  sous
```


## [2026-09-14T00:56:35.672Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ntxt=open('DRM.txt',encoding='utf-8',errors='replace').read()\nprint(txt.split('\\f')[328][-1400:])\"",
 "description": "DRM leaf 328 bar suffix"
}
```


### [2026-09-14T00:56:36.789Z] TOOL RESULT

```
), formation  parallèle  à   nemô  (sscr.  namas).
289
vâr  âvar  ,*l  ,U yâr  yiîd  >b  ^b gûn  0?S
çtcîn
çâr  jbo
dêç
§   243.  bad.  —   Le  suffixe  -ôar/  jo  dérive  du  perse  -pati, maître,  pehlvi  pat  ?ei.
Pati  s’emploie  souvent  en  zend  comme  dernier  terme  de composé,  pour  marquer  les  titres  de  commandement  :
aêthrapaiti,  maître  du  foyer  1   (nom  du  prêtre  du  feu)
zantu-paiti,  »   de  la  ville
vîç-paiti,  »   du  village
nmânô-paiti,  »   de  la  maison
dahyu-paiti,  »   de  la  province
shôitlira-paiti,  »   du  pays.
aêthra-paiti  devient  le  phi.  êr-pat ,   p.  liêrbed  zantu-
paiti,  vîç-paiti,  nmânô-paiti  deviennent  le  phi.  zand-pat  vîç- pat  mânpat
Le  perse  avait  :
*magupati,  chef  des  mages  ;   d’où  magûpat,  p.  maubad *çpâda-pati,  chef  d’armée;  çprîhpat,  p.  çipâhbad  josb-^o.
On  trouve  encore  en  persan  :
kuhbad  ermite  ;   litt.  maître  de  la  montagne
bârbad  jo^b,  maître  des  cérémonies;  »   maître  de  la  cour.
§   244.  bar.  —   Le  suffixe  bar  s’ajoute  aux  noms  de  lieu, en  général  aux  noms  de  pays  maritimes.  C’est  le  mot  zend  para, côte  (cf.  dûraêpâra,  la  terre  aux  rives  lointaines)2  : hindu-bâr^jJjb,  le  pays  d’Inde,  l’Hindoustan.
Zang-bâr  ^bJbj,  le  pays  des  Zang  (côte  orientale  d’Afrique). daryâ-bâr  ,bb,j,  pays  maritime. nîd-bâr  ^b^,  région  fluviale. jû
```


## [2026-09-14T00:56:48.342Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON پاسپورت ===\"; grep -n \"پاسپورت\\|اسپرت\\|ترانسپورت\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20",
 "description": "grep Mo'in for French loans"
}
```


### [2026-09-14T00:56:48.423Z] TOOL RESULT

```
=== MON پاسپورت ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:28216:پاسپورت: ۲5:۲0 )٩(‏ پروانه برای 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:39405:پاسپورت؟ ج. تذا کر ( کم.) 
MON_part1.txt:28216:پاسپورت: ۲5:۲0 )٩(‏ پروانه برای 
MON_part1.txt:39405:پاسپورت؟ ج. تذا کر ( کم.)
```


## [2026-09-14T00:56:49.933Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hinüberführen\\|hinüberbringen\\|per-tu-\\|portus\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20",
 "description": "grep Walde-Pokorny Bd2"
}
```


### [2026-09-14T00:56:49.986Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:56:54.918Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28210,28220p' MON_part1.txt",
 "description": "Mo'in passport entry"
}
```


### [2026-09-14T00:56:54.968Z] TOOL RESULT

```
پاسبز: 027 (ص‌مر. امر.) مبانجی. 
۳ شوم قدم. 

پاسپار: 0۲ (امر.) پاساره لگد. 
(ص‌مف.) بای سبر» بی سیر ؛ لکدکوب. 
پاسپورت: ۲5:۲0 )٩(‏ پروانه برای 
آزادی رفت و آمد اشخاص از مملکتی به 
مملکت دیگر؛ گذرنامه؛ جواز عبور بته. 
تد‌کره» ساشرد. اجازهة عبور به کشتی 
ازرگانی از آب‌های ساحلی مملکتی.
```


## [2026-09-14T00:56:57.499Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"porta\\b\\|portus\\|Furt\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20; echo \"--- parona/Feder ---\"; grep -n \"Avestan  parona\\|par\\.na\\|Feder'\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10",
 "description": "grep WLD Bd2 for portus"
}
```


### [2026-09-14T00:56:57.621Z] TOOL RESULT

```
1721:Furt, Steg, Brucke“ (s. zum Sachlichen Meringer WuS. 1, 192 f.). 
1742:„Weg‘‘ (kann auch o-St. = gr. ndrog sein), arm. him ,,Furt, Weg^^ (Hiibsch- 
2562:(trotz Pick BB. 24, 295) wesentlich dasselbe wie gr. Jiogog „Furt“ (Kretsch- 
2568:jiogog „Durchgang, Zugang, Ubergang, Furt; Ausweg; pi. Einkiinfte^ (s. 
2612:jjDurchgang, Furt^^r av. pordtu-s m. f. (urar. "^prtii-s) imd pam-s 
2613:m. (urar. ^priu-$) „Durchgang, Furt, Brucke“ (liu-para'&iva’' „gut zu iiber- 
2614:schreiten“; gall, ritii- „Furt“ in Ritumagus, Angtistoritum, ir. j'ith in Huniar- 
2615:rith (K. Meyer Rc. 16, 89f.), acymr. rit, ncymr. rhyd^ corn, rit „Furt“; ahd. 
2616:furty ags. ford „Furt'‘ (hochstufig aisl. /jorftr „enger Meerbusen“ aus 
2620:NebengaBchen^'; daneben a-St. porta „Stadttor, Tor‘^ 
13001:bradau, yti „waten", brastd, brastvd „Furt (kotige), Durchwatstelle", brddas 
13006:albernes sprechen", braslis, brasJs „Furt", bridls „Weile, kurze Zeit" (*Gang- 
13011:Russ.-ksl, bredu, bresti „ durch eine Furt waten" (tiefstufig neprebrhdo)m 
13016:bredem, bresti „waten" usw.: r.-ksl., russ. (usw.) „Furt" (russ. brodmjj 
43366:durch etrusk. Yermittlung lat. sporta ,,geflochtener Korb“, Schulze SBAk. 
--- parona/Feder ---
```


## [2026-09-14T00:57:09.302Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2600,2625p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \"=== page tag ===\"; grep -n \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt | head -3; python3 - <<'EOF'\ntxt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\ni=txt.find('gut zu iiber')\nif i<0: i=txt.find('pordtu-s')\nprint('found at',i)\nimport re\nseg=txt[:i]\ntags=re.findall(r'\\[pdf page (\\d+)\\]',seg)\nprint('last pdf page tag',tags[-3:] if tags else None)\nEOF",
 "description": "WLD Bd2 per-tu context and page"
}
```


### [2026-09-14T00:57:10.563Z] TOOL RESULT

```
„Pahre** (= aisl, far die Intonation ist die einer Set-Form) ; vermutlich 
hierher (Miklosich EWb. 258, Phlenbeck IF. 17, 94) auch abg. porjn, prati 
,.ze^schneiden'^ 



40 


per- 


jjDurchgang, Furt^^r av. pordtu-s m. f. (urar. "^prtii-s) imd pam-s 
m. (urar. ^priu-$) „Durchgang, Furt, Brucke“ (liu-para'&iva’' „gut zu iiber- 
schreiten“; gall, ritii- „Furt“ in Ritumagus, Angtistoritum, ir. j'ith in Huniar- 
rith (K. Meyer Rc. 16, 89f.), acymr. rit, ncymr. rhyd^ corn, rit „Furt“; ahd. 
furty ags. ford „Furt'‘ (hochstufig aisl. /jorftr „enger Meerbusen“ aus 

; lat. -27s;„Haustur (XII Tfln.); Hafen^*, angiporins „enge Passage, 

NebengaBchen^'; daneben a-St. porta „Stadttor, Tor‘^ 

Ygl. im allgem. Curtins 272, Pick P 81, 475, IP 38, IIP 229f., Yf. 
LEWb.^ 602, Persson Beitr. 641. 

Fern bleibt got. /’em „Seite, Gegend'', alid. fiara „Teil, Seite“ aus ei), 
=== page tag ===
found at 155971
last pdf page tag None
```


## [2026-09-14T00:57:14.756Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"parna-\\|porno-\\|por-no\\|Federkraut\\|Farnkraut\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20",
 "description": "grep WLD for feather root"
}
```


### [2026-09-14T00:57:14.807Z] TOOL RESULT

```
12938:mnd. brake m. f. „Zweig“, engl. brake ^Gestriipp, Dorngebiisch; Farnkraut“,
```


## [2026-09-14T00:57:17.634Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Flugel\\\"\\|pero \\|pero,\\|pe6ro\\|Feder\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | sed -n '1,25p'",
 "description": "grep WLD Bd2 Feder"
}
```


### [2026-09-14T00:57:17.692Z] TOOL RESULT

```
772:Weder Beziehung zu '^p{e)isqo- „junge Feder(?j'^ (Zubaty aaO.), noch 
776:p(e)isqo- „(junge) Feder^^? 
778:Ai. piccha-rn ,.Schwanzfeder'^* cech. ..unentwickelte junge Feder^^? 
1366:Ai. 2 )dtra-m „PIugek Feder^, patard-, paidru- „fliegend. fiiichtig^, av. 
1382:jz£TQidicov ovsigcov „geflugelte Traume^ (Alkman), tztsqov „Feder, FlugeP^ 
1386:und Yf. LEWb.^ s. v.); penna „Feder, Flugel“ {^petna; wenn pcsna bei 
1396:adan „Flugel, Feder“, adnog „pennatus“, abret. attanoc „volitans^^, 
1400:{pp aus tn~)^ nhd. Fit tig. Uber abg.^>ero, russ, „Feder“ (— Tnegov)^ 
1415:ein ^pcr{9)- dieser Bed. auch in eii. parnd-m „Fluge], Schwungfeder, Feder, 
1416:Blatt*’^ av. parona- „Feder, Flugel“, ahd. /ar(n)w, farm. ags. (earn „Pam“ 
1424:pent, ptrati nicht als Denominativa von pero gedeutet zu werden brauchen. 
1434:^geradaus treffend = stoBend, aufschlagend^*), Talkov „ Feder, Flaum- 
2399:♦pro unter einer besonderen Basis "^pero „Yorn“ mit lit. pirmas, ai. punas 
2598:mit Bed.-Spezialisiemng nach pero ,,Feder‘, das trotz Miklosich EWb. 241, 
5534:lautsvereinfachung, vgl. :;rT6pdv: ohg. pero u. dgl.; unklar sind die auch in 
6261:pleus „ausrupfen; gerupfte Wollflocken, Federn oder Haare, Flies, Zotten“. 
6278:sein sollten (s. u. pleiiq-), lit. piduzdints ,,(Feder)bett, Deckbett", apr. (mit 
6279:^-Einschub) plauxdme „Federbett". 
6282:Vf. LEWb.^ s. V. gegen die Gleichsetzung mit lit. plitnlcsna „Feder" bei 
6307:Gr. oTiakvooETai * onagdooetai, raQdoosrai Hes , lett. sptdwa „Feder, Ge- 
6328:„Feder“ (s. o.); ahd. flocclio „lanugo“. nhd. Floche, mnd. vlocke „AVoll-, 
8444:„Iger', schwed. mdartl. borra ut sig „die Federn strauben, von Y5geln“ 
11817:kissen, Polster, Federbett"; russ. bclozenh m. ,,Schmele, Beule, Leichdorn, 
35175:Lett, sk'ien-e^ -s „der Brustknochen beim Federvieh" (wie sk'ieta^ sldiete ds.) 
35185:zur Bed. „Spule" vgl. ahd. sqmolo^ spiiola „Weberspule, Rohre, Federkiel"
```


## [2026-09-14T00:57:25.993Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1398,1425p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt",
 "description": "WLD Bd2 parena context"
}
```


### [2026-09-14T00:57:26.042Z] TOOL RESULT

```
pitza KZ. 36, 202, 233, Pedersen KG. I 40, 90, 160). Ahd. fedara^ anfrk. 
fethera^ ags. feder^ aisl. fjqdr f. „Peder“ (^petra)) ahd. fethdhaliha „alae“ 
{pp aus tn~)^ nhd. Fit tig. Uber abg.^>ero, russ, „Feder“ (— Tnegov)^ 
perff,, phYoti „fliegen“, par-jq, ~iti ds. s. u. 

Ygl. im allg. Curtius 210, 709, Pick P 78f., 250, 473 (mit nicht aufrecht 
zu haltender Scheidung von pet- ^fallen^^ und pet- ^fliegen^, s. dagegen 
Yf. LEAYb.2 u. penna), II* 27 f., Ill* 226f., Persson Beitr. 654 f., 676, 688, 
825. 887 f. 

Die Gleichung = slay. 2)er6 (J. Schmidt PL 174 f., Kretschmer 

KZ. 31, 427) wird man trotz Meillet Et. 238 nicht aufgeben diirfen, doch 
ist si. p- aus idg. pt- oder bereits ursprachliche teilweise Erleichterung 
dieser Anlautgruppe bedenklich und eher nregov durch EinfluB von Tuigvi 
an Stelle eines altern '’^negov getreten (Petersson KZ. 47, 272; tit- aus p- 
legt, mit nicht einleuchtender Erklarung, Schrijnen KZ. 44, 19 zugrunde); 
ein ^pcr{9)- dieser Bed. auch in eii. parnd-m „Fluge], Schwungfeder, Feder, 
Blatt*’^ av. parona- „Feder, Flugel“, ahd. /ar(n)w, farm. ags. (earn „Pam“ 
(wie TiTEgig zu nxegov). lit. sparnas „Plugel, FloBfeder^, woneben mit t- 
Pormantien gall, rafis^ ir. raith, cymr. rliedyn, acorn, rcden^ bret. raden 
,,Farn“ (f'prd-ti-s)^ und m. RedupL lit. papdrtis, russ. pdporoh^ serb. pdprat 
(usw.), slov. prdprat „Farn“, auch wohl ai. pdrpatadi „eine bestimmte 
Arzneipflanze^" (z. B. Pick IP 226, Kretschmer aaO.. Uhlenbeck Ai. \Yb. 
15S, Meillet aaO., Pedersen KG. 191, Petersson aaO., s. auch Yf. LEWb.^ 
u. perna). Diese Auffassung von slav. perd bietet auch den Yorteil, da6 
pent, ptrati nicht als Denominativa von pero gedeutet zu werden brauchen. 
Ob diese Gruppe als „vibrierend, zuckend“ nach Persson Beitr. 644 zu
```


## [2026-09-14T00:57:37.599Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=1320 && NR<=1400' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | grep -nE \"^\\s*[0-9]{1,3}\\s*$\" | head; echo \"---\"; awk 'NR>=1200 && NR<=1420' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | grep -nE \"^[0-9]{1,3} $|^ ?[0-9]{1,3}$\" | head",
 "description": "find WLD page numbers near line 1415"
}
```


### [2026-09-14T00:57:38.586Z] TOOL RESULT

```
59:21 
---
49:19 
179:21
```


## [2026-09-14T00:57:42.985Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN bridge ===\"; grep -n \"10.75\\|BRIDGE\" SYN.txt | head -8; echo \"=== SYN feather ===\"; grep -n \"FEATHER\" SYN.txt | head -8",
 "description": "grep Buck for bridge/feather"
}
```


### [2026-09-14T00:57:43.060Z] TOOL RESULT

```
=== SYN bridge ===
5787:4. Ir. carpat, Nir. carbad ‘chariot, wagon’ (10.75) used also for the ‘upper jaw, palate’ (cf. NIr. fiacla carbaid ‘teeth of the upper jaw’), apparently from the resemblance in shape. Here also Br. karvan ‘beam of a loom’ and reg. word for ‘jaw’ (upper or lower), and W. car yr én ‘jawbone’. Pedersen 1.118, 494.
16624:M wb.) 10.54 OverTAKE oll pen Gb.) 10.55 Arrive, REACH 10.12 ae AROUND 10.56 APPRoAcH (vb.) 40.18 Wino, WRAP (vb.) 10.57 ENTER 10.14 Ron (7b.) 10.61 Carry (BEaR) 10,15 rairb.) 10.62 Brine re Russe, LIFT 10.63 SEND 10. vb.) 10.64 Leap (vb.) Ce se Tigui 10.65 D 1024 Dror (sb., of Liquid) : RIVE (vb. trans.) 1025 THROW (vb.) 10.66 Rive (vb.) 1098 SHAKE (vb. trans.) 10.67 Pusu, Sov (vb.) 1031 Bor (vb. intr.) 10.71 Roan 10.33 Smvx (vb.) 10.73 Street 10.34 Fuoat (vb.) 10.74 Brmwce 10.35 Sw (vb.) 10.75 Carrtace, Wacon, Cart 1036 Satz (vb.) 10.76 WHEEL 1037 Fuy (vb.) 10.77 AXLE 10.38 Brow (vb. intr.) 10.78 Yoxs 1041 Creer, CRAWL 10.81 Sup 1042 Ste, Sur (vb.) 10.82 Sartor 1043 Jump, Leap (vb.) 1044 Dancz (vb.) ee meee 1045 Watx (vb.) i 10.46 Run (vb.) 10.85 Oar 1047 Go 10.852 Row (vb.) 1048 Come 10.86 RuppER 1049 Go Away, Depart 10.87 Masr a Tze 10.88 Sar (sb.) 10.53 peso 10.89 AncHoR
18227:10.74 BRIDGE
18257:10.75 CARRIAGE, WAGON, CART
34260:‘smith’ (9.60); ‘wagonmaker, cartwright, wheelwright’ (mostly fr. ‘carriage, wag- on, cart’, 10.75, but also in part general- ized from one who makes special parts, as ‘wheel’ 10.76 or ‘frame’; cf. NHG wagner, radmacher, stellmacher, Kretsch- mer, Wortgeogr. 485 f.); ‘mason’ (9.53); ‘potter’ (9.71); ‘miner’ (‘mine’, p. 608); ‘cook’ (5.21); ‘baker’ (mostly fr. ‘bake’, 5.24; or fr. ‘bread’, 5.51, as Grk. dpro-Koros, —roLds, -rwAns, NG Yopas, Sp. panadero, Russ. chlebnik, etc.; Fr. bou- langer, OF r. boulengier, dial. boulenc, fr. MLG bolle ‘round bread’; fr. ‘oven’ 5.25, as It. fornaio, Sp. hornero, NG govpvapns; Lat. pistor, orig. ‘one who pounds the grain, miller’); ‘butcher, (5.612); ‘miller’ (5.57), ‘weaver’ (6.33); ‘tailor’ (6.13), ‘shoemaker, cobbler’ (6.54); ‘sailor’ (10.82); ‘soldier’ (20.17), ‘author, writer’ (18.62); ‘poet’ (18.63).
=== SYN feather ===
6352:4.393 FEATHER
```


## [2026-09-14T00:57:46.442Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18227,18256p' SYN.txt; echo \"###### FEATHER ######\"; sed -n '6352,6380p' SYN.txt",
 "description": "Buck bridge and feather entries"
}
```


### [2026-09-14T00:57:46.515Z] TOOL RESULT

```
10.74 BRIDGE
Gtk. -yédipa Goth. Lith.  Utiltas
NG  yégupa ON bri Lett. tilts
Iat. pons Dan. bro ChSl. mostit
It. ponte Sw. bro, brygga SCr. most
Fr, pont OE brycg Boh. most
Re puente ME brigge Pol. most
oS oe NE bridge Russ. most
Nit ote a ; Du. brug Skt. — setu-
ee p OHG  brucka Av. pasu-, paratu-
Br p : MHG brucke, brugge Pon NHG _briicke
cates ‘bridge’ are connected with Rum. pod, fr. ChSl. podi% ‘ground,
flecting a ak board-flooring’, re- | floor’. Tiktin s.v.
Inay, road ee " with words for 3. Ir. drochet, NIr. droichead, prob. as
? *) +
Purpose of the fg and’, reflecting the | a coll. *druk-anto- ‘beams’ : OE itrog Gtk, yési 0 ae 1 ‘trough’, ChSl. drikoli ‘cudgel’, ko-for-
Boeot, gg USO 7d yedipr), | mations fr. IE *dreu- in Grk. dpos ‘tree,
Cret. dépipa, earlier
oak’, etc. Walde-P. 1.805. Pedersen 2.47.
W., Br. pont, fr. Lat. pons (-tis). Loth, Mots lat. 197.
4, ON bri, Dan., Sw. bro, Sw. brygga (Dan. brygge ‘wharf, pier’), OE brycg, OHG brucka, etc., general Gme. : Gall. briva ‘bridge’, ChSI. briiviino ‘beam’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
722 SELECTED INDO-EUROPEAN SYNONYMS
SCr. bruv ‘beam, footbridge’, etc., a group with primary meaning ‘beam’, whence ‘bridge’. Walde-P. 2.207. Falk- Torp 103, 109.
5. Lith. wltas, Lett. tilts : OPruss. talas ‘floor’ (of a room), ChSIl. tilo ‘ground’, ON Jil, OHG dil ‘board-wall’, Skt. tala- ‘surface, plane’, etc. Walde-P. 1.740.
6. ChSI. mositi, SCr. most, etc., gen- eral Slavic (cf. also Russ. mostovaja ‘pavement, deck’, pomost ‘floor, scaf- fold’) prob. as orig. ‘beam’ an early loan-
word fr. the Gme. group OHG mast ‘pole flagstaff’, esp. ‘mast’, OB mest, ON mastr ‘mast’. Stender-Petersen 282 f Walde-P. 2.235 f. (rather as cognate with Gme. group). Walde-H. 2.19.
7. Skt. setu-, lit. ‘a band’, as adj ‘binding’ = Av. haétu- ‘a dam’ : Tae saela ‘coarse hair’, OHG seid ‘string’ etc., t-formations to Skt. Si-, Ay. he Lett. set ‘bind’, etc. Walde-P. 2.464,
Av. pagu-, paratu-, also ‘f ord, passage’ ; OE ford, OHG furt ‘ford’, Lat. portus ‘harbor’, porta ‘gate’, etc. Walde-P, 2.40.
###### FEATHER ######
4.393 FEATHER
Grk. —_xrepby Goth. - Lith. plunksna NG ¢grepé ON = fjodr Lett.  spalva Lat. penna Dan. fjeder, fier ChSI. pero
It. penna, piuma Sw. Sidder SCr. pero
Fr. plume OE — feper Boh. péro
Sp. pluma ME sfether Pol. pibro Rum. pand NE feather Russ. pero
Ir. cleite, cliim Du. _feder, feer Skt. parna-, pattra- Nir. _ cleite, cliim OHG fedara Av. parana- W. pluen MHG veder(e)
Br. pluenn NHG feder
The majority of the words for ‘feather’ are cognate with words for ‘wing’ and have been included in the preceding dis- cussion, 4.392. Here only the following:
1. Lat. plima, denoting the fine, soft feathers covering the body, vs. the penna,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
of wing or tail, but eventually displacing
the latter in part (hence It. piuma, Fr.
plume, Sp. pluma) prob. (fr. *plus-mda) :
MLG vliis, OF fléos, etc. ‘fleece’, also(?)
Lith. plunksna ‘feather’ (see below).
Walde-P. 2.96. Ernout-M. 781. 2. Ir., NI. cleite, etym.?
HE BODY; BODIL
4b
7s OF
C ir. clam (coll. ‘feathers’), W., 3. Cae ge. -eN, enn), fr. Lat
Br plu (coll. ; 9) Vendryes, De hib
bove,; : Mots lat. 196. 7, Loth, 0 d also pluksna,
Digitized by Arya Samaj Foundation Chennai and eGangotri
Y FUNCTIONS AND CONDITIONS 247
plusna), either : plaukas ‘hair’, Lett. plakt ‘pluck’, or, with k fr. this group, fr. old plusna, this : Lat. plima (above, 1). Walde-P. 2.96. Thurneysen IF 14.127 f.
4.40 BREAST" (Front of Chest)
; h. brusts (pl.) Lith.  kritiné Grk.  arfidos (erépvov) ON brjast Lett. krats NG — oTios Dan. _bryst ChSl. priisi (pl.), grudt Lat.  peclus Sin brést SCr. _ prsa (pl.), grudiz (pl.) mre. one OE bréost Boh.  prsa (pl.), hrud’ . ane ME _breste Pol. pier a ea NE breast ete grud’ ‘i oe . Du. borst i uras-, vaksas- Nir LS ene OHG  brust Av. varah- "bron, dwyfron MHG _ brust j NHG _brust
brennid
Words for ‘breast’ as front part of the chest and for ‘breast’ as woman’s breast are in part the same, and where they are normally different there may be some overlapping. There is also overlapping on the other side with ‘chest’. In fact, except where the distinctive Grk. @&pat (the whole ‘trunk’ in Aristot., later ‘chest’) has been borrowed, ‘breast’ as the front of the chest, and the whole ‘chest’ are generally not distinguished but covered by the same word. (So Lat. peclus, It. petto, Fr. poitrine and most of
```


## [2026-09-14T00:57:53.160Z] TOOL CALL #60: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T00:57:53.167Z] TOOL RESULT

```


```


## [2026-09-14T00:57:56.217Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%84",
 "prompt": "Persian پل (pol) 'bridge' — give the full etymology section: Middle Persian form, Old/Proto-Iranian and Avestan antecedents, cognates."
}
```


## [2026-09-14T00:57:56.877Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Euphrates",
 "prompt": "Give the full etymology entry for Euphrates."
}
```


### [2026-09-14T00:58:00.677Z] TOOL RESULT

```
# Etymology of Persian پل (pol) "bridge"

Based on the Wiktionary entry, here's the etymology:

**Middle Persian:** The term derives from Middle Persian *puhl*, meaning "bridge."

**Proto-Indo-European origin:** The ultimate source is Proto-Indo-European *pértus*, meaning "crossing." The entry notes this root also produced "English _ford_, German _Furt_, and Latin _portus_."

**Proto-Iranian stage:** While the entry mentions "Proto-Iranian" in categorization, the specific reconstructed form isn't explicitly detailed in the main etymology section beyond the Middle Persian intermediary.

The document does not provide Avestan antecedents or a detailed Proto-Iranian reconstruction. The etymology emphasizes the crossing/passage semantic field shared across Indo-European languages, connecting Persian bridge terminology to transportation and boundary-crossing concepts found in related languages.
```


### [2026-09-14T00:58:02.484Z] TOOL RESULT

```
# Etymology of Euphrates

**Definition:** A Mesopotamian river flowing from Armenia to the Persian Gulf.

**Etymology Chain:**
- Old English: *Eufrate*
- Greek: *Euphrates*
- Old Persian: *Ufratu*
- Possibly Avestan: *huperethuua* meaning "good to cross over"

**Possible Components:** The Old Persian form may derive from *hu-* ("good") plus *peretu-* ("ford"), connected to the Proto-Indo-European root *per- meaning "to lead, pass over."

**Scholarly Debate:** Researcher Kent suggests "probably a popular etymologizing in O.P. of a local non-Iranian name," indicating uncertainty about whether the proposed derivation accurately reflects the name's true origin.

**Related Form:** Akkadian *purattu*; English adjective *Euphratean*

The entry acknowledges that while a plausible linguistic breakdown exists, the name may ultimately derive from a non-Iranian source whose original meaning remains unclear.
```


## [2026-09-14T00:58:15.815Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%AA",
 "prompt": "Give the etymology for Arabic فرات (al-Furāt) 'Euphrates' and for the Persian entry if present. What is it borrowed from?"
}
```


## [2026-09-14T00:58:16.978Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1",
 "prompt": "Persian پر (par) 'feather, wing' — give the etymology: Middle Persian, Old Iranian/Avestan, PIE root, cognates."
}
```


### [2026-09-14T00:58:21.068Z] TOOL RESULT

```
# Etymology of فرات (al-Furāt)

Based on the Wiktionary entry, here's what we learn about the word's origins:

**Arabic Origin:**
The page indicates that the Arabic فرات (al-furāt) ultimately derives from Akkadian. Specifically, it traces back to "𒀀𒇉𒌓𒄒𒉣 (ÍDPurattu)" in Akkadian.

**Persian Entry:**
The Persian entry shows that فرات was "Borrowed from Arabic الْفُرَات (al-furāt)." This means Persian adopted the word from Arabic rather than developing it independently.

**Summary:**
Both the Arabic and Persian versions of this word refer to the Euphrates River. The etymological chain flows from Akkadian → Arabic → Persian (and subsequently into Ottoman Turkish, Urdu, and other languages). The word ultimately traces its linguistic ancestry to ancient Akkadian, one of the oldest documented languages.
```


### [2026-09-14T00:58:22.300Z] TOOL RESULT

```
# Etymology of Persian پر (par) - "feather, wing"

## Origin Chain

**Middle Persian:** The word derives from Middle Persian /purr/, representing a continuation of ancient Persian vocabulary.

**Proto-Iranian:** It traces back to Proto-Iranian *pr̥Hnáh, which shows cognates across related languages like Northern Kurdish *pirr* ("much, very, many").

**Proto-Indo-Iranian:** The ultimate source is Proto-Indo-Iranian *pr̥Hnás, evidenced by Old Avestan *pərəna* and Sanskrit *parṇá* (feather).

**Proto-Indo-European:** The deepest layer is PIE *pl̥h₁nós*, meaning "full" or relating to feathers/wings.

## Cognates

The entry notes related words across Indo-European languages: Russian *pólnyj* (full), Lithuanian *pilnas*, Italian *pieno*, Welsh *llawn*, and English "full"—demonstrating how this ancient root spread across linguistic families over millennia.
```


## [2026-09-14T00:58:28.591Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/parnam",
 "prompt": "Proto-Iranian *parnam 'feather, wing' — give the reconstruction, PIE source, and descendants (Avestan, Middle Persian, Persian)."
}
```


## [2026-09-14T00:58:29.829Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9rtus",
 "prompt": "PIE *pértus 'crossing, ford' — root, meaning, descendants (Avestan, Latin, Germanic, Celtic)."
}
```


### [2026-09-14T00:58:29.958Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T00:58:34.946Z] TOOL RESULT

```
# Proto-Indo-European *pértus

Based on the Wiktionary entry, here's what we know about this reconstructed word:

## Definition and Etymology
The term *pértus* means "crossing" and derives from the root *per- ("to fare") combined with the suffix *-tus.

## Linguistic Classification
This is a masculine noun with an athematic, proterokinetic declension pattern, featuring an oblique stem of *pr̥téw-.

## Descendant Languages
The word evolved across several language families:

- **Celtic**: Proto-Celtic *ɸritus
- **Germanic**: North Germanic *ferþuz and West Germanic *furduz
- **Indo-Iranian**: *pr̥túš (appearing in Classical Sanskrit as पट्टन paṭṭana)
- **Italic**: Proto-Italic *portus

## Significance
This reconstruction demonstrates how comparative linguistic methods reveal ancestral vocabulary. The modern English word "ford" (a shallow river crossing) descends from this ancient root, illustrating the word's semantic consistency across millennia and language families.
```


## [2026-09-14T00:58:38.601Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/parna",
 "prompt": "Proto-Iranian *parna- 'feather, wing' — reconstruction, PIE source, descendants (Avestan parəna-, Middle Persian, New Persian par)."
}
```


### [2026-09-14T00:58:39.826Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T00:58:39.913Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/parna",
 "prompt": "Avestan parəna-/parna 'feather, wing' and Proto-Indo-Iranian *parnám — what PIE root is it assigned to, and what are the Iranian descendants including Persian پر?"
}
```


### [2026-09-14T00:58:43.933Z] TOOL RESULT

```
# Response

I cannot provide the requested information based on the provided Wiktionary page content. The page focuses on "parna" as it appears across multiple modern languages (Czech, Martuthunira, Polish, Spanish, and Tocharian B), but it contains **no etymological discussion of Avestan, Proto-Indo-Iranian roots, or Persian descendants**.

To answer your question about PIE root assignments and Iranian linguistic connections, you would need to consult specialized historical linguistics or comparative Indo-European language resources, which are not present in this dictionary entry.
```


## [2026-09-14T00:58:46.709Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/parn%C3%A1m",
 "prompt": "Proto-Indo-Iranian *parnám 'feather, wing' — PIE root it derives from, and descendants including Avestan and Persian."
}
```


## [2026-09-14T00:58:48.616Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1#Persian",
 "prompt": "List EVERY Persian etymology section on this page separately. I specifically want the one for par 'feather, wing' (not por 'full'). Quote its etymology text verbatim."
}
```


### [2026-09-14T00:58:52.443Z] TOOL RESULT

```
# Persian Etymology Sections

There are **3 Persian etymology sections** on this page:

## Etymology 1 (por - "full")
From Middle Persian, Proto-Iranian, and Proto-Indo-European roots meaning "full."

## Etymology 2 (par - "feather, wing")
"From Proto-Iranian [Term?], from Proto-Indo-Iranian *parnám, from Proto-Indo-European *pornóm ("feather, wing"), from *perH- ("to fly")."

## Etymology 3 (par - verb form)
This section contains no etymology text; it only indicates par is "present stem form of پریدن."
```


### [2026-09-14T00:58:52.453Z] TOOL RESULT

```
# Proto-Indo-Iranian *parnám

This Wiktionary entry documents a reconstructed Proto-Indo-Iranian word meaning "leaf," "feather," or "wing."

## Key Information

**Etymology**: The term derives from Proto-Indo-European *pornóm, which comes from the root *p(t)erH- meaning "fern."

**Linguistic Classification**: It functions as a neuter a-stem noun with a complete declension paradigm across singular, dual, and plural forms.

## Descendants

The word evolved into numerous descendant languages across Indo-Aryan and Iranian branches:

- **Sanskrit**: parṇá
- **Iranian languages** include Avestan, Persian (پر - par), Kurdish (پەڕ - perr), Pashto, and others
- **Nuristani languages**: Kamviri, Prasuni, and Ashkun variants

This etymological reconstruction demonstrates how a single Proto-Indo-Iranian term dispersed across geographically and linguistically distinct modern language families, with reflexes appearing from Sanskrit to Persian to Kurdish dialects.
```


## [2026-09-14T00:59:06.558Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF%D8%A8%D8%A7%D8%B1",
 "prompt": "Persian رودبار — etymology: what is the element -بار (-bār) derived from? Quote it."
}
```


## [2026-09-14T00:59:07.774Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/passport",
 "prompt": "Etymology of passport; also mention what it says about French passeport and Latin portus/porta."
}
```


### [2026-09-14T00:59:09.677Z] TOOL RESULT

```
Based on the Wiktionary entry, the element **-بار (-bār)** is derived from Middle Persian. The etymology section states:

"Inherited from Middle Persian _lwtbʾl_ (rōd-bār, 'river bank')."

The **-bār** component means "bank" (as in riverbank), and the full word combines "rōd" (river) with "bār" (bank) to create "rōdbār" (river bank).
```


### [2026-09-14T00:59:12.360Z] TOOL RESULT

```
# Etymology of Passport

The word "passport" dates to around 1500, derived from Old French *passeport*, combining *passe* (imperative of *passer*, "to pass") and *port* (port).

**Original meaning:** The term initially meant "authorization to travel through a country" or "authorization to pass through a port" to enter or leave. This sense is now obsolete.

**Modern meaning:** By the 1540s, it came to mean "document issued by competent civil authority granting permission to travel in or out of a country."

**French connection:** The Old French *passeport* reflected "authorization to pass through a port."

**Latin roots:** The *port* component traces to Latin *portus* (harbor), which originally meant "an entrance, a passage." It's related to *porta* (city gate, door), ultimately deriving from the PIE root meaning "a going, a passage."
```


## [2026-09-14T00:59:18.209Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB puhl ===\"; grep -n \"puhl\\|pwhl\" NYB_vol2_glossary.txt | head -10; echo \"=== NYB parr/par ===\"; grep -n \"^parr\\|parr \" NYB_vol2_glossary.txt | head -5; echo \"=== CHEUNG par ===\"; grep -n \"^\\*par\\|par- \\?'to cross\\|\\\"to cross\" CHEUNG.txt | head -10",
 "description": "grep Nyberg and Cheung"
}
```


### [2026-09-14T00:59:18.297Z] TOOL RESULT

```
=== NYB puhl ===
503:apäk-puhr [LWTH pwhl] he who has a son 22%. - Cf the NP compounds with bà: bā-āb ‘having water’ and the like.
584:apé-pit [’py-’B'] fatherless 22$. ape-puhr [’pypwhl] without son 226-7.
933:bastan [bstn', inser. bstny ; '"SLWN-tn'] band-, to bind (hand and foot) 32!?; to fetter 74??. 115! (be ~); to fasten 2026; asp apar rahy ~ to harness a horse to the car 5416; andar ~ (apar rahy) id. 5418-14 (gl); dar bé ~ to shut the door 7514; puhlv, vitiry ~ to construct a bridge F:1-3.6; menišn i...6...~ to fix a p.’s mind upon = to suggest to his mind to (do ...) 4021-22; ddisr i... pat ménisn be ~ to obstruct the spiritual eye (sight) of a p. 5226-27 (ef. bastišn) — Av. (926) band- = OP; MPrth bstn bnd-; MPrs bstn, subju. byn’d = bennād,
2386:2. with -s- for -hr-: Misē; msyd msy’ny DkM 59314-15; with -rs- for -hr- : mrsy’ny (Tanbih, l.c., var. of Cod. L). — C. In Khwarizm mrd — mrd?nh (Birüni, l.e.); MPrs mwrdy’ng (A-H I, p. 220). Cf Chri- stensen, Le premier homme I, p. 9-10. The forms reconstructed and used by him: * Masyay — *Masyānay, are nowhere to be found, and fictitious. The forms Khwar. Mard ("Man") and MPrs fem. Murdiyänag are clearly WIr, and so are also Mihreh < NW *Midriya- and Misēh < SW "miciya-. The other forms are typical EIr, and betray the difficulty WlIranians felt in rendering the sound developed in EIr from -rt-, -r0-, -0r-, which must have been something like an unvoiced -r- or -l-, and which they analyzed as -hr-, -hl-, -rh-, -lh- or simply identified with their -§-. Cf the spellings of pahlom (g. v.); Av. agavan-, BP ahlav < artavan-; Av. ašsmaoya-, BP ^hlmwk: ahlamög, but KZK 1. 13 'iswmwky (in the parallel text SM 1. 20 ’himwky); hence the inverse spelling pwlsy for puhl ‘bridge’ (q. v.), SM 1. 43 (Arab mrsy’ny, v. above, is a mechanical rendering of a written BP form *mlsy’ny = mihriyäne). Consequent- ly, mahlé malhé māšē are Elr develop- ments of *martiya-; miše EIr develop- ment of *mißriya-, ci Sogd mys < midra. We have to do with two forms of different origin: 1. *martiya-, 2. *mi@riya-; as to this problem, cf Sven Hartman, Gayo- mart (1953), 45-64.
2514:crowd of Iranians who used to come there, to the court of A. the Khionite 616-7; puhl ... ke har ahlav u druvand avis ~ the (Chinvat) bridge to which everyone, pious or wicked, inevitably comes 7213; *kas-ip (g. v. amäh meneč ... ku “har- visten matür hom pat zanišn", nē amäh &t6n-ic harvisten matàr he 6 zamišn how- ever much you may think about us: ‘‘[I am an unavoidably-total-comer-to-slay =] I shall unavoidably come and slay (you) totally", yet you will never attain to slay us totally 469-5, with the gl. kū-t etón nē apasihēnītan i apāc nē bavēm ‘that is: it is not for thee to destroy (us) so utterly that we shall not come back” (the first amäh is the proleptie obj. of the first zanišn, and the second amāh of the second zanišn; however, as the author passes to direct speech after menč the dir. obj. of the first zanısn ought to be $mäh, so the first amäh lacks all connection; harvistén (g. v.), virtually a qualifier of zantšn, has been combined with matdr as its attribute).
2694:Nēv-Šāhpuhr  [ndwšhpwhl] 11419, — “Brave Shapur”.
3169:puhl [pwhl, inser. pwhly] bridge F:l. 6412, 7212.25.26 7423, 8917. 1147. — Av. (892) porotu-, (897) pasu- (cf arota-, -orota-: aša < rta-); MPrth pwrt (MHC); Paz. puh(a)l; NP pul. — Of s.v. Mahlāt:
3170:1puhr [pwhl; Prth BRY] son HajA: 3. SPrth:6; v. also apäk-puhr, apé-puhr, puhrépuhr. — The NW form of Av. (909 sqq.) pudra-; cf pus.
3171:?puhr [pwhl] punishment, penance 665. 7419, — Av. (892) parafa- ‘penalty’.
3584:Sühpuhr [Shpwhl; Prs. inser. šhpwhry, šhpwhly], Prth Sahépuhr [Shypwhr] n. pr. 1. Šahpuhr I (241-272) son of Artax- šahr: Haj, Š; 1026-17, passim; 1097-22, 1148-11622, passim. — 2. Sähpuhr II (309— 379), son of Hormizd II: P 1, P2; 10914, — 3. the name of the Sakān šah Pl. — Cf also s. v. Valaxs and xtarrah.
=== NYB parr/par ===
2964:parr [pl] feather, wing 3%. 9%, — Av. (869 sq., 894 sq.) parana-, parana-; MPrs in pr-wr ‘winged’ (A-H I), ‘spyd-pr ‘white-winged’ (A-H IT); NP par(r). parrišn [plšn'] the fiying, the twanging: ~ i kamänän 2523-26,
2965:parritan [plytn'], parristan [plstn'] to fly in the air 925, — NP parridan.
3675:šutan [ZLWN-tn'] šav- [ZLWN-), forms v. I, 177, to go, opp. (G)matan to come: hac ki mat hom u apāc 6 ku šavom? whence have I come and whither shall I go? 6245; pat druyist šutan u āmatan that they may go and come safely 8723; ka han damistan Sut when this winter has gone 972; hac man šavdi thou shalt go (fly) off from me 2715; — regularly be ~ to go away, passim; bē o ... ~ to go (away) to; bé ~ to disappear, vanish 9416, to escape 2415-16 ; bē-šutak baxt whose luck is gone, who is off his luck 5?; — andar ~ : tigr tai parr pat aškamb andar šut the arrow penetrated right up to the feather into its belly 3%; to enter 181%, also andar-rón 1813, andarón 1912-13; 7525. 10278; — apāc ~ to go back, to
4521:gor zat he shot an arrow at the onager 319-20; parr 6 pist zat its wing struck (the bowl with) the meal 925-26; 57 (= 6) fravahr + Zartuxst aš zafar frac zat threw open its mouth towards Z. 4012-13; 5; (= 6) gurg zat zanak the wolf's jaw was struck 506, with the gl. kū-š dahān ēvak apäk dit frot oškan (g. v.); Vidrafš pat dil zat stabbed V. in the heart 292; 25?! (cf s. v. rad 2 b)]; 383; — ēvak 6 dit ~ to knock to- gether 12019-20; ka šamšēr frac zanēt when the sword makes a stroke forward 254 (opp. apāc vēžēt, v. *véxtan); to drive (a peg) down into the soil 202%; tanbür ~ to play on the lute 476, — Av. (490) !gan-, pres. jan-; MPrth jdn jn-; MPrs zdn zn-; Paz. NP zadan zan-. V. also janišn, zanišn, zatak, zatar; cf apa-žand, ozatan.
5274:pāra-: pārak Para-data-: Pēš-dāt parena-, perona-: parr paresu- (peresu-): pahlūk paršta-, paršti-: pušt pasca: pas
=== CHEUNG par ===
1706:*para-) ‘to carry off, forth’ || (+ *pari-) ‘to take around ? || (+ *fra-) ‘proferre, to 
1793:*para-) puror- ‘to take away’ || (+ *fra-) haur- ‘to give’, haura- ‘word’ || (+ *ni- or ? 
1853:*para-) Yzgh. porvar-/*porvag ‘to drag across’, Khf. parfur ‘transfer of hay or 
2908:*pari-) MMP przyd (past stem) “о shut in, imprison; fix in, fasten in’ || (+ *ni-) 
4825:*pari- or *para-, *fra-) ? SSogd. prör- ‘to endeavour’ || (+ *ui-) BSogd. wyó yr, 
10636:*para-) ‘to throw around’ = Liste: 11 
11837:*pari-) Yghn. piráyZ-, paréZ- ‘to run away’ 
12340:*pari-) NP parmäsidan ‘to touch, feel’ || (+ *ui-) Kurd. (Kurm.) guvastin/guves-, 
12368:*pari-) ‘to brush, wipe around’ || (+ *fra-) ‘to wipe forth, away’ || (+ *ni-) ‘to sweep 
15442:*para-ä-) pr’gn- ‘to scatter, sow’ || (+ *pari-) prgn- ‘to scatter’ || (+ *ui-) wygn- ‘to
```


## [2026-09-14T00:59:27.207Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"to fly'\\|to cross'\\|to go over, to cross\\|pass over\" CHEUNG.txt | head -20",
 "description": "grep Cheung for par roots"
}
```


### [2026-09-14T00:59:27.252Z] TOOL RESULT

```
3348:*AVESTAN: car- ‘to come and go’ || (+ *para-) ‘to pass over’ || (+ *ui-) ‘to go to and 
24825:over, pass over’ = Ghilain: 57, 74, 92 | DMMPP: 352a, 339a 
24834:BSogd. ft’yr- ‘to come, proceed’, CSogd. ftyr- ‘to pass over, pass away, depart’, 
24835:CSogd. ftyr- ‘to cause to pass over (away), take over, remove, set aside’ || (+ *ui-)
```


## [2026-09-14T00:59:29.886Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\*par\\b\\|^\\*par 1\\|^\\*par 2\\|^\\*par 3\\|parr-\\|parridan\\|parīdan\\|paridan\" CHEUNG.txt | head -20",
 "description": "Cheung par entries"
}
```


### [2026-09-14T00:59:29.947Z] TOOL RESULT

```
19310:*par! ‘to get even, equalize, commit oneself (to a legal obligation, contract)’ 
19351:*par? ‘to go over, cross over’ 
19423:*parë ? ‘to fill’ 
19598:*NWIR: NP parridan/parr-, Abyan. parroya/parr-, Abz. parowa/par- ‘to fly’, Qohr. 
19599:parada/par- ‘to fly away’, Tr. para/par- ‘to fly, jump’, Varz. parra/parr- ‘to fly; to 
19623:*parš ‘to sprinkle, strew’ 
37178:*par- (pud-), 293 
41254:parridan/parr-, 297 
43470:parroya/parr-, 297 
45092:parrä/parr-, 297 
56130:*par! 
56175:*par’, *tarH! 
56477:*par 
56729:*par 
56747:*par
```


## [2026-09-14T00:59:32.580Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19351,19380p' CHEUNG.txt; echo \"###### par4 fly ######\"; sed -n '19585,19615p' CHEUNG.txt",
 "description": "Cheung *par2 and *par fly entries"
}
```


### [2026-09-14T00:59:32.636Z] TOOL RESULT

```
*par? ‘to go over, cross over’ 

*AVESTAN: par- (fr-) ‘to go over, cross over’ || (+ *ni-) caus. ‘to bring, lead down to’ 
|| (+ *fra-) ‘to go forward’ = Liste: 33 

Aor. them.: SUBJ. 1sg. OAv. frafrä (Y 46.10), 2sg. YAv. frafra (V 7.52); Caus.: pres. IND. 3pl. ҮАУ. 
niparaiieinti (Yt 6.1, Yt 17.54), SUBJ. 1sg. YAv. frapäraiieni (Y 19.6, rep.), med. 2sg. YAv. fraparaiianhe 
(Y 71.16), OPT. med. 3pl. YAv. nipäraiianta (V 19.26) 

*MIDDLE PERSIAN: MMP xwrpr’n ‘west’ || (+ *aua-) BMP hwl-C)wpln /xwar-ofran/ 
‘sunset, the West’ || (+ *ham-) BMP hnb’rsn /hamparisn/ ‘confluence’? > DMMPP: 
369 


294 *par3 


*PARTHIAN: (+ *ni-) nwrd (pret. stem) ‘to set (of the sun)’, hwr-nyfr’n ‘sunset, West’ 
= Ghilain: 49 | DMMPP: 248a 

Partic.: perf. pass. nwrd 

*KHOTANESE: (+ *pari-) parbira- ‘round, circumference’ 

*NWIR: (+ “*fra- ?) ? Kurd. (Kurm.) lavaryam/lavarye-, (Sor.) lawaran, 
lawarin/lawar(é)- ‘to graze’ 

*MISC: Arm. (LW) par(a)berem ‘to encircle’ 

*SANSKRIT: par ‘to bring across, over’ (RV+) = EWAia II: 85 
###### par4 fly ######
*AVESTAN: parana- ‘wing’ (Yt 10.39, Yt 10.101, etc.) 

*MIDDLE PERSIAN: MMP pr, BMP pl /parr/ ‘feather, wing’ 

*PARTHIAN: png ‘foliage, leaves’ > DMMPP: 276a 

*KHOTANESE: pärra- ‘feather, wing; leaf, petal’ 

*SOGDIAN: BSogd. prn’’y’n (partic.) ‘flying’ (SCE: p. 35 f.), BSogd. prn’k ‘leaf, 
petal’, BSogd. prn ‘feather’ 

*CHORESMIAN: pn (m.) ‘feather’ 

*NWIR: NP parridan/parr-, Abyan. parroya/parr-, Abz. parowa/par- ‘to fly’, Qohr. 
parada/par- ‘to fly away’, Tr. para/par- ‘to fly, jump’, Varz. parra/parr- ‘to fly; to 
jump; to flee’, Bal. pan(n) ‘leaf? 

*NEIR: Pash. pana (Ё), Sh. pun, Bart. pont, Yi. pünä, M. pungy ‘feather’, Yi. pónék 
‘leaf’ 

*SANSKRIT: parnä- (n.) ‘wing’ = EWAia П: 97 

9 The denominatives above derive from the noun *parna-, which has impeccable IE 
credentials. 

«PIE *por-no- ‘wing, feather’ => LIV: – | Pok.: 850 (Nachtrag) 

*IE COGNATES: OCS pero, Lith. spafnas, Latv. spārns (m.) ‘wing’ (with sec. s-), 


OHG farn, OE fearn (m.), Engl. fern, etc.
```


## [2026-09-14T00:59:43.897Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19575,19586p' CHEUNG.txt; echo \"=== ARY index ===\"; grep -n \"PERETU\\|PARENA\\|PERTUS\\|PUHL\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Cheung par4 header + ARY index"
}
```


### [2026-09-14T00:59:43.956Z] TOOL RESULT

```
*IE COGNATES: Gr. лореїу (aor.) ‘to provide, to give, grant’, (med. perf.) лёлротол 
‘is determined (by fate)’, Lat. paro ‘I provide, appoint; I produce’, Olrish ernaim ‘I 
grant’ 

*REFERENCES: EVP: 59; Morgenstierne 1942: 264; DKS: 242b f. 


*parn ‘to fly off, take wing’ 

*AVESTAN: parana- ‘wing’ (Yt 10.39, Yt 10.101, etc.) 

=== ARY index ===
4745:FAHREN GERMAN) glsST PAR-, -PARAYEITI, PARENA-
4947:PoD (RUMANIAN) gles, PERETU, PECHU, PERETUSH
4948:PONTE —._ (PORTUGUESE) , us PUHL, PUHR APAHLAVD) 5 ey
```


## [2026-09-14T00:59:44.742Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"portus\\|pertu\" IEC.txt | head -10",
 "description": "grep Mann IEC"
}
```


### [2026-09-14T00:59:44.803Z] TOOL RESULT

```
1387:bhliguo ‘bruise, hurt, afflict’. WP IT, 217 Aeol. Ion. phlibo; Lat. fíigo, Ere (variant, since "eu > Lat. -v-); W cf. blin ‘tired, tiresome’; E cf. blight; ON cf. blikra *perturb'; Cz. u- blíziti “hurt, wound’
11064:mõið ‘try, test, trouble, importune’. WP II, 302 Gk. mõmai, mp. ‘try, importune, test, tempt; OHG muoen ‘tire, trouble, oppress’; MHG müejen, Du. moeien, v. id.; cf. MHG müeje, sf. ‘trouble beside müede (‘tired, sad’: Du. moe, id.) and Go. af-mauips (for *af-moips) id. R maat, inf. ‘weary, torment’; Blg. màja, v. ‘inhibit, perturb’; — se ‘hesitate’; cf. Bis maj (cnearly'. Sense of Fr. à peine)
13402:port- (1) (portos, a, us, is) “way, passage, gate'. Cf. per-, perio (1), poros and prt- (1) Lat. portus, gs: -üs, m. ‘harbour’; porta, f. ‘gate, entrance, mountain pass’; Osc. pürta-, f. id.; OS fard, f. i-st. journey, way’; vart, sf. id.; G Fahrt & Fährte; OE fierd, f. 'expedi- tion’; OCS cf. pri-prati, f., -pratü, m. & -prata, f. ‘doorway, porch?’ beside (z-gde) pri-prütü, m. id.; cf. also prasto, pratiti, v. “attend, accom- pany’; Srb. pratiti, id. beside pracati "gend": pratnja, f. ‘escort’; (LW in) Finn. porras, cpds. port- ‘stair, footbridge’
15286:be perturbed’; ON also: ‘forge metal; brood’); R cf. Sustryj, adj. ‘lively, smart; Li. siauciu, siausti, v. ‘storm, rage’. (Latv. šaušu, Saust, pf. Sautu, v. is an isophone: “flog')
19050:Latv. trauceju, et, v. ‘disturb, perturb, frighten’ beside traucu, traukt, v. “alarm; egg on; knock down; rush'. Cf. WP I, 736 and see Supt: trouk-
19599:a. Lat. cf. portus, domus, verü; Skt. dha- nuh, S$aruh, dàru; Av. gatus, dauru; Per. ta- razu; Olr. bir; Cz. dům, plástev, krokev, etc: OCS domi, Zrüny; Go. haírus, qaírnus, faíhu; OE wegu, feoh; Gk. pélekus, daitüs, dóru; Li. turgus; Latv. tirgus, etc. Compare types *pele- Kus, Kerus, urksus, etc.
```


## [2026-09-14T00:59:51.573Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4940,4955p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== page tag ===\"; awk 'NR<=4948 && /pdf page/ {p=$0} END{print p}' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== ARY main پل ===\"; grep -n \"PERETU\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "ARY pol entry"
}
```


### [2026-09-14T00:59:52.714Z] TOOL RESULT

```
90 Sins abcd FREUDE, FROSCH (GERMAN) git
AY topes Baas HOLD ENGLISH) pS g=3Si\
FROGGA, FROSC, FORSC
leetloal
AS E59 Sb Garg yg SME GS 9 Caer ee bool SLADL 42 51s gal Clap

PONTE AUTALIAN) gists HAVESTAN) glee 31
PoD (RUMANIAN) gles, PERETU, PECHU, PERETUSH
PONTE —._ (PORTUGUESE) , us PUHL, PUHR APAHLAVD) 5 ey
FOR, FORAN, GOTHIC) SF ARURDISH) «53,5 |
FARJAN PEL, PURD, PIRD, PIR

OLD SCANDINAVIAN) 345 eeu! PUL HAFGHAND) (4) gil
FIDORDHR, FIORD, FARA SANSKRIT) cxiSuile 4°"
FJORTHR — (OLD NORSE) 4S p55 P{PARTI, PARAYAI! ‘
FORD — (OLD SAXON) pS gip-S le HORD, HORDAN (ARMENIAN) gu!
=== page tag ===
[pdf page 172]
=== ARY main پل ===
```


## [2026-09-14T01:00:06.203Z] TOOL CALL #80: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D9%84' \\\n 'https://www.etymonline.com/word/Euphrates' \\\n 'https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D8%B1' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9rtus' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/parn%C3%A1m' \\\n 'https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF%D8%A8%D8%A7%D8%B1' \\\n 'https://www.etymonline.com/word/passport' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 395, root Per 2 (pol/forat/-bar/par/porta) verification' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:00:09.460Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b462a4a24d1c76af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6eaac385e459a207.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4bc475b6e31ac862.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1a7bf5274f408ee0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73354da5ae61a9b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d0e64a347c59d293.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4a1909790b53bd7c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd81aeb410af2b73.txt
```


## [2026-09-14T01:00:38.434Z] TOOL CALL #81: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T01:00:38.482Z] TOOL RESULT

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


## [2026-09-14T01:06:52.689Z] TOOL CALL #82: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-395.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_POL = \"https://en.wiktionary.org/wiki/%D9%BE%D9%84\"\nW_FORAT = \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%AA\"\nW_PAR = \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1\"\nW_PERTUS = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9rtus\"\nW_PARNAM = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/parn%C3%A1m\"\nW_RUDBAR = \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF%D8%A8%D8%A7%D8%B1\"\nE_EUPH = \"https://www.etymonline.com/word/Euphrates\"\nE_PASS = \"https://www.etymonline.com/word/passport\"\n\nPOK_SUP = {\"ref\": \"POK:817\", \"status\": \"supports\",\n \"note\": \"Pokorny IEW 816-817, 'per-2. B. per-, pera- : hinüberführen, hinüberbringen, übersetzen, durchdringen, fliegen'. The entry ends 'Page(s): 816-817' in POK_full.txt (grep -n 'lemma: per-2. B'), and contains verbatim: \\\"per-tu-, por-tu-, Gen. pr̥teus 'passage, ford': Avestan pərətu-š m.f. ... 'passage, ford, bridge' (hu-parəθwa- 'good to overstep' = 'Euphrat'); Latin portus ... besides a-stem porta 'Stadttor, Tor'\\\".\"}\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(id=1, lang=\"Avestan\", words=\"peretu\", verdict=\"confirmed\",\n  derivation=\"Avestan pərətu- (stem pərətav-, also the parallel pəšu-) 'passage, ford, bridge' continues PIE *pértus / *pr̥tu- 'crossing', a tu-stem built to the verbal root *per- 'to cross over' (Av. verbal root par-, OAv. subj. fra-frā 'I shall cross', Y 46.10). The word is best known from the compound cinvatō pərətu- 'the Bridge of the Separator' (Y 46.10-11, Y 71.16, V 19.30). Exact cognates: Lat. portus 'harbour' (< 'entrance, passage'), OE ford, OHG furt, ON fjǫrðr, OW rit / W rhyd, Gaulish ritu- in Ritumagus, Augustoritum. Nourai's language label, form and gloss are all correct; the only nuance is that the word means 'ford, passage' as much as 'bridge'.\",\n  derivation_fa=\"اوستایی pərətu- (ستاک pərətav-؛ صورت هم‌سنگ pəšu-) به معنی «گذرگاه، گدار، پل» است و از ریشهٔ هندواروپایی آغازین *per- «گذشتن از» با پسوند اسم‌ساز ‎*-tu-‎ ساخته شده (‎*pértus‎). این واژه بیشتر در ترکیب cinvatō pərətu- «پل چینوَد» در اوستا دیده می‌شود. هم‌ریشه‌های آن لاتینی portus «بندر»، انگلیسی کهن ford و ولزی rhyd «گدار» است. بارتولومه (ستون ۸۹۲) و بوک (۱۰٫۷۴) این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n  sources=[W_PERTUS, W_POL],\n  ref_check=[POK_SUP,\n   {\"ref\": \"KLN:1220\", \"status\": \"supports\",\n    \"note\": \"Klein 1966, p.1220-21 (leaf 650, which carries the printed numerals 1220/1221) s.v. 'port, n., harbor, haven': 'L. portus, \\\"harbor\\\", orig. \\\"entrance, passage\\\" ... cogn. with Avestic peretush, \\\"passage, ford, bridge\\\", OW. rit, W. rhyd, \\\"ford\\\", OE. ford ... fr. I.-E. base *per-, \\\"to lead across, drive across, traverse, pierce\\\"'.\"}],\n  consulted=[\n   {\"src\": \"BRT\", \"where\": \"col. ~892, s.v. pərətav-\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt line 16069: \\\"j., g. pərətav- m., f. 1) 'Durchgang, Gang' ... 3) 'Durchgang durch —, Übergang über das Wasser, Furt, Brücke'\\\", with cinvatō pərətu- 'die Brücke des Scheiders'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 40 (s.v. per-)\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd2 djvu line 2612: \\\"av. pərətu-š m. f. (urar. *pr̥tu-s) und pəšu-s m. ... 'Durchgang, Furt, Brücke' (hu-parəθwa- 'gut zu überschreiten'; gall. ritu- 'Furt' ... ahd. furt, ags. ford 'Furt')\\\" — this is WP II 40, the source Pokorny 817 cites.\"},\n   {\"src\": \"SYN\", \"where\": \"10.74 BRIDGE\", \"stance\": \"supports\",\n    \"note\": \"Buck: 'Av. pəšu-, pərətu-, also \\\"ford, passage\\\"; OE ford, OHG furt \\\"ford\\\", Lat. portus \\\"harbor\\\", porta \\\"gate\\\", etc. Walde-P. 2.40.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p.294, *par² 'to go over, cross over'\", \"stance\": \"supports\",\n    \"note\": \"Cheung lists Avestan par- (fr-) 'to go over, cross over' with OAv. frafrā (Y 46.10) — the verb from which the tu-stem pərətu- is formed.\"}])\n\nN(id=2, lang=\"Pahlavi\", words=\"puhl\", verdict=\"confirmed\",\n  derivation=\"Middle Persian puhl [pwhl] 'bridge' is the regular southwestern continuant of Old Iranian *pr̥tu-/pərətu-: the Avestan cluster -rət- (< *-r̥t-) gives Middle Persian -hl-/-hr- (the same treatment as Av. arəta- > MP ahlav, Av. maša- forms in -hr-), and an earlier variant puhr is attested beside puhl; Parthian keeps the older shape pwrt. The word is common in the Zoroastrian Pahlavi books in činwad puhl, the Bridge of the Separator. Nourai's derivation from the Avestan word (rather than from a sister Old Iranian form) is the standard presentation and is correct in substance.\",\n  derivation_fa=\"فارسی میانه (پهلوی) puhl «پل» بازماندهٔ منظم ایرانی باستان *pr̥tu-/pərətu- است: خوشهٔ ‎-rət-‎ اوستایی در پهلوی جنوب‌غربی به ‎-hl-/-hr-‎ بدل می‌شود (همان دگرگونی که در arəta- > ahlav دیده می‌شود) و صورت puhr در کنار puhl به کار رفته است؛ پارتی صورت کهن‌تر pwrt را نگاه داشته. مکنزی و نیبرگ هر دو puhl «پل» را ثبت کرده‌اند، در ترکیب «چینوَد پل». ادعای نورایی درست است.\",\n  sources=[W_POL],\n  ref_check=[{\"ref\": \"SNS:137\", \"status\": \"supports\",\n    \"note\": \"Tavoosi's glossary to Šāyast nē Šāyast indexes 'puhl 137/6' and 'puhl ī ravān 137/10' (SNS_pages.txt line 15906-7), i.e. the word occurs at p.137 line 6 of the text Nourai cites — the citation is a text reference, and it checks out.\"}],\n  consulted=[\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.69, s.v. puhl\", \"stance\": \"supports\",\n    \"note\": \"PHD_mackenzie.txt line 4270: '1puhl [pwhl | N pul] bridge' (and '2puhl [pwhl] expiation, atonement; punishment'); also 'činwad [cynw(p)t'], ~ puhl: the \\\"divider bridge\\\"'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) s.v. puhl\", \"stance\": \"supports\",\n    \"note\": \"NYB_vol2_glossary.txt line 3169: \\\"puhl [pwhl, inscr. pwhly] bridge F:1. 64¹², 72¹²... — Av. (892) pərətu-, (897) pəšu- (cf arəta-, -ərəta-: aša < r̥ta-); MPrth pwrt (MHC); Paz. puh(a)l; NP pul.\\\" — the very chain Av. pərətu- > MP puhl > NP pul.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 325\", \"stance\": \"supports\",\n    \"note\": \"HRN.txt line 3096ff: '325. pul \\\"Brücke\\\". aw. peretu- \\\"Brücke\\\", pesu- \\\"Furt\\\" (d. i. peretü-, pešu-, Bartholomae, Ar. Forsch. II, 35 ff.); phlv. puhr, puhl \\\"Brücke, Furt\\\".'\"},\n   {\"src\": \"DRM\", \"where\": \"Études iraniennes I, leaf 125 (§ on r > l)\", \"stance\": \"supports\",\n    \"note\": \"DRM.txt line 2050: 'Parthaviya, parthicus / peretu, pont (*perethu) pûhl' — Darmesteter uses the pair as his example of Avestan -r- becoming -l- in Pahlavi.\"}])\n\nN(id=3, lang=\"Persian\", words=\"pol «پُل»\", verdict=\"confirmed\",\n  derivation=\"New Persian پل pol continues MP puhl directly: the Middle Persian cluster -hl- is simplified to -l- and the preceding u is shortened/lowered to o, giving pol (Manichaean and Pazand still show puh(a)l). The word is standard from the earliest New Persian; the Ṣāʾeb couplet Nourai quotes ('پل بسته‌ای که بگذری از آبروی خویش') uses it in the ordinary sense 'bridge'. Mo'in's own etymological footnote in Borhān-e Qāṭeʿ gives exactly this chain.\",\n  derivation_fa=\"فارسی نو «پُل» دنبالهٔ مستقیم فارسی میانهٔ puhl است: خوشهٔ ‎-hl-‎ ساده شده و ‎u‎ به ‎o‎ بدل گشته است (در پازند هنوز puh(a)l دیده می‌شود). معین در حاشیهٔ برهان قاطع همین زنجیره را آورده است: «اوستا pərətu- (پل)، pəšu- (گدار، پایاب)؛ پهلوی puhr, puhl (پل، گدار)». ویکی‌واژه نیز پل را از پهلوی puhl و آن را از *pértus هندواروپایی می‌داند. ادعای نورایی درست است.\",\n  sources=[W_POL, W_PERTUS],\n  ref_check=[{\"ref\": \"BQT:414\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, vol.1, the پل entry (BQT_v1_pages.txt leaf 640, printed p. ≈414-417): headword 'پل - بفتح اول و سکون ثانی' with Moʿin's footnote 6 read from the scan: 'اوستا pərətu- (پل)، pəšu- (گدار، پایاب)؛ پهلوی puhr, puhl (پل، گدار)'. Page number matches Nourai within the scan's 2-3 leaf drift.\"}],\n  consulted=[\n   {\"src\": \"HRN\", \"where\": \"Horn no. 325 (np. pul)\", \"stance\": \"supports\",\n    \"note\": \"'325. pul \\\"Brücke\\\" ... phlv. puhr, puhl'; Horn's footnote 2 warns 'Nie pul gesprochen oder geschrieben (Vullers), das nur \\\"Geld\\\" bedeutet' — i.e. the vowel is o, not u, exactly Nourai's transliteration pol.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, IE-roots dictionary, Latin index pdf p.172\", \"stance\": \"supports\",\n    \"note\": \"ARY_latin_index_pages.txt lines 4947-48 group Persian پل with 'PERETU, PESHU, PERETUSH (AVESTAN)', 'PUHL, PUHR (PAHLAVI)', Kurdish 'PEL, PURD, PIRD, PIR', Afghan 'PUL', Latin PORTUS/PORTA, Gothic FARJAN, OE FORD.\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary s.v. puhl\", \"stance\": \"supports\",\n    \"note\": \"'... Paz. puh(a)l; NP pul.'\"}])\n\nN(id=4, lang=\"Avestan\", words=\"hu-parathwa\", verdict=\"plausible\",\n  derivation=\"The form Nourai gives is the traditional reconstruction *hu-parəθβa- 'good to cross over' (hu- 'good' + a -θβa- adjective to par-/pərətu-), which Walde-Pokorny II 40 and Pokorny 817 cite in parentheses to explain the river name. Two caveats: (a) it is NOT an attested Avestan word — Bartholomae's Altiranisches Wörterbuch has hu-paitištāna-, hu-pairištā-, hu-parəna-, hu-paurva- but no *hu-parəθβa-; the attested name is OLD PERSIAN Ufrātu- (DB 1.92 Ufrātuvā); (b) Kent, Old Persian, s.v. Ufrātu- calls the whole equation 'probably a popular etymologizing in OP of a local non-Iranian name', the underlying name being Akkadian Purattu (Sumerian Buranuna), Elamite ú-ip-ra-tu-iš. So the segmentation hu- + *parəθu- is a real ancient (Old Persian) folk etymology, but the language label 'Avestan' is wrong and the etymology is secondary, not the origin of the name.\",\n  derivation_fa=\"صورت *hu-parəθβa- «خوش‌گذر» (hu- «خوب» + صفتی بر ستاک par-/pərətu-) بازسازی‌شده است و در اوستا شاهدی ندارد؛ بارتولومه در «واژه‌نامهٔ ایرانی باستان» چنین سرواژه‌ای ندارد. آنچه واقعاً گواهی شده پارسی باستان Ufrātu- است (کتیبهٔ بیستون ۱٫۹۲). کنت این ریشه‌شناسی را «ریشه‌شناسی عامیانهٔ پارسی باستان برای نامی بومی و غیرایرانی» می‌داند که اصل آن اکدی Purattu (سومری Buranuna) است. پس تجزیهٔ نورایی یک ریشه‌شناسی عامیانهٔ کهن (و درست‌نمای) است، اما برچسب «اوستایی» نادرست است؛ با احتیاط پذیرفتنی است.\",\n  sources=[E_EUPH, W_FORAT],\n  ref_check=[POK_SUP,\n   {\"ref\": \"AHD:452\", \"status\": \"not_checked\",\n    \"note\": \"Nourai's AHD:452 is a page of the 1975/76 AHD New College main dictionary (the 'Euphrates' entry), which is not open online (IA copies are lending-only). The 1985 Watkins standalone appendix on disk (AHD_watkins1985.txt, root 'per-2. To lead, pass over ... [Pok. 2. B. per 816]') does NOT mention Euphrates, so the claim could not be checked in the local AHD text; Etymonline reproduces the same AHD-style account ('Greek Euphrates, from Old Persian Ufratu, perhaps from Avestan huperethuua \\\"good to cross over\\\"').\"}],\n  consulted=[\n   {\"src\": \"BRT\", \"where\": \"hu- compounds, cols. ~1828-1831\", \"stance\": \"contradicts\",\n    \"note\": \"grep 'hu-p' in BRT.txt returns hu-paitištāna-, hu-pairi.tan-, hu-pairi.spi-, hu-pairištā-, hu-parəna-, hu-paurva-, hu-pita-, hu-puθra-, hu-ptar- — there is no *hu-parəθβa- headword, and 'Euphrat' occurs in BRT only s.v. urvā- (the Euphrates delta).\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. Ufrātu-\", \"stance\": \"contradicts\",\n    \"note\": \"KNT.txt line 5184: \\\"Ufrātu- sb. 'Euphrates', river of Babylonia: Elam. ú-ip-ra-tu-iš, Akk. purattu, Gk. Εὐφράτης ... Etymology uncertain, probably a popular etymologizing in OP of a local non-Iranian name, cf. Bthl. AiW 1830\\\"; and line 1042 lists Ufrātu- among OP words 'definitely borrowings from outside sources'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 40\", \"stance\": \"supports\",\n    \"note\": \"\\\"(hu-parəθwa- 'gut zu überschreiten'\\\" is given there in parentheses beside av. pərətu-š — the source of Pokorny's parenthesis and, ultimately, of Nourai's node.\"}])\n\nN(id=5, lang=\"Persian\", words=\"forât «فُرات»\", verdict=\"disputed\",\n  derivation=\"Persian فرات forāt is NOT an inherited Iranian word and does not descend from *hu-parəθβa-. It is a straightforward Arabic loan: Arabic الفُرات al-Furāt, itself from Aramaic Pərāt / Akkadian Purattu (cuneiform ÍD.UD.KIB.NUN, Sumerian Buranuna), the local Mesopotamian name of the river. The Arabic form was carried into Persian with the Qurʾānic/Islamic geographical vocabulary (Q 25:53 uses furāt as an adjective 'sweet, fresh' of water, a secondary Arabic re-analysis). The Persian شکل with initial f- and the vowel ā points to Arabic, not to an Iranian *hu-p- > *fr- development, which would have had to yield something like **hufrād. Even the Old Persian Ufrātu- (which does show the hu-p- shape) was not the ancestor of the Persian word; modern Persian took the name back from Arabic.\",\n  derivation_fa=\"«فُرات» در فارسی نو واژه‌ای موروثی نیست، بلکه وام‌واژه‌ای عربی است: از «الفُرات» عربی، و آن از آرامی Pərāt / اکدی Purattu (سومری Buranuna)، نام بومی بین‌النهرینی رود. ویکی‌واژه صریحاً می‌گوید فارسی فرات از عربی الفرات وام گرفته شده و عربی آن از اکدی است. اگر واژه از *hu-parəθβa- ایرانی می‌آمد، شکلی مانند **هوفراد انتظار می‌رفت، نه «فرات». پس پژوهش امروزی ادعای نورایی را رد می‌کند: این یک دورزدن سامی–عربی است، نه ارثِ ایرانی.\",\n  sources=[W_FORAT, E_EUPH],\n  ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives no reference for this node.\"}],\n  consulted=[\n   {\"src\": \"KNT\", \"where\": \"Lexicon s.v. Ufrātu-\", \"stance\": \"contradicts\",\n    \"note\": \"'Akk. purattu ... Etymology uncertain, probably a popular etymologizing in OP of a local non-Iranian name' — the Semitic name is primary, so the Persian form cannot be an Iranian inheritance.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān\", \"stance\": \"silent\",\n    \"note\": \"grep 'Furat'/'furat'/'Euphrat' in FVQ.txt and FVQ_pages.txt returns no entry — Jeffery does not treat فرات among the Qurʾānic foreign words, so no support for an Iranian source from that side either.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ (Moʿin ed.)\", \"stance\": \"silent\",\n    \"note\": \"فرات is an Arabic proper name and is not treated with a Persian etymology in the پ/ف material consulted; Moʿin's footnotes give no Iranian origin for it.\"}])\n\nN(id=6, lang=\"Greek\", words=\"Euphrates\", verdict=\"plausible\",\n  derivation=\"Greek Εὐφράτης (Herodotus, Xenophon and the whole classical tradition) is indeed the Iranian-mediated form of the river name — but the immediate source is Old Persian Ufrātu- (acc./instr. Ufrātuvā, DB 1.92), not an Avestan word. Greek re-shaped Ufrātu- as Εὐφράτης: initial u- was heard as εὐ- (helped by the Greek prefix εὐ- 'well', which matches the OP folk etymology hu- 'good'), the -tu- stem was converted to a first-declension masculine in -ης, and the aspiration of -φ- reflects the Iranian f. So the arrow Iranian → Greek is right; the parent node's 'Avestan' label is the weak point.\",\n  derivation_fa=\"یونانی Εὐφράτης بی‌گمان صورت یونانی‌شدهٔ نام ایرانی رود است، اما سرچشمهٔ مستقیم آن پارسی باستان Ufrātu- است (بیستون ۱٫۹۲)، نه واژه‌ای اوستایی. یونانی u- آغازین را εὐ- شنیده (با کمک پیشوند εὐ- «خوب» که با ریشه‌شناسی عامیانهٔ hu- «خوب» پارسی باستان هم‌خوان است) و ستاک ‎-tu-‎ را به صرف نخستِ مذکر ‎-ης‎ برده است. پس پیوند ایرانی ← یونانی درست است و تنها برچسب زبانِ گرهِ بالادست جای ایراد دارد؛ با احتیاط پذیرفتنی است.\",\n  sources=[E_EUPH],\n  ref_check=[{\"ref\": \"AHD:452\", \"status\": \"not_checked\",\n    \"note\": \"Same as node 4: the 1975/76 AHD main-dictionary page is not accessible; the 1985 Watkins appendix (root per-2) on disk does not mention Euphrates. Etymonline's entry ('Greek Euphrates ... Old Persian Ufratu') reproduces the same claim.\"}],\n  consulted=[\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. Ufrātu- and §166\", \"stance\": \"partial\",\n    \"note\": \"'Elam. ú-ip-ra-tu-iš, Akk. purattu, Gk. Εὐφράτης' — Kent equates the Greek with OP Ufrātu- (supporting the Iranian→Greek arrow) but denies the *hu-parəθwa- etymology.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966\", \"stance\": \"silent\",\n    \"note\": \"grep 'Euphrat' in KLN_1966.txt gives only incidental mentions (s.v. 'Fertile Crescent', 'Kufic', 'Mesopotamia'); Klein has no headword 'Euphrates'.\"}])\n\nN(id=7, lang=\"Latin\", words=\"\", verdict=\"confirmed\",\n  derivation=\"Pass-through node: Latin Euphrātēs, -is (Cicero, Pliny, the Vulgate) is a direct transliteration of Greek Εὐφράτης, with the Greek -ης rendered by the Latin Greek-declension -ēs. Latin is the channel through which the name entered the Western European languages, above all through the Vulgate's Euphrates in Genesis 2:14 and Revelation 9:14.\",\n  derivation_fa=\"گرهٔ واسطه: لاتینی Euphrātēs برگردان مستقیم یونانی Εὐφράτης است و پایانهٔ ‎-ης‎ یونانی در صرفِ یونانی‌تبارِ لاتین به ‎-ēs‎ بدل شده است. همین صورت لاتینی، به‌ویژه از راه ترجمهٔ ولگات (پیدایش ۲:۱۴)، نام رود را به زبان‌های اروپای غربی رسانده است. ادعای نورایی درست است.\",\n  sources=[E_EUPH],\n  ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this pass-through node.\"}],\n  consulted=[\n   {\"src\": \"KLN\", \"where\": \"Klein 1966\", \"stance\": \"silent\", \"note\": \"no 'Euphrates' headword (grep 'Euphrat').\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet\", \"stance\": \"silent\", \"note\": \"grep 'Euphrat' in LAT.txt returns nothing; Ernout-Meillet treats only Latin appellatives, not Greek river names.\"}])\n\nN(id=8, lang=\"English\", words=\"Euphrates\", verdict=\"confirmed\",\n  derivation=\"English Euphrates comes through Latin: Old English already has Eufrate (in the biblical texts), and the modern spelling with -ph- and -es follows the Latin/Vulgate Euphrates; the English pronunciation with stress on the second syllable (yoo-FRAY-teez) reflects the Latin Greek-type declension. Etymonline gives exactly this chain: 'Old English Eufrate, from Greek Euphrates, from Old Persian Ufratu'.\",\n  derivation_fa=\"انگلیسی Euphrates از راه لاتین آمده است: در انگلیسی کهن صورت Eufrate در متون کتاب مقدس دیده می‌شود و املای امروزی با ‎-ph-‎ و ‎-es‎ از لاتینِ ولگات گرفته شده است. اتیمولاین همین زنجیره را می‌آورد. ادعای نورایی درست است.\",\n  sources=[E_EUPH],\n  ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n  consulted=[\n   {\"src\": \"KLN\", \"where\": \"Klein 1966\", \"stance\": \"silent\", \"note\": \"no headword 'Euphrates' in Klein.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict.\", \"stance\": \"silent\", \"note\": \"grep 'Euphrat' in WEB_vol1.txt returns no etymological entry for the proper name.\"}])\n\nN(id=9, lang=\"Avestan\", words=\"par 2; pâra 2\", verdict=\"confirmed\",\n  derivation=\"Both words are real and both belong to this root. (a) Avestan para (Bartholomae's ²para) is an adverb/preposition 'away, aside; formerly, before', the instrumental of the stem *para- 'further, beyond' (Skt. párā 'away, forth', OP para 'beyond'); Pokorny 812 (per-2 A.b) lists 'Old Indic parā, Avestan para (Instr. Sg.) adverbal \\\"fort, weg, zur Seite\\\"'. Nourai's gloss 'there, over there' is a loose rendering of this 'away, yonder'. (b) Avestan ²pāra- m. 'shore, bank; border, limit, end' (Bartholomae: \\\"¹) 'Ufer'. a) 'Grenze, Ende'\\\", cf. the compound dūraē-pāra- 'whose shores lie far away') is the lengthened-grade noun to par- 'to cross', exactly like Skt. pāra- n. 'the further bank'. Pokorny 816 has it verbatim: 'Avestan pāra- n. \\\"bank, border, shore; limit, boundary, end\\\"'. Nourai's numbering 'par 2 / pāra 2' reproduces Bartholomae's own superscript ² for both entries.\",\n  derivation_fa=\"هر دو واژه اصیل‌اند و از همین ریشه‌اند. یکی: اوستایی para (صورت ²para نزد بارتولومه) قید و حرف اضافه به معنی «دور، کنار؛ پیش‌تر، پیشین» است، برابر سنسکریت párā «دور، فراسو» و پارسی باستان para «فراسوی»؛ ترجمهٔ نورایی «آنجا، آن‌سو» برگردانی آزاد از همین معنی است. دو: اوستایی ²pāra- «کرانه، لبه، مرز، پایان» (بارتولومه: «Ufer؛ Grenze, Ende»، نک. ترکیب dūraē-pāra- «دورکرانه») اسمی با مصوت کشیده بر ستاک par- «گذشتن» است، درست مانند سنسکریت pāra- «آن‌سوی رود». پوکورنی در ص ۸۱۶ همین را آورده است. شماره‌گذاری نورایی نیز از شماره‌گذاری بارتولومه گرفته شده. ادعای نورایی درست است.\",\n  sources=[W_PERTUS],\n  ref_check=[{\"ref\": \"POK:816\", \"status\": \"supports\",\n    \"note\": \"Pokorny 816 (per-2 B, first paragraph of the Material): \\\"Old Indic para- 'hinüberbringend, übersetzend', m. n. 'jenseitiges bank, border, shore, purpose, äußerste limit, boundary' ..., Avestan pāra- n. 'bank, border, shore; limit, boundary, end'\\\"; the adverb para 'fort, weg, zur Seite' is under per-2 A.b.\"}],\n  consulted=[\n   {\"src\": \"BRT\", \"where\": \"cols. ~851 (²para) and ~888 (²pāra-)\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt line 16022: \\\"j., p. ²pāra- m. 1) 'Ufer'. a) 'Grenze, Ende'\\\" (with 'Zum V. par-; ai. pārá- m.'), and line 15348: \\\"j., g., p. ²para 1) Adv. 'zuvor'; 2) zeitlich 'vordem, ehedem'\\\" — so the gloss 'there, over there' is looser than Bartholomae's 'zuvor / fort, weg', but the forms and the root are right.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck\", \"stance\": \"silent\",\n    \"note\": \"Buck has no 'shore' chapter entry citing Av. pāra-; grep returned nothing relevant.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p.294 *par²\", \"stance\": \"supports\",\n    \"note\": \"The verbal root Av. par- 'to go over, cross over' from which pāra- 'far bank' is built.\"}])\n\nN(id=10, lang=\"Pahlavi\", words=\"bâr 2\", verdict=\"confirmed\",\n  derivation=\"Middle Persian -bār 'shore, bank, riverside country' continues Old Iranian *pāra- 'shore'. The initial b- instead of p- is not an irregularity: the word survives only as the second member of compounds, where its *p- stood between vowels (*rauta-pāra- 'river-shore') and therefore underwent the regular Middle Persian lenition of intervocalic p > b (the same change as OIr. *āp- > MP āb 'water'). The compound is attested in Pahlavi: Horn cites 'phlv. -bār, z. B. rōt|bār (Bundahišn)'. Darmesteter, Études iraniennes I §244 (p.289), states it in so many words: 'Le suffixe bar s'ajoute aux noms de lieu, en général aux noms de pays maritimes. C'est le mot zend pāra, côte (cf. dūraē-pāra)'.\",\n  derivation_fa=\"فارسی میانه ‎-bār‎ «کرانه، ساحل، سرزمینِ کنارِ آب» دنبالهٔ ایرانی باستان *pāra- «کرانه» است. «ب» آغازین آن بی‌قاعده نیست: این واژه تنها جزء دوم ترکیب‌ها بوده و در آن جایگاه «پ» میان دو واکه قرار می‌گرفته (*rauta-pāra-) و بنا بر قاعدهٔ نرم‌شدن «پ» میان‌واکه‌ای در فارسی میانه به «ب» بدل شده است — همان دگرگونی که در *āp- > āb «آب» می‌بینیم. هرن صورت پهلوی rōt-bār را از بندهش گواه می‌آورد و دارمستتر (مطالعات ایرانی، دفتر یکم، بند ۲۴۴) صریحاً می‌گوید این پسوند همان «pāra ی زند، به معنی کرانه» است. ادعای نورایی درست است.\",\n  sources=[W_RUDBAR],\n  ref_check=[{\"ref\": \"AEF:209\", \"status\": \"not_checked\",\n    \"note\": \"AEF = Khaleqi Motlaq's Persian translation/expansion of Horn's Grundriss; the book is print-only (refs_online.json: 'Not online'). Its content at this point is Horn no.158, which IS on disk and does say exactly what Nourai claims (see the HRN line in 'consulted').\"}],\n  consulted=[\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 158\", \"stance\": \"supports\",\n    \"note\": \"HRN.txt line 1763-65: '158. (3)bār in Comp. jōi|bār, deryā|bār, rōd|bār, Zeng|bār, Hindū|bār. — aw. pāra- \\\"Ufer, Rand\\\"; phlv. -bār, z. B. rōt|bār (Bund.); ai. pāra- \\\"Ufer\\\".'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. bar\", \"stance\": \"silent\",\n    \"note\": \"PHD_mackenzie.txt line 1492 has only 'bar [bl | N ~] fruit, produce, profit' and 'bar-, ~išn, v. burdan'; MacKenzie does not list an independent MP bār 'shore' — consistent with the word existing only inside compounds.\"},\n   {\"src\": \"DRM\", \"where\": \"Études iraniennes I, §244, p.289 (leaf 328)\", \"stance\": \"supports\",\n    \"note\": \"'§244. bar. — Le suffixe bar s'ajoute aux noms de lieu, en général aux noms de pays maritimes. C'est le mot zend para, côte (cf. dūraē-pāra, la terre aux rives lointaines).'\"}])\n\nN(id=11, lang=\"Persian\", words=\"bâr 3 «-بار ۳»\", verdict=\"confirmed\",\n  derivation=\"New Persian -بار -bār is a productive place-name suffix meaning 'shore, riverside country', abstracted from compounds: رودبار rūdbār 'river country, place of many streams' (MP rōd-bār, Bundahišn), جویبار jūybār 'brookside', دریابار daryābār 'maritime land', زنگبار Zangbār 'the coast of the Zanj' = Zanzibar, and (Darmesteter adds) هندوبار Hindūbār and the -bar of Malabar (< Malaya-pāra). Wiktionary derives رودبار directly from Middle Persian lwtbʾl /rōd-bār/ 'river bank'. Darmesteter warns — correctly — not to confuse this -bār with the homophonous -bār 'time(s)' (< Skt. vāra-) or بار 'load' (< *bhāra-), which are separate words; Nourai's own numbering 'bār 3' keeps them apart, following Horn's bār 1 / bār 2 / bār 3.\",\n  derivation_fa=\"پسوند «-بار» در فارسی نو به معنی «کرانه، سرزمینِ کنارِ آب» از دل ترکیب‌ها انتزاع شده است: رودبار (فارسی میانه rōd-bār در بندهش)، جویبار، دریابار، زنگبار (کرانهٔ زنگیان = زنگبار امروزی) و به گفتهٔ دارمستتر هندوبار و «-بار» در مالابار (< Malaya-pāra). ویکی‌واژه «رودبار» را مستقیماً از فارسی میانهٔ ‎lwtbʾl‎ /rōd-bār/ «کرانهٔ رود» می‌داند. دارمستتر هشدار می‌دهد که این «-بار» را نباید با «بار» به معنی «دفعه» (از vāra- سنسکریت) یا «بار» به معنی «محموله» (از *bhāra-) اشتباه گرفت؛ شماره‌گذاری «بار ۳» نزد نورایی (به پیروی از هرن) همین تفکیک را نگاه می‌دارد. ادعای نورایی درست است.\",\n  sources=[W_RUDBAR],\n  ref_check=[{\"ref\": \"AEF:209\", \"status\": \"not_checked\",\n    \"note\": \"AEF (Khaleqi Motlaq's Persian Horn) is print-only; the corresponding Horn entry no.158 was checked instead and lists precisely Nourai's four examples jōibār, deryābār, rōdbār, Zangbār.\"}],\n  consulted=[\n   {\"src\": \"DRM\", \"where\": \"Études iraniennes I §244, pp.289-290\", \"stance\": \"supports\",\n    \"note\": \"'hindu-bār, le pays d'Inde ... Zang-bār, le pays des Zang (côte orientale d'Afrique); daryā-bār, pays maritime; rūd-bār, région fluviale; jūy-bār ... Il s'agit toujours de pays où l'on aborde par les côtes; de là l'emploi de pāra. Il ne faut pas confondre ce suffixe bar = para avec le suffixe bar marquant itération et qui est le sanscrit vāra, fois.'\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 156-158\", \"stance\": \"supports\",\n    \"note\": \"Horn separates (1)bār 'Last' (< ai. bhārá-), (2)bār 'Mal' (< skr. vāra-) and (3)bār in the compounds — the same three-way split Nourai's 'bār 3' presupposes.\"},\n   {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi\", \"stance\": \"silent\",\n    \"note\": \"grep of رودبار / جویبار in MON_part1/2 returned no etymological bracket for the suffix itself; Moʿin treats them as place names.\"}])\n\nN(id=12, lang=\"Avestan\", words=\"parena\", verdict=\"confirmed\",\n  derivation=\"Avestan parəna- n. 'feather, wing' is well attested (Yt 10.39, Yt 10.101; compounds ərəzifyō.parəna- 'fitted with eagle feathers', kahrkāsō.parəna- 'with vulture feathers', hu-parəna- 'well-winged', Yt 13.70). It reflects *por-no- 'feather, wing', with exact cognates Skt. parṇá- 'feather, leaf', OCS pero 'feather', Lith. sparnas 'wing' (with secondary s-), OHG farn / OE fearn 'fern' (i.e. 'feather-plant'). Its attachment to this root is exactly what Pokorny's own addendum to p.817 — printed on p.850, which is why Nourai cites 'POK:817,850' — asserts. Modern reconstruction is slightly different: Wiktionary/LIV assign *pornóm to a root *perH- 'to fly' (or *(s)per-) kept apart from *per- 'to cross', so the two are cognate-adjacent rather than the same root; Watkins hedges with 'Possibly suffixed form *por-no-, feather, wing (< \\\"that which carries a bird in flight\\\")'.\",\n  derivation_fa=\"اوستایی parəna- «پر، بال» به‌خوبی گواهی شده است (یشت ۱۰٫۳۹ و ۱۰٫۱۰۱، و ترکیب‌هایی چون ərəzifyō.parəna- «با پر عقاب» و hu-parəna- «خوش‌بال»). این واژه بازتاب *por-no- است با هم‌ریشه‌های دقیق سنسکریت parṇá-، اسلاوی کهن pero و لیتوانیایی sparnas. پیوند آن با ریشهٔ per- همان چیزی است که پوکورنی در «افزودهٔ» صفحهٔ ۸۱۷ آورده و آن افزوده در صفحهٔ ۸۵۰ چاپ شده است — و ارجاع دوگانهٔ نورایی «POK:817,850» دقیقاً به همین اشاره دارد. البته بازسازی امروزی (ویکی‌واژه، LIV) *pornóm را به ریشهٔ جداگانهٔ *perH- «پریدن» می‌برد، نه *per- «گذشتن»؛ واتکینز نیز با «احتمالاً» سخن می‌گوید. ادعای نورایی، در چارچوب پوکورنی، درست است.\",\n  sources=[W_PARNAM, W_PAR],\n  ref_check=[{\"ref\": \"POK:817,850\", \"status\": \"supports\",\n    \"note\": \"Pokorny, 'addendum to S. 817' (printed on p.850): \\\"To Church Slavic pero 'feather' belong *por-no- 'feather' in Old Indic parṇa- n. 'feather, leaf', Avestan parəna- n. 'feather, wing', Old Saxon/OHG farn 'Farnkraut' (*Federkraut), Old English fearn, Lithuanian sparnas ... 'wing' (das s- from the root spher-)\\\". Both page numbers in Nourai's citation are therefore correct and necessary.\"}],\n  consulted=[\n   {\"src\": \"BRT\", \"where\": \"cols. ~869, ~894\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt line 15704/16127: \\\"j. parəna- n. 1) 'Feder' ...\\\"; also ərəzifyō.parəna- 'mit Adlerfedern besetzt' (V 17.9, Yt 10.39) and hu-parəna- 'wohlbeflügelt' (Yt 13.70).\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 21 (under pet-)\", \"stance\": \"partial\",\n    \"note\": \"\\\"ein *per(ə)- dieser Bed. auch in ai. parṇá-m 'Flügel, Schwungfeder, Feder, Blatt', av. parəna- 'Feder, Flügel', ahd. far(n), ags. fearn 'Farn' ... lit. sparnas 'Flügel'\\\" — Walde-Pokorny put it under a *per(ə)- 'fly' beside pet-, i.e. the same family but a different numbered root.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.393 FEATHER\", \"stance\": \"supports\",\n    \"note\": \"Buck's table for 'feather' gives 'Skt. parṇa-, pattra-; Av. parəna-'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, per-2 II.5\", \"stance\": \"partial\",\n    \"note\": \"AHD_watkins1985.txt: 'per-2. To lead, pass over. ... 5. Possibly suffixed form *por-no-, feather, wing (< \\\"that which carries a bird in flight\\\"), in: a. Germanic *farnō ... Old English fearn, fern; b. Sanskrit parṇam, leaf, feather: PAN2. [Pok. 2. B. per 816.]' — same attachment as Nourai, but flagged 'Possibly'.\"}])\n\nN(id=13, lang=\"Persian\", words=\"par «پَر»\", verdict=\"confirmed\",\n  derivation=\"New Persian پَر par(r) 'feather, wing' continues Middle Persian parr [pl] (Manichaean pr) < Old Iranian *parna-, with the regular loss of the cluster -rn- > -rr- (compare MP zarr < *zarnya-). From the noun comes the denominative verb پریدن parīdan/parrīdan 'to fly' (MP parritan/parristan, Nyberg's Glossary), and — per Darmesteter, Études iraniennes I §237, p.286, the very page Nourai cites — پروانه parvāna 'butterfly' with the suffix -vāna (MP parvānak 'papillon'), literally 'the winged one'. Cognates: Kurdish per, Pashto pana, Balochi pan(n) 'leaf', Khotanese pārra-, Sogdian prn 'feather'.\",\n  derivation_fa=\"«پَر» فارسی نو دنبالهٔ فارسی میانهٔ parr (مانوی pr) است، از ایرانی باستان *parna-، با همگونی منظم خوشهٔ ‎-rn-‎ به ‎-rr-‎ (مانند zarr از *zarnya-). از همین اسم فعلِ اشتقاقی «پریدن» (پهلوی parritan/parristan نزد نیبرگ) ساخته شده و — بنا بر دارمستتر، مطالعات ایرانی، دفتر یکم، بند ۲۳۷، ص ۲۸۶، همان صفحه‌ای که نورایی ارجاع داده — «پروانه» با پسوند ‎-vāna‎ (پهلوی parvānak «پروانه») یعنی «بال‌دار». هم‌ریشه‌ها: کردی per، پشتو pana، بلوچی pan(n) «برگ»، ختنی pārra-، سغدی prn. هرن (شمارهٔ ۲۹۳) و هوبشمان نیز همین را دارند. ادعای نورایی درست است.\",\n  sources=[W_PAR, W_PARNAM],\n  ref_check=[\n   {\"ref\": \"BQT:397\", \"status\": \"partial\",\n    \"note\": \"Borhān-e Qāṭeʿ vol.1: the headword پر is at leaf 599 of BQT_v1_pages.txt — 'پر - بفتح اول و سکون ثانی، معروف است که بال و پر باشد و عربان ریش خوانند ... و پرِ درخت را هم می‌گویند' — which on the scan's leaf↔page mapping (leaf ≈ page + 223) is printed p. ≈376, whereas p.397 falls on the پری/پریدن/پریشیدن leaves (620-622), i.e. on the derivative پریدن that Nourai lists as 'extra'. The reference points at the right word-family; the page fits the derivative rather than the headword.\"},\n   {\"ref\": \"DRM:286\", \"status\": \"supports\",\n    \"note\": \"Darmesteter, Études iraniennes I, §237 (leaf 325 of DRM.txt, which the running numbers fix at printed p.286): 'Le suffixe vān, vâna ... de par, aile, parvâna, papillon. Le suffixe pehlvi est vânak: parvânak, papillon.' Exactly Nourai's par → parvāne.\"}],\n  consulted=[\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 293\", \"stance\": \"supports\",\n    \"note\": \"HRN.txt line 2852: '293. perr \\\"Feder, Flügel\\\"; perīden, perrīden ... aw. parena- \\\"Feder, Flügel\\\"; phlv. par bezw. parr, par(r)ītan (Bund.), par(r)īš; ai. parṇá-; lit. sparnas \\\"Flügel\\\". kurd. per, zaza pel \\\"Flügel\\\".'\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"supports\",\n    \"note\": \"HUB.txt line 9272: '...dan \\\"fliegen\\\" (parrān \\\"fliegend\\\", Fird. I, 440, 126), zd. parena-'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Glossary s.v. parr, parrītan\", \"stance\": \"supports\",\n    \"note\": \"'parr [pl] feather, wing 3⁸, 9⁵ — Av. (869 sq., 894 sq.) parəna-, pərəna-; MPrs in pr-wr \\\"winged\\\", ʾspyd-pr \\\"white-winged\\\"; NP par(r).' and 'parrītan [plytn'], parristan [plstn'] to fly in the air — NP parrīdan.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV pp.296-297, *parⁿ 'to fly off, take wing'\", \"stance\": \"supports\",\n    \"note\": \"'AVESTAN: parəna- \\\"wing\\\" (Yt 10.39, Yt 10.101); MIDDLE PERSIAN: MMP pr, BMP pl /parr/ \\\"feather, wing\\\"; NWIR: NP parrīdan/parr- ... « PIE *por-no- \\\"wing, feather\\\" => LIV: – | Pok.: 850 (Nachtrag)' — Cheung cites the same Pokorny page 850 that Nourai cites.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie\", \"stance\": \"partial\",\n    \"note\": \"MacKenzie's Concise Pahlavi Dictionary has no separate 'parr' headword in the consulted text (grep), but Nyberg and Cheung both give the Book Pahlavi spelling pl /parr/.\"}])\n\nN(id=14, lang=\"Latin\", words=\"porta; portâre\", verdict=\"confirmed\",\n  derivation=\"Latin porta 'gate, city gate' is the a-stem beside portus 'harbour' (< 'entrance, passage'), both from the same zero-grade *pr̥-tu-/*pr̥-tā of *per- 'to cross'; Oscan [p]úrtam shows the same formation. portāre 'to carry' is a denominative/iterative *poritāre to an unattested *porere, matching Skt. píparti 'carries over', pārayati 'brings across', Gk. πείρω 'penetrate'. Pokorny 816-817 and Walde-Pokorny II 40 give exactly this; Nourai's bare 'AHD' citation is Watkins's per-2, III.2-3 ('Suffixed form *pr̥-tā in Latin porta, gate'; 'Suffixed (denominative) form *pr̥-to- in Latin portāre, to carry').\",\n  derivation_fa=\"لاتینی porta «دروازه» صورت ستاک ‎-ā‎ در کنار portus «بندر» (نخست «ورودی، گذرگاه») است و هر دو از درجهٔ صفرِ *pr̥-tu-/*pr̥-tā ریشهٔ *per- «گذشتن» می‌آیند؛ اوسکی [p]úrtam نیز همین ساخت را دارد. portāre «بردن» فعلی اشتقاقی (‎*poritāre‎) بر ستاکی ناگواهی‌شده ‎*porere‎ است و با سنسکریت píparti «از این‌سو به آن‌سو می‌برد» و pārayati هم‌سنگ است. پوکورنی (۸۱۶–۸۱۷)، والده-پوکورنی (دفتر دوم ص ۴۰) و واتکینز همین را می‌گویند. ادعای نورایی درست است.\",\n  sources=[W_PERTUS, E_PASS],\n  ref_check=[{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985, 'per-2. To lead, pass over': 'III. Zero-grade form *pr̥-. 1. Suffixed form *pr̥-tu-, passage, in ... b. Latin portus, harbor (< \\\"passage\\\"): PORT1; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr̥-tā in Latin porta, gate (> Old French porte, door): PORCH, PORT2, PORTAL ... 3. Suffixed (denominative) form *pr̥-to- in Latin portāre, to carry: PORT3, PORTABLE ... [Pok. 2. B. per 816.]'\"}],\n  consulted=[\n   {\"src\": \"POK\", \"where\": \"IEW 816-817\", \"stance\": \"supports\",\n    \"note\": \"'Latin porta, -āre \\\"bear, carry, guide, lead, drive, bringen, offer\\\", Umbrian portatu \\\"portato\\\"' and 'Latin portus, -ūs \\\"Haustür\\\" (XII tab.); \\\"harbor\\\" ... besides a-stem porta \\\"Stadttor, Tor\\\" = Oscan [p]úrtam'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 40\", \"stance\": \"supports\",\n    \"note\": \"'lat. portus \\\"Haustür (XII Tfln.); Hafen\\\", angiportus \\\"enge Passage, Nebengäßchen\\\"; daneben a-St. porta \\\"Stadttor, Tor\\\"'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. port- (1)\", \"stance\": \"supports\",\n    \"note\": \"IEC.txt line 13402: 'port- (1) (portos, a, us, is) \\\"way, passage, gate\\\". Cf. per-, perio (1), poros and pr̥t- (1). Lat. portus, gs. -ūs, m. \\\"harbour\\\"; porta, f. \\\"gate, entrance, mountain pass\\\"; Osc. púrta-, f. id.; OS fard ... OE fierd ...'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1220-21\", \"stance\": \"supports\",\n    \"note\": \"'port, tr.v., to carry ... fr. L. portāre, for *poritāre, freq. of a supposed primitive verb *porere, which is cogn. with OI. piparti, \\\"brings over\\\", parayati, \\\"carries over\\\", Gk. πείρειν \\\"to penetrate\\\", fr. I.-E. base *per-'.\"}])\n\nN(id=15, lang=\"French\", words=\"\", verdict=\"confirmed\",\n  derivation=\"Pass-through node: Old/Modern French porte 'door' < Latin porta, port 'harbour' < Latin portus, and porter 'to carry' < Latin portāre — all by the ordinary Gallo-Romance developments (loss of final -a > -e, of the Latin infinitive ending -āre > -er). French is the channel through which the Latin family reached both English (after 1066 and again in the later learned borrowings) and, in the 19th-20th centuries, Persian.\",\n  derivation_fa=\"گرهٔ واسطه: فرانسوی porte «در» از لاتینی porta، port «بندر» از portus و porter «بردن» از portāre، همه با تحولات عادی گالو-رومی (سایش پایانهٔ ‎-a‎ به ‎-e‎ و ‎-āre‎ به ‎-er‎). فرانسه همان مجرایی است که این خانوادهٔ لاتینی را هم به انگلیسی (پس از ۱۰۶۶ و سپس در وام‌های عالمانه) و هم در سدهٔ سیزدهم و چهاردهم خورشیدی به فارسی رسانده است. ادعای نورایی درست است.\",\n  sources=[E_PASS],\n  ref_check=[{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 per-2 III.2 explicitly routes the Latin through French: 'Latin porta, gate (> Old French porte, door): PORCH, PORT2, PORTAL, PORTCULLIS, PORTE-COCHERE, PORTER2, PORTICO, PORTIERE'.\"}],\n  consulted=[\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1220-21\", \"stance\": \"supports\",\n    \"note\": \"'port, n., harbor ... partly fr. OE. port, partly fr. OF. (= F.) port'; 'port, n., gate ... OF. (= F.) porte, fr. L. porta'; 'port, tr.v. ... derives fr. MF. (= F.) porter, \\\"to bear, carry\\\", fr. OF., fr. L. portāre'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"supports\",\n    \"note\": \"Skeat s.v. port likewise routes English port/porter/portal through Old French from Latin portus/porta/portāre.\"}])\n\nN(id=16, lang=\"Persian\", words=\"\", verdict=\"plausible\",\n  derivation=\"Modern Persian پاسپورت pāsport, ترانسپورت trānsport and اسپرت esport are 20th-century European loans, and French is the usual channel for that layer of Persian vocabulary (Moʿin's Farhang-e Fārsi tags پاسپورت '[فر.]', i.e. French, glossing it 'پروانه برای آزادی رفت و آمد اشخاص از مملکتی به مملکت دیگر؛ گذرنامه'). So for پاسپورت (< Fr. passeport) and ترانسپورت (< Fr. transport) Nourai's French route is right. اسپرت is less certain: French sport is itself an English re-borrowing of Old French desport, and Persian اسپرت (with prothetic e- before the cluster sp-) may equally have come through English or Russian; the ultimate Latin source portāre is the same either way. Note also that پاسپورت has since been displaced in official Persian by the calque گذرنامه.\",\n  derivation_fa=\"«پاسپورت»، «ترانسپورت» و «اسپرت» وام‌واژه‌های اروپاییِ سدهٔ اخیرند و مجرای معمولِ این لایه از واژگان فارسی زبان فرانسه است؛ معین در فرهنگ فارسی «پاسپورت» را با نشانهٔ ‎[فر.]‎ آورده و «پروانه برای آزادی رفت‌وآمد اشخاص از مملکتی به مملکت دیگر؛ گذرنامه» معنی کرده است. پس برای «پاسپورت» (از passeport) و «ترانسپورت» (از transport) مسیر فرانسویِ نورایی درست است. دربارهٔ «اسپرت» باید محتاط بود: خودِ sport فرانسوی وام‌گیری دوبارهٔ انگلیسی از desport فرانسوی کهن است و «اسپرت» فارسی (با «ا» افزوده پیش از خوشهٔ sp-) می‌تواند از راه انگلیسی یا روسی هم آمده باشد. با احتیاط پذیرفتنی است.\",\n  sources=[E_PASS],\n  ref_check=[{\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": \"Moʿin, Farhang-e Fārsi (MON_part1.txt line 28216): 'پاسپورت: [فر.] (اِ) پروانه برای آزادی رفت و آمد اشخاص از مملکتی به مملکت دیگر؛ گذرنامه؛ جواز عبور ...' — the [فر.] tag is Moʿin's mark for French. ترانسپورت and اسپرت are not in the two-volume text on disk (they would be in Moʿin vol.4, the foreign-words volume, which is not available), so only پاسپورت could be checked.\"}],\n  consulted=[\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. پاسپورت\", \"stance\": \"supports\",\n    \"note\": \"See ref_check; Moʿin marks the word French.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1220-21 s.v. port/sport\", \"stance\": \"partial\",\n    \"note\": \"Klein derives English sport from OF desport (des- + porter) — i.e. the word was French before it was English, which is why an 'اسپرت < French' route is arguable but not decisive.\"}])\n\nN(id=17, lang=\"English\", words=\"port, passport, transport, report, support, sport\", verdict=\"confirmed\",\n  derivation=\"All six are Latin portus/porta/portāre words that reached English through French. port 'harbour' is partly OE port (an early direct borrowing of L. portus), partly OF port; port 'gate' < OF porte < L. porta; passport (c.1500) < OF passeport 'authorization to pass through a port', passe (imperative of passer) + port; transport < L. trānsportāre 'carry across'; report < OF reporter < L. reportāre 'carry back'; support < OF supporter < L. supportāre 'carry up, bear'; sport is aphetic for Middle English disport < OF desport(er) 'to divert oneself' (des- + porter). Klein lists this whole set under port, 'to carry', and Watkins lists PORT1-3, COMPORT, DEPORT, EXPORT, IMPORT, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT under per-2.\",\n  derivation_fa=\"هر شش واژه از خانوادهٔ لاتینی portus/porta/portāre‌اند و از راه فرانسه به انگلیسی رسیده‌اند: port «بندر» تا اندازه‌ای از انگلیسی کهن port (وام مستقیم از portus) و تا اندازه‌ای از فرانسوی کهن port؛ passport (حدود ۱۵۰۰ م) از passeport فرانسوی کهن یعنی «اجازهٔ گذر از بندر»؛ transport از trānsportāre؛ report از reportāre؛ support از supportāre؛ و sport کوتاه‌شدهٔ disport انگلیسی میانه از desporter فرانسوی کهن (des- + porter). کلاین همهٔ این مجموعه را زیر مدخل port می‌آورد و واتکینز نیز همین‌ها را ذیل ریشهٔ per-2 فهرست کرده است. ادعای نورایی درست است.\",\n  sources=[E_PASS, W_PERTUS],\n  ref_check=[{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 per-2 III.3: 'Latin portāre, to carry: PORT3, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER1; COMPORT, DEPORT, EXPORT, IMPORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT.'\"}],\n  consulted=[\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 pp.1220-21\", \"stance\": \"supports\",\n    \"note\": \"s.v. port, 'to carry': '... fr. L. portāre ... See fare, v., and cp. port, \\\"gate\\\", port, \\\"harbor\\\", apport, comport, deport, disport, export, import, portly, purport, rapport, report, sport, support, transport, and the first element in portmanteau'; s.v. port 'harbor': '... cp. port, \\\"gate\\\", portico, portolano, opportune, importunate, and the second element in passport.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"supports\",\n    \"note\": \"Skeat likewise derives sport from disport (OF desporter) and passport from F. passeport.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary\", \"stance\": \"supports\",\n    \"note\": \"F&W gives the same Latin portāre base for port, report, support, transport.\"}])\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Per 2\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *per- (Pokorny per-2 B) 'to carry/lead across, to pass over' (also 'to fly'); tu-stem *pértus 'crossing, ford'\",\n  \"note\": (\"Pokorny IEW 816-817 heads the sub-root 'per-2. B. per-, pərā-' with the German gloss \"\n    \"'hinüberführen, hinüberbringen, übersetzen, durchdringen, fliegen' — literally 'to lead across, \"\n    \"bring across, ferry over, penetrate, fly'. Nourai's 'to lead or fly across' is a faithful rendering \"\n    \"of it, the language label 'Indo-European' is right, and his cross-reference to 'Per 1' matches \"\n    \"Pokorny's own arrangement (per-1 = the preposition/adverb 'forward, through', with B/C/D/E as \"\n    \"verbal roots 'belonging to the group of per-1' in Watkins's words). Watkins/AHD word the same root \"\n    \"'per-2. To lead, pass over. A verbal root belonging to the group of per-1. [Pok. 2. B. per 816.]'. \"\n    \"Two general remarks on the page: (1) the Euphrates branch (nodes 4-8) rests on a reconstruction that \"\n    \"Kent, the standard authority on Old Persian, explicitly calls a folk etymology of a Semitic name, and \"\n    \"Persian forāt is an Arabic loan, not an Iranian inheritance — this is the weakest branch on the page; \"\n    \"(2) the 'feather' branch (nodes 12-13) is Pokorny's, taken from his addendum printed on p.850, but \"\n    \"current reconstruction prefers a separate root *perH- 'to fly' for *pornóm.\"),\n  \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *per- (نزد پوکورنی per-2 بخش B، صص ۸۱۶–۸۱۷) با معنی آلمانی \"\n    \"«hinüberführen, hinüberbringen, übersetzen, durchdringen, fliegen» یعنی «از این‌سو به آن‌سو بردن، \"\n    \"گذراندن، نفوذ کردن، پریدن». برگردان نورایی «to lead or fly across» وفادار است و برچسب «هندواروپایی» \"\n    \"درست؛ ارجاع او به «Per 1» نیز با چیدمان خودِ پوکورنی و واتکینز می‌خواند. دو نکتهٔ کلی دربارهٔ این صفحه: \"\n    \"نخست آنکه شاخهٔ «فرات» (گره‌های ۴ تا ۸) بر بازسازی‌ای استوار است که کنت، مرجع اصلی پارسی باستان، آن را \"\n    \"آشکارا «ریشه‌شناسی عامیانه» برای نامی سامی می‌خواند و «فرات» فارسی وام‌واژه‌ای عربی است، نه میراث ایرانی؛ \"\n    \"دوم آنکه شاخهٔ «پر» (گره‌های ۱۲ و ۱۳) از «افزودهٔ» پوکورنی در صفحهٔ ۸۵۰ گرفته شده و بازسازی امروزی \"\n    \"*pornóm را به ریشهٔ جداگانهٔ *perH- «پریدن» می‌برد. در مجموع ریشه و معنی درست است.\"),\n  \"sources\": [W_PERTUS, E_EUPH],\n  \"ref_check\": [POK_SUP],\n  \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. per-2\", \"stance\": \"supports\",\n    \"note\": \"'per-2. To lead, pass over. A verbal root belonging to the group of per-1. ... [Pok. 2. B. per 816.]' — same root, same page reference as Nourai.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II pp. 39-40\", \"stance\": \"supports\",\n    \"note\": \"The 'per-' entry of WP II (p.40 in the scan) contains the whole tu-stem family av. pərətu-š, lat. portus/porta, ahd. furt, ags. ford; Pokorny 817 cites 'WP. II 39 f.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. port- (1) 'way, passage, gate'\", \"stance\": \"supports\",\n    \"note\": \"IEC cross-references 'per-, perio (1), poros and pr̥t- (1)' for the same family.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 10.74 BRIDGE\", \"stance\": \"supports\",\n    \"note\": \"'Av. pəšu-, pərətu-, also \\\"ford, passage\\\"; OE ford, OHG furt \\\"ford\\\", Lat. portus \\\"harbor\\\", porta \\\"gate\\\", etc. Walde-P. 2.40.'\"}],\n  \"nodes\": nodes,\n}\n\nout = {\n  \"pdf_page\": 395,\n  \"book_page\": 365,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-395.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-395.py",
 "description": "Build page-395 verification JSON"
}
```


### [2026-09-14T01:06:54.046Z] TOOL RESULT

```
written 17 nodes
```


## [2026-09-14T01:06:56.637Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-395.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 395",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T01:06:57.975Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 13, 'plausible': 3, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'not_checked': 7, 'partial': 1}
books consulted: {'supports': 34, 'contradicts': 3, 'silent': 10, 'partial': 5} | by book: {'KLN': 7, 'HRN': 5, 'BRT': 4, 'WLD': 4, 'SYN': 3, 'CHEUNG': 3, 'PHD': 3, 'NYB': 3, 'DRM': 3, 'KNT': 3, 'MON': 2, 'SKT': 2, 'ARY': 1, 'FVQ': 1, 'BQT': 1, 'LAT': 1, 'WEB': 1, 'AHD': 1, 'HUB': 1, 'POK': 1, 'IEC': 1, 'FSD': 1}
```


## [2026-09-14T01:07:05.257Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"FVQ:\"; grep -ci \"furat\\|euphrat\" FVQ.txt FVQ_pages.txt; echo \"LAT:\"; grep -ci \"euphrat\" LAT.txt; echo \"WEB:\"; grep -ci \"euphrat\" WEB_vol1.txt; echo \"MON rudbar:\"; grep -c \"رودبار\\|جویبار\" MON_part1.txt MON_part2.txt; echo \"SKT sport/passport:\"; grep -n \"^sport\\|^passport\\|^port \" SKT.txt | head; echo \"FSD portare:\"; grep -c \"portare\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt",
 "description": "Verify asserted greps"
}
```


### [2026-09-14T01:07:05.414Z] TOOL RESULT

```
FVQ:
FVQ.txt:3
FVQ_pages.txt:3
LAT:
0
WEB:
1
MON rudbar:
MON_part2.txt:3
MON_part1.txt:8
SKT sport/passport:
13443:passport.    (F.  -  L.)     F. written  permission  to  pass  ifarc &c.  —  r. passer,  to  pass;  fvrUp^ L.  porta  ;  see  Port  (3).
14491:port  <3),  a  gate,  eutrancc.  (F.  — L.)  F. /tfr//.  -  L  porta,  a  gate.  Allied  to  Gk. viS^df,  a  fonl.  way,  and  (o  E.  Fare.  Der. port-er,  V.  poriier,  I*  portarius\  pcrt-ait O.  F.  portal^  Low  v..  tortale,
14492:port  (4),  a  dark  wine.  (Fort.-L.)  Short for  Oporto  wine.  —  Port.  0  porto,  i.  e.  the harbour;  where  o  is  the  del.  art.  (aSpan, A)  =  L.  ilium),  and  porto  U  from  L.  portum, ace.  (^  port  us,  a  harbour.
FSD portare:
FSD_vol3.txt:0
FSD_vol1.txt:0
FSD_vol4.txt:0
FSD_vol2.txt:0
```


## [2026-09-14T01:07:11.928Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ ===\"; grep -n -i \"furat\\|euphrat\" FVQ.txt | head -5; echo \"=== WEB ===\"; grep -n -i \"euphrat\" WEB_vol1.txt | head -3; echo \"=== SKT sport ===\"; grep -n \"sport\" SKT.txt | head -5; echo \"=== FSD port ===\"; grep -n \"L\\. portare\\|portare,\\|portāre\" FSD_vol3.txt | head -5; grep -c \"port\" FSD_vol3.txt",
 "description": "Check the disputed greps"
}
```


### [2026-09-14T01:07:12.073Z] TOOL RESULT

```
=== FVQ ===
1407:Islam. The Arab Kingdom centring in al-Hlra on the Euphrates had 
9276:used for river, e.g. C*J ^Jj the Euphrates. The Phlv. word is 
13884:In any case the word Cj'^ is derived from the river Euphrates 
=== WEB ===
104370:Kii’fic, a. [from Kufa (Ar. al- Kifah) town on the Euphrates, south of Babylon; and -ic.]
=== SKT sport ===
4535:U  st-mruf,  frve  from ,     sport     frora  ;     cum,
5183:^sport ;  see  Port  (i),
5283:DoU  (Du.  or  Gk,)  (1)  Pcrhaoi  from O.  Du.  dol.  a  whippinff  top:  Dn  dolUn.  to sport,  be  frolicsome,  I  fence  perhaps 'a  plav- Ihing.'  See  dally,  onder  Dwell,  (a)  Other- wile,  from  Dell,  for  Dorothy  \  %  familiar name,  of  Gk.  origin.    %  History  obscure.
9523:jocose,  merry.  (LO  L.  ioconUt  sportive. «L.  rWwj,  sport.
9785:same  as  A.  S.  ItU^  a  gam«,  sport,  (
=== FSD port ===
2145
```


## [2026-09-14T01:07:12.769Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"رودبار\" MON_part1.txt | head -5",
 "description": "MON rudbar lines"
}
```


### [2026-09-14T01:07:12.859Z] TOOL RESULT

```
20090:باشد: جویبار (- جوی)» رودبار (- رود). 
68902:رودبار: ۲ (امر.) جایی که در آن 
68911:چند رود جاری باشد؛ رودبار.
```


## [2026-09-14T01:07:21.251Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON bar suffix ===\"; sed -n '20084,20094p' MON_part1.txt; echo \"=== FVQ 13884 ===\"; sed -n '13878,13890p' FVQ.txt; echo \"=== SKT 5180 ===\"; sed -n '5178,5188p' SKT.txt",
 "description": "Context for MON bar, FVQ, SKT"
}
```


### [2026-09-14T01:07:21.363Z] TOOL RESULT

```
=== MON bar suffix ===
انجمن عام؛ مق. بار خاص. با رگاه سراير ده. 
بار: ۱(2.) دفعه» مرتبه» نویت: یک باره ده 
۳۱ 

بار: (پس.) پسوند مکان. به معنی ساحل و 
کنار؛ هندوبار» در یابار. گاه این سوند زاید 
باشد: جویبار (- جوی)» رودبار (- رود). 
بار: 2۲ (۱.) جایی در مهمانخانه با خانه که 
در آنجا مشروب نوشند و مزه خورند. 

بارا ور: 02-2۷27 (افا.) (گیا.) درختی که بار 
=== FVQ 13884 ===
The passages are all Meccan and refer to the sweet river water as 
opposed to the salt water of the sea, and in the two latter passages the 
reference is apparently to some cosmological myth. 

* --> 
I * 
In any case the word Cj'^ is derived from the river Euphrates 

(Horovitz, KU, 130), which from the Sumerian Pura-nun, " great 
water," appears in Akk. as Purattu, or Purdt, 5 and in O.Pers. as Ufrdtu,* 

1 Noldeke, Hand. Gramm., 120, n. 2. 

=== SKT 5180 ===
PS! §1
W
Dispense ;  see  Pendant.
Diaperae ;  Kt  Spkna,
Display:  sec  Ply.
^sport ;  see  Port  (i),
""  spose ;  see  Foae.
DiBposition:  see  Position.
Dispute :  see  Put&iivQ.
Disquisition ;  tee  Query-
Disruption ;  see  Rupture.
```


## [2026-09-14T01:07:22.411Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"passport\" FSD_vol3.txt FSD_vol4.txt FSD_vol1.txt FSD_vol2.txt | head -5",
 "description": "FSD passport"
}
```


### [2026-09-14T01:07:22.477Z] TOOL RESULT

```
FSD_vol3.txt:124907:admittance or convcyutieo, sometimes, u passport, us,
FSD_vol3.txt:124983:— Medlterrmnemn pass, a Mediterranean passport — *••![ * ? . f ; ^ passenger 2. A blnl of passage. I.
FSD_vol3.txt:125041:Ibth and 17th eeiitiines 4 t. A safe-roiiduct . passport
FSD_vol3.txt:125455:with a passport.
FSD_vol3.txt:125461:In the United Htatos passports for foreign travel are is-
```


## [2026-09-14T01:07:36.087Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\ni=txt.find('is derived from the river Euphrates')\nprint('found',i)\nseg=txt[:i]\ntags=re.findall(r'\\[pdf page (\\d+)\\]',seg)\nprint('pdf page',tags[-1] if tags else None)\nprint(txt[i-1200:i+400])\nEOF",
 "description": "FVQ page for furat entry"
}
```


### [2026-09-14T01:07:37.250Z] TOOL RESULT

```
found 463205
pdf page None
 of the other passages.222 FOREIGN VOCABULARY OF THE
and ^'Th/h which is both indicium and sententia iudicis. This sense
had already become domiciled in S. Arabia, as we see from the use of
in the inscriptions (Rossini, Glossarium, 221).
(Fakhkhdr).
Iv, 13.
Potter's clay.
The passage refers to the creation of man, and that it means
earthenware is the general consensus of the authorities (cf. as-Sijistani,
245 ; Kaghib, Mufradat, 380).
It is obvious that it cannot be derived from the verbal root
and Fraenkel, Vocab, 22, compared it with ];**> an earthenware
pot, which occurs as a loan-word in the Jewish ^OHS. 2 The Syr.
!;**> 3 is a word in fairly common use and translates Ktpa/mevs
(cf. l*r**g)? ]*o = yr) Kpa/JitKr)), and there can be little doubt
that it is the origin of the Arabic word, 4 though Horovitz, JPA T , 216,
withholds judgment as to whether it is of Jewish or Christian origin/
> r'
Ol^a (Furdt).
xxv, 55 ; xxxv, 13 ; Ixxvii, 27.
Sweet river water.
The passages are all Meccan and refer to the sweet river water as
opposed to the salt water of the sea, and in the two latter passages the
reference is apparently to some cosmological myth.
* -->
I *
In any case the word Cj'^ is derived from the river Euphrates
(Horovitz, KU, 130), which from the Sumerian Pura-nun, " great
water," appears in Akk. as Purattu, or Purdt, 5 and in O.Pers. as Ufrdtu,*
1 Noldeke, Hand. Gramm., 120, n. 2.
2 Fraenkel, Fremdw, 70 ; but cf. IH^ in Dan. ii, 41.
3 This itself may be of Akk. origin, see Zimmern, Akkad. Fremdw, 26.
Noldeke, Neue Beitrage, 45, n. 2 ; Vollers, ZDMG, h, 324 ; Fraenkel,
```


## [2026-09-14T01:07:44.792Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"portus\" FSD_vol3.txt | head -6",
 "description": "FSD portus"
}
```


### [2026-09-14T01:07:44.854Z] TOOL RESULT

```
97739:1. opporlHHUs, * oh, before, 4 portus harbor | lip^pwr-
125490:paeaeport, < panner (see pass, t ) + port ( L portus), har-
```


## [2026-09-14T01:08:10.535Z] TOOL CALL #91: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\np='data/verification/page-395.json'\nd=json.load(open(p,encoding='utf-8'))\nnodes={n['id']:n for n in d['entries'][0]['nodes']}\n\ndef setc(nid, src, where, stance, note):\n    n=nodes[nid]\n    for c in n['consulted']:\n        if c['src']==src:\n            c.update(where=where, stance=stance, note=note); return\n    n['consulted'].append({\"src\":src,\"where\":where,\"stance\":stance,\"note\":note})\n\nsetc(5,\"FVQ\",\"Jeffery, Foreign Vocabulary of the Qurʾān, p.223, s.v. فرات (Furāt)\",\"contradicts\",\n \"Jeffery's entry فرات (Furāt), Q xxv.55, xxxv.13, lxxvii.27 'Sweet river water': \\\"In any case the word فرات is derived from the river Euphrates (Horovitz, KU, 130), which from the Sumerian Pura-nun, 'great water,' appears in Akk. as Purattu, or Purāt, and in O.Pers. as Ufrātu.\\\" So the Semitic/Sumerian name is primary and the Arabic (hence Persian) word comes from it — not from an Iranian *hu-parəθβa-.\")\n\nsetc(5,\"BQT\",\"Borhān-e Qāṭeʿ (Moʿin ed.)\",\"silent\",\n \"فرات is an Arabic proper name and gets no Persian etymology in the Borhān material consulted (grep of the پ/ف leaves); Moʿin's footnotes give no Iranian origin for it.\")\n\nsetc(11,\"MON\",\"Moʿin, Farhang-e Fārsi, s.v. بار (4th homonym)\",\"supports\",\n \"MON_part1.txt line ~20089: 'بار: (پس.) پسوند مکان. به معنی ساحل و کنار؛ هندوبار، دریابار. گاه این پسوند زاید باشد: جویبار (= جوی)، رودبار (= رود).' — Moʿin registers -bār as a place-forming suffix meaning 'shore, edge', with Nourai's own examples.\")\n\nsetc(8,\"WEB\",\"Webster's New Twentieth Century Dict., 2nd ed.\",\"silent\",\n \"grep -i 'euphrat' in WEB_vol1.txt gives a single incidental mention (s.v. Kufic, 'town on the Euphrates'); Webster has no etymological entry for the river name itself.\")\n\nsetc(17,\"SKT\",\"Skeat, Concise Etym. Dict., s.v. Disport, passport, port (3)\",\"supports\",\n \"SKT.txt line 5183 'Disport; see Port (1)' (so sport is aphetic for disport); line 13443 'passport. (F.-L.) F. passeport, written permission to pass ... F. passer, to pass; L. porta; see Port (3)'; line 14491 'port (3), a gate, entrance. (F.-L.) F. porte. — L. porta, a gate. Allied to Gk. πόρος, a ford, way, and to E. Fare.'\")\n\nsetc(17,\"FSD\",\"Funk & Wagnalls New Standard Dict., vol. 3\",\"supports\",\n \"FSD_vol3.txt line 125490 s.v. passport: '< F. passeport, < passer (see pass) + port (< L. portus), harbor'; line 97739 s.v. opportune: '< L. opportunus, < ob, before, + portus, harbor'.\")\n\nsetc(15,\"SKT\",\"Skeat, s.v. port (3)\",\"supports\",\n \"SKT.txt line 14491: 'port (3), a gate, entrance. (F.-L.) F. porte. — L. porta, a gate ... Der. port-er, F. portier, L. portarius; port-al, O.F. portal, Low L. portale' — the Latin→French→English route for the whole set.\")\n\n# node 7 LAT: confirm grep result wording\nfor c in nodes[7]['consulted']:\n    if c['src']=='LAT':\n        c['note']=\"grep -ci 'euphrat' LAT.txt returns 0 — Ernout-Meillet treat only Latin appellatives, not the Greek-mediated river name.\"\n\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write('\\n')\nprint('patched')\nPYEOF\npython3 -m json.tool data/verification/page-395.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 395",
 "description": "Patch consulted entries and re-validate"
}
```


### [2026-09-14T01:08:11.812Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 13, 'plausible': 3, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'not_checked': 7, 'partial': 1}
books consulted: {'supports': 35, 'contradicts': 4, 'silent': 8, 'partial': 5} | by book: {'KLN': 7, 'HRN': 5, 'BRT': 4, 'WLD': 4, 'SYN': 3, 'CHEUNG': 3, 'PHD': 3, 'NYB': 3, 'DRM': 3, 'KNT': 3, 'MON': 2, 'SKT': 2, 'ARY': 1, 'FVQ': 1, 'BQT': 1, 'LAT': 1, 'WEB': 1, 'AHD': 1, 'HUB': 1, 'POK': 1, 'IEC': 1, 'FSD': 1}
```


## [2026-09-14T01:08:31.667Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-395.json` written; `verify_check.py 395` reports **0 PROBLEM lines** (17/17 nodes).

**Page 395 (book p. 365), single entry: ROOT "Per 2" [Indo-European] — root verdict `confirmed`**

Node verdicts: confirmed 13 · plausible 3 · disputed 1
Ref checks: supports 12 · partial 1 · not_checked 7 (AEF and the 1975 AHD main dictionary are not accessible; the empty pass-through nodes carry `refs=None`).

- **`disputed` — #5 Persian forāt «فُرات»**: not an Iranian inheritance. It is a loan from Arabic الفُرات, itself from Akkadian *Purattu* (Sumerian Buranuna). Jeffery, *Foreign Vocabulary of the Qurʾān* p.223 s.v. فرات says so verbatim; Wiktionary derives Persian فرات ← Arabic ← Akkadian.
- `plausible` — #4 Avestan "hu-parathwa": not an attested Avestan word (Bartholomae has hu-parəna-, hu-paurva- … but no *hu-parəθβa-); the attested form is Old Persian *Ufrātu-*, and Kent calls the whole equation "probably a popular etymologizing in OP of a local non-Iranian name".
- `plausible` — #6 Greek Euphrates: route Iranian→Greek is right, but the source is OP *Ufrātu-*, not Avestan.
- `plausible` — #16 Persian پاسپورت/ترانسپورت/اسپرت: Moʿin tags پاسپورت [فر.] (French), but اسپرت may have come via English/Russian; the other two are not in the Moʿin volumes on disk.

No transcription-suspect nodes and **no extraction errors** — the JSON faithfully reproduces the chart.

Strongest confirmations found in the local library: Pokorny 816–817 (`per-2 B`) has *pərətu-*, *hu-parəθwa-* and Latin *porta/portāre* in one entry, and its **addendum to p.817 is printed on p.850** — which is exactly why Nourai cites "POK:817,850" for *parəna-* (Cheung, EDIV, cites the same Pok. 850 Nachtrag). Klein p.1220–21 s.v. *port* cites "Avestic peretush"; Nyberg's glossary gives Av. pərətu- > MP puhl > NP pul; Darmesteter *Études iraniennes* I §237 (p.286, the page Nourai cites) gives par → parvāna, and §244 (p.289) derives the suffix -bār from Avestan pāra- with Nourai's exact example list.

One citation slip: **BQT:397** for پر — the Borhān headword پر sits ~20 printed pages earlier; p.397 falls on the پری/پریدن leaves (the derivative Nourai lists as "extra"). Recorded as `partial`, not an error worth fixing in the data.
